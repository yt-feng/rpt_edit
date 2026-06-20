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
    "title": "GS：外汇市场的真正拐点不是地缘冲突缓和，而是美联储的鹰派姿态切换",
    "digest": "[wechat_article.md]\n# GS：外汇市场的真正拐点不是地缘冲突缓和，而是美联储的鹰派姿态切换\n\n过去一周，外汇市场经历了一场典型的“假突破”。地缘冲突缓和的消息一度推动新兴市场货币大幅反弹，投资者似乎看到了风险偏好回归的曙光。然而，随后美联储的鹰派表态几乎完全抹去了这些涨幅。市场参与者很容易将这理解为一次普通的“利好出尽”，但GS最新的外汇策略报告提出了一个更值得深思的判断：市场正在经历的不是情绪波动，而是定价锚点的根本性切换。\n\n这份报告的核心洞察在于，美联储的沟通方式发生了超出预期的变化。过去几年，市场习惯了美联储相对透明、可预测的政策指引框架。但这次会议传递出的信号，无论是鹰派程度还是沟通方式，都让市场措手不及。更重要的是，这种变化并非孤立事件，而是与AI驱动的美国需求韧性、全球央行沟通范式演变等结构性力量交织在一起。这意味着，外汇市场的定价逻辑正在被重塑，而许多投资者可能仍在使用旧地图。\n\n以下是我们从这份GS报告中提炼出的五个关键判断，以及它们对全球资产配置的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美联储的鹰派意外比地缘风险缓和更能决定美元走向，因为市场从未真正为战争定价\n\n报告首先回应了一个最直观的问题：为什么地缘冲突缓和这种典型的“美元利空”，会被美联储的鹰派表态轻易压制？GS的分析给出了一个反直觉的答案——市场从来就没有为地缘风险进行过显著定价。\n\n报告指出，市场一直存在“冲突终将解决”的基线预期，因此从未在价格中计入大量的风险溢价。相比之下，美联储鹰派立场的意外程度要大得多。从历史经验看，利率差异对美元的影响比油价更大、更持续。因此，即使地缘风险缓和暂时削弱了美元的避险吸引力，美联储更鹰派的立场也足以提供一个更强大的美元支撑因素。\n\n这并不意味着油价对美元不再重要。报告特别指出，油价下跌恰恰是美联储开始\n\n[... middle omitted ...]\n\n模型数据和实时市场动态，一起推演外汇市场下一阶段的定价逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储转鹰，美元走向怎么看？\n\n美元，又要硬了？\n\n鹰派美联储 vs 能源缓和，谁更影响美元？\n\n最近这波行情，核心是美联储的态度转变。相比美伊关系缓和，这次FOMC的鹰派意外更大，也更持久。\n\n1️⃣ **美元：新变量来了**\n   - 这次FOMC的鹰派立场，比市场预期的更硬核\n   - 利率差异对美元的影响，远大于油价变动\n   - 关键是，AI驱动的美国需求才是通胀和增长背后的真推手，不只是油价\n   - 这种“新”的美元支撑，可能会让一些高贝塔货币的carry交易有点难受\n\n2️⃣ **新兴市场carry：高息与低息分化**\n   - 上周新兴货币先涨后跌，低息货币（韩元、捷克克朗、马币）跌幅更猛\n   - 在“美股涨、美债利率涨”的环境里，用欧元或日元来融资，比用美元更香\n   - 墨西哥比索表现强势，跟它和美元的高相关性有关\n   - 拉美这边，可以考虑把巴西雷亚尔换成哥伦比亚比索，巴西大选前政治噪音会增加\n\n3️⃣ **日元：继续磨底**\n   - 日本央行虽然加息，但节奏太慢，根本挡不住利差压力\n   - 美联储更鹰，让USD/JPY上行风险更大\n   - 干预风险还在，直接做多美元/日元不\n\n[... middle omitted ...]\n\nhave a larger and more consistent correlation with the Dollar than oil prices. So unless the Fed’s more hawkish stance proves fleeting as oil prices move lower, we see this as replacing one po\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "GS：中国经济的真实温度，藏在每周高频数据的边际变化里",
    "digest": "[wechat_article.md]\n# GS：中国经济的真实温度，藏在每周高频数据的边际变化里\n\n当市场还在为月度PMI的读数争论不休时，一份来自GS的每周经济追踪报告揭示了一个更微妙的现实：中国经济正在经历的不是简单的“复苏”或“放缓”，而是一个由多重力量拉扯、板块剧烈分化的“再均衡”过程。这份6月18日发布的报告，通过四大类高频指标——消费与出行、生产与投资、其他宏观活动、市场与政策——拼凑出一幅比任何单一数据都更立体的图景。\n\n核心判断是：经济活动的“量”在边际上企稳，但“价”的信号依然疲弱，且结构性分化正在加剧。这意味着，对于产业决策者和投资者而言，整体宏观数字的参考价值正在下降，真正重要的是捕捉不同板块内部边际变化的拐点。这份报告的价值不在于给出一个“好”或“坏”的结论，而在于提供了每周更新、可交叉验证的观察框架，让读者有能力在官方数据发布之前，提前感知水温的变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 房地产市场出现了一个值得警惕的背离：交易量回暖未能阻止价格继续探底\n\n报告中最引人注目的信号来自房地产市场。30城新房成交量在最近一周小幅上升，并且高于去年同期水平；16城二手房成交量也基本持平于高位。从“量”的角度看，政策松绑后的脉冲效应似乎仍在持续，市场并没有出现断崖式下跌。\n\n然而，量稳的背后是价的持续疲软。国家统计局70城二手房价格指数在5月继续下降。更令人担忧的是，报告追踪的多个独立数据源——中原、贝壳、诸葛、国信达——所构建的房价指数均显示，当前价格水平已显著低于2025年，甚至逼近或低于2019年基准。这意味着，以价换量仍然是市场的主旋律。卖方为了促成交易，正在不断下调预期价格。\n\n这个背离的含义是深远的。交易量的企稳，更多反映的是积压需求的释放和业主的主动降价，而非市场信心的根本性修复。只要价格下跌预期没有扭转，潜\n\n[... middle omitted ...]\n\n不仅分享报告本身，更会围绕这些未解问题展开持续、深入的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月高频数据：一线楼市回暖，消费还在磨底\n\n📊 6月经济快照\n\n上周30城新房成交量小幅回升，同比高于去年同期\n二手房成交量持平，但同比仍为正\n70城二手房价5月持续下跌，租金收益率稳定在1.9%\n\n📉 消费端：出行意愿偏弱\n\n国内航班量环比回升，但同比仍低于去年\n航班取消率下降，但仍在5%高位\n交通拥堵指数微升，但Morning Consult消费者信心指数小幅下行\n\n🏭 生产端：钢铁需求边际改善\n\n钢材需求/产量均小幅回升，但同比仍弱\n沿海省份煤炭日耗量高于去年同期\n地方专项债发行加速，今年累计已达1.67万亿\n\n🔍 关键信号\n\n1️⃣ 房地产：新房成交改善，但二手房价仍在下跌，说明市场分化明显\n2️⃣ 消费：出行数据偏弱，消费者信心不足，消费复苏还需观察\n3️⃣ 生产：钢铁需求边际改善，但力度有限，经济修复节奏偏慢\n\n📌 值得关注：6月18日国内汽柴油价格下调515/495元/吨，与布伦特油价下跌相关\n\n欢迎一起讨论你对当前经济形势的判断～\n\n#学习笔记\n\n[source_mineru.md]\n## China Economic Activity and Policy Tracker: June 18\n\n[... middle omitted ...]\n\n9210b6433b1e55573d75a73a4c9cec2b.jpg)\n\n<details>\n<summary>line chart</summary>\n\n| Date       | 2019 (Thousand sqm) | 2025 (Thousand sqm) | 2026 (Thousand sqm) |\n|------------|-----------------\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "NOM：央行“叫得凶”和“咬得狠”正在分岔，市场低估了这种分化",
    "digest": "[wechat_article.md]\n# NOM：央行“叫得凶”和“咬得狠”正在分岔，市场低估了这种分化\n\n理解全球央行当前的政策节奏，不能只看加息还是降息。NOM最新一份研报提供了一个更精细的观察框架：用彭博的央行沟通情绪指数，去衡量央行“说了什么”，再与其实际行动对比，看“做了什么”。结论是清晰的——三大央行的言行一致性正在显著分化，而这种分化背后是各自经济基本面和政策约束的根本差异。对于资产定价而言，这意味着一刀切的“全球央行转向”叙事可能已经失效，投资者需要重新校准对不同市场的利率风险定价。\n\n这份报告最值得关注的判断不是某个具体的利率预测，而是它揭示了一个正在发生的结构性变化：央行沟通本身正在成为独立的政策工具，且其可信度和有效性正在因央行的“兑现记录”而出现分化。欧洲央行正在用行动强化其鹰派沟通的可信度，英国央行则在用“按兵不动”削弱其鹰派信号的威慑力，而美联储的新任主席则可能让这类沟通指数本身失去意义。这三条线索，每一条都指向不同的资产配置含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧洲央行正在用行动证明“鹰派不是空话”，这是当前最值得追踪的定价信号\n\nNOM编制的ECBspeak指数已经升至20.7，这是2022年3月以来的最高水平。但更关键的是，与上次加息周期不同，这次欧洲央行在鹰派沟通升温后迅速跟进——在指数达到这一水平时，欧洲央行已经完成了25个基点的加息。而在2022年3月，指数达到类似水平后，欧洲央行等了四个月才启动首次加息。\n\n这种“言行一致”的转变，直接推动了NOM欧洲经济团队上调加息预测：在9月和12月各加25个基点，并延续到2027年3月。这并非简单的预测调整，而是对央行行为模式变化的确认——欧洲央行正在从“落后于曲线”转向“主动管理预期”。\n\n这一变化的底层逻辑在于，欧元区的通胀粘性比预期更强，尤其是第二\n\n[... middle omitted ...]\n\n价。这些问题的答案，将直接影响未来6个月的全球利率交易框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n三大央行“嘴炮”PK行动力\n\n谁在“说狠话”但不动手\n\nECB嘴炮最猛，行动也跟得快；BOE喊得凶但一直按兵不动；Fed的“鹰派发言”可能很快失效。\n\n---\n\n**1/ ECB：说狠话，也敢动手**\n\n某外资投行用彭博的央行发言鹰派指数衡量“嘴炮”程度。ECB的指数飙到20.7，跟2022年3月一样高。但这次不一样：2022年3月喊完，4个月后才加息；这次指数刚涨，ECB当月就加了25bp。嘴炮和行动同步，市场预期今年9月、12月和明年3月还会各加25bp。\n\n**2/ BOE：喊了半天，原地不动**\n\nBOE的鹰派指数只有4.4，比ECB温和得多。更关键的是，昨天会议7:2投票维持利率不变，没动手。而上一个加息周期，指数到3.7时BOE就行动了。这次指数更高反而没动作，研报判断今年不会加息，明年下半年可能降两次25bp。\n\n**3/ 为什么ECB和BOE不同？**\n\n去年4月投行曾判断“央行嘴炮大于行动”，现在看对BOE成立，对ECB不成立。核心差异：ECB利率2.25%被认为低于中性利率，通胀黏性更强，怕第二轮效应；BOE利率3.75%高于中性，劳动力市场已走弱，通胀低于预期。如果能源价格持续下跌，EC\n\n[... middle omitted ...]\n\n the respective policy rates.\n\nThe ECBspeak index has increased most sharply of the three central banks, to currently 20.7, a level last reached in March 2022. Back then, the ECB did not deliv\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R004",
    "title": "GS：中国医药资产被低估的不是基本面，而是全球定价权的再校准",
    "digest": "[wechat_article.md]\n# GS：中国医药资产被低估的不是基本面，而是全球定价权的再校准\n\n当一家全球顶级投行在参加了2026年6月的全球医疗健康大会、与30多家机构投资者交流后，得出了一个看似矛盾的结论——中国医药股年内平均下跌11%，但基本面（临床数据、BD活动）依然强劲——这通常意味着市场正在犯一个经典错误：用短期情绪定价长期资产。\n\nGS这份研报的核心判断值得每一个关注中国医药产业的决策者认真对待：当前中国医药资产的风险回报正在向有利方向倾斜，但驱动下一阶段行情的逻辑，将从“板块整体重估”转向“公司层面的全球竞争力验证”。这不是一个简单的抄底信号，而是一个结构性分化的起点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场真正担心的不是基本面，而是两个“看不见”的政策变量\n\n投资者对中国医药板块的谨慎态度，并非源于对临床数据或研发管线的否定。GS在与投资者的交流中发现，真正压制情绪的是两个政策层面的不确定性。\n\n第一个是中国与美国之间关于BD交易的监管审查。虽然目前尚未出现实质性的阻断案例，但双边监管趋严的预期已经影响了投资者的风险偏好。GS的调研显示，投资者的讨论更多集中在中国监管一侧，因为政策透明度较低。一个值得关注的细节是：多数投资者认为，如果中国监管审查聚焦于平台级技术输出（而非单一资产），结构性变化的概率不大。这意味着，近期的BD交易趋势将成为判断政策影响的关键观测窗口。\n\n第二个是国内医疗反腐对盈利的潜在冲击。这一变量在2023-2024年已经对行业产生过显著影响，但市场仍在评估其持续时间和影响深度。\n\n这两个变量的共同特点是：它们不是对行业长期价值的否定，而是对短期可见度的干扰。GS的判断是，随着催化剂可见度的提升（即将到来的临床数据、BD公告、二季度财报），市场将重新关注基本面本身。\n\n![研报原图 2](as\n\n[... middle omitted ...]\n\n间分享对关键催化剂事件的解读和行业变化的深度分析。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国创新药，正被重新定价\n\n全球视野下的中国医药\n\n最近参加了某外资投行的全球医疗健康大会，和30多家海外机构聊了聊，发现大家对中国医药的态度正在微妙转变。\n\n**1/ 情绪触底，但基本面没变**\n- 中国医药板块年内跌了11%，但临床数据和BD交易依然活跃\n- 股价和基本面明显脱节，部分投资者开始重新评估\n- 风险回报正在向有利方向倾斜，尤其进入下半年\n\n**2/ 中国创新药，全球药企离不开**\n- Gilead透露：约50%的优先BD机会来自或关联中国\n- Pfizer认为：到2030年，中国biotech可能具备全球开发能力\n- 中国创新不再是“低成本替代”，而是真正的创新来源\n\n**3/ 出海逻辑依然清晰**\n- 对外授权仍是主要路径，尤其ADC、双抗领域\n- 但监管不确定性（中美双方）是近期讨论焦点\n- 临床数据能否全球转化，是估值分化的关键\n\n**4/ CDMO：韧性超预期**\n- 药明系、凯莱英等CDMO订单依然强劲\n- GLP-1相关产能扩张是核心看点\n- 估值相对全球同行仍有折价\n\n**5/ 医疗科技：海外执行是关键**\n- 微创机器人海外订单超300台\n- 时代天使海外业务提前盈亏平衡\n-\n\n[... middle omitted ...]\n\nductors, investors highlighted policy overhangs—including evolving China/US regulatory uncertainty around BD and domestic anti-corruption-related earnings risks—as key drivers of weak position\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "JPM：市场误读了资本流动监管，真正的信号是框架重构而非收紧",
    "digest": "[wechat_article.md]\n# JPM：市场误读了资本流动监管，真正的信号是框架重构而非收紧\n\n过去几个月，中国在资本流动领域的多项监管更新引发了市场广泛讨论。多数解读倾向于将其简单归类为“资本管控收紧”，尤其是6月出台的对外投资新规。然而，JPM最新发布的这份研报提出了一个截然不同的核心判断：这些政策调整并非单向收紧，而是一场旨在构建完整资本流动治理框架的结构性努力。市场真正需要关注的，不是短期流动方向，而是这个框架如何重塑人民币汇率、银行业竞争格局以及跨境金融服务的长期逻辑。\n\n这份报告的价值不在于罗列政策条文，而在于提出了一个关键洞察：政策制定者在“前门”和“后门”之间做出了明确的区分——一方面扩大合规渠道的容量和灵活性，另一方面对非正规渠道施加压力。这种“有管理的开放”策略，对不同类型的金融机构意味着截然不同的机遇与风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮政策调整的核心不是限制资本外流，而是建立一套“前门敞开、后门收紧”的治理框架\n\nJPM在报告中系统梳理了过去12个月涉及资本流动的多项监管更新。结论是清晰的：这不是单向的收紧或放松，而是一个混合体。放松的方面包括：跨国公司本外币一体化资金池业务从试点升级为全国性框架，允许企业用一个跨境资金池统一管理境内外本外币资金；境内企业向境外放款的额度提升，且审批制改为备案制；债券通南向通的合格机构名单扩大，QDII额度审批重启；以及境内银行间接向境外企业放贷的严格标准被取消。\n\n收紧的方面同样明确：6月对外投资新规将个人投资者的境外投资纳入监管范围；跨境证券交易监管执法力度加强；以及要求境内企业及时将境外IPO募集资金调回境内。\n\nJPM的判断是，这些措施加在一起，传递的信号不是“关门”，而是“换锁”——让合规渠道更畅通，同时对灰色地带施加更大压力。对于投资者而言，这意味着\n\n[... middle omitted ...]\n\n更多关于政策执行细节的跟踪分析，以及不同银行的竞争壁垒拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币跨境新政，到底谁受益？\n\n**资本流动新格局**\n\n最近人民币跨境政策密集调整，有松有紧，市场关注度很高。某外资投行最新研报的核心判断是：这不是简单的收紧资本外流，而是在搭建一套更完整的跨境流动监管框架。\n\n**1/ 松了什么？**\n- 跨国公司在华现金管理更灵活，本外币资金池调度自由度提升\n- 境内企业对外放款额度增加，从审批制改为备案制\n- 南向债券通参与机构扩容，QDII额度重启审批\n- 境内银行间接离岸贷款限制取消（72号文）\n\n**2/ 紧了什么？**\n- 6月1日对外投资新规，将个人境外投资纳入监管（细则待出）\n- 跨境证券交易监管执法加强\n- 要求企业境外IPO资金及时回流（252号文）\n\n**3/ 对银行的影响**\n- **中行最受益**：外汇存款占集团负债16%（同业平均4%），离岸贷款限制取消后，外汇存款利差有望走阔，成为NIM的正面推动力\n- **渣打、HSBC**：受益于跨国公司现金管理放松、境内企业境外放款灵活性提升，以及人民币国际化加速（点心债、南向通扩容）\n- 香港银行的MCV财富管理业务短期承压，但企业银行（CIB）业务机会被低估\n\n**4/ 对人民币汇率**\n- 短期：\n\n[... middle omitted ...]\n\nmix of relaxation and tightening with differing implications for cross-border flows, and we view them as part of a broader effort to complete a comprehensive capital-flow regulatory framework \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R006",
    "title": "NOM：鲍威尔之后，美联储正经历一场更深刻的权力重构",
    "digest": "[wechat_article.md]\n# NOM：鲍威尔之后，美联储正经历一场更深刻的权力重构\n\n市场对6月FOMC会议的解读大多聚焦于“点阵图转鹰”与“沃什偏鸽”的表层矛盾。但NOM这份研报揭示了一个更值得关注的信号：美联储正在发生的不只是利率路径的摇摆，而是一场围绕数据定义权、通胀框架和机构治理的深层重构。真正重要的不是2026年会不会加息，而是谁来决定“什么算通胀”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 点阵图的鹰派偏移被沃什的措辞对冲，但真正重要的是框架的不确定性\n\n6月点阵图的中位数显示，2026年政策利率将升至3.75%，比当前水平高出半个加息幅度。这一结果明显比市场预期更鹰派。然而，沃什在新闻发布会上的表态却呈现出相反的温度。他将点阵图形容为“用铅笔画的——那种带大橡皮的铅笔”，暗示这些预测随时可能被擦除。他还刻意强调“一半的同事认为利率应该维持在当前水平或更低”，尽管实际上只有一位参与者预期2026年降息。\n\n这种“鹰派数据、鸽派叙事”的组合并非简单的沟通技巧，而是反映出沃什正在尝试重新定义美联储对外沟通的锚点。他更倾向于用定性判断来对冲量化预测的刚性，这本身就是在削弱点阵图作为政策信号的市场权重。\n\n对投资者的含义是：点阵图的参考价值正在下降，沃什的措辞将成为更重要的政策风向标。未来市场对美联储的解读，可能需要从“数点”转向“听词”。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 沃什的“小数点左侧”通胀观，可能系统性降低加息门槛\n\n研报中一个容易被忽略的细节是沃什对通胀目标的表述。当被问及2%的通胀目标时，他回答：“我倾向于关注小数点的左侧。”这意味着他可能将2.0%至2.9%的通胀区间都视为符合2%目标的范畴。\n\n这一表述的潜在影响不容低估。如果美联储正式或非正式地将通胀容\n\n[... middle omitted ...]\n\n式采用“小数点左侧”的通胀目标，长端利率和美元会如何重定价？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储6月按兵不动，但鲍尔放鸽\n\n利率不动，通胀还在涨\n\n美联储6月会议如期没动利率，但点阵图和预测都偏鹰。不过主席鲍尔的发布会，却透着一股鸽味。\n\n🔍 拆开看几个关键点：\n\n1️⃣ 点阵图更鹰了\n2026年利率中位数暗示加息一次（3.75%），比市场预期的3.625%高。18位委员中9位认为至少加一次，只有1位认为该降息。长期利率中位数微降至3.063%，但均值反而升了，说明对中性利率的分歧很大。\n\n2️⃣ 鲍尔给加息预期“降温”\n他说点阵图“都是铅笔画的”，随时能改。还强调“一半同事认为利率应该维持或更低”，尽管今年只有1人主张降息。更关键的是，他说“我关注小数点左边”，暗示2.0%-2.9%的通胀都算达标。\n\n3️⃣ 成立五个工作组\n鲍尔宣布成立五个工作组，分别负责沟通、数据、缩表、生产力和通胀框架。他批评政府统计数据“老派”，想用私营部门的实时数据。这意味着加息门槛可能更高，直到工作组年底出方案。\n\n4️⃣ 核心PCE通胀预计加速\n5月核心PCE通胀预计环比涨0.376%，同比升至3.457%。主要是PPI金融服务价格和进口机票价格推高。超级核心PCE（剔除食品能源住房）预计环比涨0.5%，是1月以来\n\n[... middle omitted ...]\n\nxt few weeks, with task force recommendations targeted for year-end.  \n- Incorporating CPI, PPI, and import prices, we expect core PCE inflation accelerated by $0.376\\%$ m-o-m in May. This tra\n\n[... middle omitted ...]\n\ns available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities International, Inc., US. All rights reserved."
  },
  {
    "id": "R007",
    "title": "JPM：消费股真正的底部不在宏观数据里，而在企业盈利预期的重新校准",
    "digest": "[wechat_article.md]\n# JPM：消费股真正的底部不在宏观数据里，而在企业盈利预期的重新校准\n\n2026年5月的中国零售数据，以-0.6%的同比增速，触发了市场自2022年底以来的第一次月度负增长警报。这份来自JPM的消费策略报告，没有停留在“需求疲软”的简单叙事里。它真正想传递的信号是：市场低估的不是消费何时复苏，而是企业盈利预期需要多大幅度、多长时间的下修。当前板块的估值压缩，可能还没有完全定价二季度业绩期即将出现的密集盈利预警。\n\n这份报告的核心洞察，不是告诉你消费有多差——这一点市场已经反映在股价里——而是帮你在“差”的结构里，找到哪些公司的商业模式能扛住压力，哪些公司会被原料成本和需求双杀。更重要的是，它提醒投资者：现在说“见底”仍为时过早，选股逻辑必须从“买赛道”切换为“买护城河”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 零售数据的结构比总量更值得警惕：耐用品的“高基数陷阱”正在变成“需求真空”\n\n5月零售总额的-0.6%固然是2022年12月以来首次负增长，但更值得关注的是分项数据的结构性恶化。JPM的数据拆解显示，拖累大盘的三大板块——汽车（同比-16%）、家电（-16%）、家具（-9%）——并非单纯因为高基数，而是反映出居民对高单价、高决策成本商品的消费意愿正在系统性收缩。\n\n汽车和家电在2024-2025年经历了政策刺激驱动的集中释放，高基数确实是因素之一。但问题在于，当补贴效应消退后，后续需求并没有自然衔接。家电同比-16%与家具-9%的组合，暗示房地产后周期消费的传导机制已经断裂——即使新房交付量边际改善，消费者也没有像过去那样同步配置家居产品。这意味着，耐用消费品的“以旧换新”政策红利正在快速衰减，而市场此前对2026年下半年销售回弹的预期，可能需要大幅下调。\n\n对投资者而言，这一结构变化意味着：任何\n\n[... middle omitted ...]\n\n报告原文，并围绕“盈利预警密集期的选股策略”做一次专题交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月消费数据，有点冷\n\n📉 消费真的降温了\n\n5月社零同比-0.6%，是2022年12月以来首次转负，比4月的+0.2%和3月的+1.7%都在往下走，也低于市场预期（-0.2%）。\n\n1️⃣ 谁在拖后腿？\n耐用消费品是主要拖累项：\n- 家电：-15.6%\n- 汽车：-16.1%\n- 金银珠宝：-8.9%（虽然比4月的-21%收窄，但金价波动影响还在）\n- 家具：-8.7%\n\n2️⃣ 哪些品类还在涨？\n前5名：软饮+6%、烟酒+5%、医药+4%、服装+4%、化妆品+3%\n线上零售+2.6%，线下-1.8%，线上继续分流。\n\n3️⃣ 投研机构怎么看？\n某外资投行认为：现在说触底还太早，需要精选标的。\n关注两类公司：\n- 质地好、业绩先企稳的：多品牌战略+海外增长、品牌势能强、有利润缓冲的\n- 有拐点逻辑的：GMV企稳+股东回报、同店下滑好于预期+利润释放\n\n⚠️ 注意：原材料涨价风险高的公司建议回避。\n\n4️⃣ 估值也在收缩\n过去一个月，消费板块股价下跌5-6%，估值（远期PE）压缩了6-10%。\n整个板块的估值调整幅度比市场指数更大。\n\n📌 核心问题：需求何时企稳？\n二季度业绩季可能更多公司会下调指引。你怎么看\n\n[... middle omitted ...]\n\n be the drag, including home durables (down $15\\%$ on a high base); gold & jewelry (down $9\\%$ ) - reflecting recent volatility in gold prices (though narrowing from down $21\\%$ in Apr); and a\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R008",
    "title": "JPM：日本股市上涨的核心驱动力不是流动性，而是盈利能力的结构性跃迁",
    "digest": "[wechat_article.md]\n# JPM：日本股市上涨的核心驱动力不是流动性，而是盈利能力的结构性跃迁\n\n当全球投资者还在争论日本央行何时加息、日元是否会突破160关口时，日本股市已经在2026年上半年交出了一份令人无法忽视的成绩单。截至6月17日，东证指数（TOPIX）年内上涨18%，跑赢MSCI全球指数、标普500和欧洲STOXX 600。日经225更是录得39%的涨幅，显著超越TOPIX的表现。\n\n这份来自JPM的最新日本股权策略报告，将2026年底的日经225目标价上调至75,000点，TOPIX目标价上调至4,400点。但真正值得关注的，不是目标价本身，而是支撑这一判断的核心逻辑——市场正在经历从“估值修复”到“盈利驱动”的范式切换。\n\n过去几年，日本股市上涨的主要叙事是“安倍经济学”带来的公司治理改革、股票回购和外资回流。这些因素仍然存在，但边际效应正在递减。JPM认为，当前阶段真正驱动市场的变量，是AI半导体超级周期叠加日本企业盈利能力结构性改善所带来的盈利增长。TOPIX每股收益预计在2026财年同比增长11%，2027财年再增长12%，这一增速已经显著超出市场一致预期。\n\n更值得深思的是，报告指出日经225的AI相关股票市值占比已接近50%，TOPIX约为30%。这意味着，日本股市已经不再是“价值股洼地”，而是正在成为全球AI基础设施投资的重要映射。那些仍然以“低估、高股息、低增长”框架看待日本市场的投资者，可能正在错过这一轮结构性重估。\n\n本文将从五个维度拆解这份报告的核心洞察，并探讨那些尚未被充分定价的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI超级周期的需求侧已经明确，但供给侧的结构性变化才是日本市场的独特机会\n\n全球AI投资热潮并非新鲜事，但JPM特别强调了一个容易被忽视的视角：AI推理正在取代训练\n\n[... middle omitted ...]\n\n续深入讨论这些话题，欢迎加入，一起追踪日本市场的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日股下半年怎么走？一份研报的逻辑拆解\n\n日股还能涨吗？\n\n某外资投行把年底目标价调到日经225的7.5万点\n\n1/ 核心判断：盈利撑起行情，不是纯炒作\n上半年TOPIX涨了18%，跑赢美股和欧股。但估值（PE）反而从高位回落到16倍，过热担忧减轻。原因是半导体和半导体设备企业的利润超预期增长，把EPS预期从198日元拉到了234日元。盈利在撑盘，不是纯情绪驱动。\n\n2/ AI超级周期是主线，但逻辑在变\n研报认为AI推理（inference）会成为下一波增长主力，美国云厂商的数据中心投资拉动芯片、存储、电子元件的需求。上半年AI半导体占日经225市值约50%，贡献了大部分涨幅。下半年AI驱动行情会延续，但过热迹象在细分领域出现分化。\n\n3/ 风险与对冲：日元、利率、地缘\n日元若跌破160是负面信号，会推高通胀、影响外资回报。但若美联储转鹰导致日元适度升值，反而利好日股。日本长期利率上升和财政扩张是市场担忧点，但研报认为盈利增长和企业改革（提升ROE到10%以上）能对冲这些压力。\n\n4/ 下半年板块配置思路\n核心持仓：AI半导体+金融（银行）\n阶段性机会：若中东局势缓和，油价回落，建筑、运输、化工、国防板块有望反\n\n[... middle omitted ...]\n\ne below). The Liberal Democratic Party's (LDP's) landslide victory in the February Lower House election heightened policy expectations. Since April, as stock markets recovered, AI semiconducto\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 18 Jun 2026 07:26 PM JST\n\nDisseminated 18 Jun 2026 07:28 PM JST"
  },
  {
    "id": "R009",
    "title": "JPM：市场低估的不只是加息幅度，更是货币政策沟通机制的历史性转折",
    "digest": "[wechat_article.md]\n# JPM：市场低估的不只是加息幅度，更是货币政策沟通机制的历史性转折\n\n这份JPM在FOMC会议后数小时发布的研报，表面上在分析利率曲线和通胀预期的短期移动，但真正值得关注的判断藏在细节里：美联储正在经历自格林斯潘时代以来最彻底的沟通方式变革，而市场对此的定价远未完成。\n\n2026年6月的这次FOMC会议，新任主席Warsh的首秀，被JPM定性为“鹰派”。但鹰派本身不是新闻。真正的新信号是：政策声明被完全重写，不再提供任何前瞻指引，转而采用一句近乎宣言式的表述——“委员会将实现价格稳定”。这听起来像回归格林斯潘时代的含蓄与不可预测性。JPM的NLP模型将这份声明评为一年来最鹰派，新闻发布会评分则是2024年5月以来最高。\n\n但比鹰派更重要的，是这种沟通方式转变所隐含的结构性后果。如果前瞻指引被系统性削减，市场将不得不把更多权重放在每一个“事件日”上——每一次FOMC会议、每一次讲话、每一个数据发布，都可能引发比以往更大的波动。这不仅仅是短期交易员的烦恼，它意味着期限溢价的系统性重估，进而影响所有以无风险利率为锚的资产定价。\n\n以下是我们从这份研报中提炼出的五个层次判断，以及一个尚未被充分讨论的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 鹰派点阵图只是表象，真正重要的是“不对称的政策不确定性”正在被重新定价\n\n市场对10月会议加息25bp的完全定价，以及对明年春季累计超过45bp加息的预期，看起来是直接对点阵图的反应。2026年点阵图中位数显示12.5bp加息，18位委员中有6位预计两次或更多加息。但JPM的分析揭示了一个更深层的信号：从SOFR期货期权推断的隐含概率分布，不仅整体向鹰派方向移动，而且“双边尾部均增强”——意味着市场认为极端情景（无论是更鹰派还是更鸽派）的概率都在上升，分布变得更加对\n\n[... middle omitted ...]\n\n背后的逻辑，并持续跟踪后续FOMC委员讲话对市场定价的影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新主席首秀，鹰派信号拉满\n\n**鹰派首秀，市场买单**\n\n某外资投行最新研报：美联储新主席Warsh首次FOMC会议，鹰派程度超预期。\n\n1️⃣ **政策声明大改**\n- 声明完全重写，像格林斯潘时代风格\n- 不再提供前瞻指引，只说“委员会将实现价格稳定”\n- NLP模型评分：声明为一年来最鹰派\n\n2️⃣ **点阵图更鹰**\n- 2026年点阵图显示加息12.5bp\n- 18位委员中有6位预计两次或更多加息\n- 市场已定价10月会议前加息一次，明年春季前超45bp\n\n3️⃣ **通胀方面有分歧**\n- 油价从118跌至80以下，本可借此转向鸽派\n- 但Warsh强调2%通胀目标尚未实现（核心PCE仍在2.61%）\n- 实际利率上升（5年期+10bp），盈亏平衡通胀下降\n\n4️⃣ **缩表节奏不变**\n- 资产负债表工作组评估在2026下半年\n- 实际缩表可能要到2027年\n- 若将到期国债部分转投短债，SOMA久期将逐步收敛\n\n5️⃣ **操作建议**\n- 维持10s/30s flatteners（做平曲线）\n- 当前10s/30s曲线仍比模型公允值陡12bp\n\n#学习笔记\n\n[source_miner\n\n[... middle omitted ...]\n\nturn more dovish, the hawkish comments should continue to bias real yields higher and breakevens lower, in line with today's moves.  \n- We think yields are biased higher over the near term, es\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 17 Jun 2026 07:20 PM EDT\n\nDisseminated 17 Jun 2026 07:20 PM EDT"
  },
  {
    "id": "R010",
    "title": "Bernstein：瑞士手表出口反弹只是表象，真正的复苏信号尚未到来",
    "digest": "[wechat_article.md]\n# Bernstein：瑞士手表出口反弹只是表象，真正的复苏信号尚未到来\n\n全球奢侈品行业正经历一场“数据幻觉”。2026年5月，瑞士手表出口同比微增0.4%，看似走出了4月-16.6%的深跌。但Bernstein这份最新研报揭示了一个更复杂的现实：调整日历效应后出口增长10.4%，这个数字本身仍掩盖了结构性脆弱。真正值得关注的不是月度数据反弹，而是支撑复苏的底层逻辑——美国市场的基数效应、中国需求的缓慢改善、以及中东地缘风险对奢侈品消费的潜在冲击。\n\n这份报告的核心判断是：全球奢侈品需求的复苏轨迹仍充满不确定性，投资者不应被短期数据波动所迷惑。Bernstein明确指出了两股波动源：一是消费者在脆弱的宏观环境和日益紧张的地缘政治中做出的实际需求决策；二是短线投资者在板块的多空博弈，放大了涨跌幅。在这样的背景下，报告建议采取防御性姿态。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国市场的“基数游戏”是当前出口反弹的主要推手，而非需求强劲\n\n5月瑞士手表对美出口同比增长12.3%，这个数字本身并不代表美国消费者突然变得慷慨。关键在于比较基数的剧烈波动：去年同期的基数仅为-25%，而4月的基数高达+149%。这种基数效应造成的剧烈摆动，使得月度同比数据几乎失去了解读意义。\n\nBernstein的数据显示，从过去12个月的滚动数据看，对美出口同比下降19%，虽然较4月的-21%有所改善，但仍处于收缩区间。更关键的是，报告明确指出，今年剩余月份美国的比较基数将“持续友好”——除了7月因去年提前发货导致基数高达+45%外，其余月份均为两位数的负基数。这意味着未来几个月美国市场的出口数据很可能继续“看上去不错”，但投资者需要区分这是真正的需求复苏还是统计幻觉。\n\n这里蕴含着一个重要洞察：美国消费者对关税相关涨价的接受度\n\n[... middle omitted ...]\n\nH、Burberry等标的的判断，是否经得起更长时间的检验。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n瑞士腕表出口回暖，但别高兴太早\n\n**回暖背后的基数游戏**\n\n5月瑞士腕表出口同比微增0.4%，但调整工作日差异后实际增长10.4%。这波反弹主要靠美国，剔除美国后出口反而跌了1.2%。大中华区继续缓慢爬坡，中东却成了新隐忧。\n\n**1/ 美国是最大变量**\n对美国出口5月增长12.3%，去年同期基数低至-25%。基数效应预计会持续支撑到年底，除了7月（去年有抢运，基数+45%）。LTM看，美国出口仍跌19%，只是跌幅收窄。美国消费者对关税涨价似乎还能承受，但这是否可持续？\n\n**2/ 大中华区：慢但稳**\n对香港出口+3.4%，大陆-21.4%。但LTM看，大中华区出口仅跌0.9%，比上月的-1.4%继续改善。市场最关心的中国需求，没有惊喜也没有惊吓，就是慢悠悠地恢复。\n\n**3/ 中东成了新风险**\n对阿联酋和沙特出口分别跌13.5%和5.9%。中东是2025年奢侈品行业少有的增长亮点，如果冲突扩大，旅行减少、通胀上升、消费信心下滑，可能拖累整个行业的复苏。\n\n**4/ 价格段分化**\n200-500瑞郎和3000瑞郎以上手表表现最好，出口额分别增长23.6%和22.2%。200瑞郎以下和500-300\n\n[... middle omitted ...]\n\nac650e5abf65c9421b2b563127e7b4cbdd0aa83f57430565b22f7.jpg)\n\nYi-Peng Khoo, CFA\n\n+44 20 7676 6822\n\nyi-peng.khoo@bernsteinsg.com\n\n## Specialist Sales\n\n![](images/a8afdb1cd67b7283645d150eafdd8fd1c\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R011",
    "title": "GS：地震勘探行业正在进入一个被低估的、有纪律的多年度上行周期",
    "digest": "[wechat_article.md]\n# GS：地震勘探行业正在进入一个被低估的、有纪律的多年度上行周期\n\n市场对油服板块的关注，大多停留在油价波动和短期资本开支上。但一份来自GS的研报，通过与Viridien（原CGG）管理层的深度对话，揭示了一个更关键的结构性信号：全球地震勘探行业，正在经历一场从“资本纪律”到“资源重置”的范式转换。这并非2010-2015年那种由高油价驱动的狂欢，而是一个由储量寿命衰竭、能源安全焦虑和技术壁垒共同支撑的、更可持续的周期起点。\n\n这份报告最值得看的判断是：市场真正低估的不是需求是否回升，而是供给侧的再定价能力以及行业竞争格局的质变。地震勘探行业，尤其是海洋拖缆领域，已经从“产能过剩的苦海”变成了“寡头定价的棋局”。而AI技术的渗透，非但没有削弱核心企业的护城河，反而让高质量成像数据成为了更稀缺的资产。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. EAGE 2026的“爆满”不是噪音，而是储量焦虑的集体投票\n\n2026年6月在阿伯丁举行的第86届EAGE年会，创下了超过6000人的历史参会纪录。这不仅仅是行业聚会的规模扩大。GS报告明确指出，C-level管理层的参与度较2025年显著提升。背后驱动力是“储量替换”和“储量寿命”这两个最根本的行业指标，重新回到了董事会的核心议程。\n\n这意味着什么？过去十年，行业被“资本纪律”和“股东回报”的叙事主导，上游企业普遍削减勘探开支，专注于短周期、低风险的棕地项目。但代价是储量寿命的持续下降。GS数据显示，全球主要油企的储量寿命从2012年的约55年，骤降至2026年预计的约20年。这是一个系统性的“寅吃卯粮”。EAGE的火爆，正是这种深层焦虑的集体宣泄。它告诉我们，行业共识已经形成：不勘探，就没有未来。\n\n![研报原图 2](assets/source_image_02\n\n[... middle omitted ...]\n\n共同探讨这个被低估的“新周期”中，真正的价值锚点究竟在哪里。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n前沿勘探回归，油服周期启动\n\n**勘探归来**\n\nEAGE 2026传达出近些年最强信号：前沿勘探重回议程🔥\n\n某外资投行与Viridien（前CGG）CFO交流后，核心观点如下：\n\n**1/ 勘探活动明显回暖**\n- EAGE参会人数超6000人，创历史新高\n- C-suite参与度较2025年大幅提升\n- 储备替代和储备寿命成为核心议题\n- 2026年预算在战前锁定，收入拐点预计在2027年\n\n**2/ 前沿勘探回归**\n- 历史上80%活动集中在近场勘探\n- 现在客户兴趣向乌拉圭、巴西赤道边缘、安哥拉、埃及、利比亚扩散\n- 大型油企多年投资不足，需要时间重建前沿勘探能力\n- 再处理需求是第二主线，直接利好地球物理公司\n\n**3/ 这轮周期不一样**\n- 不会回到2010-2015年60艘活跃拖缆船的盛况\n- 客户更注重股东回报，支出更理性\n- 行业预计是持续多年的温和上升周期\n\n**4/ AI不是威胁**\n- AI无法解决基于物理的波动方程成像问题\n- HPC算力是结构性护城河\n- AI主要用于降噪、工作流加速和快速交付\n- 客户在高质量成像基础上叠加自研AI工具，反而提升了数据价值\n\n**行业背景：新\n\n[... middle omitted ...]\n\nunderpinned by reserve replacement and reserve life firmly back on the agenda and reinforced by post-war energy security concerns. This has not yet flowed into seismic revenues — 2026 budgets \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "JPM：市场低估了供给侧的再定价，而非需求端的边际变化",
    "digest": "[wechat_article.md]\n# JPM：市场低估了供给侧的再定价，而非需求端的边际变化\n\n中国5月经济数据再度走弱，这本身并不令人意外。真正值得关注的信号，是JPM在最新一期亚洲基础材料研报中提出的一个隐含判断：当前大宗商品市场的定价逻辑，正在从“需求预期驱动”切换为“供给约束驱动”。对于铜、铝、煤炭这三个核心品种，市场对需求侧的悲观已经充分定价，但供给侧的结构性收紧——无论是地缘政治冲击、产能监管趋严，还是全球供应链的物理性阻塞——尚未被完全计入资产价格。\n\n这份研报的核心价值不在于罗列数据，而在于它提供了一套清晰的决策框架：在需求侧无法提供方向感的时候，投资者应该如何重新锚定大宗商品的定价基准。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹海峡的重新开放，可能成为金属板块最被低估的战术催化剂\n\n研报最引人注目的判断，是JPM认为市场对美伊局势缓和的潜在影响定价不足。自冲突爆发以来，铜和黄金相关股票的跌幅已经相当显著——紫金矿业H股下跌26%，紫金黄金下跌49%，而同期恒生指数仅下跌8%。这种跌幅反映了市场对地缘风险溢价的全面计入。\n\n但JPM提出的逻辑是：如果霍尔木兹海峡重新开放，被压抑的风险偏好将首先释放到那些受冲突冲击最严重的资产上，铜和黄金的股价反弹潜力最大。这个判断的关键支撑在于，铜和黄金的基本面并未因冲突而实质性恶化，下跌更多来自情绪层面的风险折价，而非供需结构的永久性破坏。\n\n这实际上是一个“均值回归”的战术逻辑：市场对尾部风险的定价往往过度，而一旦尾部风险消散，资产的修复速度可能快于基本面改善的速度。对于机构投资者而言，这意味着当前可能是布局铜和黄金相关标的的时间窗口——但前提是承认自己无法精准判断地缘政治事件的时点，只能以赔率而非胜率为决策依据。\n\n![研报原图 2](assets/source_image_0\n\n[... middle omitted ...]\n\n中只有结论，没有展开，而真正的投资决策需要更细致的假设拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月数据偏软，金属板块关注两大催化剂\n\n📊 五月数据偏软，但拐点信号已现\n\n某外资投行最新研报指出，5月国内活动数据继续走弱，新开工面积同比下降25%，房地产投资同比下滑25%，固定资产投资更是大幅收缩17%。整体需求依然谨慎。\n\n但市场焦点正在转向两个关键变量：\n\n1️⃣ 霍尔木兹海峡复航预期\n美伊关系缓和可能推动海峡重新开放，这对前期受避险情绪压制的金属板块形成战术性反弹机会。铜和黄金的股价修复弹性最大。\n\n2️⃣ 利率预期变化\n降息预期成为另一重要催化剂，尤其利好黄金资产。\n\n🔍 各品种怎么看？\n\n🟤 铝：短期有压力，中期看好\n复航可能释放中东积压库存，短期施压LME铝价（目前约3360美元/吨）。但中期供需偏紧，预计2026年全球原铝缺口约170万吨。中国宏桥和中铝仍是主要受益标的。\n\n🟤 锂：价格企稳但信号混乱\n锂价在16.5万元/吨附近获得支撑，但供需信号仍不清晰，预计短期内维持区间震荡。\n\n🟤 煤：供应扰动推升价格\n山西矿难后，焦煤价格持续走高，预计3季度仍将维持高位。研报将2026年动力煤价格预测上调至805元/吨。神华和兖矿盈利预测相应上调。\n\n🟤 黄金：多重利好共振\n黄金同时受益于避险需求\n\n[... middle omitted ...]\n\nectations of US-Iran de-escalation and a potential reopening of the Strait of Hormuz could support a tactical rebound in metals names that have been pressured by risk-off sentiment since the o\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 17 Jun 2026 04:56 PM HKT\n\nDisseminated 17 Jun 2026 04:57 PM HKT"
  },
  {
    "id": "R013",
    "title": "JPM：半导体设备市场的下一个结构性拐点不在需求，而在供给侧的产能释放节奏",
    "digest": "[wechat_article.md]\n# JPM：半导体设备市场的下一个结构性拐点不在需求，而在供给侧的产能释放节奏\n\n这份JPM刚刚发布的研报，核心判断只有一个：全球晶圆厂设备（WFE）市场正在经历一次被低估的上行重估。JPM将2026年WFE市场增速预测从21%大幅上调至28%，2027年从18%上调至29%，并首次给出2028年16%的增长指引。这不是一次温和的修正，而是一次系统性的预期上调。\n\n但真正值得关注的，不是增速数字本身，而是驱动这一轮上调的结构性力量正在发生质变。AI需求从训练向推理的迁移，正在重塑整个半导体资本开支的分配逻辑——内存芯片的投资权重正在从过去的个位数至15%区间，跃升至2026年的约50%。这意味着，过去几年市场习惯的“AI=GPU+ASIC”叙事，正在被“AI=加速器+高带宽内存+先进封装”的全栈逻辑取代。\n\n更关键的是，这份报告揭示了一个被多数投资者忽视的变量：洁净室产能的瓶颈正在缓解。此前市场对2026年设备交付的担忧，很大程度上源于芯片制造商洁净室建设进度滞后。但JPM的调研显示，通过工厂空间的创造性利用和洁净室扩建的正式启动，这一瓶颈正在被打破。从2027年开始，随着洁净室大规模投产，需求将迎来真正的释放窗口。\n\n以下是我们从这份研报中提炼出的五个核心洞察，每一个都指向一个正在被重新定价的产业环节。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 云厂商资本开支的“超级周期”正在从预期走向现实，且规模远超历史任何时期\n\nJPM对全球前四大美国云服务提供商（谷歌、亚马逊、微软、Meta）的资本开支预测，做了幅度惊人的上调：2026年增速从63%上调至80%，2027年从40%上调至50%。在绝对值上，这意味着2026年同比增量将超过2500亿美元，2027年超过2850亿美元——这是有史以来最大的年度增幅。\n\n[... middle omitted ...]\n\n欢迎加入我们的星球微信群，与更多产业决策者和投资者一起讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体设备市场，已看到三年高景气\n\n2026-28 WFE市场：增速上调\n\n某外资投行最新研报大幅上调了晶圆厂设备（WFE）市场增速预测👇\n\n**2026年：从21%→28%**\n**2027年：从18%→29%**\n**2028年：新给出16%增速预测**\n\n核心驱动力是AI需求从训练转向推理，结构正在拓宽，不再只是加速器。\n\n1️⃣ **云厂商砸钱不手软**\n- 美国前四大云服务商2026年资本开支预计同比+80%\n- 2027年再+50%\n- 2026年单年增量超2500亿美元，历史最大\n- 北美规划电力容量已超175GW，年底或达205GW+\n\n2️⃣ **存储器投资权重飙升**\n- 过去存储器只占云厂商投资的个位数-15%\n- 2026年预计升至约50%\n- DRAM和HBM是主要驱动力\n- 三大年存储器行业总资本开支预估从3000亿上调至4500亿美元\n\n3️⃣ **先进封装产能持续扩张**\n- 台积电CoWoS产能：2026年底11.5万片/月→2027年17.5万→2028年22万\n- 3D SoIC产能：2027年底4万片/月→2028年6.5万\n- 客户需求从NVIDIA扩展到AMD、谷歌、博\n\n[... middle omitted ...]\n\nextent for CY2026, but the outlook is improving owing to such factors as creative use of factory space. From 2027 onward, we expect demand to increase as cleanroom expansions get underway in e\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 17 Jun 2026 05:08 PM JST\n\nDisseminated 17 Jun 2026 05:10 PM JST"
  },
  {
    "id": "R014",
    "title": "JPM：AI定制芯片正在从“备选方案”变成“主导逻辑”",
    "digest": "[wechat_article.md]\n# JPM：AI定制芯片正在从“备选方案”变成“主导逻辑”\n\n过去两年，市场对AI基础设施的讨论几乎完全围绕英伟达GPU展开。算力即权力，而英伟达是唯一的铸币厂。但这份JPM最新发布的半导体深度报告揭示了一个正在发生的结构性转折：到2027年，AI加速器的出货量中，定制芯片（ASIC/XPU）的占比将从2025年的32%跃升至53%，首次超过GPU。这不是边缘替代，而是产业逻辑的根本切换。\n\n报告的核心判断是：当AI从训练走向推理，从少数巨头试验走向大规模部署，定制芯片的经济性和系统级优势正在重塑整个计算架构的供应链。这不是英伟达的“被颠覆”，而是AI计算市场本身在快速分化和成熟。理解这一轮ASIC浪潮的驱动力、竞争格局和未解问题，比争论“英伟达是否见顶”更有意义。\n\n以下是这份报告的五个关键洞察，以及一个报告尚未完全回答的关键追问。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 定制芯片的崛起不是技术竞赛，而是规模经济与软件护城河的综合博弈\n\nJPM将芯片市场清晰划分为三类：通用芯片（GP）、标准应用芯片（ASSP）和定制芯片（ASIC）。AI GPU属于ASSP，而Google TPU、Amazon Trainium、Microsoft Maia则属于ASIC。后者的核心优势不在于单点性能超越GPU，而在于系统级的总拥有成本（TCO）优化。\n\n报告提供了一个关键对比：Google/Broadcom的TPUv7 Ironwood在FP8计算性能上达到4614 TFLOPS，与英伟达B200 Blackwell的4500 TFLOPS相当，但ASIC的单价仅约13000美元，远低于B200的35000美元。这意味着每美元获得的算力（TFLOPS per $）上，ASIC是GPU的2.7倍。在功耗效率（TFLOPS\n\n[... middle omitted ...]\n\n欢迎来星球微信群里继续交流，一起追踪这些关键变量的实际进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI定制芯片正在吃掉GPU的市场\n\n定制芯片崛起\n\n当大厂开始自己造芯，NVIDIA的蛋糕还稳吗？\n\n---\n\n最近某外资投行出了一份ASIC（定制芯片）深度研报，几个关键数据值得关注👇\n\n**1/ 市场格局正在逆转**\n2023年AI加速器出货量中，GPU占55%，ASIC占45%。但到2027年，ASIC占比预计反超至53%。这不是小变化，是结构性拐点。\n\n**2/ 为什么大厂都在自研芯片？**\n苹果是教科书级案例：年出货2.5亿台设备，自研芯片能深度调优软硬件，性能功耗比更强，长期ROI极高。\n谷歌TPU、亚马逊Trainium、Meta MTIA、微软Maia…逻辑一样：量不大但单价极高，AI推理的token变现能覆盖研发成本。\n\n**3/ 性能对比：ASIC并不输GPU**\n以谷歌TPUv7 vs NVIDIA B200为例：\n- 算力：4614 vs 4500 TFLOPS（几乎持平）\n- 功耗：都是1000W\n- 每美元算力：0.35 vs 0.13（ASIC性价比高2.7倍！）\n- 每瓦算力：4.61 vs 4.50（略优）\n\n**4/ 供应链赢家已浮现**\nBroadcom拿下80-85%高\n\n[... middle omitted ...]\n\n or platform:\n\n• Example: Apple iPhone A19 processor chip (Apple does complete design)  \n• Example: Nokia Reef Shark BTS processor chip (Nokia, Marvell, Broadcom)  \n• Example: Google TPU AI pr\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R015",
    "title": "摩根斯坦利：市场低估的不是下行风险，而是政策“微调”而非“转向”的定力",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是下行风险，而是政策“微调”而非“转向”的定力\n\n四、五月的数据让一个事实变得无法回避：中国经济的“双速”格局正在加深。出口和生产端依然保持韧性，但国内需求——消费、投资、甚至石油消费——出现了明显的边际走弱。\n\n市场对此的第一反应通常是担忧。担忧经济失速，担忧政策被迫急转弯。但摩根斯坦利在本期《China Musings》中提出了一个更值得深思的判断：当前的下行并不指向需要政策“转向”的急剧恶化，而是触发“微调”的紧迫性上升。报告的标题本身就很能说明问题——“Beijing Will Fine-tune, Not Pivot”。\n\n这个判断的分量，不在于它确认了经济放缓，而在于它划出了一条重要的政策边界：北京不会因为短期数据波动就放弃既定的结构性转型路径。对于投资者而言，真正需要理解的不是“经济好不好”，而是“在4.5%-5%的增长目标与K-shaped经济现实之间，政策制定者会选择什么工具、在什么节奏上出手”。\n\n以下是这份报告的核心逻辑拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内需求的走弱是真实的，但同比读数放大了放缓的速度\n\n四五月的数据确认了一个K-shaped格局的深化：生产与出口坚挺，消费与投资软化。但摩根斯坦利提醒，不能简单地用同比增速的回落来判断放缓的严重程度。\n\n固定资产投资（FAI）的减速，部分源于政策驱动。自2月底以来，中央强调“正确政绩观”，促使地方政府将重心从新项目转向化解隐性债务。这意味着FAI数据的走弱，有主动调控的成分，而非纯粹的终端需求崩溃。零售数据同样需要拆解：5月同比转负，很大程度上受到去年“以旧换新”补贴政策高基数的影响。以两年复合年化增长率（2Y CAGR）来看，5月甚至略好于4月。\n\n但报告同时指出，放缓不仅仅是基数效应。即便\n\n[... middle omitted ...]\n\n原文与核心图表，并组织专题讨论，一起拆解这份报告的未尽之处。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n北京要微调，不会转向\n\n📌 微调而非转向\n\n5月数据显示内需走弱，但出口和工业生产依然坚挺。某外资投行认为，这是“K型复苏”的深化，不会引发政策大转向，但微调窗口在收窄。\n\n1️⃣ 内需降温，但没到崩的程度\n- 固投放缓部分原因是地方政府忙于化解隐债，新项目审批收紧\n- 零售同比转负，主要受去年以旧换新补贴高基数影响；看两年复合增速，5月比4月略好\n- 但消费确实在变弱：就业市场疲软、地产调整、油价挤压，出口强劲也没怎么传导到工资\n\n2️⃣ 政策节奏：加速花钱，但不改方向\n- 二季度GDP增速约4.4%，全年目标4.5-5%的下沿有压力\n- 近60%的政府债券额度还没用，准财政工具（政策性银行债券）发行也偏慢\n- 预计7月政治局会议会强调加快预算执行，但不会转向刺激私人消费\n\n3️⃣ 重点支持：六大网络基建\n- 水网、新型电网、算力网络、新一代通信、城市地下管网、物流基建\n- 其中AI算力、数据中心、智能电网最可能优先受益\n\n4️⃣ 外部影响：出口强≠贸易顺\n- 内需弱→更多产能转向出口→在欧盟市场份额快速上升（钢铁、电动车、电池、光伏、化工）\n- 欧盟可能采取针对性措施：关税、反补贴调查、采购限制等\n- 但\n\n[... middle omitted ...]\n\nbrupt downturn that warrants policy pivot; however, the need for policy fine-tuning is rising. Abroad, the widening K-shaped pattern may intensify trade frictions.\n\nDomestic demand is cooling,\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R016",
    "title": "摩根斯坦利：中国电动车市场的份额洗牌远未结束，真正的分化才刚刚开始",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国电动车市场的份额洗牌远未结束，真正的分化才刚刚开始\n\n5月的中国电动车市场，表面上是几家欢喜几家愁的月度排名更迭，但摩根斯坦利这份最新研报揭示的信号远比排名变化本身更值得深思：市场正在从一个“谁都能分一杯羹”的增量竞争阶段，转向一个“产品节奏、品牌势能与渠道效率必须同时在线”的存量博弈阶段。月度份额的波动，不再是随机扰动，而是企业战略执行力的压力测试结果。\n\n这份报告的核心价值，不在于告诉你哪家品牌5月卖得好，而在于它提供了一套观察竞争格局的微观透镜：当比亚迪海洋/王朝系列份额出现年内首次环比下滑，当理想汽车在L系列改款前的阵痛期份额承压，当零跑汽车创下历史新高，当特斯拉在所有城市级市场实现份额扩张——这些碎片化信号叠加在一起，指向一个更本质的判断：中国电动车市场的份额洗牌，已经从“大厂吃肉、小厂喝汤”的粗放阶段，进入“产品周期管理能力决定季度排名”的精耕阶段。谁能在新旧产品切换的窗口期保持份额稳定甚至逆势增长，谁才真正具备穿越周期的能力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪的份额松动不是衰退信号，而是市场对“规模溢价”重新定价的开始\n\n比亚迪海洋/王朝系列5月市场份额环比下降1.0个百分点至17.5%，与其年初至今的平均水平持平。这个数字本身并不令人恐慌——17.5%的市占率仍然是行业绝对龙头。但值得关注的是，这是否意味着比亚迪依靠冠军版、荣耀版等降价策略维持份额的边际效应正在递减？\n\n摩根斯坦利在报告中并未直接给出这个判断，但数据本身提供了线索：1.0个百分点的环比降幅，在所有主流品牌中仅次于小米的0.9个百分点下滑，但小米的下滑是SU7改款后销量自然回落，而比亚迪的下滑发生在没有明显产品空窗期的背景下。这暗示，当竞争对手的产品迭代速度加快、新车型密集上市时，即便是比亚迪\n\n[... middle omitted ...]\n\n你希望获得比这篇导读更深一层的分析框架，欢迎加入我们的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月新能源份额洗牌，谁在涨？\n\n五月新能源市场格局变化\n\n几家欢喜几家愁，5月新能源品牌份额排名悄悄变了。\n\n📊 五月份额变化速览\n\n**📈 份额上涨组**\n- 特斯拉中国：+2.0ppt → 5.2%\n- 零跑：+0.8ppt → 6.8%（再创历史新高）\n- 问界：+1.0ppt → 3.8%\n\n**📉 份额下滑组**\n- 小米：-0.9ppt → 3.6%（SU7改款热潮后降温）\n- 比亚迪海洋/王朝：-1.0ppt → 17.5%\n- 理想：-0.4ppt → 3.6%（L9订单增长被其他车型拖累）\n- 蔚来：-0.2ppt → 3.9%（部分销量延后确认）\n- 小鹏：-0.3ppt → 2.8%\n\n**🔮 后续看点**\n- 小鹏GX开始交付，预计份额回升\n- 蔚来L60/L80/ES9交付后有望改善\n- 比亚迪唐（6/17）和理想L8（6/23）即将发布\n\n豪华品牌这边，奔驰微降0.1ppt，宝马降0.4ppt。\n\n#学习笔记\n\n[source_mineru.md]\n# China Autos & Shared Mobility | Asia Pacific\n\n# How Market Share \n\n[... middle omitted ...]\n\nLi Auto's market share declined 0.4ppt MoM to 3.6% (vs. YTD 4.5%), likely as L9's order growth was offset by more tepid sales across other L-series models ahead of their facelifts.\n\nNIO's ma\n\n[... middle omitted ...]\n\nd>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.84</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R017",
    "title": "摩根斯坦利：功率半导体的涨价周期并非需求驱动，而是供给侧的理性收敛",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：功率半导体的涨价周期并非需求驱动，而是供给侧的理性收敛\n\n全球功率分立器件市场自2025年第四季度重回增长轨道。2026年4月，全球功率分立器件营收同比增长已达16%。这一数字本身并不令人意外——半导体行业周期性复苏的叙事在过去半年已被反复讨论。真正值得关注的，是驱动本轮上行的力量结构。\n\n摩根斯坦利最新发布的亚太半导体研报提出了一个关键判断：当前功率半导体的涨价周期是供给驱动型，而非需求驱动型。这意味着，市场若以传统周期框架来线性外推，可能会高估需求的持续性，同时低估供给侧结构性变化带来的定价权重塑。\n\n这份报告的价值不在于确认“周期回来了”，而在于拆解“这个周期和上一个有什么不同”。对于产业决策者和投资者而言，理解这种差异，比判断涨价的幅度更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 过去两年的资本开支收缩，正在为当前定价权奠定基础\n\n全球主要功率分立器件公司的资本开支已连续两年下降。2026年虽出现约11%的温和回升，但整体供给端扩张的力度远弱于以往任何一个复苏周期。摩根斯坦利的数据显示，中国功率分立器件市场在未来三年内新增产能有限——士兰微、华大半导体等企业正将资源转向AI电源管理芯片等更高附加值领域，而非继续扩大IGBT和MOSFET的传统产能。\n\n这一变化的含义是深刻的。传统半导体周期中，涨价往往伴随着产能的快速释放，继而引发价格回落。但本轮周期中，供给侧的克制使得供需关系发生了结构性改变。即使需求端仅温和复苏，定价权仍可能向供应商倾斜。\n\n报告特别指出，只要需求不发生急剧恶化，这一轮涨价趋势有望延续至2026年下半年。这个判断的核心支撑，正是供给侧的理性收敛，而非需求端的爆发。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 需求\n\n[... middle omitted ...]\n\n替代节奏、以及不同渠道结构下的定价弹性——进行更深入的探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n功率半导体的涨价逻辑\n\n供给驱动的涨价周期\n\n功率半导体价格正在回暖，这次是供给端的故事\n\n📌 全球功率器件销售从2025年Q4开始恢复增长，4月同比增速达到16%。多家中国功率器件公司在2026年2月发布涨价通知，下游渠道库存低、担心下半年价格继续涨，普遍接受了提价。\n\n📌 需求端分化明显：工业和汽车合计占功率器件需求的72%。工业自动化需求强劲，头部企业1Q26收入同比增长21%；中国电动车批发增速从4月的零增长回升到5月的7%；但光伏需求疲软，新增装机同比下降51%。\n\n📌 供给端是核心看点：全球功率器件龙头资本开支连续两年下降，2026年仅小幅增长11%。国内公司如士兰微、华虹半导体转向AI电源管理芯片，未来三年功率器件（IGBT、MOSFET等）产能扩张有限。高利用率+有限新增产能，如果需求不急剧恶化，涨价趋势可能持续到2026年下半年。\n\n📌 投行研报更新了目标价：扬杰科技目标价从91元上调至136元（看好汽车业务占比提升和运营效率）；士兰微从20元上调至26.9元；华润微从43元上调至51.6元。但评级维持不变，认为这是供给驱动的周期，对士兰微和华润微维持低配，担心预期已经打得太满。\n\n功率半导\n\n[... middle omitted ...]\n\nwer discrete companies issued price hike notices in Feb 2026, citing higher raw material prices and foundry costs. Except for IGBT for automotive customers, distributors and other end-market c\n\n[... middle omitted ...]\n\ny Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R018",
    "title": "JPM：外卖补贴新规的真正价值不在上限，而在让烧钱竞争变得“无法隐身”",
    "digest": "[wechat_article.md]\n# JPM：外卖补贴新规的真正价值不在上限，而在让烧钱竞争变得“无法隐身”\n\n市场正在用一个错误的框架解读中国外卖行业最重要的监管信号。当国家市场监管总局于6月17日发布《外卖平台补贴行为规范（征求意见稿）》时，主流反应是“没有硬性补贴上限，所以没有实质约束力”。这份JPM的深度研报提出了一个截然不同的判断：市场低估的不是规则的字面力度，而是信息披露作为一种执法机制的真实效力。\n\n这份研报的核心主张清晰而克制：新规降低了美团的下行尾部风险，但尚未将监管缓和转化为正面的盈利催化剂。JPM维持美团中性评级，目标价85港元。这个判断建立在一个承重性假设之上——资金来源条款具有真实的行为约束力，能够限制以资本优势为弹药的外卖补贴攻击。如果这个前提成立，新规则降低了JPM此前给出的熊市情景（美团公允价值约51港元）的概率。\n\n这不是一份宣告转折点的乐观报告，它更像一份情景概率的重新分配说明书。在监管信号密集、市场情绪反复的当下，这种克制恰恰是投资者最需要的东西。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 信息披露本身就是执法工具，市场误读了“没有上限”的含义\n\n市场对新规的第一反应可以概括为：没有补贴上限，等于没有作用。JPM认为，这种解读忽略了规则设计的核心机制——新规不是通过设定价格上限来监管补贴，而是通过让激进的补贴行为变得更慢、更透明、更容易被挑战来发挥作用。\n\n在外卖这个行业，最具有破坏力的竞争形式不是普通的促销，而是快速、以资本为后盾的补贴升级，其目的是在在位企业能够反应之前就改变消费者和商家的行为。七天的事前披露和资金来源报告，直接针对的就是这一机制。\n\n研报提出了三个层面的逻辑链条。第一，信息披露降低了速度优势。外卖补贴战是反应式的——挑战者发起促销，在位者回应，市场测试双方的极限。七天公告窗\n\n[... middle omitted ...]\n\n东的竞争格局演变有自己的判断，也期待在讨论中碰撞出新的视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n外卖补贴战要降温了？规则解读\n\n补贴降温，市场回归运营\n\n某外资投行最新研报指出，市监局发布的《外卖平台补贴行为规则》征求意见稿，看似没有硬性补贴上限，但实际影响可能被低估。\n\n1/ 为什么说“披露就是执法”？\n- 7天预披露：补贴活动必须提前公布，削弱了“突袭式”补贴的效果\n- 资金来源透明：要求用自身经营利润补贴，不能靠资本优势烧钱\n- 竞争影响自评：留下书面证据，方便监管和同行监督\n\n2/ 谁最受益？\n- 美团：运营效率才是护城河，补贴战降温后竞争回到它擅长的领域\n- 阿里：短期减少亏损，但即时零售战略弹性降低\n- 京东：最依赖资本补贴入场，规则收紧后持久性存疑\n\n3/ 关键变量：怎么定义“经营利润”？\n- 如果是业务线级别利润→显著利好美团\n- 如果是集团级别利润→阿里仍有操作空间\n- 最终文本模糊→看执行力度\n\n4/ 后续观察节点\n- 7月17日征求意见截止后的正式文本\n- 首批7天预披露的补贴活动\n- 三季度实际补贴强度是否下降\n\n研报维持美团中性评级，认为规则降低了极端补贴战的概率，但还没到上调盈利预测的时候。\n\n#学习笔记\n\n[source_mineru.md]\n## China Food D\n\n[... middle omitted ...]\n\nf the draft lowers the probability of our bear case (Table 4), in which prolonged capital-funded competition weakens the delivery profit pool and Meituan's fair value falls to around HK\\$51. I\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R019",
    "title": "摩根斯坦利：2026陆家嘴论坛的真正信号不是开放，而是金融业增长逻辑的重新定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：2026陆家嘴论坛的真正信号不是开放，而是金融业增长逻辑的重新定价\n\n市场对2026年陆家嘴论坛的关注，大多集中在“进一步开放”这个关键词上。新的QDII额度、简化ODI流程、跨境贸易外汇结算试点——这些政策细节确实被密集释放。但摩根斯坦利这份研报试图传达的判断，远比“开放”二字复杂。\n\n这份报告的核心主张是：陆家嘴论坛传递的，不是简单的政策宽松信号，而是一套关于中国金融业增长质量的重新定义框架。开放是手段，但风险控制和高质量发展才是目的。两者并非对立，而是构成了一个更精细的政策组合——这意味着金融机构的估值逻辑，需要从“规模增长”切换到“质量定价”。\n\n为什么这个判断重要？因为过去几个月，市场对跨境资本流动收紧的担忧在累积。香港市场和中概股的波动，部分源于这种不确定感。摩根斯坦利在5月底的两份报告中已经试图缓解这种担忧，而本次论坛的政策信号，则是对市场预期的直接回应。但报告同时明确指出，开放不等于放松监管——银行业的理性信贷增长、保险业的费用管控、资本市场的有序IPO机制，这些才是论坛真正的结构性信号。\n\n以下五个层次，拆解这份报告的真正含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 开放政策的信号意义大于实质：它缓解的不是资本流出，而是政策不确定性溢价\n\n摩根斯坦利报告明确将论坛的开放信号与5月以来的市场担忧联系起来。PBOC和SAFE在论坛上宣布的几项具体政策——新的QDII额度、简化ODI、外债外汇管理优化、上海跨境贸易外汇结算试点——在报告中被描述为“支持人民币全球化和拓宽而非限制跨境资本流动”。\n\n但仔细看，这些政策本身并非颠覆性的。QDII额度增加是渐进式操作，上海试点是局部推进。真正重要的是信号本身：政策制定者有意向市场表明，金融开放的长期方向没有改变。这一点，对于过去几个月\n\n[... middle omitted ...]\n\n变化，以及哪些金融机构更有可能在“质量定价”的新逻辑下受益。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n陆家嘴论坛释放了什么信号\n\n金融开放再提速\n\n风险防控与高质量发展并重\n\n---\n\n**某外资投行最新研报解读陆家嘴论坛信号，核心就三个关键词：开放、质量、监管。** 信息量很大，我帮你拆开看。\n\n**1. 金融开放，步子没停**\n\n- 高层再次强调金融业持续开放，央行和外管局跟进表态。\n- 政策细节很具体：新QDII额度、简化ODI流程、外债外汇管理优化。\n- 上海试点贸易外汇结算，支持人民币国际化，跨境资本流动方向是拓宽而非收紧。\n\n**2. 高质量发展，银行要“慢下来”**\n\n- 央行明确：贷款增速放缓但质量提升，将成为新常态。\n- 银行不再追求规模扩张，而是理性增长、风险可控。\n- 同时设立非银金融机构流动性支持工具，防止系统性风险。\n\n**3. 监管更严，但资本市场更灵活**\n\n- 保险：严管无序竞争，费用管控持续，利好财险公司成本率。\n- 资本市场：修改上市规则，加速推出“储架发行”机制，IPO更灵活。\n- 还会推出活跃ETF和商业地产REITs试点。\n\n**我的感受**：这次论坛信号很一致——金融不是不发展了，而是换一种方式发展。开放继续，但节奏更稳；增长继续，但质量优先。对金融机构来说，长期看\n\n[... middle omitted ...]\n\nimplified ODI, external debt FX management...  \n...and Shanghai-based pilots for trade FX settlement, which will support RMB globalization and broadening rather than containing cross-border ca\n\n[... middle omitted ...]\n\npment Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.24</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R020",
    "title": "NOM：人民币中间价模型正在发出一个被市场忽视的定价信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在发出一个被市场忽视的定价信号\n\n人民币汇率中间价的每日设定，长期以来被市场视为一个政策信号灯。大多数投资者关注的是中间价本身的方向——是升值还是贬值，以及它与前一交易日收盘价的偏离幅度。但NOM最新发布的USD/CNY定盘价模型报告揭示了一个更精细的维度：模型内部各货币的贡献权重和逆周期因子的调整幅度，正在传递一个关于央行汇率管理策略变化的信号。这个信号比中间价的方向更重要，因为它指向的是政策框架的微调，而非一次性干预。\n\n这份报告的核心判断是：市场对人民币汇率定价的理解，仍停留在“央行是否容忍贬值”的二元框架中，而忽略了中间价形成机制内部结构的持续变化。真正重要的不是中间价定在哪个数字，而是这个数字如何被计算出来。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测与官方定盘价的偏离，正在暴露政策意图的微妙变化\n\nNOM模型给出的最新预测值是6.7745，较前一交易日下降385个基点。如果考虑逆周期因子调整，预测值为6.7965，较前一交易日下降165个基点。这两个数字本身并不惊人——人民币中间价在6.7-6.8区间波动已是常态。真正值得关注的是模型误差的趋势。\n\n报告中的模型误差图显示，自2025年中的低点以来，模型误差（即模型预测与官方定盘价之间的差值）已经从接近零的水平扩大至约600个基点的正值区间。这意味着，官方定盘价系统性地高于模型预测值——换言之，央行在中间价设定中持续加入了比模型预期更强的“抗贬值”力量。\n\n这个趋势不是偶然的。它表明，央行并非简单地维持中间价稳定，而是在主动压缩贬值空间。当模型预测中间价应该更低（即人民币更强）时，官方定盘价却更高（即人民币更弱），这恰恰说明央行的操作方向与市场预期相反——它在抑制升值，而非阻止贬值。这一点对很多持有“央行在放任\n\n[... middle omitted ...]\n\n节，并讨论如何将模型误差信号转化为具体的交易和风险管理策略。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型指向6.77\n\n**6.77 附近**\n\n**模型预测出现明显下移**\n\n一份外资投行的最新研报显示，人民币中间价模型预测出现明显变动。\n\n核心数据很直接：模型对USD/CNY中间价的预测值是 **6.7745**，比上一轮的6.8130低了385个点。如果加上逆周期因子，预测值在 **6.7965** 附近，也比上次的定盘价低了165个点。\n\n几个关键细节值得留意：\n\n1.  **主要贡献来自欧元**。在影响模型预测的货币篮子中，欧元贡献了最大的正向变动（35.5 pips），日元和韩元紧随其后。这说明隔夜美元走弱是主要驱动力。\n\n2.  **逆周期因子在发挥作用**。模型显示，加入逆周期因子后，预测的下行幅度从385个点收窄到165个点。这通常被理解为一种平滑信号，防止汇率出现单边快速波动。\n\n3.  **近期模型误差不大**。从研报附带的误差图看，过去几个月模型预测与实际定盘价的偏差基本在可控范围内，没有出现极端偏离。\n\n简单来说，模型给出的信号是：在外部美元走弱的环境下，中间价存在向下调整的空间，但政策工具也在同步介入，以维持节奏的平稳。\n\n下半年国内还有几个重要会议节点，比如7月底的\n\n[... middle omitted ...]\n\nange (without counter-cyclical factor)  \n![](images/bdf4924791bcb6f668f7287eba4d10b959002675918e1dfc0b4bcff756ec2ab0.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribution t\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R021",
    "title": "NOM：亚洲出口的超级周期并非只有AI，一个被低估的转折点正在浮现",
    "digest": "[wechat_article.md]\n# NOM：亚洲出口的超级周期并非只有AI，一个被低估的转折点正在浮现\n\n市场对亚洲出口的讨论，大多集中在AI驱动的半导体和电子产业链上。但NOM最新发布的一份图表报告，揭示了一个更重要的信号：一个领先指标已经飙升至16年新高，而驱动因素正在从单一的技术周期，向一个更宽广、更可持续的复苏切换。\n\n这份报告的核心判断是：亚洲出口的超级增长周期远未结束，但市场可能低估了其结构性扩围的潜力。真正值得关注的，不是AI需求还能多强，而是当供应链扰动消退、全球资本品需求回升时，哪些国家、哪些行业能承接这轮“扩围”的增量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一个历史级信号：NELI指数升至16年高位，预示的不只是短期繁荣\n\nNOM亚洲出口领先指数（NELI）在7月攀升至121，这是自2006年以来的最高水平。该指数由九个分项组成，领先实际出口数据约三个月，且历史上准确预测了亚洲出口的每一次重大拐点。\n\n这个数字意味着什么？它暗示亚洲（除日本外）的出口增长动能将在三季度延续，甚至可能进一步加速。更重要的是，NELI的上升正在变得更加“广泛”——不仅科技相关指标强劲，整体制造业和中国需求也出现了改善迹象。\n\n这并非一个孤立的短期脉冲。NELI的构成决定了它能够过滤掉基数效应的干扰，反映的是出口增长的潜在动量。当这样一个领先指标创下16年纪录，其对资产定价的启示是：以出口为导向的经济体（如韩国、台湾、越南、马来西亚）的宏观基本面，可能在未来几个季度持续超预期。\n\n## 2. 科技周期仍是主力，但真正的变量在于“非科技”的接力\n\n报告明确指出，AI技术周期一直是亚洲出口的主要引擎。这一点市场已有充分定价。但NOM报告的关键增量，在于指出了另一个正在成形的驱动因素：霍尔木兹海峡的重新开放。\n\n这一点值得仔细拆解。霍尔木兹海峡\n\n[... middle omitted ...]\n\n更细致的拆解，并讨论这些信号对不同市场、不同资产的定价含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲出口的超级周期，还没结束\n\n亚洲出口，强势延续\n\nNELI指数飙至16年新高\n\n最近翻到一份NOM的研报，发现了一个挺有意思的信号：亚洲出口的景气度，可能比我们想象的还要强。\n\n1️⃣ **一个前瞻指标创了16年新高**\nNOM有个领先指标叫NELI，专门用来预测未来3个月的亚洲出口走势。7月这个读数飙到了121，是16年来的最高点。\n这个指标由9个细分项构成，过去几次大的拐点都提前捕捉到了，比看官方出口数据更灵敏。\n\n2️⃣ **驱动力不只是AI**\n虽然AI相关的科技产品出口依然是主要引擎，但好消息是，这次上涨的驱动力正在变广。\n除了科技板块，整体制造业和来自中国的需求都出现了改善迹象。也就是说，增长不再只靠少数几个行业撑着。\n\n3️⃣ **还有一个潜在利好**\n研报提到，霍尔木兹海峡如果重新开放，会缓解供应链的压力，降低经济不确定性。\n这可能会进一步拉动全球总需求，尤其是资本品，让亚洲出口的超景气周期从科技领域扩散到更多行业。\n\n**一点思考**\n出口周期的扩散，往往意味着企业盈利的改善会更普遍。如果你关注相关产业链，可以留意一下，哪些行业正在从“科技一枝独秀”转向“多点开花”。\n\n#学习笔记\n\n[\n\n[... middle omitted ...]\n\n---------------------|-------------------------------------|\n| Jul-16 | ~0                                 | ~90                                 |\n| Jul-18 | ~20                               \n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R022",
    "title": "JPM：中国消费板块的真正底部不在估值，而在盈利预期的重置",
    "digest": "[wechat_article.md]\n# JPM：中国消费板块的真正底部不在估值，而在盈利预期的重置\n\n中国消费板块正在经历一场罕见的估值与情绪双重压缩。JPM最新发布的研报以“Cheap but unloved”为题，直指当前市场最核心的矛盾：板块估值已跌至十年均值下方1.5个标准差，但80%覆盖公司的盈利预测仍在被下调。这份报告的真正价值不在于告诉你“便宜”，而在于揭示了“便宜”背后尚未被定价的结构性分化——下行周期中，真正决定回报的不是行业beta，而是企业运营质量。\n\n如果你认为消费板块的困境只是需求疲软，那你很可能错过了真正重要的信号。JPM的分析框架显示，市场对2026年盈利预期的下修远未结束，更关键的是，成本端压力将在2026年下半年集中释放，而这一点目前几乎未被充分定价。本文基于这份研报的核心逻辑，提炼出五个对投资者真正重要的判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 盈利下修尚未触底，2026年才是真正的压力测试窗口\n\n当前市场对消费板块的定价，隐含了一个假设：盈利下修已经大部分完成。但JPM的数据挑战了这一假设。截至报告发布，必需消费和可选消费板块2026年一致预期EPS分别较年初下调了9%和7%。从覆盖公司来看，80%的标的年初至今遭遇盈利下调，白酒、美妆等子行业是重灾区。\n\n然而，更值得关注的不是已经发生的下修，而是尚未出现的压力。报告明确指出，“成本压力的充分定价可能要到2026年底才会显现”。这一判断基于一个关键情景分析：如果伊朗冲突结束，包装材料和工业原料（如PE/PET）价格将较2025年均价上涨15-40%。结合JPM中国宏观团队对PPI和CPI的预测——2026年2-4季度PPI分别为3.5%、3.9%、3.5%，CPI仅为1.3%、1.4%、1.1%——CPI-PPI剪刀差将扩大至约2.9个百分点。\n\n[... middle omitted ...]\n\n们的知识星球微信群。我们会在群内分享原始报告和更深入的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n消费板块便宜但没人买，等盈利底\n\n便宜但有代价\n\n某外资投行刚发了中国消费研报，核心逻辑很清晰：估值够低了，但盈利还在下修，现在不是无脑捡便宜的时候。\n\n1⃣ 盈利下修还没完\n- 必选消费2026年EPS共识下修9%，可选消费下修7%\n- 80%覆盖的公司盈利预测都在往下调，白酒、美妆最惨\n- 少数逆势上调的：古茗、老铺黄金、李宁、农夫山泉\n\n2⃣ 成本压力是隐形炸弹\n- 假设伊朗冲突结束，PE/PET等包装原料已比去年均价涨15-40%\n- 研报预测PPI在3.5-3.9%，CPI只有1.1-1.4%，价差拉大到-2.9pp\n- 白酒和啤酒成本传导能力强，饮料最脆弱\n- 茅台、啤酒龙头、海天这类有定价权的相对安全\n\n3⃣ 阿尔法来自运营商质量，不是赛道\n- 需求端噪音多，但真正分化在微观层面\n- 用基本面、回报、估值三维度打分，未来3-5年看好：运动服饰、潮玩、白电\n- 安踏、泡泡玛特、美的在覆盖名单里\n\n4⃣ 关键催化剂与节奏\n- 3Q26成本通胀开始冲击，饮料要避\n- 中秋和国庆是白酒、黄金珠宝的重要观察窗口\n- 6月后可关注餐饮饮料（古茗、瑞幸、霸王茶姬）\n- 茅台从3Q26开始基数变友好，餐饮饮料要到2\n\n[... middle omitted ...]\n\nfication and important disclosures, including non-US analyst disclosures.\n\n## Key thesis\n\nChina Consumer Top Picks: (1) Nongfu (OW): strong brand momentum and margin buffer; (2) Anta (OW): wel\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R023",
    "title": "摩根斯坦利：中国钢铁市场的真实复苏信号，被周度数据的噪音掩盖了",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国钢铁市场的真实复苏信号，被周度数据的噪音掩盖了\n\n过去几周，围绕中国钢铁和铁矿石市场的讨论，大多集中在需求何时触底、库存压力能否缓解、以及减产政策是否会加码。这些问题的核心，其实指向同一个判断：市场参与者是否正在用错误的频率观察一个正在发生结构性分化的行业。\n\n摩根斯坦利最新发布的中国钢铁与铁矿石周度更新报告，提供了截至6月中旬的一组高频数据。单独看每一项，似乎只是常规的环比波动——长材表观消费周环比上升5.1%，扁平材上升2.0%；贸易商库存微降0.6%，钢厂库存微增0.7%；电炉开工率提高2个百分点。但如果把这些事实放在一起，一个更重要的信号浮现出来：市场真正低估的不是需求总量，而是供给端正在发生的、由电炉产能利用率回升所驱动的再定价。\n\n这份报告的价值，不在于它预测了价格方向，而在于它提供了一套可以持续追踪的、从“库存-产量-消费-发运”四维交叉验证的观察框架。真正值得关注的，不是某一周的数据好坏，而是这些数据叠加在一起，是否指向一个可持续的、由供给结构变化驱动的平衡点。\n\n以下是我们基于这份研报的核心解读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 长材消费的环比回升，可能比表面数字更有含金量\n\n报告显示，长材表观消费周环比增长5.1%，而扁平材仅增长2.0%。两者差距并非偶然。\n\n长材主要用于建筑和基建领域，其消费回暖往往与项目开工节奏、资金到位情况直接相关。5.1%的周环比增速，如果放在一个更长的时间窗口里观察，可能意味着前期积压的施工需求正在释放。而扁平材更多对应制造业和出口，2.0%的增速相对温和，与当前制造业PMI的修复节奏基本吻合。\n\n但这里有一个值得追问的问题：长材消费的回升，是补库行为还是终端真实消耗？报告没有直接回答，但它提供的另一个数据提供了线索——贸易商库存下\n\n[... middle omitted ...]\n\n们也正是我们希望在后续讨论中与读者共同拆解的方向。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n钢材需求回暖，铁矿石发运分化\n\n钢铁需求小幅回升\n\n📊 最新周度数据解读\n\n某外资投行最新周报显示，中国钢铁和铁矿石市场出现了一些值得关注的变化：\n\n**钢材端：需求与供给同步改善**\n1️⃣ 长材表观消费环比增长5.1%，扁平材增长2.0%\n2️⃣ 长材和扁平材周产量均环比上升\n3️⃣ 贸易商库存下降0.6%，但钢厂库存微增0.7%\n4️⃣ 电炉开工率提升2个百分点至64.4%，同比高7.7个百分点\n\n**铁矿石端：发运格局分化**\n1️⃣ 钢厂铁矿石库存小幅下降1.2%\n2️⃣ 钢厂开工率提升至62.9%，日均产量环比增1.2%\n3️⃣ 澳巴合计发运环比增加59万吨\n4️⃣ 但澳大利亚发运下降164万吨，巴西发运增加224万吨\n\n整体看，下游需求正在温和回暖，但钢材库存从贸易商向钢厂转移，反映终端采购节奏仍偏谨慎。铁矿石方面，巴西发运放量弥补了澳洲的减量，港口库存微增0.7%。\n\n对于后续走势，可以关注需求复苏的持续性和钢厂补库节奏。\n\n欢迎一起讨论对钢铁产业链的观察～\n\n#学习笔记\n\n[source_mineru.md]\n## Greater China Materials | Asia Pacific\n\n[... middle omitted ...]\n\nrom Australia were down by (1.64) Mt WoW. Shipments from Brazil were up by 2.24 Mt WoW.\n\nExhibit 1: Weekly data summary\n\n<table><tr><td colspan=\"4\">Steel</td><td colspan=\"3\">Iron Ore</td></tr>\n\n[... middle omitted ...]\n\nd>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb29.69</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R024",
    "title": "BARC：光学市场真正的拐点不在于AI需求本身，而在于供给结构正在经历不可逆的重塑",
    "digest": "[wechat_article.md]\n# BARC：光学市场真正的拐点不在于AI需求本身，而在于供给结构正在经历不可逆的重塑\n\n市场对AI拉动光学器件需求的叙事已经足够熟悉。过去两年，每一次关于数据中心互联、超算集群扩容的消息，都能在资本市场引发一轮对光学板块的关注。但这份BARC最新发布的光学模型更新报告，提供了一个更为细腻、也更值得产业决策者仔细审视的判断框架。\n\n报告的核心结论并不令人意外——BARC预计2026至2027年，全球光学网络市场将维持两位数的增长。真正有价值的洞察，藏在它对市场结构的拆解之中：增长的动力来源正在发生系统性切换，而不同细分市场的竞争壁垒和定价权正在经历根本性分化。理解这种分化，比单纯判断“AI需求是否真实”更具投资意义。\n\n这份报告更新了BARC对光学市场的详细模型，涵盖了长途、海底、城域以及可插拔模块（ZR/ZR+）的细分，并首次在客户垂直领域（电信、云、企业）做了明确的收入拆分。对于关注Ciena、思科等核心标的的投资者而言，这份报告提供了一个从总量判断下沉到结构性判断的分析框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 两位数的增长预期背后，是电信与云的双重驱动力正在形成合力\n\nBARC将2026年光学市场增长预期从此前的8%上调至10%，2027年从13%微调至12%。表面上看，这只是几个百分点的调整。但更值得关注的是，驱动这一增长的底层逻辑正在从“单一引擎”转向“双引擎”。\n\n过去几年，光学市场的增长呈现出典型的“跷跷板”效应。2022年，云计算厂商的大规模网络建设推动了市场增长。随后，电信运营商进入库存消化周期，叠加宏观压力，导致2023至2024年市场连续下滑。BARC的数据显示，2023年光学市场同比下降7%，2024年进一步下滑12%。这种“云强则市场强，云弱则市场弱”的特征，让整个行业高度依\n\n[... middle omitted ...]\n\n来星球微信群里继续讨论，一起拆解这份报告背后更深的产业逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光模块市场：2026-2027 增长加速\n\n光学网络进入上行期\n\n投行研报更新了光学模型，结论很直接：2026-2027 年，光学网络市场将实现双位数增长，背后是 AI 驱动的云需求和电信复苏。\n\n1️⃣ 市场整体判断\n- 2025-2027 年，光学市场增速从 9% 提升到 12%\n- 增长驱动力：AI 云建设（超铁路、DCOM 等）+ 电信客户恢复\n- 2023-2024 年市场经历消化期，现在进入加速通道\n\n2️⃣ 拆分看三大子市场\n- 长途（LH）：占市场一半，今年增长高个位数，受益于 AI 长距离连接\n- 城域（Metro）：2026-2027 年均双位数增长，ZR/ZR+ 可插拔模块是核心推手（2027 年市占率预计达 51%）\n- 海底（Sub）：2027 年恢复双位数增长，但整体占比小\n\n3️⃣ 客户结构变化\n- 电信仍是主力（>50%），但云厂商占比快速提升\n- 云市场 2027 年规模预计达 61 亿美元，是 2024 年的 2.2 倍\n- 企业端保持稳定\n\n4️⃣ 值得关注的玩家\n- CIEN：市场份额从 2018 年 16% 提升到 2027 年预估 32%，云市场市占率预计达 78%\n\n[... middle omitted ...]\n\nts. Additionally, we include a breakout of customer verticals (Telco, Cloud, Enterprise) and the estimated market share CIEN has in each.\n\nOverall growth has been choppy the last few years (pr\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R025",
    "title": "GS：全球IT服务订单的转折点不是AI，而是地缘政治",
    "digest": "[wechat_article.md]\n# GS：全球IT服务订单的转折点不是AI，而是地缘政治\n\n全球IT服务行业正在经历一个被市场误读的转折点。当投资者将目光聚焦于AI对传统系统集成商的颠覆性冲击时，GS最新发布的Accenture财报解读却揭示了一个更微妙、也更值得警惕的信号：订单下滑的真正推手并非技术革命，而是地缘政治摩擦。\n\n这份报告的核心判断值得每一位关注日本IT服务板块的投资者认真思考：全球IT服务需求的结构性分化正在加速，AI相关业务在扩张，但地缘政治风险正在成为悬在系统集成商头上的达摩克利斯之剑。市场可能低估了后者对行业基本面的影响周期。\n\nAccenture 3Q8/26（3-5月）财报显示，销售额基本符合预期，但新订单出现了四个季度以来的首次负增长，同比下降3%。更值得关注的是，管理服务订单同比骤降15%，而咨询订单却加速增长13%。这种分化背后，是中东局势导致部分客户决策延迟，而非AI对传统业务的替代。\n\n对日本IT服务板块而言，这份报告的启示在于：本土需求相对稳健，但全球化敞口大的企业将面临更大的不确定性。与此同时，AI相关业务的扩张趋势在日本也开始显现。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订单结构的分化揭示了客户决策逻辑的深层变化\n\nAccenture 3Q新订单的负增长并非均匀分布。管理服务订单从2Q的+3%骤降至-15%，而咨询订单从+8%加速至+13%。这种结构性分化是理解当前行业周期的关键。\n\n管理服务通常代表长期外包合同，其订单下滑往往意味着客户对未来业务不确定性的担忧。而咨询订单的加速增长，则反映出企业在战略层面仍然愿意投资于数字化转型和AI落地。两者之间的背离，恰恰说明客户正在将预算从“维持性支出”转向“变革性支出”。\n\n但这里有一个容易被忽略的细节：中东局势对订单的冲击主要集中在咨询业务，约4亿美\n\n[... middle omitted ...]\n\n报告原文和更多行业分析框架，帮助您建立更系统的投资决策体系。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球IT服务订单出现波动，AI业务却在扩张\n\n📊 订单承压，AI加速\n\n刚看完一份外资投行对Accenture最新财报的深度解析，核心趋势值得关注👇\n\n**1/ 订单端出现明显分化**\n3Q订单同比增长-3%，是四个季度以来首次转负。咨询类订单（系统集成先行指标）反而加速到+13%，但托管服务订单大跌-15%。地缘局势导致部分客户决策延迟，影响集中在制造和汽车行业。\n\n**2/ AI业务正在从概念验证走向商业部署**\n企业AI投资意愿依然强劲，需求集中在：AI实施支持、AI驱动的业务转型咨询、数据基础设施和安全。这不是短期概念炒作，而是实打实的项目落地。\n\n**3/ 对日本IT服务板块的启示**\n中东局势对日本本土IT需求影响有限，但NTT数据海外收入占比60%，可能受轻微拖累。日本市场也开始出现AI业务扩张趋势，NOM综合研究所和Trend Micro被认为受益潜力较大。\n\n**4/ 收入指引小幅下调**\n全年收入增速指引从+3%~+5%调整至+3%~+4%，管理层提示4Q地缘负面影响可能比3Q更大。\n\n总结：短期订单承压，但AI相关业务正在成为新的增长引擎。这个趋势在日本市场同样值得持续跟踪。\n\n#学习笔\n\n[... middle omitted ...]\n\nress to date and other factors, management made slight revisions to its full-year sales guidance, lowering the upper end and midpoint of its forecast range. Although the situation is driven by\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R026",
    "title": "JPM：能量饮料市场真正进入“买量竞争”阶段，品牌分化才刚刚开始",
    "digest": "[wechat_article.md]\n# JPM：能量饮料市场真正进入“买量竞争”阶段，品牌分化才刚刚开始\n\n这份JPM基于Numerator数据发布的2026年5月能量饮料月度监测报告，表面上是对品牌KPI的常规追踪，但如果你只看到“增速放缓”四个字，就错过了最重要的信号。\n\n报告真正揭示的判断是：美国能量饮料市场正在从“品类渗透红利期”转向“存量博弈期”。过去两年支撑高增长的逻辑——新用户涌入、购买频次提升、提价空间——正在同步收窄。这并不意味着行业见顶，而是竞争逻辑发生了根本性切换。\n\nJPM分析师Andrea Teixeira团队在报告中用大量连续13周滚动数据证明：品类整体投影销售额增速从4月的+15%左右降至5月的+10%，减速幅度超过500个基点。更值得关注的是，减速并非单一因素驱动，而是渗透率增速、购买频次、客单价三个引擎同时降温。\n\n这意味着什么？意味着过去“水涨船高”的阶段结束了。接下来，品牌之间的分化将急剧扩大。有些品牌会在减速中暴露脆弱性，有些则能凭借结构性优势守住阵地。这份报告的价值，不在于告诉你“谁在增长”，而在于告诉你“谁的增长更可持续”。\n\n以下是我们基于报告逻辑提炼的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 品类增速放缓的根源不在需求消失，而在“低频用户”的购买行为正在回归均值\n\n报告中最容易被误读的数据是品类整体家庭渗透率仍在创新高——5月13周滚动渗透率达到55.0%，较4月提升约80个基点。看起来市场还在扩张，但为什么销售增速反而降了？\n\n关键在于购买频次。品类整体购买频次同比增速在5月转为-2%，这是自2025年11月以来首次转负。而客单价增速虽然仍保持在+5%左右，但绝对金额环比已出现微降。\n\nJPM的数据提供了一个关键视角：品类渗透率提升主要来自新用户的首次尝试，但这些新用户的复购率和\n\n[... middle omitted ...]\n\n群里继续讨论这些未解问题，一起追踪能量饮料赛道的下一个拐点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n能量饮料五月数据，谁是赢家\n\n5月能量饮料数据更新\n\n刚看完某外资投行5月能量饮料行业数据，简单说说几个关键发现。\n\n1️⃣ 行业整体在降温\n- 5月预估销售额增速从4月的高点回落至+10%，连续第二个月放缓\n- 购买频次出现2025年11月以来首次同比下滑(-2%)，消费者购买间隔拉长\n- 家庭渗透率虽创新高(55%)，但增速也在放缓\n\n2️⃣ 品牌分化明显\n- Monster表现最抗跌：家庭渗透率32.7%创新高，单次花费持续上升(+6%YOY)，整体预估销售仍+14%\n- Red Bull压力加大：购买率从+4%转负至-3%，预估销售增速从11%骤降至4%\n- Celsius组合：主品牌Celsius销售转负(-3%)，但Alani Nu仍猛增+76%，家庭渗透率15.3%创新高\n- Bloom保持高增长：家庭渗透率+451bps、购买率+32%，但增速也在放缓\n\n3️⃣ 渠道和人群变化\n- 便利店渠道购买率增速明显放缓（-644bps至+3%），Z世代购买率环比下降近5%\n- 中高收入群体购买率也在走弱，但中产阶级绝对购买量仍创新高\n- 单次花费持续增长(+5%YOY)，连续22个月保持中高个位数增长\n\n[... middle omitted ...]\n\ne resilient vs. peers.  \n- Household penetration gains were mostly flat sequentially, decelerating by a slight -7 bps sequentially in 13-weeks ended May to +177 bps YOY (second consecutive per\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 16 Jun 2026 10:27 PM EDT\n\nDisseminated 17 Jun 2026 12:15 AM EDT"
  },
  {
    "id": "R027",
    "title": "摩根斯坦利：东盟电信股真正的回报来源不是5G，而是竞争格局的结构性改善",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：东盟电信股真正的回报来源不是5G，而是竞争格局的结构性改善\n\n市场对东盟电信板块的关注，长期集中在两个叙事上：一是5G资本开支周期何时见顶，二是数据中心需求能否带来第二增长曲线。但摩根斯坦利在最新发布的《Asia Summer School 2026: ASEAN Telecoms & Data Centers》报告中给出了一个更值得深思的判断：**决定未来12-18个月电信股超额收益的核心变量，不是技术升级，而是各国市场竞争格局的结构性变化。**\n\n这份报告覆盖了泰国、新加坡、马来西亚、印度尼西亚和菲律宾五个市场，并基于竞争、资本开支、监管、资本配置和估值五个维度进行了系统打分。结果并不令人意外：泰国和新加坡排名前二，菲律宾垫底。但真正有价值的不是排名本身，而是排名背后的逻辑——竞争格局的改善，正在重塑这些市场的投资回报框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 泰国和新加坡的领先，本质上是对“寡头红利”的定价\n\n摩根斯坦利的评分体系中，泰国以23分位居第一，新加坡以22分紧随其后。这两个市场的共同特征是什么？都是事实上的双寡头或准双寡头格局。\n\n泰国市场在TRUE与DTAC于2022年合并后，已经从三家竞争演变为AIS与TRUE的双寡头格局。报告明确指出，合并后的竞争环境“保持理性”（competition has been stable post merger）。这不仅仅是一个市场结构描述，更是一个定价信号——当市场参与者从三家减少到两家，价格战的动机显著下降，ARPU止跌回升的可能性大幅增加。报告中的ARPU数据也印证了这一点：泰国主要运营商的ARPU自2023年以来持续回升，而这一趋势在2024-2026年的预测中仍在延续。\n\n新加坡的情况则更为微妙。表面上看，新加坡是四家运营\n\n[... middle omitted ...]\n\n的原始报告图表，并与关注同一主题的投资者交流各自的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n东盟电信2026：谁是赢家？\n\n**封面：**\n5国排名解密\n\n**副标题：**\n泰国第一，菲律宾垫底\n\n---\n\n最近读了份某外资投行的东盟电信研报，把5个主要市场的底层逻辑拆得很清楚。直接上干货👇\n\n**1/ 五大驱动因子**\n研报用5个维度给各国打分：竞争格局、资本开支周期、监管环境、资本配置效率、估值水平。\n\n竞争越激烈→回报越低\n资本开支越大→ROIC越差\n监管越多→股东回报越受限\n\n**2/ 2026年排名**\n泰国(23分) > 新加坡(22分) > 马来西亚(20分)=印尼(20分) > 菲律宾(18分)\n\n**3/ 各国亮点**\n🇹🇭 **泰国**：双寡头格局稳定，TRUE和AIS各占40%份额，宽带ARPU在回升\n🇸🇬 **新加坡**：4家运营商竞争激烈，SIMBA低价宽带冲击市场\n🇮🇩 **印尼**：从10家整合到3家，Java岛外覆盖率将提升，ARPU趋近45k印尼盾\n🇵🇭 **菲律宾**：第三家运营商仍在搅局，宽带渗透率低于东盟平均水平\n\n**4/ 数据中心红利**\n研报提到运营商正受益于区域数据中心需求增长，这是传统电信业务之外的新增量。\n\n---\n\n你觉得东盟哪个市场最值得关注？\n\n[... middle omitted ...]\n\ndoes and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Invest\n\n[... middle omitted ...]\n\ntd>XL Axiata (EXCL.JK)</td><td>U (05/07/2025)</td><td>Rp2,580</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R028",
    "title": "NOM：四足机器人已越过盈亏线，但真正考验在于“大脑”尚未定型",
    "digest": "[wechat_article.md]\n# NOM：四足机器人已越过盈亏线，但真正考验在于“大脑”尚未定型\n\n2026年6月15日，NOM分析师团队实地走访了杭州的深度机器人公司（DEEP Robotics，未上市），并在18日该公司科创板IPO申请获受理后，发布了这份调研报告。这份报告的价值不在于它描述了机器人行业的火热——那是共识——而在于它提供了三个层次上市场尚未充分定价的判断：第一，这家四足机器人专业厂商在2025年首次实现全年盈利，营收同比增长227%至3.37亿元，净利润达到2900万元；第二，电力巡检和消防这两个垂直场景的需求正在从“试点”走向“批量部署”，但价格和性能仍然是规模化复制的硬约束；第三，也是最容易被忽视的一点，行业通往“物理AI”的技术路线尚未收敛，这意味着当前所有关于远期市场空间的线性外推，都可能建立在一条尚未选定的路径上。\n\n以下是我们从这份研报中提炼出的五个关键洞察，以及一个NOM尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2025年首次盈利是一个里程碑，但更值得关注的是毛利率与客户集中度的组合信号\n\n营收从2023年到2025年的复合年增长率达到159.5%，2025年产量3936台、销量2908台，产销率73.88%——这些数字本身已经能说明公司处于高速成长期。但报告中最值得推敲的财务信号是两个并存的事实：52.83%的毛利率和18.83%的前五大客户集中度。\n\n毛利率超过50%在硬件制造领域并不常见，尤其对于一家仍在快速扩张期的公司。这意味着产品定价权或成本结构有某种结构性优势——可能是四足机器人在特定场景下的不可替代性，也可能是公司在核心零部件或算法层面的自研壁垒。但与此同时，不到20%的前五大客户集中度暗示收入来源相对分散，这在一定程度上降低了单一客户依赖风险，但也意味着销售和渠道\n\n[... middle omitted ...]\n\n析师的核心判断逻辑，以及我们对这些关键变量的持续跟踪和解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n四足机器人IPO第一股，我实地看了\n\n刚盈利就上市\n\n年营收3.37亿，净利2900万\n\n上周去杭州看了家做四足机器人的公司，刚递交科创板上市申请。2025年营收同比增227%，首次年度盈利。几个核心信息量，直接拆：\n\n1️⃣ 电力+消防是主力场景\n- 东莞某变电站：每天巡检8.5小时，识别准确率超95%\n- 消防应急已在湖南、山西、河南铺开\n- 新加坡和北美也有园区仓库项目\n\n2️⃣ 工业场景还在探索期\n目前巡检机器人最大的瓶颈不是技术，是价格和性能。续航、定位精度、多楼层导航、极端环境适应——都还有改进空间。工业规模化落地，需要继续降本提能力。\n\n3️⃣ 物理AI至少还要8-10年\n管理层明确说：大脑（物理AI）路径还没收敛，VLA和世界模型两条路线还在竞争。小脑（强化学习模型）基本定型了。长期看防爆机器人是更大市场，但认证和载荷限制是难点。\n\n4️⃣ 产销量数据\n2025年生产3936台，销售2908台，产销率73.88%。毛利率52.83%，研发投入8400万，前五大客户集中度18.83%。\n\n个人观察：四足机器人从实验室走向商业化的节奏比预期快，但真正打开工业市场还需要2-3年。防爆、化工、矿山这类\n\n[... middle omitted ...]\n\npans the high-performance Jueying X series for industrial inspection, the Jueying Lite series for research and education, and the wheeled-leg Lynx series for mixed terrain. According to the co\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R029",
    "title": "NOM：宇树科技IPO揭示的真正悬念，不在硬件成本，而在“大脑”路线的未定",
    "digest": "[wechat_article.md]\n# NOM：宇树科技IPO揭示的真正悬念，不在硬件成本，而在“大脑”路线的未定\n\n当一家公司以5,500台人形机器人出货量位居全球第一，营收同比增长335%至17亿元人民币，并实现2.88亿元的净利润，毛利率约60%，它即将在科创板挂牌的消息，很容易被市场解读为“人形机器人商业化拐点已至”。\n\n但NOM在6月15日实地调研宇树科技后发布的这份报告，其真正有价值的判断并非关于出货量或毛利率。报告的核心洞察指向一个更根本、也更令人不安的结论：**行业当前最硬的约束条件，已经从“能不能动”转向了“能不能想”——而后者，整个行业都还没有找到确定的路径。**\n\n这份报告的价值，在于它没有停留在对宇树全栈自研能力的赞美，而是清晰区分了“已被验证的成本优势”与“尚未被验证的模型能力”。对于关注这一赛道的投资者而言，理解这两者之间的张力，比记住任何一组财务数字都更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 宇树的成本优势已构成护城河，但这条护城河可能只保护了一半战场\n\nNOM调研报告中最引人注目的数据，是宇树的成本结构：电机、减速器、激光雷达全部自研，外采部件仅占整体成本的14%至18%。配合超过90%的产销比，这组数字共同指向一个判断：宇树在人形机器人的“物理层”建立了一个相当完整的成本护城河。\n\n这一点在行业内并非普遍现象。许多竞争对手仍然依赖外购核心部件，这意味着它们在定价权和供应链韧性上天然处于劣势。宇树能够在2025年实现盈利，很大程度上正是得益于这种全栈自研带来的成本优势。管理层的表述也很清晰：成熟的四足机器人业务产生的现金流，正在反哺人形机器人的研发和市场拓展。\n\n但这里有一个关键问题需要区分：成本优势解决的是“能不能造得便宜”，而人形机器人产业当前的核心矛盾，已经不再是制造成本。NOM调研中引用的外部行\n\n[... middle omitted ...]\n\n“硬件厂商的数据闭环策略”这两个未解问题，展开进一步的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n宇树IPO过会，机器人“大脑”才是真门槛\n\n机器人公司，到底看什么？\n\n刚读完投行研报，去宇树科技实地调研后的分析，信息量很大👇\n\n1️⃣ 全栈成本优势是王牌\n2025年人形机器人出货5500+台，全球第一\n营收17亿，同比增335%，净利2.88亿\n毛利率约60%，产销率超90%\n电机、减速器、激光雷达自研，外购部件仅占成本14-18%\n\n2️⃣ 真正的瓶颈不在运动控制\n外部行业调研显示，宇树运动控制全球领先\n但真正卡脖子的是“大脑”——世界模型\n目前主流技术路线还没收敛\n从VLA模型转向世界模型，但各家对“世界”定义都不统一\n硬件厂商可能被AI巨头逐步挤压\n\n3️⃣ 应用场景正在从实验室走出来\n74%的人形机器人收入仍来自高校和科研机构\n但电网巡检和消防已是最快增长的工业场景\n其他垂直领域主要靠需求拉动，不是主动拓展\n\nIPO募资超50%将用于“大脑”研发\n这才是长期竞争力的关键\n\n对供应链企业持中性看法，认为人形机器人贡献的可持续性和规模存疑。\n\n欢迎一起讨论机器人赛道的技术路线和商业路径\n\n#学习笔记\n\n[source_mineru.md]\n## China advanced manufacturin\n\n[... middle omitted ...]\n\nnitree plans to issue 40.44mn shares to raise CNY4.2bn. In 2025, its humanoid shipments topped 5,500 units, ranking first globally, while revenue rose $335\\%$ y-y to CNY1.7bn and net profit re\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R030",
    "title": "NOM：机器人视觉的竞争壁垒不在“手”，而在“眼”和“脑”的数据飞轮",
    "digest": "[wechat_article.md]\n# NOM：机器人视觉的竞争壁垒不在“手”，而在“眼”和“脑”的数据飞轮\n\n机器人行业正在经历从“机器换人”到“智能体替代”的范式迁移。市场注意力大多集中在人形机器人的整机厂商和灵巧手供应商上，但一份NOM近期发布的研报，通过对国内机器视觉头部企业梅卡曼德（Mech-Mind Robotics，未上市）的实地调研，揭示了一个可能被低估的竞争逻辑：在机器人智能化的价值链中，“眼”（3D视觉）和“脑”（算法模型）所构成的认知层，才是当前最具规模效应和护城河潜力的环节，而“手”的执行层，尚处于商业化早期。\n\n这份报告的核心判断是：**机器人产业链的价值分配，正在从硬件集成向数据驱动的认知平台迁移。** 梅卡曼德的案例表明，谁能在“眼-脑”层面率先形成数据闭环，谁就有机会在长尾、多样化的工业场景中建立标准化部署的壁垒。以下是我们基于这份研报解析提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 连续六年市占率第一的背后，是“数据飞轮”而非单纯的硬件优势\n\nNOM在研报中指出，梅卡曼德在大型3D抓取领域（如拆垛）已连续六年保持国内市场份额第一。管理层的表述是：“做得多，数据就多，数据多就能改进模型。”这听起来像一句常见的商业口号，但其背后的竞争逻辑值得深究。\n\n在机器人视觉领域，单纯的传感器硬件（如深度相机）的差异化正在缩小。真正拉开差距的是算法对海量、多场景数据的消化能力。梅卡曼德的策略是不生产机器人本体，而是适配全系列机械臂。这意味着，每一次部署——无论是天津包裹处理中心每小时处理1800件包裹的场景，还是其他工业产线——都在为其“脑”积累新的训练数据。这种“眼”与“脑”的协同，构成了一个自我强化的正反馈循环：部署越多，模型越通用和稳定；模型越强，部署的门槛和成本就越低。\n\n这给我们的启示是：在评估机\n\n[... middle omitted ...]\n\n“眼-脑”平台成为主流，哪些机器人本体厂商将因此受益或受损？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n这家3D视觉公司，正在复制“数据飞轮”\n\n**3D视觉龙头，已跑通数据飞轮**\n\n最近走访了一家叫梅卡曼德的机器视觉公司，虽然没上市，但聊完挺有意思。\n\n他们专注做工业机器人的“眼睛”和“大脑”，不做机器人本体，但适配所有机械臂。核心逻辑很直接：用得越多，数据越多，模型迭代越快，通用性和稳定性就越好。\n\n分享几个核心看点：\n\n**1/ 大视野3D抓取，国内连续六年第一**\n- 主打拆垛场景，天津一个分拣项目每小时处理1800件\n- 约一半客户在海外，客户集中度不高，抗风险能力不错\n- 不过行业调研指出，和海康机器人等对手的技术差距可能在缩小\n\n**2/ “眼-脑-手”平台，瞄准长尾需求**\n- 核心收入来自3D视觉（眼睛）和算法（大脑）\n- 目标是推动行业从重定制向标准化部署转型，每年培训2000-3000名客户人员\n- 管理层强调可扩展性：大部分产品不需要大现场团队，定制化极少\n- 但“灵巧手”这块，还没形成规模化收入\n- 行业调研更谨慎：梅卡曼德的强项在视觉，而非运动控制，自研灵巧手需要时间，可能要靠股权激励抢人才\n\n**3/ 和奥比中光，走的是不同赛道**\n- 梅卡曼德在3D视觉有先发优势，后续可适配人\n\n[... middle omitted ...]\n\nnjin parcel-handling deployment processing up to 1,800 items per hour. The company does not produce robot bodies but adapts to the full range of robotic arms; in management's framing, \"doing m\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R031",
    "title": "美国银行：市场正在定价的不是繁荣，而是繁荣之后的“谁先离场”",
    "digest": "[wechat_article.md]\n# 美国银行：市场正在定价的不是繁荣，而是繁荣之后的“谁先离场”\n\n这份报告最值得关注的判断，不是资金流入了多少，而是资金流入的分布结构，正在复刻历史上泡沫末期的典型特征。美国银行最新一期的《The Flow Show》显示，过去一周全球股票基金净流入1264亿美元，创下历史纪录。其中美国股票单周流入1192亿美元，同样刷新历史。科技股单周流入192亿美元，也创下纪录。如果按年化推算，2026年全年美国股票基金流入将达7390亿美元，科技股流入将达1540亿美元。\n\n这些数字本身并不令人惊讶。真正值得警惕的是，当资金以这种速度和集中度涌入单一市场、单一风格、单一主题时，历史上往往对应的是泡沫的“最后一段”。美国银行的牛熊指标已升至9.2，进入“极端看多”区间，这是一个自2002年以来触发过17次、命中率约60%、平均回撤2-3%、最大回撤15-20%的卖出信号。\n\n这份报告的核心主张是：当前市场定价的核心变量，已经从“经济增长能否持续”，切换为“政治周期与收益率曲线谁会先打破泡沫”。这不是一篇关于基本面复苏的乐观叙事，而是一篇关于“谁先眨眼”的博弈论分析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资金流向的集中度已经触及历史泡沫的“天花板”\n\n美国银行的报告提供了一个极为关键的历史对照。当前AI相关十大股票占标普500指数的权重已达到39%。这个数字本身已经接近甚至超过了历史上几次著名泡沫的集中度峰值：19世纪80年代的铁路股、1972年的“漂亮50”、1999年的TMT泡沫，以及1985年日本股市占全球市值的巅峰。\n\n图表3的横截面比较非常清晰：每一次市场集中度达到这个水平，都对应着一场泡沫的尾声。这不是说泡沫马上会破裂，而是说“继续集中”的空间已经极为有限。报告进一步用1998年至2000年的历史数据说\n\n[... middle omitted ...]\n\n结合完整报告中的原始图表和数据分析，共同推演后续的市场路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI涨到39%了，然后呢？\n\n市场在赌什么？\n\n这轮行情，像极了1999年\n\n某外资投行最新周报，拆了几个有意思的逻辑：\n\n1️⃣ AI已成标普最大单一主题\nAI板块占标普500市值39%，创历史新高\n比当年“漂亮50”的峰值还高\n历史参考：只有铁路在1880年代超过这个集中度\n→ 泡沫的特征不是分散，而是集中\n\n2️⃣ 资金疯狂流入，但情绪已到极端\nBofA牛熊指标升至9.2（极牛区间）\n过去17次触发这个信号，全球股市平均回调2-3%\n最大回撤15-20%，命中率约60%\n但没人知道这次是不是例外\n\n3️⃣ 通胀担忧在转变方向\n市场担心“通胀=加息”\n但如果油价大跌能压住CPI回到3%以下\n那从“通胀繁荣”到“滞胀衰退”的路径可能被阻断\n关键是：油价能不能跌\n\n4️⃣ 美国大选才是真正的变量\n如果共和党在11月丢掉参议院\n市场预期是：美元跌、利率跌、股票跌\n现在华尔街对特朗普的满意度处于历史高位\n但选民通胀满意度只有28%\n\n5️⃣ 资金流向：极度集中\n美国股票周流入1192亿美元（历史纪录）\n科技股周流入192亿美元（历史纪录）\n欧洲股票连续10周流出\n中国股票连续12周流出\n→ 全球资金在“押注美国+\n\n[... middle omitted ...]\n\no in positive territory last 6 months of bubble (Charts 12-13).\n\nTale of the Tape: votes...Iran done ending plunge in Trump/economy/inflation approval (Chart 9); Wall St approval @ all-time hi\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R032",
    "title": "摩根斯坦利：市场误读了陆家嘴论坛的信号，真正重要的是利率传导机制的重塑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场误读了陆家嘴论坛的信号，真正重要的是利率传导机制的重塑\n\n市场对近期陆家嘴论坛的解读，主要集中在“资本账户开放是否转向”这一命题上。多数评论聚焦于监管收紧与QDII额度发放之间的表面矛盾，并试图从中判断政策风向的边际变化。但摩根斯坦利在论坛后发布的这份研报，提出了一个更为根本的判断：**陆家嘴论坛最重要的信号，不是资本账户开放的速度，而是货币政策传导机制正在经历一次静默但关键的升级。** 这份报告提醒我们，如果将全部注意力放在资本流动的“开关”上，可能会错过一个正在发生的、更具结构性意义的制度变革。\n\n报告的核心洞察在于，中国人民银行宣布将隔夜逆回购利率的波动区间收窄至7天逆回购利率上下各25个基点（此前为+50/-20个基点）。这并非一次简单的技术调整。在摩根斯坦利看来，这一变化的方向性意义在于，它使得短期流动性管理更加规则化和透明化，从而为提高整个政策利率体系的传导效率铺平了道路。市场当前低估了这种“机制优化”对长期资产定价和银行体系行为模式的潜在影响，而高估了短期内总量宽松的可能性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利率走廊的收窄不是在暗示降息，而是在为未来的传导效率铺路\n\n市场往往倾向于将任何利率机制的调整解读为“宽松”或“紧缩”的前奏。但摩根斯坦利的分析明确指出，这次利率走廊的收窄，其首要目标并非释放降息信号，而是改善政策利率向市场利率的传导效率。报告特别强调，在银行净息差压力高企的背景下，央行短期内不会降息。这意味着，2026年下半年乃至2027年，广义政策利率的调降可能性极低。\n\n这一判断的逻辑链条是清晰的：一个过宽的利率走廊，使得短期市场利率容易大幅偏离政策目标利率，削弱了央行通过调整政策利率来引导实体经济融资成本的能力。收窄走廊，本质上是在为未来的每一次政策利率\n\n[... middle omitted ...]\n\n化传导能否有效替代总量宽松”这一未解问题，进行更深入的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n央行刚放信号：利率传导升级，不是降息\n\n利率传导更透明，但降息还得等\n\n最近陆家嘴论坛释放了几个关键信号，我帮大家拆解一下👇\n\n**1️⃣ 利率走廊改革，不是降息信号**\n央行把隔夜逆回购利率走廊从+50/-20bp收窄到+/-25bp，让短期流动性管理更规则化、透明化。但投行研报明确说：这方向是好的，但别误会成要降息——银行净息差压力太大，2026下半年到2027年降息基本没戏。\n\n**2️⃣ 资本账户开放：没转向，但更严了**\n最近对境外投资的收紧，不是要堵死资本流动，而是要把资金引到合规通道。央行还承诺了：推离岸人民币回购工具、在上海自贸区试点离岸人民币外汇交易、支持离岸金融。\n\n**3️⃣ 不对称开放是长期策略**\n“不可能三角”下，中国优先保货币政策独立性和汇率稳定，所以资本账户开放会渐进且不对称——贸易、FDI、机构资金更开放；个人换汇、证券投资、短期资本依然严控。\n\n安全局也透露：要发新一批QDII额度、优化FDI规则、完善外汇贷款和跨境股权激励制度。\n\n💡 总的来说：方向是继续开放，但节奏可控，别指望短期内大放水或资本自由流动。\n\n#学习笔记\n\n[source_mineru.md]\n## Ch\n\n[... middle omitted ...]\n\nisclosed plans to issue a new batch of QDII quotas, improve FDI rules, and optimize foreign exchange loan and cross-border equity incentive systems.  \nToday's policy comments could ease concer\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R033",
    "title": "GS：铝市场真正被低估的不是地缘溢价，而是两股供给冲击的时间错配",
    "digest": "[wechat_article.md]\n# GS：铝市场真正被低估的不是地缘溢价，而是两股供给冲击的时间错配\n\n这份研报的核心判断，值得每一个关注大宗商品周期的决策者重新审视。\n\n当前市场对铝价的讨论，大多集中在霍尔木兹海峡的地缘风险上。主流叙事是：中东供应中断推高了近端价格，一旦局势缓和，价格将迅速回落。GS的最新报告提出了一个更精细、也更有投资含义的框架——市场正在经历的不是单一供给冲击，而是两股方向完全相反的供给力量在时间轴上的错配。\n\n第一股冲击来自中东。GS大幅下调了2026年和2027年中东地区的铝产量预测，下调幅度分别达到约66万吨和100万吨。这不仅仅是因为冲突本身，更关键的是复产节奏。报告指出，即使是宣布的临时协议达成、海峡重新开放，受损的电解槽修复和减产产能的逐步重启也需要接近一年的时间。参照2025年4月伊比利亚电网事故后Alcoa重启San Ciprian电解铝厂的经验，从停到满产大约需要12个月。这意味着，中东的供给缺口将延续至2027年。\n\n第二股冲击来自亚洲，尤其是印度尼西亚和中国。GS上调了印尼2026年和2027年的原铝产量预测，分别至170万吨和290万吨，背后是Adaro、Taijing Morowali、Juwan Weda Bay等项目的加速爬坡，以及Harita Danantara Inalum从2027年起纳入产能统计。中国方面，GS也将2026年和2027年的产量预测上调至4560万吨和4630万吨，理由是强劲的行业利润正在推动重启、替代项目甚至部分超产。\n\n这两股力量的交汇，决定了铝市场的真实图景：近端因中东缺口而收紧，远端因亚洲供给浪潮而宽松。GS将2026年Q3和2027年全年LME铝价预测分别上调至3300美元/吨和2950美元/吨，但仍显著低于远期曲线（3400美元/吨和3250美元/吨），核心逻辑就是——亚洲供给的增量最终会覆盖中东的损失\n\n[... middle omitted ...]\n\n产的实时跟踪指标。这些内容，在公开的研报摘要里很难完全展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铝的“双面冲击”：中东减产 vs 亚洲增产\n\n📉 铝价短期有支撑，但中期看空\n\n最近某外资投行更新了铝的研报，核心逻辑很清晰——全球铝市场正经历两种完全不同的供应冲击。\n\n**1️⃣ 中东供应：恢复比想象更慢**\n- 中东冶炼厂因冲突受损，停产规模比预期更大\n- 即使霍尔木兹海峡重新开放，受损的生产线修复需要时间\n- 预计巴林和UAE分别要到2027年中/底才能恢复至冲突前水平\n- 参考历史：2025年4月伊比利亚电网事故后，Alcoa用了约一年才完全恢复\n\n**2️⃣ 亚洲增产：印尼+中国正在填补缺口**\n- 印尼2026年产量上调至170万吨，2027年达290万吨\n- 多个项目（Adaro、青山系等）加速投产，部分镍项目电力被重新分配给铝\n- 中国产量超出4500万吨产能上限，2026年预计4560万吨\n- 高冶炼利润（接近2022年高点）支撑增产动力\n\n**3️⃣ 市场平衡：2026短缺→2027小幅过剩**\n- 2026年全球短缺72万吨，2027年转为过剩59万吨\n- 短期（Q3）缺口更大，支撑价格，但中期看空\n- 研报上调2026Q3/2027均价预测至3300/2950美元/吨，但仍低于远期合\n\n[... middle omitted ...]\n\n \\$3,300/\\$2,950/t from \\$3,200/\\$2,750/t previously (Exhibit 1), but remain below forwards at \\$3,400/\\$3,250/t, as stronger Indonesia and China supply growth — helped by high smelter margins\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R034",
    "title": "摩根斯坦利：韩国K型复苏的裂口正在闭合，但市场低估了财富效应与政策节奏的共振",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：韩国K型复苏的裂口正在闭合，但市场低估了财富效应与政策节奏的共振\n\n这份来自摩根斯坦利亚洲团队的研报，核心判断并非“韩国经济在复苏”——市场对此已有预期。真正值得关注的信号是：**韩国经济正在从过去几年典型的K型复苏，转向更广泛、更均衡的全面反弹，且这一反弹的力度和节奏，可能超出当前市场定价。**\n\n报告预计韩国2026年GDP增速将从2025年的1.1%跃升至2.8%，2027年稳定在2.2%。这个数字本身并不惊人，但支撑其实现的逻辑链条——科技出口超级周期、消费超预期回暖、财政空间意外打开、货币政策被迫转向紧缩——每一环都在挑战市场过去两年形成的“韩国经济结构性疲弱”的叙事。\n\n以下是我们从这份报告中提炼的五个关键洞察，以及一个尚未被充分讨论的隐含风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 科技出口的“量价齐升”不是短期脉冲，而是产能周期与AI需求的深度耦合\n\n报告中最具冲击力的数据是：2026年5月，韩国月度出口额创下历史新高，半导体出口增速同比超过60%，且这一增长并非单纯由价格驱动。报告明确指出，DRAM和HBM的bit出货量预计在未来多个季度维持两位数增长，这意味着需求端的AI资本开支周期正在转化为实打实的产能利用率提升。\n\n更关键的是，半导体在韩国总出口中的占比已从2024年的约30%跃升至40%以上。这并非简单的结构性集中度风险，而是意味着韩国出口的“质量”发生了根本变化——从过去依赖周期性大宗商品和汽车，转变为深度嵌入全球AI基础设施的供应链核心。报告中的资本品进口数据也印证了这一点：设备投资和资本品进口在2025年后显著加速，说明企业不仅在享受当前红利，更在为下一轮产能扩张做准备。\n\n对于投资者而言，这意味着韩国科技股的盈利预测存在系统性上修的可能，而非仅仅是一次性的\n\n[... middle omitted ...]\n\n内其他专业投资者一起推演不同情景下的资产定价含义。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国经济：从K型复苏到全面反弹\n\n韩国经济正在经历一场转变\n\n📌 关键看点\n\n韩国经济正从“K型复苏”走向全面反弹，预计2026年GDP增速将从2025年的1.1%跃升至2.8%，2027年稳定在2.2%。\n\n1️⃣ 出口：AI驱动的新周期\n- 半导体出口占韩国总出口比重已达40%\n- HBM和通用DRAM需求强劲，出口量预计保持两位数增长\n- 2026年5月日均出口同比增速达60.9%，创周期新高\n\n2️⃣ 消费：复苏速度快于预期\n- 财政支持、财富效应和工资增长共同推动消费回暖\n- 商品和服务消费均有望持续增长\n- 服务业生产增速预计在2026年初达到4%\n\n3️⃣ 通胀与政策\n- CPI面临上行压力，预计达到2.5%\n- 企业盈利强劲带来充足税收，政府可能在2026下半年推出追加预算\n- 韩国央行预计从2026年7月开始，在一年内加息4次，终端利率达3.50%\n\n4️⃣ 风险偏向上行\n- 科技出口表现超预期带来财政意外收入\n- 产能投资和资本品进口同步增长，显示企业信心增强\n\n欢迎一起讨论韩国经济走势，你对半导体周期怎么看？\n\n#学习笔记\n\n[source_mineru.md]\nInvestor Pre\n\n[... middle omitted ...]\n\noupled with a faster-than-expected consumption recovery look set to close the negative output gap two quarters earlier than our previous forecast. We see above-potential growth for the next tw\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R035",
    "title": "摩根斯坦利：日本制药板块的错位定价正在为深度价值投资者创造窗口",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：日本制药板块的错位定价正在为深度价值投资者创造窗口\n\n这份2026年6月发布的摩根斯坦利日本制药行业报告，在当前市场情绪低迷的背景下，传递了一个值得产业决策者和长期资本认真审视的信号：日本制药板块的整体估值已经压缩至历史低位，但结构性分化远比表面市盈率所显示的更为剧烈。报告覆盖的18家公司中，摩根斯坦利给出了7个Overweight评级，但加权平均市盈率仅为15.8倍，远低于美国制药板块的21.6倍和欧洲的15.3倍。这个估值折价背后，是市场对日本制药企业全球化能力、专利悬崖应对以及研发管线转化效率的系统性低估。报告最核心的判断并非板块整体便宜，而是某些被市场情绪压制的头部标的，其风险收益比已经出现了不对称性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对日本制药的估值折价可能过度反映了历史包袱而非未来价值\n\n当前日本制药板块加权市盈率仅为15.8倍，而美国同行高达21.6倍，折价幅度接近27%。这一差距在历史上并非罕见，但值得关注的是折价的构成正在发生变化。过去十年，日本制药的折价主要来自三方面：本土市场增长停滞、国际化进程缓慢以及研发效率低于欧美同行。然而，摩根斯坦利的研究表明，这些因素的权重正在被重新评估。\n\n以Daiichi Sankyo为例，该股年初至今下跌了25%，当前股价仅为2,520日元，较摩根斯坦利给出的4,650日元目标价存在85%的上行空间。这家公司是日本制药全球化的标杆，其ADC（抗体偶联药物）技术平台已被全球顶级药企认可，但市场似乎更关注其短期盈利波动而非管线价值。2026年预计EPS仅为126.4日元，但到2030年预计将增长至276.2日元，CAGR达到6%。当前19.9倍的2027年市盈率，对于一家拥有全球差异化技术平台的公司而言，并不算昂贵。\n\n关键在于，\n\n[... middle omitted ...]\n\n里继续讨论，我们可以一起拆解那些报告没有完全说透的隐含假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本药企研报：谁在逆势上涨？\n\n日本制药板块观察\n\n一份外资投行的日本制药业研报，覆盖了18家公司，给了一个“中性”的行业观点。但仔细看，里面藏着不少有意思的分化信号。\n\n**1. 大药企：第一三共是头号选手**\n第一三共被列为Top Pick（首选），目标价与现价差距很大。研报认为其管线价值被低估。武田、大冢、中外制药也获“超配”评级，但排序上第一三共最靠前。估值上看，日本药企整体PE在15-16倍左右，比美国同行（21-22倍）便宜不少。\n\n**2. 中盘与仿制药：Kaken和Towa有看点**\n在中盘和仿制药领域，Kaken和Towa获得“超配”。Towa的估值很有意思：2025年PE高达36倍，但2026年直接降到7.5倍，背后是EPS预计从106.7日元跳升到513.9日元——研报认为这是业绩拐点。Kaken的PEG只有0.6，是覆盖公司里最低的之一，说明成长性相对估值有吸引力。\n\n**3. 被“低配”的公司：为什么？**\n小野药品和协和麒麟被“低配”。小野药品目标价较现价有14%的下行空间，协和麒麟更是有25%的下行空间。协和麒麟的EPS增长预期只有1%，PEG高达8.3倍，性价比明显不足。\n\n*\n\n[... middle omitted ...]\n\n26\n</details>\n\n## PHARMACEUTICALS\n\nJapan\n\nIndustry View In-Line\n\nMS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a \n\n[... middle omitted ...]\n\naceutical (4502.T)</td><td>O (01/13/2026)</td><td>¥5,037</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 1: EM currencies have been on a round-trip over the last week, initially rallying on a conflict resolution but then depreciating following the more hawkish-than-expected FOMC Spot returns vs USD"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: As macro fundamentals continue to justify a weaker Yen the impact of intervention risk has diminished"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 3: AUDUSD has moved more in line with fundamentals recently..."
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ...while NZDUSD looks to have more room for catch up"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We forecast a gradual appreciation in EGP against the Dollar, and therefore see it outperforming forwards over the medium term"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Key measures of Egypt's external fundamentals have remained strong despite the Iran war"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 30-city daily property transaction volume in the primary market edged up over the last week and remained above year-ago level"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: 16-city daily property transaction volume in the secondary market was roughly flat over the last week but remained above year-ago level"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: NBS 70-city secondary home prices continued to decline in May"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China's passenger flights for domestic routes rose over the past week but remained below year-ago level"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: China's passenger flights cancellation rate declined over the last week but remained elevated"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Traffic congestion edged up over the last week"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 7",
    "context": "From 2022 onwards, we changed our data"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Amid declines in Brent price, domestic gasoline and diesel prices were lowered by 515 and 495 RMB/tonne respectively on 18 June"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The Morning Consult consumer confidence edged down"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Steel demand slightly edged up over the past week"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Steel production slightly edged up over the past week"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Daily coal consumption in coastal provinces remained rangebound over the last week and was above year-ago level"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "Exhibit 14: RMB 1.67bn local government special bonds have been issued year-to-date"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Official port container throughput edged down over the last week but was above year-ago level"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Exhibit 17",
    "context": "Exhibit 17: US soybean export sales to China continued to edged down in late May"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Our nowcast indicates China oil demand remained at 16.2mb/d in the latest reading"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Exhibit 19",
    "context": "Exhibit 19: China visible landed crude inventories edged down over the last two weeks"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Interbank repo rates edged up"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Exhibit 21",
    "context": "Exhibit 21: CNY appreciated against both the USD and the CFETS basket"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Exhibit 22",
    "context": "Exhibit 22: USDCNY fixing implied countercyclical factor remained rangebound recently"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China-sourced BD deals surged to over 50 each quarter since 4Q25 Number of in-license/out-license BD and M&A for China Biotech"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Total deal sizes continue upward trend Total deal value of out-license BD and company acquisition activities for China Biotech (FY2022-26)"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Therapeutic areas are diversifying in China out-license deals... Number of out-license BD deals for China Pharma/Biotech (FY2022—2026YTD), by therapeutic areas Unit: # of BD deals"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ...as well as in modalities where China has built visible clinical and platform depth Number of out-license BD deals for China Pharma/Biotech (FY2022—2026YTD), by modality"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Number of China out-license BD deals has reached about a quarter of total number of deals globally China go-global as % of global BD deals"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: China out-license BD deals have gained a significant proportion of total global deal size China go-global deal size as % of global BD deal size"
  },
  {
    "figure_id": "F033",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "Figure 1: Resident outflows from China have picked up in recent years, with unrecorded flows accounting for a major share"
  },
  {
    "figure_id": "F034",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "Figure 2: The synchronized strength in CNY FX and Chinese equities has created return synergies for domestic investors"
  },
  {
    "figure_id": "F035",
    "report_id": "R005",
    "label": "Figure 3",
    "context": "Figure 3: Resident outflows through southbound Bond Connect have picked up since last year's policy relaxation"
  },
  {
    "figure_id": "F036",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "Figure 4: The PBOC has resumed the expansion of the QDII quota"
  },
  {
    "figure_id": "F037",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "Figure 5: Dim Sum and Panda bond issuance is growing"
  },
  {
    "figure_id": "F038",
    "report_id": "R005",
    "label": "Figure 6",
    "context": "Figure 6: FX deposits as % of total liabilities by bank"
  },
  {
    "figure_id": "F039",
    "report_id": "R007",
    "label": "Figure 1",
    "context": "Figure 1: China retail sales YoY trend"
  },
  {
    "figure_id": "F040",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "Figure 2: China retail sales YoY trend – key categories"
  },
  {
    "figure_id": "F041",
    "report_id": "R007",
    "label": "Figure 3",
    "context": "Figure 3: Retail sales yoy growth ranked by category – May 2026"
  },
  {
    "figure_id": "F042",
    "report_id": "R007",
    "label": "Figure 4",
    "context": "Figure 4: Change in yoy growth by category (May 26 vs Apr 26)"
  },
  {
    "figure_id": "F043",
    "report_id": "R007",
    "label": "Figure 5",
    "context": "Figure 5: Unemployment rate – overall"
  },
  {
    "figure_id": "F044",
    "report_id": "R007",
    "label": "Figure 6",
    "context": "Figure 6: Unemployment rate – 16-24 years old"
  },
  {
    "figure_id": "F045",
    "report_id": "R007",
    "label": "Figure 7",
    "context": "Figure 7: China retail sales – online vs. offline sales growth"
  },
  {
    "figure_id": "F046",
    "report_id": "R007",
    "label": "Figure 8",
    "context": "Figure 8: China retail sales – online % of total"
  },
  {
    "figure_id": "F047",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "Figure 9: China headline CPI yoy"
  },
  {
    "figure_id": "F048",
    "report_id": "R007",
    "label": "Figure 10",
    "context": "Figure 10: China non-food CPI yoy"
  },
  {
    "figure_id": "F049",
    "report_id": "R007",
    "label": "Figure 11",
    "context": "Figure 11: China Staples 12-month forward P/E band"
  },
  {
    "figure_id": "F050",
    "report_id": "R007",
    "label": "Figure 12",
    "context": "Figure 12: China Discretionary (ex-Internet and auto) 12-month forward P/E band"
  },
  {
    "figure_id": "F051",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 1: Target Prices for Japanese Equities"
  },
  {
    "figure_id": "F052",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: TOPIX EPS Forecast"
  },
  {
    "figure_id": "F053",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: TOPIX ROE Forecast"
  },
  {
    "figure_id": "F054",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: Japanese Equities Outlook to End-2026 (TOPIX, Nikkei 225) Note: Orange shading indicates the end-2026 target price. Figure 4: TOPIX P/E Forecast"
  },
  {
    "figure_id": "F055",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: 2026 Year-to-Date Performance"
  },
  {
    "figure_id": "F056",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 7: Sector Allocation Figure 8: EPS Estimates by TOPIX 17 Sectors"
  },
  {
    "figure_id": "F057",
    "report_id": "R008",
    "label": "Figure 10",
    "context": "Figure 10: Net Profit Estimates for the Nikkei 225 Constituents"
  },
  {
    "figure_id": "F058",
    "report_id": "R008",
    "label": "Figure 9",
    "context": "Figure 9: Valuation Levels by TOPIX 17 Sectors"
  },
  {
    "figure_id": "F059",
    "report_id": "R008",
    "label": "Figure 11",
    "context": "Figure 11: Net Profit Estimates for the TOPIX 500 Constituents"
  },
  {
    "figure_id": "F060",
    "report_id": "R009",
    "label": "Figure 1",
    "context": "Figure 1: The 2026 dots show 12.5bp of rate hikes, and 6 of the 18 dots projected two or more hikes Distribution of projected midpoint of fed funds target range for 2026, March 2026 vs. June 2026; number of participants"
  },
  {
    "figure_id": "F061",
    "report_id": "R009",
    "label": "Figure 2",
    "context": "Figure 2: Both the statement and the press conference were scored hawkishly Fed Hawk-Dove Score\\* of FOMC statements and prepared press conference remarks; Index"
  },
  {
    "figure_id": "F062",
    "report_id": "R009",
    "label": "Figure 2",
    "context": "Figure 3: Post-FOMC, the implied distribution for Dec '26 shifted hawkishly, and both tails strengthened, indicating higher policy uncertainty Probabilities of different fed funds outcomes for Dec '26 calculated from the risk-neut"
  },
  {
    "figure_id": "F063",
    "report_id": "R009",
    "label": "Figure 4",
    "context": "Figure 4: Inflation markets shifted hawkishly with rising real yields and falling breakevens Daily change from 6/16 to 6/17 in 5-, 10-, and 30-year breakevens and real yields, bps"
  },
  {
    "figure_id": "F064",
    "report_id": "R009",
    "label": "Figure 5",
    "context": "Figure 5: The WAM of the Fed's SOMA remains significantly longer than that of the overall Treasury market"
  },
  {
    "figure_id": "F065",
    "report_id": "R009",
    "label": "Figure 7",
    "context": "Figure 7: 5-year breakevens have underperformed fundamentals since May and no longer appear fairly valued to our framework 5-year TIPS breakeven fair value model $^{*}$ ; bp"
  },
  {
    "figure_id": "F066",
    "report_id": "R009",
    "label": "Figure 8",
    "context": "Figure 8: On-the-run volumes in the 5-year TIPS sector usually see a large spike on auction days Daily Treasury volumes of 5-year on-the-run TIPS versus 0- to 5-year TIPS off-the runs in auction days versus other days\\*; \\$bn"
  },
  {
    "figure_id": "F067",
    "report_id": "R009",
    "label": "Figure 10",
    "context": "\\*Repo rates subject to change ## Technical analysis"
  },
  {
    "figure_id": "F068",
    "report_id": "R009",
    "label": "Figure 11",
    "context": "Figure 11: JPM Treasury Client Survey Treasury Client Survey Index\\*; %"
  },
  {
    "figure_id": "F069",
    "report_id": "R009",
    "label": "Figure 14",
    "context": "Figure 14: Active Core Bond Fund\\* Managers' exposure to 10-year Treasuries Partial beta with respect to 10-year US Treasury yields in our model for active bond fund excess returns\\*\\*"
  },
  {
    "figure_id": "F070",
    "report_id": "R009",
    "label": "Figure 12",
    "context": "Figure 12: CFTC non-commercial positions Net longs in SOFR and Treasury futures; 000s of TY equivalents"
  },
  {
    "figure_id": "F071",
    "report_id": "R009",
    "label": "Figure 15",
    "context": "Figure 15: Macro Hedge Fund exposure to 10-year Treasuries Partial beta with respect to the JPM US 7-10Y bond index in our model for macro hedge fund returns\\*"
  },
  {
    "figure_id": "F072",
    "report_id": "R009",
    "label": "Figure 13",
    "context": "Figure 13: CTA exposure to 10-year Treasuries Partial beta with respect to the JPM US 7-10Y bond index in our model for CTA returns\\*"
  },
  {
    "figure_id": "F073",
    "report_id": "R009",
    "label": "Figure 16",
    "context": "Figure 16: T-note dollar weighed Put/Call ratio The total (OI \\* settlement prices) of the individual T-note future Puts divided by the same calculation for Calls"
  },
  {
    "figure_id": "F074",
    "report_id": "R010",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Exports of Swiss Wristwatches watches by price categories Swiss watch exports by price - Total market (1'000 units)"
  },
  {
    "figure_id": "F075",
    "report_id": "R010",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Swiss watch exports by material Swiss watch exports by material - Total market (CHF Mil)"
  },
  {
    "figure_id": "F076",
    "report_id": "R010",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Swiss watch exports by country in absolute numbers Swiss watch exports by country - Key markets only (CHF Mil)"
  },
  {
    "figure_id": "F077",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1: While still early cycle, the change in tone suggests that exploration is moving back up the agenda for the majors, supporting a recovery in seismic demand over time"
  },
  {
    "figure_id": "F078",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Industry reserve life was broadly flat at 10.2 years in 2024 Reserve life (year) per FAS69 data"
  },
  {
    "figure_id": "F079",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Top Projects oil reserve life has fallen 35 years since 2012 Top Projects reserve life, by year of report and breakeven"
  },
  {
    "figure_id": "F080",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Exploration capex was down 59% from its peak at \\$1.8/boe in 2024 Exploration capex per bboe per FAS69 data"
  },
  {
    "figure_id": "F081",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Capex reinvestment is being rewarded by the market and has correlated with higher total return in the last 12 months 12-month share price returns in USD"
  },
  {
    "figure_id": "F082",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Longer reserve-life companies have outperformed as the market rewarded resource depth"
  },
  {
    "figure_id": "F083",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "EU Oils vs. US Oils capex intensity and payout, % CFO"
  },
  {
    "figure_id": "F084",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8: IEA's NZE +5 mboed upward revision to 2030 oil demand is comparable in scale to China's oil demand growth over 2000-10 Oil demand (mb/d)"
  },
  {
    "figure_id": "F085",
    "report_id": "R012",
    "label": "Figure 1",
    "context": "Figure 1: Stock Price Performance since US-Iran Conflict"
  },
  {
    "figure_id": "F086",
    "report_id": "R012",
    "label": "Figure 2",
    "context": "Figure 2: YTD China property GFA growth"
  },
  {
    "figure_id": "F087",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "Figure 3: Completion end vs new starts end commodity performance"
  },
  {
    "figure_id": "F088",
    "report_id": "R012",
    "label": "Figure 4",
    "context": "Figure 4: YTD China FAI growth"
  },
  {
    "figure_id": "F089",
    "report_id": "R012",
    "label": "Figure 5",
    "context": "Figure 5: China raw coal production"
  },
  {
    "figure_id": "F090",
    "report_id": "R012",
    "label": "Figure 6",
    "context": "Figure 6: China thermal power generation"
  },
  {
    "figure_id": "F091",
    "report_id": "R012",
    "label": "Figure 7",
    "context": "Figure 7: QHD 5,500Kcal Thermal Coal Spot Price"
  },
  {
    "figure_id": "F092",
    "report_id": "R012",
    "label": "Figure 8",
    "context": "Figure 8: China vs Seaborne 6,000Kcal Coking Coal Price"
  },
  {
    "figure_id": "F093",
    "report_id": "R012",
    "label": "Figure 9",
    "context": "Figure 9: China YTD Crude Steel Production"
  },
  {
    "figure_id": "F094",
    "report_id": "R012",
    "label": "Figure 10",
    "context": "Figure 10: CISA Key Members Daily Average Crude Steel Output"
  },
  {
    "figure_id": "F095",
    "report_id": "R012",
    "label": "Figure 11",
    "context": "Figure 11: Daily Average Molten Iron Output mn tons/day"
  },
  {
    "figure_id": "F096",
    "report_id": "R012",
    "label": "Figure 12",
    "context": "Figure 12: CISA Key Member Daily Average Pig Iron Output"
  },
  {
    "figure_id": "F097",
    "report_id": "R012",
    "label": "Figure 13",
    "context": "Figure 13: China steel mills operating ratio and profitability"
  },
  {
    "figure_id": "F098",
    "report_id": "R012",
    "label": "Figure 14",
    "context": "Figure 14: China Steel Products Export Volume"
  },
  {
    "figure_id": "F099",
    "report_id": "R012",
    "label": "Figure 15",
    "context": "Figure 15: China monthly aluminum production"
  },
  {
    "figure_id": "F100",
    "report_id": "R012",
    "label": "Figure 16",
    "context": "Figure 16: China aluminum social inventory"
  },
  {
    "figure_id": "F101",
    "report_id": "R013",
    "label": "Figure 1",
    "context": "Figure 1: Shipment value of semiconductors and SPE (YoY)"
  },
  {
    "figure_id": "F102",
    "report_id": "R013",
    "label": "Figure 2",
    "context": "Figure 2: SPE shipment trend by region"
  },
  {
    "figure_id": "F103",
    "report_id": "R013",
    "label": "Figure 3",
    "context": "Figure 3: Global SPE shipment trend excluding China"
  },
  {
    "figure_id": "F104",
    "report_id": "R013",
    "label": "Figure 4",
    "context": "Figure 4: Tokyo Electron SPE sales"
  },
  {
    "figure_id": "F105",
    "report_id": "R013",
    "label": "Figure 5",
    "context": "Figure 5: SCREEN HD SPE sales"
  },
  {
    "figure_id": "F106",
    "report_id": "R013",
    "label": "Figure 6",
    "context": "Figure 6: KOKUSAI Electric equipment sales"
  },
  {
    "figure_id": "F107",
    "report_id": "R013",
    "label": "Figure 7",
    "context": "Figure 7: Ulvac semiconductor & electronic device production equipment sales"
  },
  {
    "figure_id": "F108",
    "report_id": "R013",
    "label": "Figure 8",
    "context": "Figure 8: Disco precision processing equipment shipments"
  },
  {
    "figure_id": "F109",
    "report_id": "R013",
    "label": "Figure 9",
    "context": "Figure 9: Advantest test system sales"
  },
  {
    "figure_id": "F110",
    "report_id": "R013",
    "label": "Figure 10",
    "context": "Figure 10: Discretes global net billings"
  },
  {
    "figure_id": "F111",
    "report_id": "R013",
    "label": "Figure 12",
    "context": "Figure 12: Optoelectronics global net billings"
  },
  {
    "figure_id": "F112",
    "report_id": "R013",
    "label": "Figure 14",
    "context": "Figure 14: Analog global net billings"
  },
  {
    "figure_id": "F113",
    "report_id": "R013",
    "label": "Figure 16",
    "context": "Figure 16: MOS DRAM global net billings"
  },
  {
    "figure_id": "F114",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "Figure 11: IGBT (Insulated Gate Bipolar Trans) global net billings Note: Line graph shows YoY. Figure 13: Sensors & Actuators global net billings"
  },
  {
    "figure_id": "F115",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "Figure 11: IGBT (Insulated Gate Bipolar Trans) global net billings Note: Line graph shows YoY. Figure 13: Sensors & Actuators global net billings"
  },
  {
    "figure_id": "F116",
    "report_id": "R013",
    "label": "Figure 15",
    "context": "Figure 15: Logic global net billings Note: Line graph shows YoY. Figure 17: NAND Flash Memory global net billings"
  },
  {
    "figure_id": "F117",
    "report_id": "R013",
    "label": "Figure 15",
    "context": "Figure 15: Logic global net billings Note: Line graph shows YoY. Figure 17: NAND Flash Memory global net billings"
  },
  {
    "figure_id": "F118",
    "report_id": "R013",
    "label": "Figure 22",
    "context": "Figure 22: Semiconductor shipments, SPE shipments, and SPE ratio trend Figure 23: DRAM spot price trend"
  },
  {
    "figure_id": "F119",
    "report_id": "R013",
    "label": "Figure 24",
    "context": "Figure 24: NAND spot price trend"
  },
  {
    "figure_id": "F120",
    "report_id": "R013",
    "label": "Figure 25",
    "context": "Figure 25: DRAM quarterly growth rate (YoY)"
  },
  {
    "figure_id": "F121",
    "report_id": "R013",
    "label": "Figure 27",
    "context": "Figure 27: DRAM (8GB): Quarterly forecasts Note: JPM Global Memory Model. Figure 28: NAND quarterly growth rate (YoY)"
  },
  {
    "figure_id": "F122",
    "report_id": "R013",
    "label": "Figure 35",
    "context": "Figure 35: End products: Market assumptions Note: Apple as of May 1, 2026, Smartphone as of March 9, 2026, PC/Server as of January 12, 2026, Automotive as of June 3, 2026. Figure 36: PC shipments by region"
  },
  {
    "figure_id": "F123",
    "report_id": "R013",
    "label": "Figure 37",
    "context": "Figure 37: Server shipments by region"
  },
  {
    "figure_id": "F124",
    "report_id": "R013",
    "label": "Figure 38",
    "context": "Figure 38: Smartphone volume trend by region Note: JPM smartphone model. Figure 39: Smartphone shipment volume by region (2024, volume)"
  },
  {
    "figure_id": "F125",
    "report_id": "R013",
    "label": "Figure 40",
    "context": "Figure 40: Smartphone market value mix by region (2024, value)"
  },
  {
    "figure_id": "F126",
    "report_id": "R013",
    "label": "Figure 41",
    "context": "Figure 41: iPhone forecasts Note: Apple's fiscal year ends in September, fiscal year basis. Figure 42: 8CSP (top 8 cloud service providers) capex forecasts"
  },
  {
    "figure_id": "F127",
    "report_id": "R013",
    "label": "Figure 45",
    "context": "Figure 45: 8CSP (top 8 cloud service providers) capex breakdown"
  },
  {
    "figure_id": "F128",
    "report_id": "R013",
    "label": "Figure 46",
    "context": "Figure 46: Inventory trend (TSMC)"
  },
  {
    "figure_id": "F129",
    "report_id": "R013",
    "label": "Figure 47",
    "context": "Figure 47: Inventory trend (Intel)"
  },
  {
    "figure_id": "F130",
    "report_id": "R013",
    "label": "Figure 48",
    "context": "Figure 48: Inventory trend (Samsung Electronics)"
  },
  {
    "figure_id": "F131",
    "report_id": "R013",
    "label": "Figure 49",
    "context": "Figure 49: Inventory trend (SK Hynix, Micron) (KRWb; SK Hynix USDm; Micron)"
  },
  {
    "figure_id": "F132",
    "report_id": "R013",
    "label": "Figure 50",
    "context": "Figure 50: Inventory trend (Broadcom, MediaTek)"
  },
  {
    "figure_id": "F133",
    "report_id": "R013",
    "label": "Figure 51",
    "context": "Figure 51: Inventory trend (Infineon, Renesas Electronics)"
  },
  {
    "figure_id": "F134",
    "report_id": "R013",
    "label": "Figure 52",
    "context": "Figure 52: Inventory trend (Texas Instruments, STMicroelectronics)"
  },
  {
    "figure_id": "F135",
    "report_id": "R013",
    "label": "Figure 54",
    "context": "Figure 54: Inventory trend (Lam Research, AMAT, TEL)"
  },
  {
    "figure_id": "F136",
    "report_id": "R013",
    "label": "Figure 53",
    "context": "Figure 53: Inventory trend (Sony Group Semi business)"
  },
  {
    "figure_id": "F137",
    "report_id": "R013",
    "label": "Figure 55",
    "context": "Figure 55: Inventory trend (Advantest, Disco, SCREEN HD, HOYA, Ulvac) Figure 56: DRAM wafer capacity (300mm) Note: JPM Global Memory Model."
  },
  {
    "figure_id": "F138",
    "report_id": "R013",
    "label": "Figure 62",
    "context": "Figure 62: SPE shipment trends Note: Preliminary figures for April 2026. Figure 63: Wafer and mask fabrication (before the front-end process) SPE and material makers"
  },
  {
    "figure_id": "F139",
    "report_id": "R013",
    "label": "Figure 64",
    "context": "Figure 64: Front-end process SPE and material makers"
  },
  {
    "figure_id": "F140",
    "report_id": "R013",
    "label": "Figure 65",
    "context": "Figure 65: Back-end process SPE, material makers and inspection equipment makers"
  },
  {
    "figure_id": "F141",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Retail sales YoY weakened due to a high base and a softening job market"
  },
  {
    "figure_id": "F142",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Firm pace of resolving hidden debt after a relatively slow start"
  },
  {
    "figure_id": "F143",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Policy bank bond issuance has seen a net contraction YTD"
  },
  {
    "figure_id": "F144",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Consumer confidence has dipped again after a period of modest improvement"
  },
  {
    "figure_id": "F145",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Domestic flight weakened from 2Q amid the energy shock"
  },
  {
    "figure_id": "F146",
    "report_id": "R015",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Domestic petroleum retail volume slumped"
  },
  {
    "figure_id": "F147",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Electricity generation remains robust"
  },
  {
    "figure_id": "F148",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China's key EV brands – market share YTD 26 vs FY25 EV market share in China"
  },
  {
    "figure_id": "F149",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Total discrete revenue yoy growth turned positive since 4Q25"
  },
  {
    "figure_id": "F150",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Auto and industrial accounted for 70% of end demand in discrete semiconductors (2025)"
  },
  {
    "figure_id": "F151",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: China EV wholesale growth is turning incrementally positive"
  },
  {
    "figure_id": "F152",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Industrial automation companies' revenue grew robustly at 21% YoY in 1Q26"
  },
  {
    "figure_id": "F153",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Global leading power semi companies' capex declined for 2 years"
  },
  {
    "figure_id": "F154",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Capacity additions likely to slow in 2026-28 (kwpm - 12\" equiv)"
  },
  {
    "figure_id": "F155",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: MOSFET: Prices up 1% Y/Y in Apr 2026"
  },
  {
    "figure_id": "F156",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8: MOSFET: Shipments up 23% Y/Y in Apr 2026"
  },
  {
    "figure_id": "F157",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "Exhibit 9: IGBT: Prices up 1% Y/Y in Apr 2026"
  },
  {
    "figure_id": "F158",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: IGBT: Shipments increased 17% Y/Y in Apr 2026"
  },
  {
    "figure_id": "F159",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "(Rmb, mn) Note: There are not sufficient brokers supplying consensus data for this metric ♦ MS Estimates"
  },
  {
    "figure_id": "F160",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Weekly steel demand"
  },
  {
    "figure_id": "F161",
    "report_id": "R024",
    "label": "FIGURE 1",
    "context": "BCI, US expect DD growth in the cloud vertical in CY26-CY27, as AI-related cloud build-outs broaden and continue to accelerate. FIGURE 1. Optical Market Expected to Enjoy DD Growth Trends, Driven by Telco Recovery and AI"
  },
  {
    "figure_id": "F162",
    "report_id": "R024",
    "label": "FIGURE 2",
    "context": "- We currently do not forecast meaningful coherent Optical inside the data center in CY26 (potentially could see 2H26), and believe that to be more of a CY27+ opportunity. - We continue to expect the total Optical market to have a LSD CAGR from CY22-27, taking"
  },
  {
    "figure_id": "F163",
    "report_id": "R024",
    "label": "FIGURE 3",
    "context": "- We expect Sub to see +DD recovery in CY27 (on easy comps), after multiple down years through CY26. Sub is MSD-HSD% of the total market. FIGURE 3. Despite Cloud Growth, Telco Still Majority of the Market"
  },
  {
    "figure_id": "F164",
    "report_id": "R024",
    "label": "FIGURE 5",
    "context": "## From a vendor standpoint: \\- CIEN (OW-rated) is the only company under our coverage in Optical that has been, and that we continue to expect to be, a share gainer – moving from 16% of the market in CY18 to \\~32% in CY27E. We expect CIEN to be a beneficiary "
  },
  {
    "figure_id": "F165",
    "report_id": "R024",
    "label": "FIGURE 6",
    "context": "\\- Within the ZR/ZR+ market, we expect CIEN to maintain its market share in the mid-teens from CY24-27, given its tech advantage (first win in the market for 800G ZR+) offset by the multiple players in the market. CIEN remains on track to more than double its "
  },
  {
    "figure_id": "F166",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Exhibit 2: Both sales and profit growth rates slow slightly Accenture sales growth (LC basis) and operating profits/adjusted operating profits"
  },
  {
    "figure_id": "F167",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Both sales and profit growth rates slow slightly Accenture sales growth (LC basis) and operating profits/adjusted operating profits"
  },
  {
    "figure_id": "F168",
    "report_id": "R025",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Headcount rises slightly qoq Accenture headcount and attrition rate"
  },
  {
    "figure_id": "F169",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Exhibit 4: 3Q order growth turns negative at $-3\\%$ yoy Accenture orders (USD basis)"
  },
  {
    "figure_id": "F170",
    "report_id": "R033",
    "label": "Exhibit 12",
    "context": "Exhibit 1: We Raise our 2027 Price Forecast to \\$2,950 But Our Forecast Stays Well Below the Forwards LME Aluminium Price"
  },
  {
    "figure_id": "F171",
    "report_id": "R033",
    "label": "Exhibit 2",
    "context": "Exhibit 2: We Expect the Global Aluminium Market to Shift into a Smaller Surplus in 2027 Than Previously Forecast on Lower Middle East Supply Global Aluminium Market Balance"
  },
  {
    "figure_id": "F172",
    "report_id": "R033",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We Expect a Larger Q3 Deficit Before the Market Returns to Surplus in Q4 Primary Aluminium Market Balance"
  },
  {
    "figure_id": "F173",
    "report_id": "R033",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Aluminium Production Margins Are Approaching the 2022 Highs"
  },
  {
    "figure_id": "F174",
    "report_id": "R033",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Low Inventory Cover Supports Higher Smelter Margins Aluminium Inventories as Days of Consumption"
  },
  {
    "figure_id": "F175",
    "report_id": "R033",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Two Supply Shocks: Middle East Output Falls, Indonesia Supply Catching Up Aluminium Production Share"
  },
  {
    "figure_id": "F176",
    "report_id": "R033",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Expect Indonesia and China Production Growth to Partly Offset Middle East Losses Global Primary Aluminium Production YoY Growth"
  },
  {
    "figure_id": "F177",
    "report_id": "R033",
    "label": "Exhibit 8",
    "context": "Exhibit 8: We Raise Our Indonesian Primary Aluminium Production Forecast to 1.7Mt in 2026 and 2.9Mt in 2027 Indonesia Primary Aluminium Production"
  },
  {
    "figure_id": "F178",
    "report_id": "R033",
    "label": "Exhibit 9",
    "context": "Exhibit 9: We Include Harita Group Smelter from 2027 in Our Base Case Indonesia Primary Aluminium Production, Million Tonnes"
  },
  {
    "figure_id": "F179",
    "report_id": "R033",
    "label": "Exhibit 10",
    "context": "Exhibit 10: High China Smelter Margins Support Further Output Growth China Aluminium Smelter Margin"
  },
  {
    "figure_id": "F180",
    "report_id": "R033",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China Output is Testing the 45Mt Capacity Cap"
  },
  {
    "figure_id": "F181",
    "report_id": "R033",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Risks to our Middle East Supply Recovery Assumption are Two-Sided LME Aluminium Price Scenarios (avg. 2027)"
  }
]