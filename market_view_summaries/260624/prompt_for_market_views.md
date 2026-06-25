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
    "title": "摩根斯坦利：MS：新美联储的“沉默”本身就是最响亮的信号",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：新美联储的“沉默”本身就是最响亮的信号\n\n这份来自MS全球宏观论坛的报告，核心判断并非关于加息终点或降息时点，而是指向一个更深层的结构性变化：美联储正在主动退出“预期管理”的角色，将定价权交还给市场。对于习惯了“看美联储脸色”做交易的投资者而言，这意味着一套全新的游戏规则正在建立。\n\n报告由MS首席固定收益策略师Vishwanath Tirupattur领衔，联合首席全球经济学家Seth Carpenter、全球宏观策略主管Matthew Hornbach、首席美股策略师Michael Wilson等核心团队共同撰写。它不只是一份市场展望，更像是一份“新美联储操作手册”的导论。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新主席Warsh的“沉默策略”正在重塑市场定价逻辑\n\n报告明确指出，新任美联储主席Warsh有意在沟通中减少“前瞻指引”。他认为，减少对市场的前瞻性引导是其政策思路的核心。这种做法与他的前任们形成了鲜明对比。过去十年，市场习惯了从每一次FOMC会议声明、每一次记者会中寻找关于未来利率路径的蛛丝马迹。现在，这种“确定性”正在被主动撤回。\n\n然而，市场的反应却耐人寻味。尽管Warsh明确表示希望避免任何像前瞻指引的暗示，市场却将他“没有对当前定价进行反驳”的行为，解读为一种默许。结果就是，市场定价反而更加紧密地追随了点阵图。这构成了一种新的博弈：美联储不再告诉你它会怎么做，但它不纠正你，就意味着它认可你的判断。\n\n> **KC评论：** 这相当于美联储把方向盘交给了市场，但又没有完全撒手。投资者需要从“猜美联储想什么”转向“猜市场如何猜美联储”。这种二阶博弈的复杂度，远高于过去。完整报告里包含了对SOFR曲线平坦化交易的详细论证，以及为什么在当前环境下，曲线平坦化比直接做空利\n\n[... middle omitted ...]\n\n星球和微信群里，继续讨论这份报告背后那些尚未完全展开的细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新美联储，旧剧本？研报划重点\n\n美联储换帅后的信号\n\n新主席Warsh的沟通策略，市场听懂了什么？\n\n最近某外资投行出了一份美联储宏观论坛纪要，信息量很大。我提炼了几个关键判断，跟你们聊聊。\n\n1️⃣ 新主席的“去指引”策略\n新主席Warsh有意减少“前瞻指引”，认为这才是他的核心方法。他明确表示“委员会将实现价格稳定”，但刻意不画路径图。研报判断：一年后的美联储，在沟通方式和缩表规模上会变化很大，但在利率政策上的变化不会那么剧烈。\n\n2️⃣ 市场波动率要上升了\n主席的讲话暗示：利率波动率会更高，宏观市场的信号功能会更强。市场把Warsh没有反驳当前定价，解读为可以更接近点阵图来定价。研报建议：继续推荐SOFR曲线 flatteners（平坦化交易），因为联储可能跟随市场定价。\n\n3️⃣ 战术性看空抵押贷款\n原因有三：减少前瞻指引导致长期波动率上升；收益率曲线bear flattening会减少银行需求；外汇对冲成本可能维持高位。研报建议：战术性做空FNCL 5.5s vs 利率债，同时喜欢“长波动率+短抵押贷款”的组合。\n\n4️⃣ 权益市场的视角\n新主席放弃前瞻指引、更依赖市场信号，会提升美联储决策的质量和\n\n[... middle omitted ...]\n\n. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making t\n\n[... middle omitted ...]\n\ny Wharf  \nLondon E14 4AD  \nUnited Kingdom  \n+44 (0)20 7425 8000\n\nJapan  \n1-9-7 Otemachi, Chiyoda-ku  \nTokyo 100-8104  \nJapan  \n+81 (0) 3 6836 5000\n\nAsia/Pacific  \n1 Austin Road West  \nKowloon  \nHong Kong  \n+852 2848 5200"
  },
  {
    "id": "R002",
    "title": "GS：亚洲太空经济正在从“故事”转向“订单”，但市场定价仍落后60%",
    "digest": "[wechat_article.md]\n# GS：亚洲太空经济正在从“故事”转向“订单”，但市场定价仍落后60%\n\n这份GS最新发布的亚洲太空经济专题报告，核心判断并不复杂：全球太空经济正从概念验证进入大规模部署阶段，而亚洲供应链公司在这一轮部署中扮演着不可替代的硬件核心角色。但市场对这些公司的定价，仍然停留在“概念主题”阶段，而非“盈利交付”阶段。\n\n报告最值得关注的信号，不是太空经济的长期增长数字——那些已经足够震撼，LEO卫星市场预计到2035年增长7倍至1080亿美元——而是三个更具体的、对投资者有直接含义的发现：\n\n第一，亚洲太空经济股票相对于全球同行的市盈率折价高达60%，市净率折价25%，且这一折价水平处于历史区间的低位附近。第二，全球太空主题基金和ETF的资产管理规模已经从2025年初的约10亿美元飙升至峰值约250亿美元，但亚洲供应链公司在这些基金中的配置比例仍然极低。第三，亚洲太空经济股票自2025年以来已经跑赢更广泛的区域市场，但在过去三个月进入盘整区间，而全球同行仍在上涨。\n\n这意味着什么？如果太空经济确实在进入一个由订单和收入支撑的部署周期，那么亚洲供应链公司目前被低估的程度，可能提供了一个罕见的、基本面与定价之间存在系统性错位的窗口。\n\n这份报告由GS亚洲策略团队Alvin So、Timothy Moe、Kinger Lau等多位分析师联合撰写，于2026年6月发布。它不仅仅是一份行业扫描，更是一份带有明确投资主张的“买入框架”。以下是我们从报告中提炼出的五个核心洞察。\n\n> **KC评论：** 报告的核心主张是“亚洲太空经济股票被低估”，但支撑这一主张的关键证据——60%的市盈率折价——需要结合报告中的具体拆解来理解。折价本身并不自动意味着机会，关键在于折价是否被基本面恶化所解释。GS认为不是，因为盈利势头仍然积极。这正是完整报告中最值得细读的部分：分国家、分环节的盈\n\n[... middle omitted ...]\n\n讨论，一起跟踪太空经济这一正在从主题走向基本面的结构性机会。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲太空经济，为什么现在值得研究\n\n太空经济进入部署期\n\n最近看了份某外资投行的研报，专门讲亚洲太空经济供应链的机会。几个关键数据值得记录：\n\n1️⃣ 部署速度惊人\n2025年全球发射卫星4400+颗，同比增65%。未来5年还有约7万颗卫星计划发射。LEO（低轨）卫星市场预计到2035年增长7倍，达1080亿美元。\n\n2️⃣ 亚洲是硬件核心\n从卫星平台、火箭发动机到射频芯片、相控阵天线，亚洲是全球太空供应链的硬件脊梁。中国、日本、韩国、台湾、印度各有分工，且都有政府订单支撑。\n\n3️⃣ AI+太空正在融合\n地面能源和审批限制推动“轨道AI计算”进入采购阶段。AI基础设施投资与太空经济的关联，让这个主题的持续时间更长了。\n\n4️⃣ 资金在加速流入\n全球太空主题基金/ETF的规模从2025年初的约10亿美元，已膨胀到峰值约250亿美元。但亚洲供应链公司在这些基金中的配置明显不足——基本面与资金流向之间存在缺口。\n\n5️⃣ 估值有吸引力\n亚洲太空经济股票相对全球同行：市盈率折价60%，市净率折价25%，处于历史低位区间。而盈利增长趋势依然向好。\n\n研报还按“核心/成熟”和“早期增长/新兴”两个维度拆解了产业链。核心\n\n[... middle omitted ...]\n\ny in funded execution through 2028, providing non-discretionary demand independent of end-user adoption.\n\nAsia's role in the global supply chain is critical. Asia represents the hardware backb\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "摩根斯坦利：MS：日本股市的结构性牛市才刚刚进入第二幕",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：日本股市的结构性牛市才刚刚进入第二幕\n\n当全球投资者还在争论日本经济能否走出“失去的三十年”时，MS用一份夏季策略会报告给出了一个更激进的判断：日本股市正在进入一个结构性转折点，而支撑这个判断的四大驱动力——通胀稳定、政策加速、治理改革、居民入场——都在同步强化。\n\n这不是一个简单的周期性反弹故事。MS对TOPIX的基准目标价是2027年6月底达到4,300点，较当前水平约有8%的上涨空间。但真正值得关注的不是这个数字，而是报告提出的一个核心逻辑：日本股市正在从“低通胀、低传导、低利润”的旧范式，切换到一个全新的定价框架。在这个新框架下，历史估值区间不再构成上限。\n\n对于中国投资者而言，理解这个切换，远比纠结于短期汇率波动或中东油价冲击更重要。因为这意味着日本资产在全球配置中的角色正在发生根本性变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 通胀不再是威胁，而是日本股市最坚实的结构性支撑\n\n过去三十年，日本投资者最怕听到的两个字就是“通胀”。通缩思维深植于企业定价行为、居民消费习惯和资产配置逻辑中。但MS认为，日本正在进入一个“更稳定、更可持续”的通胀环境，而这一变化正在从根本上改变企业行为。\n\n报告的核心论据是产出缺口正在逐步收窄。当经济不再有闲置产能，企业开始具备定价权，工资上涨开始传导至终端价格，形成一个正向循环。这听起来像是宏观教科书的标准叙述，但放在日本语境下，这是一个历史性的转变。\n\n从数据上看，日本企业已经在行动。报告指出，自疫情后经历进口价格飙升以来，日本企业持续致力于改善利润率。这意味着即使日元升值，企业盈利的脆弱性也比过去大幅降低。一个关键证据是：美元兑日元与日本股市的正相关性在过去十年中持续下降，日元不再是日本企业盈利的唯一驱动因素。\n\n> **KC评论：** 这\n\n[... middle omitted ...]\n\n分析图表，以及后续的市场验证信号，欢迎来我们的社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本股市的四个结构性支撑点\n\n📈 日本股市为什么能持续走强？\n\n某外资投行最新研报分析了日本股市的长期结构性故事，逻辑链条挺清晰👇\n\n1️⃣ 通胀走向稳定\n日本正从通缩转向2%通胀目标，企业定价能力增强、工资上涨、资本开支回升。这个转变不是短期的，是结构性的。\n\n2️⃣ 政策确定性提升\n执政联盟大胜后，增长策略的执行力更强。政策可预测性提高，对中期盈利预期和风险溢价都是正面信号。\n\n3️⃣ 公司治理改革加速\n2022年东证市场改革后，Prime市场PBR已涨约40%。2026年预计有治理准则修订，推动企业更有效使用现金。ROE提升空间还在。\n\n4️⃣ 家庭资金入市\nNISA免税账户推动日本家庭从储蓄转向股票。2027年还计划推出“Kids NISA”，未成年人每年可免税投60万日元。\n\n💡 研报对TOPIX的基准目标：2027年6月4300点。核心逻辑是：通胀预期+国家安全溢价+AI投资周期，正在推动市场向“实物资产”模式切换。\n\n⚠️ 当然，风险也在。中东局势若升级导致油价飙升，可能触发全球衰退，TOPIX估值可能压缩到12倍PE。但基准情景假设地缘风险可控。\n\n有意思的是，研报认为日元汇率不再是日本股市的\n\n[... middle omitted ...]\n\nmine how these structural developments are supporting the long-term upward trajectory of Japanese equities, while also highlighting the near-term and cyclical themes that investors should watc\n\n[... middle omitted ...]\n\nperformance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS MUFG"
  },
  {
    "id": "R004",
    "title": "UBS：霍尔木兹海峡的VLCC运价已不是关键，集装箱的“前置抢运”才是",
    "digest": "[wechat_article.md]\n# UBS：霍尔木兹海峡的VLCC运价已不是关键，集装箱的“前置抢运”才是\n\n全球航运市场的目光正集中在霍尔木兹海峡的恢复通行上。UBS最新发布的周度航运供应链报告给出了一个反直觉的判断：VLCC运价的短期飙升是事件性的，真正值得关注的、且已经在高频数据中显现的结构性变化，是亚洲至美国航线的集装箱“前置抢运”正在加速。这轮运价的上涨，其驱动力正在从“绕航”切换为“抢运”，其影响深度和持续性可能远超市场预期。\n\n这份报告的价值不在于复述海峡通航的新闻，而在于它利用UBS Evidence Lab的高频数据，提供了一套区分“噪音”与“信号”的观测框架。对于关注全球贸易、航运资产、以及供应链韧性的决策者而言，理解这个信号切换，比猜测下一周运价的涨跌更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹的恢复是“假摔”信号，真正的运价支撑来自大西洋的“抢油”\n\n报告中最直接的冲击来自VLCC。数据显示，上周中东至中国的VLCC平均收益飙升了87%，达到约19.5万美元/天。这个数字看起来很惊人，但UBS的解读非常克制：这更多是“预期”的体现，即市场预期波斯湾重新开放后，会有大量油轮涌入装载货物，导致短期运力紧张。\n\n然而，报告中的另一组数据揭示了更底层的逻辑。VLCC一年期期租费率保持稳定。这意味着，真正的产业资本（需要长期锁定运力的炼油厂或贸易商）并未恐慌。现货市场的飙升，更多是投机性运力与短期补库需求的一次性冲高。一旦首批货物装运完毕，运价将迅速回归。\n\n> **KC评论：** 这提醒我们，不能把事件驱动的脉冲式上涨，误判为周期的反转。UBS报告里没有明说但值得追问的是：如果中东恢复，那批从大西洋绕道好望角的VLCC会如何？它们会形成新的运力冗余，对运价构成下行压力。要理解这背后的二阶效应，需要完整阅读报告\n\n[... middle omitted ...]\n\n“前置抢运”的规模感兴趣，欢迎来我们的星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹重启，油轮运价飙升\n\n航运数据周报\n\n一周航运关键变化全拆解\n\n最近某外资投行更新的航运高频数据，信息量挺大。霍尔木兹海峡通航恢复、集装箱运量持续走高、散货船市场有所降温，几个关键节点都在变化。\n\n1️⃣ 霍尔木兹重启，VLCC运价跳涨\n- 上周日均通过霍尔木兹的船舶回升至25艘，之前只有10艘左右，但距离冲突前125艘的水平还差得远。\n- 油轮一窝蜂涌向波斯湾，即期运价应声飙升。中东/西非到中国的VLCC平均日收益涨了87%，达到约19.5万美元/天。\n- 研报数据还显示，上周五以来，从霍尔木兹向东航行的油轮明显增多。\n\n2️⃣ 集装箱运量持续上升\n- 国内主要港口集装箱吞吐量环比+3%，同比+2%。\n- 主要航线运价继续走高：SCFI综合指数环比+5%，同比+67%；上海-欧洲线环比+3%；跨太平洋线环比+9-11%。\n- 亚洲-美国航线集装箱运量自5月以来同比强劲增长，可能和部分企业提前备货有关。\n\n3️⃣ 散货船市场降温，新船造价维持高位\n- BDI指数环比下降4%，但好望角型船平均收益反而环比+11%，BDI年初至今仍累计上涨43%。\n- 新造船价格指数环比持平，VLCC和LNG船需求依然旺\n\n[... middle omitted ...]\n\nct level of 125. An initial rush for VLCC to the Persian Gulf has resulted in a spike in spot rates, while most operators are still waiting to monitor the progress of the release of vessels in\n\n[... middle omitted ...]\n\nng number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R005",
    "title": "NOM：日本加息周期已过中点，但市场真正该关注的是财政牌",
    "digest": "[wechat_article.md]\n# NOM：日本加息周期已过中点，但市场真正该关注的是财政牌\n\n当全球投资者的目光仍聚焦于日本央行何时结束负利率、加息路径是否被打断时，NOM在最新一期《日本经济周报》中给出了一个值得细品的判断：日本央行的加息周期可能已经走过了一半。更关键的是，随着6月货币政策会议尘埃落定，市场关注重心正从央行转向政府——增长战略与消费税减税将成为决定日本资产定价的下一个变量。\n\n这份报告的核心信号并不复杂：日本经济、物价和金融条件三者目前都支持继续加息。但NOM同时指出，真正需要投资者警惕的，不是加息本身，而是财政政策的不确定性，尤其是消费税减税方案的资金来源与推进节奏。后者可能比加息更深刻地影响日本内需、通胀路径和国债定价。\n\n以下是这份NOM研报的核心洞察与延伸思考。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 加息周期已过中点，但终点线可能比市场预期的更近\n\nNOM在报告中明确写道：“我们认为，日本央行可能已经过了本轮加息周期的中点。” 这一判断基于三个关键信号：一是政策委员会成员Asada投下反对票，暗示鸽派力量正在集结；二是央行对经济风险的评估出现微妙变化，认为“经济显著放缓的风险相比此前有所下降”；三是央行在措辞上删除了“实际利率处于极低水平”的表述，代之以“金融条件一直宽松”。\n\n> **KC评论：** 措辞调整看似微小，但信号意义很强。央行主动降低对宽松程度的评估，意味着未来加息的理由将更依赖数据而非“补涨”逻辑。这对市场意味着，加息节奏可能从“追赶式”转向“确认式”，每一次加息都需要更强的通胀或增长数据支撑。\n\nNOM维持其基准情景：2026年12月和2027年6月各加息一次，共两次。风险情景则是在此基础上再加一次，时间点落在2026年10月、2027年3-4月和9-10月。无论哪种情景，加息周期的终点都指\n\n[... middle omitted ...]\n\n球微信群继续讨论，每天获取最新的国际投行中文摘要与KC评论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本央行还要加息吗？看懂这三个信号就够了\n\n📌 日本央行加息进度条\n\n6月16日，日本央行把政策利率从0.75%提到1.0%。这次加息本身不意外，但背后有三个信号值得关注。\n\n1️⃣ 内部已有反对声音\n政策委员Asada投了反对票，新上任的Sato可能也偏鸽。但研报认为，这轮加息周期大概率在2027年中后期结束，不影响大方向。\n\n2️⃣ 对通胀风险的评估变了\n央行认为“核心CPI有向上偏离2%目标的风险”，这为继续加息提供了理由。预计2027年Q1通胀见顶。\n\n3️⃣ 金融条件依然宽松\n贷款增速达6% y-y，房贷需求也在上升。说明政策利率仍低于中性利率，加息空间还在。\n\n📌 中东局势缓和≠供应恢复\n虽然美伊签了谅解备忘录，但霍尔木兹海峡的油轮通行量几乎为零。原油进口量和制造业原材料延迟情况，才是真正需要盯的指标。\n\n📌 财政政策成为新焦点\n6月底将公布增长战略和消费税减税方案。增长战略委员会计划到2040年实现公私投资约370万亿日元，每年约26万亿，是GX政策的1.8倍。\n\n消费税方面，LDP提案：2027年起食品饮料税率降至1%，2027-2028年秋季发放现金补贴。但反对党强烈反对，最终方案还有变数。\n\n[... middle omitted ...]\n\nts. Nevertheless, we think these three factors (the economy, prices, and financial conditions) favor more rate hikes.\n\n2. Domestic policy (government): Focus in late June likely to be on growt\n\n[... middle omitted ...]\n\n listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved."
  },
  {
    "id": "R006",
    "title": "UBS：黄金正处在“无人区”，但这次和2013年不一样",
    "digest": "[wechat_article.md]\n# UBS：黄金正处在“无人区”，但这次和2013年不一样\n\n黄金正陷入一场罕见的僵局。\n\n一方面是实际利率飙升、市场持续定价加息，金价承压明显；另一方面，央行购金、私人部门多元化配置、以及不断膨胀的美国债务，又在底部提供着结构性支撑。UBS在最新发布的贵金属研报中，用一个精准的比喻描述了这种状态：“precious metals navigate no-man's land”——贵金属正穿行于一片无人区。\n\n这份研报的核心判断是：黄金的短期风险确实在上升，但长期逻辑并未被打破。真正值得关注的，不是金价会跌多少，而是这一轮调整结束之后，谁会率先重新入场。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮调整与2013年有本质不同，市场恐慌程度被高估了\n\n许多投资者看到金价回调，第一反应是翻出2013年4月黄金崩盘的记忆。当时金价单年下跌29%，背后是美联储货币政策正常化的预期转向、塞浦路斯央行抛售黄金的恐慌蔓延，以及实际利率由负转正的重大拐点。\n\nUBS在报告中专门做了一组对比分析，结论很清晰：2026年的宏观环境与2013年存在根本性差异。\n\n2013年黄金面临的是“货币政策体制转换”——美联储从极度宽松转向退出QE，实际利率从负值区域翻正，这对零息资产的打击是致命性的。而当前，美联储才刚刚完成175个基点的降息周期，处于“暂停观察”状态，政策方向仍偏向宽松。实际利率虽然也在上升，但起点和幅度都远不及2013年。\n\n更重要的是，2013年市场担心的核心问题是“央行会不会集体抛售黄金”，而今天市场的担忧恰恰相反——央行购金仍在持续，只是买家结构在发生变化。2013年全球通胀处于下行通道（从2.0%降至1.0%），而当前通胀从2.7%升至4.2%，这本身就是黄金的长期利好。\n\n> **KC评论：** UBS这张对\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n金价在等一个信号📉\n\n夏天来了，金价在横盘\n\n贵金属进入“无人区”，短期承压但长期逻辑不变\n\n最近金价被利率压得有点喘不过气，市场还在预期加息。但投行研报说，这次和2013年那轮熊市不一样。\n\n**1/ 短期压力是真实的**\n- 实际利率走高 + 美元走强 = 金价承压\n- 市场情绪偏弱，夏天交易量本来就清淡\n- 但对比2013年，当时通胀在下降（2%→1%），现在通胀在上升（2.7%→4.2%），背景完全不同\n\n**2/ 长期支撑还在**\n- 美联储预计2027年开始降息（研报预测路径）\n- 美国债务/GDP超137%，财政可持续性成长期担忧\n- 央行购金趋势没变，只是买家换了一批——2022年是波兰、土耳其，2026年新增了其他官方机构\n- 亚洲占实物投资需求超70%，散户和机构都在买\n\n**3/ 白银铂金跟着金价走，但需求有拖累**\n- 白银有AI、新能源、电动车故事，但短期工业需求放缓会拖累表现\n- 铂金和钯金受汽车需求疲软影响更大\n- 钯金还要面对电动车市占率上升的压力（中国出口平价电动车在增加）\n- 白银和铂金在金价上涨时更容易吸引资金流入\n\n**4/ 几个值得关注的风险**\n- 美国经济数据如果\n\n[... middle omitted ...]\n\nprofile may be pushed out, with greater uncertainty on how long the current consolidation might extend. Economic data prints out of the US will be a key focus in the coming months, with any si\n\n[... middle omitted ...]\n\nlements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R007",
    "title": "Bernstein：数据中心每兆瓦值多少钱，答案藏在商业模式里",
    "digest": "[wechat_article.md]\n# Bernstein：数据中心每兆瓦值多少钱，答案藏在商业模式里\n\nAI基础设施的军备竞赛中，一个核心问题始终困扰着投资者：当一家数据中心或GPU云公司签下一份合同，这到底是一笔好交易吗？市场往往被“数十亿美元”“数万兆瓦”这类宏大数字吸引，却忽略了单位经济学的根本差异。\n\nBernstein最新发布的研究报告，提供了一个极为实用的分析框架：每兆瓦（MW）能产生多少收入。这个看似简单的指标，在拆解不同商业模式后，揭示出惊人的差异——从不到100万美元到超过5500万美元。差异本身不是答案，理解差异背后的结构性原因，才是判断哪些公司真正拥有护城河的关键。\n\n这份报告的核心判断是：对于规模尚未达到临界点的提供商，Bernstein继续偏好托管模式（colo model）而非GPU云模式（neocloud model）。但报告同时指出，当GPU云公司拥有自有房地产时，部分合同同样具有吸引力。\n\n这不是一个简单的“谁更好”的结论，而是一个关于商业模式选择、资本配置能力和风险回报权衡的深度分析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 收入密度差异背后，是商业模式对价值链的不同截取\n\nBernstein将数据中心相关公司划分为三类，每类在每兆瓦收入上呈现清晰的阶梯状分布。\n\n第一类是传统托管REITs。Equinix以约500万美元/兆瓦位居首位，这得益于其零售导向模式——不仅出租机柜空间，还叠加了网络互联服务和高价值收入。Digital Realty和CoreSite等更偏向批发模式的公司，收入密度在300万至400万美元/兆瓦之间。新兴AI基础设施提供商（如WULF、CIFR）则更低，主要因为它们在偏远地区预建未完成的项目。\n\n第二类是GPU云公司。CoreWeave的收入密度达到2080万美元/兆瓦，Nebi\n\n[... middle omitted ...]\n\n心行业的投资机会有更深入的兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心一兆瓦到底值多少钱？\n\n一兆瓦的价值，差50倍\n\n最近大家都在讨论GPU云和托管合同，今天来拆解一下每兆瓦到底能产生多少收入💰\n\n**1/ 托管模式 vs GPU云模式**\n托管就像房东出租毛坯房，收稳定租金\nGPU云则是精装修后做酒店，卖的是服务\n\n托管：每兆瓦收入300-500万美元\nGPU云：每兆瓦收入800-2000万美元\n差距主要来自服务叠加的深度\n\n**2/ 成本结构完全不同**\n托管：资产重但运营轻，电费大部分转嫁客户\nGPU云：资产更重，还要承担GPU折旧、软件、工程团队成本\n\n托管运营成本每兆瓦约220万美元\nGPU云则高达1860-3330万美元\n虽然收入高，但投入也大\n\n**3/ 谁在赚真正的钱？**\nEquinix每兆瓦收入500万美元，利润率66%\nDigital Realty收入340万美元，利润率仅8%\n差距在于零售vs批发模式\n\nGPU云公司CoreWeave利润率约10.8%，还处在扩张烧钱阶段\n\n**4/ 新兴AI基础设施玩家**\n前矿工转型的CIFR、WULF、CORZ\n签10-15年长期合同，每兆瓦收入175万美元\n但利润率高达85%，因为几乎零运营成本\n\n**\n\n[... middle omitted ...]\n\ned22.jpg)\n\nMadison Rezaei\n+1 917 344 8622\nmadison.rezaei@bernsteinsg.com\n\nGautam Chhugani\n+91 226 842 1416\ngautam.chhugani@bernsteinsg.com\n\nNancy Wu\n+1 917 344 8545\nnancy.wu@bernsteinsg.com\n\nM\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R008",
    "title": "UBS：当炼厂开工率跌至45%，化工行业下一个机会在AI制冷剂",
    "digest": "[wechat_article.md]\n# UBS：当炼厂开工率跌至45%，化工行业下一个机会在AI制冷剂\n\n中国化工行业正在经历一轮罕见的“双低”震荡：原油库存自6月初持续下降，地方炼厂开工率已跌至45.74%，而聚酯、聚丙烯等主要化工品的产能利用率同比下滑幅度普遍在10个百分点以上。市场弥漫着对需求疲软的担忧，但UBS最新发布的化工周报给出了一条清晰的差异化路径——当传统化工品陷入库存与开工率的双重压力时，AI算力驱动的含氟化学品需求正在打开一个被低估的定价空间。\n\n这份报告的核心判断是：市场尚未充分定价AI对氟化学材料带来的结构性增长机遇，部分氟化工企业存在明确的估值重估潜力。而这一判断的逻辑，需要从当前化工行业最真实的运营数据说起。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 炼厂开工率持续下滑，原油库存降至年内低位，但这不是系统性危机\n\nUBS周报数据显示，截至上周，中国主营炼厂开工率小幅回升0.23个百分点至67.41%，但地方炼厂开工率环比大幅下降2.9个百分点至45.74%。中国原油总加工量环比下降12.8万桶/日，至1232.1万桶/日。与此同时，根据Kpler数据，中国原油库存自6月初以来持续下降，截至6月22日已降至12.68亿桶。\n\n这两个数据放在一起看，容易让人联想到需求崩塌。但UBS的解读更克制：开工率分化本身说明问题不在总量，而在结构。主营炼厂开工率相对稳定，地方炼厂则面临更为严峻的利润压力和原料获取能力差异。原油库存下降叠加开工率走低，更多反映的是炼厂主动去库存和调节开工节奏，而非终端需求的全面失速。\n\n> **KC评论：** 这个地方最容易被误读。很多人看到开工率45%就会联想到“行业萧条”，但UBS把主营炼厂和地方炼厂分开看，就是为了说明这轮压力更多集中在成本传导能力弱、议价权低的环节。对于下游化工品而言，原料端的\n\n[... middle omitted ...]\n\n微信群里继续讨论，把这份报告的完整逻辑和数据链条一起过一遍。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n炼厂开工率还在降，氟化工是AI新方向\n\n📉 开工率持续下降\n\n上周国内炼厂总开工率继续走低，数据不太乐观：\n- 地炼（teapot refinery）开工率已降至45.74%，环比跌了2.9个百分点\n- 国企炼厂开工率67.41%，微涨0.23个百分点\n- 国内原油加工量周环比减少12.8万桶/天\n- 原油库存从6月初开始持续下降，截至6月22日为12.68亿桶\n\n🧪 化工各细分领域分化明显\n\n1️⃣ 聚酯链压力大\n- 涤纶长丝开工率74%，同比下滑15个百分点\n- PTA开工率69%，同比下滑13个百分点\n- PX开工率77%，同比下滑8个百分点\n\n2️⃣ 烯烃类相对平稳\n- 石脑油制乙烯开工率稳定在76%\n- PE开工率80%，同比微降1%\n- PP开工率63%，同比大降15%\n\n3️⃣ 聚氨酯有亮点\n- TDI开工率环比上升7个百分点至71%\n- MDI开工率82%，环比微降1%\n\n📦 库存数据：多品种去库存\n\n- PP库存45.2万吨，同比降26%\n- PE库存47.6万吨，同比降5%\n- PVC库存41.5万吨，同比降21%\n- 有机硅DMC库存4万吨，同比降21%\n- 涤纶长丝库存同比大增112%\n\n[... middle omitted ...]\n\n declined 2ppt/15ppt WoW/YoY\n\nEthylene: Naphtha-based ethylene utilisation was broadly flat WoW at 76%, while MTO route utilisation declined 5ppt/11ppt WoW/YoY to 78%. Polyolefins: PE utilisat\n\n[... middle omitted ...]\n\nng number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R009",
    "title": "GS：印度电缆与EMS公司正经历一轮“成本驱动型”收入修复",
    "digest": "[wechat_article.md]\n# GS：印度电缆与EMS公司正经历一轮“成本驱动型”收入修复\n\n印度资本市场正在迎来一轮财报季预热。GS在最新发布的印度电缆与电子制造服务（EMS）行业前瞻报告中，给出了一个清晰且反直觉的判断：即将到来的第一季度（Q1FY27）收入增长，主要驱动力不是需求爆发，而是上游原材料价格上涨带来的价格传导与渠道补库存。对于关注印度制造业、供应链转移以及新兴市场资产定价的读者来说，这份报告的价值不在于预测具体数字，而在于它揭示了一个关键的结构性信号——当成本通胀成为收入增长的核心引擎时，企业的盈利质量、估值逻辑和投资风险都会发生微妙但重要的变化。\n\n报告覆盖四家公司：电缆领域的Polycab India（中性评级）和KEI Industries（买入评级），以及EMS领域的Amber Enterprises（中性评级）和Dixon Technologies（卖出评级）。GS调高了前三家的盈利预测和目标价，唯一调低展望的是Dixon——这家印度最大的手机EMS厂商正面临记忆体成本通胀挤压利润率、PLI补贴退坡以及合资项目审批延迟的多重压力。\n\n这份报告的核心主张可以浓缩为一句话：印度制造业正在从一个“量价齐升”的阶段，切换到一个“价升量平、利润承压”的新区间。对于投资者而言，真正需要追问的不是Q1收入增长多少，而是这种增长能否持续、利润能否同步改善、以及不同公司在成本压力下的竞争地位将如何分化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 铜铝价格同比涨幅创16个季度新高，收入增长主要靠“涨价”而非“走量”\n\nGS的数据显示，2026年第一季度（印度财年Q1FY27），铜和铝的LME价格同比涨幅分别超过35%，创下过去16个季度以来的最大涨幅。这一数字本身并不令人意外，但GS将其与公司层面的收入预期联系起来后，结论变得耐\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜价飙涨，线缆和EMS迎来什么变化\n\n线缆EMS的Q1前瞻\n\n铜铝涨价驱动营收，但利润率承压\n\n---\n\n**1. 线缆和电线：涨价撑起营收，量增有限**\n\n铜和铝的价格同比飙升超过35%，直接推高了线缆企业的收入。投行研报预计，Q1的销量增长仅为中到高个位数（mid-to-high single digits），但营收增长会明显被价格因素拉高。\n\n- Polycab：预计Q1营收同比+36%，其中线缆业务+41%。但利润率受成本挤压，EBITDA利润率从14.5%降至13.4%。\n- KEI Industries：预计Q1营收同比+27%，线缆业务+30%。EBITDA利润率从10.0%微升至10.1%，主要靠规模效应。\n\n**2. EMS：冰火两重天**\n\n手机内存涨价传导到EMS厂商，带来了营收增长，但利润结构在恶化。\n\n- Dixon：手机平均售价（ASP）因内存涨价而提升，但销量预计同比下滑18%。营收同比+8%，但EBITDA利润率从3.8%降至3.4%。每台手机利润固定，售价高了反而显得利润率低了。\n- Amber：空调需求因雨季推迟而延续到Q2，Q1库存正常化后增长改善。预计Q1营收同比+15\n\n[... middle omitted ...]\n\ngle digits for the quarter. Strong yoy growth in input prices is the key driver supporting revenue.\n\nNirmal Gopi, CFA\n+1(332)245-7667 | nirmal.gopi@gs.com\nGS India SPL\n\nDixon: We think an incr\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R010",
    "title": "GS：中国车企的“淘汰赛”还远未到终局",
    "digest": "[wechat_article.md]\n# GS：中国车企的“淘汰赛”还远未到终局\n\n当市场普遍认为中国新能源汽车行业的“淘汰赛”已经进入白热化阶段，甚至即将迎来终局时，GS在最新发布的研报中给出了一个反直觉的判断：行业整合，短期内不会发生。\n\n这份由 Tina Hou 和 Jenny Du 主笔的报告，基于对14家主要中国车企的财务与经营数据的系统分析，提出了一个清晰的“行业触底框架”。结论是，尽管国内市场销量暴跌19%，但强劲的出口增长和内部成本削减，使得行业整体的现金利润仍在增长。绝大多数车企的现金流仍然健康，管理层并未放弃扩张，而资产负债表上的净债务状态也远未普遍出现。\n\n这意味着，我们可能正在经历一场“低烈度、长周期”的消耗战，而非一场速战速决的决战。对于投资者和产业决策者而言，理解这个框架，比猜测下一个出局者是谁更为重要。\n\n> **KC评论：** GS这份报告的核心价值不在于预测股价，而在于提供了一个可验证的“行业整合三条件”框架。它告诉我们，不要被短期的价格战和销量排名迷惑，真正决定行业格局的是现金流、管理层心态和资产负债表。这三点，才是判断行业何时见底的硬指标。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 行业整合的三个必要条件，目前一个都没满足\n\nGS的报告提出了一个简洁的分析框架，认为只有当以下三个条件同时满足时，行业才会出现真正意义上的整合与出清：\n\n**第一，大部分车企的EBITDA（税息折旧及摊销前利润）为负，即处于“现金成本”水平。** 这意味着企业连维持基本运营的现金都赚不回来，更无力进行新的投资或产能扩张。截至2026年第一季度，14家样本车企中，仍有9家保持着正的EBITDA。尽管相比2025年全年的11家有所减少，但多数企业依然“有血可流”。\n\n**第二，管理层在利润率和扩张计划上全面“投降”。** 这指的是管理\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国车市还没到洗牌时刻\n\n行业整合仍需等待\n\n近1年盈利预期已连续下修4次\n\n最近在看某外资投行对中国汽车OEM的研报，几个核心判断分享给大家👇\n\n**1/ 行业整合短期内不会发生**\n研报用三个指标判断整合时机：\n- 多数车企还在现金成本线以上（14家中10家）\n- 管理层对利润/扩张态度分化\n- 只有1家处于净负债状态\n结论：2027年前看不到整合拐点\n\n**2/ 盈利预期加速下修**\n2026/2027年EBITDA预期已连续4次下调\n最近一次下修幅度达4%\n相当于行业总利润再减17-18亿人民币\n但多数车企仍高于现金成本线\n\n**3/ 出口是唯一亮点**\n国内零售同比-19%，但出口+70%\n研报下调国内销量预测5%\n预计2026年NEV渗透率达60%\n国内NEV零售仅+1%\n\n**4/ 谁在逆势增长？**\n研报点名三家：\n- 比亚迪：出口车型+销售网络扩张\n- 零跑：海外布局加速\n- 小鹏：新出口车型储备充足\n这三家在国内增长+海外敞口上都有优势\n\n行业洗牌还没来，但盈利压力在加大。\n出口能撑多久？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\nCHINA MOBILITY T\n\n[... middle omitted ...]\n\nely in the near term. As shown in Exhibit 1, as of 1Q26: (1) The majority (10 out of 14) of OEMs are above cash cost level; (2) Management outlooks are mixed on volume/margin/capacity; (3) Onl\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "JPM：可持续投资正在“喘口气”，但真正的风险来自科技",
    "digest": "[wechat_article.md]\n# JPM：可持续投资正在“喘口气”，但真正的风险来自科技\n\n全球可持续基金总资产在今年4月达到了3.8万亿美元，同比增长3%。这个数字看起来不错，但市场份额却从高点持续下滑，目前仅占全球基金总资产的5.6%。JPM在最新发布的《可持续投资2026年中展望》中，给出了一个克制的判断：可持续基金的资金流出已经停止，但大规模资金流入的前提尚未满足。\n\n这份报告的核心信息可以概括为三个字：喘口气。\n\n过去两年，可持续投资经历了从狂热到退潮的完整周期。ESG主题基金遭遇了前所未有的信任危机，美国市场的“反ESG”政治浪潮、欧洲监管的不确定性、以及全球利率环境的变化，都让这个赛道从“必选项”变成了“可选项”。但JPM的这份报告试图告诉市场：最糟糕的阶段可能已经过去，新的结构性变量正在形成。\n\n真正值得关注的不是资金流出的止跌，而是在科技股持续主导市场的背景下，可持续基金的结构性弱点正在被放大。这个问题的答案，将决定可持续投资的下一个十年。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资金流出的“止血”不等于“输血”\n\nJPM的数据显示，可持续股票基金的资金流已经从净流出转向中性。欧洲市场的流入抵消了亚洲和美国的流出，而固定收益类可持续基金则持续保持净流入。这是一个积极信号，但远未到乐观的时候。\n\n报告明确指出，可持续基金要实现实质性的大规模资金流入，前提是相对业绩能够持续改善。而目前的情况是，可持续基金的整体表现仅仅是与大盘“基本持平”。在欧洲，可持续基金小幅跑赢欧洲大盘基金；在美国，可持续基金则小幅跑输。这种表现不足以吸引增量资金。\n\n固定收益端的表现相对更好，可持续债券基金实现了正收益，且与整体市场基本一致。这解释了为何固定收益类可持续产品能持续获得资金流入。但债券市场的故事与股票市场不同——债券投资者的决策更多受到\n\n[... middle omitted ...]\n\n方便人工快速把握市场动态。欢迎来知识星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n可持续基金中场喘息，科技股成最大变数\n\n可持续基金迎来喘息期\n\n全球可持续基金规模达到3.8万亿美元，但市场份额继续下滑至5.6%。资金流从净流出转向中性，固收类仍在持续吸引资金流入。\n\n1️⃣ 业绩分化明显\n欧洲可持续基金小幅跑赢大盘，美国则小幅跑输。固定收益类表现平稳，整体与市场同步。关键变量在于：业绩能否持续改善，决定资金能否大举回流。\n\n2️⃣ 科技股是最大风险\n全球可持续基金普遍低配科技股（因偏重欧洲配置），而AI主题恰恰集中在美股。当新兴市场和日本策略师也开始看好科技，持续基金的相对表现压力进一步加大。\n\n3️⃣ 政策基调：务实推进\n欧盟设定2040年减排90%目标，但更注重“胡萝卜+大棒”组合拳。美国虽有政策噪音，但2026-27年可再生能源+储能装机预计仍超2025年。巴西推进碳市场和反森林砍伐政策。亚洲聚焦公司治理改革和能源安全。\n\n4️⃣ 六大投资主题\n关注电网、电池供应链、气候适应、欧洲“电力主权”、股东积极主义及美国低碳赢家。这些主题标的目标上涨空间在20%-51%之间。\n\n5️⃣ 债券发行：区域分化\n欧元区绿色债券发行占比略有回升，但英镑和欧元高收益债市场持续下滑，美国市场仍处于边缘\n\n[... middle omitted ...]\n\nes, European sustainable funds marginally outperformed European broad market funds, while sustainable US funds underperformed slightly. In fixed income, sustainable fund performance was positi\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R012",
    "title": "美国银行：芯片行业下一个1万亿美元，只需五年",
    "digest": "[wechat_article.md]\n# 美国银行：芯片行业下一个1万亿美元，只需五年\n\n半导体行业用了大约50年才实现第一个1万亿美元的累计销售额。美国银行（BofA）最新发布的研报给出了一个大胆判断：在AI的驱动下，第二个1万亿美元将在未来五年内完成。\n\n这不是一个线性外推，而是一个结构性跃迁。该机构将2030年全球半导体行业总可寻址市场（TAM）从此前的2.3万亿美元大幅上调至2.7万亿美元，对应的年复合增长率从23%提升至28%。上调的核心驱动力并非消费电子复苏，而是AI基础设施从“论证投资回报率”阶段，全面转向“解决物理约束”阶段——芯片产能、电力供应、封装能力，正在成为新的稀缺资源。\n\n这份报告发布于2026年6月，正值市场对AI资本开支持续性存在分歧的时刻。美国银行选择在这个时点大幅上调行业预测，其背后逻辑值得每一位产业决策者和投资者仔细拆解。\n\n> **KC评论：** 2.7万亿美元的TAM意味着什么？作为参照，2025年全球半导体销售额预计约为7870亿美元。即使按最乐观的预测，到2030年市场规模也要翻三倍以上。这不再是“成长”，而是“爆发”。报告的标题已经点明核心驱动力：AI将行业可见性延伸至2028年。如果你还在用传统半导体周期的框架来思考，很可能错过这轮结构性机会。完整报告中的情景分析和敏感性测试，能帮助你理解这个数字在不同假设下的弹性空间。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 从“论证ROI”到“解决物理约束”：AI产业的底层逻辑已变\n\n过去两年，市场对AI的最大质疑是：巨额资本开支能否带来足够的回报。美国银行认为，这个阶段已经过去了。当前AI产业的核心矛盾，已经从“值不值得投”变成了“能不能建得出来”。\n\n报告明确指出，AI行业正在从“必须证明投资回报率”转向“应对结构和物理约束”——芯片短缺、电力供应紧张、先\n\n[... middle omitted ...]\n\nI，也方便人工快速把握市场动态。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI芯片的下一波增量，都在这里了\n\n📈 芯片行业的下一个万亿\n\n芯片行业花了50年做到第一个1万亿美金销售额，AI可能只花5年就再添一个1万亿。某外资投行刚更新了半导体行业预测，把2030年全行业规模从2.3万亿上调到2.7万亿，年复合增速从23%拉到28%。\n\n涨这么多，靠的是什么？\n\n1/ 🚀 内存和数据中心是主引擎\n内存增速最快，年复合增速接近50%。背后是AI对算力的“贪得无厌”——AI数据中心系统市场规模将从2025年的2730亿冲到2030年的1.7万亿。\n长协（LTA）让存储芯片厂对未来2-3年的供需/价格更有信心，比如最近美光与Anthropic的合作就是信号。\n\n2/ 🔧 设备厂直接受益\n芯片制造设备（WFE）预测被大幅上调：2028年从2030亿→2500亿，2029/2030年继续涨到2680亿/2920亿。\n原因有三：清洁厂房2028年更充裕、长协带来长期可见性、技术拐点推高每片晶圆的设备投入。\n\n3/ 💡 核心芯片（非内存）也在涨\n到2030年核心芯片规模约1.1万亿，年复合增速14%。服务器芯片（+24% CAGR）和有线通信（+15%）是主力，但消费电子（PC +2%、手机0%）\n\n[... middle omitted ...]\n\nn, or +28% CAGR between CY25-30E, from \\$2.3Tn/+23% CAGR prior, led mostly by growth in memory/data center, and also incrementally by recovery in auto/industrial. Our new industry forecasts/es\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R013",
    "title": "GS：新能源车周订单暴增34%，但真正的胜负手不在销量",
    "digest": "[wechat_article.md]\n# GS：新能源车周订单暴增34%，但真正的胜负手不在销量\n\n6月第三周，中国新能源车市场交出了一份让多数人意外的高分答卷。GS最新发布的周度追踪数据显示，在6月15日至21日这一周，主要新能源品牌合计订单同比大增31%，环比更是飙升34%。比亚迪、小米、零跑成为环比增长最快的三家车企，增幅分别达到134%、44%和22%。\n\n这份数据发布的时间点值得注意。市场此前普遍担忧价格战持续侵蚀利润，叠加传统燃油车在6月加大折扣力度，新能源车渗透率的上升势头可能遭遇阻力。但GS的周度数据给出了相反的信号：新能源车零售渗透率在6月前两周已达到63.9%，批发渗透率更是攀升至67.9%，均高于5月全月的水平。\n\n订单的爆发式增长，最直接的驱动力是新车型集中上市。比亚迪“大唐”于6月17日开启交付，零跑C10/C11/C16改款于6月16日上市。这些新车型在上市首周即贡献了显著的增量订单。但问题在于：这种由新品脉冲驱动的增长，能否持续？订单转化率如何？价格战是否真的在缓和？\n\nGS这份周度图表报告提供了大量高频数据，但真正值得产业决策者和投资者关注的，不是某一家公司单周订单的起伏，而是这些数据背后隐藏的结构性变化。\n\n> **KC评论：** GS这份周报的核心价值不在于告诉你“哪家卖得好”，而在于它提供了从订单、折扣、渗透率到上游电池价格的完整高频拼图。对于跟踪竞争格局的人来说，单周数据是噪音，但连续数周的趋势变化，往往比季报更能提前暴露拐点。完整报告中的逐周对比图表和品牌级折扣数据，是判断“涨价是否可持续”的关键素材。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮订单脉冲的含金量，取决于新车型能否跨越“尝鲜期”的鸿沟\n\n比亚迪“大唐”上市首周贡献了惊人的订单增量，但仔细看GS的数据，比亚迪王朝与海洋系列YTD订单同比仍\n\n[... middle omitted ...]\n\n存数据如何获取、以及哪些品牌最可能在下一轮价格战中守住利润。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月第3周新能源订单暴涨34%，谁在狂飙？\n\n📌 新能源订单周度回暖\n\n6月第3周（6/15-6/21），新能源品牌合计订单环比增长34%，同比增长31%。主要拉动来自多款新车上市：比亚迪大唐6/17上市、零跑C10/C11/C16改款6/16上市。\n\n1️⃣ 品牌增速分化明显\n- 比亚迪周订单环比+134%，主力贡献来自大唐新车型\n- 小米周订单环比+44%，持续高热度\n- 零跑周订单环比+22%，改款效应明显\n- 蔚来、理想、小鹏表现平稳，环比变化在-26%至+8%之间\n\n2️⃣ 渗透率继续爬坡\n6月1-14日，新能源零售渗透率63.9%，批发渗透率67.9%，较5月的63%/61.1%继续提升。新能源零售量34.1万辆，同比-8%但环比+5%。\n\n3️⃣ 终端折扣：新能源收窄、燃油车扩大\n- 新能源平均折扣7.48%（6/20），较上周7.54%微幅收窄\n- 燃油车平均折扣19.62%，较上周19.56%继续扩大\n- 比亚迪折扣稳定在4.27%，未随新车上市加大优惠\n\n4️⃣ 上游电池：碳酸锂继续回落\n电池级碳酸锂价格跌至16.75万元/吨，周环比-4%。LFP和NCM电芯价格稳定，成本端压力仍在缓释。\n\n[... middle omitted ...]\n\nr, and (4) Upstream battery pricing dynamics.\n\n## 2026 Week 25 highlights:\n\n■ Key brand orders: BYD / Xiaomi / Leapmotor showed the highest growth at +134%/+44%/+22% wow.\n\nCPCA weekly trend: A\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "JPM：地产股急跌不是基本面反转，而是噪音窗口",
    "digest": "[wechat_article.md]\n# JPM：地产股急跌不是基本面反转，而是噪音窗口\n\n过去四个交易日，中国地产板块跑输恒生指数9%。对于持有国企开发商仓位的投资者来说，这轮急跌像是突如其来的冷水。但仔细拆解JPM这份最新报告可以发现，市场关心的核心问题——房价是否企稳、销售是否可持续——并没有被高频数据否定。\n\n相反，报告给出的判断值得认真对待：这轮下跌主要是四重噪音的叠加，而非基本面趋势的逆转。真正关键的变化藏在两个被市场低估的信号里——一线城市二手挂牌量的持续下降，以及房价环比连续第四个月转正。这些信号指向的结论是：市场正在从“全面下跌”切换到“K型分化”，而分化的赢家已经清晰。\n\n**KC评论：** 这份报告最核心的判断是，过去几天的急跌不是基本面的“第二只脚”，而是噪音。但噪音本身也值得认真对待——它告诉我们市场对什么信号敏感、什么变量正在被错误定价。完整报告里的高频数据拆解和个股估值表，能帮你判断哪些资产在这轮噪音中反而值得加仓。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四重噪音叠加，不是基本面逆转\n\nJPM把过去四天的下跌归结为四个原因，每一个都指向“情绪和结构因素”，而非销售或价格数据的恶化。\n\n第一，消费数据的疲弱产生了负面传导。当居民消费信心走弱，市场自然怀疑房地产复苏的可持续性。第二，地产板块的高贝塔属性在市场整体回调中被放大——同期恒生指数本身就在下跌，地产只是跌得更快。第三，短期缺乏催化剂。高频数据虽然“intact”（完好），但没有出现“明显更好”的边际改善，这让市场缺少一个买入的理由。第四，部分投资者过度关注了二手成交的环比下滑，而忽视了季节性因素——3月和4月通常是成交旺季，环比回落是正常现象。\n\n报告特别指出，即使是华润置地和中海地产这样此前相对抗跌的国企龙头，也在过去两个交易日急跌了11%，而同\n\n[... middle omitted ...]\n\n和微信群，在数据图表和深度讨论中，一起判断这轮噪音何时结束。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n地产股的这波回调，是机会还是风险？\n\n**短期回调，数据其实不差**\n\n最近4个交易日，地产板块跑输恒指9%。但仔细看高频数据，基本面其实没有变差，主要是这几个原因：\n\n1️⃣ **消费数据疲软的拖累**——市场情绪传导，地产作为高beta板块，大盘一跌它跌得更快\n2️⃣ **短期催化剂真空**——高频数据虽然没崩，但也没有明显加速改善，资金缺乏做多理由\n3️⃣ **季节性误读**——有人盯着二手房环比下滑，但3-4月本来就是旺季，看同比更合理。剔除端午节影响后，9城二手房成交同比仍有+15%，跟之前几周的10-20%增速基本一致\n\n**龙头房企也在补跌，但年内依然强势**\n\n华润置地、中海地产过去2天跌了11%（恒指仅-2%）。不过拉长看，年内华润+15%、中海+7%，依然大幅跑赢恒指（-7%）。这波更像是大盘走弱下的获利了结。\n\n**一个容易被忽视的积极信号**\n\n一线城市二手房挂牌量持续下降，从3月高点已回落2.5%。挂牌量减少是价格企稳的重要前提，市场可能还没充分定价这一点。\n\n**核心结论**\n\n研报认为，一线城市数据持续企稳，逢回调可以关注销售增长强、一线城市敞口大的国企开发商。但对于多数非国企开\n\n[... middle omitted ...]\n\nntly better; (4) some investors may have focused on the weaker M/M secondary sales volume; however, in our view, this not an accurate way to gauge the market well-being due to seasonality (Mar\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R015",
    "title": "摩根斯坦利：人形机器人2026年出货量上调近八成，关键不在技术而在“部署数据闭环”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：人形机器人2026年出货量上调近八成，关键不在技术而在“部署数据闭环”\n\n2026年6月，摩根斯坦利发布了一份关于中国人形机器人产业的深度研报，核心判断清晰且直接：**商业化验证、政策支持与供应链反馈正同步加速，该机构将2026年中国人形机器人出货量预测从此前的2.8万台大幅上调至5万台，2030年预期达到44.6万台。**\n\n这不是一份关于“机器人能否造出来”的报告。报告的核心主张是：产业正在从“展示能力”进入“创造商业价值”的阶段，而决定这一轮成败的关键，不是单台机器人的技术参数，而是**谁能最快通过规模化部署，形成“部署-数据采集-算法迭代-再部署”的正向循环。**\n\n对于关注中国制造业升级、供应链重构以及AI硬件落地的读者，这份报告提供了一个从宏观政策到微观订单、从整机厂到核心零部件供应商的完整观察框架。它既指出了明确的投资主线，也留下了需要持续跟踪的关键变量。\n\n> **KC评论：** 摩根斯坦利上调出货量预测的直接驱动因素，不是实验室的技术突破，而是国家电网一笔68亿元订单、顺丰和邮政的物流场景落地、以及MIIT与SASAC联合推动的“万级部署能力”目标。这意味着，人形机器人已经从“概念验证”进入了“政策+订单”双轮驱动的阶段。完整报告中对这些订单的细节、供应链验证的现场反馈、以及各环节公司的产能规划都有更细致的拆解，值得细读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮加速的真正推手不是技术，而是“用起来”的政策与订单\n\n报告指出，2026年上半年，人形机器人的商业化进程明显提速，标志性事件密集出现。\n\n政策层面的信号最为明确。2026年3月，中央政府首次在“十五五”规划中将机器人列为战略性新兴产业。6月，工信部和国资委联合发布新倡议，目标是在2026年底前形成“万级部署能力\n\n[... middle omitted ...]\n\n讨论。我们会在那里持续追踪这些关键信号，并分享更细致的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026人形机器人出货量上调至5万台\n\n**投研笔记**\n\n**商业验证+政策加码，产业链反馈积极**\n\n某外资投行最新研报把2026年中国⼈形机器人出货预测从2.8万台上调至5万台，2030年看44.6万台。\n\n逻辑拆解一下：\n\n1️⃣ **商业化加速落地**\n- 小鹏等多家整机厂宣布2026年底量产\n- 国家电网下了68亿元订单：500台人形+3000台双臂+5000台四足\n- 顺丰、中国邮政已在物流中心部署机器人\n\n2️⃣ **政策强力推动**\n- 工信部+国资委联合发起全国性行动\n- 目标：2026年底形成万套级部署能力、超100个高价值应用场景\n- 各省≥20个、央企≥10个真实作业场所改造为训练场\n\n3️⃣ **供应链信心爆棚**\n- 绿的谐波：月产能从5万套扩至7万，年底瞄准10-12万\n- 恒立液压：墨西哥工厂年底可支撑约10万台机器人\n- 双环传动：为某美国头部整机厂开发新型减速器已超2年\n\n**关键催化剂密集**\n- 7月：WAIC世界人工智能大会\n- 8月：世界机器人大会+人形机器人运动会\n- Q3：Optimus Gen3发布、多家整机厂IPO\n\n**值得关注的赛道**\n- 谐波减速器\n\n[... middle omitted ...]\n\ndually shift toward full-size humanoids, at c.30%/50%/70% in 2026-28, in our view. Our supply-chain checks point to a constructive outlook for volume and the start of automated production line\n\n[... middle omitted ...]\n\ny Industry (000157.SZ)</td><td>O (09/08/2025)</td><td>Rmb7.38</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R016",
    "title": "摩根斯坦利：MS：中国房地产的修复，还差一个“端午效应”的量级",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国房地产的修复，还差一个“端午效应”的量级\n\n这份MS最新发布的每周数据库追踪报告，披露了一个关键信号：在刚刚过去的一周（截至6月21日），中国50城新房周度成交量同比下降16%，较前一周的-3%明显走弱。这份报告的核心判断不是“转冷”，而是“被节日效应掩盖的真实节奏正在显现”。\n\n真正值得关注的，是数据背后所揭示的市场修复的结构性特征——不是全面回暖，而是分化的加速。这份研报提供了一组精细到城市层级、一二手市场、挂牌价与去化率的交叉数据，足以让产业决策者重新审视“修复”二字的真正含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新房市场的“端午坑”暴露了修复的脆弱性\n\n如果只看周度同比数据，新房市场似乎出现了一个明显的回调。50城新房成交量同比下降16%，而前一周还是-3%。但MS明确指出了这背后的关键扰动因素——端午节假期带来的日历效应。\n\n这并非简单的技术性解释。端午节期间，各地推盘节奏明显放缓，网签系统暂停或延迟，这些都会导致当周成交数据出现系统性偏低。更值得追问的是：如果剔除节日效应，真实的市场动能是什么？\n\n答案是：修复仍在进行，但强度远不足以支撑全面反转。前一周的-3%已经是一个偏弱的读数，而本周的-16%即使进行日历调整，也很难回到正增长区间。这意味着，当前市场的修复更多是“低位企稳”而非“趋势性回暖”。\n\n> **KC评论：** 对于投资者而言，不要因为单周数据的大幅波动就改变对行业基本面的判断。节日效应在房地产周度数据中是一个常见的噪声源，但噪声背后往往隐藏着更重要的信号——即市场在没有政策刺激和假期干扰时，其自然成交动能到底有多强。完整报告中的四期移动平均线图表，才是判断趋势的真正工具。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n[... middle omitted ...]\n\n否可持续——欢迎加入社群，与我们一起跟踪和讨论这些关键变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午楼市数据出炉，一线城市现分化\n\n📊 端午楼市数据速览\n\n上周（截至6月21日），50城新房成交同比下降16%，比前一周的-3%进一步走弱。部分原因是端午节假期带来的日历效应。\n\n1️⃣ 新房成交：各线城市均回落\n- 一线城市：同比-15%（前一周+2%）\n- 二线城市：同比-12%（前一周-7%）\n- 三线城市：同比-28%（前一周+9%）\n- 年初至今累计：50城整体-12%\n\n2️⃣ 二手房成交：同样降温\n10城二手房成交同比-15%（前一周+4%）\n- 一线城市：同比-10%（前一周+3%）\n- 二线城市：同比-19%（前一周+3%）\n- 年初至今累计：仍保持+5%的正增长\n\n3️⃣ 关键指标：去化率与价格\n- 整体去化率47%，与前一周基本持平\n- 一线城市去化率59%，明显高于二三线\n- 六大城市二手房挂牌价指数17.3%，微降0.1个百分点\n- 一线城市中介信心指数51.0，较前周下降2.2\n\n🤔 值得关注的是，一线城市新房去化率从45%跳升至59%，说明优质项目仍有需求支撑。但整体来看，市场仍处于调整期。\n\n大家觉得接下来市场会怎么走？欢迎一起讨论～\n\n#学习笔记\n\n[source_mine\n\n[... middle omitted ...]\n\nTier 3 city sales fell 28% YoY (vs. +9% YoY).\n\nWeekly secondary registered unit sales in 10 cities declined 15% YoY (vs. +4% YoY in the previous week), bringing YTD sales to +5% YoY: Tier 1 ci\n\n[... middle omitted ...]\n\nty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$3.71</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R017",
    "title": "UBS：中国券商股不只是反弹，是估值体系正在被政策重写",
    "digest": "[wechat_article.md]\n# UBS：中国券商股不只是反弹，是估值体系正在被政策重写\n\n6月22日，中国券商H股板块单日大涨6.1%，同期恒生指数下跌0.65%。这不是一次简单的情绪修复。UBS在当天发布的研报中给出了一个值得认真对待的判断：券商板块正在进入一个由政策组合拳和基本面共振驱动的重新定价窗口。\n\n这份报告的核心主张是，市场低估了两件事——第二季度业绩的强劲程度，以及政策层面正在发生的结构性变化。前者是短期催化剂，后者才是估值中枢上移的真正来源。\n\n如果你还停留在“券商股是牛市放大器、熊市拖累者”的旧框架里，这篇研报可能会让你重新审视这个行业的定价逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 第二季度业绩的强劲程度，可能超出市场目前的预期\n\nUBS的判断起点是业绩。这不是一个模糊的“有望改善”，而是有数据支撑的强信号。\n\n报告指出，A股二季度至今的股票日均成交额已跃升至2.8万亿元人民币，同比增长1.2倍，环比增长9%。融资融券余额升至3.0万亿元，同比增长62%，环比增长14%。A股IPO募资额同比增长65%，环比增长91%。新发混合型基金规模达到960亿元，同比增长1.8倍。4至5月新开股票账户数达530万户，同比增长51%。\n\n这些数字合在一起意味着什么？券商的核心收入来源——经纪、两融、投行、资管——在第二季度几乎全线走强。而市场目前对券商股的定价，显然还没有充分反映这一现实。\n\n以CITICH股为例，其年内涨幅仅为5.4%，CICCH股年内涨幅11%。对于一个营收增速可能在30%以上的行业，这样的估值水平并不算贵。\n\n> **KC评论：** 这里的关键不是“业绩好”，而是“业绩好但股价还没充分反映”。UBS的测算框架显示，上市券商一季度经常性净利润已同比增长39%，二季度大概率会更高。但板块年内H股整体下跌0.\n\n[... middle omitted ...]\n\n，欢迎来我们的微信群里继续讨论，一起跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n券商板块突然大涨，背后逻辑拆解\n\n**券商板块，为什么涨了？**\n\n上周中资券商H股突然拉升6.1%，而恒指跌了0.65%。这波行情不是偶然，是两个催化剂叠加的结果。\n\n**1/ Q2业绩大概率不错**\n市场活跃度在Q2延续了强势。A股日均成交额环比Q1又增长了9%，同比翻了1.2倍。两融余额环比增14%，同比增62%。新基金发行也热，4-5月混合型新基金卖了960亿，同比增1.8倍。这些数据都指向券商Q2的盈利会比Q1更好看。\n\n**2/ 政策暖风在吹**\n上周陆家嘴论坛释放了稳定市场的信号，强调吸引长期资金、丰富金融工具。同时，商务部等部委发文，允许外资机构参与国债期货等衍生品交易，还给了基金投顾牌照。这些政策会加速行业向买方投顾模式转型。\n\n**哪些业务线受益最直接？**\n- 财富管理/经纪业务：市场活跃度提升，交易量放大。\n- 投行业务：科创板、创业板注册制改革，IPO和并购重组项目增多。\n- 跨境业务：人民币外汇期货试点、港股人民币国债期货推出，为券商开辟新收入来源。\n\n**行业估值怎么看？**\n目前覆盖的券商平均交易在2026年预期市净率的1.2倍（H股）/0.8倍（A股）。考虑到盈利改善和结构性\n\n[... middle omitted ...]\n\nd Optimizing Foreign Investment Attraction ('the Plan') issued jointly by MOFCOM, NDRC and MOF. The Plan extends derivative market access to foreign institutions, including treasury futures; a\n\n[... middle omitted ...]\n\nng number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R018",
    "title": "UBS：氟化工正被AI重新定价，但市场还没看懂",
    "digest": "[wechat_article.md]\n# UBS：氟化工正被AI重新定价，但市场还没看懂\n\n当AI算力竞赛从芯片蔓延到材料，一个被低估的板块正在浮出水面。\n\nUBS最新发布的氟化工行业报告，给出了一个值得产业决策者和投资者认真审视的判断：氟化工材料在AI领域的应用潜力正在快速增长，但市场对这一结构性变化的定价仍然不足。报告明确指出，“氟化工材料供应商目前相对于电子化工材料企业存在显著折价，我们认为市场尚未完全定价AI带给氟化工材料的增长机会。”\n\n这不是一个关于“氟化工涨价”的短期交易故事。这是一个关于材料体系迭代、供应链重构和国产替代交汇的长逻辑。\n\n这份报告发布于2026年6月，覆盖了从电子级氢氟酸到氟化液、从PTFE到氟化气体的完整产业链。但它的核心洞察其实非常集中：AI对算力的需求正在倒逼材料体系的升级，而氟化工材料在性能上的不可替代性，使其成为这一进程中的关键受益者。\n\n如果你只是把氟化工看作一个周期性化工子行业，你可能正在错过一个结构性重估的窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI对氟化工的需求不是“蹭概念”，而是材料体系的必然迭代\n\nUBS报告开篇就点明了这一轮氟化工指数跑赢化工指数的两大驱动力：一是美国推迟部分第三代制冷剂退出时间表，二是市场对氟化工材料AI应用潜力的预期升温。但真正值得关注的，是后者。\n\n为什么AI会拉动氟化工材料？核心逻辑并不复杂。\n\nAI服务器对散热效率和低介电常数提出了远超传统服务器的要求。当芯片功耗从几百瓦跃升至上千瓦，空气冷却已经达到物理极限，液冷成为必然选择。而在液冷方案中，氟化液凭借其化学惰性、不燃性、优异的电绝缘性和低表面张力，成为目前最理想的冷却介质之一。\n\n同时，AI服务器对PCB基板材料的介电性能提出了更高要求。PTFE（聚四氟乙烯）因其极低的介电常数和介电损耗，被视为下一代P\n\n[... middle omitted ...]\n\nI，也方便人工快速把握市场动态。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 算力背后，氟化工悄悄跑赢\n\n氟化工，AI 的隐形冠军\n\nAI 爆发，除了算力芯片，还有一类材料正在悄悄受益——氟化工。最近这个板块跑赢化工指数约 9%，逻辑很清晰。\n\n1/ 半导体制造：三大方向值得看\n- 电子级氢氟酸（G5 级）：技术壁垒高，国内 CR5 达 98%，主要玩家包括多氟多、巨化、滨化等。AI 驱动的存储需求让高端产品供应偏紧。\n- 氟化液：半导体清洗冷却必备。3M 已退出 PFAS 生产，国产替代机会明确，新宙邦布局较深。\n- 氟化气体：关注六氟化钨、六氟丁二烯等高壁垒品种，国产化空间大。\n\n2/ 数据中心：冷却材料成新战场\nAI 服务器功耗飙升，氟化工材料是理想散热方案。\n- PTFE：低介电常数，适合下一代 PCB 基板，东岳集团是龙头。\n- 液冷材料：冷板式看 R134a/R1234yf 制冷剂，浸没式看氟化液。\n\n3/ 估值还在低位\n当前氟化工材料公司估值相比电子化学品有明显折价，市场尚未完全定价 AI 带来的增量。某外资投行上调了东岳、新宙邦、中研股份、广钢气体的目标价，核心逻辑就是 AI 需求拉动。\n\n研报未给出具体时间表，但趋势很明确：AI 的算力军备竞赛，正在拉动上游材料\n\n[... middle omitted ...]\n\ne higher compute power demand and the iteration of material systems induced by AI developments. Currently, fluorochemical material suppliers are trading at a notable discount to electronic che\n\n[... middle omitted ...]\n\nng number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R019",
    "title": "GS：中国经济5月边际回暖，但内需疲软与信用紧缩的“温差”才是真正挑战",
    "digest": "[wechat_article.md]\n# GS：中国经济5月边际回暖，但内需疲软与信用紧缩的“温差”才是真正挑战\n\n中国经济在5月出现了一丝令人宽慰的边际改善，但这份改善的底色，远非“复苏”二字可以概括。GS最新发布的6月中国自营经济指标报告揭示了一个更复杂的图景：制造业产出带动了整体活动指标的微幅回升，然而，隐藏在数据背后的内需疲软、信用紧缩和财政节奏滞后，构成了当前经济运行的真正挑战。对于投资者和决策者而言，理解这组“温差”信号，比关注单一数据点的好坏更为关键。\n\n这份报告的核心价值不在于给出了一个乐观或悲观的结论，而在于它通过一系列自营的高频和结构性指标，拆解了经济增长的动力来源与阻力所在。它提醒我们，当前的经济修复更像是一次局部反弹，而非全面的趋势反转。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 制造业是5月唯一的亮点，但这一“独木”能否支撑全局？\n\nGS的中国当前活动指标在5月环比年化增长4.6%，高于4月的2.9%。这一改善的主要驱动力来自制造业部门。报告中的制造业增长代理指标在5月出现回升，这与官方PMI数据所显示的产出扩张趋势是一致的。\n\n然而，我们必须追问一个“所以呢”的问题：制造业的韧性能够持续多久，并且能否有效传导至消费和服务业？目前来看，答案并不乐观。制造业的改善更多是基于供给端的修复和部分外需的支撑，而非内需的全面启动。如果消费和房地产等终端需求持续疲弱，制造业的反弹很可能只是库存周期的一次短暂补库，缺乏持续扩张的动力。这就像一场接力赛，第一棒跑得不错，但第二棒迟迟未能接棒。\n\n> **KC评论：** GS的制造业增长代理指标（基于机床、汽车、发电设备等产出）是值得持续跟踪的先行指标。但读者必须意识到，这一指标的改善与终端需求的关联度正在减弱。完整报告中关于消费和“其他”（包含房地产和劳动力市场）领域的CAI分项数据，才\n\n[... middle omitted ...]\n\n欢迎来我们的星球和微信群中继续讨论，一起穿透数据，看清本质。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月经济：制造业撑场，内需偏冷\n\n📊 5月经济真相\n\n某外资投行最新研报显示，5月经济呈现“制造业强、内需弱”的分化格局。\n\n1️⃣ 制造业是唯一亮点\n5月当前活动指标（CAI）环比年化升至+4.6%（4月+2.9%），改善几乎全由制造业带动。但消费和地产板块依然疲软。\n\n2️⃣ 内需信号不太乐观\n进口隐含的国内需求指标显示，Q2内需增长偏弱。宏观数据MAP surprise指数持续低于市场预期，说明实际数据跑不赢预期。\n\n3️⃣ 金融条件小幅收紧\n5月金融条件指数（FCI）略有收紧，主要受人民币贸易加权升值+股市走弱影响。信用脉冲预计H2保持负值，因为信贷增长偏慢。\n\n4️⃣ 财政端有积极信号\n广义财政赤字在收窄，但政府债券净发行将在未来几个月加速，财政“支出转化率”小幅回升。地方地产政策继续放松。\n\n💡 总结：5月经济靠制造业撑场面，但内需和信贷偏冷，政策端还得加力。财政发力已在路上，关键看后续落地节奏。\n\n欢迎一起讨论你对后续政策节奏的判断。\n\n#学习笔记\n\n[source_mineru.md]\n# GS China Econ Proprietary Indicators: June\n\nPlease f\n\n[... middle omitted ...]\n\n Others include the housing sector and labor markets.\n\nExhibit 2: May's improvement in CAI was mainly led by manufacturing sectors  \n![](images/8892e364b98e8b2c3d94432d40512403b354eb5768290135\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R020",
    "title": "JPM：财政不是没子弹，是没扣扳机",
    "digest": "[wechat_article.md]\n# JPM：财政不是没子弹，是没扣扳机\n\n5月财政数据公布后，市场对“政策刺激力度不足”的担忧再次升温。但JPM这份最新研报给出了一个与市场直觉相反的判断：问题不在于财政空间不够，而在于部署节奏慢于预期。5月财政存款升至近十年同期第二高位，恰恰说明子弹还在枪膛里。\n\n这不是一个关于“有没有钱”的故事，而是一个关于“什么时候、以什么方式花钱”的故事。对于所有关注中国资产定价的投资者来说，理解这个时间差，比争论总量数字更有意义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 收入端超预期，但支出端暴露了结构性问题\n\n5月一般公共预算收入同比增长6.6%，延续了4月以来的强劲势头。证券交易印花税同比暴增145.9%，直观反映了市场活跃度。税收收入增长6.8%，增值税贡献最大。\n\n但支出端却连续第二个月收缩，同比下降1.6%。这与一季度2.6%的增速形成鲜明对比，更远低于全年4.4%的预算目标增速。\n\n**收入好、支出慢**，这个组合本身就是一个信号：财政当局没有选择在二季度加速发力。原因可能不是缺乏意愿，而是对一季度GDP超预期增长后的“政策耐心”。\n\n> **KC评论：** 很多投资者看到财政支出收缩就认为“政策转向紧缩”，但JPM的数据表明，问题出在基建支出这个具体环节，而非整体财政收缩。5月基建类支出同比下降12%，直接拖累了基础设施固定资产投资同比下降9.4%。这意味着，只要基建支出恢复，整体财政数据就会有明显改善。完整报告中关于支出分项的细拆图表，值得仔细对照阅读。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 土地收入加速下滑，政府性基金账本承压\n\n如果说一般公共预算还有韧性，政府性基金账本则面临更大的压力。5月政府性基金收入同比下降20.3%，其中土地出让收入\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月财政数据：钱到位了，但还没花出去\n\n封面：钱去哪了？\n\n副标题：5月财政存款创近十年次高\n\n---\n\n**1. 收入稳，支出慢**\n\n5月一般公共预算收入同比增长6.6%，税收和证券交易印花税表现亮眼。但支出却连续第二个月收缩，同比-1.6%，尤其基建类支出拖后腿，同比-12%。\n\n说白了：钱在账上，没流出去。\n\n**2. 土地收入加速下滑**\n\n政府性基金收入同比-20.3%，土地出让收入跌幅进一步扩大到-35.8%。地方财政压力不减，支出端也跟着收缩。\n\n**3. 财政存款高企，下半年空间大**\n\n5月财政存款升至近十年同期第二高。这意味着上半年钱花得慢，下半年政策空间反而更充足。\n\n**4. 专项债6月加速，但落地有滞后**\n\n6月专项债发行已近5000亿，明显提速。但研报指出，从发债到项目落地有传导时滞，6月投资数据未必能马上反映。\n\n**5. 两步走路径**\n\n第一阶段：执行已批预算，加快项目审批和资金拨付；\n第二阶段：若二季度增长不及预期，可能追加额外支持。\n\n---\n\n研报认为，当前财政节奏偏慢，更多是政策耐心而非无力。基建投资疲软背后，项目储备不足、优先还债、政策性工具落地慢都是原因。\n\n[... middle omitted ...]\n\nscal path: execution of NPC approved budget first, with additional support more likely if recent growth slowdown lingers.\n\nAligned with the continued FAI decline in May, fiscal expenditure (ac\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R021",
    "title": "NOM：人民币中间价模型释放了一个被忽视的鸽派信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型释放了一个被忽视的鸽派信号\n\n市场对人民币汇率的讨论，大多集中在央行意图、中美利差和出口表现上。但一份来自NOM亚洲外汇策略团队的模型报告，提供了一个更底层、更量化的观察视角：人民币每日中间价的定价机制本身，正在发出值得关注的信号。\n\n这份报告的核心判断是：**NOM的人民币中间价模型显示，当前中间价的设定存在系统性偏低，且逆周期因子已显著收窄。** 这并不意味着央行在主动引导贬值，而是意味着在当前的定价框架下，市场力量正在发挥更大作用，而政策干预的边际成本正在上升。\n\n对于关注宏观对冲、跨境资产配置和汇率风险管理的读者来说，理解这个“模型信号”比猜测“央行意图”更具实际意义。因为前者是可量化、可追踪的，后者则往往被噪音覆盖。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型投影的“意外下修”，暗示了中间价形成机制的变化\n\nNOM模型在6月24日的最新投影为6.7910，较前值6.8171低了261个基点。这一数字本身并非关键，关键在于它与官方实际中间价之间的差距，以及这种差距的演变趋势。\n\n模型投影是NOM基于其预设的定价因子（包括前日收盘价、一篮子货币变动、央行政策倾向等）计算出的“理论中间价”。当实际中间价显著低于模型投影时，通常意味着央行在主动引导汇率走弱；反之，则意味着央行在支撑汇率。\n\n但报告提供的图2（模型误差走势图）显示，近期的模型误差正在收窄，甚至出现方向性逆转。这指向一个更值得关注的结论：**央行对中间价的干预力度在减弱，市场化的定价因子权重在上升。**\n\n> **KC评论：** 很多市场参与者过度关注“央行是否在引导贬值”这个模糊问题。NOM模型提供了一个更精确的观察框架：不是看央行“想”做什么，而是看“实际”中间价与“模型”中间价的偏差。偏差缩小，意味着市场定\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型指向6.79\n\n6.79 模型指向\n\n比上次低了261点\n\n某外资投行最新的人民币中间价预测模型出炉，核心数据值得一看。\n\n1/ 模型直接给出了6.7910的预测值，相比上一次的6.8171，低了261个基点。这个数字比官方前一天收盘价还高了45个点。\n\n2/ 如果加入逆周期因子，模型预测值调整到6.8025，比上一次的中间价低了146个点。逆周期因子在发挥作用，方向是缓和贬值压力。\n\n3/ 从模型权重图看，对预测变化贡献最大的四个因素，研报没有给出明细，但通常包括一篮子货币走势、隔夜美元变化、市场供求等。可以推测，隔夜美元走弱可能是主要拖累项。\n\n4/ 研报还列出了2026年下半年中国的重要事件日历：7月底政治局会议、10月国庆黄金周、11月深圳APEC、12月中央经济工作会议和政治局会议，以及年底可能的中美元首会晤。这些事件都可能成为汇率政策的观察窗口。\n\n整体来看，模型显示人民币中间价有继续下行（升值）的空间，但逆周期因子在主动控制节奏。后续走势还要看这些关键事件怎么演绎。\n\n#学习笔记\n\n[source_mineru.md]\n# USD/CNY fix model\n\n24 June 2\n\n[... middle omitted ...]\n\nctor)  \n![](images/f79bd2840eaf79f872aacd4b0cab011527acb91343634de04c835ab0db5b2047.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/4f\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R022",
    "title": "JPM：中国MDI出口量价齐升，欧洲市场正成为新的定价锚",
    "digest": "[wechat_article.md]\n# JPM：中国MDI出口量价齐升，欧洲市场正成为新的定价锚\n\n中国化工品出口正在经历一场静悄悄的结构性转变。JPM最新发布的MDI（二苯基甲烷二异氰酸酯）贸易数据显示，2026年5月中国MDI出口量达到10.1万吨，同比飙升49%，出口均价环比上涨13%、同比上涨25%。这不是一次简单的周期性反弹——出口流向的重新布局和定价能力的恢复，正在改写全球MDI的竞争规则。\n\n这份由Jeffrey J. Zekauskas领衔的研报揭示了一个关键信号：在中国出口总量尚未恢复到2024年峰值水平的情况下，出口价格已经率先突破。5月MDI出口均价达到2193美元/吨，不仅是近两年来的最高水平，更意味着中国供应商正在从“以量换价”转向“以价换量”的新阶段。\n\n对于关注化工板块的投资者而言，这份数据最重要的判断是：全球MDI的供需再平衡正在加速，而定价权正在向供给端倾斜。2025年全年中国MDI净出口仅为40万吨，较2024年大幅下降49.6万吨，但进入2026年，前五个月净出口已达到25.8万吨，同比增长5.5万吨。这个拐点意味着什么？中国MDI出口的“量价双杀”阶段已经结束，取而代之的是“量价齐升”的新周期。\n\n> **KC评论：** 这份报告的核心价值不在于告诉你5月数据好，而在于揭示了一个关键转折——中国MDI出口价格连续两个月大幅回升，而同期出口量也在加速。这说明下游需求确实在恢复，而不仅仅是供给端的主动收缩。完整报告中的Table 4提供了长达六年的月度价格序列，值得仔细对比。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧洲正取代美国成为中国MDI出口的第一增量市场\n\n2025年，中国对美国的MDI出口同比下降了83%，这是一个几乎断崖式的下滑。但与此同时，对欧盟27国的出口却在快速回升。2026年前\n\n[... middle omitted ...]\n\n微信群里继续讨论，我们会在第一时间分享最新的数据变化和解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国MDI出口反弹，价格同步回暖\n\n出口量价齐升\n\n5月中国MDI出口101kt，同比大增49%，环比也显著提升。今年前5个月累计出口396kt，同比增长15.6%。同时出口均价环比涨13%、同比涨25%，达到2193美元/吨。\n\n1⃣ 欧洲需求强劲\n前5个月对欧盟出口82kt，同比大增63%；对土耳其出口47kt，增长68%。欧洲成为本轮出口增长的主要拉动力。\n\n2⃣ 进口价格飙升\n5月中国MDI进口均价2979美元/吨，环比暴涨56%，同比翻倍。进口量仅11kt，同比大降65%。\n\n3⃣ 历史对比\n2025年全年出口805kt，同比下降33%。2024年出口1204kt，增长15%。今年出口正在从低点反弹。\n\n欧洲需求回暖+价格回升，MDI出口端信号偏积极。后续关注欧洲补库持续性。\n\n#学习笔记\n\n[source_mineru.md]\n## MDI\n\nChina Exports and Prices in May Lift Y/Y\n\n\\- May MDI exports from China of 101kt were $49\\%$ higher versus 68kt in May of 2025. 2\n\n[... middle omitted ...]\n\nred with \\$1,906/t in April, and 21% higher y/y vs. \\$1,385/t in May 2025. Please see Table 5 for more details.\n\n\\- 2025 net exports were 400kt or (496kt) lower y/y. 2025 exports were 805kt or\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 22 Jun 2026 04:16 PM EDT\n\nDisseminated 22 Jun 2026 04:16 PM EDT"
  },
  {
    "id": "R023",
    "title": "JPM：中国锂贸易已发生结构性逆转，净进口时代开启",
    "digest": "[wechat_article.md]\n# JPM：中国锂贸易已发生结构性逆转，净进口时代开启\n\n中国锂产业正在经历一场被多数市场参与者低估的结构性转变。JPM最新发布的2026年5月中国锂进出口数据显示，中国已经从氢氧化锂的净出口国彻底转为净进口国，同时碳酸锂的进口依赖度正在以超出预期的速度加深。这不仅仅是月度波动，而是一个可能重塑全球锂定价体系与供应链格局的拐点。\n\n2026年前五个月，中国氢氧化锂净进口量达到10.5千吨，而2025年同期还是净出口35.4千吨。碳酸锂净进口量同比增长54.5%，达到151.4千吨。更值得关注的是，5月碳酸锂进口均价同比上涨102%，氢氧化锂出口均价同比上涨64%。价格与量的同步上升，指向的不是短期补库，而是供需关系的底层逻辑在变化。\n\n这份报告的核心判断是：中国锂产业链的“两头在外”格局（上游资源依赖进口、下游产品出口全球）正在被打破，但方向与市场预期相反——中国正在从锂化学品出口国转变为净进口国。这将对全球锂矿商、加工企业以及下游电池制造商的定价权与竞争格局产生深远影响。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 氢氧化锂的贸易地位已发生不可逆转变，中国不再是全球最大供应方\n\nJPM的数据清晰地展示了这一转变的轨迹。从2017年到2023年，中国一直是氢氧化锂的净出口国，净出口量从18.1千吨增长到126.2千吨，年复合增长率超过38%。但2024年净出口量骤降至35.4千吨，2026年前五个月更是直接转为净进口10.5千吨。\n\n月度数据更能说明变化的节奏。2026年1月至5月，中国氢氧化锂出口量分别为1.9千吨、2.6千吨、3.1千吨、5.5千吨和3.5千吨，远低于2023年同期的9.6千吨、10.3千吨、10.2千吨、10.1千吨和11.0千吨。出口量下降了约60%-70%。\n\n与此同时，进口\n\n[... middle omitted ...]\n\n态。欢迎加入我们的知识星球和微信群，在数据中找到自己的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月锂数据，有几点值得聊\n\n碳酸锂进口量创近年新高\n\n📊 5月中国锂贸易数据解析\n\n最近某外资投行更新了中国5月锂进出口数据，几个数字挺有信息量👇\n\n**1️⃣ 碳酸锂进口量飙升**\n5月碳酸锂进口3.76万吨，同比+78%📈\n今年前5个月净进口15.14万吨，比去年同期多54.5%\n——海外货源持续涌入，供应端压力不小\n\n**2️⃣ 氢氧化锂出口大幅下滑**\n5月氢氧化锂出口仅0.35万吨，同比-36%\n今年前5个月中国从净出口变成净进口1.05万吨\n——这个结构性转变值得关注\n\n**3️⃣ 价格端明显回暖**\n碳酸锂进口均价$18,993/吨，环比+15%，同比翻倍\n氢氧化锂出口均价$19,856/吨，环比+33%，同比+64%\n——价格从低位反弹明显，但绝对值仍处历史中位\n\n**4️⃣ 供需格局在变**\n碳酸锂进口量创新高+氢氧化锂出口萎缩\n中国在锂贸易中的角色正在微妙调整\n下游需求恢复情况是后续关键变量\n\n你们觉得下半年锂价走势会怎么走？欢迎一起讨论🤔\n\n#学习笔记\n\n[source_mineru.md]\n## Lithium\n\n## May China Export/Import Data\n\n\\- \n\n[... middle omitted ...]\n\n$9,392/t in May 2025. See Table 6 for details.\n\n\\- The Chinese LiOH export price was 33% higher m/m, and 64% higher y/y in May: prices averaged \\$19,856/t versus \\$14,894/t in April. The avera\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 22 Jun 2026 04:20 PM EDT\n\nDisseminated 22 Jun 2026 04:20 PM EDT"
  },
  {
    "id": "R024",
    "title": "JPM：中国钛白粉出口的“量价齐升”并非故事的全部",
    "digest": "[wechat_article.md]\n# JPM：中国钛白粉出口的“量价齐升”并非故事的全部\n\n中国钛白粉出口正在经历一个被市场低估的结构性转变。JPM最新发布的2026年5月出口数据显示，中国钛白粉出口量同比增长13%，出口均价环比上涨8.8%、同比上涨7.0%，达到每吨2218美元。表面上看，这是一组“量价齐升”的乐观信号。但深入拆解这份报告中的细分数据后，一个更复杂的图景浮现出来：真正驱动这一轮变化的，并非总量逻辑，而是产品结构、区域流向和定价权的深层分化。对于关注化工行业、尤其是涉及全球供应链重组的投资者而言，忽略这些细节，可能会错判中国钛白粉企业的真实竞争力和可持续性。\n\n**这份JPM报告的真正价值，不在于告诉你“出口在增长”，而在于揭示了增长的质量正在发生根本性变化。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 氯化法钛白粉正在成为出口增长的核心引擎，而非传统的硫酸法\n\nJPM报告中最具区分度的数据点，是氯化法与硫酸法钛白粉出口的增速差异。2026年前五个月，中国氯化法钛白粉出口量同比增长39%，而硫酸法仅增长6%。这是一个数量级的差距。\n\n氯化法钛白粉代表更高的技术壁垒、更稳定的品质和更高的附加值。长期以来，中国钛白粉出口以硫酸法为主，氯化法占比有限。但2026年的数据表明，中国企业在氯化法领域的产能释放和技术突破，正在加速改变出口结构。5月单月，氯化法出口量达34.4千吨，而2025年同期仅为24.9千吨。\n\n> **KC评论：** 氯化法出口增速是硫酸法的6.5倍，这不仅仅是产品组合的变化。它意味着中国钛白粉企业正在从“低成本、大路货”的定位，向中高端市场渗透。对于投资者而言，关注各家企业氯化法产能的释放节奏，远比关注总出口量更有意义。完整报告中的图表6提供了逐月比较，能帮助判断这一趋势的持续性。\n\n这一结构性变化对全球钛白\n\n[... middle omitted ...]\n\n续讨论这些未解问题，我们一起追踪中国钛白粉出口的下一步演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国钛白粉出口：5月数据怎么看\n\n📊 出口量继续高增\n\n5月中国钛白粉出口152.8千吨，同比增长13%。虽然环比4月有所回落，但今年前5个月累计净出口857.2千吨，同比增加14%。\n\n1️⃣ **氯化法增速亮眼**\n今年前5个月，氯化法钛白粉出口同比大增39%，达到212.9千吨。这种高端品类的出口增长值得关注——说明国内产品结构在升级。\n\n2️⃣ **硫酸法环比走弱**\n5月硫酸法出口118.4千吨，同比微增7%，但环比4月明显下滑。不过累计来看，前5个月硫酸法出口仍同比增长6%。\n\n3️⃣ **出口价格持续回暖**\n5月平均出口价2218美元/吨，环比涨8.8%，同比涨7%。经历了去年的价格低谷后，出口价格正在稳步修复。\n\n4️⃣ **主要目的地变化**\n欧盟27国：5月出口17.5千吨，同比增13%，但环比4月下降。前5个月累计出口97千吨，同比增29%。\n印度：前5个月累计出口166千吨，同比大增32%，已占出口总量的19%。\n\n5️⃣ **进口持续萎缩**\n5月进口5.3千吨，同比降29%。进口均价2958美元/吨，环比降8.3%，说明国内替代能力在增强。\n\n整体来看，钛白粉出口保持增长态势，价\n\n[... middle omitted ...]\n\ne same period last year. Exports to the EU totaled 169kt in 2025, accounting for about $9\\%$ of Chinese TiO2 exports. Exports to India rose from 126kt to 166kt year to date or by $32\\%$ .\n\n\\- \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 22 Jun 2026 04:10 PM EDT\n\nDisseminated 22 Jun 2026 04:10 PM EDT"
  },
  {
    "id": "R025",
    "title": "BARC：AI硬件股的估值游戏正在从光学转向服务器",
    "digest": "[wechat_article.md]\n# BARC：AI硬件股的估值游戏正在从光学转向服务器\n\n当市场还在为AI算力需求是否见顶争论不休时，一份来自BARC的最新双周追踪报告揭示了一个更微妙的信号：AI硬件股的隐含估值正在经历结构性分化，而光学板块的“休息”可能只是表象。\n\n这份报告的核心判断是：AI硬件股的隐含PE倍数已经从两个月前普遍的20-40倍区间，跃升至当前的40-60倍区间，但推动这一变化的驱动力正在从光学转向服务器与网络设备。市场对AI的定价逻辑，正在从“谁有AI概念”转向“谁的AI收入能持续兑现”。\n\n这不是一个简单的板块轮动。它意味着，投资者需要重新审视手中AI硬件股的估值锚点——那些被市场赋予高AI溢价的股票，其支撑逻辑是否足够坚实？\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光学板块的估值回调并非基本面恶化，而是市场预期被过度透支\n\n过去两周，BARC追踪的AI概念股平均下跌了中个位数，而光学板块是拖累主力。CIEN下跌25%，FN下跌11%，GLW也出现回调。直观判断是光学需求转弱，但BARC的分析指出，这更多是技术性回调而非基本面逆转。\n\nCIEN在财报前股价已累计上涨107%，远超同期标普500指数11%和纳斯达克22%的涨幅。财报本身并不差，但市场设定的预期过高。当实际数字无法匹配股价已经反映的“完美预期”时，回调便不可避免。FN的下行则更多是受CIEN的连带影响。\n\n> **KC评论：** 这提醒我们一个关键问题：AI硬件股的估值已经高度依赖“预期中的预期”。当股价提前反映了未来两到三个季度的利好，任何微小的miss都会引发剧烈修正。完整报告中的隐含AI PE时间序列图表，清晰地展示了这种预期透支的轨迹——从2月到5月，CIEN的隐含AI PE从58倍飙升至115倍，这个数字本身就意味着市场几乎没有任何容\n\n[... middle omitted ...]\n\n交付问题能否解决？非AI概念股中哪些具备被重新定价的催化剂？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI光学股回调，别慌\n\n光学股降温，AI估值怎么看\n\n最近两轮估值对比，有干货\n\n某外资投行更新了AI板块的估值追踪，两周一次的数据来了。整体看，光学相关股票回调明显，但其他AI标的变动不大。\n\n**1/ 整体表现**\n自5月29日以来，AI组合股价平均下跌中个位数（标普和纳指同期各跌2%）。拖后腿的主要是SMCI（-40%）、CIEN（-25%）和FN（-11%）。HPE逆势涨了12%。\n\n但别被短期波动迷惑——这些股票年初至今平均涨幅仍有近80%。\n\n**2/ 隐含AI估值在变化**\n从2月首次追踪到现在，大部分AI标的隐含PE从20-40倍区间，上移到了40-60倍。GLW、KEYS、CIEN依然偏高，SMCI因公司自身问题仍处低位（目前仅3倍）。\n\n对比两周前：\n- CIEN的隐含AI PE从115倍降到76倍——不是光学赛道不行，是财报前股价涨太多，业绩没达到市场的高预期\n- FN受CIEN拖累，从40倍降到35倍\n- HPE从55倍升到58倍，受益于财报超预期+激进投资者入股消息\n\n**3/ 非AI板块表现平淡**\n非AI标的（如AAPL、GRMN等）同期平均下跌中高个位数，估值变动不大，整体偏防\n\n[... middle omitted ...]\n\ns since we started this series. Recall, we started this analysis to assess what was embedded for our AI-related stocks across different sub-segments and exposure percentages.\n\nSince the last r\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R026",
    "title": "Citi：端午出游数据背后，中国消费韧性比想象中更“挑”",
    "digest": "[wechat_article.md]\n# Citi：端午出游数据背后，中国消费韧性比想象中更“挑”\n\n当宏观数据与微观体感出现背离时，市场往往倾向于相信悲观的一面。但2026年端午假期的中国旅游数据，却讲述了一个更精细的故事。\n\n根据中国文化和旅游部最新数据，端午三天假期（6月19-21日），国内旅游人次同比增长4.4%，旅游收入同比增长4.0%。在同期全国交通客运量同比下降0.9%的背景下，这份成绩单显得尤为突出。\n\nCiti团队在最新发布的报告中明确指出，这一数据“超出了我们的预期”。他们的核心判断是：中国休闲旅游需求依然坚韧，而出行结构正在发生深刻分化——非旅游目的的出行在减少，但休闲度假的意愿并未消退。\n\n对于关注中国消费市场的决策者而言，这份报告的真正价值不在于确认“旅游复苏”，而在于揭示了一个更关键的变化：消费的韧性正在从“总量驱动”转向“场景驱动”，而能够识别并服务于特定场景的企业，正在获得定价权。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 交通数据与旅游数据的背离，恰恰证明休闲消费的韧性\n\n端午假期，全国交通客运总量同比下降0.9%，其中占主导地位的自驾出行下降2.1%。这一数字很容易被解读为“消费意愿不足”。但Citi分析指出，这种背离恰恰说明了问题的另一面。\n\n雨天减少了非旅游目的的出行需求——通勤、探亲、短途办事等被压缩，但休闲旅游需求保持了韧性。换句话说，人们不是不出门了，而是“不出无意义的门”。当出行被赋予明确的“休闲度假”目的时，消费者的决策并未动摇。\n\n这意味着什么？对于旅游、酒店、免税等行业的观察者而言，判断消费趋势的指标需要从“人流量”转向“人均消费意愿”和“有效出行目的”。宏观交通数据可能掩盖了结构性的消费韧性。\n\n> **KC评论：** Citi这个观察非常关键。市场习惯用“出行人数”来推断消费景气度，但这份\n\n[... middle omitted ...]\n\n论。那里会有更深入的交流，也有更多来自一线从业者的实战视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午出游数据出炉，休闲需求撑住了\n\n🧳 端午出行，韧性还在\n\n端午三天假，国内旅游数据出来了。文旅部口径：游客1.24亿人次，同比+4.4%；旅游收入444.56亿，同比+4.0%。人均消费小幅下滑0.4%。\n\n有意思的是，交通部口径的人流量同比-0.9%（主要受自驾拖累），但文旅部的旅游数据却正增长。投行研报分析，这背后可能是：雨天压制了非旅游出行需求，但休闲旅游需求本身依然坚挺。\n\n1️⃣ 住宿：区域分化明显\n上海OCC（入住率）同比+1.6%。研报认为，像亚朵这类品牌，在端午期间RevPAR（每间可售房收入）有望实现正增长，OCC和ADR（平均房价）都有改善。\n\n2️⃣ 海南免税：买家多，人均降\n海口海关数据，端午离岛免税销售额2.02亿，同比+8.6%。增长靠买家数量（+11.2%）拉动，但人均消费5961元，同比-2.3%。买的人多了，但单次花得更谨慎。\n\n3️⃣ 出入境：双向回暖\n端午日均出入境人员220万人次，同比+12.9%。内地居民出境+5.5%，港澳台居民+18.4%，外国人入境+23.3%。免签入境外国人同比+15.2%，入境游势头不错。\n\n研报总结：虽然宏观和天气有不确定性，但休闲旅游\n\n[... middle omitted ...]\n\n to trend well. While macro and weather uncertainty may linger, we expect that resilient leisure travel demand, solid inbound travel momentum, and normalized industry supply should continue to\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R027",
    "title": "Citi：端午节旅游数据背后的真正信号——OTA行业正在经历一场“消费降级式繁荣”",
    "digest": "[wechat_article.md]\n# Citi：端午节旅游数据背后的真正信号——OTA行业正在经历一场“消费降级式繁荣”\n\n端午节三天假期，中国国内旅游人次1.24亿，旅游收入445亿元，同比分别增长4.4%和4.0%。如果只看这两个数字，你可能会得出“消费复苏平稳”的结论。但Citi这份研报真正值得关注的判断，藏在一个不起眼的细节里：**人均消费同比下降0.4%**。\n\n这不是一个季度的问题。从2026年元旦到端午节，人均旅游消费同比增速分别为-1.0%、-0.2%、-0.2%、-0.7%、-0.4%。连续五个假期，人均消费持续收缩。与此同时，出游人次却保持正增长。\n\n这意味着什么？Citi的结论是：国内旅游市场整体表现“有韧性”，但韧性来自量的扩张，而非价的提升。对于OTA平台而言，这轮增长的红利，正在从“卖更贵的机票和酒店”转向“卖更多的低价短途产品”。\n\n这并不是一个坏消息。Citi仍然维持对携程和同程旅行的买入评级。但这份报告真正有价值的，不是结论本身，而是它揭示的一个结构性变化：当人均消费持续下行，OTA平台的竞争逻辑正在被重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 人均消费连续五个假期下滑，这不再是天气或油价可以解释的短期波动\n\nCiti报告提供了一个非常重要的数据序列。从2026年元旦到端午节，国内旅游人均消费分别为597元、1348元、455元、571元、359元，同比增速全部为负值。\n\n| 假期 | 人均消费（元） | 同比增速 |\n|------|--------------|---------|\n| 2026元旦 | 597 | -1.0% |\n| 2026春节 | 1,348 | -0.2% |\n| 2026清明 | 455 | -0.2% |\n| 2026劳动节 | 571 | -0.7% |\n| 202\n\n[... middle omitted ...]\n\n起追踪暑期旺季的数据变化，验证或修正Citi这份报告的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午数据拆解：OTA板块韧性在哪\n\n出行数据有韧性\n\n端午3天假期，国内旅游人次1.24亿，旅游收入445亿元，同比增长4.4%和4.0%。人均消费359元，同比下降0.4%，消费力略弱但量在撑。\n\n交通口径：总客运量6.48亿人次，同比-0.9%。铁路+2.9%，航空+0.6%，公路-1.2%，水路-1.8%。铁路最稳，航空受机票涨价拖累，公路被暴雨影响明显。\n\n跨境数据亮眼\n\n出入境总人次同比+12.9%，内地居民+5.5%，港澳台居民+18.4%，外国人+23.3%。研报认为，在油价上涨背景下，这个表现算有韧性。\n\nOTA平台各有侧重\n\n1️⃣ 携程：热门城市+冷门小县城是两大主力，女性+90后是出行主力，偏好跨省短途游。\n2️⃣ 同程：短途“微度假”持续火热，江浙沪地区最明显，小县城和“村漂”式放松游在升温。\n3️⃣ 飞猪：人均预订金额和酒店间夜数同比上升，消费者偏好品质出行，西北/东北避暑和草原线路需求大增。\n\n研报观点：虽然全国客运总量偏弱，但考虑机票涨价+暴雨+油价影响，整体国内收入和出行数据仍有韧性。携程6月25日发1Q26业绩，管理层对2Q26指引预计偏保守。\n\n#学习笔记\n\n[source\n\n[... middle omitted ...]\n\nion's projection prior to the holiday. Albeit national passenger throughput data a bit weak, we view overall domestic revs and traffic performance resilient, especially considering the surging\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R028",
    "title": "JPM：香港楼市最大的风险不是加息，而是恒指",
    "digest": "[wechat_article.md]\n# JPM：香港楼市最大的风险不是加息，而是恒指\n\n香港房价年内已反弹超过10%，达到JPM全年预测区间的上沿。但这家投行在最新报告中指出，下半年动能可能显著放缓。最值得关注的判断是：市场普遍担忧的资本外流管制和加息预期，可能都不是真正的风险。真正的下行风险，是香港股市的持续疲弱。\n\n过去一个月，恒生指数从高点下跌约15%。按照历史上房价滞后股市3-6个月的经验，这一轮股市回调对楼市的影响，可能才刚刚开始被计入。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 高频数据已出现分化：购房意愿仍在，但行动在放缓\n\nJPM监测的多项高频指标出现了不一致的信号。这是判断市场是否正在转向的关键窗口。\n\n看房预约量近期反而走强，过去三周超过570组，创下年内新高。这说明潜在购房者的兴趣并未消退。然而，实际的成交转化率在下降：一手新盘的首日售出率从此前的超过70%降至64%；35大屋苑的二手成交量连续两周低于60宗。\n\n这种“看房多、成交少”的分化，指向一个典型的观望状态。购房者仍然关注市场，但在股市走弱和利率预期上升的背景下，许多人选择暂缓决策。\n\n> **KC评论：** 看房量是领先指标，成交是滞后指标。领先指标走强而滞后指标走弱，通常意味着市场正处于一个“临界点”之前。如果看房量随后也开始回落，那么观望情绪可能正在向实质性降温转化。完整报告中有详细的高频数据图表，可以帮助读者自行判断这一拐点的位置。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 两个已知的“达摩克利斯之剑”可能被高估了\n\n过去一个月，市场最关注的两个风险是：内地资本外流管制可能收紧，以及美联储加息预期升温。JPM的观点是，这两个因素方向性负面，但单独来看，可能不足以逆转当前的上行周期。\n\n关于资本外流管制，报告\n\n[... middle omitted ...]\n\n的动态变化。欢迎来我们的星球和微信群继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港楼价已涨超预期，下半年涨势会慢下来吗？\n\n**涨势放缓，但周期未结束**\n\n今年迄今二手楼价指数已反弹10.4%，甚至已经达到了某外资投行对全年的预测区间（10-15%）。这意味着，若维持预测不变，下半年楼价增速可能放缓至5%以下。\n\n1️⃣ **最大下行风险不是政策，是股市**\n\n市场之前主要担心两个问题：资本外流管制和加息预期。但投行认为，真正值得关注的其实是港股持续走弱——历史数据显示，恒指与香港楼价有3-6个月的滞后相关性。如果恒指持续疲软，楼价压力会逐步显现。好在库存、租金增长、人口等基本面还在健康区间，所以判断上行周期未结束，只是速度会变慢。\n\n2️⃣ **高频数据出现分歧**\n\n过去四周二手楼价指数仍稳中有升（+1%），但该指数有3周滞后，近期股市下跌和加息担忧的影响尚未完全反映。\n- 新房首日去化率从>70%降至64%（部分因开发商定价偏进取，平均比二手高23%）\n- 35大屋苑二手成交量连续两周低于60宗\n- 但周末看房预约量反而更强（>570组，年内最强）——买家兴趣还在，但更多人转入观望。\n\n3️⃣ **库存仍处健康水平**\n\n一手市场未售库存约1.67万套，对应9个月库存量；即便假\n\n[... middle omitted ...]\n\norically shown a strong correlation to HK home prices (typically with a 3-6 month lag). Fortunately, other sector fundamentals (e.g. inventory, rental growth, population) are still intact, and\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R029",
    "title": "JEF：中国大模型正在用“成本-智能”剪刀差改写全球AI竞争格局",
    "digest": "[wechat_article.md]\n# JEF：中国大模型正在用“成本-智能”剪刀差改写全球AI竞争格局\n\n当市场还在争论AI泡沫何时破裂时，一份来自JEF的研报揭示了一个正在发生的结构性变化：中国大模型在智能水平上已接近美国同级产品，但API成本仅为后者的一个零头。这个“成本-智能”剪刀差的持续扩大，正在从根本上改变全球AI产业的价值分配逻辑。\n\n这不是一个关于“追赶”的故事，而是一个关于“重新定义竞争规则”的故事。\n\n这份长达50多页的研报通过追踪OpenRouter、Artificial Analysis等多个数据源的Token消耗、模型定价和智能指数，给出了一个清晰但尚未被市场充分定价的判断：中国AI产业链正从“成本优势”向“规模优势”切换，而字节跳动的火山引擎大会、腾讯的微信AI内测、以及阿里巴巴蔡崇信在VivaTech上释放的信号，都在指向同一个方向——2026年下半年可能是中国AI商业化的关键拐点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国模型在Token消耗上已反超美国，但更关键的是“效率优势”而非“规模优势”\n\n根据OpenRouter在6月15日至21日当周的数据，中国模型Token消耗量达到18.8万亿，而美国模型为5.8万亿。DeepSeek V4 Flash以4.94万亿的周消耗量位居榜首，小米MiMo-V2.5和MiniMax M3紧随其后。\n\n这个数字本身并不令人意外——中国拥有更大的用户基数和更低的使用成本。真正值得关注的不是消耗量，而是这个消耗量背后的“效率逻辑”。\n\nJEF的Silicon Data LLM Token Expenditure Index在6月14日至19日期间维持在1.64至1.68之间，较5月31日的2.04有明显下降。这个指数衡量的是Token消耗的“质量”——当用户向高成本模型迁\n\n[... middle omitted ...]\n\ns。欢迎来星球微信群里继续讨论，一起跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国大模型正用性价比反超\n\n每周Token消耗排名速览\n\nDeepSeek V4 Flash稳居第一\n\n最近看了一份某外资投行的AI研报，数据密度很高，但逻辑清晰。我帮你拆成几个关键点，方便理解。\n\n1️⃣ Token消耗格局变了\n- 中国模型在OpenRouter上的Token消耗首次超越美国模型\n- 上周（6/15-6/21）中国模型消耗18.8万亿Token，美国模型5.8万亿\n- 周环比增长2.12%，整体需求仍在爬坡\n\n2️⃣ 排名速览（按Token消耗）\n1. DeepSeek V4 Flash（4.94T）\n2. 小米 MiMo-V2.5（3.94T）\n3. MiniMax M3（3.77T）\n4. 腾讯 Hy3 preview（3.63T）\n5. OpenRouter Owl Alpha（2.56T）\n6-10. 包括DeepSeek Pro、Anthropic多款模型、智谱GLM 5.2等\n\n3️⃣ 为什么中国模型能跑赢？\n- 架构优势：MoE（混合专家）、线性注意力机制、MLU优化\n- 成本仅为美国模型的几分之一\n- 智能差距在缩小：2026斯坦福AI指数报告显示，美国领先仅2.7%\n\n4\n\n[... middle omitted ...]\n\nn token consumption in OpenRouter, pricing for different models, model intelligence in Artificial Analysis, user trends by sub-sector and other industry data for analysis.\n\nVolcano Engine: ant\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R030",
    "title": "摩根斯坦利：MS：中国消费股的真正考验不是需求，是定价权",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国消费股的真正考验不是需求，是定价权\n\n当市场还在争论消费复苏的力度时，MS最新发布的这份中国消费者行业风险回报更新报告，给出了一个更冷静的判断：对于纸巾、卫生巾、护肤品这些看似刚需的品类，驱动股价的核心变量已经不是需求量的增长，而是企业在渠道碎片化时代能否守住定价权。\n\n这份覆盖恒安国际、中顺洁柔、上海家化三家公司的研报，表面上是在调整盈利预测和目标价，但背后揭示了一个更深层的行业结构性变化——线上渠道和新零售的渗透率提升，正在系统性地侵蚀消费品的平均售价和利润空间。三家公司无一例外地面临同样的困境：销量增长尚可，但价格承压，盈利修复慢于预期。\n\n报告中最值得关注的信号不是某个公司的评级变化，而是MS对三家公司2026/27年净利润预测的大幅下调——中顺洁柔被砍20%/27%，上海家化被砍35%/39%。这组数字背后，是投行对中国消费品公司盈利质量的一次重新定价。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n过去几年，中国消费品市场的一个主流叙事是“集中度提升，龙头企业受益”。但MS的这份报告揭示了一个反直觉的现实：即使行业集中度在提升，龙头企业的定价权并未同步增强。\n\n以恒安国际为例，这家纸巾龙头正在受益于中小厂商退出市场，市场份额持续扩大。但报告明确指出，销量增长的主要驱动力来自中小厂商退出后的份额承接，而非品牌溢价带来的自然增长。更关键的是，线上渠道和新零售渠道占比的持续上升，正在成为平均售价的持续拖累。\n\n这意味着什么？当一个行业的增长主要靠“吃掉别人的份额”而非“让消费者为品牌多付钱”时，规模的扩张并不自动转化为利润的增长。恒安的纸巾业务预计2026年收入增长5%，但毛利率从2025年的23%微降至22.5%——量在\n\n[... middle omitted ...]\n\n述未解问题的持续跟踪感兴趣，欢迎来我们的星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n### 卫品三巨头，谁能先走出价格战？\n\n**投研笔记**\n\n**卫品行业最新观察，谁在承压谁在守城**\n\n---\n\n最近翻了一份某外资投行关于中国消费品（卫品+美妆）的研报，覆盖了恒安、中顺洁柔和上海家化。逻辑很清晰，分享几个关键判断：\n\n**1️⃣ 恒安：守城有余，进攻不足**\n\n纸巾依然是增长主力，靠的是小厂出清后的份额提升。但线上渠道占比越来越高，促销多、定价弱，ASP一直在被稀释。所以量在涨，收入增速却上不去。\n\n卫生巾和纸尿裤更麻烦。卫生巾竞争激烈到新品牌还在烧钱抢份额，今年销售额能持平就算不错了。纸尿裤高端化有亮点，但量跌太快，增量补不了存量。\n\n好消息是木浆成本可控，纸巾毛利率能稳住。但费用率在往上走——要投品牌、投线上、投新零售，利润空间被挤压。整体看，EPS可能微降，靠6%的股息率撑估值。\n\n**2️⃣ 中顺洁柔：量在涨，但定价权是硬伤**\n\n小厂退出确实给了份额空间，但中顺的定价能力非常有限。线上渠道虽然走量，但促销力度大，ASP被压得很低。\n\n毛利率改善空间不大——产品升级和效率提升能托底，但木浆成本和渠道竞争把天花板压住了。\n\n最大的问题是估值。现在对应2026年预期PE还有24倍，\n\n[... middle omitted ...]\n\nmpany invests more in branding and channel expansion. Despite lukewarm earnings trends and a lack of upside catalysts in the near term, Hengan's commitment to Rmb1.4+/share annual payout, equi\n\n[... middle omitted ...]\n\nial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$12.97</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R031",
    "title": "摩根斯坦利：MS：PHEV关税担忧被过度定价，中国车企的缓冲比市场想象的厚",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：PHEV关税担忧被过度定价，中国车企的缓冲比市场想象的厚\n\n中国汽车板块近期的一次集体回调，表面看是欧盟可能将反补贴关税扩展至插电式混合动力车（PHEV）的传闻所致。但MS在6月22日发布的一份研报中给出了一个值得深思的判断：**当前股价下跌已经price in了最坏情景，而中国车企的适应能力，很可能比市场预期的要强。**\n\n这份报告的核心主张并非“风险不存在”，而是“市场对风险的定价已经过头”。在港股恒指仅下跌0.5%的背景下，主要中国车企股价跌幅达到3%至5%。MS认为，这种跌幅更多来自情绪和资金面的共振，而非基本面对PHEV关税风险的直接映射。\n\n我们仔细拆解这份报告后认为，它提供的不是一个简单的“抄底”信号，而是一个重新审视中国车企全球化能力的分析框架。关税风险是真实的，但车企的应对工具箱——从渠道囤货到本地化生产——也比以往更丰富。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这一轮下跌，恐慌情绪比实际风险更值得关注\n\nMS指出了一个被市场忽略的关键细节：**股价跌幅最大的车企，并非那些PHEV出口欧盟占比最高的企业，而是南向资金持仓比例较高的公司。**\n\n这个观察非常敏锐。它意味着今天的抛售，更多是资金层面的“被动减仓”或“避险性卖出”，而不是投资者对特定公司PHEV敞口的精准定价。如果市场真的在理性定价关税风险，那么比亚迪、上汽、吉利这些PHEV出口占比较高的公司应该领跌；但报告数据显示，跌幅分布与南向资金持仓高度相关。\n\n> **KC评论：** 市场有时会“先开枪，再画靶子”。当负面新闻出现时，流动性好的股票往往最先被抛售，哪怕它的实际风险敞口并不大。这份报告提醒我们，区分“情绪驱动的下跌”和“基本面驱动的下跌”，在决策中至关重要。完整报告中还包含一张各车企PHEV出口欧盟\n\n[... middle omitted ...]\n\n我们的星球和微信群继续讨论，一起追踪这些关键问题的后续演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧盟可能对PHEV加税，车市波动\n\nPHEV关税担忧再起\n\n中国车市近期回调，部分原因是担忧欧盟对PHEV加税\n\n---\n\n1. **市场反应有点过度** 🔍\n投行研报判断，今天车股跌3-5%（恒指才跌0.5%），主要是情绪驱动。跌幅大的反而是南向资金多的标的，不一定是PHEV敞口最高的。\n\n2. **PHEV出口占比已翻4倍** 📈\n2024年欧盟对BEV加征7.8-35.3%关税后，PHEV成了“避风港”。中国出口欧盟的车里，PHEV占比从6%飙升到24%。现在欧盟可能要把PHEV也纳入征税范围。\n\n3. **历史不会简单重复** 🤔\nBEV加税后，中国出口总量没受太大影响，只是结构变了。研报推测，如果PHEV也被征，欧盟可能会用不同方式操作。\n\n4. **短期反而可能抢出口** ⏳\n细节确认至少还要1-2个月，车企可能学2024年BEV的做法，先抓紧向欧洲铺货。\n\n5. **谁最受伤？** 🎯\n根据MarkLines数据，上汽、奇瑞、比亚迪在欧盟的PHEV销量占比超20%，吉利、零跑次之。蔚来、小鹏直接敞口有限，今天也跟跌了。\n\n6. **长期靠本地化** 🌍\n研报认为，如果关税蔓延到整个新能源车领域，\n\n[... middle omitted ...]\n\nade PHEVs, after a June 19 report in Handelsblatt (see here for details). The EU has not commented. Chinese-made BEVs have attracted EU duties since 2024, and OEMs have shifted their European \n\n[... middle omitted ...]\n\nd>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.21</td></tr></table>\n\n\\* Historical prices are not split adjusted.  \nStock Ratings are subject to change. Please see latest research for each company.\n\n© 2026 MS"
  },
  {
    "id": "R032",
    "title": "摩根斯坦利：MS：中国生物医药的“全球叙事”正在换剧本",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国生物医药的“全球叙事”正在换剧本\n\n2026年6月17日至18日，MS在上海举办了首届中国生物医药研讨会。这场以“连接生物医药前沿：中国与全球创新”为主题的活动，聚集了超过50家中国生物制药/生物科技公司、20多家全球药企以及10余家PE/VC机构的代表。\n\n这不是一场普通的行业聚会。它发生在全球对中国创新药资产定价逻辑正在发生根本性转变的关键节点。过去三年，市场对中国生物医药的关注高度集中在ADC、双抗和GLP-1这三个工程化能力强的赛道。但这份研报的核心判断是：**全球对中国创新的认知，正在从“工程能力验证”进入“生物学差异化”的第二阶段。**\n\n换句话说，中国生物医药的价值叙事，不再只是“我们做得更快、更便宜”，而是“我们开始思考不同的问题”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 创新1.0的“工程红利”已经定价完毕，但2.0的生物学风险尚未被充分理解\n\n中国生物医药创新1.0的核心优势——工程能力、低成本开发、执行速度——已经成功让全球药企和投资人相信，中国是药物研发价值链上不可忽视的一环。MS研报明确指出，这一阶段的成果已经基本被市场消化和定价。\n\n但真正让这次研讨会值得关注的是，全球药企和PE/VC代表开始认可中国生物医药从“快速跟进”向“差异化生物学和药物形式”的转变。First-in-class（首创）创新正在涌现，尽管仍然处于早期阶段。\n\n> **KC评论：** 这听起来像一句正确的废话，但它的投资含义很具体。如果市场已经给“中国速度”打了分，那么未来超额收益的来源，将取决于谁能真正做“全球新”的生物学。但报告也坦诚地指出，首创创新意味着更高的生物学风险——投资人可能还没有完全意识到这种风险的量级。这恰恰是完整报告中最值得细读的部分：它列出了哪些疾病领域和技术\n\n[... middle omitted ...]\n\n治风险的具体影响路径，或者不同BD模式下的估值差异如何量化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国biotech，正在被全球重新定价\n\n中国创新药，不只是ADC了\n\n某外资投行刚在上海开完中国生物医药论坛，50+中国biotech、20+全球药企、10+PE/VC到场，几个核心判断值得记下来。\n\n**1/ 中国创新进入2.0阶段**\n全球药企和投资人的共识：中国不再只是“快速跟随”，在差异化生物学机制和全新药物模式上开始冒头。虽然first-in-class还早、生物学风险不小，但方向明确。PE/VC重点关注的5个方向：\n- 慢性病的超长效给药平台\n- 肝外递送（siRNA/saRNA）\n- 口服替代生物药/多肽\n- 体内基因编辑\n- 细胞疗法（肿瘤+中枢神经+免疫）\n\n地缘风险仍在，但论坛普遍认为：只要IP和公司结构干净，资产层面的license相对安全。\n\n**2/ BD模式在升级**\n以前主要靠对外授权，现在NewCo、共同开发、战略合作越来越多。全球药企对中国早期发现平台的信心在上升。\n- 买家看：科学依据、数据成熟度、IP风险、全球可转化性、CMC确定性\n- 卖家也学会看：战略契合度、合作伙伴承诺\n- 中国公司最佳准备：临床设计时就按BD标准——高标对照组、数据能进美国监管包、患者多样性、I\n\n[... middle omitted ...]\n\ndels are broadening from pure out-licensing to NewCo, co-co and strategic partnerships to better unlock asset value.\n\n\\- Clean IP, corporate structure and globally translatable clinical develo\n\n[... middle omitted ...]\n\nng Medicine Co. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb11.71</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R033",
    "title": "摩根斯坦利：MS：6月订单透支7月，新能源车市的分水岭不在销量，在“催熟”与“真转化”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：6月订单透支7月，新能源车市的分水岭不在销量，在“催熟”与“真转化”\n\n6月最后一周，中国新能源车市的周订单数据出现了一个值得警惕的信号。根据MS最新发布的周度渠道调研，6月15-21日当周，主要品牌订单总量环比大幅攀升，但推动力高度依赖两个因素：季度末促销冲刺和新车型集中交付转化。MS分析师Tim Hsiao团队在报告中明确警告，这种订单前置正在“inflating bookings ahead of a likely July air pocket”——即6月的繁荣可能正在透支7月的需求，形成典型的“订单空气包”。\n\n这不是一个简单的季节性波动问题。它指向的是中国新能源车市场正在经历的结构性分化：真正依靠产品力实现“自然转化”的品牌，与依赖促销和订单前置“催熟”的品牌，正在走向截然不同的命运。这份报告的核心判断是，新车型驱动的转化是可持续的，而促销驱动的订单前置将在7月暴露真实需求底色。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 季度末促销正在制造一个“虚假繁荣”的6月，7月订单大概率显著回落\n\nMS的调研数据显示，6月15-21日当周，比亚迪订单达到10.45-10.5万辆，环比暴增61%，同比也有30%的增长。这一数字表面上看极为强劲，但报告明确指出，支撑这一增长的核心因素是唐系列新车型的预订单转化，以及季度末更为激进的促销活动。\n\n“Pull orders forward”是这份报告的关键词。季度末促销的本质，是将原本可能在7月或更晚时间发生的购买决策，通过折扣和限时优惠提前锁定。这种做法在财务报表上会美化6月的交付和订单数据，但代价是7月的需求池被提前抽干。MS用“air pocket”来描述7月的预期状况，这个词在航空术语中指气流导致的突然失重，在汽车行业语境下，意味着订单\n\n[... middle omitted ...]\n\n中国新能源车市场的交叉验证观点，欢迎来星球微信群里继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月第三周新能源订单：新车带节奏，促销抢跑7月淡季\n\n**新能源周报｜谁在冲量？**\n\n**6月第三周订单分化加剧：新车拉动明显，促销透支7月需求**\n\n刚刚过去的一周（6/15-6/21），新能源车市订单分化进一步拉大。投行研报跟踪显示，新车型发布/改款成为订单主要驱动力，而缺乏催化剂的品牌则表现平淡。\n\n1️⃣ **比亚迪：周订单10.45-10.5万，环比+61%**\n大唐预售订单集中转化，是本周最大增量来源。\n\n2️⃣ **零跑：周订单1.93-1.95万，环比+43%**\nC系列改款带动明显，同比+93%。\n\n3️⃣ **蔚来：周订单1.42-1.47万，环比-10%**\n乐道L60上市冲高后回落，但ES9本月交付有望超7000台。\n\n4️⃣ **问界：周订单0.91-0.93万，环比+12%**\nM6入门版定价22.98万起，拉动了订单。\n\n5️⃣ **小鹏：周订单0.72-0.74万，环比+6%**\n市场焦点全在7月2日Mona L03首秀。\n\n整体来看，季末促销力度加大，把部分订单提前到6月下旬，7月淡季可能面临订单空窗期。理想L系列受新款L8即将发布影响，订单被暂时压制。\n\n欢迎一起讨论，你\n\n[... middle omitted ...]\n\nannel feedback:\n\nBYD (1211.HK/002594.SZ) 104.5-105k (+61% WoW, +94% MoM, +30% YoY), supported by the pre-order conversion of Great Tang.\n\nGeely Galaxy (0175.HK) 19-19.5k (+12% WoW, -6% MoM, -1\n\n[... middle omitted ...]\n\nPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.35</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R034",
    "title": "摩根斯坦利：半导体设备的下一个瓶颈不是芯片，是连接",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：半导体设备的下一个瓶颈不是芯片，是连接\n\n这份报告最值得看的判断不是DRAM涨价，也不是设备出货量超预期。摩根斯坦利在2026年6月的日本半导体设备月度报告中，提出了一个真正具有结构意义的观点：当Agentic AI从概念走向部署，整个计算架构的瓶颈正在从芯片算力转向内存带宽，并进一步转向设备间的互联能力。这意味着，过去三年市场习惯的“买设备就是买AI基建”的逻辑，正在被重新定义。\n\n市场目前对日本半导体设备板块的定价，基本建立在“AI拉动先进制程、存储扩产”这条主线上。但这份报告揭示了一条更隐蔽、也更值得追踪的线索：Agentic AI的工作负载模式，与Chatbot时代有本质区别。后者是单次请求-响应，前者需要AI代理在数十到数百个循环中反复调用上下文、检索知识、执行推理。这直接导致对DRAM和NAND的需求量级发生指数级跃迁，而非线性增长。\n\n报告给出的数字值得反复推敲：仅NVIDIA Vera CPU的推出，就可能使2025年基础上的总DRAM bit需求增加约16%。这不是一个增量，而是一个跳变。更关键的是，报告指出，连接性将成为下一个瓶颈——当芯片和内存的密度足够高时，信号在铜缆上能传输的距离本身就成了物理限制。\n\n> **KC评论：** 这意味着，市场目前对半导体设备公司的估值，可能还没有充分反映“互联设备”这一细分赛道的结构性溢价。报告没有直接给出买入建议，但它提供的框架暗示：那些在测试、互联、封装环节有技术壁垒的公司，其增长曲线可能比纯前道设备公司更陡峭。完整报告中有详细的互联设备收入拆分和竞争格局分析，值得细读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Agentic AI正在改变内存需求的“量纲”，而非“斜率”\n\n市场对AI拉动存储需求的认知，基本停留在“HBM供不应求\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本半导体设备：AI正在吃掉整个内存\n\nAI吃掉内存，设备厂吃饱\n\n最近某外资投行出了份日本半导体设备月报，核心就一句话：AI对内存的需求，正在从“聊天”进化到“干活”，量级完全不一样了。\n\n1/ 过去AI聊天，一次问答就结束，内存需求有限。\n现在AI要当“代理”，自主完成复杂任务，需要在几十到几百个推理循环中保持超大工作内存。研报估算，仅Vera CPU这类AI芯片，就能让DRAM位需求比2025年增长约16%。\n\n2/ NAND闪存需求也在指数级增长。AI存储架构分为多层：模型权重用DRAM，KV缓存用NAND，向量/嵌入数据也用NAND，底层冷数据才用HDD。Agentic AI带来更长上下文，数据留存要求复合增长，NAND成了关键层。\n\n3/ 下一个瓶颈可能是连接。铜缆信号传输距离有限，随着AI集群规模扩大，互联会成为新的性能天花板。\n\n4/ 业绩端已经验证了趋势。东京电子、爱德万测试、迪斯科等主要设备商，未来几年营收和利润率都在持续上修。爱德万测试被升级为Top Pick，其计算/通信测试业务预计从26财年的7290亿日元增长到29财年的1.875万亿日元，年复合增速约37%。\n\n设备厂这波，吃的是\n\n[... middle omitted ...]\n\n have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.\n\nFor analyst certification and o\n\n[... middle omitted ...]\n\n><td>Ushio (6925.T)</td><td>O (01/05/2026)</td><td>¥4,631</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R035",
    "title": "NOM：端午消费数据透露的信号，比表面数字更值得警惕",
    "digest": "[wechat_article.md]\n# NOM：端午消费数据透露的信号，比表面数字更值得警惕\n\n消费数据正在传递一个清晰的信号：复苏的斜率在放缓，而市场对此的定价可能还不够充分。\n\nNOM在端午假期后发布的一份消费相关研报中，给出了一个简洁但有力的判断：端午假期旅游出行和消费数据表现“平淡”（lukewarm），与五一和春节假期相比，增长动能明显减弱。这份报告的价值不在于它描述了“端午消费不太好”这个现象，而在于它通过对比不同假期的数据、不同出行方式的分化，以及商业区人流与销售额的背离，揭示了一个更值得关注的结构性变化——消费者的支出意愿正在变得更加审慎，而企业需要为此调整预期。\n\n对于产业决策者和投资者而言，当前的关键问题不是“消费会不会突然崩溃”，而是“当消费增速从‘补偿性反弹’回归‘常态化低速增长’，哪些公司还能保持盈利韧性，哪些公司会被暴露在估值风险中”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 端午数据不是孤立事件，而是消费动能系统性回落的第三个信号\n\nNOM报告中最值得关注的一组对比，不是端午数据本身，而是它相对于五一和春节的减速幅度。\n\n端午假期日均旅游出行量约2.16亿人次，同比增速接近零。相比之下，2026年五一假期日均出行量同比增长3.5%，春节假期同比增长8.2%。从8%到3.5%再到接近0%，这不是单次假期的波动，而是一个清晰的减速序列。\n\nNOM将端午数据疲弱归因于三个因素：华南不利天气、出行燃料成本上升、以及更广泛的消费领域持续疲软。天气和燃料成本是短期扰动，但“消费领域持续疲软”才是结构性因素。如果只看端午数据，很容易将增速放缓归因于天气，但结合五一和春节的趋势来看，天气只是加速了已经存在的放缓过程。\n\n> **KC评论：** 消费数据的减速序列比单次数据更有说服力。8%到3.5%到接近0%的增速递减，意味着即使\n\n[... middle omitted ...]\n\n结构性的？哪些细分赛道仍然具备结构性增长机会？欢迎你的加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午出行数据：平淡但没崩\n\n消费风向标\n\n端午出行数据透露了哪些信号？\n\n刚过去的端午假期，整体旅游出行量约6.48亿人次，日均2.16亿，同比几乎持平。这个增速比五一（+3.5%）和春节（+8.2%）都慢了一截。\n\n原因不难理解👇\n\n1️⃣ **南方暴雨拖累出行**\n华南地区天气不太给力，直接影响短途游和自驾意愿。\n\n2️⃣ **出行成本在涨**\n燃油等交通费用上升，部分家庭可能减少了非必要出行。\n\n3️⃣ **消费大环境偏弱**\n整体消费意愿还在修复中，假期效应在递减。\n\n**分交通方式看：**\n- 铁路客流同比+2.9%，比五一（+4.6%）放缓\n- 自驾出行转负，同比-2.1%（五一为+2.6%）\n- 航空恢复正增长，同比+0.6%（五一为-5.7%）\n\n**出境游有小幅回暖**，端午跨境客流约670万人次，同比+12.9%，比五一（+3.5%）明显改善。\n\n**线下消费方面**，全国78个重点商圈客流同比+4.0%，销售额+3.5%，但增速都低于五一（+5.0%和+5.3%）。\n\n整体来看，端午数据不算差，但动能在减弱。消费复苏不是一条直线，天气、成本、信心都在影响节奏。\n\n你觉得下半年消费会怎么走\n\n[... middle omitted ...]\n\ny, respectively). We believe the lackluster Dragon Boat holiday tourism traffic was mainly due to: 1) unfavourable weather in South China, 2) increased travel fuel costs, and 3) continuation o\n\n[... middle omitted ...]\n\n front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R036",
    "title": "Citi：铝价缺口比市场想象的更深，中国铝业和中国宏桥的买入窗口已打开",
    "digest": "[wechat_article.md]\n# Citi：铝价缺口比市场想象的更深，中国铝业和中国宏桥的买入窗口已打开\n\n市场对电解铝行业的担忧主要集中在两个数字上：48百万吨和霍尔木兹海峡。前者是中国国家统计局4月年化产量引发的产能上限恐慌，后者是中东供应恢复可能带来的价格冲击。但Citi在6月22日发布的这份研报中，给出了一个与市场直觉相反的核心判断——这两个担忧都被夸大了。中国产能并未触碰天花板，海外供应恢复的速度将慢于需求修复的速度。结论是：铝价和行业利润将维持高位更久，当前股价回调是增持中国铝业和中国宏桥的窗口。\n\n这份报告没有停留在简单的供需平衡表推演，而是通过拆解数据来源的可靠性、海外产能恢复的实际节奏、以及价格弹性对利润的杠杆效应，构建了一个从宏观商品判断到个股估值锚定的完整逻辑链。以下是核心要点的梳理与解读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对48百万吨产能上限的恐慌，源于一个被误读的数据\n\n投资者最直接的焦虑来自中国国家统计局4月公布的电解铝产量数据。按该月产量年化计算，中国运行产能已逼近48百万吨，这被解读为产能天花板政策可能被突破的信号。\n\nCiti在报告中直接否定了这一推论。该机构指出，国家统计局的月度产量数据本身波动极大，行业参与者更少使用。以5月数据为例，年化产量已回落至45.8百万吨。更关键的是，自从2025年3月以来，统计局数据计算出的月均运行产能多次出现环比下降，这与行业实际感受——利润率持续攀升带动产能利用率走高——完全背离。\n\n> **KC评论：** 这段话的核心价值不在于指出统计局数据有误差，而在于点明一个投资逻辑：当市场对一个“坏数据”做出过度反应时，往往提供了逆向买入的机会。Citi通过交叉验证行业数据源（Mysteel、SMM与国家统计局），确认产能政策没有变化，这就把“产能突破天花板”这个\n\n[... middle omitted ...]\n\n欢迎加入我们的星球微信群，继续讨论铝价周期和个股估值的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铝价高位还能持续吗？研报拆解\n\n铝价还能涨？三个逻辑捋清楚\n\n最近铝板块关注度挺高，刚好看到一份投行研报，把核心逻辑拆给大家。\n\n**1/ 产能天花板没变，别被数据带偏**\n市场担心国内产能已经逼近4800万吨天花板，但研报认为这是4月统计局数据的“假象”——5月数据已经回落至4580万吨。行业机构Mysteel的数据更平滑，显示实际运行产能只有4530万吨，产能管控政策没有松动。\n\n**2/ 海外供给短期偏紧**\n中东霍尔木兹海峡恢复通航后，可运出的铝库存不到40万吨，远低于市场预期。印尼新增产能受电力建设制约，2026年海外新增产能185万吨，但实际产量反而同比减少160万吨。2027年恢复后才有增量。\n\n**3/ 供需缺口支撑价格**\n大宗商品团队预计2026年全球铝市场存在约200万吨的供给缺口，2027年缺口收窄至27万吨。预计三季度铝价维持在4000美元/吨左右。利润高位+强现金流=企业有空间维持分红回购。\n\n两家公司中国宏桥和中国铝业，当前估值在6-8倍PE区间，对铝价弹性很大——铝价每变动10%，利润弹性在28-35%。\n\n**一点思考**\n铝的供给端约束是明牌，需求端恢复节奏才是变量。中东复\n\n[... middle omitted ...]\n\n and margins will stay higher for longer and the strong free cash flows will continue to support dividends and buybacks for equities. We see the weakness as an opportunity to buy shares. Maint\n\n[... middle omitted ...]\n\nk to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party."
  },
  {
    "id": "R037",
    "title": "GS：日本央行内部已有人要求加速加息，关键看通胀是否会超2%",
    "digest": "[wechat_article.md]\n# GS：日本央行内部已有人要求加速加息，关键看通胀是否会超2%\n\n日本央行6月货币政策会议的意见摘要，表面上只是常规披露。但GS日本经济学家团队在最新研报中捕捉到了一个值得深读的信号：有两位委员明确主张加速加息，认为政策利率应尽快接近中性利率水平。\n\n这并非市场主流叙事。当前全球投资者的注意力仍集中在日本央行何时、以何种节奏缩减购债规模，以及日元汇率是否会继续承压。但GS指出，真正需要跟踪的，是“基础通胀超过2%的风险评估”——这个判断将决定少数派的加速加息主张是否会扩散为央行共识。\n\n换句话说，日本央行下一次加息的时间窗口，可能比市场预期更早，也可能比市场预期更晚。而决定权，掌握在通胀数据手里。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 6月会议并非全员鹰派，但鹰派的声音正在变清晰\n\n6月日本央行的政策决定本身并不令人意外：加息至1%，并从下一财年起停止缩减日本国债购买规模。市场对此已有充分预期。\n\n真正值得关注的，是意见摘要中呈现的观点分歧。\n\n一位委员明确反对加息，认为提高政策利率会抑制企业固定投资，进而同时压低通胀、产出和就业。这位委员的立场代表了对经济复苏可持续性的担忧。\n\n但更多的委员支持加息，理由是两个：经济下行风险已经减弱；基础CPI存在向上偏离2%的风险。\n\nGS的解读是：支持加息的理由中，“通胀超调风险”已经取代“经济过热风险”，成为央行决策的核心变量。这意味着，日本央行的加息逻辑正在从“预防性”转向“应对性”。\n\n> **KC评论：** 这不是日本央行第一次讨论加息，但这是第一次在意见摘要中出现“基础通胀可能超过2%”的系统性担忧。对投资者来说，这意味着日本央行的加息决策将越来越依赖实际通胀数据，而非经济增速。谁在跟踪日本的核心CPI分项，谁就能预判下一次加息时点。\n\n![研报原图 2](as\n\n[... middle omitted ...]\n\n这里，我们不只是翻译研报，而是帮你提炼出真正值得关注的信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本央行的“鹰派声音”越来越多了\n\n📈 加息节奏可能加快\n\n6月会议纪要透露了重要信号：有两位委员明确呼吁加快加息步伐，希望“尽快将政策利率向中性利率靠拢”。目前这还不是主流观点，但值得关注。\n\n1️⃣ 加息共识形成\n- 多数委员认为经济下行风险减弱\n- 核心CPI有突破2%的风险\n- 只有一位委员（Asada）反对加息，担心抑制需求\n\n2️⃣ 鹰派声音浮现\n- 一位委员认为中性利率在2%左右\n- 建议“每隔几个月考虑加息”\n- 虽然只有两位，但后续可能扩散\n\n3️⃣ 国债购买调整\n- 决定从下财年起停止减少购买日本国债\n- 多数委员认为市场功能已改善\n- 但需注意市场稳定\n\n核心看点：未来加息的节奏取决于对核心通胀是否持续超过2%的判断。如果通胀风险上升，鹰派观点可能获得更多支持。\n\n欢迎一起讨论日本货币政策走向~\n\n#学习笔记\n\n[source_mineru.md]\n# Japan: BOJ Summary of Opinions from June MPM: Two Members Call for an Acceleration in the Pace of Rate Hikes\n\nBOTTOM LI\n\n[... middle omitted ...]\n\nMAIN POINTS\n\nOn June 24, the BOJ released the Summary of Opinions from its June Monetary Policy Meeting, where it decided to raise the policy interest rate to $1\\%$ and to halt the reduction o\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R038",
    "title": "Bernstein：半导体唯一的游戏还在，但拥挤度已到历史极值",
    "digest": "[wechat_article.md]\n# Bernstein：半导体唯一的游戏还在，但拥挤度已到历史极值\n\nAI主题已经膨胀到几乎拖拽整个半导体板块前进的地步——除了一个反常的例外：AI算力公司本身。这是Bernstein最新一期半导体周期速览报告给出的核心判断。报告作者Stacy Rasgon团队用一份详尽的“Tearsheet”展示了当前周期的位置，结论是：AI需求毫无放缓迹象，但几乎所有跟踪指标都在亮黄灯。估值、拥挤度、库存天数，每一个都在警示风险，而市场的反应却是继续加注。\n\n这份报告最值得注意的判断并非“AI还会涨”，而是：**当前这轮行情的驱动力已经切换，从基本面改善转向了“只有这一个游戏可玩”的叙事惯性。** SOX指数年初至今上涨107%，是标普500涨幅的11倍。但Forward EPS同期也上涨了75%。这意味着估值扩张并非全部，盈利增长提供了支撑。但问题在于，当几乎所有非AI公司都在强行构建AI叙事时，市场已经进入了一个“只要沾上AI就能涨”的状态。\n\n对于产业决策者和投资者而言，真正需要回答的问题是：这个状态还能持续多久？Bernstein的答案是——可能比大多数人预期的更久，但途中会有剧烈颠簸。\n\n> **KC评论：** 报告的核心洞察是“唯一可玩的游戏”，而不是“唯一的增长”。这暗示了资金流向的集中度风险。当所有人都在追逐同一主题时，一旦出现任何边际变化，调整的幅度也会是同等的。完整报告中的Tearsheet图表（Exhibit 1）用红绿灯系统标出了7个关键指标的状态，其中6个已经从三个月前的“中性”转为“负面”。这些图表值得细看。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 真正的“输家”是AI算力公司本身，但它们的估值却出奇便宜\n\n这是一个反直觉的现象。Bernstein指出，当市场注意力从GPU转向内存、半导体设\n\n[... middle omitted ...]\n\n司的基本面恶化正在被市场忽视、以及WFE支出的长期可持续性。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI热潮下，半导体板块是唯一选择吗？\n\n🔥半导体板块，现在还能看吗？\n\n最近AI的热度，简直是拉着整个半导体板块一起跑。除了那些AI计算公司自己，其他环节几乎都被带飞了。\n\n1️⃣ **AI需求到底有多猛？**\n目前来看，AI需求没有任何放缓迹象。从内存、设备、光通信到模拟芯片，几乎所有环节都供不应求。而且这种状态，大概率还会持续好几年。\n\n2️⃣ **涨了这么多，估值贵不贵？**\n确实涨了不少，但今年板块的涨幅主要靠业绩增长支撑。SOX指数年初至今涨了107%，而远期EPS也同步增长了75%。泡沫可能还没到真正疯狂的时候。\n\n3️⃣ **哪些方向值得关注？**\n- **AI计算龙头**：NVDA和AVGO依然是核心受益者。虽然大家总在找“瓶颈环节”，但如果这两家不涨，其他环节也很难独善其身。\n- **CPU/GPU**：AMD在CPU和AI方面都有机会，预计2028年EPS能达到20美元。英特尔虽然基本面仍有挑战，但市场环境和叙事都在变好。\n- **半导体设备**：WFE（晶圆厂设备）需求还有上升空间，尤其看好DRAM和先进封装。AMAT在DRAM和估值上更有优势。\n- **模拟芯片**：TI和ADI已经复\n\n[... middle omitted ...]\n\nn so large that it is now dragging everything in the space along with it (except, perversely, the AI compute names themselves). But the appetite to play the constraint/bottlenecks has continue\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R039",
    "title": "Bernstein：车企造人形机器人，真正的护城河不在机器人本身",
    "digest": "[wechat_article.md]\n# Bernstein：车企造人形机器人，真正的护城河不在机器人本身\n\n汽车制造商正在集体涌入人形机器人赛道。从特斯拉到现代，从小鹏到小米，2026年北京车展上，多家车企的人形机器人成为展台主角。这不是跨界玩票，也不是资本市场的故事新编。Bernstein最新研报给出了一个核心判断：车企进入人形机器人领域，不是多元化，而是主业的自然延伸——它们的竞争优势恰恰来自造车本身积累的硬件、软件和规模化能力。\n\n这份报告的价值不在于罗列谁家机器人走得更好看，而在于它拆解了一个关键问题：当所有车企都在做同一件事，谁真正拥有结构性优势，谁只是在跟风？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 车企造机器人不是跨界，是“降维复用”\n\n理解这一轮车企进军机器人，首先要跳出“机器人是新兴行业”的思维定式。Bernstein的研报从底层逻辑切入：一辆电动车和一个双足机器人，共享的零部件远比外界想象的多。\n\n电机、减速器、传感器——这些构成机器人关节的核心部件，与新能源汽车的电驱系统高度同源。更关键的是制造端。车企现有的生产线、供应链管理能力、质量控制系统，可以直接迁移到机器人的量产过程中。这不仅仅是成本优势，更是时间优势：当纯机器人公司还在为一条产线融资时，车企已经在用现成的工厂做原型迭代。\n\n> **KC评论：** 这份报告最值得细读的是它对“复用”的量化分析。读者可以重点关注研报中关于零部件重叠度和制造成本对比的图表，它们直观展示了为什么车企的起跑线比专业机器人公司靠前得多。完整报告中还有特斯拉和小鹏的零部件拆解对比，值得深入看。\n\n从投资角度看，这意味着：评估一家车企的机器人业务前景，不能只看它机器人本身的技术参数，更要看它能把多少造车能力“平移”过去。那些垂直整合程度高、核心零部件自研比例大的车企，天然拥有更深的护城河。\n\n[... middle omitted ...]\n\n欢迎加入我们的知识星球和微信群，继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n为什么车企都在做人形机器人\n\n车企的“第二曲线”\n\n从特斯拉到小鹏，车企跨界做机器人的底层逻辑\n\n最近某外资投行出了一份报告，专门分析为什么越来越多车企开始做人形机器人。看完觉得逻辑挺清晰，分享几个核心观点。\n\n1️⃣ 车企的天然优势太明显了\n电机、减速器、传感器——这些机器人核心零部件，和智能电动车高度重合。工厂自动化又是第一波落地场景，车企可以在自家工厂里快速迭代、测试，跑通之后再推向市场。这种“自产自用”的模式，成本下降曲线会很陡。\n\n2️⃣ 商业化时间表比想象中近\n报告估算，目前人形机器人在汽车工厂的ROI周期是7-8年，一旦降到5年以下，大规模普及就会加速。按照现在的技术进展和劳动力成本上升趋势，未来3-5年就会看到明显突破。\n\n3️⃣ 头部玩家的策略各有不同\n小鹏的IRON机器人已经能走出“猫步”，目标是消费级场景和情感陪伴；小米把机器人作为“人车家”生态的自然延伸；比亚迪通过投资和自研两条腿走路。每家都在用自己的方式布局。\n\n4️⃣ 供应链机会更确定\n相比整车厂，上游零部件公司可能更值得关注。那些覆盖多种机器人品类、客户基础广泛、核心业务扎实的供应商，确定性更高。\n\n人形机器人会不会成为智能汽车之后的\n\n[... middle omitted ...]\n\nd21878a777.jpg)\n\nEthan Xu\n\n+852 2123 2634\n\nethan.xu@bernsteinsg.com\n\n![](images/6d7960ee48137e650c82c2e0bc2494d8929d5d077465695dec786f7405dabac0.jpg)\n\nWeibin Liang, Ph.D.\n\n+852 2123 2666\n\nweib\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R040",
    "title": "JEF：AI服务器PCB的“Kyber延迟”比想象中更值得警惕",
    "digest": "[wechat_article.md]\n# JEF：AI服务器PCB的“Kyber延迟”比想象中更值得警惕\n\n如果2027年你预期AI服务器会全面切换到一种全新的背板架构——Kyber，那现在可能需要重新校准预期。JEF的最新供应链调研指向一个概率极高的结论：这个架构大概率要推迟到2028年，甚至可能被取消。\n\n这个判断的直接后果是：2027年AI PCB和CCL的全球市场规模，将比JEF原先的预测分别减少5%和8%。如果Kyber最终彻底消失，2028年的冲击会扩大到11%和16%。\n\n表面上看，5%和8%的调整似乎不算灾难。但真正值得关注的不是数字本身，而是这件事揭示的产业链权力结构变化：谁在技术迭代中真正受益，谁在承担迭代失败的风险。这份报告给出的答案，对PCB和CCL领域的投资布局有直接含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nJEF的报告指出，Kyber延迟的核心原因在于“正交背板PCB”的复杂程度超出了预期。原本计划用这种PCB替代铜缆线束来实现机柜内部的高速互联，但技术挑战至今仍未解决。供应链早在5月就察觉到端倪，到最近几周，2027年看不到Kyber已经成为一个“高度可能的事件”。\n\n这意味着2027年的Rubin Ultra将延续Oberon架构——也就是当前的NVL72方案。供应链正在努力让Kyber在2028年以简化版（从4-canister缩减为2-canister）落地，但JEF明确表示“可见度很低”。\n\n> **KC评论：** 技术推迟本身不是新闻，但JEF的调研揭示了一个更关键的结构性问题：当下一代架构无法按时落地，现有的Oberon架构生命周期就被迫延长。这对铜缆连接器厂商是利好，因为他们被PCB替代的威胁暂时缓解了。但对PCB厂商来说，这意味着他们预期的“量\n\n[... middle omitted ...]\n\n兴趣，欢迎来我们的星球微信群继续讨论，一起跟踪这些关键信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI芯片互联方案生变，PCB产业链影响几何？\n\n封面：PCB变局解析\n\n副标题：背面连接技术推迟带来的连锁反应\n\n最近读到一份某外资投行的研报，里面分析了AI芯片互联方案可能出现的重大变化，直接关系到整个PCB产业链的未来格局。来拆解一下核心逻辑👇\n\n**1. 关键变化：Kyber结构大概率推迟**\n\n原本计划2027年用在Rubin Ultra上的Kyber/背板PCB，因为机柜内互联技术挑战太大，很可能要推迟到2028年甚至更晚。供应链从5月开始就感知到这个风险，最近几周“2027年看不到Kyber”基本已成定局。\n\n这意味着2027年的Rubin Ultra将继续沿用Oberon结构（也就是NVL72方案）。供应链还在努力争取2028年实现简化版的Kyber，但难度依然不小。\n\n**2. 对市场规模的影响：2027年下调5%-8%**\n\n研报原本预测AI PCB/CCL市场规模：2025年60-70亿/20-30亿美元，2026年120亿/50亿，2027年250亿/120亿，2028年410亿/210亿。\n\n如果Kyber确认推迟，2027年AI PCB/CCL市场规模将比原预期下调5%/8%。如果最\n\n[... middle omitted ...]\n\nonnectivity challenges. Our recent channel checks suggest that, due to the sophistication of orthogonal backplane PCB as a replacement of cable cartridge for intra-rack connectivity, which was\n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R041",
    "title": "摩根斯坦利：日本电子化学品正在经历一场“材料级”的供应链重构",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：日本电子化学品正在经历一场“材料级”的供应链重构\n\n市场对日本电子化学品的关注，长期以来集中在光刻胶、高纯度化学品等“明星材料”上。但摩根斯坦利在2026年6月的最新月度报告中，给出了一个值得警惕的判断：**这一轮产业链变化，真正的结构性机会不在最热门的单品，而在那些被市场低估的“中间层”材料——覆铜板（CCL）和封装材料。**\n\n这份覆盖日本电子化学品板块的报告，维持行业“In-Line”评级，但个股推荐出现了明确的分化。报告最核心的信号是：FC-BGA（倒装芯片球栅阵列）用覆铜板正经历“非常强劲”的需求周期，而中国市场的光刻胶需求是另一大驱动力。但这两条线索背后，隐藏着截然不同的竞争逻辑。\n\n**KC评论：** 大多数投资者习惯用“半导体材料”这个笼统概念来覆盖日本公司。但摩根斯坦利这份报告提醒我们，电子化学品内部已经出现严重分化——材料的结构性短缺和周期性过剩并存。读完整份报告，才能真正理解为什么Resonac被列为“Overweight”，而Tokyo Ohka Kogyo却是“Equal-weight”。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. FC-BGA覆铜板的强劲表现，正在重塑上游议价权\n\n摩根斯坦利报告明确指出，“FC-BGA CCLs”的表现“非常强劲”。这不是一个模糊的行业观察，而是对特定细分赛道的确认。\n\n覆铜板是PCB的核心基材，而FC-BGA封装基板用的CCL，技术要求远高于普通PCB。随着AI芯片、高性能计算对封装密度和信号完整性的要求持续提升，FC-BGA基板的需求在过去18个月持续走高。但真正值得关注的是，摩根斯坦利判断**Resonac很可能启动产能扩张，并进一步提价。**\n\n这意味着什么？在电子产业链中，材料供应商通常处于“被动响应”位置——晶\n\n[... middle omitted ...]\n\n以及Tokyo Ohka Kogyo的MOR产能何时能补上。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本电子化学品，谁在加产能？\n\n📌 三家公司，三条路径\n\n某外资投行刚发了日本电子化学品月报，覆盖 Resonac、Sumitomo Bakelite、Tokyo Ohka Kogyo 三家公司，行业评级维持 In-Line。研报核心判断是：FC-BGA 覆铜板（CCL）表现极强，半导体密封材料在台湾市场走俏，中国需求在拉动光刻胶。\n\n1️⃣ Resonac（评级 OW）\n被认为可能启动产能扩张，并进一步对 CCL 提价。研报给出的潜在回报空间约 21.8%。\n\n2️⃣ Sumitomo Bakelite（评级 OW）\n目前业务强劲——向 Intel 的颗粒封装材料出货在增加，向台积电和其他 OSAT 的液态封装材料也进入了样品供应阶段。潜在回报约 3.8%。\n\n3️⃣ Tokyo Ohka Kogyo（评级 EW）\n增速低于 JSR，研报推测可能与其 MOR 产能较低有关。潜在回报空间为负，约 -15.5%。\n\n📊 从季度利润趋势看，电子材料板块整体利润同比增幅已从 25Q3 的 9% 拉高到 26Q1（实际）的 82%，其中 Resonac 增幅最大（126%），Sumitomo Bakelite 也有 \n\n[... middle omitted ...]\n\nLine\n\nMS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of M\n\n[... middle omitted ...]\n\nr><td>ZEON (4205.T)</td><td>O (10/23/2014)</td><td>¥2,334</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R042",
    "title": "摩根斯坦利：MS：AI投资正从“光学狂欢”转向“网络务实”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI投资正从“光学狂欢”转向“网络务实”\n\n市场对AI基础设施的叙事正在经历一次微妙的但关键的切换。当所有人还在为光模块的订单爆发和激光器产能焦虑时，MS的最新行业反馈揭示了一个正在发生的结构性转向：投资者的关注重心，正从光通信的“需求发现”阶段，移向网络设备的“推理落地”阶段。\n\n这份报告的核心判断并非否定光学的长期价值，而是指出一个短期但重要的节奏变化——过去一个月，网络设备板块上涨6.7%，而光学板块下跌10%。这不是简单的板块轮动，而是市场在用一个更务实的框架重新审视AI基础设施的投资逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光学赛道最大的焦虑已从“需求”转向“利润”\n\n光学的需求故事并未终结。MS明确指出，需求条件仍然强劲，这不是投资者当前争论的焦点。真正的辩论已经上移了一个层次：在增量产能陆续释放、技术路线尚未收敛的背景下，这些订单的利润质量到底能维持多久？\n\n报告梳理了四个关键变量：CPO/NPO技术的落地时间与形态、激光器新玩家的产能扩张、训练与推理之间资本配置的切换对规模光学定价的影响，以及光纤现货市场的价格信号。这些因素叠加在一起，使得光学的短期可见度下降，波动性上升。\n\n> **KC评论：** 这其实是AI硬件投资从“炒预期”进入“验利润”的必然阶段。当所有人都知道订单会增长时，股价的边际驱动力就从“有没有订单”变成了“订单能赚多少钱”。这份报告最值得深读的部分，是它如何拆解不同光学公司的利润结构差异——不是所有光学股都站在同一块地基上。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 一个被市场过度解读的产能新闻：Source Photonics的扩张更像“扰动”而非“颠覆”\n\n上周最引发市场关注的数据点，是苏州\n\n[... middle omitted ...]\n\n继续讨论——很多判断，只有放在持续的数据流中才能验证和迭代。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光模块热度虽高，但市场焦点正在转移\n\n**光模块 vs 网络设备，谁更值得关注？**\n\n最近投行研报聊到一个有意思的现象：市场对光模块的热情开始降温，讨论焦点从“需求增长”转向“利润能否撑住”，而网络设备这边反而更受追捧。\n\n1️⃣ **网络设备：推理需求成为新主线**\n研报发现，市场对网络设备的关注点在“推理”（inference）而非传统的“训练”（training）场景。这个逻辑在ANET和CSCO上得到较多认可，认为未来一个月到财报季仍有支撑。\n\n2️⃣ **光模块：短期波动加大，几个争议点**\n- **CPO/NPO技术路径**：时机和形态还在拉扯，短期难以形成共识。\n- **激光器产能扩张**：苏州东山精密公告投入12亿美元扩建光芯片和模块产能，市场担心竞争加剧。但研报认为Source Photonics是相对小玩家，影响主要在CW激光器端，对EML端冲击有限，LITE/COHR近期的价格波动可能过度反应。\n- **推理 vs 训练**：网络设备侧的推理逻辑，可能改变对光模块“scale-across”场景的需求估算。\n\n3️⃣ **相对清晰的几个标的**\n- **GLW**：研报认为是光模块里最\n\n[... middle omitted ...]\n\n up given concerns around CPO/NPO timing, laser competition, training vs. inference in scale-across.\n\n\\- Cleanest setup remains with GLW, LITE / COHR becoming more interesting into earnings, s\n\n[... middle omitted ...]\n\norporation (ZBRA.O)</td><td>E (12/02/2024)</td><td>$235.98</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R043",
    "title": "JPM：AI颠覆论被高估，数字银行龙头才是真正的护城河",
    "digest": "[wechat_article.md]\n# JPM：AI颠覆论被高估，数字银行龙头才是真正的护城河\n\n市场对AI颠覆软件行业的焦虑从未消退。当ChatGPT掀起生成式AI浪潮后，每一家SaaS公司都被迫回答一个问题：你的产品会被AI一键替代吗？在数字银行这个细分领域，JPM最新发布的研报给出了一个反共识的判断——AI颠覆风险被明显高估了。\n\n这份覆盖Q2 Holdings、Alkami和nCino三家公司的深度报告，核心结论清晰而锐利：那些深耕银行核心工作流、数据整合与合规要求的垂直SaaS厂商，其护城河远比市场想象的深厚。AI新进入者无法绕过银行监管、历史数据访问权限和复杂系统集成这三道墙。\n\n更关键的是，JPM不仅给出了判断，还明确指出了两条投资主线：Q2 Holdings作为有机增长的优质标的，Alkami作为高确定性的并购候选。而nCino虽然估值有吸引力，但竞争格局和AI叙事的清晰度仍逊一筹。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 银行SaaS的护城河不在于技术，而在于合规与集成复杂度\n\n市场普遍担心AI原生公司会像颠覆内容创作一样颠覆银行软件。但这份研报揭示了一个被忽视的事实：银行软件的核心价值不在代码本身，而在系统集成、合规认证和历史数据积累。\n\nJPM分析师在访问nCino总部后明确指出，客户对底层模型并不敏感，他们真正关心的是谁承担治理与监管责任。nCino联合创始人的观察更为直接——编码只是整个解决方案的一小部分，设计、测试、治理和持续支持才是真正的大头。\n\n这意味着，即使AI能够生成代码，也无法自动完成与银行核心系统的对接、通过监管审计、处理遗留数据的兼容性问题。这些需要数年积累的行业知识和信任关系，才是数字银行SaaS最深的护城河。\n\n> **KC评论：** 很多投资者把AI时代的护城河等同于模型能力，但在银行这个行业，\n\n[... middle omitted ...]\n\n拐点、Alkami的并购时间线、以及AI对定价权的二阶影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数字银行AI护城河被低估了\n\n📊 数字银行研究笔记\n\n最近翻到一份外资投行的数字银行研报，核心观点很明确：市场对AI冲击的担忧可能过头了。\n\n这些公司真正的壁垒不在于技术多新，而在于已经嵌入银行核心流程的数据、合规和系统集成能力——这些是AI新玩家很难短期复制的。\n\n1️⃣ Q2 Holdings（QTWO）是首选\n- 跟Alkami瓜分数字银行市场，签的都是5-7年长约\n- 只覆盖美国2500家区域银行和信用合作社，渗透率才20%\n- 管理层指引FY27订阅收入增长12.5-13%，但研报认为这只是“地板”\n- 未来5年EBITDA利润率从24%提升到约35%，零负债，FCF转化率>90%\n- 目标价60美元（研报给的Dec-27）\n\n2️⃣ Alkami（ALKT）是被收购高概率标的\n- 激进投资者Jana Partners已推动重启出售流程\n- 客户留存率>98%，流失主要来自客户并购而非竞争\n- 私募股权被认为是最可能的买家——能保持处理器中立\n- 目标价19美元，比QTWO多给了2倍溢价，主要就是收购溢价\n\n3️⃣ nCino（NCNO）中性但估值有吸引力\n- 最近去总部调研后，对AI防御能力更乐观\n\n[... middle omitted ...]\n\nverweight, which operate in a consolidated, duopolistic digital banking market with long contract durations, strong gross retention, and clear pathways to meaningful margin and FCF expansion—c\n\n[... middle omitted ...]\n\nmage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is"
  },
  {
    "id": "R044",
    "title": "摩根斯坦利：新兴市场债券的“油价逻辑”尚未兑现",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：新兴市场债券的“油价逻辑”尚未兑现\n\n这份报告的核心判断简洁但有力：油价已经大幅回落，但新兴市场本地货币债券收益率并未同步下行。这中间存在一个10-15个基点的“便宜度”缺口，而摩根斯坦利认为这个缺口将在未来几周被填补。\n\n这不是一份简单的“看多”报告。它更像是一份战术指南：在油价下跌、美联储暂停、风险偏好尚可的三重背景下，新兴市场债券的定价出现了结构性错位，而这种错位恰恰是机会所在。\n\n报告发布的时间点是2026年6月22日，正值美国-伊朗冲突高峰过后、油价从高点显著回落之际。市场对新兴市场的情绪已经从三月的恐慌中恢复，但债券收益率的下行幅度远不及油价跌幅。摩根斯坦利的策略师团队——由James Lord领衔——认为，这种滞后不是基本面问题，而是由三个临时性因素造成的：美国利率走高、美元强势、以及市场对新兴市场央行加息的过度定价。\n\n而这三个因素，都在发生变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油价和新兴市场债券收益率的“脱钩”是一个定价错误\n\n报告最核心的观察来自一个简单的相关性分析。在冲突爆发后的前两个半月，新兴市场本地货币债券指数收益率与油价走势高度同步。但过去一个月，两者出现了明显的背离：油价继续下行，而收益率却停滞不前。\n\n用更宽泛的能源价格指数（Bloomberg Energy Index）来衡量，这种背离幅度约为10-15个基点。换句话说，按照历史关系，新兴市场债券收益率应该比现在的水平低10-15个基点。\n\n> **KC评论：** 10-15个基点听起来不大，但对于一个规模数万亿美元的资产类别而言，这意味着数十亿美元的定价偏差。更重要的是，这种偏差不是由基本面恶化引起的，而是由三个“临时性因素”造成的——这意味着它更可能被修复，而不是持久存在。\n\n为什么收益率没有跟\n\n[... middle omitted ...]\n\n工快速把握全球市场的动态变化。欢迎加入我们的微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储换人，新兴市场继续看好\n\n别慌，逻辑没变\n\n最近美联储人事变动让不少人紧张，但某外资投行最新研报直接说：别慌，新兴市场逻辑没变。\n\n1/ 油价跌了，但新兴市场债券收益率降得还不够。核心原因是美国利率还在高位、美元强势、市场还在定价新兴市场会加息。不过这些阻力正在消退——研报预计未来12个月新兴市场会降息而不是加息，同时看好新兴市场货币。\n\n2/ 南非兰特和匈牙利福林值得关注。这两个货币提供了利用利率风险溢价的机会。新兴市场货币6月继续对G3货币录得正回报。\n\n3/ 资金流在回暖。经历3月的大幅流出和5月的稳定后，6月资金流入开始回升。研报跟踪的9个新兴市场数据显示，滚动3个月资金流从2月中旬的400亿美元降到5月底的-200亿左右，现在正在反弹。\n\n4/ 新兴市场今年总回报约1.5%，但地区差异很大。拉美是唯一多个国家录得正回报的地区，哥伦比亚超越匈牙利成为最大赢家。亚洲整体落后，只有中国提供正回报。\n\n5/ 外汇期权数据显示投资者仍偏多美元，但对新兴市场货币的乐观情绪在增加。研报继续看好新兴市场货币，认为至少对G3货币会升值。\n\n一个有意思的细节：虽然新兴市场债券收益率还没完全跟上油价下跌，但用更广泛\n\n[... middle omitted ...]\n\ne duration rally.\n\nSome of these headwinds should fade as we generally expect rate cuts from EM over the next 12m, not hikes, and are bullish EM currencies at least vs G3.\n\n■ ZAR and HUF offer\n\n[... middle omitted ...]\n\nAnalysts/Strategists and are not opining on or expressing recommendations on equity securities: Nimish M Prabhune; Simon Waever; Ioana Zamfir; Emma C Cerda; Gek Teng Khoo; Neville Z Mandimika; James K Lord.\n\n## © 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: US remains the most active player in launching activities globally, while China is the most active player among Asia Exhibit 2: Global space object launches (primarily satellites) surged by \\~60% to over 4,500 annually"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 4: Governments across global economies have committed to increased space investment and spending"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Global space object launches (primarily satellites) surged by \\~60% to over 4,500 annually in 2025 Exhibit 4: Governments across global economies have committed to increased space investment and spending The distin"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 4: Governments across global economies have committed to increased space investment and spending The distinction between core/established and early-growth/emerging segments is important in assessing exposure to the theme."
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Space-themed funds have seen meaningful inflows since 2015, with aggregate AUM reaching US\\$24bn across 40+ funds globally Exhibit 7: Asia supply chain companies remain materially underrepresented in global thematic al"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Space-themed funds have seen meaningful inflows since 2015, with aggregate AUM reaching US\\$24bn across 40+ funds globally Exhibit 7: Asia supply chain companies remain materially underrepresented in global thematic al"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Asia Space Economy stocks have outperformed the broader regional equity market since 2025, led by Korea and Taiwan suppliers, although performance has recently consolidated following a strong rally in late 2025 Exhibit"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 10: Asia Space Economy stocks have continued to see earnings growth and upward revisions over the past year, led by Japan and Korea, although partly offset by weaker trends in China Forward 12M EPS of Asia Space Economy Bask"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 12: Asia Space Economy stocks broadly tracked global peers but underperformed in April–May amid strong thematic ETF inflows into global names, before rebounding since June as US peers likely faced liquidity drag Exhibit 11:"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Market Composition of GS Asia Space Economy basket (GSSZSPCE) Exhibit 13: Valuations remain relatively attractive for Asia Space Economy stocks, which are trading at deep P/E and P/B discounts to global peers, near the l"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 11",
    "context": "Exhibit 14: Market Composition of GS Asia Space Economy basket (GSSZSPCE) Exhibit 13: Valuations remain relatively attractive for Asia Space Economy stocks, which are trading at deep P/E and P/B discounts to global peers, near the l"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Business Category Exposure of GS Asia Space Economy Basket (GSSZSPCE)"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 13",
    "context": "Exhibit 15: Business Category Exposure of GS Asia Space Economy Basket (GSSZSPCE) ## Asia Space Economy Basket (GSSZSPCE)"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Business Category Exposure of GS Asia Space Economy Basket (GSSZSPCE) ## Asia Space Economy Basket (GSSZSPCE) Selection Criteria: Stocks with exposure to the defined Space Economy business categories, based on RBICS su"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 1: Middle East/US Gulf/West Africa-China VLCC TCE +122%/+6%/-20% vs. pre-conflict level Figure 3: Average earnings of Capesize rallied by 11% WoW last week"
  },
  {
    "figure_id": "F016",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 1: Middle East/US Gulf/West Africa-China VLCC TCE +122%/+6%/-20% vs. pre-conflict level Figure 3: Average earnings of Capesize rallied by 11% WoW last week Figure 4: Vessels passage at Hormuz picked up while still not"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Figure 2",
    "context": "Figure 3: Average earnings of Capesize rallied by 11% WoW last week Figure 4: Vessels passage at Hormuz picked up while still notably below pre-conflict level Figure 5: Container throughput at China's key ports +3% WoW, +2% Yo"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 6: Container volume new in transit from Asia to US has been showing a front loading pattern"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Figure 4",
    "context": "Figure 7: SCFI +5% WoW and +67% YoY"
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "Figure 5: Container throughput at China's key ports +3% WoW, +2% YoY last week Figure 6: Container volume new in transit from Asia to US has been showing a front loading pattern Figure 7: SCFI +5% WoW and +67% YoY"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "Figure 7: SCFI +5% WoW and +67% YoY Figure 8: SCFI Shanghai-WC America Container Freight Rate +11% WoW and 105% YoY Figure 9: Container ships re-routing away from Red Sea still at high levels (+4-5% YoY) Figure 10: Intra-Asia"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Figure 8",
    "context": "Figure 11: Strong VLCC demand drives up YTD strong global shipbuilding demand"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Figure 9",
    "context": "Figure 12: Both Clarksons and CNPI indicate new build price remain elevated"
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Figure 10",
    "context": "Figure 10: Intra-Asia chartering index recovered WoW last week Figure 11: Strong VLCC demand drives up YTD strong global shipbuilding demand Figure 12: Both Clarksons and CNPI indicate new build price remain elevated"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Figure 11",
    "context": "Figure 11: Strong VLCC demand drives up YTD strong global shipbuilding demand Figure 12: Both Clarksons and CNPI indicate new build price remain elevated This report leverages the following UBS Evidence Lab asset: Global Mariti"
  },
  {
    "figure_id": "F026",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "(a) With regard to the economy, the latest important development is that tensions in the Middle East have started to ease, with the US and Iran signing a memorandum of understanding on 18 June (US time). However, in order for global economic activity to normal"
  },
  {
    "figure_id": "F027",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "This suggests that it will take time for quantitative supply constraints, which have a direct bearing on the economy, to ease even as the situation in the Middle East eases. Looking ahead, we will need to keep a close eye on the extent of the recovery in petro"
  },
  {
    "figure_id": "F028",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "Fig. 2: Sharp decline in imports of oil and petroleum products Fig. 3: Delays in delivery of raw materials and parts ## Prices: We expect CPI inflation to peak in 2027 Q1 The second factor that will need to be monitored to see whether the BOJ is likely to cont"
  },
  {
    "figure_id": "F029",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "## Prices: We expect CPI inflation to peak in 2027 Q1 The second factor that will need to be monitored to see whether the BOJ is likely to continue to hike interest rates is (b) prices. prices of the three main crudes (Dubai, WTI, and Brent) have been edging l"
  },
  {
    "figure_id": "F030",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "The second factor that will need to be monitored to see whether the BOJ is likely to continue to hike interest rates is (b) prices. prices of the three main crudes (Dubai, WTI, and Brent) have been edging lower in anticipation of an easing of tensions in the M"
  },
  {
    "figure_id": "F031",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "Even if they do, we think it may take until around mid-2027 for price-related supply constraints to spread downstream. This is because of the time it takes for upward pressure on prices to work its way from upstream in the supply chain to downstream. Looking a"
  },
  {
    "figure_id": "F032",
    "report_id": "R005",
    "label": "Figure 8",
    "context": "Home loans have also been rising steadily. As the BOJ raises its policy interest rate, much is often made of the impact on home loan interest rates. However, home loans outstanding at private-sector financial institutions have continued to rise by 3-4% y-y, pa"
  },
  {
    "figure_id": "F033",
    "report_id": "R005",
    "label": "Figure 10",
    "context": "Automobiles accounted for around 12% of Japanese exports (total of goods and services) in 2025, with a higher weighting than for other items. Automobile exports are at the top of any watch list for gauging the outlook for the economy as a whole as they have a "
  },
  {
    "figure_id": "F034",
    "report_id": "R005",
    "label": "Figure 10",
    "context": "Automobile exports to the US and EU have also picked up. However, automobile exports to China remain lackluster (Figure 10). Fig. 10: Auto exports by region Note: Adjusted for inflation and seasonal variation by NOM. Fig. 11: Auto sales volume in China Note: D"
  },
  {
    "figure_id": "F035",
    "report_id": "R005",
    "label": "Figure 12",
    "context": "Moreover, machine tool orders from users in mainland China have continued to rise (Figure 12). In China, investment in related areas such as semiconductors, ICT, and IT services has been growing strongly since the start of this year as a result of rising AI de"
  },
  {
    "figure_id": "F036",
    "report_id": "R007",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Resume Annualized Revenue per Active MW (\\$M) per Segments Annualized Revenue per Active MW (\\$M) EXHIBIT 2: Annualized Revenue per Active MW (\\$M) by Other AI Contracts ## CUSTOMER MIX AND PRICING POWER"
  },
  {
    "figure_id": "F037",
    "report_id": "R007",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Resume Annualized Revenue per Active MW (\\$M) per Segments Annualized Revenue per Active MW (\\$M) EXHIBIT 2: Annualized Revenue per Active MW (\\$M) by Other AI Contracts ## CUSTOMER MIX AND PRICING POWER \\- Colocatio"
  },
  {
    "figure_id": "F038",
    "report_id": "R007",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Colocation Prov - Annualized Q Rental Revenue per Active MW (\\$M, 1Q23-1Q26) Neoclouds - Annualized Revenue per Active MW (\\$M, 1Q24-1Q26) EXHIBIT 4: Neoclouds - Annualized Q Revenue per Active MW (\\$M, 1Q24-1Q26)"
  },
  {
    "figure_id": "F039",
    "report_id": "R007",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Colocation Prov - Annualized Q Rental Revenue per Active MW (\\$M, 1Q23-1Q26) Neoclouds - Annualized Revenue per Active MW (\\$M, 1Q24-1Q26) EXHIBIT 4: Neoclouds - Annualized Q Revenue per Active MW (\\$M, 1Q24-1Q26) EX"
  },
  {
    "figure_id": "F040",
    "report_id": "R007",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Neoclouds - Annualized Q Revenue per Active MW (\\$M, 1Q24-1Q26) EXHIBIT 5: Emerging AI Infra. - Annualized Rental Revenue per Active MW (\\$M) Emerging AI Infra. - Annualized Rental Revenue per Active MW (\\$M) Emergin"
  },
  {
    "figure_id": "F041",
    "report_id": "R007",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: Neoclouds - Annualized Q OPEX per Active MW (\\$M, 1Q24-1Q26)"
  },
  {
    "figure_id": "F042",
    "report_id": "R007",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: Neoclouds - Annualized Q OPEX per Active MW (\\$M, 1Q24-1Q26) Neoclouds - Annualized OPEX per Active MW (\\$M, 1Q24-1Q26) EXHIBIT 9: Neoclouds - Operating Margin per Active MW (%, 1Q24-1Q26)"
  },
  {
    "figure_id": "F043",
    "report_id": "R007",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 9: Neoclouds - Operating Margin per Active MW (%, 1Q24-1Q26) Neoclouds - Operating Margin per Active MW (%, 1Q24-1Q26 EXHIBIT 10: Expected OPEX % Expense"
  },
  {
    "figure_id": "F044",
    "report_id": "R007",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: Expected OPEX % Expense ## ASSET MIX AND CAPITAL INTENSITY"
  },
  {
    "figure_id": "F045",
    "report_id": "R007",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: Neoclouds - CAPEX per New Active MW (\\$M, 1Q24-1Q26) Neoclouds - CAPEX per New Active MW (\\$M, 1Q24-1Q26)"
  },
  {
    "figure_id": "F046",
    "report_id": "R007",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Neoclouds - CAPEX per New Active MW (\\$M, 1Q24-1Q26) Neoclouds - CAPEX per New Active MW (\\$M, 1Q24-1Q26) Across all firms (IREN, CIFR, WULF, CORZ), the major investment is similar to data center REITs in the powered s"
  },
  {
    "figure_id": "F047",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: China crude oil inventory Figure 2: Utilisation of China SOE/teapot refiners Chemical utilisation Figure 3: China ethylene (naphtha cracking) capacity utilisation"
  },
  {
    "figure_id": "F048",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: China crude oil inventory Figure 2: Utilisation of China SOE/teapot refiners Chemical utilisation Figure 3: China ethylene (naphtha cracking) capacity utilisation Figure 4: China ethylene (MTO) capacity utilisation"
  },
  {
    "figure_id": "F049",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: Utilisation of China SOE/teapot refiners Chemical utilisation Figure 3: China ethylene (naphtha cracking) capacity utilisation Figure 4: China ethylene (MTO) capacity utilisation Figure 5: China PE capacity utilisa"
  },
  {
    "figure_id": "F050",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: China ethylene (naphtha cracking) capacity utilisation Figure 4: China ethylene (MTO) capacity utilisation Figure 5: China PE capacity utilisation Figure 6: China PP capacity utilisation"
  },
  {
    "figure_id": "F051",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4: China ethylene (MTO) capacity utilisation Figure 5: China PE capacity utilisation Figure 6: China PP capacity utilisation Figure 7: China PVC capacity utilisation"
  },
  {
    "figure_id": "F052",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: China PE capacity utilisation Figure 6: China PP capacity utilisation Figure 7: China PVC capacity utilisation Figure 8: China PDH capacity utilisation"
  },
  {
    "figure_id": "F053",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: China PP capacity utilisation Figure 7: China PVC capacity utilisation Figure 8: China PDH capacity utilisation Figure 9: China PX capacity utilisation"
  },
  {
    "figure_id": "F054",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 7: China PVC capacity utilisation Figure 8: China PDH capacity utilisation Figure 9: China PX capacity utilisation Figure 10: China PTA capacity utilisation"
  },
  {
    "figure_id": "F055",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 8: China PDH capacity utilisation Figure 9: China PX capacity utilisation Figure 10: China PTA capacity utilisation Figure 11: China Polyester filament capacity utilisation"
  },
  {
    "figure_id": "F056",
    "report_id": "R008",
    "label": "Figure 9",
    "context": "Figure 9: China PX capacity utilisation Figure 10: China PTA capacity utilisation Figure 11: China Polyester filament capacity utilisation Figure 12: China MDI capacity utilisation"
  },
  {
    "figure_id": "F057",
    "report_id": "R008",
    "label": "Figure 10",
    "context": "Figure 10: China PTA capacity utilisation Figure 11: China Polyester filament capacity utilisation Figure 12: China MDI capacity utilisation Figure 13: China TDI capacity utilisation"
  },
  {
    "figure_id": "F058",
    "report_id": "R008",
    "label": "Figure 11",
    "context": "Figure 11: China Polyester filament capacity utilisation Figure 12: China MDI capacity utilisation Figure 13: China TDI capacity utilisation Figure 14: China TiO2 capacity utilisation"
  },
  {
    "figure_id": "F059",
    "report_id": "R008",
    "label": "Figure 12",
    "context": "Figure 12: China MDI capacity utilisation Figure 13: China TDI capacity utilisation Figure 14: China TiO2 capacity utilisation ## Inventory"
  },
  {
    "figure_id": "F060",
    "report_id": "R008",
    "label": "Figure 13",
    "context": "Figure 13: China TDI capacity utilisation Figure 14: China TiO2 capacity utilisation ## Inventory Figure 15: Sample factories' inventory of PP"
  },
  {
    "figure_id": "F061",
    "report_id": "R008",
    "label": "Figure 14",
    "context": "Figure 14: China TiO2 capacity utilisation ## Inventory Figure 15: Sample factories' inventory of PP Figure 16: Sample factories' inventory of PE Figure 17: Sample factories' inventory of PVC"
  },
  {
    "figure_id": "F062",
    "report_id": "R008",
    "label": "Figure 15",
    "context": "Figure 15: Sample factories' inventory of PP Figure 16: Sample factories' inventory of PE Figure 17: Sample factories' inventory of PVC Figure 18: Sample factories' inventory of TiO2"
  },
  {
    "figure_id": "F063",
    "report_id": "R008",
    "label": "Figure 16",
    "context": "Figure 16: Sample factories' inventory of PE Figure 17: Sample factories' inventory of PVC Figure 18: Sample factories' inventory of TiO2 Figure 19: Sample factories' inventory of polyester filament"
  },
  {
    "figure_id": "F064",
    "report_id": "R008",
    "label": "Figure 17",
    "context": "Figure 17: Sample factories' inventory of PVC Figure 18: Sample factories' inventory of TiO2 Figure 19: Sample factories' inventory of polyester filament Figure 20: Sample factories' inventory of silicone DMC"
  },
  {
    "figure_id": "F065",
    "report_id": "R008",
    "label": "Figure 18",
    "context": "Figure 18: Sample factories' inventory of TiO2 Figure 19: Sample factories' inventory of polyester filament Figure 20: Sample factories' inventory of silicone DMC ## Valuation Method and Risk Statement"
  },
  {
    "figure_id": "F066",
    "report_id": "R008",
    "label": "Figure 19",
    "context": "Figure 19: Sample factories' inventory of polyester filament Figure 20: Sample factories' inventory of silicone DMC ## Valuation Method and Risk Statement O&G sector: We believe risks include: 1) declines or fluctuations in cru"
  },
  {
    "figure_id": "F067",
    "report_id": "R009",
    "label": "Exhibit 4",
    "context": "Exhibit 4: KEI Industries Q1FY27E expectations Exhibit 5: Copper on an average has increased 1-5% MoM every month in Q1 Exhibit 6: Aluminium also increased in April and May MoM, but has corrected \\~1% in June YTD Exhibit 7: On"
  },
  {
    "figure_id": "F068",
    "report_id": "R009",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Copper on an average has increased 1-5% MoM every month in Q1 Exhibit 6: Aluminium also increased in April and May MoM, but has corrected \\~1% in June YTD Exhibit 7: On a YoY basis, we are seeing the largest quantum"
  },
  {
    "figure_id": "F069",
    "report_id": "R009",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Aluminium also increased in April and May MoM, but has corrected \\~1% in June YTD Exhibit 7: On a YoY basis, we are seeing the largest quantum of price increases in Q1 so far vs the last 16 quarters, which should suppo"
  },
  {
    "figure_id": "F070",
    "report_id": "R010",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Aggregate 2026E/2027E EBITDA consensus estimates for China OEMs have undergone four consecutive rounds of cuts, and momentum has been accelerating ## Inflection monitor - 2025/1Q26 Bottom line: Based on our three wat"
  },
  {
    "figure_id": "F071",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Aggregate 2026E/2027E EBITDA consensus estimates for China OEMs have undergone four consecutive rounds of cuts, and momentum has been accelerating ## Inflection monitor - 2025/1Q26 Bottom line: Based on our three wat"
  },
  {
    "figure_id": "F072",
    "report_id": "R010",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Industry EBITDA became more evenly distributed, with yoy declines at the top 2 profit generators in 4Q25"
  },
  {
    "figure_id": "F073",
    "report_id": "R010",
    "label": "Exhibit 9",
    "context": "Exhibit 5: Industry EBITDA became more evenly distributed, with yoy declines at the top 2 profit generators in 4Q25 Exhibit 6: Nio/Geely/Chery contributed the most to the 4Q25 yoy EBITDA increase"
  },
  {
    "figure_id": "F074",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Nio/Geely/Chery contributed the most to the 4Q25 yoy EBITDA increase Exhibit 7: Industry EBITDA became more skewed in terms of distribution in 1Q26, mainly because industry leaders have higher exposure overseas"
  },
  {
    "figure_id": "F075",
    "report_id": "R010",
    "label": "Exhibit 5",
    "context": "Exhibit 8: Nio/SAIC/Geely contributed the most to the 1Q26 yoy EBITDA increase EBITDA change (1Q26 vs. 1Q25, Rmb mn)"
  },
  {
    "figure_id": "F076",
    "report_id": "R010",
    "label": "Exhibit 6",
    "context": "Exhibit 9: OEM industry net cash declined to levels last seen in 2024"
  },
  {
    "figure_id": "F077",
    "report_id": "R010",
    "label": "Exhibit 7",
    "context": "Exhibit 9: OEM industry net cash declined to levels last seen in 2024 Exhibit 10: OEM industry net cash declined by Rmb65bn in 1Q26 vs. 1Q25 mainly driven by BYD's payable payback"
  },
  {
    "figure_id": "F078",
    "report_id": "R010",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Nio/SAIC/Geely contributed the most to the 1Q26 yoy EBITDA increase EBITDA change (1Q26 vs. 1Q25, Rmb mn) Exhibit 9: OEM industry net cash declined to levels last seen in 2024 Exhibit 10: OEM industry net cash declin"
  },
  {
    "figure_id": "F079",
    "report_id": "R010",
    "label": "Exhibit 9",
    "context": "Exhibit 9: OEM industry net cash declined to levels last seen in 2024 Exhibit 10: OEM industry net cash declined by Rmb65bn in 1Q26 vs. 1Q25 mainly driven by BYD's payable payback Exhibit 11: OEMs/suppliers margin & leverage an"
  },
  {
    "figure_id": "F080",
    "report_id": "R010",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Potential magnitude of price cuts implied by 1Q26 EBITDA break-even point ## For OEMs with negative EBITDA but in a net cash position, we try to answer the question: How many months will it take to eliminate the net ca"
  },
  {
    "figure_id": "F081",
    "report_id": "R010",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Potential magnitude of price cuts implied by 1Q26 EBITDA break-even point ## For OEMs with negative EBITDA but in a net cash position, we try to answer the question: How many months will it take to eliminate the net ca"
  },
  {
    "figure_id": "F082",
    "report_id": "R010",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Tipping point calculation for OEMs with negative EBITDA but in a net cash position 2024 EBITDA & net cash (Rmb mn) 2023 Net cash tipping point 2024 Net cash tipping point"
  },
  {
    "figure_id": "F083",
    "report_id": "R010",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Tipping point calculation for OEMs with negative EBITDA but in a net cash position 2024 EBITDA & net cash (Rmb mn) 2023 Net cash tipping point 2024 Net cash tipping point 2025 Net cash tipping point"
  },
  {
    "figure_id": "F084",
    "report_id": "R010",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Tipping point calculation for OEMs with negative EBITDA but in a net cash position 2024 EBITDA & net cash (Rmb mn) 2023 Net cash tipping point 2024 Net cash tipping point 2025 Net cash tipping point ■ # of mont"
  },
  {
    "figure_id": "F085",
    "report_id": "R010",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Estimate changes for PV volume in terms of wholesale/retail/export Exhibit 18: China Auto industry model"
  },
  {
    "figure_id": "F086",
    "report_id": "R010",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Estimate changes for PV volume in terms of wholesale/retail/export Exhibit 18: China Auto industry model"
  },
  {
    "figure_id": "F087",
    "report_id": "R010",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Estimate changes for PV volume in terms of wholesale/retail/export Exhibit 18: China Auto industry model ## Buy BYD, Leapmotor and XPeng on domestic recovery and overseas upside potential"
  },
  {
    "figure_id": "F088",
    "report_id": "R010",
    "label": "Exhibit 19",
    "context": "Exhibit 19: BYD quarterly volume breakdown Exhibit 20: BYD quarterly net profit & margin Overseas market to become a major growth driver: We expect the overseas market to become a key growth driver over the next decade for the c"
  },
  {
    "figure_id": "F089",
    "report_id": "R010",
    "label": "Exhibit 19",
    "context": "Exhibit 19: BYD quarterly volume breakdown Exhibit 20: BYD quarterly net profit & margin Overseas market to become a major growth driver: We expect the overseas market to become a key growth driver over the next decade for the c"
  },
  {
    "figure_id": "F090",
    "report_id": "R010",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We expect BYD's overseas sales volume to be around 1mn/3.3mn/3.5mn in 2025/2030E/2035E... Exhibit 22: ...with Asia Pacific/Europe/Other regions contributing about 1/3 of the volume each"
  },
  {
    "figure_id": "F091",
    "report_id": "R010",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We expect BYD's overseas sales volume to be around 1mn/3.3mn/3.5mn in 2025/2030E/2035E... Exhibit 22: ...with Asia Pacific/Europe/Other regions contributing about 1/3 of the volume each"
  },
  {
    "figure_id": "F092",
    "report_id": "R010",
    "label": "Exhibit 26",
    "context": "Exhibit 24: We expect Leapmotor to deliver one of the highest volume growth among covered peers... Exhibit 25: ...supported by a strong and steady new model pipeline"
  },
  {
    "figure_id": "F093",
    "report_id": "R010",
    "label": "Exhibit 25",
    "context": "Exhibit 28: We see $60\\%$ upside to mgmt's 2026 overseas sales target driven by strong retail-end demand"
  },
  {
    "figure_id": "F094",
    "report_id": "R010",
    "label": "Exhibit 26",
    "context": "Exhibit 29: Shares are under-valued on both P/S and P/E given its industry-leading growth rate"
  },
  {
    "figure_id": "F095",
    "report_id": "R010",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Partnership with Stellantis has enabled Leapmotor to quickly expand its overseas presence Exhibit 28: We see $60\\%$ upside to mgmt's 2026 overseas sales target driven by strong retail-end demand Exhibit 29: Shares ar"
  },
  {
    "figure_id": "F096",
    "report_id": "R010",
    "label": "Exhibit 34",
    "context": "Exhibit 31: We expect the new model cycle to drive acceleration... Exhibit 32: ... in volume as well as revenue growth for XPeng Exhibit 33: Product comparison for large 6-seater SUVs launched recently"
  },
  {
    "figure_id": "F097",
    "report_id": "R010",
    "label": "Exhibit 31",
    "context": "Exhibit 31: We expect the new model cycle to drive acceleration... Exhibit 32: ... in volume as well as revenue growth for XPeng Exhibit 33: Product comparison for large 6-seater SUVs launched recently"
  },
  {
    "figure_id": "F098",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 1: Sustainable AuM has stabilized YTD... Figure 2: Sustainable AuM market share Sustainable AuM market share by region (%) Figure 3: European funds account for the vast majority of sustainable assets AuM of Sustainable"
  },
  {
    "figure_id": "F099",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 4: Equity funds account for roughly two-thirds of sustainable funds AuM of Sustainable Funds, by asset class and region (%)"
  },
  {
    "figure_id": "F100",
    "report_id": "R011",
    "label": "Figure 2",
    "context": "Figure 2: Sustainable AuM market share Sustainable AuM market share by region (%) Figure 3: European funds account for the vast majority of sustainable assets AuM of Sustainable Funds, by domicile (%) Figure 4: Equity funds acco"
  },
  {
    "figure_id": "F101",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "Figure 5: Equity flows"
  },
  {
    "figure_id": "F102",
    "report_id": "R011",
    "label": "Figure 5",
    "context": "Figure 5: Equity flows Figure 6: YTD equity flows by region Figure 7: Fixed income flows"
  },
  {
    "figure_id": "F103",
    "report_id": "R011",
    "label": "Figure 7",
    "context": "Figure 5: Equity flows Figure 6: YTD equity flows by region Figure 7: Fixed income flows Figure 8: YTD fixed income flows by region"
  },
  {
    "figure_id": "F104",
    "report_id": "R011",
    "label": "Figure 6",
    "context": "Figure 6: YTD equity flows by region Figure 7: Fixed income flows Figure 8: YTD fixed income flows by region Relative performance up to April has been broadly in line."
  },
  {
    "figure_id": "F105",
    "report_id": "R011",
    "label": "Figure 7",
    "context": "Figure 7: Fixed income flows Figure 8: YTD fixed income flows by region Relative performance up to April has been broadly in line. In equities, European sustainable funds marginally outperformed European broad market funds (Fi"
  },
  {
    "figure_id": "F106",
    "report_id": "R011",
    "label": "Figure 9",
    "context": "Figure 9: Sustainable equity funds outperformed in Europe by 0.8% YTD... Annualized returns of sustainable and broad market European equity funds (%) Based on EUR returns. Figure 10: ...and underperformed by 0.6% in the US Annua"
  },
  {
    "figure_id": "F107",
    "report_id": "R011",
    "label": "Figure 9",
    "context": "Figure 11: European sustainable fixed income funds performed in line with the broad market... Annualized returns of sustainable and broad market European fixed income funds (%) Based on EUR returns."
  },
  {
    "figure_id": "F108",
    "report_id": "R011",
    "label": "Figure 10",
    "context": "Figure 12: ...whilst US Sustainable fixed income funds registered very marginal underperformance Annualized returns of sustainable and broad market US fixed income funds (%) Based on USD returns."
  },
  {
    "figure_id": "F109",
    "report_id": "R011",
    "label": "Figure 11",
    "context": "Figure 11: European sustainable fixed income funds performed in line with the broad market... Annualized returns of sustainable and broad market European fixed income funds (%) Based on EUR returns. Figure 12: ...whilst US Sustai"
  },
  {
    "figure_id": "F110",
    "report_id": "R011",
    "label": "Figure 13",
    "context": "Figure 13: SFDR equity returns Based on local currency returns. Figure 14: Quarterly flows SFDR equity Figure 15: SFDR fixed income returns"
  },
  {
    "figure_id": "F111",
    "report_id": "R011",
    "label": "Figure 15",
    "context": "Figure 13: SFDR equity returns Based on local currency returns. Figure 14: Quarterly flows SFDR equity Figure 15: SFDR fixed income returns Based on local currency returns."
  },
  {
    "figure_id": "F112",
    "report_id": "R011",
    "label": "Figure 14",
    "context": "Figure 14: Quarterly flows SFDR equity Figure 15: SFDR fixed income returns Based on local currency returns. Figure 16: Quarterly flows SFDR fixed income ## Looking to the future: tech could hurt"
  },
  {
    "figure_id": "F113",
    "report_id": "R011",
    "label": "Figure 15",
    "context": "Figure 15: SFDR fixed income returns Based on local currency returns. Figure 16: Quarterly flows SFDR fixed income ## Looking to the future: tech could hurt If we left IT out of the equation, the implications of our Strategists"
  },
  {
    "figure_id": "F114",
    "report_id": "R011",
    "label": "Figure 17",
    "context": "Figure 17: Sector exposure of sustainable funds Sector exposure of sustainable equity funds relative to the MSCI ACWI (%) ## ESGQ: An Inadvertent AI Hedge The first half of 2026 has been a difficult one to read for ESG investors."
  },
  {
    "figure_id": "F115",
    "report_id": "R011",
    "label": "Figure 18",
    "context": "Figure 18: Global ESGQ, EQ, SG and GQ YTD Excess Long Performance Figure 19: Global ESGQ, EQ, SG and GQ YTD L/S Performance The headwind and the hedge are the same position. ESGQ's IT underweight is the largest"
  },
  {
    "figure_id": "F116",
    "report_id": "R011",
    "label": "Figure 18",
    "context": "Figure 18: Global ESGQ, EQ, SG and GQ YTD Excess Long Performance Figure 19: Global ESGQ, EQ, SG and GQ YTD L/S Performance The headwind and the hedge are the same position. ESGQ's IT underweight is the largest"
  },
  {
    "figure_id": "F117",
    "report_id": "R011",
    "label": "Figure 20",
    "context": "Figure 20: Global ESGQ Long vs Market P/E Relative Figure 21: Global ESGQ Long vs Short P/E Relative Both relative P/E series sit near the upper end of their post-2009 ranges, above the long-run mean and pressing against the +1"
  },
  {
    "figure_id": "F118",
    "report_id": "R011",
    "label": "Figure 20",
    "context": "Figure 20: Global ESGQ Long vs Market P/E Relative Figure 21: Global ESGQ Long vs Short P/E Relative Both relative P/E series sit near the upper end of their post-2009 ranges, above the long-run mean and pressing against the +1"
  },
  {
    "figure_id": "F119",
    "report_id": "R011",
    "label": "Figure 22",
    "context": "Figure 22: Global ESGQ Long vs Market Sector Allocation Figure 23: Global ESGQ L/S Sector Allocation ## Three times the historical IT"
  },
  {
    "figure_id": "F120",
    "report_id": "R011",
    "label": "Figure 22",
    "context": "Figure 22: Global ESGQ Long vs Market Sector Allocation Figure 23: Global ESGQ L/S Sector Allocation ## Three times the historical IT underweight. That single position is doing more to drive long-only tracking error than any ot"
  },
  {
    "figure_id": "F121",
    "report_id": "R011",
    "label": "Figure 24",
    "context": "Figure 24: ESGQ Long Factor Exposures Figure 25: ESGQ L/S Factor Exposures Quality is the dominant active exposure on both views, at 0.20 on the long leg against a 0.14 historical average and 0.61 on the long-short against 0.36"
  },
  {
    "figure_id": "F122",
    "report_id": "R011",
    "label": "Figure 24",
    "context": "Figure 24: ESGQ Long Factor Exposures Figure 25: ESGQ L/S Factor Exposures Quality is the dominant active exposure on both views, at 0.20 on the long leg against a 0.14 historical average and 0.61 on the long-short against 0.36"
  },
  {
    "figure_id": "F123",
    "report_id": "R011",
    "label": "Figure 26",
    "context": "Figure 26: ESGQ L/S Macro Sensitivities - Full Sample Full Sample - from June 2008 onwards Figure 27: ESGQ L/S Macro Sensitivities - 60M Last 60M Window Same factor, different world. Three of six macro relationships have flippe"
  },
  {
    "figure_id": "F124",
    "report_id": "R011",
    "label": "Figure 26",
    "context": "Figure 26: ESGQ L/S Macro Sensitivities - Full Sample Full Sample - from June 2008 onwards Figure 27: ESGQ L/S Macro Sensitivities - 60M Last 60M Window Same factor, different world. Three of six macro relationships have flippe"
  },
  {
    "figure_id": "F125",
    "report_id": "R011",
    "label": "Figure 28",
    "context": "Figure 28: Taiwan's listed ESG ETF market has demonstrated steady growth in recent years ESG ETF AUM (NTD bn) Figure 29: Taiwan is in the midst of reconsidering its nuclear future Taiwan operable nuclear power capacity: Reference"
  },
  {
    "figure_id": "F126",
    "report_id": "R011",
    "label": "Figure 28",
    "context": "Figure 28: Taiwan's listed ESG ETF market has demonstrated steady growth in recent years ESG ETF AUM (NTD bn) Figure 29: Taiwan is in the midst of reconsidering its nuclear future Taiwan operable nuclear power capacity: Reference"
  },
  {
    "figure_id": "F127",
    "report_id": "R011",
    "label": "Figure 30",
    "context": "Figure 30: Brazilian regulators plan 5GW of BESS capacity in the next years # Asia: positioning for El Niño (II) and renewables ideas El Niño - Expected heat waves this summer are likely to drive up power demand in Asia Despite t"
  },
  {
    "figure_id": "F128",
    "report_id": "R011",
    "label": "Figure 31",
    "context": "Figure 32: El Niño typically brings dry conditions, droughts and heatwaves to SE and S Asia, while escalating rainfall in China and Japan Beating the heat will mean elevated power demand. In China, for example, a 1°C rise in temp"
  },
  {
    "figure_id": "F129",
    "report_id": "R011",
    "label": "Figure 31",
    "context": "Figure 33: Electricity consumption growth in ASEAN is stronger in El Niño years. Electricity consumption growth (kWh, % yoy)"
  },
  {
    "figure_id": "F130",
    "report_id": "R011",
    "label": "Figure 32",
    "context": "Figure 33: Electricity consumption growth in ASEAN is stronger in El Niño years. Electricity consumption growth (kWh, % yoy) Warmer-than-normal temperatures this year are already testing system peaks. Power demand in India reache"
  },
  {
    "figure_id": "F131",
    "report_id": "R011",
    "label": "Figure 34",
    "context": "Figure 34: Performance of the APAC Power Utilities vs. respective index from early May to mid-July ## Diesel shock, solar lock Energy supply disruptions from the Middle East conflict are lifting demand for DG solar and ESS, in ou"
  },
  {
    "figure_id": "F132",
    "report_id": "R011",
    "label": "Figure 35",
    "context": "Figure 35: Policy tailwinds and improving economics should support a growing share of rooftop solar PV in ASEAN, where island use cases can be especially strong Within our coverage space, we prefer Deye (605117 CH, OW). Deye is a"
  },
  {
    "figure_id": "F133",
    "report_id": "R011",
    "label": "Figure 36",
    "context": "Figure 36: European Integrated Utility Renewable Exposures ## Sustainable debt ## Sovereign GSS bond club swells to 65 members Cumulative sovereign GSS issuance reached USD 843.48 bn at the end of May 2026. Green bonds account fo"
  },
  {
    "figure_id": "F134",
    "report_id": "R011",
    "label": "Figure 37",
    "context": "Figure 37: Historical Sovereign GSS Issuance (USD bn) Figure 38: Market Capitalization of the JPM GESSIE (USD bn)"
  },
  {
    "figure_id": "F135",
    "report_id": "R011",
    "label": "Figure 38",
    "context": "Figure 37: Historical Sovereign GSS Issuance (USD bn) Figure 38: Market Capitalization of the JPM GESSIE (USD bn)"
  },
  {
    "figure_id": "F136",
    "report_id": "R011",
    "label": "Figure 41",
    "context": "Figure 39: EUR IG GSS+ Issuance Figure 40: GBP IG GSS+ Issuance Figure 41: EUR IG NIP Differential - GSS vs. non-GSS"
  },
  {
    "figure_id": "F137",
    "report_id": "R011",
    "label": "Figure 39",
    "context": "Figure 39: EUR IG GSS+ Issuance Figure 40: GBP IG GSS+ Issuance Figure 41: EUR IG NIP Differential - GSS vs. non-GSS Figure 42: Primary Book Coverage Ratios: GSS vs. non-GSS"
  },
  {
    "figure_id": "F138",
    "report_id": "R011",
    "label": "Figure 40",
    "context": "Figure 40: GBP IG GSS+ Issuance Figure 41: EUR IG NIP Differential - GSS vs. non-GSS Figure 42: Primary Book Coverage Ratios: GSS vs. non-GSS Figure 43: EUR HY GSS+ Issuance"
  },
  {
    "figure_id": "F139",
    "report_id": "R011",
    "label": "Figure 41",
    "context": "Figure 41: EUR IG NIP Differential - GSS vs. non-GSS Figure 42: Primary Book Coverage Ratios: GSS vs. non-GSS Figure 43: EUR HY GSS+ Issuance ## Global Index"
  },
  {
    "figure_id": "F140",
    "report_id": "R011",
    "label": "Figure 42",
    "context": "Figure 42: Primary Book Coverage Ratios: GSS vs. non-GSS Figure 43: EUR HY GSS+ Issuance ## Global Index The JSTAR Index Governance - introduced in 2023 - has paved the way for key enhancements to the flagship JSTAR index suite"
  },
  {
    "figure_id": "F141",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 9: While each industry upcycle has differed in duration, unit vs. ASP contribution, and fundamental drivers, we observe that in most cases WFE intensity tends to rise during the period WFE performance during every semi indu"
  },
  {
    "figure_id": "F142",
    "report_id": "R012",
    "label": "Exhibit 10",
    "context": "Exhibit 11: WFE intensity and WFE per wafer trends tend to be less consistent across foundry/logic cycles but typically see strong expansion during tech transitions such as the move to EUV in CY18-22"
  },
  {
    "figure_id": "F143",
    "report_id": "R012",
    "label": "Exhibit 12",
    "context": "Exhibit 13: DRAM intensity and WFE per wafer generally increases during DRAM sales cycles even if growth is mainly ASP-led with the exception being CY23-25"
  },
  {
    "figure_id": "F144",
    "report_id": "R012",
    "label": "Exhibit 14",
    "context": "Exhibit 15: NAND WFE intensity per wafer has always increased in the past three cycles as bit growth is driven by migrations and conversions rather than greenfield capacity adds"
  },
  {
    "figure_id": "F145",
    "report_id": "R012",
    "label": "Exhibit 16",
    "context": "Exhibit 16: While trends have been choppy, NAND WFE per wafer rises during periods of heightened migration/conversion activity NAND WFE per 12\" wafer start per month (lhs) and NAND WFE intensity (rhs) BofA GLOBAL RESEARCH Exhibit"
  },
  {
    "figure_id": "F146",
    "report_id": "R012",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Industry HBM shipment could reach 16.190 CY30E, growing at +40% CAGR between CY25-30E HBM Unit Shipment Forecast by Vendor (GB bn) 3 Exhibit 2 By Industry HBM sales could reach \\$168bn by CY30E, growing at +37% CAGR betw"
  },
  {
    "figure_id": "F147",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 24: DRAM Industry Capex Estimate (\\$bn) We expect overall DRAM capex to meaningfully increase again in CY26-28 BofA GLOBAL RESEARCH Exhibit 25: NAND Industry Capex Estimate (\\$bn) We expect overall NAND capex to meaningful"
  },
  {
    "figure_id": "F148",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 24: DRAM Industry Capex Estimate (\\$bn) We expect overall DRAM capex to meaningfully increase again in CY26-28 BofA GLOBAL RESEARCH Exhibit 25: NAND Industry Capex Estimate (\\$bn) We expect overall NAND capex to meaningful"
  },
  {
    "figure_id": "F149",
    "report_id": "R012",
    "label": "Exhibit 26",
    "context": "## DRAM Supply/Demand Sustainability Ratio DRAM Industry Supply/Demand and Sufficiency Ratio % BofA GLOBAL RESEARCH ## NAND Supply/Demand Sustainability Ratio"
  },
  {
    "figure_id": "F150",
    "report_id": "R012",
    "label": "Exhibit 27",
    "context": "Exhibit 28: Strong DRAM spot/contract pricing trends throughout 2026"
  },
  {
    "figure_id": "F151",
    "report_id": "R012",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Strong DRAM spot/contract pricing trends throughout 2026 DRAM Spot/Contract ASP Trends BofA GLOBAL RESEARCH Exhibit 29: Strong NAND spot/contract pricing trends throughout 2026 NAND Spot/Contract ASP Trends BofA GLOB"
  },
  {
    "figure_id": "F152",
    "report_id": "R012",
    "label": "Exhibit 28",
    "context": "Exhibit 30: We raise MU FY26/27/28E sales by +11%/+27%/+31%, EPS by +21%/+35%/+43% to \\$97.78/\\$139.45/\\$139.29"
  },
  {
    "figure_id": "F153",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend By brand dealer discount is based on best-selling models. Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F154",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend By brand dealer discount is based on best-selling models. Exhibit 3: ICE dealer discount trend By brand dealer discount is based on best-selling models."
  },
  {
    "figure_id": "F155",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend By brand dealer discount is based on best-selling models. Exhibit 3: ICE dealer discount trend By brand dealer discount is based on best-selling models."
  },
  {
    "figure_id": "F156",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend By brand dealer discount is based on best-selling models. ICE dealer discount - domestic brand ## Upstream battery pricing dynamics"
  },
  {
    "figure_id": "F157",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend By brand dealer discount is based on best-selling models. ICE dealer discount - domestic brand ## Upstream battery pricing dynamics"
  },
  {
    "figure_id": "F158",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend By brand dealer discount is based on best-selling models. ICE dealer discount - domestic brand ## Upstream battery pricing dynamics Exhibit 4: Battery and battery raw materials prices"
  },
  {
    "figure_id": "F159",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 2: Iceberg Index - tier-1 cities' secondary listing volume (冰山指数二手挂牌量) No. of secondary listings ('000 units) - Tier 1 cities"
  },
  {
    "figure_id": "F160",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 2: Iceberg Index - tier-1 cities' secondary listing volume (冰山指数二手挂牌量) No. of secondary listings ('000 units) - Tier 1 cities ## Official sales registrations (lag of a few weeks) Figure 3: 60-city weekly primary sales reg"
  },
  {
    "figure_id": "F161",
    "report_id": "R014",
    "label": "Figure 2",
    "context": "Figure 4: 60-city weekly primary sales registrations (一手网签) Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public h"
  },
  {
    "figure_id": "F162",
    "report_id": "R014",
    "label": "Figure 3",
    "context": "Figure 4: 60-city weekly primary sales registrations (一手网签) Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public h"
  },
  {
    "figure_id": "F163",
    "report_id": "R014",
    "label": "Figure 5",
    "context": "Figure 5: 8-city secondary sales registrations (二手网签) Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holiday"
  },
  {
    "figure_id": "F164",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: China property – year-to-date share price performance by stock Figure 7: MSCI China Real Estate Index vs. HSI, year-to-date Note: normalized to 100 as of 5 January 2026"
  },
  {
    "figure_id": "F165",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: China property – year-to-date share price performance by stock Figure 7: MSCI China Real Estate Index vs. HSI, year-to-date Note: normalized to 100 as of 5 January 2026"
  },
  {
    "figure_id": "F166",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China humanoid development has seen rapid developments in 2024-26; we are in the early commercialization stage. ## China Humanoid Market Forecast Stronger push toward commercialization. As highlighted in our 2026 outlo"
  },
  {
    "figure_id": "F167",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We raise our China 2026 humanoid forecast to 50k unit and expect full-size humanoids to see more adoption with improving abilities. China Humanoid Sales ('k unit) Exhibit 4: We expect the industry's blended ASP to decl"
  },
  {
    "figure_id": "F168",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Our long-term global humanoid forecast is largely unchanged, expecting 1bn units of stock and US\\$7.5tr market size by 2050e."
  },
  {
    "figure_id": "F169",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: ...Implying a market size of US\\$2bn/\\$15bn in 2026e/2030e. China Humanoid Market Size (US\\$'bn) Exhibit 6: Our long-term global humanoid forecast is largely unchanged, expecting 1bn units of stock and US\\$7.5tr market"
  },
  {
    "figure_id": "F170",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: ...Implying a market size of US\\$2bn/\\$15bn in 2026e/2030e. China Humanoid Market Size (US\\$'bn) Exhibit 6: Our long-term global humanoid forecast is largely unchanged, expecting 1bn units of stock and US\\$7.5tr market"
  },
  {
    "figure_id": "F171",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China's Humanoid Value Chain Performance, Equal-weighted China Humanoid Value Chain - Equal-weighted Performance Exhibit 8: China Humanoid Value Chain list: 45 stocks in total, including three in brains, 32 in body com"
  },
  {
    "figure_id": "F172",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary weekly unit sales and four-week moving average – Total 50 cities Stephen Cheung, CFA"
  },
  {
    "figure_id": "F173",
    "report_id": "R017",
    "label": "Figure 1",
    "context": "Figure 1: Broker sector stock performance Figure 2: A-share equity-linked ADT rose 95% YoY to Rmb3.2 trn in 5M26 Figure 3: Margin financing and securities lending balances rose to Rmb3.0 trn, up 62%/14% YoY/QoQ Figure 4: YTD A"
  },
  {
    "figure_id": "F174",
    "report_id": "R017",
    "label": "Figure 2",
    "context": "Figure 2: A-share equity-linked ADT rose 95% YoY to Rmb3.2 trn in 5M26 Figure 3: Margin financing and securities lending balances rose to Rmb3.0 trn, up 62%/14% YoY/QoQ Figure 4: YTD A share IPO underwriting value +62% YoY F"
  },
  {
    "figure_id": "F175",
    "report_id": "R017",
    "label": "Figure 3",
    "context": "Figure 3: Margin financing and securities lending balances rose to Rmb3.0 trn, up 62%/14% YoY/QoQ Figure 4: YTD A share IPO underwriting value +62% YoY Figure 5: YTD A share refinancing underwriting value down 45% YoY ## Val"
  },
  {
    "figure_id": "F176",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4: YTD A share IPO underwriting value +62% YoY Figure 5: YTD A share refinancing underwriting value down 45% YoY ## Valuation Method and Risk Statement We believe main risks to China's securities sector include: 1) a ma"
  },
  {
    "figure_id": "F177",
    "report_id": "R018",
    "label": "Figure 2",
    "context": "Figure 3: China's electronic-grade hydrofluoric acid consumption and revenue"
  },
  {
    "figure_id": "F178",
    "report_id": "R018",
    "label": "Figure 3",
    "context": "Figure 4: UPSSS-grade EG-HF prices are higher than those of other grades"
  },
  {
    "figure_id": "F179",
    "report_id": "R018",
    "label": "Figure 4",
    "context": "Figure 4: UPSSS-grade EG-HF prices are higher than those of other grades Figure 5: China's anhydrous hydrogen fluoride price on the rise overall YTD"
  },
  {
    "figure_id": "F180",
    "report_id": "R018",
    "label": "Figure 4",
    "context": "Figure 4: UPSSS-grade EG-HF prices are higher than those of other grades Figure 5: China's anhydrous hydrogen fluoride price on the rise overall YTD Figure 6: Profile of major domestic EG-HF listcos"
  },
  {
    "figure_id": "F181",
    "report_id": "R018",
    "label": "Figure 7",
    "context": "Figure 7: PFAS substitutes and Chinese manufacturers (by chemical) Figure 8: 3M's PFAS net sales and EBITDA (US\\$bn) Figure 9: Semis and auto contributed 35-40% of 3M's PFAS revenue Chinese fluorinated fluid producers are embr"
  },
  {
    "figure_id": "F182",
    "report_id": "R018",
    "label": "Figure 8",
    "context": "Figure 10: Fluorinated fluid capacity layout of main listcos"
  },
  {
    "figure_id": "F183",
    "report_id": "R018",
    "label": "Figure 11",
    "context": "Figure 12: Main fluorinated ESGs and major producers"
  },
  {
    "figure_id": "F184",
    "report_id": "R018",
    "label": "Figure 13",
    "context": "Figure 13: WF6 export price trend ## PCB copper clad laminate (CCL): PTFE AI servers have significantly raised their requirements for high-frequency, high-speed materials. As such, the industry considers PTFE (polytetrafluoroethy"
  },
  {
    "figure_id": "F185",
    "report_id": "R018",
    "label": "Figure 16",
    "context": "Figure 16: SOTP valuation contribution by segment of Dongyue ## Capchem (Buy; price target raised to Rmb122.0) As a leading producer of fluorinated fine chemicals in China, Capchem started with key upstream intermediates includin"
  },
  {
    "figure_id": "F186",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Our proprietary import-implied domestic demand proxy suggests weak domestic demand growth in Q2"
  },
  {
    "figure_id": "F187",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Our proprietary import-implied domestic demand proxy suggests weak domestic demand growth in Q2 Exhibit 4: Our MAP surprise index (21-day moving average) shows recent macro data have come in below market expectations"
  },
  {
    "figure_id": "F188",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "Exhibit 5: Our manufacturing growth proxy and construction growth proxy both ticked up in May"
  },
  {
    "figure_id": "F189",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Our manufacturing growth proxy and construction growth proxy both ticked up in May Exhibit 6: Our preliminary investment tracker (on a real value-added basis) points to slightly weaker growth in Q2"
  },
  {
    "figure_id": "F190",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "Exhibit 7: Our China inventory tracker suggests inventory levels may stay roughly flat in Q2 2026"
  },
  {
    "figure_id": "F191",
    "report_id": "R019",
    "label": "Exhibit 5",
    "context": "Exhibit 8: The boost from inventory changes to sequential GDP growth is likely to decline in Q2 2026"
  },
  {
    "figure_id": "F192",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "Exhibit 9: Our China outside-in export tracker outperformed the official export growth data in April"
  },
  {
    "figure_id": "F193",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "Exhibit 10: Our China outside-in import tracker underperformed the official import growth data in April"
  },
  {
    "figure_id": "F194",
    "report_id": "R019",
    "label": "Exhibit 8",
    "context": "Exhibit 11: China Financial Conditions Index (FCI; including credit quantities) tightened slightly in May"
  },
  {
    "figure_id": "F195",
    "report_id": "R019",
    "label": "Exhibit 9",
    "context": "Exhibit 11: China Financial Conditions Index (FCI; including credit quantities) tightened slightly in May Exhibit 12: May's slight tightening in FCI was driven by FX appreciation against the trade-weighted basket and weaker equity"
  },
  {
    "figure_id": "F196",
    "report_id": "R019",
    "label": "Exhibit 10",
    "context": "Exhibit 13: We estimate credit impulse may stay negative in H2 due to weak credit growth"
  },
  {
    "figure_id": "F197",
    "report_id": "R019",
    "label": "Exhibit 11",
    "context": "Exhibit 13: We estimate credit impulse may stay negative in H2 due to weak credit growth The impulses assume that credit stays flat through the remainder of this year. Exhibit 14: Our preferred gauge suggests increased FX inflows"
  },
  {
    "figure_id": "F198",
    "report_id": "R019",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Our preferred gauge suggests increased FX inflows in May Exhibit 15: Our China domestic macro policy proxy tightened slightly in May"
  },
  {
    "figure_id": "F199",
    "report_id": "R019",
    "label": "Exhibit 13",
    "context": "Exhibit 15: Our China domestic macro policy proxy tightened slightly in May Exhibit 16: May's tightening in GS China macro policy proxy was driven by tighter fiscal policy and slower credit growth"
  },
  {
    "figure_id": "F200",
    "report_id": "R019",
    "label": "Exhibit 14",
    "context": "Exhibit 17: Our augmented fiscal deficit (AFD) metric narrowed further in May"
  },
  {
    "figure_id": "F201",
    "report_id": "R019",
    "label": "Exhibit 15",
    "context": "Exhibit 18: China's fiscal \"spend-through\" ratio rose slightly in May"
  },
  {
    "figure_id": "F202",
    "report_id": "R019",
    "label": "Exhibit 16",
    "context": "Exhibit 19: Government bond net issuance is set to accelerate in the coming months"
  },
  {
    "figure_id": "F203",
    "report_id": "R019",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Government bond net issuance is set to accelerate in the coming months Local government refinancing bond issuance for debt resolution is not included."
  },
  {
    "figure_id": "F204",
    "report_id": "R019",
    "label": "Exhibit 18",
    "context": "Exhibit 19: Government bond net issuance is set to accelerate in the coming months Local government refinancing bond issuance for debt resolution is not included. Exhibit 20: Our city-level property relative tightness index sugges"
  },
  {
    "figure_id": "F205",
    "report_id": "R019",
    "label": "Exhibit 19",
    "context": "Exhibit 2: China Current Activity Indicator (Bloomberg ticker: GSCNCAI) is the “first principal component” of several real activity indicators including industrial production, electricity consumption, PMIs, etc., expressed in GDP-e"
  },
  {
    "figure_id": "F206",
    "report_id": "R026",
    "label": "Figure 1",
    "context": "Brian Cho Figure 1. Golden Week Domestic Tourist Number & Revenue as % of 2019 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Golden Week Domestic Tourist Numbers © 2026 Citi Inc. No redistribution without Citi's written permis"
  },
  {
    "figure_id": "F207",
    "report_id": "R026",
    "label": "Figure 1",
    "context": "Figure 1. Golden Week Domestic Tourist Number & Revenue as % of 2019 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Golden Week Domestic Tourist Numbers © 2026 Citi Inc. No redistribution without Citi's written permission. Note"
  },
  {
    "figure_id": "F208",
    "report_id": "R026",
    "label": "Figure 2",
    "context": "Figure 2. Golden Week Domestic Tourist Numbers © 2026 Citi Inc. No redistribution without Citi's written permission. Note: 2026 CNY & 2025 National Day Holiday momentum calculated on avg daily basis Figure 3. Golden Week Domestic Tourism Revenue © 2026 Citi In"
  },
  {
    "figure_id": "F209",
    "report_id": "R026",
    "label": "Figure 3",
    "context": "Figure 3. Golden Week Domestic Tourism Revenue © 2026 Citi Inc. No redistribution without Citi's written permission. Note: 2026 CNY & 2025 National Day Holiday momentum calculated on avg daily basis Figure 4. Golden Week Domestic Tourist Per-Capita Spending © "
  },
  {
    "figure_id": "F210",
    "report_id": "R026",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Hainan Duty-Free Golden Week Performance Figure 7. China Inbound and Outbound Traffic as % of 2019 © 2026 Citi Inc. No redistribution without Citi's written permission. # Atour Lif"
  },
  {
    "figure_id": "F211",
    "report_id": "R028",
    "label": "Figure 1",
    "context": "Figure 1: Hong Kong secondary home price index (and major events) \\- Transaction volume: Remained strong year-to-date; the latest 12-month rolling Y/Y growth is tracking 40%. Figure 2: HK monthly private residential transactions"
  },
  {
    "figure_id": "F212",
    "report_id": "R028",
    "label": "Figure 1",
    "context": "Figure 1: Hong Kong secondary home price index (and major events) \\- Transaction volume: Remained strong year-to-date; the latest 12-month rolling Y/Y growth is tracking 40%. Figure 2: HK monthly private residential transactions"
  },
  {
    "figure_id": "F213",
    "report_id": "R028",
    "label": "Figure 3",
    "context": "Figure 3: Weekly secondary transactions in 35 major estates Figure 4: Midland weekend appointment volume (15 housing estates)"
  },
  {
    "figure_id": "F214",
    "report_id": "R028",
    "label": "Figure 3",
    "context": "Figure 5: Correlation with HK home prices Y/Y"
  },
  {
    "figure_id": "F215",
    "report_id": "R028",
    "label": "Figure 5",
    "context": "Figure 5: Correlation with HK home prices Y/Y ## Stock market \\- Hang Seng Index has shown a decent correlation to HK home prices. Figure 6: HK Secondary Home Price Index vs. Hang Seng Index (Y/Y change)"
  },
  {
    "figure_id": "F216",
    "report_id": "R028",
    "label": "Figure 6",
    "context": "Figure 6: HK Secondary Home Price Index vs. Hang Seng Index (Y/Y change) Figure 7: HK Secondary Home Price Index vs. Hang Seng Index (absolute)"
  },
  {
    "figure_id": "F217",
    "report_id": "R028",
    "label": "Figure 6",
    "context": "Figure 6: HK Secondary Home Price Index vs. Hang Seng Index (Y/Y change) Figure 7: HK Secondary Home Price Index vs. Hang Seng Index (absolute) ## Inventory Figure 8: Hong Kong unsold primary private residential properties"
  },
  {
    "figure_id": "F218",
    "report_id": "R028",
    "label": "Figure 8",
    "context": "Figure 8: Hong Kong unsold primary private residential properties \\- In the secondary market, the implied inventory is 7, based on Centraline's secondary for-sale listings. Figure 9: Centraline – No. of secondary listings (for s"
  },
  {
    "figure_id": "F219",
    "report_id": "R028",
    "label": "Figure 8",
    "context": "Figure 10: Secondary home price Y/Y vs inventory month ## Mortgage rates"
  },
  {
    "figure_id": "F220",
    "report_id": "R028",
    "label": "Figure 9",
    "context": "Figure 11: HK rental yield over mortgage rate vs. secondary home price"
  },
  {
    "figure_id": "F221",
    "report_id": "R028",
    "label": "Figure 11",
    "context": "Figure 11: HK rental yield over mortgage rate vs. secondary home price # Mainland Chinese buyers in HK residential market \\- The % of non-local buyers can be gauged by the % of homebuyers who do not hold a HKID. However, the late"
  },
  {
    "figure_id": "F222",
    "report_id": "R028",
    "label": "Figure 12",
    "context": "Figure 13: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by value) Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not dis"
  },
  {
    "figure_id": "F223",
    "report_id": "R028",
    "label": "Figure 12",
    "context": "Figure 13: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by value) Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not dis"
  },
  {
    "figure_id": "F224",
    "report_id": "R028",
    "label": "Figure 14",
    "context": "Figure 14: Earnings impact of every 100bps increase in HIBOR (considering % of HKD floating debt) Note: Figure 15: Increase in financing cost for every 100bps increase in HIBOR (considering % of HKD floating debt) Increase in fin"
  },
  {
    "figure_id": "F225",
    "report_id": "R028",
    "label": "Figure 14",
    "context": "Figure 16: Earnings impact of every 100bps increase in overall effective borrowing cost (without considering floating debt ratio)"
  },
  {
    "figure_id": "F226",
    "report_id": "R028",
    "label": "Figure 16",
    "context": "Figure 17: Increase in financing cost for every 100bps increase in overall effective borrowing cost (without considering floating debt ratio) % increase in cash interest expenses"
  },
  {
    "figure_id": "F227",
    "report_id": "R028",
    "label": "Figure 17",
    "context": "Figure 17: Increase in financing cost for every 100bps increase in overall effective borrowing cost (without considering floating debt ratio) % increase in cash interest expenses Note: The above does not consider the accounting i"
  },
  {
    "figure_id": "F228",
    "report_id": "R028",
    "label": "Figure 18",
    "context": "Figure 18: Hong Kong population Figure 19: Centraline Rental Index (CRI)"
  },
  {
    "figure_id": "F229",
    "report_id": "R028",
    "label": "Figure 18",
    "context": "Figure 18: Hong Kong population Figure 19: Centraline Rental Index (CRI) ## Share price performance Figure 20: HK Property: Year-to-date share price performance"
  },
  {
    "figure_id": "F230",
    "report_id": "R028",
    "label": "Figure 19",
    "context": "Figure 19: Centraline Rental Index (CRI) ## Share price performance Figure 20: HK Property: Year-to-date share price performance Figure 21: HK Property & Conglomerates - 2026 year-to-date share price performance by company ##"
  },
  {
    "figure_id": "F231",
    "report_id": "R028",
    "label": "Figure 20",
    "context": "Figure 20: HK Property: Year-to-date share price performance Figure 21: HK Property & Conglomerates - 2026 year-to-date share price performance by company ## Valuation Figure 22: Sector NAV discount trend"
  },
  {
    "figure_id": "F232",
    "report_id": "R028",
    "label": "Figure 21",
    "context": "Figure 21: HK Property & Conglomerates - 2026 year-to-date share price performance by company ## Valuation Figure 22: Sector NAV discount trend Figure 23: NAV discount by company Figure 24: 12m forward P/B"
  },
  {
    "figure_id": "F233",
    "report_id": "R028",
    "label": "Figure 22",
    "context": "Figure 22: Sector NAV discount trend Figure 23: NAV discount by company Figure 24: 12m forward P/B Figure 25: 12m forward P/B by company"
  },
  {
    "figure_id": "F234",
    "report_id": "R028",
    "label": "Figure 23",
    "context": "Figure 23: NAV discount by company Figure 24: 12m forward P/B Figure 25: 12m forward P/B by company Figure 26: 12m forward P/E"
  },
  {
    "figure_id": "F235",
    "report_id": "R028",
    "label": "Figure 23",
    "context": "Figure 23: NAV discount by company Figure 24: 12m forward P/B Figure 25: 12m forward P/B by company Figure 26: 12m forward P/E Figure 27: 12m forward P/E by company"
  },
  {
    "figure_id": "F236",
    "report_id": "R028",
    "label": "Figure 24",
    "context": "Figure 24: 12m forward P/B Figure 25: 12m forward P/B by company Figure 26: 12m forward P/E Figure 27: 12m forward P/E by company Figure 28: 12m forward dividend yield"
  },
  {
    "figure_id": "F237",
    "report_id": "R028",
    "label": "Figure 26",
    "context": "Figure 26: 12m forward P/E Figure 27: 12m forward P/E by company Figure 28: 12m forward dividend yield Figure 29: 12m forward dividend yield by company"
  },
  {
    "figure_id": "F238",
    "report_id": "R028",
    "label": "Figure 27",
    "context": "Figure 27: 12m forward P/E by company Figure 28: 12m forward dividend yield Figure 29: 12m forward dividend yield by company Figure 30: 12m forward dividend yield spread"
  },
  {
    "figure_id": "F239",
    "report_id": "R028",
    "label": "Figure 28",
    "context": "Figure 28: 12m forward dividend yield Figure 29: 12m forward dividend yield by company Figure 30: 12m forward dividend yield spread"
  },
  {
    "figure_id": "F240",
    "report_id": "R028",
    "label": "Figure 29",
    "context": "Figure 29: 12m forward dividend yield by company Figure 30: 12m forward dividend yield spread"
  },
  {
    "figure_id": "F241",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 1 - Weekly token consumption over the past 12 months as of 22 Jun (tn) Exhibit 2 - Silicon Data LLM Token Expenditure Index Exhibit 3 - Blended prices for China models vs US models (1Q26)"
  },
  {
    "figure_id": "F242",
    "report_id": "R029",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - Weekly token consumption over the past 12 months as of 22 Jun (tn) Exhibit 2 - Silicon Data LLM Token Expenditure Index Exhibit 3 - Blended prices for China models vs US models (1Q26) Exhibit 4 - Top 10 ranking in"
  },
  {
    "figure_id": "F243",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 2 - Silicon Data LLM Token Expenditure Index Exhibit 3 - Blended prices for China models vs US models (1Q26) Exhibit 4 - Top 10 ranking in terms of token consumption by model the latest week"
  },
  {
    "figure_id": "F244",
    "report_id": "R029",
    "label": "Exhibit 5",
    "context": "Exhibit 5 - Weekly token consumption over the past 12 months as of 22 Jun (tn) According to OpenRouter (between 15 and 21 Jun), China models token consumption increased by 2.12% compared to prior week at 18.8tn. This compares to U"
  },
  {
    "figure_id": "F245",
    "report_id": "R029",
    "label": "Exhibit 6",
    "context": "Exhibit 6 - Market share: weekly token consumption by company as of 22 Jun Exhibit 7 - Weekly token consumption since Jan-26 (bn)"
  },
  {
    "figure_id": "F246",
    "report_id": "R029",
    "label": "Exhibit 6",
    "context": "Exhibit 6 - Market share: weekly token consumption by company as of 22 Jun Exhibit 7 - Weekly token consumption since Jan-26 (bn) Exhibit 8 - Top 10 ranking in terms of token consumption by model the latest week"
  },
  {
    "figure_id": "F247",
    "report_id": "R029",
    "label": "Exhibit 10",
    "context": "Exhibit 10 - Cache hit/Input/Output API price for leading models as of 22 Jun Exhibit 11 - Quarterly Input / Output prices for China models In terms of Input/Output API price, China models are just a fraction vs US models. Exhibi"
  },
  {
    "figure_id": "F248",
    "report_id": "R029",
    "label": "Exhibit 10",
    "context": "Exhibit 10 - Cache hit/Input/Output API price for leading models as of 22 Jun Exhibit 11 - Quarterly Input / Output prices for China models In terms of Input/Output API price, China models are just a fraction vs US models. Exhibi"
  },
  {
    "figure_id": "F249",
    "report_id": "R029",
    "label": "Exhibit 11",
    "context": "Exhibit 13 - Intelligence index for top 20 models as of 22 Jun Exhibit 14 - Frontier Language Model Intelligence over time as of 22 Jun"
  },
  {
    "figure_id": "F250",
    "report_id": "R029",
    "label": "Exhibit 12",
    "context": "Exhibit 12 - Quarterly Input / Output prices for US models ■ Proprietary ■ Open Weights ■ Open Weights (Commercial Use Restricted) Exhibit 13 - Intelligence index for top 20 models as of 22 Jun Exhibit 14 - Frontier Language Mode"
  },
  {
    "figure_id": "F251",
    "report_id": "R029",
    "label": "Exhibit 13",
    "context": "Exhibit 15 - Agentic index for top 20 models as of 22 Jun"
  },
  {
    "figure_id": "F252",
    "report_id": "R029",
    "label": "Exhibit 15",
    "context": "Exhibit 15 - Agentic index for top 20 models as of 22 Jun ■ Proprietary □ Open Weights ▪ Open Weights (Commercial Use Restricted) Exhibit 16 - Coding index for top 20 models as of 22 Jun Exhibit 17 - Cost to run Artificial Intell"
  },
  {
    "figure_id": "F253",
    "report_id": "R029",
    "label": "Exhibit 15",
    "context": "Exhibit 15 - Agentic index for top 20 models as of 22 Jun ■ Proprietary □ Open Weights ▪ Open Weights (Commercial Use Restricted) Exhibit 16 - Coding index for top 20 models as of 22 Jun Exhibit 17 - Cost to run Artificial Intell"
  },
  {
    "figure_id": "F254",
    "report_id": "R029",
    "label": "Exhibit 16",
    "context": "Exhibit 16 - Coding index for top 20 models as of 22 Jun Exhibit 17 - Cost to run Artificial Intelligence Index as of 22 Jun Most attractive quadrant ## Exhibit 18 - Output speed to run Artificial Intelligence Index as of 22 Jun"
  },
  {
    "figure_id": "F255",
    "report_id": "R029",
    "label": "Exhibit 17",
    "context": "Exhibit 19 - Pricing plans for Alibaba, Tencent, Baidu and ByteDance"
  },
  {
    "figure_id": "F256",
    "report_id": "R029",
    "label": "Exhibit 41",
    "context": "Exhibit 41 - Token consumption for OpenClaw (bn) Exhibit 42 - Token consumption for Hermes Agent (bn) Exhibit 43 - Top 15 models used by OpenClaw over the last 30 days (as of 22 Jun)"
  },
  {
    "figure_id": "F257",
    "report_id": "R029",
    "label": "Exhibit 41",
    "context": "Exhibit 41 - Token consumption for OpenClaw (bn) Exhibit 42 - Token consumption for Hermes Agent (bn) Exhibit 43 - Top 15 models used by OpenClaw over the last 30 days (as of 22 Jun)"
  },
  {
    "figure_id": "F258",
    "report_id": "R029",
    "label": "Exhibit 45",
    "context": "Exhibit 45 - Global: Top 10 models by success rate as of 22 Jun Exhibit 46 - China: Top 10 models by success rate as of 22 Jun"
  },
  {
    "figure_id": "F259",
    "report_id": "R029",
    "label": "Exhibit 45",
    "context": "Exhibit 45 - Global: Top 10 models by success rate as of 22 Jun Exhibit 46 - China: Top 10 models by success rate as of 22 Jun ## AI Assistants \\- MoM trend: DAU for Qwen reached 27.9m in May (vs Apr: 29.2m) and Yuanbao reached 8"
  },
  {
    "figure_id": "F260",
    "report_id": "R029",
    "label": "Exhibit 47",
    "context": "Exhibit 47 - Weekly DAU for leading AI Assistants in China (mn) Exhibit 48 - Monthly DAU for Leading AI Assistants in China (mn) Exhibit 49 - Weekly user time spent per weekly DAU for leading AI Assistants in China (mins)"
  },
  {
    "figure_id": "F261",
    "report_id": "R029",
    "label": "Exhibit 47",
    "context": "Exhibit 47 - Weekly DAU for leading AI Assistants in China (mn) Exhibit 48 - Monthly DAU for Leading AI Assistants in China (mn) Exhibit 49 - Weekly user time spent per weekly DAU for leading AI Assistants in China (mins) Exhib"
  },
  {
    "figure_id": "F262",
    "report_id": "R029",
    "label": "Exhibit 48",
    "context": "Exhibit 48 - Monthly DAU for Leading AI Assistants in China (mn) Exhibit 49 - Weekly user time spent per weekly DAU for leading AI Assistants in China (mins) Exhibit 50 - Monthly user daily time spent per monthly DAU for leading"
  },
  {
    "figure_id": "F263",
    "report_id": "R029",
    "label": "Exhibit 48",
    "context": "Exhibit 51 - Top 15 image to video leaderboard (with audio)"
  },
  {
    "figure_id": "F264",
    "report_id": "R029",
    "label": "Exhibit 57",
    "context": "Exhibit 57 - MAU for Meituan app in past 12 months"
  },
  {
    "figure_id": "F265",
    "report_id": "R029",
    "label": "Exhibit 57",
    "context": "Exhibit 57 - MAU for Meituan app in past 12 months ## Online Music \\- MoM trend: MAU for Soda Music increased by 4% MoM to 166.8m in May. For TME, MAU for QQ Music/Kugou increased by 2%/1% MoM respectively and Kuwo declined by 2% M"
  },
  {
    "figure_id": "F266",
    "report_id": "R029",
    "label": "Exhibit 58",
    "context": "Exhibit 58 - MAU for TME, Soda Music and NetEase Cloud Music in May-26 250 Exhibit 59 - MAU for Soda Music in past 12 months Online video MAU for leading long form video platform declined YoY in May"
  },
  {
    "figure_id": "F267",
    "report_id": "R029",
    "label": "Exhibit 58",
    "context": "Exhibit 58 - MAU for TME, Soda Music and NetEase Cloud Music in May-26 250 Exhibit 59 - MAU for Soda Music in past 12 months Online video MAU for leading long form video platform declined YoY in May \\- MoM trend: MAU for Tencent"
  },
  {
    "figure_id": "F268",
    "report_id": "R029",
    "label": "Exhibit 60",
    "context": "Exhibit 60 - MAU for IQ, Tencent Video and Youku in May-26 ## Live-streaming and short video Douyin DAU maintained solid YoY growth in May \\- MoM trend: DAU for Douyin main app increased 2% MoM in May. For game broadcasting, MAU fo"
  },
  {
    "figure_id": "F269",
    "report_id": "R029",
    "label": "Exhibit 61",
    "context": "Exhibit 61 - DAU for Douyin over the past 12 months Online travel Exhibit 62 - MAU for BILI over the past 12 months TCOM MAU in domestic market decreased MoM in May after CNY in Feb"
  },
  {
    "figure_id": "F270",
    "report_id": "R029",
    "label": "Exhibit 61",
    "context": "Exhibit 63 - TCOM's MAU over the past 12 months"
  },
  {
    "figure_id": "F271",
    "report_id": "R029",
    "label": "Exhibit 63",
    "context": "Exhibit 63 - TCOM's MAU over the past 12 months ## News app • MoM: MAU for Weibo increased by 4% and MAU for Toutiao increased by 1% in May. MAU for Weibo experienced positive YoY growth in May"
  },
  {
    "figure_id": "F272",
    "report_id": "R029",
    "label": "Exhibit 64",
    "context": "Exhibit 64 - Weibo MAU over the past 12 months ## Baidu app • YoY: MAU declined by 8% YoY and DAU declined by 21% YoY in May."
  },
  {
    "figure_id": "F273",
    "report_id": "R029",
    "label": "Exhibit 65",
    "context": "Exhibit 65 - Baidu MAU over the past 12 months ## IDC estimates on tokens consumptions on public cloud and outlook Exhibit 66 - China's MaaS market monthly average daily token consumption in 2025"
  },
  {
    "figure_id": "F274",
    "report_id": "R029",
    "label": "Exhibit 65",
    "context": "Exhibit 68 - Market share of major vendors in China's MaaS market in 2025 (revenue basis)"
  },
  {
    "figure_id": "F275",
    "report_id": "R029",
    "label": "Exhibit 66",
    "context": "Exhibit 69 - Market share of major vendors in China's private large model platform market in 2025 (revenue basis)"
  },
  {
    "figure_id": "F276",
    "report_id": "R029",
    "label": "Exhibit 67",
    "context": "Exhibit 70 - The most important factors that drive people's decision to deploy model widely"
  },
  {
    "figure_id": "F277",
    "report_id": "R029",
    "label": "Exhibit 68",
    "context": "Exhibit 68 - Market share of major vendors in China's MaaS market in 2025 (revenue basis) Exhibit 69 - Market share of major vendors in China's private large model platform market in 2025 (revenue basis) Exhibit 70 - The most imp"
  },
  {
    "figure_id": "F278",
    "report_id": "R029",
    "label": "Exhibit 69",
    "context": "Exhibit 69 - Market share of major vendors in China's private large model platform market in 2025 (revenue basis) Exhibit 70 - The most important factors that drive people's decision to deploy model widely ## Appendix"
  },
  {
    "figure_id": "F279",
    "report_id": "R029",
    "label": "Exhibit 70",
    "context": "Exhibit 70 - The most important factors that drive people's decision to deploy model widely ## Appendix ## Omdia heatmap for agentic AI development platform in Asia and Oceania According to Omdia, agentic AI software market is ex"
  },
  {
    "figure_id": "F280",
    "report_id": "R029",
    "label": "Exhibit 73",
    "context": "Exhibit 73 - Global AI code tools market size (USDbn) Exhibit 74 - China AI code generation market size by service type (RMBbn) Exhibit 75 - China AI code penetration in different industries"
  },
  {
    "figure_id": "F281",
    "report_id": "R029",
    "label": "Exhibit 73",
    "context": "Exhibit 73 - Global AI code tools market size (USDbn) Exhibit 74 - China AI code generation market size by service type (RMBbn) Exhibit 75 - China AI code penetration in different industries In terms of AI code penetration, int"
  },
  {
    "figure_id": "F282",
    "report_id": "R029",
    "label": "Exhibit 74",
    "context": "Exhibit 76 - China AI + Workspace Market Size"
  },
  {
    "figure_id": "F283",
    "report_id": "R029",
    "label": "Exhibit 75",
    "context": "Exhibit 78 - Daily token consumption in China by enterprises in 2H25 vs 1H25 (tn)"
  },
  {
    "figure_id": "F284",
    "report_id": "R029",
    "label": "Exhibit 76",
    "context": "Exhibit 78 - Daily token consumption in China by enterprises in 2H25 vs 1H25 (tn) According to F&S, enterprise daily token consumption increased by 263% HoH to 37tn, among which market share for Alibaba Cloud increased the most and"
  },
  {
    "figure_id": "F285",
    "report_id": "R029",
    "label": "Exhibit 77",
    "context": "Exhibit 79 - Market share in terms of tokens used among enterprises in 1H25"
  },
  {
    "figure_id": "F286",
    "report_id": "R029",
    "label": "Exhibit 79",
    "context": "Exhibit 79 - Market share in terms of tokens used among enterprises in 1H25 Exhibit 80 - Market share in terms of tokens used among enterprises in 2H25 ## China Large Language Models"
  },
  {
    "figure_id": "F287",
    "report_id": "R029",
    "label": "Exhibit 79",
    "context": "Exhibit 81 - Market size of China LLM (RMB billions)"
  },
  {
    "figure_id": "F288",
    "report_id": "R029",
    "label": "Exhibit 81",
    "context": "Exhibit 81 - Market size of China LLM (RMB billions) China large language models are expected to increase by 64% CAGR between 2024 to 2030. By segment, on-premise is key revenue contributor Exhibit 82 - Market size of China Enterpr"
  },
  {
    "figure_id": "F289",
    "report_id": "R029",
    "label": "Exhibit 81",
    "context": "Exhibit 81 - Market size of China LLM (RMB billions) China large language models are expected to increase by 64% CAGR between 2024 to 2030. By segment, on-premise is key revenue contributor Exhibit 82 - Market size of China Enterpr"
  },
  {
    "figure_id": "F290",
    "report_id": "R029",
    "label": "Exhibit 83",
    "context": "Exhibit 83 - ARR of Anthropic Exhibit 84 - ARR of OpenAI Exhibit 85 - OpenAI revenue between 2023 and 2030F (as of 3Q25)"
  },
  {
    "figure_id": "F291",
    "report_id": "R029",
    "label": "Exhibit 83",
    "context": "Exhibit 83 - ARR of Anthropic Exhibit 84 - ARR of OpenAI Exhibit 85 - OpenAI revenue between 2023 and 2030F (as of 3Q25) Exhibit 86 - Revenue mix of OpenAI between 2024 and 2030F (as of 3Q25)"
  },
  {
    "figure_id": "F292",
    "report_id": "R029",
    "label": "Exhibit 84",
    "context": "Exhibit 84 - ARR of OpenAI Exhibit 85 - OpenAI revenue between 2023 and 2030F (as of 3Q25) Exhibit 86 - Revenue mix of OpenAI between 2024 and 2030F (as of 3Q25) Exhibit 87 - MiniMax: % of OpenAI revenue over the next few years"
  },
  {
    "figure_id": "F293",
    "report_id": "R029",
    "label": "Exhibit 85",
    "context": "Exhibit 85 - OpenAI revenue between 2023 and 2030F (as of 3Q25) Exhibit 86 - Revenue mix of OpenAI between 2024 and 2030F (as of 3Q25) Exhibit 87 - MiniMax: % of OpenAI revenue over the next few years ## Models of Leading Playe"
  },
  {
    "figure_id": "F294",
    "report_id": "R029",
    "label": "Exhibit 86",
    "context": "Exhibit 86 - Revenue mix of OpenAI between 2024 and 2030F (as of 3Q25) Exhibit 87 - MiniMax: % of OpenAI revenue over the next few years ## Models of Leading Players in China Exhibit 88 - Model list of Alibaba"
  },
  {
    "figure_id": "F295",
    "report_id": "R029",
    "label": "Exhibit 96",
    "context": "Exhibit 96 - Doubao daily token consumption ■ Daily token consumption (tn) Exhibit 97 - Token share by region"
  },
  {
    "figure_id": "F296",
    "report_id": "R029",
    "label": "Exhibit 96",
    "context": "Exhibit 96 - Doubao daily token consumption ■ Daily token consumption (tn) Exhibit 97 - Token share by region We would like to thank Fiona Fan, employee of Evalueserve Inc., for providing research support services to our prepar"
  },
  {
    "figure_id": "F297",
    "report_id": "R029",
    "label": "Exhibit 96",
    "context": "Exhibit 96 - Doubao daily token consumption ■ Daily token consumption (tn) Exhibit 97 - Token share by region We would like to thank Fiona Fan, employee of Evalueserve Inc., for providing research support services to our prepar"
  },
  {
    "figure_id": "F298",
    "report_id": "R038",
    "label": "Exhibit 27",
    "context": "EXHIBIT 2: As AI has strengthened, “bottlenecks’ have taken off YTD Average Returns By Sub-Sector As of 6/22/2026 EXHIBIT 3: Semiconductor stocks have been outperforming the broader market meaningfully YTD As of 6/22/2026"
  },
  {
    "figure_id": "F299",
    "report_id": "R038",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 4: SOX EPS is up \\~75% YTD, accounting for the bulk of the stock performance over that period As of 6/22/2026"
  },
  {
    "figure_id": "F300",
    "report_id": "R038",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Semi sales ex memory grew YoY in January, February, March and April by 31%, 28%, 25% and 33%, respectively Monthly Semiconductor Revenues Ex-Memory \\$B"
  },
  {
    "figure_id": "F301",
    "report_id": "R038",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 6: Revision behavior across our company samples was largely positive this quarter Consensus Estimate Change for Next Quarter's Revenue As of 6/18/2026"
  },
  {
    "figure_id": "F302",
    "report_id": "R038",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 7: PC shipments were up \\~3-4% YoY per IDC/Gartner, both decelerating \\~7ppts vs. last quarter YoY Change in PC Shipments"
  },
  {
    "figure_id": "F303",
    "report_id": "R038",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: Taiwan notebook shipments were down \\~4% YoY in April Taiwan ODM Notebook Shipments Monthly YoY Growth EXHIBIT 9: Taiwan notebook shipments fell 34% sequentially in April"
  },
  {
    "figure_id": "F304",
    "report_id": "R038",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 9: Taiwan notebook shipments fell 34% sequentially in April Taiwan ODM Notebook Shipments Monthly MoM Growth EXHIBIT 10: Overall, Q1 CPU shipments were mostly in-line with PCs..."
  },
  {
    "figure_id": "F305",
    "report_id": "R038",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: Overall, Q1 CPU shipments were mostly in-line with PCs... EXHIBIT 11: ...at \\~2% above PCs, up vs Q4 levels of \\~3% below"
  },
  {
    "figure_id": "F306",
    "report_id": "R038",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 12: Notebook CPU shipments were above notebooks in Q1..."
  },
  {
    "figure_id": "F307",
    "report_id": "R038",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Overall, Q1 CPU shipments were mostly in-line with PCs... EXHIBIT 11: ...at \\~2% above PCs, up vs Q4 levels of \\~3% below EXHIBIT 12: Notebook CPU shipments were above notebooks in Q1... EXHIBIT 13: ...\\~6% above,"
  },
  {
    "figure_id": "F308",
    "report_id": "R038",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: ...at \\~2% above PCs, up vs Q4 levels of \\~3% below EXHIBIT 12: Notebook CPU shipments were above notebooks in Q1... EXHIBIT 13: ...\\~6% above, vs the \\~1% below last quarter EXHIBIT 14: Desktop CPU shipments were"
  },
  {
    "figure_id": "F309",
    "report_id": "R038",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Notebook CPU shipments were above notebooks in Q1... EXHIBIT 13: ...\\~6% above, vs the \\~1% below last quarter EXHIBIT 14: Desktop CPU shipments were below PCs in Q1... Desktop PC vs CPU Shipments Millions EXHIBIT"
  },
  {
    "figure_id": "F310",
    "report_id": "R038",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: ...\\~6% above, vs the \\~1% below last quarter EXHIBIT 14: Desktop CPU shipments were below PCs in Q1... Desktop PC vs CPU Shipments Millions EXHIBIT 15: ...roughly \\~8% below, down vs \\~5% below last quarter Desktop"
  },
  {
    "figure_id": "F311",
    "report_id": "R038",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: ...roughly \\~8% below, down vs \\~5% below last quarter Desktop CPU Shipments Divided by PC Shipments EXHIBIT 16: Global smartphone shipments were down 3% YoY in Q1... Global Smartphone Shipment YoY Growth EXHIBIT 17:"
  },
  {
    "figure_id": "F312",
    "report_id": "R038",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Global smartphone shipments were down 3% YoY in Q1... Global Smartphone Shipment YoY Growth EXHIBIT 17: ...and were roughly in-line with pre-COVID seasonality QoQ CQ1 Smartphone Shipment Seasonality EXHIBIT 18: Hyper"
  },
  {
    "figure_id": "F313",
    "report_id": "R038",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 19: Euro auto sales were up (\\~3%) YoY in April"
  },
  {
    "figure_id": "F314",
    "report_id": "R038",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 20: US auto sales were up \\~3% YoY in April"
  },
  {
    "figure_id": "F315",
    "report_id": "R038",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Hyperscale capex spending was up in Q1 Super 7 Capex (\\$ Billions) EXHIBIT 19: Euro auto sales were up (\\~3%) YoY in April EXHIBIT 20: US auto sales were up \\~3% YoY in April EXHIBIT 21: Chinese autos retail sales"
  },
  {
    "figure_id": "F316",
    "report_id": "R038",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Euro auto sales were up (\\~3%) YoY in April EXHIBIT 20: US auto sales were up \\~3% YoY in April EXHIBIT 21: Chinese autos retail sales came in at 1.51mn units in May 2026, -20.0% yoy EXHIBIT 22: Auto semis \\$/car g"
  },
  {
    "figure_id": "F317",
    "report_id": "R038",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: US auto sales were up \\~3% YoY in April EXHIBIT 21: Chinese autos retail sales came in at 1.51mn units in May 2026, -20.0% yoy EXHIBIT 22: Auto semis \\$/car grew in the quarter andremain above trend.. Auto Semiconduc"
  },
  {
    "figure_id": "F318",
    "report_id": "R038",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 23: ...with unit content per car also growing in the quarter and remaining mostly on trend Auto Semiconductor Content Indexed to Q116=100"
  },
  {
    "figure_id": "F319",
    "report_id": "R038",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: ...with unit content per car also growing in the quarter and remaining mostly on trend Auto Semiconductor Content Indexed to Q116=100 EXHIBIT 24: Auto OEMs and Tier 1s saw a rise in inventory days this quarter, and Aut"
  },
  {
    "figure_id": "F320",
    "report_id": "R038",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 25: Raw materials/WIP grew across auto OEMs Auto OEM Materials and WIP Inventory Indexed to Q419 = 100"
  },
  {
    "figure_id": "F321",
    "report_id": "R038",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 25: Raw materials/WIP grew across auto OEMs Auto OEM Materials and WIP Inventory Indexed to Q419 = 100 EXHIBIT 26: Analog companies appear to be in recovery at this point Analog/Mixed-Signal Players YoY Revenue Growth As"
  },
  {
    "figure_id": "F322",
    "report_id": "R038",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 27: The street is modeling revenue growth for most semi companies in 2026 as AI strength continues and core semis recovers, though we note expected YoY declines amongst smartphone players amid memory constraints Revenue Grow"
  },
  {
    "figure_id": "F323",
    "report_id": "R038",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 29: SOX performance has been above the SPX YTD, with outperformance seen from Intel, AMD and Semicap EXHIBIT 28: SOX NTM earnings have risen 3 months ago and are at peak levels, due to AI strength and recovery in core semis"
  },
  {
    "figure_id": "F324",
    "report_id": "R038",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: SOX performance has been above the SPX YTD, with outperformance seen from Intel, AMD and Semicap EXHIBIT 28: SOX NTM earnings have risen 3 months ago and are at peak levels, due to AI strength and recovery in core semis"
  },
  {
    "figure_id": "F325",
    "report_id": "R038",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: SOX NTM earnings have risen 3 months ago and are at peak levels, due to AI strength and recovery in core semis SOX Implied NTM Earnings As of 6/22/ YTD Semiconductor Stock Performance As of 6/22/2026 EXHIBIT"
  },
  {
    "figure_id": "F326",
    "report_id": "R038",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: Stock performance around earnings was quite mixed this quarter Stock movement relative to SOX vs revenue guide surprise As of 6/18/2026 EXHIBIT 32: Some AI stocks have underperformed the SOX this year, with others seei"
  },
  {
    "figure_id": "F327",
    "report_id": "R038",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 33: Semis remain highly correlated to GDP growth Semiconductor demand continues to reflect YoY growth, with continued strength in memory and ex-memory sales"
  },
  {
    "figure_id": "F328",
    "report_id": "R038",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Some AI stocks have underperformed the SOX this year, with others seeing significant strength \"AI Stocks\" Performance Relative to SOX YTD and Prior 1-Month As of 6/22/2026 EXHIBIT 33: Semis remain highly correlated to"
  },
  {
    "figure_id": "F329",
    "report_id": "R038",
    "label": "Exhibit 34",
    "context": "EXHIBIT 34: Total semiconductor sales grew 106% YoY in April after rising 88% YoY in March EXHIBIT 35: Memory sales almost quintupled at 364.1% YoY; excluding memory, sales were still up strongly at 33.1% YoY EXHIBIT 36: Semicon"
  },
  {
    "figure_id": "F330",
    "report_id": "R038",
    "label": "Exhibit 40",
    "context": "EXHIBIT 37: The SOX is now outperforming the S&P 500 (by \\~194ppts) since the end of 2023 and outperforming by \\~97% YTD..."
  },
  {
    "figure_id": "F331",
    "report_id": "R038",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 37: The SOX is now outperforming the S&P 500 (by \\~194ppts) since the end of 2023 and outperforming by \\~97% YTD... As of 6/22/2026 EXHIBIT 38: ...with the SOX up \\~106.6% vs. the S&P 500 up \\~9.2% YTD"
  },
  {
    "figure_id": "F332",
    "report_id": "R038",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 38: ...with the SOX up \\~106.6% vs. the S&P 500 up \\~9.2% YTD As of 6/22/2026"
  },
  {
    "figure_id": "F333",
    "report_id": "R038",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: The SOX is now outperforming the S&P 500 (by \\~194ppts) since the end of 2023 and outperforming by \\~97% YTD... As of 6/22/2026 EXHIBIT 38: ...with the SOX up \\~106.6% vs. the S&P 500 up \\~9.2% YTD As of 6/22/2026 EX"
  },
  {
    "figure_id": "F334",
    "report_id": "R038",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: ...with the SOX up \\~106.6% vs. the S&P 500 up \\~9.2% YTD As of 6/22/2026 EXHIBIT 39: Over the last 3 months, the SOX has markedly outperformed the S&P 500 and the NASDAQ As of 6/22/2026 EXHIBIT 40: On an absolute ba"
  },
  {
    "figure_id": "F335",
    "report_id": "R038",
    "label": "EXHIBIT 39",
    "context": "Exhibit 41-Exhibit 44). EXHIBIT 41: 0 companies in our sample missed the current quarter, 2 missed next quarter and 18 built inventory in the quarter"
  },
  {
    "figure_id": "F336",
    "report_id": "R038",
    "label": "Exhibit 41",
    "context": "Exhibit 41-Exhibit 44). EXHIBIT 41: 0 companies in our sample missed the current quarter, 2 missed next quarter and 18 built inventory in the quarter EXHIBIT 42: 0 companies in our sample missed revenue estimates for Q1, guidance"
  },
  {
    "figure_id": "F337",
    "report_id": "R038",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 44: 2 companies in our sample missed guidance for the next quarter versus expectations"
  },
  {
    "figure_id": "F338",
    "report_id": "R038",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 44: 2 companies in our sample missed guidance for the next quarter versus expectations ## Q1 results were above seasonal with above seasonal expectations for next quarter Q1 results were above seasonal as we saw continued"
  },
  {
    "figure_id": "F339",
    "report_id": "R038",
    "label": "Exhibit 45",
    "context": "EXHIBIT 45: Consensus appears to expect revenue growth above seasonal in Q2... EXHIBIT 46: ...and expects CQ3 and CQ4 above seasonal Comparison Between Consensus QoQ Growth Estimates and Historical Seasonality"
  },
  {
    "figure_id": "F340",
    "report_id": "R038",
    "label": "Exhibit 45",
    "context": "EXHIBIT 47: Negative revisions were down a little vs a quarter ago"
  },
  {
    "figure_id": "F341",
    "report_id": "R038",
    "label": "Exhibit 47",
    "context": "EXHIBIT 47: Negative revisions were down a little vs a quarter ago % of Reported Semiconductor Company Earnings Revisions that are Negative R2 of SOX - EPS Correlation % of companies demonstrating MoM negative revision to NTM EPS;"
  },
  {
    "figure_id": "F342",
    "report_id": "R038",
    "label": "EXHIBIT 48",
    "context": "% of Reported Semiconductor Company Earnings Revisions that are Negative R2 of SOX - EPS Correlation % of companies demonstrating MoM negative revision to NTM EPS; 3-month smoothed. Negative revision if changes by at least 1% Average inventory days in the chan"
  },
  {
    "figure_id": "F343",
    "report_id": "R038",
    "label": "Exhibit 49",
    "context": "EXHIBIT 51: Semiconductor days of inventory were up slightly and remain extremely high vs history..."
  },
  {
    "figure_id": "F344",
    "report_id": "R038",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 52: ... and were up on an aggregate basis"
  },
  {
    "figure_id": "F345",
    "report_id": "R038",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 52: ... and were up on an aggregate basis Semiconductors Days of Inventory Aggregate Semiconductor Changes in Inventory"
  },
  {
    "figure_id": "F346",
    "report_id": "R038",
    "label": "EXHIBIT 51",
    "context": "EXHIBIT 53: Overall distributor inventory dollars were up QoQ and YoY"
  },
  {
    "figure_id": "F347",
    "report_id": "R038",
    "label": "EXHIBIT 53",
    "context": "EXHIBIT 53: Overall distributor inventory dollars were up QoQ and YoY EXHIBIT 54: Semiconductor company inventory dollars were up QoQ and YoY Semi relative valuations now stand at a $\\sim 62\\%$ premium to the S&P (vs $\\sim 6\\%$"
  },
  {
    "figure_id": "F348",
    "report_id": "R038",
    "label": "EXHIBIT 53",
    "context": "EXHIBIT 55: The SOX trades at a \\~62% premium to the SPX, up significantly vs 3 months ago"
  },
  {
    "figure_id": "F349",
    "report_id": "R038",
    "label": "Exhibit 55",
    "context": "EXHIBIT 55: The SOX trades at a \\~62% premium to the SPX, up significantly vs 3 months ago As of 6/22/2026 As of 6/22/2026 EXHIBIT 56: SOX valuations have risen markedly recently"
  },
  {
    "figure_id": "F350",
    "report_id": "R038",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 57: Semiconductor industry crowding has risen markedly in recent months, and is well above the high-end of the historical range vs the broader market..."
  },
  {
    "figure_id": "F351",
    "report_id": "R038",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 57: Semiconductor industry crowding has risen markedly in recent months, and is well above the high-end of the historical range vs the broader market... EXHIBIT 58: ...crowding has also risen vs the TMT sector and is above"
  },
  {
    "figure_id": "F352",
    "report_id": "R038",
    "label": "Exhibit 57",
    "context": "EXHIBIT 57: Semiconductor industry crowding has risen markedly in recent months, and is well above the high-end of the historical range vs the broader market... EXHIBIT 58: ...crowding has also risen vs the TMT sector and is above"
  },
  {
    "figure_id": "F353",
    "report_id": "R039",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Overview of Auto OEMs progresses in humanoid robots EXHIBIT 2: Overview of Auto OEMs' humanoid robot products Tesla Optimus v2.5 XPeng IRON Xiaomi CyberOne GAC GoMate"
  },
  {
    "figure_id": "F354",
    "report_id": "R039",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Overview of Auto OEMs' humanoid robot products Tesla Optimus v2.5 XPeng IRON Xiaomi CyberOne GAC GoMate"
  },
  {
    "figure_id": "F355",
    "report_id": "R039",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Overview of Auto OEMs' humanoid robot products Tesla Optimus v2.5 XPeng IRON Xiaomi CyberOne GAC GoMate EXHIBIT 3: Chery's Aimoga"
  },
  {
    "figure_id": "F356",
    "report_id": "R039",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Chery's Aimoga EXHIBIT 4: AgiBot was showcased at BYD's exhibition"
  },
  {
    "figure_id": "F357",
    "report_id": "R039",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Chery's Aimoga EXHIBIT 4: AgiBot was showcased at BYD's exhibition ## WHY AUTO OEMS ARE EXPANDING INTO HUMANOID ROBOTS?"
  },
  {
    "figure_id": "F358",
    "report_id": "R039",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Chery's Aimoga EXHIBIT 4: AgiBot was showcased at BYD's exhibition ## WHY AUTO OEMS ARE EXPANDING INTO HUMANOID ROBOTS? Auto OEMs are expanding into humanoid robotics for two main reasons: to raise internal productiv"
  },
  {
    "figure_id": "F359",
    "report_id": "R039",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Humanoid robots: Technically feasible applications across the near-, mid-, and long-term future Humanoid robots: Technically feasible applications EXHIBIT 7: Where and in what applications can humanoid robots be used E"
  },
  {
    "figure_id": "F360",
    "report_id": "R039",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 10: Chery's Aimoga is used in public security scenarios"
  },
  {
    "figure_id": "F361",
    "report_id": "R039",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 10: Chery's Aimoga is used in public security scenarios EXHIBIT 11: Hexagon's humanoid robot AEON at BMW's Leipzig plant"
  },
  {
    "figure_id": "F362",
    "report_id": "R039",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: XPeng plans to deploy 1,000 robots at its showrooms by year-end 2026 EXHIBIT 10: Chery's Aimoga is used in public security scenarios EXHIBIT 11: Hexagon's humanoid robot AEON at BMW's Leipzig plant ## AUTO OEMS' RI"
  },
  {
    "figure_id": "F363",
    "report_id": "R039",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Chery's Aimoga is used in public security scenarios EXHIBIT 11: Hexagon's humanoid robot AEON at BMW's Leipzig plant ## AUTO OEMS' RIGHT TO WIN IN HUMANOID ROBOTICS Automakers have several advantages that make them w"
  },
  {
    "figure_id": "F364",
    "report_id": "R039",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Sensitivity analysis of the payback period to humanoid robot prices and labor cost EXHIBIT 15: Adoption speed of automobiles in the early years can be regarded as a reference Note: Registration is more like a concept o"
  },
  {
    "figure_id": "F365",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Yields have lagged the move in oil prices Exhibit 2: Even using a broader measure of energy prices, yields look 10-15bp too high There are a few reasons EM yields have not fallen further US yields have moved higher:"
  },
  {
    "figure_id": "F366",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Yields have lagged the move in oil prices Exhibit 2: Even using a broader measure of energy prices, yields look 10-15bp too high There are a few reasons EM yields have not fallen further US yields have moved higher:"
  },
  {
    "figure_id": "F367",
    "report_id": "R044",
    "label": "Exhibit 3",
    "context": "Exhibit 3: EM yield compression vs USTs continues in nominal terms... Exhibit 4: ... and in real terms EM has reversed US-Iran conflict underperformance USD strength. There continues to be a good correlation between movements i"
  },
  {
    "figure_id": "F368",
    "report_id": "R044",
    "label": "Exhibit 4",
    "context": "Exhibit 3: EM yield compression vs USTs continues in nominal terms... Exhibit 4: ... and in real terms EM has reversed US-Iran conflict underperformance USD strength. There continues to be a good correlation between movements i"
  },
  {
    "figure_id": "F369",
    "report_id": "R044",
    "label": "Exhibit 2",
    "context": "Exhibit 5: FX performance helps to explain relative bond performance... 2y LCY Bond Yield (chg since 27-Feb, bp) Exhibit 6: ...but does little to explain the lag in index yields vs energy prices EM monetary policy still points"
  },
  {
    "figure_id": "F370",
    "report_id": "R044",
    "label": "Exhibit 2",
    "context": "Exhibit 7: 1y1y rates are higher in EM than Feb 27th levels"
  },
  {
    "figure_id": "F371",
    "report_id": "R044",
    "label": "Exhibit 8",
    "context": "Exhibit 7: 1y1y rates are higher in EM than Feb 27th levels Exhibit 8: MS more dovish than market on central bank pricing ## Stay Long EM vs Basket"
  },
  {
    "figure_id": "F372",
    "report_id": "R044",
    "label": "Exhibit 7",
    "context": "Exhibit 7: 1y1y rates are higher in EM than Feb 27th levels Exhibit 8: MS more dovish than market on central bank pricing ## Stay Long EM vs Basket We argued in our last EM strategist (see Global EM Strategist: Finding Your Fun"
  },
  {
    "figure_id": "F373",
    "report_id": "R044",
    "label": "Exhibit 9",
    "context": "Exhibit 9: EM vs DM Gains Continue Exhibit 10: Broad EM FX gains vs many DM funders ## What can we say about positioning?"
  },
  {
    "figure_id": "F374",
    "report_id": "R044",
    "label": "Exhibit 9",
    "context": "Exhibit 9: EM vs DM Gains Continue Exhibit 10: Broad EM FX gains vs many DM funders ## What can we say about positioning? In EM local currency bond markets, our flow tracker covers 9 EM markets – all benchmark countries – that"
  },
  {
    "figure_id": "F375",
    "report_id": "R044",
    "label": "Exhibit 11",
    "context": "Exhibit 13: Inflows are correlated with returns. So if we hit extremes on outflows (not there yet) the risk/reward to enter the market could be strong"
  },
  {
    "figure_id": "F376",
    "report_id": "R044",
    "label": "Exhibit 11",
    "context": "Exhibit 13: Inflows are correlated with returns. So if we hit extremes on outflows (not there yet) the risk/reward to enter the market could be strong In FX markets, we use FX options data to gauge positioning, and these data cont"
  },
  {
    "figure_id": "F377",
    "report_id": "R044",
    "label": "Exhibit 12",
    "context": "Exhibit 13: Inflows are correlated with returns. So if we hit extremes on outflows (not there yet) the risk/reward to enter the market could be strong In FX markets, we use FX options data to gauge positioning, and these data cont"
  },
  {
    "figure_id": "F378",
    "report_id": "R044",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Much of CEEMEA and Asia have underperformed ytd)"
  },
  {
    "figure_id": "F379",
    "report_id": "R044",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Much of CEEMEA and Asia have underperformed ytd) ## Required reading Senegal's local currency auctions are an important driver of sovereign credit valuations. In this tracker, we break down the latest auction and place"
  }
]