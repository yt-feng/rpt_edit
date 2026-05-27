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
    "title": "市场真正低估的不是通胀，而是美联储可能被迫“反向保险”加息",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是通胀，而是美联储可能被迫“反向保险”加息\n\n过去几个月，全球金融市场最核心的叙事是“通胀粘性”和“降息推迟”。几乎所有主流资产价格——从美债到权益——都在围绕一个假设反复博弈：美联储只是“迟降”，不是“不降”。但某外资投行最新一份宏观日报揭示了一个更深层、也更令人不安的逻辑转向：美联储在2024-2025年累计175个基点的降息，可能被证明是“过度保险”，而当前的通胀加速正在迫使政策制定者考虑一个此前几乎被排除的情景——用加息来逆向对冲这份保险。\n\n这不是关于通胀本身是否超预期的讨论，而是关于政策框架是否需要重新校准的命题。如果市场真正定价的不是“降息时点”，而是“政策方向可能逆转”，那么所有基于利率下行周期构建的资产配置逻辑都需要被重新审视。\n\n这份日报以极其克制的语调，在几个看似零散的数据点背后，勾勒出一条清晰但尚未被充分定价的逻辑链条。它没有高呼“加息即将到来”，而是通过一个框架性问题让读者自己得出结论：当联邦基金利率已经显著低于所有标准政策规则所指示的水平时，美联储的下一步行动究竟意味着什么？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 密歇根通胀预期的跃升，正在把“粘性”升级为“失控”\n\n日报中一个容易被忽视但极具信号意义的数据点，是5月密歇根大学消费者信心调查的最终修订值。一年期通胀预期从初值的4.5%上修至4.8%，五年至十年期通胀预期则从3.4%大幅上修至3.9%。后一个数字尤其值得警惕——它已经回到了2022年通胀恐慌时期的水平，而当时联邦基金利率还在接近零的水平。\n\n更关键的是，这个3.9%的长期通胀预期，是在美联储已经累计降息175个基点、且联邦基金利率仍维持在4%以上的背景下出现的。这意味着，消费者并不相信美联储当前的政策立场足以将通胀拉回2%目标。如果长期通胀预期\n\n[... middle omitted ...]\n\n完整报告中的图表和模型，进一步拆解加息情景下的资产配置逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储最鸽派的官员，开始谈加息了\n\n📌 通胀预期在升温\n\n📌 美联储可能已经“过度保险”\n\n最近某外资投行的每日简报里，有几个点值得聊一聊。\n\n1️⃣ 美联储官员转向鹰派\n- 最鸽派的Waller说：“不能再排除加息的可能性”\n- 虽然不认为“近期”需要考虑加息，但降息和加息的可能性现在是对等的\n- 通胀将是未来政策决策的“驱动力”\n- 如果通胀不很快缓解，不能排除未来加息\n\n2️⃣ 消费者通胀预期在飙升\n- 密歇根大学5月消费者信心终值下修至44.8，历史最低\n- 1年通胀预期上修至4.8%（2月伊朗冲击前是3.4%）\n- 5-10年通胀预期上修至3.9%\n- 这种上升趋势对美联储来说是个麻烦\n\n3️⃣ 美联储可能已经“过度保险”了\n- 研报分析认为，美联储此前175bp的降息，本质上是为劳动力市场下行风险买的“保险”\n- 第一轮降息（2024年）符合政策规则\n- 但第二轮降息后，叠加近期通胀加速，联邦基金利率已经显著低于所有政策规则设定\n- 现在的政策可能已经“过度保险”了，未来加息更像是谨慎地撤销这份保险\n\n4️⃣ 美债收益率上涨的原因\n- 4月下旬以来的美债抛售主要发生在纽约上午时段\n- 这与市场重新\n\n[... middle omitted ...]\n\ns (and \\~30bps over the week), Germany down 6bps. Oil up 0.9% to USD103.54/bbl (Brent).\n\nMichigan consumer sentiment revised down 3.4pts in final read for May, to 44.8. Historic low. One-year \n\n[... middle omitted ...]\n\n8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, SouthTowerSingapore 048583Tel: (65) 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R002",
    "title": "市场真正低估的不是需求，而是政策信号的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是政策信号的再定价\n\n四月的中国宏观数据全面低于预期。工业增加值同比增长4.1%，零售几乎零增长，固定资产投资同比下降8%。某外资投行的自建MAP指标显示，这是2023年5月以来最负面的宏观数据意外。但同一个团队在同一份报告中，却明确给出了“不必过度担忧”的判断。这不是矛盾的信号，而是理解当前中国资产定价逻辑的分水岭。\n\n市场习惯于把数据看作结果，但真正重要的不是四月数据本身有多弱，而是这些数据背后揭示的政策框架、结构性变量和预期差正在发生怎样的变化。这份报告的核心判断是：中国经济正在经历一次“有管理的减速”，而市场对这次减速的定价方式可能正在从“恐慌性防御”转向“选择性接受”。\n\n原因有三。第一，四月数据的弱，部分来自全球能源供给冲击的滞后影响，部分来自财政支出节奏的技术性放缓，并非需求端的全面塌陷。第二，房地产高频数据出现了值得密切关注的企稳迹象，一线城市新房和二手房价格环比均出现上涨。第三，人民币国际化正在从贸易结算向金融资产定价权延伸，这是一个尚未被充分定价的结构性变量。\n\n以下五个层次，逐层拆解这份报告真正想告诉你的东西。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四月数据弱在表面，但弱的原因比弱本身更重要\n\n四月数据全面低于预期，这是事实。但报告用了一个非常关键的区分：一部分弱来自“真实的逆风”，另一部分来自“技术和政策因素”。\n\n真实的逆风是什么？全球能源供给冲击导致化工和成品油生产大幅下滑。这是外生变量，不是中国国内需求能短期改变的。而技术和政策因素，则指向财政支出增速的显著放缓。报告在另一份配套数据评论中提到，四月财政支出增速进一步下降，但收入端基本稳定。这意味着四月数据中有一部分弱，是政府主动放缓支出节奏的结果，而不是经济自发失速。\n\n这个区分极其重要。如果市\n\n[... middle omitted ...]\n\n跟踪框架。这些内容，是形成独立于市场共识的判断所必需的拼图。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月数据偏弱，但地产有暖意\n\n三件事看懂4月经济\n\n出口强、内需弱，这个格局还在持续\n\n---\n\n最近某外资投行发了篇关于中国宏观的研报，核心就三件事——4月数据、地产、人民币国际化。我帮你拆成好理解的逻辑线👇\n\n**1️⃣ 4月数据确实不好看，但别只看表面**\n\n工业增加值同比+4.1%，社零同比+0.2%，固投同比-8%。这三个数字放在一起，确实有点扎眼。研报里用了一个自创的“MAP评分”，说这是去年5月以来最差的宏观数据意外。\n\n但仔细看原因：有全球能源价格冲击的真实影响（化工、成品油生产明显下滑），也有财政支出节奏放缓的技术性因素。所以不必过度解读单月波动，研报预计Q2实际GDP环比年化增速会从Q1的5.3%回落到4.0%，出口强、内需弱的格局还会持续一段时间。\n\n**2️⃣ 地产端出现了一丝暖意**\n\n高频跟踪数据显示，新房和二手房销售都在趋稳。70城房价指数显示，环比跌幅在收窄，而且一线城市的新房和二手房价格都出现了环比上涨。虽然只是“一丝暖意”，但如果地产能真正企稳，对信心和资本市场的提振作用会很明显。这个信号值得继续跟踪。\n\n**3️⃣ 人民币国际化：进步很大，路还很长**\n\n4月录得净外汇流\n\n[... middle omitted ...]\n\n spending. Overall, we expect sequential real GDP growth to slow from $5.3\\%$ qoq ann in Q1 to $4.0\\%$ in Q2, with the pattern of strong exports and weak domestic demand persisting.\n\nWe expect\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "EM信用债曲线正在传递一个被低估的信号",
    "digest": "[wechat_article.md]\n# EM信用债曲线正在传递一个被低估的信号\n\n这份某外资投行在2026年5月22日收盘后发布的EM USD 10s30s Spread Curve报告，表面上是一份常规的每周曲线更新，但数据叠加后的信号并不寻常。EM Aggregate 10s30s利差曲线当前报68个基点，较一周前缩窄2个基点，较一年前收窄7个基点。这些数字本身并不惊人，真正值得关注的是这些数据点背后的结构性含义——新兴市场信用债的期限溢价正在发生系统性重定价，而这种重定价的驱动力、可持续性以及对不同类别发行人的差异化影响，可能被市场参与者低估了。\n\n报告提供了从主权债到公司债、从投资级到高收益、从亚洲到拉美的完整曲线数据切片。把这些切片放在一起看，能得出一个更清晰的判断：当前EM信用曲线的形态变化，反映的不是简单的风险偏好回升，而是全球资本对新兴市场长期信用风险的评估框架正在发生根本性调整。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 曲线趋平不是短期波动，而是持续了一年的结构性趋势\n\nEM Aggregate 10s30s在2021年5月曾达到约100个基点的水平，2022年5月因美联储激进加息和EM资金外流，曲线一度深度倒挂至约-80个基点。此后曲线逐步恢复正斜率，但恢复的速度和形态在2024年后发生了质变。\n\n从2024年5月到2025年5月，EM Aggregate 10s30s从约70个基点降至约60个基点，再到当前约68个基点。表面上看，过去一年曲线在60-70个基点区间窄幅震荡，似乎没有明确方向。但结合更长时间维度和不同细分指数的数据，趋势就清晰了：曲线的中枢正在下移。2021年EM Aggregate 10s30s的1年均值约为68个基点，而当前水平已低于2024年同期的75个基点左右。\n\n更关键的是，这种趋平并非均匀发生。\n\n[... middle omitted ...]\n\n未来走势的判断，以及如何将这些分析框架应用到实际投资决策中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nEM新兴市场债券的曲线密码\n\n谁在变陡，谁在变平？\n\n某外资投行最新周报显示，截至2026年5月22日，EM Aggregate 10s30s利差曲线斜率为68bps，较上周小幅收窄2bps。整体来看，新兴市场债券的期限结构正在经历微妙变化。\n\n1/ 不同板块分化明显\nEM IG（投资级）曲线斜率61bps，而EM HY（高收益）达到83bps。高收益债的长端溢价明显更高，这反映了市场对高风险资产的长期补偿要求。\n\n2/ 最陡和最平的发行人\n埃及以159bps成为最陡峭曲线，其次是萨尔瓦多（117bps）、南非（112bps）、PEMEX（110bps）。最平坦的是印尼（20bps）、SQM（31bps）、EXIMBK（34bps）。这种差异背后是各国信用基本面的分化。\n\n3/ 一周变化最大的\n印尼曲线一周内陡化了14bps，是变动最大的。沙特阿美、GRUMAB、南非分别陡化了9bps。而萨尔瓦多、罗马尼亚、PIFKSA则出现不同程度的平坦化。\n\n4/ 历史位置\n从2021年5月的100bps高点，到2022年5月倒挂至-80bps，再到当前68bps，EM曲线经历了一个完整周期。目前水平处于近一年均值附近（\n\n[... middle omitted ...]\n\ntd>EM IG 10s30s</td><td>JPCUEMAI Index</td></tr><tr><td>EM HY 10s30s</td><td>JPCUEMAH Index</td></tr><tr><td>EMBIG 10s30s</td><td>JPCUEMBG Index</td></tr><tr><td>EMBIG IG 10s30s</td><td>JPCUEM\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 26 May 2026 05:21 AM HKT\n\nDisseminated 26 May 2026 06:41 AM HKT"
  },
  {
    "id": "R004",
    "title": "市场真正低估的不是AI支出规模，而是它如何被GDP统计“吃掉”",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI支出规模，而是它如何被GDP统计“吃掉”\n\n2026年一季度，美国商业固定投资以10.4%的年化速度增长，较去年全年5.6%的稳健步伐明显加速。这个数字本身并不令人意外——市场早已预期AI建设支出和新的税收激励会支撑投资。真正值得追问的是：这10.4%的增长背后，有多少是真实的国内经济扩张，有多少只是统计口径下的“幻象”？\n\n某外资投行最新发布的年中资本开支更新报告，为这个问题提供了迄今为止最清晰的拆解。它的核心判断是：2026年企业投资将增长7.8%（Q4/Q4口径），但驱动因素的结构性变化，远比总量数字更重要。报告揭示了一个多数投资者尚未定价的真相——AI对GDP的拉动远比表面数据小，而新税改的刺激效应才刚刚开始显现。\n\n如果你只关注资本开支的增速，你可能已经错过了更关键的信号。这份报告的价值不在于预测数字本身，而在于它给出了一个分析框架，让读者能够区分“统计上的增长”和“经济意义上的增长”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI对资本开支的拉动是真实的，但GDP统计至少“漏掉”了一半\n\n报告最核心的洞察之一，是AI对资本开支的拉动与对GDP的拉动之间存在巨大的剪刀差。\n\n根据该投行的测算，AI相关支出在2026年将为“真实资本开支”增长贡献约3.3个百分点。但所谓的“统计口径资本开支”增长中，AI的贡献只有2.8个百分点。这0.5个百分点的差距，源于美国经济分析局目前将半导体视为中间投入品，因而将其排除在投资统计之外。\n\n更值得关注的是，AI对GDP的拉动被“压缩”得更厉害。报告估算，AI相关支出仅能为2026年的真实GDP增长贡献0.3个百分点，而统计口径的GDP增长中，AI的贡献只有0.1个百分点。\n\n为什么差距如此之大？两个原因。第一，大量AI相关设备来自海外进\n\n[... middle omitted ...]\n\n同政策情景下的敏感性分析，这些内容在本篇导读中并未完全展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026美国企业投资：AI与减税双轮驱动\n\n**投资回暖进行时**\n\n**三大因素支撑今年企业支出**\n\n最近翻了份某外资投行的年中资本开支更新，信息量很大，直接划重点。\n\n2026年Q1美国商业固定投资年化增速达到10.4%，比去年5.6%明显提速。剔除设备进口等干扰因素后，本土实际资本开支增速也从2.4%回升到5%。全年企业投资预计增长7.8%，比之前预测的6.5%更高。\n\n背后的驱动力是什么？三个关键词：AI、减税、政策拖累消退。\n\n**1/ AI是最大增量**\nAI相关支出持续拉动设备、建筑和基础设施投资。企业正在加快数据中心、电力设施等建设。预计2026年AI将拉动真实资本开支增长约3.3个百分点。\n\n但注意：美国统计局把半导体算作中间投入品，不计入投资，所以官方统计的拉动效果只有2.8个百分点。这意味着AI对经济的实际贡献比数据显示的更大。\n\n到2026年底，AI相关年化支出预计突破8000亿美元。如果AI投资突然收缩，主要影响结构性和知识产权投资，对GDP的拖累约0.2-0.4个百分点。\n\n**2/ 新减税法案效果显现**\n《一个美好大法案》中的税收优惠正在起作用。制造业、运输、采矿等行业资本使\n\n[... middle omitted ...]\n\n4\\%$ in 2025. This week, we update our outlook for the rest of the year.   \nAI-related spending will continue to boost equipment and structures investment in 2026 as companies press ahead with\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "人民币中间价模型正在释放一个市场尚未消化的信号",
    "digest": "[wechat_article.md]\n# 人民币中间价模型正在释放一个市场尚未消化的信号\n\n在大多数市场参与者还在争论人民币短期方向时，一份来自某外资投行的每日模型测算，揭示了一个被忽视的结构性变化：其基准模型预测的USD/CNY中间价已从6.8318骤降至6.7827，单日隐含变动高达491个基点。这不是一个简单的技术修正，而是模型底层逻辑对近期汇率变量重新定价后的结果。\n\n这份报告的核心价值不在于给出一个点位预测，而在于它提供了一个观察中国央行汇率管理意图的量化框架。当模型预测值与实际中间价出现系统性偏差时，偏差的方向和幅度本身就构成了政策信号。目前，模型在计入逆周期因子后的预测值为6.8034，仍较前一交易日低284个基点。这意味着，即便考虑了央行的平滑操作，模型仍在指向一个更低的人民币中间价。\n\n为什么现在这个信号值得认真对待？因为当前时点正处于多重政策窗口期的交汇处：7月底的政治局会议、11月在深圳举办的APEC峰会、以及年末可能的中美领导人会晤。每一个事件都可能成为汇率政策调整的触发点。而模型正在告诉我们，市场的定价可能还没有充分反映这些事件的潜在影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的急剧变化并非噪音，而是对近期变量重新定价的结果\n\n理解这份模型的价值，首先要看它的预测逻辑。该模型通过追踪一篮子货币的隔夜变动，特别是韩元、土耳其里拉、俄罗斯卢布和澳元这四个权重最高的货币，来推算次日中间价的合理水平。在最新一期测算中，韩元和土耳其里拉的走弱贡献了正向调整（分别推高中间价5.0和2.5个基点），而卢布和澳元的走强则贡献了负向调整（分别压低中间价4.0和5.0个基点）。综合一篮子货币的净效应，模型得出了491个基点的向下修正。\n\n这个数字本身并不代表央行一定会按此操作。但它揭示了一个重要事实：在当前的一篮子货币框架下，\n\n[... middle omitted ...]\n\n份报告，还包括我们对全球宏观、地缘政治和资产配置的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型出了新数字\n\n6.7827\n\n模型预估较前次低491点\n\n最近某外资投行的模型更新了人民币中间价预测，数字挺有意思的。\n\n简单说，这个模型通过一篮子货币的波动，推算第二天央妈可能开的中间价。最新预测是6.7827，比上一次的6.8318低了491个点。如果把逆周期因子也算进去，预测值是6.8034，比前次低了284个点。\n\n1/ 模型怎么算的\n模型主要看四个货币的贡献：韩元贡献了+5点，土耳其里拉+2.5点，俄罗斯卢布-4点，澳元-5点。整体算下来，预测方向是往升值走的。\n\n2/ 模型误差在缩小\n看历史数据，模型误差从1月的-1800点，到4月的-1200点，最近几个月已经收窄到600点左右。说明模型对中间价的拟合度在变好，央妈的操作和市场预期的差距在缩小。\n\n3/ 中间价波动频率下降\n从去年11月到今年5月，中间价大部分时间没变，只在3月有一次150点的调整。这种“稳”的节奏，背后是央妈的政策意图——不希望汇率大起大落。\n\n4/ 下半年重要时间节点\n7月底政治局会议、10月国庆黄金周、11月APEC深圳峰会、12月中央经济工作会议，还有年底可能的中美高层会晤。这些事件都会影响汇率政策取向。\n\n[... middle omitted ...]\n\n(without counter-cyclical factor)   \n![](images/f81fdf707759bd2bdc860ed07335721f9ca0819f70e3dd84a19995dbe8cb75f5.jpg)\n\n<details>\n<summary>bar</summary>\n\n| Index | Top 4 weighted contribution t\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R006",
    "title": "人形机器人在仓库的回报期已缩短至3年，规模量产将使其低于1年",
    "digest": "[wechat_article.md]\n# 人形机器人在仓库的回报期已缩短至3年，规模量产将使其低于1年\n\n关于人形机器人的商业化落地，市场一直存在一个核心疑问：这些昂贵的双足机器到底能用在哪里？一份来自某外资投行的最新研报给出了一个大胆且具体的答案——仓库。报告的核心判断是，人形机器人在仓库场景的经济账已经算得过来了。基于当前的技术效率和定价，其投资回报期约为3年。而随着量产带来的成本下降，这个周期在不久的将来有望缩短至1年以内。这意味着，阻碍人形机器人大规模部署的最后一道关键门槛——经济性——正在被拆除。\n\n这份报告的价值不在于它描绘了一个宏大的未来图景，而在于它用具体的财务模型和场景分析，证明了“人形机器人+仓库”这个组合在商业上已经具备了可行性。对于产业决策者和投资者而言，真正需要关注的不是机器人能否学会走路，而是它们何时能以低于人工的成本，在仓库的流水线上稳定工作。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 仓库成为共识性落地场景，并非偶然的巧合\n\n超过20家人形机器人公司正在探索仓库场景，这不仅包括美国的Agility Robotics、Figure、Boston Dynamics，也包括中国的宇树科技、智元机器人等。合作的客户名单涵盖了Amazon、GXO、顺丰速运等物流与电商巨头。这并非简单的概念验证，而是产业资本用真金白银做出的选择。\n\n为什么是仓库？报告给出了三个逻辑层级清晰的原因。第一，人形机器人目前的技术能力尚无法胜任开放环境下的通用任务，而仓库是一个结构化的、任务相对标准化的场景。搬运、分拣、码垛这些工作，复杂度远低于家庭服务或精密制造。第二，仓库中存在大量重复、标准化、且劳动力需求旺盛的环节，这为机器人提供了充足的“就业岗位”，一旦验证成功，规模化复制相对容易。第三，仓库是物流链条的枢纽，从仓库切入，可以自然地向更广阔的\n\n[... middle omitted ...]\n\n不同技术路线的优劣对比，以及产业链上值得关注的潜在投资标的。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人形机器人进仓库，回本只需3年？\n\n仓库是人形机器人的第一站\n\n最近读了一份某外资投行关于人形机器人的研报，核心观点很直接——仓库场景可能是人形机器人最先大规模落地的地方，而且经济账已经算得过来了。\n\n为什么是仓库？三个原因很清晰👇\n\n1/ 仓库环境相对结构化，任务标准化（搬运、分拣、打包），比工厂和家庭场景简单，技术门槛低很多。\n\n2/ 仓库里重复性劳动需求大，自动化缺口明显。全球仓库自动化渗透率才23%（2024年数据），大部分仓库还是人工为主。\n\n3/ 从仓库切入，未来可以延伸到更广阔的物流链条，尤其是最后一公里配送，市场空间巨大。\n\n目前全球已有超过20家人形机器人公司在仓库场景做试点，合作方包括亚马逊、GXO、顺丰等。主要任务集中在物料搬运和分拣。\n\n人形机器人 VS 现有仓库自动化设备\n现有方案包括AGV/AMR、机械臂、分拣系统、AS/RS、传送带等，但自动化水平参差不齐。很多仓库即使上了自动化，仍然需要大量人工。\n\n人形机器人的核心优势是“灵活性”——可以像人一样适应不同任务，而不是像传统自动化设备那样只能做单一动作。这正好填补了现有方案的自动化盲区。\n\n💰 经济账：回本周期有多长？\n\n研报分\n\n[... middle omitted ...]\n\nd8d30040435bd10818b.jpg)\n\nMin-Joo Kang\n\n+852 2123 2644\n\nminjoo.kang@bernsteinsg.com\n\n![](images/26606b7bd8291b5be06e254e48c358098208674122a8c47c9d5132b4fe4f551d.jpg)\n\nWeibin Liang, Ph.D.\n\n+852\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R007",
    "title": "市场低估了“Tau定律”对半导体国产化的重塑力",
    "digest": "[wechat_article.md]\n# 市场低估了“Tau定律”对半导体国产化的重塑力\n\n当华为在ISCAS 2025上公布“Tau（τ）缩放定律”时，A股半导体板块随即大涨，科创50单日涨幅达5.9%。市场将其解读为又一个“DeepSeek时刻”，但这一定律的意义远不止于一次情绪催化。\n\n某外资投行最新研报的核心判断是：Tau定律提供了一条在EUV光刻机受限条件下，可预测、可规模化、持续十年的芯片性能提升路线图。它不是对摩尔定律的简单修补，而是从根本上将优化目标从“几何缩放”（把晶体管做得更小）转向了“时间缩放”（把信号延迟降到最低）。\n\n这一定律一旦被工程化验证，将从根本上改写中国半导体产业的估值逻辑——从“追赶者”切换到“另辟赛道者”。而市场目前定价的，更多是情绪，而非这一结构性变化的长期含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Tau定律的真正突破，不是堆叠本身，而是“Cell-to-Cell”的延迟压缩\n\n华为提出的Tau定律，核心是系统性地压缩整个计算栈中每个环节的信号延迟τ。其中最引人注目的技术是“LogicFolding”——一种将逻辑、存储、模拟电路垂直堆叠的3D集成方案。\n\n乍看之下，这与台积电的SoIC（系统集成芯片）类似。但关键区别在于堆叠的粒度：台积电的SoIC是Die-to-Die堆叠（通常是将SRAM堆在逻辑上），而华为的LogicFolding实现了sub-2微米的键合间距，能够在Cell-to-Cell层面进行堆叠。这意味着，他们可以将逻辑单元中的组合逻辑和时序逻辑直接垂直堆叠，从而大幅缩短相邻晶体管之间的关键路径延迟。\n\n这一突破的直接效果是：在2025年基于SMIC N+3工艺的麒麟9030上，晶体管密度为155 MTr/mm²；而通过LogicFolding，华为预计2026年就能达到238 MT\n\n[... middle omitted ...]\n\n分析，以及后续对华为Mate90和昇腾下一代芯片的跟踪解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n华为Tau定律：中国芯片的DeepSeek时刻\n\n中国芯片新路径\n\n华为在ISCAS 2025上提出了Tau（τ）缩放定律，这次不再是摩尔定律的跟随者。\n\n刚看到这份投行研报时，我第一反应是：中国半导体又有新故事了。但仔细读完，发现这次确实不一样。\n\n**什么是Tau定律？**\n\n简单来说，华为提出从“几何缩放”（把晶体管做小）转向“时间缩放”（减少信号延迟）。核心思路是通过系统性地降低整个芯片堆栈的信号延迟，来持续提升性能。\n\n这就像以前我们努力把房间隔得更小来住更多人，现在华为说：不如把房间之间的走廊缩短，让人走动更快。\n\n**三个关键技术突破**\n\n1️⃣ **LogicFolding技术**：看起来类似台积电的SoIC，但华为做到了sub-2μm的键合间距。这意味着他们能把逻辑芯片直接堆叠在逻辑芯片上，实现“cell to cell”级别的堆叠，而不是简单的“die to die”。这带来了密度和频率的双重提升。\n\n2️⃣ **晶体管密度目标**：从2025年的155 MTr/mm²，到2026年达到238 MTr/mm²（相当于台积电N3密度），到2031年目标400+ MTr/mm²。注意，这里是\n\n[... middle omitted ...]\n\n shift from geometric scaling (making transistors smaller) to temporal scaling (reducing signal latency) as a successor to Moore's Law. A-share semis names rallied yesterday (STAR 50 +5.9%). W\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R008",
    "title": "市场低估的不是加密货币，而是资产上链对金融基础设施的重构",
    "digest": "[wechat_article.md]\n# 市场低估的不是加密货币，而是资产上链对金融基础设施的重构\n\n代币化现实世界资产（RWA）的总市值已突破510亿美元，年内增长42%，而同期更广泛的加密市场下跌约15%。这一数据背后隐藏着一个被多数人忽视的结构性信号：真正在推动资金流入的，不是比特币或以太坊的价格叙事，而是一套正在悄然成型的、将传统金融资产迁移至区块链的新基础设施。某外资投行最新发布的研报《The Tokenization Memo》系统梳理了这一趋势，其核心判断值得我们认真对待——代币化不是加密货币的附属品，而是传统金融体系自身效率革命的下一站。\n\n这份报告的价值不在于罗列数据，而在于它揭示了一个关键转折：从“加密原生资产”到“现实世界资产上链”的叙事迁移正在发生，而且参与方不再是散户，而是BlackRock、DTCC、NYSE、Citi、JPM等传统金融的基石机构。当这些名字开始集体建设代币化基础设施时，我们面对的不再是投机浪潮，而是制度性变革。\n\n以下是我们从这份研报中提炼出的五层洞察，每一层都在回答同一个问题：为什么说代币化正在改变金融基础设施的底层逻辑？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 代币化的增长韧性暴露了加密市场的一个认知盲区\n\n截至2026年5月，代币化RWA总市值约510亿美元，较年初增长42%。同期比特币和以太坊价格分别下跌约15%和20%。这一背离值得反复咀嚼。\n\n传统解读认为，加密市场下行是因为宏观流动性收紧、监管不确定性上升。但代币化资产在同一环境下逆势增长，说明它的驱动因素与加密原生资产并不完全重叠。代币化资产的买家不是追逐alpha的散户，而是寻求效率提升的机构。当加密市场因投机情绪退潮而下跌时，代币化资产反而因真实业务需求而扩张。\n\n这意味着什么？代币化资产的定价逻辑正在与加密原生资产脱钩。它的增长\n\n[... middle omitted ...]\n\n的拆解，逐一审视每个关键假设的合理性，并追踪后续的行业动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n现实世界资产上链，正在加速\n\nRWA代币化\n规模已超510亿美元\n\n投行研报认为，代币化是加密资产向现实世界延伸的核心趋势之一。目前代币化RWA市场规模已超过510亿美元，年内增长42%，而同期整体加密市场下跌约15%。这说明机构资金正在寻找更稳健的链上资产载体。\n\n1/ 私人信贷依然是主力\n私人信贷占RWA总市值的44%，美国国债占30%，大宗商品占14%。以太坊和Provenance链承载了约75%的代币化资产。持有RWA的钱包地址已超过81万个，年内增长40%。\n\n2/ Hyperliquid上的RWA衍生品爆发\nHyperliquid的HIP-3升级允许开发者上线挂钩股票、商品、外汇等的永续合约。上线不到8个月，RWA衍生品已占该平台永续合约交易量的35%。今年4月，RWA衍生品贡献了650亿美元的交易量，商品和指数是主要品种。\n\n3/ 股票代币化：机构跑步入场\n尽管SEC推迟了“创新豁免”，但机构通过发行人主导模式推进股票代币化。目前代币化股票存量约15亿美元，月转移量30亿美元。关键动态：\n- Bullish收购全球过户代理Equiniti，服务约3000家发行人\n- DTCC联合50多家金融机构\n\n[... middle omitted ...]\n\nthe latest industry dashboards, news and market commentary. The Digital Assets memo shall continue to cover the latest in crypto markets.\n\nTokenized RWA Industry Metrics - Tokenized real-world\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "全球储能市场正在经历一场“去中国化”无法完成的供应链重构",
    "digest": "[wechat_article.md]\n# 全球储能市场正在经历一场“去中国化”无法完成的供应链重构\n\n如果你只关注关税和地缘政治，你会错过一个更根本的变化：全球电池供应链正在从“谁便宜买谁”转向“谁的技术生态更完整，谁就能定义规则”。这不是一个关于成本的故事，而是一个关于控制权的故事。\n\n最近一周，某外资投行发布的全球储能周报中，密集披露了多条看似独立、实则指向同一趋势的信号。福特将旗下合资工厂BlueOvalSK肯塔基工厂的韩国电池设备全部替换为CATL技术，并转向LFP磷酸铁锂体系，主要服务于储能市场。Stellantis宣布了700亿美元的反击计划，核心策略之一是采用LFP电池和Cell-to-Body结构。LG Energy Solution开始大力布局LMR锂锰富集电池专利，并与GM合作量产。Gotion获得西班牙9200万欧元政府补贴，建设正极材料和回收工厂。POSCO Future M的硅负极技术计划在2028年量产，目标不仅是电动车，还包括人形机器人和固态电池。\n\n这些事件叠加在一起，指向同一个主判断：全球储能行业的竞争已经从“产能竞赛”进入“技术生态与供应链主权”的新阶段。谁能在下一代电池技术、关键材料、制造设备和回收闭环中建立完整生态，谁就能在未来的产业格局中掌握定价权。而中国企业的优势，比市场通常理解的更深、更系统。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 福特工厂的“去韩国化”不是偶然，而是中国技术生态外溢的标志性事件\n\n福特将BlueOvalSK肯塔基工厂从韩国供应商的NCM软包路线，全面转向CATL的LFP棱柱电池技术，并服务于储能市场，这在行业内的意义远超一笔订单。韩国设备供应商——Hana Technology、MPLUS、Toptec、Yunsung F&C、PNT等——的订单被取消或闲置。这不是一个\n\n[... middle omitted ...]\n\n的数据，进一步拆解非中国供应链的成本曲线和时间表。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球储能市场正在发生什么？5月重点事件速览\n\n储能行业关键转折点\n\n从美国到中东，从韩国到中国，储能格局正在快速重塑。\n\n1️⃣ 美国市场：中国技术替代韩国供应商\n福特旗下的BlueOvalSK肯塔基工厂，在SK On与福特合资拆分后，正用CATL技术将NCM电池产线改为LFP棱柱电池，主要服务ESS市场。韩国设备供应商订单被取消或闲置。SK On控制的田纳西工厂则推迟到2028年，前景依赖新订单。\n\n2️⃣ 中东大项目：阳光电源拿下7.5GWh订单\n与Masdar签约，为阿联酋全天候可再生能源项目提供PowerTitan 3.0液冷储能系统。项目总配储19GWh，采用8小时充电/16小时放电模式，可在55°C高温下无降额运行。这是继沙特7.8GWh项目后的又一中东大单。\n\n3️⃣ 固态电池加速：赣锋、蜂巢、LG各有进展\n- 赣锋锂业开始小批量生产500Wh/kg锂金属固态电池，10Ah规格，400Wh/kg版本已超1100次循环。\n- 蜂巢能源计划2026年9月量产半固态电池，比原计划提前，第一代约300Wh/kg，第二代目标360Wh/kg。\n- LG能源加强LMR（富锂锰基）电池专利布局，与GM合作量产\n\n[... middle omitted ...]\n\non to prismatic LFP batteries using CATL technology, mainly for the ESS market under Ford Energy. As a result, equipment orders from Korean suppliers such as Hana Technology, MPLUS, Toptec, Yu\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R010",
    "title": "法国债券的夏季风暴尚未被市场定价",
    "digest": "[wechat_article.md]\n# 法国债券的夏季风暴尚未被市场定价\n\n欧洲利率市场正在进入一个微妙的窗口期。供应节奏、政治日程与评级行动将同时聚焦于法国主权债券，而市场当前的定价似乎尚未充分消化这一组合风险。\n\n这是某外资投行最新一期欧洲利率周报的核心判断之一。报告从期货持仓、供需节奏、投资者结构等多个维度，勾勒出一幅“表面平静、底层分化”的图景。对于关注欧元区利率走势的投资者而言，理解这些结构性变化，比跟踪每日收益率波动重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场最忽视的风险并非德国，而是法国夏季的供给与政治共振\n\n报告明确指出，法国国债将在未来几个月面临多重逆风，而当前估值尚未反映这些压力。\n\n首先是供给节奏。2026年法国净债券发行中，有45%集中在6月至8月这三个月。这意味着未来几周，法国国债的供给压力将显著高于其他核心欧元区国家。其次是政治日程。7月将迎来关于勒庞参选资格的关键裁决，随后总统选举周期将正式启动。报告担忧，政治与财政风险将提前对法国国债形成压力。\n\n第三是评级因素。穆迪对法国维持负面展望已近一年，按照其通常12至18个月的观察窗口，10月的审查节点可能触发评级行动。报告认为，市场目前对这一风险定价不足。\n\n这些因素叠加，使得法国国债相对于欧盟债券的利差存在走阔空间。报告建议做多欧盟10年期债券、做空法国10年期债券，目标利差从当前的30个基点走阔至40个基点。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 期货持仓的“核心化”趋势掩盖了真实的市场情绪变化\n\n从期货持仓数据看，德国国债曲线上的投资者情绪呈现明显的“核心化”特征。短端两年期Schatz期货是净多头最集中的合约，而十年期Bund和超长期Buxl则处于净空头或中性状态。意大利国债期货仍为净多头，法\n\n[... middle omitted ...]\n\n给日历、持仓分解图表，以及作者对上述未解问题的初步思考框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲债市正在悄悄换手，这些信号值得关注\n\n📊 债市持仓正在转向\n\n最近一份外资投行的欧洲利率研报，拆解了几个关键动向，信息量不小。\n\n1️⃣ 期货持仓：核心国债更受青睐\n\n德国国债期货全线转为净多头/空头减少，特别是短端DU合约净多最集中。而意大利国债期货空头增加，法国期货也在加空。\n\n⚠️ 不过研报也提醒：临近换月期，期货持仓作为市场情绪代理的可靠性在下降。\n\n2️⃣ 法国：夏季面临多重逆风\n\n研报点出三个市场可能低估的风险：\n- 45%的2026年法国国债净供给集中在6-8月\n- 预算季+勒庞候选人资格裁决（7月）+总统选举，政治和财政风险可能提前压制OAT\n- 穆迪维持负面展望，10月审查时已满12个月，通常在12-18个月窗口内会有评级行动\n\n估值目前似乎没有反映这些压力。\n\n3️⃣ 德国：央行和银行在买入\n\n3月数据显示：\n- 杠杆投资者净卖出30亿欧元德国国债，30年期流出最大\n- 银行净买入超130亿欧元，主要集中在短端和10年期\n- 央行净买入高达320亿欧元，2-10年期流入最多\n\n4️⃣ 供给：下周可能迎来多笔银团发行\n\n预计下周EGB拍卖供给150-180亿欧元。此外：\n- 葡萄牙取消拍\n\n[... middle omitted ...]\n\nas we begin to approach the rolling period, we grow increasingly hesitant in relying on futures positioning as proxy for broader market positioning/sentiment.\n\n# French headwinds, long 10y EU \n\n[... middle omitted ...]\n\ngive rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies."
  },
  {
    "id": "R011",
    "title": "市场真正低估的不是AI芯片，而是从电网到芯片的电力链路重构",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI芯片，而是从电网到芯片的电力链路重构\n\n当所有人都在关注英伟达下一代GPU的算力翻倍时，一个更根本的约束正在浮现：电力。这不是一个关于“数据中心需要更多电”的老生常谈，而是一个关于电力输送架构本身必须被彻底重写的结构性变化。某外资投行最新发布的AI电力半导体深度报告，揭示了这一变化的规模与含义：到2030年，仅AI数据中心从机架到芯片的模拟半导体市场，将从今天的79亿美元扩张至270亿美元。但真正值得关注的，不是这个数字本身，而是它背后隐含的竞争格局重塑——哪些公司将在电力链路重构中赢得定价权，哪些将被淘汰。\n\n报告的核心判断是：AI的规模化瓶颈正在从“算力”转向“电力输送效率”。当单机架功耗从传统服务器的10-15kW跃升至下一代平台的1.5MW以上时，现有的48V/12V供电架构已经无法支撑。这迫使整个电力链路——从电网接入、固态变压器、中间总线转换器，到GPU核心的电压调节模块——必须向800V直流架构迁移。这一迁移，为模拟半导体厂商创造了一个在汽车和工业周期之外、长期且确定性的增长市场。\n\n以下是我们从这份报告中提炼的五个关键洞察，以及它们对产业竞争格局和投资框架的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电力链路的“去中间商化”正在发生，最靠近芯片的组件获得最大价值增量\n\n报告最值得注意的分析框架，是将AI数据中心的电力链路拆解为“电网到机房”和“机架到芯片”两个独立的市场，并分别测算其价值分布。结论非常清晰：价值正在向最靠近加速器的环节集中。\n\n在“机架到芯片”这一环节，包括多相电压调节模块（VRM）、中间总线转换器（IBC）、以及用于光互连的模拟芯片。报告估算，单机架内容价值将从今天的3.6万美元，增长至600kW机架的近30万美元，并在兆瓦级机架时代接近100\n\n[... middle omitted ...]\n\n跟踪AI电力链路的重构进程，并分享完整报告的原始图表与数据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 数据中心，正在被电力卡脖子\n\n电力，才是 AI 新基建的硬门槛\n\n传统机柜 15kW，下一代直奔 1.5MW\n\n1️⃣ 算力密度在飙升，电力是新的稀缺资源\n\n当 GPU 从 H100 的 8 卡，演进到 Blackwell 的 72 卡，再到未来 Feynman 的 576 卡，单机柜功耗从 10-15kW 直接跳到 1.5MW。\n这个数字什么概念？相当于一个机柜的用电量，接近 1000 个美国家庭。\n但电网扩容、变压器、燃气轮机的交付周期长达 2-5 年，电力成了比芯片更卡脖子的环节。\n\n2️⃣ 供电架构必须重构，800V 直流成为关键\n\n传统数据中心用 240V 交流电，但到了 600kW 以上的高功率机柜，电流太大、损耗太高。\n研报指出，行业正转向 800V 直流架构，这直接催生了两个新市场：\n- 数据中心内部（机柜到芯片）：从 76 亿美元增长到 250 亿美元（CAGR 27%）\n- 基础设施侧（电网到机房）：从 2.45 亿增长到 18 亿美元（CAGR 49%）\n\n3️⃣ 模拟芯片厂迎来结构性机会\n\n电力从“机柜到芯片”的路径上，价值量最高的环节在靠近 GPU 的位置：\n- 多相电压调节模\n\n[... middle omitted ...]\n\n from cyclical auto/industrial demand toward secular, durable AI markets, where diverse architectures, new components, novel materials (wide-bandgap semis), and products create an unparalleled\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R012",
    "title": "市场真正低估的不是成交量，而是价格预期的自我强化",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是成交量，而是价格预期的自我强化\n\n五月第四周，中国房地产市场的周度数据呈现出一个看似矛盾的状态：成交量整体平稳，但几乎所有领先指标都在减速。某外资投行最新发布的周度追踪报告显示，新房成交量环比下降4%、同比下降5%，二手房成交量环比微增1%、同比仍保持11%的增长。表面上看，市场似乎处于一种“量稳价弱”的僵持状态。\n\n但这份报告真正值得关注的信号，并不在于周度成交量的波动，而在于价格预期的系统性走弱。二手房市场的中介信心指数（CSI）连续第三周下跌，周环比下降1.6个百分点；业主挂牌价预期指数（CAI）也同步下滑0.4个百分点。更关键的是，看房量和认购量双双环比下降7%。这意味着，当前市场的成交量稳定，可能更多是存量挂牌的去化，而非新增需求的持续入场。\n\n这不是一个简单的周期性波动。报告揭示了一个正在形成的结构性风险：价格预期的下行正在从短期波动演变为自我强化的趋势。当买方的观望情绪和卖方的降价预期同步强化，市场可能进入一个“量稳价跌”的新阶段——成交量尚未显著萎缩，但价格的底部在不断被重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 上海“以旧换新”的试点数据，暴露了政策传导的真实效率\n\n作为本轮政策工具箱中最受关注的手段之一，上海的住房“以旧换新”机制在推出三个月后，交出了第一份可量化的成绩单。截至5月中旬，三个试点区域共完成523套住房收购。但这份成绩单需要细看：徐汇区一个区就占了近90%的收购量，且这些房源主要针对的是结构受限的老旧住宅，属于城市更新范畴的定向操作。浦东新区虽然也有收购，但额外附加了“年化租金收益率需超过2.5%”的门槛条件。\n\n这意味着什么？所谓“以旧换新”，在当前阶段更像是一个精准的定向工具，而非普惠性的市场激活器。它能够解决特定区域、特定类型房源的流动性\n\n[... middle omitted ...]\n\n难在一篇周度解读中完全展开，但恰恰是判断市场拐点的关键拼图。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n上海二手房换新：3个月成交523套，徐汇占9成\n\n上海二手房“以旧换新”成绩单\n\n上海3个试点区3个月换房523套，徐汇占近9成\n\n最近投行研报跟踪了上海二手房“以旧换新”进展，数据挺有意思，拆开来聊聊。\n\n1️⃣ 政策推进：3个月523套，徐汇是主力\n上海“以旧换新”试点3个月，截至5月累计成交523套。其中徐汇区占近9成，主要针对老旧、结构受限的房源，作为城市更新的一部分。浦东也有少量成交，但多了一个门槛：房源年租金收益率需高于2.5%。目前政策已扩展到上海所有中心城区，这些区域在2025年占上海新房交易的约40%、二手房交易的约50%。\n\n2️⃣ 市场表现：新房微降，二手房量稳但预期走弱\n新房方面，上周成交面积环比降4%，同比降5%。二手房成交环比微增1%，同比增11%，但领先指标全面走弱：带看量和认购量环比均降7%；经纪人预期指数（CSI）环比降1.6个百分点，连续3周下滑；卖家挂牌价预期指数（CAI）环比降0.4个百分点。好消息是新增挂牌量也降了7%，5月累计挂牌量比4月低8%、比去年5月低20%，这对稳定成交价有支撑。\n\n3️⃣ 库存与竣工：库存微降，竣工仍承压\n20城库存环比降0.2%，去化周期\n\n[... middle omitted ...]\n\nts to generate an annual rental yield above 2.5%). We also note the program has now expanded to include all central districts, which collectively accounted for \\~40% of new home transactions a\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "小鹏GX单周2.5万不可退订单背后，市场真正低估的是“爆款能力”对竞争格局的重塑",
    "digest": "[wechat_article.md]\n# 小鹏GX单周2.5万不可退订单背后，市场真正低估的是“爆款能力”对竞争格局的重塑\n\n过去几周，中国新能源汽车市场的周度订单数据出现了一个值得深入解读的信号。根据某外资投行最新发布的周度追踪报告，2026年第21周（5月18日至5月24日），主要新能源品牌合计订单环比增长16%，同比增长9%。单看这个数字，似乎只是季节性回暖。但拆开结构，真正驱动这一轮反弹的，不是价格战，不是政策刺激，而是新车型的集中爆发——尤其是小鹏GX在发布后12小时内斩获近2.5万张不可退订单，直接推动小鹏单周订单环比暴增433%。\n\n市场往往把注意力放在月度销量、渗透率曲线和价格折扣上，这些固然重要。但这份报告揭示了一个更值得关注的变量：在行业整体增速放缓、渗透率接近60%的背景下，爆款车型的订单集中度正在急剧上升。这意味着，竞争已经从“谁卖得多”转向了“谁能定义下一款爆款”。而后者，对利润、品牌和供应链的冲击力，远大于前者。\n\n本文基于该报告的核心数据，提炼出四个层次的洞察：爆款订单如何改变品牌排位，价格折让持续扩大意味着什么，电池成本下行是否被充分定价，以及报告尚未完全回答的关键问题——这些爆款的订单转化率和可持续性如何。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 爆款订单的集中度正在改写品牌梯队，而非简单的“强者恒强”\n\n第21周的数据最突出的特征是订单增长的极度不均衡。小鹏环比增长433%，小米增长92%，吉利增长77%。这三个品牌的共同点是什么？都有新车型在当周进入订单爬坡期。小鹏GX、小米的某款新车型、吉利旗下的新序列，各自贡献了品牌当周订单的绝大部分增量。\n\n与之形成对比的是，比亚迪、理想、蔚来等品牌的周度订单环比增长仅为4%、-18%和-44%。蔚来更是在当周出现了环比大幅下滑，尽管其5月累计订单同比仍有86%的增长\n\n[... middle omitted ...]\n\n会定期分享更完整的研报解读，以及基于高频数据的实时跟踪分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新车型引爆周订单，小鹏单周逼近3万\n\n新能源周订单回暖\n\n小鹏GX首日狂揽2.5万单\n\n最近新能源市场有点意思，5月第三周订单环比涨了16%，同比也涨了9%。📊\n\n**新车型是绝对主角**\n\n小鹏GX绝对是这周的爆款。发布后12小时就拿下了近2.5万不可退订单，直接带动小鹏周订单环比暴涨433%，单周冲到2.88万台。\n\n纯电版GX占了总订单的62%——说明消费者对纯电的接受度还在走高。\n\n小米和吉利也表现亮眼，周订单分别涨了92%和77%，同样得益于新车型的拉动。\n\n**整体数据怎么看**\n\n5月1-17日，新能源零售40万台，渗透率58.9%。虽然同比下滑12%，但环比还是有18%的增长。\n\n批发端渗透率到了59.9%，比4月的57.3%提升了2.6个百分点。\n\n**价格战还在继续**\n\n新能源经销商平均折扣扩大到7.79%，比上周又宽了0.18个百分点。\n\n燃油车更猛，折扣率到了19.67%。\n\n电池级碳酸锂价格跌到18.1万/吨，环比降了5.2%。但电芯价格倒是稳住了。\n\n**下周值得关注**\n\n5月27日蔚来ES9正式发布，同天赛力斯M9改款也要上。\n\n5月28日理想和小鹏都要发Q1财报。\n\nBYD\n\n[... middle omitted ...]\n\nvents to watch, (3) NEV/ICE dealer price discount tracker, and (4) Upstream battery pricing dynamics.\n\n# 2026 Week 21 highlights:\n\nKey brand orders: XPeng / Xiaomi / Geely showed the highest g\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "霍尔木兹海峡若重启，南非资产真正的赢家不是你想的那样",
    "digest": "[wechat_article.md]\n# 霍尔木兹海峡若重启，南非资产真正的赢家不是你想的那样\n\n一份来自某外资投行的最新南非策略报告，提出了一个看似反直觉的判断：当霍尔木兹海峡重新开放时，最值得买入的并非那些在冲突期间跌幅最深的“抄底”标的，而是贵金属、零售与金融板块。但报告真正的洞察，不在于这份清单本身，而在于它揭示了市场对“重启交易”的定价方式存在系统性偏差——投资者过于关注地缘政治风险的消退，却低估了供应链重构带来的二阶效应，以及南非国内资产在汇率升值背景下的结构性重估。\n\n这份报告发布于冲突进入第12周之际，其基准假设是海峡将于6月重新开放。尽管分析师对短期内达成协议仍持谨慎态度，但过去几天伊朗高级官员飞往多哈、特朗普表示协议“已基本谈妥”等信号，正在收窄市场对“不可能”的定价区间。报告的核心价值在于：它提供了一套可重复的因子筛选框架，用以识别那些在重启后6-12个月内最有可能跑赢的标的，而不是仅仅给出一个“买南非”的笼统建议。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对“重启交易”的定价，忽略了从油轮短缺到库存重建的传导链条\n\n大多数投资者对海峡重启的理解是线性的：航线恢复，油价下跌，通胀压力缓解，南非贸易条件改善，兰特走强，国内资产受益。但报告揭示了一个更复杂的图景——即便海峡重启，石油市场的瓶颈将从物理通道转移到油轮可用性和强劲的补库需求。该投行已将2026年布伦特原油均价预测维持在96美元/桶，这意味着油价即使在重启后仍将“黏性”地停留在100美元/桶出头的水平。\n\n这个判断对南非资产定价的含义是根本性的。如果油价不会大幅回落，那么南非的通胀路径和利率预期就不会出现市场目前隐含的快速下行。报告预测南非今年仍需加息50-75个基点，同时将经济增长预期从1.2%下调至1.0%。这意味着，重启交易的第一波驱动力不会是“宏观基本面\n\n[... middle omitted ...]\n\n跟踪报告中的关键变量，并与大家分享最新的数据更新和逻辑推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 霍尔木兹海峡若重开，南非哪些板块值得看\n\n**南非策略：海峡重开买什么**\n\n**某外资投行因子筛选：贵金属、零售、银行排前列**\n\n---\n\n某外资投行最新研报，针对霍尔木兹海峡可能重开的情景，建立了一套多因子评分体系，筛选南非市场短期值得关注的板块和个股。\n\n先说结论：**贵金属板块评分最高，零售和银行紧随其后。**\n\n---\n\n**1/ 为什么现在讨论这个？**\n\n当前是冲突第12周，虽然解决时间不确定，但该行大宗商品团队预计6月可能重开，周末伊朗官员飞往卡塔尔、特朗普称“协议基本谈妥”，让市场开始提前布局。\n\n他们判断：一旦海峡重开，南非将受益于贸易条件改善（金价/PGM维持高位）、兰特走强，海外资金重新入场，国内主题会重新启动。\n\n---\n\n**2/ 因子评分怎么打的？**\n\n总分10分，权重如下：\n\n- 估值（相对EM同业 + 相对10年均值）：30%\n- 3个月EPS动量：20%\n- 对EMFX/兰特β：25%\n- 相对JSE基准近3个月跌幅：25%\n\n**评分≥7分算有吸引力。**\n\n---\n\n**3/ 哪些板块评分高？**\n\n**贵金属板块几乎全满分（10分）**：Gold Fields\n\n[... middle omitted ...]\n\nnc. theme to resume once the Strait opens, which will translate to stronger ToT (higher Gold/PGMs), a stronger ZAR and a broadening appeal for domestic equities as the marginal buyer (offshore\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 25 May 2026 05:24 PM BST\n\nDisseminated 26 May 2026 12:15 AM BST"
  },
  {
    "id": "R015",
    "title": "市场真正低估的不是需求韧性，而是供给侧的永久性收缩",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求韧性，而是供给侧的永久性收缩\n\n过去几个月，地缘冲突带来的化工品价格飙升，让几乎所有上游化学品公司的股价都经历了一轮剧烈波动。市场的主流叙事是：一旦和平协议落地，这些临时性的供给冲击就会消退，价格和利润将回归常态，届时股价必然面临回调。\n\n这个逻辑听起来无懈可击，但它隐含了一个关键假设——当前的高价是纯粹由战争造成的短期现象。某外资投行最新发布的长篇研报提出了一个截然不同的判断：市场真正低估的不是需求端的韧性，而是供给侧正在发生的结构性、永久性收缩。如果这个判断成立，那么当前股价的任何“和平回调”都可能成为一个值得认真考虑的长期买入窗口。\n\n这份研报的核心主张非常明确：即便冲突结束，上游化工品的供给曲线已经发生了不可逆的抬升。报告将其长期聚烯烃价格预测上调了5%至15%，并明确指出，对于巴斯夫、博禄、SABIC等标的，过去几年的估值底部可能已经永久性地抬高了。\n\n以下是我们基于该报告核心逻辑的深度解析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供给侧的“永久性”不是修辞，而是三种力量叠加的结果\n\n市场倾向于将当前50%的全球乙烯和聚乙烯产能受影响视为一个“开关”——和平协议签署，开关打开，产能恢复。但报告提出了一个更深刻的框架：即便大部分产能重启，仍有相当一部分产能将永久消失。这不是修辞，而是三种独立力量共同作用的结果。\n\n第一，物理性资产损毁。报告特别提到卡塔尔的LNG设施遭受了持久性破坏。对于中东地区大量以天然气为原料的化工装置而言，原料供应的基础设施修复需要数年时间，且成本极高。部分老旧装置在经济账上已经不值得修复。\n\n第二，地缘政治驱动的“再区域化”。冲突改变了全球供应链的风险定价。过去二十年，亚洲和中东凭借成本优势成为全球化工品的主要供应地。但当前的环境正在迫使各国重新评\n\n[... middle omitted ...]\n\n投资领域的朋友一起，围绕这些尚未完全解答的问题继续深入探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东冲突后，化工行业格局变了\n\n上游化工的长期机会\n\n某外资投行最近出了一份深度研报，专门分析中东冲突对上游化工的长期影响。我读完觉得逻辑很清晰，分享给大家参考。\n\n核心判断：这次危机可能不是简单的短期冲击，而是会带来行业结构的长期改善。\n\n1️⃣ 供需格局正在改善\n- 需求端：石化产品跟日常消费紧密相关，过去20年只有2007-09年需求下降过，韧性很强\n- 供给端：虽然大部分停产产能会恢复，但预计会有永久性减产\n- 研报认为，之前亚洲的过剩产能被有效消化，市场从供过于求转向供不应求\n\n2️⃣ 长期价格预期上调\n- 研报用自有的聚烯烃供需模型，综合考虑开工率、GDP增长和原油价格\n- 预计2027-30年聚烯烃价格将上调5-15%\n- 虽然GDP可能受影响，但更好的供需关系和更高的油价足以抵消\n\n3️⃣ 成本曲线变得更陡峭\n- 天然气为原料的生产商（中东、北美）优势更明显\n- 但北美面临Henry Hub天然气可能涨到5美元的风险\n- 油基原料地区，一体化程度高的企业（如BASF）更有优势\n\n4️⃣ 值得关注的长期变化\n- 中东生产商在物流成本正常化后，竞争优势会进一步扩大\n- 北美天然气价格若持续低于5美\n\n[... middle omitted ...]\n\nbc4697db366ff2c41524bb7a68983674362f360ffe9ab.jpg)\n\nJames Brady\n\n+44 20 7762 5272\n\njames.brady@bernsteinsg.com\n\n![](images/56e6e99a75ee9f461c3dbafef0fa2b7f5b5df285802b7f1101fdae6421737992.jpg)\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R016",
    "title": "土木工程服务行业真正被低估的，是结构性需求切换对头部企业的重新定价",
    "digest": "[wechat_article.md]\n# 土木工程服务行业真正被低估的，是结构性需求切换对头部企业的重新定价\n\n当一家公司的股价在财报发布日一天内上涨18%，而同行普遍下跌2%到12%，市场在传递一个远比“季度业绩好坏”更深的信号。\n\n某外资投行最新发布的土木工程服务行业季度报告，跟踪了Arcadis及其八家全球可比公司的截至3月业绩。这份报告揭示了一个反直觉的图景：行业整体需求并未因中东冲突和经济不确定性而崩塌，但资本市场对各家公司的定价却出现了罕见的巨大分化。\n\n真正值得关注的不是“需求好不好”，而是“谁有资格承接结构性的新需求”。\n\n报告的核心判断是：土木工程服务行业正在经历一场需求侧的结构性切换——数据中心、生命科学、核能等新领域的高速增长，正在取代传统住宅和商业建筑的下行。但市场目前只看到了“某些公司增长快”，尚未充分定价的是：这一轮切换将永久性地改变行业竞争格局，并重塑头部公司的估值体系。\n\n对于持有或关注Arcadis的投资者而言，这份报告提供了三个层次的关键信息：需求端并未恶化，但增长的质量比速度更重要；M&A正在成为区分赢家和输家的分水岭；以及，市场可能低估了运营效率改善对利润率的杠杆效应。\n\n以下是我们基于这份报告的深度解析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 客户需求韧性超出预期，但增长分布正在发生根本性位移\n\n报告覆盖的样本公司在截至3月的季度中，有机收入增长总体与前一季度持平，并未出现市场此前担忧的显著放缓。更重要的是，季度收入和EBITDA整体超出市场预期2%和1%。在一个充斥着地缘政治不确定性的环境下，这本身就是值得注意的信号。\n\n但真正关键的不是总量的韧性，而是结构的位移。\n\n报告明确指出，需求加速最显著的领域是数据中心、生命科学和核能。这三者有一个共同特征：它们都是长期资本开支驱动的结构性需求，而非周期性\n\n[... middle omitted ...]\n\n读和关键图表的原始数据，也欢迎你带着自己的判断和分析来碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲工程服务板块：一季度业绩全解析\n\n**工程板块最新动向**\n\n数据中心的建设需求正在爆发，这是我看完某外资投行最新研报后最直接的感受。\n\n**1. 需求韧性十足，但分化明显**\n\n一季度工程服务企业整体有机收入增长与上季度基本持平，营收和EBITDA分别超出市场预期2%和1%。但亮点集中在特定领域——\n\n数据中心、生命科学、核能相关需求加速增长。部分公司如AtkinsRéalis和Jacobs实现了5%以上的有机增长。\n\n**2. 这些公司表现更突出**\n\n• **Arcadis**：唯一一家有机增长环比加速的企业\n• **Jacobs**：在手订单创纪录达270亿美元，同比增长22%，AI相关收入已占集团收入约10%\n• **AtkinsRéalis**：工程服务板块实现5%有机增长\n\n中东地区业务、住宅建设相关板块则拖累了Stantec、Sweco等公司的表现。\n\n**3. M&A活跃度显著提升**\n\nWSP Global最活跃，完成TRC收购；Jacobs完成PA Consulting整合；Stantec受益于此前收购Page的贡献。而Arcadis选择专注运营改善，暂未跟进并购潮。\n\n**4. 业\n\n[... middle omitted ...]\n\necond edition of our quarterly report (link to the first issue here) in which we analyze the results published by Arcadis's listed competitors. Within the sector, we cover Arcadis (Outperform,\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R017",
    "title": "全球超主权债供给的结构性拐点尚未到来，但驱动逻辑正在切换",
    "digest": "[wechat_article.md]\n# 全球超主权债供给的结构性拐点尚未到来，但驱动逻辑正在切换\n\n2026年过半，全球固定收益投资者面临一个看似矛盾的局面：超主权债（Supra/SSA）的供给总量仍在高位，但增长动能正在发生根本性分化。某外资投行最新研报的数据显示，截至2026年5月，全球主要超主权发行人的年内总供给已达2547亿欧元等值，相当于2025年全年的52%。如果仅看这个比例，似乎一切正常——全年供给有望与2025年持平甚至略高。\n\n但真正需要关注的，不是总量的绝对值，而是结构的变化。世界银行体系（IBRD、IFC、IDAWBG）的供给出现了断崖式下滑，而欧洲超主权发行人（尤其是EU）的供给仍在加速。这一分化背后，是地缘政治格局、主权信用质量分化以及监管框架变迁三重力量的交汇。\n\n报告的核心判断是：全球超主权债市场正在经历从“规模驱动”向“质量驱动”的切换。过去两年供给的爆发式增长，在2026年可能难以复制，但市场的定价逻辑将从“供给压力”转向“信用稀缺性”。这对资产配置的含义是，超主权债的风险溢价需要被重新评估，尤其是那些具备优先债权人地位（PCS）和充足实缴资本的结构。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 世界银行体系供给骤降，是周期性回撤还是结构性拐点？\n\n最引人注目的变化来自世界银行体系。IBRD的年内供给仅为167亿欧元等值，相比2025年全年的593亿欧元，同比降幅显著。IFC和IDAWBG的情况类似，前者年内供给79亿欧元等值（2025年全年为242亿），后者仅为20亿欧元（2025年全年为199亿）。以美元计价来看，IBRD和IFC的美元供给同比均下降了71%。\n\n这一下降并非偶然。世界银行体系的财年是从7月1日到次年6月30日，因此截至5月的供给数据确实会受到财年节奏的影响。但即便如此，下降幅度之大，已经超出\n\n[... middle omitted ...]\n\n报原文、原始图表以及我们的扩展分析笔记，也都会在社群内分享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n加拿大监管新规：担保债券（CB）流动性升级\n\nCovered Bonds 流动性新规\n\nOSFI 拟将 CB 纳入 LCR 1B 级资产\n\n最近，加拿大金融机构监管局（OSFI）公开征求意见，计划在2027年流动性充足指引（LAR）中，将高评级担保债券（CB）纳入LCR 1B级合格优质流动性资产（HQLA），并适用7%的折扣率。\n\n1/ 目前，在巴塞尔III框架下，高评级CB通常被归为LCR 2A级资产，折扣率为15%。而在欧盟，只有获得“欧盟覆盖债券优质标签”的CB才能享受LCR 1级待遇（7%折扣）。OSFI的提议实际上超越了巴塞尔委员会的建议。\n\n2/ 为什么加拿大银行如此积极？截至当前，加拿大银行发行的CB规模高达1834亿欧元等值，其中46.5%以欧元计价，30.5%以美元计价。它们希望加拿大CB能在欧盟获得“第三国等效”认可，从目前的最高LCR 2A级提升至LCR 1级。\n\n3/ 时间线：公众咨询截止到2026年7月20日，预计2027年2月最终定稿，2027年5月1日实施。虽然距离生效还有近一年时间，但监管对CB的支持信号已经明确。\n\n全球超国家机构债券供应：2026年增速可能放缓\n\n今年截至目\n\n[... middle omitted ...]\n\nnce\" in the EU going forward (i.e. Canadian CB to be recognized as LCR Level 1 in the EU, instead of LCR level 2A at best currently.\n\nUnder Basel III framework, highly-rated CB are typically e\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R018",
    "title": "监管的代价不是一次性罚款，而是重构客户结构的长期成本",
    "digest": "[wechat_article.md]\n# 监管的代价不是一次性罚款，而是重构客户结构的长期成本\n\n2026年5月22日，中国证监会发布《全面整治非法跨境证券、期货、基金业务活动实施方案》。这不是2022年12月那轮监管的简单延续。当时，监管要求境外机构停止向境内投资者招揽新客户。这一次，监管直接给出了一条两年“整改期”，要求对存量不合规业务进行清理。\n\n市场当天用-28%和-25%的跌幅回应了富途和老虎的股价。但某外资投行最新发布的研报指出，市场对此次监管冲击的定价可能仍然不够充分。真正需要关注的，不是罚款金额本身，而是监管如何从根本上改变了这两家公司的客户结构、获客成本与单客户价值。\n\n这份研报的核心判断是：罚款是一次性冲击，但客户结构调整是永久性的。富途和老虎未来几年的利润增长将同时面临收入端流失和成本端上升的双重挤压。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 罚款是已知的，但存量客户清理的财务影响仍被低估\n\n罚款金额已经明确。富途被罚18.5亿元人民币，老虎被罚4.12亿元。按照该投行的测算，这两笔罚款在2026年对富途和老虎的净利润影响分别为-2.72亿美元和-0.61亿美元，分别占2025年净利润的-19%和-35%。\n\n但罚款只是起点。更大的影响来自存量不合规内地账户的清理。截至2026年一季度末，富途13%的付费客户来自内地，老虎内地客户占其客户AUM的10%。在两年整改期内，这些账户只能进行单向卖出交易和资金转出，不能新增买入或入金。这意味着这些账户将不再产生交易佣金收入。\n\n该投行测算，清理存量账户将使富途2026年净利润再减少1.21亿美元，老虎减少0.05亿美元。合计来看，监管对富途2026年净利润的总影响约为-3.93亿美元，相当于此前预测的-25%；对老虎的总影响约为-0.66亿美元，相当于此前预测的-60%。\n\n这里\n\n[... middle omitted ...]\n\n时间才能逐步显现。但提前建立分析框架，是做出独立判断的前提。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n富途与老虎：跨境监管落地，影响到底多大？\n\n监管重塑估值逻辑\n\n---\n\n最近某外资投行发布了一份关于互联网券商的深度研报，核心是评估5月22日中国证监会发布的跨境业务整治方案带来的影响。我把关键逻辑拆解了一下，信息密度比较高，值得收藏细看。\n\n**1/ 监管力度升级，从“禁止新客”到“全面清理”**\n\n2022年12月的监管主要禁止境外机构招揽新客户，而这次力度明显加强：\n- 要求2年内完成对现有不合规业务的“整改”\n- 整改期内，现有内地客户只能卖出、不能买入，也不能入金\n- 2年后，必须完全关闭面向内地客户的网站、交易软件和相关服务器\n- 富途和老虎分别面临18.5亿和4.12亿人民币的罚款\n\n**2/ 对业绩的影响：2026年是关键窗口期**\n\n投行预计罚款和客户清理带来的累计影响将集中在2026年下半年：\n- 富途：净利润预计减少3.93亿美元（约占2025年净利润的27%）\n- 老虎：净利润预计减少6600万美元（约占2025年净利润的38%）\n- 这导致2026年净利润预测分别下调25%和60%\n\n**3/ 估值逻辑被重塑，目标价大幅下调**\n\n投行参照2023-2024年监管周期，将目标市盈率\n\n[... middle omitted ...]\n\nnounced that online brokers including TIGR and FUTU will be subject to corresponding penalties. Both companies have since disclosed that these fines would amount to Rmb 1.85bn/412mn respective\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "集采续约的定价信号：市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 集采续约的定价信号：市场真正低估的不是需求，而是供给侧的再定价\n\n当市场还在用“集采=杀价”的线性逻辑给中国医疗器械公司定价时，一份关于冠脉药物洗脱支架（DES）第二次集采续约的报告，正在挑战这个前提。\n\n2026年5月20日，国家DES集采第二次续约结果公布。核心数字是：中标价格区间从2022年续约的730-848元，进一步上升至839-949元。这不是一次意外，而是继2022年首次续约出现5-76%的价格上涨之后，第二次价格上行。\n\n这意味着什么？集采不再是持续压价的工具，而正在变成一次性的价格重置机制。更关键的是，这个信号并非孤立事件。从创伤集采续约的价格修复，到关节集采的规则温和化，一条清晰的逻辑线正在形成：政策制定者的重心，已经从“压低价格”转向“稳定价格、保障供应、维护行业生态”。\n\n但市场定价是否已经充分反映了这一结构性转变？从当前估值水平看，答案很可能是否定的。这份研报提供了一个重新审视中国医疗器械板块的框架——不是从需求端，而是从供给侧定价权的再分配出发。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 第二次续约的价格上行，验证了集采从“砍价工具”到“定价机制”的范式转换\n\n2020年第一轮DES集采，价格从万元级直接压至798元，市场一度认为这是医疗器械行业的“末日”。但2022年首次续约时，价格不降反升，区间落在730-848元。当时市场将其解读为“一次性修复”，而非趋势。\n\n第二次续约彻底打破了这种怀疑。价格区间进一步上移至839-949元，有效价格上限从848元提高到949元。更重要的是，这一价格是在规则更加透明、量价挂钩更加清晰的框架下实现的。\n\n报告披露了分级分配机制：中标价848元以下的企业可获得90%的基础承诺量，848-898元区间对应75%，898-949元区间对应60%\n\n[... middle omitted ...]\n\n节。我们会在群里分享原始报告PDF，并持续跟踪后续政策变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n心脏支架集采续约，价格反而涨了？\n\n价格回升，外企回归\n\n某外资投行最新研报解析了国家冠脉支架集采第二轮续约结果，发现几个有意思的信号。\n\n1️⃣ 价格连续上涨\n- 本轮中标价区间839-949元，比2022年续约的730-848元继续上移\n- 最高有效报价从848元提升至949元，给了企业更多定价空间\n- 阶梯分配机制（90%/75%/60%）让企业可以更好平衡价格和量\n- 研报认为，集采正从持续压价转向一次性价格调整，医保局重心在稳定供应和行业生态\n\n2️⃣ 外企参与度明显回升\n- 波士顿科学、美敦力、雅培等跨国巨头总份额从首轮续约的32%提升至41%\n- 雅培增长最猛，从1%份额跳到13%，增长超16倍\n- 研报提到，创新能力和产品组合宽度在集采框架下越来越重要\n- 价格趋同后，医生和患者对跨国品牌的偏好可能延续\n\n3️⃣ 需求端依然强劲\n- 本轮申报需求量约273万根，较2022年续约复合增速14%\n- 参与医院从2408家扩到4468家，覆盖更广\n- PCI手术量预计从2022年129万例增至2025年221万例\n\n从数据看，冠脉支架集采已经走过最恐慌的阶段。价格企稳回升、外企重新入场、需求持续增长\n\n[... middle omitted ...]\n\ng prices, supply and overall industry economics. The pricing uptake was attributable to consistent bidding framework and clear volume-price linkage, including a higher effective price ceiling \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R020",
    "title": "中美生命科学合作面临新压力，但真正被低估的是行业的韧性再定价",
    "digest": "[wechat_article.md]\n# 中美生命科学合作面临新压力，但真正被低估的是行业的韧性再定价\n\n2026年5月21日，美国众议院“中国问题特别委员会”主席致信财政部，建议将生物技术纳入《综合对外投资国家安全法案》的禁止技术清单。这封信的导火索，是过去两年间中国生物科技公司与美国药企之间日益频繁的分子授权合作——信中专门点名了信达生物与礼来、恒瑞医药与百时美施贵宝的两笔近期交易。\n\n这并非美国首次对跨太平洋生命科学合作表达担忧。但这一次，市场似乎没有像以往那样剧烈反应：信达生物和恒瑞医药在公告合作后，股价并未出现显著异动。投资者已经对这类地缘政治噪音产生了“免疫”吗？还是说，市场正在用另一种方式定价这个行业的未来？\n\n某外资投行最新发布的研报给出了一个看似矛盾、实则深刻的判断：长期依然看好，但短期情绪压力不可忽视。真正值得关注的，不是地缘政治事件本身，而是这个行业正在经历的、被市场低估的供给侧再定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮压力测试的核心不是“脱钩”，而是合作模式的定价权转移\n\n这封信的提出背景，是中国生物科技公司从“me-too”模仿创新向“first-in-class”原创分子授权输出的结构性转变。过去两年，中国药企向美国合作伙伴授权早期分子的交易数量激增，交易结构也从单纯的许可费转向包含里程碑付款和销售分成的复杂安排。\n\n这封信之所以值得认真对待，不是因为它会立即变成法律——从提案到最终落地，涉及财政部、国会、美国制药企业、投资者等多方博弈，路径极不确定——而是因为它揭示了一个更深层的张力：美国政策制定者开始将“中国生物科技公司的创新能力”视为国家安全议题。\n\n但研报的核心洞察在于：生命科学领域的跨境合作，其经济规模和人类健康价值是万亿美元级别的。参照《生物安全法案》的实际影响路径，这类合作的基本盘大概率不会\n\n[... middle omitted ...]\n\n报精读和专题讨论，帮助读者穿透报告文本，建立自己的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国又出手了，但这次瞄准的是生物科技合作\n\n中美生命科学合作，还能继续吗？\n\n5月21日，美国众议院中国问题委员会主席致信财政部，建议将生物技术纳入《对外投资国家安全法案》的禁止技术清单。\n\n这不是第一次了，但这次针对性更强。\n\n1/ 背景：中美生物科技合作正在加速\n过去两年，中国药企向美国公司授权早期分子的案例激增。研报特别提到两笔大交易：\n- 信达生物与礼来\n- 恒瑞医药与百时美施贵宝\n正是这些合作，触动了美国某些人的神经。\n\n2/ 短期压力确实存在\n虽然市场对这两笔授权交易反应平淡（信达和恒瑞股价没怎么动），但研报认为，这种政策提案会压制板块情绪。毕竟，谁也不想看到自己关注的公司在合作上被卡脖子。\n\n3/ 长期逻辑依然成立\n研报的判断是：生命科学领域的跨境合作，本质上是人类进步的基石，也是万亿美元级别的产业。参考之前《生物安全法案》的实际影响，最终落地可能没那么极端。加上5月中旬中美领导人会晤释放的缓和信号，全面脱钩的概率不大。\n\n4/ 需要关注的变量\n- 美国药企的态度：他们是中国分子的主要买家，利益相关\n- 国会、财政部、投资者的博弈\n- 最终规则的具体条款\n\n研报没有给出明确的时间表或概率，但核心\n\n[... middle omitted ...]\n\nagainst the backdrop of surging collaboration between China and the US in life-science, mainly Chinese pharmaceuticals/biotech out licensing their early-stage molecules to US counterparts, ove\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R003",
    "label": "Figure 1",
    "context": "Figure 1: EM USD Aggregate 10s30s"
  },
  {
    "figure_id": "F002",
    "report_id": "R003",
    "label": "Figure 2",
    "context": "Figure 2: UST 10s30s yield curve slope"
  },
  {
    "figure_id": "F003",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "Figure 3: Steepest and flattest 10s30s curves"
  },
  {
    "figure_id": "F004",
    "report_id": "R003",
    "label": "Figure 4",
    "context": "Figure 4: Largest 1w changes in 10s30s"
  },
  {
    "figure_id": "F005",
    "report_id": "R003",
    "label": "Figure 5",
    "context": "Figure 6: 10s30s curves vs. the 10y level relationship"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Figure 7",
    "context": "Figure 7: 1w change in aggregate 10s30s vs. 1w change in aggregate 10 spreads"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Figure 8",
    "context": "Figure 8: 1w change in 10s30s vs. 1w change in 10y spreads by issuer Figure 9: Historical EM aggregate 10s30s spread curve slope"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Figure 8",
    "context": "Figure 8: 1w change in 10s30s vs. 1w change in 10y spreads by issuer Figure 9: Historical EM aggregate 10s30s spread curve slope"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Figure 11",
    "context": "Figure 11: Historical EMBIG vs. CEMBI spread curve slope"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Figure 13",
    "context": "Figure 13: Historical sovereign vs. quasi-sovereign curve slope"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Figure 15",
    "context": "Figure 15: Historical EMBIGD curve slope by region"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Figure 10",
    "context": "Figure 10: Historical US Treasury 10s30s yield curve slope"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Figure 12",
    "context": "Figure 12: Historical EM IG vs. HY spread curve slope"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Figure 14",
    "context": "Figure 14: EM corporate vs. US HG corporate spread curve slope"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Figure 16",
    "context": "Figure 16: Historical CEMBI curve slope by region"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Figure 17",
    "context": "Figure 17: 10s30s spread curve slopes vs. 10y spread"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Figure 18",
    "context": "Figure 18: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Figure 19",
    "context": "Figure 19: CEEMEA issuers"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "Figure 20",
    "context": "Figure 20: Latin America issuers"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Figure 21",
    "context": "Figure 21: 10s30s spread curve slopes vs. 10y spread"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Figure 22",
    "context": "Figure 22: EMBIG sovereign issuers"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Figure 23",
    "context": "Figure 23: EMBIG quasi-sovereign issuers Figure 24: CEMBI issuers # Slope versus Credit Rating Relationship Figure 25: 10s30s spread curve slopes vs. average credit rating"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Figure 23",
    "context": "Figure 23: EMBIG quasi-sovereign issuers Figure 24: CEMBI issuers # Slope versus Credit Rating Relationship Figure 25: 10s30s spread curve slopes vs. average credit rating"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Figure 24",
    "context": "Figure 24: CEMBI issuers # Slope versus Credit Rating Relationship Figure 25: 10s30s spread curve slopes vs. average credit rating"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Figure 26",
    "context": "Figure 26: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Figure 27",
    "context": "Figure 27: CEEMEA issuers Figure 28: Latin America issuers"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Figure 27",
    "context": "Figure 27: CEEMEA issuers Figure 28: Latin America issuers"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Figure 29",
    "context": "Figure 29: Steepest 10s30s spread curves across EM sovereign and corporate credit Figure 30: Steepest 10s30s curves vs. the 10y spread"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Figure 31",
    "context": "Figure 31: Steepest 10s30s curves and 1w change"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Figure 32",
    "context": "Figure 32: Flattest 10s30s spread curves across EM sovereign and corporate credit Figure 33: Flattest 10s30s curves vs. the 10y spread"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Figure 34",
    "context": "Figure 34: Flattest 10s30s curves and 1w change"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Figure 35",
    "context": "Figure 35: Largest 1w steepening across 10s30s spread curves Figure 36: 1w change in 10s30s curves vs. the current 10s30s"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Figure 37",
    "context": "Figure 37: Largest 1w steepening and current 10s30s slope"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Figure 38",
    "context": "Figure 38: Largest 1w flattening across 10s30s spread curves Figure 39: 1w change in 10s30s curves vs. the current 10s30s"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Figure 40",
    "context": "Figure 40: Largest 1w flattening and current 10s30s slope"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: After Stripping Out Increases in Equipment Imports and Other Special Factors, We Estimate That “Underlying” Domestic Capex Growth Picked Up to 5% in 2026Q1 from 2.4% in 2025 QoQ Annualized Real Nonresidential Fixed Inv"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "# AI Investment We expect AI-related spending to continue boosting equipment and structures investment in 2026 as companies press ahead with the infrastructure buildout. Over time, the impact on software and R&D should also become more visible as enterprise ad"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 3: We Estimate That AI-Related Spending Will Boost True Capex Growth by About 3.3pp and Measured Capex Growth by 2.8pp in 2026, With the Gap Reflecting Undermeasurement of Semiconductor Investment AI Spending Contribution"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We Estimate That AI-Related Spending Will Boost True GDP Growth by 0.3pp but Measured GDP Growth by Only 0.1pp in 2026, With the Gap Reflecting Undermeasurement of Semiconductor Investment and AI-Related Intellectual Pro"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: A Pullback in AI-Related Equipment Investment Would Barely Dent GDP Because Lower Imports Would Offset Much of the Hit, but a Broader Pullback in Structures and IPP Would Have a Meaningful Impact Impact of AI on 2026 C"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Early Evidence from 2026Q1 Reveals a Meaningful Increase in Capex Growth Among Categories Most Exposed to OBBBA's Expanded Expensing Provisions Estimated Impact of New OBBBA Tax Provisions on Growth of Nonresidential B"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Continue to Expect OBBBA to Boost Capex Growth by About 3pp in 2026 Impulse to QoQ Annualized Capex Growth From OBBBA Tax Provisions, GS Estimates"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Higher Energy Prices Have Not Led to a Meaningful Increase in Energy Capex in Recent Years, as Producers Have Prioritized Capital Discipline and Shareholder Returns Over Production Growth"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Higher Oil Prices Tend to Have a Modest Negative Impact on Non-Energy Equipment Capex, With the Pullback Concentrated in the Transportation Sector Impact of Oil Price Increases in GS Baseline on Industry-Level Equipmen"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Manufacturing Construction Subsidized by the Inflation Reduction Act and CHIPS Act Will Continue to Fall and Weigh on Capex Growth, but the Drag Will Gradually Fade from 1pp in 2025 to 0.6pp by 2026Q4"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: We Estimate That Higher Tariffs Lowered Capex Growth by 1.5pp in 2025 but Expect the Impact to Gradually Fade in 2026 Predicted Tariff-Driven Cost Increases* in 2025, by Type of Equipment Investment"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We Estimate That the Impact of AI Investment, New OBBBA Tax Provisions, Higher Oil Prices, Declining Manufacturing Construction Spending, and Tariffs Will Result in a Net Boost to Measured Capex Growth of Just Over 4pp i"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: We Expect Strong Equipment and IPP Investment Growth to More Than Offset Declining Structures Investment QoQ Annualized Real Nonresidential Fixed Investment Growth"
  },
  {
    "figure_id": "F049",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "EXHIBIT 1: Humanoid robots work in warehouses: material handling and sorting Industrial robot arm operating in a factory setting with yellow structural components (no visible text or symbols) Agility Robotics"
  },
  {
    "figure_id": "F050",
    "report_id": "R006",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Illustration of logistic process ```mermaid graph TD"
  },
  {
    "figure_id": "F051",
    "report_id": "R006",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Workflow in warehouses ```mermaid graph TD"
  },
  {
    "figure_id": "F052",
    "report_id": "R006",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Warehouses with different automation levels Overhead view of a large warehouse with workers sorting packages on pallets and shipping containers (no visible text or signage) Low automation level"
  },
  {
    "figure_id": "F053",
    "report_id": "R006",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Global warehouse automation solution market size and penetration rate"
  },
  {
    "figure_id": "F054",
    "report_id": "R006",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Warehouse automation market breakdown by solutions in 2024 Global warehouse automation market in 2024 (total market size USD65bn)"
  },
  {
    "figure_id": "F055",
    "report_id": "R006",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Barriers to adopting and implementing warehouse automation What do you consider to be the biggest barriers to adopting and implementing warehouse AS/RS system in your organization?"
  },
  {
    "figure_id": "F056",
    "report_id": "R006",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: US warehousing & storage labor demand has grown over the past decade"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: The U.S. warehousing and storage workforce is shifting toward fulfillment-driven roles"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: The U.S.: Rising wages have increased labor costs in warehouses"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: China logistics and warehouse employees China logistics & warehouse employees breakdown in 2023"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: China logistics and warehouse employees' annual wages Average annual wage of China logistics & warehouse employees (urban non-private units only) in 2024"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Payback analysis of humanoid robots in the U.S. warehouses EXHIBIT 16: The U.S.: Price declines in humanoid robots will shorten the payback period United States: Payback period of humanoid robots in warehouses (Assume 75"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: China: Price declines in humanoid robots will shorten the payback period China: Payback period of humanoid robots in warehouses (Assume 75% human worker efficiency)"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: On-the-ground facility layouts tells Coupang's urban logistics sites favoring flexible staging and manual handling over heavy mechanization. \\- Automation - Aided Automation - Fully Manual"
  },
  {
    "figure_id": "F064",
    "report_id": "R006",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: As last-mile delivery represents the largest cost component in the value chain, we see potential margin upside for the broader Korean e-commerce industry as automation progresses, particularly if it extends into last-mil"
  },
  {
    "figure_id": "F065",
    "report_id": "R006",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Fulfilment expenses have represented c. 7% of JD's revenue in recent years"
  },
  {
    "figure_id": "F066",
    "report_id": "R006",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: 643k of JD's 777k employees at the end of 2025 were warehouse and delivery workers 2025: JD employee count by nature"
  },
  {
    "figure_id": "F067",
    "report_id": "R007",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Huawei's tau scaling roadmap τ-Scaling Roadmap: Sustainable PPDC Evolution"
  },
  {
    "figure_id": "F068",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "EXHIBIT 1: Tokenized RWA - Market Cap (\\$Bn)"
  },
  {
    "figure_id": "F069",
    "report_id": "R008",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Tokenized RWA market cap split by asset class Tokenized RWA - Asset Class Split (%)"
  },
  {
    "figure_id": "F070",
    "report_id": "R008",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Commodities and Indices dominate HIP-3 trading volumes HIP-3 Trading Volumes - By Assets (\\$Bn)"
  },
  {
    "figure_id": "F071",
    "report_id": "R008",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: HIP-3 represented $35\\%$ of hyperliquid perp volumes in April'26 HIP-3 Volume Market Share of Hyperliquid Perpetuals (%) - April'26"
  },
  {
    "figure_id": "F072",
    "report_id": "R008",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Tokenized RWA split by blockchain network Tokenized RWA - Blockchain network split (%)"
  },
  {
    "figure_id": "F073",
    "report_id": "R008",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Top RWA tokenization platform EXHIBIT 7: Tokenized real world asset holders RWA Asset Holders (in '000)"
  },
  {
    "figure_id": "F074",
    "report_id": "R008",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: FIGR - Consumer loan volumes Consumer loan volume ($Bn)"
  },
  {
    "figure_id": "F075",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Tokenized Equities - Monthly Transfer Volumes Tokenized Equity - Transfer Volumes ($Bn)"
  },
  {
    "figure_id": "F076",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Weekly DV01 of gross issuance: past and BofA estimates for remainder of 2Q26 DV01 of gross EGB issuance expected to drop in this second half of Q2"
  },
  {
    "figure_id": "F077",
    "report_id": "R010",
    "label": "Exhibit 7",
    "context": "Exhibit 7: 5y BGB syndications allocation results by investor type, % Increased allocation to banks"
  },
  {
    "figure_id": "F078",
    "report_id": "R010",
    "label": "Exhibit 8",
    "context": "Exhibit 8: 10y BGB syndications allocation by geography of investor, % Decreased allocation to non-European investors"
  },
  {
    "figure_id": "F079",
    "report_id": "R010",
    "label": "Exhibit 9",
    "context": "Exhibit 9: IRISH Oct43 Green syndications allocation results by investor type, % Increased allocations to official institutions"
  },
  {
    "figure_id": "F080",
    "report_id": "R010",
    "label": "Exhibit 10",
    "context": "Exhibit 10: IRISH Oct43 Green syndications allocation results by geography of investor, % Increased allocations to non-European investors"
  },
  {
    "figure_id": "F081",
    "report_id": "R010",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Current outstanding volumes in futures positioning, a-accounts ('000s)\\* Neg. values for outstanding shorts equals the actual total values of outstanding shorts"
  },
  {
    "figure_id": "F082",
    "report_id": "R010",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Futures positioning in DU, open interest\\*"
  },
  {
    "figure_id": "F083",
    "report_id": "R010",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Weekly change in outstanding volumes, a-accounts\\* Neg. values for shorts indicate an increased short positioning"
  },
  {
    "figure_id": "F084",
    "report_id": "R010",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Futures positioning in OE, open interest\\* OE contracts represent GER gov bond with remaining maturity of 4.5-5.5y"
  },
  {
    "figure_id": "F085",
    "report_id": "R010",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Futures positioning in RX, open interest\\* RX contracts represent GER gov bond with remaining maturity of 8.5-10.5y"
  },
  {
    "figure_id": "F086",
    "report_id": "R010",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Futures positioning in BTS, open interest\\* BTS contracts represent ITA gov bond with remaining maturity of 2.0-3.25y"
  },
  {
    "figure_id": "F087",
    "report_id": "R010",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Futures positioning in UB, open interest\\* UB contracts represent GER gov bond with remaining maturity of 24-35y"
  },
  {
    "figure_id": "F088",
    "report_id": "R010",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Futures positioning in IK, open interest\\* IK contracts represent ITA gov bond with remaining maturity of 8.5-11.0y"
  },
  {
    "figure_id": "F089",
    "report_id": "R010",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Futures positioning in OAT, open interest\\* OAT contracts represent French gov bond with remaining maturity of 8.5-10.5y"
  },
  {
    "figure_id": "F090",
    "report_id": "R010",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Spread between special and general collateral repo rate, 3m moving average in bps More negative values indicate larger short positioning, and values are 3m moving averages"
  },
  {
    "figure_id": "F091",
    "report_id": "R010",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Weekly flows into single country and Europe ex. UK mandated funds, % of total asset (4w cumulative) Values represent 4w cumulative flows, as % of assets under management"
  },
  {
    "figure_id": "F092",
    "report_id": "R010",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Cumulative inflows into Europe ex UK mandated funds + single country mandated funds by type of fund, % YTD Funds with institutional clients have seen more inflows in 2025"
  },
  {
    "figure_id": "F093",
    "report_id": "R010",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Cumulative inflows into Europe ex UK mandated funds + single country mandated funds by type of fund, % YTD Fund mandates Short term: 0-4y. Medium term: 4-6y. Long term: +6y"
  },
  {
    "figure_id": "F094",
    "report_id": "R010",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Breakdown of govt bond holdings of Dutch PFs (bn €) and holdings as a share of outstanding bonds GE, FR & NL central govt bonds dominate govt bond holdings of Dutch PFs"
  },
  {
    "figure_id": "F095",
    "report_id": "R010",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Bank holdings of EA general gov bonds as % of total bank assets, by geographical location of banks. Last data point = Mar-26 Holdings have been on the rise in 2025"
  },
  {
    "figure_id": "F096",
    "report_id": "R010",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Bank holdings of non-domestic EA general gov bonds as % of total bank EGB holdings, by geographical location of banks. Last data point = Mar-26 Increasing share of non-domestic EGB holdings"
  },
  {
    "figure_id": "F097",
    "report_id": "R010",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Net transactions in EA general gov bonds by EA banks, split by domicile of banking system, EUR bn. Last data point = Mar-26 Values split into domestic, non-domestic, & total as well as 1m, 3m & YTD"
  },
  {
    "figure_id": "F098",
    "report_id": "R010",
    "label": "Exhibit 30",
    "context": "Exhibit 31: Duration exposure and view 2012-26ytd: Core Europe (May-26)"
  },
  {
    "figure_id": "F099",
    "report_id": "R010",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Duration exposure and view 2012-26ytd: Core Europe (May-26) In duration, both sentiment and exposure turned bullish"
  },
  {
    "figure_id": "F100",
    "report_id": "R010",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Duration exposure and view 2014-26ytd: Peripheral Europe (May-26) In peripheral Europe, sentiment turned neutral while positioning remained largely unchanged from last month's bullish levels"
  },
  {
    "figure_id": "F101",
    "report_id": "R010",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Fund managers' duration exposure 2004-YTD, FXRS Survey index (latest May-26) Positive values indicate overweight positioning"
  },
  {
    "figure_id": "F102",
    "report_id": "R010",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Fund managers' duration exposure latest 12m, FXRS Survey index (latest Apr-26) Positive values indicate overweight positioning"
  },
  {
    "figure_id": "F103",
    "report_id": "R010",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Weekly net investment abroad, medium and long term bonds, bn EUR. Values represent all non-Japanese bond purchases"
  },
  {
    "figure_id": "F104",
    "report_id": "R010",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Difference between fund managers' duration sentiment vs exposure, latest reading from FXRS Survey index (latest Apr-26) Positive values indicate more bullish sentiment than positioning"
  },
  {
    "figure_id": "F105",
    "report_id": "R010",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Cum. net flows from JP investors in long term government debt since Jan-2014, bn EUR. Last monthly data point = January JP investors have been net sellers of core since Jan-2014"
  },
  {
    "figure_id": "F106",
    "report_id": "R010",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Monthly net flows into EA vs US debt securities, bn USD. Last monthly data point = January Values are updated on a monthly basis"
  },
  {
    "figure_id": "F107",
    "report_id": "R010",
    "label": "Exhibit 40",
    "context": "Exhibit 40: BoP: Financial account, portfolio liabilities, long term gov debt from Euro Area, cum. EUR bn. Latest monthly data = February Foreign purchases of Euro Area government bonds"
  },
  {
    "figure_id": "F108",
    "report_id": "R010",
    "label": "Exhibit 41",
    "context": "Exhibit 41: BoP: Financial account, portfolio liabilities, long term gov debt to Euro Area, cumulative EUR bn. Latest monthly data = February Investment type recorded as being purchased by foreign investors: Germany Public debt. Fra"
  },
  {
    "figure_id": "F109",
    "report_id": "R010",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Leveraged investors' net sold in March Net purchases of German government securities by leveraged investors, €mn"
  },
  {
    "figure_id": "F110",
    "report_id": "R010",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Bank net purchases YTD are slightly less vs 2025 YTD Net purchases of German government securities by banks, €mn"
  },
  {
    "figure_id": "F111",
    "report_id": "R010",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Central bank net purchases surged in Mar 26 Net purchases of German government securities by central banks, €mn"
  },
  {
    "figure_id": "F112",
    "report_id": "R010",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Leveraged investors net sold across curve ex. 10y & Bubills Net purchases by leveraged investors by tenor in Mar26, €mn"
  },
  {
    "figure_id": "F113",
    "report_id": "R010",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Bank net purchases most in Bubills in March Net purchases by banks by tenor in Mar26, €mn"
  },
  {
    "figure_id": "F114",
    "report_id": "R010",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Central bank net purchases across curve ex. 15-20y Net purchases by central banks by tenor in Mar26, €mn"
  },
  {
    "figure_id": "F115",
    "report_id": "R011",
    "label": "exhibit 1",
    "context": "Multiple bottlenecks are emerging in the multi-year AI infrastructure buildout – memory, optics, leading-edge logic wafers, advanced substrates, etc. – but among the greatest constraints to scaling is arguably power. # Higher compute density is translating to "
  },
  {
    "figure_id": "F116",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Cumulative data center power demand globally is expected to increase from \\~100GW today to almost 300GW by CY30 Data center power demand by region (GW)"
  },
  {
    "figure_id": "F117",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Layering on top of conventional server power demand, AI is catalyzing electricity consumption to new heights Data center electricity consumption (TWh)"
  },
  {
    "figure_id": "F118",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We estimate AI accelerator demand implies that GWs installed per year for compute could 4x from 15GW in CY25 to 60GW in CY30, a cumulative 233GWs deployed during the period Implied GWs deployed across major accelerator p"
  },
  {
    "figure_id": "F119",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Today, power from the grid undergoes multiple conversions from high voltage AC to medium voltage AC and then multiple low voltage DCs before reaching the accelerator Traditional 48V/54V power distribution architecture"
  },
  {
    "figure_id": "F120",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 9: 800V DC architecture minimizes energy losses and supports higher reliability by making fewer AC to DC and DC to DC conversions along with reducing system component complexity Existing power flow architecture vs. next gen"
  },
  {
    "figure_id": "F121",
    "report_id": "R011",
    "label": "exhibit 12",
    "context": "Exhibit 12: As existing facilities migrate to high voltage distribution, we expect there to be several intermediary stages before “true” 800 VDC architecture is architecture including using a power side car"
  },
  {
    "figure_id": "F122",
    "report_id": "R011",
    "label": "exhibit 12",
    "context": "Exhibit 12: As existing facilities migrate to high voltage distribution, we expect there to be several intermediary stages before “true” 800 VDC architecture is architecture including using a power side car Evolution of power delive"
  },
  {
    "figure_id": "F123",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Power needs to be managed at multiple timescales when dealing with AI workloads including grid level fluctuation requirements and GPU load demand requirements Power envelope over a full compute cycle"
  },
  {
    "figure_id": "F124",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14: DC microgrids optimize system efficiency through use of new equipment like SSTs, SSCBs, and more, representing an end state for the shift to 800 VDC architecture Data center architecture evolution ```mermaid graph TD"
  },
  {
    "figure_id": "F125",
    "report_id": "R011",
    "label": "Exhibit 15",
    "context": "Exhibit 15: We expect the AI TAM for analog semis to grow 28% 5-year CAGR through CY30 to \\$27bn from \\$7.9bn in CY25. Average content per rack could grow from mid-\\$20K to over \\$60K by CY30 Analog semi data center and strategic po"
  },
  {
    "figure_id": "F126",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "Exhibit 17: While analog ICs will continue to be the largest market, we believe SiC and GaN will enjoy the most share gains AI analog semi TAM by device type"
  },
  {
    "figure_id": "F127",
    "report_id": "R011",
    "label": "Exhibit 18",
    "context": "Exhibit 18: TXN enjoys dominant share in the AI TAM but we flag that discrete suppliers ON and Infineon gain significant share Analog semi vendor AI market share"
  },
  {
    "figure_id": "F128",
    "report_id": "R011",
    "label": "Exhibit 20",
    "context": "Exhibit 20: The data center analog TAM at \\$7.6bn CY25 growing to \\$25bn by CY30, a \\~28% CAGR Analog semi AI data center TAM"
  },
  {
    "figure_id": "F129",
    "report_id": "R011",
    "label": "exhibit 22",
    "context": "Exhibit 22: PSUs are evolving from single-phase 3.3kW architectures towards three-phase 30kW devices disaggregated into sidecars Infineon PSU roadmap"
  },
  {
    "figure_id": "F130",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 23: PSU total content could grow from \\~\\$1.2bn today to \\$2.6bn by CY30 Power Supply Unit analog semi TAM estimates (\\$ mn; lhs) and \\% of total content (%; rhs)"
  },
  {
    "figure_id": "F131",
    "report_id": "R011",
    "label": "Exhibit 24",
    "context": "BofA GLOBAL RESEARCH # Intermediate Bus Conversion (IBC) An intermediate bus converter (IBC) is the conversion stage between rack-level distribution and the final processor VRM. It creates an intermediate rail the compute tray can use before the sub-1V GPU cor"
  },
  {
    "figure_id": "F132",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 25: IBC's role only increases in prominence as we move to next generation power distribution flows, still retaining the important function as high to low conversion (see placed in IT racks below) even as other components mov"
  },
  {
    "figure_id": "F133",
    "report_id": "R011",
    "label": "Exhibit 26",
    "context": "Exhibit 26: While legacy 48V IBC components disappear, these are replaced by higher value HV/MV/LV IBCs that carry more wide-bandgap semi content such as SiC and GaN 48V Intermediate Bus Converter block diagram ```mermaid graph TD"
  },
  {
    "figure_id": "F134",
    "report_id": "R011",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Suppliers (like Infineon below) often offer solutions that support alternative IBC flows such as 3-stage approaches (800V to 50V to 12V/6V) or 2-stage (800V to 12V). Each architecture comes with distinct tradeoffs and be"
  },
  {
    "figure_id": "F135",
    "report_id": "R011",
    "label": "Exhibit 28",
    "context": "Exhibit 28: ON's vGaN transistors are fabricated on bulk GaN substrates, enabling current to flow vertically through the crystal lattice rather than laterally. Using the same substrate for fabrication (Rather than GaN-on-Si) can lea"
  },
  {
    "figure_id": "F136",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Multi-phase and single phase voltage regulator modules are among the most valuable sockets on the server board (bottom right box), helping to power GPUs, CPUs, and more Block diagram of power delivery to the sever board"
  },
  {
    "figure_id": "F137",
    "report_id": "R011",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Power delivery to the processor (GPU/XPU) is among the most valuable components (mid-20% of content TAM) and grows from \\$2bn in CY25 to over \\$6.6bn by CY30 TAM for GPU related components on the server board"
  },
  {
    "figure_id": "F138",
    "report_id": "R011",
    "label": "Exhibit 31",
    "context": "Exhibit 31: VRMs increasingly have to channel more current through a smaller physical footprint as power density rises with the roadmap tripling amps per millimeter squared in several years via smaller packages, multiphase integrati"
  },
  {
    "figure_id": "F139",
    "report_id": "R011",
    "label": "Exhibit 32",
    "context": "Exhibit 32: The board opportunity is expanding as content tied to CPU and HBM continues to rise in conjunction with rising processor power as well as with new agentic workloads CPU complex and attach content along with HBM/memory at"
  },
  {
    "figure_id": "F140",
    "report_id": "R011",
    "label": "Exhibit 34",
    "context": "Exhibit 34: PICs, EICs, and MCUs are examples of analog products that vendors like STMicro can sell into both an optical transceiver (pluggable) or a co-packaged optics (CPO) solution Analog content in optics Pluggable Courtesy In"
  },
  {
    "figure_id": "F141",
    "report_id": "R011",
    "label": "Exhibit 35",
    "context": "Exhibit 35: The BBU shelf provides backup power if an AC power outage occurs for a defined period of time, giving time for the rack to be moved between power sources without disrupting the IT gear. OCP's architecture below shows a s"
  },
  {
    "figure_id": "F142",
    "report_id": "R011",
    "label": "Exhibit 36",
    "context": "We estimate the strategic power infrastructure analog semi opportunity grows from \\$300mn in CY25 to \\$1.8bn in CY30, a \\~49% CAGR, with growth near +90%/140% CY26/27 as Solid-State Transformers (SST) and Solid-State Circuit Breakers (SSCB) gain traction. Our "
  },
  {
    "figure_id": "F143",
    "report_id": "R011",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Previous functions like the HVDC sidecar rack for 500-600kW+ racks could be disaggregated and content can move up the chain as new technologies like solid-state transformers, enhanced ESS, and solid-state circuit breaker"
  },
  {
    "figure_id": "F144",
    "report_id": "R011",
    "label": "Exhibit 39",
    "context": "Exhibit 39: ESS battery shipments grow +31% CAGR CY25 to CY30 Global ESS battery shipment forecasts 2025/2026/2028 (Infineon) Global ESS battery shipment forecast"
  },
  {
    "figure_id": "F145",
    "report_id": "R011",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Most of the ESS content is concentrated in power, but control (e.g. MCUs), and analog (gate drivers sensors) are valuable too Devices used in ESS power - IGBT discretes - SiC MOSFETs - Low & medium power modules"
  },
  {
    "figure_id": "F146",
    "report_id": "R011",
    "label": "Exhibit 41",
    "context": "Exhibit 41: When compared to a conventional transformer, SSTs are superior as it replaces much of the passive transformer function typically done using copper wirings and magnetic cores to something that is more active, with high fr"
  },
  {
    "figure_id": "F147",
    "report_id": "R011",
    "label": "Exhibit 44",
    "context": "Exhibit 44: SSCB content is higher vs. traditional circuit breakers due to the inclusion of high voltage power switches, gate drivers, sensing, MCUs and more vs. the traditional mechanical design SSCB block diagram ```mermaid grap"
  },
  {
    "figure_id": "F148",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary GFA sold last week was $-4\\%$ wow and $-5\\%$ yoy in c.75 cities"
  },
  {
    "figure_id": "F149",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Primary GFA sold YTD on average was -14% yoy in c.75 cities, and -14%/-48% vs. 2024/2023 level"
  },
  {
    "figure_id": "F150",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Secondary GFA sold last week was +1% wow and +11% yoy in c.20 cities Average weekly volume of secondary property sales"
  },
  {
    "figure_id": "F151",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Secondary GFA sold YTD was -1% yoy in c.20 cities, while +23%/+6% vs. 2024/ secondary volume sold vs. 2022-25"
  },
  {
    "figure_id": "F152",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Average CSI was -1.6pp wow and +2.3pp yoy Weekly Centraline Salesman Index (CSI) tracker in 5 cities"
  },
  {
    "figure_id": "F153",
    "report_id": "R012",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Average CAI was -0.4pp wow and -4.1pp yoy Weekly Centraline Seller Asking Index (CAI) tracker in 6 cities"
  },
  {
    "figure_id": "F154",
    "report_id": "R012",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Inventory balance was -0.2% wow, -3.7% from end-25 levels c.20 cities' total inventory breakdown by city tier (Indexed to Jan 2013)"
  },
  {
    "figure_id": "F155",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Inventory month was -0.4% wow, representing +0.2% from end-25 levels c.20 cities' inventory months (12mth rolling) breakdown by city tier"
  },
  {
    "figure_id": "F156",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 9: MTD GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model"
  },
  {
    "figure_id": "F157",
    "report_id": "R012",
    "label": "Exhibit 10",
    "context": "Exhibit 10: ...suggesting completions at a high-teens % yoy decline for MTD May-26 % yoy change of GSPC - based on GS float glass S-D model"
  },
  {
    "figure_id": "F158",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend"
  },
  {
    "figure_id": "F159",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F160",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F161",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F162",
    "report_id": "R014",
    "label": "Figure 2",
    "context": "Figure 2: Gen. Retail may work for a short period but EPS compression is the risk"
  },
  {
    "figure_id": "F163",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: SA Domestic have de-rated vs EM broadening appeal for engagement to these names"
  },
  {
    "figure_id": "F164",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 1: ToT will be accommodated by an uplift from commodities which in turn turns positive for ZAR"
  },
  {
    "figure_id": "F165",
    "report_id": "R014",
    "label": "Figure 3",
    "context": "Figure 3: This is in contrast to banks which are large, liquid and offer robust earnings"
  },
  {
    "figure_id": "F166",
    "report_id": "R014",
    "label": "Figure 5",
    "context": "Figure 5: Discount to 10yr fwd. PE for JSE sectors"
  },
  {
    "figure_id": "F167",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: MSCI South Africa remains one of EM's highest beta markets"
  },
  {
    "figure_id": "F168",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "EXHIBIT 2: In the US, olefin prices have rallied since the onset of the Iran conflict and show no signs of easing. Olefin US-Gulf prices index - Rebased to 100"
  },
  {
    "figure_id": "F169",
    "report_id": "R015",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: In the US, olefin prices have rallied since the onset of the Iran conflict and show no signs of easing. Olefin US-Gulf prices index - Rebased to 100"
  },
  {
    "figure_id": "F170",
    "report_id": "R015",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Chinese olefin prices have surged since the onset of the Iran conflict and began stabilizing in April."
  },
  {
    "figure_id": "F171",
    "report_id": "R015",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: LYB also have made the case for lasting changes to the petrochemical industry in their 1Q26 presentation # Middle East war creating structural shifts in economics"
  },
  {
    "figure_id": "F172",
    "report_id": "R015",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: LYB also have made the case for lasting changes to the petrochemical industry in their 1Q26 presentation # Middle East war creating structural shifts in economics LYB is well-positioned to benefit from strengthened cost"
  },
  {
    "figure_id": "F173",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Key commodity chemicals are typically used as intermediates for other chemical processes: (1: Ethylene) World 2023 Ethylene Demand"
  },
  {
    "figure_id": "F174",
    "report_id": "R015",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Key commodity chemicals are typically used as intermediates for other chemical processes: (2: Propylene) World 2023 Propylene Demand"
  },
  {
    "figure_id": "F175",
    "report_id": "R015",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Polyethylene uses vary by grade (part 1: high density) Global Uses of High Density Polyethylene"
  },
  {
    "figure_id": "F176",
    "report_id": "R015",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Polyethylene uses vary by grade (part 2: low density) Global Uses of Low Density Polyethylene"
  },
  {
    "figure_id": "F177",
    "report_id": "R015",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Polypropylene end uses are varied Polypropylene End Use by Application"
  },
  {
    "figure_id": "F178",
    "report_id": "R015",
    "label": "Exhibit 12",
    "context": "EXHIBIT 12: Polypropylene production grows steadily over time ..."
  },
  {
    "figure_id": "F179",
    "report_id": "R015",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: ... with no strong correlation with GDP growth rates."
  },
  {
    "figure_id": "F180",
    "report_id": "R015",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: The same applies for polyethylene (1/2) EXHIBIT 15: The same applies for polyethylene (2/2)"
  },
  {
    "figure_id": "F181",
    "report_id": "R015",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: The same applies for polyethylene (1/2) EXHIBIT 15: The same applies for polyethylene (2/2)"
  },
  {
    "figure_id": "F182",
    "report_id": "R015",
    "label": "Exhibit 16",
    "context": "EXHIBIT 16: Despite price volatility, polypropylene consumption continue to grow steadily over time..."
  },
  {
    "figure_id": "F183",
    "report_id": "R015",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: ... so there's no strong correlation between consumption and price"
  },
  {
    "figure_id": "F184",
    "report_id": "R015",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: The same applies to polyethylene (1/2)"
  },
  {
    "figure_id": "F185",
    "report_id": "R015",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: The same applies to polyethylene (2/2)"
  },
  {
    "figure_id": "F186",
    "report_id": "R015",
    "label": "Exhibit 20",
    "context": "EXHIBIT 20: Major Asian economies have dealt with little inflation in the last 20 years Inflation in major Asian economies vs Asian polyolefins consumption growth"
  },
  {
    "figure_id": "F187",
    "report_id": "R015",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Inflation therefore has little impact on polyolefin consumption growth rates Inflation in major Asian economies vs Asian polyolefins consumption growth correlation"
  },
  {
    "figure_id": "F188",
    "report_id": "R015",
    "label": "Exhibit 22",
    "context": "EXHIBIT 22: Qatar LNG exports mainly go to Asia Qatar LNG exports by region"
  },
  {
    "figure_id": "F189",
    "report_id": "R015",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: The US represents 65% of European LNG imports European LNG imports by region"
  },
  {
    "figure_id": "F190",
    "report_id": "R015",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Most of the sites that declared force majeure are located in the Middle East and in Asia Sites that declared force majeure by country"
  },
  {
    "figure_id": "F191",
    "report_id": "R015",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Operating rates in Asia are understood to be falling"
  },
  {
    "figure_id": "F192",
    "report_id": "R015",
    "label": "Exhibit 24",
    "context": "EXHIBIT 29: Asia is the leading global producer of Polypropylene... EXHIBIT 30: ... and polyethylene. EXHIBIT 31: We see slightly more than 8mt of PE capacity coming online in 2026, stemming from multiple regions"
  },
  {
    "figure_id": "F193",
    "report_id": "R015",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: Asia is the leading global producer of Polypropylene... EXHIBIT 30: ... and polyethylene. EXHIBIT 31: We see slightly more than 8mt of PE capacity coming online in 2026, stemming from multiple regions"
  },
  {
    "figure_id": "F194",
    "report_id": "R015",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: ... and polyethylene. EXHIBIT 31: We see slightly more than 8mt of PE capacity coming online in 2026, stemming from multiple regions"
  },
  {
    "figure_id": "F195",
    "report_id": "R015",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Slightly less than 6mt of polypropylene capacity is expected to come online in 2026 mainly from China, wider Asia and the Middle East"
  },
  {
    "figure_id": "F196",
    "report_id": "R015",
    "label": "Exhibit 33",
    "context": "EXHIBIT 33: Our polyethylene model, back-tested, provides useful directional context for price forecasting (1/2)"
  },
  {
    "figure_id": "F197",
    "report_id": "R015",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: Our polyethylene model, back-tested, provides useful directional context for price forecasting (2/2)"
  },
  {
    "figure_id": "F198",
    "report_id": "R015",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: Our polypropylene model, back-tested, provides useful directional context for price forecasting (1/2)"
  },
  {
    "figure_id": "F199",
    "report_id": "R015",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: Our polypropylene model, back-tested, provides useful directional context for price forecasting (2/2)"
  },
  {
    "figure_id": "F200",
    "report_id": "R015",
    "label": "Exhibit 37",
    "context": "EXHIBIT 37: We expect the more muted demand growth rates of the early 2020s to continue"
  },
  {
    "figure_id": "F201",
    "report_id": "R015",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: We now see less PE capacity coming online in 2026 as a result of capacity delays in the Middle East and in Asia... (1/2)"
  },
  {
    "figure_id": "F202",
    "report_id": "R015",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: We now see less PE capacity coming online in 2026 as a result of capacity delays in the Middle East and in Asia... (2/2)"
  },
  {
    "figure_id": "F203",
    "report_id": "R015",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 40: ... which we also see happening for Polypropylene (1/2)"
  },
  {
    "figure_id": "F204",
    "report_id": "R015",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 41: ... which we also see happening for Polypropylene (2/2)"
  },
  {
    "figure_id": "F205",
    "report_id": "R015",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 42: We increase our long-term operating rate assumptions for polyethylene"
  },
  {
    "figure_id": "F206",
    "report_id": "R015",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: We increase our long-term operating rate assumptions for polypropylene"
  },
  {
    "figure_id": "F207",
    "report_id": "R015",
    "label": "Exhibit 44",
    "context": "EXHIBIT 44: Our Global O&G colleagues expect the oil price to settle at \\$70/bbl"
  },
  {
    "figure_id": "F208",
    "report_id": "R015",
    "label": "Exhibit 45",
    "context": "EXHIBIT 45: We expect GDP to slowly trend back to historical average growth rates"
  },
  {
    "figure_id": "F209",
    "report_id": "R015",
    "label": "Exhibit 46",
    "context": "EXHIBIT 46: We increase our long-term PE prices from 5-10% PE Avg. prices for each region are price weighted averages of HDPE, LLDPE and LDPE benchmarks EXHIBIT 47: We increase our long-term PP prices from 7-15%"
  },
  {
    "figure_id": "F210",
    "report_id": "R015",
    "label": "EXHIBIT 46",
    "context": "EXHIBIT 46: We increase our long-term PE prices from 5-10% PE Avg. prices for each region are price weighted averages of HDPE, LLDPE and LDPE benchmarks EXHIBIT 47: We increase our long-term PP prices from 7-15% # BULL AND BEAR"
  },
  {
    "figure_id": "F211",
    "report_id": "R015",
    "label": "EXHIBIT 48",
    "context": "EXHIBIT 48: Our polyolefin price scenarios"
  },
  {
    "figure_id": "F212",
    "report_id": "R015",
    "label": "EXHIBIT 49",
    "context": "EXHIBIT 49: In a bull case scenario, we see polyolefin prices remain around current levels (1/2)"
  },
  {
    "figure_id": "F213",
    "report_id": "R015",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 50: In a bull case scenario, we see polyolefin prices remain around current levels (2/2)"
  },
  {
    "figure_id": "F214",
    "report_id": "R015",
    "label": "Exhibit 53",
    "context": "EXHIBIT 53: After the Middle-East conflict, the oil spread with Henry Hub spiked making gas-based polyolefin feedstocks more economic than oil-based ones Brent to Henry Hub spread - 2000/2026"
  },
  {
    "figure_id": "F215",
    "report_id": "R015",
    "label": "EXHIBIT 54",
    "context": "EXHIBIT 54: The US Ethane advantage is high when oil prices are higher... Global Ethylene Variable Cost of Production by Feedstock on March 12 2025 with Brent Spot @ \\$70.95 (\\$/mt)"
  },
  {
    "figure_id": "F216",
    "report_id": "R015",
    "label": "EXHIBIT 55",
    "context": "EXHIBIT 55: ... but that advantage declines when oil prices are lower Global Ethylene Variable Cost of Production by Feedstock on April 9 2025 with Brent Spot @ \\$65.48 (\\$/mt)"
  },
  {
    "figure_id": "F217",
    "report_id": "R015",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 56: North America and the Middle East primarily rely on Ethane while Europe and China mainly produce petrochemicals with naphta Share of petrochemical feedstocks by region"
  },
  {
    "figure_id": "F218",
    "report_id": "R015",
    "label": "EXHIBIT 57",
    "context": "EXHIBIT 58: On our house natural gas forecasts, the ethane advantage would disappear. But the on the market's... Henry Hub price forecast (\\$/mmbtu)"
  },
  {
    "figure_id": "F219",
    "report_id": "R015",
    "label": "EXHIBIT 57",
    "context": "EXHIBIT 58: On our house natural gas forecasts, the ethane advantage would disappear. But the on the market's... Henry Hub price forecast (\\$/mmbtu)"
  },
  {
    "figure_id": "F220",
    "report_id": "R015",
    "label": "EXHIBIT 59",
    "context": "EXHIBIT 59: We see being integrated, like BASF are, as an advantage in a world of higher petchem prices for longer # We operate long and multiple-step value chains and sell products at every step in the value chain EO value chain as"
  },
  {
    "figure_id": "F221",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Richard Nguyen # Specialist Sales Kiran Shah, CFA"
  },
  {
    "figure_id": "F222",
    "report_id": "R016",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Engineering Services' companies share price reaction on the day of calendar 1Q26 results publication"
  },
  {
    "figure_id": "F223",
    "report_id": "R016",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Arcadis's peers end-March quarter organic sales growth (yoy %)"
  },
  {
    "figure_id": "F224",
    "report_id": "R016",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: AtkinsRéalis\\* and Sweco: sharpest decelerations in organic growth (yoy %)"
  },
  {
    "figure_id": "F225",
    "report_id": "R016",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: AtkinsRéalis\\* and Jacobs: strongest growth rates in the quarter (yoy %)"
  },
  {
    "figure_id": "F226",
    "report_id": "R016",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Arcadis's peers end-March backlog growth (yoy %)"
  },
  {
    "figure_id": "F227",
    "report_id": "R016",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Arcadis's peers end-March quarter order intake growth (yoy %)"
  },
  {
    "figure_id": "F228",
    "report_id": "R016",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Moody's projects \\$3 trillion in spending over the next five years for data center expansion"
  },
  {
    "figure_id": "F229",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Earnings will primarily be impacted by regulatory fines but also the loss of revenues from remediating non-compliant mainland accounts. Exhibit 3: The cumulative impact represents -27%/-38% of FUTU's and TIGR's 2025 net"
  },
  {
    "figure_id": "F230",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "Exhibit 5: FUTU's competitive advantages include a significantly lower fee structure than traditional banks and brokers (3bps vs. \\~25bps/\\~7bps) and a willingness to invest in acquiring new clients Exhibit 6: FUTU has enjoyed rapi"
  },
  {
    "figure_id": "F231",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Moreover, FUTU's market share has been continuously increasing in HK, from $15\\%$ in 2021 to $30\\%$ in 3Q25, and we expect it to reach $47\\%$ by 2027."
  },
  {
    "figure_id": "F232",
    "report_id": "R018",
    "label": "Exhibit 8",
    "context": "# 3. Higher Client Acquisition Cost (CACs) from International Expansion Both FUTU and TIGR have announced plans to expand into international markets. FUTU aims to enter South Korea as soon as possible, and while it has been cultivating the Japanese market for "
  },
  {
    "figure_id": "F233",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ...and $8\\%$ for TIGR"
  },
  {
    "figure_id": "F234",
    "report_id": "R018",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We have lowered AUM per client by -6% for FUTU..."
  },
  {
    "figure_id": "F235",
    "report_id": "R018",
    "label": "Exhibit 11",
    "context": "Exhibit 11: ...and by -3% for TIGR"
  },
  {
    "figure_id": "F236",
    "report_id": "R018",
    "label": "Exhibit 12",
    "context": "Neither FUTU nor TIGR have updated their new client growth guidance for 2026 (FUTU: 800k; TIGR: 150k). Even in a best case scenario that new client growth reaches guidance, higher corresponding CAC and lower AUM per new client will pressure revenues and profit"
  },
  {
    "figure_id": "F237",
    "report_id": "R018",
    "label": "Exhibit 14",
    "context": "Exhibit 14: FUTU valuation range"
  },
  {
    "figure_id": "F238",
    "report_id": "R018",
    "label": "Exhibit 15",
    "context": "Exhibit 15: FUTU 12M P/E vs. AUM growth"
  },
  {
    "figure_id": "F239",
    "report_id": "R018",
    "label": "Exhibit 16",
    "context": "Exhibit 16: TIGR valuation range"
  },
  {
    "figure_id": "F240",
    "report_id": "R018",
    "label": "Exhibit 17",
    "context": "Exhibit 17: FUTU 12M P/E vs. AUM growth"
  },
  {
    "figure_id": "F241",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Price of each round of DES VBP continue to increase Price range of each round of DES VBP (in Rmb)"
  },
  {
    "figure_id": "F242",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Submitted demand reached c.2.73mn units, implying a $14\\%$ CAGR vs. the 2022 renewal First year guaranteed volume (mn units)"
  },
  {
    "figure_id": "F243",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: MNC submitted volume increased to c.41% in the 2nd round renewal (vs. c.32% in the first round) Total first-year procurement demand of major brands in the 1st and 2nd round renewal (units)"
  },
  {
    "figure_id": "F244",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Accelerating progress in VBP since Oct 25; expecting additional announcements towards year end 2026"
  }
]