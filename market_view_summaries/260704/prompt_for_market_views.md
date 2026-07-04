请基于下面每天新报告的摘要，写一份“Market Views / 国际信源汇编&评论”的结构化 JSON，用于生成 PDF。

目标读者：
关注每日更新的国际信源汇编&评论，希望快速看到国际主流叙事、数据、图表和边际变化。读者来自头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等。

要求：
1. 严格按来源拆成三个并列板块，不要混在一起：投行/券商（source_group=bank_research）、战略咨询（source_group=consulting）、智库/国际机构（source_group=institution）。
2. 三个板块篇幅要尽量接近。即使某一类报告更多，也要压缩成和另外两类相近的阅读体量；不要让世界银行/智库报告把 PDF 撑成长篇翻译。
3. 每个来源板块内部再按主题归纳 2-4 个 themes，例如宏观与利率、AI/算力、能源与大宗、地缘政治、企业战略、发展经济等。主题由内容决定，不要机械套模板。
4. 每个 theme 综合多篇报告，写 3-5 个 bullets；每条必须是可读完整句，保留关键数据、方向、分歧和边际变化，不要逐篇复述。
5. 每个 theme 必须给 references，引用报告 ID；三个来源板块合计 references 应覆盖全部或绝大多数报告。覆盖清单会展示这些 references，所以不要漏。
6. 可以使用所有 figure_ids，没有总数限制，但只选择真正支撑该板块观点且图表说明干净的图。
7. 投行名字必须脱敏：常见投行写 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写，不确定就写“投行”。
8. 不要给投资建议，不要写买卖评级。
9. 不要输出“逐篇报告摘录”；正文只需要整合后的信号、评论、数据和图表。
10. source_roundups 必须按 source_group 输出三个对象，顺序为 bank_research、consulting、institution；如果某类当天没有报告，仍输出空 themes，并在 summary 写“今日暂无新增”。
11. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{"title":"市场最新观点汇总","subtitle":"一句话说明今天国际信源的共同主线","executive_summary":["全局要点1"],"source_roundups":[{"source_group":"bank_research","title":"投行/券商","summary":"本来源板块一句话摘要","themes":[{"heading":"主题标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001","R002"]}]},{"source_group":"consulting","title":"战略咨询","summary":"本来源板块一句话摘要","themes":[]},{"source_group":"institution","title":"智库/国际机构","summary":"本来源板块一句话摘要","themes":[]}],"closing":"简短收束"}

来源数量：
{
  "投行/券商": 0,
  "战略咨询": 5,
  "智库/国际机构": 39
}

