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
  "战略咨询": 1,
  "智库/国际机构": 7
}

报告摘要：
[
  {
    "id": "R001",
    "title": "亚洲开发银行：马尔代夫最缺的不是旅游，是财政可持续",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：马尔代夫最缺的不是旅游，是财政可持续\n\n亚洲开发银行最新发布的马尔代夫国别简报，表面看是一份常规的发展合作数据汇总。但仔细拆解其中几个关键数字，它揭示了一个比旅游收入波动更深层的结构性问题：马尔代夫正处于从“小而美”到“小而脆”的转折点。报告最值得关注的判断是——这个岛国的发展瓶颈已经从地理限制转向制度能力。\n\n截至2025年底，亚开行在马尔代夫累计承诺公共部门贷款、赠款和技术援助5.56亿美元，私营部门累计承诺5083万美元。2025年全年新批准项目仅一笔技术援助，金额202万美元。这个数字本身不惊人，但结合另一组数据看就有意思了：亚开行在马尔代夫的独立评价显示，2016年至2025年间被评估的3个公共部门项目中，1个被评为“低于成功”，成功率并非100%。\n\n> **KC评论：** 亚开行在马尔代夫的业务规模很小，但项目成功率不是满分这一点值得注意。对于一个高度依赖外部援助的小岛国，每一笔资金的使用效率都直接影响其财政空间。完整报告里的独立评价章节值得细看，它列出了具体哪些项目被判定为“低于成功”，以及背后的原因。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是政府能否把有限的人力资源转化为执行能力\n\n报告在“运营挑战”部分点出了一个常被忽视的硬约束：有限的人力资源池限制了马尔代夫设计和实施复杂项目的能力。这不是客套话。马尔代夫全国人口仅约50万，公务员体系的技术深度和广度天然受限。亚开行的应对措施是提供技术援助来加强政府机构能力——但技术援助本身也需要本地团队承接。\n\n2025年亚开行批准的技术援助项目聚焦于海关现代化，同时还有多个区域性技术援助项目涉及审计机构强化、贸易和运输便利化。这些项目看似分散，实则指向同一个核心：帮助马尔代夫用更少的人做更复杂的事。\n\n![研报图表 2\n\n[... middle omitted ...]\n\n最多（35个），累计承诺金额1.31亿美元，仅次于能源和水利。这意味着亚开行在过去几十年里一直在帮助马尔代夫维持政府运转，而不是推动宏观环境结构转型。真正的考验在于，当外部援助从“补运营”转向“促转型”时，马尔代夫能否自己接住。\n\n这份亚开行国别简报的数据颗粒度很细，包括各行业累计承诺额、承包商和咨询商排名、联合融资结构等。完整报告、中文摘要和图表合集，适合放在当天国际发展合作的主线里继续跟踪，也方便后续对比其他小岛国的亚开行合作模式。\n\n[note.md]\n马尔代夫悄悄在做的基建升级\n\n📍 马尔代夫\n不只是度假天堂\n\n亚开行最新国别数据解读\n\n最近翻到一份亚开行关于马尔代夫的国别简报，信息量不小。这个以旅游和渔业闻名的小岛国，其实正在经历一波扎实的基建和产业升级。\n\n几个值得关注的动向：\n\n1️⃣ 能源转型是重点\n亚开行在马尔代夫累计承诺了1.36亿美元用于能源项目，是所有领域中投入最高的。核心动作是升级电网、引入更多太阳能。这是从依赖进口柴油转向清洁电力的关键一步。\n\n2️⃣ 水与城市基建投入大\n累计投入1.25亿美元，仅次于能源。重点是防洪、海岸保护、垃圾处理（包括垃圾发电）。对岛国来说，应对气候变化和提升环境韧性是刚需。\n\n3️⃣ 公共部门管理是最大领域\n项目数量最多（35个），累计1.31亿美元。说明亚开行在帮政府提升财政可持续性和行政效率，这是长期发展的基础。\n\n4️⃣ 私营部门参与度有限\n私人领域累计承诺仅5083万美元，主要集中在金融和IT。报告指出，马尔代夫市场小、营商环境弱、融资渠道有限，私营投资机会受限。\n\n5️⃣ 知识输出也很有意思\n2025年亚开行做了几项研究：用机器学习绘制贫困地图、分析女性就业的社会障碍、推动金枪鱼产业链可持续融资。这\n\n[... middle omitted ...]\n\nnvestee company and ADB. It comprises the amount indicated in the investment agreement, which—depending on the exchange rate at the time of signing—may or may not be equal to the approved amou\n\n[... middle omitted ...]\n\nian Development Blog https://blogs.adb.org/\n\nNotes: (i) Figures are estimated by ADB unless otherwise stated. \"\\$\" refers to United States dollars. (ii) Data are updated as of 31 December 2025 unless otherwise indicated."
  },
  {
    "id": "R002",
    "title": "亚洲开发银行：蒙古数字宏观环境仅占GDP1.6%，统计方法才是真正突破",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：蒙古数字宏观环境仅占GDP1.6%，统计方法才是真正突破\n\n蒙古的数字宏观环境到底有多大？亚洲开发银行（ADB）最新发布的实验性统计报告给出了一个看似保守的答案：2015至2019年间，数字宏观环境仅占蒙古GDP的1.5%至1.8%。但这个数字的意义不在于它有多高，而在于它是如何被算出来的。\n\n这份报告不是一份简单的宏观环境数据简报，而是ADB与蒙古国家统计办公室联合推进的一项统计基础设施工程。它首次将OECD的“数字供给使用表”（DSUT）框架应用于蒙古宏观环境，试图在传统统计体系中为数字活动建立独立的测量通道。对于关注新兴市场数字化进程的观察者来说，这份报告的价值不在结论，而在方法论本身。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 蒙古数字宏观环境的真实规模可能比数据显示的更大\n\n报告给出的1.6%均值，在跨国比较中并不突出。ADB用投入产出框架测算的其他地区数据为：新加坡6.5%-6.8%、马来西亚7.6%-8.7%、澳大利亚5.0%-5.3%，而蒙古的邻国哈萨克斯坦和格鲁吉亚也分别达到2.4%和2.5%。\n\n但这里有两个必须注意的技术性原因，可能导致蒙古的数字宏观环境被系统性低估。\n\n第一，当前的DSUT只覆盖了七类数字产业中的第一类——“数字使能产业”，即ICT硬件制造、软件出版、电信、IT服务等。其余六类，包括数字中介平台、电商、纯数字运营商等，因数据不足尚未纳入。这意味着蒙古正在快速增长的电商和数字服务交易几乎没有被计入。\n\n第二，报告使用的是现价数据，没有做通胀调整。而数字产品和服务的价格通常随时间下降——手机资费下降、硬件成本降低——这会导致现价口径下的实际增长被低估。\n\n> **KC评论：** 1.6%这个数字本身不重要，重要的是它只覆盖了“数字化的供给端”，而“数字化的交易端”\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n蒙古数字经济，1.6%只是开始\n\n**封面短标题：** 蒙古数字账本\n**封面副标题：** 研报拆解：数字产业如何被丈量\n\n---\n\n最近翻到一份亚开行关于蒙古数字经济的研报，挺有意思。2015-2019年，蒙古的数字经济平均贡献了1.6%的GDP。乍一看不高，但背后藏着不少门道。\n\n**1. 怎么算出来的？**\n研报用了两套方法交叉验证。一套是“数字供给使用表”，从产业、产品、交易三个维度拆解。另一套是投入产出法，算直接和间接的附加值贡献。两套数据互相印证，比单一算法靠谱。\n\n**2. 数字产业长什么样？**\n2015-2019年，蒙古的数字GDP绝对值在增长，但占比从1.77%微降到1.58%。别被这个数字骗了——同期整体经济（尤其资源型产业）扩张更快，分母变大了。而且数字产品价格逐年下降，用现价算会低估实际增长。\n\n**3. 谁在扛大旗？**\n电信行业是绝对主力，一直占数字GDP大头。但增长最快的是“计算机编程、咨询及相关服务”，2018年后加速明显。换句话说，蒙古的数字经济正在从“铺网络”转向“用网络”。\n\n**4. 跟邻居比呢？**\n用同样方法算，蒙古的数字经济占比（1.6%）低于哈萨克斯坦（2.4\n\n[... middle omitted ...]\n\n estimates, the analysis also applies the Asian Development Bank's input-output-based value flow methodology. Estimates derived from the two approaches highlight the growing importance of digi\n\n[... middle omitted ...]\n\nnse (CC BY 3.0 IGO)\n\n© 2026 ADB. The CC license does not apply to non-ADB copyright materials in this publication.\nhttps://www.adb.org/terms-use#openaccess http://www.adb.org/publications/corrigenda pubsmarketing@adb.org"
  },
  {
    "id": "R003",
    "title": "国际清算银行：共识机制不是技术选择，而是宏观环境均衡的结果",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "国际清算银行",
    "digest": "[wechat_article.md]\n# 国际清算银行：共识机制不是技术选择，而是宏观环境均衡的结果\n\n多数人谈论区块链时，关注的是比特币、以太坊、Solana谁会成为“赢家”。但国际清算银行这份最新研报给出了一个更冷静的判断：**区块链不会收敛于一个统一的基础设施，而是会持续碎片化。**\n\n这并不是技术缺陷，而是宏观环境学的必然结果。共识机制的设计本质上是“代币激励下的均衡”——不同的奖励结构、验证者参与成本和协调方式，会天然产生不同的均衡点。这些均衡点无法同时满足去中心化、安全性和可扩展性三个维度，于是就有了今天我们看到的多条Layer 1链并存、Layer 2解决方案不断涌现的局面。\n\n碎片化不是暂时的混乱，而是系统的结构性特征。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 共识机制不是技术选择，而是宏观环境均衡\n\n报告最核心的洞察是：共识机制不是纯粹的技术架构问题，而是一个宏观环境激励设计问题。\n\n以比特币的工作量证明和以太坊的权益证明为例，它们都追求广泛的验证者参与，这支撑了去中心化和安全性，但代价是吞吐量受限、延迟高。当用户需求上升，交易费用飙升，价格敏感的用户就被挤出。这是“区块链三难困境”的真实体现。\n\n而Solana的时间排序加拜占庭容错、Avalanche的概率采样、Tron的委托权益证明，则走的是另一条路：通过缩小验证者规模或提高硬件门槛来换取高吞吐量和低延迟。代价是去中心化程度下降。\n\n报告明确指出：**这些设计反映的是不同的宏观环境均衡，而非纯技术约束。** 当一条链上锁定的资产价值上升，攻击成本也必须上升，而成本最终由用户通过费用和代币稀释来承担。这意味着，不存在一个“最优”共识机制——只有最适合特定用户群体的设计。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 碎片化被Layer 2加剧，\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n区块链共识机制：为什么没有一条链统治所有？\n\n**封面标题：** 链的“不可能三角”\n**副标题：** 一文看懂区块链为何越分越散\n\n---\n\n**1. 链的“个性”从共识机制就定了**\n\n所有公开区块链都在解决同一个问题：如何让互不信任的陌生人一起记账，且不造假。\n\n答案是用token奖励+惩罚来激励诚实行为。但不同链对“谁来记账、怎么奖励、成本多高”的设定完全不同，这就形成了不同的**经济均衡**。\n\n比如：\n- **比特币（PoW）**：靠算力竞争，去中心化强、安全性高，但速度慢、能耗大。\n- **以太坊（PoS）**：靠质押token选验证者，效率更高，但仍有协调成本。\n- **Solana**：用时间戳+快速投票，吞吐量高，但对硬件要求高，验证者门槛也高。\n- **Tron/BNB Chain**：只让少数验证者打包，速度快但权力集中。\n\n没有一条链能同时做到“去中心化+安全+可扩展”——这就是著名的**区块链不可能三角**。\n\n---\n\n**2. 链越来越多，流动性越来越散**\n\n因为不同用户需求不同（有人要安全，有人要便宜，有人要快），大量L1公链并存。加上L2（如Arbitrum、Optimi\n\n[... middle omitted ...]\n\nan Doerr, Pablo Hernández de Cos, Hyun Song Shin and Leanne Zhang for helpful comments and suggestions, and Nicola Faessler for administrative support.\n\nThe editors of the BIS Bulletin series \n\n[... middle omitted ...]\n\n021/04/07/sharding.html.\n\nSaleh, F (2021): \"Blockchain without waste: proof-of-stake\", Review of Financial Studies, vol 34, no 3.\n\nShin, H S (2026): \"Tokenomics and blockchain fragmentation\", BIS Working Papers, no 1335."
  },
  {
    "id": "R004",
    "title": "IMF：马里宏观环境修复，不是安全改善，而是矿业意外财",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：马里宏观环境修复，不是安全改善，而是矿业意外财\n\n马里正在经历一次不寻常的修复周期。国际货币产品组织（IMF）在2026年3月完成的对马里员工监督规划第二次审查报告中，给出了一个清晰但不太被外部注意的判断：这个西非国家在经历了2025年下半年严重的恐怖袭击冲击后，增长正在回正，但真正决定中期走向的，不是安全形势的边际改善，而是黄金和锂矿带来的意外财政空间能否被有效管理。\n\n这份报告不是一份普通的国别评估。它标志着马里完成了为期一年的员工监督规划，为未来争取更高层级的中期信贷安排铺平了道路。而报告中最值得关注的信号，藏在对“矿业收入管理”的政策讨论里。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 安全冲击后的宏观环境韧性比预期更强\n\n2025年对马里而言是典型的“前高后低”年份。上半年宏观环境动能强劲，前三季度实际GDP同比增长达到5.7%，高于2024年全年的4.3%。农业在良好收成支撑下扩张8.3%，锂矿生产也带动第二产业从负增长转正。\n\n但第四季度形势急转直下。恐怖袭击切断了关键运输路线和燃料供应，导致制造业和服务业活动明显调整。全年增长率被拉低至4.9%，低于前三季度的表现。\n\n关键在于，IMF认为这种冲击是暂时性的。随着安全局势逐步好转、金矿争端解决，2026年增长预计回升至5.5%左右，中期稳定在5.5%的潜在增速附近。这个判断基于一个核心假设：燃料供应能够恢复、金矿生产正常化、商业环境改善。\n\n> **KC评论：** 5.5%的中期增长预期对于马里而言不算激进，但也不保守。它取决于安全局势能否持续改善，以及区域融资成本是否回落。完整报告中的不确定性矩阵和情景分析值得细看。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 黄金矿争端的解决才是真正的结构性拐点\n\n[... middle omitted ...]\n\n溢出效应。马里是西非萨赫勒地区安全扰动的一部分。邻国尼日尔、布基纳法索的局势如何影响马里的贸易通道、难民负担和区域融资环境，报告没有展开。\n\n这些未解问题并不削弱报告的价值，但它们决定了马里的修复路径究竟是“V型反弹”还是“L型底部震荡”。对于关注非洲宏观环境的读者，这份报告的完整版本——包括不确定性矩阵、量化目标框架和结构性改革时间表——值得从原文中进一步提取。\n\n完整报告、中文摘要、KC评论和图表合集，可以放在当天国际主线里继续看。\n\n[note.md]\n马里经济正在回暖，IMF刚批了最后一笔监控贷款\n\n封面标题：马里复苏进行时\n封面副标题：金矿复产+安全改善，2026年加速\n\n正文：\n马里经济正在从2025下半年的冲击中反弹。IMF刚批准了第二期也是最后一期员工监督计划（SMP）的审核，说明政策执行得到了认可。\n\n几个关键点值得关注：\n\n1️⃣ 经济增速回升\n2025年前三季度GDP增长5.7%，比2024年的4.3%有明显提速。农业表现亮眼，增长8.3%，但四季度受燃料短缺和安全问题拖累，全年预计回落到4.9%。2026年有望回到5.5%左右。\n\n2️⃣ 金矿纠纷解决是最大利好\n马里最大金矿的争端在2025年11月正式解决，矿权已按2023年新矿业法续签10年。2026年黄金产量恢复，叠加金价处于历史高位，将直接拉动出口、财政收入和银行流动性。\n\n3️⃣ 财政纪律没放松\n2026年预算将赤字控制在西非经货联盟3%的GDP上限内。重点方向：扩大税基、加强税收管理、控制经常性支出。金价和锂价上涨带来的额外收入，需要用非矿业财政锚来引导，避免顺周期花钱。\n\n4️⃣ 安全与外部风险仍在\n2025下半年恐怖袭击导致燃料运输中断、电力短缺，2300所学校停课。虽然安全形势\n\n[... middle omitted ...]\n\nf these discussions, the staff report was completed on March 18, 2026.\n\nThe IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the au\n\n[... middle omitted ...]\n\nvel of debt owed to suppliers</td><td>Quarterly</td><td>End of month + 4 weeks</td></tr><tr><td colspan=\"4\">Note: Preliminary national accounts data will be shared with IMF staff at the time of reviews.</td></tr></table>"
  },
  {
    "id": "R005",
    "title": "经合组织：不是缺钱是缺数据，经合组织为政府培训支出开方",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：不是缺钱是缺数据，经合组织为政府培训支出开方\n\n全球各国政府在教育和培训上的公共支出逐年攀升，但一个尴尬的事实是：很少有政府能清楚回答，这些钱到底投到了哪些项目上，以及这些项目是否真正提升了就业率和收入水平。经合组织（OECD）最新发布的一份政策报告直指核心障碍——问题不在于资金总量，而在于决策所依赖的数据系统严重滞后。\n\n这份报告提出的判断值得产业决策者和政策研究者关注：当前技能研究领域最大的瓶颈，不是财政约束，而是信息基础设施的缺失。政府往往拥有大量分散的数据，却无法将其整合成一张可指导资源配置的完整图景。报告因此提出了一套分析框架，将阻碍数据整合的障碍归纳为四类：制度与治理障碍、人力与分析能力缺口、法律与监管约束、以及技术与互操作性问题。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 碎片化的数据系统，让每一分钱都难以追踪\n\n报告指出，技能体系天然跨越多部门、多层级政府——从教育部、劳动部到地方培训机构，再到雇主和社会伙伴。这种复杂性使得数据天然分散。一个典型场景是：教育部门掌握学生入学和毕业数据，劳动部门掌握就业和收入数据，财政部门掌握预算拨付数据，但三者之间几乎没有纵向链接。\n\n后果是直接的。政府无法追踪一个培训项目的参与者，在完成培训后是否真的找到了工作、收入是否提升、以及这些结果与投入的资金之间是否存在正相关。报告特别强调，缺乏这种链接机制，不仅导致低效支出难以被发现，也让高回报项目无法获得应有的资源倾斜。这并非技术难题，而是制度设计问题。\n\n> **KC评论：** 报告的核心洞察在于，技能研究领域的“数据问题”本质上是“治理问题”。许多国家并不缺数据，缺的是让数据流动和对话的制度安排。对于关注公共财政效率的读者，这份报告提供了一个清晰的诊断框架：先问数据是否打通，再谈资金是否到位。\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n技能数据，正在改变教育投资逻辑\n\n📊 教育投资，数据说了算\n\n为什么政府每年花那么多钱在教育上，却很难说清楚“钱花得值不值”？\n\n这份OECD研报的核心观点：不是缺钱，是缺好数据。\n\n1️⃣ 数据碎片化是最大痛点\n教育数据分散在多个部门：教育部、劳工部、财政部……各自为政，无法串联。\n结果就是：不知道哪个培训项目真正提高了就业率，哪笔钱打了水漂。\n\n2️⃣ 打通数据后，能回答三个关键问题\n- 哪些教育路径能带来稳定就业？\n- 哪个地区、哪个行业的技能培训回报最高？\n- 不同人群（尤其是弱势群体）的参与度和效果如何？\n\n3️⃣ 不是要收集更多数据，而是用好已有数据\n很多国家其实已有大量数据，但存在几个障碍：\n- 机构壁垒：部门间不愿共享\n- 人才短板：缺少懂数据分析的专家\n- 法律约束：隐私保护与数据使用难平衡\n- 技术问题：系统不兼容，标准不统一\n\n4️⃣ 数字技术（包括AI）是放大器\n但前提是：数据质量高、治理机制好。否则AI也只是“垃圾进垃圾出”。\n\n研报还提到一个有意思的点：雇主和个人的培训投入往往比政府更灵活、反应更快。公共数据应该去补充、而不是替代这些私人投入。\n\n所以，未来教育投资的方向，不是“多\n\n[... middle omitted ...]\n\ns: © Andrey\\_Popov/Shutterstock.com.\n\n© OECD 2026\n\n![](images/51b5c8cf7f7b387231017e76454da72ef87159db945572a7d392b1097f5e959e.jpg)\n\n## Attribution 4.0 International (CC BY 4.0)\n\nThis work is \n\n[... middle omitted ...]\n\nges. By analysing these barriers and highlighting promising country practices, the paper provides a basis for identifying priorities and guiding reforms to strengthen skills data systems and improve investment in skills."
  },
  {
    "id": "R006",
    "title": "经合组织：南非基础教育真正瓶颈不是入学率，而是评估体系",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：南非基础教育真正瓶颈不是入学率，而是评估体系\n\n过去三十年，南非在普及基础教育上取得了实打实的进展。更多孩子走进了教室，但教室里发生了什么，才是更棘手的问题。经合组织最新发布的政策简报，围绕南非国家学生评估框架的升级，给出了一个核心判断：南非教育质量提升的真正瓶颈，不在于学校数量或入学率，而在于缺乏一套能够精准诊断学习差距、并指导教学改进的评估体系。这份报告的价值，不只是为南非教育部门提供了技术建议，更在于它揭示了一个许多发展中地区都会遇到的共性困境——当规模扩张走到尽头，质量提升需要全新的基础设施。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 评估体系的缺失，正在让教学变成“盲人摸象”\n\n报告引用的数据相当直观。2021年，南非三年级学生中有37%属于“萌芽级”读者，这意味着他们刚刚开始发展基础知识和技能，需要大量指导才能跟上进度。国际测评如TIMSS和PIRLS也印证了这一点。更关键的是，这些低学习成果并非随机分布，而是与学校之间长期存在的结构性不平等高度相关——优质教师和学习资源的分配不均，直接体现在了成绩单上。\n\n> **KC评论：** 37%这个数字意味着什么？在任何一个三年级教室里，大约每三个孩子中就有一个连基本阅读都困难。如果评估体系只能给出一个模糊的平均分，而无法告诉老师“这个孩子到底卡在了哪里”，那教学改进就无从下手。经合组织报告的核心主张，正是要填补这个信息断层。\n\n报告明确指出，南非基础教育部虽然已经意识到评估的重要性，并在2022年起草了国家学生评估框架的概念文件，但这份文件至今未公开发布，且存在明显的信息缺口。比如，文件中详细定义了系统评估（SASE）的特征，却对学校层面的评估和国家考试着墨甚少。没有清晰的框架，就难以形成统一的评估语言，更无法将评估结果与2025-30年战略规划\n\n[... middle omitted ...]\n\n图。\n\n此外，报告建议将诊断评估放在学年或学期初进行，这一设计看似合理，但在资源有限的学校，如何保证诊断结果能迅速转化为差异化教学，仍然是一个巨大的执行挑战。南非学校之间的资源差距如此之大，一个统一的框架能否在不同情境下落地，还需要更细致的试点验证。\n\n---\n\n这份经合组织政策简报的完整版本、中文摘要、图表合集以及KC的详细拆解，会放入每日国际信源汇编。适合快速扫读当天全球主要机构的核心叙事，也方便后续对单一议题做横向比较和深入追问。\n\n[note.md]\n南非学生评估框架，如何更科学？\n\n评估框架升级指南\n\n4个关键建议，让考试真正服务于学习\n\n---\n\n南非花了30年把更多孩子送进学校，但结果并不理想。\n\n三年级37%的学生还处在“刚入门”的阅读水平，需要大量指导才能跟上。国际测评也印证了这一点——留级率和辍学率居高不下。\n\n问题出在哪？评估体系没能真正帮到教学。\n\n某外资投行最新研报给出了4条具体建议：\n\n1️⃣ 把框架升级成“全景地图”\n\n不是简单罗列考试，而是明确每项评估的目的、怎么用结果。尤其要把“普通教育证书”和“国家高级证书”这类关键节点考试纳入进来，让评估和升学路径真正挂钩。\n\n2️⃣ 补上“诊断工具”这块拼图\n\n现在缺的是能帮老师发现学生具体短板的工具。建议开发全国统一的诊断性测评和题库，最好在学期初就做，这样老师才能及时调整教学策略。\n\n3️⃣ 让“系统评估”更精细\n\n现有的系统评估设计不错，但不同年级的评分标准粗细不一。三年级和九年级的数学能力描述差别很大。建议参考国际标准，把评分维度对齐，同时试点数字化考试——能省下将近两年的出报告时间。\n\n4️⃣ 别只盯学生，也要看老师\n\n教师问卷可以更深入：工作量、压力、专业发展、教学实践……这些数\n\n[... middle omitted ...]\n\nendations:\n\n\\- Update the National Student Assessment Framework to include all major assessments and clarify their key characteristics, including their purpose and use of results. Including th\n\n[... middle omitted ...]\n\ner this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one."
  },
  {
    "id": "R007",
    "title": "经合组织：全球最低税落地后，发展中国家的真正挑战才刚开始",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：全球最低税落地后，发展中国家的真正挑战才刚开始\n\n2025年，全球税收治理进入一个微妙节点。经合组织最新发布的《2025年税收合作促进发展进展报告》传递了一个清晰信号：技术援助的需求不仅在增长，而且在质变——从“要不要接轨国际标准”转向“接轨之后如何用好规则”。这份报告覆盖了从BEPS、全球最低税到税收透明度的全链条，但最值得关注的判断只有一个：发展中国家正在从规则接受者变成主动使用者，但这一转变正遭遇能力瓶颈和资金紧缩的双重挤压。\n\n报告开篇即点明一个关键政治信号：在2025年第四届发展筹资国际会议上，各国承诺将国内资源动员的双倍资金投入——这是整个发展合作领域唯一获得此类承诺的领域。但承诺与执行之间，经合组织自己坦承，2025年预算已削减15%，主要靠效率提升来消化。这意味着，未来几年技术援助的供需缺口，大概率会进一步扩大。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 全球最低税正在重塑发展中国家的税制选择空间\n\n全球最低税（GMT）是2025年最密集的技术援助领域。20个国家获得了关于GMT和税收激励的双边支持。报告特别提到，经合组织向各国分享了更新后的宏观环境影响评估，但并未公开具体数字。这里的关键变量是：GMT一旦全面落地，发展中国家过去惯用的税收激励工具——比如免税期、税率减免——将失去部分效力，因为母公司所在国有权征收补足税。\n\n> **KC评论：** 对于在东南亚、非洲设有生产基地的跨国企业来说，GMT带来的不是税率本身的变化，而是激励工具的重新定价。过去十年常见的“零税率园区”模式，在GMT框架下可能变成纯粹的利润转移，而非真实研究吸引力。完整报告中关于Side-by-Side方案的技术细节，值得企业税务团队逐条对照。\n\n报告还指出，2026年1月达成的Side-by-Side协议带来了\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n全球税务合作，2025年最新进展\n\n🌍全球税务新动向\n\n国际税务合作在2025年迎来关键进展。OECD最新报告显示，发展中国家正加速融入全球税务透明体系，技术援助需求从广度转向深度。\n\n1️⃣ 税收透明度成效显著\n- 2024年发展中国家通过离岸税务调查和自愿披露计划，新增40亿欧元收入（2009年以来累计480亿欧元）\n- 发展中国家发出4659份信息请求（同比+43%）\n- 参与自动信息交换的发展中国家，收到5300万个金融账户信息，总值2.7万亿欧元\n\n2️⃣ 全球最低税（GMT）成为焦点\n- 2025年已有20个国家获得GMT双边支持\n- 2026年1月“并行方案”达成后，预计需求将进一步爆发\n- 多国正在评估GMT对税收优惠体系的影响\n\n3️⃣ 技术援助模式升级\n- 税务检查员无国界（TIWB）10周年，累计增收27.2亿美元\n- 2025年启动14个新项目，包括首个GMT试点\n- 培训官员超2.2万人，92%能举例说明培训如何帮助工作\n\n4️⃣ 数字化成为新引擎\n- 54个税务机构加入税务技术倡议（ITTI）\n- 60多个国家500多名官员参与数字化转型工作坊\n- 跨境电商增值税标准在法语非洲国家\n\n[... middle omitted ...]\n\nbility of the OECD Secretariat and do not necessarily reflect the official policies of those governments providing funding. This document, as well as any data and map included herein, are with\n\n[... middle omitted ...]\n\na12e63112.jpg)\n\nctp.contact@oecd.org\n\n![](images/0f98c5e02ec05f209c0b4183cb05794dd5c9d0350167d31b86bfa8bb5d89319d.jpg)\n\n@OECDtax\n\n![](images/c473f7de630c9e148c9491554f1775f564de640f021ac7770e63066cb7d7753e.jpg)\n\nOECD Tax"
  },
  {
    "id": "R008",
    "title": "波士顿咨询：AI在可持续报告中的承诺与现实，多数企业仍陷低效流程",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI在可持续报告中的承诺与现实，多数企业仍陷低效流程\n\n欧洲企业的可持续报告正站在一个关键转折点上。经历了CSRD指令下的首批强制披露周期后，一个清晰的信号已经浮现：多数公司仍在用“合规应付”的方式做报告，而非将其作为战略工具。波士顿咨询（BCG）在2026年7月发布的最新研究指出，即将生效的ESRS Set 2标准将削减约60%至70%的强制数据点，这为那些准备改变的企业提供了一个重新定义报告模式的窗口期。核心判断是：可持续报告的成本与复杂性正在迫使企业做出选择——要么继续深陷低效流程，要么将其转化为一项真正的战略能力。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 合规导向的均衡正在制造高成本与低价值\n\nBCG基于欧洲财务报告咨询组（EFRAG）对900余份2025财年报告的分析，识别出了当前市场的主流实践模式。大多数公司披露了大量实质性议题，但这些议题与公司战略目标、具体指标和激励机制之间的关联往往十分松散。报告显示，许多企业的披露议题超过7个，子议题超过16个，但其中只有不到3个议题配有可量化、有时限的目标，更少被嵌入管理层薪酬体系。这种“宽而浅”的披露模式，直接导致了每份报告的页数动辄超过110页，字符数超过35万，而年度合规成本对于大型企业而言已超过100万欧元。结果就是，报告越来越厚，但决策有用性却在下降。\n\n> **KC评论：** 这里的核心矛盾不是“披露不够”，而是“披露太多但缺乏聚焦”。对读者而言，判断一家公司在可持续议题上是否真正认真，不应只看它报告了多少议题，而应看它把哪些议题与业务战略和考核挂钩。BCG的框架提示了一个更务实的观察角度——报告的长度和议题数量，反而可能是战略模糊的信号。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. AI的承诺\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n欧洲ESRS新规：从合规到战略的跃迁\n\n🌱 研报拆解：ESRS Set 2来了\n\n欧洲可持续报告新规进入转折点。2026年将迎来ESRS Set 2，数据点减少60%-70%，更强调“决策有用性”。\n\n1️⃣ 现状：合规驱动的“过度报告”\n- 首轮CSRD报告普遍覆盖过多议题\n- 多数议题与公司战略脱节\n- 年成本超100万欧元，流程复杂\n\n2️⃣ 问题：企业陷入“合规陷阱”\n- 报告变厚，但决策价值低\n- 目标与激励机制脱钩\n- 信息碎片化，内外部都难读懂\n\n3️⃣ 转机：ESRS Set 2的三大调整\n- 数据点精简60%-70%\n- 强化双重重要性评估\n- 从“完整性”转向“决策有用性”\n\n4️⃣ 解法：战略导向的“智能合规”\n- 用业务战略重新定义重要性议题\n- 把报告从财务部的事变成跨部门协作\n- AI应用需聚焦高价值场景，而不是做实验\n\n5️⃣ 关键动作\n- 重新审视双重重要性，聚焦真正相关议题\n- 设计端到端报告流程，而非零散应对\n- 建立AI+治理+组织能力的执行基础\n\n这不是监管负担，而是构建竞争优势的机会。\n\n#学习笔记\n\n[source_mineru.md]\n![](images/a36\n\n[... middle omitted ...]\n\nplexity and significant cost, while displaying a tendency to overreport. Although the introduction of the European Sustainability Reporting Standards (ESRS) has significantly boosted transpare\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：马尔代夫最缺的不是旅游，是财政可持续｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Size of the Digital Economy of Mongolia, 2015–2019 GDP = gross domestic product, LCU = local currency unit."
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Size of the Digital Economy of Mongolia, 2015–2019 GDP = gross domestic product, LCU = local currency unit. The observed decline in the digital economy's share of GDP should therefore be interpreted with caution. The s"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The observed decline in the digital economy's share of GDP should therefore be interpreted with caution. The strong growth of overall GDP during 2015–2019 mechanically affects the relative weight of the digital economy, as total GDP serves as the denominator i"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Zooming In on Mongolia's Digital Transformation"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Zooming In on Mongolia's Digital Transformation"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：蒙古数字宏观环境仅占GDP1.6%，统计方法才是真正突破｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "国际清算银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "国际清算银行｜国际清算银行：共识机制不是技术选择，而是宏观环境均衡的结果｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F009",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "12. Public debt to GDP is expected to fall in 2026 and ease gradually over the medium term. $^{4}$ The 2025 Article IV debt sustainability analysis (DSA) assessed Mali at moderate risk of external and public debt distress—an assessment that remains valid under"
  },
  {
    "figure_id": "F010",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "arrears have declined substantially for the first time since 2022, suggesting improved control over new arrears accumulation and substantial progress towards their reduction. Mali: Fiscal and Macro-Fiscal Developments Note: lighter shades indicate projections "
  },
  {
    "figure_id": "F011",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Mali: Fiscal and Macro-Fiscal Developments Note: lighter shades indicate projections according to the Debt Sustainability Analysis ... increasing the (risk of) crowding out private sector credit. Claims on Public Sector/ Claims on Private Sector (Percent)"
  },
  {
    "figure_id": "F012",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "31. Fiscal sustainability, governance and PFM reforms, and continued arrears clearance remain key to improving the business climate and restoring investor confidence in the medium term. Staff welcomed the government's commitment to maintain a fiscal deficit be"
  },
  {
    "figure_id": "F013",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Mali: High-Frequency Indicators ... reflecting contractions in the secondary and some of the tertiary sector. Industrial and Services Sector (percent, year-on-year change) Meanwhile, gold production continued to decline in 2025 even though gold marke"
  },
  {
    "figure_id": "F014",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Quarterly Tax Revenues (CFAF billions) Sources: Malian authorities and IMF Staff calculations Credit growth remained in negative territory for much of 2025 while deposit growth turned positive, relative to 2024 ... Credit and Deposit Growth ... as domestic pol"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: Malian authorities and IMF Staff calculations Credit growth remained in negative territory for much of 2025 while deposit growth turned positive, relative to 2024 ... Credit and Deposit Growth ... as domestic policy uncertainty intensified in Q3 2025."
  },
  {
    "figure_id": "F016",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Uncertainty in Mali and the Rest of the World (Percent) ## Figure 2. Mali: Real Sector Developments Mali's real GDP growth is expected to be slightly below the WAEMU average in the medium term, ... Sources: World Economic Outlook; IMF staff calculations. The e"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Gold production fell back in 2025 but will recover from 2026 onwards amid record-high prices. Contributions to Growth: Demand Side Inflation is picking up in 2025 on the back of higher food prices and amidst rising uncertainty. Gold Production and Price (in \\$"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Inflation is picking up in 2025 on the back of higher food prices and amidst rising uncertainty. Gold Production and Price (in \\$/troy ounce and in tons) Consumer Price Inflation and Components (percent, year-on-year change and contributions) ## Figure 3. Mali"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Mali: External Sector Developments The current account balance is expected to turn positive in 2026, reflecting a larger goods trade surplus ... Current Account Balance Gold made up almost 80 percent of total exports in 2025 and is expected to rem"
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Composition of Exports ...while imports are estimated to remain broadly unchanged in 2026 relative to 2024 and 2025. Composition of Imports (percent of GDP) The REER appreciated modestly at the start of 2025 before reversing course in H2, likely the result of "
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "...while imports are estimated to remain broadly unchanged in 2026 relative to 2024 and 2025. Composition of Imports (percent of GDP) The REER appreciated modestly at the start of 2025 before reversing course in H2, likely the result of higher inflation differ"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Composition of Imports (percent of GDP) The REER appreciated modestly at the start of 2025 before reversing course in H2, likely the result of higher inflation differentials with the rest of the world. ## Figure 4. Mali: Fiscal Developments The fiscal deficit "
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The REER appreciated modestly at the start of 2025 before reversing course in H2, likely the result of higher inflation differentials with the rest of the world. ## Figure 4. Mali: Fiscal Developments The fiscal deficit is expected to remain well below the WAE"
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Government Spending (percent of GDP) External budget support has been at or near zero since 2021, .... External Public Grants and Loans (percent of GDP) ... and the authorities have become reliant on expensive domestic financing to fund budget needs. Financing"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "External budget support has been at or near zero since 2021, .... External Public Grants and Loans (percent of GDP) ... and the authorities have become reliant on expensive domestic financing to fund budget needs. Financing ## Figure 5. Mali: Monetary and Fina"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Financing ## Figure 5. Mali: Monetary and Financial Sector Developments Private credit growth was negative in much of 2025, but shows signs of a turnaround by year-end... The BCEAO (regional central bank) reduced the policy rate in July by 25 bps, with interba"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Figure 5. Mali: Monetary and Financial Sector Developments Private credit growth was negative in much of 2025, but shows signs of a turnaround by year-end... The BCEAO (regional central bank) reduced the policy rate in July by 25 bps, with interbank rates f"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：马里宏观环境修复，不是安全改善，而是矿业意外财｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F029",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 1.2. Purpose and scope While closing data gaps has significant potential to strengthen policy decision making, doing so requires overcoming a set of structural, institutional and technical barriers. These challenges are diverse and operate at different leve"
  },
  {
    "figure_id": "F030",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2.6. Granularity: Equity and regional blind spots Insufficient granularity in data can obscure important disparities across population groups and regions. In many countries, data are collected at a highly aggregated level, with limited disaggregation by gen"
  },
  {
    "figure_id": "F031",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Analytical strengths of data sources for education and skills policymaking Note: Each cell indicates how well a data"
  },
  {
    "figure_id": "F032",
    "report_id": "R005",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：不是缺钱是缺数据，经合组织为政府培训支出开方｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F033",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Further enhance the monitoring of teaching practice and teachers' working conditions through the National Student Assessment Framework. The Systemic Evaluation Teacher Questionnaire could be strengthened in several areas, such as the monitoring of teachers'"
  },
  {
    "figure_id": "F034",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Why is South Africa in updating its National Student Assessment Framework? South Africa has expanded access to education over the past three decades. However, low learning outcomes and wide inequalities between schools remain a challenge. Results from the c"
  },
  {
    "figure_id": "F035",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- A strong emphasis on ensuring coherence and balance in the use of assessments – including attention to the overall volume of assessments and duplication, and how potential tensions between the formative and summative functions will be managed. ## Features o"
  },
  {
    "figure_id": "F036",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Recommendation 4: Further enhance the monitoring of teaching practice and teachers' working conditions through the National Student Assessment Framework The National Student Assessment Framework should signal the main surveys that South Africa will use to coll"
  },
  {
    "figure_id": "F037",
    "report_id": "R006",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：南非基础教育真正瓶颈不是入学率，而是评估体系｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F038",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "International collaboration shows strong synergies between the OECD's tax standard-setting work and its offer to support DRM. Over the last 15 years, key reforms – including the introduction of AEOI, the publication of the package of measures to address BEPS ("
  },
  {
    "figure_id": "F039",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "reflected in international tax discussions. As shown in Figure 1, participation in OECD tax instruments and forums has grown steadily since 2009. The influence of developing country priorities is evident in several key outcomes of recent negotiations. Examples"
  },
  {
    "figure_id": "F040",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## The OECD offer is delivered through multiple partnerships. Alongside the TIWB initiative partnership with UNDP, the OECD takes part in the PCT, together with the International Monetary Fund (IMF), the United Nations (UN) and the World Bank Group (WBG) and w"
  },
  {
    "figure_id": "F041",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "pieces of legislation – over 65 in the area of BEPS and transfer pricing in the last five years alone – as well as developing country integration into the tools and standards for international tax collaboration (as shown in Figure 1). Ultimately, these impacts"
  },
  {
    "figure_id": "F042",
    "report_id": "R007",
    "label": "FIGURE 2",
    "figure_type": "source_exhibit",
    "context": "In recent years, the Secretariat's capacity-building work with Caribbean jurisdictions has increasingly evolved from bilateral technical assistance towards a more comprehensive strategy aimed at addressing common issues with regional impact, building on key le"
  },
  {
    "figure_id": "F043",
    "report_id": "R007",
    "label": "FIGURE 3",
    "figure_type": "source_exhibit",
    "context": "In 2025, a record 9 400 officials from 180 jurisdictions, including 13 non-member countries, participated in training on various topics related to tax transparency and administrative co-operation. These sessions were delivered through 55 events, including 37 v"
  },
  {
    "figure_id": "F044",
    "report_id": "R007",
    "label": "FIGURE 3",
    "figure_type": "source_exhibit",
    "context": "\\- For its 1 consecutive year, the Women Leaders in Tax Transparency programme has brought together 26 women from 26 developing countries for a nine-month programme comprising six technical and leadership sessions. Since its launch in 2022, the programme has g"
  },
  {
    "figure_id": "F045",
    "report_id": "R007",
    "label": "FIGURE 3",
    "figure_type": "source_exhibit",
    "context": "18th Global Forum Plenary meeting, 2-4 December 2025, New Delhi, India. FIGURE 3. Train-the-Trainer Programme: Tax officials trained locally by region Number of officials trained through Train-the-Trainer The ISM Network, launched in 2021, brought together 459"
  },
  {
    "figure_id": "F046",
    "report_id": "R007",
    "label": "FIGURE 4",
    "figure_type": "source_exhibit",
    "context": "## Trends in revenue mobilisation The new data collected in 2025 once again highlighted the substantial diversity in tax-to-Gross Domestic Product (GDP) ratios across the globe. In 2023, ratios ranged from 2.9% in Somalia to 44.0% in Denmark. Compared to 2022,"
  },
  {
    "figure_id": "F047",
    "report_id": "R007",
    "label": "FIGURE 5",
    "figure_type": "source_exhibit",
    "context": "## GLOBAL TRAINING NETWORKS ## Global Relations Programme on Taxation (GRP) The GRP continued to deliver extensive multilateral training in 2025, reaching nearly 15 000 officials through a mix of in-person workshops, virtual events, and self-paced tools. It co"
  },
  {
    "figure_id": "F048",
    "report_id": "R007",
    "label": "FIGURE 5",
    "figure_type": "source_exhibit",
    "context": "activities, and achieving significant cost efficiencies by pooling resources and avoiding duplication. The Impact Assessment Survey, completed by 556 participants from 2025 events, confirmed high levels of satisfaction and strong evidence that GRP training is "
  },
  {
    "figure_id": "F049",
    "report_id": "R007",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：全球最低税落地后，发展中国家的真正挑战才刚开始｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F050",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Across the sustainability reporting ecosystem, software providers and advisors increasingly characterize AI as a potential game changer. The promise is compelling: faster data processing, reduced manual effort, improved report quality, and more decision-useful"
  },
  {
    "figure_id": "F051",
    "report_id": "R008",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "As a result, AI in sustainability reporting today contributes less to transformation at scale and more to experimentation at the margins. Realizing its full potential will require a more disciplined focus on high-impact use cases, stronger data foundations, an"
  },
  {
    "figure_id": "F052",
    "report_id": "R008",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：AI在可持续报告中的承诺与现实，多数企业仍陷低效流程｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]