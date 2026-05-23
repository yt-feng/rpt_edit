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
    "title": "市场真正低估的不是AI需求，而是能源波动如何重塑因子定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是能源波动如何重塑因子定价\n\n2026年过半，发达市场股票投资者正面对一个看似矛盾的局面：AI资本开支以远超预期的速度扩张，能源价格却因地缘冲突频繁制造宏观噪音。两者叠加，市场对“买什么”的共识正在松动。某外资投行最新发布的量化权益中期展望给出了一个值得深思的判断：在AI与能源共同主导的周期里，因子的选择优先级高于区域的选择。换言之，未来12个月决定组合回报的核心变量，不是押注美国还是日本，而是你持有的因子是否匹配这个周期中成本结构、盈利质量和增长可持续性的再定价。\n\n这份报告的核心洞察是：当AI投资周期与能源波动周期交织时，市场会从“贝塔驱动的同涨同跌”转向“因子驱动的结构性分化”。美国、欧洲、日本三个市场虽然整体预期回报接近，但驱动因子完全不同。在AI capex带来的生产力红利与能源成本冲击之间，不同市场的企业暴露程度迥异，这意味着同一个因子在三个市场可能产生截然不同的效果。\n\n报告没有简单给出“买成长”或“买价值”的建议，而是基于宏观情景、通胀环境和油波动率，为每个市场推荐了具体的因子组合。这些推荐背后有一套四维评估框架，涵盖了经济周期、估值、质量和动量。其中最关键的变化是：欧洲的经济周期判断已经从“扩张”调整为“放缓”，这一调整直接重塑了该市场的因子排序。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国市场的核心矛盾不是增长放缓，而是增长质量的分化\n\n在美国，经济学家预测2026年实际GDP增速为2.2%，通胀从3.5%逐步回落，美联储维持利率不变至2027年上半年。这套宏观组合并不差，但报告真正关注的不是总量，而是结构。AI资本开支正在推动企业层面的生产力提升，但能源价格上升同时构成了对消费的“隐性税收”。两股力量叠加的结果是：企业之间盈利能力的差距在拉大。\n\n报\n\n[... middle omitted ...]\n\n的可行性、AI主题暴露度的时间稳定性——做更深入的专题分享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI重构周期下，三地股市该选什么因子？\n\n📌 量化选股框架升级\n\n全球AI资本开支+能源波动，让发达市场因子选择更分化：\n🇺🇸 美国：侧重自生增长和盈利兑现\n🇪🇺 欧洲：优先现金流韧性和资本纪律\n🇯🇵 日本：平衡价值与增长，关注利率\n\n---\n\n1️⃣ 美国：质量成长是主线\n\nAI生产力周期正在对冲能源成本压力。推荐三个因子：内部增长率、低PEG、上修/下修盈利修正比。\n\n内部增长率（留存率×ROE）是所有成长因子中质量暴露最强的。拆解ROE来看，高内部增长的公司利润率和资产效率更优，杠杆更低，正好匹配“跑得更瘦”的效率提升逻辑。\n\n油价高波动期，内部增长和低PEG表现稳健，而上修/下修盈利修正比会滞后，更适合油价稳定后。\n\n2️⃣ 欧洲：能源通胀下的防御选择\n\n欧洲对能源价格传导更快，央行反应函数也不同。推荐：经营性现金流收益率、低同比资产增长、3个月上修/下修盈利修正广度。\n\n现金流韧性和资本纪律是核心，同时要筛选盈利能见度高的公司。\n\n3️⃣ 日本：价值+增长的双重平衡\n\n日本股市受能源成本、工资增长、治理改革和AI/材料/国防等板块驱动。推荐：远期盈利收益率、低PEG、上修/下修盈利修正比。\n\n在利率\n\n[... middle omitted ...]\n\nd Up vs. Down EPS Revisions.   \nEurope: positioning for energy-driven inflation, we recommend Operating Cash Flow Yield, Low YoY Asset Growth Factor, and 3m Up vs. Down EPS Revisions.   \nJapan\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R002",
    "title": "半导体设备市场的真正转折：2000亿美元WFE在望，但驱动力已彻底改变",
    "digest": "[wechat_article.md]\n# 半导体设备市场的真正转折：2000亿美元WFE在望，但驱动力已彻底改变\n\n市场对半导体设备支出的讨论，长期集中在周期性波动和地缘政治扰动上。但某外资投行最新发布的深度研报揭示了一个更本质的判断：全球WFE（晶圆制造设备）支出将在2028年逼近2000亿美元，而这一轮增长的核心引擎，已经从“先进逻辑制程的军备竞赛”切换为“存储芯片的产能扩张”，尤其是DRAM领域的结构性重投入。\n\n这不是一个线性外推的乐观预测。报告将2026年WFE预测从1410亿美元上调至1480亿美元，2027年从1580亿美元上调至1750亿美元，2028年更是从1640亿美元大幅上调至1980亿美元——三年间的上调幅度逐级扩大，2028年的修正幅度高达21%。这意味着，研报作者看到的不是一次性的脉冲，而是一个正在加速的、多维度支撑的上升周期。\n\n对于产业决策者和投资者而言，真正需要追问的不是“WFE会不会到2000亿”，而是“这2000亿由谁花、花在哪里、哪些设备商能真正受益”。以下是我们从这份报告提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮WFE上修的核心驱动力是DRAM，而非逻辑制程\n\n过去几年，市场对半导体设备需求的关注焦点，几乎全部集中在台积电、三星、英特尔在先进逻辑制程上的资本开支。但这份报告的数据清楚地表明，逻辑/代工领域的WFE预测基本维持不变——2027年约890亿美元，同比增长8%，几乎没有任何上修。\n\n真正驱动预测上调的，是DRAM。报告将2027年DRAM WFE从480亿美元大幅上调至570亿美元，增幅接近20%。2028年DRAM的上修幅度更大，达到200亿美元。用报告原文的话来说，“上修主要来自DRAM，其次是NAND”。\n\n这一变化的含义是深刻的。逻辑制程的资本开支受制于先进节\n\n[... middle omitted ...]\n\n分享报告的完整解读和原始图表，并定期组织线上讨论。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体设备：2000亿美元市场在望\n\n封面：2000亿的半导体设备市场\n副标题：全球WFE预测持续上调\n\n最近在读一份某外资投行的半导体设备研报，数据更新得挺有意思，分享几个核心逻辑给大家参考。\n\n1/ 全球WFE规模持续上修\n研报把2026年WFE预测从1410亿上调到1480亿美元（+21%），2027年从1580亿上调到1750亿（+18%），2028年更是从1640亿大幅上调到1980亿（+13%）。这个上调幅度不小，主要驱动力来自存储芯片的扩产。\n\n2/ 存储是最大增量\nDRAM是这轮上调的核心。2027年DRAM WFE从480亿上调到570亿美元，增长预期从15%提到25%。NAND也有小幅上调，主要受存储上行周期影响。晶圆级封装从2025年的60亿增长到2028年的110亿。\n\n3/ 中国存储扩产提速\n研报对中国WFE需求的上调幅度很大：2026-2028年分别上调23/67/161亿美元。长江存储和长鑫存储的产能扩张信号更积极了。长鑫要支持未来本地HBM制造，IPO后资金更充裕，扩产节奏会加快。长存同样受益于NAND上行周期。\n\n4/ 设备商受益排序\n研报对主要设备商都维持看好评级，但偏好排\n\n[... middle omitted ...]\n\n8a4252b18a4cb6f2.jpg)\n\nMark Li\n\n+852 2123 2645\n\nmark.li@bernsteinsg.com\n\n![](images/ae2142925d872878cb2fda7e406b664f40a314a8ddd6697d83166494276eb7bf.jpg)\n\nJuho Hwang\n\n+852 2123 2632\n\njuho.hwan\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R003",
    "title": "黄金市场真正的短期压力不在需求，而在能源驱动的宏观逻辑切换",
    "digest": "[wechat_article.md]\n# 黄金市场真正的短期压力不在需求，而在能源驱动的宏观逻辑切换\n\n过去几个月，黄金价格在历史高位附近反复震荡，市场上关于“央行购金持续支撑金价”的叙事已经深入人心。但某外资投行最新发布的研报给出了一组值得警惕的信号：短期黄金面临的压力并非来自需求端的疲软，而是源于霍尔木兹海峡局势持续紧张所引发的能源通胀预期，以及由此带来的实际利率和美元走强。这份报告的核心判断是，市场当前的博弈焦点已经从“谁会继续买黄金”转向“宏观环境是否允许黄金继续涨”。\n\n报告将0-3个月黄金目标价设定为4300美元/盎司，并明确提示在风险事件冲击下，价格可能大幅低于这一水平。这不是一份看空黄金的长期报告，而是一份对短期节奏的清醒判断。对于持有黄金头寸或正在观察入场时机的投资者来说，理解当前的价格驱动力正在发生怎样的结构性切换，比盯着每盎司的波动数字重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 黄金与实际利率的负相关性正在回归，这才是短期定价的核心变量\n\n2022年至2024年，全球央行大规模购金推动了一轮脱离传统定价框架的黄金上涨行情。在那段时间里，黄金价格与美国实际利率之间的历史负相关性显著弱化——央行作为价格不敏感的需求方，打破了利率对金价的传导链条。但这份报告明确指出，随着非央行投资者参与度的回升，这一相关性已经恢复。截至今年以来的日度数据显示，黄金与5年期实际利率的平均相关系数已回落至-0.75，而2024年这一数值仅为-0.2。\n\n这意味着什么？意味着黄金正在重新变成一个对利率和美元高度敏感的资产。当霍尔木兹海峡局势推高能源价格，市场开始定价美联储加息预期时，实际利率上升和美元走强会直接对黄金形成压力。这不是一个关于需求是否充足的问题，而是一个关于定价锚是否正在发生位移的问题。对于资产管理者而言，这意味着过去两年那种“\n\n[... middle omitted ...]\n\n跌的投资者来说，这些细节才是真正构建判断力的基石。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n黄金短期承压，但中国买盘依然凶猛\n\n短期波动，长期逻辑不变\n\n最近黄金市场有点纠结。一方面霍尔木兹海峡持续关闭推高了能源价格，市场担心通胀失控，投资者开始避险式抛售黄金（历史上每次风险事件初期黄金都会被先卖一波）。另一方面，中国的黄金进口量依然维持在历史高位附近，年化约3000亿美元，这个数字放在疫情前几乎是全球黄金消费的总和。\n\n1️⃣ 短期压力来自哪里？\n投行研报给出的0-3个月目标价是4300美元/盎司，但警告如果出现大规模风险事件（比如美伊局势再度升级），金价可能跌到更低。核心逻辑是：能源价格持续高企→市场预期美联储加息→实际利率上升+美元走强→黄金承压。有意思的是，2022-2024年央行主导的黄金牛市期间，金价和美国实际利率的负相关性被严重削弱，但现在随着非央行投资者重新入场，这个负相关性已经恢复到了-0.75（2025年还是-0.65，2024年只有-0.2）。\n\n2️⃣ 中国在做什么？\n4月海关数据显示，非货币黄金进口虽然较3月高点略有回落，但同比仍增长25%，按价值计算更是飙升83%。一季度中国黄金表观需求（apparent demand）按价值计算创下历史新高，主要驱动力是零售金条和金币需\n\n[... middle omitted ...]\n\n during the pre-COVID years in today's dollars. This is supporting gold prices at elevated levels by historical standards, but is not changing the main delta which is lower investor demand, no\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R004",
    "title": "中国车企在欧洲的真正突破，不在销量，而在结构",
    "digest": "[wechat_article.md]\n# 中国车企在欧洲的真正突破，不在销量，而在结构\n\n2026年3月，中国车企在欧洲市场单月销量达到189,750辆，同比增长60%。这个数字本身已经足够让人侧目。但真正值得关注的，不是总量，而是结构：英国市场单月贡献超过5.7万辆，同比增长117%；意大利突破2.1万辆，同比增长116%；德国虽然绝对量仍然不高，但同比增速达到127%。\n\n这是一份某外资投行最新发布的月度追踪报告给出的核心数据。它揭示了一个正在发生的结构性变化——中国车企在欧洲的渗透，已经从“边缘试探”进入“核心市场突破”阶段。而这一轮突破的驱动力，正在从成本优势转向品牌认知和渠道能力的系统性提升。\n\n以下，是我们基于这份报告数据所做的深度解读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 英国市场的爆发，正在重塑中国车企的欧洲叙事\n\n这份报告最值得关注的数据点，不在德国，不在法国，而在英国。\n\n2026年3月，中国车企在英国的单月销量达到57,543辆，同比增长117%，环比更是暴增438%。即便考虑到英国3月本身就是传统销售旺季，这个增速仍然远超整体欧洲市场60%的平均水平。更关键的是，中国车企在英国的市场份额已经从2025年初的6%攀升至2026年3月的15%。\n\n这意味着什么？英国是中国车企在欧洲最大的单一市场，且增长没有减速迹象。\n\n从品牌分布来看，Chery是英国市场的最大赢家，市场份额达到5.9%，SAIC和BYD分别以3.9%和3.5%紧随其后。这三家车企合计占据了英国市场超过13%的份额，已经超过了许多传统欧洲品牌在当地的市占率。\n\n英国市场的特殊性在于：它是一个右舵市场，与日本、澳大利亚、印度、东南亚等右舵市场形成天然协同。中国车企在英国的成功，本质上是在验证一套“右舵市场可复制”的扩张模型。这份报告没有明确展开这一点，但逻\n\n[... middle omitted ...]\n\n行业洞察，帮助你在信息过载的时代，抓住真正重要的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 中国车在欧洲，3月卖了近19万辆\n\n**中国车企欧洲月报**\n\n**3月销量创下新高**\n\n---\n\n最近翻到一份某外资投行刚出的研报，追踪中国车企在欧洲的月度销量。3月的数据有点意思，和大家聊聊。\n\n**1/ 总量：3月卖爆了，单月近19万辆**\n\n3月中国车企在欧洲一共卖了189,750辆，同比增60%，环比也涨了近70%。一季度累计41万辆，同比+40%。\n\n这个增速，放在欧洲整体市场只涨了11%的背景下看，确实很猛。\n\n**2/ 市占率：从7%到11%，只用了1年多**\n\n去年初中国品牌在欧洲市占率不到8%，今年3月已经到10.8%。虽然中间有小波动，但趋势是向上的。\n\n目前整个欧洲市场，中国品牌已经占到约11%的份额。每卖出10辆车，就有1辆是中国品牌。\n\n**3/ 谁在撑场面？奇瑞、SAIC、比亚迪三强**\n\n按品牌分，3月卖得最好的是：\n- 奇瑞：50,256辆，同比+83%\n- SAIC：39,836辆（增速较慢，+2%）\n- 比亚迪：38,364辆，同比+112%\n\n这三个品牌占了总量的近70%。比亚迪的翻倍增长很亮眼，奇瑞基数大还能保持高增速。\n\n**4/ 爆发力选手：零跑同比增长75\n\n[... middle omitted ...]\n\n-7057\n\nFigure 1: Chinese OEMs European market volume by country \n\n<table><tr><td colspan=\"6\">Chinese OEM European Volume by Country</td></tr><tr><td>(unit)</td><td>Mar-26</td><td>YoY</td><td>M\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R005",
    "title": "四月数据“惊吓”背后，市场真正需要关注的不是疲弱，而是政策空间的重新定价",
    "digest": "[wechat_article.md]\n# 四月数据“惊吓”背后，市场真正需要关注的不是疲弱，而是政策空间的重新定价\n\n对于关注中国宏观的投资者来说，四月的经济数据无疑是一次冲击。工业增加值、零售、固定资产投资全面低于预期，其综合偏离程度创下2023年5月以来之最。市场第一反应往往是担忧增长动能是否正在急剧恶化。\n\n但某外资投行最新研报给出一个值得细品的判断：数据本身并非看上去那么糟糕，真正的关键变量在于政策制定者对经济状态的评估已经发生变化，而这将决定未来几个月的资产定价逻辑。这份报告没有停留在“经济好坏”的表层判断，而是试图拆解数据背后的结构性因素与政策意图。其核心主张可以概括为一句话：市场真正需要关注的不是四月数据有多差，而是政策空间还有多大、以及何时会被重新激活。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 工业数据的“一半真相”：能源冲击与统计噪音的叠加\n\n四月工业增加值同比增速从三月的5.7%骤降至4.1%，低于市场预期约2个百分点。乍看之下，这是需求急剧萎缩的信号。但研报通过拆解产品层面的产出数据，给出了一个更为精细的归因。\n\n左侧的“底部十项”清单清晰地指向了能源密集型行业：乙烯、化学纤维、加工原油的产量环比出现最大幅度的下滑。这并非偶然。四月份中东局势的升级与能源价格的攀升，直接冲击了中国化工和炼化环节的生产活动。报告估算，仅能源供给冲击一项，就可以解释工业增加值约1个百分点的下滑。\n\n而右侧的“顶部十项”则揭示了另一番景象：工业机器人、风力发电、新能源车的产量环比增长显著。这并非简单的“新旧经济分化”，而是说明中国制造业的韧性并非均匀分布，而是在政策扶持和产业升级方向上的集中体现。\n\n更值得玩味的是，报告提出了一个“残差季节性”假说。2025年的数据显示，工业增加值在季度末月份（三月、六月、九月）的环比增长往往偏强，而在季度初月份\n\n[... middle omitted ...]\n\n沿着这些未解问题，把完整的报告逻辑和潜在的投资含义梳理清楚。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月数据不及预期，但不必太焦虑\n\n数据有“噪音”，别急着下结论\n\n4月经济数据确实不太好看——工业增加值、社零、固投都低于预期。但仔细拆开看，很多是短期扰动，不是趋势恶化。\n\n🔹 工业：一半是外部冲击，一半是统计噪音\n4月工业增加值同比4.1%，比预期低了约2个百分点。仔细看细分品类：\n- 化学制品、石油加工品产量环比下降最明显——这和中东局势、能源价格走高有关，研报估算这部分拖累约1个百分点\n- 工业机器人、风电设备产量环比增长最快——高端制造和新能源趋势没变\n另外，去年数据显示，工业增加值在季末月（3月、6月、9月）环比偏强，次月（4月、7月、10月）偏弱，可能是企业赶季度GDP数据造成的“残余季节性”。如果今年也这样，那剩下1个百分点的拖累可能是统计性的，接下来两个月会消退。\n\n🔹 社零：政策“透支效应”在显现\n4月社零同比仅0.2%，是2022年以来的最低值。但主要原因是：\n- 政府“以旧换新”补贴拉动了汽车、家电的集中替换需求，现在进入“还债期”——家电销售从去年5月的+53%降到今年4月的-15%\n- 新能源车购置税从0%恢复到5%，导致汽车销量明显下滑\n这些更多是政策节奏问题，不是消费意愿的急剧\n\n[... middle omitted ...]\n\nby around 2pp in April. Chemicals and processed petroleum products showed the largest sequential declines in physical output, pointing to the negative impact of the energy-supply shock. We est\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "市场真正低估的不是AI需求，而是新兴市场的采纳速度",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是新兴市场的采纳速度\n\n过去两年，全球投资者对人工智能的讨论几乎都围绕着一个核心叙事：发达经济体将率先受益，新兴市场只能缓慢跟进。某外资投行的最新研报对此提出了一个值得重新审视的判断——这个假设可能正在过时。\n\n该行此前预测，AI将在未来十年为新兴市场每年带来约4%的生产率提升，但这个数字不到其对发达经济体预测的一半。支撑这一差距的核心逻辑有两条：一是新兴市场在技术采纳上历来滞后于发达经济体；二是新兴市场的劳动力更多集中在生产岗位，受AI自动化影响较小。然而，最新数据正在挑战这两个前提。\n\n这份研报的核心贡献不在于给出一个更乐观的数字，而在于揭示了一个结构性的变化：AI技术的采纳周期正在被压缩，而新兴市场可能因此获得超出传统自动化框架的收益。这不是一个简单的“追赶上”的故事，而是一个“跳跃式”的可能性——新兴市场在AI应用上可能跳过某些发展阶段，直接进入前沿应用。\n\n对于关注全球资产配置和产业趋势的决策者而言，这不仅仅是一个宏观预测的修正。它意味着，那些基于“AI红利主要属于发达国家”的投资框架，可能需要重新校准。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 采纳滞后从五年缩至三年，证据来自微软和OECD的微观数据\n\n传统上，新兴市场在技术采纳上落后发达经济体5年左右。这个数字并非凭空而来，而是基于过去数十年的技术扩散模式。但研报引用的两组数据表明，AI的采纳节奏正在打破这一规律。\n\n第一组数据来自微软的调查。截至2025年下半年，新兴市场的AI产品使用率平均为22%，仅落后发达经济体的37%约15个百分点。更重要的是，全球AI采纳率正以每年约5个百分点的速度上升。按照这个速率，新兴市场与发达经济体之间的采纳差距约为3年，而非此前假设的5年。\n\n第二组数据更为关键。OECD的统\n\n[... middle omitted ...]\n\n深度讨论。群里没有广告，只有持续的信息更新和坦诚的观点碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n海外新兴市场的AI追赶，可能比想象中快\n\nAI追赶速度，比预期快3年\n\n某外资投行最新研报指出，新兴市场在AI领域的追赶速度可能被低估了。原本预测新兴市场要落后发达市场5年，但现在看，这个差距可能只有3年。\n\n1/ 低成本+开源模型，正在改变游戏规则\n特别是来自中国的开源模型，让新兴市场的AI普及速度明显加快。微软数据显示，新兴市场的AI采用率（22%）已经快追上发达市场（37%），而且全球采用率每年还在以5个百分点的速度增长。\n\n2/ 数字技术的“跳跃式发展”更明显\n世界银行的数据有个有意思的发现：新兴市场企业在数字化的新业务领域，更愿意直接跳到最前沿的技术。比如云服务这块，新兴市场企业采用率（41%）和发达市场（48%）的差距已经很小了。\n\n3/ 医疗领域已经看到效果\n早期案例挺惊艳的：\n- 死产和新生儿死亡率下降75%\n- 宫颈癌筛查准确率提升64%\n- 结核病检测量减少50%\n- 疟疾检测率提升36%\n- 孕产妇死亡率下降27%\n\n如果这些效果能规模化，光医疗这一块，就能给新兴市场的劳动力供给带来5%的提升。\n\n4/ 对GDP的影响\n如果采用周期真的缩短到3年，未来10年新兴市场的GDP可能额外获得6\n\n[... middle omitted ...]\n\n AI adoption lag than previously assumed. This is consistent with recent technology cycle trends where DM-EM adoption lags have been compressed, particularly for ICT-related technologies.\n\nThe\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "中国补库压力被市场低估，TTF和JKM的上行风险正在积聚",
    "digest": "[wechat_article.md]\n# 中国补库压力被市场低估，TTF和JKM的上行风险正在积聚\n\n当大部分市场参与者的目光仍聚焦在霍尔木兹海峡的短期扰动时，一份来自某外资投行的最新天然气研报揭示了一个更值得关注的底层逻辑变化：**中国天然气需求虽然疲弱，但去库存的速度已经导致储气量同比转负，这意味着下半年LNG进口量必须显著回升才能为冬季做准备。** 这不是一个乐观的需求故事，而是一个被市场低估的供给侧再定价信号。\n\n市场当前对欧洲天然气TTF价格的预测区间普遍在44-40欧元/兆瓦时，但该投行的情景分析显示，如果霍尔木兹海峡的流量正常化推迟至7月下旬（基准假设是6月底），TTF价格可能分别上行至65和53欧元/兆瓦时。这个风险溢价并非来自地缘政治的随机波动，而是来自亚洲——特别是中国——即将到来的结构性补库需求。\n\n报告的框架并不复杂，但它的洞察力在于将三个看似独立的变量串联起来：中国储气数据的同比转负、全球LNG装船量的暂时性支撑、以及亚洲与欧洲之间的价差套利机制。当这些变量同时发生作用时，市场的平衡点正在移动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国4月储气量同比转负，这是近几年来首次出现的信号\n\n中国4月的天然气表观需求同比微降，年化水平约为3790亿立方米，低于该投行预期的3870亿立方米。这一偏差与中国4月整体经济活动的疲弱是一致的——工业增加值增速从3月的5.7%降至4.1%，而天然气密集型化工行业（根据IEA数据，2023年该行业消耗约400亿立方米天然气，折合2900万吨LNG）是拖累需求的主要领域之一。\n\n但关键不在于需求本身，而在于供需的边际缺口。尽管需求疲弱，4月中国的LNG进口量仍远低于去年同期水平，同时国产气产量和管道气进口量也低于预期。三者叠加的结果是：中国地下储气库在4月的注气量低于预期，导致储气量同比\n\n[... middle omitted ...]\n\n中受益。如果你对这些问题感兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国天然气去库加速，夏季LNG进口压力隐现\n\n天然气市场正在微妙变化\n\n最近某外资投行发布了一份天然气研报，核心逻辑很清晰：中国4月天然气需求同比小幅下滑，但库存却意外走低，这意味着接下来几个月LNG进口量可能要明显增加。\n\n1️⃣ 需求弱但去库仍在继续\n4月中国表观天然气需求379Bcm/y，同比微降，比预期低了8Bcm/y。工业产出增速从5.7%降到4.1%，化工行业是主要拖累（该行业2023年消耗约40Bcm天然气）。但即便需求偏弱，库存却出现多年来的首次同比下降——因为LNG进口、国内产量和管道气都低于预期。\n\n2️⃣ 夏季补库压力推高进口\n库存同比走低意味着，为了在下一个冬季前把库存拉回正常水平，中国需要在夏季增加LNG进口。5月的高频数据已经显示，中国LNG进口正在加速追赶去年水平。同时，亚洲LNG价格（JKM）相对欧洲（TTF）的溢价持续走强，这会吸引更多美国LNG船货从大西洋转向太平洋。\n\n3️⃣ 全球供给端的小意外\n一些LNG出口国（如马来西亚、阿曼、安哥拉）今年夏天似乎推迟或跳过了检修，全球LNG装载量在伊朗冲突以来首次同比转正。但这种做法不可持续，而且即便如此，西北欧的LNG进口仍在同比\n\n[... middle omitted ...]\n\nur expectations by 8 Bcm/y, consistent with the broader miss in China activity data for the month (Exhibit 1). Industrial production growth fell to $4.1\\%$ yoy in April from $5.7\\%$ yoy in Mar\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R008",
    "title": "中国环氧树脂出口的真正信号：价格弹性正在取代规模弹性",
    "digest": "[wechat_article.md]\n# 中国环氧树脂出口的真正信号：价格弹性正在取代规模弹性\n\n如果你只看中国环氧树脂4月的出口量，25.6千吨，同比上升9%，你会得出一个结论：需求在回暖，出口在恢复。\n\n但如果你同时看价格，4月平均出口价格每吨2560美元，环比上升13.4%，同比上升24.6%，而且这是连续第二个月量价齐升，你会意识到，这个市场正在发生比“需求复苏”更深刻的结构性变化。\n\n真正被低估的，不是中国环氧树脂的出口量能恢复到什么水平，而是中国厂商正在从“以量换价”的出口模式，转向“以价定量”的新均衡。这种转变一旦确立，将重新定义全球环氧树脂的定价权分布和竞争格局。\n\n某外资投行最新发布的4月中国环氧树脂进出口数据，恰好提供了观察这一转变的关键窗口。报告覆盖了2017年至2026年4月的完整进出口时间序列，数据颗粒度精细到月度。但比数据本身更重要的，是这些数字叠加在一起所揭示的行业逻辑——中国环氧树脂的净出口红利期正在收窄，但出口价格的弹性正在打开。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月的量价齐升不是偶然反弹，而是供给端主动收缩后的定价权修复\n\n4月出口量25.6千吨，同比仅增长9%，但出口价格同比跳升24.6%。更值得注意的是，2026年前四个月的累计出口量84.2千吨，同比反而下降了2.5%。这意味着，4月的单月增长并没有改变全年出口量收缩的趋势。\n\n这是理解当前市场最关键的一步：出口量的收缩发生在价格大幅上涨的背景下。这不是需求驱动的价格上涨，而是供给端主动或被动收缩后，剩余产能获得了更强的议价能力。\n\n回顾2024年，中国环氧树脂全年出口261.6千吨，同比增长51.4%，但出口价格全年维持在每吨2000美元左右的低位。那是典型的“以量换价”——中国厂商用巨大的出口量增长，弥补了单吨利润的压缩。2025年出口量小幅\n\n[... middle omitted ...]\n\n会有定期的专题讨论和实时数据跟踪，帮助你构建自己的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n环氧树脂4月出口：量价齐升，但净出口在缩水\n\n📦 出口量价齐升\n📈 净出口却在收窄\n\n最近读到某外资投行关于中国环氧树脂的研报，4月数据有点意思，分享几个关键点👇\n\n**1️⃣ 出口量同比回升，但累计仍下滑**\n4月出口2.56万吨，同比+8.9%，是今年首次单月正增长。但1-4月累计出口8.42万吨，同比-2.5%，说明前几个月基数较低。\n\n**2️⃣ 进口量也在涨，净出口收窄明显**\n4月进口1.34万吨，同比+10.7%。1-4月累计进口5.12万吨，同比+20.6%。净出口3.29万吨，同比-25%，是2023年以来最低水平。2023年全年净出口才1.3万吨，2024年就跳到12万吨，今年明显在回归。\n\n**3️⃣ 出口价格跳涨，进口价格同步走高**\n4月出口均价2560美元/吨，环比+13.4%，同比+24.6%。3月均价2258美元，去年4月才2055美元。进口均价4715美元，环比+5.1%，同比+6.7%。出口价格涨幅远大于进口，说明低价出货的格局在改善。\n\n**4️⃣ 历史趋势：中国从净进口到净出口**\n2017-2022年，中国一直是环氧树脂净进口国，每年净进口量在9.6万-35.8万吨之\n\n[... middle omitted ...]\n\nod last year.   \n- The April average export price of \\$2,560/t increased 13.4% sequentially and 24.6% y/y. The average export price per ton in March was \\$2,258/t, and prices averaged \\$2,055/\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 20 May 2026 01:28 PM EDT\n\nDisseminated 20 May 2026 01:35 PM EDT"
  },
  {
    "id": "R009",
    "title": "中国甲醇贸易的拐点信号：出口定价权正在超越进口依赖",
    "digest": "[wechat_article.md]\n# 中国甲醇贸易的拐点信号：出口定价权正在超越进口依赖\n\n2026年4月的中国甲醇进出口数据，表面看是月度波动，实则揭示了一个被市场低估的结构性变化。当月进口量同比下降29%至56.3万吨，而出口量却同比飙升218%至17.3万吨。更关键的是价格信号：进口价格环比跳升32%至365美元/吨，出口价格同步上涨25%至483美元/吨。这不是简单的供需错配，而是中国甲醇产业链在全球贸易格局中的角色正在发生质变。\n\n这份来自某外资投行的研报，用海关数据勾勒出一个正在成形的趋势：中国正从甲醇的纯进口大国，转向兼具出口竞争力的定价参与者。对于关注化工品周期、能源转型和全球贸易再平衡的投资者而言，这组数据值得深挖。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 进口量收缩并非需求疲软，而是库存周期与供给替代的叠加效应\n\n4月进口量56.3万吨，同比下滑29%，但年初至今累计进口296.9万吨，仍比2025年同期高出4%。这说明单月数据不能简单解读为需求萎缩。更合理的解释是：3月进口量已降至43.8万吨的阶段性低点后，4月环比回升29%，显示进口节奏正在恢复。\n\n报告没有直接给出原因，但结合历史数据可以推断：2025年下半年至2026年初，中国甲醇进口价格持续走低，从2025年7月的279美元/吨降至12月的241美元/吨，这刺激了国内贸易商在低价时点集中补库。进入2026年，库存消化完毕后，进口量自然回升。4月进口价格跳涨32%，恰恰说明前期低价库存正在被高成本新货替代。\n\n这意味着，进口量的波动更多反映的是采购节奏和库存管理，而非终端需求的趋势性变化。对于甲醇下游的MTO、甲醛、醋酸等行业，真正的考验是能否将原料成本上涨传导至终端产品。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2\n\n[... middle omitted ...]\n\n研报的解读框架和关键图表，并持续跟踪后续月份的贸易数据变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n甲醇4月贸易数据：进口价格跳涨32%\n\n📈 价格冲高 出口放量\n\n**1/ 进口量降了，但价格涨了**\n4月中国甲醇进口56.3万吨，同比降29%，但环比3月回升29%。更值得关注的是进口均价——从3月的277美元/吨涨到365美元/吨，环比跳升32%，同比也高了22%。这背后是海外供应收紧还是国内需求阶段性走强？研报没有直接解释，但量缩价涨的格局值得跟踪。\n\n**2/ 出口意外放量，价格同步走高**\n4月甲醇出口17.3万吨，几乎是3月（6.6万吨）的2.6倍，去年同期仅5.4万吨。出口均价483美元/吨，环比涨25%，同比涨37%。出口量价齐升，可能反映海外市场阶段性补库或中国货源竞争力提升。\n\n**3/ 前4个月进口累计仍正增长**\n1-4月累计进口296.9万吨，同比增4%。虽然4月单月进口下滑，但年初至今总量并未走弱。如果后续进口价格维持高位，国内甲醇生产企业的议价空间可能被压缩。\n\n**一点思考：** 4月进出口价格双双走强，但进口量下降、出口量激增——这种“内外倒挂”的结构是否可持续？需要关注后续海外甲醇装置开工率及国内下游需求（如MTO、甲醛）的恢复节奏。\n\n#学习笔记\n\n[source_mi\n\n[... middle omitted ...]\n\nil 2026 and were 22% higher y/y. The average import price in 2025 was \\$279/t.\n\nChina exported 173kt of methanol in April 2026, a jump compared to 66kt in March 2026 and 54kt in April 2025. Ex\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 20 May 2026 02:51 PM EDT\n\nDisseminated 20 May 2026 02:52 PM EDT"
  },
  {
    "id": "R010",
    "title": "中国锂贸易正在经历一次定价权的结构性转移，而非周期波动",
    "digest": "[wechat_article.md]\n# 中国锂贸易正在经历一次定价权的结构性转移，而非周期波动\n\n这份报告的四月进出口数据，表面上是月度数据的更新，但放在2026年以来的连续趋势中看，它揭示了一个更根本的变化：中国正在从锂化工品的“净出口定价者”转向“净进口成本接受者”，而市场对这一身份转换的长期含义可能尚未充分定价。\n\n某外资投行的这份研报提供了截至2026年4月的完整进出口时间序列。数据本身并不复杂，但合在一起指向一个清晰的结论：锂行业的获利逻辑正在被重写，而过去几年形成的“中国供给过剩、价格承压”的叙事，可能低估了结构性的力量。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国氢氧化锂已从净出口国转为净进口国，这一身份转换的定价含义远未被消化\n\n2026年前四个月，中国氢氧化锂净进口量达到10.2千吨，而2025年同期还是净出口35.4千吨。这是中国首次在氢氧化锂贸易中成为净进口方。\n\n这不是一个边际变化。回顾历史序列，中国氢氧化锂净出口量从2017年的18.1千吨一路增长至2023年的126.2千吨，2024年才首次回落至112.6千吨。2025年骤降至35.4千吨，2026年直接转为净进口。这一趋势的斜率在加速。\n\n这意味着什么？中国不再是全球氢氧化锂的边际供给方，而是变成了边际需求方。当中国从“卖货的人”变成“买货的人”，全球定价的锚点会发生位移。此前市场习惯用“中国供给过剩”来压低远期价格预期，但这一逻辑的前提正在瓦解。\n\n---\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 碳酸锂进口量价齐升，但进口价格涨幅远超国内现货，暗示海外供给溢价正在系统性地重新建立\n\n2026年4月，中国碳酸锂进口量为32.7千吨，同比增长15%。进口价格达到每吨16,586美元，同比上涨74%，环\n\n[... middle omitted ...]\n\n格序列完整版或某外资投行的行业框架感兴趣，也欢迎在群内交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月锂盐数据，一个关键信号\n\n锂盐进口量价齐升\n\n4月中国碳酸锂进口3.27万吨，同比+15%。今年前4个月净进口11.4万吨，比去年同期多了47.8%。🧊\n\n氢氧化锂这边，4月出口5500吨，同比+31%。但有意思的是，今年前4个月中国从净出口变成了净进口1.02万吨——这个拐点值得关注。\n\n价格方面更明显：\n\n1️⃣ 碳酸锂进口均价4月涨到16586美元/吨，环比+11%，同比+74%🔥\n\n2️⃣ 氢氧化锂出口均价14894美元/吨，环比持平，同比+4%\n\n简单说就是：进口量在涨，进口价涨得更猛。氢氧化锂的出口量虽然也在恢复，但整体已经转为净进口格局。\n\n为什么重要？\n\n中国一直是锂盐的加工和出口大国，氢氧化锂出口量常年远大于进口。但2026年前4个月首次出现净进口，说明：\n\n- 海外锂盐产能正在释放，反向流入中国市场\n- 国内需求端（尤其是高镍三元材料）对氢氧化锂的需求可能比预期更强\n- 碳酸锂进口持续高位，全球锂资源正在向中国集中\n\n从更长维度看，2025年全年碳酸锂净进口237.7千吨，2026年前4个月就已经114千吨，节奏明显加快。\n\n一个值得讨论的问题：如果进口量持续高增、价格同步上行，对国内\n\n[... middle omitted ...]\n\nThe lithium carbonate import price increased 11% m/m and 74% y/y in April: prices averaged \\$16,586/t in April versus \\$14,994/t in March and \\$9,557/t in April 2025. See Table 6 for details. \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 20 May 2026 01:44 PM EDT\n\nDisseminated 20 May 2026 01:44 PM EDT"
  },
  {
    "id": "R011",
    "title": "硅电容合同背后，真正被低估的是存储器工艺的重新定价",
    "digest": "[wechat_article.md]\n# 硅电容合同背后，真正被低估的是存储器工艺的重新定价\n\n一份价值约15亿美元、为期两年的硅电容供应合同，由某韩国电子元件制造商与一家全球大型企业签署。如果只看金额和周期，这似乎只是一次常规的供应链锁定。但某外资投行的半导体团队在这份研报中给出了一个更值得关注的判断：这份合同的意义不在于订单本身，而在于它揭示了硅电容市场正从“AI服务器专用”向“高性能计算全场景”扩张，而支撑这一扩张的产能基础，恰恰来自被市场长期低估的成熟DRAM工艺。\n\n这不是一个关于需求的故事。这是一个关于供给侧结构性变化的故事。市场目前对硅电容的关注主要集中在AI算力芯片的配套需求上，但真正决定这一轮供应链格局的变量，是哪些厂商能够将传统DRAM产能转化为硅电容的制造能力，以及这种转化如何改变整个被动元件和存储器产业的竞争边界。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这份合同确认了硅电容正在从AI专用走向全场景应用\n\n某韩国元件制造商宣布的这份供应合同，覆盖2027年至2028年。研报指出，该合同主要供货对象是下一代TPU上的EMIB-T封装。但更关键的信息在于，该制造商明确表示计划将供应目的地从AI服务器扩展到高性能计算的其他领域，包括自动驾驶系统和移动设备。\n\n这意味着硅电容的市场可触达空间正在被重新定义。过去，市场对硅电容的认知基本局限在AI加速器的高端封装场景，市场规模有限，增长曲线陡峭但天花板清晰。而现在，随着自动驾驶对计算密度的要求提升，以及移动设备对小型化、高性能电容的需求增加，硅电容的应用边界正在从数据中心向边缘计算和终端设备延伸。\n\n这一点在另一家存储器公司的财报电话会议上得到了印证。研报引用其表述：除了现有的AI客户，可能还会有更多客户进入，例如移动设备领域。这并非孤立的判断，而是供应链上多个参与者的共识。对于投\n\n[... middle omitted ...]\n\n享完整的研报原文和核心图表，并持续跟踪这一产业链的最新动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片圈大新闻：1.5万亿韩元硅电容大单落地🔍\n\n**硅电容，下一个存储级市场**\n\n某外资投行最新研报点出一个关键信号——三星电机刚签下约1.5万亿韩元（约10亿美元）的硅电容供货合同，从2027年1月到2028年12月，为期两年。客户是全球级大厂，供货范围不止AI服务器，还覆盖自动驾驶和手机。\n\n这背后是硅电容市场正在起量的逻辑👇\n\n**1/ 供应格局：寡头垄断**\n\n硅电容市场玩家稀缺，客户为了保供，签长约是大概率事件。研报判断这批货主要供给下一代TPU的EMIB-T封装，但后续可能有更多客户进场——爱普在法说会上也提过类似方向。\n\n**2/ 生产端：老DRAM产线是天然优势**\n\n硅电容制造不需要先进制程，传统DRAM产线就能干。这意味着台湾DRAM厂有机会吃下这块增量。目前力积电产能已满，研报推测华邦电可能成为三星电机的合作伙伴——预计2027年贡献个位数营收占比。\n\n**3/ 为什么值得关注**\n\n硅电容和传统MLCC不同，它更薄、更耐高温、更适合高性能场景。AI加速卡、自动驾驶域控、旗舰手机都在往这个方向走。一个合约10亿美元，说明这不是小打小闹的试水，而是真金白银的供应链布局。\n\n**一点延伸思\n\n[... middle omitted ...]\n\ny EMIB-T on next gen TPUs. However, there may be more customers to come (e.g. mobile), as mentioned by AP Memory on its earnings call (link). We also believe that given the Si-Cap supply oligo\n\n[... middle omitted ...]\n\n Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,080.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R012",
    "title": "中国PC与平板出货量下滑，真正值得关注的不是总量，而是份额的剧烈重塑",
    "digest": "[wechat_article.md]\n# 中国PC与平板出货量下滑，真正值得关注的不是总量，而是份额的剧烈重塑\n\n2026年3月的数据已经出炉。中国PC出货量同比下滑2%，平板出货量同比下滑3%。如果只看这两个数字，很容易得出一个结论：消费电子需求依旧疲软，行业仍在底部徘徊。\n\n但这样的判断，恰恰会让人错过这份数据里真正重要的信号。\n\n某外资投行在最新发布的研报中，给出了比总量更值得拆解的结构性细节。3月中国PC出货256万台，平板出货298万台，环比分别增长30%和47%，说明春节后的补货周期仍在正常运转。真正的关键，藏在各品牌同比增速的巨大分化里——华为PC同比暴跌47%，而华硕猛增38%，苹果平板同比下滑21%，联想平板却逆势增长6%。这些数字指向的不是一个“整体疲软”的市场，而是一个正在激烈重分配的市场。\n\n市场真正低估的不是需求，而是供给侧的再定价。当总量增速趋近于零，竞争就从“做大蛋糕”变成了“切分蛋糕”。谁能在存量市场中抢到份额，谁就能获得远超行业均值的利润弹性。而这份研报提供的数据，恰恰给了我们一个审视这场份额争夺战的绝佳窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 总量接近零增长，但品牌间的增速差接近100个百分点\n\n先看PC市场。3月256万台的出货量，同比-2%，前两个月累计同比-4%。这个数字放在过去两年的背景下，并不算特别糟糕。2024年同期基数并不高，2025年市场曾短暂回暖，现在只是重新回到一个相对平稳的通道。\n\n但品牌层面的分化才是真正的故事。\n\n联想出货74.5万台，同比-8%，累计同比+3%。作为市场老大，联想的表现中规中矩，份额暂时稳定，但增速并不亮眼。华为出货14.6万台，同比-47%，累计同比-18%。这个跌幅在主要品牌中是最极端的。华硕出货31.8万台，同比+38%，累计同比+4%，环比增幅更是高达\n\n[... middle omitted ...]\n\n这份研报的完整PDF和更多未公开的图表数据，供群内读者参考。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 3月中国PC平板出货：两个值得关注的信号\n\n📊 出货量都在降，但别只看数字\n\n3月数据出来了，某外资投行援引IDC数据：中国PC出货256万台（同比-2%），平板298万台（同比-3%）。看起来双双下滑，但拆开看，有意思的点藏在细节里。\n\n**PC市场：联想稳，华硕猛，华为掉得狠**\n\n1️⃣ 联想还是老大，3月出货74.5万台，同比-8%。但看一季度累计267.3万台，同比+3%，说明前两个月拉回了一些。\n2️⃣ 华硕3月出货31.8万台，同比+38%，环比+146%。这个增速有点猛，可能是新品拉动或渠道策略调整。\n3️⃣ 华为PC出货14.6万台，同比-47%，一季度累计-18%。下滑幅度比较大，研报未给出具体原因，推测与供应链或产品周期有关。\n4️⃣ 苹果PC出货19.6万台，同比+63%，一季度累计+42%。Mac在商务和创意人群里还是稳。\n\n**平板市场：华为守，苹果跌，小米意外下滑**\n\n1️⃣ 华为平板出货79.4万台，同比+1%，基本持平。一季度累计269.3万台，同比-8%。\n2️⃣ 苹果平板73.7万台，同比-21%。一季度累计192.1万台，同比持平。iPad换代节奏可能影响出货。\n\n[... middle omitted ...]\n\n55% m/m, -8% y/y), 580k (-4% y/y) YTD   \n• Tongfang: 167k (+41% m/m, +56% y/y), 465k (+16% y/y) YTD   \n• Apple: 196k (+48% m/m, +63% y/y), 479k (+42% y/y) YTD   \n• Dell: 114k (+92% m/m, -6% y/\n\n[... middle omitted ...]\n\ntd>NT$145.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$181.00</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$383.00</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R013",
    "title": "市场真正低估的不是AI泡沫，而是新兴市场的信用裂缝",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI泡沫，而是新兴市场的信用裂缝\n\n这份来自某外资投行策略团队的周度资金流报告，表面上在讨论“股市集中度逼近历史极值”和“散户狂热”，但真正值得产业决策者和资产配置者关注的，是报告里一个容易被忽略的嵌套判断：**全球资本成本的上升，正在从边缘地带撕开第一道裂口。而这道裂口，最终会通过汇率和通胀路径，传导回核心资产定价。**\n\n报告发布时，该投行的牛熊指标已升至8.0，触发了自2002年以来第17次逆向卖出信号。历史回溯显示，此类信号出现后，全球股市在2-3个月内平均下跌2%-3%，最大回撤可达15%-20%。但比信号本身更重要的，是信号背后的结构性驱动力——这些驱动力，才是决定资产价格拐点是否成立的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场集中度已经超越历史上所有泡沫时期，但这次的结构不同\n\n报告提供的Chart 2可能是当前最被低估的警示图。它展示了美国股市在不同历史时期前十大公司的市值占比：1920年代的铁路股约63%，1970年代的“漂亮50”约40%，1980年代的日本约44%，1990年代的TMT约41%，而当前AI Big 10（原美股七巨头加上博通、AMD、美光）的占比已接近48%。\n\n48%这个数字，已经超过了“漂亮50”和TMT泡沫时期的集中度。但真正值得追问的不是“集中度有多高”，而是“这次集中度的形成机制是否不同”。\n\n历史上的集中度，大多来自产业周期末端的估值溢价——铁路、石油、消费品、科技，都是如此。但这一次，AI巨头的集中度背后，叠加了三个新变量：一是全球资金对“稀缺增长”的追逐，二是被动投资对集中度的自我强化，三是AI产业本身正在从“工具”变成“基础设施”，其赢家通吃的特征比以往任何技术革命都更极端。\n\n这意味着，即使集中度本身是一个泡沫信号\n\n[... middle omitted ...]\n\n完整推导链条。\n\n最后，请允许我以一份免责声明结束这篇导读：\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n市场情绪过于一致，反而要警惕了\n\n警惕一致预期\n\n某外资投行最新研报显示，市场情绪指标已触发反向信号。\n\n**1/ 情绪指标亮了红灯**\n- 某外资投行的“牛熊指标”升至8.0，触发风险资产的反向卖出信号\n- 这是2002年以来第17次触发，历史平均2-3个月全球股市回调2-3%\n- 最大回撤曾达15-20%，信号准确率约60%\n\n**2/ 市场集中度堪比历史泡沫**\n- AI相关前10大公司占美股市值约48%\n- 这个集中度已经超过1920年代、1970年代Nifty Fifty、1980年代日本、1990年代TMT泡沫时期\n- 唯一没超过的是1880年代的铁路股泡沫\n\n**3/ 资金流向在说悄悄话**\n- 科技股单周流入90亿美元，创去年10月来最大\n- 但欧洲和新兴市场已经连续6周资金流出\n- 黄金流出11亿美元，加密货币流出15亿美元\n- 美债反而流入108亿美元，为9周最多\n\n**4/ 历史IPO的启示**\n- 阿里巴巴和工商银行的IPO后，中概股在3-12个月内表现强劲\n- 但Visa和AIA的IPO后，大盘反而在9-12个月后明显下跌\n- 这次大IPO潮，会是“火箭燃料”还是“顶部信号”？\n\n*\n\n[... middle omitted ...]\n\nbbles end...why bond vigilantes on maneuvers; yield tells...XBI to \\$120 = yield to melt-up, XRT>\\$85 = bond shock delayed.\n\nThe Price is Right: Asia tech advancing sharply, Asia exporting inf\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R014",
    "title": "全球储能市场真正超预期的不是中国，而是欧洲的自我强化循环",
    "digest": "[wechat_article.md]\n# 全球储能市场真正超预期的不是中国，而是欧洲的自我强化循环\n\n这份来自某外资投行与SMM分析师在2026年泛亚会议上交流的纪要，释放了一个与市场主流叙事不同的信号。当大多数投资者仍在盯着中国储能产能出清和价格战何时见底时，全球储能需求的结构性增量正在发生一次关键的板块轮动。\n\nSMM在5月将2026年全球储能电芯出货预测上调至926GWh，同比增长54%。这个数字本身并不令人惊讶——市场早已习惯储能的高增速叙事。真正值得关注的，是这份预测上调背后的驱动因素排序：欧洲项目动能超预期、大容量电芯接受度提升、以及锂价上涨环境下成本优势的重新定价。\n\n这三个因素叠加在一起，指向一个核心判断：全球储能市场正在从“中国产能驱动全球成本下降”的单边逻辑，转向“区域需求分化+技术规格升级+成本传导机制重构”的多维博弈。理解这种结构性变化，比预测下一个季度的出货量重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧洲储能正在形成一条独立于中国的需求强化回路\n\n欧洲是本次预测上调最突出的区域。SMM预计2026年欧洲储能电芯出货将达到153GWh，同比增长94%，增速远超中国的30%和北美的32%。这个数字背后不是单一的政策刺激，而是一组正在自我强化的经济性条件。\n\n报告明确提到了几个关键变量：欧洲大容量GWh级项目加速落地、峰谷价差从约80欧元/MWh扩大至100欧元/MWh，折合人民币约0.6元/kWh，是中国市场价差的两倍。辅佐服务回报也在改善。葡萄牙、德国等市场的可再生能源与储能目标及直接补贴提供了政策底，但真正驱动项目经济性提升的，是电力市场自身的结构性变化。\n\n这意味着欧洲储能的增长不再完全依赖补贴力度，而是建立在电力现货市场套利和辅助服务收益的商业化基础之上。这是一个重要的边际变化。当一个市场的储能项目IRR\n\n[... middle omitted ...]\n\n的区域分化有自己的判断，也欢迎在群内分享你的观点和项目经验。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球储能出货量上修近千GWh\n\n储能大年来了\n\n欧洲需求超预期，大电芯成主流\n\n最近一份投行研报里，SMM的储能分析师给出了一个很关键的上修判断👇\n\n📌 2026年全球储能电芯出货预测上调至926GWh，同比+54%\n📌 产量预测更猛，上调至979GWh，同比+80%\n\n这背后是三个核心驱动力在同时发力：\n\n1️⃣ 欧洲需求比想象中更猛\n欧洲2026年出货预计153GWh，同比+94%，是所有区域里增速最快的。原因很实在：峰谷价差从€80/MWh扩大到€100/MWh，折合人民币约0.6元/kWh，比国内（约0.3元/kWh）高出一倍。再加上葡萄牙、德国等地的补贴政策还在持续，大GWh级别的项目不断落地。\n\n2️⃣ 大电芯（500+Ah）开始被下游接受\n随着锂价上涨，大电芯的成本优势变得更加明显。下游对大电芯的接受度提升，直接拉动了整体出货量的上修。这是结构性变化，不是短期波动。\n\n3️⃣ 碳酸锂涨价的影响有滞后\n近期锂价上涨，但研报认为对2026年电芯产量的冲击有限。原因是成本传导链条长：电芯厂→集成商→项目方，每个环节都有时间差。锂价联动机制在电芯厂和集成商之间基本落地，但传到项目端可能要到年底。所以短期\n\n[... middle omitted ...]\n\na key concern, but the near-term negative impact on cell production may be limited given a long cost pass-through cycle and partial linkage mechanism. Regional divergence is clear: the US mark\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R015",
    "title": "CXO 的真正拐点不是订单回暖，而是商业模式的重构",
    "digest": "[wechat_article.md]\n# CXO 的真正拐点不是订单回暖，而是商业模式的重构\n\n过去两年，市场对中国医药外包板块的讨论始终围绕一个核心问题：全球生物医药融资何时触底反弹。订单增速、客户询价、投融资数据，几乎成了判断CXO景气度的唯一锚点。但最近一期某外资投行的年度中国峰会释放了一个值得重新审视的信号——真正驱动头部公司价值变化的，或许不再是周期性的需求回补，而是供给端的结构性升级。\n\n这份研报以第一天会议纪要的形式，披露了药明合联、药明康德、康龙化成、金斯瑞、翰森制药等多家公司的管理层最新表态。表面看，各家都在重申2026年业绩指引，但细读之下，每家公司都传递了一个共同逻辑：行业竞争已经从“拼产能、拼价格”进入“拼平台、拼壁垒、拼模式”的新阶段。那些能够将规模优势转化为议价权、将技术积累转化为高壁垒新业务的公司，正在拉开与同行的差距。\n\n更值得关注的是，AI对药物发现和CRO业务的影响，已经从概念走向了可量化的商业落地。金斯瑞管理层明确表示，其生命科学业务已从AIDD（AI驱动药物发现）中获得了约50%的新增蛋白合成需求。这不是未来叙事，而是正在发生的结构性变化。\n\n以下是我们从这份纪要中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 药明合联的信心来源不是订单，而是商业化产能的确定性爬坡\n\n市场对药明合联的担忧，主要集中在2026年之后的高增长能否持续。但管理层在会议上的表态提供了更清晰的锚点：公司对2026年增长轨迹的信心，核心来源于商业化生产的快速放量，而非单纯的新签项目。\n\n管理层详细披露了无锡和新加坡两地的产能扩建进度，并明确给出了XDP5和XDP6两个先进设施的GMP就绪时间表——分别指向2027年和2028年。这意味着，公司对未来的收入能见度已经覆盖到了三年之后。同时，公司目前拥有8个PPQ（工艺性\n\n[... middle omitted ...]\n\n里继续讨论这些未解问题，一起追踪中国CXO行业的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCXO赛道新信号：AI加速落地，业绩指引清晰\n\nCXO的下一步，AI说了算？\n\n药明合联、金斯瑞、药明康德等集体发声\n\n---\n\n最近看了份某外资投行的研报，信息量很大。几个中国CXO龙头在投资者会议上集体“交底”，释放了不少积极信号。\n\n**1. 药明合联：2026年指引不变，产能扩张稳步推进**\n\n管理层对2026年增长非常有信心。核心逻辑是商业化的制造业务正在快速放量。无锡和新加坡的基地都在大规模扩产，最新的XDP5和XDP6设施已经规划到2027/2028年的GMP准备。手上的8个PPQ（工艺性能确认）项目为未来商业订单提供了可见度，第一个BLA（生物制品许可申请）项目可能今年就启动。之前收购的BioDlink整合顺利，客户对提价接受度良好。\n\n**2. 药明康德：结构增长，新业务板块毛利更高**\n\n管理层给出了清晰的增长路径：从小分子向高壁垒的新分子平台扩张。2026年订单积压13.85亿美元，为19-22%的营收增长提供了高可见度。更重要的是业务结构的变化——多肽、寡核苷酸、偶联物和生物药在2025年贡献了近30%的收入，且增速在60-100%以上，毛利率比小分子还要高。多肽和寡核苷酸的稳态毛利率\n\n[... middle omitted ...]\n\n 2026 growth trajectory, anchored by rapid commercial manufacturing scale-up. Management detailed extensive, ongoing capacity expansion across both its Wuxi and Singapore sites, mapping out GM\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 21 May 2026 07:10 AM HKT\n\nDisseminated 21 May 2026 07:10 AM HKT"
  },
  {
    "id": "R016",
    "title": "中国资产重定价的核心不是宏观反转，而是微观龙头的全球议价权",
    "digest": "[wechat_article.md]\n# 中国资产重定价的核心不是宏观反转，而是微观龙头的全球议价权\n\n过去一周，某外资投行在深圳举办的中国投资峰会上，一个信号被反复确认：全球资金对中国资产的态度正在从“全面回避”转向“极度挑剔的聚焦”。大多数投资者仍然低配中国，宏观层面的疑虑——房地产修复的可持续性、缺乏广泛的复苏基础——并未消散。但与此同时，围绕AI半导体、工业自动化、电力设备和部分出口冠军企业的会议室里，却挤满了人。\n\n这不是一个关于“中国故事回归”的判断。这份峰会首日纪要揭示了一个更精确的叙事：市场正在对中国的供给侧能力进行重新定价。那些在全球价值链中已经或正在建立不可替代地位的公司，正在吸引一批不再等待宏观拐点的资金。而这一轮重定价的驱动力，并非来自需求端的爆发，而是来自供给端的结构性优势——技术壁垒、成本竞争力、以及全球客户对供应链多元化的迫切需求。\n\n报告中最值得关注的新信号，并非某个具体的订单或业绩指引，而是一种结构性的信心：在机器人、工业自动化零部件、汽车玻璃和电力设备等细分领域，中国头部企业正从“低成本替代者”转变为“技术定义者”或“不可绕过的供应商”。这种转变的意义，远超短期的盈利预测上调。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 人形机器人：从概念驱动转向硬件可靠性驱动的“验证期”，中国有望在未来1-3年主导真实部署\n\n峰会上的机器人专家讨论确认了一个关键判断：人形机器人和具身AI已经不再是主题投资，而是被确立为长期结构性增长方向。但行业仍处于早期、以验证为主的阶段。近期的进展将更少依赖模型层面的突破，更多依赖硬件可靠性、系统架构（VLA+世界模型）以及高质量数据生成的渐进式改善。\n\n商业价值将首先在结构化工业场景中显现——物流、制造、药房——而更广泛的通用化和家庭应用则仍需时日。报告特别指出，未来1-3年，中国有望在真\n\n[... middle omitted ...]\n\n争力演变。在这里，讨论的不是股票代码，而是竞争力的底层逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国机器人产业链，正在经历什么？\n\n投研视角看中国机器人\n\n人形机器人从概念走向量产，供应链正在重构\n\n📌 某外资投行近期举办了一场中国峰会，Day 1 的交流信息量很大。整体来看，全球投资者对中国的态度依然是“谨慎但开始有选择性地看好”。虽然宏观基本面还没全面回暖，但AI、半导体设备、工业自动化和电力基建，已经成为最受关注的几个方向。\n\n1️⃣ 人形机器人：从“炫技”到“干活”的关键一步\n- 行业共识：人形机器人是长期结构性增长主题，但目前还在早期验证阶段。\n- 短期看点不是大模型突破，而是硬件可靠性、系统架构（VLA+世界模型）和数据质量的逐步提升。\n- 最先落地商业价值的场景是结构化工业环境（物流、制造、药店），家庭通用化还需要更长时间。\n- 未来1-3年，中国有望在规模化试点和ROI验证方面领先全球。\n\n2️⃣ 核心零部件：精密减速器的国产替代正在加速\n- 谐波减速器龙头（某上市公司）成为投资者关注焦点。\n- 产品品质已接近日本同行，但价格优势明显（便宜约50%），正在向KUKA、ABB、安川等全球头部机器人厂商批量供货。\n- 今年来自头部客户的订单已超去年全年，订单量远超现有产能。\n- 投资者也在关\n\n[... middle omitted ...]\n\ne better priced. Interest is highly selective, with strong engagement around AI and semiconductors (particularly equipment and domestic supply chains), industrials and automation, energy trans\n\n[... middle omitted ...]\n\nww.JPM.com/disclosures.\n\nJoann Kim - Specialist Sales - APAC Industrials & Autos AC\n\nAsia Pacific Specialist Sales\n21 May 2026\n\njoann.kim@JPM.com\n\nCompleted 21 May 2026 06:35 AM HKT\n\nDisseminated 21 May 2026 06:35 AM HKT"
  },
  {
    "id": "R017",
    "title": "市场真正低估的不是需求，而是防御侧的代际断层",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是防御侧的代际断层\n\n这份来自某外资投行的2026年春季网络安全报告，开篇就抛出了一个足以让任何产业决策者重新审视预算分配的判断：网络安全行业正在经历的不是一次周期性回暖，而是一次由AI驱动的供给侧结构性断裂。攻击面的扩张速度已经超过了所有传统防御工具的设计边界。\n\n报告的核心信号并非“安全预算会增长”——这已经是共识。真正的新信息是：攻击成本正在以500到1000倍的幅度下降，而防御能力的提升速度却远远落后。这不是一个供需缺口的问题，而是一个防御范式正在被技术演进本身淘汰的问题。\n\n为什么现在重要？因为2025年9月已经发生了由AI自主策划并执行的网络攻击事件，攻击者使用了比当前开源模型能力更弱的AI系统，就成功侵入了约30个目标，包括政府机构和金融机构。这些攻击中，80%到90%的战术操作由AI独立完成，速度是人类操作员无法企及的。而今天，更强的开源模型已经广泛可用。\n\n报告没有停留在“威胁在变大”的泛泛之谈上。它用数据、案例和成本结构分析，勾勒出了一幅防御者必须立刻重新定位的图景。以下是我们从这份研究报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 攻击成本从“国家级门槛”降到“任何人可负担”，防御的逻辑基础正在失效\n\n报告中最具冲击力的不是某个新威胁类型，而是一组成本对比数据。在传统模式下，对一个操作系统进行完整的安全漏洞扫描需要一支专家团队工作数周。而使用AI，成本不到50美元。开发一个能够完全控制目标计算机的攻击工具，在黑市上需要50万到200万美元，且需要高级技能。现在，AI可以在半天内完成，成本不到1000美元。\n\n这意味着什么？攻击的门槛已经从“国家级行为体”或“高技能犯罪团伙”降到了“任何拥有模型访问权限和计算资源的组织或个人”。报告明确\n\n[... middle omitted ...]\n\n们的知识星球微信群，那里有更深入的讨论和完整的报告解读材料。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在重塑网络安全攻防格局\n\nAI加速安全攻防\n\n最近某外资投行发了一份重磅研报，核心观点很直接：AI正在从根本上改变网络安全行业。我读完感觉信息量很大，整理几个关键判断分享给大家。\n\n1/ 攻击面正在以前所未有的速度扩大\n\nAI不仅能更快发现代码漏洞，还能自动生成更复杂的攻击手段。研报提到一个关键数据：平均漏洞利用时间已经从2018年的63天，压缩到2025年的负7天——这意味着攻击者能在补丁发布前就完成利用。\n\n更值得关注的是，2025年9月已有国家级行为体使用AI模型自主进行网络间谍活动，成功入侵约30个目标。AI完成了80-90%的战术操作，速度远超人类。\n\n2/ 平台型安全厂商处于最佳位置\n\n研报认为，拥有端点、网络、身份和数据等多个领域数据积累的平台厂商，最有可能应对AI带来的新威胁。原因很简单：AI需要大量高质量数据训练，而这些厂商天然拥有这些资源。\n\nCrowdStrike和Palo Alto Networks是明显的受益者，但研报也提到Check Point、Zscaler等公司同样积极参与其中。\n\n3/ AI攻击成本断崖式下降\n\n一个惊人的数据对比：扫描整个操作系统寻找安全漏洞，AI成本\n\n[... middle omitted ...]\n\nimes comes with a larger attack surface\n\nThe attack surface is evolving and expanding at an unprecedented pace: Agents can now find vulnerabilities in code at an unprecedented rate. This trans\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Backtest performance of our recommended US factors in rising and flat inflation scenarios – Internal Growth and EPS Revisions Breadth remain resilient across regimes, while Low PEG benefits from flatter inflation environ"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Internal Growth and Low PEG remain resilient in high oil volatility, while EPS Revisions improve as volatility normalizes Annualized Performance of our recommended US Factors in High and Normal Oil Volatility Regimes"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Recommended US Factors Capture AI Diffusion and Infrastructure Capex Exposure Net thematic exposure of US recommended factors to selected AI themes"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 5: Internal Growth factor stands out with strongest quality exposure, highlighting companies with sustainable profitability and disciplined reinvestment"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Top-quintile stocks in EPS revisions factor show superior operating leverage, margin momentum, and R&D intensity, aligned with strategists' rolling recovery outlook. Internal Growth Decomposition: Relative Strength of"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Low PEG's recent correlation profile shows greater alignment with growth than value"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Low PEG remains attractively valued versus history"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 9",
    "context": "Exhibit 10 provides additional support for this fundamental outlook, illustrating median factor scores for key attributes by comparing top-quintile stocks (Q1) versus bottom-quintile stocks (Q5). Stocks in the top quintile demonstrate notably higher operating "
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Top-quintile stocks in EPS revisions factor show superior operating leverage, margin momentum, and R&D Fundamental Profile of EPS Up-Down Revisions Factor - US"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Recommended Europe factors deliver positive returns across rising and flat inflation regimes"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Operating Cash Flow Yield and Low Asset Growth lead in high oil volatility; Revisions improve as oil volatility normalizes Annualized Performance of our recommended Europe Factors in High and Normal Oil Volatility Regi"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Recommended Europe Factors Show Positive Exposure to Future of Energy and Energy Security Themes Net thematic exposure of Europe recommended factors to selected Energy themes"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Operating Cash Flow Yield Has Delivered Strong Risk-Adjusted Performance"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Operating Cash Flow Yield Remains Reasonably Valued Versus History"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Operating Cash Flow Yield Shows Positive Net Exposure to Defensive and Energy-Sensitive Areas Quintile sector exposures - Operating Cash Flow Yield (Europe)"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Low YoY Asset Growth rewards capital discipline in a higher cost-of-capital environment"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Cost of equity varies across asset growth, with low growth firms advantaged"
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Low YoY Asset Growth shows positive exposure to energy-sensitive sectors Quintile sector exposures - Low Asset Growth factor (Europe)"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "Exhibit 21",
    "context": "Exhibit 21: European equity revision breadth has rebounded from early-2026 lows"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "Exhibit 22",
    "context": "Exhibit 22: 3M Up vs. Down EPS Revisions has delivered strong cumulative performance as revision breadth recovers"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "Exhibit 23",
    "context": "Exhibit 23: 3M Up vs. Down EPS Revisions shows positive net exposure to selected ai themes"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Earnings Revisions Breadth for Japanese firms"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Foreign investor flows into cash equities Foreign investor flow into cash equities (net)"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "Exhibit 28",
    "context": "Exhibit 27: Japan 10-year yield"
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Rolling 60-month regression analysis of Composite Value factor against monthly changes in Japanese and US short- and long-term interest rates: Coefficient and t-statistic of the intercept, and adjusted r-squared"
  },
  {
    "figure_id": "F026",
    "report_id": "R001",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Rolling correlation of Low PEG with Composite Value and Composite Growth"
  },
  {
    "figure_id": "F027",
    "report_id": "R001",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Valuation percentile of Low PEG"
  },
  {
    "figure_id": "F028",
    "report_id": "R001",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Europe – Changes in Cluster Rankings"
  },
  {
    "figure_id": "F029",
    "report_id": "R001",
    "label": "Exhibit 36",
    "context": "Exhibit 36: US – Changes in Cluster Rankings This figure illustrates ranking changes of factor clusters from the end of the previous month to the most recent month. Rankings are based on our 4-Dimensions Framework, which organises"
  },
  {
    "figure_id": "F030",
    "report_id": "R001",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Japan – Changes in Cluster Rankings"
  },
  {
    "figure_id": "F031",
    "report_id": "R001",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Europe – Factor Call: Up vs Down EPS Revisions (3ma)"
  },
  {
    "figure_id": "F032",
    "report_id": "R001",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Europe – Factor Call: Operating CF Yield"
  },
  {
    "figure_id": "F033",
    "report_id": "R001",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Europe – Factor Call: \"Low Asset Growth\" Factor"
  },
  {
    "figure_id": "F034",
    "report_id": "R001",
    "label": "Exhibit 42",
    "context": "Exhibit 42: US – Factor Call: EPS Up-Down Revisions"
  },
  {
    "figure_id": "F035",
    "report_id": "R001",
    "label": "Exhibit 43",
    "context": "Exhibit 43: US – Factor Call: Internal Growth"
  },
  {
    "figure_id": "F036",
    "report_id": "R001",
    "label": "Exhibit 44",
    "context": "Exhibit 44: US – Factor Call: Low PEG"
  },
  {
    "figure_id": "F037",
    "report_id": "R001",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Japan – Factor Call: EPS Up-Down Revisions"
  },
  {
    "figure_id": "F038",
    "report_id": "R001",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Japan – Factor Call: 12M Fwd Earnings Yield"
  },
  {
    "figure_id": "F039",
    "report_id": "R001",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Japan – Factor Call: PEG"
  },
  {
    "figure_id": "F040",
    "report_id": "R001",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Europe – Performance of Main Factors # Factor Performance: US US equities rebounded strongly in April, with the S&P 500 rising 10.5% following the sharp March selloff. US data were generally firm. Payrolls rose 178k in"
  },
  {
    "figure_id": "F041",
    "report_id": "R001",
    "label": "Exhibit 49",
    "context": "Exhibit 49: US – Performance of Main Factors"
  },
  {
    "figure_id": "F042",
    "report_id": "R001",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Japan – Performance of Main Factors"
  },
  {
    "figure_id": "F043",
    "report_id": "R001",
    "label": "Exhibit 51",
    "context": "Exhibit 51: Market Performance of the Three Regions Factor Betas by Region"
  },
  {
    "figure_id": "F044",
    "report_id": "R001",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Factor Regression Coefficients"
  },
  {
    "figure_id": "F045",
    "report_id": "R001",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Europe – Valuation Percentiles of Main Factors"
  },
  {
    "figure_id": "F046",
    "report_id": "R001",
    "label": "Exhibit 54",
    "context": "Exhibit 54: US – Valuation Percentiles of Main Factors"
  },
  {
    "figure_id": "F047",
    "report_id": "R001",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Japan – Valuation Percentiles of Main Factors"
  },
  {
    "figure_id": "F048",
    "report_id": "R001",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Average pairwise correlation by region (average absolute value)"
  },
  {
    "figure_id": "F049",
    "report_id": "R001",
    "label": "Exhibit 69",
    "context": "Exhibit 69: MSCI Europe Factor Correlation"
  },
  {
    "figure_id": "F050",
    "report_id": "R001",
    "label": "Exhibit 70",
    "context": "Exhibit 70: MSCI US Factor Correlation"
  },
  {
    "figure_id": "F051",
    "report_id": "R001",
    "label": "Exhibit 71",
    "context": "Exhibit 71: MSCI Japan Factor Correlation"
  },
  {
    "figure_id": "F052",
    "report_id": "R001",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Classification of Factors into 6 Groups and 17 Clusters"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "EXHIBIT 1: We revise up our WFE projection for CY26-CY28 to reflect our latest views..."
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: In China, we now see +15% / +15% YoY (+10% / +7% prior) in 2026 / 2027."
  },
  {
    "figure_id": "F055",
    "report_id": "R002",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: ...and we now model +21% YoY in CY26 (+18% prior). For CY27 we now model +18% (+12% prior) growth."
  },
  {
    "figure_id": "F056",
    "report_id": "R002",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: We lift our 2026/2027 ex-China WFE to +25%/+21% YoY (+25%/+15% prior)."
  },
  {
    "figure_id": "F057",
    "report_id": "R002",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 6: We now estimate 2027/2028 WFE spending for DRAM to be \\$57bn / \\$71bn (\\$48bn / \\$51bn prior) / NAND \\$18bn / \\$23bn (\\$16bn / \\$16bn prior), respectively..."
  },
  {
    "figure_id": "F058",
    "report_id": "R002",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: ...and for Logic/Foundry, we keep our 2026-27 estimates, and lift 2028 to \\$93bn (\\$92bn prior)."
  },
  {
    "figure_id": "F059",
    "report_id": "R002",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: We expect a strong growth in WLP over the next two years."
  },
  {
    "figure_id": "F060",
    "report_id": "R002",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Bernstein KLAC estimates vs prior EXHIBIT 12: LRCX trades at \\~37.2x... LRCX P/FE"
  },
  {
    "figure_id": "F061",
    "report_id": "R002",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: AMAT trades at \\~29.4x forward earnings... AMAT P/FE"
  },
  {
    "figure_id": "F062",
    "report_id": "R002",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: ...a \\~36% premium to the SOX and a \\~71% premium to the SPX LRCX Relative Forward P/E"
  },
  {
    "figure_id": "F063",
    "report_id": "R002",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: ...a \\~7% premium to the SOX and a \\~34% premium to the SPX AMAT Relative Forward P/E"
  },
  {
    "figure_id": "F064",
    "report_id": "R002",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: KLAC trades at \\~37.2x P/FE... KLAC P/FE"
  },
  {
    "figure_id": "F065",
    "report_id": "R002",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: ...a 35% premium to the SOX and \\~70% premium to the SPX KLAC Relative Forward P/E"
  },
  {
    "figure_id": "F066",
    "report_id": "R002",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: AMAT remains among the cheapest of the “big-5” semicaps; Lam is the most expensive; KLAC is amongst the more expensive \"Big 5\" Semicap P/FE"
  },
  {
    "figure_id": "F067",
    "report_id": "R002",
    "label": "Exhibit 19",
    "context": "EXHIBIT 19: We expect ASML's system sales to conitnue to grow at a rapid pace over the next three years, achieving a 23% CAGR and reaching more than USD 51 Bn by 2028."
  },
  {
    "figure_id": "F068",
    "report_id": "R002",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Mar import was \\$3.1bn"
  },
  {
    "figure_id": "F069",
    "report_id": "R002",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: 2026 YTD import -17% YoY Total WFE imports to China by year"
  },
  {
    "figure_id": "F070",
    "report_id": "R003",
    "label": "Figure 1",
    "context": "Alexander Hacking, CFA Figure 1. The negative correlation between gold price and US real rate has returned - average daily correlation between gold & 5y real rate at -0.75 YTD, vs -0.65 in 2025 and only -0.2 in 2024"
  },
  {
    "figure_id": "F071",
    "report_id": "R003",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. A major equity market correction typically sees gold lower first then rebound"
  },
  {
    "figure_id": "F072",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Precious metals (particularly gold) historically outperformed during stagflationary periods (e.g. the $2^{nd}$ oil crisis), with volatility created by recessions / Volker moment co"
  },
  {
    "figure_id": "F073",
    "report_id": "R003",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Gross gold spending (annualized) at over \\~\\$1tr in 1Q'26"
  },
  {
    "figure_id": "F074",
    "report_id": "R003",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. 1Q WGC data (\\$bn, lhs) show strong bar & coin demand, still resilient jewelry demand, and a rebound in central bank buying despite higher gold price (\\$/oz, rhs)"
  },
  {
    "figure_id": "F075",
    "report_id": "R003",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. China monthly non-monetary gold import set to remain strong on CNY strength, resilient domestic demand and easing import licensing rules"
  },
  {
    "figure_id": "F076",
    "report_id": "R003",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. China gold demand reached record high in value terms (Bn RMB, annualized, lhs) in 1Q based on our apparent demand modeling... © 2026 Citi Inc. No redistribution without Citi's writ"
  },
  {
    "figure_id": "F077",
    "report_id": "R003",
    "label": "Figure 7",
    "context": "Figure 7. China gold demand reached record high in value terms (Bn RMB, annualized, lhs) in 1Q based on our apparent demand modeling... © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. ... as overall demand remains robust in volu"
  },
  {
    "figure_id": "F078",
    "report_id": "R003",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. China gold premium weakened from Mar-Apr levels; silver premium hovering just below the 13% VAT rate"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "Figure 2",
    "context": "Figure 2: Chinese OEMs European market volume by automaker # By Country Figure 3: European market total volume trend"
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "Figure 4",
    "context": "Figure 4: Total European market volume breakdown by OEM"
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "Figure 5: Chinese OEMs' aggregate European market volume trend"
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "Figure 6",
    "context": "Figure 6: Aggregate market share of Chinese OEMs in European market"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "Figure 7: Germany market wide volume trend 000 Unit"
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "Figure 8",
    "context": "Figure 8: Germany market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "Figure 9",
    "context": "Figure 9: Chinese OEMs' aggregate volume trend in Germany"
  },
  {
    "figure_id": "F086",
    "report_id": "R004",
    "label": "Figure 10",
    "context": "Figure 10: Aggregate market share of Chinese OEMs in Germany"
  },
  {
    "figure_id": "F087",
    "report_id": "R004",
    "label": "Figure 11",
    "context": "Figure 11: France market wide volume trend 000 Unit"
  },
  {
    "figure_id": "F088",
    "report_id": "R004",
    "label": "Figure 12",
    "context": "Figure 12: France market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F089",
    "report_id": "R004",
    "label": "Figure 13",
    "context": "Figure 13: Chinese OEMs' aggregate volume trend in France"
  },
  {
    "figure_id": "F090",
    "report_id": "R004",
    "label": "Figure 14",
    "context": "Figure 14: Aggregate market share of Chinese OEMs in France"
  },
  {
    "figure_id": "F091",
    "report_id": "R004",
    "label": "Figure 15",
    "context": "Figure 15: UK market wide volume trend"
  },
  {
    "figure_id": "F092",
    "report_id": "R004",
    "label": "Figure 16",
    "context": "Figure 16: UK market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F093",
    "report_id": "R004",
    "label": "Figure 17",
    "context": "Figure 17: Chinese OEMs' aggregate volume trend in the UK"
  },
  {
    "figure_id": "F094",
    "report_id": "R004",
    "label": "Figure 18",
    "context": "Figure 18: Aggregate market share of Chinese OEMs in UK"
  },
  {
    "figure_id": "F095",
    "report_id": "R004",
    "label": "Figure 19",
    "context": "Figure 19: Italy market wide volume trend"
  },
  {
    "figure_id": "F096",
    "report_id": "R004",
    "label": "Figure 20",
    "context": "Figure 20: Italy market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F097",
    "report_id": "R004",
    "label": "Figure 21",
    "context": "Figure 21: Chinese OEMs' aggregate volume trend in Italy"
  },
  {
    "figure_id": "F098",
    "report_id": "R004",
    "label": "Figure 22",
    "context": "Figure 22: Aggregate market share of Chinese OEMs in Italy"
  },
  {
    "figure_id": "F099",
    "report_id": "R004",
    "label": "Figure 23",
    "context": "Figure 23: Turkiye market wide volume trend"
  },
  {
    "figure_id": "F100",
    "report_id": "R004",
    "label": "Figure 24",
    "context": "Figure 24: Turkiye market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F101",
    "report_id": "R004",
    "label": "Figure 25",
    "context": "Figure 25: Chinese OEMs' aggregate volume trend in Turkiye"
  },
  {
    "figure_id": "F102",
    "report_id": "R004",
    "label": "Figure 26",
    "context": "Figure 26: Aggregate market share of Chinese OEMs in Turkiye"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Figure 27",
    "context": "Figure 27: Spain market wide volume trend"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Figure 28",
    "context": "Figure 28: Spain market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Figure 29",
    "context": "Figure 29: Chinese OEMs' aggregate volume trend in Spain"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Figure 30",
    "context": "Figure 30: Aggregate market share of Chinese OEMs in Spain"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Figure 31",
    "context": "Figure 31: Poland market wide volume trend"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Figure 32",
    "context": "Figure 32: Poland market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Figure 33",
    "context": "Figure 33: Chinese OEMs' aggregate volume trend in Poland"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "Figure 34",
    "context": "Figure 34: Aggregate market share of Chinese OEMs in Poland"
  },
  {
    "figure_id": "F111",
    "report_id": "R004",
    "label": "Figure 35",
    "context": "Figure 35: Netherlands market wide volume trend"
  },
  {
    "figure_id": "F112",
    "report_id": "R004",
    "label": "Figure 36",
    "context": "Figure 36: Netherlands market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F113",
    "report_id": "R004",
    "label": "Figure 37",
    "context": "Figure 37: Chinese OEMs' aggregate volume trend in the Netherlands"
  },
  {
    "figure_id": "F114",
    "report_id": "R004",
    "label": "Figure 38",
    "context": "Figure 38: Aggregate market share of Chinese OEMs in the Netherlands"
  },
  {
    "figure_id": "F115",
    "report_id": "R004",
    "label": "Figure 39",
    "context": "Figure 39: Sweden market wide volume trend"
  },
  {
    "figure_id": "F116",
    "report_id": "R004",
    "label": "Figure 40",
    "context": "Figure 40: Sweden market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F117",
    "report_id": "R004",
    "label": "Figure 41",
    "context": "Figure 41: Chinese OEMs' aggregate volume trend in Sweden"
  },
  {
    "figure_id": "F118",
    "report_id": "R004",
    "label": "Figure 42",
    "context": "Figure 42: Aggregate market share of Chinese OEMs in Sweden"
  },
  {
    "figure_id": "F119",
    "report_id": "R004",
    "label": "Figure 43",
    "context": "Figure 43: Norway market wide volume trend 000 Unit"
  },
  {
    "figure_id": "F120",
    "report_id": "R004",
    "label": "Figure 44",
    "context": "Figure 44: Norway market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F121",
    "report_id": "R004",
    "label": "Figure 45",
    "context": "Figure 45: Chinese OEMs' aggregate volume trend in Norway"
  },
  {
    "figure_id": "F122",
    "report_id": "R004",
    "label": "Figure 46",
    "context": "Figure 46: Aggregate market share of Chinese OEMs in Norway"
  },
  {
    "figure_id": "F123",
    "report_id": "R004",
    "label": "Figure 47",
    "context": "Figure 47: SAIC European market volume by country"
  },
  {
    "figure_id": "F124",
    "report_id": "R004",
    "label": "Figure 49",
    "context": "Figure 49: SAIC European market volume trend"
  },
  {
    "figure_id": "F125",
    "report_id": "R004",
    "label": "Figure 50",
    "context": "Figure 50: SAIC European market share trend"
  },
  {
    "figure_id": "F126",
    "report_id": "R004",
    "label": "Figure 51",
    "context": "Figure 51: Chery European market volume by country"
  },
  {
    "figure_id": "F127",
    "report_id": "R004",
    "label": "Figure 53",
    "context": "Figure 53: Chery European market volume trend"
  },
  {
    "figure_id": "F128",
    "report_id": "R004",
    "label": "Figure 54",
    "context": "Figure 54: Chery European market share trend"
  },
  {
    "figure_id": "F129",
    "report_id": "R004",
    "label": "Figure 55",
    "context": "Figure 55: BYD European market volume by country"
  },
  {
    "figure_id": "F130",
    "report_id": "R004",
    "label": "Figure 57",
    "context": "Figure 57: BYD European market volume trend"
  },
  {
    "figure_id": "F131",
    "report_id": "R004",
    "label": "Figure 58",
    "context": "Figure 58: BYD European market share trend"
  },
  {
    "figure_id": "F132",
    "report_id": "R004",
    "label": "Figure 59",
    "context": "Figure 59: Leapmotor European market volume by country"
  },
  {
    "figure_id": "F133",
    "report_id": "R004",
    "label": "Figure 61",
    "context": "Figure 61: Leapmotor European market volume trend"
  },
  {
    "figure_id": "F134",
    "report_id": "R004",
    "label": "Figure 62",
    "context": "Figure 62: Leapmotor European market share trend"
  },
  {
    "figure_id": "F135",
    "report_id": "R004",
    "label": "Figure 63",
    "context": "Figure 63: XPeng European market volume by country"
  },
  {
    "figure_id": "F136",
    "report_id": "R004",
    "label": "Figure 65",
    "context": "Figure 65: XPeng European market volume trend"
  },
  {
    "figure_id": "F137",
    "report_id": "R004",
    "label": "Figure 66",
    "context": "Figure 66: XPeng European market share trend"
  },
  {
    "figure_id": "F138",
    "report_id": "R004",
    "label": "Figure 67",
    "context": "Figure 67: Geely European market volume by country"
  },
  {
    "figure_id": "F139",
    "report_id": "R004",
    "label": "Figure 69",
    "context": "Figure 69: Geely European market volume trend"
  },
  {
    "figure_id": "F140",
    "report_id": "R004",
    "label": "Figure 70",
    "context": "Figure 70: Geely European market share trend"
  },
  {
    "figure_id": "F141",
    "report_id": "R004",
    "label": "Figure 71",
    "context": "Figure 71: Great Wall European market volume by country"
  },
  {
    "figure_id": "F142",
    "report_id": "R004",
    "label": "Figure 72",
    "context": "Figure 72: Great Wall European market volume breakdown"
  },
  {
    "figure_id": "F143",
    "report_id": "R004",
    "label": "Figure 74",
    "context": "Figure 74: Great Wall European market share trend"
  },
  {
    "figure_id": "F144",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: April activity data was the largest downside surprise since May 2023"
  },
  {
    "figure_id": "F145",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 2: April physical output data shows the negative impact of the Iran war as well as continued strength in high-tech manufacturing and new energy sectors Bottom 10 sequential output growth from Mar to Apr"
  },
  {
    "figure_id": "F146",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: IP was strong in March, June and September but weak in April, July and October in 2025 China industrial production sequential growth (mom sa non-annualized)"
  },
  {
    "figure_id": "F147",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Effect of government-subsidized consumer goods trade-in program should fade over time"
  },
  {
    "figure_id": "F148",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: EV sales increased while ICE car sales declined in April on higher gasoline prices"
  },
  {
    "figure_id": "F149",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 6: FAI data diverged significantly from alternative measures of construction activity Real FAI Implied vs. Actual Commodity Demand"
  },
  {
    "figure_id": "F150",
    "report_id": "R005",
    "label": "Exhibit 7",
    "context": "Exhibit 7: The pace of LGSB issuance slowed notably from Q1 to Q2"
  },
  {
    "figure_id": "F151",
    "report_id": "R005",
    "label": "Exhibit 8",
    "context": "Exhibit 8: April activity data continue to show a bifurcated economy with strong exports and weak domestic demand China April Activity Indicators"
  },
  {
    "figure_id": "F152",
    "report_id": "R005",
    "label": "Exhibit 9",
    "context": "Exhibit 9: We expect sequential real GDP growth to slow from $5.3\\%$ qoq annualized in Q1 to $4.0\\%$ in Q2 China Current Activity Indicator and GDP"
  },
  {
    "figure_id": "F153",
    "report_id": "R005",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Other than the Middle East, China exports to EM destinations held up well in March and April"
  },
  {
    "figure_id": "F154",
    "report_id": "R005",
    "label": "Exhibit 11",
    "context": "Exhibit 11: NBS data shows that existing home prices increased sequentially in tier-1 cities in April"
  },
  {
    "figure_id": "F155",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: AI Adoption in Major EMs Is Only Slightly Lagging DMs Microsoft AI Diffusion Share"
  },
  {
    "figure_id": "F156",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The Absolute and Relative Gap Between DM and EM Adoption Rates Has Been Shrinking, Including for Cloud Services"
  },
  {
    "figure_id": "F157",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The Gap in Adoption of Cloud Services Is Small, Both in Terms of Adoption Rates and Number of Uses DM vs EM Cloud Services Adoption"
  },
  {
    "figure_id": "F158",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: EM Countries Are Much More Likely Leap to the Technology Frontier with Digital Technologies Share of EM Firms Using Most Advanced Technology for Business Function, by Business Function Type"
  },
  {
    "figure_id": "F159",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "As an example, early applications of AI in EM healthcare have raised the efficiency and accuracy of certain procedures and yielded better health outcomes at a relatively low infrastructural cost (Exhibit 5). Poor health weighs heavily on economic activity in d"
  },
  {
    "figure_id": "F160",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China gas demand growth has remained weak... China apparent gas demand, Bcm/y"
  },
  {
    "figure_id": "F161",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...but not enough to prevent inventories moving down yoy in April China underground gas storage, Bcm"
  },
  {
    "figure_id": "F162",
    "report_id": "R007",
    "label": "Exhibit 3",
    "context": "Exhibit 3: China LNG imports are increasing sequentially, which we expect to continue through the summer China LNG imports, mpta"
  },
  {
    "figure_id": "F163",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The JKM-TTF premium remains strong enough to cover the incremental cost for the US to ship LNG to Asia vs to Europe JKM-TTF spread and the US shipping cost differential (lhs) vs US LNG loadings to Europe vs to Asia, mtpa"
  },
  {
    "figure_id": "F164",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 5: LNG loadings are now marginally up yoy as suppliers postpone maintenance... Global LNG loadings, mtpa"
  },
  {
    "figure_id": "F165",
    "report_id": "R007",
    "label": "Exhibit 6",
    "context": "Exhibit 6: ...slowing, but not preventing, a yoy decline in European LNG imports North West Europe LNG imports, mcm/d"
  },
  {
    "figure_id": "F166",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China PC shipments were down 2% y/y to 2.56mn units in Mar-26"
  }
]