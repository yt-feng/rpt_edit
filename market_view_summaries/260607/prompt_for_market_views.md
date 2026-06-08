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
    "title": "市场真正低估的不是风险，而是风险积累的速度",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是风险，而是风险积累的速度\n\n全球股市正在逼近历史高点，乐观情绪在多个维度同时升温。某外资投行最新发布的研报，通过其独有的“熊市检查清单”工具，给出了一个值得认真对待的判断：当前市场并非处于极端泡沫状态，但风险信号正在以2008年全球金融危机以来最快的速度积累。\n\n这份报告的核心贡献不在于预测拐点何时到来，而在于提供了一个审视市场脆弱性的结构化框架。它回答了一个投资者每天都在面对的问题：下一次下跌，是应该买入的机会，还是应该警惕的转折点？\n\n研报的结论是，目前全球熊市检查清单已亮起10面红旗（满分18面），美国市场更是高达11.5面。这已经进入了历史上“红旗数量一旦达到两位数，往往加速上升”的危险区间。但与此同时，该行仍维持对全球股市到年底的积极看法，因为尚未达到“过度狂热的临界点”。\n\n这个看似矛盾的立场，恰恰是当前市场最值得拆解的地方。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 熊市检查清单告诉你：风险正在从“量变”转向“质变”\n\n理解这份研报的关键，在于理解其分析工具的设计哲学。熊市检查清单不是用来预测市场拐点日期的水晶球，而是一套用于评估“市场底层脆弱性”的指标体系。它涵盖了18个因子，包括估值、情绪、信用利差、收益率曲线、资金流、企业基本面与融资活动等。\n\n每个因子设有两个阈值：先跨过“琥珀色”警戒线，再进入“红色”危险区。每个红色信号计1分，琥珀色计0.5分。当总分数接近两位数时，就意味着市场已经进入了历史上容易发生系统性风险的区间。\n\n现在，全球得分10/18，美国11.5/18，欧洲5/18。这个数字本身并不足以判定立即转空，但它揭示了一个重要趋势：风险积累的速度在加快。研报明确指出，一旦红旗数量达到两位数，历史上它往往倾向于更快地上升。这意味着，当前市场可能正处于从“可控\n\n[... middle omitted ...]\n\n告的详细数据和图表，进一步拆解这些尚未充分定价的结构性风险。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球股市接近历史新高，但某外资投行最新研报显示，他们的“熊市检查清单”已升至次贷危机后最高水平。不过别慌，还没到“极度亢奋”的程度。\n\n📈 **信号在累积，但未亮红灯**\n全球BMC目前亮起10/18个警示旗（美国11.5/18，欧洲5/18）。这是2008年金融危机以来最“泡沫化”的水平，但比2000年（17.5/18）和2007年（13/18）的峰值还差得远。\n\n🔍 **哪些指标在拉警报？**\n1. 估值偏高：全球CAPE达36倍，美国更高达46倍（2000年峰值48倍）。股息率仅1.6%，接近历史低位。\n2. 情绪过热：Levkovich指标已进入“ euphoric”区间，分析师看多情绪增强。\n3. 企业行为激进：资本开支增长21%（主要来自AI相关投入），IPO活动推升警示。\n4. 资金持续流入：近3年股票基金流入占市值比达1.1%，已触发警戒。\n\n🌡️ **还没到最热的时候**\n研报认为，虽然警示旗数量在增加，但整体尚未达到“过度亢奋”状态。关键区别在于：信用利差仍处于低位（高收益债利差263bp），企业资产负债表相对健康（净债务/EBITDA仅1.3倍）。\n\n⚠️ **需要关注的转折**\n一旦B\n\n[... middle omitted ...]\n\nhile acknowledging that risks are building.\n\nExuberance Building — Global equities have continued to climb, accompanied by clearer signs of exuberance. Valuations across several segments appea\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R002",
    "title": "市场真正低估的不是通胀，而是增长下行对利率曲线的重定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是通胀，而是增长下行对利率曲线的重定价\n\n在日债市场经历了数月的高波动后，一个关键信号正在浮现：10年期日本国债收益率开始企稳，盈亏平衡通胀率不再创新高。这份来自某外资投行日本利率策略团队的报告，提出了一个与当前市场主流叙事截然不同的判断——市场正在过度定价通胀风险，而低估了中东局势持续化对日本经济增长的实质性拖累。\n\n报告的核心主张清晰且具有操作性：10年期日债的腹部曲线仍隐含约30-40个基点的通胀风险溢价，如果市场焦点从“通胀超调”转向“增长下行”，这部分溢价将大概率压缩，带来可观的多头机会。\n\n这不仅仅是一次战术性的利率交易建议。它触及了一个更深层次的结构性问题——日本央行是否已经落后于曲线，以及市场是否正在重蹈“过度反应通胀、忽视增长”的覆辙。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 通胀风险溢价正在从高位回落，但市场仍定价了“最坏情景”\n\n报告通过两个独立框架交叉验证了当前10年期日债中隐含的通胀风险溢价。第一个框架基于OIS公允价模型，将10年期OIS利率与实际观测值之间的残差与盈亏平衡通胀率进行对比，发现二者走势高度吻合，残差规模大致对应30-40个基点。第二个框架则比较了市场定价的盈亏平衡通胀率与调查预期的通胀率——后者目前仍在2%以下横盘，而前者高出约30个基点。\n\n这两个框架指向同一个结论：即使通胀超调担忧已经有所缓和，市场仍然在为“最坏的通胀情景”定价。而这份报告恰恰认为，这个最坏情景发生的概率正在下降。\n\n关键在于，支撑这一判断的不是抽象的理论推演，而是具体的微观证据。报告引用了日经CPINow追踪数据，显示超市价格——最接近消费者感知通胀的指标——持续减速。POS零售销售的实际同比增速仍处于负值区间。4月是企业集中调价的时间窗口，但今年的涨价压力明显弱于上一个\n\n[... middle omitted ...]\n\n关键变量的变化，并分享更多基于原始报告的二阶推导和交易思路。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本国债正在出现一个有趣的信号📈\n\n**10年期日债还能涨多少？**\n\n日本央行落后曲线的担忧有所缓解，但中东局势仍不确定。\n\n1️⃣ **通胀风险溢价正在下降**\n10年期日债开始企稳，盈亏平衡通胀率没有创新高。研报估算当前曲线中部仍有30-40bp的通胀风险溢价——如果市场焦点从通胀转向增长下行，这部分溢价有压缩空间。\n\n2️⃣ **央行vs市场：谁更鹰？**\n日央行表态偏鹰，但市场已经定价了近3次加息（12个月内）。这意味着前端进一步重定价空间有限。行长植田提到油价上涨对增长是压力，但更关注物价上行风险。\n\n3️⃣ **实际数据不支持通胀加速**\n4月CPI剔除特殊因素后并不强。日经CPINow追踪的超市价格持续减速，POS零售销售实际同比仍为负。企业开始谨慎转嫁成本——担心失去客户。\n\n4️⃣ **增长风险开始浮现**\n1-3月资本支出（除AI相关软件）环比-3.5%，中东不确定性已在影响企业决策。如果紧张局势持续，供应链中断会进一步暴露增长脆弱性。\n\n5️⃣ **10年期还有多少下行空间？**\n模型显示10年OIS与公允价值的差距主要来自通胀预期。若增长担忧占主导，这部分30-40bp的风险溢价有望\n\n[... middle omitted ...]\n\nerns have eased.   \n- BoJ communication remains hawkish, but the market already prices nearly three hikes over the next 12 months, leaving limited room for further front-end repricing.   \nIf p\n\n[... middle omitted ...]\n\nents carefully before investing.\n\nThe following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Koichi Sugisaki; Hiromu Uezato.\n\n© 2026 MS"
  },
  {
    "id": "R003",
    "title": "亚洲市场真正被低估的不是AI，而是“安全”主题驱动的工业投资超级周期",
    "digest": "[wechat_article.md]\n# 亚洲市场真正被低估的不是AI，而是“安全”主题驱动的工业投资超级周期\n\n当前全球投资者对亚洲的关注几乎全部集中在AI算力与半导体扩张上。这份来自某外资投行策略团队的最新报告却提出了一个更值得推敲的命题：市场正在经历的不是单一技术主题的行情，而是由“安全”与“AI”两大主题碰撞所产生的投资超级周期。报告将这一框架定义为“Security（能源安全、经济安全、国防安全）与AI Compute的碰撞”，并明确指出，在这一周期中，上游行业与金融板块将持续跑赢消费与服务。\n\n这一判断的时间窗口设定在2026年中期至2027年中，覆盖MSCI亚洲（除日本）及日本、中国、韩国、印度等主要市场。报告的核心主张并非简单看多亚洲，而是指出“主题的集中度正在发生结构性偏移”。对于产业决策者和长期投资者而言，真正需要追问的不是AI还能涨多少，而是“当市场从Compute向更广泛的工业与材料领域扩散时，哪些资产类别和地区将获得重新定价”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 真正的超级周期来自“安全”与“AI”的碰撞，而非AI单点驱动\n\n报告将当前亚洲市场的驱动力归纳为三大主题的碰撞：AI基础设施、能源与经济安全、国防安全。这不是三个并列的主题，而是一个相互强化的闭环。AI算力的指数级增长需要海量电力与冷却基础设施，这直接拉动了可再生能源、储能系统与电气设备的需求；而能源安全与供应链本地化的诉求，又反过来加速了各国对关键矿产、半导体自给以及国防工业的投资。\n\n从报告提供的主题暴露度数据来看，亚洲/新兴市场在“AI与技术扩散”主题上的暴露度高达57%，与北美持平。但更关键的是，亚洲在“未来能源”主题上的暴露度为16%，在“多极世界”主题上的暴露度为4%。这意味着，亚洲市场在安全相关主题上的结构性敞口正在扩大，而这部分资产目前尚\n\n[... middle omitted ...]\n\n的原始图表与目标价表格，并围绕上述三个验证指标进行持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲投研超级周期：AI与安全驱动的新机会\n\n亚洲竞争重塑中的主题机会\n\n最近翻到某外资投行一份亚太策略报告，核心逻辑很清晰：亚洲正处在一个由AI基础设施、能源/经济安全和国防支出共同驱动的投资超级周期。\n\n几个关键判断分享给大家：\n\n1️⃣ 主题集中在哪里？\n日本、韩国、台湾是主题机会最密集的区域，新加坡和中国也在改革议程中受益。整体看，工业、材料和能源板块前景强劲，消费和服务相对滞后。\n\n2️⃣ 关注上游和金融\n研报明确偏好上游行业和金融板块，而非消费/服务。商品板块目前落后于计算和资本品，存在补涨机会。\n\n3️⃣ 核心持仓方向\n重点集中在可再生能源和储能、半导体本土化、AI计算基础设施、国防和电气设备领域。\n\n4️⃣ 区域配置偏好\n北亚优于南亚和澳洲，日本是首选市场。中国仍处于通缩环境，更看好A股而非H股，强调资本开支而非消费。\n\n5️⃣ 不确定性仍高\n研报特意设置了较宽的牛熊目标价区间，说明当前环境异常不确定。MSCI新兴市场目标价1800，但熊市可能跌至1100，牛市可达2100。\n\n6️⃣ 新兴市场反弹性质\n目前看更像周期性反弹，而非新长期牛市的开端。\n\n这份报告的思路很清晰：在AI和安全两大主题的\n\n[... middle omitted ...]\n\nlso includes Singapore and China.\n\nA super-cycle of investment in Security (Energy, Economic and Military) and AI Compute are driving a strong outlook for the Industrials, Materials and Energy\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R004",
    "title": "印度央行的真正信号：用非利率工具保卫卢比，而非加息",
    "digest": "[wechat_article.md]\n# 印度央行的真正信号：用非利率工具保卫卢比，而非加息\n\n当市场普遍预期印度央行可能通过加息来应对卢比贬值和通胀上行时，6月政策会议给出了一个完全不同的答案。印度储备银行不仅维持政策利率在5.25%不变，还推出了一整套旨在吸引资本流入的“政策火箭炮”——从降低外资准入壁垒、提供税收优惠，到直接补贴银行的汇率对冲成本以动员海外存款。这组措施传递的核心信号是：印度央行选择用非利率工具管理国际收支压力，而非通过加息来牺牲增长。\n\n这份来自某外资投行的研报解析，揭示了一个被市场低估的关键判断：印度央行已经无意中为自己设定了极高的政策偏离门槛。在将FY27通胀预测大幅上调50个基点至5.1%、同时将GDP增长预测下调30个基点至6.6%的背景下，依然维持利率不变，这意味着通胀需要趋势性大幅走高，才能触发任何紧缩行动。真正值得关注的不是利率走向，而是这套资本流动管理工具对印度资产定价和汇率预期的重塑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政策火箭炮的核心：一次针对国际收支缺口的定向资金动员\n\n研报明确指出，印度央行此次推出的措施规模可观，足以缓解国际收支压力。根据该行测算，在政策出台前，印度FY27的国际收支赤字预计高达约700亿美元。而其中一项关键工具——通过FCNR(B)窗口动员海外存款——有望单独吸引约400亿美元的资金流入，相当于GDP的约1%。\n\n这个数字并非凭空而来。研报回溯了历史经验：2013年“缩减恐慌”期间，类似的FCNR(B)方案曾带来约260亿美元流入；而1998年和2000年的干预记录表明，这类工具通常能吸引约1% GDP规模的资金。当前方案的关键创新在于，央行将全额承担银行的汇率对冲成本，这对当前面临国内存款短缺的银行而言，意味着一种成本极低的融资渠道。同时，这些存款将免于现金准备金率和法\n\n[... middle omitted ...]\n\n视角的碰撞。这些未解的问题，恰恰是投资判断中最有价值的部分。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度央行：不动利率，猛搞汇率\n\n稳住汇率，利率不动\n\n印度央行这次的操作很有意思：政策利率按兵不动（5.25%），但一口气放出一堆吸引外资的“大招”。核心逻辑是——不用加息保汇率，而是用非货币政策工具来稳住外部压力。\n\n1/ 央行工具箱全开\n- 降低外资进入门槛：扩大政府债券可投资范围，放松短期投资限制\n- 给海外存款“贴钱”：银行通过FCNR(B)窗口吸收3-5年外币存款，央行全额补贴对冲成本，还不占用准备金\n- 鼓励国企借外债：提供优惠汇率掉期，窗口到9月底\n- 收紧出口收汇时间：从15个月缩回9个月\n\n2/ 规模有多大？\n研报估算，FY27印度国际收支缺口约700亿美元。仅FCNR(B)存款一项，按历史经验可吸引约400亿美元（≈GDP的1%）。这招在2013年“缩减恐慌”时就用过，效果不错。\n\n3/ 通胀涨了，增长降了\n- FY27通胀预测从4.6%上调至5.1%\n- GDP增长预测从6.9%下调至6.6%\n但央行明确表示：不会对每次通胀偏离都反应，要等通胀压力“普遍化”再动手。\n\n4/ 研报判断\n央行给自己设了很高的加息门槛——通胀都预测到5.1%了还不加息，意味着需要通胀大幅超预期才会行动。叠加增\n\n[... middle omitted ...]\n\npatriation of export proceeds, and very importantly, the RBI will subsidise the hedging of increased ECBs by public sector companies, and for banks to attract offshore deposits through the FCN\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R005",
    "title": "台湾市场真正的再定价，不是科技股，而是金融与化工",
    "digest": "[wechat_article.md]\n# 台湾市场真正的再定价，不是科技股，而是金融与化工\n\n当大多数投资者仍将目光聚焦在台积电与AI半导体时，一份来自某外资投行的FTSE台湾指数系列季度调整报告揭示了另一个正在发生的结构性变化：资金正在从科技硬件与半导体板块大规模流出，流向银行、化工、电信和资本品。这不仅是季度调仓的技术性操作，更可能标志着被动资金对台湾市场行业权重的重新定价。\n\n2026年6月5日收盘后，FTSE Russell公布了其台湾指数系列的季度审核结果，所有调整将于6月18日收盘后生效。表面上看，这只是指数成分股的常规更替，但深入拆解数据后，我们发现这次调整的规模、方向以及隐含的信号，远比一次普通的季度调仓更具分析价值。\n\n本次调整最值得关注的判断是：市场真正低估的不是科技股的增长，而是非科技板块在被动资金流中的结构性权重重置。科技硬件与半导体板块将面临约24亿美元的净被动资金流出，而银行、化工、电信与资本品板块合计将吸纳超过27亿美元的净流入。这种资金流向的逆转，不是短期交易噪音，而是指数方法论与市场结构共同作用的结果。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这次调仓的规模远超市场预期，资金流向呈现明显的行业轮动特征\n\n根据报告测算，本次FTSE台湾指数系列调整可能产生总计130至140亿美元的双向被动资金流。其中，台湾50指数的权重调整幅度约为1.4%，而台湾高股息指数的权重调整幅度高达23.6%。这意味着后者的成分股结构正在经历一次实质性重组。\n\n从行业层面看，资金流向的分布极不均衡。银行板块预计获得约9.9亿美元的净被动资金流入，化工板块约7.5亿美元，电信服务约5.9亿美元，资本品约4.5亿美元。与之形成鲜明对比的是，科技硬件与半导体板块预计净流出约23.7亿美元。这种规模的单行业资金流出，在台湾市场的历史记录中并不常\n\n[... middle omitted ...]\n\n多产业决策者和专业投资者一起，持续跟踪台湾市场的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n台股指数换血：谁被踢出，谁被买爆？\n\n**指数调仓解析**\n\n某外资投行最新研报拆解了FTSE台湾指数6月季度调整，6月18日收盘生效。这次变动不小，台湾50指数和台湾高股息指数同时换股，背后资金流向值得一看。\n\n**1/ 台湾50指数：4进4出**\n- 新加入：臻鼎-KY、贸联-KY、创意电子、南电\n- 被剔除：中钢、台塑、和泰车、合一\n- 权重调整幅度约1.4%，整体变动不大\n\n**2/ 台湾高股息指数：大换血**\n- 新加入：华邦电、南亚塑胶、南亚科、远传、中兴电\n- 剔除：儒鸿、东阳、东和钢铁、台表科\n- 权重调整幅度达23.6%，远超台湾50指数，意味着被动资金流入流出会非常剧烈\n\n**3/ 行业资金流向**\n- 最大被动净流入：银行（约10亿美元）、化工（约7.6亿）、电信（约5.9亿）、资本品（约4.6亿）\n- 最大流出：科技硬件与半导体（约24亿美元）\n- 总双向被动交易规模预估130-140亿美元\n\n**4/ 历史规律参考**\n台湾50新加入成分股在公告前表现弱于被剔除股，但公告后至生效日前后通常有超额表现，随后可能反转。高股息指数新加入成分股则公告前后都明显跑赢。\n\n**5/ 个股被动买入\n\n[... middle omitted ...]\n\nlectronics (2344), Nan Ya Plastics (1303), Nanya Technology (2408), Far Eastone (4904), and Chung-Hsin Electric (1513) will replace Makalot Industrial (1477), Tong Yang Industry (1319), Tung H\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "指数调仓不只是换股，它正在重新定价澳洲市场的结构性偏移",
    "digest": "[wechat_article.md]\n# 指数调仓不只是换股，它正在重新定价澳洲市场的结构性偏移\n\n每年六月的S&P/ASX指数季度调整，在多数投资者眼中不过是成分股进出与被动资金再平衡的技术性事件。但某外资投行刚刚发布的2026年6月调仓分析报告揭示了一个更值得关注的信号：这次调仓引发的被动资金流向，正在暴露澳洲市场内部一个被低估的结构性偏移——资源板块的权重扩张与消费板块的持续萎缩，并非周期性的轮动，而是资本对澳洲经济结构变化的长期定价。\n\n这不是一次普通的指数维护。这是市场在告诉投资者，谁在获得定价权，谁正在失去。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 被动资金流向揭示的板块优先级：资源与资本品在吸走流动性，消费零售在失血\n\n本次调仓最直观的信号来自资金流向的行业分布。根据报告估算，ASX 200指数调仓将产生超过9亿美元的被动双向交易流量。其中，金属与采矿板块将获得约7200万美元的净被动买入，资本品板块紧随其后，净流入约4500万美元。与此同时，消费者零售与服务板块面临约8000万美元的净卖出。\n\n这一流向并非偶然。五只新纳入ASX 200的成分股中，有三只来自金属与采矿板块——Elevra Lithium、Minerals 260、FireFly Metals。而五只被剔除的成分股中，有三只属于消费者零售与服务板块——Guzman y Gomez、WEB Travel、IDP Education。\n\n这意味着，被动投资者正在系统性地将资金从消费端抽离，重新配置到资源与工业资本品端。这不是短期交易行为，而是指数编制规则背后所反映的市值变迁。当一个板块的上市公司市值持续增长，它就会在指数中获得更大权重，进而吸引更多被动资金；反之亦然。\n\n这里的关键洞察在于：被动调仓本身不是原因，而是结果。它反映的是过去一个季度乃至更长时间内，澳洲资本\n\n[... middle omitted ...]\n\n原文与更多数据图表，帮助你在信息不对称中建立自己的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nASX 200指数调整，被动资金流向一览\n\n**调仓时间节点**\n6月5日公布，6月19日收盘后生效\n\n---\n\n**1/ 换血比例不大，但个股影响明显**\n\nASX 200本次调整5进5出，权重调整约0.3%。但个股层面，被动资金进出量差异很大。\n\n新增股票中，Elevra Lithium、Electro Optic Systems、Minerals 260、FireFly Metals、Kingsgate Consolidated预计净流入约37-54百万美元，相当于其日均成交量的2.3-7.7天。\n\n被剔除的Guzman y Gomez、SiteMinder、WEB Travel等，净流出约13-29百万美元，部分股票流出量高达日均成交量的5-7天。\n\n**2/ 行业层面：金属采矿和资本品最受益**\n\n按行业汇总，金属采矿板块预计净流入约72百万美元，资本品板块净流入约45百万美元。\n\n消费者零售板块净流出约80百万美元，软件服务净流出约26百万美元。\n\n整体来看，本次调仓预计产生约9亿美元的双向被动交易量。\n\n**3/ 历史规律：公布日后股价仍有波动**\n\n研报数据显示，新增股票和被剔除股票在公布前2\n\n[... middle omitted ...]\n\n)\n\nIndex Implications: The proforma index cap is estimated at US\\$1,873 billion for ASX 200. Following the rebalancing, forward 12-month P/E is expected to shift from 16.6x to 16.7x, trailing \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "日本股市的真正叙事不是避险，而是“增长时刻”的重新定价",
    "digest": "[wechat_article.md]\n# 日本股市的真正叙事不是避险，而是“增长时刻”的重新定价\n\n当全球投资者还在把日本视为“低利率避风港”或“治理改革故事”时，某外资投行最新发布的日本权益策略报告提出了一个更大胆的判断：日本正站在一个“大增长时刻”的前夜。这个判断的核心，不是通胀、不是汇率、甚至不是公司治理改革本身，而是这些结构性力量正在汇聚成一个新的宏观组合——AI投资加速叠加财政信誉支撑的利率稳定。在这个组合下，增长型股票的重新领导，可能比市场预期的来得更快。\n\n这份报告的标题直接点出了方向：Prepare for the Great Growth Moment。这不是一个温和的“看好”，而是一个明确的“准备”指令。对于长期关注日本市场的投资者来说，这句话的分量在于，它意味着市场正在从“估值修复”阶段切换到“增长溢价”阶段。而这两个阶段的投资逻辑，几乎完全不同。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场低估了日本从“通缩修复”切换到“增长定价”的速度\n\n过去三年，日本股市的上涨主要靠两个引擎：一是公司治理改革推动的估值修复，二是日元贬值带来的出口盈利。但这份报告指出，这两个引擎正在让位给一个新的驱动力——结构性增长。\n\n报告的核心判断基于四个结构性支撑：持续稳定的通胀、政治稳定带来的政策可预期性、公司治理改革的深化，以及家庭资金通过NISA体系加速流入股市。这四个因素单独看都不算新消息，但组合在一起，它们指向一个关键转变：日本经济正在从“低通胀、低利润率、低增长”的旧均衡，走向“温和通胀、企业定价权增强、资本开支回升”的新均衡。\n\n这意味着，过去十年有效的“便宜买入、等治理改革推升估值”的策略，可能不再是最优解。在增长型股票重新获得领导力的环境下，投资者需要重新审视哪些行业和公司真正具备“增长溢价”的资格，而不是仅仅依赖估值修复的贝\n\n[... middle omitted ...]\n\n以及不同情景下的组合构建策略等方面，还有大量值得拆解的内容。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本股市：准备迎接“大增长时刻”\n\n日本股市的“大增长时刻”\n\n📈 四重利好叠加，日本股市结构性牛市正在强化\n\n**1. AI投资加速 + 利率稳定**\n如果AI投资加速，叠加日本财政信誉带来的利率稳定，成长股很可能重夺领导地位。某外资投行仍将AI行情持续作为基准情景。\n\n**2. 治理改革持续推进**\n6月股东大会+7月公司治理准则修订，预计将推动企业更有效使用现金。改革加速有望提升ROE，通过PBR/PER扩张支撑日股。\n\n**3. 通胀走向稳定**\n日本正转向通胀逐步接近2%目标的阶段。这意味着可持续增长、工资上涨、更灵活的定价、更强的资本支出和更高的生产率。\n\n**4. 家庭资金入市**\nNISA制度支持家庭资产配置转向权益。2027年1月起“Kids NISA”计划启动，18岁以下每年可免税投资60万日元。\n\n**关于汇率：日元不再是唯一驱动**\n过去10年，日股对美元/日元的敏感度明显下降。企业通过提价改善利润率，使盈利对日元升值的脆弱性降低。\n\n**行业偏好**\n上游B2B供应链板块更受青睐。银行股虽因利率上升受益且交易不拥挤，但研报维持中性配置。\n\n**三大情景**\n- 基准：TOPIX 43\n\n[... middle omitted ...]\n\nimportant: We believe puts on stocks that have been bid up on AI narratives but lack fundamental earnings support represent one of the more effective risk-management tools in the current envir\n\n[... middle omitted ...]\n\nee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R008",
    "title": "铝的全球供给故事，远不止一个“中国限产”那么简单",
    "digest": "[wechat_article.md]\n# 铝的全球供给故事，远不止一个“中国限产”那么简单\n\n市场正在用中国产能天花板的故事来定价铝价，但这份外资投行的专家访谈揭示了一个更复杂的图景：中国供给侧的约束确实在收紧，但来自印尼和中东的变量正在改写全球铝的供需方程。真正值得关注的，不是中国产量会不会下降，而是全球新增供给的兑现节奏，以及地缘政治风险如何重塑铝的贸易流向和定价权。\n\n这三股力量——中国的“名义天花板”与“实际超产”、印尼的“产能雄心”与“执行困境”、中东的“供给中断”与“恢复不确定性”——叠加在一起，正在创造一个结构性的供给博弈格局。报告的核心判断是：市场可能低估了印尼产能爬坡的摩擦成本，同时也高估了中国减产的力度。而中东的供给缺口，则可能在2026年成为全球铝价最关键的边际变量。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国的“天花板”与“超产”并存，政策容忍度才是真正的锚\n\n专家估计中国2026年铝产量将达到4550万吨，较2025年的4450万吨增长2%。这个数字本身并不令人意外，但背后的结构性细节值得拆解。\n\n报告指出，当前中国有效运行产能已经超过4550万吨，其中包含了约60-70万吨的“历史违规产能”——这些项目在三到五年前启动，尚未获得最终批准，但在申请阶段就已经建成并投产。地方政府出于财政收入考虑，缺乏关停动力。这并非新现象，但专家提供了一个关键判断：中央层面的政策重心可能会逐步转向“通过碳合规来正式化历史产能”。一旦解决，授权产能上限可能上调至约4600万吨，与当前实际运行水平基本一致。\n\n这意味着什么？市场普遍讨论的“产能天花板”可能不是一个硬约束，而是一个正在被政策重新定义的软约束。投资者需要关注的不是中国产量会不会下降，而是政策何时、以何种方式将“事实上的超产”转化为“名义上的合规”。\n\n此外，产能置换\n\n[... middle omitted ...]\n\n判断。这些未被报告完全回答的问题，恰恰是未来市场定价的核心。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球铝市，三个关键变数\n\n全球铝供应格局正在重塑\n\n🔍 最近看了份外资投行的铝行业深度研报，核心逻辑很清晰：中国控产、印尼爬坡遇阻、中东供给中断，三条线交织，2026年全球铝供需格局可能比想象的更紧。\n\n**1️⃣ 中国：产能天花板真的“天花板”了？**\n专家预计2026年中国铝产量4550万吨（+2% vs 2025）。市场担心的超产问题，主要有四个来源：\n- 历史遗留的未批产能仍在运行（约60-70万吨/年）\n- 产能置换时新旧交替不同步，新产能先开、老产能后关\n- 少数企业提高电流强度提产，但空间有限\n- 电解槽升级带来小幅单产提升\n关键点：地方政府因税收贡献大，缺乏减产动力。中央层面未来可能通过碳合规将遗留产能“转正”，届时合规产能上限可能升至~4600万吨，与当前实际运行水平接近。\n\n**2️⃣ 印尼：产能扩张雷声大雨点小**\n专家预计2026/27年印尼新增铝产能220万/200万吨，但实际执行风险很高：\n- 税收优惠是关键卡点。许多冶炼厂未获免税资格（进口税13.5%、出口税、企业所得税），导致利润压缩。Juwan和Adaro已积累~10万吨未售库存，Adaro若2027年前无法获批，2026年\n\n[... middle omitted ...]\n\nwaps are not fully synchronized. New capacity is often ramped up before legacy assets are shut, temporarily pushing output above approved levels. 3) Higher-amperage operations exist but remain\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/f5433cdaecc112955483d87e232d5bdfcb9c0388357c9bfcf8a2e4773d622f90.jpg)"
  },
  {
    "id": "R009",
    "title": "市场低估的不是美元走强，而是“低波动率”下美元定价逻辑的切换",
    "digest": "[wechat_article.md]\n# 市场低估的不是美元走强，而是“低波动率”下美元定价逻辑的切换\n\n2026年5月，某外资投行全球外汇策略团队做出了一项在一年内都未曾做出的判断：**开始看空欧元兑美元**，并将下半年目标区间从此前的1.20大幅下调至1.13-1.15。与此同时，该团队在5月重新转为美元多头。\n\n这个判断之所以值得关注，不是因为方向本身——市场上看多美元的声音并不少。真正值得深究的是**支撑这一判断的逻辑，与过去几个月市场习惯的叙事完全不同**。\n\n今年3月，该团队也曾战术性看多美元，但当时的逻辑是“对冲”。而现在，看多美元的基础是“低波动率环境下的利差交易、美国通胀数据意外上行、以及能源贸易条件改善对美国国际收支的结构性支撑”。\n\n这两轮看多，名字相同，内核不同。如果不理解这个切换，就很容易在美元交易中犯方向对、节奏错的错误。\n\n这份报告最核心的洞察不是“美元要涨”，而是：**在低波动率环境下，美元的定价权正在从避险逻辑转向利差与贸易条件逻辑，而这一切换才刚刚开始被市场定价。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利差交易锚定了后冲突时代的G10汇率，但高息货币的质量正在分化\n\n报告开篇就给出了一个清晰的实证观察：自地缘冲突爆发以来，G10货币的回报几乎完全由“事前利差”解释。做多高息货币、做空低息货币的策略，在过去几个月里是最稳定的收益来源。\n\n但这份报告真正有价值的部分，不是重复“利差交易有效”，而是指出了一个正在发生的边际变化：**高息货币的宏观质量正在下降。**\n\n该团队跟踪了一套名为T.E.A.M的多信号宏观评分体系，涵盖利差、增长、股票动量、商品贸易条件动量、估值和防御性隐含波动率。过去一个月，这套评分体系的变化方向，明显有利于中低息货币，而非高息货币。\n\n这意味着什么？利差交易虽然仍然有效，但它的“安\n\n[... middle omitted ...]\n\n波动率环境何时可能逆转”这两个未解问题，持续跟踪并更新判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元多头的底气在哪？低波环境下的货币博弈\n\n**封面：美元归来？**\n\n**低波环境下的货币再排序**\n\n---\n\n最近某头部外资投行发了份G10外汇策略，核心观点很清晰：**美元多头回来了，但不是因为避险，而是因为“低配版美国例外论”**。\n\n几个关键逻辑线，我帮你拆开看：\n\n**1/ 为什么美元现在能涨？**\n- 美国通胀数据连续超预期（通胀惊喜指数5月转正）\n- 劳动力市场依然有韧性，联储维持偏鹰\n- 美国能源自给率提升，油价涨反而利好美元（美国石油出口创纪录，美元对油价beta已转正）\n- 美股重新跑赢全球，资本回流\n\n**2/ 这波和3月那波不一样**\n- 3月做多美元是“避险对冲”\n- 现在是“低波环境下的利差交易”——美元本身是高息货币，且利差环境没有收缩\n\n**3/ 欧元被看空，是近一年首次**\n- 欧元区增长动能明显走弱，贸易条件恶化，实际利差收窄\n- 研报下调欧元/美元预测至1.13-1.15（此前1.20）\n- **用欧元做融资货币，买澳元**\n\n**4/ 利差交易仍在主导，但质量在下降**\n- 冲突以来，G10货币回报几乎完全由利差解释\n- 但高息货币的宏观质量在走弱，系统评分开始偏向\n\n[... middle omitted ...]\n\nient and inflation pressures keeping CBs cautious. Carry has anchored G10 post-invasion.   \n• We turned long-USD again in May on stronger signals out of the US and signs of entrenched EUR weak\n\n[... middle omitted ...]\n\n consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-\n\nparty."
  },
  {
    "id": "R010",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n某外资投行于6月初发布的中国基础材料行业调研纪要，在看似平淡的“需求仍弱”共识下，埋藏了一条被多数投资者忽略的主线：大宗商品的定价权正在从需求侧向供给侧转移。这不是一个短期交易逻辑，而是一个可能持续数年的结构性变化。\n\n该行分析师在完成对中国铝、铜、锂、钢及地产的实地调研后，给出了明确的板块排序：铝和铜优先于锂，锂优先于钢铁。这个排序表面看是供需分析的产物，但深入阅读报告会发现，真正决定排序的变量，并非传统意义上的“需求增长有多快”，而是“供给约束有多硬”。\n\n市场当前对基本材料的讨论，大多停留在“地产何时见底”“新能源能否对冲”的层面。但这份报告释放了一个更重要的信号：即便需求不再增长，供给侧的自我约束和政策性收紧，也足以改变部分商品的定价中枢。这恰恰是市场尚未充分定价的部分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 铝的供给约束正在从“政策限制”转向“经济性自我约束”\n\n铝是这份报告中最具结构性的品种。市场此前对铝价的担忧集中在社会库存高企——截至调研时，LME铝价年内上涨26%，而中国现货仅涨8%，价差背后是“软需求”的共识。但报告揭示了库存高企的三个非需求原因，每一个都指向供给侧的短期扭曲而非长期过剩。\n\n第一个原因是下游对当前价格水平的消化需要时间，企业缺乏补库意愿。这不是需求消失，而是价格传导的节奏问题。第二个原因更具信息价值：中国税务部门加强了对贸易发票的检查，导致原本隐匿在贸易商手中的“隐形库存”浮出水面，成为显性社会库存。这意味着，实际可流通的库存可能远低于统计数字。第三个原因则最值得关注——在铝价持续坚挺的激励下，部分生产商通过提升电流强度等方式增加了实际产出，增幅通常在低个位数百分比。但这种“超产”是以牺牲电解槽寿命为代价的，不可持续，\n\n[... middle omitted ...]\n\n铜、锂、钢四个品种的供给端变化，探讨新的定价框架和交易策略。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铝铜锂钢，谁在真回暖？\n\n投研笔记：材料端最新调研\n\n最近跟完某外资投行的大宗材料调研，分享几个有意思的点：\n\n**1/ 铝：出口在扛大旗**\n国内需求确实软，社会库存偏高。但出口端很猛——4月铝材加工企业订单同比高20-30%，5-6月预计延续。同时，部分违规超产被查，供给天花板还在。出口消化+供给收紧，淡季可能不淡。\n\n**2/ 铜：供给故事还没讲完**\n中东硫磺供应风险对大型矿商影响有限（高利润能cover成本）。长期需求逻辑（电网/新能源/AI）共识很强，但价格还没完全反映。供给端老矿枯竭、复产慢的问题没改善，战略储备需求也在抬头。\n\n**3/ 锂：短期稳，中期看不清**\n企业普遍认为15万/吨是下游能接受的价格底，但要冲击20万/吨，得看储能项目IRR能否承受。供给端：津巴布韦复产确认，江西矿虽停产但其他项目重启积极，中期供给压力不小。\n\n**4/ 钢：需求还在往下走**\n地产拖累持续，出口面临反倾销和高基数压力。但间接出口（通过成品出口）反而在增长，说明制造业韧性还在。产能置换政策收紧是长期工程，效果有待观察。\n\n**5/ 地产：仍在寻底**\n某全国中介预计2026年住宅销售面积同比再降7%，底部\n\n[... middle omitted ...]\n\nvely high social inventory, which suggests soft domestic demand, has been an overhang. Key reasons: First, it takes time for downstream to digest this year's price level, with limited appetite\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R011",
    "title": "数据中心真正的瓶颈不在需求，而在物理世界每年只能交付不到一半",
    "digest": "[wechat_article.md]\n# 数据中心真正的瓶颈不在需求，而在物理世界每年只能交付不到一半\n\n当几乎所有公开市场讨论都聚焦于AI算力需求是否可持续时，一份来自某外资投行的最新研报给出了一个截然不同的判断框架：需求信号已经清晰到无需争论，真正值得投资者关注的，是供给侧的物理约束如何重塑整个数据中心的竞争格局和资产定价。\n\n2025年，北美数据中心签约租赁容量达到15.6 GW，但实际交付的仅有3.4 GW。两者之间的缺口高达12.2 GW。这并非一次性偏差。从2021年到2025年，累计未交付容量已达到20.4 GW，且缺口正在以每年翻倍的速度扩大。2023年缺口为2.9 GW，2024年扩大到4.3 GW，2025年则直接跳升至12.2 GW。\n\n这不是一个需求故事。这是一个关于物理世界如何为数字世界设定天花板的故事。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 六大物理约束决定了可交付容量的上限，而非资本意愿\n\n研报建立了一个专有的数据中心容量交付模型，将供给天花板拆解为六类约束：EPC与劳动力、冷却系统、电力变压器、开关设备、不间断电源、以及燃气轮机。每个约束条件都对应一个独立的物理上限，而最终可交付容量由最紧的那一个决定。\n\n模型测算显示，2026年北美可交付容量的上限约为10.4 GW，而这一数字的约束变量是EPC与劳动力。这意味着一件事：即使所有其他环节都准备就绪，没有足够的技术工人和工程总包能力，项目就无法按时通电。冷却系统几乎并列为约束条件，上限为11.4 GW，并从2028年起成为最主要的瓶颈。\n\n这一分析框架的核心洞察在于：数据中心的供给瓶颈不是线性的，而是多约束条件下的短板效应。过去市场习惯于用资本开支预测未来供给，但资本可以在一夜之间增加，而熟练电工、冷却工程师、以及高压变压器制造产能的扩张周期是以年为单位计算的。\n\n[... middle omitted ...]\n\n更深入的交流。完整报告及其原始图表和数据，也可以在群内获取。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心缺口12GW，供不应求才刚开始\n\n数据中心供需失衡\n\n2025年北美数据中心缺口达12GW，租赁签约15.6GW，实际交付仅3.4GW。这个缺口从2023年的2.9GW一路飙升，2024年4.3GW，2025年直接翻倍到12.2GW。累积下来，2021-2025年未交付容量已达20.4GW。\n\n1️⃣ 需求端数据很实在\n超大规模云厂商资本支出2026年预计7700亿美元，是2023年的5倍。云服务积压订单飙到2万亿美元，增长速度快过资本支出3倍。光是GPU出货量就暗示2026年全球AI电力需求约30GW，北美占19GW。\n\n2️⃣ 供给端卡在6个瓶颈\nEPC和劳动力是2026年最紧的约束，上限10.4GW。冷却系统紧随其后，11.4GW上限，到2028年将成为主要瓶颈。建设中的数据中心是2025年交付量的6倍多，但交付速度跟不上。\n\n3️⃣ 谁在受益\n空置率1-3%，批发租金加速上涨。比特币矿企转型AI数据中心成为新玩家，他们手里有现成的场地和电网连接，能绕过漫长的排队周期。设备供应商的订单增长是收入增长的2-4倍，积压订单持续扩大。\n\n4️⃣ 租期在拉长\n以前超大规模客户只承诺12-18个月交付的容\n\n[... middle omitted ...]\n\nn pace for \\$770B in CY26E, up 74% YoY and nearly 5x the \\$156B deployed in CY23. Combined cloud backlog surged to \\$2T in 1Q26, growing 3x faster than capex since CY23. Bottom-up accelerator \n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R012",
    "title": "市场低估的不是息差收窄，而是亚太银行股资本回报的结构性重定价",
    "digest": "[wechat_article.md]\n# 市场低估的不是息差收窄，而是亚太银行股资本回报的结构性重定价\n\n亚太银行板块正在经历一个被多数投资者忽略的范式转换。过去两年，市场对银行股的定价逻辑主要围绕利率周期展开——加息周期买入，降息周期卖出。这种框架在2023年以前确实有效，但它正在快速失效。某外资投行最新发布的亚洲银行深度研报传递了一个明确信号：驱动银行股回报的核心变量，正在从“净息差弹性”转向“资本回报纪律与资产质量拐点”。这一转换的幅度和持续性，很可能被当前市场定价所低估。\n\n报告覆盖了香港、新加坡、印尼、马来西亚、泰国、菲律宾六大市场的主要银行机构，并系统拆解了各自的行业结构、盈利驱动因子和估值锚点。与市场普遍关注的降息周期对息差的影响不同，该报告花了大量篇幅讨论资本回报率、股息支付率的提升空间，以及资产质量拐点是否已经到来。这些变量对银行股长期回报的解释力，正在超越传统的利率敏感度分析。\n\n本文基于该份研报的核心逻辑框架，提炼出五个值得产业决策者和投资者重点关注的判断。每个判断背后都有数据支撑，但更重要的是它们指向了一个共同的结论：亚太银行股的风险收益比正在发生结构性变化，而市场对此的定价仍不充分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 印尼银行的ROE弹性远超区域均值，但市场仍在用“新兴市场折价”定价\n\n在亚太主要银行市场中，印尼银行的ROE表现最为突出。根据报告数据，2025年印尼银行板块平均ROE达到18.4%，显著高于菲律宾的14.7%、新加坡的13.4%、马来西亚的11.1%和泰国的9.2%。这一差距不是偶然的，而是由三个结构性因素共同支撑。\n\n第一，印尼的私人部门债务占GDP比重不到50%，是区域内最低的水平之一。这意味着信贷渗透率仍有巨大的提升空间。报告显示，印尼银行2014至2025年的贷款复合增长率约为8%，远高于\n\n[... middle omitted ...]\n\n合最新的市场动态，与大家共同拆解这些尚未完全回答的关键问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n东南亚银行怎么选？一张表看懂\n\n| 东南亚银行全解析\n\n从印尼到新加坡，地区银行差异这么大\n\n最近翻到某外资投行的亚太银行暑期研修材料，把香港和东盟银行的核心逻辑拆得很清楚。整理几个关键发现👇\n\n**1/ 印尼：高增长高回报，但集中度高**\n- 贷款CAGR 8%（2014-25），私人债务/GDP不到50%，区域最低\n- 四大行主导，长尾中小银行多，可能继续整合\n- ROE 18.4%，区域最高，派息率也高（BRI达90%）\n\n**2/ 泰国：结构性问题拖累回报**\n- 家庭债务/GDP约87%，老龄化严重\n- 贷款增速降至2-5%，资产质量问题反复\n- ROE仅9.2%，银行在探索数字信贷和财富管理\n\n**3/ 菲律宾：低渗透但成本高**\n- 贷款增长恢复至10%（2025年），但成本收入比区域最高\n- 资本比率偏低，每轮信贷周期都要融资\n- ROE 14.7%，资产质量相对稳定\n\n**4/ 新加坡：成熟市场，靠费率和资本回报**\n- 贷款增速3-5%，利率是最大驱动因素\n- 三大行区域布局不同（DBS/OCBC侧重中国，UOB侧重东盟）\n- 财富管理费收入强劲，资本回报意识强\n- ROE 13.4%\n\n[... middle omitted ...]\n\nc49bb675e6bcebe5abed495066bce9c1abfbb97b060362e3f.jpg)\n\n<details>\n<summary>text_image</summary>\n\nAsia Summer School 2026\n</details>\n\n# ASEAN FINANCIALS\n\nAsia Pacific\n\nIndustry View In-Line\n\nMS\n\n[... middle omitted ...]\n\nhart Bank PCL (TTB.BK)</td><td>U (12/21/2023)</td><td>Bt2.28</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R013",
    "title": "中国汽车市场真正被低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 中国汽车市场真正被低估的不是需求，而是供给侧的再定价\n\n当市场普遍将注意力集中在“国内乘用车销量下滑11%”这个数字上时，一份来自某外资投行的最新年度展望给出了一个值得深思的框架：真正决定未来三年中国汽车产业投资回报的核心变量，不是终端需求何时复苏，而是供给侧正在发生的结构性重塑——从出口增长、新能源渗透率突破临界点，到自主品牌市占率的不可逆提升，再到智能驾驶的商业化落地。这些因素叠加在一起，正在重新定义每一家车企的盈利曲线和估值锚点。\n\n这份报告发布于2026年6月，覆盖了从整车厂到零部件、从ADAS到eVTOL的完整产业链，涉及超过40家上市公司。报告的核心判断是：尽管2026年国内零售市场面临短期压力，但中国汽车产业正处于一个“供给创造需求”的转折点。出口、新能源、智能化这三条主线，正在将行业从存量博弈拉入增量重构。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内零售的下滑并非系统性风险，而是政策退潮后的正常回摆\n\n报告预测2026年中国乘用车批发销量为2940万辆，同比下滑2%；但更值得关注的是零售端——国内零售预计为2140万辆，同比下滑11%。这个数字看起来令人不安，但需要放在正确的参照系中理解。\n\n2025年国内零售基数高达2400万辆，其中相当一部分是由国家及地方“以旧换新”补贴政策催化的。根据报告数据，2025年全年共有1150万辆新车申请了各类补贴，仅2026年第一季度就有140万辆。这意味着，2025年的高基数中包含了大量政策透支的需求。2026年的下滑，本质上是政策退潮后的正常回摆，而非内生需求的崩塌。\n\n更重要的是，报告同时预测2027年国内零售将恢复至2205万辆，2028年进一步回升至2227万辆。这种“V型”修复的假设背后，是报告对中国汽车保有量更新周期的判断——大量201\n\n[... middle omitted ...]\n\n重点公司的利润结构和竞争壁垒，并持续跟踪关键假设的验证进度。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026中国车市：内销降温，出海加速\n\n国内销量承压，出口才是新引擎\n\n某外资投行最新研报拆解了2026年中国车市的几个关键趋势，信息量很大，直接上干货。\n\n1️⃣ 内销下滑，但总量稳住\n- 2026年国内乘用车零售预计2114万辆，同比下滑11%\n- 但加上出口，总批发量预计2941万辆，仅微降2%\n- 出口才是增长主力：预计800万辆，同比猛增33%\n\n2️⃣ 新能源渗透率突破60%\n- 2026年新能源批发预计1754万辆，同比增长13%\n- 纯电占比35%，插混占比24%，燃油车只剩40%\n- 到2030年，新能源渗透率有望达到81%\n\n3️⃣ 智能驾驶进入商用元年\n- L3级自动驾驶开始商业化落地\n- L4级Robotaxi部署加速\n- 智能驾驶与座舱融合成为新战场\n\n4️⃣ 国产品牌市占率将达70%\n- 政策端：以旧换新补贴延续到2026年底\n- 新能源购置税减免逐步退坡（2026-2027年减半）\n- 出口市场：新能源出口预计增长88%\n\n5️⃣ 几个值得关注的细分赛道\n- 智能驾驶硬件（激光雷达、芯片）\n- 汽车电子零部件\n- 新能源车出口配套服务\n\n研报覆盖了从整车厂到零部件、经销商的完整链\n\n[... middle omitted ...]\n\nS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Inve\n\n[... middle omitted ...]\n\n>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$16.81</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R014",
    "title": "新兴市场资金外流正在从“局部撤退”演变为“全面撤离”",
    "digest": "[wechat_article.md]\n# 新兴市场资金外流正在从“局部撤退”演变为“全面撤离”\n\n一周之内，新兴市场股票基金的资金外流从43亿美元骤升至75亿美元。这个数字本身已经足够引人注目，但真正值得关注的不是外流的规模，而是它的结构：此前几周还相对稳定的非ETF赎回，本周突然加速至38亿美元，而ETF的流出也同步扩大至37亿美元。这意味着什么？意味着此前市场普遍认为的“被动资金暂时离场、主动资金仍在观望”的格局正在被打破。两类资金正在形成共振，而共振的方向是出逃。\n\n这份由某外资投行发布的资金流周报，提供了截至2026年6月3日的最新数据。报告的核心信号并不复杂：新兴市场的资金外流不仅在加深，而且在扩大。但如果我们只停留在“流出很多”这个层面，就错过了真正重要的判断——这一轮外流的结构性特征，正在改写我们对新兴市场资产定价的底层假设。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 主动与被动资金同步出逃，意味着“观望”阶段已经结束\n\n此前几周，市场一度出现了一个看似积极的信号：非ETF（主动管理基金）的赎回速度在放缓。部分投资者将其解读为“聪明钱”正在逢低布局。但本周的数据彻底推翻了这个假设。非ETF赎回从上周的12亿美元猛增至38亿美元，创下近期新高。与此同时，ETF的流出也从31亿美元扩大到37亿美元。\n\n这两类资金的同步放大，在逻辑上指向一个更值得警惕的判断：此前非ETF赎回的放缓并非主动管理人在“抄底”，而更可能是赎回指令的执行延迟或投资者在重新评估仓位。当新的负面信号出现后，这些延迟的赎回指令集中释放，造成了本周的加速。\n\n从更长的周期来看，非ETF资金已经连续多年呈现净流出。2024年全年非ETF净流出54亿美元，2025年进一步扩大至61亿美元，而2026年至今虽然有所收窄至11亿美元，但本周的数据表明这一改善趋势可能逆转。这意味\n\n[... middle omitted ...]\n\n及一群同样关注新兴市场的投资者，可以一起拆解这些复杂的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nEM 资金流出在加速，不只是扩大\n\n全球资金在撤出新兴市场\n\n这一周，EM 股票基金净流出从上周的 -43 亿扩到 -75 亿美元。ETF 和非 ETF 都在卖，之前非 ETF 赎回减速的迹象没延续，本周又回到 -38 亿。\n\n1. 区域分化明显\n全球新兴市场（GEMs）赎回从 -3.6 亿猛增至 -30 亿，亚洲除日本也扩大到 -44 亿。拉美和 EMEA 反而略有缓和，但绝对值还在流出。\n\n2. 韩国、印度是重灾区\n韩国本周流出 -75 亿，过去四周累计 -376 亿，年初至今 -696 亿。印度流出 -41 亿，比上周的 -4.5 亿大幅恶化。台湾连续第二周净流入，但速度放缓到 +38 亿。\n\n3. 少数亮点\n台湾和泰国是本周仅有的两个净流入市场，泰国小幅 +1.5 亿。EM 除中国基金有 +0.5 亿的边际流入，但体量很小。\n\n4. 全球资金流向对比\n美国股票基金本周净流入 +207 亿，发达欧洲流出 -10 亿。资金从新兴市场向发达市场迁移的趋势依然明显。\n\n年初至今，EM 股票基金累计净流入 668 亿，但已从 4 月高点 833 亿回落。ETF 贡献了 782 亿，非 ETF 反而净流出 115\n\n[... middle omitted ...]\n\ns eased in LatAm (-\\$225mn, -\\$268mn last week) and EMEA (-\\$5mn, -\\$75mn last week). EM ex-China funds saw marginal inflows (+\\$50mn). YTD, EM equity funds are +\\$66.8bn (from a peak of +\\$83\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 05 Jun 2026 01:42 PM HKT\n\nDisseminated 05 Jun 2026 01:43 PM HKT"
  },
  {
    "id": "R015",
    "title": "市场真正低估的不是AI需求，而是资本开支周期对估值框架的重构",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是资本开支周期对估值框架的重构\n\n当S&P 500的资本开支预计在2026年同比增长40%，并消耗约50%的经营现金流时，投资者面临的核心问题已经不是“AI是否真实”，而是“我们正在用什么尺子来定价这个周期”。某外资投行最新发布的美国权益策略研报提出了一个在当下极具操作意义的判断：在资本开支超级周期中，EV/EBITDA比P/E更能揭示未来三年的回报信号。这一结论的深意在于，它挑战了市场当前对科技巨头估值的主流叙事，并指向一个被大多数人忽略的结构性变化——资本开支的集中度和持续性，正在重塑估值框架的有效性。\n\n这份研报并非简单地看多或看空美国股市。它在近12个月内维持建设性立场，但明确提出，对于持有期超过三年的投资者，当前需要更高的选股门槛。这不是一个短期择时信号，而是一个关于估值工具选择与投资期限匹配的框架性建议。理解这一框架，比猜测下一季度的EPS更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本开支超级周期已经启动，但它的集中度前所未有\n\n研报数据显示，S&P 500总体资本开支在2026年预计同比增长40%，这是至少35年来的最快增速。这一水平，在历史上仅能与1990年代中后期的电信/互联网建设周期以及2000年代中期的能源和房地产投资热潮相提并论。但当前周期有一个关键区别：增长的来源极度集中。\n\n通信服务、科技和非必需消费品——本质上就是AI超大规模企业、芯片制造商及其直接供应链——贡献了绝大部分增量。TMT行业的资本开支占S&P 500总资本开支的比例，预计2026年将接近50%。这是一个历史性的跳跃，甚至相对于2010年代末的公有云建设时期而言，都是质的飞跃。\n\n这意味着什么？历史上，当资本开支强度达到这一水平时，即使是好的投资也可能过度。1990年代的\n\n[... middle omitted ...]\n\nV/EBITDA信号的详细拆解，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI投资的“超级周期”来了\n\n📊 资本开支进入新阶段\n\n最近某外资投行发布了一份研报，核心观点是：AI投资正进入一个类似90年代和2000年代的“资本开支超级周期”。简单说，就是企业花钱建AI基础设施的力度非常大。\n\n1️⃣ 规模创纪录\n标普500公司2026年资本开支预计同比增长40%，是35年来最快增速。其中，科技、通信服务和非必需消费（主要是AI超大规模企业、芯片商和供应链）贡献了大部分增长。TMT领域的资本开支占比将接近50%，比2010年代末的云计算建设还要激进。\n\n2️⃣ 估值信号变了\n当资本开支特别高的时候，传统的P/E（市盈率）估值指标容易失真，因为折旧、税收等会干扰利润。研报发现，EV/EBITDA（企业价值/息税折旧摊销前利润）这个指标在资本开支高峰期，对中期（比如3年）回报的预测能力更强。当前标普500的EV/EBITDA比P/E更贵，处于历史较高分位。\n\n3️⃣ 历史经验值得警惕\n回顾90年代电信互联网投资和2000年代能源地产投资，资本开支高峰期往往伴随过度投资。虽然AI投资长期可能提升生产力，但短期也会带来“价值毁灭”的风险——投入很大，但回报周期长，中间可能经历痛苦的调整。\n\n4\n\n[... middle omitted ...]\n\nnked Strategies and Portfolio Strategy categories.\n\n# Key Points & Highlights\n\n\\- Capex finds another gear. Aggregate S&P 500 capex is projected to grow 40% Y/Y in 2026 and is on track to abso\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R016",
    "title": "AI投资叙事尚未到顶，真正稀缺的是“从GPU到机柜”的全栈受益者",
    "digest": "[wechat_article.md]\n# AI投资叙事尚未到顶，真正稀缺的是“从GPU到机柜”的全栈受益者\n\n市场对AI硬件投资的讨论已经从“需求会不会放缓”演变为“哪些环节还能超预期”。某外资投行最新发布的亚太科技硬件投资者报告给出了一个值得认真对待的判断：AI依然是核心主线，但投资逻辑正在从“谁拿到了GPU”转向“谁在数据中心的物理重构中不可替代”。这份报告覆盖了从网络交换机、散热、电源测试到精密机械的完整供应链，其核心信号是——AI资本开支的结构性受益者正在扩散，而市场对这一扩散的定价仍不充分。\n\n为什么现在需要重新审视这个判断？2026年第二季度，市场对AI硬件股的估值分歧明显加大。部分投资者认为算力投资已进入平台期，供应链订单增速将自然回落。但该投行通过对比2026年和2027年的盈利预测发现，多家核心供应商的远期市盈率仍低于其历史中枢，而盈利上修的趋势尚未被完全计入。换句话说，市场低估的不是AI本身，而是AI对硬件产业链的渗透深度。\n\n报告提供了几个值得关注的新信号：网络交换机正在成为AI加速器的收入驱动力，光学解决方案的贡献时间点开始明确，电源测试设备因机柜功率密度提升而进入新周期，就连导轨、散热模组这类“不起眼”的零部件，也因为AI服务器机柜的标准化需求而获得了结构性增长动能。这些信号叠加在一起，指向一个更重要的结论——AI投资的下半场，考验的不是谁能造出更强的芯片，而是谁能把芯片变成可靠、高效、可规模化的物理系统。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI资本开支的受益者正在从GPU向“机柜内所有组件”扩散\n\n过去两年，市场对AI硬件投资的关注高度集中在GPU和AI加速器本身。只要英伟达的出货量增长，整个供应链就跟着涨。但这种“一荣俱荣”的逻辑正在被打破。该投行的报告清晰地展示了，AI资本开支的受益面正在从单一芯片扩展到整\n\n[... middle omitted ...]\n\n动化）有更深入的兴趣，也可以在群里提出，我们会组织专题讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI还在抢C位，产业链谁在受益？\n\nAI浪潮，谁在卡位？\n\n大中华区科技硬件，AI依然是主线\n\n最近翻了份某外资投行的研报，核心就一句话：AI仍然是科技硬件的主轴。不是概念，是实打实的订单和收入在落地。\n\n研报重点拆了几个细分方向，逻辑很清晰：\n\n**1/ 网络交换与互联**\n- 网络交换机是2026年主要营收驱动力，AI加速器收入预计下半年开始贡献\n- 光解决方案预计2027年才看到收入，但客户接触已经在进行中\n- 铜数据互联持续增长，受益于客户采用率提升和规格升级\n- 电源互联则靠服务器出货增长和下一代平台推高单机价值\n\n**2/ 测试与自动化**\n- 电源测试业务受益于服务器机柜功率密度提升和客户扩产\n- 半导体业务有多个驱动：新GPU SLT周期、先进封装量测工具、光模块/CPO测试、FT分选机和老化炉的潜在收入\n\n**3/ 工业自动化**\n- 处于周期早期复苏阶段，与全球制造业PMI数据一致\n- 科技行业需求最强劲：半导体、零部件、组装\n- 电池订单在中国也表现稳健\n- 龙头公司还有份额提升和新产品贡献的额外增长点\n\n**4/ AI资本支出受益者**\n- 在GPU和ASIC服务器市场都有主导地位的公\n\n[... middle omitted ...]\n\nmay have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.\n\n# For analyst certification \n\n[... middle omitted ...]\n\ntd>NT$168.50</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$243.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$402.00</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R017",
    "title": "日本汽车股的核心矛盾：风险已被定价，但结构性优势尚未被充分重估",
    "digest": "[wechat_article.md]\n# 日本汽车股的核心矛盾：风险已被定价，但结构性优势尚未被充分重估\n\n市场正在为一个“什么都对”的叙事买单：中东地缘风险、供应链中断、原材料成本飙升、中国竞争对手的挤压、电动化与软件化的投资黑洞。这些风险每一个都真实存在，每一个都足以让投资者对日本汽车板块望而却步。但某外资投行在2026年6月初发布的这份日本汽车行业研报，却给出了一个值得深思的信号——在所有这些负面因素都被充分讨论之后，部分个股的估值已跌至历史低位，而市场可能低估了其中一些公司通过结构性优势穿越周期的能力。\n\n这不是一个简单的“抄底”建议。报告的核心判断是：行业整体面临多重逆风，但个股之间的分化将比以往任何时候都更加剧烈。真正值得关注的，不是谁能躲过所有风险，而是谁能在风险中展现出定价权、区域优势和盈利韧性。这份报告的价值，在于它提供了一套在不确定性中筛选“相对强者”的框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场定价的“完美风暴”已经包含，但结构性变量才是分水岭\n\n研报开篇即点明了日本汽车厂商当前面临的五重逆风：中东局势引发的供应链中断风险、原材料价格上涨、汽车需求放缓、来自中国OEM的竞争压力，以及电动化与软件化的投资负担。这五重压力叠加，构成了一个几乎“完美”的看空叙事。\n\nS&P Global预测全球汽车产量将同比下降2%，这并非一个灾难性的数字，但足以让市场对行业前景保持谨慎。某外资投行将行业评级定为“In-Line”，既不乐观也不悲观，这本身就是一个信号：他们认为市场已经消化了大部分坏消息。\n\n关键在于，这些逆风对不同公司的影响程度截然不同。以原材料成本为例，报告假设每辆C-D级乘用车的成本将增加约8万日元（约500美元），其中约4万日元来自原油相关材料，另外4万日元来自钢铁、铝、铜、贵金属和半导体等其他材料。对于年销量数\n\n[... middle omitted ...]\n\n们对这些未解问题的持续跟踪讨论，欢迎来星球微信群里继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本车股，现在值得看什么？\n\n**日本车股的逻辑在变**\n\n某外资投行最新研报，把日本车企的现状和选股思路讲得很清楚。分享几个核心判断👇\n\n**1. 行业压力不小，但股价跌出了看点**\n中东局势带来三重冲击：供应链中断风险（霍尔木兹海峡）、原材料涨价、需求放缓（从燃油车转向混动和电动）。S&P预计全球汽车产量同比降2%。\n\n但股价回调后，部分公司估值变得有吸引力。铃木P/B已接近历史低位，本田、斯巴鲁、马自达的股息率约5%。\n\n**2. 每家公司的处境不一样**\n- **铃木（看好）**：印度市场汽油涨价影响需求，但提价部分抵消了成本压力，盈利基础相对扎实。\n- **丰田（中性偏积极）**：很可能逐步上调保守的业绩指引，混动业务有增长空间。\n- **五十铃（谨慎）**：北美商用车和泰国轻型商用车复苏难度大，实现目标挑战较高。\n- **本田/马自达/斯巴鲁等（中性）**：各有看点，但盈利或电化转型仍需观察。\n\n**3. 原材料成本怎么影响利润？**\n研报估算，C-D级乘用车单车成本增加约8万日元（约500美元），其中原油相关材料和其他材料各占一半。车企能否消化，是后续观察重点。\n\n**4. 别忘了政策变量**\n\n[... middle omitted ...]\n\n 3) lingering risk of auto production stoppages on supply-chain constraints as passage through the Strait of Hormuz has yet to be normalized, 4) higher raw material prices, and 5) a slowdown i\n\n[... middle omitted ...]\n\nha Motor (7272.T)</td><td>E (04/17/2025)</td><td>¥1,224</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "# BMC: Exuberance Building Global equities are making new all-time highs, while exhibiting some clear signs of exuberance. Valuations in many areas look stretched, sentiment is increasingly optimistic, and the pickup in IPOs/equity issuance points to strong de"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # BMC: Under the Hood We highlight developments in all most underlying factors of our BMC below, along with thresholds and shading to indicate past bear markets. Figure 3. MSCI AC World Trai"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. MSCI AC World Dividend Yield"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. MSCI AC World CAPE"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Global Equity Risk Premium"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Levkovich Index (Formerly Panic/Euphoria)"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Equity Fund Flows (3y as % of Mkt Cap)"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. Capex Growth"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. M&A And IPOs (% of Mkt Cap)"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Global Return on Equity (RoE)"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Global EPS (% From Previous Peak)"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 1: Polymarket: Strait of Hormuz traffic return to normal by end of June/July 2026 versus Japan 10y Breakeven"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The cumulative change in rates expectation across the curve since February 27th"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Weekly change in JGB and OIS curve"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Nikkei CPI T Index (y/y) vs. POS real retail sales (y/y)"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 5: Corporate capex investment (software versus ex software)"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 10y OIS residual versus 10y JGBi breakeven"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 7: Quick 10y inflation average forecast versus 10y JGBi breakeven"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Market Implied pace of 25bp hike in the following 12 months"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 9",
    "context": "Exhibit 9: BoJ Market pricing versus survey based inflation forecast"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Major eleven Japanese life insurance companies: Asset class outstanding"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Major eleven Japanese life insurance companies: Bond holdings by investment purpose classification"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Major eleven Japanese life insurance companies: JGB outstanding by maturity"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Cumulative net purchase flow of super-long JGBs in each fiscal year by Japan lifers and non-life insurances"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Major eleven Japanese life insurance companies: Core profits and its breakdown"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Japanese lifers' premium income and 30y JGB yield"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Major eleven Japanese life insurance companies: SWAPs (receive fix) and Swaptions (Receiver) outstanding"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Major eleven Japanese life insurance companies: Swaptions (Receiver) outstanding"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Major eleven Japanese life insurance companies: SWAPs (pay fix) and Swaptions (Payer) outstanding"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Major eleven Japanese life insurance companies: Swaptions (Payer) outstanding"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Major eleven Japanese life insurance companies: Foreign bonds outstanding"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Major eleven Japanese life insurance companies: foreign currency denominated bonds outstanding"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Monthly net purchase of foreign bonds by Japanese lifers"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Major eleven Japanese life insurance companies: Estimated JPY-hedged ratio"
  },
  {
    "figure_id": "F035",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: FTSE Taiwan 50: Additions have underperformed deletions in the two weeks ahead of the announcement; historical trends suggest post-announcement outperformance, followed by a potential reversal after the effective date"
  },
  {
    "figure_id": "F036",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: FTSE Taiwan Dividend+: Additions have significantly outperformed deletions; historical trends suggest moderate post-announcement outperformance to continue before the effective date"
  },
  {
    "figure_id": "F037",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ASX 200: Additions vs. deletions have traded along a highly volatile path ahead of the announcement; historically, post-announcement performance remains volatile with a modest negative bias, before rebounding around the"
  },
  {
    "figure_id": "F038",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Exhibit 4 - In 2025, Data Center Leases Signed Exceeded Actual Delivered Capacity by Over 12 GWs"
  },
  {
    "figure_id": "F039",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5 - Under Construction GW in North America is Over 6x the Capacity Delivered in 2025"
  },
  {
    "figure_id": "F040",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - Data Center Capacity Additions in North America (GW)"
  },
  {
    "figure_id": "F041",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2 - Installed Data Center Capacity Total in North America (GW)"
  },
  {
    "figure_id": "F042",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3 - Top 15 Data Center Operators/Owners in North America by Power (GW)"
  },
  {
    "figure_id": "F043",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 6 - JEF Data Center Demand Model Exhibit 7 - Leased vs Hyperscaler Installed Data Center Capacity (GW)"
  },
  {
    "figure_id": "F044",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8 - Leased vs Hyperscaler Lit Data Center Capacity (GW) # Data Center Demand is Robust Data center demand continues to accelerate. Hyperscaler capex is on pace for \\$770B in CY26E, up 74% YoY and nearly 5x the \\$156B deplo"
  },
  {
    "figure_id": "F045",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 9 - Hyperscaler Capex Estimates Revised Higher Through 1Q26 Earnings"
  },
  {
    "figure_id": "F046",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10 - Monthly Tokens Processed Across All Google Surfaces"
  },
  {
    "figure_id": "F047",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "Exhibit 11 - AI Accelerator-Implied Power Demand vs. N.A. Incremental DC Supply Additions, Driving Structural Tightness (GW)"
  },
  {
    "figure_id": "F048",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 13 - Non-Commenced Hyperscaler Leases - Increased by 7.4 GW in 1Q26 Suggesting over 34 GW of Data Center Capacity Under Development Lease Assumptions"
  },
  {
    "figure_id": "F049",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14 - MSFT In-Place vs Non-Commenced Leases"
  },
  {
    "figure_id": "F050",
    "report_id": "R011",
    "label": "Exhibit 16",
    "context": "Exhibit 16 - META In-Place vs Non-Commenced Leases"
  },
  {
    "figure_id": "F051",
    "report_id": "R011",
    "label": "Exhibit 15",
    "context": "Exhibit 15 - GOOGL In-Place vs Non-Commenced Leases"
  },
  {
    "figure_id": "F052",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "Exhibit 17 - ORCL's Non-Commenced Leases"
  },
  {
    "figure_id": "F053",
    "report_id": "R011",
    "label": "Exhibit 18",
    "context": "Exhibit 18 - Total EPC Labor across Major EPC Provider (K) EPCs Referenced: PWR, MTZ, PRIM, MYRG, ECG, CTRI, DY, MWH, AGX, IESC, STRL, EME, FIX, LGN"
  },
  {
    "figure_id": "F054",
    "report_id": "R011",
    "label": "Exhibit 19",
    "context": "Exhibit 19 - EPC/ Construction Labor: Implied GW Ceiling"
  },
  {
    "figure_id": "F055",
    "report_id": "R011",
    "label": "Exhibit 20",
    "context": "Exhibit 20 - Cooling Systems: DC-Relevant Revenue (\\$M)"
  },
  {
    "figure_id": "F056",
    "report_id": "R011",
    "label": "Exhibit 21",
    "context": "Exhibit 21 - Cooling Systems Implied GW Ceiling"
  },
  {
    "figure_id": "F057",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 22 - Power Availability: US New Power Capacity Additions (GW)"
  },
  {
    "figure_id": "F058",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 23 - Power Availability: Implied GW Capacity Ceiling"
  },
  {
    "figure_id": "F059",
    "report_id": "R011",
    "label": "Exhibit 24",
    "context": "Exhibit 24 - Explicit GW Signed / Market Cap Updated June 2026"
  },
  {
    "figure_id": "F060",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 25 - Electrical Equipment: DC-Relevant Revenue (\\$M)"
  },
  {
    "figure_id": "F061",
    "report_id": "R011",
    "label": "Exhibit 26",
    "context": "Exhibit 26 - Electrical Equipment: Implied GW Capacity Ceiling"
  },
  {
    "figure_id": "F062",
    "report_id": "R011",
    "label": "Exhibit 27",
    "context": "Exhibit 27 - Power Transformers: DC-Relevant Revenue (\\$M)"
  },
  {
    "figure_id": "F063",
    "report_id": "R011",
    "label": "Exhibit 28",
    "context": "Exhibit 28 - Power Transformers: Implied GW Capacity Ceiling"
  },
  {
    "figure_id": "F064",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 29 - Backup Generators: DC-Relevant Revenue (\\$M) and YoY Growth"
  },
  {
    "figure_id": "F065",
    "report_id": "R011",
    "label": "Exhibit 30",
    "context": "Exhibit 30 - Backup Generators: Implied GW Capacity Ceiling"
  },
  {
    "figure_id": "F066",
    "report_id": "R011",
    "label": "Exhibit 32",
    "context": "Exhibit 32 - Heatmap Survey: \"Would you support or oppose a data center being build near where you live?\" Data center opposition continues to grow significantly, month and month. The opposition is also intensifying."
  },
  {
    "figure_id": "F067",
    "report_id": "R011",
    "label": "Exhibit 33",
    "context": "Exhibit 33 - Heatmap Survey: \"Would you support or oppose a data center being built near where you live?\""
  },
  {
    "figure_id": "F068",
    "report_id": "R011",
    "label": "Exhibit 34",
    "context": "Exhibit 34 - We Expect Rest of World AI Accelerator GW's to Accelerate Faster Than North America"
  },
  {
    "figure_id": "F069",
    "report_id": "R011",
    "label": "Exhibit 35",
    "context": "Exhibit 35 - The Iberian Digital Diagonal: Connecting Power, Fiber and Submarine cables Marea Grace Hooper Anjana Bilbao"
  },
  {
    "figure_id": "F070",
    "report_id": "R011",
    "label": "Exhibit 36",
    "context": "Exhibit 36 - London public cloud take-up (MW)"
  },
  {
    "figure_id": "F071",
    "report_id": "R011",
    "label": "Exhibit 38",
    "context": "Exhibit 38 - BBOX DC - JV structure DEAL SPECIFIC JV STRUCTURE ALIGNMENT OF INTEREST IN A SIMPLE JV STRUCTURE ```mermaid graph TD"
  },
  {
    "figure_id": "F072",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 1: Weekly EM equity fund flows: ETF vs non-ETF"
  },
  {
    "figure_id": "F073",
    "report_id": "R014",
    "label": "Figure 2",
    "context": "Figure 2: Annual cumulative EM equity fund flows (US\\$ bn)"
  },
  {
    "figure_id": "F074",
    "report_id": "R014",
    "label": "Figure 3",
    "context": "Figure 3: EM equity fund flows vs performance"
  },
  {
    "figure_id": "F075",
    "report_id": "R014",
    "label": "Figure 5",
    "context": "Figure 5: Annual EM equity fund flows: Offshore vs onshore"
  },
  {
    "figure_id": "F076",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Figure 7: Weekly flows into EM equity funds: Global vs regional funds"
  },
  {
    "figure_id": "F077",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: Weekly flows into EM equity funds: By domicile"
  },
  {
    "figure_id": "F078",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: Annual EM equity fund flows: ETF vs non-ETF"
  },
  {
    "figure_id": "F079",
    "report_id": "R014",
    "label": "Figure 8",
    "context": "Figure 8: Weekly flows into EM equity funds: Breakdown of regional funds"
  },
  {
    "figure_id": "F080",
    "report_id": "R014",
    "label": "Figure 9",
    "context": "Figure 9: EM equity funds AUM vs. MSCI EM performance"
  },
  {
    "figure_id": "F081",
    "report_id": "R014",
    "label": "Figure 10",
    "context": "Figure 10: EM equity funds' (%) share in global equity AUM"
  },
  {
    "figure_id": "F082",
    "report_id": "R014",
    "label": "Figure 11",
    "context": "Figure 11: EM equity funds – offshore vs onshore"
  },
  {
    "figure_id": "F083",
    "report_id": "R014",
    "label": "Figure 12",
    "context": "Figure 12: EM equity funds AUM breakdown (US\\$bn)"
  },
  {
    "figure_id": "F084",
    "report_id": "R014",
    "label": "Figure 13",
    "context": "Figure 13: Global vs regional EM equity funds AUM"
  },
  {
    "figure_id": "F085",
    "report_id": "R014",
    "label": "Figure 14",
    "context": "Figure 14: Regional EM equity funds AUM"
  },
  {
    "figure_id": "F086",
    "report_id": "R014",
    "label": "Figure 15",
    "context": "Figure 15: EM ex-China equity fund flows vs performance"
  },
  {
    "figure_id": "F087",
    "report_id": "R014",
    "label": "Figure 17",
    "context": "Figure 17: Weekly EM ex-China equity fund flows – ETF vs non-ETFs"
  },
  {
    "figure_id": "F088",
    "report_id": "R014",
    "label": "Figure 19",
    "context": "Figure 19: EM ex-China vs EM funds AUM"
  },
  {
    "figure_id": "F089",
    "report_id": "R014",
    "label": "Figure 16",
    "context": "Figure 16: EM ex-China equity ETF flows vs MSCI EM ex-China"
  },
  {
    "figure_id": "F090",
    "report_id": "R014",
    "label": "Figure 18",
    "context": "Figure 18: EM ex-China equity funds AUM breakdown"
  },
  {
    "figure_id": "F091",
    "report_id": "R014",
    "label": "Figure 20",
    "context": "Figure 20: EM ex-China funds share (%) in EM AUM"
  },
  {
    "figure_id": "F092",
    "report_id": "R014",
    "label": "Figure 21",
    "context": "Figure 21: Total EM equity funds' weekly net flows"
  },
  {
    "figure_id": "F093",
    "report_id": "R014",
    "label": "Figure 22",
    "context": "Figure 22: Total EM equity funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F094",
    "report_id": "R014",
    "label": "Figure 23",
    "context": "Figure 23: GEM funds' weekly net flows"
  },
  {
    "figure_id": "F095",
    "report_id": "R014",
    "label": "Figure 24",
    "context": "Figure 24: GEM funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F096",
    "report_id": "R014",
    "label": "Figure 25",
    "context": "Figure 25: EM ex-China funds' weekly net flows"
  },
  {
    "figure_id": "F097",
    "report_id": "R014",
    "label": "Figure 26",
    "context": "Figure 26: EM ex-China funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F098",
    "report_id": "R014",
    "label": "Figure 27",
    "context": "Figure 27: Asia ex-Japan funds' weekly net flows"
  },
  {
    "figure_id": "F099",
    "report_id": "R014",
    "label": "Figure 28",
    "context": "Figure 28: Asia ex-Japan funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F100",
    "report_id": "R014",
    "label": "Figure 29",
    "context": "Figure 29: EMEA funds' weekly net flows"
  },
  {
    "figure_id": "F101",
    "report_id": "R014",
    "label": "Figure 30",
    "context": "Figure 30: EMEA funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F102",
    "report_id": "R014",
    "label": "Figure 31",
    "context": "Figure 31: Latin America funds' weekly net flows"
  },
  {
    "figure_id": "F103",
    "report_id": "R014",
    "label": "Figure 32",
    "context": "Figure 32: Latin America funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F104",
    "report_id": "R014",
    "label": "Figure 33",
    "context": "Figure 33: Developed Europe funds' weekly net flows"
  },
  {
    "figure_id": "F105",
    "report_id": "R014",
    "label": "Figure 34",
    "context": "Figure 34: Developed Europe funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F106",
    "report_id": "R014",
    "label": "Figure 35",
    "context": "Figure 35: US weekly funds' net flows"
  },
  {
    "figure_id": "F107",
    "report_id": "R014",
    "label": "Figure 36",
    "context": "Figure 36: US monthly funds' cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F108",
    "report_id": "R014",
    "label": "Figure 37",
    "context": "Figure 37: International funds' weekly net flows"
  },
  {
    "figure_id": "F109",
    "report_id": "R014",
    "label": "Figure 38",
    "context": "Figure 38: International funds' monthly cumulative flows (US\\$bn)"
  },
  {
    "figure_id": "F110",
    "report_id": "R014",
    "label": "Figure 39",
    "context": "Figure 39: Weekly net foreign investment into the Japanese stock market (US\\$mn)"
  },
  {
    "figure_id": "F111",
    "report_id": "R014",
    "label": "Figure 40",
    "context": "Figure 40: Monthly cumulative net foreign investment into the Japanese stock market (US\\$bn)"
  },
  {
    "figure_id": "F112",
    "report_id": "R014",
    "label": "Figure 41",
    "context": "Figure 41: Weekly net foreign investment into the Korean stock market (US\\$mn)"
  },
  {
    "figure_id": "F113",
    "report_id": "R014",
    "label": "Figure 42",
    "context": "Figure 42: Monthly cumulative net foreign investment into the Korean stock market (US\\$bn)"
  },
  {
    "figure_id": "F114",
    "report_id": "R014",
    "label": "Figure 43",
    "context": "Figure 43: Weekly net foreign investment into the Taiwan stock market (US\\$mn)"
  },
  {
    "figure_id": "F115",
    "report_id": "R014",
    "label": "Figure 44",
    "context": "Figure 44: Monthly cumulative net foreign investment into the Taiwan stock market (US\\$bn)"
  },
  {
    "figure_id": "F116",
    "report_id": "R014",
    "label": "Figure 45",
    "context": "Figure 45: Weekly net foreign investment into the Indian stock market (US\\$mn)"
  },
  {
    "figure_id": "F117",
    "report_id": "R014",
    "label": "Figure 46",
    "context": "Figure 46: Monthly cumulative net foreign investment into the Indian stock market (US\\$bn)"
  },
  {
    "figure_id": "F118",
    "report_id": "R014",
    "label": "Figure 47",
    "context": "Figure 47: Weekly net foreign investment into the Brazil stock market (US\\$mn)"
  },
  {
    "figure_id": "F119",
    "report_id": "R014",
    "label": "Figure 48",
    "context": "Figure 48: Monthly cumulative net foreign investment into the Brazil stock market (US\\$bn)"
  },
  {
    "figure_id": "F120",
    "report_id": "R014",
    "label": "Figure 49",
    "context": "Figure 49: Weekly net foreign investment into the Saudi stock market (US\\$mn)"
  },
  {
    "figure_id": "F121",
    "report_id": "R014",
    "label": "Figure 50",
    "context": "Figure 50: Monthly cumulative net foreign investment into the Saudi stock market (US\\$bn)"
  },
  {
    "figure_id": "F122",
    "report_id": "R014",
    "label": "Figure 51",
    "context": "Figure 51: Weekly net foreign investment into the Thailand stock market (US\\$mn)"
  },
  {
    "figure_id": "F123",
    "report_id": "R014",
    "label": "Figure 52",
    "context": "Figure 52: Monthly cumulative net foreign investment into the Thailand stock market (US\\$bn)"
  },
  {
    "figure_id": "F124",
    "report_id": "R014",
    "label": "Figure 53",
    "context": "Figure 53: Weekly net foreign investment into the Indonesia stock market (US\\$mn)"
  },
  {
    "figure_id": "F125",
    "report_id": "R014",
    "label": "Figure 54",
    "context": "Figure 54: Monthly cumulative net foreign investment into the Indonesia stock market (US\\$bn)"
  },
  {
    "figure_id": "F126",
    "report_id": "R014",
    "label": "Figure 55",
    "context": "Figure 55: Weekly net foreign investment into the Malaysia stock market (US\\$mn)"
  },
  {
    "figure_id": "F127",
    "report_id": "R014",
    "label": "Figure 56",
    "context": "Figure 56: Monthly cumulative net foreign investment into the Malaysia stock market (US\\$bn)"
  },
  {
    "figure_id": "F128",
    "report_id": "R014",
    "label": "Figure 57",
    "context": "Figure 57: Weekly net foreign investment into the Philippine stock market (US\\$mn)"
  },
  {
    "figure_id": "F129",
    "report_id": "R014",
    "label": "Figure 58",
    "context": "Figure 58: Monthly cumulative net foreign investment into the Philippine stock market (US\\$bn)"
  },
  {
    "figure_id": "F130",
    "report_id": "R014",
    "label": "Figure 59",
    "context": "Figure 59: Weekly net foreign investment into the Türkiye stock market (US\\$mn)"
  },
  {
    "figure_id": "F131",
    "report_id": "R014",
    "label": "Figure 60",
    "context": "Figure 60: Monthly cumulative net foreign investment into the Türkiye stock market (US\\$bn)"
  },
  {
    "figure_id": "F132",
    "report_id": "R014",
    "label": "Figure 61",
    "context": "Figure 61: Weekly net foreign investment into the Qatar stock market (US\\$mn)"
  },
  {
    "figure_id": "F133",
    "report_id": "R014",
    "label": "Figure 62",
    "context": "Figure 62: Monthly cumulative net foreign investment into the Qatar stock market (US\\$bn)"
  },
  {
    "figure_id": "F134",
    "report_id": "R014",
    "label": "Figure 63",
    "context": "Figure 63: Weekly net foreign investment into the Dubai stock market (US\\$mn)"
  },
  {
    "figure_id": "F135",
    "report_id": "R014",
    "label": "Figure 64",
    "context": "Figure 64: Monthly cumulative net foreign investment into the Dubai stock market (US\\$bn)"
  },
  {
    "figure_id": "F136",
    "report_id": "R014",
    "label": "Figure 65",
    "context": "Figure 65: Weekly net foreign investment into the Vietnam stock market (US\\$mn)"
  },
  {
    "figure_id": "F137",
    "report_id": "R014",
    "label": "Figure 66",
    "context": "Figure 66: Monthly cumulative net foreign investment into the Vietnam stock market (US\\$bn)"
  },
  {
    "figure_id": "F138",
    "report_id": "R014",
    "label": "Figure 67",
    "context": "Figure 67: Weekly net foreign investment into the Pakistan stock market (US\\$mn)"
  },
  {
    "figure_id": "F139",
    "report_id": "R014",
    "label": "Figure 68",
    "context": "Figure 68: Monthly cumulative net foreign investment into the Pakistan stock market (US\\$bn)"
  },
  {
    "figure_id": "F140",
    "report_id": "R014",
    "label": "Figure 69",
    "context": "Figure 69: Weekly net foreign investment into the Sri Lanka stock market (US\\$mn)"
  },
  {
    "figure_id": "F141",
    "report_id": "R014",
    "label": "Figure 70",
    "context": "Figure 70: Monthly cumulative net foreign investment into the Sri Lanka stock market (US\\$bn)"
  },
  {
    "figure_id": "F142",
    "report_id": "R014",
    "label": "Figure 71",
    "context": "Figure 71: Monthly net foreign investment into Chinese equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F143",
    "report_id": "R014",
    "label": "Figure 72",
    "context": "Figure 72: Monthly cumulative net foreign investment into Chinese equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F144",
    "report_id": "R014",
    "label": "Figure 73",
    "context": "Figure 73: Monthly net foreign investment into Mexican equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F145",
    "report_id": "R014",
    "label": "Figure 74",
    "context": "Figure 74: Monthly cumulative net foreign investment into Mexican equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F146",
    "report_id": "R014",
    "label": "Figure 75",
    "context": "Figure 75: Monthly net foreign investment into Chile equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F147",
    "report_id": "R014",
    "label": "Figure 76",
    "context": "Figure 76: Monthly cumulative net foreign investment into Chile equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F148",
    "report_id": "R014",
    "label": "Figure 77",
    "context": "Figure 77: Monthly net foreign investment into Poland equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F149",
    "report_id": "R014",
    "label": "Figure 78",
    "context": "Figure 78: Monthly cumulative net foreign investment into Poland equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F150",
    "report_id": "R014",
    "label": "Figure 79",
    "context": "Figure 79: Monthly net foreign investment into Peru equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F151",
    "report_id": "R014",
    "label": "Figure 80",
    "context": "Figure 80: Monthly cumulative net foreign investment into Peru equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F152",
    "report_id": "R014",
    "label": "Figure 81",
    "context": "Figure 81: Monthly net foreign investment into Colombia equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F153",
    "report_id": "R014",
    "label": "Figure 82",
    "context": "Figure 82: Monthly cumulative net foreign investment into Colombia equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F154",
    "report_id": "R014",
    "label": "Figure 83",
    "context": "Figure 83: Monthly net foreign investment into Australian equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F155",
    "report_id": "R014",
    "label": "Figure 84",
    "context": "Figure 84: Monthly cumulative net foreign investment into Australian equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F156",
    "report_id": "R014",
    "label": "Figure 85",
    "context": "Figure 85: Monthly net foreign investment into Singapore equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F157",
    "report_id": "R014",
    "label": "Figure 86",
    "context": "Figure 86: Monthly cumulative net foreign investment into Singapore equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F158",
    "report_id": "R014",
    "label": "Figure 87",
    "context": "Figure 87: Monthly net foreign investment into Hong Kong equities by funds monitored by EPFR Global (US\\$mn)"
  },
  {
    "figure_id": "F159",
    "report_id": "R014",
    "label": "Figure 88",
    "context": "Figure 88: Monthly cumulative net foreign investment into Hong Kong equities by funds monitored by EPFR Global (US\\$bn)"
  },
  {
    "figure_id": "F160",
    "report_id": "R015",
    "label": "FIGURE 2",
    "context": "As of 3 June 2026. # S&P 500 capex outlook vs. history S&P 500 capex is on track to absorb roughly 50% of operating cash flows in 2026, a level that places this cycle squarely alongside prior capex supercycles like the mid-to-late 1990s telecom/internet buildo"
  },
  {
    "figure_id": "F161",
    "report_id": "R015",
    "label": "FIGURE 3",
    "context": "S&P 500 FIGURE 3. Aggregate capex is projected to increase 40% Y/Y, the fastest pace in at least 35 years"
  },
  {
    "figure_id": "F162",
    "report_id": "R015",
    "label": "FIGURE 4",
    "context": "What distinguishes the current cycle is not simply its scale, but its concentration. Aggregate S&P 500 capex is expected to grow roughly 40% Y/Y, the fastest pace in at least 35 years, yet the bulk of that growth is coming from Communication Services, Tech and"
  },
  {
    "figure_id": "F163",
    "report_id": "R015",
    "label": "FIGURE 5",
    "context": "FIGURE 5. TMT capex as a share of total S&P 500 capex is projected to approach $50\\%$ this year, an ATH TMT capex/ Total S&P 500 capex"
  },
  {
    "figure_id": "F164",
    "report_id": "R015",
    "label": "FIGURE 6",
    "context": "# EV/EBITDA as a check against P/E during elevated capex When capex intensity rises, valuation signals can migrate up the income statement as P/E becomes vulnerable to nonlinear distortions from leverage, tax shields, and depreciation policies. EV/EBITDA has i"
  },
  {
    "figure_id": "F165",
    "report_id": "R015",
    "label": "FIGURE 7",
    "context": "\"High capex\" defined as t12m Capex/EBITDA above the 50th percentile of monthly observations (n) since 1995. FIGURE 7. EV/EBITDA sorting delivers larger cheap-expensive 3Y return spread than P/E during high capex periods"
  },
  {
    "figure_id": "F166",
    "report_id": "R015",
    "label": "FIGURE 8",
    "context": "\"High capex\" defined as t12m Capex/EBITDA above the 50th percentile of monthly observations since 1995. Error bars = 95% CI. This framing matters for today because S&P 500 EV/EBITDA is currently more elevated than P/E, when compared to its own long-run history"
  },
  {
    "figure_id": "F167",
    "report_id": "R015",
    "label": "FIGURE 9",
    "context": "Data as of 31 May 2026. FIGURE 9. Hyperscalers are redeploying balance sheets as capex commitments rise"
  },
  {
    "figure_id": "F168",
    "report_id": "R015",
    "label": "FIGURE 10",
    "context": "This is not to say that we are taking a negative view on US equities over the next 12 months. We found the EV/EBITDA signal to be inherently medium-term in nature with limited timing power over shorter horizons, including one year or less, where the relationsh"
  }
]