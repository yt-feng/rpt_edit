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
    "title": "钢铁下游的真实信号：不是全面复苏，而是结构性分化正在加速",
    "digest": "[wechat_article.md]\n# 钢铁下游的真实信号：不是全面复苏，而是结构性分化正在加速\n\n五月的钢铁下游PMI数据出来了。综合指数50.66%，环比微升0.22个百分点，同比上升0.85个百分点。单看这个数字，很容易得出“需求在回暖”的结论。但如果只读到这一层，就错过了这份报告真正想传递的信息。\n\n某外资投行最新发布的这份中国钢铁下游PMI月度追踪，覆盖了建筑、机械、汽车、造船、家电、基建六大终端行业。数据呈现的图景远比“复苏”二字复杂。五月PMI的整体回升，背后是不同行业在截然不同的驱动力下走向分化。建筑行业的新订单指数创下52.3%的近期高点，但生产指数却在下降；机械行业连续第二个月保持51%以上的强劲读数，但内部子行业冷热不均；汽车行业环比改善幅度最大，但原材料成本压力已经开始侵蚀下游信心。\n\n把这些碎片拼在一起，一个更清晰的判断浮现出来：市场真正需要关注的，不是总量的边际改善，而是结构性分化如何重塑钢铁需求的基本面，以及这种分化对产业链定价权的深远影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 建筑业的“新订单悖论”暴露了需求质量的关键差异\n\n建筑行业五月PMI综合指数50.7%，环比微升0.1个百分点。但拆开来看，新订单指数52.3%，环比上升1.2个百分点，同比上升2.5个百分点——这是近几个月来最强劲的新订单读数。与此同时，生产指数却环比下降1.2个百分点至50.1%。\n\n新订单在加速，生产却在减速。这组数据放在一起，揭示了一个关键的结构性特征：新增订单的“质量”正在发生变化。报告明确指出，五月新增订单主要来自“短周期、快回款”的项目类型，典型代表是工厂和仓库。这类项目的特点是建设周期短、资金周转快，但单体用钢量有限，且对钢材品种的规格要求相对标准化。\n\n相比之下，传统意义上的长周期基建项目、大型住宅开发项目，在新订单\n\n[... middle omitted ...]\n\n。我们会在群里分享完整的原始报告图表和更细分的行业数据拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月钢需回暖，哪些赛道在领跑？\n\n钢需回暖，分化明显\n\n📊 5月钢铁下游PMI出炉\n综合指数50.66%，环比微升0.22ppt\n景气度在传统旺季中稳步回升\n但不同行业冷热不均，我们拆开看看👇\n\n🔧 **机械：最稳的“优等生”**\nPMI 51.01%，环比+0.31ppt，同比+1.67ppt\n机床和变压器市场订单火爆\n工程机械、重机保持平稳\n农机因春耕结束，需求走弱\n整体生产销售节奏持续向好\n\n🚗 **汽车：促销拉动效果明显**\nPMI 50.84%，环比跳升1.6ppt\n五一假期+车展+厂家折扣，新订单回暖\n新能源车继续跑赢燃油车\n出口仍是关键驱动力\n原材料采购维持“按需购买”节奏\n\n🏗️ **建筑：喜忧参半的旺季**\nPMI 50.71%，环比+0.15ppt\n利好：传统赶工期，项目加速推进\n利空：部分地区雨天影响施工进度\n新订单改善集中在短周期、快回款项目\n（比如厂房、仓库）\n原材料价格小幅上涨，下游按需采购\n\n🚢 **造船：高景气但订单平稳**\nPMI 50.03%，环比+0.23ppt\n产能依然紧张，利用率维持高位\n新订单主要来自VLCC和货船\n研报提到：301调查暂停可能带来海外订单催化\n（这\n\n[... middle omitted ...]\n\nwhich might delay progress. New orderbook trended better, mainly on projects with short cycles and quick payback periods (i.e., factories and warehouses). Raw-material prices were slightly up \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R002",
    "title": "全球通胀的真正转折点不在油价，而在核心通胀的隐性扩散",
    "digest": "[wechat_article.md]\n# 全球通胀的真正转折点不在油价，而在核心通胀的隐性扩散\n\n全球通胀格局正在经历一个被市场普遍低估的结构性切换。某外资投行最新发布的《全球通胀监测报告》显示，2026年4月全球整体通胀率已攀升至接近3%，较冲突爆发前上升了近一个百分点。乍看之下，这是能源价格冲击的延续——能源通胀飙升是主要推手。但真正值得关注的信号隐藏在更深处：全球核心通胀在表面上“持平于2.3%”的平静水面下，该行已对预测范围内的多个经济体核心通胀预期进行了上调，中位数上调幅度约为0.5个百分点。美国与欧元区的核心通胀预测分别上调了约0.4个百分点。\n\n这意味着什么？能源价格是导火索，但真正的火药桶是核心通胀正在积蓄的、尚未被充分定价的扩散压力。市场目前对通胀的判断，可能仍停留在“油价驱动的暂时性波动”这一框架内，而忽略了通胀从能源向核心领域传递的机制正在重新启动。这一判断如果成立，将对全球资产定价、央行政策路径以及企业定价策略产生深远影响。\n\n报告提供了一个关键的时间窗口：当前全球核心通胀仍处于2.3%的低位，但上调预期已经出现。这恰恰是投资者最容易误判的阶段——数据尚未全面恶化，但趋势的种子已经埋下。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源通胀不是故事的全部，核心通胀的“隐性上调”才是真正的预警信号\n\n报告中最值得细读的不是4月整体通胀率接近3%这个数字，而是该行在核心通胀预测上的操作。全球核心通胀4月同比持平于2.3%，表面上延续了此前的温和表现。但该行明确表示，已对“我们预测范围内的国家”上调了核心通胀预期，中位数上调约0.5个百分点。\n\n这种“数据持平、预测上调”的组合，本身就是一种强烈的信号。它意味着该行的分析师认为，当前的核心通胀读数低估了未来的上行压力。原因可能包括：能源成本向核心商品和服务的传导尚未完全体\n\n[... middle omitted ...]\n\n图表以及该行的完整预测路径，都值得在更深入的讨论中逐一审视。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球通胀正在“悄悄加速”\n\n4月通胀逼近3%\n\n4月全球整体通胀率接近3%，比冲突爆发前高了近一个百分点。\n\n主要推手是能源价格大涨，油价走高正在传导到终端消费。\n\n亚洲经济体如菲律宾、泰国、越南的通胀上调幅度最大。\n\n---\n\n1️⃣ 核心通胀稳，但上修压力在\n\n核心通胀（剔除食品和能源）4月持平在2.3%，看似温和。\n\n但多家经济体今年的核心通胀预测已被上修，中位数上调约0.5个百分点。\n\n美国和欧元区核心通胀预测分别上调约0.4个百分点。\n\n说明涨价压力正从能源向更广范围扩散。\n\n---\n\n2️⃣ 结构性差异：亚洲“受伤”最深\n\n新兴市场（不含中国）整体通胀达3.5%，明显高于发达市场。\n\n亚洲多国因高度依赖能源进口，受油价上涨冲击更直接。\n\n中国通胀仅1.2%，处于全球低位，与自身经济周期和能源结构有关。\n\n---\n\n3️⃣ 服务通胀仍在高位\n\n全球服务通胀4月录得2.6%，发达市场达3.0%。\n\n服务价格粘性较强，通常不会快速回落。\n\n如果能源成本持续高企，服务通胀可能更难降下来。\n\n---\n\n4️⃣ 一个值得关注的信号\n\nPPI（生产者价格指数）近期出现明显回升，全球PPI从1.4%升至2.8%。\n\n[... middle omitted ...]\n\netnam. Global core inflation meanwhile was flat at 2.3%, continuing its subdued performance. Even so, we have revised up our core inflation projections in the subset of countries we forecast, \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R003",
    "title": "城市更新的真实规模：市场低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 城市更新的真实规模：市场低估的不是需求，而是供给侧的再定价\n\n当市场仍在争论房地产销售何时见底时，一份关于城市更新的五年规划，可能已经悄悄改变了投资逻辑的底层框架。\n\n昨天，国务院发布了《城市更新十五五规划》。这并非一份普通的政策文件。某外资投行在第一时间发布的研报中给出了一个关键判断：这份规划所隐含的增量投资规模，大约在4到5万亿元人民币，相当于2026-2027年预计房地产固定投资的66%。这个比例，与上一轮棚户区改造高峰期（2015-2019年）的增量投资相对于2014年房地产固投的比例（69%）几乎持平。\n\n换句话说，市场正在寻找的需求支撑，可能并非来自新一轮大规模新建，而是来自对存量资产的系统性价值重估。规划明确提出了从“大规模增量建设”向“挖掘现有城市存量价值”的转型。这不仅仅是方向的调整，它意味着未来五年的房地产投资逻辑，正在被重新定义。\n\n这份报告最值得关注的核心判断是：城市更新带来的不是简单的基建拉动，而是一个供给侧的结构性再定价过程。那些能够将存量资产转化为现金流、将改造能力转化为议价权的企业，将获得超越周期的定价能力。而那些仍然依赖新建规模逻辑的企业，可能会在这一轮中持续承压。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4到5万亿增量投资不是终点，而是起点：供给侧收缩下的对冲逻辑\n\n理解这份规划的分量，需要先理解一个数字的参照系。\n\n根据某外资投行的测算，十五五期间城市更新的增量投资约为4到5万亿元。这个数字如果单独看，可能并不惊人。但放在房地产固定投资持续下行的背景下，其意义完全不同。报告预计，2026-2027年房地产固定投资的年均值约为6.8万亿元。也就是说，城市更新的增量投资将占到同期地产固投的66%。\n\n回顾上一轮棚改高峰期（2015-2019年），当时的增量投资约为6.2\n\n[... middle omitted ...]\n\n，继续讨论这些未解问题，并获取完整报告的原始图表与深度解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n城市更新新五年，藏着多少增量？ 📍\n\n封面标题：城市焕新计划\n副标题：十五五的4-5万亿增量从哪来\n\n---\n\n十五五城市更新规划刚出来，我翻完研报觉得有几个数据特别值得记一下。\n\n这次规划的核心逻辑很清晰：从“大拆大建”转向“存量提质”。目标是把城市从增量扩张模式，切换到安全、绿色、智慧、韧性的新轨道上。\n\n1️⃣ 规模有多大？\n\n研报估算，十五五期间城市更新带来的**增量投资约4-5万亿**（对比十四五）。\n\n什么概念？上一轮棚改集中期（2015-2019）总投约7.5万亿，增量约6万亿+。这次增量相当于2026-2027年预计房地产固投均值的66%，跟上一轮棚改增量占2014年固投的69%很接近。\n\n2️⃣ 重点砸向哪？\n\n从量化目标看，几个方向明显提速：\n- 城市危旧房改造：翻倍到50万套（十四五是25万套）\n- 老旧街区/厂区改造：+67%，到1500个\n- 历史建筑修缮：+50%，到1.5万处\n- 地下管网改造：+约50%，到36.5万公里\n\n同时新增了几个赛道：城市公园绿地改造（2万公顷）、应急避难场所改造（5万处）、住房基础信息数字化率要达95%。\n\n3️⃣ 钱从哪来？\n\n研报梳理了四条路径：\n\n[... middle omitted ...]\n\nheritage preservation and risk prevention. We see several areas of acceleration (esp. the renovation for urban dilapidated housing, old blocks and factory areas, and underground pipeline netwo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "高收益债市场真正低估的不是违约风险，而是评级迁移的“意外率”",
    "digest": "[wechat_article.md]\n# 高收益债市场真正低估的不是违约风险，而是评级迁移的“意外率”\n\n过去半年，全球信用市场最显性的主题是“向质量倾斜”。BB级债券在美欧两个市场均显著跑赢B级债券，B/BB利差比率已逼近历史高位。这是典型的风险偏好收缩信号——投资者在同一个高收益资产类别内部，选择更保守的那一端。\n\n但这份某外资投行最新发布的信用策略报告揭示了一个更微妙的判断：市场的“向质量倾斜”并未完整延伸至IG与HY的交叉地带。BBB与BB之间的利差比率，在两个市场都处于历史中低位区间，并未出现明显的压缩或扩张。这意味着，市场对于“边界地带”的定价，既没有充分反映坠落天使的风险，也没有充分反映上升之星的机会。\n\n报告的核心贡献，是引入了一个基于历史评级迁移行为的分析框架，并据此修正了2026年坠落天使与上升之星的预测。其中最具冲击力的发现是：**自2010年以来，美欧两个市场约有一半的坠落天使，在事件发生前并未被评级机构明确标记为负面展望或降级观察。** 同样的“意外”特征在上升之星一侧更为显著。\n\n换句话说，市场对评级迁移风险的定价，可能系统性低估了“意外”发生的概率。而这一低估，在两个市场之间存在显著的结构性不对称。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美欧市场正在走向截然不同的“净迁移”方向\n\n报告给出的2026年预测数字，本身就讲述了一个清晰的故事。在美国市场，上升之星预测上调至750亿美元（此前为400亿美元），而坠落天使预测为600亿美元。这意味着美国高收益市场将连续多年处于“净流入”状态——更多债券从IG降级进入HY，但更多债券从HY升级回到IG，后者规模更大。\n\n欧洲市场则完全相反。上升之星预测为200亿欧元，坠落天使预测为300亿欧元。如果这一预测兑现，将是2020年以来欧洲市场首次出现坠落天使规模超过上升之星。报\n\n[... middle omitted ...]\n\n图表、方法论细节以及框架的适用边界做更深入的拆解。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球信用债正在上演一场“质量切换”大戏，高收益债里最安全的BB级正在领跑，但投资级和高收益之间的“交叉地带”却暗藏玄机。\n\n封面：质量切换进行时\n副标题：天使坠落与星星升起\n\n最近的市场很有意思，高收益债内部出现了明显的“趋利避害”倾向。BB级债券（高收益里的优等生）持续跑赢B级，这一现象在美欧市场同时发生。背后的逻辑不难理解——面对宏观不确定性，资金选择在高收益资产里“抱紧更安全的”。\n\n但有趣的是，这种“趋利避害”并没有延伸到投资级和高收益的交叉地带。BBB级（投资级里最差的）和BB级（高收益里最好的）之间的利差比值，目前处于历史中低位。这意味着，BBB并没有因为“更安全”而被追捧。\n\n美欧市场在这里出现了分化：\n\n1️⃣ 美元市场：BB/BBB的比值目前定价相对合理。考虑到美国经济增长和通胀的组合比较复杂，这个比值大概率会在当前区间震荡。\n\n2️⃣ 欧元市场：机会可能更大。欧洲面临的能源冲击更严重，经济增长更疲弱，再加上“堕落天使”风险（从投资级跌入高收益）上升，BB级债券未来可能面临更多压力。研报判断，欧元区BBB级债券有望在未来跑赢BB级。\n\n关于“堕落天使”和“明日之星”，有几个反直觉的数据：\n\n[... middle omitted ...]\n\ny contrast, we see scope for more decompression given a more adverse macroeconomic backdrop and incremental technical pressures, including elevated fallen angel risk.   \nWhile ‘generic’ rating\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "市场低估了“风险溢价压缩”的边界，而非降息预期本身",
    "digest": "[wechat_article.md]\n# 市场低估了“风险溢价压缩”的边界，而非降息预期本身\n\n过去三周，全球利率市场经历了一轮显著的反弹。美债长端收益率从4月中旬的高点持续回落，欧洲核心国债同步走强，甚至连英国国债也在政治风险未消的背景下录得强劲周度表现。这轮行情的驱动力是什么？许多市场参与者将其归结为“对美联储降息的重新定价”。但某外资投行最新发布的全球利率策略报告给出了一个更精确、也更有操作含义的判断：这轮反弹的核心驱动力是“风险溢价压缩”，而非政策预期路径的根本性变化。\n\n这个判断之所以重要，因为它直接挑战了当前市场叙事中一个常见的混淆——把“收益率下降”等同于“降息预期升温”。如果报告的分析成立，那么投资者对后续行情的方向、幅度和持仓结构，可能都需要做出实质性调整。报告的核心贡献在于，它用一套清晰的分解框架，拆解了不同市场、不同曲线段上“风险溢价”与“政策预期”各自的贡献度，并据此给出了差异化的交易建议。\n\n以下是我们从这份报告中提炼出的五个关键洞察，以及一个报告尚未完全回答、但值得每一位利率投资者深思的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美债长端的反弹高度依赖风险溢价压缩，政策预期贡献微薄\n\n报告明确指出，近期美国长端收益率的下降，绝大部分体现为国债期限溢价的压缩，而收益率中的“预期成分”贡献非常有限。报告中的模型估算显示，10年期美债收益率从4月中旬高点回落的过程中，期限溢价的压缩贡献了绝大部分变动，而市场对美联储未来利率路径的预期几乎没有变化。\n\n这意味着什么？这意味着当前美债长端的定价，更多地反映的是地缘政治紧张局势缓解带来的“不确定性下降”，而不是市场对美联储货币政策转向的押注。从资产定价的角度看，期限溢价的压缩具有更强的“一次性”特征：一旦市场对冲突风险的定价调整到位，继续压缩的空间就会急剧收窄。报告对此的判断\n\n[... middle omitted ...]\n\n宏观的投资者一起，对报告中的关键假设进行持续跟踪和压力测试。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美债“风险溢价”正在退潮，利率还能跌吗？\n\n风险降温，美债长端利率回落\n\n最近美债长端利率快速下行，核心驱动力是地缘冲突缓和带来的“风险溢价”压缩，而不是市场对美联储降息预期的升温。这波利率曲线走平，背后是市场对不确定性定价的下降，但继续深跌需要新的催化剂。\n\n1/ 美债：长端领涨，但空间有限\n\n过去几周，10年期美债利率下行主要来自“期限溢价”的压缩，利率预期部分贡献较小。曲线持续平坦化。某外资投行认为，长端超涨的逻辑正在变难——估值缺口已修复，风险溢价也已回吐。后续要看到更深的利率下行，可能需要美联储政策路径的风险分布发生变化。劳动力市场数据是关键变量，若薪资和闲置信号温和，短期利率有望走陡。\n\n2/ 欧洲：欧元区利率仍有支撑\n\n欧债跟随全球风险偏好改善而上涨，但核心逻辑更扎实：欧央行6月加息概率高（Schnabel讲话确认），叠加活动数据偏弱和商品价格缓解，欧元区利率仍有下行空间。该行建议继续持有5y5y欧元实际利率多头。主权债利差已大幅收窄，但仍有套利价值，不过进一步压缩的难度在加大。\n\n3/ 英国：曲线有望走陡\n\n英债近期也受益于风险缓和和能源价格回落，曲线牛平。但该行认为，这种由期限溢价压缩驱动的\n\n[... middle omitted ...]\n\neeks—stay long 5y5y EUR real yields. Rates vol should remain lower in Europe, supporting sovereign credit carry despite tight spreads. In the UK, term premium relaxation has probably run its c\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "市场真正低估的不是关税，而是美加贸易谈判的结构性不对等",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是关税，而是美加贸易谈判的结构性不对等\n\n7月1日，美墨加协定的联合审查截止日正在逼近。对于大多数市场参与者而言，这只是一个日历上的标记。但对于持有加元头寸的投资者，这个日期可能意味着一次不对称的风险重定价。\n\n某外资投行最新研报的核心判断是：市场可能低估了USMCA审查对加元的结构性压力，原因不在于关税本身，而在于谈判进程的不对称——美加之间的分歧远大于美墨，而这将转化为加元持续弱势的驱动力。\n\n这份报告的价值不在于预测谈判结果，而在于揭示了一个被忽视的传导机制：贸易政策不确定性如何通过加拿大央行的反应函数，最终沉淀为加元的系统性弱势。这不是一个短期交易机会，而是一个需要重新审视加元定价框架的窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美加谈判的分歧比市场认知的更深，而加元对此更为敏感\n\n历史不会简单重复，但谈判节奏会押韵。报告通过构建“贸易冲突”新闻指数发现，在2018-2019年的原USMCA谈判期间，涉及加拿大的贸易冲突报道占比远超墨西哥——峰值时加拿大为44%，墨西哥仅为9%。当前谈判的新闻覆盖同样显示，美加之间的分歧更为突出。\n\n这不是一个偶然的统计偏差。报告指出，2018年美国与墨西哥的谈判相对顺利，而加拿大直到最后一刻才达成协议。两个独立的双边协议在当时并非不可能。这种结构性差异意味着，加元面临的贸易政策风险敞口远大于墨西哥比索。\n\n更重要的是，报告通过回归分析验证了这一点：2018-2019年间，贸易冲突新闻占比每上升10个百分点，美元/加元月度变化约上升1.5%；而同样的指标对美元/墨西哥比索的解释力度几乎为零（R²仅为0.0005）。这组数据揭示了一个关键洞察：加元是北美贸易政策不确定性的“第一接收器”，而比索的定价更多受其他因素驱动。\n\n对于投资者而言，这意味\n\n[... middle omitted ...]\n\n现松动？这些问题的答案，可能决定了未来几个月的加元交易主线。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nUSMCA谈判被低估了，但加元压力正在聚积\n\n美加墨谈判，加元才是主角\n\n加拿大谈判比墨西哥更难，加元或承压\n\n最近大家都在关注关税，但7月1日USMCA审查截止日正在悄悄靠近。某外资投行最新研报指出，这轮谈判对加元的影响可能比市场预期的要大得多。\n\n1️⃣ 为什么加拿大比墨西哥更难谈？\n\n研报通过构建“贸易冲突”新闻指数发现，2018年原版USMCA谈判时，美加之间的摩擦报道占比远高于美墨。当时美墨很快达成一致，而加拿大直到最后一刻才签字。现在历史似乎在重演——美墨已经开启首轮双边谈判，但美加谈判进度明显落后。\n\n2️⃣ 加元比墨西哥比索更敏感\n\n历史数据验证了一个规律：2018-2019年贸易摩擦升级期间，加元明显走弱，而墨西哥比索受影响有限。研报推测，这轮谈判很可能也是类似格局——加拿大被“重点关照”，加元承受的压力更大。\n\n3️⃣ 贸易冲击如何传导至加元？\n\n关键机制在于加拿大央行的反应。2018年加拿大央行明确表示“利率可能需要维持在低于中性水平，直到贸易不确定性消散”。今年4月声明又提到，新贸易限制可能需要进一步宽松。这意味着贸易冲击会通过“利差”渠道持续影响加元，而不是简单的短期溢价。\n\n4️⃣\n\n[... middle omitted ...]\n\nUSMCA process and the 2025 fentanyl-related tariffs.\n\nWe construct an index of “trade conflict” headlines, measured as a share of total trade-related news articles, which suggests that negotia\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "市场真正低估的不是需求崩塌，而是替代的不可逆性",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求崩塌，而是替代的不可逆性\n\n这份来自某外资投行的大宗商品研究团队的闪存报告，给出了一个看似矛盾但极具穿透力的判断：全球石油需求可能在极短时间内下降了9%，但这一冲击并未引发传统意义上的经济危机。报告作者在实地调研中国后指出，需求下降的幅度约为每日150万桶，而更关键的是，这种下降并非来自经济活动的萎缩，而是来自消费者在价格信号下主动做出的替代选择。\n\n如果这一判断成立，那么当前市场对油价和能源股的定价逻辑可能正在忽视一个结构性变化：石油需求的部分损失，可能永远不会回来了。这并非因为世界找到了完美的替代品，而是因为消费者一旦转向更便宜、更方便的选项，就很难再回头。\n\n报告的核心洞察在于，这次冲击与1973年石油危机有着本质区别。1973年，石油嵌入经济的每一个环节，替代方案几乎不存在，因此危机直接转化为宏观经济灾难。而今天，替代能源基础设施已经相当成熟，消费者和企业面对高价时，不是在“忍受”而是在“切换”。这种切换一旦完成，就会形成新的行为惯性。\n\n以下，我们从五个维度拆解这份报告的核心逻辑，并探讨其中尚未被充分定价的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国需求下降的真正原因不是衰退，而是消费者用脚投票选择了更便宜的替代品\n\n报告最引人注目的发现来自中国。作者指出，中国的汽油和柴油需求在4月和5月出现大幅下滑，但公路运输指标并未出现超出季节性的显著走弱。这意味着，人们并没有停止出行，而是越来越多地使用了不同的交通工具。\n\n证据是清晰的。中国高速公路电动汽车充电量在春节和五一假期期间均创下历史新高。交通运输部数据显示，五一期间平均每日有1540万辆电动汽车上路，占全部车辆的24%，同比上升33%。与此同时，航空出行同比下降6.5%，但铁路出行增长4.6%，公路出行也微增\n\n[... middle omitted ...]\n\n的行业对比、历史复盘，以及基于中国和欧洲高频数据的实时跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n世界少了9%的石油，能正常运转吗？ 🌍\n\n封面：少了9%的石油，世界还好吗？\n\n副标题：中国和欧洲的能源转型正在加速\n\n最近看到一份某外资投行的研报，里面提到一个很有意思的问题：如果全球石油供应突然减少9%，世界还能正常运转吗？\n\n答案可能比你想的更乐观。\n\n**1/ 中国：静悄悄的能源转型**\n\n研报团队去中国调研后发现，中国的石油需求可能下降了9%（约150万桶/天）。但这不是因为经济崩溃，也不是政府强制节能，而是消费者自发选择了更便宜的替代方案。\n\n数据显示，中国高速公路电动车充电量在五一假期首日同比暴增55.6%。交通部估算，五一期间有1540万辆电动车在路上跑，占全部车辆的24%，同比增加33%。\n\n有意思的是，虽然汽油和柴油需求大跌，但公路运输指标并没有明显走弱。唯一的解释是：里程还在，只是换成了不同的动力系统。\n\n**2/ 欧洲：可再生能源正在发挥作用**\n\n2022年的能源危机让欧洲经济受到重创，但这次情况完全不同。即使油价在4-5月接近120美元/桶，欧洲大部分国家的电力价格反而跌入负值区间。\n\n原因是太阳能和风能发电量大幅增长，正在挤压化石能源的空间。\n\n**3/ 哪些需求会永久消失？**\n\n[... middle omitted ...]\n\ny, and no sense of crisis in daily life. Instead, it looks like consumers have made a quiet economic choice. Faced with higher gasoline, diesel and airfare, many seem to have shifted away from\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 29 May 2026 03:14 AM EDT\n\nDisseminated 29 May 2026 07:00 AM EDT"
  },
  {
    "id": "R008",
    "title": "市场真正低估的不是AI融资缺口，而是资本中介结构的重塑",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI融资缺口，而是资本中介结构的重塑\n\n关于AI基础设施投资，市场上最流行的问题之一是：10万亿美元的资本开支，钱从哪里来？这个问题的背后，是一种隐含的担忧——资本市场的深度和流动性，可能不足以支撑一个规模远超云计算周期的投资浪潮。\n\n但某外资投行最新发布的这份研报，给出了一个与市场直觉相反的判断。报告的核心论点并非“钱不够”，而是“钱够，但如何让钱流向正确的地方，才是真正的挑战”。这不仅是关于融资工具的讨论，更是关于全球资本市场正在经历的一次结构性演化。\n\n这篇报告值得关注的信号，不在于它确认了AI投资规模有多大，而在于它系统性地拆解了“融资”这件事本身正在发生的变化。资本不是约束，但资本市场的中间化能力——即如何将不同风险偏好、久期、流动性的资金，匹配到AI基础设施的不同环节——才是决定这一轮投资周期能否持续的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 10万亿美元的投资周期，只占全球资本池的4%\n\n报告开篇就给出了一个令人意外的数据：全球零售和机构资本池总计约256万亿美元。一个10万亿美元的AI投资周期，仅占这一总量的约4%。即便只看美国股市的76万亿美元市值，也远高于所需的融资规模。\n\n这个数字本身并不新鲜。真正重要的是报告提出的一个观察：这些资本池之间几乎不可互换。保险资金偏好长期、有稳定现金流的固收资产，养老金需要兼顾成长性和流动性，主权财富基金则倾向于另类投资和直接持有。不同资本的自然属性，决定了它们在AI基础设施融资中扮演的角色完全不同。\n\n报告的深层含义是：市场讨论的“融资能力”，不应该被简化为“有没有钱”，而应该被追问为“钱愿意以什么样的条件、进入什么样的资产”。这背后涉及的是资产结构设计——收益率、久期、抵押品、流动性、风险分担机制——而不仅仅是资本总量。\n\n[... middle omitted ...]\n\n未解问题，结合更多原始图表和行业数据，做进一步的推演和拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI融资10万亿，钱够用吗？\n\n💰资本不是瓶颈\n\nAI基础设施投资正进入一个前所未有的周期，早期投入已经是上一轮云计算的10倍。市场最关心的问题：钱从哪来？\n\n1️⃣ 全球资本池足够深\n全球可调用的资本池约256万亿美元，AI基建10万亿的投入只占其中4%左右。关键是这些钱会通过不同渠道慢慢流入，而不是一次性抽干市场。\n\n2️⃣ 融资渠道正在进化\n从传统的企业债、股权融资，到资产证券化、私募市场、保险资金，AI基建正在催生一个多元化的融资生态。每个资本池都有自己擅长的位置：\n- 保险资金偏好长期固定收益\n- 养老金可以配置更广的资产\n- 私募股权擅长高风险高回报项目\n\n3️⃣ 真正的瓶颈不是钱\n研报指出，真正的约束是电力和算力。数据中心建在哪、有没有足够的电力配套，这些物理限制比融资更难解决。\n\n4️⃣ 市场空间还很大\n公共债券市场还有17万亿美元的吸收能力，股权市场还有2.6万亿美元。加上二级市场流动性解决方案的快速发展（2025年二级交易量首次突破2000亿美元），资本流通效率在提升。\n\n5️⃣ 需要注意的风险\n电力供应延迟、供应链瓶颈、融资成本上升都可能拖慢进度。长期来看，如果企业AI变现不及预期，或者模\n\n[... middle omitted ...]\n\napital pools appear sufficient to finance the AI build-out, following the \\~\\$1T mobile/cloud capex era.   \nThe key challenge is structuring assets with appropriate return, duration, collatera\n\n[... middle omitted ...]\n\n>O (02/17/2026)</td><td>$47.80</td></tr><tr><td>U.S. Bancorp (USB.N)</td><td>E (09/28/2025)</td><td>$54.45</td></tr><tr><td>Wells Fargo &amp; Co. (WFC.N)</td><td>E (09/28/2025)</td><td>$76.65</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R009",
    "title": "市场误读了监管意图：收紧的不是跨境资金，而是非法账户通道",
    "digest": "[wechat_article.md]\n# 市场误读了监管意图：收紧的不是跨境资金，而是非法账户通道\n\n最近一周，关于监管层收紧内地资金投资香港金融产品的讨论密集出现。部分投资者担心，这可能预示着更广泛的跨境资金管控，甚至影响到正常的银行账户开立和保险销售渠道。\n\n但某外资投行最新发布的一份研报给出了一个截然不同的判断：市场可能过度解读了这次监管动作的意图。该行认为，近期监管收紧的核心目标并非限制跨境资金流动，而是清理非法投资账户和不合规的交易渠道。在人民币持续升值、外汇流入健康的背景下，监管层不仅没有理由实施广泛的跨境资金管控，反而可能在未来逐步扩大合规的跨境投资计划。\n\n这一判断之所以重要，是因为它直接挑战了市场上两种流行的叙事：一是“监管正在全面收紧香港通道”，二是“跨境资金管控将常态化”。如果该投行的分析成立，那么当前市场对相关资产定价中隐含的风险溢价，可能就存在重新定价的空间。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这次监管真正瞄准的，是虚假投资账户而非正常开户\n\n理解这次监管动作的关键，在于区分“投资账户”与“银行账户”两个不同概念。该投行明确指出，香港证监会和香港金管局此次关注的重点，是清理欺诈性投资账户，而不是针对正常的投资账户开立和银行账户服务。\n\n根据香港证监会最新发布的通知，内地客户在香港开立投资账户仍然被允许，只是需要满足一些额外的合规要求。这意味着，监管的意图并非切断通道，而是提高通道的合规标准。此前市场上流传的“全面收紧内地客户开户”的说法，更像是对监管信号的误读。\n\n从监管逻辑上看，这一动作与内地证监会的要求是一致的。香港证监会正在与内地监管机构协同，打击那些利用跨境通道进行非法交易或规避监管的行为。对于合规经营的金融机构和正常投资者而言，这次清理实际上是一个利好——它减少了市场中的“噪音交易者”和潜在的系统性风险\n\n[... middle omitted ...]\n\n资投行的核心研报摘要，帮助您第一时间把握市场定价的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n港股收紧？其实是虚惊一场\n\n不必对资金收紧过度焦虑\n\n最近有朋友问我，港股那边的资金流动是不是收紧了？某外资投行最新的研报给出了一个挺有意思的视角：别慌，这次监管收紧没那么吓人。\n\n研报的核心判断是，近期监管动作主要聚焦在跨境投资账户和交易层面，并没有扩大到普通银行账户和保险销售渠道。换句话说，打击的是“假账户”和“违规交易”，不是一刀切。\n\n1/ 清场，不是关门\n香港证监会和香港金管局这次的重点，是清理欺诈性投资账户，而不是针对正常开户。根据最新通知，内地客户在香港开投资账户依然可行，只是需要满足一些额外要求。这就像商场查假货，不是要关门歇业。\n\n2/ 小票波动，大格局不变\n一些小市值公司可能会受影响，因为流动性差，部分内地投资者担心以后没法从境内下单，提前调整了持仓。但研报认为，香港证监会和内地监管机构在这点上口径是一致的。而且，官方渠道如股票通、债券通、理财通和QDII额度还在扩大，能对冲掉这部分流动性压力。\n\n3/ 人民币升值，收紧没必要\n最关键的逻辑在这里：近期人民币在升值，外汇流入健康，央行甚至在回收境内流动性来平衡资金流入。在这种背景下，监管没必要大动干戈收紧跨境资金。研报反而认为，未来可能会逐\n\n[... middle omitted ...]\n\nlly gradual further broadening of regulated cross-border investment programs over time.\n\nWe think both HK SFC and HKMA's focus is on a clean-up of fraudulent investment accounts without target\n\n[... middle omitted ...]\n\n5.02</td></tr><tr><td>Qifu Technology Inc (QFIN.O)</td><td>O (08/25/2020)</td><td>US$15.37</td></tr><tr><td>Shanghai Pudong Development Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.37</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R010",
    "title": "市场正在重新定价的不是通胀本身，而是通胀风险溢价",
    "digest": "[wechat_article.md]\n# 市场正在重新定价的不是通胀本身，而是通胀风险溢价\n\n过去几周，日本国债收益率曲线中段（Belly）的表现显著优于其他期限。这一现象在表面上看似是对通胀数据的反应，但某外资投行最新研报揭示了一个更深层的逻辑：市场真正在调整的，并非对通胀水平的预期，而是对通胀风险溢价的定价。\n\n这份研报的核心判断是，前期市场过度定价了日本央行“落后于曲线”的风险，而随着实际消费者通胀数据的走弱，这一过度定价正在被修正。更重要的是，这种修正并非一次性事件，而是可能在中东局势的两种演变路径下持续展开。\n\n对于关注全球利率市场、日本资产配置以及央行政策博弈的读者而言，理解这一判断背后的逻辑链条，远比跟踪单一数据点更有价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场焦点已从“前瞻性通胀风险”转向“实际经济数据”\n\n研报指出，此前市场对日本央行可能“落后于曲线”的担忧，主要源于两个信号：一是4月企业商品价格指数（CGPI）出现大幅超预期上行，尤其是石油煤炭和化工品价格的跳升；二是JGBi盈亏平衡通胀率持续走强，强化了市场对第二轮通胀效应的恐惧。\n\n然而，实际消费者价格数据却在讲述一个不同的故事。4月全国CPI数据显示，尽管受能源推动的总体通胀有所加速，但核心核心通胀（剔除能源和生鲜食品）和“美式核心通胀”（剔除所有食品和能源）均出现放缓。同时，Nikkei CPINow指数显示，5月的通缩趋势仍在延续。\n\n这一分化意味着什么？它说明市场此前对通胀风险的定价，更多是基于对“未来可能发生”的担忧，而非对“当下正在发生”的确认。当实际数据开始证伪这一担忧时，市场自然会重新评估通胀风险溢价。\n\n关键洞察在于：市场焦点的切换，意味着投资者需要从“盯着前瞻性指标”转向“盯着实际经济数据”，尤其是消费者端的通胀读数。这一框架调整，对于判断后续\n\n[... middle omitted ...]\n\n条件、过渡债券的供给冲击测算，以及不同情景下的资产配置策略。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本国债曲线的“肚子”在悄悄变硬\n\n市场开始重新定价通胀风险\n\n最近日本国债市场出现了一个有意思的轮动：曲线中段（5-7年期）表现明显强于长端。背后逻辑其实不复杂——市场正在从“担心通胀失控”切换到“盯着真实经济数据”。\n\n1️⃣ 通胀恐慌是怎么起来的？\n4月日本CGPI（企业物价指数）大超预期，石油煤炭和化工品价格跳涨。叠加中东局势紧张，市场一度担心日本央行会被迫加息追赶通胀曲线。盈亏平衡通胀率也跟着走高，仿佛第二轮效应已在路上。\n\n2️⃣ 但消费者物价在说另一个故事\n- 4月全国CPI核心核心（剔除能源和生鲜）和“美式核心”（剔除所有食品和能源）都在放缓\n- Nikkei CPINow指数显示5月仍在通缩趋势中\n- 东京CPI也在印证这个方向\n\n3️⃣ 关键转折点：植田和男的讲话\n5月27日，植田用历史油价冲击做例子，强调“初始条件至关重要”。他明确说：日本没有出现70年代式的工资-价格螺旋，中长期通胀预期只是从接近零温和上升到1.5-2%区间。这话基本就是在给过热的通胀担忧降温。\n\n4️⃣ 中东局势：两个情景都利好中段\n研报的判断很有意思：无论地缘局势是缓和还是升级，中段都有进一步上涨空间。\n- 缓和：\n\n[... middle omitted ...]\n\nrs for a second-round effect.   \nHowever, actual consumer inflation data (excluding temporary factors) have been softer. April nationwide CPI showed slowing in core-core and “US-style” core in\n\n[... middle omitted ...]\n\nents carefully before investing.\n\nThe following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Koichi Sugisaki; Hiromu Uezato.\n\n© 2026 MS"
  },
  {
    "id": "R011",
    "title": "数据中心存储的真正拐点，不在SSD对HDD的替代，而在供应链的再分配",
    "digest": "[wechat_article.md]\n# 数据中心存储的真正拐点，不在SSD对HDD的替代，而在供应链的再分配\n\n市场对存储产业的讨论，长期集中在两个叙事上：一是AI算力爆发带来的企业级SSD需求激增，二是传统HDD被SSD不可逆转地替代。这两个叙事都正确，但都不完整。某外资投行最新发布的日本电子元器件月度追踪报告，提供了一组值得重新审视的信号。2026年4月的数据显示，数据中心用NL HDD出货容量同比增长14.3%，企业级SSD出货容量同比暴增116.7%。两个数字都在增长，但真正值得关注的不是增速本身，而是增速背后的结构性变化——供应链正在被重新分配，而这种分配将决定未来两年哪些公司能真正捕获价值。\n\n这份报告的核心判断是：数据中心存储市场的下一个增长阶段，不再是简单的容量扩张，而是供给侧的再定价。当HDD和SSD都在向更高容量产品迁移时，单位出货量的增速将显著慢于容量增速，这意味着上游零部件供应商的议价能力正在发生根本性转移。那些能够率先将规模优势转化为技术溢价的公司，将在新一轮周期中占据主动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 数据中心存储正在从“二选一”走向“三层共存”，这对上游供应链意味着完全不同的竞争逻辑\n\n市场习惯将HDD和SSD视为对立选项，但TSR的预测数据揭示了一个更复杂的图景。报告显示，TSR将2026年数据中心用企业级SSD出货容量预测上调至476.1EB，同比增长81.3%；同时将2026年NL HDD出货容量预测上调至1,844EB，同比增长30.3%。两个市场都在高速增长，且增速都在加速——一个月前，TSR对2026年SSD的预测还是425.3EB（+62.0%），对NL HDD的预测还是2,004.5EB（+23.1%）。\n\n这组数据意味着什么？数据中心存储正在形成“SSD+HDD+磁带”的三层架构。S\n\n[... middle omitted ...]\n\n需要后续数据来验证。这些动态更新，正是微信群可以提供的价值。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心存储，HDD与SSD谁更猛？\n\n数据中心存储持续走强\n\n某外资投行最新研报解析\n\n最近的电子元器件研报里，我看到一组很有意思的数据——数据中心存储需求正在加速分化，HDD和SSD都在涨，但逻辑完全不同。\n\n1️⃣ 数据中心SSD：容量爆发式增长\n企业级SSD的出货容量，4月同比暴涨116.7%，环比+2.5%。TSR预测2026年全年容量将达到476.1EB，同比+81.3%。这个增速非常惊人，说明AI训练和高速存储需求正在快速释放。\n\n但注意，出货量（颗数）增速远低于容量增速，4月企业级SSD出货量同比+42%，环比-3.7%。这意味着单颗容量在快速提升，高容量产品占比越来越高。\n\n2️⃣ 数据中心HDD：稳中有升\nNL HDD（近线硬盘）4月出货容量同比+14.3%，环比-0.6%。TSR预测2026年NL HDD出货容量1844EB，同比+30.3%。虽然增速不如SSD，但绝对规模仍是SSD的近4倍。\n\n有趣的是，HDD也在走“大容量路线”，氦气盘（He）占比持续提升，4月氦气盘出货量同比+24.8%，而空气盘（Air）同比-21.3%。\n\n3️⃣ 消费级存储：明显降温\nPC、外接和游戏用的非企\n\n[... middle omitted ...]\n\nshipment volume/capacity of both NL HDDs and enterprise SSDs for data center use: We anticipate high production and per/unit capacity growth will continue for both NL HDDs and enterprise SSDs,\n\n[... middle omitted ...]\n\n<tr><td>Nippon Chemi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥5,080</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R012",
    "title": "市场真正低估的不是需求，而是测试环节的结构性瓶颈",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是测试环节的结构性瓶颈\n\n某外资投行近期从台湾调研归来后，发布了一份关于半导体资本设备的研报。表面看，这份报告覆盖了晶圆代工竞争格局、英特尔与三星的复苏、以及英伟达GPU测试需求。但将这些碎片拼在一起，一个更值得关注的信号浮出水面：半导体测试环节正在成为整个产业链最紧的瓶颈，而市场对这一结构性变化的定价可能远远不够。\n\n报告的核心判断并非简单的“需求强劲”。事实上，需求强劲已是共识。真正的新信息在于：测试能力的供给扩张速度，正在系统性落后于芯片复杂度提升的速度。这不仅是短期产能问题，而是将重塑从ATE设备商到OSAT封测厂的竞争格局。\n\n为什么现在重要？因为三个关键变量正在同时收敛。第一，GPU测试时间从Blackwell的约850秒延长至Rubin的约1200秒，单颗芯片对测试设备的需求增加了近40%。第二，CPO（共封装光学）技术的引入，正在创造全新的测试插入环节，而这些环节的设备供应商格局远未确定。第三，英特尔与三星在晶圆代工领域的复苏，虽然目前客户获取仍在进行中，但已开始对OSAT和测试设备产生溢出需求。这三股力量叠加，意味着测试设备市场正在经历一次不亚于EUV光刻机导入时的结构性变革。\n\n这份报告最值得细读的部分，不是它对Teradyne或Advantest的短期订单判断，而是它揭示了一个尚未被充分定价的长期逻辑：在芯片设计复杂度指数级上升的背景下，测试环节的资本密集度将迎来系统性重估。以下五个层次，将逐步拆解这一判断的支撑逻辑与隐含的投资含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 测试环节正在从“成本中心”转变为“产能瓶颈”，其稀缺性将重新定价整个产业链\n\n研报中最具冲击力的一个数据点是：GPU的最终测试时间正在从Blackwell的约850秒攀升至Rubin的\n\n[... middle omitted ...]\n\n更多原始数据与产业链调研信息，持续跟踪测试环节的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片代工暗战：英特尔、三星与测试新变量\n\n代工三国杀，测试卡脖子\n\n最近翻到一份某外资投行的台湾调研笔记，信息量挺大。芯片代工和测试设备这块，竞争格局比想象中更热闹，分享几个核心观察。\n\n**1/ 英特尔：EMIB 比代工更香**\n\n英特尔在代工业务上的进展，比预想中慢。目前苹果可能是唯一高调客户，预计2029年才量产A系列芯片。18A工艺良率大约在50%，还在爬坡。NVDA游戏芯片订单有机会，特斯拉AI6芯片也可能在TeraFab投产前下单，但整体客户获取仍在进行中。\n\n反观EMIB（嵌入式多芯片互连桥接）技术，需求非常强劲。联发科、Trainium等客户都在用它来寻找台积电以外的替代方案。英特尔代工还在挣扎，但先进封装已经成了香饽饽。\n\n**2/ 三星代工：活着，但客户想跑**\n\n三星的代工业务也接到不少客户询价，谷歌很可能在2028年把CPU订单给三星。但挑战在于，几乎所有美国客户都想把订单转移到泰勒工厂，而那里的产能还在建设中。也就是说，客户有意愿，但产能跟不上，这是个甜蜜的烦恼。\n\n**3/ 测试：最大的瓶颈**\n\n测试设备的需求持续超过供给，成了整个链条上的卡脖子环节。\n\nTeradyne在NVD\n\n[... middle omitted ...]\n\ndry TBD. The impression we received was that traction for EMIB is far outpacing Intel's foundry business. On the foundry side, Apple appears to be the only high-profile customer, with the comp\n\n[... middle omitted ...]\n\n>Teradyne Inc (TER.O)</td><td>E (07/30/2025)</td><td>$382.65</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R013",
    "title": "掩模版市场的信号：当成熟芯片需求放缓，真正的分化才刚刚开始",
    "digest": "[wechat_article.md]\n# 掩模版市场的信号：当成熟芯片需求放缓，真正的分化才刚刚开始\n\n半导体设备行业的投资者习惯盯着先进制程的资本开支曲线，却往往忽略了产业链中一个关键环节发出的早期预警信号。某外资投行最新发布的日本半导体设备行业研报，以一家美国掩模版厂商的最新季度业绩为切入点，揭示了一个正在发生的结构性变化：低端芯片的tape-out需求正在延迟，而这一变化对产业链的影响，远比表面上的季度营收miss更为深远。\n\n这份研报的核心判断是：掩模版市场正在经历一次需求结构的再平衡。开发用掩模版需求走弱，量产用掩模版需求维持韧性，但真正值得关注的不是短期波动，而是这一信号对Tekscend等日本掩模版厂商以及整个半导体设备产业链的长期含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 掩模版厂商的业绩miss背后，是低端芯片设计活动的实质性放缓\n\nPhotronics在2月到4月这一季度的营收为2.1亿美元，低于此前2.12亿至2.20亿美元的指引区间。更值得关注的是，下一季度的营收指引进一步走弱至2.07亿美元，环比继续下滑。这不是一次性的季节性波动，而是连续两个季度的走弱。\n\n根据管理层的解释，核心原因有三：晶圆代工厂产能利用率提高后，剩余产能减少，导致代工厂优先安排现有产品的量产而非新芯片的设计导入；存储芯片价格上涨和供应紧张，推迟了新的消费电子产品发布；地缘政治风险则进一步抑制了亚洲地区开发用掩模版的需求。\n\n这三个因素共同指向一个结论：低端消费类芯片的设计活动正在放缓。影响最明显的地区是中国和台湾，这正是全球低端芯片设计最活跃的区域。对于掩模版行业而言，开发用掩模版需求与量产用掩模版需求之间存在一种此消彼长的关系——当产能紧张时，代工厂自然优先保证量产，新项目的tape-out就会被推迟。\n\n这一信号的含义是：低端芯片的库存调\n\n[... middle omitted ...]\n\n和图表，进一步拆解掩模版市场变化对各设备子行业的差异化影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体光罩行业的风向变了？\n\n小厂订单在缩水\n\n一家美国同行暴露了信号\n\n最近读到一份某外资投行关于半导体生产设备的行业报告，里面重点分析了一家光罩（Photomask）公司的业绩，信息量很大。简单拆几个点，跟大家聊聊。\n\n这份报告的核心是从一家美国光罩公司（Photronics）的业绩来观察行业趋势，因为它是日本光罩公司Tekscend的同行。结果发现，这家公司的数据不算好看。\n\n1️⃣ 业绩低于预期，指引也不乐观\n这家美国公司2月到4月的季度销售额是2.1亿美元，低于他们自己给出的2.12-2.2亿的指引区间。更关键的是，他们对下一季度的指引更保守，预计会小幅下滑到2.07亿美元。这说明需求端确实有压力。\n\n2️⃣ 原因不是单一因素，而是三重叠加\n报告指出，业绩走弱背后有三个原因同时起作用：\n- 晶圆代工产能利用率上升，导致工厂优先生产现有成熟产品，而不是给新芯片做设计（tape-out），新设计的需求自然就少了。\n- 存储芯片价格上涨和缺货，推迟了消费电子新品的发布，进一步压低了开发用光罩的需求。\n- 地缘政治风险也让部分亚洲客户（尤其是中国和台湾地区）对低端消费芯片的需求放缓了。\n\n3️⃣ 光罩行业的\n\n[... middle omitted ...]\n\nresults\n\nTekscend's US peer Photronics (PLAB, not covered), announced F2/26 2Q results on the evening of May 28 Japan time. 2Q sales came in at \\$210mn, below the \\$212–220mn guidance range, w\n\n[... middle omitted ...]\n\ntd>Ushio (6925.T)</td><td>O (01/05/2026)</td><td>¥4,114</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R014",
    "title": "市场真正低估的不是地缘风险，而是印尼结构性抛售的持续性",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是地缘风险，而是印尼结构性抛售的持续性\n\n这份来自某外资投行全球外汇策略团队的周度报告，表面上是一份战术交易建议的更新。但真正值得产业决策者和资产配置者关注的，不是短期的点位判断，而是一个正在浮现的结构性信号：印尼正在成为亚洲新兴市场中一个“自我强化的负面循环”的样本。而市场对这一循环的定价，可能才刚刚开始。\n\n报告的核心主张并非关于美伊局势或美联储路径。它指向一个更具体的判断：印尼卢比的弱势，正在从“地缘冲击下的被动贬值”演变为“国内政策选择驱动的主动走弱”。如果这一判断成立，那么当前市场对东南亚资产的风险定价，尤其是对印尼相关敞口的评估，可能需要系统性地重新校准。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及它们对投资者观察框架的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 印尼正在经历的不只是货币贬值，而是一个“政策-资本-评级”的三重负反馈\n\n报告最值得注意的变化，是将做多新加坡元兑印尼卢比（long SGD/IDR）的交易信心水平从4/5上调至最高的5/5。这不仅仅是战术上的加仓，而是策略团队对印尼基本面判断的一次系统升级。\n\n报告列举了七个驱动因素，但真正关键的不是数量，而是它们之间的因果关系。这七个因素并非彼此独立的利空，而是构成了一个闭环：政府推动自然资源出口集中化（通过Danantara机构）引发了私营部门和经济学家的强烈警告，这直接打击了外国直接投资信心；与此同时，更严格的出口收益留存规定（非油气行业100%需存入国有银行）增加了对政府控制经济的担忧；在此基础上，MSCI和FTSE Russell因股权集中度问题剔除印尼股票，预计将导致约17亿美元的被动资金外流，而即将到来的市场准入审查可能进一步将外国可投资因子减半，引发额外约40亿美元的潜在流出。\n\n这个链\n\n[... middle omitted ...]\n\n，需要回到完整报告的图表、数据和情景分析中去寻找。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球央行博弈下，哪些货币在悄悄走强？\n\n**全球货币博弈**\n\n**看懂这5个关键信号就够了**\n\n最近全球汇市波动不小，背后其实是几股力量的拉扯：美伊局势缓和预期、各国通胀数据分化、以及央行政策节奏的差异。我拆解了某外资投行的最新研报，把核心逻辑整理成5个关键信号，帮你快速看懂当下格局。\n\n**1️⃣ 美伊局势是最大变量**\n- 研报认为美伊达成临时协议的概率在上升，若协议落地，油价、美债收益率和美元都可能下行，风险资产会获得支撑\n- 但风险仍在：特朗普未正式签署，伊朗方面也否认已达成最终协议\n- 如果非农数据低于预期的93K，美元反应可能更大\n\n**2️⃣ 亚洲货币：分化明显**\n- **最看多：新加坡元**。GDP增速上修至6%，工业产出超预期，央行7月可能再次收紧货币政策\n- **最看空：印尼盾**。多重压力叠加：出口集中化政策引发外资担忧、评级机构可能下调展望、MSCI指数剔除部分股票导致外资流出\n- 策略上，做多新加坡元/印尼盾的仓位已被上调至最高信心等级\n\n**3️⃣ 人民币：低估是优势**\n- 研报认为人民币仍被低估约10%，基于4种估值模型\n- 华为芯片技术突破、中美关系缓和预期，可能吸引更\n\n[... middle omitted ...]\n\non releases (important given rate hike pricing).   \n- Asia FX: We raise the conviction level on our long SGD/IDR to the maximum 5/5. We maintain short USD/CNH (4/5), short USD/TWD (3/5) and lo\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R015",
    "title": "黄金的真正问题不在利率，而在官方需求的结构性对冲能力正在衰减",
    "digest": "[wechat_article.md]\n# 黄金的真正问题不在利率，而在官方需求的结构性对冲能力正在衰减\n\n黄金近期从每盎司4700美元附近持续回落，与原油价格走势出现明显背离。市场习惯性地将矛头指向实际利率的重新定价——今年以来十年期美债实际收益率已上行48个基点。但这份来自某外资投行的研报揭示了一个更值得警惕的判断：真正约束黄金的，并非利率本身，而是过去两年支撑金价的核心力量——官方部门需求——正在从“对冲利率冲击的缓冲垫”转变为“自身也需要被重新定价的不确定项”。理解这一转变，比预测下一次美联储会议的结果更重要。\n\n报告的核心洞察在于，2022年黄金曾经历270个基点的实际利率飙升，但金价并未崩盘，原因在于同期官方黄金需求出现了716吨的剧烈摆动，有效中和了利率的冲击。然而当前，这一对冲机制正在发生结构性变化：央行购金虽在2026年第一季度超预期，但ETF需求同比萎缩78%。这意味着，黄金价格对利率的敏感度正在回归，而利率本身正被一组更复杂、更持久的通胀因子所支撑。\n\n以下五个层次，将逐一拆解这份报告所揭示的核心逻辑，以及那些尚未被市场充分定价的风险与机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 债券市场的全球性抛售正在重塑黄金的宏观定价框架\n\n报告中一个容易被忽略的细节是，近期债券市场的抛售并非美国独有的现象。在日本、英国和美国三大市场，十年期国债收益率在单周内分别上行21、24和23个基点，这一联动性促使G-7财长会议将其列为正式议题。日本方面，市场对补充预算和能源补贴的担忧导致JGB承压；英国方面，地方选举后政治不确定性上升，市场开始定价潜在的财政宽松与更高债务发行；美国方面，某投行利率策略团队直言，实际利率仍然过低，不足以将通胀拉回2%的目标，甚至不排除十年期美债收益率升至5%的可能性。\n\n这三股力量叠加的结果是，全球债券市场正在\n\n[... middle omitted ...]\n\n专业投资者一起，围绕这些尚未完全解答的关键问题展开深入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n黄金的“新麻烦”是什么？\n\n黄金的新难题\n\n通胀顽固+加息预期，黄金承压\n\n最近黄金的走势有点奇怪，和原油的负相关性突然消失，价格从5月中旬的4700美元/盎司一路下行。背后的逻辑很清晰：市场开始担心通胀不会很快消退，而各国央行必须做出负责任的政策回应。\n\n简单来说，黄金现在面临的新困境，就是“更顽固的通胀”+“更紧缩的货币政策”这个组合拳。\n\n1️⃣ 核心矛盾：实际利率在攀升\n\n今年实际利率已经上升了48个基点，这对黄金这种零息资产来说不是好消息。但有意思的是，某外资投行认为，不能简单把黄金走势和实际利率画等号——2022年实际利率飙升了270个基点，当时却被716吨的官方黄金需求给对冲掉了。\n\n也就是说，黄金的定价逻辑里，央行购金这个变量越来越重要。\n\n2️⃣ 全球债券抛售是联动现象\n\n最近美债、英债、日债同步下跌，一周内收益率分别上行21、24、23个基点。这不是某个国家的问题，而是全球性的。\n\n- 日本：需要追加预算补贴能源，但首相又说“不需要大量发债”\n- 英国：地方选举后，市场担心新领导人会搞财政宽松、多发债\n- 美国：某投行利率团队认为10年期美债收益率可能到5%\n\n3️⃣ 关键变量：新美联储主\n\n[... middle omitted ...]\n\ne repricing of 270 bps which was effectively neutralized by a 716 tonne swing in official gold demand (H2'22 vs H2'21).   \nAll indications are that incoming Fed Chair Warsh may attempt to stee\n\n[... middle omitted ...]\n\nl: (44) 20 7545 8000</td><td>The DB Center 1 Columbus Circle New York, NY 10019 Tel: (1) 212 250 2500</td><td>Filiale Singapur One Raffles Quay, South Tower Singapore 048583 Tel: (65) 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R016",
    "title": "欧洲并购的真正窗口不在大盘，而在被市场遗忘的小盘折价",
    "digest": "[wechat_article.md]\n# 欧洲并购的真正窗口不在大盘，而在被市场遗忘的小盘折价\n\n全球并购交易正在加速。某外资投行全球金融团队预测，未来12个月全球并购交易额将增长约18%。但这一轮复苏有一个显著特征：交易金额的反弹远快于交易数量的增长。这意味着，真正推动市场的不是遍地开花的交易，而是少数巨型并购案。\n\n对于关注欧洲市场的投资者而言，真正的结构性信号并不在此。欧洲并购活动仍然低迷，其占全球并购的份额已降至不足三分之一。更值得追问的是：当全球资金在追逐并购主题时，欧洲市场为何迟迟没有跟上？这种滞后背后，隐藏着怎样的定价机会？\n\n本报告的核心判断是：欧洲并购的下一波浪潮不会来自大盘蓝筹，而是来自被当前定价体系严重低估的中小盘股。这一判断的支撑逻辑，并非简单的均值回归，而是由结构性供给、估值极端分化以及买方行为错位三重力量共同推动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资产剥离意愿创纪录，并购供给端正在发生结构性变化\n\n市场通常从需求端理解并购——谁在买、为什么买。但本轮并购周期的一个关键特征在于供给端：企业主动剥离资产的意愿达到了历史高点。\n\n某外资投行针对英国CFO的最新调查显示，将“资产剥离”列为未来12个月优先事项的受访者比例创下该调查历史纪录。这一现象并非孤立。企业正在加速推进投资组合简化，通过剥离非核心资产来提升盈利可见度，并将资本重新配置到包括人工智能在内的战略优先级上。\n\n这意味着，未来12至24个月，欧洲市场将出现大量可供收购的资产。这些资产并非经营不善的“不良资产”，而是大型企业集团在战略聚焦过程中主动释放的优质业务单元。对于有资本实力和行业整合能力的买方而言，这是一个难得的“选择性买入”窗口。\n\n报告没有完全展开的一个问题是：这些剥离资产的定价是否会因为卖方“被迫出售”而出现折价。现实情况可能更为复杂。部分企\n\n[... middle omitted ...]\n\n购主题的底层数据、目标筛选框架以及当前最值得关注的候选标的。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球并购回暖，欧洲为何还在观望？\n\n全球并购回暖，欧洲为何按兵不动？\n\n欧洲买家谨慎，海外资本却在悄悄扫货\n\n全球并购正在回暖。某外资投行预计，未来12个月全球并购交易额将增长约18%。但这次复苏有个明显特征——大单撑场面，小单还没跟上。交易总额反弹得比交易数量快，说明巨型并购案是主要推手。\n\n1/ 欧洲买家还在观望\n\n欧洲的并购活跃度明显落后全球。数据显示，欧洲在全球并购中的份额已跌至不到三分之一，无论作为买方、卖方还是交易双方，参与度都在下降。\n\n本土企业收购意愿极弱，CFO调查显示，将“通过并购扩张”列为优先事项的比例接近周期低点。大家更关注成本控制，而不是花钱买增长。\n\n与之对比，海外买家正在积极入场。跨境交易在欧洲并购中的占比持续上升，外资正利用估值折价和差异化机会，主动收购欧洲资产。\n\n2/ 私募退出压力加大，IPO窗口仍窄\n\n欧洲IPO活动处于历史低位，退出渠道受限。私募基金面临越来越大的资本回报压力，不得不更多依赖并购退出。这意味着，手握充足现金的买家，有机会以合理估值收购优质资产。\n\n资产剥离也在加速。企业正在简化业务组合，通过出售非核心资产提升盈利可见性，并将资本重新配置到AI等战略方向。\n\n[... middle omitted ...]\n\nata shows a record share of UK CFOs citing asset disposals as a top priority (Exhibit 3). In parallel, private equity faces increasing pressure to return capital, reinforcing reliance on M&A e\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "三大运营商正式开卖AI“Token”：ARPU的下一轮增长，比市场预期的更早到来",
    "digest": "[wechat_article.md]\n# 三大运营商正式开卖AI“Token”：ARPU的下一轮增长，比市场预期的更早到来\n\n市场对运营商估值的核心分歧，正在从“5G投资何时见底”转向“AI变现能否真正贡献收入”。某外资投行最新发布的研报提供了一个关键信号：中国移动、中国联通、中国电信已相继推出面向个人和企业客户的AI Token计费方案，从按流量包月到按Token用量计费，定价体系已初步成型。这份报告真正值得关注的判断是，运营商的AI变现并非停留在概念层面，而是已经开始进入定价、签约、渗透的实质性阶段，其节奏可能比多数投资者的预期快一到两个季度。\n\n对于持有或关注电信板块的投资者来说，当前需要回答的核心问题不是“AI能不能赚钱”，而是“这一轮定价权之争，谁会拿到最大的份额”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三大运营商的AI Token定价已经落地，不是试点，是正式商用\n\n报告数据显示，中国移动、中国联通、中国电信均已发布明确的AI Token计费方案，且定价层级清晰。\n\n中国移动的方案是基础单价加套餐包：每40万Token收费1元，同时提供从5.99元到24.99元不等的Token套餐包。中国联通则区分个人版和企业版，个人版每月15元起，企业版每月198元起，并附带编码计划等增值服务。中国电信的定价最为细化，个人版从9.9元到49.9元三档，企业版从39.9元到299.9元三档，每档对应明确的Token用量上限。\n\n这意味着什么？AI服务不再是运营商年报里的“探索方向”，而是已经进入计费系统、可以规模化销售的标准化产品。从定价结构看，运营商明显在模仿云计算领域的“基础费+按量计费”模式，这与过去语音、流量时代的简单包月制有本质区别。Token计费的核心优势在于，它让运营商能够直接受益于用户AI使用量的增长，而不是靠固定套餐的提价来提\n\n[... middle omitted ...]\n\n透率变化和供应链出口趋势，帮你在这个关键转折期保持信息优势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n三大运营商开始卖AI Token了\n\n运营商的新算盘：按Token收费\n\n国内三大运营商最近悄悄上线了AI Token套餐，面向个人和企业用户，按月/季订阅或按用量计费。\n\n这个模式很有意思——运营商开始像卖云服务一样卖AI能力，而不是只卖流量了。\n\n1/ 三大运营商AI套餐一览\n\n中国移动：1元40万Token，或者5.99-24.99元买Token包\n中国联通：个人版15元/月起，企业版198元/月起，还有针对开发者的编程套餐\n中国电信：个人版9.9-49.9元/月，企业版39.9-299.9元/月\n\n以电信为例，企业版基础套餐39.9元/月含1500万Token，旗舰版299.9元/月含1.5亿Token。\n\n2/ 为什么运营商要推Token套餐？\n\n核心逻辑是提升ARPU（每用户平均收入）。\n\n传统通信业务增长放缓，运营商需要找到新的收入增长点。AI Token套餐把通信能力+算力+AI能力打包，相当于把管道升级成平台。\n\n运营商有两个天然优势：一是能提供“一站式”解决方案（网络+算力+应用），二是数据安全有保障。\n\n3/ 5G基站建设节奏放缓\n\n2026年4月新增5G基站5.1万座，同比增16%，但\n\n[... middle omitted ...]\n\nbn (per MIIT); 2) new 5G base station deployment decreased YoY in Apr 2026 to 51k units, vs. 44k units added in Apr 2025; and 3) 5G subscriber growth accelerated, to +8mn in Apr 2026, vs. +19m\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "市场真正低估的不是风险，而是结构性的相对价值错位",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是风险，而是结构性的相对价值错位\n\n这份来自某外资投行结构化产品团队的研报，表面上讨论的是MBS、RMBS和ABS三个细分市场的近期走势，但贯穿全文的是一条更值得产业决策者和资产配置者关注的线索：在宏观利率路径尚不明朗的当下，市场正在对“相似资产”给出差异化的定价。这种定价差异，既来自发行结构、抵押品特征和季节性因素的技术面错位，也来自消费信贷数据与情绪指标之间的裂痕。\n\n报告的核心判断可以概括为一句话：当前机构MBS和RMBS市场中的相对价值机会，远比绝对收益率水平更值得关注；而ABS市场的韧性，正在被情绪指标掩盖的结构性分化所挑战。\n\n这份报告的价值不仅在于它给出了具体的交易建议——比如在机构MBS中做多GN II/FN 4.0s互换、做空GN II/FN 4.5s互换——更在于它提供了一套可以复用的分析框架：当宏观利率路径无法确定时，如何通过拆解抵押品特征、发行节奏和资金流结构来寻找定价偏差。\n\n以下是我们从报告中提炼出的四个关键洞察，以及一个报告尚未完全回答但值得所有读者持续追踪的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 机构MBS的定价错位来自抵押品结构差异，而非利率方向\n\n报告中最重要的相对价值判断集中在机构MBS的“腹部券”互换。GN II/FN 4.5s互换从年初的-12个ticks快速回升至约6个ticks，而同期GN II/FN 4.0s和3.5s互换仍处于深度负值区间。这一分化的直接驱动力并非利率本身的变化，而是抵押品构成的结构性差异。\n\n具体来说，今年早些时候抵押贷款利率的下降导致再融资贷款在GN II 4.5s新发行中的占比显著高于其在FN 4.5s中的占比。由于再融资贷款的加权平均贷款年龄（WALA）曲线比购房贷款陡峭得多，这使得GN II 4.5s的有\n\n[... middle omitted ...]\n\n图表和我们的分析笔记，并与您一起追踪这些关键变量的后续演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMBS 市场正在悄悄换挡\n\n房利美 vs 吉利美，4.0 更香\n\n一张图看懂近期债市轮动逻辑\n\n最近看了一份某外资投行的结构化产品研报，信息量不小，关于MBS（抵押贷款支持证券）的轮动逻辑讲得很清楚。\n\n简单来说，市场正在经历一个关键的“换挡期”，几个信号值得关注：\n\n**1/ 吉利美4.5s vs 房利美4.5s，优势正在消失**\n\n年初以来，吉利美4.5s相对房利美4.5s的表现一直不错，主要因为吉利美新发贷款中再融资占比更高，这类贷款的久期变化更陡峭，让吉利美4.5s的久期显得更短，相对房利美4.5s更有优势。\n\n但研报判断，这个趋势可能要转向了。最近抵押贷款利率回升，加上春季购房季到来，新发贷款中购房贷款占比会上升。购房贷款的久期曲线更平缓，这会拉长吉利美4.5s的久期，削弱之前的相对优势。\n\n更关键的是，吉利美4.5s的可交割存量比房利美4.5s大得多，这种供给压力会进一步压制价格。\n\n相反，在4.0s这个票息上，吉利美和房利美的存量规模差不多，相对压力更小。研报倾向于“做多吉利美4.0s vs 房利美4.0s，同时做空吉利美4.5s vs 房利美4.5s”的配对思路。\n\n**2/ 优质大额RMBS\n\n[... middle omitted ...]\n\nable float of recently produced GN II 4.5s compared to FN 4.5s could exert downside pressure on the swap, especially vs. 4.0s where the size of the floats are more comparable between GNs and c\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "2026世界杯的真正悬念，不在于谁赢，而在于模型暴露了什么",
    "digest": "[wechat_article.md]\n# 2026世界杯的真正悬念，不在于谁赢，而在于模型暴露了什么\n\n世界杯预测模型从来不只是关于足球。它是一面镜子，照出我们如何用数据理解不确定的世界。某外资投行刚刚发布的2026世界杯预测报告，给出了一个清晰的结论：西班牙夺冠概率26%，法国19%，阿根廷14%，巴西8%，英格兰5%。但真正值得关注的，不是这些数字本身，而是模型背后的逻辑——以及它刻意没有回答的问题。\n\n这份报告的价值不在于预测准不准，而在于它揭示了一个更底层的判断：在足球这个公认最不可预测的竞技场上，结构性因素（Elo评分、主场优势、海拔差异）比短期变量（球员状态、抽签运气）更能解释结果。这恰恰是许多产业分析中容易被忽视的视角——人们总是高估短期波动，低估长期结构。\n\n报告基于近两万场国际比赛的数据库，用泊松分布模拟进球数，再通过蒙特卡洛模拟五万次比赛路径。方法论本身并不新鲜，但它在几个关键维度上的拓展——从“赢家诅咒”到高海拔惩罚，从“大赛型球队”到英格兰的持续低迷——提供了一个观察框架，可以用来审视任何竞争性领域的分析思维。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 赢家诅咒不是玄学，是统计显著的结构性劣势\n\n卫冕冠军在下一届世界杯表现不佳，这个现象被球迷称为“卫冕魔咒”。但报告将其量化成一个可测量的变量：赢家诅咒效应导致预期进球数减少0.12个。对比一下，主场优势能增加0.38个进球，高海拔惩罚减少0.18个——赢家诅咒的幅度大约是主场优势的三分之一，但比许多人的直觉要大。\n\n这不是玄学。报告的数据显示，从1978年到2022年，12支卫冕冠军中有7支在下一届世界杯未能进入四强，其中4支小组赛出局。阿根廷作为2022年冠军，在模型中被施加了这个惩罚。这解释了为什么阿根廷的夺冠概率只有14%，远低于其Elo排名（世界第二）所暗示的水平。\n\n[... middle omitted ...]\n\n些变量被高估、哪些被低估，以及这些偏差对分析框架意味着什么。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n西班牙最有戏？2026世界杯概率拆解\n\n🏆 冠军概率预测\n\n某外资投行用统计模型模拟了2026世界杯，给出夺冠概率排名：\n西班牙26% > 法国19% > 阿根廷14% > 巴西8% > 英格兰5%\n\n模型核心逻辑👇\n\n1️⃣ 基础评分：Elo系统\n不同于FIFA排名，Elo系统更看重历史战绩含金量。西班牙目前Elo第一，这是模型预测其夺冠的最大支撑。\n\n2️⃣ 关键修正因子\n- 射手天赋：联赛顶级射手多的球队，进球预期更高\n- 近期状态：近10场正式比赛进球数+对手近5场失球数\n- 心理因素：卫冕冠军有“赢家衰退”效应，阿根廷因此被调低概率\n- 地理劣势：低海拔国家在墨西哥高原比赛，进球预期下降18%\n\n3️⃣ 英格兰的“魔咒”\n模型显示：英格兰是唯一一个在世界杯上表现显著低于Elo评级的传统强队。加上可能要在墨西哥城高海拔迎战东道主，抽签也不理想，夺冠概率被压得很低。\n\n4️⃣ 赛程推演\n模拟显示最可能剧情：法国半决赛提前碰西班牙，阿根廷一路杀进决赛。最终西班牙vs阿根廷的“欧南美冠军对决”，西班牙捧杯。\n\n⚠️ 模型局限性\n足球本身不可预测性高，模型统计效力有限。但上届世界杯用同样方法预测，效果还不错（\n\n[... middle omitted ...]\n\nity and geographical factors.   \nWe then simulate a set of probabilities that a particular team will reach a particular round, up to winning the World Cup. We also provide a modal forecast for\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R020",
    "title": "苹果拥抱COB封装，市场低估了供应链的“双赢”格局",
    "digest": "[wechat_article.md]\n# 苹果拥抱COB封装，市场低估了供应链的“双赢”格局\n\n2026年5月29日，舜宇光学股价单日飙升14%。市场将其解读为“舜宇即将打入苹果摄像头模组供应链”的单一利好。但某外资投行最新发布的研报揭示了一个更值得关注的判断：苹果正在系统性切换摄像头模组封装工艺，从沿用多年的FC（倒装芯片）转向COB（板上芯片）。这一变化不会导致现有供应商被替代，反而会催生一个“双赢”格局——舜宇有机会切入苹果，而高伟电子不仅不会受损，反而可能在COB/FC双重技术领先下巩固并扩大份额。\n\n市场真正低估的不是舜宇能否进入苹果，而是COB工艺切换对整条供应链竞争格局的重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 苹果的封装技术路线切换，比想象中更加确定\n\n研报通过渠道调研确认，苹果正在规划将COB封装方案逐步引入多个产品线。这不是实验室阶段的探索，而是有明确时间表的供应链部署。\n\n具体路径是：苹果可能先在即将推出的可穿戴设备上采用COB方案——包括TWS和配备摄像头的AI眼镜。这些产品出货量相对较小，适合作为供应链磨合的试验场。随后，在2028年前后，COB方案可能被引入iPhone的潜望式摄像头和超广角摄像头。\n\n这一判断的关键支撑在于COB技术在微型化方面的持续演进。过去几年，COB在缩小模组体积、降低Z轴高度方面取得了实质性突破，使其终于具备了替代FC方案的技术成熟度。而苹果在过去数十年间，对大多数产品一直坚持FC方案，此次转向意味着其内部对COB的评估已经通过了关键门槛。\n\n当然，所有项目都存在不确定性。但研报的潜台词很清楚：方向已定，节奏可调，但不会回头。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 舜宇光学的机会不是“替代”，而是“扩容”\n\n市场对舜宇的炒作逻辑\n\n[... middle omitted ...]\n\n研究者交换对COB渗透节奏、供应商份额变化等未解问题的看法。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n苹果供应链迎来新变局：COB封装技术\n\nCOB封装，谁在受益？\n\n苹果摄像头封装技术路线或将生变\n\n最近某外资投行的一篇研报，把苹果摄像头供应链的潜在变化梳理得挺清楚。简单来说，苹果可能要在封装技术上动刀了。\n\n过去十几年，苹果在摄像头模组上一直用FC（倒装芯片）方案，但COB（板上芯片封装）技术在小型化方面进步很快，苹果终于开始认真考虑换方案了。\n\n研报的核心判断是：这不是一个零和游戏，而是增量机会。\n\n1/ 苹果的COB时间线\n\n根据渠道调研，苹果的COB导入会分两步走：\n- 先用在带摄像头的可穿戴设备上（TWS耳机、AI眼镜），让供应链先跑起来\n- 最早2028年，才会上到iPhone的潜望式长焦和超广角摄像头\n\n当然，这些项目都存在不确定性，但方向很明确——苹果在封装技术上要迈出新一步了。\n\n2/ Sunny的机会在哪里\n\n舜宇在摄像头模组小型化上一直有积累（MOB/MOC方案领先），COB路线正好对上了它的技术储备。研报认为，苹果采用COB确实给舜宇打开了进入其供应链的大门，这个潜在市场空间可能不比整个安卓阵营小。\n\n另外舜宇在安卓市场也在优化产品结构。研报估算2025年，混合镜头/潜望式镜头占其手\n\n[... middle omitted ...]\n\nd by $14\\%$ on Fri (May 29), likely driven by market chatter on its potential in supplying camera module with COB (chip on board) assembly solution to Apple and breakthrough in AI optics. Base\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Cynthia Wu Figure 1. Steel PMI Composite Index © 2026 Citi Inc. No redistribution without Citi's written permission. # Construction Industry Figure 2. Construction Industry PMI"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Construction PMI was 50.7%, up 0.1% MoM and 0.9ppt YoY. On a seasonally adjusted basis, the reading was 49.5%, up 0.6ppt MoM and 0.8ppt YoY. The production index was 50.1%, down 1.2ppt MoM a"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Composite index-Construction"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Machinery PMI was 51%, up 0.3% MoM and +1.7ppt YoY. On a seasonally adjusted basis, the reading was 50.3%, down 0.2ppt MoM and up 1.6ppt YoY. Production index was 51.6%, up 0.9ppt MoM and 2."
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Composite index - Machinery"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Auto PMI was 50.8%, up 1.6% MoM and +0.2ppt YoY. On a seasonally adjusted basis, the reading was 50%, up 0.4ppt MoM and flattish YoY. Production index was 51.4%, up 2.1ppt MoM and up 0.5ppt "
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. Composite index - Automobile"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Shipbuilding PMI was 50%, up 0.2ppt MoM and down 0.4% YoY. On a seasonally adjusted basis, the reading was 49.7%, up 0.5ppt MoM and down 0.5ppt YoY. Production index was 50.2%, down 1.0ppt M"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. Composite index - Ship building"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Figure 15",
    "context": "Home appliances PMI was 50.7%, up 1.7ppt MoM and +1.6ppt YoY. On a seasonally adjusted basis, the reading was 50.7%, up 1.2ppt MoM and +1.6ppt YoY. Production index was 51.1%, up 2.7ppt MoM and up 3.0ppt YoY. The new orders index was 51.3%, up 2.9ppt MoM and +"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 16. Composite index - Home Appliances"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Figure 18",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Transportation infrastructure PMI was 50%, down 0.4ppt MoM and -0.3ppt YoY. On a seasonally adjusted basis, the reading was 49.0%, up 0.2ppt MoM and down 0.3ppt YoY. Production index was 51."
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Figure 19",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 19. Composite index - Transportation Infrastructure"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Figure 1",
    "context": "# Global Inflation (April)\\* Figure 1. Global Inflation (April)"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Global Inflation (April)"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Global Headline CPI Inflation: Country-Level Detail (April) 3-Month Change (Pct Pts)"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Global Core CPI Inflation: Country-Level Detail (April) 3-Month Change (Pct Pts)"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Global PPI Inflation: Country-Level Detail (March/April) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. DM Country-Level CPI Inflation (April)"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Figure 5",
    "context": "Figure 5. Global PPI Inflation: Country-Level Detail (March/April) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. DM Country-Level CPI Inflation (April)"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. \\*Euro Area PPI data through March 2026. \\*\\*Australia PPI reflects quarterly data through 2026Q1. Figure 7. EM Country-Level CPI Inflation (April)"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. US Import Prices (April)"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. 2026 Headline Inflation Forecast Revisions (Citi)\\*"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. \\*Change from February forecasts; US forecast is for PCE. Figure 10. 2026 Core Inflation Forecast Revisions (Citi)\\*"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. \\*Change from February forecasts; US forecast is for PCE. Figure 11. Country Level Inflation Forecasts (April)"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We see acceleration of renovation for urban dilapidated housing, old neighborhoods and factory areas, historical building and urban underground pipeline network, with several niche fields of urban renewal newly introduce"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Comparison of property FAI and incremental FAI from shantytown redevelopment and urban renewal"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: On a spread basis, USD BB-rated bonds have meaningfully outperformed B-rated bonds since late 2025 OAS ratio of the B and BB subsets of the Bloomberg USD HY Corporate indices"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: In contrast, USD BB vs. BBB spreads have been rangebound OAS ratio of the BB and BBB subsets of the Bloomberg USD HY and IG Corporate indices"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: In the EUR market, BB spreads have also outperformed the B-rated cohort OAS ratio of the B and BB subsets of the Bloomberg Pan Euro HY Corporate indices"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: EUR BB vs. BBB spreads remain near the mid-to-low end of the historical range OAS ratio of the BB and BBB subsets of the Bloomberg Pan Euro HY and IG Corporate indices"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: A high share of fallen angels in the EUR and USD markets were not rated BBB or BBB- on Negative outlook or Downgrade Watch prior to the event Share of bonds in each rating bucket that became fallen angels within 12 month"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Similarly, a high share of rising stars in the EUR and USD markets were not BB+ or BB on Positive Outlook or Upgrade Watch prior to the event Share of bonds in each rating bucket that became rising stars within 12 months"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 7: In the EUR market, fallen angels are set to outpace rising stars for the first time since 2020. Fallen angel and rising star notionals in the EUR market (left panel) and USD market (right panel) EUR Notional for Fallen"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Neither market is pricing significant fallen angel risk"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Since 2021, rising stars have been dominated by Banks and Financials in the EUR market Exhibit 10: Energy intensive sectors screen at risk of becoming fallen angels in the EUR market, alongside Software in the USD mark"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 9: Since 2021, rising stars have been dominated by Banks and Financials in the EUR market Exhibit 10: Energy intensive sectors screen at risk of becoming fallen angels in the EUR market, alongside Software in the USD mark"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: In the EUR market, fallen angels tend to underperform post a downgrade, unlike in the USD market The exhibit shows the relative OAS performance before/after becoming a fallen angel since 2010, covering 155 issuers in the"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The EUR market has a high share of debt attached to just one rating agency vs. the USD market Percentages based on notional amounts Share of BBBs by number of rating agencies in Europe (%)"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: In the EUR market, fallen angels have a higher tendency to be downgraded to CCC+ or below Exhibit shows the share of bonds that become fallen angels in the EUR and USD market which are downgraded to CCC+ or below within"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Issuers in the EUR and USD market with just one rating agency tend to have wider spreads EUR average OAS by # of rating agencies"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 15: In Europe, the share of single rating agency risk has been rising"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Single rating agency risk tends to be concentrated in new and smaller issuers"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Exhibit 28",
    "context": "Exhibit 28: USD spread dispersion"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Exhibit 29",
    "context": "Exhibit 29: EUR spread dispersion"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Exhibit 30",
    "context": "Exhibit 30: USD return dispersion"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Exhibit 31",
    "context": "Exhibit 31: EUR return dispersion"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Exhibit 32",
    "context": "Exhibit 32: USD/EUR IG and HY spread differential"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Exhibit 33",
    "context": "Exhibit 33: CDX IG/iTraxx Main and CDX HY/iTraxx Xover spread differential"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "Exhibit 34",
    "context": "Exhibit 34: IG OAS/Agency MBS spread differential"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Leveraged loans/HY spread differential"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Percentile ranks for spreads across markets (2000-current)"
  },
  {
    "figure_id": "F052",
    "report_id": "R004",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Percentile ranks for spreads across markets (2010-current)"
  },
  {
    "figure_id": "F053",
    "report_id": "R004",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Percentile ranks for yields across markets (2000-current)"
  },
  {
    "figure_id": "F054",
    "report_id": "R004",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Percentile ranks for yields across markets (2010-current)"
  },
  {
    "figure_id": "F055",
    "report_id": "R004",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Average yield vs. total market value outstanding across the USD fixed income complex"
  },
  {
    "figure_id": "F056",
    "report_id": "R004",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Average yield vs. total market value outstanding for the EUR fixed income markets"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "Exhibit 44",
    "context": "Exhibit 44: CDX IG and iTraxx Main vol 3m ATM implied volatility"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Exhibit 45",
    "context": "Exhibit 45: CDX HY and iTraxx Xover vol 3m ATM implied volatility"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Exhibit 46",
    "context": "Exhibit 46: CDX IG and iTraxx Main skew"
  },
  {
    "figure_id": "F060",
    "report_id": "R004",
    "label": "Exhibit 47",
    "context": "Exhibit 47: CDX HY and iTraxx Xover skew"
  },
  {
    "figure_id": "F061",
    "report_id": "R004",
    "label": "Exhibit 48",
    "context": "Exhibit 48: CDX IG and iTraxx Main ATM implied volatility term structure"
  },
  {
    "figure_id": "F062",
    "report_id": "R004",
    "label": "Exhibit 49",
    "context": "Exhibit 49: CDX HY and iTraxx Xover ATM implied volatility term structure"
  },
  {
    "figure_id": "F063",
    "report_id": "R004",
    "label": "Exhibit 52",
    "context": "Exhibit 52: CLO new issue arbitrage spread New issue CLO arbitrage spread, i.e., the difference between new issue loan spreads and new issue CLO spreads (across the capital stack)"
  },
  {
    "figure_id": "F064",
    "report_id": "R004",
    "label": "Exhibit 51",
    "context": "Exhibit 51: CLO equity vs. CLO BB yield"
  },
  {
    "figure_id": "F065",
    "report_id": "R004",
    "label": "Exhibit 53",
    "context": "Exhibit 53: CLO vs. USD IG spread differential CLO by rating and USD IG bond by rating spread differential"
  },
  {
    "figure_id": "F066",
    "report_id": "R004",
    "label": "Exhibit 54",
    "context": "Exhibit 54: IG Weekly sentiment indicator"
  },
  {
    "figure_id": "F067",
    "report_id": "R004",
    "label": "Exhibit 55",
    "context": "Exhibit 55: HY Weekly sentiment indicator"
  },
  {
    "figure_id": "F068",
    "report_id": "R004",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Seasonally adjusted daily average turnover (trading volume/amount outstanding)"
  },
  {
    "figure_id": "F069",
    "report_id": "R004",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Primary dealer net positioning in USD corporate bonds"
  },
  {
    "figure_id": "F070",
    "report_id": "R004",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Average IG bid-ask spread 5-day moving average"
  },
  {
    "figure_id": "F071",
    "report_id": "R004",
    "label": "Exhibit 62",
    "context": "Exhibit 62: Amihud IG illiquidity measure 5-day moving average"
  },
  {
    "figure_id": "F072",
    "report_id": "R004",
    "label": "Exhibit 63",
    "context": "Exhibit 63: AUM in USD IG-focused Mutual Funds and ETFs"
  },
  {
    "figure_id": "F073",
    "report_id": "R004",
    "label": "Exhibit 64",
    "context": "Exhibit 64: AUM in USD HY-focused Mutual Funds and ETFs"
  },
  {
    "figure_id": "F074",
    "report_id": "R004",
    "label": "Exhibit 65",
    "context": "Exhibit 65: AUM in EUR IG-focused Mutual Funds and ETFs"
  },
  {
    "figure_id": "F075",
    "report_id": "R004",
    "label": "Exhibit 66",
    "context": "Exhibit 66: AUM in EUR HY-focused Mutual Funds and ETFs"
  },
  {
    "figure_id": "F076",
    "report_id": "R004",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Weekly mutual fund flows into US fixed income and equity markets"
  },
  {
    "figure_id": "F077",
    "report_id": "R004",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Weekly mutual fund flows into European fixed income and equity markets"
  },
  {
    "figure_id": "F078",
    "report_id": "R004",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Year-to-date cumulative flows as a percentage of beginning of the year AUM for US credit funds"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Year-to-date cumulative flows as a percentage of beginning of the year AUM for European credit funds"
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Our estimates of upcoming coupon and principal payments in the USD IG market"
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Our estimates of upcoming coupon and principal payments in the USD HY market"
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "Exhibit 73",
    "context": "Exhibit 73: Our estimates of upcoming coupon and principal payments in the EUR IG market"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "Exhibit 74",
    "context": "Exhibit 74: Our estimates of upcoming coupon and principal payments in the EUR HY market"
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Net notional positioning in the CDX IG 5-year on-the-run contract"
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Net notional positioning in the CDX HY 5-year on-the-run contract"
  },
  {
    "figure_id": "F086",
    "report_id": "R004",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Net notional positioning in the iTraxx Main 5-year on-the-run contract"
  },
  {
    "figure_id": "F087",
    "report_id": "R004",
    "label": "Exhibit 78",
    "context": "Exhibit 78: Net notional positioning in iTraxx over 5-year on-the-run contract"
  },
  {
    "figure_id": "F088",
    "report_id": "R004",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Ownership share of the ECB in the EUR IG market"
  },
  {
    "figure_id": "F089",
    "report_id": "R004",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Run-off projections for the ECB corporate bond holdings"
  },
  {
    "figure_id": "F090",
    "report_id": "R004",
    "label": "Exhibit 81",
    "context": "Exhibit 81: CSPP monthly run-off pace"
  },
  {
    "figure_id": "F091",
    "report_id": "R004",
    "label": "Exhibit 82",
    "context": "Exhibit 82: Performance of CSPP-eligible bonds vs. non-eligible bonds"
  },
  {
    "figure_id": "F092",
    "report_id": "R004",
    "label": "Exhibit 83",
    "context": "Exhibit 83: Net purchases of USD corporate bonds by foreign investors"
  },
  {
    "figure_id": "F093",
    "report_id": "R004",
    "label": "Exhibit 84",
    "context": "Exhibit 84: Cumulative net foreign purchases of USD and EUR bonds by Japanese investors"
  },
  {
    "figure_id": "F094",
    "report_id": "R004",
    "label": "Exhibit 85",
    "context": "Exhibit 85: Annualized 3-month rolling cost of USD hedging against EUR, GBP and JPY"
  },
  {
    "figure_id": "F095",
    "report_id": "R004",
    "label": "Exhibit 86",
    "context": "Exhibit 86: USD IG gross issuance Historical investment grade issuance: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F096",
    "report_id": "R004",
    "label": "Exhibit 87",
    "context": "Exhibit 87: USD HY gross issuance Historical USD high yield issuance: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F097",
    "report_id": "R004",
    "label": "Exhibit 88",
    "context": "Exhibit 88: USD institutional leveraged loan gross issuance Historical leveraged loan issuance: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F098",
    "report_id": "R004",
    "label": "Exhibit 89",
    "context": "Exhibit 89: USD CLO creation Historical USD CLO creation: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F099",
    "report_id": "R004",
    "label": "Exhibit 90",
    "context": "Exhibit 90: EUR IG gross issuance Historical EUR investment grade issuance: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F100",
    "report_id": "R004",
    "label": "Exhibit 92",
    "context": "Exhibit 92: EUR Leveraged loan gross issuance Historical EUR leveraged loan issuance: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F101",
    "report_id": "R004",
    "label": "Exhibit 91",
    "context": "Exhibit 91: EUR HY gross issuance Historical EUR high yield issuance: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F102",
    "report_id": "R004",
    "label": "Exhibit 93",
    "context": "Exhibit 93: EUR CLO creation Historical EUR CLO creation broken: Same period year to date vs. rest of the year"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Exhibit 94",
    "context": "Exhibit 94: Annual USD IG issuance volumes by use of proceeds"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Exhibit 95",
    "context": "Exhibit 95: USD HY issuance volumes by use of proceeds"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Exhibit 96",
    "context": "Exhibit 96: EUR IG issuance volumes by use of proceeds"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Exhibit 97",
    "context": "Exhibit 97: EUR HY issuance volumes by use of proceeds"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Exhibit 98",
    "context": "Exhibit 98: Annual USD IG net issuance"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Exhibit 99",
    "context": "Exhibit 99: Annual USD HY net issuance"
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Exhibit 100",
    "context": "Exhibit 100: Annual EUR IG net issuance"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "Exhibit 101",
    "context": "Exhibit 101: Annual EUR HY net issuance"
  },
  {
    "figure_id": "F111",
    "report_id": "R004",
    "label": "Exhibit 102",
    "context": "Exhibit 102: Annual US M&A deal volume Includes strategic and sponsored deals US M&A deal volume"
  },
  {
    "figure_id": "F112",
    "report_id": "R004",
    "label": "Exhibit 103",
    "context": "Exhibit 103: Annual European M&A deal volume Includes strategic and sponsored deals European M&A deal volume"
  },
  {
    "figure_id": "F113",
    "report_id": "R004",
    "label": "Exhibit 104",
    "context": "Exhibit 104: Year-to-date US M&A volume by sector Includes strategic and sponsored deals US year-to-date M&A volume by industry (\\$bn)"
  },
  {
    "figure_id": "F114",
    "report_id": "R004",
    "label": "Exhibit 105",
    "context": "Exhibit 105: Year-to-date European M&A volume by sector Includes strategic and sponsored deals European year-to-date M&A volume by industry (\\$bn)"
  },
  {
    "figure_id": "F115",
    "report_id": "R004",
    "label": "Exhibit 106",
    "context": "Exhibit 106: Annual US strategic M&A volumes US strategic M&A volumes"
  },
  {
    "figure_id": "F116",
    "report_id": "R004",
    "label": "Exhibit 107",
    "context": "Exhibit 107: Annual European strategic M&A volumes European strategic M&A volumes"
  },
  {
    "figure_id": "F117",
    "report_id": "R004",
    "label": "Exhibit 108",
    "context": "Exhibit 108: Annual US strategic M&A deal count US strategic M&A deal count"
  },
  {
    "figure_id": "F118",
    "report_id": "R004",
    "label": "Exhibit 109",
    "context": "Exhibit 109: Annual European strategic M&A deal count European strategic M&A deal count"
  },
  {
    "figure_id": "F119",
    "report_id": "R004",
    "label": "Exhibit 110",
    "context": "Exhibit 110: Annual US strategic M&A deal size"
  },
  {
    "figure_id": "F120",
    "report_id": "R004",
    "label": "Exhibit 111",
    "context": "Exhibit 111: Annual European strategic M&A deal size"
  },
  {
    "figure_id": "F121",
    "report_id": "R004",
    "label": "Exhibit 112",
    "context": "Exhibit 112: Annual USD Broadly syndicated loan CLO creation"
  },
  {
    "figure_id": "F122",
    "report_id": "R004",
    "label": "Exhibit 113",
    "context": "Exhibit 113: Annual USD Middle market CLO creation USD MM CLO gross issuance"
  },
  {
    "figure_id": "F123",
    "report_id": "R004",
    "label": "Exhibit 114",
    "context": "Exhibit 114: Annual USD leveraged loan net issuance"
  },
  {
    "figure_id": "F124",
    "report_id": "R004",
    "label": "Exhibit 115",
    "context": "Exhibit 115: USD CLO refinance monitor"
  },
  {
    "figure_id": "F125",
    "report_id": "R004",
    "label": "Exhibit 116",
    "context": "Exhibit 116: USD CLO refinance monitor"
  },
  {
    "figure_id": "F126",
    "report_id": "R004",
    "label": "Exhibit 117",
    "context": "Exhibit 117: USD IG bond market maturity wall"
  },
  {
    "figure_id": "F127",
    "report_id": "R004",
    "label": "Exhibit 118",
    "context": "Exhibit 118: EUR IG bond market maturity wall"
  },
  {
    "figure_id": "F128",
    "report_id": "R004",
    "label": "Exhibit 119",
    "context": "Exhibit 119: USD HY bond market maturity wall USD HY bonds"
  },
  {
    "figure_id": "F129",
    "report_id": "R004",
    "label": "Exhibit 120",
    "context": "Exhibit 120: EUR HY bond market maturity wall EUR HY bonds"
  },
  {
    "figure_id": "F130",
    "report_id": "R004",
    "label": "Exhibit 121",
    "context": "Exhibit 121: USD leveraged loan market maturity wall USD leveraged loans"
  },
  {
    "figure_id": "F131",
    "report_id": "R004",
    "label": "Exhibit 122",
    "context": "Exhibit 122: EUR leveraged loan market maturity wall EUR leveraged loans"
  },
  {
    "figure_id": "F132",
    "report_id": "R004",
    "label": "Exhibit 123",
    "context": "Exhibit 123: Default rates for US HY bond and leveraged loan issuers 12-month trailing issuer-weighted default rate in the US HY bond and leveraged loan markets"
  },
  {
    "figure_id": "F133",
    "report_id": "R004",
    "label": "Exhibit 125",
    "context": "Exhibit 125: High frequency default rates for US HY bond and leveraged loan issuers 3-month trailing issuer-weighted default rate in the US HY bond and leveraged loan markets"
  },
  {
    "figure_id": "F134",
    "report_id": "R004",
    "label": "Exhibit 127",
    "context": "Exhibit 127: Annual par value amounts of defaulted USD HY bonds and leveraged loans"
  },
  {
    "figure_id": "F135",
    "report_id": "R004",
    "label": "Exhibit 124",
    "context": "Exhibit 124: Default rates for European bond and leveraged loan issuers 12-month trailing issuer-weighted default rate in the European HY bond and leveraged loan markets"
  },
  {
    "figure_id": "F136",
    "report_id": "R004",
    "label": "Exhibit 126",
    "context": "Exhibit 126: High frequency default rates for European HY bond and leveraged loan issuers 3-month trailing issuer-weighted default rate in the European HY bond and leveraged loan markets"
  },
  {
    "figure_id": "F137",
    "report_id": "R004",
    "label": "Exhibit 128",
    "context": "Exhibit 128: Par value amounts of defaulted EUR HY bonds and leveraged loans"
  },
  {
    "figure_id": "F138",
    "report_id": "R004",
    "label": "Exhibit 130",
    "context": "Exhibit 130: Top 5 largest defaults in the EUR HY bond and leveraged loan markets in the past 12 months Exhibit 131: Industry default count in the US"
  },
  {
    "figure_id": "F139",
    "report_id": "R004",
    "label": "Exhibit 132",
    "context": "Exhibit 132: Industry default count in Europe"
  },
  {
    "figure_id": "F140",
    "report_id": "R004",
    "label": "Exhibit 133",
    "context": "Exhibit 133: Composition of defaults in the USD HY bond market by type"
  },
  {
    "figure_id": "F141",
    "report_id": "R004",
    "label": "Exhibit 134",
    "context": "Exhibit 134: Composition of defaults in the EUR HY bond market by type"
  },
  {
    "figure_id": "F142",
    "report_id": "R004",
    "label": "Exhibit 135",
    "context": "Exhibit 135: Annual average recovery rates by seniority for US issuers"
  },
  {
    "figure_id": "F143",
    "report_id": "R004",
    "label": "Exhibit 136",
    "context": "Exhibit 136: Annual average recovery rates by seniority for European issuers"
  },
  {
    "figure_id": "F144",
    "report_id": "R004",
    "label": "Exhibit 137",
    "context": "Exhibit 137: Fallen angels vs. rising stars in the USD market"
  },
  {
    "figure_id": "F145",
    "report_id": "R004",
    "label": "Exhibit 138",
    "context": "Exhibit 138: Fallen angels vs. rising stars in the EUR market"
  },
  {
    "figure_id": "F146",
    "report_id": "R004",
    "label": "Exhibit 139",
    "context": "Exhibit 139: BB-rated bonds on upgrade watch (upgrade candidates) vs. BBB-rated bonds on downgrade watch (downgrade candidates) in the USD market"
  },
  {
    "figure_id": "F147",
    "report_id": "R004",
    "label": "Exhibit 140",
    "context": "Exhibit 140: BB-rated bonds on upgrade watch (upgrade candidates) vs. BBB-rated bonds on downgrade watch (downgrade candidates) in the EUR market"
  },
  {
    "figure_id": "F148",
    "report_id": "R004",
    "label": "Exhibit 141",
    "context": "Exhibit 141: BB-rated bonds on outlook positive vs. BBB-rated bonds on outlook negative in the USD market"
  },
  {
    "figure_id": "F149",
    "report_id": "R004",
    "label": "Exhibit 145",
    "context": "Exhibit 145: Top 10 EUR Fallen angel issues Exhibit 142: BB-rated bonds on outlook positive vs. BBB-rated bonds on outlook negative in the EUR market"
  },
  {
    "figure_id": "F150",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 1: The recent US rally has been predominantly driven by a reset in Treasury term premium Change in 10y UST term premium/rate expectations, GS estimate"
  },
  {
    "figure_id": "F151",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Implied vol is at the bottom of our range of estimates of fair Average Implied Vol vs fair value model range"
  },
  {
    "figure_id": "F152",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Sovereign spread compression has run ahead of relief in rates levels and volatility Retracement from post-conflict peak / wides. Using GS fitted yields"
  },
  {
    "figure_id": "F153",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Recent bull-flattening is consistent with the relief in 10y term premium GS fitted yields and term premium model"
  },
  {
    "figure_id": "F154",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Recent JPY rate repricing mainly a function of forwards further out JPY Forward rates, change since end April"
  },
  {
    "figure_id": "F155",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 6: NZD forwards have decoupled notably from spot policy"
  },
  {
    "figure_id": "F156",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: News coverage suggests that negotiations with Canada were more contentious than with Mexico"
  },
  {
    "figure_id": "F157",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "We use Bloomberg News Trends to produce a count of news stories containing “trade war”, Canada (or Mexico), and USA, and separately “trade”, Canada (or Mexico), and USA. We then take the “trade war” share of total trade headlines for each country. We have foun"
  },
  {
    "figure_id": "F158",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ...but had a more limited impact on MXN"
  },
  {
    "figure_id": "F159",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We find markets price limited trade-specific premium beyond standard cyclical drivers in our GSBEER models"
  },
  {
    "figure_id": "F160",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 5: During the 2025 fentanyl-related tariffs and Liberation Day uncertainty, the moves in USD/CAD were largely explained by rate differentials"
  },
  {
    "figure_id": "F161",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Trade headlines have tended to move USD-CAD rate differentials and USD/CAD together"
  },
  {
    "figure_id": "F162",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Rising trade tensions are also reflected in low-delta options, consistent with stronger demand for protection against policy-driven tail risks"
  },
  {
    "figure_id": "F163",
    "report_id": "R007",
    "label": "Figure 7",
    "context": "Figure 1: Global energy stack"
  },
  {
    "figure_id": "F164",
    "report_id": "R007",
    "label": "Figure 3",
    "context": "Figure 3: China electrified vehicle sales LHS: Number of electrified vehicles sold. RHS: share of total vehicle sales"
  },
  {
    "figure_id": "F165",
    "report_id": "R007",
    "label": "Figure 5",
    "context": "Figure 5: China electric bus sales LHS: Number of buses sold. RHS: share of of total bus sales"
  },
  {
    "figure_id": "F166",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "Figure 2: Oil intensity of GDP Barrels of oil consumption per \\$1000 of real GDP"
  },
  {
    "figure_id": "F167",
    "report_id": "R007",
    "label": "Figure 4",
    "context": "Figure 4: China gasoline/diesel vehicle sales LHS: Number of gasoline/diesel vehicles sold. RHS: share of total vehicle sales"
  },
  {
    "figure_id": "F168",
    "report_id": "R007",
    "label": "Figure 6",
    "context": "Figure 6: China electric truck sales LHS: Number of trucks sold. RHS: share of total truck sales"
  },
  {
    "figure_id": "F169",
    "report_id": "R007",
    "label": "Figure 7",
    "context": "Figure 7: Global average containership speed"
  },
  {
    "figure_id": "F170",
    "report_id": "R007",
    "label": "Figure 8",
    "context": "Figure 8: Global marine fuels demand vs seaborne trade LHS: Marine fuel consumption, kbd. RHS: Global seaborne trade, million tons"
  },
  {
    "figure_id": "F171",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Deep and diverse capital pools to finance estimated \\~\\$10T AI build-out this cycle ```mermaid graph TD"
  },
  {
    "figure_id": "F172",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Every tech cycle delivers 10x more compute Computing Cycles Over Time, 1960s – Today Devices / Users (MM in Log Scale)"
  },
  {
    "figure_id": "F173",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 3: AI is following the path of past cycles Early Cycle Cloud vs. AI Era Capex ($B)"
  },
  {
    "figure_id": "F174",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Token usage is increasing non-linearly, as advancing capabilities and demand inflection points to a larger cycle than expected"
  },
  {
    "figure_id": "F175",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Capex revisions reflect upside surprises and highlight the challenge of forecasting exponential growth"
  },
  {
    "figure_id": "F176",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 6: The Emerging AI Infrastructure Financing Stack # The Emerging AI Infrastructure Financing Stack A multi-asset ecosystem matching capital to AI infrastructure risk, return and duration The AI build-out should be support"
  },
  {
    "figure_id": "F177",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Global Individual and Institutional Capital Pools of \\$256T represent \\~\\$4% of the estimated \\$10T needed to finance AI build-out Asset Owner Pools ($T)"
  },
  {
    "figure_id": "F178",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Insurance capital skews toward fixed income Life Insurance Asset Allocation"
  },
  {
    "figure_id": "F179",
    "report_id": "R008",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Pension portfolios are more diverse across asset classes vs. insurance capital"
  },
  {
    "figure_id": "F180",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Sovereign Wealth Fund capital skews the most toward alternatives and direct investments... Sovereign Wealth Funds Asset Allocation"
  },
  {
    "figure_id": "F181",
    "report_id": "R008",
    "label": "Exhibit 11",
    "context": "Exhibit 11: ... and within alternatives, infrastructure has become an increasingly core part of sovereign wealth funds' portfolios Sovereign Wealth Funds Illiquid Alternatives Allocation"
  },
  {
    "figure_id": "F182",
    "report_id": "R008",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We see \\$3.2T of data center capex spend through 2028 Updated Data Center Capex – Growing Role of Credit Markets ```mermaid graph TD"
  },
  {
    "figure_id": "F183",
    "report_id": "R008",
    "label": "Exhibit 13",
    "context": "Importantly our credit strategists, do not expect a financing bottleneck, citing significant credit market capacity and growing demand for higher-quality private credit mandates that are well suited to data center financing. They recently revisited their analy"
  },
  {
    "figure_id": "F184",
    "report_id": "R008",
    "label": "Exhibit 14",
    "context": "40.3% (dashed line) indicates the historical average percentage of US nominal GDP."
  },
  {
    "figure_id": "F185",
    "report_id": "R008",
    "label": "Exhibit 15",
    "context": "Exhibit 15: US Investment Grade Debt Represents over Half of Liquid, Public Debt Global Public Debt Outstanding"
  },
  {
    "figure_id": "F186",
    "report_id": "R008",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Global Equity Market Cap Exceeds \\$150T # Global Equity Market Cap by Region Market Capitalization (USD Trillions)"
  },
  {
    "figure_id": "F187",
    "report_id": "R008",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Global IPO volume in 2025 was nearly 50% below historical average levels as a % of nominal GDP; A hypothetical scenario in which global IPO volume moves back to average/peak levels as a % of US nominal GDP would represen"
  },
  {
    "figure_id": "F188",
    "report_id": "R008",
    "label": "Exhibit 19",
    "context": "Exhibit 19: On a broader level, global equity issuance volume in 2025 was more than 33% below historical average levels as a % of nominal GDP; A hypothetical scenario in which global ECM volume moves back to average/peak levels as a"
  },
  {
    "figure_id": "F189",
    "report_id": "R008",
    "label": "Exhibit 18",
    "context": "Exhibit 18: US IPO volume in 2025 was 50% below historical average levels as a % of nominal GDP; A hypothetical scenario in which US IPO volume moves back to average/peak levels as a % of US nominal GDP would represent \\~\\$165B/\\$45"
  },
  {
    "figure_id": "F190",
    "report_id": "R008",
    "label": "Exhibit 20",
    "context": "Exhibit 20: In the US, equity issuance volume in 2025 was 25% below historical average levels as a % of nominal GDP; A hypothetical scenario in which US ECM volume moves back to average/peak levels as a % of US nominal GDP would rep"
  },
  {
    "figure_id": "F191",
    "report_id": "R008",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We observe a modest inverse relationship between the total IPO volume in a given year and the concentration of volume in the top 10 IPOs in that year"
  },
  {
    "figure_id": "F192",
    "report_id": "R008",
    "label": "Exhibit 22",
    "context": "Exhibit 22: 2010 had the highest volume among the top 10 global IPOs in aggregate Top 10 IPOs Volume ($B, Global)"
  },
  {
    "figure_id": "F193",
    "report_id": "R008",
    "label": "Exhibit 23",
    "context": "Exhibit 23: The top 10 largest IPOs annually have historically represented 23% of global volume on average Top 10 IPOs as % of Total Volume (Global)"
  },
  {
    "figure_id": "F194",
    "report_id": "R008",
    "label": "Exhibit 24",
    "context": "Exhibit 24: 2026 money market net flows have softened while equity and bond flows have increased, suggesting investor risk appetite has grown Money Market vs Long-Term Flows ($B)"
  },
  {
    "figure_id": "F195",
    "report_id": "R008",
    "label": "Exhibit 25",
    "context": "Exhibit 25: \\$4.9T dry powder across private market funds, with \\$360B of infrastructure dry powder representing 7% of overall private markets dry powder $4.9Tn as of March '26"
  },
  {
    "figure_id": "F196",
    "report_id": "R008",
    "label": "Exhibit 26",
    "context": "Exhibit 26: We estimate there's \\~\\$2.5T in excess balance sheet capacity in aggregate across the large and super-regional banks in our coverage Large and Super-Regional Banks Coverage (Cat. I-IV): Excess Capital & Implied Balance"
  },
  {
    "figure_id": "F197",
    "report_id": "R008",
    "label": "Exhibit 27",
    "context": "Exhibit 27: The top 5/10 stocks make up 28%/39% of S&P 500 market cap"
  },
  {
    "figure_id": "F198",
    "report_id": "R008",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Tech makes up 50% of the S&P 500 market cap"
  },
  {
    "figure_id": "F199",
    "report_id": "R008",
    "label": "Exhibit 29",
    "context": "Exhibit 29: S&P 500 concentration has made new highs over the past several years"
  },
  {
    "figure_id": "F200",
    "report_id": "R008",
    "label": "Exhibit 30",
    "context": "Exhibit 30: The Nasdaq 100 is notably more concentrated than the S&P 500 and is primarily tech focused"
  },
  {
    "figure_id": "F201",
    "report_id": "R008",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Megacap stock dispersion has risen since 2025"
  },
  {
    "figure_id": "F202",
    "report_id": "R010",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Weekly change in yield in both JGB and"
  },
  {
    "figure_id": "F203",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Japan Corporate Goods price Index"
  },
  {
    "figure_id": "F204",
    "report_id": "R010",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Nikkei CPI T Index (y/y) vs. Nationwide CPI food less fresh food"
  },
  {
    "figure_id": "F205",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Nationwide CPI inflation excluding special factors"
  },
  {
    "figure_id": "F206",
    "report_id": "R010",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Polymarket: probability of Strait of Hormuz traffic returning to normal versus 5y JGB yield"
  },
  {
    "figure_id": "F207",
    "report_id": "R010",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 5y JGB fair value versus actual yield level"
  },
  {
    "figure_id": "F208",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1: HDD Production Volume YoY and Share Prices of TDK & Nidec"
  },
  {
    "figure_id": "F209",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: HDD Supply Chain ```mermaid graph TD"
  },
  {
    "figure_id": "F210",
    "report_id": "R015",
    "label": "Figure 1",
    "context": "Figure 1: Gold diverging from oil"
  },
  {
    "figure_id": "F211",
    "report_id": "R015",
    "label": "Figure 2",
    "context": "Figure 2: 10y US Treasury nominal yield more closely related to Dec'26 Brent than front month (where coefficient of determination is 0.51)"
  },
  {
    "figure_id": "F212",
    "report_id": "R015",
    "label": "Figure 2",
    "context": "Figure 3: 10y real rates have followed Dec Fed pricing"
  },
  {
    "figure_id": "F213",
    "report_id": "R015",
    "label": "Figure 4",
    "context": "Figure 4: Gold Dec'26 and Fed Dec'26"
  },
  {
    "figure_id": "F214",
    "report_id": "R015",
    "label": "Figure 5",
    "context": "Figure 5: Gold demand weaker in key categories"
  },
  {
    "figure_id": "F215",
    "report_id": "R015",
    "label": "Figure 6",
    "context": "Figure 6: Recycled gold in Q1 of 366 tonnes supports full year assumption"
  },
  {
    "figure_id": "F216",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 1: Mega-deals dominate the M&A recovery 12m rolling sum of M&A deals globally"
  },
  {
    "figure_id": "F217",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "Exhibit 2: European M&A remains subdued 12m rolling sum of M&A deals in Europe"
  },
  {
    "figure_id": "F218",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Asset disposals rise to a record strategic priority UK CFO Survey: Share of respondents prioritising asset disposals over the next 12 months (%)"
  },
  {
    "figure_id": "F219",
    "report_id": "R016",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Activity is increasingly driven by cross-border flows 12m rolling sum of M&A deals in Europe"
  },
  {
    "figure_id": "F220",
    "report_id": "R016",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Small caps tend to be correlated with our European M&A Candidates basket Price performance of GS M&A Candidates Basket (GSTRACQN) vs. STOXX 600 and Small vs. Large caps (y/y chg, %)."
  },
  {
    "figure_id": "F221",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Exhibit 6: The M&A Candidates basket (GSTRACQN) trades at a heavy discount to the market GSTRACQN vs. SXXP"
  },
  {
    "figure_id": "F222",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 7: STOXX Small are close to the deepest discount historically against STOXX Large 12m fwd P/E from Small caps vs. Large caps (premium/discount)"
  },
  {
    "figure_id": "F223",
    "report_id": "R016",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Year-to-date performance has been fully driven by EPS growth"
  },
  {
    "figure_id": "F224",
    "report_id": "R016",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Cross-asset performance # Global Strategy Views: Indices and Asset Classes Exhibit 11: GS forecasts across assets"
  },
  {
    "figure_id": "F225",
    "report_id": "R016",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Expected earnings growth and revisions by sector (%) Local currency Exhibit 14: STOXX Europe 600 EPS revisions & earnings sentiment # STOXX Europe 600 Supersectors # Exhibit 15: Our recommendations STOXX Europe 600; su"
  },
  {
    "figure_id": "F226",
    "report_id": "R016",
    "label": "Exhibit 17",
    "context": "Exhibit 17: 3-month sector performance Total Return (€) 3m Total Return Performance"
  },
  {
    "figure_id": "F227",
    "report_id": "R016",
    "label": "Exhibit 16",
    "context": "Exhibit 16: 1-week sector performance Total Return (€) 1w Total Return Performance"
  },
  {
    "figure_id": "F228",
    "report_id": "R016",
    "label": "Exhibit 18",
    "context": "Exhibit 18: YTD sector performance Total Return (€) YTD Total Return Performance"
  },
  {
    "figure_id": "F229",
    "report_id": "R016",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Cyclicals vs. Defensives Cyclicals = Equal Weighted: Industrials, Financials and Cons Discretionary. Defensives = Equal Weighted: Utilities, Health Care, Com Services, Cons Staples"
  },
  {
    "figure_id": "F230",
    "report_id": "R016",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Value vs. Growth price performance MSCI indices"
  },
  {
    "figure_id": "F231",
    "report_id": "R016",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Small-cap vs. Large-cap price performance US: Russell 2000 vs. SPX; Europe: STOXX Small vs. STOXX Europe Large"
  },
  {
    "figure_id": "F232",
    "report_id": "R016",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Momentum vs. Market MSCI indices"
  },
  {
    "figure_id": "F233",
    "report_id": "R016",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Thematic basket relative performance # Sub-Sector Performance Exhibit 24: 1-week sub-sector price performance"
  },
  {
    "figure_id": "F234",
    "report_id": "R016",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Thematic basket relative performance # Sub-Sector Performance Exhibit 24: 1-week sub-sector price performance 1w Price Performance"
  },
  {
    "figure_id": "F235",
    "report_id": "R016",
    "label": "Exhibit 25",
    "context": "Exhibit 25: YTD Sub-sector price performance YTD Price Performance"
  },
  {
    "figure_id": "F236",
    "report_id": "R016",
    "label": "Exhibit 26",
    "context": "Exhibit 26: International Exposure Baskets Relative performance vs. SXXP (EUR)"
  },
  {
    "figure_id": "F237",
    "report_id": "R016",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Domestic Exposure Baskets Relative performance vs. SXXP (EUR)"
  },
  {
    "figure_id": "F238",
    "report_id": "R016",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Shareholder Return Baskets Relative performance vs. SXXP (EUR)"
  },
  {
    "figure_id": "F239",
    "report_id": "R016",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Fundamental Thematic Baskets Relative performance vs. SXXP (EUR)"
  },
  {
    "figure_id": "F240",
    "report_id": "R016",
    "label": "Exhibit 33",
    "context": "Exhibit 33: STOXX Europe 600 12m fwd P/E"
  },
  {
    "figure_id": "F241",
    "report_id": "R016",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Global valuation range 12m fwd P/E multiple. Data since 2000"
  },
  {
    "figure_id": "F242",
    "report_id": "R016",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Market implied ERP Pan-Europe"
  },
  {
    "figure_id": "F243",
    "report_id": "R016",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Europe STOXX 600 and Europe Composite PMI Europe STOXX 600 (Y/Y % Chg) and Europe Composite PMI (RHS)"
  },
  {
    "figure_id": "F244",
    "report_id": "R016",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Cyclicals vs. Defensives and Europe Composite PMI Europe Cyclicals vs. Defensives (Y/Y % Chg) and Europe Composite PMI (RHS)"
  },
  {
    "figure_id": "F245",
    "report_id": "R016",
    "label": "Exhibit 39",
    "context": "Exhibit 39: MSCI Europe Value vs. Growth and US 10y Bond Yield MSCI Europe Value vs. Growth (Y/Y % Chg) and US 10y Bond Yield (Y/Y Chg, RHS)"
  },
  {
    "figure_id": "F246",
    "report_id": "R016",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Europe STOXX Small vs. Large and EUR/USD Europe STOXX Small vs. Europe STOXX Large (Y/Y % Chg) and EUR/USD (Y/Y % Chg, RHS)"
  },
  {
    "figure_id": "F247",
    "report_id": "R016",
    "label": "Exhibit 41",
    "context": "Exhibit 41: 1-month rolling flows from Global investors into European equities Weekly fund flows (EPFR Country Flows Database)"
  },
  {
    "figure_id": "F248",
    "report_id": "R016",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Calendarised flows from Global investors into European equities Weekly fund flows (EPFR Country Flows Database)"
  },
  {
    "figure_id": "F249",
    "report_id": "R016",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Flows into developed Europe equity from Foreign and Domestic Investors 1-month rolling sum of weekly fund flows (EPFR Country Flows Database)"
  },
  {
    "figure_id": "F250",
    "report_id": "R016",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Ownership of Euro area equities"
  },
  {
    "figure_id": "F251",
    "report_id": "R016",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Implied volatility (3-month ATM)"
  },
  {
    "figure_id": "F252",
    "report_id": "R016",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Normalised skew (3-month, 25 delta)"
  },
  {
    "figure_id": "F253",
    "report_id": "R016",
    "label": "Exhibit 47",
    "context": "Exhibit 47: STOXX Europe 600 return dispersion"
  },
  {
    "figure_id": "F254",
    "report_id": "R016",
    "label": "Exhibit 48",
    "context": "Exhibit 48: 1-month average pairwise correlation"
  },
  {
    "figure_id": "F255",
    "report_id": "R016",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Macro-data Assessment Platform (MAP) Economic surprise. GS Proprietary Index"
  },
  {
    "figure_id": "F256",
    "report_id": "R016",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Current Activity Index (CAI) GS Proprietary Index"
  },
  {
    "figure_id": "F257",
    "report_id": "R016",
    "label": "Exhibit 55",
    "context": "Exhibit 55: GS Financial Conditions Index (GSFCI) GS Proprietary Index"
  },
  {
    "figure_id": "F258",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Monthly new 5G base station additions: Apr 2026 deployment at 51k units, or $16\\%$ YoY"
  },
  {
    "figure_id": "F259",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: 5G base station deployment by quarter: 1Q26 deployment decreased QoQ"
  },
  {
    "figure_id": "F260",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Base station production was $-19\\%$ YoY in Apr 2026 Exhibit 6: The number of newly installed 5G base stations in China was up to 51k units in Apr 2026 from 49k units in Mar 2026"
  },
  {
    "figure_id": "F261",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Base station production was $-19\\%$ YoY in Apr 2026 Exhibit 6: The number of newly installed 5G base stations in China was up to 51k units in Apr 2026 from 49k units in Mar 2026"
  },
  {
    "figure_id": "F262",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Apr 2026 base station export volumes were -9.1% YoY"
  },
  {
    "figure_id": "F263",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Fiber cable production was down 16% YoY in Apr 2026"
  },
  {
    "figure_id": "F264",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Fiber preform import volume decreased $7\\%$ MoM to 33 tons in Apr 2026"
  },
  {
    "figure_id": "F265",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Fiber cable export volumes were up $9\\%$ YoY to 4,466 tons in Apr 2026"
  },
  {
    "figure_id": "F266",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "Exhibit 11: CCL export ASP increased $67\\%$ YoY or increased $9\\%$ MoM in Apr 2026"
  },
  {
    "figure_id": "F267",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China's PCB net export volume is expected to rise as domestic PCB production capacity increases"
  },
  {
    "figure_id": "F268",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Major TW telecom companies' aggregate revenue was $+6\\%$ YoY in Apr 2026 (vs. $+6\\%$ YoY in Mar 2026)"
  },
  {
    "figure_id": "F269",
    "report_id": "R017",
    "label": "Exhibit 14",
    "context": "Exhibit 14: China Mobile's 5G user penetration rate reached $6\\%$ by the end of 1Q26"
  },
  {
    "figure_id": "F270",
    "report_id": "R017",
    "label": "Exhibit 15",
    "context": "Exhibit 15: China Telecom's 5G user penetration rate reached $71\\%$ by the end of 1Q26"
  },
  {
    "figure_id": "F271",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Among the belly coupon swaps, the GN II/FN 4.5s swap has diverged from the GN II/FN 3.5s and 4.0s swaps over the past few months"
  },
  {
    "figure_id": "F272",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The price of the GN II/FN 4.5s swap appreciated just as GN TBAs traded to a shorter duration vs FN TBAs"
  },
  {
    "figure_id": "F273",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The share of refinance loans in recent GN II 4.5s issuance has exceeded that in FN 4.5s"
  },
  {
    "figure_id": "F274",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The size of the outstanding float is most comparable across GNs and conventionals (UMBS) in the 4.0% coupon Conventional float excludes balances locked in CMOs, held by the Fed or trade as specified pools. GN float is ba"
  },
  {
    "figure_id": "F275",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Treasury OAS for prime jumbo super senior PT 5.5s has tightened as mortgage rates moved higher over the past three months Treasury OAS for prime jumbo SSNR PT 5.5s tranches that are priced closest to par"
  },
  {
    "figure_id": "F276",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Recent OAS differentials between prime jumbo SSNRs and FN TBAs appear fair, adjusted for collateral rate incentive Polynomial best-fit between the collateral rate incentive and the OAS differential between the closest-to"
  },
  {
    "figure_id": "F277",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Prime Jumbo deal arb has continued to decline in line with lower GWACs Deal pricing and GWAC computed from sample deals available for the displayed months"
  },
  {
    "figure_id": "F278",
    "report_id": "R018",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Deal prices are trading below fair value estimates, stemming from negative rate incentives Fair value estimate calculated based on the Optimal Blue 30-year conforming fixed rate and closest-to-par FN TBA as of deal prici"
  },
  {
    "figure_id": "F279",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Prime jumbo issuance volume has remained healthy throughout 2026 Prime jumbo issuance volumes by pricing calendar year and month Prime Jumbo Issuance Volumes"
  },
  {
    "figure_id": "F280",
    "report_id": "R018",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Total prime issuance is also largely tracking 2025 volumes Prime RMBS issuance volumes by pricing calendar year and month; prime deals include prime jumbo and agency-eligible collateral Prime Issuance Volumes"
  },
  {
    "figure_id": "F281",
    "report_id": "R018",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Prepays slowed in May as mortgage rates remain relatively high Prepays for fixed rate, all WALA prime jumbo loans. Optimal Blue 30-year conforming fixed rate displayed at a 2-month lag"
  },
  {
    "figure_id": "F282",
    "report_id": "R018",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Prepays by GWAC declined month-over-month Prepays for fixed rate, 6-36 WALA prime jumbo loans by GWAC bucket and factor date"
  },
  {
    "figure_id": "F283",
    "report_id": "R018",
    "label": "Exhibit 13",
    "context": "Exhibit 13: The University of Michigan Consumer Sentiment Index fell to a new record low in May, with an average of 48% of consumers citing high prices as eroding their financial wellbeing University of Michigan Consumer sentiment i"
  },
  {
    "figure_id": "F284",
    "report_id": "R018",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Consumer sentiment is worse for younger and lower income consumers, but only marginally so Consumer sentiment by income tercile (left panel) and age bracket (right panel)"
  },
  {
    "figure_id": "F285",
    "report_id": "R018",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Conference Board data came in at the 40th percentile since 1980, far from the record lows of the University of Michigan survey"
  },
  {
    "figure_id": "F286",
    "report_id": "R018",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Higher income consumers have experienced a much greater improvement in their financial situation vs. lower income consumers Percentage of Respondents Concerned About Making Ends Meet in 0–6 Months (left panel) and 7–12 m"
  },
  {
    "figure_id": "F287",
    "report_id": "R018",
    "label": "Exhibit 17",
    "context": "Exhibit 17: With tax refund season fully in the rearview, seasonal drops in delinquencies have largely been in line with historical norms Drops in D30+ rates during tax season over time segmented by sector"
  },
  {
    "figure_id": "F288",
    "report_id": "R018",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Despite decreases in sentiment, delinquencies are not yet showing any clear impact from the conflict in the middle east D30+ rates for a sample of 142 subprime auto deals originated prior to 2024"
  },
  {
    "figure_id": "F289",
    "report_id": "R018",
    "label": "Exhibit 22",
    "context": "Exhibit 22: FN current coupon OAS and percentiles"
  },
  {
    "figure_id": "F290",
    "report_id": "R018",
    "label": "Exhibit 24",
    "context": "Exhibit 24: 30-year conventional MBS index excess returns by coupon As of 5/27/2026 Exhibit 26: Agency MBS index duration"
  },
  {
    "figure_id": "F291",
    "report_id": "R018",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Nominal current coupon basis vs. the key-rate duration weighted 2s5s10s30s curve"
  },
  {
    "figure_id": "F292",
    "report_id": "R018",
    "label": "Exhibit 25",
    "context": "Exhibit 25: 15-year conventional MBS index excess returns by coupon As of 5/27/2026 Exhibit 27: Agency MBS index convexity"
  },
  {
    "figure_id": "F293",
    "report_id": "R018",
    "label": "Exhibit 28",
    "context": "Exhibit 28: MBA conventional and government loan refinance application index"
  },
  {
    "figure_id": "F294",
    "report_id": "R018",
    "label": "Exhibit 29",
    "context": "Exhibit 29: MBA refinance loan application index for FHA and VA loans"
  },
  {
    "figure_id": "F295",
    "report_id": "R018",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Refinance application volume (based on FN RALI \\$ index) vs. mortgage rates"
  },
  {
    "figure_id": "F296",
    "report_id": "R018",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Purchase applications by week"
  },
  {
    "figure_id": "F297",
    "report_id": "R018",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Mortgage basis (current coupon mortgage rate -5/10-Year Treasury rate) and IG OAS"
  },
  {
    "figure_id": "F298",
    "report_id": "R018",
    "label": "Exhibit 33",
    "context": "Exhibit 33: TBA coupon stack valuations Note: As of May 27, 2026. Exhibit 34: Excess returns year to date net of Treasury hedges across asset classes"
  },
  {
    "figure_id": "F299",
    "report_id": "R018",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Agency MBS gross monthly issuance"
  },
  {
    "figure_id": "F300",
    "report_id": "R018",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Agency CMBS index spread and long-term average"
  },
  {
    "figure_id": "F301",
    "report_id": "R018",
    "label": "Exhibit 37",
    "context": "Exhibit 37: MBS Trading volumes Exhibit 38: Seasonal trends in 1-family existing home sales ('000s of units)"
  },
  {
    "figure_id": "F302",
    "report_id": "R018",
    "label": "Exhibit 39",
    "context": "Exhibit 39: FX-adjusted yields offered by current coupon GNs vs. 10-year JGBs (hedged using 3-month FX forwards)"
  },
  {
    "figure_id": "F303",
    "report_id": "R018",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Cumulative inflows into taxable mutual funds and ETFs by calendar year Exhibit 41: YoY change in Case Shiller U.S. National Home Price NSA index"
  },
  {
    "figure_id": "F304",
    "report_id": "R018",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Cumulative inflows into taxable mutual funds and ETFs by calendar year Exhibit 41: YoY change in Case Shiller U.S. National Home Price NSA index"
  },
  {
    "figure_id": "F305",
    "report_id": "R018",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Cumulative HPA by calendar year"
  },
  {
    "figure_id": "F306",
    "report_id": "R018",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Excess spread offered by IG corporates vs. MBS OAS"
  },
  {
    "figure_id": "F307",
    "report_id": "R018",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Current coupon MBS yields vs yield of the IG corporate index"
  },
  {
    "figure_id": "F308",
    "report_id": "R018",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Bloomberg MBS index yield vs. IG corporate index yield"
  },
  {
    "figure_id": "F309",
    "report_id": "R018",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Inflows into taxable bond funds and ETFs"
  },
  {
    "figure_id": "F310",
    "report_id": "R018",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Agency MBS issuance—monthly"
  },
  {
    "figure_id": "F311",
    "report_id": "R018",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Agency CMO issuance—monthly"
  },
  {
    "figure_id": "F312",
    "report_id": "R018",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Agency CMO issuance—monthly by agency"
  },
  {
    "figure_id": "F313",
    "report_id": "R018",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Floater share of CMO tranches"
  },
  {
    "figure_id": "F314",
    "report_id": "R018",
    "label": "Exhibit 51",
    "context": "Exhibit 51: DUS issuance volume—monthly"
  },
  {
    "figure_id": "F315",
    "report_id": "R018",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Freddie Multi PC issuance—monthly"
  },
  {
    "figure_id": "F316",
    "report_id": "R018",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Agency CMBS REMICs—issuance volume by agency Freddie K volumes are based on the FHMS shelf and exclude small balance deals."
  },
  {
    "figure_id": "F317",
    "report_id": "R018",
    "label": "Exhibit 54",
    "context": "Exhibit 54: BBB CMBS cash spreads vs. HY corporates"
  },
  {
    "figure_id": "F318",
    "report_id": "R018",
    "label": "Exhibit 55",
    "context": "Exhibit 55: BBB CMBX vs. HY synthetic spreads"
  },
  {
    "figure_id": "F319",
    "report_id": "R018",
    "label": "Exhibit 56",
    "context": "Exhibit 56: AAA CMBS cash spreads vs. IG corporates"
  },
  {
    "figure_id": "F320",
    "report_id": "R018",
    "label": "Exhibit 57",
    "context": "Exhibit 57: AAA CMBX vs. IG synthetic spreads"
  },
  {
    "figure_id": "F321",
    "report_id": "R018",
    "label": "Exhibit 58",
    "context": "Exhibit 58: AAA and BBB- CMBX spreads"
  },
  {
    "figure_id": "F322",
    "report_id": "R018",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Conduit CMBS annual issuance Conduit CMBS Issuance"
  },
  {
    "figure_id": "F323",
    "report_id": "R018",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Conduit CMBS weighted average coupon by maturity date"
  },
  {
    "figure_id": "F324",
    "report_id": "R018",
    "label": "Exhibit 61",
    "context": "Exhibit 61: CMBS conduit at-issuance loan-to-value (LTV, %)"
  },
  {
    "figure_id": "F325",
    "report_id": "R018",
    "label": "Exhibit 62",
    "context": "Exhibit 62: AAA Auto ABS spreads to Treasuries"
  },
  {
    "figure_id": "F326",
    "report_id": "R018",
    "label": "Exhibit 63",
    "context": "Exhibit 63: AAA Credit card ABS spreads to Treasuries"
  },
  {
    "figure_id": "F327",
    "report_id": "R018",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Subprime auto 60+ day delinquency rates by deal vintage (% by balance)"
  },
  {
    "figure_id": "F328",
    "report_id": "R018",
    "label": "Exhibit 65",
    "context": "Exhibit 65: Subprime auto 3-month average CPR by deal vintage"
  },
  {
    "figure_id": "F329",
    "report_id": "R018",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Subprime auto 3-month average CDR by deal vintage"
  },
  {
    "figure_id": "F330",
    "report_id": "R018",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Subprime auto annualized loss rates by deal vintage"
  },
  {
    "figure_id": "F331",
    "report_id": "R018",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Unsecured consumer loan 60+ day delinquency rates by deal vintage (% by balance)"
  },
  {
    "figure_id": "F332",
    "report_id": "R018",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Unsecured consumer loan 3-month average CPR by deal vintage"
  },
  {
    "figure_id": "F333",
    "report_id": "R018",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Unsecured consumer loan 3-month average CDR by deal vintage"
  },
  {
    "figure_id": "F334",
    "report_id": "R018",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Unsecured consumer loan annualized loss rates by deal vintage"
  },
  {
    "figure_id": "F335",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The Number of Goals Score by a Football Team Broadly Follows a Poisson Distribution"
  },
  {
    "figure_id": "F336",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Elo vs FIFA/Coca-Cola Rankings"
  },
  {
    "figure_id": "F337",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Goal-Scoring Potential Matters; Some Signs of a “Winner’s Slump” Effect After Winning the World Cup"
  },
  {
    "figure_id": "F338",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "Exhibit 4: What Matters in Our Model"
  },
  {
    "figure_id": "F339",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Probabilities of Advancement in the 2026 World Cup"
  },
  {
    "figure_id": "F340",
    "report_id": "R019",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Breaking Down the Winning Probability Spain: Probability of Winning the 2026 World Cup"
  },
  {
    "figure_id": "F341",
    "report_id": "R019",
    "label": "Exhibit 9",
    "context": "Exhibit 9: The Luck of the Draw"
  },
  {
    "figure_id": "F342",
    "report_id": "R019",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Comparing Our Model Probabilities to the Market Probability of Winning the World Cup"
  },
  {
    "figure_id": "F343",
    "report_id": "R019",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Assessing Our Model's Past Performance"
  },
  {
    "figure_id": "F344",
    "report_id": "R019",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The Predicted Group Standings FIFA World Cup 2026 - Final Group Standings (Prediction as of 29 May 2026) Qualified (1st / 2nd) Qualified as best-3rd Eliminated"
  },
  {
    "figure_id": "F345",
    "report_id": "R019",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The Predicted Group Standings FIFA World Cup 2026 - Final Group Standings (Prediction as of 29 May 2026) Qualified (1st / 2nd) Qualified as best-3rd Eliminated"
  }
]