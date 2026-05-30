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
    "title": "市场真正低估的不是油价，而是非石油商品的供给断点",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是油价，而是非石油商品的供给断点\n\n当霍尔木兹海峡的通行量下降超过90%，全球投资者习惯性地将目光聚焦于油价。这可以理解。原油是全球化程度最高的商品之一，价格信号清晰，库存数据透明，历史经验丰富。但这份某外资投行最新发布的全球经济学报告揭示了一个更具颠覆性的判断：**真正可能引发超预期增长冲击的，不是石油，而是那些市场更小、供应链更区域化、几乎没有替代弹性的非石油商品。**\n\n石油市场的逻辑是“价格出清”。价格上涨到一定程度，需求自然萎缩，市场重新平衡。但非石油商品——从化肥到氦气，从硫磺到甲醇——面临的风险是“数量出清”。当供给被切断，市场无法通过价格找到替代，生产链条上的企业会直接面临“无料可用”的局面。这是两种完全不同的冲击机制，后者对实体经济的破坏力，可能远超当前资产价格所反映的水平。\n\n报告的核心贡献在于，它提供了一套量化框架，将这种“供给断点”转化为可比较的GDP冲击数字。而其中最值得关注的结论是：在极端假设下，非石油商品供给中断对全球GDP的拖累可能达到1.3%，但经过更现实的假设调整后，这个数字会收窄至0.4%到0.5%。这个落差本身，就是最大的不确定性来源。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 石油冲击的“价格缓冲垫”正在变薄，但尚未破裂\n\n报告首先确认了一个市场已有共识的判断：石油供给冲击仍在可控范围内。原油价格自冲突爆发以来上涨了约50%，汽油、柴油和航空燃油的涨幅更大。按照该投行标准的经验法则，能源价格上涨对全球GDP的拖累约为0.6个百分点，在严重不利情景下可升至1.1个百分点。\n\n但报告真正有洞察力的地方在于，它指出了“价格缓冲垫”正在变薄。OECD商业原油库存虽然仍高于页岩油时代之前的平均水平，但成品油库存已经明显偏低。柴油的情况尤其值得警惕——由于其需\n\n[... middle omitted ...]\n\n内分享报告的原始图表、数据文件，以及基于最新数据的情景更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东供应链断裂，全球增长怎么看\n\n全球经济的“压力测试”\n\n最近中东局势持续紧张，霍尔木兹海峡的航运量暴跌超90%。虽然全球经济目前还算扛得住，但供应链短缺的累积效应可能随时引爆。今天拆解一份外资投行的深度研报，看看最坏情况下，全球增长会受多大冲击。\n\n1/ 石油：价格机制在起作用\n原油价格已飙升约50%，精炼产品（汽油、柴油、航空燃料）涨幅更大。投行模型显示，油价上涨本身会通过“需求破坏”来平衡市场——价格高了，自然有人少用。按基准情景，这大概拖累全球GDP 0.5个百分点。但若供应持续受限，冲击可能翻倍。\n\n2/ 非石油商品：真正的“断供”风险\n中东非石油商品出口仅占全球GDP的1.3%，但某些品类依赖度极高：\n- 化肥：占全球进口32%\n- 天然气：14.5%\n- 石化产品：基础化学品价格已涨超60%\n- 工业气体：氦气价格翻倍\n\n如果这些供应链“硬断”，按极端模型（即每个环节都缺一不可），全球GDP可能直接损失1.3%。\n\n3/ 为什么实际冲击可能更小？\n投行给出了三个缓冲机制：\n- 剔除占比极小的投入后，GDP冲击会显著下降\n- 企业会把稀缺资源从低附加值用途转向高附加值领域\n- 不同投入之间存在替\n\n[... middle omitted ...]\n\ntinue to expect that most of the demand destruction required to clear markets will be driven by prices, which have risen sharply for highly exposed products. This is especially true for oil, w\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "城镇化2.0才是真正值得关注的长期结构性变量，而非短期政策脉冲",
    "digest": "[wechat_article.md]\n# 城镇化2.0才是真正值得关注的长期结构性变量，而非短期政策脉冲\n\n市场当前对宏观叙事的焦点，大多停留在月度财政支出的快慢、专项债发行的节奏、以及中美欧关税博弈的短期起伏上。这些当然重要，但它们回答的是“下个季度会怎样”的问题。而一份由某外资投行最新发布的宏观追踪报告，揭示了一个更深层的判断：真正可能在未来三到五年重塑中国经济增长逻辑的，不是任何一轮刺激的规模，而是一个正在悄然提速的制度性安排——以常住地登记为基础提供基本公共服务。\n\n这份报告的核心洞察可以概括为一句话：中国正在从“以地为本”的城镇化，转向“以人为本”的城镇化。这个转变的起点，是2025年5月25日国务院发布的《关于促进以常住地登记提供基本公共服务的意见》。它看起来像一份常规的民生政策文件，但放在更长的时间轴和更大的分析框架下，它可能是中国消费率结构性提升、内需市场真正做大的制度基石。\n\n以下是我们基于这份报告，围绕这一主判断展开的五个层次推演。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 过去二十年城镇化的真正短板，不在户籍率，而在公共服务覆盖\n\n中国常住人口城镇化率在2024年已达到67%，但户籍人口城镇化率长期滞后约20个百分点。这20个百分点的差距，对应的正是约1.7亿在城市工作生活、却无法平等享受教育、医疗、住房保障的农民工及其家庭。\n\n报告引用了一张对比图：户籍城镇化率与常住城镇化率的差距在过去十年几乎没有收窄。这意味着，大量劳动力虽然在城市贡献了GDP，但其消费行为仍然带有“预防性储蓄”特征——因为他们不确定子女能否在城市入学，不确定自己能否纳入城市社保，不确定生病时能否获得同等质量的医疗资源。\n\n报告明确指出，这一群体消费潜力的释放，正是此次政策设计的目标所在。这不仅仅是社会公平议题，更是一个宏观经济结构议题。当1.7亿人的预\n\n[... middle omitted ...]\n\n过程感兴趣，欢迎加入，一起把这份报告的未解问题继续拆解下去。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n城市化的下一步：公共服务按常住人口覆盖\n\n**城市化2.0来了**\n\n公共服务不再只看户口，常住人口也能享受\n\n---\n\n最近某外资投行出了一份中国宏观跟踪报告，核心讲了三个变化方向，我帮你拆成能理解的大白话👇\n\n**1️⃣ 城市化2.0：从“要地”到“要人”**\n\n5月25日国务院发文，推动基本公共服务按常住人口提供。核心动作：\n\n- 加强随迁子女教育权利\n- 把非户籍家庭纳入公租房覆盖\n- 完善社保参保体系\n- 强化医疗保障和就业帮扶\n\n这和过去不一样。以前城市化是为了把农村劳动力拉进城市搞制造和建设，现在是把城市化当成“扩大内需”的杠杆——通过给1.7亿进城务工人员及其家庭提供公共服务，降低他们的预防性储蓄，释放消费潜力。\n\n财政数据也印证了这一点：今年财政支出中，民生相关领域的占比在持续提升。\n\n**2️⃣ 中欧贸易摩擦在升级**\n\n中国对欧盟出口增长和贸易顺差扩大，正在加剧紧张关系。欧盟委员会5月29日要讨论针对中国的新贸易政策，可能出台新的限制措施。\n\n不过报告认为谈判空间还在。原因：\n\n- 欧盟商会在华企业约25%正在把更多生产环节转移到中国\n- 中国商务部长6月底计划访问布鲁塞尔\n- 中美关系\n\n[... middle omitted ...]\n\n, 25 May). The key tasks are to strengthen education rights for migrant workers' children, include non-hukou households within the coverage of public rental housing, improve the system for enr\n\n[... middle omitted ...]\n\nst, Mexico\nJose Carlos Sanchez +52 55 5721 5623\njose.c.sanchez@hsbc.com.mx\n\nAllison Buck +1 212 525 4119\nallison.buck@us.hsbc.com\n\nHead of Brazil Economics Research\nDaniel Lavarda +55 11 2802 2640\ndaniel.lavarda@hsbc.com"
  },
  {
    "id": "R003",
    "title": "台湾市场的真正风险不在于基本面，而在于定价已完全透支了未来",
    "digest": "[wechat_article.md]\n# 台湾市场的真正风险不在于基本面，而在于定价已完全透支了未来\n\n过去一年，亚洲投资者几乎都在做同一件事：加仓台湾。\n\n这并非没有道理。台湾股票在MSCI新兴市场指数中的权重已升至约25%，在MSCI亚洲（除日本）指数中达到28%。台积电一家公司就贡献了14%的指数权重。全球新兴市场基金对台湾的平均配置已达到22.3%，首次超过中国。今年4月以来，台湾吸引了160亿美元的海外资金流入，创下亚洲（除日本外）的最高纪录。\n\n但某外资投行最新发布的亚洲量化策略报告提出了一个值得认真对待的判断：台湾市场正接近一个转折点。不是因为基本面出了问题，而是因为市场已经把所有的好消息都定价进去了——甚至可能更多。\n\n这份报告的核心信号是：盈利预期处于历史高位，估值处于历史极值，股权风险溢价处于历史低位，集中度风险达到历史峰值，成长股与价值股的分化程度达到十年之最。这些信号叠加在一起，意味着动量驱动的上涨已经变得非常脆弱。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 台湾已成为亚洲最拥挤的交易，资金流向本身构成了反转信号\n\n台湾在区域基准中的权重已达到历史最高水平。MSCI亚洲（除日本）指数中，台湾的权重是中国的1.1倍，是韩国的1.3倍，是印度的2.1倍。亚洲（除日本）基金对台湾的平均配置为22.1%，同样创下纪录。\n\n但真正值得关注的是资金流的节奏。今年3月，台湾市场经历了290亿美元的海外资金净流出。然而进入4月后，资金流向急剧逆转，160亿美元净流入涌回台湾。报告直言，这种“极端流入之后，我们预期海外资金将放缓”。\n\n这意味着什么？从量化视角看，当资金流向从一个极端迅速转向另一个极端时，往往是短期动量即将耗尽的信号。不是因为台湾的基本面变差了，而是因为能够推动市场继续上涨的新增资金正在减少。\n\n基金配置数据也支持这一判断。\n\n[... middle omitted ...]\n\n中受益。我们会在社群中分享完整报告的核心图表和量化模型细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n台湾权重新高，但拐点可能不远了\n\n📈台股已达历史高位\n\n最近某外资投行出了一份亚洲量化策略研报，核心观点很直接：台湾市场在MSCI新兴市场指数和亚洲（除日本）指数中权重都创了新高，分别约25%和28%。但这波上涨主要由盈利驱动而非估值扩张，目前盈利预期、估值、集中度风险都到了历史极值，拐点可能正在靠近。\n\n1️⃣ 权重创新高，资金已极度拥挤\n\n截至2026年4月底，台股在MSCI新兴市场指数中权重约25%，其中台积电一家就占了14%。亚洲（除日本）基金平均配置台湾22.1%，已经超过中国（21.9%）。全球新兴市场基金配置台湾22.3%，也高于中国的20%。今年4月以来，台湾是亚洲（除日本）外资流入最多的市场，达到160亿美元，已经是月度历史新高。研报认为这种极端流入很难持续。\n\n2️⃣ 基本面很强，但可能已完全定价\n\n台湾市场基本面确实扎实：ROIC达11.5%，研发占销售比从十年前的1.7%升至2.7%，未来三年盈利增长预期29%为亚洲最高。但问题在于，这些利好可能已经被市场完全消化。当前台股远期PE达21倍，比长期均值高2.6个标准差；PB达4.5倍，比长期均值高5.2个标准差，都是历史极值。股权风险溢\n\n[... middle omitted ...]\n\nthe fact that the rally was driven more by earnings vs. multiple expansion. However, we believe we are close to an inflection point as the mounting risk from record high earnings expectations,\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R004",
    "title": "日本央行真正担心的不是油价，而是“工资-物价螺旋”的迟到风险",
    "digest": "[wechat_article.md]\n# 日本央行真正担心的不是油价，而是“工资-物价螺旋”的迟到风险\n\n2026年5月27日，日本央行行长植田和男在一次国际会议上的发言，表面是在回顾历史，实则是在为当下货币政策定调。他选择了一个极其独特的分析框架：将本轮油价冲击与1973年第一次石油危机、1979年第二次石油危机进行系统性对比，并重点考察“初始条件”的差异。\n\n这份来自某外资投行的研报，抓住了植田发言中最核心的量化线索：**日本当前的宏观经济环境，比第二次石油危机时更具通胀倾向，而市场对这一点严重定价不足。**\n\n这不是一个关于油价涨跌的短期判断，而是一个关于日本央行政策路径、工资谈判机制与通胀粘性之间结构性关系的深层分析。报告的核心结论是：日本经济正站在一个“类1973年”的岔路口——历史不会简单重复，但押注“通胀很快回落”的风险，可能远高于押注“通胀持续”的风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 上游价格压力已回到石油危机水平，但真正的变量在工资端\n\n研报给出的第一个硬数据就足够警醒：2026年4月，日本国内企业商品价格指数（CGPI）环比上涨2.3%，这是自1980年第二次石油危机以来最大的单月涨幅，且排除了消费税上调的影响。更值得注意的是，化工产品价格创下了1973年第一次石油危机以来的最大涨幅。\n\n但植田和男的分析框架提示我们，只看上游价格是不够的。同样的外部冲击，在不同的“初始条件”下，会导致截然不同的通胀结果。1973年的第一次石油危机之所以引发了工资-物价螺旋，是因为日本经济当时已经处于过热状态，名义工资在冲击前就以15%-20%的速度增长。油价冲击只是火上浇油，将工资增速推至30%的峰值。\n\n而1979年的第二次石油危机之所以相对成功遏制了通胀，是因为日本企业和工会从第一次危机中吸取了教训，通过劳资协调机制抑制了工资\n\n[... middle omitted ...]\n\n完整研报原文、核心图表包，以及每周一次的多资产策略讨论纪要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本正在经历一场“类石油危机”式的通胀压力，但这次结局可能不同。植田和男行长最新讲话里，藏着看懂日本经济走向的关键线索。\n\n通胀压力已到历史级\n\n4月日本国内企业商品价格指数（CGPI）环比上涨2.3%，创1980年第二次石油危机以来最大涨幅（不含消费税上调影响）。化工产品价格涨幅更是1973年第一次石油危机以来最高。上游价格压力，已经来到和当年石油危机相当的水平。\n\n但植田行长提醒：冲击大小相同，结果也可能完全不同。关键在于经济的“初始条件”。\n\n1/ 工资-物价螺旋：短期风险有限，但明年是关键\n\n第一次石油危机时，日本经济已经过热，名义工资年增速15-20%，油价冲击后工资一度飙到30%涨幅，直接引爆螺旋。第二次石油危机时，吸取教训的劳资协调机制压住了工资，螺旋没形成。\n\n现在的情况：\n- 单位劳动力成本增速高于第二次石油危机前\n- 劳动力短缺程度甚至比70年代更严重（日银短观就业DI创历史新低）\n- 但今年春斗（春季工资谈判）已在油价冲击前结束，基础工资大幅上调要等明年\n- 夏季奖金增速预计低于去年\n\n结论：短期工资-物价螺旋风险不高。但如果今年高通胀转化为2027年春斗的强工资要求，高通胀持续的时间可\n\n[... middle omitted ...]\n\nspeech is highly insightful for understanding the current state of Japan's economy. Tensions in the Middle East since March have caused a sharp rise in crude oil prices. In response, Japan's C\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>TeL: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R005",
    "title": "四月财政收缩并非政策转向，而是节奏重置",
    "digest": "[wechat_article.md]\n# 四月财政收缩并非政策转向，而是节奏重置\n\n市场对四月经济数据的反应，大多聚焦在固定资产投资意外转负上。但真正值得追问的不是“投资为什么弱”，而是“钱去了哪里”。某外资投行最新发布的四月财政数据解析给出了一个反直觉的判断：财政收缩本身不是政策立场的改变，而恰恰意味着下半年财政脉冲的衰减幅度可能小于市场此前最悲观的预期。\n\n这份报告的核心洞察可以提炼为一句话：**四月财政数据的“弱”，是节奏问题，不是方向问题。** 一般公共预算支出同比转负至-3.2%，政府性基金支出更是骤降20.8%，财政存款却反常地增加了7390亿元——这笔钱不是消失了，而是被暂时“囤”在了账上。对于关注中国资产定价的投资者而言，这组数据背后隐藏的，是下半年政策支持力度的重新定价。\n\n理解这一点，需要拆解四个层次：财政收缩的结构性原因、土地财政的持续拖累、债券发行节奏的错位，以及这些因素叠加后对下半年GDP增速的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四月支出收缩的核心拖累是基建支出，而非民生支出全面走弱\n\n四月一般公共预算支出的同比收缩，并非所有项目同步下滑。报告明确指出，收缩的主要拖累来自基建类支出，同比降幅高达18.6%，而民生类支出（教育、医疗、城乡社区）仅从一季度的5.3%放缓至1.2%。两者之间的差距，说明财政收缩是有选择性的，而非全局性的紧缩。\n\n这个区分很重要。基建支出的大幅回落，直接对应了四月固定资产投资中基建投资同比-4.5%的收缩。但民生支出的相对韧性表明，政策层在“投资于人”的方向上并未转向。报告提到，尽管基建收缩显著，但教育、医疗和城乡发展等领域的支出仍在增长——只是增速放缓。\n\n这意味着，四月的数据更多反映了项目储备不足和资金拨付节奏的滞后，而非政策目标的调整。对于观察者而言，需要关注的不是“财政是否\n\n[... middle omitted ...]\n\n微信群里继续探讨这些关键变量，以及它们对资产定价的具体含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月财政数据出炉，基建支出意外收缩\n\n**财政节奏在放缓**\n\n**基建支出回落，投资同步降温**\n\n4月一般公共预算支出同比下滑3.2%，结束了1季度2.6%的增长。其中基建类支出大跌18.6%，直接拖累固定资产投资（基础设施FAI同比-4.5%）。民生类支出增速也从1季度的5.3%放缓至1.2%。\n\n政府性基金这边，收入同比-26.4%（土地出让收入跌34.8%），支出同比-20.8%。地产和土地市场低迷的影响仍在持续。\n\n1️⃣ **钱没花出去，财政存款在积累**\n\n4月财政存款增加了7390亿元，是往年季节性增量的2-3倍，总规模达1.2万亿元，创近年新高。说明资金到位后实际支出进度偏慢。\n\n2️⃣ **投资放缓不只因为财政**\n\n除了财政支出节奏，项目储备不足、地方优先化债、政策性金融工具落地慢，都是FAI收缩的原因。\n\n3️⃣ **下半年财政脉冲未必大幅消退**\n\n由于上半年支出进度没有显著前置，下半年政策“后劲”反而可能比预期更稳。如果2季度GDP明显低于4.5-5%的目标区间，年中加码财政支持的概率会上升。\n\n**一句话总结**：4月财政数据确认了支出节奏放缓，但这也意味着下半年政策空间比想象\n\n[... middle omitted ...]\n\nivery may step up. If 2Q materially undershoots $4.5 - 5\\%$ target, interim fiscal support in 2H becomes more likely.\n\nThe surprise April FAI contraction raised questions about whether fiscal \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 27 May 2026 05:58 PM HKT\n\nDisseminated 27 May 2026 06:01 PM HKT"
  },
  {
    "id": "R006",
    "title": "四月消费数据发出一个更值得警惕的信号：政策退潮后的真实需求比想象中更弱",
    "digest": "[wechat_article.md]\n# 四月消费数据发出一个更值得警惕的信号：政策退潮后的真实需求比想象中更弱\n\n理解当前中国消费市场的真实状态，最关键的锚点不是某个月的零售总额增速，而是一组被某外资投行长期跟踪的、经过标准化处理的多维消费活动综合指数。该机构在四月底发布的报告显示，其构建的“五因子消费活动Z-Score”在四月进一步回落。这个信号之所以值得高度关注，不是因为单月数据变差，而是因为它发生在几个关键支撑力同步减弱的窗口期。\n\n四月社会消费品零售总额同比增速降至0.2%，如果剔除疫情冲击的特殊时期，这是一个创纪录的低点。但比数字本身更值得拆解的是背后的结构性因素：以旧换新政策的边际效果正在递减、黄金消费热潮趋于冷却、而就业市场的疲软正在从预期层面传导至实际支出。这份报告的价值不在于告诉我们“消费不好”，而在于通过多因子交叉验证，揭示了当前消费放缓并非短期波动，而是一个由多重力量叠加形成的、具有惯性的下行趋势。\n\n对于产业决策者和资产配置者而言，真正需要回答的问题不是“消费什么时候见底”，而是“在哪些领域、哪些环节，消费下行的二阶效应尚未被充分定价”。这篇研报提供了一个从宏观到微观的推导框架，其核心逻辑值得逐层拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五因子模型的四月信号：不是所有指标都在同步恶化，但综合动量已经转向\n\n这份报告的核心分析工具是一个由五个维度构成的消费活动Z-Score：家庭贷款同比变化、餐饮零售同比变化、商品零售（不含汽车）同比变化、乘用车零售三个月移动平均同比、以及航空客运量三个月移动平均同比。将这五个维度标准化后取平均值，得到的综合指数在四月继续下行。\n\n拆开来看，各因子的表现并非完全一致。航空客运量仍在边际改善，家庭贷款和乘用车销售保持相对稳定。真正拖累综合指数的是餐饮和商品零售的走软。这种“部分稳定、\n\n[... middle omitted ...]\n\n继续讨论。我们会在那里分享更多基于完整研报的拆解和延伸思考。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n消费信号变弱了，四月数据怎么看？\n\n消费在降温\n\n四月消费数据出来了，整体偏弱。餐饮和商品零售都在放缓，只有航空客运量还在小幅改善，居民贷款和乘用车销售算稳住了。\n\n几个关键信号值得留意👇\n\n1️⃣ 零售增速创了历史新低（除疫情时期外）\n四月社会消费品零售总额同比只涨了0.2%，这个数字比预期的要低不少。背后是就业市场的疲软，加上以旧换新政策的刺激效果在减弱。\n\n2️⃣ 黄金热潮在降温\n之前大家抢金饰的热情明显回落，这对整体消费也是个拖累。毕竟金饰在商品零售里占比不小。\n\n3️⃣ 消费后续可能还会走弱\n投行研报里提到几个担忧点：以旧换新的支持力度在减弱、劳动力市场还在承压、出口对消费的溢出效应也有限。短期看不到明显的消费反弹动力。\n\n4️⃣ 五因子消费活动Z-Score继续下滑\n这个综合指标把居民贷款、餐饮零售、商品零售、乘用车销售、航空客运量五个维度合在一起看，四月读数比三月更低了。\n\n总结一下：消费复苏的节奏比预期要慢，就业和收入预期是核心制约因素。后续可以多关注政策端会不会有新的刺激出来。\n\n大家最近消费有感觉到变化吗？欢迎一起聊聊👋\n\n#学习笔记\n\n[source_mineru.md]\n# China\n\n[... middle omitted ...]\n\npillover.\n\nExhibit 1: China Five-factor Consumer Activity Z-Score vs. MSCI China YoY change – Consumer activity declined further in April   \n![](images/a23cdaaae3a624977760fd8d300b04e6d52d6594\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R007",
    "title": "市场真正低估的不是通胀本身，而是通胀指标的偏误",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是通胀本身，而是通胀指标的偏误\n\n美联储主席沃什在最近的确认听证会上，将核心PCE通胀描述为一个“粗略的猜测”——这个来自政策最高决策者的措辞，远比任何数据点都更能说明问题。当被长期视为“锚”的核心指标被其使用者亲自质疑时，资产定价的基准逻辑就需要重新审视。\n\n某外资投行最新发布的研报，并没有停留在讨论“通胀是否回落”这个已经被充分辩论的问题上。它指向了一个更底层、也更危险的变量：我们用来判断通胀趋势的尺子，本身可能已经歪了。报告聚焦于PCE截尾均值通胀这一替代指标，并给出了一个明确的结论——该指标在当前周期中可能系统性低估了真实通胀约48个基点。\n\n这个偏差，对于正在权衡降息时机的市场参与者而言，意味着对政策路径的误判风险正在累积。而更值得关注的，不是偏差本身，是偏差产生的机制尚未被主流定价模型充分吸收。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 截尾均值指标的设计初衷，决定了它在拐点时刻的天然滞后\n\n理解PCE截尾均值通胀，需要回到其构建逻辑。月度通胀数据噪声极大，少数分项的特异性波动可以扭曲整体读数。为了过滤这些“暂时性”噪音，达拉斯联储设计的截尾均值指标，从价格变动的横截面分布中，直接剪掉上下两端波动最大的部分——目前是剪掉下尾24%和上尾31%的分项。\n\n这套机制的优点是减少误报，让政策制定者不会被单月异常数据牵着走。但报告明确指出，这个优点的另一面，是它在新的通胀趋势形成初期反应迟钝。当冲击最初集中在少数分项时，这些分项恰恰因为波动过大而被剪掉，从而让指标错过了趋势启动的第一信号。\n\n这一点在疫情后的通胀飙升中表现得淋漓尽致。2021-2022年，截尾均值通胀的月度年化读数系统性地滞后于报告构建的四种“真实通胀”衡量指标。而核心PCE通胀，尽管被沃什批评为“粗糙的猜测”，却几乎\n\n[... middle omitted ...]\n\n追踪通胀分布的偏态变化，以及它如何影响我们对政策路径的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新通胀指标，可能低估了真实物价\n\n通胀指标，选对了吗？\n\n美联储主席质疑核心PCE通胀指标，抛出一个新选择\n\n最近美联储内部对通胀指标的讨论很有意思。新主席Warsh在听证会上直接说核心PCE是个“粗糙的估算”，转而推荐了“截尾均值通胀”和私营部门的物价指标。\n\n这让我翻出了一份外资投行的研报，专门分析了这个指标靠不靠谱。\n\n1/ 截尾均值通胀是什么？\n\n简单说，就是把每个月物价变动里涨幅最Daiwa跌幅最大的那些项目剔除掉，只看中间部分的走势。目前达拉斯联储的做法是：砍掉涨幅最高的31%和跌幅最大的24%。\n\n4月数据显示，截尾均值PCE同比2.35%，比核心PCE的3.29%低了将近1个百分点。\n\n2/ 问题出在哪？\n\n研报发现一个关键缺陷：这个指标对趋势变化的反应太慢了。\n\n2021-2022年通胀飙升时，截尾均值通胀迟迟没有反应，而核心PCE几乎同步捕捉到了上升趋势。原因是通胀初期冲击往往集中在少数商品领域，而截尾均值刚好把这些敏感项目给剔除了。\n\n更糟的是，研报测算发现，截尾均值通胀可能每年低估真实通胀约48个基点。\n\n3/ 为什么会有偏差？\n\n疫情后商品价格的结构性变化是主因。当通胀分布出现\n\n[... middle omitted ...]\n\nan inflation, whose method of removing outliers might not be optimal due to the recent shift in skewness of the cross-sectional inflation distribution. Trimmed-mean inflation might underestima\n\n[... middle omitted ...]\n\ns available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities International, Inc., US. All rights reserved."
  },
  {
    "id": "R008",
    "title": "ABF 基板短缺不是周期故事，而是AI算力架构重构的结构性拐点",
    "digest": "[wechat_article.md]\n# ABF 基板短缺不是周期故事，而是AI算力架构重构的结构性拐点\n\n市场对ABF基板的认知仍停留在“周期品”框架里——2023年需求下滑15%，2024年回暖25%，2025年增长18%，看起来像是半导体库存周期的又一次波动。但这份投行研报揭示了一个根本不同的图景：ABF基板正在从CPU的“封装耗材”变成AI算力扩张的“刚性约束”。真正重要的不是2025年供需缺口有多大，而是2027年之后供给将系统性落后于需求，且这一缺口无法通过简单的产能扩张来弥补。\n\n报告的核心判断是：ABF市场将在2027年进入全面短缺状态，行业利用率从2025年的80-85%快速攀升至100%以上，且短缺在2028年将进一步加剧。这不是一个“如果”的问题，而是一个“何时”的问题。需求端以22%的CAGR增长，供给端只有12%——这个差距本身就是结论。\n\n对于持有Ibiden、Unimicron或Ajinomoto的投资者，或者正在评估AI基础设施供应链风险的产业决策者，这份报告提供了一个关键的分析框架：短缺不是风险，而是定价权的再分配。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. CPU的“文艺复兴”才是ABF需求爆发的真正推手，GPU只是锦上添花\n\n市场习惯把ABF需求增长归因于AI GPU的爆发，但报告揭示了一个更底层的结构性变化：服务器CPU正在经历一场“文艺复兴”，而这才是ABF需求的核心驱动力。\n\n报告预计，到2030年服务器CPU市场规模将从2025年的330亿美元增长至1370亿美元，对应34%的年复合增长率。驱动因素不是传统的服务器换机周期，而是agentic AI的崛起——AI不再只是GPU加速的计算任务，而是需要CPU处理海量推理调度和智能体协作的复杂系统。报告引用了对SoftBank和Arm的独立分析，认为服务器\n\n[... middle omitted ...]\n\nron和Ajinomoto的投资逻辑，群里会有更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPU复兴引爆ABF基板，2027缺口将至\n\nABF基板：供不应求前夜\n\n服务器CPU出货量4倍增长，基板面积每代扩大24-36%\n\n---\n\n最近读到一份外资投行的ABF基板研报，逻辑很清晰，分享几个关键判断。\n\n**1. 需求端：CPU复兴才是主引擎**\n\n很多人把ABF需求增长全归功于AI芯片，但研报指出，服务器CPU才是ABF基板最大的需求来源，占比约40%。\n\n核心逻辑是Agentic AI的爆发。研报预测，到2030年服务器CPU市场规模将从2025年的330亿美元增长到1370亿美元，出货量达到3000万颗，是2026-2030年间的4倍。\n\n更关键的是，每代CPU的基板面积都在变大。Intel从Emerald Rapids到Granite Rapids面积增加24%，再到Diamond Rapids再增36%。AMD从SP5到SP7也增加12%。AWS的Graviton从第一代16核到第五代192核，核心数增长12倍。\n\n**2. 供需缺口：2027年正式开启**\n\n研报上调了2026/2027年ABF需求预测4%/24%，预计2025-2028年需求复合增速22%。\n\n但供给端呢？主要供应商\n\n[... middle omitted ...]\n\n0e3e89fe70605310564b9f3e1912c3b30379e3c7c115e21afe006.jpg)\n\nJack Lin\n\n+852 2123 2683\n\njack.lin@bernsteinsg.com\n\n![](images/7c45966de1ae0fa04cd6d0036877883afb10e5908b35d007abffeb05cf48970a.jpg)\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "软件投资的下一个分水岭：不是AI能否落地，而是谁在真正提升AI的ROI",
    "digest": "[wechat_article.md]\n# 软件投资的下一个分水岭：不是AI能否落地，而是谁在真正提升AI的ROI\n\n5月28日凌晨，Salesforce和Snowflake几乎同时发布了最新季度财报。市场的反应截然相反：Salesforce盘后下跌近1%，而Snowflake飙升36%。同一时间，Uber的CTO公开表示，公司已暂停部分AI工具的内部使用，理由是“当前的效率提升无法证明成本投入是合理的”。\n\n这三个信号放在一起，指向同一个判断：AI软件投资已经走过了“讲故事”的阶段，进入了“算ROI”的阶段。而真正决定哪些公司能够胜出的，不是它们是否拥抱AI，而是它们能否让自己的产品成为提升AI ROI的关键基础设施。\n\n这份来自某外资投行的研报，核心价值不在于复述Salesforce和Snowflake的财务数据，而在于它提供了一个分析框架：AI对软件行业的替代效应是有选择性的，被替代的将主要是可视化工具等浅层应用，而数据库和记录系统（SoR）这类为AI提供上下文的基础设施，不仅不会被替代，反而会因为AI的普及而变得更加重要。\n\n这个框架的意义不仅在于理解当前的市场波动，更在于重新定义投资者评估软件公司的核心维度。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场反应的巨大反差，揭示的是“预期管理”而非“基本面分化”\n\nSalesforce第一季度营收和每股收益均超出市场共识，但其第二季度指引中，营收预期仅与市场预期持平，每股收益略高于共识。市场给出的反应是股价基本持平。Snowflake则不同，第一季度业绩和第二季度营收指引双双超出预期，盘后股价飙升36%。\n\n表面上，这是业绩兑现程度的差异。但更深层的含义在于：市场对这两家公司的定价逻辑已经发生了根本性变化。\n\nSalesforce作为传统SaaS的代表，其增长故事已经被市场充分定价。即便业绩\n\n[... middle omitted ...]\n\n，以及日本IT服务板块中哪些公司最有可能在这一轮分化中受益。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nSalesforce跌了，Snowflake涨了36%，AI软件的故事还没讲完\n\nAI投资回报率，是下一轮关键\n\nSalesforce和Snowflake财报，冰火两重天\n\n---\n\n最近两家软件巨头财报，市场反应反差巨大。Salesforce盘后跌了0.6%，Snowflake直接跳涨36%。\n\n为什么差别这么大？核心就一句话：市场在重新评估“AI到底能不能帮企业赚钱”。\n\n1️⃣ 两家都在说AI，但市场只信了Snowflake\n\nSalesforce一季度营收和EPS超预期，但二季度指引只是符合预期，市场觉得“不够惊喜”。Snowflake一季报和二季度指引双双超预期，直接引爆股价。\n\n两家公司都强调AI在加速软件销售、都在说“AI不会取代我们，而是和我们共存”。但Snowflake还拿了OpenAI的2亿美元合作，Salesforce说Anthropic的产品使用量涨了5倍。\n\n2️⃣ AI ROI，是软件行业的下一个核心议题\n\nUber的CTO最近说：AI带来的效率提升，目前还cover不住成本。因为AI按token消耗收费，成本天然容易膨胀。\n\n但Snowflake在财报会上提出了解法：不同任务用不\n\n[... middle omitted ...]\n\nol derived from AI use will be a major discussion topic in the sector going forward. Uber has reportedly suspended the internal use of some AI tools due to low Rol (May 27, Futurism), but Snow\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R010",
    "title": "ABF涨价的红利，可能比市场预期的晚一个季度到来",
    "digest": "[wechat_article.md]\n# ABF涨价的红利，可能比市场预期的晚一个季度到来\n\n4月财报季是检验周期股逻辑的试金石。当某外资投行最新发布的台湾ABF载板双雄——欣兴电子与南亚电路板——的4月自结获利数据摆上桌面时，一个关键信号浮现出来：市场对涨价周期的时间节点判断，可能需要重新校准。\n\n欣兴电子4月EPS达到1.85新台币，大幅超出市场与投行预期。南亚电路板4月EPS则为0.92新台币，基本符合预期。表面上看，两者都交出了不错的答卷。但真正值得关注的，不是数字本身，而是数字背后隐藏的利润结构与时间错位。\n\n这份报告的核心判断是：ABF载板的上行周期叙事并未改变，但涨价带来的利润贡献，可能比市场普遍预期的要晚一个季度才能充分体现。4月的月度数据，恰恰暴露了这种时间差。对于正在跟踪ABF产业链的投资者而言，理解这个“滞后效应”，比追逐单月EPS的高低更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 南亚电路板的利润率稳定，恰恰说明涨价红利尚未完全入账\n\n南亚电路板4月税前利润率约为16.8%，与3月的18.2%相比基本持平。在营收环比增长3.7%的背景下，利润率没有明显扩张，这本身就值得追问。\n\n投行分析师在报告中点明了一个关键干扰项：汇兑损益。4月新台币兑美元汇率波动较大，非营业损益对利润表产生了负面影响。剔除这一因素后，营业利润率可能比账面数字更为强劲。但即便如此，利润率没有出现市场期待的跳升，暗示了一个更重要的结论：涨价带来的收入增量，尚未在4月充分反映。\n\nABF载板的涨价通常以季度为周期谈判，且从报价调整到实际出货确认收入，中间存在1-2个月的时间差。南亚电路板4月的数据，很可能只反映了涨价周期前半段的部分效益，而非全部。这意味着，5月乃至6月的利润表，才可能更完整地体现涨价效应。\n\n对于投资者而言，仅凭4月单月利润率判断\n\n[... middle omitted ...]\n\n讨论ABF周期的下一个关键变量——涨价能否真正跑赢成本曲线。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nABF 四月数据藏着什么信号？🤔\n\n封面短标题：ABF 四月利润拆解\n封面副标题：涨价落地时间差，藏在数据里\n\n---\n\n最近某外资投行更新了台湾 ABF 载板双雄的四月获利数据，两份财报放在一起看，信息量很大。\n\n**1. 欣兴电子：EPS 超预期，但利润结构有玄机**\n\n四月 EPS 1.85 新台币，明显超过市场预期。但仔细看税前利润率从三月的 12.4% 跳升到 24.8%，这个跳跃不全是本业改善。\n\n关键变量是金融资产评价损益。欣兴持有联电等科技股，四月台股大涨 23%，这部分持股的未实现收益直接拉高了整体利润。研报推测，扣除金融收益后，本业可能正面临新 HDI 产能爬坡和汇率波动的短期压力。\n\n**2. 南电：利润稳定，涨价效益还没完全体现**\n\n南电四月税前利润率 16.8%，跟三月的 18.2% 比小幅下滑，但基本平稳。研报认为，四月数据还没有充分反映最近的涨价贡献，可能要到后续月份才会逐步显现。\n\n**3. 月数据有“噪音”，看趋势比看单月更重要**\n\n研报特别提醒，月度数字容易受几个因素干扰：新产能爬坡的时间点、涨价效益的会计认列节奏、金融资产损益的波动。单月超预期或不如预期，都不宜直接线\n\n[... middle omitted ...]\n\n April non-op supposedly would recognize meaningful gain on financial assets (from Unimicron's indirectly holdings in Unimicron, UMC or other tech names, as per the mgmt.). Thus, Unimicron's A\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R011",
    "title": "医疗科技板块的真正拐点，可能不是产品周期，而是资本回报周期的重启",
    "digest": "[wechat_article.md]\n# 医疗科技板块的真正拐点，可能不是产品周期，而是资本回报周期的重启\n\n过去六个月，澳大利亚交易所医疗科技板块的四只核心标的——ResMed、Fisher & Paykel Healthcare、Nanosonics 和 Cochlear——股价表现分化显著：Cochlear 下跌超过 60%，ResMed 和 Nanosonics 跌幅约 18%-19%，Fisher & Paykel 相对坚挺，仅下跌 3%。市场习惯把这种分化归因于公司层面的独特故事：Philips 重新进入睡眠呼吸市场、GLP-1 类药物对睡眠呼吸暂停需求的影响、Cochlear 的 Nexa 市场份额变化、以及 CI 市场增速放缓。这些解释不能说错，但它们掩盖了一个更重要的结构性事实——这轮下跌并非澳大利亚公司特有的问题。\n\n某外资投行最新发布的澳大利亚医疗科技行业研报提供了一个更宏观的视角：美国大型医疗科技公司年初至今同样下跌约 20%，背后的驱动力是有机收入增长放缓叠加估值倍数急剧收缩。换句话说，澳大利亚医疗科技公司正在经历的，是一场全球性的板块重定价，而非仅仅是各自基本面的个案。\n\n这份报告最值得关注的判断，不是某只股票的买入或卖出评级，而是一个历史类比：当前板块面临的增长放缓与估值压缩，与 2010-2013 年的周期高度相似。而那一轮周期的底部，最终是由资本回报的大幅提升、盈利预期的彻底重置、以及新产品获批这三重力量共同推动反转的。如果历史可以提供某种参考，那么当前市场最应该关注的，不是需求何时复苏，而是企业是否有意愿和能力启动大规模的资本回报计划。\n\n以下是对这份研报核心逻辑的拆解，以及那些报告没有完全展开、但值得每位产业决策者和投资者深入思考的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 收入增速放缓不是澳大利亚\n\n[... middle omitted ...]\n\n关注医疗科技板块的读者而言，它们可能比任何评级本身都更重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n澳洲医疗科技板块，现在值得关注吗？\n\n板块回调中的机会\n\n最近某外资投行出了一份澳洲医疗科技板块的深度研报，把RMD、FPH、COH、NAN这几家公司从头到尾盘了一遍。我看完觉得逻辑挺清晰的，分享几个关键点。\n\n先说大背景。澳洲这几家医疗科技公司今年表现不太好，但这不是它们自己的问题——整个全球大型医疗科技板块今年也跌了差不多20%。原因有两方面：一是收入增长在放缓，二是市场给的估值倍数在收缩。\n\n1️⃣ 收入端怎么看\n美国那边因为支付政策变化，医疗设备的使用率在下降。中国的销售也成了拖累。研报认为，目前市场对2026年的盈利预期，可能还没充分反映美国医保削减的影响。历史上看（不算疫情），这种增长放缓周期大概会持续3年左右。\n\n2️⃣ 估值端怎么看\n现在板块的市盈率大概19倍，比20年平均水平低了约7个百分点。上一次估值低谷是2011年的11倍左右。那次是怎么爬出来的？三个因素：大规模股票回购、盈利预期充分下调、新产品获批或并购带来的增长催化剂。\n\n3️⃣ 个股分化明显\nRMD：新药和新产品（Noctrix收购）即将推出，同时保留着约7亿美元的股票回购计划。研报认为它处于新产品周期的前夜。\nFPH：有几个产品\n\n[... middle omitted ...]\n\nn assessing the outlook for ASX MedTech, we believe the earnings trajectory and broader sector sentiment is also worth considering. Company specific drivers which have assisted in driving a tu\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "中国医药投资进入“选择性等待”阶段：真正的分歧不在赛道，而在执行验证",
    "digest": "[wechat_article.md]\n# 中国医药投资进入“选择性等待”阶段：真正的分歧不在赛道，而在执行验证\n\n过去三个月，中国医药板块经历了从“全面反弹”到“结构性分化”的快速切换。某外资投行最新发布的投资者反馈报告揭示了一个关键信号：经历了1季度的强势表现后，机构对CDMO的态度已经从“买入布局”转向“选择性观望”，而对医疗器械和医疗服务则保持了更为克制的姿态。这并非市场对行业失去信心，而是资金正在等待一个更明确的验证节点——2季度业绩能否兑现订单趋势、利润率和管理层指引。\n\n这份报告的核心判断值得认真对待：市场真正低估的不是需求复苏的方向，而是供给端结构性变化对竞争格局的再定价。投资者在2季度末会面临一个关键抉择——哪些公司能在需求回暖中真正把规模转化为议价权和利润弹性，哪些只是搭上了行业贝塔的便车。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 投资者情绪已从“整体看多”退至“选择性聚焦”，2季度业绩成为重建信心的关键分水岭\n\n报告清晰地描绘了当前投资者的心理状态。在CDMO领域，经历了1季度的强劲表现后，资金开始向科技/半导体板块轮动，导致医药股出现明显的“获利了结”迹象。投资者普遍选择退到场边观望，核心原因并非对行业基本面的否定，而是“缺乏短期催化剂”——他们宁愿等到2季度数据出来，看到订单恢复和可见度的明确证据，再重新建立头寸。\n\n这种心态的转变并非空穴来风。近期关于美国拟限制中国临床数据使用、以及将部分中国生物技术公司纳入COINS法案的讨论，确实给市场情绪带来了额外的压力。但报告也明确指出，这些政策风险对短期基本面的实质影响“总体可控”。这意味著当前市场的谨慎更多是情绪层面的过度反应，而非基本面恶化。\n\n值得注意的是，即便药明生物宣布了高达4亿美元的回购计划、药明合联也启动了1亿美元的回购，依然未能扭转投资者的观望态度。这传递了一\n\n[... middle omitted ...]\n\n星球微信群里继续讨论，一起跟踪这些关键变量的演变。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n药企投研风向：从追高到等信号\n\n等待2Q信号\n\n一季度CDMO涨完一波后，市场态度明显变谨慎了。资金轮动到科技半导体，药企这边大家都在观望——等二季度业绩出来，看订单恢复是不是真的，边际能不能改善。\n\n1️⃣ CDMO：等催化剂，但结构逻辑还在\n\n某外资投行调研发现，投资者目前普遍“退到边线”，不是不看好，是等更清晰的信号。几个关注点：\n- 药明康德：市场在等2Q能否上调指引，订单转化和margin是核心\n- 凯莱英：GLP-1相关订单是最大看点，但估值是不是已经price in了？\n- 三星生物：短期关注罢工影响和订单节奏，Plant 6扩产是中期催化剂\n- 药明合联：ADC赛道确定性高，新加坡基地的订单爬坡决定中期收入能见度\n- 泰格医药：订单加速回暖（3-4月尤其明显），但CSRC调查和AI投入拖累利润\n\n2️⃣ 医疗器械：出海是主线，国内承压\n\n海外扩张是最大共识，但投资者要看到更实在的执行证据。\n- 微创机器人、润迈德：海外订单强劲，但市场关心的是订单能不能变成安装、安装能不能变成收入\n- 时代天使：海外案例增长指引清晰（2026年约25%），提前盈亏平衡增强信心\n- 爱康医疗：机器人战略长期看好，\n\n[... middle omitted ...]\n\nncluding proposed US restrictions on China clinical data and discussions around adding China biotech companies to the COINS Act—have added to sentiment overhang, although near-term fundamental\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "消费赛道正在经历“618前的分化”：真正有价值的不是大盘，是结构性赢家",
    "digest": "[wechat_article.md]\n# 消费赛道正在经历“618前的分化”：真正有价值的不是大盘，是结构性赢家\n\n四月的线上消费数据，像一面棱镜，折射出中国消费市场正在发生的深层分化。某外资投行最新发布的Online Brand Tracker显示，在Tmall/Taobao/JD三大平台合计口径下，宠物食品和保健品录得10%和11%的同比增长，而美容护肤和白色家电分别下滑23%和22%。这种分化并非简单的“消费降级”或“消费升级”所能概括。\n\n这份报告的价值，不在于它告诉我们哪些品类涨了、哪些跌了——这些数字本身只是结果。真正值得关注的，是数据背后暴露出的三个结构性信号：第一，618大促前的品牌策略分化已经提前显现，头部品牌正在用不同的渠道组合和定价策略重新划分地盘；第二，抖音作为增量引擎的角色进一步强化，但部分品牌对单一平台的依赖风险也在上升；第三，户外和运动服饰的增速放缓并非需求问题，而是基数效应和季节性扰动叠加后的短暂调整。\n\n以下是我们从这份报告中提炼出的四个关键洞察，以及一个尚未被充分回答的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 宠物食品和保健品是当前最具韧性的结构性赛道，但驱动逻辑截然不同\n\n四月数据中，宠物食品在Tmall/Taobao/JD合计增长10%，保健品增长11%。更值得注意的是，这两个品类并非只是短期脉冲——从季度趋势看，宠物食品从1Q26的-5%跃升至4月的+10%，保健品从1Q26的-8%改善至+11%。这意味着它们的增长具备连续性，而非单月偶发。\n\n但两者的增长驱动力完全不同。宠物食品的增长更多来自量价齐升：Tmall/Taobao口径下，宠物食品四月销售额增长14%，其中销量持平，ASP同比上升约14个百分点。这暗示着消费者在宠物消费上愿意支付更高单价，而非单纯增加购买频次。保健品则更多是价格驱动：\n\n[... middle omitted ...]\n\n。如果你对这些未解问题感兴趣，欢迎加入我们的讨论。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618前消费分化：宠粮领涨，美妆承压\n\n消费分化，谁在涨？谁在跌？\n\n4月线上数据出炉，消费赛道出现明显分化。宠粮、保健品、女装增速靠前，美妆、白电、啤酒跌幅较大。\n\n📊 整体表现（天猫/淘宝/京东合计）\n- 保健品 +11% / 宠粮 +10% / 女装 +9% / 运动服饰 +6% / 乳制品 +6%\n- 运动鞋 -5% / 小家电 -4% / 啤酒 -13% / 白电 -22% / 奶粉 -14% / 美妆 -23%\n\n1️⃣ 美妆：抖音撑场，天猫承压\n- 国货分化明显：上海家化+53%、毛戈平+36%、林清轩+23%，主要靠抖音/京东拉动\n- 珀莱雅-18%、巨子生物-16%、上美-21%、逸仙电商-29%、华熙生物-13%\n- 外资：欧莱雅+3%、雅诗兰黛+4%（靠抖音），资生堂-8%、LG生活健康-50%、爱茉莉-29%\n\n2️⃣ 运动服饰：整体放缓，户外品牌回落明显\n- 始祖鸟、萨洛蒙、lululemon 4月增速放缓，部分受高基数影响\n- 阿迪达斯、斐乐、彪马、特步、亚瑟士、ON表现相对稳健\n- 品牌也在做全渠道布局（得物等新兴渠道+线下），线上数据可能不完整\n\n3️⃣ 宠物食品：4月加速，国\n\n[... middle omitted ...]\n\nhoes/Small kitchen appliances/Beer/White\n\ngoods/IMF/Beauty lagged at -5%/-4%/-13%/-22%/-14%/-23% yoy decline. Noted we saw meaningful re-base for pet foods, white goods and Dairy for Tmall/Tao\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "日本FA设备股的最大分歧不在周期顶点，而在供给侧定价权的重新分配",
    "digest": "[wechat_article.md]\n# 日本FA设备股的最大分歧不在周期顶点，而在供给侧定价权的重新分配\n\n市场正在经历一个微妙但关键的转变。日本工厂自动化（FA）设备领域，过去几个月财报季释放的信号高度一致：订单激增，需求强劲，多家公司管理层提到询单量创下历史新高。日本机床工业会（JMTBA）3-4月的订单数据意外刷新了单月历史纪录，亚洲和美洲成为主要驱动力。\n\n这些数字本身并不令人意外。真正值得关注的是，某外资投行在最新一期研报中，对覆盖的11只FA股票进行了大规模评级调整：上调Keyence至买入，上调THK至中性，下调SMC至中性。目标价调整幅度从-11%到+44%不等。这不是一次常规的季度更新，而是一次基于“峰值周期已开始”这一判断的系统性重估。\n\n这份报告最核心的判断是：市场此前对AI资本开支的讨论高度集中在需求端，但真正驱动未来12-18个月股票相对表现的核心变量，已经转移到了供给侧——具体来说，是企业的供给能力、议价权以及资本配置政策的清晰度。那些能够在供需紧张环境中将规模转化为定价权的公司，将获得估值溢价；而那些尽管基本面强劲，但利润率、资本回报率或资本配置政策存在不确定性的公司，即使身处同一上行周期，也可能面临估值折价。\n\n这意味着，投资者不能再简单地以“AI资本开支受益股”来一篮子配置日本FA板块。周期上行是背景，但个股的分化将远比上一轮周期更为剧烈。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 峰值周期已经确认，但市场低估了供给侧的约束条件\n\n研报明确指出，一个“新的峰值周期已经开启”，并预计覆盖范围内多家公司将在FY3/27E至FY3/28E期间实现历史最高利润。这一判断基于几个关键信号：Yaskawa Electric的全年业绩发布拉开了春季财报季序幕，随后多家公司管理层强调需求正在急剧上升，并且虽然仍在可控范围内，但\n\n[... middle omitted ...]\n\neyence、SMC、THK等核心标的进行更深入的逐项拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本FA行业：AI资本开支的供给端红利\n\nAI资本开支的供给端红利\n\n谁在受益？日本FA设备股的周期新起点\n\n日本FA（工厂自动化）行业正在经历一轮新的上行周期，核心驱动力是AI资本开支从半导体向更广泛的工业领域扩散。某外资投行近期大幅调整了覆盖标的的评级和目标价，核心逻辑是：供给端紧张+AI资本开支溢出效应，将推动多家公司利润创新高。\n\n1/ 周期已启动，供给端成关键变量\n- 春季财报季多家公司表示，订单需求正在急剧上升，甚至出现提前下单的迹象。某外资投行认为，这标志着新一轮峰值周期已经开始。\n- 过去几轮周期（2017-18、2021-22）的经验表明，供给能力将成为企业能否充分受益的关键。在需求旺盛但供给受限的环境下，能够提供充足产能的公司将获得更大市场份额。\n\n2/ AI资本开支正在扩散\n- 半导体设备投资是核心驱动力，但红利正在外溢到电池、服务器、周边组件，甚至一般工业机械。\n- 日本机床工业会3-4月订单数据意外创下历史新高，主要来自亚洲和美洲地区。某外资投行预测，日本机床海外订单在FY3/27将达到1.425万亿日元（同比增长13.2%），在FY3/28回落至1.311万亿日元。\n- 全球半导体\n\n[... middle omitted ...]\n\n apparent recently, we have significantly revised our forecasts and the premiums for calculating 12-month target prices for FA companies in our coverage. The tightness in supply/demand and the\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "全球机器人需求正在出现结构性分化，中国市场的AI红利并未惠及所有玩家",
    "digest": "[wechat_article.md]\n# 全球机器人需求正在出现结构性分化，中国市场的AI红利并未惠及所有玩家\n\n2026年4月的日本机器人出口数据，表面上是一组月度海关统计，但背后隐藏着一个对全球自动化投资格局至关重要的判断：需求正在从“普涨”转向“结构性分化”，而市场对此的定价可能尚未完全反映。\n\n某外资投行刚刚发布的这份研报，通过对日本机器人及立式加工中心出口数据的拆解，揭示了一个关键信号——中国市场的AI相关需求并未均匀扩散，传统工业机器人龙头正在失去增长动能，而细分赛道的赢家可能完全不同。这不仅是日本机械股的投资线索，更是全球制造业资本开支方向的晴雨表。\n\n以下是我们基于这份研报的深度解读与延伸判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国市场的机器人需求正在“分层”，AI红利只惠及特定品类\n\n2026年4月，日本整体机器人出口至中国的量同比增长33%，环比下降18%。表面看，同比增速仍然强劲，但环比转负已经值得警惕。更关键的是，Fanuc（发那科）对中国的机器人出口环比下降了14%。研报明确指出，Fanuc并未享受到与中国AI需求同步增长的红利。\n\n原因在于，AI相关的自动化需求主要集中在小型六轴机器人或SCARA机器人领域，而Fanuc的强项在于大型机器人。这意味着，当市场谈论“AI拉动机器人需求”时，必须细分到品类和客户结构。不是所有机器人公司都能受益于AI资本开支。\n\n对于投资者而言，这意味着：单纯押注“中国机器人”主题可能已经不够。需要区分哪些公司真正切入了AI相关的精密装配、电子制造场景，哪些仍在依赖传统汽车和一般工业的周期性订单。后者的增长持续性存在疑问。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 欧洲市场成为意外亮点，但可持续性有待验证\n\n4月数据显示，日本对欧洲\n\n[... middle omitted ...]\n\n表、更细致的财务拆解，以及一群对产业趋势真正感兴趣的同路人。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月机器人出口数据出来了，几个信号值得关注\n\n📊 机器人出口数据解读\n\n4月日本机器人出口总量14,271台，同比+41%，但环比-4%。中国依然是最大买家，出口6,206台，同比+33%，环比-18%。\n\n**1/ 欧洲需求意外走强**\n欧洲出口1,991台，同比+74%，环比+13%。这个增速有点意思，欧洲制造业似乎在加速自动化升级。\n\n**2/ 北美开始降温**\n北美出口2,065台，同比-4%，环比-19%。连续两个月下滑，可能和当地制造业投资节奏放缓有关。\n\n**3/ 中国需求结构分化**\n投行研报分析，发那科对中国的机器人出口环比-14%，说明并未像部分机床设备那样持续增长。他们认为，在中国AI相关需求中，小型6轴或SCARA机器人厂商可能更受益。\n\n**4/ Robodrill的隐忧**\n发那科Robodrill对华出口环比-11%，同比-16%。研报推测，主要客户（如某美国手机巨头）在春节后需求高峰已过。同时，印度出口环比+328%，但绝对量仍低，暂不足以说明智能手机需求已完全转移。\n\n**5/ 安川电机：印度成亮点**\n安川电机4月全球出口1,309台，同比+35%，环比+33%。对印度出口\n\n[... middle omitted ...]\n\nJapan to the rest of the world can be viewed as an indicator of investment in robots and automation, mainly in the auto and electronics industries. In this note, we outline our views on the ro\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "AI驱动的MLCC周期可能比任何人预期的都要长——4月贸易数据确认量价齐升仍在加速",
    "digest": "[wechat_article.md]\n# AI驱动的MLCC周期可能比任何人预期的都要长——4月贸易数据确认量价齐升仍在加速\n\n市场对MLCC（多层陶瓷电容）的讨论，过去半年里大多集中在“周期会不会见顶”这个问题上。4月日本财务省贸易统计数据的出炉，给出了一个值得认真对待的答案：出口量环比增长7%，平均出口价格环比上涨3%，出口金额同比大增28%。这不是周期末端的信号，而是周期中段的加速。\n\n某外资投行在最新研报中明确表示，当前由AI驱动的MLCC周期，可能是历史上规模最大、持续时间最长的一次，而我们现在仍处于早期阶段。这个判断与市场主流叙事存在显著偏差——多数投资者仍倾向于用消费电子周期的旧框架来理解MLCC，而忽略了AI服务器带来的结构性需求重塑。\n\n我们仔细拆解了这份研报的核心逻辑，发现真正重要的不是短期数据有多好，而是三个正在改变行业竞争格局的结构性力量：技术门槛的不可逆提升、定价权的转移，以及供应商格局的固化。这些力量叠加在一起，意味着本轮周期的利润分配方式将与过去截然不同。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月贸易数据确认的不是“好”，而是“加速”——量价齐升的斜率在变陡\n\n先看一组关键数字。4月MLCC出口量环比增长7%，出口额环比增长9%，平均出口价格环比增长3%。同比来看，这三个数字分别是10%、28%和16%。研报特别强调，这些数据与日本MLCC制造商近期公布的财报高度吻合——订单依然非常强劲。\n\n但更值得关注的是趋势的斜率变化。环比3%的ASP上涨，在MLCC这样一个通常价格缓慢下降的行业里，本身就是一个强烈信号。过去十年中，MLCC的平均价格大多呈现温和下行趋势，只有2017-2018年的超级周期曾出现过价格持续上涨。当前的价格走势，正在重现甚至超越那个时期的特征。\n\n这意味着什么？市场对MLCC的定价逻辑正在发\n\n[... middle omitted ...]\n\n报解读、原始数据图表，以及我们自己对关键未解问题的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC的涨价逻辑，比想象中更硬\n\nAI驱动的MLCC超级周期\n\n4月日本MLCC出口数据出来了，量价齐升的趋势非常明确👇\n\n出口均价环比+3%，出口量环比+7%，出口额环比+9%。\n同比数据更猛：均价+16%、量+10%、额+28%。\n\n这不是短期波动，是AI服务器需求在持续拉动。\n\n1️⃣ 为什么说这是“史上最大最长”的MLCC周期\n\n投行研报判断：当前MLCC周期由AI驱动，规模和持续时间可能超过以往任何一轮。\n\n关键逻辑：\n- AI服务器GPU/ASIC周边需要大量低电压、高容量的MLCC\n- 在有限板面积上，小型化和容量提升必须同步推进\n- 技术门槛越来越高，能做的供应商越来越少\n\n2️⃣ 谁是这轮周期的赢家\n\n目前能供应低电压、高容量MLCC的玩家只有三家：\n- 村田、三星电机、太阳诱电\n\n研报认为它们会持续受益，而且每次技术迭代都能重新定价——这等于变相涨价。\n\n另外，TDK虽然还没进入这个细分市场（正在等材料突破），但它拿到了高电压、高容量MLCC的订单，用在电源电路周边。技术跟车规级产品几乎一样，能拉高工厂利用率。\n\n3️⃣ 为什么说现在还在早期阶段\n\n研报用了一个很有意思的表达：“stil\n\n[... middle omitted ...]\n\nn Murata Mfg. (on CL), Taiyo Yuden, and TDK. We increasingly believe that the current MLCC cycle, driven by AI, will be the largest and longest in history. We believe we are still in the early\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "中国可再生能源的真正拐点：不是需求爆发，而是供给结构正在被重新定价",
    "digest": "[wechat_article.md]\n# 中国可再生能源的真正拐点：不是需求爆发，而是供给结构正在被重新定价\n\n过去一个月，中东冲突与发达市场数据中心电力瓶颈两条线索同时发酵，让中国可再生能源板块重新进入全球投资者的视野。自5月15日以来，阳光电源和德业股份分别上涨14%和20%，而同期上证综指下跌1%。\n\n但这份由某外资投行在“全球中国峰会”后发布的研报，真正值得关注的判断并不是“需求回来了”。它揭示了一个更底层的变化：中国可再生能源的定价逻辑，正在从“规模增长”转向“结构性稀缺”。市场目前低估的，不是光伏或风电的装机量，而是供给端正在发生的三个根本性重构——储能从配角变成电网基础设施、海上风电从政策口号变成可执行的装机计划、以及新兴市场分布式储能从边缘走向主流的加速度。\n\n以下，我们从这份研报中提炼出四个核心洞察，并讨论一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 储能正在经历一次“用途升级”：从削峰填谷到AI数据中心的基础设施组件\n\n阳光电源在峰会上的表态值得反复推敲。管理层明确表示，已获得来自数据中心开发商的AI数据中心相关储能订单。这不是传统意义上的“峰谷套利”或“调频辅助服务”，而是将储能嵌入到AI数据中心的供电架构中，解决老旧电网基础设施与高可靠性供电需求之间的矛盾。\n\n报告引用阳光电源管理层的原话：AI数据中心为储能创造了“新的机会集”。具体来说，储能可以配置成“电网友好型”数据中心，支持AI数据中心的快速启动，甚至在电网互联优先级上获得优势——这取决于美国能源部即将做出的决定。\n\n这里的关键洞察是：储能的市场定位正在从电力系统的“可选配件”升级为“必要基础设施”。当AI数据中心的电力需求与电网老化之间的矛盾成为发达市场的结构性痛点时，储能厂商获得的定价权与议价能力，将显著高于传统的光伏逆变器或电池销\n\n[... middle omitted ...]\n\n的变化，并在第一时间分享最新的调研发现和产业链交叉验证结果。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国新能源投研圈，最近在聊什么？\n\n**热门方向：**\n**储能+出海，逻辑变了**\n\n---\n\n最近参加了一个外资投行的能源转型交流会，信息量很大，帮大家拎几个重点逻辑：\n\n**1/ 中东冲突+AI数据中心，把储能推到了新高度**\n以前聊储能，主要看国内大储、欧洲户储。现在多了一个变量：AI数据中心（AIDC）对电力的稳定性和可靠性要求极高，老旧电网根本扛不住。这给储能创造了一个全新的应用场景。\n\n某头部逆变器企业已经拿到了AIDC相关的储能订单，模式是“grid-friendly”数据中心，帮助数据中心快速启动、平滑并网。这个方向还在等政策落地，但方向很明确。\n\n**2/ 新兴市场的分布式储能，正在爆发**\n中东冲突导致能源供应中断，东南亚、印度、拉美等新兴市场对分布式储能的需求急剧上升。和大型储能项目不同，分布式储能订单周期短，成本传导快，部分订单已经能反映在利润里。\n\n这对相关逆变器公司是直接利好，逻辑很顺。\n\n**3/ 海上风电，政策终于给了“定心丸”**\n今年3月，国务院首次给出了2030年海上风电装机目标：100GW。这在顶层政策层面是第一次。\n\n回顾历史，国家对新能源的装机目标，实际完成往往大\n\n[... middle omitted ...]\n\nveloped-market data-center power infrastructure constraints. Sungrow and Deye share prices are up 14%/20%, respectively, since May 15 $^{th}$ (vs. SHCOMP -1%). Within ESS, Sungrow cited early \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 27 May 2026 08:09 PM HKT\n\nDisseminated 27 May 2026 08:09 PM HKT"
  },
  {
    "id": "R018",
    "title": "零售投资者正在完成一次“认知升级”，而不是单纯的追涨",
    "digest": "[wechat_article.md]\n# 零售投资者正在完成一次“认知升级”，而不是单纯的追涨\n\n这份来自某外资投行量化策略团队的周度零售资金流报告，表面上是一份交易行为记录，但放在当前市场环境下，它揭示了一个更重要的信号：零售投资者群体正在从“情绪驱动”向“主题驱动”转变，并且这一转变的持续性正在被市场低估。\n\n报告覆盖了截至5月27日的数据，核心发现是：零售投资者的整体买入力度并不激进（约历史第54百分位），但资金流向高度集中在AI、存储芯片、量子计算等结构性主题上。这不是散户在追热点，而是他们在用行动为某些长期逻辑投票。\n\n更重要的是，报告通过构建零售投资者的损益分析，证明了一个反直觉的事实：过去几个月，零售投资者在个股上的表现显著跑赢了基准。这意味着，市场对于“散户终究会被收割”的刻板印象，可能需要重新校准。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 整体买入力度温和，但主题集中度创下新高\n\n从总量看，本周零售资金净流入约63亿美元，略低于12周均值67亿美元。ETF端流入46亿美元，个股端16亿美元。表面数字并不惊人，甚至偏弱。\n\n但拆开来看，结构非常清晰。ETF端虽然整体处于历史低位（23.4百分位），但资金几乎全部涌向了半导体ETF：SOXX（z-score 5.0）、QQQM（3.4）、SMH（2.1）。个股端则更为极端，买入力度达到71.4百分位，且几乎完全由AI和存储芯片股票驱动。\n\n这组数据意味着什么？零售投资者并非对市场整体乐观，而是在用脚投票，押注少数几个他们认为能穿越周期的方向。这种“高度选择性”的买入行为，与2021年MEME热潮中“无差别买入”的模式有本质区别。\n\n对于产业决策者而言，这提供了一个观察“普通投资者长期信心”的窗口：他们愿意在哪些主题上持续加仓，哪些主题可能只是阶段性博弈。目前看，AI基础设施和存储芯\n\n[... middle omitted ...]\n\n问题，我们会在群内分享完整报告的原始图表和我们的进一步解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n散装投研｜散户正在悄悄加仓这些方向\n\n散户最近在买什么？AI、存储、太空、量子\n\n——\n\n📌 本周零售资金流整体温和（约54%分位），但方向很明确——科技依然是心头好。\n\nETF买入看似平淡（23.4%分位），但钱都集中流向了半导体相关ETF：SOXX、QQQM、SMH。个股层面更活跃（71.4%分位），几乎全是AI和存储相关。\n\n1️⃣ **存储：万亿俱乐部，散户还在买**\nMU和SK海力士市值突破1万亿美元，但散户并没有大规模获利了结。MU本周净买入+3.4个标准差，SNDK也有+0.8。期权方面，MU从短期看空回到中性。DRAM的买入节奏趋于平稳，买卖交替。分析师认为，HBM、DRAM、NAND的供应紧张会持续到2026年以后。\n\n2️⃣ **软件 vs 半导体：散户在调仓**\n之前我们聊过软件和半导体的拥挤度差异，最近出现了一些反转。SNOW宣布与亚马逊签下60亿美元大单，盘后暴涨25-30%；CRM的Q2指引略低于预期。散户在继续卖出PLTR和PANW，但买入NOW和ZS——ZS周三跌了31.5%，散户趁机抄底，单日净买入高达12个标准差。\n\n3️⃣ **太空：ETF受追捧，个股在获利**\n太空主题\n\n[... middle omitted ...]\n\nz) and SMH (2.1z); this preference was reinforced by strong single stock purchases (71.4%ile) that were overwhelmingly driven by AI / Memory stocks.   \n- Trillion Dollar Club. We highlighted M\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 27 May 2026 11:22 PM EDT\n\nDisseminated 27 May 2026 11:22 PM EDT"
  },
  {
    "id": "R019",
    "title": "AI在药物研发中的真正价值：不是颠覆，而是效率层的重构",
    "digest": "[wechat_article.md]\n# AI在药物研发中的真正价值：不是颠覆，而是效率层的重构\n\n市场对AI制药的叙事正在经历一次关键的校准。过去两年，行业舆论倾向于将AI描绘成药物发现领域的颠覆性力量——从靶点发现到临床开发的全链条重塑。但近期与英矽智能CEO Alex Zhavoronkov的对话，提供了一份更加务实的框架。这份来自投行研报的解析揭示了一个更值得关注的判断：AI在药物研发中最确定的价值，不在于替代科学家或压缩临床周期，而在于将早期发现阶段的生产力提升到一个可量化的新台阶。对于产业决策者和投资者而言，真正需要追问的不是“AI何时取代传统研发”，而是“哪些环节的效率提升已经可以被定价，哪些瓶颈仍然无法绕过”。\n\n这一判断之所以重要，是因为它直接影响了资本配置的方向。如果AI制药的核心价值仅局限于早期发现阶段，那么行业估值逻辑就需要从“平台颠覆”转向“工具赋能”。而英矽智能作为全球少数拥有多个临床阶段资产的AI制药公司，其管理层的坦诚表态——从数据护城河的有限性到动物模型不可替代的约束——为这一判断提供了重要的实证支撑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 竞争壁垒不在数据规模，而在系统整合与基准测试能力\n\n行业长期争论的一个核心问题是：AI制药公司的数据资产是否构成可持续的护城河。Alex Zhavoronkov给出了一个相当直接的否定答案。尽管英矽智能拥有超过3000个疾病-靶点关联的内部数据集，但他明确指出，单纯依赖差异化数据并未在行业层面转化为药物开发的成功。他提到了一个“数据公司的墓地”——那些以数据为中心但未能交付药物的企业。\n\n这一观点的含义是深刻的。在AI制药领域，数据本身正在快速商品化。公共数据库、文献挖掘、以及合作获取的数据，正在缩小领先者与追随者之间的数据差距。真正构成差异化的，是公司如何利用这些数据—\n\n[... middle omitted ...]\n\n图表，以及更多关于AI制药公司估值框架和竞争格局的深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI制药的真实进度：不是颠覆，是提效\n\nAI制药，到底走到哪了？\n\n最近看了一份某外资投行与英矽智能CEO的对话纪要，信息量很大，把AI制药的真实状态讲得很清楚。\n\n简单说：AI不是来颠覆新药研发的，它更像一个“效率加速器”。\n\n1/ 最确定的优势：加速早期发现\n\nAI在药物发现阶段的价值最明确。英矽智能的数据是：从靶点发现到临床前候选化合物（PCC），大概需要12-18个月，花费300-500万美元。而且计算效率还在提升，从几周缩短到几天。\n\n但注意，这只是早期阶段。到了IND申报和临床试验阶段，AI就没法加速了——这些环节受制于监管和生物学规律，AI插不上手。\n\n2/ 数据不是护城河\n\n一个反直觉的观点：英矽智能CEO认为，专有数据集不是AI制药公司的核心竞争力。\n\n虽然他们自己积累了3000+疾病-靶点关联数据，但CEO直言，光靠数据优势的公司很多都失败了，甚至称之为“数据公司的坟场”。\n\n真正拉开差距的是两样东西：\n- 集成化的基准测试系统（英矽有约1200个自研基准测试）\n- 模型编排能力\n\n说白了，算法架构和评估体系比数据量更重要。\n\n3/ 最大的瓶颈：不是安全性，是有效性\n\nAI能帮我们更快筛选\n\n[... middle omitted ...]\n\n emphasized wholesale disruption, management now highlights that AI's impact is most tangible in accelerating and de-risking early discovery workflows rather than replacing core scientific fun\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R020",
    "title": "中国车企出海，市场真正低估的不是总量，而是结构性份额的再分配",
    "digest": "[wechat_article.md]\n# 中国车企出海，市场真正低估的不是总量，而是结构性份额的再分配\n\n中国汽车制造商4月海外注册数据出炉。单月环比有涨有跌，同比仍维持高增速。这份报告最值得关注的判断不是“总量还在增长”，而是：**海外市场的增长已从“铺网点、拼低价”的粗放阶段，进入“选市场、建壁垒”的结构性分化期。** 不同车企在不同区域的表现差异，正在揭示谁真正拥有可持续的海外竞争力。\n\n4月的数据信号很清晰：比亚迪海外注册量环比下降10-15%，主要受英国市场从3月峰值（约1.5万辆）正常化拖累；但拉丁美洲和东南亚的增量正在补位。吉利环比增长10-15%，巴西和澳大利亚是核心驱动。长城汽车环比下降5-10%，澳大利亚和巴西同时出现下滑。三家头部企业，三条截然不同的轨迹。\n\n这组数字背后，是投资者需要重新理解的一个关键问题：**中国车企海外扩张的胜负手，已经从“卖了多少车”转向“在哪里卖、卖给了谁、能否守住份额”。** 某外资投行的这份月度追踪报告，恰恰提供了拆解这一问题的第一手数据。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 巴西和澳大利亚已成为中国车企海外竞争的核心战场\n\n4月数据中最突出的结构性特征，是巴西和澳大利亚两个市场对中国车企海外销量的集中贡献。对于比亚迪、吉利、长城三家而言，这两个市场的表现几乎决定了其整体海外业绩的走向。\n\n比亚迪在巴西4月销量达到1.8万辆，环比增长12%，而同期巴西整体汽车市场环比下降9%。这意味着比亚迪在当地的市场份额正在快速提升，而非仅仅跟随市场波动。澳大利亚市场同样如此，比亚迪销量环比增长9%至8200辆，市场整体却下降9%。这种“逆势增长”是判断品牌力和渠道效率的关键指标。\n\n吉利在巴西的表现更为激进。4月销量环比暴增210%至3600辆，虽然绝对量仍低于比亚迪，但增速暗示其巴西战略正在加速落地\n\n[... middle omitted ...]\n\n内容均基于公开研报原文，不做荐股，只做分析框架的搭建与讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月中国车企出海成绩单：谁在领跑？🚗\n\n封面：出海成绩单\n\n副标题：4月海外销量拆解\n\n4月中国车企海外销量出炉，整体势头不错，但具体到每家，故事完全不同。某外资投行最新研报拆解了BYD、吉利、长城的海外销售数据，信息量很大。\n\n**1️⃣ BYD：总量微降，但结构在优化**\n\n4月BYD海外注册量环比下降10-15%，主因是英国市场从3月高峰（1.5万辆）回落至正常水平（约0.5万辆）。但别急，亮点在拉美和东南亚：\n- 巴西：环比增长12%至1.8万辆，逆势跑赢当地大盘（-9%）\n- 澳大利亚：环比增长9%至0.82万辆，同样碾压当地市场\n- 印度尼西亚：环比暴增67%至0.56万辆，远超当地市场增速（+32%）\n\n整体看，巴西、澳大利亚、印尼三国已占BYD海外销量的44%，同比增速仍高达55-60%。\n\n**2️⃣ 吉利：环比增长10-15%，巴西是最大增量**\n\n吉利4月海外表现亮眼，环比增长10-15%，同比接近翻倍（+95-100%）。主要驱动力：\n- 巴西：环比暴增210%至0.36万辆，虽然基数低但增速惊人\n- 澳大利亚：环比增长57%至0.3万辆\n- 俄罗斯：环比微增2%至0.75万辆，但跑输\n\n[... middle omitted ...]\n\n.5k declines in both Australia and Brazil. YoY growth reached 15-20% in April.   \nIn April, Brazil and Australia remained the key overseas growth drivers for Chinese OEMs, while BYD and Geely \n\n[... middle omitted ...]\n\nd>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$16.55</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "光伏产业链的真正企稳，或许不是底部，而是新一轮分化的起点",
    "digest": "[wechat_article.md]\n# 光伏产业链的真正企稳，或许不是底部，而是新一轮分化的起点\n\n过去几周，光伏产业链价格传递出一个令市场既熟悉又陌生的信号：上游多晶硅价格在经历长达数月的阴跌后，终于止住了下滑势头，稳定在每公斤34.5至35元人民币的区间。硅片价格已经横盘超过一个月，电池片虽然周环比微跌0%至1.5%，但跌幅明显收窄。组件端，无论是国内集中式还是分布式项目，TOPCon组件价格均未出现进一步松动。\n\n对于习惯了“跌跌不休”的市场参与者而言，这种全面企稳的态势，很容易被解读为底部信号。但某外资投行最新发布的太阳能产品价格追踪周报（截至2026年5月27日）揭示了一个更复杂的图景：价格的稳定并非源于需求的强劲复苏，而是供给端在极端亏损下的被动收缩。这意味着，当前的价格均衡是脆弱的，真正值得关注的不是“价格是否见底”，而是“哪些企业能在这种脆弱均衡中活下来，并重新获得议价权”。\n\n这份报告的核心价值不在于罗列了哪些价格变化，而在于它提供了判断产业链竞争格局转折点的关键证据。以下是我们从这份周报中提炼出的五个核心洞察，它们将帮助产业决策者和投资者重新校准对光伏行业未来走势的认知框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 多晶硅价格止跌的真正含义不是供需再平衡，而是行业现金成本的硬约束被触及\n\n报告中最引人注目的数据点，莫过于多晶硅均价在连续多周下跌后首次企稳。从历史价格走势图来看，多晶硅价格从2022年底的高点每公斤约300元一路下探至当前的35元附近，跌幅超过88%。这一价格水平意味着什么？它已经低于绝大多数二三线企业的现金成本。\n\n报告并未直接披露各企业的成本曲线，但我们可以从行业常识推断：当价格跌破现金成本时，企业每生产一吨多晶硅都在消耗现金流，而非创造价值。此时，停产检修、推迟投产、甚至永久性退出成为理性选择。因此，本\n\n[... middle omitted ...]\n\n报告的解读、原始数据图表，以及更多基于产业链调研的一手判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光伏产业链价格周报：硅料止跌，EVA大跌\n\n光伏产业链价格进入稳定期\n\n某外资投行最新周报显示，5月27日当周光伏产业链价格整体平稳，但有个关键变量值得关注。\n\n1️⃣ 上游硅料止跌企稳\n多晶硅均价停在34.5-35元/kg，结束了此前连续下跌。硅片价格也稳了一个多月，182mm和210mm分别报0.9元/片和1.2元/片，环比持平。\n\n2️⃣ 电池片小幅松动\n182mm TOPCon电池片均价0.33元/W，周环比微跌1.5%。210mm电池片持平在0.34元/W。整体看，电池端价格弹性比硅片大一点。\n\n3️⃣ 组件价格按兵不动\n国内分布式TOPCon组件0.76元/W，地面电站项目0.72元/W，周环比均持平。出口端，中国产输欧TOPCon组件0.123美元/W，美国组装版0.30美元/W，也没变化。\n\n4️⃣ 辅材出现分化\n光伏胶膜价格稳定，但EVA树脂价格单周暴跌18.5%，从13500元/吨直接跌到11000元/吨。POE树脂倒是稳在20750元/吨。这里推测EVA大跌可能跟下游备货节奏放缓有关，研报未给出具体原因。\n\n5️⃣ 关键时间线对比\n从数据看，182mm TOPCon电池片年初至今跌了14\n\n[... middle omitted ...]\n\nhina-made EU TOPCon and US-assembled TOPCon module prices were unchanged at US\\$0.123/W and US\\$0.30/W, respectively.   \nPrices of solar films were stable. EVA resin price plunged 18.5% WoW, w\n\n[... middle omitted ...]\n\nr><td>Huaming Power Equipment (002270.SZ)</td><td>O (04/08/2026)</td><td>Rmb23.25</td></tr><tr><td>Ningbo Sanxing Medical Electric Co. Ltd. (601567.SS)</td><td>O (04/08/2026)</td><td>Rmb16.82</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R022",
    "title": "巴西糖市真正的拐点不在产量，而在乙醇对定价权的争夺",
    "digest": "[wechat_article.md]\n# 巴西糖市真正的拐点不在产量，而在乙醇对定价权的争夺\n\n全球糖市正在经历一个被广泛误解的阶段。当市场聚焦于巴西中南部2026/27榨季创纪录的开局压榨量时，真正需要被关注的不是“糖多了”，而是“糖厂选择了乙醇”。这个选择正在重塑未来的价格曲线和行业竞争格局。\n\n某外资投行最新发布的拉美农业研报揭示了这一结构性变化。报告显示，截至4月底，巴西中南部甘蔗压榨量同比增长75%，糖产量同比增幅达55%，均显著超出市场预期。但与此同时，糖醇比从去年的45.2%骤降至38.2%——糖厂在绝对产量增加的情况下，主动减少了糖的生产比例。\n\n这意味着什么？短期糖价承压是事实，但市场低估了供给端正在发生的再定价过程。这不是一个简单的“丰收导致价格下跌”的故事，而是一场关于能源政策、乙醇溢价和天气风险的复杂博弈。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 压榨开局超预期，但真正超预期的不是产量而是糖厂的选择\n\n研报数据显示，4月下半月甘蔗压榨量达到6046万吨，同比增幅高达74.6%，比投行模型预期高出48.9%。TRS（总可回收糖）升至112.58公斤/吨，同比增长5.4%。糖产量达到248万吨，同比增长55.2%，也比预期高出32.4%。\n\n这些数字看起来是典型的“供给冲击”。但如果只看糖产量，就会错过关键信息：糖醇比从45.2%降至38.2%，意味着糖厂将更多甘蔗用于生产乙醇，而非糖。乙醇产量同比增长71.8%，达到32.9亿升，同样大幅超出预期。\n\n这里的逻辑需要拆解：糖厂并非因为甘蔗太多而被动调整，而是基于价格信号主动选择。当前乙醇对糖的溢价已经达到具有吸引力的水平，加上巴西政府即将推行的混合燃料政策（将乙醇掺混比例从30%提升至32%），糖厂认为乙醇的短期回报更优。\n\n对于投资者而言，这意味着糖价短期承压并非来自供给\n\n[... middle omitted ...]\n\n模型、政策路径的概率分布，以及不同天气情景下的资产定价逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n巴西糖季提前爆发，供应压力与乙醇博弈\n\n供需博弈中的巴西糖市\n\n巴西2026/27榨季开局比预期更猛、更早，4月甘蔗压榨量同比暴增75%，糖产量同比+55%，远超市场预期。但有趣的是，糖醇比却从45%降至38%，糖厂更倾向生产乙醇，因为乙醇价格更香。\n\n1️⃣ 供应提前集中释放\n4月甘蔗压榨量6046万吨，比机构预期高出49%。糖产量248万吨，超预期32%。这意味着短期供应压力骤增，糖价面临下行压力。但这也是好事——库存能更早见底，为下半年价格反弹铺路。\n\n2️⃣ 乙醇才是主角\n乙醇产量同比+72%，其中甘蔗乙醇产量+110%。糖醇比降至38%，创近年新低。原因是乙醇价格相对糖价有溢价，糖厂理性选择利润更高的品种。但大量乙醇供应也压低了乙醇出厂价，反过来刺激加油站需求。\n\n3️⃣ 政策变量值得关注\n巴西计划6月将汽油中乙醇掺混比例从30%提至32%，预计每年消化约8-9亿升乙醇。这项政策就像泄压阀，能缓解乙醇供应过剩，间接支撑糖价。不过汽油补贴政策仍是最大不确定因素。\n\n4️⃣ 天气风险不可忽视\n厄尔尼诺风险正在上升，历史上厄尔尼诺常导致亚洲主产区减产、推高糖价。虽然巴西当前供应充裕，但若厄尔尼诺在后期影响\n\n[... middle omitted ...]\n\nt is running \\~30–50% above consensus in the opening months of the harvest. More mills operating and at a faster pace and probably also more cane as well.   \nMills are choosing ethanol. Ethano\n\n[... middle omitted ...]\n\ngricola S.A. (SLCE3.SA)</td><td>E (09/17/2025)</td><td>R$15.89</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R023",
    "title": "香港地产的真正拐点不在住宅，而在写字楼的“结构性分叉”",
    "digest": "[wechat_article.md]\n# 香港地产的真正拐点不在住宅，而在写字楼的“结构性分叉”\n\n市场对香港地产板块的讨论，大多仍停留在“利率何时降”、“住宅库存何时消化”这些周期性问题上。但一份来自某外资投行与莱坊联合举办的专家电话会议纪要，揭示了一个更值得关注的信号：香港地产市场的复苏，正在从“普涨预期”转向“结构性分化”。真正决定资产价值走向的，不是利率本身，而是不同细分市场之间的供需错位程度，以及资金在其中的重新分配。\n\n这份报告的核心判断是：住宅市场已经进入温和复苏通道，但写字楼市场的分化才是当前最大的定价变量。莱坊专家预计2026年大众住宅价格涨幅在8-10%之间，而甲级写字楼租金整体可能上涨8-12%。然而，后者内部的分化远比前者剧烈——顶级中环写字楼租金同比上涨9.2%，而港岛东写字楼租金反而下跌了10.6%。这不是同一轮复苏的不同速度，而是两个截然不同的市场逻辑在同时上演。\n\n为什么这个判断现在很重要？因为过去一年，市场对香港地产的关注几乎全部集中在住宅库存消化和利率预期上，而写字楼市场——尤其是其内部的结构性分化——被严重低估了。当投资者还在用“香港地产复苏”这样一个笼统叙事来配置仓位时，真正决定超额收益的，是能否识别出哪些细分市场正在经历“供给侧的再定价”。\n\n以下，我们从几个关键维度展开这份报告的核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 住宅市场的复苏逻辑已经从“利率驱动”切换为“库存驱动”\n\n莱坊专家在电话会中明确表示，利率“不是当前需要担忧的问题”。这一判断值得细品。过去两年，几乎所有关于香港地产的讨论都以利率为轴心——降息预期推迟，股价下跌；降息预期提前，股价反弹。但莱坊的立场暗示，这个叙事框架正在失效。\n\n真正驱动住宅市场走向的，是库存。当前香港住宅库存约为2万套，而2021年高峰时期为2.8万套。更\n\n[... middle omitted ...]\n\n们的详细解读笔记，并持续跟踪这些判断在后续数据中的验证情况。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港楼市：回暖信号已经出现\n\n2026年，香港楼市怎么看？\n\n某外资投行最近与莱坊（Knight Frank）开了一场专家会，几个关键判断值得关注👇\n\n1/ 住宅市场：回暖在路上\n莱坊预计2026年大众住宅价格涨幅8-10%\n豪宅价格涨幅5-8%\n豪宅（1000万美元以上）2025年价格同比微涨0.5%，虽然相比2021年还跌了8%，但资金正在从新加坡和中东回流香港\n2025年全球最大豪宅市场是迪拜，但香港正在追赶\n\n2/ 写字楼：分化明显\n甲级写字楼租金复苏呈现“冰火两重天”：\n- 中环核心区租金同比涨9.2%\n- 港岛东租金同比跌10.6%\n需求主要来自金融业（占44%），现有企业扩张+品质升级\n有趣的是，灵活办公空间需求占比达18%，比想象中强\n“The Henderson”几乎满租，ICC也吸引大量银行和财富管理需求\n\n3/ 库存问题：最坏时刻已过？\n目前库存约2万套，比2021年的1.2万套高，但比高峰期2.8万套明显下降\n库存消化周期已从23.5个月的高点降至11.7个月\n莱坊认为利率不是主要担忧，高库存才是\n\n4/ 投行怎么看？\n该投行维持“具有吸引力”的行业观点\n他们预计2026年利率不变，2\n\n[... middle omitted ...]\n\ntals recovery is nuanced, with Premium Central +9.2% YoY in 1Q26, while rent in Island East declined by 10.6% YoY   \n(-) According to Knight Frank, interest rates are not a cause for worry, bu\n\n[... middle omitted ...]\n\nWharf REIC (1997.HK)</td><td>U (12/13/2024)</td><td>HK$24.34</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R024",
    "title": "市场真正低估的不是需求，而是供给侧的再定价能力",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价能力\n\n关于AI基础设施投资回报的讨论，过去一年几乎都集中在同一个问题上：这些资本开支最终能否产生足够的收入。市场对此的分歧从未消失，但分歧的焦点正在发生一次重要的转移。\n\n某外资投行最新发布的一份深度研报，通过对超大规模云厂商的资本开支进行自下而上的拆解，构建了一个此前很少被系统讨论的分析框架——每GW新增算力容量所能产生的增量收入。这个看似技术性的指标，恰恰是回答“2万亿美元资本开支到底值不值”的关键。\n\n报告的结论值得认真对待：当前市场对AWS和Google Cloud 2027年的收入预期，不仅合理，甚至可能是保守的。而其中最被低估的，是Google Cloud的增长潜力。这不是一个关于“AI需求能否持续”的判断，而是一个关于“当供给瓶颈打开后，收入曲线会以多陡的斜率上升”的命题。\n\n这个判断的底层逻辑并不复杂。当算力容量成为云厂商增长的核心约束时，资本开支的规模本身不再是风险，而是释放被压抑需求的必要条件。真正的问题在于，每一GW新增容量能带来多少收入，以及这个数字在不同厂商之间为何存在显著差异。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 算力容量正在从“成本项”转变为“收入驱动项”\n\n过去两年，市场对超大规模资本开支的担忧，本质上是一种线性思维：更多的资本开支意味着更高的折旧，从而压制利润率。但这份研报提供了一个截然不同的视角——当容量本身是稀缺资源时，资本开支的扩张恰恰是收入加速的前提。\n\n报告的自下而上模型显示，超大规模云厂商在2026年和2027年将分别新增约14GW和20GW的算力容量。这组数字本身并不令人意外，真正有洞察的是其结构：在2027年的新增容量中，约有8GW将被投入AWS和Google Cloud的公有云业务。这意味着，云厂商的收入\n\n[... middle omitted ...]\n\n入可能面临的下行风险。这些细节的讨论往往比结论本身更有价值。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 每GW算力到底能赚多少钱？\n\n**算力变现效率**\n\n**云厂商的隐性盈利密码**\n\n最近看了一份某外资投行对云厂商算力投入与收入关系的拆解，逻辑挺有意思，分享几个核心发现。\n\n**1/ 算力扩张节奏：未来两年加速明显**\n\n研报通过自下而上的测算，预计头部云厂商在2026/2027年分别新增约14GW和20GW的算力容量。其中，AWS和Google Cloud的公有云部分，在26/27年分别约有6GW和8GW的容量投入商用。\n\n简单说，算力基建正在加速落地，不是画饼。\n\n**2/ 每GW能转化多少收入？**\n\n这是最核心的视角。研报把云厂商未来的收入预期，除以新增的算力容量，得出一个关键指标：**每新增1GW算力，对应多少增量收入**。\n\n目前测算结果是：\n- AWS在2027年：每GW约带来**140亿美元**增量收入\n- Google Cloud在2027年：每GW约带来**110亿美元**增量收入\n\n**3/ 这个数字是保守还是乐观？**\n\n研报认为，目前的市场预期很可能偏保守。理由有三：\n\n- 2025年的实际表现已经优于模型假设\n- 一些新兴云厂商（如CoreWeave等）目前每瓦特收入约10\n\n[... middle omitted ...]\n\ngo to https://www.extelinsights.com/voting.\n\n![](images/31ce5b23ffcaa63560b8f54fe02a04253350a768f4a22ac0adda9a1724cca734.jpg)\n\n<details>\n<summary>text_image</summary>\n\nMS | RESEARCH\n2026 EXTEL\n\n[... middle omitted ...]\n\n(03/14/2022)</td><td>$5.77</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$19.40</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$13.84</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "市场低估的不是数字健康2.0的叙事，而是其单位经济模型的可持续性",
    "digest": "[wechat_article.md]\n# 市场低估的不是数字健康2.0的叙事，而是其单位经济模型的可持续性\n\n数字健康领域留给投资者的记忆并不愉快。上一轮IPO浪潮中，大量公司以高增长姿态登陆公开市场，随后迅速陷入增长失速、亏损扩大、估值崩塌的循环。这种“疤痕效应”至今仍深刻影响着机构投资者的风险偏好——当Hinge Health和Omada Health在2024年先后上市时，市场的主流叙事是警惕，而非拥抱。\n\n但一份来自某外资投行的最新研报提出了一个与市场共识截然不同的判断：这批数字健康公司是真正不同的。报告用超过50张图表和详尽的财务拆解，试图证明HNGE和OMDA正在走一条与前辈完全不同的路——不仅增长更可持续，更重要的是，它们的单位经济模型已经开始展现规模化的杠杆效应。\n\n这份报告的核心主张并非简单的“看好数字健康”，而是一个更具体的判断：市场系统性低估了这两家公司在“自保雇主市场渗透加速”和“平台化边际扩张”双重驱动下的盈利弹性。而这背后，是数字健康行业从“讲故事”到“算得清账”的范式转换。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 自保雇主市场的渗透率远未触顶，但市场把早期成功误读为短期冲顶\n\n报告中最值得关注的数据之一，是HNGE和OMDA在其核心市场——自保雇主（self-insured employers）——中的渗透率。截至最新数据，HNGE在自保市场的渗透率约为18%，OMDA约为14%。如果将视野扩大到全险（fully-insured）和Medicare Advantage市场，两家公司的总渗透率仅在10%至11%之间。\n\n这意味着什么？市场普遍担心数字健康公司已经“吃掉了最容易摘的果实”，后续增长将急剧放缓。但报告通过横向对比上一轮数字健康IPO公司上市后的增长轨迹，提出了一个反直觉的结论：HNGE和OMDA在上市第一\n\n[... middle omitted ...]\n\n社群中持续跟踪这些未解问题的进展，并分享更完整的图表和数据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数字健康2.0：新龙头正在跑出来\n\n📈 研究笔记\n\n当上一代玩家还在讲故事，新龙头已经开始用业绩说话\n\n---\n\n**1. 为什么这次不一样？**\n\n某外资投行最新研报指出，数字健康正在进入2.0时代。如果之前被数字健康1.0的失败案例吓到，现在可能是重新审视这个赛道的时候了。\n\n核心逻辑很简单：Hinge Health (HNGE) 和 Omada Health (OMDA) 这两家公司，正在用实打实的业绩打破市场的怀疑论。\n\n**2. 三个关键数据点支撑这个判断👇**\n\n**① 市场渗透率还很低，天花板很高**\n- Hinge 在自保市场的渗透率仅18%，全保市场仅3%\n- Omada 在自保市场14%，全保9%，Medicare Advantage仅1%\n- 两家公司整体渗透率都在10%左右\n\n这意味着什么？增长空间还很大，不是零和博弈。\n\n**② 连续超预期，不是偶然**\n两家公司上市后已经连续4个季度beat并上调指引。Hinge在营收、毛利率、EBITDA利润率三个维度都大幅超预期。Omada虽然股价波动较大（受IPO锁定期和解禁影响），但同样交出了超预期的成绩单。\n\n**③ 竞争壁垒在加强**\n\n[... middle omitted ...]\n\ntrated within TAMs, providing a long runway for growth...   \n...underpinned by strong go to market execution, health plan & PBM partnerships and increasingly effective marketing campaigns driv\n\n[... middle omitted ...]\n\n01/2025)</td><td>$16.10</td></tr><tr><td>Veeva Systems Inc (VEEV.N)</td><td>E (02/17/2026)</td><td>$158.54</td></tr><tr><td>Waystar Holding Corp. (WAY.O)</td><td>E (03/30/2026)</td><td>$19.72</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "市场真正在定价的，不是AI本身，而是“谁能在AI时代守住护城河”",
    "digest": "[wechat_article.md]\n# 市场真正在定价的，不是AI本身，而是“谁能在AI时代守住护城河”\n\n上周美国互联网板块整体下跌2%，而标普500和纳斯达克分别上涨约1%。这不是一个简单的“科技股回调”故事。拆开来看，谷歌和Meta分别下跌3%和1%，亚马逊却上涨1%。Booking涨4%，Lyft涨7%，Roblox涨12%。\n\n这些数字背后藏着一个更本质的问题：当市场从“AI主题”转向“AI落地”，它不再问哪些公司有AI故事，而是问哪些公司能把AI转化为可定价的竞争优势。\n\n某外资投行最新发布的北美互联网周报，用一张估值表和一组价格表现数据，揭示了当前市场的真实状态——这不是AI泡沫破裂，而是市场正在对“AI受益者”进行更严格的筛选。筛选的标准，不再是技术叙事，而是商业模式的结构性壁垒。\n\n这份报告没有长篇大论地讨论AI，但它给出的数据，比任何AI专题报告都更说明问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 数字广告巨头正在承受“AI预期”的反噬\n\n过去一周，数字广告板块市值加权平均下跌2.8%。谷歌和Meta是主要拖累。表面看，这是对宏观不确定性的反应。但更深层的原因，是市场开始质疑：这些公司过去几年积累的规模优势，在AI时代是否仍然等同于定价权？\n\n谷歌的搜索垄断地位，Meta的社交广告网络，它们的护城河建立在用户规模和广告主依赖度上。但AI正在改变广告投放的逻辑——从“买位置”到“买转化”，从“覆盖人群”到“预测意图”。如果AI让广告主能够更精准地绕过平台直接触达用户，那么平台的中介价值就会被压缩。\n\n报告没有直接给出这个结论，但数据提供了线索。谷歌的EV/Rev倍数在2026年预期为9.1倍，Meta为6.0倍，两者都低于过去五年的历史中枢。市场不是在为AI定价，而是在为“AI可能削弱平台议价权”定价。\n\n这意味着，数字广\n\n[... middle omitted ...]\n\n资框架感兴趣，欢迎加入，我们一起拆解更多类似报告的底层逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI vs 非AI，市场正在分裂\n\n市场分裂进行时\n\n最近互联网板块整体下跌-2%，但内部走势分化非常明显👇\n\n**1/ 广告巨头承压**\nGOOGL -3%，META -1%\n市场开始质疑：除了超级巨头，还有哪些公司能真正吃到AI红利？\n今年互联网“赢家”名单很短\n\n**2/ 非AI板块反而走强**\nBKNG +4%（旅游）\nLYFT +7%（共享出行）\nRBLX +12%（游戏平台）\nAMZN +1%（电商）\n\n**3/ 核心观察**\n这周的市场走势，本质上是一场“AI vs 非AI”的轮动。\n资金从AI概念股流出，转向基本面扎实、估值合理的非AI板块。\n旅游、共享经济、电商成为资金避风港。\n\n**4/ 关键数据**\n- 数字广告板块：市值加权平均-2.8%\n- 电商板块：+0.8%\n- 旅游板块：+2.1%\n- 共享经济：-2.2%（但个股分化明显）\n\n**5/ 空头信号**\n短期利率最高的股票：LYFT 23%、WW 19%、DUOL 19%\n说明市场对这些标的的看空情绪依然浓厚\n\n**我的理解**\n市场正在重新定价“AI受益者”的范围。不是所有公司都能靠AI讲故事，真正能兑现业绩的才值得溢价。这个分\n\n[... middle omitted ...]\n\n1ba22593fb56603e9e8f733199eaf6c4644112c7534f31218edc43a77ebd0.jpg)\n\n<details>\n<summary>text_image</summary>\n\nMS | RESEARCH\n2026 EXTEL\nALL-AMERICA\nRESEARCH POLL\nVIEW OUR\nANALYSTS >\nMay 26 - Jun\n\n[... middle omitted ...]\n\n(03/14/2022)</td><td>$5.77</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$19.40</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$13.84</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R027",
    "title": "欧洲半导体重估的核心不是周期回暖，而是AI基础设施正把欧洲功率半导体公司推入新的定价框架",
    "digest": "[wechat_article.md]\n# 欧洲半导体重估的核心不是周期回暖，而是AI基础设施正把欧洲功率半导体公司推入新的定价框架\n\n市场对欧洲半导体公司的讨论，过去一年大多集中在“周期何时见底”、“库存何时消化完毕”、“汽车和工业需求何时复苏”。这些问题并非不重要，但它们指向的是同一个方向：回到过去。而一份5月底发布的外资投行深度研报，提供了一个完全不同的叙事框架。\n\n报告的核心判断很明确：英飞凌和意法半导体近期的股价表现（英飞凌年内上涨约100%，意法半导体上涨约14.7%）并非仅仅由周期复苏驱动。真正尚未被市场完全定价的，是两家公司在AI基础设施领域结构性角色的重新定义。报告将英飞凌的数据中心业务估值倍数从周期性的20倍提升至50倍，并首次将意法半导体的光学和低轨卫星业务以36倍独立估值，而将其核心业务仍按18倍估值。这种估值框架的切换，本质上是承认：这些公司的部分业务已经脱离了传统的半导体周期，进入了一个由AI资本开支驱动的结构性增长轨道。\n\n这不是一个关于“什么时候买”的判断，而是一个关于“应该用什么框架来看这些公司”的判断。后者比前者更为根本。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 数据中心功率半导体的价值正从“每瓦多少钱”转向“每机柜多少钱”，英飞凌正在这个链条里占据更核心的位置\n\n报告对英飞凌数据中心业务估值大幅上调的直接原因，是提高了对Rubin Ultra和Feynman机柜功率半导体单机柜价值量的估算。具体来看，英飞凌在Rubin Ultra机柜中的功率半导体单机柜价值被上调至约170美元每千瓦。这个数字本身的意义，不如其背后的结构性变化重要。\n\n报告特别强调了两点：第一，在机柜电源链的第一级——中间总线转换（IBC）环节，氮化镓（GaN）正在成为主导技术。报告将英飞凌在Rubin Ultra机柜IBC环节的单机柜价值估\n\n[... middle omitted ...]\n\n信群里继续讨论，获取完整报告原文和更多结构性机会的深度解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲半导体：结构性重估还有空间\n\n欧洲半导体，不只是周期回春\n\n最近某外资投行发了份欧洲半导体研报，核心逻辑很清晰：周期复苏是明牌，但结构性的增长驱动力被低估了。\n\n1/ 英飞凌：数据中心里的“隐形冠军”\n研报把英飞凌目标价从63欧元上调到91欧元，核心原因是它在AI数据中心里的功率半导体机会。\n- 每机柜功率半导体含量从159美元/kW上调到170美元/kW\n- 主要增量来自GaN（氮化镓）在IBC（中间总线转换）中的渗透，以及Agentic AI带来的CPU增量需求\n- 7月1日德累斯顿“智能功率晶圆厂”开幕是个关键催化剂，可能会更新数据中心收入指引\n\n2/ 意法半导体：光学+低轨卫星的新故事\n目标价从46欧元大幅上调到74欧元，核心是SOTP（分部加总）估值框架的转变。\n- 光学业务受益于数据中心从铜缆转向光互联\n- 低轨卫星（LEO）增长主要来自用户终端，2027年LEO销售预估从10.8亿上调到12.5亿欧元\n- 核心业务给18倍PE，光学/LEO给36倍PE，反映结构性增长溢价\n\n3/ 周期底部的信号很清晰\n两家公司都在说：客户库存更低、交货周期改善、订单在回升。\n虽然英飞凌股价从4月以来涨了94\n\n[... middle omitted ...]\n\nin the data centre and STMicro's exposure to optics and low-earth-orbit satellites.\n\n# Key Takeaways\n\nWe lift our Infineon Technologies PT to €91 on higher power semi dollar content per rack. \n\n[... middle omitted ...]\n\n>E (02/10/2025)</td><td>NKr 201.60</td></tr><tr><td>Soitec SA (SOIT.PA)</td><td>O (03/26/2026)</td><td>€154.20</td></tr><tr><td>VAT Group AG (VACN.S)</td><td>E (03/21/2025)</td><td>SFr 604.60</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R028",
    "title": "原油市场的真正拐点不在价格，而在7月战略储备的断崖式下降",
    "digest": "[wechat_article.md]\n# 原油市场的真正拐点不在价格，而在7月战略储备的断崖式下降\n\n过去两个月，全球战略石油储备（SPR）以每天250万桶的速度释放，这是有史以来最快的战略库存消耗节奏。但市场可能低估了一个关键事实：这个节奏将在7月骤降至每天70万桶，降幅超过70%。这不是预测，而是基于已签署合同和各国政府明确承诺的排期推算。\n\n某外资投行在最新发布的石油手册中，首次系统性地追踪了全球各国SPR的实际释放进度和未来排期。这份报告的价值不在于重复“战略储备释放”这个已知事实，而在于用一个数据拼图回答了一个关键问题：当战略储备这个缓冲垫在7月突然变薄，市场会面临什么？\n\n这份报告的原始数据分散在美国能源部每周石油状况报告、日本经济产业省、Argus、Platts以及各国政府声明中。该投行将这些碎片拼接成一张完整的全球SPR流量表，并给出了一个清晰的判断：市场真正需要关注的不是已经释放了多少，而是即将停止释放多少。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球SPR释放已经消耗了近1500万桶，但真正的压力测试在7月\n\n截至5月25日，全球已确认的战略储备实物释放量约为1.5亿桶。这个数字来自该投行对各国实际提油数据的追踪，与IEA执行董事比罗尔近期提到的每天250万至300万桶的释放速率基本吻合。\n\n但更重要的数字是释放节奏的分布。4月至6月，全球SPR释放量维持在每月7500万至8000万桶的高位，其中美国贡献了约4500万桶，日本约2700万至2900万桶。然而，进入7月后，这一数字将骤降至约2200万桶，8月进一步降至约2000万桶。\n\n这个“7月断崖”并非假设性情景，而是由各国已公布的释放计划时间表所决定的。日本的第二阶段释放将在7月初结束，韩国IEA协调释放已经完成，西班牙的剩余释放量将在6月中旬交付完毕，匈牙利的第二轮\n\n[... middle omitted ...]\n\n们会持续追踪这些关键信号，并在第一时间分享对市场含义的分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球战略石油储备正以史上最快速度释放，但数据分散难追踪。这篇笔记帮你拆解核心逻辑和关键变量。\n\nSPR释放追踪\n正在经历一场前所未有的“泄洪”\n\n全球战略石油储备（SPR）正经历一轮历史级释放，但数据分散，尤其非美国家很难追踪。这篇笔记帮你理清现状和后续关键变量。\n\n1️⃣ 总量与节奏\nIEA宣布释放4.26亿桶，目前实际释放约1.5亿桶，4-6月日均释放250万桶。美国与日本是绝对主力，分别承诺1.33亿桶和约9900万桶。日本释放直接流向炼厂，无法通过货轮数据追踪，常被低估。\n\n2️⃣ 美国释放细节\n美国已签署1.329亿桶合同，实际释放5030万桶。释放节奏基本按计划推进，但第四轮招标认购率仅58%，说明需求在降温。DOE警告：随着库存下降，释放速率会自然衰减，预计从6月起从140万桶/日逐步降至70-90万桶/日。\n\n3️⃣ 7月“断崖”预警\n当前全球SPR释放约250万桶/日，但到7月会骤降至约70万桶/日。日本第二阶段7月初结束，韩国已完成，西班牙6月中旬交付完毕。之后只剩美国第四轮合同在跑，每月约1800万桶。\n\n4️⃣ 三个可能“补位”的因素\n- 美国第五轮招标（概率中等，取决于地缘局势）\n-\n\n[... middle omitted ...]\n\n contracted and 99 mb committed respectively. Japan's releases go direct to refiners, invisible for cargo trackers   \nUS draws hit a record 1.4 mb/d in mid-May. However, DOE has warned lift ra\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R029",
    "title": "市场低估了瑞士央行的“克制”，却高估了日本当局的决心",
    "digest": "[wechat_article.md]\n# 市场低估了瑞士央行的“克制”，却高估了日本当局的决心\n\n在当前的全球外汇市场，一个看似矛盾的现象正在上演：瑞士央行口头干预的强硬表态与日本财务省同样强硬的措辞，引导着市场走向截然不同的定价逻辑。某外资投行最新发布的策略更新报告，通过对两国央行真实行为模式的拆解，提出了一个值得投资者重新审视的判断——市场真正需要关注的，不是两国央行“会不会干预”，而是它们“以什么节奏、什么力度、什么目标去干预”。这个差异，正在为做多瑞郎兑日元的交易提供坚实的基本面支撑。\n\n报告的核心交易建议是：维持做多CHF/JPY，目标206.50，截至6月底。这一判断的背后，是对瑞士央行和日本财务省干预哲学的深度对比。报告没有停留在“谁更强硬”的表层叙事，而是从实际干预数据、通胀预期、官员措辞演变和隐含波动率等多个维度，揭示了两个央行在“干预工具箱”中的真实排序。\n\n这不仅仅是货币对交易的技术判断。对于关注全球宏观资产配置的决策者而言，这组分析提供了一个理解“央行干预时代”的新框架：当口头干预常态化后，真正决定汇率走向的，不是干预的“存在”，而是干预的“边界”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 瑞士央行的口头干预，比实际动作更有信号意义\n\n瑞士央行行长施莱格尔近期讲话中重申了干预意愿，尤其是在中东冲突加剧背景下瑞郎面临的升值压力。这被市场解读为瑞士央行的强硬姿态。但报告通过月度外汇储备数据发现，在3月和4月，经估值调整后的瑞士央行外汇储备并未出现有意义的增加。这意味着，尽管央行表态“愿意干预”，实际动手的力度和频率远低于市场想象。\n\n这种“雷声大雨点小”的模式，恰恰是瑞士央行当前干预哲学的体现。报告指出，施莱格尔在演讲中特别提到一个关键事实：瑞郎实际有效汇率的升值幅度，远小于名义有效汇率。这意味着，从贸易竞争力的角度看，瑞郎\n\n[... middle omitted ...]\n\n告未完全回答的关键问题，结合最新市场数据，进行更深度的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n瑞士央行与日本财务省的外汇博弈\n\nCHF/JPY 交易逻辑拆解\n\n目标206.50，高确信度\n\n---\n\n最近在跟踪某外资投行的一份策略报告，核心是继续持有瑞郎/日元（CHF/JPY）多头仓位，确信度高达4/5（满分5），目标价206.50，6月底前到期。\n\n为什么在大家都在关注日元的时候，选择做多瑞郎？逻辑链是这样的：\n\n1️⃣ 瑞士央行（SNB）的态度：会干预，但不会猛干\nSNB主席Schlegel近期讲话再次确认央行愿意干预汇市，尤其在中东局势升级推升瑞郎升值压力的背景下。但关键细节是——他认为瑞郎实际有效汇率的升值幅度远小于名义有效汇率。这意味着SNB的干预大概率是“有节制的”，目的是缓解升值速度，而非逆转趋势。\n\n2️⃣ 通胀数据不支持激进干预\nSNB在3月会议上上调了通胀预测，但2026年CPI展望依然只有0.5% yoy。通缩压力仍然存在，所以央行不会容忍瑞郎大幅贬值带来的输入性通胀风险。同时Schlegel明确表示不愿回到负利率，这意味着利率工具不会成为打压瑞郎的手段。\n\n3️⃣ 日元这边：口头干预升级，但实际风险还没起来\n日本财务省（MOF）5月19日用了“大胆行动”这样的强硬措辞。但市场更\n\n[... middle omitted ...]\n\n of the Middle East conflict. There has also been little change in tone on FX intervention over the last few months (\"greater\" or \"higher\" willingness to intervene since March). It is difficul\n\n[... middle omitted ...]\n\ninformation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International plc, UK. All rights reserved."
  },
  {
    "id": "R030",
    "title": "人民币中间价模型的真正信号：市场低估了央行“以静制动”的定价权",
    "digest": "[wechat_article.md]\n# 人民币中间价模型的真正信号：市场低估了央行“以静制动”的定价权\n\n当多数市场参与者还在争论人民币是否会突破某个整数关口时，一份来自某外资投行的中间价模型预测给出了一个值得重新审视的信号：模型预测的美元兑人民币中间价为6.7658，较前一日的6.8340低了682个基点，较前一官方即期收盘价也低了142个基点。这并非一个简单的数字变化。它意味着，在当前市场定价中，隐含了央行通过中间价工具进行逆周期调节的空间，而这个空间被市场普遍低估了。\n\n这份研报的核心价值不在于预测一个具体的汇率点位，而在于它揭示了一个被忽视的机制：中间价不仅是市场价格的被动反映，更是政策意图的主动表达。当模型误差持续存在，且逆周期因子被系统性启用时，市场真正需要关注的不是汇率会贬到多少，而是央行选择在什么时点、以何种节奏来重新校准预期。这才是决定未来几个月资产定价逻辑的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测与官方定价之间的“误差”本身就是一个政策信号\n\n研报中最值得注意的并非模型预测的绝对值，而是模型预测与官方中间价之间的差值。数据显示，在引入逆周期因子后，模型预测从6.7658调整为6.7843，两者相差185个基点。这185个基点，就是央行在当前时点主动“压住”的贬值空间。\n\n从历史数据看，模型误差并非随机波动。研报提供的图表显示，模型误差在2025年1月曾达到-1800个基点的极端水平，随后逐步收窄，但在2026年4月和10月又分别出现-600个基点的误差。这意味着，央行并非在所有时点都积极干预，而是在特定压力期选择“出手”。2026年3月19日中间价单日变动达到150个基点，就是一次明确的政策信号。\n\n对于投资者而言，理解这一点至关重要：当模型误差扩大时，不是模型错了，而是政策意图在加强。误差的方向和幅度\n\n[... middle omitted ...]\n\n将在社群中结合更多历史数据和情景分析，深入拆解这些关键假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型在暗示什么？\n\n**6.7658**\n\n模型预测比上次低682个点\n\n---\n\n最近某外资投行发布了一份关于人民币中间价（USD/CNY fix）的模型预测报告，信息量不小。拆解一下核心逻辑，帮助大家理解汇率定价的“黑箱”。\n\n1️⃣ **模型预测大幅下修**\n报告给出了模型预测值：**6.7658**。相比此前的**6.8340**，低了整整682个点。即使与前一日的官方收盘价相比，也低了142个点。这说明模型认为人民币有较强的升值动能。\n\n2️⃣ **“逆周期因子”的调节作用**\n如果加入“逆周期因子”，预测值变为**6.7843**，比此前的固定价低了497个点。这告诉我们，政策工具依然在发挥作用，旨在平滑市场波动，避免汇率出现单边快速走势。逆周期因子就像是给汇率加了一个“缓冲垫”。\n\n3️⃣ **主要贡献货币是哪些？**\n模型预测的变动，并非凭空而来。报告给出了前四大贡献货币（未考虑逆周期因子）：\n- **欧元**：贡献了-36个点（推动人民币升值）\n- **韩元**：贡献了-24个点\n- **澳元**：贡献了-19个点\n- **泰铢**：贡献了-8个点\n可以看到，欧元和亚洲货币的联动\n\n[... middle omitted ...]\n\n![](images/bdd16b900963109fa4df7aa51a06e17ecddb101f3c2be535e8316ece2a8124b0.jpg)\n\n<details>\n<summary>bar</summary>\n\n| Currency | Top 4 weighted contribution to projected change (pips) |\n| :---\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R031",
    "title": "市场真正低估的不是泡沫本身，而是泡沫破裂后的资产轮动规律",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是泡沫本身，而是泡沫破裂后的资产轮动规律\n\n当前全球资产价格正处于一个危险的甜蜜点。标普500指数屡创新高，但只有4%的成份股（21只）在同步创出新高——这个比例与2000年互联网泡沫顶峰时几乎完全一致。与此同时，某外资投行最新发布的周度资金流报告显示，其牛熊指标已从8.0升至8.5，正式进入“卖出信号”区间。自2002年以来，该指标共触发17次卖出信号，全球股票在此后2-3个月的平均跌幅为2-3%，最大回撤可达15-20%。\n\n但真正值得关注的不是这些警示信号本身，而是报告揭示的一个被绝大多数投资者忽视的规律：自1929年以来，每一次重大市场顶部的共同特征，不是泡沫本身的破裂方式，而是破裂后六个月内资产轮动的惊人一致性。这份报告的核心判断是：泡沫破灭后的赢家，几乎总是那些在泡沫最后阶段被羞辱的资产。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 当前市场结构与1929年、2000年的泡沫顶峰高度相似\n\n这不是一个情绪化的判断，而是基于可量化的市场结构数据。报告提供了一个关键数字：标普500指数中，当前有222只股票交易价格较其高点下跌超过20%，109只股票下跌超过40%。换句话说，指数的新高是由极少数股票拉动的，而大部分股票已经陷入技术性熊市甚至更深的跌幅。\n\n这种“指数繁荣、个股萧条”的结构，历史上只在两个时期出现过：1929年9月和2000年3月。1929年的泡沫由公用事业、电信、工业和银行股引领；2000年的泡沫则是一维度的科技股行情，纳斯达克在见顶前六个月翻了一倍，而标普500等权重指数同期却在下跌。\n\n当前的情况更接近2000年。报告指出，科技板块已占到美国投资级债券市场的10%、高收益债券市场的8%。这意味着AI相关投资的“支出者”——那些大规模举债投入算力基础设施的公司——不\n\n[... middle omitted ...]\n\n、以及中国市场资金流出的二阶影响这些报告没有完全展开的话题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n市场越来越窄，但钱还在往一个地方跑\n\n市场集中度逼近历史极值\n\n最近某外资投行出了一份很有意思的研报，讲的是“泡沫后的投资路线图”。虽然不是新结论，但数据很扎实，值得拿出来拆一拆。\n\n📊 先看几个扎眼的数据\n1️⃣ 标普500创新高，但只有21只股票（占比4%）也在创新高。对比2000年互联网泡沫顶部，这个数字是20只。宽度之窄，几乎一样。\n2️⃣ 新兴市场更夸张，1224只股票里只有21只（2%）在历史高点。\n3️⃣ 另一边，222只标普成分股比高点跌了20%以上，109只跌了40%以上。\n4️⃣ 散户端：私人客户股票仓位66%创历史新高，现金仓位9.6%创历史新低。\n\n🧠 核心逻辑：长羞辱，短傲慢\n研报的核心观点是“long humiliation, short hubris”——做多那些在泡沫后期被狠狠羞辱的板块，做空那些泡沫里最傲慢的板块。\n\n历史复盘来看，泡沫破灭后6个月内，10年期国债收益率通常会下降40-50个基点。而表现最好的，往往是泡沫最后几个月跌最惨的防御型板块。\n\n📈 几个历史案例很有参考价值\n- 1929年：泡沫领涨的是公用事业、工业、银行。泡沫后6个月，能源从最大输家变成最大赢家。\n\n[... middle omitted ...]\n\nbble until new Chair Warsh forced to enact tightening of financial conditions.\n\nTale of the Tape: S&P 500 index at new highs but just 21 stocks (4% of SPX) making new highs (was just 20 stocks\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R032",
    "title": "日本医药市场的真正挑战：低药价正在重塑全球药企的竞争版图",
    "digest": "[wechat_article.md]\n# 日本医药市场的真正挑战：低药价正在重塑全球药企的竞争版图\n\n当全球制药巨头把目光投向中国、印度等新兴市场时，一个成熟市场正在悄然失去吸引力，而这对全球医药投资逻辑的冲击可能被严重低估。\n\n某外资投行最新发布的研报揭示了一个令人警醒的趋势：日本已经从2012年全球第二大医药市场，下滑至2024年的第四位，市场规模仅相当于美国的十分之一。更值得关注的是，日本市场的药品价格在主要发达国家中几乎垫底，仅为美国价格的22%，与法国并列最低。\n\n这不是一个简单的市场排名变化。它正在倒逼日本本土药企加速全球化布局，同时也在重新定义全球药企的战略优先级。对于关注医药板块的投资者而言，理解日本药价体系的运作逻辑，比关注任何单一药品的销售数据都更为重要。\n\n这份研报的核心判断是：日本的低药价政策虽然在短期内帮助政府控制了医疗支出，但其长期后果可能是让患者失去获得创新药物的机会，同时迫使日本药企加速向海外转移研发和商业化资源。这背后是一个典型的政策与市场博弈的案例，其演变过程值得每一个关注全球医药格局的人深入理解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日本药价体系的核心逻辑：政府全权控制下的“成本优先”机制\n\n日本的药品定价机制与其他发达国家有本质区别。在日本，几乎所有获批药物都纳入国民健康保险（NHI）体系，由政府直接决定药品的报销价格。这意味着，药企在日本市场几乎没有定价权，只能接受政府设定的价格。\n\n新药定价主要采用两种方式：类比定价法和成本定价法。类比定价法占新药定价的65%，即参照市场上已有的同类药物价格，再根据新药的“创新性”和“有用性”给予一定溢价。理论上，一款真正具有突破性创新的药物可以获得70%-120%的创新溢价，但即便是最高溢价，其绝对价格水平仍然远低于美国市场。\n\n成本定价法则更为棘手。当市场上没\n\n[... middle omitted ...]\n\n会在社群中分享完整报告的解读和原始图表，与大家一起深入探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本药价全球最低，药企在“逼”着出海\n\n日本药价为何全球最低\n\n日本药价到底有多低？只有美国的22%，跟法国并列倒数第一。这个数字背后，是日本从全球第二大药品市场跌到第四，市场规模只有美国的十分之一。\n\n1/ 老龄化逼出来的控费压力\n日本65岁以上人口占比从22%飙升到29%，老年人占了医疗开支的大头。政府债务高企，38%的医疗费还得财政掏钱。控费成了必须做的事，而药费虽然只占医疗总开支的16%，却是最好下手的那块。\n\n2/ 政府握着定价权\n日本几乎所有上市药都走医保报销，政府直接定报销价。药企想卖药，就得接受这个价。定价方式有两种：跟现有药比效果定溢价，或者按成本定价。创新药能拿70-120%的溢价，但65%的新药还是走对比定价这条路。\n\n3/ 年年砍价，创新药除外\n日本每年9月做药价调查，根据药店实际进货价和报销价的差额来调价。2026年调查显示差额只有4.8%，是30年来最低，最终平均砍价0.9%。不过创新药能享受15年价格保护期，直到仿制药上市才被砍。\n\n4/ 卖太好也要被砍\n如果某款药年销售超过1000亿日元，而且超过当初申报峰值预测的1.3-1.5倍，政府有权砍价10-50%。因为很多药后来会批新\n\n[... middle omitted ...]\n\nouet@bernsteinsg.com\n\nCourtney Breen +1 917 344 8407 courtney.breen@bernsteinsg.com\n\nWilliam Pickering, MD +1 917 344 8340 william.pickering@bernsteinsg.com\n\nNandan Kulkarni +91 22 6842 1436 n\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Exports from the Middle East Account for a Large Share of Global Trade in Certain Key Industrial and Agricultural Inputs, Although Their Share of Global GDP is Smaller Middle East Goods Exports to RoW"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Commodity Prices Have Surged In Response to the Supply Shock Reported Price Increases Since Feb 27, 2026"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Crude Inventories Remain Above Historical Levels Despite Rapid Drawdowns; Our Rules of Thumb Capture the Growth Impact of Demand Destruction via Higher Prices"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: A Complete Loss of Middle Eastern Crude Oil Supply Would Likely Lower Global GDP by 2% Effect of a 100% Loss of Middle East Oil Supply on GDP (Ghosh Model)"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Downstream GDP Exposure to Middle East Goods Supply Ranges from $0.3\\%$ in the US to Over $3\\%$ in India, Turkiye and South Korea Effect of a 100% Loss of Middle East Non-Oil Goods Supply on GDP (Ghosh Model)"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: In an Extreme Scenario Where Goods from the Middle East Are Critical for Production and No Opportunities for Substitution Exist, the Growth Impact Would Be Severe Effect of a 100% Loss of Middle East Non-Oil Goods Supp"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 7: The Growth Impact Would Be Much Smaller If Goods That Account for a Trivial Share of Overall Inputs are Non-Critical for Production"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Diverting Supply to Higher Value-Added Industries Could Reduce the Global GDP Hit from $10\\%$ to Less than $1\\%$ Effect of a 100% Loss of Middle East Non-Oil Goods Supply on GDP, by Reallocation Scenario"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Even a Small Degree of Substitutability Between Imports Would Dampen the GDP Hit Substantially"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "To assess the magnitude of the potential growth hit after accounting for these margins of adjustment, we make reasonable assumptions on the bottleneck threshold, ease of reallocation and substitutability of inputs, guided by the academic literature and our own"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Business Surveys Point to Emerging Supply Chain Stress"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Exhibit 13",
    "context": "Exhibit 13: News Reports of Supply Disruptions Have Slowed Somewhat in Recent Weeks but Remain Elevated"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Prices for Exposed Products Have Retraced Following Outsized Gains at the Start of the Conflict"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: Global Emerging Market funds allocation to TW has seen a much sharper rise since 2019, now reaching record high of 22.3% vs. 20% in China, 17% in Korea and 10% in India"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: Global Emerging Market funds allocation to TW has seen a much sharper rise since 2019, now reaching record high of 22.3% vs. 20% in China, 17% in Korea and 10% in India"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: YTD, Taiwan market has seen foreign outflow of -3bn USD due to extreme outflows seen in Mar (-29bn USD). However, since April, it is the only Asian market outside of Japan to see net inflows (Q226 inflows of 16bn USD). G"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "EXHIBIT 6: Taiwan has better return on invested capital than most of Asian peers (except India/Indonesia) and higher that its own 5yr/10yr levels Taiwan ROIC vs. Other Markets"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Taiwan ranks second in the region on innovation, behind China. Its R&D to sale ratio is above the historical averages, which reflects accelerating investment on innovation in the past few years Taiwan R&D % of Sales vs."
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Next 3yr earnings growth expectations is the highest for Taiwan markets. Interestingly, Taiwan and Korea are the only two Asian markets where future earnings expectations are higher than the average seen in the recent 5y"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 9-Exhibit 13) EXHIBIT 9: Taiwan rally has been more led by earnings than multiple-expansion, making it more healthy and less of a bubble Taiwan - Performance vs. 12m Fwd. PE and EPS"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Taiwan has been in a strong upgrade cycle which has supported the market rally. However, now the earnings expectations are already near historical high, making continued upward revisions less sustainable Taiwan - Earning"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Taiwan is trading near record high valuations at 21x fwd. PE ie. +2.6SD above average"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Taiwan is trading at never seen before PB multiples of 4.5x PB ie. +5.2SD above long-term average"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: The equity risk premium in Taiwan has continued to decline since 2022 and it has reached record low levels. While these are not sustainable levels, it is difficult to pin-point what would reverse this"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 14",
    "context": "Exhibit 14-Exhibit 17). EXHIBIT 14: In terms of stock-count, Technology Hardware & Equipment stocks and Semiconductors & Semiconductor Equipment are the biggest sectors followed by Materials, Cap Goods and Banks"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: In terms of market cap, Semiconductors & Semiconductor Equipment accounts for 62% of total market cap, followed by Technology Hardware & Equipment (22%). 10yrs back, these two sectors accounted for 50% of the market. The"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Concentration risk is the highest in Taiwan, where top 10 names account for 72% of their market's value. Similarly, Korean top 10 names accounted for 64% of the market value"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Both stock correlation and factor correlation in Taiwan is going up but factor correlation is now at record high. This highlights that intra market dispersion is getting to extreme levels now"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 18",
    "context": "EXHIBIT 18: Semiconductors & Semiconductor Equipment and Technology Hardware & Equipment are trading at record high valuations. Even Capital goods is stretched, trading above +1SD, while other sectors are cheap"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: The upgrade cycle for Technology Hardware & Equipment and Banks is already at record high, increasing the risk of peak earnings. Semis and CapGoods have also been seeing rising upward revisions, though there is still mor"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Exhibit 20",
    "context": "EXHIBIT 20: High yield and value stocks the best performers in Taiwan in the past three years, while in YTD, growth and momentum have outperformed them both Data as of May 22 $^{th}$ 2026 EXHIBIT 21: Momentum and Quality are the m"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 27",
    "context": "EXHIBIT 22: Given there has been a broad-based re-rating cycle, we look at relative valuations - even then, momentum and quality is trading at record high levels while growth is just shy of 2020 peak Value - Rel. to Market 12m fwd."
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 22: Given there has been a broad-based re-rating cycle, we look at relative valuations - even then, momentum and quality is trading at record high levels while growth is just shy of 2020 peak Value - Rel. to Market 12m fwd."
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 24: Relative to market, upward revisions for price momentum portfolio has already peaked while growth/quality/earnings momentum are at record high. Interestingly, earnings sentiment for value/high yield is now near decade hi"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 24: Relative to market, upward revisions for price momentum portfolio has already peaked while growth/quality/earnings momentum are at record high. Interestingly, earnings sentiment for value/high yield is now near decade hi"
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: Growth is overcrowded while crowding risk in momentum/quality is still not that extreme yet. Value/high yield have fallen to decade low crowding levels Data as of May 22 $^{th}$ 2026 EXHIBIT 26: Relative to market, how"
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 27: Dispersion between growth and value/low vol is at decade high in TW, though there is more room for trends to continue led by earnings momentum Correlation: Taiwan Price Momentum 12m vs. Other factors"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 27: Dispersion between growth and value/low vol is at decade high in TW, though there is more room for trends to continue led by earnings momentum Correlation: Taiwan Price Momentum 12m vs. Other factors"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 1: MoM changes in domestic corporate goods price index"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Figure 2",
    "context": "Figure 2: Inflation rates during the previous oil shocks"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 4: Unit labor costs (ULC) during the previous oil shocks"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Figure 4",
    "context": "Figure 4: Unit labor costs (ULC) during the previous oil shocks"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "Figure 5: BoJ Tankan: Employment condition DI (all industries)"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Figure 6",
    "context": "Figure 6: Policy rates during the oil shocks"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "Figure 7: Degree of monetary accommodation (nominal growth rate - policy interest rate)"
  },
  {
    "figure_id": "F046",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China Five-factor Consumer Activity Z-Score vs. MSCI China YoY change – Consumer activity declined further in April"
  },
  {
    "figure_id": "F047",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4-Exhibit 5). For Intel (INTC, covered by Stacy A. Rasgon), substrate size has increased by 24-36% with each generation (Exhibit 6), vs. 12-23% substrate size increase for AMD (AMD, covered by Stacy A. Rasgon) (Exhibit 7)."
  },
  {
    "figure_id": "F048",
    "report_id": "R008",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Total ABF Substrate Demand: New vs. Old Total ABF Substrate Deman - New vs. Old"
  },
  {
    "figure_id": "F049",
    "report_id": "R008",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: We expect the server CPU market to increase from US\\$33bn in 2025 to US\\$137bn in 2030, accelerating at a 34% CAGR, driven by Agentic AI adoption."
  },
  {
    "figure_id": "F050",
    "report_id": "R008",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: AMD Server CPU: Substrate Size Data of Venice are estimated by Bernstein. EXHIBIT 6: Intel Server CPUs - Substrate Size Growth"
  },
  {
    "figure_id": "F051",
    "report_id": "R008",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: AMD Server CPUs - Substrate Size Growth"
  },
  {
    "figure_id": "F052",
    "report_id": "R008",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: AWS Graviton CPUs: Core Count by Generator AWS Graviton - Core Count by Generation"
  },
  {
    "figure_id": "F053",
    "report_id": "R008",
    "label": "Exhibit 9",
    "context": "Substrate Demand from Server CPUs"
  },
  {
    "figure_id": "F054",
    "report_id": "R008",
    "label": "EXHIBIT 11",
    "context": "Substrate Demand from CPUs"
  },
  {
    "figure_id": "F055",
    "report_id": "R008",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Substrate Demand driven by Server CPUs: New vs. Old Substrate Demand from Server CPUs - New vs. Old"
  },
  {
    "figure_id": "F056",
    "report_id": "R008",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Substrate Demand driven by Total CPUs: New vs. Old Substrate Demand from CPUs - New vs. Old"
  },
  {
    "figure_id": "F057",
    "report_id": "R008",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: We estimate total substrate area to grow 80-100% by generation for Nvidia AI GPUs."
  },
  {
    "figure_id": "F058",
    "report_id": "R008",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: We expect significant ASP increase for substrates as generation migrates. Substrate ASP by Nvidia product generation (indexed to Hopper)"
  },
  {
    "figure_id": "F059",
    "report_id": "R008",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: We expect ABF substrate TAM for Nvidia AI GPUs to continue strong growth of \\~40% over the next 2 years. FY24/3-FY29/3: Nvidia AI GPU"
  },
  {
    "figure_id": "F060",
    "report_id": "R008",
    "label": "Exhibit 17",
    "context": "EXHIBIT 17: ABF Substrate Supply - Total Capacity ABF Substrate Supply - Total Capacity"
  },
  {
    "figure_id": "F061",
    "report_id": "R008",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: ABF Substrate Supply - New vs. Old ABF Substrate Supply - New vs. Old"
  },
  {
    "figure_id": "F062",
    "report_id": "R008",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Ibiden's Capex Plan vs. Bernstein and Consensus Estimates Ibiden Capex Plan"
  },
  {
    "figure_id": "F063",
    "report_id": "R008",
    "label": "EXHIBIT 20",
    "context": "1. Upstream material bottleneck is happening now: While ABF supply has been tight, the key bottleneck to date has largely been upstream materials, particularly T-glass. Major suppliers such as Ibiden are still operating at relatively healthy utilization levels"
  },
  {
    "figure_id": "F064",
    "report_id": "R008",
    "label": "Exhibit 21",
    "context": "EXHIBIT 21: Ajinomoto's 2025 Gunma site expansion increased ABF production capacity by c. 25% by our estimates June 2023 AFT varnish plant Outsourced coating plant"
  },
  {
    "figure_id": "F065",
    "report_id": "R008",
    "label": "Exhibit 22",
    "context": "EXHIBIT 22: Ajinomoto's Gifu ABF produciton capacity is scheduled to come online in 2032, with scope to bring this forward to 2030 as required Ajinomoto Co. Inc. and Ajinomoto Fine Techno Co., Inc. Acquire New Plant Site Land for"
  },
  {
    "figure_id": "F066",
    "report_id": "R008",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 24: Ibiden - ASP for FC Packages"
  },
  {
    "figure_id": "F067",
    "report_id": "R008",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Ibiden: ABF Substrate Price Hike Sensitivity (FY29/3E) EXHIBIT 27: FY21/3-FY28/3E: Ibiden Revenue FY21/3-FY29/3E: Ibiden Revenue"
  },
  {
    "figure_id": "F068",
    "report_id": "R008",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: FY21/3-FY28/3E: Ibiden Gross Profit FY21/3-FY29/3E: Ibiden GP"
  },
  {
    "figure_id": "F069",
    "report_id": "R008",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: FY21/3-FY28/3E: Ibiden Operating Profit FY21/3-FY29/3E: Ibiden OP"
  },
  {
    "figure_id": "F070",
    "report_id": "R008",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Ibiden: Forward P/E Band"
  },
  {
    "figure_id": "F071",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1: YTD performance of Australian Med Device companies versus global Med Device Indices"
  },
  {
    "figure_id": "F072",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: MedTech Industry Organic/CC Revenue Growth"
  },
  {
    "figure_id": "F073",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3: NTM PE Multiples Over Time (Annual Averages)"
  },
  {
    "figure_id": "F074",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Aptamil maintained its No.1 position with market share loss 1.7ppt mom to 21%; A2 lost 0.7ppt market share respectively in Apr International IMF value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F075",
    "report_id": "R013",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Feihe/Yili's Market share on Tmall/Taobao was $15\\% / 9\\%$ in Apr Domestic IMF value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F076",
    "report_id": "R013",
    "label": "Exhibit 5",
    "context": "Exhibit 5: ByHealth's Market share recorded $3.0\\%$ in Apr (0.2ppt gain vs. Mar) Supplements value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F077",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 2: WFE by segment"
  },
  {
    "figure_id": "F078",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Semiconductor capex by segment"
  },
  {
    "figure_id": "F079",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: AirTAC monthly revenue and yoy"
  },
  {
    "figure_id": "F080",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Inovance industrial automation monthly orders and yoy growth"
  },
  {
    "figure_id": "F081",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 6: JMTBA machine tools orders Exhibit 7: SMC: Monthly order trend by region"
  },
  {
    "figure_id": "F082",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Exhibit 8: SMC: Monthly order trend by segment # Whether or not companies possess supply capacity will become the focus point We reiterate our view that the greater focal point going forward for the FA industry and capital market"
  },
  {
    "figure_id": "F083",
    "report_id": "R014",
    "label": "Exhibit 12",
    "context": "Exhibit 13: Yaskawa Electric: EV/EBITDA Premium/Discount"
  },
  {
    "figure_id": "F084",
    "report_id": "R014",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Yaskawa Electric: 12m fwd P/E"
  },
  {
    "figure_id": "F085",
    "report_id": "R014",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Yaskawa Electric: 12m fwd ROE vs. P/B"
  },
  {
    "figure_id": "F086",
    "report_id": "R014",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Yaskawa Electric: 12m fwd EV/EBITDA"
  },
  {
    "figure_id": "F087",
    "report_id": "R014",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Yaskawa Electric: 12m fwd CROCI vs. EV/GCI"
  },
  {
    "figure_id": "F088",
    "report_id": "R014",
    "label": "Exhibit 19",
    "context": "Exhibit 20: Keyence: EV/EBITDA Premium/Discount"
  },
  {
    "figure_id": "F089",
    "report_id": "R014",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Keyence: 12m fwd P/E"
  },
  {
    "figure_id": "F090",
    "report_id": "R014",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Keyence: 12m fwd ROE vs. P/B"
  },
  {
    "figure_id": "F091",
    "report_id": "R014",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Keyence: 12m fwd EV/EBITDA"
  },
  {
    "figure_id": "F092",
    "report_id": "R014",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Keyence: 12m fwd CROCI vs. EV/GCI"
  },
  {
    "figure_id": "F093",
    "report_id": "R014",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Keyence: 24m EPS and P/E"
  },
  {
    "figure_id": "F094",
    "report_id": "R014",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Keyence: Trend of dividend, buyback, and FCF"
  },
  {
    "figure_id": "F095",
    "report_id": "R014",
    "label": "Exhibit 28",
    "context": "Exhibit 29: THK: EV/EBITDA Premium/Discount"
  },
  {
    "figure_id": "F096",
    "report_id": "R014",
    "label": "Exhibit 30",
    "context": "Exhibit 30: THK: 12m fwd P/E"
  },
  {
    "figure_id": "F097",
    "report_id": "R014",
    "label": "Exhibit 31",
    "context": "Exhibit 31: THK: 12m fwd ROE vs. P/B"
  },
  {
    "figure_id": "F098",
    "report_id": "R014",
    "label": "Exhibit 32",
    "context": "Exhibit 32: THK: 12m fwd EV/EBITDA"
  },
  {
    "figure_id": "F099",
    "report_id": "R014",
    "label": "Exhibit 33",
    "context": "Exhibit 33: THK: 12m fwd CROCI vs. EV/GCI"
  },
  {
    "figure_id": "F100",
    "report_id": "R014",
    "label": "Exhibit 36",
    "context": "Exhibit 36: SMC: EV/EBITDA Premium/Discount"
  },
  {
    "figure_id": "F101",
    "report_id": "R014",
    "label": "Exhibit 37",
    "context": "Exhibit 37: SMC: 12m fwd P/E"
  },
  {
    "figure_id": "F102",
    "report_id": "R014",
    "label": "Exhibit 38",
    "context": "Exhibit 38: SMC: 12m fwd ROE vs. P/B"
  },
  {
    "figure_id": "F103",
    "report_id": "R014",
    "label": "Exhibit 39",
    "context": "Exhibit 39: SMC: 12m fwd EV/EBITDA"
  },
  {
    "figure_id": "F104",
    "report_id": "R014",
    "label": "Exhibit 40",
    "context": "Exhibit 40: SMC: 12m fwd CROCI vs EV/GCI"
  },
  {
    "figure_id": "F105",
    "report_id": "R014",
    "label": "Exhibit 41",
    "context": "Exhibit 41: SMC: CROCI factor decomposition # Investment Thesis - SMC (6273.T) We are Neutral-rated on SMC, the world's largest pneumatics manufacturer. While we are taking a positive view of the management team's efforts to furth"
  },
  {
    "figure_id": "F106",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Fanuc: Robot shipment value by destination (GSe)"
  },
  {
    "figure_id": "F107",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Japan: Robot shipment value by destination"
  },
  {
    "figure_id": "F108",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe)"
  },
  {
    "figure_id": "F109",
    "report_id": "R015",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Fanuc: Robot export volume to North America and average export price (GSe)"
  },
  {
    "figure_id": "F110",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe)"
  },
  {
    "figure_id": "F111",
    "report_id": "R015",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Fanuc: Robodrill export volume to China and average export price (GSe)"
  },
  {
    "figure_id": "F112",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: MLCC export volume and average export price(ASP) # Price Target Risks and Methodologies # Price Target Risks and Methodology - Murata Mfg. Valuation methodology: We are Buy rated on Murata Mfg. (on CL) with a 12-month"
  },
  {
    "figure_id": "F113",
    "report_id": "R017",
    "label": "Figure 1",
    "context": "Figure 1: China's offshore wind grid connection from 2022 to 2027E"
  },
  {
    "figure_id": "F114",
    "report_id": "R017",
    "label": "Figure 3",
    "context": "Figure 3: CAGR from 2025 to 2027 of the distributed ESS market"
  },
  {
    "figure_id": "F115",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4: Rising ex-China WTG revenue mix (higher GPM)"
  },
  {
    "figure_id": "F116",
    "report_id": "R017",
    "label": "Figure 5",
    "context": "Figure 5: Polysilicon production cash costs by major players in 2025"
  },
  {
    "figure_id": "F117",
    "report_id": "R017",
    "label": "Figure 6",
    "context": "Figure 6: Net cash of listed polysilicon producers as of 2025"
  },
  {
    "figure_id": "F118",
    "report_id": "R018",
    "label": "Figure 10",
    "context": "VOTE Voting Open May 26 $^{th}$ - June 12 $^{th}$ Please vote for JPM (5 stars) # Retail Trading Activity Overview - Although their overall buying remained moderate (\\~54%ile) amid conflicting US-Iran signals, Tech remained front of retail investors' minds and"
  },
  {
    "figure_id": "F119",
    "report_id": "R018",
    "label": "Figure 12",
    "context": "Figure 1: Retail Investor Daily Purchases by Stocks and ETFs"
  },
  {
    "figure_id": "F120",
    "report_id": "R018",
    "label": "Figure 2",
    "context": "Figure 2: Retail Investors' P&L in ETF As of May 26 $^{th}$"
  },
  {
    "figure_id": "F121",
    "report_id": "R018",
    "label": "Figure 3",
    "context": "Figure 3: Retail Investors' P&L in Single Stocks As of May 26 $^{th}$"
  },
  {
    "figure_id": "F122",
    "report_id": "R018",
    "label": "Figure 4",
    "context": "Figure 4: Impact of AI - Retail vs Institutional Investors Investor Poll Results from JPM NY Quantitative and AI Conference, May 19-20 How will AI impact institutional investors' edge over Retail Investors?"
  },
  {
    "figure_id": "F123",
    "report_id": "R018",
    "label": "Figure 5",
    "context": "Figure 5: Emerging Tech to Surpass NVDA in Market Cap? Investor Poll Results from JPM NY Quantitative and AI Conference, May 19-20 Which company is most likely to first surpass NVIDIA in market cap (whenever that happens...) ?"
  },
  {
    "figure_id": "F124",
    "report_id": "R018",
    "label": "Figure 6",
    "context": "Figure 6: Cumulative Retail Imbalance in Memory Stocks As of May 27 $^{th}$ , in B"
  },
  {
    "figure_id": "F125",
    "report_id": "R018",
    "label": "Figure 7",
    "context": "Figure 7: Cumulative Retail Imbalance in Quantum Stocks As of May 27 $^{th}$ , in B"
  },
  {
    "figure_id": "F126",
    "report_id": "R018",
    "label": "Figure 8",
    "context": "Figure 8: Overall Crowding in Software and Semis - Some Reversal Recently As of May 26 $^{th}$"
  },
  {
    "figure_id": "F127",
    "report_id": "R018",
    "label": "Figure 9",
    "context": "Figure 9: Overall Crowding in Software and Semis"
  },
  {
    "figure_id": "F128",
    "report_id": "R018",
    "label": "Figure 10",
    "context": "Figure 10: Retail Crowding in Software and Semis"
  },
  {
    "figure_id": "F129",
    "report_id": "R018",
    "label": "Figure 11",
    "context": "Figure 11: Shorts Herding in Software and Semis"
  },
  {
    "figure_id": "F130",
    "report_id": "R018",
    "label": "Figure 12",
    "context": "Figure 12: Daily Retail Imbalance in DRAM"
  },
  {
    "figure_id": "F131",
    "report_id": "R018",
    "label": "Figure 14",
    "context": "Figure 14: Daily Retail Imbalance in MU"
  },
  {
    "figure_id": "F132",
    "report_id": "R018",
    "label": "Figure 13",
    "context": "Figure 13: Cumulative Retail Imbalance in ZS"
  },
  {
    "figure_id": "F133",
    "report_id": "R018",
    "label": "Figure 15",
    "context": "Figure 15: Cumulative Retail Imbalance in MU"
  },
  {
    "figure_id": "F134",
    "report_id": "R018",
    "label": "Figure 16",
    "context": "Figure 16: Retail Options Volume in MU"
  },
  {
    "figure_id": "F135",
    "report_id": "R018",
    "label": "Figure 18",
    "context": "Figure 18: Daily Retail Imbalance in SNDK"
  },
  {
    "figure_id": "F136",
    "report_id": "R018",
    "label": "Figure 20",
    "context": "Figure 20: Daily Retail Imbalance in NASA"
  },
  {
    "figure_id": "F137",
    "report_id": "R018",
    "label": "Figure 17",
    "context": "Figure 17: Retail Delta and Gamma in MU"
  },
  {
    "figure_id": "F138",
    "report_id": "R018",
    "label": "Figure 19",
    "context": "Figure 19: Cumulative Retail Imbalance in SNDK"
  },
  {
    "figure_id": "F139",
    "report_id": "R018",
    "label": "Figure 21",
    "context": "Figure 21: Cumulative Retail Imbalance in NASA"
  },
  {
    "figure_id": "F140",
    "report_id": "R018",
    "label": "Figure 22",
    "context": "Figure 22: Daily Retail Imbalance in RKLB"
  },
  {
    "figure_id": "F141",
    "report_id": "R018",
    "label": "Figure 24",
    "context": "Figure 24: Daily Retail Imbalance in PL"
  },
  {
    "figure_id": "F142",
    "report_id": "R018",
    "label": "Figure 26",
    "context": "Figure 26: Daily Retail Imbalance in FLY"
  },
  {
    "figure_id": "F143",
    "report_id": "R018",
    "label": "Figure 23",
    "context": "Figure 23: Cumulative Retail Imbalance in RKLB"
  },
  {
    "figure_id": "F144",
    "report_id": "R018",
    "label": "Figure 25",
    "context": "Figure 25: Cumulative Retail Imbalance in PL"
  },
  {
    "figure_id": "F145",
    "report_id": "R018",
    "label": "Figure 27",
    "context": "Figure 27: Cumulative Retail Imbalance in FLY"
  },
  {
    "figure_id": "F146",
    "report_id": "R018",
    "label": "Figure 28",
    "context": "Figure 28: Daily Retail Imbalance in ASTS"
  },
  {
    "figure_id": "F147",
    "report_id": "R018",
    "label": "Figure 30",
    "context": "Figure 30: Retail Options Volume in ASTS"
  },
  {
    "figure_id": "F148",
    "report_id": "R018",
    "label": "Figure 29",
    "context": "Figure 29: Cumulative Retail Imbalance in ASTS"
  },
  {
    "figure_id": "F149",
    "report_id": "R018",
    "label": "Figure 31",
    "context": "Figure 31: Retail Delta and Gamma in ASTS"
  },
  {
    "figure_id": "F150",
    "report_id": "R018",
    "label": "Figure 34",
    "context": "Figure 34: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Note: The last weekly data point includes a holiday, May 25 $^{th}$ ."
  },
  {
    "figure_id": "F151",
    "report_id": "R018",
    "label": "Figure 33",
    "context": "Figure 33: Retail Cumulative Purchases in Mag 7 + PLTR (\\$B)"
  },
  {
    "figure_id": "F152",
    "report_id": "R018",
    "label": "Figure 35",
    "context": "Figure 35: Retail ETF Activity by Themes Buying / Selling of ETFs aggregated by themes, in \\$B. Note: The last weekly data point includes a holiday, May 25 $^{th}$ ."
  },
  {
    "figure_id": "F153",
    "report_id": "R018",
    "label": "Figure 37",
    "context": "Figure 37: Increasing Squeeze Risk in Meme Stocks: Retail Selling in High Short Interest Names Positive Slope = Opposite Positioning (Heightened Risk of Short Squeeze or Retail Losses); Negative Slope = Similar Positioning (Diffusi"
  },
  {
    "figure_id": "F154",
    "report_id": "R018",
    "label": "Figure 38",
    "context": "Figure 38: Retail Activity in FLO"
  },
  {
    "figure_id": "F155",
    "report_id": "R018",
    "label": "Figure 39",
    "context": "Figure 39: Retail Activity in PATH"
  },
  {
    "figure_id": "F156",
    "report_id": "R018",
    "label": "Figure 40",
    "context": "Figure 40: Retail Activity in SLG"
  },
  {
    "figure_id": "F157",
    "report_id": "R018",
    "label": "Figure 41",
    "context": "Figure 41: Retail Trading Volume Share for Single Stocks"
  },
  {
    "figure_id": "F158",
    "report_id": "R018",
    "label": "Figure 43",
    "context": "Figure 43: Retail Trading Dollar Share for Single Stocks"
  },
  {
    "figure_id": "F159",
    "report_id": "R018",
    "label": "Figure 45",
    "context": "Figure 45: Median Retail Trading Share for Single Stocks"
  },
  {
    "figure_id": "F160",
    "report_id": "R018",
    "label": "Figure 42",
    "context": "Figure 42: Retail Trading Volume Share for ETFs"
  },
  {
    "figure_id": "F161",
    "report_id": "R018",
    "label": "Figure 44",
    "context": "Figure 44: Retail Trading Dollar Share for ETFs"
  },
  {
    "figure_id": "F162",
    "report_id": "R018",
    "label": "Figure 46",
    "context": "Figure 46: Median Retail Trading Share for ETFs"
  },
  {
    "figure_id": "F163",
    "report_id": "R018",
    "label": "Figure 47",
    "context": "Figure 47: Top 40 Equities with Most Delta Bought (in \\$Mn)"
  },
  {
    "figure_id": "F164",
    "report_id": "R018",
    "label": "Figure 48",
    "context": "Figure 48: Top 40 Equities with Most Delta Sold (in \\$Mn)"
  },
  {
    "figure_id": "F165",
    "report_id": "R018",
    "label": "Figure 49",
    "context": "Figure 49: Top 40 Equities with Most Gamma Bought (in \\$Mn)"
  },
  {
    "figure_id": "F166",
    "report_id": "R018",
    "label": "Figure 50",
    "context": "Figure 50: Top 40 Equities with Most Gamma Sold (in \\$Mn)"
  },
  {
    "figure_id": "F167",
    "report_id": "R018",
    "label": "Figure 51",
    "context": "Figure 51: Daily Retail Imbalance in IBM As of May 26 $^{th}$"
  },
  {
    "figure_id": "F168",
    "report_id": "R018",
    "label": "Figure 52",
    "context": "Figure 52: Cumulative Retail Imbalance in IBM As of May 26 $^{th}$"
  },
  {
    "figure_id": "F169",
    "report_id": "R018",
    "label": "Figure 53",
    "context": "Figure 53: Daily Retail Imbalance in GFS As of May 26 $^{th}$"
  },
  {
    "figure_id": "F170",
    "report_id": "R018",
    "label": "Figure 54",
    "context": "Figure 54: Cumulative Retail Imbalance in GFS As of May 26 $^{th}$"
  },
  {
    "figure_id": "F171",
    "report_id": "R018",
    "label": "Figure 55",
    "context": "Figure 55: Daily Retail Imbalance in IONQ"
  },
  {
    "figure_id": "F172",
    "report_id": "R018",
    "label": "Figure 56",
    "context": "Figure 56: Cumulative Retail Imbalance in IONQ"
  },
  {
    "figure_id": "F173",
    "report_id": "R018",
    "label": "Figure 57",
    "context": "Figure 57: Daily Retail Imbalance in QUBT"
  },
  {
    "figure_id": "F174",
    "report_id": "R018",
    "label": "Figure 58",
    "context": "Figure 58: Cumulative Retail Imbalance in QUBT"
  },
  {
    "figure_id": "F175",
    "report_id": "R018",
    "label": "Figure 59",
    "context": "Figure 59: Daily Retail Imbalance in ARQQ"
  },
  {
    "figure_id": "F176",
    "report_id": "R018",
    "label": "Figure 60",
    "context": "Figure 60: Cumulative Retail Imbalance in ARQQ"
  },
  {
    "figure_id": "F177",
    "report_id": "R018",
    "label": "Figure 61",
    "context": "Figure 61: Daily Retail Imbalance in QBTS"
  },
  {
    "figure_id": "F178",
    "report_id": "R018",
    "label": "Figure 62",
    "context": "Figure 62: Cumulative Retail Imbalance in QBTS"
  },
  {
    "figure_id": "F179",
    "report_id": "R018",
    "label": "Figure 63",
    "context": "Figure 63: Daily Retail Imbalance in RGTI"
  },
  {
    "figure_id": "F180",
    "report_id": "R018",
    "label": "Figure 64",
    "context": "Figure 64: Cumulative Retail Imbalance in RGTI"
  },
  {
    "figure_id": "F181",
    "report_id": "R018",
    "label": "Figure 65",
    "context": "Figure 65: Daily Retail Imbalance in INFQ"
  },
  {
    "figure_id": "F182",
    "report_id": "R018",
    "label": "Figure 66",
    "context": "Figure 66: Cumulative Retail Imbalance in INFQ"
  },
  {
    "figure_id": "F183",
    "report_id": "R018",
    "label": "Figure 67",
    "context": "Figure 67: Retail Options Trading Share"
  },
  {
    "figure_id": "F184",
    "report_id": "R018",
    "label": "Figure 69",
    "context": "Figure 69: Retail Options Volume (Calls and Puts), Information Technology"
  },
  {
    "figure_id": "F185",
    "report_id": "R018",
    "label": "Figure 71",
    "context": "Figure 71: Retail Options Volume (Calls and Puts), Health Care"
  },
  {
    "figure_id": "F186",
    "report_id": "R018",
    "label": "Figure 68",
    "context": "Figure 68: Retail Options Volume (Calls and Puts)"
  },
  {
    "figure_id": "F187",
    "report_id": "R018",
    "label": "Figure 70",
    "context": "Figure 70: Retail Options Volume (Calls and Puts), Communication Services"
  },
  {
    "figure_id": "F188",
    "report_id": "R018",
    "label": "Figure 72",
    "context": "Figure 72: Retail Options Volume (Calls and Puts), Financials"
  },
  {
    "figure_id": "F189",
    "report_id": "R018",
    "label": "Figure 73",
    "context": "Figure 73: Retail Options Volume (Calls and Puts), Discretionary"
  },
  {
    "figure_id": "F190",
    "report_id": "R018",
    "label": "Figure 74",
    "context": "Figure 74: Retail Options Volume (Calls and Puts), Staples"
  },
  {
    "figure_id": "F191",
    "report_id": "R018",
    "label": "Figure 75",
    "context": "Figure 75: Retail Options Volume (Calls and Puts), Energy"
  },
  {
    "figure_id": "F192",
    "report_id": "R018",
    "label": "Figure 76",
    "context": "Figure 76: Retail Options Volume (Calls and Puts), Materials"
  },
  {
    "figure_id": "F193",
    "report_id": "R018",
    "label": "Figure 77",
    "context": "Figure 77: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F194",
    "report_id": "R018",
    "label": "Figure 77",
    "context": "Figure 77: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F195",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 1: BYD's overseas sales breakdown"
  },
  {
    "figure_id": "F196",
    "report_id": "R020",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Geely's overseas sales breakdown"
  },
  {
    "figure_id": "F197",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Solar products – Price changes"
  },
  {
    "figure_id": "F198",
    "report_id": "R022",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Sugar Price (US/lb): We expect sugar prices to increase to \\$17clb by 2027/28"
  },
  {
    "figure_id": "F199",
    "report_id": "R022",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Ethanol vs Gasoline and Parity: Ethanol is cheap vs gasoline and will attract consumers demand"
  },
  {
    "figure_id": "F200",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Cane crushing went up +123.12% YoY to 40.06Mt Exhibit 2: ATR/ton of cane improved to 116.89kg/t in 2H April, up +6.34% YoY from 109.92kg/t"
  },
  {
    "figure_id": "F201",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Cane crushing went up +123.12% YoY to 40.06Mt Exhibit 2: ATR/ton of cane improved to 116.89kg/t in 2H April, up +6.34% YoY from 109.92kg/t ATR/ton of Cane (kg of ATR)"
  },
  {
    "figure_id": "F202",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Sugar production increased +109.48% YoY to 1.8Mt, with sugar mix of 40.34% down from 45.69% last year and 32.93% in previous report Sugar Production in CS Brazil (mn tons)"
  },
  {
    "figure_id": "F203",
    "report_id": "R022",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Ethanol production increased +105.85% YoY to 2.04bn liters, driven by corn ethanol production of 0.39 liters (+9.4% YoY) and sugar cane ethanol production of 1.65bn liters (+164.0% YoY) Exhibit 5: Total Center South Et"
  },
  {
    "figure_id": "F204",
    "report_id": "R022",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Ethanol production increased +105.85% YoY to 2.04bn liters, driven by corn ethanol production of 0.39 liters (+9.4% YoY) and sugar cane ethanol production of 1.65bn liters (+164.0% YoY) Exhibit 5: Total Center South Et"
  },
  {
    "figure_id": "F205",
    "report_id": "R022",
    "label": "Exhibit 6",
    "context": "Exhibit 6: And Inventory days went to 35 vs 14 same time last year"
  },
  {
    "figure_id": "F206",
    "report_id": "R022",
    "label": "Exhibit 10",
    "context": "Exhibit 10 : S&E Price Parity (Ethanol vs Sugar NY#11): Ethanol parity to sugar converges faster than expected, but given working capital and subsidies we think still likely more attractive to sell ethanol than sugar Exhibit 11 : E"
  },
  {
    "figure_id": "F207",
    "report_id": "R022",
    "label": "Exhibit 10",
    "context": "Exhibit 10 : S&E Price Parity (Ethanol vs Sugar NY#11): Ethanol parity to sugar converges faster than expected, but given working capital and subsidies we think still likely more attractive to sell ethanol than sugar Exhibit 11 : E"
  },
  {
    "figure_id": "F208",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Center South - Crushing (ktons) Exhibit 13: Center South - ATR"
  },
  {
    "figure_id": "F209",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Center South - Crushing (ktons) Exhibit 13: Center South - ATR Center South - ATR"
  },
  {
    "figure_id": "F210",
    "report_id": "R022",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Center South - ATR/ton Center South - ATR/ton"
  },
  {
    "figure_id": "F211",
    "report_id": "R022",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Center South - Sugar Production (ktons) Exhibit 16: Center South - Total Ethanol Production (th I)"
  },
  {
    "figure_id": "F212",
    "report_id": "R022",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Center South - Sugar Production (ktons) Exhibit 16: Center South - Total Ethanol Production (th I) Center South - Total Ethanol Production (th I)"
  },
  {
    "figure_id": "F213",
    "report_id": "R022",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Center South - Ethanol Mix Evolution (%)"
  },
  {
    "figure_id": "F214",
    "report_id": "R022",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Center South - Total Corn Ethanol Production (th I) Center South - Total Corn Ethanol Production (th l)"
  },
  {
    "figure_id": "F215",
    "report_id": "R022",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Center South - % Ethanol from Cane # Valuation Methodology and Risks # ADECOAGRO S.A. (AGRO.N) In our bull case, we assume Profertil generates US\\$335 million in EBITDA, supported by a urea price of US\\$490/ton and gas"
  },
  {
    "figure_id": "F216",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Knight Frank's Residential Market Outlook in 2026 Exhibit 2: Grade-A Office Rental Change YoY MS ASIA LIMITED+ Praveen K Choudhary"
  },
  {
    "figure_id": "F217",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Our Bottoms Up Analysis Shows Hyperscalers Are Set to Bring on \\~14GW/20GW of Incremental Capacity in '26/'27..."
  },
  {
    "figure_id": "F218",
    "report_id": "R024",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ... with \\~3 GW/3.5 GW to be added at Google Cloud in '26/'27, and 3.5 GW/\\~5 GW at AMZN"
  },
  {
    "figure_id": "F219",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We See Revenue Acceleration Ahead at All Hyperscalers..."
  },
  {
    "figure_id": "F220",
    "report_id": "R024",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ...which implies \\$11-\\$14bn of Incremental Revenue/Incremental GW for AWS/GCP...which seems conservative, and Google Cloud in '27 arguably looking the most conservative"
  },
  {
    "figure_id": "F221",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Hinge and Omada posted above-average growth in their first year as public companies..."
  },
  {
    "figure_id": "F222",
    "report_id": "R025",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...With Hinge screening favorably and Omada in-line on GM..."
  },
  {
    "figure_id": "F223",
    "report_id": "R025",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ...And Hinge well ahead on EBITDA margin and Omada below First Year EBITDA Margin"
  },
  {
    "figure_id": "F224",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Hinge Health TAM Penetration"
  },
  {
    "figure_id": "F225",
    "report_id": "R025",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Omada Health TAM Penetration"
  },
  {
    "figure_id": "F226",
    "report_id": "R025",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Hinge continues to screen as 2-3x the size of next largest competitor Sword based on monthly app downloads Exhibit 7: Omada has broken away from the pack on monthly app downloads, highlighting increasing momentum for i"
  },
  {
    "figure_id": "F227",
    "report_id": "R025",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Hinge continues to screen as 2-3x the size of next largest competitor Sword based on monthly app downloads Exhibit 7: Omada has broken away from the pack on monthly app downloads, highlighting increasing momentum for i"
  },
  {
    "figure_id": "F228",
    "report_id": "R025",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Hinge screens above peers and Omada slightly below on revenue growth in the year after IPO..."
  },
  {
    "figure_id": "F229",
    "report_id": "R025",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ...With both companies demonstrating stronger GM performance... Second Year Gross Margin"
  },
  {
    "figure_id": "F230",
    "report_id": "R025",
    "label": "Exhibit 10",
    "context": "Exhibit 10: ...And Hinge EBITDA margins well above and Omada in-line Second Year EBITDA Margin"
  },
  {
    "figure_id": "F231",
    "report_id": "R025",
    "label": "Exhibit 11",
    "context": "Exhibit 11: First Earnings Report"
  },
  {
    "figure_id": "F232",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Second Earnings Report"
  },
  {
    "figure_id": "F233",
    "report_id": "R025",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Third Earnings Report"
  },
  {
    "figure_id": "F234",
    "report_id": "R025",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Fourth Earnings Report"
  },
  {
    "figure_id": "F235",
    "report_id": "R025",
    "label": "Exhibit 15",
    "context": "Exhibit 15: First Earnings Report"
  },
  {
    "figure_id": "F236",
    "report_id": "R025",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Second Earnings Report"
  },
  {
    "figure_id": "F237",
    "report_id": "R025",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Third Earnings Report"
  },
  {
    "figure_id": "F238",
    "report_id": "R025",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Fourth Earnings Report"
  },
  {
    "figure_id": "F239",
    "report_id": "R025",
    "label": "Exhibit 19",
    "context": "Exhibit 19: First Earnings Report"
  },
  {
    "figure_id": "F240",
    "report_id": "R025",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Second Earnings Report"
  },
  {
    "figure_id": "F241",
    "report_id": "R025",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Third Earnings Report"
  },
  {
    "figure_id": "F242",
    "report_id": "R025",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Fourth Earnings Report"
  },
  {
    "figure_id": "F243",
    "report_id": "R026",
    "label": "Exhibit 4",
    "context": "Exhibit 4: NTM EV/EBITDA for AMZN/GOOGL/META vs. Historical Averages Exhibit 5: Internet names fell $-2\\%$ last week (SPX/NDX $+1 / + 1\\%$ )"
  },
  {
    "figure_id": "F244",
    "report_id": "R026",
    "label": "Exhibit 6",
    "context": "Exhibit 6: NTM EV/EBITDA Multiples Are +1%/-4% vs. 5/10-Year Averages..."
  },
  {
    "figure_id": "F245",
    "report_id": "R026",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ... and NTM EV/Sales Multiples Are +26%/+30% vs. 5/10-Year Averages Last 5-Year Average: 4.2x"
  },
  {
    "figure_id": "F246",
    "report_id": "R026",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Digital Media: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~36%, on Average Digital Media"
  },
  {
    "figure_id": "F247",
    "report_id": "R026",
    "label": "Exhibit 9",
    "context": "Exhibit 9: eCommerce: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~30%, on Average ecommerce"
  },
  {
    "figure_id": "F248",
    "report_id": "R026",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Video Games: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~17%, on Average Video Games"
  },
  {
    "figure_id": "F249",
    "report_id": "R026",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Travel / Shared Economy / Real Estate Tech: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~44%, on Average Travel / Shared Economy + Real Estate Tech"
  },
  {
    "figure_id": "F250",
    "report_id": "R027",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Infineon IBC Solutions ```mermaid graph LR"
  },
  {
    "figure_id": "F251",
    "report_id": "R027",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Rubin Ultra Power Semi Content by Element Rubin Ultra Power Semi Content by Element"
  },
  {
    "figure_id": "F252",
    "report_id": "R027",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Data Centre Revenue Mix Data Centre Revenue Mix"
  },
  {
    "figure_id": "F253",
    "report_id": "R027",
    "label": "Exhibit 8",
    "context": "Exhibit 8: The 2-step margin re-rate cycle The 2 -Step GM% Re-rate"
  },
  {
    "figure_id": "F254",
    "report_id": "R028",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Global SPR releases are running at 2.5 mb/d during Apr-Jun, but are set to fall sharply to 0.7 mb/d in July and August Global strategic stock draws by"
  },
  {
    "figure_id": "F255",
    "report_id": "R028",
    "label": "Exhibit 3",
    "context": "Exhibit 3: US SPR: Four tranches have been awarded so far Exhibit 4: The pace of US SPR releases is tracking close to the schedule implied by the first four tranches US SPR: contracted vs scheduled vs actual lifting Cumulative mb,"
  },
  {
    "figure_id": "F256",
    "report_id": "R028",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Tracked SPR releases average $\\sim 2.5\\mathrm{mb / d}$ during April, May and June, but on current plans, drop off sharply in July Global strategic stock draws by"
  },
  {
    "figure_id": "F257",
    "report_id": "R032",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: Today Japan is the fourth pharmaceutical market and less than a tenth size of the US, tumbling from being the second-biggest market with a third of the US's back in global pharmaceutical market size in USD Bn"
  },
  {
    "figure_id": "F258",
    "report_id": "R032",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Despite its aging population, Japan's pharmaceutical market is weakest among the key markets"
  },
  {
    "figure_id": "F259",
    "report_id": "R032",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Japan's drug pricing is the lowest among the peers Branded drug listing price comparison as % of the US price"
  },
  {
    "figure_id": "F260",
    "report_id": "R032",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Given the unattractive domestic market situation with low drug prices, key Japanese pharma companies are expanding their overseas business to seek growth Revenue (JPY B) Breakdown by Japan vs. Overseas"
  },
  {
    "figure_id": "F261",
    "report_id": "R032",
    "label": "Exhibit 5",
    "context": "EXHIBIT 5: The productivity of Japan's healthcare system is better than that of peer countries, delivering the longest life expectancy without spending more..."
  },
  {
    "figure_id": "F262",
    "report_id": "R032",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: ... yet its fast-growing aging population is challenging healthcare expenditure..."
  },
  {
    "figure_id": "F263",
    "report_id": "R032",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: .. as the older population accounts for the majority of healthcare expenditure Japan healthcare expenditure by age (JPYBn)"
  },
  {
    "figure_id": "F264",
    "report_id": "R032",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: In Japan, 38% of healthcare expenditure is funded by the federal or local government Japan healthcare expenditure breakout by funding"
  },
  {
    "figure_id": "F265",
    "report_id": "R032",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: Drug spending only accounts for 16% of overall healthcare expenditure... Japan healthcare expenditure breakout by category"
  },
  {
    "figure_id": "F266",
    "report_id": "R032",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: ... yet was the fastest growing category within the healthcare expenditure # IN JAPAN, THE GOVERNMENT HAS FULL CONTROL OF DRUG PRICING: PRICING AT LAUNCH AND DOWNWARD ADJUSTMENT WHILE IN THE MARKET # MOST NEW DRUG PRIC"
  },
  {
    "figure_id": "F267",
    "report_id": "R032",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: # of new drug approvals has been declining in Japan while growing in the US and EU"
  },
  {
    "figure_id": "F268",
    "report_id": "R032",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: R&D spend in Japan is declining while increasing elsewhere Pharmaceutical R&D expenditure in the US, EU, Japan and China in USD Mn"
  }
]