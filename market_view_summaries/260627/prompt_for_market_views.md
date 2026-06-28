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
    "title": "Citi：全球经济的下一个“超预期”冲击不是地缘，是天气",
    "digest": "[wechat_article.md]\n# Citi：全球经济的下一个“超预期”冲击不是地缘，是天气\n\n全球经济的韧性正在经历一次真正的压力测试。Citi最新发布的《全球经济展望与策略》报告给出一个核心判断：中东冲突的缓解正在移除一个持续数季的供给端阴霾，但与此同时，一场潜在的“超级厄尔尼诺”事件正在酝酿，可能成为下一个更持久、更难以对冲的供给冲击。\n\n这份报告的价值不在于它预测了油价在75美元/桶附近企稳——这是市场已经部分定价的。真正值得关注的是，Citi用大量篇幅和数据分析了一个被多数投资者低估的变量：天气。当全球央行刚刚开始松一口气、准备正常化货币政策时，一场可能持续到2027年3月的强厄尔尼诺事件，正在改变通胀路径、财政空间和资产定价的底层假设。\n\n我们仔细拆解了这份超过50页的报告，提炼出五个最值得产业决策者和投资者关注的洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球经济的“油压”正在释放，但增长已经永久性损失了约0.4个百分点\n\n中东局势的阶段性缓和确实带来了好消息。Citi判断，随着美国与伊朗签署谅解备忘录，霍尔木兹海峡的通行正在逐步恢复。布伦特油价预计在2026年下半年平均维持在75美元/桶左右，这比冲突爆发前的预期高出15美元，但已远低于此前100美元以上的高位。\n\n然而，不要误读为“风险解除”。Citi明确指出，全球经济已经承受了一段持续的高油价时期，全球增速已从冲突前的2.9%降至2.5%。这意味着，即使地缘溢价消退，增长缺口已经形成。更关键的是，不同经济体的受损程度高度分化。\n\n> **KC评论：** 这里的核心含义是，投资者不应因为油价回落就“抄底”所有受冲击的资产。Citi的数据显示，菲律宾、越南、瑞典等高度依赖石油进口的经济体，增速被下修了0.75个百分点甚至更多。而韩国、台湾、新加坡等受益于AI出口的经济体\n\n[... middle omitted ...]\n\n投资与天气冲击的交互作用有进一步兴趣，欢迎来社群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球经济的下一只灰犀牛来了\n\n🌍 全球经济迎来关键转折\n\n刚消化完中东冲突的冲击,又一只灰犀牛正在逼近。\n\n某外资投行最新研报指出:全球经济韧性超出预期,但新的风险正在酝酿。\n\n1️⃣ 中东局势现转机\n美伊达成60天临时协议,霍尔木兹海峡有望重新开放。但完全恢复通航还需数月:清除水雷、重建保险体系、协商通行费...这些都需要时间。\n\n全球经济已消化了油价长期高于100美元/桶的冲击,当前增速从冲突前的2.9%降至2.5%。\n\n2️⃣ 真正的风险:超级厄尔尼诺\nNOAA预测:2026年出现超强厄尔尼诺概率超过95%,其中63%可能达到“极强”级别。这将是1902年以来最强的一次。\n\n历史经验表明,极端厄尔尼诺会:\n- 扰乱全球农业产出,推高食品价格\n- 影响水力发电,巴西、哥伦比亚等国首当其冲\n- 干扰航运(还记得巴拿马运河干旱吗?)\n- 降低户外劳动生产率\n\n3️⃣ AI成为意外支撑\n美国Q1 AI相关投资飙升至4000亿美元(年化),带动韩国、台湾、新加坡等科技出口国逆势增长。\n\n但财政和货币政策空间有限,全球央行开始正常化,政府债务压力上升。\n\n全球通胀今年预计3.4%,明年回落至2.7%。\n\n一个有趣的\n\n[... middle omitted ...]\n\nthat global growth is tracking at 2½%, down from 2.9% prior to the conflict. Meanwhile a new risk to the global economy may be emerging. NOAA ascribes a greater than 95% probability to an El N\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R002",
    "title": "GS：油价下跌正在重建利率市场的对冲功能",
    "digest": "[wechat_article.md]\n# GS：油价下跌正在重建利率市场的对冲功能\n\n过去几周，全球利率市场经历了一次微妙但关键的结构性转变。原油价格持续回落，不仅直接压低了通胀预期，更在重塑一个被市场忽视的核心问题：名义利率作为风险资产对冲工具的功能正在恢复。\n\n这份GS全球利率交易报告的核心判断是：能源价格下跌正在改变通胀与增长风险的共动关系，从而让美国利率重新具备了对冲风险资产的能力。这不是一个短期交易信号，而是对利率定价机制的一次底层修复。\n\n理解这一点，才能理解为什么GS认为当前曲线中段(1y1y或2y1y)的多头头寸具有不对称优势，以及为什么欧洲利率波动率将继续跑输美国。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源价格下跌正在修复利率作为风险对冲工具的核心功能\n\n过去两年，利率市场最令人困惑的问题之一是：为什么股票跌的时候债券不涨了？原因在于通胀与增长风险从\"反向\"变成了\"同向\"——通胀上行时，央行不得不加息，债券收益率反而上升，失去了对冲功能。\n\nGS现在明确表示，油价下跌正在打破这个困局。能源价格回落降低了通胀上行风险，使通胀与增长风险重新回到\"共动\"状态，而非此消彼长。这意味着，当风险资产下跌时，利率可以再次提供对冲保护。\n\n报告特别指出，短期实际利率已经开始参与反弹，前端偏斜度从鹰派极端水平回摆，美联储定价也从极端鹰派位置有所缓和。这不是市场情绪的自然回归，而是定价机制本身在修复。\n\n> **KC评论：** 对资产配置者来说，这意味着债券在组合中的角色正在被重新定义。过去两年\"股债双杀\"的痛感可能正在消退。完整报告中有一张前端偏斜度回摆的图表，直观展示了美联储定价从极端鹰派位置回撤的过程，是判断这一修复是否可持续的关键证据。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 美联储\n\n[... middle omitted ...]\n\net dynamics。欢迎加入，继续讨论这些未解问题。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价缓口气，全球利率怎么走\n\n🔹油价回落带来的喘息\n\n全球能源价格持续走低，通胀压力明显缓解。这让各国利率市场都松了一口气，尤其是美国前端利率此前因通胀预期而大幅走高的压力开始消退。\n\n🔹美国：关注曲线中段\n\n1️⃣ 最近美联储定价从极端鹰派位置回落，前端利率的偏斜已经转向接收方\n2️⃣ 研报认为，与其押注短期利率下行，不如关注略远一点的曲线位置（如1年后的1年期利率或2年后的1年期利率）\n3️⃣ 如果未来几个月就业和通胀数据温和，到2026年底美联储维持利率不变的概率会逐渐增大\n\n🔹欧洲：窄幅震荡，关注监管红利\n\n1️⃣ 欧洲利率波动率主要受能源不确定性驱动，油价回落应该会降低波动率而非收益率水平\n2️⃣ 9月ECB会议定价仍处于0-1次加息之间，市场预期相对平衡\n3️⃣ Solvency II审查即将实施，对长期主权债券需求构成支撑——保险公司需要增加利率对冲，这是被低估的结构性利好\n\n🔹英国：前端继续表现，但长端空间有限\n\n1️⃣ 10年期Gilt收益率下降主要是期限溢价压缩所致，而非加息预期消退\n2️⃣ 前端利率仍有进一步下行空间，但长端进一步压缩的门槛较高\n3️⃣ 倾向于做陡曲线，即押注前端表现优于\n\n[... middle omitted ...]\n\nEuropean rates should remain in a relatively tight range as September ECB pricing remains between 0-1 hike. Lower rates vol and growth risks should favour front-end EGB spreads, with the upcom\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "GS：美元短期看涨，但AI资本开支才是真正变数",
    "digest": "[wechat_article.md]\n# GS：美元短期看涨，但AI资本开支才是真正变数\n\n这份GS外汇策略报告的核心判断是：美元短期仍有上行风险，但中期路径取决于三个关键变量——利率预期何时逆转、美联储信誉是否受损、以及美国经济能否维持“例外主义”。而AI相关资本开支，正在成为重塑这一格局的底层力量。\n\n报告没有简单给出“美元涨还是跌”的二元结论，而是构建了一个从利率差到AI资本流动的完整分析框架。在这个框架下，真正值得关注的不是美元本身的方向，而是驱动美元变化的力量正在从传统的利率差，转向更复杂的结构性因素——尤其是AI对美国资本流入和经常账户的深远影响。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及一个报告尚未完全展开但值得追问的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美元短期强势由利率差驱动，但这轮利率预期的修正可能比市场想象得更快\n\n报告明确指出，美元近期走强的核心驱动力不是地缘风险或避险情绪，而是最传统的变量——利率差。美联储6月会议释放鹰派信号后，市场对利率路径的重新定价直接推动了美元突破此前波动区间。\n\n值得注意的一点是：报告认为油价下跌未能压制美元，恰恰印证了利率差才是当前的主导因素。对于习惯了“商品货币”逻辑的投资者来说，这是一个重要的框架转换。\n\n> **KC评论：** 很多投资者习惯用油价或风险偏好来解释美元走势，但GS这份报告提醒我们，当前阶段回归“利率差”这个最基础的变量可能更有效。报告中的图表详细展示了利率差与美元汇率的历史关系，但限于篇幅，这里无法完整呈现。完整报告里还有一套利率差与汇率回归的定量分析，可以帮助读者判断当前美元定价是否已经充分反映了利率预期。\n\n报告给出的短期判断是：美元上行风险仍在，因为加息概率“可能快速上升，但消退会很缓慢”。这意味着市场对美联储转鸽的定价可能过度乐观，短期内\n\n[... middle omitted ...]\n\n的知识星球微信群，与更多产业决策者和专业投资者一起讨论交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元近期的强势还能持续多久\n\n强势美元，但后劲存疑\n\n最近美元走强，不少人觉得奇怪：油价明明在跌，美元怎么反而涨了？\n\n其实核心逻辑很简单——利率差。美联储鹰派表态后，美债利率走高，资金自然青睐美元。短期看，加息预期可能还会推一把美元，但中期风险已经更均衡了。\n\n美元走弱的三条路：\n1️⃣ 如果市场开始定价未来降息（符合多数经济学家的判断），美元会跌回之前几个月的区间\n2️⃣ 如果市场对央行独立性产生担忧，美元也会承压\n3️⃣ 下半年美国经济增速放缓，美元可能跟着走弱\n\n但注意！如果AI带动的资本支出太猛，美联储觉得政策不够紧，反而可能继续加息——这对美元是额外支撑，但对欧洲那些被迫输入紧缩的国家来说，压力更大。\n\n新兴市场：低息货币最受伤\n泰铢、以色列谢克尔、智利比索，过去一周跌得最惨。共同点？都是各自区域里利率最低的货币。美联储鹰派→美债利率走高→低息货币被抛售，逻辑很顺。\n\n不过这三只货币各有特色：\n- 谢克尔对科技股最敏感，适合做对冲\n- 智利比索跟铜价绑定，适合对冲周期风险\n- 泰铢跟黄金联动，金价继续跌的话，它还得承压\n\n英镑：政治溢价已消失\n最近英镑走稳，主要因为新首相的胜选大幅缩小了领导层不确\n\n[... middle omitted ...]\n\nerm because we think the probability of rate hikes could move up quickly, but come out only slowly. Over the medium term, however risks remain more balanced. We see three primary routes for th\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "GS：市场正从宏观波动转向微观波动",
    "digest": "[wechat_article.md]\n# GS：市场正从宏观波动转向微观波动\n\n当全球投资者还在为油价、美联储和地缘政治焦头烂额时，一份来自GS的最新研报提出了一个反直觉的判断：**宏观不确定性正在快速退潮，而微观层面的波动将成为未来市场的主导旋律。**\n\n这不是一个温和的过渡。它意味着过去两年驱动资产价格的核心变量——通胀、利率、地缘风险——正在让位于另一组更难以捉摸的力量：AI投资回报的争议、个股层面的盈利分化、以及估值与基本面之间的张力。\n\n这份报告由GS全球市场策略主管Kamakshya Trivedi和首席策略师Dominic Wilson联合撰写，于6月底发布。报告的核心信息可以浓缩为一句话：**市场已经消化了大部分坏消息，但好消息也被充分定价了。接下来的博弈，将从“宏观叙事”转向“微观验证”。**\n\n对于习惯了用宏观框架做决策的投资者来说，这意味着观察框架需要调整。而这份报告恰好提供了一张路线图。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油价冲击消退，宏观波动率正在系统性下降\n\n报告最明确的信号来自能源端。GS指出，伊朗战争停火协议的签署以及霍尔木兹海峡能源运输的恢复，正在系统性地降低全球市场最大的宏观不确定性来源。\n\n这不是一个边际改善。数据显示，波斯湾地区的石油出口已恢复至正常水平的66%，这一数字还在上升。更重要的是，市场此前已经在相当程度上“看穿”了油价冲击——股票市场早已回到战前水平上方，但原油期货合约和利率市场仍残留着部分溢价。\n\nGS大宗商品团队对四季度布伦特原油的基准预测是80美元/桶，但明确表示风险双向。然而，市场已经开始探索下行尾部——即生产快速恢复后出现短期供应过剩的情景。\n\n> **KC评论：** 油价冲击的消退，相当于拆除了市场最大的“尾部风险炸弹”。但这不意味着油价会直线下跌。关键是，GS认为这个变量对\n\n[... middle omitted ...]\n\n节、美联储利率路径的概率分布、以及不同情景下的资产配置建议。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价降温，市场焦点在换挡\n\n从宏观波动转向微观博弈\n\n最近全球市场出现了一个有意思的切换：油价带来的宏观不确定性在下降，但AI相关资产内部的微观波动反而在加剧。\n\n投行研报给出了这样几个观察点：\n\n1/ 油价回落降低宏观风险\n美伊协议落地后，霍尔木兹海峡的能源运输已恢复至正常水平的66%。油价从高位回落，意味着“高通胀+低增长”这种极端尾部风险的概率在降低。这对全球资产定价是个好消息。\n\n2/ 美联储是新的关注点\n6月议息会议偏鹰，市场开始提前定价加息。但研报认为，油价下跌会缓解通胀压力，未来2-3个月后加息的必要性会降低。当前市场对利率的定价可能过度悲观，反而提供了机会。\n\n3/ 宏观波动下降，微观波动上升\n最值得关注的观点是：股市的整体波动率在下降，但个股之间的分化在加剧。AI板块的估值已经很高，需要越来越乐观的假设才能支撑当前价格。一旦市场对AI投资回报的预期出现动摇，就会引发剧烈波动。\n\n4/ 美元“分裂”走势\n美联储偏鹰支撑美元走强，但亚洲国家（日本、中国、印度）的汇率管理措施限制了美元涨幅。美元整体偏强，但不同货币对的表现会分化。\n\n5/ 新兴市场有机会\n油价下跌对石油进口国（印度、土耳其、埃及）\n\n[... middle omitted ...]\n\ned hike risk is now the main macro concern, following a more hawkish Fed meeting in June. That risk is likely to stay on the agenda for a while and could cause more local volatility with a del\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "JPM：全球经济的真正风险不是衰退，是加息",
    "digest": "[wechat_article.md]\n# JPM：全球经济的真正风险不是衰退，是加息\n\n2026年上半年的能源价格冲击，并没有改变JPM全球研究团队的核心判断——全球经济正处于一轮由商业信心修复和技术投资扩张共同驱动的周期性回升之中。这份6月发布的中期展望报告，在标题“A Cyclical State of Mind”中就已亮明立场：市场对“结构性放缓”的叙事过于悲观，真正的张力不在增长本身，而在增长带来的通胀压力，以及央行被迫加息的连锁反应。\n\n这不是一份简单的“经济预测更新”。它试图回答一个在2026年初被广泛争论的问题：去年全球就业市场的停滞，究竟是结构性拐点，还是暂时性调整？JPM给出了明确的答案——是后者。而这一判断的兑现，意味着投资者需要重新校准对利率路径、资产定价和企业盈利的预期。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源冲击没有打断周期，只是让通胀问题变得更棘手\n\n霍尔木兹海峡的关闭一度让市场陷入恐慌。油价飙升、CPI跳升、央行转鹰——这些因素叠加，使2026年一季度末的全球增长预期被下调了0.2个百分点。但JPM认为，随着海峡重新开放的协议达成，最坏情景已经排除。\n\n关键不在于冲击本身，而在于冲击后的传导路径。报告明确指出，能源价格对核心通胀的传导效应将持续存在。2026年全球核心CPI预计将上升超过0.2个百分点，且这一上调并非一次性——它意味着核心通胀将连续第六年高于央行目标。\n\n> **KC评论：** 能源冲击是短期变量，但核心通胀的粘性是长期变量。JPM的核心判断是，即便油价回落，通胀也不会回到疫情前水平。这对利率路径的影响，远比一次能源冲击更深远。完整报告中对“核心商品价格模型”和“服务通胀的劳动力成本传导”有更详细的拆解，值得细读。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球经济的“中场休息”\n\n📌 周期正在切换\n\n全球经济的剧本在年中悄悄改写。能源冲击让增长短暂承压，但一场由科技扩张和商业信心回暖驱动的周期上行已经拉开序幕。这不是一个简单的“V型”反弹，更像是一场结构性的“换挡”。\n\n1️⃣ 能源冲击是“插曲”，不是终章\n霍尔木兹海峡的重新开放，让能源价格飙升的风险大幅降低。尽管二季度CPI跳升暂时挤压了消费，但全球GDP增长只是“中场休息”，而非趋势逆转。库存周期转向、财政政策托底、以及能源价格回落后的信心修复，将为下半年经济再加速铺路。\n\n2️⃣ 科技扩张正在“下沉”\nAI投资不再是少数巨头的游戏，支出正向更广泛的行业渗透。这不仅在提升生产率，也实实在在地拉动全球需求。科技相关的资本开支和工业产出，成为支撑增长的“硬核”力量。\n\n3️⃣ 就业和欧洲是两大看点\n美国就业增长正在提速，每月10万+的岗位增加已从“预期”变为“现实”。而欧洲的景气指数有望快速回升，欧元区增速可能在下半年回归趋势之上。这意味着，本轮复苏的“广度”正在改善，不再只有美国在唱独角戏。\n\n4️⃣ 通胀的“烫手山芋”交给央行\n全球核心CPI连续第六年高于目标。强劲增长+能源冲击+劳动力紧张，让通胀压力根深\n\n[... middle omitted ...]\n\nit of Hormuz. However, global GDP growth is still expected to downshift into midyear as the recent CPI spike softens consumption gains.\n\n\\- Several factors should temper this downshift and set\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R006",
    "title": "GS：全球央行正在“明紧暗松”，但市场可能低估了加息风险",
    "digest": "[wechat_article.md]\n# GS：全球央行正在“明紧暗松”，但市场可能低估了加息风险\n\n全球央行在2026年6月的最新政策立场出现了一个罕见的背离：过去三个月，发达市场没有一家央行降息，39%的央行选择了加息。但与此同时，GS的全球金融条件指数却显示，全球金融条件反而宽松了24个基点。这不是数据打架，而是全球货币政策正在进入一个关键的分化阶段——名义利率在上升，但实际金融条件在宽松。GS最新发布的《中央银行政策追踪》报告揭示了一个重要信号：市场可能过于乐观地定价了降息，而低估了部分经济体的加息风险。\n\n这份由首席经济学家Jan Hatzius团队撰写的报告，覆盖了全球30多个主要经济体的政策利率预测，核心判断是：未来四个季度，全球央行加权平均利率只会下降0.1个百分点至3.1%，但发达市场平均将加息8个基点，新兴市场平均降息33个基点。换句话说，全球利率不会出现市场期待的“降息潮”，而是“发达市场加息、新兴市场分化”的格局。\n\n> **KC评论：** GS的核心结论与市场主流预期存在明显偏差。当前市场定价显示，市场预期73%的发达市场和57%的新兴市场利率会低于GS预测——说明市场比GS更乐观。但GS认为，这种乐观定价可能忽略了地缘冲突（伊朗战争）对通胀和央行决策的持续影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 过去三个月：没有一家发达市场央行降息，39%选择加息\n\n这是这份报告最引人注目的数据点。在全球经济增速放缓的背景下，发达市场央行的集体鹰派转向，与市场此前的降息预期形成了鲜明反差。\n\n从Exhibit 4和Exhibit 5可以清晰看到，过去三个月的政策利率变化呈现出明显的“上移”趋势。发达市场中，加息的国家和地区包括新西兰、欧元区、瑞典、挪威和日本，而美国、英国等经济体则选择了按兵不动。新兴市场方面，16%的央行选择\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球央行最新动向：加息潮未退，降息在远处\n\n全球央行“鹰”声依旧\n\n最近三个月，全球央行动作有点意思。发达市场（DM）没有一家降息，39%在加息；新兴市场（EM）16%降息，7%加息。但有意思的是，全球金融条件反而在放松——过去三个月放松了24个基点，发达市场贡献了34个基点的宽松，新兴市场也有10个基点。\n\n1️⃣ **金融条件分化明显**\n土耳其金融条件最宽松（-117bps），韩国（-93bps）和罗马尼亚（-83bps）紧随其后。而俄罗斯（+158bps）、以色列（+57bps）和巴西（+57bps）的金融条件在收紧。\n\n2️⃣ **利率预测大调整**\n美国：最后两次降息推迟到2027年6月和12月（之前是2026年12月和2027年3月）\n巴西：2026年底利率上调75个基点至14.0%\n匈牙利：2026年底利率下调50个基点至5.25%\n台湾：不再降息，维持2%至2026年底\n韩国：2027年底利率上调25个基点至3.25%\n\n3️⃣ **未来四个季度怎么走？**\n全球央行预计平均降息0.1个百分点至3.1%。但分化明显：\n- 发达市场：平均加息8个基点（新西兰+50bps，欧元区+25bps等）\n\n[... middle omitted ...]\n\n and tightened the most in Russia (158bps), Israel (57bps), and Brazil (57bps).\n\nForecast updates: We have made several policy rate forecast revisions over the last 30 days. In the US, we push\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "NOM：韩国央行转向，通胀让位给房价",
    "digest": "[wechat_article.md]\n# NOM：韩国央行转向，通胀让位给房价\n\n韩国央行的决策天平正在发生一次关键倾斜。过去一年多，市场习惯用“通胀粘性”和“全球紧缩”来理解韩国货币政策的方向。但NOM最新发布的研报揭示了一个更微妙的转折：通胀风险已经明显消退，真正主导韩国央行政策节奏的，变成了首尔公寓价格的持续攀升。\n\n这不是一个短期的噪音扰动，而是政策逻辑框架的系统性切换。理解这一变化，对于判断韩国资产定价、韩元汇率走向乃至整个亚洲利率周期的节奏，都至关重要。\n\nNOM维持其加息路径预测——7月、10月和明年1月各加息25个基点，终端利率达到3.25%。但报告的真正价值不在于这个数字本身，而在于它点出了支撑这个路径的“支柱”已经更换：从对抗通胀，转向防范金融稳定风险。\n\n**KC评论：** 很多投资者习惯把韩国央行的加息决策简化为“通胀数据+美联储动作”的函数。NOM的报告提醒我们，在通胀压力已经大幅缓解的背景下，韩国央行可能正在进入一个更复杂的决策阶段——房价和家庭债务的“金融稳定”权重正在上升。这意味着，即使未来CPI数据出现低于预期的读数，也不一定意味着加息节奏会放缓。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源溢价消退，通胀不再是加息的急迫理由\n\nNOM报告中最清晰的一个信号是：通胀风险正在快速消散。布伦特原油价格在美国-伊朗停火协议后，已经回撤至接近冲突前的水平，这几乎完全抹去了韩国央行在2026年下半年通胀展望中嵌入的能源溢价。\n\n韩国央行此前的预测是基于布伦特原油均价约95美元/桶的假设。油价的实际回落意味着，7月货币政策会议时，通胀预测面临的下行风险正在累积。除非油价出现戏剧性的逆转，否则支撑此前“连续加息”策略的通胀支柱已经显著弱化。\n\n这一判断直接指向一个结论：韩国央行没有理由再维持“鹰派急行军”式的加息节奏。通胀不\n\n[... middle omitted ...]\n\n态。欢迎在社群微信群里继续讨论，获取当日最新的数据图表合集。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国央行：通胀降温，但房价才是真问题\n\n首尔房价年化涨15.8% 📈\n\n涨速连续8周双位数，比通胀更让央行头疼\n\n---\n\n1️⃣ 通胀压力其实在退潮\n布伦特原油已回落至冲突前水平，此前韩国央行上半年预测油价95美元/桶，现在这个假设已明显偏乐观。\n除非油价突然暴涨，否则靠通胀支撑连续加息的逻辑已经弱了很多。\n\n2️⃣ 房价才是真正的“政策舵手”\n6月最后一周，首尔公寓价格年化涨幅达15.8%，且连续8周保持双位数增长。\n这种涨速已经不是短期波动，而是系统性金融稳定风险。\n韩国央行现在最关心的，已经从“物价涨多少”变成了“房价压不压得住”。\n\n3️⃣ 加息节奏会变，但方向不变\n研报预计7月、10月、明年1月各加25bp，终点利率3.25%。\n但重点变了：之前是抗通胀，现在是为金融稳定踩刹车。\n所以7月大概率加，之后节奏会放缓——要同时照顾房价风险、通胀回落、内需缓慢修复这三件事。\n\n📌 一个观察\n当房价涨速超过通胀，央行的决策逻辑就变了。\n不是不收紧，而是收紧的理由换了。\n\n#学习笔记\n\n[source_mineru.md]\nEconomics - Asia ex-Japan\n\n# Korea: Housin\n\n[... middle omitted ...]\n\nthe energy premium embedded in the BOK's H2 2026 inflation outlook. The BOK's latest projections were conditioned on Brent averaging around USD95/bbl, leaving the July MPC meeting with a growi\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R008",
    "title": "NOM：美国就业只是“喘口气”，市场别急着定价降息",
    "digest": "[wechat_article.md]\n# NOM：美国就业只是“喘口气”，市场别急着定价降息\n\n市场正在等待一份数据，来判断美国经济的下一个方向。这份NOM研报给出的判断是：6月非农就业新增可能只有7万人，比5月大幅回落，但这不是衰退信号，而是临时性因素的消退。\n\n对于习惯了“就业好=加息、就业差=降息”的简化逻辑的投资者来说，这个判断意味着一个关键转折：劳动力市场正在从“过热”回归“韧性”，而美联储最关心的通胀压力并未解除。市场如果因此加速定价降息，可能会失望。\n\n报告的核心主张清晰且克制：就业数据存在噪音，但政策利率在2027年底前都不会调整。这背后是一个更值得关注的权力结构变化——白宫正在从“施压降息”转向“中立旁观”，而美联储内部鹰派仍然占据话语权。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 6月非农的“7万”不是坏消息，而是噪音回归均值\n\nNOM预计6月非农新增就业降至7万人，显著低于5月的读数。但这并不意味着劳动力市场突然恶化。报告明确指出，5月的数据受到了世界杯相关酒店休闲业招聘、地方政府教育岗位季节性异常等临时因素的推高。这些因素在6月自然消退。\n\n更值得关注的不是单月波动，而是综合指标：ADP就业数据虽然从峰值回落，但仍指向私营部门稳健增长；初次申请失业金人数维持在低位；裁员率持续低迷。这些信号共同指向一个结论：劳动力市场不是“走弱”，而是从“异常强劲”回归到“韧性增长”的轨道。\n\n> **KC评论：** 市场容易对单月非农做出过度反应。NOM的框架提醒我们，把数据拆解为“趋势项”和“噪音项”才是专业做法。完整报告中包含对休闲酒店业和政府就业的细分拆解图，这些图表能帮你判断哪些行业在真正降温，哪些只是季节性回摆。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 薪资增速放缓才是美联储真\n\n[... middle omitted ...]\n\n新数据图表合集，既方便喂给AI，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国6月非农要降温？投行提前划重点\n\n📊 非农数据前瞻\n\n6月非农新增就业预计放缓至7万人，低于近几个月均值。5月数据受临时因素推高，这部分增量大概率会回吐。但整体看，劳动力市场依然有韧性，美联储短期内不会因为就业转弱就放松对通胀的关注。\n\n1️⃣ 哪些行业在降温？\n- 休闲酒店业：世界杯相关招聘和季节性因素消退，5月的高增长不可持续\n- 地方政府就业：5月创下2024年7月以来最强月增，6月大概率回落\n- ADP周度数据从高点放缓，但仍在扩张区间\n\n2️⃣ 工资通胀压力减弱\n- 时薪环比增速预计放缓至0.2%\n- 亚特兰大联储工资跟踪指标、ADP薪资数据都在缓慢下行\n- 这有助于抑制对工资敏感的核心服务通胀\n\n3️⃣ 失业率可能微升\n- 预计6月失业率4.3%（四舍五入后持平）\n- 裁员率近期保持低位，劳动力需求在2025年下行后趋于稳定\n\n💡 美联储怎么看？\n- 主席Warsh在辛特拉论坛预计不会释放新信号，重点看他如何描述中东局势和油价下跌\n- 若将油价下跌视为通胀积极信号，偏鸽；若强调核心通胀粘性，偏鹰\n- 纽约联储Williams偏鸽，认为当前政策足以让通胀回到2%\n- 鹰派Goolsbee表示“一\n\n[... middle omitted ...]\n\nins resilient. Real personal spending growth accelerated in May, despite Iran war-related uncertainty, while the durable goods report points to broad based business investment.\n\n## Research An\n\n[... middle omitted ...]\n\ns available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities International, Inc., US. All rights reserved."
  },
  {
    "id": "R009",
    "title": "GS：MLCC的五月数据不是疲软，是黄金周",
    "digest": "[wechat_article.md]\n# GS：MLCC的五月数据不是疲软，是黄金周\n\n日本财务省6月26日发布的5月MLCC贸易数据，表面上看并不好看。出口量环比下降10%，出口额环比下降12%，平均出口单价环比下降3%。如果只看环比，一个典型的“量价齐跌”画面似乎已经浮现。\n\n但GS在第一时间给出的判断是：这不是趋势反转，而是季节性噪音。5月日本黄金周长假对出货节奏的影响，掩盖了MLCC市场真实的景气度。\n\n这份报告的真正价值，不在于它对5月数据的解释，而在于它给出了一个更重要的判断框架：对于MLCC这类被动元件的景气判断，环比数据的意义远不如同比数据，而同比数据又不如订单趋势和产品组合的结构性变化。投资者如果把注意力放在月度贸易数据的短期波动上，反而可能错过真正决定企业价值的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 环比疲软是季节性噪音，同比高增长才是真实信号\n\n5月MLCC出口量的环比下降，GS明确归因于黄金周长假带来的出货天数减少。这是一个合理的解释。日本制造业的出货节奏在5月受到假期扰动，是每年都会发生的季节性现象。\n\n同比数据更能说明问题。出口量同比上升7%，出口额同比上升19%。在去年同期基数并不低的背景下，这样的同比增速意味着下游需求依然强劲。更值得注意的是，出口额增速（19%）显著高于出口量增速（7%），这指向一个关键判断：产品结构在向高价值方向迁移。\n\n> **KC评论：** 很多投资者看MLCC数据时习惯性关注环比，但环比数据受假期、月末出货节奏、船期等短期因素影响极大。GS这里提供了一个更有效的观察框架：同比数据过滤季节性噪音，而“出口额增速与出口量增速的差值”才是判断产品结构升级的核心指标。完整报告中，GS对历史数据的同比趋势做了更系统的拆解，值得仔细看。\n\n![研报原图 2](assets/source_im\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC五月数据怎么看？全年逻辑更关键\n\n📊 核心干货\n\n五月MLCC出口数据出炉，环比受假期影响下滑，但同比依然坚挺。出口金额同比+19%，均价+11%，量+7%。\n\n1️⃣ 为什么环比下滑不用慌？\n五月日本黄金周，工厂出货节奏受影响，环比下滑是正常季节性。更值得关注的是同比增速还在高位，说明需求端没熄火。\n\n2️⃣ AI和汽车是两条主线\n某外资投行与村田确认：AI/数据中心订单非常强劲，汽车领域的复苏感也在增强。MLCC不仅是手机零件，AI服务器对高端MLCC的需求正在拉动产品结构升级。\n\n3️⃣ 真正的看点在下半年\n相比一季报本身，市场更关注4-6月的订单出货比、7-9月展望，以及下半年产品组合的改善。AI服务器用的MLCC单价更高，会显著拉高ASP。\n\n4️⃣ 涨价预期的时间窗口\n同口径产品涨价讨论，关键节点在年底前后（2027年展望出现时），一季报季节不是重点。\n\n研报维持对村田、太阳诱电、TDK的积极看法。\n\n欢迎一起讨论MLCC产业链的机会与风险～\n\n#学习笔记\n\n[source_mineru.md]\n# Japan Technology: Hardware - Electronic Compo\n\n[... middle omitted ...]\n\nthat despite the seasonality in May due to the Golden Week holiday, order trends are at a very high level. The company commented that very strong orders for AI/DC applications are continuing, \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R010",
    "title": "GS资金流向警报：科技股开始失血，但这不是撤退信号",
    "digest": "[wechat_article.md]\n# GS资金流向警报：科技股开始失血，但这不是撤退信号\n\n过去几周还在疯狂涌入科技板块的资金，突然踩了刹车。GS最新一期全球资金流向周报显示，截至6月24日当周，全球科技股基金遭遇了238亿美元的净流出，与此前一周383亿美元净流入形成剧烈反转。这是这份报告里最值得关注的单一信号。\n\n但如果你据此判断市场风向已经彻底转向，可能就错过了报告里更重要的信息。同一周，全球固定收益基金净流入164亿美元，新兴市场债券基金净流入32亿美元，跨境外汇资金整体保持正值。资金并未逃离风险资产，只是在重新定价路径。\n\n这份周报的核心判断是：科技股的阶段性获利了结是真实的，但它更像是一次仓位调整，而非趋势逆转。真正值得关注的，是资金在区域、资产类别和期限结构上的结构性迁移——这些迁移正在告诉我们下一阶段的市场逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 科技股单周净流出238亿美元，但此前四周累计净流入近350亿美元\n\nGS的数据显示，在截至6月24日的一周内，科技板块基金净流出规模居所有行业之首，达到238亿美元。这一数字远超同期工业、能源、金融等板块的流出规模。与此形成对比的是，医疗保健、基础设施、房地产等低贝塔板块仍录得净流入。\n\n但解读这一数据需要放在更长的时间维度中。此前四周，科技股基金累计净流入约350亿美元，Z-score高达2.75，属于统计上的极端值。单周的流出更像是连续超买后的正常修正，而非系统性撤退。\n\n> **KC评论：** GS这张行业资金流向图最值得细看的是“4周累计”和“单周”的对比。科技股单周流出238亿，但4周累计仍有350亿净流入。这意味着什么？追高的资金在撤退，但长期配置的资金还没走完。完整报告里还有按国家拆分的科技股资金流向数据，能帮你判断这一轮流出是全面性的还是区域性的。\n\n![研报\n\n[... middle omitted ...]\n\n工快速把握全球市场的资金动态。欢迎来星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n科技资金大撤退，债市还在买\n\n资金转向了\n\n全球资金流向出现明显切换\n\n1️⃣ 股票资金由流入转流出\n截至6月24日当周，全球股票基金净流出约50亿美元，而前一周还是净流入1260亿。发达市场中，美国和欧洲是主要流出地区。\n\n2️⃣ 科技板块遭遇最大赎回\n连续几周强劲流入后，科技基金上周出现最大规模净流出（约238亿美元）。工业、基础设施和房地产板块仍有资金流入。\n\n3️⃣ 债市继续吸金\n全球固定收益基金净流入约164亿美元，短久期债券和通胀保护债券持续受欢迎。新兴市场债券也保持净流入。\n\n4️⃣ 外汇流向：美元、欧元、日元需求最强\n人民币在连续几周净流出后，本周转为净流入。整体跨境资金流向偏正面。\n\n投行研报认为，虽然科技板块波动加剧，但AI投资热潮仍在，这可能会继续支撑美元相对强势。\n\n欢迎一起讨论这轮资金切换背后的逻辑🧐\n\n#学习笔记\n\n[source_mineru.md]\n# WEEKLY FUND FLOWS Tech Turbulence\n\n## Global fund flows, week ending June 24\n\n■ Flows into mutual funds and relate\n\n[... middle omitted ...]\n\nal weeks of strong inflows, technology funds saw the largest net outflows (see chart of the week). We recently noted that the Dollar's resilience though software sell-off in February and tech-\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "HSBC：集装箱航运的景气周期比市场想的更长",
    "digest": "[wechat_article.md]\n# HSBC：集装箱航运的景气周期比市场想的更长\n\n当市场还在为集装箱航运的短期繁荣是否会戛然而止而争论时，HSBC与Linerlytica在6月25日的联合研讨会上给出了一个反共识的判断：这轮上行周期的驱动力不是关税前抢运，而是科技驱动的结构性需求。运价不仅没有见顶，还在6月下旬继续攀升。这意味着，行业EBIT利润率将从一季度的约5%跳升至二季度的约10%，三季度还有进一步上行的空间。\n\n对于长期被贴上“周期性过山车”标签的集装箱航运来说，这个判断的分量不亚于一次行业认知的重塑。如果需求真的是结构性的，那么当前估值中隐含的“景气很快消退”的假设，就需要被重新审视。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 运价还在涨，而且涨得比市场预期的更久\n\nHSBC的这份研报最直接的信号是：运价没有在传统旺季前掉头向下。截至6月下旬，美西航线现货运价维持在约每40英尺集装箱6000美元，美东航线在7000至8000美元区间。更重要的是，船公司还在推动7月新一轮涨价。租船费率维持高位，且租船与运费的价差正在收窄——这是运价上涨动能尚未衰竭的典型信号。\n\n市场此前普遍预期，随着中国出口数据走弱，运价会在短暂冲高后回落。但HSBC的结论恰恰相反：有效运力紧张叠加需求改善，市场至少会坚挺到8月，甚至可能延续到9月。这意味着二季度和三季度的盈利弹性可能被严重低估。\n\n> **KC评论：** 这里的关键不是运价绝对水平，而是运价上涨的持续性。如果市场预期的是“脉冲式冲高后回落”，那么当前股价可能只反映了短暂的盈利脉冲。但如果运价能维持到三季度末，整个年度的盈利预测都需要上修。完整报告里对运价分航线的逐月走势图，值得仔细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 需求不是抢跑，是\n\n[... middle omitted ...]\n\n化。欢迎来知识星球或微信群里继续讨论，一起拆解这些未解之问。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球航运周期比想象中更持久\n\n🧭 航运周期还没走完\n\n某外资投行刚开了航运专家会，结论很直接：2-3季度利润率大概率继续走高，不是短期脉冲。\n\n1️⃣ 运力紧、需求强，不是“抢运”\n传统出口品类（服装-1.6%、鞋类-10.3%）其实偏弱。真正拉动的，是AI数据中心、清洁能源（电池/光伏/电动车）这些结构性需求。\n\n2️⃣ 运价还在涨\n到美西约6000美元/40尺箱，美东7000-8000美元。承运商7月还在推涨。非洲航线+50%、拉美+12%，北美反而偏慢。\n\n3️⃣ 关税影响有限\n之前的关税到期后，新方案类似，7-8月货量预计不会崩。\n\n4️⃣ 关键风险：红海恢复\n如果红海通航，约6%运力会释放，可能冲击运价。但目前港口拥堵还在，短期支撑力仍在。\n\n5️⃣ 利润弹性正在释放\n燃油比冲突前贵30%，但成本控制好。CCFI运价指数同比+40-42%，行业EBIT利润率有望从1季度的约5%提升到2季度的约10%。\n\n6️⃣ 2027-28年才是“大考验”\n新船交付高峰在2028年，供给增速可能超14%。拆船能力有限，届时供需格局可能逆转。\n\n📌 现在市场在交易的是“这轮比想象中长”，但真正要盯的，是红海何时恢复\n\n[... middle omitted ...]\n\nsted Linerlytica to discuss the outlook for container shipping. We discuss key takeaways below. Reach out here to request the replay and slides.\n\n1) Upcycle looks stronger (and longer): Tight \n\n[... middle omitted ...]\n\n69c10f305d487cac398b8.jpg)\n\n## Newsletters\n\nSubscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points"
  },
  {
    "id": "R012",
    "title": "摩根斯坦利：MS：地产股跌回历史最低估值，但这不是抄底信号",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：地产股跌回历史最低估值，但这不是抄底信号\n\n地产板块跌回去了。不是跌回起点，是跌到比起点更低的位置。\n\n自五月中旬以来，中国开发商股票整体回撤超过30%，同期恒生指数仅下跌13%。MS在最新发布的中国地产行业报告中承认，这一轮下跌的幅度“超出了他们此前的预期”——即便他们原本就对行业持谨慎态度。\n\n现在，整个板块的市净率已经回落至0.30倍，处于历史最低区间。对于信奉价值投资的资金来说，这个数字看起来很有诱惑力。但MS的判断是：低估值不等于底部，更不等于买点。\n\n核心问题在于：市场在交易什么？交易的是“还能不能更差”，而不是“什么时候变好”。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮下跌的驱动力不是基本面本身，而是资金流向的系统性转移\n\nMS将本轮地产股下跌归因为两个因素的叠加：销售端快速冷却，以及资金向AI相关板块的大规模转移。\n\n销售端的冷却并不意外。三至五月期间，市场曾出现一波短暂的销售反弹和房价跌幅收窄，这在当时引发了一些“触底”讨论。但进入六月后，高频数据显示动能正在迅速消退。MS预计，三季度主要城市的二手住宅成交同比可能转负，新房价格环比跌幅将较二季度有所扩大。\n\n更值得关注的是资金流向的结构性变化。AI主题在五月中旬之后持续升温，吸引了大量原本可能配置在地产板块的资金。这不是一个短期现象。当市场的主线叙事从“复苏”切换为“技术革命”，地产这种需要漫长等待基本面验证的板块，在资金争夺中天然处于劣势。\n\n> **KC评论：** 资金流向的转移意味着，即使地产股的基本面没有进一步恶化，股价也可能持续承压。因为估值不仅仅是利润的函数，也是资金供给的函数。完整报告中对资金流向的量化分析值得细读，它会帮助你判断这个“挤出效应”到底有多大。\n\n---\n\n![研报原图 2]\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n地产板块跌超30%，到底了吗？\n\n**地产板块，还能不能看？**\n\n最近地产板块跌得有点猛，5月中旬以来跌幅超30%，跑输恒指不少。某外资投行刚出的研报，核心逻辑很清楚，我帮你拆开看。\n\n1️⃣ **短期没催化剂，别急着冲**\n- 虽然估值回到历史低位（市净率0.3倍），但销售还在降温，三季度房价可能跌得更快。7月政治局会议大概率不会有增量政策，因为3-5月数据还行。\n- 研报判断：短期没有反弹动力，资金还在往AI板块跑。\n\n2️⃣ **选股要挑“能自己造血”的**\n- 不是所有地产股都悲观。研报重点看好那些有“自下而上alpha”的公司，比如购物中心租金收入稳健的房企，在当前估值下性价比更高。\n- 具体提了三家：华润置地（首选）、建发国际、新城控股，认为它们即便市场不回暖，EPS也有支撑，中期有重估空间。\n\n3️⃣ **避雷：哪些不能碰？**\n- 研报明确看空金地集团和万科，理由是土地储备枯竭，未来增长动力不足。\n\n4️⃣ **两个短期风险要留意**\n- 三季度二手房成交可能同比转负。\n- 多数房企上半年业绩会下滑或亏损（7月中旬开始发预告），这是近期最大的压力点。\n\n**我的看法**：研报判断偏谨慎，认为\n\n[... middle omitted ...]\n\nCurrent record-low P/Bs may suit value investment, but sales/earnings headwinds and limited policy upside may put further near-term pressure on the stocks.\n\nWe reiterate our cautious view on \n\n[... middle omitted ...]\n\nty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$3.40</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R013",
    "title": "HSBC：猪周期底部的核心信号不是价格反弹，而是谁在被迫退出",
    "digest": "[wechat_article.md]\n# HSBC：猪周期底部的核心信号不是价格反弹，而是谁在被迫退出\n\n这一轮猪周期的深度与长度，已经超出了多数市场参与者的预期。2026年4月，全国生猪均价跌至每公斤9元，创下2014年以来的绝对低点。自2025年9月至今，自繁自养模式已连续亏损超过9个月，平均每头亏损超过215元。这是2014年以来亏损幅度第二深、严重亏损持续时间第二长的下行周期。\n\n但HSBC近期发布的这份研报，并没有停留在“市场很惨”的描述上。它的核心判断是：产能去化的路径已经清晰，供给收缩将从2026年第四季度开始兑现，届时猪价将迎来温和复苏。更重要的是，这份报告通过拆解“2025年5月多养一万头母猪究竟会亏多少钱”，揭示了一个反直觉的结论——这轮周期底部的真正信号，不是猪价何时反弹，而是谁在被亏损逼退、退出的速度有多快。\n\n对于投资者而言，当前需要回答的问题不是“猪价见底了吗”，而是“产能出清的结构是否已经完成”。HSBC的答案指向2026年第二季度末，而估值层面，牧原、温氏等龙头已回到周期底部中枢，市场对它们盈利能力的定价可能过度悲观。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2025年5月逆势扩产的教训：多养一万头母猪可能亏掉5000万\n\n理解当前产能过剩的根源，需要回到2025年5月。当时，农业农村部多次召集大型养殖企业开会，要求控制或缩减能繁母猪存栏。龙头公司确实执行了——仅牧原一家，从2025年6月到9月，能繁母猪存栏就减少了12万头，超过同期全国降幅。\n\n但非集团养殖户（中小散户）并未听从政策指引，反而在猪价预期改善的刺激下继续扩产。HSBC的研报用一个非常具体的测算，展示了这一决策的财务后果。\n\n以2025年5月购买1万头淘汰母猪作为种猪为例：淘汰母猪平均体重180公斤以上，按当时每公斤11.7元的价格计算，仅购买成本\n\n[... middle omitted ...]\n\n工快速把握市场动态。欢迎来我们的微信群继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n猪周期拐点，最快4季度\n\n猪价见底了？\n\n9元/公斤是底部吗\n\n最近看了一份某外资投行的生猪研报，逻辑很清晰，信息量也大，整理一下核心判断。\n\n1️⃣ 这轮亏损有多惨？\n- 自繁自养头均亏损超300元，已经亏了9个月\n- 这是2014年以来第二深的亏损周期（仅次于2021年）\n- 4月猪价跌到9元/公斤，创2014年以来新低\n- 但猪肉已经是所有肉里最便宜的，冷库库存创三年新高，需求其实不弱\n\n2️⃣ 为什么这么惨？\n- 问题出在供给端，不是需求\n- 2025年5月农业部要求大厂减能繁，大厂听话了\n- 但散户逆势扩产，导致2026上半年供给过剩\n- 研报算了一笔账：2025年5月多养1万头母猪，到2026年3月卖肥猪，额外亏损约2300万\n\n3️⃣ 产能出清到哪一步了？\n- 能繁存栏同比已降3.3%，目标3750万头\n- 大厂已按政策减到位，散户被亏损逼着减\n- 如果7kg仔猪跌破200元/头，专业育肥场也会加速退出\n- 效率提升会部分抵消减量，但预计4季度起生猪供给同比转负\n\n4️⃣ 拐点什么时候来？\n- 基准判断：4季度猪价温和回升，不是暴涨\n- 冷库库存高会缓冲涨幅，需要活猪和冻品库存一起消化\n- 20\n\n[... middle omitted ...]\n\nexceed RMB300/head, with over-RMB200/head losses persisting for over three months, making this the second-worst loss amplitude and the second-longest severe-loss episode on record. Despite por\n\n[... middle omitted ...]\n\nproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited."
  },
  {
    "id": "R014",
    "title": "JPM：数据中心“后院起火”，反而催生了亚太能源转型的新主线",
    "digest": "[wechat_article.md]\n# JPM：数据中心“后院起火”，反而催生了亚太能源转型的新主线\n\n当美国社会对AI数据中心的抵制从社区抗议升级为联邦监管改革，一场关于“谁为电力基础设施买单”的博弈正在改写全球能源转型的投资逻辑。JPM最新发布的亚太能源转型研报指出，FERC（美国联邦能源监管委员会）近期提出的电网并网改革，核心并非仅仅为了加速数据中心供电，更关键的是防止普通居民为数据中心的扩张“交叉补贴”。这一变化，正在将“表后（BTM）发电”从一种备选方案推向前所未有的战略高地。\n\n对于亚太的投资者而言，这意味着能源转型的价值链正在经历一次深刻的“需求重构”。报告明确点出，亚太储能系统（ESS）、电气与发电设备以及核电SMR三大主题将直接受益。但这不仅仅是技术清单的更迭，而是一场关于“社会许可”如何决定技术路径的预演。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 社会反弹是表层的，成本传导的“政治风险”才是真正的监管变量\n\n市场此前对FERC改革的关注点大多集中在“如何让数据中心的电更快接上”。但JPM这份报告揭示了一个更微妙的维度：改革文件中与“加速”并列的五大领域之一，是“成本透明度和防止成本向普通用户转移”。这意味着，监管机构正在认真对待一个尖锐的社会问题——AI发展的巨额电力投资，是否应该由不享受其红利的家庭用户来买单。\n\n这并非杞人忧天。PJM市场的容量拍卖价格已逼近监管上限，而美国部分地区正讨论保护居民免于为数据中心开发付费的两党法案。当电力成本成为政治议题，数据中心的“社会运营许可证”就变得比技术可行性更关键。因此，任何能够减轻公共电网负担、从而降低居民电费上涨压力的技术方案，都将获得额外的政策倾斜。\n\n> **KC评论：** 很多人看AI电力需求只看“总量”增长，但JPM提醒我们，看“成本分配”更重要。如果监管层强力介入，\n\n[... middle omitted ...]\n\nFERC改革的后续进展及其对亚太供应链的传导效应。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心遇上电网改革，能源转型新逻辑\n\n数据中心 vs 电网，谁买单？\n\nFERC（美国能源监管机构）最近搞了个大动作——针对大型负荷并网发布改革令。核心就两点：一是加速数据中心这类大负荷接入电网，二是防止电费成本转嫁给普通居民。说白了，数据中心扩建带来的电网升级费用，不能让老百姓买单。\n\n这场改革背后，是数据中心开发引发的社会反弹。社区担心电价上涨、噪音扰民，监管层不得不出手。\n\n1️⃣ 自备电源（BTM）成关键变量\n\n改革令特别提到要支持“表后发电”技术（BTM），就是数据中心自己建发电设施。这既能解决并网排队慢的问题（美国部分地区排队要等3-5年），又能减轻公共电网负担，减少社会争议。\n\n研报观点：BTM可能从“速度优势”变成“长期趋势”。目前美国两党正在讨论一项法案，保护居民不为数据中心扩建买单。\n\n2️⃣ 亚太能源转型链的受益方向\n\n按投行研报分析，亚太能源转型链中三个主题最相关：\n- 储能系统（ESS）\n- 电气与发电设备\n- 小型模块化核反应堆（SMR，偏中长期）\n\n具体到公司层面，研报提到的超配标的包括：斗山能源、潍柴动力（A/H）、应流股份、晓星重工、阳光电源、宁德时代、LG新能源。\n\n3️\n\n[... middle omitted ...]\n\nide our US team's (Mark Strouse's report) callout on BTM (behind the meter) technology and transmission from the FERC reform, we highlight the importance of BTM's role in obtaining social acce\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R015",
    "title": "GS：美国风电订单正在加速，但市场低估了利润上修的幅度",
    "digest": "[wechat_article.md]\n# GS：美国风电订单正在加速，但市场低估了利润上修的幅度\n\n当市场还在争论特朗普关税政策对清洁能源的冲击时，一份来自GS的研报揭示了一个反直觉的信号：欧洲风电制造商正在美国获得大量订单，且是在政策尚未完全明确的前提下。\n\nVestas 在昨晚宣布，其在美国获得了总计 869 兆瓦的陆上风电订单。这并非孤例。根据GS统计，Vestas 在 2026 年第二季度已从美国获得 1.5 吉瓦的订单，过去四个季度的滚动订单量达到 5.2 吉瓦。Nordex 同样不甘示弱，在 2025 年下半年获得 1.1 吉瓦有条件订单的基础上，又新增了三个总规模达 0.5 吉瓦的确定订单。\n\n这份报告的核心判断是：美国风电订单的持续恢复，正在为 Vestas 和 Nordex 的盈利前景提供超出当前预期的上行风险。GS对两家公司均维持“买入”评级，Vestas 目标价 236 丹麦克朗，Nordex 目标价 53.2 欧元。\n\n但真正值得追问的是：为什么在政策不确定性笼罩下，订单反而在加速？这背后隐藏着怎样的结构性变化？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国风电市场正在经历一场“无声的修复”，而非衰退\n\n市场对特朗普政府可能对进口风电设备加征 232 条款关税的担忧并非没有道理。但现实是，订单数据正在讲述一个不同的故事。\n\nVestas 在美国的订单积压正在以肉眼可见的速度增长。Nordex 也在积极重返美国市场，其目标是恢复到约 20% 的美国市场份额。GS的研究显示，Nordex 在过去 12 个月中已经看到了订单回升的迹象，这为其实现市场份额目标提供了支撑。\n\n为什么开发商愿意在政策前景不明朗的情况下下订单？答案可能在于：市场已经将关税风险纳入了定价，而当前的 PPA（购电协议）价格已经足够高，足以消化潜在的关税成\n\n[... middle omitted ...]\n\n业决策者和专业投资者一起，持续跟踪这些关键判断的验证与修正。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧美风电订单回暖，利润有向上空间\n\n美国订单持续回暖\n\n欧洲风电巨头Vestas和Nordex近期在美国市场收获超预期订单📈\nVestas昨晚宣布获得869MW美国陆上风电订单\nQ2至今累计1.5GW，近4个季度共5.2GW\nNordex也拿到0.5GW确订单，加上H2的1.1GW条件订单\n目标重回20%美国市场份额\n\nPPA价格翻倍带来利润弹性💡\n美国风电PPA价格从2020-21年的$30/MWh涨到$70+\n电力需求上升+竞争减少+设备成本增加\n三重因素推高项目回报率\n研报认为美国订单是利润预测的上行风险\n\n两家公司怎么看？\n\n1️⃣ Vestas（目标价Dkr236）\n- 风电制造商里位置最好的一家\n- 地理多元+规模效应=强基本面\n- 预计FY27实现90%中期目标\n- 未来5年累计回购€50亿\n- 美国+德国订单回暖是催化剂\n\n2️⃣ Nordex（目标价€53.2）\n- 同样受益行业回暖\n- 定价改善+订单增长→利润率修复\n- 现金回报预期提升\n- 可用于分红、回购、再投资\n\n核心逻辑：政策不确定性下订单仍在增长，说明基本面够硬。PPA价格翻倍后，项目利润空间明显改善。\n\n#学习笔记\n\n[sou\n\n[... middle omitted ...]\n\naims to return to its previous US market share which was c.20%.\n\nExhibit 1: Nordex had started to see a pick-up in orders over the last 12 months, helping to reach its US market share ambition\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "NOM：中国信用评级体系已无法反映企业真实风险",
    "digest": "[wechat_article.md]\n# NOM：中国信用评级体系已无法反映企业真实风险\n\n当超过一半的债券发行人手握AAA或AA+评级，而同时近四分之一工业企业处于亏损状态，这两个数字放在一起，指向的不是技术性偏差，而是整个评级信号系统的失灵。\n\nNOM亚洲经济团队在最新一份研报中提出了一个直指中国债券市场核心机制的问题：国内评级体系正在被日益上升的亏损企业比例所挑战。报告援引数据指出，截至2026年第一季度，59%的发行人被评为AAA或AA+，非金融企业债务融资工具中这一比例甚至高达74.6%。与此同时，国家统计局数据显示，2025年亏损工业企业占比升至23.8%，为2000年以来最高；2026年前四个月这一比例进一步攀升至32.4%。\n\n评级膨胀与财务恶化之间的背离，已经不是技术细节，而是一个系统性的风险信号。它意味着投资者和监管机构正在被一套无法有效区分信用质量的标签所引导。\n\n> **KC评论：** 这份报告的核心判断不是“企业很烂”或“评级很水”这种泛泛之谈。它的价值在于把两个趋势放在一起看：评级分布越来越集中在上游，而企业基本面越来越下沉。这种背离对债券定价、投资组合风险管理、甚至货币政策传导都有直接含义。完整报告中有更多关于不同行业亏损分布和评级迁移率的数据，值得细读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 评级膨胀的规模已经超出技术性偏差，接近系统失灵\n\nNOM报告引用的数据揭示了一个令人不安的结构性特征。在发达债券市场，即使是信用质量较高的企业群体，AAA评级也是稀缺资源。但在中国，这一评级已成为“标配”。当大部分发行人都拿到同一档评级时，评级的区分度和信息含量就趋近于零。\n\n这种膨胀并非一日之功。报告追踪显示，非金融企业AAA/AA+评级债务融资工具的占比在过去几年持续攀升，目前已接近四分之三。而同期，企业的盈利状况却在\n\n[... middle omitted ...]\n\nrket dynamics。欢迎来我们的星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n59%都是AAA/AA+，这评级还准吗？\n\n信用评级失真\n\n亏损企业占比创25年新高\n\n---\n\n最近看了一份外资投行的研报，讲中国信用评级体系的问题，信息量很大，分享几个关键发现👇\n\n**1/ 评级通胀有多夸张？**\n今年一季度，有59%的发债主体评级是AAA/AA+。对比国际机构，即使在成熟市场，这种顶级评级占比也远低于这个数。更夸张的是，非金融企业的高评级融资工具占比已升至74.6%。\n\n**2/ 评级和基本面严重脱钩**\n一边是评级虚高，另一边企业盈利状况却在恶化。2025年规模以上工业亏损企业占比达到23.8%，是2000年以来最高。今年前四个月进一步攀升到32.4%，比去年同期还高。评级体系几乎没有反映这种变化。\n\n**3/ 为什么现在问题凸显？**\n地产行业下行持续拖累经济，企业和家庭的信用风险都在上升。在这种脆弱环境下，一个失真的评级系统，可能会隐藏真实的违约风险，对市场和监管都形成误导。\n\n**4/ 监管已关注到问题**\n据彭博报道，央行等监管机构已要求国内评级机构改革系统，更准确地反映信用风险。研报认为，评级体系确实需要一次彻底调整。\n\n评级失真不是小事，它影响的是整个市场的定价效率。当大\n\n[... middle omitted ...]\n\nc rating agencies revamp their rating systems to more accurately reflect the credits risks of local firms. In Q1 2026, a striking $59\\%$ of issuers were rated as AAA/AA+, while major internati\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R017",
    "title": "DB：中国光伏装机跌至四年最低，但真正的机会在电力运营商",
    "digest": "[wechat_article.md]\n# DB：中国光伏装机跌至四年最低，但真正的机会在电力运营商\n\n2026年5月，中国新增光伏装机8.7GW，同比暴跌91%。这个数字如果只看同比，很容易被归因为去年抢装潮的高基数效应。但DB最新研报做了一个更关键的对比：剔除2025年5月的异常高基数后，2026年前五个月的累计装机仍比2024年同期低25%，比2023年同期低3%。这意味着，中国光伏行业正在经历的不是一次短期波动，而是实质性装机增速失速——五年来的最低水平。\n\n这份报告同时释放了两个看似矛盾但实则高度相关的信号：光伏供给端尚未见底，但需求端可能因异常高温而迎来结构性支撑。真正值得关注的，不是光伏制造商的困境何时反转，而是电力运营商在电价承压、资产分拆、派息提升三重逻辑下的价值重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光伏产业链最痛苦的阶段可能还在7-8月，而非已经过去\n\nDB报告指出，多晶硅价格已跌至每公斤33元人民币，逼近其预估的每公斤30元左右的底部区间。但短期内产出仍在增加，这意味着整个光伏价值链在7-8月将继续承压，任何有意义的复苏都要等到2026年四季度季节性需求改善，或看到切实可行的政策落地。\n\n> **KC评论：** 市场常常把“接近底部”误解为“即将反弹”。实际上，价格逼近成本线不等于产能出清。只有当行业亏损持续足够长、足够深，迫使高成本产能真正退出，供需平衡才能重建。DB认为这个拐点不会在第三季度到来。\n\n这份报告对通威股份的判断尤为尖锐。DB维持卖出评级，目标价从13元下调至10元，预计2026-2027年净亏损将比此前预测扩大10%，2028年每股收益下调25%。核心逻辑是多晶硅和电池片的平均售价假设进一步走低。通威股价年初至今已下跌约40%，跑输沪深300指数48%，跑输光伏同行22%。但DB明确表示，尚未看到\n\n[... middle omitted ...]\n\n迎来知识星球和微信群里继续讨论，一起把这些问题拆解得更清楚。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光伏装机创四年新低，夏天用电会紧张吗？\n\n**光伏降温，用电升温**\n\n5月光伏装机仅8.7GW，同比暴跌91%，创四年新低。剔除去年抢装影响，今年前5月累计装机仍比2024年同期低25%。多晶硅价格跌至33元/kg，逼近30元/kg的底部，产业链压力预计持续到三季度。但另一边，5月用电量同比增长6.9%，AI相关用电增速高达45.4%，高温天气可能进一步推高夏季电力需求。\n\n1️⃣ **光伏产业链压力未减**\n- 5月装机数据惨淡，主要因为去年5月抢装导致高基数\n- 更关键的是，前5月累计装机比2023年还低3%，说明需求确实疲软\n- 多晶硅价格持续下跌，产能还在增加，短期看不到拐点\n- 研报预计，光伏产业链压力至少持续到7-8月\n\n2️⃣ **夏季用电需求有支撑**\n- 5月用电量增速从4月的6.0%升至6.9%\n- 工业用电+6.0%，商业用电+9.7%，居民用电+7.5%\n- AI相关用电增速从42.8%升至45.4%，数据中心的电力需求持续强劲\n- 国家气候中心预测7月气温偏高，可能推高制冷用电\n\n3️⃣ **火电和水电表现分化**\n- 5月火电发电量同比仅增2.1%，增速放缓\n- 水电表现亮眼，同\n\n[... middle omitted ...]\n\nnear-term support from tighter energy-efficiency standards across the solar manufacturing value chain have yet to materialize. Industry fundamentals continue to weaken, with polysilicon prices\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R018",
    "title": "GS：中国车市正在重写欧洲豪车利润区的游戏规则",
    "digest": "[wechat_article.md]\n# GS：中国车市正在重写欧洲豪车利润区的游戏规则\n\n中国汽车市场正在发生一场“静默的利润转移”。GS最新发布的2026年5月中国市场月度追踪报告揭示了一个关键趋势：欧洲豪华品牌在中国整体上仍在守住份额，但利润最丰厚的价格带正被中国科技与高端品牌系统性地渗透。这不是一场简单的份额争夺，而是一场利润池的重新分配。\n\n大众集团在主流市场遭遇了所有外资品牌中最剧烈的份额流失，而比亚迪和吉利这些本土巨头的主流品牌也在同步承压。真正值得关注的信号是：中国品牌正在从“以价换量”转向“以产品换定价权”，而这个过程才刚刚开始。\n\n以下是这份报告的核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧洲豪华品牌的“表面稳定”掩盖了利润区的结构性侵蚀\n\nGS数据显示，2026年5月，梅赛德斯奔驰、宝马、奥迪和沃尔沃四个欧洲豪华品牌在中国市场的份额合计变化为-75个基点（一个月同比）和+2个基点（三个月同比）。从三个月维度看，几乎持平。但细节揭示出完全不同的图景。\n\n奔驰和宝马的份额正在加速流失。奔驰一个月同比下滑28个基点，宝马下滑29个基点。奥迪和沃尔沃则相对抗跌，分别微增9个和16个基点。奥迪受益于其新推出的AUDI品牌（与上汽合作）带来的增量销售，沃尔沃则依靠本土开发的XC70插电混动车型的强劲表现。\n\n但更值得关注的是，这些品牌利润最丰厚的价格带正在被中国科技与高端品牌系统性地渗透。GS定义的“中国科技与高端品牌”组合——包括AITO、小鹏、小米、理想、蔚来、仰望、腾势、极氪等——在5月合计增加了329个基点（一个月同比）和279个基点（三个月同比）的市场份额。极氪和小米是领涨者，分别贡献了93个和72个基点的月同比增幅。\n\n> **KC评论：** 这不是“欧洲豪华品牌不行了”的简单叙事。奔驰、宝马、奥迪在中国的利润池\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n德系豪华车，正在被本土品牌抢地盘\n\n中国车市洗牌进行时\n\n最近看到某外资投行一份关于欧洲车企在华表现的研报，信息量很大。简单来说，就是中国本土品牌（尤其是高端线）正在快速蚕食德系豪华车的市场份额。\n\n几个关键点，值得记录：\n\n1️⃣ **德系豪华车，压力山大**\n奔驰和宝马的市占率同比下滑明显（奔驰-28/-11bps，宝马-29/-10bps）。奥迪和沃尔沃相对坚挺，主要靠新品牌（AUDI）和本土化车型（XC70 PHEV）撑着。但整体来看，四大欧洲豪华品牌加起来，份额还是在跌。\n\n2️⃣ **本土高端品牌，精准打击**\n以蔚小理、小米、极氪、问界为代表的“中国科技+高端品牌”阵营，市占率大幅提升（+329/+279bps）。它们的新车（极氪8X、蔚来ES9、小鹏GX、问界M6）直接打入了BBA最赚钱的价格带。\n\n3️⃣ **大众集团，最受伤的外资**\n大众品牌市占率下滑最严重（-156/-159bps），斯柯达退出中国影响不大。而同样主打大众市场的比亚迪和吉利，也在激烈竞争中丢了份额（比亚迪-168/-227bps，吉利-63/-116bps）。\n\n4️⃣ **一个有趣的例外**\n在所有国际品牌中，特斯拉\n\n[... middle omitted ...]\n\n -29/-10bps), while Audi -9/+16bps and Volvo -9/+8bps proved more resilient. Audi was supported by incremental sales from the AUDI brand, and Volvo by the strength of the locally developed XC7\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "GS：日本机器人出口的“假回暖”与结构性分化",
    "digest": "[wechat_article.md]\n# GS：日本机器人出口的“假回暖”与结构性分化\n\n这份来自GS日本机械团队的最新月度贸易数据解读，揭示了一个与市场普遍感知略有温差的核心判断：2026年5月，日本机器人出口总量同比仍在增长，但环比大幅回落，且不同产品、不同区域、不同公司的表现正在急剧分化。市场若只看到“同比+9%”的数字就认为自动化需求已经回暖，可能会错判节奏。\n\n报告基于日本财务省5月贸易数据，将日本机器人出口作为全球自动化投资的风向标——因为日本企业占据全球机器人市场绝大多数份额，且本土生产比率极高。GS团队通过拆解东京/横滨港和门司港的出口数据，分别追踪发那科（Fanuc，给予卖出评级）和安川电机（Yaskawa Electric，给予买入评级）的出货量趋势。这些数据不只是一组数字，它直接指向两个核心问题：AI带动的需求是否足以拉动传统自动化周期？以及，不同公司的订单结构，是否会带来截然不同的股价表现。\n\n> **KC评论：** GS利用日本海关数据来“拆解”发那科和安川电机的出口量，这是一个很聪明的研究技巧。因为这两家公司的主要工厂所在地不同，海关数据可以近似看作它们的出货量。但要注意，这毕竟是估算，不是公司官方披露。完整报告中包含了更详细的区域拆分图表，以及GS对这些数据与公司实际订单之间映射关系的说明，这些细节对于判断数据的可靠性至关重要。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 机器人总量同比仍在增长，但环比动能已明显衰减\n\nGS估算的日本机器人总出口量在5月达到10,828台，同比增长9%。这一数字在同比层面似乎不错，但环比下降了24%。更重要的是，出口金额同比下降8%，平均售价（ASP）同比下降16%。这意味着，量的增长在很大程度上是靠低价产品拉动的，而不是高端需求的全面复苏。\n\n分区域看，对中国出口量同比增长\n\n[... middle omitted ...]\n\n义，欢迎加入我们的微信群，与更多产业决策者和投资者一起交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月机器人出口，中国区还在撑\n\n📊 投研数据快闪\n\n---\n\n5月日本机器人出口数据出炉，全球总量10828台（+9%yoy），但环比下滑24%，市场在降温。\n\n**1/ 中国区：唯一正增长亮点**\n中国出口5390台（+6%yoy），占全球一半。但ASP仅1.58百万日元，是北美/欧洲的一半——说明竞争激烈，价格战还在持续。\n\n**2/ 北美/欧洲：量增价跌**\n北美+3%yoy，欧洲+7%yoy，但ASP分别跌20%和39%。高端市场在放量，但利润空间被压缩。\n\n**3/ 小型机器人更吃香**\n某外资投行指出，做小6轴和SCARA机器人的公司，在中国AI需求上更受益。Fanuc（大型机器人为主）5月对华出口环比-23%，明显跑输。\n\n**4/ Robodrill（加工中心）全面走弱**\n全球1204台，同比-26%，环比-27%。中国区559台（-4%yoy），但环比-33%。研报认为智能手机相关需求依然疲软。\n\n**5/ 安川电机（九州出口）断崖式下滑**\n5月出口347台，同比-54%，环比-73%。韩国-80%mom，中国-51%mom，印度-86%mom。OEM项目在收尾。\n\n**总结：** 5月\n\n[... middle omitted ...]\n\nindicator of investment in robots and automation, mainly in the auto and electronics industries. In this note, we outline our views on the robot industry and casing demand trends inferred from\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R020",
    "title": "摩根斯坦利：MS：流媒体战争已结束，赢家不是靠内容取胜",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：流媒体战争已结束，赢家不是靠内容取胜\n\n美国消费者的流媒体订阅数量首次突破5个，日均观看时长接近3小时。但真正值得关注的信号不是总量的增长，而是用户行为正在发生结构性分化——少数平台正在吸收绝大多数注意力和付费意愿，而其他平台正被挤入“可随时取消”的备选名单。\n\nMS最新发布的第16届年度流媒体调查，覆盖约3000名美国消费者，给出了一个清晰但反直觉的判断：流媒体的竞争格局已经不再是“内容军备竞赛”，而是进入了“注意力质量”的决胜阶段。报告核心发现是，亚马逊Prime Video、Netflix和谷歌旗下YouTube在用户渗透率、留存率和付费意愿上继续扩大领先优势，而Meta旗下的Facebook和Instagram Reels正在以惊人的速度抢占用户时间。\n\n这份报告的价值不在于确认“头部平台很强”，而在于揭示了支撑这些平台优势的深层机制——用户与平台之间的交互模式差异，正在成为决定未来盈利能力和估值分化最关键的因素。\n\n> **KC评论：** 多数投资者仍然在用“订阅用户数”和“内容预算”来衡量流媒体公司的价值。但MS这份调查表明，真正值得关注的是“用户打开平台时是否带着明确的目的”——这决定了广告变现效率、定价权以及用户流失风险。完整报告中包含大量关于用户行为模式的细分数据，这些数据对理解不同平台的真实竞争壁垒至关重要。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 用户时间总量在增长，但头部平台的份额增长更快\n\n调查显示，美国平均每个家庭拥有5.4个流媒体服务（含免费），其中付费订阅从去年的3.1个增至3.2个。日均观看时长约3小时，年长用户群的观看时间更长。\n\n但总量增长并不代表所有平台都能受益。亚马逊Prime Video渗透率同比上升264个基点至66%，Netfl\n\n[... middle omitted ...]\n\ncs。欢迎来星球微信群继续讨论，一起跟踪这些关键指标的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国年轻人一天刷3小时视频，这5个平台最稳\n\n流量大战，谁能留住用户？\n\n某外资投行最新调查：平均每人订阅5.4个流媒体服务，每天看3小时内容。大平台越来越强，小平台在边缘挣扎。\n\n1/ 三巨头地位稳固\nAmazon Prime Video渗透率66%，Netflix 55%，YouTube 47%，都在涨。Netflix虽然股价跌了23%，但用户留存率依然最强，被评“最后才会取消”的服务。\n\n2/ 内容质量决定粘性\nNetflix在原创内容质量上重回第一，用户打开它通常是冲着具体剧集去的，专注度最高。YouTube和Disney+则更多被用来“随便刷刷”或当背景音。\n\n3/ 社交平台抢时间\nMeta的Instagram/Facebook Reels和TikTok使用时长同比增长超1000个基点。短视频正在蚕食传统电视时间，微短剧也成了年轻用户的新消耗品。\n\n4/ 体育直播是硬通货\n超过60%的人经常看体育直播，ESPN依然是第一选择。亚马逊靠NFL周四夜赛冲到第二，Netflix也在往上走。\n\n5/ 广告层是增量\nNetflix广告层用户占比从22%升到26%，无广告版稳定在30%左右。说明广告层吸引的是新\n\n[... middle omitted ...]\n\n 16th annual survey of \\~3K American consumers suggests a competitive, but growing streaming landscape with AMZN Prime, NFLX & GOOGL's YouTube showing the strongest engagement & stickiness. Th\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R021",
    "title": "摩根斯坦利：MS：旧存储芯片正经历一场被低估的恐慌性采购",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：旧存储芯片正经历一场被低估的恐慌性采购\n\n市场当下的注意力几乎全部集中在HBM、DDR5和先进封装上。但MS一份最新报告揭示了一个反直觉的判断：真正让企业客户陷入“恐慌性购买”的，不是最前沿的存储芯片，而是被视为“旧时代”的DDR4、NOR Flash和SLC NAND。\n\n这份由Daniel Yen、Charlie Chan等分析师联合署名的研报，将华邦电、南亚科、旺宏、兆易创新和力积电的目标价全面上调，并在标题中直言：“Old Memory: Better to buy more”。\n\n这不是一次简单的补库存周期。这是一场由供给结构性收缩、需求意外扩张和客户行为突变共同驱动的错配。它在告诉我们：旧存储芯片的紧俏，可能比市场预期的更持久、更深刻。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. DDR4的紧俏正在从“涨价”演变为“囤积”，企业客户的行为已经发生变化\n\nMS在5月底将南亚科和华邦电上调至增持时，市场看到的还是DDR4价格连续双位数月涨幅的“涨价故事”。但到了6月底，情况已经升级。\n\n报告明确指出，企业客户正在“as early as possible securing supply amid fears of shortages”。渠道库存已经降至两周以下。这不再是简单的供需缺口，而是客户心态的转变——从“等降价再买”变成了“先锁定产能再说”。\n\n这种恐慌性采购的后果是什么？它意味着即使后续实际需求没有爆发式增长，企业客户为了自保也会建立更高的安全库存。这种“需求缓冲”一旦形成，就会把原本可能只是几个季度的涨价周期拉长，并放大价格弹性。\n\n> **KC评论：** 传统上，存储芯片的涨价周期往往在客户开始“double ordering”时见顶。但这一次，DDR4的供给端没有大规\n\n[... middle omitted ...]\n\nI做训练，也方便人工快速把握market dynamics。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片短缺蔓延到老款存储了\n\n📌 老存储，更紧俏\n\n企业客户正恐慌性囤货，DDR4、NOR、SLC NAND全面告急。\n\n最近投行研报指出，传统存储芯片（DDR4、NOR、SLC NAND）的供应紧张程度远超预期，企业客户正在恐慌性采购，渠道库存已降至两周以下。\n\n几个关键逻辑：\n\n1️⃣ **DDR4涨势未止**：研报提到，DDR4每月已出现两位数环比涨幅，但企业客户担心断供，正提前锁定产能，预计涨势延续到Q4。\n\n2️⃣ **SLC NAND意外受益**：由于MLC NAND短缺，企业级HDD（机械硬盘）开始转向SLC NAND做固件和热数据缓存。Q3已涨50-60%，Q4大概率继续。\n\n3️⃣ **NOR闪存供给更集中**：美系厂商减产NOR，台湾供应商市占率上升。同时新一代AI服务器机架（Vera Rubin）对NOR用量比上一代高出50%+，Q3预计涨价30-40%，Q4仍可能上行。\n\n研报同步上调了多家公司目标价，包括华邦电、南亚科、旺宏、兆易创新等，幅度在4%到62%不等。\n\n你最近有留意存储芯片的价格走势吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n<table><t\n\n[... middle omitted ...]\n\nAIWAN LIMITED+</td></tr><tr><td colspan=\"2\">Tiffany Yeh</td></tr><tr><td colspan=\"2\">Equity Analyst</td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td col\n\n[... middle omitted ...]\n\no Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,100.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R022",
    "title": "Citi：锂价跌了，但真正的紧缺还没来",
    "digest": "[wechat_article.md]\n# Citi：锂价跌了，但真正的紧缺还没来\n\n当锂价在过去一周从每吨16.7万元跌至15.7万元，市场的第一反应是恐慌。江西锂云母龙头复产的传闻像幽灵一样盘旋，下游采购商缩手观望，贸易商库存开始松动。但Citi最新发布的这份周度追踪报告，给出了一个和价格走势截然不同的判断：供需基本面依然紧张，去库存仍在延续，而三季度大量新电池产能的集中释放，可能会让这个市场再次措手不及。\n\n这不是一份简单的“价格下跌，所以看空”的报告。Citi在5M26的进口数据中看到了一个被价格信号掩盖的结构性变化——锂原料的全球供应版图正在发生迁移，而市场对此的定价远未充分。如果你只看价格曲线，你会觉得行业正在走向过剩；但如果你看库存结构、看非洲矿的快速崛起、看下游产能的投产节奏，你会得到一个完全不同的结论。\n\n这份报告最值得关注的核心判断是：锂的供需紧张格局并未被打破，当前的价格回调更多是情绪和短期博弈的结果，而非基本面的反转。Citi甚至明确表示，即便计入江西复产的预期，他们仍然维持看涨观点。这不是一个随大流的立场。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月进口数据揭示了一个被忽视的转折：非洲正在成为锂原料的新供应极\n\nCiti的数据显示，2026年前五个月，中国进口碳酸锂约15.3万吨，同比增长153%。其中5月单月进口量达到约3.75万吨，创下历史新高。锂辉石方面，5M26进口274万吨，同比增长15%。\n\n这些数字本身并不意外——中国作为全球最大的锂加工国，原料进口持续增长是常态。真正值得关注的是供应来源的结构性变化。\n\n澳大利亚仍然是中国最大的锂辉石供应国，占比58%。但这一比例已经显著下降：2025年全年是62%，2025年前五个月是65%。换句话说，澳大利亚的份额在一年内下降了7个百分点。填补这个空缺的不是南美盐湖\n\n[... middle omitted ...]\n\n续交流。每天我们都会在群里分享最新的投行研报摘要和市场数据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n锂进口创历史新高，供给压力来了\n\n从数据看锂电材料\n\n5月碳酸锂进口量创新高，供给端在加速\n\n某外资投行最新研报显示，5月中国碳酸锂进口量约3.75万吨，创单月历史新高。前5个月累计进口约15.3万吨，同比暴增153%。这波进口放量，直接给锂价带来了压力。\n\n1️⃣ 进口结构在变\n\n澳大利亚仍是中国锂辉石最大供应国，占比58%，但份额在下降（2025年65%→现在58%）。非洲国家加速补位，尼日利亚和马里合计占比已升至37%，而2025年只有30%。\n\n2️⃣ 价格持续走弱\n\n截至6月25日，碳酸锂均价15.7万元/吨，较一周前的16.7万下跌约6%。氢氧化锂也同步回落至14.35万/吨。供给增加叠加下游去库存，价格承压明显。\n\n3️⃣ 库存小幅去化\n\n碳酸锂总库存约9.58万吨，环比降低1%，主要来自贸易商环节去库。但下游正极材料厂库存反而微增3%，说明需求端仍在观望。\n\n研报判断，虽然锂价短期承压，但供需结构依然偏紧，预计3季度大量新电池产能投产，可能对需求形成支撑。不过江西某大厂复产仍在扰动市场预期。\n\n#学习笔记\n\n[source_mineru.md]\n# China Battery Material\n\n[... middle omitted ...]\n\n and 30% in 2025 respectively. Lithium price has been under pressure with hovering concern on JXW resumption, albeit lithium S/D dynamics remained tight and de-stocking extended for another we\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R023",
    "title": "GS：中国手机出货量回暖，但真正的结构性机会在摄像头升级",
    "digest": "[wechat_article.md]\n# GS：中国手机出货量回暖，但真正的结构性机会在摄像头升级\n\n中国智能手机市场在2026年5月交出了一份亮眼的月度数据——出货量同比增长19%至2700万部，环比也实现了7%的增长。这组数字很容易让人产生“市场全面复苏”的错觉。但GS这份最新研报揭示的图景远比表面复杂：出货量的反弹背后，是内存成本高企对需求的持续压制，以及摄像头规格升级这一不可逆的结构性趋势。换句话说，行业正在经历一场“量价分化”——出货量波动回升，但真正的价值增量正从“卖更多手机”转向“卖更贵的镜头模组”。\n\n这份报告最值得关注的核心判断是：中国智能手机市场的竞争焦点，已经从“多摄像头堆砌”转向“高像素单摄升级”。这一转变将重塑整个供应链的价值分配，而大多数投资者可能仍停留在旧框架中。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月出货量反弹背后，内存成本仍是悬在需求头上的达摩克利斯之剑\n\n五月出货量同比增长19%，环比增长7%，延续了四月环比增长25%的势头。从数字上看，这似乎是市场加速复苏的信号。但GS在报告中明确预警：**预计二季度整体出货量将同比下降14%**。这个看似矛盾的预测，恰恰揭示了当前市场复苏的脆弱性。\n\n出货量的月度波动，很大程度上受到新机型发布节奏的影响。四月新机型发布数量同比大增56%至50款，五月则骤降至15款，同比下滑44%。这种脉冲式的新品发布，使得单月出货数据容易失真。真正需要关注的是内存成本这一持续变量。\n\n> **KC评论：** 内存成本上升正在抑制中低端机型的需求弹性。当一部手机的BOM中内存占比从15%攀升至20%以上时，厂商要么压缩利润，要么提价转嫁成本。GS预期二季度出货量下降14%，意味着这种压力尚未完全释放。报告中对内存成本如何具体影响不同价位段机型的拆解，值得完整阅读。\n\n![研\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月手机出货量涨了19%，但镜头数量在缩水\n\n📱 出货回暖，但隐忧浮现\n\n5月国内智能手机出货量2700万部，同比+19%，环比+7%，连续第二个月环比正增长。但投行研报提示，受存储芯片涨价影响，预计二季度出货量可能同比下滑14%。\n\n📸 摄像头：数量在降，像素在升\n\n梳理了荣耀/小米/OPPO/vivo/传音2026年已发布的165款机型、487颗摄像头，发现两个趋势：\n\n1️⃣ 每台手机平均摄像头数量从2022年的3.8颗降至2026年至今的3.0颗，厂商不再堆数量\n\n2️⃣ 但高像素（2000万以上）占比持续攀升，2026年至今已达65%，2023年时仅39%\n\n🔍 品牌差异明显\n\nOPPO目前已发布56款机型，摄像头总数171颗，其中低像素（200/500/800万）占比25%；华为最低仅18%，传音最高达33%。各品牌在影像配置上策略分化明显。\n\n🧠 研报解读\n\n手机厂商正在经历“去库存+提规格”的调整期。出货量短期承压，但摄像头升级方向明确——像素竞赛仍在继续，只是从“数量”转向“质量”。这条产业链上的光学零部件厂商值得关注。\n\n#学习笔记\n\n[source_mineru.md]\n# China \n\n[... middle omitted ...]\n\nith our view on camera specification upgrades for China smartphones (report link). Read more: Smartphone TAM.\n\nBuy: Hon Hai (on CL), AAC, Lingyi, Largan, SZS, Fositek, and TSMC (on CL).\n\nAllen\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R024",
    "title": "GS：浆价600美元就是天花板，中国买家正在“罢工”",
    "digest": "[wechat_article.md]\n# GS：浆价600美元就是天花板，中国买家正在“罢工”\n\n过去两个月，中国阔叶浆市场正在经历一场无声的僵局。报价持平，成交量却骤降至正常水平的不到一半。GS拉美纸浆研究团队在最新报告中给出一个直白判断：当前价格需要继续下跌，才能吸引足够的买盘。这对全球纸浆定价体系意味着什么，值得关注。\n\n这份报告的核心洞察并不复杂：GS认为，阔叶浆价格在每吨600美元附近已接近历史周期顶部。当价格维持在这个水平或以上时，中国一体化纸企的竞争力反而更强，并倾向于从非一体化对手手中夺取市场份额。其结果是，商品浆需求减弱，纸浆卖家的定价权随之下降。\n\n报告引用的数据显示，中国FOEX阔叶浆进口价格持平于每吨605美元，而国内转售价已下跌相当于每吨549-556美元。这意味着进口浆与国内浆之间存在每吨约50美元的价差，反映了海外供应商在维持报价上的努力与国内市场实际承受力之间的脱节。\n\n> **KC评论：** GS的核心逻辑是“中国一体化纸企的竞争壁垒”。当浆价高企时，拥有自备浆线的大厂反而能利用成本优势挤压小厂，从而减少对商品浆的采购。这并非简单的供需失衡，而是产业链利润分配的再平衡。完整报告中对这一机制在不同价格区间的演绎有更细致的模型拆解，值得细读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 报价下调20美元仍不足以打动买家，卖方库存正在累积\n\n报告披露了一个关键信号：尽管Arauco和CMPC已将报价下调每吨20美元至约580美元，但渠道调研显示，这并未激发显著的采购热情。4-5月的成交量低于常规量的50%，而卖方的库存正在上升。\n\nGS分析师指出，6月是季度末月，卖方出货压力增加，而买方并不急于下单。这与过往几乎所有熊市周期中的情景如出一辙。报告认为，价格需要进一步下跌，直至能够分配全部常规销量。\n\n这里的关键变量在于卖\n\n[... middle omitted ...]\n\n报告中的未解问题，以及如何将这些判断转化为可操作的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n浆纸周期又来了，这次怎么走\n\n浆纸周期信号\n\n中国阔叶浆价格接近周期顶部\n\n某外资投行最新研报指出，阔叶浆价格在600美元/吨附近已接近过去几轮周期的顶部水平。这个价位上，中国一体化纸厂竞争力更强，会从非一体化厂商手里抢份额，进而削弱浆厂的定价权。\n\n1/ 中国阔叶浆量价信号\n- 4-5月实际成交量不到常规的50%\n- 虽然浆厂检修限制了供应量，但销量还是低于可供应量\n- 卖方库存持续攀升，6月是季度末，卖家出货压力更大\n- 买家完全不急，继续观望\n\n2/ 浆厂降价还不够\nArauco和CMPC已经调降报价20美元/吨至约580美元/吨，但调研反馈显示这个价格还不足以吸引大量采购。研报判断：浆价需要进一步下跌，才能刺激买家回到正常采购量。\n\n3/ 历史规律会重演\n过去几轮熊市周期中，卖家都会选择压货来暂缓中国市场价格下跌，以保护欧美基准价。但这次可能行不通——中国以外地区净价高出至少50美元/吨，这种价差不可持续。中国阔叶浆价格继续下行是大概率事件，最终会传导到其他主要市场。\n\n4/ 新产能压力\n年底中国和印尼都有新浆线投产，预计价格会朝着边际成本线靠拢，直到需求或减产重新平衡供需。\n\n5/ 最新价格参考\n-\n\n[... middle omitted ...]\n\nad limited availability due to downtime in the quarter, sales were below available volumes and sellers inventories have been trending higher. With June being the last month of the quarter, pre\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R025",
    "title": "摩根斯坦利：MS：中国汽车销量已触底，但反弹要等到8月",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国汽车销量已触底，但反弹要等到8月\n\n市场对中国汽车股的悲观情绪已经超越了基本面。这是MS最新一份行业报告中传递出的核心判断。报告通过近期渠道调研与行业会议，得出了一个看似矛盾但逻辑清晰的结论：销量已经找到了底部，但反弹的催化剂尚未就位。\n\n这份报告发布于2026年6月25日，正值二季度收官之际。投资者最关心的问题是：当前的低迷是暂时的周期性低谷，还是结构性下行的开始？MS的答案倾向于前者，但前提是必须接受一个时间差——真正的修复窗口在8月至9月，届时新车周期、季节性因素和地缘政治环境将形成共振。\n\n报告指出，当前市场情绪比真实情况更差。持续的宏观担忧，叠加短期盈利催化剂的缺失，导致投资者缺乏自下而上的买入信心。更关键的是，资金正在向AI/科技板块集中，这种流动性虹吸效应扭曲了行业讨论——大多数对话停留在宏观层面，而非聚焦比亚迪、吉利、蔚来、小鹏和福耀玻璃等公司的基本面。\n\n> **KC评论：** 这意味着当前汽车股的估值中可能已经包含了过多的悲观预期。如果8月后的反弹如期而至，那么二季度末可能是一个值得关注的布局窗口。完整报告中对每家公司的估值方法和风险情景有详细拆解，这是判断安全边际的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 6月销量比表面数据更强，但二季度整体仍将同比下滑\n\nMS的渠道调研显示，6月零售端表现好于批发数据所暗示的水平。背后有多重因素支撑：618促销活动的延长、补贴的叠加、部分城市的牌照豁免政策，以及油价下跌对燃油车需求的短期提振。\n\n具体来看，报告预计6月批发销量环比增长约10-13%，主要由纯电动和插电混动车型驱动，混合动力车型在15-20万元价格段也有温和增长。值得注意的是，部分主机厂正在悄然下调目标，优先消化库存以保护渠道利润，为下半年的新品上市做准\n\n[... middle omitted ...]\n\ns。欢迎来星球微信群里继续讨论，获取完整报告解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n汽车销量触底，反弹窗口在哪？\n\n汽车销量，到底了？\n\n最近某外资投行做了渠道调研，结论挺直接：汽车销量已经找到地板，但还没弹起来。\n\n1️⃣ 销量见底，但还没回暖\n2Q 乘用车批发预计 670-690 万辆，同比降 3-5%，比 1Q 的 -8% 已经收窄。6 月数据会比表面好看，618 促销+补贴+部分地区免牌，推高了实际零售。但消费者还是犹豫——电车迭代太快，隔几个月就出新款、降价，决策周期越拉越长。\n\n2️⃣ 下一波窗口：8-9 月\n7 月是传统淡季，真正有意义的反弹可能在 8-9 月。低基数、订单积累、政策消费支持、新车型集中上市（7 月底开始），这几个因素会叠加。比亚迪和吉利在这个阶段看起来位置不错，小鹏则更多是事件驱动。\n\n3️⃣ 市场情绪比现实更差\n现在资金都往 AI 跑，汽车板块被抽血严重。但投行认为这种悲观反而在给下半年创造交易机会。有些投资者已经开始把估值框架往 2027 年拉了。\n\n4️⃣ 几个值得关注的车型\n比亚迪大唐（锁单 4-5 万）、海狮 08、小鹏 Mona L03、理想 L8、吉利战船 700、小米 Sky Nomad N90。华为的 HIMA 生态还在扩张，但品牌太多、价格\n\n[... middle omitted ...]\n\nlack of near-term earnings catalysts, continue to limit bottom-up conviction. At the same time, the ongoing liquidity drain toward regional AI/tech plays has distorted sector discussions, with\n\n[... middle omitted ...]\n\ntd>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$12.48</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "摩根斯坦利：MS：中国钢铁需求正在“长弱板稳”中筑底，但库存压力才是真正的考验",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国钢铁需求正在“长弱板稳”中筑底，但库存压力才是真正的考验\n\n中国钢铁市场正在经历一轮微妙的分化。MS最新发布的《中国钢铁和铁矿石周报》显示，长材的表观消费量环比下降了12.7%，而扁平材的降幅仅为3.1%。这不是一个简单的需求疲软信号，而是一个清晰的“长弱板稳”结构正在形成。对于产业决策者和投资者而言，真正需要关注的不是总量下滑，而是这种分化背后暴露出的库存积累和利润挤压风险。\n\n这份报告的核心判断是：中国钢铁需求正在经历一个结构性筑底过程，但库存的被动积累正在成为价格和利润的核心压制因素。市场情绪的低迷可能已经过度反映在价格中，但基本面改善仍需等待更明确的去库存信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 长材需求骤降12.7%背后，是房地产的“最后一跌”还是基建的“青黄不接”\n\nMS的数据显示，长材周度表观消费量仅为268.1万吨，环比下降12.7%，同比下降12.2%。这是整个报告中最刺眼的数据。长材主要用于建筑领域，其需求的急剧收缩直接指向房地产和基建两大终端。\n\n从逻辑上推理，长材消费的加速下滑可能来自两个叠加效应：一是房地产新开工面积仍然处于深度负增长区间，存量项目对建材的拉动效应正在递减；二是地方专项债发行节奏在6月出现阶段性放缓，导致基建项目的实物工作量未能如期释放。MS报告没有展开讨论具体的原因，但数据本身已经给出了清晰的指向。\n\n> **KC评论：** 长材消费的12.7%周环比降幅不是一个小波动。它意味着建筑工地的实际用钢量正在以超出季节性的速度收缩。如果这种趋势持续，三季度螺纹钢价格可能面临更大的下行压力。完整的周报中包含了分品种的库存和产量数据，这些数据能帮助判断这种收缩是暂时的还是趋势性的。\n\n![研报原图 2](assets/source_image\n\n[... middle omitted ...]\n\n，欢迎加入我们的知识星球和微信群，与我们一起持续跟踪和讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n钢材周报：库存走高，需求走弱\n\n供需双弱，库存承压\n\n**某外资投行最新钢材周报解读**\n\n最近钢材市场有点“冷”，从最新周度数据看，供需两端都在走弱，库存压力在加大。\n\n**1/ 需求端：长材和板材都在下滑**\n上周长材表观消费环比降12.7%，同比也降12.2%；板材相对好一些，环比降3.1%，同比降4.8%。整体看，下游需求确实不太给力。\n\n**2/ 供给端：产量小幅收缩**\n长材周产量环比降2%，板材降0.5%。虽然产量在降，但降幅明显小于需求，所以库存还是往上走了。247家样本钢厂高炉开工率90.8%，环比微增0.5个百分点，电炉开工率64.5%，基本持平。\n\n**3/ 库存：贸易商和钢厂都在累库**\n贸易商库存1144.9万吨，环比增1.7%，同比增26.3%；钢厂库存456.1万吨，环比增5.8%，同比增5.2%。库存压力不小，尤其是贸易商库存同比增幅明显。\n\n**4/ 铁矿石：到港减少，钢厂补库**\n港口库存1.567亿吨，环比微降0.2%。但钢厂库存环比增5.6%，日均产量和开工率都有小幅提升。发运端，澳洲发运环比增86万吨，巴西降118万吨，整体发运量环比减少。\n\n**总结一下**：短期钢\n\n[... middle omitted ...]\n\nand Brazil were down by 0.32Mt WoW for the period 15th June to 21st June. Shipments from Australia were up by 0.86Mt WoW. Shipments from Brazil were down by 1.18Mt WoW.\n\nExhibit 1: Weekly data\n\n[... middle omitted ...]\n\ning Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb25.92</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R027",
    "title": "Bernstein：数据中心REIT的高估值，不是泡沫，是定价权",
    "digest": "[wechat_article.md]\n# Bernstein：数据中心REIT的高估值，不是泡沫，是定价权\n\n当一家数据中心REIT的EV/EBITDA倍数超过20倍，对于习惯了用市盈率衡量科技公司的投资者而言，第一反应通常是“太贵了”。但Bernstein一份深度研报提出了一个反直觉的判断：这些看起来昂贵的倍数，恰恰反映了这些资产最核心的价值——它们能以远高于资本成本的回报率，持续创造现金。\n\n这份报告的核心洞察是，传统财务指标在评估数据中心REIT时存在系统性失真。资本密集型、长开发周期、以及会计折旧政策，共同导致ROA和市盈率等指标严重低估了这些资产真实的经济回报。对于非REIT专业的投资者而言，直接套用科技股的估值框架，可能会错过AI时代最确定的基础设施投资机会。\n\nBernstein对Digital Realty和Equinix均维持“跑赢大盘”评级，目标价分别为232美元和1222美元。但比目标价更值得关注的，是报告揭示的估值逻辑：市场为这些REIT支付的高溢价，本质上是在为它们“持续将资本转化为高于资本成本的回报”这一能力买单。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 传统估值指标在数据中心REIT上几乎完全失效\n\n非REIT投资者最容易犯的错误，是用ROA或市盈率来衡量数据中心REIT的吸引力。Bernstein明确指出，这种做法会产生严重误导。数据中心资产的使用寿命长达数十年，前期资本投入巨大，建设周期可能长达数年才能产生收入。一旦稳定运营，它们能产生持续几十年的可预测现金流。\n\n在这种资产结构下，ROA被严重压低，因为分母（PP&E）在建设期迅速膨胀，而分子（NOI）需要数年才能充分释放。同样的逻辑适用于市盈率：早期的高折旧费用压缩了GAAP净利润，导致市盈率虚高。\n\n> **KC评论：** 这解释了为什么很多投资者看着Eq\n\n[... middle omitted ...]\n\ns。欢迎来星球微信群里继续讨论，共同跟踪这些关键假设的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心REITs：别被传统指标骗了\n\n📊 真正该看什么？\n\n数据中心REITs在AI热潮中吸引了大量非传统REIT投资者，但用常规指标看它们，容易得出错误结论。\n\n**1/ 为什么传统指标失灵？**\n数据中心资产前期投入大、建设周期长，ROA和盈利倍数往往“不好看”。但这不是业务差，而是因为这些指标是为短期资产设计的。数据中心能用50年+，稳定后能持续产生现金流几十年，用短期指标衡量长期资产，自然失真。\n\n**2/ 真正该看什么？**\n✅ **AFFO（调整后运营资金）**：REIT框架下最接近可分配现金流的指标\n✅ **成本收益率**：评估稳定资产回报的核心指标\n- Digital Realty（DLR）≈11%\n- Equinix（EQIX）≈26%\n远高于私人市场开发商的HSD水平\n\n**3/ 为什么EQIX回报更高？**\n- 零售托管占比大，单位定价高、利润结构更好\n- 互连和托管服务占收入24%（DLR仅8%），边际利润接近软件水平\n- 折旧政策更优：EQIX用12-60年折旧，DLR用5-39年，前者平滑了费用\n\n**4/ 高估值合理吗？**\nEV/EBITDA看起来贵（22-23x），但结合资\n\n[... middle omitted ...]\n\nrs puzzle over the right way to think about these companies—both how to contextualize them against one another and against alternate investment opportunities.\n\nData center REITs often screen p\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R028",
    "title": "Citi：香港地产的真正催化剂不在6月，而在8月",
    "digest": "[wechat_article.md]\n# Citi：香港地产的真正催化剂不在6月，而在8月\n\n市场对香港地产的担忧集中在短期情绪和资金管制上，但Citi最新研报给出了一个反直觉的判断：这些短期扰动不会改变中期上行周期。6-7月股价可能继续波动，但真正的催化来自8月公布的强劲1H26业绩。\n\n这份研报基于Citi近期举办的Property & Financials Conference，覆盖14家地产公司和全球投资者。其核心结论是：发展商利润率已明确触底，写字楼租金在核心区出现上涨动力，而零售租户销售正在改善。市场目前对政策执行和利率预期的担忧，恰恰可能为中期布局提供了窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 内地资金管制的影响被市场高估，香港物业仍是CRS之外的资产配置选项\n\nCiti在会议中与14家地产公司逐一确认后发现，内地ODI新规对香港住宅和写字楼市场“没有可衡量的实际影响”。过去一个月内仅有1-2例取消或延迟成交的个案，且与政策无关，属于正常波动。\n\n更值得关注的是开发商提供的数据：非香港身份证买家占比始终低于10%。即使在启德这类内地买家集中的区域，非香港身份证持有者比例也仅约15%，尽管77%的买家姓名为内地姓氏。这意味着市场担忧的“资金断流”场景并未出现。\n\n> **KC评论：** Citi指出一个常被忽视的关键点——香港物业不在中国CRS税务信息交换范围之内。这意味着对于部分高净值内地投资者，香港物业不仅是居住需求或租金回报的配置，更是一种资产保护和隐私安排。这个维度在公开讨论中很少被充分展开，完整报告中有更详细的分析框架。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 短期成交量波动是多重因素叠加，而非趋势逆转\n\nCiti预计1H26E一手住宅登记量约12,500套，可能创\n\n[... middle omitted ...]\n\n每家公司的具体拆解和估值假设，以及如何将其纳入你的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港楼市，中期看涨逻辑没变\n\n📌 短期震荡，中期向上\n\n刚参加完某外资投行的地产金融会，聊了14家上市房企+全球投资者，信息量很大，直接上干货。\n\n**1/ 内地资金管制影响有限**\n- 开发商反馈：目前未观察到实质影响\n- 非香港本地买家占比<10%（与税务局数据一致）\n- 启德项目虽77%是内地姓氏，但非本地身份仅15%\n- 香港房产不在CRS范围内，仍是资产配置优选\n\n**2/ 短期楼市在等什么？**\n6月成交确实静了，原因：\n- 港股回调影响情绪\n- 买家观望，预计1-2个月情绪稳定\n- 天气+推盘节奏放缓\n- 二手议价空间收窄\n\n但下半年新房注册量有望创21年新高（约1.25万套），二手同比+35%。\n\n**3/ 中期逻辑更值得关注**\n- 2026-28年新供应仅1.5-1.8万套/年，结构性短缺\n- 开发商利润率已见底，1H业绩将验证\n- 启德项目今年已涨10-15%，OPM回到中双位数\n\n**4/ 各板块亮点速览**\n🏠 开发商：\n- 新地：FY26香港销售目标370亿，利润率回升\n- 长实：中期或有“小糖果”特别息\n- 恒地：政府收地预计27年中重启\n\n🏢 收租股：\n- 太古地产：内地商场4\n\n[... middle omitted ...]\n\no concern on policy execution, higher interest rate expectations, and rotation to other sectors or regions. Investors showed greater focus on company-specific features (DPS, buyback, capital r\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R029",
    "title": "GS：CPU服务器被严重低估，Agentic AI可能带来5-6倍市场增量",
    "digest": "[wechat_article.md]\n# GS：CPU服务器被严重低估，Agentic AI可能带来5-6倍市场增量\n\n当市场几乎把所有注意力都集中在GPU和AI训练集群上时，一个被忽视的结构性机会正在传统服务器领域悄然成型。\n\nGS在6月26日举办的专家网络系列研讨会上，邀请前英特尔全球AI产品与战略总监、现任Pacific AI Advisory创始人与执行AI策略师Jordan Plawner，围绕CPU服务器需求趋势进行了深度讨论。这份研报给出的核心判断值得每一个关注企业级IT基础设施的决策者认真对待：**Agentic AI可能为CPU服务器市场带来5-6倍的需求增量，而传统服务器更新换代的经济账已经算得过来。**\n\n这不是一个关于“GPU还能涨多少”的故事。这是一个关于“当AI从训练走向推理，从集中式走向分布式，从少数巨头走向千万家企业，谁将承接这一轮基础设施重构”的判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Agentic AI正在改写CPU与GPU的配比逻辑，CPU服务器需求可能迎来数量级跃升\n\n当前AI训练工作负载中，CPU与GPU的配比约为1:4。换算成实际投入，每1美元的CPU支出对应50-80美元的GPU支出。这是一个极度偏向GPU的配置，反映了过去两年行业集中建设训练集群的现实。\n\n但Plawner的判断是，随着市场向更多样化的推理和Agentic工作负载演进，CPU与GPU的配比将逐步趋向1:1。这意味着，每1美元的CPU支出对应6-10美元的GPU支出。如果这一趋势成立，CPU服务器市场规模将实现5-6倍的增长。\n\n为什么CPU在Agentic AI场景中更占优势？核心原因在于两类芯片的架构差异。GPU是为大规模并行处理设计的，适合训练过程中海量矩阵运算。但AI代理执行的是序列化任务和异构工作负载——比如编排、\n\n[... middle omitted ...]\n\n入我们的知识星球和微信群，继续深入讨论这份报告中的未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPU服务器，这轮是被低估的主角\n\n**服务器需求的三重推力**\n\n---\n\n最近读了一份外资投行的专家访谈，核心观点很清晰：CPU服务器市场可能正站在一个被低估的拐点上，需求来自三个方向。\n\n**1. Agentic AI 带来的结构性机会**\n\n专家认为，Agentic AI 的普及可能让CPU服务器市场扩容5-6倍。逻辑是这样的：目前AI训练场景中，CPU与GPU的支出比大约是1:50-80；但推理和agent任务需要处理大量顺序、异构工作流，CPU天然更适合这类操作。随着agentic工作负载增加，这一比例可能逐步走向1:1左右，即每花1美元在CPU上，对应6-10美元的GPU支出。这对深耕通用计算的企业级OEM厂商是明确的增量。\n\n**2. 存量服务器更新的窗口**\n\n现有传统服务器的平均服役年限已拉长到约6年（历史均值3-4年），因为过去几年IT预算被GPU和AI训练占用了。但新一代CPU服务器核心数提升约4倍，每核内存密度翻倍，意味着可以用约350台新机替换1000台旧机。除了性能跃升，还能显著降低电费（每年约100万美元），投资回收期约2-3年。而且，运行24/7的agent会加速服务器老化，\n\n[... middle omitted ...]\n\nssive parallel processing); (2) Significant opportunity for performance and efficiency improvements from refreshing the installed based of legacy servers; (3) Only \\~1/2 of enterprise server d\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R030",
    "title": "GS：AI已在广告业全面部署，但真正的赢家不是科技公司",
    "digest": "[wechat_article.md]\n# GS：AI已在广告业全面部署，但真正的赢家不是科技公司\n\n戛纳国际创意节刚刚落幕。GS分析师团队在四天内与超过20家广告主、广告集团、独立代理机构和广告技术公司进行了密集交流。得出的结论值得每一位关注AI商业落地的读者认真审视。\n\n这份报告最核心的判断是：AI正在从根本上改变广告业的成本结构和竞争逻辑，但最大的受益者可能不是人们以为的科技公司，而是那些能够把技术转化为服务溢价的传统广告集团。\n\n当市场还在争论AI会不会取代人类创意时，广告业已经悄悄完成了从“要不要用AI”到“怎么用好AI”的转变。GS团队发现，AI已经几乎被部署在所有广告活动中——不是试点，不是测试，而是全面铺开。\n\n这背后隐藏着一个更重要的信号：广告支出与GDP的相关性正在被打破。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年广告支出与GDP脱钩，AI玩家的增量资金正在改写行业周期\n\n长期以来，广告行业被视为经济的滞后指标——企业只有在经济向好时才会增加营销预算。但这个规律正在被打破。\n\nGS团队在戛纳获得的关键反馈是：2026年广告支出预期上调，增量资金主要来自AI企业。这些新玩家为了抢占市场份额，正在大规模投入品牌建设和效果广告。即使中东地缘冲突持续，也未能阻挡这一趋势。\n\n但这并不意味着行业已经进入新周期。报告同时指出，2027年将面临更严峻的挑战——届时大型体育赛事和政治广告等一次性刺激因素将不再存在，行业需要靠内生增长来维持当前增速。\n\n> **KC评论：** 这意味着2026年可能是一个特殊的“政策窗口”。AI企业的广告投放带有强烈的“占位”性质，一旦市场份额稳定，这部分增量可能快速消退。对于广告集团而言，2026年的营收增长不能简单线性外推。\n\n## 2. 大语言模型在广告变现上面临结构性天花板，搜索广告仍是最大战\n\n[... middle omitted ...]\n\ns。欢迎来星球微信群里继续讨论，一起跟踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n戛纳广告节回来后，我整理了8个关键发现\n\nAI正在重塑广告行业\n\n1️⃣ 广告支出与GDP的关联被打破\nAI玩家带来的新预算正在拉动增长，2026年表现超预期。但2027年可能面临挑战，因为体育赛事和政治活动的基数效应会显现。\n\n2️⃣ 大语言模型（LLM）的广告收入\n它们需要更多帮助来规模化广告收入，但搜索、品牌和效果预算都是可触及的。生成式搜索这个品类预计会指数级增长。\n\n3️⃣ AI已全面渗透广告活动\n几乎所有广告活动都在用AI，代理商的生产收入也在增长。但技术之外，服务需求依然存在。大型代理商没有讨论裁员，戛纳参会人数远超往年。\n\n4️⃣ 营销组织变革困难重重\n广告主有更高效的组织方式，但变革既难又慢。CMO任期短，优先级太多。\n\n5️⃣ 媒体代理商的新机会\n它们很适合聚合LLM的token采购，但管理层会不会抓住这个机会？\n\n6️⃣ LLM可能商品化DSP界面\n智能代理（agentic AI）甚至可能完全取代DSP。但购买代理和DSP真的有本质区别吗？\n\n7️⃣ LiveRamp的服务难以复制\n虽然Omnicom声称做到了，Dentsu也在自建替代方案。行业反馈认为这笔交易能帮助Publicis实现\n\n[... middle omitted ...]\n\norts and political events.\n\nJames Tate  \n+44(20)7774-3705 | james.tate@gs.com  \nGS International\n\nPulkit Gubgotra +1(332)245-7520 | pulkit.gubgotra@gs.com GS India SPL\n\n2. Major LLMs may need \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R031",
    "title": "NOM：南京高端mall正在告诉我们，消费分化已进入“品牌级”决战",
    "digest": "[wechat_article.md]\n# NOM：南京高端mall正在告诉我们，消费分化已进入“品牌级”决战\n\n中国消费市场的复苏故事，正在从一个简单的“总量回升”演变为一场残酷的“品牌级”分化。NOM最新发布的南京某头部高端购物中心渠道调研显示，即便在同一座商场、同一层楼，品牌之间的销售表现已经拉开巨大差距——有的品牌在2季度依然保持两位数增长，有的已陷入同比下滑。这份报告的核心判断是：**消费复苏的“水涨船高”阶段已经结束，接下来考验的是每个品牌能否在客流回暖中找到自己的定价权和复购逻辑。**\n\n为什么现在值得认真读这份报告？因为南京这座商场的数据，某种程度上是中国高净值消费的“压力测试场”。2季度总客流同比增长约10%，总销售额同比增长中个位数，但品牌之间的冷热不均，比任何宏观指标都更直接地揭示了消费信心的真实底色。NOM通过一场与商场专家的电话会，拿到了第一手的品牌级销售数据——不是泛泛的“消费降级”或“消费升级”叙事，而是具体的、可验证的赢家与输家。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 客流恢复已是事实，但消费者把预算从“买包”转向了“体验”\n\nNOM调研的这座南京高端mall，2季度客流同比增长约10%，但专家明确指出：客流增长并未等比例转化为商品销售增长。消费者更倾向于将支出投向体验型消费——餐饮、展览、亲子活动、限时快闪。商场管理层也顺势而为，在五一假期、“520”节点以及商场20周年庆等窗口期，集中策划了多轮体验导向的促销活动。\n\n这意味着什么？**客流的“量”回来了，但客单的“质”在变。** 消费者不再像过去那样，走进商场就直奔奢侈品店刷卡，而是先喝杯咖啡、看个展、再决定是否购买。这种消费节奏的变化，对依赖冲动消费的品牌是利空，对拥有强品牌黏性的品牌则是中性甚至利好。\n\n> **KC评论：** 消费行为从“目的\n\n[... middle omitted ...]\n\n们整理的消费赛道观察框架感兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n南京高端商场客流回暖，但消费分化明显\n\n消费回暖，但各有各的节奏\n\n最近和某外资投行一起调研了南京一家头部高端商场，聊完发现一个很有意思的点：客流回来了，但钱包还没完全打开。\n\n1️⃣ 整体数据：人流涨了，消费增速慢半拍\n- 2季度客流同比增约10%\n- 但销售额只涨了中个位数（mid-single digit%）\n- 对比1季度（春节旺季），2季度环比明显走弱\n- 消费者更愿意为“体验”买单，商场借劳动节、520、20周年庆来刺激体验型消费\n\n2️⃣ 黄金珠宝：长期看好，短期分化\n- 专家长期看好黄金珠宝赛道，认为高品质珠宝和收藏品需求持续\n- 梵克雅宝（历峰旗下）2季度同店销售双位数增长，势头强劲\n- 卡地亚（历峰旗下）跌幅也在收窄\n- 老铺黄金（6181 HK）2季度同店增长40-50%，但比1季度超70%明显放缓\n  - 原因1：商场内金饰品牌竞争加剧\n  - 原因2：金价下跌影响消费情绪\n\n3️⃣ 奢侈品：几家欢喜几家愁\n- Dior（LVMH旗下）出现明显复苏信号\n- 爱马仕、LV（LVMH）、香奈儿增长稳定\n- 其他品牌仍在承压\n\n一点观察：高端消费不是“全面回暖”，而是“结构性分化”——黄金珠\n\n[... middle omitted ...]\n\nD) 2Q26 saw some sequential weakening from 1Q26 (historically the peak season with the Chinese New Year holiday). As per the expert, in 2Q26, the shopping mall's total foot traffic grew by c.1\n\n[... middle omitted ...]\n\n front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R032",
    "title": "NOM：高端mall的韧性，藏在K型分化的裂缝里",
    "digest": "[wechat_article.md]\n# NOM：高端mall的韧性，藏在K型分化的裂缝里\n\n当市场对中国消费的普遍叙事停留在“降级”与“收缩”时，一份来自NOM的渠道调研给出了截然不同的截面。这份报告的核心判断是：中国高端消费并未崩塌，而是在经历一场剧烈的K型分化。头部高端购物中心的销售额在2026年第二季度虽然边际放缓，但整体仍保持正增长，且NOM专家对下半年持乐观态度。这并非盲目的乐观，而是基于一个清晰的逻辑：财富效应正在从股市和一线城市楼市传导至特定人群，而高端mall正是这一效应的直接受益者。这份报告的价值，不在于它给出了一个简单的“好”或“坏”的结论，而在于它拆解了“谁在增长、谁在承压、背后的驱动力是什么”。\n\n> **KC评论：** 这份报告最值得关注的信号是“K型复苏”在中国消费领域的具象化。它意味着，用宏观消费数据一刀切地判断所有消费类资产，可能会犯下严重的错误。对于投资者而言，真正的功课不是判断消费整体是冷是热，而是识别出哪些细分赛道和商业模式正在享受K型曲线的上半段。\n\n以下，我们将基于NOM这份最新的渠道调研纪要，拆解其核心洞察，并探讨这些信号对投资决策的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度销售边际放缓，但“韧性”才是关键词，而非“衰退”\n\nNOM专家调研的这家拥有超过100个中高端购物中心的头部运营商，其同店销售（SSS）在4月录得中单位数同比增长，5月回升至高单位数增长，6月至今又回落至中单位数。从月度波动看，确实出现了边际放缓，尤其是对比3月份低双位数（luxury brands）的增速。但需要强调的是，整体依然处于正增长区间，且客流同样保持正向增长。\n\n这组数据最核心的启示是：高端消费的基本盘并未动摇。市场此前对消费的悲观预期，可能过度定价了“断崖式下跌”的风险。实际上，高端mall的客流和销售\n\n[... middle omitted ...]\n\n百位产业决策者和专业投资者一起，持续追踪这些关键的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n高端mall的客流秘密：K型复苏正加速\n\n高端mall的“K型分化”\n\n最近和一位深耕国内高端消费的专家聊了聊，发现头部高端商场正在经历一场有趣的“K型复苏”。简单来说，就是有钱人的消费力依然坚挺，而中间层的消费在变谨慎。\n\n1️⃣ 二季度业绩小幅放缓，但韧性还在\n根据某头部高端商场（全国超100家门店）的观察，二季度同店销售和客流增速略有降温：\n- 4月：同店销售同比增5-6%，客流增低个位数（比3月的10%+和高个位数明显回落）\n- 5月：靠营销活动拉动，两项数据都回到高个位数增长\n- 6月至今：又回落到中个位数\n但奢侈品mall整体还是跑赢了非奢侈品mall，餐饮和娱乐业态增速尤其亮眼。\n\n2️⃣ 专家对下半年偏乐观\n理由很直接：K型复苏下，高净值人群是股市回暖、一线城市房价企稳的直接受益者。他们认为下半年高端mall的销售有望继续领跑。\n\n3️⃣ 三个细分赛道表现各异\n- 奢侈品：增速从3月的约10%放缓，二季度整体降速\n- 黄金珠宝：4-5月同店销售降10-15%，但老铺黄金（某高端黄金品牌）逆势爆发，4月同比增50%，5月加速到60%+，靠的是门店调整和高端营销\n- 户外：依然坚挺，始祖鸟、萨洛蒙\n\n[... middle omitted ...]\n\nwitnessed a slightly softened sales momentum quarter-to-date (QTD) 2Q26, according to the expert. The expert shared that same-store sales (SSS) across projects of the leading high-end shopping\n\n[... middle omitted ...]\n\nent is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:"
  },
  {
    "id": "R033",
    "title": "JPM：澳洲基金经理正在集体撤离防御板块，这次不是战术调整",
    "digest": "[wechat_article.md]\n# JPM：澳洲基金经理正在集体撤离防御板块，这次不是战术调整\n\n五月的数据释放了一个清晰的信号：澳洲主动型基金经理正在系统性降低防御性板块的持仓。这并非一次战术性减仓，而是更大范围板块轮动的序幕。JPM最新发布的澳洲基金持仓雷达报告显示，基金经理在通讯服务、医疗保健和必需消费这三个防御性板块的主动权重合计下降了约59个基点，且近70%的被跟踪基金经理同步削减了通讯和医疗保健的头寸。\n\n在防御板块退潮的同时，原材料板块正经历一场由价格驱动的被动增仓。五月，原材料板块在指数中的权重飙升了230个基点，所有被跟踪的基金都提高了该板块的持仓。但JPM的分析揭示了一个关键细节：剔除价格效应后，仅有40%的基金经理实际增加了主动权重，大多数人是被动跟随指数上涨，甚至利用这一机会悄悄减仓。\n\n这两个方向相反的动作指向同一个结论：澳洲市场的资金流向正在发生结构性转变，而基金经理的持仓行为显示，这一转变仍处于早期阶段。\n\n> **KC评论：** JPM这篇报告的独特价值不在于告诉你“资金在轮动”——这是市场公开信息——而在于它拆解了“主动加仓”与“被动跟涨”的区别。5月原材料板块的暴涨（BHP单月涨16%）迫使所有基金被动提升持仓，但真正主动加仓的只有四成。这意味着如果原材料行情延续，仍有大量低配基金需要追买；反之，如果行情逆转，这四成主动加仓者可能率先撤退。完整报告中的“Love Index”和“Short Interest Monitor”提供了更精细的个股层面信号，值得细读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 防御板块的撤退是系统性而非个案，通讯服务减仓力度创近两年新高\n\n五月防御板块的减持并非均匀分布，而是有明确的领跌者。通讯服务板块的主动权重降幅最大，达到30个基点，接近两个标准差的统计异常水平。必需消费和\n\n[... middle omitted ...]\n\n个股层面的持仓变化感兴趣，欢迎来我们的社群和微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n基金经理们正在集体“跑路”防御股\n\n基金经理集体“跑路”防御股\n\n5月，防御板块遭遇全面减持\n\n最近一份某外资投行的基金持仓监测报告显示，基金经理们正在从防御性板块撤退。\n\n1. 防御板块遭遇全面减持\n5月份，基金经理们集体减持了通讯服务、医疗保健和日常消费品三大防御板块，平均主动权重下降了约59个基点。其中通讯服务领跌（-30bp），医疗保健（-11bp）和日常消费品（-13bp）紧随其后。值得注意的是，近70%的基金经理同时削减了通讯服务和医疗保健的持仓。\n\n2. 资源股逆势受追捧\n与防御板块形成鲜明对比的是，材料板块在5月获得了高达230个基点的指数权重增加。不过这份研报指出，这更多是被动跟随板块上涨的结果——剔除价格效应后，只有40%的基金经理主动增加了该板块的权重。\n\n3. 谁是基金经理的“新宠”？\n根据该行编制的“Love Index”，ORI首次登顶“最受青睐”榜首，IAG和QBE也进入了“受青睐”区间。而BHP、CSL等7只股票则跌出了“受青睐”名单。\n\n4. 热门讨论话题\n基金经理们5月主要讨论两个主题：一是联邦预算案中资本利得税和负扣税政策变化对房地产市场的影响；二是以铜为代表的大宗商品正\n\n[... middle omitted ...]\n\nmunications and Healthcare positions. The key question is whether this is the opening salvo of a sustained exit from defensives, or a tactical trimming. In our view, there is increasing eviden\n\n[... middle omitted ...]\n\nthird-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 25 Jun 2026 07:59 PM AEST\n\nDisseminated 25 Jun 2026 08:05 PM AEST"
  },
  {
    "id": "R034",
    "title": "HSBC：软件末日远未到来，市场过度恐慌给了买入机会",
    "digest": "[wechat_article.md]\n# HSBC：软件末日远未到来，市场过度恐慌给了买入机会\n\n当整个市场都在讨论“AI将消灭软件公司”时，HSBC的一份最新研报给出了截然不同的判断：不仅没有看到任何实质性的AI颠覆迹象，反而认为软件板块的恐慌性抛售已经过头了。\n\n这份来自HSBC科技团队的深度报告，核心结论可以用一句话概括：**软件公司的营收、合同负债、利润率、管理层指引和自身回购行为，全部指向一个方向——AI非但没有杀死软件，软件公司正在用AI巩固自己的护城河。**\n\n对于担心“AI会替代所有软件”的投资者来说，这份报告提供了一组反直觉的数据。2026年第一季度，主要软件公司的营收中位数同比增长12.7%，合同负债保持双位数增长，SAP、Salesforce、ServiceNow等巨头纷纷发布了未来数年的强劲增长指引。更值得关注的是，软件公司正在以2023-24年三倍以上的速度回购自家股票。\n\n市场可能高估了AI的效率提升，也低估了企业软件的护城河。这不是一份简单的“看多报告”，而是一次对市场主流叙事的结构性挑战。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 营收与合同负债双强，未见任何需求崩塌信号\n\n如果AI真的在颠覆软件，最直接的证据应该是软件公司的收入增长放缓甚至下滑。但HSBC的数据显示，事实恰恰相反。\n\n2026年第一季度，主要软件公司营收中位数同比增长12.7%。这不是被少数巨头拉高的数字，而是整个板块的普遍现象。Adobe、Salesforce、ServiceNow、Workday的合同负债（cRPO）增长均在13%至23%之间，SAP的云合同负债更是同比增长25%。\n\n更关键的是长期指引。ServiceNow给出了2026-2030年18.4%的营收CAGR指引；SAP、Salesforce和Oracle都明确表示未来几年营收\n\n[... middle omitted ...]\n\n论是否适用于中国软件市场？这些都需要更深入的拆解和持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n软件末日论，该醒醒了\n\nAI威胁被高估\n\n最近总有人说AI要“取代软件”，甚至“软件末日”来了。但翻完某外资投行最新研报，我发现事实恰恰相反——软件公司不仅没崩，反而活得挺好。\n\n1️⃣ 收入增长依然强劲\n一季度软件行业收入中位数同比增长12.7%。SAP、Salesforce、ServiceNow等巨头都给出了未来几年的高增长指引。如果AI真在颠覆软件，这些公司不会这么淡定。\n\n2️⃣ 没有定价压力，利润还在涨\n用非GAAP运营利润率当定价信号，大部分软件公司一季度利润率都在扩张。SAP涨了276bp，Salesforce涨了253bp。客户没少花钱，公司也没降价。\n\n3️⃣ 回购翻倍，公司自己最信自己\n如果排除异常值，主流软件公司的回购金额比2023-24年翻了3倍以上。公司用真金白银投票，比任何分析都诚实。\n\n4️⃣ AI生产力提升，其实很有限\n目前AI编码工具对IT服务和软件公司的生产力提升最多只有100-500bp。想靠“vibe coding”低成本重建企业级应用？研报说：市场想多了。\n\n5️⃣ 巨头们自己怎么看\nOracle、SAP、Salesforce的高管都在淡化AI威胁。SAP CTO说得\n\n[... middle omitted ...]\n\neady eating AI (26 Feb 2026).\n\nSoftware revenue growth remained strong in 1Q26 (median 12.7% y-o-y constant currency). Current remaining performance obligations also posted strong double-digit\n\n[... middle omitted ...]\n\nreproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Bank Middle East Limited."
  },
  {
    "id": "R035",
    "title": "摩根斯坦利：MS：钠离子电池的真正突破不在成本，而在AIDC",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：钠离子电池的真正突破不在成本，而在AIDC\n\n当市场还在争论钠离子电池能否在成本上挑战磷酸铁锂时，MS最近一份深度报告给出了一个更值得关注的判断：钠离子电池的真正价值，可能首先体现在AI数据中心（AIDC）储能场景中。\n\n这不是一个关于“更便宜”的故事，而是一个关于“更适合”的故事。本周，宁德时代在德国慕尼黑正式发布了TENER Sodium储能系统——全球首个经过现场验证的钠离子电池储能系统。管理层的目标是在2026年底前实现1GWh的累计出货，全球交付从2027年6月开始。\n\n这份报告最值得读的判断是：钠离子电池在AIDC储能中的性能优势，可能比成本优势更具颠覆性。而这一判断背后的逻辑，值得每一个关注下一代储能技术的人重新审视。\n\n> **KC评论：** 大多数人对钠离子电池的认知还停留在“比磷酸铁锂便宜但能量密度低”的标签上。MS这份报告的核心贡献，是把讨论从“成本替代”拉到了“场景适配”——在某些特定的高价值场景里，钠离子电池的短板不是问题，长板反而是刚需。完整报告里有一张关键的性能对比图，值得仔细看。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 钠离子电池在AIDC场景中具备天然的性能匹配优势\n\n为什么是AIDC？原因在于钠离子电池的化学特性与AI数据中心的用电需求之间存在高度匹配。\n\nAI数据中心的电力负荷不是平稳的。训练和推理任务的密集计算会产生频繁的功率波动，需要储能系统具备快速响应、高倍率充放电和频繁循环的能力。传统磷酸铁锂电池在这些场景下并非最优解——它的倍率性能受限于锂离子在正极材料中的扩散动力学。\n\n钠离子电池的化学特性恰好相反。钠离子的离子半径虽然比锂离子大，但在某些电解质体系和电极材料中，钠离子的传输动力学反而更快。这听起来反直觉，但实际表现是：钠离子电池在高电\n\n[... middle omitted ...]\n\net dynamics。欢迎来星球微信群里继续讨论这些问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n钠电商业化，这步迈得挺大\n\n钠电进入GWh时代\n\n某外资投行最新研报，拆解了钠离子电池的商业化进展。核心观点很清晰——钠电不是低端替代，而是技术壁垒更高的新物种。\n\n1️⃣ 关键节点：CATL发布TENER钠电储能系统\n这是全球首个通过现场验证的钠电储能系统。目标：2026年底累计出货1GWh，2027年6月全球交付。研报认为这标志着钠电从实验室走向GWh级商业化。\n\n2️⃣ 供应链已跑通\nCATL已锁定超10GWh的材料供应，目标年内建成40GWh钠电产能。上游材料规模化能力，将成为早期玩家的核心竞争壁垒。\n\n3️⃣ 钠电在AIDC场景比LFP更合适\n核心优势：倍率性能更强、低温表现更好、成本更低。虽然能量密度略低，但在需要快速响应、高功率输出的场景（如AIDC），钠电的综合性能更优。研报认为AIDC会是钠电商业化的天然切入点。\n\n4️⃣ 技术壁垒比LFP高得多\n钠电需要攻克：正极材料优化、硬碳负极开发、电解质配方、SEI工程、低温与倍率平衡、制造良率等。CATL还开发了无负极钠电架构，能量密度接近高端LFP。这意味着行业会更集中，先发优势明显。\n\n钠电不是简单的替代方案，而是一个需要深厚材料科学积累的技术\n\n[... middle omitted ...]\n\nl supply has been secured now; further supply chain expansion is on the way\n\n\\- Superior rate capability vs. LFP makes batteries particularly well suited for AIDC storage, apart from cheaper c\n\n[... middle omitted ...]\n\n Co. Ltd. (002001.SZ)</td><td>E (01/26/2026)</td><td>Rmb30.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R036",
    "title": "Bernstein：酒店品牌的生命周期只有30年，豪华是唯一的例外",
    "digest": "[wechat_article.md]\n# Bernstein：酒店品牌的生命周期只有30年，豪华是唯一的例外\n\n当你下一次计划出差或家庭旅行，打开预订APP浏览酒店品牌时，或许从未想过一个问题：那些你信赖的连锁品牌，正在不可逆转地老去。\n\nBernstein一份名为《Whatever happened to Howard Johnson? The lifecycle of a hotel brand》的研报，给出了一个令人意外的判断：绝大多数主流酒店品牌，从诞生到巅峰的生命周期只有大约30年。Howard Johnson从1950年代超过1500家门店的辉煌，萎缩到今天仅有约120家，不是偶然，而是行业规律。\n\n这个判断之所以重要，不仅因为它解释了为什么万豪、希尔顿、洲际这些酒店集团旗下品牌数量越来越多，更因为它直接指向一个投资逻辑：那些拥有最年轻品牌组合的酒店集团，比如希尔顿和凯悦，在未来的增长竞赛中可能天然占据优势。而那些品牌组合老化、未能及时补充新鲜血液的公司，将面临系统性增长减速。\n\n这份研报没有停留在简单的历史回顾，而是系统性地拆解了品牌为什么在30年左右触顶、哪些因素可以打破这一规律、以及这对酒店股意味着什么。以下是核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 品牌老化不是管理问题，是结构性宿命\n\nBernstein的分析覆盖了美国主流酒店品牌的历史数据，结论非常清晰：无论是Holiday Inn、Crowne Plaza还是Comfort Inn，其客房数量和管道项目数量，都在品牌创立后的25至35年间达到峰值，随后进入不可逆的萎缩阶段。\n\n以Crowne Plaza为例。该品牌1983年作为Holiday Inn Crowne Plaza推出，1994年独立更名。其美国管道项目在2008年达到43家酒店的峰值，总酒店数在2\n\n[... middle omitted ...]\n\n中文摘要和原始图表，也会持续跟踪主要酒店集团的品牌组合变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n酒店品牌也有“保质期”\n\n品牌生命周期：30年定律\n\n你有没有想过，为什么酒店集团要不停推出新品牌？\n\n某外资投行的一份研报，用Howard Johnson的故事讲了一个很有意思的逻辑：品牌是有生命周期的。\n\nHoward Johnson在1970年代巅峰期有超过1500家门店，如今只剩120家左右。不是美国人突然不爱吃汉堡冰淇淋了，而是酒店品牌本身就有“保质期”。\n\n📌 30年是一个分水岭\n\n研报追踪了大量美国主流酒店品牌，发现一个惊人一致的规律：\n- 品牌创立后25-30年，在建项目数达到顶峰\n- 30-35年，客房总数达到峰值\n- 之后开始下滑，最终稳定在远低于峰值的水平\n\nCrowne Plaza就是典型案例，1983年推出，2008年达到43家在建酒店的峰值，现在全球429家，美国在建仅5家。\n\n为什么品牌会老化？\n\n1️⃣ 客人喜新厌旧。新酒店评分普遍更高，老酒店设施老化会拖累整个品牌形象。\n\n2️⃣ 消费者偏好会变。比如“全服务”酒店（带餐厅、会议室）越来越不受欢迎，客人更倾向有限服务模式，这对老牌全服务品牌是结构性逆风。\n\n3️⃣ 好位置就那么多。同一品牌不能扎堆开，最终会碰到增长天花板。\n\n[... middle omitted ...]\n\nneesha Sherman +1 917 344 8457 aneesha.sherman@bernsteinsg.com\n\nCallum Elliott, CFA, ACA +44 20 7676 7183 callum.elliott@bernsteinsg.com\n\nDanilo Gargiulo +1 917 344 8475 danilo.gargiulo@bernst\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R037",
    "title": "Bernstein：医疗器械不是基本面崩了，是故事变复杂了",
    "digest": "[wechat_article.md]\n# Bernstein：医疗器械不是基本面崩了，是故事变复杂了\n\n过去一年，美国医疗器械板块跑输标普500指数4600个基点。这不是一个温和的调整——它是全医疗健康板块中最差的细分领域，幅度远超生物科技、生命科学工具甚至管理式医疗。市盈率从去年11月至今被砍掉了30%，回到2017年之前的水平。\n\n如果你只看这些数字，很容易得出一个结论：医疗器械的基本面出了大问题。\n\n但Bernstein这份由九位分析师联合署名的周末深度报告，给出了一个反直觉的判断：基本面没有问题。问题出在“故事”上。\n\n这份报告的核心主张是：医疗器械公司的基本面依然扎实，但每一家公司的“故事”都变得比一年前复杂得多。在一个AI主题吸走几乎所有注意力的市场里，投资者对“有瑕疵的故事”几乎没有耐心。于是，整个板块被集体抛售，不分好坏。\n\n这不是一个行业危机，这是一个叙事危机。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 波士顿科学的坠落是理解整个板块的关键\n\n要理解医疗器械板块的溃败，必须先理解波士顿科学（BSX）发生了什么。这家公司曾是板块中最闪耀的明星，市盈率在2025年初一度超过36倍。如今，这个数字跌到了12.5倍。\n\n发生了什么？两个核心产品线出了问题。\n\nFarapulse（脉冲场消融）和Watchman（左心耳封堵器）是BSX过去两年增长的双引擎。2024和2025年，公司有机增长率冲到16%，这是医疗设备公司罕见的增速。Farapulse让BSX的电生理业务从2023年的8亿美元暴涨到2025年的33亿美元；Watchman的收入则在三年内从10亿美元翻倍到20亿美元。\n\n转折点出现在2025年下半年。随着PFA领域的竞争加剧，BSX的电生理增长开始减速。2025年第四季度，美国电生理销售低于预期6%，Watchman的有机增长\n\n[... middle omitted ...]\n\n二阶影响，这些是决定你是否应该在这个估值水平出手的关键变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n医疗板块跌到怀疑人生？真相在这里\n\n💉医疗科技，跌够了没？\n\n过去一年，美国医疗科技板块跑输标普500近5000个基点，估值被砍了30%。很多朋友问：这个赛道是不是凉了？\n\n**1/ 真正的问题不在基本面**\n研报观点很清晰：不是行业出问题，而是个股故事变复杂了。\n医院手术量依然稳健，公司财报也说“需求健康”。真正的压力来自——\n当AI故事太耀眼，投资者对“有瑕疵”的医疗股耐心为零。\n\n**2/ 几家龙头各有各的烦恼**\n- 波士顿科学：Farapulse+Watchman两大王牌增速放缓，管理层一季度就下调全年指引\n- 雅培：营养品业务意外下滑，CGM增速放缓\n- 史赛克：3月遭网络攻击，Q1收入低于预期\n- Insulet：胰岛素泵出现制造问题，股价跌46%\n- 直觉外科：业绩依然强劲，但整个板块估值被拖累\n\n**3/ 什么能拯救医疗科技？**\n不是某个单一催化剂。\n研报认为：需要AI热潮降温、资金轮动；更需要这些公司一个个解决自己的问题——史赛克交出超预期Q2、雅培营养品恢复增长、直觉外科的新产品持续发力。\n\n**4/ 估值回到10年低位**\n多数优质公司估值已大幅回落。对于愿意接受“有点复杂”故事的投\n\n[... middle omitted ...]\n\nogi, Ph.D. +81 3 6777 6991 miki.sogi@bernsteinsg.com\n\nLance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com\n\nJeffrey Walch, MD, Ph.D. +1 917 344 8613 jeffrey.walch@bernsteinsg.com\n\n## Spec\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R038",
    "title": "国际货币基金组织：IMF：中国房地产的“小冲击”为什么会有大后果",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：中国房地产的“小冲击”为什么会有大后果\n\n中国房地产市场的调整已经持续了近五年。多数市场参与者已经接受了“行业规模收缩”这个事实，但真正值得追问的问题是：当风险集中在特定类型的开发商和区域性金融机构时，这些看起来“体量不大”的压力点，会不会通过金融体系内部的连锁反应，演变成宏观经济的系统性冲击？\n\n国际货币基金组织（IMF）在2026年6月发布的一份工作论文，给出了一个反直觉的回答：是的，而且这种传导机制比大多数人想象的更隐蔽、更持久。这篇题为《Assessing Macrofinancial Linkages in China Using a Machine-Learned Parsimonious VAR Model》的报告，由三位经济学家运用机器学习优化的向量自回归模型，精确量化了从微观压力到宏观冲击的传导链条。\n\n核心结论值得每一个关注中国资产定价的人认真对待：中国金融体系与房地产之间的“宏观金融关联”，远比资产负债表上显示的贷款敞口更复杂。压力可以通过共同风险暴露、市场情绪传染、以及业务模式相似性等非贷款渠道传播，而后者恰恰是目前监管和市场分析中最容易被忽视的部分。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 模型揭示的真相：压力传导不靠贷款，靠“看不见的网”\n\n传统上，分析房地产与金融体系之间的关联，主要依赖银行对开发商的贷款敞口数据。但这篇报告指出，这种分析框架存在严重盲区。IMF团队采用的是一种基于违约概率（PD）的复合指数，覆盖了中国所有上市房地产开发商和金融机构。与CDS利差或股价等纯市场指标不同，PD指数同时包含了市场信号（股价、波动率）和基本面信息（流动性、盈利能力、杠杆率），更能反映真实的部门健康度。\n\n更重要的是，PD指数的共同波动能捕捉到超越借贷关系的关联性—\n\n[... middle omitted ...]\n\n整研报解读与原始图表，与我们一起持续追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n房价波动如何传导到银行系统？\n\n**房价—银行—经济**\n\n房价波动不只影响买房人\n\n某外资投行最新研报用机器学习跑了一套模型，把中国地产商、金融机构和宏观经济的关联拆得挺清楚。\n\n**核心发现：**\n\n1️⃣ **民企开发商是风险放大器**\n研报用违约概率（PD）指标做分析，发现民企开发商的压力会传导到国企开发商和金融机构。规模不大，但影响持久——通过贷款关系、共同敞口和市场情绪形成连锁反应。\n\n2️⃣ **区域小银行也能捅娄子**\n别只看大行。城商行这类区域性金融机构，一旦承压，冲击会通过同业市场和信贷渠道扩散。模型显示，它们的PD波动对整体系统有显著影响。\n\n3️⃣ **房价是连接器**\n房价下跌→投资萎缩→消费者信心下滑→银行资产质量恶化→信贷收缩→经济放缓。这个循环一旦启动，靠单一政策很难打断。\n\n**模型亮点：**\n用了零范数惩罚的VAR模型（机器学习帮忙降维），不是黑箱。只保留显著关系，能看清谁影响谁、影响多久。\n\n**政策启示：**\n稳定房价要和恢复信心一起做。光托市没用，得让市场主体（开发商、银行、消费者）的资产负债表都健康起来。\n\n你们觉得，当前政策工具箱里，哪个工具最能打断这个负循环？\n\n[... middle omitted ...]\n\nepartment\n\nAssessing Macrofinancial Linkages in China Using a Machine-Learned Parsimonious VAR Model Prepared by Jin-Chuan Duan\\*, Dimitrios Laliotis\\*\\*, and Wei Sun\\*\\*,\n\nAuthorized for dist\n\n[... middle omitted ...]\n\n20.\n\nZou, H. (2006), “The Adaptive Lasso and Its Oracle Properties”, Journal of the American Statistical Association, 101(476), 1418-1429.\n\n![](images/d4b8a1b010a95febf540ebf94da51f185830cab5acb4a8a6b5178316da0c5ae0.jpg)"
  },
  {
    "id": "R039",
    "title": "国际货币基金组织：IMF：巴西增值税改革的最大受益者不是穷人，而是服务税",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：巴西增值税改革的最大受益者不是穷人，而是服务税\n\n巴西2023年通过的增值税改革，被广泛视为一项里程碑式的税制简化工程。然而，国际货币基金组织（IMF）最新发布的Working Paper WP/26/132揭示了一个更值得关注的判断：这项改革虽然旨在改善税制公平，但其最显著的公平性改善并非来自对穷人的直接减税，而是来自税负从商品向服务的结构性转移——这实际上是向高收入群体征税。\n\n这份报告的核心价值在于，它用微观模拟数据拆解了每一项政策工具的真实分配效应，并给出了一个反直觉的结论：如果只关注改革已批准的减税措施，反而会加剧累退性；真正改善公平的，是那些不直接针对穷人的结构性变化。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 改革后的税负分布：穷人依然最重，但差距在缩小\n\n报告基于2018年巴西家庭调查数据，模拟了改革后不同收入分位组的增值税负担变化。核心发现是：改革后，最贫困的10%家庭仍然承担着最高的相对税负——其增值税支出占可支配收入的比重约为25%，而最富裕的10%家庭这一比例仅为10%左右。\n\n但这并不意味着改革无效。与改革前的税制相比，最贫困的三个分位组的税负下降了约7个百分点。更重要的是，这种改善并非均匀分布：中低收入群体（第2至第5分位组）的税负下降最为明显，而最贫困10%家庭的改善幅度相对有限。\n\n> **KC评论：** 这意味着改革在公平性上的“边际改善”主要惠及了“接近贫困线”的群体，而非最底层的极端贫困人口。完整报告中的图6清晰展示了这种非线性改善，值得仔细对比改革前后的税负曲线形状变化。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 减税措施的真实效果：零税率和现金返还有效，但低税率适得其反\n\n报告将改革中的各项政策工具拆开分\n\n[... middle omitted ...]\n\n要，既方便您快速把握市场动态，也适合作为AI模型的训练素材。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n巴西增值税改革：穷人真的受益了吗？\n\n巴西税改的公平账\n\n新税制下，最穷的人还是负担最重\n\n---\n\n最近读了一份IMF的工作论文，讲的是巴西2023年通过的增值税改革。这个改革酝酿了30多年，核心是把五个复杂的消费税合并成一个双层的增值税加一个消费税。\n\n聊聊几个有意思的点：\n\n**1. 改革目标很清晰**\n- 消除现有税制的扭曲和复杂\n- 保持税收中性（不增加总体税负）\n- 改善公平性\n\n**2. 实际效果怎么样？**\n论文用微观模拟模型分析发现：\n- 新税制下，中低收入群体的税负分布相对公平\n- 但最穷的10%家庭，税负占可支配收入的比例仍然最高\n- 零税率（主要是基本食品篮）让底层三个收入组税负降低了约7%\n- 现金返还机制更关键，让穷人税负降低了近10%\n\n**3. 有意思的政策组合问题**\n- 降低某些商品税率反而加剧了累退性（因为高收入群体消费更多）\n- 从商品转向服务征税，因为服务消费更多集中在高收入群体，反而有利于公平\n- 但如果把所有优惠都取消，只扩大对最穷群体的现金返还，可以让他们的可支配收入增加25%，同时还能降低基准税率\n\n**4. 一个值得思考的角度**\n巴西税制改革面临一个经典困\n\n[... middle omitted ...]\n\nus\\*\n\nAuthorized for distribution by Daniel Leigh and Alexander Klemm\nJune 2026\n\nIMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to e\n\n[... middle omitted ...]\n\n, J-F., 2019. “The Optimal Turnover Threshold and Tax Rate for SMEs.” IMF Working Paper WP/19/98. Washington: International Monetary Fund.\n\n![](images/b6f58ec1fb82e8c1d4319a477653930b84a7e755fc9351821c3f6047ff93cb05.jpg)"
  },
  {
    "id": "R040",
    "title": "国际货币基金组织：IMF：欧洲央行正在分裂——先进经济体向前看，新兴经济体向后看",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：欧洲央行正在分裂——先进经济体向前看，新兴经济体向后看\n\n央行沟通，正在成为比利率本身更重要的政策工具。这是国际货币基金组织（IMF）最新工作论文的核心判断。在连续经历疫情、战争、地缘分裂和贸易摩擦之后，欧洲央行体系内部出现了一个被多数市场参与者忽视的分化：面对通胀不确定性，发达经济体的央行选择用更前瞻的语言锚定预期，而新兴经济体的央行却在向后看——更多依赖数据依赖和回溯性解释。这不是工具选择的差异，而是信用和制度能力的根本分野。\n\n这篇论文由IMF欧洲部的八位经济学家完成，基于2009年至2025年间二十家欧洲央行的沟通实践，结合AI文本挖掘构建了量化指标。它回答的核心问题是：当不确定性成为新常态，央行的沟通策略究竟在如何演化？而答案，对全球资产定价和利率路径判断有直接影响。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 沟通工具趋同，但透明度差距在扩大\n\n表面上看，欧洲各国央行的沟通工具箱已经高度一致：货币政策声明、新闻发布、在线平台几乎成为标配。但IMF的调查揭示了一个关键差异——发达经济体央行更愿意使用“前瞻性工具”：发布会议纪要、召开新闻发布会、公布利率路径预测、情景分析和扇形图。新兴经济体央行在这些工具的使用上明显保守。\n\n这不仅是技术问题。会议纪要和利率路径预测意味着更明确的政策信号，也意味着更少的政策灵活性。发达经济体央行之所以敢于使用这些工具，是因为它们有更高的制度信用作为背书——市场相信它们能兑现承诺。而新兴经济体央行一旦给出前瞻指引却无法兑现，代价是信用折价，这是它们承受不起的。\n\n> **KC评论：** 这一发现直接挑战了一个流行观点——“新兴市场央行沟通更灵活、更适应实时条件”。IMF的数据表明，灵活性有时不是优势，而是制度约束的产物。如果央行无法让市场相信它的前瞻\n\n[... middle omitted ...]\n\n径和全球资产定价的微观机制有持续兴趣，欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n央行怎么说话，比说什么还重要\n\n央行都在“说话”，但方式很不一样\n\n最近读到一份IMF的工作论文，用AI分析了2009-2025年欧洲20家央行的沟通风格变化，结论很有意思。\n\n**1/ 通胀越不确定，央行反而越“看过去”或“看未来”？**\n\n- 发达经济体央行在通胀不确定性上升时，会更多使用**前瞻性语言**（比如“预计未来利率路径”）\n- 新兴经济体央行则相反，转向**回顾性语言**（比如“基于已发生的数据”）\n\n**2/ 为什么会有这种分化？**\n\n核心是**信誉**和**制度能力**。\n- 发达经济体央行信誉高，市场相信它们的预测，所以敢说未来\n- 新兴经济体央行信誉基础较弱，说“未来会怎样”市场未必信，不如解释“过去为什么这么做”来建立信任\n\n**3/ 沟通工具包差不多，但用法差很多**\n\n- 发达经济体央行更常用：会议纪要、新闻发布会、利率路径图、情景分析\n- 新兴经济体央行更依赖：基础声明、官网发布\n\n**4/ 央行也会“惯性说话”**\n\n研究发现央行的沟通风格有很强的惯性——今天怎么说，明天大概率还这么说，除非遇到重大冲击（比如疫情、战争）。\n\n**5/ 市场怎么看？**\n\n- 央行沟通越前瞻\n\n[... middle omitted ...]\n\n2be7e88a996fd68d6a.jpg)\n\n# IMF Working Paper European Department\n\n# Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe\\*\n\nAuthorized for distri\n\n[... middle omitted ...]\n\nunication index: Robustness to dictionary  \nThis figure reports the backward-looking index excluding the terms related to data dependence.\n\n![](images/3860c88f179bca3b584a7839cdc3e9c655b75ee1c97a9e3db69b2ec8ee680919.jpg)"
  },
  {
    "id": "R041",
    "title": "国际货币基金组织：IMF：气候灾难正在改写主权债务违约的定价逻辑",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：气候灾难正在改写主权债务违约的定价逻辑\n\n一份来自国际货币基金组织（IMF）的最新工作论文，揭示了一个被市场严重低估的风险传导链条：气候灾难不是单纯的“自然灾害”，而是主权债务违约的独立驱动因子。报告用全球面板数据证明，当灾害损失占GDP比重每上升1个百分点，主权违约概率将增加约2-3%。更关键的是，报告提出了一个“不可能三角”——脆弱国家无法在不影响债务可持续性的前提下，完成气候适应的必要投资。\n\n这不是远期的ESG叙事，而是正在发生的资产负债表重构。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 灾害损失对违约概率的影响，比市场定价更直接\n\n传统主权信用分析中，气候风险往往被归入“尾部风险”或“长期结构性因素”，很少被直接纳入违约概率模型。而IMF这篇论文做了三件事：第一，用灾害事件层面的实际经济损失（而非ND-GAIN等结构性脆弱性指数）作为冲击变量；第二，采用专门针对“稀有事件”的logit估计方法，纠正传统模型对违约这类低频事件的低估；第三，将违约定义从信用评级下调或利差走阔，直接落到债务违约事件本身。\n\n结果非常清晰：灾害损失占GDP比重每提高1个百分点，下一年违约概率上升约2-3%。这个效应在控制了IMF项目干预、收入组别和年份固定效应后仍然稳健。更重要的是，分债权人类型的分析显示，违约风险上升并非均匀分布——对官方债权人（IMF、世界银行、巴黎俱乐部）的违约概率上升幅度，显著高于对私人债权人的违约。\n\n> **KC评论：** 这意味着，气候灾难后的债务重组不再是“市场选择”，而可能演变为“体制性违约”。对官方债权人的违约概率更高，说明脆弱国家在灾难后会优先保护商业债权人，而将官方债务作为缓冲垫。这对持有新兴市场主权债券的机构投资者而言，是一个需要重新定价的信号。\n\n![研报图\n\n[... middle omitted ...]\n\n息过载的时代，优先抓住那些真正改变资产定价逻辑的结构性信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n气候灾害正在变成“债务炸弹”\n\n🌪️ 灾害每多1%，违约风险就高3%\n\n你可能想不到，一场飓风或洪水，可能直接推高一个国家的债务违约概率。IMF最新工作论文揭示了一个残酷的“不可能三角”：气候脆弱国家既要投钱搞防灾基建，又要控制债务别爆表，还不能拖延适应——因为越拖，未来的违约风险越高。\n\n📉 数据触目惊心\n- 灾害损失占GDP每增加1个百分点，主权违约概率就上升约2-3%。\n- 2004年飓风“伊万”袭击格林纳达，损失高达GDP的200%，债务直接从80%飙到95%，被迫重组。\n- 2024年飓风“贝丽尔”又让该国损失了约三分之一的GDP。\n\n🔍 核心发现\n1️⃣ 灾害冲击→违约风险上升\n   - 研究用全球面板数据，发现灾害损失与次年违约概率显著正相关。即使是控制IMF救助项目后，结果依然稳健。\n\n2️⃣ 适应能力是关键缓冲\n   - 每10亿美元官方发展援助（ODA），能提升一国适应能力指数约0.13点。\n   - 适应能力越强，灾害造成的经济损失越小，违约概率也越低。\n\n3️⃣ 优惠融资是“解药”吗？\n   - 研究估算：如果用优惠贷款（低息、长期）来资助防灾基建，可以在不推高债务的前提下降低未来违约\n\n[... middle omitted ...]\n\nate Shocks, Debt Defaults and Investment in Climate Adaptation – Squaring an Impossible Trilemma Prepared by Constance de Soyres, Emmanuella Obeng and Joanne Tan\n\nAuthorized for distribution b\n\n[... middle omitted ...]\n\nndard errors in parentheses. Controls included but not reported. Country and Year FE included. \\* p < 0.10, \\*\\* p < 0.05, \\*\\*\\* p < 0.01\n\n![](images/0c1ef74c429dc79e89aefd910f4cdf6a0f4265452b715ed45a78625cfd70534b.jpg)"
  },
  {
    "id": "R042",
    "title": "国际货币基金组织：IMF：全球一半国家都在错误地定价燃油",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：全球一半国家都在错误地定价燃油\n\n当全球能源市场剧烈波动时，超过95个国家的政府选择用行政之手干预燃油价格。国际货币基金组织（IMF）最新发布的技术指南直接指出：这些干预措施几乎从未达成其宣称的目标，反而制造了隐蔽的财政黑洞、扭曲了市场信号，并催生了难以根除的寻租行为。\n\n这份题为《如何（不）为燃油产品定价》的报告，并非讨论是否应该对燃油征税或补贴，而是聚焦一个更基础、也更被忽视的问题：当政府决定干预燃油定价时，什么样的机制设计是有效的，什么样的做法注定失败。\n\n报告的核心判断简洁而有力：燃油定价的成功，不在于干预的力度，而在于干预的结构。透明、锚定国际价格、简单、一致——这四个原则决定了定价机制是帮助还是伤害一个经济体。\n\n这不仅仅是一份给财政部长或能源监管者的技术手册。对于任何关注宏观经济稳定、财政可持续性，或者希望通过理解政策设计逻辑来把握市场方向的人来说，这份报告提供了一个极具价值的分析框架。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 燃油定价的“标准答案”与全球现实之间的巨大鸿沟\n\nIMF报告首先构建了一个“参考价格”框架，作为判断各国燃油定价是否合理的基准。这个框架将燃油的最终消费价格分解为三个核心组成部分：产品可获得性（availability）、产品可及性（access）、产品销售（sale）。\n\n在理想状态下，一个完全自由化的燃油市场，其价格应该等于国际基准价格（如FOB价格）加上运输、保险、分销、零售等环节的供应链成本，再加上合法的关税、增值税和消费税。这个价格会随国际市场波动，向消费者传递准确的供需信号。\n\n然而现实是，全球一半国家通过各种方式干预这个价格形成过程。报告数据显示，2015年至2024年间，实施价格管制的国家，其柴油、高辛烷值汽油和煤油的平均消费价格，\n\n[... middle omitted ...]\n\n在于你设计了多么精巧的公式，而在于你是否敢于让价格回归真实。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球一半国家在“错误”地定价燃料\n\n燃料定价的四个原则\n\n看懂各国燃料价格背后的逻辑\n\n最近读了一篇IMF的研报，讲的是全球一半国家都在干预燃料价格，但效果往往适得其反。把核心逻辑拆给大家。\n\n1/ 为什么燃料价格这么重要？\n燃料占全球能源供应的25%，2023年汽油和柴油消费约占全球GDP的6%。价格波动直接影响通胀、竞争力和宏观稳定。\n\n2/ 常见的干预方式\n- 保护消费者免受价格波动\n- 维持燃料可负担性\n- 保障供应安全\n- 实现社会或政治目标\n\n但这些干预很少真正达成目标，反而带来走私、效率低下等副作用。\n\n3/ 燃料参考价格的三层结构\n- 产品可得性：国际市场价格+运费+保险费\n- 产品可及性：分销+零售成本\n- 产品销售：关税+增值税+消费税\n\n4/ 四个核心原则\n- 透明：定期公开所有价格构成\n- 锚定国际价格：国内价格应反映国际波动\n- 简单：干预措施要精简，避免附加税\n- 一致：类似燃料应适用类似定价规则\n\n5/ 一个关键洞察\n燃料需求弹性低，统一征税是有效的财政收入来源。但很多国家通过复杂的价格公式和补贴，反而造成了更大的财政负担。\n\n想和大家讨论：你们国家的燃料定价是怎样的？有没有遇到\n\n[... middle omitted ...]\n\nCLAIMER:\n\nHow-To Notes offer practical advice from IMF staff members to policymakers on important issues. The views expressed in How-To Notes are those of the author(s) and do not necessarily re\n\n[... middle omitted ...]\n\nWorld Bank. 2025. Global Landscape of Fuel Subsidies and Price Controls. Washington, DC: World Bank.\n\nThis page intentionally left blank\n\n![](images/289b532a2092f724d12b702ea6877dc2fe22f3e673e88dd37e7cdf19f2c39ef7.jpg)"
  },
  {
    "id": "R043",
    "title": "国际货币基金组织：性别预算声明正在成为财政透明度的新标尺",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：性别预算声明正在成为财政透明度的新标尺\n\n当全球超过100个国家的财政部长在年度预算中，越来越多地加入一份名为“性别预算声明”的文件时，一个值得关注的趋势已经形成：财政透明度正在从“钱花在哪里”延伸到“钱对不同群体的影响是什么”。国际货币基金组织（IMF）在其最新发布的《如何准备性别预算声明》技术指南中，系统梳理了这一工具的设计逻辑、全球实践与实施路径。这份报告的核心判断是：性别预算声明不仅是一项社会政策工具，更正在成为衡量政府财政管理成熟度的新维度。\n\n对于关注公共财政改革、ESG投资以及政府治理效率的读者而言，这份报告提供了一个观察政府预算透明度和问责机制演进的独特窗口。它揭示了一个重要信号：当越来越多的政府承诺将性别平等纳入预算决策时，财政数据的颗粒度、政策评估的深度以及公众监督的广度都在发生结构性变化。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 性别预算声明的本质不是“女性预算”，而是财政透明度的升级\n\nIMF报告开宗明义：性别预算声明是一份透明度和问责文件，政府通过它向立法机构和公众沟通预算如何致力于改善性别平等。它并非另起炉灶的“女性预算”，而是将性别视角嵌入现有预算流程的产物。\n\n从全球实践来看，截至2024年，IMF调查的100多个国家中，约三分之一的国家已开始编制某种形式的性别预算声明，其中超过四分之三的声明已公开出版。亚太地区（如澳大利亚、印度、韩国）和非洲（如多哥、津巴布韦）是主要实践者，分别占32%和28%。这一分布本身就说明：性别预算声明的推广并不完全与经济发展水平正相关，政治意愿和制度设计才是关键变量。\n\n> **KC评论：** 对于投资者而言，这一趋势意味着什么？当政府预算开始系统性地披露性别影响时，公共支出数据的透明度和可预测性将提高。那些能够率先建立高质量性别预\n\n[... middle omitted ...]\n\n观经济政策的衔接——这些正是当前全球公共财政改革的前沿议题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n预算报告里的“性别账本”\n\n性别预算报告\n\n让每一笔财政支出都算上性别账\n\n---\n\n预算不只是数字游戏，它直接影响每个人。\n\n最近读到IMF一篇关于“性别预算报告”的研报，发现很多国家正在把性别平等写进财政文件里。\n\n**什么是性别预算报告？**\n\n它不是独立的财务文件，而是政府预算的附件。核心就一件事：把预算对性别平等的影响讲清楚——哪些政策、花了多少钱、想解决什么问题。\n\n**为什么需要它？**\n\n1. **透明**：预算花在哪、对谁有利，公开可查\n2. **问责**：政策有没有效果，有指标可追踪\n3. **共识**：让各部门对性别差距有统一认知\n\n**报告里通常写什么？**\n\n- 当前性别差距数据（比如女性劳动参与率）\n- 政府承诺和优先目标\n- 具体政策和预算分配\n- 预期影响和衡量指标（更进阶的做法）\n\n**各国怎么做？**\n\n澳大利亚是先行者（80年代就开始了），韩国、印尼、多哥等从试点做起。不同国家叫法不同——“妇女预算报告”“性别影响报告”都有。\n\n一个有意思的发现：亚洲和非洲国家更积极采用，欧洲反而相对保守。\n\n**怎么开始做？**\n\n研报建议分阶段推进：\n- 先挑几个关键领域试点\n- 用\n\n[... middle omitted ...]\n\nalena Tomczynska-Smith, Gemma Preston, Virginia Alonso Albarran, Laura Gores, Teresa Curristine, and Chloe Cho\nHTN/2026/02\n\n## DISCLAIMER:\n\nHow-To Notes offer practical advice from IMF staff m\n\n[... middle omitted ...]\n\nap Report 2022.\" https://www3.weforum.org/docs/WEF\\_GGGR\\_2022.pdf\n\nThis page intentionally left blank\n\nThis page intentionally left blank\n\n![](images/f3c83800c512ce13f77d170746497ebf6783fdc96fcd3ae8a671a62bc6e6c799.jpg)"
  },
  {
    "id": "R044",
    "title": "国际货币基金组织：IMF：汇率篮子不该只看贸易权重，波动才是真正的成本",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：汇率篮子不该只看贸易权重，波动才是真正的成本\n\n国际货币基金组织（IMF）最新工作论文（WP/26/131）提出一个反直觉的判断：当前多数小国开放经济体采用的贸易权重汇率篮子，并非最优设计。论文作者Etienne Vaccaro-Grange将现代投资组合理论中Markowitz最小方差框架，移植到汇率传导空间，证明一个核心结论——通过优化篮子权重，可以在不改变汇率对国内物价长期传导总量的前提下，将进口通胀的波动性降低约20%。\n\n这个结论的意义远不止于太平洋岛国斐济的案例。它指向一个更深层的追问：在全球化退潮、供应链重构、各国央行重新审视物价稳定目标的大背景下，汇率制度设计是否正在经历一次范式转换？贸易权重这个看似“客观”的锚，是否正在成为通胀管理中的盲点？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 贸易权重是“过去的结构”，而非“最优的解”\n\n当前主流做法是将汇率篮子权重与贸易伙伴的进出口份额挂钩。这种做法有三个直观优势：透明、可操作、与实体经济结构对应。但IMF这篇论文指出，贸易权重只描述了“从哪里买”，却没有回答“买来的价格波动有多大”以及“这种波动如何传导到国内物价”。\n\n问题的核心在于：不同货币的汇率波动对国内进口通胀的传导效率并不相同。美元波动对斐济进口价格的影响，与澳元波动的影响，存在系统性差异。更重要的是，各货币之间的汇率变动存在复杂的协方差结构——当某种货币升值时，另一种可能贬值，这种相关性能否被用来对冲通胀风险，在贸易权重框架下完全被忽略。\n\n> **KC评论：** 这就像用一个只看营收占比的指数基金去配置资产，完全不考虑各资产的风险和相关性。贸易权重是“外生的结构”，而通胀管理需要“内生的风险优化”。完整报告中对斐济案例的实证分析，展示了这种差异究竟有多大。\n\n!\n\n[... middle omitted ...]\n\n原始图表、数据表格和计量细节，并持续跟踪相关讨论和后续研究。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n小国货币锚，换种算法更稳\n\n**重新定义货币篮子**\n\n**汇率波动对通胀的影响，比想象中更可控**\n\n最近读了一篇IMF的工作论文，讲小国经济体如何优化货币篮子权重。结论很直接：**按贸易份额定权重，不一定最稳。**\n\n核心逻辑是这样：\n\n1️⃣ **传统做法看贸易，但忽略了传导差异**\n很多小国把本币锚定一篮子外币，权重按贸易伙伴的进出口份额来分。这种方法直观，但没考虑一个关键变量——**不同货币的汇率变动，传导到国内进口通胀的程度不一样**。有的货币贬10%，进口价格只涨5%；有的能涨8%。如果只看贸易量，可能给了“高传导”货币过高的权重，反而放大通胀波动。\n\n2️⃣ **新框架：最小化进口通胀的方差**\n这篇论文直接把问题转化成一个“最小方差组合”问题——类似于金融里Markowitz的均值-方差模型。只不过这里“资产”是不同外币，“收益”是汇率变动对进口通胀的传导系数，“组合”就是货币篮子权重。\n目标：**在保持篮子累计传导率不变的前提下，让进口通胀的波动最小**。\n\n3️⃣ **实证案例：斐济，降波动20%**\n作者用斐济的数据跑了一遍。斐济是个进口密集型岛国，篮子里有5种货币（澳元、新西兰元、美\n\n[... middle omitted ...]\n\nd for distribution by Romain Veyrune\nApril 2026\n\nIMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expre\n\n[... middle omitted ...]\n\nw Exchange Rate Regime, Optimal Basket Currency and Currency Diversification.” MPRA Paper No. 32642. Munich: University Library of Munich.\n\n![](images/0939fa876f8dec0794694b1ecf1e44ac6284d125164603b9cb6b9385faa22687.jpg)"
  },
  {
    "id": "R045",
    "title": "国际货币基金组织：产业链位置决定了美联储加息与降息谁更有效",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：产业链位置决定了美联储加息与降息谁更有效\n\n货币政策传导机制的研究，长期以来都隐含着一个假设：无论利率上升还是下降，其作用于经济的路径是对称的。但现实世界的价格调整从来不是对称的——汽油价格“火箭般”上涨、却“羽毛般”下跌的现象，早已被经济学家记录为“火箭与羽毛”效应。\n\n国际货币基金组织最新发布的工作论文（WP/26/127）将这一不对称性嵌入到生产网络框架中，得出了一个对产业决策者和投资者都极具冲击力的结论：产业链上游与下游企业对货币政策的反应存在系统性差异，而这种差异在加息和降息时截然不同。降息带来的价格效应是加息的数倍，而加息对下游企业的真实产出冲击却远大于上游。\n\n这份报告的核心贡献在于：它不仅仅是发现了“产业链位置影响货币政策传导”这一现象，更通过精巧的反事实分解，揭示了背后的主导机制并非通常认为的成本传导链条，而是由产业链位置决定的价格调整频率差异。这意味着，任何改变产业链结构的政策或趋势——贸易协定、垂直整合、平台经济——都在悄然改变货币政策的效力。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 上游企业价格更灵活，因为它们的客户不是消费者\n\n报告首先建立了一个基础事实：在美国经济中，越远离最终消费者的上游产业，其价格调整频率越高。这一结论来自对271个六位数NAICS行业月度生产者价格指数的分析。\n\n为什么上游企业调价更频繁？原因并不复杂。上游企业的主要客户是其他企业，而非终端消费者。企业客户在采购谈判中更关注价格条款，价格粘性天然更低。相反，面向消费者的下游企业面临菜单成本更高，调价更为谨慎。\n\n> **KC评论：** 这一发现看似直观，但其政策含义常被忽视。当美联储加息时，上游企业可以更快地将成本压力转嫁出去，而下游企业只能通过压缩利润或减少产出应对。这意味着，加息对下游企业的\n\n[... middle omitted ...]\n\n动态。欢迎加入我们的社群，获取这份报告的完整解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n生产网络里的价格秘密\n\n离消费者越远，价格越灵活\n\n货币政策传导的“上游优势”\n\n---\n\n最近读到一篇IMF的研报，讲的是生产网络如何影响货币政策的传导。简单说就是：美联储加息或降息，这个冲击沿着产业链传递时，不同位置的企业反应完全不一样。\n\n**1. 上游企业更“灵活”**\n离最终消费者越远的行业（比如原材料、零部件），价格调整越频繁。因为它们主要卖给其他企业，B2B价格本来就更灵活。数据显示，上游行业对货币政策的累计价格反应，比下游行业高出约2.8个百分点。\n\n**2. 不是成本传导，是定价习惯**\n很多人以为上游涨价会顺着供应链往下传。但研究发现，真正的原因是上游企业本身定价更灵活，而不是成本在链条里层层传递。这个叫“灵活性渠道”，而非“成本级联渠道”。\n\n**3. 不对称的“火箭与羽毛”**\n降息时，上游价格涨得又快又猛；加息时，上游价格却降得又慢又少。这种不对称性在产业链里被放大了——链条越长，不对称越明显。说明通胀容易制造，通缩却很难。\n\n**4. 对实体经济的暗示**\n价格灵活的上游企业，更多通过调价吸收冲击，保住了产量；价格粘性的下游企业，只能通过减产来应对。这种分化在紧缩时尤其明显。\n\n一\n\n[... middle omitted ...]\n\nPolicy\n\nPrepared by Francesco Grigoli\\*\n\nAuthorized for distribution by Antonio Spilimbergo\nJune 2026\n\nIMF Working Papers describe research in progress by the author(s) and are published to el\n\n[... middle omitted ...]\n\nne lag of own-industry PPI inflation. Driscoll-Kraay standard errors in parentheses. \\*\\*\\* $p < 0.01$ ; \\*\\* $p < 0.05$ ; \\* $p < 0.10$ .\n\n![](images/2850b1c437d653b3c5232e4277da7db48abaf6aa77ba5a3c46e6b0d8db20474f.jpg)"
  },
  {
    "id": "R046",
    "title": "国际货币基金组织：IMF：稳定币越流行，经济波动越大——但有一把“调节阀”",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：稳定币越流行，经济波动越大——但有一把“调节阀”\n\n2025年7月，美国GENIUS Act正式签署成为法律；一个月后，香港《稳定币条例》生效。全球两大金融中心几乎同时为稳定币铺好了监管轨道。但一个根本问题仍然悬而未决：当稳定币从边缘资产变成支付系统的一部分，宏观经济会变得更稳定，还是更脆弱？\n\n国际货币基金组织（IMF）在2026年6月发布的工作论文《Stablecoins and Macroeconomic Stability: A DSGE Investigation》给出了一个清晰且反直觉的答案。这是IMF首次用动态随机一般均衡（DSGE）模型对稳定币进行系统性宏观分析。结论并不温和：稳定币渗透率越高，经济面对冲击时的波动越大。但论文同时发现，有一种政策工具可以充当“调节阀”——稳定币与法定储备资产的比率要求，类似于银行的流动性覆盖率。\n\n这份报告的价值不在于它发现了稳定币有风险——这一点市场早已有共识。它的独特之处在于：它把“稳定币如何放大宏观波动”这个模糊担忧，变成了一个可以被量化、被模拟、被政策校准的机制。对于正在制定数字资产监管框架的政策制定者，以及试图理解未来支付格局的投资者，这篇论文提供了一套必须认真对待的理论基础。\n\n> **KC评论：** 这篇论文的核心不是“稳定币好不好”，而是“如果稳定币真的成为日常支付工具，传统货币政策工具还能不能有效传导”。它用模型告诉你，答案是否定的——而且这种失效会随着稳定币使用率的上升而加速。完整报告中的脉冲响应图清晰地展示了这一非线性关系，值得细读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 模型揭示的核心机制：稳定币放大了所有宏观变量的波动\n\n论文构建了一个两部门模型。一个部门是传统的实体经济，使用法定货币进行交易；另一个部门是去\n\n[... middle omitted ...]\n\n欢迎加入我们的社群，每日更新的研报解读中会包含这些关键素材。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n稳定币，真的稳定吗？\n\n**稳定币的宏观风险**\n\nIMF最新DSGE模型揭秘\n\n最近读到一份IMF的工作论文，用DSGE模型拆解了稳定币对宏观经济的真实影响，结论很有意思。\n\n1️⃣ **稳定币≠更稳定**\n模型显示，稳定币渗透率越高，主要宏观变量的波动反而越大。它并没有像名字暗示的那样“稳定”经济，反而放大了外部冲击的传导效应。\n\n2️⃣ **货币竞争真实存在**\n研究发现，法币和稳定币之间存在明显的“货币替代效应”。当稳定币更方便、交易成本更低时，人们会主动切换支付工具，这种竞争会影响央行货币政策的有效性。\n\n3️⃣ **监管可以当“稳定器”**\n好消息是，审慎监管（比如要求稳定币发行方保持足够的储备资产比例，类似银行的流动性要求）能有效抑制这种额外波动。模型证明，这类监管工具可以充当“减震器”，平滑经济周期。\n\n4️⃣ **模型设计很有创意**\n研究者把稳定币嵌入了一个“双重经济”框架：实体经济用法币，虚拟经济（DeFi场景）用稳定币。这种分割设计很贴合现实，因为链上交易确实需要稳定币作为媒介。\n\n5️⃣ **政策启示明确**\n结论支持对稳定币实施类似银行业的审慎监管框架。GENIUS法案和香港稳定币\n\n[... middle omitted ...]\n\nDSGE Investigation Prepared by Hui He, Yao Zhao, and Dayong Zhou\n\nAuthorized for distribution by Oana Croitoru\nJune 2026\n\nIMF Working Papers describe research in progress by the author(s) and \n\n[... middle omitted ...]\n\ne</td><td>3.0998</td><td>3.7476</td><td>4.8342</td></tr></table>\n\nTable 11: Macro stability for different values of $\\nu$ : Kalai solution\n\n![](images/85c1468092f1d0674dab833d9921c446c166ceca932aea4ce190ea463c09a7cd.jpg)"
  },
  {
    "id": "R047",
    "title": "国际货币基金组织：选举年，新兴市场央行正在用外汇储备买选票",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：选举年，新兴市场央行正在用外汇储备买选票\n\n一份来自国际货币基金组织的最新工作论文，揭示了一个长期被市场忽视但影响深远的现象：在新兴市场国家，大选前的外汇干预力度会显著加大，央行倾向于抛售美元、支撑本币，目的是维护选民购买力。这不是简单的市场行为，而是政治经济周期在外汇政策领域的直接体现。\n\n这份研报的核心判断是：新兴市场央行在外汇市场上的操作，并不总是纯粹基于经济基本面或汇率稳定目标。当选举临近，政治压力会显著改变干预的规模和频率。对于关注新兴市场资产定价、汇率走势和主权风险的投资者而言，理解这一机制，比单纯跟踪央行资产负债表更具前瞻意义。\n\n为什么现在需要关注这个问题？全球通胀回落周期中，新兴市场货币普遍面临升值压力，但选举年的到来可能改变央行的行为逻辑——他们更倾向于“逆风干预”，即在本币贬值时卖出美元，而不是在本币升值时买入美元。这种非对称操作，会加速外汇储备的消耗，削弱央行应对未来冲击的缓冲垫。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 选举前的外汇抛售，规模远超市场预期\n\n研报基于28个国家（17个新兴市场和11个发达经济体）2000年至2019年的月度数据，发现了一个统计上显著且经济含义明确的规律：新兴市场国家在大选前1到3个月，外汇抛售的规模和频率显著高于选举后同期。\n\n具体而言，在竞争性选举的新兴市场，选举前月份的外汇抛售量比选举后月份高出约0.3至0.5个百分点的GDP。考虑到这些国家外汇储备占GDP的比例通常在10%到30%之间，这意味着选举周期可能消耗掉储备的1%到3%。这个数字看似不大，但考虑到干预的集中性和时效性，其对市场预期的冲击不可小觑。\n\n> **KC评论：** 这个发现最值得投资者注意的地方在于，它揭示了央行行为的一种“政治季节性”。如果你投资的新兴市场国家即\n\n[... middle omitted ...]\n\n干预行为？后疫情时代的新兴市场央行为何行为模式可能已经改变？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n选前稳汇率，央行的小算盘\n\n央行会在大选前卖外汇稳汇率吗？\n\n📌 最近读到一篇IMF工作论文，讲的是外汇干预背后的政治经济学，逻辑挺有意思的。\n\n简单来说，论文发现：\n\n1️⃣ 选举前，新兴市场国家的央行更倾向于卖出外汇储备，来“托住”本币汇率。因为汇率贬值=老百姓购买力下降=政府支持率下降，这个逻辑太直白了。\n\n2️⃣ 这种操作在“竞争激烈”的选举中尤其明显。越是选情焦灼，央行越可能下场干预，让本币别跌太惨。\n\n3️⃣ 更关键的是，论文发现：**货币政策透明度越高，这种“选前干预”冲动就越弱。** 透明公开的央行，不容易被政治压力绑架。\n\n4️⃣ 一个有意思的细节：论文还发现，这种外汇卖出操作之后，政府支持率确实会短暂上升。所以这不是阴谋论，是实打实的“政治经济周期”。\n\n💡 研报给出的政策建议也很实在：与其靠“选前卖外汇”来维稳，不如建立清晰的外汇干预规则。比如设定一个汇率波动的“安全区间”，到了就自动触发干预，这样既透明又公平。\n\n#学习笔记\n\n[source_mineru.md]\n# The Political Economy of Foreign Exchange Interventions\n\nKo\n\n[... middle omitted ...]\n\n Eklou\n\nAuthorized for distribution by Lamin Leigh\nJune 2026\n\nIMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. Th\n\n[... middle omitted ...]\n\nle” one: A novel measure of central bank independence and its effect on inflation. Journal of Money, Credit and Banking, 43(6), 1185-1215.\n\n![](images/bc3a37dc607c8968808a762f5b701be7951cb6703488cfab24eb32e1d2078b45.jpg)"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Cole Langlois The global economy has remained resilient despite numerous headwinds. Whether measured by PMIs (Figure 1), the performance of equities or surprise indices, global activity metrics have remained broadly consistent with moderate growth not too far "
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "The global economy has remained resilient despite numerous headwinds. Whether measured by PMIs (Figure 1), the performance of equities or surprise indices, global activity metrics have remained broadly consistent with moderate growth not too far below trend. T"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "\\*Net number of hikes or cuts across 27 central banks. The Strait of Hormuz should re-open... Negotiations between previously warring parties will hopefully lead to sustained higher Strait of Hormuz (SoH) vessel flows after four months of substantially reduced"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "The Strait of Hormuz should re-open... Negotiations between previously warring parties will hopefully lead to sustained higher Strait of Hormuz (SoH) vessel flows after four months of substantially reduced crossing (Figure 3). Even if the recent agreement prov"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "\\* Dotted bars indicate Citi forecasts. ## Implications for Macroeconomic Projections The US-Iran interim agreement has eased key headwinds for the global economy, with Brent oil prices declining towards \\$75/barrel. That said, the jury is still out on whether"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "The US-Iran interim agreement has eased key headwinds for the global economy, with Brent oil prices declining towards \\$75/barrel. That said, the jury is still out on whether this resolution proves lasting, with thorny issues remaining — particularly regarding"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 7",
    "context": "\\*Dotted bars indicate Citi forecasts. Figure 7. 2026 Growth Forecasts: Delta Since Feb (Citi) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Global Headline Inflation (Annual Average)\\* Figure 9. 2026 Headline Inflation Foreca"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Global Headline Inflation (Annual Average)\\* Figure 9. 2026 Headline Inflation Forecast Revisions (Citi)\\* © 2026 Citi Inc. No redistribution without Citi's written permission. \\*C"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Figure 9",
    "context": "At the country level, the mark-ups in our inflation forecasts have been significant and broad-based (Figure 9). The largest mark-ups have been among Asian economies — including the Philippines, Thailand, and Vietnam — which have all been revised up by 1½ ppt o"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Figure 10",
    "context": "Figure 10. El Niño and Precipitation Figure 11. ENSO Strength Probabilities (issued June 2026) © 2026 Citi Inc. No redistribution without Citi's written permission. ## Potential economic impacts of El Niño El Niño significantly impacts the global economy by di"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Figure 12",
    "context": "For central banks, the response is less clear. As an isolated event, El Niño can be a relative price shock for agricultural commodities. Energy provision can also be affected when this depends on hydro sources. The headline inflation impact can usually be igno"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Figure 12",
    "context": "Figure 12. Sea Temps & Global Output Loss: El Niño Events © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. Sea Surface Temperatures: Forecasts\\* © 2026 Citi Inc. No redistribution without Citi's written permission. \\*Based on th"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Figure 14",
    "context": "## Asia El Niño tends to lead to intense heat and drought conditions in Southeast Asia (Vietnam, Indonesia, the Philippines), below normal monsoons in India, Pakistan and Sri Lanka, while providing a more mixed pattern for China, where we see drought condition"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Figure 14",
    "context": "El Niño tends to lead to intense heat and drought conditions in Southeast Asia (Vietnam, Indonesia, the Philippines), below normal monsoons in India, Pakistan and Sri Lanka, while providing a more mixed pattern for China, where we see drought conditions in the"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "Figure 16",
    "context": "We find a dramatic amplification of the inflationary response when El Niño arrives during an already-elevated inflation environment. Headline inflation responses in the El Niño state are 2 to 17 times larger than the unconditional average, with Colombia's resu"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "Figure 16",
    "context": "Brazil and Peru show significant amplification. Brazil's fast response (+1.47 pp at month 2) is consistent with the northeast drought channel affecting coffee, sugar, and citrus prices, while Peru show an accumulate response +1.15 pp at month 6 (Figures 18 & 1"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "Figure 17",
    "context": "Figure 18. Brazil's fast response to El Niño © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 19. Peru is affected through fishing channel © 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "Figure 18",
    "context": "Figure 18. Brazil's fast response to El Niño © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 19. Peru is affected through fishing channel © 2026 Citi Inc. No redistribution without Citi's written permission. ## Global Commodities: "
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "Figure 20",
    "context": "Agriculture price risks are heavily skewed to the upside over the next 6-12 months, as they face major supply risks resulting from high fertilizer prices and from likely poor weather related to El Niño (with the only question being how bad the weather impact w"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "Figure 22",
    "context": "■ Warmer Winters: In the northern United States and Canada. These shifts in temperature and precipitation are the primary drivers of El Niño's impact on agriculture, which are explored below. ICE soft commodities are highly exposed to a significant disruption "
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "Figure 44",
    "context": "■ Global Recommendations: For now, our price targets still see upside to year-end across major, boosted by solid EPS growth. We remain Overweight on the US market and global Tech in our equity allocation. Other preferred global sectors include Materials and He"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Front-end skew has rotated back towards receivers as Fed pricing has moderated from the hawkish extremes Exhibit 2: Current front-end steepness tends to see vol undershoot what is implied by macro fundamentals 2y1y/1y"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Front-end skew has rotated back towards receivers as Fed pricing has moderated from the hawkish extremes Exhibit 2: Current front-end steepness tends to see vol undershoot what is implied by macro fundamentals 2y1y/1y"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 3: Appetite for funding has declined amid compressed Treasury futures bases, evidenced by dwindling levered fund shorts Exhibit 4: With limited pass-through from higher oil prices, CAD rates have more room to fall Wider"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Appetite for funding has declined amid compressed Treasury futures bases, evidenced by dwindling levered fund shorts Exhibit 4: With limited pass-through from higher oil prices, CAD rates have more room to fall Wider"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: In the past, sharp moves in equity funding have spilled over to Bund spreads Euro STOXX funding spread to OIS of 2nd nearest future Exhibit 6: The rally in 10y Gilts has been mostly driven by term premium compression C"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: The rally in 10y Gilts has been mostly driven by term premium compression Change in 10y UK term premium and rates expectations (yield curve-only model) Gilt relief likely to slow, prefer GBP steepeners. The ongoing dec"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Under our GSBEER-based proxy, premium in Sterling has now be reduced to around zero after the recent compression"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Under our GSBEER-based proxy, premium in Sterling has now be reduced to around zero after the recent compression Exhibit 3: Steady EUR/GBP performance reflects a balance between premium compression and a Sterling-negat"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Under our GSBEER-based proxy, premium in Sterling has now be reduced to around zero after the recent compression Exhibit 3: Steady EUR/GBP performance reflects a balance between premium compression and a Sterling-negat"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 5: The broader equity impulse has clearly shifted from an expected drag to a support for the Dollar ## Global FX Forecasts"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The broader equity impulse has clearly shifted from an expected drag to a support for the Dollar ## Global FX Forecasts Note: Spot values are as of Thursday's close."
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Room for macro volatility to move lower as the oil shock fades... Exhibit 2: ...but more micro volatility as debate around AI investment returns remain centre-stage 2. Coming to an understanding. The Iran War MoU has"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Oil Exports from the Persian Gulf Have Returned to 66% of Normal Levels Includes flows through the Strait of Hormuz, Yanbu, Fujairah, Gulf of Oman, and Botas Ceyhan."
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 3: Oil Exports from the Persian Gulf Have Returned to 66% of Normal Levels Includes flows through the Strait of Hormuz, Yanbu, Fujairah, Gulf of Oman, and Botas Ceyhan. Yanbu is on the west coast of Saudi Arabia, borderin"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Lower oil price supports resilient growth picture, but markets already reflecting cyclical optimism Exhibit 5: US breakeven inflation lower as oil falls and Fed tilts hawkish"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Lower oil price supports resilient growth picture, but markets already reflecting cyclical optimism Exhibit 5: US breakeven inflation lower as oil falls and Fed tilts hawkish Exhibit 6: Measures of US risk premium de"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 7: Growth pricing is already high, as equities mostly shrug off Fed shift"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Value added to AI equities requires more optimistic assumptions about the future macro benefits to companies Change in Market Cap/Valuation From Nov. 30 2022 to Jun. 25 2026 vs. GS Estimates of PDV of Potential AI Capita"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 9: Realised vol in G10 FX reset to a 5-year low following energy relief"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 10: More oil relief should come with broadening gains in equities"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 11: High stock volatility, lower volatility in macro assets"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 12: With growth pricing robust, inflation/policy relief is a more plausible macro tailwind"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 12: With growth pricing robust, inflation/policy relief is a more plausible macro tailwind ## Disclosure Appendix ## Reg AC We, Kamakshya Trivedi and Dominic Wilson, hereby certify that all of the views expressed in this r"
  },
  {
    "figure_id": "F045",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "Figure 1: Global forecast evolution, 2026 % chg saar, annual figures are %4Q/4Q; potential growth estimates in parentheses"
  },
  {
    "figure_id": "F046",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "Figure 2: Global business confidence and employment \\- ... with a recovery in Western Europe. The rebound in business sentiment should be concentrated in Western Europe, which experienced the most significant drop when the Strai"
  },
  {
    "figure_id": "F047",
    "report_id": "R005",
    "label": "Figure 3",
    "context": "Figure 4: Global consumer goods spending and mfg output %3m/3m, saar"
  },
  {
    "figure_id": "F048",
    "report_id": "R005",
    "label": "Figure 3",
    "context": "Figure 5: Global (ex China) employment"
  },
  {
    "figure_id": "F049",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "Figure 5: Global (ex China) employment Figure 6: Energy contribution to global CPI Underpinning this constructive outlook are accommodative financial conditions and supportive fiscal stances. The Fed's model of the financial c"
  },
  {
    "figure_id": "F050",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "Figure 7: US Fed FCI-G and global credit stress"
  },
  {
    "figure_id": "F051",
    "report_id": "R005",
    "label": "Figure 6",
    "context": "Figure 8: US corporate profits and private wages You can't have your cake and eat it too"
  },
  {
    "figure_id": "F052",
    "report_id": "R005",
    "label": "Figure 7",
    "context": "Figure 9: Global (ex China) labor markets Incoming reports highlight building pressure on goods prices. While the recent spike in energy prices is expected to fade, a mix of tech sector bottlenecks, stronger non-tech demand, and"
  },
  {
    "figure_id": "F053",
    "report_id": "R005",
    "label": "Figure 8",
    "context": "Figure 10: Global\\* core goods CPI model"
  },
  {
    "figure_id": "F054",
    "report_id": "R005",
    "label": "Figure 10",
    "context": "Figure 11: Global core CPI Amidst this uncertainty, we continue to take our lead on service price inflation from labor cost dynamics and signals of pricing power. Consistent with the broad easing in labor markets last year, wage"
  },
  {
    "figure_id": "F055",
    "report_id": "R005",
    "label": "Figure 11",
    "context": "Figure 11: Global core CPI Amidst this uncertainty, we continue to take our lead on service price inflation from labor cost dynamics and signals of pricing power. Consistent with the broad easing in labor markets last year, wage"
  },
  {
    "figure_id": "F056",
    "report_id": "R005",
    "label": "Figure 12",
    "context": "Figure 12: Real policy rate %; Nominal rate less 2y trailing core inflation The expansion's resilience and supportive financial conditions are linked to the tolerance of central banks in the face of persistently elevated inflatio"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Global Central Banks Have Mostly Either Held or Hiked Over the Last Three Months Exhibit 2: We Forecast Further Policy Rate Declines in the UK, US, and Some EMs, but Rate Hikes or Holds in Most DMs Over the Next Four"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Our End-2026 Policy Rate Forecasts Are Dovish Relative to Market Pricing but Skewed Hawkish Relative to Consensus"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Our End-2026 Policy Rate Forecasts Are Dovish Relative to Market Pricing but Skewed Hawkish Relative to Consensus"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: We Forecast Further Policy Rate Declines in the UK, US, and Some EMs, but Rate Hikes or Holds in Most DMs Over the Next Four Quarters Exhibit 3: Our End-2026 Policy Rate Forecasts Are Dovish Relative to Market Pricin"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Recent Policy Rate Changes Exhibit 5: Change in Average Global Policy Rate Over Time Exhibit 6: Changes in Financial Conditions Over the Last 3 Months"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Recent Policy Rate Changes Exhibit 5: Change in Average Global Policy Rate Over Time Exhibit 6: Changes in Financial Conditions Over the Last 3 Months Exhibit 7: Changes in Financial Conditions Over the Last 12 Mon"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Change in Average Global Policy Rate Over Time Exhibit 6: Changes in Financial Conditions Over the Last 3 Months Exhibit 7: Changes in Financial Conditions Over the Last 12 Months ## Policy Rate Forecasts"
  },
  {
    "figure_id": "F064",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Changes in Financial Conditions Over the Last 3 Months Exhibit 7: Changes in Financial Conditions Over the Last 12 Months ## Policy Rate Forecasts Exhibit 8: Policy Rate Forecast Revisions in Last 30 Days"
  },
  {
    "figure_id": "F065",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Changes in Financial Conditions Over the Last 12 Months ## Policy Rate Forecasts Exhibit 8: Policy Rate Forecast Revisions in Last 30 Days Exhibit 9: GS Forecast Policy Rate Changes ## Exhibit 11: GS Policy Rate Fo"
  },
  {
    "figure_id": "F066",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Policy Rate Forecast Revisions in Last 30 Days Exhibit 9: GS Forecast Policy Rate Changes ## Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing"
  },
  {
    "figure_id": "F067",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GS Forecast Policy Rate Changes ## Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing"
  },
  {
    "figure_id": "F068",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GS Forecast Policy Rate Changes ## Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing"
  },
  {
    "figure_id": "F069",
    "report_id": "R006",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing"
  },
  {
    "figure_id": "F070",
    "report_id": "R006",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing We exclude economies where GS forecasts differ from market pricing and consensus by more than 3pp due to data quality concerns,"
  },
  {
    "figure_id": "F071",
    "report_id": "R006",
    "label": "Exhibit 12",
    "context": "Exhibit 12: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing"
  },
  {
    "figure_id": "F072",
    "report_id": "R006",
    "label": "Exhibit 12",
    "context": "Exhibit 12: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing"
  },
  {
    "figure_id": "F073",
    "report_id": "R006",
    "label": "Exhibit 12",
    "context": "Exhibit 12: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing Note: Red shading indicates consensus forecast or market pricing above GS forecast, and blue shading indicates consensus forecast or market pr"
  },
  {
    "figure_id": "F074",
    "report_id": "R006",
    "label": "Exhibit 13",
    "context": "Exhibit 13: GS Growth and Policy Rate Forecasts vs. Bloomberg Consensus Forecasts Exhibit 14: GS GDP Growth Forecasts vs. Central Bank and Bloomberg Consensus Forecasts Note: Red shading indicates GS forecast above consensus forec"
  },
  {
    "figure_id": "F075",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 15: GS Inflation and Policy Rate Forecasts vs. Bloomberg Consensus Forecasts Exhibit 16: GS Inflation Forecasts vs. Central Bank and Bloomberg Consensus Forecasts"
  },
  {
    "figure_id": "F076",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 15: GS Inflation and Policy Rate Forecasts vs. Bloomberg Consensus Forecasts Exhibit 16: GS Inflation Forecasts vs. Central Bank and Bloomberg Consensus Forecasts Note: Red shading indicates GS forecast above consensus f"
  },
  {
    "figure_id": "F077",
    "report_id": "R006",
    "label": "Exhibit 17",
    "context": "Exhibit 17: DM Central Bank Balance Sheet Exhibit 18: Balance Sheet Forecasts and Key Views"
  },
  {
    "figure_id": "F078",
    "report_id": "R009",
    "label": "Exhibit 1",
    "context": "Exhibit 1: MLCC export volume and average export price(ASP) ## Price Target Risks and Methodologies ## Price Target Risks and Methodology - Murata Mfg. Valuation methodology: We are Buy-rated on Murata Mfg. with a 12-month price"
  },
  {
    "figure_id": "F079",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "## Why are prices so low? Exhibit 1. Hog price (RMB/kg): lowest since 2014 Exhibit 2. Pork price near multi-year lows vs. other meats – lowest since 2014 Exhibit 3. Profitability of self-breeding farmers since 2014 (RMB/head)"
  },
  {
    "figure_id": "F080",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1. Hog price (RMB/kg): lowest since 2014 Exhibit 2. Pork price near multi-year lows vs. other meats – lowest since 2014 Exhibit 3. Profitability of self-breeding farmers since 2014 (RMB/head) Note: If a loss cycle is interrupted only by a brief period "
  },
  {
    "figure_id": "F081",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2. Pork price near multi-year lows vs. other meats – lowest since 2014 Exhibit 3. Profitability of self-breeding farmers since 2014 (RMB/head) Note: If a loss cycle is interrupted only by a brief period of profitability with profits under RMB50/head be"
  },
  {
    "figure_id": "F082",
    "report_id": "R013",
    "label": "Exhibit 7",
    "context": "Other self-breeding farmers, even those who did not expand in May 2025, are being squeezed by the March – June 2026 deep-loss environment. The sustained losses will push these operators to reduce sow inventory as working capital depletes. Piglet-specialist far"
  },
  {
    "figure_id": "F083",
    "report_id": "R013",
    "label": "Exhibit 7",
    "context": "Conclusion: We maintain our view that hog industry capacity will accelerate its decline through 2Q26e. Exhibit 7. Self-breeding profits (RMB/head) Exhibit 8. Piglet (7kg) price (RMB/head) ## The impact of efficiency gains Efficiency improvements will partially"
  },
  {
    "figure_id": "F084",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 2: Interconnection queue in the US has risen significantly (years)"
  },
  {
    "figure_id": "F085",
    "report_id": "R014",
    "label": "Figure 2",
    "context": "Figure 2: Interconnection queue in the US has risen significantly (years) Speed to market is another key rationale for behind the meter power solutions, particularly for data centers where delivery timelines are critical. In m"
  },
  {
    "figure_id": "F086",
    "report_id": "R014",
    "label": "Figure 2",
    "context": "Figure 2: Interconnection queue in the US has risen significantly (years) Speed to market is another key rationale for behind the meter power solutions, particularly for data centers where delivery timelines are critical. In m"
  },
  {
    "figure_id": "F087",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: NSW power load on a typical day Figure 5: Power load by hour in New England on a typical day Figure 6: Power load fluctuations in New England and NSW"
  },
  {
    "figure_id": "F088",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: NSW power load on a typical day Figure 5: Power load by hour in New England on a typical day Figure 6: Power load fluctuations in New England and NSW"
  },
  {
    "figure_id": "F089",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Figure 7: Weichai Power's SOFC capacity targets vs. vehicle fuel cell demand base in 2024 Figure 8: Global FCEV sales trends ## DC gives rise to SOFC technology"
  },
  {
    "figure_id": "F090",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Figure 7: Weichai Power's SOFC capacity targets vs. vehicle fuel cell demand base in 2024 Figure 8: Global FCEV sales trends ## DC gives rise to SOFC technology ## Key research by JPM Asia Industrial team (led by Karen Li)"
  },
  {
    "figure_id": "F091",
    "report_id": "R014",
    "label": "Figure 10",
    "context": "Figure 10: US operational and planned nuclear capacity vs industry forecast and gov't target Figure 11: Announced US nuclear capacity tied to data centers and AI since 4Q23"
  },
  {
    "figure_id": "F092",
    "report_id": "R014",
    "label": "Figure 12",
    "context": "Figure 12: LCOE comparison among different types of nuclear reactors and CCGT in a few emerging markets Note: CCGT refers to combined-cycle gas turbines."
  },
  {
    "figure_id": "F093",
    "report_id": "R014",
    "label": "Figure 14",
    "context": "Figure 14: Performance of APAC Uranium Miners Theme vs. MSCI Asia Pacific Index Index to 100 Key players under the APAC Nuclear SMR Export Theme (equal weight) MSCI Asia Pacific Index Figure 15: Performance of APAC Nuclear SMR Ex"
  },
  {
    "figure_id": "F094",
    "report_id": "R014",
    "label": "Figure 14",
    "context": "Figure 16: Performance of APAC Submarine Cable and Inter-Grid Connect Theme vs. MSCI Asia Pacific Index Key players under the APAC Submarine Cable and Inter-Grid Connect Theme (equal weight) MSCI Asia Pacific Index Note: Prices a"
  },
  {
    "figure_id": "F095",
    "report_id": "R014",
    "label": "Figure 15",
    "context": "Figure 17: Performance of APAC Electrical & Power Gen Equipment Theme vs. MSCI Asia Pacific Index Key players under the APAC Electrical and Power Gen Equipment Theme (equal weight)"
  },
  {
    "figure_id": "F096",
    "report_id": "R014",
    "label": "Figure 16",
    "context": "Figure 18: Performance of APAC ESS Theme vs. MSCI Asia Pacific Index Note: Prices as of 24 June 2026."
  },
  {
    "figure_id": "F097",
    "report_id": "R014",
    "label": "Figure 17",
    "context": "Figure 18: Performance of APAC ESS Theme vs. MSCI Asia Pacific Index Note: Prices as of 24 June 2026. Note: Prices as of 24 June 2026."
  },
  {
    "figure_id": "F098",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Nordex had started to see a pick-up in orders over the last 12 months, helping to reach its US market share ambitions Vestas and Nordex Announced US Onshore Orders (GW) Vestas and Nordex Announced US Onshore Orders (GW)"
  },
  {
    "figure_id": "F099",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: US PPA prices have gone up significantly from \\$30/MWh in 2020-21 to c.\\$70/MWh currently Evolution of PPA prices in the US over 2020-26 (\\$/MWh) We see the contribution of US orders as an upside risk to our estimates,"
  },
  {
    "figure_id": "F100",
    "report_id": "R017",
    "label": "Figure 1",
    "context": "Figure 1: China monthly solar installations"
  },
  {
    "figure_id": "F101",
    "report_id": "R017",
    "label": "Figure 1",
    "context": "Figure 1: China monthly solar installations"
  },
  {
    "figure_id": "F102",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4: China – monthly total power consumption (YoY)"
  },
  {
    "figure_id": "F103",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 7: Power consumption in the internet and related services sector - YoY"
  },
  {
    "figure_id": "F104",
    "report_id": "R017",
    "label": "Figure 5",
    "context": "Figure 5: China – monthly power consumption by end user (YoY)"
  },
  {
    "figure_id": "F105",
    "report_id": "R017",
    "label": "Figure 6",
    "context": "Figure 6: China – power consumption breakdown (May 2026)"
  },
  {
    "figure_id": "F106",
    "report_id": "R017",
    "label": "Figure 8",
    "context": "Figure 8: China – monthly total power generation volume (YoY)"
  },
  {
    "figure_id": "F107",
    "report_id": "R017",
    "label": "Figure 8",
    "context": "Figure 11: Utilization hours YoY change by fuel type in Apr 2026 (DBe)"
  },
  {
    "figure_id": "F108",
    "report_id": "R017",
    "label": "Figure 9",
    "context": "Figure 12: Thermal power monthly utilization hours and YoY changes"
  },
  {
    "figure_id": "F109",
    "report_id": "R017",
    "label": "Figure 10",
    "context": "Figure 13: Hydro power monthly utilization hours and YoY changes"
  },
  {
    "figure_id": "F110",
    "report_id": "R017",
    "label": "Figure 11",
    "context": "Figure 14: Wind/solar monthly utilization hours (YoY)"
  },
  {
    "figure_id": "F111",
    "report_id": "R017",
    "label": "Figure 12",
    "context": "Figure 14: Wind/solar monthly utilization hours (YoY)"
  },
  {
    "figure_id": "F112",
    "report_id": "R017",
    "label": "Figure 13",
    "context": "Figure 13: Hydro power monthly utilization hours and YoY changes"
  },
  {
    "figure_id": "F113",
    "report_id": "R017",
    "label": "Figure 15",
    "context": "Figure 15: China – monthly solar installations"
  },
  {
    "figure_id": "F114",
    "report_id": "R017",
    "label": "Figure 15",
    "context": "Figure 18: China - power capacity addition breakdown"
  },
  {
    "figure_id": "F115",
    "report_id": "R017",
    "label": "Figure 16",
    "context": "Figure 16: China – annual solar installation demand estimates"
  },
  {
    "figure_id": "F116",
    "report_id": "R017",
    "label": "Figure 17",
    "context": "Figure 17: China – monthly wind installations"
  },
  {
    "figure_id": "F117",
    "report_id": "R017",
    "label": "Figure 19",
    "context": "Figure 19: China's average monthly market-based power tariffs"
  },
  {
    "figure_id": "F118",
    "report_id": "R017",
    "label": "Figure 19",
    "context": "Figure 19: China's average monthly market-based power tariffs"
  },
  {
    "figure_id": "F119",
    "report_id": "R017",
    "label": "Figure 21",
    "context": "Figure 24: China Resources Power (0836.HK) – one-year-forward P/B history"
  },
  {
    "figure_id": "F120",
    "report_id": "R017",
    "label": "Figure 24",
    "context": "Figure 24: China Resources Power (0836.HK) – one-year-forward P/B history"
  },
  {
    "figure_id": "F121",
    "report_id": "R017",
    "label": "Figure 24",
    "context": "Figure 24: China Resources Power (0836.HK) – one-year-forward P/B history"
  },
  {
    "figure_id": "F122",
    "report_id": "R017",
    "label": "Figure 24",
    "context": "Figure 27: China Resources Power (0836.HK) – dividend yield history"
  },
  {
    "figure_id": "F123",
    "report_id": "R017",
    "label": "Figure 25",
    "context": "Figure 25: China Yangtze Power (600900.SS) – dividend yield history"
  },
  {
    "figure_id": "F124",
    "report_id": "R017",
    "label": "Figure 25",
    "context": "Figure 25: China Yangtze Power (600900.SS) – dividend yield history"
  },
  {
    "figure_id": "F125",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 1: European premium held up better than mass peers but still lost share, while domestic premium expanded into European price bands. Among international brands, VW Group saw the steepest decline (Tesla the sole exception), a"
  },
  {
    "figure_id": "F126",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 1: European premium held up better than mass peers but still lost share, while domestic premium expanded into European price bands. Among international brands, VW Group saw the steepest decline (Tesla the sole exception), a"
  },
  {
    "figure_id": "F127",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Definition of the brand cohort"
  },
  {
    "figure_id": "F128",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Definition of the brand cohort"
  },
  {
    "figure_id": "F129",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Fanuc: Robot shipment value by destination (GSe) Exhibit 4: Japan: Robot shipment value by destination Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe)"
  },
  {
    "figure_id": "F130",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Fanuc: Robot shipment value by destination (GSe) Exhibit 4: Japan: Robot shipment value by destination Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe) Exhibit 6: Fanuc: Robot export vo"
  },
  {
    "figure_id": "F131",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Japan: Robot shipment value by destination Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe) Exhibit 6: Fanuc: Robot export volume to North America and average export price (GSe) Vertica"
  },
  {
    "figure_id": "F132",
    "report_id": "R019",
    "label": "Exhibit 5",
    "context": "Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe)"
  },
  {
    "figure_id": "F133",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe) Exhibit 8: Fanuc: Robodrill export volume to China and average export price (GSe) ## Price Target Risks and Methodology - Fanuc (6954.T)"
  },
  {
    "figure_id": "F134",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe) Exhibit 8: Fanuc: Robodrill export volume to China and average export price (GSe) ## Price Target Risks and Methodology - Fanuc (6954.T) Our 12-month target"
  },
  {
    "figure_id": "F135",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 1: Paid streaming service user penetration sees gains YoY Note: \\* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads. ## Share of Time Exhibit 2: Among"
  },
  {
    "figure_id": "F136",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Pay TV subs spend 43% of their watching time watching pay TV, suggesting further opportunity for streaming. Exhibit 4: Netflix and YouTube get the largest on-platform watching hours/share than other streaming services"
  },
  {
    "figure_id": "F137",
    "report_id": "R020",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Among total TV/video watchers, AMZN, NFLX, and YT lead on SVOD share of time Exhibit 3: Pay TV subs spend 43% of their watching time watching pay TV, suggesting further opportunity for streaming. Exhibit 4: Netflix a"
  },
  {
    "figure_id": "F138",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Pay TV subs spend 43% of their watching time watching pay TV, suggesting further opportunity for streaming. Exhibit 4: Netflix and YouTube get the largest on-platform watching hours/share than other streaming services"
  },
  {
    "figure_id": "F139",
    "report_id": "R020",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Meanwhile, platform subscribers are quicker to drop Starz, Crunchyroll, and MGM+ Note: \\* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads."
  },
  {
    "figure_id": "F140",
    "report_id": "R020",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Meanwhile, platform subscribers are quicker to drop Starz, Crunchyroll, and MGM+ Note: \\* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads. Exhibit"
  },
  {
    "figure_id": "F141",
    "report_id": "R020",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Netflix continues to lead on original programming, increasing further YoY"
  },
  {
    "figure_id": "F142",
    "report_id": "R020",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Netflix continues to lead on original programming, increasing further YoY % of respondents viewing Netflix as service with \"best original programming\" among major streaming services & premium networks Exhibit 9: After"
  },
  {
    "figure_id": "F143",
    "report_id": "R020",
    "label": "Exhibit 8",
    "context": "Exhibit 10: Netflix leads on many content quality-related metrics, although Paramount+, HBO Max, and Peacock compete closely on TV shows Platform Market Fit: The quality of engagement with platform content is a complex and multifa"
  },
  {
    "figure_id": "F144",
    "report_id": "R020",
    "label": "Exhibit 9",
    "context": "Exhibit 9: After years of decline, Netflix appears to be regaining ground as the host of the best original programming Exhibit 10: Netflix leads on many content quality-related metrics, although Paramount+, HBO Max, and Peacock c"
  },
  {
    "figure_id": "F145",
    "report_id": "R020",
    "label": "Exhibit 11",
    "context": "Exhibit 13: How often do you open this platform with a specific show, movie, or video in mind?"
  },
  {
    "figure_id": "F146",
    "report_id": "R020",
    "label": "Exhibit 11",
    "context": "Exhibit 13: How often do you open this platform with a specific show, movie, or video in mind? Exhibit 14: YouTube, Peacock, and Disney+ have the most 'browsing' users"
  },
  {
    "figure_id": "F147",
    "report_id": "R020",
    "label": "Exhibit 12",
    "context": "Exhibit 15: Quality is King: Focus index and destination index are positively correlated"
  },
  {
    "figure_id": "F148",
    "report_id": "R020",
    "label": "Exhibit 13",
    "context": "Exhibit 13: How often do you open this platform with a specific show, movie, or video in mind? Exhibit 14: YouTube, Peacock, and Disney+ have the most 'browsing' users Exhibit 15: Quality is King: Focus index and destination ind"
  },
  {
    "figure_id": "F149",
    "report_id": "R020",
    "label": "Exhibit 14",
    "context": "Exhibit 16: Level of focus is lower among platform users who got their subscription via a bundle or another member of their household"
  },
  {
    "figure_id": "F150",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 18: Price sensitivity test suggests near-optimal pricing for Netflix Exhibit 19: Current Netflix subs and non-subs have very similar views on pricing"
  },
  {
    "figure_id": "F151",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 18: Price sensitivity test suggests near-optimal pricing for Netflix Exhibit 19: Current Netflix subs and non-subs have very similar views on pricing 2018 survey 2019 survey 2020 survey 2021 survey 2022 survey 2023 surve"
  },
  {
    "figure_id": "F152",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Price sensitivity test suggests near-optimal pricing for Netflix Exhibit 19: Current Netflix subs and non-subs have very similar views on pricing 2018 survey 2019 survey 2020 survey 2021 survey 2022 survey 2023 surve"
  },
  {
    "figure_id": "F153",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Pay-TV subscriptions among total respondents ticked down YoY to $40\\%$ , in line with 2022-24 levels Exhibit 21: Pay-TV and vMVPD subscription rates are highest among 25-34-year-olds, males, and higher-income household"
  },
  {
    "figure_id": "F154",
    "report_id": "R020",
    "label": "Exhibit 21",
    "context": "Exhibit 23: YouTube TV and Hulu+ Live TV tick up in share of total subscriptions YoY"
  },
  {
    "figure_id": "F155",
    "report_id": "R020",
    "label": "Exhibit 21",
    "context": "Exhibit 23: YouTube TV and Hulu+ Live TV tick up in share of total subscriptions YoY ## Streaming Service Adoption"
  },
  {
    "figure_id": "F156",
    "report_id": "R020",
    "label": "Exhibit 22",
    "context": "Exhibit 24: Paid streaming service user penetration sees gains YoY"
  },
  {
    "figure_id": "F157",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Paid streaming service user penetration sees gains YoY Note: \\* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads. Exhibit 25: On average, survey re"
  },
  {
    "figure_id": "F158",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 26: Across all age groups, SVODs have the largest share of watching time"
  },
  {
    "figure_id": "F159",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Across all age groups, SVODs have the largest share of watching time Exhibit 27: Older groups watch more hours of TV/video per week, driven by pay TV ## Ad Tier Subscriptions"
  },
  {
    "figure_id": "F160",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 28: Across all platforms, adoption of ad-tier subscriptions is trending upward... Streaming Platform Adoption: Advertisement / No Advertisement Tiers"
  },
  {
    "figure_id": "F161",
    "report_id": "R020",
    "label": "Exhibit 28",
    "context": "Exhibit 29: ... and ad-tier subscriptions are making up an increasing share of each platform's user base"
  },
  {
    "figure_id": "F162",
    "report_id": "R020",
    "label": "Exhibit 29",
    "context": "Exhibit 30: When you watch content on each of these platforms, how often is the content your primary focus versus something you mainly have on in the background while doing other activities?"
  },
  {
    "figure_id": "F163",
    "report_id": "R020",
    "label": "Exhibit 30",
    "context": "Exhibit 31: Netflix, Apple TV+, and HBO Max elicit the most focus for subscribers"
  },
  {
    "figure_id": "F164",
    "report_id": "R020",
    "label": "Exhibit 31",
    "context": "Exhibit 33: YouTube, Peacock, and Disney+ have the most 'browsing' users"
  },
  {
    "figure_id": "F165",
    "report_id": "R020",
    "label": "Exhibit 31",
    "context": "Exhibit 33: YouTube, Peacock, and Disney+ have the most 'browsing' users Destination Index: Frequency of Opening Platform with Specific Content in Mind (Among Platform Users) ## Exhibit 34:"
  },
  {
    "figure_id": "F166",
    "report_id": "R020",
    "label": "Exhibit 32",
    "context": "Exhibit 34: Focus index and destination index are positively correlated"
  },
  {
    "figure_id": "F167",
    "report_id": "R020",
    "label": "Exhibit 34",
    "context": "Exhibit 35: Level of focus is lower among platform users who got their subscription via a bundle or another member of their household"
  },
  {
    "figure_id": "F168",
    "report_id": "R020",
    "label": "Exhibit 36",
    "context": "Exhibit 36: More than half of respondents are at least somewhat likely to subscribe combined service Exhibit 37: Likely way of adding the combined HBO Max/Paramount+ service? Likely Way of Adding Combined HBO Max / Paramount+ (Amo"
  },
  {
    "figure_id": "F169",
    "report_id": "R020",
    "label": "Exhibit 36",
    "context": "Exhibit 38: Amazon Prime Video is the most likely streaming platform to be replaced by a hypothetical HBO Max / Paramount+ platform Note: \\* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respecti"
  },
  {
    "figure_id": "F170",
    "report_id": "R020",
    "label": "Exhibit 38",
    "context": "Exhibit 39: If respondents in our survey were to follow through on their expected actions, we see significant upside for PSKY Potential Share Shift Following Introduction of HBO Max / Paramount+ Combination Offering (Among Total)"
  },
  {
    "figure_id": "F171",
    "report_id": "R020",
    "label": "Exhibit 39",
    "context": "Exhibit 39: If respondents in our survey were to follow through on their expected actions, we see significant upside for PSKY Potential Share Shift Following Introduction of HBO Max / Paramount+ Combination Offering (Among Total)"
  },
  {
    "figure_id": "F172",
    "report_id": "R020",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Almost two thirds of the survey watch sports regularly... Regularly Watch Live Sports (Among Total) Exhibit 41: ... skewing towards pay-TV subscribers Regularly Watch Live Sports, by TV Subscription Note: Access to l"
  },
  {
    "figure_id": "F173",
    "report_id": "R020",
    "label": "Exhibit 40",
    "context": "Exhibit 42: Over half of total respondents report regularly watching live sports on a TV channel (led by ESPN at 31%), and about a third watch live sports on a streaming platform (led by Prime Video at 22%) Channels/Platforms Where"
  },
  {
    "figure_id": "F174",
    "report_id": "R020",
    "label": "Exhibit 42",
    "context": "Exhibit 43: Watching live sports on SVOD is up 3ppt YoY... Watch Live Sports on TV / Streaming Platforms (Among Exhibit 44: ... driven most by Prime Video and Peacock"
  },
  {
    "figure_id": "F175",
    "report_id": "R020",
    "label": "Exhibit 43",
    "context": "Exhibit 45: Peacock and Amazon Prime have the highest percentage of users who subscribe for live sports programming"
  },
  {
    "figure_id": "F176",
    "report_id": "R020",
    "label": "Exhibit 43",
    "context": "Exhibit 45: Peacock and Amazon Prime have the highest percentage of users who subscribe for live sports programming Subscribe to Platform Because it Has Live Sports Programming (Among Respective Subscribers)"
  },
  {
    "figure_id": "F177",
    "report_id": "R020",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Peacock and Amazon Prime have the highest percentage of users who subscribe for live sports programming Subscribe to Platform Because it Has Live Sports Programming (Among Respective Subscribers) ## AlphaWise Survey Me"
  },
  {
    "figure_id": "F178",
    "report_id": "R020",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Sample age distribution Exhibit 47: Sample gender distribution Exhibit 48: Sample region distribution"
  },
  {
    "figure_id": "F179",
    "report_id": "R020",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Sample age distribution Exhibit 47: Sample gender distribution Exhibit 48: Sample region distribution Exhibit 49: Sample area distribution"
  },
  {
    "figure_id": "F180",
    "report_id": "R020",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Sample gender distribution Exhibit 48: Sample region distribution Exhibit 49: Sample area distribution Exhibit 50: Sample household income distribution"
  },
  {
    "figure_id": "F181",
    "report_id": "R020",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Sample region distribution Exhibit 49: Sample area distribution Exhibit 50: Sample household income distribution ## Disclosure Section"
  },
  {
    "figure_id": "F182",
    "report_id": "R020",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Sample area distribution Exhibit 50: Sample household income distribution ## Disclosure Section The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bol"
  },
  {
    "figure_id": "F183",
    "report_id": "R021",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Order of preference: GC memory Exhibit 2: NOR flash demand and supply growth rates Exhibit 3: NOR flash demand growth and supply growth by"
  },
  {
    "figure_id": "F184",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NOR flash demand and supply growth rates Exhibit 3: NOR flash demand growth and supply growth by Exhibit 5: Quarterly oversupply/undersupply ratio vs. Nanya and Winbond pricing Q/Q change"
  },
  {
    "figure_id": "F185",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: NOR flash demand growth and supply growth by Exhibit 5: Quarterly oversupply/undersupply ratio vs. Nanya and Winbond pricing Q/Q change Exhibit 6: Quarterly supply breakdown (mn Gb)"
  },
  {
    "figure_id": "F186",
    "report_id": "R021",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Quarterly oversupply/undersupply ratio vs. Nanya and Winbond pricing Q/Q change Exhibit 6: Quarterly supply breakdown (mn Gb) Exhibit 7: Quarterly demand breakdown by product (mn Gb)"
  },
  {
    "figure_id": "F187",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Quarterly oversupply/undersupply ratio vs. Nanya and Winbond pricing Q/Q change Exhibit 6: Quarterly supply breakdown (mn Gb) Exhibit 7: Quarterly demand breakdown by product (mn Gb) Exhibit 8: DDR4 8Gb (1Gx8) pric"
  },
  {
    "figure_id": "F188",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Quarterly supply breakdown (mn Gb) Exhibit 7: Quarterly demand breakdown by product (mn Gb) Exhibit 8: DDR4 8Gb (1Gx8) pricing chart Exhibit 9: DDR5 16Gb (2Gx8) pricing chart"
  },
  {
    "figure_id": "F189",
    "report_id": "R021",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Quarterly demand breakdown by product (mn Gb) Exhibit 8: DDR4 8Gb (1Gx8) pricing chart Exhibit 9: DDR5 16Gb (2Gx8) pricing chart # Winbond: Estimate Revisions and Quarterly Financials"
  },
  {
    "figure_id": "F190",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "Exhibit 10: Winbond: Estimate revisions"
  },
  {
    "figure_id": "F191",
    "report_id": "R021",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Winbond: Historical forward P/B Exhibit 13: Winbond: Historical forward P/B vs ROE Exhibit 14: Winbond: Earnings estimate revision breadth"
  },
  {
    "figure_id": "F192",
    "report_id": "R021",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Winbond: Historical forward P/B Exhibit 13: Winbond: Historical forward P/B vs ROE Exhibit 14: Winbond: Earnings estimate revision breadth ## Risk Reward – Winbond Electronics Corp (2344.TW)"
  },
  {
    "figure_id": "F193",
    "report_id": "R021",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Winbond: Historical forward P/B vs ROE Exhibit 14: Winbond: Earnings estimate revision breadth ## Risk Reward – Winbond Electronics Corp (2344.TW) DDR, NOR and SLC NAND pricing upside; long-term opportunities in CUBE"
  },
  {
    "figure_id": "F194",
    "report_id": "R021",
    "label": "Exhibit 15",
    "context": "## OWNERSHIP POSITIONING MS ESTIMATES VS. CONSENSUS Income Statement"
  },
  {
    "figure_id": "F195",
    "report_id": "R021",
    "label": "Exhibit 18",
    "context": "Exhibit 18: GigaDevice: Residual Income model Exhibit 19: GigaDevice: Historical forward P/E ## Risk Reward – GigaDevice Semiconductor Beijing Inc (603986.SS) Multiple drivers ahead"
  },
  {
    "figure_id": "F196",
    "report_id": "R021",
    "label": "Exhibit 19",
    "context": "Exhibit 19: GigaDevice: Historical forward P/E ## Risk Reward – GigaDevice Semiconductor Beijing Inc (603986.SS) Multiple drivers ahead ## PRICE TARGET Rmb888.00 Our price target is our base case value, derived from our residual"
  },
  {
    "figure_id": "F197",
    "report_id": "R021",
    "label": "Exhibit 20",
    "context": "## OWNERSHIP POSITIONING MS ESTIMATES VS. CONSENSUS"
  },
  {
    "figure_id": "F198",
    "report_id": "R021",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Nanya Tech – Historical P/B band Exhibit 24: Nanya Tech: Historical forward P/B vs ROE Exhibit 25: Nanya Tech: Earnings estimate revision breadth"
  },
  {
    "figure_id": "F199",
    "report_id": "R021",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Nanya Tech – Historical P/B band Exhibit 24: Nanya Tech: Historical forward P/B vs ROE Exhibit 25: Nanya Tech: Earnings estimate revision breadth ## Risk Reward – Nanya Technology Corp. (2408.TW)"
  },
  {
    "figure_id": "F200",
    "report_id": "R021",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Nanya Tech: Historical forward P/B vs ROE Exhibit 25: Nanya Tech: Earnings estimate revision breadth ## Risk Reward – Nanya Technology Corp. (2408.TW) DDR4 S/D becoming more favorable; OW ## PRICE TARGET NT\\$550.00"
  },
  {
    "figure_id": "F201",
    "report_id": "R021",
    "label": "Exhibit 28",
    "context": "Exhibit 28: PSMC: Historical forward P/B Exhibit 29: PSMC: Historical forward P/B vs ROE ## Risk Reward – Powerchip Semiconductor Manufacturing Co (6770.TW)"
  },
  {
    "figure_id": "F202",
    "report_id": "R021",
    "label": "Exhibit 28",
    "context": "Exhibit 28: PSMC: Historical forward P/B Exhibit 29: PSMC: Historical forward P/B vs ROE ## Risk Reward – Powerchip Semiconductor Manufacturing Co (6770.TW) Beneficiary of mature node up-cycle and EMIB supply chain ## PRICE TARG"
  },
  {
    "figure_id": "F203",
    "report_id": "R021",
    "label": "Exhibit 30",
    "context": "FY Dec 2026e ## MS ESTIMATES VS. CONSENSUS"
  },
  {
    "figure_id": "F204",
    "report_id": "R021",
    "label": "Exhibit 30",
    "context": "## MS ESTIMATES VS. CONSENSUS"
  },
  {
    "figure_id": "F205",
    "report_id": "R021",
    "label": "Exhibit 30",
    "context": "Cash Flow Statement"
  },
  {
    "figure_id": "F206",
    "report_id": "R021",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Forward P/B vs. ROAE ## Risk Reward – Macronix International Co Ltd (2337.TW) Top Pick Top Pick; OW on legacy Flash opportunities"
  },
  {
    "figure_id": "F207",
    "report_id": "R021",
    "label": "Exhibit 34",
    "context": "## OWNERSHIP POSITIONING MS ESTIMATES VS. CONSENSUS ◆ Mean ◆ MS Estimates"
  },
  {
    "figure_id": "F208",
    "report_id": "R022",
    "label": "Figure 1",
    "context": "## Shreyas Madabushi Figure 1. Lithium carbonate monthly inventory Figure 2. Lithium carbonate weekly inventory Figure 3. Lithium carbonate monthly production"
  },
  {
    "figure_id": "F209",
    "report_id": "R022",
    "label": "Figure 1",
    "context": "Figure 1. Lithium carbonate monthly inventory Figure 2. Lithium carbonate weekly inventory Figure 3. Lithium carbonate monthly production Figure 4. Lithium carbonate weekly production"
  },
  {
    "figure_id": "F210",
    "report_id": "R022",
    "label": "Figure 2",
    "context": "Figure 2. Lithium carbonate weekly inventory Figure 3. Lithium carbonate monthly production Figure 4. Lithium carbonate weekly production Figure 5. 5M26 spod import by country"
  },
  {
    "figure_id": "F211",
    "report_id": "R022",
    "label": "Figure 3",
    "context": "Figure 3. Lithium carbonate monthly production Figure 4. Lithium carbonate weekly production Figure 5. 5M26 spod import by country © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Monthly spodumene import vol (tons)"
  },
  {
    "figure_id": "F212",
    "report_id": "R022",
    "label": "Figure 4",
    "context": "Figure 4. Lithium carbonate weekly production Figure 5. 5M26 spod import by country © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Monthly spodumene import vol (tons)"
  },
  {
    "figure_id": "F213",
    "report_id": "R022",
    "label": "Figure 5",
    "context": "Figure 5. 5M26 spod import by country © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Monthly spodumene import vol (tons) ## Appendix A-1"
  },
  {
    "figure_id": "F214",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 5G smartphone shipments in China: 26m units in May Exhibit 2: Monthly # of new 5G smartphone models launched in China"
  },
  {
    "figure_id": "F215",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 5G smartphone shipments in China: 26m units in May Exhibit 2: Monthly # of new 5G smartphone models launched in China Exhibit 4: Monthly # of new 4G mobile phone models launched in China"
  },
  {
    "figure_id": "F216",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 5G smartphone shipments in China: 26m units in May Exhibit 2: Monthly # of new 5G smartphone models launched in China Exhibit 4: Monthly # of new 4G mobile phone models launched in China (m units)"
  },
  {
    "figure_id": "F217",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Exhibit 4: Monthly # of new 4G mobile phone models launched in China (m units) Exhibit 5: Smartphone shipments in China"
  },
  {
    "figure_id": "F218",
    "report_id": "R023",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Monthly # of new 4G mobile phone models launched in China (m units) Exhibit 5: Smartphone shipments in China Exhibit 6: Number of new smartphone models launched in China Exhibit 7: Mobile phone shipments in China"
  },
  {
    "figure_id": "F219",
    "report_id": "R023",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Smartphone shipments in China Exhibit 6: Number of new smartphone models launched in China Exhibit 7: Mobile phone shipments in China"
  },
  {
    "figure_id": "F220",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Mobile phone shipments in China Exhibit 8: Model pricing for various foldable smartphone brands Expected model and launch date for those cells with white background Exhibit 10: Cameras per smartphone model peaking ou"
  },
  {
    "figure_id": "F221",
    "report_id": "R023",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Model pricing for various foldable smartphone brands Expected model and launch date for those cells with white background Exhibit 10: Cameras per smartphone model peaking out Smartphone models launched by Huawei, Hon"
  },
  {
    "figure_id": "F222",
    "report_id": "R023",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Cameras per smartphone model peaking out Smartphone models launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since Dec 2020 Data as of Jun 26, 2026 Exhibit 12: Huawei/Honor/Xiaomi/OPPO/Vivo/Transsion: 20MPx+ bec"
  },
  {
    "figure_id": "F223",
    "report_id": "R023",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Huawei/Honor/Xiaomi/OPPO/Vivo/Transsion: 20MPx+ becomes the main contributor Cameras on smartphones launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since 2018: % of cameras in terms of pixels Exhibit 11: 20MPx"
  },
  {
    "figure_id": "F224",
    "report_id": "R023",
    "label": "Exhibit 11",
    "context": "Exhibit 11: 20MPx+ becomes the main contributor Cameras on smartphones launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since Dec 2020, % of cameras in terms of pixels Data as of Jun 26, 2026 Exhibit 13: 2/5/8MPx at $24\\%$"
  },
  {
    "figure_id": "F225",
    "report_id": "R023",
    "label": "Exhibit 13",
    "context": "Exhibit 13: 2/5/8MPx at $24\\%$ in 2026 YTD 487 cameras on 165 models launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion in 2026 YTD, divided by pixel count Data as of Jun 26, 2026 Exhibit 14: Honor: 20MPx+ remains the main c"
  },
  {
    "figure_id": "F226",
    "report_id": "R023",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Honor: 20MPx+ remains the main contributor Cameras on smartphones launched by Honor since 2018: % of cameras in terms of pixels Data as of Jun 26, 2026 Exhibit 15: Honor: $22\\%$ at 2/5/8MPx 72 cameras on 25 models laun"
  },
  {
    "figure_id": "F227",
    "report_id": "R023",
    "label": "Exhibit 14",
    "context": "Exhibit 16: Xiaomi: 20MPx+ decreasing Cameras on smartphones launched by Xiaomi since 2018: % of cameras in terms of pixels Exhibit 17: Xiaomi: $24\\%$ at 2/5/8MPx 67 cameras on 24 models launched by Xiaomi in 2026 YTD, by pixel nu"
  },
  {
    "figure_id": "F228",
    "report_id": "R023",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Xiaomi: 20MPx+ decreasing Cameras on smartphones launched by Xiaomi since 2018: % of cameras in terms of pixels Exhibit 17: Xiaomi: $24\\%$ at 2/5/8MPx 67 cameras on 24 models launched by Xiaomi in 2026 YTD, by pixel nu"
  },
  {
    "figure_id": "F229",
    "report_id": "R023",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Xiaomi: $24\\%$ at 2/5/8MPx 67 cameras on 24 models launched by Xiaomi in 2026 YTD, by pixel number Data as of Jun 26, 2026 Data as of Jun 26, 2026 Exhibit 18: OPPO: 20MPx+ remains the main contributor Cameras on smartp"
  },
  {
    "figure_id": "F230",
    "report_id": "R023",
    "label": "Exhibit 18",
    "context": "Exhibit 18: OPPO: 20MPx+ remains the main contributor Cameras on smartphones launched by OPPO since 2018: % of cameras in terms of pixels Data as of Jun 26, 2026 Exhibit 20: Vivo: 20MPx+ becomes the main contributor Cameras on sma"
  },
  {
    "figure_id": "F231",
    "report_id": "R023",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Vivo: 20MPx+ becomes the main contributor Cameras on smartphones launched by Vivo since 2018: % of cameras in terms of pixels Exhibit 19: OPPO: $25\\%$ at 2/5/8MPx 171 cameras on 56 models launched by OPPO in 2026 YTD,"
  },
  {
    "figure_id": "F232",
    "report_id": "R023",
    "label": "Exhibit 19",
    "context": "Exhibit 19: OPPO: $25\\%$ at 2/5/8MPx 171 cameras on 56 models launched by OPPO in 2026 YTD, by pixel number Data as of Jun 26, 2026 Data as of Jun 26, 2026 Exhibit 21: Vivo: $22\\%$ at 2/5/8MPx 93 cameras on 31 models launched by V"
  },
  {
    "figure_id": "F233",
    "report_id": "R023",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Vivo: $22\\%$ at 2/5/8MPx 93 cameras on 31 models launched by Vivo in 2026 YTD, by pixel count Data as of Jun 26, 2026 Exhibit 22: Transsion: 20MPx+ remains as the main contributor Cameras on smartphones launched by Tra"
  },
  {
    "figure_id": "F234",
    "report_id": "R023",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Transsion: 20MPx+ remains as the main contributor Cameras on smartphones launched by Transsion since 2021: % of cameras in terms of pixels Data as of Jun 26, 2026 Exhibit 23: Transsion: $33\\%$ at 2/5/8MPx 45 cameras on"
  },
  {
    "figure_id": "F235",
    "report_id": "R023",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Transsion: $33\\%$ at 2/5/8MPx 45 cameras on 16 models launched by Transsion in 2026 YTD, by pixel Data as of Jun 26, 2026 ## Disclosure Appendix ## Reg AC We, Allen Chang, Verena Jeng, Ting Song and Yifan Hu, hereby ce"
  },
  {
    "figure_id": "F236",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Hardwood domestic resale prices vs. Hardwood PIX China price (in USD) Exhibit 2: Softwood domestic resale prices vs. Softwood PIX China price (in USD) ## Global"
  },
  {
    "figure_id": "F237",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Global pulp shipments (kt)"
  },
  {
    "figure_id": "F238",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Global pulp shipments (kt) Exhibit 4: Global pulp sellers' inventories (days of supply) ## China"
  },
  {
    "figure_id": "F239",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Exhibit 5: China's hardwood and softwood imports (kt)"
  },
  {
    "figure_id": "F240",
    "report_id": "R024",
    "label": "Exhibit 5",
    "context": "Exhibit 6: China woodchip imports (kt) and prices (in RMB/t)"
  },
  {
    "figure_id": "F241",
    "report_id": "R024",
    "label": "Exhibit 5",
    "context": "Exhibit 6: China woodchip imports (kt) and prices (in RMB/t) ## Europe Essity: Oil relief lifts forecasts, but margin risks persist; Neutral. Our GS Europe consumer products team has updated its view on Essity after oil prices ha"
  },
  {
    "figure_id": "F242",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Weekly steel demand MS ASIA LIMITED+ Rachel L Zhang Hannah Yang, CFA"
  },
  {
    "figure_id": "F243",
    "report_id": "R027",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: ROA of Stabilized Assets Calculated as total stabilized NOI / gross PP&E EXHIBIT 2: Yield on Cost of Stabilized Assets Calculated as est. stabilized net income / average net PP&E"
  },
  {
    "figure_id": "F244",
    "report_id": "R027",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: ROA of Stabilized Assets Calculated as total stabilized NOI / gross PP&E EXHIBIT 2: Yield on Cost of Stabilized Assets Calculated as est. stabilized net income / average net PP&E EXHIBIT 3: We believe that ROA may ob"
  },
  {
    "figure_id": "F245",
    "report_id": "R027",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 4: Our preferred measure is yield on cost when looking at unlevered project-level returns, as colo REITs are extremely CapEx-heavy and depreciation is large and can be arbitrary"
  },
  {
    "figure_id": "F246",
    "report_id": "R027",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Our preferred measure is yield on cost when looking at unlevered project-level returns, as colo REITs are extremely CapEx-heavy and depreciation is large and can be arbitrary Calculated as est. stabilized net income /"
  },
  {
    "figure_id": "F247",
    "report_id": "R027",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: DLR Historical Forward EV/EBITDA (NTM) EXHIBIT 6: EQIX Historical Forward EV/EBITDA (NTM)"
  },
  {
    "figure_id": "F248",
    "report_id": "R027",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: DLR Historical Forward EV/EBITDA (NTM) EXHIBIT 6: EQIX Historical Forward EV/EBITDA (NTM)"
  },
  {
    "figure_id": "F249",
    "report_id": "R027",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: EQIX Historical Forward EV/EBITDA (NTM) ## EXAMPLE: 350 E CERMAK, A 27YO, STILL-PRODUCING, HIGHLY VALUABLE DATA CENTER"
  },
  {
    "figure_id": "F250",
    "report_id": "R027",
    "label": "EXHIBIT 7",
    "context": "## EXAMPLE: 350 E CERMAK, A 27YO, STILL-PRODUCING, HIGHLY VALUABLE DATA CENTER While we do not have infinite examples of data centers with very long lifespans, there are enough. Our personal favorite is 350 Cermak in Chicago, an enormous 1.1M sqft facility own"
  },
  {
    "figure_id": "F251",
    "report_id": "R027",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Digital Realty's facility at 350 Cermak, originally built in 1912 EXHIBIT 10: The facility was retrofitted into a telecom and data center hub in 1999 and acquired by DLR in 2005 ## I. REQUIRED DISCLOSURES"
  },
  {
    "figure_id": "F252",
    "report_id": "R027",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Digital Realty's facility at 350 Cermak, originally built in 1912 EXHIBIT 10: The facility was retrofitted into a telecom and data center hub in 1999 and acquired by DLR in 2005 ## I. REQUIRED DISCLOSURES Bernstein i"
  },
  {
    "figure_id": "F253",
    "report_id": "R033",
    "label": "Figure 1",
    "context": "Figure 1: Current sector allocation (May-26) At the end of May-26, the largest OW positions were in Tech and Healthcare. Financials and REITs remain the deepest UWs. The scale back in Communications in May hit nearly 2z. Along w"
  },
  {
    "figure_id": "F254",
    "report_id": "R033",
    "label": "Figure 2",
    "context": "At the end of May-26, the largest OW positions were in Tech and Healthcare. Financials and REITs remain the deepest UWs. The scale back in Communications in May hit nearly 2z. Along with downweightings in Staples, Healthcare and Utilities, this saw a 1.8z narr"
  },
  {
    "figure_id": "F255",
    "report_id": "R033",
    "label": "Figure 2",
    "context": "The scale back in Communications in May hit nearly 2z. Along with downweightings in Staples, Healthcare and Utilities, this saw a 1.8z narrowing in the Defensives OW."
  },
  {
    "figure_id": "F256",
    "report_id": "R033",
    "label": "Figure 10",
    "context": "## Debate & Divergence"
  },
  {
    "figure_id": "F257",
    "report_id": "R033",
    "label": "Figure 8",
    "context": "## Debate & Divergence In this month's edition of \\*Debate & Divergence\\*, we have scoured manager commentaries to gather insights into the following themes: (i) The Federal Budget: CGT / negative gearing and housing and (ii) The AI capex cycle and resources. "
  },
  {
    "figure_id": "F258",
    "report_id": "R033",
    "label": "Figure 12",
    "context": "Figure 12: Top mentions by fund managers ## Love Index \\- Upward momentum - five stocks moved up to ‘loved’ territory in May – GMG, QBE, IAG, TLC and ORI. Four stocks - CBA, MQG, WDS and XRO- moved into Neutral from underheld. \\-"
  },
  {
    "figure_id": "F259",
    "report_id": "R033",
    "label": "Figure 13",
    "context": "Figure 13: JPM Love Index vs ASX Rank – May-26 Figure 14: JPM Love Index vs ASX Rank – Apr-26 Figure 13 plots the Top 50 stocks in the ASX 200 (x-axis) against their respective ranking in our “Love Index” (y-axis) as at the end"
  },
  {
    "figure_id": "F260",
    "report_id": "R033",
    "label": "Figure 13",
    "context": "Figure 13: JPM Love Index vs ASX Rank – May-26 Figure 14: JPM Love Index vs ASX Rank – Apr-26 Figure 13 plots the Top 50 stocks in the ASX 200 (x-axis) against their respective ranking in our “Love Index” (y-axis) as at the end"
  },
  {
    "figure_id": "F261",
    "report_id": "R033",
    "label": "Figure 13",
    "context": "Figure 13 plots the Top 50 stocks in the ASX 200 (x-axis) against their respective ranking in our “Love Index” (y-axis) as at the end of May. ## Short Interest Monitor Figure 15 plots the change in days-to-cover (x-axis) of the top 50 stocks against their resp"
  },
  {
    "figure_id": "F262",
    "report_id": "R033",
    "label": "Figure 16",
    "context": "Note 1: Green markers indicate 'well-held' stocks, yellow markers indicate 'neutral' stocks, and red markers indicate 'underheld' stocks. Arrows represent movement in the Love Index. Note 2: Data labels only for Love Index movers and the stocks with the larges"
  },
  {
    "figure_id": "F263",
    "report_id": "R033",
    "label": "Figure 16",
    "context": "## Sector trends"
  },
  {
    "figure_id": "F264",
    "report_id": "R033",
    "label": "Figure 17",
    "context": "## Sector trends"
  },
  {
    "figure_id": "F265",
    "report_id": "R033",
    "label": "Figure 18",
    "context": "## Sector trends"
  },
  {
    "figure_id": "F266",
    "report_id": "R033",
    "label": "Figure 21",
    "context": "## Sector trends"
  },
  {
    "figure_id": "F267",
    "report_id": "R033",
    "label": "Figure 22",
    "context": "## Sector trends"
  },
  {
    "figure_id": "F268",
    "report_id": "R033",
    "label": "Figure 23",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F269",
    "report_id": "R033",
    "label": "Figure 24",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F270",
    "report_id": "R033",
    "label": "Figure 27",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F271",
    "report_id": "R033",
    "label": "Figure 28",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F272",
    "report_id": "R033",
    "label": "Figure 32",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F273",
    "report_id": "R033",
    "label": "Figure 30",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F274",
    "report_id": "R033",
    "label": "Figure 33",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F275",
    "report_id": "R033",
    "label": "Figure 34",
    "context": "## Sector trends (z-scores)"
  },
  {
    "figure_id": "F276",
    "report_id": "R033",
    "label": "Figure 38",
    "context": "## Appendix – Methodology"
  },
  {
    "figure_id": "F277",
    "report_id": "R033",
    "label": "Figure 36",
    "context": "## Appendix – Methodology ## Sector positioning For the purposes of assessing consensus positioning in each of the 11 GICS sectors, we gather data from 55 funds that together represent a meaningful proportion of assets under management in Australia. Our method"
  },
  {
    "figure_id": "F278",
    "report_id": "R036",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: A Howard Johnson's motor lodge in Panama City (in the 60's) ## KEY CHART EXHIBIT 2: Across many of the largest hotel brands in the US the number of hotels has tended to peak at \\~30 years \\* Holiday Inn ▲ Crowne Plaz"
  },
  {
    "figure_id": "F279",
    "report_id": "R036",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 3: Hilton's Spark brand saw an upward inflection in the pace of additions within 12 months of launching"
  },
  {
    "figure_id": "F280",
    "report_id": "R036",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Hotel brands tend to peak \\~30 years after creation"
  },
  {
    "figure_id": "F281",
    "report_id": "R036",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Hotel brands tend to peak \\~30 years after creation The peak - After the early acceleration, the successful hotel brands tend to face a steady upwards trajectory, with a relatively consistent number of hotels added ann"
  },
  {
    "figure_id": "F282",
    "report_id": "R036",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Not all brands are created equal though, similarly targeted brands can see very different success - the first 3 years provide a strong indication of potential Hotels - number of hotel rooms under Midscale brands EXHIBI"
  },
  {
    "figure_id": "F283",
    "report_id": "R036",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 7: Similarly pipelines tend to peak (ex-some pre GFC over optimism) Pipeline vs peak (Americas) EXHIBIT 8: On average hotel brand pipelines have peaked after 34 years, shortly after the total hotel number peaks"
  },
  {
    "figure_id": "F284",
    "report_id": "R036",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 7: Similarly pipelines tend to peak (ex-some pre GFC over optimism) Pipeline vs peak (Americas) EXHIBIT 8: On average hotel brand pipelines have peaked after 34 years, shortly after the total hotel number peaks Years post"
  },
  {
    "figure_id": "F285",
    "report_id": "R036",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Similarly pipelines tend to peak (ex-some pre GFC over optimism) Pipeline vs peak (Americas) EXHIBIT 8: On average hotel brand pipelines have peaked after 34 years, shortly after the total hotel number peaks Years post"
  },
  {
    "figure_id": "F286",
    "report_id": "R036",
    "label": "Exhibit 10",
    "context": "EXHIBIT 11: ROI is a strong predictor of relative pipeline size although Midscale hotels outperform the trend on ROI"
  },
  {
    "figure_id": "F287",
    "report_id": "R036",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: ROI is a strong predictor of relative pipeline size although Midscale hotels outperform the trend on ROI ROI vs relative supply by segment"
  },
  {
    "figure_id": "F288",
    "report_id": "R036",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: ROI is a strong predictor of relative pipeline size although Midscale hotels outperform the trend on ROI ROI vs relative supply by segment ## CAN BRANDS DEFY THE 30 YEAR PEAK? The two key ways where we see brands persi"
  },
  {
    "figure_id": "F289",
    "report_id": "R036",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: On a worldwide basis we don't see the same 30 year peak for brands EXHIBIT 13: Whitbread has also been able to push past the 30 year peak (albeit with the UK room count beginning to plateu as we approach 40 years) Whti"
  },
  {
    "figure_id": "F290",
    "report_id": "R036",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 14: We see little correlation between hotel age and average review score in the luxury segment, and a slightly negative slope Luxury brands - average year built vs average review score"
  },
  {
    "figure_id": "F291",
    "report_id": "R036",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 16: Intercontinental have just opened their Red Sea Resort, despite the brand turning 80 years old in 2026"
  },
  {
    "figure_id": "F292",
    "report_id": "R036",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 17: Hyatt are set to open the Grand Hyatt Miami Beach in 2027 - under a 46 year old brand"
  },
  {
    "figure_id": "F293",
    "report_id": "R036",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 17: Hyatt are set to open the Grand Hyatt Miami Beach in 2027 - under a 46 year old brand ## WHAT DOES THIS MEAN FOR THE COMPANIES?"
  },
  {
    "figure_id": "F294",
    "report_id": "R036",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 18: Hilton and Hyatt have the 'newest' brands among the asset light hotel groups Hotels - Age of hotel brands by owner (years)"
  },
  {
    "figure_id": "F295",
    "report_id": "R036",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Hilton and Hyatt have the 'newest' brands among the asset light hotel groups Hotels - Age of hotel brands by owner (years) Wyndham not covered EXHIBIT 19: In the US specifically Hyatt and Hilton look to have the newest"
  },
  {
    "figure_id": "F296",
    "report_id": "R036",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: In the US specifically Hyatt and Hilton look to have the newest brands, and should be off the peak room count for 64% and 30% of their brands respectively Wyndham not covered O - Outperform, M - Market-Perform, U - Und"
  },
  {
    "figure_id": "F297",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: Over the last 12 months, U.S. Medtech has underperformed the S&P (by 4600bps!) and has lagged all other healthcare subsectors US Healthcare Stock Performance EXHIBIT 2: U.S. Medtech P/E multiples are down $30\\%$ since"
  },
  {
    "figure_id": "F298",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "EXHIBIT 2: U.S. Medtech P/E multiples are down $30\\%$ since November 2025. We haven't seen these levels sustainably since before 2017 U.S. Medtech (S5HCEP\\*) Price/Earnings Ratio (1BF) EXHIBIT 3: Year to date, BSX and PODD have b"
  },
  {
    "figure_id": "F299",
    "report_id": "R037",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: U.S. Medtech P/E multiples are down $30\\%$ since November 2025. We haven't seen these levels sustainably since before 2017 U.S. Medtech (S5HCEP\\*) Price/Earnings Ratio (1BF) EXHIBIT 3: Year to date, BSX and PODD have b"
  },
  {
    "figure_id": "F300",
    "report_id": "R038",
    "label": "Figure 1",
    "context": "State-owned developers initially benefit from the weakening performance of their private competitors. However, as market sentiment, sales, and profitability decline, their creditworthiness also deteriorates, although the overall impact remains much milder. The"
  },
  {
    "figure_id": "F301",
    "report_id": "R038",
    "label": "Figure 2",
    "context": "Joint stock banks and asset management companies appear particularly affected likely due to their balance sheet connections with city commercials and shared market sentiment dynamic. Joint stock and city commercial banks share a similar business model: they ar"
  },
  {
    "figure_id": "F302",
    "report_id": "R038",
    "label": "Figure 3",
    "context": "## Shock to Property Prices At a macro level, favorable price dynamics encourage real estate investments in subsequent periods due to improved return prospects (Allen, 1993). Healthier balance sheets for developers and financial institutions further enable the"
  },
  {
    "figure_id": "F303",
    "report_id": "R038",
    "label": "Figure 4",
    "context": "## Shock to Consumer Sentiment A positive boost to consumer sentiment improves the performance of many other sectors (Figure 4). The improved willingness to purchase homes raises sales and strengthens financial positions of private developers, thereby improvin"
  },
  {
    "figure_id": "F304",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "## Status Quo and Key Reform Features ## Brazil's Current Tax System Brazil's tax system has historically heavily relied on the taxation of good and services. Total tax revenues to GDP in Brazil, at 32 percent in 2023, are among the highest in Latin America an"
  },
  {
    "figure_id": "F305",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "Brazil's tax system has historically heavily relied on the taxation of good and services. Total tax revenues to GDP in Brazil, at 32 percent in 2023, are among the highest in Latin America and the Caribbean (LAC), reaching levels close to the OECD average of 3"
  },
  {
    "figure_id": "F306",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "Consumption Tax Revenues by Sector Percent of GDP Tax Structure: Comparing Brazil with Latin America and OECD Averages, 2023 (Percent of GDP) Notes: LAC includes Caribbean countries while LAT only Latin American countries. In addition, the consumption tax syst"
  },
  {
    "figure_id": "F307",
    "report_id": "R039",
    "label": "Figure 2",
    "context": "generally, given the subnational governments' significance and power in the Brazilian federation, almost any fiscal policy issue – including macroeconomic management – is an issue of intergovernmental fiscal relations. In 2022, the combined shares of state and"
  },
  {
    "figure_id": "F308",
    "report_id": "R039",
    "label": "Figure 2",
    "context": "In LAC, the taxes most frequently assigned to sub-national entities are property taxes, motor-vehicle licenses, taxes on specific services and municipal fees. In OECD countries, sub-national entities tend to have broader potential tax bases with a substantial "
  },
  {
    "figure_id": "F309",
    "report_id": "R039",
    "label": "Figure 3",
    "context": "Notes: Adjusting monetary income includes aligning consumption and income when (mainly lower-income) households overstate their consumption relative to income, forcing budgets to equalize. ## The 2023 VAT Reform The reform will gradually replace the existing c"
  },
  {
    "figure_id": "F310",
    "report_id": "R039",
    "label": "Figure 4",
    "context": "One of the most important achievements of the reform is a harmonized tax base for both federal and subnational VAT components, anchored in the constitution since December 2023. This unified base, jointly with a full refund for VAT on intermediate goods and the"
  },
  {
    "figure_id": "F311",
    "report_id": "R039",
    "label": "Figure 4",
    "context": "and exemptions (IPI). “Exporting” the existing concessions to the new regime, while not optimal, is mainly explained by political economy factors, in particular strong lobbying of beneficiaries and the challenge to eliminate acquired rights (current status quo"
  },
  {
    "figure_id": "F312",
    "report_id": "R039",
    "label": "Figure 5",
    "context": "We estimate VAT liabilities by income and consumption deciles building on the World Bank's SimVAT model, adjusted with the most recent approved reform policies. $^{24}$ The model is calibrated with household data from the national budget survey (Pesquisa de Or"
  },
  {
    "figure_id": "F313",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "Informality. With significant informality present in Brazil, $^{33}$ and since households' share of spending in the informal sector declines with income (Bachas and al., 2020; Brusco et al., 2022), our results could underestimate the progressivity of consumpti"
  },
  {
    "figure_id": "F314",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "\\- SIMPLES. Poorer households are more likely to buy from small retailers and service providers which are operating under SIMPLES and are subject to lower (fixed) taxation, which is not modeled here. However, taxes charged under SIMPLES do not take into accoun"
  },
  {
    "figure_id": "F315",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "\\- First, the reduced rates as per reform parameters worsen equity. This instrument allows households across the income distribution to benefit from lower taxes on goods and services such as non-basic food items, health and education, local transportation, and"
  },
  {
    "figure_id": "F316",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "Third, the partial cashback would reduce the tax liability on lower-income households noticeably but also falls short of restoring progressivity. The tax liability of the poorest would fall by 5 percent of income and 3 percent of expenditure (compared to full "
  },
  {
    "figure_id": "F317",
    "report_id": "R039",
    "label": "Figure 8",
    "context": "Consumption microdata reflect a relatively strong representation of goods in lower income households' baskets, while services dominate for high-income households. Agricultural products, which include basic food items, mostly correspond to Cesta Basica, make up"
  },
  {
    "figure_id": "F318",
    "report_id": "R039",
    "label": "Figure 8",
    "context": "Consumption by Decile (percent of total consumption) basket of the poorest two deciles. Consumption of manufactured goods, ranging from processed foods to furniture, electric goods, cars, and fuels, is relatively constant across income groups, with a somewhat "
  },
  {
    "figure_id": "F319",
    "report_id": "R039",
    "label": "Figure 9",
    "context": "The maximum benefit for the poor would be achieved under a full cashback system. The cashback mechanism that fully refunds VAT payments for the lower two (and a half) deciles (with the exception of excise taxes) has the most redistributive power (Error! Refere"
  },
  {
    "figure_id": "F320",
    "report_id": "R039",
    "label": "Figure 9",
    "context": "Figure 9. Expanding the Cashback VAT reliefs – Reform vs cashback options (Full VAT as baseline, percent of income) Full Cashback by Sector (percent of total cashback) Tax Liability by Policy Instrument (percent of income) Tax Liability by Policy Instrument (p"
  },
  {
    "figure_id": "F321",
    "report_id": "R039",
    "label": "Figure 10",
    "context": "Full Cashback by Sector (percent of total cashback) Tax Liability by Policy Instrument (percent of income) Tax Liability by Policy Instrument (percent of expenditure) Sources: PNAD, World Bank, Receita Federal, and staff calculations ## Relaxing the Assumption"
  },
  {
    "figure_id": "F322",
    "report_id": "R039",
    "label": "Figure 10",
    "context": "## Relaxing the Assumption of Revenue Neutrality Reducing revenue collection via indirect taxes would align Brazil closer with peers. While revenue neutrality of the reform is enshrined in the reform law, this hypothetical exercise focuses on analyzing the dis"
  },
  {
    "figure_id": "F323",
    "report_id": "R039",
    "label": "Figure 10",
    "context": "Figure 10. Relaxing Revenue Neutrality (Percent of income) (Percent of expenditure) Equity improves when measured relative to income, but not when measured relative to expenditure. Under reform policy settings, the wedge between the tax liability of the lowest"
  },
  {
    "figure_id": "F324",
    "report_id": "R039",
    "label": "Figure 11",
    "context": "Adjusting monetary income for the lowest decile yields an improved equity pattern but still displays regressivity. As discussed above, the measurement of income might be subject to underreporting of alternative income sources. This could be particularly pertin"
  },
  {
    "figure_id": "F325",
    "report_id": "R039",
    "label": "Figure 11",
    "context": "points. Tax liabilities for the middle to upper deciles, however, remain broadly unaffected. Overall, there remains a strong incentive for companies to remain VAT (and thus refund) eligible and therefore process VAT electronically. This would, in turn, increas"
  },
  {
    "figure_id": "F326",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "(\\*) Items further adjusted with the approval of LC 214/2025. These adjustments are relatively small and are not considered in this paper. They would not change the results qualitatively. ## Annex IV. Supplementary Figures Figure 1. Tax Liability by Policy Ins"
  },
  {
    "figure_id": "F327",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "## Annex IV. Supplementary Figures Figure 1. Tax Liability by Policy Instrument by Income Decile (Percent of income) (Percent of expenditure) Figure 2. Services Shift Tax Liability by Income Decile (percent of expenditure) Sources: PNAD, World Bank, staff calc"
  },
  {
    "figure_id": "F328",
    "report_id": "R039",
    "label": "Figure 2",
    "context": "(Percent of expenditure) Figure 2. Services Shift Tax Liability by Income Decile (percent of expenditure) Sources: PNAD, World Bank, staff calculations. Note: Reform setting excludes cashback to allow for better comparison with pre-reform settings. ##"
  },
  {
    "figure_id": "F329",
    "report_id": "R040",
    "label": "Figure 1",
    "context": "14. CBUI Highly Correlated with Policy Rate Pricing Uncertainty During Certain Periods 25 15. ECB's backward-looking communication index: Robustness to dictionary 37 ## I. INTRODUCTION Successive large shocks—including pandemics, armed conflicts, geopolitical "
  },
  {
    "figure_id": "F330",
    "report_id": "R040",
    "label": "Figure 2",
    "context": "## II. A SURVEY OF CENTRAL BANK COMMUNICATION PRACTICES IN EUROPE As a first step, we survey the existing European central bank communication toolkits and their use in practice. Having been disproportionately affected by a sequence of recent shocks, European c"
  },
  {
    "figure_id": "F331",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "More pronounced differences arise in the content of central bank communications, particularly between AEs and EMs (Figure 3). On the one hand, there are important similarities: all AE central banks and more than 80 percent of EM central banks publish quantitat"
  },
  {
    "figure_id": "F332",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "## A. Stylized fact I: AE central banks make greater use of forward-looking language the forward-looking focus since the 2024 Bernanke review as the BoE increasingly incorporated scenario analysis in its communications. Figure 4. Distribution of the net forwar"
  },
  {
    "figure_id": "F333",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "the forward-looking focus since the 2024 Bernanke review as the BoE increasingly incorporated scenario analysis in its communications. Figure 4. Distribution of the net forward-looking index across country groups Note: The figure plots the density of the net f"
  },
  {
    "figure_id": "F334",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4. Distribution of the net forward-looking index across country groups Note: The figure plots the density of the net forward-looking communication indicator for the two separate country groups. AEs include the Czech Republic, the euro area, the United K"
  },
  {
    "figure_id": "F335",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Note: The figure plots the density of the net forward-looking communication indicator for the two separate country groups. AEs include the Czech Republic, the euro area, the United Kingdom, Iceland, Israel, and Sweden. EMs include Hungary, Poland, Romania, Ser"
  },
  {
    "figure_id": "F336",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Figure 5. Net forward-looking index evolution over time for selected countries Note: The figure plots the net forward-looking index for the ECB, the Bank of England, the Czech National Bank, and the Central Bank of the Republic of Türkiye. ## B. Stylized fact "
  },
  {
    "figure_id": "F337",
    "report_id": "R040",
    "label": "Figure 6",
    "context": "## B. Stylized fact II: Central banks commonly use forward-looking and backward-looking communication at the same time Figure 6 shows that central banks tend to use both styles of communication together. This pattern is particularly pronounced among advanced e"
  },
  {
    "figure_id": "F338",
    "report_id": "R040",
    "label": "Figure 7",
    "context": "Note: The figure plots the correlation between the forward- and backward-looking indices for each country. ## C. Stylized fact III: Inertia in central banks communication Persistence is another key feature of central bank communication. Changes tend to occur g"
  },
  {
    "figure_id": "F339",
    "report_id": "R040",
    "label": "Figure 8",
    "context": "We showed that inflation uncertainty, as proxied by forecasters' disagreements, is the main determinant of the shift in central bank communication towards a more forward-looking stance. We extend the framework in Equation 3 to a rolling panel regression to tes"
  },
  {
    "figure_id": "F340",
    "report_id": "R040",
    "label": "Figure 9",
    "context": "$$ \\text { MonetaryPolicyUncertainty } _ {i, t} = \\alpha_ {i} + \\beta_ {1} \\text { NetIndex } _ {i, t - 1} + \\beta_ {2} \\text { VSTOXX } _ {t} + \\beta_ {3} \\pi_ {t} + \\beta_ {4} \\text { Policyrate } _ {t} + \\beta_ {5} F F R _ {t} + \\varepsilon_ {i, t},\\tag{5} "
  },
  {
    "figure_id": "F341",
    "report_id": "R040",
    "label": "Figure 10",
    "context": "reverse: what is the central banks' own account of uncertainty, and how does the audience of CB communication react to it? To do a cross-country comparison of how central banks communicate uncertainty, we build another numerical index on uncertainty. We apply "
  },
  {
    "figure_id": "F342",
    "report_id": "R040",
    "label": "Figure 11",
    "context": "The trends in the CBUI across all countries and in the subindices for AEs and EMs are broadly similar. Spikes generally coincide with large shocks such as the Global Financial Crisis, Brexit, COVID-19, and tariff announcements. There has also been an increasin"
  },
  {
    "figure_id": "F343",
    "report_id": "R040",
    "label": "Figure 11",
    "context": "Figure 11. Cross-country correlation of the CBUI and policy rates CBUI Policy Rate Figure 12. Rolling correlation of CBUI Notwithstanding country idiosyncrasies, the common spikes and upward trend, suggests that central banks' own account of uncertainty is bro"
  },
  {
    "figure_id": "F344",
    "report_id": "R040",
    "label": "Figure 12",
    "context": "CBUI Policy Rate Figure 12. Rolling correlation of CBUI Notwithstanding country idiosyncrasies, the common spikes and upward trend, suggests that central banks' own account of uncertainty is broadly aligned with other major metrics of uncertainty. A formal reg"
  },
  {
    "figure_id": "F345",
    "report_id": "R040",
    "label": "Figure 12",
    "context": "Figure 12. Rolling correlation of CBUI Notwithstanding country idiosyncrasies, the common spikes and upward trend, suggests that central banks' own account of uncertainty is broadly aligned with other major metrics of uncertainty. A formal regression analysis "
  },
  {
    "figure_id": "F346",
    "report_id": "R040",
    "label": "Figure 13",
    "context": "Figure 13. What drives central banks to talk about uncertainty This figure reports the relative importance of each explanatory variable in accounting for variation in the uncertainty index. The measure is based on changes in the regression $R^{2}$ for each var"
  },
  {
    "figure_id": "F347",
    "report_id": "R040",
    "label": "Figure 14",
    "context": "Communicating about uncertainty could reflect central banks attempt to discuss factors which affect model uncertainty and signal possible uncertainty about the future monetary policy path. To analyze this possibility, we explore to which degree our CBUI is cor"
  },
  {
    "figure_id": "F348",
    "report_id": "R040",
    "label": "Figure 15",
    "context": "## A.5. Robustness to different dictionary: the ECB index A central bank should always be data dependent, but the term has been used in different ways and in different contexts across central banks. As a result, interpreting \"data dependence\" as inherently bac"
  },
  {
    "figure_id": "F349",
    "report_id": "R040",
    "label": "Figure 15",
    "context": "Figure 15 plots the original index identified in the main text (orange line) alongside an alternative index constructed using the same dictionary but excluding terms related to data dependence (blue line). By construction, the blue line is lower than the orang"
  },
  {
    "figure_id": "F350",
    "report_id": "R041",
    "label": "Figure 1",
    "context": "## 4. Stylized Facts We document a set of descriptive patterns in our dataset that motivates our empirical strategy. Stylized Fact 1: Countries with a higher vulnerability measure face significantly higher predicted default probability. A conditional fixed eff"
  },
  {
    "figure_id": "F351",
    "report_id": "R041",
    "label": "Figure 1",
    "context": "Figure 1. Predicted default probability from a conditional fixed-effects logit model with 95 percent confidence intervals. Note: The figure plots predicted default probabilities as the ND-GAIN vulnerability index varies. Higher values indicate greater climate "
  },
  {
    "figure_id": "F352",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "Figure 2. Distribution of Sovereign Defaults: top 20 countries by frequency. Notes: The figure reports the number of sovereign default episodes by country in the Asonuma and Trebesch (2016) database and shows the 20 countries with the highest frequency of defa"
  },
  {
    "figure_id": "F353",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "a. Impact of disasters on damage loss by adaptation level b. Impact of adaptation level on damage loss by disaster frequency Finally, we look at whether ODA concessional finance can contribute to build adaptive capacity and through the attenuation channel docu"
  },
  {
    "figure_id": "F354",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "a. Impact of disasters on damage loss by adaptation level b. Impact of adaptation level on damage loss by disaster frequency Finally, we look at whether ODA concessional finance can contribute to build adaptive capacity and through the attenuation channel docu"
  },
  {
    "figure_id": "F355",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "a. Impact of disasters on damage loss by adaptation level b. Impact of adaptation level on damage loss by disaster frequency Finally, we look at whether ODA concessional finance can contribute to build adaptive capacity and through the attenuation channel docu"
  },
  {
    "figure_id": "F356",
    "report_id": "R042",
    "label": "Figure 1",
    "context": "In practice, deviations from reference prices occur widely across countries, regardless of their level of development. Governments often justify intervening in fuel pricing to (1) shield consumers from volatility shocks by preserving affordability of fuel prod"
  },
  {
    "figure_id": "F357",
    "report_id": "R042",
    "label": "Figure 1",
    "context": "Figure 1. Differences between Liberalized and Regulated Fuel Consumer Prices (US dollars per liter, by fuel type and country income group) 1. Yearly Averages of Liberalized and Regulated Consumer Prices, by Fuel Type 2. Yearly Averages of Liberalized and Regul"
  },
  {
    "figure_id": "F358",
    "report_id": "R042",
    "label": "Figure 2",
    "context": "## Price Intervention at Product Access Figure 2. Composition of Gasoline Prices, by Country Income Group (Percent of pump price) ## Price Intervention at Product Sale"
  },
  {
    "figure_id": "F359",
    "report_id": "R043",
    "label": "Figure 1",
    "context": "Gender Budget Statements vary considerably across countries in many aspects such as the processes by which they are produced, their scope and depth, and the quality and detail of the contents presented. Countries also use different terminology to name the docu"
  },
  {
    "figure_id": "F360",
    "report_id": "R043",
    "label": "Figure 3",
    "context": "\\- Including the expected impact of policies on gender equality. This is supported by developing a methodology for gender impact assessments to analyze the expected or actual effect of policies or programs on gender equality, intended or unintended, and to imp"
  },
  {
    "figure_id": "F361",
    "report_id": "R043",
    "label": "Figure 3",
    "context": "The program budget architecture was leveraged to account for gender in terms of gender-sensitive objectives and performance indicators for programs, projects, and activities. Gender-focused budget expenditures were identified and tagged according to their gend"
  },
  {
    "figure_id": "F362",
    "report_id": "R044",
    "label": "Figure 1",
    "context": "## APPLICATION TO A SMALL OPEN ECONOMY We apply the model to an import intensive small island open economy. The currency of this country is in a basket peg with five currencies: the USD, NZD, AUD, EUR, and JPY (Figure 1). The country has been managing a basket"
  },
  {
    "figure_id": "F363",
    "report_id": "R044",
    "label": "Figure 2",
    "context": "competitiveness stability. However, this has not been always translated into price stability. Year-on-year headline inflation is volatile and has swung a lot post-COVID-19, from 6.9 percent in April 2024 to -3.8 percent in September 2025. Similarly, headline a"
  },
  {
    "figure_id": "F364",
    "report_id": "R044",
    "label": "Figure 3",
    "context": "Aligning the weights of a currency basket with trade shares or financial exposure is a traditional and intuitive approach, as it mirrors the structure of the economy's external transactions. However, this method does not fully satisfy a central bank's mandate "
  },
  {
    "figure_id": "F365",
    "report_id": "R044",
    "label": "Figure 3",
    "context": "Minimizing the variance of imported inflation through the exchange rate pass-through presents several benefits. First, stabilizing imported inflation contributes to the mandate of general price stability, i.e. low variance of inflation. Second, reducing the un"
  },
  {
    "figure_id": "F366",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure 1: The U.S. production network and upstreamness distribution (a) Production network (b) Upstreamness distribution As a robustness check, I also use the monetary policy shocks of Jarociński and Karadi (2020), which is av"
  },
  {
    "figure_id": "F367",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure 1: The U.S. production network and upstreamness distribution (a) Production network (b) Upstreamness distribution As a robustness check, I also use the monetary policy shocks of Jarociński and Karadi (2020), which is av"
  },
  {
    "figure_id": "F368",
    "report_id": "R045",
    "label": "Figure 2",
    "context": "Figure 2: Upstreamness and monetary policy transmission Notes: Panel (a) plots the coefficient on the interaction between upstreamness and monetary policy shocks from Equation 27. Panel (b) plots the cumulative price response"
  },
  {
    "figure_id": "F369",
    "report_id": "R045",
    "label": "Figure 2",
    "context": "Figure 2: Upstreamness and monetary policy transmission Notes: Panel (a) plots the coefficient on the interaction between upstreamness and monetary policy shocks from Equation 27. Panel (b) plots the cumulative price response"
  },
  {
    "figure_id": "F370",
    "report_id": "R045",
    "label": "Figure 3",
    "context": "Figure 3: Quantitative fit and decomposition of the upstreamness effect (a) Empirical estimates vs. calibrated model (b) Decomposition: flexibility vs. cost-cascade channel Notes: Panel (a) plots the model-implied interaction"
  },
  {
    "figure_id": "F371",
    "report_id": "R045",
    "label": "Figure 3",
    "context": "Figure 3: Quantitative fit and decomposition of the upstreamness effect (a) Empirical estimates vs. calibrated model (b) Decomposition: flexibility vs. cost-cascade channel Notes: Panel (a) plots the model-implied interaction"
  },
  {
    "figure_id": "F372",
    "report_id": "R045",
    "label": "Figure 4",
    "context": "Figure 4: Asymmetric effects from expansionary and contractionary monetary shocks (a) Asymmetric interaction coefficients (b) Cross-sectional evidence Notes: Panel (a) plots the coefficient on the interaction term between upst"
  },
  {
    "figure_id": "F373",
    "report_id": "R045",
    "label": "Figure 4",
    "context": "Figure 4: Asymmetric effects from expansionary and contractionary monetary shocks (a) Asymmetric interaction coefficients (b) Cross-sectional evidence Notes: Panel (a) plots the coefficient on the interaction term between upst"
  },
  {
    "figure_id": "F374",
    "report_id": "R045",
    "label": "Figure 5",
    "context": "Figure 5: Effects on industrial production (a) Symmetric specification (b) Asymmetric specification Notes: Panel (a) plots the coefficient on the interaction coefficient between upstreamness and monetary policy shocks from Equ"
  },
  {
    "figure_id": "F375",
    "report_id": "R045",
    "label": "Figure 5",
    "context": "Figure 5: Effects on industrial production (a) Symmetric specification (b) Asymmetric specification Notes: Panel (a) plots the coefficient on the interaction coefficient between upstreamness and monetary policy shocks from Equ"
  },
  {
    "figure_id": "F376",
    "report_id": "R045",
    "label": "Figure 6",
    "context": "$$ \\Delta^ {h} p _ {i t} = \\alpha_ {i} ^ {h} + \\mu_ {s (i), t} ^ {h} + \\phi^ {h} \\Delta^ {h} \\bar {p} _ {i t} ^ {\\mathrm{supplier}} + \\beta^ {h, \\mathrm{net}} (U _ {i} \\times \\varepsilon_ {t} ^ {m}) + \\rho^ {h} \\Delta p _ {i, t - 1} + u _ {i t} ^ {h}.\\tag{31} "
  },
  {
    "figure_id": "F377",
    "report_id": "R045",
    "label": "Figure 6",
    "context": "The coefficient $\\phi^{h}$ captures the pass-through from upstream supplier prices to downstream industry prices—the supply chain cascade. The coefficient $\\beta^{h,net}$ captures any residual effect of network position beyond what operates through the supplie"
  },
  {
    "figure_id": "F378",
    "report_id": "R045",
    "label": "Figure 7",
    "context": "Figure 7: Amplification of network effects (b) Supplier-weighted upstreamness Notes: Panel (a) plots the coefficient on the interaction term between upstreamness, input share, and monetary policy shocks. Panel (b) plots the co"
  },
  {
    "figure_id": "F379",
    "report_id": "R045",
    "label": "Figure 7",
    "context": "Figure 7: Amplification of network effects (b) Supplier-weighted upstreamness Notes: Panel (a) plots the coefficient on the interaction term between upstreamness, input share, and monetary policy shocks. Panel (b) plots the co"
  },
  {
    "figure_id": "F380",
    "report_id": "R046",
    "label": "Figure 1",
    "context": "Figure 1: Timeline for sequential economic decisions in VE and RE ## 2.1.1 Household behavior in RE We present households' mathematical decision problems using backward induction, consistent with the solution method employed for t"
  },
  {
    "figure_id": "F381",
    "report_id": "R046",
    "label": "Figure 2",
    "context": "Figure 2: Responses to Productivity Shock ## 4.1.2 Responses to monetary policy shock ## 4.1.3 Responses to fiscal policy shock"
  },
  {
    "figure_id": "F382",
    "report_id": "R046",
    "label": "Figure 4",
    "context": "Figure 3: Responses to Monetary Policy Shock Figure 4: Responses to Government Spending Shock"
  },
  {
    "figure_id": "F383",
    "report_id": "R046",
    "label": "Figure 5",
    "context": "Figure 3: Responses to Monetary Policy Shock Figure 4: Responses to Government Spending Shock ## 4.1.5 Variance decomposition While the previous subsections examined the dynamic effects of individual exogenous shocks, this sub"
  },
  {
    "figure_id": "F384",
    "report_id": "R046",
    "label": "Figure 3",
    "context": "Figure 3: Responses to Monetary Policy Shock Figure 4: Responses to Government Spending Shock ## 4.1.5 Variance decomposition While the previous subsections examined the dynamic effects of individual exogenous shocks, this sub"
  },
  {
    "figure_id": "F385",
    "report_id": "R047",
    "label": "Figure 1",
    "context": "Figure 1: Size of FX Sales Around Elections ## FX Sales and Elections ## II. The Political Economy of Foreign Exchange Intervention: Empirical Analysis ## A. Empirical Strategy To empirically investigate whether political econom"
  }
]