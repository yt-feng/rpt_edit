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
    "title": "GS：2026年底核心PCE仍在3.2%，AI和油价是最大变量",
    "digest": "[wechat_article.md]\n# GS：2026年底核心PCE仍在3.2%，AI和油价是最大变量\n\n市场对通胀的叙事在过去三个月里经历了一次急转弯。年初时，主流预期是“最后一英里”的顽固通胀将缓慢回落；到了年中，地缘冲突、AI基建狂潮和美股财富效应同时发力，迫使几乎所有机构上调了通胀预测。但GS最新发布的这份《年中通胀展望》给出的判断，比市场共识更精细、也更值得警惕。\n\n核心结论是：到2026年12月，核心PCE通胀仍将高达3.2%，远高于美联储2%的目标。但真正让人意外的不是这个数字本身，而是驱动这一结果的三个力量——能源、AI和租金——正在以完全不同的节奏和机制发挥作用。GS认为，到2027年底通胀会降至2.2%，但风险偏向上行。换句话说，未来18个月的通胀路径，不是一条平滑的下坡路，而是一场多方角力的拉锯战。\n\n这份报告的价值不在于它给出了一个预测数字，而在于它拆解了通胀的“分子结构”：哪些力量正在推高物价，哪些力量正在压制物价，以及这些力量的可持续性如何。对于产业决策者和资产配置者来说，理解这套框架远比知道一个终点数字重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美伊协议让油价风险从“最大威胁”降级为“可控变量”\n\n今年上半年，中东局势是通胀预测中最难量化的变量。但GS大宗商品团队在美伊协议达成后，大幅下调了油价预测：2026年四季度布伦特原油均价预期从90美元降至80美元，2027年从80美元降至75美元。这个调整直接意味着，能源对核心PCE的推升力度比此前假设减少了约0.2个百分点。\n\n更值得关注的是GS给出的情景分析。在霍尔木兹海峡持续受阻的极端情景下，布伦特原油可能在2026年升至130美元，对核心PCE的额外推升约为0.2个百分点，对整体PCE的推升则高达1.1个百分点。而在供给增加的乐观情景下，油价可能跌至70美元\n\n[... middle omitted ...]\n\n识星球微信群继续讨论，一起追踪这份报告中的关键变量如何演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n通胀新剧本：油价降温，AI涨价，房租拖后腿\n\n通胀拆解：油价、AI与房租\n\n最近通胀又抬头了，核心PCE重新加速。拆开看，背后是三个力量在角力。\n\n1/ 油价突然“退烧”\n美伊协议让能源风险下降。某外资投行把2026Q4油价预测从90降到80美元，2027年从80降到75美元。这意味着今年核心PCE少涨0.05pp。汽油价格回落，6月CPI可能报-0.13%，PCE报0.07%。不过非油商品价格（化肥、聚乙烯）虽然从高点回落，但硫磺、氨气仍偏高。整体商品价格会给核心PCE贡献约0.4pp的同比涨幅。\n\n2/ AI带来的“测量失真”\nAI基建推高内存价格，部分品类几个月涨了10-15倍。这会通过“软件和配件”推高PCE，但测量方法放大了影响。预计月环比涨幅从4-5%降到0.6%。手机电脑也会涨，但权重小。预计AI给2026年12月核心PCE贡献0.4pp，峰值在2026H2达0.6pp。有趣的是，对CPI影响小得多（仅0.1pp），因为CPI没有同样的方法论问题。\n\n3/ 房租和工资在拖后腿\n新租约租金增长疲软，预计住房通胀会持续放缓，最终比疫情前低1-1.5pp。工资增长也在减速，会压低非住房服务通胀。但医疗\n\n[... middle omitted ...]\n\n which implies about 0.2pp and 0.05pp less upward pressure on headline and core PCE inflation this year than our previous assumptions. In the near term, lower gasoline prices will translate in\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "GS：东盟正面临三重粮食通胀冲击，印尼和菲律宾首当其冲",
    "digest": "[wechat_article.md]\n# GS：东盟正面临三重粮食通胀冲击，印尼和菲律宾首当其冲\n\n全球投资者刚刚消化了中东冲突对能源价格的直接影响，一个更隐蔽、周期更长的风险已经在东南亚浮现。GS亚洲经济团队在最新发布的研报中发出明确警告：东盟地区正在同时承受油价冲击、化肥成本飙升和潜在的强厄尔尼诺现象三重压力，未来12个月食品通胀可能额外增加超过2个百分点。这不是一个温和的警告——在印尼、菲律宾和泰国，峰值影响可能达到1.1至1.2个百分点的整体CPI贡献。\n\n这份报告的核心判断是：东盟食品通胀的同步性极高，而当前的三重供给冲击叠加，正在逼近过去二十年中少见的压力水平。市场此前关注的焦点集中在能源价格本身，但GS的分析框架揭示了一个更值得警惕的逻辑——第二轮通胀传导效应正在进入食品供应链，而政策缓冲的空间正在被压缩。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三个供给冲击正在同步放大，这不是简单的成本传导\n\nGS的报告建立了一个清晰的冲击传导模型。第一层是油价：中东冲突导致布伦特原油价格在5月底仍比2月水平高出约46%。这一冲击首先反映在交通和机票等燃料敏感型CPI分项上，但真正的第二轮传导——通过运输成本、包装和加工环节进入食品价格——正在发生。\n\n第二层是化肥价格。尿素价格在同期上涨了约63%，这对东盟的冲击尤为严重。即使是泰国这个区域唯一的净食品出口国，其90%以上的化肥依赖进口。GS的估算显示，油价每上涨10%，将在12个月后推高东盟食品CPI约0.3个百分点；化肥价格同样上涨10%，效应约为0.2个百分点。单独看似乎不大，但两者叠加，再加上厄尔尼诺的不确定性，压力正在累积。\n\n第三层是气候。美国国家海洋和大气管理局（NOAA）评估认为，2026年11月至2027年1月期间出现强厄尔尼诺事件的风险显著。如果成真，这将恰好发生在油价和化\n\n[... middle omitted ...]\n\n案例或二阶通胀效应有进一步疑问，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n东南亚粮食通胀：三重冲击正在路上\n\n**封面标题**\n三重冲击\n\n**副标题**\n油、化肥、厄尔尼诺的叠加效应\n\n---\n\n最近读了一篇某外资投行的东盟研报，把粮食通胀的逻辑讲得很清楚。\n\n简单说，东南亚接下来要扛住三波冲击，而且它们是叠加的。\n\n**1/ 油价传导最直接**\n油价涨10%，12个月后东盟食品CPI会涨约0.3%。中东冲突推高油价，先反映在交通和机票上，但第二波会慢慢渗入食品供应链。\n\n**2/ 化肥成本在累积**\n化肥涨10%，食品CPI涨约0.2%。泰国90%以上化肥靠进口，即使它是区域净出口国，也被卡住脖子。\n\n**3/ 厄尔尼诺可能成为催化剂**\nNOAA预测2026年底可能出现强厄尔尼诺。研报模型显示，如果油+化肥+气候三股压力同时释放，12个月后东盟食品通胀可能额外增加2.1个百分点。\n\n**各国受影响程度差异很大**\n- 印尼、菲律宾、泰国：上行风险最明显\n- 新加坡和马来西亚：相对可控（新加坡食品在CPI中权重仅6.5%）\n\n**有意思的发现**\n过去厄尔尼诺对食品通胀的传导并不明显，因为各国政府通常会释放储备、放开进口、补贴或限价。比如泰国2015-16年释放了约1780万吨\n\n[... middle omitted ...]\n\nlton  \n+852-2978-1802 | andrew.tilton@gs.com GS (Asia) L.L.C.\n\nASEAN is exposed through trade, CPI weights and commodity linkages. Food inflation is highly synchronized across the region and f\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "GS：AI泡沫还没到1999年，但市场已经把未来十年利润透支了",
    "digest": "[wechat_article.md]\n# GS：AI泡沫还没到1999年，但市场已经把未来十年利润透支了\n\nAI热潮推动美股屡创新高，市场对AI的定价究竟是否合理？GS在最新研报中给出了一个既令人安心又值得警惕的判断：AI投资热潮的基本面依然坚实，但市场已经将大量潜在价值提前计入价格，且这一趋势在过去六个月进一步加剧。\n\n与1990年代末的科技泡沫相比，当前AI热潮在宏观层面呈现出关键差异——企业利润率持续攀升而非下滑，企业部门整体财务状况稳健，经常账户赤字在收窄而非扩大。唯一接近当年水平的，是AI相关投资的规模。但问题在于，市场对AI相关公司的估值已经远远超出了GS“基准情景”下AI能为美国经济带来的资本收入现值。\n\n这份报告的核心信息是：现在仍有可能用乐观假设来弥合市场定价与经济基本面之间的差距，但需要的假设越来越多、越来越激进。这并不意味着市场马上会跌，但意味着市场对负面消息的脆弱性正在上升。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 投资规模已追上1990年代，但宏观失衡尚未出现\n\nGS在去年11月首次系统对比当前AI热潮与1990年代科技泡沫时，识别出四个关键宏观信号：持续异常高的投资水平、利润率下滑、企业融资需求和杠杆率急剧上升、经常账户赤字扩大。当时这四个信号中只有第一个出现，六个月后，情况依然如此。\n\n变化最显著的是投资规模。科技投资占GDP的比重已经突破1990年代高点，且上升速度更快。超大规模云服务商对2026年的资本支出预期比六个月前高出近80%。AI相关投资有望在未来一两年内接近甚至超越1990年代科技投资热潮的峰值水平。\n\n但其他三个信号尚未出现。企业利润率不仅没有下滑，反而升至新高。强劲的生产率增长没有被工资加速上涨侵蚀，单位劳动力成本增速远低于1998-2000年。超大规模云服务商的自由现金流确实大幅下降，但整个企业\n\n[... middle omitted ...]\n\n市场动态。欢迎来星球微信群继续讨论，获取完整报告和原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI泡沫要来了吗？看看数据怎么说\n\nAI热潮与1990s对比\n\nAI投资热度已接近1990s科技泡沫规模\n\n最近关于AI泡沫的讨论很多，翻了一份外资投行的深度研报，把核心逻辑拆给大家。\n\n先说结论：AI投资热潮仍在加速，但市场估值已经跑在了基本面前面。和1990s科技泡沫相比，有相似，也有不同。\n\n📌 相似点：投资规模在追赶\n- 科技投资占GDP比重已突破1990s高点\n- 云厂商2026年资本开支预期比半年前高了近80%\n- AI相关投资未来2-3年可能超过1990s科技投资峰值\n\n📌 关键不同：其他泡沫指标没跟上\n1️⃣ 利润率：没有下降，反而创了新高\n2️⃣ 企业融资需求：除了云厂商，整体没恶化\n3️⃣ 经常账户赤字：在收窄，不是扩大\n4️⃣ 劳动力成本：增长比1990s温和得多\n\n📌 最值得关注的风险\n自2022年11月以来，AI相关公司市值增加了约27万亿美元，远超研报估算的9万亿美元AI生产力提升带来的“合理价值”。\n\n要弥合这个差距，需要同时满足多个乐观假设：更快的AI采用率、更高的资本回报率、美国公司拿到更多全球份额。\n\n📌 总结\n投资热潮还会持续，但市场已经price in了很多乐观预期。一\n\n[... middle omitted ...]\n\nn the late 1990s, only one has changed meaningfully: the AI capex boom is neither as broad-based nor as long-lived as the 1990s tech boom, but it is now matching its scale. Other macro dynamic\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "摩根斯坦利：MS：沃什的第一次FOMC会议，市场真正该关注的是流动性而非加息",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：沃什的第一次FOMC会议，市场真正该关注的是流动性而非加息\n\n这份MS最新周报的核心判断值得每一个资产配置者重视：凯文·沃什被提名为美联储主席以来，标普500/黄金比率已经上涨了约40%，这是市场在投信任票。但信任票兑现的过程，可能伴随着短期阵痛。报告明确指出，当前对股市更现实的威胁不是加息，而是流动性正在收紧。\n\n沃什第一次主持FOMC会议，释放的信号比市场预期的更加清晰。他明确表示美联储的首要任务是通胀，而不是就业或经济增长。他甚至公开批评美联储过去五年持续偏离通胀目标。这种“新警长上任”的姿态，在报告看来，是重建美联储信誉的必要步骤，但也意味着市场需要适应一个更少“手把手指导”的央行。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 沃什的鹰派转向并非意在加息，而是为了给长期“热运行”策略铺路\n\n市场普遍将沃什的强硬表态解读为鹰派，但MS的分析视角更为精细。报告认为，沃什的真正意图不是要立刻加息压制经济，而是要通过重建美联储在通胀问题上的信誉，来为政府“以增长化解债务”的长期策略赢得时间与空间。\n\n沃什在会议上的措辞值得玩味。他一方面强调通胀是首要任务，另一方面又暗示“2字头”的通胀是可以接受的。这实际上是在说，2%到3%的通胀区间是可以容忍的。报告将此解读为一种精妙的平衡：既要让市场相信央行不会失控，又要为经济“热运行”保留必要的弹性空间。放弃点阵图、减少前瞻指引，本质上是在为未来的政策操作保留“惊喜”能力。\n\n> **KC评论：** 沃什的做法很像一位企业CEO，先通过严厉表态重置市场预期，再在实际操作中保留灵活性。市场如果只看到“鹰派”的一面，可能会忽略他真正关心的长期目标——在不引发债券市场叛乱的前提下，让名义GDP增速尽可能跑在高位。完整报告中对“热运行”策略与债务化解之间的逻\n\n[... middle omitted ...]\n\n被公开讨论的市场细节，欢迎来我们的知识星球和微信群一起讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新主席首秀：鹰派还是鸽派？\n\n美联储换“话事人”了\n\n新主席首场会议释放了哪些信号？\n\n📌 这是一份来自某外资投行的最新解读，信息量很大，我帮你划重点。\n\n1️⃣ 新主席的“定调”：通胀是唯一目标\n研究认为，新主席Kevin Warsh在首次会议上明确表态，美联储的首要职责是控制通胀，而非劳动力市场或经济增长。他甚至公开批评美联储过去5年多次未能实现通胀目标。这意味着，美联储的“指挥棒”彻底变了。\n\n2️⃣ 少说多做，让市场自己判断\n新主席的另一大变化是：不再提供过多“前瞻指引”。他主张，金融市场最好的状态就是根据数据自由反应，而不是总在猜测美联储下一步要说什么。研究认为，这能让美联储保留“出其不意”的空间，也更有助于它获取真实的市场信号。\n\n3️⃣ 短期市场可能“消化不良”\n虽然方向明确，但过程可能有点颠簸。研报指出，市场不喜欢不确定性。新主席的强硬表态可能导致债券收益率曲线急剧平坦化、美元走强、贵金属承压。不过，这恰恰是重建美联储公信力的必经之路。\n\n4️⃣ 真正的风险不是加息，是流动性\n研究特别强调，短期对股市构成压力的，可能不是加息预期，而是流动性收紧。美联储的储备管理计划（RMP）规模已从峰值\n\n[... middle omitted ...]\n\nbruary, the roughly 40% rise in the S&P 500/Gold ratio since his nomination reinforces our view that markets are giving him the benefit of the doubt. Specifically, we think markets are signali\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R005",
    "title": "摩根斯坦利：MS：美债市场即将回归“格林斯潘时代”，波动率才是真正的分水岭",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：美债市场即将回归“格林斯潘时代”，波动率才是真正的分水岭\n\n理解美联储未来的政策路径，市场习惯盯着利率水平——降息几次、终点利率在哪、点阵图如何移动。但MS全球宏观策略主管Matthew Hornbach团队在一份题为《Get Ready For the Noisiest US Front End In a Generation》的研报中，提出了一个完全不同的分析框架：决定利率市场“体质”的，不是利率的绝对水平，而是美联储使用的政策工具箱。而这一框架指向一个明确的结论——无论下一任美联储主席是谁，只要政策风格向格林斯潘时代回归，美债前端市场就将迎来一代人以来最嘈杂的交易环境。\n\n这份报告的核心主张是：**不要只看利率水平，要看波动率的分布。** 基于对格林斯潘、伯南克、耶伦、鲍威尔四任主席任期内数据的拆解，MS发现，前端波动率和曲线形态波动率才是区分不同利率体制的真正标尺。在格林斯潘时代，前端是整条曲线的引擎，2年期收益率变动拉动整条曲线移动。而在耶伦时代，前端几乎静止，长端主导曲线。两者形成了近乎镜像的关系。\n\n这一判断在当前市场环境下尤其重要。随着美联储缩表进程持续推进、前瞻指引的使用趋于克制，市场正在从耶伦/鲍威尔早期的“指引锚定”模式，向格林斯潘式的“市场定价”模式过渡。对于投资者而言，这意味着过去几年那种低波动、窄区间、曲线形态稳定的交易环境可能正在系统性改变。\n\n> **KC评论：** MS不是在预测利率会涨还是会跌，而是在说“市场波动的性质”将发生根本变化。这对所有持有利率相关头寸的机构都是重要信号——即使你的方向判断对了，波动率环境的改变也会影响仓位管理和风险预算。完整报告中有36年的数据图表，清晰展示了四任主席期间前端波动率的阶梯式变化，值得仔细看。\n\n![研报原图 1](assets/source_image_01.\n\n[... middle omitted ...]\n\n形态波动率指标、交易思路，以及下一任主席人选对工具箱的影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储换人，债市要变天？\n\n**债市变局**\n\n**当美联储不再“话多”，曲线开始跳舞**\n\n最近某外资投行发了一篇很有意思的研报，讲的是美联储主席的“工具箱”如何决定债市性格。结论很干脆：决定利率环境的，不是主席本人，而是他们用的那套工具。\n\n1️⃣ **前端的噪音，才是关键**\n过去36年数据表明，区分四位联储主席的不是收益率绝对水平，而是**前端波动率**。格林斯潘时期前端年化波动率高达110bp，到耶伦时代骤降至21bp（因为利率被钉在零），鲍威尔又回升到60bp。后端（10年期）波动率变化反而不大，约90-100bp。所以，变的是前端，不是长端。\n\n2️⃣ **格林斯潘 vs 耶伦：谁在驱动曲线？**\n- 格林斯潘时期：2年期收益率涨，曲线就变平（负相关）。**前端是整条曲线的引擎**，拉着全场跑。\n- 耶伦时期：前端被钉死，**长端主导**曲线形态，相关性转为正。\n- 鲍威尔目前处于中间地带，正慢慢回归格林斯潘模式。\n\n3️⃣ **少说两句，曲线更动荡**\n工具越少，市场接手越多。研报测算了2s10s30s蝶式曲线的曲率波动率：格林斯潘时期约80bp，耶伦时期仅44bp，鲍威尔约52bp。**减少\n\n[... middle omitted ...]\n\nmove pulling the whole curve along. Under Yellen the front end sat still and the long end led.\n\nWe measure it directly. Correlation between 2-year moves and slope moves runs negative under Gre\n\n[... middle omitted ...]\n\nuthors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.\n\n© 2026 MS"
  },
  {
    "id": "R006",
    "title": "Bernstein：数据中心冷却的“隐形瓶颈”正在改写竞争格局",
    "digest": "[wechat_article.md]\n# Bernstein：数据中心冷却的“隐形瓶颈”正在改写竞争格局\n\n当全球超大规模云厂商和AI算力军备竞赛进入“每兆瓦必争”的阶段，一个看似基础却至关重要的设备——冷水机组——正从幕后走向台前。它不仅是数据中心冷却系统的核心，更可能成为决定未来几年算力扩张速度与成本结构的“隐形瓶颈”。\n\nBernstein最新发布的一份深度专题报告，系统拆解了这个价值约80亿美元（2026年预估）的市场。报告的核心判断是：**市场并非简单的“量价齐升”，而是正在经历一场由技术路线选择（风冷 vs. 水冷）和区域资源禀赋（电价 vs. 水价）共同驱动的结构性分化。** 这种分化将直接影响Trane、Carrier、Johnson Controls和Vertiv等主要玩家的订单能见度、利润率乃至长期竞争地位。\n\n对于关注AI基础设施投资的决策者而言，理解冷水机组的技术经济学，比单纯追踪算力需求数字更为关键。因为它揭示了算力成本中一个常被忽视、但正在快速放大的变量：**冷却的“隐性成本”正在从电力转向水资源。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nBernstein报告估算，2026年全球数据中心冷水机组市场（含安装及配套设备）约为80亿美元，在基准情景下，2030年将增长至约165亿美元，对应约20%的年复合增长率。这个数字本身并不令人意外，但报告通过“熊市”和“牛市”两种情景分析，揭示了市场规模的巨大不确定性。\n\n在熊市情景下，如果干冷器（dry coolers）等替代方案侵蚀份额，市场规模可能仅增长至约90亿美元，年复合增长率不足5%。而在牛市情景下，如果冷水机组在液冷普及中进一步获得份额，市场规模将膨胀至约200亿美元，年复合增长率超过25%。\n\n**这意味着，未\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心冷却的隐藏成本：空冷 vs 水冷\n\n冷却器选择的关键变量\n\n数据中心冷却器市场2026年预计80亿美元，2030年有望达到165亿美元。但选空冷还是水冷，不是简单答案。\n\n1️⃣ 空冷 vs 水冷的基础逻辑\n空冷：前期成本低，但能耗高约30%\n水冷：更节能，但需要大量水资源\n两者都依赖制冷剂循环，区别在于散热方式\n\n2️⃣ 自由冷却改变了一切\n当环境温度够低，可以关掉压缩机\n水冷在自由冷却模式下，水耗不减\n空冷能耗大幅下降，反而可能更划算\n\n3️⃣ 地域差异决定选择\n亚特兰大：水价高，50%自由冷却时空冷更优\n其他主要数据中心市场：需要更高比例自由冷却才划算\n\n4️⃣ 市场格局\n主要玩家：Trane、Carrier、Johnson Controls、Vertiv\n目前供给严重不足，产品差异远小于需求缺口\n空冷正在重获关注\n\n#学习笔记\n\n[source_mineru.md]\n# U.S. Multi Industry & Electrical Equipment\n\n# Data Center Chillers (1/3): Primer and free cooling economics\n\n![](\n\n[... middle omitted ...]\n\nthen pumps to CDUs to extract heat from the coolant or to CRAHs to reduce the temperature of air blowing through the data center. We size this as a \\~\\$8B market in 2026 (fully loaded cost inc\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R007",
    "title": "GS：全球金融条件正在宽松，但真正的分化才刚刚开始",
    "digest": "[wechat_article.md]\n# GS：全球金融条件正在宽松，但真正的分化才刚刚开始\n\n全球宏观投资者的注意力正在从“通胀是否粘性”转向“增长是否可持续”。GS最新发布的全球周度经济指标更新给出了一个清晰但容易被忽略的信号：金融条件正在普遍宽松，但宽松的来源与质量，正在制造新一轮国家间的增长分化。\n\n这份由GS首席经济学家Jan Hatzius领衔的周度更新，覆盖了金融条件指数、当前活动指标、薪资跟踪器、财政脉冲等十余项自研指标。数据截止到5月底到6月初，信息密度极高。但真正值得关注的，不是单个数字的升降，而是这些指标合在一起指向的一个结论：全球经济正在经历一轮由科技股驱动的金融条件宽松，但实体经济动能的分化正在加剧。\n\n对于资产配置者而言，这意味着单纯看“全球增长”已经不够。你需要拆开每一层，看清楚宽松的钱流向了哪里，增长的动力来自哪个国家、哪个部门。\n\n> **KC评论：** GS这套自研指标的价值，不在于每周更新的数字，而在于它提供了一个结构化的观察框架——金融条件、活动指标、薪资通胀、财政脉冲，四块拼图合在一起，才能判断周期的真实位置。完整报告包含了31张图表和详尽的国别数据，很多细节在周度速览中无法展开。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 韩国成为金融条件宽松的缩影：科技股驱动的放松并非普适\n\nGS本周的“图表之选”聚焦于韩国。上周韩国金融条件指数放松了29个基点，主要驱动力是科技股引领的股市上涨。这一现象并非韩国独有——全球除俄罗斯外的金融条件指数上周也放松了0.8个基点，同样是受股市推动。\n\n但问题在于，这种由股市上涨驱动的金融条件宽松，是否可持续？韩国是一个高度依赖半导体出口的经济体，科技股的上涨有基本面支撑，但也意味着它的金融条件与全球科技周期高度共振。一旦AI叙事出现扰动或半导体周期转向，韩国的金融条件可能迅速\n\n[... middle omitted ...]\n\n交流。顺着这些问题，你会发现完整报告的价值远超一篇周度速览。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国金融条件继续放松，科技股领涨\n\n全球金融条件追踪\n\n上周韩国金融条件指数（FCI）放松了29个基点，主要靠科技股带动的权益市场上涨。全球除俄罗斯外的FCI也小幅放松，股市是主要推手。\n\n1️⃣ 韩国2026年增长预期上调\n某外资投行的最新研报显示，韩国2026年的经济增长预期被调高，这与金融条件持续放松的态势一致。\n\n2️⃣ 全球CAI仍高于潜在水平\n5月全球CAI为+2.9%（年化），发达市场+2.2%，新兴市场+4.0%。中国5月CAI为+4.6%，但周环比下降0.8个百分点；日本上升0.7个百分点至+1.3%。\n\n3️⃣ 各国FCI变化差异明显\n上周FCI变化各国不一，韩国放松幅度最大，而部分欧洲国家略有收紧。从年同比角度看，多数经济体金融条件比一年前更宽松。\n\n4️⃣ 短期利用率显示经济状态\n6月美国短期利用率-1.8%（低于潜在水平），德国+0.5%，法国+0.9%，意大利+6.5%。中国5月为-0.1%，基本处于潜在水平。\n\n这些指标可以帮助我们理解全球经济的实时状态，比单纯的GDP数据更及时。你们觉得哪个地区的金融条件变化最值得关注？\n\n#学习笔记\n\n[source_mineru.md]\n#\n\n[... middle omitted ...]\n\ns\n+1(212)902-2163 |\njoseph.briggs@gs.com\nGS & Co. LLC\n\nSarah Dong\n+1(212)357-9741 | sarah.dong@gs.com\nGS & Co. LLC\n\nMegan Peters\n+44(20)7051-2058 |\nmegan.l.peters@gs.com\nGS International\n\n## K\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R008",
    "title": "GS：全球股市的下一轮驱动力，不再是估值扩张",
    "digest": "[wechat_article.md]\n# GS：全球股市的下一轮驱动力，不再是估值扩张\n\n当全球股市在过去一周继续上涨1.2%，日本和亚太（除日本）分别反弹4.6%和4.1%时，大多数投资者关注的是地缘政治缓和带来的风险偏好回升。但这份GS最新周报传递的核心信号远比这层表象更值得深思：我们正在进入一个“后现代周期”，在这个周期里，股票回报的逻辑将发生根本性转变。\n\n这不是一次简单的周期性轮动。GS策略团队用“Post Modern Cycle”这个框架，试图告诉投资者一个不那么令人舒适但必须接受的判断——过去十五年驱动全球资产价格上涨的核心变量正在系统性逆转。\n\n通缩结束、利率触底、全球化退潮，这三个曾经支撑估值扩张的支柱，正在被高通胀波动、实际利率上升、国家干预增强和区域化重构所取代。在这样一个新范式下，股权回报将越来越依赖每股盈利增长，而非估值倍数提升。\n\n对于习惯了“买跌等宽松”策略的中国和全球投资者而言，这不仅是资产配置框架的挑战，更是一次投资哲学的拷问。\n\n> **KC评论：** GS这篇报告最值得细读的不是短期市场走势，而是它对“后现代周期”的定义。如果你还停留在用过去十年的估值框架来思考当前市场，可能会错失整个结构性变化的方向。完整报告里有详细的宏观数据对比和行业轮动证据，值得花时间研究。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本开支超级周期正在重塑全球资产回报格局\n\nGS在这份报告中提出了一个关键判断：一个由AI革命、能源安全和供应链重构三重力量驱动的资本开支超级周期正在形成。\n\n这不是一个抽象的概念。它意味着私人部门投资正在被AI革命激活，成为新的增长引擎；与此同时，能源安全和地缘政治考量正在推动政府支出同步上升。供应链从效率优先转向韧性优先，这本身就提高了资本密集度，并结构性推高了成本基础。\n\n对投资者而言，这个超级周期\n\n[... middle omitted ...]\n\n变化。欢迎来我们的知识星球和微信群里继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球市场正在反弹，但风向变了\n\n市场回暖，逻辑在切换\n\n全球股票上周涨了1.2%，日本和亚太（除日本）领涨，分别涨了4.6%和4.1%。AI带动的科技板块继续走强，涨了4.3%。但能源板块拖后腿，跌了6.3%，布伦特原油跌了约8%，因为美国与伊朗开始长期谈判。\n\n1. 风险偏好明显回升\n周期股跑赢防御股，全球资金流入创历史新高，主要是被动基金在推动。这说明大家对风险没那么紧张了。\n\n2. 宏观数据密集发布\n美国PCE通胀报告、多位美联储官员讲话（Waller、Williams、Goolsbee、Kashkari）。欧洲多国PMI初值、日本央行会议纪要、韩国20天出口数据等，都是本周看点。\n\n3. 核心逻辑：后现代周期\n投行研报提出，我们正进入“后现代周期”——告别低通胀、放松监管、低利率和全球化，转向高宏观波动、高实际利率、更多政府干预和区域化。未来回报不再靠估值扩张，而是靠盈利增长。\n\n资本支出超级周期来了。AI革命驱动私人投资，能源安全和地缘政治推高公共支出，供应链重建提升资本密集度。结果就是市场机会更分散，主动管理更容易跑出超额收益。\n\n#学习笔记\n\n[source_mineru.md]\nGLOBAL \n\n[... middle omitted ...]\n\n (Exhibit 44).\n\n## Macro data this week\n\nUS: PCE inflation report, several speaking engagements with Fed officials, including events with Governor Waller and Presidents Williams, Goolsbee, and\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "Citi：扫地机器人赛道的最大悬念，不是关税，是618之后谁能把流量变成利润",
    "digest": "[wechat_article.md]\n# Citi：扫地机器人赛道的最大悬念，不是关税，是618之后谁能把流量变成利润\n\n中国扫地机器人行业刚刚经历了一个信号密集的星期。两个看似独立的事件，在Citi看来，共同指向了一个判断：行业竞争格局正在出现微妙但重要的分化。\n\n6月19日，欧盟委员会拒绝了针对中国产割草机器人的临时反倾销税动议，将终裁推迟至2027年初。同一天前后，科沃斯公布了618全渠道GMV达到40.2亿元，同比增长23%。这两条消息，让Citi在覆盖的扫地机器人标的中，明确表达了对科沃斯的偏好，同时维持对石头科技的“中性”评级。\n\n这不仅仅是一次评级调整。它折射出Citi对行业未来12-18个月核心驱动力的判断：关税风险正在阶段性后移，而国内电商大促的竞争质量，正在成为区分赢家与输家的关键标尺。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧盟割草机关税的“暂缓”，是窗口期，不是终局\n\nCiti报告中最具时效性的信号，是欧盟对中国产机器人割草机反倾销调查的初步结论。欧盟委员会以“难以比较智能割草机的成本和定价”为由，拒绝征收临时反倾销税，并将调查推进至终裁阶段，预计2027年初才会有最终结论。\n\n这个决定的直接含义是：科沃斯在欧洲割草机市场的短期风险被移除。Citi指出，科沃斯拥有欧洲最畅销的机器人割草机之一，在这一细分赛道的暴露度是覆盖标的中最高的。\n\n但需要冷静看待的是，这只是“暂缓”，不是“豁免”。欧盟的终裁仍有变数。对中国企业而言，这提供了一个约18个月的窗口期，但窗口期的价值取决于企业如何利用它——是加紧本地化布局、优化供应链，还是继续依赖价格优势扩张。\n\n> **KC评论：** 关税风险后移，不等于关税风险消失。对投资者而言，关键不是赌终裁结果，而是看企业是否在为“有税世界”做准备。Citi报告没有展开的是：科沃斯在欧洲的渠\n\n[... middle omitted ...]\n\n者两家公司的详细财务对比感兴趣，欢迎来我们的微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n扫地机器人赛道，这两件事值得关注\n\n📌 EU关税风险暂缓 + 618超预期\n\n最近扫地机器人赛道有两个信号，值得拎出来看看。\n\n1️⃣ EU对中国产割草机器人暂不征收临时反倾销税\n- 6月19日，欧盟委员会发布初步结论，暂不征收临时反倾销税\n- 理由是智能割草机的成本和定价对比难度较大\n- 终裁预计要到2027年初，近期的关税风险被后置了\n- 这对某家欧洲畅销割草机品牌来说是利好，它在这个细分里暴露最多\n\n2️⃣ 某扫地机器人公司618战绩\n- 全渠道GMV 40.2亿，同比增长23%\n- 高端扫地机、擦窗机器人、洗地机是主要增长引擎\n- 其中T90扫地机系列卖了29万台，洗地机系列卖了23万台\n- 在4000元以上高端线排第一，擦窗机器人市占率65%+\n- 这个表现比市场预期的要好\n\n3️⃣ 另一家竞品说自己618开门红在天猫京东抖音三个平台都排第一\n- 但没公布完整618周期的具体数据\n- 目前来看，前者在高端线和擦窗领域更有优势\n\n🌟 一个观察：关税风险后置给了中国品牌更多时间布局海外，而618数据说明国内消费升级逻辑还在，尤其高端清洁电器依然有增长空间。\n\n扫地机器人这个赛道，接下来怎么走？欢迎一起讨\n\n[... middle omitted ...]\n\n its own press release, which we believe is better than market's expectations, led by premium robot vacuums, window-cleaning robots and Tineco floor washers. We continue to prefer Ecovacs (603\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R010",
    "title": "摩根斯坦利：MS：新主席，新美联储，但利率路径可能没那么新",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：新主席，新美联储，但利率路径可能没那么新\n\n这份由MS首席全球经济学家Seth B. Carpenter撰写的周日宏观周报，在Kevin Warsh首次以美联储主席身份主持议息会议后发出。它给出的核心判断是：市场正在过度解读一次加息的可能性，而真正重要的结构性变化——缩表、通胀目标框架、沟通方式——才刚刚开始，且方向远比利率路径更不确定。\n\n报告写于6月21日，恰逢市场消化6月FOMC会议后的第一周。声明和新闻发布会共同强化了市场对今年加息的预期，但MS认为，这种强化可能建立在脆弱的假设之上。Warsh刻意不给指引不是偶然，而是他的哲学：减少“前瞻指引”本身就是政策。这要求投资者从“猜利率”转向“猜框架”。\n\n以下是我们从这份报告中提炼出的五个层次判断。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 市场对一次加息的定价，可能忽略了通胀正在快速下行这一事实\n\n这是报告最锋利的一个洞察。FOMC点阵图中位数显示今年仅一次加息，但中位数的形成本身就具有偶然性——多一个加息点，中位数就从“不加”跳到“加一次”。而更关键的矛盾在于，这个加息路径对应的通胀预测是2026年核心PCE达到3.3%。\n\n但MS指出，关税对价格的推升效应已基本完成。油价大幅下跌，能源传导的“第二轮通胀”风险显著消退。他们明确写道：“FOMC的通胀预测是合理的，但不是最有可能的。”如果通胀实质性低于预期，而中位数参与者又预期明年降息，那么今年加息一次的逻辑就出现了自洽性难题——既然你知道明年要降息，为什么现在还要加息？\n\n> **KC评论：** 这相当于在说，市场可能正在为一个“一次性、象征性”的加息定价，而这个加息本身可能就不会发生。完整报告中还包含了MS对5月核心PCE的具体预测（0.36%月环比），以及他们如何通过历史修正来解读\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新主席，第一把火怎么烧？\n\n**新官上任，不划重点**\n\n某外资投行最新研报解析了美联储新主席Kevin Warsh的首秀，风格很不一样——他刻意不给市场\"指路\"。\n\n1️⃣ **利率路径：故意模糊**\n- Warsh明确表示，减少\"前瞻指引\"是他的核心哲学\n- 会议声明只说\"委员会将实现物价稳定\"，但没说怎么走\n- 有趣的是：FOMC点阵图显示今年只加一次息，但多一个点就可能变成不加\n- 关键矛盾：如果通胀确实回落（研报认为关税推价效应已基本结束），为啥要先加一次再考虑降？逻辑有点拧巴\n\n2️⃣ **缩表：可能比想象中猛**\n- Warsh主张更小的资产负债表规模\n- 一个有意思的路径：把财政部在美联储的账户减半，就能直接缩表约5000亿美元，且对市场几乎没影响\n- 降低对部分准备金支付的利率，也能减少银行对准备金的需求\n- 研报推测：最终缩表规模可能超预期，但对市场的冲击可能低于担忧\n\n3️⃣ **通胀目标：会变吗？**\n- Warsh重申2%通胀目标，但新设了一个通胀研究工作组\n- 市场已经在关注PCE和CPI之间的差异，会不会再出现新的\"脱节\"？\n- 研究会不会导致目标调整？目前没有明确信号\n\n[... middle omitted ...]\n\nrice stability” seems clear, but (again...by design) the path was not laid out. Before determining when the Fed will hike rates and by how much, consider the following. Chair Warsh did not wri\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R011",
    "title": "GS：油价下跌是顺风，但前端的利率不确定性才是真正的逆风",
    "digest": "[wechat_article.md]\n# GS：油价下跌是顺风，但前端的利率不确定性才是真正的逆风\n\n上周的市场，被两股力量同时拉扯：一边是多家央行的议息会议，另一边是美伊谈判的持续推进。最终的结果，用一个词概括就是“分化”——大宗商品和债券市场在定价衰退风险缓解，而利率市场却在定价更加鹰派、更加不确定的货币政策路径。\n\n这份GS最新的跨资产配置周报，给出了一个清晰但不简单的判断：**短期战术性中性，12个月战略性温和看多风险资产。** 但真正值得细读的，不是这个结论本身，而是支撑这个结论的三层逻辑——油价下跌如何改变了衰退概率，新主席的沟通风格如何重塑了利率预期，以及科技股为何在利率上行中依然坚挺。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油价大跌让衰退概率减半，但GS并未因此全面看多\n\nGS的大宗商品团队下调了布伦特原油价格预测，这一调整直接传导至宏观团队：他们将美国未来12个月衰退概率从25%下调至15%。逻辑很直接——更低的能源成本意味着更低的通胀压力，为消费者和企业提供了喘息空间，也给了美联储更多政策灵活性。\n\n但有趣的是，GS并未因此大幅上调风险资产配置权重。报告显示，他们维持战术性中性，仅对12个月维度保持温和超配股票。这意味着，油价下跌带来的“顺风”被其他因素抵消了。\n\n> **KC评论：** 衰退概率的下调是好事，但GS选择不以此作为加仓的理由。这提示投资者：不要因为一个好消息就全盘推翻之前的配置逻辑。完整报告中详细拆解了油价预测调整如何影响不同资产类别的收益率预期，以及GS内部跨部门观点是如何协调的——这些细节对于理解当前市场的定价结构非常关键。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 新主席的首秀让市场最不确定的不是方向，而是“如何沟通”\n\n这是美联储主席Kevin Wa\n\n[... middle omitted ...]\n\nI，也方便人工快速把握市场动态。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价降了，但利率更不确定了\n\n短期利率波动加大\n\n最近全球资产的关键词：油价下跌是顺风，短期利率不确定性是逆风。\n\n1️⃣ 油价走低，衰退概率下调\n某外资投行大宗商品团队下调了布伦特原油预测，经济学家随之将美国12个月衰退概率从25%砍到15%。油价下行对经济是实实在在的利好。\n\n2️⃣ 新主席首秀，鹰派信号拉满\n美联储新主席Warsh首次会议维持利率不变，但措辞偏鹰，美元指数冲到一年新高100.7。关键变化：他倾向减少前瞻指引和新闻发布会，这让短期政策路径的分布更宽、更不确定。\n\n3️⃣ 短期利率波动率飙升\n2年vs5年利率互换波动率比值飙到2023年初以来最高——市场对近端路径的困惑远超中期。虽然通胀预期因油价跌而下降，但2年实际利率仍接近2024年10月高位。\n\n4️⃣ 科技股免疫于利率上升\n纳指/标普比值在利率上行中反而走高。AI相关盈利预期和资本开支抵消了传统估值压力。但黄金承压，美元走强+利率上升让金价回调，黄金波动率现在比股票和利率都贵。\n\n5️⃣ 市场定价：短期利率将“粘住”\n美联储新沟通风格可能让短期利率波动持续。但期权市场显示，未来6个月2年美债利率偏离当前±50bp的概率约41%，高于1\n\n[... middle omitted ...]\n\ned policy rates by 25bp as widely expected, while the BoE held at 3.75%. Looking ahead, the US Core PCE release on Thursday will be the key data this week (GS: +0.31% m/m vs. 0.3% cons.). In t\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "GS：美国电力市场进入“区域撕裂”的夏季，PJM收紧而ERCOT松动",
    "digest": "[wechat_article.md]\n# GS：美国电力市场进入“区域撕裂”的夏季，PJM收紧而ERCOT松动\n\n美国电力市场正在进入一个罕见的“区域分化”夏季。GS在最新发布的Power Tracker报告中提供了一个清晰但容易被忽视的判断：美国电力市场并非整体紧张，而是出现了以PJM（中大西洋地区）持续收紧和ERCOT（德州）逐步软化为核心的“区域撕裂”格局。这一判断的含金量在于，它直接指向了数据中心选址、能源投资和电力资产定价的结构性错位。\n\n报告的核心信号是：PJM在6月合约换月时的电价涨幅远超十年均值，而ERCOT的同期涨幅却低于历史平均水平。这不是季节性波动，而是供给端基本面的根本性分化。GS还指出，联邦政府对煤电的7亿美元支持计划，对缓解市场紧张程度的作用可能有限。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PJM的6月电价跳升揭示了一个持续收紧的市场，而ERCOT的同期表现则确认了供给过剩的软化路径\n\nGS通过观察6月1日区域电力市场从交易6月合约换月至交易7月合约时的价格变化，发现了一个关键信号。在PJM市场，2026年5月至6月的电价绝对涨幅达到28美元/兆瓦时，远高于2016-2025年历史均值15美元/兆瓦时；百分比涨幅为44%，也高于历史均值30%。这一涨幅是在天然气和煤炭等边际燃料价格涨幅更小的背景下实现的，说明电价上涨的动力来自供需基本面而非燃料成本。\n\n相比之下，ERCOT市场同期绝对电价涨幅仅为24美元/兆瓦时，低于历史均值30美元/兆瓦时；百分比涨幅61%略高于历史均值56%，但5月和6月的价格水平均低于2024/2025年同期。这一对比直接验证了GS此前提出的“区域分化”观点：ERCOT自2025年下半年以来因大量新增电力供给而进入软化通道，而PJM预计在未来几年内仍将维持高度紧张状态。\n\n> **\n\n[... middle omitted ...]\n\n能源投资有进一步思考，欢迎来我们的知识星球和微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国电力市场：两个区域，两种剧本\n\n**区域分化，夏季见真章**\n\n**PJM紧，ERCOT松，煤炭政策能救场吗？**\n\n---\n\n6月1日是美国区域电力市场换月节点（从6月合约切换到7月合约），这次换月透露出两个关键信息：**市场对夏季紧张的预期**，以及**发电燃料成本的变化**。PJM（中大西洋）和ERCOT（德州）走出了截然不同的剧本。\n\n**1. PJM：紧上加紧**\n\n今年5-6月的换月，PJM电价涨幅显著高于过去十年均值：\n\n- 绝对涨幅：+28美元/兆瓦时（2026年）vs 历史均值+15美元/兆瓦时\n- 涨幅比例：+44% vs 历史均值+30%\n\n更关键的是，天然气和煤炭价格涨幅远没这么大。电价涨得比燃料成本快，说明**供需在收紧**。PJM聚集了美国39%的数据中心电力需求，需求增长持续快于供应增长。\n\n**2. ERCOT：开始松了**\n\n相比之下，ERCOT的换月表现偏弱：\n\n- 绝对涨幅：+24美元/兆瓦时，低于历史均值30美元/兆瓦时\n- 涨幅比例：61%，略高于历史均值56%，但5月和6月的**绝对价格水平**都低于2024/2025年\n\n原因很直接：德州从2025年底开始，发\n\n[... middle omitted ...]\n\nared to the historical average in the past decade, both in terms of the absolute price level (+28 USD/MWh in 2026 vs +15 USD/MWh in 2016-2025) and the percentage change (+44% vs +30%, Exhibit \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "Bernstein：中国半导体设备进口最差时刻已过，下半年将迎来修复",
    "digest": "[wechat_article.md]\n# Bernstein：中国半导体设备进口最差时刻已过，下半年将迎来修复\n\n中国半导体设备进口数据在2026年前五个月交出了一份让市场担忧的答卷。根据Bernstein最新发布的China WFE进口追踪报告，2026年1-5月，中国晶圆制造设备进口总额约为120亿美元，同比下降12%。5月单月进口额仅为22亿美元，远低于去年月均32亿美元的水平。\n\n这份数据表面上看是疲软的。但Bernstein分析师在报告标题中明确写出了一个与数据本身形成张力的判断：**“疲软持续，但预计下半年将复苏。”**\n\n这个判断并非简单的乐观主义。它建立在对进口结构、设备类型、区域来源以及主要设备商季度指引的交叉验证之上。当市场被月度数据的波动所困扰时，这份报告试图回答一个更根本的问题：中国半导体设备需求的真实底部在哪里，以及驱动修复的力量将从何而来。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月的疲软不是全面衰退，而是光刻机供给瓶颈的集中体现\n\n将5月进口数据拆解到设备类型后，一个清晰的图景浮现出来。5月进口总额22亿美元，环比下降20%，同比下降9%。但拉长到前五个月看，年累计同比下降12%的主要拖累因素只有一个：**光刻机进口同比下降24%**。\n\n光刻机在2026年前五个月的进口额仅为21.4亿美元，处于历史低位区间。5月单月光刻机进口2.97亿美元，虽然环比从4月的极低点有所恢复，但仍处于历史低位。Bernstein的回归模型估算，二季度ASML在中国的销售额将骤降至5.7亿欧元，环比下降52%，同比下降33%。这意味着中国在ASML二季度系统销售中的占比将降至仅9%。\n\n这不是需求问题，这是供给问题。ASML在Q1业绩会上已经重申，2026财年中国收入占比将从2025年的33%降至20%。Bernstein的判断是，\n\n[... middle omitted ...]\n\n—光刻机进口数据、存储WFE采购节奏以及国产替代的最新进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体投研：中国WFE进口仍弱，下半年有望回暖\n\n📉 5月进口数据解读\n\n**正文**\n\n刚看完某外资投行最新研报，关于中国半导体设备进口的月度追踪，信息量很大，直接上干货。\n\n**1. 整体数据：5月进口继续走弱**\n\n5月中国WFE（晶圆制造设备）进口额22亿美元，环比下降20%，同比下降9%。\n今年前5个月累计进口120亿美元，同比下滑12%。\n主要拖累因素是光刻设备，前5个月累计进口同比下降24%。\n\n**2. 光刻设备：供给短缺是主因**\n\n5月光刻进口2.97亿美元，虽然环比从4月低点回升，但仍处于历史低位。\n研报分析认为，光刻设备进口疲软主要受供给端限制，而非需求不足。\n光刻机龙头ASML此前明确表示，2026年中国收入占比将从2025年的33%降至20%。\n\n**3. 区域分布：东南亚通道持续活跃**\n\n从进口来源地看，新加坡和韩国表现强劲，同比分别增长38%和12%。\n美国+新加坡+马来西亚合计占比44%，而日本和荷兰分别占21%和16%。\n值得注意的是，美国供应商正越来越多地从新加坡/马来西亚的工厂向中国发货，以规避直接贸易限制。\n\n**4. 设备公司影响：分化明显**\n\n研报通过海关数据\n\n[... middle omitted ...]\n\ncee07cc6e3e79ab8355dc2cd0.jpg)\n\n![](images/d4c9f4653fa6b7f5fc7f1a004d043d1fa7e982976c6adf79d2ff57483ff61710.jpg)\n\n![](images/3d6fd9e528e2f8a7fcfbb465c70301a46d2d5b1a645c0e7e8d9461347e65d64a.jp\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R014",
    "title": "GS：中国对美出口已转负，但真正的拐点藏在6月之后",
    "digest": "[wechat_article.md]\n# GS：中国对美出口已转负，但真正的拐点藏在6月之后\n\n这份来自GS的最新周度关税影响追踪报告，传递了一个清晰但容易被忽视的信号：中国对美集装箱货流在最新一周出现了同比和环比的双重下滑。但这并非简单的“需求退潮”，而是一个更复杂格局的开端——去年“解放日”关税暂停期带来的提前抢运效应正在消退，同比基数将变得陡峭，而真正的考验在于，船公司、货主和物流商如何在不确定性中重新校准他们的库存与航线决策。\n\n报告的核心价值不在于给出一个方向性的看多或看空，而在于它用高频数据拆解了“关税影响”这个宏观概念，将其还原为每周的船舶离港数、TEU（标准箱）变动、港口吞吐量与运价波动。对于产业决策者和关注全球贸易格局的投资者而言，理解这些数据背后的逻辑，远比猜测下一个关税公告更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国出发的满载集装箱船已出现同比负增长，抢运效应正在快速消退\n\nGS追踪的数据显示，截至6月18日当周，从中国驶往美国的满载集装箱船数量环比下降4%，同比下降6%。这与前一周10%的同比增长形成了鲜明对比。TEU（标准箱）数据同样印证了这一趋势，同比下降4%，环比下降3%。\n\n这组数据最直接的解读是：去年“解放日”关税暂停后引发的集中抢运潮，其基数效应正在快速放大。2025年同期，大量货物为了赶在关税恢复前涌入美国，形成了异常高企的同比基数。当这个基数效应开始显现，即使绝对货量并未断崖式下跌，同比数据也会自然转负。\n\n> **KC评论：** 同比转负本身并不等同于需求崩溃。它更多是告诉我们，去年那个由政策窗口期驱动的“人造高峰”已经过去。真正值得关注的是未来几周环比数据的走向——如果环比持续负增长，才意味着需求本身在萎缩。GS报告里还有一张“TEU 15日滚动同比”的图表，能更清晰地看到这个拐点是如何形成\n\n[... middle omitted ...]\n\n动态。欢迎加入我们的星球微信群，一起追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国到美西的货量，拐点来了吗？\n\n**拐点观察**\n\n最近一周，中国发往美国的集装箱船数量环比下降4%，同比也转为-6%（前一周还是+10%）。数据开始走弱了。\n\n**1/ 洛杉矶港的短期节奏**\n- 刚过去的一周，进港TEU环比微增+1%\n- **下周（6/26）预计环比-6%**，再下周（7/3）又反弹+7%\n- 但同比来看，未来两周都是负数（-0.5%和-6%）\n- 原因是去年“解放日”后集中抢运，基数太高\n\n**2/ 海运价还在涨**\n- 中国/东亚→美西的集装箱运价，上周环比跳涨+19%\n- 同比也+3%，但后续可能波动——全球运力正在重新配置\n\n**3/ 卡车和铁路的局部信号**\n- 西海岸铁路联运量同比+11%（前一周+16%）\n- 卡车运力可用性同比+79%，但环比略降-3%\n- 卡车即期运价（不含油）同比+50%\n\n**4/ 中期怎么看？**\n研报核心逻辑：**2026年运输股能不能翻身，就看货量能不能持续增长。**\n- 美联储预计2026年12月有一次降息，通常利好运输板块\n- “解放日”一周年已过，货主有了更清晰的应对框架\n- 苹果、英伟达等大公司宣布增加美国本土制造，可能带动更多国内货\n\n[... middle omitted ...]\n\nestock with in some cases lower effective tariff rates amidst an uncertain geopolitical backdrop. China import comps may toughen ahead given the pull forward following the Liberation Day pause\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "GS：韩国出口加速，全球贸易最清晰的领先信号已经出现",
    "digest": "[wechat_article.md]\n# GS：韩国出口加速，全球贸易最清晰的领先信号已经出现\n\n全球投资者仍在争论“去全球化”与“再全球化”的叙事，但GS最新发布的韩国6月前20天出口数据，给出了一个更直接的答案：全球贸易正在加速，而不是减速。\n\n韩国6月前20个工作日日均出口环比增长8.7%，较前值3.1%明显提速。总出口环比增长5.7%，贸易顺差扩大至175亿美元的历史新高。这不是一个孤立的月度波动，而是一个连续加速的趋势信号——韩国出口在5月环比增长9.8%的基础上，6月进一步走强。\n\n对于任何一个跟踪全球周期的投资者来说，韩国出口数据都是最可靠的先行指标之一。韩国经济体高度外向，半导体、汽车、船舶、机械等产品覆盖全球供应链的各个环节。韩国的出口数据，本质上是全球制造业需求的一张实时心电图。\n\nGS这份报告的核心判断是：韩国出口的加速是广泛的，产品覆盖半导体、其他科技产品和非科技产品，区域覆盖亚洲新兴市场、中国、美国和日本。这不是一个由单一产品或单一市场驱动的脉冲，而是一个需求面同步改善的信号。\n\n> **KC评论：** 韩国出口数据之所以重要，不仅因为它是“全球贸易的煤矿中的金丝雀”，更因为它往往领先全球制造业PMI 1-2个月。6月数据意味着，三季度全球制造业活动大概率会继续改善。完整报告中的Exhibit 1提供了环比走势的时间序列，值得仔细对比历史拐点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 半导体增速放缓但仍在扩张，更值得关注的是其他科技产品出口的爆发\n\nGS报告显示，6月前20天韩国半导体出口环比仅增长2.0%，较前值11.9%明显放缓。半导体出口增速的放缓，可能会被部分投资者解读为AI需求见顶的信号。但GS的数据揭示了一个更完整的图景：其他科技产品出口环比增速从前值大幅跃升至17.1%，主要由计算机和家用电器出口驱动。\n\n[... middle omitted ...]\n\n群微信群里继续讨论，一起从数据中寻找全球贸易的真正信号。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国6月前20天出口加速，贸易顺差创新高\n\n出口加速，顺差新高\n\n韩国6月前20天出口数据出来了，日均出口环比增长8.7%，比上个月的3.1%明显提速。总出口环比增长5.7%，延续了不错的势头。\n\n1/ 主要产品都在涨\n半导体出口环比增长2.0%，虽然比上个月的11.9%放缓，但已经是连续第9个月增长。其他科技产品出口猛增17.1%，计算机和家电是主要推手。非科技产品出口也增长了4.8%，汽车、机械、石油、船舶都在提速。\n\n2/ 新兴市场是主力\n对新加坡出口暴增98.4%，马来西亚增长59.0%，台湾增长11.1%，这三个地方加起来贡献了约三分之二的环比增长。对中国大陆和日本出口增长约2%，对美国增长3.6%。\n\n3/ 进口温和增长，顺差创新高\n总进口环比增长3.1%，比上个月的5.4%放缓。一半的进口增长来自科技产品（半导体和手机）的反弹，能源产品进口因为石油制品收缩而走弱。贸易顺差从115亿美元扩大到175亿美元，创历史新高。\n\n这个数据说明全球贸易需求还在回暖，特别是科技产品和新兴市场。不过半导体出口增速在放缓，值得继续观察。\n\n#学习笔记\n\n[source_mineru.md]\n# South Kore\n\n[... middle omitted ...]\n\n11.5bn the prior month.\n\nIrene Choi\n+82(2)3788-1722 | irene.choi@gs.com\nGS (Asia) L.L.C., Seoul Branch\n\nGoohoon Kwon, CFA\n+852-2978-0048 |\ngoohoon.kwon@gs.com\nGS (Asia) L.L.C.\n\n## Key numbers:\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "Bernstein：锂价还没见顶，真正的高点在2027年",
    "digest": "[wechat_article.md]\n# Bernstein：锂价还没见顶，真正的高点在2027年\n\n碳酸锂价格从2025年低点至今已经上涨超过两倍，市场情绪从极度悲观迅速转向亢奋。但这份Bernstein的最新报告给出了一个与当前市场共识不同的判断：这轮上涨不是周期尾声的狂欢，而是中周期修复的中间站。\n\n报告的核心逻辑链条非常清晰。锂价在2025年触底后快速反弹，5月一度触及每吨3万美元，随后因部分停产产能重启回落至2万至2.5万美元区间。很多人认为这已经是顶部区域，但Bernstein认为，市场仍处于中周期修复阶段，真正的价格高峰可能要到2027年才会出现。\n\n这个判断的底层支撑来自三个相互强化的变量：需求端储能系统（ESS）的超预期爆发、供给端资本开支的滞后响应、以及库存水平已经进入历史性紧张区间。这三个变量共同指向一个结论——当前的价格上涨只是前奏。\n\n> **KC评论：** 这份报告最值得关注的地方不在于它预测了具体价格数字，而在于它提供了一个判断周期位置的框架。当市场情绪从极度悲观快速转向乐观时，最危险的事情就是把中周期误判为尾部。Bernstein用库存天数、资本开支周期和需求结构这三个指标，给出了一个相对清晰的定位工具。完整报告里还有一张历史周期对比图，展示了锂矿股在价格触底后6至12个月的典型表现路径，对于判断当前持仓节奏很有参考价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 储能需求正在改写锂市场的需求结构\n\n锂需求在2026年至今增长了约32%，远超供给24%的增速。这个剪刀差的直接结果是市场供需平衡显著收紧。但真正值得关注的不是总量增速，而是需求结构的变化。\n\n储能系统（ESS）需求同比增长了约100%，成为拉动锂需求最核心的引擎。相比之下，电动汽车（EV）需求增速仅为9%。这意味着锂市场的需求基本面正在发生结构性转变—\n\n[... middle omitted ...]\n\n的知识星球和微信群，与更多产业和投资领域的读者一起持续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n碳酸锂涨了，但还没到顶\n\n还在半山腰\n\n锂价2027年前还有空间\n\n最近碳酸锂价格从2025低点涨了两倍多，到了2万-2.5万美元/吨。但投行研报认为，现在只是周期中段，不是顶点。原因是库存才20天左右，历史经验看，低于20天价格容易加速上涨。\n\n1️⃣ 需求增速超过供给\n今年锂需求增长约32%，但供给只涨了24%。储能（ESS）需求同比翻倍，是最大推手，电动车需求仅增9%。供需缺口在拉大。\n\n2️⃣ 供给恢复有限\n约20万吨LCE的停产产能正在回归，但这只是短期缓冲。2026年能补一部分缺口，但2027年会更紧。资本开支还在低位，新项目启动需要时间。\n\n3️⃣ 价格能涨到哪\n研报上调了价格预测：2026年约2.5万美元/吨（之前2.1万），2027年约3.25万美元/吨（之前2.5万）。长期来看，行业需要1.5万-2万美元/吨才能维持10%的资本回报率。\n\n4️⃣ 库存信号很关键\n锂库存天数已降到20天以下，历史上每次跌破这个水平，价格都会出现更明显的上涨。目前库存还在继续收紧。\n\n研报还提到，锂业公司股价通常比现货价格提前6-12个月见底。当前板块反弹符合周期中段特征，而不是尾声。\n\n锂价还能走多远？欢迎\n\n[... middle omitted ...]\n\n before easing to \\$20–25k/t on supply restarts, which we view as a short-term buffer. We continue to view the market as being in a mid-cycle recovery rather than approaching a peak. Inventori\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R017",
    "title": "DB：航运业正在从“效率最大化”转向“韧性最优化”，这是一个被低估的投资窗口",
    "digest": "[wechat_article.md]\n# DB：航运业正在从“效率最大化”转向“韧性最优化”，这是一个被低估的投资窗口\n\n全球贸易的逻辑正在发生一次根本性的转向。过去三十年，航运业的核心驱动力是效率——更快的航线、更满的舱位、更低的成本。但DB在近期发布的航运行业深度报告中提出了一个明确的判断：这个时代已经结束。取而代之的，是一个以“韧性”和“安全”为核心的新逻辑。\n\n这份报告基于DB分析师参加 Marine Money Week 航运业年度大会后的观察与思考。他们发现，行业共识正在发生一次罕见的集体转向。与会者不再把地缘政治视为背景噪音，而是将其视为当前贸易格局最核心的塑造力量。从干散货到油轮，从LPG到LNG，几乎每个细分领域的船东都在重新思考同一个问题：当全球供应链从“追求效率”转向“追求安全”，谁的资产会受益？\n\nDB的结论很直接：航运资产，尤其是那些拥有现代化船队、资产负债表灵活、且具备运营敞口的优质公司，正在成为对冲地缘风险的不对称工具。这不是一个短期的交易逻辑，而是一个结构性的资产重估机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 地缘政治不再是变量，而是贸易模式的新操作系统\n\n过去，航运分析师的框架通常是“供需决定运价，地缘政治只是偶尔的扰动项”。但DB报告指出，这个框架已经过时。在Marine Money Week上，多个小组讨论都回到同一个判断：全球贸易正在从全球化走向区域化、自给自足、甚至“巴尔干化”。\n\n这意味着什么？报告给出了一个反直觉的推论：去全球化不一定会减少贸易总量，但它一定会让每一吨货物的运输距离变得更长、装卸效率变得更低、供应链冗余变得更多。当船只被迫绕行、港口作业效率下降、战略储备需求上升时，有效运力供给反而被压缩了。\n\n以霍尔木兹海峡为例。报告详细列举了船东们重返该区域需要满足的四个条件：完全停火、安全通\n\n[... middle omitted ...]\n\n群，继续讨论这份报告中的未解问题，以及更多的投资框架与数据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球航运正在“变慢变绕”\n\n效率退场，韧性登场\n\n航运业正在经历一场结构性转变：全球化退潮，地缘冲突频发，贸易路线不再追求最短最快，而是转向更安全、更冗余、更抗风险。简单说，效率让位给了韧性。\n\n这对航运公司来说反而是利好——航程变长、中转变多、库存需求增加，都会推高吨海里需求（即每吨货物运输一海里）和运费。\n\n1/ 地缘政治不再是背景音，而是主要驱动力\n- 霍尔木兹海峡危机后，船东们短期内不敢回去。他们列出的条件包括：完全停火、安全通行、保险正常化、地区稳定——目前都没满足。\n- 这意味着更多绕航、更多战略储油设施建设，直接推高运输需求。\n- 有趣的是，如果对伊朗石油的制裁放松，反而会利好主流合规油轮。因为伊朗“暗舰队”（老旧、维护差的船）会被更合规的船只取代，就像委内瑞拉现在的情况。\n\n2/ 中国仍是关键买家，但策略变了\n- 中国不再是过去那种房地产驱动的增长模式，但它依然是多种大宗商品的边际买家。\n- 贸易摩擦后，中国更强调供应链自主和“一带一路”整合。具体动作包括：从西非、南美进口更多铁矿石、铝土矿、谷物；从美国恢复采购粮食；从阿根廷囤积玉米。\n- 还有一个被低估的细节：中国进口的铁矿石品位在下降。这\n\n[... middle omitted ...]\n\n conference and presents our thesis that maritime shipping equity assets are an interesting opportunity for investors to hedge against greater geopolitical risk and uncertainty.\n\nThe conferenc\n\n[... middle omitted ...]\n\nited Kingdom\nTel: (44) 20 7545 8000\n\nDB Securities Inc.\n\nThe DB Center\n1 Columbus Circle\nNew York, NY 10019\nTel: (1) 212 250 2500\n\nDB AG\nFiliale Singapur\nOne Raffles Quay, South Tower\nSingapore 048583\nTel: (65) 6423 8001"
  },
  {
    "id": "R018",
    "title": "GS：美国衰退风险已降至15%，但增长引擎比想象更脆弱",
    "digest": "[wechat_article.md]\n# GS：美国衰退风险已降至15%，但增长引擎比想象更脆弱\n\n这份由GS首席经济学家Jan Hatzius在2026年6月发布的全球宏观报告，给出了一个看似矛盾的核心判断：美国经济衰退风险已从战时高点的25%回落至15%的长期常态水平，但这并不意味着市场可以高枕无忧。真正的风险正从“经济是否会衰退”转向“增长质量是否可持续”。\n\n报告最值得关注的信号不是衰退概率数字本身，而是支撑这一判断的几条逻辑链正在发生结构性变化：油价回落带来的通胀缓解是真实的，但AI资本开支对美国GDP的直接拉动微乎其微，劳动力市场的改善信号存在广泛分歧，而美联储新主席Warsh的沟通方式正在制造新的不确定性。\n\n以下是我们从报告中提炼出的六个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 衰退风险降至长期常态，但支撑逻辑并非来自内生增长\n\nGS将12个月美国衰退概率从25%进一步下调至15%，这是自2025年以来的最低水平。但支撑这一判断的核心变量并非美国经济自身动能的增强，而是外部冲击的消退。\n\n报告明确指出，下调衰退概率的最直接原因是美伊协议达成后油价预期的大幅回落。GS大宗商品团队将2026年底布伦特原油目标价下调至每桶80美元，且承认风险双向存在——霍尔木兹海峡的反复警告提醒市场，石油供给的恢复可能不会一帆风顺；但短期内，原油快速释放到一个战前就已供过于求的市场，也可能形成阶段性过剩。\n\n> **KC评论：** 衰退概率回到15%是一个重要的锚点信号，但决策者需要追问的是“为什么降下来了”。答案不是因为美国消费强劲或企业投资加速，而是因为地缘政治溢价消退。这意味着如果中东局势再次升温，这个15%的假设会迅速失效。完整报告中有一张美国衰退概率的时间序列图，值得仔细看的是它如何从20%降至15%——那条曲线的斜率比绝对水平更\n\n[... middle omitted ...]\n\n识星球微信群，继续讨论这些未解问题，以及更多报告背后的细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价跌了，但别急着喊“衰退解除”\n\n全球经济没那么糟，也没那么好\n\n1️⃣ 油价回落≠风险消失\n美伊协议降低经济下行风险，但油价可能短期过剩\n布伦特年底预计80美元，两边都有波动空间\n美国12个月衰退概率从25%砍到15%，回到长期均值\n\n2️⃣ 美国经济：AI撑场面，消费在喘\nAI资本开支多买亚洲芯片，对GDP拉动有限\n汽油降价确实利好实收入，但退税效应消退后，消费增速只剩1.5%\n就业数据“虚胖”，家庭调查和薪资增长都在走弱\n\n3️⃣ 通胀在降温，但方式不同\n6月汽油大跌直接拉低CPI，核心CPI未来三个月月均仅0.17%\n核心PCE更顽固，因软件和金融服务的权重更大\n更科学的“截尾均值PCE”反而更温和\n\n4️⃣ 美联储：新主席偏鹰，但未必真加息\nWarsh首秀偏鹰，半数委员点阵图暗示加息\n但其中一半是非投票委员，且油价暴跌让预测“过时”\n如果后续通胀下来、增长温和，大概率维持不动\n\n5️⃣ 欧洲日本各走各路\nECB 9月可能再加一次25bp，然后2027年回到2%\nBOJ继续温和加息，但核心通胀才1.5%，不着急\n中国4-5月数据疲软，Q3有望反弹，但内需出口差距拉大\n\n6️⃣ 市场消化FOMC冲击后\n\n[... middle omitted ...]\n\nurther from 25% to the long-term norm of 15%. (This is below our 20% estimate on the eve of the war because the labor market improvement since then indicates greater underlying resilience.)\n\nJ\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "Bernstein：世界杯掩盖了全球酒店业的真实分化",
    "digest": "[wechat_article.md]\n# Bernstein：世界杯掩盖了全球酒店业的真实分化\n\n全球酒店业正在经历一场被世界杯数据掩盖的结构性分化。Bernstein在最新发布的全球酒店与旅游研报中给出了一个核心判断：美国市场的强劲表现正在抵消中东、欧洲和中国的疲软，但这种“对冲”是不可持续的。Q2美国RevPAR同比增长4%，6月第一周加速至7%，世界杯效应将推动酒店集团达到甚至超出指引上限。然而，这份报告真正值得关注的不是世界杯带来的短期脉冲，而是三个正在重塑行业格局的长期变量：OTA流量结构的变化、AI作为新流量入口的早期信号、以及酒店开发在地缘冲突下的韧性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 世界杯红利集中在北美，掩盖了全球其他市场的真实疲软\n\nBernstein的数据显示，美国RevPAR在4-5月增长4%，6月第一周跳升至7%，而这一周仅进行了8场世界杯比赛，后续两周还有28场和36场。即使没有进一步加速，世界杯效应也足以将酒店集团推向指引上限甚至超出。Hyatt被列为最大受益者。\n\n但这份报告没有停留在这个表面利好。真正值得追问的是：世界杯之后，支撑北美需求的结构性因素是什么？Bernstein指出，北美市场的“K型复苏”依然存在——奢侈品酒店表现显著优于中端。Hyatt RevPAR增长4.3%，Marriott 3.2%，Hilton 2.9%，IHG仅2.6%，后者主要受中国业务拖累。\n\n> **KC评论：** 世界杯就像一针强心剂，但它掩盖了一个关键问题——如果没有这个短期事件，北美酒店业的真实需求曲线是怎样的？报告中的图表显示，Hyatt的RevPAR增速领先，但其估值倍数也最高。世界杯效应退潮后，这些高估值能否被持续的经营数据支撑，是完整报告里反复检验的核心假设。\n\n中东市场的疲软已被充分预期，但欧洲和中国增长\n\n[... middle omitted ...]\n\n解问题，以及完整报告中关于各家公司的具体估值模型和风险敞口。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n世界杯撑起Q2，酒店OTA谁最稳？\n\n世界杯红利期，酒店赢家是谁\n\n北美RevPAR冲高，中东欧洲在拖后腿\n\nQ2的全球酒店和OTA数据出来了，亮点在北美，世界杯效应比想象中更猛。某外资投行刚出的研报，逻辑很清晰，我拆成三条讲给你听。\n\n1️⃣ 酒店板块：世界杯推高，但K形分化明显\n- 美国RevPAR 4-5月涨4%，6月第一周直接跳到7%，世界杯赛程密集是关键推手。\n- 研报预计，只要6月保持这个节奏，酒店集团业绩能冲到指引上限甚至更高，Hyatt被点名领跑。\n- 但全球是K形复苏：北美强，中东（早就在预期内偏弱）、欧洲和中国增长更慢。豪华品牌（Hyatt +4.3%、Marriott +3.2%）明显跑赢中端（IHG受中国拖累仅+2.6%）。\n- 开发端倒挺稳，中东冲突没压住酒店建设潮，全球在建房间比年初多了6.1%。\n\n2️⃣ OTA板块：Airbnb最干净，Booking能超预期，Expedia最悬\n- 三家大平台Q2流量都放缓了，但分化严重。\n  - Airbnb：网页流量还在涨（低双位数），下载量加速到~30% y/y，增量主要来自印度、巴基斯坦、印尼。研报预计夜量增长约10%，比共识高1.6%\n\n[... middle omitted ...]\n\n660723ae812e5e077a9818f4f.jpg)\n\nSabrina Blanc\n\n+33 1 42 13 47 32\n\nsabrina.blanc@bernsteinsg.com\n\nThe headline grabbing numbers at Q2 look set to be in US RevPAR. US RevPAR rose 4% across April\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R020",
    "title": "GS：全球电动车正在“再电气化”，但这次主角是中国",
    "digest": "[wechat_article.md]\n# GS：全球电动车正在“再电气化”，但这次主角是中国\n\n当全球汽车行业还在消化2024年电动车增速放缓的悲观叙事时，GS最新发布的全球汽车研报给出了一个截然不同的信号：全球纯电动车（BEV）销售占比已从2月的13%反弹至5月的19%。这不是一个温和的复苏，而是一次明确的“再电气化”（re-electrification）。\n\n这份由GS日本首席汽车分析师Kota Yuzawa领衔的研报，核心判断简洁而有力：驱动本轮反弹的力量并非技术突破，而是地缘政治——中东局势不稳推高了汽油价格，消费者用钱包投票，转向了电动车。但更值得产业决策者关注的，是这轮反弹背后的结构性分化：中国正在加速，美国在倒退，而泰国和澳大利亚正成为新的增长极。\n\n如果你以为这只是油价的短期扰动，那可能会错过一个更重要的趋势：中国电动车制造商正在利用成本优势重塑全球供应链，欧洲和日本传统车企的反应已经开始改变游戏规则。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球电动车渗透率在5月跳升，但驱动力不是环保而是地缘政治\n\nGS的数据显示，全球BEV销售占比在2月触底13%后，连续三个月攀升至5月的19%。这一增速在过去两年中极为罕见。报告明确指出，推动这一变化的核心变量是中东局势导致的油价上涨——当汽油价格走高，消费者对电动车的接受度随之提升。\n\n但“平均”数据掩盖了巨大的区域差异。中国BEV渗透率在短短三个月内跳升了10个百分点，成为全球最强劲的增量来源。而美国BEV渗透率反而下降了1个百分点——在高利率环境和充电基础设施不足的双重压力下，美国消费者正在退回到燃油车或混动车型。\n\n> **KC评论：** GS的这个判断很关键——它把电动车的短期需求波动从一个“技术叙事”重新拉回到“能源价格叙事”。这意味着，如果你在跟踪电动车供应链的投资机会，油\n\n[... middle omitted ...]\n\n的最新观点，以及中国车企的月度出口数据和欧洲政策的立法进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球电动车，正在重新加速\n\n🌍 区域分化明显\n\n全球纯电渗透率从2月的13%涨到5月的19%，中东局势是催化剂。\n\n但地区差异很大：中国纯电渗透率一个月跳升10个百分点，泰国涨了19个百分点，澳洲+6个百分点。美国反而掉了1个百分点。欧洲整体+2个百分点，德国表现不错，涨了3个点。\n\n油价和储备条件是关键变量，直接影响消费者的购买决策。\n\n📊 价格战在降温\n\n某外资投行的价格调查显示：美加市场售价小幅下降，但其他地区价格企稳甚至回升。\n\n原因是再电动化趋势下，新兴纯电车厂定价更保守了。\n\n但注意——铝、石脑油、内存等原材料在涨价，研报预计2026年利润率同比会恶化3个百分点。目前还没有哪个区域涨价幅度能覆盖成本压力。\n\n🔧 供应链正在变天\n\n中国纯电车厂在全球的份额持续上升，成本竞争力开始改写游戏规则：\n\n1️⃣ 欧洲3月提出的IAA法案，要求电池以外70%以上零部件本地化，保护区域经济\n2️⃣ 传统车企正在大幅调整采购策略，日本车企开始积极采用中国零部件或中国标准件\n\n⛽ 6-7月是观察窗口\n\n研报大宗商品团队下调了WTI油价预测：2026年从85→80，2027年从75→70，2028年从70→66美元/\n\n[... middle omitted ...]\n\nular expanded by 3 pp. It is highly likely that oil reserve conditions and rising gasoline prices are significantly impacting consumer purchasing behavior.\n\n## Price competition moderates with\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R021",
    "title": "JPM：铜价核心矛盾已从供需转向关税，中国正失去定价权",
    "digest": "[wechat_article.md]\n# JPM：铜价核心矛盾已从供需转向关税，中国正失去定价权\n\n这份JPM最新发布的铜市场深度报告，给出了一个反直觉的判断：全球精炼铜市场正处于2025年超过50万吨的过剩状态，但LME铜价在过去一年却上涨了超过40%，并在2026年持续高位运行。供需基本面与价格走势之间的背离，并非市场失灵，而是全球铜定价权的结构性转移。\n\n报告的核心主张清晰而锐利：当前铜市场的核心驱动力已不再是全球供需平衡表，而是美国关税政策预期所引发的“美中铜拉锯战”。在这场拉锯中，中国作为全球最大铜消费国的传统边际定价权正在被削弱，而美国通过COMEX/LME价差机制，正在以前所未有的力度从全球市场“虹吸”铜资源。报告预测，这一格局将推动铜价在未来几个季度向每吨15000美元迈进，而2026年下半年的关键催化剂，并非任何供需数据，而是美国对铜232条款关税审查的沟通与执行节奏。\n\n以下是我们对这份报告核心逻辑与投资含义的拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球供需平衡表已失去定价权，美国才是新的边际买家\n\n传统铜市场分析框架中，全球精炼铜的供需缺口是判断价格方向的核心变量。但JPM这份报告明确指出，这一框架在当前阶段已基本失效。2025年全球精炼铜市场过剩超过50万吨，LME铜价却全年上涨42%；2026年过剩预计仍有约36万吨，但价格依然在每吨13600美元附近高位运行。\n\n这种背离的直接原因，是美国自2025年初以来通过持续高企的COMEX/LME价差，从全球市场大量进口铜。报告估算，过去18个月，美国累计建立了约120万吨的铜库存——这相当于2024年全年美国铜进口量的近20个月水平。美国实际铜消费仅占全球约6%，但过去一年半的进口行为，使其对全球铜市场的拉动力度相当于一个消费占比9%的经济体。\n\n这意味着，全球铜市\n\n[... middle omitted ...]\n\narket dynamics。欢迎来星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜的拉锯战：美国在囤，中国在扛\n\n铜价冲向15000\n\n供需平衡已不是定价关键\n\n最近在看某外资投行关于铜的深度研报，逻辑很有意思——全球精铜明明是过剩的，但铜价却一路冲到13600美元/吨，涨了40%以上。\n\n核心原因就一个：**美国在疯狂囤铜**。\n\n1/ 美国从2025年初就开始通过COMEX/LME价差套利，大量进口铜。18个月里，美国囤了约120万吨精铜库存——相当于全球年需求的近2%。\n\n2/ 中国原来才是铜价的边际定价者，价格高了就“买家罢工”，等跌了再买。但现在不行了——美国抢走了大量铜，中国为了保证进口需求，不得不接受更高的价格。买价底线从10000-11000美元/吨，一路抬升到12500甚至13500美元/吨。\n\n3/ 接下来最关键的时间点是6月30日——美国将公布对精铜的232关税评估结果。研报判断，特朗普政府会选择**阶梯式加税**，而不是一次性到位。\n\n为什么是阶梯式？因为美国已经囤了120万吨铜，如果立刻加50%关税，价差关闭，美国就变成铜的净卖家，库存会快速流出。阶梯式加税能继续吸引铜流入美国，同时让已囤的铜留在境内。\n\n4/ 对LME铜价来说，**关税的“升级预期”比关税本身\n\n[... middle omitted ...]\n\nly 2025, tightening the ex-US market and reducing China’s historical role as the marginal price setter.\n\n\\- Amid this competition, China's buying floor has shifted materially higher. Despite e\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 21 Jun 2026 09:01 PM BST\n\nDisseminated 21 Jun 2026 09:01 PM BST"
  },
  {
    "id": "R022",
    "title": "NOM：中国楼市K型分化已成定局，全国复苏仍是伪命题",
    "digest": "[wechat_article.md]\n# NOM：中国楼市K型分化已成定局，全国复苏仍是伪命题\n\n中国房地产市场正在上演一场“冰与火之歌”。少数“聪明城市”的房价已经企稳甚至反弹，但全国平均房价跌幅却在5月重新扩大，地产投资与销售数据持续恶化。NOM在最新研报中给出了一个清晰但令人不安的判断：中国楼市正出现地理上的“K型分化”，而AI带来的股市繁荣，非但无法成为全国楼市的解药，反而可能加剧了区域与人群间的财富不平等。\n\n这份报告的核心洞察在于：市场期待已久的“全面复苏”可能根本不会到来。取而代之的，是一个被AI与政策选择性托举的“头部城市”与基本面持续恶化的“广大低线城市”之间的结构性断裂。对于投资者和决策者而言，理解这个“K型”的走向，远比押注一个模糊的“底部”更为关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 头部城市房价已连续三个月上涨，但支撑逻辑并非普适\n\nNOM的数据显示，北京、上海、广州、深圳四个一线城市的二手房价格在5月实现了0.4%的环比平均涨幅，且已连续三个月保持正增长。其中，上海是70个大中城市中表现最强劲的，5月环比上涨0.6%，从1月低点累计反弹1.9%。深圳紧随其后，同样录得0.6%的月度涨幅，这得益于4月30日进一步放松的限购政策。\n\n但这份回暖的“含金量”需要仔细拆解。以上海为例，其价格稳定的背后是成交量的大幅放量和挂牌量的急剧萎缩。5月10日，上海单日二手房成交量创下1664套的五年新高。同时，安居客数据显示，截至5月31日，上海有效二手房挂牌量同比下降近20%。更关键的结构性变化在于，成交主力正在从“老破小”向改善型房源迁移。链家数据显示，5月上海总价500-800万元的房源成交环比激增9.3%，而300万元以下的低总价房源成交反而环比下降2.6%。\n\n> **KC评论：** 这意味着，上海楼市的回暖并非“雨露\n\n[... middle omitted ...]\n\n微信群里继续讨论这些未解的问题，共同追踪K型分化的演进路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI造富 vs 地产分化\n\nK型楼市，正在发生\n\n最近读到一份某外资投行的研报，讲的是中国楼市的K型分化，信息量很大，直接拆给你看👇\n\n1️⃣ 聪明城市在回暖，其他在跌\n一线城市二手房连涨3个月，月均+0.4%。\n上海最猛，5月环比+0.6%，从1月低点累计涨了1.9%。\n深圳5月也+0.6%，靠的是4月底放开限购。\n北京、广州也有温和上涨。\n杭州、合肥等少数二线城市出现企稳信号。\n\n但大部分低线城市房价跌幅在扩大。\n5月70城二手房均价环比-0.26%，比4月的-0.23%更差。\nK型分化越来越明显——少数城市涨，多数城市跌。\n\n2️⃣ 全国数据更糟，小城市拖后腿\n4-5月新房销售面积同比-11.4%，比Q1的-10.4%还差。\n新房销售额同比-8.7%，反而比Q1的-16.7%收窄——研报说，是因为一线城市销售额占比高（约18%），拉高了整体。\n房地产投资4-5月同比-22.3%，比Q1的-11.2%恶化了一倍。\n百强房企前5月合同销售面积同比-20.1%，销售额-15.3%，比2021年同期跌了80%以上。\n\n3️⃣ 股市涨了，但只帮到富人\nAI带动科技股大涨，A股科技板块市值占比超30%。\n股市财富效\n\n[... middle omitted ...]\n\nr signs of stabilization, while price declines in most lower-tier cities have worsened. On net, overall housing prices have fallen at a faster pace, leading to heightened downward pressures on\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R023",
    "title": "GS：端午假期掩盖了一个关键信号——中国楼市底部的韧性正在积累",
    "digest": "[wechat_article.md]\n# GS：端午假期掩盖了一个关键信号——中国楼市底部的韧性正在积累\n\n市场看到的是成交量回落，GS看到的却是“剔除假期后，底层动能仍然为正”。这份最新周度跟踪报告揭示了一个微妙但值得重视的分化：当多数人因节日数据走弱而继续悲观时，少数决策者应该关注的是“剔除噪音后的真实方向”。\n\n本周（Week 25）中国房地产市场出现了明显的成交量环比回调，新房销售面积环比下降5%，二手房更达20%。单看这些数字，很容易得出“市场再次走弱”的结论。但GS分析师特别指出，这主要是受6月19日至21日端午节假期影响。如果剔除这一扰动，新房市场成交环比实际改善6%，二手房也录得2%的环比增长——两者分别比6月日均水平高出7%和31%。\n\n这组数据隐含的判断是：中国房地产市场的自然需求并未恶化，而是在一个相对低位上出现了企稳迹象。对于长期跟踪这个板块的投资者而言，这可能是过去几个月里最值得认真对待的信号之一。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供应端主动收缩正在改善价格预期，而非需求端崩溃\n\n市场通常把成交量下降等同于需求疲软。但GS报告揭示了一个更精细的机制：本周新房上市量环比大幅减少了15%，直接导致库存周转月数下降至27.7个月，低于5月均值28.5个月。与此同时，监测城市的成交均价环比微涨0.8%。\n\n这意味着什么？供应端的主动收缩——而非需求端的突然崩溃——是当前市场的主要驱动因素。开发商在去库存压力下选择控制推盘节奏，反而对价格形成了支撑。这与2024年“量价齐跌”的局面有本质区别。对于关注资产定价的读者来说，这是一个需要重新评估的变量：如果供应端持续克制，价格底部的确认时间可能比预期更早。\n\n> **KC评论：** 很多人只看成交量绝对值，但GS告诉我们，供应端的行为变化同样重要。开发商不再不计代价\n\n[... middle omitted ...]\n\n差异化定价逻辑有持续跟踪的需求，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午后市场降温？数据拆给你看\n\n📊 端午假期后，楼市数据怎么看？\n\n上周正好赶上端午小长假（6/19-6/21），新房成交环比-5%，二手房-20%，看起来有点冷。\n\n但把假期影响去掉，实际内生动力还不错👇\n\n1️⃣ 新房成交环比+6%，二手房+2%\n都超过了6月的日均水平（分别高出7%和31%）\n\n2️⃣ 价格反而稳住了\n监测城市成交均价环比+0.8%\n背后原因：供应端收紧了，新房入市量环比-15%\n\n3️⃣ 库存压力在缓\n库存月数27.7个月，低于5月均值28.5，说明去化节奏在改善\n\n再看几个关键信号📌\n\n🔹 6月百强房企合同销售预计同比-8%（5月是-2%），还在收缩\n🔹 竣工端：6月预计同比-20%，全年预计-1%（某外资投行模型推算）\n🔹 新开工：6月预计同比降幅在25%-30%之间（基于土地成交和水泥出货量推测）\n\n估值方面，覆盖的地产股上周普跌👇\n- 强国企开发商平均-12%（保利相对抗跌，-4%）\n- 民企开发商平均-14%\n- 其他国企开发商平均-4%\n\n目前港股覆盖标的平均较2026年底NAV折价38%，A股折价31%，都在历史低位区间。\n\n🤔 问题来了：供应收缩推稳了价格，但成交量还在\n\n[... middle omitted ...]\n\nd with new home searches dipping 0.4% wow while secondary subscription sales and visitations moderating \\~15% wow, transaction price improved +0.8% wow across monitored cities, supported by mo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R024",
    "title": "GS：传统服务器正在被AI“吃掉”",
    "digest": "[wechat_article.md]\n# GS：传统服务器正在被AI“吃掉”\n\n当所有人都在谈论英伟达的GPU如何改变世界时，GS一份长达数十页的服务器产业报告揭示了一个被忽视的结构性变化：传统服务器市场正在被AI服务器“吃掉”，而这场吞噬不仅发生在营收数字上，更在重塑整个硬件产业的利润池和竞争规则。\n\n这份由GS硬件分析师团队完成的产业入门报告，并非简单的行业科普。它给出了一个清晰的判断框架：到2030年，全球服务器市场将从2025年的2840亿美元增长至1.4万亿美元，复合年增长率38%。但真正值得关注的不是总量，而是结构——加速服务器（AI服务器）将以45%的五年复合增速增长至1.2万亿美元，而传统服务器即便保持13%的增速，到2030年也只有1640亿美元。\n\n这意味着什么？AI服务器将在五年内吃掉整个服务器市场85%的营收份额。传统服务器不仅增长缓慢，其单位出货量甚至可能进入长期收缩通道。\n\n但这份报告最锋利的地方，不在市场预测，而在它揭示了一个隐蔽的囚徒困境：传统服务器越高效，OEM厂商的利润池越危险。\n\n> **KC评论：** GS这份报告的核心贡献不是给出了一个万亿级市场的预测数字——这个数字市场早有共识——而是把“服务器密度提升”和“OEM利润”之间的冲突量化了出来。如果你只看营收预测，你会觉得这是个稳健增长的行业。但如果你看单位经济模型，你会意识到传统服务器OEM正在面临一个“量缩价难升”的困局。完整报告里有详细的BOM拆解和情景分析，值得仔细推敲。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 传统服务器正在经历一场“自我吞噬”式的效率革命\n\nGS估计，全球传统服务器装机量约为7000万台，平均使用寿命已从2003-2019年的4.4年延长至目前的5.7年。这背后有两个动力：一是超大规模云服务商将服务器折旧年限从3年拉长到5-6\n\n[... middle omitted ...]\n\ns。欢迎来星球微信群里继续讨论，一起追踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n传统服务器，正在被AI“吃掉”\n\n服务器市场大变局\n\n最近读了一份某外资投行的服务器行业研报，信息量很大。简单拆解给大家：\n\n**1. 市场在“分裂”**\n服务器市场正被一刀切成两块：传统服务器（通用型）和加速服务器（带GPU的AI服务器）。2025年整个服务器市场约2840亿美元，同比+45%，几乎全是AI服务器在拉。传统服务器虽然也有+10%的增长，但出货量反而下滑了18%——大家买的都是更贵的机器。\n\n**2. AI服务器才是主角**\n研报预测，到2030年全球服务器市场将达1.4万亿美元，年复合增速38%。其中传统服务器到2030年只有1640亿（增速13%），而加速服务器将冲到1.2万亿（增速45%）。简单说，未来五年服务器增长，几乎全靠AI。\n\n**3. 传统服务器在“缩量提价”**\n全球传统服务器保有量约7000万台，平均寿命已从4.4年延长到5.7年。超大规模云厂商把服务器折旧年限从3年拉到5-6年，企业也在“机器用到冒烟”。更关键的是，新一代服务器密度极高——比如某品牌17代服务器可以1台替代6台14代老机器。如果大规模替换，传统服务器出货量可能从年均1190万台骤降到400万甚至170万台\n\n[... middle omitted ...]\n\n and long-term shifts within the global server ecosystem.\n\n## Key areas of focus in this primer include:\n\n2026-30 server market forecast: 650 Group forecasts the global server market to grow a\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R025",
    "title": "摩根斯坦利：Bernstein：中国啤酒五月数据揭示，喜力加速而百威仍在挣扎",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：Bernstein：中国啤酒五月数据揭示，喜力加速而百威仍在挣扎\n\n中国啤酒行业正在经历一场无声的权力交接。Bernstein最新发布的5月跟踪数据显示，行业整体销售额同比微增2%，但这份温和的行业均值之下，是各品牌之间愈发悬殊的走势分化。华润啤酒旗下的喜力正在以37%的同比增速碾压高端赛道，而百威中国却连续多月陷入负增长泥潭，5月销售额再度下滑3%。这不是一次简单的月度波动，而是中国啤酒市场结构性力量重组的信号。\n\n这份基于18万家超市POS数据和23万家餐厅二维码数据的月度报告，为我们提供了比上市公司季度财报更及时、更精细的竞争图景。当行业总量增长乏力时，谁在抢夺份额、谁在丢失阵地，才是真正决定未来三年投资回报的关键变量。\n\n> **KC评论：** 2%的行业增速听起来平淡无奇，但真正的故事藏在结构里。Bernstein的数据颗粒度让我们能看到，华润啤酒正在用喜力这把尖刀，精准切入百威最核心的高端腹地。这种“总量平淡、结构剧烈”的格局，往往是龙头公司估值分化的前夜。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 喜力加速的本质不是品牌力，而是华润的渠道执行力\n\n5月数据中最亮眼的信号来自喜力。在整体高端啤酒品类增长5%的背景下，喜力以37%的同比增速跑赢了整个类别7倍以上。更值得注意的是，喜力在餐饮和零售两个渠道均实现了11%的增长，且环比4月均在加速。\n\n这组数字的背后，不是简单的“消费者更喜欢喜力了”。Bernstein的数据显示，华润啤酒在广东和福建两个省份实现了餐饮和零售渠道的双位数增长。广东是中国啤酒消费的第一大省，占全国销售额的17%，同时也是百威的传统强势区域。华润在广东的突破，意味着其渠道下沉和终端覆盖的策略正在产生实质性效果。\n\n华润啤酒整体的5月销售额增速为3%，虽然看起来\n\n[... middle omitted ...]\n\n一起，第一时间获取这些高价值的信息，并参与深入的讨论与追问。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月啤酒数据更新：喜力加速，百威还在挣扎\n\n喜力狂飙，百威承压\n\n5月啤酒行业整体销售额+2%，餐饮渠道稳定，但格局分化明显\n\n1️⃣ 行业整体：5月销售额同比+2%，较4月的+1%小幅改善。餐饮渠道维持+3%增长，非即饮渠道从-1%转正至+1%。\n\n2️⃣ 玩家表现分化：\n• 雪花啤酒：+3%，喜力品牌表现亮眼，增速高达+37%，带动雪花在高端段跑赢行业（+11% vs +5%）。广东、福建两省双渠道均实现双位数增长。\n• 青岛啤酒：-2%，主产区山东拖累明显，餐饮渠道表现比3-4月更差。\n• 百威中国：-3%，和4月持平，但较Q1的-8%和Q4的-11%明显收窄。非即饮渠道仍跌-10%，渠道扩张策略效果待验证。\n• 燕京（未覆盖）：+17%，继续领跑。\n• 重庆（未覆盖）：+9%，但环比4月+12%有所放缓。\n\n3️⃣ 区域亮点：浙江非即饮从-7%大幅反弹至+11%，江苏从-11%升至+5%。广东餐饮渠道+20%领跑全国，但百威在该区域表现落后于整体。\n\n4️⃣ 价格段：高端段+5%持续增长，超高端仍跌-10%，主流及经济段转正至+2%。\n\n从Q2至今数据推算，雪花Q2营收增速有望加速至约+2%，百威降幅\n\n[... middle omitted ...]\n\nstep up from April's 1% growth. Restaurant channel value growth continued in line with April at +3%, while off-trade value growth improved to +1% from -1% in April. Yanjing (not covered) was a\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R026",
    "title": "Citi：日本材料商手握AI供应链命脉，但还缺一张“涨价”的通行证",
    "digest": "[wechat_article.md]\n# Citi：日本材料商手握AI供应链命脉，但还缺一张“涨价”的通行证\n\n当全球投资者的目光都聚焦在英伟达的GPU迭代、台积电的先进封装产能，以及美国对华半导体设备出口管制时，一份来自Citi的深度研报将聚光灯转向了一个相对低调却至关重要的环节——日本材料商。\n\n这份报告的核心判断清晰且犀利：**日本材料企业是当前AI供应链中不可绕过的技术底座，但其资本市场表现与产业地位之间存在显著落差。** 落差的核心，不在于技术，而在于定价策略与下游需求感知能力。\n\n这不是一份简单的“日本材料股推荐清单”。Citi通过与管理层（而非IR部门）的直接对话，揭示了日本材料行业正在经历的“甜蜜与痛苦”：技术壁垒极高，需求确定性极强，但企业自身在将技术优势转化为利润增长上的犹豫，正在让投资者失去耐心。\n\n对于关注AI硬件产业链、日本制造业复苏以及全球供应链重构的读者而言，这份报告提供了一个关键的观察窗口：当“卖铲子”的生意变得炙手可热，铲子的定价权究竟在谁手里？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 技术护城河比想象中更深，但市场需要看到“变现”的意愿\n\nCiti在与多家日本材料企业管理层的访谈中，首先确认了一个令同行羡慕的事实：日本在AI相关关键材料领域的技术优势是真实且牢固的。\n\n以JX Advanced Metals为例，其在InP（磷化铟）衬底、半导体溅射靶材、HDD磁记录靶材等多个领域占据全球40%至60%不等的市场份额，甚至在EUV光刻反射材料上近乎垄断。三井金属在HVLP5铜箔上拥有80%的份额，旭化成在RDL（重布线层）材料上拥有极高份额。这些数据表明，AI服务器的“心脏”和“血管”，很大程度依赖这些日本企业的供应。\n\n然而，报告同时点出了一个尖锐的矛盾：**投资者对日本材料商在价格谈判中的“低姿态”感到沮丧\n\n[... middle omitted ...]\n\n球微信群里继续讨论，共同拆解日本材料涨价浪潮的下一阶段信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本材料厂，AI供应链的隐形冠军\n\n日本材料厂正在AI供应链里大杀四方\n\n刚跟几家日本材料巨头的技术负责人聊完，信息量巨大。他们不声不响，但AI核心材料几乎都被日本公司卡着脖子。\n\n1/ AI需求不只是“热”，是管理层都亲自下场\n这次聊的不是IR部门，而是执行董事、事业部总经理。三菱瓦斯化学、日东纺、JX Advanced Metals、旭化成、三井金属的高管们，口径高度一致：AI材料需求不是短期风口，是结构性增长。日本材料厂的技术壁垒，比市场想象的要深。\n\n2/ 但定价策略太保守，外资都看不下去了\n日本材料厂技术强，但谈价格时总“不好意思”。某外资研报直接吐槽：明明供需紧张、技术独供，却不敢涨价。\n不过JX Advanced Metals是个例外——InP基板产能要扩10倍，还暗示要涨价2-3倍。外资投资者说：“这不像日本公司的风格，但太对了。”\n\n3/ 下游趋势看不清？这是日本材料厂的“盲区”\n很多上游材料厂只知道直接客户的订单，但不知道材料最终用在GPU还是交换机里。研报说，如果能打通“下游需求感知”能力，就能提前布局下一代产品，避免重复下单导致的供给过剩。\n\n4/ 几个关键材料玩家的动向\n- 三菱瓦斯\n\n[... middle omitted ...]\n\nusiness); Nitto Boseki's Hiroki Kajikawa (Senior Executive Officer, Deputy Division General Manager of the Corporate Management Division, General Manager Corporate Communication); JX Advanced \n\n[... middle omitted ...]\n\nk to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party."
  },
  {
    "id": "R027",
    "title": "摩根斯坦利：MS：MCU涨价不是需求回暖，是供给被AI“挤”出来的",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：MCU涨价不是需求回暖，是供给被AI“挤”出来的\n\nMCU现货价格在6月走平，但这只是暴风雨前的宁静。MS最新研报发出明确信号：下半年MCU价格将再次上涨，但驱动因素并非终端需求复苏，而是成熟制程产能被AI相关应用大量挤占。这是半导体周期中一种罕见的“无需求复苏的涨价”，对产业格局和投资逻辑的影响需要重新审视。\n\n这份由Daniel Yen、Charlie Chan等分析师联合撰写的报告，在6月21日更新了对大中华区MCU市场的判断。核心结论清晰而克制：供给紧张将在下半年持续，现货价格有望再次上行，但最终用户需求并未明显改善。这意味着，当前的价格上涨更多是成本推动和渠道补库，而非终端拉动的健康循环。\n\n对于关注半导体周期的投资者来说，这是一个需要警惕的信号。当涨价不是来自需求扩张，而是来自供给收缩，企业的议价能力和利润持续性将出现显著分化。MS在报告中对不同MCU厂商给出了截然不同的评级，正是基于对这一结构性差异的判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮涨价的核心驱动力不是需求，而是AI对成熟制程产能的挤出\n\nMS报告中最反直觉的判断是：MCU涨价并非下游需求回暖的结果。6月现货价格环比持平，STMicro的32位MCU现货价维持在12.8元人民币，GigaDevice同规格产品为8.5元人民币，均未出现明显波动。同时，报告明确指出“消费和工业终端需求与上月基本持平”。\n\n那么涨价动力来自哪里？答案是供给端。成熟制程代工厂正在将更多产能分配给AI电源相关应用。这是一个容易被忽视但影响深远的结构性变化。当台积电、联电等代工厂的成熟制程产能被AI基础设施的电源管理芯片、驱动芯片等持续占用，留给MCU设计公司的产能空间就被压缩了。而新产能上线有限，供给紧张局面在下半年难以缓解。\n\n[... middle omitted ...]\n\n缘AI的长期机会有进一步兴趣，欢迎来星球和微信群中继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMCU下半年还要涨价？不是需求驱动\n\nMCU下半年涨价预期\n\n6月现货价持平，但ST下周一涨价，下半年供应更紧\n\n最近某外资投行出了份MCU研报，信息量不小，直接划重点👇\n\n1️⃣ **现货价6月走平，但涨价马上来**\n- 意法半导体32位MCU现货价12.8元，GD 8.5元，环比都没动\n- 但意法半导体刚通知客户：6月28日起新一轮涨价，今年第二次了（第一次3月宣布4月执行）\n\n2️⃣ **供应紧张会贯穿下半年**\n- 成熟制程代工厂把更多产能挪给了AI电源相关应用\n- 新增产能又有限，MCU设计公司拿到的晶圆只会更紧\n\n3️⃣ **需求端没啥惊喜**\n- 分销商因为库存低+怕下半年继续涨，补货意愿强\n- 但终端消费和工业需求跟5月差不多，没看到明显回暖\n\n4️⃣ **下半年现货价会再涨，但原因变了**\n- 核心驱动不是需求，而是供应紧张+代工成本上升\n- 研报更看好大厂（如GD）和WiFi MCU厂商（如乐鑫），因为它们在边缘AI有长期机会\n- 对新唐保持谨慎，等毛利率恢复再说\n\n🧠 简单说：MCU涨价不是因为大家买得多，而是产能被AI抢走了，成本也压不住。这波涨价能持续多久，关键看终端需求能不能跟上。\n\n[... middle omitted ...]\n\nrs allocate more capacity to AI power-related applications and bring limited new capacity online, we expect supply to remain tight for MCU design houses.\n\n\\- End-market demand largely the same\n\n[... middle omitted ...]\n\nCo Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R028",
    "title": "DB：美国高收益债市场真正的风险不是衰退，而是分层",
    "digest": "[wechat_article.md]\n# DB：美国高收益债市场真正的风险不是衰退，而是分层\n\n2026年过半，美国高收益债市场正在经历一场“安静的洗牌”。DB在最新发布的《2026年中检查》报告中给出一个核心判断：美国经济衰退概率仍然很低，但市场内部的“分散度”正在快速上升——这意味着，过去两年“买一篮子高收益债就能赚钱”的简单策略，正在失效。\n\n这份报告的价值不在于它预测了宏观方向，而在于它拆解了“低衰退概率”之下，哪些行业、哪些资本结构、哪些信用层级正在积累真正的风险。对于持有高收益债敞口的机构投资者而言，现在需要回答的问题不是“要不要撤”，而是“应该怎样筛选”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 宏观没有崩，但增长引擎正在切换\n\nDB美国经济团队维持了对2026年实际GDP增长2.2%（Q4/Q4）的预测，仅比美伊冲突前的2.4%小幅下调。报告明确指出，拖累主要来自油价冲击（约-0.2个百分点）和年初消费走弱，但财政政策、金融条件、生产率和AI投资的持续强劲形成了对冲。\n\n这是一个“软着陆叙事”的延续。但真正值得注意的不是GDP数字本身，而是增长引擎的结构性变化。报告提到“劳动力市场信心正在修复”，通胀仍将“显著高于目标水平”，这意味着美联储不会很快转向宽松。\n\n> **KC评论：** 对于高收益债投资者，低衰退假设是定价的“底层操作系统”。只要这个假设不破裂，信用利差就不会系统性走阔。但DB提醒：利差不扩，不等于所有债券都安全。关键在于，谁能在增长引擎切换中保持现金流。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 技术面仍然强劲，但这恰恰是最大的“温水煮青蛙”信号\n\n报告在策略展望部分指出，“技术面仍然强劲，这可以缓和HY利差的走阔幅度”。换句话说，资金仍在流入高收益债市场，供需关\n\n[... middle omitted ...]\n\n欢迎来知识星球微信群中继续讨论，一起拆解这些报告的深层含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国高收益债年中盘点：分化正在加大\n\n📊 信用市场正在变局\n\n**1. 宏观底色：温和但分化**\n\n某外资投行最新研报更新了2026年中展望。核心判断：美国衰退概率依然偏低，但油价的拖累与财政/金融条件的支撑在角力。通胀预计全年仍高于目标，劳动力市场则趋于稳定。\n\n**2. 策略核心：灵活应对，关注分散化**\n\n研报认为，下半年技术面依然强劲，能在一定程度上缓冲高收益债利差的走阔。但关键信号是——市场分散化正在加剧。不同行业、不同评级的信用表现将明显分化，不再是普涨格局。\n\n**3. 行业亮点与风险点**\n\n- **消费与零售**：整体谨慎，但个股有亮点（如Crocs、Dave & Buster's被分析师列为高确信标的）\n- **医疗健康**：仍在调整期，Community Health Systems被列为重点关注\n- **工业/建筑**：住宅与非住宅需求分化，Bristow、Whirlpool等各有看点\n- **媒体/商业服务**：Gray TV、iHeart Media等被列为买入评级\n- **租赁、汽车、金属**：Herc Rentals、EquipmentShare、Rivian等被提及\n\n**4\n\n[... middle omitted ...]\n\nove target 11\n- Risks to our outlook... 12\n- DB US Forecast Summary 13\n- Strategy Outlook 14\n- Nimble? More dispersion is coming 15\n- Technicals remain strong, which can moderate \\$HY spread w\n\n[... middle omitted ...]\n\ns of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.\n\nCopyright © 2026 DB AG"
  },
  {
    "id": "R029",
    "title": "GS：中国财政的真实支撑力，不在5月的数据里",
    "digest": "[wechat_article.md]\n# GS：中国财政的真实支撑力，不在5月的数据里\n\n当大多数市场参与者还在盯着5月出口数据寻找经济韧性时，一份来自GS的研报揭示了一个更值得关注的结构性变化：中国财政政策的实际支持力度，在二季度出现了明显收紧。\n\n这不是简单的月度波动。GS构建的“广义财政赤字”指标，在5月继续收窄。无论是3个月移动平均还是12个月移动平均，这条曲线都在告诉市场一个反直觉的事实：尽管中央和地方政府仍有大量未使用债券额度，但财政政策对增长的支撑力度，在二季度反而弱于一季度。\n\n对于关注中国资产定价的投资者而言，理解这个“赤字缺口”的走向，比预测单月基建投资增速重要得多。因为它直接关系到下半年经济增长的底层驱动力——究竟是靠财政主动发力，还是被动等待经济内生修复。\n\n这份报告的核心判断可以浓缩为一句话：**中国财政不缺资金，但缺的是“把钱花出去”的速度和方向。**\n\n> **KC评论：** GS这个“广义财政赤字”指标，是把一般公共预算、政府性基金预算、以及政策性银行等准财政渠道全部算进去后的综合赤字率。它比单看财政收支差额更能反映真实的财政脉冲。5月这个指标进一步收窄，意味着财政对经济的净注入在减少，这不是流动性问题，是执行节奏问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 财政收入依然坚挺，但结构变化暗示了企业利润的隐忧\n\n5月一般公共预算收入同比增长6.6%，与4月的6.7%基本持平。表面看，数据不差。但拆开看，支撑力来自非税收入的高速增长，而非税收收入的稳健。\n\n税收收入增速从4月的8.2%回落至5月的6.8%，而非税收入则从-5.3%大幅反弹至+5.6%。这种“税收放缓、非税补位”的组合，通常意味着经济内生增长动能在边际减弱——企业利润增长放缓，直接拖累了企业所得税和个税的税基。\n\n更值得关注的是，主要税种在4-5月间\n\n[... middle omitted ...]\n\n市场动态。欢迎加入我们的社群微信群，继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n财政宽松度在收窄，Q2靠什么撑？\n\n**财政脉冲转弱**\n\n5月广义财政赤字率收窄，政策支撑力度在降\n\n最近看了份某外资投行的中国财政追踪报告，几个关键信号值得留意👇\n\n**1/ 收入端：税收增长放缓，非税收入补位**\n5月一般公共预算收入同比+6.6%，与4月基本持平。但结构变了——税收增速从8.2%降到6.8%，非税收入因低基数从-5.3%反弹到+5.6%。个税、企业所得税、消费税增速全面放缓。\n\n**2/ 支出端：基建支出依然疲弱**\n5月一般公共预算支出同比-1.6%，比4月的-3.2%有所改善。但基建相关支出同比-12%，拖累基建投资增速从-5.6%进一步降到-11.2%。科技、城乡社区、节能环保支出增速较快。\n\n**3/ 土地财政继续承压**\n5月土地出让收入同比-35.8%，比4月的-34.9%进一步恶化。房产相关税收增速也转负到-2.6%。两项合计，政府来自房地产的直接收入同比-23.9%。虽然部分城市住宅交易有回暖迹象，但土地收入预计持续下滑。\n\n**4/ 广义财政赤字率收窄**\n投行自建的“广义财政赤字”指标（含预算内+政府性基金+准财政渠道）在5月进一步收窄。3个月移动平均从-9.5%缩\n\n[... middle omitted ...]\n\n and off-budget financing channels, our proprietary “augmented fiscal deficit” (AFD) metric tightened further in May on both a 3-month and 12-month moving average basis, suggesting fiscal poli\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R030",
    "title": "NOM：人民币中间价模型释放的意外信号，比点位本身更重要",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型释放的意外信号，比点位本身更重要\n\n6.7851。这是NOM最新一期USD/CNY中间价模型给出的预测数字。相比上一期的6.8150，模型调降了299个基点。而计入逆周期因子后，预测值为6.8008，也比前次低了142个基点。\n\n在人民币汇率讨论几乎被地缘政治叙事和外部冲击主导的时刻，NOM这一模型更新显得格外冷静，甚至有些反直觉。当市场情绪普遍偏弱时，模型输出的信号却是：中间价的隐含方向在走强。\n\n这不是一个简单的点位预测。这背后是NOM亚洲外汇策略团队对定价机制、政策意图和市场结构三者关系的系统性拆解。理解这个模型，比知道那个数字更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测方向与市场情绪出现明显裂口，这本身就是一个信号\n\nNOM这份报告的核心价值不在于6.7851这个数字是否准确，而在于它揭示了一个正在发生的结构性背离：模型计算的“无逆周期因子”中间价，正在与市场交易的现货价格之间拉开一个显著的偏差。\n\n报告中的模型误差图（Fig. 2）记录了近期无逆周期因子调整的模型预测与实际中间价的偏离轨迹。这些误差不是随机波动，而是呈现出某种方向性的聚集。当模型持续预测一个比实际更强的中间价，而实际中间价却迟迟没有跟上时，意味着什么？\n\n有两种可能。一是市场正在消化尚未被模型完全捕捉的外部冲击预期。二是政策层面正在通过逆周期因子或其他工具，主动延缓中间价的调整节奏，为市场提供缓冲期。\n\n无论哪一种，都指向同一个结论：当前人民币汇率的定价，正处于一个“模型逻辑”与“政策逻辑”相互拉扯的阶段。这种拉扯本身就是最值得跟踪的信号。\n\n> **KC评论：** 不要去猜6.7851会不会成为明天的中间价。更重要的问题是：为什么模型认为应该更强，而实际却更弱？这中间的差值，就是政策意图\n\n[... middle omitted ...]\n\n继续讨论。\n\n欢迎加入，一起追踪人民币定价博弈的下一步走向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，到底怎么算的？\n\n**藏在模型里的汇率密码**\n\n某外资投行刚更新了USD/CNY中间价预测模型，核心逻辑拆解如下👇\n\n**1/ 模型预测：6.7851**\n比上一期预测（6.8150）低了299个点，比上一交易日官方收盘价高了88个点。简单说，模型觉得中间价应该更偏向升值方向。\n\n**2/ 加入“逆周期因子”后：6.8008**\n比前一次中间价低了142个点。逆周期因子是央行调节工具，用来平滑市场波动，防止汇率大起大落。加了它之后，预测值比纯模型结果更保守。\n\n**3/ 模型怎么跑的？**\n- 权重最高的四个隔夜变量（图1）驱动了预测变动\n- 近期模型误差在缩小（图2），说明模型拟合度不错\n- 每日中间价变动趋势（图3）显示近期波动趋缓\n\n**4/ 下半年关键事件日历**\n- 7月底：政治局经济工作会议\n- 10月国庆黄金周\n- 11月：深圳APEC峰会\n- 12月：中央经济工作会议+政治局会议\n- 年底：习主席访美\n\n这些事件都会影响汇率预期，尤其是年底中美高层互动。\n\n**一点想法**\n模型预测和实际中间价经常有偏差，逆周期因子就是那个“调节阀”。想看懂汇率，不能只看数字，还要理解背后的政\n\n[... middle omitted ...]\n\nactor)  \n![](images/6ddc9f3b2b82246b9cd8324db6c78c8a6fdafa51ac8d3ca2da91b1106ca4a69e.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/c\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R031",
    "title": "DB：欧洲资本品板块已从“战争输家”变为“和平赢家”",
    "digest": "[wechat_article.md]\n# DB：欧洲资本品板块已从“战争输家”变为“和平赢家”\n\n当市场还在消化伊朗战争停火带来的能源价格波动时，一份来自DB的研报提出了一个反直觉的判断：**那些在战争中跌幅最深的欧洲工业股，恰恰是当前风险回报比最优的标的。**\n\n这份发布于2026年6月22日的周报，核心信号清晰而直接——随着霍尔木兹海峡封锁解除、停火延长60天，欧洲资本品板块正从“通胀受害者”转向“复苏受益者”。报告并非简单看多整个板块，而是精准指向那些对工业生产最敏感、股价却仍低于战前水平的公司。\n\n为什么现在这个判断值得认真对待？因为市场正在经历一个典型的“后战争震荡期”：能源价格回落带来的通胀压力缓解，与企业投资信心恢复之间存在时间差。DB认为，这个时间差正是布局窗口。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 战争中最受伤的公司，现在拥有最大的反弹空间\n\nDB本周的核心图表，绘制了其覆盖范围内各公司有机销售增长与德国工业生产的关联度，对比自伊朗战争爆发以来的股价表现。\n\n结果非常直观：**那些短周期敞口最高的公司——KION、Knorr-Bremse和SKF——股价仍低于战前水平。** 而这三家公司恰恰是欧洲工业生产复苏最直接的受益者。\n\n这不是一个简单的均值回归故事。它的底层逻辑是：战争期间，能源价格飙升直接压制了工业企业的资本开支意愿。现在，随着“伊朗-美国谅解备忘录”签署，能源成本压力边际缓解，被压抑的资本开支需求有望释放。KION和Knorr-Bremse的核心业务——物流设备和制动系统——与制造业活动高度同步，一旦工业生产触底回升，它们的订单弹性最大。\n\n> **KC评论：** 这份报告最有价值的部分不是结论本身，而是它提供了一个可验证的分析框架——用“销售增长与工业生产的相关系数”来识别哪些公司对经济周期最敏感。\n\n[... middle omitted ...]\n\ncs。这些未解问题，正是我们每天在群里持续跟踪和讨论的内容。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n工业周期股，反弹窗口打开？\n\n**周期回归？**\n\n**地缘风险缓释，欧洲工业股或迎拐点**\n\n最近外资投行开始重新关注欧洲工业周期股。\n\n核心逻辑很简单：伊朗与美国签署谅解备忘录、霍尔木兹海峡封锁解除、停火延长60天——此前受战争冲击最严重的公司，现在可能反弹空间最大。\n\n欧洲对能源价格敏感，之前受伤最深。但通胀压力消退、企业投资信心恢复，与工业生产高度相关的资本品公司，有望率先反弹。\n\n**三个值得跟踪的标的：**\n\n1️⃣ **Knorr-Bremse**\n7月30日Q2业绩时将发布战略更新，包括新的中期目标。预计2029/2030年利润率目标16%+，比2026年指引高约2个百分点。\n\n2️⃣ **KION**\n目前估值接近历史低位，市场对其业务韧性的定价几乎为零。即便FY26 EBIT指引小幅下调，市场已消化，反而可能成为“利空出尽”的节点。研报认为风险回报比非常不对称：下行风险20%，上行潜力100%。\n\n3️⃣ **SKF**\n汽车业务分拆按计划推进，预计秋季完成，有望推动估值重估。\n\n**上周行业动态：**\n- 施耐德电气与富士康达成战略合作，联合交付AI数据中心集成方案\n- Wärtsilä\n\n[... middle omitted ...]\n\nds names most exposed to industrial production should be well placed for a rebound. This week's chart plots the correlation between organic sales growth and German industrial production across\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R032",
    "title": "DB：黄金不缺央行，缺的是ETF",
    "digest": "[wechat_article.md]\n# DB：黄金不缺央行，缺的是ETF\n\n黄金市场正在经历一场罕见的“三重背离”。价格从高位回落，但央行仍在买，ETF却在卖，而中国和印度的实物需求也同时转弱。DB最新发布的贵金属专题报告给出了一个判断：黄金当前最大的问题不是缺乏长期买家，而是短期投资需求出现了结构性断裂。这份报告将2026年Q4的黄金基准预测下调至4800美元/盎司，但更值得关注的不是这个数字本身，而是报告揭示的黄金定价逻辑正在发生根本性切换——从地缘政治溢价转向货币政策定价。\n\n如果你还停留在“黄金就是避险”的简单框架里，你可能已经错过了最重要的信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 黄金与原油的脱钩，暴露了真正的定价锚已经切换\n\n今年3月至4月，黄金与原油价格高度负相关，市场普遍认为这是地缘政治溢价在主导金价。但5月中旬之后，这个关系彻底断裂了。DB的分析师指出，黄金开始与美联储加息预期紧密挂钩，而原油价格的下行反而被市场忽略。\n\n这意味着什么？黄金已经从“战争避险”模式切换到了“货币政策定价”模式。美联储主席Warsh在6月FOMC会议上的鹰派表态——强调“我们已经在通胀目标上失守了五年，现在要纠正”——直接成为压制金价的核心力量。\n\n> **KC评论：** 许多投资者仍然习惯用“地缘风险”来理解黄金，但这份报告清楚地表明，黄金当前的主要矛盾是美联储的利率路径。如果你还在关注中东局势来判断金价，你可能需要重新校准你的分析框架。完整报告中有一张图清晰展示了黄金与Fed定价的回归关系，R2高达0.80，值得仔细研究。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. ETF清仓的速度，已经超过了央行买入的速度\n\n央行需求确实是黄金市场最坚实的支柱。Q1全球央行购金量创下历史新高，达到389\n\n[... middle omitted ...]\n\n便你人工快速把握全球市场动态。欢迎来星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n黄金的“鹰派”压力测试\n\n黄金何时能企稳？\n\n当前定价里，加息风险已被计入\n\n📌 黄金最近跌得有点多？核心原因是美联储政策预期转鹰，叠加美国经济数据持续韧性。这份研报的逻辑拆得清楚，我帮你理一下关键点。\n\n1️⃣ 黄金和原油“分手”了\n之前黄金跟着原油跌（地缘冲突缓和），但5月中旬后，两者关系脱钩。黄金开始更紧密地跟随美联储加息预期走。这是近期黄金下行的主因。\n\n2️⃣ 美联储“鹰派”主导，但内部有分歧\n- 鹰派：新主席Warsh明确表示“我们错过通胀目标太久了”，Taylor规则暗示利率应比当前高80bp。\n- 鸽派：市场通胀预期在下降（原油跌、通胀互换利率走低），且点阵图只显示一次加息后明年就反转。\n- 结论：黄金短期“数据依赖”，波动会很大。\n\n3️⃣ 投资需求“缺席”\n- ETF持续流出，期货持仓创17年新低，净多头靠近年内低点。\n- 中国黄金溢价转负，说明进口需求不再支撑。人民币走强+地产可能触底，削弱了黄金的避险吸引力。\n- 印度加征黄金进口增值税，需求也会被抑制。\n\n4️⃣ 央行购金是“定海神针”\n- 新兴市场央行黄金储备仍只有发达市场的一半，长期增持趋势不变。\n- 但Q1购金速度并未加速，单靠\n\n[... middle omitted ...]\n\nt, supported by a Taylor rule prescription some 80 bps higher. On the dovish side, our house call remains for an indefinite hold near neutral, market-based measures of inflation expectations a\n\n[... middle omitted ...]\n\nited Kingdom\nTel: (44) 20 7545 8000\n\nDB Securities Inc.\n\nThe DB Center\n1 Columbus Circle\nNew York, NY 10019\nTel: (1) 212 250 2500\n\nDB AG\nFiliale Singapur\nOne Raffles Quay, South Tower\nSingapore 048583\nTel: (65) 6423 8001"
  },
  {
    "id": "R033",
    "title": "GS：中国经济真正的风险不是增长放缓，而是AI替代就业的速度",
    "digest": "[wechat_article.md]\n# GS：中国经济真正的风险不是增长放缓，而是AI替代就业的速度\n\n理解中国当前的经济格局，最核心的一个判断是：出口和科技是唯一的亮点，而国内消费和房地产仍在收缩。GS最新发布的这份中国宏观报告，并不仅仅是对5月数据的常规复盘。它在做一件更重要的事——把短期数据波动与中国长期战略转型之间的张力，清晰地摆在了决策者和投资者面前。\n\n报告的核心主张是：中国正在全力押注科技驱动型经济转型，这个方向在工业生产、资本市场和政策信号中已经极其明确。但问题在于，如果AI对就业的替代速度过快，它可能会打断从“技术投入”到“收入增长”再到“内需扩张”这个理想循环。这不是一个遥远的担忧，而是当前已经可以观测到的结构性风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月数据揭示了一个前所未有的“双收缩”格局\n\n5月的经济数据，在出口和工业生产的亮眼表现之外，暴露了国内需求的深度疲软。GS的数据分析显示，5月零售销售同比下降0.6%，1-5月固定资产投资同比下降4.1%。在官方统计史上，零售销售和固定资产投资同时录得负增长，这是第二次——第一次是2020年疫情封锁期间。\n\n更直观的对比来自汽车行业。5月国内汽车销售同比下降22%，而汽车出口同比飙升75%。出口对GDP增长的贡献大约为3个百分点，这意味着国内需求的实际增速可能只有1-2%。这个数字比市场普遍感知的还要低。\n\n> **KC评论：** 这里的关键不是“数据不好”，而是“结构极度分化”。出口和科技制造撑住了总量的体面，但内需的收缩幅度已经接近疫情最严重时期。对于关注消费和地产板块的投资者来说，这组数据意味着，任何关于“内需触底”的判断都需要更谨慎的验证。\n\nGS据此将二季度实际GDP环比年化增速预测从4.0%下调至3.5%，但维持全年4.7%的预测不变。这背后的逻辑是，随\n\n[... middle omitted ...]\n\n科技板块估值有更深入的兴趣，欢迎加入我们的微信群继续讨论。*\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国5月经济数据出炉：出口一枝独秀，内需承压\n\n出口强，内需弱\n\n📊 5月经济数据解读来了，信息量很大，但逻辑很清楚。\n\n1/ **出口是唯一亮点**：5月出口同比增近20%（美元计），但零售和固投双双转负。这是2020年疫情以来第二次出现零售和固投同时负增长。\n\n2/ **内需实际增速仅1-2%**：出口贡献了约3个百分点的实际GDP增长，意味着国内需求增速非常缓慢。汽车数据最典型：国内销量跌22%，出口却涨75%。\n\n3/ **Q2增速下调，Q3有望反弹**：某外资投行将Q2实际GDP环比年化增速从4.0%下调至3.5%，但预计Q3将回升至5.0%。全年增速预测维持4.7%不变。\n\n4/ **科技与地产的“冰火两重天”**：工业机器人产量较2019年翻三倍，半导体翻倍，而玻璃、水泥等建材产出下降。A股科技板块涨超50%，消费板块跌超25%。\n\n5/ **AI投资的“中美差异”**：中国超大规模企业资本开支远低于美国，但数据中心装机容量已达美国的60%。原因有二：建设成本更低，且大量AI相关投资由政府主导。\n\n6/ **AI对就业的双刃剑**：历史经验显示，技术替代劳动力往往在经济下行期加速。如果AI大面积\n\n[... middle omitted ...]\n\ncal spending, and normalized weather conditions, we project Q3 real GDP growth to rebound to 5.0% qoq annualized (vs. 4.5% previously). Our full-year real GDP growth forecast remains unchanged\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R034",
    "title": "GS：美国供应链已“正常化”，但真正的考验才刚开始",
    "digest": "[wechat_article.md]\n# GS：美国供应链已“正常化”，但真正的考验才刚开始\n\n2026年6月的第三周，GS发布了一份看似平淡的供应链拥堵追踪报告。其核心结论是：**美国供应链拥堵指数连续第二周维持在“2”的水平，综合指数周环比下降6%。** 这个数字，已经非常接近2020年2月疫情前的基准线。\n\n对于习惯了过去几年“港口拥堵-运费暴涨-缺箱少柜”叙事的人来说，这个信号值得认真对待。它意味着，后疫情时代的供应链危机，至少在物理物流层面，已经基本结束。但GS报告真正有价值的洞察，并非“正常化”本身，而是**正常化之后，产业格局将如何重塑**。\n\n这份报告用大量高频数据，回答了一个关键问题：当潮水退去，谁在裸泳？而我们更关心的是：**当供应链不再是稀缺资源，企业的竞争逻辑将从“抢运力”转向“抢效率”，这轮变化真正考验的是什么？**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 拥堵指数回到疫情前，但不同环节的“解压”速度并不均匀\n\nGS构建的周度拥堵指数，是其分析师团队基于14个高频和低频指标合成的。最新的读数显示，综合指数周环比下降6%，而月度平均得分在6月也稳定在2.0。这个水平，与2021年底至2022年初的峰值（10分）相比，已是天壤之别。\n\n但仔细拆解报告中的分项数据，会发现“正常化”的进程并不平坦。\n\n**西海岸港口的情况最为理想。** 等待靠泊的集装箱船数量连续多周维持在1艘，几乎可以忽略不计。而东海岸和墨西哥湾的积压船只，从上周的5艘下降到了3艘。GS分析师指出，东海岸的改善是本周指数下行的主要贡献因素之一。\n\n**铁路多式联运的增速则出现了分化。** 西海岸两大一级铁路公司（联合太平洋和BNSF）的周度联运量同比增速，从前一周的+16%放缓至+11%。这或许暗示，前期被压抑的补库需求正在逐步释放完毕，或者说，陆路运输的弹\n\n[... middle omitted ...]\n\n迎来我们的知识星球和微信群里继续讨论，一起拆解这些未解之谜。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国港口堵不堵？最新数据来了\n\n供应链堵点继续缓解\n\n某外资投行最新周度供应链拥堵指数显示，6月22日当周指数环比下降6%，拥堵程度评级维持在“2”的水平（满分10）。这个数字远低于2021年底的高峰期，基本回到疫情前的通畅水平。\n\n几个关键指标变化👇\n\n1️⃣ 集装箱船排队情况\n- 西海岸等待靠港的船数不变：1艘\n- 东海岸从5艘降到3艘，明显好转\n\n2️⃣ 铁路联运数据\n- 西海岸两大铁路公司联运量增速放缓：同比+11%（上周+16%）\n- 铁路停留时间小幅改善：UNP从19.7小时降到19.4小时\n\n3️⃣ 底盘周转效率\n- 20英尺集装箱底盘在街边停留时间：4.4天（上周4.7天）\n- 码头的底盘停留时间也多数下降\n\n4️⃣ 海运价格\n- 中国到美西的集装箱运价约$4,840/FEU\n- 同比降19%，环比持平\n\n5️⃣ 滞后月度指标（4月数据）\n- 圣佩德罗湾集装箱平均停留2.6天，与3月持平\n- 铁路集装箱停留5.1天，比3月的4.4天略升，但远低于2022年高峰的16天\n- 中国到美国门到门运输时间约47天，接近疫情前平均水平\n\n整体来看，全球供应链压力持续缓解，关税和地缘政治对需求的影响仍是未\n\n[... middle omitted ...]\n\nw; Exhibit 2). For this week’s scale and index, the number of container ships waiting to dock and unload goods along the West Coast remained unchanged at 1, while backlogs along the East Coast\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R035",
    "title": "JPM：中东停火最大的受益者，可能不是中东",
    "digest": "[wechat_article.md]\n# JPM：中东停火最大的受益者，可能不是中东\n\n这份JPM最新发布的亚洲前沿市场周报，看似在讨论巴基斯坦预算与央行利率决议，但真正值得关注的判断藏在标题里——“和平红利正在路上”。报告的核心主张是：如果中东停火能够维持并导向持久稳定，亚洲前沿经济体将是全球能源冲击中最被低估的受益方。这不是一个关于地缘政治的判断，而是一个关于贸易平衡、通胀路径与央行政策空间的结构性推演。\n\n巴基斯坦、斯里兰卡、越南——这些在能源价格飙升中承受最大压力的经济体，正站在一个关键拐点上。而JPM的分析框架，为我们提供了一个观察“和平红利”如何从宏观假设传导至具体资产定价的完整链条。\n\n> **KC评论：** 这份报告的价值不在于它预测了油价会跌到多少，而在于它画出了一张传导地图——从地缘事件到贸易赤字，再到通胀预期，最后落到央行政策利率。完整报告里还有详细的表格拆解巴基斯坦的融资结构，以及斯里兰卡GDP分项数据，这些细节是理解“传导是否通畅”的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 亚洲前沿经济体才是能源冲击中真正的“受伤者”\n\n理解这份报告的前提，是重新认识亚洲前沿经济体在全球能源格局中的位置。JPM明确指出，这些经济体是“对全球能源冲击暴露度最高的地区之一”。不是中东，不是欧洲，而是巴基斯坦、斯里兰卡、越南——这些国家在油价飙升期间承受了贸易条件恶化和通胀输入的双重打击。\n\n报告提供了一个关键观察维度：贸易平衡。在今年3月至5月期间，除蒙古之外的所有亚洲前沿经济体都经历了贸易平衡的显著恶化。蒙古之所以成为例外，是因为它本身是资源出口国，从大宗商品价格上涨中获得了意外收益。这种分化本身就说明了问题——同样是亚洲前沿，资源禀赋的差异决定了暴露度的不同。\n\n> **KC评论：** JPM在图1中展示了贸易平衡的季节调整数据\n\n[... middle omitted ...]\n\n基于完整的研报原文，拆解每一个关键假设，追问每一个未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东停火，亚洲经济迎来转机\n\n**能源红利兑现中**\n\n中东停火若持续，亚洲边缘经济体将迎来实质性利好。这些国家此前受全球能源冲击最大，如今油价回落、供给逐步正常化，增长压力明显缓解。\n\n**1/ 贸易账改善**\n除了蒙古，其他亚洲边缘经济体的贸易平衡都在恶化。随着油价稳定在80美元/桶附近，巴基斯坦的经常账户赤字有望从GDP的1%收窄约0.5个百分点。\n\n**2/ 通胀压力缓解**\n巴基斯坦、斯里兰卡、越南的通胀将开始回落。若油价维持在80美元，巴基斯坦的通胀峰值可能从14%降至12%左右，斯里兰卡和越南的峰值通胀也可降低约1个百分点。\n\n**3/ 政策空间打开**\n能源价格下降让央行更有信心认为通胀冲击是暂时的。巴基斯坦央行在停火后立即维持利率不变，就是例证。\n\n**巴基斯坦预算：窄路难行**\n预算案承诺维持IMF计划下的2%基本盈余目标，但税收目标实现难度大——FBR收入连续低于目标，而减税措施又削弱税基。政府只能靠削减省级和资本支出来达标，这种模式难以持续。\n\n**央行抉择：加息还是观望**\n巴基斯坦央行6月维持利率在11.5%，但通胀已从3月的7.3%升至5月的11.7%。若油价维持当前水平，通胀可\n\n[... middle omitted ...]\n\ng and hydrocarbon supply gradually normalizing, pressures on growth from supply constraints and energy-conservation measures should fade. Trade balances, which had deteriorated everywhere outs\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R036",
    "title": "摩根斯坦利：亚洲市场正在出现三个不可忽视的结构性机会",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：亚洲市场正在出现三个不可忽视的结构性机会\n\n当市场还在为宏观不确定性争论不休时，摩根斯坦利的最新一期“Three Actionable Ideas”给出了一个清晰的信号：亚洲市场内部的结构性分化正在加速，真正的超额收益机会来自那些能够抓住AI基础设施、利率正常化和能源转型三重浪潮的公司。\n\n这份报告的核心判断是：亚洲市场的投资逻辑正在从“宏观博弈”转向“微观验证”。那些能够证明自己受益于AI资本开支、利率上升周期和政策驱动型能源投资的公司，正在获得明显的估值溢价。而市场对某些公司的回调反应过度，恰恰创造了重新入场的机会。\n\n报告精选了三只标的：村田制作所、三井住友金融集团和斗山能源。但这三只股票背后，其实代表了亚洲市场正在发生的三个趋势性变化。\n\n> **KC评论：** 摩根斯坦利这个“Three Actionable Ideas”系列的历史表现值得关注。截至2026年6月16日，累计相对超额收益达到8955个基点，平均持有期总回报4.3%，相对基准的12个月平均回报为11.5%。这不是一个随意的选股组合，而是一个经过长期验证的、基于基本面研究的信号系统。对读者来说，理解这三只股票背后的逻辑，比记住股票代码重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI基础设施的需求正在从“芯片”向“被动元件”传导，村田制造是最大受益者\n\n市场对AI的关注长期集中在GPU和服务器层面，但摩根斯坦利指出，下一个需求爆发的环节可能是高附加值MLCC（多层陶瓷电容）。报告预计，AI和数据中心应用对高附加值MLCC的需求年复合增长率将接近100%。\n\n这是一个典型的“二阶效应”投资逻辑。AI服务器的功耗和信号处理复杂度远超传统服务器，对高端电容的需求量是普通服务器的数倍。村田制造作为全球MLCC龙头，拥有最\n\n[... middle omitted ...]\n\n里继续讨论，我们会持续跟踪这三只标的的关键催化剂和风险变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI和银行股的逻辑，这篇讲得清楚\n\n三个方向值得看\n\n最近某外资投行更新了三个值得关注的方向，逻辑很直给👇\n\n1️⃣ **MLCC需求增速惊人**\n- 高端MLCC在AI和数据中心场景，未来3年需求复合增速预计约100%\n- 某日本电子元件公司被上调为Top Pick，受益于量价齐升\n\n2️⃣ **日本银行股有催化**\n- 终端利率预期走高 + 企业盈利韧性，银行盈利预期持续改善\n- 潜在盈利上修和更强的股东回报，是接下来可能的催化剂\n\n3️⃣ **核电/SMR题材值得再关注**\n- 某韩国能源公司近期回调，研报认为只是催化剂真空期，不是逻辑破坏\n- 下半年核能/小型模块化反应堆的催化事件更清晰，值得重新看\n\n📌 三个方向分别对应电子元件、金融、能源，覆盖不同周期逻辑，适合做组合参考。\n\n欢迎一起讨论你对哪个方向更感兴趣～\n\n#学习笔记\n\n[source_mineru.md]\nJune 21, 2026 10:00 PM GMT\n\nAsia | Asia Pacific\n\n## Three Actionable Ideas\n\nMurata Manufacturing – OW | Sumitomo Mitsu\n\n[... middle omitted ...]\n\n and stronger shareholder returns should serve as catalysts.\n\nOW – Doosan Enerbility (034020.KS): The recent pullback looks more like a catalyst vacuum than a thesis break. With a more visible\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R037",
    "title": "Citi：锂价暴跌的真正信号不是供给，是市场对“重启”的定价方式变了",
    "digest": "[wechat_article.md]\n# Citi：锂价暴跌的真正信号不是供给，是市场对“重启”的定价方式变了\n\n这份Citi研报发布的时间点，恰好卡在一个微妙窗口：市场刚刚消化了江西某重要锂矿（JXW）初步场地评估获批的消息，锂盐现货价格随即急转直下。但如果你只把注意力放在“复产时间表”上，可能就错过了这份报告真正想传达的结构性判断。\n\nCiti的核心结论是：锂的供需基本面在2026年三季度前仍然偏紧，但市场已经开始提前交易一个更复杂的逻辑——不是复产本身，而是市场对复产预期的反应机制已经发生了不可逆的改变。\n\n为什么这份报告值得认真看？因为它同时触及了三个层面：短期库存数据的真实状态、中期供给释放的节奏博弈，以及长期市场定价权从供给端向需求端的转移。而这三个层面，恰好指向同一个问题：锂价的下一个锚点在哪里？\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 库存数据出现了一个容易被忽略的拐点，但市场选择了无视\n\n先看Citi给出的最硬的数据：截至6月18日当周，中国碳酸锂总库存为96,645吨，环比下降1,184吨，降幅约1.2%。其中冶炼厂库存下降7%至15,373吨，下游正极材料厂商库存持平，贸易商和电池厂库存也基本持平。\n\n这个库存下降值得注意。Citi在报告中特别指出，这是库存连续几周横盘后首次出现周度环比下降。更关键的是，冶炼厂库存的下降幅度明显大于下游，说明上游正在主动去库存，而不是需求端在主动补库。\n\n但市场的反应是什么呢？锂盐现货价格在当周基本持平，碳酸锂和氢氧化锂报价分别为16.725万元/吨和15.25万元/吨，周环比几乎无变动。也就是说，库存下降这个利多信号，被市场完全忽略了。\n\n> **KC评论：** 库存下降但价格不涨，这在商品市场里通常意味着“市场认为这个库存下降不可持续”或“市场在等待一个更大的利空”。Citi\n\n[... middle omitted ...]\n\n品市场有持续跟踪的需求，欢迎来我们的星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n锂矿复产预期突袭，供需博弈加剧\n\n供需博弈，锂价承压\n\n上周投行研报更新了锂矿板块的观察，核心关注点集中在JXW复产的潜在影响。\n\n1/ 市场开始定价JXW复产\n初步场地评估已获批，市场迅速反应，今早锂现货均价明显走弱。研报指出，采矿环节可能在8月或10月恢复，选矿环节可能延后，锂云母矿或外包加工。尽管复产预期带来压力，但研报仍认为，考虑到3Q26大量新电池产能计划投产，锂供需格局可能持续偏紧。\n\n2/ 上周数据：产量持平，库存微降\n- 锂盐均价周环比基本持平，截至6月18日，碳酸锂16.73万元/吨，氢氧化锂15.25万元/吨。\n- 碳酸锂周产量2.64万吨，环比持平。盐湖提锂产量环比-1%，锂云母+1%，锂辉石和回收持平。\n- 总库存9.66万吨，周环比-1%（-1184吨）。其中下游库存持平，冶炼厂库存-7%，其他环节库存持平。\n\n3/ 关键变量：复产时间与节奏\n目前JXW复产的精确用途（采矿或选矿）、剩余流程和时间表尚未确认。市场对复产的预期已部分反映在价格中，但实际落地节奏和加工能力的外包安排，仍是影响后续供需平衡的关键。\n\n锂矿的复产预期与下游电池产能扩张之间，正在形成新的博弈点。你怎么看后续供需\n\n[... middle omitted ...]\n\no be postponed, and the lepidolite mines could be outsourced to a third party for mineral processing and conversion afterwards. We see looming concern on JXW resumption, but we still expect li\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R038",
    "title": "Citi：2026年618是16年来最低调的一届，但真正的信号藏在品类结构里",
    "digest": "[wechat_article.md]\n# Citi：2026年618是16年来最低调的一届，但真正的信号藏在品类结构里\n\n2026年的618购物节，在一种近乎静默的氛围中结束了。各大平台不再高调发布战报，GMV增速仅为3.2%，创下16年来的最低调记录。Citi在最新研报中给出了一个清晰的判断：这不是一次简单的“消费降级”，而是消费者行为正在从“价格驱动”转向“场景驱动”的结构性转变。\n\n这份报告最值得关注的信息，不是GMV增速本身，而是品类分化的背后，哪些平台正在失去议价权，哪些品类正在成为新的增长锚点。对于关注中国互联网和消费资产的投资者来说，理解这种结构性变化，比关注短期GMV数字更有意义。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 3.2%的增速背后，是平台从“补贴战”转向“品牌战”的集体默契\n\nCiti研报指出，2026年618期间，阿里巴巴显著削减了在“淘宝闪购”上的补贴投入，转而将资源投向剧集品牌广告和明星代言。京东则通过服务类目（家政、育儿、家电安装）拉动用户增长。抖音虽然保持了直播GMV翻倍，但更多依赖长尾主播和消费券，而非平台大额补贴。\n\n这种“默契”并非偶然。过去几年，电商平台在618和双11期间的补贴战，边际效用已经递减到几乎为零。消费者对“满减”“红包”的敏感度下降，平台则面临毛利率持续承压的困境。2026年的618，更像是行业集体完成了一次成本结构的优化。\n\n> **KC评论：** 平台不再烧钱换GMV，意味着利润表的修复可能比市场预期的更快。但代价是，增速数据会变得更难看。对于投资者来说，这反而是一个更健康的信号——行业从“跑马圈地”进入“精细化运营”阶段。完整报告里Citi对各家平台利润率趋势的拆解，值得细读。\n\n---\n\n![研报原图 2](assets/source_image_02.jpg)\n\n##\n\n[... middle omitted ...]\n\n市场动态。欢迎来星球微信群里继续讨论，一起拆解这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026 6.18，史上最安静的一次大促\n\n**最安静的 618**\n\n**16年最低调的一次购物节**\n\n今年 618 静悄悄结束了。不是大家不买，而是宏观环境温和，消费者花钱更精打细算。投行研报直接用“过去16年最低调的一次”来形容。\n\n复旦消费市场大数据实验室估算，2026年618全网线上GMV同比只增长了3.2%，增速和去年差不多。两大主力——淘宝天猫+京东，合计占了约60%的份额，抖音20%，拼多多7%。\n\n**1/ 阿里：从补贴战到品牌广告战**\n\n去年618主推“淘宝山购”补贴，今年阿里大幅收缩补贴，转而投钱在热播剧做品牌广告（《家族》《第一茉莉》《展昭》等）。明星策略也变了——不直接请代言，而是让合作品牌自己出明星做背书。\n\n品类表现上，3C类里鼠标键盘增长不错，但智能手表、充电宝增长平平。家居家纺和户外品类（床垫、自行车、跑步机）在6月第二周出现了环比下滑，只有智能开关是少数正增长的品类。\n\n**2/ 京东：用户数创新高，服务类爆发**\n\n京东宣布618期间交易用户数创历史新高，增长主要来自服务类——家政、育儿、家电安装。直播用户观看时长翻倍。\n\n品类亮点：\n- 3C：AI相关电子产品GMV\n\n[... middle omitted ...]\n\n in online GMV for 2026 6.18 festival with Taobao and JD captured \\~60% of total shares. As we are waiting for Syntun forecast release, we reconcile 2026 likely be the most low-profile/quiet 6\n\n[... middle omitted ...]\n\nk to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party."
  },
  {
    "id": "R039",
    "title": "GS：白酒端午动销恢复，但分化才是真正的胜负手",
    "digest": "[wechat_article.md]\n# GS：白酒端午动销恢复，但分化才是真正的胜负手\n\n这份GS在端午后发布的渠道追踪报告，给出了一个看似矛盾、实则清晰的判断：白酒行业正在走出最糟糕的时刻，但复苏的红利几乎全部流向了超高端和少数区域强势单品。中高端、次高端品牌，尤其是那些依赖商务宴请场景的，依然承压。这轮复苏不是普涨，而是一次结构性的出清与集中。\n\n报告的核心价值不在于“动销同比改善”这个事实——这几乎是共识——而在于它精确刻画了改善的分布、驱动力以及背后尚未解决的结构性问题。对于投资者和产业决策者而言，理解这种“有温度的复苏”的边界，远比知道一个总量数字更重要。\n\n以下是基于这份报告的深度解读与延伸思考。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 总量改善背后的“温差”：超高端两位数增长，中高端仍在失血\n\n端午小长假期间，茅台和五粮液的终端动销实现了10%至20%以上的同比增长，预收款比例也维持在健康水平。这直接印证了高端送礼和自饮需求的韧性。但与此同时，泸州老窖在河南等核心市场动销“显著下降”，洋河二季度动销“略有下滑”，渠道库存压力并未实质性缓解。\n\n这份报告揭示了一个关键事实：白酒消费的“K型分化”正在加剧。超高端品牌凭借品牌势能和刚需场景（送礼、高端宴请）率先反弹，而300至800元价格带的产品，尤其是那些依赖商务宴请和团购渠道的品牌，依然在消化过去几年过度铺货的苦果。\n\n> **KC评论：** 这意味着，对于持有或关注白酒股的投资者，不能再用“行业整体回暖”的框架来估值。茅台、五粮液的动销数据，并不能线性外推至整个板块。真正需要关注的是，哪些品牌在库存去化后，依然能维持价格体系和渠道利润。这份报告中的渠道检查表格，详细列出了各品牌的库存月数和批发价走势，是判断这一点的关键素材。完整报告中有更细分的区域数据，值得仔细拆解。\n\n![研\n\n[... middle omitted ...]\n\n析。我们会在社群中持续跟踪白酒行业的库存去化进程与价格演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午白酒动销：高端回暖，大众分化\n\n高端回暖，大众承压\n\n端午白酒消费整体偏淡，但高端酒动销同比改善明显。投行研报显示，茅台/五粮液多数区域动销增长10-20%+，预收款进度60%+/55%-70%。而次高端及大众价位整体平淡，仅个别大单品（如今世缘的淡雅）表现突出。\n\n1. **高端韧性超预期**：飞天茅台批价虽小幅下调25元至1645元，但i茅台MAU仍超1000万，618期间飞天原箱GMV达3亿元。普五批价稳定在840元，电商增速超13倍。\n2. **次高端压力持续**：泸州老窖河南市场动销明显下滑，国窖1573批价持平。洋河/古井2季度动销小幅下降，渠道库存普遍3-4个月+。\n3. **区域分化加剧**：江苏科技产业带动商务需求环比改善，四川商务需求同比增10%+（但仍低于2024年30-40%）。安徽受政务活动约束，表现偏弱。\n4. **场景结构变化**：送礼仍为高端酒核心支撑，宴席场景偏弱。个人消费/餐饮驱动100-300元价位，商务需求恢复仍需时间。\n\n端午作为小旺季，今年动销整体同比微增，但远低于2024年水平。高端酒率先企稳，大众价位仍需观察中秋表现。\n\n欢迎一起讨论区域分化逻辑\n\n#学习笔\n\n[... middle omitted ...]\n\nr-premium category and selected regions, while the upper mid end segment remained under pressure. Our latest channel checks suggest Dragon Boat Festival sell-through improved slightly yoy but \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R040",
    "title": "GS：中国光伏需求2028年才会迎来真正拐点",
    "digest": "[wechat_article.md]\n# GS：中国光伏需求2028年才会迎来真正拐点\n\n市场对2026年中国光伏装机下滑已有预期，但多数投资者仍倾向于认为，这不过是行业周期中的一次短暂调整，2027年即可重回增长。GS最新发布的一份专家调研报告，给出了一个更为审慎的判断：中国光伏需求的真正拐点可能要到2028年才会到来。这意味着，产业链的盈利修复时间表将被推迟，而行业出清的过程将比市场普遍预期的更为漫长。\n\n这份报告的核心信号并非悲观，而是提供了一个更贴近产业现实的观察框架。它揭示了一个关键矛盾：当前市场对分布式光伏的韧性存在高估，而对电网消纳瓶颈的解决速度存在低估。真正的拐点，取决于政策、电网投资和电力需求三者能否在2028年前后形成合力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年装机下滑已成定局，分布式结构将出现显著分化\n\nGS专家预计，2026年中国光伏装机将同比下降26%至238GW左右，这一总量预测与GS此前给出的235GW基本吻合。但真正值得注意的，是装机结构内部的显著分化。\n\n公用事业规模项目（USS）预计下滑18%，至135GW，与GS此前预测基本一致。分布式工商业项目（DS-C&I）预计下滑48%，至55GW，显著低于GS此前预测的83GW。而分布式户用项目（DS-Resi）则展现出意外韧性，预计同比增长3%，至57GW，远超GS此前预测的14GW。\n\n这一分化背后，是不同细分市场商业模式的根本性转变。工商业项目正在从“余电上网”模式转向“自发自用+储能”模式。随着光伏配储的平准化度电成本（LCOE）降至0.65-0.7元/kWh，已低于多数地区的工商业峰值电价，经济性驱动了模式切换。但“直供电”项目因电网接入要求更复杂，建设周期显著拉长，这解释了近期的装机低于预期。户用市场的韧性，则源于融资成本下降后，部分运营商\n\n[... middle omitted ...]\n\ns。欢迎来星球微信群里继续讨论，一起跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国光伏需求拐点，预计在2028年\n\n光伏需求触底倒计时\n\n最近看了一份某外资投行的光伏专家访谈，核心结论是：2026-2027年中国光伏装机量会连续下降，但2028年开始，需求会迎来明显拐点。\n\n1/ 2026年装机量预计下降26%\n专家预测2026年总装机在210-245GW之间，与投行预测的235GW基本一致。分结构看：\n- 大型地面电站：135GW（下降18%）\n- 工商业分布式：55GW（下降48%）\n- 户用分布式：57GW（反而增长3%）\n\n户用分布式之所以坚挺，是因为在融资成本下降背景下，POE模式的内部收益率门槛降低，且东南沿海地区并网保障好、电价结构优。\n\n2/ 2027年继续下滑，但速度放缓\n地面电站新项目储备不足是主因。2026年前4个月，地面电站新开工量同比下降34%，而项目从开工到并网通常需要6-12个月，这直接拖累了2027年的装机量。\n\n3/ 2028年迎来需求拐点\n核心驱动因素是“弃光率改善”。2025年已有23个省份光伏利用小时数下降，西部地区尤其严重。但接下来有三个结构性支撑：\n① 政策端：清洁能源消费被纳入省级考核指标\n② 电网投资：2026-30年预计达5万亿，较20\n\n[... middle omitted ...]\n\ns are projected to decrease by $26\\%$ YoY in 2026, with a continued downward trend in 2027 (at a slower pace) due to a diminishing pipeline of new Utility Scale Solar (USS) projects; ii) Allev\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R041",
    "title": "摩根斯坦利：MS：中国AI芯片TAM上调36%，但真正的变量不在国内",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国AI芯片TAM上调36%，但真正的变量不在国内\n\n当美国商务部在6月初悄然收紧对中资海外子公司获取最先进AI芯片的管制时，大多数人的第一反应是“又一轮利空”。但MS最新发布的这份中国半导体本土化追踪报告，给出了一个反直觉的判断：这恰恰是中国AI GPU的“牛市情景”。\n\n报告将中国AI芯片可寻址市场（TAM）从670亿美元大幅上调至910亿美元，增幅36%，对应2025-2030年23%的年复合增长率。这个数字背后，核心驱动力并非国内需求的线性增长，而是一个此前未被纳入测算的新变量：中国云服务商的海外数据中心，将开始采用本土GPU。\n\n这不是一份简单的“国产替代”叙事。它揭示了一个正在发生的结构性转折：当海外供应通道被系统性收窄，中国AI基础设施的投资逻辑正从“被动替代”转向“主动扩张”。而后者，才是真正值得产业决策者和投资者重新审视的底层变化。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 最关键的增量来自海外：中国GPU的“出海”假设被首次纳入\n\n报告上调TAM的第一条理由，是新增了“中国CSP（云服务商）海外AI数据中心使用本土GPU”这一类别。MS的假设是：2028至2030年，中国云厂商海外资本开支中分别有3%、10%、20%将由本土芯片满足。\n\n这个假设的含金量在于它打破了两个固有认知。第一，此前市场普遍认为中国AI芯片只能在国内市场消化，海外需求几乎为零。第二，即便在短期，中国云厂商面临算力缺口时，首选方案仍是GPU租赁而非本地采购——这本身就意味着海外数据中心的需求真实存在，只是供应链尚未切换。\n\n> **KC评论：** MS把“海外采用”放进TAM模型，本质上是在押注一个闭环逻辑：美国管制越紧，中国云厂商在海外越难买到英伟达Blackwell，就越有动力在自己\n\n[... middle omitted ...]\n\n标的估值有进一步讨论的兴趣，欢迎来我们的星球微信群继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国AI芯片，迎来关键窗口\n\n91bn美金的想象空间\n\n2030年中国AI芯片TAM上调36%\n\n某外资投行刚发了一篇中国半导体本土化的跟踪报告，核心判断很清晰：**美国出口管制收紧，反而打开了国产AI GPU的新市场空间。**\n\n几个关键点拆开看👇\n\n1️⃣ **AI芯片TAM大幅上调**\n- 2030年中国AI芯片市场规模预测从670亿→910亿美金（+36%）\n- 新增了一个重要变量：**中国云厂商的海外数据中心**，预计2028年起开始采用国产GPU\n- 字节跳动2026-2027资本开支大幅加码（2027年可能到800亿人民币级别）\n- 金山云加入数据库，2026年资本开支预计超150亿\n- 国企/主权AI需求从70亿上调至90亿美金\n\n2️⃣ **2026年将是关键节点**\n- 国内CSP（云服务商）目前普遍算力短缺\n- 国产供应商进入采购体系的窗口正在加速打开\n- 竞争核心不再是单纯的芯片性能，而是**生态成熟度、软件优化、集群部署能力**\n- 先进制程产能是重要分水岭——能拿到台积电7nm/6nm的厂商有明显优势\n\n3️⃣ **国产化率目标：从42%到70%**\n- 2025年自给率42%，预\n\n[... middle omitted ...]\n\nlackwell processors – to subsidiaries of Chinese companies located outside China. We think that, in the short term, China CSPs may turn to more GPU rental to fulfill the strong computing deman\n\n[... middle omitted ...]\n\ny Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,460.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R042",
    "title": "NOM：中国医疗板块的“恐惧”与“灵感”，AI之外还有结构性机会",
    "digest": "[wechat_article.md]\n# NOM：中国医疗板块的“恐惧”与“灵感”，AI之外还有结构性机会\n\n当市场几乎将所有注意力都倾注于AI主题时，中国医疗板块正经历着一场由资金流出引发的情绪低谷。NOM在2025年6月15日至18日的半年度医疗产业调研中，与20家上市公司管理层进行了深入交流，其结论与当前市场悲观情绪形成了鲜明对比：基本面正在改善，但市场尚未定价。\n\n这份调研报告的核心判断是：中国医疗板块正处在一个“恐惧与灵感并存”的关键节点。恐惧来自国内反腐政策的持续深化、海外地缘政治对license-out的潜在封锁，以及医保基金监管的收紧；而灵感则来自于企业海外扩张的不可逆趋势、创新药销售的持续爬坡，以及CRO/CDMO领域强劲的产能扩张需求。报告认为，短期情绪波动无法掩盖长期结构性机会，而当前资金配置已接近历史低位，这本身就是一个值得关注的信号。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 资金持续流出AI主题，医疗板块配置已近历史冰点\n\n调研中一个反复出现的现象是，无论是南向资金还是国内机构投资者，都在持续从医疗板块撤出，转而涌入AI相关主题。多家H股上市公司管理层直言，南向投资者的减持是其股价下跌的直接原因之一。参与调研的国内投资者也承认，其医疗板块的整体仓位已接近历史最低水平。\n\n这一现象意味着什么？NOM分析师张佳琳团队认为，这并非基本面恶化所致，而是一种典型的“主题轮动”效应。当AI成为市场唯一的热点，资金集中度达到极端水平时，其他板块必然面临失血。但经验表明，当某一板块的配置比例降至历史冰点时，往往也意味着最悲观的预期已经充分定价，后续任何边际改善都可能引发估值修复。\n\n> **KC评论：** 这不是一个简单的“别人恐惧我贪婪”的口号。关键在于理解，当前医疗板块的估值压缩并非源于盈利下调，而是单纯的资金搬家。一旦AI主题出现阶段性\n\n[... middle omitted ...]\n\n动态变化。我们每天在星球微信群里继续讨论这些未解问题的进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n医疗AI热潮下的冷思考与真机会\n\n📌投研笔记｜带你看清当前医疗板块\n\n---\n\n最近跟了一个外资投行的医疗行业调研，20家上市公司聊了一圈，信息量很大。分享几个关键判断：\n\n**1/ 资金确实在跑，但基本面没崩**\n很多H股公司提到，南下资金持续撤出，板块仓位已接近历史低点。但奇怪的是，大部分公司对基本面反而偏乐观——创新药销售在爬坡，出海订单在增长，临床进展也顺利。股价弱和基本面强之间，出现了明显背离。\n\n**2/ 反腐影响没想象中大**\n5月起药品/器械销售监管确实收紧了，部分公司短期业务受到一些影响。但研报认为这波担忧大概率是短期的——头部公司收入主要来自创新药，本身就不是监管重点；而且2023年以来反腐常态化，行业已经有一定适应度。\n\n**3/ 出海逻辑没变，地缘扰动更多是情绪**\n关于中美摩擦影响分子出海，几乎所有参会公司都表示：和海外伙伴的日常交流依然繁忙，没有实质影响。CRO公司更是觉得地缘风险不是新鲜事。核心判断：短期摩擦会反复，但长期合作方向不变，只要中国企业保持效率优势。\n\n**4/ 各细分板块分化明显**\n- CRO：最坚挺，制造服务需求强劲，多家在扩产\n- 生物科技：ASCO会议数据不\n\n[... middle omitted ...]\n\n abroad recently. Starting with the domestic market. Stricter regulations on drugs/equipment sales (such as on sales reps visiting physicians or on offline pharmacies sales) were issued beginn\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R043",
    "title": "摩根斯坦利：MS：新药放量正在改写美国处方药市场的竞争规则",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：新药放量正在改写美国处方药市场的竞争规则\n\n美国处方药市场正在经历一场静水深流的格局重塑。在整体处方量增速放缓至1%左右的大背景下，少数新药正在以远超历史对标的速度撕开市场缺口，而另一些曾经的现象级产品则在生物类似药和竞争替代的双重挤压下加速失血。\n\nMS最新发布的美国药品市场追踪报告，以IQVIA处方数据为锚，揭示了这一结构性分化。报告的核心判断并非总量层面的惊喜或恐慌，而是一个更值得产业决策者关注的信号：新药放量的斜率，正在成为区分赢家与输家的关键分水岭。\n\n对于关注生物医药投资的读者来说，这份报告的价值不在于它复述了哪些药卖得好，而在于它用处方数据这条“硬线”，量化了市场共识预期与真实放量轨迹之间的差距。这些差距，恰恰是投资判断中最重要的变量。\n\n> **KC评论：** MS这份报告的核心价值在于“校准”。它不提供宏大叙事，而是用每周处方数据去检验市场共识的合理性。对于投资者而言，真正重要的不是知道某个药卖了多少，而是知道它目前的放量速度能否支撑华尔街的营收预期——如果不能，预期差本身就是机会或风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 整体市场增速已降至1%附近，但结构性分化远比总量数字更剧烈\n\n截至6月12日当周，美国全市场总处方量同比增速仅为0.6%，低于前一周的0.9%和过去12周滚动均值1.1%。4周滚动同比增速为1.0%，12周滚动为1.1%。这意味着美国处方药市场已经进入一个低增速的稳态区间。\n\n但总量数字掩盖了剧烈的结构性变化。在GLP-1赛道，诺和诺德和礼来的双头垄断格局依然稳固，但增速正在分化。诺和诺德的Ozempic和Wegovy周处方量分别稳定在51.8万和47.5万的水平，礼来的Mounjaro和Zepbound合计周处方量已接近157.7万。值得注\n\n[... middle omitted ...]\n\n来星球微信群里继续讨论，一起追踪这些新药放量曲线的真实走向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国药市开年：新药放量谁在跑？\n\n新药放量速度观察\n\n📊 美国处方药市场6月12日当周总量同比+0.6%，低于前几周增速。但几个新药的表现，值得拆开看。\n\n1️⃣ **Cobenfy（精神分裂症）**\n- 周处方量约3200张，环比小幅回落\n- 要达成2026年市场预期（约2.96亿美元），需达到此前同类新药放量速度的2-5倍\n- 目前走势还在早期验证阶段\n\n2️⃣ **Journavx（急性疼痛）**\n- 周处方约22430张，环比微增\n- 注意：医院端处方未被IQVIA完全覆盖（医院/零售约45%/55%）\n- 假设12天疗程、GTN在65-75%，要达成2026年预期约2.39亿美元，需总处方量120-210万张\n\n3️⃣ **Yeztugo（HIV预防）**\n- 周处方约1720张（含口服+注射），注射剂稳定在980张\n- 已覆盖95%支付方，多数不要求共付或事前授权\n- PrEP市场整体同比+14%，Descovy份额>45%，支撑2026年预期\n\n4️⃣ **Icotyde（银屑病）**\n- 周处方约480张，环比增长明显\n- 医生反馈：作为口服IL-23药物，有望扩大治疗人群，但早期取样可能影响\n\n[... middle omitted ...]\n\nt17 – Exhibit19 depict YoY momentum for key products.\n\nBMY's Cobenfy was approved for schizophrenia on 9/26/24. Scripts are \\~3,200 for the week vs \\~3,430 last week. For full details on our v\n\n[... middle omitted ...]\n\n Pharma Plc (RPRX.O)</td><td>O (05/16/2025)</td><td>$52.96</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R044",
    "title": "GS：韩国AI红利比预想更强更长，但红利并未普惠",
    "digest": "[wechat_article.md]\n# GS：韩国AI红利比预想更强更长，但红利并未普惠\n\n这份GS研报的核心判断是：韩国正在经历一轮由AI资本开支驱动的、比预期更强更持久的芯片上行周期，其外部账户和财政状况将因此创下历史性改善。但与此同时，一个更关键的结构性矛盾正在浮现——AI红利高度集中于半导体部门，其向国内消费、就业和工资的传导极为有限，导致韩国经济呈现出典型的“K型”分化。\n\n这份报告的真正价值不在于确认AI的强劲，而在于揭示一个被市场普遍低估的事实：韩国经济的“双速”格局正在固化，而政策制定者和投资者都必须据此重新校准自己的分析框架。GS因此上调了韩国2026年和2027年的GDP增长预测至2.7%和2.3%，均高于市场共识，同时将终端政策利率预测从3.0%上调至3.25%，并将加息周期延长至2027年。\n\n这些预测调整背后，隐藏着对韩国资产定价的深层含义。以下是我们从这份报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮AI驱动的“超级盈余”正在改变韩国的外部账户，但盈余并未转化为韩元升值\n\nGS报告中最引人注目的数字之一，是韩国经常账户盈余预期将超过GDP的15%，达到历史最高水平。2026年商品出口总额有望突破1万亿美元。这背后是AI资本开支对存储芯片需求的持续拉动，其强度和持续时间均超出了此前预期。\n\n然而，一个反直觉的现象正在发生：尽管经常账户盈余大幅改善，韩元却并未相应走强。GS的数据显示，2025年上半年几乎全部盈余都以创纪录的净海外股票投资流出的形式被“再循环”到了境外。这些流出主要来自机构投资者的再平衡需求和杠杆头寸。\n\n> **KC评论：** 这解释了为什么经常账户盈余改善与汇率贬值可以同时发生。对于持有韩元资产的投资者而言，关键问题不是盈余规模有多大，而是盈余是否“留在了国内”。GS认为\n\n[... middle omitted ...]\n\n们可以继续讨论这些未解问题，并共享原始报告的完整图表与数据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国AI红利比预期更久更强\n\n韩国经济：AI拉动超预期\n\n最近读了一份某外资投行的韩国研报，数据太有意思了。AI对韩国经济的拉动，比很多人想的更持久、更集中。\n\n1️⃣ AI出口狂飙，但经济出现“K型分化”\n半导体出口直奔万亿美金，但非科技行业几乎没沾到光。零售、消费依然疲软，就业增长全靠公共部门撑场子。\n\n2️⃣ 工资传导有限，通胀压力可控\n半导体公司发的奖金看似很多，但科技行业工资只占GDP的1.2%。非科技企业利润率普遍低于5%，很难跟着涨薪。核心通胀目前很稳，不像2022年那样全面上涨。\n\n3️⃣ 财政意外变好，韩元可能被低估\n半导体企业多缴的税可能让财政赤字从1.9%降到0.5%以下。韩元现在偏弱，但基本面其实在改善，政策层面也开始关注汇率稳定。\n\n4️⃣ 加息不会太快\n虽然首尔房价又涨了，但其他地方没跟。家庭债务负担重，国内需求也没完全恢复，央行大概率会慢慢来。\n\n整体看，韩国这波AI红利很真实，但受益面还比较窄，需要持续观察传导效果。\n\n大家觉得韩国经济这种“K型复苏”会持续多久？\n\n#学习笔记\n\n[source_mineru.md]\n# Korea Views: Korea—Riding St\n\n[... middle omitted ...]\n\ne inflation unchanged at 2.6% and 2.2%, under our updated base-case scenario for reopening of the Strait of Hormuz, and extend the hiking cycle into 2027 and lift our terminal policy-rate fore\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R045",
    "title": "摩根斯坦利：MS：中国经济的“K型”分裂正在固化，而不是修复",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国经济的“K型”分裂正在固化，而不是修复\n\n这份报告的核心判断，比标题“Beijing Will Fine-tune, Not Pivot”要锋利得多。MS首席中国经济学家邢自强及其团队在6月18日的投资者演示中，并没有停留在“政策不会转向”这一市场共识上。他们真正想说的是：中国经济的“双速”格局——出口强劲、内需疲软——不是暂时现象，而是一个正在自我强化的结构性分裂。而市场对下半年消费反弹的期待，可能忽略了几个正在收紧的约束条件。\n\n为什么现在重要？因为5月零售数据转负，已经不是一个基数效应可以解释的信号。报告明确指出，消费放缓“more than a base effect”。当出口和工业生产的韧性还在支撑宏观叙事时，内需的冷却正在从“预期中的放缓”滑向“超预期的收缩”。这意味着，投资者需要重新校准对中国资产定价的底层假设——尤其是那些押注消费复苏的仓位。\n\n以下是我们从这份研报中提炼出的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n> **KC评论：** 邢自强团队的报告通常以“不惊不乍、逻辑严密”著称。这次他们用一个“fine-tune”的标题，装下了一个“结构性分化正在加深”的硬核判断。对读者而言，关键不是记住结论，而是理解他们用来推导结论的那几个数据链条——尤其是消费、固定资产投资和贸易摩擦这三条线。完整报告里有更多细分图表和交叉验证，值得细读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口与内需的裂口在扩大，这不是周期波动，是结构分化\n\n报告用两张图直接对比了工业生产和零售销售的趋势。工业生产在出口和“新三样”的拉动下保持韧性，而零售销售——尤其是剔除汽车和石油后的核心零售——在5月出现了同比负增长。这不是一个短期的库存调整或天气扰动。\n\n更关键的是，报告指出这\n\n[... middle omitted ...]\n\n们试图做那个帮你“把报告读薄、把判断读透”的角色。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国经济：微调而非转向\n\n📌 政策逻辑在变，但方向没变\n\n某外资投行最新研报的核心判断：北京在“微调”而非“转向”。简单说，不是大水漫灌，而是结构性修补。\n\n**1/ 经济正在“两极化”**\n出口强劲，工业数据不错，但国内消费和需求在降温。5月零售数据转负，不完全是基数效应——就业市场偏弱，大家花钱更谨慎了。\n\n**2/ 消费压力被低估**\n去年“以旧换新”补贴拉高了基数，但实际也在放缓。油价冲击让消费者压缩非必要支出，比如燃油车使用和航空出行。K型复苏在加深：生产端好，消费端冷。\n\n**3/ 政策抓手在哪？**\n全年政府债券额度还有约60%没用完，准财政工具（8000亿）落地也慢。预计三季度开始加速执行，重点投向AI、能源转型等“六网”基建。方向很明确：不走老路，但要补短板。\n\n**4/ 贸易摩擦风险上升**\n中国贸易顺差持续扩大，欧盟可能加强防御性措施。外部压力在累积，这也是为什么政策需要更灵活。\n\n**5/ 美联储可能按兵不动**\n美国通胀回落速度慢于预期，年内降息概率不高。外部利率环境对国内政策空间也有影响。\n\n整体看，政策更强调“精准”而非“力度”，方向是修补结构性问题，不是全面刺激。\n\n欢迎一起讨\n\n[... middle omitted ...]\n\nrial production  \n![](images/c124996a46535820d08c8a880e58857110b7afa39208a2e4facc24915d16c00d.jpg)\n\nCooling domestic demand  \n![](images/b2e14ee7e474aefde7771b72a92006216d57cb68d78c8630c24884e\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R046",
    "title": "Bernstein：韩国电商的胜负手不在价格，而在“凑单成本”",
    "digest": "[wechat_article.md]\n# Bernstein：韩国电商的胜负手不在价格，而在“凑单成本”\n\n一份由Bernstein分析师以亲身采购酸奶和泡面为起点的研报，揭示了韩国在线杂货市场一个被投资者长期忽视的结构性事实：谁在消费者最终支付的“实际总成本”上胜出，谁才能赢得下一阶段的竞争。而价格最低的平台，未必是消费者最划算的选择。\n\n这份于2026年6月22日发布的报告，核心判断并非关于GMV增速或用户数，而是落在一个极其微观却具有颠覆性的洞察上——**Coupang在绝对价格上的领先，被其复杂的免运门槛和品类隔离所抵消；而Naver与Kurly凭借更友好的门槛机制，在真实购物场景中实现了更低的“有效总价”。**\n\n对于关注韩国电商格局的投资者而言，这不仅仅是一次购物体验的对比。它意味着，当市场普遍将Coupang视为“价格屠夫”时，其竞争优势可能正在被自身运营结构的摩擦力所侵蚀。而Naver在电商领域的价值，可能被市场严重低估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Coupang的绝对低价，被“15,000韩元门槛”与“品类隔离”双重削弱\n\n在Bernstein的模拟采购中，Coupang的Rocket Fresh在单品价格上确实最低。然而，问题出现在结算环节。Rocket Fresh的免费配送门槛是15,000韩元，且这一门槛基于的是折扣后的支付价格，而非商品标价。更关键的是，非Fresh品类的商品（如Rocket配送的拉面）无法计入这一门槛。\n\n这意味着，消费者为了凑单免运费，可能被迫购买更多Fresh品类商品，或者支付额外的配送费。这种“结构性的摩擦”在研报中被明确点出：Coupang在价格上获胜，但品类分割带来了实际可用性的显著限制。\n\n> **KC评论：** 这揭示了一个投资者容易忽略的“隐性成本”。Coupang的低价\n\n[... middle omitted ...]\n\n全球市场的动态。我们会在星球微信群里继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国电商实测：谁在真正赢你的购物车\n\n实测4家平台，谁最划算？\n\n买酸奶+拉面，4家韩国电商的真实对比\n\n前几天帮朋友在韩国线上买酸奶和BTS联名拉面，顺手做了个四平台实测。结果很有意思，价格最低的不一定最省心。\n\n1️⃣ Coupang：价格最低，但凑单很累\n- 酸奶和拉面分属不同品类，不能合并凑免运\n- 生鲜免运门槛1.5万韩元，按折后价算，比标价更难达标\n- 最后为了免运多买了东西，总花费反而上去了\n\n2️⃣ Naver Shopping+Kurly：门槛友好，隐藏优势\n- 免运按标价算，更容易达标\n- 达标后总价不输Coupang，Naver会员还有3%+返现\n- 结构更灵活，不用被迫凑单\n\n3️⃣ SSG.com：品类不够全\n- 想买的希腊酸奶品牌没有上架\n- 线上SKU比线下少，受制于线下店配送规则\n- 如果政策放开，这个缺口可能会缩小\n\n4️⃣ Baemin B-Mart：送得快但贵\n- 1-2小时送达，适合急用\n- 价格明显更高，品类也有限\n- 应急可以，日常买菜性价比不高\n\n研报核心判断：某外资投行看好Naver在电商的持续投入，认为其现金流能支撑长期竞争；对Coupang持谨慎态度，认为价\n\n[... middle omitted ...]\n\n ramen for a short stay in Korea - quickly evolved into a grounded comparison of four major grocery platforms: Coupang, Naver Shopping with Kurly, SSG.com, and Baemin B-Mart. This exercise hig\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R047",
    "title": "Bernstein：印度乙醇的尽头是E27，不是E85",
    "digest": "[wechat_article.md]\n# Bernstein：印度乙醇的尽头是E27，不是E85\n\n印度在2025年底提前五年达到E20乙醇掺混目标，这本应是一个值得庆祝的里程碑。但Bernstein最新发布的这份印度汽车行业深度报告，却给出了一个反直觉的判断：印度乙醇计划的“容易部分”已经结束，继续推进到E25甚至E27虽可行但难度陡增，而建设全国性的灵活燃料和E85供应链，则是一个回报有限、时机已过的昂贵对冲。\n\n这份报告的核心主张可以浓缩为一句话：印度乙醇的故事，在E20之后就不再是关于能源独立，而是关于如何在一个快速电气化的时代，为一个旧时代的解决方案找到合理的退出路径。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. E20的成功恰恰是建立在三个“免费”条件之上，而这些条件在E20之后全部消失\n\n印度乙醇掺混率从十年前的不到2%飙升至2025年的20%，表面上看是政策执行力的胜利。但Bernstein的分析揭示了一个更微妙的真相：这个成功建立在三个恰好成立的条件之上——掺混的乙醇进入的是印度已经拥有的发动机、原料来自印度已经种植的作物、消费者没有被要求付出任何额外成本。\n\n一个不需要任何人改变的方案，自然容易规模化。\n\n但问题在于，这三个条件在E20之后全部开始逆转。超过80%的印度道路车辆是在2023年4月之前制造的，只兼容E10。E20本身已经在老旧车辆中引发了橡胶密封件退化、燃油泵投诉和6-10%的里程损失——这些抱怨随着掺混比例每提高一个百分点而显著加剧。\n\n> **KC评论：** 这份报告最值得注意的洞察在于，它把“政策可行性”和“技术可行性”区分了开来。E20之所以成功，不是因为技术有多成熟，而是因为它恰好落在了一个“所有人都无需改变”的舒适区。一旦进入E25及以上，消费者要承担里程损失、维修成本增加，而政府要面对选民不满。这是典\n\n[... middle omitted ...]\n\n既方便喂给AI做进一步分析，也方便人工快速把握全球市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度乙醇：E20之后，还能走多远？\n\n封面：乙醇的边界\n\n印度E20只是开始，但下一步更难\n\n印度的乙醇计划，到E20这一步走得很快，但再往后推，每一步都很难。\n\n1/ E20之后的“混合墙”\n超过80%的印度路上跑的车，都是为E10设计的。\nE20已经让老车出现里程损失（官方说1-6%，车主反馈接近10%），还有橡胶密封件腐蚀、燃油泵问题。\n政府刚让ARAI去研究E25对现有车队的影响。\n结论：新车可以适配E25，但老车要么等报废加速，要么等改装方案规模化。\n\n2/ 原料不是产能问题，是水的问题\n印度乙醇产能过剩（200亿升 vs E20需求110亿升），但可持续原料只有60-100亿升。\n2023年弱雨季，甘蔗减产，印度从玉米出口国变成净进口国，进口了100万吨玉米做乙醇。\n乙醇成本从60-62卢比/升（甘蔗）涨到72卢比/升（玉米）。\n一个想减少石油进口的计划，反而要靠进口粮食来维持。\n\n3/ 乙醇不比汽油便宜\n按75美元/桶原油算，汽油成本约55-58卢比/升，乙醇采购价60-62卢比/升（好雨季），还不算里程损失。\n所以继续推乙醇的唯一理由：作为对冲原油价格飙升的保险。\n但这个保险只在原油暴涨时有用\n\n[... middle omitted ...]\n\n, and then beyond to flex-fuel vehicles and E85? More importantly, is the incremental reduction in crude imports worth the cost and complexity of building an entirely new fuel value chain?\n\nWe\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R048",
    "title": "GS618复盘：补贴换增长，但赢家只在少数赛道",
    "digest": "[wechat_article.md]\n# GS618复盘：补贴换增长，但赢家只在少数赛道\n\n2026年618购物节落幕，GS在第一时间发布了复盘报告。核心判断并不复杂，但值得认真拆解：**整体GMV增速从去年的10%放缓至6%，但头部品牌和少数品类依然跑出了两位数增长。** 这不是一场普涨的盛宴，而是一场补贴换增长、平台换打法、消费者换偏好的结构性分化。\n\n这份报告最值得看的判断，不是增速放缓本身，而是“补贴效率的分化”正在成为品牌竞争格局的分水岭。谁能在更大的折扣压力下，依然守住利润和排名，谁才是真正的结构性赢家。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 整体增速放缓，但包裹均价上升揭示了一个反常识信号\n\nGS援引Analysys的数据显示，2026年618主要平台整体GSV（总商品交易额）同比增长6%，较2025年的10%明显回落。与此同时，包裹量增速为8%，同样低于去年同期的16%。但一个值得关注的细节是：**GSV增速与包裹量增速的差距在收窄，意味着客单价在提升。**\n\n这听起来反常识——在一片“消费降级”的叙事中，618的客单价反而高了。GS在专家电话中给出的解释是：平台和政府的补贴力度加大，但更多流向了高客单价品类（如3C、高端美妆、超高端白酒），拉高了整体均价。\n\n> **KC评论：** 客单价上升不一定是消费升级，更可能是补贴结构的选择性倾斜。平台在把有限的补贴资源集中到能拉动GMV的高价商品上。这对低客单价、低毛利的品牌意味着什么？如果补贴不流向你，你的增长压力会更大。完整报告中有分品类的折扣率对比表，值得仔细看。\n\n---\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 美妆赛道：MNC重新夺回Tmall前十，但本土品牌在抖音找到了新战场\n\nGS的数据显示，化妆品是今年6\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618成绩单：谁在扛着消费走\n\n📊 618复盘：消费分化加剧\n\n今年618整体增速6%，比去年10%有所放缓。但拆开看，不同品类、不同品牌的分化非常明显。\n\n1️⃣ 美妆是最大赢家\n天猫美妆GMV同比+15%，抖音+21%。国际高端品牌强势回归——修丽可、雅诗兰黛、SK-II排名大幅提升。本土品牌毛戈平、珀莱雅、上海家化也表现不俗，增速超过行业平均。\n\n2️⃣ 宠物经济持续爆发\n天猫宠物食品GMV同比暴增48%。但竞争也在加剧，本土品牌折扣力度普遍加大3-13个百分点。乖宝、中宠在抖音表现不错，但天猫排名有所下滑。\n\n3️⃣ 运动品牌冷热不均\n整体增速16%，但品牌间差距大。Descente、迪卡侬、可隆排名上升，Nike和骆驼反而下滑。安踏集团旗下多品牌表现亮眼。\n\n4️⃣ 家电增长乏力\n受去年高基数影响，家电整体平淡。但清洁电器等渗透率仍在提升的品类有相对更好的增长。\n\n5️⃣ 白酒线上集中度提升\n京东白酒GMV同比+25%，茅台五粮液贡献主要增量。超高端价格带是增长主力，飞天茅台单品GMV突破3亿。\n\n6️⃣ 折扣力度普遍加大\n除零食外，多数品类折扣同比扩大。宠物食品折扣最猛，从23%扩到32%。美妆和\n\n[... middle omitted ...]\n\nst year) likely due to higher ticket size (see our 618 expert call takeaways) but a wider gap vs. yoy GMV growth according to the expert's note of mid-teens yoy GMV in this year/low-teens yoy \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R049",
    "title": "GS：罕见病药物临床转折点已至，医生真实反馈正在改写竞争格局",
    "digest": "[wechat_article.md]\n# GS：罕见病药物临床转折点已至，医生真实反馈正在改写竞争格局\n\n一份来自GS生物技术团队的研报，最近在产业圈和投资圈引发了超出预期的关注。原因不在于它预测了某个重磅药物的销售额，而在于它做了一件研报通常不擅长的事：邀请一位每天接诊约350名患者的成年内分泌科医生，坐下来聊了整整一顿午餐的时间。\n\n这份报告的核心判断极为直接：罕见病药物的竞争，正在从“临床数据比拼”进入“医生真实体验驱动”的新阶段。那些在临床试验中表现优异的药物，未必能在真实世界中顺利推开；而一些数据并非最亮眼、但解决了医生和患者真实痛点的方案，反而可能成为赢家。GS通过这位一线医生的视角，揭示了几个即将发生结构性变化的治疗领域，以及对相关公司竞争格局的深远影响。\n\n对于关注生物技术投资的读者而言，这份报告的价值不在于它提供了多少个新靶点，而在于它给出了一个稀缺的“临床决策显微镜”——让我们看到，医生在面对不同药物时，真正在意的是什么，以及这些偏好将如何转化为市场份额的重新分配。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 每周一次注射的“妥协点”已经清晰，但金标准药物的护城河比想象中更深\n\n在甲状旁腺功能减退症领域，GS与医生的交流揭示了一个关键的竞争临界点。目前，Ascendis Pharma的Yorvipath作为每日注射的疗法，在临床数据上确立了约80%的稳定应答率，被视为“金标准”。然而，每周一次的注射方案，如MBX Biosciences的canvuparatide，无疑更符合患者对便利性的追求。\n\n医生给出的判断非常务实：如果每周一次的方案能达到50%的应答率，就是一个可以接受的“妥协点”。但关键在于，医生同时指出，临床试验中限制急救药物使用的应答标准，并不反映真实世界的治疗实践。这意味着，canvuparatide在\n\n[... middle omitted ...]\n\n决策者和投资者一起讨论这些未解问题，欢迎加入我们的知识星球。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n罕见病投研笔记：内分泌专家午餐会干货\n\n罕见病用药的真实世界观察\n\n和一位管理350+患者的内分泌专家聊了聊，发现几个有意思的点：\n\n1️⃣ 甲旁减治疗：Yorvipath仍是金标准\n- 专家管理10个HPT患者，5个在用Yorvipath\n- 患者对每日注射接受度高，满意能停用钙剂\n- 对每周一次的新药（canvuparatide），专家认为50%应答率是可接受的权衡\n\n2️⃣ CAH治疗：Crenessity初体验\n- 20个患者中3个女性在用，效果不错（减少激素用量+体重下降+血糖改善）\n- 但每日2次给药+对雄激素控制有限是短板\n- 新药atumelnant因每日一次口服+独特机制被看好\n\n3️⃣ PBH：被低估的未满足需求\n- 30个患者中40%控制不佳，15-20%有严重低血糖事件\n- 现有治疗（二氮嗪、GLP-1）效果有限\n- 新药avexitide若能使L2/L3事件降低50%，临床意义显著\n\n4️⃣ PWS：两个新选择各有亮点\n- Vykat改善患者和照顾者生活质量\n- setmelanotide减重效果\"前所未有\"（GLP-1在PWS中一年只能减1-3%）\n- 联合使用值得期待\n\n5️⃣ \n\n[... middle omitted ...]\n\n Yorvipath, Crenessity, and Vykat in particular, despite insurance/reimbursement hurdles which he cited are an issue across high price point rare disease therapies that his office is navigatin\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R050",
    "title": "摩根斯坦利：MS：MLCC的“另一个AI挤压”刚刚开始",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：MLCC的“另一个AI挤压”刚刚开始\n\nAI算力的军备竞赛，正在从GPU、HBM等半导体核心部件，蔓延到一个此前被市场低估的被动元件领域——MLCC（多层陶瓷电容）。MS在最新发布的深度研报中，提出了一个值得产业决策者和投资者高度关注的判断：MLCC行业正在经历一场“超级周期”，其结构性紧张的逻辑，与两年前DDR4 DRAM因HBM挤占产能而引发的价格飙升如出一辙。\n\n这不是一次普通的元器件缺货。报告的核心论点是，AI服务器对MLCC的需求正在从“量的增长”演变为“质的重构”。一台AI服务器消耗的MLCC数量是传统服务器的10到15倍，但更重要的是，高端AI级MLCC的产能正被锁定数年，而普通消费级和车规级产能无法轻易转换。这意味着，一场由AI驱动的、结构性的供给挤压已经拉开序幕，而市场可能才刚刚开始定价这一变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一台AI服务器吃掉44万颗MLCC，但数量只是故事的一半\n\nMS的测算显示，NVIDIA GB300平台每台全配机柜需要约32万颗MLCC，而下一代Vera Rubin平台更是将这一数字推高至约57万颗，单位价值量提升约182%。作为对比，一台高端智能手机的MLCC用量仅约1万颗。这组数字直观地解释了为什么AI正在成为MLCC需求端最大的增量变量。\n\n但真正关键的并非数量，而是规格的跃迁。AI GPU需要在纳秒级时间尺度内应对剧烈的电流变化，这对MLCC的等效串联电阻（ESR）和等效串联电感（ESL）提出了严苛要求。传统服务器中大量使用的标准品无法胜任。在Rubin架构中，47微法以上高容值MLCC的用量占比已从GB300时代的不足20%提升至超过30%。MS预计，云端AI对47微法以上MLCC的需求将从2025年的约40亿颗，激增至\n\n[... middle omitted ...]\n\ns。欢迎加入，继续讨论这轮MLCC超级周期的投资机会与风险。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI在“吃”电容？MLCC超级周期来了\n\nAI从芯片“挤”到电容了\n\n最近某外资投行发了一份MLCC（多层陶瓷电容）研报，核心观点很直接：AI正在从半导体转向MLCC，高端电容供需严重错配。\n\n简单说，AI服务器对MLCC的需求是传统服务器的10-15倍——一台GB300机柜要用约32万颗，而最新的Rubin平台直接飙到57万颗。而且不只是数量多，规格也变了：需要更小尺寸、更大容量、更低电阻的“高端货”。\n\n几个关键变化值得关注：\n\n1️⃣ 产能被“吃掉”了\n高端MLCC需要几百上千层介质层，一颗就吃掉大量产能。虽然AI只占行业总出货量的3%左右，但消耗的产能远超这个比例。日韩双巨头（Murata和SEMCO合计占85%份额）都在把产能往AI倾斜，消费电子、汽车、工业的供应就紧了。\n\n2️⃣ 价格开始涨了\n研报提到，深圳华强北的现货市场，部分型号价格已经涨了2-10倍。分销商从2季度开始提价20-30%，还取消了批量折扣。库存也低——分销商平均只有1.5个月库存，下游客户不到1个月。\n\n3️⃣ 这不是短期炒作\n和2017-2018年的MLCC超级周期不同，这次有AI的持续需求支撑。新产能从建厂到投产要2年，设\n\n[... middle omitted ...]\n\nch in high-end components. TAM is set to expand, driven by compute, power, and networking needs. The key question is not if supply tightens, but how long constraints could persist.\n\nWhat's cha\n\n[... middle omitted ...]\n\nynix (000660.KS)</td><td>O (09/21/2025)</td><td>W2,919,000</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Beyond Oil, the Prices of Several Gulf Exports Have Retraced From Their Recent Peaks, and Some Are Now Close to Pre-War Levels; US Refined Product Spreads Rose Sharply in May"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 3: We Estimate That Higher Commodity Prices Will Deliver a Roughly 0.4pp Boost to Year-over-Year Core PCE Inflation This Year, Which We Expect to Fade in 2027"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 3: We Estimate That Higher Commodity Prices Will Deliver a Roughly 0.4pp Boost to Year-over-Year Core PCE Inflation This Year, Which We Expect to Fade in 2027"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 4: We Expect Headline Inflation to Slow From Here; Our Strategists' Upside Scenario Would Add Another 1.1pp to Headline PCE and 0.2pp to Core PCE, While Their Downside Scenario Would Subtract 0.4pp and 0.1pp"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 4: We Expect Headline Inflation to Slow From Here; Our Strategists' Upside Scenario Would Add Another 1.1pp to Headline PCE and 0.2pp to Core PCE, While Their Downside Scenario Would Subtract 0.4pp and 0.1pp Note: Inclu"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We Expect Headline Inflation to Slow From Here; Our Strategists' Upside Scenario Would Add Another 1.1pp to Headline PCE and 0.2pp to Core PCE, While Their Downside Scenario Would Subtract 0.4pp and 0.1pp Note: Inclu"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 5",
    "context": "Exhibit 6: We Expect AI-Related Price Pressures to Boost Year-over-Year Core PCE Inflation by 0.4pp by December 2026, With a 0.6pp Peak Earlier in H2; We Expect AI-Related Price Pressures to Boost Core CPI by About 0.1pp by Decembe"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We Expect AI-Related Price Pressures to Boost Year-over-Year Core PCE Inflation by 0.4pp by December 2026, With a 0.6pp Peak Earlier in H2; We Expect AI-Related Price Pressures to Boost Core CPI by About 0.1pp by Decembe"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 8: Slower Wage Growth in Labor-Intensive Services Should Provide an Additional Disinflationary Impulse This Year \\* Includes food services, hotels and casinos, other recreational services, nursing homes, motor vehicle ser"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 8: Slower Wage Growth in Labor-Intensive Services Should Provide an Additional Disinflationary Impulse This Year \\* Includes food services, hotels and casinos, other recreational services, nursing homes, motor vehicle ser"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Our Tool for Tracking Input Cost Pressures Across the Supply Chain Accelerated Somewhat in Recent Months, but This Largely Reflected Energy Passthrough"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Our Persistent Inflation Risk Indicator Ticked Up Somewhat in Recent Months but Remains Broadly in Line With Its Post-1995 Average"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Our Persistent Inflation Risk Indicator Ticked Up Somewhat in Recent Months but Remains Broadly in Line With Its Post-1995 Average ## The Inflation Outlook We forecast year-over-year core PCE inflation of $3.2\\%$ in De"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We Expect Energy Price Passthrough, AI-Related Pressure, and the Stock Market Boom to Keep Year-over-Year Core PCE Inflation at 3.2% in December 2026, Even as Core CPI Inflation Slows to 2.6%; We Expect Both PCE and CPI"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We Expect Energy Price Passthrough, AI-Related Pressure, and the Stock Market Boom to Keep Year-over-Year Core PCE Inflation at 3.2% in December 2026, Even as Core CPI Inflation Slows to 2.6%; We Expect Both PCE and CPI"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: ASEAN economies are largely net food importers Excluding palm oil, Malaysia and Indonesia are net food importers Exhibit 2: The latest biofuel mandates in ASEAN"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in oil prices Exhibit 4: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in fertiliser prices Exhibit 5: Pooled ASEAN cumulative food CP"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in oil prices Exhibit 4: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in fertiliser prices Exhibit 5: Pooled ASEAN cumulative food CP"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in fertiliser prices Exhibit 5: Pooled ASEAN cumulative food CPI response (%) to a 1°C increase in El Niño (RONI) ## Pipeline pressure still building Us"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Percentage point contribution to headline CPI from oil, fertilizer and El Niño shocks Exhibit 7: Peak headline CPI response from oil, fertilizer and El Niño shocks ## Domestic policy responses Around El Niño episodes,"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Tech investment contributions to growth now match the 1990s, but have not been as sustained yet"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Tech investment contributions to growth now match the 1990s, but have not been as sustained yet Exhibit 4: AI investment now likely to be comparable to if not exceed the 1990s tech peak"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Hyperscaler capex estimates have risen sharply since late 2025 Exhibit 3: Tech investment contributions to growth now match the 1990s, but have not been as sustained yet Exhibit 4: AI investment now likely to be comp"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Corporate profits have remained near record levels"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Corporate profits have remained near record levels Exhibit 6: Unit labor costs and wages are growing more slowly than in late 1990s Exhibit 7: Free cash flow for hyperscalers has dropped sharply, but not for the mark"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 8: No meaningful deterioration in corporate financial balance and current account has improved"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Unit labor costs and wages are growing more slowly than in late 1990s Exhibit 7: Free cash flow for hyperscalers has dropped sharply, but not for the market as a whole Exhibit 8: No meaningful deterioration in corpor"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 9: US valuations remain high, particularly on “backward-looking” measures"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 9: US valuations remain high, particularly on “backward-looking” measures Exhibit 10: Earnings revisions, not valuations have driven the rally this year We have used a simple macro approach as a cross-check on the valua"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 11: Substantial value added to AI-related areas of the market since late 2022 \"Semiconductors\", \"hyperscalers\", and \"other AI-related\" are constituents of the GS TMT AI basket (developed by GS Global Banking & Markets)"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Substantial value added to AI-related areas of the market since late 2022 \"Semiconductors\", \"hyperscalers\", and \"other AI-related\" are constituents of the GS TMT AI basket (developed by GS Global Banking & Markets) We"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: More optimistic assumptions would raise the Present Discounted Value of potential AI-related capital revenues"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: More optimistic assumptions would raise the Present Discounted Value of potential AI-related capital revenues ## From aggregation to extrapolation"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 15: Higher productivity growth is correlated with increased profit shares in the short term..."
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Higher productivity growth is correlated with increased profit shares in the short term... Exhibit 16: ...but this relationship is much weaker over longer time periods As importantly, the investment boom is itself fu"
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Higher productivity growth is correlated with increased profit shares in the short term... Exhibit 16: ...but this relationship is much weaker over longer time periods As importantly, the investment boom is itself fu"
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Rise in equity volatility has so far mostly been at single stock level, with correlations falling to record lows Exhibit 18: Late 1990s saw higher volatility at both single stock and index levels"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Rise in equity volatility has so far mostly been at single stock level, with correlations falling to record lows Exhibit 18: Late 1990s saw higher volatility at both single stock and index levels Exhibit 19: Returns"
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Returns in broad indices more moderate, but narrower indices now matching late 1990s returns Exhibit 20: April-May 2026 saw an acceleration in returns in key indices ## From the macro masking the boom, to the boom ma"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Returns in broad indices more moderate, but narrower indices now matching late 1990s returns Exhibit 20: April-May 2026 saw an acceleration in returns in key indices ## From the macro masking the boom, to the boom ma"
  },
  {
    "figure_id": "F041",
    "report_id": "R003",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We have seen a large rise in US household wealth and a sharp fall in the savings rate Exhibit 22: US spending and income growth outside tech investment much more muted than in late 1990s Where the 1990s macro picture"
  },
  {
    "figure_id": "F042",
    "report_id": "R003",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We have seen a large rise in US household wealth and a sharp fall in the savings rate Exhibit 22: US spending and income growth outside tech investment much more muted than in late 1990s Where the 1990s macro picture"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Private Payrolls Are Back on the Rise"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Private Payrolls Are Back on the Rise Exhibit 3: But So Is Inflation In addition to pivoting the Fed's main reaction function toward inflation, Chair Warsh also indicated that the Fed would no longer provide as much"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Private Payrolls Are Back on the Rise Exhibit 3: But So Is Inflation In addition to pivoting the Fed's main reaction function toward inflation, Chair Warsh also indicated that the Fed would no longer provide as much"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Fresh Money Buy List & S&P 500 Cumulative Total Return Exhibit 6: Fresh Money Buy List / S&P 500 Cumulative Relative Return ## Weekly Charts to Watch"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Fresh Money Buy List & S&P 500 Cumulative Total Return Exhibit 6: Fresh Money Buy List / S&P 500 Cumulative Relative Return ## Weekly Charts to Watch Exhibit 7: US Earnings Snapshot S&P 500 Y/Y EPS Growth S&P 500 Con"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US Earnings Snapshot S&P 500 Y/Y EPS Growth S&P 500 Consensus EPS US Leading Earnings Indicator US Non-PMI Leading Earnings Indicator MS Non-PMI Leading Earnings Indicator (Leading 1-Yr.)"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US Earnings Snapshot S&P 500 Y/Y EPS Growth S&P 500 Consensus EPS US Leading Earnings Indicator US Non-PMI Leading Earnings Indicator MS Non-PMI Leading Earnings Indicator (Leading 1-Yr.)"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US Earnings Snapshot S&P 500 Y/Y EPS Growth S&P 500 Consensus EPS US Leading Earnings Indicator US Non-PMI Leading Earnings Indicator MS Non-PMI Leading Earnings Indicator (Leading 1-Yr.)"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "US Leading Earnings Indicator US Non-PMI Leading Earnings Indicator MS Non-PMI Leading Earnings Indicator (Leading 1-Yr.)"
  },
  {
    "figure_id": "F052",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Sector Ratings Exhibit 10: Equity Risk Premium Exhibit 11: US Equity Market Technicals and Financial Conditions S&P 500 Advance/Decline Line S&P 500 Percent Members Above 200-Day Moving Average"
  },
  {
    "figure_id": "F053",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Equity Risk Premium Exhibit 11: US Equity Market Technicals and Financial Conditions S&P 500 Advance/Decline Line S&P 500 Percent Members Above 200-Day Moving Average S&P 500 with Moving Averages"
  },
  {
    "figure_id": "F054",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Equity Risk Premium Exhibit 11: US Equity Market Technicals and Financial Conditions S&P 500 Advance/Decline Line S&P 500 Percent Members Above 200-Day Moving Average S&P 500 with Moving Averages Chicago Fed Nati"
  },
  {
    "figure_id": "F055",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 12: US Small Cap Equities Russell 2000 NTM P/B and Relative NTM P/B vs. S&P 500"
  },
  {
    "figure_id": "F056",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: US Small Cap Equities Russell 2000 NTM P/B and Relative NTM P/B vs. S&P 500"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: US Small Cap Equities Russell 2000 NTM P/B and Relative NTM P/B vs. S&P 500 NTM EPS by Cap Size"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: US Small Cap Equities Russell 2000 NTM P/B and Relative NTM P/B vs. S&P 500 NTM EPS by Cap Size Exhibit 13: Earnings Revisions Breadth"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: US Small Cap Equities Russell 2000 NTM P/B and Relative NTM P/B vs. S&P 500 NTM EPS by Cap Size Exhibit 13: Earnings Revisions Breadth US Earnings Revisions Breadth vs Price Y/Y"
  },
  {
    "figure_id": "F060",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Earnings Revisions Breadth US Earnings Revisions Breadth vs Price Y/Y US Earnings Revisions Breadth (Adv. 25W) vs EPS Y/Y"
  },
  {
    "figure_id": "F061",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Earnings Revisions Breadth US Earnings Revisions Breadth vs Price Y/Y US Earnings Revisions Breadth (Adv. 25W) vs EPS Y/Y Exhibit 14: Earnings Revisions Breadth vs YoY Performance"
  },
  {
    "figure_id": "F062",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Earnings Revisions Breadth US Earnings Revisions Breadth vs Price Y/Y US Earnings Revisions Breadth (Adv. 25W) vs EPS Y/Y Exhibit 14: Earnings Revisions Breadth vs YoY Performance"
  },
  {
    "figure_id": "F063",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Earnings Revisions Breadth vs YoY Performance"
  },
  {
    "figure_id": "F064",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Earnings Revisions Breadth vs YoY Performance"
  },
  {
    "figure_id": "F065",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Earnings Revisions Breadth vs YoY Performance"
  },
  {
    "figure_id": "F066",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Earnings Revisions Breadth vs YoY Performance"
  },
  {
    "figure_id": "F067",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Front-end volatility: 3m par yield, daily changes, 63-day standard deviation, annualized Exhibit 2: Front-end vs back-end volatility by Fed Chair: 3m yield, 10y yield, period standard deviation The ranking across the"
  },
  {
    "figure_id": "F068",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Front-end volatility: 3m par yield, daily changes, 63-day standard deviation, annualized Exhibit 2: Front-end vs back-end volatility by Fed Chair: 3m yield, 10y yield, period standard deviation The ranking across the"
  },
  {
    "figure_id": "F069",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Correlation between daily changes in 2y yields and the 2s10s yield curve shape Exhibit 4: Front-end share of yield curve variance: average daily change of 1m-2y yields vs. 1m-30y Readings above 100% mean the front en"
  },
  {
    "figure_id": "F070",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Correlation between daily changes in 2y yields and the 2s10s yield curve shape Exhibit 4: Front-end share of yield curve variance: average daily change of 1m-2y yields vs. 1m-30y Readings above 100% mean the front en"
  },
  {
    "figure_id": "F071",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Yield curve slope volatility: 2s10s curve, daily changes, 63-day standard deviation, annualized Exhibit 6: Yield curve curvature volatility: 2s10s30s butterfly, daily changes, 63-day standard deviation, annualized ##"
  },
  {
    "figure_id": "F072",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Yield curve slope volatility: 2s10s curve, daily changes, 63-day standard deviation, annualized Exhibit 6: Yield curve curvature volatility: 2s10s30s butterfly, daily changes, 63-day standard deviation, annualized ##"
  },
  {
    "figure_id": "F073",
    "report_id": "R005",
    "label": "Exhibit 8",
    "context": "Exhibit 7: Front-end vol vs. curve slope vol: 3m vs. 2s10s curve Exhibit 8: Regime scorecard: three volatility dimensions ## Investment implications"
  },
  {
    "figure_id": "F074",
    "report_id": "R005",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Front-end vol vs. curve slope vol: 3m vs. 2s10s curve Exhibit 8: Regime scorecard: three volatility dimensions ## Investment implications A move back toward the Greenspan toolkit argues for owning curve-shape and fro"
  },
  {
    "figure_id": "F075",
    "report_id": "R006",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: Trade-offs by chiller type and regional variation Deciding between air-cooled and water-cooled chillers based on geography Note: Power costs are \\$10.25, \\$6.26, \\$6.7, \\$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from E"
  },
  {
    "figure_id": "F076",
    "report_id": "R006",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Trade-offs by chiller type and regional variation Deciding between air-cooled and water-cooled chillers based on geography Note: Power costs are \\$10.25, \\$6.26, \\$6.7, \\$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from E"
  },
  {
    "figure_id": "F077",
    "report_id": "R006",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Trade-offs by chiller type and regional variation Deciding between air-cooled and water-cooled chillers based on geography Note: Power costs are \\$10.25, \\$6.26, \\$6.7, \\$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from E"
  },
  {
    "figure_id": "F078",
    "report_id": "R006",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: Air-cooled vs. Water-cooled Chillers"
  },
  {
    "figure_id": "F079",
    "report_id": "R006",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Comparison of compressors"
  },
  {
    "figure_id": "F080",
    "report_id": "R006",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 5: Comparison of compressors Most appropriate for data center loads ## How big is the market?"
  },
  {
    "figure_id": "F081",
    "report_id": "R006",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Chiller Market Size (Fully loaded) by Scenario ## Air vs. Water ... what's better? Both air-cooled and water-cooled chillers have clear niches. Generally, air-cooled chillers make more sense when power costs are low (b"
  },
  {
    "figure_id": "F082",
    "report_id": "R006",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 8: Air-cooled vs. Water-cooled; when do you deploy it?"
  },
  {
    "figure_id": "F083",
    "report_id": "R006",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 9: How much water does a water-cooled chiller use?"
  },
  {
    "figure_id": "F084",
    "report_id": "R006",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: How much water does a water-cooled chiller use? ## Competitor benchmarking of products Broadly, we think Trane, JCI, and Carrier all have strong products. On the air-cooled side, JCI and Carrier have announced new prod"
  },
  {
    "figure_id": "F085",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The South Korea FCI Eased by 29bp Last Week as Tech Continued to Lead an Equity Rally Jan Hatzius GS & Co. LLC Joseph Briggs"
  },
  {
    "figure_id": "F086",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The Global ex Russia FCI Eased by -0.8bps Last Week Primarily on Equities Exhibit 3: Higher 2026 Growth in South Korea"
  },
  {
    "figure_id": "F087",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The Global ex Russia FCI Eased by -0.8bps Last Week Primarily on Equities Exhibit 3: Higher 2026 Growth in South Korea Exhibit 4: Our Preliminary May CAI Fell by -0.8pp in China and Rose by +0.7pp in Japan"
  },
  {
    "figure_id": "F088",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The Global ex Russia FCI Eased by -0.8bps Last Week Primarily on Equities Exhibit 3: Higher 2026 Growth in South Korea Exhibit 4: Our Preliminary May CAI Fell by -0.8pp in China and Rose by +0.7pp in Japan CAI in c"
  },
  {
    "figure_id": "F089",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 6: GS Wage Trackers and Inflation Measures US wage tracker is composition-adjusted in 2020 and 2021."
  },
  {
    "figure_id": "F090",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 6: GS Wage Trackers and Inflation Measures US wage tracker is composition-adjusted in 2020 and 2021. Exhibit 7: GS Jobs-Workers Gaps"
  },
  {
    "figure_id": "F091",
    "report_id": "R007",
    "label": "Exhibit 6",
    "context": "Exhibit 6: GS Wage Trackers and Inflation Measures US wage tracker is composition-adjusted in 2020 and 2021. Exhibit 7: GS Jobs-Workers Gaps ## Detailed Indicators Update ## Financial Conditions Index (FCI)"
  },
  {
    "figure_id": "F092",
    "report_id": "R007",
    "label": "Exhibit 7",
    "context": "Exhibit 7: GS Jobs-Workers Gaps ## Detailed Indicators Update ## Financial Conditions Index (FCI) Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F093",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F094",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 10: GS US FCI Level (Left) and Weekly C"
  },
  {
    "figure_id": "F095",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 10: GS US FCI Level (Left) and Weekly C"
  },
  {
    "figure_id": "F096",
    "report_id": "R007",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change"
  },
  {
    "figure_id": "F097",
    "report_id": "R007",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change"
  },
  {
    "figure_id": "F098",
    "report_id": "R007",
    "label": "Exhibit 10",
    "context": "Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 12: Weekly Change in FCI Across Countries"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "Exhibit 10",
    "context": "Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 12: Weekly Change in FCI Across Countries"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 12: Weekly Change in FCI Across Countries Exhibit 13: Year-Over-Year Change in FCI Across Countries"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 12: Weekly Change in FCI Across Countries Exhibit 13: Year-Over-Year Change in FCI Across Countries FCI Impulses Exhibit 14: FCI"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Weekly Change in FCI Across Countries Exhibit 13: Year-Over-Year Change in FCI Across Countries FCI Impulses Exhibit 14: FCI Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right) Exhibit"
  },
  {
    "figure_id": "F103",
    "report_id": "R007",
    "label": "Exhibit 13",
    "context": "Exhibit 16: CAI Aggregates"
  },
  {
    "figure_id": "F104",
    "report_id": "R007",
    "label": "Exhibit 14",
    "context": "Exhibit 14: FCI Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right) Exhibit 15: FCI Impulses in the US, Euro Area, Japan, and UK Current Activity Indicator (CAI) Exhibit 16: CAI Aggregates GS DM"
  },
  {
    "figure_id": "F105",
    "report_id": "R007",
    "label": "Exhibit 15",
    "context": "Exhibit 17: CAI Heatmap"
  },
  {
    "figure_id": "F106",
    "report_id": "R007",
    "label": "Exhibit 15",
    "context": "Exhibit 17: CAI Heatmap CAI in countries with 0% of data released is forecasted. CAI aggregates for Global, Developed Markets, and Emerging Markets are GDP-weighted using market FX country weights."
  },
  {
    "figure_id": "F107",
    "report_id": "R007",
    "label": "Exhibit 17",
    "context": "Exhibit 19: GS MAP Surprise Index We present the 21-day moving average of daily MAP scores."
  },
  {
    "figure_id": "F108",
    "report_id": "R007",
    "label": "Exhibit 18",
    "context": "Exhibit 18: CAIs for Large DMs and EMs MAP Exhibit 19: GS MAP Surprise Index We present the 21-day moving average of daily MAP scores."
  },
  {
    "figure_id": "F109",
    "report_id": "R007",
    "label": "Exhibit 18",
    "context": "Exhibit 18: CAIs for Large DMs and EMs MAP Exhibit 19: GS MAP Surprise Index We present the 21-day moving average of daily MAP scores. We present the 21 day moving average of daily MAP scores."
  },
  {
    "figure_id": "F110",
    "report_id": "R007",
    "label": "Exhibit 19",
    "context": "Exhibit 19: GS MAP Surprise Index We present the 21-day moving average of daily MAP scores. We present the 21 day moving average of daily MAP scores. ## Trimmed Core Inflation"
  },
  {
    "figure_id": "F111",
    "report_id": "R007",
    "label": "Exhibit 19",
    "context": "Exhibit 19: GS MAP Surprise Index We present the 21-day moving average of daily MAP scores. We present the 21 day moving average of daily MAP scores. ## Trimmed Core Inflation Exhibit 21: GS Trimmed Core Inflation"
  },
  {
    "figure_id": "F112",
    "report_id": "R007",
    "label": "Exhibit 21",
    "context": "Exhibit 21: GS Trimmed Core Inflation ## Wage Trackers Exhibit 22: GS Wage Trackers"
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "Exhibit 21",
    "context": "Exhibit 21: GS Trimmed Core Inflation ## Wage Trackers Exhibit 22: GS Wage Trackers Exhibit 23: GS Sequential Wage Trackers"
  },
  {
    "figure_id": "F114",
    "report_id": "R007",
    "label": "Exhibit 22",
    "context": "Exhibit 22: GS Wage Trackers Exhibit 23: GS Sequential Wage Trackers"
  },
  {
    "figure_id": "F115",
    "report_id": "R007",
    "label": "Exhibit 22",
    "context": "Exhibit 22: GS Wage Trackers Exhibit 23: GS Sequential Wage Trackers"
  },
  {
    "figure_id": "F116",
    "report_id": "R007",
    "label": "Exhibit 23",
    "context": "Exhibit 23: GS Sequential Wage Trackers"
  },
  {
    "figure_id": "F117",
    "report_id": "R007",
    "label": "Exhibit 23",
    "context": "Exhibit 23: GS Sequential Wage Trackers Exhibit 24: GS Jobs-Workers Gaps"
  },
  {
    "figure_id": "F118",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps"
  },
  {
    "figure_id": "F119",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps Exhibit 25: Wage Survey Leading Indicators"
  },
  {
    "figure_id": "F120",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps Exhibit 25: Wage Survey Leading Indicators"
  },
  {
    "figure_id": "F121",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps Exhibit 25: Wage Survey Leading Indicators"
  },
  {
    "figure_id": "F122",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps Exhibit 25: Wage Survey Leading Indicators ## Top-Down Fiscal Impulses Exhibit 26: Top-Down Fiscal Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right)"
  },
  {
    "figure_id": "F123",
    "report_id": "R007",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Wage Survey Leading Indicators ## Top-Down Fiscal Impulses Exhibit 26: Top-Down Fiscal Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right) We compute the 4-quarter measure using averag"
  },
  {
    "figure_id": "F124",
    "report_id": "R007",
    "label": "Exhibit 26",
    "context": "Exhibit 27: Top-Down Fiscal Impulses in the US, Euro Area, China, and UK The US impulse captures both expansionary fiscal discretionary policy and the tax-like effects of tariffs."
  },
  {
    "figure_id": "F125",
    "report_id": "R007",
    "label": "Exhibit 26",
    "context": "Exhibit 27: Top-Down Fiscal Impulses in the US, Euro Area, China, and UK The US impulse captures both expansionary fiscal discretionary policy and the tax-like effects of tariffs. Output Gaps Exhibit 28: Latest Short-Run Utilizati"
  },
  {
    "figure_id": "F126",
    "report_id": "R007",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Latest Short-Run Utilization Scores Exhibit 29: Short-Run Utilization Scores ## GS Forecasts vs. Consensus Exhibit 30: Change in GS 2026 Inflation Forecasts"
  },
  {
    "figure_id": "F127",
    "report_id": "R007",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Short-Run Utilization Scores ## GS Forecasts vs. Consensus Exhibit 30: Change in GS 2026 Inflation Forecasts ## Exhibit 31: Change in GS 2027 Inflation Forecasts Exhibit 32: Change in GS 2026 GDP Forecasts"
  },
  {
    "figure_id": "F128",
    "report_id": "R007",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Change in GS 2026 Inflation Forecasts ## Exhibit 31: Change in GS 2027 Inflation Forecasts Exhibit 32: Change in GS 2026 GDP Forecasts ## Exhibit 33: Change in GS 2027 GDP Forecasts"
  },
  {
    "figure_id": "F129",
    "report_id": "R007",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Change in GS 2027 Inflation Forecasts Exhibit 32: Change in GS 2026 GDP Forecasts ## Exhibit 33: Change in GS 2027 GDP Forecasts ## Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters"
  },
  {
    "figure_id": "F130",
    "report_id": "R007",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Change in GS 2026 GDP Forecasts ## Exhibit 33: Change in GS 2027 GDP Forecasts ## Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters Exhibit 35: GS 2027 Global GDP Forecasts vs. Other Forecasters"
  },
  {
    "figure_id": "F131",
    "report_id": "R007",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Change in GS 2027 GDP Forecasts ## Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters Exhibit 35: GS 2027 Global GDP Forecasts vs. Other Forecasters Thank you to Jamal Lawal, intern on the Global Econom"
  },
  {
    "figure_id": "F132",
    "report_id": "R007",
    "label": "Exhibit 34",
    "context": "Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters Exhibit 35: GS 2027 Global GDP Forecasts vs. Other Forecasters Thank you to Jamal Lawal, intern on the Global Economics team, for his contributions to this report. #"
  },
  {
    "figure_id": "F133",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Global market performance MSCI Indices, 1-week price return (USD, %) Exhibit 2: World equity indices USD, indexed price performance Exhibit 3: MSCI AC World sector performance MSCI Indices, 1-week price return (USD,"
  },
  {
    "figure_id": "F134",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 4: Cross-asset performance MSCI Indices, 1-week price return (USD, %)"
  },
  {
    "figure_id": "F135",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: World equity indices USD, indexed price performance Exhibit 3: MSCI AC World sector performance MSCI Indices, 1-week price return (USD, %) Exhibit 4: Cross-asset performance MSCI Indices, 1-week price return (USD, %)"
  },
  {
    "figure_id": "F136",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 3: MSCI AC World sector performance MSCI Indices, 1-week price return (USD, %) Exhibit 4: Cross-asset performance MSCI Indices, 1-week price return (USD, %) ## Forecasts Exhibit 5: GDP growth, % yoy: GS vs. consensus"
  },
  {
    "figure_id": "F137",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 6: GS Macro 3-, 6- and 12-month forecasts Exhibit 7: GS top-down vs. consensus bottom-up estimates of 2026 EPS growth Exhibit 8: GS top-down vs. consensus bottom-up estimates of 2027 EPS growth ## Risk and Sentiment ind"
  },
  {
    "figure_id": "F138",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: GS top-down vs. consensus bottom-up estimates of 2026 EPS growth Exhibit 8: GS top-down vs. consensus bottom-up estimates of 2027 EPS growth ## Risk and Sentiment indicators Exhibit 9: GS Bull/Bear Market Indicator ("
  },
  {
    "figure_id": "F139",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GS top-down vs. consensus bottom-up estimates of 2027 EPS growth ## Risk and Sentiment indicators Exhibit 9: GS Bull/Bear Market Indicator (GSBLBR) GS Bull/Bear Market Indicator = Average percentile Note: 100 $^{th}$"
  },
  {
    "figure_id": "F140",
    "report_id": "R008",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Risk Appetite Indicator (GSRAII) Exhibit 12: Percentile of sentiment indicators Data since 2007 ## Performance - Local indices"
  },
  {
    "figure_id": "F141",
    "report_id": "R008",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Percentile of sentiment indicators Data since 2007 ## Performance - Local indices Exhibit 13: Global equity market performance (local indices)"
  },
  {
    "figure_id": "F142",
    "report_id": "R008",
    "label": "Exhibit 16",
    "context": "Exhibit 16: 12m trailing return contribution 12m trailing return in local currency Exhibit 17: MSCI AC World 12m trailing return contribution by sector/style 12m trailing return in USD Exhibit 18: Sales growth, EPS growth and ne"
  },
  {
    "figure_id": "F143",
    "report_id": "R008",
    "label": "Exhibit 16",
    "context": "Exhibit 16: 12m trailing return contribution 12m trailing return in local currency Exhibit 17: MSCI AC World 12m trailing return contribution by sector/style 12m trailing return in USD Exhibit 18: Sales growth, EPS growth and ne"
  },
  {
    "figure_id": "F144",
    "report_id": "R008",
    "label": "Exhibit 19",
    "context": "Exhibit 19: MSCI AC World EPS Consensus estimates in USD ## Earnings revisions Exhibit 20: 2026 EPS revisions Indexed to 100. Local currency"
  },
  {
    "figure_id": "F145",
    "report_id": "R008",
    "label": "Exhibit 20",
    "context": "Exhibit 20: 2026 EPS revisions Indexed to 100. Local currency Exhibit 21: 2026 Earnings Sentiment (nb upgrades - nb downgrades) / nb estimates over the past month Exhibit 22: 3-month EPS revision"
  },
  {
    "figure_id": "F146",
    "report_id": "R008",
    "label": "Exhibit 20",
    "context": "Exhibit 23: Year-to-date EPS revisions MSCI AC World sectors and Global Regions. Local currency"
  },
  {
    "figure_id": "F147",
    "report_id": "R008",
    "label": "Exhibit 21",
    "context": "Exhibit 21: 2026 Earnings Sentiment (nb upgrades - nb downgrades) / nb estimates over the past month Exhibit 22: 3-month EPS revision MSCI AC World sectors and Global Regions. Local currency Exhibit 23: Year-to-date EPS revision"
  },
  {
    "figure_id": "F148",
    "report_id": "R008",
    "label": "Exhibit 22",
    "context": "Exhibit 22: 3-month EPS revision MSCI AC World sectors and Global Regions. Local currency Exhibit 23: Year-to-date EPS revisions MSCI AC World sectors and Global Regions. Local currency ## Valuation Exhibit 24: 12m and 24m fwd M"
  },
  {
    "figure_id": "F149",
    "report_id": "R008",
    "label": "Exhibit 24",
    "context": "Exhibit 24: 12m and 24m fwd MSCI AC World stock valuation 12m and 24m fwd P/E Exhibit 25: Global market implied ERP (%) Exhibit 26: MSCI Regions valuations 12-month forward P/Es relative to the last 20 years - STOXX 600 P/E for"
  },
  {
    "figure_id": "F150",
    "report_id": "R008",
    "label": "Exhibit 24",
    "context": "Exhibit 27: MSCI World sector/style valuations"
  },
  {
    "figure_id": "F151",
    "report_id": "R008",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Global market implied ERP (%) Exhibit 26: MSCI Regions valuations 12-month forward P/Es relative to the last 20 years - STOXX 600 P/E for Europe Exhibit 27: MSCI World sector/style valuations 12-month forward P/Es re"
  },
  {
    "figure_id": "F152",
    "report_id": "R008",
    "label": "Exhibit 26",
    "context": "Exhibit 28: Value vs. Growth MSCI Indices relative price return (USD)"
  },
  {
    "figure_id": "F153",
    "report_id": "R008",
    "label": "Exhibit 28",
    "context": "Exhibit 30: Cyclicals vs. Defensives MSCI Indices relative price return (USD)"
  },
  {
    "figure_id": "F154",
    "report_id": "R008",
    "label": "Exhibit 28",
    "context": "Exhibit 30: Cyclicals vs. Defensives MSCI Indices relative price return (USD)"
  },
  {
    "figure_id": "F155",
    "report_id": "R008",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Cyclicals vs. Defensives MSCI Indices relative price return (USD) Exhibit 31: Momentum vs. Market MSCI Momentum Indices relative price return (USD)"
  },
  {
    "figure_id": "F156",
    "report_id": "R008",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Cyclicals vs. Defensives MSCI Indices relative price return (USD) Exhibit 31: Momentum vs. Market MSCI Momentum Indices relative price return (USD) ## Style valuation Exhibit 32: Value vs. Growth 12m fwd P/E Premium"
  },
  {
    "figure_id": "F157",
    "report_id": "R008",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Value vs. Growth 12m fwd P/E Premium (or Discount) Exhibit 33: Small vs. Large 12m fwd P/E Premium (or Discount) Exhibit 34: Cyclicals vs. Defensives"
  },
  {
    "figure_id": "F158",
    "report_id": "R008",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Value vs. Growth 12m fwd P/E Premium (or Discount) Exhibit 33: Small vs. Large 12m fwd P/E Premium (or Discount) Exhibit 34: Cyclicals vs. Defensives 12m fwd P/E Premium (or Discount) Exhibit 35: Momentum vs. Marke"
  },
  {
    "figure_id": "F159",
    "report_id": "R008",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Small vs. Large 12m fwd P/E Premium (or Discount) Exhibit 34: Cyclicals vs. Defensives 12m fwd P/E Premium (or Discount) Exhibit 35: Momentum vs. Market 12m fwd P/E Premium (or Discount)"
  },
  {
    "figure_id": "F160",
    "report_id": "R008",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Cyclicals vs. Defensives 12m fwd P/E Premium (or Discount) Exhibit 35: Momentum vs. Market 12m fwd P/E Premium (or Discount) ## Sector weights, geographical exposure and concentration Exhibit 36: Index sector composi"
  },
  {
    "figure_id": "F161",
    "report_id": "R008",
    "label": "Exhibit 37",
    "context": "Exhibit 37: GS recommended sector weightings by region Exhibit 38: Geographical Sales Exposure MSCI Indices. See our Portfolio Passport 2024. Exhibit 39: Country Composition MSCI AC World Index ## Cross-asset performance and cor"
  },
  {
    "figure_id": "F162",
    "report_id": "R008",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Geographical Sales Exposure MSCI Indices. See our Portfolio Passport 2024. Exhibit 39: Country Composition MSCI AC World Index ## Cross-asset performance and correlation Exhibit 40: Performance of equities, bonds and"
  },
  {
    "figure_id": "F163",
    "report_id": "R008",
    "label": "Exhibit 40",
    "context": "Exhibit 42: 3m correlation of weekly returns with GSCI Total Return Index"
  },
  {
    "figure_id": "F164",
    "report_id": "R008",
    "label": "Exhibit 40",
    "context": "Exhibit 42: 3m correlation of weekly returns with GSCI Total Return Index Correlation vs. GSCI Commodities Total Return Index Exhibit 43: 3m rolling equity/FX correlation of weekly returns"
  },
  {
    "figure_id": "F165",
    "report_id": "R008",
    "label": "Exhibit 41",
    "context": "Exhibit 43: 3m rolling equity/FX correlation of weekly returns S&P 500 vs. GS USD TWI; EURO STOXX 50 vs. EUR/USD; Topix vs. JPY/USD; MSCI EM vs. GS USD TWI ## Flows from Global investors into equity funds"
  },
  {
    "figure_id": "F166",
    "report_id": "R008",
    "label": "Exhibit 42",
    "context": "Exhibit 44: Monthly flows from Global investors into DM and EM equity funds In USD bn."
  },
  {
    "figure_id": "F167",
    "report_id": "R008",
    "label": "Exhibit 43",
    "context": "Exhibit 45: Cumulative flows into equity by regions Monthly flows, USD bn. EPFR Country Flows (weekly data for current month). Exhibit 46: Calendarised flows from Global investors into DM and EM equity funds"
  },
  {
    "figure_id": "F168",
    "report_id": "R008",
    "label": "Exhibit 44",
    "context": "Exhibit 47: Cumulative flows from Global investors into DM and EM funds"
  },
  {
    "figure_id": "F169",
    "report_id": "R008",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Cumulative flows into equity by regions Monthly flows, USD bn. EPFR Country Flows (weekly data for current month). Exhibit 46: Calendarised flows from Global investors into DM and EM equity funds In USD bn Exhibit 47"
  },
  {
    "figure_id": "F170",
    "report_id": "R008",
    "label": "Exhibit 46",
    "context": "Exhibit 49: 2026 earnings sentiment % for MSCI The World and EM"
  },
  {
    "figure_id": "F171",
    "report_id": "R008",
    "label": "Exhibit 47",
    "context": "Exhibit 50: EM vs. DM valuation"
  },
  {
    "figure_id": "F172",
    "report_id": "R008",
    "label": "Exhibit 49",
    "context": "Exhibit 49: 2026 earnings sentiment % for MSCI The World and EM Earnings sentiment = (upgrades – downgrades) / total estimates on all stocks Exhibit 50: EM vs. DM valuation 12-month forward P/E Premium (Discount) Exhibit 51: EM"
  },
  {
    "figure_id": "F173",
    "report_id": "R008",
    "label": "Exhibit 49",
    "context": "Exhibit 49: 2026 earnings sentiment % for MSCI The World and EM Earnings sentiment = (upgrades – downgrades) / total estimates on all stocks Exhibit 50: EM vs. DM valuation 12-month forward P/E Premium (Discount) Exhibit 51: EM"
  },
  {
    "figure_id": "F174",
    "report_id": "R008",
    "label": "Exhibit 50",
    "context": "Exhibit 50: EM vs. DM valuation 12-month forward P/E Premium (Discount) Exhibit 51: EM vs. DM Cumulative flows (% Total Net Assets) Monthly flows, EPFR Country Flows (weekly data for current month). ## Vol, skew and dividends Ex"
  },
  {
    "figure_id": "F175",
    "report_id": "R008",
    "label": "Exhibit 51",
    "context": "Exhibit 54: 2026 dividend markets, rebased to 100"
  },
  {
    "figure_id": "F176",
    "report_id": "R008",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Implied volatility of 3-month atms Exhibit 53: 3-month normalised skew Exhibit 54: 2026 dividend markets, rebased to 100 Exhibit 55: 2026 implied dividend yield"
  },
  {
    "figure_id": "F177",
    "report_id": "R008",
    "label": "Exhibit 53",
    "context": "Exhibit 53: 3-month normalised skew Exhibit 54: 2026 dividend markets, rebased to 100 Exhibit 55: 2026 implied dividend yield ## Disclosure Appendix"
  },
  {
    "figure_id": "F178",
    "report_id": "R008",
    "label": "Exhibit 54",
    "context": "Exhibit 54: 2026 dividend markets, rebased to 100 Exhibit 55: 2026 implied dividend yield ## Disclosure Appendix ## Reg AC We, Guillaume Jaisson, Peter Oppenheimer, Sharon Bell, John Kwon, Giovanni Ferrannini and Elena Porfidia,"
  },
  {
    "figure_id": "F179",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 3: Tech leadership has become increasingly linked to AI-related optimism and less about real rates"
  },
  {
    "figure_id": "F180",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Tech leadership has become increasingly linked to AI-related optimism and less about real rates Exhibit 4: Gold vol is expensive versus other downside hedges Ratio of 3-month 25d volatility"
  },
  {
    "figure_id": "F181",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 5: Markets are pricing a stickier front-end by year-end Option-implied probability of US 2y rate more than +/- 50bps from spot in 6 months."
  },
  {
    "figure_id": "F182",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 6: Top hedges in a ‘rate shock’ scenario 1m return/vol implied by the beta to 2 sd. move in RAI “PC2”"
  },
  {
    "figure_id": "F183",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Top hedges in a ‘rate shock’ scenario 1m return/vol implied by the beta to 2 sd. move in RAI “PC2” ## Cross-asset: Forecasts"
  },
  {
    "figure_id": "F184",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 7: GOAL asset allocation recommendations and GS cross-asset forecasts"
  },
  {
    "figure_id": "F185",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 7: GOAL asset allocation recommendations and GS cross-asset forecasts ## Cross-asset: Weekly and YTD performance, absolute and risk-adjusted ## Cross-asset: Risk appetite indicator Exhibit 10: Risk appetite indicator le"
  },
  {
    "figure_id": "F186",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Risk appetite indicator level and momentum factors"
  },
  {
    "figure_id": "F187",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Risk appetite indicator level and momentum factors Exhibit 11: Risk appetite indicators for different asset classes Exhibit 12: Cyclicals vs. defensives 1-year rolling z-score across regions"
  },
  {
    "figure_id": "F188",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Risk appetite indicator level and momentum factors Exhibit 11: Risk appetite indicators for different asset classes Exhibit 12: Cyclicals vs. defensives 1-year rolling z-score across regions Exhibit 13: Sub-compone"
  },
  {
    "figure_id": "F189",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Risk appetite indicators for different asset classes Exhibit 12: Cyclicals vs. defensives 1-year rolling z-score across regions Exhibit 13: Sub-components of equity risk appetite indicator ## Cross-asset: Risk Appe"
  },
  {
    "figure_id": "F190",
    "report_id": "R011",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Cyclicals vs. defensives 1-year rolling z-score across regions Exhibit 13: Sub-components of equity risk appetite indicator ## Cross-asset: Risk Appetite principal component analysis Exhibit 14: GS RAI principal comp"
  },
  {
    "figure_id": "F191",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14: GS RAI principal component Exhibit 15: PC1: Global growth factor vs. Global MAP Score Exhibit 16: PC2: Monetary policy factor vs. US 10-year TIPS yield"
  },
  {
    "figure_id": "F192",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14: GS RAI principal component Exhibit 15: PC1: Global growth factor vs. Global MAP Score Exhibit 16: PC2: Monetary policy factor vs. US 10-year TIPS yield Exhibit 17: PC3: Dollar factor vs. USD TWI"
  },
  {
    "figure_id": "F193",
    "report_id": "R011",
    "label": "Exhibit 15",
    "context": "Exhibit 15: PC1: Global growth factor vs. Global MAP Score Exhibit 16: PC2: Monetary policy factor vs. US 10-year TIPS yield Exhibit 17: PC3: Dollar factor vs. USD TWI ## Cross-asset: Balanced portfolios and dynamic allocation"
  },
  {
    "figure_id": "F194",
    "report_id": "R011",
    "label": "Exhibit 16",
    "context": "Exhibit 16: PC2: Monetary policy factor vs. US 10-year TIPS yield Exhibit 17: PC3: Dollar factor vs. USD TWI ## Cross-asset: Balanced portfolios and dynamic allocation strategies performance Exhibit 18: 60/40 equity/bond portfol"
  },
  {
    "figure_id": "F195",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Risk parity portfolio performance across regions last 12m Weighted inversely by 3m realised volatility of equity and 10y bonds Exhibit 20: 60/40 portfolio with volatility target strategies overlay vs. US 60/40 portfoli"
  },
  {
    "figure_id": "F196",
    "report_id": "R011",
    "label": "Exhibit 18",
    "context": "Exhibit 20: 60/40 portfolio with volatility target strategies overlay vs. US 60/40 portfolio 60% S&P 500, 40% US 10y bond; based on 1m realised S&P 500 volatility Exhibit 21: 60/40 portfolio with volatility target strategies and m"
  },
  {
    "figure_id": "F197",
    "report_id": "R011",
    "label": "Exhibit 19",
    "context": "Exhibit 21: 60/40 portfolio with volatility target strategies and momentum overlay vs. US 60/40 60% S&P 500, 40% US 10y bond; Strategy methodology see: GOAL: The Balanced Bear - Part 2 ## Cross-asset: Equity vs. credit monitor"
  },
  {
    "figure_id": "F198",
    "report_id": "R011",
    "label": "Exhibit 20",
    "context": "Exhibit 22: USD cash credit vs. US equity Cash credit excess returns (beta-adjusted) vs. S&P 500 total returns"
  },
  {
    "figure_id": "F199",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 24: EUR cash credit vs. European equity"
  },
  {
    "figure_id": "F200",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 24: EUR cash credit vs. European equity Cash credit excess returns (beta-adjusted) vs. MSCI Europe total returns Exhibit 25: EUR synthetic credit vs. European equity"
  },
  {
    "figure_id": "F201",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 25: EUR synthetic credit vs. European equity Synthetic credit excess returns (beta-adjusted) vs. MSCI Europe total returns Exhibit 26: EM cash credit vs. EM equity"
  },
  {
    "figure_id": "F202",
    "report_id": "R011",
    "label": "Exhibit 24",
    "context": "Exhibit 26: EM cash credit vs. EM equity Cash credit excess returns (beta-adjusted) vs. MSCI EM total returns Exhibit 27: EM synthetic credit vs. EM equity"
  },
  {
    "figure_id": "F203",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 27: EM synthetic credit vs. EM equity Synthetic credit excess returns (beta-adjusted) vs. MSCI EM total returns ## Cross-asset: Valuation and risk premia"
  },
  {
    "figure_id": "F204",
    "report_id": "R011",
    "label": "Exhibit 26",
    "context": "Exhibit 26: EM cash credit vs. EM equity Cash credit excess returns (beta-adjusted) vs. MSCI EM total returns Exhibit 27: EM synthetic credit vs. EM equity Synthetic credit excess returns (beta-adjusted) vs. MSCI EM total returns"
  },
  {
    "figure_id": "F205",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Credit spread minus equity risk premium estimates across markets Equity risk premia based on 1-stage DDM using local 10-year yields and LT GDP consensus estimates. Using past 10 years of data. Exhibit 30: Equity vs. cr"
  },
  {
    "figure_id": "F206",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 31: Current yields across assets and their percentile to the past 10 years"
  },
  {
    "figure_id": "F207",
    "report_id": "R011",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Current yields across assets and their percentile to the past 10 years Exhibit 32: Past week change in yields across assets Exhibit 33: YTD change in yields across assets ## Cross-asset: Sentiment and Positioning"
  },
  {
    "figure_id": "F208",
    "report_id": "R011",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Past week change in yields across assets Exhibit 33: YTD change in yields across assets ## Cross-asset: Sentiment and Positioning Exhibit 34: Percentile of sentiment indicators Data since 2007"
  },
  {
    "figure_id": "F209",
    "report_id": "R011",
    "label": "Exhibit 33",
    "context": "Exhibit 33: YTD change in yields across assets ## Cross-asset: Sentiment and Positioning Exhibit 34: Percentile of sentiment indicators Data since 2007 Exhibit 35: Average percentile of sentiment indicators Data since 2007 Exh"
  },
  {
    "figure_id": "F210",
    "report_id": "R011",
    "label": "Exhibit 34",
    "context": "Exhibit 37: Risky vs. safe assets fund flows"
  },
  {
    "figure_id": "F211",
    "report_id": "R011",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Average percentile of sentiment indicators Data since 2007 Exhibit 36: Cumulative fund flows across assets Monthly flows (\\$bn). MTD sum of weekly flows when monthly not yet available Exhibit 37: Risky vs. safe asset"
  },
  {
    "figure_id": "F212",
    "report_id": "R011",
    "label": "Exhibit 36",
    "context": "Exhibit 38: YTD cross-asset global fund flows All funds reporting monthly. MTD sum of weekly flows when monthly not yet available (\\$bn)"
  },
  {
    "figure_id": "F213",
    "report_id": "R011",
    "label": "Exhibit 38",
    "context": "Exhibit 40: 1-week cross-asset global fund flows"
  },
  {
    "figure_id": "F214",
    "report_id": "R011",
    "label": "Exhibit 38",
    "context": "Exhibit 40: 1-week cross-asset global fund flows All funds reporting weekly Exhibit 41: 4-week cross-asset global fund flows All funds reporting weekly"
  },
  {
    "figure_id": "F215",
    "report_id": "R011",
    "label": "Exhibit 39",
    "context": "Exhibit 39: YTD cross-asset global fund flows All funds reporting monthly. MTD sum of weekly flows when monthly not yet available (% of AUM) Exhibit 40: 1-week cross-asset global fund flows All funds reporting weekly Exhibit 41:"
  },
  {
    "figure_id": "F216",
    "report_id": "R011",
    "label": "Exhibit 40",
    "context": "Exhibit 40: 1-week cross-asset global fund flows All funds reporting weekly Exhibit 41: 4-week cross-asset global fund flows All funds reporting weekly ## Cross-asset: CFTC positioning Exhibit 42: Equity net long positioning Lev"
  },
  {
    "figure_id": "F217",
    "report_id": "R011",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Equity net long positioning Leveraged funds and asset managers net future positions (\\$ bn) Exhibit 43: Currency net long positioning Net non-commercial positions (\\$ bn) Exhibit 44: Commodity net long positioning"
  },
  {
    "figure_id": "F218",
    "report_id": "R011",
    "label": "Exhibit 42",
    "context": "Exhibit 45: US Treasury net long positioning"
  },
  {
    "figure_id": "F219",
    "report_id": "R011",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Currency net long positioning Net non-commercial positions (\\$ bn) Exhibit 44: Commodity net long positioning Net non-commercial positions (\\$ bn) Exhibit 45: US Treasury net long positioning Net non-commercial posit"
  },
  {
    "figure_id": "F220",
    "report_id": "R011",
    "label": "Exhibit 44",
    "context": "Exhibit 46: 3m rolling equity vol/CDS correlation of weekly level changes CDX HY for the US, iTraxx Xover for Europe; ATM implied vol for S&P 500 and Euro Stoxx 50"
  },
  {
    "figure_id": "F221",
    "report_id": "R011",
    "label": "Exhibit 46",
    "context": "Exhibit 48: 3m rolling equity/bond correlation of weekly returns"
  },
  {
    "figure_id": "F222",
    "report_id": "R011",
    "label": "Exhibit 46",
    "context": "Exhibit 48: 3m rolling equity/bond correlation of weekly returns Exhibit 49: 3m rolling equity/FX correlation of weekly returns"
  },
  {
    "figure_id": "F223",
    "report_id": "R011",
    "label": "Exhibit 47",
    "context": "Exhibit 47: 3m rolling commodity price correlations of weekly % changes with different assets Exhibit 48: 3m rolling equity/bond correlation of weekly returns Exhibit 49: 3m rolling equity/FX correlation of weekly returns ## C"
  },
  {
    "figure_id": "F224",
    "report_id": "R011",
    "label": "Exhibit 48",
    "context": "Exhibit 48: 3m rolling equity/bond correlation of weekly returns Exhibit 49: 3m rolling equity/FX correlation of weekly returns ## Cross-asset: Correlation matrix ## Exhibit 50: Cross-asset correlation matrix Upper half of matri"
  },
  {
    "figure_id": "F225",
    "report_id": "R011",
    "label": "Exhibit 51",
    "context": "Exhibit 53: Putwing and Callwing normalised skew 5y percentile Normalised skew = (impl. vol 25 delta put/call minus implied vol 50 delta call)/50 delta call ## Cross-asset: Volatility, skew, CDS with equity vol, rate vol"
  },
  {
    "figure_id": "F226",
    "report_id": "R011",
    "label": "Exhibit 52",
    "context": "Exhibit 54: ATM implied volatility term structure for equity indices"
  },
  {
    "figure_id": "F227",
    "report_id": "R011",
    "label": "Exhibit 53",
    "context": "Exhibit 55: Normalised implied volatility skew across regions 3m 25 delta put vol minus 25 delta call vol scaled by ATM implied vol Exhibit 56: CDS and equity vol levels in the US"
  },
  {
    "figure_id": "F228",
    "report_id": "R011",
    "label": "Exhibit 54",
    "context": "Exhibit 57: 3m ATM implied rate volatility across regions"
  },
  {
    "figure_id": "F229",
    "report_id": "R011",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Normalised implied volatility skew across regions 3m 25 delta put vol minus 25 delta call vol scaled by ATM implied vol Exhibit 56: CDS and equity vol levels in the US CDX HY, 3m ATM S&P 500 implied vol Exhibit 57: 3"
  },
  {
    "figure_id": "F230",
    "report_id": "R011",
    "label": "Exhibit 56",
    "context": "Exhibit 56: CDS and equity vol levels in the US CDX HY, 3m ATM S&P 500 implied vol Exhibit 57: 3m ATM implied rate volatility across regions 3-month implied volatility of 10-year rates (bp/day) ## Cross-asset: Liquidity indicato"
  },
  {
    "figure_id": "F231",
    "report_id": "R011",
    "label": "Exhibit 57",
    "context": "Exhibit 57: 3m ATM implied rate volatility across regions 3-month implied volatility of 10-year rates (bp/day) ## Cross-asset: Liquidity indicators Exhibit 60: Top-of-book depth 5-day average, \\$ mln E-MINI S&P 500 = 5d avg."
  },
  {
    "figure_id": "F232",
    "report_id": "R011",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Top-of-book depth 5-day average, \\$ mln E-MINI S&P 500 = 5d avg. # of contracts \\* S&P 500 price \\* \\$50. 10-year T-note = 5d avg. # of contracts \\* \\$100,000"
  },
  {
    "figure_id": "F233",
    "report_id": "R011",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Top-of-book depth 5-day average, \\$ mln E-MINI S&P 500 = 5d avg. # of contracts \\* S&P 500 price \\* \\$50. 10-year T-note = 5d avg. # of contracts \\* \\$100,000 Exhibit 61: US financial institutions wholesale funding cos"
  },
  {
    "figure_id": "F234",
    "report_id": "R011",
    "label": "Exhibit 60",
    "context": "Exhibit 62: Market-implied US recession probability Average of univariate logit models on the right. Orange shade: NBER recession"
  },
  {
    "figure_id": "F235",
    "report_id": "R011",
    "label": "Exhibit 62",
    "context": "Exhibit 64: Probability of a US recession in the next 1 year"
  },
  {
    "figure_id": "F236",
    "report_id": "R011",
    "label": "Exhibit 62",
    "context": "Exhibit 64: Probability of a US recession in the next 1 year Exhibit 65: Market-implied path of the Fed Funds rate Based on 30-day Fed Funds futures"
  },
  {
    "figure_id": "F237",
    "report_id": "R011",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Market-implied US recession probability by indicator Univariate logit models. Maximum history since 1950 Exhibit 64: Probability of a US recession in the next 1 year Exhibit 65: Market-implied path of the Fed Funds r"
  },
  {
    "figure_id": "F238",
    "report_id": "R011",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Probability of a US recession in the next 1 year Exhibit 65: Market-implied path of the Fed Funds rate Based on 30-day Fed Funds futures ## Equity: Drawdown probability Exhibit 66: Implied probability of S&P 500 draw"
  },
  {
    "figure_id": "F239",
    "report_id": "R011",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Implied probability of S&P 500 drawdown based on multi-variate logit model Based on Shapley values. Inputs aggregated by type Exhibit 68: Implied probability of S&P 500 rally based on multi-variate logit model"
  },
  {
    "figure_id": "F240",
    "report_id": "R011",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Implied probability of S&P 500 drawdown based on multi-variate logit model Based on Shapley values. Inputs aggregated by type Exhibit 68: Implied probability of S&P 500 rally based on multi-variate logit model Base"
  },
  {
    "figure_id": "F241",
    "report_id": "R011",
    "label": "Exhibit 67",
    "context": "Exhibit 68: Implied probability of S&P 500 rally based on multi-variate logit model Based on Shapley values. Inputs aggregated by type ## Equity: Valuation and styles"
  },
  {
    "figure_id": "F242",
    "report_id": "R011",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Implied probability of S&P 500 rally based on multi-variate logit model Based on Shapley values. Inputs aggregated by type ## Equity: Valuation and styles Exhibit 70: Valuation ranges of MSCI World styles indices 12-"
  },
  {
    "figure_id": "F243",
    "report_id": "R011",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Valuation ranges of MSCI World styles indices 12-month forward P/Es relative to the last 10 years Exhibit 71: MSCI World sector valuations 12-month forward P/Es relative to the last 10 years Exhibit 72: Global market"
  },
  {
    "figure_id": "F244",
    "report_id": "R011",
    "label": "Exhibit 70",
    "context": "Exhibit 73: MSCI World style index performance"
  },
  {
    "figure_id": "F245",
    "report_id": "R011",
    "label": "Exhibit 71",
    "context": "Exhibit 73: MSCI World style index performance Performance indexed to 100 12m ago ## Equity: Earnings"
  },
  {
    "figure_id": "F246",
    "report_id": "R011",
    "label": "Exhibit 72",
    "context": "Exhibit 74: 1-month revision to I/B/E/S consensus earnings MSCI World sectors, other global equity index aggregates"
  },
  {
    "figure_id": "F247",
    "report_id": "R011",
    "label": "Exhibit 74",
    "context": "Exhibit 74: 1-month revision to I/B/E/S consensus earnings MSCI World sectors, other global equity index aggregates Exhibit 75: 6-month revision to I/B/E/S consensus earnings MSCI World sectors, other global equity index aggregate"
  },
  {
    "figure_id": "F248",
    "report_id": "R011",
    "label": "Exhibit 74",
    "context": "Exhibit 77: FY1 consensus earnings expectations over the past 12 months"
  },
  {
    "figure_id": "F249",
    "report_id": "R011",
    "label": "Exhibit 75",
    "context": "Exhibit 75: 6-month revision to I/B/E/S consensus earnings MSCI World sectors, other global equity index aggregates 1-month moving average of net monthly upgrades Exhibit 77: FY1 consensus earnings expectations over the past 12"
  },
  {
    "figure_id": "F250",
    "report_id": "R011",
    "label": "Exhibit 76",
    "context": "Exhibit 77: FY1 consensus earnings expectations over the past 12 months Earnings indexed to 100 12 months ago ## Government bonds: Yield curves Exhibit 79: German yield curve dynamics Current relative to 1 month and 3 months ago"
  },
  {
    "figure_id": "F251",
    "report_id": "R011",
    "label": "Exhibit 77",
    "context": "Exhibit 80: Japan yield curve dynamics Current relative to 1 month and 3 months ago"
  },
  {
    "figure_id": "F252",
    "report_id": "R011",
    "label": "Exhibit 79",
    "context": "Exhibit 79: German yield curve dynamics Current relative to 1 month and 3 months ago Exhibit 80: Japan yield curve dynamics Current relative to 1 month and 3 months ago Exhibit 81: Yield curve term slope across regions"
  },
  {
    "figure_id": "F253",
    "report_id": "R011",
    "label": "Exhibit 79",
    "context": "Exhibit 79: German yield curve dynamics Current relative to 1 month and 3 months ago Exhibit 80: Japan yield curve dynamics Current relative to 1 month and 3 months ago Exhibit 81: Yield curve term slope across regions ## Gove"
  },
  {
    "figure_id": "F254",
    "report_id": "R011",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Japan yield curve dynamics Current relative to 1 month and 3 months ago Exhibit 81: Yield curve term slope across regions ## Government bonds: Real yields, inflation, breakevens, 10y IR differentials Exhibit 82: 10y"
  },
  {
    "figure_id": "F255",
    "report_id": "R011",
    "label": "Exhibit 81",
    "context": "Exhibit 83: 10y inflation swaps across regions CPI inflation swap (RPI for the UK) Exhibit 84: US breakeven inflation"
  },
  {
    "figure_id": "F256",
    "report_id": "R011",
    "label": "Exhibit 82",
    "context": "Exhibit 85: 10y nominal bond yield differentials"
  },
  {
    "figure_id": "F257",
    "report_id": "R011",
    "label": "Exhibit 83",
    "context": "Exhibit 83: 10y inflation swaps across regions CPI inflation swap (RPI for the UK) Exhibit 84: US breakeven inflation Nominal yield minus TIPS yield Exhibit 85: 10y nominal bond yield differentials ## Commodities: Curve shapes"
  },
  {
    "figure_id": "F258",
    "report_id": "R011",
    "label": "Exhibit 84",
    "context": "Exhibit 84: US breakeven inflation Nominal yield minus TIPS yield Exhibit 85: 10y nominal bond yield differentials ## Commodities: Curve shapes and roll yields Exhibit 87: Gold price and US real yields"
  },
  {
    "figure_id": "F259",
    "report_id": "R011",
    "label": "Exhibit 85",
    "context": "Exhibit 85: 10y nominal bond yield differentials ## Commodities: Curve shapes and roll yields Exhibit 87: Gold price and US real yields US 10-year TIPs yield, Gold U\\$/ounce Exhibit 88: S&P GSCI spot, roll and total returns"
  },
  {
    "figure_id": "F260",
    "report_id": "R011",
    "label": "Exhibit 87",
    "context": "Exhibit 87: Gold price and US real yields US 10-year TIPs yield, Gold U\\$/ounce Exhibit 88: S&P GSCI spot, roll and total returns Returns over the past 1 week, 3 months and 1 year Exhibit 89: Recent performance of S&P GSCI secto"
  },
  {
    "figure_id": "F261",
    "report_id": "R011",
    "label": "Exhibit 87",
    "context": "Exhibit 87: Gold price and US real yields US 10-year TIPs yield, Gold U\\$/ounce Exhibit 88: S&P GSCI spot, roll and total returns Returns over the past 1 week, 3 months and 1 year Exhibit 89: Recent performance of S&P GSCI secto"
  },
  {
    "figure_id": "F262",
    "report_id": "R011",
    "label": "Exhibit 89",
    "context": "Exhibit 91: Recent performance of dollar crosses Percentage change over past 1 week, 3 months Exhibit 92: EUR/USD against German - US 2y interest rate differentials past 3m"
  },
  {
    "figure_id": "F263",
    "report_id": "R011",
    "label": "Exhibit 90",
    "context": "Exhibit 93: USD/JPY against US - Japan 2y interest rate differentials past 3m"
  },
  {
    "figure_id": "F264",
    "report_id": "R011",
    "label": "Exhibit 91",
    "context": "Exhibit 91: Recent performance of dollar crosses Percentage change over past 1 week, 3 months Exhibit 92: EUR/USD against German - US 2y interest rate differentials past 3m Exhibit 93: USD/JPY against US - Japan 2y interest rate"
  },
  {
    "figure_id": "F265",
    "report_id": "R011",
    "label": "Exhibit 92",
    "context": "Exhibit 92: EUR/USD against German - US 2y interest rate differentials past 3m Exhibit 93: USD/JPY against US - Japan 2y interest rate differentials past 3m ## Disclosure Appendix ## Reg AC We, Christian Mueller-Glissmann, CFA,"
  },
  {
    "figure_id": "F266",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Coal retirement delays since 2025 have effectively increased power supply in the next few years, but are more constrained going forward"
  },
  {
    "figure_id": "F267",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Coal retirement delays since 2025 have effectively increased power supply in the next few years, but are more constrained going forward Based on EIA generator schedules released in late May 2026, which do not include s"
  },
  {
    "figure_id": "F268",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 3: ERCOT (Texas) early summer power price remains weak yoy, remaining below 60 USD/MWh ERCOT North 345kV Hub peak load prices"
  },
  {
    "figure_id": "F269",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ERCOT (Texas) early summer power price remains weak yoy, remaining below 60 USD/MWh ERCOT North 345kV Hub peak load prices Exhibit 4: Power prices in PJM (Mid-Atlantic) rally into the 90 USD/MWh range with the forward"
  },
  {
    "figure_id": "F270",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 5: The PJM (Mid-Atlantic) power market was tightened by heatwaves into June Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a giv"
  },
  {
    "figure_id": "F271",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Exhibit 6: The MISO (Mid-Continental) power market also turned tighter into June before softening this week Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capaci"
  },
  {
    "figure_id": "F272",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 7: The ERCOT (Texas) power market maintained a soft balance with mild weather Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a g"
  },
  {
    "figure_id": "F273",
    "report_id": "R012",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Total US yoy power demand growth strengthens to $2.3\\%$ in March, but still below the annual yoy growth rate of $2.4\\%$ in 2025"
  },
  {
    "figure_id": "F274",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 10: The commercial sector continues to be the strongest sector in power demand growth in Jan-Mar2026 with a $2.7\\%$ yoy growth rate"
  },
  {
    "figure_id": "F275",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 10: The commercial sector continues to be the strongest sector in power demand growth in Jan-Mar2026 with a $2.7\\%$ yoy growth rate Not weather adjusted Exhibit 11: After a weak start of the year in Jan2026, US residential"
  },
  {
    "figure_id": "F276",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 11: After a weak start of the year in Jan2026, US residential power demand remained flattish yoy in Feb-Mar Not weather adjusted"
  },
  {
    "figure_id": "F277",
    "report_id": "R012",
    "label": "Exhibit 10",
    "context": "Exhibit 12: Industrial power demand strengthened into March after Jan-Feb2026 yoy weakness Not weather adjusted"
  },
  {
    "figure_id": "F278",
    "report_id": "R012",
    "label": "Exhibit 11",
    "context": "Exhibit 13: US power demand growth remained below US GDP growth through Apr2026 Weather-adjusted US total power demand (including small-scale solar power use) and US real GDP yoy, monthly To avoid underestimating power demand, we"
  },
  {
    "figure_id": "F279",
    "report_id": "R012",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Estimated data center power demand in Virginia continued to edge higher Not weather adjusted"
  },
  {
    "figure_id": "F280",
    "report_id": "R012",
    "label": "Exhibit 13",
    "context": "Exhibit 14: Estimated data center power demand in Virginia continued to edge higher Not weather adjusted Exhibit 15: US data center capacity continued to grow, which we expect to accelerate in June and also in 2H2026 Exhibit 16:"
  },
  {
    "figure_id": "F281",
    "report_id": "R012",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Estimated data center power demand in Virginia continued to edge higher Not weather adjusted Exhibit 15: US data center capacity continued to grow, which we expect to accelerate in June and also in 2H2026 Exhibit 16:"
  },
  {
    "figure_id": "F282",
    "report_id": "R012",
    "label": "Exhibit 15",
    "context": "Exhibit 17: Ohio, Texas, and Virginia are leading data center development in 2026Q2 Data Center Capacity Additions Across US States in 2026Q2 Exhibit 18: We expect significant data center growth acceleration in both the US nationa"
  },
  {
    "figure_id": "F283",
    "report_id": "R012",
    "label": "Exhibit 16",
    "context": "Exhibit 18: We expect significant data center growth acceleration in both the US national and key regional power markets in 2026/27 Exhibit 19: Construction employment related to US data center expansion continued its growing tren"
  },
  {
    "figure_id": "F284",
    "report_id": "R012",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Construction employment related to US data center expansion continued its growing trend ## Supply"
  },
  {
    "figure_id": "F285",
    "report_id": "R012",
    "label": "Exhibit 18",
    "context": "Exhibit 20: US total power generation stayed in line in most of May before gaining strength into early-summer"
  },
  {
    "figure_id": "F286",
    "report_id": "R012",
    "label": "Exhibit 20",
    "context": "Exhibit 20: US total power generation stayed in line in most of May before gaining strength into early-summer Not weather adjusted Exhibit 21: After adjusting for weather, US total power generation holds in line with early-summer"
  },
  {
    "figure_id": "F287",
    "report_id": "R012",
    "label": "Exhibit 20",
    "context": "Exhibit 22: The thermal (natural gas and coal) share in US power supply continues to increase from mid-April given yoy weaker hydro and nuclear Not weather adjusted"
  },
  {
    "figure_id": "F288",
    "report_id": "R012",
    "label": "Exhibit 21",
    "context": "Exhibit 23: Within thermal power generation, the natural gas share remained higher yoy given price competitiveness Not weather adjusted Exhibit 24: US power transmission and distribution losses continued to increase into 2026, tho"
  },
  {
    "figure_id": "F289",
    "report_id": "R012",
    "label": "Exhibit 22",
    "context": "Exhibit 24: US power transmission and distribution losses continued to increase into 2026, though marginally lower in Apr/May Not weather adjusted ## Generation by Fuels"
  },
  {
    "figure_id": "F290",
    "report_id": "R012",
    "label": "Exhibit 23",
    "context": "Exhibit 25: YoY growth in natural gas-fired generation has moved sequentially lower June-to-date vs March and April but remains positive Not weather adjusted"
  },
  {
    "figure_id": "F291",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 26: Higher gas competitiveness keeps coal power generation lower yoy most of the time from mid-Feb to Jun Not weather adjusted"
  },
  {
    "figure_id": "F292",
    "report_id": "R012",
    "label": "Exhibit 25",
    "context": "Exhibit 27: Nuclear power generation turns higher yoy into May and June following April maintenance Not weather adjusted"
  },
  {
    "figure_id": "F293",
    "report_id": "R012",
    "label": "Exhibit 26",
    "context": "Exhibit 28: Wind generation moves higher yoy in May and June Not weather adjusted"
  },
  {
    "figure_id": "F294",
    "report_id": "R012",
    "label": "Exhibit 27",
    "context": "Exhibit 30: Hydro power generation remains weak yoy due to droughts in more than half of the country"
  },
  {
    "figure_id": "F295",
    "report_id": "R012",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Wind generation moves higher yoy in May and June Not weather adjusted Exhibit 29: Solar generation has continued to seasonally ramp up, driven by yoy capacity additions of over 30 GW Exhibit 30: Hydro power generatio"
  },
  {
    "figure_id": "F296",
    "report_id": "R012",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Solar generation has continued to seasonally ramp up, driven by yoy capacity additions of over 30 GW Exhibit 30: Hydro power generation remains weak yoy due to droughts in more than half of the country ## Disclosure"
  },
  {
    "figure_id": "F297",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: May import was \\$2.2 billion Total WFE imports to China by month (USDmn) EXHIBIT 2: Month-over-month showed 20% decline, mostly dragged down by dry etch and others import. Total WFE imports to China MoM growth by segme"
  },
  {
    "figure_id": "F298",
    "report_id": "R013",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 3: The year-over-year figures only show a modest decline, given that weak dry etch and others imports were offset by stronger process control and deposition imports. Total WFE imports to China YoY growth by segment (monthly"
  },
  {
    "figure_id": "F299",
    "report_id": "R013",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: The lithography import was \\$295mn in May 2026, slightly lower than last year Lithography imports to China (monthly) (USDmn)"
  },
  {
    "figure_id": "F300",
    "report_id": "R013",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: The lithography import was \\$295mn in May 2026, slightly lower than last year Lithography imports to China (monthly) (USDmn) EXHIBIT 5: 2026 YTD import -12% YoY Total WFE imports to China by year ## BY REGION & BY EQ"
  },
  {
    "figure_id": "F301",
    "report_id": "R013",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: The lithography import was \\$295mn in May 2026, slightly lower than last year Lithography imports to China (monthly) (USDmn) EXHIBIT 5: 2026 YTD import -12% YoY Total WFE imports to China by year ## BY REGION & BY EQ"
  },
  {
    "figure_id": "F302",
    "report_id": "R013",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: Excluding lithography, there has been a gradual uptick in imports from Singapore and Malaysia to offset the share loss for US, indicating a shift in production for US vendors."
  },
  {
    "figure_id": "F303",
    "report_id": "R013",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: Excluding lithography, there has been a gradual uptick in imports from Singapore and Malaysia to offset the share loss for US, indicating a shift in production for US vendors. Total WFE excl. lithography imports to China"
  },
  {
    "figure_id": "F304",
    "report_id": "R013",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 9: In 2025, imported Lithography intensity just slightly dropped by 1ppt, further declined in 2026 Total WFE imports to China market share by equipment type"
  },
  {
    "figure_id": "F305",
    "report_id": "R013",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 12: Netherlands' lithography imports share increased materially after 2022 and is still increasing in 2025 and onwards Lighography imports to China - share by region (yearly)"
  },
  {
    "figure_id": "F306",
    "report_id": "R013",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 12: Netherlands' lithography imports share increased materially after 2022 and is still increasing in 2025 and onwards Lighography imports to China - share by region (yearly) ## REGRESSION ANALYSIS"
  },
  {
    "figure_id": "F307",
    "report_id": "R013",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Share of lithography imports from Japan has decreased since Aug 2023 and remains relatively low. Lithography imports to China - share by region (monthly) EXHIBIT 12: Netherlands' lithography imports share increased mat"
  },
  {
    "figure_id": "F308",
    "report_id": "R013",
    "label": "Exhibit 14",
    "context": "EXHIBIT 15: The predicted systems sales from China at EUR 0.57bn represents a 52% decline QoQ. This implies China revenue representing only 9% of Q2 total system sales."
  },
  {
    "figure_id": "F309",
    "report_id": "R013",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 15: The predicted systems sales from China at EUR 0.57bn represents a 52% decline QoQ. This implies China revenue representing only 9% of Q2 total system sales."
  },
  {
    "figure_id": "F310",
    "report_id": "R013",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Our estimate for ASML's China system sales in Q2 implies a 52% QoQ decline and a 62% YoY drop, marking the lowest level since the restrictions were introduced. ASML China Quarterly System Sales EXHIBIT 17: Based on our"
  },
  {
    "figure_id": "F311",
    "report_id": "R013",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 18: LRCX 2-month regression yields R2 of 0.86 and should have solid predictive power..."
  },
  {
    "figure_id": "F312",
    "report_id": "R013",
    "label": "Exhibit 18",
    "context": "EXHIBIT 18: LRCX 2-month regression yields R2 of 0.86 and should have solid predictive power... LRCX Quarterly China Sales vs Relevant Semicap Imports to China in 1st & 2nd Months of CQ115-CQ126 EXHIBIT 19: ...with our analysis su"
  },
  {
    "figure_id": "F313",
    "report_id": "R013",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 21: The AMAT 1-month regression yield R2 of 0.70 and hence should have OK predictive power... AMAT Quarterly China Sales vs Relevant Semicap Imports to China in 1st Month of CQ115-CQ126"
  },
  {
    "figure_id": "F314",
    "report_id": "R013",
    "label": "Exhibit 21",
    "context": "EXHIBIT 21: The AMAT 1-month regression yield R2 of 0.70 and hence should have OK predictive power... AMAT Quarterly China Sales vs Relevant Semicap Imports to China in 1st Month of CQ115-CQ126 EXHIBIT 22: ...with our analysis sug"
  },
  {
    "figure_id": "F315",
    "report_id": "R013",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 24: The KLAC 2-month regression yields R2 of 0.92 and hence should have good predictive power... KLAC Quarterly China Sales vs Relevant Semicap Imports to China in 1st & 2nd Months of CQ115-CQ126"
  },
  {
    "figure_id": "F316",
    "report_id": "R013",
    "label": "Exhibit 24",
    "context": "EXHIBIT 24: The KLAC 2-month regression yields R2 of 0.92 and hence should have good predictive power... KLAC Quarterly China Sales vs Relevant Semicap Imports to China in 1st & 2nd Months of CQ115-CQ126 EXHIBIT 25: ...with our an"
  },
  {
    "figure_id": "F317",
    "report_id": "R013",
    "label": "EXHIBIT 26",
    "context": "Exhibit 27-Exhibit 30)."
  },
  {
    "figure_id": "F318",
    "report_id": "R013",
    "label": "Exhibit 27",
    "context": "Exhibit 27-Exhibit 30). TEL China SPE Revenue & Monthly Japan Semicap Imports to China EXHIBIT 28: China import yields decent correlation with TEL's China revenue. TEL Quarterly PRC Sales vs. 2M PRC Import: 1QCY23-1QCY26"
  },
  {
    "figure_id": "F319",
    "report_id": "R013",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: China import yields decent correlation with TEL's China revenue. TEL Quarterly PRC Sales vs. 2M PRC Import: 1QCY23-1QCY26 EXHIBIT 29: The regression suggests TEL's revenue from China to be +5% QoQ in JunQ."
  },
  {
    "figure_id": "F320",
    "report_id": "R013",
    "label": "EXHIBIT 30",
    "context": "Exhibit 31-Exhibit 33). EXHIBIT 31: Kokusai's Quarterly China sales shows decent correlation with monthly import."
  },
  {
    "figure_id": "F321",
    "report_id": "R013",
    "label": "Exhibit 31",
    "context": "Exhibit 31-Exhibit 33). EXHIBIT 31: Kokusai's Quarterly China sales shows decent correlation with monthly import. Kokusai Quarterly PRC Sales vs. 2M PRC Import: 2QCY22-1QCY26 EXHIBIT 32: The regression suggests Kokusai's revenue"
  },
  {
    "figure_id": "F322",
    "report_id": "R013",
    "label": "EXHIBIT 33",
    "context": "Exhibit 34-Exhibit 36). EXHIBIT 34: Screen's Quarterly China sales shows some correlation with monthly import."
  },
  {
    "figure_id": "F323",
    "report_id": "R013",
    "label": "Exhibit 34",
    "context": "Exhibit 34-Exhibit 36). EXHIBIT 34: Screen's Quarterly China sales shows some correlation with monthly import. Screen Quarterly PRC Sales vs. 2M PRC Import: 2QCY18-1QCY26 EXHIBIT 35: The regression suggests Screen's revenue from"
  },
  {
    "figure_id": "F324",
    "report_id": "R013",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 37: Advantest's Quarterly China sales shows decent correlation with monthly import."
  },
  {
    "figure_id": "F325",
    "report_id": "R013",
    "label": "Exhibit 37",
    "context": "EXHIBIT 37: Advantest's Quarterly China sales shows decent correlation with monthly import. Advantest Quarterly PRC Sales vs. 2M PRC Import: 1QCY16-1QCY26 EXHIBIT 38: Our regression suggests Advantest's China sales to be -7% QoQ i"
  },
  {
    "figure_id": "F326",
    "report_id": "R013",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: ...with overall China exposure predicted at 14% vs MarQ exposure of 17% China as % of Advantest's Quarterly SPE Revenue ## APPENDIX: DATA"
  },
  {
    "figure_id": "F327",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 4: TEU growth was decelerated in the most recent week Daily TEU from China to the US, YoY Data as of 6/18/2026. Represents the aggregated container volume, measured in twenty-foot equivalent units (TEU), of vessels depart"
  },
  {
    "figure_id": "F328",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Week 24 China to US vessels and TEUs were down WoW Weekly Average TEUs and Vessels from China to US"
  },
  {
    "figure_id": "F329",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 7: TEU growth from Mainland China and Asia-Ex Mainland China was down this past week Daily TEU from Asia ex-Mainland China and Mainland China to US, YoY Asia ex-Mainland China includes Vietnam, South Korea, Taiwan and Jap"
  },
  {
    "figure_id": "F330",
    "report_id": "R014",
    "label": "Exhibit 7",
    "context": "Exhibit 8: Chinese port activity was down -1% sequentially in the most recent week and up +5% YoY"
  },
  {
    "figure_id": "F331",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Exhibit 9: Ocean rates increased +19% WoW after remaining unchanged in the previous week China/East Asia to the North American West Coast, \\$/FEU"
  },
  {
    "figure_id": "F332",
    "report_id": "R014",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Planned TEUs are expected to decrease sequentially next week and increase 2 weeks out Planned TEUs into the Port of LA"
  },
  {
    "figure_id": "F333",
    "report_id": "R014",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Tracking volumes over the last four weeks and upcoming 2 weeks Port Optimizer 6 Week Dashboard Weekly data update as of 6/19/2026 Port Optimizer data includes two week forward data for week ending 7/3"
  },
  {
    "figure_id": "F334",
    "report_id": "R014",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Rates were +50% YoY last week on the West Coast Intermodal traffic growth on the West Coast (UNP/BNSF) was +11% YoY in the most recent week, versus +16% last week. Exhibit 15: Truckload load availability was +79% YoY thi"
  },
  {
    "figure_id": "F335",
    "report_id": "R014",
    "label": "Exhibit 14",
    "context": "Exhibit 13: West Coast intermodal carloads were +11% YoY versus +16% YoY last week Intermodal Carloads on the West Coast Weekly intermodal carload as of 6/13/2026 Truckload spot rates ex-fuel on the West Coast from truckstop.com i"
  },
  {
    "figure_id": "F336",
    "report_id": "R014",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Congestion remains fluid as per our supply chain congestion index, about in line with pre-Covid levels"
  },
  {
    "figure_id": "F337",
    "report_id": "R014",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Congestion remains fluid as per our supply chain congestion index, about in line with pre-Covid levels GS Weekly Supply Chain Congestion Index, Feb 2020 – June 2026"
  },
  {
    "figure_id": "F338",
    "report_id": "R014",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Congestion remains fluid as per our supply chain congestion index, about in line with pre-Covid levels GS Weekly Supply Chain Congestion Index, Feb 2020 – June 2026 Weekly data as of 6/7/2026 ## Lagged Monthly Data We"
  },
  {
    "figure_id": "F339",
    "report_id": "R014",
    "label": "Exhibit 18",
    "context": "Exhibit 19: April rates were up 25% from March Drewry Air Rates Shanghai to LA Big Three YoY v. China/Asia/Asia ex-China to US TEU Monthly YoY"
  },
  {
    "figure_id": "F340",
    "report_id": "R014",
    "label": "Exhibit 19",
    "context": "Exhibit 20: Big Three growth tends to follow TEU growth out of Asia to the US China and Asia TEU YoY data through 2/26"
  },
  {
    "figure_id": "F341",
    "report_id": "R014",
    "label": "Exhibit 19",
    "context": "Exhibit 21: We estimate that April levels were lower YoY Implied Trade Value Change YoY Based on YoY TEU Change and Estimated Value/TEU"
  },
  {
    "figure_id": "F342",
    "report_id": "R014",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We estimate that April levels were lower YoY Implied Trade Value Change YoY Based on YoY TEU Change and Estimated Value/TEU ■ Logistics Managers Index Inventory Level Expansion ☐ April upstream (B2B) inventories expand"
  },
  {
    "figure_id": "F343",
    "report_id": "R014",
    "label": "Exhibit 22",
    "context": "Exhibit 23: Inventory costs slowed in April LMI Inventory Cost Index"
  },
  {
    "figure_id": "F344",
    "report_id": "R014",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Inventory costs slowed in April LMI Inventory Cost Index \\- Inventory to sales for retailers/manufacturers/wholesalers were 1.09/1.51/1.21 for March which is lower versus February at 1.11/1.52/1.23. Exhibit 24: Invento"
  },
  {
    "figure_id": "F345",
    "report_id": "R014",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Inventory to sales have not shown an increase like in Trump 1.0... Inventory to Sales Ratio: Retailers ex Motor Vehicle and Parts Dealers Exhibit 25: ...nor for manufacturers... Inventory to Sales Manufacturers Exhib"
  },
  {
    "figure_id": "F346",
    "report_id": "R014",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Inventory to sales have not shown an increase like in Trump 1.0... Inventory to Sales Ratio: Retailers ex Motor Vehicle and Parts Dealers Exhibit 25: ...nor for manufacturers... Inventory to Sales Manufacturers Exhib"
  },
  {
    "figure_id": "F347",
    "report_id": "R014",
    "label": "Exhibit 25",
    "context": "Exhibit 25: ...nor for manufacturers... Inventory to Sales Manufacturers Exhibit 26: ...while wholesalers were also unchanged Inventory to Sales Wholesalers ## Disclosure Appendix ## Reg AC We, Jordan Alliger, Paul Stoddard and"
  },
  {
    "figure_id": "F348",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Acceleration in early June exports ## Disclosure Appendix ## Reg AC We, Irene Choi and Goohoon Kwon, CFA, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have"
  },
  {
    "figure_id": "F349",
    "report_id": "R016",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Lithium prices have rebounded to around \\$20-25k/t from the 2025 trough, but we still see further upside as the market tightens"
  },
  {
    "figure_id": "F350",
    "report_id": "R016",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: Inventory days have fallen below 20 days, a level that has historically been supportive of stronger lithium prices"
  },
  {
    "figure_id": "F351",
    "report_id": "R016",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Average return on capital for the industry have remained close to zero for the last two years and have only started recovering Profitability and Returns"
  },
  {
    "figure_id": "F352",
    "report_id": "R016",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 6: Based on historical correlation, the industry needs a lithium price of \\$15-20k/t to achieve a 10% return on capital Industry ROACE vs lithium carbonate price"
  },
  {
    "figure_id": "F353",
    "report_id": "R016",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 7: Capex is expected to have fallen by 50% in 2025 which would take lithium investments to a 3-year low. Higher price signal is required to drive new supply growth"
  },
  {
    "figure_id": "F354",
    "report_id": "R016",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 8: Higher prices are bringing back curtailed supply, but around 200kt LCE of restarts is still not enough to solve 2027 tightness"
  },
  {
    "figure_id": "F355",
    "report_id": "R016",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 10: Demand is growing faster than capacity and we expect the lithium market to tighten further through 2026 and 2027"
  },
  {
    "figure_id": "F356",
    "report_id": "R016",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 12: In 2026, we estimate only around 300ktpa of capacity growth which is not enough to keep up with demand growth of c.500ktpa Annual lithium supply and demand growth (kt LCE)"
  },
  {
    "figure_id": "F357",
    "report_id": "R016",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 13: Based on our lithium supply and demand outlook, we expect lithium spot prices will average \\$24.6k/t in 2026, \\$32.5k/t in 2027 and \\$16k/t long term Forecast Lithium Carbonate Price versus Forward Curve and Consensus"
  },
  {
    "figure_id": "F358",
    "report_id": "R016",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 14: Sensitivity of BESS costs to lithium prices"
  },
  {
    "figure_id": "F359",
    "report_id": "R016",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 16: The setup remains positive for higher lithium prices given we are mid-cycle"
  },
  {
    "figure_id": "F360",
    "report_id": "R016",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 17: Tianqi's share price moves 6-12 months ahead of spot lithium prices. We expect Tianqi share price to rise, ahead of our higher price view Tianqi's share price vs Li price"
  },
  {
    "figure_id": "F361",
    "report_id": "R016",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 18: Tianqi's 1yr forward P/S"
  },
  {
    "figure_id": "F362",
    "report_id": "R016",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Tianqi's 1yr forward P/S EXHIBIT 19: Tianqi's 1yr forward P/E ## LITHIUM INVENTORY"
  },
  {
    "figure_id": "F363",
    "report_id": "R016",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 20: Real-time lithium inventory days in China are at the lowest since 2023 China's lithium carbonate (Li2CO3) inventory"
  },
  {
    "figure_id": "F364",
    "report_id": "R016",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 21: Lithium inventory has fallen below 20 days, implying a tighter market and stronger support for prices China's lithium carbonate (Li2CO3) + hydroxide (LiOH) inventory"
  },
  {
    "figure_id": "F365",
    "report_id": "R016",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 22: Lithium prices are highly correlated to lithium prices. Current inventory datys are aligned with average"
  },
  {
    "figure_id": "F366",
    "report_id": "R016",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 23: Sub-20 inventory days support further upside in lithium prices versus our prior balanced-market view"
  },
  {
    "figure_id": "F367",
    "report_id": "R016",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 24: Monthly lithium supply and demand. Global lithium market was largely balanced year to date Monthly Lithium Supply and Demand (kt LCE)"
  },
  {
    "figure_id": "F368",
    "report_id": "R016",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 25: Year to date, lithium demand is up around 32% versus supply growth of around 24% Global lithium supply vs demand growth"
  },
  {
    "figure_id": "F369",
    "report_id": "R016",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 26: YTD, EV demand is up around 9% year to date while ESS demand is up around 100%"
  },
  {
    "figure_id": "F370",
    "report_id": "R016",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 27: We estimate global lithium demand is up around 32% year to date, driven by stronger ESS demand Global lithium demand (kt LCE)"
  },
  {
    "figure_id": "F371",
    "report_id": "R016",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 28: Lithium supply is up around 24% year to date, still below demand growth"
  },
  {
    "figure_id": "F372",
    "report_id": "R016",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 29: Lithium supply by countries"
  },
  {
    "figure_id": "F373",
    "report_id": "R016",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 31: China, Chile and Argentina have led supply growth this year, while Australia has lagged Jan-Apr 2026 lithium supply growth (kt LCE)"
  },
  {
    "figure_id": "F374",
    "report_id": "R016",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 32: Australia's lithium supply. Year-to-date growth is around $6\\%$"
  },
  {
    "figure_id": "F375",
    "report_id": "R016",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 33: Operating rates for Australian mines are at 80% which has fallen from 90% in 2023-24 due to weak lithium prices Australia Lithium Supply and Mine Operating Rate"
  },
  {
    "figure_id": "F376",
    "report_id": "R016",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 34: Chile's lithium supply. Year-to-date growth is around $25\\%$"
  },
  {
    "figure_id": "F377",
    "report_id": "R016",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 35: China's lithium supply. Year-to-date growth is around $30\\%$"
  },
  {
    "figure_id": "F378",
    "report_id": "R016",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 35: China's lithium supply. Year-to-date growth is around $30\\%$ EXHIBIT 36: China's lepidolite production (kt LCE) EXHIBIT 37: China's brine production (kt LCE)"
  },
  {
    "figure_id": "F379",
    "report_id": "R016",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: China's lithium supply. Year-to-date growth is around $30\\%$ EXHIBIT 36: China's lepidolite production (kt LCE) EXHIBIT 37: China's brine production (kt LCE) EXHIBIT 38: China's spodumene production (kt LCE)"
  },
  {
    "figure_id": "F380",
    "report_id": "R016",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: China's lepidolite production (kt LCE) EXHIBIT 37: China's brine production (kt LCE) EXHIBIT 38: China's spodumene production (kt LCE) EXHIBIT 39: China's lepidolite production have not increased despite higher lit"
  },
  {
    "figure_id": "F381",
    "report_id": "R016",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: China's brine production (kt LCE) EXHIBIT 38: China's spodumene production (kt LCE) EXHIBIT 39: China's lepidolite production have not increased despite higher lithium prices China's Lithium Supply from Lepidolite Mi"
  },
  {
    "figure_id": "F382",
    "report_id": "R016",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 40: Zimbabwe's lithium supply. Year-to-date growth is around $16\\%$"
  },
  {
    "figure_id": "F383",
    "report_id": "R016",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 41: Argentina's lithium supply. Year-to-date growth is around $106\\%$"
  },
  {
    "figure_id": "F384",
    "report_id": "R016",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 42: RoW lithium supply. year to date, supply grew by 36% y-o-y"
  },
  {
    "figure_id": "F385",
    "report_id": "R016",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 42: RoW lithium supply. year to date, supply grew by 36% y-o-y ## SUPPLY AND DEMAND OUTLOOK ## LITHIUM DEMAND We estimate battery demand to grow from 1,770GWh in 2025 to 5,307GWh by 2030, representing growth of 25% CAGR. W"
  },
  {
    "figure_id": "F386",
    "report_id": "R016",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 46: Global lithium projects by region"
  },
  {
    "figure_id": "F387",
    "report_id": "R016",
    "label": "EXHIBIT 46",
    "context": "EXHIBIT 46: Global lithium projects by region remains highly concentrated within China. EXHIBIT 47: 2024 and 2030 lithium capacity. We expect China and Australia will remain the largest suppliers, while many countries including Ar"
  },
  {
    "figure_id": "F388",
    "report_id": "R016",
    "label": "EXHIBIT 47",
    "context": "EXHIBIT 47: 2024 and 2030 lithium capacity. We expect China and Australia will remain the largest suppliers, while many countries including Argentina, US, Canada, Brazil, Zimbabwe, and Mali are expanding rapidly Taking a closer lo"
  },
  {
    "figure_id": "F389",
    "report_id": "R016",
    "label": "EXHIBIT 48",
    "context": "EXHIBIT 49: Lithium projects by start-up year (2022-26)"
  },
  {
    "figure_id": "F390",
    "report_id": "R016",
    "label": "EXHIBIT 52",
    "context": "EXHIBIT 53: We expect lithium demand growth to outpace supply growth in 2026 and again in 2027 Annual lithium supply and demand growth (kt LCE)"
  },
  {
    "figure_id": "F391",
    "report_id": "R016",
    "label": "EXHIBIT 53",
    "context": "EXHIBIT 54: Lithium prices have doubled from the trough to around \\$20-25k/t, with further upside possible if inventories stay tight"
  },
  {
    "figure_id": "F392",
    "report_id": "R016",
    "label": "EXHIBIT 54",
    "context": "EXHIBIT 54: Lithium prices have doubled from the trough to around \\$20-25k/t, with further upside possible if inventories stay tight EXHIBIT 55: Lithium refining margins have started to increase as market tightens Lepidolite ref"
  },
  {
    "figure_id": "F393",
    "report_id": "R016",
    "label": "EXHIBIT 54",
    "context": "EXHIBIT 56: Based on our lithium supply and demand outlook, we expect lithium spot prices will average \\$24.6k/t in 2026, \\$32.5k/t in 2027 and \\$16k/t long term Forecast Lithium Carbonate Price versus Forward Curve and Consensus"
  },
  {
    "figure_id": "F394",
    "report_id": "R016",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 57: Lithium carbonate price has a high correlation with demand/capacity"
  },
  {
    "figure_id": "F395",
    "report_id": "R016",
    "label": "EXHIBIT 57",
    "context": "EXHIBIT 58: According to our analysis, the marginal cash cost of lithium at 90th percentile is around US\\$11.1k/ton"
  },
  {
    "figure_id": "F396",
    "report_id": "R016",
    "label": "EXHIBIT 57",
    "context": "EXHIBIT 59: Full breakeven costs of lithium supply by technology. We now estimate long-term lithium price at around \\$16k/t LCE"
  },
  {
    "figure_id": "F397",
    "report_id": "R016",
    "label": "EXHIBIT 58",
    "context": "EXHIBIT 60: Lithium prices are capped by EV competitiveness to ICE"
  },
  {
    "figure_id": "F398",
    "report_id": "R016",
    "label": "EXHIBIT 59",
    "context": "EXHIBIT 61: Sensitivity of BESS costs to lithium prices"
  },
  {
    "figure_id": "F399",
    "report_id": "R016",
    "label": "EXHIBIT 62",
    "context": "EXHIBIT 63: The setup remains positive for higher lithium prices given we are mid-cycle"
  },
  {
    "figure_id": "F400",
    "report_id": "R016",
    "label": "EXHIBIT 62",
    "context": "EXHIBIT 63: The setup remains positive for higher lithium prices given we are mid-cycle ## STOCK IMPLICATIONS EXHIBIT 64: Lithium equities have rebounded shareply since late 2025 but we still view the market as mid-cycle Performan"
  },
  {
    "figure_id": "F401",
    "report_id": "R016",
    "label": "EXHIBIT 63",
    "context": "EXHIBIT 65: Average return on capital for the industry have remained close to zero for the last two years and have only started recovering Profitability and Returns"
  },
  {
    "figure_id": "F402",
    "report_id": "R016",
    "label": "EXHIBIT 65",
    "context": "EXHIBIT 66: Capex is expected to have fallen by 50% in 2025 which would take lithium investments to a 3-year low. Higher price signal is required to drive new supply growth Capex and Reinvestment"
  },
  {
    "figure_id": "F403",
    "report_id": "R016",
    "label": "EXHIBIT 66",
    "context": "EXHIBIT 67: ND/E level remains reasonable at 20% currently"
  },
  {
    "figure_id": "F404",
    "report_id": "R016",
    "label": "EXHIBIT 67",
    "context": "EXHIBIT 68: Share price beta of key lithium stocks to lithium spot price Beta to spot lithium price (2019-current)"
  },
  {
    "figure_id": "F405",
    "report_id": "R016",
    "label": "EXHIBIT 68",
    "context": "EXHIBIT 69: Tianqi's share price moves 6-12 months ahead of spot lithium prices. We expect Tianqi share price to rise, ahead of our higher price view"
  },
  {
    "figure_id": "F406",
    "report_id": "R016",
    "label": "EXHIBIT 69",
    "context": "EXHIBIT 70: Tianqi's operating margin vs lithium carbonate price"
  },
  {
    "figure_id": "F407",
    "report_id": "R016",
    "label": "EXHIBIT 69",
    "context": "EXHIBIT 70: Tianqi's operating margin vs lithium carbonate price EXHIBIT 71: Tianqi Lithium financial outlook"
  },
  {
    "figure_id": "F408",
    "report_id": "R016",
    "label": "EXHIBIT 75",
    "context": "EXHIBIT 75: Tianqi's 1yr forward P/S EXHIBIT 76: Tianqi's 1yr forward P/E ## APPENDIX - FINANCIAL FORECASTS"
  },
  {
    "figure_id": "F409",
    "report_id": "R016",
    "label": "EXHIBIT 75",
    "context": "EXHIBIT 75: Tianqi's 1yr forward P/S EXHIBIT 76: Tianqi's 1yr forward P/E ## APPENDIX - FINANCIAL FORECASTS EXHIBIT 77: Tianqi Lithium's financial forecast"
  },
  {
    "figure_id": "F410",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 2: AI Investment Surge Adds Little to US GDP and the US Consumer Remains Under Pressure"
  },
  {
    "figure_id": "F411",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 3: The Payroll Surge Is an Outlier Relative to Other Labor Market Indicators"
  },
  {
    "figure_id": "F412",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Trimmed-Mean PCE Still Looks More Benign Than Core PCE"
  },
  {
    "figure_id": "F413",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 5: While Hikes Have Become More Likely, We Think They Are Less Likely Than Markets Are Pricing"
  },
  {
    "figure_id": "F414",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "Exhibit 5: While Hikes Have Become More Likely, We Think They Are Less Likely Than Markets Are Pricing 6. We had expected Warsh's refusal to provide either a \"dot\" or verbal guidance about upcoming rate decisions but his broader"
  },
  {
    "figure_id": "F415",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Our ECB and BoE Rate Views Remain Below Market Pricing"
  },
  {
    "figure_id": "F416",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Underlying Inflation in Japan Remains Benign"
  },
  {
    "figure_id": "F417",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "Exhibit 9: China's Domestic Demand Is Growing Far More Slowly Than Its Exports"
  },
  {
    "figure_id": "F418",
    "report_id": "R018",
    "label": "Exhibit 8",
    "context": "Exhibit 9: China's Domestic Demand Is Growing Far More Slowly Than Its Exports 10. US financial markets have digested the hawkish FOMC shock well, with declines in breakeven inflation and 30-year Treasury yields alongside a rebou"
  },
  {
    "figure_id": "F419",
    "report_id": "R019",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: Airbnb is set to lead room night growth given the current traffic data 26Q2 BernE Room Night Growth EXHIBIT 3: Based on current traffic data, we expect Airbnb and Booking to outperform consensus on room nights, while E"
  },
  {
    "figure_id": "F420",
    "report_id": "R019",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: Airbnb is set to lead room night growth given the current traffic data 26Q2 BernE Room Night Growth EXHIBIT 3: Based on current traffic data, we expect Airbnb and Booking to outperform consensus on room nights, while E"
  },
  {
    "figure_id": "F421",
    "report_id": "R019",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 6: Only BKNG is preferred to the SPX by the sell side OTAs: Sell side ratings Ratings as at 19 June 2026"
  },
  {
    "figure_id": "F422",
    "report_id": "R019",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 8: Only Airbnb recorded a gain in share price following the Q1 results"
  },
  {
    "figure_id": "F423",
    "report_id": "R019",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Only Airbnb recorded a gain in share price following the Q1 results YTD Stock Price Returns Share prices as of 19 June 2026 ## AIRBNB"
  },
  {
    "figure_id": "F424",
    "report_id": "R019",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Only Airbnb recorded a gain in share price following the Q1 results YTD Stock Price Returns Share prices as of 19 June 2026 ## AIRBNB EXHIBIT 9: Airbnb's web traffic continues to accelerate whilst app engagement growth"
  },
  {
    "figure_id": "F425",
    "report_id": "R019",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: India saw the largest increase in downloads versus Q2 last year, contributing to 34% of the total increase, following by Pakistan (20%) and Indonesia (6%). This is followed by three South American nations, with MSD % con"
  },
  {
    "figure_id": "F426",
    "report_id": "R019",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: India saw the largest increase in downloads versus Q2 last year, contributing to 34% of the total increase, following by Pakistan (20%) and Indonesia (6%). This is followed by three South American nations, with MSD % con"
  },
  {
    "figure_id": "F427",
    "report_id": "R019",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 12: Airbnb model vs actual"
  },
  {
    "figure_id": "F428",
    "report_id": "R019",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Airbnb model vs actual EXHIBIT 13: Traffic is correlated with nights booked Airbnb - Traffic vs nights booked ## BOOKING"
  },
  {
    "figure_id": "F429",
    "report_id": "R019",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Airbnb model vs actual EXHIBIT 13: Traffic is correlated with nights booked Airbnb - Traffic vs nights booked ## BOOKING EXHIBIT 14: Both app and web traffic growth have decelerated in the quarter driven by a weak st"
  },
  {
    "figure_id": "F430",
    "report_id": "R019",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 16: Growth at Agoda continues to exhibit strength but has slowed down from the $40\\%+$ growth seen in Q1; the Booking app's engagement has decelerated whilst Priceline continues to struggle"
  },
  {
    "figure_id": "F431",
    "report_id": "R019",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 16: Growth at Agoda continues to exhibit strength but has slowed down from the $40\\%+$ growth seen in Q1; the Booking app's engagement has decelerated whilst Priceline continues to struggle BKNG - App DAU growth by app"
  },
  {
    "figure_id": "F432",
    "report_id": "R019",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 17: Booking's traffic is correlated to room nights BKNG - Traffic vs room nights EXHIBIT 18: BKNG model vs actual"
  },
  {
    "figure_id": "F433",
    "report_id": "R019",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 18: BKNG model vs actual BKNG - room nights (millions) quarterly predictor Traffic growth change since guidance issued"
  },
  {
    "figure_id": "F434",
    "report_id": "R019",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Booking's traffic is correlated to room nights BKNG - Traffic vs room nights EXHIBIT 18: BKNG model vs actual BKNG - room nights (millions) quarterly predictor Traffic growth change since guidance issued EXHIBIT 19:"
  },
  {
    "figure_id": "F435",
    "report_id": "R019",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 20: App engagement has been very weak through the quarter, set to grow just 2.3%, whilst web has also slowed following five consecutive quarters of acceleration; downloads growth now laps the beginning of declines in 2Q25 EX"
  },
  {
    "figure_id": "F436",
    "report_id": "R019",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 21: App engagement and web traffic decelerated through the quarter; the y/y fall in downloads abated in June EXHIBIT 22: Both Hotels.com and Expedia have experienced a deceleration in app engagement through the quarter wit"
  },
  {
    "figure_id": "F437",
    "report_id": "R019",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 23: Expedia B2C room nights are correlated with traffic"
  },
  {
    "figure_id": "F438",
    "report_id": "R019",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 23: Expedia B2C room nights are correlated with traffic Actual vs. modelled room nights (B2C) EXHIBIT 24: EXPE model vs actual"
  },
  {
    "figure_id": "F439",
    "report_id": "R019",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 24: EXPE model vs actual EXPE - Room nights (millions) quarterly predictor ## TRIPADVISOR"
  },
  {
    "figure_id": "F440",
    "report_id": "R019",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Expedia B2C room nights are correlated with traffic Actual vs. modelled room nights (B2C) EXHIBIT 24: EXPE model vs actual EXPE - Room nights (millions) quarterly predictor ## TRIPADVISOR EXHIBIT 25: App engagement a"
  },
  {
    "figure_id": "F441",
    "report_id": "R019",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 27: Viator, which suffered web traffic declines through 2025, has seen declines ease in last six months with y/y traffic up so far in June; app engagement at the Viator was storing in April and May with \\~40% y/y growth"
  },
  {
    "figure_id": "F442",
    "report_id": "R019",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 27: Viator, which suffered web traffic declines through 2025, has seen declines ease in last six months with y/y traffic up so far in June; app engagement at the Viator was storing in April and May with \\~40% y/y growth Viat"
  },
  {
    "figure_id": "F443",
    "report_id": "R019",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Tripadvisor continues to struggle with declines in traffic across both web and app channels Tripadvisor traffic growth (y/y) EXHIBIT 27: Viator, which suffered web traffic declines through 2025, has seen declines ease"
  },
  {
    "figure_id": "F444",
    "report_id": "R019",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 30: Claude now automatically suggests relevant connectors (apps) to hotel search queries"
  },
  {
    "figure_id": "F445",
    "report_id": "R019",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 30: Claude now automatically suggests relevant connectors (apps) to hotel search queries EXHIBIT 31: We can with a little trial and error, now get ChatGPT to call apps mid-flow rather than right at the top. Here is only ca"
  },
  {
    "figure_id": "F446",
    "report_id": "R019",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 30: Claude now automatically suggests relevant connectors (apps) to hotel search queries EXHIBIT 31: We can with a little trial and error, now get ChatGPT to call apps mid-flow rather than right at the top. Here is only ca"
  },
  {
    "figure_id": "F447",
    "report_id": "R019",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: We can with a little trial and error, now get ChatGPT to call apps mid-flow rather than right at the top. Here is only calls one app - in this case Booking.com Stays based on your search 20 Jun – 22 Jun · ⚠ 2 So a query"
  },
  {
    "figure_id": "F448",
    "report_id": "R019",
    "label": "Exhibit 38",
    "context": "EXHIBIT 32: Q2 RevPAR by U.S. chain scale: all segments saw growth. US chain scale RevPAR growth by quarter EXHIBIT 33: Q2 RevPAR by region: Americas and MEA saw declines Regional RevPAR growth by quarter EXHIBIT 34: In the US,"
  },
  {
    "figure_id": "F449",
    "report_id": "R019",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 35: The Luxury chain scale continues to outperform the rest of the market, with a slowdown at the lower end, with Economy roughly flat in May and Midscale - Upscale decelerating to LSD growth"
  },
  {
    "figure_id": "F450",
    "report_id": "R019",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 35: The Luxury chain scale continues to outperform the rest of the market, with a slowdown at the lower end, with Economy roughly flat in May and Midscale - Upscale decelerating to LSD growth Hotels: y/y US RevPAR growth by"
  },
  {
    "figure_id": "F451",
    "report_id": "R019",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 36: The US continued to grow RevPAR in the MSDs whilst European performance slowed; China failed to maintain its recovery with a y/y decline in May despite strength across APAC. The MEA region recovered to 3.7% in May, suppo"
  },
  {
    "figure_id": "F452",
    "report_id": "R019",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 37: The Middle East has rebounded strongly in May after a 25% y/y RevPAR contraction in April, with recent strength driven by Saudi Arabia ## THE LATEST WEEKLY DATA"
  },
  {
    "figure_id": "F453",
    "report_id": "R019",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 37: The Middle East has rebounded strongly in May after a 25% y/y RevPAR contraction in April, with recent strength driven by Saudi Arabia ## THE LATEST WEEKLY DATA EXHIBIT 38: US RevPAR performance has surged in the first"
  },
  {
    "figure_id": "F454",
    "report_id": "R019",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: US RevPAR performance has surged in the first month of June, likely due to early demand from the North American World Cup US weekly RevPAR growth (y/y) EXHIBIT 39: On a rolling basis, RevPAR has accelerated across the"
  },
  {
    "figure_id": "F455",
    "report_id": "R019",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 40: The number of tickets available for the World Cup peaks in late June but later games will likely elicit more interest and economic activity. The most important games are almost exclusively being held in the US. Tickets f"
  },
  {
    "figure_id": "F456",
    "report_id": "R019",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 42: Hyatt and Marriott lead in terms of exposure to host cities and near stadiums"
  },
  {
    "figure_id": "F457",
    "report_id": "R019",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 42: Hyatt and Marriott lead in terms of exposure to host cities and near stadiums World Cup Total System Exposure We use global room counts given in FY25 results"
  },
  {
    "figure_id": "F458",
    "report_id": "R019",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 42: Hyatt and Marriott lead in terms of exposure to host cities and near stadiums World Cup Total System Exposure We use global room counts given in FY25 results EXHIBIT 43: Under April - May performance and assuming early"
  },
  {
    "figure_id": "F459",
    "report_id": "R019",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: Under April - May performance and assuming early June performance will continue through the month, we expect Hyatt to come in ahead of their FY guide and Marriott to beat their Q2 guide, and Hilton to come right at the t"
  },
  {
    "figure_id": "F460",
    "report_id": "R019",
    "label": "Exhibit 46",
    "context": "EXHIBIT 44: The global pipeline added \\~55k rooms in April and another \\~7k in May, to more than offset the small contraction in March STR Hotel Global Pipeline (millions of rooms) EXHIBIT 45: The US and Asia Pacific together adde"
  },
  {
    "figure_id": "F461",
    "report_id": "R019",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 46: Rooms under construction has increased through the quarter by \\~15.6k EXHIBIT 47: The % of global pipeline under construction ticked down marginally"
  },
  {
    "figure_id": "F462",
    "report_id": "R019",
    "label": "EXHIBIT 45",
    "context": "EXHIBIT 46: Rooms under construction has increased through the quarter by \\~15.6k EXHIBIT 47: The % of global pipeline under construction ticked down marginally STR Hotel Global Pipeline - % under construction EXHIBIT 48: The re"
  },
  {
    "figure_id": "F463",
    "report_id": "R019",
    "label": "EXHIBIT 46",
    "context": "EXHIBIT 46: Rooms under construction has increased through the quarter by \\~15.6k EXHIBIT 47: The % of global pipeline under construction ticked down marginally STR Hotel Global Pipeline - % under construction EXHIBIT 48: The re"
  },
  {
    "figure_id": "F464",
    "report_id": "R019",
    "label": "EXHIBIT 47",
    "context": "EXHIBIT 50: The MEA pipeline continues to grow despite the ongoing conflict in the Middle East, with the pipeline growing by \\~12k rooms so far this quarter"
  },
  {
    "figure_id": "F465",
    "report_id": "R019",
    "label": "EXHIBIT 48",
    "context": "EXHIBIT 51: Pipeline growth has offset a 5.3% increase in rooms under construction since Februray, resulting in a small tick down in the % of rooms under construction"
  },
  {
    "figure_id": "F466",
    "report_id": "R019",
    "label": "EXHIBIT 49",
    "context": "EXHIBIT 50: The MEA pipeline continues to grow despite the ongoing conflict in the Middle East, with the pipeline growing by \\~12k rooms so far this quarter STR Hotel MEA Pipeline (millions of rooms) EXHIBIT 51: Pipeline growth ha"
  },
  {
    "figure_id": "F467",
    "report_id": "R019",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 50: The MEA pipeline continues to grow despite the ongoing conflict in the Middle East, with the pipeline growing by \\~12k rooms so far this quarter STR Hotel MEA Pipeline (millions of rooms) EXHIBIT 51: Pipeline growth ha"
  },
  {
    "figure_id": "F468",
    "report_id": "R019",
    "label": "Exhibit 56",
    "context": "EXHIBIT 54: Marriott has the biggest share of global pipeline at around 19-19.5%"
  },
  {
    "figure_id": "F469",
    "report_id": "R019",
    "label": "EXHIBIT 52",
    "context": "EXHIBIT 54: Marriott has the biggest share of global pipeline at around 19-19.5% Marriott share of global pipeline (STR) EXHIBIT 55: Hilton added \\~26k rooms to its pipeline in April, increasing its share of pipeline"
  },
  {
    "figure_id": "F470",
    "report_id": "R019",
    "label": "EXHIBIT 53",
    "context": "EXHIBIT 55: Hilton added \\~26k rooms to its pipeline in April, increasing its share of pipeline Hilton share of global pipeline (STR) EXHIBIT 56: IHG share of pipeline is steady"
  },
  {
    "figure_id": "F471",
    "report_id": "R019",
    "label": "EXHIBIT 54",
    "context": "EXHIBIT 56: IHG share of pipeline is steady IHG share of global pipeline (STR)"
  },
  {
    "figure_id": "F472",
    "report_id": "R019",
    "label": "EXHIBIT 55",
    "context": "EXHIBIT 55: Hilton added \\~26k rooms to its pipeline in April, increasing its share of pipeline Hilton share of global pipeline (STR) EXHIBIT 56: IHG share of pipeline is steady IHG share of global pipeline (STR) Hyatt share of"
  },
  {
    "figure_id": "F473",
    "report_id": "R019",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 56: IHG share of pipeline is steady IHG share of global pipeline (STR) Hyatt share of global pipeline (STR) STR tends to understate Hyatt's pipeline Branded share of hotel rooms (May 2026) EXHIBIT 58: Brands are taking s"
  },
  {
    "figure_id": "F474",
    "report_id": "R019",
    "label": "EXHIBIT 58",
    "context": "EXHIBIT 58: Brands are taking share in all geographies, most notably in MEA and Latin America ## I. REQUIRED DISCLOSURES Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically no"
  },
  {
    "figure_id": "F475",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 1: BEV and PHEV are on rise Sales by powertrain Exhibit 2: BEV penetration advances in China and Others BEV mix by region Exhibit 3: BEV adoption advances in Thailand, Australia, and Brazil"
  },
  {
    "figure_id": "F476",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 1: BEV and PHEV are on rise Sales by powertrain Exhibit 2: BEV penetration advances in China and Others BEV mix by region Exhibit 3: BEV adoption advances in Thailand, Australia, and Brazil BEV mix by region Exhibit 4"
  },
  {
    "figure_id": "F477",
    "report_id": "R020",
    "label": "Exhibit 2",
    "context": "Exhibit 2: BEV penetration advances in China and Others BEV mix by region Exhibit 3: BEV adoption advances in Thailand, Australia, and Brazil BEV mix by region Exhibit 4: Strong regional divergence for BEV penetration BEV mix b"
  },
  {
    "figure_id": "F478",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Exhibit 3: BEV adoption advances in Thailand, Australia, and Brazil BEV mix by region Exhibit 4: Strong regional divergence for BEV penetration BEV mix by region Sentiment map"
  },
  {
    "figure_id": "F479",
    "report_id": "R020",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Automakers importing vehicles from outside of EU warrant attention Difference in production and sales volume in West Europe Exhibit 8: China OEMs expanding market share for BEV Global BEV mix and China OEMs' market sha"
  },
  {
    "figure_id": "F480",
    "report_id": "R020",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Automakers importing vehicles from outside of EU warrant attention Difference in production and sales volume in West Europe Exhibit 8: China OEMs expanding market share for BEV Global BEV mix and China OEMs' market sha"
  },
  {
    "figure_id": "F481",
    "report_id": "R020",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Aggressive cost reduction plan Comparison of cost reduction target (as of May 2026) Exhibit 10: Increasing risks for procurement of materials Supply chain index Exhibit 11: Our investment view"
  },
  {
    "figure_id": "F482",
    "report_id": "R020",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Aggressive cost reduction plan Comparison of cost reduction target (as of May 2026) Exhibit 10: Increasing risks for procurement of materials Supply chain index Exhibit 11: Our investment view Valuation comps \\*denot"
  },
  {
    "figure_id": "F483",
    "report_id": "R020",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Industry volume, market share, sales trends Volume YoY by brand"
  },
  {
    "figure_id": "F484",
    "report_id": "R020",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Industry volume, market share, sales trends Volume YoY by brand Exhibit 13: Powertrain trends"
  },
  {
    "figure_id": "F485",
    "report_id": "R020",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Industry volume, market share, sales trends Volume YoY by brand Exhibit 13: Powertrain trends"
  },
  {
    "figure_id": "F486",
    "report_id": "R020",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Powertrain trends BEV share by brand"
  },
  {
    "figure_id": "F487",
    "report_id": "R020",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Powertrain trends BEV share by brand Volume YoY by powertrain"
  },
  {
    "figure_id": "F488",
    "report_id": "R020",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Powertrain trends BEV share by brand Volume YoY by powertrain BEV volume YoY"
  },
  {
    "figure_id": "F489",
    "report_id": "R020",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Powertrain trends BEV share by brand Volume YoY by powertrain BEV volume YoY ## Indonesia Exhibit 14:"
  },
  {
    "figure_id": "F490",
    "report_id": "R020",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F491",
    "report_id": "R020",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Industry volume, market share, sales trends Volume YoY by brand"
  },
  {
    "figure_id": "F492",
    "report_id": "R020",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Industry volume, market share, sales trends Volume YoY by brand ## Exhibit 15:"
  },
  {
    "figure_id": "F493",
    "report_id": "R020",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Industry volume, market share, sales trends Volume YoY by brand ## Exhibit 15: Powertrain trends"
  },
  {
    "figure_id": "F494",
    "report_id": "R020",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Powertrain trends BEV share by brand Volume YoY by powertrain"
  },
  {
    "figure_id": "F495",
    "report_id": "R020",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Powertrain trends BEV share by brand Volume YoY by powertrain"
  },
  {
    "figure_id": "F496",
    "report_id": "R020",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Powertrain trends BEV share by brand Volume YoY by powertrain BEV volume YoY ## Australia"
  },
  {
    "figure_id": "F497",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Powertrain trends"
  },
  {
    "figure_id": "F498",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Powertrain trends Exhibit 16: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F499",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Powertrain trends Exhibit 16: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F500",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Powertrain trends Exhibit 16: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F501",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Powertrain trends Exhibit 16: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F502",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Powertrain trends Exhibit 16: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F503",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F504",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Industry volume, market share, sales trends # of Chinese brands"
  },
  {
    "figure_id": "F505",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Industry volume, market share, sales trends # of Chinese brands Volume YoY by brand"
  },
  {
    "figure_id": "F506",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Industry volume, market share, sales trends # of Chinese brands Volume YoY by brand ## Exhibit 19:"
  },
  {
    "figure_id": "F507",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Industry volume, market share, sales trends # of Chinese brands Volume YoY by brand ## Exhibit 19: Powertrain trends"
  },
  {
    "figure_id": "F508",
    "report_id": "R020",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Powertrain trends Volume YoY by powertrain"
  },
  {
    "figure_id": "F509",
    "report_id": "R020",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Powertrain trends Volume YoY by powertrain BEV volume YoY"
  },
  {
    "figure_id": "F510",
    "report_id": "R020",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Powertrain trends Volume YoY by powertrain BEV volume YoY ## UK"
  },
  {
    "figure_id": "F511",
    "report_id": "R020",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Powertrain trends Volume YoY by powertrain BEV volume YoY ## UK Exhibit 20: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F512",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F513",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Industry volume, market share, sales trends Volume YoY by brand"
  },
  {
    "figure_id": "F514",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Industry volume, market share, sales trends Volume YoY by brand Exhibit 21: Powertrain trends"
  },
  {
    "figure_id": "F515",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Industry volume, market share, sales trends Volume YoY by brand Exhibit 21: Powertrain trends"
  },
  {
    "figure_id": "F516",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Industry volume, market share, sales trends Volume YoY by brand Exhibit 21: Powertrain trends Volume YoY by powertrain"
  },
  {
    "figure_id": "F517",
    "report_id": "R020",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Powertrain trends Volume YoY by powertrain BEV volume YoY"
  },
  {
    "figure_id": "F518",
    "report_id": "R020",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Powertrain trends Volume YoY by powertrain BEV volume YoY"
  },
  {
    "figure_id": "F519",
    "report_id": "R020",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Powertrain trends Volume YoY by powertrain BEV volume YoY ## EU(Germany/France/Italy/Spain) Exhibit 22: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F520",
    "report_id": "R020",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F521",
    "report_id": "R020",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Industry volume, market share, sales trends Volume YoY by brand"
  },
  {
    "figure_id": "F522",
    "report_id": "R020",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Industry volume, market share, sales trends Volume YoY by brand ## Exhibit 23:"
  },
  {
    "figure_id": "F523",
    "report_id": "R020",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Industry volume, market share, sales trends Volume YoY by brand ## Exhibit 23: Powertrain trends"
  },
  {
    "figure_id": "F524",
    "report_id": "R020",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Powertrain trends"
  },
  {
    "figure_id": "F525",
    "report_id": "R020",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Powertrain trends Volume YoY by powertrain BEV volume YoY"
  },
  {
    "figure_id": "F526",
    "report_id": "R020",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Powertrain trends Volume YoY by powertrain BEV volume YoY"
  },
  {
    "figure_id": "F527",
    "report_id": "R020",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Powertrain trends Volume YoY by powertrain BEV volume YoY ## US Exhibit 24: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F528",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Industry volume, market share, sales trends Exhibit 25: Powertrain trends"
  },
  {
    "figure_id": "F529",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Industry volume, market share, sales trends Exhibit 25: Powertrain trends"
  },
  {
    "figure_id": "F530",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Industry volume, market share, sales trends Exhibit 25: Powertrain trends"
  },
  {
    "figure_id": "F531",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Industry volume, market share, sales trends Exhibit 25: Powertrain trends"
  },
  {
    "figure_id": "F532",
    "report_id": "R020",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Powertrain trends"
  },
  {
    "figure_id": "F533",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F534",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Industry volume, market share, sales trends"
  },
  {
    "figure_id": "F535",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Industry volume, market share, sales trends Volume YoY by brand"
  },
  {
    "figure_id": "F536",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Industry volume, market share, sales trends Volume YoY by brand Exhibit 27: Powertrain trends"
  },
  {
    "figure_id": "F537",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Industry volume, market share, sales trends Volume YoY by brand Exhibit 27: Powertrain trends"
  },
  {
    "figure_id": "F538",
    "report_id": "R020",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Industry volume, market share, sales trends Volume YoY by brand Exhibit 27: Powertrain trends"
  },
  {
    "figure_id": "F539",
    "report_id": "R020",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Powertrain trends BEV volume YoY"
  },
  {
    "figure_id": "F540",
    "report_id": "R020",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Powertrain trends BEV volume YoY ## Disclosure Appendix"
  },
  {
    "figure_id": "F541",
    "report_id": "R020",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Powertrain trends BEV volume YoY ## Disclosure Appendix ## Reg AC"
  },
  {
    "figure_id": "F542",
    "report_id": "R021",
    "label": "Figure 2",
    "context": "Figure 2: Global copper mine supply and refined production growth Percent change, yoy Figure 3: Global copper scrap usage growth"
  },
  {
    "figure_id": "F543",
    "report_id": "R021",
    "label": "Figure 2",
    "context": "Figure 2: Global copper mine supply and refined production growth Percent change, yoy Figure 3: Global copper scrap usage growth ## As the US vacuums up copper, China has had to react too The US has built a $\\sim 1.2$ mmt stoc"
  },
  {
    "figure_id": "F544",
    "report_id": "R021",
    "label": "Figure 4",
    "context": "Figure 4: Monthly US refined copper imports Note: 01 May - 16 Jun 2026 estimated based on bill of lading data. Figure 5: Jul'26 COMEX/LME copper spread LHS: US\\$/mt, RHS: Percent of LME price"
  },
  {
    "figure_id": "F545",
    "report_id": "R021",
    "label": "Figure 4",
    "context": "Figure 6: Global visible copper inventories by location Thousand mt Includes LME (+ off warrant), COMEX, SHFE, Chinese bonded stocks"
  },
  {
    "figure_id": "F546",
    "report_id": "R021",
    "label": "Figure 6",
    "context": "Figure 6: Global visible copper inventories by location Thousand mt Includes LME (+ off warrant), COMEX, SHFE, Chinese bonded stocks Figure 7: Chinese spot copper import arbitrage and onshore spot premium/discount Before this"
  },
  {
    "figure_id": "F547",
    "report_id": "R021",
    "label": "Figure 6",
    "context": "Figure 8: China's buying floor has moved sharply higher in the last year LME 3M Copper prices (US\\$/mt) vs an open Chinese spot copper import arb window"
  },
  {
    "figure_id": "F548",
    "report_id": "R021",
    "label": "Figure 7",
    "context": "Figure 8: China's buying floor has moved sharply higher in the last year LME 3M Copper prices (US\\$/mt) vs an open Chinese spot copper import arb window Case in point, Chinese purchasing went ice cold (buyer's strike, boosted co"
  },
  {
    "figure_id": "F549",
    "report_id": "R021",
    "label": "Figure 9",
    "context": "Figure 9: LME on-warrant copper stocks vs LME cash-3M spread, weekly X-axis: Thousand mt, Y-axis: US\\$/mt (+ = backwardation / - = contango) Data since 2000, x-axis truncated to 500 kmt Figure 10: Weekly returns of LME 3M copper"
  },
  {
    "figure_id": "F550",
    "report_id": "R022",
    "label": "Figure 4",
    "context": "Indeed, property investment growth worsened to -24.3% y-o-y in May from -20.1% in April, below the market consensus forecast of -15.0% but close to our more cautious forecast of -20.0%. New home sales growth fell to -13.1% y-o-y by floor space and to -9.5% by "
  },
  {
    "figure_id": "F551",
    "report_id": "R022",
    "label": "Figure 5",
    "context": "\\- On wealth effects, from July 2025 to 18 June 2026, the Wind All-A Index, a holistic benchmark tracking the overall performance of all A-shares listed on the Shanghai, Shenzhen and Beijing stock exchanges, increased by $33.2\\%$ (Figure 5), which should have "
  },
  {
    "figure_id": "F552",
    "report_id": "R022",
    "label": "Figure 6",
    "context": "financial professionals. Daily average of stock trading volumes surged to new highs of RMB2.8trn in Q2 (as of 18 June) and RMB2.6trn in Q1 2026 (Figure 6), after jumping to RMB2.0trn in Q4 and RMB2.1trn in Q3 from RMB1.2trn in Q2 2025. Fig. 5: Rising stock ind"
  },
  {
    "figure_id": "F553",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Secondary GFA sold last week was -20% wow and -13% yoy in c.20 cities"
  },
  {
    "figure_id": "F554",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Secondary GFA sold last week was -20% wow and -13% yoy in c.20 cities Average weekly volume of secondary property sales"
  },
  {
    "figure_id": "F555",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Secondary GFA sold last week was -20% wow and -13% yoy in c.20 cities Average weekly volume of secondary property sales Exhibit 4: Secondary GFA sold YTD was flat yoy in c.20 cities, while +20%/+9% vs. 2024/ s"
  },
  {
    "figure_id": "F556",
    "report_id": "R023",
    "label": "Exhibit 4",
    "context": "Exhibit 7: Inventory balance was $-0.2\\%$ wow, $-4.7\\%$ from end-25 levels c.20 cities' total inventory breakdown by city tier Exhibit 8: Inventory month was $-0.6\\%$ wow, representing $-0.9\\%$ from end-25 levels c.20 cities' inv"
  },
  {
    "figure_id": "F557",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Inventory balance was $-0.2\\%$ wow, $-4.7\\%$ from end-25 levels c.20 cities' total inventory breakdown by city tier Exhibit 8: Inventory month was $-0.6\\%$ wow, representing $-0.9\\%$ from end-25 levels c.20 cities' inv"
  },
  {
    "figure_id": "F558",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Exhibit 9: MTD GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model"
  },
  {
    "figure_id": "F559",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 9: MTD GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model Jan-Feb refers to average level in Jan and Feb. Exhibit 10: ...suggesting completions at a"
  },
  {
    "figure_id": "F560",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 9: MTD GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model Jan-Feb refers to average level in Jan and Feb. Exhibit 10: ...suggesting completions at a"
  },
  {
    "figure_id": "F561",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The total server market was \\~\\$284 bn in annual revenue in 2025, up +45% yoy driven by robust growth in AI server demand & higher ASPs Industry server revenue (\\$, mn) and growth (%) Exhibit 2: Industry server units w"
  },
  {
    "figure_id": "F562",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Vendor market share differs significantly by vertical & product (AI v. traditional)"
  },
  {
    "figure_id": "F563",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Vendor market share differs significantly by vertical & product (AI v. traditional) ## Traditional Servers The traditional server market was \\~\\$89 bn in annual revenue in 2025 (+10% yoy) with approximately 8.4 mn un"
  },
  {
    "figure_id": "F564",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Exhibit 4: The traditional server market was \\~\\$89 bn in annual revenue in 2025 (+10% yoy)..."
  },
  {
    "figure_id": "F565",
    "report_id": "R024",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The traditional server market was \\~\\$89 bn in annual revenue in 2025 (+10% yoy)... Industry traditional server revenue (\\$, mn) and annual growth rate (%) Exhibit 5: ... with approximately 8.4 mn units sold at an aver"
  },
  {
    "figure_id": "F566",
    "report_id": "R024",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Industry standard servers are based on the x86 CPU architecture Exhibit 7: The majority of traditional servers are rack-mounted or modular"
  },
  {
    "figure_id": "F567",
    "report_id": "R024",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Industry standard servers are based on the x86 CPU architecture Exhibit 7: The majority of traditional servers are rack-mounted or modular 2024 traditional (non-accelerated) server shipments by form factor The earlie"
  },
  {
    "figure_id": "F568",
    "report_id": "R024",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Servers are available in several form factors including mainframe, rack-mounted, blade, and tower"
  },
  {
    "figure_id": "F569",
    "report_id": "R024",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Servers are available in several form factors including mainframe, rack-mounted, blade, and tower Industry standard servers are based on the x86 CPU architecture, which is the most commonly deployed CPU architecture ac"
  },
  {
    "figure_id": "F570",
    "report_id": "R024",
    "label": "Exhibit 9",
    "context": "Exhibit 11: ... driven in large part by extended useful lives of servers at major hyperscalers"
  },
  {
    "figure_id": "F571",
    "report_id": "R024",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We estimate that 32% of the global server installed base is 5+ years old as of 2025, up meaningfully from 8% a decade ago... Global server installed by age (units, mn) and % of servers aged 5 years and older Exhibit 11"
  },
  {
    "figure_id": "F572",
    "report_id": "R024",
    "label": "Exhibit 10",
    "context": "Exhibit 12: DELL has reported that its 17G converts old 14G servers at a 6:1 ratio Illustrative comparison of 14G and 17G Dell servers specs"
  },
  {
    "figure_id": "F573",
    "report_id": "R024",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Assuming a 3:1 or 7:1 replacement rate on 14G older servers, Dell could shrink its server installed base by up to 60% in our illustrative scenario analysis Dell traditional server installed base scenario analysis Indus"
  },
  {
    "figure_id": "F574",
    "report_id": "R024",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Similarly, revenue share from the top 5 vendors has declined from 63% in 2014 to 57% in 2025 Share of traditional server industry revenue by vendor (%) The major driver of this shift is a change in underlying demand ac"
  },
  {
    "figure_id": "F575",
    "report_id": "R024",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Similarly, revenue share from the top 5 vendors has declined from 63% in 2014 to 57% in 2025 Share of traditional server industry revenue by vendor (%) The major driver of this shift is a change in underlying demand ac"
  },
  {
    "figure_id": "F576",
    "report_id": "R024",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Hyperscaler traditional server ASPs are \\~30% cheaper than enterprise ASPs in 2025 Traditional server ASP by customer vertical (\\$)"
  },
  {
    "figure_id": "F577",
    "report_id": "R024",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Hyperscaler traditional server ASPs are \\~30% cheaper than enterprise ASPs in 2025 Traditional server ASP by customer vertical (\\$) Exhibit 20: 650 Group estimates that 72% of the hyperscaler traditional server market"
  },
  {
    "figure_id": "F578",
    "report_id": "R024",
    "label": "Exhibit 18",
    "context": "Exhibit 20: 650 Group estimates that 72% of the hyperscaler traditional server market was addressed by ODMs/white box providers Traditional server revenue market share - hyperscaler customer vertical (%) Exhibit 21: As compared 98"
  },
  {
    "figure_id": "F579",
    "report_id": "R024",
    "label": "Exhibit 19",
    "context": "Exhibit 21: As compared 98% of the enterprise server market addressed by branded OEMs Traditional server revenue market share – enterprise customer vertical (%) ## Traditional server unit economics"
  },
  {
    "figure_id": "F580",
    "report_id": "R024",
    "label": "Exhibit 20",
    "context": "Exhibit 22: Traditional server bill of materials Illustrative bill of materials for a CPU general server"
  },
  {
    "figure_id": "F581",
    "report_id": "R024",
    "label": "Exhibit 23",
    "context": "Exhibit 23: The accelerated server market was \\~\\$195 bn in annual revenue in 2025 (+69% yoy)... Industry traditional server revenue (\\$, mn) and annual growth rate (%) Exhibit 24: ... with approximately 1.9 mn units sold (+27%) a"
  },
  {
    "figure_id": "F582",
    "report_id": "R024",
    "label": "Exhibit 23",
    "context": "Exhibit 25: A neural network is a basic computational model that is designed to recognize patterns and learn from data by finding connections between different interconnected nodes, or neurons"
  },
  {
    "figure_id": "F583",
    "report_id": "R024",
    "label": "Exhibit 25",
    "context": "Exhibit 26: The massive size of AI models (Llama 4 is reported to have anywhere between 2.0 trillion parameters) makes accelerated servers not just an advantage but a necessity to train models in a feasible amount of time Paramete"
  },
  {
    "figure_id": "F584",
    "report_id": "R024",
    "label": "Exhibit 25",
    "context": "Exhibit 26: The massive size of AI models (Llama 4 is reported to have anywhere between 2.0 trillion parameters) makes accelerated servers not just an advantage but a necessity to train models in a feasible amount of time Paramete"
  },
  {
    "figure_id": "F585",
    "report_id": "R024",
    "label": "Exhibit 27",
    "context": "Beyond model training, accelerated compute also plays a role in inference and RAG. First, AI inference is the process of using a trained AI model to make predictions on new data. Although requiring less raw computational power than training an AI model, AI inf"
  },
  {
    "figure_id": "F586",
    "report_id": "R024",
    "label": "Exhibit 29",
    "context": "Exhibit 29: 19.8% of Firms Across All Industries Have Adopted AI as of April 2026 Share of US firms using AI by sector (%) Exhibit 30: Current Adoption is highest among medium-sized and large enterprises Share of US firms using AI"
  },
  {
    "figure_id": "F587",
    "report_id": "R024",
    "label": "Exhibit 29",
    "context": "Exhibit 29: 19.8% of Firms Across All Industries Have Adopted AI as of April 2026 Share of US firms using AI by sector (%) Exhibit 30: Current Adoption is highest among medium-sized and large enterprises Share of US firms using AI"
  },
  {
    "figure_id": "F588",
    "report_id": "R024",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Current Adoption is highest among medium-sized and large enterprises Share of US firms using AI by number of employees Share of US Firms Using AI by Number of Employees \\*6 survey moving average. \\*\\*Spot data shown si"
  },
  {
    "figure_id": "F589",
    "report_id": "R024",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Hyperscalers account for the majority of industry AI server revenue as of 2025... AI server revenue (\\$, bn) Exhibit 32: .. with the highest share of AI server unit shipments... AI server shipments (units, mn) Exhibi"
  },
  {
    "figure_id": "F590",
    "report_id": "R024",
    "label": "Exhibit 31",
    "context": "Exhibit 34: The hyperscaler AI server market is dominated by white box..."
  },
  {
    "figure_id": "F591",
    "report_id": "R024",
    "label": "Exhibit 32",
    "context": "Exhibit 32: .. with the highest share of AI server unit shipments... AI server shipments (units, mn) Exhibit 33: ... but the lowest AI server ASP AI server ASP (\\$) Exhibit 34: The hyperscaler AI server market is dominated by wh"
  },
  {
    "figure_id": "F592",
    "report_id": "R024",
    "label": "Exhibit 33",
    "context": "Exhibit 35: ... while the tier 2 market is lead by best-in-breed server vendors DELL & SMCI"
  },
  {
    "figure_id": "F593",
    "report_id": "R024",
    "label": "Exhibit 34",
    "context": "Exhibit 36: The enterprise AI server market is more balanced across HPE, DELL, and Nvidia Enterprise AI server market share (% of total)"
  },
  {
    "figure_id": "F594",
    "report_id": "R024",
    "label": "Exhibit 35",
    "context": "Exhibit 35: ... while the tier 2 market is lead by best-in-breed server vendors DELL & SMCI Exhibit 36: The enterprise AI server market is more balanced across HPE, DELL, and Nvidia Enterprise AI server market share (% of total)"
  },
  {
    "figure_id": "F595",
    "report_id": "R024",
    "label": "Exhibit 40",
    "context": "Exhibit 38: DDR5 16Gb spot is trading at 10% premium vs. latest contract price DDR5 16Gb spot pricing premium/discount vs. contract Hardware OEMs have a well-established playbook for managing typical commodity cost volatility, inc"
  },
  {
    "figure_id": "F596",
    "report_id": "R025",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: We see a 73-96% correlation between BigOne Lab quarterly brewer value growth and reported revenue growth CRBeer reports semi-annually"
  },
  {
    "figure_id": "F597",
    "report_id": "R025",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: We see a 73-96% correlation between BigOne Lab quarterly brewer value growth and reported revenue growth CRBeer reports semi-annually ## MONTHLY OVERVIEW Our BigOne Lab China beer data set leverages the POS sell-out da"
  },
  {
    "figure_id": "F598",
    "report_id": "R025",
    "label": "Exhibit 3",
    "context": "EXHIBIT 5: Off-trade value was in marginal growth at +1% YoY in the month"
  },
  {
    "figure_id": "F599",
    "report_id": "R025",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Off-trade value was in marginal growth at +1% YoY in the month China Off-Trade Beer Value Growth Monthly YoY % China Total Beer Value Growth YoY% by Brewer"
  },
  {
    "figure_id": "F600",
    "report_id": "R025",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 6: In Q1 Bud China / Chongqing / Yanjing performed sequentially better than Q4 EXHIBIT 7: Monthly value growth improved for CRBeer but worsened for Chongqing / Yanjing / Tsingtao in May vs April"
  },
  {
    "figure_id": "F601",
    "report_id": "R025",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 7: Monthly value growth improved for CRBeer but worsened for Chongqing / Yanjing / Tsingtao in May vs April China Total Beer Value Growth YoY% by Brewer EXHIBIT 8: Yanjing materially outperformed in most segments in the m"
  },
  {
    "figure_id": "F602",
    "report_id": "R025",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: Yanjing materially outperformed in most segments in the month Beer Value YoY % in May 2026 by Segment by Brewer (Both Channel) EXHIBIT 9: Yanjing & Chongqing were top in share gains while Bud China's share loss narrowe"
  },
  {
    "figure_id": "F603",
    "report_id": "R025",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: And similarly in May vs April China Total Beer Value Share Gain/Loss (YoY in bps)"
  },
  {
    "figure_id": "F604",
    "report_id": "R025",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: And similarly in May vs April China Total Beer Value Share Gain/Loss (YoY in bps) EXHIBIT 11: At the national level Bud China's share loss was across the board in May while CRB gained the most in Super Premium and M/S&"
  },
  {
    "figure_id": "F605",
    "report_id": "R025",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: At the national level Bud China's share loss was across the board in May while CRB gained the most in Super Premium and M/S&Econ May '26 National Segment Share Gain/Loss in bps YoY EXHIBIT 12: In the Off-Trade, Bud Chi"
  },
  {
    "figure_id": "F606",
    "report_id": "R025",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 12: In the Off-Trade, Bud China was maintaining its share in MS+ May '26 National Off-Trade Segment Share Gain/Loss in bps YoY EXHIBIT 13: And they even gained share in Premium segment of Restaurant channel May '26 Nationa"
  },
  {
    "figure_id": "F607",
    "report_id": "R025",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 13: And they even gained share in Premium segment of Restaurant channel May '26 National Restaurant Segment Share Gain/Loss in bps YoY EXHIBIT 14: In June comps are softer for CRBeer and Bud China but tougher for Chongqing"
  },
  {
    "figure_id": "F608",
    "report_id": "R025",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 14: In June comps are softer for CRBeer and Bud China but tougher for Chongqing and Yanjing Forthcoming Comps - China Total Beer Value Growth YoY% by Brewer"
  },
  {
    "figure_id": "F609",
    "report_id": "R025",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: In June comps are softer for CRBeer and Bud China but tougher for Chongqing and Yanjing Forthcoming Comps - China Total Beer Value Growth YoY% by Brewer EXHIBIT 15: By province Jiangsu and Zhejiang were improving MoM i"
  },
  {
    "figure_id": "F610",
    "report_id": "R025",
    "label": "Exhibit 17",
    "context": "EXHIBIT 17: Bud China Value bridge by PROVINCE Bud China Value Bridge by PROVINCE (Indexed to May '25 = 100) Restaurant Channel EXHIBIT 18: Bud China Value bridge by SEGMENT Bud China Value Bridge by SEGMENT (Indexed to May '25"
  },
  {
    "figure_id": "F611",
    "report_id": "R025",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Bud China Value bridge by PROVINCE Bud China Value Bridge by PROVINCE (Indexed to May '25 = 100) Restaurant Channel EXHIBIT 18: Bud China Value bridge by SEGMENT Bud China Value Bridge by SEGMENT (Indexed to May '25"
  },
  {
    "figure_id": "F612",
    "report_id": "R025",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Bud China Value bridge by SEGMENT Bud China Value Bridge by SEGMENT (Indexed to May '25 = 100) EXHIBIT 19: Bud China monthly growth diagnostic by Province and Segment and Channel"
  },
  {
    "figure_id": "F613",
    "report_id": "R025",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Bud China Value bridge by SEGMENT Bud China Value Bridge by SEGMENT (Indexed to May '25 = 100) EXHIBIT 19: Bud China monthly growth diagnostic by Province and Segment and Channel ## CRBEER"
  },
  {
    "figure_id": "F614",
    "report_id": "R025",
    "label": "Exhibit 21",
    "context": "EXHIBIT 20: CRBeer Value bridge by PROVINCE CRBeer Value Bridge by PROVINCE (Indexed to May '25 = 100) Off-Trade Channel Restaurant Channel EXHIBIT 21: CRBeer Value bridge by SEGMENT CRBeer Value Bridge by SEGMENT (Indexed to Ma"
  },
  {
    "figure_id": "F615",
    "report_id": "R025",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: CRBeer Value bridge by SEGMENT CRBeer Value Bridge by SEGMENT (Indexed to May '25 = 100) Off-Trade Channel Restaurant Channel"
  },
  {
    "figure_id": "F616",
    "report_id": "R025",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: CRBeer Value bridge by SEGMENT CRBeer Value Bridge by SEGMENT (Indexed to May '25 = 100) Off-Trade Channel Restaurant Channel Restaurant Channel EXHIBIT 22: CRBeer monthly growth diagnostic by Province and Segment an"
  },
  {
    "figure_id": "F617",
    "report_id": "R025",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: CRBeer Value bridge by SEGMENT CRBeer Value Bridge by SEGMENT (Indexed to May '25 = 100) Off-Trade Channel Restaurant Channel Restaurant Channel EXHIBIT 22: CRBeer monthly growth diagnostic by Province and Segment an"
  },
  {
    "figure_id": "F618",
    "report_id": "R025",
    "label": "Exhibit 23",
    "context": "EXHIBIT 23: Tsingtao Value bridge by PROVINCE Tsingtao Value Bridge by PROVINCE (Indexed to May '25 = 100) Off-Trade Channel Off-Trade Channel EXHIBIT 24: Tsingtao Value bridge by SEGMENT Tsingtao Value Bridge by SEGMENT (Indexe"
  },
  {
    "figure_id": "F619",
    "report_id": "R025",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Tsingtao Value bridge by SEGMENT Tsingtao Value Bridge by SEGMENT (Indexed to May '25 = 100)"
  },
  {
    "figure_id": "F620",
    "report_id": "R025",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Tsingtao Value bridge by SEGMENT Tsingtao Value Bridge by SEGMENT (Indexed to May '25 = 100) EXHIBIT 25: Tsingtao monthly growth diagnostic by Province and Segment and Channel"
  },
  {
    "figure_id": "F621",
    "report_id": "R025",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Tsingtao Value bridge by SEGMENT Tsingtao Value Bridge by SEGMENT (Indexed to May '25 = 100) EXHIBIT 25: Tsingtao monthly growth diagnostic by Province and Segment and Channel ## CHONGQING"
  },
  {
    "figure_id": "F622",
    "report_id": "R025",
    "label": "Exhibit 26",
    "context": "EXHIBIT 26: Chongqing Value bridge by PROVINCE Chongqing Value Bridge by PROVINCE (Indexed to Apr '25 = 100) Off-Trade Channel Restaurant Channel EXHIBIT 27: Chongqing Value bridge by SEGMENT Chongqing Value Bridge by SEGMENT (I"
  },
  {
    "figure_id": "F623",
    "report_id": "R025",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Chongqing Value bridge by SEGMENT Chongqing Value Bridge by SEGMENT (Indexed to Apr '25 = 100) Off-Trade Channel Restaurant Channel"
  },
  {
    "figure_id": "F624",
    "report_id": "R025",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Chongqing Value bridge by SEGMENT Chongqing Value Bridge by SEGMENT (Indexed to Apr '25 = 100) Off-Trade Channel Restaurant Channel Restaurant Channel EXHIBIT 28: Chongqing monthly growth diagnostic by Province and S"
  },
  {
    "figure_id": "F625",
    "report_id": "R025",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Chongqing Value bridge by SEGMENT Chongqing Value Bridge by SEGMENT (Indexed to Apr '25 = 100) Off-Trade Channel Restaurant Channel Restaurant Channel EXHIBIT 28: Chongqing monthly growth diagnostic by Province and S"
  },
  {
    "figure_id": "F626",
    "report_id": "R025",
    "label": "Exhibit 29",
    "context": "EXHIBIT 29: Yanjing Value bridge by PROVINCE Yanjing Value Bridge by PROVINCE (Indexed to May '25 = 100) EXHIBIT 30: Yanjing Value bridge by SEGMENT Yanjing Value Bridge by SEGMENT (Indexed to May '25 = 100)"
  },
  {
    "figure_id": "F627",
    "report_id": "R025",
    "label": "Exhibit 29",
    "context": "EXHIBIT 29: Yanjing Value bridge by PROVINCE Yanjing Value Bridge by PROVINCE (Indexed to May '25 = 100) EXHIBIT 30: Yanjing Value bridge by SEGMENT Yanjing Value Bridge by SEGMENT (Indexed to May '25 = 100)"
  },
  {
    "figure_id": "F628",
    "report_id": "R025",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Yanjing Value bridge by SEGMENT Yanjing Value Bridge by SEGMENT (Indexed to May '25 = 100) EXHIBIT 31: Yanjing monthly growth diagnostic by Province and Segment and Channel"
  },
  {
    "figure_id": "F629",
    "report_id": "R025",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Yanjing Value bridge by SEGMENT Yanjing Value Bridge by SEGMENT (Indexed to May '25 = 100) EXHIBIT 31: Yanjing monthly growth diagnostic by Province and Segment and Channel ## APPENDIX - PROVINCE ABBREVIATION"
  },
  {
    "figure_id": "F630",
    "report_id": "R026",
    "label": "Figure 3",
    "context": "Asahi Kasei — Asahi Kasei's PIMEL, used as a redistribution layer (RDL) material, has an extremely high share in cutting edge applications at key customers, with supply struggling to keep up with demand. The company plans to bring forward production increases."
  },
  {
    "figure_id": "F631",
    "report_id": "R026",
    "label": "Figure 3",
    "context": "■ PTFE — We attended a talk on PTFE at JPCA 2026 (Total Solution Exhibition for Electronic Equipment) held on June 10-12. PTFE's extremely favorable low-Dk and low-Df characteristics mean it is expected to be used in high-speed, high-volume, low-latency PCBs. "
  },
  {
    "figure_id": "F632",
    "report_id": "R026",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. JXAM: Product deployment in data centers (particularly AI servers) © 2026 Citi Inc. No redistribution without Citi's written permission. Note: All numbers are Citi estimates."
  },
  {
    "figure_id": "F633",
    "report_id": "R026",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: All numbers are Citi estimates. Figure 4. Resins with low dielectric properties and OPE application areas © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5"
  },
  {
    "figure_id": "F634",
    "report_id": "R026",
    "label": "Figure 4",
    "context": "Figure 4. Resins with low dielectric properties and OPE application areas © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. AGC's solutions for semiconductor target applications # Appendix A-1"
  },
  {
    "figure_id": "F635",
    "report_id": "R027",
    "label": "Exhibit 1",
    "context": "Exhibit 1: STMicro - 32F103VET6 spot market price trend Exhibit 2: GigaDevice - 32F103VET6 spot market price trend Daniel Yen, CFA"
  },
  {
    "figure_id": "F636",
    "report_id": "R027",
    "label": "Exhibit 1",
    "context": "Exhibit 1: STMicro - 32F103VET6 spot market price trend Exhibit 2: GigaDevice - 32F103VET6 spot market price trend Daniel Yen, CFA Charlie Chan"
  },
  {
    "figure_id": "F637",
    "report_id": "R029",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Fiscal revenue growth continued to outperform fiscal spending growth in May Exhibit 2: Property-related government revenue continued to weaken in May Exhibit 3: Our augmented fiscal deficit (AFD) metric tightened fur"
  },
  {
    "figure_id": "F638",
    "report_id": "R029",
    "label": "Exhibit 1",
    "context": "Exhibit 4: China's fiscal \"spend-through\" ratio rose slightly in May on a 12mma basis"
  },
  {
    "figure_id": "F639",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 5: Fiscal impulse has weighed on sequential growth in Q2, while we expect it to be more supportive of growth in H2"
  },
  {
    "figure_id": "F640",
    "report_id": "R029",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Fiscal impulse has weighed on sequential growth in Q2, while we expect it to be more supportive of growth in H2 ## The China Economics Team"
  },
  {
    "figure_id": "F641",
    "report_id": "R029",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Fiscal impulse has weighed on sequential growth in Q2, while we expect it to be more supportive of growth in H2 ## The China Economics Team Andrew Tilton GS (Asia) L.L.C."
  },
  {
    "figure_id": "F642",
    "report_id": "R031",
    "label": "Figure 1",
    "context": "Figure 1: Cap goods sales growth correlation to German IP vs price performance since Iran war"
  },
  {
    "figure_id": "F643",
    "report_id": "R031",
    "label": "Figure 1",
    "context": "Figure 1: Cap goods sales growth correlation to German IP vs price performance since Iran war"
  },
  {
    "figure_id": "F644",
    "report_id": "R031",
    "label": "Figure 4",
    "context": "Figure 4: Capital Goods SMID Caps (2026e)"
  },
  {
    "figure_id": "F645",
    "report_id": "R031",
    "label": "Figure 4",
    "context": "Figure 6: Europe YTD performance"
  },
  {
    "figure_id": "F646",
    "report_id": "R031",
    "label": "Figure 4",
    "context": "Figure 6: Europe YTD performance"
  },
  {
    "figure_id": "F647",
    "report_id": "R031",
    "label": "Figure 5",
    "context": "Figure 8: US YTD performance"
  },
  {
    "figure_id": "F648",
    "report_id": "R031",
    "label": "Figure 6",
    "context": "Figure 8: US YTD performance"
  },
  {
    "figure_id": "F649",
    "report_id": "R031",
    "label": "Figure 8",
    "context": "Figure 10: Asia YTD performance"
  },
  {
    "figure_id": "F650",
    "report_id": "R031",
    "label": "Figure 8",
    "context": "Figure 10: Asia YTD performance"
  },
  {
    "figure_id": "F651",
    "report_id": "R031",
    "label": "Figure 10",
    "context": "Figure 10: Asia YTD performance"
  },
  {
    "figure_id": "F652",
    "report_id": "R032",
    "label": "Figure 1",
    "context": "Figure 1: Precious metal forecasts Figure 2: Gold negatively linked to oil in March & April Figure 3: Gold linkage to Fed pricing more influential after May Although the sources of inflation are quite broad-based (Link) and th"
  },
  {
    "figure_id": "F653",
    "report_id": "R032",
    "label": "Figure 2",
    "context": "Figure 2: Gold negatively linked to oil in March & April Figure 3: Gold linkage to Fed pricing more influential after May Although the sources of inflation are quite broad-based (Link) and there are numerous reasons to doubt t"
  },
  {
    "figure_id": "F654",
    "report_id": "R032",
    "label": "Figure 4",
    "context": "Figure 5: US FCI index eased since March Last but not least, Fed Chair Warsh was equivocal on the nature of the current policy setting. Chair Warsh indicated that \"Broadly I would say there Fed policy appears to be somewhat rest"
  },
  {
    "figure_id": "F655",
    "report_id": "R032",
    "label": "Figure 4",
    "context": "Figure 5: US FCI index eased since March Last but not least, Fed Chair Warsh was equivocal on the nature of the current policy setting. Chair Warsh indicated that \"Broadly I would say there Fed policy appears to be somewhat rest"
  },
  {
    "figure_id": "F656",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "Figure 5: US FCI index eased since March Last but not least, Fed Chair Warsh was equivocal on the nature of the current policy setting. Chair Warsh indicated that \"Broadly I would say there Fed policy appears to be somewhat rest"
  },
  {
    "figure_id": "F657",
    "report_id": "R032",
    "label": "Figure 7",
    "context": "Figure 8: Gold and Fed hiking cycle over 2022-23 ## Short-term flow factors appear weak We look at three components of short-term flow which are not encouraging at this moment in time. First, ETF assets across US, Europe, Chin"
  },
  {
    "figure_id": "F658",
    "report_id": "R032",
    "label": "Figure 7",
    "context": "Figure 8: Gold and Fed hiking cycle over 2022-23 ## Short-term flow factors appear weak We look at three components of short-term flow which are not encouraging at this moment in time. First, ETF assets across US, Europe, Chin"
  },
  {
    "figure_id": "F659",
    "report_id": "R032",
    "label": "Figure 11",
    "context": "Figure 10: ETF investment nearly zero year to date; would need to rise to 5 mm troy oz to imply gold at USD 4,800/oz Figure 11: Gold progressively responding more steeply to any given ETF volume change Second, China and India g"
  },
  {
    "figure_id": "F660",
    "report_id": "R032",
    "label": "Figure 10",
    "context": "Figure 10: ETF investment nearly zero year to date; would need to rise to 5 mm troy oz to imply gold at USD 4,800/oz Figure 11: Gold progressively responding more steeply to any given ETF volume change Second, China and India g"
  },
  {
    "figure_id": "F661",
    "report_id": "R032",
    "label": "Figure 13",
    "context": "Figure 14: China discount or smaller premium is associated with lower gold imports"
  },
  {
    "figure_id": "F662",
    "report_id": "R032",
    "label": "Figure 14",
    "context": "Figure 14: China discount or smaller premium is associated with lower gold imports ## Longer-term gold drivers"
  },
  {
    "figure_id": "F663",
    "report_id": "R032",
    "label": "Figure 14",
    "context": "Figure 15: Long-term gold model sees debt growth as structurally positive driver"
  },
  {
    "figure_id": "F664",
    "report_id": "R032",
    "label": "Figure 15",
    "context": "Figure 15: Long-term gold model sees debt growth as structurally positive driver Figure 16: US public debt growth faster than CBO projection Second, the higher pace of central bank demand since 2022 may also be structural in na"
  },
  {
    "figure_id": "F665",
    "report_id": "R032",
    "label": "Figure 15",
    "context": "Figure 15: Long-term gold model sees debt growth as structurally positive driver Figure 16: US public debt growth faster than CBO projection Second, the higher pace of central bank demand since 2022 may also be structural in na"
  },
  {
    "figure_id": "F666",
    "report_id": "R032",
    "label": "Figure 19",
    "context": "Figure 17: Unreported official demand higher than expected in Q1 Figure 18: Relationship between unreported official demand and China still reasonably strong Figure 19: Q1 official demand highest yet in real USD terms"
  },
  {
    "figure_id": "F667",
    "report_id": "R032",
    "label": "Figure 17",
    "context": "Figure 17: Unreported official demand higher than expected in Q1 Figure 18: Relationship between unreported official demand and China still reasonably strong Figure 19: Q1 official demand highest yet in real USD terms Figure"
  },
  {
    "figure_id": "F668",
    "report_id": "R032",
    "label": "Figure 18",
    "context": "Figure 18: Relationship between unreported official demand and China still reasonably strong Figure 19: Q1 official demand highest yet in real USD terms Figure 20: Q1 jewellery demand sees lowest quarter since Q2-20 Figure 21"
  },
  {
    "figure_id": "F669",
    "report_id": "R032",
    "label": "Figure 19",
    "context": "Figure 19: Q1 official demand highest yet in real USD terms Figure 20: Q1 jewellery demand sees lowest quarter since Q2-20 Figure 21: Jewellery demand is typically elastic, yielding supply to inelastic demand (ETF and CB) ##"
  },
  {
    "figure_id": "F670",
    "report_id": "R032",
    "label": "Figure 20",
    "context": "Figure 20: Q1 jewellery demand sees lowest quarter since Q2-20 Figure 21: Jewellery demand is typically elastic, yielding supply to inelastic demand (ETF and CB) ## Appendix 1"
  },
  {
    "figure_id": "F671",
    "report_id": "R033",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Exports remain the best performing part of the economy Exhibit 2: Domestic sales of autos dropped 22% yoy in May while exports jumped 75% yoy ## A Slower Q2 and a Faster Q3"
  },
  {
    "figure_id": "F672",
    "report_id": "R033",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Exports remain the best performing part of the economy Exhibit 2: Domestic sales of autos dropped 22% yoy in May while exports jumped 75% yoy ## A Slower Q2 and a Faster Q3 Given the April and May realized data, we n"
  },
  {
    "figure_id": "F673",
    "report_id": "R033",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Local government special bond issuance slowed after Q1 Exhibit 4: We nudge down Q2 sequential real GDP growth forecast while raising Q3 forecast"
  },
  {
    "figure_id": "F674",
    "report_id": "R033",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Physical output of industrial robots and semiconductors climbed while that of glass and cement fell Exhibit 6: In the onshore equity market, tech index rallied while consumer index slid ## Racing for AI in a differen"
  },
  {
    "figure_id": "F675",
    "report_id": "R033",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Physical output of industrial robots and semiconductors climbed while that of glass and cement fell Exhibit 6: In the onshore equity market, tech index rallied while consumer index slid ## Racing for AI in a differen"
  },
  {
    "figure_id": "F676",
    "report_id": "R033",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Hyperscaler capex is much lower in China than in the US Exhibit 8: China's installed data center capacity was $60\\%$ of that in the US as of June 2025 As China continues to push aggressively on tech and AI advancemen"
  },
  {
    "figure_id": "F677",
    "report_id": "R033",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Hyperscaler capex is much lower in China than in the US Exhibit 8: China's installed data center capacity was $60\\%$ of that in the US as of June 2025 As China continues to push aggressively on tech and AI advancemen"
  },
  {
    "figure_id": "F678",
    "report_id": "R033",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Rising unemployment often precedes falling rents in China ## Policymakers focusing on the long-term"
  },
  {
    "figure_id": "F679",
    "report_id": "R033",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Rising unemployment often precedes falling rents in China ## Policymakers focusing on the long-term Recent policy news has focused on long-term strategies. The State Council Decree 834, published in April, addressed su"
  },
  {
    "figure_id": "F680",
    "report_id": "R034",
    "label": "Exhibit 2",
    "context": "TRACKING U.S. SUPPLY CHAIN CONGESTION # GS Supply Chain Congestion Scale: June 22nd; Index Lower W/W, Bottleneck Scale Unchanged at '2' GS Supply Chain Congestion Scale Week of 6/22/2026 Scale is based solely off weekly metrics to give more granularity on high"
  },
  {
    "figure_id": "F681",
    "report_id": "R034",
    "label": "Exhibit 9",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F682",
    "report_id": "R034",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F683",
    "report_id": "R034",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 3/1\\* container ships backed up this week on the East/West Coast West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - June 2026 \\*East Coast is estimated via satellite data - includes container ships"
  },
  {
    "figure_id": "F684",
    "report_id": "R034",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~13% YoY on average in June West Coast Class 1 Rail Inter"
  },
  {
    "figure_id": "F685",
    "report_id": "R034",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~13% YoY on average in June West Coast Class 1 Rail Inter"
  },
  {
    "figure_id": "F686",
    "report_id": "R034",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast"
  },
  {
    "figure_id": "F687",
    "report_id": "R034",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast Rate is \\$ per FEU (Forty-Foot Equivalent Unit) ## Lagged Monthly Indicators (April Data) San Pedro's Bay Container Dwell \\- Container weighte"
  },
  {
    "figure_id": "F688",
    "report_id": "R034",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days Exhibit 12: % of Containers Dwelling More than 5 Days Exhibit 13: Rail Container Dwell Time, Days"
  },
  {
    "figure_id": "F689",
    "report_id": "R034",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days Exhibit 12: % of Containers Dwelling More than 5 Days Exhibit 13: Rail Container Dwell Time, Days \"Big Three\" West Coast Ports' Inbound Loaded Containe"
  },
  {
    "figure_id": "F690",
    "report_id": "R034",
    "label": "Exhibit 12",
    "context": "Exhibit 14: West Coast Ports' Inbound Loaded Containers -1.0% YoY in April"
  },
  {
    "figure_id": "F691",
    "report_id": "R034",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Door to Door Shipping Days, China to US"
  },
  {
    "figure_id": "F692",
    "report_id": "R034",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted"
  },
  {
    "figure_id": "F693",
    "report_id": "R034",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted ## LMI Capacity and Utilization ■ LMI Transportation Capacity Index Transportation capacity contracted in April given the 28.4 reading; the reading decreas"
  },
  {
    "figure_id": "F694",
    "report_id": "R034",
    "label": "Exhibit 17",
    "context": "Exhibit 17: PMI: Manufacturing Suppliers' Delivery Times, YoY, Seasonally Adjusted ## Appendix Given the importance supply chain fluidity has on retailers, consumer goods companies, inflationary pricing, etc., we think this scale'"
  },
  {
    "figure_id": "F695",
    "report_id": "R034",
    "label": "Exhibit 19",
    "context": "Exhibit 18: The weekly composite index (light blue) leads the monthly (dark blue); expect future monthly updates to confirm recent weekly trends Exhibit 19: Our combined scale averaged ‘108’ in April, indicating a bottleneck score"
  },
  {
    "figure_id": "F696",
    "report_id": "R034",
    "label": "Exhibit 18",
    "context": "Exhibit 20: GS Legacy Supply Chain Congestion Scale (incorporates monthly and weekly data)"
  },
  {
    "figure_id": "F697",
    "report_id": "R035",
    "label": "Figure 1",
    "context": "Figure 1: Trade balance March-May, seasonally-adjusted ## Pakistan's budget offers too narrow a path to fiscal targets Pakistan's FY2026/27 draft budget, which we discussed in a recent note, reaffirms commitment to the IMF progr"
  },
  {
    "figure_id": "F698",
    "report_id": "R035",
    "label": "Figure 2",
    "context": "Figure 2: SBP's interest rate corridor Figure 3. Pakistan: Inflation Data releases and forecasts Week of Jun 22 - 26 No data releases."
  },
  {
    "figure_id": "F699",
    "report_id": "R035",
    "label": "Figure 2",
    "context": "Figure 2: SBP's interest rate corridor Figure 3. Pakistan: Inflation Data releases and forecasts Week of Jun 22 - 26 No data releases. Review of past week's data"
  },
  {
    "figure_id": "F700",
    "report_id": "R036",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Cumulative outperformance Exhibit 3: Weekly hit ratio Three Actionable Ideas are not and should not be considered a portfolio: Each investment idea is chosen based on its own merit and without any consideration of th"
  },
  {
    "figure_id": "F701",
    "report_id": "R036",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Three Actionable Ideas – Still in effect"
  },
  {
    "figure_id": "F702",
    "report_id": "R036",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Number of ideas, by market Exhibit 7: Idea performance, by market"
  },
  {
    "figure_id": "F703",
    "report_id": "R037",
    "label": "Figure 1",
    "context": "## Shreyas Madabushi Figure 1. Lithium carbonate monthly inventory Figure 2. Lithium carbonate weekly inventory Figure 3. Spread of battery-grade LC (assume 1M inventory)"
  },
  {
    "figure_id": "F704",
    "report_id": "R037",
    "label": "Figure 1",
    "context": "Figure 1. Lithium carbonate monthly inventory Figure 2. Lithium carbonate weekly inventory Figure 3. Spread of battery-grade LC (assume 1M inventory) Figure 4. Spread of battery-grade LC (assume 1M inventory)"
  },
  {
    "figure_id": "F705",
    "report_id": "R037",
    "label": "Figure 2",
    "context": "Figure 2. Lithium carbonate weekly inventory Figure 3. Spread of battery-grade LC (assume 1M inventory) Figure 4. Spread of battery-grade LC (assume 1M inventory) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Lithium carbonate"
  },
  {
    "figure_id": "F706",
    "report_id": "R037",
    "label": "Figure 3",
    "context": "Figure 3. Spread of battery-grade LC (assume 1M inventory) Figure 4. Spread of battery-grade LC (assume 1M inventory) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Lithium carbonate monthly production Figure 6. Lithium carbona"
  },
  {
    "figure_id": "F707",
    "report_id": "R037",
    "label": "Figure 4",
    "context": "Figure 4. Spread of battery-grade LC (assume 1M inventory) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Lithium carbonate monthly production Figure 6. Lithium carbonate weekly production"
  },
  {
    "figure_id": "F708",
    "report_id": "R037",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Lithium carbonate monthly production Figure 6. Lithium carbonate weekly production ## Appendix A-1"
  },
  {
    "figure_id": "F709",
    "report_id": "R038",
    "label": "Figure 1",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F710",
    "report_id": "R038",
    "label": "Figure 1",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. GMV growth in apparel category by platforms during 6.18 © 2026 Citi Inc. No redistribution without Citi's writ"
  },
  {
    "figure_id": "F711",
    "report_id": "R038",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. GMV growth in apparel category by platforms during 6.18 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. GMV growth in home living category by platfo"
  },
  {
    "figure_id": "F712",
    "report_id": "R038",
    "label": "Figure 3",
    "context": "Figure 3. GMV growth in apparel category by platforms during 6.18 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. GMV growth in home living category by platforms during 6.18 © 2026 Citi Inc. No redistribution without Citi's writ"
  },
  {
    "figure_id": "F713",
    "report_id": "R039",
    "label": "Exhibit 1",
    "context": "Exhibit 2: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai"
  },
  {
    "figure_id": "F714",
    "report_id": "R039",
    "label": "Exhibit 2",
    "context": "Exhibit 2: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai ## Key news this week: Moutai announced its 2025 final dividend distribution (Jun 21): Moutai's 2025 dividend distribution"
  },
  {
    "figure_id": "F715",
    "report_id": "R039",
    "label": "Exhibit 3",
    "context": "Exhibit 3: 53% Feitian Moutai product prices Most recent data points as of Jun 21, 2026. Exhibit 4: 52% Common Wuliangye product prices Most recent data points as of Jun 21, 2026."
  },
  {
    "figure_id": "F716",
    "report_id": "R039",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Guojiao 1573 product prices Most recent data points as of Jun 21, 2026."
  },
  {
    "figure_id": "F717",
    "report_id": "R039",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Wholesale prices of Moutai's 4 non-standard SKUs Rmb/bottle Jingpin Moutai (53%, 500ml)"
  },
  {
    "figure_id": "F718",
    "report_id": "R039",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Wholesale prices of Moutai's 4 non-standard SKUs Rmb/bottle Jingpin Moutai (53%, 500ml) Latest data as of Jun 21, 2026. Rmb/bottle Moutai 15 years (53%, 500ml)"
  },
  {
    "figure_id": "F719",
    "report_id": "R039",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Wholesale prices of Moutai's 4 non-standard SKUs Rmb/bottle Jingpin Moutai (53%, 500ml) Latest data as of Jun 21, 2026. Rmb/bottle Moutai 15 years (53%, 500ml)"
  },
  {
    "figure_id": "F720",
    "report_id": "R039",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Wholesale prices of Moutai's 4 non-standard SKUs Rmb/bottle Jingpin Moutai (53%, 500ml) Latest data as of Jun 21, 2026. Rmb/bottle Moutai 15 years (53%, 500ml)"
  },
  {
    "figure_id": "F721",
    "report_id": "R039",
    "label": "Exhibit 7",
    "context": "Rmb/bottle Jingpin Moutai (53%, 500ml) Latest data as of Jun 21, 2026. Rmb/bottle Moutai 15 years (53%, 500ml)"
  },
  {
    "figure_id": "F722",
    "report_id": "R039",
    "label": "Exhibit 9",
    "context": "Exhibit 10: China Spirits Comps"
  },
  {
    "figure_id": "F723",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect China AI chip TAM to grow to US\\$91bn by 2030E Exhibit 2: We expect China AI chip self-sufficiency to reach 70% in 2030E ## China Semi Equipment Import Trends"
  },
  {
    "figure_id": "F724",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect China AI chip TAM to grow to US\\$91bn by 2030E Exhibit 2: We expect China AI chip self-sufficiency to reach 70% in 2030E ## China Semi Equipment Import Trends China's semi equipment import value was US\\$2.4"
  },
  {
    "figure_id": "F725",
    "report_id": "R041",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Growth in China's semi equipment imports declined to -9% Y/Y (3MMA) in Apr 2026 Exhibit 4: Semi equipment imports from most major countries was down yoy (YTD) ## Monthly Performance and Catalysts"
  },
  {
    "figure_id": "F726",
    "report_id": "R041",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Growth in China's semi equipment imports declined to -9% Y/Y (3MMA) in Apr 2026 Exhibit 4: Semi equipment imports from most major countries was down yoy (YTD) ## Monthly Performance and Catalysts Outperformers: ACMR"
  },
  {
    "figure_id": "F727",
    "report_id": "R041",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Share price performance of key Chinese semi localization stocks Exhibit 8: Exhibit 6: 12-month share price performance, by segment Exhibit 7: Key stocks' 12-month share price performance Greater China semi localizati"
  },
  {
    "figure_id": "F728",
    "report_id": "R041",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Exhibit 6: 12-month share price performance, by segment Exhibit 7: Key stocks' 12-month share price performance Greater China semi localization stocks' performance trends ## Catalysts and key events"
  },
  {
    "figure_id": "F729",
    "report_id": "R041",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Key stocks' 12-month share price performance Greater China semi localization stocks' performance trends ## Catalysts and key events ## Cambricon: Earnings estimate revisions and quarterly financials"
  },
  {
    "figure_id": "F730",
    "report_id": "R041",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Cambricon: Residual income model Exhibit 12: Cambricon: One-year forward P/S trend ## Risk Reward – Cambricon Technology Corporation (688256.SS) Raising China AI GPU TAM"
  },
  {
    "figure_id": "F731",
    "report_id": "R041",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Cambricon: One-year forward P/S trend ## Risk Reward – Cambricon Technology Corporation (688256.SS) Raising China AI GPU TAM ## PRICE TARGET Rmb1,528.00"
  },
  {
    "figure_id": "F732",
    "report_id": "R041",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Iluvatar: Residual income model Exhibit 17: Iluvatar: One-year forward P/S trend - - - - Iluvatar one-year forward P/S ## Risk Reward – Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK) Leveraging supply chain resilienc"
  },
  {
    "figure_id": "F733",
    "report_id": "R043",
    "label": "Exhibit 37",
    "context": "Exhibit 1: MS-Estimated Cobenfy TRx trajectory to achieve 2025/2026 consensus estimates vs. schizophrenia launch analogs Exhibit 2: Cobenfy Launch vs. Recent antipsychotic launches (all indications) Exhibit 3: MS-Estimated Jour"
  },
  {
    "figure_id": "F734",
    "report_id": "R043",
    "label": "Exhibit 1",
    "context": "Exhibit 4: GILD's Yeztugo and Descovy vs. GSK's Apretude TRx launch comparison"
  },
  {
    "figure_id": "F735",
    "report_id": "R043",
    "label": "Exhibit 2",
    "context": "Exhibit 5: MS-Estimated Yeztugo TRx trajectory based on 1Q \\$/script to achieve 2Q26 cons estimate of \\$225mn"
  },
  {
    "figure_id": "F736",
    "report_id": "R043",
    "label": "Exhibit 3",
    "context": "Exhibit 6: MS-estimated Ico TRx trajectory to achieve 2026 consensus vs. prior I&I launches"
  },
  {
    "figure_id": "F737",
    "report_id": "R043",
    "label": "Exhibit 4",
    "context": "Exhibit 7: Tremfya and Skyrizi NRx trend"
  },
  {
    "figure_id": "F738",
    "report_id": "R043",
    "label": "Exhibit 5",
    "context": "Exhibit 5: MS-Estimated Yeztugo TRx trajectory based on 1Q \\$/script to achieve 2Q26 cons estimate of \\$225mn Exhibit 6: MS-estimated Ico TRx trajectory to achieve 2026 consensus vs. prior I&I launches Exhibit 7: Tremfya and Sk"
  },
  {
    "figure_id": "F739",
    "report_id": "R043",
    "label": "Exhibit 6",
    "context": "Exhibit 6: MS-estimated Ico TRx trajectory to achieve 2026 consensus vs. prior I&I launches Exhibit 7: Tremfya and Skyrizi NRx trend ## Momentum of top outpatient drugs: Exhibit 8: Key products TRx YOY % for US Major Pharma and"
  },
  {
    "figure_id": "F740",
    "report_id": "R043",
    "label": "Exhibit10",
    "context": "Exhibit10: Total Market weekly YOY TRx growth Note: TRx= Total Prescription. See definition above. Exhibit 11: Total market absolute TRx and NRx Note: NRx= New Prescription. See definition above."
  },
  {
    "figure_id": "F741",
    "report_id": "R043",
    "label": "Exhibit10",
    "context": "Exhibit 12: Total market weekly NRX and EUNRx YOY growth since January 2020"
  },
  {
    "figure_id": "F742",
    "report_id": "R043",
    "label": "Exhibit 11",
    "context": "Exhibit 12: Total market weekly NRX and EUNRx YOY growth since January 2020 Exhibit 13: Total market weekly TRx and EUTRx YOY growth since January 2020 Exhibit14: U.S. market\\* including brands and generics monthly gross sales g"
  },
  {
    "figure_id": "F743",
    "report_id": "R043",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Total market weekly NRX and EUNRx YOY growth since January 2020 Exhibit 13: Total market weekly TRx and EUTRx YOY growth since January 2020 Exhibit14: U.S. market\\* including brands and generics monthly gross sales g"
  },
  {
    "figure_id": "F744",
    "report_id": "R043",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Total market weekly TRx and EUTRx YOY growth since January 2020 Exhibit14: U.S. market\\* including brands and generics monthly gross sales growth Exhibit15: Total market Branded\\* pharmaceutical monthly YOY volume vs"
  },
  {
    "figure_id": "F745",
    "report_id": "R043",
    "label": "Exhibit14",
    "context": "Exhibit14: U.S. market\\* including brands and generics monthly gross sales growth Exhibit15: Total market Branded\\* pharmaceutical monthly YOY volume vs. sales dollar growth Exhibit 16: Total market Generic pharmaceutical month"
  },
  {
    "figure_id": "F746",
    "report_id": "R043",
    "label": "Exhibit15",
    "context": "Exhibit17: Key products from U.S. Major Pharma"
  },
  {
    "figure_id": "F747",
    "report_id": "R043",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Biosimilar Actemra 52-week TRx share ## Avastin AMGN's Mvasi launched in Jul-19. PFE's Zirabev was launched on December 31, 2019. AMRX's Alymsys was launched on October 3, 2022. Exhibit 22: Biosimilar Avastin monthly s"
  },
  {
    "figure_id": "F748",
    "report_id": "R043",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Biosimilar Avastin monthly sales share Epogen Exhibit 23: Biosimilar Epogen monthly sales share"
  },
  {
    "figure_id": "F749",
    "report_id": "R043",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Biosimilar Avastin monthly sales share Epogen Exhibit 23: Biosimilar Epogen monthly sales share Exhibit 24: Biosimilar Epogen 52-week TRx share. Epogen is administered as an IV as well as Sub-Q ## Herceptin"
  },
  {
    "figure_id": "F750",
    "report_id": "R043",
    "label": "Exhibit 23",
    "context": "Exhibit 25: Biosimilar Herceptin monthly sales share"
  },
  {
    "figure_id": "F751",
    "report_id": "R043",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Biosimilar Herceptin monthly sales share ## Humalog See Exhibit65 for weekly TRx share chart. Exhibit 26: Biosimilar Humalog monthly sales share. We include Humalog A.G. (Insulin Lispro) in Humalog franchise"
  },
  {
    "figure_id": "F752",
    "report_id": "R043",
    "label": "Exhibit65",
    "context": "Exhibit 27: Biosimilar Humira 52-week TRx share"
  },
  {
    "figure_id": "F753",
    "report_id": "R043",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Biosimilar Humira 52-week TRx share ## Lantus See Exhibit67 to Exhibit71 for weekly charts on biosimilar Lantus. Exhibit 28: Biosimilar Lantus monthly sales share"
  },
  {
    "figure_id": "F754",
    "report_id": "R043",
    "label": "Exhibit67",
    "context": "Exhibit 29: Biosimilar Lucentis monthly sales share"
  },
  {
    "figure_id": "F755",
    "report_id": "R043",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Biosimilar Lucentis monthly sales share ## Neulasta Neulasta biosimilar Biocon's Fulphila market share (monthly sales) has flattened after January inflection, but there may be a reporting restriction in place. Biocon's"
  },
  {
    "figure_id": "F756",
    "report_id": "R043",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Biosimilar Neulasta monthly sales share Exhibit 31: Biosimilar Neulasta 52-week TRx share. Neulasta is Sub-Q ## Neupogen"
  },
  {
    "figure_id": "F757",
    "report_id": "R043",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Biosimilar Neulasta monthly sales share Exhibit 31: Biosimilar Neulasta 52-week TRx share. Neulasta is Sub-Q ## Neupogen Exhibit 32: Biosimilar Neupogen monthly sales share"
  },
  {
    "figure_id": "F758",
    "report_id": "R043",
    "label": "Exhibit 31",
    "context": "Exhibit 34: Biosimilar Prolia 52-week TRx share"
  },
  {
    "figure_id": "F759",
    "report_id": "R043",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Biosimilar Neupogen monthly sales share Exhibit 33: Biosimilar Neupogen 52-week TRx share. Neupogen is administered as an IV as well as Sub-Q ## Prolia Exhibit 34: Biosimilar Prolia 52-week TRx share Note: Bomyntra"
  },
  {
    "figure_id": "F760",
    "report_id": "R043",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Biosimilar Neupogen 52-week TRx share. Neupogen is administered as an IV as well as Sub-Q ## Prolia Exhibit 34: Biosimilar Prolia 52-week TRx share Note: Bomyntra appears in IQVIA but TRx are sporadic ## Remicade Exh"
  },
  {
    "figure_id": "F761",
    "report_id": "R043",
    "label": "Exhibit 35",
    "context": "Exhibit 36: Biosimilar Rituxan monthly sales share"
  },
  {
    "figure_id": "F762",
    "report_id": "R043",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Biosimilar Rituxan monthly sales share ## Stelara Exhibit 37: Biosimilar Stelara 52-week TRx share."
  },
  {
    "figure_id": "F763",
    "report_id": "R043",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Biosimilar Rituxan monthly sales share ## Stelara Exhibit 37: Biosimilar Stelara 52-week TRx share. Exhibit 38: Biosimilar Stelara monthly sales share ## Cardiovascular"
  },
  {
    "figure_id": "F764",
    "report_id": "R043",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Biosimilar Stelara 52-week TRx share. Exhibit 38: Biosimilar Stelara monthly sales share ## Cardiovascular ## Anti-Coagulants Exhibit39: Anti-coagulants TRx market share"
  },
  {
    "figure_id": "F765",
    "report_id": "R043",
    "label": "Exhibit39",
    "context": "Exhibit39: Anti-coagulants TRx market share Exhibit40: Anti-Coagulants TRx YOY Exhibit41: Novel oral anti-coagulants launch comparison FDA approved Xarelto for deep vein thrombosis in July 2011; launch trends above capture Xa"
  },
  {
    "figure_id": "F766",
    "report_id": "R043",
    "label": "Exhibit39",
    "context": "Exhibit39: Anti-coagulants TRx market share Exhibit40: Anti-Coagulants TRx YOY Exhibit41: Novel oral anti-coagulants launch comparison FDA approved Xarelto for deep vein thrombosis in July 2011; launch trends above capture Xa"
  },
  {
    "figure_id": "F767",
    "report_id": "R043",
    "label": "Exhibit39",
    "context": "Exhibit 42: Lipid lowering absolute TRx: Amarin's Vascepa, Sanofi's Praluent, AMGN's Repatha. Vascepa is EPA indicated for high triglycerides. Praluent and Repatha are PCSK9s indicated for high LDL. Nexletol is ACLi indicated for hi"
  },
  {
    "figure_id": "F768",
    "report_id": "R043",
    "label": "Exhibit41",
    "context": "Exhibit 44: TRx YOY growth"
  },
  {
    "figure_id": "F769",
    "report_id": "R043",
    "label": "Exhibit 42",
    "context": "Exhibit 44: TRx YOY growth ## Other Heart Diseases"
  },
  {
    "figure_id": "F770",
    "report_id": "R043",
    "label": "Exhibit 43",
    "context": "Exhibit 44: TRx YOY growth ## Other Heart Diseases Exhibit 45: Vyndaqel TRx launch trend"
  },
  {
    "figure_id": "F771",
    "report_id": "R043",
    "label": "Exhibit 44",
    "context": "Exhibit 44: TRx YOY growth ## Other Heart Diseases Exhibit 45: Vyndaqel TRx launch trend Exhibit 46: Vyndaqel franchise absolute TRx and YOY ## Diabetes"
  },
  {
    "figure_id": "F772",
    "report_id": "R043",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Vyndaqel TRx launch trend Exhibit 46: Vyndaqel franchise absolute TRx and YOY ## Diabetes ## DPP-4, SGLT-2 and GLP-1 Diabetes trends. The drugs can be used in combination so share gain/loss does not necessarily mean"
  },
  {
    "figure_id": "F773",
    "report_id": "R043",
    "label": "Exhibit 47",
    "context": "Exhibit 47: TRx share by class Exhibit48: DPP-4, SGLT-2 and GLP-1 TRx as % of total DPP-4 + SGLT-2 + GLP-1 TRxs. The drugs can be used in combination with each other so \"share loss\" does not necessarily mean switching. ## DPP-4"
  },
  {
    "figure_id": "F774",
    "report_id": "R043",
    "label": "Exhibit 47",
    "context": "Exhibit49: DPP-4 and SGLT-2 TRx as % of total DPP-4 + SGLT-2 TRxs. The drugs can be used in combination with each other so \"share loss\" does not necessarily mean switching."
  },
  {
    "figure_id": "F775",
    "report_id": "R043",
    "label": "Exhibit48",
    "context": "Exhibit50: Individual DPP-4 and SGLT-2 TRx as % of total DPP-4 + SGLT-2 TRxs ## DPP-4 only"
  },
  {
    "figure_id": "F776",
    "report_id": "R043",
    "label": "Exhibit49",
    "context": "Exhibit51: DPP-4 TRx market share"
  },
  {
    "figure_id": "F777",
    "report_id": "R043",
    "label": "Exhibit50",
    "context": "Exhibit50: Individual DPP-4 and SGLT-2 TRx as % of total DPP-4 + SGLT-2 TRxs ## DPP-4 only Exhibit51: DPP-4 TRx market share Exhibit52: DPP-4s TRx YOY Exhibit53: DPP-4s launch comparison"
  },
  {
    "figure_id": "F778",
    "report_id": "R043",
    "label": "Exhibit51",
    "context": "Exhibit51: DPP-4 TRx market share Exhibit52: DPP-4s TRx YOY Exhibit53: DPP-4s launch comparison Onglyza launched in week of 8/14/09, Tradjenta launched in week of 5/20/11, Nesina launched in week of 6/14/13 ## SGLT-2 only"
  },
  {
    "figure_id": "F779",
    "report_id": "R043",
    "label": "Exhibit52",
    "context": "Exhibit52: DPP-4s TRx YOY Exhibit53: DPP-4s launch comparison Onglyza launched in week of 8/14/09, Tradjenta launched in week of 5/20/11, Nesina launched in week of 6/14/13 ## SGLT-2 only Exhibit54: SGLT-2 TRx market share Fa"
  },
  {
    "figure_id": "F780",
    "report_id": "R043",
    "label": "Exhibit53",
    "context": "Exhibit55: SGLT-2s TRx YOY Exhibit56: SGLT-2s launch comparison"
  },
  {
    "figure_id": "F781",
    "report_id": "R043",
    "label": "Exhibit54",
    "context": "Exhibit55: SGLT-2s TRx YOY Exhibit56: SGLT-2s launch comparison Invokana launched in week of 4/12/13, Farxiga launched in week of 1/24/14, Jardiance launched in week 8/29/14, Steglatro launched in week of 2/2/18. ## GLP-1"
  },
  {
    "figure_id": "F782",
    "report_id": "R043",
    "label": "Exhibit55",
    "context": "Exhibit55: SGLT-2s TRx YOY Exhibit56: SGLT-2s launch comparison Invokana launched in week of 4/12/13, Farxiga launched in week of 1/24/14, Jardiance launched in week 8/29/14, Steglatro launched in week of 2/2/18. ## GLP-1 Exhib"
  },
  {
    "figure_id": "F783",
    "report_id": "R043",
    "label": "Exhibit56",
    "context": "Exhibit59: GLP-1 TRx market share"
  },
  {
    "figure_id": "F784",
    "report_id": "R043",
    "label": "Exhibit 57",
    "context": "Exhibit 57: GLP-1 TRx launches Exhibit 58: LLY's Mounjaro & Zepbpound launch vs. recent GLP-1 launches, Ozempic and Wegovy Exhibit59: GLP-1 TRx market share Exhibit 60: GLP-1 NRx market share"
  },
  {
    "figure_id": "F785",
    "report_id": "R043",
    "label": "Exhibit 58",
    "context": "Exhibit 58: LLY's Mounjaro & Zepbpound launch vs. recent GLP-1 launches, Ozempic and Wegovy Exhibit59: GLP-1 TRx market share Exhibit 60: GLP-1 NRx market share Exhibit61: GLP-1s TRx YOY"
  },
  {
    "figure_id": "F786",
    "report_id": "R043",
    "label": "Exhibit59",
    "context": "Exhibit59: GLP-1 TRx market share Exhibit 60: GLP-1 NRx market share Exhibit61: GLP-1s TRx YOY Exhibit 62: Trulicity 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F787",
    "report_id": "R043",
    "label": "Exhibit 60",
    "context": "Exhibit 60: GLP-1 NRx market share Exhibit61: GLP-1s TRx YOY Exhibit 62: Trulicity 52-week absolute TRx and YOY performance Exhibit 63: LLY GLP-1 franchise 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F788",
    "report_id": "R043",
    "label": "Exhibit61",
    "context": "Exhibit61: GLP-1s TRx YOY Exhibit 62: Trulicity 52-week absolute TRx and YOY performance Exhibit 63: LLY GLP-1 franchise 52-week absolute TRx and YOY performance Exhibit 64: Novo GLP-1 franchise 52-week absolute TRx and YOY p"
  },
  {
    "figure_id": "F789",
    "report_id": "R043",
    "label": "Exhibit 62",
    "context": "Exhibit 62: Trulicity 52-week absolute TRx and YOY performance Exhibit 63: LLY GLP-1 franchise 52-week absolute TRx and YOY performance Exhibit 64: Novo GLP-1 franchise 52-week absolute TRx and YOY performance ## Insulin ## Sh"
  },
  {
    "figure_id": "F790",
    "report_id": "R043",
    "label": "Exhibit 62",
    "context": "Exhibit65: LLY insulin franchise (Humalog+Humulin) vs. Novo insulin franchise (Novolog+Novolin) TRx market share. Sanofi's Admelog (generic Humalog) launched in March 2018. We await MYL/Biocon's Semglee."
  },
  {
    "figure_id": "F791",
    "report_id": "R043",
    "label": "Exhibit65",
    "context": "Exhibit65: LLY insulin franchise (Humalog+Humulin) vs. Novo insulin franchise (Novolog+Novolin) TRx market share. Sanofi's Admelog (generic Humalog) launched in March 2018. We await MYL/Biocon's Semglee. Exhibit66: LLY insulin fr"
  },
  {
    "figure_id": "F792",
    "report_id": "R043",
    "label": "Exhibit65",
    "context": "Exhibit67: Long-acting insulin market share. Branded insulin glargine is Lantus/Solostar and Toujeo; Basaglar and Semglee are biosimilar insulin glargine."
  },
  {
    "figure_id": "F793",
    "report_id": "R043",
    "label": "Exhibit66",
    "context": "Exhibit68: Long-acting insulin TRx YOY Exhibit 69: Lantus+Lantus Solostar vs Basaglar TRx share"
  },
  {
    "figure_id": "F794",
    "report_id": "R043",
    "label": "Exhibit67",
    "context": "Exhibit 70: Insulin glargine branded (Lantus, Solostar, Toujeo) vs. biosimilar (Basaglar) TRx share; Lantus, Solostar, and Basaglar are 100 units/mL while Toujeo is 300 units/mL."
  },
  {
    "figure_id": "F795",
    "report_id": "R043",
    "label": "Exhibit68",
    "context": "Exhibit71: Recent long-acting insulin launches: Basaglar vs. Tresiba vs. Toujeo vs. Soliqua vs. Xultophy vs. Semglee"
  },
  {
    "figure_id": "F796",
    "report_id": "R043",
    "label": "Exhibit 69",
    "context": "Exhibit71: Recent long-acting insulin launches: Basaglar vs. Tresiba vs. Toujeo vs. Soliqua vs. Xultophy vs. Semglee ## SFU"
  },
  {
    "figure_id": "F797",
    "report_id": "R043",
    "label": "Exhibit 70",
    "context": "Exhibit 72: Total SFU 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F798",
    "report_id": "R043",
    "label": "Exhibit71",
    "context": "Exhibit71: Recent long-acting insulin launches: Basaglar vs. Tresiba vs. Toujeo vs. Soliqua vs. Xultophy vs. Semglee ## SFU Exhibit 72: Total SFU 52-week absolute TRx and YOY performance Exhibit 73: Drugs approved for IgAN ##"
  },
  {
    "figure_id": "F799",
    "report_id": "R043",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Total SFU 52-week absolute TRx and YOY performance Exhibit 73: Drugs approved for IgAN ## Immunology Exhibit 74: Autoimmune drugs with their MOA and approved indications"
  },
  {
    "figure_id": "F800",
    "report_id": "R043",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Stelara \\$/TRx vs. TRx Exhibit 77: Tremfya \\$/TRx vs. TRx Exhibit 78: Cosentyx \\$/TRx vs. TRx"
  },
  {
    "figure_id": "F801",
    "report_id": "R043",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Stelara \\$/TRx vs. TRx Exhibit 77: Tremfya \\$/TRx vs. TRx Exhibit 78: Cosentyx \\$/TRx vs. TRx Exhibit 79: Dupixent \\$/TRx vs. TRx"
  },
  {
    "figure_id": "F802",
    "report_id": "R043",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Tremfya \\$/TRx vs. TRx Exhibit 78: Cosentyx \\$/TRx vs. TRx Exhibit 79: Dupixent \\$/TRx vs. TRx Exhibit 80: Rinvoq \\$/TRx vs. TRx"
  },
  {
    "figure_id": "F803",
    "report_id": "R043",
    "label": "Exhibit 78",
    "context": "Exhibit 78: Cosentyx \\$/TRx vs. TRx Exhibit 79: Dupixent \\$/TRx vs. TRx Exhibit 80: Rinvoq \\$/TRx vs. TRx Exhibit 81: Skyrizi \\$/TRx vs. TRx"
  },
  {
    "figure_id": "F804",
    "report_id": "R043",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Dupixent \\$/TRx vs. TRx Exhibit 80: Rinvoq \\$/TRx vs. TRx Exhibit 81: Skyrizi \\$/TRx vs. TRx ## Anti-TNF"
  },
  {
    "figure_id": "F805",
    "report_id": "R043",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Rinvoq \\$/TRx vs. TRx Exhibit 81: Skyrizi \\$/TRx vs. TRx ## Anti-TNF"
  },
  {
    "figure_id": "F806",
    "report_id": "R043",
    "label": "Exhibit 81",
    "context": "Exhibit 81: Skyrizi \\$/TRx vs. TRx ## Anti-TNF IL-13"
  },
  {
    "figure_id": "F807",
    "report_id": "R043",
    "label": "Exhibit82",
    "context": "Exhibit 84: IL-13 launches: Adbry (Leo), Ebglyss (LLY) and IL-4 Dupixent (SNY/REGN)"
  },
  {
    "figure_id": "F808",
    "report_id": "R043",
    "label": "Exhibit 83",
    "context": "Exhibit 84: IL-13 launches: Adbry (Leo), Ebglyss (LLY) and IL-4 Dupixent (SNY/REGN) Exhibit 85: IL-13 weekly TRx market share IL-17 and IL-23"
  },
  {
    "figure_id": "F809",
    "report_id": "R043",
    "label": "Exhibit 84",
    "context": "Exhibit 84: IL-13 launches: Adbry (Leo), Ebglyss (LLY) and IL-4 Dupixent (SNY/REGN) Exhibit 85: IL-13 weekly TRx market share IL-17 and IL-23 Exhibit 86: IL-17A and IL-23 combined weekly TRx market share: Cosentyx (NVS), Siliq ("
  },
  {
    "figure_id": "F810",
    "report_id": "R043",
    "label": "Exhibit 85",
    "context": "Exhibit 87: IL-17A weekly TRx market share: Cosentyx (NVS), Siliq (VRX), and Taltz (LLY)"
  },
  {
    "figure_id": "F811",
    "report_id": "R043",
    "label": "Exhibit 86",
    "context": "Exhibit 88: Taltz 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F812",
    "report_id": "R043",
    "label": "Exhibit 88",
    "context": "Exhibit 88: Taltz 52-week absolute TRx and YOY performance Exhibit 89: Cosentyx 52-week absolute TRx and YOY performance Exhibit90: IL-17A launches: Cosentyx (NVS), Siliq (Bausch/Ortho Dermatologics), and Taltz (LLY)"
  },
  {
    "figure_id": "F813",
    "report_id": "R043",
    "label": "Exhibit 88",
    "context": "Exhibit 88: Taltz 52-week absolute TRx and YOY performance Exhibit 89: Cosentyx 52-week absolute TRx and YOY performance Exhibit90: IL-17A launches: Cosentyx (NVS), Siliq (Bausch/Ortho Dermatologics), and Taltz (LLY) ## IL-23"
  },
  {
    "figure_id": "F814",
    "report_id": "R043",
    "label": "Exhibit 88",
    "context": "Exhibit 91: IL-23 launches: Tremfya, Skyrizi, Ilumya and Omvoh (we do not have Stelara launch data)"
  },
  {
    "figure_id": "F815",
    "report_id": "R043",
    "label": "Exhibit 91",
    "context": "Exhibit 92: IL-23 weekly TRx market share Tremfya and Skyrizi scripts are restricted and unreliable."
  },
  {
    "figure_id": "F816",
    "report_id": "R043",
    "label": "Exhibit 91",
    "context": "Exhibit 92: IL-23 weekly TRx market share Tremfya and Skyrizi scripts are restricted and unreliable. Exhibit 93: Skyrizi (ABBV) 52-week absolute TRx and YOY performance Exhibit 94: Tremfya (JNJ) 52-week absolute TRx and YOY perf"
  },
  {
    "figure_id": "F817",
    "report_id": "R043",
    "label": "Exhibit 92",
    "context": "Exhibit 95: Stelara (JNJ) 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F818",
    "report_id": "R043",
    "label": "Exhibit 93",
    "context": "Exhibit 93: Skyrizi (ABBV) 52-week absolute TRx and YOY performance Exhibit 94: Tremfya (JNJ) 52-week absolute TRx and YOY performance Exhibit 95: Stelara (JNJ) 52-week absolute TRx and YOY performance ## JAK inhibitor"
  },
  {
    "figure_id": "F819",
    "report_id": "R043",
    "label": "Exhibit 94",
    "context": "Exhibit 94: Tremfya (JNJ) 52-week absolute TRx and YOY performance Exhibit 95: Stelara (JNJ) 52-week absolute TRx and YOY performance ## JAK inhibitor Exhibit96: JAK inhibitor launches. Supplier restrictions were removed for Rin"
  },
  {
    "figure_id": "F820",
    "report_id": "R043",
    "label": "Exhibit 95",
    "context": "Exhibit 97: JAK inhibitor TRx market share Exhibit 98: JAK inhibitor 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F821",
    "report_id": "R043",
    "label": "Exhibit96",
    "context": "Exhibit 97: JAK inhibitor TRx market share Exhibit 98: JAK inhibitor 52-week absolute TRx and YOY performance Exhibit99: Xeljanz + XR (PFE) 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F822",
    "report_id": "R043",
    "label": "Exhibit 97",
    "context": "Exhibit 97: JAK inhibitor TRx market share Exhibit 98: JAK inhibitor 52-week absolute TRx and YOY performance Exhibit99: Xeljanz + XR (PFE) 52-week absolute TRx and YOY performance Exhibit 100: Rinvoq (ABBV) 52-week absolute T"
  },
  {
    "figure_id": "F823",
    "report_id": "R043",
    "label": "Exhibit 98",
    "context": "Exhibit 98: JAK inhibitor 52-week absolute TRx and YOY performance Exhibit99: Xeljanz + XR (PFE) 52-week absolute TRx and YOY performance Exhibit 100: Rinvoq (ABBV) 52-week absolute TRx and YOY performance. Rinvoq scripts benefi"
  },
  {
    "figure_id": "F824",
    "report_id": "R043",
    "label": "Exhibit99",
    "context": "Exhibit 101: Galderma's Nemluvio launch trend"
  },
  {
    "figure_id": "F825",
    "report_id": "R043",
    "label": "Exhibit 100",
    "context": "Exhibit 100: Rinvoq (ABBV) 52-week absolute TRx and YOY performance. Rinvoq scripts benefited from removal of reporting restrictions starting Feb 2023 ## IL-31 Exhibit 101: Galderma's Nemluvio launch trend ## TYK2 Exhibit 102: BM"
  },
  {
    "figure_id": "F826",
    "report_id": "R043",
    "label": "Exhibit 101",
    "context": "Exhibit 104: AMGN's Otezla vs BMY's Sotyktu vs JNJ's Icotyde TRx since launch"
  },
  {
    "figure_id": "F827",
    "report_id": "R043",
    "label": "Exhibit 102",
    "context": "Exhibit 105: Otezla 52-week TRx absolute and YOY performance"
  },
  {
    "figure_id": "F828",
    "report_id": "R043",
    "label": "Exhibit 103",
    "context": "Exhibit 103: Sotyktu vs other recent Plaque Psoriasis approved only launches. See Exhibit 74 for approved indications Exhibit 104: AMGN's Otezla vs BMY's Sotyktu vs JNJ's Icotyde TRx since launch Exhibit 105: Otezla 52-week TRx a"
  },
  {
    "figure_id": "F829",
    "report_id": "R043",
    "label": "Exhibit 104",
    "context": "Exhibit 104: AMGN's Otezla vs BMY's Sotyktu vs JNJ's Icotyde TRx since launch Exhibit 105: Otezla 52-week TRx absolute and YOY performance ## Atopic dermatitis Exhibit 106: Atopic dermatitis launches: Dupixent (SNY/REGN), Eucrisa"
  },
  {
    "figure_id": "F830",
    "report_id": "R043",
    "label": "Exhibit 106",
    "context": "Exhibit 107: Atopic dermatitis launches: Dupixent (SNY/REGN) and Eucrisa (PFE). TRxs may not be directly comparable because Eucrisa (PDE4) is an ointment that comes in 60g and 100g tubes, and is applied in a thin layer twice daily to"
  },
  {
    "figure_id": "F831",
    "report_id": "R043",
    "label": "Exhibit 106",
    "context": "Exhibit 108: Dupixent 52-week absolute and YOY TRx ## Other Topicals"
  },
  {
    "figure_id": "F832",
    "report_id": "R043",
    "label": "Exhibit 107",
    "context": "Exhibit 108: Dupixent 52-week absolute and YOY TRx ## Other Topicals Exhibit 109: Weekly TRx for Vtama, Opzelura and Zoryve (please refer Exhibit 74 above for indications approved) Exhibit 110: Weekly NRx for Vtama, Opzelura and"
  },
  {
    "figure_id": "F833",
    "report_id": "R043",
    "label": "Exhibit 108",
    "context": "Exhibit 108: Dupixent 52-week absolute and YOY TRx ## Other Topicals Exhibit 109: Weekly TRx for Vtama, Opzelura and Zoryve (please refer Exhibit 74 above for indications approved) Exhibit 110: Weekly NRx for Vtama, Opzelura and"
  },
  {
    "figure_id": "F834",
    "report_id": "R043",
    "label": "Exhibit 109",
    "context": "Exhibit 109: Weekly TRx for Vtama, Opzelura and Zoryve (please refer Exhibit 74 above for indications approved) Exhibit 110: Weekly NRx for Vtama, Opzelura and Zoryve ## Infectious disease HCV Exhibit 111: HCV TRx market share"
  },
  {
    "figure_id": "F835",
    "report_id": "R043",
    "label": "Exhibit 110",
    "context": "Exhibit 110: Weekly NRx for Vtama, Opzelura and Zoryve ## Infectious disease HCV Exhibit 111: HCV TRx market share ## HIV Exhibit112: Integrase inhibitor TRx market share"
  },
  {
    "figure_id": "F836",
    "report_id": "R043",
    "label": "Exhibit 111",
    "context": "Exhibit 111: HCV TRx market share ## HIV Exhibit112: Integrase inhibitor TRx market share Exhibit 113: GILD's Biktarvy vs ViiV's Dovato, Cabenuva TRx launch trends Exhibit 114: Biktarvy weekly TRx and YOY growth"
  },
  {
    "figure_id": "F837",
    "report_id": "R043",
    "label": "Exhibit112",
    "context": "Exhibit112: Integrase inhibitor TRx market share Exhibit 113: GILD's Biktarvy vs ViiV's Dovato, Cabenuva TRx launch trends Exhibit 114: Biktarvy weekly TRx and YOY growth Exhibit 115: Truvada vs Descovy vs Apretude TRx share."
  },
  {
    "figure_id": "F838",
    "report_id": "R043",
    "label": "Exhibit 113",
    "context": "Exhibit 116: GILD's Descovy and Yeztugo vs GSK's Apretude TRx launch comparison"
  },
  {
    "figure_id": "F839",
    "report_id": "R043",
    "label": "Exhibit 114",
    "context": "Exhibit 116: GILD's Descovy and Yeztugo vs GSK's Apretude TRx launch comparison Exhibit 117: GILD's Descovy and Yeztugo vs GSK's Apretude TRx launch comparison. We are unable to separate the prescriptions by indication and the data"
  },
  {
    "figure_id": "F840",
    "report_id": "R043",
    "label": "Exhibit 115",
    "context": "Exhibit 116: GILD's Descovy and Yeztugo vs GSK's Apretude TRx launch comparison Exhibit 117: GILD's Descovy and Yeztugo vs GSK's Apretude TRx launch comparison. We are unable to separate the prescriptions by indication and the data"
  },
  {
    "figure_id": "F841",
    "report_id": "R043",
    "label": "Exhibit 116",
    "context": "Exhibit 118: Paxlovid vs Molnupiravir TRx trends"
  },
  {
    "figure_id": "F842",
    "report_id": "R043",
    "label": "Exhibit 117",
    "context": "Exhibit 119: Migraine drugs with their MOA and approved indications"
  },
  {
    "figure_id": "F843",
    "report_id": "R043",
    "label": "Exhibit 127",
    "context": "One TRx for one drug may represent different numbers of months of therapy and/or doses. For example, assuming simplistically that one TRx represents one course of treatment, one Aimovig TRx represents one month of drug, one Ajovy TRx could represent one or thr"
  },
  {
    "figure_id": "F844",
    "report_id": "R043",
    "label": "Exhibit 120",
    "context": "Exhibit 123: Oral CGRP weekly TRx share % of total oral CGRP"
  },
  {
    "figure_id": "F845",
    "report_id": "R043",
    "label": "Exhibit 121",
    "context": "Exhibit 123: Oral CGRP weekly TRx share % of total oral CGRP Exhibit 124: Migraine weekly TRx. \\*Total CGRP includes Aimovig, Ajovy, Emgality, Ubrelvy, Qulipta, Nurtec and Vyepti. Vyepti is an IV, hence TRx is not captured by IQVIA"
  },
  {
    "figure_id": "F846",
    "report_id": "R043",
    "label": "Exhibit 122",
    "context": "Exhibit 123: Oral CGRP weekly TRx share % of total oral CGRP Exhibit 124: Migraine weekly TRx. \\*Total CGRP includes Aimovig, Ajovy, Emgality, Ubrelvy, Qulipta, Nurtec and Vyepti. Vyepti is an IV, hence TRx is not captured by IQVIA"
  },
  {
    "figure_id": "F847",
    "report_id": "R043",
    "label": "Exhibit 123",
    "context": "Exhibit 126: Oral CGRP weekly TRx YOY"
  },
  {
    "figure_id": "F848",
    "report_id": "R043",
    "label": "Exhibit 124",
    "context": "Exhibit 124: Migraine weekly TRx. \\*Total CGRP includes Aimovig, Ajovy, Emgality, Ubrelvy, Qulipta, Nurtec and Vyepti. Vyepti is an IV, hence TRx is not captured by IQVIA completely Exhibit 126: Oral CGRP weekly TRx YOY"
  },
  {
    "figure_id": "F849",
    "report_id": "R043",
    "label": "Exhibit 125",
    "context": "Exhibit 126: Oral CGRP weekly TRx YOY"
  },
  {
    "figure_id": "F850",
    "report_id": "R043",
    "label": "Exhibit 126",
    "context": "Exhibit 126: Oral CGRP weekly TRx YOY Another helpful metric to compare may be number of injections. We estimate the number of injections prescribed as another means of comparison. For Aimovig and Emgality we assume no. of inje"
  },
  {
    "figure_id": "F851",
    "report_id": "R043",
    "label": "Exhibit 127",
    "context": "Exhibit 129: CGRP weekly no. of injections since launch. Vyepti is an IV, hence EUTRx/TRx is not captured by IQVIA completely"
  },
  {
    "figure_id": "F852",
    "report_id": "R043",
    "label": "Exhibit 128",
    "context": "Exhibit 129: CGRP weekly no. of injections since launch. Vyepti is an IV, hence EUTRx/TRx is not captured by IQVIA completely Exhibit 130: CGRP drugs IQVIA monthly sales trend ## Multiple sclerosis"
  },
  {
    "figure_id": "F853",
    "report_id": "R043",
    "label": "Exhibit 129",
    "context": "Exhibit 129: CGRP weekly no. of injections since launch. Vyepti is an IV, hence EUTRx/TRx is not captured by IQVIA completely Exhibit 130: CGRP drugs IQVIA monthly sales trend ## Multiple sclerosis Exhibit131: Oral multiple scler"
  },
  {
    "figure_id": "F854",
    "report_id": "R043",
    "label": "Exhibit 130",
    "context": "Exhibit 132: S1P1 TRx market share: NVS' Gilenya and Mayzent and BMY's Zeposia. Zeposia was approved for Ulcerative Colitis on 5/28/21"
  },
  {
    "figure_id": "F855",
    "report_id": "R043",
    "label": "Exhibit131",
    "context": "Exhibit 132: S1P1 TRx market share: NVS' Gilenya and Mayzent and BMY's Zeposia. Zeposia was approved for Ulcerative Colitis on 5/28/21 Exhibit 133: Vumerity conversion TRx share"
  },
  {
    "figure_id": "F856",
    "report_id": "R043",
    "label": "Exhibit 132",
    "context": "Exhibit 132: S1P1 TRx market share: NVS' Gilenya and Mayzent and BMY's Zeposia. Zeposia was approved for Ulcerative Colitis on 5/28/21 Exhibit 133: Vumerity conversion TRx share ## Antidepressants"
  },
  {
    "figure_id": "F857",
    "report_id": "R043",
    "label": "Exhibit 133",
    "context": "Exhibit 133: Vumerity conversion TRx share ## Antidepressants Exhibit 135: Antidepressant TRx for MDD"
  },
  {
    "figure_id": "F858",
    "report_id": "R043",
    "label": "Exhibit 134",
    "context": "Exhibit 135: Antidepressant TRx for MDD Exhibit 136: Auvelity 52-week absolute TRx and YOY performance ## Antipsychotic"
  },
  {
    "figure_id": "F859",
    "report_id": "R043",
    "label": "Exhibit 135",
    "context": "Exhibit 135: Antidepressant TRx for MDD Exhibit 136: Auvelity 52-week absolute TRx and YOY performance ## Antipsychotic Exhibit137: Vraylar and Lybalvi are approved for schizophrenia and bipolar disorder. At the time of launch, L"
  },
  {
    "figure_id": "F860",
    "report_id": "R043",
    "label": "Exhibit 136",
    "context": "Exhibit 138: Recent antipsychotic launches Exhibit 139: Antipsychotic TRx"
  },
  {
    "figure_id": "F861",
    "report_id": "R043",
    "label": "Exhibit137",
    "context": "Exhibit 138: Recent antipsychotic launches Exhibit 139: Antipsychotic TRx Exhibit 140: Vraylar 52-week absolute TRx and YOY performance"
  },
  {
    "figure_id": "F862",
    "report_id": "R043",
    "label": "Exhibit 138",
    "context": "Exhibit 138: Recent antipsychotic launches Exhibit 139: Antipsychotic TRx Exhibit 140: Vraylar 52-week absolute TRx and YOY performance ## Alzheimer's"
  },
  {
    "figure_id": "F863",
    "report_id": "R043",
    "label": "Exhibit 139",
    "context": "Exhibit 139: Antipsychotic TRx Exhibit 140: Vraylar 52-week absolute TRx and YOY performance ## Alzheimer's Exhibit 141: Leqembi and Kisunla IQVIA sales trend"
  },
  {
    "figure_id": "F864",
    "report_id": "R043",
    "label": "Exhibit 140",
    "context": "Exhibit 140: Vraylar 52-week absolute TRx and YOY performance ## Alzheimer's Exhibit 141: Leqembi and Kisunla IQVIA sales trend Exhibit 142: Leqembi vs Kisunla launch trend Exhibit 143: Leqembi and Kisunla IQVIA US sales compar"
  },
  {
    "figure_id": "F865",
    "report_id": "R043",
    "label": "Exhibit 141",
    "context": "Exhibit 141: Leqembi and Kisunla IQVIA sales trend Exhibit 142: Leqembi vs Kisunla launch trend Exhibit 143: Leqembi and Kisunla IQVIA US sales comparison Exhibit 144: Leqembi and Kisunla reported US sales comparison"
  },
  {
    "figure_id": "F866",
    "report_id": "R043",
    "label": "Exhibit 142",
    "context": "Exhibit 142: Leqembi vs Kisunla launch trend Exhibit 143: Leqembi and Kisunla IQVIA US sales comparison Exhibit 144: Leqembi and Kisunla reported US sales comparison Note: 2Q:23 to 4Q:23 Leqembi sales are reported WW sales. ##"
  },
  {
    "figure_id": "F867",
    "report_id": "R043",
    "label": "Exhibit 143",
    "context": "Exhibit 143: Leqembi and Kisunla IQVIA US sales comparison Exhibit 144: Leqembi and Kisunla reported US sales comparison Note: 2Q:23 to 4Q:23 Leqembi sales are reported WW sales. ## Obesity Exhibit 145: Obesity drug launches No"
  },
  {
    "figure_id": "F868",
    "report_id": "R043",
    "label": "Exhibit 144",
    "context": "Exhibit 144: Leqembi and Kisunla reported US sales comparison Note: 2Q:23 to 4Q:23 Leqembi sales are reported WW sales. ## Obesity Exhibit 145: Obesity drug launches Note: FDA requested the withdrawal of Belviq on Feb 13. 2020. E"
  },
  {
    "figure_id": "F869",
    "report_id": "R043",
    "label": "Exhibit 145",
    "context": "Exhibit 145: Obesity drug launches Note: FDA requested the withdrawal of Belviq on Feb 13. 2020. Exhibit 146: Zepbound and Wegovy launch vs Ozempic vs Rybelsus ## Ophthalmology Dry Eye Exhibit 147: Dry Eye TRx market share"
  },
  {
    "figure_id": "F870",
    "report_id": "R043",
    "label": "Exhibit 146",
    "context": "Exhibit 146: Zepbound and Wegovy launch vs Ozempic vs Rybelsus ## Ophthalmology Dry Eye Exhibit 147: Dry Eye TRx market share Exhibit 148: Dry Eye 52-week TRx trend ## Orphan Drugs"
  },
  {
    "figure_id": "F871",
    "report_id": "R043",
    "label": "Exhibit 147",
    "context": "Exhibit 147: Dry Eye TRx market share Exhibit 148: Dry Eye 52-week TRx trend ## Orphan Drugs Exhibit 149: ALNY's Onpattro and Amvuttra monthly sales trend. We normalize sales in March, June, September, and December to a 4-week ba"
  },
  {
    "figure_id": "F872",
    "report_id": "R043",
    "label": "Exhibit 148",
    "context": "Exhibit 150: ARGX's Vyvgart monthly sales trend. We normalize sales in March, June, September, and December to a 4-week basis to better compare with the other months"
  },
  {
    "figure_id": "F873",
    "report_id": "R043",
    "label": "Exhibit 149",
    "context": "Exhibit 151: AMGN's Uplizna monthly sales trend. We normalize sales in March, June, September, and December to a 4-week basis to better compare with the other months ## Pulmonary"
  },
  {
    "figure_id": "F874",
    "report_id": "R043",
    "label": "Exhibit 150",
    "context": "Exhibit152: Inhaled LABA-ICS combo TRx market share. Wixela is Mylan's generic Advair Exhibit153: Advair+Breo+Advair authorized generic weekly TRx YoY"
  },
  {
    "figure_id": "F875",
    "report_id": "R043",
    "label": "Exhibit 151",
    "context": "Exhibit153: Advair+Breo+Advair authorized generic weekly TRx YoY Exhibit 154: Advair brand vs generics weekly TRx market share"
  },
  {
    "figure_id": "F876",
    "report_id": "R043",
    "label": "Exhibit152",
    "context": "Exhibit152: Inhaled LABA-ICS combo TRx market share. Wixela is Mylan's generic Advair Exhibit153: Advair+Breo+Advair authorized generic weekly TRx YoY Exhibit 154: Advair brand vs generics weekly TRx market share Exhibit155: I"
  },
  {
    "figure_id": "F877",
    "report_id": "R043",
    "label": "Exhibit153",
    "context": "Exhibit153: Advair+Breo+Advair authorized generic weekly TRx YoY Exhibit 154: Advair brand vs generics weekly TRx market share Exhibit155: Inhaled LAMA/Combo TRx market share Exhibit156: Trelogy Ellipta (LAMA+LABA+ICS) launch"
  },
  {
    "figure_id": "F878",
    "report_id": "R043",
    "label": "Exhibit 154",
    "context": "Exhibit 154: Advair brand vs generics weekly TRx market share Exhibit155: Inhaled LAMA/Combo TRx market share Exhibit156: Trelogy Ellipta (LAMA+LABA+ICS) launch way above its peers Exhibit 157: Ohtuvayre launch vs Daliresp"
  },
  {
    "figure_id": "F879",
    "report_id": "R043",
    "label": "Exhibit155",
    "context": "Exhibit155: Inhaled LAMA/Combo TRx market share Exhibit156: Trelogy Ellipta (LAMA+LABA+ICS) launch way above its peers Exhibit 157: Ohtuvayre launch vs Daliresp ## Women Health ## Osteoporosis"
  },
  {
    "figure_id": "F880",
    "report_id": "R043",
    "label": "Exhibit155",
    "context": "Exhibit155: Inhaled LAMA/Combo TRx market share Exhibit156: Trelogy Ellipta (LAMA+LABA+ICS) launch way above its peers Exhibit 157: Ohtuvayre launch vs Daliresp ## Women Health ## Osteoporosis Exhibit 158: AMGN's Prolia vs Eve"
  },
  {
    "figure_id": "F881",
    "report_id": "R043",
    "label": "Exhibit 158",
    "context": "Exhibit 158: AMGN's Prolia vs Evenity TRx launch trends Vaccines Exhibit 159: RSV vaccine launch"
  },
  {
    "figure_id": "F882",
    "report_id": "R043",
    "label": "Exhibit 158",
    "context": "Exhibit 158: AMGN's Prolia vs Evenity TRx launch trends Vaccines Exhibit 159: RSV vaccine launch Exhibit 160: RSV vaccine as of launch chart"
  },
  {
    "figure_id": "F883",
    "report_id": "R043",
    "label": "Exhibit 159",
    "context": "Exhibit 159: RSV vaccine launch Exhibit 160: RSV vaccine as of launch chart Exhibit 161: Prevnar franchise absolute TRx and YOY Exhibit 162: Pneumovax absolute TRx and YOY"
  },
  {
    "figure_id": "F884",
    "report_id": "R043",
    "label": "Exhibit 160",
    "context": "Exhibit 160: RSV vaccine as of launch chart Exhibit 161: Prevnar franchise absolute TRx and YOY Exhibit 162: Pneumovax absolute TRx and YOY Exhibit 163: Gardasil absolute TRx and YOY"
  },
  {
    "figure_id": "F885",
    "report_id": "R043",
    "label": "Exhibit 161",
    "context": "Exhibit 161: Prevnar franchise absolute TRx and YOY Exhibit 162: Pneumovax absolute TRx and YOY Exhibit 163: Gardasil absolute TRx and YOY Exhibit 164: Comirnaty absolute TRx and YOY"
  },
  {
    "figure_id": "F886",
    "report_id": "R043",
    "label": "Exhibit 161",
    "context": "Exhibit 161: Prevnar franchise absolute TRx and YOY Exhibit 162: Pneumovax absolute TRx and YOY Exhibit 163: Gardasil absolute TRx and YOY Exhibit 164: Comirnaty absolute TRx and YOY Exhibit 165: Spikevax absolute TRx and YOY"
  },
  {
    "figure_id": "F887",
    "report_id": "R043",
    "label": "Exhibit 163",
    "context": "Exhibit 163: Gardasil absolute TRx and YOY Exhibit 164: Comirnaty absolute TRx and YOY Exhibit 165: Spikevax absolute TRx and YOY Exhibit 166: Covid Vaccine weekly TRx since August 2023"
  },
  {
    "figure_id": "F888",
    "report_id": "R043",
    "label": "Exhibit 164",
    "context": "Exhibit 164: Comirnaty absolute TRx and YOY Exhibit 165: Spikevax absolute TRx and YOY Exhibit 166: Covid Vaccine weekly TRx since August 2023"
  },
  {
    "figure_id": "F889",
    "report_id": "R043",
    "label": "Exhibit 165",
    "context": "Exhibit 165: Spikevax absolute TRx and YOY Exhibit 166: Covid Vaccine weekly TRx since August 2023 Exhibit 167: Covid Vaccine monthly TRx (Mn) since launch IQVIA Disclosure"
  },
  {
    "figure_id": "F890",
    "report_id": "R043",
    "label": "Exhibit 166",
    "context": "Exhibit 166: Covid Vaccine weekly TRx since August 2023 Exhibit 167: Covid Vaccine monthly TRx (Mn) since launch IQVIA Disclosure Monthly TRx (NPA) and Sales (NSP) channel sources"
  },
  {
    "figure_id": "F891",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Exports of goods on track to reach USD 1 trillion in 2026 on strong memory demand Exhibit 2: Recent surge in foreign equity outflows outweighed gains in the current account, weakening KRW 2. We raise our growth forec"
  },
  {
    "figure_id": "F892",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "Exhibit 3: We expect growth meaningfully higher in 2027 than consensus"
  },
  {
    "figure_id": "F893",
    "report_id": "R044",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Increasing dominance of public sector jobs in labor markets in Korea"
  },
  {
    "figure_id": "F894",
    "report_id": "R044",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Increasing dominance of public sector jobs in labor markets in Korea"
  },
  {
    "figure_id": "F895",
    "report_id": "R044",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Korea's tech sector accounts for far smaller jobs and total wages paid than Taiwan"
  },
  {
    "figure_id": "F896",
    "report_id": "R044",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Korea's tech sector accounts for far smaller jobs and total wages paid than Taiwan 6. The key question, then, is whether higher memory-sector wages could spill over to the rest of the economy. We think this spillover r"
  },
  {
    "figure_id": "F897",
    "report_id": "R044",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Large divergence in profits between chip and other sectors Note: Showing consensus estimates for 2026"
  },
  {
    "figure_id": "F898",
    "report_id": "R044",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Large divergence in profits between chip and other sectors Note: Showing consensus estimates for 2026 7. With broader wage spillovers likely contained, inflation pressures should come mainly through imported goods pric"
  },
  {
    "figure_id": "F899",
    "report_id": "R044",
    "label": "Exhibit 8",
    "context": "Note: Showing consensus estimates for 2026 7. With broader wage spillovers likely contained, inflation pressures should come mainly through imported goods prices and exchange rates. Headline inflation has picked up on surging energy prices, largely as expected"
  },
  {
    "figure_id": "F900",
    "report_id": "R044",
    "label": "Exhibit 8",
    "context": "Exhibit 10: The AI boom strengthens Korea's fiscal outlook materially"
  },
  {
    "figure_id": "F901",
    "report_id": "R044",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Market pricing of policy rates is more hawkish than our view"
  },
  {
    "figure_id": "F902",
    "report_id": "R044",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Market pricing of policy rates is more hawkish than our view ## Disclosure Appendix ## Reg AC We, Goohoon Kwon, CFA, Irene Choi and Andrew Tilton, hereby certify that all of the views expressed in this report accuratel"
  },
  {
    "figure_id": "F903",
    "report_id": "R046",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: With a 30% membership coupon on June 22, the deal on Naver/Kurly looks attractive, supported by a more favorable free shipping threshold. Disclaimer: This case is intended to illustrate a specific consumer experience a"
  },
  {
    "figure_id": "F904",
    "report_id": "R046",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 3: SSG.com underscores an assortment constraint - limited SKU availability, driven partly by offline-to-online fulfillment restrictions, caps demand capture today but could improve if regulatory integration evolves."
  },
  {
    "figure_id": "F905",
    "report_id": "R046",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: Baemin B-Mart prioritizes ultra-fast delivery with adequate item availability, but higher pricing and limited assortment confine its value to urgent, short-window needs rather than everyday grocery shopping. The high f"
  },
  {
    "figure_id": "F906",
    "report_id": "R046",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Baemin B-Mart prioritizes ultra-fast delivery with adequate item availability, but higher pricing and limited assortment confine its value to urgent, short-window needs rather than everyday grocery shopping. The high f"
  },
  {
    "figure_id": "F907",
    "report_id": "R047",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: India's current capacity far exceeds the demand for ethanol (20bn litres of capacity vs \\~11 bn litres of consumption) MoPNG, Bernstein analysis and estimates ## ETHANOL STOPS NEAR E25/E27 AND THAT IS THE CEILING There"
  },
  {
    "figure_id": "F908",
    "report_id": "R047",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Fuel Properties E0 to E100: The physics are clear - energy density drops from 32 MJ/L at E0 to 21 MJ/L at E100, while the RON rises from 91 to 120. The jump from E20 to E85 is not incremental; it requires entirely new en"
  },
  {
    "figure_id": "F909",
    "report_id": "R047",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Water requirement is extremely high across ethanol feedstocks highlighting a key sustainability concern."
  },
  {
    "figure_id": "F910",
    "report_id": "R047",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Water requirement is extremely high across ethanol feedstocks highlighting a key sustainability concern. EXHIBIT 6: India has a 4.11 water stress score on a scale of 1 (low stress) to 5 (extremely high stress) vs Brazi"
  },
  {
    "figure_id": "F911",
    "report_id": "R047",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 6: India has a 4.11 water stress score on a scale of 1 (low stress) to 5 (extremely high stress) vs Brazil's 1.04 ## ETHANOL IS NOT CHEAPER THAN PETROL - SO THE CASE FOR GOING FURTHER RESTS ON ONE IDEA: A HEDGE"
  },
  {
    "figure_id": "F912",
    "report_id": "R047",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Water requirement is extremely high across ethanol feedstocks highlighting a key sustainability concern. EXHIBIT 6: India has a 4.11 water stress score on a scale of 1 (low stress) to 5 (extremely high stress) vs Brazi"
  },
  {
    "figure_id": "F913",
    "report_id": "R047",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Mileage loss due to increasing ethanol blend % as per govt studies; however consumers seem to report more mileage loss than the below estimates ## THE HEDGE PAYS ONLY IN A SPIKE - AND BRAZIL BUILT IT OVER FIFTY YEARS,"
  },
  {
    "figure_id": "F914",
    "report_id": "R047",
    "label": "Exhibit 9",
    "context": "EXHIBIT 8: Even with aggressive Flex Fuel Vehicle adoption starting FY28, the petrol stock vehicle by the end of this decade will be significant Fleet Movement of Stock Cars across Powertrains with aggressive FFV adoption EXHIBIT"
  },
  {
    "figure_id": "F915",
    "report_id": "R047",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Crude savings from Increasing Blend Rate and Flex Fuel PV adoption will be low in the next 5 years even in the aggressive scenario (Flex fuel replace Petrol Vehicle sales) - Scenario Analysis for 2030/2035/2040 Crude Imp"
  },
  {
    "figure_id": "F916",
    "report_id": "R047",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: Thailand's E85 failure is the most recent and directly relevant global precedent for India. It shows that subsidy-dependent high-blend ethanol is structurally unsustainable without Brazil-like conditions. Against these"
  },
  {
    "figure_id": "F917",
    "report_id": "R047",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: Thailand's E85 failure is the most recent and directly relevant global precedent for India. It shows that subsidy-dependent high-blend ethanol is structurally unsustainable without Brazil-like conditions. Against these"
  },
  {
    "figure_id": "F918",
    "report_id": "R047",
    "label": "EXHIBIT 12",
    "context": "Against these three stands Brazil, the exception that proves the rule - and even Brazil should temper rather than inflame the ambition. Brazil sustains high blends because it has what no one else has: sugarcane yields near 7,000 litres a hectare, an 8–10 times"
  },
  {
    "figure_id": "F919",
    "report_id": "R048",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 618 online GSV yoy moderated to 6% in 2026 vs. 10% in 2025 per Analysys 618 Shopping festival online GSV YoY growth Exhibit 2: Industry online GMV (excl. Taobao) reached Rmb864bn this 618 largely flat yoy per Syntun 61"
  },
  {
    "figure_id": "F920",
    "report_id": "R048",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Compared to the 618 shopping festival last year, discounts were higher in most segments with snacks cutting back on discounts while beauty/jewelry were flat yoy We use the change in price after discounts for ACs to calcu"
  },
  {
    "figure_id": "F921",
    "report_id": "R048",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Jewelry offered mixed discount rate vs. year ago Discount rate comparison (Jewelry) ## Sportswear"
  },
  {
    "figure_id": "F922",
    "report_id": "R048",
    "label": "Exhibit 11",
    "context": "Exhibit 11: AC discounts narrowed vs. a year ago Discount price comparison (air conditioner) ## Dairy and IMF Dairy and IMF discounts broadened vs. last 6.18, incl. liquid milk of Mengniu/Bellamy's and A2 milk. For top listed comp"
  },
  {
    "figure_id": "F923",
    "report_id": "R048",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Discounts for Yili and Mengniu in general broadened yoy Discount rate comparison (dairy) Exhibit 13: Discount level of A2 Milk and Mengniu notably broadened Discount rate comparison (IMF) Exhibit 14: Discount rate of"
  },
  {
    "figure_id": "F924",
    "report_id": "R048",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Discounts for Yili and Mengniu in general broadened yoy Discount rate comparison (dairy) Exhibit 13: Discount level of A2 Milk and Mengniu notably broadened Discount rate comparison (IMF) Exhibit 14: Discount rate of"
  },
  {
    "figure_id": "F925",
    "report_id": "R048",
    "label": "Exhibit 13",
    "context": "Exhibit 16: Compound condiment and convenience food showed broader discount rates by SKU Discount rate comparison (condiment & convenience food)"
  },
  {
    "figure_id": "F926",
    "report_id": "R048",
    "label": "Exhibit 14",
    "context": "Exhibit 16: Compound condiment and convenience food showed broader discount rates by SKU Discount rate comparison (condiment & convenience food) Exhibit 17: Pet food SKUs showed broader discounts vs. last year"
  },
  {
    "figure_id": "F927",
    "report_id": "R048",
    "label": "Exhibit 15",
    "context": "Exhibit 17: Pet food SKUs showed broader discounts vs. last year Discount rate comparison (pet food)"
  },
  {
    "figure_id": "F928",
    "report_id": "R048",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Compound condiment and convenience food showed broader discount rates by SKU Discount rate comparison (condiment & convenience food) Exhibit 17: Pet food SKUs showed broader discounts vs. last year Discount rate compar"
  },
  {
    "figure_id": "F929",
    "report_id": "R050",
    "label": "Exhibit 1",
    "context": "Exhibit 2: MLCC evolution in AI servers"
  },
  {
    "figure_id": "F930",
    "report_id": "R050",
    "label": "Exhibit 1",
    "context": "Exhibit 2: MLCC evolution in AI servers ## Channel Checks Our recent channel checks point to 200%–300% price increases at distributors since 1Q26 (vs. a 10x peak in 2017) and direct sales up to 30% QoQ. \\- Spot pricing: The Huaqi"
  },
  {
    "figure_id": "F931",
    "report_id": "R050",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Taiwan monthly MLCC sales – cycle edging up with May +40% YoY ## Market structure Who dominates? The high-end AI MLCC market is dominated by a Japanese-Korean duopoly, with a combined 85% market share. \\- Murata (45% s"
  },
  {
    "figure_id": "F932",
    "report_id": "R050",
    "label": "Exhibit 4",
    "context": "Exhibit 4: MLCC Bull-Base-Bear risk reward analysis ## Key Charts Exhibit 5: MLCC remains one of the best performing segments within Asia Tech YTD"
  },
  {
    "figure_id": "F933",
    "report_id": "R050",
    "label": "Exhibit 4",
    "context": "Exhibit 4: MLCC Bull-Base-Bear risk reward analysis ## Key Charts Exhibit 5: MLCC remains one of the best performing segments within Asia Tech YTD Exhibit 6: SEMCO outperform MLCC peers YTD Exhibit 7: MLCC group now trading a"
  },
  {
    "figure_id": "F934",
    "report_id": "R050",
    "label": "Exhibit 5",
    "context": "Exhibit 5: MLCC remains one of the best performing segments within Asia Tech YTD Exhibit 6: SEMCO outperform MLCC peers YTD Exhibit 7: MLCC group now trading at 9.6x NTM P/B vs. historical average of 1.7x"
  },
  {
    "figure_id": "F935",
    "report_id": "R050",
    "label": "Exhibit 6",
    "context": "Exhibit 6: SEMCO outperform MLCC peers YTD Exhibit 7: MLCC group now trading at 9.6x NTM P/B vs. historical average of 1.7x Exhibit 8: Taiwan monthly MLCC sales – cycle edging up with May +40% YoY Exhibit 9: Earnings revision"
  },
  {
    "figure_id": "F936",
    "report_id": "R050",
    "label": "Exhibit 7",
    "context": "Exhibit 10: EPS revision YTD"
  },
  {
    "figure_id": "F937",
    "report_id": "R050",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Taiwan monthly MLCC sales – cycle edging up with May +40% YoY Exhibit 9: Earnings revision breadth has bounced back since Oct-25 and is moving to positive territory Exhibit 10: EPS revision YTD ## Will AI Impact ML"
  },
  {
    "figure_id": "F938",
    "report_id": "R050",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Earnings revision breadth has bounced back since Oct-25 and is moving to positive territory Exhibit 10: EPS revision YTD ## Will AI Impact MLCC? MLCCs (multilayer ceramic capacitors) are critical components in modern"
  },
  {
    "figure_id": "F939",
    "report_id": "R050",
    "label": "Exhibit 11",
    "context": "Exhibit 11: VR200 MLCC unit demand is rising to 570K+, up close to 80% vs a GB300 rack Exhibit 13: Demand for high-cap (47uF+) MLCC is growing faster ## Market outlook"
  },
  {
    "figure_id": "F940",
    "report_id": "R050",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Global MLCC market forecasts"
  },
  {
    "figure_id": "F941",
    "report_id": "R050",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Global MLCC market forecasts Exhibit 15: Global MLCC shipment value to continue rising, driven by AI-related high-value products AI Server MLCC Demand (US\\$ M) Exhibit 16: By 2027, AI server MLCC demand will likely alr"
  },
  {
    "figure_id": "F942",
    "report_id": "R050",
    "label": "Exhibit 15",
    "context": "Exhibit 17: MLCC market share"
  },
  {
    "figure_id": "F943",
    "report_id": "R050",
    "label": "Exhibit 17",
    "context": "Exhibit 17: MLCC market share Exhibit 18: MLCC market share (CY25) 1. How does profitability compare? This question comes to us regularly as business mix varies as well as level of disclosure. We highlight margin dynamics below,"
  },
  {
    "figure_id": "F944",
    "report_id": "R050",
    "label": "Exhibit 17",
    "context": "Exhibit 19: MLCC player EBITDA margin"
  },
  {
    "figure_id": "F945",
    "report_id": "R050",
    "label": "Exhibit 18",
    "context": "Exhibit 20: SEMCO and Yageo leading growth into next upcycle"
  },
  {
    "figure_id": "F946",
    "report_id": "R050",
    "label": "Exhibit 19",
    "context": "Exhibit 21: MLCC players' FCF conversion"
  },
  {
    "figure_id": "F947",
    "report_id": "R050",
    "label": "Exhibit 20",
    "context": "Exhibit 22: Improving ROIC into 2026-28e"
  },
  {
    "figure_id": "F948",
    "report_id": "R050",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Improving ROIC into 2026-28e SEMCO – 1Q26 results were strong, with revenue +17% YoY (+3% vs. consensus) and operating profit +40% YoY (+75% YoY excluding a one-off severance expense), beating an already elevated conse"
  },
  {
    "figure_id": "F949",
    "report_id": "R050",
    "label": "Exhibit 23",
    "context": "Exhibit 23: MLCC group now trading at 9.6x NTM P/B vs. historical average of 1.7x Exhibit 24: MLCC High-end (Japan/Korea) vs. Low-end (Taiwan/China) relative performance Exhibit 25: SEMCO outperforming MLCC peers YTD"
  },
  {
    "figure_id": "F950",
    "report_id": "R050",
    "label": "Exhibit 23",
    "context": "Exhibit 23: MLCC group now trading at 9.6x NTM P/B vs. historical average of 1.7x Exhibit 24: MLCC High-end (Japan/Korea) vs. Low-end (Taiwan/China) relative performance Exhibit 25: SEMCO outperforming MLCC peers YTD Exhibit 2"
  },
  {
    "figure_id": "F951",
    "report_id": "R050",
    "label": "Exhibit 24",
    "context": "Exhibit 24: MLCC High-end (Japan/Korea) vs. Low-end (Taiwan/China) relative performance Exhibit 25: SEMCO outperforming MLCC peers YTD Exhibit 26: Earnings revision breadth has bounced back since Oct-25 # Raising SEMCO Earning"
  },
  {
    "figure_id": "F952",
    "report_id": "R050",
    "label": "Exhibit 25",
    "context": "Exhibit 25: SEMCO outperforming MLCC peers YTD Exhibit 26: Earnings revision breadth has bounced back since Oct-25 # Raising SEMCO Earnings and PT ## Investment thesis – MLCC three key drivers The company aligns its MLCC roadmap"
  },
  {
    "figure_id": "F953",
    "report_id": "R050",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Silicon capacitor mounting locations determined by package type and thickness ## What's next? SEMCO is likely to be a leader in next generation glass substrate – a cutting-edge solution that enhances the durability and"
  }
]