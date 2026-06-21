请基于下面每天新报告的摘要，写一份“市场最新观点汇总”的结构化 JSON，用于生成 PDF。

要求：
1. 观点要分门别类，例如：宏观与利率、AI/算力、能源与大宗、地产与消费、区域市场、风险偏好等。类别由内容决定，不要机械套模板。
2. sections 建议 5-8 个，尽量覆盖所有报告 ID；references 合并后应覆盖大多数甚至全部报告。
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
    "title": "GS：市场低估的不是通胀本身，而是通胀预期的再定价机制",
    "digest": "[wechat_article.md]\n# GS：市场低估的不是通胀本身，而是通胀预期的再定价机制\n\n这份GS全球利率策略报告的核心判断，并非关于通胀是否见顶，而是关于一个更微妙、也更具交易含义的转变：通胀风险已经从单纯的能源价格冲击，转移到了央行反应函数的重新定价上。这意味着，市场对通胀的敏感度正在发生结构性变化，投资者需要调整的不是方向判断，而是对利率曲线不同段落的定价逻辑。\n\n报告明确指出，美伊协议带来的能源缓解已经部分消化，但取而代之的是美联储鹰派沟通对短端利率的重塑。GS团队认为，市场正在从一个以宏观冲击为主导的环境，转向一个以政策不确定性为主导的环境。这个转变的直接后果是：利率波动率的重心将从长端向短端转移，而曲线中段（即所谓的“belly”）可能成为风险收益比最优的区间。\n\n这不是一个简单的“通胀见顶，做多债券”的故事。这是一个关于波动率结构、央行沟通机制和曲线形态重新定价的深度叙事。以下，我们从五个层次展开这份报告的核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 鹰派预期的前置化正在压缩长端风险溢价，但曲线中段反而提供了不对称机会\n\nGS团队观察到，市场对加息的定价已经从前期的“分散化”转向了“前置化”。OIS曲线显示，市场几乎定价了两次加息，但有趣的是，利率曲线的峰值并未显著高于5月非农数据出炉后的水平。这意味着什么？\n\n这意味着市场对美联储反应函数的理解正在发生变化。过去，通胀数据超预期会同时推升短端和长端利率；但现在，市场似乎认为，只要美联储展现出足够的前瞻性，长端的风险溢价就会被压制。GS将这种现象描述为“鹰派的前端/丰富的长端”格局。这种格局在历史上往往对应着曲线陡峭化的倾向。\n\n但GS团队并未简单地推荐陡峭化交易。他们认为，在短期内，市场对反应函数的重新评估更有利于曲线中段（5年期）的表现。逻辑在于：如果加息风险被\n\n[... middle omitted ...]\n\n能被证伪，以及如何在当前环境下调整自己的投资组合。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储变脸后，利率市场怎么玩\n\n利率市场新逻辑\n\n美联储突然鹰了，市场措手不及。油价下跌带来的通胀缓解，很快被央行的强硬表态盖过。利率曲线正在重新定价。\n\n1/ 利率曲线变平了\n美联储暗示可能再加息，市场定价迅速前移。但奇怪的是，远期利率反而被压低了——因为市场相信央行会提前行动、控制通胀。结果是，短期利率飙升，长期利率受压制，曲线整体走平。\n\n2/ 中段是当前最优选择\n研报认为，5年期国债（曲线中段）最值得关注。如果加息风险落地，5年相对2年和10年会跑赢；如果数据继续走强，5年同样受益。简单说，无论哪种情况，中段都是风险收益比最好的位置。\n\n3/ 通胀交易逻辑变了\n以前油价跌=通胀预期降=利率下行。现在变了——美联储鹰派表态后，实际利率飙升，通胀预期反而被压缩。这意味着，未来通胀数据对市场的影响，更多会通过实际利率传导，而不是通胀溢价本身。\n\n4/ 欧洲和英国各有看点\n欧洲：油价缓解降低了利率波动，利好主权债券利差收窄。但能源期货已低于研报预期，继续利好空间有限。\n英国：通胀数据走弱+失业率趋势下行，央行大概率按兵不动。市场定价了45bp加息，这个预期有下行空间。\n\n5/ 日本：财政政策成焦点\n日本央行加\n\n[... middle omitted ...]\n\npositioning for belly outperformance on the curve offers the best near-term risk/reward for longs. Energy relief narrows the outcomes for European rates, favouring lower vol and EGB carry, but\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "GS：市场真正低估的不是期限溢价的水平，而是它为何不再回落",
    "digest": "[wechat_article.md]\n# GS：市场真正低估的不是期限溢价的水平，而是它为何不再回落\n\n过去两年，全球债券市场一直在争论一个核心问题：长端利率的抬升，究竟是因为市场预期未来短期利率会结构性走高，还是因为投资者要求更高的“期限溢价”来补偿持有长期债券的风险？这不仅仅是学术争论。它直接决定了你的组合应该配置长债还是短债、是押注利率下行还是接受一个更高的中性利率环境。\n\nGS在最新发布的G10期限溢价更新报告中，给出了一个比以往更锐利的分析框架。报告的核心判断不是“期限溢价现在有多高”，而是：**传统基于收益率曲线推算的期限溢价模型，可能正在系统性高估当前实际期限溢价水平，因为它没能区分“结构性利率预期上移”和“周期性风险定价”**。\n\n这份报告的意义在于，它提供了一个更精确的“拆解工具”，帮助投资者判断当前债券市场定价中，哪些是可持续的结构性变化，哪些是可能均值回归的周期性溢价。对于任何管理利率风险的决策者来说，这可能是今年最重要的分析框架更新之一。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 两种模型，两种世界观：一个高估风险，一个低估趋势\n\nGS此次的核心贡献，是同时发布了两种期限溢价估算结果，并系统对比了它们的差异。\n\n第一种是传统的“纯收益率曲线模型”（类似经典的ACM模型）。它只利用当前收益率曲线的形状来推断市场对未来短期利率的预期，然后将剩余部分归为期限溢价。这种模型的优点是实时性强、对市场情绪变化敏感，但缺点也很明显：它高度依赖历史均值作为长期利率预期的锚点。当经济发生结构性转变时，比如央行政策框架变化或通胀中枢上移，这种模型会倾向于把大部分收益率曲线陡峭化解释为期限溢价上升，而不是利率预期的结构性调整。\n\n第二种是“基于调查的模型”（类似Kim-Wright方法）。它引入经济学家和交易员的短期利率预期调查数据，直接约束模\n\n[... middle omitted ...]\n\n表和数据，并持续跟踪GS后续关于期限溢价驱动因素的深度研究。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球债券的期限溢价，还在高位\n\n**期限溢价，还高着**\n\n**两种模型都指向同一个方向**\n\n最近某外资投行的研报更新了G10经济体的期限溢价估算，引入了基于调查数据的新模型，和传统只用收益率曲线的模型对比着看。\n\n**1/ 两个模型，两种视角**\n\n传统模型（纯收益率曲线法）波动更大，能实时捕捉市场情绪变化。新模型（加入调查数据）更稳定，能更好识别利率预期的结构性转变。\n\n比如日本：传统模型把收益率曲线陡峭化几乎全归因于期限溢价上升，但加入调查数据后发现，很大一部分其实是市场对政策利率路径的预期在结构性抬升。\n\n**2/ 当前水平，两种方法都显示溢价偏高**\n\n美国：调查模型估算10年期期限溢价约70bp，比传统模型低40bp\n欧洲：调查模型比传统模型低约15bp\n英国：调查模型竟然是G4中最低的，说明英国利率预期本身很高\n日本：调查模型显示期限溢价上升幅度远小于传统模型\n\n**3/ 各有优劣，不是非此即彼**\n\n调查模型在经济直觉上更合理，特别适合捕捉结构性变化（比如德国债务刹车改革后，市场不仅调整了对债券供给的预期，还上调了增长预期）\n\n但传统模型在预测未来持有债券的超额回报方面表现更好，对交易信号更\n\n[... middle omitted ...]\n\nin major bond markets.  \nJapan is a clear illustration of the advantages of survey-based models. Yield curve-only estimates interpret almost the entirety of the yield curve steepening as a ris\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "GS：韩国市场上涨背后的结构性分歧，比指数本身更值得关注",
    "digest": "[wechat_article.md]\n# GS：韩国市场上涨背后的结构性分歧，比指数本身更值得关注\n\nKOSPI一周暴涨11%，突破9000点，科技股领涨，外资回流。这是本周韩国市场的直观画面。\n\n但如果只看这个数字，可能会错过这份GS周报真正想传递的信号。指数上涨的同时，资金流向、基金仓位和MSCI评估这三个维度，正在指向一个更微妙、也更需要警惕的结论：韩国市场正在经历一轮“有选择的上涨”，而非系统性重估。上涨的广度、可持续性以及背后的结构性障碍，仍然存在明显分歧。\n\n这份报告的数据点很多，但最值得提炼的判断只有一个：**韩国市场的短期动能来自事件驱动和外资回补，但中期结构性折价的修复，仍取决于MSCI评估中那些尚未解决的制度性障碍能否真正落地。** 市场目前定价的是前者，而后者才是决定估值能否系统性扩张的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 外资流入看似强劲，但基金仓位数据揭示的却是持续减持\n\n本周外资净买入KOSPI市场2.5万亿韩元，推动指数大涨。单看这一数据，很容易得出“外资重新看好韩国”的结论。\n\n但GS援引的EPFR初步数据（覆盖约46%的AUM）给出了另一幅图景。截至2026年5月，亚洲基金和新兴市场基金对韩国股票的配置，相对于基准指数，仍然是显著低配的。亚洲基金低配195个基点，新兴市场基金低配285个基点。更关键的是，在过去一个月和过去三个月中，这两类基金都在持续削减对韩国的敞口。亚洲基金过去一个月减持105个基点，过去三个月累计减持140个基点；新兴市场基金则分别减持165和195个基点。\n\n这意味着什么？本周的外资净买入，更可能来自交易型资金或被动型资金的短期回补，而非主动管理型基金的战略性加仓。主动基金的真实仓位仍在下降，这与指数上涨形成了方向性背离。这种背离本身就是一个需要警惕的信号：短期资金推动的上涨\n\n[... middle omitted ...]\n\n星球微信群里继续讨论。那里有更完整的报告原文和更细致的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国市场一周观察：外资回流与MSCI评级\n\n韩国市场，外资回来了\n\nKOSPI上周大涨11%，突破9000点，科技板块领涨。外资净买入约2.5万亿韩元，主要流向科技和汽车板块。\n\n1️⃣ 市场表现\n保险(+18.4%)、科技(+16.6%)、零售(+5.4%)领跑\n建筑(-9.9%)、电信(-6.2%)、休闲(-5.1%)垫底\n12个月前瞻EPS上调1.5%，科技板块盈利预期最强\n\n2️⃣ 资金流向\n外资从净卖出转为净买入，主要买入KOSPI科技和汽车\n但亚洲和新兴市场基金对韩国整体仍低配\n保险和科技硬件最受超配，互联网和医疗最受低配\n\n3️⃣ MSCI评级更新\n韩国指数衍生品在海外交易所上市，获MSCI肯定\n但仍有5项“需改善”评级：外汇自由化、投资者注册、英文信息披露、清算结算、可转移性\nMSCI表示要看到实际改善，而非仅凭改革承诺\n6月23日年度评估大概率不会纳入发达市场观察名单\n\n4️⃣ 汇率与风险指标\n韩元兑美元贬值0.8%\n韩国权益风险指标回到中性区域\n\n💡 市场处于关键观察期，外资回流趋势能否持续，取决于MSCI后续评估和改革落地进展。\n\n#学习笔记\n\n[source_mineru.md]\n##\n\n[... middle omitted ...]\n\nctor saw the strongest upward earnings revisions, while the Chemicals sector was revised down the most this week (Exhibit 20).  \nThe KRW weakened 0.8% vs. USD this week. It also weakened by 0.\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "GS：资金流向正在重塑全球资产定价的底层逻辑",
    "digest": "[wechat_article.md]\n# GS：资金流向正在重塑全球资产定价的底层逻辑\n\n全球资金正在经历一次结构性的再配置。这不是一次简单的板块轮动，而是一个可能影响未来12至18个月资产定价的核心变量。\n\nGS最新一期全球资金流向周报（截至6月17日）揭示了一个清晰的信号：资金正在从分散的试探性布局，转向有明确主题的集中押注。当周全球股票基金净流入达到1260亿美元，远超此前一周的310亿美元。这一数字本身已经足够引人注目，但真正值得深入拆解的，是资金流入的结构——科技板块的吸金能力正在加速，工业板块紧随其后，而中国内地股票基金则持续面临净流出。\n\n这份报告的核心判断是什么？不是“资金回来了”，而是“资金正在为新的宏观叙事定价”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 科技板块的资金虹吸效应正在从美国向外扩散\n\nGS的图表清晰地展示了美国科技板块基金在最近几周的强劲净流入。这并非孤立现象。报告指出，科技基金和工业基金在全球范围内都录得了最大的净流入。但美国科技板块的流入尤为突出，其背后是AI驱动的需求增长。\n\n这里有一个关键的分析层次。GS在报告中点明了一个经常被市场忽视的传导机制：强劲的AI需求不仅推高了增长预期，还通过推高通胀和中性利率预期，强化了美元的强势。换句话说，资金流入科技板块，表面上是在押注技术突破，实际上是在对整个宏观组合——更高的增长、更高的利率、更强的美元——进行系统性下注。\n\n这意味着，科技板块的涨跌不再仅仅是行业基本面问题。它已经成为全球宏观资产定价的一个核心锚点。如果后续科技板块的资金流入出现逆转，其影响将远不止于纳斯达克，而是会通过美元、利率和新兴市场资金流向产生连锁反应。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 中国内地股票基金的持续失血暴露了更深层的结构性\n\n[... middle omitted ...]\n\n表解读，并定期组织对GS、MS等头部机构最新研报的深度拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n科技基金吸金，AI仍是主旋律\n\n全球资金流向观察\n\n最近某外资投行发布的资金流研报很有意思，信息量很大，我帮你拆解一下核心逻辑。\n\n1️⃣ 权益市场继续吸金\n截至6月17日当周，全球权益基金净流入1260亿美元，远超上周的310亿。美国基金是主要驱动力，科技和工业板块最受青睐。美国科技基金近期流入尤其强劲，AI驱动的需求是背后关键因素。\n\n2️⃣ 固收市场同样稳健\n全球固收基金净流入191.6亿美元。短久期和通胀保护债券持续受欢迎。新兴市场方面，硬通货债券基金净流入，本币债券基金则净流出。货币市场基金资产增加250亿美元。\n\n3️⃣ 新兴市场出现分化\n中国大陆权益基金净流出，台湾则净流入。整体看，资金正在从部分新兴市场撤出，转向美元资产。跨境外汇流中，美元、欧元、日元需求最强，人民币净流出最大。\n\n4️⃣ 行业资金流向一览\n从年初至今的累计数据看，工业、基础设施、能源板块资金流入最多。科技板块虽然近期热度高，但累计流入并不算最突出。消费和金融板块则出现净流出。\n\n5️⃣ 区域资金流向对比\n台湾、巴西、韩国是资金流入最多的新兴市场，中国大陆和印度则净流出最多。美国市场虽然持续吸金，但欧洲和日本也有一定流入。\n\n[... middle omitted ...]\n\nbeen particularly strong in recent weeks (see Chart of the Week) and we have noted that strong AI-led US demand has been a major factor behind higher growth, inflation and pricing for the neut\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "GS：市场低估的不是资本开支本身，而是资本开支正在重塑行业竞争格局",
    "digest": "[wechat_article.md]\n# GS：市场低估的不是资本开支本身，而是资本开支正在重塑行业竞争格局\n\n这份GS研报传递了一个核心信号：全球正在进入一个由资本开支驱动的“后现代周期”，但市场对它的理解仍然停留在“谁在花钱”的层面，而忽略了“钱花在哪里、谁有能力花、花完之后谁受益”这三个更深层的结构性变化。\n\n研报覆盖了从AI数据中心、油气勘探到电力基础设施的广泛领域，但将这些分散的线索串联起来，你会发现一个共同的主线：资本开支的回报逻辑正在从“规模扩张”转向“议价权重构”。那些能够将资本投入转化为行业准入壁垒、技术标准定义权或稀缺资源控制权的企业，才是这个周期真正的赢家。\n\n以下是我们从这份报告中提炼出的五个关键洞察，以及一个尚未被充分讨论的隐忧。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本开支周期的本质不是“花钱”，而是“重新划定谁有资格进场”\n\nGS全球策略师Peter Oppenheimer在研报中提出了一个关键判断：当前资本开支周期与以往不同，其回报更多来自每股盈利增长而非估值扩张，这意味着个股之间的分化将显著加大，主动选股的空间正在打开。\n\n这个判断的潜台词是：市场正在从“水涨船高”的阶段进入“优胜劣汰”的阶段。过去几年，低利率环境下，几乎所有企业都能轻松融资、扩大投资，资本开支的回报差异被流动性掩盖。而现在，随着利率维持高位、融资成本上升，资本开支的“准入门槛”正在提高——只有那些拥有稳定现金流、明确战略方向和技术壁垒的企业，才能持续投入并看到回报。\n\n以数据中心为例。GS欧洲公用事业分析师Alberto Gandolfi的最新估算显示，欧洲数据中心管道已接近500GW，相当于当前欧盟电力需求的1.5倍，六个月前这个数字还只有约300GW。这意味着，谁能在未来几年获得稳定的电力供应、谁能在电网接入和土地审批上占据先机，谁就\n\n[... middle omitted ...]\n\nBS等头部投行研报的深度解读，以及对这些未解问题的跟踪分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI时代的“暗工厂”，资本开支新周期\n\n**资本开支新周期**\n\n某外资投行最新报告指出，全球正进入资本密集型增长的新阶段。与传统周期不同，这轮回报更多来自每股收益增长而非估值提升，意味着个股分化将加大，主动选股的空间在扩大。\n\n**1/ 三大受益赛道**\n\n首先是**数据中心与公用事业**。欧洲数据中心管道已接近500GW（相当于当前欧盟电力需求的1.5倍），半年内增长了70%。这意味着电力基础设施将迎来长期需求支撑。\n\n其次是**AI基础设施**。超大规模云服务商的AI基础设施需求依然强劲，数据中心定价权持续增强。半导体设备、电力电网相关公司成为直接受益者。\n\n第三是**软件与自动化**。一个有趣的观察来自专家电话会：“自主软件开发”正在催生“暗工厂”模式——编码AI写代码，运维AI自动诊断和修复问题，形成更紧密的开发-运维闭环。\n\n**2/ 石油资本开支回归**\n\n尽管油价回落至80美元/桶附近，但石油公司的资本开支正在回暖。原因很简单：过去10年储备寿命下降了60%，而美国页岩油对油价的压制效应正在消退。能源安全压力进一步推动了这一趋势。\n\n某地震勘探公司反馈，EAGE行业会议参会人数创纪录，“前沿勘\n\n[... middle omitted ...]\n\nhin which we should view the sector (as well as covering some of the basics which haven't changed) – on Monday (sign up).\n\nFrontier exploration is back even with a lower oil price. Amidst Iran\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 1: Hike risk is more front-loaded, but the curve is not pricing a significantly higher peak 3m SOFR futures curve"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: 5s should outperform on the curve from front-loading of hike risk against stickier or declining forwards further out the curve Shift in curve segments implied by changes in pace of hikes over next 6m, extent of hikes ove"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Front-end inflation pricing aligns with our economists' forecasts CPI yoy Fixings vs GS Forecasts"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Greater policy uncertainty flattens the volatility tail curve 1y3m US rate uncertainty (orthogonalized against inflation, growth) vs implied vol tail curve"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Markets are hawkish vs policy rate surveys ECB surveys of the policy rate vs market probabilities based on swaption pricing"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: EU bid-ask spread has underperformed growth in the EU debt stock Bid-ask spread of 10y benchmark vs Debt outstanding"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Survey-based estimations currently sit below yield curve only term premium estimates ..."
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ... and also show relatively more stability"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 3: UK survey-based estimates are the lowest among the G4, indicating an important part comes from high rates expectations"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Using surveys shows that the rise in JGBs is not only a term premium story"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 5: Within some of the smaller G10 the level of term premium differs meaningfully depending on approach Current G10 10y Term Premium Estimates"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Our existing estimates of term premium are more volatile than survey-augmented estimates Standard Deviation of Term Premium Estimates"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 7",
    "context": "Exhibit 7: The debt brake removal might be a justification for higher real rates over time"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Including surveys suggests a larger role for rates expectations in the recent increase in JGB yields"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Term premium is typically a useful predictor of duration excess returns over medium horizons 1y holding excess return of 10y UST vs term premium"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Yield curve-based (GS) approach better at predicting excess duration returns than survey-augmented estimates (KW) G4 Average"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Yield curve models only show more responsiveness to shifts in level and slope Term premium sensitivity (in pp) to a 1-standard deviation change in PC1 and 2"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 12: G4 term premium has risen alongside shrinking central bank balance sheets Average of yield curve-only and survey-based term premium across G4 (GDP weighted) and average central bank holdings (GDP weighted)"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 13",
    "context": "Exhibit 13: The recent decline in implied volatility has not yet been reflected in lower term premium Average of yield curve-only and survey-based term premium across G4 (GDP weighted) and average implied vol (GDP weighted)"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Among EM & Asian focused funds, Insurance and Tech H/W are the most OW while Internet and Health Care are the most UW Korea allocation in EM & Asian focused funds (OW/UW vs. benchmark, bp)"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Over the past 3 months, EM & Asian funds have raised their exposure to Industrials the most while trimmed down Tech H/W exposure by sector Change in Korea allocation in EM & Asian focused funds (past 3M, bp)"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Up (↑) = Up wow vs. the previous week Asterisk (\\*) = Expressed in standard deviation of 1-wk change in 1-year Year-to-date Foreign Inflows to Korea"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Equity inflows to 5 AEJ markets 4-week rolling sum"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Equity inflows to 5 AEJ markets"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Bond inflows to 4 AEJ markets 4-week rolling sum"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Bond inflows to 4 AEJ markets"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Housing prices and rental prices National, monthly and weekly price changes"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Living expense price changes Monthly and weekly changes vs. CPI"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Daily Financial Condition Index Jan 1, 2013=100"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Performance of Korean and regional equity markets Exhibit 17: KOSPI and MSCI regional index KOSPI Index price performance (KRW)"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Weekly sector performance relative to KOSPI"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Historical trend of monthly KOSPI earnings momentum"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Weekly earnings momentum for KOSPI and selected sectors"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Exhibit 22",
    "context": "Exhibit 23: 12-month forward P/E and P/B for KOSPI, since Jan 2008"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Exhibit 24",
    "context": "Exhibit 24: 12-month forward P/E for MSCI Korea, since Jan 2008"
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Current 12m forward P/E of KOSPI and selected sectors since Jan 2006"
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Exhibit 27",
    "context": "Exhibit 27: MXKR valuation discount relative to MSCI AC World NTM P/E"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "Exhibit 28",
    "context": "Exhibit 28: MXKR valuation discount relative to MXAPJ NTM P/E"
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Exhibit 31",
    "context": "Exhibit 31: 2025 & 2026 year-to-date KOSPI purchase by investor type"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Weekly fund flows on sectors by investor type, with relative returns to KOSPI KOSPI and sector's relative returns and flow data Exhibit 34: KOSPI sectors, ranked by foreign ownership as a % of total market value"
  },
  {
    "figure_id": "F041",
    "report_id": "R003",
    "label": "Exhibit 35",
    "context": "Exhibit 35: KOSPI sectors ranked by foreign ownership % change Absolute ownership % (market value) changes"
  },
  {
    "figure_id": "F042",
    "report_id": "R003",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Equity net weekly flows (Week ending on Thursday due to data availability)"
  },
  {
    "figure_id": "F043",
    "report_id": "R003",
    "label": "Exhibit 37",
    "context": "Exhibit 37: 12-month forward D/Y for KOSPI and Korea Treasury bond yield"
  },
  {
    "figure_id": "F044",
    "report_id": "R003",
    "label": "Exhibit 39",
    "context": "Exhibit 39: USDKRW and USDCNY rates"
  },
  {
    "figure_id": "F045",
    "report_id": "R003",
    "label": "Exhibit 40",
    "context": "Exhibit 40: USDKRW vs. 10 year bond yields differentials between the US and Korea"
  },
  {
    "figure_id": "F046",
    "report_id": "R003",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Korea Equity Risk Barometer"
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Loans on Margin account balance"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Korea Volatility Index (VKOSPI)"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Exhibit 44",
    "context": "Exhibit 44: KOSPI Percent of Members above 200 day moving average"
  }
]