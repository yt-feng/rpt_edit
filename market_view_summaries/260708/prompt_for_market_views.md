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
  "战略咨询": 6,
  "智库/国际机构": 9
}

报告摘要：
[
  {
    "id": "R001",
    "title": "亚洲开发银行：政策不确定性延缓清洁转型，新兴市场如何提升排放韧性",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：政策不确定性延缓清洁转型，新兴市场如何提升排放韧性\n\n政策不确定性不仅仅是研究和增长的敌人。亚洲开发银行最新工作论文给出了一个更具体的结论：在13个新兴市场地区长达33年的数据中，政策不确定性每上升一个标准差，碳排放就会增加0.03%。这个数字看似微小，但它揭示了一个被忽视的传导链条——不确定性不仅让企业推迟研究，还让它们推迟了向清洁技术的转型。\n\n这份报告的价值不在于发现“不确定性需要继续观察”，而在于它系统性地回答了“什么样的地区更容易扛住这种冲击”。答案指向一组清晰的结构性特征：有碳定价机制、资金体系更发达、贸易开放度更高、政治更稳定的地区，对政策不确定性的“排放敏感度”显著更低。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 真正起作用的不是“减碳决心”，而是制度缓冲垫\n\n报告最值得关注的发现，不是不确定性本身推高排放，而是不同地区之间的巨大差异。作者将13个地区按多种维度分组后发现：高收入新兴市场在面对政策不确定性时，碳排放几乎没有明显响应；而低收入新兴市场的排放则显著上升，且持续时间更长。\n\n这个差异的背后是几根“缓冲支柱”。有碳定价机制的地区，在面对不确定性时排放增幅更小。资金发展水平更高的地区也是如此——它们的企业在面对政策模糊期时，更有能力维持清洁能源研究，而不是被迫回到高碳路径。政治稳定性同样是一个关键变量：政局越稳，政策不确定性对排放的冲击越弱。\n\n> **KC评论：** 这里隐含的判断值得反复读：碳定价和资金发展不是“锦上添花”，而是对冲政策不确定性的减震器。对于正在设计碳市场的新兴地区来说，这份报告提供了一个额外论据——碳定价不仅能直接降排放，还能让整个地区在面对政策波动时更有韧性。\n\n---\n\n![研报图表 2](assets/xhs_card_02.png)\n\n#\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n政策不确定，反而让碳排放变高了？\n\n新兴市场排放困局\n\n当政策摇摆，环境先买单\n\n最近读了一份亚开行的研究，发现一个反直觉的结论：经济政策不确定性越高，新兴市场的碳排放反而越明显上升。\n\n研报覆盖了13个新兴经济体，时间跨度是1990到2023年。核心发现很清晰——政策不确定上升1个标准差，碳排放最大会多出0.03%。\n\n背后逻辑其实不难理解：\n\n1️⃣ **“等等看”心态拖慢转型**\n政策摇摆时，企业会推迟投资。尤其清洁能源这种前期投入大、回报周期长的项目，最容易被搁置。结果就是继续用老旧的碳密集型设备，排放自然下不去。\n\n2️⃣ **结构差异决定了谁更受伤**\n研报特别分析了不同经济体的反应差异：\n- 有碳定价机制、金融更发达、贸易更开放、政治更稳定的国家，受政策不确定影响更小\n- 可再生能源占比高、研发投入多的经济体，应对能力也更强\n- 高收入新兴市场受影响弱，低收入国家则更持久、更明显\n\n3️⃣ **气候脆弱性是个矛盾点**\n有意思的是，气候脆弱性低的国家，政策不确定时排放反而升得更快。推测可能是这些国家更有“余量”先发展经济，环境约束没那么紧迫。\n\n这份研究提醒我们：政策稳定本身就是一种环境治理资源\n\n[... middle omitted ...]\n\n the governments they represent.\n\nNuobu Renzhi (renzhinuobu@gmail.com) is an assistant professor and assistant dean at the School of Economics, Capital University of Economics and Business, Be\n\n[... middle omitted ...]\n\nes together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region."
  },
  {
    "id": "R002",
    "title": "IMF：基里巴斯案例，当社保支出增加，教育投入反而减少？",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：基里巴斯案例，当社保支出增加，教育投入反而减少？\n\n基里巴斯在新冠疫情期间大幅扩张社会保障支出，贫困率从21.9%骤降至5.5%，极端贫困几乎被消除。但IMF最新一期国别报告揭示了一个值得深思的问题：当社会保障覆盖率达到接近全民水平时，新增转移支付中的相当比例流向了酒精、烟草和卡瓦酒等不利于人力资本积累的消费。这份由IMF亚太部宏观环境学家Ni Wang执笔的Selected Issues Paper，通过断点回归设计建立了失业救济金与物质消费之间的因果关系，为小岛屿发展中国家的社会保障设计提供了新的分析框架。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 社会保障扩张的“双刃剑”：减贫成效与消费结构偏移\n\n2019至2023年间，基里巴斯的社会保障支出发生了质变。新冠疫情后推出的失业救济金（SFU）覆盖了约95%的人口，加上已经翻倍的老年津贴和新增的残疾人津贴，传统社会援助支出占GDP比重远超OECD国家和太平洋岛国平均水平。报告显示，收入最低的四分之一家庭在此期间的收入增长几乎完全来自社会转移支付，而正式劳动收入基本未变。\n\n问题在于，新增收入并未按预期流向教育、健康等人力资本研究领域。2023/24年度的家庭收支调查数据显示，所有收入组别的家庭都增加了食品和物质消费（酒精、烟草、卡瓦酒）的支出，而教育、健康等类别支出增长有限。这意味着，社会保障扩张在消除货币贫困的同时，可能并未有效提升家庭长期发展能力。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 失业救济金与物质消费：一个被证实的因果关系\n\n报告最具方法论贡献的部分，是使用年龄资格断点作为工具变量，通过控制函数方法建立了失业救济金与物质消费之间的因果关系。由于失业救济金仅面向18-59岁的非正式就业人群，研究者利\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n太平洋小岛国的福利实验：发钱后他们买了什么？\n\n发钱之后\n钱去了哪里\n\n一个偏远岛国，发失业金后贫困率从22%降到5%，但烟酒消费也涨了。\n\n1️⃣ 疫情后福利大扩张\n这个太平洋岛国（基里巴斯）在疫情后大幅增加社保支出，贫困率从21.9%骤降到5.5%，基尼系数从27.8降到24.7。极端贫困几乎消失（0.04%）。\n\n2️⃣ 钱发出去，花在哪了？\n2023年数据显示，失业补贴（每月50澳元/人）覆盖了95%的家庭。但研究发现，这笔钱与教育支出负相关，与烟酒、卡瓦（一种传统饮品）支出正相关。\n\n3️⃣ 穷人和富人的区别\n最穷的1/4家庭拿到失业金后，花在烟酒上的钱比富裕家庭少——每多1澳元失业金，富裕家庭多花34分在烟酒上，穷困家庭只多花25分。\n\n4️⃣ 因果证据\n研究者用年龄门槛（18-60岁才能领失业金）做断点回归，确认失业金确实导致了烟酒支出增加，不是巧合。\n\n5️⃣ 政策启示\n研报建议：优化福利发放方式，考虑将部分现金转移改为实物或定向补贴，减少对烟酒的激励。\n\n一个有趣的问题：当基本生存需求被满足，额外的现金会流向哪里？这不仅仅是经济学问题。\n\n#学习笔记\n\n[source_mineru.md]\n\n[... middle omitted ...]\n\nby Corinne Deléchat\nJuly 2026\n\nIMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information\n\n[... middle omitted ...]\n\nle linear regression in terms of level and a probit model for the extensive margin, do not materially change the results. Neither does redefining the instruments as indicators for the exact number of age-eligible people."
  },
  {
    "id": "R003",
    "title": "IMF：塞拉利昂的紧缩见效了，但真正的考验在2028之前",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：塞拉利昂的紧缩见效了，但真正的考验在2028之前\n\nIMF在2026年6月完成了对塞拉利昂的第三次ECF审查，同时批准了新的RSF安排。这份报告的核心信号是：过去三年的财政货币双紧缩确实稳住了汇率、压低了通胀、恢复了信贷，但储备依然薄弱，债务不确定性高企，而2028年大选前的政治不确定性正在上升。真正的问题不是紧缩是否有效，而是紧缩能否持续到选举结束。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 财政紧缩的成果是真实的，但2026年不确定性正在回流\n\n塞拉利昂的国内基础收支从2022年到2025年改善了7个百分点的GDP，其中税收收入增长了3.5个百分点。这一成绩在非洲低收入国家中并不常见。与此同时，货币政策的收紧帮助稳定了汇率，通胀从2024年底的13.8%降至2025年底的4.3%，私人信贷增速从18%跃升至49%。\n\n但2026年的数据开始出现裂痕。一季度财政收入低于预期10%，主要原因是税收合规率下降。更关键的是，由于中东战争推高燃料成本，政府不得不维持燃油补贴，每升汽油和柴油分别补贴1.1和4.3新利昂。这笔补贴虽然避免了更剧烈的价格波动，但也意味着财政空间正在被压缩。\n\n> **KC评论：** 紧缩的成果是真实的，但报告也暗示了“改革疲劳”的不确定性。读者可以重点关注报告中的“国内基础收支”这一指标——它比整体赤字更能反映政府的自主财政纪律。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 债务可持续性仍是最大约束，RSF提供了一条新路径\n\n报告明确指出，塞拉利昂的债务仍处于“高不确定性”状态。2025年公共债务占非铁矿石GDP的49.3%，预计2026年降至47.3%。但这个下降主要依赖宏观环境增长和财政紧缩，而非债务减免或重组。\n\nRSF安排是这次审查中最\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nIMF批了塞拉利昂2.1亿美元\n\n气候韧性+经济改革\n\n塞拉利昂拿到IMF新融资，总额约2.1亿美元（RSF），同时完成ECF第三次审查，立即拨付3170万美金。核心逻辑：用改革换资金，用气候韧性稳增长。\n\n1️⃣ 宏观成绩单\n- 2025年GDP增长5.0%，通胀从13.8%降到4.3%\n- 财政紧缩见效：国内基础收支改善7个GDP百分点\n- 汇率稳定、私人信贷恢复，但外汇储备只有2个月进口覆盖\n\n2️⃣ 风险不容乐观\n- 中东战争外溢：2026年增长预计降至4.0%，通胀反弹至11.6%\n- 债务仍处高风险，外汇储备薄弱\n- 2028大选前政治紧张，改革疲劳风险上升\n\n3️⃣ RSF三大改革方向\n- 气候敏感型公共投资管理\n- 气候韧性建设（防洪、农业适应）\n- 金融稳定（银行风险监控）\n\n4️⃣ 财政纪律不能松\n- 燃料补贴临时保留但需透明+限额\n- 加强矿业税收征管、海关数字化\n- 继续推进公共财务管理改革\n\n5️⃣ 货币政策看通胀\n- 若通胀压力持续，需进一步收紧\n- 重建外汇储备，保持汇率弹性\n- 强化银行监管，解决问题银行\n\n塞拉利昂的故事告诉我们：小国在气候+地缘双重冲击下，靠制度改革换融资空\n\n[... middle omitted ...]\n\nocuments have been released and are included in this package:\n\n• A Press Release including a statement by the Chair of the Executive Board.\n\n\\- The Staff Report prepared by a staff team of the\n\n[... middle omitted ...]\n\n support for the completion of the third review and associated requests, and the approval of their request for an arrangement under the RSF to strengthen long-term resilience and advance sustainable and inclusive growth."
  },
  {
    "id": "R004",
    "title": "IMF：不是周期而是治理，IMF评估所罗门群岛政策执行能力",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：不是周期而是治理，IMF评估所罗门群岛政策执行能力\n\n2025年，所罗门群岛的宏观环境交出了一份不错的成绩单。黄金产量和农业产出双双走高，基础设施项目稳步推进，全年GDP增速达到3.5%，经常账户甚至录得5.6个百分点的盈余。但这份来自IMF的2026年第四条磋商报告，指向了一个更复杂的叙事：外部冲击正在重塑这个小岛国的增长轨迹，而内部治理的脆弱性让调整空间变得异常逼仄。\n\n报告给出的核心判断是：2026年的增长将明显降温，通胀不确定性上升，财政空间正在被侵蚀。这不仅是周期性的扰动，更是对政策执行能力和治理质量的一次不确定性测试。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 黄金红利难以对冲中东冲击波\n\n报告中最直观的变化来自外部账户。2025年经常账户从赤字4.2%大幅跳升为盈余5.6%，主要推手是黄金和农产品出口。但IMF预计，2026年这一格局将迅速逆转，经常账户将重新陷入3.4%的赤字。原因很直接：中东局势推高了燃料和食品进口价格，而出口端的黄金价格红利可能不足以完全对冲。\n\n从数据看，进口占GDP的比重预计从2025年的55.5%升至61.9%，而出口占比则从52.4%回落至50.0%。贸易条件的出现变化几乎是确定性的。对于这样一个高度依赖进口能源和食品的地区，外部价格冲击的传导速度往往比模型预测更快。\n\n> **KC评论：** 这里的关键变量不是黄金产量，而是黄金出口价格能否持续高位运行。报告提到了金矿扩产作为上行不确定性，但其前提是“稳健的资源管理和有限的财政激励”——这两个条件在当前治理环境下都非易事。完整报告中的债务可持续性分析（DSA）部分，值得关注外部债务在油价冲击下的不确定性测试假设。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 财政缓冲已近枯\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n所罗门经济：金矿撑起一片天，但中东战火正在逼近\n\n封面短标题：小岛国的大麻烦\n\n封面副标题：金矿红利能持续多久？\n\n---\n\n所罗门群岛2025年经济表现超出预期，GDP增长3.5%，通胀仅2.7%。但这份来之不易的成绩单，正被中东局势投下阴影。\n\n1️⃣ 金矿是最大亮点\n黄金和农产品出口推动经常账户顺差达到GDP的5.6%，这是过去几年罕见的数字。但关键在于，这种资源型增长能持续吗？研报指出，如果资源管理得当、不过度使用财政激励，金矿扩产可能进一步拉动增长。\n\n2️⃣ 2026年压力陡增\n中东战争正在传导——预计GDP增速放缓至2.6%，通胀飙升至5.4%（主要来自燃料价格上涨）。经常账户将从顺差转为逆差，幅度达GDP的3.4%。财政赤字预计扩大到4.1%，而政府现金储备已经见底。\n\n3️⃣ 财政纪律是核心课题\n研报反复强调一个关键点：必须通过现实预算减少赤字、重建流动性缓冲。具体建议包括：尽快引入增值税、加强税收执法、削减采掘业的税收优惠。应对战争影响的措施要严格限时、保留价格信号、精准定向。\n\n4️⃣ 汇率制度不动摇\n所罗门群岛实行固定汇率制（盯住美元、澳元、新西兰元篮子），央行被建议保持政策一致性，避\n\n[... middle omitted ...]\n\nIslands on economic developments and policies. Based on information available at the time of these discussions, the staff report was completed on June 10, 2026.\n\n• A Debt Sustainability Analys\n\n[... middle omitted ...]\n\nup:\n\nPacific Islands: Development news, research, data | World Bank\n\n• Asian Development Bank:\n\nhttps://www.adb.org/countries/solomon-islands/main\n\n• Pacific Financial Technical Assistance Center:\n\nhttps://www.pftac.org/"
  },
  {
    "id": "R005",
    "title": "IMF：不是台风而是海洋，IMF评估所罗门群岛两大长期不确定因素",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：不是台风而是海洋，IMF评估所罗门群岛两大长期不确定因素\n\n一份来自IMF的《所罗门群岛：气候变化、宏观宏观环境不确定性与适应》报告，给出了一个反直觉的判断：这个太平洋岛国未来几十年最需要关注的，不是极端高温或更频繁的台风，而是两股更缓慢但更确定的力量——海平面上升和海洋生态系统变化。\n\n报告基于最新气候模型和实证分析，试图回答一个核心问题：当气候变化以渐进方式冲击一个小型岛屿地区时，最脆弱的是哪些环节？答案指向了渔业资源、海岸基础设施和人口分布格局。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 渔业资源的长期调整，比想象中更确定\n\n报告引用了Fisheries and Marine Ecosystem Model Intercomparison Project（FishMIP）的模拟结果：在所罗门群岛专属宏观环境区，可开发鱼类生物量到2050年将下降约11%，无论全球采取低排放还是高排放路径。到2100年，高排放场景下的降幅可能达到50%。\n\n关键洞察在于时间窗口。报告指出，气候和海洋系统的惯性决定了，不同排放路径对渔业的影响要到本世纪后半叶才会显著分化。这意味着，即使全球减排取得进展，所罗门群岛在未来二三十年仍将承受渔业资源下降的冲击。考虑到渔业贡献了该国约4%的GDP，并支撑着大量人口的生计和粮食安全，这一趋势的宏观宏观环境含义不容忽视。\n\n> **KC评论：** 渔业资源的长期下降，本质上是将所罗门群岛置于一个“时间陷阱”中——短期适应措施无法逆转这一趋势，而长期调整又需要从现在开始。报告没有展开的是，这将对政府财政收入、贸易平衡和农村就业结构产生怎样的连锁反应。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 海平面上升：一项可以量化的成本，但分布极不均匀\n\n报\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n气候变局下的所罗门群岛：经济韧性怎么建？\n\n封面标题：气候风险与所罗门经济\n\n副标题：升温、海平面、渔业——三座大山\n\n---\n\n气候变化对经济的影响，不是未来的事，而是正在发生的事。所罗门群岛这份最新研报，把风险拆得很清楚。\n\n1️⃣ **升温是慢变量，但累积效应惊人**\n- 到2020年，平均气温已比工业化前升高约0.9-1.1°C\n- 若维持高排放路径，到2085年可能再升温3°C\n- 气温每上升1°C，GDP潜在损失约1.3-2.6%\n- 这不是短期冲击，而是会持续压低经济增长基线\n\n2️⃣ **极端降雨才是“急脾气”**\n- 所罗门没有极端高温事件，但短时强降雨在加剧\n- 最大1日降水量（Rx1day）呈上升趋势\n- 这意味着：洪水、滑坡、基础设施损坏会越来越频繁\n- 相比干旱，这才是更紧迫的宏观风险来源\n\n3️⃣ **海平面上升是“沉默的资产侵蚀”**\n- 到2100年，低排放情景下海平面上升约0.52米，高排放可达0.79米\n- 所罗门人口和关键基础设施高度集中在低海拔沿海\n- 仅海平面上升，年均损失就可能占GDP的0.1-0.4%\n- 加上风暴潮和ENSO影响，实际冲击可能更大\n\n4️⃣ **\n\n[... middle omitted ...]\n\nshington, D.C.\n\n# SOLOMON ISLANDS\n\nSELECTED ISSUES\n\nJune 10, 2026\n\nApproved By\n\nNada Choueiri\n\nPrepared By Emanuele Massetti and Filippos Tagklis\n\n## CONTENTS\n\n## CLIMATE CHANGE, MACROECONOMIC\n\n[... middle omitted ...]\n\niyatikanto, A. Sorichetta, A.J. Tatem and M. Bondarenko. 2024 \"WorldPop high resolution, harmonised annual global geospatial covariates. Version 1.0.\" University of Southampton: Southampton, UK. DOI:10.5258/SOTON/WP00772"
  },
  {
    "id": "R006",
    "title": "IMF：不是缺贸易意愿，是政策卡住了，IMF看海湾与中亚合作",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：不是缺贸易意愿，是政策卡住了，IMF看海湾与中亚合作\n\n全球贸易碎片化正在重塑区域合作的逻辑。当各国都在寻找更可靠的贸易伙伴时，一份来自IMF的新报告给出了一个反直觉的判断：海湾合作委员会（GCC）与高加索和中亚地区（CCA）之间的宏观环境联系虽然目前很薄弱，但政策改善的回报可能远超预期。报告的核心不是提到某个具体行业，而是指出物流、治理和跨境支付这些“基础设施”层面的改革，能撬动高达150%的贸易增长。这不是一个关于石油的故事，而是一个关于如何把地缘邻近转化为宏观环境互补的实操框架。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 两地贸易的瓶颈不在需求，在政策环境\n\nGCC和CCA的出口结构确实相似——都高度依赖碳氢化合物。但报告指出，非油气贸易正在变得多样化，且两地存在明显的资本流动互补性：GCC是资本净输出方，CCA是资本净输入方。理论上，这样的组合应该催生活跃的贸易和研究。\n\n现实却是双边贸易占比极低。IMF通过引力模型测算发现，如果只看宏观环境规模和地理距离，GCC与CCA之间的实际贸易额远低于“应有水平”。造成这一差距的，不是缺乏贸易意愿，而是政策环境的制约。报告特别指出，GCC在物流、治理、监管负担和跨境支付系统方面表现更好，而CCA在非关税措施和政府宏观环境干预方面反而更优。这意味着，两地各有短板，也各有可相互借鉴的领域。\n\n> **KC评论：** 这份报告最有价值的部分，不是告诉你“要合作”，而是用数据告诉你“卡在哪里”。如果你关注中亚或海湾的研究机会，真正值得看的不是资源禀赋，而是那些影响交易成本的制度细节——比如海关效率、支付清算速度、研究保护条款。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 物流和治理改善，能带来贸易翻倍增长\n\n报告给出了具体的\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n海湾与中亚，正悄悄连成一条线\n\n🔗 GCC + CCA = 下一个区域合作亮点？\n\n最近读了一份投行研报，讲的是海湾合作委员会（GCC）与高加索及中亚地区（CCA）的经济合作潜力。信息量很大，但逻辑很清晰，整理几个核心发现：\n\n1/ 两个区域都在搞“去油”转型\n- GCC和CCA的共同点：都靠油气吃饭\n- 但两边都在努力降低油气出口占比，非油气贸易正在多元化\n- CCA是资本输入方，GCC是资本输出方——天然互补\n\n2/ 政策改善能撬动巨大增量\n- 如果CCA把物流和治理水平做到全球前25%，商品贸易能分别增长150%和120%\n- 降低关税、减少贸易限制、改善营商环境，效果同样显著\n- GCC因为起点高，改善空间小一些，但治理和物流领域仍有提升余地\n\n3/ 外资流入也有潜力\n- 结构性改革（制度质量、贸易自由化、劳动力市场、金融发展）能显著提升FDI\n- CCA如果补上政策短板，FDI增量可达GDP的0.7%\n- GCC相对小一些，约0.14%\n\n4/ 跨境支付是隐形基础设施\n- CCA的跨境支付系统整体偏弱\n- G20路线图提供了三个方向：支付系统互通、法律框架完善、数据标准统一\n- 每个国家情况不\n\n[... middle omitted ...]\n\nkhache, Said A., author. | Painchaud, Francois, author. | Assem, Hoda, author. | Ismail, Muayad, author. | Lee, Jeong Dae, author. | Rao, Nasir, author. | Simone, Alejandro, author. | Troug, H\n\n[... middle omitted ...]\n\nvernment and FDI: An Empirical Analysis Based on the Panel Data of 81 Countries.\" Journal of Technology Management in China 5 (2): 176–84.\n\n![](images/e806a1d201a159089ace6791f7c45b40100e37030d3c08a4292f577de83ed1cb.jpg)"
  },
  {
    "id": "R007",
    "title": "经合组织：经合组织支招阿根廷，NCP重建信任需先修复基础",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：经合组织支招阿根廷，NCP重建信任需先修复基础\n\n阿根廷负责任商业行为国家联络点（NCP）正面临一个结构性矛盾：制度设计有潜力，但执行资源在过去五年被砍掉一半以上。经合组织2026年发布的同行评审报告指出，这个设在阿根廷外交部的机构目前只有0.85个全职人力，远低于2021年的1.75个。人力不足直接导致推广活动被动、案件处理量下降、利益相关方信任度走低。\n\n这份报告的价值不在于批评，而在于它提供了一个可操作的修复路径：从法律基础、咨询委员会运作、到案件处理程序的全面更新。对在阿根廷运营的跨国公司、人权组织以及关注拉美负责任商业实践的观察者来说，这份报告揭示了NCP机制在实际运作中的典型困境。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 咨询委员会“有名无实”，制度设计未转化为实际影响力\n\n阿根廷NCP在2000年成立，2006年通过部长决议获得法律基础。其制度设计中的一个亮点是设立了咨询委员会，理论上应包括企业、工会、公民社会和政府代表。但报告发现，这个委员会自2019年通过决议成立以来，从未就NCP的推广计划或具体案件处理被真正召集过。网站上列出的委员会成员信息已经过时，也没有明确的职权范围。\n\n这意味着什么？利益相关方反馈显示，NCP的实际运作并未鼓励外部参与。一个不运作的咨询委员会，不仅浪费了制度设计的潜力，还会让外界认为NCP缺乏透明度和包容性。对于希望利用NCP作为非司法申诉机制的企业和公民社会组织来说，这种不确定性本身就是障碍。\n\n> **KC评论：** 咨询委员会空转是许多新兴地区NCP的共性问题。经合组织的建议很具体：先明确职权范围，再定期开会，最后把委员会成员变成推广活动的“放大器”。完整报告里关于委员会组成和会议频率的建议，值得正在建设类似机制的国家仔细看。\n\n![研报图表 2](a\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n阿根廷NCP的同行评审：投研视角\n\n**阿根廷NCP：成效与挑战**\n\nOECD最新发布的阿根廷NCP同行评审报告，信息量很大。\n\n1/ **机构设置：有基础，但运转不畅**\n- 阿根廷NCP设在外交部，2000年成立，2006年正式立法。\n- 设有咨询委员会（企业、工会、民间社会、政府代表），但2019年成立后从未实际运作。\n- 人员：从2021年1.75个全职岗位降至现在的0.85个，4个兼职人员。\n- 无独立预算，依赖外交部常规经费。\n\n2/ **推广活动：被动且集中**\n- 过去几年推广活动多靠受邀参与，而非主动策划。\n- 近3年未制定推广计划。\n- 推广内容偏通用，未针对特定行业或地区（如阿根廷各省）。\n- 网站内容较全（西英双语），但无社交媒体运营。\n\n3/ **具体案件处理：数量下降，结果有限**\n- 2000年至今共受理15件案件，13件已结案，2件未受理。\n- 仅2件达成协议，占比13%。\n- 近5年仅收到1件新案，下降明显。\n- 2025年更新了案件处理程序，但未征求利益相关方意见。\n\n4/ **关键建议**\n- 明确咨询委员会的职权范围、成员构成和会议频率。\n- 更新部长决议，明确NCP\n\n[... middle omitted ...]\n\n![](images/e1127408ae289bd5d0078327f60c19beba391a98fd3621517997448493a7fe9e.jpg)\n\nAttribution 4.0 International (CC BY 4.0).\n\nThis work is made available under the Creative Commons Attribution\n\n[... middle omitted ...]\n\n17 Ministerial Council Statement, https://one.oecd.org/document/C/MIN(2017)9/FINAL/en/pdf (accessed on 24 June 2026).\n\nOECD (unpublished) (n.d.), Core Template for Voluntary Peer Reviews of National Contact Points.\n\nOECD"
  },
  {
    "id": "R008",
    "title": "联合国贸发会议：AI与半导体驱动全球FDI，但发展中国家被落下",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：AI与半导体驱动全球FDI，但发展中国家被落下\n\n全球外国直接研究在2025年录得6%的增长，达到1.6万亿美元。但如果只看到这个数字，就错过了这份报告真正想传递的信号。联合国贸发会议最新发布的《2026年世界研究报告》揭示了一个更深层的结构性变化：驱动全球资本流动的逻辑，正在从“成本与效率”转向“战略与安全”。这个转变的后果，远比增速本身更值得关注。\n\n报告的主判断很清晰：FDI总量在恢复，但恢复的方式暴露了脆弱性。增长主要来自少数大型地区和少数巨型项目——尤其是AI相关的基础设施。前20大东道地区吸纳了全球超过80%的FDI流入。在大多数行业和地区，新建项目的活跃度仍然仍在调整。地缘政治紧张、贸易政策波动、融资成本上升和技术竞争，正在让读者的决策变得高度选择性。\n\n> **KC评论：** 这份报告最有价值的部分不是那个6%的增速，而是它拆解了“谁在增长、谁被落下”。对于关注全球供应链布局的产业决策者来说，理解研究逻辑的转变，比盯着总量数字重要得多。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 战略行业的集中度在快速上升，发展中国家的传统优势正在失效\n\n报告中最值得注意的一个数据点：半导体、AI、清洁能源、关键矿产这四类战略行业，在2025年已占全球所有绿地研究项目的近一半。而在最不发达国家和中低收入国家，它们只吸引了不到10%的此类项目——在其他行业，这个比例超过20%。\n\n这个反差背后是研究逻辑的根本转变。过去几十年，资本追逐的是劳动成本、市场规模和效率优势，这正是许多发展中国家的竞争力所在。但今天，研究越来越多地受制于产业政策、补贴竞争、宏观环境安全考量和技术生态的成熟度。报告明确指出，这种新逻辑“奖励的是资金雄厚的地区和已建立的生态系统”，而大多数发展中国家无法匹配大国现在能够部署的扶持力\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n全球资本流向，正在悄悄转向\n\n全球资本正在“挑食”\n\n2025年全球FDI（外国直接投资）反弹了6%，达到1.6万亿美元。但别被这个数字骗了——增长背后藏着不少“偏科”。\n\n1️⃣ 钱只去几个地方\n全球超80%的FDI流向了前20大经济体。大型AI基础设施、半导体、清洁能源项目成为吸金主力。发展中国家整体只微增2%，而最不发达国家虽然涨了21%，但绝对量很小，只占全球2.7%。\n\n2️⃣ 项目变少，但单体变大\n发达国家绿地项目数量减少，但单个项目金额飙升——集中在数据中心、油气、半导体。发展中国家绿地项目则下降了18%。简单说：大玩家在砸大钱搞战略产业，小玩家连入场券都难拿。\n\n3️⃣ 供应链逻辑变了\n以前资本跟着成本走，现在跟着“经济安全”和“产业政策”走。各国补贴竞赛白热化，2025年新出台的投资政策措施创历史新高。结果就是：富国能砸钱抢项目，穷国只能干瞪眼。\n\n4️⃣ 发展中国家还有机会吗？\n有，但门槛很高。供应链重构带来“替代制造基地”和“关键矿物加工中心”的机遇，不过需要基础设施、技术、人才配套。比如东南亚、南亚部分国家正在承接转移，但多数低收入国家仍被排除在外。\n\n📌 一个观察：\n全球投资正在从“\n\n[... middle omitted ...]\n\n frontiers or boundaries.\n\nPhotocopies and reproductions of excerpts are allowed with proper credits.\n\nThis publication has been edited externally.\n\nUnited Nations publication issued by the Un\n\n[... middle omitted ...]\n\nthe United Nations system.\n\n![](images/ab537371392a9f96087c91d57dfc314a47ea474dd26503b5eacea1f38e9fbcc4.jpg)\n\nWorld Investment Report 2026\n\n![](images/e82fef2724c31980fe1cc100e84f546d7a8fb1280a78772183158e38c658156f.jpg)"
  },
  {
    "id": "R009",
    "title": "世界贸易组织：光伏电池到绿氢电解槽，环境产品贸易壁垒被逐一梳理",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界贸易组织",
    "digest": "[wechat_article.md]\n# 世界贸易组织：光伏电池到绿氢电解槽，环境产品贸易壁垒被逐一梳理\n\n全球贸易与环境政策的交汇处，最缺的不是共识，而是可执行的行动框架。世界贸易组织最新发布的《贸易与环境可持续性结构化讨论五年报告》给出了一个清晰信号：经过五年对话，参与方已从“要不要做”进入到“怎么做”的阶段。这份报告的价值不在于提出新目标，而在于为碳定价、绿色补贴、环境产品贸易等争议性议题提供了可比较、可参照的实践清单。\n\n报告由加拿Daiwa哥斯达黎加联合牵头，79个世贸组织成员参与，覆盖从清洁能源转型到循环宏观环境四大工作组。相比过往多边环境谈判的“宣言多、落地少”，TESSD的独特之处在于：它把自己定位为“孵化器和测试实验室”，而非又一个谈判平台。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 贸易相关气候措施的透明度，正在从原则走向操作\n\n报告最值得关注的产出之一，是工作组对贸易相关气候措施的系统梳理。成员方分享了在碳定价、边境碳调整、税收激励、标准认证、自愿行动等六大类政策设计中的具体做法。这不是一份理论文件，而是各国实际政策的“汇编与映射”。\n\n关键洞察在于：各国在碳计量标准、合格评定程序、认证体系上仍存在显著差异，这正是未来贸易摩擦的潜在爆发点。报告明确提出，信息共享和透明度是降低摩擦成本的最直接路径。对于出口导向型地区而言，理解不同市场的碳核算规则，正在成为合规竞争力的新维度。\n\n> **KC评论：** 这份报告没有给出统一的碳核算标准，但它提供了一份“谁在用哪种方法”的清单。对于企业而言，这意味着未来五年内，供应链碳足迹的披露要求将不再是选择题，而是必答题。报告附录中的具体政策清单值得细读。\n\n## 2. 绿色补贴的“好与坏”，需要更精细的设计框架\n\n补贴工作组是TESSD中最具争议性的议题之一。报告没有回避补贴可能产生的贸易扭曲效应，但也\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n全球贸易规则悄悄转向了\n\n🌍贸易×环保，正在改写全球规则\n\n最近翻了一份WTO五年总结报告，发现全球贸易规则正在经历一场静默转型——环保议题正在成为贸易谈判的核心。\n\n1️⃣ 什么是TESSD？\n2020年由50个WTO成员发起的贸易与环境可持续性结构化讨论。到现在已有79个成员参与，覆盖各大洲、不同发展阶段国家。不是一个简单会议，而是一个\"试验室\"，专门研究贸易政策如何支持气候和环保目标。\n\n2️⃣ 四个工作组在忙什么？\n- 贸易相关气候措施：讨论碳定价、边境碳调整、标准认证等政策设计\n- 环境商品与服务：识别太阳能电池、风电齿轮箱、电解槽等绿色商品的贸易壁垒\n- 循环经济：从产品设计到废弃处理全链条的贸易政策\n- 补贴：分析哪些补贴真正有利于低碳转型，哪些会扭曲贸易\n\n3️⃣ 为什么值得关注？\n这些讨论不是空谈。报告提到多个国家已落地具体政策——欧盟循环经济行动计划、毛里求斯2030路线图、秘鲁国家循环经济规划、沙特碳循环经济倡议。更重要的是，发展中国家在其中的角色被特别强调。\n\n4️⃣ 核心启示\n贸易不再只是关税和配额，碳足迹、循环标准、绿色认证正在成为新的贸易规则。对于做跨境生意、供应链管理、政策研究\n\n[... middle omitted ...]\n\n TRADE IN SUPPORT OF CLIMATE AND ENVIRONMENT: INSIGHTS FROM TESSD....7\n2.1 Clean energy transition....8\n2.2 Decarbonizing industry and transport ....11\n2.2.1 Energy-intensive industries (e.g. \n\n[... middle omitted ...]\n\n increase knowledge and understanding about the circular economy, facilitate training, training and technical assistance for the development of circular economy and sustainable consumption and production public policies."
  },
  {
    "id": "R010",
    "title": "波士顿咨询：生鲜供应链的瓶颈不是技术，而是组织协同",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：生鲜供应链的瓶颈不是技术，而是组织协同\n\n生鲜电商的扩张和消费者对“更新鲜”产品的追求，正在将零售供应链推向一个危险的临界点。波士顿咨询（BCG）在一份最新研报中提出一个核心判断：零售商与快消品（CPG）供应商之间传统的、以博弈为主的合作关系已经失效，双方必须转向深度的供应链协同与数字化整合，否则成本与服务水平将同时出现变化。\n\n这份报告并非老生常谈的“降本增效”。它揭示了一个结构性的矛盾：消费者想要更多品类、更短保质期的生鲜产品，这直接导致零售商从配送中心发出的卡车装载率下降、紧急补货增多、损耗率上升。与此同时，供应商端也面临订单波动加剧、前置时间缩短的困境，双方正在互相推诿责任。波士顿咨询认为，问题的根源不在于单点效率，而在于整条供应链的信息孤岛和激励错位。\n\n> **KC评论：** 简单说，零售商抱怨供应商送货不准时，供应商则说是零售商的订单太乱太急。双方都觉得自己没错，但问题出在彼此没有共享同一个计划系统。波士顿咨询的核心建议是：把“你的库存”和“我的货架”当成一个整体来看，而不是各自为战。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 生鲜渗透率每提升一个点，供应链成本就多一分不确定性\n\n报告引用的数据显示，生鲜产品的特性——保质期短、需求波动大、需要冷链运输——天然不适合传统的大批量、长周期供应链模式。当零售商为了满足线上订单而增加生鲜SKU时，一个直接后果是：出库卡车的装载率远低于入库卡车。波士顿咨询的调研显示，2018年出库卡车的平均装载率（按重量计）显著低于入库端，这意味着每趟运输的固定成本被摊薄到更少的产品上。\n\n更隐蔽的成本来自“损耗”和“紧急补货”。生鲜产品一旦错过最佳上架窗口，就会变成损耗。为了抢时间，零售商不得不增加紧急订单和加急配送，这反过来又推高了物流成本和运营复杂度。报告\n\n[... middle omitted ...]\n\n、更有能力去推动这种深度协同？是拥有终端消费者数据的零售商，还是拥有生产能力和品牌资产的供应商？报告没有提供明确的判断。\n\n从行业实践来看，沃尔玛这样的巨头可以凭借规模要求供应商接入自己的系统，但大多数区域零售商并不具备这种议价能力。反过来，宝洁、雀巢这样的全球CPG巨头，也可能更倾向于自建数据平台，而非被动接入每个零售商的系统。这场协同的最终形态，可能取决于哪一方能率先证明“共享数据带来的增量收益”远大于“放弃数据控制权的不确定性”。\n\n[note.md]\n生鲜电商背后，供应链在打架\n\n**供应链转不动了**\n\n**当零售商和供应商开始互相甩锅，谁在买单？**\n\n---\n\n投行研报拆解了一个有意思的现象：生鲜越卖越多，但供应链越来越疼。\n\n1️⃣ **运输成本在涨，但车没装满**\n消费者要“更新鲜”的产品，意味着保质期更短、配送更快。结果是——卡车经常半空着从配送中心出发。司机难招，运费涨，但每趟运的货反而少了。\n\n2️⃣ **损耗率上升，服务水平下降**\n“新鲜”是有代价的：急单增多，破损和丢失（shrinkage）随之上升。同时，货架缺货率却在恶化。多数零售商已经没达到自己的内部服务目标。\n\n3️⃣ **零售商和供应商开始互相埋怨**\nCPG供应商说：零售订单波动大、提前期短、单量小，根本没法预测。零售商说：生产可靠性不行。双方各执一词，但问题其实出在——**没有一起看整条供应链**。\n\n4️⃣ **解决方案？用数字工具打通信息孤岛**\n报告建议零售商和CPG公司坐下来，不只是销售和营销开会，运营也要参与。然后用云、大数据、AI、IoT等技术，共享需求预测和库存数据，减少浪费。\n\n5️⃣ **四个关键步骤**\n- 统一目标和激励\n- 打通端到端信息\n-\n\n[... middle omitted ...]\n\nrter shelf lives—putting more pressure on the entire supply chain. This pressure is pushing retailers' cost and service metrics in the wrong direction and boosting tension between retailers an\n\n[... middle omitted ...]\n\nmpanies should take four steps to digitize and further integrate their supply chains.\n\nAgree on incentives and goals: Ensure common KPIs and objectives among retailers and CPG companies to address end-to-end performance."
  },
  {
    "id": "R011",
    "title": "波士顿咨询：超市SKU不是太少，而是太多，减20%反增销售额",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：超市SKU不是太少，而是太多，减20%反增销售额\n\n疫情之后，超市行业面临一个反直觉的结论：让货架变空，反而能提升销售额。波士顿咨询在一份针对美国区域连锁超市的研究中，通过试验发现，主动削减20%至25%的SKU后，受影响品类的销售额反而增长了2%。这个数字背后，是传统超市行业一个长期被忽视的结构性问题。\n\n过去三十年，美国传统超市的平均SKU数量增长了80%。货架被塞满，顾客却更难找到想要的东西。波士顿咨询指出，这种“产品泛滥”不仅没有带来销售增长，反而成为传统超市在与折扣店、会员店甚至便利店竞争中的致命短板。一个关键数据是：区域超市每英尺货架的SKU数量，比折扣渠道高出50%。\n\n> **KC评论：** 这个2%的销售增长，是在疫情前完成的试验。但疫情后，消费者对“快速完成购物”的诉求只会更强。波士顿咨询认为，如果传统超市不主动简化，它们会继续被两端挤压——价格上输给Costco这种会员店，便利性上输给便利店。完整报告里有一张“消费者决策树”的图表，展示了如何用数据决定保留哪些SKU，值得细看。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 品种越多，运营成本越高，但顾客满意度越低\n\n超市行业的“品种悖论”在于，零售商长期把“更多选择”等同于“更好服务”。波士顿咨询的调研显示，在维生素、冷冻蔬菜、罐头汤这类标准化品类中，过多的选择反而引发“决策瘫痪”——顾客因为选择困难而放弃购买。2020年美国零售联合会的调查中，63%的消费者把“便利”列为重要指标，其中47%的人明确说“容易找到商品”就是便利。\n\n从运营端看，SKU膨胀带来的成本是系统性的。仓储空间被低效占用，补货和理货的工时持续增加，供应链因为品项过多而接近满负荷运转。更隐蔽的问题是，供应商通过进场费和新品上架费控制了货架决策权，零售商反而失去了\n\n[... middle omitted ...]\n\n径。这也意味着，对于已经启动SKU优化的企业来说，简化只是第一步，真正的挑战在于如何把省下来的资源和空间，转化为对顾客有吸引力的新价值——比如更快的配送、更好的生鲜品质，或者更具竞争力的自有品牌。\n\n对于行业观察者而言，波士顿咨询的判断提供了一个清晰的观察框架：未来几年，超市行业的竞争焦点将从“货架多不多”转向“货架对不对”。能够用数据驱动的方式持续优化品种结构，同时把节省的成本转化为顾客体验提升的企业，才更有可能在存量市场中守住份额。\n\n[note.md]\n超市货架正在杀死你的购物体验\n\n货架变少，反而卖得更多\n\n你有没有发现，现在的超市越来越难逛了？货架堆得满满当当，但想买的东西却经常找不到。这不是错觉，而是真实存在的问题。\n\n投行研报发现，过去30年超市SKU数量暴增80%。但更可怕的是，区域超市每英尺货架的SKU数量比折扣店多50%，却还在不断丢失市场份额。\n\n1/ 太多选择=没有选择\n研究表明，63%的消费者把“便利”放在首位。当货架上摆满20种番茄酱时，你反而更难做出决定。这就是“选择瘫痪”——太多选项反而降低了购物体验。\n\n2/ 减少20%SKU，销售额反增2%\n这不是理论。某超市试点减少20%-25%的SKU后，受影响品类的销售额反而增长了2%。精简货架不仅让购物更轻松，还能释放仓库空间、优化供应链、降低运营成本。\n\n3/ 怎么精简才对？\n- 用消费者决策树分析：什么属性对顾客最重要\n- 结合忠诚度数据：保留高粘性产品\n- 考虑全链路成本：不只是采购价，还有仓储、配送、上架\n- 先试点再推广：不要一刀切\n\n后疫情时代，消费者对价格和便利性的要求只会更高。精简不是减少选择，而是帮顾客更快找到他们真正想要的东西。\n\n欢迎一起讨论，你觉得哪些品类的\n\n[... middle omitted ...]\n\nare most in demand has been a pivotal measure in helping traditional retailers manage during the height of the crisis. As middle-market grocery retailers emerge from the unprecedented strain o\n\n[... middle omitted ...]\n\no reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter."
  },
  {
    "id": "R012",
    "title": "波士顿咨询：年轻家庭线上杂货消费比线下高30%至50%",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：年轻家庭线上杂货消费比线下高30%至50%\n\n线上买菜的渗透率在多数国家仍远低于消费者意愿。波士顿咨询这份报告的核心判断是：供给端的犹豫，而非需求端的不足，才是制约市场爆发的关键。报告预测全球线上杂货市场到2018年将达1000亿美元，并指出早期行动者将获得显著的先发优势。但真正有价值的洞察，不在于市场规模有多大，而在于如何用宏观环境上可行的方式去获取它。\n\n报告的核心主张可以概括为：不要在起步阶段就追求昂贵的“最后一公里”配送，而应优先选择“点击取货”模式，在积累足够本地规模后再谨慎拓展上门配送。这个判断基于对八个国家消费者的调研和多家头部零售商的实际运营经验。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 消费者已准备好，但零售商仍在观望\n\n波士顿咨询的调研显示，消费者对线上购物的期待远高于当前的实际使用频率。受访者平均每年愿意使用线上杂货服务13.5次，超过每月一次。在巴西和中国，这一频率接近每月两次。在美国，约半数受访者表示会尝试上门配送或点击取货服务。\n\n报告特别指出，零售商最重要的客户群体——年轻家庭和高收入夫妇——对线上购物尤其热衷。当他们转向线上后，全渠道消费额往往比纯线下购物高出30%至50%。\n\n> **KC评论：** 这意味着零售商面临的核心不确定性不是线上业务蚕食线下，而是竞争对手通过线上渠道锁定你的最佳客户，进而带动更高价值的全渠道消费。报告的逻辑是：线上不是替代线下，而是客户关系管理的延伸和升级。\n\n目前各国线上杂货渗透率的差异，更多源于供给端而非需求端。英国线上杂货已占市场总额的5%，法国3%，韩国4%。这些领先市场每年以20%至50%的速度增长。报告认为，到2016年，多数市场的线上份额将翻倍。而落后市场的差距，主要源于零售商的犹豫，而非消费者的抗拒。\n\n![研报图表 2]\n\n[... middle omitted ...]\n\n亿美元后，竞争格局会如何演变？报告提到早期行动者能获得显著优势，但没有深入分析当市场成熟后，规模效应是否会压倒先发优势。\n\n第三，“点击取货”与“上门配送”的切换条件是什么？报告建议在“足够本地规模”后再添加配送，但这个“足够”的具体标准是什么？是订单密度、客户基数，还是区域覆盖率？\n\n这些问题本身，就是读者在阅读完整报告时可以重点寻找答案的方向。波士顿咨询的分析框架为零售商的决策提供了清晰的起点，但真正的挑战在于执行细节和本地化调整。\n\n[note.md]\n线上买菜这门生意，终于有人算清楚账了\n\n📌 1000亿美金的赛道，别等\n\n最近读了一份BCG的研报，讲的是线上生鲜这门难做的生意。分享几个核心判断：\n\n1️⃣ 别等了，需求是真的\n全球线上生鲜市场预计2018年达$1000亿。消费者平均一年愿意线上下单13.5次，年轻家庭和高收入群体更积极。不是没需求，是零售商太犹豫。\n\n2️⃣ 最后一公里是烧钱黑洞\n直接送货上门成本太高，低密度区域每单配送费高达$20，但消费者只愿意付$5-10。聪明做法：先做“线上下单+门店自提”，等规模起来再考虑配送。\n\n3️⃣ 差异化要“买得起”\n不是所有功能都值得投。重点投资那些真正影响满意度的地方，同时盯紧运营成本。别为了炫技把利润烧光。\n\n4️⃣ 模式必须进化\n没有一劳永逸的方案。随着市场、用户和自身能力变化，模式要跟着调整。设定现实的里程碑和回报目标。\n\n几个有意思的细节：\n- 英国线上生鲜已占5%，法国3%，韩国4%\n- 线上客户全渠道消费比纯线下高30-50%\n- Tesco线上销售已占8%，增长主要靠线上\n- Fresh Direct在纽约做到年收入$4亿且盈利\n\n你所在的城市，线上买菜体验怎么样？欢迎一起讨论。\n\n#学\n\n[... middle omitted ...]\n\nrkets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure l\n\n[... middle omitted ...]\n\ninneapolis\n\nRome\n\nWarsaw\n\nBudapest\n\nHong Kong\n\nMonterrey\n\nSan Francisco\n\nWashington\n\nBuenos Aires\n\nHouston\n\nMontréal\n\nSantiago\n\nZurich\n\nCanberra\n\nIstanbul\n\nMoscow\n\nSão Paulo\n\nCasablanca\n\nJakarta\n\nMumbai\n\nSeattle\n\nbcg.com"
  },
  {
    "id": "R013",
    "title": "波士顿咨询：AI定价不是选择题，是零售商的生存题",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI定价不是选择题，是零售商的生存题\n\n当成本通胀、供应链波动、消费转移和价格竞争同时发生，传统零售定价方法已经到达极限。波士顿咨询最新报告给出的判断非常直接：AI驱动的动态定价，不再是可选项，而是零售商维持竞争力的必要条件。\n\n报告基于对全球零售商的调研发现，那些已经完成AI定价转型的企业，毛利润提升5%到10%，同时营收和客户价值感知也获得可持续增长。这不是一个理论推演，而是可量化的结果。\n\n> **KC评论：** 很多零售商还在用Excel或传统规则引擎做定价，认为“AI定价就是自动化调价”。波士顿咨询的报告提醒，真正的AI定价是同时处理战略、卫生和动态三个维度的复杂系统，而不是简单替代人工。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 传统定价只抓一两个维度，AI定价同时处理十几个变量\n\n规则驱动的定价通常只关注一到两个维度，比如成本加成或竞品对标。波士顿咨询报告指出，AI定价引擎可以同时考虑战略、卫生和动态三大类十几个维度，在数十亿个潜在场景中找到每个门店、每个商品的最优价格。\n\n战略维度包括定价目标、品类角色和关键价值商品、全渠道定价、价格区域。卫生维度关注商品间关系、自有品牌与全国品牌的价格差、定价的“魔法数字”。动态维度则涉及实时竞品追踪和动态预测。\n\n一个关键差异：传统定价做“平均化”，AI定价做“去平均化”。零售商可以主动研究于那些最能吸引客流、最能塑造价值感知的品类和商品，而不是对所有商品一视同仁。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 动态定价的核心不是降价，而是精准定位\n\n报告中最具操作性的洞察来自动态维度。当一家连锁超市开始系统追踪竞品价格，它发现自己的某些商品价格比主要竞品低了20%到30%。通过提价到刚好低于竞品的位置，这家零\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nAI如何帮零售定价多赚10%？\n\nAI定价，零售新解法\n\n用智能化把复杂变成利润\n\n---\n\n最近读了一篇某外资投行的研报，关于AI在零售定价中的应用，信息量很大，整理几个关键点。\n\n**1. 为什么现在需要AI定价？**\n传统定价方式已经搞不定了。成本持续上涨、供应链波动、消费者变来变去、竞争激烈……靠人工定规则根本管不过来。AI能同时处理几十个变量，帮零售商找到最优价格。\n\n**2. 用AI定价，效果如何？**\n研报显示，已经落地AI定价的零售商，毛利率提升了5%-10%，收入也同步增长，消费者对价格的感知反而变好了。不是简单降价，是聪明地定价。\n\n**3. 三大定价维度**\n- **战略层**：明确定价目标（比如要收入还是要利润），识别哪些商品是吸引顾客的关键品（KVIs），统一线上线下价格策略，按门店周边消费力差异化定价。\n- **卫生层**：保持价格逻辑让消费者觉得合理。比如同类商品的价格关系要清晰（好/更好/最好），自有品牌和品牌产品的价差要合适，尾数定价要符合心理习惯（比如9.9）。\n- **动态层**：实时追踪竞品价格，用AI预测需求变化，不再靠固定模型，而是根据天气、促销、竞品动态调整。\n\n[... middle omitted ...]\n\ns and methods. Instead of sticking with traditional rule-based approaches that focus on simplification, retailers are now implementing AI-powered solutions and dynamic pricing models.\n\nThese s\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R014",
    "title": "波士顿咨询：自有品牌不是平替，而是零售商核心竞争力",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：自有品牌不是平替，而是零售商核心竞争力\n\n传统超市正在被折扣店、会员店和电商蚕食份额，而驱动这场格局重塑的核心力量，并非全国性品牌，而是自有品牌。波士顿咨询这份报告的核心判断是：自有品牌已从“低价仿制品”进化为零售商差异化、提升利润、掌控供应链的战略武器。那些仍将其视为“二线产品”的零售商，将在未来五年内失去市场地位。\n\n报告指出，美国自有品牌年销售额已达1200亿美元，占整体市场的18%。而在欧洲，这一比例更高，自有品牌早已成为多个品类的市场领导者。更重要的是，美国市场的份额转移几乎完全由自有品牌驱动——每年约30亿美元的自有品牌销售额从传统超市流向其他渠道，而全国性品牌并未出现同等幅度的转移。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 消费者变了，自有品牌是唯一能同时满足“价值”与“差异化”的答案\n\n波士顿咨询认为，当前零售业的竞争已从“价格战”转向“价值战”。消费者并非只追求最低价，而是寻求“最佳品质与价格的平衡”。千禧一代（占美国成年购物者的27%）更看重便捷、创新、健康与可持续性，他们对尝试新品牌持开放态度，也更愿意为独特的购物体验付费。\n\n这意味着，零售商若仅靠全国性品牌打价格战，利润空间会被持续压缩，且无法建立真正的用户忠诚。自有品牌则提供了一条路径：通过独家产品、品质对标甚至超越全国性品牌，同时保持价格优势，从而在消费者心中建立“只有在这里才能买到”的认知。\n\n> **KC评论：** 这个判断的关键在于“价值”的定义。报告强调的是“质量价格比”而非“绝对低价”。对零售商而言，自有品牌的战略价值不在于“更便宜”，而在于“用同样的钱买到更好的东西”。完整报告中对千禧一代消费偏好的详细拆解，值得所有面向年轻消费者的品牌仔细阅读。\n\n![研报图表 2](assets/xhs_card_02.p\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n超市自有品牌，正在逆袭\n\n自有品牌，不再是平替\n\n传统超市正在被折扣店和会员店抢走份额，而核心武器，就是自有品牌。\n\n1️⃣ 自有品牌为什么突然变强了？\n- 以前：低价平替，包装朴素，消费者觉得“不如大牌”\n- 现在：品质升级，创新更快，甚至能引领行业趋势\n- 消费者：更追求“价值感”——不是最低价，而是最好的品质/体验\n\n2️⃣ 数据很直观\n- 美国自有品牌年销售额已达1200亿美元，占整体市场18%\n- 欧洲更早完成渗透，很多品类自有品牌已是市场第一\n- 传统超市份额在下降，而折扣店、会员店、便利店都在涨\n\n3️⃣ 为什么传统超市必须做自有品牌？\n- 差异化：别人买不到，只有你有\n- 利润更高：省掉品牌溢价，还能控制供应链\n- 减少对大品牌的依赖，集中资源做爆款\n\n4️⃣ 成功案例参考\n- 沃尔玛：垂直整合供应链，从农场到货架全掌控\n- Aldi：自有品牌占90%销售额，靠极致效率和低价圈粉\n- Lidl：最早推出“好/更好/最好/高端”多层级自有品牌\n- HEB：自有品牌占线上销售28%，甚至打进超级碗广告\n\n5️⃣ 做自有品牌的三个关键\n- 战略与组织：明确品牌定位，选择适合的管理模式（独立团队/卓越\n\n[... middle omitted ...]\n\nnds—that they’re similar to but not as good as national brands, come in plain packaging, and carry a lower price—is outdated and changing fast. Grocers that don’t rapidly adapt their private-b\n\n[... middle omitted ...]\n\no reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter."
  },
  {
    "id": "R015",
    "title": "麦肯锡：AI匹配工具正改写技能培训与就业市场规则",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "麦肯锡",
    "digest": "[wechat_article.md]\n# 麦肯锡：AI匹配工具正改写技能培训与就业市场规则\n\n当全球宏观环境被不确定性笼罩，大多数讨论聚焦于不确定性与挑战时，麦肯锡在其2025年可持续与包容性增长影响报告中，提出了一个值得产业决策者认真对待的判断：**乐观不是情绪，而是基于事实的战略选择。**\n\n这份报告发布正值麦肯锡成立100周年。它没有停留在罗列企业社会责任项目，而是试图回答一个更根本的问题：在长达一个世纪的尺度上，增长能否同时做到可持续、包容、且可量化？报告给出的答案是肯定的，但前提是领导者必须同时管理三个维度——宏观环境机会、健康改善、环境可持续——而非将其视为零和博弈。\n\n> **KC评论：** 这份报告的独特之处在于，它把“影响力”从叙事层面拉回到可测量的绩效指标。例如，报告指出其客户贡献了全球GDP增长的16%，每年创造约100万个就业岗位，并实现了超过80%的报告二氧化碳减排量。这些数字本身比任何口号都更有说服力。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 技术赋能包容性增长，正从愿景走向可规模化的实践\n\n报告中最具操作性的洞察来自技术应用领域。麦肯锡与厄瓜多尔最大银行合作推出数字银行Deuna，覆盖600万用户和50万商户，其中大量用户此前从未被正规资金服务覆盖。这一案例的关键不在于技术本身，而在于它证明了**数字基础设施可以同时实现商业可行性与社会包容性**。\n\n在AI应用方面，报告提供了两个值得关注的信号：一是与默克合作将临床研究报告的撰写时间从数周压缩至数天，二是与青年成就组织合作开发AI教练工具，帮助50万以上学生提升表达能力。这些案例的共同特征是，AI被嵌入到具体工作流中，而非作为独立项目存在。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 技能重塑的规模效应，正在改写劳动力市场的游戏规则\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n别再说“百年未有之变局”了，看看这家公司怎么做\n\n**这家公司真的做了100年**\n\n有个数据挺有意思：过去100年，人类寿命翻倍、数十亿人脱贫、登上了月球。而这家公司刚好也成立100年。它最近发了一份年度影响力报告，不讲营收讲贡献，我翻完觉得很有启发。\n\n**它们聚焦四个方向，逻辑很清晰：**\n\n1️⃣ **经济机会**\n不是空谈“共同富裕”。帮一家非洲生物科技公司拿到2500万美元融资，直接创造300+岗位，覆盖2万农户。还搞了个免费线上培训项目，2025年在133个国家毕业了12万学员。\n\n2️⃣ **健康改善**\n重点不是治病，是“把健康嵌入日常场景”。比如在费城，把健康服务放进超市、学校和职场。还专门做了女性健康和脑健康研究——这些领域长期被忽视。\n\n3️⃣ **环境可持续**\n跟苹果合作，搞稀有金属的循环价值链。还给国家做“气候转型影响框架”，帮它们测试不同减碳路径的经济影响。不是喊口号，是给工具。\n\n4️⃣ **科技驱动的包容增长**\n帮厄瓜多尔最大银行做数字银行，让600万人（占市场60%以上）用上金融服务——很多是以前没银行账户的人。还跟JA合作做了个AI教练，帮50万学生练习演讲。\n\n**\n\n[... middle omitted ...]\n\nking inclusive growth\nthrough technology\n\n3 Message from our global managing partner\n\n4 Our approach to impact\n\n5 A century of helping organizations think bigger, build stronger, and expand op\n\n[... middle omitted ...]\n\ncreated with the help of AI.\n\nLearn more online at: McKinsey.com/sustainable-inclusive-growth-report\n\nWe welcome your comments and questions regarding this report. Please contact us at Social\\_Responsibility@McKinsey.com"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Adding the Quadratic Term of Gross Domestic Product Growth Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviatio"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Placebo Test"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Placebo Test Notes: The figure plots the impulse responses of carbon emissions to a placebo shock, constructed by randomly shifting the timing of economic policy uncertainty within each economy. Shaded areas represent"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Initial Carbon Emission Level Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Energy Intensity"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Energy Intensity Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in economic p"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Income Level"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Income Level Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in economic polic"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Climate Vulnerability"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Climate Vulnerability Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in econo"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Climate Vulnerability Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in econo"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Political Stability"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Political Stability Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in economi"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Political Stability Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in economi"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Financial Development"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Financial Development Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in econo"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Trade Openness"
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Trade Openness Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in economic pol"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Share of Renewable Energy"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Share of Renewable Energy Notes: The figure plots the impulse responses of carbon emissions to a 1-standard deviation increase in e"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Share of Research and Development Expenditure"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Share of Research and Development Expenditure R&D = research and development. Notes: The figure plots the impulse responses of carb"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Dynamic Response of Carbon Emissions to Economic Policy Uncertainty, Conditioning on Share of Research and Development Expenditure R&D = research and development. Notes: The figure plots the impulse responses of carb"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：政策不确定性延缓清洁转型，新兴市场如何提升排放韧性｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：基里巴斯案例，当社保支出增加，教育投入反而减少？｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Policy support amid the war in the Middle East. As of early May, the authorities have raised fuel prices this year by 28 (Petrol) and 46 percent (Diesel). To avoid more disruptive price movements, and in the absence of a strong social safety net to provide "
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Sierra Leone: Macroeconomic Stabilization 2022-26 Fiscal policy tightened substantially since 2022 on the back of successful tax revenue mobilization. Monetary policy also contracted considerably over the same period. The significant tightening in th"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The significant tightening in the policy stance contributed to stabilizing the exchange rate, ... ... sharply reducing inflation, ... ... bringing borrowing costs down to sustainable levels ... Sources: Sierra Leonean authorities and IMF estimates. ... and rev"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "... bringing borrowing costs down to sustainable levels ... Sources: Sierra Leonean authorities and IMF estimates. ... and reversing the crowding out of private credit. 5. The Bank of Sierra Leone (BSL) has made progress in rebuilding reserves. Coverage increa"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "58. The authorities have made progress on governance and anti-corruption reforms. Pursuing an action plan to implement the recommendations of the GCD will help focus and coordinate reform efforts. 59. Staff welcome the authorities' request for the proposed RSF"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "60. On the basis of the authorities' prior actions and corrective actions, staff support the requests for completion of the third ECF review, waivers of nonobservance of missed PCs, modification of PCs, and approval of the RSF arrangement. Figure 2. Sierra Leo"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Sierra Leone: Real and External Sectors, 2014-26 Non-iron ore growth accelerated in 2025. Inflation fell to the BSL's single-digit objective last year but has since increased amid the oil price shock. Exports have continued to grow while imports edge"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Exports have continued to grow while imports edged down last year. Official reserves declined further in 2025. Sources: Sierra Leonean authorities; and IMF staff estimates. ... and the REER appreciated in recent months. ## Figure 3. Sierra Leone: Fiscal Sector"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Official reserves declined further in 2025. Sources: Sierra Leonean authorities; and IMF staff estimates. ... and the REER appreciated in recent months. ## Figure 3. Sierra Leone: Fiscal Sector, 2010-25 The fiscal effort was substantial in 2025... Revenue coll"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Sierra Leonean authorities; and IMF staff estimates. ... and the REER appreciated in recent months. ## Figure 3. Sierra Leone: Fiscal Sector, 2010-25 The fiscal effort was substantial in 2025... Revenue collection continues to improve ... ... and dome"
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Sierra Leone: Fiscal Sector, 2010-25 The fiscal effort was substantial in 2025... Revenue collection continues to improve ... ... and domestic borrowing decreased. ... and expenditures decreased. Sources: Sierra Leonean authorities; and IMF staff "
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The fiscal effort was substantial in 2025... Revenue collection continues to improve ... ... and domestic borrowing decreased. ... and expenditures decreased. Sources: Sierra Leonean authorities; and IMF staff estimates. Figure 4. Sierra Leone: Monetary and Fi"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "... and domestic borrowing decreased. ... and expenditures decreased. Sources: Sierra Leonean authorities; and IMF staff estimates. Figure 4. Sierra Leone: Monetary and Financial Indicators, 2014–26 Base money growth has come down from recent peaks ... ...and "
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "... and expenditures decreased. Sources: Sierra Leonean authorities; and IMF staff estimates. Figure 4. Sierra Leone: Monetary and Financial Indicators, 2014–26 Base money growth has come down from recent peaks ... ...and private credit growth has picked up. P"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Sierra Leone: Monetary and Financial Indicators, 2014–26 Base money growth has come down from recent peaks ... ...and private credit growth has picked up. Private and Public Sector Credit Growth The banking sector is well capitalized, ... ... NPL rat"
  },
  {
    "figure_id": "F041",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "The banking sector is well capitalized, ... ... NPL ratios have fallen below the 10 percent threshold... ... and banks remain liquid. Sources: Sierra Leonean authorities; and IMF staff estimates. Notes: Figure 5. Sierra Leone: Capacity to Repay Indicators Comp"
  },
  {
    "figure_id": "F042",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "... and banks remain liquid. Sources: Sierra Leonean authorities; and IMF staff estimates. Notes: Figure 5. Sierra Leone: Capacity to Repay Indicators Compared to UCT Arrangements for PRGT Countries (In percent of the indicated variable)"
  },
  {
    "figure_id": "F043",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Notes: Figure 5. Sierra Leone: Capacity to Repay Indicators Compared to UCT Arrangements for PRGT Countries (In percent of the indicated variable) A. Total Fund Credit Outstanding B. Total Debt Service to the Fund"
  },
  {
    "figure_id": "F044",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Sierra Leone: Capacity to Repay Indicators Compared to UCT Arrangements for PRGT Countries (In percent of the indicated variable) A. Total Fund Credit Outstanding B. Total Debt Service to the Fund C. Largest Peaks"
  },
  {
    "figure_id": "F045",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1. Overview of Past and Present CD Spending Sierra Leone has received as much CDs as the AFR average country, both in terms of spending ... Most CD is delivered by FAD ... ... and number of projects. ...and primarily focused on revenue administration"
  },
  {
    "figure_id": "F046",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1. Overview of Past and Present CD Spending Sierra Leone has received as much CDs as the AFR average country, both in terms of spending ... Most CD is delivered by FAD ... ... and number of projects. ...and primarily focused on revenue administration"
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "... while MCM's CD is aimed at improving financial sector supervision and regulation, and monetary and macroprudential policies Inclusion & gender, and governance were two priority areas of intervention in Sierra Leone. Sources: IMF Staff calculations. ## Anne"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Sierra Leone's economy is highly vulnerable to climate shocks, including floods and landslides, as well as to changes to its already hot and humid climate. The country's capacity to deal with these shocks is severely constrained by lack of fiscal space, weak i"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "2. Sierra Leone is projected to experience rising temperatures throughout the century, with the extent of warming depending on future global emission scenarios (Figure 2). A particularly concerning trend is the sharp increase in the number of extremely hot day"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Average annual precipitation is high at 2700 mm... 3. These changes in climatic conditions are undermining agricultural productivity, weighing on GDP and worsening food insecurity. Agriculture accounts for half of employment and 30 percent of value added in th"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Average annual precipitation is high at 2700 mm... 3. These changes in climatic conditions are undermining agricultural productivity, weighing on GDP and worsening food insecurity. Agriculture accounts for half of employment and 30 percent of value added in th"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "3. These changes in climatic conditions are undermining agricultural productivity, weighing on GDP and worsening food insecurity. Agriculture accounts for half of employment and 30 percent of value added in the economy. Nonetheless, food insecurity has been in"
  },
  {
    "figure_id": "F053",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "4. Floods and landslides are costly, disproportionately affecting vulnerable communities and undermining livelihoods. Informal settlements around urban centers are especially exposed and vulnerable to floods. About 10 percent of Freetown's population lives in "
  },
  {
    "figure_id": "F054",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "5. Despite high rainfall, Sierra Leone faces significant challenges in access to drinking water and vulnerability to contamination. In rural areas, only about half of the population has access to treated water. The remainder rely on water sources like rivers, "
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "28. Development partners have also contributed to strategic planning and institutional strengthening. The Green Climate Fund (GCF) has supported the development of Sierra Leone's comprehensive National Adaptation Plan, while Germany has assisted with the third"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: Following Pondi and others (2022), intensity is defined as (Total death+30% Total Affected)/Total population. Sources: EM-DAT and Staff calculations using Pondi and others (2022). ## A3. Food Security and Adaptation Sierra Leone is more vulnerable than o"
  },
  {
    "figure_id": "F057",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "■ EMDEs ■ Most vulnerable ## Figure 4. Main Climate Data in Sierra Leone (concluded) ## M4. GHG Emissions vs. NDC Targets The gap between Sierra Leone's NDC target and its baseline emissions is modest, indicating that additional, yet manageable, mitigation eff"
  },
  {
    "figure_id": "F058",
    "report_id": "R003",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Adaptation scenario: The government invests 2.0 percent of GDP in climate-resilient public infrastructure instead of standard public infrastructure for each of the five years before the natural disaster. It finances this expenditure through a mix of grants "
  },
  {
    "figure_id": "F059",
    "report_id": "R003",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "4. Upfront investment in climate-resilient infrastructure, combined with efficiency enhancing fiscal reforms, reduces the adverse macroeconomic impact of natural disasters in Sierra Leone (Text figure 1). DIGNAD simulations show that early resilience measures "
  },
  {
    "figure_id": "F060",
    "report_id": "R003",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "4. Upfront investment in climate-resilient infrastructure, combined with efficiency enhancing fiscal reforms, reduces the adverse macroeconomic impact of natural disasters in Sierra Leone (Text figure 1). DIGNAD simulations show that early resilience measures "
  },
  {
    "figure_id": "F061",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## BACKGROUND ON DEBT 3. End-2025 stock data shows that Sierra Leone's public external debt marginally declined as a ratio to GDP (Text Figure 1). Total public debt declined from 46.9 to 46.7 percent of GDP at end-2025 amid strong nominal GDP growth and the st"
  },
  {
    "figure_id": "F062",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "5. The authorities are current on previously discovered external arrears. In February 2024, they verified external arrears of US\\$23.4 million owed to two companies for road construction and penalty interest on delayed payment of civil war-related services. Th"
  },
  {
    "figure_id": "F063",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- Under the baseline scenario, the PV of the public debt-to-GDP ratio exhibits a one-time breach of the threshold of 35 percent of GDP only in 2026 and gradually declines over the medium term (Figure 2). The overall debt service-to-revenue ratio is projected "
  },
  {
    "figure_id": "F064",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "\\- Stress tests indicate that the shocks to combined contingent liabilities and the primary balance are the most extreme ones. All the shocks simulated lead the PV of debt to GDP to breach the threshold, at least in the short run. Since the external debt servi"
  },
  {
    "figure_id": "F065",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "\\- In this context, (i) sustained and significant fiscal adjustment; and (ii) continued reliance on highly concessional external financing (ideally grants) are particularly important, including from IFIs which account for a large share of Sierra Leone's PPG ex"
  },
  {
    "figure_id": "F066",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023 Sources: Country authorities; and staff estimates and projections. ## RISK RATING AND VULNERABILITIES"
  },
  {
    "figure_id": "F067",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "18. It will be critical to mitigate risks through steadfast implementation of the fiscal consolidation, paired with the development of a deeper domestic debt market. While staff assesses that risks remain manageable at the current juncture, debt burden indicat"
  },
  {
    "figure_id": "F068",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Sierra Leone: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026–36 Sources: Sierra Leonean authorities; and IMF staff estimates and projections. 1/ The most extreme stress test is the test that yields the hi"
  },
  {
    "figure_id": "F069",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "1/ The most extreme stress test is the test that yields the highest ratio in or before 2032. The stress test with a one-off breach is also presented (in any), while the one-breach is deemed away for mechanical signals. When a stress test with a one-off breach "
  },
  {
    "figure_id": "F070",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Gross Nominal Public Debt (In Percent of GDP, DSA Vintages) Unexpected Changes in Debt 1/ (Past 5 Years, Percent of GDP 1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs for which LIC DSAs were produced. 3/ "
  },
  {
    "figure_id": "F071",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively low private external debt for average low -income countries, a ppt change in PPG external debt shou"
  },
  {
    "figure_id": "F072",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "3/ Given the relatively low private external debt for average low -income countries, a ppt change in PPG external debt should be largely explained by the drivers of the external debt dynamics equation. Figure 4. Sierra Leone: Realism Tools 3-Year Adjustment in"
  },
  {
    "figure_id": "F073",
    "report_id": "R003",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：塞拉利昂的紧缩见效了，但真正的考验在2028之前｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F074",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Total Exports (In Percent of GDP) ## Figure 1. Solomon Islands: Macroeconomic Developments and Outlook Economic recovery continues at moderate pace, in line with regional peers. ...and normalization of imports following the Pacific Games. Sources: Solomon Isla"
  },
  {
    "figure_id": "F075",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The current account balance recorded a surplus in 2025... Current Account Balance ...on the back of strong export performance, particularly from the mining sector... Sources: World Economic Outlook; and IMF Staff Calculations. Total Imports (In Percent of GDP)"
  },
  {
    "figure_id": "F076",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "...on the back of strong export performance, particularly from the mining sector... Sources: World Economic Outlook; and IMF Staff Calculations. Total Imports (In Percent of GDP) Sources: World Economic Outlook; and IMF Staff Calculations. ## Figure 2. Solomon"
  },
  {
    "figure_id": "F077",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Total Imports (In Percent of GDP) Sources: World Economic Outlook; and IMF Staff Calculations. ## Figure 2. Solomon Islands: Fiscal Indicators Solomon Islands tax revenue is relatively volatile... Sources: World Economic Outlook; and IMF Staff Calculations. .."
  },
  {
    "figure_id": "F078",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2. Solomon Islands: Fiscal Indicators Solomon Islands tax revenue is relatively volatile... Sources: World Economic Outlook; and IMF Staff Calculations. ... while the share of logging revenue has declined. Sources: Solomon Islands Authorities; and IM"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Expenditure has remained high, reflecting spending pressures and progress in infrastructure projects. Consequently, the fiscal deficit has persisted... Government Expenditure ...leading to continued increases in the public debt ratio, including domestic debt. "
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "...leading to continued increases in the public debt ratio, including domestic debt. Public Debt Non-performing Loans (In Percent) ## Figure 3. Solomon Islands: Money and Credit Developments Monetary conditions remain accommodative..."
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Non-performing Loans (In Percent) ## Figure 3. Solomon Islands: Money and Credit Developments Monetary conditions remain accommodative... Sources: IMF-IFS; and Central Bank of Solomon Islands. ...while commercial banks are moderately increasing credit to the p"
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "# Annex III. Assessing Solomon Islands' Growth Drivers and Prospects $^{1}$ This annex examines the factors driving or hindering economic growth in Solomon Islands and forecasts medium- to long-term growth prospects using growth accounting and dynamic time war"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "$$ where $I_{t}$ and $\\delta$ represent gross fixed capital formation at time t and the depreciation rate, respectively. We assume a depreciation rate ( $\\delta$ ) of 5 percent, following the cases of other low-income countries (IMF, 2024). $^{2}$ 5. Growth ac"
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "$$ \\hat {Y} = \\alpha \\hat {K} + (1 - \\alpha) (\\hat {A} + \\hat {h} + \\hat {L})\\tag{3} $$ Figure 3. Projected Labor Force Growth (In percent) Note: 5-PICs average is the average of Fiji, Papua New Guinea, Samoa, Tonga, and Vanuatu. ## C. Dynamic Time Warping For"
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "10. We use historical data of more than 200 countries ranging from 1970 to 2023 to forecast Solomon Islands' growth rates from 2024 to 2044. The data are sourced from the national accounts database compiled by the United Nations Statistics Division, the same d"
  },
  {
    "figure_id": "F086",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## A. Banking System Characteristics 1. Solomon Islands' banking system is small and concentrated, dominated by foreign-owned banks. In 2024, banks held SI\\$7.2 billion in assets, equivalent to 61 percent of the total financial system and 0.7 times the size of"
  },
  {
    "figure_id": "F087",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## A. Banking System Characteristics 1. Solomon Islands' banking system is small and concentrated, dominated by foreign-owned banks. In 2024, banks held SI\\$7.2 billion in assets, equivalent to 61 percent of the total financial system and 0.7 times the size of"
  },
  {
    "figure_id": "F088",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(Figure 2)The modest lending activity reflects structural challenges, including high informality, limited collateral due to communal land ownership, and high costs of providing services in rural and outer islands. On the liability side, banks are primarily fun"
  },
  {
    "figure_id": "F089",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "(Figure 2)The modest lending activity reflects structural challenges, including high informality, limited collateral due to communal land ownership, and high costs of providing services in rural and outer islands. On the liability side, banks are primarily fun"
  },
  {
    "figure_id": "F090",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "4. Non-performing loans (NPLs) remain elevated, and among the highest in the Pacific (Figure 5). In 2024, the NPL ratio stood at 11.6 percent, and concentrated in the personal, distribution, transportation, and construction sectors (Figure 6). These sectors al"
  },
  {
    "figure_id": "F091",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "4. Non-performing loans (NPLs) remain elevated, and among the highest in the Pacific (Figure 5). In 2024, the NPL ratio stood at 11.6 percent, and concentrated in the personal, distribution, transportation, and construction sectors (Figure 6). These sectors al"
  },
  {
    "figure_id": "F092",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "6. Results of the sensitivity analysis show that banks remain well capitalized and resilient to the set of shocks under both mild and severe downside scenarios. Among the shocks, credit risk adversely impacts banks' capital positions in both scenarios, compare"
  },
  {
    "figure_id": "F093",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "7. The section below shows the results of the different shocks in the adverse downside scenarios. a. Credit Risk Shock. This test assesses a general deterioration in asset quality, with NPLs assumed to increase proportionately across all banks, with an increas"
  },
  {
    "figure_id": "F094",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "c. FX shock. The FX shock assesses bank' sensitivity to a depreciation of the Solomon Islands dollar. Large exchange rate volatility has historically been limited, given that currency is pegged to a basket of currencies. The analysis focuses solely on direct F"
  },
  {
    "figure_id": "F095",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "21. The stress tests highlight important risks to debt sustainability. In the commodity price and GDP growth scenarios, public debt sustainability would be significantly undermined. The alternative scenario shows that slow-moving, long-term climate shifts coul"
  },
  {
    "figure_id": "F096",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "23. The domestic debt tool (Text Figure 2) illustrates the risks associated with domestic debt. The baseline assumes that the government will primarily rely on external debt to finance future deficits, reflecting the narrow investor base and the underdeveloped"
  },
  {
    "figure_id": "F097",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "23. The domestic debt tool (Text Figure 2) illustrates the risks associated with domestic debt. The baseline assumes that the government will primarily rely on external debt to finance future deficits, reflecting the narrow investor base and the underdeveloped"
  },
  {
    "figure_id": "F098",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ A bold value indicates a breach of the benchmark. 2/ Variables include real GDP growth, GDP deflator and primary deficit in percent of GDP. 3/ Includes official and private transfers and FDI"
  },
  {
    "figure_id": "F099",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ A bold value indicates a breach of the benchmark. 2/ Variables include real GDP growth, GDP deflator and primary deficit in percent of GDP. 3/ Includes official and private transfers and FDI"
  },
  {
    "figure_id": "F100",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "2/ Variables include real GDP growth, GDP deflator and primary deficit in percent of GDP. 3/ Includes official and private transfers and FDI."
  },
  {
    "figure_id": "F101",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections."
  },
  {
    "figure_id": "F102",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections. 1/ The most extreme str"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections. 1/ The most extreme str"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections. 1/ The most extreme str"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ The most extreme stress test is the test that yields the highest ratio in or before 2035. The stress test with a one-off breach is also presented (if any), while the one-off breach is deemed"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Solomon Islands: Drivers of Debt Dynamics – Baseline Scenario External and Public Debt Gross Nominal PPG External Debt (in percent of GDP; DSA vintages) Debt-creating flows (percent of GDP) Public debt Unexpected Changes in Debt 1/(past 5 years, perc"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Unexpected Changes in Debt 1/(past 5 years, percent of GDP) Gross Nominal Public Debt (in percent of GDP; DSA vintages) 1/ Difference between anticipated and actual contributions on debt ratios. Unexpected Changes in Debt 1/(past 5 years, percent of GDP) 2/ Di"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Gross Nominal Public Debt (in percent of GDP; DSA vintages) 1/ Difference between anticipated and actual contributions on debt ratios. Unexpected Changes in Debt 1/(past 5 years, percent of GDP) 2/ Distribution across LICs for which LIC DSAs were produced. Fig"
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Unexpected Changes in Debt 1/(past 5 years, percent of GDP) 2/ Distribution across LICs for which LIC DSAs were produced. Figure 4. Solomon Islands: Realism tools 3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported prog"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "2/ Distribution across LICs for which LIC DSAs were produced. Figure 4. Solomon Islands: Realism tools 3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since"
  },
  {
    "figure_id": "F111",
    "report_id": "R004",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：不是周期而是治理，IMF评估所罗门群岛政策执行能力｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F112",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Drawing on recent scientific data and model-based projections, this section provides an overview of the evolving risks and adaptation challenges posed by a warming climate, changes in marine ecosystems, and sea level rise. 2. Solomon Islands experiences high i"
  },
  {
    "figure_id": "F113",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "2. Solomon Islands experiences high interannual rainfall variability characteristic of the western tropical Pacific. The country has a humid equatorial-to-tropical climate with substantial precipitation throughout the year. Data on historical precipitations sh"
  },
  {
    "figure_id": "F114",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Notes: The solid gray line displays annual mean temperature. The solid black line displays the 30-year moving average. The first complete 15 years of the moving average are not shown because incomplete. The last 14 years show a linear trend estimated using the"
  },
  {
    "figure_id": "F115",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Projected Annual Temperature, Total Annual Precipitations for the Solomon Islands Temperature °C Precipitations (mm) Notes: The gray line describes historical values based on reanalysis (ERA5 for temperature and precipitation). The black line describ"
  },
  {
    "figure_id": "F116",
    "report_id": "R005",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Notes: The gray line describes historical values based on reanalysis (ERA5 for temperature and precipitation). The black line describes the 30-year moving average around each year. Colored lines represent the median of 30-year moving averages of CMIP6 anomalie"
  },
  {
    "figure_id": "F117",
    "report_id": "R005",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "4. Indices of within-year climate extremes show that intense precipitation events are the primary climate hazard for Solomon Islands and the main"
  },
  {
    "figure_id": "F118",
    "report_id": "R005",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Projected Changes of Extreme Precipitation and Dry Periods Maximum 1-day Precipitations (mm) Changes in Extreme 1-Day Rainfall (Rx1day) Under High Emissions 5. Sea-level rise represents a critical challenge for Solomon Islands, where much of the popu"
  },
  {
    "figure_id": "F119",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Changes in Extreme 1-Day Rainfall (Rx1day) Under High Emissions 5. Sea-level rise represents a critical challenge for Solomon Islands, where much of the population, essential infrastructure, and economic activity is in low-elevation coastal zones, including Ho"
  },
  {
    "figure_id": "F120",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "5. Sea-level rise represents a critical challenge for Solomon Islands, where much of the population, essential infrastructure, and economic activity is in low-elevation coastal zones, including Honiara and other major settlements. In the western tropical Pacif"
  },
  {
    "figure_id": "F121",
    "report_id": "R005",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "8. Forests in the Solomon Islands are expected to grow faster than in the present due to carbon fertilization and continued favorable climate conditions for biomass growth. CO $_{2}$ fertilization – the phenomenon where elevated atmospheric carbon dioxide enha"
  },
  {
    "figure_id": "F122",
    "report_id": "R005",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Rising Temperatures 10. Losses from rising temperatures are expected to emerge gradually over the century but their effect can lead to a cumulative deterioration of the macroeconomic outlook. Economic losses are anticipated to result from various sectoral e"
  },
  {
    "figure_id": "F123",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Box 1. The Impact of Climate Change on the Forestry Sector (Concluded) Using model output for the Oceania region, and considering two emissions scenarios and four climate models, we calculate the projected rate of change of model predicted production of ind"
  },
  {
    "figure_id": "F124",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Sea Level Rise 16. Sea level rise is a long-term challenge that can cause large disruptions in a country with large exposure to coastal inundation. Sea level rise does not pose long-term existential risks because the country is sparsely populated and has ma"
  },
  {
    "figure_id": "F125",
    "report_id": "R005",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "16. Sea level rise is a long-term challenge that can cause large disruptions in a country with large exposure to coastal inundation. Sea level rise does not pose long-term existential risks because the country is sparsely populated and has many high-elevation "
  },
  {
    "figure_id": "F126",
    "report_id": "R005",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "17. Adopting a strategy of planned retreat based on relocating people and assets away from vulnerable coastal zones proactively and gradually, is the adaptation strategy with the lowest economic cost across the entire country. This approach could reduce the ov"
  },
  {
    "figure_id": "F127",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## Box 2. Estimating the Cost of Sea Level Rise Granular analysis employing elevation data from a global grid with 100x100 meter resolution enables the identification of coastal regions that may experience permanent inundation under various scenarios of sea le"
  },
  {
    "figure_id": "F128",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## Box 2. Estimating the Cost of Sea Level Rise Granular analysis employing elevation data from a global grid with 100x100 meter resolution enables the identification of coastal regions that may experience permanent inundation under various scenarios of sea le"
  },
  {
    "figure_id": "F129",
    "report_id": "R005",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：不是台风而是海洋，IMF评估所罗门群岛两大长期不确定因素｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F130",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## A. Trade in Goods and Services Trade openness is relatively high in both regions, especially in the GCC (Figure 1). Trade openness, as measured by the ratio of export plus import of goods and services to GDP, is higher in the GCC and CCA than in emerging ma"
  },
  {
    "figure_id": "F131",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Trade Openness 1. Trade Openness (Percent of GDP) 2. Non-hydrocarbon Trade Openness (Percent of non-hydrocarbon GDP) Sources: World Economic Outlook Database; and IMF staff calculations. Note: AEs = advanced economies; CCA = Caucasus and Central Asia"
  },
  {
    "figure_id": "F132",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "CCA is also relatively close to having a comparative advantage in textiles and agriculture, whereas the GCC almost has a comparative advantage in chemicals and plastics. Services exports are more diversified, with both regions having comparative advantages in "
  },
  {
    "figure_id": "F133",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Comparative Advantage and Structure of Exports 1. CCA: Structure of Goods Exports (Percent of total exports) 3. CCA: Structure of Services Exports 2. GCC: Structure of Goods Exports (Percent of total exports) 4. GCC: Structure of Services Exports (Pe"
  },
  {
    "figure_id": "F134",
    "report_id": "R006",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "2. GCC: Structure of Goods Exports (Percent of total exports) 4. GCC: Structure of Services Exports (Percent of total exports) Sources: BACI (Base pour l'Analyse du Commerce International) database from the Centre d'Études Prospectives et d'Informations Intern"
  },
  {
    "figure_id": "F135",
    "report_id": "R006",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: Government services include embassies and consulates, military units and agencies, other government services. 1. Non-hydrocarbon: Goods Product and Market Concentration (Herfindahl-Hirschman Index, 2023) Figure 3. GCC and CCA Exports and Imports: Product"
  },
  {
    "figure_id": "F136",
    "report_id": "R006",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The GCC's and the CCA's growing non-hydrocarbon trade (goods and services) is relatively well diversified, which bodes well in the current environment. The GCC is typically more diversified than the CCA in terms of non-hydrocarbon trade, both in terms of produ"
  },
  {
    "figure_id": "F137",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Share of GCC-CCA Trade 1. Non-hydrocarbon Trade between GCC and CCA (Percent of non-hydrocarbon exports) 2. Services Exports between GCC and CCA (Percent of total exports) Sources: BACI (Base pour l'Analyse du Commerce International) database from th"
  },
  {
    "figure_id": "F138",
    "report_id": "R006",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sources: BACI (Base pour l'Analyse du Commerce International) database from the Centre d'Études Prospectives et d'Informations Internationales (CEPII); WTO-OECD Balanced Trade in Services dataset; and IMF staff calculations. Note: CCA = Caucasus and Central As"
  },
  {
    "figure_id": "F139",
    "report_id": "R006",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: CCA = Caucasus and Central Asia; GCC = Gulf Cooperation Council. Figure 5. Structure of GCC and CCA Imports 1. Structure of GCC Imports by Regions (Percent of non-hydrocarbon imports, . Structure of CCA Imports by Regions (Percent of non-hydrocarbon impo"
  },
  {
    "figure_id": "F140",
    "report_id": "R006",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "2. Structure of CCA Imports by Regions (Percent of non-hydrocarbon imports, . GCC: Structure of Services Imports by Regions (Percent of total exports, . CCA: Structure of Services Imports by Regions (Percent of total exports, 2019-23) Sources: BACI (Base pour "
  },
  {
    "figure_id": "F141",
    "report_id": "R006",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Note: CCA = Caucasus and Central Asia; GCC = Gulf Cooperation Council. ## B. Capital and Financial Flows The GCC and the CCA have complementary external investment dynamics. By typically registering current account surpluses, the GCC is a net provider of finan"
  },
  {
    "figure_id": "F142",
    "report_id": "R006",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "The GCC and the CCA have complementary external investment dynamics. By typically registering current account surpluses, the GCC is a net provider of financing to the rest of the world. In contrast, the CCA region is a net recipient of financial flows from the"
  },
  {
    "figure_id": "F143",
    "report_id": "R006",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Sources: World Economic Outlook; and IMF staff calculations. Note: Data in both charts are presented on net basis following BPM5 definitions. AEs = advanced economies; CCA = Caucasus and Central Asia; EMs = emerging markets; FDI = foreign direct investment; GC"
  },
  {
    "figure_id": "F144",
    "report_id": "R006",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "FDI inflows to the CCA have shifted from resource-driven investments dominated by Kazakhstan to a more diversified and regionally balanced landscape. Before the pandemic, Kazakhstan attracted the bulk of FDI, particularly in upstream hydrocarbon activities (UN"
  },
  {
    "figure_id": "F145",
    "report_id": "R006",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8. GCC Investments in the CCA 1. Announced and Actual Cumulative GCC Investments in the CCA per Economic Activity (2015-23) (US\\$ million) 2. Announced and Realized GCC Investments in the CCA (US\\$ million) Sources: fDi Markets; and IMF staff calculatio"
  },
  {
    "figure_id": "F146",
    "report_id": "R006",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9. Tariffs ## 3. Trade and Investment Enabling Environment Economic ties can be facilitated or impeded by several factors. In addition to exogenous considerations (such as distance between countries, cultural proximity, and landlocked status), trade can"
  },
  {
    "figure_id": "F147",
    "report_id": "R006",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Economic ties can be facilitated or impeded by several factors. In addition to exogenous considerations (such as distance between countries, cultural proximity, and landlocked status), trade can be affected by policy-dependent factors including tariffs and NTM"
  },
  {
    "figure_id": "F148",
    "report_id": "R006",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Sources: World Integrated Trade Solution (WITS); and IMF staff calculations. Note: AEs = advanced economies; CCA = Caucasus and Central Asia; EMDEs = emerging market and developing economies; GCC = Gulf Cooperation Council. NTMs typically have a negative impac"
  },
  {
    "figure_id": "F149",
    "report_id": "R006",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10. NTMs by Region and Type (Latest year, median number by region) Sources: UNCTAD TRAINS database; World Bank Logistics Performance Index; and IMF staff calculations. Note: This includes the average number of bilateral NTMs and NTMs applied to all coun"
  },
  {
    "figure_id": "F150",
    "report_id": "R006",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Note: This includes the average number of bilateral NTMs and NTMs applied to all countries. Border NTMs are defined as in Nicita and Koloskova (2025). Border NTMs focus on measures applied at the border, which include customs controls, quota licensing, pre-shi"
  },
  {
    "figure_id": "F151",
    "report_id": "R006",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "NTMs have been under growing scrutiny because of their potential dual objectives and increased use. NTMs can not only be used to improve social welfare (for example, protecting human health) but also be used as protectionist measures. The growing use of NTMs h"
  },
  {
    "figure_id": "F152",
    "report_id": "R006",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12. Logistics Performance Index (Latest data available; 1 = low to 5 = high) Sources: World Bank Logistics Performance Index; and IMF staff calculations. Note: AEs = advanced economies; CCA = Caucasus and Central Asia; EMDEs = emerging market and develo"
  },
  {
    "figure_id": "F153",
    "report_id": "R006",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "In logistics, infrastructure, and trade facilitation, GCC performs at a level comparable to AEs, while the CCA is closer to the EMDE median (Figure 12). GCC countries have a Logistics Performance Index (LPI) $^{10}$ similar to AEs. CCA countries have less favo"
  },
  {
    "figure_id": "F154",
    "report_id": "R006",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "(2022; 1 = burdensome to 7 = not burdensome) Figure 14. Governance Performance Index (Average 2019-23, range 0-5) Note: The index is a simple average of the following governance indices: rule of law, government effectiveness, control of corruption, and regulat"
  },
  {
    "figure_id": "F155",
    "report_id": "R006",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15. Regulatory Burden Sources: Fraser Institute; and IMF staff calculations. Note: Data for Turkmenistan and Uzbekistan are unavailable. AEs = advanced economies; CCA = Caucasus and Central Asia; EMDEs = emerging market and developing economies; GCC = G"
  },
  {
    "figure_id": "F156",
    "report_id": "R006",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16. Financial Regulations (Average 2018-22) Figure 17. Labor Market (Average 2018-22) Note: Data for Turkmenistan and Uzbekistan are unavailable. Data labels in the figure use International Organization for Standardization (ISO) country codes. AEs = adv"
  },
  {
    "figure_id": "F157",
    "report_id": "R006",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "The GCC and CCA labor market regulatory frameworks are broadly in line with AEs (Figure 17). The index incorporates both regulatory aspects—such as minimum wage policies, hiring and firing regulations, and centralized wage determination—and indicators of human"
  },
  {
    "figure_id": "F158",
    "report_id": "R006",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Sources: Fraser Institute; World Bank; and IMF staff calculations. Note: Data for Turkmenistan and Uzbekistan are unavailable. Data labels in the figure use International Organization for Standardization (ISO) country codes. AEs = advanced economies; EMs = eme"
  },
  {
    "figure_id": "F159",
    "report_id": "R006",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19. Trade Policy (Average 2018-22) Sources: Fraser Institute; and IMF staff calculations. Note: Data for Turkmenistan and Uzbekistan are unavailable. Data labels in the figure use International Organization for Standardization (ISO) country codes. AEs ="
  },
  {
    "figure_id": "F160",
    "report_id": "R006",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "2004). To examine this, we construct the state footprint index, a composite of government consumption, government investments, and state ownership in the economy. This measure pertains to the state's direct involvement in the economy rather than its control th"
  },
  {
    "figure_id": "F161",
    "report_id": "R006",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Sources: BACI (Base pour l'Analyse du Commerce International) database from the Centre d'Études Prospectives et d'Informations Internationales (CEPII); UNCTAD Investment Hub; and IMF staff calculations. Note: AEs = advanced economies; CCA = Caucasus and Centra"
  },
  {
    "figure_id": "F162",
    "report_id": "R006",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "2. Forward Participation in GVCs (Average 2010-20) In the current external environment, strengthening existing value chains and developing more robust ones, between the GCC and the CCA, could help safeguard growth and resilience. $^{18}$ The expansion of GVCs "
  },
  {
    "figure_id": "F163",
    "report_id": "R006",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Sources: EORA Global Supply Chain Database; and IMF staff calculations. Note: Data labels in the figure use International Organization for Standardization (ISO) country codes. AEs = advanced economies; CCA = Caucasus and Central Asia; EMMIs = emerging markets "
  },
  {
    "figure_id": "F164",
    "report_id": "R006",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "SEZs have had mixed results in promoting GVCs, supporting industrialization, and attracting FDI (UNCTAD 2019). In some cases, SEZs could possibly be useful if market failures and uneven reforms lead to malfunctioning land market, inadequate infrastructure, and"
  },
  {
    "figure_id": "F165",
    "report_id": "R006",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Sources: UNCTAD 2019; and IMF staff calculations. Note: CCA = Caucasus and Central Asia; GCC = Gulf Cooperation Council. Figure 24. Made or Received a Digital Payment (% Age 15+) (Percent) Sources: World Bank, Global Findex Database; and IMF staff calculations"
  },
  {
    "figure_id": "F166",
    "report_id": "R006",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "This section presents the results of empirical models for trade in goods, trade in services, and FDI. They shed light on key determinants of these flows and offer clues on what policies and actions are needed to improve trade and FDI outcomes. The gravity mode"
  },
  {
    "figure_id": "F167",
    "report_id": "R006",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Note: NTM = nontariff measure. Figure 26. Impact on Bilateral Trade in Goods (Percentage point) 1. Trade Agreement 2. Selected Policies (10 percent change) Policy priorities to improve trade differ between the GCC and the CCA. $^{26}$ This reflects the fact th"
  },
  {
    "figure_id": "F168",
    "report_id": "R006",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26. Impact on Bilateral Trade in Goods (Percentage point) 1. Trade Agreement 2. Selected Policies (10 percent change) Policy priorities to improve trade differ between the GCC and the CCA. $^{26}$ This reflects the fact that the policy gaps are very dif"
  },
  {
    "figure_id": "F169",
    "report_id": "R006",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "\\- GCC and CCA countries should review their NTMs. NTMs likely have a significant impact on prices and trade volumes (see Box 2), even if the results on nominal trade indicate a limited impact. Countries should revisit their NTMs and improve trade facilitation"
  },
  {
    "figure_id": "F170",
    "report_id": "R006",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "A gravity model is estimated to assess the performance of bilateral trade in services and its drivers. The findings are broadly in line with those for trade in goods. The results show that a trade agreement is associated with higher bilateral trade in services"
  },
  {
    "figure_id": "F171",
    "report_id": "R006",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "IMF staff estimates suggest that domestic GDP growth and trade openness are the most robust and statistically significant macroeconomic drivers of the FDI. A 1-percentage-point increase in GDP growth is associated with an increase in FDI inflows of approximate"
  },
  {
    "figure_id": "F172",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "# Annex 1. Facilitating Cross-Border Payments (XBPs) between the Gulf Cooperation Council (GCC) and the Caucasus and Central Asia (CCA) XBPs are indispensable for facilitating international trade and capital flows. Although XBPs build upon domestic payment sys"
  },
  {
    "figure_id": "F173",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "■ Weak competition: There are significant barriers to entry for nonbank service providers seeking to provide XBP services. It is also difficult for end users making payments to accurately assess the cost of initiating a payment, which makes it difficult to gau"
  },
  {
    "figure_id": "F174",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Annex Figure 1.2. Financial Development in GCC and CCA 1. Financial Institutions and Markets Development (Index level, 0-1, simple averages) 2. Bank's State Ownership Prevalence, Sovereign-Bank Nexus, and Profitability (Percent; medians; 2022) Sources: Fitc"
  },
  {
    "figure_id": "F175",
    "report_id": "R006",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：不是缺贸易意愿，是政策卡住了，IMF看海湾与中亚合作｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F176",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- A section on the Argentine NCP, its role in promoting and implementing the Guidelines, and an overview of its promotional activities (also available in English) \\- A section on the submission of specific instances to the NCP, including the NCP's case-handli"
  },
  {
    "figure_id": "F177",
    "report_id": "R007",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "• Section III: processing of the specific instance (Articles 12-25) • Section IV: confidentiality (Article 26). The NCP includes an infographic on the case-handling process within a promotional guide on the Argentine NCP, available in Spanish only on its websi"
  },
  {
    "figure_id": "F178",
    "report_id": "R007",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：经合组织支招阿根廷，NCP重建信任需先修复基础｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F179",
    "report_id": "R008",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：AI与半导体驱动全球FDI，但发展中国家被落下｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F180",
    "report_id": "R009",
    "label": "世界贸易组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界贸易组织｜世界贸易组织：光伏电池到绿氢电解槽，环境产品贸易壁垒被逐一梳理｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F181",
    "report_id": "R010",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：生鲜供应链的瓶颈不是技术，而是组织协同｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F182",
    "report_id": "R011",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：超市SKU不是太少，而是太多，减20%反增销售额｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F183",
    "report_id": "R012",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "A SK MOST INDUSTRY EXECUTIVES about the prospects for online grocery shopping, and you'll encounter hesitancy, if not skepticism. Ask consumers—especially younger, more affluent consumers and families—and they'll tell you that they are excited by the idea. The"
  },
  {
    "figure_id": "F184",
    "report_id": "R012",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "## Don't Wait Our research indicates that there's plenty of pent-up demand in major markets, even after factoring in the tendency of respondents in surveys such as this one to overstate demand. Consumers in the countries we surveyed said that they would expect"
  },
  {
    "figure_id": "F185",
    "report_id": "R012",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "Our research indicates that there's plenty of pent-up demand in major markets, even after factoring in the tendency of respondents in surveys such as this one to overstate demand. Consumers in the countries we surveyed said that they would expect to use an onl"
  },
  {
    "figure_id": "F186",
    "report_id": "R012",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "Consumers in the countries we surveyed said that they would expect to use an online grocery service offering either a click-and-collect option or home delivery an average of 13.5 times a year—more than once a month. In some markets, such as Brazil and China, c"
  },
  {
    "figure_id": "F187",
    "report_id": "R012",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "## Target Affordable Differentiation Product Range and Quality. Most online grocers will need to find the right tradeoff between offering an attractive range of products and providing fast delivery. Because consumers like choice, adding variety normally boosts"
  },
  {
    "figure_id": "F188",
    "report_id": "R012",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Satisfaction is an ongoing challenge, however. Established players spend two to three times more on retaining customers than on attracting new ones. The once linear route through the classic purchasing funnel has morphed into a fluid and dynamic process; the p"
  },
  {
    "figure_id": "F189",
    "report_id": "R012",
    "label": "EXHIBIT 5",
    "figure_type": "source_exhibit",
    "context": "can provide higher service levels. National warehouses in larger countries supported by regional spokes, in our view, come with prohibitively high delivery costs. Whatever the model, a strong link between the online operation and the company's existing supply "
  },
  {
    "figure_id": "F190",
    "report_id": "R012",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：年轻家庭线上杂货消费比线下高30%至50%｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F191",
    "report_id": "R013",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1 - The Impact of Improving Pricing Capabilities With AI-powered solutions, retailers can translate their strategic choices into optimal prices for each product and store. They can respond dynamically to both internal and"
  },
  {
    "figure_id": "F192",
    "report_id": "R013",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2 - AI-Powered Engines Embrace the Full Complexity of Retail Pricing The dimensions of an AI-powered approach to pricing fall into three categories: strategic, hygienic, and dynamic. AI-powered solutions can iterate throug"
  },
  {
    "figure_id": "F193",
    "report_id": "R013",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：AI定价不是选择题，是零售商的生存题｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F194",
    "report_id": "R014",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "As we look at the overall rise of discount and other formats in the US, the correlation is clear: traditional supermarkets are in decline, and channels that rely more heavily on private brands are gaining share. Private brands used to be nothing more than lowe"
  },
  {
    "figure_id": "F195",
    "report_id": "R014",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "CONSUMERS ARE SHIFTING FROM SUPERMARKETS TO WHOLESALE CLUB, CONVENIENCE, OR DISCOUNT STORES Sources: Planet Retail; Nielsen/PLMA 2018 Yearbook; BCG analysis. THE SHARE OF PRIVATE-LABEL PRODUCTS IS GROWING AT MASS, CLUB, AND DISCOUNT STORES AS CONSUMERS SEEK DI"
  },
  {
    "figure_id": "F196",
    "report_id": "R014",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "\\- Texas retailer HEB has become a destination for innovative private-label products, which now make up 28% of its online sales. The company even promoted its brand during the 2019 Super Bowl. \\- In Europe, Tesco and Carrefour have formed a buying alliance to "
  },
  {
    "figure_id": "F197",
    "report_id": "R014",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：自有品牌不是平替，而是零售商核心竞争力｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F198",
    "report_id": "R015",
    "label": "麦肯锡视觉摘要 1",
    "figure_type": "external_card",
    "context": "麦肯锡｜麦肯锡：AI匹配工具正改写技能培训与就业市场规则｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]