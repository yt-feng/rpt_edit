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
    "title": "美元真正的分裂不在指数里，而在“谁在涨、谁在跌”的背离中",
    "digest": "[wechat_article.md]\n# 美元真正的分裂不在指数里，而在“谁在涨、谁在跌”的背离中\n\n如果你只看DXY指数，今年美元似乎涨了1.5%。但如果把目光放到更全面的贸易加权指数上，美元实际是跌了0.1%。这不是统计口径的差异，而是全球外汇市场正在发生一场结构性的重新定价——美元不再是一个统一的“强美元”或“弱美元”故事，而是被地缘冲突、能源贸易流和各国央行政策分化撕成了两半。\n\n某外资投行最新发布的全球外汇策略报告，用“Divided Dollar”这个判断贯穿全文。我们认为，这份报告最有价值的洞察不在于它预测了哪个货币对会涨，而在于它提供了一个框架：为什么在同一个宏观环境下，有些货币在涨，有些在跌，以及当环境变化时，资金会流向哪里。\n\n以下是我们从这份报告中提炼出的核心判断与结构性推演。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美元的分裂不是暂时的，而是“战争经济”的永久性印记\n\n报告用了一个非常精准的对比：DXY指数（欧元权重超过57%）年初至今上涨约1.5%，而更全面的美元贸易加权指数却下跌约0.1%。这意味着，美元的强弱完全取决于你拿它去和谁比。\n\n这背后的驱动力是什么？报告指出，一方面，美国国内的周期性数据仍然强劲——非农就业数据超预期、ISM调查显示增长前景改善与通胀压力并存——这使得利率差持续偏向美元，尤其是相对于欧洲。但另一方面，中国人民币的持续升值（报告认为这一趋势虽然渐进但将超出市场预期）和日元在干预威胁下的“粘性”，使得美元在亚洲和新兴市场方向上反而承压。\n\n更深层的结构是“战争印记”。中东冲突持续近100天，霍尔木兹海峡的能源流动仍然严重受限，这导致贸易条件（terms of trade）在不同经济体之间产生了巨大的分化。能源出口国的货币受益于价格上涨，能源进口国的货币则承受压力。美元在这种分化中扮演了“两面角\n\n[... middle omitted ...]\n\n里，我们会分享完整的报告原文、原始图表，以及每周的跟踪更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元还在“分裂”，日元要加息了\n\n美元在打架，日元要动真格\n\n最近某外资行研报梳理了主要货币的最新逻辑，信息量很大，我帮你拆成几条主线👇\n\n**1️⃣ 美元：数据很强，但指数没涨**\n\n- 非农、ISM都在说“经济不错+通胀顽固”，按理说美元该强\n- 但DXY涨了1.5%，而贸易加权指数反而跌了0.1%\n- 原因是：人民币在慢慢升值、日元靠干预撑着，导致美元对不同货币表现“分裂”\n- 接下来如果数据不能突破区间，市场会盯着政策会议\n\n**2️⃣ 日元：6月可能加息**\n\n- 日本央行行长讲话暗示6月加息，比市场预期的7月要早\n- 理由是“如果市场觉得央行落后了，长端利率反而会更高”\n- 但仅靠一次加息很难扭转日元弱势，除非宏观背景也配合\n- 短期内，美债收益率偏高+风险偏好回暖，日元还是偏弱\n\n**3️⃣ 如果中东冲突缓和，哪些货币受益最大？**\n\n- 能源出口国（如澳元、巴西雷亚尔）前期涨了很多\n- 一旦局势缓和，受益者会切换到“能源进口国”\n- 新兴市场：南非兰特、韩元、波兰兹罗提、智利比索、匈牙利福林\n- G10：瑞典克朗、新西兰元、英镑\n\n**4️⃣ 新兴市场高息货币：选哪个？**\n\n- 依然看好匈牙\n\n[... middle omitted ...]\n\ny EM currencies have been resilient through the conflict, as US-Iran negotiations inch forward, the potential for lower oil prices and relief across key energy importing economies has raised t\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "美国利率的真正拐点，取决于一个被忽视的变量",
    "digest": "[wechat_article.md]\n# 美国利率的真正拐点，取决于一个被忽视的变量\n\n这份研报的核心判断值得每一个关注全球资产定价的人仔细琢磨：市场目前对美联储路径的定价，可能低估了一个结构性因素——利率的“新地板”已经抬升，而非短期波动的噪音。\n\n五月非农就业报告的强劲表现，让美国国债收益率在近期找到了一个更高的底部。但这不仅仅是数据本身的问题。真正重要的不是“美联储会不会再加息一次”，而是整个利率分布的形态已经发生了变化。研报明确指出，尽管最终仍预期年底收益率低于当前水平，但近期内，前端的加息定价压力难以消散。\n\n这意味着，投资者需要调整的，不是对某个具体利率水平的预测，而是对整个风险收益框架的重新认知。过去一年里，市场在“衰退交易”和“再通胀交易”之间剧烈摇摆，但这一轮周期可能正在进入一个新的阶段：增长韧性叠加通胀粘性，正在把利率的“地板”钉在一个更高的位置。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场低估的不是加息本身，而是加息定价的“不对称性”\n\n研报中一个关键的洞察是，市场对美联储政策路径的定价，目前呈现出一个显著的不对称结构：加息的风险被前置，而降息的空间被压缩。五月就业报告发布后，前端利率的重新定价并非均匀分布，而是朝着一个方向倾斜。\n\n这种不对称性，并非来自市场对美联储单次行动的预期，而是来自对“政策反应函数”本身的重新评估。当经济增长数据持续超预期，而通胀回落速度不及预期时，市场会自然而然地认为，美联储维持高利率的时间会更长，甚至不排除在某个时点再次加息的可能性。研报中提到的“长期暂停”而非“加息周期”的判断，恰恰是这种不对称定价的核心体现。\n\n对于投资者而言，这意味着不能简单地用“加息见顶”的思维来布局。更务实的做法是，承认前端利率在短期内可能维持在一个相对较高的水平，并且任何向下的修正都需要来自数据层面的明确验证。研\n\n[... middle omitted ...]\n\n整的研报解读和原始图表，并围绕这些未解问题展开更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美债利率的“新地板”\n\n利率地板抬高了\n\n美国5月就业数据超预期，给美债利率设了一个更高的地板。虽然研报认为美联储更可能“长停”而非加息，但短期看，强劲增长+通胀压力会持续支撑前端利率。\n\n1️⃣ 美债收益率预测上调\n10年期美债收益率年末目标从4.1%上调至4.4%。目前收益率已高于这个水平，所以对其他G10市场的溢出效应有限。英国国债因近年对全球利率敏感度更高，10年期目标上调至4.5%。\n\n2️⃣ 欧洲市场分化\n欧央行预计下周加息25bp，但7月是否继续是关键。通胀远期定价近期回落（受美伊协议预期影响），但降幅已超过宏观和能源价格隐含的水平。推荐做多5年5年实际欧元互换利率。\n\n3️⃣ 英国国债：宏观风险 > 供给风险\n尽管有政治和供给担忧，10年期英国国债近期表现稳健。风险溢价更多来自宏观（通胀、财政前景）而非供给。推荐2s10s曲线陡化策略。\n\n4️⃣ 日本：鹰派信号 vs 市场反应\n日央行行长暗示更紧迫地收紧，6月加息概率升至95%。但曲线在鹰派信号后反而陡化，说明市场对反应函数变化存疑。若没有更明确的加快加息信号，收益率仍有上行压力。\n\n加拿大央行面临两难：通胀下行但经济已衰退，短期加息门槛高，\n\n[... middle omitted ...]\n\nently above this level, we expect limited spillover effects into other G10 markets and keep most other yield forecasts unchanged. That said, we raise our 10y Gilt forecasts by 10bp to $4.5\\%$ \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "日元回流叙事被高估了：真正驱动汇率的不是日本邮政银行，而是GPIF的未对冲仓位",
    "digest": "[wechat_article.md]\n# 日元回流叙事被高估了：真正驱动汇率的不是日本邮政银行，而是GPIF的未对冲仓位\n\n过去几周，日本邮政银行CEO一句“可能将日本国债持有量翻倍”的表态，迅速点燃了市场对日元大规模回流叙事的想象。10年期日债收益率处于数十年高位，日元汇率仍处于历史低位——这两个事实叠加在一起，看起来确实像是一个“资金回家”的完美剧本。\n\n但某外资投行最新发布的研报给出了一个更冷静的判断：市场对日元回流规模与速度的预期，很可能被过度简化了。真正可能对日元汇率产生实质性影响的，并不是日本邮政银行这类对冲型投资者，而是以GPIF为代表的、持有近6万亿美元海外资产且大部分未对冲的日本机构投资者。而恰恰是后者，当前缺乏大规模回流的充分动机。\n\n这份报告的核心价值不在于否定日元回流的可能性，而在于拆解了“谁在推动回流”以及“什么条件下回流才会真正发生”。它提供了一个区分信号与噪音的分析框架——这对于任何关注日元资产定价、全球利率传导或日本资本流动的决策者而言，都是必要的前提工作。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日本邮政银行的表态更多是利率市场信号，而非汇率市场信号\n\n日本邮政银行持有约5500亿美元的海外资产，主要是债券，是日本除财务省外最大的单一外债持有者。当它的CEO公开表示可能增持日债时，市场本能地将其解读为日元利好。\n\n但这份研报指出一个关键区别：日本邮政银行是一个高度对冲的投资者。它的投资决策主要取决于“对冲后的海外收益率”与“日债收益率”之间的比较，而非简单的名义收益率高低。数据显示，尽管10年期日债收益率已升至3%以上，但同期全球主要国债收益率也在同步上升，导致日债的相对吸引力并未显著改善。\n\n这意味着，即便日本邮政银行真的增加日债持仓，它对日元汇率的直接影响也相当有限——因为对冲操作已经锁定了汇率风险。真正需\n\n[... middle omitted ...]\n\n注全球宏观与资产配置的读者一起，持续跟踪这些未解问题的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日元回流？谁才是真正的推手\n\n日元回流，关键看谁\n\n别被日本邮政银行带偏了节奏\n\n最近日本邮政银行说要加倍持有日债，很多人开始YY日元要大涨。但某外资投行的最新研报说：别想太多，真正的关键角色不是它。\n\n1️⃣ 日本邮政银行：看似巨无霸，实则“伪主力”\n- 持有约5500亿美元海外资产，主要是债券\n- 但它是hedged投资者，买日债还是买美债，看的是对冲后的利差\n- 目前全球利率同步上行，日债的相对吸引力其实没变太多\n- 它加仓日债可能只是调整日元组合，并非抛售海外资产\n\n2️⃣ GPIF才是真正的“日元发动机”\n- 管理近1万亿美元资产，大部分未对冲汇率风险\n- 私人养老金都跟着它走\n- 每五年一次战略评估，上次是2025年，2030年前不会有大的战略转向\n- 但在允许范围内仍有调整空间：若减持海外债券至下限（20%），可释放约870亿美元回流日债\n\n3️⃣ 现实很骨感：利差不支持大规模回流\n- 对未对冲投资者来说，日美10年期利差仍为负\n- 研报判断：没有更有利的利差环境，日元升值式的资金回流很难出现\n- 目前数据也显示，GPIF和私人养老金仍在买海外债券\n\n一句话总结：别被日本邮政银行带节奏，GPIF\n\n[... middle omitted ...]\n\ndinated reallocation towards domestic securities should be a source of notable JPY appreciation. Japan Post Bank, however, would unlikely be the driver as it tends to invest largely on a hedge\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "中国经济的真实温度：需求在修复，但供给侧的再定价才是关键",
    "digest": "[wechat_article.md]\n# 中国经济的真实温度：需求在修复，但供给侧的再定价才是关键\n\n这份某外资投行在6月初发布的中国高频经济活动追踪报告，表面上是在更新消费、生产、外贸和政策的周度数据。但如果只把它当作一系列图表来读，就错过了这份报告背后真正值得推敲的判断。\n\n报告的结论并不复杂：中国经济正在经历一个“非对称修复”——消费和出行层面的高频指标在改善，但工业生产和投资端的信号却呈现出明显的分化。市场目前讨论最多的是“需求是否见底”，但这份报告揭示了一个更深层的信号：真正需要被重新定价的，不是需求本身，而是供给侧的结构性变化。\n\n为什么这个判断重要？因为过去几个季度，市场对中国经济的预期始终在“弱复苏”和“二次探底”之间摇摆。高频数据虽然短期波动大，但它们能比月度宏观数据更早地捕捉到边际变化。而这份报告恰好提供了一组关键信号：消费信心在回升，但工业品价格和就业指标仍在低位徘徊。这意味着，当前的经济修复并不是全面的，而是有选择性的。对产业决策者和投资者而言，理解这种“选择性”在哪里，比猜测下一个月的GDP数字更有意义。\n\n以下是我们从这份报告中提炼出的四个核心洞察，以及一个尚未被充分讨论的潜在风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费信心的回升比表面数据更扎实，但结构性问题仍未解决\n\n报告中最亮眼的数据来自消费端。Morning Consult消费者信心指数在最新读数中升至多年新高，这并非一个孤立的信号。与此同时，30城新房成交面积虽然周环比持平，但仍高于去年同期；二手房成交面积也维持在高位。更值得注意的是，国内汽油和柴油价格在6月初被大幅下调，这直接降低了居民的出行成本，对消费意愿形成支撑。\n\n这些数据合在一起意味着什么？市场此前对消费复苏的持续性存疑，但高频率的出行和购房数据表明，居民的实际消费行为正在边际改善，且这种\n\n[... middle omitted ...]\n\n的是，我们会围绕这些“尚未回答的问题”展开持续的跟踪和讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n消费回暖但地产分化：6月高频数据怎么看\n\n**消费回暖，地产分化**\n\n某外资投行最新周度追踪显示，6月初经济呈现消费改善但地产仍弱的状态。\n\n**1/ 消费与出行**\n- 30城新房成交面积周环比持平，同比仍为正增长\n- 16城二手房成交面积环比下滑，但同比依然高于去年\n- 国内航班量环比下降，同比低于去年，航班取消率上升\n- 交通拥堵指数小幅回落\n- 消费者信心指数升至多年高位，PMI就业分项有所回暖\n\n**2/ 生产与投资**\n- 钢铁需求与产量均有所下降\n- 沿海省份动力煤日耗继续增加，高于去年同期\n- 地方专项债累计发行约1500亿元，进度偏慢\n- PSL余额5月继续收缩（净偿还）\n\n**3/ 其他宏观指标**\n- 港口集装箱吞吐量周环比上升，高于去年\n- 20港船舶离港货运量数据未完整披露\n\n**4/ 市场与政策**\n- 国内汽油、柴油价格6月4日分别下调525元/吨和505元/吨\n- 硫酸等部分化工品价格略涨，其他品种趋稳\n\n整体来看，消费端数据有所改善，但地产销售和工业活动仍偏弱，政策发力节奏需要关注。\n\n欢迎一起讨论你对近期经济走势的看法\n\n#学习笔记\n\n[source_mineru.md]\n\n[... middle omitted ...]\n\n3a1f0e8ea63dc9bdcc9e18684a07b98302c70e.jpg)\n\n<details>\n<summary>line</summary>\n\n| Month | 2019 (Thousand sqm) | 2025 (Thousand sqm) | 2026 (Thousand sqm) |\n|-------|---------------------|-----\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "资金流向正在告诉你一个被忽视的结构性切换",
    "digest": "[wechat_article.md]\n# 资金流向正在告诉你一个被忽视的结构性切换\n\n全球资金正在重新定价风险，但市场关注的焦点可能放错了地方。\n\n截至6月3日当周，全球股票基金净流入230亿美元，扭转了前一周70亿美元的净流出。同期固定收益基金继续获得超过400亿美元的净流入，货币市场基金资产更是飙升了1220亿美元。这些数字本身并不令人意外——市场情绪在宏观事件后反弹是常见剧本。\n\n真正值得追问的是：这些钱流向了哪里，以及它们没有流向哪里。\n\n某外资投行最新发布的全球资金流向周报揭示了一个被多数投资者低估的信号：资金从“防御性集中”转向“结构性再配置”的拐点可能已经出现。这不仅仅是风险偏好的短期修复，而是一场关于产业周期、区域竞争和资产定价逻辑的深层重置。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国市场正在从“避险目的地”变成“唯一增长叙事”\n\n当周全球股票基金净流入230亿美元，几乎全部由美国市场贡献。除美国外，发达市场普遍呈现净流出。这已经不是第一次出现这种分化。\n\n过去几年，美国市场一直被视为全球资金的“安全港”——流动性好、制度透明、科技龙头抗跌。但当前这轮流入的驱动力正在发生变化。它不再仅仅是对冲不确定性的防御性配置，而是资金开始相信：美国经济可能在主要经济体中率先完成“软着陆”甚至“不着陆”。\n\n报告数据显示，美国股票基金的净流入在经历了4月份的剧烈波动后，4周移动均值已回到正值区间。这种修复速度比市场预期的更快。更重要的是，同期欧洲、日本等发达市场的资金流向并未同步改善。这意味着资金不是在“抄底全球”，而是在“加注美国”。\n\n对于资产管理者而言，这一信号的含义是：美国市场的相对表现优势可能不是暂时的，而是结构性的。如果全球其他主要经济体无法在短期内提供同样清晰的增长路径，资金向美国集中的趋势还会持续。\n\n![研报原图 2](\n\n[... middle omitted ...]\n\n报告原文和原始数据图表，并围绕这些未解问题展开进一步的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球资金流向大反转\n\n📊 资金流向，有看头\n\n最近某外资投行发布的全球基金流动周报显示，6月3日当周，全球股市终于迎来了久违的净流入，规模达230亿美元，而前一周还在净流出70亿美元。\n\n1️⃣ **美国是这波流入的主力**\n全球股票基金净流入由负转正，主要靠美国基金带动。但其他发达市场普遍还在流出。新兴市场内部也分化明显：全球新兴市场基准基金、中国A股基金、韩国基金都在流出，只有台湾基金逆势流入。\n\n2️⃣ **行业偏好大洗牌**\n工业类基金成为资金最追捧的板块，累计净流入占管理资产比例高达24%。而金融和消费品板块则遭遇最大规模流出。科技板块表现中性，累计流入约3%。基础设施和能源板块也获得较多关注。\n\n3️⃣ **债市继续吸金，但偏好变了**\n全球固定收益基金整体依然强劲，当周净流入超400亿美元。但内部结构在变化：短期债券和通胀保护债券持续受欢迎，而长久期债券却在净流出。新兴市场债券中，本币债和硬通货债都有净流入。\n\n4️⃣ **货币市场基金暴增**\n货币市场基金资产单周飙升1220亿美元，说明市场仍有大量资金在观望。\n\n5️⃣ **外汇流向有亮点**\n美元需求最强，人民币净流出最多。有意思的是，英镑\n\n[... middle omitted ...]\n\nial sector and consumer goods funds saw the largest net outflows. Industrial sector funds saw the largest net inflows across sectors.   \n- Flows into global fixed income funds remained well-su\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "A股情绪降温背后，真正的结构性信号尚未被定价",
    "digest": "[wechat_article.md]\n# A股情绪降温背后，真正的结构性信号尚未被定价\n\n过去两周，A股市场出现了一个值得关注的变化：某外资投行编制的A股情绪指标MSASI加权值从66%回落至62%，创业板与全市场日均成交额分别下降9%和6%。如果只看这些数字，很容易得出“市场正在冷却”的结论。但这份研报真正想传达的判断，远比情绪降温本身更值得推敲。\n\n**市场真正低估的不是需求疲弱，而是K型分化格局下供给侧的再定价。** 5月制造业PMI滑至50%的荣枯线，消费出口订单与高耗能生产走弱，但高端制造依然坚挺。这不是一个简单的“好”或“差”的故事，而是一个结构正在剧烈重组的信号。投资者若仅以总量情绪判断方向，很可能错过本轮周期中最关键的定价机会。\n\n报告的核心结论是：短期波动仍将持续，但6-12个月维度上，A股仍有10-12%的上行空间。这一判断建立在三个尚未被充分讨论的变量之上——二季度盈利改善的路径、政策加速落地的节奏，以及A股相对于离岸市场的结构性优势。\n\n以下是我们从这份研报中提炼出的五个关键洞察，以及一个报告尚未完全回答的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 情绪指标的结构性下滑比总量下滑更值得警惕\n\nMSASI加权值从66%降至62%，4个百分点的降幅本身并不剧烈。但更值得关注的是分项指标的分化。根据报告披露的12个情绪指标权重，30日RSI（权重15%）和融资余额（权重15%）是贡献最大的两个因子。5月28日至6月3日期间，30日RSI仅上升1%，而融资余额基本未变——这意味着市场情绪的下滑并非来自恐慌性抛售，而是来自“参与意愿的边际递减”。\n\n这种递减在成交额上体现得更为清晰。创业板日均成交额降至7790亿元，全市场降至3.02万亿元，分别较上一周期下降9%和6%。但股指期货成交额和融资余额并未同步萎缩。这传递出一个微妙\n\n[... middle omitted ...]\n\n，但可以帮助你更系统地理解这些关键变量如何影响你的投资框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nA股情绪降温，K型分化还在\n\nA股情绪降温，K型分化持续\n\n市场在等一个更清晰的信号\n\n最近某外资投行的A股情绪指标（MSASI）从上一周期的66%降到了62%，虽然只是微调，但结合成交量来看，市场确实在“冷静期”。\n\n1/ 情绪降温但没崩\n- 创业板日均成交降至7790亿，全A降至3.02万亿，环比分别降9%和6%。\n- 股指期货成交和两融余额变化不大，说明存量资金还在，只是增量观望。\n- 30日RSI小幅回升1%，技术面没有恶化。\n\n2/ 宏观数据指向K型分化\n- 5月制造业PMI降到50%，符合预期。消费出口订单和能源密集型生产走弱，高端制造扛住了。\n- 基建还没看到政策发力。PPI环比回落至1%（4月是1.7%），油价涨势放缓。\n- 国内经济团队认为4-5月数据偏弱，Q2 GDP下行压力加大，预计6月起财政会加速落地。\n\n3/ 南向资金还在流入\n- 5月28日-6月3日，南向净流入45亿美元，年内累计353亿，月内33亿。\n- 北向交易数据自去年8月起已停止披露，所以现在只能看南向。\n\n4/ 对后市怎么看\n- 6-12个月仍有10-12%的上行空间，支撑来自出口改善、AI/能源资本开支、人民币升值、互\n\n[... middle omitted ...]\n\n for ChiNext and A-shared decreased 9% (to Rmb779bn) and 6% (to Rmb3,019bn), respectively, vs. the previous cycle, while equity futures turnover and margin transactions outstanding remained la\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R007",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n过去两个月，全球集装箱航运业经历了一场被多数人误解的行情反弹。上海出口集装箱运价指数（SCFI）自3月以来飙升73%，跨太平洋和亚欧航线录得两位数周涨幅，船公司普遍征收紧急燃油附加费和旺季附加费。表面上看，这是地缘冲突和旺季前备货驱动的短期脉冲。但某外资投行最新发布的行业深度报告揭示了一个更结构性的判断：当前市场定价的核心驱动力，并非需求端的意外强劲，而是供给侧已经发生且不可逆的再定价。\n\n这份报告基于对亚洲头部船公司1Q26运营数据的系统梳理，结合美国终端市场指标、运力管理动态和监管环境变化，勾勒出一幅“行业盈利能力正在经历结构性抬升”的图景。报告覆盖的标的包括TS Lines、中远海控、东方海外、长荣海运和商船三井等亚洲领先航运商，其核心逻辑值得每一位关注全球贸易和产业周期的决策者仔细推敲。\n\n为什么说这不是又一个“旺季故事”？因为支撑当前运价水平的三个结构性因素——有效运力持续收紧、船公司成本传导能力增强、以及行业竞争格局的优化——都具有超越短期周期的持续性。而市场对此的定价，可能才刚刚开始。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 有效运力比名义运力紧张得多，且这一缺口短期内无法弥补\n\n报告中最具洞察力的判断之一，是对“有效运力”与“名义运力”的区分。从全球集装箱船队总量看，运力似乎并不短缺。但港口拥堵、航线绕行（因中东冲突导致的红海绕行好望角）以及船公司主动的空白航行管理，正在吸收大量可用运力。Clarksons的港口拥堵指数在2026年1-5月创下历史新高，这意味着全球相当比例的集装箱船队实际上处于“等待”或“绕行”状态，而非有效运输货物。\n\n这一结构性紧平衡解释了为什么在名义运力增长、需求并未爆发式扩张的背景下，运价却能持续上行。报告指出，当前\n\n[... middle omitted ...]\n\n社群中，每周都有分析师对这类报告的逐段拆解和讨论。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n集装箱航运正在走出低谷\n\n运价回升+旺季提前\n\n最近几周运价明显走高，SCFI指数自3月以来上涨73%，且周环比出现双位数增长。这背后是多重因素叠加：中东局势推高燃油成本、船公司主动缩减运力、以及货主提前备货应对不确定性。\n\n1️⃣ 需求端比想象中更稳\n- 亚洲区域内航线表现亮眼，SITC一季度运量同比+7.6%，TS Lines同比+3.3%\n- 全球龙头马士基一季度超预期盈利，维持全年指引\n- 美国物流指数5月仍处高位69.5，显示终端需求韧性\n\n2️⃣ 供给端持续偏紧\n- 港口拥堵成为结构性特征，有效运力比名义数据更紧\n- 船公司通过空白航次控制运力，未来5周取消率约7%\n- 租船成本高企，自有船比例高的船公司优势更明显\n\n3️⃣ 亚洲船公司有额外红利\n- 高硫/低硫燃料价差扩大至135美元/吨\n- 亚洲船公司脱硫塔安装率远高于行业平均（长荣95% vs 行业47%）\n- 这意味着燃油成本传导能力更强，成本优势更突出\n\n4️⃣ 旺季预期已经提前兑现\n- 4月台湾船公司营收环比大幅改善，长荣、万海、阳明均转正\n- 跨太平洋和亚欧航线运价自2月底已涨114%/88%\n- 7月燃油附加费调整前，货主继续抢运\n\n[... middle omitted ...]\n\nnd elevated bunker costs. 1Q26 operational updates from leading liners underscore robust demand, particularly in intra-Asia and regional trades, with SITC and TS Lines reporting year-on-year v\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R008",
    "title": "市场真正低估的不是AI需求，而是它如何重塑全球收入分配",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是它如何重塑全球收入分配\n\n这份由某外资投行发布的研报，试图回答一个被多数讨论忽略的问题：当生成式AI从“生产力工具”进化为“认知替代者”，谁才是真正的受害者？主流叙事说，知识密集型行业首当其冲，低端岗位最先消失，依赖劳动力套利的新兴经济体（印度、印尼、墨西哥）风险最大。但这份报告的数据给出了相反的判断——高收入经济体才是AI冲击下最大的输家，而市场当前的定价恰恰呈现了这种“认知倒挂”。\n\n为什么AI开始大规模替代认知任务时，发达国家的经济基础反而更脆弱？为什么新兴市场的股指跌幅最大，但长期经济损伤却可能更小？这不是一篇关于哪个行业会失业的常规分析，而是一个关于“全球收入金字塔如何被AI重塑”的推演框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 信息产业的就业占比决定了谁真正暴露在AI冲击之下\n\n主流叙事认为，知识产业将遭受最严重打击，而新兴经济体依赖知识产业的劳动力套利，因而风险最高。但这个判断的第一个漏洞在于：信息产业在就业中的占比，在不同经济体之间差异巨大。\n\n研报数据显示，高收入国家中，信息产业（IT、广播电视、电信、信息通信）直接雇佣的劳动力占总量7%到10%。而在中等收入国家，这一比例仅为1%到4%。以印度为例，即使将间接依赖数字技术的岗位（如金融、医疗、零售）全部纳入，其数字密集型就业占比也远低于OECD国家均值。\n\n这意味着什么？即便AI以最激进的速度替代知识工作者，新兴经济体的就业基础受到的直接冲击在量级上远小于发达国家。这不是说新兴市场没有风险，而是说风险的“体积”被放错了位置。一个经济体如果只有3%的人在信息产业工作，AI替代掉其中一半，对整体就业的影响是1.5个百分点；而如果这个比例是10%，替代掉一半就是5个百分点——后者才是真正的结构性冲击。\n\n[... middle omitted ...]\n\n继续讨论，我们会在那里分享报告的原始图表和我们的进一步解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI不是穷国的噩梦，富国更慌\n\nAI颠覆，谁更危险？\n\n某外资投行的最新研报，看完让人重新思考AI的赢家输家。\n\n多数人觉得AI会先砸了印度、印尼这类低成本外包国的饭碗。但数据给出的答案正好相反👇\n\n1️⃣ 信息产业就业占比\n- 高收入国家：7-10%的劳动力在信息行业\n- 印度、印尼：仅1-4%\n- 服务业占GDP比重：发达国家70%+ vs 印度50%、印尼44%\n→ 发达经济体对AI的暴露度其实更高\n\n2️⃣ 工资剪刀差\n- 软件工程师年薪：印度1万美元 vs 美国13.6万 vs 英国8.1万\n- 会计、客服、数据分析——所有AI能替代的白领岗位，工资差距都一样夸张\n- 企业用AI替代一个年薪10万的美国人的动力，远大于替代一个1万的印度人\n→ 高收入国家被替代的“经济诱因”更大\n\n3️⃣ 市场为何反向定价？\n- 印度、印尼股市在AI浪潮中跌得最惨\n- 原因：这些市场没有AI产业链上的受益者（不造芯片、不搞模型）\n- 市场只看到短期冲击（IT服务被替代），没看到长期经济结构反转\n\n4️⃣ 真正的颠覆逻辑\n- 中低收入国家国民收入平均损失10%\n- 高收入国家国民收入平均损失22%\n- AI反而可能成为“拉\n\n[... middle omitted ...]\n\ns, and will that in turn trigger tighter controls on AI adoption? Amid the myths and noise around these questions, we set out here our data-backed view.\n\nThe dominant narrative falters: The mo\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "就业市场比通胀更值得关注的信号：美联储的降息叙事正在被重新定价",
    "digest": "[wechat_article.md]\n# 就业市场比通胀更值得关注的信号：美联储的降息叙事正在被重新定价\n\n市场对美联储降息的预期，可能正建立在一个正在被数据推翻的假设上：劳动力市场会显著放缓。但最新发布的5月就业报告表明，实际情况恰恰相反。\n\n非农就业人数增长17.2万，远高于市场预期的8.8万，且前两个月数据被上修。失业率稳定在4.3%，而衡量失业的多个指标在5月出现回落，逆转了4月的恶化趋势。这不是一个正在冷却的劳动力市场——这是一个在政策利率维持高位的情况下，依然表现出韧性的市场。\n\n某外资投行在最新研报中明确指出：这份报告应让美联储官员继续聚焦通胀风险。其核心判断是，当前政策立场并未对经济构成实质性抑制。这一结论对资产定价的含义是深远的——如果劳动力市场不降温，通胀回落至2%目标的路径就更难被确认，降息的时间窗口可能比市场预期的更远。\n\n以下是我们从这份研报中提炼的五个核心洞察，以及在数据背后值得追问的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 就业增长的广度在改善，这比总量数字更值得关注\n\n非农就业17.2万的增量本身已经超出预期，但真正重要的信号藏在结构里。研报使用的扩散指数显示，就业增长的广度在近期持续改善，周期性行业的表现尤为突出。这意味着增长不是由少数几个板块拉动的，而是具有更广泛的产业基础。\n\n具体来看，休闲酒店业增长了7万，部分受世界杯临时性因素推动；地方政府就业增加了5.5万。这些看似有“噪音”的细节，恰恰说明劳动力市场的韧性并非虚胖。即便剔除这些一次性因素，私营部门就业的3个月移动均值也已攀升至2024年3月以来的最高水平。\n\n对于投资者而言，这意味着一个关键判断：劳动力市场的韧性正在从“结构性短缺”转向“周期性复苏”。如果后者成立，那么工资增长和消费支出的下行空间将比市场预期的更有限。\n\n![研报原图 2]\n\n[... middle omitted ...]\n\n享完整的研报原文、数据图表，以及围绕这些未解问题的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月非农超预期，就业加速但未过热\n\n就业韧性超预期\n\n📊 5月非农就业新增17.2万，大幅超过市场预期的8.8万。前几个月数据也向上修正，3个月均值创2024年3月以来新高。\n\n1️⃣ 就业广度在改善\n- 休闲酒店行业新增7万，部分受世界杯临时提振\n- 地方政府就业增加5.5万\n- 贸易运输行业均值回归、精神航空破产导致减少0.9万\n- 周期性行业招聘广度持续提升\n\n2️⃣ 失业率稳定在4.3%\n- 5月失业人数下降，扭转了4月的上升趋势\n- 求职成功率小幅回升但仍偏弱\n- 时薪环比增长0.3%，带动工资收入增长0.4%\n\n3️⃣ 通胀方面\n- 核心CPI预计从4月的0.376%降至5月的0.183%，主要因为租金技术调整消退\n- 但核心PCE预计从0.239%升至0.327%，因为PPI相关项目走强\n- 年化核心PCE预计达3.4%，远高于美联储2%目标\n\n4️⃣ 联储官员态度偏鹰\n- 达拉斯联储主席Logan明确主张可能加息\n- 克利夫兰联储Hammack认为就业市场平衡，维持利率合理\n- 纽约联储Williams是少数鸽派，不担心通胀持续\n\n5️⃣ 关税方面\n- 新301关税税率10-12.5%，主要延\n\n[... middle omitted ...]\n\n Goods inflation was slightly positive as IT-related price pressures offset the waning impact of tariffs.   \n- Despite benign core CPI, we expect core PCE inflation accelerated in May due to s\n\n[... middle omitted ...]\n\ns available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities International, Inc., US. All rights reserved."
  },
  {
    "id": "R010",
    "title": "欧洲汽车市场真正被低估的风险，不是中国份额，而是欧洲的利润优先策略",
    "digest": "[wechat_article.md]\n# 欧洲汽车市场真正被低估的风险，不是中国份额，而是欧洲的利润优先策略\n\n欧洲正在经历一场它不愿承认的结构性变化。中国汽车制造商在欧洲的市场份额在过去12个月内翻了一倍，达到约6.8%。这个数字本身并不惊人，真正值得关注的，是这背后两股力量的分化：中国车企在加速渗透，而欧洲车企却在主动选择“不反击”。\n\n这不是一个关于“谁将赢得市场”的故事，而是一个关于“谁愿意为市场份额牺牲利润”的博弈。某外资投行最新发布的全球汽车研报给出了一个反直觉的判断：市场过度关注了中国的进攻，却低估了欧洲的防守策略——后者可能才是决定未来五年行业利润分配的核心变量。\n\n这份报告的核心洞察在于：中国车企的崛起并非靠简单的价格战，而是产品力的系统性提升；欧洲车企并非无力反击，而是选择了保护利润而非份额。这两种策略的碰撞，正在重塑欧洲汽车业的竞争逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国车企的欧洲攻势：份额翻倍背后是产品力而非补贴\n\n中国车企在欧洲的市场份额从2023年初的约1%攀升至2026年4月的近7%，这一增速远超历史上任何新进入者。以英国市场为例，奇瑞集团和比亚迪在极短时间内就达到了3-4%的市场份额，而丰田和现代当年达到这一水平耗费了数倍的时间。\n\n报告特别强调了一个关键判断：中国车企的竞争力并非来自价格战。在德国市场，中国品牌的定价基本处于各细分市场的中位区间，并未出现系统性低价倾销。真正驱动消费者选择的，是产品本身的“物超所值”——更丰富的配置、更精致的工艺、更先进的智能化功能。\n\n这一点在报告中得到了实地验证。该投行的分析师团队在2025年北京车展和英国经销商走访中发现，中国汽车的产品质量已经不再是“够用”，而是“更好”。这背后是中国国内市场的“完美竞争”逻辑：大量生产资质和地方政府资金支持，迫使车企在配置和品\n\n[... middle omitted ...]\n\n，我们将结合完整报告和最新行业动态，持续追踪这一趋势的演进。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国车在欧盟翻倍增长，欧洲车企为何不反击？\n\n中国车企在欧盟悄悄赢了\n\n一年之内，市占率从不到3%冲到近7%\n\n某外资投行最新研报，核心信息量很大：\n\n1️⃣ 中国车在欧盟的市占率过去12个月翻了一倍，到2026年4月已接近7%\n——速度比当年丰田、现代进入欧洲快得多\n——英国市场，奇瑞和比亚迪只用很短时间就拿到3-4%份额\n\n2️⃣ 这次不是靠低价\n——研报团队亲自去了北京车展和英国经销商\n——结论：中国车在配置、做工、功能上已经“更好”\n——本质是“完美竞争”带来的产品力碾压\n\n3️⃣ 反补贴关税没挡住\n——中国车企直接自己消化了关税成本\n——欧洲市场60%是公司车队采购，残值很重要，所以中国品牌没有疯狂压价\n\n4️⃣ 欧洲车企的选择：保利润，不硬拼\n——Stellantis、福特、日韩品牌是份额流失最严重的\n——但欧洲车企更倾向于保护现金流和利润率，而不是打价格战\n——正在拼命降成本，比如加速用便宜的LFP电池\n\n5️⃣ 电动车领域更明显\n——比亚迪在欧盟电动车市占率一年增长了6.3个百分点\n——大众也涨了6.8个百分点，但Stellantis跌了7.6个百分点\n\n有意思的是，研报认为最大的限制因素可能\n\n[... middle omitted ...]\n\nd their collective market share has risen to close to 7% in April 2026. Perhaps more worrying is the pace of the ascent – in the UK, one of the markets where they have been strongest, brands s\n\n[... middle omitted ...]\n\nf041ec436e53aa9833924f.jpg)\n\n# Newsletters\n\nSubscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points"
  },
  {
    "id": "R011",
    "title": "中国油价调控的真正成本，比市场担心的低得多",
    "digest": "[wechat_article.md]\n# 中国油价调控的真正成本，比市场担心的低得多\n\n当霍尔木兹海峡的阴影笼罩全球能源市场，3月以来布伦特原油在每桶80-130美元区间剧烈波动时，中国决策者面临一个老问题：如何在外部冲击与内部稳定之间找到平衡。市场普遍关注油价上涨对通胀和消费的冲击，但这份来自某外资投行的研报给出了一个反直觉的核心判断：中国零售燃油价格管理的财政成本是可控的，年化不到GDP的0.3%，且这一成本正在被结构性变量——尤其是新能源汽车的加速渗透——所稀释。\n\n真正值得关注的不是短期油价波动本身，而是中国在应对这场危机中暴露出的定价机制弹性、需求侧的结构性转移，以及政策空间的实际边界。这份报告的深度在于，它没有停留在描述“政府干预了什么”，而是量化了“干预的代价有多大”，并指出了“哪些成本被市场高估了”。\n\n以下是我们从这份研报中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 定价机制的核心不是“补贴”，而是一个精密的非线性传导器\n\n中国成品油定价机制常被外界简单理解为“政府补贴油价”，但报告揭示的框架远比这复杂。其核心是一个以国际原油价格每桶40-130美元为边界的非线性传导系统。\n\n当布伦特原油低于40美元时，国内零售价格不再下调，价差部分进入“风险准备金”，用于节能减碳和油品升级。当高于130美元时，零售价格冻结，政府通过转移支付补偿炼油商损失。而在40-130美元的正常区间内，每桶80美元又构成一个关键阈值：低于80美元时，国际价格变动几乎全额传导；高于80美元时，政府启动“部分传导”机制，要求炼油商通过压缩加工利润来吸收部分冲击。\n\n这个机制的精妙之处在于，它天然具备“自动稳定器”功能。在油价温和上涨时，市场化传导维持了价格信号的有效性；在油价极端波动时，行政干预介入保护实体经济。报告特别指出，自中东冲突以\n\n[... middle omitted ...]\n\n解问题，一起拆解报告中的图表数据，探讨不同情景下的投资含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n国内油价调控，成本比你想的低\n\n油价调控，成本可控\n\n最近国际油价波动很大，国内油价怎么稳住的？成本高不高？翻到一份投行研报，讲得挺清楚。\n\n1️⃣ 核心机制：价格“缓冲带”\n国内零售油价有个40-130美元/桶的“走廊”机制：\n- 国际油价低于40美元：国内不降，差额进风险储备金\n- 高于130美元：国内不涨，政府补贴炼厂\n- 40-130美元之间：80美元是分水岭，以下全额传导，以上部分传导\n\n2️⃣ 传导率：大约一半\n历史数据看，布伦特涨10%，国内汽油柴油大概涨5%。\n最近几个月布伦特在80-130美元区间，实际传导率还低于历史均值——因为发改委有灵活调控。\n\n3️⃣ 实际冲击：需求比想象更敏感\n中东冲突后，3-4月国内油品零售量同比降17%，价格涨17%。\n需求弹性比历史规律更大——新能源车渗透率已到54%，替代效应在加速。\n\n4️⃣ 财政成本：不到GDP的0.3%\n政府干预成本年化约0.3%GDP，而且库存增值和上游利润还能对冲。\n成本可控，不是无底洞。\n\n5️⃣ 进口多元化：俄罗斯+拉美补缺口\n中东进口降38%，俄罗斯+13%，拉美+64%，总量只降11%。\n还在用库存缓冲短期短缺。\n\n新能源替\n\n[... middle omitted ...]\n\nmpression for refiners and even fiscal burdens.   \nChina regulates domestic retail fuel prices through a mechanism anchored by a USD40-130/bbl international crude price corridor. Specifically,\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "锂价短期回调不是反转，真正被低估的是CATL产能释放带来的需求硬缺口",
    "digest": "[wechat_article.md]\n# 锂价短期回调不是反转，真正被低估的是CATL产能释放带来的需求硬缺口\n\n2026年6月初，碳酸锂价格在触及20万元/吨阻力位后出现回调，现货报价从5月底的17.55万元/吨回落至16.83万元/吨。市场情绪随之转弱，部分投资者开始质疑锂价上行动力是否已经耗尽。\n\n但某外资投行最新发布的研报给出了一个与市场直觉相反的判断：基本面并未松动，锂价从当前水平仍有上行空间。支撑这一判断的核心变量，并非市场热议的供给侧减产或政策刺激，而是一个被大多数人忽视的硬需求增量——CATL的新增产能将在2026年8至9月前投产，届时将带来单月约5000至6000吨的增量锂需求。\n\n这不是一个模糊的“需求复苏”叙事，而是一个可以量化的、时间节点明确的供需错配窗口。市场当前的低迷情绪，恰恰为理解这一结构性变化提供了时间差。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 情绪与基本面正在背离：周度数据揭示了什么\n\n截至6月4日当周，碳酸锂和氢氧化锂的现货均价分别环比下跌4.2%和5.5%。从表面看，价格走弱似乎印证了市场对需求疲软的担忧。但拆解周度生产与库存数据后，结论恰恰相反。\n\n产量方面，当周中国碳酸锂产量环比增长3%至26344吨。其中，盐湖提锂产出环比增长1%，锂云母提锂环比下降4%，锂辉石提锂环比增长5%，回收提锂环比增长3%。产量增长并未引发累库，反而库存出现了边际下降。\n\n总库存当周为98786吨，环比减少630吨，降幅约1%。更关键的是库存结构的变化：下游正极材料厂商的库存环比增长7%至46429吨，冶炼厂库存环比下降2%至16615吨，而其他环节（主要是电池厂和贸易商）的库存环比大幅下降8%至35742吨。\n\n这意味着，价格回调期间，下游正在主动补库，而上游和中游的库存压力在减轻。这种库存转移本身就是一个价格支撑信号—\n\n[... middle omitted ...]\n\n球微信群不是信息速递群，而是一个围绕产业逻辑展开对话的圈子。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n锂价短期回调，但基本面没变\n\n锂价回落≠趋势反转\n\n最近锂价从20万/t阻力位回落，市场情绪有点降温。但某外资投行最新研报指出，基本面依然扎实，6月电池产量预计环比再增4%。\n\n关键看三个点👇\n\n1️⃣ 需求端有硬支撑\nCATL今年产量预计达到1.2TWh，同比+61%。新产能将在8-9月前投产，届时会额外拉动5-6千吨锂需求。供需只会更紧。\n\n2️⃣ 库存结构在改善\n截至6月4日，碳酸锂总库存9.88万吨，环比-1%。下游正极材料厂库存+7%，但冶炼厂和贸易商库存分别-2%和-8%。库存正在向下游转移，不是被动堆积。\n\n3️⃣ 供给增速有限\n上周碳酸锂产量2.63万吨，环比+3%。其中锂辉石提锂+5%，但锂云母提锂-4%。高成本产能出清仍在继续。\n\n价格短期承压，但中期上行空间还在。研报维持看多观点，目标价25万/t。\n\n你们觉得锂价这波回调是上车机会，还是需要再等等？欢迎一起讨论👋\n\n#学习笔记\n\n[source_mineru.md]\n04 Jun 2026 11:53:11 ET | 9 pages\n\n# China Battery Materials\n\nLithium into 1st week of\n\n[... middle omitted ...]\n\n26, suggesting an incremental demand of lithium at \\~5-6k tons by that time. We see lithium S/D dynamics should be even tighter going ahead, and lithium price skews to the upside from the curr\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R013",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n中国4月工业增加值同比增速从3月的5.7%骤降至4.1%，远低于市场预期的6.0%，甚至低于某外资投行自己更谨慎的5.2%预测。这一读数创下近三年来的最低月度纪录。市场普遍将其解读为需求疲软，但这份研报提供了一个截然不同的叙事框架：供给冲击才是主因。\n\n报告的核心判断是，中东能源设施受损与霍尔木兹海峡封锁导致的原材料供应中断，已经对中国工业生产造成了结构性伤害。据估算，4月工业增加值增速骤降中，约有一半来自石油和化工两个子行业的直接与间接拖累。这两个行业合计占工业总产出的15%，却贡献了原材料行业40%的产出。\n\n更关键的是，随着美国总统特朗普警告海峡封锁可能持续到9月，这种供给瓶颈在未来几个月内不会自然消退。研报预计5月工业增加值同比增速将维持在4%左右的低位，并将第二季度GDP增速预测下调至4.1%，远低于市场共识的4.7%。\n\n这并非一次短暂扰动，而是一场供给侧压力测试。以下五个层次的分析将揭示：为什么这次供给冲击比表面数据更严重，以及它如何重塑我们对中国经济短期走势的判断框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 石油化工行业的产出收缩并非需求问题，而是原材料断供的直接结果\n\n4月工业增加值的行业分解揭示了一个清晰的传导链条。石油、煤炭及其他燃料加工业的产出增速从3月的8.1%骤降至-0.9%，这是自2024年8月以来的最低水平。原油加工量同比收缩5.8%，较3月的-2.2%进一步恶化。沥青产出量同比暴跌40.1%，而3月这一数字是-19.7%。\n\n化工原材料及制品业的产出增速也从3月的9.0%放缓至5.3%。化学纤维制造业的产出增速降至2.2%，为2023年3月以来最低。这些数据指向同一个问题：原材料进口断供。\n\n报告提供了一组关键数据：4月中\n\n[... middle omitted ...]\n\n供给冲击的传导机制，并持续跟踪后续数据变化对投资框架的影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月工业增速急刹车，源头找到了\n\n原材料断供冲击\n\n4月工业增速从5.7%骤降至4.1%，创近三年新低。拆开看，石油化工是主要拖累。\n\n1/ 石油加工板块直接跌入负增长（-0.9%），原油加工量同比缩5.8%。沥青产量暴跌40%，修路材料告急。\n\n2/ 化工链条受困。原油和LNG是化工原料，进口锐减后，化学原料制品增速腰斩（9%→5.3%）。硫酸（化工之母）产量转负，塑料和化纤产量也同步下滑。\n\n3/ 综合估算，油化板块直接拖累工业增速0.7个百分点，加上间接影响，贡献了4月工业减速的一半左右。\n\n有意思的是，AI相关电子设备增速逆势上行至15.6%，拉动了0.4个百分点。如果没有这块，工业增速会更难堪。\n\n高频数据暗示，5月供应瓶颈仍在延续：\n- 山东地炼开工率从4月底60%降至5月底54.7%\n- 沥青工厂开工率跌至16%，低于去年同期\n- PTA（涤纶原料）开工率从69%骤降至59.3%\n- 下游聚酯长丝开工率同步下行\n\n进口端，4月原油进口量跌至2022年8月以来最低，俄罗斯增量有限。石脑油（化工原料）进口跌51.3%，LNG进口创2018年以来新低，卡塔尔进口几乎归零。\n\n投行研报预计，供应瓶颈可能\n\n[... middle omitted ...]\n\nWe expect IP growth to remain subdued at around $4\\%$ y-o-y in May and maintain our below-consensus Q2 GDP growth forecast of $4.1\\%$ y-o-y (Consensus: $4.7\\%$ ). Though China's stable power s\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R014",
    "title": "市场真正低估的不是地缘风险，而是中国药企已不可替代的全球研发节点地位",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是地缘风险，而是中国药企已不可替代的全球研发节点地位\n\n2026年6月初，港股医药板块在ASCO数据公布后依然呈现“卖事实”的弱势表现。表面看，市场是在消化地缘政治带来的监管不确定性——美国国会接连提出将生物技术纳入COINS法案、引入BINSA法案，试图限制美国资本与中国生物科技公司的交易。但一份来自某外资投行的最新研报提出了一个值得反复推敲的判断：**市场可能严重高估了这些法案的实际影响，同时严重低估了中国药企在全球创新药研发链条中已经形成的结构性位置。**\n\n这不是一个情绪层面的判断，而是一个基于全球R&D投入分布、临床资产供给格局、以及交易对手方利益结构的硬逻辑。报告的核心主张是，如果美国真的选择“脱钩”，受损更大的可能不是中国，而是美国自身的生物技术产业。这个结论听起来有些反直觉，但报告用三组数据链条支撑了这一判断。\n\n我们详细拆解这份报告的核心逻辑，并沿着其分析框架，探讨一个更深层次的问题：这轮地缘博弈，真正考验的是什么？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国已不是“低成本替代”，而是全球最大的创新药早期资产供给方\n\n许多投资者对中国的印象仍停留在“仿制药大国”或“低成本CRO基地”。但报告提供的数据揭示了另一个现实：中国在创新药早期研发阶段的资产供给能力，已经全球领先。\n\n2020年至2025年，中国制药研发支出从260亿美元增长至约390亿美元，年复合增长率8.5%，占全球制药研发支出的比例稳定在11%至13%之间。但更关键的是产出效率——自2020年以来，中国每年进入临床试验的创新药数量已经超过美国，成为全球第一。2024年，中国有722个创新药进入临床试验，而美国为457个。2025年，这一数字进一步拉大到827比482。\n\n这些数字意味着什么？中国已经从一个\n\n[... middle omitted ...]\n\n助读者建立更完整的投资框架。\n\n欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n医药被情绪砸了个坑，值得看看\n\n医药板块被情绪砸了？\n\n📉近期回调，更多是“吓”出来的\n\n1️⃣ 地缘情绪被过度定价了\n某外资投行认为，市场对潜在限制法案的反应可能过度。法案立法流程长、阻力大，最终未必落地。即便落地，对中国药企的license-out合作影响也有限。\n\n2️⃣ 中国研发实力不可忽视\n2025年中国医药研发支出预计达390亿美元，占全球约13%。自2020年起，中国每年进入临床的创新药数量已全球第一。尤其在ADC、双抗等前沿领域，中国企业是重要合作方。\n\n3️⃣ 限制合作，美国伤得更重\n2020-2026年，中国license-out交易中，美国企业占比42%，但贡献了57%的首付款。若切断合作，美国药企将错失大量优质管线，反而推高自身研发成本。\n\n4️⃣ 数据说话：合作仍在加速\n2026年前5个月，中国license-out首付款已达48亿美元，同比增长93%。5月单月首付款12.5亿美元，主要由恒瑞与BMS、信达与辉瑞的交易贡献。\n\n💡 当市场因情绪下跌时，基本面扎实的赛道反而值得多看几眼。\n\n欢迎一起讨论医药板块的后续逻辑～\n\n#学习笔记\n\n[source_mineru.md]\nAsia\n\n[... middle omitted ...]\n\ne potential regulations would likely do more harm than good to the US biotech industry. Furthermore, the legislation would likely be a long and lengthy process, facing significant opposition f\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R015",
    "title": "市场真正低估的不是AI需求，而是数据护城河的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是数据护城河的再定价\n\n这份由某外资投行发布的周度研究报告，表面上覆盖了从AI到油气服务的广泛话题，但贯穿其中的一条暗线值得所有产业决策者停下来思考：**市场对AI的定价正在从“谁在花钱”转向“谁的数据不可替代”**。\n\n报告的核心判断并非来自某个单独的结论，而是来自一个被大多数投资者忽略的结构性信号——当欧洲媒体与互联网分析师Adam Berlin用一套新的AI框架重新评估公司时，得分最高的并非芯片公司，而是那些拥有专有、难以复制的数据库的企业。RELX在10分制中拿到9分，Pearson 8分，Springer Nature 7.5分。而这些公司恰恰被市场错误地归类为“AI风险敞口”标的。\n\n这个信号意味着什么？AI的竞争正在从算力军备竞赛转向数据资产的深度变现。而这一转变，将对当前市场对AI产业链的定价逻辑产生根本性冲击。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 半导体集中的经济价值不可持续，数据层才是真正的价值洼地\n\n报告中最值得反复咀嚼的判断来自Jim Covello：半导体领域的经济价值集中是不可持续的。这并非唱空芯片，而是在提醒一个被忽视的结构性问题——当前AI投资回报的最大瓶颈不在算力，而在数据结构和编排。\n\n报告明确指出，尽管企业级AI投入巨大，但效果参差不齐。问题的核心在于，大多数企业还没有建立起能够真正释放AI价值的数据基础设施。这解释了为什么Adam Berlin的AI框架将“专有、难以复制的数据库”作为核心评分维度。\n\n从投资角度看，这意味着当前市场对AI产业链的估值分布存在系统性偏差。半导体公司享受了AI叙事带来的绝大部分估值溢价，而真正掌握数据护城河的企业却被市场错误地贴上了“AI风险”的标签。这种定价错位的修复，可能成为未来12-18个月最重\n\n[... middle omitted ...]\n\n重估。我们会在群里分享完整的图表分析和对关键假设的验证进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# AI投研的新视角：别只看半导体\n\n**换个角度看AI**\n\n---\n\n最近看了一份外资投行的研报，有几个观点值得拿出来聊聊。\n\n**1/ AI的价值集中度不可持续**\n目前AI的经济价值高度集中在半导体环节，但这种结构并不健康。数据架构和编排能力才是企业真正落地AI的关键。虽然企业花了大钱，但AI应用的效果参差不齐——好的很好，但大部分还停留在\"试试看\"阶段。\n\n**2/ AI护城河比想象中深**\n媒体和互联网领域的AI颠覆风险被高估了。研报指出：拥有专有、难复制的数据库（特别是法律等敏感领域）的公司，反而能建立更牢固的AI护城河。比如某信息服务商，AI框架评分高达9/10，却被市场错误地归类为\"AI风险股\"。\n\n**3/ 别忘了传统能源的故事**\n市场注意力太窄了。石油服务领域正在酝酿机会——国际石油公司开始愿意增加勘探支出。地震勘探行业经过整合后，一旦需求回暖，定价权会很强。这不仅是地缘政治驱动的短期交易，而是有基本面支撑的结构性变化。\n\n**4/ 法拉利的电动化逻辑**\n法拉利推出新电动车型后股价承压，但研报认为：个性化定制能力持续强劲，ASP（平均售价）仍有上升空间。电动化是\"加法\"而非\"替代\"。\n\n[... middle omitted ...]\n\nof this year. More below and a podcast version with the analysts on the new additions here.\n\nAI – a different lens on the theme overall... We spent time with Jim Covello this week which brough\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "中国科技股的核心机会不在下游，而在上游的设备与封测",
    "digest": "[wechat_article.md]\n# 中国科技股的核心机会不在下游，而在上游的设备与封测\n\n五月中国科技板块反弹18%之后，市场对近期回调的看法分化。多数讨论集中在AI应用、消费电子复苏节奏和芯片设计公司的估值上。但某外资投行最新研报给出的判断与此不同：当前真正值得加仓的，不是下游的芯片设计或终端组装，而是上游的半导体设备、封测和代工。这个排序的逆转，背后是供应链利润分配的结构性变化。\n\n这份研报将半导体子行业的优先顺序重新排列为：半导体设备大于封测，封测大于代工，代工大于无晶圆设计。对于长期关注中国科技股的投资者而言，这个排序的变动意味着什么？它是否暗示了市场共识的盲点？\n\n简单说，上游企业的订单可见度正在从“季度”拉长到“两年”。下游企业的利润则面临成本上升和需求分化的双重挤压。这不是一个短期的交易信号，而是一个可能持续到2027年的结构性配置逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 半导体设备的增长可见度正在从“季度”拉长到“两年”\n\n研报给出的核心数据是：2026年，本土WFE（晶圆前端设备）供应商来自存储和先进逻辑的需求，预计将分别同比增长超过50%和30%，且2027年还有进一步上行空间。这个判断的底层支撑，是长鑫存储和长江存储的IPO时间表推进——这两家企业的资本开支计划正在从“不确定”变为“可预期”。\n\n更关键的是，这个增长周期与以往不同。过去中国半导体设备公司的订单多依赖单一客户的扩产节奏，波动大、可预测性差。但本轮驱动因素更加多元：存储扩产之外，本土AI芯片从2026年下半年开始进入量产爬坡期，将带动后端设备（先进封装、测试等）的增量需求。这意味着设备公司的收入来源正在从“单引擎”变为“双引擎”，增长的可预测性显著提升。\n\n对于估值而言，这带来的不是简单的盈利上调，而是估值框架的切换——从“周期股”切换到“成长股”\n\n[... middle omitted ...]\n\n能见度和封测涨价传导的量化分析，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国科技板块，选上游更稳妥\n\n🧠 上游更稳，下游要挑\n\n某外资投行最新研报拆解了中国科技板块的机会，核心逻辑很清晰：**上游确定性更高，下游要精挑细选。**\n\n1️⃣ **半导体设备：订单最扎实**\n- 存储和先进逻辑的本地设备需求，预计2026年同比增长超50%和30%，2027年还有空间\n- 国产AI芯片放量（2H26起），后端封测设备也会受益\n- 订单能见度拉长，估值有支撑\n\n2️⃣ **封测/代工：涨价红利来了**\n- 产能利用率高+材料成本传导，2Q26持续涨价\n- 折旧压力虽在，但涨价能驱动利润率从2H26开始改善\n- 尤其是AI相关（GPU、PMIC）的封测厂受益更大\n\n3️⃣ **下游：结构分化明显**\n- 云服务商AI投资依然强劲，汽车和工业在2Q26回暖\n- 但消费电子（安卓手机、AIoT）需求在走弱\n- 成本上涨压力下，依赖消费电子又无法转嫁成本的Fabless公司压力最大\n\n4️⃣ **几个值得关注的方向**\n- AI芯片：某国产AI芯片公司供应稳定，客户和产品有突破\n- 半导体设备：存储和逻辑厂资本开支强劲，国内设备龙头受益\n- 苹果链：高端iPhone机型（17/18 Pro系列）\n\n[... middle omitted ...]\n\necking order for Semi space which is now: Semi equipment $>$ OSAT $>$ Foundry $>$ Fabless. Iluvatar CoreX, Naura, AMEC, Luxshare and Cowell are our top picks in the China Tech space.\n\n\\- Semi \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R017",
    "title": "GLP-1口服药的战场，IQVIA数据正在低估真实竞争烈度",
    "digest": "[wechat_article.md]\n# GLP-1口服药的战场，IQVIA数据正在低估真实竞争烈度\n\n过去两个月，GLP-1赛道最受关注的话题已经从“谁在减重效果上更优”转向“口服药能否真正打开增量市场”。每周处方数据追踪，看似枯燥的数字波动，背后却隐藏着两个关键判断：第一，市场正在用注射剂的逻辑来评估口服药，这可能导致对需求潜力的系统性低估；第二，由于IQVIA数据捕获率存在显著偏差，投资者对两款核心口服药——诺和诺德的Wegovy Pill和礼来的Foundayo——的竞争态势判断，可能正在偏离真实情况。\n\n某外资投行最新发布的周度追踪报告，虽然标题只提到“长周末影响周处方量”，但仔细拆解后会发现，这份报告真正有价值的部分，不在于那6%的周环比下降，而在于它揭示了一个尚未被充分定价的结构性变量：口服GLP-1的处方数据捕获率差异，正在扭曲市场对两款药物相对表现的认知。本文基于该报告的核心数据与逻辑框架，提炼出几个值得产业决策者和投资者认真对待的洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 周度处方波动是噪音，真正重要的是口服药渗透率正在加速提升\n\n截至5月29日当周，GLP-1类药物的总处方量为244万张，环比下降约6%。报告明确指出，这一下降与长周末有关，属于预期内的季节性扰动。如果只看这一周的数据，很容易得出“市场增长趋缓”的错误结论。\n\n真正值得关注的信号是：4周同比增速仍维持在39.2%的高位，与上周的39.3%几乎持平。这意味着，即便剔除短期波动，GLP-1的整体需求仍在以接近40%的年化速度扩张。更关键的是，这一增长的主要驱动力正在从注射剂转向口服药。\n\n从市场份额结构看，礼来整体（Zepbound、Mounjaro、Foundayo合计）在总处方量中的占比已达59.7%，诺和诺德为40.3%。但口服药的渗透率变化才是决定未\n\n[... middle omitted ...]\n\n整报告的原始图表与数据源，并持续追踪每周处方数据的变化趋势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nGLP-1口服药最新战报：诺和礼来谁跑得更快？\n\n口服GLP-1赛道最新数据出炉\n\n5月底受长周末影响，整体处方量环比下降约6%。但新玩家Foundayo（礼来口服GLP-1）第8周处方量16,982，环比增长6.1%，仍在爬坡期。\n\n1️⃣ 整体市场格局\n- 周处方总量244万，环比降5.67%\n- 4周同比增速39.2%，基本持平\n- 礼来市占59.7%（Zepbound 26.4%+Mounjaro 32.6%+Foundayo 0.7%）\n- 诺和诺德市占40.3%（Wegovy针剂13.3%+口服5.8%+Ozempic 21.2%）\n\n2️⃣ 口服药竞争关键点\n- Wegovy口服本周13.4万处方，环比降8%\n- Foundayo第8周1.7万处方，但IQVIA捕获率仅约70%\n- 诺和在股东大会上透露：Wegovy口服第10周处方量是Zepbound的3倍（但IQVIA数据仅显示1.6倍）\n- IQVIA对Wegovy口服的捕获率可能仅50%（类似Zepbound瓶装上市初期）\n\n3️⃣ 礼来Foundayo的独特挑战\n- 这是一个全新分子，不是semaglutide的延伸\n- 医生教育需要时\n\n[... middle omitted ...]\n\ne80eeb07da8a443dba0077.jpg)\n\nChristian Moore\n\n+1 917 344 8555\n\nchristian.moore@bernsteinsg.com\n\nThis week's scripts were (as expected, and flagged previously) impacted by the long weekend, and\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R018",
    "title": "保险股反弹背后，市场真正低估的是渠道结构重塑的定价权",
    "digest": "[wechat_article.md]\n# 保险股反弹背后，市场真正低估的是渠道结构重塑的定价权\n\n如果你在过去三个月看到中国保险公司的股价反弹，自然会问一个问题：这是跟着A股大盘走的贝塔，还是行业基本面发生了结构性改善？\n\n某外资投行在5月底对中国主要保险公司进行了一轮深度调研，覆盖平安、太保、太平、众安、国寿、新华和人保财险。调研的结论可以浓缩为一句话：行业基本面确实在变好，但变好的方式比多数人想象的更微妙——不是单纯靠股市上涨拉高投资收益，而是渠道费用监管收紧正在悄悄改变竞争格局，让大型保险公司重新拿回定价权。\n\n这份调研释放的信号，值得认真拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 银保渠道的“监管红利”正在重塑寿险竞争格局，大型险企是最大受益者\n\n2025年3月，国家金融监管总局发布了银保渠道费用新规。这次调研中，所有寿险公司都对这一政策表达了欢迎态度。这不是客套话，而是有实质含义的。\n\n过去几年，银保渠道的竞争本质上是费用战。中小保险公司为了抢占银行网点，不惜以高额手续费换取规模，导致整个渠道的利润率被压得很低。新规的核心在于对渠道费用进行更精细化的审查，这直接抬高了中小公司的竞争门槛。\n\n大型险企的逻辑很清楚：银行在费用受控的条件下，会更倾向于与偿付能力充足、品牌认知度高、能够提供长期服务的大型保险公司合作。这不是猜测，而是已经在发生的事实。以中国太平为例，其银保渠道的VONB贡献在2025年约为35%，但管理层明确表示这个比例有潜力逐步提升到50%。太平人寿已经是银保渠道前七大寿险公司之一，这恰恰是监管整顿后的结果。\n\n当然，监管红利不是免费的午餐。多家公司都承认，短期内销售激励的减少会造成一定的业务扰动。国寿在经历了2026年一季度VONB同比增长75%的异常高增长后，管理层预计后续增速会回归正常，部分原因就是银保新规带来的\n\n[... middle omitted ...]\n\n星球微信群里继续讨论，一起追踪这些关键变量的变化。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n保险投研：5月调研后的几个判断\n\n封面标题：保险调研笔记\n封面副标题：5月线下交流后的关键信号\n\n先说结论：某外资投行近期调研了国内多家保险机构，整体判断行业基本面比较扎实。寿险新保单销售有持续性，财险承保也在改善，叠加权益市场反弹，利润和净资产都在恢复。\n\n几个核心观察：\n\n**1. 渠道与竞争格局**\n寿险公司对银保渠道增长有信心。3月出台的银保渠道费用新规，大公司普遍欢迎——更严格的费用审查会推动银行倾向与大保司合作。虽然短期销售激励减少可能带来扰动，但利润影响不大，省下的成本大概率让利给客户。\n\n代理人队伍方面，未来2-3年人数预计稳定，重点在提升高质量代理人的产能。尽管银保增长快，但多数公司认为代理人更适合服务高净值客户。\n\n**2. 投资策略：红利股是主线**\n3月底以来权益市场走强，带动保险公司投资收益反弹。但多数公司不打算大幅加仓权益，更倾向维持现有水平，在成长股和红利股之间做平衡配置。\n\n长期国债仍是拉长久期的重要工具，但利率偏低，大家更关注高股息股票——能提供类债券的收益和久期。目标股息率普遍在4%以上。部分公司OCI账户中权益投资占比已升至约30%。\n\n**3. 财险承保：空间仍在**\n\n[... middle omitted ...]\n\nbound in investment results, but insurers mostly see stable equity allocation at the current level, emphasizing a balanced portfolio between growth and dividend stocks. P&C insurers generally \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "AI基础设施的供给瓶颈，正在从芯片设计延伸至整个物理供应链",
    "digest": "[wechat_article.md]\n# AI基础设施的供给瓶颈，正在从芯片设计延伸至整个物理供应链\n\n这份来自某外资投行的研报，在Broadcom 2Q26财报后第一时间更新了对AI半导体产业链的判断。表面上看，它是对一家公司业绩的追踪。但当我们把数字背后的信号串联起来，一个更重要的结构性叙事浮现出来：AI基础设施的竞争，已经从“谁的芯片算力更强”进入了“谁能锁定物理世界的供应”阶段。\n\n报告中最值得关注的判断，不是Broadcom AI收入突破100亿美元的时间表，而是管理层披露的AI半导体订单积压已超过300亿美元，且订单能见度已延伸至2028年。客户之所以提前下单，不仅是为了锁定晶圆和HBM产能，更是为了确保电力基础设施的配套到位。这是一个信号：AI基础设施的供给瓶颈，正在从硅片层面蔓延到整个物理世界。\n\n以下，我们从四个层次来拆解这份报告的核心洞察，并在最后提出一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订单能见度延伸至2028年，供应链约束正在从晶圆向物理基础设施转移\n\n报告中最硬核的数字，是Broadcom AI半导体季度订单积压超过300亿美元。管理层明确表示，客户正在提前下单，原因不仅仅是晶圆和HBM的交付周期长，更关键的是电力基础设施的配套周期。\n\n这指向一个被市场低估的变化：AI基础设施的供给约束，正在从“芯片产能”向“数据中心电力容量”迁移。当电力成为瓶颈，客户不得不提前数年锁定芯片供应，以确保在拿到电力配额时，配套的计算设备已经就位。反过来，这也意味着芯片供应商的订单能见度被大幅拉长。\n\n报告提到，这份研报的亚洲供应链调研确认，3至5年的长期协议已经越来越多地覆盖基板、HBM和CCL等关键瓶颈环节，而先进制程晶圆仍维持年度谈判周期。这隐含了一个判断：供应链约束的关键变量，正在从台积电的Co\n\n[... middle omitted ...]\n\n享完整的研报解读、原始图表，以及围绕这些未解问题的持续追踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI芯片格局要大洗牌了\n\n博通财报里的关键信号\n\n最近翻了某外资投行关于博通最新财报的研报，信息量很大。核心结论是：AI芯片的供应链正在从单一依赖走向多元化，一批新玩家正在崛起。\n\n1. **AI收入翻倍，但订单被“抢”走了**\n博通AI收入达108亿美元，同比增长143%，管理层还指引下半年收入翻倍，FY27目标超1000亿美元。但研报指出，博通在谷歌TPU项目上可能正在失去份额，因为联发科（MTK）将其ASIC（专用芯片）时间表提前了一年。这说明，大客户不想只吊在一棵树上。\n\n2. **供应链多元化，谁是赢家？**\n管理层承认，谷歌会保持TPU/AI计算栈的供应商多元化。研报认为，未来大型云服务商（CSP）找2-3家后端设计服务商将成为常态。这意味着，像联发科和世芯（Alchip）这样的“半定制化”模式玩家，凭借其结构性较低的毛利率（40%+），可能成为关键受益者。相比之下，那些提供全定制化服务、毛利率60%+的厂商，可能会面临压力。\n\n3. **AI预订量超300亿美元，订单看到2028年**\n博通披露单季AI半导体预订量超300亿美元，客户因为长交期在提前下单。更重要的是，管理层说现在能看清2028年\n\n[... middle omitted ...]\n\nc (additional TPU-based compute beginning 2027), OpenAI (production in late 2026 with contractual deployments in 2027), and Meta (MTIA XPU partnership; initial 1GW order with deliveries starti\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 04 Jun 2026 02:41 PM HKT\n\nDisseminated 04 Jun 2026 02:41 PM HKT"
  },
  {
    "id": "R020",
    "title": "ASCO 2026第三天：市场低估的不是PD-1/VEGF组合的竞争，而是IL-2赛道“可成药性基准”的转移",
    "digest": "[wechat_article.md]\n# ASCO 2026第三天：市场低估的不是PD-1/VEGF组合的竞争，而是IL-2赛道“可成药性基准”的转移\n\n每年ASCO的第三天，往往是泡沫退潮、信号浮现的时刻。前两天的喧嚣过后，临床数据开始接受更冷静的拆解。\n\n某外资投行在ASCO 2026第三天发布的研报，表面上是一份常规的会议纪要，但细读之下，它揭示了一个正在发生的结构性变化：中国创新药行业正在从“跟随式创新”进入“基准定义”阶段。这个判断，比任何单个分子的数据都更重要。\n\n市场当前关注的焦点是PD-1/VEGF双抗的竞争格局，但报告真正值得重视的信号，是IL-2赛道正在经历的“可成药性基准”的转移。谁定义了基准，谁就掌握了下一轮定价权。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PD-1/VEGF的竞争已进入“数据细节决定估值分化”的阶段\n\nHB0025在1L鳞状NSCLC中交出了ORR 84.5%、mPFS 16.46个月的数据。单看数字，这组数据在同类分子中具有竞争力。但报告明确指出，存在几个需要谨慎解读的“caveats”：患者分期的偏倚、PD-L1表达水平的分布差异、以及低转移负荷患者的比例偏高。\n\n这意味着什么？意味着PD-1/VEGF这个赛道的竞争，已经从“有没有疗效”进入了“疗效是否经得起亚组分析”的阶段。对于投资者而言，这不再是一个“买赛道”的逻辑，而是一个“挑分子”的逻辑。\n\nAK112的Ph2数据作为参照系，HB0025的疗效信号需要放在同样的患者基线下去比较。报告没有给出结论，但暗示了方向：在鳞癌PD-L1<1%的患者中，mPFS达到16.72个月，这一信号如果能在更大样本中复现，将具有临床意义。但G3+蛋白尿和TRAE死亡事件的存在，说明安全性窗口仍是这类分子的核心挑战。\n\n所以呢？PD-1/VEGF双抗的估值分化已经\n\n[... middle omitted ...]\n\n是建立一套能够区分“基准定义者”和“基准跟随者”的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nASCO第三天，这些靶点值得深挖\n\nPD-1/IL-2双抗的进与退\n\nPD-1/IL-2赛道，ANV600和AWT020都给出了验证数据，但βγ设计的IL-2分子依然受限于剂量窗口。IBI363作为可药性标杆，在2线免疫耐药EGFRwt非鳞NSCLC中，3mg剂量显示出OS优势，支持注册路径。\n\nPD-(L)1/VEGF组合的新信号\n\nHB0025 20mg/kg Q3W联化疗，在1线NSCLC中展现高活性。鳞癌亚组尤其亮眼：ORR 84.5%，mPFS 16.46个月，PD-L1<1%和≥1%患者的mPFS几乎一致（16.72 vs 16.46个月）。但需注意，与AK112的Ph2数据比，存在PD-L1、分期和低转移率的偏倚，G3+蛋白尿和TRAE死亡也是隐忧。\n\nRASolute302的2线管理启示\n\n停药率仅1.2%（化疗组11.2%），中位剂量强度93.1%。皮疹（17%）和口腔炎（6.6%）是主要减量原因。1线设计的核心争论点：单药vs联合vs SOC/维持，以及不同分子的临床表型差异。\n\n欢迎一起讨论这些靶点的临床设计逻辑。\n\n#学习笔记\n\n[source_mineru.md]\n## China \n\n[... middle omitted ...]\n\nvs. allele-specific depth; 1L focus echoes Day 2 on mono vs combo/SOC/maintenance design.\n\n## Posters:\n\n- PD-(L)1/IL-2: ANV600 dosing remained confined to g/kg - with activity mixed across reg\n\n[... middle omitted ...]\n\n Co. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb12.08</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "减肥药热潮的真正瓶颈不在需求，而在多肽制造的绿色化能力",
    "digest": "[wechat_article.md]\n# 减肥药热潮的真正瓶颈不在需求，而在多肽制造的绿色化能力\n\n市场对GLP-1类药物的关注几乎全部集中在需求端：全球肥胖药物支出预计在2025-2029年间以20%以上的年复合增速增长，到2029年突破800亿美元，向千亿美元门槛逼近。但某外资投行最新发布的医疗健康周报揭示了一个被严重低估的结构性矛盾——多肽制造的可持续性瓶颈。这不是一个遥远的ESG议题，而是未来3-5年决定哪些CDMO能真正兑现产能扩张、哪些制药企业能锁定稳定供应链的核心变量。\n\n报告的核心判断是：**多肽API制造的高溶剂消耗和高过程质量强度（PMI），正在成为制约产能有效扩张的隐形天花板。** 每生产1公斤GLP-1类多肽API，平均消耗约14吨溶剂，而典型小分子药物的这一数字仅为0.3吨。当行业从公斤级向多公吨级跃迁时，这种效率差距将直接转化为成本劣势、产能瓶颈和环境负债。\n\n这不是一次技术路线的渐进改良，而是对多肽制造底层逻辑的重塑。那些率先掌握绿色合成工艺的CDMO，将在未来5年获得显著的竞争壁垒。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 多肽已成新药模态中规模最大、增速最快的赛道，但制造端的“脏活”被低估了\n\n到2030年，多肽药物的市场规模预计将达到1200亿美元，年复合增长率18%，在新型药物模态中规模最大、增速仅次于寡核苷酸和双抗。这一增长的绝对主力是GLP-1类药物——Semaglutide、Tirzepatide、Liraglutide三大品种已经将多肽从学术研究和化妆品原料的细分市场，推升为制药制造的核心赛道。\n\n但报告明确指出了硬币的另一面：多肽API被美国化学会绿色化学研究所明确标记为“最不可持续的药物模态之一”。固体相多肽合成（SPPS）虽然是当前商业标准，但其过程质量指数（PMI）高达13,000以上——这\n\n[... middle omitted ...]\n\n的规模经济拐点？我们会在群内分享更多独家分析框架和数据追踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nGLP-1减肥药，制造端藏着一个大问题\n\n减肥药制造，比想象中更“脏”\n\n全球减肥药市场正冲向1000亿美元，但制造这些多肽药物的过程，却是个环境难题。\n\n1/ 多肽药有多火？\n到2030年，多肽类药物市场规模预计达1200亿美元，增速18%，在所有新药模式中独一档。GLP-1减肥药是核心驱动力，仅2025-2029年就将新增500亿美元支出。\n\n2/ 制造端的“脏活”\n生产1公斤GLP-1类多肽原料药，需要消耗14吨溶剂！而普通小分子药只要0.3吨。有机溶剂如DMF、二氯甲烷的使用量惊人，环保压力巨大。\n\n3/ 三大挑战\n- 高溶剂消耗侵蚀利润：CDMO若不能降本，规模越大越被动\n- 批次纯化效率低：5天变1天的技术已有，但多数企业还在用老方法\n- ESG监管趋严：药企开始要求供应商提供绿色合成方案\n\n4/ 破局者已出手\n投行研报指出，头部CDMO正通过三种方式降本增效：\n- 连续色谱技术：溶剂消耗降30%，材料使用降70%\n- 溶剂回收+工艺优化：某CDMO将PMI（工艺质量强度）做到行业平均的1/3\n- 绿色合成路线：用更安全的溶剂替代DMF\n\n欢迎一起讨论：减肥药赛道这么热，制造端的环保成本会不会成为\n\n[... middle omitted ...]\n\nernsteinsg.com\n\nLance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com\n\nDelphine Le Louet +33 1 42 13 92 93 delphine.le-louet@bernsteinsg.com\n\nRelated reading - Weekend Healthcare Pulse: GL\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R022",
    "title": "市场真正低估的不是卡组织费率，而是“信任即服务”的定价权",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是卡组织费率，而是“信任即服务”的定价权\n\n关于银行卡收单费率（Merchant Discount Rate, MDR）的讨论，几乎每隔一段时间就会在支付行业掀起一轮争论。反对者认为，2.4%的信用卡费率是美国商户的沉重负担，稳定币、即时支付等替代方案将终结卡组织的“超额利润”。支持者则强调，卡支付带来的争议处理、欺诈保护、全球通用性等增值服务，远非简单的资金转移可比。\n\n这份来自某外资投行的周末技术简报，用一个看似老生常谈的费率问题，揭示了支付行业最核心却最容易被误解的结构性事实：**市场对卡组织费率的焦虑，本质上混淆了“资金转移”与“信任服务”两种完全不同的价值定价**。而真正决定未来十年支付格局的，不是费率高低，而是谁能把“信任”这个抽象资产，转化为可规模化的商业模型。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 费率对比中最常被忽略的前提：借记卡与信用卡根本是两种商品\n\n许多关于卡支付“昂贵”的批评，从一开始就站错了比较基准。该报告明确指出，借记卡与信用卡在功能上完全是两回事。借记卡对应的是“你已有的钱”，是资金转移；信用卡对应的是“你还没有的钱”，是信用延伸。\n\n这一区分至关重要。当人们拿“银行直付”（pay-by-bank）或稳定币与信用卡比较时，实质是在拿一种资金转移工具，去对标一种集成了信用、奖励、争议处理、欺诈保障的复合服务产品。数据显示，美国受监管的借记卡平均MDR仅为0.7%，远低于信用卡的2.4%。即便加上不受监管的借记卡部分（约占全美借记卡交易量的三分之一），其费率也仅在1.7%左右，仍然低于信用卡。\n\n在欧洲，这一对比更加鲜明。欧盟对借记卡和信用卡的交换费（interchange fee）分别设有约20个基点和30个基点的上限，卡支付的总体费率在全球属于最低水平之\n\n[... middle omitted ...]\n\n群里继续讨论，我们可以一起拆解这些未解问题背后的数据和逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n信用卡收费，真的贵得没道理吗？\n\n**费率的“潜台词”**\n\n**一张卡背后的成本，比你想象的复杂**\n\n1/ 刷信用卡，商户要交2.4%的手续费；刷借记卡，只要0.7%。乍一看，信用卡真贵。但别忘了，借记卡花的是你账上已有的钱，信用卡花的是银行借给你的钱。两者本来就不是同一类产品。欧洲的信用卡费率低到0.5%，但那里大部分交易用的都是借记卡——拿信用卡跟借记卡比费率，有点像拿打车跟坐公交比价格。\n\n2/ 信用卡那2.4%里，真正落到卡组织手里的只有0.23%。剩下的大头去了哪里？发卡行要覆盖奖励积分（约3%）、欺诈损失（约1.5%）、争议处理（约1.2%）、资金成本（约2.5%）。这些服务，稳定币和银行直付目前都做不到——稳定币交易不可逆，没有争议处理机制；银行直付没有积分体系。如果要把这些服务都加上，成本自然也会上去。\n\n3/ 有意思的是，欧洲在2015年把借记卡费率限制在0.2%、信用卡0.3%之后，卡渗透率反而从33%飙到了77%。说明合理的费率上限，其实能刺激更多商户接受卡片，把蛋糕做大。\n\n4/ 美国现在有点微妙。小商户的信用卡费率经常超过3%，导致34%的小商户开始对信用卡交易额外收费（surc\n\n[... middle omitted ...]\n\nam.chhugani@bernsteinsg.com\n\nLaurent Yoon +1 917 344 8502 laurent.yoon@bernsteinsg.com\n\nViola Chen +1 917 344 8614 viola.chen@bernsteinsg.com\n\nSimran Ratani +1 917 344 8329 simran.ratani@berns\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R023",
    "title": "日本汽车业IT投资正在踩刹车，但这恰恰暴露了另一条增长主线",
    "digest": "[wechat_article.md]\n# 日本汽车业IT投资正在踩刹车，但这恰恰暴露了另一条增长主线\n\n一份来自某外资投行的研报，通过对三家非覆盖公司（Systena、Argo Graphics、DIT）的实地调研，揭示了一个正在发生的结构性变化：日本汽车行业的IT投资意愿正在快速降温。但比这更重要的是，这份报告同时指向了一个被市场低估的替代增长引擎——金融行业的核心系统更新需求。\n\n这不是一份关于“日本IT服务行业整体好不好”的报告。它的真正价值在于，它用三家公司的微观数据，拆解了“谁在收缩、谁在扩张、以及收缩与扩张之间的传导逻辑”。对于跟踪日本IT服务板块的投资者来说，这份报告提供了一个关键的观察框架：在汽车行业这个传统大客户的IT支出放缓时，哪些公司有能力完成切换，哪些公司会被困在原地。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 汽车行业的IT投资收缩不是偶发现象，而是三个信号叠加的结果\n\n研报中三家公司给出的信息高度一致，但程度不同。Systena说“部分整车厂的投资意愿正在减弱”；Argo Graphics直接给出了六年来首次营业利润同比下降的指引，原因是“主要汽车客户的投资受到抑制”；DIT的情况更严峻，其嵌入式解决方案业务的销售额和毛利润在3Q均出现同比下降，且公司明确表示“主要汽车客户的投资意愿正在迅速下降”。\n\n这不是一个公司的个案，而是一个行业层面的信号。三个公司分别覆盖了车载系统集成（Systena、DIT）和汽车CAD/半导体相关系统（Argo Graphics），它们的共同指向是：日本汽车行业正在经历一轮IT投资的周期性回调。\n\n这意味着什么？对于投资者而言，需要重新审视那些汽车行业收入占比较高的IT服务公司的盈利预期。虽然报告指出目前没有大型系统集成商对汽车行业的销售敞口特别高，但这恰恰是风险所在——当风险分散在多个子\n\n[... middle omitted ...]\n\n具体公司的投资逻辑有进一步疑问，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本汽车IT风向变了？三家公司业绩拆解\n\n📉 汽车IT投资降温\n\n某外资投行近期调研了三家日本汽车/制造IT服务商，发现：汽车客户的投资意愿正在减弱，这对整个IT服务板块来说是个小信号。\n\n1️⃣ Systena（车载系统/SI）\n- 移动出行和金融领域开发项目依然景气\n- 但FY3/27营业利润仅微增4%（主要受股权激励成本影响）\n- 核心业务EBITDA预计仍能双位数增长\n- 汽车SDV（软件定义汽车）投资需求强劲，但不同客户态度分化\n\n2️⃣ Argo Graphics（汽车CAD/半导体）\n- FY3/27营业利润预计同比-4%，六年来首次下滑\n- 汽车客户投资收紧，加上数据中心折旧增加\n- 半导体客户投资有回暖迹象（北海道/九州/三重工厂扩产）\n- PLM业务增长乏力，HPC靠大项目支撑\n\n3️⃣ DIT（车载系统）\n- 3Q营业利润连续第二个季度下滑（-5%）\n- 汽车客户投资意愿快速下降，开发+验证业务都承压\n- 公司表示这一趋势可能延续到FY6/27\n\n📌 关键观察\n虽然没有大型SI商高度依赖汽车行业，但那些服务多行业的系统集成商（如富士通、NEC）值得关注。汽车IT投资的降温，可能引发连锁反\n\n[... middle omitted ...]\n\npment projects for the mobility and financial sectors, but the company sees FY3/27 operating profits growing only modestly, due to an increase in share-based compensation costs from the issuan\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Divergent year-to-date performance across DXY and our Dollar TWI is testament to divided recent Dollar performance 2026 Year-to-Date GS USD TWI and DXY Composition"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: High-beta energy importer currencies would likely benefit most from a resolution to the conflict, unwinding their recent outperformance USD/XXX Vulnerabilities to Terms of Trade Shifts vs Risk-Off Shifts (Larger Bubble"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: INR carry is now higher than for other Asia high-yielders (IDR and PHP), ZAR and MXN"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The 1y1y point has typically led on the US curve during sharp inflections in front-end rates 3m change in 2y swap rate vs 1y/1y1y/2y1y swap fly return (higher = belly underperforms)"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Solid YTD Money Fund AUM growth reflects the higher-for-longer front-end yields"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The recent decline in traded inflation has outpaced what the macro and energy pricing imply Fair value model based on energy prices, core inflation, the euro currency and the level of nominal yields"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Signals for Gilt spreads suggest supply is not the key issue for Gilts Fair value model based on repo-ois spread, rates volatility, free float, the level of yield and the curve"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Hawkish BoJ policy innovations typically result in bear flattening consistent with a more front-loaded policy reaction JGB Curve Betas* to Changes in 3m OIS"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Japanese investors (excluding the MoF) hold nearly \\$6tn of foreign assets, with the majority mostly unhedged"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Data from Post Bank and GPIF financial reports, the BoJ's April FSR, and Flow of Funds data (Outward Investment in Securities + Investment Trust Beneficiary Certificates) as of Q4 2025."
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: While the ITS data show that Banks flows have turned negative since the start of the year..."
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ...the more-lagged FOF data have yet to confirm any shift"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The timeliest data suggest that GPIF and the private pensions have continued buying foreign debt while selling foreign equities"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: While JGB yields have risen more than UST yields over the past year, the differential remains negative"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 30-city daily property transaction volume in the primary market was roughly flat over the last week but remained above year-ago level"
  },
  {
    "figure_id": "F016",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: 16-city daily property transaction volume in the secondary market declined but remained above year-ago level"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: China's passenger flights for domestic routes declined and remained below year-ago level"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China's passenger flights cancellation rate increased over the last week *11.3%*"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Traffic congestion edged down over the last week"
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Domestic gasoline and diesel prices were adjusted downwards by 525 and 505 RMB/tonne respectively on June 4"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Prices for sulfuric acid slightly edged up over the last week while other exposed chemicals stabilized somewhat"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: The Morning Consult consumer confidence edged up to multi-year high"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Weighted PMI employment sub-index edged up in May"
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Steel demand edged down over the past week"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Steel production edged down over the past week"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Daily coal consumption in coastal provinces increased further over the last week and remained above year-ago level"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: RMB 1.50bn local government special bonds have been issued year-to-date"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: PSL loans outstanding contracted in May 2026 PSL: Net injection vs outstanding amount"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Official port container throughput rose over the last week and was above year-ago level"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Freight volume of departing ships at 20 major ports rose over the past week and was above year-ago level"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Our nowcast indicates China oil demand increased to 16.5mb/d in the latest reading"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 18",
    "context": "Exhibit 18: China visible landed crude inventories declined somewhat over the last week"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Interbank repo rates remained low"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 20",
    "context": "Exhibit 20: CNY appreciated against both the USD and the CFETS basket over the past week"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 21",
    "context": "Exhibit 21: USDCNY fixing implied countercyclical factor remained rangebound over the past week"
  },
  {
    "figure_id": "F036",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: MS A-share Sentiment Indicator: MSASI weighted and MSASI weighted 1MMA"
  },
  {
    "figure_id": "F037",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: MS A-share Sentiment Indicator: MSASI weighted and MSASI weighted 1MMA"
  },
  {
    "figure_id": "F038",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: MSASI trajectory since January 1, 2019"
  },
  {
    "figure_id": "F039",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ChiNext turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F040",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 5: A-share turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F041",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Equity futures turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F042",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Margin transactions adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F043",
    "report_id": "R006",
    "label": "Exhibit 10",
    "context": "Exhibit 10: RSI-30D since January 2014 vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F044",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Northbound turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F045",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 9: SSE new accounts adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F046",
    "report_id": "R006",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Number of limit-up A-shares adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F047",
    "report_id": "R006",
    "label": "Exhibit 12",
    "context": "Exhibit 12: CSI 300 future backwardation adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F048",
    "report_id": "R006",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Foreign domiciled passive funds flows to CSI 300 (1mma) adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F049",
    "report_id": "R006",
    "label": "Exhibit 13",
    "context": "Exhibit 13: CSI 300 put-call ratio adjusted by moving 100D min-max (scaled to $0 - 100\\%$ based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA"
  },
  {
    "figure_id": "F050",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 16: ChiNext daily turnover (RMB bn) trend vs. CSI 300"
  },
  {
    "figure_id": "F051",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 16: ChiNext daily turnover (RMB bn) trend vs. CSI 300"
  },
  {
    "figure_id": "F052",
    "report_id": "R006",
    "label": "Exhibit 18",
    "context": "Exhibit 18: A-share equity futures turnover (RMB bn) trend vs. CSI 300"
  },
  {
    "figure_id": "F053",
    "report_id": "R006",
    "label": "Exhibit 20",
    "context": "Exhibit 20: A-share margin financing vs. CSI 300"
  },
  {
    "figure_id": "F054",
    "report_id": "R006",
    "label": "Exhibit 17",
    "context": "Exhibit 17: A-share daily turnover (RMB bn) trend vs. CSI 300"
  },
  {
    "figure_id": "F055",
    "report_id": "R006",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Northbound daily turnover (RMB bn) trend vs. CSI 300"
  },
  {
    "figure_id": "F056",
    "report_id": "R006",
    "label": "Exhibit 21",
    "context": "Exhibit 21: SSE new accounts registered (unit thousand) vs. CSI 300"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "Exhibit 22",
    "context": "Exhibit 22: RSI (30 days) vs. CSI 300"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "Exhibit 24",
    "context": "Exhibit 24: CSI 300 future backwardation vs. CSI 300"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Foreign domiciled passive funds flows (1mma, USDmn) to CSI 300 vs. CSI 300"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "Exhibit 28",
    "context": "Exhibit 28: A-share margin financing (USD mn)"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Number of A-shares trading at limit up vs. CSI 300"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "Exhibit 25",
    "context": "Exhibit 25: CSI 300 call put ratio vs. CSI 300"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Shanghai A-share earnings estimate revision breadth (3mma) vs. CSI 300"
  },
  {
    "figure_id": "F064",
    "report_id": "R007",
    "label": "Figure 1",
    "context": "Figure 1: Global Liners' YTD Share Price performance (2026)"
  },
  {
    "figure_id": "F065",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "Figure 2: Global Liners' share price performance during the first 3 weeks of the conflict (28 $^{th}$ Feb – 18 $^{th}$ March)"
  },
  {
    "figure_id": "F066",
    "report_id": "R007",
    "label": "Figure 3",
    "context": "Figure 3: Global Liners' share price performance pre-conflict in 2026 (2 Jan - 28 Feb)"
  },
  {
    "figure_id": "F067",
    "report_id": "R007",
    "label": "Figure 4",
    "context": "Figure 4: % of Capacity Scrubber-fitted Across Industry (Based on Clarksons' Vessel Ownership Tracking)"
  },
  {
    "figure_id": "F068",
    "report_id": "R007",
    "label": "Figure 5",
    "context": "Figure 5: HFSO vs VLSFO Bunker Fuel Price (USD/ton)"
  },
  {
    "figure_id": "F069",
    "report_id": "R007",
    "label": "Figure 6",
    "context": "Figure 6: Shanghai Containerized Freight Index by route"
  },
  {
    "figure_id": "F070",
    "report_id": "R007",
    "label": "Figure 7",
    "context": "Figure 7: Drewry World Container Index"
  },
  {
    "figure_id": "F071",
    "report_id": "R007",
    "label": "Figure 8",
    "context": "Figure 8: Drewry Intra-Asia Container Index (IACI)"
  },
  {
    "figure_id": "F072",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "Figure 9: Clarksons - Containership Time Charter Rate by size Figure 10: Top 10 Carriers Owned vs. Chartered Fleet Ratio"
  },
  {
    "figure_id": "F073",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "Figure 9: Clarksons - Containership Time Charter Rate by size Figure 10: Top 10 Carriers Owned vs. Chartered Fleet Ratio"
  },
  {
    "figure_id": "F074",
    "report_id": "R007",
    "label": "Figure 11",
    "context": "Figure 11: Descartes - U.S. Containerized Import Volume"
  },
  {
    "figure_id": "F075",
    "report_id": "R007",
    "label": "Figure 12",
    "context": "Figure 12: U.S. NRF - Monthly Imports (MM TEU)"
  },
  {
    "figure_id": "F076",
    "report_id": "R007",
    "label": "Figure 13",
    "context": "Figure 13: U.S. Logistics Managers' Index (LMI) - LMI Index vs Future Expectations"
  },
  {
    "figure_id": "F077",
    "report_id": "R007",
    "label": "Figure 14",
    "context": "Figure 14: U.S. Logistics Managers' Index (LMI) - Inventory Levels vs Future Levels"
  },
  {
    "figure_id": "F078",
    "report_id": "R007",
    "label": "Figure 15",
    "context": "Figure 15: Clarksons - Weekly Total No. of Strait of Hormuz Vessel Transits"
  },
  {
    "figure_id": "F079",
    "report_id": "R007",
    "label": "Figure 16",
    "context": "Figure 16: Clarksons Port Congestion Index - Containerships in Port, m.TEU, 7dma Figure 17: Port Congestion Index - Containerships in Port, China P.R., m.TEU, 7dma Figure 18: Port Congestion Index - Containerships in Port, Sout"
  },
  {
    "figure_id": "F080",
    "report_id": "R007",
    "label": "Figure 16",
    "context": "Figure 16: Clarksons Port Congestion Index - Containerships in Port, m.TEU, 7dma Figure 17: Port Congestion Index - Containerships in Port, China P.R., m.TEU, 7dma Figure 18: Port Congestion Index - Containerships in Port, Sout"
  },
  {
    "figure_id": "F081",
    "report_id": "R007",
    "label": "Figure 17",
    "context": "Figure 17: Port Congestion Index - Containerships in Port, China P.R., m.TEU, 7dma Figure 18: Port Congestion Index - Containerships in Port, South East Asia, m.TEU, 7dma"
  },
  {
    "figure_id": "F082",
    "report_id": "R007",
    "label": "Figure 19",
    "context": "Figure 19: Clarksons Port Congestion Index - Containerships in Port, ME & Indian Subcontinent, m.TEU, 7dma"
  },
  {
    "figure_id": "F083",
    "report_id": "R007",
    "label": "Figure 20",
    "context": "Figure 20: Drewry Global Container Port Throughput Index (PTI)"
  },
  {
    "figure_id": "F084",
    "report_id": "R007",
    "label": "Figure 21",
    "context": "Figure 21: CMPH Monthly Throughput Tracker by Region"
  },
  {
    "figure_id": "F085",
    "report_id": "R008",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Middle income economies have far lower workforce share in information industries compared to high income ones Employment Share (%) in Information Industries"
  },
  {
    "figure_id": "F086",
    "report_id": "R008",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Not only employment, but in overall share of GDP too, emerging economies are less reliant on services than high income ones"
  },
  {
    "figure_id": "F087",
    "report_id": "R008",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Emerging economies have salaries an order of magnitude below those of high income economies for the same roles Average Salaries across exposed job categories in key economies"
  },
  {
    "figure_id": "F088",
    "report_id": "R008",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Markets of middle income economies (highlighted in red) have seen the steepest falls since the spurt of AI announcements USD Returns of Indices since Anthropic's Cowork Tools Announcement"
  },
  {
    "figure_id": "F089",
    "report_id": "R008",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: India has among the highest exposure to IT services in its benchmark indices Benchmark Indices exposure to IT services across key economies"
  },
  {
    "figure_id": "F090",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "EXHIBIT 6: Limitless productivity increase does not increase demand infinitely; it rather gradually kills it"
  },
  {
    "figure_id": "F091",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: When it comes to income inequality, middle income economies are far less equal - with top 10% having over 50% of national income. The corresponding number for high income economies is 43%"
  },
  {
    "figure_id": "F092",
    "report_id": "R008",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: However, when it comes to wealth, the countries are relatively closely bundled, with 60%+ share of top 10 for all"
  },
  {
    "figure_id": "F093",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: IT stocks sit at their cheapest valuations since COVID period six years back"
  },
  {
    "figure_id": "F094",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 1: Domestic retail fuel prices have risen less than Brent crude oil prices since the start of the Middle East conflict"
  },
  {
    "figure_id": "F095",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Increased imports from Russia and Latin America have partially offset falling Middle East supply"
  },
  {
    "figure_id": "F096",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3: An illustration of China's domestic retail oil product pricing framework ```mermaid graph TD"
  },
  {
    "figure_id": "F097",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Gasoline and diesel together accounted for less than half of China's domestic oil product consumption in 2025 China oil consumption breakdown by major oil product category (in volume terms, 2025)"
  },
  {
    "figure_id": "F098",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 6: NBS oil product retail sales volume accounted for around 75% of NDRC oil product apparent consumption in recent years Oil product consumption volume"
  },
  {
    "figure_id": "F099",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8: For every $10\\%$ domestic retail oil price increase, China's domestic oil product retail sales volume would decline by around $5\\%$"
  },
  {
    "figure_id": "F100",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Domestic retail oil product sales volume contracted by 17% yoy during March-April whereas retail prices gained 17%"
  },
  {
    "figure_id": "F101",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10: China's visible oil inventory level has been on the rise since 2022 ..."
  },
  {
    "figure_id": "F102",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "Exhibit 11: ... with rapid stockpiling in 2025 when oil prices were relatively low China's visible oil inventory changes vs. domestic gasoline prices"
  },
  {
    "figure_id": "F103",
    "report_id": "R011",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China's \"Big Three\" Oil Giants operating profits averaged RMB480bn over the past five years China's \"Big Three\" Oil Giants Operating Profits (Annual)"
  },
  {
    "figure_id": "F104",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Despite the global energy-supply shock, oil giants operating profit growth rebounded in Q1 2026 China's \"Big Three\" Oil Giants Operating Profit (Quarterly)"
  },
  {
    "figure_id": "F105",
    "report_id": "R012",
    "label": "Figure 1",
    "context": "## Shreyas Madabushi Figure 1. Lithium carbonate monthly inventory"
  },
  {
    "figure_id": "F106",
    "report_id": "R012",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Lithium carbonate weekly inventory"
  },
  {
    "figure_id": "F107",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Spread of battery-grade LC (assume 1M inventory)"
  },
  {
    "figure_id": "F108",
    "report_id": "R012",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Spread of battery-grade LC (assume 1M inventory)"
  },
  {
    "figure_id": "F109",
    "report_id": "R012",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Lithium carbonate monthly production"
  },
  {
    "figure_id": "F110",
    "report_id": "R012",
    "label": "Figure 6",
    "context": "The chart displays stacked bars for each product category over time, with values in kt. The labels on the bars are 'Industrial-grade' and 'Battery-grade'. The data is extracted from the image and presented in a CSV format as requested. The title of the chart i"
  },
  {
    "figure_id": "F111",
    "report_id": "R013",
    "label": "Figure 5",
    "context": "- The operating rate of purified terephthalic acid (PTA) factories fell sharply to 59.3% at end-May from 69.0% at end-April (Figure 5), before rebounding moderately to 66.4% in early June. The monthly average operating rate dropped further to 8.9pp below last "
  },
  {
    "figure_id": "F112",
    "report_id": "R013",
    "label": "Figure 7",
    "context": "Before the Iran war, $50\\%$ of China's oil imports and $16\\%$ of its natural gas imports passed through the Strait of Hormuz (SoH). Due to the severe damage to a wide range of energy facilities in the Middle East and the blockage of the SoH, the supply disrupt"
  },
  {
    "figure_id": "F113",
    "report_id": "R013",
    "label": "Figure 9",
    "context": "## The import disruptions of chemical raw materials For sulfur, import volumes crashed by $72.4\\%$ y-o-y in April to its lowest monthly reading since October 2008 (Figure 9), and the supply shortage worsened even further after April. Inventories of sulfur at C"
  },
  {
    "figure_id": "F114",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "On essential chemical raw materials for producing plastics and fabrics, import volumes of ethylene glycol plummeted by $46.3\\%$ y-o-y in April to its lowest monthly reading since 2007 (Figure 11). Import volumes of methanol dropped by $28.6\\%$ y-o-y in April a"
  },
  {
    "figure_id": "F115",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 1: YTD performance of HK-listed healthcare companies"
  },
  {
    "figure_id": "F116",
    "report_id": "R014",
    "label": "Figure 2",
    "context": "Figure 2: Global and China R&D spending (USD bn)"
  },
  {
    "figure_id": "F117",
    "report_id": "R014",
    "label": "Figure 3",
    "context": "Figure 3: Number of innovative drugs newly entered into clinical trials"
  },
  {
    "figure_id": "F118",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: Geographical breakdown of out-licensing deals Geographical breakdown of out-licensing deals"
  },
  {
    "figure_id": "F119",
    "report_id": "R014",
    "label": "Figure 5",
    "context": "Figure 5: Geographical breakdown of upfront payments Geographical breakdown of upfront"
  },
  {
    "figure_id": "F120",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: Out-licensing deals in China"
  },
  {
    "figure_id": "F121",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Figure 7: Out-licensing deals in China"
  },
  {
    "figure_id": "F122",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Overview of Adam Berlin's AI moat scores by sector across stocks that have shown a correlation with the GS AI basket GS structural AI moat score (1-10) - Higher score is a higher moat"
  },
  {
    "figure_id": "F123",
    "report_id": "R017",
    "label": "Exhibit 18",
    "context": "Louisa Qiu # Specialist Sales Christian Moore This week's scripts were (as expected, and flagged previously) impacted by the long weekend, and hence total scripts were down \\~6% for the class. Foundayo saw 16,982 TRx in its eighth week, +971 and +6.1% sequenti"
  },
  {
    "figure_id": "F124",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "EXHIBIT 1: Oral GLP-1 Launch Trajectories (TRx)"
  },
  {
    "figure_id": "F125",
    "report_id": "R017",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Wegovy Pill & Foundayo vs Zepbound Launch (New to Brand - NBRx; Weekly)"
  },
  {
    "figure_id": "F126",
    "report_id": "R017",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Daily scripts track below weekly in absolute amount, but are directionally correct"
  },
  {
    "figure_id": "F127",
    "report_id": "R017",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Daily TRx's correlate well with the Weekly data IQVIA collects"
  },
  {
    "figure_id": "F128",
    "report_id": "R017",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: We estimate \\~70% capture rate for Foundayo EXHIBIT 8: Early data points, but daily Foundayo scripts - although materially lower - look to trend well with weekly scripts"
  },
  {
    "figure_id": "F129",
    "report_id": "R017",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Potentially some impact on Wegovy daily NRx following the Foundayo approval"
  },
  {
    "figure_id": "F130",
    "report_id": "R017",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: At the 2026 Novo AGM, Novo reported that weekly Wegovy pill TRx were three times higher than tirzepatide at week 10"
  },
  {
    "figure_id": "F131",
    "report_id": "R017",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Total new patient starts on GLP-1s remain elevated"
  },
  {
    "figure_id": "F132",
    "report_id": "R017",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: GLP1 Weekly TRx data EXHIBIT 14: GLP1 Weekly NRx data EXHIBIT 15: Zepbound Weekly TRx data by form"
  },
  {
    "figure_id": "F133",
    "report_id": "R017",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: GLP1 Weekly TRx data EXHIBIT 14: GLP1 Weekly NRx data EXHIBIT 15: Zepbound Weekly TRx data by form"
  },
  {
    "figure_id": "F134",
    "report_id": "R017",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: GLP1 Weekly NRx data EXHIBIT 15: Zepbound Weekly TRx data by form"
  },
  {
    "figure_id": "F135",
    "report_id": "R017",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: 4 Wk Rolling growth rates for Zepbound TRx by form"
  },
  {
    "figure_id": "F136",
    "report_id": "R017",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: NBRx - Broken out by pens and vials for Zepbound (vs Wegovy)"
  },
  {
    "figure_id": "F137",
    "report_id": "R017",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: LLY vs Novo on % of share of NBRx"
  },
  {
    "figure_id": "F138",
    "report_id": "R017",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: The Wegovy pill is taking NBRx share of weightloss drugs"
  },
  {
    "figure_id": "F139",
    "report_id": "R017",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Semaglutide vs Tirzepatide - 4 weekly average TRx share"
  },
  {
    "figure_id": "F140",
    "report_id": "R017",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: 4 weekly average TRx share by Brand"
  },
  {
    "figure_id": "F141",
    "report_id": "R017",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Total GLP-1 Weekly TRx"
  },
  {
    "figure_id": "F142",
    "report_id": "R017",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Total GLP-1 Weekly NRx"
  },
  {
    "figure_id": "F143",
    "report_id": "R017",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Rolling 4-weekly year-on-year volume growth for GLP-1s"
  },
  {
    "figure_id": "F144",
    "report_id": "R017",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: Mounjaro TRx by dose EXHIBIT 30: Zepbound TRx by dose EXHIBIT 31: Ozempic TRx by dose"
  },
  {
    "figure_id": "F145",
    "report_id": "R017",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: Mounjaro TRx by dose EXHIBIT 30: Zepbound TRx by dose EXHIBIT 31: Ozempic TRx by dose EXHIBIT 32: Wegovy TRx by dose"
  },
  {
    "figure_id": "F146",
    "report_id": "R017",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Zepbound TRx by dose EXHIBIT 31: Ozempic TRx by dose EXHIBIT 32: Wegovy TRx by dose EXHIBIT 33: Wegovy Pill TRx by dose"
  },
  {
    "figure_id": "F147",
    "report_id": "R017",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: Ozempic TRx by dose EXHIBIT 32: Wegovy TRx by dose EXHIBIT 33: Wegovy Pill TRx by dose"
  },
  {
    "figure_id": "F148",
    "report_id": "R017",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Wegovy TRx by dose EXHIBIT 33: Wegovy Pill TRx by dose"
  },
  {
    "figure_id": "F149",
    "report_id": "R017",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: Foundayo TRx by dose"
  },
  {
    "figure_id": "F150",
    "report_id": "R021",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Oncology and obesity are the fastest growing therapeutic areas - and should remain so in the near term Global historic and forecast growth for top 20 therapy areas"
  },
  {
    "figure_id": "F151",
    "report_id": "R021",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Depending on pricing and reimbursement developments, obesity spending could break into the \\$100Bn level in the coming years Global obesity spending and growth"
  },
  {
    "figure_id": "F152",
    "report_id": "R021",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Among the newer molecular modalities, peptides stand out as both the largest market by 2030 and one of the fastest-growing Market size forecast by modality"
  },
  {
    "figure_id": "F153",
    "report_id": "R021",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Comparison of peptide synthesis methods - despite high solvent waste, SPPS is the commercial standard for mid to long peptides like GLP-1 agonists EXHIBIT 6: Major CDMOs are expanding their peptide synthesis capacity to"
  },
  {
    "figure_id": "F154",
    "report_id": "R021",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Compared to traditional batch chromatography, continuous chromatography (multi-column countercurrent solvent gradient purification or MCSGP) increases throughput and reduces process control and lyphilization volume Thr"
  },
  {
    "figure_id": "F155",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: Debit is significantly cheaper vs. credit in the U.S. Weighted Average Merchant Card Fees in the US (2025, %)"
  },
  {
    "figure_id": "F156",
    "report_id": "R022",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: Cards are especially cheaper in Europe Merchant Discount Rate by Country"
  },
  {
    "figure_id": "F157",
    "report_id": "R022",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Mix between credit/debit cards varies widely by country.. Debit vs Credit Mix in Select Countries (%, 2025)"
  },
  {
    "figure_id": "F158",
    "report_id": "R022",
    "label": "Exhibit 4",
    "context": "EXHIBIT 4: Cards wrap around a lot of services for debit.. Debit Merchant Discount Rate"
  },
  {
    "figure_id": "F159",
    "report_id": "R022",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: ..and credit Credit Merchant Discount Rate"
  },
  {
    "figure_id": "F160",
    "report_id": "R022",
    "label": "EXHIBIT 6",
    "context": "Doesn't include losses Shopify Payment Rates"
  },
  {
    "figure_id": "F161",
    "report_id": "R022",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Europe interchange regulation went into effect in Dec 2015, significantly boosting card penetration and adoption Europe Card Penetration Rate"
  },
  {
    "figure_id": "F162",
    "report_id": "R022",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: Surcharging among small business owners reached 34% per a survey conducted early 2025 % Small Business Owners Adopting Surcharging"
  },
  {
    "figure_id": "F163",
    "report_id": "R022",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: The networks yields are only a small fraction of total MDR US Merchant Discount Rate vs Visa US Yield"
  },
  {
    "figure_id": "F164",
    "report_id": "R022",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Tokens are proliferating, and will do so even more with Agentic commerce - solidifying moat and pricing power Visa # of Tokens and Cards (B, CY) '20-25 CAGR Tokens: 77% Cards: 7%"
  }
]