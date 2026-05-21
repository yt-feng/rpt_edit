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
    "title": "市场真正在交易的不是AI，而是通胀预期重新定价",
    "digest": "[wechat_article.md]\n# 市场真正在交易的不是AI，而是通胀预期重新定价\n\n过去一周，全球股市下跌0.6%。表面看是AI主题的获利回吐，但更值得关注的信号是：通胀预期正在取代盈利增长，成为资产定价的主导变量。某外资投行最新高频监控报告显示，能源板块单周上涨4.2%，而公用事业、房地产、材料等利率敏感型板块跌幅均超过2.9%。这不是一个简单的板块轮动，而是市场在重新学习一个被遗忘的法则——当通胀预期抬头时，估值逻辑会从远期现金流折现切换到当期盈利保护。\n\n这份报告的核心判断是：全球盈利周期仍在改善，新闻情绪面也在好转，但一个被低估的风险正在累积——通胀上行可能迫使央行重新加息。市场当前定价中隐含的“软着陆”叙事，可能低估了这一尾部风险。\n\n以下是我们从这份报告中提炼出的五个关键洞察，以及它们对资产配置的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 通胀恐慌正在取代AI叙事，成为短期市场的核心矛盾\n\n报告明确指出，全球股市上周下跌的直接原因是“通胀担忧”。这不是一个孤立事件。从板块表现看，能源（+4.2%）和科技硬件（+2.0%）是仅有的两个正收益板块，而公用事业（-3.0%）、材料（-3.0%）、房地产（-2.9%）全线下跌。这种分化逻辑清晰：能源受益于通胀预期上升，科技硬件受益于AI资本开支周期，而利率敏感型资产则在重新定价加息风险。\n\n更值得注意的是区域表现。美国市场（+0.2%）是唯一正收益的发达市场，而新兴市场（-2.5%）和亚太除日本（-2.1%）跌幅最大。这暗示通胀恐慌对新兴市场的冲击更大——这些市场的外资流入对全球利率预期高度敏感。如果通胀数据进一步超预期，新兴市场可能面临更大的资金外流压力。\n\n报告还提到，全球盈利周期仍然强劲，新闻情绪面也在改善。但“一个日益增长的风险是，通胀上行可能迫使央行加息”。这句话值得反\n\n[... middle omitted ...]\n\n似的高质量研报解读，帮助读者在信息过载中抓住真正重要的信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球市场被通胀吓到了？上周走势拆解\n\n通胀担忧升温，全球市场小幅回调\n\n上周全球股市整体下跌-0.6%，美股勉强收红（+0.2%），新兴市场最惨（-2.5%）。核心矛盾：企业盈利和AI主题的乐观情绪，被通胀担忧盖过去了。\n\n1️⃣ 板块分化明显\n- 能源板块一枝独秀（+4.2%），石油相关继续走强\n- 科技硬件（+2.0%）紧随其后，AI产业链仍有支撑\n- 公用事业（-3.0%）、原材料（-3.0%）、地产（-2.9%）跌幅最大，利率敏感板块承压\n\n2️⃣ 主题投资方面\n- 太空概念（+4.3%）、可再生能源（+1.5%）表现最好\n- 核能（-7.2%）、黄金（-6.8%）大幅回调，前期涨幅过大的主题在调整\n- 三重动量（盈利+价格+新闻综合评分）最强的是黄金、稀土和机器人，最弱的是SaaS和奢侈品\n\n3️⃣ 行业动量排名\n从三重动量看，半导体、能源、科技硬件仍是资金最青睐的方向。全球大市值流动性好的标的中，排名靠前的主要是半导体和能源相关公司。\n\n4️⃣ 一个值得关注的信号\n研报提到：全球盈利周期依然强劲，新闻情绪也在改善，但通胀上升可能迫使央行继续加息——这是目前最大的风险点。\n\n简单来说，市场现在处于“\n\n[... middle omitted ...]\n\nisk is that rising inflation prompts central banks to raise rates.\n\n# Best performing themes: Space, Renewable Energy\n\nLast week, among the 12 themes we monitor, the best performers were Space\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R002",
    "title": "市场对美联储缩表的担忧，可能高估了实际影响",
    "digest": "[wechat_article.md]\n# 市场对美联储缩表的担忧，可能高估了实际影响\n\nKevin Warsh正式就任美联储主席后，市场最关心的问题之一，就是这位长期批评美联储资产负债表的前理事，会带来多大变数。\n\n答案是：不会很大。\n\n某外资投行最新研报给出了一个直白的判断：Warsh对美联储资产负债表的影响，将是“雷声大，雨点小”。这个结论看似反直觉，但背后的逻辑链条非常清晰——美联储资产负债表的规模，在完成量化紧缩（QT）后，本质上是由负债端决定的，而负债端三大项中，真正可操作的只有准备金。Warsh能做的，更多是技术性调整，而非结构性变革。\n\n这不是一份简单的“新官上任三把火”分析，它触及了一个更深层的问题：当市场把注意力集中在缩表规模时，真正需要关注的其实是两个结构性变量——资产负债表的“结构”和“制度设计”。而后者，可能才是未来几年影响流动性格局的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 缩表规模的空间，比市场想象的要小得多\n\n理解美联储资产负债表的关键，在于认清一个事实：缩表到一定程度后，规模就不再由资产端决定，而是由负债端决定。\n\n美联储的负债端有三座大山：流通中货币、财政部一般账户（TGA）、以及银行准备金。其中，货币是“外生性负债”，美联储几乎无法主动减少——除非像欧洲央行那样取消大面额纸币，但这在美国政治上完全不可行。TGA方面，财政部已经明确表态，不仅不会缩减，预计到2026年二季度末还会升至9000亿美元。\n\n唯一有操作空间的是准备金。但即便是这块，Warsh也面临两难选择。\n\n如果采取“对银行不友好”的方式——比如设置准备金上限或分层付息——会直接降低银行的流动性缓冲，导致银行减少做市和贷款，进而拖累经济。这与特朗普政府希望维持宽松金融条件的诉求背道而驰。Warsh几乎不可能走这条路。\n\n更可能的是“对银行友好\n\n[... middle omitted ...]\n\n续交流。我们将基于完整研报，逐层拆解这些关键变量的二阶效应。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新主席上任，缩表雷声大雨点小？\n\n缩表动作有限，市场影响不大\n\n---\n\n刚看完一份某外资投行对美联储新主席Warsh的深度研报，核心观点很直接：市场可能高估了他缩表的影响。\n\n先说结论：Warsh虽然一直批评美联储资产负债表太大，但他真正能改变的空间其实很小。\n\n**关于缩表规模，有三个关键点：**\n\n1️⃣ 美联储的负债端有三个大头：流通货币、财政部现金账户（TGA）、银行准备金。货币和TGA基本动不了，唯一能打主意的就是准备金。\n\n2️⃣ Warsh最可能走“亲银行”路线：通过放松监管，让银行提前把抵押品质押给贴现窗口，这样银行需要的准备金就少了。预计能减少2000-5000亿美元，但过程会很慢。\n\n3️⃣ 有个“蓝天方案”值得关注：让银行的SRP（常备回购工具）利率等于IOR（准备金利率）。如果银行能以市场利率随时用国债换现金，就不需要持有那么多准备金了。这个方案如果落地，影响可能比传统缩表更大。\n\n**关于资产端结构，也有两个看点：**\n\n1️⃣ MBS到期后继续滚入短期国债，这个已经在做了，市场已经消化。\n\n2️⃣ 缩短国债持仓久期：Warsh可能会把到期国债再投资全部集中在2-3年期。但关\n\n[... middle omitted ...]\n\nry>\n\n| Year | Currency | Reserves | TGA | Foreign RRP | ON RRP | Other |\n|---|---|---|---|---|---|---|\n| 2008 | 0.7 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 |\n| 2010 | 0.8 | 1.5 | 0.0 | 0.0 | 0.0 | 1.0 |\n\n[... middle omitted ...]\n\ngive rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies."
  },
  {
    "id": "R003",
    "title": "利率市场真正的拐点信号，不是降息时点，而是多头彻底离场",
    "digest": "[wechat_article.md]\n# 利率市场真正的拐点信号，不是降息时点，而是多头彻底离场\n\n过去几周，全球利率市场经历了一轮罕见的仓位清洗。多头在曲线各个期限上几乎全面溃退，残存的虚值多头头寸已经所剩无几。与此同时，空头主导了市场，且大部分处于实值状态。\n\n这份来自某外资投行利率策略团队的报告，核心判断并非关于美联储何时降息，而是指向一个更根本的结构性变化：市场参与者正在用仓位投票，宣告一个长达数年的多头叙事周期的终结。\n\n报告数据显示，CTA（商品交易顾问）在曲线远端已经处于极端做空状态，而资管经理也在系统性降低久期敞口。更值得关注的是，即便收益率走高吸引了部分资金回流，流入的方向却是短期政府债和投资级信用债，而非长久期国债。这意味着市场正在主动压缩久期暴露，而非被动等待利率见顶。\n\n对于资产配置决策者而言，这份报告揭示了一个容易被忽视的关键问题：当前利率市场的定价逻辑，已经从“交易降息预期”切换到了“交易供给和仓位结构”。谁先理解这个切换，谁就能在未来几个季度的波动中占据主动。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 多头的“长期告别”已经完成，残存仓位只会加剧卖压\n\n报告中最具冲击力的数据来自期货持仓代理指标。截至上周，曲线各期限上的虚值多头头寸几乎被全部平仓。在TU、TY和WN合约中，仅剩少量残存的虚值多头，而空头不仅占据绝对主导，且大部分处于实值状态。\n\n这意味着什么？传统的“多头止损-价格下跌-更多多头止损”的负反馈循环已经基本走完。但市场并非就此进入均衡。残存的虚值多头依然构成一个不对称的卖压来源：只要利率继续上行，这些头寸就会被迫平仓，进一步加剧卖压。\n\n从量化角度看，报告构建的“曲线仪表盘”显示，当前利率市场的定价偏向于继续走陡，且久期方向偏空。这个综合指标并非单一来源，而是融合了CTA仓位、期货持仓代理、基\n\n[... middle omitted ...]\n\n，帮助会员在第一时间理解这些变量如何影响利率市场的定价逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美债多头正在“认输”离场\n\n美债市场的“大洗牌”\n\n多头全线撤退，空头主导市场，资金正在寻找新方向。\n\n---\n\n最近某外资投行的一份美债研报，把当前市场的“暗流涌动”讲得很清楚。我帮你拆成3个关键点，看完就明白发生了什么。\n\n**1. 多头“缴械”，空头“上桌”**\n\n过去一周，美债期货市场上，那些“虚值”（out of the money）的多头仓位被大规模平仓，几乎覆盖了所有期限品种。现在，空头仓位占据主导，并且大部分处于“实值”（in the money）状态。这意味着市场情绪已经彻底转向，此前押注利率下行的资金，已经基本认输出局。\n\n**2. 资金在“搬家”：从长端跑到短端**\n\n虽然多头在撤退，但更高的美债收益率本身也在吸引新的资金入场。最近一周，美国固定收益基金净流入约180亿美元，是过去12周平均速度的两倍。\n\n但流入的钱，结构很有意思：\n- **短久期基金**（短期国债、投资级债券）是流入主力。\n- **长久期基金**则持续遭遇赎回。\n\n这说明，投资者并没有因为利率更高就盲目“抄底”长债，反而在主动缩短债券组合的久期，应对可能继续加息的环境。\n\n**3. 日本投资者在卖，但官方干预的“风暴”\n\n[... middle omitted ...]\n\nning washes out and longs exit, higher yields are drawing money back in. Fund inflows have accelerated—led by Agg, short-duration, and IG—while long-duration funds see outflows, signaling shif\n\n[... middle omitted ...]\n\ngive rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies."
  },
  {
    "id": "R004",
    "title": "亚洲正在经历的，不是周期复苏，而是一个新的资本支出超级周期",
    "digest": "[wechat_article.md]\n# 亚洲正在经历的，不是周期复苏，而是一个新的资本支出超级周期\n\n市场当前对亚洲的讨论，大多停留在“能否承受油价冲击”或“中国复苏是否可持续”这类短期问题上。但某外资投行最新发布的年中宏观展望，提供了一个截然不同的判断框架：亚洲正在经历的，不是一个周期性的反弹，而是一个由多重结构性需求共同推动的资本支出超级周期。这个周期的强度，足以让能源冲击变成背景噪音。\n\n这份报告的核心主张并不复杂，但它的推论链条值得每一位关注亚洲资产配置的读者仔细推敲。报告认为，亚洲2026年GDP增速将达4.8%，高于此前的预测。但更关键的不是这个数字本身，而是支撑这个数字的结构——工业周期正在取代消费周期，成为亚洲增长的主导力量。\n\n这不是一个关于“需求回暖”的故事，而是一个关于“供给端结构重置”的故事。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 工业周期正在超越能源冲击，成为亚洲增长的主导变量\n\n报告最值得注意的判断，是亚洲宏观团队明确提出的“工业超级周期”概念。这个判断建立在两个关键观察上。\n\n第一，高频数据已经确认工业周期在加速。亚洲和全球制造业PMI在2026年4月再次回升，亚洲PMI达到53.0，全球PMI达到52.5。这不是一个孤立的信号——从2025年下半年开始，亚洲工业生产的三个月移动平均增速已经持续改善，到2026年4月达到5.9%的同比增长。\n\n第二，政策制定者有效地限制了国际油价上涨向国内燃料价格的传导。报告指出，到目前为止，国际油价上涨向亚洲国内燃料价格的传导比例只有大约四分之一。这意味着能源冲击对企业盈利和消费者支出的实际影响，远低于名义油价涨幅所暗示的程度。\n\n将这两个观察放在一起，结论是清晰的：工业周期的内生动力足够强劲，足以吸收外部冲击。这不是一个“没有坏消息”的乐观，而是一个“好消息足够大，可以覆盖\n\n[... middle omitted ...]\n\n试？非科技出口的加速是否意味着亚洲供应链正在发生根本性重组？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲宏观：工业强周期来了\n\n亚洲经济韧性超预期\n\n亚洲经济正在经历一个有趣的阶段：工业超级周期的力量，正在抵消能源冲击的影响。某外资投行最新研报给出了一些值得关注的数据和判断。\n\n📊 增长预期上调\n2026年亚洲GDP增速预期被上调40bp至4.8%。这个调整的背景是，4月全球和亚洲制造业PMI同步回升，工业周期正在加速。\n\n📈 复苏面在扩大\n不只是科技出口在回暖，非科技出口也跟上来了。4月早期报告国家的非科技出口年化增速达到19%。资本开支（Capex）势头同样强劲，3月亚洲Capex增速高达27%（同比）。\n\n🔧 四大结构性需求驱动\n研报认为，亚洲正走向一个资本开支超级周期，背后有四大驱动力：\n1️⃣ AI及AI相关基建投资\n2️⃣ 能源及能源转型相关支出\n3️⃣ 全球国防开支增加\n4️⃣ 对更广泛工业资本开支的正面溢出效应\n\n预计亚洲固定投资将从2025年的11万亿美元，增长到2030年的16万亿美元。\n\n💰 货币政策判断\n美联储预计在2026年底前按兵不动，2027上半年才降息50bp。亚洲央行则进入一个渐进温和加息周期，日本、澳大利亚和韩国央行有紧缩倾向。\n\n💱 美元先弱后强\n研报预计美元在2026\n\n[... middle omitted ...]\n\nshould be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.\n\n[... middle omitted ...]\n\n, Canary Wharf\n\nLondon E14 4AD\n\nUnited Kingdom\n\n+44 (0)20 7425 8000\n\n# Japan\n\n1-9-7 Otemachi, Chiyoda-ku\n\nTokyo 100-8104\n\nJapan\n\n+81 (0) 3 6836 5000\n\n# Asia/Pacific\n\n1 Austin Road West\n\nKowloon\n\nHong Kong\n\n+852 2848 5200"
  },
  {
    "id": "R005",
    "title": "日本经济真正的拐点，不是GDP数字，而是“缓冲垫”已经耗尽",
    "digest": "[wechat_article.md]\n# 日本经济真正的拐点，不是GDP数字，而是“缓冲垫”已经耗尽\n\n市场正在等待日本央行下一步动作，而刚刚公布的Q1 GDP数据，似乎给出了一个清晰的信号：经济依然坚实。2.1%的季调后年化环比增速，不仅超过了市场预期的1.7%，也是连续第七个季度实现正增长。乍看之下，这是一个标准的“好数据”。\n\n但这份某外资投行的研报揭示了一个更深层的判断：真正重要的不是GDP本身有多强，而是支撑日本经济韧性的几层“缓冲垫”正在逐一消失。2022年，日本经济承受住了能源冲击，靠的是日元贬值对企业的对冲和家庭储蓄的消耗。而这一次，这两个条件都不再成立。\n\n这意味着，如果霍尔木兹海峡的局势导致油价进一步上行，日本经济面临的不是简单的“增速放缓”，而是一种结构性脆弱性的暴露。日本央行加息的窗口，可能比市场预期的更窄、也更紧迫。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 增长的“广度”比“速度”更重要，内外需的平衡正在重建\n\n这份报告最值得关注的细节，不是2.1%这个数字本身，而是增长的结构。Q1的增长几乎由国内需求和净出口对半贡献：国内需求贡献了1.0个百分点，净出口贡献了1.1个百分点。这在日本近几年的增长图谱中并不常见。\n\n过去几个季度，日本经济经常呈现“外需强、内需弱”或“内需补、外需拖”的跷跷板状态。而Q1的数据显示，私人消费环比增长了0.3%，超出预期的0.1%；资本支出也保持了0.5%的环比增长，背后有AI投资热潮的支撑。更重要的是，私人消费平减指数已经从2025年Q1的峰值3.2%回落至2.0%，这意味着家庭部门的实际购买力正在修复——实际员工薪酬自2024年Q4以来保持了1.3%的同比增长。\n\n这不是一个“靠一次性因素拉动的脉冲式增长”，而是一个基本面改善驱动的、有广度的复苏。对于日本央行而言，这提供了加息所需的经\n\n[... middle omitted ...]\n\n价权的微观证据，以及这些变化对全球利率和汇率格局的二阶影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本一季度GDP超预期，消费和出口都在发力\n\n日本经济，稳住了？\n\nQ1 GDP环比年化增长2.1%，高于市场预期的1.7%，连续第七个季度正增长。内外需共同拉动，结构不错。\n\n1️⃣ 消费比想象中强\n私人消费环比+0.3%，比预期的0.1%高出不少。背后原因是通胀放缓，消费者物价涨幅从3.2%回落到2.0%，实际薪资持续增长，购买力在恢复。\n\n2️⃣ 出口明显回暖\n商品出口环比+1.7%，结束了连续两个季度的下滑。汽车相关出口大涨+6.5%，资本品出口也增长+4.5%。服务出口小幅增长，但入境消费反而下降了1.6%。\n\n3️⃣ 资本开支保持韧性\n受AI投资热潮带动，资本开支环比+0.5%，同比+3.5%，增速稳定。政府支出也有小幅扩张。\n\n4️⃣ 但未来风险不小\n研报的核心担忧是：原油价格飙升导致贸易条件恶化，进口价格大涨，可能挤压企业利润、抑制资本开支，同时推高通胀、削弱居民购买力。\n\n和2022年那次不同：当时日元贬值缓冲了冲击，家庭还能靠储蓄撑消费。但现在日元贬值幅度有限，家庭储蓄率已经很低，缓冲空间更小。\n\n整体来看，一季度数据给了日本央行继续加息的底气，但后续能源价格的影响仍需观察。\n\n#学习笔记\n\n[... middle omitted ...]\n\nd 0.5% in FY2024. Nominal growth was supported by firm domestic inflation above 2%, reaching a stronger 4.2% in FY2025, following 4.7% in FY2023 and 3.7% in FY2024, broadly in line with levels\n\n[... middle omitted ...]\n\ntual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/8369aa5be91e72ace9b1e468b85971d3c272586071a2b8de9fc86d12c44c8d71.jpg)"
  },
  {
    "id": "R006",
    "title": "市场真正低估的不是AI需求，而是供给侧的约束正在重塑赢家",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是供给侧的约束正在重塑赢家\n\n过去六个月，围绕AI基础设施的讨论大多集中在需求端：谁的算力卡卖得更多，谁的资本开支计划更激进，谁的云业务增长更快。但一份刚刚发布的亚洲供应链调研报告传递了一个更微妙的信号——需求仍然强劲，但真正驱动本轮周期走向的变量，已经从“谁拿到了订单”转向了“谁能把订单变成交付”。\n\n这份由某外资投行分析师团队发布的报告，基于近期与亚洲IT硬件供应链核心企业的直接交流，覆盖了从TPU专用芯片到通用服务器、从数据中心交换到电源管理的完整链条。我们读下来的核心判断是：市场对AI资本开支的热情定价已经比较充分，但对供给端出现的结构性变化——产能瓶颈、组件短缺、多源采购策略的加速——定价尚不充分。这些变化正在重新分配供应链中的利润池，也将决定下一阶段哪些公司能跑赢行业。\n\n报告没有直接给出“买什么”的清单，但它提供了足够多的线索，让有经验的读者可以自己拼出下一张牌桌的格局。以下是我们从报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 专用芯片供应链的扩容速度仍在加速，但受益者正在从单一供应商向多层级扩散\n\n报告中最值得关注的一个信号来自TPU供应链。六个月前，分析师基于调研判断TPU产能将在2026年初翻倍，并在2026年中可能再上调50%。而本次调研的结论是：这一计划正在按甚至超预期推进。\n\n这意味着什么？TPU的出货量增速可能比市场模型假设的更陡峭。更重要的是，供应链的受益范围正在扩大。报告明确指出，CLS作为TPU及其变体的主要供应商，无论底层芯片供应商是谁，其TPU相关收入将从2025年的约10亿美元翻倍至2026年的28亿美元。但报告同时指出，JBL虽然没有直接参与TPU制造，却为测试硬件的主要供应商提供测试设备，测试产能的稳步增长\n\n[... middle omitted ...]\n\n分享原始研报PDF、数据表格，以及我们对关键假设的逐项拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI硬件供应链，正在经历一场“甜蜜的供不应求”\n\n供不应求，还在加剧\n\n最近跟某外资投行团队去亚洲跑了一圈，跟IT硬件供应链上的公司聊了个遍。整体感觉：需求端非常积极，但供给端压力山大。产能限制、元器件短缺、多源采购，成了每家必聊的话题。\n\n1️⃣ TPU：最确定性的增长主线\n\n六个月的观察周期里，TPU相关供应商的景气度不仅没降，反而超预期。某外资投行之前预测TPU产能会在2026年初翻倍，年中再提50%，现在看至少是符合预期，甚至可能更好。\n\n几个关键玩家：\n- CLS：TPU的主力供应商，无论芯片是谁家做的。2026年TPU相关收入预计从10亿跳到28亿美金，翻倍都不止。\n- FLEX：传统CPU的第二供应商，虽然市场份额有担忧，但依然参与其中，只是增速不如生态内其他玩家。\n- JBL：不直接做TPU，但给测试设备老大供货，测试产能持续扩张对它来说是利好。\n- ODM：TPU主板和整机柜的ODM活动在增多，谷歌以前自己做的部分现在开始外放。\n\n2️⃣ Trainium：增长确定，但量级不同\n\nTrainium今年也会有不错的增长，供应链反馈是30%以上，如果其他云厂商也采用，可能会更高。不过跟TPU的量\n\n[... middle omitted ...]\n\nnths ago, one of our main calls was being positive on TPU-exposed vendors as we heard of a doubling of capacity in early 2026, and a potential raise of $50\\%$ in mid-2026. We believe this is d\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R007",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n这份来自某外资投行权益衍生品团队的最新报告，核心判断并非关于宏观衰退或通胀失控，而是指向一个更微妙也更危险的信号：在泡沫化的市场结构中，FOMO（害怕错过）的力量正在压倒传统的宏观风险因子。报告通过多个独立但相互印证的指标——从利率波动率偏斜与权益波动率偏斜的罕见背离，到全球泡沫风险指标的持续走高——揭示了一个投资者必须正视的现实：当前市场的核心矛盾，不是经济强不强，而是资产价格的自我强化机制是否已经脱离了基本面锚定。\n\n报告发布于2026年5月19日，正值美债长端收益率再度上行、通胀担忧重燃之际。但报告作者明确提醒：在泡沫构建阶段，FOMO可以压倒收益率上行和宏观逆风，正如互联网泡沫时期纳斯达克在30年期国债收益率飙升中继续暴涨。这不是历史类比，而是基于当前数据识别出的结构性特征。对于做资产配置的决策者而言，忽视这一信号的成本，可能远高于对宏观风险的过度谨慎。\n\n以下是我们从这份报告中提炼出的四个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利率市场与权益市场正在发出截然相反的信号，这种背离本身就是一个重要判断\n\n报告指出了一个极其罕见的市场现象：利率波动率市场呈现出陡峭的看跌偏斜，而权益指数和板块的看涨偏斜却处于历史平坦水平。用通俗的话说，利率交易员在为长端收益率的进一步上行（利空风险资产）定价，但权益交易员几乎完全没有为指数下跌定价，反而在廉价地卖出看涨期权。\n\n这种背离意味着什么？它说明两个市场对同一宏观环境的解读完全相反。利率市场在定价“通胀粘性-紧缩预期”，权益市场在定价“AI叙事-资金涌入”。两者不可能同时正确。报告隐含的判断是：在泡沫化的市场环境中，权益市场的定价可能暂时压倒利率市场的警示，但尾部风险\n\n[... middle omitted ...]\n\n群内分享完整报告的关键图表，并定期组织对上述问题的跟踪分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球股市的FOMO，可能比你想的更持久\n\n别低估FOMO的力量\n\n美股近期涨势放缓，通胀担忧和长端利率上升开始施压。但研报指出，市场韧性依然很强，FOMO（害怕错过）可能压倒宏观逆风。\n\n1️⃣ FOMO vs 宏观：谁赢？\n在泡沫型市场里，FOMO可以压倒利率上升和宏观压力。比如互联网泡沫时期，纳斯达克就在30年国债收益率飙升的背景下照样大涨。\n眼下，宏观风险和泡沫倾向的碰撞，让风险同时往两个极端堆积。这时候，期权的不对称性就很有价值了。\n\n2️⃣ 具体怎么用期权？\n- TLT看跌价差：如果利率继续上行，这个策略的历史最大赔付约8倍\n- QQQ看涨价差：低成本、有限风险地去参与上行\n- NDX-USDGBP混合产品：另一种便宜的看涨参与方式\n\n3️⃣ 英国的特殊机会\n英国政治风险（工党领导层不确定性）重新成为宏观驱动因素，导致英镑走弱、英债收益率波动。\n这创造了跨资产交易机会：\n- 英国银行股对国内政治敏感，SX7E/SX7P波动率比值处于历史低位\n- 看好SX5E上涨+EURGBP上涨的双重数字期权，最大赔付13:1\n- NDX看涨期权挂钩英镑走弱，比普通期权便宜60%\n\n4️⃣ 中国AI硬件：7.1倍赔\n\n[... middle omitted ...]\n\nNear term, the clash between macro risks and a bubble-prone market is pushing risk into both tails, making options' asymmetry valuable. TLT put spreads offer historic \\~8x max payouts to hedge\n\n[... middle omitted ...]\n\nered/qualified as a research analyst under the FINRA rules. Refer to \"Other Important Disclosures\" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions."
  },
  {
    "id": "R008",
    "title": "铜冶炼加工费跌穿-100美元，市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 铜冶炼加工费跌穿-100美元，市场真正低估的不是需求，而是供给侧的再定价\n\n过去一周，大宗商品市场最值得关注的信号，不是铜价在每吨13900美元附近徘徊，也不是金价从高点回落3.7%。真正值得产业决策者和投资者反复咀嚼的，是铜精矿的现货加工费——TC/RC——跌破了每吨-100美元。\n\n这不是一个简单的数字。TC/RC是冶炼厂购买铜精矿后，向矿商收取的加工费用。当这个数字跌到负值，意味着冶炼厂不仅拿不到加工费，反而要倒贴钱给矿商才能买到原料。这在历史上几乎从未发生过。\n\n某外资投行最新发布的周度报告，用一组数据揭示了当前基本材料板块的核心矛盾：上游矿端供应持续收紧，中游冶炼环节利润被挤压，下游需求端却并未出现明显坍塌。这种结构性错配，正在重塑整个产业链的定价逻辑。\n\n报告中最具冲击力的图表，是Domestic monthly treatment charges on copper concentrate的走势图。从2018年的每吨75美元，到2024年的每吨100美元，再到2026年5月跌至-103.72美元。这条曲线不仅是供应紧张的直观证据，更是整个铜产业链利润分配发生根本性转移的信号。\n\n黄金价格在同期下跌3.7%，而铜铝价格逆势走强。这本身就在暗示：当前铜价的支撑力量，并非来自宏观避险情绪，而是来自无法绕开的实物供应缺口。\n\n以下，我们从这份报告出发，拆解供给侧再定价的四个层次，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 铜冶炼加工费跌入负值，意味着矿端议价权已彻底转移\n\nTC/RC的本质，是矿商与冶炼厂之间的利润分配。当矿端供应充裕时，冶炼厂拥有议价权，可以要求更高的加工费；当矿端供应紧张时，矿商占据主导，加工费就会下降。\n\n当前TC/RC跌至-103.72美元\n\n[... middle omitted ...]\n\n欢迎来星球微信群里继续讨论，一起拆解这些未解问题的底层逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n有色金属这一周，供应端的故事还在继续 🔥\n\n铜铝价格坚挺，冶炼利润改善，但钢铁还在亏\n\n上周有色金属板块整体偏强，核心驱动还是供应端扰动。中东局势反复影响霍尔木兹海峡航运，抬高了冶炼和物流成本；秘鲁给 Petroperu 批了 20 亿美元贷款，也说明当地能源系统压力不小，市场对矿端供应的担忧没有消退。\n\n**1/ 铜：精矿紧缺到了新高度** 🔶\n\nLME 铜周涨 2.8% 到 13,895 美元/吨，国内现货也跟涨 2.7% 到 105,790 元/吨。但更值得关注的是现货 TC/RC——就是冶炼厂买矿的加工费——已经跌到 -104 美元/吨，创下新低。负值意味着冶炼厂不仅拿不到加工费，还要倒贴钱买矿，精矿供应紧张的程度可见一斑。\n\n**2/ 铝：冶炼利润不错，但持续性待观察** 🔷\n\nLME 铝周涨 5% 到 3,741 美元/吨，国内长江现货微涨 0.6% 到 24,370 元/吨。按 60% 自备电比例算，全国平均吨铝利润已经回升到 8,077 元，环比增加 115 元。这个利润水平在历史上不算低，但关键要看成本端——氧化铝和电力价格会不会跟着涨。\n\n**3/ 钢铁：原料成本高，利润还在亏损区** ⚙\n\n[... middle omitted ...]\n\nnd continued market concerns over potential mining supply disruptions. LME copper rose 2.8% WoW to USD 13,895/t, meanwhile, China spot copper prices also increased by 2.7% WoW to RMB 105,790/t\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R009",
    "title": "中国奶粉市场的真正拐点：消费者不再为“进口”买单，而是为“科学”付费",
    "digest": "[wechat_article.md]\n# 中国奶粉市场的真正拐点：消费者不再为“进口”买单，而是为“科学”付费\n\n这份由某外资投行发布的第六次中国婴幼儿配方奶粉年度调查报告，覆盖了从一线到五线城市的1200名家长，其核心发现指向一个被多数投资者低估的结构性变化：中国消费者对奶粉的选择逻辑正在发生根本性重置。过去十年，行业的核心叙事是“进口 vs 国产”的二元对立；而2026年的数据清晰地表明，这一框架正在瓦解。消费者的决策天平已经从“品牌出身”转向“成分科学”，而这一转变对行业竞争格局、定价权分布以及各公司的长期战略价值，将产生远比出生率波动更深远的影响。\n\n报告揭示了一个关键信号：在经历过2025年的一系列产品召回事件后，消费者的实际行为变化比市场预期的更为剧烈。但真正值得关注的，不是短期的份额此消彼长，而是这些行为背后所反映出的、不可逆的认知升级。本文将从五个层次拆解这份报告的核心洞察，并指出其中未被充分定价的挑战与机遇。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 召回事件暴露了进口品牌的软肋，但最大赢家并非外资同行\n\n调查显示，84%的受访者表示今年因召回事件而发现雀巢（Wyeth系列）或达能（Aptamil、Nutrilon）产品缺货。其中，47%的受访者明确表示雀巢的库存减少，而达能库存未变。这直接对应了雀巢产品在中国被召回、而达能未被波及的事实。\n\n但真正值得关注的是这些消费者的去向。在曾购买达能或雀巢的受访者中，63%转向了国产品牌，仅有35%转向了其他国际品牌。这意味着，召回事件并未在进口品牌内部形成“此消彼长”的闭环，反而加速了消费者向国产阵营的迁徙。\n\n这一数据的含义是双重的。对于像H&H（健合集团）这样定位欧洲原产、主打超高端的产品线而言，它确实成为了一个显著受益者——其法国和丹麦生产的奶粉恰好满足了从召回品牌中流失的、仍对\n\n[... middle omitted ...]\n\n续讨论，我们将结合完整报告内容，持续跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国奶粉市场正悄悄变天\n\n消费者用脚投票\n\n**进口品牌信任危机，国产品牌迎来窗口期**\n\n最近一份覆盖1200位中国家长的奶粉消费调研，揭示了一个正在发生的结构性变化。某外资投行的年度调查显示，消费者对国产奶粉的接受度正悄悄攀升。\n\n---\n\n**1/ 召回事件后的品牌大迁徙**\n\n调研发现，84%的受访者表示今年因召回事件，遇到过达能和雀巢旗下奶粉断货的情况。其中，63%的消费者转投了国产品牌，只有35%选择了其他进口品牌。\n\n这个数字很说明问题——进口品牌过去建立的信任壁垒，正在被打破。消费者不是简单地换一个进口牌子，而是直接转向国产。\n\n**2/ 国产品牌凭什么赢回来？**\n\n核心驱动力是“品质认知改善”。调研显示，消费者对国产奶粉质量的评价逐年提升，特别是“中国制造”的标签反而成了加分项。\n\n但更有意思的是，消费者最看重的既不是国产也不是进口，而是“营养价值/科学益处”。55%的受访者表示对国内外品牌没有偏好，这个比例创下历史新高。\n\n这意味着什么？品牌出身正在退居二线，产品力才是真正的护城河。\n\n**3/ 谁在这轮洗牌中受益？**\n\n根据调研结果，几个方向值得关注：\n\n- **国产龙头品牌**：凭\n\n[... middle omitted ...]\n\nngs\n\n2024: Global Agricultural Products - Infant formula: 2024 proprietary survey findings\n\n2023: Greater China Food Manufacturers - Infant formula: 2023 proprietary survey findings\n\n2022: Gre\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R010",
    "title": "中国房地产的真正拐点，不是销量，是库存结构",
    "digest": "[wechat_article.md]\n# 中国房地产的真正拐点，不是销量，是库存结构\n\n四月的数据，表面上看起来并不一致。国家统计局公布的房地产开发投资同比下降20%，新开工面积下滑27%，土地市场仍在收缩。但与此同时，住宅销售额的同比降幅收窄至6%，为过去11个月最小，重点城市的二手房成交量在5月前两周同比增长了30%。\n\n市场参与者很容易被这些相互矛盾的信号迷惑。有人看到投资继续下滑，认为行业仍在探底；有人看到销量边际改善，便高呼复苏已至。两种看法都有其数据支撑，但都忽略了当前最核心的结构性变化。\n\n某外资投行在最新发布的研报中，没有停留于描述这些数据本身，而是给出了一个更具穿透力的判断：市场正在经历的不是一次简单的周期性反弹，而是一次供给侧的深度重构。真正值得关注的，不是销量何时转正，而是库存的“质”正在发生根本性转变——待售面积中，三年以内的新房库存正在以2.6%的同比速度下降，而竣工未售库存总量也在近十年来首次出现同比负增长。\n\n这意味着什么？意味着过去几年困扰行业的“库存堰塞湖”，正在被时间消化。当库存结构从“大量积压”转向“相对干净”，行业定价权的分配逻辑将被重新书写。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四月数据的表面矛盾，其实指向同一个方向：供应端正在加速出清\n\n四月单月的数据，确实有让人担忧的一面。房地产开发投资同比下滑20%，较3月的-11%明显加速；新开工面积同比下降27%，较3月的-17%进一步恶化。这两个数字，很容易被解读为行业仍在失速。\n\n但如果我们把目光从“投资”转向“库存”，会发现另一幅图景。截至4月末，全国住宅竣工未售库存为4.21亿平方米，同比仅增长1.0%，而3月末这个数字是1.5%。更关键的是，三年以内的新房库存同比下降2.6%。这两个数据放在一起，意味着什么？\n\n意味着过去几年累积的“老库存”正在\n\n[... middle omitted ...]\n\n读。这些图表背后的二阶效应，往往比报告正文本身更具洞察价值。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月地产数据：销售跌幅收窄，但投资还在加速下滑\n\n复苏信号增多，但结构分化明显\n\n最近某外资投行出了一份4月地产数据解读，信息量很大。我拆了几个关键点，和你们聊聊。\n\n**1/ 销售端：跌幅收窄，二手房更活跃**\n\n4月住宅销售额同比-6%，是过去11个月最小跌幅。销售面积-9%（3月-10%），也在收窄。\n\n更值得关注的是：5月前两周，18城二手房成交量同比+30%，比4月的+9%明显提速。新房也维持了正增长。\n\n一线城市房价环比微涨（新房+0.1%，二手房+0.4%），二三四线跌幅也在缩小。\n\n**2/ 供给端：开工和投资还在加速下滑**\n\n4月新开工同比-27%（3月-17%），房地产投资-20%（3月-11%）。说明开发商对后市仍然谨慎，不敢轻易加杠杆。\n\n竣工-19%，与3月持平。库存方面，已竣工未售住宅同比仅+1%，三年内库存甚至-2.6%，说明去化在推进。\n\n**3/ 政策：从“救市”转向“加温”**\n\n4月政治局会议后，深圳、广州等城市陆续出台本地宽松措施。这次不同以往——以前是市场差才出政策，现在是市场已经在恢复，政策来再加一把火。\n\n公积金贷款放松被认为是在购房者预期转好后支撑需求，但不是\n\n[... middle omitted ...]\n\n11%). [7] CREIS 300-cities Mar land sales GFA/ value -29%/-40% (Mar: -24%/-40%); MoF 1Q land sales revenue -24%yoy. Macro: Apr beat in inflation (PPI +2.8%yoy, CPI +1.2%) and exports (+14%), b\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R011",
    "title": "铝市场最被低估的不是需求，而是供给侧的不可逆重置",
    "digest": "[wechat_article.md]\n# 铝市场最被低估的不是需求，而是供给侧的不可逆重置\n\n过去两个月，全球铝市场经历了一场罕见的供给冲击。某外资投行最新发布的研报用了一个罕见的表述：这是现代铝市场历史上最大的供给冲击之一，上一次可以追溯到1970年代的能源危机。但真正值得关注的，不是冲击本身有多大，而是冲击之后市场结构发生了什么变化。\n\n这份报告的核心判断是：即使中东地缘冲突不再进一步升级，全球铝市场也已经进入了一个结构性更紧的库存制度。这不是一个短期价格波动的故事，而是一个供给弹性系统性下降、传统市场自我修复机制失效、库存缓冲带正在被逐层消耗的故事。报告认为，即便在需求疲软的假设下，未来6-12个月铝库存仍将刷新55年历史低点，2026年下半年均价有望达到每吨4000美元。\n\n为什么这个判断值得认真对待？因为铝市场的供需失衡逻辑与过去二十年完全不同。这不是一个需求驱动的牛市，而是一个供给侧的不可逆重置。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供给冲击的规模已经超过了市场定价所反映的程度\n\n中东冲突导致的产量损失并不是一个短期扰动。报告数据显示，超过300万吨的年化产量损失已经嵌入到最新的产量预测中，而恢复路径本身高度不确定——取决于冲突持续时间、基础设施修复时间表、物流正常化以及原材料补库周期。市场不太可能看到区域供给的V型复苏。\n\n更关键的是，整个铝系统的供给弹性已经大幅下降。中国在经历了多年的供给侧改革后，有效产能天花板已经形成。数据显示，中国铝行业闲置产能占总产能的比例已从2010年代的35%-47%下降至目前的约5%，预计到2028年将进一步降至3%以下。这意味着，当价格上升时，中国不再有能力像过去那样快速重启或增加大量供给。\n\n在产能天花板之外，印尼虽然是非中国地区少数能够提供增量供给的地区，但报告明确指出，其扩张节奏和时机仍\n\n[... middle omitted ...]\n\n最终会给出比报告预期更大的下行惊喜？欢迎分享你的观察和判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铝，50年来最紧的供需格局\n\n铝价或冲击4000美元\n\n最近读了份某外资投行的铝行业研报，信息量炸裂，给大家拆解一下核心逻辑。\n\n铝市场正经历近50年来最大的供应冲击之一（上次还是1970年代的能源危机），而这次情况更特殊：\n\n1️⃣ 库存已在55年低位\n- 全球铝库存已处于历史最低水平\n- 中国产能天花板已到，闲置产能几乎为零\n- 中东地缘冲突导致超300万吨产能损失\n\n2️⃣ 替代品成本高企\n- 铜和塑料等替代品价格都处于高位\n- 铝的性价比优势反而更加突出\n\n3️⃣ 需求结构变了\n- 新能源基建、电网升级、电动车产业链成为铝需求新引擎\n- 这部分需求受经济周期影响较小\n- 中国约25%的铝需求来自能源转型领域\n\n4️⃣ 供应弹性消失\n- 中国产能已达上限（约4600万吨）\n- 印尼等新兴产区扩产慢，执行风险大\n- 即使需求增长放缓，市场仍会持续短缺\n\n核心判断：\n- 除非出现类似2008年或沃尔克时期级别的严重衰退，否则铝库存只会继续收紧\n- 2026下半年均价有望达4000美元/吨\n- 乐观情景下2027年均价可达5350美元\n\n最关键的一点是：这次不是需求拉动的牛市，而是供给驱动的结构性紧张。即使需\n\n[... middle omitted ...]\n\ne lows over the next 6-12 months, with the associated buying of physical inventory futures hedges driving up prices to average \\$4,000/t during 2H'26, and in our bull case to average \\$5,350/t\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R012",
    "title": "中国光伏行业真正的底部信号，不是价格，而是企业开始“做不同的事”",
    "digest": "[wechat_article.md]\n# 中国光伏行业真正的底部信号，不是价格，而是企业开始“做不同的事”\n\n如果你在过去两年持续跟踪中国光伏行业，大概率已经对“产能过剩”、“价格战”、“行业出清”这些词产生了听觉疲劳。每一轮周期底部，市场都在等待一个信号：价格企稳、需求反弹、库存消化。但这份来自某外资投行2026年5月全球光伏会议的调研纪要，提供了一个更值得深思的视角——真正预示行业拐点临近的，或许不是某个价格数据，而是头部企业集体从“拼规模”转向“找差异”的战略转向。\n\n这份报告覆盖了隆基绿能、协鑫科技、海南钧达、大全能源和晶科能源五家中国光伏龙头。五家公司管理层的共同叙事是：上半年需求疲弱，多晶硅环节仍在承压，但政策驱动的反内卷措施、更严格的行业标准以及产业整合正在逐步改善行业纪律，定价趋于理性。这听起来像一份标准的周期底部报告。但真正值得关注的，是每一家公司都在讲述一个不同于过去的故事——隆基在讲BC组件和储能系统，协鑫在讲颗粒硅和电池材料，钧达在讲空间太阳能。这不是巧合，这是行业从“规模竞赛”转向“能力竞赛”的早期信号。\n\n以下是我们从这份报告中提炼出的五个关键洞察，它们共同指向一个判断：中国光伏行业正在经历的不是一次简单的周期波动，而是一次结构性的价值重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 需求端最悲观的预期可能已经反映在股价中，但供给端的结构性变化才刚刚开始被定价\n\n报告中最引人注目的数据点之一，是隆基对2026年中国光伏需求的预期：200-250GW，相较于2025年的317GW出现明显下降。这背后的原因是电网约束和“十五五”规划目标尚未落地的阶段性真空。如果这一预测成立，2026年将成为中国光伏市场多年来首次出现年度需求负增长的年份。\n\n但有趣的是，市场对此的反应并非恐慌。这或许说明，需求端的悲观预期已经被相当程度地消\n\n[... middle omitted ...]\n\n的同行，他们的视角和判断，可能会帮助你形成更完整的投资框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 光伏行业：分化求生，谁能熬过寒冬？\n\n📌 **行业复苏前夜**\n\n---\n\n最近某外资投行举办了一场全球太阳能会议，5家中国龙头公司参加。听完一圈下来，整体感觉是：行业还在底部磨，但分化已经很明显了。\n\n**先说大环境**：上半年需求疲软（尤其国内），多晶硅还在过剩、库存高企，价格承压。但好消息是，政策驱动的“反内卷”措施、更严格的行业标准、以及产能出清，正在慢慢改善行业纪律，组件价格开始趋于理性。\n\n**各家都在找自己的路**：\n\n1️⃣ **隆基绿能**：押注BC高效组件，同时杀入储能系统（ESS）赛道。今年目标组件出货80GW，BC产品占比超55%，组件业务预计下半年扭亏。储能目标出货6GWh。但要注意，美国业务因合规要求已降低子公司持股至20%以下，态度谨慎。\n\n2️⃣ **协鑫科技**：颗粒硅成本优势明显，现金成本仅24元/kg，比棒状硅低10元/kg。除了主业，还在拓展正极材料和硅碳负极两大新方向。公司认为行业回暖取决于政策落地和进一步整合。\n\n3️⃣ **海南钧达**：海外市场是亮点，出口占比从去年的50%提升到今年一季度的70%，主要卖往印度、土耳其。海外组件比国内贵2分/W。还有一个小众\n\n[... middle omitted ...]\n\nth demand softness in 1H26 (particularly in China) and ongoing oversupply and high inventories in polysilicon segment weighing on pricing. At the same time, there is a shared view that policy-\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R013",
    "title": "全球电动车市场正在经历一场“结构性分化”，而非简单的复苏",
    "digest": "[wechat_article.md]\n# 全球电动车市场正在经历一场“结构性分化”，而非简单的复苏\n\n如果你在2026年3月看到全球前15大电动车市场的整体销量同比增长8%，渗透率升至24.3%，你可能会认为行业正在稳步回暖。但这份来自某外资投行的月度追踪报告揭示了一个更微妙的图景：增长是真实的，但增长的质量和方向正在发生根本性转变。市场真正低估的，不是电动车的渗透曲线是否还能上行，而是这场增长背后的结构性分化——国家之间、技术路线之间、车型级别之间、甚至企业之间的分化——正在重塑整个行业的竞争规则。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球市场的“假性回暖”背后，是三个截然不同的增长故事\n\n2026年3月，G15国家电动车总销量达到176.9万辆，环比大幅增长62.8%，同比也录得8%的正增长。单看这个数字，很容易得出“行业走出低谷”的结论。但渗透率数据给出了第一个警示信号：G15平均渗透率从2025年3月的22.7%升至24.3%，仅提升1.6个百分点。这意味着整体销量的增长，更多来自汽车大盘的扩张和季节性的补库效应，而非消费者对电动车的接纳度出现了跳跃式提升。\n\n更关键的是，拆开国家层面的数据，你看到的是三个截然不同的增长故事。\n\n第一个故事发生在中国。作为全球最大的电动车市场，中国3月销量116.1万辆，同比仅增长1.6%，渗透率维持在40.1%的高位。这意味着中国市场正在从“渗透率快速爬升”进入“渗透率高位震荡”阶段。1.6%的同比增速，与过去几年动辄30%-50%的增长率形成鲜明对比。这不是衰退，而是市场成熟化的标志——当渗透率超过40%，增量市场的获取难度和成本都在急剧上升。\n\n第二个故事在欧洲。德国、法国、意大利、英国等主要市场在3月集体发力：德国同比增长42.8%，法国增长51.9%，意大利增长84.8%，英国增长30.7\n\n[... middle omitted ...]\n\n演。欢迎来星球微信群里继续讨论，一起追踪这个行业的真实变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026年3月全球新能源车销量出炉，看点不少\n\n全球新能源车，3月回暖了\n\nG15国家3月卖了176.9万辆，同比增8%\n\n---\n\n**1. 整体大盘：季节性回暖，但Q1增速放缓**\n\n3月全球G15（前15大市场）新能源车卖了176.9万辆，同比+8%，环比+62.8%。这个环比增幅主要来自2月春节的低基数效应。但看整个Q1，累计销量410.7万辆，同比只微增2.3%，说明增长引擎并没有想象中那么强劲。\n\n渗透率方面，3月G15平均达到24.3%，比去年同期的22.7%高了1.6个百分点，电动化趋势还在，但速度在放缓。\n\n**2. 区域分化：欧洲反弹，美国塌陷，巴西狂奔**\n\n- **欧洲老牌强国集体回暖**：德国（9.8万辆，+42.8%）、法国（6.1万辆，+51.9%）、意大利（3.3万辆，+84.8%）、英国（14.2万辆，+30.7%），同比增速都在30%以上。英国3月环比暴增309%，可能和季度末冲量有关。\n\n- **美国是唯一负增长的主要市场**：3月销量10.1万辆，同比大跌35.5%；Q1累计25.6万辆，同比-34.3%。渗透率也从9.6%掉到7%。这背后可能是补贴政策退坡和部分车企策\n\n[... middle omitted ...]\n\nny, France, Brazil, UK, South Korea, Canada, Italy and Thailand) and 3 Nordic countries (Norway, Sweden, Finland).\n\nTim Rokossa\n\nHead of Research\n\nChristoph Laskawi\n\nResearch Analyst\n\nNicolai \n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R014",
    "title": "市场真正低估的不是需求，而是供给的价格弹性正在重塑天然气定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给的价格弹性正在重塑天然气定价\n\nHenry Hub 重新站上 3 美元/百万英热单位，这是三月底以来的第一次。天气预期当然是第一推动力，欧洲天然气价格的联动效应也提供了短期支撑。但这些都不是这份研报最值得关注的信息。真正值得产业决策者和投资者反复推敲的，是一个更根本的变化：美国天然气供给端正在展现出过去几年被市场严重低估的价格敏感性。Haynesville 产区产量增长明显放缓，而这一变化恰好发生在价格低于去年同期的背景下。这意味着，天然气市场的供给曲线可能比共识假设要陡峭得多。如果这一信号被证实是结构性趋势，那么当前市场对 2027 年价格压力的担忧，可能需要重新校准。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 价格信号的有效性正在回归，但市场尚未充分定价供给端的反应机制\n\n过去一年，许多市场参与者倾向于认为，Haynesville 产区的产量增长对价格几乎不敏感。无论 Henry Hub 处于什么价位，充足的库存井和持续的基础设施建设都能保证产量稳定增长。然而，2026 年上半年的数据提供了不同的叙事。\n\n报告明确对比了两个时间窗口：2025 年 1-5 月，Henry Hub 均价约为 3.70 美元/百万英热单位，Haynesville 产量从 2024 年 12 月到 2025 年 5 月增长了约 8 亿立方英尺/日。而 2026 年同期，Henry Hub 均价降至约 3.19 美元/百万英热单位，Haynesville 产量反而从 2025 年 12 月下降了约 2 亿立方英尺/日。即便只观察 4 月这个年内产量高点，同比增幅也从 7 亿立方英尺/日骤降至 2 亿立方英尺/日。\n\n这里需要强调一个关键点：市场此前普遍认为，经过 2025 年的大幅增产，Hayn\n\n[... middle omitted ...]\n\n未完全回答的关键问题，以及完整报告中关于价格路径的更多细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n天然气产量开始对价格敏感了\n\n产量对价格有反应了\n\nHenry Hub突破3美元后的供需新逻辑\n\n最近Henry Hub天然气价格重新站上3美元关口，这是3月底以来的首次。背后的驱动力不只是夏季天气预测的演变，还有一些更结构性的变化正在发生。\n\n1️⃣ 价格敏感信号出现\nHaynesville产区今年的产量增长明显放缓。去年1-5月，在均价3.70美元的环境下，该产区产量环比增加了8亿立方英尺/日。而今年同期，在均价3.19美元（甚至4-5月跌破3美元）的背景下，产量反而下降了2亿立方英尺/日。这说明：当价格低于某个阈值，生产商会主动减产。\n\n2️⃣ 库存不是唯一变量\n目前夏季平衡价在3.17美元左右，市场既不紧张也不拥挤。真正的看点在于：Haynesville的钻机数量在1季度已显著增加，这意味着新井可能在4季度投入市场。同时，Permian盆地的伴生气产量预计在2027年达到27.8亿立方英尺/日，比当前高出3.4亿立方英尺/日。\n\n3️⃣ 2027年的关键变量\n真正值得关注的是2027年的供需平衡。随着Permian管道运力在2H26增加45亿立方英尺/日，伴生气产量将大幅攀升。虽然目前Haynesvi\n\n[... middle omitted ...]\n\n price sensitivity as the most relevant, as it can impact how the market manages what we expect to be a further softening of US gas balances into 2027.\n\nFor the balance of summer 2026 we belie\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "化工板块的真正考验不在油价，而在利润峰值能否被消化",
    "digest": "[wechat_article.md]\n# 化工板块的真正考验不在油价，而在利润峰值能否被消化\n\n2026年5月，某外资投行在港股、北京、上海三地路演后，得出了一个让市场必须正视的判断：当前化工板块面临的核心矛盾不是地缘冲突带来的油价波动，而是市场正在定价“2026年上半年可能是未来两年的利润高点”。投资者仓位普遍偏低，不是因为看不懂油价，而是因为看不清利润常态化的位置。\n\n这份路演反馈覆盖了35家机构投资者，信息密度极高。它揭示了一个关键信号：市场已经从“买不买化工”转向了“什么时候买化工”。这个转变背后，是对盈利可持续性的深度怀疑，也是对估值合理性的重新校准。\n\n以下是我们从这份路演反馈中提炼出的五层逻辑，每层都在回答一个更根本的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 仓位偏轻不是情绪问题，而是结构性的等待策略\n\n投资者普遍承认化工板块“难以交易”。原因在于化工作为中游行业，产品价格波动往往被原油价格放大，而原油本身又受地缘冲突影响。当中东局势持续紧张时，化工股的价格走势几乎完全被外部变量主导，企业自身的经营质量反而退居其次。\n\n这意味着，当前的低仓位并非短期悲观情绪的产物，而是一种主动的“等待策略”。投资者并非不看好化工的长期逻辑，而是在等待一个更清晰的定价锚——这个锚可能是地缘局势的明朗化，也可能是盈利周期的底部确认。\n\n从资产定价的角度看，这种等待本身就在压低估值。当大多数资金选择观望时，即使基本面没有恶化，股价也难以获得系统性重估。这反过来又强化了等待的合理性，形成了一种“低仓位-低估值-继续低仓位”的循环。\n\n对于产业决策者而言，这意味着：如果你的公司处于化工中游，当前资本市场的定价已经部分反映了“盈利不可持续”的预期，而不是当前的基本面。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n##\n\n[... middle omitted ...]\n\n口、以及出口政策情景分析的内容，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n化工研报拆解：机构眼里的机会和纠结\n\n📌 当下化工，怎么看？\n\n最近聊了一圈机构投资者，大家对化工板块的态度比较一致——谨慎，但又不想完全离场。\n\n**1/ 仓位很轻，但也不敢空仓**\n化工属于中游行业，原油一波动，产品价格就跟着抖，企业盈利很难把控。所以多数机构目前只是轻仓配置，中东局势没明朗前，不太敢大动作。\n\n**2/ 2026上半年可能是盈利高点**\n一季度部分公司业绩超预期，但机构普遍认为，这主要是原油涨价带来的库存收益。如果下半年地缘冲突降温，化工品价格回落，上半年那种高盈利可能很难持续。现在估值看着合理，但一旦盈利正常化，可能就不便宜了。\n\n**3/ 需求端有隐忧**\n虽然油价还撑着，但5月以来化工品价格其实在跌（Wind数据），说明下游需求已经偏弱。机构担心，高原料成本正在压制采购意愿。跟工业、地产关联度高的品种，大家基本在回避。\n\n**4/ 化肥是少数共识**\n化肥需求相对刚性，是机构比较关注的方向。讨论焦点集中在：出口配额何时放开？全球种植季需求有没有被抑制？硫磺涨价怎么消化？如果下半年农业周期回暖，化肥基本面可能改善。但短期来看，原料成本上涨对利润的挤压，是机构最担心的点。\n\n**5/ \n\n[... middle omitted ...]\n\nicult to trade. As a midstream industry, volatility in chemical product prices, often amplified by movements in crude oil, creates significant pressure on corporate operations. As a result, mo\n\n[... middle omitted ...]\n\ntored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.\n\n[1279589]"
  },
  {
    "id": "R016",
    "title": "中国房地产的真正拐点不在销售端，而在供给端",
    "digest": "[wechat_article.md]\n# 中国房地产的真正拐点不在销售端，而在供给端\n\n过去两年，投资者对中国房地产市场的讨论始终围绕一个核心问题：这轮反弹是情绪驱动，还是基本面改善？多数人倾向于前者。2026年以来的市场表现似乎也支持这一判断——股价波动剧烈，成交数据时好时坏，库存去化周期并未显著缩短。\n\n但某外资投行最新发布的一份研报提出了一个值得认真对待的相反观点：市场真正低估的不是需求何时回暖，而是供给端正在发生的结构性收缩。这份报告的核心判断是，中国房地产的“广义库存”在2023至2025年间下降了约19%，从37.22亿平方米降至30.2亿平方米。这不是一个温和的去化，而是一个数量级的跃迁。\n\n更关键的是，这个趋势仍在加速。如果投资者仍然用传统的“库存去化月数”来衡量市场健康度，可能会错过一个正在形成的供需再平衡。报告认为，供给侧的收紧正在为更可持续的复苏奠定基础——不仅仅是情绪修复，而是基本面层面的改善。\n\n这个判断如果成立，意味着过去几年主导房地产投资逻辑的“供过于求”叙事正在被改写。我们需要问的是：库存下降的驱动力是什么？哪些城市的信号最明确？对不同类型的开发商意味着什么？以及，这个趋势的可持续性如何？\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 广义库存的下降并非来自销售加速，而是来自新开工的持续萎缩\n\n理解当前库存变化的关键，在于区分“狭义库存”和“广义库存”。狭义库存通常指已竣工但未售出的房屋，这是市场最常跟踪的指标。广义库存则包括未开发土地、在建但未取得预售证的项目、以及已竣工未售房源。\n\n报告估算，广义库存从2023年的37.22亿平方米降至2025年的30.2亿平方米，降幅约19%。但驱动因素并非销售端爆发，而是新开工面积的持续萎缩。2025年，全国新开工面积已降至约4.5亿平方米，而同期销售面积约为16.5\n\n[... middle omitted ...]\n\n跟踪、或者开发商的估值重估逻辑感兴趣，这里会有更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n地产库存真的在快速出清\n\n📉 库存正在快速收窄\n\n---\n\n过去两年，市场一直在讨论地产供应收缩，但数据终于开始说话了。\n\n某外资投行最新研报显示，2023-2025年，全国广义库存下降了约19%（从37.2亿平米降至30.2亿平米）。这不是情绪驱动，而是实实在在的结构变化。\n\n核心逻辑其实很简单👇\n\n**1️⃣ 卖得比建得快**\n\n2023年以来，每年新开工面积持续低于销售面积，意味着开发商一直在“吃老本”——消耗已开工但未销售的库存。到2025年底，这部分面积从25亿平米降到了19亿平米。\n\n**2️⃣ 库存结构正在变化**\n\n未开发土地和在建未取证项目大幅减少，剩余库存越来越集中在已完工现房和未开工项目上。虽然现房去化仍是短期重点，但随着新开工减少，现房库存也会逐步下降。\n\n**3️⃣ 闲置土地回购加速**\n\n2026年Q1，地方政府发行了480亿专项债用于闲置土地回购，同比+56%。重庆、广东等地力度较大，重庆计划回购面积占2019-2024年卖地面积的16%。如果更多城市将回购比例提升至10%（目前全国平均约5.5%），广义库存还能再降5-10%。\n\n**4️⃣ 深圳已经出现信号**\n\n深圳库存快速\n\n[... middle omitted ...]\n\nn the rally, 7 May 2026). We see fundamentals doing the heavy lifting. Beyond resilient near-term sales, a tightening supply pipeline should help extend the recovery. Shenzhen's fast-declining\n\n[... middle omitted ...]\n\nystem, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.\n\n[1279524]"
  },
  {
    "id": "R017",
    "title": "出口才是中国汽车利润的真正锚点",
    "digest": "[wechat_article.md]\n# 出口才是中国汽车利润的真正锚点\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内需求疲软不是短期波动，而是结构性问题正在重塑竞争逻辑\n\n这份来自某外资投行的中国汽车行业追踪报告，在4月数据中捕捉到了一个容易被忽视的信号：国内汽车零售量同比下降21%，而新能源车零售量虽然同比仅下降6%，但环比已经持平。更值得关注的是，1-5月前10天国内乘用车销量继续同比下降21%，渠道库存指标从1.5上升至1.89，库存预警指数从57.5%跳升至62.1%。\n\n这些数字叠加在一起，指向的不是一个简单的周期性回调。报告明确指出，国内需求疲软背后有三个结构性因素：政策刺激效应的退潮、提前消费需求的透支效应、以及油价高企背景下燃油车需求的持续萎缩。这三个因素没有一个是短期能够逆转的。\n\n所以，报告将2026年国内需求预测下调，就不是一个战术判断，而是一个战略判断。这意味着，过去几年市场习惯的“中国汽车增长故事”已经切换了章节。国内市场的竞争，将从“做大蛋糕”转向“存量博弈”，而存量博弈的赢家，不一定是销量最大的企业，而是那些在特定价格带和技术维度上建立护城河的企业。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 出口才是当前中国车企盈利能力的真实支撑，而不是国内份额\n\n报告给出的出口数据是整个分析中最硬的信号。4M26中国乘用车出口量达到270万辆，同比增长69%。其中，新能源车在出口中的占比从38%提升至49%，这意味着出口增长主要由电动车驱动，而不仅仅是燃油车的海外替代。\n\n奇瑞、比亚迪和吉利是出口的主力军。但这里有一个更重要的洞察：出口不仅仅是量的补充，更是利润结构的优化。在国内市场，折扣率已经上升到10.9%，而出口市场由于定价权和竞争格局的不同，盈利能力显著优于国内。报告虽\n\n[... middle omitted ...]\n\n讨论，我们会基于完整报告和最新数据，持续跟踪这些变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n国内车市四月遇冷，出口成唯一亮点\n\n车市四月遇冷\n出口撑起半边天\n\n国内新能源车市四月遇冷，但出口数据非常亮眼。刚读完一份外资投行的中国电动车追踪报告，几个关键点值得关注。\n\n📊 国内需求持续承压\n四月新能源零售84.8万辆，环比持平，同比下滑6%。整体乘用车需求更是同比下降21%。主要原因：政策红利消退、提前消费透支需求、油价高位抑制燃油车消费。\n\n五月初的情况也不乐观，1-10日乘用车销量同比再降21%。渠道库存高企，行业仍在去库存阶段。\n\n💰 锂价上涨引发连锁反应\n碳酸锂价格已涨至约20万元/吨。比亚迪率先宣布五月涨价，多家车企跟进。研报认为，这波涨价对短期需求是额外压力。\n\n🚀 出口成为增长引擎\n前四个月中国乘用车出口达270万辆，同比增长69%。奇瑞、比亚迪、吉利领跑。电动车占比从38%提升至49%，出口结构持续优化。\n\n出口强劲的背后：产品竞争力提升 + 高油价增强电动车成本优势。在国内需求疲软背景下，出口成为支撑产能利用率、盈利能力和产品结构改善的关键。\n\n🔋 下半年有望回暖\n虽然短期承压，但研报认为下半年行业情绪将逐步改善。竞争焦点正从价格战转向技术整合和用户体验。\n\n近期新品表现亮眼：比亚迪\n\n[... middle omitted ...]\n\n weakness in ICE demand amid elevated oil prices. The soft tone has continued into early May. Domestic passenger car sales for 1–10 May were again down 21% y-o-y, and elevated channel inventor\n\n[... middle omitted ...]\n\nystem, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.\n\n[1279533]"
  },
  {
    "id": "R018",
    "title": "AI铜箔的真正瓶颈不是产能，而是规格升级的速度",
    "digest": "[wechat_article.md]\n# AI铜箔的真正瓶颈不是产能，而是规格升级的速度\n\n当市场把目光集中在AI芯片算力竞赛、服务器出货量、以及PCB和CCL的产能扩张时，一个上游材料的结构性变化正在悄然发生，而它可能成为未来2-3年AI基础设施供应链中最被低估的瓶颈。\n\n某外资投行最新发布的PCB/CCL产业链更新报告，将焦点对准了电解铜箔——这个在CCL成本中占比约30%、在高端PCB成本中占比约5%的关键材料。报告的核心判断是：高速铜箔的需求正在从HVLP1/2/3向HVLP4加速迁移，叠加DTH（直接压合铜箔）的渗透率提升，铜箔行业的平均售价（ASP）正在经历非线性跃升，而供给缺口恰好为中国供应商打开了窗口期。\n\n这不是一个简单的“量增”故事，而是一个“规格升级驱动价值重定价”的结构性变化。理解这一点，比跟踪下个月的出货量更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI基础设施的扩建正在将铜箔需求从“吨级”推向“万吨级”，但真正驱动价值的是规格跃迁\n\n报告给出了一个清晰的量化框架：2025年全球AI CCL月需求约为180万张/月，对应HVLP铜箔需求约1.3千吨/月。到2030年，这两个数字将分别增长至超过900万张/月和6千吨/月，对应30-40%的年复合增长率。\n\n这个数字本身已经足够有冲击力。但报告真正有价值的洞察在于：需求增长只是基础，规格升级才是价值放大器。\n\n传统HTE铜箔（高温延伸铜箔）是典型的商品化产品，广泛应用于消费电子、汽车等中低端领域，单价低、竞争激烈。而HVLP铜箔，特别是HVLP4及以上规格，其单价可以达到HTE的10倍以上。DTH铜箔的单价甚至可以达到HVLP4的约2倍。\n\n这意味着，即使出货量增长放缓，只要规格持续上移，整个铜箔市场的价值量增速将显著高于出货量增速。报告预计，主要AI玩家（包括NV\n\n[... middle omitted ...]\n\n分析进行了深度拆解，并会在社群中持续更新产业链的第一手动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜箔，AI基建的下一个瓶颈？\n\nAI基建，缺铜箔\n\nAI服务器的铜箔正在从HVLP1/2/3升级到HVLP4，价格可能飙升10倍以上。国内厂商正在填补供给缺口。\n\n---\n\n最近在研究AI基建的上游材料，发现铜箔这个环节很有意思，值得和大家聊聊。\n\n**1/ 为什么铜箔突然重要了？**\n\nAI服务器对数据传输要求极高，传统铜箔已经不够用了。现在主流方案是HVLP（高压低压铜箔），技术壁垒高、价值量大。投行研报预测，AI CCL（覆铜板）月需求将从2025年的约180万张，以30-40%的年复合增速，增长到2030年的900万张以上。\n\n换算成HVLP铜箔，月需求将从约1.3千吨增长到6千吨以上。\n\n**2/ 价格可能涨10倍**\n\n更关键的是规格升级。从HVLP1/2/3升级到HVLP4，价格可能是传统HTE铜箔的10倍以上。而更先进的DTH铜箔，价格甚至是HVLP4的2倍。\n\n主要AI玩家（某几家大厂）预计在2026下半年开始大规模切换新服务器规格，这会带来巨大的HVLP4需求。某日本供应商给出的15-20%年增长预期，可能偏保守了。\n\n**3/ 供给缺口怎么补？**\n\n如果只看国际厂商的产能，2027年H\n\n[... middle omitted ...]\n\noing our previous initiation on PCB (Link), given we forecast \\~60%/70% CAGR of AI PCB/CCL TAM in 2025-30E driven by tech giants' rising capex plans on AI infra buildout, this trend has also b\n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R019",
    "title": "夏季用电高峰前，煤炭市场真正被低估的不是需求，而是供给侧的季节性收缩力度",
    "digest": "[wechat_article.md]\n# 夏季用电高峰前，煤炭市场真正被低估的不是需求，而是供给侧的季节性收缩力度\n\n过去几周，动力煤与焦煤价格同步出现周度环比上涨。秦皇岛港5500大卡动力煤价格已回升至715元/吨，山西大同5800大卡坑口价格单周上涨2.9%。这些数字本身并不惊人，但真正值得关注的，是它们背后一个容易被忽视的结构性信号：4月煤炭产量环比下降12.5%，同比也出现1%的负增长。这不是一个随机波动，而是冬季供暖季结束后，供给端系统性收缩的开始。\n\n某外资投行最新发布的煤炭周报指出，当前煤炭库存处于近年同期低位，沿海与内陆主要电厂的库存水平较去年同期低0.5%至2.9%。在夏季降温需求即将到来的背景下，供给侧的收缩与库存的低位，正在为煤炭价格构筑一个比市场预期更坚实的底部。\n\n市场对煤炭板块的讨论，往往聚焦于可再生能源替代和长期需求见顶。但这份报告揭示了一个更近期的矛盾：短期供需缺口可能比大多数投资者预期的更紧。本文将从产量季节性规律、库存结构、价格传导机制以及报告未完全展开的关键变量四个层面，拆解这一判断背后的逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月产量环比骤降12.5%，季节性是表层原因，深层是供给弹性正在收窄\n\n4月中国煤炭产量降至3.86亿吨，环比下降12.5%，同比下降1%。从历史数据看，每年3月供暖季结束后，4月产量确实会出现季节性回落。但今年的环比降幅，需要放在更长的周期中评估。\n\n报告提供的图表数据揭示了一个重要趋势：自2021年以来，中国月度煤炭产量从4.8亿吨的峰值区域逐步回落，至2025-2026年维持在4.2-4.5亿吨区间。这意味着，即便在旺季，供给端也未能回到2021年的高位。更关键的是，4月产量3.86亿吨的水平，已经低于2023年和2024年同期的产出。\n\n这里需要回答一个“为什么”。供\n\n[... middle omitted ...]\n\n影响、水电来水预测、以及各煤种价差套利机会，做更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月煤炭产量季节性回落，价格已企稳\n\n📉 产量季节性下滑，库存低位\n\n煤炭产量4月环比降12.5%\n\n📊 动力煤焦煤价格周环比均上涨\n\n最近某外资投行的煤炭周报更新了不少信号，我帮你提炼几个关键点👇\n\n**1️⃣ 动力煤价格延续回暖**\n- QHD 5500大卡煤价周环比微涨0.3%至715元/吨\n- CCI 5500指数周涨1.3%至835元/吨\n- 山西大同5800坑口价周涨2.9%至705元/吨\n- 但海运煤NEWC价格周跌1.5%，内外价差在收窄\n\n**2️⃣ 焦煤价格多数上涨**\n- 柳林4号主焦煤坑口价周涨2.9%至710元/吨\n- 车板价周涨1.9%至1640元/吨\n- 澳洲昆士兰焦煤微跌0.4%至239美元/吨\n\n**3️⃣ 产量季节性下滑明显**\n- 4月原煤产量3.86亿吨，同比降1%，环比降12.5%\n- 冬季供暖季结束后，产量回落是正常季节性规律\n- 但1-4月累计产量仍同比增1.2%\n\n**4️⃣ 夏季需求预期乐观**\n- 研报认为，虽然可再生能源在替代，但夏季降温用电需求会推高火电出力\n- 截至5月14日，沿海及内陆电厂煤炭库存同比低0.5%-2.9%\n- 迎峰度夏前，补库需求可能\n\n[... middle omitted ...]\n\n rose 2.9% WoW, to Rmb710/t...   \n• ...while FOR prices rose 1.9% WoW, to Rmb1,640/t.   \n- QLD prices dipped 0.4% WoW, to US\\$239/t.\n\nChart of the week – May coal production showed seasonal de\n\n[... middle omitted ...]\n\nesources Group Limited (0639.HK)</td><td>O (09/15/2022)</td><td>HK$2.60</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R020",
    "title": "市场低估的不是销售反弹，而是反弹的不可持续",
    "digest": "[wechat_article.md]\n# 市场低估的不是销售反弹，而是反弹的不可持续\n\n4月房地产销售数据出现了预期内的收窄，全国商品住宅销售额同比仅下降6.4%，较3月的-15.2%明显改善。但这份某外资投行最新发布的研报，真正值得关注的判断并不在销售数字本身。\n\n报告的结论是：**这轮反弹的可持续性存疑，真正的结构性风险仍在供给端，而非需求端。**\n\n这不是一份简单的月度数据点评。它背后隐含着对2026年全年房地产投资逻辑的重新梳理。在股价近期已经有所反弹的背景下，报告明确表示“风险回报比正在向负面倾斜”。这意味着，如果市场只是简单地将4月数据解读为“见底信号”而继续追高，可能会忽视几个尚未被定价的关键变量。\n\n以下是我们从这份研报中提取的几个核心洞察，以及它们对投资决策的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月销售收窄的本质是低基数效应，而非需求回暖\n\n4月全国商品住宅销售额同比下降6.4%，销售面积同比下降9.1%，较一季度-15.2%和-10.3%的降幅确实收窄。但如果拆解月度环比数据，4月销售额较3月环比下降33.7%，销售面积环比下降41.3%。这组数据揭示了一个关键事实：所谓的“改善”几乎完全来自2025年4月的低基数，而非需求的实质性回暖。\n\n更值得警惕的是，3月的数据本身也并非趋势性改善。3月销售额同比下降13.3%，销售面积同比下降7.4%，同样是在2025年3月基数较低的基础上实现的。将两个月连起来看，2026年一季度整体销售金额同比下降15%，销售面积同比下降10%，这个斜率并未出现明显拐点。\n\n这意味着什么？如果市场将4月数据解读为“销售见底”，那么它可能正在犯一个典型的基数效应误判。真正的需求面——居民收入预期、杠杆空间、购房意愿——在报告引用的AlphaWise调查中仍在恶化。没有需求的回暖，任何由基\n\n[... middle omitted ...]\n\n这些未解问题，我们会持续跟踪这些变量的变化，并及时更新判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月楼市数据解析：跌幅收窄但持续性存疑\n\n4月楼市跌幅收窄，但别急着乐观\n\n---\n\n最近某外资投行发布了中国房地产研报，核心判断是：4月销售数据确实比3月好看，但反弹的持续性需要打个问号。\n\n**1/ 数据改善，但主要是低基数效应**\n\n4月全国商品房销售额同比-7.6%，销售面积同比-9.5%，相比3月的-17%和-10%确实明显收窄。但仔细看，这个改善主要是因为去年4月基数太低。前4个月累计销售额同比-14.6%，累计面积同比-10.2%，整体还在下滑通道中。\n\n70城房价指数继续小幅下跌，3月新房和二手房环比均-0.2%，跌幅没有扩大也没有缩小。一线城市二手房相对坚挺，环比+0.4%，新房+0.1%。\n\n**2/ 开工和竣工数据更弱**\n\n3月竣工面积同比-19%，新开工面积同比-27%，比前两个月还差。房地产投资前4个月同比-13.7%，比一季度的-11.2%进一步扩大。研报认为开发商对拿地仍然谨慎，2026年施工活动大概率继续低迷。\n\n**3/ 二手房回暖可能是昙花一现**\n\n3-4月部分高能级城市二手房成交确实超出预期，但进入5月后，最新几周的数据已经出现明显回落。城市之间的分化也在加剧，部分二\n\n[... middle omitted ...]\n\nin value and -10% in volume in 4M26. The NBS 70-city home price index continued to edge down, at a similar pace, falling 0.2% m-m in both primary and secondary markets in March (vs. -0.2% and \n\n[... middle omitted ...]\n\nerty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.66</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "4月社零数据真正值得关注的不是0.2%，而是“补贴效应退潮”后的结构性分化",
    "digest": "[wechat_article.md]\n# 4月社零数据真正值得关注的不是0.2%，而是“补贴效应退潮”后的结构性分化\n\n2026年4月中国社会消费品零售总额同比增长0.2%，不仅低于市场预期的2%，更较3月的1.7%进一步放缓。如果只看这个数字，很容易得出“消费复苏再次受阻”的简单结论。但某外资投行最新发布的这份研报告诉我们，数字背后的结构性变化远比总量放缓更重要。\n\n真正值得关注的信号有两条：第一，零售商品在疫情后首次出现同比负增长（-0.1%），这是标志性事件；第二，补贴驱动的消费脉冲正在快速消退，而市场对这一“退潮效应”的定价可能仍不充分。换句话说，消费板块的分化正在从“可选vs必选”的粗框架，转向“补贴受益vs补贴免疫”的精细逻辑。\n\n这份报告的核心价值不在于告诉读者4月数据有多差，而在于提供了一个框架，帮助理解为什么某些品类在总量放缓中反而加速增长，以及哪些企业可能在这轮分化中跑出超额收益。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 零售商品首次转负的背后，是补贴效应退潮而非需求崩塌\n\n4月零售商品同比增速从3月的1.5%骤降至-0.1%，这是疫情后首次出现负增长。但更值得细看的是对比2019年的CAGR：从4.0%降至2.9%。这意味着，即便剔除基数效应，整体消费动能也在放缓，但放缓幅度并没有同比数字显示的那么极端。\n\n关键在于理解“补贴效应退潮”这个变量。电子家电品类从3月的-5.0%进一步恶化至-15.1%，家居用品从-8.7%跌至-10.4%。这两个品类恰恰是此前以旧换新、消费补贴政策的主要受益者。补贴政策在2025年下半年至2026年初曾显著拉动需求，但这种拉动本质上是在透支未来需求。当补贴力度减弱或政策预期消化完毕，需求自然回落。\n\n这引出一个重要判断：市场此前对消费复苏的定价，可能过度包含了补贴的持续性，而对补贴退潮后的真\n\n[... middle omitted ...]\n\n数据的变化，以及AI换机周期、补贴政策走向等关键变量的演进。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月消费数据出来了，整体节奏在放缓。\n\n消费复苏的节奏比想象中要慢一些\n\n4月社零同比仅增长0.2%，低于市场预期的+2%，对比3月的1.7%也在减速。如果跟2019年比，年复合增速从3月的4.0%降到了2.9%。\n\n几个关键变化值得留意：\n\n1️⃣ 商品零售首次转负\n商品零售同比-0.1%，是疫后首次负增长。线上零售增速也从5.8%放缓到2.3%（部分受高基数影响）。餐饮相对有韧性，但增速也从2.9%降到2.2%。\n\n2️⃣ 可选消费是主要拖累\n- 金银珠宝：同比-21.3%（3月还是+11.7%），金价波动影响明显\n- 家电：同比-15.1%（3月-5%），补贴效应在消退\n- 家居：同比-10.4%（3月-8.7%），地产相关需求依然疲软\n\n3️⃣ 唯一加速的品类\n烟酒是唯一增速加快的品类，从3月的7.7%提高到11.7%。食品饮料整体增速从9.0%放缓到5.4%。\n\n某外资投行认为，五一假期的消费情绪偏软，5月难有明显反弹。他们关注三条主线：\n- 供给调整+需求改善：蒙牛、伊利\n- 线下消费改善：百胜中国、海底捞、华润啤酒\n- 公司自身驱动反转：巨子生物\n\n消费复苏的路还是渐进式的，有波动很正常。你们最\n\n[... middle omitted ...]\n\nCovid and online sales (partly from high comp base). Restaurants relatively resilient with some slowdown to 2.2% from 2.9% in March. Among goods, discretionary categories are the main drag: Go\n\n[... middle omitted ...]\n\n76</td></tr><tr><td>Techtronic Industries Co Ltd (0669.HK)</td><td>O (12/05/2019)</td><td>HK$118.00</td></tr><tr><td>Yue Yuen Industrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$14.98</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R022",
    "title": "中国房地产的真正拐点，可能已经出现在二手房市场",
    "digest": "[wechat_article.md]\n# 中国房地产的真正拐点，可能已经出现在二手房市场\n\n过去两年，市场一直在争论中国房地产的底部在哪里。大多数讨论围绕新房销售何时企稳、开发商债务如何化解、政策何时真正见效展开。这些议题当然重要，但某外资投行最新一期周度数据库追踪报告提供了一个容易被忽视却更具前瞻性的信号：**二手房市场的交易量正在以远超新房的速度恢复，而这一结构性分化，可能才是理解行业下一步走向的关键。**\n\n截至5月17日当周，该机构追踪的50城新房周度注册成交量同比增长5%，较前一周的-3%明显改善。但更值得关注的是10城二手房周度注册成交量同比飙升49%，远高于前一周的17%增速。一线城市二手房成交量同比大增65%，二线城市也达到40%。\n\n新房市场在政策刺激下终于转正，这符合预期。但二手房市场的弹性远超新房，且这一趋势正在加速。这意味着什么？**市场的定价权正在从开发商向存量房业主转移，行业的价值创造逻辑正在被重写。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二手房成交量的爆发不是短期脉冲，而是结构性的需求迁移\n\n周度数据容易被视为噪音，但把时间拉长到年初至今，这一趋势更加清晰。50城新房年初至今累计成交量仍同比下降15%，而10城二手房累计成交量已同比转正至+3%。新房仍在去库存的泥潭中挣扎，二手房却已经站上同比正增长的地板。\n\n这不仅仅是基数效应的结果。从周度环比看，二手房成交量增速从前一周的17%跳升至49%，而新房仅从-3%改善至5%。二手房市场的边际改善斜率明显更陡峭。\n\n更深层的原因是：购房者的偏好正在发生不可逆的转变。过去几年新房交付风险、质量不确定性、以及开发商信用问题，让越来越多的购房者转向二手房市场。二手房“所见即所得”的优势在风险厌恶周期中被放大。这不是一个短期现象，而是住房消费从“买期房”向“买现房”的长期\n\n[... middle omitted ...]\n\n，或者具体公司的估值修复路径感兴趣，社群里会有更细致的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新房成交回暖，二手房热度更高\n\n市场数据回暖中\n\n某外资投行最新周度数据显示，中国楼市正在出现一些积极信号。\n\n截至5月17日当周，50城新房成交同比转正，增长5%。而前一周还是下降3%。这个变化虽然不大，但方向值得关注。\n\n更亮眼的是二手房。10城二手房成交同比大增49%，前一周只有17%的增幅。二手房的活跃度明显超过新房。\n\n分城市来看：\n1️⃣ 一线城市新房成交同比+5%，比前一周的-4%明显改善\n2️⃣ 二线城市新房成交同比+6%，前一周是0%\n3️⃣ 三线城市新房成交同比+1%，前一周是-9%\n\n二手房方面：\n🔹 一线城市同比+65%，前一周是+25%\n🔹 二线城市同比+40%，前一周是+12%\n\n不过也要看到，新房年初至今累计成交同比仍为-15%，说明整体回暖还需要时间。二手房累计同比已经转正，+3%。\n\n另外，中原地产6城二手房挂牌价指数为18.5%，较前一周的19.4%有所下降。挂牌价在走低，可能说明业主心态在变化。\n\n研报未给出具体原因分析，但结合数据来看，政策放松的效果可能正在逐步显现，特别是二手房市场的流动性明显改善。\n\n新房市场虽然没有新项目推出，但存量房的成交在回暖。这是一个值得持续\n\n[... middle omitted ...]\n\nWeekly secondary registered unit sales in 10 cities increased $49\\%$ YoY (vs. $+17\\%$ YoY in the previous week), bringing YTD sales to $+3\\%$ YoY: Tier 1 city weekly secondary unit sales ros\n\n[... middle omitted ...]\n\nerty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.40</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R023",
    "title": "运营商卖“Token包月”不是跟风，是供给侧定价权的重新校准",
    "digest": "[wechat_article.md]\n# 运营商卖“Token包月”不是跟风，是供给侧定价权的重新校准\n\n中国电信刚刚在全国范围推出了面向企业和个人的Token套餐。这则消息在科技新闻里可能只是一条产品发布，但放在运营商过去十年的转型史中，它释放了一个值得产业决策者认真对待的信号：当移动数据流量红利见顶、资费持续下行，三大运营商正在用同一套基础设施，去试探一个完全不同的定价逻辑。\n\n某外资投行最新研报对此给出了一个克制但重要的判断。报告没有用“颠覆”“革命”这类词汇，而是将此举定位为“在AI时代测试新商业模式的积极尝试”。但这个判断背后隐藏的问题，可能比产品本身更值得追问：运营商卖Token，是在模仿云厂商，还是在走一条属于自己的路？这条路走通的关键，是技术能力，还是定价策略，还是别的什么？\n\n这份报告的核心价值，不在于它描述了电信推出了什么套餐，而在于它提供了一个观察框架——当基础设施提供者开始按“智能”而不是按“流量”收费，整个AI产业链的价值分配逻辑正在发生微妙但结构性的变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国电信的Token套餐，真正的新意不在“Token”，而在“统一定价”\n\n先看产品本身。中国电信此次推出的套餐分为企业版和个人版两类，按月订阅。企业版三个档位，从每月39.9元到299.9元，包含的Token数量从1500万到1.5亿不等，折合每百万Token的价格在2.0元到2.7元之间。个人版更便宜，每月9.9元到49.9元，每百万Token价格在0.6元到1.0元。\n\n表面上，这是一个典型的订阅制定价模型。但报告敏锐地指出了一个关键差异：与阿里云等云厂商的Token方案不同，中国电信的方案对旗下接入的所有模型统一定价。也就是说，无论是调用中国电信自研的模型，还是接入GLM5.1、DeepSeek V3.2等第三方生态\n\n[... middle omitted ...]\n\n解。如果你对这份研报有自己的判断，也欢迎带着问题来群里碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n运营商开始卖AI“流量包”了\n\n运营商卖AI，香不香\n\n中国电信刚刚推出全国统一的AI Token套餐，按用量收费，像极了当年的手机流量包。\n\n1⃣️ 价格结构很清晰\n- 企业版：39.9元/月（1500万token）到299.9元/月（1.5亿token）\n- 个人版：9.9元/月（1000万token）到49.9元/月（8000万token）\n- 企业版每百万token约2-2.7元，个人版约0.6-1元\n\n2⃣️ 跟云厂商有什么不同\n阿里云等厂商的Token套餐是按“座席+模型”定价，不同模型消耗不同额度。但电信的方案更简单——所有模型统一定价。企业版能调用主流模型（包括电信自研和GLM5.1），个人版能用DeepSeek V3.2等生态模型。\n\n3⃣️ 为什么运营商要干这事\n移动数据流量见顶，资费持续下降，运营商需要新增长点。它们有现成的数据中心和算力基础设施，做AI服务是顺理成章的延伸。\n\n4⃣️ 但挑战也不小\n短期内，个人用户真正用起来还得等杀手级AI应用出现。企业侧，竞争拼的是服务能力、MaaS平台指标和自研模型水平。目前移动和联通只在省级试点，电信是第一个全国铺开的。\n\n个人觉得，这是运营商在\n\n[... middle omitted ...]\n\nas Alicloud also offer token plans but the package includes credits per seat per month, where different underlying models would result in different credit usages. Whereas China Telecom's plan \n\n[... middle omitted ...]\n\nr><tr><td>GDS Holdings Ltd (GDS.O)</td><td>++</td><td>US$42.44</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R024",
    "title": "印度燃料涨价的真正信号：零售商的亏损修复才刚刚开始",
    "digest": "[wechat_article.md]\n# 印度燃料涨价的真正信号：零售商的亏损修复才刚刚开始\n\n当印度柴油和汽油价格在近期再次小幅上调90派萨/升时，市场习惯性地将其解读为一次寻常的行政调价。但这份来自某外资投行的研报揭示了一个更深的逻辑：这轮涨价不是终点，而是一系列结构性修复的起点。真正重要的不是单次调价的幅度，而是它背后隐含的定价机制回归、亏损收窄路径，以及哪些公司将在这一过程中获得超额收益。\n\n报告的核心判断是：印度石油营销公司(OMCs)的运输燃料亏损已从此前的约15.5美元/桶收窄至9美元/桶，但更值得关注的是，液化石油气(LPG)的亏损仍高达每月10亿美元。这意味着，即便经历了累计约6.5美元/桶的涨价，零售商的利润修复仍处于早期阶段。而过去经验表明，OMCs在每日定价机制下有能力将涨价分散实施，对消费量的冲击有限。这为后续持续涨价提供了操作空间。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮涨价不是一次性事件，而是亏损修复周期的开始\n\n研报明确指出，此轮柴油和汽油累计涨价幅度相当于布伦特原油价格每桶82美元的水平。这个数字本身并不惊人，但结合运输燃料亏损从15.5美元/桶降至9美元/桶的变化，我们可以推导出一个关键判断：OMCs的盈亏平衡点远高于当前零售价格。\n\n更值得关注的是，液化石油气的亏损问题被严重低估。每月10亿美元的亏损规模，意味着即便政府过去曾对这类受控产品进行补贴，当前的价格机制仍然无法覆盖成本。这不仅是OMCs的财务负担，更是一个政策定价与市场成本脱节的系统性风险。\n\n从行业竞争格局看，亏损修复对不同公司的影响是非对称的。研报特别指出，印度斯坦石油公司(HPCL)是最大受益者，其次是巴拉特石油公司(BPCL)。这种排序并非随机，而是反映了各公司业务结构中运输燃料与LPG的占比差异。对于关注印度能源板块的投资者而言，\n\n[... middle omitted ...]\n\n被压缩在一份短报告中的关键信号，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度又调油价，这次逻辑有点不一样\n\n🎯 油价再涨，但这次不是坏事\n\n印度柴油和汽油又涨价了，每升上调0.9卢比，折算下来相当于每桶原油涨了6.5美元（约4-4.5%）。听起来像是老调重弹，但这次研报的视角很有意思——它更像是好事。\n\n1️⃣ 亏损在收窄\n这次调价把零售商的运输燃料亏损从之前的水平压缩到每桶9美元。虽然还没完全扭亏，但方向是对的。研报预计未来几周还会有进一步调价动作。\n\n2️⃣ 定价机制变了\n过去印度油价的调整是“每日定价机制”在起作用，也就是每天/每周微调，而不是一次性大幅跳涨。这种温和节奏对消费端的冲击更小，不容易引发需求骤降。\n\n3️⃣ 谁最受益？\n从产业链看，炼油商是最大赢家。研报明确排序：HPCL受益最大，其次是BPCL，Reliance和ONGC也有正面影响。更重要的是，持续的油价上调有助于改善这些公司长期盈利能力——这才是核心逻辑。\n\n4️⃣ 但有个“隐形成本”\n液化石油气（LPG，即家用燃气）这块还在亏，每月亏损约10亿美元。虽然政府历史上会补贴这部分亏损（因为LPG是管制产品），但这个窟窿还在。\n\n📊 一组有意思的数据\n研报给出了亚洲各国汽柴油批发/零售价格对比表：\n- 印度批\n\n[... middle omitted ...]\n\nin the past, as cooking gas is a controlled product   \nHPCL benefits the most, followed by BPCL. Reliance and ONGC also benefit; more importantly, fuel price hikes help improve long-term profi\n\n[... middle omitted ...]\n\nata Chemicals Limited (TTCH.NS)</td><td>U (03/23/2026)</td><td>Rs730.35</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R025",
    "title": "市场对保险板块的悲观已充分定价，但真正的上行风险来自结构而非弹性",
    "digest": "[wechat_article.md]\n# 市场对保险板块的悲观已充分定价，但真正的上行风险来自结构而非弹性\n\n在经历了一季度普遍偏弱的盈利和投资收益率数据之后，许多投资者的第一反应是避险。某外资投行最新发布的亚太保险营销包却给出了一个看似反直觉的判断：一季度的盈利压力已是过去式，市场自四月以来已经反弹，而真正的上行风险尚未被充分定价。这份报告并非简单地看多保险股的周期性修复，而是试图拆解一个更深层的问题——当传统盈利弹性叙事失效，哪些结构性变量才是真正驱动估值重估的力量。\n\n报告覆盖了从AIA、友邦中国到平安、国寿、太保、人保财险等核心标的，数据截止至2026年5月15日。核心信号可以提炼为一句话：保险行业的基本面正在发生一次“质量优先于数量”的切换，而市场对这一切换的定价尚不充分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一季度盈利下滑的归因远比表面复杂，投资端拖累掩盖了保险业务的真实韧性\n\n如果只看净利润，一季度的表现确实令人担忧。中国人寿净利润同比下降32%，人保集团下降31%，人保财险下降24%，中安在线更是下降70%。但报告通过拆解盈利结构揭示了一个被忽视的事实：保险业务端的盈利实际上是稳定的，甚至略有改善。\n\n以平安为例，其保险业务税前利润从1Q25的270亿微增至1Q26的280亿，而投资端税前利润则从-120亿扩大至-150亿。国寿的保险业务利润从260亿降至240亿，降幅远小于净利润的32%。换言之，一季度盈利的下滑几乎完全由投资端拖累，而非保险业务的恶化。\n\n这一区分至关重要。投资端的波动是市场已知的变量——利率下行、权益市场震荡已在预期之中。但保险业务端的韧性意味着，如果市场环境改善，盈利修复的弹性可能比表面数字所暗示的要大。更重要的是，报告数据显示，大多数险企的BVPS在一季度实现了环比正增长——平安+1.8%、太保+5\n\n[... middle omitted ...]\n\n及如何构建一个既能捕捉上行风险又能管理下行风险的保险股组合。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 保险业一季报：盈利承压但业务质量在变好\n\n**封面：** 保险一季报拆解\n\n**副标题：** 盈利降了，但业务结构更健康了\n\n---\n\n某外资投行刚发了港中保险业1Q26的总结，核心判断是：**一季度盈利压力基本消化，后续向上空间可能更大。**\n\n几个关键发现，值得认真看👇\n\n**1️⃣ 盈利分化明显**\n- 平安、太保、新华、太平人寿的净利润同比正增长（+8%、+4%、+11%、+6%）\n- 国寿、人保集团、众安则下滑显著（-32%、-31%、-70%）\n- 主要原因：投资收益率普遍下降，但保险主业本身其实很稳\n\n**2️⃣ 投资收益率集体走低**\n- 年化总投资收益率从1Q25的2.8%-5.7%，降至1Q26的2.0%-3.2%\n- 降幅最明显的是新华（5.7%→2.1%）和人保财险（4.8%→2.8%）\n- 这是盈利下滑的核心拖累项\n\n**3️⃣ 寿险业务质量在提升**\n- 新单保费（APE）增速亮眼：人保寿+47%、太保+42%、新华+20%\n- 更关键的是**价值率（VNB margin）在改善**——国寿从14%→20%，太保14%→16%，新华13%→15%\n- 说明保险公司在主动优化结构\n\n[... middle omitted ...]\n\n9\n\n# HONG KONG/CHINA INSURANCE\n\n# Asia Pacific\n\nIndustry View Attractive\n\nMS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm ma\n\n[... middle omitted ...]\n\nnce Co Ltd (6060.HK)</td><td>O (05/30/2023)</td><td>HK$11.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "人形机器人产业已跨越“技术可行性”鸿沟，真正的竞赛在“可量产性”与“运营数据飞轮”",
    "digest": "[wechat_article.md]\n# 人形机器人产业已跨越“技术可行性”鸿沟，真正的竞赛在“可量产性”与“运营数据飞轮”\n\n过去一年，市场对物理人工智能（Physical AI）的讨论集中在“机器人能不能学会走路、抓取、上下楼梯”。这些是技术问题，也是风险资本愿意在早期阶段买单的理由。但进入2026年5月，这个叙事发生了根本性的转变。\n\n某外资投行在最新发布的研报中明确指出：行业的核心关切已经从“技术是否可行”切换到了“商业化能否规模化”。支撑这一判断的关键证据，来自波士顿动力（Boston Dynamics）与Figure AI在2026年5月中旬几乎同期释放的两个信号——前者展示了全电动Atlas在重载工业场景中的可部署性，后者则用连续六天的自主运行证明了人形机器人已经具备替代人类轮班作业的运营耐力。\n\n这两个事件揭示了一个更深的产业逻辑：人形机器人正在从“研发成本中心”转变为“可扩展的运营资产”。而在这条赛道上，最终胜出的将不是技术最炫的公司，而是那些能在“量产单位经济学”和“专有数据飞轮”两个维度上建立壁垒的企业。\n\n以下是我们从这份研报中提炼出的五个关键洞察，以及一个仍未完全解答的核心问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 波士顿动力证明：重载能力是当前人形机器人最被低估的竞争维度\n\n在5月18日的投资者演示中，波士顿动力展示了一个看似简单但意义重大的动作：Atlas利用全身控制（Whole-Body Control）抬起并搬运了一个23公斤的迷你冰箱。而在训练数据中，底层的强化学习模型已经成功扩展至处理45公斤的重量。\n\n这个数字的行业含义是什么？对比一下同类产品的有效载荷：特斯拉Optimus Gen-3的目标是20公斤，优必选Walker S2和宇树H2均为15公斤，Agility Digit为16公斤。Atlas的\n\n[... middle omitted ...]\n\n先受益”等话题，结合完整研报的图表与数据，进行更深入的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人形机器人，离我们究竟还有多远？\n\n2026年，人形机器人开始“上班”\n\n某外资投行最新研报指出，人形机器人行业已从“技术能不能行”切换到“商业怎么落地”阶段。5月中旬的两个关键事件，让整个逻辑发生了质变。\n\n1/ 波士顿动力：从“表演”到“生产力”\n- 新款Atlas把液压系统砍掉，只保留两种标准化的执行器。这意味着供应链简化、制造成本大幅下降。\n- 展示中，Atlas用全身控制搬运23kg的小冰箱，训练时能处理45kg的重量。这个载荷能力，让它能进工厂搬重物，而轻量级选手根本干不了。\n\n2/ Figure AI：用物流证明“能打”\n- 在宝马工厂连续11个月自主搬运价值9万美元以上的零部件，零人工干预。这个数据点直接证明：机器人可以当“正式工”了。\n- 产能从每天1台提升到每小时1台，年化产能超过1.2万台。转向汽车级压铸工艺后，单台成本在快速下降。\n- 物流仓储是近期最大市场：精度要求比汽车产线低，但量级巨大。比如某电商平台，用机器人替代人工，能压缩可变成本、锁定利润。\n\n3/ 关键对比：谁在领跑？\n- 载荷：波士顿动力50kg > Figure AI 20kg > 特斯拉20kg\n- 续航：特斯拉12\n\n[... middle omitted ...]\n\ns. Our key takeaway from the two events is clear: the industry is rapidly nearing deployment of humanoids at logistics and industrial sites, and the market is moving into a winner-take-all rac\n\n[... middle omitted ...]\n\n upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved."
  },
  {
    "id": "R027",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n这份来自某外资投行的专家电话会纪要，表面上是关于中国宏观经济韧性的一次常规更新。但如果你只读到“经济稳定”“政策支持”这些关键词，很可能错过真正重要的结构性信号。\n\n报告的核心判断可以浓缩为一句话：**中国大宗商品需求的底层逻辑正在切换，从“地产驱动的总量扩张”转向“新基建与能源转型驱动的结构性再分配”。** 这个切换的幅度、速度以及对不同品种的影响分化，才是当前资产定价中最容易被低估的变量。\n\n为什么现在重要？因为市场仍在用旧框架定价新周期。多数投资者的注意力还停留在“地产何时触底”“基建能否对冲”这类总量问题上，但报告揭示的图景是：即使总量增速平稳，需求的结构性迁移已经足以重塑铜、铝与钢铁的长期定价逻辑。如果你只盯着GDP数字，就会错过品种层面的巨大分化。\n\n这份报告提供了几个关键信号：政策层对地产的态度已从“托市”转向“稳而不举”；基建投资正在经历一轮“质变”而非“量变”；而真正驱动大宗商品长期需求的力量，正从钢筋水泥转向电网、AI基础设施与能源转型。下面我们逐一拆解这些信号背后的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 地产对大宗商品的拖累正在“钝化”，而非反转\n\n报告中最容易被误读的一句话是“房地产市场出现早期企稳迹象”。很多读者会本能地将其解读为“地产要复苏了，利好黑色系”。但仔细看，报告明确限定了条件：企稳仅体现在交易量和市场情绪上，且集中在核心城市。更重要的是，政策目标被清晰界定为“稳定而非再通胀”。\n\n这意味着什么？从大宗商品需求的角度看，地产的拖累正在从“急剧下滑”转为“低位钝化”。新开工面积持续低迷，但存量去库存和二手房交易成为政策重心，这对螺纹钢等建筑用材几乎不构成新增需求。真正值得关注的是“拖累的边际减弱”——即地产对大宗商品\n\n[... middle omitted ...]\n\n组织线上讨论，邀请行业专家和资深投资者一起拆解这些关键变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026中国经济韧性：地产筑底，新经济接力\n\n中国经济的底层逻辑正在切换\n\n**地产拖累减轻，但新引擎还没完全点火**\n\n某外资投行首席中国经济学家近期分享了对2026年宏观的判断，信息量很大。我拆成了几个关键点，方便理解。\n\n**1/ 宏观整体：韧性比想象中强**\n年初增长强劲，出口和国内需求都在改善。4月数据虽然有所放缓，但专家认为这更多是政策收紧的短期影响，而非结构性问题。中国政策传导通常很快，后续更多支持政策落地后，经济数据有望回升。\n\n**2/ 地产：最差的时候可能正在过去**\n- 成交量与市场情绪出现早期企稳信号\n- 但结构性挑战仍在：人口下降、低线城市库存高企\n- 复苏将是不均匀的，集中在头部城市\n- 政策目标是“托底”而非“刺激”，所以大宗商品需求短期内不会反弹\n- 好消息是：地产对经济的拖累正在减弱\n\n**3/ 基建与新经济：未来需求的主战场**\n- 基建投资预计比去年更强，尤其在新五年计划开局之年\n- 重点在“六网”建设：能源、电网、物流等，聚焦AI和国家安全\n- 商品需求正在从传统领域（建筑用钢）向新领域（铜、铝等新能源相关）转移\n- 需要注意：地方在执行层面面临“鼓励投资”与“限制债务\n\n[... middle omitted ...]\n\nlead to a recovery in economic data, given China's typically short policy lag. On commodity demand, we expect a continued structural shift away from traditional end use sectors (i.e. steel in \n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/1b4eb1938370344dbaa39107824c90f1768232bff438765a6a62c0d0bb00083f.jpg)"
  },
  {
    "id": "R028",
    "title": "油服行业的AI叙事被高估了：真正重要的不是技术本身，而是谁能把规模转化为议价权",
    "digest": "[wechat_article.md]\n# 油服行业的AI叙事被高估了：真正重要的不是技术本身，而是谁能把规模转化为议价权\n\n这份Bernstein研报发布于2026年5月，核心判断并非关于AI技术何时落地，而是关于一个更根本的结构性变化——地缘政治冲突正在重塑油服行业的优先级排序。AI不再是CEO们开会讨论的头号议题，取而代之的是供应安全和能源基础设施的增量建设。\n\n对于关注油服行业的投资者来说，这意味着一个关键的认知调整：市场正在用“AI概念”来定价油服公司，但行业自身的节奏和驱动力已经悄然转向。报告的核心洞察不是AI有多大的市场空间，而是“AI的叙事节奏与行业实际需求之间，正在出现一次显著的错位”。\n\n这份报告的价值不在于它预测了AI能带来多少亿美元的收入增量，而在于它揭示了一个被市场忽视的底层逻辑——油服行业的AI应用，本质上是“成本优化工具”而非“收入增长引擎”。这个判断如果成立，将直接颠覆许多投资者对油服公司估值逻辑的假设。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油服行业的AI落地，比市场预期的要晚至少两年\n\n报告最直接的判断是：油服行业的AI/数字化大规模采用，可能从2026-2027年推迟到2028-2029年。这不是技术本身的问题，而是行业优先级的变化。\n\n2025年12月，Bernstein团队曾判断油服行业即将进入AI/数字化的“追赶期”。但到了2026年5月，这个判断被修正了。原因很直接：2026年3-4月以来，中东冲突的升级让大型油服公司的CEO们把大量精力转向了与政府的沟通，而政府的优先事项已经急剧转向——从“如何用AI提高效率”变成了“如何确保能源供应的安全性和多样性”。\n\n这意味着什么？对于一家油服公司来说，CEO的时间是有限资源。当政府要求你优先讨论管道建设、产能扩张和供应链安全时，AI项目自然会被排到后面。这\n\n[... middle omitted ...]\n\nI增量贡献的详细估算。这些内容，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油服行业AI落地，比想象中晚一点\n\n**AI再等等**\n\n**油服行业的数字化，还在路上**\n\n最近翻到一份某外资投行关于油服行业AI的深度报告，信息密度很高，把核心逻辑拆给大家。\n\n先说一个有意思的洞察：油服行业对AI的探索其实很早。早在1979年，行业龙头SLB的CEO就在年报里提到了“人工智能”。但几十年过去，整个行业的AI落地进度，依然比大家想的要慢。\n\n报告的核心观点是：油服行业的AI/数字化拐点，可能会推迟到2028-2029年，而不是之前预期的2026-2027年。\n\n为什么推迟？主要原因是中东局势变化，各国政府的优先级转向了“能源供应安全”，而不是数字化升级。油服公司的CEO们最近都在忙着和政府谈产能建设，AI暂时不是头号议题。\n\n1️⃣ AI能带来什么价值？\n报告估算，AI每年能给油服行业带来约56亿美元的机会。其中：\n- 82%来自成本优化（约46亿美元）\n- 18%来自新增收入（约10亿美元）\n\n这个结构很说明问题——目前AI在油服行业的主要价值，还是“省钱”，而不是“赚钱”。\n\n2️⃣ 谁最受益？\n从细分领域看：\n- 油田服务公司（OFS）机会约33亿美元，其中23亿来自降本，10亿来\n\n[... middle omitted ...]\n\n.nguyen@bernsteinsg.com\n\n# Specialist Sales\n\n![](images/ea02d5553564d556c8559fb034c6c9438a97436552f333f15a8f70bd8e7e2ff6.jpg)\n\nGareth Williams\n\n+44 20 7762 5256\n\ngareth.b.williams@bernsteinsg.\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R029",
    "title": "AI 正在重塑中国软件业的定价权，但市场低估了“从 SaaS 到 RaaS”的深远影响",
    "digest": "[wechat_article.md]\n# AI 正在重塑中国软件业的定价权，但市场低估了“从 SaaS 到 RaaS”的深远影响\n\n过去一个月，某外资投行在深圳举办的中国投资会议上，与超过10家中国软件公司管理层进行了密集交流。会议传递的核心信号并非某个单一公司的业绩拐点，而是一个正在加速发生的行业结构性变化：软件价值的计量单位，正在从“账号数”转向“Token数”。这听起来像技术细节，但它对收入模型、竞争格局和利润结构的影响，可能比大多数投资者预期的更为深刻。\n\n这份研报解析并非要复述所有会议纪要，而是提炼出那些值得产业决策者和长期投资者认真对待的判断。其中最关键的一条是：AI 货币化正在从概念验证进入规模兑现期，但真正的投资机会不在于谁先喊出“AI”，而在于谁能把技术能力转化为可预测、可定价的经常性收入。\n\n以下是我们基于报告原文逻辑推导出的五个核心洞察，以及一个尚未被充分回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI 货币化正在从 ARPU 提升走向收入模型的重构，Token 计价是真正的变量\n\n报告中最具信号意义的变化，并非某家公司 AI 业务收入增长了多少，而是收入计量方式的转变。多家公司管理层明确提到，定价模式正从传统的按席位收费（seat-based），转向按使用量或 Token 收费（usage/token-based）。\n\n这不仅仅是定价策略的调整。从 SaaS（软件即服务）到 RaaS（结果即服务），意味着软件公司的收入从“订阅一个工具”变为“为每一次有效输出付费”。对于客户而言，这降低了前期投入门槛，但也让成本与使用价值直接挂钩。对于软件公司而言，这带来了 ARPU 的弹性——如果 AI 功能确实能提升效率，客户愿意为更频繁的使用支付更多。\n\n金蝶的 AI 原生产品合同价值在2026年第一季度已达2.3亿元\n\n[... middle omitted ...]\n\n里，我们会分享完整的研报原文、图表以及更深入的交叉验证分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n软件AI变现正在加速，逻辑比想象中清晰\n\nAI变现，进入加速期\n\n某外资投行在深圳办了一场软件行业峰会，和10多家公司聊完，核心感受是：AI变现不再是概念，而是正在发生的事。几个关键变化，值得认真看。\n\n1/ 收费模式变了：从“卖座位”到“卖结果”\n过去软件按人头收钱（seat-based），现在越来越多转向按用量、按Token收费。这意味着什么？用户用得越多，软件公司赚得越多，ARPU（每用户平均收入）有明确的上行空间。更关键的是，服务模式从SaaS（软件即服务）向RaaS（结果即服务）迁移——客户买的不是工具，是产出。\n\n2/ 谁在增长？谁还在挣扎？\n分化很明显。ERP（企业资源管理）、修图/设计工具这两类，增长可见度最高。AI带来的收入贡献在上升，订阅收入占比也在提高。但IT外包、网络安全、地产软件需求依然偏软。客户那边，央企（尤其是能源等关键基础设施领域）和大型民企需求扎实，政府相关客户还没恢复。\n\n3/ AI代码能力进步太快了\n某AI专家提到，AI编程能力提升很快，开发者效率大幅提高，软件开发成本在结构性下降。这对行业格局是重塑级的——大型软件厂商和灵活的小团队会成为赢家，中型软件公司反而面临转型压\n\n[... middle omitted ...]\n\ning a shift in software service models, transitioning from SaaS to RaaS; (3) demand trends are diverging: ERP / photo editing & design tools demonstrate better growth visibility, supported by \n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R030",
    "title": "市场真正低估的不是AI芯片，而是CPU的重新定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI芯片，而是CPU的重新定价\n\n过去两年，资本市场几乎将所有注意力集中在GPU和AI加速器上。每一轮大模型发布、每一笔算力采购、每一次数据中心capex上调，都被视为NVIDIA及其追随者的利好。CPU被默认视为“传统计算”的代名词，增长缓慢、份额被侵蚀、叙事平淡。\n\n但这份最新发布的投行研报提出了一个值得所有产业决策者和投资者重新审视的判断：到2030年，服务器CPU的潜在市场规模将从2025年的约293亿美元扩张至约1315亿美元，年复合增长率达到35%。更关键的是，驱动这一增长的引擎并非传统通用计算，而是一个几乎从零起步的新品类——Agentic CPU，其年复合增长率高达185%，到2030年将占据CPU总市场的45%。\n\n这一判断之所以重要，不仅因为它给出了一个比ARM和AMD自身预期都更为激进的TAM数字，更因为它揭示了当前市场定价中的一个结构性盲点：当所有人都在追逐AI训练和推理的算力需求时，支撑AI工作流协调、调度、安全与决策的CPU基础设施，正在成为下一个供不应求的环节。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及一个尚未被充分回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Agentic CPU不是概念炒作，而是AI基础设施的下一块拼图\n\n报告将CPU TAM拆分为三个部分：通用CPU、AI头节点CPU和Agentic CPU。其中，Agentic CPU是最大的变量，也是市场目前认知最不充分的领域。\n\n从数据看，2025年Agentic CPU的规模仅为约3亿美元，几乎可以忽略不计。但报告预计到2026年，这一数字将跃升至约100亿美元，到2030年达到约594亿美元。这意味着在五年内，Agentic CPU将从几乎零基础成长为一个超过通用CP\n\n[... middle omitted ...]\n\n交叉验证，帮助读者在信息过载中抓住真正影响定价的结构性变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPU市场要变天？2030年规模翻4倍\n\n服务器CPU的黄金时代\n\n某外资投行刚刚更新了服务器CPU的TAM模型，预测到2030年市场将从293亿扩大到1315亿美元，年复合增长35%。其中最大的变量是——Agentic CPU。\n\n1️⃣ Agentic CPU是什么？\n不是传统CPU，也不是AI加速器，而是专门运行AI agent应用的处理器。研报预测这部分将从2025年的3亿美元飙升至2030年的594亿美元，年复合增长185%。到2030年，它将占据整个CPU市场的45%。\n\n2️⃣ 传统CPU也在增长\n通用CPU预计以20%的复合增长率增长，到2030年达到509亿美元。AI head node（AI集群的管理节点）以21%增长，达到211亿美元。整体来看，CPU不仅没有被AI取代，反而在AI的带动下迎来新增长。\n\n3️⃣ 市场份额怎么变？\n- Intel：从61%下降到47%，但仍保持第一\n- AMD：从25%上升到34%，成为主要受益者\n- ARM：从14%上升到19%，但增速在放缓\n\n研报认为AMD是CPU复兴的最大受益者，主要因为：\n- 性能领先\n- 台积电产能保障\n- 拿下Anthropi\n\n[... middle omitted ...]\n\nieve the CPU TAM could expand from \\$29.3 billion in 2025 to \\$131.5 billion in 2030, or a 35% CAGR. We expect general purpose CPUs to grow at a 20% CAGR to \\$50.9 billion in 2030, AI head nod\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R031",
    "title": "机构持仓数据揭示的真正信号：AI投资从“押注赢家”转向“押注瓶颈”",
    "digest": "[wechat_article.md]\n# 机构持仓数据揭示的真正信号：AI投资从“押注赢家”转向“押注瓶颈”\n\n市场对大型科技股的讨论，长期集中在估值是否过高、盈利增长能否持续、以及AI货币化路径是否清晰。但一份基于1Q26 13-F持仓数据的研报，提供了一组更底层的信号：机构投资者的仓位配置，正在发生一次结构性的偏移——从追逐最大市值的AI赢家，转向重仓AI基础设施的“瓶颈环节”。\n\n截至1Q26末，Mega-cap科技股（NVDA、AAPL、MSFT、AMZN、GOOGL、META、TSLA）相对标普500的机构低配幅度，从4Q25的-137个基点收窄至-125个基点。这个12个基点的变化看似微小，但放在近一年的趋势中看，它标志着机构对大型科技股的“被动低配”正在被主动修正。更值得关注的是，低配的分布极度不均：NVDA、AAPL、MSFT依然是最被低配的个股，而存储与半导体设备领域的公司——SNDK、STX、LRCX、KLAC——却处于明显的超配状态。\n\n这份数据告诉我们一个判断：市场真正低估的不是AI需求，而是AI供给侧的再定价。机构资金正在用仓位投票，选出他们认为在未来12-18个月最具议价能力的环节。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 低配收窄不等于全面看多，真正的分歧在于谁被“主动选择”\n\n低配收窄12个基点，这个数字本身并不足以驱动行情。它的意义在于方向——机构正在从“系统性低配大型科技股”的状态中走出来，但这种修正是有选择性的。\n\n从个股层面看，NVDA的低配幅度仍高达-2.39%，位居所有大型科技股之首。AAPL（-2.32%）、MSFT（-1.86%）、AMZN（-1.24%）紧随其后。这些公司都是AI叙事中的核心标的，但机构的仓位配置并未完全反映其标普500权重。这背后可能有两个原因：一是部分主动管理基金仍然对估值保\n\n[... middle omitted ...]\n\n观察框架。期待与你一起，把这份报告的信号转化为更清晰的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 大机构悄悄加仓了哪些科技股\n\n**机构持仓风向变了**\n\n**从13F数据看科技龙头持仓变化**\n\n---\n\n刚读到某外资投行一份有意思的研报，追踪了1Q26大型科技股的机构持仓变化。几个关键发现和大家聊聊。\n\n**1️⃣ 科技巨头“被低估”的程度在缩小**\n\n截至1Q26，Mega-cap科技股（NVDA、AAPL、MSFT等）在机构主动管理组合中的占比，相比它们在标普500中的权重，平均低了125个基点。这个缺口比去年底的137个基点收窄了12个基点。\n\n简单说：机构正在慢慢补仓这些大票。\n\n**2️⃣ 谁是机构最“不爱”的？**\n\nNVDA仍然是最被低配的大型科技股，差距达-2.39%。紧随其后：\n- AAPL：-2.32%\n- MSFT：-1.86%\n- AMZN：-1.24%\n- GOOGL：-0.63%\n\n前五大科技巨头全部处于“欠配”状态。\n\n**3️⃣ 谁是机构最“偏爱”的？**\n\n最被超配的是SNDK，差距达+2.16%，是第二名STX（+0.84%）的两倍多。\n\n排在前面的还有：\n- CRM：+0.63%\n- LRCX：+0.52%\n- KLAC：+0.50%\n\n**4️⃣ 一个清晰的\n\n[... middle omitted ...]\n\np and S&P 500 weighting was +32bps, in-line with last quarter.   \nNVDA remains the most under-owned large-cap tech stock vs. S&P 500 at -2.39%, followed by AAPL (-2.32%), MSFT (-1.86%), and AM\n\n[... middle omitted ...]\n\n(03/14/2022)</td><td>$5.30</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$18.45</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$10.03</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R032",
    "title": "全球汽车投资者真正焦虑的不是销量，而是“中国车企的下一步”还能被定价吗",
    "digest": "[wechat_article.md]\n# 全球汽车投资者真正焦虑的不是销量，而是“中国车企的下一步”还能被定价吗\n\n过去两周，某外资投行全球汽车团队在欧洲与数十家机构投资者进行了密集沟通。结论清晰得有些令人不安：市场对中国汽车板块的情绪并非简单的“看多”或“看空”，而是一种结构性的、带有方向性选择的谨慎。投资者并不否认中国车企在电动化与智能化上的领先优势，但他们正在用脚投票——将资金从那些仅依赖国内销量和低利润率的传统车企中撤出，集中押注于三条能穿越周期的叙事：全球化执行能力、自动驾驶与物理AI、以及电池技术的差异化。\n\n这份报告最值得关注的判断，并非某个具体标的的评级调整，而是它揭示了一个正在发生的范式转移：中国汽车行业的估值中心，正在从“卖了多少辆车”转向“技术栈能在多大程度上跨越国界、进入全新市场”。对于产业决策者和长期投资者而言，忽视这一转变，将面临系统性风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口不再是选项，而是生存门槛——没有海外路径的车企将遭遇销量与利润的双杀\n\n报告中最具冲击力的数据之一，是中国乘用车及新能源车出口在2024年1-4月分别实现了约70%和120%的同比增长。这并非一个简单的增长信号，而是一个结构性分水岭：对于没有可信海外扩张路径的整车厂而言，国内市场内卷带来的价格压力与海外市场的缺失，将形成难以逆转的“剪刀差”——国内销量增长乏力，同时国内竞争导致的利润率收缩无法被海外利润弥补。\n\n但投资者需要警惕的是，欧洲的政策环境并非铁板一块。报告明确指出，欧盟内部尚未形成针对中国汽车进口的统一立场。这意味着，不同国家对中国车企的准入态度、关税水平、本地化要求将高度碎片化。对于中国车企而言，这既是风险，也是机会——那些能够驾驭国别政治、灵活调整本地化策略的企业，将获得非对称优势。\n\n报告特别提到，近岸/在岸建厂（on\n\n[... middle omitted ...]\n\n后续的产业链调研，持续探讨这些关键假设的验证节点和潜在拐点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球汽车投资人最近在想什么？\n\n📊 投研笔记：欧洲路演反馈\n\n上周跟着某外资投行去欧洲做了一圈路演，跟几十位全球汽车投资人聊完，发现大家的态度很微妙——不是不看好，是谨慎中带着明显的分化。\n\n1️⃣ 出口是唯一的增长引擎？\n今年1-4月中国乘用车和新能源车出口同比分别增长约70%和120%。没有海外布局的车企，面临销量和利润双杀的风险。但欧洲政策还没统一，对中国汽车进口的态度碎片化，能搞定国家层面关税和监管的公司才有机会。近岸/在岸化建厂是战略必然，比如某欧洲车企收购中国工厂的进展，大家都在盯。\n\n2️⃣ 物理AI和机器人成了新主线\n欧洲投资人没美国那么狂热，但也在往物理AI方向转。汽车公司正把现金流投到人形机器人和自动驾驶上，想靠这个逻辑重估估值。硬件、感知、移动能力这些老本行，反而成了讲机器人故事的核心资产。传统车企的低估值魔咒，可能要靠这个来打破。\n\n3️⃣ 具体谁被关注？\n- BYD：出口和电池的标杆，但短期国内销量承压，股价可能横盘到明年上半年。20倍以上的估值需要海外出货和国内复苏双重验证。\n- 小鹏：被看作中国版的“物理AI+机器人”标的，跟现代波士顿动力的讨论一起升温。\n- 蔚来：年内涨了15\n\n[... middle omitted ...]\n\nutious, weighed by concerns over weak China demand and legacy OEM vulnerabilities globally. Investors are broadly rotating capital toward long-duration growth stories backed by structural indu\n\n[... middle omitted ...]\n\nd><td>O (11/19/2024)</td><td>US$7.14</td></tr><tr><td>XPeng Inc. (9868.HK)</td><td>O (11/16/2021)</td><td>HK$60.65</td></tr><tr><td>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$15.62</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R033",
    "title": "日本电子元器件：市场低估的不是AI需求，而是北美智能手机高附加值部件的重新定价",
    "digest": "[wechat_article.md]\n# 日本电子元器件：市场低估的不是AI需求，而是北美智能手机高附加值部件的重新定价\n\n过去六个月，全球资本市场对电子元器件板块的关注几乎全部集中在AI服务器、数据中心和算力基础设施上。逻辑很简单：AI是结构性增长，智能手机是周期性成熟市场。但一份来自某外资投行日本团队的深度研报，提出了一个值得所有产业决策者重新审视的判断——在F3/27财年，北美智能手机高附加值元器件的供应商，其盈利将系统性超出市场预期。\n\n这不仅仅是“手机周期复苏”的老调重弹。报告的核心逻辑建立在两个被市场低估的变量之上：一是北美旗舰机型正在经历一轮“功能升级驱动的价值密度提升”，而非简单的出货量增长；二是日本元器件厂商在MLCC、摄像头致动器、连接器、HDD相关产品等细分赛道上，正在将技术壁垒转化为不可逆的议价权。\n\n本文基于该研报的核心框架，提炼出五个关键洞察，并指出报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对北美智能手机的定价模型，忽略了“价值升级”而非“数量增长”的盈利弹性\n\n大多数投资者对智能手机供应链的估值框架，仍然建立在出货量同比增速的线性外推上。但这份报告的核心贡献之一，是指出北美某头部品牌正在经历一轮“单位价值含量”的显著提升。具体而言，高端机型中MLCC的单机用量、性能等级和单价均在上升，摄像头模组从硬件规格竞争转向致动器精度竞争，连接器从通用型向高速、小型化、耐高温方向迁移。\n\n报告对村田制作所（Murata）给出了Overweight评级，核心论据正是“高附加值MLCC的需求增长和产能利用率提升”。这不是简单的补库存逻辑。当市场还在讨论智能手机整体出货量是否见顶时，报告揭示的是：即便出货量持平，单机中高价值元器件的价值占比也在扩大。这意味着，传统以出货量为自变量的盈利预测模型，可能系\n\n[... middle omitted ...]\n\n产能爬坡假设和客户集中度分析，进一步拆解这些未解问题的答案。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本电子零件，新一轮机会在哪\n\n北美手机零件+AI算力\n\n最近在看某外资投行关于日本电子零件板块的报告，核心逻辑很清晰——北美高端智能手机零件和AI算力是两大主线。📱\n\n研报认为，到F3/27年，北美智能手机高附加值零件供应商的盈利有望超过市场预期，叠加AI算力设备普及，整个板块正迎来新一轮增长周期。\n\n1️⃣ TDK（首选标的）\n可充电电池和HDD相关产品盈利扩张，被列为最看好的公司。\n\n2️⃣ 村田制作所（Murata）\n高附加值MLCC（积层陶瓷电容）需求增长，产能利用率持续提升，盈利改善空间大。\n\n3️⃣ 阿尔卑斯阿尔派（Alps Alpine）\n高性能摄像头致动器预计4-6月开始放量，新智能手机摄像头零件将成为盈利贡献点。\n\n4️⃣ 日本特殊陶业（Niterra）\n替换火花塞和SPE静电卡盘业务盈利持续增长，汽车后市场需求稳定。\n\n5️⃣ 广濑电机（Hirose Electric）\n一般工业机械和AI服务器连接器业务盈利扩张，AI基础设施建设带动需求。\n\n🔍 核心逻辑：\n- AI算力设备渗透率提升，带动MLCC、连接器、PCB等核心零件需求\n- 北美高端手机供应链升级，高附加值零件供应商受益\n- 日\n\n[... middle omitted ...]\n\nors to ramp up from Apr-Jun.   \n■ OW on Niterra: Continued earnings growth for replacement plugs and SPE electrostatic chucks.   \n■ OW on Hirose Electric: Earnings expansion for general indust\n\n[... middle omitted ...]\n\n10/2021)</td><td>¥2,872</td></tr><tr><td>Nihon Dempa Kogyo (6779.T)</td><td>E (03/07/2024)</td><td>¥2,342</td></tr><tr><td>Nippon Chemi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥2,944</td></tr></table>\n\n© 2026 MS MUFG"
  },
  {
    "id": "R034",
    "title": "记忆体行业的“结构性契约”正在改写周期的定价逻辑",
    "digest": "[wechat_article.md]\n# 记忆体行业的“结构性契约”正在改写周期的定价逻辑\n\n市场对AI基础设施的讨论，大多集中在GPU算力、网络带宽和电力消耗上。但一个更深层的结构性变化正在发生，它可能比任何单一芯片的迭代都更能重塑半导体投资的底层逻辑：记忆体（Memory）的合约模式正在从“随行就市的现货博弈”转向“锁定3-5年的长期战略联盟”。\n\n这份来自某外资投行的研报，核心判断并非记忆体需求有多强劲——这已是共识——而是供给侧的合约结构发生了不可逆的质变。这种质变的结果是，记忆体公司的盈利可见性、现金流质量和估值倍数，都可能经历一次系统性的重估。市场目前对此的定价，可能仍停留在“周期股”的旧框架里。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 长期协议不再是“君子协定”，而是带有财务担保的硬约束\n\n过去半导体景气周期中，长期协议（LTA）并不罕见。但那些协议往往约束力薄弱，更像是基于信任的意向书，一旦市场转弱，客户可以轻易推迟或取消订单，供应商几乎没有追索权。\n\n当前这一轮LTA，性质完全不同。根据研报中引用的产业链信息，新协议的期限普遍拉长至3-5年，且包含了预付款、价格区间、利润保护等机制。更关键的是，这些协议很可能是“不可取消、不可退款”的。有供应商在财报电话会上透露，客户通过“数十亿美元的金融工具”作为抵押，一旦未能履行每季度的采购承诺，这些抵押将直接转为对供应商的补偿。\n\n这意味着什么？过去记忆体公司的产能扩张，很大程度上是在赌未来的市场需求。现在，扩张的资本开支直接对应的是已被确认的、不可撤销的客户订单。这消除了库存风险，也让供应商的产能规划从“猜测”变成了“执行”。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 一个被低估的结构性变化：记忆体正从“大宗商品”变为“定制化基础设施”\n\n[... middle omitted ...]\n\n的完整图表和测算，一起拆解那些尚未被市场充分定价的二阶影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片长协正在改写行业逻辑\n\n🔒 长协重构芯片行业\n\n最近某外资投行出了一篇深度研报，核心观点：存储芯片市场正在经历结构性转变——长期协议（LTA）正在改变这个过去以周期波动闻名的行业。\n\n1/ 长协不一样了\n过去的长协约束力弱，基本是“软性承诺”。但现在的3-5年长协包含预付款、定价机制、利润保护条款。有些客户甚至为2027年需求预付50%，为2028年预付100%。这些协议大概率不可取消、不可退款，是真正的“保险”。\n\n2/ 周期变平了\n长协锁定未来供应和价格，给存储公司带来收入可见性和利润保护。即使产能扩张导致供给过剩，已签约的量价也能缓冲冲击。产能投资不再基于预测，而是基于超大规模客户的确定需求。\n\n3/ 客户行为变了\n超大规模云服务商不再“机会性”采购，而是通过长协保障AI基建的供应。三星、SK海力士、美光、闪迪都在签这类协议。闪迪CEO说客户“通过金融工具提供数十亿美元抵押”，如果季度采购不达标，赔偿立刻生效。\n\n4/ 估值可能重估\n研报将SK海力士2026-2028年EPS预期上调6%/3%/14%，目标价从170万韩元升至260万韩元。逻辑是：长协降低周期性，提升自由现金流可见性，可以支撑更高股\n\n[... middle omitted ...]\n\nts are being contracted through long-term agreements (LTA) of 3-5 years:\n\nThese have existed during semiconductor booms, but recent LTAs differ from past ones with weak binding power. They may\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R035",
    "title": "欧洲中小盘股的真正机会，藏在管理层问答的缝隙里",
    "digest": "[wechat_article.md]\n# 欧洲中小盘股的真正机会，藏在管理层问答的缝隙里\n\n市场对欧洲中小盘股的关注，往往集中在宏观叙事和行业轮动上。但一份来自某外资投行的研报，提供了一个截然不同的视角：它不急于给出结论，而是精心准备了10个问题，让投资者带着这些框架去与管理层对话。这份报告的核心判断是——**当前欧洲中小盘股的价值重估，并不取决于宏观数据的回暖，而取决于企业能否在细分赛道上证明自己的议价能力和战略执行力。**\n\n为什么这个判断现在重要？因为过去两年，欧洲中小盘股经历了估值压缩和盈利下修的双重打击。市场已经充分定价了宏观逆风。但正如这份报告所暗示的，真正区分“赢家”和“输家”的，不再是行业贝塔，而是企业自身的阿尔法。报告通过对45家覆盖公司的管理层提问，揭示了一个尚未被市场充分定价的结构性变化：在半导体设备、国防、能源转型和医疗科技等特定领域，一批中小盘公司正在建立难以复制的竞争壁垒，而它们的估值却仍停留在周期股的水平。\n\n这份报告提供的不是一份简单的“买入清单”，而是一套用来识别这种结构变化的提问框架。以下是我们从报告中提炼出的五个关键洞察，以及它们对投资决策的含意。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 半导体设备复苏的“二阶效应”被低估，但需验证其可持续性\n\n报告中对Aalberts、Melexis、X-Fab等半导体相关公司的提问，指向了一个共同的关切：市场是否低估了半导体设备复苏带来的“二阶效应”。例如，对Aalberts的提问明确聚焦于“半导体设备后端和东南亚市场的商业与运营协同效应”，以及对Melexis的提问则关注“汽车半导体内容增长是否正在加速”。这些问题的潜台词是：半导体设备的复苏不仅仅是周期性的补库存，而是由AI、电动汽车和工业自动化驱动的结构性需求扩张。\n\n但报告也留下了关键悬疑。对X-Fab的提问显示\n\n[... middle omitted ...]\n\n球微信群里继续讨论，我们将分享完整报告的解读和更多独家分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲中小盘投研：管理层最关心的10个问题\n\n中小盘研究，问对问题比什么都重要\n\n某外资投行在尼斯SMID大会前，整理了一份“提问清单”，覆盖了参会公司的管理层最可能被追问的方向。我拆了几家公司的核心逻辑，发现其实问题框架是通用的。\n\n🧠 核心观察：\n这次大会覆盖了工业、科技、医疗、消费等多个赛道，但管理层被问得最多的问题，集中在5个维度：\n\n1️⃣ 增长能见度\n- 短期订单和业绩指引是否可靠？\n- 比如Aalberts被追问：半导体设备复苏在2H到底多确定？2027年更强的信心来自哪些假设？\n- 很多管理层对2026-2027的成长路径其实有分歧，关键在于“自发性增长”vs“并购驱动”的比例。\n\n2️⃣ 利润率改善的路径\n- 是靠量（收入增长）还是靠价（成本削减/效率提升）？\n- 比如Aalberts的margin提升，有多少来自半导体复苏的量，多少来自内部优化？\n- 很多公司面对“如果法国/德国住宅市场继续弱，利润率会怎样”这类压力测试。\n\n3️⃣ 资本配置与并购策略\n- 分红、回购、并购的优先级怎么排？\n- 比如Aalberts被问到：未来会不会更系统地做回购？剩余资产剥离计划的时间表？\n- 这其实是判断\n\n[... middle omitted ...]\n\nfe29c228e5672e1888566546df2286e47.jpg)\n\n# Delphine Le Louet\n\n+33 1 42 13 92 93\n\ndelphine.le-louet@bernsteinsg.com\n\n![](images/92d2261423ac53f83f1ef05fa55503abff341b496900df30981da442cbe4d139.j\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R036",
    "title": "市场真正低估的不是光模块，而是光学引擎的渗透率跃迁",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是光模块，而是光学引擎的渗透率跃迁\n\n当大多数人还在讨论光模块的出货量增速时，一份来自某外资投行的研报提出了一个更为根本的判断：AI数据中心的光学架构正在经历一次从“铜线为主、光学为辅”到“光学全面介入”的范式转换。这个转换的核心，不是光模块数量的线性增长，而是光学引擎（Optical Engine）每GPU附着率的非线性跃迁——从今天的2-4个，跃升至NVL576架构下的17个，再到全光架构下的35个以上。\n\n这份报告上调了Soitec和Besi两家欧洲半导体公司的目标价，幅度之大令人侧目：Soitec从70欧元上调至200欧元，Besi从200欧元上调至300欧元。但真正值得产业决策者关注的，不是目标价本身，而是支撑这一判断的底层逻辑——当AI集群从单机架扩展到多机架，铜线物理极限迫使光学渗透加速，这不仅仅是供应链的重新分配，而是整个数据中心互联架构的价值重估。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及一个尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. NVL576是一个分水岭：它第一次把光学推进了“scale-up”域\n\n理解这次变化的起点，是区分AI数据中心中的两种网络流量。scale-out网络负责连接不同GPU集群之间的通信，今天已经大量采用光学互联；而scale-up网络负责同一集群内GPU之间的高速协同，至今仍以铜线为主。NVL72之所以能在单机架内完成72颗GPU的紧密耦合，靠的就是铜线在短距离内的高效传输。\n\n但NVL576的出现改变了游戏规则。当GPU集群从单机架扩展到多机架，铜线的距离极限（约2米）被突破，机架之间的连接必须转向光学。这是光学第一次进入scale-up域，也意味着一个全新的增量市场被打开。\n\n报告引用Corning投资者\n\n[... middle omitted ...]\n\n和Besi的估值锚点，以及如何从产业链交叉验证中寻找预期差。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心正在经历一场“光进铜退”的升级，而两家欧洲半导体公司正站在这个趋势的C位。\n\n光进铜退，这俩公司站C位\n\nCPO给Soitec和Besi带来的机会\n\n最近看了份某外资投行的研报，把AI数据中心从铜线切换到光通信的逻辑讲得很透。简单说，AI集群越做越大，GPU之间的数据传输距离变长，铜线扛不住了，光通信（CPO，共封装光学）就成了必然选择。这里有两个关键受益方：\n\n1️⃣ **Soitec：光芯片的“地基”供应商**\n   - Soitec的核心产品是光子学SOI晶圆，专门用来制造光子集成电路（PIC），也就是光引擎的核心部件。\n   - 以前每个GPU只需要2-4个光引擎，主要用在机柜间的网络连接。\n   - 但到了NVL576这种多机柜架构，光引擎的用量会飙升到每个GPU大约17个。如果未来实现全光互联，这个数字会超过35个，甚至可能到70个。\n   - 研报大幅上调了Soitec的预期：到2028年，仅AI数据中心的光子学SOI收入就可能达到4.68亿美元，目标价从70欧元直接提到了200欧元。\n\n2️⃣ **Besi：封装环节的“粘合剂”**\n   - 光引擎需要把电子芯片（EIC）和光子芯片（\n\n[... middle omitted ...]\n\n, resulting in material PT increases for both.\n\n# Key Takeaways\n\n■ Agentic systems increase the need for high bandwidth, low latency communication in the AI datacenter which may accelerate the\n\n[... middle omitted ...]\n\n>E (02/10/2025)</td><td>NKr 201.20</td></tr><tr><td>Soitec SA (SOIT.PA)</td><td>O (03/26/2026)</td><td>€140.25</td></tr><tr><td>VAT Group AG (VACN.S)</td><td>E (03/21/2025)</td><td>SFr 586.80</td></tr></table>\n\n© 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Fed balance sheet liabilities (\\$tn) Currency, reserves, and TGA make up the largest shares of the Fed's liabilities"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Stylized Fed reserve demand and supply curves if reserve demand curve shifts left. If reserve demand curve shifts left due to de-reg, it will place downward pressure on funding rates"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Stylized Fed reserve demand and supply curves if reserve demand curve shifts left and Fed reduces supply of reserves"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 5: Fed WAM and WAM projection scenarios (months) Fed WAM has already started to decline due to RMPs and MBS reinvestments into T-bills but shifting coupon reinvestments into short-dated tenors would speed up this decline"
  },
  {
    "figure_id": "F005",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Curve-o-meter Rates to trade like positioning is modestly short & in flattener; residual out of the money longs continue to bias rates to selloff"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: 2y contract CTA positioning across different lookback models All lookback models suggest CTAs are short 2y"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: 30y contract CTA positioning across different lookback models All lookback models suggest CTAs are short 30y"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: 5y percentile of 10 equivalent duration positioning (percentile: higher = longer) Futures proxy shows longs are still out of the money, funds are underweight, our top down 10y momentum figure suggests modest CTA shorts"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 5y percentile of curve positioning (percentile: higher = longer back-end relative to front end) Futures proxy skewed flatter; fund regression still relatively neutral while CTAs regression implies steepener"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Asset manager and leveraged fund positioning (10y equivalent, \\$bn) Asset manager longs correspond with leveraged fund shorts"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Asset manager futures positioning in 10y equivalents (\\$bn) More longs in TU-TY vs UXY – WN but deviation is narrowing"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Decomposition of 1w change in asset manager open interest (10y equivalent, \\$bn) More AM shorts created last week; significant new longs created at WN only"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Proxies for futures positioning (\\$mil '01, duration-weighted by contract) In the money positions are predominantly shorts with some long out of the money in TY and WN points of the curve"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: CTA positioning in 10yT Momentum suggests longs reduced at 10y point; Betas imply shorter than momentum"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Decomposition of 4w change in asset manager open interest (10y equivalent, \\$bn) Last 4w positioning stays mixed with more new vs covered positions"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Analysis of proxies for futures positioning Futures proxy implies most of curve to selloff"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Exhibit 14",
    "context": "Exhibit 14: CTA positioning in 2y vs 10y UST Top-down model shows CTAs are taking more underweight risk at 10y"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Changes in CTA 10yT beta Beta increased modestly on the week"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "Exhibit 16",
    "context": "BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 17",
    "context": "Exhibit 17: UST supply versus sources of demand (\\$bn) Demand in Q4 was weaker relative to Q3 despite similar supply"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Change in UST holdings (\\$bn) Much of growth in household holdings likely driven by hedge funds"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Hedge fund cash UST holdings vs leveraged HF shorts (\\$bn) Form PF data shows growth in cash UST since 2022, short futures position picked up since drop in Q4 2024"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Exhibit 20",
    "context": "Exhibit 20: FX hedged pickup of TSYs versus local alternatives implied by forwards Market pricing suggests relatively negative pickup for major foreign investor types BofA GLOBAL RESEARCH Exhibit 21: 10Y UST pickup to 20Y JGB, wit"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Exhibit 20",
    "context": "Exhibit 20: FX hedged pickup of TSYs versus local alternatives implied by forwards Market pricing suggests relatively negative pickup for major foreign investor types BofA GLOBAL RESEARCH Exhibit 21: 10Y UST pickup to 20Y JGB, wit"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 22",
    "context": "Exhibit 22: 10Y UST pickup to 10Y JGB, with 3m FX hedge (bps) 10y TSY offers negative hedged pickup versus 10y JGBs"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Exhibit 23",
    "context": "Exhibit 23: 10Y UST pickup to 10Y Bund, with 3m FX hedge (bps) 10y TSY hedged pickup still negative versus 10y Bund"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Exhibit 24",
    "context": "Exhibit 24: 10Y UST pickup to 10Y CAD govie, with 3m FX hedge (bps) 10y TSY hedged pickup increasingly negative versus 10y CAD gov bond"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Exhibit 25",
    "context": "Exhibit 25: 10Y UST pickup to 10Y Gilt, with 3m FX hedge (bps) 10y TSY offers negative pickup versus gilts"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Japan investment in foreign bonds, cumulative weekly (\\$bn) Long & medium term bonds holdings rose \\$10bn on the week"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Cumulative UST flows from foreign investors (\\$bn) UK has been large buyer since '21"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Cumulative UST flows from foreign investors (\\$bn) Foreign holdings increased in February"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Weekly UST custody holdings, foreign official (\\$bn) Custody holdings declined \\$24bn on the week"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Largest MoM changes in foreign TSY holdings (\\$bn) Japan, UK biggest buyers; Canada & China + Belgium biggest sellers"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Cumulative change in Japanese investor holdings of USTs Higher foreign private buying vs combined private & official Japanese holdings of UST"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Japanese deposits with other central banks and Fed foreign repo pool (\\$bn) Vast majority of \\$162bn in MoF deposits likely at Fed's foreign repo pool"
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Monthly change in Japanese investor foreign bond holdings (\\$USD, bn) Mar saw selling from pensions, lifers, and banks"
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Cumulative change in custody holdings and foreign RRP UST securities held in custody are typically negatively correlated with foreign RRP take-up but we have seen some divergence since July '25"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Cumulative change in Japanese investor foreign bond holdings (\\$USD, bn) Pension holdings have increased in recent months"
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Sovereign fund inflows by year (\\$bn) 2025 inflows rose steadily over the year; 2026 inflows greater than last year"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Sovereign fund inflows by year (\\$bn) Short-term inflows were strong at the start of 2025 but slowed since April"
  },
  {
    "figure_id": "F041",
    "report_id": "R003",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Total return funds, excess return vs. 10y rate Weekly asset-weighted total returns for total return funds. Funds return in line with benchmark on the week"
  },
  {
    "figure_id": "F042",
    "report_id": "R003",
    "label": "Exhibit 43",
    "context": "Exhibit 43: UST beta from PCA regression (z-score) Betas suggest funds are underweight benchmark duration; lower beta = funds' underweight duration versus benchmark"
  },
  {
    "figure_id": "F043",
    "report_id": "R003",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Curve beta from PCA regression (z-score) Betas suggest funds are likely positioning for steepeners; higher beta = funds positioning for steepeners versus benchmark"
  },
  {
    "figure_id": "F044",
    "report_id": "R003",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Cumulative return of TR FI funds over benchmark vs 10yT Funds have modestly outperformed in recent months"
  },
  {
    "figure_id": "F045",
    "report_id": "R003",
    "label": "Exhibit 44",
    "context": "Exhibit 44: WoW change in UST beta from PCA regression Funds' duration declined modestly on the week"
  },
  {
    "figure_id": "F046",
    "report_id": "R003",
    "label": "Exhibit 46",
    "context": "Exhibit 46: WoW change in curve beta from PCA regression Curve bias little changed on the week"
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "Exhibit 47",
    "context": "Exhibit 47: MBS beta from PCA regression (z-score) Betas suggest funds are overweight MBS; higher beta = funds overweight MBS versus benchmark"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Exhibit 48",
    "context": "Exhibit 48: IG beta from PCA regression (z-score) Betas suggest funds have added IG risk vs benchmark; lower beta = funds underweight IG versus benchmark"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Bloomberg US Aggregate Bond Fund – Treasury share through time US Treasury's share at 46% on the week"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Bloomberg US Aggregate Bond Fund – MBS and Corporate share through time US corporate and MBS shares have slowly trended lower"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "Exhibit 53",
    "context": "Exhibit 53: YoY change in securities, loans, and deposits Securities growth usually only positive when deposit growth is positive"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "Exhibit 55",
    "context": "Exhibit 55: 3m5y curve (bps) & YoY securities growth Securities portfolios tend to grow when curve is upward sloping"
  },
  {
    "figure_id": "F053",
    "report_id": "R003",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Domestic bank holdings of UST& Agy, MBS (\\$bn) Domestic banks' UST & AGY holdings have seen a faster pace of increase in recent months while MBS has been relatively flat"
  },
  {
    "figure_id": "F054",
    "report_id": "R003",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Cumulative change in domestic bank holdings of UST & Agency, MBS (\\$bn) Domestic bank UST & AGY holdings are notably higher vs MBS since Feb '25"
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Dealers WoW change in positions Holdings have increased notably at long end across cash & futures"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Dealers change in positions over last 6 months Long-end futures holdings have increased meaningfully"
  },
  {
    "figure_id": "F057",
    "report_id": "R003",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Dealers total sector positions 10y equivalent, \\$bn, short futures positions coincide with long Treasury security holdings."
  },
  {
    "figure_id": "F058",
    "report_id": "R003",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Primary dealer – average auction allotment Dealer participation remains low"
  },
  {
    "figure_id": "F059",
    "report_id": "R003",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Avg foreign investment at auction (all nominal coupons) Foreign participation increased modestly"
  },
  {
    "figure_id": "F060",
    "report_id": "R003",
    "label": "Exhibit 62",
    "context": "Exhibit 62: Investment fund – average auction allotment Fund participation remains elevated"
  },
  {
    "figure_id": "F061",
    "report_id": "R003",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Depository institutions – average auction allotment Depository participation is lower"
  },
  {
    "figure_id": "F062",
    "report_id": "R003",
    "label": "Exhibit 65",
    "context": "Exhibit 65: DB private pension fixed income allocation from Flow of Funds and smaller Milliman subset Milliman funds have higher fixed income share of assets vs broader private DB pension funds according to FoF"
  },
  {
    "figure_id": "F063",
    "report_id": "R003",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Milliman index and 12-month increase in USTs held in stripped form Stripping activity has moderated from end '24 peak while Milliman funds are still well funded"
  },
  {
    "figure_id": "F064",
    "report_id": "R003",
    "label": "Exhibit 69",
    "context": "Exhibit 69: UST holdings of private DB pensions and funded status When funded status is higher, pension funds buy more USTs"
  },
  {
    "figure_id": "F065",
    "report_id": "R003",
    "label": "Exhibit 66",
    "context": "Exhibit 66: 10y UST yield and Milliman pension funded index Funded status historically improves with an increase in interest rates"
  },
  {
    "figure_id": "F066",
    "report_id": "R003",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Change in USTs held in stripped form (\\$bn) UST stripping activity below average in April"
  },
  {
    "figure_id": "F067",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "Figure 1: Real/nominal GDP (level)"
  },
  {
    "figure_id": "F068",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "Figure 2: Actual vs forecast Figure 3: Real/nominal GDP (q/q, saar)"
  },
  {
    "figure_id": "F069",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "Figure 4: Real/nominal GDP (y/y)"
  },
  {
    "figure_id": "F070",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "Figure 5: Quarterly contribution (q/q, saar)"
  },
  {
    "figure_id": "F071",
    "report_id": "R005",
    "label": "Figure 6",
    "context": "Figure 6: Domestic demand was flat %q/q, saar"
  },
  {
    "figure_id": "F072",
    "report_id": "R005",
    "label": "Figure 7",
    "context": "Figure 7: Private consumption rose 0.3%q/q, better than our expectation (0.1%)"
  },
  {
    "figure_id": "F073",
    "report_id": "R005",
    "label": "Figure 8",
    "context": "Figure 8: Consumption of both goods and services"
  },
  {
    "figure_id": "F074",
    "report_id": "R005",
    "label": "Figure 9",
    "context": "Figure 9: Breakdown of private consumption (%y/y)"
  },
  {
    "figure_id": "F075",
    "report_id": "R005",
    "label": "Figure 10",
    "context": "Figure 10: Inbound consumption fell by $0.6\\% \\mathrm{q} / \\mathrm{q}$"
  },
  {
    "figure_id": "F076",
    "report_id": "R005",
    "label": "Figure 11",
    "context": "Figure 11: Contribution of inbound consumption to real GDP growth (y/y)"
  },
  {
    "figure_id": "F077",
    "report_id": "R005",
    "label": "Figure 12",
    "context": "Figure 12: Residential investment showed an rebound but not back to the previous level"
  },
  {
    "figure_id": "F078",
    "report_id": "R005",
    "label": "Figure 13",
    "context": "Figure 13: Capex rose $0.3\\% \\mathrm{q} / \\mathrm{q}$ , steadily rising"
  },
  {
    "figure_id": "F079",
    "report_id": "R005",
    "label": "Figure 14",
    "context": "Figure 14: Both public consumption and investment rose $0.4\\% \\mathrm{q / q}$ and $-0.2\\%$ respectively"
  },
  {
    "figure_id": "F080",
    "report_id": "R005",
    "label": "Figure 15",
    "context": "Figure 15: Exports of goods rebounded supported by auto related and capital goods (2.2%q/q vs 0.4% in services)"
  },
  {
    "figure_id": "F081",
    "report_id": "R005",
    "label": "Figure 16",
    "context": "Figure 16: Breakdown of service exports growth"
  },
  {
    "figure_id": "F082",
    "report_id": "R005",
    "label": "Figure 17",
    "context": "Figure 17: Both imports of goods and services rose $0.4\\%$ q/q and $0.8\\%$ respectively."
  },
  {
    "figure_id": "F083",
    "report_id": "R005",
    "label": "Figure 18",
    "context": "Figure 18: Nominal households consumption, disposable income and saving rate"
  },
  {
    "figure_id": "F084",
    "report_id": "R005",
    "label": "Figure 19",
    "context": "Figure 19: Compensation of employees in national account rose $3.4\\%$ YoY mainly due to wage growth"
  },
  {
    "figure_id": "F085",
    "report_id": "R005",
    "label": "Figure 20",
    "context": "Figure 20: Real compensation of employees rose $1.3\\%$ YoY, highest since Q3 2026"
  },
  {
    "figure_id": "F086",
    "report_id": "R005",
    "label": "Figure 21",
    "context": "Figure 21: Term of trade starts to worsen"
  },
  {
    "figure_id": "F087",
    "report_id": "R005",
    "label": "Figure 23",
    "context": "Figure 23: In 2022, the negative impact of higher oil prices on real disposable income was more than offset by a decline in the savings rate, keeping consumption on an upward trend."
  },
  {
    "figure_id": "F088",
    "report_id": "R005",
    "label": "Figure 24",
    "context": "Figure 24: The savings rate, which was relatively high in 2022, has recently turned negative, leaving limited room for further decline to support consumption"
  },
  {
    "figure_id": "F089",
    "report_id": "R007",
    "label": "Exhibit 7",
    "context": "Exhibit 2: Latest\\* stress across GFSI sub-components Crude implied vol is the most stressed while Govt-OIS EUR is the least stressed"
  },
  {
    "figure_id": "F090",
    "report_id": "R007",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Change\\*\\* in stress across GFSI sub-components Interest rate implied vol EUR was the largest stress riser over the last week while volume flow stress fell the most"
  },
  {
    "figure_id": "F091",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Commodity stress increased the most last week On the other hand, credit stress decreased"
  },
  {
    "figure_id": "F092",
    "report_id": "R007",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Top 10 biggest stress movers (vs history) Copper implied vol saw a historically large stress increase %-ile of abschg in stress vs history*"
  },
  {
    "figure_id": "F093",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 5: EM led regional stress higher last week In contrast, US stress declined"
  },
  {
    "figure_id": "F094",
    "report_id": "R007",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Biggest stress movers in cross-asset vols and spreads Rates vol experienced the largest increase in stress last week"
  },
  {
    "figure_id": "F095",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Bubble-like instability in global equities (MSCI World) broadly continues to rise, led by the BRIs of Kospi, Nikkei and US tech (though Mag7 still appears subdued); persistent geopolitical stress understandably keeps the"
  },
  {
    "figure_id": "F096",
    "report_id": "R007",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Taiwan, quantum and semis stocks are showing relatively high bubble-like dynamics among popular equity themes Highest BRI readings across popular equity themes (as of 15-May-26)"
  },
  {
    "figure_id": "F097",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 10: Solar & quality factor stocks have seen the biggest jump in their BRI over the past week among popular equity themes Largest 1w changes in BRI across popular equity themes (as of 15-May-26)"
  },
  {
    "figure_id": "F098",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 11: While the number of stocks exhibiting frothy price action has risen meaningfully, it remains localized vs Dotcom bubble peaks # of SPX stocks with BRIs above 0.8"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 12: The total index weight of SPX stocks exhibiting frothy behaviour has risen significantly over the past week Total weight of SPX stocks with BRIs above 0.8"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 13: Tech stocks like CSCO, INTC, DELL and PANW rank highest in terms of their Bubble Risk Indicators amongst S&P 500 members, with 16/25 of the top BRI stocks being in the tech space S&P 500 member stocks with highest BRI re"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Unlike TLT skew, which has reached extreme steepness towards the put side, US equity vol skews are broadly looking through macro concerns, pricing in resilience and greater call side risks in the near-term 1m 25d/ATMf pu"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Bubble-like regimes can withstand rising yields, as seen from the strong Nasdaq rally in the latter stages of the Dotcom bubble alongside higher 30y yields NDX & US 30y yields during the 1990s Dotcom bubble"
  },
  {
    "figure_id": "F103",
    "report_id": "R007",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Equity resilience to high rates in today's bubble-prone market has resulted in elevated 30y yields today (now at '07 levels) vs other times the last 25 years when equities were near all-time highs US 30y yields when SPX"
  },
  {
    "figure_id": "F104",
    "report_id": "R007",
    "label": "Exhibit 18",
    "context": "Exhibit 18: While equity index vol appears subdued, single stock vol is historically elevated (96 $^{th}$ %ile), with ultra-low correlation (5 $^{th}$ %ile) acting as the dampener S&P Top 50 1m single stock implied vol & implied cor"
  },
  {
    "figure_id": "F105",
    "report_id": "R007",
    "label": "Exhibit 19",
    "context": "Exhibit 19: With rates vol remaining relatively subdued and TLT put skew steep, TLT put spreads are offering historically attractive payout ratios to hedge against a further rise in long-end yields TLT 1m 30d/10d put spread payout r"
  },
  {
    "figure_id": "F106",
    "report_id": "R007",
    "label": "Exhibit 22",
    "context": "Exhibit 20: Gilt yields widened by a historically extreme amount last week, driven by global macro concerns and amplified further by emerging UK political risk 10y Gilts daily sigma moves"
  },
  {
    "figure_id": "F107",
    "report_id": "R007",
    "label": "Exhibit 21",
    "context": "Exhibit 21: The accompanying Sterling weakness has typically driven relative strength in FTSE vs EU equities, albeit this has lessened over the years (making FTSE less GBP-dependent) FTSE vs SXXP relative performance and its correla"
  },
  {
    "figure_id": "F108",
    "report_id": "R007",
    "label": "Exhibit 22",
    "context": "Exhibit 22: UK-specific risks are clear in recent SX7E (EZ-Banks) vs SX7P (European banks) outperformance, although the former's long-run underperformance leaves room for a further catch-up SX7E/SX7P Price Ratio"
  },
  {
    "figure_id": "F109",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: SX7P-SX7E correlation remains close to 100% while the SX7E/SX7P vol ratio screens historically low ( $2^{nd}$ %tile)..."
  },
  {
    "figure_id": "F110",
    "report_id": "R007",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Net longs in SX7E futures have sharply declined since February, while SX7P has seen incremental net long positioning Eurex A-accounts futures open interest (in contracts)"
  },
  {
    "figure_id": "F111",
    "report_id": "R007",
    "label": "Exhibit 25",
    "context": "Exhibit 25: ... leading to a historically low cost of (+SX7E, -SX7P) call switches 2m 40-delta call premia for SX7E, SX7P and their spread (rhs)"
  },
  {
    "figure_id": "F112",
    "report_id": "R007",
    "label": "Exhibit 26",
    "context": "Exhibit 26: SX7P embeds significant UK banks' exposure unlike SX7E, which has proportionally higher exposures to EU banks Top 5 countries vs bottom 5 countries in terms of market cap weights difference between SX7E and SX7P and the"
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "Exhibit 27",
    "context": "Exhibit 27: European equities (SX5E) have been range-bound through the war, but may rally hard on a potential ‘resolution’, while EURGBP likely gains on UK political and fiscal concerns (GBP weakness) YTD SX5E and EURGBP Spot levels"
  },
  {
    "figure_id": "F114",
    "report_id": "R007",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Recent SX5E-EURGBP realised correlation and current implied levels are negative, and could turn positive if both assets rise in the coming weeks Rolling 1y SX5E-vs-EURGBP realised correlation and the latest implied level"
  },
  {
    "figure_id": "F115",
    "report_id": "R007",
    "label": "Exhibit 29",
    "context": "Exhibit 29: NDX has rallied 15% YTD, and is now within 1.5% of all-time highs, while Cable may see further weakness on UK risk YTD NDX and GBPUSD Spot levels"
  },
  {
    "figure_id": "F116",
    "report_id": "R007",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Recent realised and current implied NDX-GBPUSD correlations are positive, but could turn negative if Sterling weakens while NDX continues to make new highs Rolling 1y NDX-vs-GBPUSD realised correlation and the latest imp"
  },
  {
    "figure_id": "F117",
    "report_id": "R007",
    "label": "Exhibit 31",
    "context": "Exhibit 31: The AI hardware rally is changing the FTSE China A50 index. From less than 8% a year ago to 25%, IT is about to surpass Financials (and CATL, the battery maker, makes up most of Industrials) FTSE China A50 sector weights"
  },
  {
    "figure_id": "F118",
    "report_id": "R007",
    "label": "Exhibit 32",
    "context": "Exhibit 32: The China A50 index has better captured the recent semis rally compared to the Hang Seng Tech index and the KWEB ETF Equal risk performance relative to the start of the Iran war (+/-0% on 27 Feb)"
  },
  {
    "figure_id": "F119",
    "report_id": "R007",
    "label": "Exhibit 33",
    "context": "Exhibit 33: The FTSE China A50 (XIN9I) index has by far the most inverted call skew relative to global peers. All else equal, this makes XIN9I call spreads relatively cheaper Call skew across indices globally (3-month 105% - 115% vo"
  },
  {
    "figure_id": "F120",
    "report_id": "R007",
    "label": "Exhibit 34",
    "context": "Exhibit 34: While XIN9I vol is in the 76 $^{th}$ percentile, call skew is in the 7 $^{th}$ percentile, meaning one is buying skew at historically low levels XIN9I 3-month 105% implied vol and call skew (105% minus 115% vol)"
  },
  {
    "figure_id": "F121",
    "report_id": "R007",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Both price returns and price momentum of the Nasdaq rose as the dotcom bubble inflated NDX 6m price returns and 6m price momentum"
  },
  {
    "figure_id": "F122",
    "report_id": "R007",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Nasdaq's vol and fragility also rose into the peak of the dotcom bubble as tech stock price rose NDX 6m realized vol and 6m realized convexity"
  },
  {
    "figure_id": "F123",
    "report_id": "R007",
    "label": "Exhibit 37",
    "context": "Exhibit 37: The aggregate indicator is an average of 3 sub-indicators that capture short-, medium- and long-term price dynamics. Each sub-indicator is computed as a scaled average percentile rank of the four metrics (returns, vol, m"
  },
  {
    "figure_id": "F124",
    "report_id": "R007",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Looking at eight historical asset bubbles from a distributional lens using the BRI methodology reveals increasingly elevated returns, vol, momentum and fragility in the asset bubble formation process, as seen by rising l"
  },
  {
    "figure_id": "F125",
    "report_id": "R007",
    "label": "Exhibit 39",
    "context": "Exhibit 39: The median 3m max draw-down following indicator readings above 0.8 would have been more adverse than when below 0.8 during historical asset bubbles"
  },
  {
    "figure_id": "F126",
    "report_id": "R007",
    "label": "Exhibit 40",
    "context": "Exhibit 40: The median 3m max draw-up would have been similar at both high and low indicator readings, suggesting that de-risking completely following high indicator levels can risk underperformance"
  },
  {
    "figure_id": "F127",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Copper and aluminum spot prices LME copper price +2.8% WoW to US\\$13,895/t and LME aluminum price was +5.0% WoW at USD 3,741/t as of May 15"
  },
  {
    "figure_id": "F128",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Domestic monthly treatment charges on Cu concentrate Domestic monthly treatment charges on copper concentrate: -US\\$103.72/t as of May 15"
  },
  {
    "figure_id": "F129",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: COMEX gold spot price COMEX gold (spot) price decreased by 3.7% WoW to US\\$4,543/oz as of May 15"
  },
  {
    "figure_id": "F130",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Copper social inventory As of May 15, Shanghai bonded warehouse inventory/Shanghai social inventory was -2.7% / +4.5% WoW; Guangdong bonded warehouse inventory/Guangdong social inventory was +2.6% / flattish WoW"
  },
  {
    "figure_id": "F131",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Avg. national aluminum margin (60% captive plant) Avg. national aluminum margin rose by RMB 115/t WoW to RMB8,077/t as of May 15"
  },
  {
    "figure_id": "F132",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Spot cash margins at steel mills By May 15, spot rebar cash margins rose by RMB 23/t to -RMB 257/t, while spot HRC cash margins decreased by RMB 30/t to -RMB 213/t"
  },
  {
    "figure_id": "F133",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Containerboard margin tracker Nine Dragons margin tracker is now indicating NP/t of RMB118/t for this week"
  },
  {
    "figure_id": "F134",
    "report_id": "R008",
    "label": "Exhibit 9",
    "context": "Exhibit 9: China national cement shipment ratio The nationwide shipment ratio rose by 1.1ppts WoW to 43.9% as of May 15"
  },
  {
    "figure_id": "F135",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 10: National Float Glass Price and Xinyi Float Glass GPM As of May 14 $^{th}$ , the national average float glass price inched down by 0.05% WoW to RMB1,150.8/t. Our analysis shows Xinyi float glass GPM edged down by 0.4ppts"
  },
  {
    "figure_id": "F136",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 8: ASP at Qinhuangdao port (Kcal 5,500) ASP of QHD 5,500kcal spot price rose by 2.3% WoW to RMB830/t as of May 13"
  },
  {
    "figure_id": "F137",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Lithium carbonate unit refining margin Current lithium carbonate refining margin based on spodumene has narrowed and still stayed negative amid decreasing spodumene price"
  },
  {
    "figure_id": "F138",
    "report_id": "R008",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China Solar Glass Price vs GPM (%) Spot 3.2mm coated solar glass mid-point prices remained flat WoW as 15.25/sqm while 2.0mm coated solar glass mid-point prices down RMB 0.55/sqm to RMB8.45/sqm"
  },
  {
    "figure_id": "F139",
    "report_id": "R008",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Price comparison in LME & Changjiang copper LME copper price +2.8% WoW to US\\$13,895/t and Changjiang price +2.7% WoW to RMB105,790/t (US\\$13,036/t ex.VAT) as of May 15"
  },
  {
    "figure_id": "F140",
    "report_id": "R008",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Copper social inventory"
  },
  {
    "figure_id": "F141",
    "report_id": "R008",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Domestic monthly treatment charges on Cu concentrate"
  },
  {
    "figure_id": "F142",
    "report_id": "R008",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Copper inventory at exchanges"
  },
  {
    "figure_id": "F143",
    "report_id": "R008",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Price comparison in LME & Changjiang Aluminum LME aluminum price was +5.0% WoW at USD 3,741/t t and Changjiang price +0.6% wow to RMB24,370/t (USD3,166/t ex.VAT) as of May 15"
  },
  {
    "figure_id": "F144",
    "report_id": "R008",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Aluminum ingot inventory Domestic aluminum ingot inventory was -3.2% WoW to 1,390kt as of May 14"
  },
  {
    "figure_id": "F145",
    "report_id": "R008",
    "label": "Exhibit 20",
    "context": "Exhibit 20: COMEX gold spot price COMEX gold (spot) price decreased by 3.7% WoW to US\\$4,543/oz as of May 15"
  },
  {
    "figure_id": "F146",
    "report_id": "R008",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Avg. national aluminum margin (60% captive plant) Avg. national aluminum margin rose by RMB 115/t WoW to RMB8,077/t as of May 15"
  },
  {
    "figure_id": "F147",
    "report_id": "R008",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Domestic alumina prices Domestic alumina price settled higher at RMB2,685/t as of May 15"
  },
  {
    "figure_id": "F148",
    "report_id": "R008",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Global gold ETF monthly flows Global gold ETF had 45t net inflows in Apr 2026, +153% mom"
  },
  {
    "figure_id": "F149",
    "report_id": "R008",
    "label": "Exhibit 22",
    "context": "Exhibit 22: China central bank gold reserves China gold reserves was slightly increased mom to 74.64mn ounce in Apr 2026"
  },
  {
    "figure_id": "F150",
    "report_id": "R008",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Domestic battery-grade lithium carbonate ASP As of May 15, domestic battery-grade lithium carbonate (99.5%) price fell by 1.0% WoW to RMB192,000/t"
  },
  {
    "figure_id": "F151",
    "report_id": "R008",
    "label": "Exhibit 26",
    "context": "Exhibit 26: UxC Uranium U308 Weekly Spot Price (USD/lbs) Uranium U308 spot price +0.1% WoW to US\\$86.1/lbs"
  },
  {
    "figure_id": "F152",
    "report_id": "R008",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Lithium carbonate unit refining margin Current lithium carbonate refining margin based on spodumene has narrowed and still stayed negative amid decreasing spodumene price"
  },
  {
    "figure_id": "F153",
    "report_id": "R008",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Domestic lithium carbonate inventory China lithium carbonate inventory was -0.89% WoW to 102.7kt"
  },
  {
    "figure_id": "F154",
    "report_id": "R008",
    "label": "Exhibit 27",
    "context": "Exhibit 27: China Shanghai Changjiang Cobalt Spot Price (RMB/ton) China Shanghai Changjiang Cobalt Spot Price -0.2% WoW to RMB 425k/t"
  },
  {
    "figure_id": "F155",
    "report_id": "R008",
    "label": "Exhibit 28",
    "context": "Exhibit 28: National average NdPr oxide price National average NdPr oxide price -2.5% WoW to RMB738,200/t"
  },
  {
    "figure_id": "F156",
    "report_id": "R008",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Natioanl average black tungsten concentrate (Wolframite) price, (65% WO $_{3}$ , RMB/ton) National average black tungsten concentrate price -27.3% WoW to RMB 493k/t"
  },
  {
    "figure_id": "F157",
    "report_id": "R008",
    "label": "Exhibit 30",
    "context": "Exhibit 30: China domestic steel prices at key cities By May 15, domestic rebar prices across major cities (Beijing, Guangzhou, Shanghai, Shenyang, Wuhan) fell by 1.3% WoW to RMB 3,416/t, and domestic HRC prices also inched down by"
  },
  {
    "figure_id": "F158",
    "report_id": "R008",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Weekly China Steel Output"
  },
  {
    "figure_id": "F159",
    "report_id": "R008",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Imported iron ore CFR 62% prices at Tianjin Port"
  },
  {
    "figure_id": "F160",
    "report_id": "R008",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Iron ore inventory at large-medium steel mills and at ports"
  },
  {
    "figure_id": "F161",
    "report_id": "R008",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Spot cash margins at steel mills By May 15, spot rebar cash margins rose by RMB 23/t to -RMB 257/t, while spot HRC cash margins decreased by RMB 30/t to -RMB 213/t Rmb/t"
  },
  {
    "figure_id": "F162",
    "report_id": "R008",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Utilization rates of blast furnaces across the nation According to Mysteel, national blast-furnace utilization kept inched up by 0.2 WoW as 89.7% as of May 15, while the operating rate across 247 surveyed steel mills inc"
  },
  {
    "figure_id": "F163",
    "report_id": "R008",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Steel inventory By May 15, finished-steel inventories (rebar, wire rod, HRC, CRC and plate) narrowed by 4.3% WoW to 15.8 mnt"
  },
  {
    "figure_id": "F164",
    "report_id": "R008",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Cash margins at large mills (inventory lag) By May 15, rebar cash margins at large mills improved by RMB 75/t to -RMB 151/t, while HRC cash margins also increased by RMB 21/t to -RMB 107/t"
  },
  {
    "figure_id": "F165",
    "report_id": "R008",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Operating rate of Electric-arc-furnace (EAF) mills The operating rate of EAF mills inched up by 0.4ppts WoW to 55.25% in the week ending May 15"
  },
  {
    "figure_id": "F166",
    "report_id": "R008",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Steel apparent consumption Steel apparent consumption (rebar, wire rod, HRC, CRC and plate) improved by 8.4% WoW to 9.1 mnt"
  },
  {
    "figure_id": "F167",
    "report_id": "R008",
    "label": "Exhibit 27",
    "context": "Exhibit 27: National average Cement price The average national cement price +0.4% WoW to RMB313/t as of May 15"
  },
  {
    "figure_id": "F168",
    "report_id": "R008",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Central South China average cement price As of May 15, Central South China cement prices increased by 5.7% WoW to RMB314/t"
  },
  {
    "figure_id": "F169",
    "report_id": "R008",
    "label": "Exhibit 40",
    "context": "Exhibit 40: East China average cement price As of May 15, East China cement prices fell by 2.1% WoW to RMB314/t WoW"
  },
  {
    "figure_id": "F170",
    "report_id": "R008",
    "label": "Exhibit 41",
    "context": "Exhibit 41: China national average cement prices vs inventory Prices edged up while inventory trended higher WoW"
  },
  {
    "figure_id": "F171",
    "report_id": "R008",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Glass Inventory & Inventory day As of May 14, glass producers' inventory from monitored provinces was 68.92mn weight case, representing 38.12 inventory days"
  },
  {
    "figure_id": "F172",
    "report_id": "R008",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Glass effective capacity As of May 14, there are 264 float glass production lines nationwide, of which 203 are currently operating. Nationally effective capacity of all float glass lines remained the same as 147,635t/d"
  },
  {
    "figure_id": "F173",
    "report_id": "R008",
    "label": "Exhibit 44",
    "context": "Exhibit 44: China linerboard and corrugating medium price As of May 13, national average linerboard price edged up by 0.3% WoW to RMB3,652/t; national average corrugating medium price was +1.0% WoW to RMB2,789/t. Blended paper price"
  },
  {
    "figure_id": "F174",
    "report_id": "R008",
    "label": "Exhibit 46",
    "context": "Exhibit 46: China Solar Glass Price vs GPM (%) Spot 3.2mm coated solar glass mid-point prices remained flat WoW as 15.25/sqm while 2.0mm coated solar glass mid-point prices down RMB 0.55/sqm to RMB8.45/sqm"
  },
  {
    "figure_id": "F175",
    "report_id": "R008",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Nine Dragons margin tracker Nine Dragons margin tracker is now indicating NP/t of RMB118/t for this week"
  },
  {
    "figure_id": "F176",
    "report_id": "R008",
    "label": "Exhibit 47",
    "context": "Exhibit 47: China Solar Glass Production and Inventory Solar glass daily capacity remained flat WoW as 86,800t/day and inventory days expanded 7.1% WoW to 52.82 during the week-ended on 14 May 2026"
  },
  {
    "figure_id": "F177",
    "report_id": "R009",
    "label": "Figure 1",
    "context": "# #1. Noticeable shortages of recalled formula brands and switching from recalled brands to Chinese brands 84% of respondents who currently use or used to purchase Danone (Aptamil, Nutrilon) and/or Nestle Wyeth (NAN, Illuma, S-26) have found these labels to be"
  },
  {
    "figure_id": "F178",
    "report_id": "R009",
    "label": "Figure 2",
    "context": "Figure 2. Have you switched from Danone (Aptamil, Nutrilon) and Nestle Wyeth (NAN, Illuma, S-26) to other brands?"
  },
  {
    "figure_id": "F179",
    "report_id": "R009",
    "label": "Figure 4",
    "context": "Whilst the percentage of respondents that prefer foreign brands has declined to its lowest point since the start of our infant formula surveys in 2020 (Figure 4), the proportion of respondents who prefer domestic brands is unchanged since 2025, with the majori"
  },
  {
    "figure_id": "F180",
    "report_id": "R009",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Which of the following offers the highest quality infant milk formula?"
  },
  {
    "figure_id": "F181",
    "report_id": "R009",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. When purchasing infant milk formula, do you prefer to buy domestic or foreign brands?"
  },
  {
    "figure_id": "F182",
    "report_id": "R009",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Based on your experience or what you read/heard, which of the regions below produces the highest quality formula milk?"
  },
  {
    "figure_id": "F183",
    "report_id": "R009",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. What are the main three factors that influence your choice of formula milk?"
  },
  {
    "figure_id": "F184",
    "report_id": "R009",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. How have your views of the quality of Chinese and foreign brands of formula milk changed in the past 12 months?"
  },
  {
    "figure_id": "F185",
    "report_id": "R009",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. Are you more likely to buy a foreign brand, if it is manufactured in China?"
  },
  {
    "figure_id": "F186",
    "report_id": "R009",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. What infant formula has your child primarily consumed over the last 12 months?"
  },
  {
    "figure_id": "F187",
    "report_id": "R009",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Why do you choose domestic Chinese brands for formula milk?"
  },
  {
    "figure_id": "F188",
    "report_id": "R009",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Why do you choose foreign brands for formula milk?"
  },
  {
    "figure_id": "F189",
    "report_id": "R009",
    "label": "Figure 13",
    "context": "Nestlé. The improving quality perception of domestically produced infant formula is a headwind for Nestlé – premiumization and increasing need for R&D is a positive for price/mix, but we would still assume Danone to be a relative winner. Abbott. These results "
  },
  {
    "figure_id": "F190",
    "report_id": "R009",
    "label": "Figure 14",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 14. Why are you spending more money on infant formula product compared to 12 months ago?"
  },
  {
    "figure_id": "F191",
    "report_id": "R009",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 15. Why are you spending less money on infant formula product compared to 12 months ago?"
  },
  {
    "figure_id": "F192",
    "report_id": "R009",
    "label": "Figure 16",
    "context": "The survey suggests the majority of respondents are not likely to change whether they breastfeed or not (Figure 16). However, the survey has detected a growing proportion of Chinese mothers who believe that breastmilk is better quality than bottle milk for chi"
  },
  {
    "figure_id": "F193",
    "report_id": "R009",
    "label": "Figure 17",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 17. Why are you less likely to breastfeed?"
  },
  {
    "figure_id": "F194",
    "report_id": "R009",
    "label": "Figure 18",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 18. What do you see as the best quality milk for children?"
  },
  {
    "figure_id": "F195",
    "report_id": "R009",
    "label": "Figure 19",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 19. Why have you changed the brand of formula milk you purchase?"
  },
  {
    "figure_id": "F196",
    "report_id": "R009",
    "label": "Figure 20",
    "context": "Danone/ Nestlé. Any substitution from breastfeeding to infant formula would be positive for multinationals and should help decouple the company's prospects from the birth rate. Abbott. Any shift in preference to infant formula from breastfeeding would benefit "
  },
  {
    "figure_id": "F197",
    "report_id": "R009",
    "label": "Figure 21",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 21. Which of the following formula milk types has the highest quality?"
  },
  {
    "figure_id": "F198",
    "report_id": "R009",
    "label": "Figure 22",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 22. Which of the following formula milk types has the highest quality?"
  },
  {
    "figure_id": "F199",
    "report_id": "R009",
    "label": "Figure 24",
    "context": "Nestlé. The growing importance of added nutrients such as HMOs is a tailwind for Nestlé which launched its first HMO growing-up milk in China under Wyeth illumina in 2023 and has a strong historic presence in that field. Abbott. These results are not relevant "
  },
  {
    "figure_id": "F200",
    "report_id": "R009",
    "label": "Figure 25",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 25. Main reason respondents buy formula at Cross border e-commerce"
  },
  {
    "figure_id": "F201",
    "report_id": "R009",
    "label": "Figure 24",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 24. Given cost of living pressures, are you likely to switch from buying from retail stores to buying through online channels in the next 12 months?"
  },
  {
    "figure_id": "F202",
    "report_id": "R009",
    "label": "Figure 26",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 26. Main reason respondents buy formula at Emerging online channels (Douyin/TikTok)"
  },
  {
    "figure_id": "F203",
    "report_id": "R009",
    "label": "Figure 27",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 27. Where respondents most often shop for infant formula"
  },
  {
    "figure_id": "F204",
    "report_id": "R009",
    "label": "Figure 28",
    "context": "Danone/ Nestlé. The move towards online channels including CBEC and emerging online channels (Douyin/TikTok) is a positive for all multinationals operating at scale, be it Danone or Nestlé in our view. Abbott. These results are likely neutral for Abbott, altho"
  },
  {
    "figure_id": "F205",
    "report_id": "R009",
    "label": "Figure 29",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 29. Are you seeing more people in China getting married but not having children?"
  },
  {
    "figure_id": "F206",
    "report_id": "R009",
    "label": "Figure 30",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 30. With marriages increasing, what do you expect the impact to be on the number of newborns?"
  },
  {
    "figure_id": "F207",
    "report_id": "R009",
    "label": "Figure 31",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 31. China marriage rate © 2026 Citi Inc. No redistribution without Citi's written permission. # Potential stock implications ■ a2 Milk. The fall in the birth rate in 2025 is a headwin"
  },
  {
    "figure_id": "F208",
    "report_id": "R009",
    "label": "Figure 32",
    "context": "# #8. As financial pressures ease, respondents require less government support incentives (including subsidies) to have children Survey respondents are split on whether the government subsidy will increase motivation to have children (Figure 32). However, a la"
  },
  {
    "figure_id": "F209",
    "report_id": "R009",
    "label": "Figure 34",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 34. What are the main reasons for not planning to have a child or children in the future?"
  },
  {
    "figure_id": "F210",
    "report_id": "R009",
    "label": "Figure 33",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 33. In the past 12 months your financial health has?"
  },
  {
    "figure_id": "F211",
    "report_id": "R009",
    "label": "Figure 35",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 35. How much financial support do you need from the government to increase your motivation to have children?"
  },
  {
    "figure_id": "F212",
    "report_id": "R009",
    "label": "Figure 36",
    "context": "# #9. Chinese zodiac signs have small influence on births over the next two years Almost three quarters of respondents reported that zodiac signs had no influence on their plans on when to have children. The improved sentiment for 2026 and 2027 (Horse and Goat"
  },
  {
    "figure_id": "F213",
    "report_id": "R009",
    "label": "Figure 37",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 37. Please indicate the likelihood of having a child during the following years in comparison to other years."
  },
  {
    "figure_id": "F214",
    "report_id": "R009",
    "label": "Figure 38",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Year of Snake data from 2025 survey, Year of Horse and Year of Goat data from 2026 survey Figure 38. Please indicate the likelihood of having a child during the Year of the Horse (2026)"
  },
  {
    "figure_id": "F215",
    "report_id": "R009",
    "label": "Figure 44",
    "context": "Roughly two thirds of respondents purchase pediatric supplements. When choosing pediatric supplements, 62% are more likely to choose a brand known for infant formula, and 86% see foreign pediatric supplements brands becoming more popular compared to domestic b"
  },
  {
    "figure_id": "F216",
    "report_id": "R009",
    "label": "Figure 40",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 40. Why does your child/would your child consume stage 4 / kids milk powder?"
  },
  {
    "figure_id": "F217",
    "report_id": "R009",
    "label": "Figure 41",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 41. Until what age would I keep my child consuming stage 4 / kids milk powder?"
  },
  {
    "figure_id": "F218",
    "report_id": "R009",
    "label": "Figure 42",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 42. Do you purchase pediatric supplements?"
  },
  {
    "figure_id": "F219",
    "report_id": "R009",
    "label": "Figure 44",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 44. Do you see foreign pediatric supplement brands becoming more or less popular compared to domestic brands?"
  },
  {
    "figure_id": "F220",
    "report_id": "R009",
    "label": "Figure 43",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 43. When choosing a pediatric supplement brand, are you more or less likely to choose a brand who is known for infant formula?"
  },
  {
    "figure_id": "F221",
    "report_id": "R009",
    "label": "Figure 45",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 45. What would cause you to try a new brand of pediatric supplement?"
  },
  {
    "figure_id": "F222",
    "report_id": "R009",
    "label": "Figure 46",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 46. Are older people in your family likely to consume milk formula products specifically formulated for senior citizens from infant formula brands?"
  },
  {
    "figure_id": "F223",
    "report_id": "R009",
    "label": "Figure 47",
    "context": "Nestlé. Nestle also has a presence in both pediatrics and Adult Nutrition, addressing roughly the same segments (tube feeding, supplements for elder malnutrition). Abbott. With Abbott offering a diverse product line beyond infant nutrition, more consumer inter"
  },
  {
    "figure_id": "F224",
    "report_id": "R009",
    "label": "Figure 48",
    "context": "Citi's Research Innovation Lab has conducted a survey of 1,200 parents/caregivers of young children (0 to 6 years) in China who purchase infant formula. The sample spans all city tiers (1 to 5) and income brackets. We analyse the drivers behind infant formula "
  },
  {
    "figure_id": "F225",
    "report_id": "R009",
    "label": "Figure 49",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 49. Number of people in respondent's household"
  },
  {
    "figure_id": "F226",
    "report_id": "R009",
    "label": "Figure 50",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 50. Sample city tier distribution"
  },
  {
    "figure_id": "F227",
    "report_id": "R009",
    "label": "Figure 51",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 51. Respondent type - responsible for buying IMF"
  },
  {
    "figure_id": "F228",
    "report_id": "R010",
    "label": "Figure 3",
    "context": "4M26 REI -13.7% ('25: -17.2%); 4M26 FAI -1.6% (NBS) Figure 3. Real Estate Investment: Monthly YoY Change (Apr-26)"
  },
  {
    "figure_id": "F229",
    "report_id": "R010",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 4. YoY YTD Change in REI vs. GFA Starts (by 4M26)"
  },
  {
    "figure_id": "F230",
    "report_id": "R010",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 5. FAI Breakdown on REI, Manufacturing & Infrastructure Investments (by 4M26)"
  },
  {
    "figure_id": "F231",
    "report_id": "R010",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission # Starts, Completion and Land Investment (NBS) Figure 6. GFA Starts: Monthly YoY Change (by Apr-26)"
  },
  {
    "figure_id": "F232",
    "report_id": "R010",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 7. GFA Completion: Monthly YoY Change (by Apr-26)"
  },
  {
    "figure_id": "F233",
    "report_id": "R010",
    "label": "Figure 9",
    "context": "Figure 9. 300 Cities Land Sales by Transaction Value © 2026 Citi Inc. No redistribution without Citi's written permission Figure 10. CREIS 300-Cities Residential Land GFA Sold"
  },
  {
    "figure_id": "F234",
    "report_id": "R010",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. National Residential Inventory hits 421m sqm by Apr 2026 (mn sqm GFA)"
  },
  {
    "figure_id": "F235",
    "report_id": "R010",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # ■ Ministry of Finance government land sales revenue Figure 12. Govt Land Sales Revenue"
  },
  {
    "figure_id": "F236",
    "report_id": "R010",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. 18 cities include 3 Tier-1 cities: Beijing, Shanghai, Shenzhen; 9 Tier-2 cities: Chengdu, Dalian, Hangzhou, Nanjing, Nanning, Qingdao, Suzhou, Wuxi, Xiamen; 6 Tier-3/4 cities: Dongguan, Fosh"
  },
  {
    "figure_id": "F237",
    "report_id": "R010",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 16. 80-Cities Inventory Months by City Tier"
  },
  {
    "figure_id": "F238",
    "report_id": "R010",
    "label": "Figure 17",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission # Home Price Index (NBS 70-Cities) Figure 17. NBS Monthly Primary Price Index of 70 Key Cities (Apr -3.7%yoy/ -0.2%mom; Mar -3.6%yoy/ -0.2%mom)"
  },
  {
    "figure_id": "F239",
    "report_id": "R010",
    "label": "Figure 18",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 18. NBS Monthly Secondary Price Index of 70 Cities (Apr-6.2%yoy/ -0.2%mom; Mar-6.3%yoy/ -0.2%mom)"
  },
  {
    "figure_id": "F240",
    "report_id": "R010",
    "label": "Figure 19",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 19. NBS 70 Cities Primary ASP MoM Change: No. of cities with MoM Primary Price Higher/ Flattish/ Lower"
  },
  {
    "figure_id": "F241",
    "report_id": "R010",
    "label": "Figure 20",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission Figure 20. NBS 70 Cities Secondary ASP MoM Change: No. of cities with MoM Secondary Price Higher/ Flattish/ Lower © 2026 Citi Inc. No redistribution without Citi's written permission # Valuat"
  },
  {
    "figure_id": "F242",
    "report_id": "R010",
    "label": "Figure 20",
    "context": "Figure 20. NBS 70 Cities Secondary ASP MoM Change: No. of cities with MoM Secondary Price Higher/ Flattish/ Lower © 2026 Citi Inc. No redistribution without Citi's written permission # Valuations Figure 21. China Property: NAV Discount (15 May 2026)"
  },
  {
    "figure_id": "F243",
    "report_id": "R010",
    "label": "Figure 22",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 22. China Property: PE (15 May 2026)"
  },
  {
    "figure_id": "F244",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "The aluminium market is increasingly transitioning from an initial geopolitical shock into a structurally tighter inventory regime. The first phase of the move was dominated by war escalation risk, Strait of Hormuz concerns, oil price spikes, and broader macro"
  },
  {
    "figure_id": "F245",
    "report_id": "R011",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Historical spare capacity in Chian's aluminium industry has disappeared-implications for prices and supply elasticity"
  },
  {
    "figure_id": "F246",
    "report_id": "R011",
    "label": "Figure 11",
    "context": "Only an extreme recession scenario comparable to the Volcker-era downturn or the 2008-09 GFC appears sufficient to stabilise aluminium inventory cover. We have already revised down our aluminium demand growth assumptions materially in our base case supply and "
  },
  {
    "figure_id": "F247",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "Historically, severe recessions rebuilt aluminium inventories. In the current framework, they merely prevent inventories tightening further. This represents a materially higher threshold for market rebalancing relative to previous aluminium cycles. The market "
  },
  {
    "figure_id": "F248",
    "report_id": "R011",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Today's aluminium demand profile also looks structurally less cyclical than during previous recession periods. Historically, aluminium demand growth relied much more heavily on traditional i"
  },
  {
    "figure_id": "F249",
    "report_id": "R011",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. China's aluminium demand has become increasingly supported by less cyclical energy transition sectors"
  },
  {
    "figure_id": "F250",
    "report_id": "R011",
    "label": "Figure 7",
    "context": "We also expect the impact of the current US-Iran conflict on aluminium demand to remain highly asymmetric between China and ex-China markets. A similar pattern was visible during the 2008-09 GFC when ex-China economies absorbed most of the cyclical demand dest"
  },
  {
    "figure_id": "F251",
    "report_id": "R011",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Relative aluminium-to-steel pricing has become increasingly elevated in China, although substitution economics across ex-China markets remain materially less extreme"
  },
  {
    "figure_id": "F252",
    "report_id": "R011",
    "label": "Figure 9",
    "context": "Figure 9. Citi aluminium price forecasts and scenarios © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. Citi aluminium price forecasts and scenarios © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11"
  },
  {
    "figure_id": "F253",
    "report_id": "R012",
    "label": "Figure 2",
    "context": "Figure 2: Polysilicon spot prices"
  },
  {
    "figure_id": "F254",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "Figure 3: Wafer spot prices"
  },
  {
    "figure_id": "F255",
    "report_id": "R012",
    "label": "Figure 4",
    "context": "Figure 4: Cell spot prices"
  },
  {
    "figure_id": "F256",
    "report_id": "R012",
    "label": "Figure 5",
    "context": "Figure 5: Module spot prices"
  },
  {
    "figure_id": "F257",
    "report_id": "R012",
    "label": "Figure 6",
    "context": "Figure 6: Polysilicon unit all-in cash profit tracker"
  },
  {
    "figure_id": "F258",
    "report_id": "R012",
    "label": "Figure 7",
    "context": "Figure 7: Wafer unit all-in cash profit tracker"
  },
  {
    "figure_id": "F259",
    "report_id": "R012",
    "label": "Figure 8",
    "context": "Figure 8: Cell unit all-in cash profit tracker"
  },
  {
    "figure_id": "F260",
    "report_id": "R012",
    "label": "Figure 9",
    "context": "Figure 9: Unit net profit/loss for integrated module"
  },
  {
    "figure_id": "F261",
    "report_id": "R013",
    "label": "Figure 2",
    "context": "Figure 2: G15 NEV Penetration Rate by Country"
  },
  {
    "figure_id": "F262",
    "report_id": "R013",
    "label": "Figure 4",
    "context": "Figure 4: G15 NEV Penetration Rate Trend"
  },
  {
    "figure_id": "F263",
    "report_id": "R013",
    "label": "Figure 9",
    "context": "Figure 9: Brazil Top Models Breakdown"
  },
  {
    "figure_id": "F264",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "Figure 11: Brazil NEV Breakdown"
  },
  {
    "figure_id": "F265",
    "report_id": "R013",
    "label": "Figure 12",
    "context": "Figure 12: Brazil NEV Penetration Rate"
  },
  {
    "figure_id": "F266",
    "report_id": "R013",
    "label": "Figure 13",
    "context": "Figure 13: Canada Top Models Breakdown"
  },
  {
    "figure_id": "F267",
    "report_id": "R013",
    "label": "Figure 15",
    "context": "Figure 15: Canada NEV Breakdown"
  },
  {
    "figure_id": "F268",
    "report_id": "R013",
    "label": "Figure 16",
    "context": "Figure 16: Canada NEV Penetration Rate"
  },
  {
    "figure_id": "F269",
    "report_id": "R013",
    "label": "Figure 17",
    "context": "Figure 17: China Top Models Breakdown"
  },
  {
    "figure_id": "F270",
    "report_id": "R013",
    "label": "Figure 19",
    "context": "Figure 19: China NEV Breakdown"
  },
  {
    "figure_id": "F271",
    "report_id": "R013",
    "label": "Figure 20",
    "context": "Figure 20: China NEV Penetration Rate"
  },
  {
    "figure_id": "F272",
    "report_id": "R013",
    "label": "Figure 21",
    "context": "Figure 21: Finland Top Models Breakdown"
  },
  {
    "figure_id": "F273",
    "report_id": "R013",
    "label": "Figure 23",
    "context": "Figure 23: Finland NEV Breakdown"
  },
  {
    "figure_id": "F274",
    "report_id": "R013",
    "label": "Figure 24",
    "context": "Figure 24: Finland NEV Penetration Rate"
  },
  {
    "figure_id": "F275",
    "report_id": "R013",
    "label": "Figure 25",
    "context": "Figure 25: France Top Models Breakdown"
  },
  {
    "figure_id": "F276",
    "report_id": "R013",
    "label": "Figure 27",
    "context": "Figure 27: France NEV Breakdown"
  },
  {
    "figure_id": "F277",
    "report_id": "R013",
    "label": "Figure 28",
    "context": "Figure 28: France NEV Penetration Rate"
  },
  {
    "figure_id": "F278",
    "report_id": "R013",
    "label": "Figure 29",
    "context": "Figure 29: Germany Top Models Breakdown"
  },
  {
    "figure_id": "F279",
    "report_id": "R013",
    "label": "Figure 31",
    "context": "Figure 31: Germany NEV Breakdown"
  },
  {
    "figure_id": "F280",
    "report_id": "R013",
    "label": "Figure 32",
    "context": "Figure 32: Germany NEV Penetration Rate"
  },
  {
    "figure_id": "F281",
    "report_id": "R013",
    "label": "Figure 33",
    "context": "Figure 33: India Top Models Breakdown"
  },
  {
    "figure_id": "F282",
    "report_id": "R013",
    "label": "Figure 34",
    "context": "Figure 34: India NEV Sales Trend"
  },
  {
    "figure_id": "F283",
    "report_id": "R013",
    "label": "Figure 36",
    "context": "Figure 36: India NEV Penetration Rate"
  },
  {
    "figure_id": "F284",
    "report_id": "R013",
    "label": "Figure 37",
    "context": "Figure 37: Italy Top Models Breakdown"
  },
  {
    "figure_id": "F285",
    "report_id": "R013",
    "label": "Figure 39",
    "context": "Figure 39: Italy NEV Breakdown"
  },
  {
    "figure_id": "F286",
    "report_id": "R013",
    "label": "Figure 40",
    "context": "Figure 40: Italy NEV Penetration Rate"
  },
  {
    "figure_id": "F287",
    "report_id": "R013",
    "label": "Figure 41",
    "context": "Figure 41: Japan Top Models Breakdown"
  },
  {
    "figure_id": "F288",
    "report_id": "R013",
    "label": "Figure 43",
    "context": "Figure 43: Japan NEV Breakdown"
  },
  {
    "figure_id": "F289",
    "report_id": "R013",
    "label": "Figure 44",
    "context": "Figure 44: Japan NEV Penetration Rate"
  },
  {
    "figure_id": "F290",
    "report_id": "R013",
    "label": "Figure 45",
    "context": "Figure 45: Korea Top Models Breakdown"
  },
  {
    "figure_id": "F291",
    "report_id": "R013",
    "label": "Figure 47",
    "context": "Figure 47: Korea NEV Breakdown"
  },
  {
    "figure_id": "F292",
    "report_id": "R013",
    "label": "Figure 48",
    "context": "Figure 48: Korea NEV Penetration Rate"
  },
  {
    "figure_id": "F293",
    "report_id": "R013",
    "label": "Figure 49",
    "context": "Figure 49: Norway Top Models Breakdown"
  },
  {
    "figure_id": "F294",
    "report_id": "R013",
    "label": "Figure 51",
    "context": "Figure 51: Norway NEV Breakdown"
  },
  {
    "figure_id": "F295",
    "report_id": "R013",
    "label": "Figure 52",
    "context": "Figure 52: Norway NEV Penetration Rate"
  },
  {
    "figure_id": "F296",
    "report_id": "R013",
    "label": "Figure 53",
    "context": "Figure 53: Sweden Top Models Breakdown"
  },
  {
    "figure_id": "F297",
    "report_id": "R013",
    "label": "Figure 55",
    "context": "Figure 55: Sweden NEV Breakdown"
  },
  {
    "figure_id": "F298",
    "report_id": "R013",
    "label": "Figure 56",
    "context": "Figure 56: Sweden NEV Penetration Rate"
  },
  {
    "figure_id": "F299",
    "report_id": "R013",
    "label": "Figure 57",
    "context": "Figure 57: Thailand Top Models Breakdown"
  },
  {
    "figure_id": "F300",
    "report_id": "R013",
    "label": "Figure 59",
    "context": "Figure 59: Thailand NEV Breakdown"
  },
  {
    "figure_id": "F301",
    "report_id": "R013",
    "label": "Figure 60",
    "context": "Figure 60: Thailand NEV Penetration Rate"
  },
  {
    "figure_id": "F302",
    "report_id": "R013",
    "label": "Figure 61",
    "context": "Figure 61: UK Top Models Breakdown"
  },
  {
    "figure_id": "F303",
    "report_id": "R013",
    "label": "Figure 63",
    "context": "Figure 63: UK NEV Breakdown"
  },
  {
    "figure_id": "F304",
    "report_id": "R013",
    "label": "Figure 64",
    "context": "Figure 64: UK NEV Penetration Rate"
  },
  {
    "figure_id": "F305",
    "report_id": "R013",
    "label": "Figure 65",
    "context": "Figure 65: USA Top Models Breakdown"
  },
  {
    "figure_id": "F306",
    "report_id": "R013",
    "label": "Figure 67",
    "context": "Figure 67: USA NEV Breakdown"
  },
  {
    "figure_id": "F307",
    "report_id": "R013",
    "label": "Figure 68",
    "context": "Figure 68: USA NEV Penetration Rate"
  },
  {
    "figure_id": "F308",
    "report_id": "R013",
    "label": "Figure 70",
    "context": "Figure 70: BYD NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F309",
    "report_id": "R013",
    "label": "Figure 72",
    "context": "Figure 72: BYD G15 NEV Market Share"
  },
  {
    "figure_id": "F310",
    "report_id": "R013",
    "label": "Figure 73",
    "context": "Figure 73: Geely NEV Sales by Country Figure 75: Geely NEV Sales Trend"
  },
  {
    "figure_id": "F311",
    "report_id": "R013",
    "label": "Figure 74",
    "context": "Figure 74: Geely NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F312",
    "report_id": "R013",
    "label": "Figure 78",
    "context": "Figure 78: Great Wall Motor NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F313",
    "report_id": "R013",
    "label": "Figure 80",
    "context": "Figure 80: Great Wall Motor G15 NEV Market Share"
  },
  {
    "figure_id": "F314",
    "report_id": "R013",
    "label": "Figure 82",
    "context": "Figure 82: Li Auto NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F315",
    "report_id": "R013",
    "label": "Figure 84",
    "context": "Figure 84: Li Auto G15 NEV Market Share"
  },
  {
    "figure_id": "F316",
    "report_id": "R013",
    "label": "Figure 86",
    "context": "Figure 86: XPeng NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F317",
    "report_id": "R013",
    "label": "Figure 88",
    "context": "Figure 88: XPeng G15 NEV Market Share"
  },
  {
    "figure_id": "F318",
    "report_id": "R013",
    "label": "Figure 90",
    "context": "Figure 90: NIO NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F319",
    "report_id": "R013",
    "label": "Figure 92",
    "context": "Figure 92: NIO G15 NEV Market Share"
  },
  {
    "figure_id": "F320",
    "report_id": "R013",
    "label": "Figure 94",
    "context": "Figure 94: Leapmotor NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F321",
    "report_id": "R013",
    "label": "Figure 96",
    "context": "Figure 96: Leapmotor G15 NEV Market Share"
  },
  {
    "figure_id": "F322",
    "report_id": "R013",
    "label": "Figure 98",
    "context": "Figure 98: Tesla NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F323",
    "report_id": "R013",
    "label": "Figure 100",
    "context": "Figure 100: Tesla G15 NEV Market Share"
  },
  {
    "figure_id": "F324",
    "report_id": "R013",
    "label": "Figure 102",
    "context": "Figure 102: Rivian NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F325",
    "report_id": "R013",
    "label": "Figure 104",
    "context": "Figure 104: Rivian G15 NEV Market Share"
  },
  {
    "figure_id": "F326",
    "report_id": "R013",
    "label": "Figure 106",
    "context": "Figure 106: GM NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F327",
    "report_id": "R013",
    "label": "Figure 108",
    "context": "Figure 108: GM G15 NEV Market Share"
  },
  {
    "figure_id": "F328",
    "report_id": "R013",
    "label": "Figure 109",
    "context": "Figure 109: Ford NEV Sales by Country Figure 111: Ford NEV Sales Trend"
  },
  {
    "figure_id": "F329",
    "report_id": "R013",
    "label": "Figure 110",
    "context": "Figure 110: Ford NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F330",
    "report_id": "R013",
    "label": "Figure 113",
    "context": "Figure 113: BMW NEV Sales by Country Figure 115: BMW NEV Sales Trend"
  },
  {
    "figure_id": "F331",
    "report_id": "R013",
    "label": "Figure 114",
    "context": "Figure 114: BMW NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F332",
    "report_id": "R013",
    "label": "Figure 118",
    "context": "Figure 118: Mercedes-Benz NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F333",
    "report_id": "R013",
    "label": "Figure 120",
    "context": "Figure 120: Mercedes-Benz G15 NEV Market Share"
  },
  {
    "figure_id": "F334",
    "report_id": "R013",
    "label": "Figure 121",
    "context": "Figure 121: VW NEV Sales by Country Figure 123: VW NEV Sales Trend"
  },
  {
    "figure_id": "F335",
    "report_id": "R013",
    "label": "Figure 122",
    "context": "Figure 122: VW NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F336",
    "report_id": "R013",
    "label": "Figure 126",
    "context": "Figure 126: Renault NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F337",
    "report_id": "R013",
    "label": "Figure 128",
    "context": "Figure 128: Renault G15 NEV Market Share"
  },
  {
    "figure_id": "F338",
    "report_id": "R013",
    "label": "Figure 130",
    "context": "Figure 130: Stellantis NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F339",
    "report_id": "R013",
    "label": "Figure 132",
    "context": "Figure 132: Stellantis G15 NEV Market Share"
  },
  {
    "figure_id": "F340",
    "report_id": "R013",
    "label": "Figure 134",
    "context": "Figure 134: Honda NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F341",
    "report_id": "R013",
    "label": "Figure 136",
    "context": "Figure 136: Honda G15 NEV Market Share"
  },
  {
    "figure_id": "F342",
    "report_id": "R013",
    "label": "Figure 138",
    "context": "Figure 138: Toyota NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F343",
    "report_id": "R013",
    "label": "Figure 140",
    "context": "Figure 140: Toyota G15 NEV Market Share"
  },
  {
    "figure_id": "F344",
    "report_id": "R013",
    "label": "Figure 142",
    "context": "Figure 142: Nissan NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F345",
    "report_id": "R013",
    "label": "Figure 144",
    "context": "Figure 144: Nissan G15 NEV Market Share"
  },
  {
    "figure_id": "F346",
    "report_id": "R013",
    "label": "Figure 146",
    "context": "Figure 146: Hyundai-Kia NEV Sales Breakdown - Top Models"
  },
  {
    "figure_id": "F347",
    "report_id": "R013",
    "label": "Figure 148",
    "context": "Figure 148: Hyundai-Kia G15 NEV Market Share"
  },
  {
    "figure_id": "F348",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 1: Henry Hub prices have been correlated with this summer's weather forecast evolution Total CDD forecast evolution for Apr+May+Jun vs Henry Hub Prompt (rhs, \\$/mmBtu)"
  },
  {
    "figure_id": "F349",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 2: YTD growth in Haynesville production has been much lower than a year ago, suggesting a degree of sensitivity to price North Louisiana dry gas production, Bcf/d"
  },
  {
    "figure_id": "F350",
    "report_id": "R016",
    "label": "Figure 5",
    "context": "Figure 1: Broad inventory declines 19% in 2024-25"
  },
  {
    "figure_id": "F351",
    "report_id": "R016",
    "label": "Figure 2",
    "context": "Figure 2: Accumulated GFA started but not sold declined to 1.9bn sqm as of end-2025 from 2.5bn sqm as of end-2023"
  },
  {
    "figure_id": "F352",
    "report_id": "R016",
    "label": "Figure 3",
    "context": "Figure 3: 19 cities had a $10\\%$ -plus inventory decline in the past 12 months"
  },
  {
    "figure_id": "F353",
    "report_id": "R016",
    "label": "Figure 4",
    "context": "Figure 4: Developers' completed homes for sale continue to increase"
  },
  {
    "figure_id": "F354",
    "report_id": "R016",
    "label": "Figure 5",
    "context": "Figure 5: Chongqing leads in announcing to buy back land, accounting for $16\\%$ of land area sold in 2019-24"
  },
  {
    "figure_id": "F355",
    "report_id": "R016",
    "label": "Figure 6",
    "context": "Figure 6: Issuance of special bonds for land buyback should accelerate, according to the seasonality in 2025"
  },
  {
    "figure_id": "F356",
    "report_id": "R016",
    "label": "Figure 8",
    "context": "Figure 8: SOE developers' forward PE (x)"
  },
  {
    "figure_id": "F357",
    "report_id": "R016",
    "label": "Figure 9",
    "context": "Figure 9: SOE developers' NAV discount (%)"
  },
  {
    "figure_id": "F358",
    "report_id": "R016",
    "label": "Figure 10",
    "context": "Figure 10: 2026 YTD share price performance"
  },
  {
    "figure_id": "F359",
    "report_id": "R016",
    "label": "Figure 11",
    "context": "Figure 11: SOE developers' trailing PB (x)"
  },
  {
    "figure_id": "F360",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "Note: Priced as of 14 May 2026. # Sector highlights Exhibit 2. China EV market: Top 10 EV makers took $71\\%$ market share in 4M26"
  },
  {
    "figure_id": "F361",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3. China ICE car market: Top 10 brands took $73\\%$ share in 1Q26"
  },
  {
    "figure_id": "F362",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Top 10 took 73% market share in 1Q26 (vs 72% in 2025, 71% in 2024). Long tail: 69 brands are competing for the remaining 27% of the market (vs. 74 brands in 2025, 82 brands in 2024). Exhibit 4. China overall passenger car market: Top 15 brands took $62\\%$ shar"
  },
  {
    "figure_id": "F363",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Long tail: 138 brands are competing for the remaining 38% of the market (vs. 145 brands in 2025, 150 brands in 2024) # Most frequently discussed charts of the month Exhibit 5. China passenger car export volume booked $69\\%$ y-o-y growth in 4M26 China PC export"
  },
  {
    "figure_id": "F364",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6. Chery, BYD and Geely lead China's passenger car export volume in 4M26"
  },
  {
    "figure_id": "F365",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7. EV penetration rate rose to 61% in April 2026"
  },
  {
    "figure_id": "F366",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8. Overall auto retail sales decreased 21% y-o-y in April 2026"
  },
  {
    "figure_id": "F367",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "The chart includes a bar chart (red) and a line chart (gray). The data is already in English. The labels 'Jan' through 'Dec' appear above the bars. The percentage change indicators are shown above each bar. Exhibit 9. Geely is the top share gainer in the China"
  },
  {
    "figure_id": "F368",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10. Passive mix uplift in premium segment due to low-end slump in 1Q26"
  },
  {
    "figure_id": "F369",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "Exhibit 11. China EV sales volume booked -17% y-o-y decline in 4M26"
  },
  {
    "figure_id": "F370",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 12. In 4M26, BEV mix in China EV sales volume increased to 64%"
  },
  {
    "figure_id": "F371",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "Exhibit 13. China's EV passenger vehicle discount level rises slightly m-o-m to $10.9\\%$ in April 2026"
  },
  {
    "figure_id": "F372",
    "report_id": "R017",
    "label": "Exhibit 14",
    "context": "Exhibit 14. China's ICE passenger vehicle discount level decreased m-o-m to $22.1\\%$ in April 2026"
  },
  {
    "figure_id": "F373",
    "report_id": "R017",
    "label": "Exhibit 15",
    "context": "Exhibit 15. New model launches expected to peak in 2Q26 and 4Q26"
  },
  {
    "figure_id": "F374",
    "report_id": "R017",
    "label": "Exhibit 16",
    "context": "Exhibit 16. EVs account for c90% of new models in 2026e"
  },
  {
    "figure_id": "F375",
    "report_id": "R017",
    "label": "Exhibit 17",
    "context": "Exhibit 17. Inventory indicator decreased to 1.89 in April 2026"
  },
  {
    "figure_id": "F376",
    "report_id": "R017",
    "label": "Exhibit 18",
    "context": "Exhibit 18. Inventory alert index: 62.1% in April 2026 vs 57.5% in March 2026"
  },
  {
    "figure_id": "F377",
    "report_id": "R017",
    "label": "Exhibit 19",
    "context": "Exhibit 19. Lithium carbonate price increased $21\\%$ in last one month"
  },
  {
    "figure_id": "F378",
    "report_id": "R017",
    "label": "Exhibit 20",
    "context": "Exhibit 20. Battery cell pricing has been largely flat in last one month"
  },
  {
    "figure_id": "F379",
    "report_id": "R017",
    "label": "Exhibit 21",
    "context": "Exhibit 21. China's EV battery installations increased $15\\%$ y-o-y in April 2026"
  },
  {
    "figure_id": "F380",
    "report_id": "R017",
    "label": "Exhibit 22",
    "context": "Exhibit 22. LFP's share of China's EV battery market was $80\\%$ in 4M26"
  },
  {
    "figure_id": "F381",
    "report_id": "R017",
    "label": "Exhibit 23",
    "context": "Exhibit 23. CATL: $47\\%$ share of China's EV battery market in 4M26"
  },
  {
    "figure_id": "F382",
    "report_id": "R017",
    "label": "Exhibit 24",
    "context": "Exhibit 24. CATL: $40\\%$ share of China's LFP EV battery market in 4M26"
  },
  {
    "figure_id": "F383",
    "report_id": "R017",
    "label": "Exhibit 25",
    "context": "# Where we are in terms of valuation Exhibit 25. NIO, XPeng, and Li Auto trade at 0.6x, 0.9x, and 0.9x 12-month forward P/S multiples, respectively"
  },
  {
    "figure_id": "F384",
    "report_id": "R017",
    "label": "Exhibit 26",
    "context": "Exhibit 26. H-share OEMs trade at a 0.77x 12-month forward PB multiple"
  },
  {
    "figure_id": "F385",
    "report_id": "R017",
    "label": "Exhibit 27",
    "context": "Exhibit 27. China passenger car and EV demand forecast change Exhibit 28. We estimate $10\\%$ EV demand growth in 2026, with penetration at $62\\%$"
  },
  {
    "figure_id": "F386",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Chart of the week – China: Monthly Coal Production"
  },
  {
    "figure_id": "F387",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "Exhibit 3: MSCI China vs. Retail Sales Exhibit 4: China Retail Sales by Category Exhibit 6: Online Retail Sales"
  },
  {
    "figure_id": "F388",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: MSCI China vs. Retail Sales Exhibit 4: China Retail Sales by Category Exhibit 6: Online Retail Sales"
  },
  {
    "figure_id": "F389",
    "report_id": "R021",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China Retail Sales by Category Exhibit 6: Online Retail Sales"
  },
  {
    "figure_id": "F390",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Discretionary Categories"
  },
  {
    "figure_id": "F391",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Retail Sales Growth"
  },
  {
    "figure_id": "F392",
    "report_id": "R021",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Restaurants & Dining"
  },
  {
    "figure_id": "F393",
    "report_id": "R021",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Staples Categories"
  },
  {
    "figure_id": "F394",
    "report_id": "R021",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Discretionary as a % of 2019"
  },
  {
    "figure_id": "F395",
    "report_id": "R021",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Office & Mobile Categories Office & Mobile"
  },
  {
    "figure_id": "F396",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Staples as a % of 2019"
  },
  {
    "figure_id": "F397",
    "report_id": "R021",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Other Categories # Disclosure Section For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morga"
  },
  {
    "figure_id": "F398",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary weekly unit sales and four-week moving average - Total 50 cities"
  },
  {
    "figure_id": "F399",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Fuel Prices in Asia and Refinery implications Exhibit 2: India Diesel Price Build-up after the fuel price hikes Price Build up - Diesel"
  },
  {
    "figure_id": "F400",
    "report_id": "R028",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Agentic AI can be trained... it therefore has a bigger ego than Generic AI and AI Agents ```mermaid graph TD"
  },
  {
    "figure_id": "F401",
    "report_id": "R028",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The largest LLMs can still be compared to four-year old children (according to Bruno Patino)... Cartoon illustration of a smiling boy with brown hair and large eyes (no text or symbols)"
  },
  {
    "figure_id": "F402",
    "report_id": "R028",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: ... even if large LLMs are thirsty (for energy, knowledge and maybe self-recognition?). From 10^18 towards 10^26 flops and beyond.... Data on AI models"
  },
  {
    "figure_id": "F403",
    "report_id": "R028",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: ... subsurface leader Viridien is trying hard to cope... its computing power is now 690 x 10^15 flops"
  },
  {
    "figure_id": "F404",
    "report_id": "R028",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Poetic cartoon. How Perplexity rightly factors in the continuing rise of: 1) offshore developments (rigs, drilling systems); 2) LNG transportation (e.g. the spheric LNGC); and 3) interconnections (pipelines, solar pannel"
  },
  {
    "figure_id": "F405",
    "report_id": "R028",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: AI applications are poised to have a higher impact in 1) resource management and 2) operational optimisation EXHIBIT 10: AI applications in oilfield operations ```mermaid graph TD"
  },
  {
    "figure_id": "F406",
    "report_id": "R028",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: AI use-case assessment for Oil & Gas. SLB and Viridien main business lines put them in the “likely wins” top right part of the chart."
  },
  {
    "figure_id": "F407",
    "report_id": "R028",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: AI use-case scorecard for Oil & Gas: Highest positive revenue impact for Artificial lift, Crude selection, Equipment performance, Field Development Planning, Product Mix Optimization and Well Performance and Production O"
  },
  {
    "figure_id": "F408",
    "report_id": "R028",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: IT spending in the O&G industry: \\$45bn in 2025. This is expected to grow 7.4% CAGR up to 2029. We expect the war in Iran to boost these numbers (particularly for E&P)."
  },
  {
    "figure_id": "F409",
    "report_id": "R028",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: IT spending in the O&G industry: refining spending is higher (\\$25bn) than E&P spending (\\$19bn) - but E&P spending should grow faster (8% CAGR)."
  },
  {
    "figure_id": "F410",
    "report_id": "R028",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: AI adoption is still in its early stages in the O&G industry. Only 13% of O&G groups have already deployed AI agents and 49% plan to do it in 2026. However, they are not yet fully decision-making agents, but use GenAI an"
  },
  {
    "figure_id": "F411",
    "report_id": "R028",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Immersive technologies (Virtual Reality, Augmented Reality, Mixed Reality, Digital Twins, Simulation Twins, Spatial Computing...) are still to be deployed at large scale. 42% of respondents to Gartner's annual survey are"
  },
  {
    "figure_id": "F412",
    "report_id": "R028",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Dating. Could IT (= technology backbone of an enterprise) and OT (= hardware + software + processes behind physical operations) work more closely in the O&G world? This has historically never been the case...but things a"
  },
  {
    "figure_id": "F413",
    "report_id": "R028",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: 66% of O&G companies deployed have deployed hybrid cloud infrastructure. 57% of them have introduced industry specific cloud platforms. Edge computing remains limited at 28%."
  },
  {
    "figure_id": "F414",
    "report_id": "R028",
    "label": "Exhibit 10",
    "context": "EXHIBIT 19: State of deployment of AI agents"
  },
  {
    "figure_id": "F415",
    "report_id": "R028",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: According to McKinsey, the Oil Services industry could increase its overall EBITDA by c.\\$12-20bn “by scaling AI diligently”. This is consistent with our previous findings."
  },
  {
    "figure_id": "F416",
    "report_id": "R028",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: 2025 adoption fell massively short of expectations Gen AI adoption, expectations vs reality, $^{1}$ % of respondents 2023 expectations by 2025"
  },
  {
    "figure_id": "F417",
    "report_id": "R028",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Digital & O&G: three series of challenges - data complexity, organizational / stakeholder constraints, and infrastructure & geography. # Data complexity - Wide range from technical (drilling, seismic, sensors) to compl"
  },
  {
    "figure_id": "F418",
    "report_id": "R028",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Our representation of SLB's digital capabilities resembles a six-layer digital city: Operational + Infrastructure + Platform + Application + Innovation + the Cognitive layer (provided by Tela, SLB's new agentic AI platfo"
  },
  {
    "figure_id": "F419",
    "report_id": "R028",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: The differences between generic AI, AI agents, and agentic AI lie in their internal architecture ```mermaid graph TD"
  },
  {
    "figure_id": "F420",
    "report_id": "R028",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: In essence, Tela is akin to a digital orchestrator, specifically trained for the O&G industry ```mermaid graph TD"
  },
  {
    "figure_id": "F421",
    "report_id": "R028",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: Seismic in three phases: 1) first, data collection (through a vessel); 2) second, data processing and; 3) third, final image. ```mermaid graph LR"
  },
  {
    "figure_id": "F422",
    "report_id": "R028",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: Seismic imaging has dramatically changed in the past 70 years. The most recent methodologies include multi-parameter FWI and FWI imaging"
  },
  {
    "figure_id": "F423",
    "report_id": "R028",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: Viridien's proprietary technology is Time-Lag TWI. Larger computing power allows new technologies to come to the market. Viridien's computer power has now reached c.700 PFLOPS"
  },
  {
    "figure_id": "F424",
    "report_id": "R028",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: Geoscience revenues have increased from c. \\$394m in 2021 to c.\\$580m in 2025, while the number of employees has only increased from 1,147 to 1,499..."
  },
  {
    "figure_id": "F425",
    "report_id": "R028",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 40: ...resulting in an increase from c.\\$286k revenue per employee to c.\\$387k revenue per employee (c.9% CAGR). In our view, this is a reflection of: 1) the integration of AI/ML models shifting scientists focus from low-val"
  },
  {
    "figure_id": "F426",
    "report_id": "R028",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: For DUG, committed compute represents c.50% of total HPC monthly billings, providing a recurring"
  },
  {
    "figure_id": "F427",
    "report_id": "R030",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # 1Q26 Market Share Data AMD and ARM continued to gain unit share over Intel in 1Q26. Intel's server MPU share was down 372 basis points QoQ from $58.7\\%$ in 4Q25 to $54.9\\%$ in 1Q26 on serv"
  },
  {
    "figure_id": "F428",
    "report_id": "R030",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. AMD gained revenue CPU share over Intel in 1Q26. Intel's server MPU revenue share was down 492 basis points QoQ from $58.7\\%$ in 4Q25 to $53.8\\%$ in 1Q26. AMD's server MPU revenue share was "
  },
  {
    "figure_id": "F429",
    "report_id": "R031",
    "label": "Exhibit1",
    "context": "Exhibit1: The gap between mega-cap tech's institutional weighting and its S&P 500 weighting narrowed in 1Q26. Average Institutional Portfolio Weighting"
  },
  {
    "figure_id": "F430",
    "report_id": "R031",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Of the large cap stocks we evaluate, NVDA, AAPL, MSFT, AMZN, and GOOGL are currently the most under-owned in actively managed portfolios vs. the S&P 500, while SNDK, STX, CRM, and LRCX are the most over-owned. Average Ac"
  },
  {
    "figure_id": "F431",
    "report_id": "R031",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Of the large cap stocks we evaluate, SNDK saw the gap between its institutional ownership and S&P 500 weighting increase the most by 57bps in 1Q (vs. 4Q), while KLAC saw the gap narrow by 30bps. Q/Q Change in Gap of Acti"
  },
  {
    "figure_id": "F432",
    "report_id": "R031",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The spread between the average active portfolio weighting vs. the S&P 500 widened Q/Q for AAPL, but narrowed for AMZN, META, GOOGL, NVDA, MSFT, and TSLA. \"Mag 7\" Average Active Portfolio Weighting vs. S&P 500 Weighting"
  },
  {
    "figure_id": "F433",
    "report_id": "R031",
    "label": "Exhibit 5",
    "context": "Software Average Active Portfolio Weighting vs. S&P 500 Weighting"
  },
  {
    "figure_id": "F434",
    "report_id": "R031",
    "label": "Exhibit 6",
    "context": "Exhibit 6: In semis, SNDK saw the largest increase in the spread between the average active vs. passive ownership Q/Q. Semis Average Active Portfolio Weighting vs. S&P 500 Weighting"
  },
  {
    "figure_id": "F435",
    "report_id": "R031",
    "label": "Exhibit 8",
    "context": "Exhibit 8: CSCO active institutional ownership weighting has remained relatively in-line with the S&P 500 over the last 5 years."
  },
  {
    "figure_id": "F436",
    "report_id": "R031",
    "label": "Exhibit 9",
    "context": "Exhibit 9: IBM's S&P 500 weighting vs active ownership upticked slightly by 3bps in 1Q26 Q/Q. IBM Average Active Portfolio Weighting vs. S&P 500 Weighting"
  },
  {
    "figure_id": "F437",
    "report_id": "R032",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China's Auto Export Breakdown by Region"
  },
  {
    "figure_id": "F438",
    "report_id": "R034",
    "label": "Exhibit 5",
    "context": "Exhibit 2: Apple: sustained buybacks coincided with material long-term outperformance"
  },
  {
    "figure_id": "F439",
    "report_id": "R034",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Apple: buybacks and dividends drove $\\sim 70\\%$ of excess compounded return vs. S&P proxy Apple's excess return vs. S&P"
  },
  {
    "figure_id": "F440",
    "report_id": "R034",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Continued outperformance from enhanced dividend payout ratio after Covid"
  },
  {
    "figure_id": "F441",
    "report_id": "R034",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Samsung's FCF and FCF yield Samsung"
  },
  {
    "figure_id": "F442",
    "report_id": "R034",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Hynix's FCF and FCF yield Hynix"
  },
  {
    "figure_id": "F443",
    "report_id": "R036",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect the optical engines attach rate per GPU to increase 10x in future configurations"
  },
  {
    "figure_id": "F444",
    "report_id": "R036",
    "label": "Exhibit 2",
    "context": "Exhibit 2: AI Transceivers global volume - Global market volume ('000 units)"
  },
  {
    "figure_id": "F445",
    "report_id": "R036",
    "label": "Exhibit 3",
    "context": "# Insights from Corning's Investor Day France's Soitec, a leader in manufacturing engineered substrates; Netherlands-based Besi, which develops leading edge assembly equipment; and Corning, the American multi-technology company (covered by Meta Marshall) seem "
  },
  {
    "figure_id": "F446",
    "report_id": "R036",
    "label": "Exhibit 5",
    "context": "Exhibit 5: How Soitec's Photonics SOI enables PIC ```mermaid graph TD"
  },
  {
    "figure_id": "F447",
    "report_id": "R036",
    "label": "Exhibit 6",
    "context": "Exhibit 6: TSMC Coupe increases power efficiency and reduces latency through hybrid bonding ```mermaid graph LR"
  },
  {
    "figure_id": "F448",
    "report_id": "R036",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Although transceivers are expected to show healthy growth... AI Transceivers global volume (m)"
  },
  {
    "figure_id": "F449",
    "report_id": "R036",
    "label": "Exhibit 8",
    "context": "Exhibit 8: ...the larger opportunity lies in the adoption of CPO"
  },
  {
    "figure_id": "F450",
    "report_id": "R036",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We expect the networking mix to move towards higher attach rates due to increasing CPO adoption"
  },
  {
    "figure_id": "F451",
    "report_id": "R036",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Soitec Photonic SOI revenue to accelerate towards CY28e and maintain strong growth thereafter Soitec Photonics SOI revenue ($m)"
  },
  {
    "figure_id": "F452",
    "report_id": "R036",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Besi hybrid bonding revenue Besi hybrid bonding revenue (€m)"
  },
  {
    "figure_id": "F453",
    "report_id": "R036",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Soitec bridge from previous to new PT"
  }
]