报告摘要：
[
  {
    "id": "R001",
    "title": "国际清算银行：全球经济的“韧性”已到极限，下一步是“稳健性”还是危机？",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "国际清算银行",
    "digest": "[wechat_article.md]\n# 国际清算银行：全球经济的“韧性”已到极限，下一步是“稳健性”还是危机？\n\n2026年6月，国际清算银行（BIS）发布了其年度经济报告。这份长达百余页的文件，在看似中立的“从韧性到稳健性”标题下，传递了一个并不平静的信号：全球经济在过去一年展现出的“韧性”，很大程度上依赖于AI泡沫、贸易转移和企业的利润压缩。当霍尔木兹海峡的封锁让能源供应链遭受真实冲击，当通胀再次抬头，当财政空间被高债务侵蚀，BIS真正想问的问题是——当这些临时缓冲垫逐一失效，全球经济的底层架构，是否足够“稳健”？\n\n这不是一份关于“复苏”的报告，而是一份关于“脆弱性”的诊断书。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 2025年的“韧性”是个假象：AI泡沫与贸易转移是两大临时止痛药\n\nBIS的报告开篇承认，2025年全球经济增长确实顶住了关税冲击。但细看其归因分析，这份“韧性”的来源并不令人安心。\n\n第一个缓冲是关税的实际冲击低于预期。有效关税率低于最初宣布的水平，加之贸易转移效应，企业通过压缩自身利润来消化成本。第二个、也是更关键的缓冲，是AI浪潮催生的资本支出狂潮。美国科技巨头在AI基础设施上的巨额投资，不仅拉动了本国经济，还通过全球供应链产生了正向溢出。第三个缓冲则是“动物精神”——AI叙事推高了股市估值，维持了宽松的全球金融条件。\n\n这三个因素有一个共同点：它们都是临时性的、不可持续的。关税转移终有尽头，企业利润压缩有边界，而AI投资能否持续，取决于其商业化回报是否兑现。\n\n> **KC评论：** 将2025年的增长解读为“韧性”，就像把病人靠止痛药下床走路称为“康复”。BIS这份报告的核心洞察在于，它区分了“韧性”和“稳健性”——前者是扛住冲击的能力，后者是系统本身不易受损的结构。当前全球经济的“韧性”正在被消耗，而真正的“稳健性”建\n\n[... middle omitted ...]\n\n管机构、战略咨询和智库的朋友们一起，观测全球经济的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026全球经济的四个压力点\n\n韧性够吗？要看这四个关键\n\n2025年全球经济增长扛住了高关税和地缘不确定性，靠的是AI投资浪潮和金融条件宽松。但2026年初霍尔木兹海峡封锁，能源供给的冲击直接把通胀推回高位，塑料涨了30%、化肥涨了50%，粮食安全风险在低收入国家尤其突出。⚡️\n\n往后看，四个压力点值得盯紧：\n\n1️⃣ 通胀会不会“二次传染”\n能源价格传导到工业品和食品，关键是会不会像2021-23年那样扩散。好消息是劳动力市场没那么紧、政策利率也比当年高；坏消息是大家刚经历一轮通胀，预期很容易被“拉回来”。\n\n2️⃣ 财政空间在收窄\n公共债务创历史新高，利率上行后利息负担加重。很多经济体在好年景没有做债务整合，现在遇到冲击，财政回旋余地更小了。\n\n3️⃣ 非银机构在国债市场的作用变大\n对冲基金通过回购大量借钱买国债，市场流动性变得更脆。一旦出现“财政风险重定价”和流动性枯竭的互动，可能放大波动。\n\n4️⃣ AI繁荣能持续多久\nAI相关资本开支撑住了增长，但估值已经很高。如果AI落地不及预期，企业信用可能面临重定价，从而收紧信贷条件。\n\n📌 核心启示：韧性不等于稳健。要走向真正的“robustness”，需\n\n[... middle omitted ...]\n\nrights reserved. Brief excerpts may be reproduced or translated provided the source is stated.\n\nISSN 2616-9428 (print)\n\nISSN 2616-9436 (online)\n\nISBN 978-92-9259-961-4 (print)\n\nISBN 978-92-925\n\n[... middle omitted ...]\n\nda7ba835a79e4a8c8f421a1bf.jpg)\n\n![](images/ef55f0b94344372c9dd20fe6ba5e2db7119c045960c9121a4a9f79f695b55046.jpg)\n\nBank for International Settlements (BIS)\n\nwww.bis.org\nemail@bis.org\n\nISSN 2616-9428\nISBN 978-92-9259-961-4"
  },
  {
    "id": "R002",
    "title": "布鲁金斯学会：土耳其军工从“客户”到“对手”，全球供应链正在被改写",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁金斯学会",
    "digest": "[wechat_article.md]\n# 布鲁金斯学会：土耳其军工从“客户”到“对手”，全球供应链正在被改写\n\n这份由布鲁金斯学会与IISS联合发布的报告，揭示了一个正在发生的结构性变化：一个曾经依赖西方武器供应的国家，如何通过数十年战略布局，在多个领域成为传统军工强国的竞争者。报告的核心判断是，土耳其的国防工业已走到一个十字路口——继续追求完全自主的成本越来越高，而出口导向的工业化模式又将其推入全球竞争的新战场。对于关注全球供应链重构、地缘政治风险以及新兴市场工业化路径的读者来说，这不仅仅是一个国家的故事，更是一个关于“依赖与自主”的经典案例。\n\n报告指出，土耳其的国防工业化进程，并非简单的技术追赶，而是一场由外交危机、国内政治意志和产业政策共同驱动的系统性转型。从1923年建国初期的“客户”身份，到1974年塞浦路斯行动后遭遇西方武器禁运的“被迫觉醒”，再到21世纪“本土设计”的全面爆发，土耳其走过的路，对许多试图摆脱技术依赖的发展中国家具有深刻的借鉴意义。\n\n然而，报告也毫不避讳地指出了当前模式面临的挑战：绝对自主无法实现，出口依赖带来新的脆弱性，人才流失正在侵蚀创新基础。这些问题的答案，或许就藏在土耳其下一步的战略选择中。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 1974年禁运：一次“因祸得福”的战略转折\n\n报告将1974年定义为土耳其国防工业的“分水岭”。当年土耳其出兵塞浦路斯后，美国及其盟友实施了武器禁运。这一外部冲击，直接摧毁了土耳其此前依赖美国军援的“舒适区”，也彻底改变了其决策层对国防工业的认知。\n\n在此之前，土耳其的国防工业几乎完全依附于美国。冷战期间，作为北约成员国，土耳其接受了大量美国军事援助，包括超过3000辆M48坦克和约260架F-100战斗机。这种“免费”的装备供给，虽然短期内满足了军队需求，却导致本土军工能力萎缩。19\n\n[... middle omitted ...]\n\n人才流失和新兴竞争对手的双重压力下，土耳其的出口增长能否持续？我们每日更新国际主流信源汇编与评论，汇聚了头部券商、PE/VC、投行、并购、对冲基金、资管机构、战略咨询、智库等领域的从业者，期待与您交流探讨。\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n土耳其军工：从客户到竞争对手的百年路\n\n封面：土耳其军工崛起\n\n从买家到竞争者，这步走了100年\n\n---\n\n最近读了一份很扎实的研报，讲土耳其军工工业的百年转型。从1923年建国时的“小客户”，到2024年能造五代机KAAN，这中间的逻辑值得捋一捋。\n\n**1/ 早期：被“白送”的武器拖垮了本土工业**\n\n二战后，美国通过马歇尔计划和军事援助，给土耳其送了大量装备：3000多辆M48坦克、260架F-100战机。看起来是好事，但结果？本土飞机厂直接被美制T-6教练机“卷死”，土耳其从武器买家变成了“纯受援国”，本土研发能力几乎归零。\n\n**2/ 1974年：转折点——被禁运逼出来的自主化**\n\n1974年土耳其出兵塞浦路斯，美国立刻实施武器禁运。土耳其这才意识到：靠别人，关键时刻会被卡脖子。1980年代开始，政府成立国防工业署（SSM），用“合资+技术转移”模式，让本国私企跟外国公司合作生产F-16，逐步建立供应链。\n\n**3/ 2000年后：从组装到自研**\n\n埃尔多安时期，政策转向“国产化优先”。典型例子：Bayraktar TB2无人机，从设计到量产全自主，出口到30多个国家，成了土耳其军工的“名片”\n\n[... middle omitted ...]\n\ns (CATS).\n\n## Disclaimers\n\nThe views outlined in this paper are exclusively those of the authors and do not represent institutional views of the CFPPR or the IISS.\n\n## Contents\n\nExecutive Summ\n\n[... middle omitted ...]\n\nvenes conferences including the IISS Shangri-La Dialogue and IISS Manama Dialogue, world-leading forums for the discussion of security issues. IISS research helps governments, academics, the media and the private sector."
  },
  {
    "id": "R003",
    "title": "布鲁金斯学会：中美AI对话的真正价值不在信任，而在共同恐惧",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁金斯学会",
    "digest": "[wechat_article.md]\n# 布鲁金斯学会：中美AI对话的真正价值不在信任，而在共同恐惧\n\n特朗普与习近平在2025年宣布重启中美政府间AI对话，这本身就是一个信号。但真正值得关注的，不是对话重启这个动作，而是驱动这个动作的底层逻辑发生了变化。\n\n过去七年主持中美AI二轨对话的布鲁金斯学会专家，在日内瓦联合国AI安全与伦理全球会议上给出了一个关键判断：中美之间在AI问题上能够坐下来谈，不是因为信任的修复，而是因为恐惧的趋同。这种恐惧并非泛泛的“技术失控”，而是指向两个具体领域——AI叠加网络攻击，以及AI叠加生物安全。这两条线索，正在成为两国技术安全议程上最有可能产生实际成果的突破口。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮重启与拜登时期的失败形成鲜明对比，关键教训在于议程准备\n\n拜登政府时期中美曾尝试过一次AI对话，结果并不理想。布鲁金斯学会专家在播客中将其描述为“shambolic”——外交上缺乏准备，双方带着完全不同的议程预期走进会议室。那次失败的直接后果是，对话不仅没有推进实质问题，反而加深了彼此的疑虑。\n\n而这一次，两位领导人在北京会晤时公开宣布重启对话，并明确将其作为2025年华盛顿峰会的阶段性成果来预期。这意味着，这次对话不是试探性的，而是带有明确的成果导向。\n\n这里的关键变量在于，双方是否吸取了上次失败的教训。布鲁金斯学会的专家明确指出：双方必须在进入会议室之前完成外交层面的“功课”，确保议程和预期已经对齐。这一点看似基础，但在中美关系当前的大背景下，实际操作难度远高于表面。\n\n> **KC评论：** 拜登时期那次失败的对话，本质上反映了技术问题在外交议程中的“夹生”状态——技术团队和外交团队没有形成有效的协同。这次重启能否避免重蹈覆辙，取决于双方是否在桌下完成了真正的技术议题对齐。报告里对那次失败的描述值得细读，因为\n\n[... middle omitted ...]\n\n域的同行一起交流，每日更新国际主流叙事与数据，观测边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中美AI对话：比核弹更难管的技术来了\n\n封面：AI安全对话实录\n\n副标题：从日内瓦联合国会议看大国博弈\n\n---\n\n1/ 中美在AI安全领域有个共同点：**都怕对方失控**。\n这不是客套话，而是双方在日内瓦联合国AI安全与伦理大会上反复提及的真实焦虑。投行研报指出，两国都担心AI被非国家行为体滥用，尤其是**生物武器和网络攻击**领域。\n\n2/ 过去7年，布鲁金斯学会和清华一直在搞“二轨对话”——就是非官方专家之间的闭门交流。这种对话在战略竞争背景下还能持续，说明**双方都觉得不谈不行**。\n\n3/ 对话的核心逻辑不是“信任”，而是**共同利益**。\n研报原话是：“对话发生在一个相互不信任但彼此利益交汇的背景下。”双方都认为AI技术发展速度远超政府监管能力，这是罕见的共识。\n\n4/ 特朗普和习近平已宣布恢复政府间AI对话。\n但上一轮拜登政府的尝试被形容为“一团糟”——双方连议程都没对齐。这次必须吸取教训，**先做足外交铺垫**，再谈实质性议题。\n\n5/ 最可能优先讨论的领域是：**AI+网络攻击**和**AI+生物安全**。\n这两个领域中美都感到“脆弱”，且风险是全球性的。研报特别提到，连中方也承认技术\n\n[... middle omitted ...]\n\nmary:\n\nIn this special episode of The Beijing Brief, Ryan Hass speaks with R. David Edelman on the sidelines of the United Nations Global Conference on AI, Security, and Ethics in Geneva, Swit\n\n[... middle omitted ...]\n\nir support.\n\nTo learn more about our research, visit us at Brookings dot edu slash China Center, and to learn more about this podcast, go to Brookings dot edu slash The Beijing Brief or wherever you like to get podcasts."
  },
  {
    "id": "R004",
    "title": "IMF：中亚信贷扩张的结构性机会与周期性隐忧",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：中亚信贷扩张的结构性机会与周期性隐忧\n\n信贷增长是金融稳定的核心变量。历史上，信贷高速扩张往往先于金融压力出现，而信贷深度长期低于基本面则可能制约投资与增长。对于政策制定者而言，真正的挑战在于区分可持续的金融深化与过度的信贷扩张。这份由IMF两位经济学家Etibar Jafarov和Chingis Matayev撰写的工作论文，聚焦高加索和中亚地区（CCA）的信贷动态，给出了一个既清醒又具有操作性的判断：该地区仍有金融深化的空间，但家庭信贷的扩张速度正在接近需要密切关注的临界点。\n\n报告的核心贡献在于建立了一套“双重视角”的分析框架——既看信贷相对于基本面的水平，也看信贷相对于自身趋势的增速。这组框架的意义不仅限于CCA地区，对任何关注新兴市场信贷风险的人来说，都值得细读。\n\n> **KC评论：** 这份报告最值得注意的结论不是“信贷高了”或“信贷低了”，而是“水平还有空间，但速度需要警惕”。对于投资者而言，这意味着该地区的银行股和信贷资产仍有结构性故事可讲，但需要密切跟踪家庭部门的杠杆节奏。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 信贷深度仍有空间，但结构性分化显著\n\n报告首先通过均衡模型估算了各国信贷/GDP比率的长期均衡水平。结果显示，所有CCA经济体都存在进一步的金融深化空间，但这种空间在不同国家之间差异巨大。\n\n亚美尼亚和格鲁吉亚是区域内的金融深化领先者，信贷/GDP比率在某些年份接近60-70%，反映了更深入的经济转型和金融中介化。吉尔吉斯斯坦和塔吉克斯坦则处于另一个极端，信贷/GDP比率仅在10-25%之间，金融体系仍然较浅。哈萨克斯坦、阿塞拜疆和乌兹别克斯坦位于中间位置，但前两个国家经历了明显的信贷繁荣-萧条周期。\n\n这一发现对投资者的含义是明确的：在评估该地区信贷资产质量时，不能简单套\n\n[... middle omitted ...]\n\n资管机构和战略咨询等领域的朋友，共同探讨全球市场的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n高加索中亚信贷，正在发生什么？\n\n信贷扩张的AB面\n\n金融深化与风险信号如何共存？\n\n最近读了一份IMF的工作论文，讲的是高加索和中亚地区的信贷扩张，逻辑很清晰，分享几个核心发现👇\n\n**1. 信贷深度：还有空间**\n整体来看，这些国家的信贷/GDP比国际水平偏低，说明金融深化还有很大空间。但各国差异明显：亚美尼亚、格鲁吉亚接近60-70%，而吉尔吉斯、塔吉克只有10-25%，中间层是乌兹别克、哈萨克和阿塞拜疆。\n\n**2. 增长的引擎变了：家庭信贷崛起**\n过去几年，家庭贷款成了信贷增长的主力，多数国家家庭信贷已经超过企业贷款。只有乌兹别克斯坦例外，企业贷款仍占大头，但家庭贷款增速更快。这意味着信贷结构在发生实质变化。\n\n**3. 波动性高，警惕“过热”信号**\n哈萨克、阿塞拜疆、塔吉克都经历过信贷急剧收缩，信贷/GDP一度下降15-20个百分点。论文用了三种方法测度信贷“过热”风险：长期均衡法、统计缺口法、卡尔曼滤波法，结论是——没有单一指标能完美预测风险，组合使用更靠谱。\n\n**4. 美元化下降，是个好消息**\n过去这些地区外贷占比高，汇率风险大。现在本币贷款占比明显上升，所有中亚国家本币贷款都已超过外\n\n[... middle omitted ...]\n\n by Etibar Jafarov and Chingis Matayev\\*\n\nAuthorized for distribution by Amina Lahreche\nJune 2026\n\nIMF Working Papers describe research in progress by the author(s) and are published to elicit\n\n[... middle omitted ...]\n\ning their histories to define tranquil observations and to document vulnerability build-ups that did not crystallize into systemic breaks.\n\n![](images/f215817b6111823c66ad03c32d991086d7c45074c575451831827308e8cf2d01.jpg)"
  },
  {
    "id": "R005",
    "title": "IMF：前沿市场真正的门槛不是增长，是制度",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：前沿市场真正的门槛不是增长，是制度\n\n当全球投资者还在为新兴市场的波动焦虑时，一个被忽视的群体正在悄悄改变国际资本的流向版图。IMF最新工作论文给出了一组值得深思的判断：前沿市场（Frontier Markets）的跃迁，本质上不取决于全球流动性是否宽松，而取决于国内制度质量和宏观经济纪律。\n\n这份由IMF战略、政策与审查部授权的报告，系统梳理了30年来低收入国家如何跨越“前沿市场”这道门槛。其核心发现可能颠覆许多投资者的固有认知——**决定一个国家能否从低收入国升级为前沿市场的，不是增长故事，而是治理质量**。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 前沿市场的门槛：金融深度的量化标尺\n\nIMF团队构建了一套可复制的量化识别框架，用五个金融指标来划定前沿市场的边界：广义货币与GDP之比、跨境贷款和存款、股票市场市值、投资组合流入，以及主权债券发行能力。一个低收入国家只有在这五项中至少满足四项，才能被认定为前沿市场。\n\n这套方法论的价值在于去主观化。过去，金融机构和评级机构对前沿市场的认定往往带有判断成分，甚至存在“一锤子买卖”的问题——某个国家可能因为一次偶然的债券发行就被贴上前沿市场标签。IMF的滚动三年窗口机制，有效过滤了这种噪音。\n\n从数据看，1993年至2022年间，前沿市场群体持续扩大，尤其在2008年全球金融危机后加速。23个低收入发展中国家在此期间成功进入国际债券市场。但值得注意的是，前沿市场状态具有强持续性——一旦获得，很少轻易失去，这暗示其背后是结构性因素在支撑。\n\n> **KC评论：** 对于投资者而言，这套识别框架意味着什么？它提供了一个比传统指数更干净、更可回溯的筛选工具。完整报告附录中有各国每年的分类结果热力图，可以清晰看到哪些国家在什么时间点跨过了门槛，以及哪些国家在危机中\n\n[... middle omitted ...]\n\n际变化。如果你也关注这些被主流忽视的市场信号，欢迎扫码交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n从低收入到新兴市场，中间还藏着关键一步\n\n中间地带：前沿市场\n\n前沿市场（Frontier Market）不是新兴市场，而是低收入国家走向新兴市场前的一个中间站。这个概念诞生于30年前，2008年全球金融危机后开始被更多投资者关注。\n\n📌 什么是前沿市场？\nIMF在2014年给出了一个数据驱动的定义，主要看5个指标：\n- 金融体系深度（广义货币/GDP、股市市值）\n- 金融开放度（跨境贷款、存款、组合投资流入）\n- 国际市场发债能力\n\n前沿市场≠简单发过一次债。有些国家可能只是“一次性发债”，不构成真正的市场地位。\n\n📌 什么决定一个国家能成为前沿市场？\n研究用动态样本分析了低收入国家升级为前沿市场的驱动因素，发现：\n\n1️⃣ 基本面是硬门槛\n- 强劲的经济增长\n- 低公共债务水平\n- 经济制度和治理改善\n\n2️⃣ 全球因素反而没那么重要\n- 美国货币政策、股市波动这些“推因素”对升级影响不大\n- 前沿市场地位本身有很强的持续性，说明“拉因素”（国内基本面）才是关键\n\n📌 前沿市场受美国货币政策影响大吗？\n研究用影子短期利率衡量美国货币政策，发现：\n\n- 前沿市场的主权利差对美政策变化的敏感度，和新兴市场差不\n\n[... middle omitted ...]\n\n)\n\nWP/26/140\n\nIMF Working Paper\nStrategy, Policy, and Review Department\n\nFrontier Markets: Analyzing Drivers of Market Growth and Sovereign Risks\\* Prepared by Younes Takki Chebihi, Naoya Kato\n\n[... middle omitted ...]\n\narch, 16(3), 294-312.\n\nSpeidell, L. S., & Krohne, A. (2007). The case for frontier equity markets. The Journal of Investing, 16(3), 12-22.\n\n![](images/b9adff0cc4b4aaa0815303cd24579d11476daea913e442bfca8dac4f44e3bc44.jpg)"
  },
  {
    "id": "R006",
    "title": "IMF：卡塔尔主权利差收窄，改革“广度”比“深度”更值钱",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：卡塔尔主权利差收窄，改革“广度”比“深度”更值钱\n\n全球不确定性创下历史新高，投资者正在用脚投票。他们奖励的不是某个单一领域的激进改革，而是“全面、平衡、协调”的改革组合。\n\n这是国际货币基金组织（IMF）最新工作论文《Pricing Reform Progress: Evidence from Sovereign Spreads and Consensus Forecasts》的核心发现。这篇由Ken Miyajima撰写、发布于2026年7月的报告，以卡塔尔为锚点，为中东和北非（MENA）地区18个经济体过去十年的主权信用利差变化，提供了一个极其清晰的解释框架。\n\n报告给出的结论并非模棱两可：**投资者不仅看“改革做了什么”，更看“改革是否平衡”。** 那些在多个维度同步推进改革的国家，其主权信用利差收窄的幅度，远大于只在一两个领域发力、其他领域滞后的国家。\n\n这对任何正在推进结构性改革的新兴市场，都是一个值得反复推敲的信号。\n\n> **KC评论：** 这篇报告的真正价值不在于它证明“改革有用”——这几乎是常识。它真正锋利的地方在于区分了“改革深度”和“改革广度”。它用计量方法证明：当五个改革子指标的标准差越小（即改革越平衡），主权利差收窄越明显。这意味着，一个在财政纪律上做到极致、但在营商环境或货币政策独立性上毫无进展的国家，其信用溢价可能高于一个各项改革都做到70分的国家。这是对“单项冠军”式改革策略的直接挑战。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 全球不确定性高企的背景下，国内稳定成为稀缺溢价\n\n报告开篇即点明背景：全球经济和政策不确定性已升至前所未有的水平。IMF使用的全球不确定性指数在2025年初仍处高位，而中东地区的地缘政治风险更是加剧了这一趋势。\n\n但卡塔尔是一个显著的例外。报告使\n\n[... middle omitted ...]\n\n际变化，交流深度观点。扫码加入，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n卡塔尔凭什么拿到AA评级？\n\n主权信用升级的逻辑\n\n投资者奖励全面的改革\n\n最近在看一份IMF的工作论文，讲的是主权信用质量与改革进程的关系，案例聚焦卡塔尔。看完最大的感受是——市场真的会为“靠谱的改革”买单。\n\n1. 改革要“全面”，不能偏科\n论文用了一个很妙的指标：改革子项的均衡度（标准差）。不是单个指标做得好就行，而是五个维度（财政、货币、制度等）要同步推进。均衡度越好的国家，主权信用利差越低。\n\n2. 财政纪律是硬通货\n对于资源型经济体（卡塔尔是天然气出口大国），投资者最看重的不是增长多快，而是财政支出有没有纪律。数据显示，财政纪律严明的国家，面对外部冲击时利差波动更小。\n\n3. 预期比现状更重要\n论文用的是“共识预测”数据（分析师对未来宏观变量的预期），而不是历史数据。说明市场定价的是“你将要变成什么样”，而不是“你现在是什么样”。\n\n4. 卡塔尔的案例很典型\n过去十年，卡塔尔主权CDS利差从100bp收窄到40bp，三大评级机构都给了AA。背后是第三国家发展战略下的全面改革，加上LNG产能扩张带来的中期增长确定性。\n\n5. 对投资者的启示\n主权信用质量不是静态的。如果看到某个国家在财政纪律、货币可\n\n[... middle omitted ...]\n\nreign Spreads and Consensus Forecasts Prepared by Ken Miyajima\\*\n\nAuthorized for distribution by Nathan Porter\nJuly 2026\n\nIMF Working Papers describe research in progress by the author(s) and \n\n[... middle omitted ...]\n\nThe credit signals that matter most for sovereign bond spreads with split rating.” Journal of International Money and Finance, 53, 174–91.\n\n![](images/ec645b995e9398817bc943c7b38a441c9ebfc35a051aa10b61a7c918529d2eb2.jpg)"
  },
  {
    "id": "R007",
    "title": "IMF：中东和中亚的真正考验不是冲击本身，而是政策框架能否扛住下一轮全球波动",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：中东和中亚的真正考验不是冲击本身，而是政策框架能否扛住下一轮全球波动\n\n全球经济的核心叙事正在切换。贸易保护主义、地缘碎片化、以及美联储政策路径的不确定性，共同构成了一个高频外部冲击的新常态。对于中东、北非、巴基斯坦（MENAP）以及高加索和中亚（CCA）地区而言，一个根本性问题浮出水面：当下一轮全球风险溢价飙升或贸易条件恶化时，这些经济体靠什么来缓冲？\n\nIMF在2026年7月发布的工作论文《Resilience by Design》给出了一个清晰且可检验的答案。核心判断是：政策框架的设计质量，而非资源禀赋或短期刺激能力，才是决定这些地区能否在冲击后实现“V型”修复的关键。报告通过全球面板实证和模型模拟，系统论证了两个支撑性结论——灵活的汇率制度与可信的通胀目标制组合，以及强约束力的财政规则，能够显著降低外部冲击带来的产出损失，并缩短调整周期。这篇导读将提炼报告中最值得决策者关注的逻辑链条和隐含判断，并指出报告尚未完全展开的关键追问。\n\n> **KC评论：** 很多人把中东和中亚的经济韧性等同于石油美元储备或主权财富基金。但这份报告揭示了一个更微妙的现实：储备是盾牌，而政策框架是免疫系统。没有后者，冲击的滞后效应会持续侵蚀增长潜力。这一点，在报告对财政规则与主权利差关系的实证分析中表现得尤为突出，值得完整阅读原文图表。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 汇率制度选择不是技术细节，而是决定冲击传导路径的结构性变量\n\n报告在实证部分采用局部投影法，对过去三十多年全球样本进行分析，得出了一个对政策制定者具有直接指导意义的结论：在遭遇全球不确定性冲击后，实行浮动汇率或通胀目标制灵活汇率的经济体，其实际GDP的累计损失明显小于实行固定汇率或严格钉住汇率的经济体。\n\n这一结论的机制并不复杂。浮动汇率在冲击发\n\n[... middle omitted ...]\n\n踪全球宏观叙事与边际变化，获取每日更新的国际信源汇编与评论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东中亚要“抗揍”，政策工具箱得升级\n\n全球变局下的韧性设计\n\nIMF新出的工作论文，专门研究了中东、北非、巴基斯坦（MENAP）和高加索、中亚（CCA）地区，在外部冲击越来越频繁的背景下，怎么靠政策框架来“稳住”。\n\n核心就两句话，但背后逻辑值得拆开看：\n\n1️⃣ 汇率灵活是“减震器”，但需要配套条件\n- 论文用模型跑出来，面对全球负面冲击，实行通胀目标制+浮动汇率的经济体，GDP损失更小、恢复更快。\n- 关键前提：出口多元化 + 金融市场够深。目前MENAP和CCA地区这两项还在追赶中，但论文认为，随着未来几年进步，浮动汇率的收益会越来越大。\n- 固定汇率能“借”来低通胀，但代价是丧失政策自主权——一旦财政纪律松了、储备不够，就容易崩（论文提了阿根廷2001和黎巴嫩2019的案例）。\n\n2️⃣ 强财政规则能“压舱”，还能降融资成本\n- 全球样本回归显示，有“强财政规则”的国家，主权利差平均低85个基点。换句话说，市场更信任它们。\n- 但MENAP和CCA地区只有1/4的国家有正式财政规则，远低于新兴市场（2/3）和发达经济体（80%+）。\n- 例外：海湾产油国虽然没正式规则，但靠主权财富基金和高储备，同样\n\n[... middle omitted ...]\n\naper MCD\n\nResilience by Design:\nWhat Role Can Policy Frameworks Play in the Middle East and Central Asia?\nPrepared by Hasan Dudu, Troy Matheson, Dirk Muir, Karmen Naidoo, Salem Nechi, and Pedr\n\n[... middle omitted ...]\n\nip Report: Global Economic Prospects. Washington DC. June.\n\nWorld Bank. 2022. Fiscal Frameworks for Resilience and Growth. Washington D.C.\n\n![](images/d0b81764f5bbe9468ca016b294f00d0d93dc53df201d46993c4dafb80abcb7ac.jpg)"
  },
  {
    "id": "R008",
    "title": "IMF：石油经济体真正该担心的不是银行破产，而是存款被抽干",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：石油经济体真正该担心的不是银行破产，而是存款被抽干\n\n石油价格暴跌时，市场习惯性追问银行会不会倒闭。IMF这份以阿曼为案例的最新工作论文给出了一个反直觉的结论：阿曼银行的资本充足率高达17.5%，远高于监管底线，资本缓冲足以吸收典型油价冲击带来的信用损失。真正值得担忧的，是一个被多数人忽略的流动性渠道——当油价下跌，政府同时抽走存款、增发国债，银行体系的可贷资金被双重挤压，私人信贷被系统性挤出，而这与银行自身的资产质量毫无关系。\n\n这份由Yurii Sholomytskyi等人撰写的DSGE模型研究，将阿曼银行业对石油冲击的脆弱性拆解为两个独立渠道：偿债能力渠道，即油价下跌导致企业违约率上升、不良贷款增加；以及流动性渠道，即政府因财政收入骤降而从银行提取存款并发行国债。IMF的定量分解显示，后者才是主导力量——油价冲击解释了非石油GDP波动的54%和信贷波动的53%，而银行资本冲击的贡献不足0.1%。\n\n这意味着，对于阿曼乃至整个海湾地区的石油经济体而言，金融稳定的核心风险不在资产负债表的资产端，而在负债端的政府存款依赖。这是一个完全不同的监管和政策逻辑。\n\n> **KC评论：** 传统银行压力测试主要关注资本充足率和不良贷款率。IMF这份报告暗示，对于石油经济体，压力测试的假设框架需要重写——最危险的情景不是信用风险集中爆发，而是政府同时作为存款人和债券发行人对银行流动性的双向挤压。完整报告中对“流动性缓冲陷阱”的建模，以及主权财富基金在缓冲链条中的角色，值得每一位关注新兴市场金融稳定的读者仔细阅读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 银行不缺资本，但缺存款——流动性渠道才是真正的大头\n\nIMF模型最核心的发现是结构性方差分解的结果。在阿曼的经济结构中，油价冲击对非石油GDP波动的贡献率达到54\n\n[... middle omitted ...]\n\n一同交流这些尚未完全解答的问题，观测全球宏观叙事的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n石油国银行，怕油价跌吗？\n\n油价跌了，银行会怎样？\n\n石油收入占政府收入70%，银行系统30%的存款来自政府和国企。油价一跌，双面夹击就来了。\n\n1️⃣ 不是坏账风险，而是流动性挤压\n很多人觉得油价跌了，企业还不上钱，银行坏账飙升。但阿曼的情况恰恰相反——银行资本充足率17.5%，坏账率4.5%，有69.3%的拨备覆盖，资本缓冲很足。\n真正的问题在流动性端。\n\n2️⃣ 政府存款抽水 + 发债 = 银行可贷资金被挤占\n油价跌→政府收入锐减→政府一边提取银行存款，一边发行国债让银行买。\n对银行来说，这两件事效果一样：钱被抽走了，能放贷的资金变少。\nIMF用DSGE模型测算：油价冲击解释了非石油GDP波动的54%、信贷波动的53%。而银行资本冲击的贡献不到0.1%。\n\n3️⃣ 银行自己也会“囤钱”\n研究发现一个有意思的现象叫“流动性缓冲陷阱”——油价好的时候，银行反而囤积超额流动性，不积极放贷，因为怕后面油价又跌。\n这导致生产部门长期得不到足够信贷。\n\n4️⃣ 什么在起作用？\n阿曼2040愿景推动伊斯兰银行和sukuk市场发展，企业融资渠道变多，银行系统韧性在增强。\n还有一个“信用深度”的概念：银行保守放贷，反而保\n\n[... middle omitted ...]\n\nor Capacity Development\n\nShould Oil Economies Worry About Oil Shocks' Impact on the Banking System? The Case of Oman\n\nPrepared by Yurii Sholomytskyi, Nathaniel Butler Blondel, $^{1}$ and Mumta\n\n[... middle omitted ...]\n\ncal Economy, 90(6):1187–1211, 1982.\n\nC. A. Sims. Solving linear rational expectations models. Computational Economics, 20(1-2):1–20, 2002.\n\n![](images/517e7dea3686b487fbb834ea838ab2857fc087598a0187a905f732568774fd30.jpg)"
  },
  {
    "id": "R009",
    "title": "IMF最新研究：自然灾害正在重塑发展中国家的国债定价",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF最新研究：自然灾害正在重塑发展中国家的国债定价\n\n当一场干旱或飓风过后，市场对主权信用的重新定价往往比灾后重建更快。IMF最新工作论文揭示了一个此前被忽视的机制：自然灾害不仅摧毁实体资产，还会直接推高发展中国家的国内国债融资成本，且这种冲击沿着收益率曲线呈现非对称传导——短期利率飙升，长期利率却几乎不受影响。\n\n这份由Kpodar、Drabo和Meyimdjui撰写的研究，基于一个全新的99国国内国债收益率数据库，覆盖2000至2020年间的72个发展中国家。其核心发现值得所有关注新兴市场债务和气候风险的投资者认真审视：气候脆弱性正成为主权信用定价中一个独立的、系统性的风险因子。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 国内债务市场已成为气候风险传导的“第一现场”\n\n过去二十年，发展中国家的国内公共债务占GDP比重从约22%升至2020年的34%。国内债务占总债务的比例也从世纪初的约30%提升至接近50%。与此同时，国内债务的利率普遍高于外债，这意味着国内利息支出占总利息支出的比例远超其债务占比。\n\n这意味着什么？当自然灾害发生时，政府首先需要融资的场所就是国内债券市场。但恰恰是这一市场，此前几乎没有被系统性地研究过气候风险如何定价。\n\n> **KC评论：** 传统研究聚焦于主权外债利差，但IMF这份报告提醒我们，对发展中国家而言，国内债券市场才是主权信用的“第一定价场所”。外债违约有IMF和双边债权人参与谈判，而国内债务的定价调整是即时、直接且影响更广的。这一点对理解新兴市场债务风险至关重要。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 灾害冲击只推高短期利率，但气候脆弱性拉平了整个收益率曲线\n\n报告的实证结果呈现出一个清晰且富有洞察力的分化：干旱和风暴等具体灾害\n\n[... middle omitted ...]\n\n追踪国际主流叙事与边际变化，每日更新汇总全球关键数据与图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n气候灾害如何影响政府借债成本\n\n🌍 灾难溢价真实存在\n\n某外资投行最新研报发现：自然灾害冲击会显著推高发展中国家短期国债利率，但对长期国债影响有限。这背后是“灾难溢价”在定价。\n\n**1/ 短期 vs 长期：分化明显**\n- 干旱和风暴事件只会让短期（1年内）国债利率上升\n- 中长期国债利率基本不受单次灾害影响\n- 但整体气候脆弱性会推高整条收益率曲线\n\n**2/ 两大传导渠道**\n🔹 财政压力：灾害后财政赤字扩大、债务上升，投资者要求更高风险溢价\n🔹 货币政策：灾害引发通胀压力，央行加息，推高短期融资成本\n\n**3/ 金融深度是缓冲器**\n研报发现：金融体系越深的国家，气候脆弱性对长期国债利率的负面影响会被削弱。这意味着发展本地资本市场是气候韧性的重要一环。\n\n**4/ 数据背后的逻辑**\n研究覆盖72个发展中国家（2000-2020年），首次系统拆解了不同期限国债的利率反应。短期债受冲击大，因为投资者对近期不确定性更敏感；长期债则更多反映结构性风险。\n\n**讨论**\n当气候风险开始影响主权融资成本，债务管理框架是不是也该把“韧性建设”纳入核心考量？欢迎一起探讨。\n\n#学习笔记\n\n[source_miner\n\n[... middle omitted ...]\n\n Natural Disaster Shocks: Unraveling the Domestic Yield Curve Response Prepared by Kangni Kpodar, Alassane Drabo and Carine Meyimdjui\\*\n\nAuthorized for distribution by Kangni Kpodar\n\nJuly 2026\n\n[... middle omitted ...]\n\nt; robust standard errors in parentheses; \\* significant at 10 percent, \\*\\* significant at 5 percent and \\*\\*\\* significant at 1 percent.\n\n![](images/0485a076cb90a35fc8822b1e55da175f6ae1bf3f43ae7e6537e8bdf48322f606.jpg)"
  },
  {
    "id": "R010",
    "title": "世界银行：AI准备度差距的真正分界线，不是算力，而是经济复杂度",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：AI准备度差距的真正分界线，不是算力，而是经济复杂度\n\n当全球目光聚焦在芯片算力、大模型参数和资本开支竞赛时，一个更根本的结构性鸿沟正在被低估。世界银行最新工作论文《Beyond the AI Divide》给出了一个反直觉的结论：决定一个国家能否跨越AI鸿沟的核心变量，并非其拥有的GPU数量或AI初创公司估值，而是其经济复杂度——即经济体生产多样化、高附加值产品与服务的能力。这份基于IMF 2023年AI准备度指数（AIPI）的实证研究，通过对比174个国家的实际AI准备度与基于其经济复杂度的预测值，系统识别出全球和区域层面的“AI超预期者”。这些超预期者并非AI领域的全球领导者，而是那些在经济复杂度给定的条件下，AI准备度显著高于预期的经济体。这一发现为产业决策者提供了一个全新的观察框架：AI竞争的本质，是经济体知识密度的竞争。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 经济复杂度解释了约75%的AI准备度差异，这远超算力或资本投入的单独解释力\n\n报告的核心实证发现是，在125个样本国家中，经济复杂度指数（ECI）与AI准备度指数（AIPI）之间的相关性高达0.89（未加权），R方达到0.79。这意味着，仅凭一个国家的经济复杂度，就能解释其AI准备度近八成的差异。这一数字远高于任何单一要素——如互联网渗透率、研发支出或STEM教育投入——对AI准备度的单独解释力。\n\n世界银行经济学家Pierre Mandon采用贝叶斯模型平均法（BMA），从67个历史、政治和经济指标中筛选出AI准备度的最稳健预测因子。结果清晰显示：1960年的初始条件——包括预期寿命、高等教育水平和经济规模——以及儒家文化传统和东亚区域虚拟变量，均与AIPI显著正相关。相反，政治不稳定性（以革命和军事政变频率衡量）则呈现显著负相关\n\n[... middle omitted ...]\n\n，汇总国际主流叙事、数据和图表，观测边际变化。期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球AI准备度：谁在超常发挥？\n\nAI准备度的隐形冠军\n\n国家AI准备度，和经济复杂度强相关。但有些国家，硬是跑赢了“预测线”。\n\n投行研报用国际货币基金组织的AI准备度指数(AIPI)和经济复杂度指数(ECI)，找出两类“超常发挥者”：\n\n1️⃣ 全球超常者（高收入组）\n新加坡、韩国、日本、荷兰、丹麦、芬兰、挪威、澳大利亚、新西兰、香港（中国）\n他们的AI准备度明显高于ECI预测值，证明制度设计能放大经济基础优势。\n\n2️⃣ 地区超常者（中低收入组）\n中国、马来西亚、印度、越南、印尼、哈萨克斯坦、加纳、卢旺达、突尼斯、斯里兰卡\n这些国家在资源约束下，通过战略投入实现AI准备度跃升。\n\n关键驱动力是什么？\n- 所有收入组：法规和伦理框架是共同核心\n- 低收入组：法规+劳动力市场政策优先\n- 中高收入组：数字基础设施重要性上升\n- 高收入组：数字基建+创新系统+人力资本全面领先\n\n有意思的是，政治稳定性和儒家文化背景都被发现是AI准备度的长期正向预测因素。\n\n这意味着，AI准备度不是单纯砸钱就能追上的。制度质量、教育基础、社会稳定，才是真正拉长或缩短AI鸿沟的关键变量。\n\n#学习笔记\n\n[source_m\n\n[... middle omitted ...]\n\nring a comprehensive assessment of national artificial intelligence capabilities. The findings highlight the varying significance of regulation and ethics frameworks, digital infrastructure, a\n\n[... middle omitted ...]\n\nrom the “wbopendata” module in Stata (Azevedo, 2020), with data for Taiwan Province of China obtained from the Statista website. For more details, see the \\`\\` Data and Methodology\" and \\`\\` Empirical Findings\" sections."
  },
  {
    "id": "R011",
    "title": "世界银行：数据透明是主权债投资者的隐藏回报来源",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：数据透明是主权债投资者的隐藏回报来源\n\n全球投资者在配置新兴市场主权债券时，通常把注意力集中在信用评级、外债水平、政治风险和全球流动性环境上。但世界银行最新发布的一篇政策研究论文提出了一个被严重低估的变量：数据透明度。\n\n这份由经济学家 Megumi Kubota 撰写的工作论文，首次从债权人（投资者）而非债务人（借款国）的视角，系统检验了数据透明度与主权债券回报之间的关系。结论简洁但有力：在制度质量达到一定门槛的国家，数据透明度的提升可以直接转化为更高的主权债券回报。更关键的是，即使一个国家已经处于高负债状态，增强数据透明度仍然可以部分抵消债务对债券回报的负面拖累。\n\n这不是一个关于“做好事有好报”的道德叙事。这是一份关于主权债券定价中一个被忽略的套利因子的实证分析。对于正在重新评估新兴市场敞口的机构投资者而言，这份报告提供了一个可量化的新观察维度。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 数据透明度对主权债回报的影响存在明确的制度质量门槛\n\n论文使用固定效应工具变量法（FE-IV），对 76 个国家 1995 年至 2020 年的面板数据进行了回归分析。核心发现是：数据透明度对主权债券回报的正向影响，并非在所有国家都成立。只有当一国的制度质量（以 ICRG 指数衡量）超过一个特定阈值时，透明度改善才能带来债券回报的提升。\n\n这个阈值是多少？论文估计出的 ICRG 指数（取对数后）门槛值稳定在 4.15 左右。换算成原始分数，大约是 63.66 分（满分 100）。这意味着，对于制度质量处于中低水平的国家，单纯提高数据透明度可能无法让投资者直接受益。\n\n> **KC评论：** 这个门槛的存在，解释了为什么很多新兴市场国家即使加入了 IMF 的数据公布标准（SDDS），也没有立刻吸引更多资本流入。投资\n\n[... middle omitted ...]\n\n欢迎扫码加入，与来自头部券商、资管机构和智库的朋友一起交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据透明，债券投资者能赚更多？\n\n数据透明≠高回报\n\n但高制度质量下，它确实能增厚收益\n\n最近读了一份某外资投行的研报，讲的是数据透明度对主权债券回报的影响。结论很有意思：数据透明不是万能的，但在制度质量中等的国家，它能帮投资者多赚钱。\n\n1/ 数据透明 ≠ 所有人受益\n- 研报用76个国家25年数据发现：数据透明度提高，主权债券回报上升，但前提是“制度质量”达标。\n- 门槛是ICRG指数（制度质量指标）超过4.15（对数）。低于这个值，透明度提升对回报影响不大。\n- 换句话说：制度好的国家，透明=加分；制度弱的，透明=白费劲。\n\n2/ 高债务也能“减负”\n- 债务高的国家，债券回报通常低。但研报发现：数据透明度提升，能缓解高债务的负面冲击。\n- 即使国家杠杆率很高，只要数据更透明，投资者依然愿意给更高回报。\n- 这解释了为什么有些高负债新兴市场，债券反而有吸引力。\n\n3/ 投资者能赚多少？\n- 研报算了一笔账：如果数据透明度提升到中高收入国家前10%水平，全球投资者能多赚多少？\n- 举例：中国可多赚870个基点（约2500亿美元），巴西680个基点，南非572个基点。\n- 数据透明不再是“道德呼吁”，而是实\n\n[... middle omitted ...]\n\n that it examines the relationship between sovereign bond returns and data transparency, and then calculates the benefits accrued by external creditors from improved data transparency in the b\n\n[... middle omitted ...]\n\n 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region  \n![](images/109884ab3b56e4ebeeefa2c6448ef2f33ccb3f25d0b85da3b034bb7e85acd2fd.jpg)"
  },
  {
    "id": "R012",
    "title": "世界银行：冲突地带才是生物多样性最被低估的“沉默金库”",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：冲突地带才是生物多样性最被低估的“沉默金库”\n\n当全球目光聚焦于亚马逊雨林和珊瑚礁的生态危机时，世界银行一份2025年初发布的工作论文揭示了一个更棘手但也更具战略意义的盲区：那些被战争撕裂、主权悬而未决、治理几乎真空的地带，恰恰是大量濒危物种的最后庇护所。这个结论本身并不令人意外——人类活动的减少客观上为野生动物创造了喘息空间。但真正值得决策者关注的，是报告提供了一套可操作的数据框架，使得在这些“法外之地”开展基于证据的保育合作成为可能。这不再是一个纯粹的生态议题，而是一个被忽视的地缘政治与可持续发展的交叉点。\n\n这份由世界银行研究团队基于全球生物多样性信息设施(GBIF)逾59万种物种记录生成的研究，系统绘制了35个非定法律地位领土、19个受冲突影响国家、20个脆弱国家、18个海洋联合管辖区以及311个国际河流流域的物种丰富度、特有性和灭绝风险。其核心判断是：在这些治理薄弱区域，生物多样性保护不应被视为冲突解决后的“副产品”，而应被用作建立信任、促成对话的“入场券”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 治理真空区不是生态荒漠，而是被低估的物种库\n\n报告最直接的贡献，是用数据证明了一个长期被直觉感知但缺乏量化的现象：全球最不稳定的政治地理单元，恰恰承载着不成比例的生物多样性负担。这并非因为冲突本身有益于生态，而是因为这些区域往往地形复杂、人类开发密度低，客观上保留了相对完整的栖息地。更重要的是，这些区域中许多物种的分布范围极其狭窄——即所谓的“特有物种”——这意味着一旦栖息地被破坏，物种灭绝几乎是不可逆的。\n\n世界银行的数据显示，在这些治理薄弱区域，不仅物种数量可观，而且许多物种面临极高的灭绝风险。以非定法律地位领土为例，这些区域的主权归属存在争议，导致没有任何一方有动力或能力实施长期保育规划。\n\n[... middle omitted ...]\n\nfund、资管机构、战略咨询、智库等朋友，期待与你交流。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n生物多样性保护的“隐形战场”\n\n数据是和平的桥梁\n\n---\n\n为什么说“数据”是保护生物多样性的关键？\n\n最近读了一份世界银行的研报，讲的是在冲突地区、边界模糊区、脆弱国家里，怎么保护那些濒危物种。\n\n🌍 一个残酷的事实：\n\n全球物种灭绝速度已加速到自然水平的1000倍。而在那些战乱、治理薄弱、主权争议地区，保护工作几乎陷入停滞——不是不想管，是没有可靠数据。\n\n🔍 研报用了一个聪明的方法：\n\n借助全球生物多样性信息平台（GBIF）的开放数据，加上机器学习，绘制了近60万种物种的分布图。覆盖范围包括：\n- 35个法律地位未定区域\n- 19个冲突影响国家\n- 20个脆弱国家\n- 18个海洋联合管辖区\n- 311个国际河流流域\n\n📊 发现什么？\n\n这些“灰色地带”恰恰是许多濒危物种的栖息地。比如一些边界河流流域，鱼类和两栖动物种类丰富，但各国数据不统一、监测断档，保护工作根本无从下手。\n\n💡 一个有意思的视角：\n\n研报认为，生物多样性保护反而可以成为“信任建设”的切入点。当各方围绕共同的气候韧性、可持续生计目标协作，数据就成了对话的基础。\n\n比如，尼罗河流域、湄公河流域的跨国合作，就是典型案例。\n\n🧠 我的启发：\n\n[... middle omitted ...]\n\nange. Effective conservation requires urgent, coordinated global action, as ecosystems and species habitats often transcend national borders. Collaboration among governments, industries, and c\n\n[... middle omitted ...]\n\nnd Implementation Plan for the Zambezi River Basin (ZAMSTRAT). https://zambezicommission.org/publication/integrated-water-resources-management-strategy-and-implementation-plan-zambezi-river-1 (Accessed 11 December 2024)."
  },
  {
    "id": "R013",
    "title": "世界银行：国企不是就业杀手，但它在悄悄改变市场规则",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：国企不是就业杀手，但它在悄悄改变市场规则\n\n关于国有企业，一个长期流行的叙事是：它们效率低、拿补贴、挤压民营空间。但世界银行一份针对巴西的最新研究，给出了一个更复杂、也更值得决策者认真对待的判断。\n\n这份题为《巴西的国有企业：对就业和商业活力的影响》的工作论文，利用一个覆盖全巴西正式就业的独特数据集，系统检验了国有及国有参股企业（Businesses of the State, BOS）在经济中的真实角色。结论是：国企确实支付了更高的工资，私有化也确实会压低工人收入。但在就业总量层面，并没有发现私有化导致大规模裁员的稳健证据。更深层的矛盾在于，国企的存在与行业集中度上升、年轻企业占比下降、企业退出率降低同时相关。\n\n这意味着什么？国企不是简单的“好”或“坏”，它正在以一种更隐蔽的方式重塑市场的竞争规则。对于正在讨论“增强国有经济核心功能”与“促进民营经济发展壮大”如何平衡的中国读者，这份报告的视角和方法论，都值得细读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 国企支付的工资溢价是真实的，但私有化的冲击同样清晰\n\n报告首先回答了一个基础问题：在巴西，国企是否支付了更高的工资？答案是肯定的。在控制企业和工人特征后，国企的工资溢价约为18.5%。但一旦加入工人固定效应，控制工人自选择进入国企的偏差后，这个溢价下降至4.5%。这意味着，国企高工资很大一部分来自它们吸引了更优秀的工人，而非纯粹的“体制红利”。\n\n更直接的证据来自私有化事件。报告采用事件研究法估计，私有化发生后，留在原企业的工人在头两年内相对工资下降约10%。值得注意的是，私有化企业倾向于解雇教育水平更高、年龄更大、工龄更长的员工。这暗示了私有化后企业的人力资本结构调整：从“养人”转向“用人”。\n\n> **KC评论：** 10%的工资降幅不是一个\n\n[... middle omitted ...]\n\ne fund、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n巴西国企研究：工资高但影响市场活力\n\n国企的隐形影响力\n\n投行研报用巴西数据，拆解了国企（BOS）对就业和市场的影响，结论很有意思👇\n\n1️⃣ 国企确实给高工资\n- 国企员工工资比私企高18.5%\n- 但控制员工个人能力差异后，真实溢价只有4.5%\n- 说明高工资更多是因为国企吸引了更优秀的人，而非纯粹“发钱多”\n\n2️⃣ 私有化后工资下降\n- 私有化事件后，员工工资两年内下降约10%\n- 被裁的员工中，学历高、年龄大、工龄长的比例更高\n- 但研究没有发现私有化导致总就业人数减少的强证据\n\n3️⃣ 国企对市场活力的影响\n- 国企占比高的行业：新企业进入少、退出率低、市场集中度高\n- 但同时：就业创造率更高，净就业变化为正\n- 结论：国企可能抑制了行业竞争和创业活力，但稳定了就业\n\n4️⃣ 国企的“创新”特征\n- 国企（尤其是参股企业）使用更多技术类员工（创新指标）\n- 规模更大，就业增长也更快\n\n📌 核心发现：国企在提供高薪和稳定就业的同时，可能以牺牲市场活力和竞争为代价。政策制定需要权衡这其中的利弊。\n\n#学习笔记\n\n[source_mineru.md]\nPolicy Research Working\n\n[... middle omitted ...]\n\nwned or mixed enterprises and with indirect state participation in competitive sectors. The paper looks at their impact through two connected perspectives: employment and business dynamism. Fi\n\n[... middle omitted ...]\n\nf employees. The results indicate that privatized BOS have a wage premium of 0.04 log points larger than their non-privatized peers, the difference between the two groups is not statistically different from zero. $^{18}$"
  },
  {
    "id": "R014",
    "title": "世界银行：家暴数据被严重低估，一个简单的问卷顺序改变能提升57%的披露率",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：家暴数据被严重低估，一个简单的问卷顺序改变能提升57%的披露率\n\n在发展中国家，家庭暴力（IPV）的数据收集一直面临一个核心困境：受害者不愿对调查员开口。传统认为，计算机辅助自填问卷（ACASI）能通过匿名性提高披露率，但在文盲率高达93%的农村地区，这种方法可能适得其反——受访者根本看不懂选项。世界银行最新的一份政策研究论文，基于巴基斯坦旁遮普省6135名已婚女性的实地实验，给出了一个反直觉的答案：问题的关键不在于用什么工具，而在于先问什么。当受访者先用ACASI私下回答敏感问题后，再与调查员面对面访谈时，家暴披露率提升了41%到57%。这意味着，数据收集的“第一问”决定了真相的边界。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 高文盲率不是ACASI的障碍，设计粗糙才是\n\n这份报告的第一个核心判断，直接挑战了此前学界的主流认知。此前，Park等人2021年在利比里亚和马拉维的研究发现，ACASI在农村地区存在严重的理解障碍——约三分之一的受访者连训练题都答错。这导致了一个危险的推论：ACASI提高的披露率可能不是更真实，而是更混乱。\n\n世界银行的团队没有止步于此。他们做了两件事。第一，重新设计了ACASI的视觉界面。他们没有使用抽象的色块或形状，而是与当地调查员合作，开发了与频率选项（“从未”“一两次”“三次以上”）高度关联的图片。第二，他们设计了一个随机实验：对一半受访者，ACASI中的频率选项按升序排列；对另一半，按降序排列。如果受访者只是在“瞎选”第一个选项，那么顺序变化会显著影响结果。\n\n结果令人信服：两个顺序组之间，所有六种暴力类型（推搡、掌掴、扭臂、拳击、窒息、持械威胁）的报告率均无统计显著差异。这意味着受访者真正理解了选项的含义。\n\n> **KC评论：** 这对所有在发展中国家做田野调查\n\n[... middle omitted ...]\n\n叙事、数据与图表，观测边际变化。扫码交流，期待与你一起探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 亲密暴力数据收集：先私下问，更敢说\n\n**先私问，后公开**\n\n**先匿名回答，再面对面，披露率提高41%-57%**\n\n---\n\n巴基斯坦农村的调研，给了我一个很实用的启发。\n\n6,000多位已婚女性参与，93%不识字。研究想解决一个经典难题：面对面的家暴调查，受访者因为害怕、羞耻、家里有人偷听，往往不敢说实话。\n\n他们做了两件事：\n\n**1. 把自填问卷改成音频+图像版**\n\n不识字没关系。她们戴上耳机听问题，屏幕用图片表示“从没”“一两次”“三次以上”。测试发现，就算把选项顺序打乱，回答也没显著差异。理解率很高。\n\n**2. 先私下回答，再面对面聊**\n\n一半人先通过ACASI（音频电脑自填）回答两个问题，再被访员面对面问同样的问题；另一半反之。\n\n结果：先私下答过的人，后续当面报告家暴的频率高出41%-57%。先打开一个安全的开口，后面就容易说真话了。\n\n这个逻辑不只在调研里适用。任何敏感话题——心理健康、性健康、职场霸凌——先给一个低门槛、低暴露的入口，后续的坦诚度会大幅提升。\n\n**一点思考**：我们设计问卷、访谈、甚至日常对话时，是不是也可以先给对方一个“安全的匿名空间”？\n\n---\n\n#学\n\n[... middle omitted ...]\n\nompare disclosure of intimate partner violence when questions were asked face-to-face first versus through audio computer-assisted interviewing first. The findings show that despite high illit\n\n[... middle omitted ...]\n\n Malawi. NBER Working Paper 29584.\n\nPeterman, A., Dione, M., Le Port, A., Briaux, J., Lamesse, F. and Hidrobo, M. (2024). Disclosure of violence against women and girls in Senegal. World Bank Economic Review Forthcoming."
  },
  {
    "id": "R015",
    "title": "世界银行：社区健康工作者推高避孕针用量70%，但总覆盖率未变",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：社区健康工作者推高避孕针用量70%，但总覆盖率未变\n\n一项来自布隆迪农村的随机实验显示，授权社区健康工作者在常规家访中提供新型避孕注射剂，使注射量飙升约70%。然而，这项看似成功的干预并未提升总体避孕覆盖率——因为女性从长效避孕方法（皮下埋植、宫内节育器）显著转向了这种更方便的注射剂。这一发现对全球公共卫生政策和资源分配提出了一个根本性问题：我们追求的是服务可及性，还是实际保护效果？\n\n这份由世界银行研究团队完成的政策研究工作论文（编号11074），通过集群随机对照试验和卫生中心行政数据，揭示了上述反直觉的结论。对于关注新兴市场医疗体系改革、公共卫生项目评估以及行为经济学的读者而言，这份报告提供了一个难得的“自然实验”案例，其结论的严谨性值得深入解读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 真正的增量不在“新增用户”，而在“用户迁徙”\n\n这份报告最核心的发现是：干预组卫生中心辖区内的新型避孕注射剂（Sayana Press）月均使用量比对照组高出约13单位，增幅约70%。这一增长在统计学上高度显著，且贯穿了社区健康工作者的理论培训和实践认证两个阶段。在认证后，由社区健康工作者在家访中提供的续针注射量同样出现了强劲且显著的增长。\n\n然而，关键问题在于“所以呢”？当研究者将目光投向所有避孕方法的总体使用量时，发现干预并未产生统计学上的显著变化。这意味着，这70%的增长并非来自新增的避孕用户，而主要是原有用户的方法转换。报告明确指出，观察到了向长效避孕方法（尤其是皮下埋植和宫内节育器）的显著替代效应，月均下降约2.7单位。考虑到不同方法的有效保护时长（Sayana Press为3个月，皮下埋植可达3-5年），探索性估算表明，干预在整个分析期内并未净增加避孕覆盖人月数。\n\n> **KC评论：** 这是典型的\n\n[... middle omitted ...]\n\n交流，期待与你深入探讨这份报告及其对全球健康投资格局的启示。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n布隆迪农村避孕实验，一个反直觉发现\n\n家庭访视的意外效果\n\n---\n\n**1. 一个看似聪明的设计**\n\n某外资投行在布隆迪农村做了一个实验：培训社区健康工作者（CHW），让他们在常规家访时，帮女性注射新一代避孕针Sayana Press（皮下注射，操作简单，保护期3个月）。\n\n核心逻辑：女性不用专门跑卫生中心，省去路程、时间、带娃的麻烦，更重要的是——家访是常规服务，邻居不会因为看到CHW进家门就猜到她去避孕，隐私性提升。\n\n**2. 结果很反直觉**\n\n干预确实有效：每月注射量比对照组增加了约70%（约13针/卫生中心覆盖区）。\n\n但——总避孕覆盖率没有显著变化。\n\n为什么？因为女性**从长效避孕方法（皮下埋植、宫内节育器）换到了避孕针**。每月约2.7个长效方法被替代，基本抵消了新增的注射量。\n\n**3. 哪里出了问题**\n\n研究推测（注意是推测）：CHW家访时，可能更倾向于推荐自己熟悉、能操作的避孕针，而不是需要转诊到卫生中心才能做的长效方法。女性也更容易接受“立刻能打一针”的方案，而不是“需要去一趟卫生中心”的植入或上环。\n\n**4. 一个值得思考的视角**\n\n不是所有“让避孕更方便”的措施，都会提\n\n[... middle omitted ...]\n\nncrease of approximately 70 percent in the administered quantity of these injections, which provide average protection for three months. However, the results suggest that the intervention does\n\n[... middle omitted ...]\n\nation and development review 43(Suppl Suppl 1), 166–191.\n\nUnited Nations (2022). World Family Planning 2022: Meeting the changing needs for family planning: Contraceptive use by age and method. UN DESA/POP/2022/TR/NO. 4."
  },
  {
    "id": "R016",
    "title": "世界银行：中东产油国的燃料补贴，正在成为全球减排的最大盲区",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：中东产油国的燃料补贴，正在成为全球减排的最大盲区\n\n全球气候治理的讨论，长期聚焦于碳税、碳市场、可再生能源补贴这些“正面清单”工具。但一份由世界银行发布的最新实证研究，却将矛头指向了一个被严重低估但规模惊人的反向变量：化石燃料补贴。\n\n这份由Hamid Mohtadi和Zeljko Bogetic共同完成的工作论文，基于41个国家2011-2018年的面板数据，对中东和北非（MENA）地区的脱碳政策效果进行了严谨的计量分析。其核心结论极为明确且具有政策颠覆性：在中东产油国，石油补贴不仅直接且显著地推高了二氧化碳排放，更关键的是，**削减这些补贴，并不会对短期或长期的经济增长造成任何可统计的负面影响。**\n\n这意味着，全球气候政策工具箱里，最优先的“低成本高收益”选项，或许不是尚未成熟的碳捕集技术，也不是充满争议的碳边境调节机制，而是直接拆除那些由本国财政支付的、扭曲能源价格的补贴体系。世界银行这份报告，为全球投资者和产业决策者提供了一个重新评估中东资产风险与机遇的硬核分析框架。\n\n> **KC评论：** 这份报告最值得关注的不是“补贴有害环境”这个常识，而是它用数据证明了一个反直觉的结论：对于中东产油国，取消补贴在经济上几乎没有代价。如果这个结论被当地政策制定者接受，整个中东的能源定价逻辑、财政收支结构乃至主权信用评估框架，都可能需要重写。完整报告对样本选择、内生性处理和分组回归的细节，是理解这一结论稳健性的关键。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 补贴的排放“放大器”效应，只存在于中东产油国，而非全球\n\n报告的第一个核心发现，是石油补贴对碳排放的推动作用具有显著的区域特异性。在全样本（41国）和中东非样本中，石油补贴与二氧化碳排放之间的正相关关系并不显著。但一旦将样本限定为“中东非地区的石油生\n\n[... middle omitted ...]\n\n略咨询机构的最新研究，观测全球边际变化，期待与你的深度交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东减碳：补贴才是关键\n\n🔍 补贴才是排放的元凶\n\n某外资投行最新研报，用41国数据拆解MENA（中东北非）地区的减碳政策效果。结论很有意思：\n\n1️⃣ 石油补贴是排放的“加速器”\n对MENA产油国来说，石油补贴显著推高CO2排放，主要通过能源消费路径。即使控制了消费效应，补贴对碳排放仍有直接净影响（可能来自制造业等其他环节）。\n\n2️⃣ 补贴≠经济增长\n关键发现：石油补贴对短期或长期经济增长都没有显著影响。所以减补贴不会拖累经济——对包括产油国在内的所有国家都成立。\n\n3️⃣ 减补贴 vs 碳税\n在MENA产油国，化石燃料补贴规模巨大，导致碳价被严重压低。单纯加碳税效果有限，因为不先消除补贴，碳税无法有效改变相对价格。研报暗示：先减补贴，再加碳税，才是合理顺序。\n\n4️⃣ 产油国更特殊\n对比41国整体、MENA整体、MENA产油国三组，石油补贴的负面排放效应只对MENA产油国显著。火炬燃烧（flaring）也是它们的排放来源。\n\n💡 一个值得思考的问题：如果减补贴不影响增长，为什么各国还在补贴？\n\n#学习笔记\n\n[source_mineru.md]\n# Decarbonization in MENA Cou\n\n[... middle omitted ...]\n\nThese new estimates contribute to the literature seeking to understand the pros and cons and effectiveness of various policy instruments in promoting decarbonization, with particular focus on \n\n[... middle omitted ...]\n\ntd><td>369</td><td>5.06E-09</td><td>1.34E-08</td><td>0</td><td>9.97E-08</td></tr><tr><td>subsidy share of GDP: MENA oil exporters</td><td>369</td><td>4.11E-09</td><td>1.32E-08</td><td>0</td><td>9.97E-08</td></tr></table>"
  },
  {
    "id": "R017",
    "title": "世界银行：不参与决策，可能恰恰是权力的体现",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：不参与决策，可能恰恰是权力的体现\n\n在绝大多数关于女性赋权的研究中，参与决策被视为衡量个体能动性的核心指标。一个常见的假设是：如果你没有在决策桌上发言，你就没有权力。但世界银行最新发布的一篇工作论文，基于对肯尼亚基利菲县农村家庭的混合方法研究，提出了一个挑战直觉的判断：**不参与决策，有时恰恰是权力的体现，而非权力缺失的信号。**\n\n这篇论文的标题本身就极具洞察力——“Deciding Not to Decide”（决定不做决定）。它提醒我们，在理解家庭内部的权力动态时，传统的问卷调查可能严重低估了某些成员的真正影响力，尤其是那些无需开口就能让自己的偏好自动得到满足的人。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 传统的决策参与指标，可能高估了弱势群体的权力，也低估了强势群体的影响力\n\n当我们问“谁决定家庭用水怎么分配”时，如果一个人回答“我没有参与”，研究者通常会将其归为“无权者”。但世界银行的这项研究指出，这种判断存在根本性的盲区。权力不仅仅体现在直接参与决策的过程中，更体现在“有效权力”上——即无论你是否在场，结果都按照你的意愿发生。\n\n在肯尼亚基利菲县的农村家庭中，男性户主往往不需要亲自参与日常的水源选择或家庭开支讨论。他们可能在地里干活，或者在村里闲聊，但家庭用水的最终分配方案，天然地倾向于他们的偏好。这不是因为他们参与了决策，而是因为“默认选项”本身就站在他们一边。长期形成的家庭权力结构和社会规范，使得他们的需求成为家庭的默认设定。\n\n> **KC评论：** 这意味着，当我们用“是否参与决策”来测量权力时，我们实际上是在测量“显性权力”，而忽略了“隐性权力”。对于男性户主而言，不参与决策是一种高效的权力行使方式——他们既节省了时间和精力，又确保了结果符合自己的利益。而对于女性或年轻成员，不参\n\n[... middle omitted ...]\n\n与图表，观测边际变化。扫码交流，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n“不参与决策”≠“没权力”\n\n封面：不决策也是一种权力\n\n副标题：肯尼亚农村家庭的权力游戏\n\n最近读到一篇有趣的研报，讲的是“不参与决策”这件事。\n\n传统上，我们用“是否参与决策”来衡量一个人的自主权。但这篇研报提出了一个扎心的观察：不参与决策≠没权力。\n\n1️⃣ 什么是“有效权力”？\n研报提出两种形式：\n- 代理权力：你知道有人会替你做出符合你意愿的决定，所以干脆不参与\n- 影响权力：通过说服或施压，让决策者按你的意愿行事\n\n2️⃣ 谁在“不参与”？\n研究发现，在肯尼亚Kilifi县的农村家庭中：\n- 丈夫和父亲更可能“不参与”决策，因为他们知道家里的默认选项会偏向自己\n- 这不是懒惰，而是一种权力：不需要花时间和精力去参与，就能得到想要的结果\n\n3️⃣ 女性权力更复杂\n研报特别指出：\n- 已婚女性和丈夫之间的权力关系，不能代表所有女性\n- 在跨代家庭中，婆婆或儿子可能比丈夫更有影响力\n- 年轻媳妇往往最弱势，即使“参与”决策，也可能是被动的\n\n4️⃣ 为什么这很重要？\n如果只用“是否参与决策”来衡量自主权，会低估那些通过“不参与”就能实现目标的人。这提醒我们：\n- 权力可以无声无息地运作\n- 不发声不代表\n\n[... middle omitted ...]\n\nr by proxy and effective power by influence or persuasion. The paper explores indirect ways of pursuing one’s goals when not directly involved in the decision, using unique mixed methods data \n\n[... middle omitted ...]\n\nble>\n\nNotes: Standard errors in parentheses. \\*\\*\\* p<0.01, \\*\\* p<0.05, \\* p<0.1. All estimations are computed using survey weights to address sampling. There is less than one percent of men who live with their in-laws."
  },
  {
    "id": "R018",
    "title": "世界银行：你低估了集群实验中的“大小不均”代价",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：你低估了集群实验中的“大小不均”代价\n\n如果你正在设计一项涉及社区、学校或企业的随机实验，有一个假设可能正在悄悄侵蚀你的统计功效——而这个假设，很多研究者甚至没有意识到自己在做。\n\n世界银行最新一期政策研究工作论文（编号11059）直面了一个长期被实验设计文献回避的问题：当集群规模不均、且不同集群的结局分布本身就有系统性差异时，你的实验可能远没有你想象的那么有力。\n\n这份报告的核心判断是：**忽略集群异质性，不仅会让实验严重“动力不足”，还会让你对结果的信心建立在错误的标准误估计之上。**\n\n这不是一个纯方法论问题。它直接影响你如何判断一项政策是否有效、需要多大样本才能检测到真实效果、以及你该把资源投放到哪些集群上。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 集群异质性不是噪音，而是被系统低估的方差来源\n\n我们通常理解集群实验的方差构成时，会想到两个因素：个体观测之间的独立性假设被打破带来的“设计效应”，以及组内相关系数。但这份报告指出，还有两个被广泛忽略的方差来源：集群规模的差异，以及不同集群之间结局分布的系统性差异。\n\n为了说明这一点，报告做了一个简单的数值模拟。假设有200个集群，其中10个大型集群各含100个单位，其余190个小型集群各含25个单位。大型集群的平均结局是1，小型集群是0。组内相关系数设定为0.5。\n\n如果研究者完全忽略集群异质性，按照标准公式计算，在80%统计功效下能检测到的最小效应量是0.29个标准差。但一旦将集群规模差异纳入考量，实际功效降至69%。如果再考虑结局分布的异质性，真实功效只有48%。\n\n换句话说，你自以为设计了一个80%把握的实验，实际上只有不到一半的概率能检测到你想找的效果。\n\n> **KC评论：** 这个数字差距不是边际性的，而是根本性的。对于任何需要在真实\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n实验设计中的“群组异质性”有多重要？\n\n群组异质性\n\n影响实验统计效力与偏差\n\n最近读了一篇关于局部人口实验设计的工作论文，来自世界银行政策研究工作论文系列。核心是探讨群组实验设计（比如学校、社区、企业）中，不同群组大小和结果分布差异（即“群组异质性”）对实验结果的巨大影响。\n\n**1. 为什么群组异质性这么重要？**\n\n传统实验设计往往假设群组是同质的。但现实中，群组大小可能差很多（比如有的社区10人，有的100人），不同群组的结果分布也完全不同。\n\n论文用模拟证明：如果忽略这种异质性，实验的统计效力会严重不足，也就是本来有效果的实验可能检测不出来。同时，常用的“群组稳健标准误”在高异质性下会高估，导致推断偏保守。\n\n**2. 论文的五个核心贡献**\n\n- **推导了新的大样本分布理论**：在群组异质性下，OLS估计量依然一致且渐近正态，但方差构成复杂，包含群内相关、群组大小差异、分布差异三部分。\n- **给出了明确的统计效力与最小可检测效应公式**：可以直接套用公式计算样本量和效果阈值，特别适合有基线数据但分布不均的情况。\n- **找到了最优的群组分配概率**：如何分配不同“处理饱和度”的群组，能使估计量\n\n[... middle omitted ...]\n\noring cluster heterogeneity may result in severely underpowered experiments and (ii) the cluster-robust variance estimator may be upward-biased when clusters are heterogeneous. The paper deriv\n\n[... middle omitted ...]\n\n) ]\n$$\n\nwhich completes the proof. □\n\n## D.9 Proof of Theorem 4\n\nThis result follows from the fact that conditions (i) and (ii) imply Assumption 5 and thus under the conditions for Theorem 3, Corollary 1 holds. $\\square$"
  },
  {
    "id": "R019",
    "title": "世界银行：乌克兰难民学生融入意大利学校，比想象中更难",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：乌克兰难民学生融入意大利学校，比想象中更难\n\n2022年俄乌冲突爆发后，超过600万乌克兰人被迫流离失所，其中近600万涌入欧盟国家。意大利作为第五大接收国，迎来了约17万乌克兰难民。当这些孩子坐进意大利教室，他们面临的不仅是语言障碍，还有一场关于人力资本能否被挽救的严峻考验。\n\n世界银行最新发布的工作论文《Displaced Learners: Early Integration of Ukrainian Refugee Students into Italy‘s Schools》，利用意大利教育部和INVALSI的行政数据（覆盖2021-22至2023-24学年），首次系统量化了这批特殊学生的教育融入状况。核心判断并不乐观：乌克兰难民学生的入学率显著偏低、缺勤率是本地学生的两倍、语言类科目成绩大幅落后。但报告同时揭示了一个反直觉的发现——尽管成绩不佳，意大利教师却更倾向于推荐乌克兰难民学生进入大学预科方向的高阶教育轨道。\n\n这种“教师乐观主义”能否转化为实际的教育成果，取决于一个关键变量：语言支持与心理干预能否在短期内到位。而世界银行的数据显示，意大利现有的支持体系可能远远不够。\n\n> **KC评论：** 这份报告的价值不在于它揭示了“难民学生成绩差”这个常识，而在于它用行政数据精确量化了差距的规模，并拆解了“教师推荐”与“实际成绩”之间的背离。对于关注欧洲教育政策、移民融入或人力资本投资的读者，这份报告提供了难得的微观证据。完整报告包含了分年级、分科目的详细回归表格，以及教师问卷的一手数据，建议领取原文细读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 入学率缺口：不是难民不想上学，而是系统接不住\n\n报告数据显示，在2022-23学年，乌克兰难民学生在意大利中学阶段的注册总数为8012人，仅占同期意\n\n[... middle omitted ...]\n\n库的朋友一起，追踪全球教育政策与人力资本投资的边际变化。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=“color:#999999;font-size:12px;”>Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n乌克兰难民在意大利读书，成绩到底怎么样？\n\n**封面：** 难民学生成绩单\n\n**副标题：** 语言是最大难关，但老师很看好\n\n---\n\n最近读了一份某外资投行关于乌克兰难民学生在意大利教育融入的研报，数据详实，结论很有启发。\n\n**1. 入学率低，缺课多**\n- 跟意大利本地学生和其他外国学生比，乌克兰难民学生的入学率明显偏低。\n- 缺课天数也更高，几乎是本地学生的两倍（平均46天 vs 23天）。\n- 这背后是语言障碍、心理压力和对未来的不确定性。\n\n**2. 成绩差异：数学强，语言弱**\n- 在需要语言能力的科目（意大利语、英语）上，乌克兰难民学生成绩显著落后。\n- 但在数学上，他们表现不错，甚至不输本地学生。\n- 这说明他们之前的教育基础并不差，语言是主要瓶颈。\n\n**3. 老师却很乐观？**\n- 尽管成绩有差距，但老师们更倾向于推荐乌克兰难民学生进入大学预科方向（高学术轨道）。\n- 相比之下，其他新来的外国学生得到的推荐比例更低。\n- 研报推测，老师可能看到了这些学生更强的学习潜力。\n\n**4. 核心障碍：不止是语言**\n- 语言障碍是第一道坎。\n- 心理健康问题也很突出，战争创伤和流离失所带来的焦\n\n[... middle omitted ...]\n\nabsenteeism, and lower test scores than other students, particularly in subjects requiring language proficiency. Despite these challenges, teachers often recommend Ukrainian refugee students f\n\n[... middle omitted ...]\n\ners arrived in the country after February 2022 and enrolled in Grades 8 through 13. “Ukr Post Feb 2022 is a variable identifying Ukrainian refugees. The “recommended for high-track” variable is relevant for grade 8 only."
  },
  {
    "id": "R020",
    "title": "世界银行：免费短信反而劝退，就业项目招生的“信任悖论”",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：免费短信反而劝退，就业项目招生的“信任悖论”\n\n一个旨在提升青年就业项目参与率的短信提醒，最终却让报名率下降了超过40%。这不是技术故障，而是世界银行一份最新政策研究工作论文揭示的“信任悖论”：当你告诉潜在受益者一个项目“完全免费”时，对于那些不了解你、不信任你的人而言，这句话听起来更像是一个陷阱，而不是一个机会。\n\n这份由Jeannie Annan等六位研究者完成的随机实验，在科特迪瓦针对一个青年就业培训项目PRO-Jeunes进行。实验设计直接且精妙：将2,926名已表达参与意愿的合格青年随机分为三组——第一组仅向青年本人发送“项目免费”的短信提醒；第二组同时向青年及其事先指定的联系人发送相同短信；第三组为对照组，不发送任何短信。结果令人意外：仅联系青年本人几乎没有效果，但一旦将短信同时发送给联系人，男性青年的报名率从43.8%骤降至25.2%，降幅达42.4%；女性青年的报名率也从38.5%降至30.7%，降幅20.2%。\n\n这组数据背后，是一个在发展中国家政策实施中常被忽视、却至关重要的变量：信任。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. “免费”信号在信息不对称的环境下可能反向触发质量怀疑\n\n经济学中有一个经典悖论：当消费者缺乏对产品的充分了解时，低价或免费可能被解读为低质量的信号。Bagwell和Riordan在1991年的经典论文中已经论证了这一机制——高价格可以传递产品质量信号，而免费则可能适得其反。\n\n这份世界银行的研究将这一理论从消费品市场延伸到了公共政策领域。在科特迪瓦的语境下，青年和他们的联系人对于“免费培训”的直觉反应不是“太好了”，而是“为什么免费？是不是没有价值？是不是骗局？”\n\n研究中的定性访谈提供了关键证据：受访者明确表示，短信中“免费”这个信息本身是正面的，但它同时\n\n[... middle omitted ...]\n\n朋友们，期待与你交流如何从这些研究中提炼出可操作的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n免费短信反而劝退？这是真的\n\n**免费≠吸引**\n\n**免费提醒短信，反而让年轻人放弃报名**\n\n某外资投行在科特迪瓦做了一个青年就业培训项目，为了提升报名率，给符合条件的年轻人发短信提醒“项目是免费的”。\n\n结果呢？\n\n1️⃣ **只发给年轻人自己：** 没效果，既不增加也不减少报名。\n\n2️⃣ **同时发给年轻人+他的联系人（父母/配偶等）：** 报名率大幅下降。男性从43.8%降到25.2%，女性从38.5%降到30.7%。\n\n为什么免费反而让人不敢来？\n\n**关键是“信任”**。年轻人已经参加过项目说明会，对机构有了解。但联系人没接触过，突然收到“免费”短信，第一反应是：是不是骗人的？或者质量很差？\n\n**性别差异也很明显：**\n- 男性：不管联系人是男是女，报名率都大幅下降\n- 女性：只有联系人是女性时，才没有被劝退。如果联系人是男性，照样下降\n\n这说明在集体主义文化里，家庭/社交圈对个人决策影响巨大，而“免费”这个信号在缺乏信任时会产生反效果。\n\n**给项目方的启示：** 光说“免费”不够，还得先建立信任，让年轻人的联系人也能了解项目的价值和质量。\n\n你们有没有遇到过类似的情况？明明是福利，反而让\n\n[... middle omitted ...]\n\ngative effect was smaller for women, and null when their contact was also female. Qualitative findings suggest that distrust among unfamiliar contacts contributed to this decline. The study hi\n\n[... middle omitted ...]\n\nontacts, the impact differed by gender: it decreased enrollment for men but increased enrollment for women. Due to the inconclusive nature of these results, we have chosen to focus on the first type of SMS in this paper."
  },
  {
    "id": "R021",
    "title": "世界银行：社会流动性未必直接拉动经济增长，真正起作用的是“谁在向上流动”",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：社会流动性未必直接拉动经济增长，真正起作用的是“谁在向上流动”\n\n社会流动性越高，经济就越发达——这似乎是直觉上最合理的假设。如果一个社会能让更多底层孩子凭借才华而非出身改变命运，人才配置效率提高，创新和增长理应加速。世界银行最新发布的工作论文《Does Social Mobility Affect Economic Development?》却给出了一个远更复杂、甚至反直觉的答案：用不同方式测量社会流动性，得出的结论截然不同。有些情况下，更高的相对流动性反而与更低的收入水平相伴出现。\n\n这份覆盖68个国家、跨越2000至2020年面板数据的研报，真正有价值的判断并非“社会流动性是否重要”，而是“在什么发展阶段、用什么指标衡量，社会流动性与经济增长的关系才成立”。对于正在制定人才政策、教育投资或区域发展战略的决策者来说，这一区分比泛泛谈论“促进社会流动”要关键得多。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 欧洲与中亚地区：只有“高等教育向上流动”与经济增长显著正相关\n\n世界银行将68个国家划分为四个区域进行分组回归，结果差异显著。在欧洲与中亚地区，无论是用代际教育持久性（IP）还是代际教育相关性（IC）来衡量的相对流动性指标，都与人均GDP没有统计上显著的关系。真正与经济增长正相关的，只有一个特定的绝对流动性指标——高等教育向上流动概率（UMHE），即父母未受过高等教育的子女完成高等教育的概率。\n\n这意味着，在欧洲与中亚，社会整体是否“公平”并不直接转化为经济产出。真正产生经济回报的，是那些原本没有高等教育背景的家庭中，子女通过教育实现了向上跃迁的那部分人群。这背后的逻辑是：这批人往往是边际收益最高的群体——他们从低技能岗位转向高技能岗位的劳动生产率提升幅度，远大于高知家庭子女的教育延续。\n\n[... middle omitted ...]\n\n和研究者来说，这些细节远比一个笼统的结论更有价值。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n社会流动性，才是经济增长的隐藏引擎？\n\n封面：社会流动＝经济动力？\n\n社会流动性如何影响国家发展？新研究来了\n\n最近读到某外资投行一份68国跨代教育流动性与经济增长的研报，结论很有意思：**社会流动性和经济发展的关系，远比想象中复杂。**\n\n1/ 什么是“教育流动性”？\n简单说就是：孩子最终的教育水平，多大程度上不受父母教育水平的影响。\n- 流动性高 → 寒门出贵子更容易\n- 流动性低 → 教育代际固化，拼爹效应明显\n\n2/ 核心发现：不同地区，规律完全不同\n🔹 欧洲和中亚：\n只有“向上流动到高等教育”这个指标，与人均GDP正相关。\n简单说：父母没上过大学、孩子上了大学的人越多，经济越强。\n但相对流动性指标（比如教育代际相关性）与经济水平无关。\n\n🔹 拉丁美洲：\n出现了矛盾现象——\n相对流动性越高（社会越平等），人均收入反而越低。\n绝对流动性越高（更多人向上流动），收入越高。\n研报推测：这可能与教育扩张速度快、但质量跟不上有关。\n\n🔹 其他地区：\n呈现混合模式，没有统一规律。\n\n3/ 为什么这很重要？\n当社会流动性高时：\n- 更多有天赋的孩子能进入科研和创新领域\n- 劳动力市场更高效\n- 技术进步更快（社会回报\n\n[... middle omitted ...]\n\nh gross domestic product per capita in Europe and Central Asia, but relative mobility indicators are uncorrelated with country income. In Latin America, higher relative mobility is associated wi\n\n[... middle omitted ...]\n\n![](images/7d9e4862cff917286a5d1de94f68ff2f783f5546933d2ddfc807525e88c8dfee.jpg)  \nNote: The figure plots the posterior densities in the Bayesian Model Averaging linear regression for each of the four mobility indices."
  },
  {
    "id": "R022",
    "title": "世界银行：财政规则的效果，取决于你是在什么时刻定下的",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：财政规则的效果，取决于你是在什么时刻定下的\n\n一个被全球108个国家实践了数十年的政策工具，其效果并不总是如预期般线性累积。世界银行最新发布的工作论文，通过对1984年至2012年间跨国数据的细致分析，给出了一个反直觉的结论：财政规则能否真正约束政府行为，不仅取决于规则本身的设计，更取决于它是在什么经济与政治背景下被“按下启动键”的。\n\n这份报告的核心判断值得所有关注宏观政策与主权信用的人认真对待：**财政规则的长期有效性，高度依赖其采纳时的初始条件。** 在发达经济体和制度质量高的国家，规则的效果会随时间不断增强；但在新兴市场和发展中经济体，尤其是那些制度薄弱的国家，规则的效果往往在经历短期提振后便逐渐衰减。这意味着，对于许多正在或准备引入财政规则的国家而言，真正重要的不是是否拥有规则，而是规则诞生时那个“原点”的状态。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 财政规则并非一劳永逸：效果随时间分化的两个路径\n\n报告首先确认了一个基础结论：财政规则的采纳确实会改善初级财政余额。在十年时间窗口内，初级余额平均改善幅度约为GDP的1%。但这只是一个整体均值，掩盖了背后深刻的异质性。\n\n当研究者将样本区分为发达经济体与新兴市场和发展中经济体时，分化的图景立刻显现。在发达经济体中，规则的效果呈现出一种“信任积累”的特征：初期改善幅度有限，但随着时间推移，效果持续增强。这符合直觉——规则的公信力需要时间来建立，市场参与者、选民和官僚机构对约束的适应与内化是一个渐进过程。\n\n而在新兴市场和发展中经济体，情况截然不同。规则在采纳后的头几年确实带来了明显的财政改善，但这种积极效应在中期开始减弱，并在长期几乎完全消失。报告将此归因于制度质量的差异。进一步分析证实：在制度质量高的国家，无论其发展阶段如何，财政规则都能持续\n\n[... middle omitted ...]\n\n整研报解读与原始图表，与我们一起探讨财政规则背后的真实逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n财政纪律不是一劳永逸的事\n\n财政纪律的长期赛跑\n\n它拼的不是起点，而是制度韧性\n\n某外资投行用108国1984-2012年数据，研究了财政规则采纳后的动态效果。结论很有意思：规则有效，但效果走向取决于你的“出身”和“当下”。\n\n1️⃣ 时间是个变量\n- 财政规则整体能改善财政平衡，10年内约提升1% GDP。\n- 但效果不是线性的。发达国家、强制度国家：效果随时间增强。\n- 新兴市场、低收入国家：短期有效，中期后效果逐渐消失。\n\n2️⃣ 起点决定终点\n- 经济衰退期匆忙上马的规则，长期效果差。\n- 政治高度集权下推行的规则，也容易中途乏力。\n- 相反，经济平稳期、政治共识强时引入的规则，能持续发挥作用。\n\n3️⃣ 制度是加速器，不是万能药\n- 强制度国家：规则效果随时间累积，像复利。\n- 弱制度国家：规则效果像脉冲，短期冲高，长期回归。\n- 但研报也指出：好制度不是唯一条件，初始环境同样关键。\n\n4️⃣ 对新兴市场的启示\n- 规则设计需要匹配本国制度能力。\n- 在经济下行时强行推规则，可能适得其反。\n- 政治共识比技术设计更重要。\n\n所以，财政规则的长期成功，更像一场“制度基建”：需要好的时机、共识基础和执行\n\n[... middle omitted ...]\n\nal rules generally improve the primary balance, their effects depend on the time horizon under consideration and the context of adoption. In advanced economies and countries with strong politi\n\n[... middle omitted ...]\n\non, DC.\n\nWyplosz, C. 2013. “Fiscal Rules: Theoretical Issues and Historical Experiences.” In Fiscal Policy After the Financial Crisis, edited by Alesina, A. and F. Giavazzi, 495-525. Chicago: University of Chicago Press."
  },
  {
    "id": "R023",
    "title": "世界银行：卫星+AI正在解决一个核心测量难题",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：卫星+AI正在解决一个核心测量难题\n\n当国际组织、各国政府和慈善基金会试图追踪“贫困是否在减少”时，他们面临一个几乎无解的矛盾：最需要数据的地方，恰恰最缺少数据。\n\n传统家庭调查耗时、昂贵，在非洲许多国家，十年才能更新一次。而当你终于拿到数据，它可能已经过时了。更棘手的是，这些调查通常只能在省级层面代表总体，无法告诉你某个村庄或街区的真实状况——而反贫困干预恰恰需要落到这个级别。\n\n世界银行联合斯坦福大学发布的最新政策研究工作论文，试图用卫星影像、公开地理特征和新型深度学习架构，回答一个关键问题：在数据稀缺的环境中，我们能否以低成本、高频率、街区级精度来测量家庭财富？\n\n答案是：可以，而且比以往任何时候都更接近实用化。\n\n这份报告的核心判断是：基于Transformer架构的深度学习模型，在四个非洲国家的测试中，不仅能够精准捕捉国家内部的财富空间差异，还能预测十年间的财富变化。更令人意外的是，仅需每个行政区域10户家庭的样本数据，模型就能达到接近全样本训练的精度。\n\n这不仅仅是技术论文的进展。它意味着，对于全球数以亿计生活在数据空白地带的人口，我们终于有了一个可行的、动态的财富监测工具。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 传统测量方法正在成为发展目标的“瓶颈”\n\n联合国可持续发展目标1“消除贫困”的2030年截止日期正在逼近。但一个尴尬的现实是，对于许多低收入国家，我们甚至无法准确知道贫困是否在减少。\n\n家庭调查是官方贫困测量的基石。但它的局限性正在被越来越多地讨论：调查需要专业能力、后勤支持，往往只能在较大地理尺度上代表总体。这意味着，在村庄或街区层面——反贫困干预最需要精准定位的地方——传统调查几乎无能为力。\n\n更关键的是，调查的频率。在许多非洲国家，全国性的家庭调查每五到十年才进行一次。这\n\n[... middle omitted ...]\n\n数据效率实验、以及不同卫星传感器的性能对比，都在完整报告中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n卫星+AI，贫困测量终于不用走街串巷了\n\n精准测量财富，数据却难拿\n\n传统家户调查又贵又慢，非洲很多国家根本做不到全面普查。但贫困地图得画，扶贫政策要落地，怎么办？卫星遥感+深度学习，这几年成了新出路。\n\n这篇斯坦福+世界银行团队的研报，用4个非洲国家、1200万家庭的数据，直接验证了新一代Transformer模型的效果。结果很惊喜：\n\n1️⃣ 精度碾压传统方法\n用单一卫星影像+Transformer，在马拉维、莫桑比克、马达加斯加分别能解释83%、70%、62%的财富差异。这比之前常用的CNN模型强出一截。\n\n2️⃣ 数据不够也能用\n人工把训练样本砍到10%，模型精度才明显下降。更关键的是，每个区域只要能拿到10户家庭的数据，模型表现就接近用全部家庭数据训练的结果——这意味着实地调查成本可以大幅压缩。\n\n3️⃣ 城市里也能看清街道级差异\n以前卫星测贫困主要看城乡差异，但城市内部贫富差距更大。这篇用马拉维两个城市的精准普查数据，证明Transformer能识别到街区甚至街道级别的财富分布。\n\n4️⃣ 还能追踪财富变化\n同一地点、间隔10年的两次普查数据，模型竟然能预测出财富变化。这个能力之前一直没被验证过，\n\n[... middle omitted ...]\n\nsed deep learning approaches using detailed household census extracts from four African countries to accelerate progress toward comprehensive, fine-scale, and dynamic measurement of asset weal\n\n[... middle omitted ...]\n\nPerez, A., Driscoll, A., Azzari, G., Tang, Z., Lobell, D., Ermon, S., Burke, M., 2020. Using publicly available satellite imagery and deep learning to understand economic well-being in africa. Nature communications 11, 2"
  },
  {
    "id": "R024",
    "title": "世界银行：刚果金农村WASH项目改善了设施，但未能减少儿童腹泻",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：刚果金农村WASH项目改善了设施，但未能减少儿童腹泻\n\n一份来自世界银行的随机对照试验，评估了刚果民主共和国国家级农村水、环境卫生与个人卫生项目的实际效果。结论清晰且令人深思：项目成功建立了村级WASH委员会，提升了改善水源和卫生设施的使用率，但这些变化并未转化为儿童腹泻率的下降或身高发育的改善。这不仅仅是关于一个项目的评估，它挑战了国际发展领域一个核心的因果假设：基础设施改善是否必然带来健康改善。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 项目本身是成功的：社区机构与基础设施确实得到了有效改善\n\n这份报告最坚实的结论在于，干预措施在“过程指标”上取得了显著成效。在项目实施3.6年后，干预组村庄的WASH机构指数得分比对照组高出0.4分。更具体地说，干预组中拥有活跃WASH委员会的村庄比例比对照组高出21个百分点。家庭层面，使用改善水源的比例提高了24个百分点，使用改善卫生设施的比例提高了18个百分点。居民对水治理的感知也更为积极。这些数据表明，一个设计良好的社区驱动项目，在冲突频发、治理薄弱的刚果金农村地区，能够有效地建立起可持续的社区治理结构和基础设施。\n\n> **KC评论：** 这意味着，对于许多发展项目而言，最大的挑战往往不是“做什么”，而是“如何做”才能落地并持续。刚果金的这个项目证明了，通过社区动员、资金支持和制度建设的组合拳，可以在复杂环境中实现机构和设施的实质性改变。但这也引出了更关键的问题：这些改变是否足够？\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 健康结果未改善：基础设施与健康之间的“黑箱”依然存在\n\n尽管过程指标亮眼，但研究的核心健康指标——儿童腹泻患病率和身长别年龄Z评分——在干预组和对照组之间没有统计学上的显著差异。这是一个典型的“过\n\n[... middle omitted ...]\n\n际主流叙事、数据与图表，观测边际变化。我们期待与您继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n刚果金这个国家级水卫项目，效果出乎意料\n\n**基础设施上去了，腹泻却没降**\n\n一个持续3.6年的随机对照试验，结果有点反直觉\n\n---\n\n**1. 项目做了什么？**\n\n刚果金政府+联合国儿童基金会搞的“健康村”项目，给每个村大约7000美元经费，包括：\n- 修水井/供水设施\n- 建厕所\n- 成立村水卫委员会\n- 搞卫生习惯宣传\n\n目标是让村里达到7条标准，比如80%的人用上安全水、80%家庭有卫生厕所。\n\n**2. 效果怎么样？**\n\n3.6年后，干预组和对照组对比：\n✅ 水卫机构评分高0.4分\n✅ 有活跃水卫委员会的村多21个百分点\n✅ 用上改善水源的家庭多24个百分点\n✅ 用上卫生厕所的家庭多18个百分点\n✅ 村民对水务治理的感知更正向\n\n❌ 儿童腹泻率没降\n❌ 儿童身高发育（年龄别身长Z评分）没改善\n\n**3. 为什么基础设施好了，健康却没变？**\n\n这是目前全球水卫领域最头疼的问题之一。推测几个原因：\n- 基础设施改善不等于持续使用\n- 光有硬件，行为改变可能不够彻底\n- 环境中的病原体暴露可能依然很高\n- 项目覆盖的只是村级改善，家庭层面的卫生习惯可能没跟上\n\n**4. 这个研究特别在哪**\n\n[... middle omitted ...]\n\nnd sanitation institutions. The program combined (i) funds for latrine and water upgrades, (ii) institutional strengthening activities, and (iii) behavior change campaigns. In 2018, the progra\n\n[... middle omitted ...]\n\nrials, non-pharmacological treatments, herbal interventions, and pragmatic trials. Additional extensions are forthcoming: for those and for up-to-date references relevant to this checklist, see www.consort-statement.org."
  },
  {
    "id": "R025",
    "title": "世界银行：电价上涨1%，高能耗无节能措施企业裁员1.5%",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：电价上涨1%，高能耗无节能措施企业裁员1.5%\n\n2019年到2023年，全球经历了疫情冲击、供应链断裂、俄乌冲突引发的能源价格剧烈波动。当各国政府忙着发放能源补贴、央行盯着通胀数据时，一个被忽视的问题正在发展中国家蔓延：电价上涨正在悄悄改变企业的雇佣决策，而大多数企业并没有做好准备。\n\n世界银行最新政策研究论文给出了一个极具政策含义的发现：电价每上涨1%，那些处于高能耗行业且没有采取节能措施的企业，就业规模会减少约1.5%。这个数字不是理论推演，而是基于24个新兴市场和发展中经济体、超过6万家企业数据的实证结果。\n\n更值得关注的是，这份报告揭示了一个反直觉的现象：同一批企业在电价上涨后，其销售额和劳动生产率反而可能上升。这意味着企业并非被动承受冲击，而是通过两种方式调整——将成本转嫁给消费者，以及用资本替代劳动力。但问题是，那些没有节能措施的高能耗企业，在就业端的代价最为惨烈。\n\n这不是一个关于能源转型的远期故事，而是当下正在发生的结构性调整。对于投资新兴市场、关注全球供应链的企业决策者而言，理解这种调整的传导机制，比猜测下一个季度GDP数据更有价值。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 电价冲击的传导路径：不是所有企业都受伤，但受伤的企业很致命\n\n报告的核心贡献在于区分了两种异质性：行业层面的能源强度和企业层面的节能措施。这种“交叉分类”让分析从泛泛而谈的“能源涨价影响企业”推进到可操作的判断层面。\n\n基准回归结果相当清晰。在控制国家、时间、行业和规模等固定效应后，电价每上涨1%，整体样本中企业的销售额和劳动生产率反而显著上升。这听起来像是好消息，但报告特意指出，这个正向效应在加入不同稳健性检验后并不稳定。更关键的是，当引入行业能源强度和企业节能措施两个交互项后，真实的图景才浮现出来。\n\n高能\n\n[... middle omitted ...]\n\n评论，追踪全球能源、经济和市场的边际变化。我们期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n电费涨了，谁最受伤？\n\n📊 电费涨1%，用工减1.5%\n\n最近读了一份世界银行的研报，发现电费上涨对企业的冲击比想象中更具体。不是所有企业都扛得住。\n\n1/ 核心发现\n电费每涨1%，那些没做节能改造的高能耗企业，用工量会减少约1.5%。这个数据来自24个新兴市场2019-2023年的企业调查，样本量近2万。\n\n2/ 为什么？\n高能耗企业本来利润就薄，电费一涨，成本压力直接传导到用工上。而那些提前做了节能改造的企业，抗冲击能力明显更强。\n\n3/ 有意思的反差\n研报还发现，电费上涨后，企业的销售额和生产率反而可能上升。推测是：企业把成本转嫁给了消费者，同时用更少的人干更多的活。但这在统计上不是所有模型都成立。\n\n4/ 谁最危险？\n制造业、重工业这些能源密集型行业，如果之前没做节能投入，现在就面临两难：要么涨价丢客户，要么裁员降成本。\n\n5/ 启示\n节能改造不只是环保口号，在能源价格波动时，它直接决定企业能不能保住岗位。对于政策制定者来说，支持企业做能效升级，比事后补贴更值得。\n\n你觉得在当下能源价格波动周期里，企业应该优先做节能改造，还是先保现金流？\n\n#学习笔记\n\n[source_mineru.md]\n# En\n\n[... middle omitted ...]\n\n(self-reported in the Business Pulse Survey). The findings show that increasing electricity prices by 1 percent reduces employment at firms in energy-intensive industries that did not adopt en\n\n[... middle omitted ...]\n\nS</td></tr></table>\n\nRobust standard errors in parentheses\n\\*\\*\\* p<0.01, \\*\\* p<0.05, \\* p<0.1\nWeighted by country sample size\nControls for size[1], age, wave, and subsector [1] Sales if dependent variable is employment"
  },
  {
    "id": "R026",
    "title": "世界银行：女性在高端房产的拥有率不足20%，但税收政策对她们更不公平",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：女性在高端房产的拥有率不足20%，但税收政策对她们更不公平\n\n世界银行最新发布的一份基于阿根廷大型城市行政税收数据的研究，揭示了一个在财产税讨论中常被忽视的维度：性别。这份报告的核心发现并非简单的“女性缴税更少”或“女性更守规矩”，而是一个更微妙、更具政策含义的判断：在财产所有权上存在显著的性别财富差距，但现行的财产税制度，因其累退性结构，反而对拥有较低价值房产的女性群体构成了更高的有效税率。税收执法的软性干预措施，如催缴信，对男女效果相似，并未展现出显著的性别差异。这意味着，解决财产税领域的性别公平问题，重点不在于调整执法手段，而在于审视税制设计本身，以及更根本的财富创造与分配结构。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 财产所有权的性别鸿沟在高端市场急剧拉大，低端市场相对均衡\n\n报告利用阿根廷特雷斯德费布雷罗市超过10万条房产的行政数据，首次在拉美地区清晰描绘了财产所有权与房产价值分布之间的性别关系。研究将房产所有者分为女性、男性和共同所有三类。在房产价值分布的最底端40%区间，所有权分布相当均衡，女性、男性和共同所有各占约三分之一。然而，一旦越过这个分水岭，女性所有权的比例便急剧下降。在房产价值最高的前1%区间，共同所有占50%，男性占约30%，而女性的所有权比例跌至20%以下。\n\n这一发现印证了全球范围内关于性别财富差距的普遍认知，但其贡献在于用精确的行政数据而非抽样调查，量化了这一差距在财产税这一具体税种上的表现。报告没有深入探讨造成这一差距的根源——是女性创业和职业发展受限导致的收入差距，还是信贷获取上的性别歧视，抑或是继承和赠与中的性别偏好——但它为后续研究指明了方向。对于政策制定者而言，这意味着单纯关注税收执法无法触及财富分配的源头问题。\n\n> **KC评论：** 这份报告最重要的贡\n\n[... middle omitted ...]\n\n您将获得比一篇公众号文章更完整、更深入的洞察。期待与您交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n高净值房产的性别鸿沟，比你想的更深\n\n🏠 女性在高端房产中的占比不到20%\n\n最近看了一份阿根廷某城市的房产税研报，数据维度非常有意思，分享几个核心发现👇\n\n1️⃣ 房产所有权：低端均衡，高端失衡\n- 在房产价值后40%的低端市场，女性、男性、共有产权各占约1/3\n- 但到了前1%的高端房产，女性占比骤降至不到20%，男性约30%，共有产权占50%\n- 高端房产的性别差距，比我们想象中更明显\n\n2️⃣ 房产税缴纳：男女基本一致\n- 整体逃税率约46%，女性略低（46% vs 男性48.5%）\n- 随着房产价值上升，按时缴税比例从35%升至60%\n- 男女在按时缴税上没有显著差异\n- 但女性因持有更多低价值房产，实际有效税率略高（税制轻微累退）\n\n3️⃣ 催缴效果：男女反应类似\n- 收到催缴信后，女性按时缴税提升4.2个百分点，男性提升4.7个百分点\n- 男性反应更快，但女性后续追缴很快补上差距\n- 催缴信还能带动清理旧债和预缴未来税款\n- 疫情期间，男女缴税行为变化也无明显差异\n\n4️⃣ 一个有趣的细节\n- 女性使用电子支付的概率略低，即使控制年龄因素后仍然存在\n\n研报启示：在房产税领域，性别差异更多体现在资\n\n[... middle omitted ...]\n\narities, with women's share dropping to less than $20\\%$ in the top $1\\%$ . Tax compliance increases with property value, with an average evasion rate of $46\\%$ , and men and women are equally\n\n[... middle omitted ...]\n\nf each regression, corresponding to the average of the dependent variable for accounts that did not receive a letter. Standard errors clustered by blocks are reported in parentheses. \\* p<0.10, \\*\\* p<0.05, \\*\\*\\* p<0.01"
  },
  {
    "id": "R027",
    "title": "世界银行：全球16万家企业数据揭示，气候适应力正在制造新的贫富分化",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：全球16万家企业数据揭示，气候适应力正在制造新的贫富分化\n\n气候变化的讨论长期集中在宏观预测——升温多少度，GDP下降几个百分点。但真正的问题不在宏观，而在微观：当温度比历史均值高出0.5度时，一家具体的企业会发生什么？它的收入会减少多少？它有没有能力做出调整？如果调整不了，是谁的错？\n\n世界银行最新发布的政策研究工作论文《Firm-Level Climate Change Adaptation: Micro Evidence from 134 Nations》，用近16万家企业、覆盖134个国家、跨越15年的数据，给出了一个冷峻但可以被政策改变的答案。这份报告的核心判断是：市场不完善正在阻碍低收入和中等收入国家的企业适应气候变化，而适应能力的差距，正在制造一种新的结构性不平等——不是国家之间的，而是企业之间的。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 温度偏离历史均值0.5度，中小企业收入下降12%\n\n报告最核心的发现是一个具体到令人不安的数字。在低收入和中低收入国家，当年度平均温度比历史均值高出0.5摄氏度时，中小企业的收入平均下降12%。这个数字不是理论推演，而是来自将卫星气象数据与企业调查数据在空间上精确匹配后的回归结果。\n\n为什么是0.5度？因为报告测量的是温度偏离，而不是绝对温度。一个常年30度的热带城市，如果某年温度上升到30.5度，其经济影响可能比一个从5度上升到10度的温带城市更严重。关键在于偏离——企业、工人、基础设施都是基于历史气候模式来设计的，当模式被打破，调整成本就出现了。\n\n12%的收入下降意味着什么？对于利润率通常在5%-10%之间徘徊的中小企业来说，这相当于一整年的利润被抹掉，甚至可能直接触发现金流断裂。报告同时指出，这种冲击不是一次性的——随着全球变暖加速，温度偏离的\n\n[... middle omitted ...]\n\n基金、资管机构、战略咨询、智库等领域的从业者，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n气温升高1度，小企业收入跌12%\n\n全球企业都在“热”中承压\n\n我最近翻到一份世界银行的研究论文，覆盖134个国家、近16万家企业，用卫星气象数据+企业调查数据，专门分析气温升高对企业收入的影响。\n\n几个核心发现：\n\n1️⃣ 气温升高0.5°C，小企业收入跌12%\n- 低收入和中低收入国家的中小企业，在年平均气温比历史均值高0.5°C的年份，收入下降12%\n- 初创企业受影响更大，因为融资渠道有限、适应能力弱\n\n2️⃣ 制造业和服务业都受影响\n- 研究覆盖了制造业和服务业企业，结果显示两类企业受影响程度相当\n- 传导路径：气温升高→劳动生产率下降→工资降低→收入减少\n\n3️⃣ 哪些企业更脆弱？\n- 热敏感行业（食品、医疗、交通等）受损更严重\n- 生产过程弹性差的企业更易受冲击\n- 大型企业、高收入国家的企业适应能力更强\n\n4️⃣ 政策环境是关键制约因素\n- 融资困难、监管负担重、安全条件差，都会提高企业适应气候变化的成本\n- 低收入国家企业的适应能力被政策约束明显削弱\n\n研究用15年数据，结合企业所在地的精确温度偏差（企业财年内温度vs 1980-2008年历史均值），识别出因果关系，不是简单相关。\n\n#学习\n\n[... middle omitted ...]\n\ns in 134 countries over a 15-year period. Our results show that market imperfections in low- and middle-income countries constrain firms' ability to adapt. Small and medium-size firms in low- \n\n[... middle omitted ...]\n\n108(0.071)</td><td>-0.113(0.036)</td><td>-0.063(0.034)</td><td>-0.166(0.228)</td><td>-0.034(0.041)</td><td>-0.136(0.059)</td><td>0.113(0.096)</td></tr></table>\n\nTable A8: Regression Results using Coefficient of Variation"
  },
  {
    "id": "R028",
    "title": "世界银行：冲突如何迫使高技能人才主动“降级”求职",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：冲突如何迫使高技能人才主动“降级”求职\n\n这份世界银行最新工作论文揭示了一个反常识的结论：当冲突加剧时，高技能人才非但没有因为稀缺性而更挑剔工作，反而更愿意接受低于自身资历的岗位。这不是简单的“生存优先”，而是安全需求对人力资本定价机制的结构性重塑。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 冲突让高技能人才愿意为“低就”接受更低的工资溢价\n\n传统经济学假设，劳动者会对不适合自己资历的工作要求额外补偿——即“补偿性工资差异”。世界银行这份针对缅甸高技能青年的实验研究表明，当冲突强度上升一个标准差，劳动者为接受低技能工作所要求的额外溢价会下降约7-9个百分点。这意味着，冲突地区的人才正在用职业尊严换取安全。\n\n这个发现的关键不在于“冲突导致移民”，而在于它改变了移民质量。通常，经济移民是为了获取更高的技能匹配回报，而冲突驱动的移民却在出发前就已经接受了人力资本的折价。这批人到了目的地后，更可能长期停留在低技能岗位，形成代际传递的贫困陷阱。\n\n> **KC评论：** 这份报告的核心洞察不是“冲突让人想移民”，而是“冲突让人愿意以更低的价格出卖自己的技能”。如果你关注全球劳动力市场或东南亚产业链转移，这个发现意味着流入泰国、马来西亚等国的缅甸劳动力，其实际生产力可能远低于其教育水平，这会压低当地低技能岗位的均衡工资，同时也意味着这些移民的人力资本被系统性浪费。完整的实验设计和数据分组在报告中有更详细的拆解。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 冲突的边际效应在女性、少数民族和语言弱势群体中放大三倍\n\n报告最值得关注的异质性分析显示，冲突对职业降级意愿的影响并非平均分布。女性群体受冲突影响的边际效应是男性的2-3倍；英语能力“不足好”的群体，其效应显著，而英语能力\n\n[... middle omitted ...]\n\n与图表，观测边际变化。扫码交流，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n缅甸冲突下的高学历青年：愿意降级工作赴海外\n\n**降级也去？**\n\n**冲突下的海外工作选择**\n\n---\n\n最近读了一份世界银行的研究报告，研究的是缅甸冲突如何影响高学历青年的海外工作选择。\n\n先说个有意思的发现：在正常情况下，人们要求一份比自己能力低的工作时，会要求多20%的工资溢价作为补偿。但冲突地区的人，这个溢价要求明显降低了。\n\n**核心逻辑：**\n1. 安全 vs 经济：冲突地区的人把“物理安全”放在第一位，愿意牺牲工作匹配度来换取安全\n2. 补偿工资差异（CWD）降低：冲突减少了人们对“降级工作”的工资补偿要求\n3. 越弱势，越妥协：女性、少数族裔、语言能力弱、没有海外关系网的人，妥协意愿更强\n\n**具体数据支持：**\n- 冲突地区的人对降级工作的工资溢价要求显著降低\n- 生活在“领土争夺区”（territorial contestation）的人影响最大\n- 征兵令颁布后，符合条件的年轻人更愿意接受降级工作\n\n**有意思的异质性发现：**\n- 女性比男性更容易接受降级工作\n- 没有海外关系网的人比有关系的更“好说话”\n- 最近收入下降的人，妥协意愿更强\n- 感觉被“低薪”对待的人，更愿意接受降\n\n[... middle omitted ...]\n\nuced by conflict reduces the additional wage premium that individuals would typically demand for taking on lower skilled work, indicating greater amenability to occupational downgrading. These\n\n[... middle omitted ...]\n\n/td><td>762</td><td>868</td><td>614</td><td>1016</td><td>1098</td><td>454</td></tr></table>\n\nFor all tables: Standard errors clustered at the township level and indicated in parentheses. Controls as indicated in Table 2."
  },
  {
    "id": "R029",
    "title": "世界银行：性别壁垒下降贡献了全球28%的人均GDP增长，但印度是反例",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：性别壁垒下降贡献了全球28%的人均GDP增长，但印度是反例\n\n当全球大部分经济体在过去五十年经历了女性劳动参与率的显著上升时，一个更深层的经济问题被忽略了：性别壁垒的消融，不仅仅是社会进步的标志，更是结构性转型和经济增长的独立驱动力。世界银行最新发布的工作论文，基于91个国家、跨越五个十年（1970-2018）的微观数据，给出了一个量化的答案：性别壁垒的下降，平均解释了样本国家28%的人均GDP增长。但这一数字背后，隐藏着国家间的巨大分化——从巴西的超过50%，到印度的负贡献。\n\n这份报告的价值不在于重复“女性参与经济有益”的常识，而在于它首次系统性地拆解了性别壁垒、结构性转型与经济增长之间的因果链条。更关键的是，它揭示了一个反直觉的发现：制造业的“去工业化”并非完全是技术或贸易的结果，性别壁垒的下降本身就在推动劳动力向服务业转移。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 女性就业路径与男性迥异：制造业不是女性的目的地\n\n传统结构性转型理论认为，随着经济发展，劳动力会从农业流向制造业，再流向服务业。但世界银行的这份报告发现，这一经典路径主要适用于男性。女性的就业转型遵循完全不同的轨迹。\n\n在低发展阶段，女性离开农业后，主要流向是“退出劳动力市场”，而非进入制造业。只有当经济发展到更高阶段，女性才重新进入劳动力市场，且几乎全部集中在服务业。女性的制造业就业比例在所有发展水平上都保持低位，这一模式与男性形成鲜明对比。\n\n这意味着什么？如果一个经济体试图通过发展制造业来吸纳女性劳动力，可能从一开始就选错了方向。女性的就业选择更多受到社会规范、职业隔离和家庭责任的约束，而非单纯的产业结构变化。这一发现对发展中国家制定产业政策和就业战略具有直接的警示意义。\n\n> **KC评论：** 许多发展中国家的政策制定者仍\n\n[... middle omitted ...]\n\n的朋友，期待与你交流。扫码加入，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n女性崛起，如何重塑经济结构？\n\n女性就业变迁\n揭示背后经济增长密码\n\n📌 一份来自90+国家、跨度50年的研究，用数据告诉我们：女性进入职场，不只是平权问题，更是一股重塑经济结构的力量。\n\n1️⃣ 男女就业路径大不同\n男性随经济发展，从农业→制造业→服务业，是经典模式。\n女性却不同：低发展阶段，她们离开农业后往往退出职场；等到经济更发达，才重新进入，但主要集中在服务业，制造业占比始终很低。\n\n2️⃣ 性别壁垒下降，是增长的关键引擎\n研究用6大经济体（印、印尼、巴西、墨、加、美）数据建模，发现：\n- 性别“规范壁垒”（如社会偏见带来的职业选择成本）和“工资歧视”都在下降\n- 1970-2018年，壁垒下降解释了这些国家**28%**的人均GDP增长\n- 巴西贡献最大（超50%），印度反而因壁垒上升拖累了增长\n\n3️⃣ 服务业崛起，女性是“隐形推手”\n研究特别指出：性别壁垒下降，加速了劳动力向服务业转移。这为发展中国家“过早去工业化”现象提供了一个新解释——不是制造业不行了，而是服务业因女性加入而更快扩张。\n\n💡 一点思考\n经济转型不止是产业升级，也关乎“谁”在做什么工作。当性别壁垒降低，不仅女性受益，整个经济的\n\n[... middle omitted ...]\n\nining gender barriers—defined as gender-specific distortions in employment and wages—were a key driver of the observed rise in female labor force participation, expansion of the service sector\n\n[... middle omitted ...]\n\nart-time workers as described above.\n\nEarnings in Home Sector: For each country-year, we set earnings in the Home Sector equal to the measured earnings of women who work in “elementary occupations” in the service sector."
  },
  {
    "id": "R030",
    "title": "世界银行：中小企业怕的不是税务官，而是“税务官来了又走”",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：中小企业怕的不是税务官，而是“税务官来了又走”\n\n坦桑尼亚的税务局官员跟着调查员一起入户走访，这件事本身听起来像一场“突袭检查”。但世界银行一份基于随机对照实验的最新工作论文给出了一个反直觉的结论：税务官员的短期在场，并没有显著提升中小企业的整体纳税遵从度。真正值得关注的，不是“有没有人管”，而是“管完之后还管不管”。\n\n这份研究由世界银行与坦桑尼亚税务局联合实施，在119个城市和城郊区域随机抽取一半的社区，让税务官员陪同独立调查公司进行面对面访谈。这相当于一次人为制造的、短暂但真实的税务官在场率提升。研究团队随后结合调查问卷和行政申报数据，追踪了这些企业对税务的态度和实际纳税行为的变化。\n\n如果你以为“只要税务官多露脸，企业就会乖乖交税”，那这份报告可能会让你重新思考。它揭示了一个更深层的治理难题：短期震慑有效，但不可持续；长期信任的建立，需要的不是一次性的“帮忙”，而是可预期的、公平的制度环境。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 税务官在场对纳税遵从的整体影响并不显著，但存在明显的区域分化\n\n这是整个实验最核心的发现。从全样本看，无论是“是否纳税”（广度）还是“纳税金额”（深度），处理组和控制组之间没有统计上的显著差异。换句话说，让税务官跟着调查员走一圈，并没有让整个社区的中小企业突然变得老实。\n\n但细分之后，故事出现了转折。在坦桑尼亚的经济中心达累斯萨拉姆（Eastern区域），处理组企业在实验后的第一个季度（2023年第一季度）中，无论是纳税概率还是纳税金额都出现了显著的短期提升。而在其他地区，这种效应并不存在。\n\n这意味着什么？达累斯萨拉姆是税务局总部所在地，税务官的日常可见度本来就远高于其他地区。当实验进一步提高了这种可见度，企业感知到的执法可信度被推高到了某个“临界点”，从而触发了\n\n[... middle omitted ...]\n\n头部券商、PE/VC、投行、战略咨询和智库的朋友们一起讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n税务官员在场，小企业主还敢说真话吗？\n\n税务官员“盯梢”小企业\n\n一场关于纳税诚实度的田野实验\n\n📌 一篇世行与坦桑尼亚税务局合作的田野实验，揭示了一个有趣的现象：当税务官员陪同调查员一起上门时，中小企业主的行为和态度会怎么变？\n\n1/ 实验怎么设计的？\n- 调查覆盖坦桑尼亚大陆119个城区/近郊社区，随机分成两组\n- 一组由独立调查公司单独上门，另一组有税务局官员陪同\n- 税务官员只是观察，不参与提问和记录\n\n2/ 核心发现：效果是“分裂”的\n- 整体来看，税务官员在场对纳税遵从（是否按时缴税、缴多少）没有显著影响\n- 但在首都达累斯萨拉姆，短期内（2023年第一季度）缴税概率和金额都有提升\n- 而坦桑尼亚其他地区，税务官员在场显著提升了纳税道德感\n\n3/ 为什么会出现“言行不一”？\n- 研究团队在2024年4-5月做了回访调查，发现一个可能的解释：\n- 企业主在税务官员面前说的“我认同纳税很重要”可能是假话\n- 更像是“怕被穿小鞋”而说谎，而非真的被说服\n- 真正起作用的是“执法可信度”的感知提升，而非信任和便利感的增强\n\n4/ 对政策设计的启示\n- 临时性的“友善接触”效果有限，尤其在没有后续跟进的情况\n\n[... middle omitted ...]\n\n mainland Tanzania. An independent survey firm was accompanied by Tanzania Revenue Authority officers, who observed the interviews in a randomly selected set of urban and peri-urban wards. Thi\n\n[... middle omitted ...]\n\ntd><td></td><td></td></tr><tr><td>Other</td><td>381</td><td>(62.5)</td><td>345</td><td>(57.5)</td><td>0.10135</td></tr><tr><td>Wholesale ~1</td><td>229</td><td>(37.5)</td><td>255</td><td>(42.5)</td><td></td></tr></table>"
  },
  {
    "id": "R031",
    "title": "世界银行：越南经济增长的“穷人隔离”悖论",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：越南经济增长的“穷人隔离”悖论\n\n越南是过去二十年全球经济增长和减贫的明星案例。从2002年到2020年，人均实际支出增长超过三倍，贫困率从29%骤降至不足5%。然而，世界银行最新政策研究工作论文揭示了一个令人不安的结构性事实：贫困人口正在被“隔离”到特定省份，而省内不平等已经远超省际不平等，且差距仍在扩大。这份报告的核心判断是：越南的增长模式正在从“普惠式减贫”转向“空间隔离式增长”，如果政策不转向减少空间差异和收入不平等，可持续发展目标将难以实现。\n\n为什么这个判断值得关注？因为越南的增长故事长期被简化为“开放+改革=减贫”的线性叙事。但世界银行的分析表明，这个公式正在失效——增长的红利越来越集中，而贫困的“硬核”正固化在少数民族聚居的山区省份。对于关注新兴市场投资、全球供应链转移以及发展经济学范式的读者来说，这不仅是越南的问题，更是所有高速增长经济体面临的普遍挑战。\n\n> **KC评论：** 报告最尖锐的发现是“贫困隔离”而非“贫困减少”。越南的贫困率虽然大幅下降，但剩下的贫困人口越来越集中到少数省份，而且这些省份的少数民族人口占比极高。这意味着传统的“增长带动减贫”模式已经触及天花板，下一步减贫必须针对特定地区和群体，而非泛泛的经济刺激。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 省内不平等是省际不平等的三倍，且差距仍在扩大\n\n世界银行报告使用泰尔指数（Theil index）对不平等进行分解，发现了一个被多数宏观分析忽略的关键事实：越南的不平等主要来自省内差异，而非省际差异。2002年，省内不平等解释了约66%的总不平等；到2020年，这一比例已超过70%。换言之，省内不平等从约为省际不平等的两倍，扩大到了三倍。\n\n这意味着什么？传统的“沿海-内陆”“城市-农村”二元分析框架已经不足以解释越南\n\n[... middle omitted ...]\n\n解读与原始图表。这里汇聚了来自头部机构的朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n越南经济亮眼，但穷人被“隔离”了\n\n贫富差距，藏在省界内\n\n越南经济增速快，但内部不平等才是真问题\n\n---\n\n最近读了一篇某外资投行的研报，讲的是越南过去20年的经济增长与贫富分化。数据很新，观点也很清晰。\n\n**核心发现：越南经济增长快，但穷人被“隔离”在某些省份。**\n\n1️⃣ **经济增长快，但贫富差距在省内部拉大**\n- 2002-2020年，越南人均支出翻了3倍多\n- 但省内的不平等比省之间大得多，2020年省内不平等是省间的3倍\n- 这意味着：你住在哪个省不重要，重要的是你在省里处于哪个阶层\n\n2️⃣ **穷人越来越集中在少数省份**\n- 贫困率从2002年的29%降到2020年的不到5%\n- 但剩下的穷人高度集中在北方山区省份，比如奠边省贫困率46%、莱州36%\n- 这些省份有个共同点：少数民族人口占比超过70%\n\n3️⃣ **经济增长对减贫有帮助，但要看不平等程度**\n- 经济增长总体上有利于减贫\n- 但不平等程度越高，经济增长对减贫的正面作用就越弱\n- 不平等对贫困深度和贫困严重程度的影响更显著\n\n4️⃣ **从农业转向非农业，是好事**\n- 研究发现，经济从农业向工资性收入和服务业转型，\n\n[... middle omitted ...]\n\nother data sources, this paper finds within-province inequality to be much larger than between-province inequality. Furthermore, this inequality gap has been rising over time. Despite the coun\n\n[... middle omitted ...]\n\nnd predict per capita expenditure for these households. As a result, we have per capita expenditure data for the full sample of 45,000 households, and we use this data to estimate the per capita expenditure of provinces."
  },
  {
    "id": "R032",
    "title": "世界银行：小国正在从全球化中收获超预期的福利，但多数人忽视了这一点",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：小国正在从全球化中收获超预期的福利，但多数人忽视了这一点\n\n全球化的批评声浪在过去十年持续高涨。从供应链脱钩到关税壁垒，从地缘政治碎片化到国内分配不均，质疑经济一体化益处的论述几乎成为主流叙事。然而，世界银行最新发布的工作论文（Policy Research Working Paper 11072）提供了一个被当前舆论场严重低估的视角：对于新兴市场和发展中经济体，尤其是那些规模较小、正在转型的经济体，国际贸易带来的品种扩张仍在创造可观的福利收益，其幅度远超多数人的直觉。\n\n这篇由Enkhmaa Battogtvor、Socrates Kraido Majune和Angella Faith Montfaucon完成的报告，估算了28个东亚和东非国家在1995年至2021年间因进口商品种类增长所带来的福利变化。结论清晰而有力：非洲国家平均获得了相当于GDP 5.47%的福利增益（年均0.20%），亚洲国家（不含不丹）则为3.46%（年均0.13%）。不丹、蒙古、卢旺达和莫桑比克是样本期间获益最高的国家。\n\n这不是一篇关于“贸易总量增长”的报告，而是一篇关于“贸易结构变化如何影响消费者真实福利”的严谨量化分析。它提醒我们，在宏观辩论之外，微观层面的品种扩张——一个中国消费者能买到智利红酒、一个卢旺达农民能用上日本农机——所释放的福利改善，可能远比我们想象得更加显著。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 进口品种的爆炸式增长，比贸易额增长更能衡量真实福利\n\n传统贸易福利分析往往聚焦于进口总额的变化，即所谓的“集约边际”。但世界银行这份报告指出，这种视角严重低估了福利改善的真实幅度。真正关键的变量是“广延边际”——即进口商品种类和来源国数量的增长。\n\n报告采用Armington（1969）的定义，将“品种”\n\n[... middle omitted ...]\n\n金、资管机构、战略咨询、智库等机构的朋友，期待与你交流。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n多进口一种商品，国家能多赚多少\n\n进口品种越多，国家越赚\n\n研究显示：每多一种进口品类，GDP平均多增0.2%\n\n1/ 最近翻到一篇世界银行的政策研究论文，测算1995-2021年间，28个东亚和东非国家从进口品种多样化中获得的福利收益。\n\n结论很直观：进口的商品种类越多，国家的整体福利就越高。\n\n2/ 核心数据：\n- 非洲国家平均获益5.47%的GDP（年均0.20%）\n- 亚洲国家（不含不丹）平均获益3.46%（年均0.13%）\n- 不丹、蒙古、卢旺达、莫桑比克是获益最大的国家\n\n3/ 逻辑拆解：\n- 论文估算超过10万个产品层面的替代弹性\n- 用Feenstra和Broda-Weinstein的方法构建精确价格指数\n- 平均弹性为13.0，中位数为4.1（弹性越低，产品差异化越高，品种收益越大）\n\n4/ 一个反直觉发现：\n法国和德国这样的大经济体，在欧盟内部的品种收益竟然是负的。\n原因很简单：它们已经高度一体化，新品类增长空间有限。\n\n而小经济体、转型经济体，每多一个进口来源，收益都显著。\n\n5/ 对研究者的价值：\n论文提供了4537个产品的替代弹性估计值，可用于其他研究——比如分析进口产品对汇率波动的\n\n[... middle omitted ...]\n\n level of disaggregation. More than 100,000 elasticities are estimated, and the paper constructs an exact price index to measure the welfare gains from variety growth. The findings show that f\n\n[... middle omitted ...]\n\n:5–38.\n\nSato, K. (1976). The ideal log-change index number. The Review of Economics and Statistics, pages 223–228.\n\nVartia, Y. O. (1976). Ideal log-change index numbers. scandinavian Journal of statistics, pages 121–126."
  },
  {
    "id": "R033",
    "title": "世界银行：刚果金的道路修复带来了和平，但这份红利只有三年有效期",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：刚果金的道路修复带来了和平，但这份红利只有三年有效期\n\n当一个国家有超过120个武装组织活跃在东部，而70%的暴力事件发生在公路附近时，修复一条道路究竟是带来和平，还是为冲突提供更便捷的通道？世界银行最新发布的工作论文给出了一个既令人振奋又令人不安的答案：道路修复确实能显著降低暴力事件，降幅达到5到10个百分点。但这个“和平红利”的有效期只有三年。三年后，随着道路质量退化，暴力会重新回到修复前的水平。\n\n这份报告的价值不在于简单回答“修路是好是坏”，而在于它用刚果金过去二十年的数据，揭示了一个被国际援助界长期忽略的关键变量——维护。没有系统性维护的基础设施投资，本质上是在购买一张有期限的和平保单。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 道路修复对暴力的抑制效应是真实的，但也是短暂的\n\n研究团队收集了刚果金自2003年第二次刚果战争结束以来的192个大型城际道路投资项目，结合高分辨率卫星图像和机器学习算法，对道路质量变化进行了纵向追踪。核心发现清晰且有力：道路修复项目完成后，项目所在区域的暴力事件发生率显著下降5到10个百分点，其中针对平民的暴力下降最为明显。\n\n但动态效应分析揭示了另一个残酷的事实：这种和平效应在项目完成三年后基本消失。暴力水平会反弹至修复前的状态。研究团队通过遥感数据测算出一个关键指标——道路年退化系数为0.735。这意味着修复后的道路，每年质量下降约26.5%，三年后平均质量下降超过60%。当道路重新变得难以通行，武装组织重新获得了对“不可达区域”的控制权，暴力也随之回归。\n\n> **KC评论：** 这是整篇报告最值得记住的一个数字：三年。对于任何在冲突地区规划基础设施投资的决策者来说，这个时间窗口意味着必须把项目预算的30%以上留给后期维护，否则前期的和平投资本质上是在“租用”\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n刚读完一份很有意思的世行研报，讲的是刚果（金）修路和暴力冲突的关系。结论很反直觉：路修好了，暴力确实会降；但路一烂，暴力又回来了。\n\n**修路带来的和平，有保质期**\n\n刚果（金）的公路，很多只存在于地图上。国际组织砸了巨资修路，想通过改善交通来稳定局势、发展经济。研报用了一个很巧妙的方法：对比修路区域和没修路区域的暴力事件变化。\n\n1️⃣ **修路期间，暴力事件减少**\n   研究发现，在道路修复项目完工后，该区域的暴力事件显著下降了约5-10个百分点。尤其是针对平民的暴力，下降最明显。路通了，政府军和维和部队能更快到达，经济活动也能恢复，大家都有饭吃，就不那么想打仗了。\n\n2️⃣ **和平红利，只有三年保质期**\n   但问题来了。刚果（金）的热带气候和缺乏维护，让修好的路很快就烂了。研报用机器学习分析了大量卫星图像，发现修复后的道路质量每年会下降约26.5%。三年后，路的质量平均下降60%。\n\n3️⃣ **路一烂，暴力就反弹**\n   关键发现来了：随着道路质量下降，暴力事件又慢慢回升了。研报的统计显示，道路修复带来的“和平红利”在三年内就基本消退。路烂了，政府管不到，武装分子又活跃起来，暴力重新抬头。\n\n[... middle omitted ...]\n\nad rehabilitation deter violence, which decreases significantly by around 5 to 10 percentage points after the completion of road rehabilitation. However, another significant finding, based on \n\n[... middle omitted ...]\n\n level often led to changes in leadership within the PS, with ministers opting to nominate a confidant to lead the PS.”\n\n5. Democratic Republic Of Congo Emergency Social Action Project P086874 Large Implementation delays"
  },
  {
    "id": "R034",
    "title": "世界银行：印度农村非农就业的真正瓶颈不是技能，是结构",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：印度农村非农就业的真正瓶颈不是技能，是结构\n\n一份来自世界银行的最新工作论文，聚焦印度拉贾斯坦邦的农村非农就业，给出了一个既符合直觉又令人不安的判断：教育确实能打开非农就业的大门，但门后的世界并非对所有受教育者一视同仁。对于女性、低种姓群体以及偏远地区居民而言，即使拥有了中学学历，他们进入高薪正规非农岗位的概率仍然远低于同等条件的男性或高种姓群体。这份报告的核心贡献不在于重复“教育重要”的老生常谈，而在于量化了“教育之外的结构性壁垒”究竟有多顽固。\n\n这并非一份关于印度某个邦的孤立研究。拉贾斯坦邦的困境——农业受气候制约、土地细碎化、非农就业增长但质量分化——在多数发展中国家具有高度代表性。当中国读者关注国内乡村振兴与县域经济时，这份报告提供的分析框架和实证方法，恰好回答了一个普遍问题：为什么同样的政策工具，在不同地区、不同人群身上效果差异巨大？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 中学教育是入场券，但女性与低种姓群体拿到的不是同一张\n\n报告基于1999年至2011年四轮全国家庭调查数据，以及2015年的最新抽样数据，对拉贾斯坦邦农村个体的非农就业参与进行了回归分析。结论清晰且稳健：完成中学教育（secondary education）是个体进入非农部门，尤其是正规服务业岗位的最强预测因子。与仅有小学学历者相比，中学学历者获得正规非农工作的概率高出数倍。\n\n然而，交互项分析揭示了关键的不平等。当模型加入“女性”与“中学学历”的交互项后，教育对女性的正向效应显著弱于男性。换言之，一个受过中学教育的农村女性，进入正规非农就业的概率仍然低于同等学历的男性。同样，表C2显示，对于表列种姓和表列部落（SC/ST）群体而言，即使完成了中学教育，他们进入正规非农就业的概率也显著低于同等学历的高种姓群体，反而更可\n\n[... middle omitted ...]\n\ne fund、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n农村非农就业，谁在吃肉谁在喝汤？\n\n**非农≠高薪**\n\n**拉贾斯坦邦的农村非农就业真相**\n\n---\n\n1/ 农村非农就业（RNFE）一直被视为农村发展的关键路径，能帮农户分散农业风险、平滑消费，还能带动地方经济。但这份针对印度拉贾斯坦邦的研究告诉我们：非农就业的“好”，并不均等。\n\n2/ **谁更容易进入非农领域？**\n- 完成中学教育的人，进入非农（尤其是技能型服务业）的概率显著更高。\n- 女性、社会边缘群体（如种姓弱势群体）在进入高薪非农岗位时，面临明显壁垒。女性即使有银行账户，在正规非农就业上仍处于劣势。\n\n3/ **非农就业真的能改善生活吗？**\n- 是的，但分类型。拥有**稳定、正式**的非农工作（尤其是服务业）的家庭，消费水平明显更高。\n- 但**临时性、非正式**的非农工作，其福利水平与农业劳动相差无几。不是进了非农就脱贫，得看是什么工。\n\n4/ **农村小企业卡在哪？**\n- 最大障碍：**本地需求不足** + **融资渠道有限**。不是不想做大，是没人买、没钱借。\n\n5/ **历史规律还在吗？**\n- 1999-2011年间的预测因素（如教育、性别差距）在2015年依然有效，说明结构性\n\n[... middle omitted ...]\n\nly predicts participation in non-farm activities, particularly in skilled service sector jobs. However, women and socially marginalized groups face significant barriers in accessing non-farm e\n\n[... middle omitted ...]\n\nforce. Educated is a dummy equaling 1 if the individual has completed secondary or higher education; Bank is a dummy equaling 1 if the individual has a bank account. Standard errors in parentheses, clustered by district."
  },
  {
    "id": "R035",
    "title": "世界银行：种子市场化改革让埃塞俄比亚玉米增产18%，但小麦为何失效？",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：种子市场化改革让埃塞俄比亚玉米增产18%，但小麦为何失效？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 一份来自世界银行的实证研究，揭示了“放松管制”在农业领域的真实效果与边界\n\n农业是埃塞俄比亚经济的命脉，但低下的作物生产率长期制约着这个东非国家的发展。核心症结之一，是农民对改良种子的采用率极低——到2019年，全国仅有不到四分之一的小农户使用改良品种。问题出在供给端：埃塞俄比亚的种子市场长期由国有企业垄断，从品种培育、种子繁殖到最终分销，整个链条几乎不给私营部门留出空间。这种高度集中的体制带来了需求预测失准、供应错配、库存积压、配送延迟等一系列问题。\n\n2011年，埃塞俄比亚政府启动了一场被称为“直接种子营销”（DSM）的实验性改革，试图打破这种僵局。DSM的核心逻辑很简单：允许种子生产商（无论是国有还是私营）直接向农民销售种子，绕过政府主导的行政分销体系。这不仅是渠道的简化，更是整个种子市场运行机制的深层变革——从“计划驱动”转向“市场驱动”。\n\n世界银行最新发布的工作论文《Seeds of Change: The Impact of Ethiopia's Direct Seed Marketing Approach on Smallholders' Seed Purchases and Productivity》，首次对这一改革进行了严格的定量评估。研究结论清晰而微妙：DSM确实有效，但它的效果高度依赖作物品种的生物学特性。对于杂交玉米，改革带来了显著的生产率提升；但对于自花授粉的小麦，效果几乎为零。\n\n这份报告的价值不仅在于它为非洲农业政策提供了实证依据，更在于它揭示了一个普遍性的问题：市场化改革并非万能药，其成效取决于改革对象的内在属性。对于正在探索农业转型的发展中国家，以及关注新兴市场农业投资机会\n\n[... middle omitted ...]\n\nfund、资管机构、战略咨询、智库等朋友，期待与你交流。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n埃塞俄比亚的种子革命，居然只对玉米有效？\n\n🌱 种子的力量\n\n埃塞俄比亚搞了个“直接种子营销”实验，想打破国有垄断，让农民能直接买到好种子。结果呢？玉米增产18%，小麦却纹丝不动。\n\n1️⃣ 改革逻辑：以前种子从国企到农民，层层审批、经常断货。2011年起，政府允许私企和国企直接卖种子给农民，缩短链条、引入竞争。\n\n2️⃣ 玉米赢了：购买种子的农户增加15%，每公顷用量涨45%，产量提升18%。因为玉米杂交种每年都得买新种子，市场动力足。\n\n3️⃣ 小麦输了：自花授粉作物，农民可以留种，对商业种子需求弱。改革对它基本没影响。\n\n4️⃣ 政策启示：不是所有作物都适合市场化。杂交作物（如玉米）改革见效快，自花授粉作物需要更精细的配套。\n\n💡 思考：农业改革不是万能药，得看作物“性格”。自花授粉作物怎么破？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n# Seeds of Change\n\n## The Impact of Ethiopia's Direct Seed Marketing Approach on Smallholders' Seed Purchases and Producti\n\n[... middle omitted ...]\n\nia introduced a novel experiment—the direct seed marketing approach—to reduce some of the centralized, state-run attributes of the country's seed market and rationalize the use of public resou\n\n[... middle omitted ...]\n\n3060d65f301a68c0c393f9c7f6933c02.jpg)  \nNote: ATT refers to the Average Treatment Effect on the Treated. DSM refers to Direct Seed Marketing. Source: Authors' estimation based on the ACC 2012, 2016, and 2019 survey data."
  },
  {
    "id": "R036",
    "title": "世界银行：数字化企业更环保、更培训，但更少女性高管",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：数字化企业更环保、更培训，但更少女性高管\n\n数字科技公司常常被描绘成未来商业的引领者——更敏捷、更透明、更注重社会责任。然而，世界银行一份覆盖158个国家、近20万家企业的研究报告揭示了一个远比想象中复杂的真相：技术的伦理效应并非单向的绿灯，而是一幅充满张力与矛盾的图景。\n\n这份基于2006年至2023年企业调查数据的工作论文，核心发现可以概括为一个判断句：数字科技企业在环境和社会维度上表现更优，但在公司治理的性别维度上，却显示出显著的倒退。这不是一个简单的“科技向善”或“科技作恶”的故事，而是一个关于文化土壤、制度环境与商业激励机制如何共同塑造企业伦理行为的复杂叙事。\n\n我们来看数据究竟说了什么，以及这些发现对产业决策者和投资者意味着什么。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 数字科技企业在环保和员工培训上确实表现更好，但这并非理所当然\n\n研究选取了三个指标来刻画企业的伦理行为：是否监测二氧化碳排放（环境维度E）、是否为员工提供正式培训（社会维度S）、以及是否聘用女性高管（治理维度G）。在控制了企业规模、融资渠道、销售增长、企业年龄和国家人均GDP后，结果清晰显示：同时具备技术密集度和数字化在线存在（拥有网站或社交媒体页面）的企业，在监测碳排放和提供员工培训上的概率显著高于其他企业。\n\n这个结果听起来符合直觉，但其背后的逻辑值得深究。报告指出，数字科技企业之所以更倾向于监测碳排放，并非仅仅因为“它们更环保”，而是因为技术本身提供了更低成本的监测手段。同样，数字化培训工具使得员工技能提升变得可规模化、可追踪。换句话说，伦理行为的“成本曲线”因技术而下降，从而激励了企业采取这些行动。\n\n> **KC评论：** 这意味着，对于政策制定者而言，推动企业环境和社会责任的关键杠杆之一，可能是降低技术工具的采\n\n[... middle omitted ...]\n\n观与产业的边际变化。扫码交流，期待与您一起讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n科技公司，真的更“道德”吗？\n\n科技巨头的ESG真相\n\n某外资投行一份覆盖158个国家、19万+企业的研报，专门研究了“数字化+技术密集型企业”的伦理表现。结论很有意思：科技公司在环保和员工培训上确实做得更好，但在性别平等上却“翻车”了。\n\n1/ 环境与社会：科技是加分项\n有网站/社交媒体、且属于中高技术密集度的企业，监控CO2排放的概率更高，也更愿意给员工提供正式培训。\n→ 数字化工具让环保数据更透明，线上培训也降低了成本，科技确实能推动可持续发展。\n\n2/ 治理：女性高管更少了\n但同一批企业，雇佣女性高管的概率却显著更低。\n研报推测原因：STEM领域的性别历史差距导致合格女性候选池小，加上科技行业“男性气质”文化更突出。\n\n3/ 文化背景是关键调节器\n- 在“男性气质”强、偏短期导向的社会，科技公司雇佣女性高管的负面效应更明显。\n- 在“个人主义”弱、长期导向强的文化中，科技公司反而更愿意监控碳排放和提供培训。\n\n4/ 监管环境：双刃剑\n- 监管负担越低，科技公司越愿意监控碳排放和提供培训（灵活性高）。\n- 但监管负担降低，反而扩大了性别差距（推测女性高管在低监管环境下更易被挤出）。\n\n一个开放问题：为什\n\n[... middle omitted ...]\n\nen of business regulation, and the perception of the courts as an obstacle to business activity. This underscores the importance of the broader society and the quality of the business environm\n\n[... middle omitted ...]\n\nf the courts are perceived as a major/very severe obstacle to the current operations of the firm, and zero if the courts are perceived as either a minor/moderate obstacle or not perceived as an obstacle</td></tr></table>"
  },
  {
    "id": "R037",
    "title": "世界银行：减税救不了实体经济，别再迷信企业税收优惠了",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：减税救不了实体经济，别再迷信企业税收优惠了\n\n税收优惠是全球政府吸引投资最常用的工具。OECD数据显示，2022年87%的发展中经济体至少提供一种企业所得税减免。世界银行的研究估计，2021年全球企业税收减免规模相当于全球GDP的1.4%、全球税收收入的7.8%。\n\n但一个根本问题始终悬而未决：这些动辄占GDP数个百分点、耗资巨大的优惠政策，真的带来了就业、产出和投资增长吗？\n\n世界银行最新发布的工作论文《The Elusive Impact of Corporate Tax Incentives》，用突尼斯出口企业税收优惠改革的自然实验，给出了一个反直觉但严谨的答案：税收优惠能吸引企业注册，但注册数量的增加并不转化为真实经济活动。换言之，大量政策投入可能只是在“制造公司壳子”，而非创造经济价值。\n\n这份研究对当前中国地方政府招商引资、产业园区政策设计，以及全球税制改革讨论，都有直接借鉴意义。\n\n> **KC评论：** 世界银行这篇论文的核心判断是，企业税收优惠对经济的拉动作用远低于政策制定者的预期。它区分了两个概念：企业注册数量和经济活动总量。前者对税收敏感，后者几乎不敏感。这意味着，如果政策目标只是让更多公司出现在工商登记簿上，减税确实有效；但如果目标是增加就业、提高工资、扩大产出，减税可能不是最优工具。完整报告提供了详实的因果识别策略和稳健性检验，值得仔细推敲其方法论边界。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 突尼斯实验：一个罕见的“干净”政策冲击\n\n世界银行选择突尼斯作为研究场景，是因为这里发生了一次罕见且近乎理想的政策变动。突尼斯长期实行“离岸”与“在岸”双轨税制：出口企业（离岸）享受零企业所得税，内销企业（在岸）面临30%税率。这个离岸免税政策自1972年实施以来，历经多次延期，企业早\n\n[... middle omitted ...]\n\n略咨询公司和智库的朋友，期待与你一起观察全球经济的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n企业税优惠真的能拉动经济吗？\n\n税收优惠未必奏效\n\n一项最新研究发现，税收激励的效果可能被高估了\n\n投行研报解析：突尼斯出口企业税收改革告诉我们什么？\n\n1/ 很多人认为给企业减税就能刺激投资、带动就业，但真实世界的数据并不总是支持这个逻辑。某外资投行最近发布了一份基于突尼斯企业税收改革的研究，结论很反直觉：取消税收优惠后，新企业进入减少了20%，但就业、营收、工资总额竟然没受影响。\n\n2/ 怎么回事？关键原因是：存量企业才是经济的主体。新进入的企业通常规模很小，而大企业才是就业和产出的主力。税收改革后，这些大企业既没有搬走也没有裁员，所以整体经济没受冲击。\n\n3/ 研究用的是“双重差分法”，比较出口企业（税收优惠取消）和内销企业（税率同时下调）在改革前后的差异。数据覆盖了突尼斯所有注册企业，时间跨度从2010年到2018年，可信度很高。\n\n4/ 这个结论和很多其他研究吻合：企业选址更看重基础设施、劳动力成本、政治稳定性，税收优惠排位并不靠前。对于发展中国家来说，放弃大量税收收入去吸引投资，可能得不偿失。\n\n5/ 当然也有反例。美国的一些研究表明，降低有效税率确实能刺激投资。但综合来看，税收激励的效果在\n\n[... middle omitted ...]\n\nhe incentives. However, the reduced entry did not translate into any effects on employment, revenue, or the wage bill, as the reform did not impact the activities of incumbent firms, which acc\n\n[... middle omitted ...]\n\ned to firms in the manufacturing sector. Mbar refers to multiples of the largest deviation from parallel trends in the pre-period (i.e. Mbar = 0.8 considers a deviation equals to 80% of the largest pre-period deviation)."
  },
  {
    "id": "R038",
    "title": "世界银行：AI对低收入国家劳动力的冲击，可能远小于市场预期",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：AI对低收入国家劳动力的冲击，可能远小于市场预期\n\n当全球资本市场的注意力几乎全部集中在生成式AI如何颠覆高收入国家白领工作时，一份来自世界银行的最新研究却指向了一个被严重忽视的方向：对于占全球人口近一半的低收入和中等收入国家，AI的劳动力市场冲击可能远比想象中有限。\n\n这份由Gabriel Demombynes、Jörg Langbein和Michael Weber撰写的政策研究工作论文，分析了覆盖35亿人口的25个国家的微观数据，得出了一个与主流叙事形成鲜明对比的核心判断：AI的暴露度与国家收入水平呈正相关，且低收入国家的基础设施瓶颈——尤其是电力供应的缺乏——构成了AI渗透的实质性物理天花板。\n\n这不是一份关于“AI将如何消灭发展中国家工作岗位”的悲观预测，而是一份冷静的、基于数据的结构性分析。它告诉我们，在谈论AI对全球劳动力的影响时，必须首先区分“可能性”与“现实性”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 一个反直觉的事实：国家越穷，AI暴露度越低\n\n报告的核心发现建立在一个精心构建的AI职业暴露指数（AIOE）之上。该指数将每个职业的AI暴露度标准化为0到100的区间。结果呈现出清晰的阶梯状分布：美国作为高收入国家的代表，平均暴露度高达62；上中等收入国家为49；下中等收入国家为44；而低收入国家仅为37。\n\n这意味着什么？在低收入国家，只有约12%的劳动力处于高AI暴露度的职业中，而在高收入国家，这一比例接近四分之一。这种差异不是统计噪声，而是经济结构的系统性反映。低收入国家的就业结构仍然以农业和低技能服务业为主，这些领域的任务构成与当前AI的能力边界之间存在显著鸿沟。\n\n> **KC评论：** 市场常常将“AI替代工作”视为一个全球统一的线性进程。但世界银行的这份报告提醒我们，AI\n\n[... middle omitted ...]\n\n据和图表，观测边际变化，共同探讨AI时代的新兴市场投资逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI对不同国家的影响，差距比想象中大\n\nAI对不同国家劳动者影响有多大？\n\n某外资投行最新研报，覆盖25国35亿人，结论很清晰：\nAI对低收入国家影响远小于高收入国家。\n\n核心发现：\n1️⃣ 美国劳动者AI暴露度62分，低收入国家仅37分\n2️⃣ 高收入国家60%岗位受AI影响，低收入国家仅26%\n3️⃣ 女性、城市居民、高学历人群AI暴露度更高\n4️⃣ 电力不足是低收入国家AI应用的关键瓶颈\n\n关键解读：\n- AI暴露≠失业，可能是提效工具\n- 白领岗位受冲击最大\n- 发展中国家农业和低技能服务业占比高，AI影响有限\n\n有意思的细节：\n在低收入国家，只有12%的劳动者属于高AI暴露群体\n而高收入国家这个比例是60%\n\n这说明什么？\nAI对劳动力市场的冲击不是均匀的\n国家发展阶段决定了AI的渗透深度\n\n欢迎一起讨论：你觉得这对发展中国家是机会还是挑战？\n\n#学习笔记\n\n[source_mineru.md]\n11057\n\n# The Exposure of Workers to Artificial Intelligence in Low- and Middle-Income Countries\n\nGabrie\n\n[... middle omitted ...]\n\n The approach advances work by using harmonized microdata at the level of individual workers, which allows for a multivariate analysis of factors associated with exposure. Additionally, unlike\n\n[... middle omitted ...]\n\n8.65***</td><td>26.46***</td><td>24.19***</td></tr><tr><td>(1.26)</td><td>(6.56)</td><td>(30.59)</td><td>(19.99)</td></tr><tr><td>Observations</td><td>123780</td><td>814562</td><td>1269224</td><td>82189</td></tr></table>"
  },
  {
    "id": "R039",
    "title": "世界银行：一场降雨如何重塑印度农村经济的全部链条",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界银行",
    "digest": "[wechat_article.md]\n# 世界银行：一场降雨如何重塑印度农村经济的全部链条\n\n一份来自世界银行的最新研究，以印度最大的农业邦拉贾斯坦邦为样本，系统拆解了降雨冲击如何沿着“农业产出——非农企业——家庭消费”这条链条逐级传导，并最终放大或收缩整个农村经济的总产出。研究结论清晰且有力：降雨冲击对非农企业收入和增值的影响，远大于对农业本身的直接影响。这一发现，对于所有关注新兴市场农村经济、气候变化适应能力以及农业政策设计的人来说，都构成了一次认知上的必要升级。\n\n这份报告的核心判断不是“降雨影响农业”——这早已是共识。它的真正贡献在于，用严格的因果识别方法，量化了降雨冲击通过农业这个“放大器”，如何对看似无关的农村零售、服务等非农部门产生数倍于农业的冲击力。这意味着一场旱灾摧毁的不仅是庄稼，更是整个乡村经济体系的购买力、就业机会和抗风险能力。反过来，一场好雨带来的繁荣，也远不止是粮仓丰满那么简单。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 正面降雨冲击让农业产出提升7%，但灌溉设施是关键的“减震器”\n\n研究首先确认了一个基础事实：相较于负面降雨冲击，正面降雨冲击能够使拉贾斯坦邦的农业综合生产率提升约7%。这个数字本身并不令人意外，但报告揭示了一个关键的调节变量——灌溉基础设施。灌溉面积占比越高的地区，降雨冲击对农业生产率的影响就越小。换句话说，灌溉不仅是在干旱年份保产，更是在所有年份中平滑掉农业产出的剧烈波动，让农民的收入预期更加稳定。\n\n这7%的提升，是后续所有连锁反应的起点。它意味着农民和农业相关从业者口袋里的钱变多了。而这笔增量收入，不会全部存起来，它必然流向消费和投资。这正是理解农村经济循环的关键入口。\n\n> **KC评论：** 7%这个数字看似不大，但它是一个“平均效应”。对于没有灌溉条件的雨养农业区，这个冲击的实际影响可能远超7%。报\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询和智库的朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n下雨多，农村反而更赚钱？\n\n🌧️ 降水冲击=经济变量\n\n**下雨多，农业增产7%，但连锁反应远不止于此。**\n\n最近读了一份某外资投行关于印度拉贾斯坦邦的研报，把“下雨”这个自然现象拆解成了农村经济的完整传导链，逻辑很清晰，分享给大家。\n\n**1. 下雨→农业：增产7%，但灌溉是关键**\n- 正向降水冲击（多雨年）能让农业生产力提升约7%。\n- 但灌溉基础设施能显著“对冲”这种波动，有灌溉的地区，降水影响就没那么大。\n\n**2. 农业→非农生意：连锁反应更猛**\n- 农业增产带来的“溢出效应”惊人：农村非农企业（尤其是零售店）的收入能增加25.7%，附加值提升30.3%。\n- 核心逻辑：农民手里有钱了，会去村里买更多消费品（非贸易品），带动本地小生意。\n\n**3. 家庭消费：钱花在哪？**\n- 多雨年，农村家庭月人均支出增加6%。\n- 这笔钱主要花在**“奢侈品”**（非必需品，比如娱乐、耐用品）上，而不是米面粮油。这正好解释了为什么零售店生意最好——需求端拉动了非农企业。\n\n**总结一下：**\n降水冲击 → 农业产出变化 → 农民收入变化 → 本地消费变化（偏向非必需品） → 非农企业（零售）业绩波动。\n\n[... middle omitted ...]\n\nhocks increase agricultural productivity by approximately 7 percent compared to negative shocks, with irrigation infrastructure significantly moderating this effect. Second, these weather-indu\n\n[... middle omitted ...]\n\ntd> $R^2$ </td><td>.78</td><td>.78</td><td>.78</td><td>.78</td><td>.78</td><td>.78</td></tr><tr><td>Dep Var Mean</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td></tr></table>"
  },
  {
    "id": "R040",
    "title": "波士顿咨询：CEO们搞砸AI转型的五个共同死穴",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CEO们搞砸AI转型的五个共同死穴\n\nAI的能力似乎无限，其变革潜力看似没有边界。但一个残酷的事实是，绝大多数CEO正在将这场技术革命搞砸。\n\n波士顿咨询(BCG)最近一项研究给出了一个令人不安的数据：只有5%的公司能从AI中持续产生利润表(P&L)层面的实质影响，而大约60%的公司几乎没有看到任何实质性收益。这不是技术问题。这是转型纪律的溃败。\n\nAI转型之所以比其他转型更棘手，在于它的两个独特属性：一是它能在早期快速展现成果，制造出“进展神速”的假象，而真正困难的工作——重新设计决策权、重塑专业知识应用方式、调整全价值链激励——却隐蔽且困难，常常被忽略。二是AI的大部分影响是间接的。它改善判断、生产力和洞察力，但这些财务效果是二阶的、脆弱的，除非被刻意捕获。\n\n这种“早期可见性、系统性颠覆和间接价值”的组合，使AI转型天生就容易表现不佳。CEO们必须首先承认这一点，然后才能开始解决问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 碎片化试水是最大的价值陷阱\n\n90%的公司至少在进行AI实验。但问题在于，他们停留在实验阶段太久，只迈出“婴儿步”，获取有限的效率提升。这些零散的努力缺乏实现持久P&L影响所需的规模和整合深度。\n\n根据BCG的估算，约70%的AI价值潜力集中在核心业务流程工作流中——即决策、成本和结果交汇之处。碎片化试水不仅浪费资源，更致命的是，它让组织误以为自己“已在路上”，从而延迟了真正需要的根本性变革。\n\nCEO必须亲自驱动AI努力，寻求对企业核心环节进行有目的、深层次的再造。仅仅提高某个环节的效率，与重新设计整个价值链，是完全不同的两件事。\n\n> **KC评论：** 很多企业把AI当成“锦上添花”的工具，用它来优化一个客服流程或一个生产环节。但BCG的数据告诉我们，真正的价值藏在\n\n[... middle omitted ...]\n\n国际主流叙事、数据与图表，观测这场变革的每一个关键信号。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI转型不成功，问题不在技术\n\nCEO们，别被AI的“快”骗了\n\n真正难的是组织重构和价值落地\n\n最近读了一份某外资投行的研报，核心观点很直接：AI转型失败，90%是管理问题，不是技术问题。\n\n1️⃣ 别只做“小步快跑”的实验\n90%的企业都在试AI，但只有5%真正产生了持续的利润影响。问题出在：大家停留在“试点”阶段，没敢动核心业务流程。70%的AI价值其实藏在核心流程里，CEO需要亲自带队，用AI重新设计价值链。\n\n2️⃣ 钱没给够，效果出不来\n2026年企业AI投入预计翻倍，但很多CEO低估了“最后一公里”的成本。从70分做到95分，需要大量投入在数据基础、流程工业化、跨部门协同上。早期小成果反而容易让人误判，导致资金链断裂。\n\n3️⃣ 没有价值蓝图\n很多AI项目只盯着效率提升，但效率不等于利润。研报指出，没有明确价值逻辑的项目，10%-20%的预期价值会在落地前蒸发。CEO必须在启动前就画好“从效率到利润”的路径图，让CFO和财务团队从第一天介入。\n\n4️⃣ 别用“运动量”代替“结果”\n很多团队展示的是“AI使用率”“自动化任务数”这类指标，但这些不等于财务回报。需要建立P&L直接挂钩的KPI，设阶段\n\n[... middle omitted ...]\n\nmation discipline. At the same time, AI transformations differ from other transformations in two ways.\n\n\\- AI delivers visible results quickly, creating the impression of fast progress. Howeve\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R041",
    "title": "波士顿咨询：企业转型的成败，终于被拆解到了“人”这一层",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：企业转型的成败，终于被拆解到了“人”这一层\n\n企业转型的失败率，远比多数高管愿意承认的要高。波士顿咨询（BCG）的最新研究给出了一个冷峻的数字：只有大约四分之一的组织转型，能够同时捕获短期与长期价值。换言之，四分之三的努力，要么中途折戟，要么昙花一现。\n\n但这份报告的价值，不在于重复“转型很难”这个共识，而在于它找到了那四分之一的成功者与其余失败者之间最关键的差异。答案不在战略蓝图，不在技术工具，也不在组织架构的调整——而在于一个长期被低估、被简化为“沟通培训”或“文化口号”的变量：人。\n\nBCG 的结论是：那些将行为科学原则系统性地嵌入转型全过程的企业，其股东总回报（TSR）比同行高出 15%。这并非软性的“员工关怀”，而是一个可量化、可复制的竞争优势来源。本文基于这份研报，拆解其核心洞察，并追问那些报告没有完全展开的深层问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 转型失败的根源不是战略错误，而是对“人的惯性”的漠视\n\n所有转型都试图回答三个问题：为什么转（Why）、转什么（What）、怎么转（How）。绝大多数企业在前两个问题上投入了不成比例的资源——宏大的愿景、精准的财务目标、详尽的业务组合调整。但问题恰恰出在第三个环节：How。\n\nBCG 的研究指出，转型本质上依赖人们改变行为的意愿。然而，人类天生厌恶变化。这不是态度问题，而是认知机制。行为科学告诉我们，人们在面对不确定性和额外认知负荷时，会本能地退回旧有模式。因此，无论“为什么”多么动人，“转什么”多么合理，如果“怎么转”的设计忽视了这一人性底层逻辑，转型就注定在落地阶段被消耗殆尽。\n\n这意味着，企业需要将“人”从转型的被动接受者，转变为主动参与者。这不是一句口号，而是一套可操作的方法论。报告给出了四个具体维度：领导者赋能（Leade\n\n[... middle omitted ...]\n\n表，观测边际变化。扫码交流，获取更多国际信源汇编与深度评论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n只有1/4的组织变革能成功，关键差异在哪里？\n\n人本变革才是核心\n\nBCG研究发现，四分之三的变革项目折戟，成功的那1/4都有个共同点——把人放在中心。\n\n1/ 为什么人本变革更有效？\n人天生抗拒变化，但变革又必须靠人推动。行为科学告诉我们，与其强迫改变，不如设计让人愿意改变的环境。数据显示，把人本管理融入变革的公司，股东回报率高出同行15%。\n\n2/ 四个关键抓手\n- 领导赋能：不只是发号施令，要让管理者成为变革的“翻译官”，把“为什么变”讲清楚，用同理心替代命令式管理。\n- 员工参与：别只盯着KPI，要评估变革对团队的实际冲击。定期做脉搏调查、开全员会，让员工感觉被听见。\n- 执行确定性：设立变革办公室，用阶段性关卡和透明报表，确保方向不跑偏。\n- 文化重塑：诊断现有文化，让领导层带头示范新行为，比如想提升透明度，就每月分享核心报告。\n\n3/ 真实案例：一家全球饮料公司\n通过聚焦“怎么变”而非“变什么”，供应链成本降了15-20%，生产力提升55%。250位领导接受了定制化赋能，95%的员工理解变革目标，80%以上给出好评。\n\n变革不是画蓝图，而是让每个人都成为变革的一部分。欢迎一起讨论你们公司的变革经验\n\n[... middle omitted ...]\n\nrch from BCG's Bruce Henderson Institute and the firm's Behavioral Science Lab points to a crucial factor: a human-centric approach.\n\nHuman-centric transformations are grounded in, and informe\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R042",
    "title": "波士顿咨询：营销的“旅程”时代已死，“代理”时代已来",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：营销的“旅程”时代已死，“代理”时代已来\n\n当大多数企业还在费力优化客户旅程的每一步时，一份来自波士顿咨询的最新报告抛出了一个颠覆性的判断：以“旅程”为核心的个人化策略，其增长红利已经见顶。未来12到18个月，决定企业营销效率分野的关键，不再是设计更长的旅程，而是转向由AI代理实时编排的“原子化动作”。\n\n这份报告的核心主张清晰而锐利：营销决策的单位，必须从“旅程”切换到“动作”。这不是技术的渐进改良，而是架构的根本重构。对于任何在营销上投入巨大、却感觉ROI越来越难提升的组织，这份报告提供了一个不容忽视的战略预警和行动路线图。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 旅程模式的增长已触顶，其结构性缺陷无法通过优化修补\n\n过去十年，“客户旅程”是营销组织的黄金法则。通过精心设计从认知到购买的每一步，企业能够系统性地转化用户。波士顿咨询的报告明确指出，这套模式在今天的环境中已经“平台化”——它的效能增长曲线已经趋于平缓。\n\n原因在于，旅程模式是一个“确定性”的架构。它假设用户会按照预设的路径前进，但现实是：渠道爆炸式增长，客户信号在实时涌现，可用的内容、优惠和体验组合呈指数级膨胀。为了覆盖更多场景，企业不得不创建成百上千条旅程，但每一条新旅程都需要手动设计、测试和部署。这导致一个悖论：试图通过增加旅程数量来提升覆盖率，反而让营销团队的管理负担超出了其承载能力。\n\n**所以呢？** 对于任何依赖大规模营销的企业，继续在现有旅程框架内修修补补，投入产出比将加速递减。这不是运营效率的问题，而是架构天花板的问题。下一阶段的增长，不可能通过“优化”当前模式来实现。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 下一代营销架构的决策单元，将从“旅程步骤”变为“原子动作”\n\n波\n\n[... middle omitted ...]\n\n和产业一线的朋友，共同观测和讨论这些边际变化。期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n个性化营销，进入Agent时代\n\nAI Agent接管营销决策\n\n营销人从设计旅程，到策划内容货架\n\n某外资投行最新研报指出，传统客户旅程模型的效果已经见顶。核心问题：渠道太多、信号实时、内容爆炸，靠人力设计旅程根本跟不上。\n\n**1/ 三个进化阶段**\n- 阶段1：人工设计旅程，每推新品就建新流程，团队累死\n- 阶段2：模型优化旅程，AI在预设框架内选最优分支\n- 阶段3：AI Agent自主决策，营销人只负责“组货”和定目标\n\n**2/ 核心变化：从“旅程”到“原子动作”**\n以前决策单位是“整条旅程”，现在变成“每个微观动作”。Agent能实时从货架上挑选、排序、组合内容，几小时就能上线个性化活动，不用等几周。\n\n**3/ 四大能力支柱**\n- 可组合货架：内容、优惠、模板都打上标签，模块化管理\n- Agent架构：专业Agent分工协作，灵活调用工具\n- 工具层模块化：每个模型、数据源都做成可调用的API\n- 持续学习：每次交互都做因果测试，越用越聪明\n\n**4/ 一个真实场景**\n客户刚处理完盗刷投诉，打开银行App。传统系统还在推分期优惠，Agent却能识别这是“重建信任”时刻，自动推送安全确认+\n\n[... middle omitted ...]\n\npossible content, offers, and experiences has grown substantially.\n\nAs a result, the journey model's impact has plateaued. Personalization must evolve by changing its unit of decision from mar\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R043",
    "title": "波士顿咨询：营销战役的终结，不是营销的终结",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：营销战役的终结，不是营销的终结\n\n如果你还认为营销的核心是“策划一场漂亮的战役”，那么波士顿咨询公司（BCG）这份最新报告，可能会让你重新审视整个职业的底层逻辑。\n\nBCG 在这份题为《The End of Marketing Campaigns as We Know It》的报告中，提出了一个直接且尖锐的判断：以“战役”和“日历”为核心的传统营销组织方式，正在走向终结。取而代之的，是一套由 AI 智能体（Agent）驱动的、以“下一最优行动”为核心的实时响应系统。\n\n这并非一个渐进式的优化，而是一次对营销执行价值链的彻底重构。报告的核心洞察在于，技术本身已不再是瓶颈，真正的挑战在于改变“人”的工作方式、组织的协作逻辑，以及企业的决策治理体系。\n\n这份报告的价值，不在于描绘一个遥远的未来图景，而在于给出了一个可操作、可量化的转型路径。它告诉你，从今天起，你的团队结构和日常节奏，应该发生怎样的变化。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 70%到80%的客户触点，将不再由“战役”驱动\n\nBCG 报告中最具冲击力的一个数字是：在成熟的智能体原生模式下，70%到80%的客户触点将从预定义的营销战役，转向由 NBA 驱动的实时交互。这意味着，“战役”将从营销工作的核心单元，退化为只服务于品牌大事件、产品首发或合规通讯等少数例外场景的“特例”。\n\n传统营销的逻辑是：先有目标，再有受众，然后是创意，最后是排期。一切围绕“日历”展开。而智能体原生的 NBA 完全颠倒了这个逻辑：系统从每一个具体的客户出发，实时从“可组合货架”上抓取最合适的行动。预定义的受众消失了，取而代之的是实时的上下文定位。\n\n> **KC评论：** 这里的关键不在于“战役”会消失，而在于营销团队的核心工作流发生了根本性迁移。过去，你的团队花\n\n[... middle omitted ...]\n\n行业边际变化。欢迎扫码加入交流，获取完整报告解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n营销的终点是“没有营销”\n\n告别营销战役\n\n某顶级咨询研报提出，未来70%~80%的客户触点将从预设战役转向AI实时决策。这不是科幻，是正在发生的组织变革。\n\n1/ 从“排期表”到“组合货架”\n传统营销按日历排战役，把客户分群、统一推送。新逻辑反过来了：系统实时感知每个客户的需求，从“组合货架”上抓取最适合的动作。货架上存的是模块化的内容、优惠和微旅程，AI代理负责组装。\n\n2/ 构建侧 vs 交付侧\n营销团队裂变成两拨人：构建侧（人类+AI协作生产内容、审批、上架），交付侧（完全由AI代理执行1对1实时触达）。构建周期从60~90天压缩到几天，人力减少60%，内容产出量暴增10~100倍。\n\n3/ 决策治理是安全阀\nAI不能乱跑。需要跨部门的“决策治理”来定目标函数（比如这季度主推交叉销售，下季度转向留存），并设置边界：高频低风险动作让AI自主，高价值或策略性动作必须人类审批。\n\n4/ 营销人的新角色\n不再是“发战役的人”，而是策略师、策展人、治理架构师。每天审仪表盘、调约束条件、批创意变体。一个VP级营销负责人，可能早上花4分钟就管理了数万次客户互动。\n\n未来已来，只是分布不均。你所在的组织，准备好重构工\n\n[... middle omitted ...]\n\nving. Now comes the hardest part: changing the prevailing ways of working.\n\nCompanies need to address three key aspects of the broader marketing operating model. The first is a shift in how or\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R044",
    "title": "波士顿咨询：下一代“最佳下一步行动”不是算法升级，是决策架构的重构",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：下一代“最佳下一步行动”不是算法升级，是决策架构的重构\n\n绝大多数企业当前部署的“最佳下一步行动”系统，本质上仍是一个更聪明的排序器。它根据历史数据，给每个客户打一个响应概率分，然后选出分数最高的那个动作。波士顿咨询在最新发布的系列研究报告第三部分中，提出了一个截然不同的判断：这套范式正在触及天花板。真正能带来下一轮增长差异的，不是把模型从XGBoost换成Transformer，而是从根本上重构营销决策的架构——从“预测并排序”转向“探索、推理与组合”。\n\n这份报告的核心洞察在于，未来有效的NBA系统需要同时运行三层决策引擎：倾向性评分、情境化Bandit算法，以及基于基础模型的智能体推理。这三层不是演进关系，而是叠加关系。大多数企业目前只运行了第一层，而真正拉开差距的能力，藏在后两层。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 倾向性模型的三个结构性局限，决定了它无法承载下一阶段个性化\n\n波士顿咨询的报告直接点明了当前主流做法的天花板。倾向性模型，即便是加入了增量建模的Uplift模型，也存在三个无法通过调参或增加特征来解决的结构性问题。\n\n第一，它们无法提供真正的“处方”建议。一个倾向性模型能告诉你“客户A有90%的概率会响应”，但它回答不了“这个响应是因为你的动作，还是客户本来就要买”。报告指出，转向Uplift模型的企业通常会发现自己20%到40%的活跃营销项目几乎没有带来任何增量效果，它们只是在捕获本来就会发生的意图。这意味着大量营销预算被浪费在了“奖励已转化意图”上。\n\n第二，它们无法发现新的组合。倾向性模型只能在一个预设的动作空间内做排序。如果营销人员定义了15个优惠，模型就只在这15个里面挑。它永远无法发现，把一个小额优惠与某个特定内容框架、在一个非标准时间、通过特定渠道组合起来，效\n\n[... middle omitted ...]\n\n构的朋友，每日更新国际主流叙事与边际变化，期待与你交流。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNBA 系统背后的三层决策科学\n\n三层决策，一次讲透\n\n从打标签到真智能，NBA系统升级路径\n\n---\n\n最近读了一篇某外资投行关于Next-Best Action的研报，很有启发。它把个性化推荐系统拆成了三层，逻辑非常清晰。\n\n**1. 第一层：倾向性评分**\n这是目前大多数公司的做法。用历史数据训练模型，预测用户对某个动作（比如发优惠券）的反应概率。然后按分数排序，选最高的去执行。\n*   **优点**：成熟、可解释、效果好，是基础。\n*   **缺点**：只能在你定义好的动作里选，发现不了新组合；没法处理“今天发券会影响明天决策”的连续性问题。\n\n**2. 第二层：情境赌博机**\n这层的关键是“探索-利用权衡”。系统不再只选“看起来最好”的动作，而是会故意分出一些流量去尝试“不确定好不好”的动作，从而学习真实效果。\n*   **核心算法**：汤普森采样比简单的贪心算法更优，它能根据不确定性自动调节探索频率。\n*   **案例**：一个信用卡发卡机构，传统模型只发现高余额、长时长的用户适合做余额转账。但情境赌博机发现，配上特定创意，新激活的中等余额用户响应率更高——历史数据里根本没有这个组合。\n\n**3.\n\n[... middle omitted ...]\n\nearning loops that compound without human intervention, and a layered architecture with different classes of algorithms.\n\nThis shift requires different applications and a fundamental evolution\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "国际清算银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "国际清算银行｜国际清算银行：全球经济的“韧性”已到极限，下一步是“稳健性”还是危机？｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Turkiye: defence spending, 1980–2024 Note: Figures in Turkish lira reflect the revaluation in 2005, which removed six zeros from the currency. Sources: NATO, 'Financial and Economic Data Relating to NATO Defence'; Mili"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Turkiye: defence spending, 1980–2024 Note: Figures in Turkish lira reflect the revaluation in 2005, which removed six zeros from the currency. Sources: NATO, 'Financial and Economic Data Relating to NATO Defence'; Mili"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Turkiye: defence and aerospace imports, 2012–22 SSM was placed under the direct authority of the presidency in 2018. It was accordingly renamed the Defence Industry Agency (Savunma Sanayii Başkanlığı, SSB). This upgrad"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Turkiye: defence and aerospace exports, 1997–2023 In stark contrast to the bottom-up, purely technical and price-based considerations that led to the selection of the Chinese FD-2000 air- and missile-defence system in"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Turkiye: defence and aerospace exports, 1997–2023 In stark contrast to the bottom-up, purely technical and price-based considerations that led to the selection of the Chinese FD-2000 air- and missile-defence system in"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "布鲁金斯学会视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁金斯学会｜布鲁金斯学会：土耳其军工从“客户”到“对手”，全球供应链正在被改写｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "布鲁金斯学会视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁金斯学会｜布鲁金斯学会：中美AI对话的真正价值不在信任，而在共同恐惧｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F009",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Second, household credit has recently become the main driver of credit growth across much of the region. In most countries, household lending now exceeds corporate credit. Household loans have long accounted for the larger share of private sector credit in "
  },
  {
    "figure_id": "F010",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Third, credit cycles in the region have been highly volatile. Kazakhstan, Azerbaijan, and Tajikistan experienced sharp credit contractions following banking sector stresses in late 2000s-mid-2010s, with the credit-to-GDP ratios falling by 15–20 percentage p"
  },
  {
    "figure_id": "F011",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Fourth, the currency composition of credit has shifted over time. FX lending was historically dominant in the region, exposing borrowers and banks to exchange rate risks. However, loan dollarization has declined significantly in recent years, with the share"
  },
  {
    "figure_id": "F012",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Evolution of Total, Household, and Corporate Credit Across CCA Economies (In percent of GDP) Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates."
  },
  {
    "figure_id": "F013",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Figure 2. Credit Decomposition by Currency of Denomination"
  },
  {
    "figure_id": "F014",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Figure 2. Credit Decomposition by Currency of Denomination"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Figure 2. Credit Decomposition by Currency of Denomination"
  },
  {
    "figure_id": "F016",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Figure 2. Credit Decomposition by Currency of Denomination"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Figure 2. Credit Decomposition by Currency of Denomination"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Figure 2. Credit Decomposition by Currency of Denomination"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Credit Decomposition by Currency of Denomination Sources: National central banks, and authors' estimates."
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "\\- In Tajikistan, the actual credit-to-GDP ratio has been in the equilibrium range but has shown limited increase, underscoring limited banking depth. Overall, the emerging-market equilibrium model highlights three main findings. First, most CCA countries rema"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Overall, the emerging-market equilibrium model highlights three main findings. First, most CCA countries remain under-credited relative to fundamentals. Second, convergence dynamics are uneven: Armenia, Georgia, and to some extent Kyrgyzstan and Uzbekistan are"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "In sum, the analysis indicates that, while financial deepening remains incomplete, the region has made tangible progress toward equilibrium levels of credit. The next section turns to the cyclical dimension—credit-to-GDP gaps—to evaluate how the speed of credi"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Deviation from the Equilibrium Level Credit -to-GDP Ratio Sources: BIS; IMF, International Financial Statistics; IMF Financial Development Index database; World Bank, World Development Indicators; national authorities; and authors' estimates."
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "\\- In the Kyrgyz Republic, most gap measures were slightly negative but credit was rising fast, with the moving-average and HP-filter based measures approaching zero and the five-year growth rate turning modestly positive. In Tajikistan, the moving-average and"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "\\- In the Kyrgyz Republic, most gap measures were slightly negative but credit was rising fast, with the moving-average and HP-filter based measures approaching zero and the five-year growth rate turning modestly positive. In Tajikistan, the moving-average and"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "\\- In Uzbekistan, the indicators point to a continued moderation in credit dynamics. The moving-average and Christiano–Fitzgerald filters remained slightly above zero, suggesting that credit-to-GDP was still somewhat above trend, while the Hamilton filter was "
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Credit Gap Measures for the CCA Economies Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates. Note: Credit gaps computed as deviations of the credit-to-GDP ratio from its trends using four different fi"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "\\- In Uzbekistan, the short data series complicates assessment, but both filters are slightly negative, and the five-year growth rate is flat, implying that corporate credit is broadly aligned with its trend following the earlier surge after financial liberali"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "\\- In Uzbekistan, the short data series complicates assessment, but both filters are slightly negative, and the five-year growth rate is flat, implying that corporate credit is broadly aligned with its trend following the earlier surge after financial liberali"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Taken together, these patterns suggest that corporate credit across the CCA is recovering from a prolonged period of weakness, with early signs of recovery in Azerbaijan, Kazakhstan, and the Kyrgyz Republic, and small negative gaps narrowing rapidly in Armenia"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Household Credit Gap Measures for the CCA Economies Sources: National authorities, and authors' estimates."
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: National authorities, and authors' estimates. Note: Credit gaps computed as deviations of the household-credit-to-GDP ratio from its trends using four different filters: two-sided HP filter, Hamilton filter, Christiano–Fitzgerald filter, and a moving-"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: National authorities, and authors' estimates. Note: Credit gaps computed as deviations of the household-credit-to-GDP ratio from its trends using four different filters: two-sided HP filter, Hamilton filter, Christiano–Fitzgerald filter, and a moving-"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: National authorities, and authors' estimates. Note: Credit gaps computed as deviations of the household-credit-to-GDP ratio from its trends using four different filters: two-sided HP filter, Hamilton filter, Christiano–Fitzgerald filter, and a moving-"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: National authorities, and authors' estimates. Note: Credit gaps computed as deviations of the household-credit-to-GDP ratio from its trends using four different filters: two-sided HP filter, Hamilton filter, Christiano–Fitzgerald filter, and a moving-"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Note: Credit gaps computed as deviations of the household-credit-to-GDP ratio from its trends using four different filters: two-sided HP filter, Hamilton filter, Christiano–Fitzgerald filter, and a moving-average benchmark. Left axis: gap in percentage points "
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6. Corporate Credit Gap Measures for the CCA Economies Sources: National authorities, and authors' estimates."
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "\\- a credit equation in which the credit gap responds to lagged output, its own persistence, and the real interest-rate gap. This structure ensures that credit booms are interpreted in the context of strong growth, accommodative real rates, and improving labor"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "This structure ensures that credit booms are interpreted in the context of strong growth, accommodative real rates, and improving labor markets, rather than simply as deviations from a smooth statistical trend. In the Kazakhstan–Russia application, Russia is m"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Pesaran, M. H., Shin, Y., & Smith, R. P. (1999). \"Pooled Mean Group Estimation of Dynamic Heterogeneous Panels,\" Journal of the American Statistical Association, 94(446), 621–634. Ravn, M. O., and Uhlig, H. (2002). \"On adjusting the Hodrick-Prescott filter for"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Ravn, M. O., and Uhlig, H. (2002). \"On adjusting the Hodrick-Prescott filter for the frequency of observations.\" Review of Economics and Statistics, 84(2), 371–376. ## Annex I. Equilibrium (Large Economies) Figure 1. Deviation from the Equilibrium Level Credit"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Annex I. Equilibrium (Large Economies) Figure 1. Deviation from the Equilibrium Level Credit-to-GDP Ratio, Large Economies reference panel (In percent of credit to GDP)"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Deviation from the Equilibrium Level Credit-to-GDP Ratio, Large Economies reference panel (In percent of credit to GDP) Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII)"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Deviation from the Equilibrium Level Credit -to-GDP Ratio, Large Economies Reference panel (without FII) # Annex II: Multivariate Filter Estimation for Kazakhstan"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：中亚信贷扩张的结构性机会与周期性隐忧｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F052",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 shows the dynamics of FMs status over time for a sample of countries that changed status between 1993 and 2022. This figure shows that several countries have transitioned to FM status in the aftermath of the GFC, a period characterized by accommodativ"
  },
  {
    "figure_id": "F053",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2 also reveals that the higher attractiveness of FMs as a destination for foreign investments is driven by post-2013 years, coinciding with higher yields in EMDEs and substantial Official Development Assistance flows from China attracting foreign invest"
  },
  {
    "figure_id": "F054",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Overall, descriptive statistics indicate that FMs typically exhibit stronger economic performance and governance than NFLICs, with noticeable gains leading up to their transition. Cross-Group Comparison Dynamics Surrounding Transition to FM Status (in years) O"
  },
  {
    "figure_id": "F055",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Cross-Group Comparison Dynamics Surrounding Transition to FM Status (in years) OUTPUT GROWTH FDI FLOWS (% GDP) BUDGET BALANCE (%GDP)"
  },
  {
    "figure_id": "F056",
    "report_id": "R005",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: Shaded area represents 90% confidence. Figure 3. FMs spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs FRONTIER MARKETS vs LOW INCOME COUNTRIES FM REGIME (SOLID BLUE) - LIC REGIME (D"
  },
  {
    "figure_id": "F057",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "FRONTIER MARKETS vs LOW INCOME COUNTRIES FM REGIME (SOLID BLUE) - LIC REGIME (DASHED RED) Note: Shaded area represents 90% confidence. FRONTIER MARKETS vs EMERGING MARKETS FM REGIME (SOLID BLUE) - EM REGIME (DASHED RED) Figure 4. FMs Spreads response to a U.S."
  },
  {
    "figure_id": "F058",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. FMs Spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals FLOATING vs NON-FLOATING EXCHANGE RATE REGIME FLOATING EXR REGIME (SOLID BLUE) - NON-FLOATING EXR REGIME (DASHED RED)"
  },
  {
    "figure_id": "F059",
    "report_id": "R005",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Finally, greater exports diversification could cushion against trade fluctuations arising from changes in U.S. monetary policy, as shown by Figure 5. Results show that spreads also tend to react less for oil exporters compared to oil importers, except in the i"
  },
  {
    "figure_id": "F060",
    "report_id": "R005",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "More Diversified countries (SOLID BLUE) - Less diversified countries (DASHED RED) Note: Shaded area represents 90% confidence. OIL EXPORTERS vs OIL IMPORTERS OIL EXPORTERS (SOLID BLUE) - OIL IMPORTERS (DASHED RED) Figure 6 and Figure 7 show the differential re"
  },
  {
    "figure_id": "F061",
    "report_id": "R005",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6 and Figure 7 show the differential response of EMs spreads to U.S. monetary policy stance changes depending on macroeconomic fundamentals, and the exports structure, respectively. While they also appear to matter for the response of EMs spreads to U.S"
  },
  {
    "figure_id": "F062",
    "report_id": "R005",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6. EMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals FLOATING vs NON-FLOATING EXCHANGE RATE REGIME LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO HIGH OFFICIAL RESERVES "
  },
  {
    "figure_id": "F063",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "FLOATING vs NON-FLOATING EXCHANGE RATE REGIME LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO HIGH OFFICIAL RESERVES vs LOW OFFICIAL RESERVES HIGH FISCAL BALANCE vs. LOW FISCAL BALANCE Note: Shaded area represents 90% confidence. Figure 7. EMs spreads response"
  },
  {
    "figure_id": "F064",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "HIGH OFFICIAL RESERVES vs LOW OFFICIAL RESERVES HIGH FISCAL BALANCE vs. LOW FISCAL BALANCE Note: Shaded area represents 90% confidence. Figure 7. EMs spreads response to a U.S. monetary policy stance changes: The role of external position structure THE ROLE OF"
  },
  {
    "figure_id": "F065",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Note: Shaded area represents 90% confidence. Figure 7. EMs spreads response to a U.S. monetary policy stance changes: The role of external position structure THE ROLE OF DIVERSIFICATION (COUNTRIES' EXPORTS) Note: Shaded area represents 90% confidence. OIL EXPO"
  },
  {
    "figure_id": "F066",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7. EMs spreads response to a U.S. monetary policy stance changes: The role of external position structure THE ROLE OF DIVERSIFICATION (COUNTRIES' EXPORTS) Note: Shaded area represents 90% confidence. OIL EXPORTERS vs OIL IMPORTERS ## Robustness Three ro"
  },
  {
    "figure_id": "F067",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Dynamics Surrounding Transition to FM Status (in years) INVESTMENT GOVERNMENT SPENDING (% GDP) ## SHARE OF PUBLIC INVESTMENT IN CAPITAL FORMATION"
  },
  {
    "figure_id": "F068",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "INVESTMENT GOVERNMENT SPENDING (% GDP) ## SHARE OF PUBLIC INVESTMENT IN CAPITAL FORMATION Cross-Group Comparison"
  },
  {
    "figure_id": "F069",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## SHARE OF PUBLIC INVESTMENT IN CAPITAL FORMATION Cross-Group Comparison Dynamics Surrounding Transition to FM Status (in years)"
  },
  {
    "figure_id": "F070",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Cross-Group Comparison Dynamics Surrounding Transition to FM Status (in years) WGI – GOVERNMENT EFFECTIVENESS"
  },
  {
    "figure_id": "F071",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Cross-Group Comparison Dynamics Surrounding Transition to FM Status (in years) WGI – GOVERNMENT EFFECTIVENESS WGI – REGULATORY QUALITY"
  },
  {
    "figure_id": "F072",
    "report_id": "R005",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "WGI – VOICE AND ACCOUNTABILITY CPIA GOVERNANCE INDEX ## Annex II. Robustness Checks"
  },
  {
    "figure_id": "F073",
    "report_id": "R005",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "WGI – VOICE AND ACCOUNTABILITY CPIA GOVERNANCE INDEX ## Annex II. Robustness Checks"
  },
  {
    "figure_id": "F074",
    "report_id": "R005",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "CPIA GOVERNANCE INDEX ## Annex II. Robustness Checks"
  },
  {
    "figure_id": "F075",
    "report_id": "R005",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Annex II. Robustness Checks"
  },
  {
    "figure_id": "F076",
    "report_id": "R005",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12. FMs Spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs (Taking the first alternative FM identification) FRONTIER MARKETS vs LOW INCOME COUNTRIES Note: Shaded area represents 90% "
  },
  {
    "figure_id": "F077",
    "report_id": "R005",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12. FMs Spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs (Taking the first alternative FM identification) FRONTIER MARKETS vs LOW INCOME COUNTRIES Note: Shaded area represents 90% "
  },
  {
    "figure_id": "F078",
    "report_id": "R005",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Note: Shaded area represents 90% confidence. FRONTIER MARKETS vs EMERGING MARKETS Figure 13. Spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs (Taking the second alternative for FM identif"
  },
  {
    "figure_id": "F079",
    "report_id": "R005",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13. Spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs (Taking the second alternative for FM identification) FRONTIER MARKETS vs LOW INCOME COUNTRIES Note: Shaded area represents 90%"
  },
  {
    "figure_id": "F080",
    "report_id": "R005",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "FRONTIER MARKETS vs EMERGING MARKETS Figure 14. Spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs (taking alternative spreads measure) FRONTIER MARKETS vs LOW INCOME COUNTRIES Note: Shaded"
  },
  {
    "figure_id": "F081",
    "report_id": "R005",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14. Spreads response to a U.S. monetary policy stance changes: A comparative analysis of regime switching with NFLICs and EMs (taking alternative spreads measure) FRONTIER MARKETS vs LOW INCOME COUNTRIES Note: Shaded area represents 90% confidence. FRON"
  },
  {
    "figure_id": "F082",
    "report_id": "R005",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "FRONTIER MARKETS vs EMERGING MARKETS Figure 15. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (Taking the first alternative FM identification) FLOATING vs NON-FLOATING EXCHA"
  },
  {
    "figure_id": "F083",
    "report_id": "R005",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (Taking the first alternative FM identification) FLOATING vs NON-FLOATING EXCHANGE RATE REGIME HIGH OFFICIAL RESERVE"
  },
  {
    "figure_id": "F084",
    "report_id": "R005",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "HIGH OFFICIAL RESERVES vs LOW OFFICIAL RESERVES LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO LOV Note: Shaded area represents 90% confidence. HIGH FISCAL BALANCE vs. LOW FISCAL BALANCE ## Figure 16. FMs spreads response to a U.S. monetary policy stance chan"
  },
  {
    "figure_id": "F085",
    "report_id": "R005",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO LOV Note: Shaded area represents 90% confidence. HIGH FISCAL BALANCE vs. LOW FISCAL BALANCE ## Figure 16. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and "
  },
  {
    "figure_id": "F086",
    "report_id": "R005",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "HIGH FISCAL BALANCE vs. LOW FISCAL BALANCE ## Figure 16. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (Taking the second alternative FM identification) FLOATING vs NON-FLOA"
  },
  {
    "figure_id": "F087",
    "report_id": "R005",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "## Figure 16. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (Taking the second alternative FM identification) FLOATING vs NON-FLOATING EXCHANGE RATE REGIME HIGH OFFICIAL RES"
  },
  {
    "figure_id": "F088",
    "report_id": "R005",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "HIGH OFFICIAL RESERVES vs LOW OFFICIAL RESERVES LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO LOI Note: Shaded area represents 90% confidence. Figure 17. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers an"
  },
  {
    "figure_id": "F089",
    "report_id": "R005",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO LOI Note: Shaded area represents 90% confidence. Figure 17. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (taking alternative"
  },
  {
    "figure_id": "F090",
    "report_id": "R005",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Note: Shaded area represents 90% confidence. Figure 17. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (taking alternative spreads measure) FLOATING vs NON-FLOATING EXCHANGE "
  },
  {
    "figure_id": "F091",
    "report_id": "R005",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17. FMs spreads response to a U.S. monetary policy stance changes: The role of domestic financial buffers and macroeconomic fundamentals (taking alternative spreads measure) FLOATING vs NON-FLOATING EXCHANGE RATE REGIME HIGH OFFICIAL RESERVES vs LOW OFF"
  },
  {
    "figure_id": "F092",
    "report_id": "R005",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "HIGH OFFICIAL RESERVES vs LOW OFFICIAL RESERVES LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO LOW Note: Shaded area represents 90% confidence. Figure 18. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure ("
  },
  {
    "figure_id": "F093",
    "report_id": "R005",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "LOW PUBLIC DEBT RATIO vs HIGH PUBLIC DEBT RATIO LOW Note: Shaded area represents 90% confidence. Figure 18. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking the first alternative FM identification) "
  },
  {
    "figure_id": "F094",
    "report_id": "R005",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Note: Shaded area represents 90% confidence. Figure 18. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking the first alternative FM identification) THE ROLE OF DIVERSIFICATION (COUNTRIES' EXPORTS) Not"
  },
  {
    "figure_id": "F095",
    "report_id": "R005",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking the first alternative FM identification) THE ROLE OF DIVERSIFICATION (COUNTRIES' EXPORTS) Note: Shaded area represents 90% confidence. OIL"
  },
  {
    "figure_id": "F096",
    "report_id": "R005",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "OIL EXPORTERS vs OIL IMPORTERS Figure 19. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking the second alternative FM identification) OIL EXPORTERS vs OIL IMPORTERS THE ROLE OF DIVERSIFICATION (COUNT"
  },
  {
    "figure_id": "F097",
    "report_id": "R005",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking the second alternative FM identification) OIL EXPORTERS vs OIL IMPORTERS THE ROLE OF DIVERSIFICATION (COUNTRIES' EXPORTS) Note: Shaded are"
  },
  {
    "figure_id": "F098",
    "report_id": "R005",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Note: Shaded area represents 90% confidence. OIL EXPORTERS vs OIL IMPORTERS Figure 20. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking alternative spreads measure) THE ROLE OF DIVERSIFICATION (COUN"
  },
  {
    "figure_id": "F099",
    "report_id": "R005",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20. FMs spreads response to a U.S. monetary policy stance changes: The role of external position structure (taking alternative spreads measure) THE ROLE OF DIVERSIFICATION (COUNTRIES' EXPORTS) Note: Shaded area represents 90% confidence. ##"
  },
  {
    "figure_id": "F100",
    "report_id": "R005",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：前沿市场真正的门槛不是增长，是制度｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F101",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## A. Introduction Figure 1. External Sovereign Credit Spreads in MENA (Basis point) ...and has generally tightened underpinned by ongoing reforms and the favorable economic outlook. Sources: Bloomberg and IMF staff calculations. Reform momentum could be an im"
  },
  {
    "figure_id": "F102",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. External Sovereign Credit Spreads in MENA (Basis point) ...and has generally tightened underpinned by ongoing reforms and the favorable economic outlook. Sources: Bloomberg and IMF staff calculations. Reform momentum could be an important form of rea"
  },
  {
    "figure_id": "F103",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: Bloomberg and IMF staff calculations. Reform momentum could be an important form of reassurance to markets about the prospects for economic stability, growth, and price stability. Global economic and policy uncertainty has risen to unprecedented level"
  },
  {
    "figure_id": "F104",
    "report_id": "R006",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "other (that is, the ranges between the green dots overlap). While tentative, investors seem to pay more attention to Qatar's balance of reform, potentially as Qatar has currently more room to make progress in this area. Qatar has made progress in overall refor"
  },
  {
    "figure_id": "F105",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Economic diversification (Figure 4, panel 4) The extent of economic diversification affects how investors assess the susceptibility of sovereign credits to oil price movement. Earlier regression results highlighted that sovereign credits of oil exporters ar"
  },
  {
    "figure_id": "F106",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "...and continued economic diversification. Qatar's economic resilience to shocks is underpinned including by low public debt to GDP... ...and stability and certainty of economic prospects domestically. Public sector debt and economic certainty (Figure 4, panel"
  },
  {
    "figure_id": "F107",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "...and continued economic diversification. Qatar's economic resilience to shocks is underpinned including by low public debt to GDP... ...and stability and certainty of economic prospects domestically. Public sector debt and economic certainty (Figure 4, panel"
  },
  {
    "figure_id": "F108",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Qatar's economic resilience to shocks is underpinned including by low public debt to GDP... ...and stability and certainty of economic prospects domestically. Public sector debt and economic certainty (Figure 4, panels 5–6) Tentative evidence suggests that ref"
  },
  {
    "figure_id": "F109",
    "report_id": "R006",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：卡塔尔主权利差收窄，改革“广度”比“深度”更值钱｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F110",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## I. Policy Frameworks in the Middle East and Central Asia ## A. Monetary Frameworks The “impossible trinity,” or the Mundell–Fleming Trilemma, highlights the inherent constraints on a country’s monetary policy objectives (Obstfeld, Shambaugh, and Taylor 2005"
  },
  {
    "figure_id": "F111",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 displays indexes that capture the three dimensions of the impossible trinity (Aizenman, Chin, and Ito 2008). Monetary policy autonomy is measured by the correlation between a home country's money market interest rate and that of a base country. Exchan"
  },
  {
    "figure_id": "F112",
    "report_id": "R007",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Monetary policy frameworks in the MENAP region reflect a clear preference for exchange rate stability (see Annex I, Figure A-1). In the Gulf Cooperation Council (GCC) countries and other MENA oil exporters, this is maintained primarily through currency pegs, w"
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## B. Fiscal Frameworks Strong fiscal frameworks can help anchor private sector expectations of future fiscal policy by lending credibility to official (budget) projections and commitments. Adopting credible medium-term fiscal frameworks and fiscal rules can h"
  },
  {
    "figure_id": "F114",
    "report_id": "R007",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## C. Fiscal Rules and Sovereign Spreads To highlight the importance of fiscal rules, this section explores the role of strong fiscal rules and other macroeconomic and institutional factors in explaining the variation in sovereign spreads across countries, usi"
  },
  {
    "figure_id": "F115",
    "report_id": "R007",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "where $y_{i,t}$ is the dependent variable of interest (real output, current account balance, primary balance, or sovereign spreads) for country i in year t; PolicyFramework is a dummy variable indicating either the exchange rate regime (fixed vs. floating), or"
  },
  {
    "figure_id": "F116",
    "report_id": "R007",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "This analysis indicates that exchange rate regimes have played a significant role in how economies adjust to global uncertainty shocks. Economies with floating exchange rates have tended to experience smaller and less persistent output declines after an advers"
  },
  {
    "figure_id": "F117",
    "report_id": "R007",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: IMF, World Economic Outlook database; IMF, The Annual Report on Exchange Arrangements and Exchange Restrictions database; Ahir, Bloom, and Furceri (2022); World Uncertainty Index (WUI) database; Federal Reserve Bank of St. Louis, Federal Reserve Econo"
  },
  {
    "figure_id": "F118",
    "report_id": "R007",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Note: Strong (weak) financial market development and high (low) export diversification are based on having a score above (below) the global median for each indicator, respectively. Vertical lines represent the 90 percent confidence interval. \\* denotes a stati"
  },
  {
    "figure_id": "F119",
    "report_id": "R007",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "The results of this analysis also show that economies with stronger fiscal frameworks—defined as those in the top one-third of the IMF's Fiscal Rules Strength Index distribution—experience smaller output losses one year after an adverse global shock compared t"
  },
  {
    "figure_id": "F120",
    "report_id": "R007",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Note: 1/ GCC treated like AEs. 2/ Lower coefficient for the GCC (3bps per one percent of GDP) than for non-GCC (5 bps). After the adverse global shock, global output declines by about 1.4 percent relative to baseline after two years, with inflation falling by "
  },
  {
    "figure_id": "F121",
    "report_id": "R007",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "The external demand shock compounds these challenges. Slower growth in China reduces export demand for Central Asia, while weaker activity in the U.S. and Europe hits MENA exporters. Overall, the combination of subdued investment, constrained policy space, and"
  },
  {
    "figure_id": "F122",
    "report_id": "R007",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Overall, while the combined scenario delivers substantial macroeconomic benefits for most MCD subregions, its effectiveness varies depending on structural characteristics. For GCC countries, where fiscal buffers are already strong and exchange rate flexibility"
  },
  {
    "figure_id": "F123",
    "report_id": "R007",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：中东和中亚的真正考验不是冲击本身，而是政策框架能否扛住下一轮全球波动｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F124",
    "report_id": "R008",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Historical smoothed variables: risk vs. liquidity interaction (2004–2024). Crucially, the decomposition resolves the banking stability question. The oil-liquidity nexus explains 53.02% of the total variance in aggregate"
  },
  {
    "figure_id": "F125",
    "report_id": "R008",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Historical smoothed variables: risk vs. liquidity interaction (2004–2024). Crucially, the decomposition resolves the banking stability question. The oil-liquidity nexus explains 53.02% of the total variance in aggregate"
  },
  {
    "figure_id": "F126",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impulse Responses to a 1 std (about 10%) Oil Price Crash under the Conservative baseline. Variables denote percentage deviations from steady state."
  },
  {
    "figure_id": "F127",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impulse Responses to a 1 std (about 10%) Oil Price Crash under the Conservative baseline. Variables denote percentage deviations from steady state. The simulated oil crash (Figure 2) illustrates the macroeconomic dynamic"
  },
  {
    "figure_id": "F128",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impulse Responses to a 1 std (about 10%) Oil Price Crash under the Conservative baseline. Variables denote percentage deviations from steady state. The simulated oil crash (Figure 2) illustrates the macroeconomic dynamic"
  },
  {
    "figure_id": "F129",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impulse Responses to a 1 std (about 10%) Oil Price Crash under the Conservative baseline. Variables denote percentage deviations from steady state. The simulated oil crash (Figure 2) illustrates the macroeconomic dynamic"
  },
  {
    "figure_id": "F130",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impulse Responses to a 1 std (about 10%) Oil Price Crash under the Conservative baseline. Variables denote percentage deviations from steady state. The simulated oil crash (Figure 2) illustrates the macroeconomic dynamic"
  },
  {
    "figure_id": "F131",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The simulated oil crash (Figure 2) illustrates the macroeconomic dynamics of the Omani business cycle as captured by the model's structural transmission channels. As shown in Figure 3, the rationing index $(\\Psi_{t})$ drops precipitously during a liquidity squ"
  },
  {
    "figure_id": "F132",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state."
  },
  {
    "figure_id": "F133",
    "report_id": "R008",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state."
  },
  {
    "figure_id": "F134",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state."
  },
  {
    "figure_id": "F135",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state. Cumulative Welfare (Consumption) (%)"
  },
  {
    "figure_id": "F136",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state. Cumulative Welfare (Consumption) (%) 15 Credit Supply Gap (Flow $\\Delta$ $\\Psi$ , %)"
  },
  {
    "figure_id": "F137",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state. Cumulative Welfare (Consumption) (%) 15 Credit Supply Gap (Flow $\\Delta$ $\\Psi$ , %) Figure 4:"
  },
  {
    "figure_id": "F138",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse Responses to an Exogenous Liquidity Squeeze Shock. Variables denote percentage deviations from steady state. Cumulative Welfare (Consumption) (%) 15 Credit Supply Gap (Flow $\\Delta$ $\\Psi$ , %) Figure 4:"
  },
  {
    "figure_id": "F139",
    "report_id": "R008",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Cumulative Regime Trade-off (Oil Crash): The shaded areas plot the policy differential (Accommodative minus Conservative) under the current economy. The dashed line plots the structural differential (Vision 2040 minus Cu"
  },
  {
    "figure_id": "F140",
    "report_id": "R008",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Sensitivity analysis: impulse responses to an oil price shock under alternative parameterizations. Blue solid = baseline; red dashed = demand-side dominant; green dash-dot = aggressive SWF stabilization; blue band = $\\ka"
  },
  {
    "figure_id": "F141",
    "report_id": "R008",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Channel decomposition: response to the same oil price shock with each channel shut off individually. Blue solid = both channels active; red dashed = liquidity channel off; green dash-dot = solvency channel off. We identi"
  },
  {
    "figure_id": "F142",
    "report_id": "R008",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Channel decomposition: response to the same oil price shock with each channel shut off individually. Blue solid = both channels active; red dashed = liquidity channel off; green dash-dot = solvency channel off. We identi"
  },
  {
    "figure_id": "F143",
    "report_id": "R008",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：石油经济体真正该担心的不是银行破产，而是存款被抽干｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F144",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Recognizing that the intensification of climate and disaster shocks has drastic macroeconomic consequences, the economic literature on the matter has expanded considerably in the recent years (e.g. Benson and Clay, 2004; Hochrainer, 2009; Dell, Jones, and Olke"
  },
  {
    "figure_id": "F145",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Nonetheless, the impact of disaster shocks on the cost of government domestic borrowing was overlooked. Yet, domestic public debt has risen in many developing countries as domestic financial markets deepen, and international liquidity dried up during the globa"
  },
  {
    "figure_id": "F146",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Gathering comparable data across countries requires some adjustments. The bulk of the securities are issued on the primary market while others are traded on the secondary market. There are also securities issued at discount, and the periodicity of the interest"
  },
  {
    "figure_id": "F147",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3 presents the evolution of the median interest rate on government domestic securities from 2000 to 2020 by maturity. The drop in the cost of government domestic borrowing in two decades was staggering, more than a 50 percent decline for short to medium"
  },
  {
    "figure_id": "F148",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "This contrasting trend had implications for the shape of the median yield curve (Figure 4). The yield curve inverted at the onset of the global financial crisis (GFC), which typically is believed to be a strong predictor of recessions (Stock and Watson, 1989; "
  },
  {
    "figure_id": "F149",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Nominal Interest Rate on Government Securities, 2000–20 (sample median, percent) Figure 4. Yield Curve in Selected Years (sample median, percent) Looking at the median real interest rate, the data suggest that the real cost of government borrowing ex"
  },
  {
    "figure_id": "F150",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Yield Curve in Selected Years (sample median, percent) Looking at the median real interest rate, the data suggest that the real cost of government borrowing exhibited significant volatility over the period and across maturities, with the cost of shor"
  },
  {
    "figure_id": "F151",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Yield Curve in Selected Years (sample median, percent) Looking at the median real interest rate, the data suggest that the real cost of government borrowing exhibited significant volatility over the period and across maturities, with the cost of shor"
  },
  {
    "figure_id": "F152",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Looking at the median real interest rate, the data suggest that the real cost of government borrowing exhibited significant volatility over the period and across maturities, with the cost of short-term maturities having been the longest in the negative territo"
  },
  {
    "figure_id": "F153",
    "report_id": "R009",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Splitting the sample by income group reveals common but also contrasting trends (Figure 5). Predictably, nominal interest rates on government securities are typically higher for lower income countries. While we observe a downward trend in the nominal rate for "
  },
  {
    "figure_id": "F154",
    "report_id": "R009",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Nominal Interest Rate on Government Securities by Income Group, 2000-20 (sample median, percent) ## Natural disasters and climate indicators Turning to the disaster shock variables, the paper focuses on two sets of indicators commonly used in the lit"
  },
  {
    "figure_id": "F155",
    "report_id": "R009",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Bivariate correlation A graphical representation of the bivariate correlation between the average cost of government securities and disaster indicators shows a mixed picture (Figure 6). There is marginally no difference between the cost of government securi"
  },
  {
    "figure_id": "F156",
    "report_id": "R009",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "A graphical representation of the bivariate correlation between the average cost of government securities and disaster indicators shows a mixed picture (Figure 6). There is marginally no difference between the cost of government securities for countries that e"
  },
  {
    "figure_id": "F157",
    "report_id": "R009",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Local projection difference in difference As underscored in Section III.B, the local projection difference in difference allows us to account for a richer dynamic between climate shocks and the cost of government domestic financing, while addressing potenti"
  },
  {
    "figure_id": "F158",
    "report_id": "R009",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Specifically, Figure 7 shows the average treatment effect (ATE) of drought on the average interest rate on government domestic securities. It provides evidence of a causal positive impact of drought on the cost of government financing, with the marginal impact"
  },
  {
    "figure_id": "F159",
    "report_id": "R009",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Notes: The ATEs are estimated using quarterly data; never treated units used a control group; vertical dash lines denote the 90 percent confidence band in the full specification and the one without the control variables. Figure 8. Average Treatment Effect of D"
  },
  {
    "figure_id": "F160",
    "report_id": "R009",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8. Average Treatment Effect of Drought on the Interest Rate on Domestic Government Securities by Maturity (Up to 3-month maturity) (Up to 1 year maturity) (2-to-3-year maturity) (4-year maturity and beyond) Notes: The ATEs are estimated using quarterly "
  },
  {
    "figure_id": "F161",
    "report_id": "R009",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "(Up to 1 year maturity) (2-to-3-year maturity) (4-year maturity and beyond) Notes: The ATEs are estimated using quarterly data; never treated units used a control group; vertical dash lines denote the 90 percent confidence band in the full specification and th"
  },
  {
    "figure_id": "F162",
    "report_id": "R009",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "(4-year maturity and beyond) Notes: The ATEs are estimated using quarterly data; never treated units used a control group; vertical dash lines denote the 90 percent confidence band in the full specification and the one without the control variables. Figures 9 "
  },
  {
    "figure_id": "F163",
    "report_id": "R009",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Notes: The ATEs are estimated using quarterly data; never treated units used a control group; vertical dash lines denote the 90 percent confidence band in the full specification and the one without the control variables. Under the parallel trend assumption, th"
  },
  {
    "figure_id": "F164",
    "report_id": "R009",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "With regard to the climate vulnerability index, we created a dummy variable for the purpose of the local projection difference in difference, taking 1 when a country has a climate vulnerability index above the sample median, and 0 otherwise. Although the resul"
  },
  {
    "figure_id": "F165",
    "report_id": "R009",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10. Average Treatment Effect of Storm on the Interest Rate on Domestic Government Securities by Maturity (Up to 3-month maturity) (Up to 1 year maturity) (2-to-3-year maturity) (4-year maturity and beyond) Notes: The ATEs are estimated using quarterly d"
  },
  {
    "figure_id": "F166",
    "report_id": "R009",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "(Up to 1 year maturity) (2-to-3-year maturity) (4-year maturity and beyond) Notes: The ATEs are estimated using quarterly data; never treated units used a control group; vertical dash lines denote the 90 percent confidence band in the full specification and th"
  },
  {
    "figure_id": "F167",
    "report_id": "R009",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "(2-to-3-year maturity) (4-year maturity and beyond) Notes: The ATEs are estimated using quarterly data; never treated units used a control group; vertical dash lines denote the 90 percent confidence band in the full specification and the one without the contro"
  },
  {
    "figure_id": "F168",
    "report_id": "R009",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11. Average Treatment Effect of Climate Vulnerability on the Interest Rate on Domestic Government Securities, all maturities combined Notes: The ATEs are estimated using annual data; not yet treated units used a control group; vertical dash lines denote"
  },
  {
    "figure_id": "F169",
    "report_id": "R009",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12. Average Treatment Effect of Climate Vulnerability on the Interest Rate on Domestic Government Securities by Maturity (Up to 3-month maturity) (2-to-3-year maturity) (Up to 1 year maturity) (4-year maturity and beyond) Notes: The ATEs are estimated u"
  },
  {
    "figure_id": "F170",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Stylized facts Annex Figure 1 shows the number of instruments/observations in the database for each year. The number of instruments steadily increased over time, rising from around 1,000 instruments in 2020 to 6700 in 2020. This increase reflects not only c"
  },
  {
    "figure_id": "F171",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "database is broad as shown in Annex Figure 2, with Sub-Saharan Africa countries representing 37 percent of the sample (37 countries), followed by Europe and Central Asia (18 countries); and Latin America and Caribbean (17 countries). The share of the remaining"
  },
  {
    "figure_id": "F172",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Annex Figure 2. Country Coverage by Region, 1977–2021 ## Annex Figure 3. Country Coverage by Income Group, 1977–2021 Annex Figure 4 depicts the distribution of the maturity of domestic securities. Predictably, short-term instruments are more common, with secur"
  },
  {
    "figure_id": "F173",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Annex Figure 3. Country Coverage by Income Group, 1977–2021 Annex Figure 4 depicts the distribution of the maturity of domestic securities. Predictably, short-term instruments are more common, with securities featuring a maturity of less than 3 months accou"
  },
  {
    "figure_id": "F174",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Annex Figure 4. Distribution of Domestic Securities by Maturity Annex Figure 5 presents the distribution of nominal and real interest rates on government securities. The average nominal interest rate is 9 percent, and for the real interest rate (calculated as "
  },
  {
    "figure_id": "F175",
    "report_id": "R009",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Annex Figure 5 presents the distribution of nominal and real interest rates on government securities. The average nominal interest rate is 9 percent, and for the real interest rate (calculated as the difference between nominal interest rate and inflation), the"
  },
  {
    "figure_id": "F176",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Notes: The asterisk (\\*) indicates the 72 developing countries used in the econometric analysis. Sources: Authors Appendix Figure 1. Evolution of the Real Interest Rate on Government Securities, 2000–20 (sample median, percent)"
  },
  {
    "figure_id": "F177",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Notes: The asterisk (\\*) indicates the 72 developing countries used in the econometric analysis. Sources: Authors Appendix Figure 1. Evolution of the Real Interest Rate on Government Securities, 2000–20 (sample median, percent) Appendix Figure 2. Real Interest"
  },
  {
    "figure_id": "F178",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Sources: Authors Appendix Figure 1. Evolution of the Real Interest Rate on Government Securities, 2000–20 (sample median, percent) Appendix Figure 2. Real Interest Rate on Government Securities by Income Group (sample median, percent)"
  },
  {
    "figure_id": "F179",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 1. Evolution of the Real Interest Rate on Government Securities, 2000–20 (sample median, percent) Appendix Figure 2. Real Interest Rate on Government Securities by Income Group (sample median, percent)"
  },
  {
    "figure_id": "F180",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 2. Real Interest Rate on Government Securities by Income Group (sample median, percent)"
  },
  {
    "figure_id": "F181",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 2. Real Interest Rate on Government Securities by Income Group (sample median, percent) All maturities combined"
  },
  {
    "figure_id": "F182",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 2. Real Interest Rate on Government Securities by Income Group (sample median, percent) All maturities combined Up to 3-month maturity"
  },
  {
    "figure_id": "F183",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 2. Real Interest Rate on Government Securities by Income Group (sample median, percent) All maturities combined Up to 3-month maturity All maturities combined"
  },
  {
    "figure_id": "F184",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "All maturities combined Up to 3-month maturity All maturities combined Appendix Figure 3. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to Disaster Damage as a Share of GDP"
  },
  {
    "figure_id": "F185",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Up to 3-month maturity All maturities combined Appendix Figure 3. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to Disaster Damage as a Share of GDP Appendix Figure 4. Impulse Response Function (IRF) of the Interest"
  },
  {
    "figure_id": "F186",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "All maturities combined Appendix Figure 3. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to Disaster Damage as a Share of GDP Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Sec"
  },
  {
    "figure_id": "F187",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 3. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to Disaster Damage as a Share of GDP Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to "
  },
  {
    "figure_id": "F188",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 3. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to Disaster Damage as a Share of GDP Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to "
  },
  {
    "figure_id": "F189",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to the Share of Affected Population in Total Population"
  },
  {
    "figure_id": "F190",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to the Share of Affected Population in Total Population"
  },
  {
    "figure_id": "F191",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to the Share of Affected Population in Total Population"
  },
  {
    "figure_id": "F192",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Appendix Figure 4. Impulse Response Function (IRF) of the Interest Rate on Government Securities with respect to the Share of Affected Population in Total Population"
  },
  {
    "figure_id": "F193",
    "report_id": "R009",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF最新研究：自然灾害正在重塑发展中国家的国债定价｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F194",
    "report_id": "R010",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Model Inclusion in BMA on AIPI [hyper-g/n prior; random model prior]"
  },
  {
    "figure_id": "F195",
    "report_id": "R010",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Model Inclusion in BMA on AIPI [hyper-g/n prior; random model prior] To measure the economic complexity of each country, we consider ECIs for trade, technology, and research available on the Observatory of Economic Com"
  },
  {
    "figure_id": "F196",
    "report_id": "R010",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Global relationship between AIPI and ECI a) Unweighted analysis b) Population-weighted analysis Both charts highlight the top performers in AI preparedness, concentrated in the northeast quadrants. Consistent with pr"
  },
  {
    "figure_id": "F197",
    "report_id": "R010",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Global relationship between AIPI and ECI a) Unweighted analysis b) Population-weighted analysis Both charts highlight the top performers in AI preparedness, concentrated in the northeast quadrants. Consistent with pr"
  },
  {
    "figure_id": "F198",
    "report_id": "R010",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 5: AI preparedness and economic complexity in LICs and LMICs: Identifying local overperformers"
  },
  {
    "figure_id": "F199",
    "report_id": "R010",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: AI preparedness and economic complexity in LICs and LMICs: Identifying local overperformers 2024). In contrast, a few LMICs with relatively high observed AIP scores, such as Kenya, Kyrgyzstan, Lebanon, and the Philippi"
  },
  {
    "figure_id": "F200",
    "report_id": "R010",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Key pillars driving overperformance across income groups of overperformers In low-income and lower-middle-income overperformers, regulation and ethics emerge as the most significant driver of AI preparedness, accountin"
  },
  {
    "figure_id": "F201",
    "report_id": "R010",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Selected HICs (global) overperformers Singapore's AI readiness strategy strongly emphasizes all the AIPi pillars detailed above, and particularly regulation and ethics, as well as the development of robust digital infr"
  },
  {
    "figure_id": "F202",
    "report_id": "R010",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Selected UMICs overperformers Spiderweb charts illustrate that China and Malaysia excel in all AIPi pillars relative to the average of non-overperformers within their income group. Notably, China demonstrates exception"
  },
  {
    "figure_id": "F203",
    "report_id": "R010",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Selected LICs/LMICs overperformers India's AI readiness strategy places a significant emphasis on both human capital development and an ethical framework to support its vision of becoming a leader in AI innovation (Fig"
  },
  {
    "figure_id": "F204",
    "report_id": "R010",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：AI准备度差距的真正分界线，不是算力，而是经济复杂度｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F205",
    "report_id": "R011",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region"
  },
  {
    "figure_id": "F206",
    "report_id": "R011",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region"
  },
  {
    "figure_id": "F207",
    "report_id": "R011",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：数据透明是主权债投资者的隐藏回报来源｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F208",
    "report_id": "R012",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Total count of species ## Data and Method The data for this study have been provided by the Global Biodiversity Information Facility (GBIF), a global network, funded by various national governments, that offers open ac"
  },
  {
    "figure_id": "F209",
    "report_id": "R012",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Selected species occurrence regions ## Results Taken together, non-determined legal status territories, areas with fragile and conflict-affected situations status, joint marine regimes, and transboundary river basins c"
  },
  {
    "figure_id": "F210",
    "report_id": "R012",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Countries determined as Fragile and Conflict-affected Situations areas (FCS) in 2024 Figure 4: Log human population density in transboundary river basins Figure 5: Total count of critical species in geopolitically se"
  },
  {
    "figure_id": "F211",
    "report_id": "R012",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Countries determined as Fragile and Conflict-affected Situations areas (FCS) in 2024 Figure 4: Log human population density in transboundary river basins Figure 5: Total count of critical species in geopolitically se"
  },
  {
    "figure_id": "F212",
    "report_id": "R012",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Countries determined as Fragile and Conflict-affected Situations areas (FCS) in 2024 Figure 4: Log human population density in transboundary river basins Figure 5: Total count of critical species in geopolitically se"
  },
  {
    "figure_id": "F213",
    "report_id": "R012",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas"
  },
  {
    "figure_id": "F214",
    "report_id": "R012",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas Fragile Conflict States Marine Joint Regime Transboundary River Basins"
  },
  {
    "figure_id": "F215",
    "report_id": "R012",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas Fragile Conflict States Marine Joint Regime Transboundary River Basins Figure 8: Global taxon variations"
  },
  {
    "figure_id": "F216",
    "report_id": "R012",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas Fragile Conflict States Marine Joint Regime Transboundary River Basins Figure 8: Global taxon variations"
  },
  {
    "figure_id": "F217",
    "report_id": "R012",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Global taxon variations This lack of governance coverage is especially troubling for endemic species with small occurrence regions (9.4% without treaties; 29.9% without RBOs; 9.3% with neither) and high ETIs (9.6% with"
  },
  {
    "figure_id": "F218",
    "report_id": "R012",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Global taxon variations This lack of governance coverage is especially troubling for endemic species with small occurrence regions (9.4% without treaties; 29.9% without RBOs; 9.3% with neither) and high ETIs (9.6% with"
  },
  {
    "figure_id": "F219",
    "report_id": "R012",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：冲突地带才是生物多样性最被低估的“沉默金库”｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F220",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Distribution of ownership shares by BOS type (a) Public (b) Mixed (c) Participated Note: The figures show the distribution of ownership shares computed using data obtained from Orbis. Data from Orbis, 2019. Public"
  },
  {
    "figure_id": "F221",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Distribution of ownership shares by BOS type (a) Public (b) Mixed (c) Participated Note: The figures show the distribution of ownership shares computed using data obtained from Orbis. Data from Orbis, 2019. Public"
  },
  {
    "figure_id": "F222",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Distribution of ownership shares by BOS type (a) Public (b) Mixed (c) Participated Note: The figures show the distribution of ownership shares computed using data obtained from Orbis. Data from Orbis, 2019. Public"
  },
  {
    "figure_id": "F223",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups"
  },
  {
    "figure_id": "F224",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education"
  },
  {
    "figure_id": "F225",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education (b) Age (c) Tenure"
  },
  {
    "figure_id": "F226",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicat"
  },
  {
    "figure_id": "F227",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicat"
  },
  {
    "figure_id": "F228",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education"
  },
  {
    "figure_id": "F229",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education (b) Age (c) Tenure"
  },
  {
    "figure_id": "F230",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indica"
  },
  {
    "figure_id": "F231",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indica"
  },
  {
    "figure_id": "F232",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Effect of privatization on firms' average wages and employment (a) Average wage"
  },
  {
    "figure_id": "F233",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Effect of privatization on firms' average wages and employment (a) Average wage (b) Employment Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions"
  },
  {
    "figure_id": "F234",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Effect of privatization on firms' average wages and employment (a) Average wage (b) Employment Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions"
  },
  {
    "figure_id": "F235",
    "report_id": "R013",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Employment share of BOS. ## Entry and exit Figure 7: Entry and exit rates."
  },
  {
    "figure_id": "F236",
    "report_id": "R013",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Entry and exit rates. Following the observed decline in the entry rate of new firms, we also find a steady fall in the employment share of young firms. Figure 8 reveals that the fraction of employment in firms operatin"
  },
  {
    "figure_id": "F237",
    "report_id": "R013",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Job creation and destruction."
  },
  {
    "figure_id": "F238",
    "report_id": "R013",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Job creation and destruction. Figure 10: Job reallocation. A lower level of business dynamism is also associated with declining variation in firm-level growth rates. Although there is a declining trend in the standar"
  },
  {
    "figure_id": "F239",
    "report_id": "R013",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Standard deviation of firm employment growth."
  },
  {
    "figure_id": "F240",
    "report_id": "R013",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Standard deviation of firm employment growth. ## 5.2 BOS and business dynamism We test whether a high concentration of BOS is associated with different metrics of business dynamism using variation in the industry-level"
  },
  {
    "figure_id": "F241",
    "report_id": "R013",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：国企不是就业杀手，但它在悄悄改变市场规则｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F242",
    "report_id": "R014",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: A training question preceding the ACASI administered IPV module ## 3 Experiment 1: Do respondents understand ACASI?"
  },
  {
    "figure_id": "F243",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Design of the Measurement Experiment II Figure 3: Impact of the Measurement Experiment II on Face-to-Face IPV Reporting Notes: The figure shows results from an experiment where for half the respondents two questions"
  },
  {
    "figure_id": "F244",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Design of the Measurement Experiment II Figure 3: Impact of the Measurement Experiment II on Face-to-Face IPV Reporting Notes: The figure shows results from an experiment where for half the respondents two questions"
  },
  {
    "figure_id": "F245",
    "report_id": "R014",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：家暴数据被严重低估，一个简单的问卷顺序改变能提升57%的披露率｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F246",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Intervention timeline \\- renewals delivered in health centers (or during home visits by HPO, with very limited capacity) ## 4 Study Design ## Randomization ## Data and Outcomes"
  },
  {
    "figure_id": "F247",
    "report_id": "R015",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Evolution of Sayana Press injections (above) and overall number of contraceptives dispensed (below) Notes: The first figure plots the average number of Sayana Press injections while the second figure shows the average"
  },
  {
    "figure_id": "F248",
    "report_id": "R015",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：社区健康工作者推高避孕针用量70%，但总覆盖率未变｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F249",
    "report_id": "R016",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Fossil Fuel Subsidies by Country (latest year available) ## 2. Fossil Fuel Subsidies, Resource Rent and Carbon Emissions among Oil Exporters The magnitudes of global subsidies of fossil fuels are staggering. Black et a"
  },
  {
    "figure_id": "F250",
    "report_id": "R016",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2. Fossil Fuel Subsidies, Resource Rent and Carbon Emissions among Oil Exporters The magnitudes of global subsidies of fossil fuels are staggering. Black et al. (2023) in an IMF working paper estimate that the total global subsidies of fossil fuels amounted"
  },
  {
    "figure_id": "F251",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "However, the above report and other studies of fossil fuel subsidies, such as one by Kojum and Koplow (2017), focus on oil consuming/importing countries or fossil fuel consuming sectors of the economy. The oil and gas producing countries, on the other hand, fa"
  },
  {
    "figure_id": "F252",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Fossil Fuel Subsidies, Resource Rents and Carbon emission among Oil Exporters: Case 1 Note: The figure assumes producers are subsidized at the production level and thus for full output aimed at domestic and world markets. It also assumes domestic con"
  },
  {
    "figure_id": "F253",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Fossil Fuel Subsidies significantly contribute to CO2 Emissions in Oil Exporting MENA ## 5.3. Flaring matters in contributing to CO2 emissions only for the full sample of 41 countries Figure 5. Flaring by Country"
  },
  {
    "figure_id": "F254",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## 5.3. Flaring matters in contributing to CO2 emissions only for the full sample of 41 countries Figure 5. Flaring by Country ## Figure 6. Trends in flaring ## 5.4 World oil prices affect the level of subsidy"
  },
  {
    "figure_id": "F255",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Flaring by Country ## Figure 6. Trends in flaring ## 5.4 World oil prices affect the level of subsidy ## 6. Country-Level Projections: Removing Subsidies or Taxing Carbon?"
  },
  {
    "figure_id": "F256",
    "report_id": "R016",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：中东产油国的燃料补贴，正在成为全球减排的最大盲区｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F257",
    "report_id": "R017",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The quantitative data confirms that while women are more likely than men to make the decisions about the water"
  },
  {
    "figure_id": "F258",
    "report_id": "R017",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：不参与决策，可能恰恰是权力的体现｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F259",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Distribution of cluster sizes in six partial population experiments (a) This paper; $n = 68,808$ ; $G = 3,982$ ; $n / G = 17.3$ ; $sd(n_g) = 8.25$ . (b) Crépon et al. (2013); $n = 21,431$ ; $G = 235$ ; $n / G = 91.2$"
  },
  {
    "figure_id": "F260",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Distribution of cluster sizes in six partial population experiments (a) This paper; $n = 68,808$ ; $G = 3,982$ ; $n / G = 17.3$ ; $sd(n_g) = 8.25$ . (b) Crépon et al. (2013); $n = 21,431$ ; $G = 235$ ; $n / G = 91.2$"
  },
  {
    "figure_id": "F261",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Distribution of cluster sizes in six partial population experiments (a) This paper; $n = 68,808$ ; $G = 3,982$ ; $n / G = 17.3$ ; $sd(n_g) = 8.25$ . (b) Crépon et al. (2013); $n = 21,431$ ; $G = 235$ ; $n / G = 91.2$"
  },
  {
    "figure_id": "F262",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Power functions - numerical illustration"
  },
  {
    "figure_id": "F263",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Power functions - numerical illustration Notes: This figure illustrates how ignoring heterogeneity can result in severely underpowered experiments. We consider the simple setting of a cluster RCT with a few “large” clu"
  },
  {
    "figure_id": "F264",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Direct and spillover effects on property tax payments in high-saturation blocks Direct Effects Treated vs. Pure Control"
  },
  {
    "figure_id": "F265",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Direct and spillover effects on property tax payments in high-saturation blocks Direct Effects Treated vs. Pure Control Spillover Effects Untreated vs. Pure Control Above Median Compliance"
  },
  {
    "figure_id": "F266",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure A.5: Distribution of payment date for treated, untreated, and pure control (October 2020 billing period) (a) Treated vs. Pure Control (b) Untreated vs. Pure Control Notes: These figures show the fraction of individuals paying the October 2020 bill befor"
  },
  {
    "figure_id": "F267",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure A.5: Distribution of payment date for treated, untreated, and pure control (October 2020 billing period) (a) Treated vs. Pure Control (b) Untreated vs. Pure Control Notes: These figures show the fraction of individuals paying the October 2020 bill befor"
  },
  {
    "figure_id": "F268",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Finally, for completeness, we also study the relationship between payment rates and exposure to adjacent treated blocks in blocks where 80% of the units were treated, again for the 100-meter buffer. The results of this exercise are reported in Figure B.14. The"
  },
  {
    "figure_id": "F269",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "(a) 2018 vs 2019 (b) 2019 vs 2020 Notes: These figures show compliance in the first 9 billing periods of the year. For each block, we compute the share of total bills paid out of 9. Panel (a) compares 2018 and 2019, and panel (b) compares 2019 and 2020. We res"
  },
  {
    "figure_id": "F270",
    "report_id": "R018",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：你低估了集群实验中的“大小不均”代价｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F271",
    "report_id": "R019",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "June 30, 2022. $^{15}$ As such, approximately three in each four Ukrainian refugee students in secondary school age were not enrolled in Italian schools in academic year 2021-22. Analysis of MoE data covering academic years 2022-23 through 2023-24 highlights a"
  },
  {
    "figure_id": "F272",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "On average, Ukrainian students miss 46 school days per year in 2022-23, 18 days more than Italians. In upper secondary schools, Ukrainian refugee students exhibit twice the absenteeism of their Italian peers. Italian students miss half as many days (23 days) o"
  },
  {
    "figure_id": "F273",
    "report_id": "R019",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Lower test score performance The evidence suggests that Ukrainian refugees in Italy face important learning gaps across all subjects. Figure 4 reports the INVALIDSI test scores by topic and category of students. $^{23}$ The educational disparity is particul"
  },
  {
    "figure_id": "F274",
    "report_id": "R019",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Lower test score performance The evidence suggests that Ukrainian refugees in Italy face important learning gaps across all subjects. Figure 4 reports the INVALIDSI test scores by topic and category of students. $^{23}$ The educational disparity is particul"
  },
  {
    "figure_id": "F275",
    "report_id": "R019",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The evidence suggests that Ukrainian refugees in Italy face important learning gaps across all subjects. Figure 4 reports the INVALIDSI test scores by topic and category of students. $^{23}$ The educational disparity is particularly pronounced between Ukrainia"
  },
  {
    "figure_id": "F276",
    "report_id": "R019",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "39 points less, and recent migrants score 24 points less than other students, highlighting language as a likely barrier in the learning process."
  },
  {
    "figure_id": "F277",
    "report_id": "R019",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Track enrollment and recommendation Ukrainian students are less likely than Italians to enroll in high track education. Figure 5 shows that the rate of Ukrainian refugees (74%) enrolled in the High Track is much lower than that of Italians (84%) but higher "
  },
  {
    "figure_id": "F278",
    "report_id": "R019",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Uncertainty about the future may impact refugees' connectedness to Italy, including to its education system. Figure 6 presents the statistics on aspirations and connectedness to Ukraine and Italy for caregivers and children. Displaced Ukrainians are not only u"
  },
  {
    "figure_id": "F279",
    "report_id": "R019",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：乌克兰难民学生融入意大利学校，比想象中更难｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F280",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: SMS Delivery Rates by Treatment Group ## Appendix ## SMS on long-term benefits of the program Another type of SMS, emphasizing the long-term benefits of the program, was sent to either youth only or youth and their con"
  },
  {
    "figure_id": "F281",
    "report_id": "R020",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：免费短信反而劝退，就业项目招生的“信任悖论”｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F282",
    "report_id": "R021",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\*\\*\\* significant at the 1% level, \\*\\* significant at the 5% level, \\* significant at the 10% level. Figure 1 Upward mobility, by country and parent (1980s birth cohort) Note: This figure plots the upward mobility gap by parent for the 1980s birth cohort. Th"
  },
  {
    "figure_id": "F283",
    "report_id": "R021",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\*\\*\\* significant at the 1% level, \\*\\* significant at the 5% level, \\* significant at the 10% level. Figure 1 Upward mobility, by country and parent (1980s birth cohort) Note: This figure plots the upward mobility gap by parent for the 1980s birth cohort. Th"
  },
  {
    "figure_id": "F284",
    "report_id": "R021",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: This figure plots the upward mobility gap by parent for the 1980s birth cohort. The vertical axis plots the value calculated with respect to fathers, while the horizontal axis plots the value calculated with respect to mothers. The 45 degree line is plot"
  },
  {
    "figure_id": "F285",
    "report_id": "R021",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2 Correlation between share of upward movers and upward education gap, by country (1980s birth cohort) Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Figure 3"
  },
  {
    "figure_id": "F286",
    "report_id": "R021",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3 Average upward mobility (based on mothers' education), by birth cohort Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indicate regional medians "
  },
  {
    "figure_id": "F287",
    "report_id": "R021",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indicate regional medians Grey lines plot values for individual countries. Figure 5 Average upward educati"
  },
  {
    "figure_id": "F288",
    "report_id": "R021",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indicate regional medians Grey lines plot values for individual countries. Figure 6 Average upward mobilit"
  },
  {
    "figure_id": "F289",
    "report_id": "R021",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6 Average upward mobility into higher education (based on mothers' education), by birth cohort Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indi"
  },
  {
    "figure_id": "F290",
    "report_id": "R021",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：社会流动性未必直接拉动经济增长，真正起作用的是“谁在向上流动”｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F291",
    "report_id": "R022",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Adoption timeline of fiscal rules The academic literature posits the origin of fiscal rules on the need to foster fiscal discipline and ensure debt remains on a sustainable path (Wyplosz 2013; Kopits and Symansky 1998)"
  },
  {
    "figure_id": "F292",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Dynamic effects of fiscal rule adoption Notes: The figure presents the impulse response function of the primary balance to the adoption of a fiscal rule, with the rule(s) adopted at year h = 0. The blue line shows the"
  },
  {
    "figure_id": "F293",
    "report_id": "R022",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse responses: advanced economies vs. EMDEs (b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions"
  },
  {
    "figure_id": "F294",
    "report_id": "R022",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse responses: advanced economies vs. EMDEs (b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of obser"
  },
  {
    "figure_id": "F295",
    "report_id": "R022",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Impulse responses: advanced economies vs. EMDEs (b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of obser"
  },
  {
    "figure_id": "F296",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations included in each regression ranges between 1,807 and 1,817. Figure 3, panel (b), shows a"
  },
  {
    "figure_id": "F297",
    "report_id": "R022",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Impulse responses: commodity importers vs. commodity exporters. (a) Commodity importers (b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions"
  },
  {
    "figure_id": "F298",
    "report_id": "R022",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Impulse responses: commodity importers vs. commodity exporters. (a) Commodity importers (b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions Note"
  },
  {
    "figure_id": "F299",
    "report_id": "R022",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Impulse responses: commodity importers vs. commodity exporters. (a) Commodity importers (b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions Note"
  },
  {
    "figure_id": "F300",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations included in each regression ranges between 1,8"
  },
  {
    "figure_id": "F301",
    "report_id": "R022",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Impulse responses conditional on the state of the economy (a) Strong state of the economy"
  },
  {
    "figure_id": "F302",
    "report_id": "R022",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Impulse responses conditional on the state of the economy (a) Strong state of the economy (b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong insti"
  },
  {
    "figure_id": "F303",
    "report_id": "R022",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Impulse responses conditional on the state of the economy (a) Strong state of the economy (b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong insti"
  },
  {
    "figure_id": "F304",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(a) Strong state of the economy (b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations in"
  },
  {
    "figure_id": "F305",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations in each regression ranges from 1,7"
  },
  {
    "figure_id": "F306",
    "report_id": "R022",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Impulse responses conditional on fiscal regime"
  },
  {
    "figure_id": "F307",
    "report_id": "R022",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Impulse responses conditional on fiscal regime Notes: See notes Figure 2. The analysis is based on 107 countries; the number of observations in each regression ranges from 1,794 to 1,803. ## 5.3. Political landscape"
  },
  {
    "figure_id": "F308",
    "report_id": "R022",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Impulse responses conditional on fiscal regime Notes: See notes Figure 2. The analysis is based on 107 countries; the number of observations in each regression ranges from 1,794 to 1,803. ## 5.3. Political landscape"
  },
  {
    "figure_id": "F309",
    "report_id": "R022",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power"
  },
  {
    "figure_id": "F310",
    "report_id": "R022",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power (b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—St"
  },
  {
    "figure_id": "F311",
    "report_id": "R022",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power (b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—St"
  },
  {
    "figure_id": "F312",
    "report_id": "R022",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power (b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—St"
  },
  {
    "figure_id": "F313",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—Strong institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations in each regression ran"
  },
  {
    "figure_id": "F314",
    "report_id": "R022",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Robustness analyses (a) Split-sample jackknife estimator (b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance"
  },
  {
    "figure_id": "F315",
    "report_id": "R022",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Robustness analyses (a) Split-sample jackknife estimator (b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance Notes: See text and notes Figure 2. Across all panels, the regressio"
  },
  {
    "figure_id": "F316",
    "report_id": "R022",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Robustness analyses (a) Split-sample jackknife estimator (b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance Notes: See text and notes Figure 2. Across all panels, the regressio"
  },
  {
    "figure_id": "F317",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance Notes: See text and notes Figure 2. Across all panels, the regression includes 108 countries. The number of observations varies as follows: panel (a) ranges from 1,807 to 1,"
  },
  {
    "figure_id": "F318",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Appendix 1 Figure A1: Impulse responses of primary balances, national vs. supranational rules (a) National rules (b) Supranational rules Notes: See notes Figure 2. The regression includes 108 countries, and the number of observations ranges from 1,807 to 1,"
  },
  {
    "figure_id": "F319",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure A1: Impulse responses of primary balances, national vs. supranational rules (a) National rules (b) Supranational rules Notes: See notes Figure 2. The regression includes 108 countries, and the number of observations ranges from 1,807 to 1,817. Figure A2"
  },
  {
    "figure_id": "F320",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(a) National rules (b) Supranational rules Notes: See notes Figure 2. The regression includes 108 countries, and the number of observations ranges from 1,807 to 1,817. Figure A2: Overlap check: empirical distributions of the treatment propensity score Notes: S"
  },
  {
    "figure_id": "F321",
    "report_id": "R022",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：财政规则的效果，取决于你是在什么时刻定下的｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F322",
    "report_id": "R023",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}"
  },
  {
    "figure_id": "F323",
    "report_id": "R023",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}"
  },
  {
    "figure_id": "F324",
    "report_id": "R023",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}"
  },
  {
    "figure_id": "F325",
    "report_id": "R023",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F326",
    "report_id": "R023",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F327",
    "report_id": "R023",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F328",
    "report_id": "R023",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F329",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F330",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F331",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F332",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F333",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Performance of city-level asset wealth index prediction. a. Performance comparison for two cities across four different machine learning methods trained on various fractions of the census. b. Performance comparison betwe"
  },
  {
    "figure_id": "F334",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Performance of city-level asset wealth index prediction. a. Performance comparison for two cities across four different machine learning methods trained on various fractions of the census. b. Performance comparison betwe"
  },
  {
    "figure_id": "F335",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Performance of city-level asset wealth index prediction. a. Performance comparison for two cities across four different machine learning methods trained on various fractions of the census. b. Performance comparison betwe"
  },
  {
    "figure_id": "F336",
    "report_id": "R023",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: An example of satellite image with geospatial features and asset wealth index label. This is a case of a country-level training sample. systematic observations from $[14]$ , we choose SwinV2-T $[19]$ as a representative"
  },
  {
    "figure_id": "F337",
    "report_id": "R023",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：卫星+AI正在解决一个核心测量难题｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F338",
    "report_id": "R024",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "33. Bain R, Johnston R, Khan S, Hancioglu A, Slaymaker T. Monitoring Drinking Water Quality in Nationally Representative Household Surveys in Low- and Middle-Income Countries: Cross-Sectional Analysis of 27 Multiple Indicator Cluster Surveys 2014–2020. Environ"
  },
  {
    "figure_id": "F339",
    "report_id": "R024",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figures Figure 1. Trial profile Figure 2. Distribution of length-for-age Z-scores, intervention and control groups ## Supporting Information"
  },
  {
    "figure_id": "F340",
    "report_id": "R024",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：刚果金农村WASH项目改善了设施，但未能减少儿童腹泻｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F341",
    "report_id": "R025",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Yusuf, S., Nabeshima, K., & Perkins, D. H. (2006). Under New Ownership: Privatizing China's State-Owned Enterprises. Stanford University Press."
  },
  {
    "figure_id": "F342",
    "report_id": "R025",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "https://www.globalpetrolprices.com Quarterly electricity price, businesses rate (country level) Figure 1. Average Labor Productivity, Sales, and Employment Figure 2. Energy prices Figure 3a. Explicit subsidies to petroleum Figure 3b. Explicit subsidies to elec"
  },
  {
    "figure_id": "F343",
    "report_id": "R025",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Average Labor Productivity, Sales, and Employment Figure 2. Energy prices Figure 3a. Explicit subsidies to petroleum Figure 3b. Explicit subsidies to electricity"
  },
  {
    "figure_id": "F344",
    "report_id": "R025",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Energy prices Figure 3a. Explicit subsidies to petroleum Figure 3b. Explicit subsidies to electricity Robust standard errors in parentheses"
  },
  {
    "figure_id": "F345",
    "report_id": "R025",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：电价上涨1%，高能耗无节能措施企业裁员1.5%｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F346",
    "report_id": "R026",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## 5.2.1 Experimental design We estimate the effects of personalized tax letters on current and subsequent property tax payments for women and men by leveraging a large-scale field experiment conducted by Cruces et al. (2023) in Tres de Febrero in October 2020"
  },
  {
    "figure_id": "F347",
    "report_id": "R026",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Assessed property value by gender, 2018"
  },
  {
    "figure_id": "F348",
    "report_id": "R026",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Tax gap by gender, 2019"
  },
  {
    "figure_id": "F349",
    "report_id": "R026",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Tax gap by gender, 2019 Figure 5: Bills paid on-time, 2019"
  },
  {
    "figure_id": "F350",
    "report_id": "R026",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Effective tax rates, 2019"
  },
  {
    "figure_id": "F351",
    "report_id": "R026",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Effective tax rates, by gender, 2019"
  },
  {
    "figure_id": "F352",
    "report_id": "R026",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Property tax compliance: women and men respond similarly to personalized tax letters"
  },
  {
    "figure_id": "F353",
    "report_id": "R026",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Property tax compliance: women and men respond similarly to personalized tax letters Timely payments Timely and late"
  },
  {
    "figure_id": "F354",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Property tax compliance: men respond earlier to the letter, but women catch up (a) Distribution of payment date for women and men (October 2020 bill)"
  },
  {
    "figure_id": "F355",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Property tax compliance: men respond earlier to the letter, but women catch up (a) Distribution of payment date for women and men (October 2020 bill) (b) Treated vs Control (October 2020 bill)"
  },
  {
    "figure_id": "F356",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles"
  },
  {
    "figure_id": "F357",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles (b) Treated vs Control"
  },
  {
    "figure_id": "F358",
    "report_id": "R026",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles (b) Treated vs Control Notes: These figures show the effect of the communication campaign on payment rates by quintiles of assesse"
  },
  {
    "figure_id": "F359",
    "report_id": "R026",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles (b) Treated vs Control Notes: These figures show the effect of the communication campaign on payment rates by quintiles of assesse"
  },
  {
    "figure_id": "F360",
    "report_id": "R026",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "SUPPLEMENTARY MATERIALS FOR: \"EXPLORING THE GENDER DIVIDE IN REAL ESTATE OWNERSHIP AND PROPERTY TAX COMPLIANCE\" ## A Residential ownership in Tres de Febrero Based on the 2021 ARBA cadaster, the municipality boasts approximately 140,000 registered properties. "
  },
  {
    "figure_id": "F361",
    "report_id": "R026",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure A.1: Number of residential properties Note: This map presents the number of residential properties at the block \"manzana\" Level in Tres de Febrero 2021 ARBA register. Figure A.2: Assessed values for residential properties, 2018 Note: This figure present"
  },
  {
    "figure_id": "F362",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure C.7: Example of the intervention letter Figure C.8: Property tax compliance: no effect for the placebo bill of July 2020 (a) Distribution of payment date for women and men (July 2020 bill) (b) Treated vs Control (July 2020 bill) Notes: Panel (a) shows t"
  },
  {
    "figure_id": "F363",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure C.8: Property tax compliance: no effect for the placebo bill of July 2020 (a) Distribution of payment date for women and men (July 2020 bill) (b) Treated vs Control (July 2020 bill) Notes: Panel (a) shows the fraction of men and women paying the July 20"
  },
  {
    "figure_id": "F364",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "(b) Treated vs Control (July 2020 bill) Notes: Panel (a) shows the fraction of men and women paying the July 2020 bill before and after the due date (July 8th, 2020). The area of each histogram integrates into one. A larger bar on a particular date means that "
  },
  {
    "figure_id": "F365",
    "report_id": "R026",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Notes: Panel (a) shows the fraction of men and women paying the July 2020 bill before and after the due date (July 8th, 2020). The area of each histogram integrates into one. A larger bar on a particular date means that the payment frequency of the correspondi"
  },
  {
    "figure_id": "F366",
    "report_id": "R026",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：女性在高端房产的拥有率不足20%，但税收政策对她们更不公平｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F367",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Temperature Response Functions by GDP and Firm Size Vertical axes show changes in the logarithm of sales revenues. Horizontal axes show differences in current fiscal year temperatures compared to historical average tempe"
  },
  {
    "figure_id": "F368",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Temperature Response Functions by GDP and Firm Characteristics The top panel shows heterogeneity by firm age. The bottom shows heterogeneity by the proportion of sales that are direct exports. Vertical axes show changes"
  },
  {
    "figure_id": "F369",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Temperature Response Functions by GDP and Sectoral Attributes Vertical axes show changes in the logarithm of sales revenues. Horizontal axes show differences in current fiscal year temperatures compared to historical ave"
  },
  {
    "figure_id": "F370",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Temperature Response Functions by GDP and Attributes of Business Environment. The top panel shows heterogeneity by access to finance. The bottom panel shows heterogeneity by the regulatory environment. Vertical axes show"
  },
  {
    "figure_id": "F371",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Temperature Response Functions by GDP and Quality of Public Goods The top panel shows heterogeneity by the quality of electricity access. The bottom panel shows heterogeneity by security. Vertical axes show changes in th"
  },
  {
    "figure_id": "F372",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Temperature Response Functions by GDP and Quality of Public Goods The top panel shows heterogeneity by the quality of electricity access. The bottom panel shows heterogeneity by security. Vertical axes show changes in th"
  },
  {
    "figure_id": "F373",
    "report_id": "R027",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Temperature Response Functions by GDP and Quality of Public Goods The top panel shows heterogeneity by the quality of electricity access. The bottom panel shows heterogeneity by security. Vertical axes show changes in th"
  },
  {
    "figure_id": "F374",
    "report_id": "R027",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：全球16万家企业数据揭示，气候适应力正在制造新的贫富分化｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F375",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "This paper is set against the backdrop of the military takeover of the Government of Myanmar since 2021, which was followed by high levels of violent conflict and economic slowdown. We explore the factors prompting high-skilled youth to migrate abroad for work"
  },
  {
    "figure_id": "F376",
    "report_id": "R028",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Standard errors clustered at the township level in parentheses. Controls include individual demographic and labor market characteristics including occupation, sector of employment, and field of study. 5.2.2 Instrumental Variables Estimation We employ Instrumen"
  },
  {
    "figure_id": "F377",
    "report_id": "R028",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：冲突如何迫使高技能人才主动“降级”求职｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F378",
    "report_id": "R029",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Sectoral Employment Transitions by Gender (a) Transitions Across Sectors: Men (b) Transitions Across Sectors: Women (c) (De)Industrialization: Men (d) (De)Industrialization: Women"
  },
  {
    "figure_id": "F379",
    "report_id": "R029",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Sectoral Employment Transitions by Gender (a) Transitions Across Sectors: Men (b) Transitions Across Sectors: Women (c) (De)Industrialization: Men (d) (De)Industrialization: Women"
  },
  {
    "figure_id": "F380",
    "report_id": "R029",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Occupational Employment Shares by Gender and by Sector (a) Transition Across Occupations: Men (b) Transition Across Occupations: Women More generally, sectors employ occupations in different proportions, creating a d"
  },
  {
    "figure_id": "F381",
    "report_id": "R029",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Occupational Employment Shares by Gender and by Sector (a) Transition Across Occupations: Men (b) Transition Across Occupations: Women More generally, sectors employ occupations in different proportions, creating a d"
  },
  {
    "figure_id": "F382",
    "report_id": "R029",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: H-Index of Gender Segregation across Sectors and Occupations (a) Aggregate Index (b) Fraction Explained Within Sector ## 2.5 Gender Gaps within Countries over Time We next use a core sample of six large economies – I"
  },
  {
    "figure_id": "F383",
    "report_id": "R029",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: H-Index of Gender Segregation across Sectors and Occupations (a) Aggregate Index (b) Fraction Explained Within Sector ## 2.5 Gender Gaps within Countries over Time We next use a core sample of six large economies – I"
  },
  {
    "figure_id": "F384",
    "report_id": "R029",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Effect of Gender Barriers on Sectoral and Occupational Employment Shares (a) Sectoral Population Shares: All (b) Sectoral Population Shares: Women (c) Sectoral Employment Shares (d) Occupational Population Shares"
  },
  {
    "figure_id": "F385",
    "report_id": "R029",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Effect of Gender Barriers on Sectoral and Occupational Employment Shares (a) Sectoral Population Shares: All (b) Sectoral Population Shares: Women (c) Sectoral Employment Shares (d) Occupational Population Shares"
  },
  {
    "figure_id": "F386",
    "report_id": "R029",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：性别壁垒下降贡献了全球28%的人均GDP增长，但印度是反例｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F387",
    "report_id": "R030",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Map of locations covered by survey by treatment and control wards ## 3.1 Tax Administrative Data Administrative data from the TRA was utilized to analyze the impact of the intervention on taxpayers' behavior. This data"
  },
  {
    "figure_id": "F388",
    "report_id": "R030",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：中小企业怕的不是税务官，而是“税务官来了又走”｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F389",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Density of log of per capita expenditure over time Note: i) Authors' estimation based on VHLSSs data Note: i) Authors' estimation based on VHLSSs data ## Supporting Information for review and online publication only"
  },
  {
    "figure_id": "F390",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Density of log of per capita expenditure over time Note: i) Authors' estimation based on VHLSSs data Note: i) Authors' estimation based on VHLSSs data ## Supporting Information for review and online publication only"
  },
  {
    "figure_id": "F391",
    "report_id": "R031",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：越南经济增长的“穷人隔离”悖论｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F392",
    "report_id": "R032",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 2 Data and Descriptive Analysis We used trade data from BACI (Gaulier and Zignago, 2010). $^{2}$ We used the import data of the selected countries from 1995 to 2021, covering 27 continuous years. The data contains information on the total values, quantities"
  },
  {
    "figure_id": "F393",
    "report_id": "R032",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：小国正在从全球化中收获超预期的福利，但多数人忽视了这一点｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F394",
    "report_id": "R033",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Road network in Belgian Congo, 1960 Maintenance of feeder roads in rural areas was by and large neglected, and rural populations were forced to rely on subsistence farming; underpaid government agents and local authoriti"
  },
  {
    "figure_id": "F395",
    "report_id": "R033",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Road network in Belgian Congo, 1960 Maintenance of feeder roads in rural areas was by and large neglected, and rural populations were forced to rely on subsistence farming; underpaid government agents and local authoriti"
  },
  {
    "figure_id": "F396",
    "report_id": "R033",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Political Violence in the DRC Notes: Figure shows the location of ACLED and UCDP events in the DRC. ## 3.2 A New Database of Road Investments First, we created a database of road transport projects relying on multiple"
  },
  {
    "figure_id": "F397",
    "report_id": "R033",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Map of Geolocalized Projects One of the main concerns regarding the analysis of roads and violence is the self-selection of road projects into peaceful regions or peaceful periods in violent regions. Three arguments spea"
  },
  {
    "figure_id": "F398",
    "report_id": "R033",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Roads and Violence at the Province Level Notes: Figure shows the log of armed conflict event totals per million inhabitants together with the log of completed road projects at the province level. Finally, we provide ev"
  },
  {
    "figure_id": "F399",
    "report_id": "R033",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Example of satellite imagery aggregation Project 04 Segments Project 04 Segments (Zoomed) Notes: The road for one of the three projects is divided into segments of 10 km. Segments 180, 181, and 182 are highlighted in"
  },
  {
    "figure_id": "F400",
    "report_id": "R033",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation 2012"
  },
  {
    "figure_id": "F401",
    "report_id": "R033",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is mar"
  },
  {
    "figure_id": "F402",
    "report_id": "R033",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is mar"
  },
  {
    "figure_id": "F403",
    "report_id": "R033",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is mar"
  },
  {
    "figure_id": "F404",
    "report_id": "R033",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Mining Locations and Roads Notes: Mining locations for small artisanal mines and large projects together with road investments by international actors. ## 4 Roads and Armed Conflict ## 4.1 Hypothesis and Descriptive Ev"
  },
  {
    "figure_id": "F405",
    "report_id": "R033",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Roads and Armed Conflict in North Kivu Notes: The Figure shows the number of violent events sourced from UCDP and the number of PRIO cells with a newly or recently (last year) completed road project for Nord-Kivu."
  },
  {
    "figure_id": "F406",
    "report_id": "R033",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Road Stock and Armed Conflict in North Kivu Notes: The Figure shows the number of violent events sourced from UCDP and the road project Stock for North Kivu. A newly completed project takes a value of one. This value g"
  },
  {
    "figure_id": "F407",
    "report_id": "R033",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Road Stock and Armed Conflict in North Kivu Notes: The Figure shows the number of violent events sourced from UCDP and the road project Stock for North Kivu. A newly completed project takes a value of one. This value g"
  },
  {
    "figure_id": "F408",
    "report_id": "R033",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Roads and Events: PreMDiD Notes: Figure shows the effect of road completion at year 0 compared to a control group that is matched by violence prediction in year -1. Figure 13: Roads and Fatalities: PreMDiD Notes: Fig"
  },
  {
    "figure_id": "F409",
    "report_id": "R033",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Roads and Events: PreMDiD Notes: Figure shows the effect of road completion at year 0 compared to a control group that is matched by violence prediction in year -1. Figure 13: Roads and Fatalities: PreMDiD Notes: Fig"
  },
  {
    "figure_id": "F410",
    "report_id": "R033",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：刚果金的道路修复带来了和平，但这份红利只有三年有效期｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F411",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Trends in Non-Farm Employment by Gender"
  },
  {
    "figure_id": "F412",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Trends in Non-Farm Employment by Gender Notes: The above figures shows trends in non-farm employment categories and sectors, conditional on participation in the labour force, and disaggregated by gender. NSS survey r"
  },
  {
    "figure_id": "F413",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Trends in Non-Farm Employment by Gender and Secondary Education"
  },
  {
    "figure_id": "F414",
    "report_id": "R034",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Trends in Non-Farm Employment by Gender and Secondary Education"
  },
  {
    "figure_id": "F415",
    "report_id": "R034",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Trends in Non-Farm Employment by Gender and Secondary Education Notes: The above figures shows trends in non-farm employment categories and sectors, conditional on participation in the labour force, and disaggreg"
  },
  {
    "figure_id": "F416",
    "report_id": "R034",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F417",
    "report_id": "R034",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F418",
    "report_id": "R034",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F419",
    "report_id": "R034",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F420",
    "report_id": "R034",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F421",
    "report_id": "R034",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F422",
    "report_id": "R034",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F423",
    "report_id": "R034",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：印度农村非农就业的真正瓶颈不是技能，是结构｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F424",
    "report_id": "R035",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. The impact of DSM on farmers' decision to purchase maize and wheat seeds, event study aggregation"
  },
  {
    "figure_id": "F425",
    "report_id": "R035",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. The impact of DSM on farmers' decision to purchase maize and wheat seeds, event study aggregation"
  },
  {
    "figure_id": "F426",
    "report_id": "R035",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The results from the event-study (dynamic) aggregation on the quantity of maize and wheat seed purchased by farmers show coefficients similar to those from the cohort and survey year aggregations. DSM led to a 46 percent increase in the quantity of maize seed "
  },
  {
    "figure_id": "F427",
    "report_id": "R035",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The results from the event-study (dynamic) aggregation on the quantity of maize and wheat seed purchased by farmers show coefficients similar to those from the cohort and survey year aggregations. DSM led to a 46 percent increase in the quantity of maize seed "
  },
  {
    "figure_id": "F428",
    "report_id": "R035",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. The impact of DSM on maize and wheat yields, event study aggregation (a) Maize (b) Wheat Given the lack of a significant impact of DSM on wheat seed purchases and productivity, we extend our analysis to examine whether DSM has any effect on seed purc"
  },
  {
    "figure_id": "F429",
    "report_id": "R035",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. The impact of DSM on maize and wheat yields, event study aggregation (a) Maize (b) Wheat Given the lack of a significant impact of DSM on wheat seed purchases and productivity, we extend our analysis to examine whether DSM has any effect on seed purc"
  },
  {
    "figure_id": "F430",
    "report_id": "R035",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "A related explanation for the differences in crop-specific outcomes stems from the historical evolution of DSM in Ethiopia. Even before the introduction of DSM, there was considerable accumulated experience in maize seed production and marketing, along with cl"
  },
  {
    "figure_id": "F431",
    "report_id": "R035",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "In fact, data on the DSM approach indicate that the initial emphasis was placed exclusively on maize beginning in 2011, with the expansion to wheat following in 2013 (Figure 4). The resulting supply response for maize occurred more rapidly than for wheat: wher"
  },
  {
    "figure_id": "F432",
    "report_id": "R035",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：种子市场化改革让埃塞俄比亚玉米增产18%，但小麦为何失效？｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F433",
    "report_id": "R036",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：数字化企业更环保、更培训，但更少女性高管｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F434",
    "report_id": "R037",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Timeline of reform. Note: This timeline depicts the subsequent budget law postponements of the enforcement of the Corporate Income Tax (CIT) reform for Offshore firms, thus leaving the full exemption in place until 201"
  },
  {
    "figure_id": "F435",
    "report_id": "R037",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Participation of offshore sector (a) Total firms (b) Total employment (c) Total revenue"
  },
  {
    "figure_id": "F436",
    "report_id": "R037",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Participation of offshore sector (a) Total firms (b) Total employment (c) Total revenue (d) Total export value Note: These figures display the participation of offshore firms in several economic aggregates over t"
  },
  {
    "figure_id": "F437",
    "report_id": "R037",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Participation of offshore sector (a) Total firms (b) Total employment (c) Total revenue (d) Total export value Note: These figures display the participation of offshore firms in several economic aggregates over t"
  },
  {
    "figure_id": "F438",
    "report_id": "R037",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms"
  },
  {
    "figure_id": "F439",
    "report_id": "R037",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms (b) Total Revenue (c) Total Employment Note: These figures display the composition of offshore firms by economic sectors. In panel (a) we present how fi"
  },
  {
    "figure_id": "F440",
    "report_id": "R037",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms (b) Total Revenue (c) Total Employment Note: These figures display the composition of offshore firms by economic sectors. In panel (a) we present how fi"
  },
  {
    "figure_id": "F441",
    "report_id": "R037",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms (b) Total Revenue (c) Total Employment Note: These figures display the composition of offshore firms by economic sectors. In panel (a) we present how fi"
  },
  {
    "figure_id": "F442",
    "report_id": "R037",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Aggregate quantities (normalized) - Offshore versus Onshore (a) Total firms normalized (b) Normalized numbers of entrants (c) Normalized numbers of exiters"
  },
  {
    "figure_id": "F443",
    "report_id": "R037",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Aggregate quantities (normalized) - Offshore versus Onshore (a) Total firms normalized (b) Normalized numbers of entrants (c) Normalized numbers of exiters (d) Number of employees - normalized"
  },
  {
    "figure_id": "F444",
    "report_id": "R037",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Aggregate quantities (normalized) - Offshore versus Onshore (a) Total firms normalized (b) Normalized numbers of entrants (c) Normalized numbers of exiters (d) Number of employees - normalized (e) Total wage bi"
  },
  {
    "figure_id": "F445",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing)"
  },
  {
    "figure_id": "F446",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms"
  },
  {
    "figure_id": "F447",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms (b) Entry (c) Exit"
  },
  {
    "figure_id": "F448",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms (b) Entry (c) Exit (d) Employment"
  },
  {
    "figure_id": "F449",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms (b) Entry (c) Exit (d) Employment (e) Wage bill"
  },
  {
    "figure_id": "F450",
    "report_id": "R037",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Employment outcomes on the balanced sample - Offshore versus Onshore (a) Ln(Employees) (b) Firm has more than 2 employees (c) Firm has more than 5 employees"
  },
  {
    "figure_id": "F451",
    "report_id": "R037",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Employment outcomes on the balanced sample - Offshore versus Onshore (a) Ln(Employees) (b) Firm has more than 2 employees (c) Firm has more than 5 employees (d) Firm has more than 10 employees"
  },
  {
    "figure_id": "F452",
    "report_id": "R037",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Employment outcomes on the balanced sample - Offshore versus Onshore (a) Ln(Employees) (b) Firm has more than 2 employees (c) Firm has more than 5 employees (d) Firm has more than 10 employees Figure 7: Other out"
  },
  {
    "figure_id": "F453",
    "report_id": "R037",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill)"
  },
  {
    "figure_id": "F454",
    "report_id": "R037",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill) (b) $\\mathrm{Ln}(\\mathrm{Revenue})$ (c) $\\mathrm{Ln}(\\mathrm{Profits})$ Note: Firm-level DID obtained from estimating equation (3) on"
  },
  {
    "figure_id": "F455",
    "report_id": "R037",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill) (b) $\\mathrm{Ln}(\\mathrm{Revenue})$ (c) $\\mathrm{Ln}(\\mathrm{Profits})$ Note: Firm-level DID obtained from estimating equation (3) on"
  },
  {
    "figure_id": "F456",
    "report_id": "R037",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill) (b) $\\mathrm{Ln}(\\mathrm{Revenue})$ (c) $\\mathrm{Ln}(\\mathrm{Profits})$ Note: Firm-level DID obtained from estimating equation (3) on"
  },
  {
    "figure_id": "F457",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure A21: Honest DID - Industry-level impacts on Log(number of firms) (a) Original dynamic estimates (Fig 5a) (b) Manufacturing - average post-period (c) Manufacturing - last post-period (d) Full sample - average post-period (e) Full sample - last post-perio"
  },
  {
    "figure_id": "F458",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "(a) Original dynamic estimates (Fig 5a) (b) Manufacturing - average post-period (c) Manufacturing - last post-period (d) Full sample - average post-period (e) Full sample - last post-period Note: Panel (a) reproduces Figure 5(a) in the main text, while remaini"
  },
  {
    "figure_id": "F459",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "(b) Manufacturing - average post-period (c) Manufacturing - last post-period (d) Full sample - average post-period (e) Full sample - last post-period Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensit"
  },
  {
    "figure_id": "F460",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "(e) Full sample - last post-period Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Mbar refers to "
  },
  {
    "figure_id": "F461",
    "report_id": "R037",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Mbar refers to multiples of the largest deviation "
  },
  {
    "figure_id": "F462",
    "report_id": "R037",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：减税救不了实体经济，别再迷信企业税收优惠了｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F463",
    "report_id": "R038",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: AI Occupational Exposure by Country Income Group AI Occupation Exposure by Income group"
  },
  {
    "figure_id": "F464",
    "report_id": "R038",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: AI Occupational Exposure by Country Income Group AI Occupation Exposure by Income group Figure 3: AI Occupational Exposure by GNI per capita"
  },
  {
    "figure_id": "F465",
    "report_id": "R038",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: AI Occupational Exposure by Country Income Group AI Occupation Exposure by Income group Figure 3: AI Occupational Exposure by GNI per capita"
  },
  {
    "figure_id": "F466",
    "report_id": "R038",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: AI Occupational Exposure by GNI per capita We categorize the AIOE scores into four exposure levels (high, moderately high, moderately low and low exposure) and analyze these across country income groups and sub-groups"
  },
  {
    "figure_id": "F467",
    "report_id": "R038",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: AI Occupational Exposure by GNI per capita We categorize the AIOE scores into four exposure levels (high, moderately high, moderately low and low exposure) and analyze these across country income groups and sub-groups"
  },
  {
    "figure_id": "F468",
    "report_id": "R038",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## 3.2. The role of worker characteristics in determining AI occupational exposure There is no clear difference in the age pattern across income groups. Younger workers, aged 15-24, tend to have left school earlier and are not employed in occupations with AI e"
  },
  {
    "figure_id": "F469",
    "report_id": "R038",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "There is no clear difference in the age pattern across income groups. Younger workers, aged 15-24, tend to have left school earlier and are not employed in occupations with AI exposure (Figure 5). This may be explained by the fact that workers who leave educat"
  },
  {
    "figure_id": "F470",
    "report_id": "R038",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: AI Exposure by Location and Country Income Level"
  },
  {
    "figure_id": "F471",
    "report_id": "R038",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: AI Exposure by Location and Country Income Level"
  },
  {
    "figure_id": "F472",
    "report_id": "R038",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: AI Exposure by Location and Country Income Level When analyzing the relationship between income group, exposure to AI in the workplace and education, two patterns emerge: In all countries, the more educated workers are"
  },
  {
    "figure_id": "F473",
    "report_id": "R038",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: AI Exposure by Location and Country Income Level When analyzing the relationship between income group, exposure to AI in the workplace and education, two patterns emerge: In all countries, the more educated workers are"
  },
  {
    "figure_id": "F474",
    "report_id": "R038",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## 3.3. The importance of job choice for AI occupational exposure around the world High-skilled occupations are more exposed to AI than medium- and low-skilled occupations. The ILO defines high-skilled occupations as ISCO categories for \"Managers\", \"Profession"
  },
  {
    "figure_id": "F475",
    "report_id": "R038",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: AI Exposure by Electricity Access, Location and Country Income Level"
  },
  {
    "figure_id": "F476",
    "report_id": "R038",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: AI Exposure by Electricity Access, Location and Country Income Level ## 4. Conclusion This paper discusses the potential of artificial intelligence for the next generation of work. While most previous economic research"
  },
  {
    "figure_id": "F477",
    "report_id": "R038",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: AI occupation exposure for the 2- and 4-digit occupation codes ## AI occupation exposure information detail for 2 digit and 4 digit ISCO codes - Professionals • Technicians and associate professionals • Service and s"
  },
  {
    "figure_id": "F478",
    "report_id": "R038",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: AI occupation exposure for the 2- and 4-digit occupation codes ## AI occupation exposure information detail for 2 digit and 4 digit ISCO codes - Professionals • Technicians and associate professionals • Service and s"
  },
  {
    "figure_id": "F479",
    "report_id": "R038",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: AI exposure and industry sector AI Exposure by Industry Sector AI Occupation Exposure by Country"
  },
  {
    "figure_id": "F480",
    "report_id": "R038",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: AI exposure and industry sector AI Exposure by Industry Sector AI Occupation Exposure by Country Note: Results are population weighted and include workers aged 15 to 64"
  },
  {
    "figure_id": "F481",
    "report_id": "R038",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：AI对低收入国家劳动力的冲击，可能远小于市场预期｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F482",
    "report_id": "R039",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures"
  },
  {
    "figure_id": "F483",
    "report_id": "R039",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures"
  },
  {
    "figure_id": "F484",
    "report_id": "R039",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures"
  },
  {
    "figure_id": "F485",
    "report_id": "R039",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F486",
    "report_id": "R039",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F487",
    "report_id": "R039",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F488",
    "report_id": "R039",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F489",
    "report_id": "R039",
    "label": "世界银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界银行｜世界银行：一场降雨如何重塑印度农村经济的全部链条｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F490",
    "report_id": "R040",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：CEO们搞砸AI转型的五个共同死穴｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F491",
    "report_id": "R041",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：企业转型的成败，终于被拆解到了“人”这一层｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F492",
    "report_id": "R042",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "As a result, the journey model's impact has plateaued. Personalization must evolve by changing its unit of decision from marketer-orchestrated journeys to agent-orchestrated actions, with AI agents selecting, sequencing, and composing interactions from a modul"
  },
  {
    "figure_id": "F493",
    "report_id": "R042",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 1 AI-Native Marketing Drives More Efficient, More Effective Growth Across the Enterprise Savings from NBA Savings from AI Reduction in campaign cycle time More assets in market"
  },
  {
    "figure_id": "F494",
    "report_id": "R042",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Savings from AI Reduction in campaign cycle time More assets in market Increase in addressable revenue ## How NBA Is Evolving Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an org"
  },
  {
    "figure_id": "F495",
    "report_id": "R042",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Reduction in campaign cycle time More assets in market Increase in addressable revenue ## How NBA Is Evolving Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an organization sits o"
  },
  {
    "figure_id": "F496",
    "report_id": "R042",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "## How NBA Is Evolving Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an organization sits on this continuum is the first step toward preparing for what comes next. (See Exhibit 2"
  },
  {
    "figure_id": "F497",
    "report_id": "R042",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "# Four Capabilities of Agent-Native NBA Evolving to agent-native NBA requires building four interconnected capabilities: composable shelf, agent architecture, tools/state management, and learning and optimization. (See Exhibit 3.) These four capabilities const"
  },
  {
    "figure_id": "F498",
    "report_id": "R042",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Learning and optimization Experimentation engine that measures every shelf asset and agent decision through causal testing, compounding performance over time ## Inside the Composable Shelf The composable shelf is the modular catalog of offers, creatives, and m"
  },
  {
    "figure_id": "F499",
    "report_id": "R042",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "# Building for Tomorrow's Agent Infrastructure The agent-native architecture does not require or assume a greenfield build. Every component that organizations build today for the second evolution of NBA will map directly to a capability that agents can use in "
  },
  {
    "figure_id": "F500",
    "report_id": "R042",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：营销的“旅程”时代已死，“代理”时代已来｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F501",
    "report_id": "R043",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：营销战役的终结，不是营销的终结｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F502",
    "report_id": "R044",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "NBA action selection occurs across three layers: propensity and uplift scoring, contextual bandits, and agent-based reasoning. These layers are additive, not alternative. Systems don't necessarily need to graduate from one to the next, however, as each layer h"
  },
  {
    "figure_id": "F503",
    "report_id": "R044",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "These limitations are not bugs. They are inherent to the paradigm. Moving past them requires both a different system architecture and an additional (not alternative) class of decisioning models. ## The Two-Track Architecture The production system that makes La"
  },
  {
    "figure_id": "F504",
    "report_id": "R044",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：下一代“最佳下一步行动”不是算法升级，是决策架构的重构｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]