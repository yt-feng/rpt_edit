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
    "title": "GS：亚洲通胀最猛烈的阶段已经过去，但结构性分化才刚刚开始",
    "digest": "[wechat_article.md]\n# GS：亚洲通胀最猛烈的阶段已经过去，但结构性分化才刚刚开始\n\n当能源价格从峰值回落、供应链瓶颈逐步疏通，市场对亚洲通胀的焦虑正在快速降温。但GS最新发布的《亚太通胀监测》报告揭示了一个更微妙的图景：通胀压力整体见顶，并不意味着所有经济体都将同步回归平静。真正值得关注的，不是通胀是否回落，而是回落之后，各经济体的价格粘性、政策空间和结构韧性将如何重新定义资产定价和投资逻辑。\n\n这份发布于2026年6月的报告，基于截至5月的CPI/PPI数据以及6月中旬的能源价格走势，给出了一个清晰的主判断：亚洲通胀的能源冲击阶段已经过去，但核心通胀的路径分化、工资传导的不对称性，以及政策退出的节奏差异，将成为未来6至12个月市场定价的核心变量。GS同时下调了布伦特原油Q4预测至80美元/桶，这一调整本身就在释放一个信号——供给侧的尾部风险正在收窄，但需求侧的韧性尚未被充分定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源价格冲击正在退潮，但输入型通胀的滞后效应仍未被完全消化\n\nGS大宗商品团队将布伦特原油Q4预测从90美元/桶下调至80美元/桶，直接原因是霍尔木兹海峡恢复通航的前景改善。报告中的图表清晰显示，原油价格已从4月超过140美元/桶的峰值大幅回落，6月布伦特现货价格已降至约80美元/桶。这是一个重要的拐点信号。\n\n但真正需要推敲的是传导链条的时滞。亚洲经济体在2026年初经历了剧烈的进口价格和生产者价格飙升，尽管部分国家通过隐性或显性补贴缓冲了零售燃料价格的上行，但企业端的成本压力并未完全消除。GS的数据显示，韩国、中国、日本及其他亚洲经济体的进口价格同比变化在3月至4月间出现剧烈波动，部分经济体在5月仍处于负值区间。这意味着，能源价格的回落尚未完全反映到终端消费品价格中。\n\n对投资者而言，这一滞后效应意味着\n\n[... middle omitted ...]\n\n新定价？这些问题的答案，可能就藏在报告图表背后的二阶影响中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚太通胀，油价的顶已经过了\n\n🌏 亚太通胀观察\n\n能源价格拐点已至，通胀压力正在缓解\n\n---\n\n最近某外资投行发布了亚太通胀追踪报告，核心结论很清晰：**能源价格已经过了最猛的阶段**。\n\n1️⃣ 油价预期下调\n布伦特原油Q4预测从$90/桶降到$80/桶，主要原因是霍尔木兹海峡有望重新开放，全球油价这几周已经大幅回落。研报显示，油价从4月高点$140跌到6月约$80，降幅明显。\n\n2️⃣ 通胀压力分化明显\n- 菲律宾、泰国等低收入经济体过去三个月CPI年化超10%，但5月环比已明显放缓\n- 高收入经济体（日本除外）工资通胀反而偏软\n- 整体来看，核心通胀目前还算温和\n\n3️⃣ 进口价格正在传导\n年初以来亚洲进口价格大幅上涨，但部分国家有补贴缓冲。随着能源价格回落，**下一个月的通胀数据预计会明显改善**。\n\n4️⃣ 风险转向下行\n研报提到，战前多数国家CPI在目标区间内，现在整体略高于目标。但能源价格已从高点回落一段时间，通胀预测的风险现在偏向下行。\n\n---\n\n几个值得关注的细节：\n- 韩国、中国、日本的原油进口来源已在调整\n- 炼油产品价格虽回落，但仍高于战前水平\n- 中东局势仍是最大变量\n\n研报整体\n\n[... middle omitted ...]\n\narly 2026 (though implicit or explicit subsidies have moderated or capped retail fuel prices in some countries), but are set to ease materially in the next monthly update.  \n■ Pre-war, CPI inf\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "摩根斯坦利：黄金的下一段行情，关键不在央行，而在ETF能否重新入场",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：黄金的下一段行情，关键不在央行，而在ETF能否重新入场\n\n当前市场对黄金的讨论，大多集中在央行购金、地缘冲突和通胀对冲这三个传统叙事上。但摩根斯坦利在最新发布的这份报告中，提出了一个更值得推敲的判断：黄金的结构性支撑仍然坚实，但短期内推动价格从当前水平走向每盎司5200美元的关键变量，已经不是央行，而是ETF资金流的重新激活。报告明确指出，如果没有ETF需求的配合，他们的目标价将变得难以实现。\n\n这份报告的价值不在于重申“黄金长期看多”这一共识，而在于它精准地拆解了当前黄金定价中三个相互拉扯的力量：地缘缓和的正面效应、美联储鹰派立场的压制、以及央行结构性买盘的托底。这三个力量叠加的结果，不是简单的多空判断，而是一个需要特定触发条件才能兑现的价格路径。\n\n报告的核心主张可以概括为一句话：黄金的上行风险仍在，但通往5200美元的道路已经变窄，而这条道路能否走通，取决于一个尚未被满足的条件——ETF买家是否愿意重新进场。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中东缓和对黄金是利好，但路径与传统避险逻辑正好相反\n\n很多人直觉上认为，中东冲突缓和会削弱黄金的避险需求，从而打压金价。但摩根斯坦利的分析得出了一个反直觉的结论：冲突缓和反而对黄金构成支撑。原因在于，本轮中东冲突中，黄金并没有扮演传统的避险角色。\n\n报告提供了一个关键的分析框架：供给冲击比需求冲击更难对冲。中东冲突本质上是一个供给侧的冲击——它推高油价、抬高债券收益率、并对油气进口国的财政平衡造成压力。在这种环境下，黄金的避险功能反而受到抑制。报告特别指出，土耳其等国家在压力下甚至不得不卖出黄金。数据显示，冲突升级期间黄金的平均日表现为负值，而缓和期间反而录得正回报。\n\n这意味着，地缘缓和对黄金的正面效应，不是通过“避险需求下降”这个渠道，\n\n[... middle omitted ...]\n\n会持续跟踪ETF资金流、央行购金节奏和美联储政策路径的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n黄金的十字路口：中东降温与美联储博弈\n\n金价进退两难\n\n中东局势缓和支持金价，但美联储偏鹰的态度构成新挑战。某外资投行维持看多倾向，但认为5200美元目标实现难度加大。\n\n1/ 中东降温反而利好黄金\n这次中东冲突中，黄金并没有发挥传统避险功能，因为供给冲击比需求冲击更难对冲。冲突反而给金价带来两重压力：推高债券收益率、迫使油气进口国卖金换汇。因此局势缓和，对金价是正向支撑。油价走低还能缓解各国央行收紧货币或卖出黄金的压力。\n\n2/ 央行买盘仍是最大支撑\n世界黄金协会调查显示，45%的受访央行预计未来12个月将增加黄金储备。中国央行已加速购金，3-5月买入23吨，而此前12个月合计仅19吨。官方需求是结构性利好。\n\n3/ 美联储是短期最大变数\n鹰派表态推高加息预期，提高了持有黄金的机会成本，尤其影响ETF流入。不过历史数据显示，加息后一个月金价平均仍上涨0.84%。美联储预计将暂停至2026年，通胀路径可能被高估，存在修正空间。\n\n4/ 5200目标的实现条件\n需要两个变量配合：一是ETF需求的回归，目前ETF对利率路径、实际收益率和美元走势高度敏感；二是油价走低能否真正传导至利率预期，从而改变美联储立场。\n\n[... middle omitted ...]\n\nis the main near-term constraint. A hawkish hold raises the opportunity cost of holding gold and is likely to matter most through ETF flows.  \nWe retain an upside bias, but \\$5,200/oz in 2H26 \n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R003",
    "title": "JPM：中东局势缓和，日本日化与造纸股迎来结构性成本重估",
    "digest": "[wechat_article.md]\n# JPM：中东局势缓和，日本日化与造纸股迎来结构性成本重估\n\n地缘政治风险从来不只是新闻标题。当美国与伊朗在6月17日签署谅解备忘录、暂时结束敌对状态的消息传出，全球资本市场的第一反应是油价回落。但JPM日本股票研究团队在最新发布的一份跨行业报告中提出了一个更值得深思的问题：中东局势改善对不同行业、不同公司的利润影响，是否被市场以同一把尺子衡量？答案是否定的。这份报告的核心判断是，市场低估了成本端改善对日本个人护理公司的利润弹性，高估了造纸企业的定价权风险，而对化妆品公司的传导链条则完全看错了方向。\n\n这不是一则简单的“油价跌了，成本降了”的故事。真正需要拆解的是，成本下降的时滞、传导机制、以及不同行业在面对成本改善时截然不同的议价能力。这些变量，决定了哪一类公司能从地缘政治红利中真正获益。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 个人护理公司拥有最清晰的成本弹性，但市场可能忽略了4-6个月的传导时滞\n\nJPM分析师Akiko Kuwahara在报告中给出了一个非常具体的测算：原油价格每变动1美元/桶（按年计算），对Unicharm和花王的营业利润影响约为5-6亿日元，对狮王的影响约为1-2亿日元。这个数字本身并不惊人，但关键变量在于传导时滞——报告明确指出，原材料价格波动需要4-6个月才能反映到这些公司的损益表中。\n\n这意味着什么？假设当前油价下跌趋势能够维持，那么对2027财年（日本财年通常从4月开始）的成本压力缓解将是实质性的。但市场往往只关注即期的油价变动，而忽略了利润表反映的滞后性。这恰恰为投资者提供了一个时间窗口：在油价下行趋势确立后，个人护理公司的盈利预期存在上修空间，而这个上修尚未被充分定价。\n\n更重要的是，Unicharm在中东地区有直接业务敞口。局势缓和不仅降低其原材料成本，还消除了其\n\n[... middle omitted ...]\n\n们会分享完整的研报解读、原始图表，以及更深入的行业交叉分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东缓和对日股的影响拆解\n\n中东局势暂缓，影响几何？\n\n6月17日美伊签署谅解备忘录，中东紧张局势阶段性缓和。如果后续不恶化，对日本几家消费品公司的业绩影响值得细看。\n\n1️⃣ 个人护理板块受益最直接\n- 尤妮佳、花王、狮王的成本结构受原油影响较大，研报测算油价每变动1美元/桶，对尤妮佳和花王的核心营业利润影响约500-600百万日元，对狮王影响约100-200百万日元\n- 成本传导周期约4-6个月，近期油价回落预计缓解FY2027的成本压力\n- 尤妮佳中东业务销售环境也有望改善\n- 但需警惕：FY2026下半年可能因家庭囤货需求回落、高价原料库存承压\n\n2️⃣ 化妆品板块影响有限\n- 包装材料和部分原料的供应短缺风险降低，但由于成本占比低，市场此前关注度本就不高\n- 更值得关注的是：消费者信心回升和游客增加带来的销售环境改善\n\n3️⃣ 纸浆包装板块情况复杂\n- 油价下跌确实缓解成本压力，理论上利好王子制纸、日本制纸、大王制纸、联果等股价\n- 但矛盾点：主要纸企原计划7-8月提价（尤其印刷纸），油价急跌可能导致议价难度加大，成本转嫁机制建立可能延迟\n- 油价每变动1美元/桶，对王子制纸和日本制纸影响约300百\n\n[... middle omitted ...]\n\nctor.\n\n- Personal care: The manufacturing cost structures of Unicharm, Kao, and Lion are affected by crude oil market conditions to an extent. We estimate that it will take 4-6 months for inpu\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 20 Jun 2026 12:07 AM JST\n\nDisseminated 20 Jun 2026 12:07 AM JST"
  },
  {
    "id": "R004",
    "title": "JPM：日本制药板块正在经历的不是回调，而是结构性出清",
    "digest": "[wechat_article.md]\n# JPM：日本制药板块正在经历的不是回调，而是结构性出清\n\n2026年6月，日本股市在AI和半导体板块的带动下创下历史新高，日经225指数在6月19日收于纪录高位。但如果你只看制药板块，会以为自己身处另一个市场。JPM最新一周的日本制药行业周报揭示了一个令人不安但必须正视的事实：日本制药板块正在经历的不是短期回调，而是一场由资金结构、研发风险和估值体系共同驱动的出清过程。\n\n这份报告的核心判断是：日本制药板块的疲软并非周期性波动，而是市场正在用AI时代的估值逻辑重新定价整个行业。那些无法在2026年下半年拿出明确催化剂的公司，将继续被市场抛弃。但报告同时指出，2026年下半年的催化剂事件可能成为板块反转的关键节点。问题在于，这些催化剂是否足够强大，足以逆转当前的结构性压力。\n\n以下是我们从这份报告中提炼的五个关键洞察，以及一个尚未被充分讨论的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日本制药板块正在经历的不是行业问题，而是资金流向的结构性挤压\n\nJPM的数据显示，在截至6月19日的一周内，制药板块仅上涨0.8%，而同期TOPIX指数上涨4.2%。拉长到一个月维度，制药板块下跌5.6%，而TOPIX上涨5.0%。更令人警醒的是，在三个月和六个月的时间跨度内，制药板块分别下跌11.1%和4.2%，而TOPIX同期上涨12.1%和19.5%。\n\n这不是某个公司的业绩问题，这是整个板块在资金争夺战中的系统性溃败。日本股市的上涨高度集中于AI和半导体相关板块，非铁金属、电子设备、玻璃与陶瓷产品等板块在过去三个月分别上涨28.0%、44.0%和38.7%。相比之下，制药板块在行业分类中排名倒数。\n\n这意味着什么？日本制药公司当前的估值压力，很大程度上是“被动的”——不是因为基本面恶化，而是因为市场可配置资金\n\n[... middle omitted ...]\n\n正想在这个板块中寻找机会的投资者来说，可能是最有价值的部分。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本医药板块，下半年等风来\n\n📉 短期还在休整\n🔬 下半年催化剂值得盯\n\n某外资投行最新周报显示，日本医药板块上周仅涨0.8%，远跑输大盘（+4.2%）。资金全在AI和半导体，医药被冷落。\n\n但别急着划走，几个关键点值得关注：\n\n1️⃣ **短期疲弱，但下半年有戏**\n板块过去1个月跌5.6%，3个月跌11.1%，确实惨。研报认为短期还会偏弱，但看好4-6月财报季和下半年催化剂（10月学术会议等）带动股价回升。\n\n2️⃣ **Kyowa Kirin：坏消息出尽？**\n虽然rocatinlimab开发终止导致中长期不确定，但研报认为短期利空已消化。重点看KHK4951（湿性AMD）的2期数据，预计10月学术会议公布。\n\n3️⃣ **Sumitomo Pharma：短期最强**\n上周涨6.9%领跑板块。6月16日在EHA大会公布了nuvisertib和enzomenib最新数据，值得关注。\n\n4️⃣ **其他动态速览**\n- Chugai：6月17日举办Elevidys（日本首个DMD基因疗法）说明会；6月19日提交sparsentan（IgA肾病）上市申请\n- Santen：6月19日获批Rhopressa滴眼\n\n[... middle omitted ...]\n\nd Kyowa Kirin outperformed TOPIX. In particular, Kyowa Kirin was the sector's best performer over the past month. Despite the uncertain medium- to long-term outlook after rocatinlimab developm\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 20 Jun 2026 01:22 AM JST\n\nDisseminated 20 Jun 2026 01:23 AM JST"
  },
  {
    "id": "R005",
    "title": "GS：618大促揭示中国美妆市场真正的分水岭，不是国货与外资，而是高端与大众",
    "digest": "[wechat_article.md]\n# GS：618大促揭示中国美妆市场真正的分水岭，不是国货与外资，而是高端与大众\n\n市场对2026年618美妆大促的普遍解读，往往落入“国货崛起”或“外资反攻”的二元叙事。但GS这份最新发布的618抖音渠道脉冲检查报告，揭示了一个更深层、也更值得产业决策者关注的信号：真正的分水岭不在于品牌国籍，而在于价格带。高端化正在从趋势变为结构性力量，而这一力量的受益者，并非所有高端品牌。\n\n这份报告的数据窗口覆盖2026年5月1日至6月18日，聚焦抖音平台。抖音作为当前中国美妆线上增长最快的渠道，其表现往往领先于天猫和京东，成为品牌战略调整的先行指标。GS的追踪数据显示，抖音美妆Top 500品牌整体GMV同比增长约35%，但这一数字背后，是极度分化的格局：头部50个品牌增速高达约40%，而排名100名之后的品牌增速已回落至20%左右。市场正在加速集中，而集中的方向，是高端。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 外资高端品牌在抖音的“反攻”并非全面胜利，而是集团内部资源向高利润线集中\n\nGS数据显示，在抖音Top 500品牌中，外资品牌在各个价格带的完成率普遍高于国产品牌，平均完成率约140%，而国产品牌约110%。但“外资”这个标签过于笼统。真正驱动外资整体表现的，是雅诗兰黛集团和欧莱雅集团旗下高端线的强势。\n\n雅诗兰黛集团在抖音的2026年5月1日至6月18日GMV同比增长56%，其中雅诗兰黛主品牌增长65%，海蓝之谜增长54%，两者完成率分别高达167%和154%。欧莱雅集团整体增长33%，但驱动来自修丽可（增长89%，完成率190%）和YSL（增长74%，完成率176%），而大众品牌巴黎欧莱雅仅增长7%，美宝莲甚至下滑7%。\n\n这意味着什么？外资巨头在抖音的增长，并非“全线复苏”，而是集团战略性地将资源、\n\n[... middle omitted ...]\n\n我们会在社群中分享完整的研报原始图表和专家电话会的核心纪要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618美妆战报：抖音谁在领跑？\n\n**高端国货逆袭**\n\n大牌加速，MGP反弹超50%\n\n618刚结束，抖音美妆数据出来了。整体top500品牌增速中高双位数，头部集中度在提升——top50品牌增速约40%，100名开外的品牌只有20%+。\n\n几个关键趋势👇\n\n**1/ 高端品牌继续领跑**\n奢侈/高端线在抖音表现最猛。5月增速还是20-30%，6月直接拉到40-50%+。中高端/大众线反而从40%+放缓到20%左右。\n\n**2/ 外资>国货，但有个例外**\n外资整体完成率约140%，国货约110%。但在高端线，国货反而跑赢了——毛戈平6月1-18日增速91%，全周期完成率150%。研报认为这是品牌主动控节奏的结果，类似双十一的打法。\n\n**3/ 具体品牌亮点**\n- 林清轩：抖音全周期增速188%，完成率356%（但基数较低）\n- 毛戈平：全周期增速54%，6月加速到91%\n- 巨子生物：全周期增速15%，6月追到44%\n- 珀莱雅：全周期24%，但6月下滑5%\n- 华熙/上美：承压，完成率77%/63%\n\n**4/ 外资品牌**\n- 雅诗兰黛集团：全周期增速56%，6月加速到75%，海蓝之谜/雅诗兰黛完成\n\n[... middle omitted ...]\n\ncing segment (refer to Exhibit 3 for our definition for different pricing segment): Within top 500 brands, we see global brands tracking above local brands, in majority of the pricing segment \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Energy flows through the Strait of Hormuz have yet to revive... Estimated oil exports through Strait of Hormuz, based on reported vessel count"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...though some Asian economies have secured imports from other sources"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Oil prices are down sharply over the past month"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Refined product prices are also down, though they remain notably above pre-war levels"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Our base case oil forecast now has Brent at \\$80/bbl in Q4 Monthly Brent oil price"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Median headline CPI inflation up to 3% regionally"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Core inflation generally has been well-behaved so far"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Inflation is generally in line with, or above, policy targets across the region Inflation vs. central bank targets, Asia-Pacific (higher core CPI inflation relative to target)"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China CPI inflation"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China CPI momentum"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Exhibit 13",
    "context": "Exhibit 13: China CPI contribution breakdown"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Exhibit 14",
    "context": "Exhibit 14: China PPI and Import Price Index"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Exhibit 15",
    "context": "Exhibit 15: China wage growth"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Exhibit 16",
    "context": "Exhibit 16: China retail energy prices China weighted average fuel price"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Korea CPI inflation"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Korea CPI momentum"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Korea CPI contribution breakdown"
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Korea PPI and Import Price Index"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Korea wage growth"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Korea retail energy prices"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Taiwan CPI inflation"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Taiwan CPI momentum"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Taiwan CPI contribution breakdown"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Taiwan PPI and Import Price Index"
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Taiwan wage growth"
  },
  {
    "figure_id": "F026",
    "report_id": "R001",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Taiwan retail energy prices"
  },
  {
    "figure_id": "F027",
    "report_id": "R001",
    "label": "Exhibit 29",
    "context": "Exhibit 29: India CPI inflation"
  },
  {
    "figure_id": "F028",
    "report_id": "R001",
    "label": "Exhibit 30",
    "context": "Exhibit 30: India CPI momentum"
  },
  {
    "figure_id": "F029",
    "report_id": "R001",
    "label": "Exhibit 31",
    "context": "Exhibit 31: India CPI contribution breakdown"
  },
  {
    "figure_id": "F030",
    "report_id": "R001",
    "label": "Exhibit 32",
    "context": "Exhibit 32: India Wholesale Price Index Percent change, yoy"
  },
  {
    "figure_id": "F031",
    "report_id": "R001",
    "label": "Exhibit 33",
    "context": "Exhibit 33: India retail energy prices"
  },
  {
    "figure_id": "F032",
    "report_id": "R001",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Indonesia CPI inflation"
  },
  {
    "figure_id": "F033",
    "report_id": "R001",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Indonesia CPI momentum"
  },
  {
    "figure_id": "F034",
    "report_id": "R001",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Indonesia CPI contribution breakdown Contribution to year-over-year CPI Inflation"
  },
  {
    "figure_id": "F035",
    "report_id": "R001",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Indonesia PPI and Import Price Index"
  },
  {
    "figure_id": "F036",
    "report_id": "R001",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Indonesia wage growth Indonesia average net monthly wage*"
  },
  {
    "figure_id": "F037",
    "report_id": "R001",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Indonesia retail energy prices"
  },
  {
    "figure_id": "F038",
    "report_id": "R001",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Malaysia CPI inflation"
  },
  {
    "figure_id": "F039",
    "report_id": "R001",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Malaysia CPI momentum"
  },
  {
    "figure_id": "F040",
    "report_id": "R001",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Malaysia PPI and Import Price Index"
  },
  {
    "figure_id": "F041",
    "report_id": "R001",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Malaysia wage growth"
  },
  {
    "figure_id": "F042",
    "report_id": "R001",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Malaysia retail energy prices"
  },
  {
    "figure_id": "F043",
    "report_id": "R001",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Philippines CPI inflation"
  },
  {
    "figure_id": "F044",
    "report_id": "R001",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Philippines CPI momentum"
  },
  {
    "figure_id": "F045",
    "report_id": "R001",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Philippines CPI contribution breakdown"
  },
  {
    "figure_id": "F046",
    "report_id": "R001",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Philippines Manufacturing PPI and Import Price Index"
  },
  {
    "figure_id": "F047",
    "report_id": "R001",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Philippines retail energy prices"
  },
  {
    "figure_id": "F048",
    "report_id": "R001",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Thailand CPI inflation"
  },
  {
    "figure_id": "F049",
    "report_id": "R001",
    "label": "Exhibit 51",
    "context": "Exhibit 51: Thailand CPI momentum"
  },
  {
    "figure_id": "F050",
    "report_id": "R001",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Thailand CPI contribution breakdown"
  },
  {
    "figure_id": "F051",
    "report_id": "R001",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Thailand PPI and Import Price Index"
  },
  {
    "figure_id": "F052",
    "report_id": "R001",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Thailand wage growth Thailand average monthly wages per person"
  },
  {
    "figure_id": "F053",
    "report_id": "R001",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Thailand retail energy prices"
  },
  {
    "figure_id": "F054",
    "report_id": "R001",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Vietnam CPI inflation"
  },
  {
    "figure_id": "F055",
    "report_id": "R001",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Vietnam CPI momentum"
  },
  {
    "figure_id": "F056",
    "report_id": "R001",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Vietnam PPI and Import Price Index"
  },
  {
    "figure_id": "F057",
    "report_id": "R001",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Vietnam wage growth Vietnam average monthly earnings"
  },
  {
    "figure_id": "F058",
    "report_id": "R001",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Vietnam retail energy prices"
  },
  {
    "figure_id": "F059",
    "report_id": "R001",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Japan CPI inflation"
  },
  {
    "figure_id": "F060",
    "report_id": "R001",
    "label": "Exhibit 62",
    "context": "Exhibit 62: Japan CPI momentum"
  },
  {
    "figure_id": "F061",
    "report_id": "R001",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Japan PPI and Import Price Index"
  },
  {
    "figure_id": "F062",
    "report_id": "R001",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Japan wage growth"
  },
  {
    "figure_id": "F063",
    "report_id": "R001",
    "label": "Exhibit 65",
    "context": "Exhibit 65: Japan shunto wage agreements"
  },
  {
    "figure_id": "F064",
    "report_id": "R001",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Japan retail energy prices"
  },
  {
    "figure_id": "F065",
    "report_id": "R001",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Hong Kong CPI inflation"
  },
  {
    "figure_id": "F066",
    "report_id": "R001",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Hong Kong CPI momentum"
  },
  {
    "figure_id": "F067",
    "report_id": "R001",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Hong Kong PPI and Import Price Index"
  },
  {
    "figure_id": "F068",
    "report_id": "R001",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Hong Kong wage growth Hong Kong average employment earnings"
  },
  {
    "figure_id": "F069",
    "report_id": "R001",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Hong Kong retail energy prices"
  },
  {
    "figure_id": "F070",
    "report_id": "R001",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Singapore CPI inflation \\*The forecast is for headline CPI inflation \\*\\*CPI excluding accommodation and private road transportation costs Exhibit 74: Singapore PPI and Import Price Index"
  },
  {
    "figure_id": "F071",
    "report_id": "R001",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Singapore CPI inflation \\*The forecast is for headline CPI inflation \\*\\*CPI excluding accommodation and private road transportation costs Exhibit 74: Singapore PPI and Import Price Index"
  },
  {
    "figure_id": "F072",
    "report_id": "R001",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Singapore retail energy prices"
  },
  {
    "figure_id": "F073",
    "report_id": "R001",
    "label": "Exhibit 73",
    "context": "Exhibit 73: Singapore CPI momentum"
  },
  {
    "figure_id": "F074",
    "report_id": "R001",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Singapore wage growth"
  },
  {
    "figure_id": "F075",
    "report_id": "R001",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Australia CPI inflation"
  },
  {
    "figure_id": "F076",
    "report_id": "R001",
    "label": "Exhibit 78",
    "context": "Exhibit 78: Australia CPI momentum"
  },
  {
    "figure_id": "F077",
    "report_id": "R001",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Australia Finished Goods PPI and Import Price Index"
  },
  {
    "figure_id": "F078",
    "report_id": "R001",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Australia wage growth"
  },
  {
    "figure_id": "F079",
    "report_id": "R001",
    "label": "Exhibit 81",
    "context": "Exhibit 81: Australia retail energy prices"
  },
  {
    "figure_id": "F080",
    "report_id": "R001",
    "label": "Exhibit 82",
    "context": "Exhibit 82: New Zealand CPI inflation"
  },
  {
    "figure_id": "F081",
    "report_id": "R001",
    "label": "Exhibit 83",
    "context": "Exhibit 83: New Zealand CPI momentum"
  },
  {
    "figure_id": "F082",
    "report_id": "R001",
    "label": "Exhibit 84",
    "context": "Exhibit 84: New Zealand Output Prices PPI and Import Price Index"
  },
  {
    "figure_id": "F083",
    "report_id": "R001",
    "label": "Exhibit 85",
    "context": "Exhibit 85: New Zealand wage growth New Zealand salary and wage rates"
  },
  {
    "figure_id": "F084",
    "report_id": "R001",
    "label": "Exhibit 86",
    "context": "Exhibit 86: New Zealand retail energy prices"
  },
  {
    "figure_id": "F085",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Gold has reconnected with real yields"
  },
  {
    "figure_id": "F086",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: On average, gold has rallied 0.84% in the 1 month after a 25bp Fed hike versus 3.93% after a cut % Change in Gold 1m after US Fed Hike/Cut"
  },
  {
    "figure_id": "F087",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Gold is less effective as a safe haven in supply shocks than demand shocks Annualised Performance Post Crisis (CAGR)"
  },
  {
    "figure_id": "F088",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The market pricing for Fed rate hikes has increased dramatically"
  },
  {
    "figure_id": "F089",
    "report_id": "R002",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ETFs have been selling some gold with the Fed on hold"
  },
  {
    "figure_id": "F090",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: And gold has been performing better on de-escalation days Average Daily Performance Since Ceasefire On Market Events"
  },
  {
    "figure_id": "F091",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Real yields are still well above February levels"
  },
  {
    "figure_id": "F092",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: ETFs tend to be most active buying gold during rate cutting"
  },
  {
    "figure_id": "F093",
    "report_id": "R002",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Gold's performance after rate hikes is quite mixed"
  },
  {
    "figure_id": "F094",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 10: On average, gold has rallied 0.84% in the 1 month after a 25bp Fed hike % Change in Gold 1m after US Fed Hike/Cut"
  },
  {
    "figure_id": "F095",
    "report_id": "R002",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China's gold purchases have accelerated with the pullback China Central Bank Monthly Gold Purchases (tonnes)"
  },
  {
    "figure_id": "F096",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 12: India's imports moderated, with the gold import duty hiked during May to discourage purchases India Gold Imports versus Gold Price"
  },
  {
    "figure_id": "F097",
    "report_id": "R004",
    "label": "Figure 12",
    "context": "Figure 12: New Cases of COVID-19 in Japan (Fixed Point Observation)"
  },
  {
    "figure_id": "F098",
    "report_id": "R004",
    "label": "Figure 13",
    "context": "Figure 13: Cases of Influenza in Japan (Fixed Point Observation)"
  },
  {
    "figure_id": "F099",
    "report_id": "R004",
    "label": "Figure 14",
    "context": "Figure 14: List of TRx Figure 15: Takeda Pharmaceutical (4502) Entyvio IV Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F100",
    "report_id": "R004",
    "label": "Figure 16",
    "context": "Figure 16: Takeda Pharmaceutical (4502) Entyvio Pen Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F101",
    "report_id": "R004",
    "label": "Figure 17",
    "context": "Figure 17: Takeda Pharmaceutical (4502) TAKHZYRO Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F102",
    "report_id": "R004",
    "label": "Figure 19",
    "context": "Figure 19: Astellas Pharma (4503) XTANDI and Competitors' Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Figure 21",
    "context": "Figure 21: Astellas Pharma (4503) Competitor of VEOZAH Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Figure 18",
    "context": "Figure 18: Takeda Pharmaceutical (4502) VYVANSE Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Figure 20",
    "context": "Figure 20: Astellas Pharma (4503) Myrbetriq and Sumitomo Pharma (4506) Gemtesa Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Figure 22",
    "context": "Figure 22: Astellas Pharma (4503) Competitor of IZERVAY Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Figure 23",
    "context": "Figure 23: Chugai Pharmaceutical (4519) Competitor of Actemra SC Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Figure 25",
    "context": "Figure 25: Chugai Pharmaceutical (4519) Nemluvio and Its Competitors Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Figure 27",
    "context": "Figure 27: Chugai Pharmaceutical (4519) Hemlibra and Its Competitor Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "Figure 24",
    "context": "Figure 24: Chugai Pharmaceutical (4519) Competitor of Actemra IV Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F111",
    "report_id": "R004",
    "label": "Figure 26",
    "context": "Figure 26: Competitor of Nemluvio, Dupixent Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F112",
    "report_id": "R004",
    "label": "Figure 28",
    "context": "Figure 28: Chugai Pharmaceutical (4519) Foundayo and Its Competitor Number of US Prescriptions (TRx) (1)"
  },
  {
    "figure_id": "F113",
    "report_id": "R004",
    "label": "Figure 29",
    "context": "Figure 29: Chugai Pharmaceutical (4519) Foundayo and Its Competitor Number of US Prescriptions (TRx) (2)"
  },
  {
    "figure_id": "F114",
    "report_id": "R004",
    "label": "Figure 31",
    "context": "Figure 31: Daiichi Sankyo (4568) American Regent Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F115",
    "report_id": "R004",
    "label": "Figure 30",
    "context": "Figure 30: Eisai (4523) Lenvima Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F116",
    "report_id": "R004",
    "label": "Figure 32",
    "context": "Figure 32: Otsuka Holdings (4578) Long-Acting Injections and Competitors Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F117",
    "report_id": "R004",
    "label": "Figure 33",
    "context": "Figure 33: Otsuka Holdings (4578) and Sumitomo Pharma (4506) Main Atypical Antipsychotics Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F118",
    "report_id": "R004",
    "label": "Figure 35",
    "context": "Figure 35: Otsuka Holdings (4578) Samsca/Jynarque Generic Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F119",
    "report_id": "R004",
    "label": "Figure 34",
    "context": "Figure 34: Otsuka Holdings (4578) CDK4/6 Inhibitor and Competitors Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F120",
    "report_id": "R004",
    "label": "Figure 36",
    "context": "Figure 36: Otsuka Holdings (4578) Voyxact Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F121",
    "report_id": "R004",
    "label": "Figure 37",
    "context": "Figure 37: Otsuka Holdings (4578) Voyxact Accumulated Number of US Prescriptions"
  },
  {
    "figure_id": "F122",
    "report_id": "R004",
    "label": "Figure 39",
    "context": "Figure 39: Kyowa Kirin (4151) Komzifti and Competitor's Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F123",
    "report_id": "R004",
    "label": "Figure 41",
    "context": "Figure 41: Sumitomo Pharma (4506) ORGOVYX Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F124",
    "report_id": "R004",
    "label": "Figure 38",
    "context": "Figure 38: Kyowa Kirin (4151) FASENRA Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F125",
    "report_id": "R004",
    "label": "Figure 40",
    "context": "Figure 40: Sumitomo Pharma (4506) Myfembree and Competitors' Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F126",
    "report_id": "R004",
    "label": "Figure 42",
    "context": "Figure 42: Shionogi & Co. (4507) Xofluza Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F127",
    "report_id": "R004",
    "label": "Figure 43",
    "context": "Figure 43: Shionogi & Co. (4507) HIV Drugs (1) Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F128",
    "report_id": "R004",
    "label": "Figure 45",
    "context": "Figure 45: Nippon Shinyaku (4516) Uptravi Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F129",
    "report_id": "R004",
    "label": "Figure 44",
    "context": "Figure 44: Shionogi & Co. (4507) HIV Drugs (2) Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F130",
    "report_id": "R004",
    "label": "Figure 46",
    "context": "Figure 46: Psoriasis Treatment Number of US Prescriptions (TRx)"
  },
  {
    "figure_id": "F131",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Tmall+Douyin+JD: Growth of MNC brands has outperformed local brands since 4Q25 Cosmetics Monthly Online GMV YoY by Brand Positioning"
  },
  {
    "figure_id": "F132",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Tmall+Douyin+JD: Growth of Domestic Premium brands (i.e. Mao Geping) has outperformed MNC peers Cosmetics Monthly Online GMV YoY by Brand Positioning"
  },
  {
    "figure_id": "F133",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Tmall+Douyin+JD: Growth of MNC Mid-to-high end brands has outperformed local peers in 2026 Cosmetics Monthly Online GMV YoY by Brand Positioning"
  },
  {
    "figure_id": "F134",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Tmall+Douyin+JD: In mass brands, local has outperformed MNC growth Cosmetics Monthly Online GMV YoY by Brand Positioning Cosmetics Monthly Online GMV YoY by Brand Positioning"
  }
]