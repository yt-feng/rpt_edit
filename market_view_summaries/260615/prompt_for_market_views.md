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
    "title": "Bernstein：K-pop 的盈利重心已从卖专辑转向卖时间，演唱会才是真正的利润引擎",
    "digest": "[wechat_article.md]\n# Bernstein：K-pop 的盈利重心已从卖专辑转向卖时间，演唱会才是真正的利润引擎\n\n全球音乐产业的叙事正在经历一次静默但彻底的切换。过去二十年，K-pop 的增长故事几乎等于专辑销量的增长故事——实体销量、数字下载、流媒体播放量，构成了行业估值的核心锚点。但Bernstein最新发布的深度报告《Global Music: The Long View》提出了一个值得所有产业决策者认真审视的判断：这个模型已经过时了。\n\n报告的核心主张非常清晰——K-pop 已经从以“单位”驱动的业务，转向了以“时刻”驱动的经济。粉丝不再为拥有产品付费，而是为与偶像共度的时间付费。演唱会，正在取代专辑，成为整个行业利润池的自然重心。这不仅仅是疫情后线下消费的报复性反弹，而是一个结构性的、不可逆的商业模式迁移。\n\n这份Bernstein研报的洞察力不在于它发现了“演唱会赚钱”，而在于它揭示了这一转变背后的经济学逻辑：当资产价格膨胀，真正的稀缺资源不再是资本，而是时间。时间的价值在持续攀升，而实物商品的价值在相对下降。在这样的框架下，艺术家管理的本质，变成了如何最优地分配艺术家的时间，并最大化每一次互动的货币化效率。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 粉丝经济学正在从“拥有”转向“体验”，演唱会成为情感回报率最高的消费场景\n\n报告提出了一个在咨询行业常被称为“情感回报率”的概念。粉丝愿意为一场两到三小时的演唱会支付远高于一张专辑的价格，不是因为演唱会本身作为“产品”的价值更高，而是因为它带来的情感回报密度更大。\n\n在 K-pop 的语境中，一场演唱会结束后，价值并不会停止产生。它会通过社交媒体分享、粉丝二次创作、社群持续互动等方式，\n\n[... middle omitted ...]\n\n估值模型中的关键假设，以及分享我们对行业竞争格局的实时观察。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n音乐公司的新算盘：卖时间比卖专辑更赚\n\n**超级粉丝经济**\n\n**当演唱会成为核心变现引擎**\n\n最近看了一份某外资投行的研报，讲全球音乐产业正在经历一个关键转折——K-pop已经从卖专辑转向卖“时间”。\n\n核心逻辑很直白：\n\n**1/ 粉丝在买“和偶像在一起的时间”**\n\n过去二十年，K-pop商业模式从卖实体唱片，转向卖“现场时刻”。资产通胀让钱贬值，但时间越来越贵。粉丝愿意为2-3小时的演唱会支付高价，因为看完演出后还能通过剪辑、社群互动、二创内容，把情绪价值拉长到几个月。这种“情感回报/小时”的性价比，远高于任何实体产品。\n\n**2/ 每场演出都是变现节点**\n\n以某头部K-pop公司为例，80场以上全球巡演场场售罄。但演唱会本身不是终点——每场演出同时带动门票、VIP套餐、周边、会员订阅、流媒体点播、甚至Netflix特辑。一个IP可以同时出现在Spotify榜单、Netflix全球榜首和体育场舞台，把内容价值链拉满。\n\n**3/ 超级粉丝的终身价值正在打通**\n\n流媒体平台和现场演出方正在形成闭环：超级粉丝在线上高消费（高级会员、数字内容），通过工具直接转化为线下演唱会的高客单价观众。线上变现一\n\n[... middle omitted ...]\n\n06923400b1ac3.jpg)\n\nDavid Dai, CFA\n\n+852 2918 5704\n\ndavid.dai@bernsteinsg.com\n\n![](images/519ac0ca45564eb47b4b8631d7146897b1086295960e8ffe46f560dffe371431.jpg)\n\nChristophe Cherblanc\n\n+41 582 7\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R002",
    "title": "JEF：K型经济深化，市场低估了结构性分化对金融资产定价的影响",
    "digest": "[wechat_article.md]\n# JEF：K型经济深化，市场低估了结构性分化对金融资产定价的影响\n\n五月的金融数据公布后，市场情绪一度被社融总量超预期所提振。但这份JEF研报揭示了一个更值得关注的信号：表面改善的流动性，其质量远低于市场直觉判断。M1增速超预期并非企业资本开支意愿的回暖，而是预防性现金囤积；新增贷款中超过100%由票据贴现驱动，居民信贷仍在收缩区间。这些数据合在一起指向一个结论——中国经济正在加速K型分化，而这一分化对金融资产定价的含义，远比总量数字所显示的更为深远。\n\n这份报告的核心价值不在于它给出了哪些投资建议，而在于它提供了一个识别结构分化的分析框架。JEF团队从三个维度拆解了当前宏观数据的真实含义，并在此基础上提出了一个在金融板块内部的杠铃策略。以下是我们基于这份研报的解读与延伸思考。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 社融总量超预期的背后，是政府信用对私人信用的加速替代\n\n五月新增社融2.03万亿元，超出市场预期19%。但拆解结构后，这一数字的“含金量”需要重新审视。政府债券发行贡献了1.22万亿元，占当月新增社融的60%。企业债券融资同比改善14.6%，部分抵消了企业中长期贷款的疲弱。而影子银行继续收缩，表外融资净减少。\n\n这组数据的含义是清晰的：当前信用扩张的引擎已经从市场转向政府。这不是一个周期性的切换，而是一个结构性趋势的延续。2022年以来，政府债券在新增社融中的占比持续走高，从2021年的不到20%上升至当前接近40%的水平。这背后反映的是私人部门去杠杆与政府部门加杠杆的并行。\n\n对于投资者而言，这一趋势意味着两个层面的含义。第一，信用扩张的效率在下降——政府债的乘数效应通常低于企业贷款和居民贷款。第二，银行资产的组合结构正在发生根本性变化，对政府债的依赖度上升意味着净息差的长期压力，因为政府\n\n[... middle omitted ...]\n\n己的判断和疑问来交流，K型经济的投资机会，值得更深入的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月社融的钱去哪了？🧐\n\nK型复苏的三个信号\n\n5月社融数据超预期，但细看结构，钱并不是大家想的那样流向实体。某外资投行最新研报拆了三层逻辑，我觉得挺清醒的。\n\n1️⃣ 社融靠政府债撑场面\n5月新增社融2.03万亿，比预期高19%，但60%靠政府债拉动（1.2万亿）。企业债券融资同比改善14.6%，但企业中长期贷款却转弱了。说白了，实体借钱意愿还在犹豫。\n\n2️⃣ M1反弹但质量堪忧\nM1增速5.5%，比预期高0.5个百分点，M2-M1剪刀差收窄。看起来是定期存款在活化，好事？但研报点出关键：5月PMI新订单指数下滑到49.9，说明企业手里的钱更可能是预防性囤着，不是真拿去投资。\n\n3️⃣ 居民信贷还在收缩\n新增人民币贷款5200亿，但107%靠票据贴现撑，居民短贷和中长贷都在负增长。家庭存款增速也放缓了，5月甚至净减少。大家更爱存钱还是还债？数据看，去杠杆的节奏没停。\n\n三个K型复苏迹象：\n- 服务业PMI和制造业PMI的差距在拉大，AI相关出口很猛（5月出口同比+19.4%），但内需偏软，核心CPI环比还跌了0.1%。\n- PPI同比+3.9%继续走高，但上游涨价向下游传导不畅，出厂价和购进价的差距还在，\n\n[... middle omitted ...]\n\n29bn, 19% above consensus, driven by Rmb1.2tn issuance in government bonds, which contributes to 60% of new monthly TSF. Total TSF balance printed at Rmb458,810bn, +7.7% YoY. Corporate bond fi\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R003",
    "title": "GS：六月FOMC的真正焦点不是利率决议，而是新主席如何重塑美联储的沟通框架",
    "digest": "[wechat_article.md]\n# GS：六月FOMC的真正焦点不是利率决议，而是新主席如何重塑美联储的沟通框架\n\n市场参与者正在将目光投向即将到来的六月FOMC会议，但多数讨论集中在“是否会加息”这一表层问题上。然而，GS最新发布的这份研报提出了一个更值得关注的判断：本次会议最重要的变化并非利率路径本身，而是新任主席Kevin Warsh领导下的FOMC将如何重塑其沟通框架。就业市场已从疲软中显著回暖，通胀虽因战争和油价走高而居高不下，但美联储加息的概率依然很低。真正值得深度跟踪的，是点阵图的结构性变化、前瞻指引的措辞调整，以及Warsh个人对美联储沟通哲学的可能改造——这些变量将重新定义未来两年全球资产的定价锚。\n\n这份报告的核心洞察在于：市场可能低估了美联储从“降息预期管理”向“平衡型指引”切换的含金量。这不仅是文字游戏，而是美联储对自身反应函数的重新校准。以下是我们从GS研报中提炼出的五个关键判断，以及它们对投资者意味着什么。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 就业数据的强劲反弹让美联储拥有了“不着急”的底气，但这不等于加息风险消失\n\nGS明确指出，自上次FOMC会议以来，经济数据中最显著的变化是就业增长的强劲回升。报告中的就业趋势图显示，经过2025年下半年的持续低迷后，2026年初非农就业数据出现了明显的V型反弹，这使劳动力市场重新回到了更稳固的轨道上。这一变化的意义在于：它为美联储争取了时间，使其可以更从容地评估通胀数据，而不必急于做出反应。\n\n但需要警惕的是，GS并未因此降低对失业率的预测。报告预计2026年Q4失业率将维持在4.4%左右，比3月SEP中的4.3%略高。这意味着，就业市场的改善更多体现在增量上，而非存量结构的根本好转。对于投资者而言，这暗示了一个重要判断：美联储现在有空间“等一等”，但一旦通胀预期或工\n\n[... middle omitted ...]\n\n的二阶影响，并探讨Warsh上台后可能出现的超预期政策路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月FOMC前瞻：换帅首秀\n\n新主席上任，政策不变\n\n📌 6月会议看点：降息指引或删除\n\n最近就业数据强劲，让美联储暂时不用太担心经济。但油价推高通胀，核心PCE全年可能维持在3%以上。\n\n1️⃣ 加息概率低\n- 美联储历史上很少因油价冲击加息\n- 当前就业市场更平衡，工资增长温和，不容易形成通胀螺旋\n\n2️⃣ 6月会议预期\n- 利率维持不变，删除“额外调整的幅度和时机”措辞\n- 点阵图：2026年无变化，3位成员倾向加息\n- 中位数仍预计2027-2028年各降一次\n\n3️⃣ 经济预测调整\n- 2026年GDP从2.4%下调至2.2%\n- 失业率从4.4%微降至4.3%\n- 通胀大幅上调：整体PCE从2.7%升至3.9%\n\n4️⃣ 新主席Warsh首秀\n- 曾批评美联储沟通方式和缩表政策\n- 这次会议能看出他的施政思路\n\n⚠️ 如果通胀预期或涨价范围明显扩大，加息概率会上升。但目前看，更可能是长时间按兵不动。\n\n大家觉得新主席会带来什么变化？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n## US ECONOMICS ANALYST\n\n# June FOMC Preview: Lea\n\n[... middle omitted ...]\n\npandemic's wide-ranging shortages and price spikes.\n\nWe continue to see rate hikes as unlikely, both because the Fed has usually not hiked in response to oil price shocks in the past, and beca\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "Bernstein：太阳能加储能正在重新定义基荷电力的竞争边界",
    "digest": "[wechat_article.md]\n# Bernstein：太阳能加储能正在重新定义基荷电力的竞争边界\n\n市场对可再生能源的讨论长期停留在“间歇性”和“需要补贴”两个标签上。AI数据中心的爆发式增长，让电力供应的稳定性和可预测性成为比价格更紧迫的议题。Bernstein最新发布的全球储能深度报告，基于阿联酋Masdar与EWEC正在推进的吉瓦级项目，提出了一个值得产业决策者认真审视的判断：太阳能加储能不再是边缘补充方案，而是正在成为基荷电力的一个可行选项。\n\n这份报告的独特价值不在于复述储能成本下降的老生常谈，而在于第一次用实际工程数据证明了，通过系统性的过度建设和长时储能配置，可再生能源可以实现接近99.6%的供电可靠性。这个数字直接挑战了“太阳能无法承担基荷”的行业共识。\n\n我们基于报告的核心逻辑，提炼出五个层次的分析框架，帮助读者理解这一趋势对能源投资、AI基础设施布局和电池产业链的真正含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一个吉瓦级项目正在验证太阳能从间歇电源向可靠基荷的结构性转变\n\n阿联酋Masdar和EWEC联合推进的项目，其设计逻辑与传统可再生能源项目有本质区别。它不是为了最大化太阳能发电的利用小时数，而是为了输出连续稳定的1吉瓦电力。为此，项目配置了5.2吉瓦的太阳能装机，搭配19吉瓦时的储能系统，储能时长约19小时。\n\nBernstein的分析显示，基于当地辐照条件，这个系统每年可产生约12.45太瓦时的太阳能电力，而1吉瓦基荷负荷的年需求仅为8.76太瓦时。这意味着系统在能量层面被故意过度建设了约40%。白天的超额发电不是被弃掉，而是存入电池，在夜间和阴天释放。\n\n这种设计思路的关键转变在于：它不再把储能视为调峰工具，而是将其作为系统可靠性保障的核心环节。报告测算的系统可靠性达到99.6%，这个数字对于数据中心运\n\n[... middle omitted ...]\n\n都需要根据自己的具体场景，补充这些关键假设的验证。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光储一体化，AI用电新解法\n\n光储供电，不止是环保\n\n最近在看某外资投行的研报，讲了一个很有意思的项目——阿联酋的Masdar和EWEC正在建一个5.2GW光伏+19GWh储能的超级电站，目标2027年完工，能输出约1GW的持续电力。这可能是全球首个大规模验证“光储=稳定基荷”的案例。\n\n几点关键发现：\n\n1️⃣ 系统可靠性可达99.6%\n传统观点认为光伏+储能没法做基荷，但这个项目通过“过度建设”解决了问题。5.2GW光伏产生的多余电力不弃掉，而是存进19小时时长的储能系统，晚上再放出来。研报测算，这样能达到99.6%的系统可靠性，基本接近火电水平。\n\n2️⃣ 成本：在气价高的地方有竞争力\n项目总成本约60亿美元（约6000美元/kW），其中储能系统占了近一半。度电成本约97美元/MWh，能跟气价8美元/mmbtu以上的燃气发电竞争。如果储能时长降到12小时，度电成本可降到80美元/MWh，可靠性仍有95%。\n\n3️⃣ 建设时间快，但挑地方\n光储项目约2年建成，而燃气轮机现在交货要4年左右，核电更是6年以上。但缺点也很明显——需要高日照和大量土地。这个项目占地约60平方公里，相当于一个曼哈顿的面积。\n\n4️\n\n[... middle omitted ...]\n\nfor baseload power particularly for 24/7 AI-driven demand. Masdar and EWEC's gigascale solar-plus-storage project challenges this view with the world's first deployment of firm renewable power\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R005",
    "title": "Bernstein：全球储能市场正在经历从“量变”到“质变”的临界点",
    "digest": "[wechat_article.md]\n# Bernstein：全球储能市场正在经历从“量变”到“质变”的临界点\n\n这份由Bernstein分析师Neil Beveridge团队发布的Battery Weekly报告，表面上是一份周度动态汇总，但当我们把北美、亚洲、欧洲三个区域本周发生的十几个事件放在一起看，一个更重要的信号浮现出来：全球储能市场正在从“产能扩张驱动”的阶段，转向“技术路线分化与商业模式验证驱动”的新阶段。\n\n过去两年，市场对储能的理解主要停留在“量”的层面——多少GWh的产能规划、多少GW的装机目标。但本周的信息流显示，真正决定下一轮竞争格局的变量，已经从“谁建得更多”变成了“谁在技术路线上选对了方向、谁在商业闭环上走通了路径”。\n\n这不是一个渐进式的变化。钠离子电池从实验室走向项目落地，固态电池从材料验证走向系统集成，车企从动力电池向储能领域的战略跨界，以及直接提锂技术在美国的首次商业化尝试——这些事件在同一个时间窗口密集出现，意味着行业正在为下一轮结构性增长做技术储备和商业模式测试。\n\n对于产业决策者和投资者而言，现在需要回答的问题不再是“储能市场有多大”，而是“哪些技术路线将在下一轮竞争中胜出，哪些企业有能力完成从规模扩张到价值捕获的跃迁”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 车企的储能战略转型正在加速，这不仅仅是“第二增长曲线”\n\n通用汽车本周宣布进入固定式储能市场，与Peak Energy和Redwood Materials合作开发钠离子电池用于电网储能，并推进V2G技术。福特此前已经做了类似的布局。Bernstein的这份报告捕捉到了一个关键趋势：车企正在将其在动力电池领域积累的能力，系统性地向储能领域迁移。\n\n这背后有两个驱动因素。第一，AI数据中心带来的电力需求激增，创造了一个全新的、高确定性的储能需求场景\n\n[... middle omitted ...]\n\n可以与其他产业研究者一起探讨那些尚未被市场定价的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 数据中心需求，正在改写储能格局\n\n储能行业正在换挡\n\n**1. 美国：大项目 + 新玩家**\n- Cypress Creek 拿了 35 亿美元融资，在 Arkansas 建 1.63GW 光伏配 1.9GWh 储能，电是卖给科技公司的。AI 和云计算的用电需求，正在成为储能大项目的直接推手。\n- GM 也下场了，学福特，跟 Peak Energy 和 Redwood 合作做钠离子电池，目标是电网储能。技术路线选钠离子，理由是成本低、安全性好、材料不缺。同时推 V2G（车网互动），让电动车给电网放电。\n\n**2. 亚洲：扩产 + 技术迭代**\n- 中国 Lopal 投 1.6 亿美元在印尼扩 LFP 正极材料，12 万吨年产能，目标是 LG 和宁德时代的需求。\n- 宁德时代跟 Capchem 签了 3 年电解液大单，2028 年要买 15 万吨，按现价算约 81 亿人民币。这个量级说明储能电池出货量还在高速爬坡。\n- 韩国 Toptec 拿到了印度车企的电池模组设备订单，13 亿韩元，首次直接出海。\n- CK Solution 做了个除湿机，专为固态电池产线设计，风量是常规的 2.4 倍，能帮工厂省 3\n\n[... middle omitted ...]\n\nof battery storage, with electricity to be supplied to a large technology company amid rising AI and data center power demand. The deal highlights continued strong investor support for solar a\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "美国银行：市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 美国银行：市场真正低估的不是需求，而是供给侧的再定价\n\n当市场还在争论AI芯片出货量能否持续超预期时，一份来自美国银行的全球存储技术周报揭示了一个更深层的结构性变化：存储芯片行业正经历一场前所未有的定价权转移。这不是一轮简单的周期性涨价，而是供给格局重塑后，行业定价机制的根本性改变。\n\n这份报告的核心判断值得每一位产业决策者关注：存储芯片的超级周期并非昙花一现，其背后是技术迭代、产能约束与地缘因素三重力量叠加的结果。而市场目前最大的误判，是将这轮涨价简单归因于AI需求的短期爆发，忽视了供给侧结构性收缩带来的长期影响。\n\n报告中最具冲击力的数据是：韩国半导体在6月前10天的出口额达到111亿美元，环比增长30%，同比增长206%。这已经是连续第五个月实现三位数同比增长。与此同时，美国银行的存储指标在2026年3-4月达到189的历史峰值，这一数字远超此前设定的140上限，迫使研究团队将指标天花板调整至240。\n\n这些数据背后，是一场正在发生的产业权力交接。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n存储芯片行业历来以强周期著称，但本轮周期的驱动力与以往截然不同。过去，存储芯片价格波动主要由终端需求驱动，PC和手机出货量的增减直接决定芯片价格走势。而本轮周期中，供给侧的结构性变化正在成为主导力量。\n\n报告指出，DRAM现货价格在6月第二周出现明显反弹，DDR4和DDR5分别环比上涨3-4%。这一价格走势并非孤立现象。中国5月集成电路进口额达到566亿美元，同比增长68%，但进口数量仅下降1%。这意味着，价格上涨几乎全部由单价提升驱动，而非需求量的扩张。\n\n这种“量平价升”的格局，是供给侧定价权增强的典型特征。对于三星、SK海力士、美光等头部企业而言，这意味着它\n\n[... middle omitted ...]\n\n将在群内分享完整研报的解读，并围绕上述未解问题持续跟踪更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNVIDIA新CPU的存储容量没缩水\n\nVera存储不减量\n\n市场传闻可能是误读\n\n最近有个传闻挺有意思，说NVIDIA新款CPU Vera的存储容量要砍半，从1500GB降到750GB。我仔细翻了下研报，发现这个说法大概率不成立。\n\n1/ **Vera Rubin依然是1500GB为主流**\n- 带HBM4的Vera Rubin超算芯片，标配是192GB×8的SOCAMM，也就是1500GB\n- 不带HBM的Vera CPU机架，可以用750GB（96GB×8），但初始出货也是1500GB\n- 客户（Google、Amazon、微软、Meta）可以自己选配，但低配会影响性能\n\n2/ **存储需求不仅没减，还多了增量**\n- 初始SOCAMM订单都是给Vera Rubin的\n- Vera CPU机架是新增需求，反而扩大了整体市场空间（TAM）\n- 所以这波不是砍单，是扩容\n\n3/ **行业数据也在印证景气度**\n- 韩国6月上旬半导体出口创历史新高：110亿美元，同比+206%\n- DDR4/DDR5现货价格周涨3-4%\n- 台湾存储厂商5月营收同比暴涨：南亚科+730%，群联+301%\n- 中国5月IC进口\n\n[... middle omitted ...]\n\nVera CPU rack. Net-net, we conclude 1) Vera Rubin should continue to use 1,500GB (750GB possible but lower performance), and 2) Vera CPU rack also should initially use 1,500GB, but it can work\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R007",
    "title": "Bernstein：AI前沿模型的可逆性，才是市场真正低估的风险",
    "digest": "[wechat_article.md]\n# Bernstein：AI前沿模型的可逆性，才是市场真正低估的风险\n\n这份Bernstein研报以一个虚构但极具警示意味的故事开场：Anthropic的Claude Fable 5模型在发布后被美国商务部以国家安全为由要求撤回，AI前沿首次出现了“倒退”。这不仅仅是一次技术事故，它揭示了一个市场尚未充分定价的结构性变量——前沿AI模型的可用性，可能不再由技术能力决定，而是由地缘政治意志决定。\n\n报告的核心判断是：当AI模型从工具演变为关键基础设施，其“可被远程关闭”的特性将从根本上改变企业采购决策、主权AI战略，甚至全球AI竞争格局。这不是一个短期扰动，而是一个需要重新评估AI资产定价框架的信号。\n\n市场的注意力仍集中在模型参数、基准分数和推理成本上。但Bernstein提醒我们，一个更根本的问题正在浮出水面：如果最前沿的模型可以在一夜之间“被消失”，那么依赖这些模型构建的业务，其底层假设还成立吗？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一个虚构故事背后的真实警告：AI前沿的“可逆性”从未被定价\n\nBernstein巧妙地借用了一个寓言：Anthropic的Claude Fable 5发布后即被撤回，理由是国家安全。尽管报告认为这一决定可能很快被逆转，Anthropic也将重回榜单前列，但事件本身的意义远超基准分数。\n\n这不仅仅是技术问题。它首次公开表明，前沿AI模型的可用性可以因非技术原因而被中断。市场此前对AI的定价，隐含了一个关键假设：最先进的模型始终可用，且技术演进是单向的、不可逆的。现在，这个假设出现了裂缝。\n\n对于任何将AI嵌入核心业务流程的企业而言，模型的“可撤销性”是一个全新的风险维度。过去，企业担心的是模型性能不足或成本过高；现在，它们需要开始担心模型是否会被“拔掉电源”。这个风险尚未\n\n[... middle omitted ...]\n\n趣，欢迎来星球微信群里继续讨论，一起追踪这个判断的后续验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI前沿模型刚被“撤回”了一次\n\nAI模型也能被“下架”？\n\n**1. 一个真实发生的“撤回”事件**\n投行研报记录了一个罕见案例：Anthropic的Claude Fable 5模型，刚发布就被美国商务部以国家安全为由要求撤回。这是AI前沿首次“倒退”。虽然研报认为禁令大概率会撤销，但这件事本身已经值得深思。\n\n**2. 主权AI的理由变强了**\n想想看：一个前沿AI模型，可以因为远在千里之外的某个决定被直接关停。随着AI工具越来越深入关键业务，大型企业和主权国家会开始追问——那些部署在云端的模型，到底靠不靠谱？如果访问权不在自己手里，谁敢把核心业务交给它？这是研报提出的核心观察。\n\n**3. 中国AI实验室的“周末突袭”**\n有意思的是，Kimi和Z.ai（研报认为的中国前沿AI实验室）恰好在这个周末发布了新模型。K2.7 Code主推理效率升级，Z.ai的GLM-5.2直接对标Claude Opus 4.8。研报的初步测试结果不错，认为这支持了一个观点：中国头部实验室能继续跟上全球节奏。更微妙的是，在主权AI的叙事下，中国开源模型可能意外占据了“道义高地”。\n\n**4. 地缘竞争下的AI新规则**\n这次\n\n[... middle omitted ...]\n\n)  \nMin-Joo Kang\n\n+852 2123 2644\n\nminjoo.kang@bernsteinsg.com\n\n![](images/7d9c70e0b51bd1512a81da5f4e6cad1ade29cda6f4234eb2f27a9ffc2b1ce0e8.jpg)  \nHyrum Caesar\n\n+81 3 6777 6979\n\nhyrum.caesar@be\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R008",
    "title": "GS：卢比贬值压力正在被结构性变量消化，而非基本面恶化",
    "digest": "[wechat_article.md]\n# GS：卢比贬值压力正在被结构性变量消化，而非基本面恶化\n\n市场对印度卢比持续走弱的担忧，很可能高估了外部失衡的风险，而低估了印度国际收支结构正在发生的根本性变化。GS最新发布的《Asia in Focus：印度国际收支前景更为有利》报告，提出了一个与市场主流认知形成鲜明对比的判断：尽管中东地缘冲突推高油价、全球资本流动趋于谨慎，但印度在2026年第一季度仍录得约72亿美元的国际收支顺差，经常账户甚至出现70亿美元盈余。这份报告的核心贡献，不在于预测卢比何时见底，而在于系统性地拆解了印度外部账户中几个被市场忽视的“结构性缓冲器”——石油强度下降、进口弹性上升、黄金进口的政策可调节性，以及央行精心设计的一套资本流入激励机制。这些因素叠加在一起，意味着印度当前面临的国际收支压力，本质上不是一次不可持续的外部危机，而是一次由不确定性驱动的、可被政策工具对冲的周期性扰动。\n\nGS据此大幅下调了印度经常账户赤字预测：2026年从GDP的2.0%下调至1.3%，2027财年从2.1%下调至1.7%。更重要的是，该机构预计印度在2026和2027财年每年都将录得约GDP 0.6%的国际收支顺差。这个判断如果成立，将意味着卢比的贬值空间比市场预期的要小得多，而印度资产的相对吸引力可能被系统性重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场误读了卢比走弱：这不是基本面恶化，而是预防性美元需求\n\nGS在报告开头就直接点明了一个关键矛盾：卢比的近期弱势，看起来比国际收支基本面所暗示的要大。2026年第一季度，尽管面临能源冲击和资本流入放缓的担忧，印度的国际收支依然录得约72亿美元顺差。经常账户更是出现70亿美元盈余，背后是创纪录的侨汇流入、强劲的服务贸易顺差，以及低于预期的石油进口账单。\n\n那么，卢比为什么还在走弱？GS的\n\n[... middle omitted ...]\n\n文、GS的敏感性测算表格，以及针对上述未解问题的进一步推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度卢比跌过头了？看看真实数据\n\n📊 卢比被低估了？\n\n某外资投行最新研报指出，印度Q1国际收支其实录得72亿美元顺差，经常账户还出现了70亿美元盈余。卢比走弱更多是中东局势引发的预防性美元需求，不是基本面恶化。\n\n📌 为什么油价冲击没那么可怕？\n\n1️⃣ 印度石油强度持续下降（能源效率提升+交通电动化）\n2️⃣ 油价超80美元/桶时，进口量反而下降\n3️⃣ 国内油价涨10%，汽油消费增速12个月平均降3%\n\n📌 黄金进口也有办法控制\n\n历史经验显示，提高进口关税后1-2个月，黄金进口量就开始下降，5-6个月后降幅可达40-50%。5月的关税上调已经在起作用。\n\n📌 经常账户赤字预测大幅下调\n\n研报将2026年经常账户赤字预测从2.0%GDP下调至1.3%（约460亿美元），主要因：\n- 石油进口预测从2440亿降至2200亿美元\n- 黄金进口从640亿降至560亿美元\n- 侨汇收入上调至1360亿美元\n\n📌 卢比会怎么走？\n\n预计贬值压力缓解，但大幅升值空间有限。央行可能会通过囤积外汇储备来吸收新增美元流入，而不是让卢比升值。\n\n欢迎一起讨论印度市场的逻辑变化～\n\n#学习笔记\n\n[source_mineru\n\n[... middle omitted ...]\n\nIndia's oil intensity has declined steadily since 1990s, reflecting improved energy efficiency, rising transport electrification, and a shift toward less energy-intensive growth. Post-pandem\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "GS：香港IPO市场的Alpha，藏在三个被低估的策略窗口里",
    "digest": "[wechat_article.md]\n# GS：香港IPO市场的Alpha，藏在三个被低估的策略窗口里\n\n香港IPO市场正在经历一次不容忽视的复苏。2025年至今，已有超过60只新股完成上市，首日平均涨幅45%，首月平均涨幅49%，三个月平均涨幅达到67%。这些数字本身已经足够吸引注意力，但GS这份研报的核心价值不在于确认“IPO赚钱”，而在于揭示了一个更关键的问题：在回报高度分化的市场中，什么样的信号能帮助你筛选出超额收益，什么样的风险会在锁定期后集中释放。\n\n这份报告提出了三条清晰的交易策略路径，但真正值得产业决策者和投资者思考的，不是策略本身，而是这些策略背后反映出的市场结构性变化——IPO不再是简单的“打新”游戏，而是一个需要精细化判断的资产配置环节。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 大型股、独立上市与高认购倍数，构成了短期回报的最强信号\n\nGS对2025年以来香港主板IPO的因子分析显示，有几个变量在统计上对首日及首周回报具有显著解释力。\n\n首先是市值规模。大型股IPO在首日、首周、首月乃至三个月的时间窗口内，均持续跑赢小型股。这并非直觉上的“大盘股稳健”，而是反映了当前市场环境下，资金更倾向于向流动性好、机构覆盖充分的标的集中。小盘股虽然在极端行情下可能爆发，但概率和持续性都不及大盘股。\n\n其次是上市类型。独立在港上市的公司，其表现显著优于A+H双重上市的公司。背后的逻辑并不复杂：双重上市的公司已经在A股市场有定价锚，香港市场的交易更多是套利或配置需求，而非纯粹的发现价格。而独立上市的公司，尤其是那些选择香港作为唯一上市地的企业，往往具备更强的融资诉求和市场沟通意愿，也更容易吸引增量资金。\n\n第三个信号是零售超额认购倍数。GS的数据显示，高认购倍数的股票在上市首周内表现出更强的价格动能。但这个效应的持续性有限——到了六个月的\n\n[... middle omitted ...]\n\n的核心发现，结合最新的市场动态，持续跟踪这些策略的实战效果。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n港股打新还能赚吗？三个策略帮你选\n\n**打新策略复盘**\n\n**2025-2026年港股IPO平均首日涨45%**\n\n---\n\n今年港股IPO市场真的回来了。超过60只新股上市，首日平均涨45%，一个月涨49%，三个月涨67%。\n\n但别光看平均数——表现分化很大。最好的涨了10倍，最差的跌了74%。怎么挑？三个策略分享。\n\n**1. 哪些新股更容易涨？**\n\n某外资投行拆解了关键因素：\n\n- **大盘股 > 小盘股**：独立上市的大市值公司表现更好，A+H两地上市的反而不行\n- **零售认购倍数高**：短期有催化，但效应很快消退\n- **基石投资者持股30%-50%**：这个区间的公司中长期表现更强，低于或高于都不如\n- **新经济 > 传统行业**：生物科技、AI公司3个月涨130%和70%，金融股反而跌了5%\n- **估值不是关键**：高增长比低估值更重要，亏损但增速快的公司反而被市场追捧\n\n**2. 锁定期到期怎么办？**\n\n未来12个月，预计有2740亿美元的解禁股进入港股市场，创历史新高。\n\n历史数据显示：解禁后3个月股价平均跌4%，6个月跌7%。但同样是分化很大。\n\n短期的压力主要看解禁股占总股本\n\n[... middle omitted ...]\n\nl oversubscription serves as a primary catalyst for short-term price appreciation, while moderate cornerstone ownership of $30\\%$ to $50\\%$ signals high-quality listings positioned for sustain\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R010",
    "title": "GS：消费分化的本质不是需求疲软，而是品牌议价权的再分配",
    "digest": "[wechat_article.md]\n# GS：消费分化的本质不是需求疲软，而是品牌议价权的再分配\n\n5月消费数据出炉，市场普遍关注的是“需求是不是又弱了”。但GS这份5月线上品牌追踪报告揭示了一个更值得深究的信号：品类层面的下滑与品牌层面的分化同时存在，且分化程度正在加剧。这并非简单的“消费降级”或“需求不足”所能概括。\n\n真正的问题是：在平台补贴、政府刺激和618大促节奏的多重叠加下，哪些品牌有能力把外部变量转化为自身增长，哪些品牌正在失去定价权和渠道话语权。GS的数据表明，答案越来越取决于品牌在“全渠道运营”和“产品力溢价”上的真实能力，而非单纯依靠流量红利。\n\n这份报告最值得关注的判断是：消费板块的投资逻辑正在从“赛道选择”切换到“品牌选择”。同一品类内，头部品牌的增速差距可以超过50个百分点。这意味着，未来的超额收益将更多来自对品牌个体竞争力的深度拆解，而非对宏观消费趋势的押注。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月线上消费的“假摔”背后，藏着结构性加速的品类\n\n如果只看天猫、淘宝、京东三大平台的合并数据，5月消费表现确实令人担忧。女性服装勉强持平，运动鞋、美妆、保健品、乳制品、运动服饰、小家电、婴幼儿配方奶粉、啤酒、宠物食品、白电无一例外录得同比下滑，跌幅从2%到31%不等。\n\n但GS的数据并没有停留在这一层。当纳入抖音渠道后，画面发生了根本性变化：美妆品类合并GMV同比增长14%，较4月的11%进一步加速。运动服饰和调味品的核心品牌GMV增速分别达到14%和47%，同样高于4月的9%和34%。\n\n这意味着什么？传统电商平台的数据正在失去作为“消费温度计”的完整性。消费者正在大规模向内容电商迁移，而不同品牌对这一趋势的适应能力天差地别。那些在抖音上建立了有效运营体系的品牌，正在从这一渠道迁移中获益；而那些仍依赖传统\n\n[... middle omitted ...]\n\n更细致的图表解读，也会持续跟踪6月合并数据出来后的最新信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618消费风向：谁在加速，谁在承压\n\n📊 5月线上消费图景\n\n5月线上消费整体偏弱，但618大促正在改写格局。\n\n只看天猫/淘宝/京东三个平台，几乎所有品类都在跌。女装勉强持平，运动鞋/美妆/保健品/乳制品/运动服/小家电/奶粉/啤酒/宠物食品/白电，同比分别-2%/-4%/-6%/-9%/-11%/-18%/-19%/-22%/-22%/-31%。\n\n但如果把抖音加进来，故事就不一样了。\n\n**美妆：分化最明显的赛道**\n\n全平台（含抖音）看，5月美妆GMV同比增长14%，比4月的11%还在加速。背后是平台补贴+地方政府消费券在发力。\n\n国货品牌明显回暖：林清轩+110%，珀莱雅+64%，薇诺娜+43%，毛戈平+43%，巨子生物+20%。但也不是所有国货都好，华熙生物-19%，逸仙电商-36%。\n\n外资这边，雅诗兰黛+36%，欧莱雅+16%，资生堂+11%。高端线表现更稳，欧莱雅靠皮肤学级产品拉动，大众线反而被国货抢了份额。\n\n618前25天（5.15-6.8），抖音上林清轩继续三位数增长（基数低），珀莱雅+64%，薇诺娜+51%，毛戈平+43%，巨子生物+20%。\n\n**运动服饰：品牌之间冰火两重天**\n\n[... middle omitted ...]\n\note: Tracker data suggest a meaningful re-base in Beauty and Supplements for Tmall/Taobao numbers in 2025 Jan - May.\n\nConsidering Douyin/Tmall/Taobao/JD combined, we saw Beauty GMV growing at \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "美国银行：市场低估了未来三个月A股和港股的流动性分化",
    "digest": "[wechat_article.md]\n# 美国银行：市场低估了未来三个月A股和港股的流动性分化\n\n这份由美国银行在6月12日发布的研报，首次推出了一个名为“China Flow Lens”的月度流动性追踪产品。在大多数市场参与者还在争论估值和盈利预期时，这份报告将焦点拉回到一个更底层、更直接的变量：资金的供给与需求。\n\n报告的核心判断非常清晰，但容易被市场情绪淹没：**当前流动性条件对A股仍然友好，但港股正面临显著的短期压力，而这种分化在未来三个月可能加剧。**\n\n这不是一个简单的“看好A股、看空港股”的判断。它背后是一系列正在发生但尚未被充分定价的结构性变化：国家队资金的撤退节奏、南向资金的突然转向、以及港股即将到来的解禁洪峰。这篇导读将提炼报告中最值得关注的几个洞察，并指出那些报告尚未完全展开、但值得投资者自行追问的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. A股和港股正在经历完全不同的流动性周期\n\n报告通过一张流动性仪表盘清晰地展示了这种分化。5月份的数据显示，A股市场的日均成交额（ADTV）从4月的2.34万亿元人民币大幅回升至3.18万亿元，而港股的日均成交额虽然也从2534亿港元升至2928亿港元，但支撑其上涨的资金结构完全不同。\n\nA股的支持力量来自内部：混合型基金发行量创下四个月新高，达到481亿份；股票回购规模也攀升至171亿元人民币，为12个月最高。这些是内生的、可持续的流动性供给。\n\n而港股的支撑更多依赖外部变量：南向资金在5月出现了36亿港元的净流出，与4月565亿港元的净流入形成鲜明对比。同时，EPFR追踪的海外中国基金虽然整体呈流入态势，但MSCI中国指数基金仍在持续遭遇赎回。\n\n**这意味着什么：** A股的流动性改善更多来自国内资产配置的内生修复，而港股的流动性则高度依赖外部资金的持续流入。一旦外部环境出\n\n[... middle omitted ...]\n\n分享更详细的图表拆解、历史复盘以及对这些未解问题的跟踪分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nA股流动性还在，但压力已在路上\n\n流动性转向了吗？\n\n最近某外资投行出了一份新的流动性跟踪报告，信息量很大，我拆了几个关键点👇\n\n**1/ 短期流动性依然OK，但拐点快到了**\n\n5月A股日均成交额回升到3.2万亿，比4月的2.3万亿明显放大。新基金发行、回购也都在增加，短期环境不差。\n\n但问题是：未来3个月压力会明显上升。\n\n**2/ 港股面临更大压力**\n\n南向资金5月净流出36亿港元，4月还是净流入565亿。加上港股7月、9月有大量解禁，7月预计2700亿港元，9月更是接近4000亿。这个量级不容忽视。\n\n**3/ “国家队”在退场**\n\n跟踪国内ETF的资金流向发现，过去一个月ETF仍在持续净赎回。而且今年以来的累计赎回量，已经超过了2023-2025年流入的总和。研报认为，这意味着之前的托市力量基本已撤出，但换个角度，也为未来留出了政策空间。\n\n**4/ 外资在回流，但结构分化**\n\n跟踪EPFR数据看，5月外资流入中国权益基金加速了。全球新兴市场基金对中国和台湾的配置低配在收窄，对印度则在扩大低配。但资金主要流向A股和港股基金，MSCI中国基准基金还在净赎回。\n\n整体结论：A股短期流动性环境优于港\n\n[... middle omitted ...]\n\nal team” capital provides downside support for A-shares, Hong Kong faces near-term headwinds from slowing southbound inflows, tighter cross-border capital rules, and an upcoming wave of lock-u\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R012",
    "title": "GS：中国经济的“温差”正在扩大，市场低估了结构分化的烈度",
    "digest": "[wechat_article.md]\n# GS：中国经济的“温差”正在扩大，市场低估了结构分化的烈度\n\n五月的中国宏观数据，呈现出一幅让人难以简单下判断的画面。出口和进口双双超预期，PPI同比继续攀升，但CPI纹丝不动，信贷总量看似回暖，细节却透露出需求的疲软。GS在最新一期中国经济快报中，用一组看似矛盾的数据，揭示了一个核心判断：中国经济正在经历一轮罕见的“结构性温差”——供给端受AI资本开支和上游价格修复的拉动，而需求端，尤其是终端消费和私人投资，依然在低位徘徊。市场如果只看到贸易数据亮眼就认为经济复苏已经稳固，很可能误判了接下来的政策节奏和资产定价逻辑。这份报告真正的价值，不在于罗列数据，而在于点出了“温差”背后，哪些是可持续的结构性力量，哪些是短期扰动，以及政策可能如何回应。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI资本开支已成中国贸易增长的“单引擎”，其可持续性才是关键问题\n\n五月的贸易数据无疑是这份报告最亮眼的信号。出口同比增长19.4%，进口同比增长27.5%，双双超出市场预期。但GS并没有停留在“贸易强劲”这个结论上，而是直接指出了驱动力的集中度问题：半导体和自动数据处理设备（含数据中心设备）两项，合计贡献了五月出口和进口增长的大约一半。\n\n这意味着，中国贸易的韧性，正在高度依赖AI资本开支这一条主线。这不是一个分散的、由全球消费需求回暖带动的全面复苏，而是一个由特定产业周期驱动的结构性脉冲。从服务器、芯片到数据中心基础设施，中国既是全球AI硬件供应链的重要出口方，也是关键设备和原材料的进口方。因此，贸易数据的两端同步走强，本质上反映的是同一个故事——全球AI投资热潮在实物层面的落地。\n\n对于投资者而言，这里的关键问题不是五月的贸易数据好不好，而是这一增长引擎的可持续性。全球AI资本开支是否会在未来几个季度出现边际放缓？中国\n\n[... middle omitted ...]\n\n的范围。这份报告没有给出所有答案，但它提供了正确的提问方式。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月贸易数据超预期\n\n贸易出口强劲\n\nAI算力拉动出口，但内需偏弱\n\n---\n\n**1. 出口超预期，AI是主因**\n\n5月出口同比+19.4%，进口+27.5%，都超过市场预期。\n\n主要推手是AI相关投资：半导体+数据中心设备合计贡献了约一半的进出口增量。AI算力投资带来的硬件需求，正在直接体现在贸易数据上。\n\n**2. PPI在涨，但CPI没动**\n\nPPI同比从4月的2.8%涨到5月的3.9%，但CPI一直停在1.2%。\n\n上游涨价没有传导到消费端，说明终端需求偏弱。研报预计5月零售和固定资产投资都会同比下滑。\n\n**3. 2万亿数据中心投资？不是新消息**\n\n最近有报道称政府计划投入2万亿建设数据中心，引发关注。\n\n但研报指出，这其实是\"十五五\"规划中\"六网\"的一部分，不是新动作。六网包括：水网、新型电网、算力网（含数据中心）、下一代通信网、城市地下管网、物流网。今年六网投资可能超过7万亿（占GDP的5%）。\n\n---\n\n**讨论：** AI带来的出口增长，能不能弥补内需的缺口？欢迎一起聊聊。\n\n#学习笔记\n\n[source_mineru.md]\n# China: Three things in Ch\n\n[... middle omitted ...]\n\ndetails>\n<summary>line chart</summary>\n\n| Year | Exports | Imports |\n|------|---------|---------|\n| 2018 | ~25     | ~20     |\n| 2019 | ~10     | ~5      |\n| 2020 | ~-20    | ~-10    |\n| 2021 \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "NOM：人民币中间价模型正在发出一个被市场低估的政策信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在发出一个被市场低估的政策信号\n\n人民币中间价的设定机制，正在成为观察中国政策意图最精确的窗口。NOM最新发布的USD/CNY中间价模型测算给出了一个值得认真对待的信号：模型无逆周期因子调整的预测值为6.7544，较前一日官方中间价低565个基点，较前一日官方即期收盘价低72个基点。这不是一个普通的波动，而是一个系统性的偏移。\n\n这份报告的真正价值不在于预测了一个具体的汇率数字，而在于它揭示了一个事实：在看似平静的中间价背后，模型与实际定价之间的偏差正在积累，而这种偏差本身就是政策意图的表达。对于关注中国资产定价、跨境资本流动和出口竞争力的决策者来说，理解这个偏差的含义，比猜测下一个中间价是多少更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型偏差的累积方向，比任何单日预测都更具信号意义\n\nNOM的模型误差图表显示了一个值得注意的趋势。从2025年1月到2026年4月，每日模型误差（即模型预测值与实际中间价之间的差值）从约-1800个基点逐步收敛至接近零，并在2026年4月转为正值约600个基点。这个轨迹说明了两件事。\n\n第一，2025年初，实际中间价显著强于模型预测，这意味着当时政策端在主动引导人民币汇率偏强，以对抗贬值预期或支撑市场信心。第二，到2026年4月，误差方向逆转，实际中间价开始弱于模型预测，尽管幅度不大，但方向性的转变才是关键。\n\n这个转变的含义是，政策端对汇率贬值的容忍度正在上升，或者更准确地说，政策端不再认为维持偏强汇率是当前优先目标。对于观察者而言，这比任何一次具体的中间价调整都更重要，因为它反映的是政策立场的边际变化，而不是战术性的日间操作。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 逆周期因子的使用\n\n[... middle omitted ...]\n\n们一起拆解这份报告的每一个细节，探讨人民币汇率的下一步走向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型，探到6.75附近\n\n模型指向6.75\n\n比前次低了565个基点\n\n最近看某外资投行的研报，他们在跟踪人民币中间价的定价模型。模型最新跑出来的数字是6.7544，相比上一次的6.8109，低了565个pips。这个变化值得关注。\n\n1️⃣ 模型怎么算的\n模型会参考一篮子货币隔夜的变动，加权计算对中间价的贡献。这次贡献最大的几个货币是：欧元（-24 pips）、澳元（-13 pips）、韩元（-8 pips）、泰铢（-5 pips）。欧元走弱是主要拖累。\n\n2️⃣ 加上逆周期因子\n如果加入逆周期因子调整，模型预测的中间价是6.7757，比上次官方中间价低了352个pips。逆周期因子可以理解为央行平滑汇率波动的工具，这里显示其仍在发挥作用。\n\n3️⃣ 模型误差在收窄\n从历史模型误差看，2025年初误差高达-1800 pips，到2026年4月已收窄至600 pips左右。这说明模型对中间价的拟合度在提升，预测的参考价值在增强。\n\n4️⃣ 重要时间节点\n研报还列了一些后续值得关注的事件：7月底的政治局会议、11月深圳APEC、12月的中央经济工作会议，以及年底可能的中美领导人会晤。这些都可能影响汇\n\n[... middle omitted ...]\n\n![](images/a4d784474f8722e94ed968aa1186b9540853913470ada9d3bb4be145f6468cdf.jpg)\n\n<details>\n<summary>bar chart</summary>\n\n| Currency | Top 4 weighted contribution to projected change (pips) |\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R014",
    "title": "GS：中国半导体市场的真实强度，被进口均价的大幅跳升所揭示",
    "digest": "[wechat_article.md]\n# GS：中国半导体市场的真实强度，被进口均价的大幅跳升所揭示\n\n市场对2026年中国半导体行业的讨论，大多集中在产能扩张的速度和国产替代的叙事上。但最新出炉的4-5月贸易与生产数据，揭示了一个更深刻、也更值得推敲的信号：中国半导体需求的强度，并非简单地体现在量的增长上，而是通过进口金额与进口量的严重背离，暴露了产品结构正在发生根本性迁移。\n\nGS这份最新的大中华区半导体月度追踪报告，核心判断并非“需求很好”或“生产很强”，而是：**中国正在以更高的成本，进口价值密度更高的芯片，同时自身的出口能力也在以惊人的速度升级。** 这意味着，投资逻辑的锚点，需要从“谁在扩产”转向“谁在价值链上爬升”。\n\n以下是我们从这份报告中提炼出的四个关键洞察，以及一个悬而未决的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 进口“量减价增”的剪刀差，暴露了需求结构的高端化转向\n\n2026年5月，中国IC进口金额同比增长68.0%，但进口量却同比下降了1.0%。这组数据是整篇报告最核心的信号。它直接导致了一个结果：5月IC进口均价同比飙升了69.7%。\n\n这不仅仅是涨价。这是需求结构的质变。\n\n当一个市场的进口量基本持平甚至微降，但进口金额却以接近70%的速度增长时，唯一的解释是：终端客户不再大量采购低单价、成熟制程的通用芯片，而是转向了高单价、高性能的计算芯片、存储芯片或AI加速芯片。这与中国本土AI算力建设、以及高端智能手机和服务器市场的复苏逻辑高度吻合。\n\nGS的库存数据也支持这一判断。4月中国电子制造业的库存天数（DOI）为61天，与过去几年的平均水平基本持平。这意味着，当前的高进口额并非企业在恐慌性囤货，而是真实的、结构性的需求拉动。库存没有爆表，价格却在大幅上涨，这是典型的需求驱动型涨价，而非成本推动。\n\n![研\n\n[... middle omitted ...]\n\n里分享完整的原始图表数据，并持续追踪这些关键变量的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片进口金额大涨68%意味着什么？\n\n半导体需求持续走强\n\n某外资投行最新研报显示，2026年4-5月中国半导体需求持续强劲，核心数据值得关注：\n\n1️⃣ 进口金额大幅增长\n5月IC进口金额同比+68%（4月+54.7%），但进口量同比-1%。这说明进口单价在快速提升，5月IC进口ASP同比大涨69.7%——高端芯片需求旺盛。\n\n2️⃣ 国产产量加速增长\n4月中国IC产量同比+22.1%（3月+20.6%），产量达48亿颗。国产替代趋势持续，产量增速连续两个月加速。\n\n3️⃣ 出口同样强劲\n5月IC出口金额同比+110.9%至355亿美元，2026年前5月累计出口1391亿美元，同比+89.8%。中国芯片在全球市场竞争力增强。\n\n4️⃣ 库存健康\n4月电子制造业库存天数61天，与过去几年平均水平相当（59/57/64天），没有明显库存积压。\n\n5️⃣ 设备进口分化\n4月半导体设备进口额同比-4.2%，但测试设备进口额同比+48.4%。光刻机进口量同比-29%，均价同比-43%——这里推测与荷兰出口限制有关。\n\n研报观点：AI驱动、ADAS/自动驾驶趋势、本土供应商份额扩张，是支撑中国半导体发展的三大主线。先进\n\n[... middle omitted ...]\n\n9/57/64 days in Apr 2025/2024/2023).\n\nOverall, the Apr-May data indicates semiconductor demand remains solid in the China market. We continue to prefer stocks with strong company-specific driv\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "GS：日本银行股的估值重估才刚刚开始，市场低估了ROE目标的战略含义",
    "digest": "[wechat_article.md]\n# GS：日本银行股的估值重估才刚刚开始，市场低估了ROE目标的战略含义\n\n当市场还在争论日本央行加息路径的不确定性时，一份来自GS的研报揭示了一个更值得关注的信号：日本主要银行正在系统性地将ROE目标从“可接受的10%”上调至“全球同业级别的15%”。这不是简单的财务预测调整，而是日本银行业经营逻辑的根本性转变。\n\n三菱UFJ金融集团（MUFG）预计本财年就能实现其当前中期计划的12% ROE目标，并已明确将目光投向“中双位数”水平。三井住友金融集团（SMFG）更是在今年3月就向市场抛出了15%的中长期ROE目标，并详细拆解了实现路径。Mizuho金融集团（Mizuho）则将中期ROE目标从10%提升至12%，并直言要“超越PBR 2.0倍”。\n\n这些数字背后，隐藏着一个更大的叙事：日本银行股长期以来被视为“低增长、低回报”的估值折价，可能正在被系统性地修复。GS的报告提供了一个关键的分析框架——当ROE从当前的6-10%区间向中期目标的10-12%甚至中长期目标的15%迈进时，沿着当前的P/B-ROE斜率推算，对应的市净率倍数存在显著的上行空间。\n\n这不是一个短期交易信号，而是一个结构性重估的起点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中期计划中的ROE目标不再是“愿景”，而是“路线图”\n\nGS这份报告的核心贡献，在于它系统性地梳理了日本主要银行在最新一轮财报季中更新的中期计划。这些计划不再是模糊的“我们希望提高盈利能力”，而是包含了具体的政策利率假设、业务驱动因素和量化目标。\n\n以SMFG为例，其12%的中期ROE目标建立在1.25%政策利率假设之上，驱动因素包括Olive/Trunk存款平台收入、公司业务、交易银行业务以及亚洲投资利润。Mizuho的12%目标则基于0.75%的政策利率，更依赖公\n\n[... middle omitted ...]\n\n继续交流。我们会在群内分享原始研报的完整图表和更多延伸分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本银行股，ROE正在悄悄爬坡\n\n📈 银行股ROE目标上修\n\n某外资投行最新研报指出，日本银行股的中期计划正在释放积极信号。多家大型和中型银行更新了FY3/29（2029年3月期）的中期经营计划，目标净利润年复合增长率在8%-25%之间，显示利润增长动能强劲。\n\n1️⃣ **ROE目标普遍上调**\n- 大型银行ROE目标从以往的10-12%提升至12%以上\n- 部分区域银行目标超过10%（按东证基准）\n- 三菱UFJ金融集团（MUFG）本财年即可实现12%的ROE，中长期瞄准15%水平\n- 三井住友金融集团（SMFG）已公布中长期ROE目标15%\n- Mizuho金融集团将ROE目标从10%以上提升至12%以上\n\n2️⃣ **利润增长的驱动力**\n- 日本国内利率上升带来的存贷利差扩大\n- 企业重组和业务继承等企业活动加速\n- 资本市场活跃\n- 无现金支付普及\n- “从储蓄到投资”的趋势推动资管产品需求\n\n3️⃣ **P/B与ROE的联动逻辑**\n研报分析显示，当前ROE在6-10%的银行股，P/B倍数为0.6-1.5倍。如果ROE按目标提升，沿着同样的P/B-ROE斜率，更高的P/B倍数有望被解锁。比如，中\n\n[... middle omitted ...]\n\n profit growth is supported not only by the tailwind of expanding loan-deposit spreads from rising domestic interest rates, but also by a broad-based demand for financial functions. This deman\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "GS：日本造船业重启LNG船建造，真正的信号是供给侧的“再入场”而非需求爆发",
    "digest": "[wechat_article.md]\n# GS：日本造船业重启LNG船建造，真正的信号是供给侧的“再入场”而非需求爆发\n\n2026年6月15日，日本经济新闻一则报道，在资本市场投下了一颗信号弹：今治造船、川崎重工、名村造船所计划在2035年左右联合重启LNG运输船的建造。对于全球造船业而言，这则消息的价值不在于“日本要造更多船”，而在于一个曾在价格战中主动退出的玩家，正在以新的联盟形式重新入局。\n\nGS第一时间发布了点评。这份报告的核心判断，不是需求端的景气度，而是供给端的结构性变化——日本造船业正在从“被动退出”转向“主动再配置”。这一变化，对投资者理解全球造船产能格局、日本造船企业的中长期盈利能见度，具有框架性的意义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日本造船业的重返，不是扩张，而是“替代性供给”的战略卡位\n\n理解这则新闻，首先要回到一个基本事实：日本造船业在LNG船领域，已经缺席了整整七年。自2019年最后一艘LNG船交付后，日本船厂在与中国和韩国对手的价格竞争中全面撤退。\n\nGS报告明确指出，目前一艘17万立方米级LNG船的单价约为2.5亿美元（按160日元兑1美元汇率计算，约合400亿日元）。在这个价位上，日韩中三方各有优势：韩国在大型化、标准化方面领先；中国在成本控制和规模化方面占据主动；日本则在精密焊接、复杂船型设计上仍有积累。\n\n日本企业此次联合重启，其战略意图不在于争夺全球市场份额，而在于确保“本土能源供应链的自主可控”。报道中提到，目前约有100艘LNG船专门为日本供应液化天然气，按20年替换周期计算，每年需要约5艘新船来维持运力。这意味着，即便没有外部订单，仅日本国内的替换需求，就足以支撑一个每年1200亿至2000亿日元的稳定市场。\n\nGS估算，当前日本造船业（仅限商船）的市场规模约为1.3万亿至1.5万亿日元。\n\n[... middle omitted ...]\n\n业后续的成本数据和订单情况，帮助大家在不确定性中寻找确定性。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本船厂重启LNG船建造\n\n日本造船业回来了\n\nLNG船订单有望稳定释放\n\n日本三大船厂时隔多年，要联手造LNG船了。\n\n根据日经报道，今治造船、川崎重工、名村造船计划在2035年前后，重新启动LNG运输船的建造。这个细分市场，自2019年最后一艘交付后，日本船厂几乎被中韩低价攻势挤出局。\n\n📌 核心信息拆解\n\n1️⃣ 合作模式\n三家共享LNG船设计技术和焊接工人，计划以川崎重工的坂出工厂为生产基地，目标年产3-5艘。\n\n2️⃣ 需求逻辑\n目前日本LNG进口用船约100艘，按20年替换周期，每年5艘刚好覆盖替换需求。日本政府也考虑在2026年6月前出台支持政策，给船东提供补贴。\n\n3️⃣ 经济账\n一艘17万立方米级LNG船单价约2.5亿美元（按160日元/美元，约400亿日元）。年产3-5艘，对应日本造船业年收入增量1200-2000亿日元。对照当前日本商船市场约1.3-1.5万亿日元的规模，这个增量不算小。\n\n📌 对相关公司的影响\n\n名村造船和川崎重工：直接受益，能锁定中长期稳定订单。不过川崎重工的产品组合需要关注利润率影响。\n\n三井E&S：作为国内船用发动机制造商，也会间接受益。\n\n📌 一点思考\n\n这个动\n\n[... middle omitted ...]\n\nhnologies and the welders involved in the construction. The leading proposal is to utilize Kawasaki Heavy Industries' Sakaide Works as the production base. They aim to build three to five vess\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "GS：韩国军工股的情绪拐点可能比想象中更近",
    "digest": "[wechat_article.md]\n# GS：韩国军工股的情绪拐点可能比想象中更近\n\n市场当前对韩国军工股的情绪，或许正处于一个被低估的转折点。过去几个月，韩华航空航天和现代Rotem的股价持续承压，但GS在最新发布的一份研报中明确指出，一个关键催化剂可能正在酝酿——美伊和平协议的前景。这份报告的核心判断是：市场对地缘政治风险的定价已经过度，而一旦和平进程出现实质性进展，被压抑的订单管线将重新成为估值核心驱动力。\n\n这份报告的价值不在于简单地给出“买入”评级，而在于它提供了一个清晰的传导链条：和平预期如何转化为订单落地，订单落地又如何重塑两家公司的盈利增长曲线。对于关注全球国防供应链和地缘政治套利的投资者来说，这可能是2026年下半年最具不对称回报潜力的主题之一。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场情绪的“冰点”恰恰是反转的起点\n\n要理解GS的逻辑，首先要看清过去几个月发生了什么。韩华航空航天和现代Rotem的股价自4月高点以来持续下滑，尽管期间有零星订单消息（如爱沙尼亚Chunmoo交易、挪威Chunmoo交易等），但整体市场情绪始终不振。GS将其归因于中东地区紧张局势的持续发酵——只要冲突没有明确降温信号，潜在订单的讨论就被搁置，催化剂自然匮乏。\n\n但6月11日，美伊可能达成和平协议的媒体报道引发了两只股票单日分别上涨6.3%和10.7%，大幅跑赢Kospi指数。这一价格行为表明，市场并非不认可这两家公司的基本面价值，而是在等待一个“开关”——一个能把潜在订单从“可能”变为“确定”的触发条件。\n\nGS的推断非常直接：任何朝向和平的进展，都会让市场逐步将订单管线重新定价进股价。这本质上是一种“情绪均值回归”的逻辑——当悲观预期已经充分反映在价格中，任何超预期的正面信号都会带来显著的估值修复。\n\n![研报原图 2](assets/s\n\n[... middle omitted ...]\n\n定期分享对全球国防供应链、地缘政治套利和估值模型的深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国军工股跌够了？关键信号出现\n\n📉 情绪低谷，拐点隐现\n\n上周五韩华航空航天涨6.3%、现代Rotem涨10.7%，双双跑赢Kospi。过去几个月这两家股价持续下滑，但最新消息可能是个转折点。\n\n1️⃣ 为什么之前跌？\n中东地区长期紧张局势导致潜在订单谈判搁置，加上一季报后缺乏催化剂，市场情绪一直低迷。\n\n2️⃣ 周五为什么涨？\n媒体报道美伊可能达成和平协议。对这两家公司来说，和平进展是推进大单的关键催化剂。\n\n3️⃣ 订单潜力有多大？\n按100%胜率估算：\n- 韩华：潜在订单95.5万亿韩元\n- Rotem：潜在订单89.5万亿韩元\n这意味着2025-2028年EPS年复合增长率可达32%和48%。\n\n4️⃣ 后续怎么看？\n任何和平进展都可能让市场重新定价这些订单预期。目前股价已从4月高点回落不少，情绪面有修复空间。\n\n研报未给出具体时间表，但逻辑清晰：地缘缓和→订单重启→业绩兑现。\n\n#学习笔记\n\n[source_mineru.md]\n# South Korea Aerospace & Defense: Potential inflection point in beaten down sentimen\n\n[... middle omitted ...]\n\n lackluster market sentiment to the prolonged tensions in the region, which put discussions on the potential order pipelines on hold and left limited sector catalysts post 1Q results (Exhibit \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "Bernstein：半导体设备正在重演涨价逻辑，市场尚未充分定价",
    "digest": "[wechat_article.md]\n# Bernstein：半导体设备正在重演涨价逻辑，市场尚未充分定价\n\n半导体设备板块近期跑输了存储、模拟等大宗芯片，原因很直接——后者正享受涨价周期的红利。但Bernstein这份最新研报提供了一个值得关注的信号：设备公司可能正在进入自己的涨价窗口，而市场对这一变化的定价远未充分。\n\n过去两个月，以Ibiden、Sumco、Renesas为代表的非设备类半导体公司涨幅显著跑赢设备板块。Bernstein用一张图表清晰展示了这一分化：非设备类平均上涨约74%，而设备类平均仅上涨约30%。传统逻辑认为，设备是“卖铲子”的生意，需求弹性滞后于芯片涨价。但这份报告的核心判断是：这种滞后本身正在成为新的催化剂——大宗芯片涨价必然推动资本开支扩张，而资本开支扩张最终会反馈到设备订单；更重要的是，设备公司自身也在酝酿价格调整。\n\nBernstein观察到，日本设备企业多数以日元定价，而过去三年日元对美元贬值约30%。在正常商业逻辑下，这已经构成了充分的提价理由。但日本设备企业过去一直缺乏提价意愿。变化正在发生——东京电子和Screen近期的管理层表态暗示战略转向，而市场消息显示SK海力士已经收到了3-4%的涨价要求。\n\n这不仅仅是一次汇兑损益的修复，而是设备行业定价权的结构性重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 东京电子的定价策略正在从“被动接受”转向“主动管理”\n\n东京电子将利润率改善列为最高优先级，并提出了一个清晰的三个阶段提价路径。第一阶段是紧急交付加价——客户经常提出加急订单，但东京电子过去并未因此额外收费，现在开始对此收取溢价。第二阶段是与客户谈判通胀、材料、劳动力成本上涨的附加费。第三阶段是在新机型发布时，基于技术进步、功能增加、新材料应用等理由，系统性地提高定价。\n\n这三步走战略的核心含义是：东\n\n[... middle omitted ...]\n\n群内会定期分享原始研报、估值模型以及我们对产业链的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体设备涨价信号已出现\n\n半导体设备，要涨价了\n\n日系设备厂开始调整定价策略\n\n最近看到某外资投行一份研报，聊到半导体设备行业可能迎来涨价周期。逻辑很清晰，分享给大家。\n\n1️⃣ 为什么现在关注设备涨价？\n之前半导体设备股跑输其他科技板块（如存储、模拟芯片），因为后者有涨价故事。但研报认为风向在变：\n- 其他科技股涨 → 资本开支增加 → 设备需求提升\n- 设备公司本身也能涨价，尤其在需求高或产能紧张时\n\n2️⃣ 日系设备厂最有机会\n日本设备商多以日元定价，过去3年日元对美元贬值约30%。按理说早该涨价，但之前意愿不强。最近Tokyo Electron和Screen的公开表态显示策略可能转变。有消息称SK海力士已收到3-4%的涨价要求。\n\n3️⃣ 具体怎么涨？\nTokyo Electron的涨价三步走：\n- 短期：客户催货可收加急费（以前不收）\n- 中期：谈判通胀、原材料、人工成本附加费\n- 长期：新机型上市时，凭技术升级谈更高价\n目标：毛利率从目前水平升至50%+，营业利润率接近35%（市场预期FY29/3才到48%毛利率和30%利润率）\n\nScreen类似：先谈通胀相关涨价（已获接受），再谈新机型附加价\n\n[... middle omitted ...]\n\nJack Lin\n\n+852 2123 2683\n\njack.lin@bernsteinsg.com\n\nSemi equipment can potentially outperform again. Semi equipment companies have been underperforming commodity tech (memory, analog, wafer, s\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R019",
    "title": "JPM：软件估值分化背后，是市场对“利润质量”的重新定价",
    "digest": "[wechat_article.md]\n# JPM：软件估值分化背后，是市场对“利润质量”的重新定价\n\n这份由JPM软件研究团队在2026年6月发布的《Software Landscape Benchmarking》报告，表面上是例行估值对比，但如果我们仔细拆解其数据结构和行业覆盖，会发现一个更值得关注的信号：软件市场的估值分化正在从“增长溢价”转向“利润质量溢价”，而安全软件板块正处于这一分化的最前沿。\n\n报告覆盖了101家软件公司，从Crowdstrike到Elastic，从Palo Alto Networks到Zscaler，涵盖了从大型股到小型股、从安全软件到垂直软件的完整谱系。但真正有价值的，不是这些数字本身，而是数字背后透露出的行业结构性变化。\n\n本文尝试从五个层次拆解这份报告的隐含判断，以及这些判断对产业决策者和投资者的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 安全软件板块的估值溢价并非来自增长更快，而是来自利润更稳定\n\n报告数据显示，安全与分析软件板块（Security & Analytics）的EV/Sales倍数在CY26E为9.2x，远高于全行业平均的5.7x，也高于垂直软件的4.7x。但如果只看收入增长，安全软件板块的CY26E增速为17%，仅略高于全行业平均的17%和垂直软件的16%。\n\n这意味着安全软件的高估值，不能简单地用“增长更快”来解释。更关键的是利润质量的差异。\n\n安全软件板块的毛利率为80%，高于全行业平均的76%和垂直软件的72%。在FCF利润率方面，安全软件为15%，低于全行业平均的20%，但这主要是由于该板块SBC（股权激励）占收入比重高达15%，远超垂直软件的9%和全行业平均的13%。\n\n换句话说，安全软件公司正在用更激进的股权激励来换取更优质的客户留存和更可预测的经常性收入。市场愿意为这种“高\n\n[... middle omitted ...]\n\n告的拆解和研讨，帮助大家从数据中提炼出真正有操作价值的洞察。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n软件赛道最新估值画像：安全板块溢价明显\n\n**安全板块估值全景**\n\n**大型股平均EV/Sales高达10.3x，安全分析子板块9.2x**\n\n刚看完某外资投行6月出的软件行业估值全景图，数据到6月12日，覆盖101家软件公司。几个有意思的点分享：\n\n**1/ 不同市值区间估值分化严重**\n- 大型股（市值>200亿）平均EV/Sales：10.3x\n- 中型股（30-200亿）：5.0x\n- 小盘股（<30亿）：1.9x\n大市值公司享受明显溢价，但增速也更高（24% vs 7%）。\n\n**2/ 安全分析板块估值突出**\n安全分析子板块EV/Sales 9.2x，远高于垂直软件4.7x。EV/EBITDA 23.7x，毛利率80%，但FCF利润率只有15%，SBC占收入15%——烧钱换增长的特征明显。\n\n**3/ 增速分组看估值逻辑**\n- 高增长组（>20% y/y）：EV/Sales 13.7x，营收增长39%\n- 中速组（10-19%）：7.0x，增长16%\n- 低速组（<10%）：4.3x，增长7%\n高增长组FCF利润率仅6%，但市场愿意给溢价。\n\n**4/ 安全软件个股差异大**\nCrowdstr\n\n[... middle omitted ...]\n\nesearch report, although it may refer to information and data contained in JPM published research reports or models from all JPM affiliated regions. Opinions and estimates constitute our judgm\n\n[... middle omitted ...]\n\nC\n\nalexei.gogolev@jpmchase.com\n\n(1-212) 622-9391\n\nElla Smith\n\nella.smith@jpmchase.com\n\n(1-212) 622-2451\n\nDestiny Jackson\n\ndestiny.jackson@JPM.com\n\n(1-212) 622-4360\n\nIsabella A Camaj\n\nbella.camaj@JPM.com\n\n(1-212) 834-2379"
  },
  {
    "id": "R020",
    "title": "摩根斯坦利：笔记本出货量真正的拐点不在需求，而在组件供应的结构性错配",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：笔记本出货量真正的拐点不在需求，而在组件供应的结构性错配\n\n这份报告的核心判断，与市场主流叙事存在根本性分歧。\n\n当我们看到“5月出货量低于预期7%”、“二季度环比零增长”、“三季度环比下降1%”这些数字时，最直接的反应是“需求不行”。但摩根斯坦利的分析师给出了一个反直觉的解读：真正的瓶颈不是需求，而是组件供应。这不仅仅是短期扰动，而是一种正在重塑整个PC供应链竞争格局的结构性力量。\n\n报告揭示了一个关键机制：当组件供应受限时，ODM和OEM会优先将稀缺的零部件分配给高端机型，以获取更高利润。这意味着，总量数据的疲软掩盖了产品结构的剧烈分化。高端市场可能正在经历供应驱动的增长，而中低端市场则被主动收缩。这种“选择性出货”策略，正在改变我们对行业景气度的判断框架。\n\n这份报告的价值，不在于它预测了出货量数字，而在于它提供了一个理解当前PC供应链“非典型周期”的分析框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月出货量低于预期，但核心矛盾是组件约束而非需求疲软\n\n5月前五大ODM笔记本出货量为930万台，环比增长2%，但同比下降12%，且低于摩根斯坦利预期7%。从表面看，这组数据足以让市场担忧需求前景。但报告明确指出，元凶是“component constraints remain the key bottlenecks”——组件约束是核心瓶颈。\n\n这是一个有分量的判断。它意味着，如果组件供应恢复正常，实际出货量可能高于当前数字。这不是需求不足导致的被动减产，而是供应链瓶颈导致的主动选择。\n\n更值得关注的是ODM的行为模式：它们被迫将有限的组件优先用于高端、高利润率的机型。这意味着，即使总量数据难看，高端产品的出货占比和利润率可能都在提升。这解释了为什么一些ODM公司的股价表现与出货量数据出\n\n[... middle omitted ...]\n\n后的隐含假设是什么？AI PC是否会改变当前的供应分配逻辑？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月笔记本出货：低于预期7%\n\n出货不如预期，但结构在变好\n\n某外资投行最新研报跟踪了前5大ODM的笔记本出货数据，5月实际出货930万台，比他们预估的低了7%。核心原因还是**零组件供应紧张**，厂商只能优先把有限的料给高端机型。\n\n几个关键数据拆解一下：\n\n1️⃣ **5月实际出货**：930万台（环比+2%，同比-12%），低于预期\n2️⃣ **6月预估**：1090万台（环比+17%，同比-16%），季末拉货效应\n3️⃣ **Q2整体**：下调至2930万台（环比持平，同比-12%），比15年季节均值低12个百分点\n\n**下半年的两个关注点**：\n\n🔸 **需求端保持谨慎**：虽然具体时点难预测，但研报对下半年需求持保守态度\n🔸 **产品结构持续上移**：PC厂商会把有限零组件优先给高端机型，追求更高利润\n\n研报还给出了Q3的初步预估：2900万台（环比-1%，同比-15%），明显低于过去15年Q3平均5%的环比增速。\n\n目前最大的变量还是**零组件供应**，实际出货会持续取决于这个瓶颈的缓解程度。欢迎一起讨论后续走势。\n\n#学习笔记\n\n[source_mineru.md]\n## Greater Ch\n\n[... middle omitted ...]\n\nlenecks, forcing ODMs to prioritize higher-end, more profitable models. We forecast June NB builds at 10.9m (+17% q/q, -16% y/y) due to quarter-end pull-ins.\n\nWe lower our 2Q notebook build es\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "摩根斯坦利：苹果真正的拐点不在销量，而在产品结构的定价权迁移",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：苹果真正的拐点不在销量，而在产品结构的定价权迁移\n\n市场对苹果供应链的讨论，长期陷入一个误区：把注意力集中在iPhone总出货量的季度波动上。这份摩根斯坦利最新发布的月度数据手册，给出了一组看似平淡的数字——2Q26 iPhone build estimate维持在5200万部，3Q26初步预估为5400万部——但真正值得关注的，不是这些数字本身，而是数字背后的结构性变化。\n\n这家投行的核心判断是：iPhone的出货节奏正在打破历史规律，而这种打破，恰恰是苹果产品战略从“量”向“价”转型的实证。2Q26环比仅下降7%，远低于历史上15%-25%的季度性回撤。摩根斯坦利将其归因于“memory cost hikes背景下iPhone sell-through持续走好”。但如果我们把这句话翻译成更直白的商业语言，那就是：在成本上升的环境下，苹果不仅没有丢失需求，反而通过产品结构调整，正在把成本压力转化为定价权的强化。\n\n这份报告真正值得深读的信号，不是5200万或5400万这个数字，而是这些数字背后隐藏的供给侧逻辑：iPhone Fold的加入、Pro系列占比的持续提升、以及iPad在材料涨价背景下的平稳备货。这些信号叠加在一起，指向一个结论——市场正在低估苹果通过产品结构升级来重塑利润池的能力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度iPhone备货的“反季节性”才是关键信号，而非绝对数字\n\n摩根斯坦利维持2Q26 iPhone build estimate在5200万部，环比下降7%，同比增长12%。单独看这个数字，似乎只是例行更新。但真正有信息量的，是报告中提到的一个对比维度：历史上二季度iPhone备货的环比降幅通常在15%-25%之间，而这一次仅下降了7%。\n\n报告给出的解释是\n\n[... middle omitted ...]\n\n解苹果供应链的每一个关键变量，并持续跟踪这些未解问题的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\niPhone 折叠屏要来了？产能排期已出\n\n📱 折叠屏蓄力\n\niPhone 备货淡季不淡，折叠机明年见\n\n最近看到一份某外资投行的研报，聊了聊iPhone和iPad的产能排期，信息量挺大，直接说重点👇\n\n1️⃣ iPhone 2Q26 备货超预期\n- 2Q26 预估产量 5200 万台，环比只跌 7%（往年同期跌 15-25%）\n- 原因是内存涨价背景下，终端销售依然不错\n- 主力代工厂鸿海 5 月出货环比还在涨\n\n2️⃣ 3Q26 新机布局：折叠屏来了\n- 3Q26 产量预估 5400 万台，环比微增 4%\n- 新机型全面转向高端：18 Pro/Pro Max + iPhone Fold\n- 折叠屏预计 2H26 生产 700-800 万台\n- 普通版 iPhone 18 要到 1H27 才亮相\n\n3️⃣ iPad 稳中微降\n- 2Q26 产量 1300 万台，同比跌 10%（去年基数高）\n- 3Q26 预估持平，但内存和材料涨价可能影响后续\n\n一句话总结：iPhone 淡季不淡，折叠屏是明年重头戏，iPad 短期承压但库存正常。\n\n欢迎研究消费电子供应链的朋友一起聊聊～\n\n#学习笔记\n\n[source_m\n\n[... middle omitted ...]\n\ns suggest better-than-seasonal builds this quarter from major assembly partners including Hon Hai, with iPhone shipments in May up MoM. This indicates to us that iPhone sell-through continues \n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Hybe has a clear strategic positioning and execution capability to scale in Western markets. \\- The K-pop training system and processes will be implemented in local markets to incubate new artists, enhancing localizati"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Hybe has a clear strategic positioning and execution capability to scale in Western markets. \\- The K-pop training system and processes will be implemented in local markets to incubate new artists, enhancing localizati"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: K-pop is the most promising subsector within Korea's internet industry, driven by the global expansion of K-pop artists' large-scale international tours."
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: The rise of K-pop IPs into global franchises has laid the groundwork for the genre's penetration into mainstream global audiences. Axis Y: Youtube Viewership (Billion times)"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Time series of K-pop industry revenue by segment highlighting concerts as an increasing share of total revenue, which we view as evidence of a shift in consumer IP consumption behavior."
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Highlight the post-2022 inflection as global touring resumes, with concert revenue growth outpacing album and digital segments, reflecting a rapidly expanding K-pop fandom."
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: K-pop concert revenue has shown strong compounding growth over time, and we see incremental opportunities for IP monetization through an increasingly engaged “super fan”."
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: K-pop is rapidly gaining share in the global Top 100 touring circuit, with its tour revenue footprint now approaching \\~10% of global."
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Hybe commands c.70% of K-pop concert revenue, dwarfing peers in scale and positioning itself within a structurally expanding global live market."
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: BTS sits at the top tier globally in concert ticket pricing. 2022: Average ticket price"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Spending is shifting from goods to experiences, with fandom ARPU from concerts rising meaningfully above physical albums. 2015 vs 2025: ARPU by revenue stream"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: In a debased currency world, premium IP commands real pricing power."
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Artist time is scarce and valuable - the key is fully monetizing every minute."
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Concerts are emerging as the primary growth engine, as scaled IP portfolios enable K-pop companies to fill global venues."
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Concert margins may be thin, but bundled merch turns global tours into a meaningful profit pool."
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Hybe's concert revenue scale sets it apart, aligning its model with global live promoters rather than traditional labels."
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Hybe is ramping concert cadence on the back of a broad, multi-tiered IP portfolio."
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Concert GP margins are lower (c.25%), but pairing with high-margin merch (c.50%) lifts blended gross margins."
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Hybe's global tour unit economics stand apart, with lower local promoter take rates (\\~10% vs. 20-30%+ for other labels), resulting in structurally higher margins. Top tier IP tour unit economics"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: We like Hybe, as consistent mid-sized successes have built a diversified IP portfolio."
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Human scarcity wins - AI scales reach, but artist time drives K-pop value. Nature of business comparison in Entertainment space \"You can do multiple games, but fandom is only for 1 artist\" Music is one surface in a broad"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Human scarcity wins - AI scales reach, but artist time drives K-pop value. Nature of business comparison in Entertainment space \"You can do multiple games, but fandom is only for 1 artist\" Music is one surface in a broad"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "Exhibit 24",
    "context": "EXHIBIT 24: On a like-for-like arena and stadium basis K-pop concertgoers behave like superfans, filling 96% of capacity versus 86% for all shows... Avg. Capacity sold at like-for-like venues (2025)"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: ...and paying about 27% more per ticket (\\$132 versus \\$104) Avg. USD Ticket Price at like-for-like venues (2025)"
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "Exhibit 26",
    "context": "EXHIBIT 26: The US is the single largest K-pop touring market in the world and Live Nation promoted about 60% of it in 2025, with Live Nation also dominant across the other Western markets (Mexico \\~81%, Netherlands \\~71%, UK \\~68%)"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Figure 1",
    "context": "Figure 1 - TSF quick read Figure 2 - Household deposit vs household debt"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "Figure 3 - All new deposits breakdown by savers Figure 4 - China credit impulse"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "Figure 3 - All new deposits breakdown by savers Figure 4 - China credit impulse China's credit impulse (3-m TSF change % quarterly GDP)"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Figure 5",
    "context": "Figure 5 - RatingDog PMI vs Official PMI"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The Recent Pick-Up in Job Growth Has Provided Reassurance About the Labor Market Outlook"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The Combined Effect of Increases in Tariffs, Oil Prices, and Computer Memory Prices Is Likely to Hold Roughly Steady and Keep Year-over-Year Core PCE Inflation Above $3\\%$ All Year but Should Fade in 2027"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We See Rate Hikes as Unlikely Because the Fed Tends Not to Hike in Response to Oil Shocks and Because the Oil Shock Is Less Likely to Spark Self-Sustaining High Inflation in a More Balanced Labor Market Correlation Bet"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Concerning Signals from Inflation Expectations or the Breadth of High Inflation Across Categories Would Make Hikes More Likely"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Expect the Median Dot to Show No Change in 2026 and One Cut in Each of 2027 and 2028"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Our Baseline Fed Forecast Calls for Two Final Cuts in June and December 2027; Our Probability-Weighted Fed Forecast Remains More Dovish Than Market Pricing, Reflecting Our Skepticism of Hikes"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Solar plus storage (12+ hours) are competitive against gas-fired power at high gas prices"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: We estimate total project capex at approximately \\$6bn (or \\~\\$6,000/kW). Energy storage dominates the economics Project cost ($bn) for 5.2GW solar + 19GWh storage = 1GW baseload power"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "EXHIBIT 4",
    "context": "Assuming a build for 1GW of baseload power ## SOLAR-PLUS-STORAGE PROVIDES BASELOAD POWER EWEC Enagas Water & Electricity Co. J20D MASDAR"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Annual power output of the project (TWh). Solar and storage overbuilt enables continuous 1 GW output"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: We have modeled 5.2GW of solar capacity. The solar farm can achieve an average capacity factor of 27% although we have not factored in curtailment and power load"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Solar power is mostly generated between 7am to 5pm, which means there is no power for more than 12 hours of the day without storage or other power"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Annually, the project could generate 12.45TWh of electricity, although this is interruptible"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: While the solar project can theoretically achieve 27% capacity factor, realistically utilization is lower due to curtailment during midday without storage"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Without storage, the curtailment results in capacity factor falling to 9%"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: 1GW of continuous power output enabled by the project"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: System sustains \\~1 GW of near-continuous output throughout the year"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Based on our modelling, this configuration (19 hours) can achieve \\~99.7% uptime, effectively delivering baseload-like reliability"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Solar ASP are at decade low which makes economics attractive"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: ESS costs have also continued to decline in recent years"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: We estimate total project capex at approximately \\$6bn (or \\~\\$6,000/kW). Energy storage dominates the economics Project cost (\\$bn) for 5.2GW solar + 19GWh storage = 1GW baseload power"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Solar plus storage (12+ hours) are competitive against gas-fired power at high gas prices"
  },
  {
    "figure_id": "F052",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Significant jump in Jun (US\\$11.1bn; +30% MoM); around 3x higher than 2025-average Korea semis exports – First 10 days of month US\\$bn"
  },
  {
    "figure_id": "F053",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China monthly integrated circuit (IC) imports and YoY IC imports reached a record high at US\\$56.6bn in May, +68% YoY"
  },
  {
    "figure_id": "F054",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Solid MoM growth led by memory names – ADATA +23%, Phison +13%, Nanya Tech +9% Taiwan tech companies' MoM monthly sales (May 2026)"
  },
  {
    "figure_id": "F055",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 3: YoY rebound accelerated to +206% in Jun; already five consecutive months of triple-digit growth Korea semis exports – First 10 days of month YoY growth"
  },
  {
    "figure_id": "F056",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 5: China monthly integrated circuit (IC) imports volume and YoY China IC imports reached 49.7bn units in May, -1% YoY"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Positive YoY growth across all companies; notably strong rebound seen – Nanya +730%, Phison +301%, Quanta +94%, TSMC +30% Taiwan tech companies' YoY monthly sales (May 2026)"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Our memory indicator reached an all-time high of 189 in Mar/Apr-26, driven by exceptionally strong DRAM/NAND spot pricing, rising ASPs and billings, along with Korea's $150\\%+$ export growth. BofA Memory Indicator – back"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 9: May share price surged to record highs, supported by Samsung (strong 1Q results, optimism around HBM4 upside, and higher exposure to conventional DRAM), SK Hynix (solid 1Q performance and leadership in HBM3e/4), and Nany"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Exceptionally strong DRAM/NAND spot pricing persisted through Apr–May, with DRAM ASPs and billings also rising sharply in April, while semiconductor exports remained robust, reaching record highs in May Seven components"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "Exhibit 12",
    "context": "Exhibit 12: DRAM/NAND spot prices stabilized in Apr–May following a sharp rally in 4Q25/1Q26; however, semiconductor exports rebounded strongly MoM in May, while DRAM/NAND ASPs remained elevated in Apr even as billings showed some m"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "Exhibit 13",
    "context": "Exhibit 13: DRAM spot prices rebounded in 1H- June after softening through April–May, following a strong rally from September 2025 to January 2026. Prices have reached multi-decade highs, with 16Gb DDR5 at \\~\\$45 and DDR4 at \\~\\$65,"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Exhibit 14",
    "context": "Exhibit 14: DRAM spot and contract prices reached record highs (\\$35-40), then leveled off during April–May following a strong rally in 4Q25 and 1Q26. DRAM spot and contract price - quarterly average trend"
  },
  {
    "figure_id": "F064",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 15: NAND wafer contract prices have surged significantly ahead of spot prices, with both now at record-high levels NAND wafer spot and contract price - quarterly average trend"
  },
  {
    "figure_id": "F065",
    "report_id": "R006",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Prices rebounded through May/1H-June, reaching an all-time high (\\$45) following a volatile April. Uptrend was driven by strong gains in Oct (+70%), Nov (+60%), Jan (+25%), before moderating into a more subdued trend dur"
  },
  {
    "figure_id": "F066",
    "report_id": "R006",
    "label": "Exhibit 18",
    "context": "Exhibit 18: 8Gb DDR4 prices rose sharply in 1H-Jun and throughout May after stabilizing in April; they remain significantly higher YoY due to supply cuts by major vendors, currently around \\$30—well above the prior \\~\\$10 peak in Oc"
  },
  {
    "figure_id": "F067",
    "report_id": "R006",
    "label": "Exhibit 20",
    "context": "Exhibit 20: DDR4 and DDR5 (16Gb) contract prices are similar at US\\$35-\\$40 levels – DDR5 price premium no longer exists due to DDR4 shortage 16Gb DDR5 vs 16Gb DDR4 contract price trend, Jan '23-May '26"
  },
  {
    "figure_id": "F068",
    "report_id": "R006",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Modest uptick observed in May/1H-Jun (+6-7%), following a sequential slowdown from Feb (+10%) to flat momentum in Mar and a minor decline in Apr, after the strong Jan (+25%) surge and the sharp Oct–Nov-25 rally (+60–120%"
  },
  {
    "figure_id": "F069",
    "report_id": "R006",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Prices edged up slightly in late May/1H-June after a \\~25% correction from April to mid-May, having peaked near \\~\\$80 in early March. Despite this pullback, prices remain elevated—up \\~2000% from \\~\\$3 in October 2025—s"
  },
  {
    "figure_id": "F070",
    "report_id": "R006",
    "label": "Exhibit 21",
    "context": "BofA GLOBAL RESEARCH 16Gb DDR5 vs 16Gb DDR4 contract price change - MoM, Jan '23-May '26"
  },
  {
    "figure_id": "F071",
    "report_id": "R006",
    "label": "Exhibit 22",
    "context": "BofA GLOBAL RESEARCH 512Gb NAND wafer spot price – weekly, Mar '21 - Jun '26"
  },
  {
    "figure_id": "F072",
    "report_id": "R006",
    "label": "Exhibit 24",
    "context": "BofA GLOBAL RESEARCH NAND wafer contract price trend, Jul '23-May '26"
  },
  {
    "figure_id": "F073",
    "report_id": "R006",
    "label": "Exhibit 26",
    "context": "Exhibit 26: 16Gb DDR5 spot and contract prices are in the range of US\\$35-40 vs historical range of US\\$3-5 16Gb DDR5 spot vs contract price trend (US\\$), Jul '23-May '26"
  },
  {
    "figure_id": "F074",
    "report_id": "R006",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Flat in 1H-June, while slightly corrected in Apr/May vs up +15-20% in Feb/ Mar-26 and up +40-70% MoM in Oct/Nov/Dec/Jan 512Gb NAND wafer spot average – MoM change, Jun'21 - Jun'26"
  },
  {
    "figure_id": "F075",
    "report_id": "R006",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Apr/May price only up +3-5% MoM each following Jan/Feb/Mar-26 rally (up 20-30% MoM) and Oct/Nov/Dec upturn (up 40-60% MoM) MoM change of NAND contract price (512Gb wafer), Jul '23-May '26"
  },
  {
    "figure_id": "F076",
    "report_id": "R006",
    "label": "Exhibit 27",
    "context": "Exhibit 27: May'26 spot/contract prices turned positive again after April's divergence (spot dip vs contract surge), prices had witnessed a sharp Oct–Dec'25 rally and subsequent Feb–Mar moderation 16Gb DDR5 spot vs contract price tr"
  },
  {
    "figure_id": "F077",
    "report_id": "R006",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Current NAND spot and contract prices are a few times higher than 2025 summer level 512Gb NAND wafer spot vs contract price trend (US\\$), May '19 - May '26"
  },
  {
    "figure_id": "F078",
    "report_id": "R006",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Current price of 64GB DDR4/DDR5 modules hit all-time high of more than \\$1,000 level (DDR5: US\\$1,200, DDR4: US\\$1,100) Server DRAM contract price trend – DDR5 vs DDR4 modules, Jan '24-May '26"
  },
  {
    "figure_id": "F079",
    "report_id": "R006",
    "label": "Exhibit 32",
    "context": "Exhibit 32: 2H-May SSD price declined after a sharp surge in 1Q26 and April (per DRAMeXchange), prices followed a gradual upward trend throughout 2025 Client SSD price trend – mostly for PC (not server), Mar '24 - May '26"
  },
  {
    "figure_id": "F080",
    "report_id": "R006",
    "label": "Exhibit 29",
    "context": "Note: SSD prices are as of 30 May 2026, reported by DRAMeXchange. TB = terabyte. BofA GLOBAL RESEARCH 512Gb NAND spot vs contract price trend – MoM change, May '19 - May '26"
  },
  {
    "figure_id": "F081",
    "report_id": "R006",
    "label": "Exhibit 31",
    "context": "BofA GLOBAL RESEARCH MoM change of server DRAM contract prices, Jan '24-May '26"
  },
  {
    "figure_id": "F082",
    "report_id": "R006",
    "label": "Exhibit 33",
    "context": "Exhibit 33: May prices have doubled compared to end-2025 levels, while the 2025 increase was more modest at around 35–40% Client SSD (for PC) price comparison – current vs. end-2025"
  },
  {
    "figure_id": "F083",
    "report_id": "R006",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Prices remained volatile this week amid global uncertainty, but remain broadly higher year-to-date, led by NAND and HDD players and supported by strength in DRAM, primarily driven by robust AI-related demand Memory compa"
  },
  {
    "figure_id": "F084",
    "report_id": "R006",
    "label": "Exhibit 36",
    "context": "Exhibit 36: CPU names such as Intel and AMD clearly outperforming other US big tech names such as NVIDIA/Apple/QCOM Global major tech companies – 2026 YTD stock performance comparison"
  },
  {
    "figure_id": "F085",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: India's oil intensity has declined over the last three decades Oil consumption intensity (Tonnes/INR mn)"
  },
  {
    "figure_id": "F086",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: India's net crude oil import volumes have become more elastic (vs. the pre-pandemic period)"
  },
  {
    "figure_id": "F087",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Domestic fuel price hikes likely to weigh on fuel consumption demand going forward"
  },
  {
    "figure_id": "F088",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Gold import volumes typically weaken within 1-2 months of duty hikes, with the full impact materializing over 5-6 months"
  },
  {
    "figure_id": "F089",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Current account balance came in at a surplus (vs. our expectation of a deficit) mainly on lower oil imports and higher remittance receipts India Q1 CY26 current account deficit change (GSe vs. actual)"
  },
  {
    "figure_id": "F090",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We expect current account deficit to average around $1.3\\%$ of GDP in CY26 and $1.7\\%$ of GDP in FY27"
  },
  {
    "figure_id": "F091",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Overall, we estimate around \\$40-80bn of inflows from the various measures announced by the RBI, with our baseline of around \\$60bn in CY26"
  },
  {
    "figure_id": "F092",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 8: The FCNR (B) scheme and the concessional swap facility for offshore borrowings by quasi-sovereigns will result in further increase in the RBI's net short dollar forward book"
  },
  {
    "figure_id": "F093",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 10: FPI debt inflows have been closely associated with India - US 10Y yield differentials"
  },
  {
    "figure_id": "F094",
    "report_id": "R009",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Fund-raising activity recovered in 2025 and we expect it to further normalize to historical averages in 2026"
  },
  {
    "figure_id": "F095",
    "report_id": "R009",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Cornerstone investors contributed around 40% of capital raised by HK IPOs"
  },
  {
    "figure_id": "F096",
    "report_id": "R009",
    "label": "Exhibit 5",
    "context": "Exhibit 5: IT, Industrials, and Consumer Discretionary are the top 3 sectors that raised the most capital in HK Capital raised by HK IPOs since 2025 (Total = HK$452bn)"
  },
  {
    "figure_id": "F097",
    "report_id": "R009",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Investors participating in IPOs over the past two years could have achieved approximately 50% returns on average in the first month Average post-IPO returns (in absolute terms for all HK Main Board IPOs)"
  },
  {
    "figure_id": "F098",
    "report_id": "R009",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The offer-to-demand ratio for HK IPOs this year dropped to a historical low, which indicates strong retail investor demand HK IPO offer-to-demand ratio^"
  },
  {
    "figure_id": "F099",
    "report_id": "R009",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Biotech and AI companies tend to have stronger post-IPO performance Post-IPO performance"
  },
  {
    "figure_id": "F100",
    "report_id": "R009",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Companies where cornerstone investors acquire 30-50% of shares generally demonstrate stronger post-IPO performance 3-month returns after IPO (relative to HSCI)"
  },
  {
    "figure_id": "F101",
    "report_id": "R009",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Despite higher valuations, newly listed companies with significant growth potential tend to perform better after their IPOs"
  },
  {
    "figure_id": "F102",
    "report_id": "R009",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Large caps with standalone listings in Hong Kong and high over-subscription ratios tend to generate superior post-IPO returns Factors driving post-IPO relative returns of HK new listings since Sep 2024"
  },
  {
    "figure_id": "F103",
    "report_id": "R009",
    "label": "Exhibit 10",
    "context": "Exhibit 10: US\\$274bn of lock-up shares are expected to release to the HK markets in coming 12 months"
  },
  {
    "figure_id": "F104",
    "report_id": "R009",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Equities typically experience moderate downward price pressure following lock-up expirations Returns of stocks listed in HK since 2025"
  },
  {
    "figure_id": "F105",
    "report_id": "R009",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The percentage of shares released serves as the primary determinant of the first week post-expiration returns, while the post-release free float ratio and the stock's pre-expiration post-IPO performance are the key drive"
  },
  {
    "figure_id": "F106",
    "report_id": "R009",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Primary Hong Kong listings that satisfy specific market capitalization and liquidity requirements can be added into Southbound universe Exhibit 14: Additions/deletions in HSI and HSTECH experienced stronger price actions"
  },
  {
    "figure_id": "F107",
    "report_id": "R009",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Newly-listed stocks tend to have a short-lived rally after Southbound inclusion, while inflows tend to persist"
  },
  {
    "figure_id": "F108",
    "report_id": "R010",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Aptamil maintained its No.1 position with market share loss 0.9ppt mom to 20%; A2 lost 2.7ppt market share in May International IMF value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F109",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Feihe/Yili's Market share on Tmall/Taobao was $14\\% / 9\\%$ in May Domestic IMF value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F110",
    "report_id": "R010",
    "label": "Exhibit 5",
    "context": "Exhibit 5: ByHealth's Market share recorded $3.8\\%$ in May (0.8ppt gain vs. Apr) Supplements value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F111",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Fund flow data show a strong correlation with China stocks Monthly capital flows to foreign-domiciled China funds (USD bn) vs. MSCI China and CSI 300 indices"
  },
  {
    "figure_id": "F112",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Stock selling by China's \"national team\" continues Cumulative capital flows to China's domestic ETF funds (USD bn)"
  },
  {
    "figure_id": "F113",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: SSE new account opening +11% MoM in May New account openings at the Shanghai Stock Exchange ('000)"
  },
  {
    "figure_id": "F114",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 6: EM funds' exposure to South Korea and Taiwan stocks soar Market allocations by active global EM funds (%)"
  },
  {
    "figure_id": "F115",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Active funds reduce their UW positions on China Active and passive global EM funds' exposure to China stocks $(\\%)$"
  },
  {
    "figure_id": "F116",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Active funds reduce their UW positions on Taiwan Active and passive global EM funds' exposure to Taiwan stocks (%)"
  },
  {
    "figure_id": "F117",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Active funds increase their OW positions on South Korea"
  },
  {
    "figure_id": "F118",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Active funds increase their UW positions on India Active and passive global EM funds' exposure to India stocks (%)"
  },
  {
    "figure_id": "F119",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Active funds reduce their UW positions on Brazil"
  },
  {
    "figure_id": "F120",
    "report_id": "R011",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Hybrid fund issuances almost double MoM Issuances of new mutual funds (bn shares)"
  },
  {
    "figure_id": "F121",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14: A-share buybacks hit the 12-month high Share buybacks value in the A-share market (RMB bn)"
  },
  {
    "figure_id": "F122",
    "report_id": "R011",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Southbound capital flows to HK notably slowed in May Cumulative southbound capital flows to HK stocks since 2026 (HKD bn)"
  },
  {
    "figure_id": "F123",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Investors exit HK ETFs at the fastest pace on record Changes in shares of HK equity ETFs listed in China mainland (bn shares)"
  },
  {
    "figure_id": "F124",
    "report_id": "R011",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Hong Kong stock buybacks hit the 16-month high Share buybacks in the Hong Kong market (HKD bn)"
  },
  {
    "figure_id": "F125",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F126",
    "report_id": "R011",
    "label": "Exhibit 19",
    "context": "Exhibit 19: IPO financing value notably eases in May IPO financing value in HK (HKD bn) and A-share market (RMB bn)"
  },
  {
    "figure_id": "F127",
    "report_id": "R011",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Major shareholders' stock selling continues to pick up Share reductions by major shareholders in the A-share market (RMB bn)"
  },
  {
    "figure_id": "F128",
    "report_id": "R011",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Limited pressure from A-share lock-up expirations Monthly amount of lock-up expiration in the A-share market (RMB bn)"
  },
  {
    "figure_id": "F129",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Restricted stock unlocks in HK expected to surge in 3Q26 Monthly amount of lock-up expiration in HKEX (HKD bn)"
  },
  {
    "figure_id": "F130",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Interbank lending rates trend lower amid strong liquidity DR007, Shibor – 3 month, and CGB yield (%, 5-day moving average)"
  },
  {
    "figure_id": "F131",
    "report_id": "R011",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Average A-share turnover surged above RMB3tn in May Average daily trading value in the A-share market (RMB bn)"
  },
  {
    "figure_id": "F132",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Margin trading activities heat up again in May Margin trading as % of A-share market turnover (5-day moving average)"
  },
  {
    "figure_id": "F133",
    "report_id": "R011",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Hong Kong market turnover stays elevated Average daily trading value in the Hong Kong stock market (HKD bn)"
  },
  {
    "figure_id": "F134",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Apr 2026 IC production YoY growth was $+22.1\\%$ YoY, vs. $+20.6\\%$ in Mar 2026 Semiconductor monthly data in Greater China Exhibit 2: IC production was +22.1% YoY in Apr (vs. +20.6% YoY in Mar) China's monthly IC produ"
  },
  {
    "figure_id": "F135",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 3: IC import value was +68.0% YoY in May 2026 (vs. +54.7% YoY in Apr 2026) China's monthly IC import value YoY"
  },
  {
    "figure_id": "F136",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: IC imports volume at $+11.2\\%$ / $-1.0\\%$ YoY in Apr / May 2026"
  },
  {
    "figure_id": "F137",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Apr 2026 inventory days were at 61 vs. 59/57/64 days in Apr 2025/2024/2023 Inventory balance and inventory days of China's electronics manufacturing industry (including computers, mobile phones, other electronics devices"
  },
  {
    "figure_id": "F138",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 6: IC production units in China was up $22.1\\%$ YoY in Apr 2026"
  },
  {
    "figure_id": "F139",
    "report_id": "R014",
    "label": "Exhibit 7",
    "context": "Exhibit 7: SPE import value was down 4% YoY in Apr 2026 (vs. +1% YoY in Mar 2026)"
  },
  {
    "figure_id": "F140",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Semiconductor revenue in China was up 78.3% YoY in Apr 2026 (vs. 74.1% YoY in Mar 2026)"
  },
  {
    "figure_id": "F141",
    "report_id": "R014",
    "label": "Exhibit 9",
    "context": "Exhibit 9: China IC export value was up 111% YoY in May 2026 to US\\$36bn"
  },
  {
    "figure_id": "F142",
    "report_id": "R014",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Major TW semiconductor companies' aggregate revenue was up +26% YoY in May 2026 (vs. +15% YoY in Apr 2026)"
  },
  {
    "figure_id": "F143",
    "report_id": "R014",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China lithography import volume from Netherlands -40% YoY to 9 units and ASP -39% YoY to US\\$11.3m in Apr 2026"
  },
  {
    "figure_id": "F144",
    "report_id": "R014",
    "label": "Exhibit 13",
    "context": "Exhibit 13: China semiconductor test equipment import value +48% YoY in Apr 2026 to US\\$57mn China monthly semiconductor test equipment import value Exhibit 11: China lithography import volume globally -29% YoY to 55 units and ASP -"
  },
  {
    "figure_id": "F145",
    "report_id": "R014",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Foundries: Quarterly revenue"
  },
  {
    "figure_id": "F146",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Image of P/B-ROE for MTP & Mid-Long term target ROE"
  },
  {
    "figure_id": "F147",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Hanwha Aerospace share price has been falling since April highs - key events"
  },
  {
    "figure_id": "F148",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Hyundai Rotem share price has been falling since April highs - key events"
  },
  {
    "figure_id": "F149",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: At $100\\% / 50\\%$ win-rate, the key potential order pipeline would push up Hanwha's export backlog to W95tn/62tn which exceeds GSe $26 - 30\\%$ overseas revenue GSe Hanwha Aerospace order potentials"
  },
  {
    "figure_id": "F150",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Hyundai Rotem order potentials"
  },
  {
    "figure_id": "F151",
    "report_id": "R018",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Over the last 2 months, SPEs have significantly underperformed analog (Renesas) and commodity (Ibiden / Sumco)."
  }
]