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
    "title": "GS：亚洲央行正在打一场“汇率防御战”，但真正决定胜负的变量不在利率",
    "digest": "[wechat_article.md]\n# GS：亚洲央行正在打一场“汇率防御战”，但真正决定胜负的变量不在利率\n\n当一场地缘冲突持续进入第四个月，最初被市场视为“短期冲击”的能源价格上涨，已经演变为对亚洲货币的系统性压力测试。过去三个月，除人民币外的所有亚洲货币对美元均出现贬值，韩元、印尼盾、菲律宾比索和印度卢比相继突破前期低点。外汇储备的普遍消耗，是这场防御战最直观的成本。\n\n大多数市场讨论仍停留在“央行是否加息”的表层叙事上。但这份来自GS的研报揭示了一个更深层的判断：亚洲央行的政策工具箱正在发生结构性切换——从单纯消耗储备的“干预模式”，转向加息、资本流入管理和行政措施的组合拳。这不仅仅是应对方式的升级，更意味着各国对“汇率弱势容忍度”的重新定价。\n\n真正值得关注的，不是哪家央行会加息，而是这场防御战之后，亚洲货币的相对强弱格局将如何被重塑。GS的核心结论是：在能源冲击得到明确解决之前，亚洲货币难以对美元出现显著升值。但在这个大背景下，不同经济体的分化路径已经清晰可见——而这恰恰是资产配置的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 加息只是表象，真正起作用的是“三重干预”组合\n\n理解亚洲央行当前的政策逻辑，不能只看利率决议。GS的报告指出，这轮政策响应的广度远超市场预期。以印尼央行为例，其在5月加息50个基点、6月非会议时间再加息25个基点之外，还同步推出了三项关键措施：提高SRBI各期限收益率、将外资对冲掉期利率降低10%，以及强化“三重干预”政策（即干预即期、远期和境内债券市场）。\n\n菲律宾央行则是加息政策最为激进的先行者——4月率先加息25个基点至4.50%，GS预计还将连续四次加息。韩国央行虽然按兵不动，但转向了更鹰派的措辞，同时鼓励国民年金公团进行汇率对冲，这是典型的资本流动管理手段。\n\n印度储备银行则采取了“利率不动、规\n\n[... middle omitted ...]\n\n工具箱深度”和“能源依赖度”两个维度上均优于泰国。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲央行出手，货币保卫战升级\n\n汇率保卫战，央行动真格了\n\n最近亚洲货币普遍承压，各国央行终于坐不住了。从加息到外汇干预，一套组合拳打下来，效果怎么样？我们一起来拆解。\n\n1️⃣ 加息+干预，央行双管齐下\n- 菲律宾央行率先加息25bp，通胀压力下不得不行动\n- 印尼央行更猛，50bp+25bp连续加息，还出新招吸引外资\n- 印度央行虽然按兵不动，但也在调整政策吸引资金流入\n- 韩国更侧重资本流动管理，鼓励养老金做汇率对冲\n\n2️⃣ 人民币逆势走强，逻辑在哪？\n- 整个亚洲货币都在跌，人民币却在升值\n- 出口持续强劲，企业结汇意愿提升\n- 央行似乎乐见这种温和升值节奏，年化约4%\n- 预计6个月到6.70，12个月到6.50\n\n3️⃣ 韩元困局：出口爆棚，汇率反跌\n- AI带动的半导体出口超强，KOSPI涨了90%\n- 但外资反而净卖出800亿美元韩国股票\n- 原因：两大半导体公司权重太高，触发减持\n- 如果涨势扩散到其他股票，外资可能回流\n\n4️⃣ 新台币：出口明星，汇率稳中有升\n- 出口增速40-70%，GDP冲到13.7%\n- 半导体出口抵消了油价上涨的影响\n- 经常账户盈余创新高，支撑新台币表现\n\n5\n\n[... middle omitted ...]\n\nwn in FX reserves. However, as the conflict has entered its fourth month, policy responses have since broadened across Asia. The BSP raised the policy rate by 25bp to $4.50\\%$ in April, citing\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "GS：美元并非被高估，而是被错误定价——能源冲击的“项圈效应”才是核心",
    "digest": "[wechat_article.md]\n# GS：美元并非被高估，而是被错误定价——能源冲击的“项圈效应”才是核心\n\n这份最新发布的GS外汇策略报告，标题看似平淡——“项圈中的美元”——但如果你只看到它对美元短期走势的判断，就错过了真正的信号。报告的核心主张不在于预测美元涨跌，而在于揭示一个正在发生的、市场尚未充分定价的机制切换：全球外汇市场的定价权，正在从宏观风险偏好（AI叙事、商品价格）向国内利率差异（货币政策分化、实际利差）转移。这个转移，将重新定义未来6-12个月所有主要货币对的交易逻辑。\n\n报告发布于一个微妙的时点。市场仍在消化中东冲突对能源供应的冲击，AI驱动的资本开支周期正经历第一轮预期修正，而美联储即将召开会议。在这样的背景下，GS团队没有给出简单的“买美元”或“卖美元”建议，而是提供了一个分析框架：理解当前外汇市场，需要同时把握两个维度——能源冲击的持续时间和国内政策的分化程度。前者决定美元的底部，后者决定货币对的相对强弱。\n\n这份报告最有价值的判断是：市场真正低估的不是美元的方向，而是能源冲击正在从“脉冲式扰动”演变为“结构性约束”。这意味着，传统上依赖风险偏好和增长差异的外汇交易模型，可能需要重新校准。GS用两个图表清晰地展示了这种切换——从3-4月全球因素（股票、商品）主导汇率波动，到5月后利率差异重新成为关键驱动。这个信号，对于任何持有跨境资产或关注汇率风险敞口的决策者，都值得认真对待。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源冲击的“项圈效应”：收窄美元波动区间，而非决定方向\n\n理解这份报告的关键，在于区分“能源冲击的规模”和“能源冲击的持续性”。GS的观点是，市场可能过于关注前者——即油价具体涨多少——而低估了后者带来的结构性影响。报告原文指出：“过热的油价正在降温，这让美元被困在项圈中。”这个判断的底层逻辑是：\n\n[... middle omitted ...]\n\n球外汇市场的结构性变化，这些讨论会比任何单一报告都更具价值。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元被油价“拴住”了\n\n美元窄幅震荡\n\n能源扰动下，美元短期承压\n\n最近美元走势有点纠结，核心原因在油价。\n\n1️⃣ 能源供应冲击降温 → 美元失去一部分向上动力\n投行研报指出，AI 繁荣和能源短缺原本是支撑美元的两大支柱，但近期油价涨幅收窄，削弱了这波支撑力。短期看，油价持续扰动会限制美元下行空间，但向上突破也需要新催化剂。\n\n2️⃣ 人民币持续走强，压制美元涨幅\n人民币是近期抑制美元指数上涨的关键因素之一。研报认为，中国贸易顺差在5月回升至1056亿美元（4月为977亿），出口韧性超预期。虽然能源和半导体进口成本上升带来短期压力，但绿色科技产业链的结构性优势仍在，人民币仍被低估超20%，预计12个月内美元/人民币目标价6.50。\n\n3️⃣ 英镑：政治事件影响有限\n下周的补选是市场关注点，但研报认为英镑的政治风险溢价并不高。即使工党上台概率上升，对英镑的压制也偏短期。真正决定英镑走势的，还是能源冲击的演变——若中东局势缓和，英镑作为能源进口国货币，可能反弹明显。\n\n4️⃣ 日元：政策空间有限\n日本央行6月预计加息25bp，但市场已充分预期。关键是：若不加码紧缩，日元将继续受制于美日利差、美国经济韧性和国内财\n\n[... middle omitted ...]\n\n sustained energy shortfall grows. At the same time, a growing realization of a smaller-than-expected oil deficit has helped keep growth expectations from diverging further even as the disrupt\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "GS：市场真正低估的不是通胀本身，而是利率曲线重新定价的路径",
    "digest": "[wechat_article.md]\n# GS：市场真正低估的不是通胀本身，而是利率曲线重新定价的路径\n\n当全球投资者还在为地缘政治冲击下的油价波动焦虑时，一份来自GS全球利率交易团队的研报提出了一个更值得深思的框架：市场对短期通胀的定价已经相当充分，但真正未被消化的是利率曲线在多重路径下的重新定价。这份报告的核心判断是——美国利率曲线陡化的概率被系统性低估，而欧洲和英国的前端利率则存在被过度定价的加息风险。\n\n这份报告发布于美联储新主席Warsh首次议息会议前夕，时间点本身就具有信号意义。全球利率市场正在经历一个罕见的“多路径均衡”阶段：油价在供给端冲击与需求端疲软之间拉扯，各国央行在“抗通胀的尾声”与“经济增长的脆弱”之间摇摆，而新一任美联储主席的沟通风格本身就是一个不确定变量。\n\nGS分析师在报告中明确指出，市场定价隐含的加息概率已经包含了过多的鹰派预期。对于美国，30-35个基点的加息风险定价意味着市场已经计入了多次加息的可能性，而GS认为更可能的情景是“长期按兵不动”。对于欧元区和英国，情况则更加复杂——通胀的持续性而非短期油价飙升，才是决定央行政策路径的真正变量。\n\n这篇文章将沿着GS的分析框架，拆解三个核心问题：为什么美国利率曲线陡化被低估、欧洲和英国的利率定价存在什么结构性偏差、以及新一任美联储主席的沟通方式可能如何改变市场游戏规则。最后，我们将指出报告尚未完全回答的几个关键问题，这些将决定投资者能否真正利用这份研报的洞见。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国利率市场最大的误判，是以为“加息风险”就是全部风险\n\nGS研报的第一个核心洞察，直指美国利率市场当前定价的结构性偏差。报告指出，美国前端利率的加息定价已经从高点回落，曲线也从近期低点有所陡化，但市场仍然在接下来一年内定价了30-35个基点的加息风险。这个数字意味着\n\n[... middle omitted ...]\n\n，帮助成员在GS这份框架的基础上，形成自己的判断和交易策略。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球利率市场正在悄悄换锚\n\n利率转向真实信号\n\n全球利率进入“换锚期”\n\n---\n\n1️⃣ **油价不再是唯一剧本**\n市场已在定价“通胀缓解”路径，但真正能锚定长期利率的，是远期油价。短期波动只是噪音。\n\n2️⃣ **美联储新主席的“话术”比点阵图更重要**\nWarsh上任首场FOMC，市场会盯住他如何描述风险平衡。更强调劳动力通胀压力小→曲线陡；更警惕通胀→偏鹰。30-35bp的加息风险已被定价，但研报认为“长时间按兵不动”概率更高。\n\n3️⃣ **欧洲：通胀粘性在“持续”而非“飙升”**\nECB加息是因为通胀持续超预期，而不是短期油价跳涨。所以即便油价回落，欧元前端利率也没掉多少——市场更关注远期油价（如z6合约）。长期看，5y5y真实利率仍值得关注。\n\n4️⃣ **英国：前端利率是“通胀缓解交易”**\n英国利率对油价敏感度最高（图表显示t-stat高达8.5），而经济基本面偏弱。研报认为，如果油价缓和，英镑前端利率有更大下行空间。财政空间有限→宏观缓解要靠利率下降。\n\n5️⃣ **加拿大：加息溢价会慢慢消退**\nBoC按兵不动，增长与政策因素大致对冲。没有明确催化剂的情况下，此前积累的加息溢价会逐步衰\n\n[... middle omitted ...]\n\nhough 1y1y rates have become less sensitive to spot oil prices, the combination of a hawkish central bank, weak data and a shift in the distribution of energy prices skews risks to the downsid\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "GS：高频数据正在揭示一个被低估的“成本传导型”经济周期",
    "digest": "[wechat_article.md]\n# GS：高频数据正在揭示一个被低估的“成本传导型”经济周期\n\n当前市场对中国经济的讨论，大多仍停留在“需求复苏有多强”这个框架里。房地产销售是否企稳、消费信心是否回升、出口订单是否可持续——这些问题的答案当然重要，但它们可能正在让人忽略一个更深层的结构性变化。\n\nGS在6月12日发布的这份中国经济高频追踪周报中，释放了一个值得反复推敲的信号：**中国经济的短期波动，正在从“需求驱动”向“供给成本驱动”切换。** 进口价格、出口价格、工业品价格之间的联动关系，正在形成一个过去几年罕见的传导链条。这一链条的走向，将直接决定2025年下半年到2026年的企业盈利分配、通胀路径以及政策空间。\n\n这份报告的核心价值，不在于它提供了多少数据点，而在于它用一种“高频+多维”的视角，捕捉到了传统月度或季度数据容易平滑掉的拐点。以下是我们从这份报告提炼出的四个核心洞察，以及一个尚未被充分回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费与地产的“温差”正在扩大，高能级市场的韧性被高估\n\n报告中的高频消费数据，呈现出一种罕见的“背离”状态。一方面，Morning Consult的消费者信心指数在5月攀升至多年新高，甚至超过了2021年的水平。另一方面，真实世界的消费活动，至少在几个关键维度上，并没有同步走强。\n\n最值得关注的是房地产市场。报告显示，30城新房日均成交面积在6月已跌至低于去年同期水平。而16城二手房成交量虽然仍高于去年，但环比已出现明显下滑。新房与二手房之间的“温差”，暗示市场正在经历一个“以价换量”的尾声阶段——二手房的放量，更多依赖业主降价，而非真实需求的持续涌入。\n\n与此同时，国内航班量虽然有所回升，但依然低于去年同期；航班取消率虽有下降，但绝对水平仍然偏高。这说明居民的跨区域流动意愿，并未完\n\n[... middle omitted ...]\n\n们会持续追踪这些高频信号的变化，并给出更贴近投资决策的解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n消费弱了，地产还在磨底\n\n地产、出行、消费都在降温\n\n某外资投行最新周度追踪显示，当前经济活动呈现“消费降温、生产平稳”的分化格局。\n\n1️⃣ 地产成交继续走弱\n30城新房成交面积已低于去年同期水平，16城二手房成交虽高于去年但也在回落。地产“小阳春”效应消退明显，后续政策窗口值得关注。\n\n2️⃣ 出行消费边际放缓\n国内航班量低于去年同期，航班取消率虽下降但仍偏高。交通拥堵指数上周基本持平，没有出现明显反弹。汽油柴油价格保持不变，居民出行意愿偏谨慎。\n\n3️⃣ 汽车销售不及去年\n5月新能源车销量环比提升，但同比仍低于去年。整体汽车销量小幅走高，同样低于去年同期水平。消费端的修复需要更多时间。\n\n4️⃣ 工业生产相对稳定\n钢铁需求和生产在过去一周变化不大，产量基本持平。但进口能源和集成电路价格在5月大幅上涨，成本端压力正在累积。\n\n5️⃣ 一个积极信号\nMorning Consult消费者信心指数升至多年新高，说明居民对未来的预期在改善。但信心的修复需要传导到实际消费行为，中间还有一段路。\n\n整体来看，当前经济处于“预期改善、现实偏弱”的阶段，地产和消费是主要拖累项，后续政策节奏值得跟踪。\n\n#学习笔记\n\n[s\n\n[... middle omitted ...]\n\n)\n\n<details>\n<summary>line chart</summary>\n\n| Date       | 2019 (Thousand sqm) | 2025 (Thousand sqm) | 2026 (Thousand sqm) |\n|------------|---------------------|---------------------|---------\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "GS：韩国股市的真正机会不在大盘，而在被低估的KOSDAQ",
    "digest": "[wechat_article.md]\n# GS：韩国股市的真正机会不在大盘，而在被低估的KOSDAQ\n\n当全球投资者都在盯着KOSPI的波动和外资流出时，一个更值得关注的信号正在被忽视：KOSDAQ正在吸引结构性的外资流入，而其背后的驱动因素——盈利修正的背离与估值的错位——恰恰构成了一个战术性alpha机会。这是GS最新一期韩国市场周报中，最值得认真对待的一个判断。\n\n这份报告发布于市场持续波动的背景下。KOSPI上周小幅下跌0.5%，外资净卖出4,400亿韩元，主要集中在科技和造船板块。与此同时，KOSDAQ逆势上涨2.7%，外资净流入67亿韩元。韩元兑美元单周升值2.8%，韩国股票风险指标进一步滑入风险厌恶区域。这些数字本身并不惊人，但将它们放在一起看，一个清晰的图景浮现出来：市场正在重新定价韩国股市的内部结构，而大多数投资者可能还停留在对大盘的单一关注中。\n\nGS的核心论点并不复杂，但需要认真拆解。自2023年8月以来，KOSDAQ相对于KOSPI持续跑输，累计差距已相当显著。但与此同时，KOSDAQ的盈利修正却远弱于KOSPI——KOSPI的12个月远期每股盈利上修幅度显著强于KOSDAQ。更关键的是，尽管KOSDAQ大幅跑输，其估值却仍然比KOSPI更贵：KOSDAQ的12个月远期市盈率远高于KOSPI，而其盈利修正却弱得多。这种“估值溢价+盈利弱势”的组合，通常意味着市场对KOSDAQ的定价存在某种结构性偏差。\n\n然而，外资的行为却在讲述另一个故事。今年以来，KOSPI遭遇了大规模外资流出，但KOSDAQ却吸引了持续的外资流入。GS分析认为，KOSPI的外资流出很大程度上与投资组合再平衡有关，尤其是两只最大的半导体股票贡献了大部分卖压。而流入KOSDAQ的外资则高度集中在信息技术和医疗保健板块。这种资金流向的分化，与盈利修正和估值的背离形成了有趣的对照。\n\n这意味着什么？简单说，市\n\n[... middle omitted ...]\n\n的拆解和推演。完整的GS报告原文及原始图表，也将在群内分享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国股市有个“隐藏”机会\n\nKOSDAQ 战术窗口\n\n外资在悄悄调仓\n\n最近韩国市场波动不小，KOSPI 一周微跌 0.5%，但 KOSDAQ 反而涨了 2.7%。一个有意思的现象是：一边是外资持续卖出 KOSPI，一边却在悄悄买入 KOSDAQ。\n\n1/ 为什么 KOSPI 被卖？\n外资流出主要集中在 KOSPI 的科技和造船板块。研报指出，卖盘主要来自两只最大的半导体股，背后可能是组合再平衡的需求。与此同时，韩国风险指标已跌至 -2.1，市场情绪偏谨慎。\n\n2/ KOSDAQ 的“逆袭”逻辑\n虽然 KOSDAQ 自 2023 年 8 月以来跑输 KOSPI，但最近几周表现更强。外资今年流入 KOSDAQ 的板块集中在信息技术和医疗保健。研报认为，KOSDAQ 的估值虽然比 KOSPI 贵（28.8 倍 vs 7.1 倍远期 PE），但盈利修正趋势在改善，存在战术性轮动机会。\n\n3/ 行业冷热对比\n上周表现最好的行业：建筑（+10.8%）、休闲（+4.4%）、机械（+2.8%）。\n表现最差的：软件（-9.3%）、汽车（-5.3%）、证券（-3.9%）。\n化工板块盈利上修最强，休闲板块下修最多。\n\n4/ 汇率\n\n[... middle omitted ...]\n\nearnings revisions, while the Leisure sector was revised down the most this week (Exhibit 21).  \nThe KRW strengthened 2.8% vs. USD this week. It also strengthened by 2.6% vs. JPY and 2.3% vs. \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "NOM：中国利率市场真正被低估的风险不是降息预期，而是流动性正常化的传导加速",
    "digest": "[wechat_article.md]\n# NOM：中国利率市场真正被低估的风险不是降息预期，而是流动性正常化的传导加速\n\n过去两个月，中国债券市场经历了一轮罕见的“先涨后跌”行情。5月末，各期限利率下行4-6个基点，市场一度沉浸在“宽松延续”的叙事中。但进入6月，利率迅速反弹约4-5个基点，将此前涨幅几乎全部回吐。\n\n市场参与者习惯性地将这一切归因于央行降息或政策信号。但NOM最新发布的这份中国利率策略报告，提供了一个更值得警惕的判断框架：真正驱动利率走向的，不是降息与否，而是一套被市场低估的流动性正常化机制正在加速运转。这份报告的核心主张是，过去几个月支撑债市极度宽松的流动性环境正在系统性逆转，而这一过程才刚刚开始。\n\nNOM明确提出，维持做空3年期NDIRS的头寸，目标看向1.60%。这个判断并非基于对经济数据的乐观，而是基于对流动性供给结构、债券发行节奏以及机构行为三重变量的拆解。以下是我们从这份研报中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 央行已经在悄悄收紧中期流动性，而市场直到6月才反应过来\n\n市场对央行操作的关注，往往集中在7天逆回购利率或MLF利率是否调整。但NOM指出，真正重要的变化发生在“中期货币政策工具”的净投放上。\n\n数据显示，今年1-2月，央行通过MLF、买断式逆回购、国债净买入等工具，累计净投放流动性约2.05万亿元，远超历史均值。这解释了为什么一季度市场流动性极度充裕。但从3月开始，情况逆转：3月净回笼200亿元，4月净回笼560亿元，5月净回笼850亿元。到了6月5日，央行又通过3个月期买断式逆回购净回笼300亿元。结果就是，截至6月初，今年以来的累计中期净投放已降至仅140亿元，远低于2020-2025年约1.1万亿元的平均水平。\n\n这个数字意味着什么？意味着过去两个月支撑债市上涨的“流动\n\n[... middle omitted ...]\n\n的星球微信群继续交流。那里有更完整的研报原文和更深入的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n债市逻辑变了，流动性收紧信号已现\n\n流动性收紧，债市风向变了\n\n📌 最近债市发生了一个关键变化：流动性真的开始收紧了。等了很久的“流动性正常化”终于到来。\n\n📌 核心逻辑两点：\n1️⃣ 央行在收紧中长期流动性。3月以来，通过MLF、逆回购等手段持续净回笼资金，累积净投放已降至远低于往年平均的水平。\n2️⃣ 政府债供给即将放量。前5个月国债+地方债发行进度仅35%，落后于往年，这意味着Q3供给压力会显著加大。\n\n📌 资金面信号：\n- 7天回购利率已回到1.4%以上，且6月以来反弹明显\n- 存单发行转正，到期量巨大（本周+下周合计9400-9600亿）\n- DR007和1年NCD收益率自6月5日起明显上行\n\n📌 机构行为也在变：\n5月基金大买长债后，6月开始减仓，尤其本周卖出了大量10年政金债。保险则在30年国债下跌时开始加仓，形成一定支撑。\n\n📌 关注两个关键点位：\n10年国债1.75%、30年国债2.25%——如果收益率触及这些位置，可能有“逢跌买入”资金入场。\n\n#学习笔记\n\n[source_mineru.md]\n## China rates: Maintain pay 3y NDIRS position\n\n[... middle omitted ...]\n\nn long bond positions.\n\n## The long-awaited liquidity normalization has finally happened\n\nIn the last week of May, China rates rallied by 4-6bp across tenors, owing to flush liquidity (the PBo\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R007",
    "title": "UBS：汽车半导体复苏已至，但真正的分歧在“中国放缓”与“工业超预期”之间",
    "digest": "[wechat_article.md]\n# UBS：汽车半导体复苏已至，但真正的分歧在“中国放缓”与“工业超预期”之间\n\n汽车半导体行业正在走出长达两年的去库存周期。UBS在最新发布的研报中确认，2026年Q1汽车半导体收入同比增速达到7.8%，这是两年多来首次出现明确的同比增长。模拟芯片收入更是同比增长20%，且这一势头预计将贯穿整个2026年。\n\n但这份报告的真正价值不在于确认复苏，而在于揭示一个多数市场参与者尚未完全定价的结构性分化：中国市场的需求正在放缓，而工业领域的增长正在超预期加速。这两股力量的方向相反，但都在同一个时间窗口内作用于全球汽车半导体公司的业绩与估值。\n\nUBS维持了对2026年汽车半导体市场10%同比增长的预测，但明确提醒，中国1-5月零售数据已出现15%-20%的同比下滑，其中新能源汽车下滑10%-15%。如果这一趋势在下半年引发库存修正，全球汽车半导体增长可能面临显著的下行风险。\n\n与此同时，工业领域的半导体需求正在被AI相关产品拉动，UBS将2026年工业半导体收入增速预测从16%上调至25%。这意味着，那些同时覆盖汽车和工业市场的模拟芯片公司，其业绩分化将比行业整体更加剧烈。\n\n复苏是真实的，但复苏的结构并不均匀。对于投资者而言，问题不再是“要不要配置汽车半导体”，而是“在哪些公司、哪些下游、哪些区域中配置”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模拟芯片的涨价周期正在打开一个被低估的利润弹性\n\nUBS的分销商追踪数据显示，Q1多家模拟芯片公司已开始提价，包括TI、英飞凌和恩智浦。提价的直接原因是通胀成本传导，但其隐含意义远不止于此。\n\n在去库存周期的尾声阶段，市场普遍预期2026年模拟芯片价格将出现低个位数下降。但UBS指出，目前的价格走势表明，实际定价可能持平甚至略好于预期。这意味着，此前被计入估值模型的\n\n[... middle omitted ...]\n\n性。这些问题的答案，将直接影响你对汽车半导体板块的配置判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n车规芯片复苏中，但得挑着看\n\n芯片回暖，但要选对方向\n\n汽车半导体正在走出低谷，但别急着all in\n\n---\n\n最近看了某外资投行刚出的车规芯片研报，几个关键点值得记一下。\n\n**1/ 模拟芯片还在涨，但估值已经不便宜了**\n\nQ1营收同比增长20%，Q2预计也有21%。几个大厂都已经开始提价，主要是通胀成本传导。但要注意，目前模拟芯片板块的12个月前瞻PE已经到了30倍，而十年均值才19倍。涨了不少，安全边际在收窄。\n\n**2/ 汽车芯片确实在复苏，但中国是个变数**\n\n汽车半导体Q1终于恢复了正增长，同比+7.8%，预计全年+10%。但中国前5个月零售数据不太好，全球20-30%的车规芯片需求在中国，如果继续走弱，下半年可能面临库存修正。欧洲和美国的恢复，可能被中国拖后腿。\n\n**3/ 工业芯片超预期，AI是推手**\n\n工业端Q1营收同比+26%，全年预期从16%上调到25%。几个主要玩家都上调了指引，AI相关需求贡献明显。这块比汽车更值得关注。\n\n**4/ 几点个人观察**\n\n- 涨价是好事，但要看持续性\n- 中国新能源车增速放缓，对芯片需求影响不小\n- 估值已经不低，需要更多业绩兑现来支撑\n\n欢迎一\n\n[... middle omitted ...]\n\neve these are limited—primarily within certain AI-related products—and that broader markets still face mixed demand and lingering oversupply. As such, we do not see conditions approaching a CO\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/0c59cc7e8f295942721e98c1c6aa8525e5a1343733979c21f8a685aa17c49772.jpg)"
  },
  {
    "id": "R008",
    "title": "GS：五月信贷超预期，但真正的信号藏在结构里",
    "digest": "[wechat_article.md]\n# GS：五月信贷超预期，但真正的信号藏在结构里\n\n市场对五月金融数据的初步解读，多数停留在“总量超预期”这个层面。新增社融2.03万亿，新增人民币贷款5200亿，双双高于GS和彭博的预测值。如果只看这些数字，似乎可以得出“宽信用正在见效”的乐观结论。\n\n但GS这份研报的核心判断恰恰相反：**总量超预期不是复苏信号，而是结构性疲弱的又一次确认。**\n\n原因在于，数据超预期主要来自银行信贷的供给端发力，而非实体融资需求的真实回暖。当一份信贷报告需要用“票据融资大幅增加”和“中长期企业贷款收缩”来解释时，决策者应当警惕的不是流动性不足，而是信用传导机制中的梗阻。\n\n这份研报最有价值的洞察，不是告诉读者信贷数据超预期了，而是拆解了“为什么超预期反而令人担忧”。对于关注中国经济周期和资产定价的投资者而言，理解这种结构性的分化，远比记住一个总量数字重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 真正支撑总量的不是企业投资意愿，而是银行在“填表”\n\n五月新增人民币贷款5200亿，高于GS预测的4000亿和彭博一致预期的4500亿。表面看是银行放贷意愿增强，但细拆结构会发现，这更像是银行在监管和考核压力下的被动行为。\n\n企业贷款是五月信贷的主要支撑，新增6400亿，高于去年同期的5300亿。但关键在于构成：票据融资贡献了5570亿，短期贷款1000亿，而中长期企业贷款反而净减少200亿。去年同期，中长期企业贷款是净增3300亿。\n\n这个对比意味着什么？中长期贷款通常对应企业的资本开支、设备投资和扩张计划，是衡量真实融资需求的核心指标。当这个指标从净增3300亿转为净减200亿，而票据融资大幅飙升时，最合理的解释是：企业没有投资意愿，银行只能用低成本票据融资来“填满”信贷额度。\n\n票据融资本质上是银行间的一种短期资金安排，\n\n[... middle omitted ...]\n\n群继续讨论，我们将围绕这份研报的未尽议题做进一步的深度拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月社融超预期，但钱去哪了？\n\n**超预期的社融**\n\n**但居民企业都不爱借钱**\n\n5月社融数据出来了，乍一看超了市场预期，但细看结构，还是能感受到实体的“冷”。\n\n某外资投行的研报拆了拆数据，核心逻辑很清晰：\n\n1️⃣ **总量超预期，靠的是银行冲量**\n5月新增社融2.03万亿，比市场预期的1.7万亿高出一截。主要拉动项是银行贷款，新增1.15万亿（季调后），比4月多了2000亿。影子银行（信托+委托贷款）也转正了，从4月的收缩186亿变成新增20亿。但注意，政府债券和企业债券变化不大，说明不是全口径回暖。\n\n2️⃣ **居民和企业，都不愿意借长钱**\n- 居民端：5月住户贷款存量减少1410亿，而去年同期是增加540亿。大家还在去杠杆，消费贷、房贷需求都很弱。\n- 企业端：新增企业贷款6400亿，看似不错，但拆开看——票据融资5570亿，短期贷款1000亿，中长期贷款反而少了20亿（去年同期是增加3300亿）。说明企业只敢借短期周转，不敢投长期项目，信心还在修复。\n\n3️⃣ **M1回升，可能靠财政“输血”**\nM1同比从5.0%微升至5.5%，M2持平在8.6%。但财政存款5月增加了7100亿，比\n\n[... middle omitted ...]\n\nng compared to a year ago.\n\n## Key numbers:\n\nNew RMB loans (flow, reported): RMB +520bn in May (RMB loans to the real economy: RMB 500bn) vs. GS forecast: RMB 400bn, Bloomberg consensus: RMB 4\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "NOM：美元多头共识已达峰值，历史规律指向未来三个月大概率走弱",
    "digest": "[wechat_article.md]\n# NOM：美元多头共识已达峰值，历史规律指向未来三个月大概率走弱\n\n当前市场对美元的共识有多强？NOM最新外汇策略报告给出了一个值得警惕的答案：当“美国例外论”成为客户会议和媒体高频词时，美元多头头寸正在逼近一个危险的临界点。\n\n这份研报的核心判断并非否定美元近期的强势逻辑——美国数据持续超预期、利率重新定价、资本流入加速，这些支撑因素仍然存在。但NOM提出了一个反直觉的历史规律：当美国经济惊喜指数突破60这一阈值后，美元在未来三个月下跌的概率高达75%。当前该指数正处于近三年高位，这意味着市场可能站在美元情绪周期的拐点。\n\n更关键的是，NOM识别出三个可能触发美元逆转的具体风险点：7月美国就业数据的季节性残留效应、新任美联储主席沃什可能释放鸽派信号、以及AI驱动的科技股叙事面临成本质疑。这些因素尚未被市场充分定价，但它们正在积累。\n\n对于持有美元敞口的投资者而言，当前需要关注的不是美元还能涨多少，而是什么会打破这个共识。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 经济惊喜指数已达历史极端区间，美元后续回报历史规律指向弱势\n\nNOM的核心论据建立在一个简洁而有力的统计规律上。报告追溯了美国经济惊喜指数过去23年的全部历史，发现该指数突破60水平共出现41次。当考察随后三个月的美元表现时，结果呈现出高度一致的负面特征：美元兑G10等权重指数的平均回报为-1.8%，而“命中率”——即美元走弱的概率——高达73.2%。\n\n这个规律在分货币对层面同样显著。美元兑欧元、英镑、澳元、新西兰元、挪威克朗和瑞典克朗在三个月窗口期的平均跌幅均超过1.5%，命中率在63%至80%之间。即使是对美元相对抗跌的加元和日元，三个月平均回报也分别为-1.2%和-0.7%。\n\nNOM进一步指出，如果将阈值提高到70，美元在所有表现窗口期\n\n[... middle omitted ...]\n\n键信号的变化，并分享更多未在公开报告中展开的分析框架和图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元强势还能撑多久？几个信号值得看\n\n🔍 美元恐面临反转风险\n\n某外资投行最新研报指出，当前市场对美元过于乐观，但历史上当美国经济数据超预期指数达到当前水平后，美元在接下来三个月里有75%的概率会走弱。\n\n1️⃣ 数据越好，反而越危险？\n美国经济惊喜指数创近三年新高，但研报回溯20年数据发现，当该指数突破60后，美元后续三个月平均下跌1.8%，且这一规律在41次历史样本中一致性很高。简单说：好消息可能已经被定价了。\n\n2️⃣ 三个可能触发反转的变量\n- 7月美国就业数据：过去三年7月非农都大幅低于预期，今年可能重演，冲击“美国例外论”叙事\n- 新任美联储主席Warsh偏鸽派，可能利用就业疲软信号打压市场加息预期\n- AI热潮降温风险：科技股IPO密集、AI投资回报遭质疑，若股价回调将冲击市场情绪\n\n3️⃣ 仓位信号已亮黄灯\n美元多头仓位虽然还没到极端水平，但其他G10货币的空头仓位正在累积。当市场共识过于一致时，往往意味着反转临近。\n\n研报团队目前仍持有美元/加元多头，但对其他货币对已减少美元方向性敞口。欢迎一起讨论你对美元走势的判断。\n\n#学习笔记\n\n[source_mineru.md]\n## FX Ins\n\n[... middle omitted ...]\n\ns also become more skewed to USD longs, exacerbating pullback risk.\n\n## Tactical USD bull case remains intact\n\nThe USD bull case has become more prominent in recent weeks. Strong US data and a\n\n[... middle omitted ...]\n\ninformation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International plc, UK. All rights reserved."
  },
  {
    "id": "R010",
    "title": "NOM：美联储的“按兵不动”比降息或加息更值得市场重新定价",
    "digest": "[wechat_article.md]\n# NOM：美联储的“按兵不动”比降息或加息更值得市场重新定价\n\n市场正在为一个并不存在的降息周期做准备。这并非危言耸听，而是NOM最新一期美国经济周报的核心判断。该报告详细拆解了6月美联储议息会议可能呈现的决策图景，其结论清晰而坚定：联邦基金利率将在当前水平停留至2027年底。对于习惯了“加息-暂停-降息”线性思维的市场参与者而言，这意味着一场对资产定价逻辑的根本性修正。\n\n报告提供的不仅仅是一次会议的预测，而是一整套关于美联储新常态的叙事。其中包含了几个关键信号：鹰派措辞的回归、点阵图中位数的大幅上移、以及新任主席沃尔什对前瞻指引这一传统工具的潜在解构。这些信号叠加在一起，指向一个远比市场当前定价更为严峻的利率环境。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 六月议息会议的核心动作不是加息，而是清除所有关于降息的暗示\n\nNOM预期，6月FOMC会议将维持利率不变，这将是连续第四次按兵不动。但真正重要的政策信号并非利率本身，而是会后声明的措辞调整。报告明确指出，声明将删除所有关于“宽松倾向”（easing bias）的前瞻指引语言，且这一变化将以全票通过的方式呈现。\n\n这意味着，美联储将主动关闭市场对未来降息的任何想象空间。近期多位FOMC与会者已经公开讨论加息的可能性，鹰派声音的密集程度在过去几个月中显著上升。尽管委员会内部仍存在一个“鸽派阵营”，对通胀前景保持谨慎乐观，并认为当前政策具有适度限制性，但这一阵营的声音正在被整体转向鹰派的共识所淹没。\n\n对于资产定价而言，这带来的直接含义是：此前市场所消化的任何降息预期，都需要被重新校准。如果美联储连“暗示降息可能”的措辞都不再保留，那么基于降息逻辑的久期交易、成长股估值、以及新兴市场资本流动假设，都将面临根本性的动摇。\n\n![研报原图 2](assets/\n\n[... middle omitted ...]\n\n”以及上游通胀传导的具体路径——进行深入探讨。期待你的加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储6月按兵不动，点阵图透露什么信号？\n\n**利率暂停，但信号变了**\n\n美联储6月会议大概率维持利率不变，但措辞会转向鹰派。关键看点：点阵图中位数显示，利率可能维持到2027年底。\n\n**1/ 鸽派措辞要删了**\n会后声明可能删除“降息倾向”的表述。近期多位官员公开讨论加息可能性，联储内部鹰派声音明显增强。\n\n**2/ 点阵图：2026-2027无降息**\n预计2026年和2027年的利率中位数上调至3.625%，意味着未来一年半都不会降息。18位委员中，5人可能支持加息，7-9人支持维持不变，4-6人支持降息。长期中性利率预估从3.125%上调至3.25%。\n\n**3/ 通胀数据在加速**\n5月核心PCE通胀预计环比上涨0.345%，同比达到3.426%，创2023年10月以来新高。PPI数据显示上游成本压力持续，制造业成本正在传导至消费品价格。\n\n**4/ 核心看点：新主席首秀**\n新任主席Warsh可能不会提交自己的利率预测（延续他过去对前瞻指引的批评）。在新闻发布会上，他可能会承认当前鹰派环境，但暗示中期可能放松——前提是伊朗战争等不确定性消退。他可能强调AI带来的生产率提升将推动去通胀。\n\n**\n\n[... middle omitted ...]\n\n-m or $3.426\\%$ y-o-y in May. Pipeline price pressures measured by PPI data continued to grow and point to an upside risk to the inflation outlook.\n\n## We expect the Fed to remain on hold and \n\n[... middle omitted ...]\n\ns available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities International, Inc., US. All rights reserved."
  },
  {
    "id": "R011",
    "title": "Bernstein：医疗保健政策的下一个拐点不在2028，而在2026中期选举",
    "digest": "[wechat_article.md]\n# Bernstein：医疗保健政策的下一个拐点不在2028，而在2026中期选举\n\n市场对医疗保健板块的关注，大多集中在2028年总统大选可能带来的政策摇摆上。但Bernstein这份最新研报提出了一个更紧迫的判断：真正影响资产定价的政策拐点，可能出现在2026年中期选举之后，而非四年后的大选周期。\n\n这份报告的核心洞察在于：如果民主党在2026年拿下众议院，医疗保健政策的方向将发生实质性转变——从削减Medicaid和 Marketplace注册，转向恢复覆盖率和扩大保障。而这一转变对Medicaid导向的保险公司和医院的影响，远比市场当前定价所反映的要深远。\n\n研报同时指出，尽管特朗普的民调支持率已降至第二任期内最低点，但众议院的席位争夺并非一边倒。Bernstein的分析框架显示，共和党在众议院仍有约200个席位的“地板”，这意味着民主党的席位增长可能不如历史典型的中期选举那样剧烈。正是这种“有限但关键”的转变，让政策博弈变得更加微妙——妥协的可能性上升，极端政策的概率下降。\n\n对于投资者而言，这不仅仅是一次政治预测。它直接关系到Medicaid管理式医疗组织的风险池变化、坏账趋势、以及垂直整合监管的走向。Bernstein的评级表已经透露出信号：Centene、Molina、Humana等安全网MCO均获得“跑赢大盘”评级，而医院股HCA仅为“与大盘持平”。\n\n以下是我们从这份报告中提炼出的五个关键层次，每一个都指向一个尚未被市场充分定价的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 民主党重掌众议院将扭转Medicaid削减，但医院的定价尚未反映这一预期\n\nBernstein的分析指出，民主党若拿下众议院，首要政策目标将是恢复Medicaid资金和ACA增强补贴。这意味着此前因共和党政策导致的\n\n[... middle omitted ...]\n\n这些关键变量的演变，并在市场定价偏差出现时做出更及时的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国医疗政策走向：2026中期选举影响解析\n\n📊 中期选举与医疗政策\n\n2026中期选举临近，民主党可能拿下众议院，参议院则充满变数。这对医疗板块意味着什么？\n\n1️⃣ 众议院或将“变天”\n根据最新民调，民主党大概率重掌众议院（预测市场给出82%概率），预计净增约15-20席。参议院更胶着——共和党微弱优势，但俄亥俄、得州等深红州可能翻蓝。\n\n2️⃣ 政策方向：聚焦Medicaid\n若民主党取胜，核心议题将是恢复Medicaid和ACA市场 enrollment。具体可能包括：\n- 推迟某些OBBBA条款实施（作为2027-28年妥协方案）\n- 降低Medicaid MCO的赔付率恶化风险\n- 缓解医院坏账压力\n\n3️⃣ 板块影响：谁受益？\n- ✅ 专注Medicaid的保险公司（CNC、MOH）已有所反映\n- ✅ 医院股尚未充分price in\n- ❌ Medicare Advantage和PBM改革可能性低（近年已出台重大政策）\n\n4️⃣ 2028年总统选举前瞻\n虽然为时尚早，但政策焦点已浮现：\n- 扩大覆盖、降低未参保率\n- 控制医疗可负担性\n- 垂直整合与AI监管\n“全民医保”虽不太可能落地，但民主党\n\n[... middle omitted ...]\n\nhe House, while the Senate remains a toss-up. What this means for policy - Democrats' main focus would likely be reversing declines in Medicaid and Marketplace enrollment. Policy outcomes shou\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R012",
    "title": "JPM：全球电动车市场的真正拐点不在销量增速，而在中国渗透率的结构性跃迁",
    "digest": "[wechat_article.md]\n# JPM：全球电动车市场的真正拐点不在销量增速，而在中国渗透率的结构性跃迁\n\n5月全球电动车销量数据出来了。环比增长9%，同比增长8%，看起来是一个温和复苏的信号。但JPM这份最新研报真正值得关注的点，不是总量数字，而是一个被多数人低估的结构性变化：中国BEV（纯电动车）渗透率在4月达到42%之后，5月稳稳守住了这一水平，同时总EV（含插混）渗透率攀升至63%，创下2025年8月以来的新高。\n\n这不是一个简单的季节性波动。在整体乘用车市场同比下降22%的背景下，BEV销量反而实现了5%的同比增长。这意味着电动车正在从一个“政策驱动的新兴市场”转变为一个“即使在宏观逆风中也能自主增长的成熟品类”。对于锂矿、电池材料、乃至整个汽车产业链的投资者而言，这个信号比任何短期销量预测都重要。\n\n报告同时揭示了一个更大的叙事：全球三大市场中，只有中国在完成真正的渗透率跃迁。欧盟虽然同比增长强劲（32%），但渗透率仍停留在24%的低位；而美国市场BEV渗透率连续五个月纹丝不动地停在6%。这三条线之间的分歧，正在重新定义全球锂需求的地理分布和定价逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国市场的核心变化不是销量数字，而是电动车正在变成“新燃油车”\n\nJPM的数据显示，5月中国BEV销量63.7万辆，环比增长10%，但同比增速仅为5%。单纯看这个数字，容易得出“增长放缓”的结论。但真正有价值的信息藏在一个对比中：在总乘用车销量同比下降22%的恶劣环境下，BEV销量逆势增长。这意味着电动车已经从“可选消费”变成了“刚需替代”。\n\n更关键的是渗透率结构。5月中国BEV渗透率42%，与4月持平。但总EV渗透率达到63%，这意味着每卖出三辆车，就有两辆是带插电的。这个数字在2025年5月仅为53%。一年之内，中国汽车市场的电\n\n[... middle omitted ...]\n\n这份报告的完整图表和原始数据，探讨其中的二阶影响和投资含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球电动车销量还在爬坡\n\n中国BEV渗透率42%\n\n欧盟靠补贴和低价车型冲到了32%\n\n5月全球电动车销量数据更新，几个关键点值得关注👇\n\n**1/ 整体销量回暖**\n全球BEV销量93.8万辆，环比+9%，同比+8%\n但年初至今仍比2025年同期低3%\n渗透率从4月23%→24%，缓慢爬升\n\n**2/ 中国是绝对主力**\n5月中国BEV销量63.7万辆，环比+10%\nBEV渗透率维持在42%高位\n如果算上插混，整体新能源渗透率高达63%\n这是2025年8月以来的最高水平\n\n**3/ 美国依旧低迷**\n5月BEV销量8.6万辆，环比+10%\n但年初至今同比仍下降25%\n渗透率持续卡在6%，基本没动\n\n**4/ 欧盟是亮点**\nEU-10地区BEV销量21.4万辆，环比+5%\n年初至今同比+32%，增速领跑全球\n渗透率从4月24%→32%，提升明显\n主要靠国家补贴和低价电动车放量\n\n**5/ 对锂的启示**\n储能市场持续强劲 + 供应端有滞后\n研报判断锂辉石价格有温和上行压力\n（这里是推测：锂需求端有支撑）\n\nEU是目前最值得关注的区域\n补贴驱动+平价车型普及\n渗透率正在加速追赶中国\n\n你们觉得美国什么时候能突\n\n[... middle omitted ...]\n\nn continued to stand at 6%. (4) EU-10 BEV sales increased 5% MoM to 214kt and remain up 32% YTD YoY; BEV penetration increased to 32% (from 24% in April). The EU remains the strongest region o\n\n[... middle omitted ...]\n\nthird-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 12 Jun 2026 11:07 AM AEST\n\nDisseminated 12 Jun 2026 11:07 AM AEST"
  },
  {
    "id": "R013",
    "title": "GS：全球资金正在重新定价“安全”，而非追逐风险",
    "digest": "[wechat_article.md]\n# GS：全球资金正在重新定价“安全”，而非追逐风险\n\n全球资金流向正在传递一个比表面数据更复杂的信号。截至6月10日当周，全球股票基金净流入310亿美元，固收基金净流入177亿美元，看起来是典型的risk-on格局。但真正值得关注的不是总量，而是结构：资金正在同时涌入美国科技股和短期债券，却在撤出中国A股和欧洲股票。这不是简单的“风险偏好回升”，而是全球投资者在重新定义什么才是当前环境下真正的“安全资产”。\n\n这份GS最新发布的资金流向周报，揭示了一个正在发生的资产再定价过程。它告诉我们，市场并非在无差别地追逐收益，而是在有选择性地为确定性支付溢价。对于产业决策者和资产配置者而言，理解这个结构比盯着大盘涨跌重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国科技股的单向吸金正在重塑全球权益市场的定价逻辑\n\n当周全球股票基金净流入310亿美元，连续第二周保持高位。但拆开来看，驱动力量几乎完全来自美国市场。欧洲股票基金持续净流出，新兴市场内部也出现显著分化：台湾和韩国股票基金是EM净流入的主要来源，而全球EM基准基金和中国大陆股票基金则录得净流出。\n\n这意味着什么？全球投资者的权益配置正在向“美国科技叙事”集中，而这一叙事正在与地缘政治风险、供应链重构等议题脱钩。台湾和韩国的资金流入并非简单的EM轮动，而是全球科技产业链资金流向的延伸——它们是美国科技投资的“卫星市场”。\n\n对于中国企业而言，这种资金结构意味着：即便整体EM资金面改善，中国大陆股票仍然面临结构性流出压力。这不是周期性问题，而是全球资本重新评估中国市场风险溢价的结果。报告显示，中国大陆股票基金的资金流出在当周仍在持续，且来自境外投资者的流出尤为明显。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2.\n\n[... middle omitted ...]\n\n知识星球和微信群里开始了对这些问题的拆解，欢迎继续加入交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球资金正在流向哪里？📊\n\n资金持续涌入这些市场\n\n截至6月10日当周，全球资金流向出现几个明显信号：\n\n1️⃣ 股票基金净流入310亿美元，比前一周的230亿继续扩大。美国依然是资金首选，但欧洲基金持续流出。新兴市场内部出现分化：台湾和韩国吸引资金，中国内地和全球新兴市场基准基金则遭遇流出。\n\n2️⃣ 行业层面，科技基金是最大赢家，消费品基金继续失血。工业、基建类基金年初至今累计流入最多，能源和科技紧随其后。\n\n3️⃣ 债券基金全面获支撑，短期债和通胀保护债尤其受欢迎。新兴市场硬通货债券基金出现净流出，货币基金规模小幅缩减。\n\n4️⃣ 匈牙利债券流入显著增加，年初至今趋势明显。研报观点认为，匈牙利经济政策转向（包括欧元采用前景）将推动其收益率向欧元区收敛，福林存在进一步升值空间。\n\n5️⃣ 跨境外汇方面，美元和韩元需求最强，印度卢比、巴西雷亚尔和人民币流出最多。\n\n从区域累计数据看，韩国、巴西、台湾是今年资金流入最多的市场，而中国内地和印度流出明显。\n\n你关注的市场在哪里？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\nWEEKLY FUND FLOWS\n\n# Convergence \n\n[... middle omitted ...]\n\ngest net inflows while consumer goods funds saw continued net outflows.  \n- Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond fun\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "JPM：2026世界杯的真正价值不在门票，而在北美服务生态的定价权重估",
    "digest": "[wechat_article.md]\n# JPM：2026世界杯的真正价值不在门票，而在北美服务生态的定价权重估\n\n2026年世界杯将于2026年6月开赛，距现在正好一年。对于全球资本市场，这通常被归类为“事件驱动型主题”——赛事临近时炒作一波，结束后迅速退潮。但JPM最新发布的专题研报提出了一个值得严肃对待的判断：**本届世界杯的独特性在于，它是历史上第一次由北美三个经济体联合主办、赛事规模从32队扩至48队、104场比赛覆盖16座城市的超级事件，其经济影响远非“一次性消费脉冲”所能概括。**\n\n这份报告的真正洞察，不在于预测世界杯期间美国GDP将增加172亿美元，而在于它揭示了北美服务生态（从住宿、出行到数字广告）正在经历一场结构性压力测试。市场目前的定价远远低估了这种压力测试对相关行业估值中枢的长期含义。\n\n以下是我们对这份报告的拆解与延伸。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这届世界杯的规模本身，就是一个被低估的结构性变量\n\nJPM在报告中反复强调一个数字：500万张门票申请对应约700万张可售座位，超额认购倍数约为70倍。这个数字本身是惊人的，但更重要的是它背后的两层含义。\n\n第一，赛事扩编至48队、104场比赛，意味着比赛日从传统的约30天拉长到近40天。这对于主办城市而言，不是一周的狂欢，而是一个完整的高峰运营季。第二，78场比赛和11个主办城市集中在美国，且大量比赛位于所谓的“sprawl/drive markets”——即需要驾车跨城出行的市场。这意味着，世界杯的消费辐射不是点状的，而是网络状的。\n\n报告引用住宿研究团队的估算：世界杯将为美国酒店业带来9.1亿美元的增量客房收入，对应30-40个基点的RevPAR增长，主办城市在2026年6-7月的RevPAR将提升7-25%。这个数字看起来不大，但需要放在一个背景下来理\n\n[... middle omitted ...]\n\n行行业有深入研究的群友一起探讨世界杯主题的交易逻辑和风险点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026世界杯，哪些公司会受益？\n\n**世界杯受益清单**\n\n**从出行到消费，一张图看懂**\n\n2026年世界杯首次由美加墨三国联合举办，赛事规模史无前例——48支球队、104场比赛，预计吸引650万现场观众。投行研报指出，这将带来约140亿美元赛事相关支出，仅美国就能拉动172亿美元GDP。\n\n哪些赛道最值得关注？研报梳理了6个核心方向：\n\n**1/ 住宿与出行**\n- 酒店业预计新增9.1亿美元收入，主办城市RevPAR（每间可售房收入）在2026年6-7月可能上涨7-25%\n- 网约车和外卖平台预计分别增加3.77亿和0.73亿美元订单额\n- 租车公司受益于60%比赛分布在“自驾友好型”城市\n\n**2/ 票务与娱乐**\n- 二手票务平台是直接受益者——700万张门票收到5亿份申请，超额认购70倍\n- 体育博彩、游戏类公司也被列为高弹性标的\n\n**3/ 广告与媒体**\n- 全球广告支出预计增加50亿美元，其中40亿流向数字渠道（占比73%）\n- 媒体平台、流媒体、社交平台将分到最大蛋糕\n\n**4/ 消费品牌**\n- 饮料、食品、运动服饰是传统赢家\n- 赞助商组合在过往两届世界杯期间表现持续跑赢大盘\n\n*\n\n[... middle omitted ...]\n\n will be in the United States. Much of this is driven by the expansion of the tournament from 32 to 48 teams and from 64 to 104 matches. The tournament expansion is expected to drive higher fa\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 10 Jun 2026 11:56 PM EDT\n\nDisseminated 11 Jun 2026 12:15 AM EDT"
  },
  {
    "id": "R015",
    "title": "GS：欧洲石油巨头隐含的长期油价远低于市场共识，这才是真正的价值锚点",
    "digest": "[wechat_article.md]\n# GS：欧洲石油巨头隐含的长期油价远低于市场共识，这才是真正的价值锚点\n\n当市场目光聚焦于美伊和谈可能带来的霍尔木兹海峡重新开放，并因此推动布伦特油价下跌时，一个更深层的定价问题被忽略了：欧洲上市石油巨头（EU Big Oils）的当前股价，究竟在反映什么样的长期油价预期？GS最新发布的研报给出了一个令人意外的答案——这些公司的估值所隐含的长期油价，远低于当前市场共识和远期期货所暗示的水平。这并非一个简单的“便宜还是贵”的判断，而是指向了一个关于资产定价、股东回报和地缘政治风险重新定价的核心分歧。\n\n这份报告的核心判断是：欧洲石油巨头的估值已经消化了显著低于市场预期的长期油价，这为投资者提供了一个不对称的风险收益窗口。但前提是，投资者需要理解这种“隐含定价”背后的结构性假设，并识别出哪些公司能够在低油价环境中依然保持强劲的现金流和股东回报能力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场定价的长期油价仅为每桶60美元，远低于共识与远期\n\nGS采用了一个简洁但有力的框架：求解欧洲石油巨头在实现8%的自由现金流收益率（FCF yield）时，所对应的2026-2029年平均布伦特油价。结果令人瞩目——这一隐含价格仅为每桶60美元。这与此期间彭博共识预期的每桶78美元、GS自己的预测每桶77美元，以及远期期货价格每桶79美元相比，存在约20美元的显著折价。\n\n换句话说，市场对欧洲石油公司的定价，并非建立在对当前高油价持续性的乐观假设上，而是已经提前、且相当充分地计入了油价回归到接近页岩油边际成本的水平。这意味着，如果未来油价能够维持在每桶70美元甚至更高的水平，这些公司的实际现金流和股东回报将显著高于当前市场所预期的。\n\n这个发现的核心含义在于：投资者对欧洲石油股的“价值陷阱”担忧，可能恰恰是误解了市场已经完\n\n[... middle omitted ...]\n\n完全展开的图表和假设，看看哪些公司的结构性优势被市场低估了。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价60美元，欧洲油气公司还值不值？\n\n**隐含油价60美元**\n\n**欧洲油气估值里藏了什么信号**\n\n最近Brent受美伊和谈预期影响走弱，某外资投行做了一组压力测试：如果油价在50-90美元/桶区间波动，欧洲油气公司的估值会怎样？\n\n1️⃣ **当前估值隐含的长期油价只有60美元**\n- 以8%自由现金流收益率倒推，2026-2029年隐含Brent均价约60美元\n- 而Bloomberg共识/该行预测/远期期货同期均值在77-79美元\n- 市场定价比共识低了一大截，说明估值已经消化了悲观预期\n\n2️⃣ **不同油价下的现金流回报**\n- 2026年自由现金流收益率：90美元时13.4% → 70美元时9.9% → 50美元时6.4%\n- 股东总回报率（分红+回购）：90美元时8.0% → 70美元时7.3% → 50美元时5.5%\n- 即使在70美元的中性情景，回报率也接近7%，不算差\n\n3️⃣ **该行看好的三家**\n- BP：财务去杠杆空间大，交易利润有弹性\n- Repsol：受益于欧盟航空燃料市场偏紧，美洲产量增长不错\n- Galp：按项目分析，油气储量寿命最长\n\n**一点思考**：市场现在定价\n\n[... middle omitted ...]\n\nsee little upside to Bloomberg consensus earnings as it is currently pricing 2026E Brent at \\$91/bl (vs GSe of \\$87/bl) and 2030E Brent at \\$70/bl on consensus (vs GSe of \\$75/bl).\n\nUnder a wi\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "GS：日本市场真正值得关注的不是AI反弹，而是股东会投票率背后的治理信号",
    "digest": "[wechat_article.md]\n# GS：日本市场真正值得关注的不是AI反弹，而是股东会投票率背后的治理信号\n\n每年六月的最后一周，日本迎来股东大会的绝对高峰期。根据GS最新发布的日本市场周报，6月25日和26日两天，将有超过1100家3月决算期的公司集中召开年度股东大会。这一现象本身并不新鲜——日本企业长期习惯于在同一时间窗口完成股东大会，以便于统一应对机构投资者的集中质询。\n\n但这份报告真正值得关注的判断，并不是会议日程本身，而是一个被当前市场情绪掩盖的结构性信号：**那些在去年股东大会上获得低赞成票的公司，正在系统性地改善治理表现，而这种改善正在转化为可量化的超额收益。**\n\nGS筛选出的12家2025年AGM赞成票率处于最低十分位的公司中，已有10家在今年的投票中获得了明显的赞成率提升。更关键的是，这一组合在去年股东大会到今年伊朗冲突爆发前，跑赢TOPIX指数13个百分点。尽管此后因市场风格转向AI主题而暂时落后，但GS认为，低赞成票率仍然是预测企业未来股东友好行为的最强先行指标。\n\n这一判断的隐含含义是：当前市场对日本股市的定价，可能过度集中于AI和科技主题的短期叙事，而低估了治理改善这一慢变量对资产定价的长期重塑力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 低AGM赞成票率是一个被低估的“治理改善催化剂”，而非简单的负面信号\n\n许多投资者的直觉是，一家公司在股东大会上获得低赞成票，说明管理层与股东之间存在矛盾，是负面信号。但GS的研究提供了相反的实证：**低赞成票率恰恰是推动企业在下一年度采取股东友好行动的最强动力。**\n\n逻辑链条并不复杂。日本交易所集团（JPX）和机构投资者对治理透明度的要求逐年提高。当一家公司的管理层在股东大会上获得低于80%甚至70%的赞成票时，这不仅是面子问题，更会触发机构投资者的持续关注和跟进。管理\n\n[... middle omitted ...]\n\n后一周股东大会的投票结果，看看哪些公司正在释放新的治理信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本股东大会季：哪些公司正在“讨好”股东？\n\n股东会季观察\n\n又到一年日本股东大会集中期。6月23-26日是最高峰，单日最多635家公司开会。\n\n翻完某外资投行最新研报，几个有意思的发现：\n\n**1/ 低赞成率公司，反而更值得关注**\n\n去年AGM赞成率垫底的公司，今年有10/12家出现明显改善。而且从去年股东大会到今年4月，这批公司相对TOPIX跑赢13个百分点。研报认为，低赞成率是预测公司后续改善股东回报行为的重要信号。\n\n**2/ “优待+分红”组合，在市场回调时很抗跌**\n\n6月3日以来，同时提供股东优待（yuutai）和分红的股票，相对既无优待也无分红的股票，跑赢12个百分点。食品饮料和零售板块本周逆势上涨3%，而系统集成、苹果供应链等跌幅达6-7%。\n\n**3/ 谁在买、谁在卖？**\n\n6月第一周数据：国内机构净买入2140亿日元，个人投资者净买入2980亿日元，而外资净卖出650亿日元。\n\n**一点观察**：当市场情绪转弱时，有实际股东回馈机制的公司，似乎更容易获得资金青睐。这轮AI驱动行情中表现落后的低赞成率公司，反而可能是接下来治理改善的潜在受益者。\n\n欢迎一起讨论，你们关注的公司今年股东大\n\n[... middle omitted ...]\n\nthat were in the bottom decile for AGM approval ratings during the CY2025 AGM season. So far, 10 out of 12 companies in the screen saw improvements in their approval rating this year (Exhibit \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "Bernstein：邮轮市场的真正稀缺资产，不是船，是品牌定位的不可替代性",
    "digest": "[wechat_article.md]\n# Bernstein：邮轮市场的真正稀缺资产，不是船，是品牌定位的不可替代性\n\n当大多数投资者还在用“运力增长”和“客单价”来理解邮轮行业时，一份来自Bernstein的深度报告提出了一个更值得追问的问题：在一个供给和需求都在结构性扩张的市场里，什么才是真正不可复制的护城河？\n\n答案不是船队规模，不是航线数量，甚至不是豪华程度。答案是一种近乎反直觉的品牌定位——在奢华邮轮领域，真正跑赢的不是最贵的那个，而是最“不一样”的那个。\n\n这份研报聚焦于一个长期被主流投资者忽视的细分赛道：奢华邮轮。Bernstein的判断很明确：奢华邮轮正站在邮轮行业最强的结构性需求风口上，而在这个细分市场中，只有一家公司具备“纯正标的”属性——Viking。但真正值得深思的，不是Viking的估值，而是它凭什么能在定价上跑赢船型规模相似的竞争对手，以及这种定价权的可持续性。\n\n这不是一篇简单的“推荐买入”报告。它实际上在回答一个更深层的问题：当消费升级的故事不再新鲜，当“有钱人变多”变成共识，企业之间真正的差距，来自对“什么是奢华”的重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 奢华邮轮的需求动力，比主流邮轮更陡峭、更确定\n\nBernstein在报告中明确指出，奢华邮轮面临的两个核心需求驱动因素，在可预见的未来都不会逆转。\n\n第一个因素是人口结构。邮轮消费本身就有明显的年龄倾向，而奢华邮轮尤甚——平均乘客年龄达到63岁。这一群体在美国人口中的占比正在持续扩大，更重要的是，他们的财富集中度也在上升。目前，美国55岁以上人群持有近75%的家庭财富。与此同时，美国收入分布的两极分化进一步加剧，收入最高四分位群体的收入增长最快，休闲时间也最多。这个群体是奢华旅游消费的核心客群。\n\n第二个因素来自供给端。奢华酒店的新增供应正在放缓。\n\n[... middle omitted ...]\n\n群内分享完整的研报原文、关键图表，以及基于报告的进一步推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n豪华邮轮赛道，谁在悄悄领跑？\n\n**豪华邮轮的隐藏赢家**\n\n**最强劲的风口在高端邮轮**\n\n某外资投行最新研报深度拆解了豪华邮轮市场，几个核心逻辑值得关注👇\n\n1️⃣ **需求端有两大引擎**\n- 美国55岁以上人群正在变富，占全美家庭财富近75%，且休闲时间更多\n- 豪华酒店供给增速放缓，高端邮轮正好承接溢出需求\n\n2️⃣ **豪华邮轮不是铁板一块**\n价格从每晚500美元到5000美元+不等\n关键变量：船的大小。小船（100舱位）价格是大船（1000舱位）的10倍\n但维京邮轮打破了这个规律——同样大小的船，它能卖出2倍价格\n\n3️⃣ **维京的差异化打法**\n定位“思考者”，不卖奢华感，卖文化沉浸\n船上请历史学家、设图书馆、安排文化讲座\n明确“不做什么”：没有赌场、没有儿童、没有拍卖、没有白手套服务\n2025年回头客率达到54%，客户评分行业领先\n\n4️⃣ **供给端格局**\n维京占豪华邮轮新增运力的50%以上\n新船成本控制出色，每舱位成本与主流品牌相当，但收益率更高\n\n豪华邮轮不是追求“更大更炫”，而是精准抓住一个细分人群的需求。这个思路，放在很多行业都值得思考。\n\n欢迎一起讨论邮轮行业的趋势走向～\n\n[... middle omitted ...]\n\n industry is a constructive one, the Luxury segment faces the most pronounced demographic and structural demand tailwinds in cruise. An increasingly wealthy, higher-earning and older consumer \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R018",
    "title": "Bernstein：AI在放射科的落地，真正被低估的不是技术，而是结构性供需缺口",
    "digest": "[wechat_article.md]\n# Bernstein：AI在放射科的落地，真正被低估的不是技术，而是结构性供需缺口\n\n医疗AI的故事已经讲了十年。但Bernstein这份最新研报揭示了一个被市场忽视的关键信号：放射科AI的渗透正在从一个“可选项”转变为一个“必需品”。这不是因为技术突然成熟了，而是因为人口结构和劳动力市场的双重挤压，已经让医疗系统别无选择。\n\n这份报告最值得关注的判断是：AI在医学影像领域的价值，不是来自于它能做什么，而是来自于它不得不做什么。老龄化叠加放射科医生供给缺口，正在制造一个结构性需求缺口，而AI是目前唯一能够在不显著增加人力成本的前提下填补这个缺口的方案。\n\nBernstein的分析师团队指出，美国65岁以上人口将以每年约3%的速度增长至2030年，而放射科医生的供给缺口将在2034年达到10%。这两条线的交叉点，就是AI医学影像从“锦上添花”到“雪中送炭”的转折点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 放射科的结构性压力正在从偶发变成永久性\n\nCOVID-19疫情是一个关键的催化剂，但它不是问题的根源。疫情只是将原本缓慢积累的压力一次性释放了出来。英国NHS的数据提供了一个清晰的参照：等待超过六周进行CT或MRI检查的患者数量，从疫情前的约8000人飙升至2020年的约80000人，而到了2025年，这个数字仍然维持在约75000人的高位。\n\n这意味着什么？这意味着疫情后的“恢复正常”并没有真正恢复。医疗系统在应对积压需求时，发现常规的扩招医生、增加设备投入已经无法跟上需求的增长速度。这不是一个短期波动，而是一个结构性失衡的持续表现。\n\nBernstein的报告引用McKinsey的数据指出，AI能够释放医疗设备准备人员高达48%的工作时间。这个数字放在放射科的具体场景中，意味着同样的设备和人员，可以在\n\n[... middle omitted ...]\n\n争终局”“中国市场与美国市场的差异”等未解问题展开深入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI让放射科医生效率翻倍？真的假的\n\n📊 放射科AI，正在悄悄改变医疗\n\n1/ 放射科是医疗AI最成熟的赛道\n影像识别天然适合AI——大量结构化的图像数据，重复性高的工作流。AI已经嵌入到图像采集、流程协调、报告生成等环节，目标是让医生从“看图”变成“分析”。\n\n2/ 为什么医院现在开始认真买AI？\n疫情是转折点。2020年后，放射科积压了大量患者。以NHS为例，等CT/MRI超过6周的患者从疫情前8000人飙到8万，2025年仍高达7.5万。医院发现：光招人不够，效率才是解药。\n\n3/ 老龄化让需求只增不减\n美国65岁以上人口2030年前每年增长约3%，欧洲约2%。老年人需要更多影像检查，但放射科医生供给跟不上——美国预计2034年缺口达10%。AI成了“增容”的关键工具。\n\n4/ AI能释放多少人力？\nMcKinsey数据：AI可释放医疗设备准备员48%的时间、药剂师23%的时间。对放射科来说，自动排序、快速扫描、辅助报告——这些不是锦上添花，是刚需。\n\n5/ 硅谷的解法\nAidoc（估值5.2亿美元）做CT/X光AI分析，嵌入医院系统，自动识别急症并协调团队。Viz.ai（估值12亿美元）专注神经和心血\n\n[... middle omitted ...]\n\nin.smith@bernsteinsg.com\n\nMiki Sogi, Ph.D. +81 3 6777 6991 miki.sogi@bernsteinsg.com\n\nLance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com\n\nJeffrey Walch +1 917 344 8613 jeffrey.walch@ber\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R019",
    "title": "摩根斯坦利：市场低估的不是消费复苏，而是亚洲工业超级周期对中国出口的锚定效应",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是消费复苏，而是亚洲工业超级周期对中国出口的锚定效应\n\n这份来自摩根斯坦利亚洲团队的投资者演示，标题直接点明了当前中国经济最关键的结构性变量——AI与能源超级周期。但真正值得反复咀嚼的判断，并不在标题本身，而在于报告揭示的一个核心张力：中国经济正在经历一场“双速”分化，而出口驱动的增长韧性，远比市场普遍认知的更持久、更结构化。\n\n市场目前对2026-2027年中国经济的讨论，仍然高度集中在房地产何时触底、消费何时回暖、通缩压力何时缓解。这些固然是重要变量，但摩根斯坦利的分析框架提示我们：真正被低估的，是亚洲工业超级周期对中国出口竞争力的重塑。这不是一个短期库存回补的故事，而是一个可能持续到2030年的结构性再定价过程。\n\n报告的核心主张可以概括为一句话：中国正在借助AI与能源相关的资本开支浪潮，以及自身在全球制造业中已经占据的压倒性份额，将出口市场占有率从当前的14.8%推升至2030年的16.5%，这一过程将有效对冲内需的疲弱，使GDP增速在4.7%-5.0%的区间内保持稳定。但这一判断成立的前提，以及它背后隐藏的风险，需要逐层拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 亚洲工业超级周期并非AI主题的衍生品，而是一次广泛且独立的产能扩张\n\n摩根斯坦利在报告中明确指出，亚洲正在经历自2000年代中期以来最强的工业周期。这一判断的关键证据，并非仅来自半导体或AI相关产品的出口数据。报告展示了一张极具说服力的图表：自2025年10月以来，亚洲剔除半导体和燃料的非科技出口出现了急剧且广泛的增长，涵盖中间品、资本品、消费品乃至乘用车等几乎所有产品类别。\n\n这意味着什么？这轮工业周期的驱动力不是单一的AI军备竞赛，而是亚洲制造业整体竞争力的提升和全球供应链重构的深化。中国作为亚洲制造业\n\n[... middle omitted ...]\n\n份额提升的边界在哪里”这一核心问题，进行更深度的拆解和推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国经济的“双速”新格局\n\nAI与能源超级周期下的出口驱动\n\n1️⃣ 出口成为增长主力\n中国GDP增速预计2025-2027年维持在4.7-5.0%，净出口贡献从2023年的-0.5%跳升至2025年的1.6%。这不是短期波动，而是AI和能源资本支出超级周期带来的结构性变化。\n\n2️⃣ 亚洲工业超级周期\n亚洲正进入2000年代中期以来最强的工业周期，非科技出口自2025年10月起全面回升——中间品、资本品、消费品全线增长。中国在全球制造业增加值中的占比已从2017年的26%升至27%，部分细分领域（如木材制品）从21%跃至38%。\n\n3️⃣ 出口份额持续扩大\n预计中国全球出口市场份额将从2024年的14.8%升至2030年的16.5%，乐观情景下甚至可达18%。这不是守成，而是扩张。\n\n4️⃣ 内需为何跟不上？\n工业自动化程度提高，就业弹性下降——企业营收增长70%，就业仅增20%。AI扩散正加剧劳动力市场压力，青年失业、中产工资稳定性、蓝领服务岗位的结构性替代风险都在上升。\n\n5️⃣ 房地产仍在调整\n新开工面积持续下滑，房价面临下行压力。春节后销售反弹更多是积压需求释放，而非趋势逆转。对比国际经验，房价调整\n\n[... middle omitted ...]\n\n](images/2cd822fab0717e5b28c6dd4190f0558f66889108cc6744e23267b96c78f46ce4.jpg)\n\n<details>\n<summary>bar-line hybrid</summary>\n\nChina Real GDP Growth by Expenditure, %\n| Year | Net Exports (%) |\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R020",
    "title": "JPM：中国电力设备在美渗透的拐点比市场预期的更快到来",
    "digest": "[wechat_article.md]\n# JPM：中国电力设备在美渗透的拐点比市场预期的更快到来\n\n这份JPM本周发布的研报，来自分析师团队在上海参加数据中心展和智慧能源展后的现场调研笔记。其核心判断不是关于中国电力设备市场的整体景气度——这已经被充分定价——而是关于一个正在发生但尚未被市场完全消化的结构性变化：中国电气设备供应商正在以超出预期的速度渗透美国数据中心供应链。\n\n报告透露的信号是具体的、可验证的：部分中国企业的变压器交付周期是西方同行的四分之一到六分之一，美国数据中心客户已经开始实地考察中国工厂并下达订单，而更关键的是，这一轮渗透并非简单的价格战，而是建立在交期、定制化能力和逐步积累的认证基础之上。对于关注电力设备板块的投资者而言，真正需要回答的问题不是“中国设备能否进入美国”，而是“哪些企业能在这轮渗透中建立可持续的竞争优势，而不是仅仅享受一轮周期红利”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国电气设备供应链的瓶颈正在为中国供应商打开一扇以前紧闭的门\n\n研报中反复出现的核心事实是：美国电力设备市场的供需缺口正在为中国企业创造历史性的窗口期。一家输配电设备供应商的变压器交付周期为6至12个月，而西方同行需要2至3年。这不是微小的差距，这是决定数据中心能否按时上线的关键变量。\n\n更值得关注的是，这并非个例。JPM的渠道调研显示，中国供应商在高压/低压设备领域的渗透率正在上升，驱动因素正是供应紧张和交期优势。数据中心的电力设备需求具有高度的时间敏感性——项目延迟意味着算力无法按时交付，这对云服务提供商（CSP）和大型互联网公司而言是巨大的机会成本。因此，当西方供应商的交付周期拉长至两年以上时，中国供应商的6个月交期就变得具有压倒性的吸引力。\n\n但交期优势只是入场券。真正让这轮渗透不同于以往的是：美国客户正在主动评估中国供应商。报\n\n[... middle omitted ...]\n\n论，我们会在社群中分享完整的研报原文和更深入的财务模型拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国电力设备出海，正在加速\n\n中国电力设备出海提速\n\n美国数据中心订单比想象中更多\n\n最近去上海参加了两场行业展会（数据中心展+智慧能源光伏展），有几个有意思的发现👇\n\n1️⃣ 中国电力设备供应商在美国的渗透率超预期\n- 交期优势明显：变压器交付6-12个月 vs 海外同行2-3年\n- 利润空间更大：美国市场变压器毛利率可达30-40%+，国内仅~teens\n- 美国CSP（云服务商）今年已参观中国工厂并下了订单\n- 已进入美国市场的公司包括：伊戈尔、安科瑞、上海电气、山东泰开（民营）\n- 主要从数据中心切入，公用事业领域因认证门槛高，渗透还比较有限\n\n2️⃣ 固态变压器（SST）是800V直流架构下的新方向\n- 伊顿在中国发布了MV SST 2.0，10kV交流输入→800V直流输出，专为AI数据中心设计\n- 单系统容量2.5MW，效率98.5%，可用性>99.999%\n- 已有国内参考项目运行超1年，但大规模应用还在早期\n- 特锐德与伊顿合作开发全预制数据中心电源方案，自研高压SST计划2027年完成并网示范\n\n3️⃣ 行业对SST的采用时间点有分歧\n- 部分厂商认为AI机架密度提升后，800V DC/S\n\n[... middle omitted ...]\n\nVDC products, and while most have not yet commercialized these offerings, Eaton (ETN.US) has launched a medium-voltage SST for AI data centers in China and Southeast Asia. TGOOD also announced\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 06:17 PM HKT\n\nDisseminated 11 Jun 2026 06:17 PM HKT"
  },
  {
    "id": "R021",
    "title": "UBS：人形机器人供应链的“确定性”正在从概念走向订单，但市场仍低估了传统业务的反转弹性",
    "digest": "[wechat_article.md]\n# UBS：人形机器人供应链的“确定性”正在从概念走向订单，但市场仍低估了传统业务的反转弹性\n\n2026年6月10日，UBS在嘉兴举办了一场面向机构投资者的实地调研，走访了双环传动和荣泰电工两家公司，并与核心管理层进行了深度交流。这份调研纪要看似聚焦于两家零部件企业的季度经营更新，但其背后揭示了一个更深层的产业信号：中国汽车零部件供应链正在经历一轮“需求结构切换”的关键拐点。\n\n市场目前的关注点高度集中在人形机器人这一新兴赛道上。这当然重要。但UBS这份报告最有价值的判断，并非机器人业务本身，而是“传统NEV业务正在环比改善，而欧洲市场渗透率提升正在为这些企业提供新的增长动量”。换句话说，人形机器人的故事是估值弹性，而传统业务的复苏才是安全边际的基石。\n\n这份报告真正值得细读的地方在于：它提供了三家核心标的（科达利、双环传动、荣泰电工）在“新旧动能切换”这个时点上的微观证据。这不是一份宏观展望，而是一次带着订单和产能数据回来的实地验证。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 双环传动的NEV齿轮产能利用率突破90%，这是比机器人更重要的信号\n\n双环传动在交流中披露了一个关键数字：Q2 2026 NEV齿轮出货量环比显著增长，产能利用率已超过90%。在汽车零部件行业，产能利用率一旦突破85%-90%的临界点，就意味着固定成本摊薄进入加速区间，毛利率将出现非线性改善。\n\n这个数字的意义在于：它验证了UBS此前对国内NEV需求在二季度企稳回升的判断。过去几个季度，市场对NEV零部件企业的担忧主要集中在“价格战传导”和“产能过剩”上。双环传动90%以上的产能利用率，至少说明在齿轮这个细分领域，头部企业的产能消化能力远好于市场悲观假设。\n\n更值得关注的是，双环传动正在将齿轮技术外溢到AIDC发电机领域，核心客户包括\n\n[... middle omitted ...]\n\nBS报告中未完全展开的竞争格局分析，都是值得深入拆解的话题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新能源车链+人形机器人，两个方向都动了\n\n供应链新变量\n\n实地调研拆解：两条主线浮出水面\n\n刚跟完一场嘉兴工厂调研，信息量很大，直接说重点。\n\n某外资投行带队走访了两家汽车零部件公司——双环传动和荣泰股份，聊完发现新能源车业务环比改善明显，人形机器人这块也开始有实质进展了。\n\n1/ 新能源车业务回暖\n双环Q2新能源车齿轮出货环比大增，产能利用率已超90%。欧洲市场新能源车渗透率提升，给传统业务带来新增量。荣泰那边，欧洲新能源车销售强劲，加上特斯拉Semi和Cybercab的新订单，管理层对传统业务挺乐观。\n\n2/ 人形机器人进入量产前夜\n双环从去年开始就和北美某头部人形机器人公司联合研发新型减速器，进展顺利。荣泰更具体——灵巧手和身体用的精密螺丝已经拿到生产批准，6月订单就在爬坡，泰国工厂正在赶工，下半年量产。\n\n3/ 供应链公司都在往机器人方向转\n除了这两家，科达利也被点名，被认为是执行力最强的几家之一。齿轮、螺丝、减速器这些核心零部件，正在从车用走向机器人用，逻辑很顺。\n\n一个值得观察的趋势：传统汽车供应链公司凭借精密制造能力，正在打开第二增长曲线。研报未给出具体机器人业务收入预期，但方向已经很明确了。\n\n[... middle omitted ...]\n\nn European market likely to bring new growth momentum to the traditional businesses; 3) progress in the robotics business has been positive, the humanoid robotics of a leading North American h\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/a2fc8462a9562ede9663fde3dfd3695571c59fa461ed37211ebb4e867ce1c47e.jpg)"
  },
  {
    "id": "R022",
    "title": "GS：中国教育市场最值得跟踪的不是增长，而是结构分化的加速",
    "digest": "[wechat_article.md]\n# GS：中国教育市场最值得跟踪的不是增长，而是结构分化的加速\n\n当多数人还在关注教育行业“复苏”或“监管松动”时，一份来自GS的5月跟踪报告揭示了一个更值得深究的信号：市场的真实故事不是整体回暖，而是三条独立逻辑线正在同时加速——AI原生产品的用户争夺、硬件定价权的重新分配、以及海外需求的触底节奏。这三条线并不平行，它们的交汇点将决定未来12个月哪些公司能获得估值重评。\n\n这份5月26日更新的教育行业追踪报告，覆盖了AI教育应用、AI学习平板、移动端用户活跃度、非学科培训牌照、留学趋势以及东方甄选等多个维度。数据密度极高，但去掉噪音后，真正值得决策者关注的只有三个问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 字节跳动的“豆包爱学”正在改写AI教育应用的竞争规则\n\n豆包爱学的DAU同比增速在5月底加速至146%，这已经是它连续第二个月加速增长（4月为60%）。更重要的是，它在中国AI原生应用DAU排名中稳居第六位。考虑到它是一款垂直教育产品，这个排名的含金量远超表面数字。\n\n横向对比更说明问题。Gauth（好未来旗下出海AI产品）5月月流水约110万美元，同比增长24%，近12个月累计流水已达1320万美元。Gauth在全球AI教育应用中MAU排名第一，但它的增长斜率正在放缓——4月同比增速还有35%，5月降至24%。豆包爱学则在加速追赶。\n\n这两款产品的反差揭示了一个关键判断：AI教育应用的竞争已经从“谁先推出产品”进入“谁能持续获取用户注意力”的阶段。豆包爱学的DAU增长加速，叠加它在K-12学习工具类应用中的使用时长份额持续扩大（报告中有详细图表），说明字节跳动在教育场景的AI能力正在从“工具”向“习惯”迁移。而Gauth虽然流水仍在增长，但用户增长放缓意味着它可能需要更强的变现能力来维持估值逻辑。\n\n[... middle omitted ...]\n\n讨论，我们会在群里分享更多来自原始报告的分析框架和跟踪方法。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n豆包学习App日活涨了146%，AI学习机却卖不动了？\n\nAI学习机遇冷，豆包学习App却在狂飙\n\n最近翻了份某外资投行的教育行业跟踪报告，几个有意思的点分享给大家👇\n\n**1/ 豆包学习App爆发式增长**\n- 5月底日活同比+146%，稳居国内第6大AI原生应用\n- 时间份额持续提升，在K-12学习工具中表现亮眼\n- Gauth（AI解题）月流水约110万美元，同比+24%\n\n**2/ 学习机市场：量跌价稳**\n- 6大品牌线上GMV同比-35%（去年基数高）\n- TAL卖出约9.6万台，GMV约3.55亿元，同比-24%\n- 但均价同比降幅收窄至-4%，说明价格战趋缓\n\n**3/ 留学签证回暖**\n- 中国学生赴加拿大、澳洲、英国签证量1季度同比-9%\n- 相比去年-22%的降幅明显收窄，趋势向好\n\n**4/ 东方甄选：新平台撑起增长**\n- 5月抖音GMV约10亿元，同比+38%\n- 新平台GMV同比+246%，但原有3个平台同比-2%\n- 自有App月活同比+38%\n\n**5/ 非营利性学科辅导持续萎缩**\n- 5月MAU同比-26%，用户时长同比-33%\n- 教培监管效果持续显现\n\n最让我意外的是\n\n[... middle omitted ...]\n\nh maintained its leadership with monthly billings +24% yoy to c.US\\$1.1mn; ii) TAL: MAU growth for Xueersi.com decelerated to +10% yoy in May and Peiyou MAU maintained +19% yoy growth. On the \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R023",
    "title": "GS：资本开支的“结构性集中”正在重塑全球工业投资逻辑",
    "digest": "[wechat_article.md]\n# GS：资本开支的“结构性集中”正在重塑全球工业投资逻辑\n\n全球资本开支正在经历一场罕见的双重分化。一方面，总量数据持续向好，2026年预期增速高达13%，远超历史中位数2%的水平；另一方面，增长几乎完全由数据中心、半导体和电力公用事业三个领域驱动，这三个领域在总资本开支中的占比已从2022年的22%跃升至2026年的39%。这份GS最新发布的跨行业资本开支追踪报告（Capex Tracker）揭示了一个核心判断：市场当前低估的不是资本开支总量的韧性，而是增长结构高度集中所带来的供应链定价权转移和周期性风险错配。\n\n这份报告覆盖了约4000家公司、34个终端和子终端市场，追踪规模高达3.4万亿欧元的资本开支计划。其结论并非简单的“资本开支强劲”，而是指向一个更深刻的产业格局变化：少数几个结构性增长领域正在吸收越来越多的投资资源，而传统周期性行业正在被挤出。这种集中度达到历史极值，意味着投资者需要重新评估哪些环节真正享有议价能力，哪些资产可能面临需求透支后的回调风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本开支增长的结构性集中已达到历史极值，传统周期行业正被系统性挤出\n\n报告最值得关注的数字不是总量增速，而是增长分布的变化。2026年预期资本开支增速为13%，2027年预期为12%，均显著高于历史趋势。但拆解来看，增长贡献高度集中：数据中心2025-2029年复合增速约为35%，半导体约为23%，油气约为4%。与此同时，化学品和工程机械领域的资本开支预期分别下调了4.1和4.0个百分点，机场领域的复合增速甚至为-4%。\n\n这意味着，全球资本开支的增量几乎全部来自少数几个与AI、能源转型相关的领域。传统制造业、化工、建筑设备等行业的投资预期正在收缩。这种结构性集中并非短期现象——从2022年到2026年\n\n[... middle omitted ...]\n\n证节点、以及电力基础设施投资的潜在瓶颈——进行更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n科技和电网，撑起资本开支新周期\n\n投研观察\n\n资本开支正在向少数领域集中\n\n📊 最近某外资投行更新了他们的Capex Tracker，覆盖约4000家公司、34个终端市场，总资本开支高达3.4万亿欧元。几个关键变化值得关注：\n\n1️⃣ 中期预期继续上调\n2026年资本开支增速预计达13%，远高于历史中位数2%。2027年预期也从年初的8%上调至12%。驱动因素高度集中——科技和公用事业。\n\n2️⃣ 结构分化极其明显\n2025-2029年资本开支复合增速约9%，但内部差异巨大：\n- 数据中心：约35%（较上次更新上调6.5个百分点）\n- 半导体：约23%（上调6.8个百分点）\n- 油气：约4%（上调3.5个百分点）\n- 化工：下调4.1个百分点\n- 工程机械：下调4.0个百分点\n- 机场：复合增速为-4%\n\n3️⃣ 资金越来越“扎堆”\n数据中心、半导体、电网三大领域，2026年预计占全部资本开支的39%。而四年前这个比例只有22%。增长正在向少数结构性方向集中。\n\n4️⃣ 周期与结构的分化\n电信和消费等行业的capex-to-sales比率和产能利用率，目前都低于历史中位数。与科技和电网的结构性强势形成对比。\n\n[... middle omitted ...]\n\n366\n\nchristian.hinderaker@gs.com\n\nGS International\n\n## Meihan Yang\n\n+44 20 7051-6601\n\nmeihan.x.yang@gs.com\n\nGS International\n\n## Ope Otaniyi\n\n+44 20 7051 6955\n\nope.otaniyi@gs.com\n\nGS Internati\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R024",
    "title": "JPM：中国房地产并非整体回暖，而是一场K型分化下的资产再定价",
    "digest": "[wechat_article.md]\n# JPM：中国房地产并非整体回暖，而是一场K型分化下的资产再定价\n\n市场对“中国房地产复苏”的讨论，大多仍停留在总量层面：销售面积是否企稳、价格是否见底、政策是否继续加码。但JPM最新发布的实地调研报告，提供了一个远比总量数据更尖锐的视角——深圳和上海的地产市场正在经历一场清晰的“K型复苏”。\n\n所谓K型，即市场的不同层级正在走向截然不同的方向：高端住宅需求旺盛、去化迅速，入门级住房交易量有所恢复，而中间价位段则持续承压。这不是一个“复苏”的故事，而是一个“分化加剧、资产重新定价”的故事。\n\n这份报告的独特价值不在于其结论本身——分化是行业共识——而在于它通过实地调研、专家访谈和项目走访，给出了分化的具体形态、背后的驱动因素，以及对不同资产类别的含义。对于持有地产信用债、关注商业地产REIT化进程，或者正在思考中国资产配置框架的读者而言，这份报告提供了一组不可忽视的微观信号。\n\n以下是我们从报告中提炼出的六个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. K型分化的本质不是消费降级，而是财富效应与收入预期的结构性裂口\n\nJPM在深圳和上海走访了多个高端住宅项目，包括深圳宝安的观潮、上海徐汇的安澜上海以及杨浦的翠湖滨江。这些项目总价从2000万元至超过1亿元不等，但销售情况出奇一致：每批次开盘即售罄，买家多为30-40岁、从事科技、金融或AI/半导体行业的本地精英。报告引用销售经理的描述，有客户年收入达1亿元。\n\n与此同时，入门级住房（约300万元总价）的交易量在经历了过去五年的价格大幅下跌后有所恢复，但中间价位段（500万至1000万元）表现最弱。\n\n这意味着什么？\n\n这不仅仅是“有钱人更有钱”的老生常谈。报告揭示了一个更关键的结构性变化：高端市场的购买力来源于AI和机器人产业带来的正向财富效应，而大\n\n[... middle omitted ...]\n\n后的二阶影响，并与更多产业决策者一起，构建更完整的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n深圳楼市，K型复苏已来\n\nK型分化\n\n深圳/上海走了一圈，楼市正在上演K型复苏。\n\n高端豪宅卖得火，刚需回暖，中间段最惨。\n\n1️⃣ 深圳：两极分化明显\n- 二手房均价从2020高点跌了43%，但1月以来回涨2%，价格底已现\n- 5月交易量破万套，14个月新高\n- 豪宅（2000万+）靠科技新贵撑场，AI/机器人造富效应明显\n- 刚需（300万左右）回暖，中端（500-1000万）最弱\n- 南山、福田跑赢，其他区偏软\n- 保障房大规模入市（2026-30年推20-30万套），会压制大众市场\n\n2️⃣ 上海：同样剧本\n- 瑞安翠湖滨江、中海安澜上海，2000万到1亿+的项目几乎售罄\n- 买家30-40岁，本地或长三角为主\n- 恒隆广场66：一季度销售同比增10%+，韩台中东客增多\n\n3️⃣ IP商业：分化也明显\n- 高端商场稳，大众商场看位置和运营\n- 新城控股：低线城市消费更稳定，万达是主要对手\n- 龙湖天街：工作日午后客流不错，定位家庭+学生\n\n4️⃣ 选谁？\n- 龙湖：年到期债务60-70亿，手头现金170亿+每年50-100亿自由现金流，偿债能力扎实\n- 瑞安：上海豪宅复苏代表，到期债务在下降\n- 新城\n\n[... middle omitted ...]\n\nON '29s (9%), as they are a proxy for Shanghai's luxury market recovery with declining maturities. Seazen has managed to handle refinancing so far, but we stay Neutral on the '28s, as we find \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 11:43 PM HKT\n\nDisseminated 12 Jun 2026 07:30 AM HKT"
  },
  {
    "id": "R025",
    "title": "摩根斯坦利：市场对楼市“小阳春”的可持续性存在显著误判",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场对楼市“小阳春”的可持续性存在显著误判\n\n在经历了3-4月超预期的二手房成交回暖后，市场情绪一度转向乐观。然而，摩根斯坦利最新发布的6月高频数据显示，这一轮复苏的动能正在迅速衰减。截至6月10日，25城二手房实时成交同比增速已从4月的30%骤降至9%，低能级二线城市甚至出现同比负增长。这并非一次简单的季节性回调，而是政策脉冲效应消退与积压需求释放完毕后的结构性回落。市场真正需要重新定价的，不是需求何时反弹，而是供给侧的出清速度与房价下行压力将持续多久。\n\n为何这个判断在当前时点尤为重要？因为市场对“小阳春”的解读存在根本分歧。部分投资者将其视为周期拐点的前兆，而摩根斯坦利在5月发布的报告《An Inflection or Another False Start?》中已明确指出，3-4月的反弹更可能是积压需求的集中释放，而非基本面改善。如今6月数据进一步印证了这一判断，但股价自5月中旬以来已回调18%，而恒生指数同期仅下跌8%。这意味着，市场对房地产板块的风险定价仍不充分，尤其是在政策效果递减、二手房挂牌量未见显著收缩的背景下。\n\n这份报告的核心贡献在于，它通过高频数据拆解了25个城市的成交结构，揭示了三个关键信号：第一，政策放松的边际效用正在递减，且城市间分化加剧；第二，低能级城市的二手房市场已率先转弱，这可能是一线城市的前瞻指标；第三，即便在一线城市内部，成交量与价格走势也出现背离。这些信号合在一起指向一个判断：2026年下半年，二手房成交同比增速可能转负，而房价将在2026-2027年持续承压，仅极少数库存去化较好的核心城市可能出现温和回升。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政策脉冲效应正在快速衰减，低能级城市已率先“熄火”\n\n摩根斯坦利的数据显示，25城二手房实时成交同比增\n\n[... middle omitted ...]\n\n定期分享其他顶级投行的独家解读，以及基于这些报告的实战推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n二手房销量拐点，值得关注\n\n📊 二手房回暖在退潮\n\n25城二手房实时销售增速，从4月的+30%一路降到6月初的+9%。\n政策刺激的“脉冲效应”正在减弱，市场热度在降温。\n\n---\n\n1️⃣ 城市分化明显\n南昌、佛山、南通等低能级城市增速快速回落。\n天津、长沙、成都已转负。\n苏州、武汉还算坚挺，但广深佛增速也掉了10个百分点以上。\n\n2️⃣ 3季度可能更冷\n研报判断：如果政策效果和积压需求继续衰减，3季度二手房销售可能转负。\n背后是2026-2027年房价大概率继续承压，仅少数一线城市可能靠去库存走出小反弹。\n\n3️⃣ 关注这几个信号\n6-8月重点盯：\n· 成交量、挂牌量\n· 成交结构（是刚需还是改善）\n· 租金变化\n——这些才是判断市场是否真正触底的关键。\n\n---\n\n研报保持谨慎，认为行业风险收益比仍偏向下行。\n比起赌反弹，更值得关注的是那些基本面扎实、有分红、有长期价值的公司。\n\n欢迎一起讨论：你所在的城市，二手房最近是冷是热？\n\n#学习笔记\n\n[source_mineru.md]\n## China Property | Asia Pacific\n\n# More Signs of Secondary Ho\n\n[... middle omitted ...]\n\nour call for milder y-y in June, with potential to turn negative y-y in 3Q amid diminishing policy effects and pent-up demand...  \n… leading to a broadly soft m-m home price downtrend in 2026–\n\n[... middle omitted ...]\n\nperty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.30</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "摩根斯坦利：重卡销量超预期背后，真正的分化信号才刚刚开始",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：重卡销量超预期背后，真正的分化信号才刚刚开始\n\n2026年5月，中国重卡市场交出了一份超出预期的成绩单。中国汽车工业协会数据显示，当月重卡销售10.95万辆，同比增长23%，比行业研究机构CV World此前预测的10.3万辆高出约6个百分点。这份来自摩根斯坦利的月度数据追踪，表面上只是一次常规的行业销量更新，但如果我们把视线从单月数字上移开，转而审视前五个月的结构性变化，会发现一个更值得关注的判断正在浮现：市场对重卡行业的关注点，正在从“总量增长”转向“结构分化”，而后者对投资决策的含义，远比前者深刻。\n\n2026年前五个月，中国重卡累计销售54.43万辆，同比增长23%。这个增速本身并不令人震惊——它更多反映的是去年同期低基数下的恢复性增长。真正值得追问的问题是：谁在增长？谁在丢失份额？增长的动力来自哪里？这些问题的答案，将直接决定未来12至18个月重卡行业竞争格局的走向。\n\n这份报告的真正价值，不在于它告诉我们重卡卖了多少辆，而在于它揭示了行业内部正在发生的、投资者尚未充分定价的再分配过程。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 单月数据超预期，但真正值得关注的是市场份额的加速迁移\n\n5月重卡销量超预期，表面上是一个好消息。但摩根斯坦利的数据显示，超预期的背后是几家欢喜几家愁。\n\n中国重汽是5月最大的赢家。单月销售3.45万辆，同比增长41%，市场份额达到31.5%，同比提升3.9个百分点。这一表现背后有两个支撑：一是出口持续强劲，单月出口超过1.8万辆；二是在新能源重卡领域也处于领先位置。出口和新能源的双轮驱动，让中国重汽在行业整体复苏中跑出了加速度。\n\n对比之下，陕汽的表现令人担忧。5月销售约1.5万辆，同比下滑3%，市场份额13.7%，同比下降3.7个百分点。前五个月累计市场份\n\n[... middle omitted ...]\n\n们不提供投资建议，但我们提供可以用于形成独立判断的思考工具。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n重卡5月销量超预期，谁在领跑\n\n重卡销量超预期\n\n5月重卡卖了10.95万辆，同比涨23%，比机构预期的10.3万辆还多。虽然环比微降6%，但整体势头挺猛。\n\n1️⃣ 中国重汽是最大赢家\n- 单月销量3.45万辆，同比暴增41%\n- 市占率冲到31.5%，同比提升近4个百分点\n- 出口超1.8万辆+新能源重卡领先，双轮驱动\n\n2️⃣ 陕汽掉队明显\n- 5月销量同比下滑3%，市占率13.7%\n- 同比丢了3.7个百分点的份额\n- 前5月累计增速也只有14%，跑输行业\n\n3️⃣ 北汽福田和徐工小幅扩张\n- 福田5月同比增37%，市占率提升1.5ppt\n- 东风和解放表现平淡，东风甚至微降2%\n\n前5月行业累计销量54.4万辆，同比增23%。重汽累计市占率28.4%，同比微增0.3ppt，继续巩固龙头地位。\n\n重卡行业这轮增长，出口和新能源是两个关键变量。谁能在这两条线都跑通，谁就能抢到更多蛋糕。\n\n#学习笔记\n\n[source_mineru.md]\n## China Industrials | Asia Pacific\n\n# CAAM: HDT Sales Up 23% y-y in May 2026\n\nHDT \n\n[... middle omitted ...]\n\n+0.3ppt y-y); ShaanQi lagged behind with 14% y-y growth and a market share of 15.0% (-1.2ppt y-y). Beiqi Foton and XCMG expanded market share modestly.\n\nExhibit 1: China's HDT monthly sales vo\n\n[... middle omitted ...]\n\ny Industry (000157.SZ)</td><td>O (09/08/2025)</td><td>Rmb7.38</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R027",
    "title": "摩根斯坦利：香港地产市场真正被低估的不是住宅，而是写字楼的结构性拐点",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：香港地产市场真正被低估的不是住宅，而是写字楼的结构性拐点\n\n这份由摩根斯坦利发布的香港地产研报，表面上是一次常规的行业专家电话会纪要。但如果我们把它放在2026年这个时间节点来读，会发现它传递了一个比“住宅销售回暖”远更重要的信号：香港甲级写字楼市场正在经历一个由供给端驱动的结构性拐点，而市场情绪对此的定价远未充分。\n\n报告的核心价值不在于确认住宅市场“量价齐升”的已知事实，而在于揭示了两个被当前市场叙事忽略的关键变量：一是写字楼供给的未来路径已经锁定，二是学生公寓正在从边缘话题变成可规模化的新资产类别。理解这两个变量，才能理解摩根斯坦利为何在行业近期表现不佳、政策不确定性犹存的背景下，依然维持“Attractive”的行业评级。\n\n这不仅仅是一份关于地产周期的报告。它是一份关于“资产稀缺性如何被重新定价”的底层逻辑推演。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 住宅库存的快速去化，正在改变开发商的定价权结构\n\n报告中最直观的数据是：截至2026年第一季度，香港已完工住宅库存从2025年第一季度的28,000套峰值下降至20,000套，降幅达30%。与此同时，5月份住宅销售量同比增长44%，连续第15个月维持在5,000套以上。\n\n这两个数据放在一起，揭示的不仅仅是需求回暖。它意味着开发商正在从“去库存压力下的价格竞争”转向“库存可控后的定价主动”。当库存从28,000套降至20,000套，市场已经从买方市场重新回到了卖方市场的边缘。\n\n摩根斯坦利预测2026年全年住宅价格将上涨7%-10%，而截至目前的官方数据显示，年初至今已上涨约6%。如果这个预测成立，那么上半年6%的涨幅意味着下半年仍有约4%的上涨空间。但更值得关注的不是价格本身，而是这个价格走势背后的驱动因素从“政策刺激”切换到了“\n\n[... middle omitted ...]\n\n架，并与关注香港市场的同行一起，持续验证这些判断的边界条件。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港楼市正在悄悄换挡\n\n📊 数据回暖，情绪还没跟上\n\n刚看完某外资投行跟戴德梁行的最新专家交流，几个关键信号值得记下来：\n\n1️⃣ 住宅端：2026年5月成交量同比+44%，连续15个月维持在5000套以上。全年楼价预计涨7-10%（年初至今已涨6%）。库存从2025年一季度的2.8万套降到今年一季度的2万套，去化速度在加快。\n\n2️⃣ 写字楼：中环和西九龙是复苏主力，银行和金融需求撑场。甲级写字楼净吸纳量一季度仍有21.7万平方英尺为正。未来4年新增供应只有260万平方英尺，供应压力在减小。租金预计涨6-8%。\n\n3️⃣ 零售：前4个月零售额同比+11.3%，游客增长15%+人民币走强是双引擎。核心区商铺空置率接近零，租金在往上走。\n\n4️⃣ 学生公寓是新机会：香港八大学生与床位比3.4:1，床位只有非本地学生数的一半。这个缺口值得关注。\n\n⚠️ 不确定因素还在：新出境投资规则的影响、股市波动、利率走向——但到目前为止，还没有实质冲击。\n\n研报认为，当前估值相对资产净值折价50%，在历史低位区间。有明确项目推出、利润率改善、股东回报提升的公司更值得关注。\n\n📌 标签：#学习笔记 #研究笔记\n\n#学习笔记\n\n[... middle omitted ...]\n\n the recovery, helped by banking and finance demand and peaked-out supply.  \nMS view: Still constructive despite recent underperformance and concerns (rates and regulation). Valuation at a 50%\n\n[... middle omitted ...]\n\n>Wharf REIC (1997.HK)</td><td>U (12/13/2024)</td><td>HK$22.08</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R028",
    "title": "摩根斯坦利：韩国居民资产迁移到股票市场的趋势具有结构性，而非周期性",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：韩国居民资产迁移到股票市场的趋势具有结构性，而非周期性\n\n韩国正在经历一场深刻的居民资产负债表重构。过去二十五年间，韩国居民资产增长了91%，增速在主要经济体中位居前列。但真正值得关注的，不是总量增长，而是资产配置方向的根本性转变——从长达数十年的房地产与现金偏好，转向权益资产。摩根斯坦利在最新发布的研报中明确指出，这一转变具有可持续性，并将KOSPI的12个月目标从8500点上调至9000点，牛市情景上调至10500点。\n\n这份报告的核心判断是：韩国居民资产向权益市场的迁移，不是一次短期的交易性行为，而是一个由政策、人口结构与市场改革共同驱动的结构性拐点。对于关注亚太资产配置的投资者而言，这可能是未来三到五年最重要的宏观叙事之一。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 居民资产配置的结构性拐点已经到来，但市场尚未充分定价其持续性\n\n韩国居民长期以来将财富高度集中于房地产。截至2025年，主要住宅与其他房产合计占比超过70%，而股票、债券与基金的合计占比仅为3.6%。相比之下，近一半的金融资产仍以现金和存款形式持有。这种配置结构在过去二十年中几乎没有变化，直到2025年出现了显著拐点。\n\n数据显示，2025年韩国居民权益资产持有量同比增长48%，而此前十年的平均增速仅为7.4%。这一跳跃并非偶然。报告指出，房地产政策的持续收紧——包括信贷限制与对多套房持有的税收惩罚——正在系统性地降低房地产作为财富储存工具的吸引力。与此同时，股票市场的改革措施、企业治理改善以及股东回报提升，正在为权益资产创造更具吸引力的制度环境。\n\n这意味着，居民资金从房地产向权益市场的迁移，其驱动力不是短期的市场情绪，而是持续三到四年的政策方向。报告认为，这种“错失恐惧”已经从房地产转向股票，并且这种转变具有自我强化的\n\n[... middle omitted ...]\n\n以及，如果韩国央行的加息节奏快于预期，哪些板块的脆弱性最高？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国人正在大搬家：从房产到股票\n\n🇰🇷 韩国人资产大挪移\n\n过去一年，韩国散户的股票持仓暴涨48%，而过去十年平均增速只有7.4%。\n\n1️⃣ 为什么突然转向？\n- 房价高企+信贷收紧，买房变得不划算\n- 政府推资本市场改革，公司治理和分红改善\n- 6月将推出股息税改革和ISA账户升级\n- 房地产政策未来3-4年持续收紧，为资金流入股市提供结构性支撑\n\n2️⃣ 这波散户有啥不一样？\n- 2019年只有620万散户，2025年已达1450万，占成年人50%\n- 40岁以下投资者占43%，这群人消费意愿更强\n- 信息获取更便捷，AI让分析门槛降低\n- 积累海外投资经验，变得更“聪明”\n\n3️⃣ 对经济的影响\n- 股票财富效应→消费提振，预计KOSPI每涨1%，消费增速提升0.03-0.035%\n- 但风险也在：家庭债务高企+2026年7月可能加息，市场波动可能反噬消费\n\n4️⃣ 韩国vs日本\n韩国金融资产过去10年增长94%，日本只有31%。韩国人风险偏好更高，转型速度更快。\n\n研报上调KOSPI目标至9000点，看好科技、工业、医疗和百货板块。\n\n#学习笔记\n\n[source_mineru.md]\n## Kor\n\n[... middle omitted ...]\n\nredit policy contrasted by stock-market reform measures are behind the transition to an alternative wealth-building vehicle.  \nBoth positive and negative economic implications are at play: wea\n\n[... middle omitted ...]\n\nneither Equity Research Analysts/Strategists nor Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity or fixed income securities: Shreya Singh; Kathleen Oh.\n\n© 2026 MS"
  },
  {
    "id": "R029",
    "title": "JPM：电力设备板块的20-30%回调，不是风险出清，而是结构性机会的重新定价",
    "digest": "[wechat_article.md]\n# JPM：电力设备板块的20-30%回调，不是风险出清，而是结构性机会的重新定价\n\n过去一个季度，亚洲电力设备公司股价从四月高点普遍回撤20%至30%。如果只看价格信号，这很容易被解读为行业景气见顶的信号。但JPM最新发布的研报给出了一个相反的判断：这轮回调不是因为基本面恶化，而是市场在多重噪音中暂时失去了定价焦点。真正的结构性逻辑——美国电网资本开支的结构性增长、数据中心之外的重型电气化需求、以及中国电力设备在欧盟市场的低渗透率——并未被破坏，反而因为回调变得更清晰。\n\n这份报告最值得关注的核心判断是：回调后的估值水平，为那些订单结构偏向公用事业和电网、而非纯数据中心概念的公司，提供了更有吸引力的入场窗口。JPM特别点名了晓星重工（Hyosung Heavy）和威胜控股（Wasion Holdings），认为它们在当前估值下提供了明显的安全边际。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度回调的真正驱动力不是基本面，而是估值、资金流和催化剂真空三重叠加\n\nJPM的分析显示，这轮回调并非源于订单或盈利的实质性恶化。报告明确指出，一季度新订单数据创下历史新高后，市场面临的是一个“高基数下的真空期”——缺乏高频前瞻数据来确认订单增速能否持续。对于电力设备这类季度数据驱动的行业，这种信息真空很容易放大短期情绪波动。\n\n更关键的是资金流层面的结构性变化。JPM观察到，在韩国市场，部分对冲基金正在将电力设备股作为空头仓位，以融资买入存储器等AI主题股票。这种“做空电力设备、做多AI”的配对交易，使得电力设备板块的走势与美股科技股出现了一定程度的联动。这意味着，这轮回调中有相当一部分是资金流驱动的，而非基本面驱动的。\n\n对于中国电力设备公司，JPM认为资金流向AI主题板块是另一个拖累因素。数据显示，二季度中国AI\n\n[... middle omitted ...]\n\n拆解每个标的的风险收益特征，以及报告中未完全展开的关键假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n电力设备回调20-30%，该不该慌\n\n**回调之后，怎么看**\n\n某外资投行最新研报拆解：电力设备股从4月高点跌了20-30%，但估值已经回到更舒服的位置。\n\n**1/ 为什么跌？三个原因**\n\n- 市场担心数据中心连接延迟，影响明年订单增速\n- 韩国标的短期估值偏高，叠加空头资金转移（部分对冲基金用电力设备空头来对冲半导体多头）\n- 中国标的受欧盟关税担忧影响，资金流向AI板块\n\n**2/ 韩国标的：最抗跌的是它**\n\n研报认为，数据中心连接问题对重电公司影响最小。因为数据中心订单占比不到10%，主要订单来自电网和公用事业，这部分资本开支趋势不变。\n\n其中一家韩国重电公司，2028年预期PE约20倍，是韩国电力设备里最便宜的，且90%以上新订单来自美国电网，几乎不受数据中心问题影响。\n\n**3/ 中国标的：欧盟关税风险可能被高估**\n\n研报判断，欧盟对中国电力设备加征关税的可能性较低。原因：中国产品在欧盟市占率不到10%，对本地厂商（如西门子能源）构不成威胁。且欧盟能源转型需求大，本土产能有限，依然需要中国产品。\n\n**4/ 值得关注的方向**\n\n回调后，一些标的估值变得有吸引力。比如某中国电表龙头，1年远\n\n[... middle omitted ...]\n\nure 2). We see good value in Hyosung Heavy, as the stock trades at \\~20x 2028E P/E — the cheapest among Korean electricals (Figure 1) — and should be least impacted by any data center connecti\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 08:44 PM HKT\n\nDisseminated 11 Jun 2026 08:44 PM HKT"
  },
  {
    "id": "R030",
    "title": "摩根斯坦利：市场真正低估的不是厄尔尼诺本身，而是它对作物窗口的精准打击",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场真正低估的不是厄尔尼诺本身，而是它对作物窗口的精准打击\n\nNOAA刚刚确认厄尔尼诺已正式形成，并将“非常强”事件的概率从37%大幅上调至63%。这个数字正在快速从气象部门的概率表渗透到大宗商品交易员的头寸决策中。但摩根斯坦利这份最新研报的核心判断是：市场可能已经定价了“厄尔尼诺会发生”，但远未定价“它会在什么时间、什么地点、以什么强度击中最脆弱的作物窗口”。\n\n这不再是天气噪声，而是正在成形的投资信号。\n\n这份由拉丁美洲农业研究团队Julia Rizzo主导的报告，以罕见的紧迫感回应了投资者最关心的问题——如果今年出现超级厄尔尼诺，大宗商品、通胀、汇率、股票将面临怎样的重置？报告没有给出简单的“涨或跌”答案，而是构建了一个基于作物窗口、区域差异和时序节奏的分析框架。以下是我们从中提炼的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 概率的大幅跳升只是表层，真正的变量是“海洋-大气耦合”能否在夏季完成确认\n\n63%这个数字本身已经足够引人注目。但摩根斯坦利报告真正有价值的判断，在于它区分了“概率”和“确认”之间的关键差距。NOAA的最新数据确实指向了一个可能跻身历史前三的强厄尔尼诺事件——与1982/83、1997/98和2015/16年类似。但报告同时明确指出，官方指引仍然是概率加权的结果，尚未确认这是一次创纪录事件。\n\n关键在于“春季可预测性障碍”。当前模型的不确定性仍然较大，部分气象专家警告不要过早外推至“超级厄尔尼诺”情景。真正的确认信号需要观察：夏季海洋-大气耦合是否如期加强、Niño 3.4区域的升温是否持续超过+2.5°C阈值、以及不同模型在越过春季预测障碍后是否收敛。\n\n这意味着，市场目前定价的更多是“厄尔尼诺已来”这个事实，而不是“它可能有多强”。如果后续确认信号\n\n[... middle omitted ...]\n\n，更重要的是围绕这些关键假设展开持续的跟踪和验证。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n厄尔尼诺逼近：农产品影响全解析\n\n**厄尔尼诺来了**\n\n**概率飙升到63%，影响有多大？**\n\nNOAA刚刚确认，厄尔尼诺已经正式形成。最新数据显示，11月至1月期间出现极强厄尔尼诺的概率从37%跃升至63%，这可能是历史上最强的几次之一。市场开始认真思考：这会对农产品、通胀、汇率带来什么连锁反应？\n\n1️⃣ **糖是最敏感的品种**\n厄尔尼诺带来的干旱可能收紧亚洲供应，对糖价形成向上支撑。印度作为全球第二大产糖国，季风雨量面临下行风险。但短期巴西压榨仍在进行，供应充裕可能压制价格，真正的行情窗口在27/28作物年。\n\n2️⃣ **大豆和玉米要看时间窗口**\n巴西中西部和MATOPIBA产区面临干旱风险，但南里奥格兰德州和阿根廷反而可能受益。玉米的关键在于巴西二季玉米（占全国产量80%）的窗口期是否被压缩，以及美国夏季是否出现高温压力。\n\n3️⃣ **航运和渔业也受影响**\n巴拿马运河可能再次面临水位限制，推高运费成本。秘鲁鳀鱼捕捞因海水变暖受阻，鱼粉供应紧张会传导到养殖成本。\n\n4️⃣ **哪些公司受影响更明显？**\n糖价上涨环境对圣马蒂诺（SMTO3）偏利好；阿根廷降雨改善对Adecoagro（AGR\n\n[... middle omitted ...]\n\n... but some experts caution about extrapolating to “super El Niño” as confidence declines further out the curve.  \nAs we gain clarity on the scale of El Niño, we intend to work with our globa\n\n[... middle omitted ...]\n\nricola S.A. (SLCE3.SA)</td><td>E (09/17/2025)</td><td>R$14.89</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R031",
    "title": "UBS：酒店业真正的拐点不在RevPAR，而在定价策略的深层分化",
    "digest": "[wechat_article.md]\n# UBS：酒店业真正的拐点不在RevPAR，而在定价策略的深层分化\n\n过去一周，中国酒店行业的整体RevPAR同比增长了3%。单看这个数字，很容易得出“行业温和复苏”的结论。但如果拆开来看，UBS这份基于STR和Flight Master数据的周报揭示了一个更值得警惕的信号：行业内部的分化正在从“档次差异”演变为“定价逻辑的彻底分裂”——中端市场正在用降价换入住率，而高端市场则在靠供给侧约束和入境需求维持价格刚性。\n\n这不是一个简单的“复苏强弱”问题，而是一个结构性拐点：当一部分玩家选择主动降价以争夺存量客源时，整个行业的利润池分布和竞争规则正在被重写。市场真正需要关注的，不是RevPAR的均值，而是这个均值背后的定价权转移。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中端酒店正在用“降价换量”，但这条路径的可持续性存疑\n\nUBS数据显示，5月31日至6月6日这一周，中档和经济型酒店的RevPAR表现出现明显分化。中档酒店RevPAR同比下降3.4%，而经济型酒店同比上升2.8%。更关键的是，中档和上中档酒店的RevPAR改善，主要来自降低平均房价（ADR）来拉动入住率（OCC）。具体来看，中档ADR同比下降约2.5%，上中档ADR同比下降约2.5%，而入住率则分别提升了约-1.0和2.8个百分点。\n\n这意味着什么？中端酒店正在主动牺牲价格弹性来换取流量。这与一季度的情况形成了鲜明对比——当时行业更多是在价格相对稳定的情况下自然恢复。UBS报告明确指出，这标志着酒店集团正在“积极适应商务和休闲旅游市场的变化”。翻译过来就是：需求端的结构性疲软已经迫使中端酒店放弃价格纪律。\n\n但问题在于，这种策略能否持续？降价换量的本质是争夺存量市场，而存量市场的总盘子并没有显著扩大。当所有中端玩家都开始降价，最终的结果可能\n\n[... middle omitted ...]\n\n跨数据源的交叉验证，帮助你在信息碎片中找到真正有价值的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n酒店业悄悄变盘：中档降价抢客，高端靠外需撑\n\n酒店业最新周度数据解析\n\n最近一周（5/31-6/6）的酒店和机票数据出来了，几个有意思的信号值得关注👇\n\n**1️⃣ 整体RevPAR回暖，但增速放缓**\n大陆酒店RevPAR同比+3%，比前一周的+8%明显减速，不过仍然好于5月水平。价格（ADR）+1.7%，入住率（OCC）+0.7个百分点。\n\n**2️⃣ 中档酒店开始“以价换量”**\n中档RevPAR同比-3.4%，而中高档+2.6%。STR数据显示，这两个档次的回暖主要靠降价拉入住率——中档ADR降2.5%，中高档降2.5%，但入住率分别+2.8和-1.0个百分点。这跟Q1的策略明显不同，说明酒店集团正在主动调整，应对商旅和休闲需求的变化。\n\n**3️⃣ 高端&奢华酒店表现更稳**\n奢华/高端RevPAR分别+3.5%/+3.1%，好于有限服务酒店。原因：①高端供给增量相对少；②入境游增加拉动了需求。\n\n**4️⃣ 机票涨价，旅客变少**\n国内机票同比+23%，但旅客量同比-13%（前一周-7%），旅客收入增速也从18%放缓到7%。涨价确实压制了出行意愿。\n\n**我的观察**：酒店和航空呈现“分化复苏”—\n\n[... middle omitted ...]\n\n segment, upper-midscale/midscale/economy hotels RevPAR posted +2.6%/-3.4%/+2.8% YoY, respectively; weaker than last week, but better than those in May. Notably, STR data indicates that RevPAR\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/a07814770bf24aab83bd4cccd080e303a632525b88d515806736c42b2d20485e.jpg)"
  },
  {
    "id": "R032",
    "title": "摩根斯坦利：AI光互连的下一波赢家不在光模块，而在电路板",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI光互连的下一波赢家不在光模块，而在电路板\n\n当市场将全部注意力集中在GPU、网络芯片和光模块供应商时，一份来自摩根斯坦利的深度报告揭示了一个被低估的结构性机会：光收发器PCB。这并非简单的配套逻辑，而是一个正在经历“量价齐升”式重估的细分市场。\n\n这份报告的核心判断是：AI投资周期正进入新阶段，光互连的重要性正与算力本身持平。当超大规模云厂商将AI集群从数万GPU扩展至数十万GPU时，连接这些系统的光收发器数量正在指数级增长。但摩根斯坦利团队看到的，不仅是收发器数量的增长，更是每块电路板价值的跃迁。\n\n这意味着，传统意义上被视为“被动配套”的PCB制造商，正在成为AI基础设施支出的结构性受益者。而其中最值得关注的，并非当前市场份额最大的玩家，而是一家正在加速追赶的挑战者。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光收发器PCB市场正在以83%的复合增速成为全球PCB行业最强劲的增长引擎\n\n摩根斯坦利预测，全球AI光收发器PCB市场规模将从2025年的约6.2亿美元增长至2028年的约37.7亿美元，复合年增长率高达83%。这一增速远超同期光收发器出货量的60%复合增速，背后是“量”与“价”双重驱动。\n\n从绝对规模来看，这一市场正在快速逼近全球最大的HDI PCB需求方——苹果。报告估算，苹果每年对HDI PCB的需求约为30至35亿美元。而到2027年，AI光收发器PCB市场将成长至与苹果需求相当的规模，并在2028年超越它。\n\n这一对比的意义不仅在于市场体量。多年来，苹果一直是HDI PCB行业技术进步、产能投资和盈利能力的核心驱动力。而现在，AI光互连正在成为下一个主要需求引擎，这可能重塑PCB行业的竞争格局。\n\n根据Prismark的估算，全球HDI PCB市场约为162亿美元。到\n\n[... middle omitted ...]\n\n壁垒、估值差异的合理性，以及那些报告没有完全展开的二阶影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI光模块爆发，PCB是隐藏赢家\n\n光模块PCB，需求爆发\n\nAI集群从万级GPU扩展到百万级，光模块需求随之飙升。但容易被忽略的是，每块光模块里都有一块PCB，且技术门槛正快速提升。\n\n1️⃣ 量价齐升的双重逻辑\n📈 量：AI光模块出货量预计25-28年CAGR约60%\n📈 价：PCB规格从400G升级到1.6T，ASP从$10涨到$25\n💡 结果是：光模块PCB市场规模增速（83% CAGR）远超模块本身\n\n2️⃣ 技术升级推高壁垒\n400G→1.6T，PCB从10-12层HDI升级到14-16层mSAP\n材料从M6级CCL升级到M8级\n毛利率从20-30%跃升至40-50%+\n这意味只有具备mSAP能力的供应商才能吃到最大蛋糕\n\n3️⃣ 谁最受益？\n投行研报认为，臻鼎（ZDT）是最大赢家：\n- 800G市场份额从7.5%有望扩至28年约20%\n- 1.6T市场份额从5%有望扩至约25%\n- 原因是mSAP工艺壁垒高，而臻鼎有苹果供应链经验\n\n欣兴和深南也会受益，但臻鼎的增长弹性更大。\n\n4️⃣ 一个有趣的对比\n到28年，光模块PCB市场规模（~$38亿）将超过苹果的HDI PCB需求（~$30-35亿）\n\n[... middle omitted ...]\n\ns to hundreds of thousands of GPUs, the number of optical transceivers required to connect these systems is growing rapidly. While investors have largely focused on beneficiaries such as GPUs,\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$320.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R033",
    "title": "摩根斯坦利：市场低估的不是AI投资放缓，而是日本线缆企业供给侧的差异化定价权",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是AI投资放缓，而是日本线缆企业供给侧的差异化定价权\n\n当市场目光聚焦于宏观不确定性和AI半导体板块的剧烈回调时，一份来自摩根斯坦利的日本线缆行业研报，给出了一个与近期股价表现截然相反的判断：基本面依然强劲，且真正的结构性机会可能被市场误读了。\n\n这份由分析师Yu Shirakawa主笔的报告，覆盖了住友电工、藤仓和古河电工三家日本线缆巨头。报告发布之际，三家公司股价均经历了不同程度的回调——藤仓一个月内下跌近40%，住友电工跌超8%，即便是涨幅最为凌厉的古河电工也回落了6%。然而，摩根斯坦利却在此刻上调了住友电工的目标价，同时维持对古河电工的“超配”评级，并重申整个行业的“吸引力”评级。\n\n这并非简单的逆势看多。其核心逻辑在于：市场当前对股价回调的解读，可能过度归因于宏观风险或AI投资周期见顶，而真正决定这三家公司未来两年业绩走向的关键变量——供给侧的产能瓶颈、产品结构的升级以及由此带来的议价权重塑——尚未被充分定价。\n\n本文基于这份研报，提炼出三个层次的核心洞察：为什么AI投资不是问题、三家公司的差异化究竟在哪、以及市场尚未完全消化的风险与机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 超大规模云厂商的资本开支正在加速，而非减速，这是行业最坚实的底部\n\n市场近期对AI相关股票的担忧，很大程度上源于对资本开支周期见顶的恐惧。然而，摩根斯坦利援引其美国IT团队的更新预测指出，2026年11家超大规模云厂商的资本开支同比增速预期已从此前的63%大幅上修至87%。\n\n这一数字的意义在于，它直接回答了“AI投资是否已经放缓”这一关键问题。答案是否定的。不仅如此，报告明确指出，约75%的资本开支将直接投向AI基础设施，包括数据中心、GPU集群和电力设施。这意味着，对于处于产业链上游的线缆\n\n[... middle omitted ...]\n\n和二阶影响推演，可能正是你做出独立判断所需要的最后一块拼图。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日股线缆三兄弟，谁在AI基建里最能打？\n\n**AI基建，光缆先行**\n\n最近日股线缆板块回调不少，但投行研报认为基本面没变——超大规模云厂商2026年资本开支预计同比+87%，AI数据中心投资依然是强支撑。\n\n**1/ 三家公司，三个定位**\n\n古河电工（首选）：预计F3/27-29年营业利润CAGR达42.1%，三家中最高。液冷模块是核心增量，预计F3/27营收500亿日元，F3/29到3000亿日元。\n\n住友电工（上调目标价）：光通信产品扩产节奏更确定，预制棒产能过剩反而成竞争优势。但市场预期已打满，上行空间有限。\n\n藤仓（下调目标价）：盈利能力没问题，但产能是瓶颈——光纤生产受氢气短缺影响，预计光缆销量增速放缓至+10%。\n\n**2/ 光通信的“隐形冠军”**\n\n住友电工的连续波激光二极管（CW-LD）在磷化铟平台垂直整合，市占率高。随着CPO（共封装光学）产品普及，这类高附加值器件占比提升是利润驱动力。\n\n**3/ 风险在哪？**\n\n如果超大规模厂商因电力/基建瓶颈放缓投入，估值可能比盈利下修更惨。古河电工的液冷模块认证若延迟，增长会打折。藤仓的产能扩张若提前，反而可能是股价催化剂。\n\n**📌 一句话\n\n[... middle omitted ...]\n\nct high 2-digit growth in hyperscaler capex (87% YoY). We also expect broader adoption of products for CPO ahead, and think increased mix of high-value-added products together with new product\n\n[... middle omitted ...]\n\n Electric (5802.T)</td><td>E (01/16/2026)</td><td>¥10,250</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R034",
    "title": "Bernstein：AI购物离“自主决策”还差一个支付环节",
    "digest": "[wechat_article.md]\n# Bernstein：AI购物离“自主决策”还差一个支付环节\n\n过去六个月，从沃尔玛宣布与ChatGPT合作开始，“Agentic Shopping”成为美国零售业最热的关键词。但喧嚣之下，一个根本问题始终悬而未决：AI到底能在多大程度上替代人类的购物决策？\n\nBernstein（Bernstein）最近发布了一份极具实操性的研报。研究团队没有停留在概念推演，而是直接上手测试了五款AI工具——ChatGPT、Gemini、Claude三大基础模型，以及亚马逊Alexa和沃尔玛Sparky两个零售原生系统。测试任务简单到近乎朴素：为一家人买一盒牛奶，为一周备餐搭建购物篮。\n\n结果却揭示了一个被市场严重低估的核心矛盾。AI在“发现商品”环节已经展现出令人印象深刻的潜力，但在“完成交易”这一最终步骤上，所有工具无一例外地败下阵来。这份报告的核心判断并不在于AI购物何时到来，而在于：**真正决定AI购物能否从“玩具”变成“工具”的关键，并非模型能力，而是支付环节的深度嵌入。**\n\n这不是一个技术问题，而是一个商业模式和竞争格局的问题。谁先打通支付闭环，谁就掌握了下一代零售的入口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 从“发现”到“购买”的断层，是所有AI购物工具的阿克琉斯之踵\n\nBernstein的测试设计精准地抓住了购物漏斗的六个关键环节：品类识别、SKU识别、定价、总成本估算、加入购物车、支付。结果一目了然：在“加入购物车”和“支付”这两个环节，所有工具都亮起了红灯。\n\n基础模型（ChatGPT、Gemini、Claude）在信息检索和推荐上表现尚可，但一旦涉及交易执行，它们立刻暴露出“手不够长”的致命缺陷。它们可以告诉你“这盒牛奶在Whole Foods卖4.79美元”，但无法帮你下单。它们依赖网络爬虫\n\n[... middle omitted ...]\n\n们会在那里分享更多关于AI购物竞争格局的深度分析和独家图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI购物助手实测：谁真能帮你下单？\n\n**实测5款AI购物工具**\n\n**买一盒牛奶的完整体验**\n\n最近某外资投行出了一份很有趣的研报，测试了5款AI购物工具的能力。从“找商品”到“付钱”全流程打分，结果有点意思。\n\n**1/ 通用AI模型 vs 零售原生AI**\n\nChatGPT、Gemini、Claude这类通用模型，更像“商品搜索器”。它们能推荐产品、对比价格，但数据来源是网页抓取，价格和库存信息经常不准。比如Gemini第一次问牛奶价格时，只能给个模糊区间，追问后才给出具体SKU信息。\n\n**2/ 零售自己的AI确实更强**\n\nAmazon Alexa和Walmart Sparky能直接对接实时库存数据，从推荐到加购物车一气呵成。Sparky甚至能展示送达时间（18分钟到货）、价格、评分，还能直接加购。Alexa也能做到，但Amazon Fresh和Whole Foods的产品需要跳转网页才能加购。\n\n**3/ 支付环节是最大短板**\n\n所有AI在“付钱”这一步都卡住了。即使是表现最好的Sparky和Alexa，也无法在对话界面内完成支付。用户最后还是得自己去点“下单”。研报判断：AI离真正的“端到\n\n[... middle omitted ...]\n\n 723 126 luca.solca@bernsteinsg.com\n\nMelinda Hu +852 2123 2643 melinda.hu@bernsteinsg.com\n\nNadine Sarwat, CFA +44 20 7676 6849 nadine.sarwat@bernsteinsg.com\n\nRichard J. Clarke, FCA +44 20 7676\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 1: FX reserves have dropped in most Asian economies since February"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: CNH continued to strengthen vs. USD despite rangebound DXY"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: FX conversion ratio for goods trade balance has generally been rising"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Net foreign outflows from the KOSPI have reached approximately US\\$80bn, largely driven by the two largest semiconductor stocks."
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The rally in two semiconductor stocks pushed their index weights above diversification thresholds under the Investment Company Act of 1940"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: BI has been raising SRBI yields in an attempt to attract inflows"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Inflation pass through in the Philippines has been swift, prompting BSP to be hawkish"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Electronics has helped to buffer Malaysian exports...."
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ... as well as Singapore's exports"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Global factors like equity and commodity prices could explain the majority of FX moves in March and April"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...but lately more domestic factors—like rate differentials—are starting to become more important once again"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Even as the pace of total returns has flattened out over the past month, the past week has marked another year-to-date low in the USD/CNY fix"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Modest Sterling reactions to rising odds of a Burnham led government"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: SNB CHF selling was fairly small in March and April—consistent with other periods where inflation is comfortably within their 0-2% target range"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: As inflation has repriced lower, we see value to being long 10y real rates on beta vs nominals"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: CAD growth and policy pricing roughly offset each other currently Contributions from Macro PCA factors over past month, to Canadian government bond yields"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: UK rates have been the most sensitive to oil moves Volatility adjusted beta (t-stat) of daily changes in 2y1y swap rates for a $1\\%$ change in oil prices (in local currency)"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 4: UK bank Gilt holdings increasing Banks holdings of Gilts per maturity"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Divergence in policy outlooks should drive the widening further"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Belly yields have continued to move higher in tandem with traded inflation"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 30-city daily property transaction volume in the primary market fell below year-ago level"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: 16-city daily property transaction volume in the secondary market declined but remained above year-ago level"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: China's passenger flights for domestic routes edged up but remained below year-ago level"
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China's passenger flights cancellation rate declined over the last week but remained elevated"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Traffic congestion was roughly flat over the last week"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Domestic gasoline and diesel prices remained unchanged over the last week"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Prices for polypropylene edged up over the last week while other exposed chemicals stabilized somewhat"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Import prices for both energy products and integrated circuits surged in May"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Export prices of refined petroleum products and integrated circuits surged in May"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The Morning Consult consumer confidence rose to multi-year high"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: New energy vehicles (NEVs) sales volume increased in May but remained below year-ago level"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Total auto sales volume edged higher in May but remained below year-ago level"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Steel demand edged down over the past week"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Steel production was roughly flat over the past week"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Daily coal consumption in coastal provinces fell from recent high"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 16: RMB 1.59bn local government special bonds have been issued year-to-date"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Official port container throughput fell over the last week but was above year-ago level"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Freight volume of departing ships at 20 major ports declined over the past week but still above year-ago level"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Our nowcast indicates China oil demand fell to 16.2mb/d in the latest reading"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Interbank repo rates edged up in recent weeks"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Exhibit 21",
    "context": "Exhibit 21: CNY appreciated against both the USD and the CFETS basket over the past week"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Exhibit 22",
    "context": "Exhibit 22: USDCNY fixing implied countercyclical factor fell somewhat over the past week"
  },
  {
    "figure_id": "F043",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: KOSDAQ has significantly underperformed since August 2023"
  },
  {
    "figure_id": "F044",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 2: KOSPI earnings upgrades have been materially stronger than KOSDAQ earnings revisions"
  },
  {
    "figure_id": "F045",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: KOSDAQ valuations remain more elevated than KOSPI's 12-month forward P/E"
  },
  {
    "figure_id": "F046",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: However, KOSDAQ has seen stronger foreign inflows year-to-date, while KOSPI has experienced significant foreign outflows"
  },
  {
    "figure_id": "F047",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Foreign outflows from KOSPI have been largely driven by the two largest semiconductor stocks"
  },
  {
    "figure_id": "F048",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Foreign inflows into KOSDAQ have been concentrated in the information technology and health care sectors"
  },
  {
    "figure_id": "F049",
    "report_id": "R005",
    "label": "Exhibit 8",
    "context": "Up (↑) = Up wow vs. the previous week Asterisk (\\*) = Expressed in standard deviation of 1-wk change in 1-year Year-to-date Foreign Inflows to Korea"
  },
  {
    "figure_id": "F050",
    "report_id": "R005",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Equity inflows to 5 AEJ markets 4-week rolling sum"
  },
  {
    "figure_id": "F051",
    "report_id": "R005",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Equity inflows to 5 AEJ markets"
  },
  {
    "figure_id": "F052",
    "report_id": "R005",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Bond inflows to 4 AEJ markets 4-week rolling sum"
  },
  {
    "figure_id": "F053",
    "report_id": "R005",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Bond inflows to 4 AEJ markets"
  },
  {
    "figure_id": "F054",
    "report_id": "R005",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Housing prices and rental prices National, monthly and weekly price changes"
  },
  {
    "figure_id": "F055",
    "report_id": "R005",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Living expense price changes Monthly and weekly changes vs. CPI"
  },
  {
    "figure_id": "F056",
    "report_id": "R005",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Daily Financial Condition Index Jan 1, 2013=100"
  },
  {
    "figure_id": "F057",
    "report_id": "R005",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Performance of Korean and regional equity markets Exhibit 18: KOSPI and MSCI regional index KOSPI Index price performance (KRW)"
  },
  {
    "figure_id": "F058",
    "report_id": "R005",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Weekly sector performance relative to KOSPI"
  },
  {
    "figure_id": "F059",
    "report_id": "R005",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Historical trend of monthly KOSPI earnings momentum"
  },
  {
    "figure_id": "F060",
    "report_id": "R005",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Weekly earnings momentum for KOSPI and selected sectors"
  },
  {
    "figure_id": "F061",
    "report_id": "R005",
    "label": "Exhibit 23",
    "context": "Exhibit 24: 12-month forward P/E and P/B for KOSPI, since Jan 2008"
  },
  {
    "figure_id": "F062",
    "report_id": "R005",
    "label": "Exhibit 25",
    "context": "Exhibit 25: 12-month forward P/E for MSCI Korea, since Jan 2008"
  },
  {
    "figure_id": "F063",
    "report_id": "R005",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Current 12m forward P/E of KOSPI and selected sectors since Jan 2006"
  },
  {
    "figure_id": "F064",
    "report_id": "R005",
    "label": "Exhibit 28",
    "context": "Exhibit 28: MXKR valuation discount relative to MSCI AC World NTM P/E"
  },
  {
    "figure_id": "F065",
    "report_id": "R005",
    "label": "Exhibit 29",
    "context": "Exhibit 29: MXKR valuation discount relative to MXAPJ NTM P/E"
  },
  {
    "figure_id": "F066",
    "report_id": "R005",
    "label": "Exhibit 32",
    "context": "Exhibit 32: 2025 & 2026 year-to-date KOSPI purchase by investor type"
  },
  {
    "figure_id": "F067",
    "report_id": "R005",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Weekly fund flows on sectors by investor type, with relative returns to KOSPI KOSPI and sector's relative returns and flow data Exhibit 35: KOSPI sectors, ranked by foreign ownership as a % of total market value"
  },
  {
    "figure_id": "F068",
    "report_id": "R005",
    "label": "Exhibit 36",
    "context": "Exhibit 36: KOSPI sectors ranked by foreign ownership % change Absolute ownership % (market value) changes"
  },
  {
    "figure_id": "F069",
    "report_id": "R005",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Equity net weekly flows (Week ending on Thursday due to data availability)"
  },
  {
    "figure_id": "F070",
    "report_id": "R005",
    "label": "Exhibit 38",
    "context": "Exhibit 38: 12-month forward D/Y for KOSPI and Korea Treasury bond yield"
  },
  {
    "figure_id": "F071",
    "report_id": "R005",
    "label": "Exhibit 40",
    "context": "Exhibit 40: USDKRW and USDCNY rates"
  },
  {
    "figure_id": "F072",
    "report_id": "R005",
    "label": "Exhibit 41",
    "context": "Exhibit 41: USDKRW vs. 10 year bond yields differentials between the US and Korea"
  },
  {
    "figure_id": "F073",
    "report_id": "R005",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Korea Equity Risk Barometer"
  },
  {
    "figure_id": "F074",
    "report_id": "R005",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Loans on Margin account balance"
  },
  {
    "figure_id": "F075",
    "report_id": "R005",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Korea Volatility Index (VKOSPI)"
  },
  {
    "figure_id": "F076",
    "report_id": "R005",
    "label": "Exhibit 45",
    "context": "Exhibit 45: KOSPI Percent of Members above 200 day moving average"
  },
  {
    "figure_id": "F077",
    "report_id": "R006",
    "label": "Figure 5",
    "context": "## 4. Our view on liquidity in coming weeks: We continue to expect the PBoC to be more flexible with 7d OMOs to inject short-term liquidity amid higher government bond supply, as well as tax payment and month-end funding needs. As for medium- to long-term liqu"
  },
  {
    "figure_id": "F078",
    "report_id": "R006",
    "label": "Figure 10",
    "context": "As shown in Figure 10, after accumulating massive (ultra) long-end CGBs/policy bank bonds in April and May, onshore funds reduced bond holdings in June. In the first week of June, funds were still adding 10y and above tenors while net selling the front-end and"
  },
  {
    "figure_id": "F079",
    "report_id": "R007",
    "label": "Figure 1",
    "context": "Figure 1: UBS leading indicators for Autos/Industrial semis - we see a general positive trend in terms of cycle Figure 2: We expect next quarter to grow by 9% q-o-q after an increase of 4% in Q1'26..."
  },
  {
    "figure_id": "F080",
    "report_id": "R007",
    "label": "Figure 3",
    "context": "Figure 3: ...Q2'26E likely to deliver 21% y-o-y growth after 20% in Q1'26"
  },
  {
    "figure_id": "F081",
    "report_id": "R007",
    "label": "Figure 4",
    "context": "Figure 4: CQ2 26E Guidance Comp. Y-o-Y % Analog Semis"
  },
  {
    "figure_id": "F082",
    "report_id": "R007",
    "label": "Figure 5",
    "context": "Figure 5: CQ2 26E Guidance Comp. Q-o-Q % Analog Semis"
  },
  {
    "figure_id": "F083",
    "report_id": "R007",
    "label": "Figure 6",
    "context": "Figure 6: We estimate 10% y-o-y auto semis revenue growth in 2026E (unchanged) and +c14% in 2027E vs (unchanged) based on our bottom-up estimates. Figure 7: The analog semis within our coverage are trading on a -17% discount to se"
  },
  {
    "figure_id": "F084",
    "report_id": "R007",
    "label": "Figure 8",
    "context": "Figure 8: China % of revenue for main analog players China % of revenue"
  },
  {
    "figure_id": "F085",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "Figure 9: China growth y-o-y by companies shows significant difference Figure 10: China grew c7% y-o-y in 2025 but is set to grow more in line with the market going forward"
  },
  {
    "figure_id": "F086",
    "report_id": "R007",
    "label": "Figure 11",
    "context": "Figure 11: When accounting for share loss, we estimate incumbents' revenue growth should be stronger outside China 2025-29E"
  },
  {
    "figure_id": "F087",
    "report_id": "R007",
    "label": "Figure 14",
    "context": "Figure 14: When accounting for content growth, we estimate inventory digestion started in Q4'23 and we expect an improving trend through the year"
  },
  {
    "figure_id": "F088",
    "report_id": "R007",
    "label": "Figure 15",
    "context": "Figure 15: Auto/industrial OEM inventory days stabilizing"
  },
  {
    "figure_id": "F089",
    "report_id": "R007",
    "label": "Figure 16",
    "context": "Figure 16: Total inventories '000 units: inventories were up 3% during 1Q26 vs 1Q25 levels. This is back to a relatively high level for Stellantis for example"
  },
  {
    "figure_id": "F090",
    "report_id": "R007",
    "label": "Figure 17",
    "context": "Figure 17: We expect next quarter to grow by 9% q-o-q after an increase of 4% in Q1'26..."
  },
  {
    "figure_id": "F091",
    "report_id": "R007",
    "label": "Figure 18",
    "context": "Figure 18: ...Q2'26E likely to deliver 21% y-o-y growth after 20% in Q1'26"
  },
  {
    "figure_id": "F092",
    "report_id": "R007",
    "label": "Figure 21",
    "context": "Figure 21: China's PV inventory changes (monthly)"
  },
  {
    "figure_id": "F093",
    "report_id": "R007",
    "label": "Figure 24",
    "context": "Figure 24: Auto production growth outpaced auto semis revenue growth in Q1'24, marking the start of an inventory digestion"
  },
  {
    "figure_id": "F094",
    "report_id": "R007",
    "label": "Figure 25",
    "context": "Figure 25: When accounting for content growth, we believe inventory digestion started in Q4'23, and eased into H2'25"
  },
  {
    "figure_id": "F095",
    "report_id": "R007",
    "label": "Figure 26",
    "context": "Figure 26: When accounting for content growth and exceptional pricing through 2021-22, inventories appear to be reaching healthier levels"
  },
  {
    "figure_id": "F096",
    "report_id": "R007",
    "label": "Figure 29",
    "context": "Figure 29: Capex (\\$bn) from analog semis is decelerating. Consensus expects -7% y-o-y in 2026E (-22% y-o-y 2025)"
  },
  {
    "figure_id": "F097",
    "report_id": "R007",
    "label": "Figure 30",
    "context": "Figure 30: Infineon backlog/4Q rolling forward revenues - we see a normalisation in terms of backlog close to pre-Covid level"
  },
  {
    "figure_id": "F098",
    "report_id": "R007",
    "label": "Figure 33",
    "context": "Figure 33: Powertrain auto semis bottom-up model - we forecast 6% in 2026E (unchanged), with +11% (unchanged) estimated in 2027E Figure 34: Autos/Industrial semis Forward EV/Sales"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "Figure 35",
    "context": "Figure 35: Autos/Industrial semis Forward P/E"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "Figure 36",
    "context": "Figure 36: Infineon outperformed the sector 80% of the time, on average, since 2012, driven mainly by power, in our view. 2021 underperformance was mainly driven by conservative behaviour on pricing, being reversed in 2023"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "Figure 37",
    "context": "Figure 37: Texas Instruments outperformed the sector 63% of the time since 2012, and we believe underperformance in 2023 was mainly due to consignment strategy and less discrete power exposure"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "Figure 38",
    "context": "Figure 38: ON Semi outperformed the sector 45% of the time since 2012 and performed better recently, driven by power content growth, in our view"
  },
  {
    "figure_id": "F103",
    "report_id": "R007",
    "label": "Figure 39",
    "context": "Figure 39: ADI outperformed the sector 64% of the time since 2012, driven by solid content growth"
  },
  {
    "figure_id": "F104",
    "report_id": "R007",
    "label": "Figure 40",
    "context": "Figure 40: MCHP outperformed the sector 61% of the time since 2012, and 2022 was mainly driven by MCU pricing, in our view"
  },
  {
    "figure_id": "F105",
    "report_id": "R007",
    "label": "Figure 41",
    "context": "Figure 41: STM outperformed the sector 48% of the time since 2012, driven by silicon carbide and stockpiling, in our view"
  },
  {
    "figure_id": "F106",
    "report_id": "R007",
    "label": "Figure 42",
    "context": "Figure 42: Renesas outperformed the sector 23% of the time since 2012"
  },
  {
    "figure_id": "F107",
    "report_id": "R007",
    "label": "Figure 43",
    "context": "Figure 43: NXP outperformed the sector 50% of the time since 2012, and we believe it underperformed before 2020 due to less discrete power exposure and outperformed in 2021, driven by MCU pricing"
  },
  {
    "figure_id": "F108",
    "report_id": "R007",
    "label": "Figure 44",
    "context": "Figure 44: Gross margin average across analog players rebounded in H2'25, and is expected to increase further until the end of FY26E"
  },
  {
    "figure_id": "F109",
    "report_id": "R007",
    "label": "Figure 45",
    "context": "Figure 45: Industrial as % of sales by company"
  },
  {
    "figure_id": "F110",
    "report_id": "R007",
    "label": "Figure 46",
    "context": "Figure 46: Industrial recovery took off in Q2'25 and is expected to accelerate further"
  },
  {
    "figure_id": "F111",
    "report_id": "R007",
    "label": "Figure 47",
    "context": "Figure 48: CQ2 26E Guidance Comp. YoY % Analog Semis"
  },
  {
    "figure_id": "F112",
    "report_id": "R007",
    "label": "Figure 47",
    "context": "Figure 48: CQ2 26E Guidance Comp. YoY % Analog Semis"
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "Figure 49",
    "context": "Figure 49: CQ2 26E Guidance Comp. QoQ % Analog Semis"
  },
  {
    "figure_id": "F114",
    "report_id": "R007",
    "label": "Figure 50",
    "context": "Figure 50: Q1 Automotive revenues YoY"
  },
  {
    "figure_id": "F115",
    "report_id": "R007",
    "label": "Figure 51",
    "context": "Figure 51: Q1 Automotive revenues QoQ"
  },
  {
    "figure_id": "F116",
    "report_id": "R007",
    "label": "Figure 52",
    "context": "Figure 52: Q1 Industrial revenues YoY"
  },
  {
    "figure_id": "F117",
    "report_id": "R007",
    "label": "Figure 53",
    "context": "Figure 53: Q1 Industrial revenues QoQ"
  },
  {
    "figure_id": "F118",
    "report_id": "R007",
    "label": "Figure 54",
    "context": "Figure 54: Q2 Automotive revenues YoY"
  },
  {
    "figure_id": "F119",
    "report_id": "R007",
    "label": "Figure 55",
    "context": "Figure 55: Q2 Automotive revenues QoQ"
  },
  {
    "figure_id": "F120",
    "report_id": "R007",
    "label": "Figure 56",
    "context": "Figure 56: Q22 Industrial revenues YoY Industrial Q2 YoY"
  },
  {
    "figure_id": "F121",
    "report_id": "R007",
    "label": "Figure 57",
    "context": "Figure 57: Q2 Industrial revenues QoQ"
  },
  {
    "figure_id": "F122",
    "report_id": "R007",
    "label": "Figure 58",
    "context": "Figure 58: We expect next quarter to grow by 9% q-o-q after a decrease of 4% in Q1'26..."
  },
  {
    "figure_id": "F123",
    "report_id": "R007",
    "label": "Figure 59",
    "context": "Figure 59: ...Q2'26E likely to deliver 21% y-o-y growth after 20% in Q1'26"
  },
  {
    "figure_id": "F124",
    "report_id": "R007",
    "label": "Figure 60",
    "context": "Figure 60: Total inventories '000 units: inventories were up 3% during 1Q26 vs 1Q25 levels"
  },
  {
    "figure_id": "F125",
    "report_id": "R007",
    "label": "Figure 61",
    "context": "Figure 61: Q1s Autos/Industrial OEMs inventory days"
  },
  {
    "figure_id": "F126",
    "report_id": "R007",
    "label": "Figure 63",
    "context": "Figure 63: Analog semis revenue growth (3-mth rolling) vs. stock performance"
  },
  {
    "figure_id": "F127",
    "report_id": "R007",
    "label": "Figure 64",
    "context": "Figure 64: Semis revenue growth vs OEM growth"
  },
  {
    "figure_id": "F128",
    "report_id": "R007",
    "label": "Figure 65",
    "context": "Figure 65: Autos/industrial semis inventory days"
  },
  {
    "figure_id": "F129",
    "report_id": "R007",
    "label": "Figure 66",
    "context": "Figure 66: Q1 autos/industrial semis inventory days"
  },
  {
    "figure_id": "F130",
    "report_id": "R007",
    "label": "Figure 67",
    "context": "Figure 67: Autos/Industrial OEMs inventory days"
  },
  {
    "figure_id": "F131",
    "report_id": "R007",
    "label": "Figure 68",
    "context": "Figure 68: Five-year Q1s Autos/Industrial OEMs inventory days"
  },
  {
    "figure_id": "F132",
    "report_id": "R007",
    "label": "Figure 69",
    "context": "Figure 69: Auto Tier 1/OEM inventory days"
  },
  {
    "figure_id": "F133",
    "report_id": "R007",
    "label": "Figure 70",
    "context": "Figure 70: Five-year Q1s Auto Tier 1/OEM inventory days"
  },
  {
    "figure_id": "F134",
    "report_id": "R007",
    "label": "Figure 71",
    "context": "Figure 71: Absolute automotive inventory level (US\\$bn)"
  },
  {
    "figure_id": "F135",
    "report_id": "R007",
    "label": "Figure 72",
    "context": "Figure 72: Absolute industrial inventory level (US\\$bn)"
  },
  {
    "figure_id": "F136",
    "report_id": "R007",
    "label": "Figure 73",
    "context": "Figure 73: Comments on inventory from Automotive OEMs/suppliers Figure 74: Autos/Industrial semis Forward EV/Sales"
  },
  {
    "figure_id": "F137",
    "report_id": "R007",
    "label": "Figure 75",
    "context": "Figure 75: Autos/Industrial semis Forward P/E"
  },
  {
    "figure_id": "F138",
    "report_id": "R007",
    "label": "Figure 76",
    "context": "Figure 76: Autos/Industrial semis Forward EV/EBITDA"
  },
  {
    "figure_id": "F139",
    "report_id": "R007",
    "label": "Figure 77",
    "context": "Figure 77: Autos/Industrial semis Forward P/BV"
  },
  {
    "figure_id": "F140",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 1: TSF flows rose from April to May after seasonal adjustment"
  },
  {
    "figure_id": "F141",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: M1 growth edged up in May"
  },
  {
    "figure_id": "F142",
    "report_id": "R011",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Trump's approval rating"
  },
  {
    "figure_id": "F143",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "EXHIBIT 2: Change in House seats in mid-term elections for President's party Changes in House seats during Mid-term elections for President's party"
  },
  {
    "figure_id": "F144",
    "report_id": "R011",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Chance to Win House Majority"
  },
  {
    "figure_id": "F145",
    "report_id": "R011",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Midterm House Seats Projection"
  },
  {
    "figure_id": "F146",
    "report_id": "R011",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Prediction market on who will will the US House?"
  },
  {
    "figure_id": "F147",
    "report_id": "R011",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Senate - Key races for 2026 midterms EXHIBIT 7: Chance to Win Senate Majority"
  },
  {
    "figure_id": "F148",
    "report_id": "R011",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Midterm Senate Seats Projection"
  },
  {
    "figure_id": "F149",
    "report_id": "R011",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Prediction market on who will win the US Senate"
  },
  {
    "figure_id": "F150",
    "report_id": "R011",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: ACA favorability as per KFF Health Tracking Polls"
  },
  {
    "figure_id": "F151",
    "report_id": "R011",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Uninsured rate in the US US Uninsured rate"
  },
  {
    "figure_id": "F152",
    "report_id": "R011",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Cost concerns"
  },
  {
    "figure_id": "F153",
    "report_id": "R011",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Healthcare cost concerns Which political party, the Democrats or the Republicans, do you trust to do a better job in each of the following?"
  },
  {
    "figure_id": "F154",
    "report_id": "R011",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Dec 2025 survey of top 10 public concerns -% of respondents mentioning each issue"
  },
  {
    "figure_id": "F155",
    "report_id": "R012",
    "label": "Figure 1",
    "context": "Figure 1: China vehicle sales vs. BEV sales"
  },
  {
    "figure_id": "F156",
    "report_id": "R012",
    "label": "Figure 2",
    "context": "Figure 2: China EV penetration rates"
  },
  {
    "figure_id": "F157",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "Figure 3: Battery electric vehicle penetration rates by region"
  },
  {
    "figure_id": "F158",
    "report_id": "R012",
    "label": "Figure 4",
    "context": "Figure 4: Battery electric vehicle sales – monthly (China + EU + US)"
  },
  {
    "figure_id": "F159",
    "report_id": "R012",
    "label": "Figure 6",
    "context": "Figure 6: Total vehicle sales – Global"
  },
  {
    "figure_id": "F160",
    "report_id": "R012",
    "label": "Figure 7",
    "context": "Figure 7: Battery electric vehicle sales – Global"
  },
  {
    "figure_id": "F161",
    "report_id": "R012",
    "label": "Figure 8",
    "context": "Figure 8: Total vehicle sales – China"
  },
  {
    "figure_id": "F162",
    "report_id": "R012",
    "label": "Figure 9",
    "context": "Figure 9: Battery electric vehicle sales – China"
  },
  {
    "figure_id": "F163",
    "report_id": "R012",
    "label": "Figure 10",
    "context": "Figure 10: Total vehicle sales – US"
  },
  {
    "figure_id": "F164",
    "report_id": "R012",
    "label": "Figure 11",
    "context": "Figure 11: Battery electric vehicle sales – US"
  },
  {
    "figure_id": "F165",
    "report_id": "R012",
    "label": "Figure 12",
    "context": "Figure 12: Total vehicle sales – EU"
  },
  {
    "figure_id": "F166",
    "report_id": "R012",
    "label": "Figure 13",
    "context": "Figure 13: Battery electric vehicle sales – EU"
  },
  {
    "figure_id": "F167",
    "report_id": "R012",
    "label": "Figure 14",
    "context": "Figure 14: Lithium spodumene prices"
  },
  {
    "figure_id": "F168",
    "report_id": "R012",
    "label": "Figure 15",
    "context": "Figure 15: Lithium hydroxide prices"
  },
  {
    "figure_id": "F169",
    "report_id": "R012",
    "label": "Figure 16",
    "context": "Figure 16: Lithium carbonate prices"
  },
  {
    "figure_id": "F170",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "CLICK TO VOTE Voting Open May 26 $^{th}$ - June 12 $^{th}$ Please vote for JPM (5 stars) For the first time since 1994, the FIFA World Cup returns to North America as the United States, Canada and Mexico jointly host the 2026 tournament. This is likely to be t"
  },
  {
    "figure_id": "F171",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 1: Performance Lookback 2026 World Cup Beneficiaries and Sponsors Baskets Since 2024-end, Rebased 100, Capped Liquidity-Weighted, Relative to S&P 500 (EW)"
  },
  {
    "figure_id": "F172",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: Median Relative Returns Across Major Sporting Events Relative to MSCI ACWI"
  },
  {
    "figure_id": "F173",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Includes both domestic and international visitation, see Report"
  },
  {
    "figure_id": "F174",
    "report_id": "R014",
    "label": "Figure 10",
    "context": "Figure 10: World Cup: Occupancy on the Books – Full Range of World Cup Match Dates Average forward occupancy, first match date to final match date by market (as of 1 June 2026), see Report"
  },
  {
    "figure_id": "F175",
    "report_id": "R014",
    "label": "Figure 11",
    "context": "Figure 11: Occupancy on the Books – Lead-in and World Cup Match Days Average forward occupancy, nights before and on match day by market (as of 1 June 2026), see Report"
  },
  {
    "figure_id": "F176",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 1: In this volatile macro backdrop, we highlight for superior upside: BP, Repsol and Galp"
  },
  {
    "figure_id": "F177",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: On our estimates, EU Oils are pricing a long-term Brent of \\$60/bbl solving for an 8% FCF yield Implied 2026-29 oil price for the EU majors solving by a 8% FCF yield (Brent, \\$/bl)"
  },
  {
    "figure_id": "F178",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: On consensus estimates, EU Oils are pricing a long-term Brent of \\$60/bbl solving for an 8% FCF yield Implied 2026-29 oil price for the EU majors by a 8% FCF yield (Brent, \\$/bl)"
  },
  {
    "figure_id": "F179",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The market is currently pricing 2030E Brent at \\$70/\\$72/bl on Bloomberg consensus/forwards (vs GSe of \\$75/bl)."
  },
  {
    "figure_id": "F180",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Mar FY-end companies AGM schedule by number of companies"
  },
  {
    "figure_id": "F181",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Mar FY-end companies AGM schedule by market cap"
  },
  {
    "figure_id": "F182",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Concentration of AGM for peak day increased slightly % of companies"
  },
  {
    "figure_id": "F183",
    "report_id": "R016",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Since the 2025 AGM season, low approval screen outperformed until the start of the Iran war, but remains a laggard as the market focused on AI themes"
  },
  {
    "figure_id": "F184",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Y+D screen has outperformed NYND screen by 12ppt since June 3rd ..."
  },
  {
    "figure_id": "F185",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ... and SMID Y+D has outperformed SMID NYND by 7ppts in the same period"
  },
  {
    "figure_id": "F186",
    "report_id": "R016",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Our 3-/6-/12-month TOPIX targets are 4,100/4,200/4,400 TOPIX"
  },
  {
    "figure_id": "F187",
    "report_id": "R016",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GS Top-down earnings forecast (TOPIX)"
  },
  {
    "figure_id": "F188",
    "report_id": "R016",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Sector recommendation Exhibit 14: GS top-down vs. consensus bottom-up estimates of FY2026 EPS growth"
  },
  {
    "figure_id": "F189",
    "report_id": "R016",
    "label": "Exhibit 15",
    "context": "Exhibit 15: GS top-down vs. consensus bottom-up estimates of FY2027 EPS growth"
  },
  {
    "figure_id": "F190",
    "report_id": "R016",
    "label": "Exhibit 16",
    "context": "Exhibit 16: TOPIX 12-month forward P/E Consensus"
  },
  {
    "figure_id": "F191",
    "report_id": "R016",
    "label": "Exhibit 17",
    "context": "Exhibit 17: TOPIX P/B Actual"
  },
  {
    "figure_id": "F192",
    "report_id": "R016",
    "label": "Exhibit 18",
    "context": "Exhibit 18: TOPIX Index"
  },
  {
    "figure_id": "F193",
    "report_id": "R016",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Global equity indices Indexed, local currency"
  },
  {
    "figure_id": "F194",
    "report_id": "R016",
    "label": "Exhibit 22",
    "context": "Exhibit 22: TSE net equity transaction by investor type ¥ billion"
  },
  {
    "figure_id": "F195",
    "report_id": "R016",
    "label": "Exhibit 23",
    "context": "Exhibit 23: TSE net equity transaction by investor type ¥ billion Exhibit 24: Cumulative announced buyback JPY tn, as of Jun 4 2026"
  },
  {
    "figure_id": "F196",
    "report_id": "R016",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Margin transaction ¥ billions; Index"
  },
  {
    "figure_id": "F197",
    "report_id": "R016",
    "label": "Exhibit 26",
    "context": "Exhibit 26: TOPIX earnings revision index Indexed"
  },
  {
    "figure_id": "F198",
    "report_id": "R016",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Global earnings revision index indexed, FY2026"
  },
  {
    "figure_id": "F199",
    "report_id": "R016",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Style analysis: Value vs. Growth, Size MSCI Japan Value / MSCI Japan Growth, Topix Large 100 / Mid 400"
  },
  {
    "figure_id": "F200",
    "report_id": "R016",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Style analysis: Cyclical / Defensive Relative Performance"
  },
  {
    "figure_id": "F201",
    "report_id": "R016",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Japan Portfolio Strategy Baskets performance Exhibit 31: Strategy Baskets performance (1) TOPIX relative"
  },
  {
    "figure_id": "F202",
    "report_id": "R016",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Strategy Baskets performance (2) TOPIX relative"
  },
  {
    "figure_id": "F203",
    "report_id": "R016",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Strategy Baskets performance (3) TOPIX relative"
  },
  {
    "figure_id": "F204",
    "report_id": "R016",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Sector Performance (Topix Relative, 1-week, %)"
  },
  {
    "figure_id": "F205",
    "report_id": "R016",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Sector earnings revision momentum/ranking Past 1M, FY2026"
  },
  {
    "figure_id": "F206",
    "report_id": "R016",
    "label": "Exhibit 37",
    "context": "Exhibit 37: SPE index 52 week equal-weighted cumulative weekly performance and best-worst spreads"
  },
  {
    "figure_id": "F207",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "EXHIBIT 1: Luxury cruise industry ```mermaid graph LR"
  },
  {
    "figure_id": "F208",
    "report_id": "R017",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Viking is priced at the lower end of the luxury cruise market, behind smaller-ship luxury brands such as Silversea, Seabourn and Regent. Nightly prices for sailings aboard yachts range well into the \\$000s, with an Aman"
  },
  {
    "figure_id": "F209",
    "report_id": "R017",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Viking and Oceania have the largest average ship capacity in the luxury cruise segment at \\~950 berths, over double the size of the largest yacht operated by Ritz-Carlton Yacht Collection Average Ship Capacity"
  },
  {
    "figure_id": "F210",
    "report_id": "R017",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Customers are willing to pay significantly more for cruises aboard smaller ships, but Viking commands a price premium relative to its average ship size Cruise Price vs Ship Capacity"
  },
  {
    "figure_id": "F211",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "EXHIBIT 6: They also make a point of being differentiated from the mainstream cruise lines (“no casinos”) and also other luxury cruise lines (“no butlers or white gloves”)"
  },
  {
    "figure_id": "F212",
    "report_id": "R017",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Viking's unique offering is well-loved by their customers, with an average review score ahead of the rest of the luxury segment Average guest review score - Luxury Ocean"
  },
  {
    "figure_id": "F213",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: The luxury hotel brands entering the cruise market bring a more modern and sleek design to ships and cabins EXHIBIT 9: Orient Express's Corinthian yacht can be chartered for a private cruise if booked far in advance"
  },
  {
    "figure_id": "F214",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "EXHIBIT 8: The luxury hotel brands entering the cruise market bring a more modern and sleek design to ships and cabins EXHIBIT 9: Orient Express's Corinthian yacht can be chartered for a private cruise if booked far in advance"
  },
  {
    "figure_id": "F215",
    "report_id": "R017",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: These yacht brands compete in luxury yacht charter markets like the Greek islands, Croatian coast or French Riviera"
  },
  {
    "figure_id": "F216",
    "report_id": "R017",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: These yacht brands compete in luxury yacht charter markets like the Greek islands, Croatian coast or French Riviera Aerial view of a rocky cliff with turquoise water and small boats, surrounded by hilly terrain (no vis"
  },
  {
    "figure_id": "F217",
    "report_id": "R017",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Cruise yacht ships in service and order EXHIBIT 12: Supply in the yacht segment is set to grow faster than in the traditional luxury segment until 2029 Cruise - Gross capacity growth by segment"
  },
  {
    "figure_id": "F218",
    "report_id": "R017",
    "label": "Exhibit 16",
    "context": "EXHIBIT 13: The average age of luxury cruise goers is roughly ten years older than guests aboard mainstream cruise brands Average Guest Age by Cruise Brand"
  },
  {
    "figure_id": "F219",
    "report_id": "R017",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Over the next decade, the US population is set to add \\~22m over 45s but see virtually no growth in under 45s"
  },
  {
    "figure_id": "F220",
    "report_id": "R017",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Almost 75% of wealth owned by those over 55, with this share up more than 15% since 1990"
  },
  {
    "figure_id": "F221",
    "report_id": "R017",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Over the last three decades, the wealthiest Americans have become wealthier with the top quintile's share of wealth increasing from 61% to 72% Share of Household Wealth (Net Worth) by Income Quintile"
  },
  {
    "figure_id": "F222",
    "report_id": "R017",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: The rich are getting richer - he highest income groups have also seen the greatest increase in income US income by quintile, indexed to 2004"
  },
  {
    "figure_id": "F223",
    "report_id": "R017",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: The highest income groups have seen the largest reduction in hours worked - with more time for leisure Change in average hours worked on an average day (by income group)"
  },
  {
    "figure_id": "F224",
    "report_id": "R017",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Travel agents expect Luxury cruise to deliver the strongest growth Travel advisor expected booking growth compared to one year ago"
  },
  {
    "figure_id": "F225",
    "report_id": "R017",
    "label": "Exhibit 28",
    "context": "EXHIBIT 20: US hotel supply growth is firmly below 1%"
  },
  {
    "figure_id": "F226",
    "report_id": "R017",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Luxury hotel rooms under construction have tumbled, with owner returns under pressure"
  },
  {
    "figure_id": "F227",
    "report_id": "R017",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Luxury hotel rooms under construction relative to supply has plummeted vs pre pandemic"
  },
  {
    "figure_id": "F228",
    "report_id": "R017",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Luxury hotels are already close to maximum occupancy US hotels - occupancy"
  },
  {
    "figure_id": "F229",
    "report_id": "R017",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Luxury hotels have a lower owner ROI than hotels further down the chain scale, limiting supply growth as owners opt for higher ROI projects Average Hotel ROI by Chain Scale"
  },
  {
    "figure_id": "F230",
    "report_id": "R017",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: Luxury hotels require almost 5x the initial investment required for an Upscale hotel Average Initial Investment by Chain Scale"
  },
  {
    "figure_id": "F231",
    "report_id": "R017",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: US dynamics are mirrored in key US outbound markets - supply growth has slowed at the high end... Hotels - Mexican Caribbean supply growth (Luxury)"
  },
  {
    "figure_id": "F232",
    "report_id": "R017",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: ...while hotels under construction have also fallen materially Hotels - Mexican Caribbean under construction rooms as a % of supply (Luxury)"
  },
  {
    "figure_id": "F233",
    "report_id": "R017",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Luxury RevPAR has been significantly outperforming the rest of the industry"
  },
  {
    "figure_id": "F234",
    "report_id": "R017",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: Luxury hotels have also had significantly more pricing power than any other chain scale US 12 month ADR by Chain Scale vs CPI (indexed Jan 2000)"
  },
  {
    "figure_id": "F235",
    "report_id": "R017",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Luxury cruise (including yachts) has a higher penetration of the luxury leisure hotel market than the overall cruise industry does of the entire hotel market. Although this isn't the case with luxury leisure yet, it is s"
  },
  {
    "figure_id": "F236",
    "report_id": "R017",
    "label": "Exhibit 32",
    "context": "EXHIBIT 31: The luxury cruise market (including yachts) is set to outpace the supply growth of the mainstream and premium segments through to 2030 Cruise - Gross capacity growth by segment"
  },
  {
    "figure_id": "F237",
    "report_id": "R017",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Over the next decade, almost all the luxury capacity on order is being built at Fincantieri, suggesting that luxury capacity is limited by just one shipyard. Yachts being built for Aman, Orient Express and Emerald have l"
  },
  {
    "figure_id": "F238",
    "report_id": "R017",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: Whilst other luxury cruise brands are set to add capacity sporadically over the next 5 years, Viking is set to add 2 ships per year on average"
  },
  {
    "figure_id": "F239",
    "report_id": "R017",
    "label": "Exhibit 35",
    "context": "EXHIBIT 35: Viking's most recent ship, Mira, costs about the same as RCL's newest Icon class ship per berth but operates at higher luxury yields Latest Ships Cost per berth (\\$m)"
  },
  {
    "figure_id": "F240",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: The U.S. senior population will grow at a 3% CAGR through 2030"
  },
  {
    "figure_id": "F241",
    "report_id": "R018",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The European senior population will grow at a 2% CAGR through 2030"
  },
  {
    "figure_id": "F242",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "EXHIBIT 4: The gap between U.S. demand and supply of physicians in radiology is expected to reach -10% by 2034"
  },
  {
    "figure_id": "F243",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "EXHIBIT 5: AI could free up a significant amount of time for hospital staff"
  },
  {
    "figure_id": "F244",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "EXHIBIT 6: The number of patients who had to wait at least six weeks for a CT or an MRI more than quadrupled between 2019 and 2020, and continues to be elevated compared to pre-pandemic Patients waiting six weeks or more for a MRI"
  },
  {
    "figure_id": "F245",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "Against the backdrop of mounting pressure on radiology departments, start-ups are stepping in to address these systemic inefficiencies through the development of advanced, AI-enabled software solutions. These firms are rethinking radiology workflows, from imag"
  },
  {
    "figure_id": "F246",
    "report_id": "R018",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: Aidoc's aiOS platform provides a unified user interface for accessing results from both Aidoc and third-party algorithms ```mermaid graph TD"
  },
  {
    "figure_id": "F247",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: Viz.ai radiology solutions AI-powered care coordination. At the center of clinical decision making. Flag potential indications and prioritize worklists View images with"
  },
  {
    "figure_id": "F248",
    "report_id": "R018",
    "label": "Exhibit 10",
    "context": "EXHIBIT 10: Rad AI Reporting employs machine learning algorithms and generative AI (GenAI) to assist radiologists to create reports ```mermaid graph LR"
  },
  {
    "figure_id": "F249",
    "report_id": "R018",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: HeatFlow is a clinically proven AI platform to support end-to-end CAD care ```mermaid graph LR"
  },
  {
    "figure_id": "F250",
    "report_id": "R018",
    "label": "Exhibit 12",
    "context": "EXHIBIT 12: InferRead is Infervision's multi-faceted medical imaging solution A multi-faceted medical imaging solution series InferRead®'s full range of solutions covers assisted diagnosis for, but is not limited to, cancers, infe"
  },
  {
    "figure_id": "F251",
    "report_id": "R018",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: SpectraWave provides AI-enabled, automated Imaging solutions AI-ENABLED, AUTOMATED Lipid Calcium EEL Diameter"
  },
  {
    "figure_id": "F252",
    "report_id": "R020",
    "label": "Figure 1",
    "context": "Figure 1: Eaton's MV SST 2.0 launched in IDCE 2026 Exterior view of a large industrial control room with multiple panels and control panels (no visible text or symbols)"
  },
  {
    "figure_id": "F253",
    "report_id": "R020",
    "label": "Figure 2",
    "context": "Figure 2: TGOOD's AI PowerHouse Exterior view of a modern industrial building with green and white facade signage, featuring a large 'Xingtong' logo and Chinese text on the facade (no other signage visible)"
  },
  {
    "figure_id": "F254",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Doubao Study DAU growth accelerated to +146% yoy as of May-end and sustained the position of the 6th largest AI native app in China in terms of DAUs DAUs of major AI apps as of Apr-end"
  },
  {
    "figure_id": "F255",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Gauth has outperformed global AI-native education peers in terms of MAUs MAUs by AI education apps (mn)"
  },
  {
    "figure_id": "F256",
    "report_id": "R022",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Doubao Study continued to expand time spent market share among major K-12 learning tool/study companion apps in May Time spent share among major K-12 learning tool/study companion apps Exhibit 4: Gauth achieved c.US\\$1"
  },
  {
    "figure_id": "F257",
    "report_id": "R022",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Doubao Study continued to expand time spent market share among major K-12 learning tool/study companion apps in May Time spent share among major K-12 learning tool/study companion apps Exhibit 4: Gauth achieved c.US\\$1"
  },
  {
    "figure_id": "F258",
    "report_id": "R022",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Gauth monthly billings per avg. DAU grew +39% yoy to US\\$0.4 in May (vs. +49% yoy in Apr) Gauth monthly billings (US\\$ mn) and monthly billings per avg. DAU (US\\$)"
  },
  {
    "figure_id": "F259",
    "report_id": "R022",
    "label": "Exhibit 6",
    "context": "Exhibit 6: MAU growth of Xueersi.com grew +10% yoy in May (vs. +22% yoy in Apr) MAU yoy growth of major tutoring platforms (%)"
  },
  {
    "figure_id": "F260",
    "report_id": "R022",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Xueersi.com and TAL still led MAU yoy growth within non-academic tutoring in May MAUs of major non-academic tutoring platforms (mn)"
  },
  {
    "figure_id": "F261",
    "report_id": "R022",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Not-for-profit subject tutoring platforms: Combined MAUs dropped -26% yoy in May (vs. -21% yoy in Apr) MAUs of not-for-profit subject tutoring platforms"
  },
  {
    "figure_id": "F262",
    "report_id": "R022",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Not-for-profit subject tutoring platforms: Total time spent dropped -33% yoy in May (vs. -21% yoy in Apr)"
  },
  {
    "figure_id": "F263",
    "report_id": "R022",
    "label": "Exhibit 10",
    "context": "GMV: Combined GMV of 6 major learning device brands dropped -35% yoy or increased +46% mom in May (vs. -2% yoy/-47% mom in Apr) on Douyin/Taobao/Tmall/JD. By brand, GMV of (+) Yuanfudao increased +31% yoy in May, while (-) iFlytek/TAL/Xiaodu/BBK/Zuoyebang drop"
  },
  {
    "figure_id": "F264",
    "report_id": "R022",
    "label": "Exhibit 11",
    "context": "TAL's quarterly online GMV on major eCommerce platforms"
  },
  {
    "figure_id": "F265",
    "report_id": "R022",
    "label": "Exhibit 15",
    "context": "User engagement: MAUs of major education device brands grew +42% yoy/+4% mom to c.16.7mn in May (vs. +47% yoy/-6% mom in Apr). For TAL, MAUs of the Xueersi Smart app grew +100% yoy/+6% mom to c.3.6mn in May (vs. +117% yoy/-5% mom in Apr). MAUs of smart educati"
  },
  {
    "figure_id": "F266",
    "report_id": "R022",
    "label": "Exhibit 16",
    "context": "Exhibit 16: For TAL, MAUs of the Xueersi Smart app grew +100% yoy/+6% mom to c.3.6mn in May (vs. +117% yoy/-5% mom in Apr)"
  },
  {
    "figure_id": "F267",
    "report_id": "R022",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Breakdown of after-school tutoring licenses (May 2026) Exhibit 18: The number of offline non-academic tutoring licenses further dropped -0.2% mom in May (vs. -0.2% mom in Apr)..."
  },
  {
    "figure_id": "F268",
    "report_id": "R022",
    "label": "Exhibit 19",
    "context": "Exhibit 19: ...while offline licensed subject tutoring supply dropped -0.1% mom in May (vs. -0.4% mom in Apr)"
  },
  {
    "figure_id": "F269",
    "report_id": "R022",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Student visas # granted to Chinese for Canada, Australia, and UK combined dropped -9% yoy in 1Q26"
  },
  {
    "figure_id": "F270",
    "report_id": "R022",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Canada student visas granted to Chinese dropped -34% yoy in Mar (vs. +29% yoy in Feb) Canada student permit holders from China"
  },
  {
    "figure_id": "F271",
    "report_id": "R022",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Chinese student visas issued by Australia declined -5% yoy in 1Q26, while those issued by the UK/Canada dropped -10%/-17% yoy % change of student visas # granted to Chinese"
  },
  {
    "figure_id": "F272",
    "report_id": "R022",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Australia student visas granted to Chinese increased +24% yoy in Apr (vs. -5% yoy in Mar) Australia student visas granted to Chinese"
  },
  {
    "figure_id": "F273",
    "report_id": "R022",
    "label": "Exhibit 24",
    "context": "Exhibit 24: UK student visas granted to Chinese dropped -10% yoy in 1Q26 (vs. -11% yoy in 4Q25) UK student permit holders from China"
  },
  {
    "figure_id": "F274",
    "report_id": "R022",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Duolingo maintained its leading position among language learning apps in China by MAU in May, likely driven by non-English learning demand MAUs of major language learning apps in China"
  },
  {
    "figure_id": "F275",
    "report_id": "R022",
    "label": "Exhibit 26",
    "context": "Exhibit 26: East Buy monthly GMV on Douyin grew +38% yoy/+7% mom to c.Rmb1.03bn in May (vs. +42% yoy/-10% mom in Apr) East Buy monthly GMV on Douyin (Rmb mn)"
  },
  {
    "figure_id": "F276",
    "report_id": "R022",
    "label": "Exhibit 28",
    "context": "Exhibit 28: East Buy's GMV from 1P products increased to $29\\%$ in May (vs. $28\\%$ in Apr) East Buy's GMV by 1P/3P"
  },
  {
    "figure_id": "F277",
    "report_id": "R022",
    "label": "Exhibit 27",
    "context": "Exhibit 27: East Buy GMV from new platforms grew +246% yoy in May (vs. +183% yoy in Apr), while GMV from the original platforms dropped -2% yoy in May (vs. +7% yoy in Apr) East Buy GMV by original platforms and new platforms (Rmb mn"
  },
  {
    "figure_id": "F278",
    "report_id": "R022",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Avg. live viewers per stream by major Douyin accounts"
  },
  {
    "figure_id": "F279",
    "report_id": "R022",
    "label": "Exhibit 30",
    "context": "Exhibit 30: East Buy app MAUs increased +38% yoy or dropped -7% mom in May (vs. +42% yoy/-1% mom in Apr)"
  },
  {
    "figure_id": "F280",
    "report_id": "R023",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Trucks, O&G, Telecom and Consumer/F&B show favorable capex environment, although some have overcapacity constraints"
  },
  {
    "figure_id": "F281",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We see Renewables, Transmission, Datacenters and Semiconductors as structural growth areas GS Capex Tracker by end market"
  },
  {
    "figure_id": "F282",
    "report_id": "R023",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We expect 2026 capex to be well above the historical trend growth GS General Industrial Capex Tracker (4k companies, €3.1tn worth of capex)"
  },
  {
    "figure_id": "F283",
    "report_id": "R023",
    "label": "Exhibit 6",
    "context": "Exhibit 6: US utilisation trends stronger, while Europe stays flat and China declines"
  },
  {
    "figure_id": "F284",
    "report_id": "R023",
    "label": "Exhibit 8",
    "context": "Exhibit 8: We see a concentration of growth in a small number of areas all related to datacenters, semis and utilities, now representing c.39% of total capex... End-market size implied by our Capex Tracker, 2026"
  },
  {
    "figure_id": "F285",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ....versus only 22% just 4 years ago End-Market Size implied by our Capex Tracker, 2022"
  },
  {
    "figure_id": "F286",
    "report_id": "R023",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We continue to see capex growth in 2026/27 at historical highs GS General Industrial Capex Tracker (c.4k companies, €3.4 tn of capex in 2026) (adjusted Throughcycle)\\*"
  },
  {
    "figure_id": "F287",
    "report_id": "R023",
    "label": "Exhibit 12",
    "context": "Exhibit 12: General Industrial Capex/Depreciation remains above median levels in 2026 General Industrial Capex/Depreciation"
  },
  {
    "figure_id": "F288",
    "report_id": "R023",
    "label": "Exhibit 11",
    "context": "Exhibit 11: General Industrial Capex/Sales remains slightly above median levels in 2026 General Industrial Capex/Sales"
  },
  {
    "figure_id": "F289",
    "report_id": "R023",
    "label": "Exhibit 13",
    "context": "Exhibit 13: We expect 2026 to end 13% above the historical peak (2025) GS General Industrial Capex Tracker (indexed)"
  },
  {
    "figure_id": "F290",
    "report_id": "R023",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Manufacturing capacity utilization slightly below history in EU and China Average Capacity Utilization (EU, China)"
  },
  {
    "figure_id": "F291",
    "report_id": "R023",
    "label": "Exhibit 15",
    "context": "Exhibit 15: We now expect +4% O&G capex growth from flat previously GS Oil & Gas Capex Tracker (255 companies, €450 bn of capex in 2026)"
  },
  {
    "figure_id": "F292",
    "report_id": "R023",
    "label": "Exhibit 16",
    "context": "Exhibit 16: O&G Capex/Sales is expected to stabilize in 2026, but levels remain below the historical median O&G Capex/Sales"
  },
  {
    "figure_id": "F293",
    "report_id": "R023",
    "label": "Exhibit 17",
    "context": "Exhibit 17: O&G Capex/Depreciation is likely to remain well below median levels in 2026 O&G Capex/Depreciation"
  },
  {
    "figure_id": "F294",
    "report_id": "R023",
    "label": "Exhibit 19",
    "context": "Exhibit 19: O&G equipment age is at peak levels Average Age of O&G Equipment (US)"
  },
  {
    "figure_id": "F295",
    "report_id": "R023",
    "label": "Exhibit 18",
    "context": "Exhibit 18: We expect 2026 to end 4% above the historical peak (2025) GS O&G Capex Tracker (indexed)"
  },
  {
    "figure_id": "F296",
    "report_id": "R023",
    "label": "Exhibit 20",
    "context": "Exhibit 20: O&G capacity utilization is slightly higher than median levels in US/EU and China Average Capacity Utilization (US, EU, China)"
  },
  {
    "figure_id": "F297",
    "report_id": "R023",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We see strong technology capex upgrades into 2026 and outer years GS Tech Capex Tracker (177 companies, €984 bn of capex in 2026)"
  },
  {
    "figure_id": "F298",
    "report_id": "R023",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Tech Capex/Depreciation is likely to remain above median levels in 2026 Tech Capex/Depreciation"
  },
  {
    "figure_id": "F299",
    "report_id": "R023",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Tech Capex/Sales remains well above median levels Tech Capex/Sales"
  },
  {
    "figure_id": "F300",
    "report_id": "R023",
    "label": "Exhibit 24",
    "context": "Exhibit 24: We expect 2026 to end 62% higher vs the historical peak (2025) GS Tech Capex Tracker (indexed)"
  },
  {
    "figure_id": "F301",
    "report_id": "R023",
    "label": "Exhibit 25",
    "context": "Exhibit 25: We see datacenter capex growth rates remaining at double digits in 2026 and 2027 GS Datacenter Capex Tracker (63 companies, €695 bn of capex in 2026)"
  },
  {
    "figure_id": "F302",
    "report_id": "R023",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Datacenters Capex/Depreciation is expected to remain above median levels in 2026 Datacenters Capex/Depreciation"
  },
  {
    "figure_id": "F303",
    "report_id": "R023",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Datacenters Capex/Sales remains well above median levels Datacenters Capex/Sales"
  },
  {
    "figure_id": "F304",
    "report_id": "R023",
    "label": "Exhibit 28",
    "context": "Exhibit 28: We expect 2026 to end 79% higher vs the historical peak (2025) GS Datacenters Capex Tracker (indexed)"
  },
  {
    "figure_id": "F305",
    "report_id": "R023",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Datacenters capacity utilization below median levels Average Capacity Utilization (US)"
  },
  {
    "figure_id": "F306",
    "report_id": "R023",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Semis capex has seen some upgrades in 2026 GS Semiconductor Capex Tracker (39 companies, €200 bn of capex in 2026)"
  },
  {
    "figure_id": "F307",
    "report_id": "R023",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Semis Capex/Sales is expected to be below median levels in 2026 Semiconductors Capex/Sales"
  },
  {
    "figure_id": "F308",
    "report_id": "R023",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Semis Capex/Depreciation is expected to remain above the median in 2026 Semiconductors Capex/Depreciation"
  },
  {
    "figure_id": "F309",
    "report_id": "R023",
    "label": "Exhibit 33",
    "context": "Exhibit 33: We expect 2026 to end 41% above vs the historical peak (2025) GS Semis Capex Tracker (indexed)"
  },
  {
    "figure_id": "F310",
    "report_id": "R023",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Semis capacity utilization is below median levels Average Capacity Utilization"
  },
  {
    "figure_id": "F311",
    "report_id": "R023",
    "label": "Exhibit 35",
    "context": "Exhibit 35: The energy transition and data center expected boom are contributing to high investments in power generation in medium term GS Conventional Power Generation Capex Tracker (115 companies, €350 bn of capex in 2026)"
  },
  {
    "figure_id": "F312",
    "report_id": "R023",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Conventional Power Generation Capex/Depreciation is likely to remain above median levels in 2026 Conventional Power Generation Capex/Depreciation"
  },
  {
    "figure_id": "F313",
    "report_id": "R023",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Conventional Power Generation Capex/Sales is likely to remain above median levels in 2026 Conventional Power Generation Capex/Sales"
  },
  {
    "figure_id": "F314",
    "report_id": "R023",
    "label": "Exhibit 38",
    "context": "Exhibit 38: We expect 2026 to end 22% above the historical peak (2025) GS Conventional Power Generation Capex Tracker (indexed)"
  },
  {
    "figure_id": "F315",
    "report_id": "R023",
    "label": "Exhibit 39",
    "context": "Exhibit 39: The average age of utilities equipment looks extended vs history Average Age of Utilities Equipment (US)"
  },
  {
    "figure_id": "F316",
    "report_id": "R023",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Utilities utilization rate has been decreasing and is well below the median levels Average Capacity Utilization (US and EU)"
  },
  {
    "figure_id": "F317",
    "report_id": "R023",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Energy transition spending remains a growth driver, though capex growth moderates in outer years GS Renewables Capex Tracker (15 companies, €43 bn of capex in 2026)"
  },
  {
    "figure_id": "F318",
    "report_id": "R023",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Renewables and T&D Capex/Sales is likely to be above all historical levels in 2026 Renewables and T&D Capex/Sales"
  },
  {
    "figure_id": "F319",
    "report_id": "R023",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Renewables and T&D Capex/Depreciation is trending above median levels in 2026 Renewables and T&D Capex/Depreciation"
  },
  {
    "figure_id": "F320",
    "report_id": "R023",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Transmission capex remains supported by grid modernization needs despite moderating growth GS Transmission Capex Tracker (9 companies, €32 bn of capex in 2026)"
  },
  {
    "figure_id": "F321",
    "report_id": "R023",
    "label": "Exhibit 44",
    "context": "Exhibit 44: We expect 2026 to end 22% above the historical peak (2025) GS Renewables and T&D Capex Tracker (indexed)"
  },
  {
    "figure_id": "F322",
    "report_id": "R023",
    "label": "Exhibit 46",
    "context": "Exhibit 46: We expect 2026 to end 21% above the historical peak (2025) GS Transmission Capex Tracker (indexed)"
  },
  {
    "figure_id": "F323",
    "report_id": "R023",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Telecom capex has seen slight downgrades in 2026 GS Telecom Capex Tracker (114 companies, €201 bn of capex in 2026)"
  },
  {
    "figure_id": "F324",
    "report_id": "R023",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Telecom Capex/Depreciation is likely to be below median levels in 2026 Telecom Capex/Depreciation"
  },
  {
    "figure_id": "F325",
    "report_id": "R023",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Telecom Capex/Sales is on track to remain well below median levels in 2026 Telecom Capex/Sales"
  },
  {
    "figure_id": "F326",
    "report_id": "R023",
    "label": "Exhibit 50",
    "context": "Exhibit 50: We expect 2026 to end 6% below the historical peak (2022) GS Telecom Capex Tracker (indexed)"
  },
  {
    "figure_id": "F327",
    "report_id": "R023",
    "label": "Exhibit 51",
    "context": "Exhibit 51: US telecom equipment slightly above the historical median age Average Age of Telecom Equipment (US)"
  },
  {
    "figure_id": "F328",
    "report_id": "R023",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Capex growth in Consumer is expected to remain positive but grow at a much slower rate than the first few years post covid GS Consumer Capex Tracker (490 companies, €205 bn of capex in 2026)"
  },
  {
    "figure_id": "F329",
    "report_id": "R023",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Consumer Capex/Depreciation should remain slightly below median level in 2026 Consumer Capex/Depreciation"
  },
  {
    "figure_id": "F330",
    "report_id": "R023",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Consumer Capex/Sales is expected slightly below median levels in 2026 Consumer Capex/Sales"
  },
  {
    "figure_id": "F331",
    "report_id": "R023",
    "label": "Exhibit 55",
    "context": "Exhibit 55: We expect 2026 to end 5% above the historical peak (2024) GS Consumer Capex tracker (indexed)"
  },
  {
    "figure_id": "F332",
    "report_id": "R023",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Retail capex has seen a modest increase this year but the current macro uncertainty challenges 2027 GS Retail Capex Tracker (241 companies, €128 bn of capex in 2026)"
  },
  {
    "figure_id": "F333",
    "report_id": "R023",
    "label": "Exhibit 57",
    "context": "Exhibit 57: We expect 2026 to end 8% above the historical peak (2025) GS Retail Capex Tracker (indexed)"
  },
  {
    "figure_id": "F334",
    "report_id": "R023",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Retail capacity utilization is below median levels in US, EU and China Average Capacity Utilization (US, EU, China)"
  },
  {
    "figure_id": "F335",
    "report_id": "R023",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Food & Beverage capex has seen some downgrades for medium-term capex vs our Feb update GS Food & Beverage Capex Tracker (213 companies, €71 bn of capex in 2026)"
  },
  {
    "figure_id": "F336",
    "report_id": "R023",
    "label": "Exhibit 60",
    "context": "Exhibit 60: We expect 2026 to end 3% below the historical peak (2024) GS F&B Capex Tracker (indexed)"
  },
  {
    "figure_id": "F337",
    "report_id": "R023",
    "label": "Exhibit 61",
    "context": "Exhibit 61: F&B equipment age is slightly above historical median level Average Age of F&B Equipment (US)"
  },
  {
    "figure_id": "F338",
    "report_id": "R023",
    "label": "Exhibit 62",
    "context": "Exhibit 62: F&B capacity utilization is declining but remains at median levels Average Capacity Utilization (US, EU)"
  },
  {
    "figure_id": "F339",
    "report_id": "R023",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Food capex shows sustained growth momentum beyond 2025 GS Food Capex Tracker (116 companies, €32 bn of capex in 2026)"
  },
  {
    "figure_id": "F340",
    "report_id": "R023",
    "label": "Exhibit 65",
    "context": "Exhibit 65: Food Capex/Depreciation is expected to be below median levels in 2026 Food Capex/Depreciation"
  },
  {
    "figure_id": "F341",
    "report_id": "R023",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Food Capex/Sales is expected to be below median levels in 2026 Food Capex/Sales"
  },
  {
    "figure_id": "F342",
    "report_id": "R023",
    "label": "Exhibit 66",
    "context": "Exhibit 66: We expect 2026 to end 7% below the historical peak (2013) GS Food Capex Tracker (indexed)"
  },
  {
    "figure_id": "F343",
    "report_id": "R023",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Beverage investment outlook points to a 2025 trough and subsequent cyclical recovery GS Beverage Capex Tracker (69 companies, €34 bn of capex in 2026)"
  },
  {
    "figure_id": "F344",
    "report_id": "R023",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Beverage Capex/Depreciation is expected to be at median levels in 2026 Beverage Capex/Depreciation"
  },
  {
    "figure_id": "F345",
    "report_id": "R023",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Beverage Capex/Sales is expected to be slightly below median levels in 2026 Beverage Capex/Sales"
  },
  {
    "figure_id": "F346",
    "report_id": "R023",
    "label": "Exhibit 70",
    "context": "Exhibit 70: We expect 2026 to end 5% below the historical peak (2024) GS Beverage Capex Tracker (indexed)"
  },
  {
    "figure_id": "F347",
    "report_id": "R023",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Dairy capex expected to decline from 2025 highs and stabilize thereafter GS Dairy Capex Tracker (28 companies, €5 bn of capex in 2026)"
  },
  {
    "figure_id": "F348",
    "report_id": "R023",
    "label": "Exhibit 73",
    "context": "Exhibit 73: Dairy Capex/Depreciation is expected to be below median levels in 2026 Dairy Capex/Depreciation"
  },
  {
    "figure_id": "F349",
    "report_id": "R023",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Dairy Capex/Sales is expected to be below median levels in 2026 Dairy Capex/Sales"
  },
  {
    "figure_id": "F350",
    "report_id": "R023",
    "label": "Exhibit 74",
    "context": "Exhibit 74: We expect 2026 to end 9% below the historical peak (2014) GS Dairy Capex Tracker (indexed)"
  },
  {
    "figure_id": "F351",
    "report_id": "R023",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Vehicles Capex growth seems set to recover medium term from lows of 2025, but saw further downgrades in 2026 GS Vehicles Capex Tracker (106 companies, €171 bn of capex in 2026)"
  },
  {
    "figure_id": "F352",
    "report_id": "R023",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Vehicles Capex/Depreciation is seen declining to median levels in 2026 Vehicle Capex/Depreciation"
  },
  {
    "figure_id": "F353",
    "report_id": "R023",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Vehicles Capex/Sales is expected to be at median levels in 2026 Vehicles Capex/Sales"
  },
  {
    "figure_id": "F354",
    "report_id": "R023",
    "label": "Exhibit 78",
    "context": "Exhibit 78: We expect 2026 to end 1% below the historical peak (2024) GS Vehicles Capex Tracker (Indexed)"
  },
  {
    "figure_id": "F355",
    "report_id": "R023",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Vehicle age in the US is at an all-time high Average Age of Vehicle Equipment (US)"
  },
  {
    "figure_id": "F356",
    "report_id": "R023",
    "label": "Exhibit 81",
    "context": "Exhibit 81: Mining Capex saw a meaningful rise in 2026, with moderation in the outer years GS Mining Capex Tracker (174 companies, €184 bn of capex in 2026)"
  },
  {
    "figure_id": "F357",
    "report_id": "R023",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Vehicles capacity utilization is below the median level Average Capacity Utilization (US, EU, China)"
  },
  {
    "figure_id": "F358",
    "report_id": "R023",
    "label": "Exhibit 82",
    "context": "Exhibit 82: Mining Capex/Sales is expected to remain at the median level in 2026 Mining Capex/Sales"
  },
  {
    "figure_id": "F359",
    "report_id": "R023",
    "label": "Exhibit 83",
    "context": "Exhibit 83: Mining Capex/Depreciation is expected above median levels in 2026 Mining Capex/Depreciation"
  },
  {
    "figure_id": "F360",
    "report_id": "R023",
    "label": "Exhibit 85",
    "context": "Exhibit 85: Mining equipment age is above the long-run average Average Age of Mining Equipment (US)"
  },
  {
    "figure_id": "F361",
    "report_id": "R023",
    "label": "Exhibit 84",
    "context": "Exhibit 84: We expect 2026 to end 11% below the historical peak (2012) GS Mining Capex Tracker (indexed)"
  },
  {
    "figure_id": "F362",
    "report_id": "R023",
    "label": "Exhibit 86",
    "context": "Exhibit 86: Mining capacity utilization has been on a downward trend Average Capacity Utilization (US, China)"
  },
  {
    "figure_id": "F363",
    "report_id": "R023",
    "label": "Exhibit 87",
    "context": "Exhibit 87: We are seeing copper capex upgrades into 2026 and outer years GS Mining Capex Tracker (26 companies, €42 bn of capex in 2026)"
  },
  {
    "figure_id": "F364",
    "report_id": "R023",
    "label": "Exhibit 89",
    "context": "Exhibit 89: Chemicals capex has been cut for outer years GS Chemicals Capex Tracker (98 companies, €90 bn of capex in 2026)"
  },
  {
    "figure_id": "F365",
    "report_id": "R023",
    "label": "Exhibit 88",
    "context": "Exhibit 88: We expect 2026 to end 7% above the historical peak (2024) GS Copper Capex Tracker (indexed)"
  },
  {
    "figure_id": "F366",
    "report_id": "R023",
    "label": "Exhibit 90",
    "context": "Exhibit 90: Chemicals Capex/Sales is falling below median levels in 2026 Chemicals Capex/Sales"
  },
  {
    "figure_id": "F367",
    "report_id": "R023",
    "label": "Exhibit 91",
    "context": "Exhibit 91: Chemicals Capex/Depreciation is trending below median levels in 2026 Chemicals Capex/Depreciation"
  },
  {
    "figure_id": "F368",
    "report_id": "R023",
    "label": "Exhibit 93",
    "context": "Exhibit 93: Age of Chemical equipment in the US is above history Average Age of Chemical Equipment (US)"
  },
  {
    "figure_id": "F369",
    "report_id": "R023",
    "label": "Exhibit 92",
    "context": "Exhibit 92: We expect 2026 to end 24% below the historical peak (2024) GS Chemicals Capex Tracker (indexed)"
  },
  {
    "figure_id": "F370",
    "report_id": "R023",
    "label": "Exhibit 94",
    "context": "Exhibit 94: Chemicals capacity utilization is below median levels Average Capacity Utilization (US, EU, China)"
  },
  {
    "figure_id": "F371",
    "report_id": "R023",
    "label": "Exhibit 95",
    "context": "Exhibit 95: Airlines capex remains in line with our previous Feb update GS Airlines Capex Tracker (107 companies, €89 bn of capex in 2026)"
  },
  {
    "figure_id": "F372",
    "report_id": "R023",
    "label": "Exhibit 97",
    "context": "Exhibit 97: Airlines Capex/Depreciation is seen below median levels in 2026 Airlines Capex/Depreciation"
  },
  {
    "figure_id": "F373",
    "report_id": "R023",
    "label": "Exhibit 96",
    "context": "Exhibit 96: Airlines Capex/Sales is expected to fall below the median levels in 2026 Airlines Capex/Sales"
  },
  {
    "figure_id": "F374",
    "report_id": "R023",
    "label": "Exhibit 98",
    "context": "Exhibit 98: We expect 2026 to end 12% below the historical peak (2018) GS Airlines Capex Tracker (indexed)"
  },
  {
    "figure_id": "F375",
    "report_id": "R023",
    "label": "Exhibit 99",
    "context": "Exhibit 99: The age of Airlines equipment is at all-time highs Average Age of Airline Equipment (US)"
  },
  {
    "figure_id": "F376",
    "report_id": "R023",
    "label": "Exhibit 101",
    "context": "Exhibit 101: Our pharma capex expectations for 2026 have increased sharply vs previous update GS Pharma Capex Tracker (124 companies, €58 bn of capex in 2026)"
  },
  {
    "figure_id": "F377",
    "report_id": "R023",
    "label": "Exhibit 100",
    "context": "Exhibit 100: Airlines capacity utilization is increasing and approaching median levels Average Capacity Utilization (US)"
  },
  {
    "figure_id": "F378",
    "report_id": "R023",
    "label": "Exhibit 102",
    "context": "Exhibit 102: Pharma Capex/Sales is expected to be at median levels in 2026 Pharma Capex/Sales"
  },
  {
    "figure_id": "F379",
    "report_id": "R023",
    "label": "Exhibit 103",
    "context": "Exhibit 103: Pharma Capex/Depreciation is above the median levels in 2026 but decelerating Pharma Capex/Depreciation"
  },
  {
    "figure_id": "F380",
    "report_id": "R023",
    "label": "Exhibit 104",
    "context": "Exhibit 104: We expect 2025 to end 4% above the historical peak (2025) GS Pharma Capex Tracker (indexed)"
  },
  {
    "figure_id": "F381",
    "report_id": "R023",
    "label": "Exhibit 105",
    "context": "Exhibit 105: Pharma capacity utilization in EU is recovering but well below the median Average Capacity Utilization (EU, China)"
  },
  {
    "figure_id": "F382",
    "report_id": "R023",
    "label": "Exhibit 106",
    "context": "Exhibit 106: We expect Construction Equipment capex has seen steady cuts for 2026 on rates uncertainty GS Construction Equipment Capex Tracker (46 companies, €46 bn of capex in 2026)"
  },
  {
    "figure_id": "F383",
    "report_id": "R023",
    "label": "Exhibit 108",
    "context": "Exhibit 108: Construction Equipment Capex/Depreciation is seen below median levels in 2026 Construction Equipment Capex/Depreciation"
  },
  {
    "figure_id": "F384",
    "report_id": "R023",
    "label": "Exhibit 107",
    "context": "Exhibit 107: Construction Equipment Capex/Sales is seen below median levels in 2026 Construction Equipment Capex/Sales"
  },
  {
    "figure_id": "F385",
    "report_id": "R023",
    "label": "Exhibit 109",
    "context": "Exhibit 109: We expect 2026 to end 45% below the historical peak (2006) GS CE Capex Tracker (indexed)"
  },
  {
    "figure_id": "F386",
    "report_id": "R023",
    "label": "Exhibit 110",
    "context": "Exhibit 110: Construction equipment age is declining, implying less need for investment Average Age of Construction Equipment (US)"
  },
  {
    "figure_id": "F387",
    "report_id": "R023",
    "label": "Exhibit 112",
    "context": "Exhibit 112: We have seen capex being trimmed for rail over recent months, but still expect outer years to see a growth recovery on the back of stimulus programs GS Rail Capex Tracker (41 companies, €38 bn of capex in 2026) Exhibit"
  },
  {
    "figure_id": "F388",
    "report_id": "R023",
    "label": "Exhibit 112",
    "context": "Exhibit 112: We have seen capex being trimmed for rail over recent months, but still expect outer years to see a growth recovery on the back of stimulus programs GS Rail Capex Tracker (41 companies, €38 bn of capex in 2026) Exhibit"
  },
  {
    "figure_id": "F389",
    "report_id": "R023",
    "label": "Exhibit 113",
    "context": "Exhibit 113: Rail Capex/Sales remains slightly below median levels in 2026 Rail Capex/Sales"
  },
  {
    "figure_id": "F390",
    "report_id": "R023",
    "label": "Exhibit 114",
    "context": "Exhibit 114: Rail Capex/Depreciation is seen below median levels in 2026 Rail Capex/Depreciation"
  },
  {
    "figure_id": "F391",
    "report_id": "R023",
    "label": "Exhibit 116",
    "context": "Exhibit 116: Average age of US rail equipment is well below the historical median Average Age of Rail Equipment (US)"
  },
  {
    "figure_id": "F392",
    "report_id": "R023",
    "label": "Exhibit 115",
    "context": "Exhibit 115: We expect 2026 to end 3% below the historical peak (2025) GS Rail Capex Tracker (indexed)"
  },
  {
    "figure_id": "F393",
    "report_id": "R023",
    "label": "Exhibit 117",
    "context": "Exhibit 117: Rail utilization rates are below, but close to, historical levels Average Capacity Utilization (US)"
  },
  {
    "figure_id": "F394",
    "report_id": "R023",
    "label": "Exhibit 118",
    "context": "Exhibit 118: REITs capex forecasts show lower spending in 2026 REIT Capex Tracker (130 companies, €37 bn of capex in 2026)"
  },
  {
    "figure_id": "F395",
    "report_id": "R023",
    "label": "Exhibit 120",
    "context": "Exhibit 120: REIT Capex/Depreciation is expected to remain below median levels in 2026 REIT Capex/Depreciation"
  },
  {
    "figure_id": "F396",
    "report_id": "R023",
    "label": "Exhibit 119",
    "context": "Exhibit 119: REIT Capex/Sales is seen well below median levels REIT Capex/Sales"
  },
  {
    "figure_id": "F397",
    "report_id": "R023",
    "label": "Exhibit 121",
    "context": "Exhibit 121: We expect 2026 to end 95% below the historical peak (2002) GS REIT Capex Tracker (Indexed)"
  },
  {
    "figure_id": "F398",
    "report_id": "R023",
    "label": "Exhibit 122",
    "context": "Exhibit 122: The age of real REIT assets is around the historical levels Average Age of real estate assets (US)"
  },
  {
    "figure_id": "F399",
    "report_id": "R023",
    "label": "Exhibit 123",
    "context": "Exhibit 123: Marine capex shows slight increase going into 2026 GS Marine Capex Tracker (32 companies, €34 bn capex in 2026)"
  },
  {
    "figure_id": "F400",
    "report_id": "R023",
    "label": "Exhibit 125",
    "context": "Exhibit 125: Marine Capex/Depreciation is seen slightly above median levels in 2026 Marine Capex/Depreciation"
  },
  {
    "figure_id": "F401",
    "report_id": "R023",
    "label": "Exhibit 124",
    "context": "Exhibit 124: Marine Capex/Sales is expected to remain above median levels in 2026 Marine Capex/Sales"
  },
  {
    "figure_id": "F402",
    "report_id": "R023",
    "label": "Exhibit 126",
    "context": "Exhibit 126: We expect 2026 to end 3% below the historical peak (2008) as the last peak was characterized by significant overcapacity GS Marine Capex Tracker (indexed)"
  },
  {
    "figure_id": "F403",
    "report_id": "R023",
    "label": "Exhibit 127",
    "context": "Exhibit 127: Marine equipment average age is slightly above historical levels Average age of marine equipment (US)"
  },
  {
    "figure_id": "F404",
    "report_id": "R023",
    "label": "Exhibit 129",
    "context": "Exhibit 129: Cruise capex remains resilient following 2025 investment peak GS Marine Capex Tracker (4 companies, €10 bn capex in 2026)"
  },
  {
    "figure_id": "F405",
    "report_id": "R023",
    "label": "Exhibit 128",
    "context": "Exhibit 128: Marine capacity utilization is slightly below median levels Average Capacity Utilization"
  },
  {
    "figure_id": "F406",
    "report_id": "R023",
    "label": "Exhibit 130",
    "context": "Exhibit 130: Cruise Capex/Sales is expected to remain at median levels in 2026 Cruise Capex/Sales"
  },
  {
    "figure_id": "F407",
    "report_id": "R023",
    "label": "Exhibit 131",
    "context": "Exhibit 131: Cruise Capex/Depreciation is seen above median levels in 2026 Cruise Capex/Depreciation"
  },
  {
    "figure_id": "F408",
    "report_id": "R023",
    "label": "Exhibit 132",
    "context": "Exhibit 132: We expect 2026 to end 1% below the historical peak (2009) GS Cruise Capex Tracker (indexed)"
  },
  {
    "figure_id": "F409",
    "report_id": "R023",
    "label": "Exhibit 133",
    "context": "Exhibit 133: Cruise capacity utilization is at the median levels Average Capacity Utilization"
  },
  {
    "figure_id": "F410",
    "report_id": "R023",
    "label": "Exhibit 134",
    "context": "Exhibit 134: Merchant capex expected to trough in 2026 before recovering and moderating thereafter GS Merchant Capex Tracker (22 companies, €23 bn capex in 2026)"
  },
  {
    "figure_id": "F411",
    "report_id": "R023",
    "label": "Exhibit 136",
    "context": "Exhibit 136: Merchant Capex/Depreciation is seen slightly above median levels in 2026 Merchant Capex/Depreciation"
  },
  {
    "figure_id": "F412",
    "report_id": "R023",
    "label": "Exhibit 135",
    "context": "Exhibit 135: Merchant Capex/Sales is expected to remain above median levels in 2026 Merchant Capex/Sales"
  },
  {
    "figure_id": "F413",
    "report_id": "R023",
    "label": "Exhibit 137",
    "context": "Exhibit 137: We expect 2026 to end 3% above the historical peak (2025) GS Merchant Capex Tracker (indexed)"
  },
  {
    "figure_id": "F414",
    "report_id": "R023",
    "label": "Exhibit 138",
    "context": "Exhibit 138: Merchant capacity utilization is slightly below median levels Average Capacity Utilization"
  },
  {
    "figure_id": "F415",
    "report_id": "R023",
    "label": "Exhibit 139",
    "context": "Exhibit 139: LNG/Offshore capex expected to flatten during the outer years GS LNG/Offshore Capex Tracker (6 companies, €2 bn capex in 2026)"
  },
  {
    "figure_id": "F416",
    "report_id": "R023",
    "label": "Exhibit 140",
    "context": "Exhibit 140: LNG Capex/Sales is expected to remain above median levels in 2026 LNG Capex/Sales"
  },
  {
    "figure_id": "F417",
    "report_id": "R023",
    "label": "Exhibit 141",
    "context": "Exhibit 141: LNG Capex/Depreciation is seen slightly above median levels in 2026 LNG Capex/Depreciation"
  },
  {
    "figure_id": "F418",
    "report_id": "R023",
    "label": "Exhibit 142",
    "context": "Exhibit 142: We expect 2026 to end 56% below the historical peak (2006) GS Marine Capex Tracker (indexed)"
  },
  {
    "figure_id": "F419",
    "report_id": "R023",
    "label": "Exhibit 143",
    "context": "Exhibit 143: Ports capex is broadly unchanged vs our last update in February GS Ports Capex Tracker (37 companies, €23 bn of capex in 2026)"
  },
  {
    "figure_id": "F420",
    "report_id": "R023",
    "label": "Exhibit 145",
    "context": "Exhibit 145: Ports Capex/Depreciation is falling to median levels in 2026 Ports Capex/Depreciation"
  },
  {
    "figure_id": "F421",
    "report_id": "R023",
    "label": "Exhibit 144",
    "context": "Exhibit 144: Ports Capex/Sales is rising above median levels in 2026 Ports Capex/Sales"
  },
  {
    "figure_id": "F422",
    "report_id": "R023",
    "label": "Exhibit 146",
    "context": "Exhibit 146: We expect 2026 to end 30% below the historical peak (2008) GS Ports Capex Tracker (indexed)"
  },
  {
    "figure_id": "F423",
    "report_id": "R023",
    "label": "Exhibit 147",
    "context": "Exhibit 147: Trucking capex downgrades seem to have bottomed out and we see a pick-up into 2026 GS Truck Capex Tracker (35 companies, €17 bn of capex in 2026)"
  },
  {
    "figure_id": "F424",
    "report_id": "R023",
    "label": "Exhibit 149",
    "context": "Exhibit 149: Trucking Capex/Depreciation is seen below median levels in 2026 Trucking Capex/Depreciation"
  },
  {
    "figure_id": "F425",
    "report_id": "R023",
    "label": "Exhibit 148",
    "context": "Exhibit 148: Trucking Capex/Sales remains below median levels in 2026 Trucking Capex/Sales"
  },
  {
    "figure_id": "F426",
    "report_id": "R023",
    "label": "Exhibit 150",
    "context": "Exhibit 150: We expect 2026 to end 31% below the historical peak (2023) GS Trucking Capex tracker (indexed)"
  },
  {
    "figure_id": "F427",
    "report_id": "R023",
    "label": "Exhibit 151",
    "context": "Exhibit 151: Trucking equipment in the US is older than the historical median Average Age of Truck Equipment (US)"
  },
  {
    "figure_id": "F428",
    "report_id": "R023",
    "label": "Exhibit 153",
    "context": "Exhibit 153: The Capex Tracker indicates Pulp & Paper investments are set to pick up in the medium term GS Pulp & Paper Capex Tracker (40 companies, €18 bn of capex in 2026)"
  },
  {
    "figure_id": "F429",
    "report_id": "R023",
    "label": "Exhibit 152",
    "context": "Exhibit 152: Truck capacity utilization is above median levels North America Active Truck Utilization (\\%, SA)"
  },
  {
    "figure_id": "F430",
    "report_id": "R023",
    "label": "Exhibit 154",
    "context": "Exhibit 154: Pulp & Paper Capex/Sales is likely to fall to median levels in 2026 Pulp & Paper Capex/Sales"
  },
  {
    "figure_id": "F431",
    "report_id": "R023",
    "label": "Exhibit 155",
    "context": "Exhibit 155: Capex/Depreciation for Pulp & Paper is seen slightly below median levels in 2026 Pulp & Paper Capex/Depreciation"
  },
  {
    "figure_id": "F432",
    "report_id": "R023",
    "label": "Exhibit 157",
    "context": "Exhibit 157: Pulp & Paper equipment age is well above median levels Average age of Pulp & Paper equipment (US)"
  },
  {
    "figure_id": "F433",
    "report_id": "R023",
    "label": "Exhibit 156",
    "context": "Exhibit 156: We expect 2026 to end at 4% above the historical peak (2024) GS Pulp & Paper Capex Tracker (indexed)"
  },
  {
    "figure_id": "F434",
    "report_id": "R023",
    "label": "Exhibit 158",
    "context": "Exhibit 158: Pulp and Paper capacity utilization is well below median levels Average Capacity Utilization (US, EU)"
  },
  {
    "figure_id": "F435",
    "report_id": "R023",
    "label": "Exhibit 159",
    "context": "Exhibit 159: Our Healthcare Capex Tracker has seen upgrades in medium term GS Healthcare Capex Tracker (40 companies, €12 bn of capex in 2026)"
  },
  {
    "figure_id": "F436",
    "report_id": "R023",
    "label": "Exhibit 161",
    "context": "Exhibit 161: Healthcare Capex/Depreciation is seen below median levels in 2026 Healthcare Capex/Depreciation"
  },
  {
    "figure_id": "F437",
    "report_id": "R023",
    "label": "Exhibit 160",
    "context": "Exhibit 160: Healthcare Capex/Sales to remain below median levels in 2026 Healthcare Capex/Sales"
  },
  {
    "figure_id": "F438",
    "report_id": "R023",
    "label": "Exhibit 162",
    "context": "Exhibit 162: We expect 2026 to end 4% above the historical peak (2025) GS Healthcare Capex Tracker (Indexed)"
  },
  {
    "figure_id": "F439",
    "report_id": "R023",
    "label": "Exhibit 163",
    "context": "Exhibit 163: The age of Healthcare equipment in the US has been increasing for more than a decade Average Age of Healthcare Equipment (US)"
  },
  {
    "figure_id": "F440",
    "report_id": "R023",
    "label": "Exhibit 164",
    "context": "Exhibit 164: Airport capex is expected to see a weak 2026 GS Airports Capex Tracker (14 companies, €5 bn of capex in 2026)"
  },
  {
    "figure_id": "F441",
    "report_id": "R023",
    "label": "Exhibit 165",
    "context": "Exhibit 165: Airport Capex/Sales is seen below median levels in 2026 Airports Capex/Sales"
  },
  {
    "figure_id": "F442",
    "report_id": "R023",
    "label": "Exhibit 166",
    "context": "Exhibit 166: Airport Capex/Depreciation is expected to drop below median levels in 2026 Airports Capex/Depreciation"
  },
  {
    "figure_id": "F443",
    "report_id": "R023",
    "label": "Exhibit 168",
    "context": "Exhibit 168: Biotech capex to see downgrades during the medium term GS Biotech Capex Tracker (157 companies, €6 bn of capex in 2026)"
  },
  {
    "figure_id": "F444",
    "report_id": "R023",
    "label": "Exhibit 167",
    "context": "Exhibit 167: We expect 2026 to end 90% below the historical peak (2002) GS Airport Capex Tracker (indexed)"
  },
  {
    "figure_id": "F445",
    "report_id": "R023",
    "label": "Exhibit 169",
    "context": "Exhibit 169: Biotech Capex/Sales is seen below median levels in 2026 Biotech Capex/Sales"
  },
  {
    "figure_id": "F446",
    "report_id": "R023",
    "label": "Exhibit 170",
    "context": "Exhibit 170: Biotech Capex/Depreciation is expected to be below median levels in 2026 Biotech Capex/Depreciation"
  },
  {
    "figure_id": "F447",
    "report_id": "R023",
    "label": "Exhibit 171",
    "context": "Exhibit 171: We expect 2026 to end 90% below the historical peak (2004) GS Biotech Capex Tracker (indexed)"
  },
  {
    "figure_id": "F448",
    "report_id": "R023",
    "label": "Exhibit 172",
    "context": "Exhibit 172: ABB OSG vs Capex Tracker (R-Square: 63%)"
  },
  {
    "figure_id": "F449",
    "report_id": "R023",
    "label": "Exhibit 173",
    "context": "Exhibit 173: Alfa Laval OSG vs Capex Tracker (R-Square: 53%)"
  },
  {
    "figure_id": "F450",
    "report_id": "R023",
    "label": "Exhibit 174",
    "context": "Exhibit 174: Atlas Copco OSG vs Capex Tracker (R-Square: 76%)"
  },
  {
    "figure_id": "F451",
    "report_id": "R023",
    "label": "Exhibit 175",
    "context": "Exhibit 175: IMI OSG vs Capex Tracker (R-Square: 65%)"
  },
  {
    "figure_id": "F452",
    "report_id": "R023",
    "label": "Exhibit 176",
    "context": "Exhibit 176: Schneider OSG vs Capex Tracker (R-Square: 60%)"
  },
  {
    "figure_id": "F453",
    "report_id": "R023",
    "label": "Exhibit 177",
    "context": "Exhibit 177: SKF OSG vs Capex Tracker (R-Square: 60%)"
  },
  {
    "figure_id": "F454",
    "report_id": "R024",
    "label": "Figure 1",
    "context": "Figure 1: Strong sell-through at Marivista (观潮) in Bao'an, Shenzhen 深圳观潮房源销控表 MARIVISTA 深圳观潮房源销控表 MARIVISTA"
  },
  {
    "figure_id": "F455",
    "report_id": "R024",
    "label": "Figure 2",
    "context": "Figure 2: Neighborhood and school network near Marivista (观潮) in Bao'an, Shenzhen 西安云游集团海洋学校 西安中宇集团海洋学校"
  },
  {
    "figure_id": "F456",
    "report_id": "R024",
    "label": "Figure 3",
    "context": "Figure 3: NWD's K11 ECOAST shopping mall in Nanshan, Shenzhen QQ音乐 K11 价值超·500游客礼遇 免费领"
  },
  {
    "figure_id": "F457",
    "report_id": "R024",
    "label": "Figure 4",
    "context": "Figure 4: NWD's K11 ECOAST shopping mall in Nanshan, Shenzhen Interior view of a modern luxury shopping mall with a large decorative cake and a circular skylight, featuring a 'LUXBA' retail store sign (no readable text on main s"
  },
  {
    "figure_id": "F458",
    "report_id": "R024",
    "label": "Figure 5",
    "context": "Figure 5: COLI's Anlan Shanghai (left) and HKL's Westbund Central project (right) in Xuhui, Shanghai 3D architectural model of a modern city with skyscrapers and road networks, no visible text or symbols"
  },
  {
    "figure_id": "F459",
    "report_id": "R024",
    "label": "Figure 6",
    "context": "Figure 6: Shui On's Riverville villa project in Yangpu, Shanghai Exterior view of a modern brick building with a decorative roof and glass balcony, surrounded by greenery and urban buildings in the background (no visible text or"
  },
  {
    "figure_id": "F460",
    "report_id": "R024",
    "label": "Figure 7",
    "context": "Figure 7: Shui On's Riverville villa project in Yangpu, Shanghai Exterior view of a modern multi-story residential building with brick walls, balconies, and landscaping (no signage or text visible)"
  },
  {
    "figure_id": "F461",
    "report_id": "R024",
    "label": "Figure 8",
    "context": "Figure 8: Hang Lung Plaza 66 shopping mall in Jing'an, Shanghai 给同一天生日的你 HONG KONG YU Happy BIRTHDAY OF HONG KONG YU"
  },
  {
    "figure_id": "F462",
    "report_id": "R024",
    "label": "Figure 9",
    "context": "Figure 9: Longfor Paradisewalk shopping mall in Minhang, Shanghai Interior view of a modern multi-level shopping mall with escalators, retail displays, and visible store signage (no readable text in focus)"
  },
  {
    "figure_id": "F463",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Bingshan 25-city secondary real-time home sales continued to decelerate, to $+9\\%$ y-y in MTD June"
  },
  {
    "figure_id": "F464",
    "report_id": "R025",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Chinese New Year-adjusted cumulative secondary real-time home sales fell $\\sim 1\\%$ y-y in those cities"
  },
  {
    "figure_id": "F465",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China's HDT monthly sales volume HDT Sales Volume (monthly, k unit)"
  },
  {
    "figure_id": "F466",
    "report_id": "R027",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Official R&V Home Price Rose 5.7% YTD"
  },
  {
    "figure_id": "F467",
    "report_id": "R027",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Office - 1Q26 New Lettings"
  },
  {
    "figure_id": "F468",
    "report_id": "R028",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Historically, Korean households have shown a heavy bias toward real assets over financial assets – marginal asset growth led mainly by real assets Korean households annual change in asset composition"
  },
  {
    "figure_id": "F469",
    "report_id": "R028",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Real estate assets across main and other residences composed 70% of total household assets while the size of total assets nearly doubled in the past decade Household asset breakdown by sub-category (2025)"
  },
  {
    "figure_id": "F470",
    "report_id": "R028",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Korean household assets nearly doubled during 2000-24; fastest among DMs"
  },
  {
    "figure_id": "F471",
    "report_id": "R028",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The number of retail investors increased to 50% of total adult population vs. 21% in 2019 Number of retail investors and % to adult population"
  },
  {
    "figure_id": "F472",
    "report_id": "R028",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Korea registered a rapid expansion in financial assets of +94% vs. 31% in Japan during 2015-25"
  },
  {
    "figure_id": "F473",
    "report_id": "R028",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 43% of retail investors are aged 40s or below, groups with a higher marginal propensity to consume % share of retail investors by age group (2025)"
  },
  {
    "figure_id": "F474",
    "report_id": "R028",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Along with goods consumption, services has shown a higher response to KOSPI performance in recent quarters"
  },
  {
    "figure_id": "F475",
    "report_id": "R028",
    "label": "Exhibit 9",
    "context": "Exhibit 9: KOSPI: Annualized volatility and share of retail trade value – retail investors still seek volatility and chase themes, but compared to previous cycles, they have better access to quality information, as well as experien"
  },
  {
    "figure_id": "F476",
    "report_id": "R028",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Compared to the 2020-21 cycle, we find that retail net buying has been less concentrated in the current up-cycle. We believe retail investors have become more controlled and tactical in approaching equity investment"
  },
  {
    "figure_id": "F477",
    "report_id": "R028",
    "label": "Exhibit 11",
    "context": "Exhibit 11: For all of our scenarios, we expect equity holdings' proportion of household financial assets to be on an upward trajectory – but much steeper for the bull case. Strong market fundamentals, copious liquidity, and the ref"
  },
  {
    "figure_id": "F478",
    "report_id": "R028",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We raise our KOSPI target to 9,000 (from 8,500) with our new bull case being 10,500 and our bear case set at 6,500. We set our three- to six-month KOSPI trading band at 7,000-10,000."
  },
  {
    "figure_id": "F479",
    "report_id": "R028",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Household assets nearly doubled in the past decade Korea National Balance Sheet: Household sector (2024)"
  },
  {
    "figure_id": "F480",
    "report_id": "R028",
    "label": "Exhibit 14",
    "context": "Exhibit 14: The growth was the fastest among major markets"
  },
  {
    "figure_id": "F481",
    "report_id": "R028",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Historically, most of the marginal asset growth has been led by growth in real assets Korean households annual change in asset composition"
  },
  {
    "figure_id": "F482",
    "report_id": "R028",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Real estate assets across main and other residences composed 67% of total household assets back in 2015 Household asset breakdown by sub-category (2015)"
  },
  {
    "figure_id": "F483",
    "report_id": "R028",
    "label": "Exhibit 17",
    "context": "Exhibit 17: The share rose to 70% while the size of total assets nearly doubled in the past decade through 2025 Household asset breakdown by sub-category (2025)"
  },
  {
    "figure_id": "F484",
    "report_id": "R028",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Korean households' real asset share exceeded trend compared to other economies Share of real assets to total household assets (2024)"
  },
  {
    "figure_id": "F485",
    "report_id": "R028",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Real assets likely substituted for the low-funded pension and post-retirement income Share of pension and insurance to total household assets (2024)"
  },
  {
    "figure_id": "F486",
    "report_id": "R028",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Wealthier households showed a stronger preference to holding real estate: 77% vs. medium-income of 66.8% vs. 26.5% for bottom income households Household asset breakdown by income groups"
  },
  {
    "figure_id": "F487",
    "report_id": "R028",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Households showed the largest increase in equities holdings in 2025 Korean household sector financial asset growth contribution (pp) by products"
  },
  {
    "figure_id": "F488",
    "report_id": "R028",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Residential Property Market Volume Growth vs. Retail Net Buying+Brokerage Deposits Growth Trend"
  },
  {
    "figure_id": "F489",
    "report_id": "R028",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Liquid Money vs. Brokerage Customer Deposit Growth"
  },
  {
    "figure_id": "F490",
    "report_id": "R028",
    "label": "Exhibit 26",
    "context": "Exhibit 26: KOSPI Price Trend versus Retail Net Flows by Price Intervals (2020\\~2021)"
  },
  {
    "figure_id": "F491",
    "report_id": "R028",
    "label": "Exhibit 27",
    "context": "Exhibit 27: KOSPI: Annualized Volatility and Share of Retail Trade Value"
  },
  {
    "figure_id": "F492",
    "report_id": "R028",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Net Retail Flows by Sector (Consumer Discretionary + Tech)"
  },
  {
    "figure_id": "F493",
    "report_id": "R028",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Net Retail Flows by Sector (Healthcare + Comm. Services)"
  },
  {
    "figure_id": "F494",
    "report_id": "R028",
    "label": "Exhibit 30",
    "context": "Exhibit 30: KOSPI + KOSDAQ: Margin Loan Balance"
  },
  {
    "figure_id": "F495",
    "report_id": "R028",
    "label": "Exhibit 31",
    "context": "Exhibit 31: KOSPI + KOSDAQ: Margin Loan Balance as a Percentage of Market Cap"
  },
  {
    "figure_id": "F496",
    "report_id": "R028",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Leveraged Domestic Equity ETF AUM Trend"
  },
  {
    "figure_id": "F497",
    "report_id": "R028",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Retail investors taking out unsecured loans to invest in equities but tighter regulatory control"
  },
  {
    "figure_id": "F498",
    "report_id": "R028",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Meanwhile, mortgage debt growth has been slowing down amid tight credit control by the authorities Mortgage growth rate trend"
  },
  {
    "figure_id": "F499",
    "report_id": "R028",
    "label": "Exhibit 35",
    "context": "Exhibit 35: KOSPI: Annual Total Shareholder Return Trend"
  },
  {
    "figure_id": "F500",
    "report_id": "R028",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Share of Interim Dividends out of Total Dividends"
  },
  {
    "figure_id": "F501",
    "report_id": "R028",
    "label": "Exhibit 37",
    "context": "Exhibit 37: KOSPI: ROE"
  },
  {
    "figure_id": "F502",
    "report_id": "R028",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Annual retail fund flows into Banks, Insurers and Securities (2020\\~2026 YTD)"
  },
  {
    "figure_id": "F503",
    "report_id": "R028",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Liquid Money vs. Brokerage Deposit Growth"
  },
  {
    "figure_id": "F504",
    "report_id": "R028",
    "label": "Exhibit 40",
    "context": "Exhibit 40: The pace of house transaction volume growth has slowed, especially in Seoul from end-2025"
  },
  {
    "figure_id": "F505",
    "report_id": "R028",
    "label": "Exhibit 41",
    "context": "Exhibit 41: The share of speculative flows into Seoul's housing market has dropped to a three-year low"
  },
  {
    "figure_id": "F506",
    "report_id": "R028",
    "label": "Exhibit 42",
    "context": "Exhibit 42: KOSPI Price Trend versus Retail Net Flows by Price Intervals (2H25\\~1H26)"
  },
  {
    "figure_id": "F507",
    "report_id": "R028",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Korea Domestic Retail Activity vs. Forward Returns of MSCI Korea - Retail Flows Have Shifted from Contrarian in the past 5 years to Momentum-Reinforcing Since 2025 L4W Domestic Retail Flows 5-Year Percentile"
  },
  {
    "figure_id": "F508",
    "report_id": "R028",
    "label": "Exhibit 44",
    "context": "At the same time, the intensity of the wealth effect looks to have deepened. Equity market deposits surpassed W100tn for the first time and total household equity holdings climbed to an all-time high of W1,644tn as of 2025, marking a 48.2%Y increase in 2025. W"
  },
  {
    "figure_id": "F509",
    "report_id": "R028",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Along with goods consumption, services has shown a higher response to KOSPI performance in recent quarters Korea: Services consumption and equity market performance"
  },
  {
    "figure_id": "F510",
    "report_id": "R028",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Korea's financial imbalance with high asset skewed in real estate by the household sector vs. corporates"
  },
  {
    "figure_id": "F511",
    "report_id": "R028",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Local authorities target to lower Korea's household debt level to 80% of GDP by 2030 from 93% as of 2025 ## (3) Diversifying household income channels beyond labor and real asset returns The shift to financial assets c"
  },
  {
    "figure_id": "F512",
    "report_id": "R028",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Income breakdown across labor, financial and real asset returns show a heavy dependency on labor income % share of total household income (2025)"
  },
  {
    "figure_id": "F513",
    "report_id": "R028",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Households' dividend income shows an up-trend, yet remains relatively low at 2.2% of total disposable income Household dividend income trend to total income"
  },
  {
    "figure_id": "F514",
    "report_id": "R028",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Size of equity assets held by households set to reach highest share, at 35%, of total financial assets Equity holding exposure to total household assets"
  },
  {
    "figure_id": "F515",
    "report_id": "R028",
    "label": "Exhibit 51",
    "context": "Exhibit 51: This likely extends the size to over 80% of nominal GDP by 2027 vs. 61% in 2025 and 43% in 2024"
  },
  {
    "figure_id": "F516",
    "report_id": "R028",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Households' sensitivity to rising interest rates adds pressure to their already high leverage"
  },
  {
    "figure_id": "F517",
    "report_id": "R028",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Amid persistent increase in mortgage loans, other loans turned around to an increase past 4 quarters Quarterly changes: mortgage vs other loans"
  },
  {
    "figure_id": "F518",
    "report_id": "R028",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Rising financial asset wealth passing through to household income likely implies inflationary pressure build-up; Our analysis shows that KOSPI move showed high correlation with a statistical lead of 15-18 months"
  },
  {
    "figure_id": "F519",
    "report_id": "R028",
    "label": "Exhibit 55",
    "context": "Exhibit 55: We expect a hiking cycle to start from July 2026 through mid-2027"
  },
  {
    "figure_id": "F520",
    "report_id": "R028",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Customer Deposit Balance"
  },
  {
    "figure_id": "F521",
    "report_id": "R028",
    "label": "Exhibit 57",
    "context": "Exhibit 57: KOSPI + KOSDAQ: Margin Loan Balance"
  },
  {
    "figure_id": "F522",
    "report_id": "R028",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Domestic Equity ETF AUM Trend"
  },
  {
    "figure_id": "F523",
    "report_id": "R028",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Retail investors: monthly net buying of US equities"
  },
  {
    "figure_id": "F524",
    "report_id": "R028",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Retail investors: overseas equity holdings"
  },
  {
    "figure_id": "F525",
    "report_id": "R028",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Korea – Aggregate Household Financial Holdings Trend and Forecast (Base Case) Exhibit 62: Household Equity Holdings – Base, Bull, and Bear Cases"
  },
  {
    "figure_id": "F526",
    "report_id": "R028",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Impact on KOSPI linked to Samsung Electronics and SK Hynix Price Targets Exhibit 67: KOSPI target, bull case, and bear case – three- to six-month range of 7,000\\~10,000"
  },
  {
    "figure_id": "F527",
    "report_id": "R028",
    "label": "Exhibit 68",
    "context": "Exhibit 68: 2026 YTD Fund Flows by Investor Type and Price Performance Exhibit 69: Korean Cycle Indicator"
  },
  {
    "figure_id": "F528",
    "report_id": "R028",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Korean Cycle Indicator vs. KOSPI"
  },
  {
    "figure_id": "F529",
    "report_id": "R028",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Luxury sales growth at department stores"
  },
  {
    "figure_id": "F530",
    "report_id": "R028",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Department stores – foreign spending"
  },
  {
    "figure_id": "F531",
    "report_id": "R028",
    "label": "Exhibit 78",
    "context": "Exhibit 78: S. Korea: Retirement Pension Market"
  },
  {
    "figure_id": "F532",
    "report_id": "R028",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Retirement Pension Reserves by Type of Invested Assets"
  },
  {
    "figure_id": "F533",
    "report_id": "R028",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Financial Product/Services Mapping by Sophistication and Capability ```mermaid graph TD"
  },
  {
    "figure_id": "F534",
    "report_id": "R028",
    "label": "Exhibit 85",
    "context": "Exhibit 85: 2026YTD Domestic Individual Credit Card Spending Market Share"
  },
  {
    "figure_id": "F535",
    "report_id": "R028",
    "label": "Exhibit 86",
    "context": "Exhibit 86: Total Domestic Credit Sales and Growth Trend"
  },
  {
    "figure_id": "F536",
    "report_id": "R028",
    "label": "Exhibit 89",
    "context": "Exhibit 89: Sector Allocation"
  },
  {
    "figure_id": "F537",
    "report_id": "R028",
    "label": "Exhibit 90",
    "context": "Exhibit 90: Japanese households have shown stronger appetite for lower-risk assets vs. Korea; bias to cash remains higher Historical changes in the composition of household financial assets: Japan vs Korea"
  },
  {
    "figure_id": "F538",
    "report_id": "R028",
    "label": "Exhibit 91",
    "context": "Exhibit 91: Japan: Majority of contributions to annual increase in financial assets came from equity and investment trust holdings in 2025, following new NISA reforms Japanese household sector financial asset growth contribution ("
  },
  {
    "figure_id": "F539",
    "report_id": "R028",
    "label": "Exhibit 92",
    "context": "Exhibit 92: The number of NISA accounts nearly tripled over the past 10 years, and is up 50% since the new NISA reforms Japan: NISA Accounts (millions)"
  },
  {
    "figure_id": "F540",
    "report_id": "R028",
    "label": "Exhibit 93",
    "context": "Exhibit 93: NISA reforms have helped the market rise since 2H25 amid strong corporate earnings performance in Japan"
  },
  {
    "figure_id": "F541",
    "report_id": "R029",
    "label": "Figure 1",
    "context": "Figure 1: Korea Power Equipment Companies' Valuation"
  },
  {
    "figure_id": "F542",
    "report_id": "R029",
    "label": "Figure 2",
    "context": "Figure 2: Fund Rotations from China Power Equipment into China AI-Themed Stocks"
  },
  {
    "figure_id": "F543",
    "report_id": "R029",
    "label": "Figure 3",
    "context": "Figure 3: Share Price Weaknesses Across Global Power Equipment Companies Since May"
  },
  {
    "figure_id": "F544",
    "report_id": "R030",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Central/eastern Pacific SST anomalies are now clearly positive, confirming the ocean-side setup for a likely very strong El Niño Relative SST Anomalies (°C) 03 JUN 2026"
  },
  {
    "figure_id": "F545",
    "report_id": "R030",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NOAA/CPC now assigns a 63% (up from 37%) probability to a very strong El Niño in Nov-Jan, making intensity the key watchpoint NOAA CPC ENSO Strength Probabilities (issued June 2026) based on thresholds in ERSSTv5 Relat"
  },
  {
    "figure_id": "F546",
    "report_id": "R030",
    "label": "Exhibit 4",
    "context": "Exhibit 4: El Niño is now confirmed, while very-strong odds increased to 63% in Nov-Jan from 37% in the prior update Exhibit 5: El Niño strength distribution remains wide"
  },
  {
    "figure_id": "F547",
    "report_id": "R030",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ENSO Follows Seasonal Pattern: Peaking in Nov-Feb Oceanic Nino Index (ONI) by Season - 2000 to Latest Available Exhibit 6: El Niño is now officially confirmed, with NOAA/CPC moving to El Niño Advisory as ocean and atmo"
  },
  {
    "figure_id": "F548",
    "report_id": "R030",
    "label": "Exhibit 6",
    "context": "Exhibit 6: El Niño is now officially confirmed, with NOAA/CPC moving to El Niño Advisory as ocean and atmospheric indicators point to a coupled event"
  },
  {
    "figure_id": "F549",
    "report_id": "R030",
    "label": "Exhibit 8",
    "context": "Exhibit 8: CFSv2 points to continued Niño 3.4 strengthening into OND/NDJ, with several ensemble members near or above the +2.0°C very strong threshold"
  },
  {
    "figure_id": "F550",
    "report_id": "R030",
    "label": "Exhibit 10",
    "context": "Exhibit 10: El Niño is now officially confirmed, with NOAA/CPC moving to El Niño Advisory as ocean and atmospheric indicators point to a coupled event"
  },
  {
    "figure_id": "F551",
    "report_id": "R030",
    "label": "Exhibit 12",
    "context": "Exhibit 12: India usually receives below-normal rainfall during El Niño years. India is the world second largest sugar producer and below normal monsoon may reduce its sugar output potential Correlation between El Niño and Indian"
  },
  {
    "figure_id": "F552",
    "report_id": "R030",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Strong El Niño historically leads to soybean yield losses in MT, which is the largest producing state with 29% of national output"
  },
  {
    "figure_id": "F553",
    "report_id": "R030",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Sugar remains the cleanest bullish El Niño trade"
  },
  {
    "figure_id": "F554",
    "report_id": "R030",
    "label": "Exhibit 15",
    "context": "Exhibit 15: and to yield pressure in Matopiba, important grain frontier formed by Maranhão, Tocantins, Piauí and Bahia"
  },
  {
    "figure_id": "F555",
    "report_id": "R030",
    "label": "Exhibit 16",
    "context": "Exhibit 16: But, El Niño has historically supported higher soybean yields in Rio Grande do Sul..."
  },
  {
    "figure_id": "F556",
    "report_id": "R030",
    "label": "Exhibit 17",
    "context": "Exhibit 17: ...and better yields in Argentina"
  },
  {
    "figure_id": "F557",
    "report_id": "R030",
    "label": "Exhibit 19",
    "context": "Verão Tempo OK ## 2026 Weather Risk Outlook May 6, 2026 ## Regional Crop Impact Matrix by ENSO Phase Typical yield impact direction and severity across major producing regions"
  },
  {
    "figure_id": "F558",
    "report_id": "R030",
    "label": "Exhibit 21",
    "context": "Exhibit 21: El Niño Impacts on Global Weather Wet Dry Dry Oct. to following Jan."
  },
  {
    "figure_id": "F559",
    "report_id": "R030",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Crop Calendar North Hemisphere"
  },
  {
    "figure_id": "F560",
    "report_id": "R030",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Sugar remains the cleanest bullish El Niño trade."
  },
  {
    "figure_id": "F561",
    "report_id": "R030",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Sugar remains the cleanest bullish El Niño trade."
  },
  {
    "figure_id": "F562",
    "report_id": "R030",
    "label": "Exhibit 24",
    "context": "Exhibit 24: We expect prices impact to Soybeans to be more balanced"
  },
  {
    "figure_id": "F563",
    "report_id": "R030",
    "label": "Exhibit 25",
    "context": "Exhibit 25: While Corn Could face upside risk, due to shorter planting windows"
  },
  {
    "figure_id": "F564",
    "report_id": "R030",
    "label": "Exhibit 26",
    "context": "Exhibit 26: ENSO Follows Seasonal Pattern: Peaking in Nov-Feb Current conditions look closer to 2023 than to a more extreme 2015/16 setup Oceanic Nino Index (ONI) by Season - 2000 to Latest Available Legend ## Valuation Methodolog"
  },
  {
    "figure_id": "F565",
    "report_id": "R031",
    "label": "Figure 1",
    "context": "Figure 1: Mainland China RevPAR YoY change"
  },
  {
    "figure_id": "F566",
    "report_id": "R031",
    "label": "Figure 2",
    "context": "Figure 2: China weekly domestic air seat capacity, pax volume and airfare YoY"
  },
  {
    "figure_id": "F567",
    "report_id": "R031",
    "label": "Figure 3",
    "context": "Figure 3: RevPAR YoY performance by segment (May 31-Jun 6) RevPAR (YoY change %)"
  },
  {
    "figure_id": "F568",
    "report_id": "R031",
    "label": "Figure 4",
    "context": "Figure 4: ADR YoY performance by segment (May 31-Jun 6) ADR (YoY change %)"
  },
  {
    "figure_id": "F569",
    "report_id": "R031",
    "label": "Figure 5",
    "context": "Figure 5: OCC YoY performance by segment (May 31-Jun 6) Occ (YoY change ppt)"
  },
  {
    "figure_id": "F570",
    "report_id": "R031",
    "label": "Figure 6",
    "context": "Figure 6: Hotel booking APP weekly active users trend"
  },
  {
    "figure_id": "F571",
    "report_id": "R032",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our Global team raised forecasts for 800G and 1.6T optical transceiver shipments Exhibit 3: Our Global team estimates AI optical transceivers growing at \\~60% CAGR from 2025-28E We estimate AI transceivers growing at 60%"
  },
  {
    "figure_id": "F572",
    "report_id": "R032",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Optical transceiver PCB specs Exhibit 5: We estimate Global AI Transceiver PCB TAM to grow at 83% CAGR from 2025-28E AI transceiver PCB TAM is growing at 83% CAR from 2025-28E (US$ M)"
  },
  {
    "figure_id": "F573",
    "report_id": "R032",
    "label": "Exhibit 6",
    "context": "Exhibit 6: TAM comparison: AI transceiver vs. AI transceiver PCB"
  },
  {
    "figure_id": "F574",
    "report_id": "R032",
    "label": "Exhibit 7",
    "context": "Exhibit 7: AI transceiver PCB value contribution to suppliers - we expect suppliers to see 50-176% CAGR over CY25-28E AI Transceiver PCB value by supplier (US\\$M)"
  },
  {
    "figure_id": "F575",
    "report_id": "R032",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Residual income (RI) model Exhibit 13: ZDT P/E"
  },
  {
    "figure_id": "F576",
    "report_id": "R032",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Unimicron residual income (RI) model Exhibit 18: Unimicron P/E"
  },
  {
    "figure_id": "F577",
    "report_id": "R032",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Shennan Circuits residual income (RI) model Exhibit 23: Shennan Circuits 5Y P/E Band"
  },
  {
    "figure_id": "F578",
    "report_id": "R033",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Furukawa Electric (5801): OP MSe vs Consensus"
  },
  {
    "figure_id": "F579",
    "report_id": "R033",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Sumitomo Electric (5802): OP MSe vs Consensus"
  },
  {
    "figure_id": "F580",
    "report_id": "R033",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Fujikura (5803): OP MSe vs Consensus"
  },
  {
    "figure_id": "F581",
    "report_id": "R033",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Hyperscaler CAPEX YoY"
  },
  {
    "figure_id": "F582",
    "report_id": "R033",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Hyperscaler capital intensity Top 14 Cloud Providers: Capital Intensity"
  },
  {
    "figure_id": "F583",
    "report_id": "R033",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Hyperscaler CAPEX"
  },
  {
    "figure_id": "F584",
    "report_id": "R033",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Performance of optical component stocks (May 1, 2026=1)"
  },
  {
    "figure_id": "F585",
    "report_id": "R033",
    "label": "Exhibit 11",
    "context": "Exhibit 11: PEG Map"
  },
  {
    "figure_id": "F586",
    "report_id": "R033",
    "label": "Exhibit 12",
    "context": "Exhibit 12: ROE vs P/B"
  },
  {
    "figure_id": "F587",
    "report_id": "R033",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Furukawa Electric: Stock Price & OP Consensus Estimate Trend"
  },
  {
    "figure_id": "F588",
    "report_id": "R033",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Sumitomo Electric: Stock Price & OP Consensus Estimate Trend"
  },
  {
    "figure_id": "F589",
    "report_id": "R033",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Fujikura: Stock Price & OP Consensus Estimate Trend"
  },
  {
    "figure_id": "F590",
    "report_id": "R033",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Estimated P/E: Furukawa Electric vs TOPIX"
  },
  {
    "figure_id": "F591",
    "report_id": "R033",
    "label": "Exhibit 21",
    "context": "Exhibit 21: P/B: Furukawa Electric vs TOPIX"
  },
  {
    "figure_id": "F592",
    "report_id": "R033",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Estimated P/E: Sumitomo Electric vs TOPIX"
  },
  {
    "figure_id": "F593",
    "report_id": "R033",
    "label": "Exhibit 23",
    "context": "Exhibit 23: P/B: Sumitomo Electric vs TOPIX"
  },
  {
    "figure_id": "F594",
    "report_id": "R033",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Estimated P/E: Fujikura vs TOPIX"
  },
  {
    "figure_id": "F595",
    "report_id": "R033",
    "label": "Exhibit 25",
    "context": "Exhibit 25: P/B: Fujikura vs TOPIX"
  },
  {
    "figure_id": "F596",
    "report_id": "R033",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Corning, Lumentum, and Coherent P/E"
  },
  {
    "figure_id": "F597",
    "report_id": "R033",
    "label": "Exhibit 27",
    "context": "Exhibit 27: 3 Cable Companies P/E"
  },
  {
    "figure_id": "F598",
    "report_id": "R033",
    "label": "Exhibit 28",
    "context": "Exhibit 28: 3 Cable Companies Div Yield"
  },
  {
    "figure_id": "F599",
    "report_id": "R033",
    "label": "Exhibit 29",
    "context": "Exhibit 29: 3 Cable Companies EV/EBITDA"
  },
  {
    "figure_id": "F600",
    "report_id": "R033",
    "label": "Exhibit 36",
    "context": "## MS ESTIMATES VS. CONSENSUS"
  },
  {
    "figure_id": "F601",
    "report_id": "R033",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Optical fiber & cable export value"
  },
  {
    "figure_id": "F602",
    "report_id": "R033",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Optical fiber & cable export value"
  },
  {
    "figure_id": "F603",
    "report_id": "R033",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Optical fiber & cable export value"
  },
  {
    "figure_id": "F604",
    "report_id": "R033",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Optical cable exports to N. America (from Yokohama/Tokyo Customs)"
  },
  {
    "figure_id": "F605",
    "report_id": "R033",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Power cable (over 1kV) exports by customs site"
  },
  {
    "figure_id": "F606",
    "report_id": "R033",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Optical cable exports by customs site"
  },
  {
    "figure_id": "F607",
    "report_id": "R033",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Optical cable exports to Western Europe (from Yokohama/Tokyo Customs) Exhibit 44: Power cable & optical cable exports from Chiba Customs"
  },
  {
    "figure_id": "F608",
    "report_id": "R033",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Optical cable exports to Western Europe (from Yokohama/Tokyo Customs) Exhibit 44: Power cable & optical cable exports from Chiba Customs"
  },
  {
    "figure_id": "F609",
    "report_id": "R033",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Optical Fiber Connector export value"
  },
  {
    "figure_id": "F610",
    "report_id": "R033",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Optical Fiber Connector by Location from Tokyo Customs Optical Fiber Connector from Tokyo (¥bn)"
  },
  {
    "figure_id": "F611",
    "report_id": "R033",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Optical Fusion Splicer export value (from Kumamoto and Yokohama)"
  },
  {
    "figure_id": "F612",
    "report_id": "R033",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Optical Fusion Splicer export value by Location from Kumamoto Customs"
  },
  {
    "figure_id": "F613",
    "report_id": "R034",
    "label": "Exhibit 7",
    "context": "EXHIBIT 2: ChatGPT can identify the SKU and estimate an approximate price range, but appears to rely on web scraping at times. Whole Foods link, in exhibit, directs to an article on Whole Foods delivery policy. I want to make scram"
  },
  {
    "figure_id": "F614",
    "report_id": "R034",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Through its partnership with Uber Eats, Claude enables users to complete purchases via Uber Eats directly within the interface. I don't have a grocery delivery connector available to place orders directly. Let me see if"
  },
  {
    "figure_id": "F615",
    "report_id": "R034",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Amazon provides product recommendations at the SKU level, presenting users with a range of options to choose from. I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of or"
  },
  {
    "figure_id": "F616",
    "report_id": "R034",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Alexa is unable to do so for Amazon Fresh and Whole Foods products; it directs the user to an external link. All four options qualify for free delivery today (1 PM – 3 PM) on qualifying orders. The 365 by Whole Foods Mar"
  },
  {
    "figure_id": "F617",
    "report_id": "R034",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Sparky is capable of handling the full flow from product discovery through to building a basket (or cart). Great news — two of these options show delivery as soon as 18 minutes to 22201 (Arlington, VA). Here are your 64"
  },
  {
    "figure_id": "F618",
    "report_id": "R034",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Of the 15 meals listed, Sparky was able to match 14 to existing recipes in its database. Recipes seem to come from the American Diabetes Association (ADA)."
  },
  {
    "figure_id": "F619",
    "report_id": "R034",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Of the 15 meals listed, Sparky was able to match 14 to existing recipes in its database. Recipes seem to come from the American Diabetes Association (ADA). Ask Sparky *L - salad and fruits * D - Pizza and fries Please"
  },
  {
    "figure_id": "F620",
    "report_id": "R034",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Users can open recipes within the Sparky interface, adjust the serving size, and add the relevant SKUs to cart. Recipes Frozen yogurt bark with strawberries and dark chocolate"
  },
  {
    "figure_id": "F621",
    "report_id": "R034",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Gemini manages the allergy, but its list lacks quantitative budgeting and retailer optimization. EXHIBIT 16: Unlike Gemini, ChatGPT provides a more extensive product list from different retailers, while recognizing aller"
  },
  {
    "figure_id": "F622",
    "report_id": "R034",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Estimated weekly cost provides a useful benchmark, helping shoppers plan. Estimated Weekly Cost (NYC) Category Estimated Cost Produce $35–45 Dairy & Eggs $25–35"
  },
  {
    "figure_id": "F623",
    "report_id": "R034",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Claude's HTML interface creates a visually polished and engaging experience, but lacks shoppability. Pricing is somewhat consistent with that of other models. □ PANTRY, BREAD & DRY GOODS"
  },
  {
    "figure_id": "F624",
    "report_id": "R034",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Walmart doesn't stock Longchamp (1P), similar to its absence on Amazon. However, Sparky still provides alternatives from its third-party marketplace. Here's what's available for the Longchamp Le Pliage Original large tot"
  }
]