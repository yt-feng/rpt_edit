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
  "投行/券商": 86,
  "战略咨询": 6,
  "智库/国际机构": 4
}

报告摘要：
[
  {
    "id": "R001",
    "title": "Bernstein：AI基础设施新受益者并非GPU，而是CPU与内存接口芯片",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：AI基础设施新受益者并非GPU，而是CPU与内存接口芯片\n\n当市场还在讨论AI资本开支的走向时，一份来自Bernstein的深度报告提出了一个反直觉的判断：AI的下一个结构性受益者不是GPU，而是CPU，以及连接CPU与内存的那块接口芯片。报告的核心结论是，全球内存接口芯片的可触达市场（TAM）到2030年将达到200亿美元，是此前预测的3倍，复合年增长率从32%跳升至65%。这个数字背后，是三个相互强化的驱动力：服务器CPU出货量的结构性增长、单颗CPU搭载的DRAM模组数量增加，以及MRDIMM升级带来的单模组接口芯片价值量跃升。\n\n这份报告的价值不在于简单的“看好”，而在于它提供了一个理解AI基础设施演进的新框架。当AI从训练走向推理，再走向自主智能体（Agentic AI），计算模式正在发生根本性转变。训练阶段是GPU的天下，但推理和智能体任务——尤其是那些需要多步骤、序列化、低延迟响应的任务——CPU重新成为核心。Bernstein估算，在智能体架构中，CPU与GPU的比例可以达到1:1至1:2，远高于当前训练集群中的1:8甚至更低。AMD最近将其对全球x86服务器CPU TAM的预测弹性较高至1200亿美元，恰恰印证了这一趋势。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三股驱动力叠加，TAM的爆发不是线性而是指数级\n\nBernstein的TAM模型建立在三个独立且可验证的驱动力之上。首先是服务器CPU出货量的加速增长。报告引用了一个关键数据点：在智能体工作负载中，CPU侧处理可以占到任务完成时间的50%到90%。这意味着数据中心需要部署更多的CPU服务器，而不是简单地增加GPU。每一颗新增的服务器CPU，都需要配套多个DDR内存模组，而每个模组都需要接口芯片。\n\n第二层驱\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 别再只盯着GPU了，CPU正在悄悄成为关键角色\n\nAI进入推理阶段，CPU开始承担更多任务\n\n某机构最新研究显示：**内存接口芯片**是Agentic AI趋势下的潜在受益方向，相关市场规模预计2030年达200亿美元，是此前预测的3倍。\n\n为什么关注它？三个逻辑拆开看👇\n\n1️⃣ **CPU需求增长，服务器配置升级**\nAI从训练转向推理，任务变为多步骤、有顺序的复杂流程。CPU作为“总协调”，调度能力不可替代。服务器CPU出货量将结构性增长，带动配套芯片需求。\n\n2️⃣ **内存容量增加，接口芯片价值提升**\n每颗CPU搭配的DRAM数量和带宽都在上升——大模型对内存需求高，CPU需配置更多内存条。每个内存条中都包含接口芯片。\n\n3️⃣ **MRDIMM升级，单颗价值提升**\n新标准MRDIMM的接口芯片价值是旧款RDIMM的10倍（1颗MRCD+10颗MDB vs 1颗RCD）。预计到2030年，MRDIMM将占全球服务器DDR出货量的25%。\n\n行业格局较为清晰：三家主要企业控制90%以上份额，客户认证周期长、替换成本高，竞争壁垒较深。\n\n短期市场有波动，但拉长到12个月，随着MRDIMM渗透率持\n\n[... middle omitted ...]\n\n428bb.jpg)\n\nFrancis Ma\n+852 2123 2626\nfrancis.ma@bernsteinsg.com\n\n![](images/d8362b6cf491b929990b128b2a1db8d0ad03cb6eae8b92634d720e2e801fc810.jpg)\n\nKai Zhang\n+852 2123 2665\nkai.zhang@bernstein\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R002",
    "title": "Bernstein：欧洲水电影响2Q26发电，唯独瑞典逆势增长",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：欧洲水电影响2Q26发电，唯独瑞典逆势增长\n\n欧洲公用事业公司正在经历一场由自然条件驱动的发电结构分化。Bernstein最新发布的2Q26欧洲发电数据追踪显示，一个清晰的趋势正在浮现：水电产量在几乎所有主要市场同比下降，而太阳能凭借新增装机继续扩张，风电表现则高度分化。这一组合对依赖水电的公用事业公司构成了直接的盈利不确定性。\n\n报告覆盖法国、德国、意大利、西班牙、葡萄牙、奥地利、英国、芬兰和瑞典九个市场。整体而言，2Q26的发电数据呈现三个特征：水电普遍走弱，太阳能靠装机增长维持上升势头，风电表现取决于地理位置和项目类型。这些变化并非短期波动，而是反映了欧洲可再生能源结构进入新阶段的信号——新增装机对发电量的贡献正在超越天气条件的影响。\n\n> **KC评论：** 这份报告的价值不在于罗列发电数据，而在于揭示了“装机增长”与“实际出力”之间的剪刀差。对于读者来说，需要区分哪些公司受益于确定性装机扩张，哪些仍暴露在天气不确定性之下。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 水电产量普降，伊比利亚半岛与意大利受创最深\n\n葡萄牙2Q26水电产量同比下降42.7%，西班牙下降27.2%，意大利下降25.1%。即便是法国和德国，也分别录得2.4%和0.4%的同比下滑。相对少见实现正增长的是瑞典，产量微增2.6%。\n\n报告指出，西班牙和葡萄牙的同比降幅部分归因于2025年的高基数效应，但即便如此，这一降幅仍然显著。水库蓄水水平的变化同样令人关注：葡萄牙和西班牙的蓄水率分别下降8.5%和1.9%，而意大利的蓄水率反而上升11.8%，暗示其产量下降更多来自来水条件而非蓄水能力。\n\n对公用事业公司而言，这意味着直接的收入冲击。Bernstein明确列出受影响的公司：意大利的Enel、西班牙和葡萄牙的\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n欧洲水电发电量变化观察，部分公司受影响\n\n欧洲水电整体表现出现波动\n\n近期一份研究资料梳理了欧洲2Q26发电数据，主要发现：多数国家水电发电量有所下降，仅瑞典例外。\n\n1️⃣ 水电降幅情况\n- 葡萄牙：产量-42.7%，库存-8.5%\n- 西班牙：-27.2%，库存-1.9%\n- 意大利：-25.1%\n- 芬兰：-14.8%\n- 奥地利：-10.9%（含抽水蓄能）\n- 法国：-2.4%，库存-7.2%\n- 德国：-0.4%（含抽水蓄能）\n- 瑞典：逆势+2.6%，但库存-21.3%\n\n2️⃣ 风电表现分化\n- 海上风电：法国+22.1%、德国+1.3%（受新增装机影响）\n- 陆上风电：德国-12%、法国-5.9%、葡萄牙-5.4%、西班牙-0.6%\n- 英国+7.3%、意大利+4.8%、芬兰+2.4%、瑞典+1.9%\n\n3️⃣ 太阳能全线增长\n- 奥地利+27.4%、西班牙+22.3%、法国+19%、葡萄牙+16.8%、德国+6.9%、英国+6.2%、意大利+4.5%\n- 主要受新增装机推动，负荷因子有所下降\n\n4️⃣ 哪些公司受影响较大？\n- Enel：意大利水电减产\n- Iberdrola、EDP、Eng\n\n[... middle omitted ...]\n\nbartlomiej.kubicki@bernsteinsg.com\n\nThibault Dujardin, CFA\n+33 1 58 98 59 16\nthibault.dujardin@bernsteinsg.com\n\nJorge Alonso Suils\n+34 915 893 913\njorge.alonso@bernsteinsg.com\n\nRory Graham-Wa\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R003",
    "title": "Bernstein：裂解价差创纪录，原油现货与成品油价格背离达20美元",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：裂解价差创纪录，原油现货与成品油价格背离达20美元\n\n原油价格在每桶70美元以下徘徊，但消费者在加油站支付的价格却已大幅上涨。这种“输入”与“输出”之间的巨大裂口，构成了当前全球能源市场最值得关注的定价矛盾。Bernstein一份最新研报指出，基于汽油和柴油价格反向推导出的隐含原油价格已超过每桶90美元，比当前现货价格高出逾20美元。这一价差已达到该机构有记录以来的最高水平。\n\n裂解价差，即原油提炼为成品油后的收入与原料成本之差，长期以来呈现规律性。Bernstein分析师发现，在页岩油革命之前，裂解价差约为油价的20%；而在过去十余年间，这一比例已稳定上升至33%左右。基于这一稳定的比例关系，可以从成品油价格反推出原油的“合理”价格。模型显示，当前实际的原油价格显著低于模型隐含水平，偏离程度为历史之最。\n\n> **KC评论：** 这份研报的核心贡献不是预测油价，而是提供了一个观察框架——裂解价差是理解炼油环节利润和油价错位的重要工具。真正值得关注的不是油价本身，而是这种价差何时以及如何收敛。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 价差背离背后，不仅有供应链扰动，还有库存行为的结构性扭曲\n\n俄乌冲突后，成品油供应链一度受阻，裂解价差随之走高。但Bernstein认为，单靠供应链扰动无法解释当前价差的极端程度。更关键的因素在于战略石油储备的释放行为。报告指出，商业库存数据往往被市场定价所反映，而战略储备的变动则被定价机制“忽视”。美国等国的战略储备释放，在压低原油现货价格的同时，并未同步压低成品油价格，人为制造了价差裂口。\n\n这种扭曲并非永久性。报告判断，通过物理释放或口头干预压低原油价格的能力存在时效性。一旦各国开始重建战略储备，将在每桶60美元附近形成需求支撑——这恰好接近当前价\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n原油价格与成品价价差处于历史高位\n\n**原油价格与成品价价差处于历史高位**\n\n**裂解价差隐含的油价已超90美元/桶**\n\n原油本身几乎没什么用，但炼出来的汽油和柴油才是全球宏观环境的重要燃料。今天想分享一个研究机构报告里的核心观察：当前原油价格（约70美元/桶）与成品油价格之间存在**历史级别的价差**。\n\n1/ 裂解价差（Crack Spread）是衡量炼油利润的关键指标，简单说就是用2桶汽油+1桶柴油的收入，减去3桶原油的成本。传统上，这个价差约占油价的20%，而近十年来已升至33%左右。\n\n2/ 基于这个规律，报告用汽油和柴油价格反推出“隐含油价”。模型显示，当前隐含油价已超过**90美元/桶**，而实际油价却低于70美元/桶，差值达20+美元，创下历史记录。\n\n3/ 为什么会出现这种价差？报告分析认为：相关方面释放战略石油储备（SPR）影响了商业库存数据，同时一些短期措施也在影响价格。但这些因素不具持久性，未来相关方面重建储备的需求反而可能为价格提供一定支撑。\n\n4/ 对于拥有炼油业务的综合油企，这种价差意味着一定的利润空间。报告提到，裂解价差在供应冲击（如地缘事件）后可以维持数年高位。\n\n5/ \n\n[... middle omitted ...]\n\ns >\\$90/bbl\n\nOil is useless for the most part. As a product, it has little utility in its raw state. However, oil is not worthless. It has a price which today sits below \\$70/bbl (up perhaps 2\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R004",
    "title": "Bernstein：香奈儿新品率67%领跑，但奢侈品定价权靠的不是上新数量",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：香奈儿新品率67%领跑，但奢侈品定价权靠的不是上新数量\n\n奢侈品行业正在经历一场静默的分化。当大多数头部品牌在2季度继续执行低单位数提价时，Gucci却反其道而行——对SS26系列Mercato托特包进行了20%-25%的全球降价。Bernstein最新发布的《手袋价格与组合晴雨表》追踪了这一变化，并给出了一个值得深思的判断：Gucci的降价并非主动选择，而是品牌吸引力尚未恢复的被动结果。\n\n这份报告的核心价值不在于罗列价格变动，而在于它揭示了奢侈品行业当前最根本的竞争逻辑——当“新意”成为相对少见稀缺品时，谁能持续创造产品新鲜感，谁才能维持定价权。Bernstein的追踪数据显示，不同品牌在“上新率”上的差距，正在转化为实际的价格组合表现。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 香奈儿的新品率远超同行，但真正的挑战在于如何把“新”转化为“价”\n\nBernstein的“新品率”追踪器显示，2季度香奈儿以67%的SKU更新率领跑，普拉达以52%紧随其后，古驰51%位列第三。而迪奥和博柏利的新品率分别降至39%和37%，相对落后。\n\n但“上新率”高并不自动等于定价能力强。同一份报告的价格组合数据显示，香奈儿在法国和英国的“同店价格变化”仅为0.6%和0.9%，虽然高于多数品牌，但远谈不上激进。真正让香奈儿脱颖而出的是其“隐含组合变化”——在法国录得1.1%的正向组合提升，在英国达到2.3%。这意味着香奈儿不仅推出了更多新品，还推出了更高价位的新品。\n\n> **KC评论：** 香奈儿的案例说明，在奢侈品行业，“上新”和“上价”是两件事。真正决定品牌定价能力的，不是新品数量的相对值，而是新品在价格带上的分布。香奈儿的新品集中在高端价位，而普拉达的新品则集中在价格带的底部——这解释了为什么后\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n奢侈品牌包袋动态观察：哪些品牌在调整价格\n\n奢侈品手袋价格趋势观察\n\nChanel新品占比67%领先，Gucci则出现价格调整\n\n近期某机构发布了一份关于奢侈品手袋的追踪报告，以下为其中的核心信息整理👇\n\n1️⃣ 哪些品牌上新较多？\n- Chanel：2Q26新品占比67%，5-6月集中上新（Métiers d'Art系列）\n- Prada：52%新品集中在较低价位段\n- Gucci：51%新品占比，但走的是\"实验性\"路线\n- Dior和Burberry新品占比放缓，分别为39%和37%\n\n2️⃣ Gucci的价格调整\n- Mercato托特包全球价格下调20%-25%（小号从€2600调整为€1950）\n- 这是Gucci主动调整价格架构的信号\n- 整体手袋组合均价环比下降中到高个位数\n- 新创意总监采取\"先发布后销售\"策略，参考Moncler的Genius模式\n\n3️⃣ 其他品牌在做什么？\n- 大部分品牌做了低个位数价格上调\n- 只有Dior保持价格不变\n- Chanel小幅价格上调并优化正价产品组合\n- Saint Laurent和Burberry都在价格上调并优化产品组合\n\n4️⃣ 关键观察\nGucc\n\n[... middle omitted ...]\n\n6bc4d129fef837ddc7bf5dfa0294.jpg)\n\nEric Chen, CFA\n\n+852 2123 2628\n\neric.chen@bernsteinsg.com\n\nSpecialist Sales\n\n![](images/6afe8f4abe201a5464c26c6c5c69159886901fae7ce0cabc5c3ba1098a615ec2.jpg)\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R005",
    "title": "Bernstein：现金流修复才是真正拐点，Bernstein拆解防务股自证能力",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：现金流修复才是真正拐点，Bernstein拆解防务股自证能力\n\n欧洲防务板块过去一年经历了从集体飙升到剧烈分化的转折。Bernstein在最新发布的Q2'26前瞻报告中给出一个清晰判断：板块普涨阶段已经结束，公司将根据自身执行力、订单可见度和业务结构进入分化行情。报告重点覆盖了六家公司，但核心信号只有一个——在宏观叙事让位于公司基本面的窗口期，拥有“自证”能力的标的将跑赢。\n\n这份报告发布的时间点值得注意。欧洲防务股自2025年初以来波动剧烈，多数标的的估值已回落到2026年初的水平。市场不再满足于“国防开支上升”的宏大逻辑，而是开始追问：哪家公司真正把订单转化成了利润，谁的现金流在改善，谁的业务组合能抵御“新战争形态”的叙事冲击。\n\n**KC评论：** Bernstein的核心框架其实是一个经典的“从beta到alpha”切换。当行业整体估值不再便宜，资金就会从买赛道变成买选手。这份报告的价值在于，它给出了一个可验证的筛选逻辑——关注那些不需要依赖宏观假设、靠自身经营就能实现盈利超预期的公司。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 莱昂纳多：管理层更迭后的“自证”机会\n\n在所有覆盖标的中，Bernstein对莱昂纳多的战术偏好最高。核心逻辑不是订单暴增，而是“连续超预期并上调指引”的能力。报告预计其二季度EBITA将高出市场共识5%，且现金流改善明显。更重要的是，公司业务组合偏重电子、导弹和防空系统，在当前“新战争形态”叙事下防御性更强。\n\n一个意外的催化剂是CEO更迭。前CEO Cingolani自2023年起主导了公司的扭亏为盈，但他的背景是科学家和政治家。接任的Mariani在莱昂纳多和MBDA工作超过20年，更熟悉核心业务。Bernstein认为，这一变化虽然短期引发报价\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n欧洲防务相关公司，哪些值得持续观察？\n\n欧洲防务板块进入分化阶段\n\n2026年第二季度，这几家值得留意\n\n---\n\n1️⃣ **Leonardo：内生动力较强**\n- 预计Q2延续此前趋势，EBITA比市场预期高5%\n- 自由现金流改善，各业务线表现均衡\n- 估值约11倍EBITDA（行业均值14倍），管理层调整后的市场反应可视为观察窗口\n- 新任CEO来自MBDA，战略方向保持连贯\n\n2️⃣ **Thales：战术性拐点或已临近**\n- 核心航空航天与防务业务表现稳健，我们比市场预期高6%\n- 此前拖累的网络安全业务占比仅8%，Q2有望恢复增长\n- 收购Exail（28倍EV/EBIT）战略方向明确，但短期财务贡献有限\n- F126项目取消影响已被消化，一次性非现金损失约4.5亿欧元\n\n3️⃣ **Rheinmetall：增速领先但需验证**\n- Q2是实现收入增长60%指引的关键阶段\n- Arminius Boxer订单是下一个关注点\n- 我们对2030年EBIT的预期比市场共识低18%，但当前风险回报比值得关注\n\n4️⃣ **Dassault：等待印度订单落地**\n- 上半年因Falcon交付偏弱，但市\n\n[... middle omitted ...]\n\n7e7f3b621a942cb84d72a6227a91465f12879a503dda2e.jpg)\n\nJames Brady\n\n+44 20 7762 5272\n\njames.brady@bernsteinsg.com\n\nEuropean Defense stocks are decoupling after a period of broad performance. Ahe\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "Bernstein：印度信贷增长18%韧性显现，Bernstein称宏观担忧被高估",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：印度信贷增长18%韧性显现，Bernstein称宏观担忧被高估\n\n印度银行业正在进入2027财年第一季度的财报季，宏观担忧仍然主导市场情绪，但Bernstein这份最新研报给出了一个与市场普遍叙事不太一样的判断：运营基本面比市场担心的要稳健，增长、利润率与资产质量的韧性正在将焦点从宏观不确定性转向公司层面的执行能力。\n\n报告的核心信号很清晰——外部不确定性在边际上正在缓解，而银行自身的基本面修复比多数读者预期的要快。这不是一个全面反转的故事，而是一个“坏消息已被定价、好消息正在积累”的窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 宏观不确定性在边际上被高估了\n\n印度宏观环境在FY26实现了7.7%的实际GDP增长，通胀控制在4%目标附近，财政轨迹符合历史季节性规律。市场最担心的几个外部不确定性——贸易逆差、外资流出、地缘不确定性——在近期都出现了边际改善。\n\n尤其值得关注的是，中东停火协议触发了一轮固定收益市场的反弹，12个月CD利率从此前冲突高峰水平下降了超过100个基点。这直接降低了银行的融资成本，缓解了市场对流动性收紧的担忧。\n\n> **KC评论：** 市场往往把宏观不确定性线性外推，但Bernstein提醒读者注意边际变化。CD利率下降100bps这件事，对银行净息差的支撑可能比很多分析师预期的更直接。完整报告里有详尽的图表对比，值得细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 银行信贷增长保持韧性，结构分化正在收窄\n\n系统信贷增速维持在约18%的同比水平，支撑来自工业、服务业和抵押贷款等领域的广泛复苏。值得注意的是，个人贷款中的无担保部分仍然仍在调整——信用卡债务增速不到2%，但整体信贷组合的多元化正在吸收这部分不确定\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n印度银行业：关注这些关键指标\n\n📊 银行基本面依然稳健\n\n印度银行业即将进入FY27Q1财报季，宏观层面的关注仍是市场主导情绪，但运营基本面比预期更为稳定。增长、息差、资产质量均保持支撑，焦点正转向个股的执行力和盈利持续性。\n\n**宏观环境边际改善**\n- 印度FY26实际GDP增长7.7%，通胀回落至4%目标附近\n- 贸易逆差虽高，但服务贸易顺差和RBI措施在缓解外部影响\n- 西雅停火后，12个月CD利率下降超100bps，融资成本明显改善\n\n**银行核心指标**\n1️⃣ 信贷增长依然强劲，系统贷款同比增速约18%，工业、服务业和担保零售贷款全面发力\n2️⃣ 息差压力可控——贷存利差在扩大，存款结构改善\n3️⃣ 资产质量保持良性，未见明显恶化信号\n\n**关键个股关注点**\n- HDFC Bank：贷款和存款增长能否转化为净利息收入增长\n- ICICI Bank：信贷成本正常化后，ROA能否持续改善\n- Axis Bank：估值重估后，息差和信贷成本走势\n- Kotak：增长放缓和管理层过渡期，如何守住息差\n- SBI：增长势头和ROA能否持续\n- IndusInd：信贷成本改善和ROA回升\n- Bajaj \n\n[... middle omitted ...]\n\noperating fundamentals remain resilient. Recent trends suggest growth, margins and asset quality are holding up better than feared, shifting the focus toward company-specific execution and the\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R007",
    "title": "BofA：AI蚕食创意软件护城河，Adobe的低估值是机会还是陷阱",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "BofA",
    "digest": "[wechat_article.md]\n# BofA：AI蚕食创意软件护城河，Adobe的低估值是机会还是陷阱\n\n市场对Adobe的定价已经反映了悲观预期——报价从2024年高点下跌约70%，当前估值位于历史低位。但BofA一份最新研报提出了一个更尖锐的问题：如果AI带来的不是短期扰动，而是结构性替代，那么Adobe当前看似“便宜”的报价，是否只是价值陷阱？\n\n这份报告的核心判断是：Adobe的AI策略本质上是防御性的，难以形成可持续的高质量收入增长。而真正值得关注的，是生成式AI正在压缩创意软件的门槛，让“足够好”的替代品蚕食Adobe的核心市场。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI对Adobe的影响并非均匀分布，但低端市场的流失会侵蚀整体定价权\n\nBofA将Adobe的用户分为两个群体：专业创意与营销人员（CMP），以及商业专业与消费者（BPC）。前者贡献约71%的订阅收入，后者约29%。\n\n报告认为，不确定性是不对称的。在BPC群体中，用户对像素级控制没有执念，“足够好”的AI输出就能替代付费工作流。这部分用户最容易流失到免费的AI原生工具。而在CMP群体中，专业用户对工具深度和生态黏性有更高要求，短期内相对稳定。\n\n但问题在于，低端市场的流失会反过来压缩Adobe在高端市场的定价空间。当大量用户习惯了免费或低成本的AI工具，Adobe要维持现有订阅价格和座位数，将面临持续不确定性。\n\n> **KC评论：** 这种“从底部开始瓦解”的竞争逻辑，在软件行业并不陌生。但Adobe的特殊之处在于，它的产品本身就是行业标准。当AI让“非标准”变得足够好用，标准的价值就会被重新定价。BofA报告里有一张用户分层与不确定性矩阵图，值得仔细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. AI产品\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nAdobe的竞争壁垒，在AI时代面临新挑战\n\nAI正在影响Adobe的业务格局\n\nAdobe近期被某外资机构调整了评级，核心观点是：AI正在改变它的竞争环境。\n\n1/ AI降低了内容创作的门槛，一些价格较低甚至免费的AI工具正在吸引Adobe的用户。专业用户可能仍会留在平台，但大量普通用户可能会转向其他选择。\n\n2/ Adobe的AI产品（如Firefly等）虽然增长较快，但目前仅占总ARR不到2%，尚未形成显著的收入贡献。更值得关注的是，AI功能可能会对原有付费业务产生一定影响。\n\n3/ 增长节奏有所变化。相关研究预计收入增速从FY25的10.5%降至FY27的8.8%，短期内尚未看到明显的加速信号。\n\n4/ 从估值角度看（8x EV/FCF），当前价格似乎不算高，但缺乏明确的推动因素。CEO和CFO同时离职也增加了执行层面的不确定性。\n\n值得注意的是，Adobe的利润率依然保持在较高水平（45%+），自由现金流也较为健康。但在AI快速发展的背景下，这些优势能否持续，值得进一步观察。\n\n你怎么看Adobe在AI时代的未来？\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.m\n\n[... middle omitted ...]\n\n tools, but AI will likely displace large parts of the core market over time, with likely pressure on pricing and seat expansion. We see Adobe's own AI strategy as largely defensive, supportin\n\n[... middle omitted ...]\n\n BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies."
  },
  {
    "id": "R008",
    "title": "Bernstein：功率半导体第二增长引擎，AI电力需求下的电装并购窗口",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Bernstein",
    "digest": "[wechat_article.md]\n# Bernstein：功率半导体第二增长引擎，AI电力需求下的电装并购窗口\n\n电装对罗姆的收购要约在四月底撤回后，市场关注的焦点迅速转向这家日本汽车零部件巨头的下一步动作。Bernstein在最新研究报告中给出了一个清晰的判断：并购仍是电装实现中期增长目标最现实、最有效的路径，而在所有潜在标的中，富士电机在收购成本、产品组合和管理契合度上均最具可行性。\n\n这份报告的独特价值不在于罗列所有可能目标，而在于它建立了一个筛选框架——电装需要的不是任何半导体公司，而是一家能帮它从汽车市场跨入工业和消费电子领域的功率半导体企业。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n![研报原图 2](assets/source_image_02.jpg)\n\n![研报原图 3](assets/source_image_03.jpg)\n\n电装的半导体业务目前几乎完全服务于内部需求。据Gartner数据，其2025年半导体收入约2080亿日元，其中功率和模拟芯片占比接近90%，汽车应用占99.7%。这种高度集中的结构在电装的中期计划中被明确列为需要改变的方向——公司希望将半导体技术“扩展到工业设备和消费电子领域”。\n\n问题是，电装过去通过少数股权研究建立的合作关系，如入股英飞凌、瑞萨、安森美和罗姆，主要目的都是强化汽车业务。要真正实现跨领域扩张，仅靠现有合作远远不够。\n\nBernstein认为，电装瞄准的六个细分市场——分立器件和模拟芯片在汽车、工业、消费三大领域的组合——虽然只占全球半导体市场的5%左右，但规模可观且增长稳定：预计从2025年的500亿美元增长至2030年的800亿美元，年复合增长率约10%。更重要的是，这些市场仍有整合空间。\n\n> **KC评论：** 电装并非要在半导体领域与英伟达或三星竞争。它选择的是一个规模适中、增长可预\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n日本电装的下一个合作方向观察\n\n**电装与半导体布局**\n\n**功率器件领域的下一步可能选择**\n\n电装撤回对罗姆的提议后，市场持续关注其后续动向。从现有信息来看，通过并购或合作仍是电装实现中期目标较为可行的路径之一。\n\n1/ **电装的半导体业务现状**\n- 产品几乎全部自用，主要聚焦功率与模拟芯片（Si-IGBT、SiC、电池管理ASIC）\n- 功率器件占营收74%，ASIC占16%\n- 99.7%依赖汽车市场，工业与消费领域几乎空白\n- 中期计划明确希望拓展至工业和消费电子领域\n\n2/ **目标市场具有一定吸引力**\n- 电装关注的6个细分赛道（离散/模拟 × 汽车/工业/消费）\n- 2025年市场规模约500亿美元，2030年预计达800亿美元\n- 年复合增长率约10%，市场空间较大且集中度较低\n\n3/ **哪些选择较为可行？**\n- 较受关注：富士电机（市值约2万亿日元）\n  - 与电装在IGBT/SiC上有长期合作基础\n  - 工业客户基础扎实\n  - 收购成本相对可控\n- 罗姆/东芝/三菱电机联盟：部分入股存在可能，全盘收购难度较大\n- 安森美、瑞萨、英飞凌/意法半导体：从财务角度看可行性较低\n\n[... middle omitted ...]\n\n](images/fa599893e15f740bbe7df316f76b3fc9f3c6d6c50b29e6a7bfbf963c747c3afe.jpg)\n\nDavid Dai, CFA\n+852 2918 5704\ndavid.dai@bernsteinsg.com\n\nTomohiro Kashimoto\n+81 3 6777 6975\ntomohiro.kashimoto@b\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "BofA：AI主题重塑资金流向，中国消费板块观察",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "BofA",
    "digest": "[wechat_article.md]\n# BofA：AI主题重塑资金流向，中国消费板块观察\n\n二季度中国市场的表现，让不少关注者感到困惑。一边是创业板和科创板分别上涨38.6%和78.6%，另一边是MSCI中国和恒生国企指数分别下跌7.6%和9.8%。这种极端的分化，不是简单的板块轮动，而是一个更深层信号：市场已经进入了一个对选股能力要求极高的阶段，传统的指数配置思路可能面临持续挑战。\n\nBofA在最新发布的季度策略报告中，用“K-shaped market”来概括这一格局。报告的核心判断是，中国市场的整体估值虽然看起来不算贵——MSCI中国当前远期市盈率10.3倍，比长期均值低12%——但这个数字并不构成观点偏积极理由。真正值得关注的，是盈利预期正在被持续下调。2026年每股盈利增长预期已从1月的11-12%降至目前的2-3%。估值便宜但盈利预期承压，两者叠加，意味着市场缺乏系统性向上的驱动力。\n\n> **KC评论：** 10.3倍的市盈率放在历史上看确实不贵，但报告提醒读者注意，这个估值水平仍高于8-9倍的历史底部。更关键的是，盈利预期下调的速度在加快。如果盈利继续走弱，当前的“便宜”可能只是暂时的。报告中的图表值得细看，它展示了盈利预测修正的轨迹，能帮助判断后续估值是否还有压缩空间。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮分化背后，是AI主题对资金流向的彻底重塑\n\n二季度最显著的特征，是AI相关产业链对资金的虹吸效应。MSCI中国中，信息技术是相对少见录得正回报的板块，涨幅36.7%。而可选消费、必选消费和原材料分别下跌20.7%、18.6%和18.3%。市值增长前十的公司全部来自科技硬件和半导体领域。这种集中度，在历史上并不多见。\n\nBofA的报告指出，AI研究主题在二季度变得更加复杂。市场在内存超级周期、CPO部署延迟、国产GP\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 市场观察：不同板块的表现差异\n\n📈 市场分化现象观察\n\n二季度中国相关市场呈现结构性分化：某综合指数/国企指数出现一定调整，但部分科技类板块表现相对活跃。人工智能主题成为重要推动因素，资金集中在科技硬件和半导体相关领域。\n\n1️⃣ 估值：处于历史区间\n\n某综合指数目前估值水平为10.3倍，低于长期均值约12%，但仍高于历史底部区域。盈利预期有所调整，未来两年的增速预期从年初的11-12%降至2-3%。部分市场面临一定的流动性因素，三季度有较大规模解禁，新股发行也较为密集。\n\n2️⃣ 宏观环境：出口表现较好，内需有待观察\n\n5月信贷增速有所放缓，固定资产投资同比下降，零售增长有限。出口是相对亮点，同比增长15.5%。工业品价格在转正后有所上升，带动工业利润增长，但持续性需关注（能源价格已回落）。政策层面保持稳健。\n\n3️⃣ 配置方向：关注工业/科技，消费/公用相对谨慎\n\n某机构三季度配置建议关注：工业（重型机械、电气设备）、科技硬件、通信设备、多元金融、金属采矿（除黄金）、化工、生命科学工具。\n相对谨慎的领域：独立发电及新能源、白酒、汽车、燃气水务、地产、生物科技、家电。\n\n整体来看，不同市场板块存在结构性\n\n[... middle omitted ...]\n\nail leverage (incl leveraged ETFs) amplified market swings. Sentiment became more fragile amid inflation and liquidity concerns. We continue to view China as a stock pickers' market, with A-sh\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R010",
    "title": "BofA：AI芯片龙头估值低于同行30%，BofA指市场误判不确定性",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "BofA",
    "digest": "[wechat_article.md]\n# BofA：AI芯片龙头估值低于同行30%，BofA指市场误判不确定性\n\nAI芯片龙头英伟达今年以来涨幅仅3%，远不及费城半导体指数82%的表现。市场在担忧什么？BofA一份7月发布的报告给出了直接判断：当前报价已经在为2027-2028年每股盈利预期打折30-35%，而这一折价缺乏依据。\n\n这份报告的核心论点不是“英伟达很好”，而是“市场已经过度悲观”。在18倍远期市盈率这个七年低点，机构看到的不是不确定性，而是定价错误。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 内存成本上涨被高估，定价权被低估\n\n读者最担心的是HBM内存成本上升挤压毛利率。从Blackwell到Rubin架构，每机柜的HBM成本确实会增加约20-30万美元。但报告指出一个容易被忽略的数字：同期单机柜定价可能从300-400万美元升至600-700万美元。\n\n这意味着什么？内存成本在机柜总成本中的占比其实变化不大——从Blackwell的5.2%微升至Rubin的6.4%。真正驱动定价上升的是Vera CPU升级、NVLink和Quantum以太网等非内存组件，以及软件功能带来的推理成本下降。\n\n> **KC评论：** 市场习惯把英伟达简单看作“卖显卡的”，但它的机柜系统里越来越多的价值来自网络、CPU和软件。只看HBM成本，就像只看发动机成本来评估一辆豪华车。完整报告里那张HBM成本占比的表格值得细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 定制芯片威胁被历史数据证伪\n\nGoogle TPU在2015年推出，亚马逊Trainium在2020年，Meta MTIA在2023年。这些定制ASIC芯片一直在“威胁”英伟达，但报告给出的数据是：英伟达的GPU加速器销售额自2015年以来增长\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 英伟达被低估？研报拆解4个关键点\n\n估值折价30-35%的AI龙头\n\n某外资机构最新研究认为，当前市场对英伟达的担忧过度，估值已隐含30-35%的盈利下调风险，但实际基本面比想象中强。\n\n1️⃣ 毛利率压力被高估\n市场担心HBM内存成本上涨挤压利润，但研报指出：从Blackwell到Rubin架构，每机架HBM成本只增加约20-30万美元，而整机定价能提升200-300万美元（从300-400万到600-700万）。原因是CPU、网络、软件等非内存部分的全面升级。预计毛利率仍维持在75%左右。\n\n2️⃣ 定制芯片威胁被夸大\nGoogle TPU（2015年）、Amazon Trainium（2020年）、Meta MTIA（2023年）都推出多年，但英伟达GPU收入自2015年增长了约700倍。向云厂商的销售额同比增长115%，几乎是云资本开支增速的2倍，说明份额还在扩大。长期看，英伟达有望维持AI资本开支65-70%+的份额。\n\n3️⃣ 估值已提前消化负面因素\n对比亚马逊、Meta、谷歌、微软、苹果这5家科技巨头，它们2027/28年PE平均为22x/19x，而英伟达只有约16x/12x，折价30-35\n\n[... middle omitted ...]\n\ncounting an unjustified \\~30-35% headwind to CY27/28 EPS ests (effectively delta between NVDA and growth peer forward PE). We strongly disagree with the EPS discount and see as an enhanced Buy\n\n[... middle omitted ...]\n\n BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies."
  },
  {
    "id": "R011",
    "title": "JPM：香港银行贷款增速回升，JPM提醒注意非利息收入基数效应",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：香港银行贷款增速回升，JPM提醒注意非利息收入基数效应\n\n当市场还在为跨境研究新规和地产不确定性担忧时，一份来自JPM的月度追踪报告给出了一组值得细看的信号：香港银行板块6月虽下跌5%，却跑赢恒生指数4个百分点。跑赢本身不稀奇，稀奇的是跑赢的逻辑——美联储偏鹰的利率立场，反而成了区域性银行的相对利好。\n\n这份报告的核心判断是：香港银行股正在经历一个从“宏观影响”到“微观分化”的转折点。不是所有银行都受益，但结构性的赢家已经浮现。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资产质量的底部信号比市场预期的更清晰\n\n报告中最值得关注的不是利润增速，而是资产质量数据。香港银行整体不良贷款率在2026年第一季度降至1.87%，这是八个季度以来的最低点。惠誉同期将香港银行业展望从“出现变化”上调至“中性”，理由是商业地产最坏阶段已经过去。\n\n更微观的指标也在印证这一趋势：3个月按揭逾期率从0.12%进一步降至0.11%，破产申请量在5个月内同比下降12%。这些数字单独看幅度不大，但方向一致——资产质量的节奏变化周期正在收窄。\n\n> **KC评论：** 不良率见顶不等于马上改善，但至少让市场少了一个“继续出现变化”的理由。对于持有银行仓位的读者，真正的观察窗口不在一两个季度的不良率波动，而是银行管理层是否愿意增加拨备——如果拨备反而开始下降，才是真正的信心信号。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 贷款增长正在悄悄加速，但结构决定赢家\n\n行业贷款增速从4月的5.4%升至5月的6.0%，延续了自2025年11月以来的回升趋势。驱动力来自贸易融资，而非地产相关贷款。按揭贷款增速虽也微升至3.3%，但新批按揭环比增长10.1%的背后，是银行间市场份额的激烈争夺。\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n港银6月表现观察，逻辑梳理\n\n封面：港银6月复盘\n封面副标题：在利率周期中如何保持相对稳定？\n\n6月港银整体回调5%，但相对市场表现有一定韧性。市场受到新规则影响，银行股则因两个因素获得支撑：经营趋势改善与外部政策表态。\n\n拆三个关键看点👇\n\n**1/ 贷款增速持续回暖**\n- 行业贷款同比增速从4月的5.4%升至5月的6.0%，贸易融资是主要推动因素\n- 按揭贷款增速也小幅上升至3.3%，新批按揭环比增10%\n- 中银香港在已完工按揭市场份额31%排第一，HSBC在楼花按揭以24%领先\n\n**2/ 息差环境出现转折信号**\n- HIBOR 6月明显走强，1个月HIBOR环比升23bps，推动SOFR-HIBOR利差收窄至82bps\n- 综合利率5月升至1.26%，结束此前连续下降趋势\n- 存款竞争整体理性，但小型银行和虚拟银行在季末加大了港币定存争夺\n\n**3/ 资产质量持续改善**\n- 3个月逾期按揭比率进一步降至0.11%，为2025年11月来新低\n- 香港银行1Q26不良率降至1.87%，创8个季度新低\n- 毕马威预计FY27不良率将继续改善，惠誉将行业展望上调至“中性”\n\n几个值得跟踪的事件：\n- \n\n[... middle omitted ...]\n\ntial FED rate hikes might allow HSBC to sustain the relative outperformance in the near future.\n\n\\- News summary for June 2026: June headlines continued to focus on tighter cross-border invest\n\n[... middle omitted ...]\n\n not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not"
  },
  {
    "id": "R012",
    "title": "JPM：中国铜库存降至多年低位，JPM解读消费改善信号",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：中国铜库存降至多年低位，JPM解读消费改善信号\n\n全球大宗商品市场经历连续六周的持仓下滑后，终于在上周出现企稳信号。JPM最新发布的《大宗商品市场持仓与资金流》周报显示，截至7月3日，跟踪市场的未平仓合约估值小幅回升至1.7万亿美元，结束了自5月中旬霍尔木兹海峡重开预期以来的持续缩水。但更值得关注的不是总量，而是结构——资金正在从能源和工业金属撤出，重新涌入贵金属，尤其是黄金。\n\n这份报告的核心判断是：黄金正在重新获得利率敏感型资金的支持，ETF流量正在取代央行购金成为边际定价力量。而原油市场则陷入了“中国需求变化”与“闲置产能重新入市”的双重夹击，短期内看不到明确的向上动力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 黄金的定价权正在从央行转向ETF，但这不是一个简单的信号\n\n报告中最值得细读的是黄金部分。截至7月3日，贵金属板块的未平仓合约估值周环比增长3%至2500亿美元，净多头持仓增加40亿美元，其中黄金贡献了35亿美元。更关键的是，COMEX黄金期货中管理资金净多头增加了4700手，总量达到12万手。\n\nJPM分析师明确指出：在其他需求板块购买力度暂时下降的背景下，对利率敏感的ETF流量重新获得了黄金的边际定价权。这意味着一件重要的事情——黄金与真实利率之间的相关性正在重新建立。\n\n> **KC评论：** 过去两年黄金的上涨逻辑更多是央行购金和地缘避险，与利率脱钩。如果ETF流量重新成为主导，那么美联储的利率路径将再次成为黄金定价的核心变量。报告预计3季度金价均价4300美元/盎司，4季度4500美元/盎司，但前提是美联储保持耐心。如果市场开始定价更早的降息，这个区间可能被打破。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 原油的现状：中国\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n大宗商品持仓出现企稳信号\n\n**持仓拐点来了？**\n\n**商品市场连续六周下滑后首次回升**\n\n商品持仓总价值在连续六周下滑后首次回升，截至7月3日达到约1.7万亿美元。虽然合约层面仍有130亿美元资金流出（主要集中在原油），但被成品油、天然气和贵金属的价格上涨所抵消。这是自5月中旬市场开始定价霍尔木兹海峡重新开放以来的首次增长。\n\n---\n\n1/ **能源市场：原油承压，天然气挺住**\n- 能源持仓总值下降1%至7180亿美元，原油合约流出120亿美元\n- 但天然气持仓逆势微增1%，欧洲和亚洲基准价格上涨抵消了26亿美元的合约流出\n- 注意：卡塔尔能源运营基本稳定，预计8月恢复满产\n\n2/ **贵金属：黄金重新获得定价权**\n- 持仓总值增长3%至2500亿美元，黄金净流入25亿美元\n- 黄金净多头增加4700手至12万手\n- 利率敏感的ETF资金流重新获得边际定价权，黄金与实际回报表现的关联性在增强\n- 短期看震荡，预计3Q26均价4300美元/盎司，4Q26均价4500美元/盎司\n\n3/ **基本金属：铜库存降至多年低位**\n- 持仓总值持平于2120亿美元\n- 中国铜库存过去三周累计减少8.2万吨，降\n\n[... middle omitted ...]\n\nthe reopening of the Strait of Hormuz. On the macro front, our economists continue to see a tightening labor market, alongside solid growth and sticky inflation, as the catalyst that pushes Fe\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 07 Jul 2026 06:51 PM BST\n\nDisseminated 07 Jul 2026 06:52 PM BST"
  },
  {
    "id": "R013",
    "title": "JPM：MLCC涨价预期落空？JPM称真正供需紧张在2027年",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：MLCC涨价预期落空？JPM称真正供需紧张在2027年\n\n四月至六月这一财报季，日本电子元器件公司大概率交出一份不错的成绩单。JPM最新研报的判断很直接：AI服务器、工业设备和汽车领域的订单回暖叠加日元贬值，多数公司的营业利润有望达到甚至超过公司指引。但报告紧接着提出了一个反直觉的提醒——利润好，不代表报价能继续涨。\n\n被动元件和AI服务器相关公司的涨幅已经远远跑在了短期盈利前面。过去三个月，村田制作所涨了191%，太阳诱电涨了352%，罗姆涨了64%。当报价已经包含大量乐观预期时，财报只要“没有惊喜”，就可能成为回调的理由。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日元贬值与需求复苏构成双重安全垫，但市场定价已提前消化\n\n这份研报在盈利预测中埋了一个关键变量：日元汇率。多数日本电子元器件公司在制定2026财年指引时，假设的美元兑日元汇率在150-155区间。而四月至六月的实际汇率已经来到159-160。仅汇率这一个变量，就能直接推高以日元计价的海外收入。\n\n与此同时，AI服务器、工业设备和汽车这三个终端市场的需求复苏势头比预期更扎实。JPM认为，在日元贬值和需求回暖的双重作用下，四月至六月这一季的营业利润大概率落在“符合指引”或“超越指引”的区间。\n\n> **KC评论：** 日元贬值和AI需求回暖是两股不同性质的力量。汇率是一次性红利，而AI带动的MLCC（多层陶瓷电容）出货量增长才是结构性故事。研报提示了短期报价不确定性，但真正值得深读的是它对MLCC供需缺口的远期判断——缺货预期可能在2026年四季度才开始体现。\n\n问题在于，市场已经提前为这些好消息买单了。报告里的报价表现表格显示，太阳诱电过去12个月涨幅接近700%，村田制作所超过400%。一家公司利润增长30%-50%，报价涨了4-7\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 日系电子元件，二季度表现观察\n\n📊 二季度业绩前瞻\n\n近期有机构发布了日本电子元件相关研究，逻辑清晰，整理供参考👇\n\n**1️⃣ 整体判断：业绩表现可能较好，但市场反应未必同步**\n\n4-6月季度，AI服务器、工业设备、汽车三大需求均有回暖迹象，叠加日元汇率波动（实际在159-160区间，机构假设为150-155），利润表现大概率符合或略超预期。\n\n但需留意——被动元件和AI相关公司前期涨幅较大，市场已部分消化预期。即便业绩小幅不及预期，也可能引发一定波动。\n\n**2️⃣ 被动元件：MLCC涨价预期需理性看待**\n\n部分海外观点仍在期待MLCC（多层陶瓷电容）短期涨价，但研究认为7-9月涨价可能性较低。真正的供给变化预计从FY2027开始，相关谈判可能集中在10-12月。\n\n具体公司观察：\n- **村田制作所**：1Q营业利润可能达到900亿日元以上（研究保守估865亿），汇率波动和行业景气是主要因素\n- **太阳诱电**：韩国MLCC工厂运营存在变数，利润可能低于预期（研究估50亿日元）\n- **TDK**：若1Q利润超过700亿日元，或带来积极信号（研究估674亿）\n\n**3️⃣ 其他关注点：工业设备\n\n[... middle omitted ...]\n\nector outlook: Most of the companies in our electronic component coverage assumed USD/JPY of 150-155 for FY2026, but the actual level in April-June was 159-160, which should boost earnings. In\n\n[... middle omitted ...]\n\ninions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not"
  },
  {
    "id": "R014",
    "title": "JPM：韩国汽车零部件公司机器人业务不再是免费期权",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：韩国汽车零部件公司机器人业务不再是免费期权\n\n报价从高点回调超过36%之后，JPM开始重新审视韩国两大汽车零部件公司——现代摩比斯和HL万都。这份研报的核心判断并不复杂：机器人执行器业务此前被市场当作“免费看涨期权”定价，但现在报价已经跌到只反映核心零部件业务的价值，执行器变成了真正的增量期权。不确定性回报比变了，评级也随之调整。\n\n报告上调现代摩比斯至“超配”，HL万都从“低配”上调至“中性”。这不是因为两家公司的基本面出现了突然的改善，而是因为市场已经替它们完成了“不确定性测试”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 报价回调之后，核心业务提供了估值底\n\nJPM用SOTP（分部加总估值法）拆解了两家公司的价值构成。对于现代摩比斯，核心汽车零部件业务估值约44万亿韩元，再加上其在现代汽车集团机器人业务中12%的持股（约6万亿韩元），两者之和已经基本覆盖了当前市值。也就是说，市场目前对摩比斯的定价，几乎完全基于它作为传统汽车零部件供应商的价值，机器人业务几乎没有被赋予额外溢价。\n\nHL万都的情况类似：核心零部件业务隐含价值约2.3万亿韩元，与当前市值大致相当。执行器业务虽然被讨论，但报告明确指出“订单可见性仍然有限”，因此没有给予其估值上的“信任票”。\n\n> **KC评论：** 这实际上是一种“安全边际”的重新确认。当一家公司的市值已经跌到其传统业务的价值附近时，市场对它的叙事溢价就被挤干了。剩下的只有两个可能性：要么传统业务被低估，要么新业务成为真正的惊喜。JPM选择赌后者。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 机器人叙事没有消失，但性质变了\n\n报告里有一组很有意思的读者反馈。JPM在亚洲路演中得到的反馈是：大部分读者同意，新进入执行\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 韩国汽车零部件调整后，机器人业务成关注点\n\n📉 调整36%后，关注价值显现\n\n某外资机构近期上调了现代摩比斯和HL Mando的评级。核心逻辑：报价从高点回落36%-37%后，当前水平已基本反映传统汽车零部件业务的价值，机器人执行器这块增量业务相当于“潜在增长机会”。\n\n1️⃣ **现代摩比斯：核心业务支撑报价**\n- 传统汽车零部件业务估值约44万亿韩元，加上现代汽车集团机器人业务股份（6万亿），基本解释了当前市值\n- 执行器业务按2030年预计销售额约0.8万亿韩元、20倍市销率估值，额外价值约13万亿韩元\n- 市场目前用市销率（而非市盈率）看待执行器机会，只要收入可见性改善，报价就可能有所反应\n\n2️⃣ **HL Mando：估值有底，但执行器订单还不明朗**\n- 核心零部件业务估值约2.3万亿韩元，基本等于当前市值\n- 执行器业务订单可见度有限，因此暂未给予太多估值溢价\n- 但报价已回到核心业务支撑位，下行空间有限\n\n3️⃣ **市场怎么看？**\n- 读者普遍把这两家公司当“机器人杠杆”标的\n- 虽然新进入执行器领域可能不会很赚钱，但机器人叙事会持续影响市场情绪\n- 有人觉得调整已充分，加上机器人\n\n[... middle omitted ...]\n\nfore assign limited benefit of the doubt, but valuation is effectively supported by the implied value of the core franchise (W2.3tn), roughly in-line with the current market cap. Investor feed\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 07 Jul 2026 09:03 PM HKT\n\nDisseminated 07 Jul 2026 09:03 PM HKT"
  },
  {
    "id": "R015",
    "title": "JPM：日本银行股上涨37%之后，真正的分化从1Q财报开始",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：日本银行股上涨37%之后，真正的分化从1Q财报开始\n\n日本银行板块过去一年涨幅可观，TOPIX银行指数自2025年底以来已上涨约37%。市场对加息周期的定价并不算低。但JPM最新发布的日本银行业1Q财报前瞻报告指出，真正的分化才刚刚开始——核心看点不是利润本身，而是哪些银行会在8月财报季主动上调全年指引，把6月日本央行加息的影响纳入预测。\n\n这份报告覆盖了三菱日联、三井住友、Mizuho三大巨型银行，以及一批区域性银行和网络银行。分析师Takahiro Yano的观察框架很清晰：在加息路径已经明朗的环境下，管理层是否敢于在1Q就修正指引，比单季度利润数字更能说明问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 加息预期已落地，但多数银行的指引还没跟上\n\n6月日本央行加息后，市场利率曲线进一步陡峭化。3个月TIBOR回报表现随之走高。但JPM在报告中的一张表格（Figure 3）揭示了一个关键事实：在覆盖的17家银行中，大部分在制定全年指引时并未纳入6月加息的影响。\n\n三菱日联是少数例外——其指引已假设2026年中期有一次加息，因此JPM预计它不会在1Q财报时调整指引。而像静冈资金集团、横滨资金集团等区域性银行，其指引仍基于“2026财年无加息”的假设。一旦它们主动修正，市场将解读为管理层对业务进展有足够信心。\n\n> **KC评论：** 这里的关键不是利润数字本身，而是管理层的“信号释放”。如果一家银行在1Q就上调全年指引，意味着它对净息差扩张和贷款增长有底气。反过来，如果等到2Q或3Q才修正，市场可能会认为管理层反应偏慢。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 贷款增长加速，但结构差异正在拉大\n\n报告引用了日本央行的统计数据：2026年5月国内\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n日本银行股Q1业绩，关注这三点\n\n日本银行股进入财报季\n\n关键看点：谁会在Q1上调指引？\n\n---\n\n某外资机构最新研报拆解日本银行股Q1业绩看点，逻辑清晰，信息量很大。\n\n**1/ 核心看点：6月加息是否纳入指引**\n日本央行6月加息后，很多银行并未将其纳入全年业绩指引。如果Q1季报中有银行快速上调指引，说明管理层对业务进展有信心。三菱UFJ（MUFG）已提前计入年中加息，预计不会调整。三井住友信托（SMTG）和日本邮政银行（JPB）预计Q1利润增速较高，前者来自股票出售收益，后者因海外NII低基数反弹。\n\n**2/ 利润增速分化明显**\n- 部分银行因去年同期有资产出售或一次性税收优惠，Q1利润同比可能大幅下降（如SBI新生银行、青空银行、福冈金融集团）。\n- Seven银行Q1有一项子公司特别损失。\n- 地方银行利润走势取决于信用成本或证券出售损失是否在去年同期发生。\n\n**3/ 回购是Q1的股东回报重点**\n五大行、SMTG和理索纳已在5月宣布回购，多数地方银行选择在Q1季报时公布。研报预计静冈金融集团和横滨银行将宣布约400亿日元回购（接近全年计划），而目白金融集团和千叶银行可能只回购全年预测额的一\n\n[... middle omitted ...]\n\ncide that they do not need to revise guidance, but if any banks move quickly to revise guidance with 1Q results, we would view this positively as a sign of confidence in business progress. Amo\n\n[... middle omitted ...]\n\n THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer"
  },
  {
    "id": "R016",
    "title": "JPM：东南亚利润韧性强，极兔新市场跨过盈亏平衡点",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：东南亚利润韧性强，极兔新市场跨过盈亏平衡点\n\n极兔速递自2023年10月上市以来，报价表现一直承压。市场关注中国快递行业的价格竞争、东南亚市场增长空间，以及新市场能否真正贡献利润。但JPM最新覆盖报告给出了一个截然不同的判断：这些担忧已经被过度反映，而公司基本面正在发生一个关键转折——从追求规模转向释放利润。\n\n报告的核心逻辑并不复杂。极兔目前交易在约10倍远期市盈率，而公司未来三年净利润复合增长率预计达到约50%，远超行业15-20%的平均水平。这种估值与盈利增速的背离，在JPM看来，是一个值得关注的结构性机会。更重要的是，公司已经完成了从亏损到盈利的切换，自由现金流正在改善，管理层也开始启动股份回购。\n\n> **KC评论：** 市场对极兔的定价逻辑，本质上是在问两个问题：东南亚还能不能增长？新市场能不能赚钱？JPM的回答是，这两个问题都已经有了阶段性答案——东南亚的利润韧性比市场预期的强，新市场已经跨过盈亏平衡点。完整报告里对每个区域的成本拆解和自动化投入数据，值得仔细看。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 东南亚不是天花板，而是利润压舱石\n\n市场对东南亚市场的关注集中在两点：竞争加剧导致单价下降，以及市场成熟后增长节奏变化。但JPM的数据显示，极兔在东南亚的市场份额仍在提升，预计2025年达到34.4%。更重要的是，公司的成本优势正在拉大——通过自动化分拣中心和自营车队，极兔在东南亚的单件成本持续下降，这使得即便单价承压，利润率依然有支撑。\n\n报告特别指出，极兔正在从单纯的电商件向高毛利的非平台业务拓展，这为利润提供了额外缓冲。东南亚不再是增长故事的全部，但它正在成为一个稳定且可预期的利润来源。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 快递行业观察：行业拐点或已出现\n\n📦 极兔的调整期是否接近尾声？\n\n**海外机构首次覆盖极兔，给出13港元目标价，隐含约37%上行空间。**\n核心逻辑：市场此前可能过度悲观，但盈利拐点已经出现。\n\n---\n\n**1/ 为什么报价下跌？并非公司基本面问题**\n\n自2023年10月上市以来，极兔报价经历了较大波动：\n- 中国快递行业价格竞争\n- 上市初期亏损\n- 中东地缘冲突及燃料价格波动\n- 市场对东南亚市场饱和后增长空间的担忧\n\n这些因素将估值压至**10倍远期市场定价**，但研报认为**这轮调整是周期性的，而非结构性的**。\n\n---\n\n**2/ 为什么现在值得关注？三个拐点同步出现**\n\n① **盈利拐点已来**\n- 2025年调整后净利润4.25亿美元，2028年预计达到15亿\n- 净利率从3.5%提升至7.2%\n- 所有区域均在改善，并非仅依赖东南亚\n\n② **新市场开始贡献利润**\n- 巴西、墨西哥、中东：件量弹性较高增长\n- 从投入期进入盈利拐点\n- 中国/东南亚的经验被成功复制至全球\n\n③ **与顺丰的合作并非简单资本合作**\n- 联合投资自动化分拣中心和干线车辆\n- 极兔借助顺丰的跨境和仓\n\n[... middle omitted ...]\n\n loss-making status, and external shocks such as recent fuel price volatility. The market has also questioned the scalability of J&T's model outside China and the sustainability of margins in \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R017",
    "title": "研究笔记：欧莱雅提前接手古驰美妆，利润修复预计在2028年",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# 研究笔记：欧莱雅提前接手古驰美妆，利润修复预计在2028年\n\n欧莱雅与开云集团之间的古驰美妆许可协议，比原计划提前一年生效。根据一份最新研究报告，这笔交易将从2027年7月1日起执行，欧莱雅将为此支付约4亿欧元对价之外的最高4亿美元过渡成本。但报告的核心判断并非“交易提速”，而是：**这笔交易对欧莱雅的中期利润贡献要到2028年才能体现，而在此之前，公司仍需面对全球美妆市场增速正常化带来的估值不确定性。**\n\n这份报告由欧洲消费品分析师执笔，覆盖欧莱雅、开云及全球美妆与奢侈品格局。报告在给出交易细节的同时，也提出了一个值得产业决策者关注的框架：当一家公司以溢价估值收购长期许可权，其回报周期与市场预期之间的缺口，往往才是真正的不确定性所在。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 交易提速的代价是短期利润承压\n\n欧莱雅原本预计在2028年开云与科蒂的现有协议到期后，才开始接手古驰美妆业务。但开云集团近期宣布提前终止与科蒂的协议，使得欧莱雅的新许可协议随之提前至2027年7月生效。作为交换，欧莱雅需承担约70%的提前赎回成本，即2026年支付2.5亿美元、2027年再支付最高1.5亿美元。这笔费用是在此前已公布的40亿欧元交易对价之外的额外支出。\n\n报告预计，这笔交易（包括收购开云美妆及Creed品牌，以及宝缇嘉和巴黎世家的50年整理版许可）将在2028年带来1%至2%的利润增厚。但管理层近期明确表示，2026年和2027年交易将带来轻微稀释。换言之，**欧莱雅用两年的利润不确定性，换取了一个更早启动的品牌资产整合窗口。**\n\n> **观察：** 很多读者只看到“提前一年生效”这个信息，却忽略了过渡成本对短期利润表的直接冲击。报告的真正信号是：这笔交易的价值释放需要时间，2026和2027年的利润预期可能需\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n开云提前一年将Gucci美妆业务移交欧莱雅\n\nGucci美妆授权变更\n\n欧莱雅提前接手，2027年7月生效\n\n---\n\n**1. 时间线加速了**\n\n原本计划2028年才交接的Gucci美妆授权，现在提前到2027年7月1日。研究分析显示，开云提前终止了与Coty的现有协议，欧莱雅将为此支付约70%的提前赎回成本（2026年2.5亿+2027年最多1.5亿美元），外加库存费用。这笔支出是在之前公布的40亿欧元交易对价之外的。\n\n**2. 这笔交易的整体评估如何？**\n\n研究观点较为清晰：\n- 预计到2028年，这笔交易（包括收购Kering Beauté和Creed，以及Bottega Veneta、Balenciaga的授权）能带来1-2%的利润增厚\n- 但2026和2027年反而会小幅稀释利润——前期投入需要时间消化\n\n**3. 欧莱雅为什么愿意多花钱提前接手？**\n\n两个品牌都是开云旗下的核心资产。提前一年拿到Gucci美妆的控制权，意味着欧莱雅可以更早开始整合和运营，尤其是全球旅游零售渠道的布局。研究提到，欧莱雅将全权负责Gucci Beauty的全球开发和运营。\n\n**4. 对欧莱雅整体怎么看？**\n\n[... middle omitted ...]\n\nng's announcement today ending the current agreement about a year early, the new license with L'Oreal shall come into effect as of July 1st, 2027, subject to regulatory approvals. The company \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R018",
    "title": "JPM：铝铜塑料涨价冲击汽车利润，韩元贬值对冲效果有限",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：铝铜塑料涨价冲击汽车利润，韩元贬值对冲效果有限\n\n当市场还在争论现代汽车与起亚谁能在新车型周期中占据优势时，一份来自JPM的报告揭示了一个更本质的判断：这两家韩国汽车制造商在2026年第二季度的业绩分化，根源不在于销量本身，而在于成本结构对两家公司不同的传导机制。\n\n现代汽车二季度全球零售销量99.9万辆，同比下降4%，而起亚则录得83.7万辆，同比增长6%。这一差异本身并不意外——现代正处在老旧车型周期的尾部，而起亚的产品线正值青壮年。但真正值得关注的，是两家公司在面对同样成本不确定性时的不同表现。\n\n报告预计现代汽车二季度营业利润为2.9万亿韩元，低于市场预期的3.1万亿；起亚同为2.9万亿，基本符合预期。差异的关键在于产能利用率。现代汽车的产能利用率降至约85%，而起亚仍维持在接近满产的100%水平。在原材料成本全面上涨的背景下，更低的产能利用率意味着固定成本无法被充分摊薄，这是一个结构性劣势。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 成本通胀正在成为比销量更关键的变量\n\n报告估算，铝、铜、塑料和DRAM等大宗商品的价格上涨，在二季度对现代汽车和起亚的营业利润分别造成约3500亿韩元和2500亿韩元的冲击。虽然韩元贬值为两家公司提供了约5000亿和4000亿韩元的汇兑对冲，但成本上涨的节奏在二季度明显加速，后续几个季度可能无法被完全吸收。\n\n> **KC评论：** 这里需要读者关注的不是成本上涨的相对值，而是“成本传导机制”的差异。现代汽车由于销量下滑和产能利用率不足，成本不确定性被进一步放大；而起亚凭借销量增长，部分抵消了原材料上涨的影响。这说明在通胀环境下，产能利用率变成了一个放大器——好的公司被放大收益，弱的公司被放大亏损。\n\n![研报原图 2](assets/source_imag\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n现代 vs 起亚，谁在应对成本变化\n\n韩国双雄，Q2表现各有不同\n\n某机构最新研究分析了现代汽车和起亚的Q2情况——两家都受到成本变化影响，但销量节奏差异明显。\n\n1️⃣ 销量表现分化\n- 现代Q2全球零售99.9万辆（同比-4%），韩国和欧洲因车型更新节奏及供应链因素影响\n- 起亚Q2零售83.7万辆（同比+6%），海外和本土市场均有增长\n- 研究认为现代下半年有望通过新车上市改善，起亚现有产品线仍具支撑\n\n2️⃣ 成本变化持续\n- 铝+13%、铜+15%、塑料+30%、DRAM+72%，Q1涨价效应延续至Q2\n- 现代成本影响约3500亿韩元，起亚约2500亿\n- 汇率带来正向贡献（每季度约5000亿/4000亿韩元），但Q2成本增速加快，对冲效果存在不确定性\n- 现代另一因素：产能利用率降至85%（Q2 2025约为100%），起亚维持在约100%\n\n3️⃣ 机器人业务或成新关注点\n- 市场关注HMG机器人训练中心（今夏开放）及年底前机器人业务详细规划\n- 目前起亚估值更具吸引力：6x 2027年预期回报 + 4%以上分红率\n- 若机器人领域关注度提升，现代可能展现更大弹性\n\n4️⃣ 研究维持两家“优于\n\n[... middle omitted ...]\n\ncelerated in 2Q and may not be fully offset in the following quarters. Investors are now focused on the next robotics catalysts, with Kia preferred on valuation (6x 2027E P/E) and >4% yield bu\n\n[... middle omitted ...]\n\nof any issuer, its products or services, or its securities in any jurisdiction.\n\nConfidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or"
  },
  {
    "id": "R019",
    "title": "JPM：JPM看辉瑞，不是价值陷阱，而是管线期权时间折价",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：JPM看辉瑞，不是价值陷阱，而是管线期权时间折价\n\n辉瑞的报价已经跌到不足2027年预期每股回报的9倍，在大型制药公司中属于罕见的低估值区间。但JPM在7月初发布的这份报告中给出了一个克制却值得注意的判断：便宜不是问题，问题是市场需要看到管线里的东西真正落地。这份报告写于二季度财报公布前夕，分析师对当季和全年的营收与每股回报预期均略高于公司指引和市场共识，但真正决定公司能否重新定价的变量，是2027年之后才能兑现的候选药物数据。\n\n**1. 短期业绩有上修空间，但市场不会为此买单**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n![研报原图 2](assets/source_image_02.jpg)\n\n![研报原图 3](assets/source_image_03.jpg)\n\n报告给出的全年营收预测为627亿美元，高于辉瑞自己给出的595至625亿美元指引区间上限；每股回报预测为3.05美元，也高于公司指引的2.80至3.00美元。上修主要来自Eliquis的持续超预期表现，这部分收入全年比市场共识高出2.7亿美元，足以抵消新冠产品Comirnaty和Paxlovid的持续下滑。但报告直言，无论是Eliquis还是新冠业务，都已经不是市场定价的核心变量。即便季度业绩超预期，也很难推动报价出现系统性修复。\n\n> **KC评论：** 辉瑞的业绩指引本身已经留有余地，分析师认为上修空间存在，但这条信息对判断公司短期走势的参考价值有限。真正值得关注的，是报告对“什么能驱动重新定价”的判断——不是现有产品，而是管线进展。\n\n**2. 管线才是定价的钥匙，但关键数据要等到2027年以后**\n\n报告对辉瑞管线的态度是“有吸引力但需要进一步去不确定性”。目前市场情绪处于低位，读者普遍认为报价节奏变化空间有限，但要想让报价重\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n辉瑞二季度前瞻：业绩有望小幅超预期，市场更关注管线进展\n\n📌 估值处于低位，但关键驱动因素在远期\n\n某机构在辉瑞二季报前发布报告，认为业绩有望小幅超预期，但市场关注点已转向管线进展。\n\n**核心判断：**\n- 二季度预测：营收146亿（比市场预期高1.3亿），EPS 0.69（高0.01）\n- 全年预测：营收627亿（比公司指引上限高2亿），EPS 3.05（比指引上限高0.05）\n- 目标价从30下调至28，维持中性评级\n\n**1️⃣ 业绩拆解：新冠业务下滑，主力品种表现稳健**\n- Padcev：7亿（+7000万 vs 预期）\n- Ibrance：11亿（+9000万）\n- Eliquis：21亿（同比+3%，全年比预期高2.7亿）\n- 新冠业务：Comirnaty同比-27%，Paxlovid同比-77%，全年预测42亿（公司指引约50亿）\n- 非新冠品种的强劲表现足以抵消新冠业务下滑，全年有望小幅超指引\n\n**2️⃣ 估值处于低位，但市场反应有限**\n- 当前估值约9倍2027年EPS，处于历史较低区间\n- 市场普遍认为：下行空间有限，但公司价值重估需要管线进展\n- 主要催化剂集中在2027-202\n\n[... middle omitted ...]\n\ntinue to view PFE shares as inexpensive (\\~9x 2027e EPS) with several assets in the company's pipeline that could make the story more interesting over time. However, we believe further deriski\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 07 Jul 2026 09:16 PM EDT\n\nDisseminated 08 Jul 2026 12:15 AM EDT"
  },
  {
    "id": "R020",
    "title": "JPM：从挂牌量到报价指数，中国房地产市场修复的新观察框架",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：从挂牌量到报价指数，中国房地产市场修复的新观察框架\n\n过去几周，市场对中国房地产的讨论集中在销售数据能否延续年初以来的反弹。JPM最新发布的周度监测报告提供了一个更值得关注的信号：一线城市二手房挂牌量正在持续下降，且这一趋势并非短期波动。\n\n截至7月4日当周，深圳挂牌量环比下降2.2%，上海下降0.4%，推动一线城市整体挂牌量较3月峰值已回落3.5%。在成交量仍保持正增长的背景下，供给侧的主动调整，正在为二手房价格构筑一个更坚实的底部。\n\n这份报告的核心价值不在于罗列周度数据，而在于它揭示了一个正在发生的结构性变化：卖盘不再无节制堆积，市场供需正在重新平衡。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 挂牌量下降比成交量上升更能预示价格拐点\n\n过去一年，市场习惯用成交量的同比变化来判断复苏强度。但JPM报告指出，真正影响价格走向的是挂牌量——即供给端的意愿。\n\n目前10个重点城市的二手房挂牌总量基本持平，但一线城市已连续多周下降。深圳从6月初的89万套降至85万套，上海从84万套降至82万套。这个趋势如果持续，意味着此前压在市场上的“堰塞湖”正在缓慢消解。\n\n> **KC评论：** 成交量的波动受季节性、推盘节奏甚至天气影响，但挂牌量的变化反映的是业主的真实预期。一线城市挂牌量从高位持续回落，说明卖方的恐慌性抛售正在消退。这是价格稳定的前提，比单周成交数据更有说服力。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 上海是相对少见量价齐升的一线城市，但领先指标出现微妙变化\n\n从周度数据看，上海表现突出：二手房实时成交同比增长20%，挂牌量环比下降0.4%，经理人信心指数从48回升至52，重返乐观区间。这是报告中最亮眼的一张图。\n\n但报告也提示了隐忧。中原地\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n一线城市二手挂牌量，出现新变化\n\n二手市场的关键信号\n\n近期研究数据更新，几个核心变化值得关注👇\n\n**1️⃣ 一线城市二手挂牌量持续下降**\n- 深圳环比降2.2%，上海降0.4%\n- 一线城市整体挂牌量已从3月峰值回落3.5%\n- 挂牌量持续走低，是二手房价企稳的关键支撑\n\n**2️⃣ 二手成交分化明显**\n- 上海表现突出，同比+20%\n- 一线城市整体二手成交同比+15%\n- 但广州、深圳部分数据出现环比下滑\n\n**3️⃣ 市场情绪有所回暖**\n- 经理人信心指数从52升至55\n- 上海信心指数从48跳升至52\n- 但业主涨价意愿指数仍在下行（17.0→16.6）\n\n**4️⃣ 香港市场：上半年涨幅已达标**\n- 上半年房价已涨12%，达到全年10-15%目标\n- 下半年预计涨幅放缓至5%以下\n- 二手成交同比仍大幅下降54%\n\n**5️⃣ 开发商表现**\n- 相关公司板块上周涨4%，跑赢恒指\n- 世茂+12%、金茂+9%领涨\n- 融创-6%表现较弱\n\n小讨论：一线城市挂牌量持续下降，是业主惜售还是市场调整？欢迎一起聊聊～\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_miner\n\n[... middle omitted ...]\n\n in Shanghai (Table 2). The volume of secondary listings in tier-1 cities has been consistently coming down (down $3.5\\%$ from the peak in March), and this is a key factor that will support co\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 07 Jul 2026 08:05 PM HKT\n\nDisseminated 07 Jul 2026 08:05 PM HKT"
  },
  {
    "id": "R021",
    "title": "JPM：三星远期市盈率仅5倍，JPM认为市场误判了存储周期长度",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：三星远期市盈率仅5倍，JPM认为市场误判了存储周期长度\n\n三星电子刚刚交出了一份创纪录的二季度初步业绩。营收171万亿韩元，营业利润89.4万亿韩元，双双超出近期被下修的市场预期。但这份成绩单背后藏着一个关键的分歧：市场将其视为周期高点的信号，而JPM认为这恰恰是结构性短缺被低估的起点。\n\n报告的核心判断直指一个容易被忽略的变量——当前三星电子的远期市盈率仅为5.2倍，是全球最便宜的存储芯片公司。这个估值定价隐含的假设是，这轮盈利高峰将在一年内见顶回落。但JPM的分析指出，供给端的约束远比市场想象的更持久，而需求端的结构性变化才刚刚开始。\n\n**理解这份报告，需要抓住三个层次。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 盈利超预期的真正来源不是一次性项目，而是NAND定价的持续上移\n\n二季度营业利润超出市场预期区间约5万亿韩元。表面上看，这笔超额利润中有相当部分来自劳务成本拨备的一次性调整。但拨备只是会计处理，真正驱动业绩超预期的是NAND的混合均价环比涨幅超过70%，远高于JPM此前预期的53%。\n\nDRAM的均价涨幅则低于预期，主要原因在于产品组合向低毛利品类倾斜。但JPM认为这恰恰是健康的信号——客户正在通过调整产品结构来应对BOM成本不确定性，而非削减采购量。存储芯片的供应满足率仍处于50%-60%的低位，这意味着定价权依然在供应商手中。\n\n> **KC评论：** 市场容易把“超预期”归因于一次性项目，从而低估定价趋势的持续性。真正值得关注的是NAND涨价的结构性驱动力——美国超大规模云厂商对企业级SSD的需求正在从AI训练扩展到KV缓存卸载，这是一个全新的消耗场景。报告没有完全展开的是，这种需求是否会随着AI推理规模的增长而加速。\n\n![研报原图 2](assets/source_i\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n三星存储芯片，近期表现如何？\n\n📌 存储周期延续时间或超预期\n\n某外资机构近期更新了对三星的研究报告，梳理了几个关键逻辑，供大家参考。\n\n**1/ 二季度业绩超预期，但存在“一次性”因素**\n- 营收171万亿韩元，OP 89.4万亿，高于市场预期的75-84万亿\n- 超预期主要源于：存储价格表现强于预期 + 韩元汇率变化\n- 但利润中包含15万亿+的劳动成本拨备（一次性），实际运营利润需适当调整\n\n**2/ 存储供应缺口仍在，价格支撑因素未减弱**\n- 当前采购端仅50-60%的供应能被满足，缺口依然明显\n- 服务器端需求保持强劲（尤其企业级SSD用于AI的KV cache卸载）\n- 研究判断：NAND价格可能继续超预期（环比约+20%），DRAM受产品组合影响略弱\n\n**3/ 代工业务是否迎来转机？**\n- 三星4nm HBM4基底层已进入量产阶段\n- 正在接触Google/Anthropic/Meta/AMD/BYD等新客户（此前已拿下Tesla AI5/AI6和Apple CIS）\n- 若订单落地，美国泰勒工厂可能需要扩产\n\n**4/ 市场关注焦点：本轮周期能持续多久？**\n- 三星当前估值约5.2倍\n\n[... middle omitted ...]\n\n price (SEC shares are trading at 5.2x FTM P/E, the cheapest memory stock globally) appears to price in only a little of the structural S&D dynamic shifts (e.g., multi-year shortage, growing L\n\n[... middle omitted ...]\n\normational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or\n\nCompleted 07 Jul 2026 03:02 PM HKT"
  },
  {
    "id": "R022",
    "title": "JPM：不是复苏而是再定价，JPM拆解新加坡地产二元化行情",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：不是复苏而是再定价，JPM拆解新加坡地产二元化行情\n\n新加坡地产市场的叙事正在切换。JPM近期与Colliers研究主管的联合研讨，以及同步发布的东南亚数据中心专题报告，共同指向一个核心判断：新加坡地产市场并非整体回暖，而是在AI需求、供给约束和资金偏好三股力量作用下，进入“优质资产”的独立行情阶段。这份研报最有价值的信息，不是某个子市场的短期波动，而是揭示了一幅“新加坡优化每一兆瓦，马来西亚承接下一兆瓦”的区域分工新图景。\n\n报告认为，新加坡地产市场基本面仍然健康，但增长正在变得越来越有选择性——或者说，越来越“二元化”。办公楼领域的“向优质资产转移”（flight-to-quality）、郊区零售的韧性、工业资产中的选择性机会、住宅需求的温和节奏变化，这四个趋势共同指向一个结论：不是所有资产都能受益，只有那些位于最高品质区间的物业——核心CBD办公楼、优质郊区购物中心、现代物流设施和差异化住宅项目——才能在宏观不确定性中持续吸引需求。\n\n> **KC评论：** 这份报告的核心判断其实是一句大白话：在新加坡，买“好东西”和买“一般东西”的回报差距，正在拉大。报告里用“bifurcated”这个词，直译是“分叉”，但更准确的理解是：市场已经不再相信普涨，资金只愿意为稀缺性买单。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI正在成为商业地产最被低估的需求引擎\n\n报告特别点出，AI已成为新加坡办公楼、科技园和数据中心需求的重要推动力。这不是一个遥远的概念。JPM在数据中心专题中给出了一个非常具体的量化框架：新加坡正在收紧电能使用效率（PUE）标准，要求数据中心PUE达到约1.25-1.3，而马来西亚对超大规模数据中心（hyperscalers）的PUE门槛是1.4。这个差距看似微小，实则是区域分工的\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n新加坡地产市场呈现“分化式增长”\n\n**分化式增长**\n\n**核心资产依然稳健，但逻辑有所调整**\n\n---\n\n近期与某外资机构一同参加了Colliers研究主管的分享，了解了新加坡地产的最新动态。整体来看：**市场健康，但增长越来越依赖资产选择。**\n\n1️⃣ **写字楼：企业持续迁往优质楼宇**\n企业继续向优质办公楼搬迁，CBD核心区的好楼租金保持稳定。AI行业成为新的需求推动力，不仅科技公司，金融、咨询等领域也在积极选择好位置。但老旧楼宇面临一定挑战，供应受限也难以扭转这一趋势。\n\n2️⃣ **零售：郊区购物中心表现突出**\n乌节路的高端商场和组屋区的社区mall表现良好，但最稳定的仍是郊区购物中心——生活必需消费支撑了客流和租金。高端商场更多依赖游客和富裕人群，波动相对较大。\n\n3️⃣ **工业物流：现代仓库需求上升**\nAI和电商驱动的现代物流资产需求在增长，但老旧的工业空间则面临挑战。数据中心的竞争也值得关注：新加坡收紧了能效标准，马来西亚反而成为新增容量的热门选择。成本差异明显（新加坡每兆瓦1200万美元 vs 马来西亚700万），加上马来西亚可再生能源更易获取，增量需求自然外溢。\n\n4️⃣ *\n\n[... middle omitted ...]\n\nustrial assets, and moderation in residential demand. Across all sectors, supply remains constrained in the highest-quality segments, with prime CBD offices, premium suburban malls, modern log\n\n[... middle omitted ...]\n\nResearch. Subject also to msci.com/disclaimer\n\nSustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1)\n\nCompleted 08 Jul 2026 09:11 AM HKT"
  },
  {
    "id": "R023",
    "title": "JPM：半导体设备利润率改善或提前兑现，JPM看好定价权驱动增长",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：半导体设备利润率改善或提前兑现，JPM看好定价权驱动增长\n\n市场对AI主题的担忧让半导体相关公司近期出现调整，但JPM最新发布的日本半导体与材料板块季度展望给出了一个与市场情绪不同的判断：不仅WFE（晶圆制造设备）市场增速预期被上调，且设备厂商的利润率改善可能比公司自身指引来得更快。这份报告的核心观察在于，行业正从“靠需求拉动增长”转向“靠定价权重塑利润结构”，而后者才是这一轮财报季真正需要验证的变量。\n\n报告覆盖了半导体、玻璃基板、水泥三个子行业，但重心明确落在半导体设备。JPM在6月17日上调了WFE市场展望，预计2026年同比增长28%，2027年增长29%，2028年增长16%。这个增速序列意味着，市场此前对AI资本开支周期见顶的担忧可能被高估了。更关键的是，报告认为这一预测仍有上行空间——不是基于更乐观的需求假设，而是基于设备厂商正在推进的定价策略调整。\n\n> **KC评论：** 这份报告最有价值的部分不是WFE增速数字本身，而是它把“涨价”和“利润率改善”作为独立于需求周期的变量来讨论。读者在阅读完整报告时，应该重点关注Tokyo Electron和Advantest在定价和利润率方面的具体表述，以及Kioxia在NAND价格趋势上的信号——这些才是判断本轮设备周期能否从“量增”切换到“价利双升”的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Tokyo Electron的利润率目标可能提前实现，涨价是核心催化剂\n\n在上一季度（1-3月）的业绩发布会上，Tokyo Electron提出了一个中期目标：两年内将毛利率提升至50%。JPM的判断是，这一目标可能比公司预期更早实现。报告没有给出具体的提前时间表，但明确指出“我们预期它将更早实现”——这个措辞暗示，分析师基于对订单结构、定价\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n半导体研报拆解：这3个方向被持续关注\n\n📈 研究信号拆解\n\n近期某外资机构更新了日本半导体/技术材料板块的财报前瞻，核心排序：半导体 > 玻璃 > 水泥。\n\n**1/ 半导体：WFE景气度仍在上升**\n研报6月上调了WFE市场预期，预计2026年增长28%、2027年29%、2028年16%，且认为仍有向上空间。重点看3家：\n- Kioxia：关注价格趋势、LTA方向、Super High IOPS进展\n- Tokyo Electron：此前提到计划2年内将毛利率提升至50%，研报认为可能提前实现\n- Advantest：除GPU/ASIC外，CPU和CPO的TAM增长可能带来额外回报弹性\n\n**2/ 玻璃材料：产能扩张是关注重点**\nNittobo近期报价因竞争担忧有所调整，但研报对长期定位仍持正面看法。虽然4-6月财报可能不会公布具体扩产计划，但M9用NER-glass和MLC用T-glass的TAM增长值得关注。NEG方面，7月6日宣布的玻璃纤维业务重组细节是重点。\n\n**3/ 水泥：国内需求平稳，关注海外**\n国内需求保持稳定，各公司提升产能利用率的具体措施（出口扩张、减产、合作）是FY2026的关键\n\n[... middle omitted ...]\n\ntill upside potential. Amid discussions about price revisions, we are also watching for initiatives to raise profit margins without relying solely on demand. Key focus points in the glass subs\n\n[... middle omitted ...]\n\n THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer"
  },
  {
    "id": "R024",
    "title": "JPM：SpaceX不只是火箭公司，JPM称其是AI基础设施新玩家",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：SpaceX不只是火箭公司，JPM称其是AI基础设施新玩家\n\nSpaceX在2025年实现了187亿美元收入，但真正值得关注的不是这个数字本身，而是这家公司正在同时押注三条增长曲线——发射、卫星通信和AI基础设施——并且每条曲线都指向一个共同目标：到2030年前后触及1万亿美元的年收入。JPM在最新发布的覆盖报告中给出了一个大胆但并非空想的判断：SpaceX有能力在2031年达到9560亿美元营收，距离马斯克提出的1万亿美元目标仅差约5%。支撑这一判断的，不是单一业务的爆发，而是三块业务的协同演进。\n\n报告将SpaceX的定位从“商业航天公司”重新定义为“横跨太空、连接和AI的基础设施平台”。这个框架本身就在回答一个问题：为什么一家发射火箭的公司，估值逻辑应该对标科技巨头而非传统航天企业？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 发射业务是结构性护城河，但不再是增长天花板\n\nSpaceX已完成约670次轨道发射，成功率超过99%，自2023年以来承担了全球80%以上的入轨质量。猎鹰系列火箭的成熟度已经让发射变成一项近乎公用事业的服务。但JPM认为，真正的变量在于星舰V3能否将年发射量从目前的数十次提升到2030年代初的每年5000次。\n\n这个数字听起来激进。报告给出的路径是：2027年发射40次，2028年300次，2029年1000次，2030年2500次。关键在于星舰的可重复使用率和周转时间——如果每艘星舰平均飞行次数从3次提升到16次，周转时间从52天压缩到23天，5000次年发射在物理上是可能的。\n\n> **KC评论：** 5000次发射的假设是整份报告最核心的“杠杆点”。如果星舰产能或周转速度达不到预期，太空数据中心和宽带扩容都会同步受限。值得在原文中仔细看那张发射供需表，它把每个假设\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 星舰要造太空数据中心\n\n🚀 下一个前沿观察\n\n某机构最新研究分析：SpaceX 正同时布局三条万亿级赛道，目标是2028年营收突破千亿美元。\n\n1️⃣ 星舰产能是关键变量\n预计到2031年实现年发射5000次，2028年开始部署轨道AI计算。每颗V3卫星的下行容量是V2-Mini的11倍，需要星舰大规模量产来支撑。\n\n2️⃣ 星链宽带稳步扩张\n预计美国住宅宽带份额从3%提升到8%（2030年）。核心用户群集中在铜缆和未充分投资的有线电视市场，对光纤威胁有限。\n\n3️⃣ 地面AI算力加速建设\n预计2028年建成约9GW算力，成本比同业低29-43%。已与Anthropic和谷歌签订租约，租金远高于当前Grok变现水平。\n\n4️⃣ 轨道AI数据中心计划\n2028年开始发射首批AI卫星，年末实现0.4GW在线，2031年扩至75.1GW。需要半导体行业同步提升芯片供给。\n\n5️⃣ 与特斯拉合并可能性上升\n未来1-2年概率提升，但不急于近期。全股票收购可能是最可行的方案，整合后TAM达约28.5万亿美元。\n\n6️⃣ 资金来自传统业务+债务\n2026-2030年预计通过债务融资约3750亿美元，传统发射和星链业务持\n\n[... middle omitted ...]\n\nAs a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single fa\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R025",
    "title": "JPM：转产ABF不是临时措施，载板厂商的定价权将如何变化",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：转产ABF不是临时措施，载板厂商的定价权将如何变化\n\n当多数人还在关注AI算力芯片的封装技术竞赛时，一份来自JPM的台湾载板产业报告揭示了一个更根本的结构性变化：多家亚洲供应商正在将BT载板的生产设备转向ABF载板，部分厂商甚至可能在三年内完全退出BT业务。这不仅是产能调配，更是整个载板行业利润重心的一次迁移。\n\n报告的核心判断是：BT产能转产ABF，对载板厂商的收入和利润率都将产生净正面影响，因为ABF的利润率明显更高。但这条路径并非没有摩擦——短期内的BT供应扰动，将迫使手机SoC厂商重新调整采购策略，而订单外溢效应可能惠及二线厂商。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI驱动的载板需求正在重塑产能配置\n\nAI芯片对核心层数和大尺寸封装的要求，正在推动ABF载板需求快速攀升。日本和奥地利载板厂商近期的扩产公告已经印证了这一点。JPM的供应链调研显示，多家亚洲供应商正将原本用于消费电子和存储芯片的BT载板设备，转移至ABF产线。\n\n这种转产策略为ABF提供了及时的产能补充，但代价是BT供给侧的收紧。报告预计，部分载板厂商可能在三年内彻底退出BT业务。这意味着，BT载板市场的玩家结构将发生根本性变化，而ABF将成为赢家。\n\n> **KC评论：** 转产不是临时措施，而是战略选择。当ABF利润率显著高于BT时，厂商没有理由继续保留低利润业务。关键在于，这种转产是否会成为行业共识，进而改变整个载板市场的定价权和竞争格局。\n\n## 2. BT供给扰动：短期阵痛，但价格弹性可能被低估\n\n转产带来的直接后果是BT载板供给出现缺口。JPM指出，2025年中期以来，BT价格已在1-2个季度内上行，主要受存储芯片需求上升和供给增长有限的共同推动。虽然尚未看到新一轮大规模涨价，但报告并未排除这种可能性。\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n芯片基板产能调整，BT向ABF转型观察\n\n封面：BT产能调整，ABF需求上升\n\n副标题：AI应用推动下的基板行业变化\n\n近期有外部研究机构发布了一份关于基板行业产能调整的报告，主要关注点是：部分生产BT基板的厂商，正在将产线转向ABF基板的生产。\n\n1/ BT基板主要应用于消费电子和存储芯片领域，而ABF基板则是AI芯片、高性能计算的关键材料。随着AI相关需求的增长，ABF基板的市场需求持续上升，其市场表现和利润空间也相对更优。\n\n2/ 多家亚洲供应商已开始行动——将BT产线的设备转移至ABF产线。研究判断，这一转型对基板厂商的收入和利润表现有积极影响（ABF的利润表现明显更好）。甚至有部分厂商可能在三年内完全退出BT业务。\n\n3/ 短期来看，BT基板的供给可能会出现一定紧张。主要手机SoC厂商的采购计划需要相应调整。BT价格在2025年中后已出现一定幅度的上涨，持续了1-2个季度，虽然尚未观察到新一轮大规模涨价，但这一可能性也不能完全排除。\n\n4/ 溢出订单将流向二线台湾厂商，以及韩国和中国大陆的部分小型厂商。\n\n这一产业调整，本质上是AI需求推动供应链升级。BT基板可视为“现有产能”，ABF则是“新兴产能”，\n\n[... middle omitted ...]\n\nddition to ABF. We believe the results of conversion will be net-net positive for both rev and margin for substrate makers (ABF margin meaningfully higher). We believe some substrate makers co\n\n[... middle omitted ...]\n\n losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.\n\nCompleted 08 Jul 2026 06:32 AM HKT"
  },
  {
    "id": "R026",
    "title": "JPM：特斯拉与SpaceX合并，JPM指市场低估中国变量",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：特斯拉与SpaceX合并，JPM指市场低估中国变量\n\n将SpaceX与特斯拉合并在纸面上逻辑自洽，但JPM最新报告指出，市场低估了监管障碍的复杂性，尤其是中国这一关键变量。报告认为，SpaceX高达1.77万亿美元的IPO为合并提供了高价值收购货币，而马斯克近期将特斯拉投票权提升至约20%也增加了控制力。但真正的门槛，是特斯拉在中国的制造版图与SpaceX的国防背景之间的根本冲突。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 运营整合已深，但中国监管才是真正的“房间里的象”\n\nJPM分析师指出，SpaceX与特斯拉之间的运营联系已经相当紧密。双方共享工程人才、AI基础设施，以及位于德克萨斯州的Terafab芯片设施。SpaceX购买了特斯拉的Megapack电池和Cybertruck，特斯拉则向xAI研究了20亿美元。SpaceX第一季度101亿美元资本支出中的76%投入了AI，而特斯拉计划在2026年投入约250亿美元用于AI、机器人和芯片。\n\n但报告真正着墨的，是中国的特殊挑战。特斯拉在中国拥有规模可观且盈利的制造基地，而SpaceX与美国国防部和NASA的合同关系，以及星链在中国未获批准的事实，形成了难以调和的矛盾。JPM认为，这种国家安全敏感性可能成为中国审批的关键障碍。\n\n> **KC评论：** 特斯拉过去能以非中国OEM身份在中国保有全资工厂，靠的是与中国市场的利益绑定。但如果合并后SpaceX的国防业务成为特斯拉的一部分，这种平衡可能被打破。报告没有给出答案，但暗示了路径：特斯拉可能需要证明合并不会改变其在中国市场的独立性。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 投票权不对称与估值差距，指向SPCX主导的收购\n\n马斯克控制着Spac\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n星舰与特斯拉，合体逻辑在哪？\n\n**封面短标题：** 合体逻辑拆解  \n**封面副标题：** 星舰IPO后，特斯拉会变天？\n\n某外资机构最近发布了一份研究，专门分析SpaceX和特斯拉合并的可能性。逻辑上很有看点，但现实阻力也不少。\n\n**1/ 为啥要合体？**\n两家公司已经在共享资源：工程人才、AI基础设施、德州那个规模可观的Terafab芯片厂，以及马斯克本人的领导力。商业上也有实际案例——SpaceX采购了特斯拉的Megapack电池和Cybertruck，特斯拉向xAI投入了20亿美元（现归入SpaceX）。更关键的是，两家都把AI作为核心方向：SpaceX一季度101亿美元资本开支中76%投向AI，特斯拉2026年预计投入250亿美元用于AI、机器人及芯片。马斯克一贯倾向于整合，将AI生态收归一个体系，逻辑上较为顺畅。\n\n**2/ 阻力在哪里？**\n最核心的是**监管**。SpaceX有NASA和五角大楼的合同，特斯拉在中国有大量制造业务（且Starlink尚未在中国获批），这些涉及国家安全的环节会触发多国审批。此外，**投票权不对称**是一个重要问题——马斯克控制SpaceX约85%投票权，但特斯\n\n[... middle omitted ...]\n\ny. That said, we think recent press reports understate the practical bottleneck of securing multi-jurisdictional regulatory approvals, especially in markets where TSLA has meaningful manufactu\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R027",
    "title": "JPM：资源价格高位已成明牌，日本商社真正催化剂是回购计划",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：资源价格高位已成明牌，日本商社真正催化剂是回购计划\n\n日本综合商社和能源板块即将进入一季度财报季。JPM最新报告给出的判断很直接：利润本身不再是报价的推动力。资源价格高位带来的业绩同比改善已是明牌，市场真正在等的，是各家商社能否拿出真金白银的回购计划。\n\n这份覆盖七大商社、三家炼油商和INPEX的季度展望，核心信号只有一个——当资源价格从高点回落，市场对日本商社的定价逻辑正在从“赚了多少”转向“愿意分多少”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n![研报原图 2](assets/source_image_02.jpg)\n\n![研报原图 3](assets/source_image_03.jpg)\n\n**资源价格推高利润，但市场已经计价**\n\n报告测算，2026财年一季度（4-6月），七大商社的净利润进度大概率在23%-30%之间。三井物产有望达到30%，丸红和三菱商事均为29%，伊藤忠和丰田通商27%，住友商事26%，双日因季节性因素只有22%。这样的进度放在历史数据中属于偏强水平。\n\n背后推手是资源价格的大幅上涨。布伦特原油一季度均价97美元/桶，同比上涨45%；LME铜价13355美元/吨，同比涨幅超过40%；焦煤238.8美元/吨，同比也接近30%。但报告特别提醒，商社的能源项目收益存在三个月时滞，一季度财报实际反映的是1-3月的资源业务表现。换句话说，这份利润的“含金量”已经被市场提前消化。\n\n> **KC评论：** 利润进度亮眼，但报告真正想说的是“这已经是过去时”。资源价格见顶后，市场对商社的下一步预期需要新的变量来支撑。完整报告中对各家商社的利润结构拆解和资源价格敏感性分析，比利润数字本身更有参考价值。\n\n**回购才是真正的催化剂**\n\n报告对商社板块的研究评级是“中性”。原因在于，既然利\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n日本商社炼油厂最新业绩前瞻\n\n📊 商社板块近期动态观察\n\n**一、业绩进度：Q1普遍符合预期**\n7大商社Q1净利润预计完成全年指引的23-30%。资源价格同比有所上涨（布伦特原油$97/桶、铜$13,355/吨），但利润计入存在约3个月滞后，因此Q1实际反映的是1-3月业绩。除双日外，其余6家进度均超过25%，三井物产以30%领先。\n\n**二、市场关注点：聚焦公司策略**\n研报认为，业绩表现本身可能不会成为市场关注的核心——资源价格已处于阶段性高位。市场更关注的是：\n- 三井物产和三菱商事是否宣布回购计划（三井预计至少2000亿日元）\n- 伊藤忠是否执行全年3000亿+计划中的回购（预估约200亿）\n- 丸红是否追加回购（可能性存在，但更可能在Q2财报时宣布）\n\n**三、炼油板块：表现分化**\nENEOS利润同比+41%表现较强（受益于JX金属股票出售收益），出光兴产和Cosmo分别-13%和-53%。中东局势导致阿布扎比油田停产，替代原油采购成本未能完全转嫁到产品价格。经产省已宣布7月起将替代原油成本纳入补贴计算。\n\n**四、INPEX看点**\nQ2净利润预计1210亿日元，同比+24%。Ichthys \n\n[... middle omitted ...]\n\nbl for Brent crude (\\$78.4/bbl in January-March 2026, \\$66.7/bbl in April-June 2025); \\$13,355/t or \\$6.05/lb for LME copper (\\$12,824/t or \\$5.82/lb in January-March 2026, \\$9,508/t or \\$4.31\n\n[... middle omitted ...]\n\ned by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not\n\nCompleted 08 Jul 2026 10:10 AM JST"
  },
  {
    "id": "R028",
    "title": "关于万华化学的一份研究笔记",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# 关于万华化学的一份研究笔记\n\n市场对万华化学的关注，过去几个月集中在MDI价差收窄和油价走弱上。报价从4月高点回落超过20%，同期上证指数几乎未动。市场情绪似乎已经充分反映。\n\n某机构最新发布的研究报告给出了一个不同的判断：万华化学二季度净利润预告远超预期，隐含的季度利润达到61亿至67亿元，环比增长68%至80%，创下公司历史上第二高的单季利润。这份报告的核心结论是，利润超预期的主要驱动力并非传统MDI业务，而是一个更结构性的变量——其烟台乙烯裂解装置成功完成原料切换，从油基转向乙烷基。\n\n这意味着，万华正在经历一次成本曲线的重塑，而市场对此的认知可能仍停留在旧框架里。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 乙烷裂解的宏观环境性，正在改写万华的利润结构\n\n报告明确指出，二季度利润超预期，很大一部分来自万华烟台100万吨乙烯裂解装置。该装置在2026年1月完成从丙烷到乙烷的原料切换，并实现满负荷运行。这一切换的时机极为关键。\n\n在油价处于每桶70至80美元的区间时，乙烷裂解（ECC）的成本优势明显优于传统石脑油裂解（NCC）。数据显示，亚洲乙烯利润在4月和5月较2月显著提升，因为聚乙烯（PE）价格季度环比上涨超过30%，而美国乙烷价格基本持平。即便随后油价回落，亚洲PE现货价格仍比冲突前水平高出15%。\n\n> **KC评论：** 乙烷裂解的核心逻辑不是赚产品价格波动的钱，而是赚原料价差的结构性钱。万华把一套原本烧油的装置改成了烧乙烷，相当于在化工周期底部给自己装了一个成本减震器。报告没有完全展开的一点是，万华二期120万吨裂解装置具备石脑油和乙烷灵活切换能力，这给了它在不同油价环境下动态调节利润率的期权。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. MD\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 万华化学，近期表现观察\n\n某外资机构近期发布报告，对万华化学（600309）给出积极评价。核心观点是：**公司盈利可能已阶段性企稳，第二季度业绩表现突出，新业务逐步显现成效。**\n\n1️⃣ **第二季度业绩表现亮眼，历史第二高**\n- 公司预告上半年净利润98-104亿，其中第二季度单季61-67亿，环比增长68-80%，同比增幅明显。\n- 这是公司历史上单季第二高利润，超出市场普遍预期。\n\n2️⃣ **业绩超预期的原因：两大因素共同作用**\n- **MDI/TDI价差扩大**：海外部分产能因区域因素停产（全球约4%的MDI、6%的TDI），国内MDI/TDI价格环比上涨1560元/吨和635元/吨，对利润形成支撑。\n- **乙烯装置切换成功**：烟台1期乙烯裂解装置从油头切换为乙烷，1月实现满产。乙烷裂解成本低于石脑油路线，第二季度贡献了可观的增量利润。\n\n3️⃣ **乙烷裂解：未来2-3年的关注重点**\n- 在油价70-80美元的环境下，乙烷裂解相比传统石脑油路线，成本优势较为明显。\n- 目前亚洲PE价格较冲突前仍高15%，而美国乙烷价格保持稳定，价差空间依然存在。\n- 报告认为，该装置带来的利润弹性\n\n[... middle omitted ...]\n\nrice has declined >20% since 13 April (vs SHCOMP flat) on the back of lower oil prices and a fall in MDI/TDI spreads. We believe weakness is priced in, and see potential for a recovery in marg\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R029",
    "title": "MS：阿里即时零售亏损收窄超预期，电商稳利润控亏损",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：阿里即时零售亏损收窄超预期，电商稳利润控亏损\n\n市场对阿里的关注，过去几个季度一直停在“电商还能不能稳”、“亏损业务何时止血”这些老问题上。但MS最新发布的1QF27预览报告给出了一个值得重新校准视角的信号：云业务的增速和利润改善，正在成为这家公司最值得跟踪的变量，其重要性可能超过电商本身的短期波动。\n\n报告预计阿里云当季收入同比增长45%，高于市场预期的40%，利润率也从9%进一步扩张至11%。这个增速不是一次性脉冲——MAAS贡献的超预期、4月起提价、以及AI相关收入继续三位数增长，都指向云业务有持续加速的能力。与此同时，国内电商的EBITA表现“好于担忧”，即时零售亏损收窄的速度也比预期更快。\n\n换句话说，阿里正在经历一个结构转换：增长引擎从电商向云迁移，而电商业务则从“高增长高投入”转向“稳利润控亏损”的现金牛模式。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 云业务45%的增速背后，是MAAS和AI驱动的结构性升级\n\n这份报告最核心的判断，是阿里云的增速正在从“追赶行业”变成“引领行业”。45%的同比增长，相比上一季度40%的外部增速继续加速，且利润率的改善与规模扩张同步发生——EBITA margin从9%升至11%，距离管理层长期20%的目标还有空间，但方向明确。\n\n驱动因素有三层。第一层是MAAS（模型即服务）贡献超预期，此前管理层设定的季度ARR 100亿目标已提前达成。第二层是AI相关收入继续三位数增长，这部分业务的利润率天然高于传统IaaS。第三层是4月开始的价格调整，叠加MAAS收入占比提升，直接拉动了利润率。\n\n> **KC评论：** 云业务45%的增速和11%的利润率放在一起看，意味着阿里云不再只是“烧钱抢份额”的阶段。如果MAAS和AI的贡献持续提升，市场对云业务长期利润\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n阿里云增速达45%，电商亏损收窄幅度优于预期\n\n云业务持续增长，电商业务改善\n\n根据某机构最新观察，阿里1Q27业绩有望呈现积极变化：主要关注点在于云业务增长加快和本地生活亏损快速收窄。\n\n1⃣ 云业务是主要亮点\n- 营收同比增长45%，高于市场普遍预期的40%\n- 利润率从9%提升至11%\n- 驱动因素：MaaS（模型即服务）贡献持续扩大，AI相关收入保持较高增速\n- 4月调整价格后利润率仍有提升空间，长期目标20%\n\n2⃣ 电商业务：亏损收窄好于预期\n- 快消业务（QC）亏损收窄至100亿（上季度为180亿）\n- 主要依靠客单价提升改善单位经济\n- 中国电商整体EBITA仅同比下降2%，优于市场此前预期\n\n3⃣ 其他业务也在改善\n- 其他板块亏损缩减至165亿（上季度为210亿）\n- 但通义千问模型训练费用仍在较高水平，后续将逐步披露明细\n\n机构维持积极评级，目标价从190美元调整至180美元，主要因上调云业务收入预估但小幅下调电商预期。当前估值对应FY28 PE约13倍。\n\n你觉得阿里云的45%增速能否持续？欢迎一起交流。\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru\n\n[... middle omitted ...]\n\n(vs 40% external in 4Q), EBITA margin to expand to 11% (vs 9% in 4Q).\n\nCMR +1-2% YoY on a LFL basis (vs 7-8% in 4Q). E-com EBITA (ex QC) -3-4% YoY. QC losses narrow to Rmb10bn (vs MSe Rmb18bn \n\n[... middle omitted ...]\n\nom Group Ltd (TCOM.O)</td><td>O (05/17/2021)</td><td>US$40.81</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R030",
    "title": "MS：MS拆解中国医药全球化，不是卖资产，而是全球买家排队采购",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：MS拆解中国医药全球化，不是卖资产，而是全球买家排队采购\n\n这份MS的中国医疗健康暑期学校报告，核心判断并不复杂：中国创新药不再只是“低成本仿制”的代名词。从2025年到2026年上半年，一批总额数十亿美元的跨境交易，正在改写全球药企的研发管线地图。报告认为，中国生物医药的全球化已从单纯的“工程化能力”升级到“2.0时代”——更多新机制、新疾病领域和下一代技术正在涌现。\n\n为什么这个判断值得关注？因为全球大型药企正面临2025-2030年间大量专利到期的不确定性。报告数据显示，部分跨国药企到2030年底将失去超过40%的2025年收入来源。填补这一缺口的需求，与中国生物技术公司日益增强的研发能力和融资韧性形成了结构性匹配。\n\n> **KC评论：** 这不是一个“中国公司卖资产”的故事，而是一个“全球买家排队采购中国管线”的结构性变化。报告中最值得细看的是那张“全球药企专利悬崖”图表——它解释了为什么跨国药企愿意支付越来越高的首付款。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. BD交易从“单笔买卖”升级为“组合式战略合作”，恒瑞医药成为典型案例\n\n报告列出的2025-2026年上半年中国生物医药前15大交易，呈现出一个明显趋势：交易规模在急剧放大。CSPC与阿斯利康的18.5亿美元总交易额、恒瑞与百时美施贵宝的15.2亿美元合作、信达与辉瑞的10.5亿美元战略伙伴关系——这些数字背后是交易结构的根本变化。\n\n恒瑞医药的案例值得拆解。报告显示，恒瑞与BMS的合作不仅是简单的对外授权，而是包含了共同开发、共同商业化选项和反向授权。此外，恒瑞通过NewCo模式将GLP-1资产剥离至Kailera，后者已于2026年4月在纳斯达克上市，恒瑞持有13.6%股权。这种“对外授权+股权收益+共同商业化”的复合结构，\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n### 中国创新药出海，进入2.0时代\n\n**中国药企全球化新逻辑**\n\n某研究机构近期报告指出，中国创新药出海正从“工程化模仿”迈向“2.0时代”——更新颖的机制、更广的疾病领域、更前沿的技术。\n\n**1. 交易模式升级，不再只是“卖产品”**\n过去是单纯对外授权，现在演变为新公司、共同商业化、战略联盟等复杂模式。恒瑞医药与BMS的13个管线合作就是典型：既有授权引入，也有联合开发，甚至反向授权，交易总额达152亿美元。\n\n**2. 全球药企的“专利悬崖”催生需求**\n报告测算，全球大药企到2030年将面临大量核心产品专利到期。这为中国biotech创造了窗口——跨国药企急需补充管线，而中国资产凭借成本、速度和临床验证优势成为首选。\n\n**3. 中国biotech的“自我造血”能力增强**\n过去依赖融资，现在通过BD交易获得大量预付款（如CSPC与AZ的12亿美元首付款），加上资本市场退出路径更清晰（如恒瑞的GLP-1资产通过新公司在纳斯达克上市），企业越来越“不差钱”。\n\n**4. 供应链优势：人才、成本、效率**\n中国STEM毕业生数量远超美国，临床试验成本仅为美国1/3-1/5，且IND审评已缩短至3\n\n[... middle omitted ...]\n\n94d6de497ff3ad4ff0ac.jpg)\n\n## CHINA HEALTHCARE\n\nAsia Pacific\nIndustry View Attractive\n\nMS does and seeks to do business with companies covered in MS. As a result, investors should be aware tha\n\n[... middle omitted ...]\n\no. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb12.85</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R031",
    "title": "JPM：散户不再一起买什么才是市场真正信号",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：散户不再一起买什么才是市场真正信号\n\n散户资金上周加速入场，ETF和公司净观点偏积极均处高位。但JPM在最新一期Retail Radar中发现，一个更值得关注的信号已经出现：动量因子正在退潮，散户的操作从一致追涨，分裂为“底部观察部分明星股”与“观点偏谨慎其他高位股”两种截然不同的行为。这轮变化真正考验的，是市场能否在动量退潮后找到新共识。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 动量拥挤度从极值回落，散户不再“一起买”\n\nJPM自建的动量拥挤度指标已从接近100%的高位回落至98.6%。虽然相对值仍高，但趋势拐点清晰。报告特别指出，半导体板块是这轮动量节奏变化的主要影响。散户在High Momentum组合中的操作出现了明显分化：他们继续观点偏积极Sandisk（SNDK）和Micron（MU）这类年度明星股，但对Applied Materials（AMAT）、Western Digital（WDC）、KLA Corp（KLAC）和Marvell Technology（MRVL）却选择了观点偏谨慎。同一个板块，同一个动量因子，散户的判断已经不再统一。\n\n> **KC评论：** 散户的分化通常发生在市场情绪从“一致看多”转向“选择性相信”的阶段。报告没有直接说这轮回调是否见底，但散户从追涨到挑标的转变，本身就是一个值得跟踪的情绪信号。完整报告里对半导体各子行业的资金流向拆解，值得仔细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. SpaceX上市后的散户行为，提供了一个新的观察样本\n\nSpaceX（SPCX）是本期报告最突出的个案。该公司6月12日登陆纳斯达克，散户获得了约20%的IPO配售份额，远高于通常的5%。上市首周，散户净观点偏积极达11\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n散户行为出现分化迹象\n\n**散户操作分化阶段**\n\n一边保持观察一边调整持仓，趋势跟随策略有所减弱\n\n---\n\n上周散户整体净买入力度偏强，但内部已出现明显分化。📉\n\n**1️⃣ 趋势跟随减弱，半导体板块率先体现**\n趋势拥挤度指标从接近100%降至98.6%，涨幅较大的半导体个股，散户操作开始出现不同方向：\n- 继续观察今年热门品种：SNDK（+2.3z）、MU（+0.3z）\n- 适时调整弱势品种：AMAT（-3.4z）、WDC（-3.0z）、KLAC（-2.9z）\n\n**2️⃣ 能源板块短期活跃**\n地缘因素推动油价重回80美元上方，散户买入能源股升至92%分位。但油类ETF需求一般，做空油价的SCO反而被平仓（-1.5z）——说明这波跟进偏短线。\n\n**3️⃣ SpaceX上市首周散户占比20%**\n远高于常规的5%，前三天报价涨幅约50%。研报预期2025-2030年营收CAGR达91%，核心看点是Starship从2026年几次发射到2031年5000次——这个时间跨度较长。\n\n**4️⃣ AI上游设备股集体调整**\nGEV、CAT、CMI在7月1日同步下跌约7%，原因是市场对AI资本开支前景产生讨\n\n[... middle omitted ...]\n\nound of strikes against Iran and oil rebounded above \\$80, retail buying in Energy stocks climbed to their 92%ile on Wednesday. However, oil ETFs only saw moderate demand, e.g. BNO (1.0z) and \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jul 2026 10:18 PM EDT\n\nDisseminated 08 Jul 2026 10:18 PM EDT"
  },
  {
    "id": "R032",
    "title": "MS：AI芯片的“库存担忧”被高估了，2027年才是真正的放量年",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：AI芯片的“库存担忧”被高估了，2027年才是真正的放量年\n\n市场对AI芯片库存的讨论，最近有些过度。MS最新发布的AI供应链追踪报告，给出了一个直接且有力的判断：Blackwell芯片所谓的“库存”，本质是供应链缓冲，到2026年将被完全消化，无需担忧。更关键的是，这份报告首次系统性地拆解了2027年的CoWoS产能分配与芯片出货量，揭示出一个被当前讨论忽视的结构性趋势——AI芯片的竞争格局，正在从“GPU单极”走向“GPU+ASIC双轮驱动”。\n\n这份报告最值得关注的，不是某个季度的出货预期修正，而是它提供的2027年全局视图。当市场还在为季度波动争论时，MS已经用数据证明：AI基础设施的研究周期远未结束，只是驱动力正在发生变化。\n\n> **KC评论：** 报告的真正价值不在于预测数字本身，而在于它给出了一个可验证的框架——用CoWoS产能反推芯片出货，再折算成HBM消耗和整机需求。这比单纯跟踪季度出货更接近真实需求。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AMD的CoWoS分配不变，但执行不确定性是2027年的关键变量\n\n市场对AMD的CoWoS分配有过疑虑。MS维持了AMD 2027年24万片CoWoS的预期，MI455和MI450合计出货150万颗。但报告也明确提醒：AMD过去有削减CoWoS订单的记录，2027年的执行不确定性不能忽视。\n\n值得注意的结构性变化是AMD产品线的分化。MI455是标准版，面向微软、AWS和Oracle；MI450则是为Meta定制的半尺寸芯片。这种定制化策略，一方面降低了单一客户的依赖，另一方面也意味着AMD正在从“通用GPU供应商”向“半定制化方案商”转型。这对供应链的弹性提出了更高要求。\n\n另一个被忽视的信号是AMD的Venice CPU。作为AMD\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n2027 AI芯片格局：AMD、谷歌、Meta全解析\n\n2027年AI芯片路线图大拆解\n\nCoWoS产能与ASIC定制化趋势\n\n---\n\n最近看到一份关于2027年AI芯片供应链的行业研究，信息量很大，跟大家分享几个关键点。\n\n**1/ AMD的MI400系列来了**\n- MI455标准版：2颗计算芯片+12颗HBM4，面向微软、AWS、Oracle\n- MI450定制版：专为Meta设计，半尺寸芯片，1颗计算芯片+6颗HBM4\n- 2027年CoWoS产能维持24万片，但存在执行风险（之前有过削减订单的记录）\n- 预计MI455出货100万颗，MI450出货50万颗\n\n**2/ 谷歌TPU进度调整**\n- Sunfish芯片主要出货集中在4Q，全年96万颗\n- Zebrafish芯片量产时间不变，仍从4Q26开始\n- 整体节奏往后推，但订单没有被砍\n\n**3/ 英伟达Blackwell的库存真相**\n- 所谓的“库存”其实是供应链缓冲，2026年会被完全消化\n- 2027年预计Rubin系列芯片出货700万颗，NVL72机架9万个\n\n**4/ Meta的ASIC路线**\n- 取消了原2nm芯片Olympus\n\n[... middle omitted ...]\n\ne Moore) CoWoS number. Some MI300 series and upcoming MI500 production will still run in 2027. However, the MI400 series will come in two versions: (1) MI455: the standard version with 2 compu\n\n[... middle omitted ...]\n\no Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$7,705.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R033",
    "title": "MS：AI订单分化，高端ABF基板和MLCC成少数提价方向",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：AI订单分化，高端ABF基板和MLCC成少数提价方向\n\n这份MS研报发布在7月初，覆盖19家日本电子元器件公司，预测4-6月合计营业利润同比增长33.6%。但数字本身不是重点。报告真正想表达的是：AI和数据中心带来的需求仍在扩张，但市场已经消化了这个故事。接下来需要回答的不是“谁在增长”，而是“增长能持续多久、谁在真正积累结构性优势”。\n\n报告把焦点放在了三个维度上：产品组合的含金量、客户锁定能力、以及成本转嫁能力。这不是一个“AI受益公司都能关注”的阶段了。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI订单的分化已经开始，高端ABF基板和MLCC是少数能持续提价的方向\n\n报告明确区分了两类需求。一类是AI服务器和数据中心直接驱动的元器件，包括ABF封装基板和高容MLCC。这些产品的技术门槛高，客户粘性强，而且随着NVIDIA Rubin平台逐步放量，Ibiden的高端ABF基板出货量预计将超过Blackwell平台。另一类是传统消费电子和汽车用元器件，尽管也有增长，但竞争格局更分散，议价权弱。\n\n> **KC评论：** 报告没有明说但逻辑清晰的是，AI对元器件需求的拉动正在从“量增”走向“质变”。能参与Rubin供应链的公司，其产品结构和利润率都会与同行拉开差距。完整报告里有一张Ibiden与Murata的盈利能力对比图，值得细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 村田的盈利质量正在拉开与同行的距离，而太阳诱电的估值已经透支了预期\n\n报告把Murata Manufacturing列为Top Pick，理由不是简单的“AI受益”，而是其高附加值MLCC在AI/DC应用中的销售占比持续提升，叠加核心MLCC产能利用率走高，从而推动了利润率的\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n日本电子元件Q1业绩前瞻\n\nAI驱动盈利持续\n\nAI/数据中心需求继续拉动日本电子元件厂，Q1利润预计同比+33.6%\n\n1️⃣ 核心看点\n- ABF载板（AI芯片封装基板）和MLCC（多层陶瓷电容）是增长主力\n- 铝电解电容面临原材料成本上升影响\n\n2️⃣ 值得关注的公司\n- 村田制作所：高附加值MLCC在AI/数据中心领域占比持续提升，Q1利润有望超预期（预测904亿日元 vs 共识856亿日元）\n- TDK：硬盘磁头和被动元件驱动增长，充电电池业务贡献有限\n- 广濑电机：工业设备和AI服务器连接器双增长\n\n3️⃣ 需观察的公司\n- 揖斐电：短期盈利强劲，但2028年营业利润目标3000亿日元门槛较高，估值偏高\n- 太阳诱电：与村田的盈利差距在拉大（村田高附加值MLCC占比更高）\n- 日本化学电容：下半年盈利指引存在不确定性，估值约50倍PE\n\n4️⃣ 关键时间节点\n- 7月31日：村田、TDK、阿尔卑斯阿尔派等密集发布财报\n- 8月4日：揖斐电、广濑电机\n- 8月5日：太阳诱电\n\n原材料成本是共性因素，但AI需求持续性仍是中期关注重点。欢迎交流。\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[s\n\n[... middle omitted ...]\n\nrata's high-value-added MLCCs to become increasingly evident.\n\nWe also expect Ibiden's earnings expansion to continue over the longer term, but remain UW as market expectations and valuation l\n\n[... middle omitted ...]\n\nmi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥4,250</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS MUFG"
  },
  {
    "id": "R034",
    "title": "MS：中国电动车7月进入淡季，但比亚迪和小鹏的局部亮点值得关注",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：中国电动车7月进入淡季，但比亚迪和小鹏的局部亮点值得关注\n\n7月第一个完整周的数据，给中国电动车市场描绘了一幅“整体降温、局部升温”的画面。MS最新发布的周度订单追踪显示，7月正式进入传统销售淡季，门店客流和订单量预计将普遍回落并趋于平稳。但这份报告的核心价值不在于确认淡季，而在于指出了少数几家车企正在逆势创造自己的小周期。\n\n报告基于6月29日至7月5日的渠道反馈，覆盖了主要电动车品牌。整体而言，季度末冲量结束后，行业进入休整期。但有两家公司的数据变化，值得产业观察者仔细拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪在淡季中展现出超强的产品驱动能力\n\n比亚迪单周订单达到9.09至9.14万辆，环比增长25%，同比增长17%，是本周最突出的表现。驱动因素很明确：海豹08的上市。在行业整体进入淡季的节点，一款新车型的发布能够拉动如此显著的订单增量，说明比亚迪的产品节奏和市场号召力仍处于高位。\n\n> **KC评论：** 比亚迪的这一数据提醒我们，当头部企业拥有足够宽的产品矩阵和密集的迭代周期时，淡季的“季节效应”可以被部分对冲。关键在于，这种能力是否可持续，以及竞争对手能否复制。\n\n## 2. 小鹏MONA M03的预订单量，才是下周真正的观察点\n\n小鹏本周订单约6800辆，环比仅微增2%，但同比大幅下降77%。表面数据并不亮眼。然而，报告指出，MONA M03在首展周末获得了“坚实的预订单”，并且门店客流显著增加。7月16日MONA M03的正式发布，将是检验小鹏能否在20万元以下市场打开局面的关键节点。\n\n理想汽车本周订单环比下降36%，蔚来环比下降14%，两家公司都面临季度末冲量后的正常回落。蔚来还受到ES8五座版即将上市前销量下滑的影响。这些数据本身并不意外，但叠加来看，头部新势力的订\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n夏季电动车订单进入常规调整期，部分品牌表现稳健\n\n夏季订单呈现分化趋势\n\n7月是行业传统调整期，整体门店客流和订单量预计有所回落。但部分品牌凭借新车型发布，依然保持了较好的关注度。\n\n📊 6.29-7.5周订单概览（基于渠道反馈）\n\n1️⃣ **比亚迪**：9.09-9.14万单，环比+25%，同比+17%\n海豹08发布后关注度提升，表现较为突出\n\n2️⃣ **吉利银河**：1.87-1.92万单，环比+10%\n银河战舰700将在7月下旬正式发布\n\n3️⃣ **理想汽车**：0.73-0.75万单，环比-36%\nL8发布后订单回归常规水平\n\n4️⃣ **蔚来**：1.12-1.14万单，环比-14%，但同比+104%\nONVO销量有所放缓，ES8在五座版发布前也有所调整\n\n5️⃣ **小鹏**：0.67-0.69万单，环比+2%\nMONA L03在7月16日发布，预售表现良好，是后续观察重点\n\n6️⃣ **特斯拉中国**：1.1-1.12万单，环比+16%\n\n7️⃣ **问界**：0.8-0.82万单，环比-19%，同比+7%\n\n8️⃣ **极氪**：0.64-0.66万单，环比+12%，同比+83%\n五座版\n\n[... middle omitted ...]\n\nhe past week, BYD, Luxeed, Tesla and Geely Group (Galaxy/Zeekr) delivered standout order intake.\n\n## Weekly order trends in June 29 to July 5 based on channel feedback:\n\nBYD (1211.HK/002594.SZ\n\n[... middle omitted ...]\n\nPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.56</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R035",
    "title": "MS：太空计算的真正起点不是数据中心，是边缘AI",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：太空计算的真正起点不是数据中心，是边缘AI\n\n把数据中心搬到太空，听起来像是科幻小说的场景。但MS一份最新研报给出了更务实的判断：大规模轨道计算基础设施仍是一个长期选项，未来五到十年真正能落地的商业场景，是“轨道边缘AI”——卫星在轨完成图像、传感器数据和推理任务，只把有用结果传回地面。\n\n这份报告的价值不在于描绘一个宏大的太空计算愿景，而在于拆解了哪些技术环节已经成熟、哪些成本曲线正在收敛、以及供应链上哪些公司正在提供真正可交付的组件。对于关注AI基础设施研究的读者，这是一个值得提前建立观察框架的领域。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 轨道计算的宏观环境账正在接近地面AI基础设施\n\n报告给出了一个关键的成本对标：轨道计算每瓦资本支出，预计从2030年的约60美元，下降到2035年的15美元，2040年进一步降至9美元。以五年使用寿命折算，2031年的约6.5美元/瓦/年，已经接近当前行业Blackwell基准的6.8美元/瓦/年。\n\n这个数字的意义在于，它表明轨道计算不再是一个成本无限高的概念验证。驱动下降的因素有三个可追踪的变量：可重复使用发射技术持续降低入轨成本、卫星硬件本身的规模效应、以及计算载荷能效的提升。换句话说，太空不再只是通信中继站的天下，它正在变成一个可以运行AI工作负载的平台。\n\n> **KC评论：** 成本对标是这份报告最值得细读的部分。它给出了一个可验证的假设框架——如果发射成本每下降10%，轨道计算的单位成本改善多少？报告没有完全展开，但这个框架本身就可以用来跟踪关键公司的季度进展。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 供应链机会集中在三大技术层，欧洲两家公司位置突出\n\n报告把轨道计算供应链分为六个层级，但真\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n把AI数据中心，搬到太空去\n\n太空计算，离我们比想象中近\n\n最近某机构发布了一份关于“轨道计算”的研究报告，探讨将AI算力部署到太空的可能性。初看像科幻设定，但逻辑框架较为完整。\n\n1/ 为什么要在太空做计算？\n🌍 地面AI数据中心，超过一半的成本用于基础设施——电力、土地、水资源和散热。\n🛰️ 太空拥有充足的太阳能，散热效率更高（背对太阳的散热器始终处于阴影中）。\n🚀 可复用火箭使发射成本持续下降，太空的“能源成本”正逐步接近地面水平。\n\n2/ 不是飘着的巨型机房\n报告明确指出——并非科幻作品中的大型空间站。\n🔹 是太阳同步轨道上的“机架”，配备太阳能板和散热器。\n🔹 机架之间通过激光在真空中互联，该技术已在现代卫星上应用。\n🔹 更像一个分布式的“轨道边缘AI”，先处理数据，再传回有用结果。\n\n3/ 现在走到哪一步了？\n📌 短期落地场景：轨道边缘AI——卫星在轨处理图像、传感器数据，仅传回关键结果。\n📌 长期图景：太空中的分布式AI基础设施层。\n📌 SpaceX的Starmind是最清晰的蓝图，中国“三体计算星座”已发射首批12颗卫星，目标2800颗。\n\n4/ 成本测算如何？\n报告给出了成本预测（按每瓦计算\n\n[... middle omitted ...]\n\ne linked using lasers travelling through vacuum, which are technologies widely used in modern satellites. These platforms can drive higher cost efficiencies, alleviate terrestrial constraints,\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R036",
    "title": "MS：不是悲观而是低估，村田一季报或成消费电子观察节点",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：不是悲观而是低估，村田一季报或成消费电子观察节点\n\n市场对日本电子元器件龙头村田制作所（Murata Manufacturing）的预期，可能低估了即将到来的一季报。MS在最新发布的战术性观点中判断，该公司将于7月31日公布的2027财年第一季度业绩有望超出市场共识，并推动报价在未来60天内跑赢日本大盘。\n\n这不是一个模糊的“看好”判断。报告给出了明确的数字锚点：MS预测一季度营业利润为904亿日元，而FactSet共识预期为856亿日元。同比来看，上年同期仅为616亿日元，环比也高于上一季度的788亿日元。分析师认为，这一超预期的概率超过80%。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 超预期的基础在于高端智能手机需求的持续韧性\n\n村田的核心产品——多层陶瓷电容（MLCC）、高频元件和MetroCirc基板——与高端智能手机的出货量高度相关。报告提到的不确定性因素中，高端智能手机需求强弱被列为最关键变量。\n\n当前市场对消费电子复苏的节奏仍有分歧，但村田的一季度表现可能证明，高端机型的需求比部分预期更为稳定。苹果供应链的订单能见度、安卓旗舰机型的拉货节奏，都可能成为超预期的具体来源。值得注意的是，报告强调汇率影响同样不可忽视：每1日元兑美元波动，将影响村田营业利润约45亿日元。\n\n> **KC评论：** 村田作为MLCC行业的定价者，其业绩不仅是自身经营状况的反映，更是整个消费电子产业链健康度的温度计。如果一季度利润真的超出预期，可能意味着下游库存去化已基本完成，补库周期正在启动。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 战术性观察的窗口期只有60天\n\n这份报告被明确标注为“Research Tactical Idea”，而非长期基本面分析。MS\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n村田制造：财报前的观察窗口\n\n封面：村田的潜在关注节点\n\n财报前值得关注的信号\n\n某外资机构近期发布了一份关于村田制造（6981）的观察观点，认为未来60天内，其市场表现可能优于日本大盘。核心逻辑围绕即将公布的财报展开。\n\n1️⃣ 财报预期差是关键\n- 村田将于7月31日下午2点公布2027财年第一季度业绩。\n- 该机构预测其营业利润为904亿日元，远超去年同期的616亿日元，也高于市场一致预期的856亿日元。\n- 关键点：如果实际数据超出共识，财报发布后市场表现可能获得正向反馈。\n\n2️⃣ 概率评估与风险提示\n- 该机构认为该情景发生的概率超过80%（即“高度可能”）。\n- 但需注意，这一概率是主观评估，并非精确预测。\n- 上行风险：高端智能手机需求超预期，带动MetroCirc、MLCC和射频器件销售。\n- 下行风险：全球经济波动影响核心产品需求；高端手机需求变化；日元每升值1日元，营业利润预计减少45亿日元。\n\n3️⃣ 估值与评级\n- 当前报价9212日元，目标价12500日元，评级为“超配”。\n- 估值基于DCF模型，假设无风险利率2.6%，股权风险溢价3.2%，WACC为6.1%。\n\n研报解读：核心\n\n[... middle omitted ...]\n\nity for the scenario.\n\nEstimated probabilities are illustrative and assigned subjectively based on our assessment of the likelihood of the scenario.\n\n<table><tr><td colspan=\"2\">MS MUFG SECURIT\n\n[... middle omitted ...]\n\nmi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥4,250</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS MUFG"
  },
  {
    "id": "R037",
    "title": "MS：人形机器人2026年中国出货5万台，供应链比整机更受益",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：人形机器人2026年中国出货5万台，供应链比整机更受益\n\n资本开支的扩张周期还没有结束，但这轮增长的结构已经和2025年完全不同。MS在最新发布的中国工业2026年中展望中给出了一个清晰判断：整体资本开支在下半年仍将保持强劲，但1H26各子板块报价表现已经出现明显分化，接下来选股不仅要看订单和收入动能，还要叠加盈利质量、催化剂和估值。\n\n这份报告覆盖了自动化、机器人、AI数据中心设备、工程机械等多个领域。核心信号是：AI驱动的资本开支仍是主线，但“卖铲子”的公司比直接做AI应用的公司更具确定性；人形机器人正从展示阶段进入小批量商业化，2026年中国出货量预计达到5万台；而传统基建承包商、铁路设备和光伏制造设备，则被列为最不偏好的方向。\n\n**报告的真正判断不是“资本开支还在涨”，而是“这轮资本开支的质量和分布已经变了”。** 理解这一点，比押注某个子板块的增速更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI资本开支超级周期仍在加速，但收益正在向“铲子”集中\n\nMS对美国前14家云服务商的资本开支追踪显示，2026年全球云资本开支预计达到9160亿美元，同比增长92%。中国前6家科技公司的年度资本开支预计在2026/27年分别超过6000亿和7000亿元人民币。\n\n这些数字本身已经很大，但报告关注的不是总量，而是结构。随着AI芯片快速迭代（从GB200到Rubin架构），设备升级周期被大幅压缩，这直接拉动了PCB、连接器、冷却系统等“卖铲子”环节的需求。以Rubin机架为例，其PCB单机价值量比GB300增长了233%。\n\n> **KC评论：** 报告没有直接说，但隐含的逻辑是：AI硬件迭代越快，设备公司受益越确定。真正的不确定性在于——当芯片迭代速度节奏变化后，这批公司的增长故事还能讲多久？\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n下半年工业研究观察，4条主线逐步显现\n\n下半年工业领域资本开支保持活跃\n\n1️⃣ 自动化进入明确上行周期\n自动化市场预计2026年同比增长5%左右\n伺服、工业机器人增速领先\n国产化率持续提升（伺服已达60%）\n\n2️⃣ 人形机器人开始小规模商业化\n预计2026年中国出货5万台\n未来5年增长9倍\n核心零部件（轴承、减速器、电机）需求增长\n\n3️⃣ AI基础设施投入不减\n全球云资本开支2026年约9160亿美元\n同比增长92%\n设备迭代加速，PCB等环节价值量提升\n\n4️⃣ 出口持续走强\n工程机械、液压件等海外拓展加速\n国产供应链成本优势明显\n\n关注度相对较低的方向：传统基建、铁路设备、光伏设备\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.md]\nJuly 7, 2026 03:42 AM GMT\n\nInvestor Presentation | Asia Pacific\n\n# China Industrials Mid-year Outlook\n\nCapex should remain broadly strong across the sub-sectors we cov\n\n[... middle omitted ...]\n\nmanoids in early commercialization with intensive catalysts -> Leaderdrive, Shuanghuan, Hengli Hydraulic.\n\n\\- Beyond AI, a broadening capex upcycle -> Hongfa, Bochu, Wuxi Lead.\n\n\\- Export stre\n\n[... middle omitted ...]\n\nHeavy Industry (1157.HK)</td><td>O (09/08/2025)</td><td>HK$7.10</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R038",
    "title": "MS：轨道边缘计算不是科幻，MS拆解供应链机会",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "MS",
    "digest": "[wechat_article.md]\n# MS：轨道边缘计算不是科幻，MS拆解供应链机会\n\n当全球AI算力需求以指数级增长，地面数据中心面临电力、土地和散热的三重约束时，一个反直觉的答案正在浮现：把计算送上天。\n\nMS近期发布的全球科技网络研讨会报告，系统性地提出了“轨道计算”（Orbital Compute）这一概念框架。这不是科幻，而是基于可复用火箭成本下降、星间激光通信技术成熟以及AI推理工作负载向边缘迁移三个现实趋势推演出的研究主题。报告的核心判断是：轨道计算将从“轨道边缘AI”起步，最终可能演变为天基AI基础设施，而欧洲半导体公司将成为这一链条上的关键赋能者。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 轨道计算的演进路径比大多数人想象得更务实\n\n报告将轨道计算划分为三个阶段，但最值得关注的是第一阶段：轨道边缘计算。这并非要在太空建设1GW的AI训练集群，而是在卫星上直接运行AI推理、图像处理和传感器数据分析，只将有用的输出传回地面。\n\n这个场景的落地逻辑非常清晰。地球观测、国防、海事监控和灾害监测等领域，每天产生海量数据，但卫星与地面之间的带宽有限。如果所有原始数据都要下传处理，延迟和成本都不可接受。将AI推理能力部署到卫星上，意味着只有“结论”需要传输，带宽需求可降低数个量级。\n\n> **KC评论：** 轨道边缘计算不是替代地面AI，而是填补一个空白——那些对实时性有要求、但无法依赖地面网络的场景。报告没有夸大到“算力上太空”，而是给出了一个可执行的起点。完整报告中的三阶段推演图值得细看，它回答了“为什么不是直接跳到天基数据中心”这个关键问题。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 成本曲线正在向有利于轨道计算的方向倾斜\n\n报告给出了一个关键数据点：轨道计算的每瓦特资本支出预计将从\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n太空计算，下一波AI基建观察\n\n🚀 太空计算新赛道\n\n某外资机构最新研报深度解析：轨道计算正在成为AI基础设施的新前沿。\n\n1/ 为什么是太空？\n- 太空有近乎连续的太阳能，不受地面电网限制\n- LEO轨道延迟低（10-30ms RTT）\n- 可重复使用火箭让部署成本持续下降\n\n2/ 三阶段演进路径\n📍 近期：轨道边缘计算\n卫星搭载AI芯片，在轨处理图像和传感器数据，只把有用结果传回地球。应用场景：地球观测、国防、海事监测、灾害预警。\n\n📍 中期：轨道云/分布式计算\n多颗计算卫星通过激光互联，形成太空分布式网络。难点在于低轨卫星移动快、资源有限、链路不断变化。\n\n📍 远期：太空AI数据中心\n卫星集群搭载AI加速器、存储、散热系统，通过高速光通信互联，形成虚拟太空数据中心。\n\n3/ 成本趋势如何？\n轨道计算每瓦成本预计从2030年的约60美元降至2040年的9美元。关键驱动：发射成本下降、卫星硬件优化。\n\n4/ 值得关注的欧洲半导体公司\n某欧洲半导体龙头被列为太空计算核心受益标的，LEO业务预计FY26-28年复合增长率48%。\n\n5/ 内存周期怎么看？\nDRAM和NAND报价仍在上涨，但增速见顶。EPS修正广\n\n[... middle omitted ...]\n\n \nResearch Associate  \nAmelia.Scicluna@morganstanley.com +44 20 7425-6694\n\n## TECHNOLOGY - EUROPEAN SEMICONDUCTORS\n\nEurope Industry View In-Line\n\n## Global Technology Webcast Space Technology,\n\n[... middle omitted ...]\n\nroup AG (VACN.S)</td><td>E (03/21/2025)</td><td>SFr 692.80</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R039",
    "title": "NOM：NOM拆解日元走势，NISA散户资金流是被低估的变量",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "NOM",
    "digest": "[wechat_article.md]\n# NOM：NOM拆解日元走势，NISA散户资金流是被低估的变量\n\n日元在6月加速走弱，市场习惯性地将目光投向美日利差、央行干预和财政相关讨论。但NOM最新发布的《JPY Monthly Flow Monitor》提供了一个容易被忽略的视角：日本国内散户通过新NISA（小额研究免税制度）渠道流出的资金，可能才是那个让日元空头更肆无忌惮的“隐形推手”。这份报告的价值不在于重复已知的宏观叙事，而在于用资金流数据拆解了谁在真正观点偏谨慎日元。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 银行连续六个月抛售外债，但交易量并不大\n\n银行类读者在6月净卖出2.0万亿日元的外国债券，这已是连续第六个月净卖出。NOM认为，核心驱动因素是美国国债通过资产互换（asset swap）的吸引力下降——6月下旬，即便美联储加息预期升温，美国互换利差却在持续收窄。这意味着通过借入日元、换成美元、再买入美债的套利空间被压缩，银行自然选择减仓。\n\n但一个值得注意的细节是：银行的粗交易量（gross trading volume）仍然偏低。换句话说，他们不是在恐慌性出逃，而是在低波动环境下主动调整了敞口。这与此前“银行因利率预期剧烈波动而被迫抛售”的叙事有微妙区别。\n\n> **KC评论：** 银行的抛售是“主动”而非“被动”，说明这不是流动性扰动驱动的信号，而是套利策略的正常调整。完整报告里对互换利差的图表拆解值得细看，它能帮你判断这个趋势还能持续多久。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 信托账户的“再平衡”并没有指向GPIF要大举买入日债\n\n信托账户在6月净观点偏积极1.5万亿日元外国债券，同时净观点偏谨慎1.3万亿日元外国公司。NOM判断这是典型的再平衡操作——全球市场上涨后，外国\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n日元资金流动观察：6月NISA相关资金变化\n\n📊 日元资金流动分析\n\n**6月日本跨境资金概况**\n日本市场参与者6月净卖出海外证券69亿日元，其中股票51亿、债券18亿。具体结构如下👇\n\n1️⃣ **银行：连续6个月减少海外债券持有**\n银行净卖出海外债券2万亿日元，主要因美债资产互换吸引力下降。整体交易量不高，波动率较低也影响了交易活跃度。\n\n2️⃣ **信托账户：股债配置调整**\n净卖出海外股票1.3万亿，同时净买入海外债券1.5万亿。逻辑清晰：股票前期上涨较多，权重超配，通过卖出股票、买入债券调整至25%基准线。目前未观察到GPIF明显增配国内债券的迹象。\n\n3️⃣ **寿险公司：态度谨慎但未大规模调整**\n净买入海外股票111亿，净卖出海外债券41亿。年度计划表态谨慎，但实际动作有限。若日元继续偏弱，可能更倾向于无对冲的外债。\n\n4️⃣ **投资信托：NISA相关资金流入明显**\n净买入海外股票767亿，NISA相关资金流入规模可观。6月正值夏季奖金发放，对日元有一定影响。7月后全球市场涨势放缓，流入速度可能下降。\n\n5️⃣ **外资：整体减少日本资产配置**\n净卖出日本证券5.5万亿，股票3万亿、\n\n[... middle omitted ...]\n\nng equity market gains. Our analysis does not suggest clear signs of a GPIF portfolio review aimed at materially raising domestic bond allocations at this stage.\n\n\\- Life insurers: Life insure\n\n[... middle omitted ...]\n\nation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved."
  },
  {
    "id": "R040",
    "title": "NOM：电商利润韧性超预期，NOM指阿里云正重塑公司利润结构",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "NOM",
    "digest": "[wechat_article.md]\n# NOM：电商利润韧性超预期，NOM指阿里云正重塑公司利润结构\n\n市场对阿里巴巴的讨论仍集中在电商份额与宏观消费的拉锯上。但NOM在2026年7月发布的最新季度预览报告中，给出了一个值得重新审视的判断：阿里云的盈利能力正在加速改善，其MaaS（模型即服务）业务的年化经常性收入已经超过百亿元人民币指引，达到120亿元。这个数字本身不算巨大，但结合该机构对云业务利润率持续扩张的预测，它指向了一个更结构性的变化——阿里巴巴的核心利润构成正在从“电商主导”向“电商+云双引擎”迁移，而云的边际贡献可能在未来2-3个季度内超出市场定价。\n\n以下是这份报告中最关键的三个层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 云业务的收入增速和利润率改善，都超出了市场共识\n\nNOM预计，阿里巴巴中国云业务在6月季度的收入同比增长45%，显著高于市场一致预期的37.5%。更值得注意的是利润率。报告指出，阿里云的EBITA利润率目前约为11-12%，但受年初提价以及高毛利MaaS业务收入占比提升的推动，这一数字有望持续上行。\n\n这里的关键变量不是收入规模，而是收入结构。MaaS业务的毛利率显著高于传统的IaaS和PaaS。当MaaS的ARR从100亿跳升至120亿，并且仍在加速，云的利润弹性就会被放大。NOM没有给出具体的利润率目标，但从其表述“should improve further”来看，这并非一次性修复，而是一个可持续的趋势。\n\n> **KC评论：** 市场习惯用电商的GMV和CMR来给阿里定价，但云的利润贡献正在快速接近甚至超过电商。这意味着，如果云的利润率每提升1个百分点，对整体利润的拉动可能比电商业务同等幅度的改善更显著。完整报告中对云业务各细分增速的拆解，值得仔细看。\n\n![研报原图 2](assets/sourc\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n阿里云表现突出，电商板块保持稳定\n\n云业务增长超预期，电商业务平稳可控\n\n近期有研究机构发布了阿里6月季报前瞻，核心观察较为清晰：电商广告收入可能有所调整，但云业务增长显著，整体盈利韧性比市场预期的更为稳健。\n\n1/ 电商CMR可能同比下降8%（可比口径微增1%），但云业务增速达45%，高于市场预期的37.5%。MaaS（模型即服务）年化收入已达120亿，超过此前指引的100亿。\n\n2/ 利润端表现较为稳定：中国电商EBITA仅下降3%（剔除即时零售），即时零售亏损从180亿收窄至103亿，好于市场预期的120-130亿。国际电商AIDC已实现盈利。\n\n3/ 云业务利润率仍有提升空间：当前为11-12%，随着今年提价及高毛利MaaS占比提升，后续几个季度有望持续改善。\n\n4/ 阿里云的核心竞争力在于全栈能力：从AI芯片（平头哥）到IT基础设施（最大公有云平台），再到百炼大模型平台和自研通义千问，覆盖AI价值链的关键环节。\n\n整体来看，虽然电商面临一定调整，但云业务增长与亏损收窄的组合，使得6月季报可能比市场预期的更为平稳。\n\n欢迎一起探讨云业务和电商的发展趋势～\n\n#学习笔记 #研究笔记 #学习研究 #研报解\n\n[... middle omitted ...]\n\nts MaaS (Model-as-a-Service) likely surpassed the guidance of CNY10bn, reaching CNY12bn as of the end of the June quarter. We believe BABA's cloud revenue will accelerate further over the next\n\n[... middle omitted ...]\n\n front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R041",
    "title": "NOM：4亿销售额背后，中国生物制药呼吸科新品能否兑现增长？",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "NOM",
    "digest": "[wechat_article.md]\n# NOM：4亿销售额背后，中国生物制药呼吸科新品能否兑现增长？\n\n中国生物制药与葛兰素史克的合作正在深化。7月8日午间，这家相关市场公司宣布，从GSK获得两款呼吸科药物在中国的商业权益。这并非一次孤立的交易。今年5月，双方刚就一款乙肝药物达成类似协议。两个月内两次出手，NOM分析师认为，这不仅是产品线的补充，更意味着中国生物制药正在用其被验证的商业化能力，换取跨国药企更深的信任和更多管线。\n\n呼吸科是中国生物制药的传统强项之一。此次获得的两款产品，分别是三联复方吸入粉雾剂“全再乐”和二联复方“欧乐欣”。前者是中国相对少见获批用于哮喘和慢阻肺维持治疗的单吸入器三联疗法，后者2018年已在中国获批用于慢阻肺。根据GSK披露的数据，这两款产品全球销售额合计超过35亿英镑。在中国样本医院渠道，全再乐2025年销售额约8.19亿元，同比增长34%；欧乐欣约1.18亿元，增长11%。增速可观，但相对规模仍有空间。\n\n> **KC评论：** 呼吸科吸入制剂的技术壁垒和渠道壁垒都很高。中国生物制药在这个领域有现成的销售队伍和医院覆盖，接手GSK的产品，比从头自研或代理一个全新品类，不确定性更低、兑现更快。完整报告里还拆了这两款产品与公司现有管线的协同效应，值得细看。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮合作真正考验的是，中国生物制药能否把规模转化为议价权\n\nNOM在报告中明确表示，对该合作持积极看法。核心逻辑不是产品本身有多惊艳，而是中国生物制药在中国的商业化能力，正在成为它与跨国药企谈判时的一张牌。过去几年，国内药企与MNC的合作模式，正在从单纯的代销、分成，走向更深度的捆绑。中国生物制药两个月内两次出手，说明GSK愿意把更多成熟产品交给它打理。这种信任一旦建立，后续的管线获取成本会下降，速度会加快。\n\n但这里\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n### 中国生物制药再添新品，呼吸产品线持续拓展\n\n**产品线进一步丰富**\n\n**引入GSK两款呼吸领域重点产品**\n\n研究资料显示，中国生物制药（1177 HK）与GSK的合作取得新进展。继5月获得乙肝药物商业化权益后，7月8日公司宣布取得两款呼吸领域药品在中国市场的相关权益。\n\n**本次引入的两款产品分别为：**\n\n1️⃣ **全再乐（Trelegy Ellipta）**：在中国市场，该产品是较早用于哮喘和COPD维持治疗的单吸入器三联疗法之一。2025年全球销售额为30亿英镑，同比增长11%；2026年第一季度为6.46亿英镑（同比-4%）。\n\n2️⃣ **欧乐欣（Anoro Ellipta）**：2018年在中国获批，用于COPD长期维持治疗。2025年全球销售额为5.42亿英镑（同比-5%）；2026年第一季度为1.28亿英镑（同比+1%）。\n\n**中国市场数据参考：** 根据Pharmcube数据，2025年全再乐与欧乐欣在样本医院的销售额分别为8.19亿元（+34%）和1.18亿元（+11%）；2026年第一季度分别为2.18亿元（+6%）和0.3亿元（-3%）。\n\n研究观点认为，此次合作有助\n\n[... middle omitted ...]\n\non powder (FF/UMEC/VI, 全再乐, Trelegy Ellipta) and umeclidinium and vilanterol inhalation powder (UMEC/VI, 欧乐欣, Anoro Ellipta) from GSK.\n\nTrelegy Ellipta is the first and only single-inhaler tri\n\n[... middle omitted ...]\n\n front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R042",
    "title": "NOM：AI不是威胁而是引擎，金蝶订阅业务规模效应显现",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "NOM",
    "digest": "[wechat_article.md]\n# NOM：AI不是威胁而是引擎，金蝶订阅业务规模效应显现\n\n当市场还在关注大语言模型公司是否会改变传统ERP厂商的格局时，金蝶用一份盈利预警给出了自己的回应。NOM在最新报告中判断，这家中国软件公司的基本面正在发生实质性变化——不是靠概念，而是订阅业务规模效应叠加AI驱动的效率提升，正在把利润从亏损拉回正值区间。\n\n金蝶7月7日收盘后发布2026年上半年业绩预告，收入36.08至36.39亿元，同比增长13%至14%。更值得关注的是净利润预期为4000万至6000万元，相比去年同期9800万元的亏损，这是一个明确的转折信号。经营现金流也由负转正，从净流出1800万元转为净流入1.3亿至1.5亿元。\n\n报告认为，市场对LLM影响的关注并非全无道理，但金蝶正在把自己变成一家“AI原生”公司。这不是一句口号——其AI原生产品的强劲增长是收入加速的直接驱动因素之一。换句话说，这轮业绩改善的核心不是压缩成本，而是业务结构本身在变。\n\n> **KC评论：** 金蝶这份盈利预警最值得看的不是利润相对值，而是“经营现金流同步转正”。这意味着利润改善不是靠纸面调整，而是真实的现金在回流。完整报告里对订阅业务规模效应的拆解值得仔细读，它解释了为什么这个拐点可能比市场预期的更可持续。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订阅业务的规模效应正在取代一次性收入成为利润引擎\n\n金蝶过去几年一直在推动从License向SaaS的转型，市场对此并不陌生。但真正的分歧在于：订阅收入的增长何时能覆盖转型成本，并开始释放利润。NOM的判断是，这个临界点已经出现。\n\n报告明确提到，利润改善“主要归因于订阅业务的规模宏观环境以及AI驱动的效率提升”。这背后的逻辑是：订阅模式前期投入高、后期边际成本低，一旦用户基数跨过某个门槛，收入增长带来的利\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n这家SaaS公司，利润实现转正\n\n利润转正，AI驱动加速\n\n某外资机构近期发布了关于金蝶（268.HK）1H26的业绩前瞻报告，核心观点是：订阅收入持续增长，AI原生产品放量，公司利润从亏损转为盈利。\n\n几个关键信息👇\n\n1️⃣ 收入加速增长\n1H26营收预计在36-36.4亿人民币区间，同比增幅约13-14%。从管理口径来看，订阅收入保持增长，AI原生产品增长势头良好——这是研报原文。\n\n2️⃣ 利润转正，经营现金流改善\n1H26净利润预计为4000-6000万，去年同期为亏损9800万。经营现金净流入预计1.3-1.5亿，去年同期为净流出1800万。规模效应与AI提效的逻辑较为清晰。\n\n3️⃣ LLM冲击？研报认为影响有限\n市场关注大模型公司可能对金蝶的ERP核心业务带来影响。但研报判断：金蝶的云ERP仍具韧性，AI解决方案反而可能加速收入增长与盈利改善。短期LLM扰动因素或仍存在，但公司正在向“AI原生”方向转型。\n\n4️⃣ 目标价18.49港元\n基于DCF估值，目标价对应FY26F P/S 8.7x。研报未给出具体时间表，此处为推测。\n\n风险提示：云收入增长不及预期、竞争加剧、下一代云平台竞争。\n\n欢\n\n[... middle omitted ...]\n\nrovements driven by AI. Net cash inflow from operating activities is expected to be CNY130-150mn vs net outflow of CNY18mn in 1H25, reflecting better operating efficiency and subscription busi\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R043",
    "title": "NOM：不是点位而是机制，NOM解读人民币中间价新信号",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "NOM",
    "digest": "[wechat_article.md]\n# NOM：不是点位而是机制，NOM解读人民币中间价新信号\n\n人民币对美元中间价近期持续调整，但真正值得关注的不是具体点位，而是定价机制内部的信号。NOM亚洲外汇策略团队在最新报告中更新了其人民币中间价预测模型，结果显示，在不含逆周期因子的情况下，模型预测值已较前一日官方收盘价低约90个基点。这个缺口暗示了什么？中间价管理可能正在从“稳定”向“有序弹性”过渡。\n\n报告的核心判断是：当前中间价定价已隐含更强的市场化信号，而非单纯的政策干预。NOM的模型显示，剔除逆周期因子后，预测中间价为6.7984，较前一日官方收盘价低93个基点。这一偏离幅度在近期属于相对明显水平，意味着决策层可能正在利用中间价机制，释放更灵活的管理信号，而非被动跟随市场波动。\n\n> **KC评论：** 这组数字的实质是，中间价不再是简单的“市场+过滤”公式，而是一个带有前瞻指引意味的政策工具。读者应关注模型误差的累积方向，而非单日变动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 逆周期因子的使用已趋于克制\n\n逆周期因子是中间价定价中用来缓冲市场波动的工具。NOM模型显示，当前含与不含逆周期因子的预测值仅相差0.3个基点，几乎可以忽略。这与2023年或2024年初期的情形形成对比——当时逆周期因子曾被频繁使用以对抗单边贬值预期。\n\n这种变化意味着什么？决策层可能认为当前市场环境已不需要强力干预，或者更愿意让价格发现机制发挥更大作用。对市场参与者而言，逆周期因子的淡出意味着中间价的波动性可能上升，单日调整幅度或更接近模型隐含的方向。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 报告尚未完全回答的关键问题：弹性管理的边界在哪里\n\nNOM的模型提供了清晰的“当前信号”，但并未明确回答：这种弹性管理的容\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n人民币中间价，外资行怎么看\n\n6.7984\n\n新模型预测比前次低93点\n\n---\n\n某外资行最新研报更新了USD/CNY中间价预测模型，核心数据如下👇\n\n**1️⃣ 模型预测值**\n- 新模型预测：6.7987\n- 前次预测：6.8077（低了90点）\n- 较前次官方收盘价：低了6点\n\n**2️⃣ 加入逆周期因子后**\n- 预测值为6.7984\n- 比前次官方中间价低93点\n- 说明模型认为短期仍有温和调整空间，但逆周期因子会平滑波动\n\n**3️⃣ 近期关键事件日历**\n- 7月下旬：政治局会议（经济工作）\n- 10月1-7日：国庆黄金周\n- 11月：APEC会议在深圳\n- 12月中旬：中央经济工作会议\n- 年底：相关访问安排（据媒体报道）\n\n**4️⃣ 研报团队**\n- 由亚洲外汇策略团队负责，包括Craig Chan等四位分析师\n- 基于多因子模型，结合隔夜市场贡献权重计算\n\n💡研报未给出具体操作建议，模型预测仅作研究参考。后续关注7月政治局会议定调，可能影响下半年汇率政策走向。\n\n欢迎一起讨论，你对下半年人民币走势怎么看？\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru\n\n[... middle omitted ...]\n\na5405afe647913c9a62e5b7fde44e4bfcd5eee96f6b46.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/0af5216eec5ba53ac2b9e627a90b05f1356984e8\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R044",
    "title": "UBS：常规CCL涨价超预期，UBS揭示AI产能挤占下的新周期",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "UBS",
    "digest": "[wechat_article.md]\n# UBS：常规CCL涨价超预期，UBS揭示AI产能挤占下的新周期\n\n市场对英伟达Kyber正交背板延迟的关注，可能被放大了。UBS最新报告给出一个与多数媒体报道不同的判断：这次延迟早在预期之内，对2026-2027年PCB公司影响有限，真正值得关注的不是时间表推迟，而是材料路线的重新洗牌。\n\n这份报告发布于7月6日，核心信号有三层：Kyber延迟已在5月上游CCL厂商调研中被预判，当前对行业更关键的是常规CCL涨价周期正在加速，以及mSAP产能扩张正在为1.6T/3.2T光模块需求做准备。三个信号指向同一个结论——PCB行业正处于一个结构性分化阶段，不同环节的受益逻辑完全不同。\n\n![研报原图1](assets/source_image_01.jpg)\n\n## 1. Kyber延迟的实质是材料方案尚未收敛，而非项目取消\n\nUBS分析师明确指出，英伟达Kyber正交背板延迟到2028年，与他们在5月从上游CCL供应商处调研得到的预期一致。这并非突发变化，而是技术路线选择过程中的正常波折。\n\n报告拆解了三个核心难点：M9+Q-glass方案加工难度高、供应不足且成本高于其他方案；PTFE作为替代方案性能优异但供应链尚未就绪；100+层PCB对Q-glass和PTFE材料的制造良率要求极高。\n\n> **KC评论：** 读者容易把“延迟”等同于“取消”，但UBS的调研显示，多个材料方案仍在并行推进，PTFE-M9混合方案正成为主要选项。真正需要跟踪的变量不是时间点，而是哪个材料方案最终胜出——这决定了相关PCB供应商的制造壁垒和利润空间。\n\n![研报原图2](assets/source_image_02.jpg)\n\n## 2. 常规CCL涨价周期正在加速，且可持续性超出预期\n\n报告中最具即时冲击力的信息来自常规CCL市场。KBL在6月两轮涨价（15%和10%）之后\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# NVIDIA Kyber 延迟，PCB 行业观察\n\n## 📌 Kyber 延期，有迹可循\n\n近期有消息显示，NVIDIA 的 Kyber 机架架构因 PCB 背板供应链环节的调整，可能将时间表调整至 2028 年。这一时间节点，早在今年 5 月，已有外部研究机构通过上游 CCL 厂商调研时有所提及。当时提到正交背板方案可能调整至 Feynman 平台（2028 年），目前来看，这一判断得到了印证。\n\n### 1️⃣ 延迟背后的三大技术因素\n- **M9+Q-glass 组合**：加工难度较高、供应量有限、成本偏高，虽然经过多轮尝试，但 Kyber 背板方案目前处于暂缓状态。\n- **PTFE 材料成为有力替代**：性能表现良好，良率在逐步提升，但供应链仍需时间进行更充分的验证。\n- **PCB 制造端良率面临挑战**：Q-glass 和 PTFE 均对制造能力提出更高要求，尤其是 100 层以上的多层板。\n\n### 2️⃣ 对 PCB 公司业绩影响有限\n研究认为，Kyber 原计划在 2027 年底随 Rubin Ultra 推出，初期规模不大。虽然时间表有所调整，但项目并未取消。因此，对 2026/27\n\n[... middle omitted ...]\n\n+ material/vendor combinations being considered including different layer count designs. We see potential challenges are: 1) M9+Q-glass' processing difficulties, inadequate supply and higher c\n\n[... middle omitted ...]\n\nng number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R045",
    "title": "UBS：黑石KKR利润率近70%，另类资管如何系统蚕食市场",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "UBS",
    "digest": "[wechat_article.md]\n# UBS：黑石KKR利润率近70%，另类资管如何系统蚕食市场\n\n美国资产管理行业正在发生一场并不张扬的洗牌。UBS一份覆盖美国机构与资管机构的研报，用一组对比鲜明的估值和财务数据揭示了一个判断：另类资产管理公司正在系统性蚕食传统资管公司的市场份额与利润池，而市场对这一结构性变化的定价远未完成。\n\n这份报告覆盖了三大类公司——另类资管（黑石、KKR、阿波罗等）、传统资管（贝莱德、富兰克林资源等）以及财富经纪商（嘉信资金规划、LPL等）。数据跨度从2026年预测到2027年预期，呈现的不是短期波动，而是商业模式的分化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 另类资管的估值溢价并非情绪驱动，而是盈利结构决定的\n\n报告显示，另类资管公司2026年预期市盈率中位数约为15.9倍，传统资管为13.0倍。表面看差距不大，但深入看盈利质量，差异就清晰了。\n\n另类资管的费用相关收益（FRE）利润率普遍在50%以上，KKR甚至接近70%。相比之下，传统资管的运营利润率多在35-45%区间。更关键的是，另类资管的收益更少依赖市场涨跌——它们从管理费、业绩报酬和自有研究中获取收入，而传统资管高度依赖管理资产规模（AUM）随市场波动的被动增长。\n\n> **KC评论：** 估值差异的核心不在增速，而在收益的“可预测性”。另类资管的FRE相当于订阅收入，传统资管的费用收入更像过路费。市场愿意为前者付更高倍数，逻辑上成立。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 传统资管面临的真正挑战不是规模，是议价权流失\n\n报告表格中，传统资管公司的预期收入增速并不低，但利润率改善空间有限。贝莱德2026年预期运营利润率46.3%，已属行业领先；但多数传统资管公司仍在35-40%区间。\n\n问题出在\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n美国资产管理行业最新观察  \n哪些公司可能被市场低估？  \n某外资机构近期研究观点整理  \n\n最近看到某外资机构7月发布的美国资产管理及券商行业研究，数据量较大，逻辑清晰。我将其梳理为三个板块，供参考👇  \n\n**1/ 另类资产管理：增长较快但估值分化明显**  \n- 该板块平均目标价上涨空间约28%，但个股差异较大。  \n- 例如Apollo、Carlyle、KKR、StepStone获得积极评价，目标价涨幅在33%-60%之间。  \n- 而Blackstone、Ares、Blue Owl则偏中性，涨幅在1%-12%之间。  \n- 关键观察指标包括费用收入（FRE）和利润率：KKR的FRE利润率约70%，在板块中表现突出；Carlyle虽然较低（47%），但估值相对便宜。  \n\n**2/ 传统资产管理：规模大但增速相对平缓**  \n- 传统资管整体估值约13倍，低于另类资管的16倍。  \n- BlackRock是少数获得积极评价的公司，目标价涨幅约28%，管理资产规模接近14万亿美元。  \n- 其他如Franklin、Invesco、T.Rowe Price则未给出明确评级，显示不确定性较高。  \n- 传统\n\n[... middle omitted ...]\n\n<table><tr><td rowspan=\"2\">Alternative Asset Managers</td><td rowspan=\"2\">Ticker</td><td rowspan=\"2\">Rating</td><td rowspan=\"2\">Market Cap ($B)</td><td rowspan=\"2\">Price</td><td rowspan=\"2\">P\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/bd200f17468374ae57a47247b0a1763b17e7b8167febb1aa2b6e30245e79eaf5.jpg)"
  },
  {
    "id": "R046",
    "title": "UBS：消费趋势变化下的免税龙头观察，中国中免收入变化需关注政策方向",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "UBS",
    "digest": "[wechat_article.md]\n# UBS：消费趋势变化下的免税龙头观察，中国中免收入变化需关注政策方向\n\n当一家公司收入可能下滑，利润却可能增长超过两位数，市场通常不会太兴奋。原因很简单——这种利润改善往往被解读为“省出来的”，而不是“赚回来的”。UBS最新一份与中国中免管理层的交流纪要和业绩预览，恰恰揭示了这个微妙局面。\n\n这份报告的核心判断是：中免正处在一个“收入承压、利润修复”的过渡期。2025年第二季度，公司收入可能同比下滑超过10%，但净利润有望实现双位数增长，甚至可能超过20%。问题在于，市场对利润增长的可持续性存疑，而收入端的真正变化节点，可能取决于海南当地补贴的力度和持续性。\n\n> **KC评论：** 利润改善主要来自折扣减少和销售结构优化，而非需求回暖。这意味着，如果只看利润数字做判断，可能会高估公司内生增长的强度。完整报告里对海南4-5月增速节奏变化的渠道数据，值得细看。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度收入下滑已成定局，海南和机场业务各有观察点\n\nUBS预计中免二季度收入同比下滑超过10%，明显弱于一季度。拆开看，三个核心板块都不轻松。\n\n海南业务占公司总收入超过70%，二季度估计仅增长约10%，远低于一季度的28%。这个节奏变化速度值得注意——4月和5月海南离岛免税销售增速较一季度明显回落，说明消费趋势的不确定性仍在，政策托底的效果也在边际递减。\n\n机场业务同样承压。虽然上海浦东机场T2和S2的销售额实现双位数同比增长，但公司失去了上海机场T1和S1的经营权，整体机场免税收入仍在同比下滑。线上业务方面，CTG Sunrise的销售继续同比下降，且UBS预计2026年内都难以企稳。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 利润修复的“两条腿”：折扣减\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n免税龙头，收入表现如何？\n\n近期行业观察中的一些数据点\n\n最近翻阅了某外资机构关于中国中免的最新研究，几个值得留意的信息👇\n\n**1️⃣ 二季度收入可能同比有所变化**\n预计Q2收入同比下降超10%，主要受海南销售额增速变化影响。海南占中免收入70%+，但Q2增速从Q1的28%降至约10%。\n\n**2️⃣ 利润却在增长？**\n毛利率和净利率预计同比改善，Q2净利润可能实现双位数增长，甚至有机会超20%。利润增长主要靠折扣减少和产品结构优化，并非由收入拉动。\n\n**3️⃣ 市场关注什么？**\n- 消费环境持续调整，海南免税增长高度依赖政策支持\n- 2026-2027年市场一致预期有调整可能\n- 利润靠利润率修复，持续性有待观察\n\n**4️⃣ 机场业务分化**\n上海浦东T2+S2销售额同比两位数增长，但T1+S1经营权丢失，整体机场免税仍有所变化。\n\n**5️⃣ 下半年怎么看？**\n7月海南加大政策支持，包括补贴航空公司增加航班量，预计7-8月海南免税增速能回到双位数。但要回到Q1的20%+增长，难度不小。\n\n研究未给出具体补贴规模，这里是推测：补贴力度是下半年增速的关键变量。\n\n**6️⃣ 海外扩张方向**\n公\n\n[... middle omitted ...]\n\ncerns remain: 1) ongoing consumer downtrading could continue to weigh on CTG's revenue. The sharp slowdown in Hainan duty-free sales growth in April-May versus 1Q suggests the continued relian\n\n[... middle omitted ...]\n\nng number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved."
  },
  {
    "id": "R047",
    "title": "BofA：市场误判Soitec光子学增速？BofA指移动端影响盈利拐点",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "BofA",
    "digest": "[wechat_article.md]\n# BofA：市场误判Soitec光子学增速？BofA指移动端影响盈利拐点\n\n这份来自BofA的报告，核心判断并非关于Soitec在光子学领域的潜力——实际上，市场对此已经充分预期。真正的不确定性在于其基本盘：移动通信业务，幅度接近30%，背后是对智能手机市场变化和客户库存消化的审慎评估。\n\nBofA认为，Soitec从FY26的盈利低谷中复苏是确定的，但节奏和幅度远不如市场想象的那么乐观。当市场聚焦于光子学带来的AI增量时，移动端这个占比过半的板块，正在影响整体盈利修复的斜率。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对光子学的增长假设，可能过于激进\n\n报告最值得关注的洞察在于，市场共识（consensus）对Soitec光子学业务的增长预期，已经隐含了远超行业基本面的乐观情绪。BofA测算，市场预计FY27-29年光子学-SOI收入分别增长28%、34%和43%，这一增速显著高于BofA基于总晶圆面积（die area）CAGR预测的50%复合增长率。\n\n关键问题在于，光子学-SOI的增长并非线性。它依赖于多个尚未明确的变量：NPO/CPO（近封装/共封装光学）的爬坡时间表、光引擎对PIC（光子集成电路）尺寸的要求变化、以及不同收发器速率下的良率表现。这些变量既有上行也有节奏变化，但市场似乎已经将最乐观的NPO/CPO渗透率增长“定价”了进去。\n\n> **KC评论：** 当一家公司的报价已经反映了最乐观的技术路线图时，任何技术落地节奏的延迟，都可能成为报价的谨慎催化剂。完整报告中关于不同技术路径假设的敏感性分析，值得细读。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 移动端才是决定短期业绩走向的关键变量\n\nSoitec的移动通信业务在FY26贡献了超过\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# Soitec 光通信前景已反映在市场定价中\n\n📉 预期已充分体现\n\n某外资研究机构最新报告指出，Soitec 的Photonic-SOI（光子学绝缘体上硅）业务增长预期已经较高，但实际落地仍有不确定性。\n\n**1️⃣ 光子学业务：增长预期较高**\n- 市场共识预计FY27/28/29年Edge和Cloud AI业务增长28%/34%/43%\n- 但报告认为这意味着Photonics-SOI增速远超行业50%的复合增长率水平\n- 关键变量较多：良率、收发器速度、光学引擎要求、NPO/CPO量产时间线均存在不确定性\n\n**2️⃣ 移动业务：复苏节奏温和**\n- 手机价格调整背景下，移动业务FY27年预计下降6%（报告模型更保守，预测下降11%）\n- RF-SOI库存消化缓慢，客户库存仍约200万片晶圆\n- 预计FY28/29年移动业务恢复增长19%/27%\n\n**3️⃣ 整体财务展望**\n- FY26年收入下降34%至5.92亿欧元，每股收益为-6.17欧元\n- 预计FY27年收入持平，FY28/29年恢复增长23%/29%\n- 目标报价从193欧元调整至138欧元\n\n**关键观察点**：GlobalWafe\n\n[... middle omitted ...]\n\n €193) on updated SOTP valuation.\n\n## Street is projecting Photonics-SOI growing above industry\n\nWe view Soitec's Photonics-related upside as priced in, with Edge and Cloud AI (of which Photon\n\n[... middle omitted ...]\n\n BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies."
  },
  {
    "id": "R048",
    "title": "BofA：中国医药行业交易活跃度正在驱动新一轮市场定价",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "BofA",
    "digest": "[wechat_article.md]\n# BofA：中国医药行业交易活跃度正在驱动新一轮市场定价\n\n中国医药行业正在经历一个关键转折：交易活跃度与研发进展的共振，开始推动市场重新审视。BofA在最新一期行业报告中指出，这轮变化并非单纯的政策回暖，而是由具体公司的战略动作和临床数据共同支撑的结构性修复。报告覆盖的四家公司——石药集团、固生堂、信达生物和恒瑞医药——各自展示了不同的增长路径，但背后指向同一个判断：行业已经从“集采冲击”过渡到“创新兑现”阶段。\n\n> **KC评论：** BofA的“重估”判断值得注意。它不是简单地说“行业变好了”，而是强调催化剂密度——合作、并购、临床数据——正在累积到足以改变市场对个别公司未来现金流的预期。这种“微观驱动宏观”的修复，比政策口号更扎实。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 大型药企的“合作换空间”策略正在被市场验证\n\n石药集团与阿斯利康的 siRNA 平台合作，是这份报告中最具信号意义的交易。石药获得 3000 万美元首付款，并有资格获得最高 12 亿美元的里程碑付款。BofA将石药的报价上调至 7.6 港元，但维持“弱于大盘”评级。这个看似矛盾的判断背后，是报告的核心洞察：石药现有主力产品的销售不确定性，仍然大于新合作带来的增量。合作的价值在于打开了长期技术平台变现的想象空间，而非短期内扭转基本面。\n\n信达生物则走了另一条路——通过承接礼来的 CDK4/6 抑制剂 Verzenios 在中国大陆的商业化，直接补充收入。BofA因此将信达 2026-2028 年收入预期上调 3.3%-5.3%。信达的案例说明，当一家公司拥有成熟的商业化网络时，它可以从跨国药企的“中国授权退出”中获益。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 恒瑞的研发管线密度\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n7月研报速读：4家药企关键动作\n\n**中国医药行业正在重估**\n\n某外资机构最新研究，覆盖了4家药企的最新动态，核心逻辑是：研发推进+交易活跃，正在驱动行业重新定价。\n\n1️⃣ **石药集团与阿斯利康合作**\n- 双方合作开发siRNA药物，针对两个肾病靶点\n- 石药收到3000万美元首付款，未来还有高达5.4亿/12亿美元的里程碑付款\n- 目标价从6.8上调至7.6港元，但维持“跑输大市”评级\n- 原因：核心品种持续面临销售压力\n\n2️⃣ **固生堂收购扩张**\n- 收购沙河医院和北京红阳医院，扩大北京布局\n- 管理层预计能与现有线上线下体系产生协同\n- 维持“买入”评级，目标价32.6港元\n\n3️⃣ **信达生物与礼来商业化合作**\n- 负责礼来CDK4/6抑制剂Verzenios（阿贝西利）在中国大陆的进口、营销和推广\n- 该药2021年已进医保，覆盖乳腺癌早晚期适应症\n- 上调2026-2028年收入预估3-5%，目标价上调至119.2港元\n\n4️⃣ **恒瑞医药多款新药进展**\n- SHR-A1811第三个适应症（HER2低表达乳腺癌）申请获受理并获优先审评\n- 多款新药获临床试验批准\n- 研报预计\n\n[... middle omitted ...]\n\nof US\\$30mn and is eligible for up to US\\$540mn/US\\$1.2bn in development/sales milestone payments plus potential single-digit royalties. We add the US\\$30mn upfront payment to our estimates an\n\n[... middle omitted ...]\n\n BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies."
  },
  {
    "id": "R049",
    "title": "Citi：面板供需平衡临界点2027年到来，公司定价权改善但新业务待验证",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：面板供需平衡临界点2027年到来，公司定价权改善但新业务待验证\n\n公司在读者日上勾勒了一个宏大叙事：从显示面板全球第一，延伸至玻璃基先进封装、光互连、钙钛矿光伏、可折叠玻璃等新赛道。Citi最新研报选择在这个时点将评级从观点偏积极下调至中性。核心逻辑并非看空，而是认为当前估值已部分反映了LCD业务改善和玻璃基板的潜在贡献——预期的空间正在被定价，真正的考验从“能不能做”转向“什么时候能做成规模”。\n\n这份报告最值得关注的判断，不是公司能否守住面板龙头地位，而是其第二、第三增长曲线是否具备从实验室走向大规模量产的确定性。Citi的判断是：市场对玻璃基板的期待已经走在技术落地之前。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 面板主业正在接近供需平衡的关键临界点\n\n公司管理层在读者日上释放了一个重要信号：当全球电视面板平均出货尺寸达到55英寸时，电视面板行业将进入供需平衡状态。公司预计这一临界点将在2027年到来。70-75英寸电视的出货份额已从2025年的8%跃升至2026年的22%，80英寸以上电视出货量预计同比增长超过20%。\n\n这对公司意味着什么？作为大尺寸面板的领先者，行业供需平衡将直接改善其定价权和盈利稳定性。但Citi也指出，OLED业务在未来两年仍将面临竞争不确定性，全球OLED智能手机需求预计同比下降10-17%，主要受内存价格上涨推高终端价格的影响。公司的OLED业务虽在1H26保持增长，但运营层面仍在亏损。\n\n> **KC评论：** 面板行业的逻辑正在从“产能竞赛”转向“尺寸升级驱动的供需再平衡”。55英寸这个阈值值得持续跟踪——如果2027年确实实现，面板龙头的估值框架将从周期股转向稳定现金流资产。完整报告中对LCD行业集中度、折旧趋势和资本开支的详细拆解，是理解这一转变的关键\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n京东方下一个增长点在哪？\n\n**研究笔记梳理**\n\n近期有机构更新了关于京东方的研究观点，核心思路较为清晰：面板主业已得到较多关注，真正值得观察的是玻璃基板等新业务的落地节奏。\n\n1/ **面板主业：利润结构在变化**\n- 重庆/福建两条8.5代线净利率超20%，10.5代线靠效率提升出货\n- 折旧高峰已过，OLED 8.6代线投产后资本开支趋势向下\n- 大尺寸化明显：70-75寸出货占比从8%→22%，80寸以上今年预计增超20%\n\n2/ **第二增长曲线：创新业务**\n- 目标2026年收入600亿，占总营收约30%\n- 已在车载、商显、医疗等20+细分领域做到全球领先\n\n3/ **第三曲线：玻璃基板是重点**\n- 和康宁合作四大方向：玻璃基封装、光互连、折叠玻璃、钙钛矿光伏\n- 玻璃基板已突破20:1深宽比TGV钻孔、无空洞填孔、sub-2μm线宽\n- 单层基板通过1000次温循、HAST等可靠性测试，75mm样片室温翘曲仅40μm\n- 目标：2027年中前决定是否量产\n\n4/ **光互连：配合AI算力需求**\n- 自研micro-LED光源达1.8GHz响应、3Gbps传输\n- 路线图：2027年二维\n\n[... middle omitted ...]\n\nproduction, but BOE targets to launch mature multi-channel product demos aligned with 1.6T, 3.2T and 6.4T industry requirements in 2028. We downgrade BOE from Buy to Neutral with a new TP of R\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R050",
    "title": "Citi：不是行业回暖，而是份额重组，Citi看比亚迪如何抢回市场",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：不是行业回暖，而是份额重组，Citi看比亚迪如何抢回市场\n\n7月第一周的中国新能源车市订单数据，传递了一个清晰的信号：行业总量在季节性走弱，但头部玩家的份额格局正在剧烈重组。Citi最新周度订单跟踪显示，7月首周（6月29日至7月5日）主要品牌总订单环比下降4%，同比基本持平，符合季节性规律。但真正的看点在于结构——比亚迪的订单份额从6月第一周的27%迅速攀升至7月首周的51%，仅四周时间几乎弹性较高。\n\n> **KC评论：** 份额从27%到51%不是微调，是市场力量的一次集中释放。Citi的经销商调研捕捉到了这一拐点，但完整报告里关于“Great Tang”车型的讨论和订单数据图表，才是理解这一变化驱动力的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪的反弹并非行业共性，大部分品牌在失速\n\nCiti数据清晰呈现了分化格局。7月首周，比亚迪订单环比增长81%，吉利银河仅下滑1%，表现优于行业均值。但其他品牌普遍承压：理想汽车环比下降14%，特斯拉下降23%，小米下降27%，小鹏下降29%，零跑下降5%。蔚来和华为鸿蒙的环比降幅分别达到61%和66%，主要原因是6月初新款M9和ES9上市带来的订单高峰已过。\n\n这意味着，比亚迪的份额扩张并非行业景气度回升的结果，而是在总量持平的背景下，从其他品牌手中直接争取了用户。对于读者而言，真正需要关注的问题是：这种份额转移是可持续的结构性变化，还是短期促销或新车型脉冲带来的阶段性现象？\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 订单数据暴露了大多数新势力的增长瓶颈\n\nCiti报告中一个容易被忽略的信号是：理想、小鹏、小米、特斯拉的订单环比降幅均在两位数以上，且均跑输行业均值。这些品牌并非缺乏产品力\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n比亚迪市场表现观察，7月首周订单超8.6万\n\n**比亚迪近期动态**\n\n7月第一周，新能源车市场订单环比下滑4%，但比亚迪订单增长81%，市占率从6月初的27%升至51%。\n\n**1. 比亚迪为何增长？**\n6月底“大唐朝”上市后，订单明显提升。7月首周8.65万单，环比+81%，是10家主流品牌中相对少见的正增长案例。\n\n**2. 哪些品牌在调整？**\n- 理想、小鹏、小米、特斯拉环比降14%-29%\n- 蔚来、华为鸿蒙降幅超60%——因6月初新车（M9/ES9）冲高后自然回落\n- 零跑、吉利银河相对稳定，环比-5%和-1%\n\n**3. 行业观察**\n7月整体订单持平，符合季节性规律。但比亚迪一家占据行业过半份额，说明“价格策略+新车周期”的组合仍有效。\n\n**4. 值得关注**\n研究机构提到，L2级政策落地可能对地平线（市值90亿美元）和小鹏产生外溢效应。后续可以观察智驾产业链的联动。\n\n大家觉得比亚迪这轮表现如何？欢迎一起交流。\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.md]\n# China Auto Manufacturers\n\n## Weekly Order\n\n[... middle omitted ...]\n\ndecline of Huawei Harmony and Nio was due to early-June order peak post new models launch (all-new M9 and ES9). Further readings: (1) China Auto Manufacturers – Growth Divergences into 3Q26; 4\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R051",
    "title": "BofA：SpaceX垂直整合闭环，发射、应用、现金流的飞轮",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "BofA",
    "digest": "[wechat_article.md]\n# BofA：SpaceX垂直整合闭环，发射、应用、现金流的飞轮\n\n这家公司已经证明自己能把火箭发射变成一门高利润的应用生意。Starlink就是最好的证据。但BofA在7月发布的这份覆盖报告中，把核心判断放在了更远处：SpaceX的长期价值，几乎全部押注在Starship能否真正实现完全可重复使用。\n\n但更值得关注的是其背后的逻辑链条——SpaceX已经从一个发射服务商，演变为太空宏观环境的基础设施搭建者。而Starship就是这条高速公路的最后一个关键节点。\n\n读者可以重点看报告中的三情景DCF模型，理解BofA如何为这种高度不确定性定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 发射优势是起点，但真正创造价值的是应用层\n\nSpaceX的Falcon系列火箭已经执行了超过650次发射，成功率超过99%。过去几年，这家公司承担了全球80%以上的入轨质量。但BofA指出，发射业务本身在财务上需要继续观察——成本核算方式让这个板块的利润表显得相当单薄。\n\n真正的价值在于，发射能力被转化成了高利润、经常性的应用收入。Starlink就是最典型的例子。SpaceX自己设计卫星、自己发射、自己运营网络、直接服务终端用户。这种端到端的垂直整合，让它在不到十年内建成了约一万颗卫星的星座，拥有了超过一千万用户。\n\n发射与应用之间形成了一个正循环：发射能力支撑应用部署，应用产生现金流，现金流再反哺下一代发射系统。这个飞轮能否继续转动，取决于下一个变量。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. Starship是估值逻辑的“全有或全无”节点\n\nBofA将Starship称为“宇宙之王”。这不是修辞，而是估值模型中最大的单一变量。\n\n如果Starship成功实现完全可重复使用\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# SpaceX的飞轮，已经转到AI了\n\n🚀 太空超级高速公路\n\n某外资研究机构首次覆盖SpaceX，给出报告评级和235美元目标价。核心逻辑：SpaceX已经从一家火箭发射公司，进化成太空经济的基础设施提供者。\n\n1/ 发射能力是根基\nFalcon火箭已执行超650次发射，成功率99%+，承担全球80%+的入轨质量。可复用技术让单次发射成本大幅下降，最牛的助推器已经复用35次。这个护城河，竞争对手短期内追不上。\n\n2/ 星链是现金牛\nSpaceX把发射能力转化成高利润的订阅业务——星链。现在服务超160个国家，覆盖消费、企业、航空、海事、政府等多个场景。发射→应用→现金流→再投资基础设施，这个飞轮已经转起来了。\n\n3/ 星舰是关键变量\n研报认为，星舰能否实现完全可复用，是决定SpaceX下一阶段增长的核心。如果成功，发射成本可能再降一个数量级。如果推迟，很多增长点的兑现时间都会后移。\n\n4/ 太空计算是新故事\nSpaceX正把目光投向AI基础设施和太空计算。依托发射能力和垂直整合，这个方向有很高的期权价值。当然，前提还是星舰的成功。\n\n📊 财务数据速览\n- 2026年预计营收407.7亿美元，2028年飙到\n\n[... middle omitted ...]\n\nations are in our view laying the foundation for Starship and future applications to drive another paradigm shift in capabilities.\n\n## Monetizing the mass to orbit moat\n\nSpaceX has demonstrate\n\n[... middle omitted ...]\n\new in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R052",
    "title": "Citi：CICCH股盈利加速可见性高，Citi关注机构板块估值修复",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：CICCH股盈利加速可见性高，Citi关注机构板块估值修复\n\n一份来自Citi的研报，在CICC（3908.HK）即将发布半年报前，给出了一个明确的判断：二季度盈利增速有望从一季度的75%进一步加速至超过80%。这个数字本身不算意外，真正值得行业观察者留意的，是支撑这一加速的三条收入线——自营、国际机构、经纪——各自背后都站着同一个变量：相关市场活跃度的持续提升。\n\nCiti在这份报告中同时启动了对CICCH股的30日催化剂观察，方向为上行，触发事件为8月31日的中期业绩发布。这不是一个宽泛的行业提到，而是针对具体时间窗口的集中判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三条收入线同步发力，盈利加速有迹可循\n\n自营业务是二季度最直接的增量来源。沪深300指数在二季度环比上涨约12%，而去年同期仅环比上涨1.3%。CICC作为自营敞口较大的头部机构，受益于这一市场环境变化是清晰的逻辑。国际机构业务方面，CICC在二季度的相关市场IPO承销金额达到约27亿元人民币，而去年同期仅为不到5亿元，基数效应显著。经纪业务同样受益于相关市场日均成交额在二季度达到约2.9万亿元，环比增长12%，同比增长超过130%。\n\n这三条线不是孤立的利好，而是同一个市场环境下的协同输出。Citi的判断之所以值得关注，不在于它预测了盈利增速，而在于它把盈利加速的“可见性”建立在了已发生的市场数据之上，而非对未来的假设。\n\n> **KC评论：** 这份报告的核心价值不是预测数字本身，而是提供了一个观察框架：当市场活跃度持续时，哪些机构的收入结构最敏感、最直接。CICCH股在自营和国际机构上的敞口，使其成为这一逻辑下的典型标的。完整报告中的EPS预测路径和分部收入拆解，值得细看。\n\n![研报原图 2](assets/sou\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# CICCH股：30天业绩观察窗口\n\n📊 业绩观察窗口\n\n研究机构指出，CICC（3908.HK）将在8月31日发布二季报，预计净利润增速将超过80%（一季度为75%）。背后有三个支撑：\n\n1️⃣ 自营交易：沪深300二季度环比涨12%，去年同期为+1.3%\n2️⃣ 投行业务：二季度A股IPO承销额达270亿元，去年同期为4.44亿\n3️⃣ 经纪佣金：二季度A股日均成交额2.9万亿，同比增加132%\n\n📈 市场板块还有两个观察点\n\n研究认为，市场板块估值有望继续提升：\n- 资本流动相关监管收紧，可能影响居民资产配置方向，对市场相关公司有利\n- 相关持仓调整压力基本释放（90%持仓已调整）\n\nCICCH股ROE预计回升至10%左右，当前0.7倍PB估值处于一定区间。\n\n💡 长期观察\n\nCICC在投行、机构客户、研究能力上有品牌优势，还能受益于中概股回归、注册制改革、居民资产入市等趋势。\n\n欢迎一起讨论市场板块的逻辑变化～\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.md]\n07 Jul 2026 05:06:44 ET | 11 pages\n\n# China Intern\n\n[... middle omitted ...]\n\nin 2Q26 (+12% q-q/+132% y-y). Together with strong 2Q result, we think China brokers will further re-rate on a) tightened regulatory scrutiny on China's capital outflow, which will accelerate \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R053",
    "title": "Citi：存储涨价重塑季度轮廓，AI服务器公司超预期靠的不是需求",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：存储涨价重塑季度轮廓，AI服务器公司超预期靠的不是需求\n\n一份来自Citi的研究报告，用一组数字吸引了市场注意：一家中国AI服务器公司第二季度净利润指引达到20至25亿元人民币，环比增长229%至312%，大幅超出Citi自身预期的13亿元，也明显高于市场此前10亿元左右的普遍期待。\n\n这个超预期的原因，Citi给出了一个关键变量——存储涨价。该公司截至第一季度末拥有约440亿元的存货，而同期营业成本为330亿元。在第二季度存储价格上涨的环境下，这些存货可能带来了可观的收益。这不是AI服务器出货量的爆发，而是一次库存价值的重新定价。\n\n报告同时提及，第二季度可能存在部分超级节点（Superpod）的出货，但贡献预计有限。这意味着，市场如果简单将这份业绩超预期解读为AI硬件需求的全面加速，可能需要再审视。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存货规模才是这轮超预期的真正支撑\n\n440亿元存货，对应330亿元季度成本，这个比例在硬件公司中不算常见。Citi的逻辑很直接：当存储芯片进入涨价周期，持有大量库存的公司会自然受益于成本端的时间差——低价购入的存储芯片在服务器成品中实现了更高的售价。\n\n这一点对理解该公司的短期盈利弹性至关重要。它不是靠市场份额提升或产品溢价，而是靠供应链管理能力在周期波动中获利。对于关注中国AI硬件产业链的读者，这份报告提供了一个观察窗口：存货规模和质量，正在成为衡量服务器公司抗周期能力的新指标。\n\n> **KC评论：** Citi的这个判断，本质上是在说“库存就是利润”。完整报告里还有关于存货周转和成本结构的细节值得继续看，尤其是440亿存货中有多少是存储芯片、多少是其他组件，这决定了后续季度能否复制类似弹性。\n\n## 2. AI硬件预算的分配格局仍未完全清晰\n\nCi\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n服务器存储龙头，Q2利润表现超预期\n\n存储涨价带来的影响\n\n某外资机构解读Q2业绩预告\n\n近期服务器存储龙头公布了Q2业绩预告，净利润20-25亿，环比增长229%-312%，表现超出市场预期。某外资机构第一时间发布了分析，逻辑清晰，整理出来供大家参考。\n\n1️⃣ 存储涨价是主要驱动因素\n公司截至Q1末存货约440亿，而Q1的营业成本为330亿。在存储芯片价格上升周期中，这样的库存规模会放大利润弹性。Q2存储价格明显上涨，公司前期积累的低价库存逐步释放，对利润率产生了积极影响。\n\n2️⃣ AI服务器出货也有一定贡献\n研报提到Q2可能有部分超大规模集群出货，但认为贡献相对有限。目前主要的利润增量仍来自存储涨价，AI服务器属于额外助力。\n\n3️⃣ 估值角度观察\n目标价75元，基于2027年25倍PE，参考过去3年均值。当前报价71元，预期总回报约5.8%。评级中性，认为市场已较为充分地反映了国内AI服务器的贡献。\n\n核心逻辑是：在存储涨价周期中，高库存的服务器厂商会经历一段利润释放期。但AI服务器领域的竞争格局和利润率仍需持续关注。\n\n大家觉得存储涨价趋势会持续多久？欢迎一起交流。\n\n#学习笔记 #研究笔记 #学\n\n[... middle omitted ...]\n\nsed.\n\n<table><tr><td colspan=\"2\">Neutral</td></tr><tr><td>Price (07 Jul 26 15:00)</td><td>Rmb71.060</td></tr><tr><td>Target price</td><td>Rmb75.000</td></tr><tr><td>Expected share price return\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R054",
    "title": "Citi：被低估的第二曲线，Citi详解SpaceX的AI业务前景",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：被低估的第二曲线，Citi详解SpaceX的AI业务前景\n\n当一家公司的长期估值框架敢于对标“万亿俱乐部”成员，而当前市值已超过2.1万亿美元时，市场真正需要回答的问题不是“它值不值”，而是“它的增长引擎能否以可验证的方式持续运转”。Citi在近期一份长达62页的深度报告中给出了明确判断：SpaceX正处于2-3年催化剂密集期，其核心优势不在于单一业务，而在于用极端垂直整合将发射成本降至无人能及的水平，从而打开连接和人工智能两个万亿级市场。\n\n报告构建了一个清晰的逻辑链条：如果星舰（Starship）的关键工程里程碑在2026-2028年按计划实现，那么公司有能力在2031年实现约1万亿美元营收和约8300亿美元调整后EBITDA。报告将这个长期情景下的每股估值锚定在900美元以上。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 发射能力是护城河，但真正的变量是星舰的规模化节奏\n\nCiti认为，SpaceX现有的猎鹰9号发射能力已经是市场领先，但真正的结构性优势在于星舰。报告特别强调了几个关键里程碑：2026年下半年星舰开始向轨道运送有效载荷，2026年底前实现用“筷子”捕获星舰第二级，以及2027年发射“数十次”、2028年“数百次”、2031年“数千次”的节奏目标。\n\n这里需要关注的核心不是技术本身，而是成本曲线的陡峭程度。如果星舰实现完全快速复用——即助推器和飞船在24小时内重新飞行——那么每公斤入轨成本将降至现有水平的十分之一甚至更低。这不仅是发射业务的效率提升，更是整个空间基础设施商业模式的底层重构。\n\n> **KC评论：** Citi的逻辑是，当入轨成本下降一个数量级，原本不宏观环境的空间业务（如大规模卫星星座、空间计算）就变成了可盈利的生意。报告中的里程碑清单值得仔细看，尤其是“星舰V\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n这家公司，可能是下一个值得关注的长期故事\n\n从技术到连接，再到AI\n\n某外资机构近期覆盖了一家太空探索公司，给出了200美元的参考目标，并认为长期有望看到900美元以上。核心逻辑是：它正在用极致的垂直整合，打开三个万亿级市场。\n\n1/ 发射能力是地基\n这家公司拥有目前较为领先的火箭技术，而且还在迭代。Starship一旦成熟，能把东西送上太空的成本降到较低，规模做到较大。这是它所有业务的基础，也是同行较难复制的壁垒。\n\n2/ 连接业务是第二增长曲线\nStarlink星链已经在全球铺开，从宽带服务到手机直连卫星（D2D），市场空间在不断扩大。研报认为，它能成为全球性的电信服务商。\n\n3/ AI是未来想象空间\n这里分两块：\n- 地球AI：通过X平台的数据和Grok模型，以及收购Cursor，在AI企业服务市场拓展。\n- 太空AI：把算力送上太空，解决地球上的算力瓶颈，这可能是下一个重要方向。\n\n关键看点：未来2-3年，Starship能否实现高频次发射并快速复用，将是估值能否从200升至900的核心变量。\n\n你们觉得，太空经济离我们还有多远？欢迎一起讨论。\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[s\n\n[... middle omitted ...]\n\nkets that no other company can realistically tap into. SPCX is at the beginning of a particularly catalyst-rich 2-3 years which we expect will result in the company establishing dominant posit\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R055",
    "title": "关于某公司近期业务动态的观察笔记",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# 关于某公司近期业务动态的观察笔记\n\n六月宏观零售数据表现平稳，618大促的补贴和反哺效应进一步影响了客户管理收入（CMR）的节奏变化。某机构最新一期财报预览给出的判断是：市场当前对该公司云业务的收入增速和利润率改善已有一定预期，但真正需要重新校准的，是电商主业的利润韧性——尤其是核心电商板块在补贴调整与竞争格局稳定之间的平衡点。\n\n这份报告覆盖FY1Q27（自然年2026年4-6月）的业绩前瞻，核心调整集中在两处：CMR同比预计下降8.7%，但云业务收入增速上调至45%，云业务利润率同步改善至11.5%。一降一升之间，该公司正在经历从“电商驱动利润”到“云+AI驱动增长”的过渡期。这个过渡期能否平滑完成，取决于两个变量的节奏：补贴调整的速度，以及企业AI产品的商业化效率。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. CMR下滑不是周期问题，而是结构性的反哺成本\n\n据估算，核心电商板块本季度GMV增速已节奏变化至低个位数，这与4-5月社零数据表现以及618大促的补贴力度直接相关。但更值得关注的是，CMR同比下降8.7%这个数字背后，并非简单的流量下滑，而是“反哺”（contra-revenues）在当季被进一步放大——平台为了维持商家参与度和价格竞争力，持续以返点、补贴等形式让利。\n\n换句话说，广告收入的下滑不完全是需求变化，而是平台主动选择的一种成本结构。这种结构性成本在接下来几个季度不会快速消失。报告中也明确提到，反哺对CMR的压制将持续数个季度。\n\n> **观察评论：** 理解CMR下滑的关键不在于“电商是不是需要继续观察了”，而在于该公司是否愿意用短期收入换长期市场份额和商家粘性。完整报告里对反哺规模和持续时间的假设，是理解未来几个季度利润预期的基础。\n\n![研报原图 2](assets/source\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n阿里云增长明显，淘天仍在调整\n\n阿里云值得关注\n\n近期有机构发布了阿里新季度的业务前瞻分析，信息量较大，整理三个要点供参考。\n\n1️⃣ 淘天：618带动效果有限\n4-5月零售数据表现平稳，618大促也未带来明显波动。研报预计淘宝天猫GMV增速可能降至低个位数。更值得关注的是，大促期间平台对商家的补贴（counter-revenues）会进一步影响收入，预计客户管理收入（CMR）同比下降8.7%。不过，竞争态势有所缓和，本地生活（饿了么+淘鲜达）亏损在收窄，中国商业整体利润预计持平在380亿。\n\n2️⃣ 阿里云：增速和利润率双双提升\n这是值得关注的亮点。研报预计云收入增速可能加快至45% YoY，利润率有望提升至11.5%。背后是AI需求持续增长，通义千问、百炼平台、视频生成模型“寻光”等产品密集发布。近期还整合了企业级AI Agent产品，将“悟空”“MuleRun”的能力统一到“QoderWork”上，集中资源与字节的Coze和飞书Agent进行竞争。\n\n3️⃣ 外卖监管新动向，即时零售迎来新目标\n北京市场监督管理局召集美团、饿了么、京东进行沟通，核心是引导“分钟级”配送竞赛和过度补贴回归理性。这对平台长期\n\n[... middle omitted ...]\n\n Due to strong demand, we model Cloud revs to accelerate to 45%yoy with cloud margin improving to 11.5%. Into CY2H27, we expect a stable/unexciting macro with counter-revs impact on CMR persis\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R056",
    "title": "Citi：腾讯AI布局加速，混元3日均Token消耗增长20倍",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：腾讯AI布局加速，混元3日均Token消耗增长20倍\n\n腾讯即将于8月12日发布2026年第二季度财报。在Citi最新发布的业绩预览报告中，一个关键判断值得关注：腾讯的游戏和广告业务将继续提供扎实的收入支撑，但市场真正的焦点已转向AI投入的兑现节奏与利润影响。这份报告的核心张力在于——短期业绩与长期叙事之间的平衡点正在移动。\n\nCiti预计二季度总收入同比增长9.3%至2017亿元人民币，非GAAP净利润增长5.1%至662.5亿元，利润率约32.8%。这一预测低于彭博一致预期，主要分歧来自对AI相关投入的谨慎假设。换言之，市场对腾讯的定价逻辑，正在从“增长故事”向“效率故事”切换。\n\n> **KC评论：** Citi的利润预测比市场共识低约3个百分点，这暗示AI投入对利润表的短期影响可能被低估。完整报告中的分业务收入和利润率假设值得细看——尤其是云业务和资金科技板块的增速差异。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 游戏与广告的双引擎仍在运转，但增速分化正在收窄\n\nCiti预计二季度游戏总收入同比增长8.3%至641亿元，其中国内游戏增长8%，国际游戏增长9%。广告收入预计同比增长19%至425亿元。这两块业务合计贡献了腾讯总收入的约53%，是短期业绩的压舱石。\n\n值得注意的是，游戏收入的韧性并非来自新吸引人的，而是现有产品的持续运营。Citi指出，二季度虽有季节性因素，但游戏表现依然稳健。进入三季度，腾讯已上线《舞力全开：派对》和《Rust》，并计划在9月前推出《控制共鸣》。产品管线还包括《怪物猎人：旅人》《彩虹六号：围攻》等重磅IP。\n\n广告业务的19%增速虽然亮眼，但相比此前几个季度已有边际节奏变化。这并非需求减弱，而是基数效应开始显现。广告市场的结构性增长逻辑——短视频、视频号、小\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n腾讯下半年观察：游戏业务稳健，AI投入持续加大\n\n📌 游戏与广告业务稳健，AI投入值得关注\n\n某研究机构近期更新了对腾讯2Q26E的前瞻分析，预计8月12日发布中期报告。整体判断：收入端表现平稳，利润端存在一定调整。\n\n1️⃣ 收入端：游戏与广告双轮驱动\n- 2Q26E总收入预计同比增长约9.3%至2017亿\n- 游戏收入增长约8.3%（国内增长约8%，海外增长约9%）\n- 广告收入增长约19%，增速较为突出\n- 云业务收入增长约24%，金融科技业务增长约5.2%\n- 新游戏储备：Just Dance、Rust已上线，Control Resonant即将推出\n\n2️⃣ 利润端：AI相关投入影响\n- 非GAAP净利润同比增长约5.1%，低于收入增速\n- 利润率约32.8%，较市场预期低约1.2个百分点\n- 研究机构相对保守，主要因AI相关的资本开支和研发投入持续增加\n\n3️⃣ 下半年核心关注点\n- 微信内Agentic AI测试（小程序与Hy3整合）\n- Hy3模型于7月6日正式发布，预览期间日token消费量增长20倍\n- WorkBuddy月活跃用户达885万，被定位为“QQ和微信之后第三款现象级产品”\n-\n\n[... middle omitted ...]\n\nl continue to evaluate its investment portfolio with rotation and rebalance between strategic AI-related investment vs maturing industry with limited future synergies. Opportunistic buyback an\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R057",
    "title": "Citi：不是库存回补而是架构演进，Citi详解BBU渗透率跃升路径",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "Citi",
    "digest": "[wechat_article.md]\n# Citi：不是库存回补而是架构演进，Citi详解BBU渗透率跃升路径\n\nAI基础设施正在经历一场不易察觉但影响深远的电源架构变革。Citi最新发布的研究指出，随着机架功率密度持续攀升，数据中心备用电源正在从传统的集中式UPS向机架级分布式备份电源迁移。这一转变的核心组件——电池备份单元（BBU），正从可选配置变为高密度AI机架的标准配置。\n\n报告的核心判断是：BBU的单机架价值量和行业渗透率将在未来几年同步提升，形成一条被市场低估的多年度增长曲线。Citi测算，BBU在AI机架中的渗透率将从2025年的40-45%跃升至2026年的60-65%，到2027年超过85%。与此同时，单机架BBU价值量将从当前GB300 NVL72的约1.5-1.6万美元，攀升至Rubin架构的1.7-1.8万美元，在Rubin Ultra架构下可能超过3.3万美元。\n\n这一判断的关键驱动力来自两个方向：一是机架功率密度提升使得集中式UPS在响应速度、转换损耗和可扩展性方面的劣势被放大；二是高压直流配电架构的普及为分布式BBU创造了更好的集成条件。Citi认为，这不是一个周期性的库存回补，而是电源架构本身的结构性演进。\n\n> **KC评论：** 将BBU渗透率从40%拉到85%以上，意味着这个市场在未来三年内会从“少数先行者的选择”变成“行业标配”。对于关注AI硬件供应链的读者，报告第6页的BBU供应链估值对比表值得细看——它清晰展示了不同环节公司的当前定价是否已反映这一增长预期。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nCiti在报告中明确表达了对两家BBU供应商的不同偏好。AES-KY作为当前BBU市场的龙头，在规模、客户关系和技术积累上占据明显优势。但Citi认为，Dy\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# AI机柜的电源架构正在变化\n\n## BBU的演变\n\n从集中式UPS到机柜级备电，一个值得关注的结构性趋势\n\n### 1️⃣ 为什么BBU近期受到关注\n\nAI机柜的功率密度持续提升，传统集中式UPS逐渐难以适应。新一代架构正向分布式备电方向发展——BBU（电池备电单元）直接集成在机柜中，其优势包括：响应更迅速、转换损耗更低、扩展更灵活。\n\n行业研究指出，这一变化并非局部调整，而是AI电源架构的结构性迁移。BBU正从“可选配置”逐步成为高密度机柜的“标准配置”。\n\n### 2️⃣ 单机柜价值量逐步提升\n\n研究资料对BBU的单机柜价值量变化进行了分析：\n\n- GB300 NVL72：约1.5-1.6万美元\n- Rubin架构：1.7-1.8万美元\n- Rubin Ultra：可能超过3.3万美元\n\n同时，BBU的渗透率也在快速提升：2025年约40-45%，2026年达到60-65%，2027年预计超过85%。\n\n价值量与渗透率的组合，确实值得持续观察。\n\n### 3️⃣ 哪些公司可能受益\n\n研究资料重点提及了一家台湾公司Dynapack（3211.TWO）。其逻辑在于：该公司是BBU结构性增长中较为直接的受益\n\n[... middle omitted ...]\n\n it is one of the most direct beneficiaries of this structural transition. Boosted by accelerating BBU demand, improving product mix and expanding profitability, we forecast 34% sales CAGR and\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R058",
    "title": "DB：光伏玻璃正接近周期拐点，但多晶硅不确定性未减",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "DB",
    "digest": "[wechat_article.md]\n# DB：光伏玻璃正接近周期拐点，但多晶硅不确定性未减\n\n这份来自DB的2026年7月中国光伏行业报告，在行业普遍谨慎时给出了一个分化判断：光伏玻璃可能在经历九个月库存积累和价格下跌后，接近一个短期周期拐点；而多晶硅的库存去化已经结束，新一轮不确定性正在形成。报告的核心不是全面看好或看淡，而是指出产业链各环节正在走向不同的供需节奏。\n\n报告发布时，信义光能的报价已从5月中旬高点回调约38%，市净率降至0.6倍。DB认为这一估值已过度反映谨慎预期，并不意味着马上反转。\n\n> **KC评论：** 光伏玻璃的库存拐点是这份报告最值得关注的信号。库存从6月中旬高点下降约10%，且去化速度在最近几周加快。但读者需要区分“短期价格反弹”和“行业盈利修复”是两回事。报告对2027年的需求预测仍然保守，这意味着反弹的幅度和持续性仍需验证。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光伏玻璃的库存拐点已现，但盈利修复需要更长时间\n\n报告的核心判断建立在供需两侧的同时改善上。需求端，7月组件排产环比增长10%，带动玻璃需求温和复苏。供给端，由于行业整体亏损，产能重启意愿极低。DB测算当前玻璃价格已低于行业现金成本，这意味着任何需求改善都可能触发价格反弹。\n\n但报告没有回避一个关键问题：即便价格反弹，行业盈利能力的恢复仍取决于产能出清的速度。目前行业库存虽在下降，但相对水平仍然偏高。报告将信义光能2026年盈利预测从此前的盈利调整为亏损，这一调整本身就说明短期基本面并未根本好转。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 多晶硅：去库存只是插曲，雨季复产将加剧过剩\n\n与光伏玻璃形成鲜明对比的是多晶硅。DB指出，此前约三个月的库存去化（主要由通威驱动）已经结束。随着西南水电丰富地区进\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n光伏玻璃行业观察：周期变化与市场动态\n\n---\n\n近期看到一份关于光伏产业链的研究报告，其中对光伏玻璃等环节的分析值得关注，整理如下供参考。\n\n**1. 光伏玻璃：库存变化趋势显现**\n- 经历约9个月的库存积累和价格调整后，行业库存似乎在6月中旬达到阶段性高点，随后下降约10%，去库存速度有所加快。\n- 报告认为，7月行业可能逐步进入去库存阶段，背后是组件需求温和回升（环比+10%）和玻璃供给减少。\n- 在低基数需求、季节性回升和供给受限的共同作用下，光伏玻璃价格有望在未来几个月出现一定反弹。\n\n**2. 多晶硅：供给端面临新变化**\n- 此前约3个月的库存去化（主要由通威驱动）似乎已告一段落。\n- 随着西南地区进入丰水期，闲置的多晶硅产能正逐步复产，7月产量预计环比+6-7%。\n- 虽然新的能效标准（2027年1月生效）可能影响部分现有产能，但报告认为这不足以改变行业整体格局，因为终端需求变化才是核心因素。预计2027年行业产能利用率即使经过调整，仍将低于60%。\n\n**3. 产业链其他环节速览**\n- **硅片**：7月产量预计环比-6%，库存却环比+7%至28GW。盈利仍在现金成本线附近波动。\n- *\n\n[... middle omitted ...]\n\ny-demand analysis, which suggests the industry could enter a destocking phase in July, supported by a modest recovery in module demand (+10% MoM) and declining glass supply. With end demand st\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R059",
    "title": "DB：中国新能源车订单修复信号，比亚迪韧性凸显，蔚来修复而非反转",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "DB",
    "digest": "[wechat_article.md]\n# DB：中国新能源车订单修复信号，比亚迪韧性凸显，蔚来修复而非反转\n\n7月第一周的订单数据，可能比很多人预期的更能说明问题。DB最新发布的周度订单追踪显示，中国新能源汽车市场正在经历一轮明显的“K型分化”：头部企业的订单集中度在提升，而部分曾经的热门品牌开始显露调整迹象。\n\n这份报告追踪的并非交付量，而是新订单——后者是更前置的需求指标。在7月1日当周（W27），比亚迪单周新订单达到8.65万辆，环比增长23%，同比增长11%。而同一周，理想汽车新订单仅5700辆，环比下降42%，同比下降40%。特斯拉中国的新订单也同比下降了36%。\n\n这些数字叠加在一起，指向一个观察：中国新能源车市场的增长红利正在向少数几家拥有定价能力或产品定义能力的公司集中，其余玩家面临的是份额争夺战，而非增量蛋糕的分配。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪的周订单跳升，背后是产品矩阵的“全价格带覆盖”\n\n比亚迪8.65万辆的周订单并非偶然。从6月最后一周的7.06万辆跳升至8.65万辆，环比增幅达23%。这背后是比亚迪在7月初推出的新一轮限时优惠和权益调整，覆盖了从海鸥到汉、唐的多个主力车型。\n\n关键在于，比亚迪的订单增长并非依赖单一产品，而是由其完整的产品矩阵支撑。从10万元以下到30万元以上的价格带，比亚迪在每个区间都有至少一款具备竞争力的车型。这种“全价格带覆盖”策略，使得它在面对友商的新品冲击时，有更大的腾挪空间。\n\n> **KC评论：** 比亚迪的订单韧性，本质上是规模效应与产品矩阵深度带来的“抗波动能力”。对于其他车企而言，单点突破越来越难，因为对手在每个价格带都预留了反击弹药。完整报告中的图表清晰展示了比亚迪订单曲线的波动区间，值得细看。\n\n![研报原图 2](assets/source_image_02\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n7月首周新能源车订单速览\n\n📊 周度订单快报\n\n7月第一周（5天），新能源车订单表现呈现分化：\n\n**比亚迪** 周订单8.65万，环比+23%，同比+11%。6月底冲量后，7月初依然保持稳定。\n\n**蔚来** 周订单1.08万，同比+96%，是增速较快的品牌。虽然环比-7%，但去年同期基数低，增长趋势值得关注。\n\n**理想** 环比-42%，周订单0.57万，同比-40%。6月冲刺后有所调整。\n\n**特斯拉** 周订单1.09万，同比-36%，环比-3%。\n\n**小鹏、小米、零跑** 环比均下降8%-11%，整体处于7月常规调整阶段。\n\n**吉利（极氪+银河）** 周订单2.27万，环比-20%。\n\n**鸿蒙智行（主问界）** 周订单0.81万，环比-25%，同比-18%。\n\n**几个观察：**\n1. 7月首周整体有所降温，多数品牌环比下滑，符合季节性特征\n2. 比亚迪逆势增长，份额进一步集中\n3. 蔚来同比增幅明显，后续持续性值得留意\n4. 特斯拉同比降幅较大，竞争环境变化\n\n7月是传统调整期，各品牌都在为下半年新品做准备。你对哪个品牌三季度表现更感兴趣？\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[... middle omitted ...]\n\n>WoW</td><td>YoY</td></tr><tr><td colspan=\"7\">Weekly New Orders of key OEMs</td></tr><tr><td>1211 HK</td><td>BYD</td><td>86.5 k</td><td>70.6 k</td><td>78 k</td><td>23%</td><td>11%</td></tr><tr\n\n[... middle omitted ...]\n\nited Kingdom\nTel: (44) 20 7545 8000\n\nDB Securities Inc.\n\nThe DB Center\n1 Columbus Circle\nNew York, NY 10019\nTel: (1) 212 250 2500\n\nDB AG\nFiliale Singapur\nOne Raffles Quay, South Tower\nSingapore 048583\nTel: (65) 6423 8001"
  },
  {
    "id": "R060",
    "title": "DB：人形机器人收购情绪高涨，但埃斯顿利润修复可持续吗？",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "DB",
    "digest": "[wechat_article.md]\n# DB：人形机器人收购情绪高涨，但埃斯顿利润修复可持续吗？\n\n这份DB首次覆盖埃斯顿的研报，最值得关注的判断并非利润修复本身，而是它揭示了一个正在形成的市场结构：相关市场读者对人形机器人主题的定价热情，与H股读者的冷静形成了鲜明对比。报告对相关市场更新公司观点、对H股更新公司观点，这个评级差异本身，就是当前中国机器人行业估值分化的缩影。\n\n埃斯顿预计在7月发布盈利预喜。1H26净利润预计同比增长近20倍，从700万人民币跃升至1.38亿。这个数字看起来很惊人，但基数极低——2025年上半年净利润仅700万。真正值得看的是收入端：2Q26收入预计同比增长15%，扭转1Q26的-2%下滑。电池和电子终端需求回暖、一季度5-15%的提价逐步兑现，是主要驱动力。\n\n但利润修复的可持续性，报告没有完全回答。一季度净利润包含8700万的非经常性收益，2Q26环比将明显回落。资产减值损失也可能随汽车业务占比提升而增加。DB预计2026全年净利润3.05亿，净利率5.1%，这个水平在工业机器人行业里并不突出。\n\n> **KC评论：** 利润修复是真实的，但市场对埃斯顿的定价早已脱离了当期利润。2026年P/E高达146倍，P/S 7.4倍。读者买的不是2026年的利润，而是人形机器人这个远期期权。完整报告里关于Codroid的财务数据值得细看——2025年收入仅5000万，净亏损5300万，收购对短期财报贡献几乎为零。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 人形机器人收购：情绪价值远大于财务价值\n\n埃斯顿7月2日公告正考虑现金收购Codroid全部股权。Codroid成立于2022年，生产协作机器人、具身机器人和核心零部件，2025年收入5000万，净亏损5300万。埃斯顿已持有其13.95%股权，母公司南京派雷斯特科\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 人形机器人热度观察\n\n📌 人形机器人收购案相关动态\n\n某外资研究机构最新报告，关注这家工业机器人公司的发展情况。\n\n1️⃣ **业绩变化节点已现，但需理性看待**\n- 预计1H26净利润同比增幅较大，但基数较低（去年1H25约700万）\n- 2Q26营收预计15亿，同比+15%，受益于电池和电子端需求回暖\n- 毛利率有望回升至31%，与产品定价调整和成本管理有关\n\n2️⃣ **人形机器人收购：市场关注度较高**\n- 公司正考虑现金收购Codroid（已持股14%，母公司持股39%）\n- Codroid 2025年营收约5000万，净亏损5300万——短期贡献有限\n- 市场对此反应积极：A股估值已按2026年PS 7.4倍定价，接近优必选的11倍\n\n3️⃣ **A/H股估值差异明显**\n- A股目标价31.4元，评级Sell（当前46元，已反映人形机器人预期）\n- H股目标价23.6港元，评级Hold（估值相对合理，PS仅3.3倍）\n- 港股读者对人形机器人更为审慎，折价普遍超50%\n\n4️⃣ **需关注的主要因素**\n- 人形机器人尚未形成稳定收入，模型训练成本持续增加\n- 外部环境变化可能影响出口业务\n\n[... middle omitted ...]\n\nth the company's guidance. The potential acquisition of the humanoid robot business Codroid should contribute minimally to financials, but positively to valuation. This optimism is well-reflec\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R061",
    "title": "从零售到批发，世纪互联利润率拐点如何兑现？",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "DB",
    "digest": "[wechat_article.md]\n# 从零售到批发，世纪互联利润率拐点如何兑现？\n\n中国第三方数据中心行业正在经历一次结构性分化。当市场普遍关注行业供给过剩不确定性时，一份来自DB的深度研报给出了相反的判断：世纪互联（VNET）正在进入一个由订单、客户结构和资本模式共同驱动的增长拐点。报告的核心信号不是“行业变好”，而是“这家公司变了”。\n\n这份研报覆盖的时点值得注意。2026年上半年，世纪互联累计获得517MW新订单，其中510MW来自字节跳动，规模远超同行。这不是简单的需求回暖，而是公司从零售型IDC运营商向超大规模数据中心开发商的转型正在兑现。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订单规模已经拉开了与同行的差距\n\n报告中最有信息量的数据是订单对比。2026年前五个月，世纪互联新签517MW，而同一时期万国数据（GDS）为334MW。差距不仅在于总量，更在于客户结构——字节跳动一笔订单就贡献了510MW，集中在京津冀地区的两个园区。\n\n这种订单密度意味着什么？字节跳动通常上架速度很快，交付后能迅速转化为收入。报告预计这些项目分三批交付：2026年下半年三分之一、2027年上半年三分之一、剩余在2027下半年至2028年上半年。2027年的收入增长会明显好于2026年。\n\n> **KC评论：** 订单领先本身不是新闻，但领先幅度和客户集中度值得关注。世纪互联目前对单一大客户的依赖度显著上升，这既是增长引擎，也是不确定性敞口。报告没有完全展开的是，一旦字节跳动的需求节奏变化，公司能否快速找到替代客户来填补产能。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 商业模式切换正在重塑利润率\n\n世纪互联的收入结构已经发生质变。2026年第一季度，批发型IDC收入首次超过零售型，占总收入约40%。这不\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 这家数据中心公司，正在从“零售”转向“批发”\n\n**转型进行时**\n\n**字节跳动大单背后，藏着什么逻辑？**\n\n---\n\n最近某外资机构首次覆盖了一家国内数据中心运营商，直接给出积极评级，目标价较当前有约60%的上行空间。\n\n核心逻辑很简单：**这家公司正在经历一场从零售到批发的业务大转型。**\n\n1️⃣ **订单增长，字节跳动是重要推动力**\n\n今年至今，公司新签批发订单517MW，超过同行的334MW。其中510MW来自字节跳动，两个数据中心园区都在大北京区域，分批交付：2H26交1/3，1H27交1/3，剩下的2H27-1H28交完。\n\n字节跳动的上架速度一向很快，意味着这些容量很快就能转化为收入和利润。\n\n2️⃣ **业务结构已出现关键拐点**\n\n2026年Q1，批发业务收入首次超过零售，占整体营收约40%。这是公司从传统零售IDC服务商，转型为以超大规模数据中心为主力的重要里程碑。\n\n零售业务依然稳定，客户流失率常年低于1%；非IDC业务（微软云代理+企业VPN）贡献约22%。\n\n3️⃣ **土地储备充足，西部建成本更低**\n\n公司在乌兰察布等地有超过1GW的批发容量储备，建设成本比一线城市低\n\n[... middle omitted ...]\n\nal capex program. The successful monetization of mature data centers at 13-14x EV/EBITDA through REIT listing provides an important source of capital and could support a self-reinforcing devel\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R062",
    "title": "GS：GS详解一家半导体设备商，二季度超预期，毛利率先升后降再升",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：GS详解一家半导体设备商，二季度超预期，毛利率先升后降再升\n\n市场对共封装光学（CPO）技术路线的疑虑，让一家台湾半导体后端设备供应商的报价从高点下跌超过三成。但GS最新研究认为，这些担忧很大程度上已经反映在当前报价中，而公司真正的增长方向——先进封装扩产和下一代CPO设备的更高价值——正在加速推进。\n\n这份由分析师Evelyn Yu和Ryan Huang签发的报告，核心判断可以概括为：CPO的出货量预期被下调，但单台设备的价值和定价都在提升；与此同时，CoWoS产能的加速扩张为2027年提供了更确定的收入支撑。两者叠加，不确定性回报比正在向有利方向倾斜。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度超预期，但毛利率的“新老交替”值得关注\n\n公司6月营收10.12亿新台币，带动整个第二季度营收达到23.55亿新台币，比GS此前的预测高出12.8%。超预期的主要驱动力来自客户对CoWoS需求的强劲拉货。\n\n但更有意思的是毛利率的阶段性变化。GS将二季度和三季度的毛利率预期分别上调至54.0%和54.5%，背后是先进封装产品组合占比提升。然而，随着公司开始出货新的面板级设备，四季度毛利率预计会小幅回落至52.7%。\n\n> **KC评论：** 毛利率在四季度出现短期下滑，不是因为需求变差，而是新产品爬坡期的正常成本结构。完整报告里对2026年各季度毛利率的拆解，值得关注的是这个“先升后降再升”的节奏是否已被市场充分理解。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 2027年CoWoS扩产加速，这家供应商是直接受益者\n\nGS在7月初的台积电报告中，将2027年底的CoWoS（含WMCM）产能预估从此前的25万片/月上调至28万片/月。作为CoWoS后端设\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 先进封装设备趋势观察\n\n近期，某外资机构更新了对一家台湾先进封装设备商的研究观点，核心逻辑较为清晰。\n\n1️⃣ 近期动能超出预期  \n6月营收表现优于预期，二季度整体较预测高出12.8%。主要原因是CoWoS相关需求拉动更为明显。毛利率也因此有所上调，预计Q2至Q4分别为54.0%/54.5%/52.7%。Q4小幅回落，主要因开始出货新面板级设备，初期会摊薄毛利。\n\n2️⃣ 2027年CoWoS增长预期更为明确  \nTSMC的CoWoS产能目标上调至28万片/月（此前为25万），该设备商直接受益。研报预计其CoWoS相关收入在2027年同比增长27%，占总收入77%。这一比例较此前预估的60%有明显提升。\n\n3️⃣ CPO逻辑变化：台数减少，单价上升  \nCPO方面，设备出货台数有所下调，但单台ASP预计提升约20%。原因是设备商在提升单台效率，客户需求不变但所需设备减少。预计CPO收入在2027/2028年分别占16%/60%（此前预估为29%/69%）。\n\n4️⃣ 价格调整后的观察机会  \n从4月高点回撤约31%，市场主要关注CPO的节奏变化。但研报认为CoWoS和CPO的基本需求均较为扎实，且该公司\n\n[... middle omitted ...]\n\npreviously), supported by a higher advanced packaging mix, though we now expect a modest sequential decline in 4Q26 GM as All Ring begins shipping new products including new panel-level equipm\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R063",
    "title": "GS：惠普出货量下滑9%，PC行业分化从供应链开始",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：惠普出货量下滑9%，PC行业分化从供应链开始\n\n连续九个季度的正增长之后，全球PC市场出现调整。IDC最新数据显示，2026年第二季度PC出货量（含工作站）约为6820万台，同比下降4.9%。这是自2024年初以来的首次季度同比下滑，标志着行业进入了一个新的调整阶段。\n\nGS在最新发布的行业报告中指出，本轮调整并非需求端的全面变化，而是供给端的结构性收紧。内存、存储等关键元器件的持续短缺，叠加宏观环境的不确定性，构成了出货量下滑的主要因素。更关键的是，IDC预计这一局面要到2028年初才可能缓解，下半年出货量将因平均售价上升和供应受限而出现更明显的下降。\n\n这意味着，行业竞争的逻辑正在发生根本性转变。当供给成为瓶颈，谁能拿到足够的元器件、谁能管理好复杂的供应链，谁就能在份额争夺中占据主动。GS判断，拥有多产品线和成熟供应链管理能力的大型厂商——苹果、戴尔、联想——将有机会在这一轮调整中进一步巩固市场地位，从小型竞争者手中获取份额。\n\n> **KC观察：** 过去几年，PC行业讨论最多的是“需求何时恢复”。现在问题变成了“在供给受限的环境下，谁的供应链更强”。这份报告的核心信号是：规模不再是锦上添花，而是生存和扩张的必要条件。完整报告中的出货量数据表值得细看，它揭示了各厂商在不同季度的增长节奏差异，这些差异背后是供应链策略的体现。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 苹果和华硕逆势增长，惠普成为变化最明显的厂商\n\n从市场份额变化来看，第二季度的赢家和输家非常清晰。\n\n苹果出货量同比增长10%，市场份额达到9.9%，是Top5厂商中增速最快的。华硕出货量基本持平，微增0.2%，份额维持在7.4%。联想出货量同比下滑2%，但凭借24.4%的份额仍居行业首位。戴尔出货量下降5%，份额降至13.6%。惠\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nPC九连涨后首次下滑，哪些品牌表现稳健？\n\n📉 全球PC出货量首次转负\n\nIDC近期发布2Q26数据：全球PC出货6820万台，同比-4.9%，结束了连续9个季度的正增长。主要原因在于存储和内存供应紧张，加上宏观环境影响，相关研究预计供应问题要到2028年初才逐步缓解。\n\n📊 各品牌表现分化明显\n\n1️⃣ **苹果+10%**（市占9.9%）\n   - 连续多季保持增长，供应链管理能力是核心优势\n\n2️⃣ **华硕+0.2%**（市占7.4%）\n   - 基本持平大盘，但份额微增\n\n3️⃣ **联想-2%**（市占24.4%）\n   - 虽有所下滑，但仍是市占第一\n\n4️⃣ **戴尔-5%**（市占13.6%）\n   - 与大盘同步下滑\n\n5️⃣ **惠普-9%**（市占19.1%）\n   - 跌幅相对明显，份额承压\n\n🔍 几个值得关注的观察\n\n- 虽然出货量下滑，但行业收入却在增长——因为产品均价有所上升。平均售价提升部分抵消了出货减少的影响。\n- 供应紧张反而对大型品牌有利。研究指出，像苹果、戴尔、联想这类产品线丰富、供应链管理成熟的企业，有望在长期整合中扩大份额。\n- 下半年预计出货量可能继续调整，因为\n\n[... middle omitted ...]\n\nlimited supply. Though units are down, IDC observes industry revenue growth from price increases. A prolonged supply shortage should benefit larger, scaled players with multiple product lines \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R064",
    "title": "GS：中国6月CPI回落背后，能源和黄金价格波动才是主因",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：中国6月CPI回落背后，能源和黄金价格波动才是主因\n\n中国6月通胀数据出炉，CPI同比从5月的+1.2%回落至+1.0%，PPI同比则从+3.9%微升至+4.1%。表面看，PPI仍在走高，但GS团队判断：这很可能是本轮PPI再通胀的阶段性峰值。更关键的是，二季度PPI的超预期表现，更多来自能源价格的前置冲击，而非需求端的持续性改善。随着原油价格预期下修，下半年PPI同比将逐步回落。\n\n**这份报告真正值得关注的是它对2027年PPI预测的调整——从+0.6%直接下调至0%。** 这意味着，GS认为本轮由能源驱动的价格冲击，其尾部影响将比市场普遍预期的更快消退。对于依赖价格弹性做库存决策的企业，以及关注工业利润分配格局的读者，这个信号值得认真对待。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源和黄金是CPI节奏变化的主要影响，核心通胀保持稳定\n\n6月CPI同比回落，并非需求走弱所致，而是结构性的价格因素在起作用。GS援引国家统计局的测算称，燃料成本和黄金价格下跌，合计解释了CPI同比从5月到6月0.23个百分点的降幅。其中，燃料价格同比从+21.1%大幅收窄至+15.3%；“其他商品与服务”价格同比从+9.9%降至+6.6%，主要反映金饰价格回调。\n\n剔除食品和能源后的核心CPI同比仅从+1.1%微降至+1.0%，基本平稳。食品端，猪肉价格同比-15.9%，较5月的-16.1%略有收窄，但仍在深度负区间。整体而言，CPI读数反映的是能源和贵金属价格波动的传导，而非消费动能的实质性变化。\n\n> **KC评论：** 核心通胀稳定意味着，当前政策层面无需因物价数据而调整节奏。真正需要关注的是PPI回落的速度，以及它对企业利润分配和库存周期的含义——这比单月CPI波动更有观察价值。\n\n![研报原图 2](a\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n6月CPI、PPI数据公布，如何理解？\n\n通胀数据变化，保持观察\n\n6月CPI同比+1.0%，较5月的+1.2%略有回落。PPI同比+4.1%，较5月的+3.9%小幅上升，但环比增长动力有所减弱。\n\n1️⃣ CPI放缓，能源和黄金是主要因素\n- 食品价格同比-1.6%，与5月基本持平。猪肉-15.9%，蔬菜-0.3%，水果-0.7%。\n- 非食品价格同比+1.5%，较5月的+1.9%明显回落。燃料成本从+21.1%降至+15.3%，交通服务从+4.7%降至+3.8%。\n- 核心CPI（剔除食品和能源）同比+1.0%，较5月的+1.1%略低，主要受金价走弱影响。“其他商品/服务”从+9.9%降至+6.6%。\n\n2️⃣ PPI小幅上升，但增长动能或已见顶\n- 上游贡献基本稳定，油气和化工价格下跌，被黑色金属和煤炭上涨所抵消。\n- 下游贡献了全部0.2个百分点的涨幅，其中一半来自电子设备制造（计算机、通信设备）。\n- 环比年化增速从5月的+8.8%降至6月的+1.2%，显示涨价势头明显放缓。\n\n3️⃣ 下半年PPI走势展望\n研究机构认为，二季度PPI表现超出预期，但大宗商品团队已下调下半年和明年的油价预测。因此，下\n\n[... middle omitted ...]\n\n more front-loaded oil-driven reflation shock than we previously anticipated. On the back of our commodity team's lower oil price forecasts, we revise down our H2 sequential PPI inflation, and\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R065",
    "title": "GS：央行调整例会措辞，GS解读为何短期不调整利率",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：央行调整例会措辞，GS解读为何短期不调整利率\n\n中国央行在二季度货币政策委员会例会上的措辞出现了微妙但重要的变化。GS最新研报指出，央行对国内增长的描述从“总体平稳、稳中有进”调整为“总体平稳、向新向优”，并首次明确提及“结构性分化”。这意味着决策层已更清晰地看到宏观环境复苏的不均衡——尤其是内需偏弱的事实。但报告的真正判断在于：**央行并未因此准备开启新一轮全面宽松**。\n\nGS维持其基准预测——2026年全年不调整利率、不调整准备金率。近期的政策支撑更可能来自财政支出提速、银行间流动性充裕以及定向信贷工具，而非总量层面的货币宽松。这一判断与市场部分降息预期形成对比，值得关注。\n\n与此同时，央行行长潘功胜在7月7日宣布了一揽子支持香港离岸人民币市场的措施。GS将其归类为两大方向：提升流动性和完善市场基础设施。这组动作，连同此前推出的跨境债券回购，共同指向一个更清晰的战略意图——人民币国际化的下一阶段，将由离岸市场主导、以香港为中心。\n\n> **KC评论：** 央行在例会措辞上的调整，是“承认问题但不出重手”的典型信号。对于关注宏观政策的读者，报告里值得细看的是央行删掉了“综合运用多种工具，加强货币政策调控”这句话——这是判断短期不会全面宽松的关键依据。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 二季度例会措辞调整：承认分化，但未暗示加码\n\n与一季度相比，央行在二季度例会声明中做了两处关键修改。第一，将国内宏观环境描述从“总体平稳、稳中有进”改为“总体平稳、向新向优”。“向新向优”指向结构性转型，而非总量扩张。第二，新增了“结构性挑战”的表述，这被GS解读为对宏观环境复苏不均衡、内需偏弱的更清晰认知。\n\n但报告同时指出，声明并未释放即将加大宽松力度的信号。央行删除了“综合运用多种工具，加强货币政策调控”这一\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n央行最新信号：降息降准不急于一时\n\n**政策定力**\n**但香港离岸市场迎来新支持**\n\n---\n\n央行刚开了Q2货币政策委员会例会，通稿里有些新变化值得关注👇\n\n**1/ 对宏观环境判断更谨慎了**\n之前说\"总体平稳、稳中有进\"，这次改成\"总体平稳、向新向优\"。\n还新增了\"结构分化\"的表述——可以理解为，当前内需偏弱、增长不均衡的情况被进一步确认。\n\n**2/ 但短期不会大放水**\n\"综合运用多种工具加强调控\"这句话这次删了。\n研究机构判断：年内降息降准概率不大。\n短期靠什么？财政发力更快、银行间流动性充裕、定向信贷支持。\n\n**3/ 香港离岸市场有新动作**\n7月7日潘功胜宣布了一揽子措施，分成两类：\n- **流动性支持**：债券通南向额度从5000亿扩到8000亿；香港金管局人民币贸易融资安排从2000亿扩到5000亿；还打算推7天离岸人民币流动性招标工具。\n- **市场基础设施**：推离岸国债期货、扩大人民币债券抵押范围、延长北向通结算时间、新增FDR007利率互换合约。\n\n**4/ 人民币国际化下一站**\n研究认为，这些措施指向一个方向：离岸主导、香港中心。\n从贸易结算往投融资功能延伸，流动性更深、\n\n[... middle omitted ...]\n\nn our baseline of no policy rate or RRR cuts in 2026. In our view, near-term policy support is more likely to more likely to come through faster fiscal policy implementation, ample interbank l\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R066",
    "title": "GS：硬件与入境旅游跑赢软件，GS日本中小盘分化明显",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：硬件与入境旅游跑赢软件，GS日本中小盘分化明显\n\n日本中小盘公司（SMID）的股东会投票季传递出一个微妙信号：过去几年该群体承受的CEO批准率波动正在向大盘股靠拢。GS最新发布的日本SMID监测报告显示，2026年股东会季，中小盘与大盘股CEO批准率的四分位差已从2024年的明显分化收敛至同一水平——9%。这意味着，日本中小盘公司曾经“更容易因个别事件被股东惩罚”的特征正在消退，市场对管理层的评价标准正趋于统一。\n\n这一变化的背后，是日本公司治理改革的持续渗透。2024年，中小盘CEO批准率的四分位差一度超过11%，而流动性更强的大盘股仅为7%。到2026年，两者已完全趋同。GS分析师Bruce Kirk和Julius Chan在报告中指出，目前仅有约15%的中小盘公司CEO批准率低于80%，而大盘股中这一比例不到10%。但整体均值和中位数的差异几乎可以忽略。\n\n> **KC评论：** 股东不确定性收敛不等于不确定性消失。它意味着市场不再用“大小盘”来区分治理不确定性，而是用行业和具体公司行为来定价。对读者而言，过去那种“买大盘股更安全”的标签式判断需要重新校准。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 行业分化比市值分化更值得关注：硬件、工业和入境旅游跑赢IT服务\n\nGS覆盖的日本SMID公司在6月表现出了鲜明的行业分化。Taiyo Yuden（+36%）、Japan Material（+25%）、Kyoritsu Maintenance（+21%）和Kotobuki Spirits（+19%）领涨，而ANYCOLOR（-22%）和Cover Corp（-14%）垫底。主题指数层面，区域银行（+17%）和银行（+11%）领跑，SAAS（-13%）和软件（-9%）垫底。\n\n报告没有完全解释这种分化\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n日本中小盘公司观察\n\n📊 中小盘公司治理动态\n\n日本中小盘公司正面临更多来自持有人的关注。\n\n相关研究数据显示，超过15%的日本中小盘公司CEO支持率低于80%，而流动性更好的大盘股中这一比例不到10%。\n\n不过从整体平均支持率变化来看，两者差距并不显著。\n\n**1/ 股东会趋势变化**\n中小盘CEO支持率的四分位差（IQR）在2024年达到11%的峰值，但到2026年已回落至9%。\n同期，流动性更好公司的CEO支持率IQR从7%升至9%。\n两边目前几乎持平，说明中小盘公司在治理改善方面进展更快。\n\n**2/ 6月表现分化**\n科技硬件、工业和入境旅游板块表现优于IT服务。\n• 太阳诱电（+36%）、日本Material（+25%）、共立维护（+21%）涨幅居前\n• ANYCOLOR（-22%）、Cover Corp（-14%）表现相对靠后\n\n**3/ 金融板块表现突出，软件板块承压**\n6月行业指数中，区域银行（+17%）和银行（+11%）表现最佳。\nSAAS（-13%）和软件（-9%）跌幅较大。\n\n**4/ 造船业值得留意**\n日本2026年5月订单积压达2930万总吨，相当于未来3-4年的需求。\n有消息\n\n[... middle omitted ...]\n\nExhibit 6), there appears to be very little difference between the two data-sets. Historically, CEO approval IQRs were significantly higher with Japan SMID stocks (Exhibit 6), but this differe\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R067",
    "title": "关于Costco近期运营数据的观察笔记",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# 关于Costco近期运营数据的观察笔记\n\n这份来自研究机构的报告，关注的不是 Costco 6 月销售数据本身——全球同店增长 7.0%，略低于一致预期的 7.3%——而是数据背后一个更值得注意的信号：客流量在减速，但管理层表示没有观察到消费者行为或竞争格局的实质性变化。\n\n对长期跟踪零售的读者来说，这组数据最有趣的地方在于，它把一个问题摆到了桌面上：当一家公司增长节奏变化，但管理层既不认为是大环境问题，也不认为是竞争加剧，那问题出在哪里？\n\n答案可能藏在报告里一个不起眼的细节：新店蚕食效应在 6 月对 Costco 产生了约 50 个基点的谨慎影响。这是理解这组数字的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 客流量减速是结构性的，但并非需求性的\n\n6 月全球客流量增速从 5 月的 3.9% 降至 3.2%，美国市场从 3.7% 降至 3.2%。与此同时，全球客单价增速也从 4.0% 降至 3.7%。\n\n这两个数字同时走弱，看起来像是需求节奏变化的典型信号。但报告引用了管理层的判断：没有观察到消费者趋势或竞争格局的重大变化。\n\n> **观察评论：** 管理层说“没变”，不等于数据“没变”。关键在于这个减速是否被新店蚕食效应解释。报告估算蚕食影响约 50 个基点，如果把这部分加回去，实际经营趋势可能更接近 5 月水平。完整报告里的图表 3 专门展示了蚕食影响的月度变化，值得仔细看。\n\n这意味着，Costco 面临的不是一个需求问题，而是一个选址和密度问题。当新店开在现有会员的覆盖范围内，短期会分流既有门店客流，但长期看，这恰恰是提高会员渗透率的必经之路。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 品类结构没有出现变化，反而有亮点\n\n报告按品类拆分\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nCostco 6月运营数据：客流增速趋稳，会员消费黏性保持\n\n**客流增速趋稳，会员消费意愿仍在**\n\n**6月数据反映了哪些市场趋势？**\n\n---\n\n6月运营数据已公布，Costco的同店销售（剔除油价和汇率影响）增长7.0%，略低于市场预期的7.3%，也较5月的8.0%有所回落。不过，管理层表示，目前未观察到消费者行为或竞争格局出现明显变化。\n\n**1/ 客流增速有所趋稳**\n\n全球客流增速从5月的3.9%降至6月的3.2%，美国市场也从3.7%降至3.2%。客单价（剔除油价和汇率影响）同样呈现趋稳态势，美国市场从5.0%降至4.4%。\n\n**2/ 品类表现分化明显**\n\n- **生鲜食品**：中高个位数增长，烘焙和肉类品类表现突出\n- **食品杂货**：低到中个位数增长，糖果和冷冻食品为主要增长品类\n- **非食品**：中到高个位数增长，黄金首饰、家居用品、家电销售情况良好\n- **附属业务**：高二十个百分点增长，药店、加油站、助听器位列前三。管理层提到，GLP-1药物需求、Costco专科药房业务扩展，以及新增支付方式，共同推动了药房收入增长\n\n**3/ 新尝试：独立加油站**\n\n由于门店附近缺乏\n\n[... middle omitted ...]\n\n, which opened in Mission Viejo, CA due to a lack of real estate space at the nearby warehouse. Going forward, standalone gas stations will be opened as needed, based on real estate constraint\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R068",
    "title": "GS：长虹AI电视定价高420美元，GS称产品化能力成竞争关键",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：长虹AI电视定价高420美元，GS称产品化能力成竞争关键\n\n一份来自GS的最新行业观察显示，LCD电视面板价格在经历2026年上半年的温和上涨后，6月环比已趋于持平。但这并非报告的核心信号。真正值得关注的，是面板行业竞争格局的实质性改善，以及三个正在打开新需求空间的细分方向：AI电视、高刷新率电竞显示器，以及电子纸显示在消费电子中的跨界应用。\n\n报告认为，面板行业竞争正在变得更健康。头部供应商不再单纯追求产能利用率最大化，而是根据市场需求灵活调节产线负荷，从而稳定产品均价。这一判断在价格数据上得到印证：32英寸、43英寸、55英寸和65英寸面板今年以来的累计涨幅在4%至9%之间，但当前价格仍远低于2021年7月的高峰——这意味着行业已走出最差的供需失衡阶段，但远未到过热。\n\n> **KC评论：** 面板价格企稳本身并不意外，但GS强调的“竞争变健康”是一个更重要的定性判断。过去几年面板行业最大的问题是产能扩张过快导致价格竞争，现在头部厂商开始用产能调节代替降价抢单，这对整个产业链的盈利稳定性是一个结构性利好。完整报告中的价格走势图值得细看，尤其是2026年YTD的涨幅斜率——它比2024-2025年任何一轮反弹都更平缓，也更可持续。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI电视开始从概念走向产品化，差异在于大模型集成能力\n\n长虹在5月发布的D8S Pro AI电视，是这份报告中最具代表性的产品。它搭载了100英寸Mini LED面板，同时集成了通义千问、豆包、DeepSeek等多个大模型。相比2024年2月发布的85U8F，新机型价格高出约420美元，但存储容量弹性较高，AI功能从单一的语音助手扩展为智能问答、AI教育、生活助理和AI搜索。\n\n这一变化意味着：电视厂商正在把“AI电视”从营销话\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nLCD面板价格企稳，新终端需求增长\n\n面板行业企稳 + AI电视需求提升\n\nLCD TV面板价格6月环比持平，但2026年至今累计上涨4%-9%，供需关系逐步改善。\n\n近期几款新品值得关注👇\n\n1️⃣ **AI电视登场**\n长虹D8S Pro，100寸Mini LED屏，搭载通义千问、豆包、DeepSeek等多个大模型。不仅支持问答功能，还可作为AI教育及生活助手。相比上一代价格提升约$420，但存储空间更大、屏幕尺寸升级。\n\n2️⃣ **电竞显示器刷新率提升**\nTCL P2A Ultra，27寸Mini LED，刷新率可在550Hz和1080Hz之间切换，峰值亮度800nits，延迟1ms。定价$514，比Pro版贵$276，但刷新率表现更优。\n\n3️⃣ **电子纸新应用**\nInsta360的无线麦克风Mic Pro，首次在领夹麦上采用1.22寸六色电子纸屏。用户可自定义显示logo、频道标识。电子纸技术正逐步渗透更多消费电子品类。\n\n面板厂商通过调节产能利用率来稳定价格，行业竞争格局趋于优化。新终端（AI TV、高刷显示器、电子纸）也在拓展增量空间。\n\n欢迎交流面板周期与终端创新🧐\n\n#学习笔记 #研\n\n[... middle omitted ...]\n\nASP better by adjusting their production utilization rate depending on market demand.\n\nExhibit 1: Price increased YTD LCD TV panel price trend  \n![](images/a5fddb335ba728cd111da7713171455f6371\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R069",
    "title": "GS：欧莱雅接手Gucci彩妆，YSL模式能否再现",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：欧莱雅接手Gucci彩妆，YSL模式能否再现\n\n欧莱雅与科蒂提前终止Gucci授权协议，将古驰彩妆的掌控权收入囊中。这笔交易的核心逻辑不在于财务数字本身，而在于欧莱雅能否复制YSL Beauty的路径——将Gucci彩妆从目前约5亿欧元的规模推向十亿级。GS这份报告最值得关注的判断是：Gucci Beauty的潜力空间，可能远超市场预期。\n\n欧莱雅已与科蒂达成协议，将Gucci授权协议的赎回日期从2028年提前至2027年7月1日。科蒂将获得约4亿美元的提前赎回补偿，其中2.5亿美元于2026年支付，最高1.5亿美元于2027年支付。欧莱雅承担约70%的提前赎回成本，外加一笔未披露的库存采购金额。这笔交易是2026年3月31日欧莱雅与开云美妆交易的延伸——当时欧莱雅收购了Creed品牌，并获得了葆蝶家、巴黎世家和Gucci的50年授权。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧莱雅有把时装品牌做成十亿美妆的完整方法\n\nYSL是欧莱雅最成功的案例。2008年欧莱雅与PPR（现开云集团）签订YSL长期整理版授权时，YSL美妆业务年销售额仅约3亿欧元。经过17年运营，YSL美妆已增长至超过30亿欧元，其中在授权第9年就突破了10亿欧元。如今YSL美妆的规模已超过其时装业务本身。\n\n阿玛尼美妆的规模约为时装业务的70%。华伦天奴和普拉达美妆的规模分别达到授权初期的15倍和3.5倍。欧莱雅奢侈品部门总裁已明确表示，结合Gucci的品牌地位与欧莱雅的运营能力，他们计划将Gucci打造成一个数十亿欧元的品牌。\n\n> **KC评论：** 欧莱雅这套方法的核心不是“做化妆品”，而是“把时装品牌的势能转化为美妆的规模”。YSL从3亿到30亿的路径，本质上是用香水、口红、粉底等高频消费品类，把一个奢侈品牌的认知资产变\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# Gucci美妆，欧莱雅的下一个十亿级品牌？\n\n## 下一个十亿级品牌\n\n欧莱雅正在为Gucci美妆布局\n\n最近有研究机构详细分析了欧莱雅获得Gucci美妆授权背后的逻辑，信息量较大，整理几个要点👇\n\n1️⃣ 提前赎回，加速整合\nGucci和Coty的授权协议从2028年提前到2027年7月到期。欧莱雅承担了约70%的提前赎回费用（约2.45亿欧元），加上额外库存支出。但欧莱雅资产负债表较为稳健（净债务/EBITDA仅0.7倍），这笔支出在可控范围内。\n\n2️⃣ 参考YSL的成长路径\n欧莱雅在奢侈品牌美妆领域有成功经验。YSL美妆从2008年的3亿欧元增长到超过30亿欧元，9年就突破10亿，目前美妆业务规模已超过成衣线。Armani美妆也达到成衣的70%，Valentino和Prada美妆分别翻了15倍和3.5倍。\n\n3️⃣ Gucci潜力有多大？\n研究估算Gucci美妆目前销售额约5亿欧元。欧莱雅奢侈品部门总裁明确表示，将凭借集团的运营能力把Gucci打造成数十亿欧元级别的大牌。参考YSL路径，Gucci美妆规模有望超过Gucci成衣本身。\n\n4️⃣ 对整体表现的拉动\nGucci授权预计每年为欧莱雅贡献约\n\n[... middle omitted ...]\n\n0-year licences for Bottega Veneta and Balenciaga with Gucci from 2028. The new agreement is subject to customary regulatory approvals.\n\nWhat potential does Gucci have? We look to L'Oréal's st\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R070",
    "title": "GS：Kakao盈利质量正在修复，比AI更确定的估值催化剂",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：Kakao盈利质量正在修复，比AI更确定的估值催化剂\n\n韩国互联网公司Kakao即将发布2026年第二季度业绩。市场关注的核心议题已经不是季度营收，而是其AI战略能否从路线图走向可验证的商业闭环。\n\nGS最新报告的核心判断是：Kakao的AI代理服务在2Q业绩前上线，时机已定，但读者不应只盯着发布本身。真正的变量在于，Kakao能否把KakaoTalk里的对话意图——搜索、预约、支付、购买——转化为高频可交易动作。这份报告的价值不在于预测季度数字，而在于它重新界定了Kakao AI的验证框架：从“有没有AI”转向“用户用不用AI做交易”。\n\n核心平台业务提供了稳定的盈利底座。Talk Biz广告收入预计同比增长20%，商务板块受3月购物节递延收入和5月家庭月促销支撑，增长约16%。支付和出行板块也保持两位数增速。但报告同时提醒，不要对利润率过于乐观——Piccoma的营销支出和门户业务AXZ从5月起并表剥离，会部分抵消季节性利好。\n\n> **KC评论：** GS给出的2Q26展望其实“中规中矩”，营收和营业利润基本与市场共识一致。真正值得细读的是报告后半段对AI验证框架的拆解——它把Kakao的AI故事从“概念驱动”切换到了“数据驱动”，这对理解公司未来6-12个月的定价逻辑很关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI代理服务的关键不是首发，而是能否形成“意图-行动-交易”闭环\n\nKakao的代理AI服务将连接垂直合作伙伴，在KakaoTalk内完成从对话到行动的全流程。GS明确表示，真正重要的不是发布本身，而是后续能否看到：重复使用率上升、合作伙伴数量扩大、交易完成率改善、用户参与度提升。\n\n报告提出了一个层层递进的验证链条。第一层是用户是否在KakaoTalk内完成更多任务——搜索、\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nKakao的AI布局即将展开\n\n📌 KakaoAI来了，这次值得关注\n\n📌 核心平台支撑，AI发展路径逐渐清晰\n\n---\n\nKakao的第二季度业绩即将公布，但市场更关注的，是即将上线的AI产品。\n\n1️⃣ 核心平台表现稳健\n\n第二季度Talk Biz广告预计同比增长约20%，Commerce受3月购物节和5月家庭月带动，Pay和Mobility也保持增长。不过利润率方面需留意——Piccoma的营销投入较大，加上5月Portal业务因AXZ交易出表，收入可能受到一定影响。\n\n整体来看，第二季度收入预计约2万亿韩元（同比+6%），营业利润约2140亿韩元（同比+5%），与市场预期基本一致。\n\n2️⃣ AI是值得关注的变量\n\nKakao计划在第二季度业绩发布前推出agentic AI服务，旨在连接KakaoTalk中的对话意图与合作方服务。关键问题不在于“是否有路线图”，而在于“能否落地”。\n\n更值得关注的是：用户是否会持续使用、合作方是否会扩展、交易完成率如何。这些指标比产品发布会本身更能验证AI的商业化可行性。\n\n3️⃣ 长期逻辑：从“连接”到“交易”\n\n要验证AI的商业价值，需要观察几个信号：用户是否直接\n\n[... middle omitted ...]\n\nthe mechanical Portal Biz impact from AXZ deconsolidation.\n\nThe key near-term debate remains AI. Kakao's agentic AI service connection with vertical partners is still expected to launch before\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R071",
    "title": "GS：GS调研，强生口服新药Icotyde峰值收入或超100亿美元",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：GS调研，强生口服新药Icotyde峰值收入或超100亿美元\n\n强生新上市的口服银屑病药物Icotyde，正在成为市场重新评估这家医疗健康巨头增长潜力的关键变量。GS最新发布的KOL（关键意见领袖）调研报告给出了一个值得关注的信号：如果这款口服IL-23药物达到医生预期的市场份额，其峰值收入可能超过100亿美元，远高于目前市场共识的71亿美元。\n\n这一判断来自GS对26名皮肤科医生的专项调查。这些医生每人至少治疗100名中重度银屑病患者，并在过去一年中开具过多种品牌全身性治疗药物。调研的核心发现是：医生们预计Icotyde在中重度银屑病患者中的处方比例将从目前的2-3%，在一年内升至8-10%，五年后达到15-20%。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 口服药正在改写银屑病治疗格局\n\nIL-23抑制剂一直是银屑病治疗的重磅武器，但此前均为注射剂型。强生的Tremfya和艾伯维的Skyrizi在这一领域占据主导地位。Icotyde作为首个口服IL-23药物，其最大优势在于给药便利性——患者无需注射，也无需频繁就医。\n\nGS调研显示，医生对Icotyde的定位非常清晰：它主要服务于两类人群——从未使用过品牌全身性治疗的新患者，以及从其他口服品牌（如安进的Otezla和百时美施贵宝的Sotyktu）转换而来的患者。对于已经在使用注射类IL-23或IL-17药物的患者，医生并不倾向于让他们转换。这意味着Icotyde正在扩大整个银屑病治疗市场，而非蚕食现有注射药物的份额。\n\n> **KC评论：** 这个判断对行业竞争格局有重要含义。如果Icotyde确实是在做大市场蛋糕而非抢份额，那么Tremfya和Skyrizi面临的直接冲击可能小于市场此前担忧。但值得关注的是，强生同时拥有Tremfya和Ico\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n口服银屑病新药，医生怎么看？\n\n**Icotyde 真实反馈**\n\n26位皮肤科医生的调研结果\n\n最近看到一份关于强生口服银屑病新药Icotyde的医生调研，信息量挺大。这款药今年3月刚获批，被公司视为未来十年营收双位数增长的关键方向。来看看一线医生怎么说👇\n\n**1/ 处方量正在逐步增加**\n- 目前医生开给中重度患者的比例约2-3%\n- 预计1年内升至8-10%，5年内达到15-20%\n- 有医生预期5年后用到29%——说明市场空间可能比想象中大\n\n**2/ 它主要影响哪些现有选择？**\n- 主要吸引两类患者：**初次使用品牌系统治疗**的人，以及**从其他口服药（如Otezla/Sotyktu）转过来**的人\n- 不太会抢注射类IL-23药物（如Skyrizi、Tremfya）的份额——注射剂仍是约50%新患者的首选\n- 强生自己也说，Icotyde是来**扩大市场**的，不是内卷\n\n**3/ 医生开药看什么？**\n- 疗效和口服便利性是核心\n- 需要空腹服用这一点，目前没成为障碍\n\n**4/ 如果真达到15-20%市占率**\n- 峰值收入可能超过100亿美元（投行自己估77亿，市场共识71亿）\n- 未\n\n[... middle omitted ...]\n\n the 1Q26 earnings call in mid-April, JNJ highlighted positive early launch indicators, noting 1,500 patients with prescriptions had been written with over 1,000 unique prescribers; subsequent\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R072",
    "title": "GS：特朗普撕毁停火协议后，原油供应恢复的真正瓶颈",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：特朗普撕毁停火协议后，原油供应恢复的真正瓶颈\n\n布伦特原油期货价格本周三回升至每桶80美元附近。触发因素是特朗普总统宣布与伊朗的停火协议破裂，此前霍尔木兹海峡发生了新的袭击事件。两艘油轮和一艘LNG船在阿曼海岸附近遭无人机击中，美国随即撤销对伊朗石油的制裁豁免，并对伊朗发动空袭。伊朗的报复打击了巴林和科威特，美方则在周三晚进行了新一轮打击。\n\n这份GS最新发布的石油追踪报告，核心判断并非短期价格波动，而是指向一个更关键的变量：**霍尔木兹海峡石油流量的恢复，瓶颈不在于有多少空油轮可以装货，而在于伊朗是否愿意放行。**\n\n报告显示，波斯湾的石油出口流量在停火协议签署后的头10天内，一度恢复到战前水平的80%以上，积压的油轮蜂拥而出。但好景不长。随着近期油轮遇袭，7日移动平均流量已回落至正常水平的71%左右，大约每天1600-1700万桶。通过海峡本身的流量更是从协议后的每天1000万桶，降到了最近的830万桶。\n\nGS的分析师指出，一个关键证据是：**目前海峡附近空油轮的运载能力高达9.26亿桶，波斯湾内部的空油轮容量比已装载的油轮容量高出50%以上。** 换句话说，运力不是问题。船只不敢走、或者走了也未必安全，才是核心。\n\n> **KC观察：** 这组数据点出了市场定价的一个微妙之处。很多人认为只要停火，供应就能迅速恢复。但报告明确指出，伊朗的配合意愿才是真正的开关。只要海峡的“安全感”没有建立，即使油轮排成长队，流量也无法恢复到正常水平。这意味着需要密切关注的不只是停火协议的新闻，更是实际通过海峡的油轮数。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 伊朗制裁豁免的取消，将重新压制刚刚抬头的进口\n\n报告中的另一条线索值得留意。美国撤销对伊朗石油的制裁豁免，意味着此前刚刚开始回升的伊朗石油进口将再次承\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n霍尔木兹海峡近期出现新情况\n\n供需两端均有所变化\n\n油轮在两天内接连遇袭，美军与伊朗之间发生互相打击，海峡通行风险有所上升。\n\n1️⃣ 波斯湾出口量降至正常水平的71%\n- 霍尔木兹油运恢复后一度达到83%，但袭击事件发生后迅速回落\n- 目前日流量约1670万桶，比正常水平少近600万桶\n\n2️⃣ 伊朗意愿是恢复的关键因素\n- 海峡内有大量空油轮，运力较为充足\n- 美国取消伊朗石油制裁豁免后，伊朗油进口刚有回暖又面临调整\n\n3️⃣ 俄罗斯炼厂受到较大影响\n- 炼厂停产规模达380万桶/日，超过一半产能处于离线状态\n- 柴油出口同比减少60万桶/日，欧洲柴油利润升至60美元/桶\n- 俄罗斯汽油柴油零售价两个月内上涨超10%，多地出现供应紧张\n\n4️⃣ 库存短暂回补后再次下降\n- 全球可见库存6月中旬见底，前3周快速回补\n- 但最近一周又减少650万桶/日，成品油在途量下降\n\n供需两端均有所收紧：中东供给恢复受阻，俄罗斯炼厂减产推高成品利润。接下来60天的谈判窗口值得关注。\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.md]\n# Oil Tracker: Negative S\n\n[... middle omitted ...]\n\nducted additional strikes against Iran Wednesday night.\n\n☐ The recent attacks on tankers highlight still elevated risks of crossing, and shippers may hesitate to cross under the currently uncl\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R073",
    "title": "GS：微软三大关注点被市场充分定价，资本开支与AI发展进入新阶段",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：微软三大关注点被市场充分定价，资本开支与AI发展进入新阶段\n\n当一家市值近3万亿美元的公司，在财报前一个月里跑输纳斯达克10个百分点，市场在关注什么？GS这份覆盖微软4QFY财报预览的报告，给出了三个明确答案：资本开支持续上行、对英伟达的依赖、以及Copilot的商业化进展。但报告的核心判断是——这些关注点已经被充分定价，而基本面正在改善。\n\n这份报告发布于7月7日，距离微软7月29日财报约三周。GS认为，当前报价与基本面之间存在一个值得关注的缺口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本开支不是问题，问题是市场如何理解微软的“内部算力分配”\n\n市场对微软资本开支的关注，很大程度上来自一个误读：认为资本开支高企就等同于Azure增长仍在调整。GS的数据显示，微软在2QFY曾明确表示，如果将所有增量GPU容量全部投向Azure，后者增速本可超过40%（GS估算约44%）。但微软选择将部分算力分配给第一方应用（Copilot）和内部研发（MAI）。\n\n这意味着，Azure当前的增长速度并非能力上限，而是战略选择的结果。随着过去两年研究逐步落地，内部算力占比正在接近稳态。GS预计4QFY Azure增速可达40-41%（按固定汇率），高于公司指引的39-40%，且下季度指引同样乐观。\n\n> **KC评论：** 这里的关键不是Azure增速本身，而是“内部算力分配比例”这个变量。如果微软能在财报电话会上给出更清晰的分配逻辑，市场对资本开支的焦虑会明显缓解。报告中有详细的计算框架，值得细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 英伟达依赖不是死穴，但微软的芯片策略需要更多证据\n\n报告坦率承认，微软的芯片策略确实落后于部分竞争对手。Maia芯片的成\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# Azure增速加快，但微软面临三个观察点\n\n📊 微软近期观察\n\n最近有机构发布了微软的研究笔记，简单梳理一下逻辑👇\n\n**1/ 核心看点：Azure增速持续提升**\n- 4QFY预期Azure增速40-41%（此前指引39-40%）\n- 1QFY预期继续40-41%，略低于市场预期的41%\n- 关键：供应仍受限，但新产能（如威斯康星Fairwater数据中心）陆续上线\n\n**2/ 三个值得关注的方面**\n自4月财报后，微软报价有所调整，同期纳指表现不同，主要关注：\n① 资本开支预期不断上调，Azure增速却只小幅上修\n② 对特定供应商依赖度较高，相关成本变化值得留意\n③ Copilot用户反馈分化，新同类产品（如Claude Cowork）可能影响Office 365\n\n**3/ 资本开支仍在增加**\n- 研报将FY28-30资本开支上调约10%，预计FY28达3190亿美元（含融资租赁）\n- 微软约13%的CY26资本开支与组件涨价相关，其中超50%来自内存\n- 内部芯片（Maia）进展慢于同业，短期内仍高度依赖外部供应商\n\n**4/ Copilot数据在改善**\n- 3QFY付费席位超2000万，AI\n\n[... middle omitted ...]\n\nnternal silicon offerings; and 3) the potential for Microsoft's knowledge worker applications business (Office 365) to be disintermediated with new AI competition, such as Claude Cowork, fuele\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R074",
    "title": "GS：户外广告正在经历一场被低估的结构性修复",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：户外广告正在经历一场被低估的结构性修复\n\n户外广告（OOH）可能是传统媒体中最容易被忽视的“幸存者”。当数字广告持续蚕食预算时，户外广告的份额并未崩塌，反而在2026年迎来一轮明显的增长加速。GS最新研报的核心判断是：这轮增长不只是基数效应和体育赛事带来的脉冲，行业竞争格局的理性化、数字化库存的成熟以及并购活跃度的提升，正在共同推动一个可持续的中个位数增长阶段。\n\n报告将德高集团（JCDecaux）和Stroeer列为重点关注对象，预计两者2026年户外广告有机收入增速分别达到4.6%和5.6%，显著高于2025年的1.8%。这一判断建立在三个可验证的支柱之上：结构性需求韧性、竞争环境的改善，以及中东等区域不确定性的边际缓和。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 户外广告是传统媒体中最抗数字侵蚀的品类，这一逻辑正在被强化\n\n过去十年，几乎所有传统媒体都在数字化的冲击下丢失份额。但户外广告是个例外。GS引用的WPP数据显示，2013年至2025年间，户外广告的市场份额不仅没有下降，反而在多数周期中保持稳定甚至微升。核心原因在于其高回报表现率和广告主投放的灵活性——尤其是在数字化户外（DOOH）改造后，程序化购买和精准受众测量大幅提升了单位库存的价值。\n\n这并非新故事，但关键在于2026年的加速背景。2025年由于基数效应（前一年有欧洲杯和奥运会）增速偏低，而2026年有世界杯等大型赛事叠加，同时宏观环境并未显著出现变化。GS认为，户外广告与全球实际GDP增长之间存在0.78的R平方相关性，这意味着只要宏观环境不出现大幅下滑，中个位数的行业增速是合理的。\n\n> **KC评论：** 这份报告的核心贡献不是“户外广告会增长”，而是给出了一个可检验的框架：增长由数字化渗透率、程序化交易占比和体育赛事日历\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n户外广告的行业观察，值得一看\n\n户外广告，结构性机会\n\n2026年户外广告增速有望回到中个位数\n\n某外资研究机构最新报告显示，户外广告可能正在迎来一轮结构性变化。\n\n2026年，两大户外广告龙头的有机收入增速预计将从2025年的+1.8%加速至+4.6%/+5.6%。背后的逻辑很清晰：基数变友好，叠加大型体育赛事（比如世界杯）拉动。\n\n为什么户外广告能扛住数字冲击？\n\n1️⃣ 高回报，给广告主灵活度\n在传统媒体中，户外广告是份额流失最少的。数字化改造后，程序化购买+精准受众测量，让千人成本反而能提升。\n\n2️⃣ 竞争环境变理性\n过去几年估值压缩，玩家们更关注利润，而不是烧钱抢份额。最近行业并购活跃，比如几家私募对户外广告资产出价，说明资本也在重新评估这个领域。\n\n3️⃣ 龙头优势在巩固\n全球市场非常分散，龙头市占率约8%，第二名不到5%。新签合同的分成比例可能更有利，这对龙头是额外收益。\n\n⚠️ 也有一些需要留意的点：\n- 中东地缘政治不确定性（约占某龙头5%收入）\n- 部分地区（如德国）宏观偏弱\n- 谷歌、Meta等数字平台仍在抢广告预算，户外玩家必须持续投入技术\n\n整体看，报告认为户外广告的结构性驱动力还\n\n[... middle omitted ...]\n\nfers to advertisers.\n\nWe also believe that the overall competitive environment has improved, becoming more rational over the past few years, with an increased focus on profitability as valuati\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R075",
    "title": "GS：美联储纪要揭示双向准备，降息或加息都看通胀速度",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：美联储纪要揭示双向准备，降息或加息都看通胀速度\n\n6月FOMC会议纪要释放了一个清晰的信号：美联储内部并非铁板一块，决策路径高度取决于通胀的演变方向。这份由Jan Hatzius团队出具的报告，其核心判断并非“美联储将降息”或“美联储将加息”，而是“几乎所有”参与者都同意——如果通胀“很快”消散，他们支持维持或降低利率；如果通胀持续高企，则支持进一步收紧。这种“双向准备”的状态，才是当前宏观环境最值得关注的变量。\n\n报告没有给出一个确定的路径，而是揭示了美联储决策框架的脆弱性——它完全押注于一个无法精确预测的变量：通胀何时、以何种方式回归2%。对于市场参与者而言，这意味着不再有单一的“美联储叙事”可以押注，而是需要同时为两种场景做好准备。\n\n> **KC评论：** GS这份会议纪要解读的精髓，在于它把美联储的“观望”状态拆解成了两个具体场景。读者最该关注的不是“降不降息”，而是报告里描述的“almost all”这个措辞——这代表内部高度一致，一旦通胀数据出现方向性变化，政策转向的速度可能比市场预期的更快。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 通胀路径决定政策路径，但“时间”才是关键变量\n\n报告明确指出，美联储内部存在两种主流场景讨论。第一种是通胀不确定性消散、通胀“很快”开始回归2%——在这种情况下，“几乎所有”参与者都认为维持或最终降低利率是合适的。第二种是通胀因AI相关需求、中东冲突或关税而持续高企——此时“几乎所有”参与者都认为需要“一些政策收紧”。\n\n这里的关键词是“soon”。美联储的决策不是基于通胀的相对水平，而是基于通胀回归2%的“速度”。如果通胀下降的速度符合预期，降息的大门是敞开的；如果下降速度慢于预期，加息的不确定性就会上升。GS自己的预测也印证了这一点——他们预计核心PCE通胀\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n美联储6月会议：政策路径取决于通胀变化\n\n**政策方向如何？通胀数据是关键**\n\n美联储6月会议纪要显示，与会官员对下一步行动存在不同看法，核心取决于通胀能否“较快”出现变化。\n\n1. **6月维持不变，但部分官员考虑调整**\n   - 所有与会者均支持维持当前利率\n   - 但“少数”官员认为6月有理由采取更紧的措施\n\n2. **政策走向取决于通胀表现**\n   - 如果通胀“较快”开始回落→“几乎所有”官员认为可以维持或最终调整方向\n   - 如果通胀持续处于较高水平（受AI需求、地缘因素、关税影响）→“几乎所有”官员认为需要“进一步收紧”\n\n3. **通胀压力仍较广泛**\n   - 通胀“进一步上升且远高于2%目标”\n   - 价格压力已扩散到交通、航空、化工、农产品等领域\n   - 服务业（除住房）通胀仍然较高\n   - AI相关投资带来的增长潜力可能增加通胀的持续性\n\n4. **劳动力市场稳定，消费结构分化**\n   - 劳动力市场“不是当前通胀来源”\n   - 经济活动“稳健”，AI投资是主要驱动力\n   - 消费主要靠高收入群体，得益于公司报价上涨和退税\n\n5. **未来展望**\n   - 美联\n\n[... middle omitted ...]\n\nfirming” in such cases. We expect year-over-year core PCE inflation to slow to 3.0% by December 2026 (vs. 3.4% currently), partially reflecting the effects of methodological changes announced \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R076",
    "title": "GS：西门子医疗真正问题不在估值，在诊断业务修复路径",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：西门子医疗真正问题不在估值，在诊断业务修复路径\n\n这份由GS欧洲MedTech分析师Richard Felton签发的研报，核心判断并不复杂：西门子医疗Q3业绩大概率与预期基本持平，但真正值得关注的不是季度波动，而是FY27的盈利预期存在结构性下修不确定性。问题出在诊断业务。\n\n，隐含约19%的上行空间，评级更新公司观点。但仔细读下来，这个中性背后藏着一条关键线索——市场对诊断业务FY27的反弹幅度可能过于乐观，而这一点恰恰是决定公司能否走出估值僵局的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 诊断业务是中国政策不确定性的集中暴露面\n\n报告最值得关注的不是Q3数字本身，而是GS对中国诊断市场的判断。分析师在3月中国实地调研后，明确指出了两重政策仍在调整：凝血项目的集采(VBP)和IVD统一定价/服务收费指南的实施。这两项政策并非新消息，但GS认为市场对它们的影响程度和持续时间可能存在误判。\n\n具体到数字层面，GS对FY27调整后EPS的预测比市场共识低4%，主要影响项就是诊断。报告指出，市场共识假设诊断业务FY27的EBIT同比增长73%，这个数字占集团整体EBIT增长的约20%。如果诊断的修复路径被政策因素拉长，整个FY27的盈利故事就需要重新校准。\n\n> **KC评论：** 73%的同比EBIT增长预期，意味着市场在定价一个相当陡峭的V型反弹。GS的谨慎态度提醒我们：政策对医疗器械行业的冲击，往往不是一次性出清，而是渐进式、多轮次的。完整报告里对中国诊断业务的细分假设和敏感性分析，值得仔细对比。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 分拆传闻是催化剂，但时间窗口在两年后\n\n近期媒体关于西门子医疗可能剥离诊断业务的报道，是GS报告里少数带\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n西门子医疗Q3：诊断业务观察\n\n诊断业务存在变数\n\n刚读完某外资机构对西门子医疗的最新研究，分享几个核心判断👇\n\n**1/ Q3业绩预期：收入略低于共识**\n预计Q3有机增长4.1%（共识4.8%），收入€57.83亿（低于共识1%）。各板块均低于市场预期：影像+5%、诊断-3%、精准治疗+7%。\n\n**2/ 利润率变化是关注点**\n受汇率和成本因素影响，调整后EBIT利润率预计15.6%，同比降130个基点。所有板块利润率同比都在调整，尤其诊断板块利润率仅3%（同比降超600bps），中国相关政策是主要因素。\n\n**3/ FY27风险来自诊断业务**\n市场对FY27诊断业务盈利反弹较为乐观（共识预期EBIT同比增长73%），但中国统一采购和集采政策持续影响，研报认为恢复速度会更慢。\n\n**4/ 诊断分拆是长期变量**\n近期媒体报道可能在24个月内分拆诊断业务，估值约€60亿。分拆后集团整体增长率和利润率将有所变化（诊断是低增长、低利润业务），现金收入可加速降杠杆。\n\n**5/ 估值有空间但缺乏催化剂**\n自2021年12月以来未见实质性盈利上修，目前交易在14.5倍远期PE和11.1倍EV/EBITDA。目\n\n[... middle omitted ...]\n\nis €899m (broadly in line with consensus).\n\nWe continue to see modest downside risk to consensus expectations in FY27 due to Diagnostics. Given this risk of further policy headwinds (Unified p\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R077",
    "title": "GS：ServiceNow推100天ROI保证，AI用例从概念走向量化",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：ServiceNow推100天ROI保证，AI用例从概念走向量化\n\n企业软件市场正在经历一个微妙的信任重建期。当一家公司连续完成多笔数十亿美元的并购，市场最关心的不是整合进度，而是它的核心业务到底稳不稳。\n\nGS在ServiceNow 7月22日二季报发布前更新了判断。报告的核心逻辑很清晰：ServiceNow的重新定价，取决于它能否向市场证明自己在企业AI堆栈中的不可或缺性。这不是一个关于短期业绩的问题，而是关于增长算法的可信度。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季报的预期差，藏在指引的保守里\n\nServiceNow对二季度的指引本身已经包含了足够的审慎。有机cRPO增速指引约为17.25%，相比一季度的约20%明显节奏变化。中东地缘政治因素导致的上季度部分本地部署交易推迟，让管理层在指引中额外留出了缓冲空间。\n\n但GS认为，这个低基数恰恰创造了超预期的空间。报告预计二季度cRPO增速有望达到20.5%至21.5%，订阅收入增速为22%至22.5%。如果兑现，这将分别超出指引约150个基点和100个基点，与公司过去三年的平均超预期幅度基本吻合。\n\n真正需要关注的不只是二季度数据本身，而是三季度cRPO指引会如何揭示增长减速的节奏。在并购贡献已被充分预期的情况下，有机增长的稳定性才是市场定价的锚点。\n\n> **KC评论：** GS对二季报超预期的判断，建立在管理层主动压低指引的基础上。但真正值得跟踪的是三季度指引——它才是判断有机增长是否触底的关键信号。完整报告中对cRPO覆盖率的图表值得细看。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 并购不是从弱势出发，但市场需要看到核心业务企稳\n\n市场对ServiceNow连续收购Moveworks\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nServiceNow的AI应用进展，这次有了一些观察信号\n\nAI技术能否在企业场景中真正落地？\n\n某外资研究机构在2Q26业绩发布前更新了观点。核心逻辑：ServiceNow的市场价值重估，取决于它能否证明自己在企业AI技术体系中的位置。\n\n**1/ 这次业绩窗口，比上一季更值得关注**\n\n- 2Q指引偏保守：cRPO增速指引约17.25%（有机口径），相比1Q实际值20%明显放缓。中东地缘波动后，管理层主动加了一层谨慎。\n- 但催化剂也在：Knowledge大会上推出了ITSM Level 1自动化用例，附带100天ROI保证。这是对系统集成商“不知道推什么用例”的回应。\n- 标杆客户已落地：NVIDIA、FedEx、CVS Health。\n\n**2/ 收购整合进入第二阶段**\n\n- Moveworks（+100bps）、Armis（+125bps）开始贡献增量。\n- 另外收了ai.work——做跨企业应用的自主AI代理，金额不大（千万级），但补齐了“从用户请求到执行”的闭环。\n- 研究报告观点：这波收购不是从弱势出发，而是在技术格局变动期，用“自研+并购”平衡布局。\n\n**3/ 核心关注：有机增长何时企稳\n\n[... middle omitted ...]\n\nessing feedback we had heard from system integrators around being uncertain of which use cases to lead with and establishing customer use cases with NVIDIA, FedEx, and CVS Health; c) ServiceNo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R078",
    "title": "GS：中国PCB外迁的真相，不是成本战，而是溢价能力",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：中国PCB外迁的真相，不是成本战，而是溢价能力\n\n当市场还在争论中国PCB产业外迁是否会侵蚀利润时，GS在7月实地调研后给出了一个反直觉的判断：成本不是决定项，客户支付意愿才是。这份针对沪电股份泰国工厂的调研报告，核心信号只有一个——产能分散化正在从防御性策略转向溢价能力证明。\n\n为什么这个判断值得关注？因为过去两年，几乎所有中国电子制造企业的海外扩产都被市场解读为“被动应对关税”。GS的调研结论却表明，头部PCB厂商的泰国产能正在获得客户主动溢价。如果这个逻辑成立，那么市场对相关公司海外业务的估值方式可能需要修正。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 泰国生产成本比国内高10-20%，但客户愿意承担\n\nGS团队实地走访了沪电股份位于大城府的三个厂区。目前A1厂已量产，A2厂在建，预计2026年三季度投产。公司给出的信息很直接：泰国生产成本比国内高出10-20%，主要原因是覆铜板等原材料从国内进口需缴纳超过10%的关税。尽管泰国当地劳动力成本更低，但生产效率仍低于国内工人。\n\n关键转折在于客户反应。管理层明确表示，即使成本高出20%，客户也愿意支付。这背后有两个支撑：一是全球科技巨头对供应链多元化的刚性需求，二是沪电股份在AI PCB领域的技术卡位——A1厂约20%产值来自汽车PCB，其余大部分产能正用于AI PCB的客户认证。\n\n> **KC评论：** 成本溢价能否转嫁给客户，是海外扩产估值逻辑的分水岭。如果客户不买单，海外产能就是利润影响；如果客户愿意溢价，海外产能就是竞争壁垒。GS调研给出了后者的初步证据，但完整报告里关于客户认证进度和具体溢价幅度的细节，才是判断这一逻辑可持续性的关键。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 中期毛利\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n泰国工厂探访：PCB产能布局观察\n\n产能外迁，但客户愿意配合\n\n某研究机构近期去了Victory Giant泰国工厂，分享几个关键发现👇\n\n1️⃣ 泰国三座工厂规划清晰\n- A1已量产，A2在建（目标26Q3量产）\n- A1产值≈2025年营收的26%\n- A2/A3单厂产值是A1的1.4-2倍\n\n2️⃣ 产品结构在升级\n- A1约20%产值来自汽车PCB\n- 剩余80%准备做AI PCB（正在客户认证）\n\n3️⃣ 成本高了，但客户接受\n- 泰国制造成本比国内高10-20%\n- 主要因为原材料（如CCL）从国内进口，关税10%+\n- 但客户愿意承担这部分溢价\n- 公司目标：中期通过自动化+本地供应链，毛利率追平国内\n\n4️⃣ 人员结构\n- 1400+员工，50%本地人\n- 25%缅甸劳工，25%国内派驻\n\n核心逻辑：AI PCB规格升级+全球客户扩张，产能跟着客户需求走。\n\n研报预测25-28年营收从193亿→880亿，EPS从5→27.6元，估值26.3x PE。\n\n你觉得东南亚产能转移是长期趋势，还是短期关税规避？欢迎一起讨论～\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mine\n\n[... middle omitted ...]\n\nhe company to better support demand from global-tier clients. We remain positive on Victory Giant's growth ahead, riding the trend of AI infrastructure ramp-up, AI PCB specification upgrades w\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R079",
    "title": "GS：美国宏观韧性超预期，GS，资金条件收紧有限",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：美国宏观韧性超预期，GS，资金条件收紧有限\n\n当市场还在为美联储降息节奏反复争论时，GS最新发布的宏观环境指标更新给出了一个更稳定的画面。这份由Jan Hatzius团队更新的高频数据包显示，美国宏观环境当前处于一种“温和但未过热”的状态，核心指标既没有指向调整，也没有暗示重新加速。\n\n报告最值得关注的不是单一数据，而是这些指标组合在一起传达的信号：美国宏观环境的韧性比市场定价所反映的更强，但通胀不确定性也在有序回落。这种组合意味着，美联储不需要急于行动，也不需要被迫暂停。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资金条件收紧的幅度有限，市场定价与基本面之间仍有距离\n\nGS的资金条件指数在过去一周名义上收紧了2.3个基点，主要来自10年期国债回报表现的上升。但值得注意的是，实际资金条件指数仅收紧1.2个基点，到98.17。这个差值本身就是一个信号：市场对利率的敏感度正在下降，或者说，宏观环境对利率的承受力在增强。\n\n从历史经验看，当资金条件收紧到一定程度时，宏观环境动能会明显受损。但当前的水平距离那个临界点还有距离。GS对二季度GDP的预测维持在2.2%（季环比年化），这个数字既不惊艳，也不令人担忧，恰好落在“软着陆”的叙事框架内。\n\n> **KC评论：** 资金条件指数是观察政策传导效率的关键工具。GS的这个数据告诉我们，即使长端利率上行，对实体宏观环境的抑制效果可能被企业盈利韧性部分抵消。读者如果关注利率敏感型资产，可以重点看报告里的实际FCI走势图，它比名义值更能反映真实约束。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 宏观环境活动指标稳定，但惊喜指数暗示边际动能正在减弱\n\nGS6月的当前活动指标为+2.6%，与5月持平。这个数字本身并不意外\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n美国经济冷热不均？最新指标拆解\n\n📊 美国经济最新温度计\n\n最近某外资机构更新了一组美国经济跟踪指标，信息量挺大，简单拆几个核心看点👇\n\n1️⃣ 金融条件边际收紧\n名义金融条件指数上周收紧2.3bp至98.45，主因10年期美债回报表现走高。实际指数也小幅收紧1.2bp至98.17——融资成本在悄悄上升。\n\n2️⃣ 增长预期不差\nQ2 GDP预测仍维持在+2.2%（季调年化），经济扩张的底子还在。6月当前活动指标录得+2.6%，与5月持平，说明增长动能没有明显下滑。\n\n3️⃣ 经济意外指数转正\n美国MAP经济意外指数净值为+0.1，意味着近期数据整体略好于预期。但幅度很小，属于“刚刚好”的水平。\n\n4️⃣ 通胀与薪资跟踪\n核心通胀指标和薪资增速都在观察窗口内，暂时没有看到加速迹象。制造业与服务业调查也偏平稳，未出现剧烈波动。\n\n📌 整体感觉：美国经济处在“不冷不热”的微妙区间——增长有韧性，金融条件在收紧，但尚未对需求产生明显影响。\n\n欢迎一起讨论你对美国经济后续走势的看法🧐\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.md]\n## USA: GS Economic In\n\n[... middle omitted ...]\n\n![](images/b9a3f287eb81333db0d5ed9b1666cb917f1789c1738dfe87d9355f3cd77c22a7.jpg)\n\n![](images/2a46e744bb66bac5eac9643f98e2bbb2ef15f533cf90c2d892dcc5a53c1198af.jpg)  \nSource: GS Global Investm\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R080",
    "title": "GS：GS拆解迪士尼奥兰多，客流下降2%，消费却创历史新高",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "GS",
    "digest": "[wechat_article.md]\n# GS：GS拆解迪士尼奥兰多，客流下降2%，消费却创历史新高\n\n奥兰多机场5月客流同比下降2%，但当地酒店税收入却创下同期新高。这两个看似矛盾的数据，恰好勾勒出迪士尼主题公园业务当前的真实处境——国内客流在正常化，但国际游客正在补位，且游客的消费意愿并未减弱。\n\nGS最新一期奥兰多旅游市场追踪报告，通过两个高频指标拆解了迪士尼（DIS）的季度内需求变化。数据来自奥兰多国际机场（MCO）的乘客量和奥兰治县的旅游发展税（TDT）收入。前者反映客流规模，后者反映实际消费金额。\n\n5月MCO总客流同比下降2%，较4月的+3%明显节奏变化。影响主要来自国内旅客，同比下滑3%。但国际旅客增长了2%，且已连续两个月实现正增长。GS指出，这符合迪士尼管理层此前的判断——国际客流已度过疫后恢复的重叠期，不再呈现进一步出现变化的迹象。\n\n与此同时，奥兰治县5月TDT收入同比增长9%至3280万美元，尽管增速较4月的+14%有所节奏变化，但仍是历史同期最高水平，且已连续14个月保持增长。\n\n> **KC评论：** 客流下降但消费额创新高，说明游客结构或消费行为正在发生变化。完整报告中对国内与国际客流的分拆数据，以及TDT收入的月度趋势图，值得仔细对比。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内客流仍在调整不等于需求转弱，结构变化才是关键\n\n5月国内到达旅客同比下降3%，与4月+4%的增速形成明显反差。但这一变化需要放在更长的时间轴上看。2025年同期基数较高（国内客流在2025年4-5月已开始回升），同时5月本身是季节性过渡月份，波动本身并不罕见。\n\n真正值得关注的是国际客流的恢复节奏。在经历了连续三个月的相对疲软后，国际客流在4月和5月连续录得同比增长。GS认为，这意味着迪士尼国际游客的疫后恢复期已基本完成，不再构成进一\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n奥兰多五月客流微降，但酒店税创纪录\n\n奥兰多旅游数据解析\n\n🌴 迪士尼的奥兰多晴雨表\n\n最近某机构更新了奥兰多旅游数据，与迪士尼和环球影城的季度需求相关。拆开看几个关键点：\n\n1️⃣ 机场客流变化\n- 5月奥兰多机场到达客流同比下降2%\n- 相比4月+3%的增速有所变化\n- 国内客流下降3%，国际客流增长2%\n- 国际客流已连续两个月正增长，说明海外游客正在回归\n\n2️⃣ 酒店税收入创纪录\n- 5月旅游发展税同比增长9%至3280万美元\n- 虽然增速比4月的14%有所变化，但这是历史上较强的5月数据\n- 已连续14个月保持增长\n\n3️⃣ 季度趋势\n- 截至目前的二季度机场客流同比+1%\n- 机构估计迪士尼二季度国内乐园客流增长也约+1%\n- 两者高度吻合\n\n📌 我的观察：国内客流微降可能是高基数效应，国际游客恢复是亮点。酒店税创纪录说明游客消费意愿不弱，整体需求仍有支撑。\n\n#学习笔记 #研究笔记 #学习研究 #研报解读\n\n[source_mineru.md]\n# Walt Disney Co. (DIS)\n\n# Orlando airport arrivals in May decrease $2 \\%$ \n\n[... middle omitted ...]\n\noller's office).\n\nKey takeaways from our analysis include:\n\n\\- Orange County's Tourist Development Tax (TDT) collections rose 9% yoy to \\$32.8 mn in May 2026, a moderation from the +14% yoy pa\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R081",
    "title": "JPM：机构盈利超预期，但市场为何不买账？",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：机构盈利超预期，但市场为何不买账？\n\n这份JPM研报的核心判断，既不是单纯看多招商标的，也不是对二季度业绩的超预期感到意外。它真正想回答的问题是：当业绩预告连续超预期，板块报价却在下跌，市场到底在担心什么？以及，这种担心是否过度了？\n\n报告以招商标的H股为引子，但讨论的其实是整个中国机构板块的定价逻辑。二季度净利润同比大增160%-198%，创历史新高，但市场反应冷淡——A/H机构股在国泰海通业绩预告后反而平均下跌3%。这组反差，比业绩本身更值得琢磨。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 业绩超预期不是新闻，市场对“质量”的质疑才是\n\n报告指出，招商标的上半年净利润已达全年市场一致预期的67%-74%。仅从数字看，这是明确的超预期信号。但市场没有庆祝，原因有两个。\n\n第一，读者在获利了结。机构股自5月中旬以来已有明显涨幅，招商标的A/H股分别上涨28%和23%，显著跑赢板块。利好兑现后，部分资金选择离场。\n\n第二，也是更关键的，市场对盈利质量存疑。有人担心二季度业绩过度依赖回报表现，而7月以来沪深300和科创50指数分别下跌4%和9%，如果市场热度消退，三季度的经营表现可能软化。换句话说，市场在问：这轮高增长，到底有多少来自可持续的经纪、国际机构、资本中介业务，多少来自不可重复的回报表现？\n\n> **KC评论：** 这个问题其实适用于所有强周期板块——当业绩创历史新高时，市场反而开始问“然后呢”。这份报告的价值不在于确认业绩好，而在于它提供了一个框架：如何判断超预期业绩是拐点还是顶点。报告里对招商标的回报表现的拆分，以及CXMT上市带来的潜在重估，是值得仔细看的细节。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 报告认为回调是机会，但理由并非“\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n券商二季报表现较好，但市场反应平淡？\n\n二季报数据亮眼，但市场关注点在哪？\n\n行业观察笔记：某券商二季报利润同比增幅明显，创历史新高，但公司报价反而有所回落。\n\n1/ 业绩表现较好，但市场未充分反应\n某券商1H26净利润预计100-110亿，同比+93-112%，2Q26单季净利润67-77亿，同比+160-198%。这一数据高于市场预期，1H26利润已达到Bloomberg全年预测的67-74%。\n但消息公布后，A/H券商股本周反而回落约3%。原因在于市场关注：本轮业绩增长主要依赖投资收入，若市场环境变化，3Q表现可能不如预期。\n\n2/ 市场调整是否带来观察窗口？\n研究认为市场反应可能过度。理由有三：\n- 2Q业绩不仅来自投资收入，经纪、投行、资本中介等业务也在回暖\n- 该券商和另一家头部券商1H26利润均达到全年预测的70%，说明市场可能低估了券商业绩弹性\n- 估值处于合理区间：A股券商1.15倍PB，H股仅0.74倍PB\n\n3/ 某科技公司上市或成为关键变量\n该券商自5月18日以来报价上涨28%（A股）/23%（H股），跑赢板块16-17个百分点。核心原因是市场重新评估其对某科技公司的投资。该科技公司已\n\n[... middle omitted ...]\n\nid, investors may question whether the beat still matters given that A/H share brokers' share prices were down by an average 3%/3% this week, after GTHT's strong profit alert (link). We argue \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R082",
    "title": "研究笔记：拜耳二季度业绩前瞻——全年指引仍是市场关注核心",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# 研究笔记：拜耳二季度业绩前瞻——全年指引仍是市场关注核心\n\n市场对拜耳2026年二季度业绩的预期已经较为充分。研究机构在最新发布的业绩预览报告中指出，无论是集团营收、核心利润还是每股收益，二季度数据大概率与市场共识基本吻合。真正值得关注的不是单季波动，而是管理层是否会利用这次窗口，再次确认全年指引——而这恰恰是当前市场定价最需要的支撑。\n\n这份报告的核心判断是：二季度本身缺乏催化力，但指引的稳定性能为市场提供确定性。当前一致预期已基本落在公司全年指引的中枢附近，这意味着只要拜耳不主动下调目标，市场就不会出现预期差带来的谨慎修正。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度业绩不会偏离共识，但细节里藏着结构变化\n\n研究机构预计拜耳二季度集团营收为106.87亿欧元，与彭博共识的107.21亿欧元几乎持平。核心EBITDA预计为19.39亿欧元，略低于共识的19.56亿欧元，偏差不到1%。\n\n分业务看，制药板块营收预计为43.81亿欧元，略低于共识。但关键增长产品的势头依然强劲：Nubeqa预计同比增长54%，Kerendia预计增长63%。这两款产品正在接力Xarelto和Eylea的专利悬崖缺口——后者分别同比下滑45%和24%。作物科学板块营收预计为47.77亿欧元，与共识一致，草甘膦受益于量价齐升，同比增长20%。\n\n> **观察评论：** 二季度的数字本身不会改变市场对拜耳的叙事。但透过产品结构的变化，可以更清晰地看到拜耳正在经历从“旧药现金牛”向“新药增长引擎”的切换。Nubeqa和Kerendia的增速是否可持续，比单季总量是否达标更重要。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 全年指引才是当前市场定价的“定海神针”\n\n研究机构对全年指\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n# 拜耳Q2前瞻：业绩平稳，指引稳定\n\n**业绩平稳，指引稳定**\n\n**Q2预计符合预期，全年指引大概率维持**\n\n某外资机构最新研究预计，拜耳8月4日发布的Q2业绩将整体符合市场预期，核心看点在于管理层是否会维持全年指引。\n\n1️⃣ **Q2业绩预测：整体平稳**\n- 集团销售预计€106.87亿，与市场预期€107.21亿基本持平\n- 调整后EBITDA预计€19.39亿，略低于市场预期€19.56亿\n- 核心EPS预计€0.73，低于市场€0.76（注意：新口径下市场预期可能未完全调整）\n\n2️⃣ **三大板块各有看点**\n- **制药**：销售预计€43.81亿，略低于预期。但利润端更优，EBITDA €10.38亿，比市场预期高2%。\n  - 明星药Nubeqa（+54%）、Kerendia（+63%）持续高增长\n  - 老药Xarelto（-45%）、Eylea（-24%）继续调整\n- **作物科学**：销售€47.77亿，与预期一致。除草剂（+12%）、棉花（+67%）表现强劲，玉米（-6%）、大豆（-1%）因销售时点偏弱。\n  - 草甘膦增长20%，量价齐升\n- **消费者健康**：销售€1\n\n[... middle omitted ...]\n\nlow BBG Consensus at €1,956m, with our expectation for better profitability in Pharma [EBITDA (u/l) of €1,038m vs. €1,023m] offset by greater costs in Reconciliation [EBITDA (u/l) of €149m vs.\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 07 Jul 2026 09:11 PM BST\n\nDisseminated 08 Jul 2026 12:15 AM BST"
  },
  {
    "id": "R083",
    "title": "开源大模型：不是收入分流，而是能力分化的加速器",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# 开源大模型：不是收入分流，而是能力分化的加速器\n\n市场习惯把开源大模型视为一种收入威胁——权重公开后，第三方可以绕开官方API自行部署，流量和付费自然分流。这个逻辑没错，但只对了一半。一份关于中国大模型开源策略的深度报告提出了一个更尖锐的判断：开源不是分流，而是一面筛子。它真正考验的是模型能力本身——强者借此扩大分发和付费转化，弱者则更快暴露可替代性。这个框架正在改写中国大模型公司的市场定价逻辑。\n\n报告以智谱和MiniMax为例做了直接对比。GLM-5.2的全球竞争力让智谱有底气走宽松开源路线，通过MIT协议吸引开发者、云平台和海外用户，再通过官方API、Turbo系列和企业级服务完成变现。MiniMax的M3虽然也做了开源，但模型差异化尚不清晰，开源反而让用户更容易比价和切换。同一套策略，因为模型能力不同，走向了完全相反的结果。\n\n> **观察评论：** 这份报告的核心洞察其实很简单——开源策略的效果取决于模型是否“不可替代”。如果模型足够强，开源等于免费铺渠道，用户最终还是会回到官方API购买服务质量和持续更新。如果模型可替代，开源等于给竞品送用户。这个框架可以用来重新审视所有中国AI公司的估值基础，而不仅仅是这两家。\n\n报告进一步拆解了“开源不等于API同质化”这一关键机制。一个开源权重发布后，官方API仍是持续迭代的活产品——后训练优化、指令遵循改进、缓存策略、推理效率提升，这些都不会实时回馈到开源版本。第三方部署的同一模型，可能在几个月后与官方API产生肉眼可见的质量差距。对于编程、智能体和长上下文等高要求场景，这种差距直接决定用户付费意愿。\n\n报告用DeepSeek V4 Pro和MiniMax M3两个案例做了量化验证。DeepSeek官方API在缓存命中率上达到93.5%，第三方最低只有18.2%，一个典型工作负载的月度成本相差4-8倍\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n大模型开放模型≠放弃变现\n\n开放模型，更考验实力\n\n某研究机构最新报告在聊一个很有意思的话题：大模型公司把模型权重开源，到底是“分享”还是“布局”？\n\n结论很直接：强者更强，弱者更难。\n\n1/ 开源不是放弃变现，而是换一种方式提供服务\n- 开源让更多人用上模型，但官方API依然是“最优解”\n- 第三方部署跑的是“快照版”，官方API是“持续优化版”\n- 模型越强，用户越愿意为官方服务付费（速度、稳定性、最新版本）\n\n2/ 拼的是“模型力”\n- 智谱GLM-5.2全球竞争力强，开源策略更自信：用开源拉用户，用Turbo系列保利润\n- MiniMax M3差异化不够，开源反而让用户更容易比价、替换\n\n3/ 官方API的护城河\n- 模型发布后，官方还在持续优化：指令跟随、代码能力、长上下文、缓存策略\n- 第三方跑的还是“老版本”，体验差距会越来越大\n- 对复杂任务（编程、Agent、长文本），用户愿意为稳定付费\n\n4/ 数据说话\n- DeepSeek V4 Pro官方API比第三方便宜6-12倍（靠缓存）\n- MiniMax M3官方缓存命中率更高，实际成本更低\n\n一句话总结：开源是漏斗，官方API是变现口。模型够\n\n[... middle omitted ...]\n\nrnal GPU capacity across CSP, inference platforms and private deployments, rather than only on the provider's own compute stack. The LLM provider can still participate and monetize through off\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R084",
    "title": "JPM：政策扩容与治理完善，人民币流动性的双重信号",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：政策扩容与治理完善，人民币流动性的双重信号\n\n6月中国外汇储备下降260亿美元至3.416万亿美元，低于市场普遍预期。这个数字本身并不惊人，真正值得关注的是它背后揭示的结构性变化：进口比预期更强，贸易顺差正在收窄。而更关键的问题是，这些顺差有多少最终变成了人民币的买盘。\n\nJPM这份7月8日发布的研究报告，核心判断并不复杂——人民币的支撑逻辑正在从“贸易顺差”向“政策管道”切换。报告没有给出具体的汇率点位预测，而是系统性地梳理了影响下半年人民币走势的五个变量，其中多数变量指向一个共同结论：人民币升值空间存在，但节奏和幅度取决于政策容忍度与市场行为之间的博弈。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 外汇储备下降不只是估值损失，进口结构变化更值得追踪\n\n6月外储下降的260亿美元中，JPM估算估值损失约335亿美元，经常账户顺差约524亿美元，隐含资本外流约450亿美元。估值损失主要来自美元指数从98.9升至101.2带来的非美元资产折算效应。\n\n但报告真正想传递的信号藏在进口端。结合另类数据追踪，6月进口强于预期，这意味着贸易顺差收窄的趋势可能比市场目前定价的更持续。如果下半年能源进口账单回升（此前石油进口调整），贸易顺差将进一步压缩。\n\n> **KC评论：** 贸易顺差收窄本身不一定是人民币的利空，关键看收窄的原因。如果是内需驱动的进口增加，反而说明宏观环境动能改善，对人民币中长期是支撑。但如果是关税冲击导致出口下滑，那就是另一回事。报告没有直接下结论，而是把判断权留给后续的贸易数据。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 政策信号两线并行：一边完善治理，一边扩容管道\n\n5-6月出台的一系列跨境标的、期货、产品和对外研究相关政策，在市场上引\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n央行新工具上线，人民币后续观察\n\n📌 人民币下半年走势探讨\n\n6月外汇储备有所回落，较预期减少约260亿美元。从结构来看，主要受进口端变化影响，而非资本流动因素。贸易顺差虽仍存在，但收窄趋势值得留意。\n\n1️⃣ 央行政策调整：优化而非收紧\n5-6月的跨境政策调整，外界有不同解读。实际上，央行同步推出了离岸人民币回购工具、提升债券通额度、扩大香港人民币流动性安排。更准确的理解是：在规范现有渠道的同时，也在拓宽新的通道。\n\n2️⃣ 下半年人民币的几个观察点\n- 贸易与能源进口：若能源价格持续调整，顺差支撑仍可关注\n- 出口商结汇意愿：美元走强时，企业倾向于持有美元\n- 美联储政策节奏：中美利差参考意义有所下降，但美元强弱仍是重要变量\n- 7月重要会议：市场关注后续政策方向，实际效果更多取决于执行节奏\n\n3️⃣ 离岸人民币的“新基础设施”\n央行7月7日宣布的措施值得关注：债券通额度从5000亿提升至8000亿、推出5年期离岸国债期货、香港人民币流动性安排扩大至5000亿。这些举措旨在为人民币国际化提供更完善的制度支持。\n\n一个值得注意的细节：央行6月增持黄金（+48万盎司），同时美债持仓小幅下降。这反映储备资产多元\n\n[... middle omitted ...]\n\n52) 2800-0143 tingting.ge@JPM.com\n\n\\- May–June measures read more like governance and enforcement/channel clean-up than a broad outbound investment clampdown.\n\n\\- New plumbing includes offshor\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R085",
    "title": "JPM：中国再保险受益于海上保险回流，估值或未充分反映",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：中国再保险受益于海上保险回流，估值或未充分反映\n\n中国已是全球最大的船队和货物贸易国之一，但一个长期存在的结构性问题始终未解：大量海上保险保费、再保险份额、理赔仲裁服务，仍然流向伦敦和其他成熟市场。JPM最新研报指出，政策驱动的“不确定性回流”正在改变这一格局，而中国再保险和中国太平是这一趋势中最直接的受益者。\n\n这份报告的核心判断并不复杂：当监管层将上海定位为海上保险枢纽，并密集出台支持政策时，中国本土保险公司正在获得一个历史性的结构性增长窗口。这不是一个短期的主题炒作，而是涉及承保能力、法律框架、争议解决全链条的深度重构。\n\n> **KC评论：** 不确定性回流（onshore risk repatriation）这个词值得留意。它意味着原本外流的保费和业务正在被政策引导回流本土，这为国内保险公司创造了增量蛋糕，而非存量竞争。报告特别提到了两个受益标的，但更重要的是理解这个趋势的持续性——它依赖于政策、法律和基础设施的协同推进，而非单一事件驱动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政策密集出台，但真正的变化在2026年\n\n报告梳理了从2023年至今的一系列政策，包括2024年10月发布的《关于推动上海航运保险业高质量发展的指导意见》，以及将于2026年5月生效的修订版《海商法》。这些政策并非孤立存在，而是围绕一个核心目标：降低中国海上保险对海外市场的结构性依赖。\n\n值得注意的细节是，这些政策覆盖了从产品创新、数字化理赔、到跨境争议解决的全链条。例如，上海临港新片区对再保险机构的落户奖励和人才政策，以及海南自贸港推动的人民币计价和结算试点，都在为不确定性回流搭建基础设施。\n\n但报告也暗示，这些政策的效果需要时间才能体现在报表中。2026年《海商法》的实施可能是一个关键的催化剂，因为它将重\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n海上保险，正在回归本土市场\n\n海上保险回归  \n政策推动本土化发展  \n\n近期有研究机构发布了一份关于中国海上保险的分析报告，核心逻辑较为清晰：中国作为全球主要航运国家之一，过去大量海上保险业务依赖海外市场，现在政策正在推动相关风险保障逐步回归国内。\n\n1️⃣ 为什么需要回归？  \n中国在造船、货运、商船吨位等方面已处于全球前列，但海上保险的承保、再保、理赔、仲裁等环节长期由海外市场主导。这不仅导致保费持续外流，也带来供应链方面的潜在考量。绿色航运、海上风电、一带一路等新需求，更要求国内具备独立承保能力。\n\n2️⃣ 政策正在推进  \n2024年10月上海发布航运保险高质量发展指导意见，2026年5月新《海商法》生效，配合海南自贸港、洋山港等政策，都在推动上海成为海上保险枢纽。核心方向：产品创新（新能源船险）、数字化（区块链电子保单）、跨境服务便利化。\n\n3️⃣ 相关方向  \n报告认为，中国再保险（中再集团）是中期主要关注对象，作为国内相对少见的综合性再保集团，主导国家船舶保险共同体和海上丝绸之路共同体。中国太平也有相关产险和再保业务，可能受益于政策催化。\n\n4️⃣ 估值参考  \n报告给出中再集团FY26E P\n\n[... middle omitted ...]\n\npport, specialized clauses and cross-border dispute settlement, has long been dominated by London and other developed markets (For details, see Asia Insurance: Summer Series: China's marine in\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R086",
    "title": "JPM：生产端修复与需求端错位，JPM拆解中国库存周期",
    "source_group": "bank_research",
    "source_label": "投行/券商",
    "institution": "JPM",
    "digest": "[wechat_article.md]\n# JPM：生产端修复与需求端错位，JPM拆解中国库存周期\n\n这份JPM最新月度数据展望提出了一个值得产业决策者反复咀嚼的判断：当前中国宏观环境呈现的“韧性”和“仍在调整”并非同一层面的矛盾，而是生产端修复与需求端吸收之间的错位。报告的核心信号是——工业产出有底，但内需依然构成硬约束。\n\n5月数据显示，工业增加值同比增长5.8%，高技术制造业增速达到15.1%，对前五个月工业增长的贡献接近40%。出口在AI相关设备、存储芯片、新能源产品以及贸易转口的支撑下保持强劲。但与此同时，零售销售同比转负，固定资产研究调整10.7%，基础设施研究下降9.4%，房地产研究跌幅扩大至24.3%。\n\n换个角度看：生产端并非没有活力，但活力集中在电子、高技术制造和部分上游行业，而与消费、住房和传统产业相关的领域仍然偏弱。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 财政存款创十年同期次高，说明钱还没花出去\n\n报告中最值得关注的图表之一是5月财政存款数据。一般公共预算支出连续第二个月调整，基础设施支出同比下降12.0%，而财政存款攀升至过去十年5月第二高水平。\n\n这意味着什么？专项债发行确实在提速，但资金从发行到形成实物工作量之间，仍然存在明显的传导阻滞。财政资金停留在账面上，而不是转化为项目开工和施工活动。这份JPM报告明确指出，如果6月活动和二季度GDP数据不及预期，7月政治局会议可能会释放更强的逆周期信号。但无论政策如何定调，核心瓶颈在于：能否把财政资源转化为真实需求。\n\n> **KC评论：** 财政存款高企不是流动性问题，是执行力问题。报告提醒读者关注的是“资金到项目”的转化率，而不是政策本身的方向。完整报告中关于财政执行节奏的月度追踪图表值得细看。\n\n![研报原图 2](assets/source_image_02.jpg\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n工业企稳，但内需仍在等待政策落地\n\n📊 生产端有韧性，需求端关注财政节奏\n\n近期有机构发布了关于中国月度数据的观察，核心逻辑较为清晰：生产端暂时保持稳定，但内需仍需财政政策进一步发力。6月数据可能较4-5月有所改善，但不宜过早判断趋势。\n\n1️⃣ 生产端有支撑，但覆盖面有限\nPMI小幅改善，出口受高科技和AI相关需求带动，油价下跌也缓解了部分成本压力。5月高技术制造业同比增长15.1%，贡献了1-5月工业增长的近40%。但就业、库存、出口订单数据仍存在分化，尚未出现大规模的补库存或招聘周期。\n\n2️⃣ 内需表现相对偏弱\n5月零售同比下降0.6%，固定资产投资下降10.7%，基建投资下降9.4%，房地产投资下降24.3%。以旧换新补贴可能更多是提前释放需求，收入预期和信心有待修复，服务消费的增长空间有限。生产端有韧性，但需求端承接不足，导致库存积累和价格调整。\n\n3️⃣ 财政执行是7月的重要观察点\n5月一般预算支出连续第二个月收缩，基建支出同比下降12%，财政存款却创下十年同期第二高。专项债发行有所提速，但关键在于资金能否转化为项目开工和实物工作量。如果6月数据及二季度GDP表现不及预期，后续政策可能进一步调整\n\n[... middle omitted ...]\n\nity before external demand becomes less reliable. PMIs point to a floor in industrial momentum, not a new upswing. Production and orders improved, but employment, inventories, and export order\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R087",
    "title": "国际清算银行：消费贷款监管加码，小银行在108个月这道门槛上退缩",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "国际清算银行",
    "digest": "[wechat_article.md]\n# 国际清算银行：消费贷款监管加码，小银行在108个月这道门槛上退缩\n\n一项针对哥伦比亚消费贷款拨备新规的实证研究，给出了一个反直觉的结论。2023年1月生效的监管要求，对期限超过72个月和108个月的消费贷款分别加征10%和40%的额外拨备——这原本被市场预期会显著压缩长期信贷供给。但国际清算银行（BIS）最新工作论文显示，这项政策的平均效果几乎为零：贷款金额、利率和抵押要求均未出现统计显著的调整。\n\n真正的故事藏在细节里。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 拨备成本上升，大银行选择“自己消化”\n\n论文的核心发现是：大型机构吸收了新增拨备成本，没有将其转嫁给借款人。对于期限超过108个月的贷款，大银行既没有提高利率，也没有降低贷款价值比（LTV）。原因不难理解——这些机构在消费信贷市场占据主导份额，资产负债表足够厚，能够将额外拨备视为一项可控的合规成本，而非需要立即调整定价策略的信号。\n\n这意味着，当监管政策针对的是整个系统的韧性目标时，头部机构的缓冲能力远比想象中强。它们的行为逻辑不是“成本增加就调整”，而是“成本增加是否触及盈利底线”。对于大行而言，10%或40%的边际拨备增幅，远未达到需要改变放贷策略的阈值。\n\n> **KC评论：** 这份报告最值得关注的地方，不是结论本身，而是它揭示了一个经常被忽视的机制——监管成本在不同规模机构间的分布极不均匀。大银行可以“吸收”，小银行只能“调整”。完整报告中对机构异质性的计量分析，尤其是利用匹配方法处理选择偏误的部分，值得仔细阅读。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 小银行被迫收紧：108个月成为真正的分水岭\n\n与大型机构的从容不同，小型贷款机构在108个月以上的超长期贷款上做出了明确调整。具体表现为：贷款发放\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n哥伦比亚新规：长期贷款不缩量，但小银行在悄悄收紧\n\n**长期贷款新规，效果如何？**\n\n**哥伦比亚2023年对超长期消费贷加了拨备要求，结果贷款总量没降，但小银行悄悄收紧了。**\n\n---\n\n1/ **新规的背景**\n哥伦比亚2021-2022年消费贷增速过快，到2022年下半年，贷款质量开始恶化。监管担心长期贷款风险积累，2023年1月起要求：\n- 期限>72个月（6年）的新消费贷，拨备加10%\n- 期限>108个月（9年）的，拨备加40%\n\n2/ **整体效果：不影响信贷供给**\nBIS这篇论文用了精细匹配方法，结论是：\n- 贷款金额没下降\n- 利率没显著变化\n- 抵押要求（LTV）也没收紧\n也就是说，大银行直接吸收了成本，没转嫁给借款人。\n\n3/ **但小银行不一样**\n小机构对>108个月的贷款，明显收紧了：\n- 放贷金额减少\n- LTV比例降低\n原因：小银行抗风险能力弱，拨备成本上升直接影响利润空间。\n\n4/ **政策启示**\n- 窄范围、期限定向的拨备规则，对整体信贷供给冲击有限\n- 但会加剧大小银行之间的市场分化\n- 同期央行加息的影响，可能比这条拨备新规更显著\n\n---\n\n**欢迎一起讨论：\n\n[... middle omitted ...]\n\nomists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do no\n\n[... middle omitted ...]\n\nts the coefficients estimated from Equation (4) along with their 95% confidence intervals, computed using standard errors clustered at the entity level. The vertical red line denotes the reference period of the analysis."
  },
  {
    "id": "R088",
    "title": "布鲁盖尔研究所：中国掌控70%锂加工，欧盟供应链突围要靠贸易协定",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：中国掌控70%锂加工，欧盟供应链突围要靠贸易协定\n\n全球绿色转型对关键原材料的需求正在以指数级增长。锂的需求预计到2050年将增长470%至800%，石墨和镍的增幅也在130%到250%之间。然而，欧盟的应对策略——从《关键原材料法案》到战略伙伴关系——在实证检验面前，成绩单并需要继续观察看。\n\n布鲁盖尔研究所最新发布的政策简报，系统评估了欧盟关键原材料战略的内外两个维度。结论直接且克制：欧盟的“战略项目”很难实现自给自足目标，“战略伙伴关系”至今未产生可测量的贸易效应。真正有效的，反而是那些被低估的贸易协定条款。\n\n这份报告的价值不在于罗列问题，而在于提供了一套可量化的评估框架。它让产业决策者看清：哪些政策工具在真实运转，哪些只是纸面承诺。\n\n> **KC评论：** 报告中关于“战略项目”的数据值得细看。60个项目中，目前只有21个获得了明确的资金支持，总金额约12.5亿欧元。考虑到单个大型矿山从勘探到投产的平均周期超过10年，这笔资金能否撬动足够产能，存在很大疑问。建议读者重点关注报告中的表A3，那里详细列出了每个项目的资金来源和规模。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 欧盟自给自足的目标，与项目现实之间存在断层\n\n《关键原材料法案》设定了四个2030年基准：10%的消费来自国内开采，40%来自国内加工，25%来自回收，且单一第三国供应不超过65%。这些数字本身是合理的战略目标，但报告用数据揭示了一个尴尬的落差。\n\n欧盟目前的全球开采份额几乎可以忽略不计，绝大多数关键矿物的开采占比低于10%。加工环节稍好，锂的加工份额达到9.5%，石墨达到49.4%。但这些数字距离40%的加工目标仍有巨大差距。更关键的是，欧盟在回收环节的全球份额较高，这反而暗示了一个结构性现实：欧洲的优势不在“挖矿”\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n欧盟抢锂矿，为什么还是输给中国？\n\n🔍 欧盟的“关键原材料焦虑”\n\n欧盟想实现绿色转型，电池、风电、芯片都离不开锂、钴、稀土等关键原材料。但现实很骨感：供应链高度集中在中国，而且日本、美国也在抢资源。欧盟的应对策略效果如何？这篇研报给出了几个核心判断。\n\n1️⃣ 战略项目不够“解渴”\n欧盟有个“关键原材料法案”（CRMA），目标是到2030年实现自给自足。但研报分析发现，目前60个战略项目的产能，远远达不到这个目标。比如锂，全球需求到2050年要涨4-8倍，欧盟自己挖的矿和建的厂，杯水车薪。\n\n2️⃣ 战略伙伴关系“雷声大、雨点小”\n欧盟和不少资源国签了战略伙伴协议，但研报数据显示，这些协议对实际贸易量的提升效果不明显。反而是贸易协定（FTA）里的相关条款，实实在在地推动了关键原材料对欧盟的出口增长。\n\n3️⃣ 中国卡在“加工”环节\n欧盟对中国的依赖，不只是矿产本身，更多是在加工和精炼。中国控制着全球70%的锂精炼、90%的稀土加工。即使欧盟从别国买矿石，最后还是得运到中国加工。这才是真正的软肋。\n\n4️⃣ 别学美国的“地板价”\n美国想推动“价格下限”机制，保护本国矿产商。但研报建议欧盟别跟，应该更灵活地签双\n\n[... middle omitted ...]\n\necutive summary\n\nCRITICAL RAW MATERIALS (CRMs) are essential to the European Union's green and digital transition, underpinning technologies from batteries to semiconductors. Demand is expecte\n\n[... middle omitted ...]\n\ngel.org. Publication of altered content (for example, translated content) is allowed only with Bruegel's explicit written approval. Bruegel takes no institutional standpoint. All views expressed are the researchers' own."
  },
  {
    "id": "R089",
    "title": "IMF：财政赤字压至3%上限，科特迪瓦如何应对中东冲击？",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：财政赤字压至3%上限，科特迪瓦如何应对中东冲击？\n\n西非国家科特迪瓦在2026年6月完成了与IMF的最后一轮项目审查，拿到了约8.3亿美元的最后一笔拨款。这份IMF国别报告（Country Report No. 26/171）的核心判断是：一个依赖大宗商品出口、长期面临财政赤字和债务不确定性的发展中国家，通过持续的收入侧财政整顿和审慎债务管理，不仅把财政赤字压到了西非经货联盟3%的GDP上限，还让公共债务占GDP比重在十多年来首次下降，债务困境不确定性从“中等”改善为“低”。这个转变对观察新兴市场债务治理和非洲主权信用修复具有参照价值。\n\n报告完成于全球不确定性加剧的背景下——中东冲突推高油价至每桶100美元左右，科特迪瓦两大收入来源（石油税收和可可出口）同时承压。但这并未打乱其改革节奏。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 财政纪律的考验在于：外部冲击来临时，是否还守得住3%赤字红线\n\n科特迪瓦在2025年成功将财政赤字压到3%的GDP，完成了西非经货联盟的硬性要求。但进入2026年，中东冲突的溢出效应开始显现：燃油收入下降、可可出口收入减弱，叠加需要维持优先研究支出，政府不得不将2026年赤字目标从3%放宽至3.8%。\n\n这个调整并非放弃纪律。报告明确指出，政府承诺在2028年前重回3%的赤字上限。关键在于调整的“质量”——不是靠压缩公共研究，而是通过提高燃油零售价（2026年5月1日执行）、加强税收征管（包括推进电子发票、完善转让定价规则）来弥补收入缺口。换句话说，调整的代价主要由消费端和税收合规承担，而非砍掉基础设施建设。\n\n> **KC评论：** 对关注新兴市场主权信用的读者来说，科特迪瓦的案例提供了一个“不确定性测试”样本。当外部冲击来临时，财政松弛的“度”在哪里？IMF认可了3%到3.\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n科特迪瓦：IMF最后审查过关，8.3亿美元到账\n\n封面：8.3亿美元到账\n\n副标题：IMF最后审查过关，释放了什么信号？\n\n---\n\nIMF刚刚完成了对科特迪瓦的最终审查，一次性释放约8.3亿美元资金。\n\n这意味着什么？简单拆解一下：\n\n1. **财政纪律在收紧**\n   财政赤字从2023年的5.1%降到2025年的3%（西非经货联盟上限），这是十年来公共债务占GDP首次下降。债务风险评级从“中等”调至“低”。\n\n2. **2026年赤字目标小幅放宽**\n   受中东局势影响，2026年油价预计涨至100美元/桶，科特迪瓦把赤字目标从3%放宽到3.8%。但承诺2028年回到3%。\n\n3. **气候改革全部完成**\n   包括农业指数保险、碳税战略、清洁汽车政策、两个太阳能电站招标——全部达标。\n\n4. **经济增速放缓但稳健**\n   2026年GDP增速预计从6.5%降至6%，通胀从接近零反弹至3.3%。家庭消费和投资仍是主要增长动力。\n\n5. **结构改革重点：减税、反腐、去灰色名单**\n   中期收入战略持续推进，税基拓宽、电子发票、转让定价规则都在路上。FATF灰色名单退出在望。\n\n---\n\n科特迪\n\n[... middle omitted ...]\n\nlowing documents have been released and are included in this package:\n\n• A Press Release including a statement by the Chair of the Executive Board.\n\n\\- The Staff Report prepared by a staff tea\n\n[... middle omitted ...]\n\nties' commitment to reforms, we would appreciate Executive Directors' support for the completion of the $6^{\\text{th}}$ reviews under the ECF and EFF arrangements and the $5^{\\text{th}}$ review under the RSF arrangement."
  },
  {
    "id": "R090",
    "title": "IMF：黄金不是终极避险资产？IMF揭示其流动性远低于市场预期",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：黄金不是终极避险资产？IMF揭示其流动性远低于市场预期\n\n黄金在各国央行储备中的占比从2019年初的10%飙升至2025年8月的超过22%，但这份IMF最新发布的Note/2026/007号研究报告给出了一个反直觉的判断：推动这一变化的，不是央行大规模观点偏积极实物黄金，而是金价上涨带来的估值效应。2018年至2025年，全球央行黄金储备的市值从约1.2万亿美元升至4.5万亿美元，增幅达268%，但同期黄金持有量仅增长约8.5%。这意味着，近三分之二的市值增长来自那些持有量基本未变的央行。\n\n这份报告的核心主张是：黄金是一种高不确定性储备资产，其避险属性高度依赖于特定情境，且流动性远低于其名义市场价值所暗示的水平。对央行和决策者而言，当前最需要警惕的不是“该不该买黄金”，而是“如何正确评估现有黄金头寸的真实不确定性”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 黄金的避险功能正在退化，尤其在尾部不确定性面前\n\n报告通过大量实证数据检验了黄金对不同不确定性的响应特征。结果显示，黄金最稳定的对冲功能是针对利率不确定性和美元贬值，但在疫情后，其对市场下跌、通胀意外和地缘政治冲击的保护作用显著减弱。2022年以来，公司与债券之间传统负相关关系的瓦解，进一步削弱了黄金在组合观察中的分散化价值。\n\n更关键的是，黄金并不具备可靠的“安全港”属性。在尾部事件中，黄金价格与不确定性资产的相关性并不稳定，有时甚至同步下跌。这意味着，当央行最需要动用储备来应对极端市场冲击时，黄金可能无法提供预期的保护。\n\n> **KC评论：** 许多市场参与者习惯将黄金视为“终极避险资产”，但IMF的实证分析提示，这一认知需要更新。黄金的避险功能是有条件的，且正在变化。对于依赖储备进行扰动管理的央行来说，过度依赖黄金可能反而削弱储备的“自我保\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n央行买金潮，真不是你以为的那样\n\n封面：黄金储备真相\n\n副标题：IMF最新报告划重点\n\n---\n\n最近各国央行都在增持黄金，但这轮金价上涨带动的储备扩张，其实另有玄机。\n\n某外资投行最新研报指出：2019-2025年间，央行黄金储备市值从1.2万亿飙到4.5万亿，但实物量只增了8.5%。近三分之二的增值，来自金价上涨的“被动收益”，而非主动买入。\n\n1/ 黄金≠高流动性资产\n\n黄金日均交易量约1340亿美元，流动性确实不错。但跟美债（日均1.07万亿）比，差距明显。更关键的是，黄金在极端行情下的变现能力，远不如账面价值那么“好看”。\n\n2/ 避险属性有“条件限制”\n\n黄金确实能对冲利率风险和美元贬值，但对冲股市下跌、通胀冲击和地缘风险的效果，在疫情后明显减弱。它不是万能的“安全港”，更像一个“条件性”避险品。\n\n3/ 央行应该怎么配\n\n研报建议：黄金更适合放在“投资层”，而不是“流动性层”。如果混在一起，需要用流动性调整后的价值来评估实际可用资金。简单说，别把黄金当“现金”用。\n\n4/ 国内购金风险大\n\n一些央行从国内买金矿，这涉及准财政操作、治理风险、货币调控难题。研报明确表态：非货币黄金收购，最好别碰。\n\n[... middle omitted ...]\n\news expressed in IMF Notes are those of the author(s), although they do not necessarily represent the views of the IMF, its Executive Board, or its Management.\n\nABSTRACT: This Note examines th\n\n[... middle omitted ...]\n\nfor Gold? On the Interaction of Gold and Foreign Exchange Reserve Returns.” BIS Working Paper No. 906, Bank for International Settlements.\n\n![](images/873952478e3aa51a1f6ad478d9ab2df956155e174fc99496064788956a3de1d6.jpg)"
  },
  {
    "id": "R091",
    "title": "波士顿咨询：AI价值创造不是斜坡而是门槛，波士顿咨询揭晓6%真相",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI价值创造不是斜坡而是门槛，波士顿咨询揭晓6%真相\n\n关于AI的讨论充斥每季度的业绩发布会。波士顿咨询（BCG）一项覆盖600余家美国上市公司的研究发现，CEO们在电话会上提及最多的主题就是AI。但这家咨询机构想回答一个更实在的问题：哪些公司真正把AI的讨论转化成了可衡量的业绩？\n\n答案比多数人预想的更集中，也更反直觉。\n\nBCG构建了一套从外部衡量AI应用成熟度的指标体系，涵盖技术栈、人才密度和部署深度三个维度。结果只有一个数字值得记住：**仅有6%的公司可以被定义为AI应用领导者。** 但这6%的企业在过去三年创造了行业调整后9.3个百分点的股东总回报（TSR）超额收益。更关键的是，这一超额收益并非来自市场情绪驱动的估值扩张，而是完全由基本面——营收增长和利润率提升——贡献。\n\n这意味着一件事：AI的价值创造不是一条平缓的斜坡，而是一道陡峭的门槛。绝大多数公司还站在门槛之外。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 真正的价值不在效率，而在增长\n\n外界对AI的主流叙事是自动化、降本和裁员。BCG的数据给出了另一个方向。在那些AI领导者中，只有10%选择了“用更少的人做同样的事”这一路径。59%的领导者走的是“用同样的人做更多的事”——他们将AI带来的生产力提升重新投入业务扩张，而不是转化为成本削减。\n\n结果也很直接：这些领导者不仅在营收和利润率上领先，其员工人数增速也比行业中位数高出3个百分点。AI并没有让它们变得更“瘦”，而是让它们变得更大、更快。\n\n> **KC评论：** 这组数据对任何正在制定AI战略的管理者都值得反复看。效率路径是入门，不是终点。如果一家公司把AI的回报定义在减少几个岗位或节省百分之几的运营成本上，它可能永远无法跨过那道价值门槛。报告里提到的IBM、Salesforce\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\nAI聊得多，做到的人只有6%\n\n**AI落地的真相**\n\n投行研报分析了600多家美国上市公司，发现AI话题在CEO财报电话会里出现频率最高。但真正把AI落地、跑出业绩的公司，只有6%。\n\n**1. 价值不靠“说”，靠“做”**\n\n这6%的领先者，过去3年行业调整后的股东回报比中位数高出9.3个百分点。而剩下94%的公司，回报基本没变化。更关键的是，这个回报优势完全来自基本面——收入增长和利润率提升，不是靠P/E倍数吹起来的泡沫。\n\n**2. 用AI不是“减人”，而是“增人”**\n\n很多人以为AI等于裁员。但研报发现，领先者使用AI的主要路径是“增长”而非“效率”。59%的领先者用AI放大每个员工的能力，比如客服少花20%时间处理常规问题，省出的时间去做高价值工作。结果是，这些公司反而在扩招——员工人数年增速比中位数高3个百分点。\n\n**3. 从“买工具”到“建能力”，最难的是人才**\n\n研报把AI能力拆成三个维度：技术、人才、部署。从入门到领先，需要经历三个关键转变：\n- 从买几个工具到构建专业AI生态系统\n- 从试点项目到规模化部署\n- 跨越人才鸿沟——这是最难的一步\n\n领先者中13%的员工有AI相\n\n[... middle omitted ...]\n\nions or from self-reported surveys. Both have limitations: corporate communications reflect what company leaders think investors want to hear, and surveys reflect what companies say about them\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R092",
    "title": "波士顿咨询：波士顿咨询拆解加拿大消费韧性，收入覆盖不足六成",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：波士顿咨询拆解加拿大消费韧性，收入覆盖不足六成\n\n加拿大2026年第一季度实际消费支出增长约2%，与十年均值持平，人均支出连续六个季度上升。如果只看这个数字，结论很直接：消费者韧性十足，宏观环境基本面健康。\n\n但波士顿咨询（BCG）一份最新研报给出了完全不同方向的判断。报告标题已经点明：**这个信号的含义已经变了。**\n\n增长确实存在，但来源正在切换。收入已不再是消费扩张的主要支撑。取而代之的是三个更脆弱的引擎：储蓄消耗、资产增值和借贷。而真正需要关注的，是中间60%的家庭——这是多数消费企业赖以生存的核心客群——正在向低收入群体的财务状态靠拢，而非向上。\n\n> **KC评论：** 报告的真正价值不在于否定消费数据，而在于拆解了“支出增长”这个总量指标背后的结构性分化。对于任何以加拿大为重要市场的消费企业，这份报告提供了一个更精细的不确定性地图。完整报告中的四张图表，分别展示了收入覆盖、储蓄变化、资产分配和负债结构，值得仔细对照。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 收入只覆盖了中间家庭不到六成的新增支出\n\n从2021年到2025年，加拿大各收入阶层的支出增幅大致相当：最低20%家庭支出增长27%，中间60%增长19%，最高20%增长24%。表面看，消费扩张是普适的。\n\n真正的分化在于收入能否覆盖这些新增支出。最高20%是唯一一个收入增长完全匹配并支撑支出扩张的群体，覆盖了新增支出的106%。中间60%的收入增长只覆盖了每新增1美元中的57美分。最低20%几乎完全没有被收入覆盖。\n\n这意味着，对于中间阶层而言，近一半的新增支出并非来自工资增长，而是来自其他来源。报告没有完全展开的是，这种“收入与支出脱钩”的状态已经持续了四年，而非一个季度的异常波动。\n\n![研报图表 2](assets/xhs_\n\n[... middle omitted ...]\n\n转化为支出——尤其是在汽车、奢侈品、餐饮和宠物护理等跨收入群体消费差异较大的品类上。\n\n**一个尚未完全回答的问题是：如果资产价格维持高位但通胀因油价上升而重新抬头，消费者的实际购买力将如何变化？** 波士顿咨询的框架暗示，这种组合对中间和低收入家庭可能是最糟糕的情景——他们既无法从资产增值中获益，又要面对更高的生活成本。但对于最高收入群体，这种情景的影响可能有限。加拿大消费市场的二元分化，正在从一种观察变成企业必须纳入战略规划的现实。\n\n[note.md]\n加拿大消费回暖？别急着开心\n\n消费数据回暖≠钱包鼓了\n\n加拿大Q1消费增长2%，连续6个季度人均支出上升。表面看是消费力强，但拆开看：增长主要靠前20%高收入群体拉动，剩下80%的人靠什么在撑？\n\n1️⃣ 收入跟不上，储蓄在消耗\n中等收入家庭每新增1元消费，只有0.57元来自收入增长。低收入家庭更惨，收入增长几乎为零。2021-2025年，中等家庭储蓄每年减少约7000加元，低收入家庭减少15000加元。\n\n2️⃣ 资产升值帮了忙，但只帮到有钱人\n前80%家庭资产增长13%-26%，靠股市和房产升值。但底层20%资产反而缩水2%，被迫变卖家当维持日常。\n\n3️⃣ 借钱消费成为常态\n中等家庭负债增长最快（+22%），底层家庭负债增17%但资产缩水，净资产缩水约35000加元/户。借钱消费的底气来自资产升值，但大部分资产是房子，流动性差。\n\n关键问题：如果资产价格回调、利率继续走高，这些靠借钱和消耗储蓄支撑的消费还能持续多久？\n\n对企业来说，加拿大已经没有“平均消费者”了。前20%和后80%的消费能力、资产状况、债务压力差距越来越大。未来增长策略需要更精准地针对不同收入群体设计。\n\n#学习笔记\n\n[source_\n\n[... middle omitted ...]\n\nolds are covering their spending by relying more on savings, leaning on rising portfolio values, and borrowing. And much of the increase isn't buying goods at all. Services are driving most of\n\n[... middle omitted ...]\n\nto receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.\n\n![](images/8e91c1ba99929d7612e00d64a5834a912bda80d5a7098ed6ea5772920f5324a5.jpg)"
  },
  {
    "id": "R093",
    "title": "波士顿咨询：折扣超市占据过半市场？波士顿咨询称这不是预警而是现实",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：折扣超市占据过半市场？波士顿咨询称这不是预警而是现实\n\n折扣超市的崛起已经不再是“宏观环境节奏变化时的替代选择”，而是一场结构性的行业重塑。波士顿咨询这份最新报告的核心判断是：折扣超市正在从“低价简陋”的业态进化为“高质低价”的主流渠道，在许多地区，它们即将占据超过一半的市场份额。这不是威胁预警，而是行业格局已经发生根本性变化的信号。\n\n过去十年，折扣超市不再满足于用有限品类和简陋店面吸引价格敏感人群。它们开始开设更大的门店，扩充生鲜和有机产品线，在盲测中击败传统品牌的自有产品，并通过精心设计的店面体验赢得顾客提到度。更关键的是，它们的客户群已经从低收入群体扩展到了高收入、精明的消费者——这些人开始问一个根本问题：“我为什么要多付钱？”\n\n> **KC评论：** 这份报告最值得关注的不是折扣超市的增速，而是它们已经打破了“低价=低质”的消费者心智。当高收入群体开始主动选择折扣渠道，传统超市的定价权就出现了不可逆的裂缝。报告中的BAI（品牌倡导指数）数据值得细看，它揭示了折扣超市如何将价格优势转化为品牌忠诚度。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 折扣超市的扩张已进入“自我强化”阶段，传统玩家很难靠等待逆转\n\n波士顿咨询将折扣超市的发展分为三个阶段：萌芽期（市场份额低于15%）、扩张期（15%-40%）、成熟期（超过35%）。在德国、挪威、丹麦等成熟市场，折扣超市已占据超过35%的份额，传统玩家即便反击，也难以扭转趋势。\n\n更值得警惕的是扩张期市场。在比利时、波兰等地，折扣超市已建立高效运营模型，单店坪效远超传统超市，并正在通过新店复制加速渗透。报告提到，Lidl计划在波兰开设200家门店，在罗马尼亚开设100家。这不是零星的试水，而是系统性的市场占领。\n\n![研报图表 2](assets/xhs\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n折扣零售正在改写超市格局\n\n**折扣超市崛起**\n\n折扣超市不再是“廉价”的代名词，它们正在变大、变潮，甚至能抢走一半市场。\n\n**1/ 折扣超市变了样**\n过去十年，折扣超市从“简陋小店”进化成“品质选择”。它们开更大的店，卖更多生鲜和有机产品，自有品牌甚至能在盲测中击败大牌。价格依然便宜15%-200%，但体验感拉满：充电桩、现烤面包、限时新品……消费者开始问：“凭什么我要多花钱？”\n\n**2/ 它们抢走了谁？**\n在成熟市场（如德国、挪威），折扣超市已占超35%份额。在扩张市场（波兰、比利时），它们占据10%-40%。连美国这种“空白市场”，Aldi和Lidl都在疯狂开店。数据很直接：传统超市利润从5%+跌到3%以下，折扣超市却靠高效运营赚更多。\n\n**3/ 传统超市怎么办？**\n方案一：彻底改造自己。降价、优化品类、升级门店体验，不是小修小补，而是大转型。\n方案二：自己推出折扣子品牌。但需要独立运营，甚至换一套文化和思维，投入不小。\n\n**4/ 折扣超市别飘**\n扩张太快会毁掉简单高效的模型。进入新市场前，必须吃透当地需求，保持供应链优势。别为了“更好看”牺牲效率。\n\n**最后一句**\n折扣超市的崛起\n\n[... middle omitted ...]\n\nclients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with 85 offices in 48 countries. For \n\n[... middle omitted ...]\n\n Paulo\n\nMontréal\n\nIstanbul\n\nShanghai\nSingapore\nStockholm\nStuttgart\nSydney\nTaipei\nTel Aviv\nTokyo\nToronto\nVienna\nWarsaw\nWashington\nZurich\n\nCasablanca\n\nJakarta\n\nChennai\n\nSeattle\n\nJohannesburg\n\nMoscow\n\nMumbai\n\nSeoul\n\nbcg.com"
  },
  {
    "id": "R094",
    "title": "波士顿咨询：超市运营利润提升1-3个百分点的秘密，不是降本，而是重置流程",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：超市运营利润提升1-3个百分点的秘密，不是降本，而是重置流程\n\n传统超市正面临折扣店、会员店和电商的多面夹击，多数人的应对方法是供应链降本、门店减员、减少损耗。但波士顿咨询一份深度研报指出，这条路走不通。报告的核心判断是：传统超市真正需要的不是零敲碎打的优化，而是一场以顾客为起点的运营模式重置。这不是一个效率改善项目，而是一次战略级重构。\n\n报告认为，那些敢于从顾客真实需求出发、重新设计端到端流程的超市，有机会将运营利润率提升1到3个百分点。这个数字听起来不大，但放在整个行业，意味着可以腾出数十亿美元重新投入价格、服务和体验，而这恰恰是传统超市生存的关键。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 多数超市的优化方向一开始就错了\n\n波士顿咨询发现，传统超市的普遍问题不是不努力，而是努力的方向偏了。大多数企业把目标框定在“降低成本”和“提升效率”上，结果往往是每个部门都在自己的孤井里做优化：供应链团队压缩库存，门店团队削减工时，损耗团队盯着过期商品。这些动作各自有道理，但放在一起，反而可能损害顾客体验。\n\n报告举了一个典型案例：一家欧洲超市因SKU过多导致补货效率下降、库存成本上升，同时顾客面对琳琅满目的货架反而感到困惑。传统的做法可能是进一步削减SKU或压缩补货人手，但波士顿咨询的建议是成立跨职能团队，从顾客需求出发重新梳理品类结构、优化货架布局、与供应商重新谈判。结果顾客满意度提升，品类销售额实现个位数增长，毛利率显著改善，从配送中心到门店的端到端运营成本也下降了两位数。\n\n这个案例说明一个道理：当优化目标从“省钱”转向“让顾客满意”，反而更容易找到成本与体验的双赢点。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 真正的杠杆藏在端到端流程里，不是单一职能\n\n报\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n传统超市的转型密码：从顾客出发\n\n顾客说了算\n\n传统超市正面临折扣店、电商、即时配送的多重挤压。但很多超市的应对方式是做“部门级优化”——供应链省点钱、门店减点人、损耗降一点。这些动作有用，但不够。\n\n投行研报给出一个更本质的解法：**以顾客为中心的运营重置**。核心不是内部省钱，而是先搞清楚顾客到底为什么买单。\n\n1/ 顾客要的不是“价值”或“选择多”\n这两个词太虚。真正有用的是颗粒度够细的需求。\n比如烘焙区，顾客要的是“早上7点到晚上7点，都能买到刚出炉的、有酥脆外皮的面包”。这才叫可执行的顾客价值。\n\n2/ 端到端（E2E）流程改造\n把每个环节拆开看：从选品、陈列、补货到门店运营。哪些动作是在创造顾客价值？哪些是内部浪费？\n案例：某欧洲超市SKU太多，货架塞满，顾客反而挑花眼。跨部门团队重新梳理品类结构，精简SKU，用标准化托盘提高补货效率。结果：顾客满意度提升，品类销售个位数增长，毛利率显著改善，从配送到门店的运营成本双位数下降。\n\n3/ 让改变“粘得住”\n很多变革项目轰轰烈烈开始，三个月后打回原形。关键有三：\n- 结构化推进：把大目标拆成每周每天的具体动作，有节点可庆祝。\n- 团队共鸣：让员工\n\n[... middle omitted ...]\n\nansform their operations if they are to navigate through these dislocations. So far, however, many grocers have focused on incremental change within each function, while hesitating to make the\n\n[... middle omitted ...]\n\ning results. Founded in 1963, BCG is a private company with offices in more than 90 cities in 50 countries. For more information, please visit bcg.com.\n\n© The Boston Consulting Group, Inc. 2018. All rights reserved. 4/18"
  },
  {
    "id": "R095",
    "title": "波士顿咨询：超市行业新战场，不是价格战而是品牌战，折扣店已领先15年",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：超市行业新战场，不是价格战而是品牌战，折扣店已领先15年\n\n传统超市的自有品牌业务正面临一个尴尬的转折点。它们拥有大量SKU，却既无法在品质上追赶国家品牌，也无法在价格上匹敌折扣店的内生品牌。波士顿咨询最新报告指出，问题的根源不在于产品本身，而在于运营逻辑——超市需要从“卖货渠道”转变为“品牌经营者”。\n\n报告的核心判断相当尖锐：传统超市目前的自有品牌策略，是“最差的两个世界”——既没有国家品牌的资产价值，也无法在价格或品质上击败折扣店。而折扣店如Aldi、Lidl、Mercadona的成功，恰恰证明了一件事：当超市像消费品牌一样思考时，它们能同时实现差异化、降低成本并提高客户忠诚度。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 折扣店正在用“品牌思维”重塑行业规则\n\n报告以服装行业为类比，指出多品牌零售商（如百货公司）的困境正在超市行业重演。Zara和H&M通过控制从设计到门店的全链条，实现了更短的交付周期和更低的成本。折扣超市正在做同样的事：它们开发自己的产品，控制生产（Lidl甚至自产冰淇淋和巧克力），并通过更少的SKU实现更高效的供应链。\n\n以蛋黄酱品类为例，传统超市的SKU数量是折扣店的3-5倍，但价格区间却更宽，从0.75美元到5.77美元不等。而折扣店的价格集中在0.75-1.99美元，且自有品牌占比高达71%。这种简化不仅降低了运营成本，还让消费者在更低的价格点上获得了不逊于国家品牌的品质。\n\n> **KC评论：** 这张表格值得细看。它揭示了传统超市的“复杂性陷阱”：为了覆盖所有价格带，它们不得不增加SKU，但每个SKU的销量和利润都不足以支撑其存在。折扣店的选择是“少而精”，用爆款逻辑替代全覆盖逻辑。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2.\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n传统超市正在被“自己”打败\n\n**自有品牌，不是贴牌**\n\n超市的货架，正在被自己堆垮。\n\n某外资投行最新研报指出：传统超市的自有品牌，SKU又多又杂，既打不过品牌商，又拼不过折扣店。而像Aldi、Lidl、Mercadona这类“硬折扣玩家”，靠的是少而精的**零售商品牌**，不是简单的贴牌。\n\n1/ **折扣店赢在哪？**\n- 它们像CPG公司一样思考：自己研发、自己生产、自己卖。\n- 每个品类只做1-2个SKU，但品质对标大牌，价格低50%-75%。\n- 供应链极简，门店运营成本极低。\n\n2/ **传统超市的致命伤**\n- 为了对抗折扣店，传统超市推出多层级自有品牌：入门款、有机款、高端款...\n- 结果SKU爆炸，规模效应丧失，库存复杂，利润被吃掉。\n- 既没有品牌商的溢价能力，也没有折扣店的成本优势。\n\n3/ **真正的解法：从“自有品牌”升级为“零售商品牌”**\n- 不是简单贴个超市Logo，而是针对品类打造独立的消费者品牌。\n- 比如Mercadona的Deliplus（美妆）直接超越欧莱雅，Hacendado（食品）是西班牙家庭首选。\n- 关键：基于消费者洞察做研发，而不是跟风上架。\n\n4/ \n\n[... middle omitted ...]\n\nCPG offerings, grocers can differentiate themselves from their peers, better engage with their customers, and drive down operating costs across the entire value chain, from production to in-st\n\n[... middle omitted ...]\n\ning results. Founded in 1963, BCG is a private company with offices in more than 90 cities in 50 countries. For more information, please visit bcg.com.\n\n© The Boston Consulting Group, Inc. 2018. All rights reserved. 4/18"
  },
  {
    "id": "R096",
    "title": "麦肯锡：全球资产负债表显示，过去20年财富增长七成来自通胀",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "麦肯锡",
    "digest": "[wechat_article.md]\n# 麦肯锡：全球资产负债表显示，过去20年财富增长七成来自通胀\n\n麦肯锡全球研究院在2025年年末发布的年度图表总结，没有停留在罗列数据，而是给出了一个反直觉的判断：全球生产率增长的引擎，不是广泛的企业群体，而是极少数“杰出公司”。在三个国家的8300家大型企业中，不到100家公司贡献了63%的生产率增长。这个发现推翻了“涓滴式进步”的传统叙事，也让决策者和读者不得不重新思考——真正驱动宏观环境效率的，到底是什么力量。\n\n这份报告覆盖了生产率、全球贸易、技术变革、能源转型和人口结构五大主题。但最值得关注的，不是每个领域的独立进展，而是它们共同指向的一个核心矛盾：全球宏观环境的“账面财富”在膨胀，但真实的生产性研究并未跟上。麦肯锡构建的全球资产负债表显示，2000年至2024年间，全球家庭财富增加了400万亿美元，但其中约四分之三来自资产价格重估和通胀，而非新增储蓄和研究。这意味着，过去二十年的财富增长，相当一部分是“写在纸上的”。\n\n> **KC评论：** 麦肯锡的全球资产负债表是一个很有价值的分析框架。它提醒我们，不要被资产价格的上涨所迷惑，真正支撑长期繁荣的是实物研究和生产率提升。这份报告里对“账面财富”和“真实研究”的拆解，值得仔细研究。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 生产率增长的主角是“少数派”，而非“多数派”\n\n麦肯锡的研究发现，生产率进步并非均匀分布。在三个国家的研究样本中，那些被称为“杰出公司”的企业，其生产率增长往往以爆发式的方式实现，而非渐进的改善。这些公司通过大胆的战略举措、收入增长和业务组合调整来推动进步，而非单纯依赖效率提升。这一发现挑战了传统宏观环境学中“生产率进步来自大多数企业缓慢改善”的假设。对于政策制定者而言，这意味着支持“明星企业”的成长环境，可能比试图提升所有企业的平均\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n全球生产力真相：少数公司撑起大半江山\n\n少数公司撑起大半江山\n\n全球生产力格局正在被极少数公司改写\n\n📌 今天想聊聊某外资投行最新研报里的几个有意思的发现，信息密度高，建议收藏慢慢看。\n\n1️⃣ 少数公司才是生产力引擎\n- 研究覆盖8300家大型企业，发现不到100家公司贡献了63%的生产力增长\n- 这些“杰出企业”通过大胆战略布局和业务组合调整实现爆发式增长，而非渐进式改善\n- 生产力进步是“少数公司走一英里”，而不是“多数公司挪一英寸”\n\n2️⃣ 全球财富增长背后的“纸面游戏”\n- 2000-2024年，全球家庭财富增长约400万亿美元\n- 但其中仅约100万亿来自实际净投资，其余75%是资产价格膨胀和通胀带来的“纸面财富”\n- 这些增长并未完全由经济基本面支撑\n\n3️⃣ 贸易格局正在“缩近距离”\n- 2017-2024年，贸易的地缘政治距离下降了约7%\n- 中美德等经济体之间贸易往来的地缘政治距离明显缩短\n- 但地理距离反而在缓慢增加，每年约10公里\n\n4️⃣ AI与机器人正在重塑工作方式\n- 现有技术下，AI代理可完成44%的美国工作时长，机器人可完成13%\n- 但超过70%的人类技能在自动化和非自动\n\n[... middle omitted ...]\n\nnce-sheet health and drive prosperity. We explored ways in which the private sector could help lift more people above an “empowerment line” to meet essential needs and otherwise advance beyond\n\n[... middle omitted ...]\n\nany\n\nDesigned by the McKinsey Global Institute\n\nmckinsey.com/mgi\n\nX @McKinsey\\_MGI\n\n@McKinseyGlobalInstitute\n\nin @McKinseyGlobalInstitute\n\nSubscribe to MGI's LinkedIn newsletter,\n\nForward Thinking: mck.co/forwardthinking"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 2: As AI transitions from a training-heavy era (dominated by GPUs) to an inference-heavy era, the role of CPUs expands. Training requires parallel processing, but inference and specifically agentic workflows requires the se"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 2: As AI transitions from a training-heavy era (dominated by GPUs) to an inference-heavy era, the role of CPUs expands. Training requires parallel processing, but inference and specifically agentic workflows requires the se"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 2: As AI transitions from a training-heavy era (dominated by GPUs) to an inference-heavy era, the role of CPUs expands. Training requires parallel processing, but inference and specifically agentic workflows requires the se"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 4: The expansion of the TAM is driven by three core factors, each of which is expected to accelerate in the second half of this decade relative to the past 5 years Driver 1: Global server CPU shipment vol (Mn units)"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "EXHIBIT 4",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 4: The expansion of the TAM is driven by three core factors, each of which is expected to accelerate in the second half of this decade relative to the past 5 years Driver 1: Global server CPU shipment vol (Mn units) Drive"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "EXHIBIT 5",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 5: 2030 TAM Sensitivity Analysis: Even in a bear-case scenario, the global memory interface chip TAM reaches our prior-version projection, reinforcing a well-protected downside for Montage at current share price"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "EXHIBIT 5",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 5: 2030 TAM Sensitivity Analysis: Even in a bear-case scenario, the global memory interface chip TAM reaches our prior-version projection, reinforcing a well-protected downside for Montage at current share price ## PRODUCT"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: Among all DRAM variants, DDR packaged in DIMMs requires RCD/MRCD and DB/MDB to interface with server CPUs, while LPDDR used by NVIDIA Vera CPUs also needs some simplified memory interface chips"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 8: Memory interface chip: core networking chip to connect CPU and DRAM in servers to support more memory capacity/bandwidth"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "EXHIBIT 8",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 8: Memory interface chip: core networking chip to connect CPU and DRAM in servers to support more memory capacity/bandwidth ## DRAM for PC and low-end servers: CPU connect to DRAM directly \\- Limited requirement on the DRAM"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 9: Logic diagram for RCD, including a MCU EXHIBIT 10: Logic diagram for DB chips EXHIBIT 11: The mechanism of MRCD and MDB in MRDIMM: MRCD allows simultaneous access to both ranks, and MDB enables muxing and demuxing. H"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 9: Logic diagram for RCD, including a MCU EXHIBIT 10: Logic diagram for DB chips EXHIBIT 11: The mechanism of MRCD and MDB in MRDIMM: MRCD allows simultaneous access to both ranks, and MDB enables muxing and demuxing. H"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "EXHIBIT 10",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 10: Logic diagram for DB chips EXHIBIT 11: The mechanism of MRCD and MDB in MRDIMM: MRCD allows simultaneous access to both ranks, and MDB enables muxing and demuxing. Hence, two DDR ranks run in a multiplexed mode to doub"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "EXHIBIT 12",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 12: DDR5 module introduces a SPD Hub, which stores configuration information in the EEPROM EXHIBIT 13: DDR5 temperature sensors must achieve \\~0.25 °C accuracy to trigger effective thermal management actions, including low"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "EXHIBIT 14",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 14: Upgrading to DDR5 introduces an on-module PMIC, which improves power efficiency while reducing vulnerability to power noise on the motherboard DDR4 DIMM DDR5 DIMM ## PC DDR MODULE FORMATS AND CKD While this report main"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 16: Our TAM model follows a bottom-up approach, reflecting the impacts of three drivers on five multiplicative factors ## INCREASING SERVER CPU SHIPMENTS We project global server CPU shipment volumes (excluding NVIDIA's pr"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "EXHIBIT 17",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 18: CPU under-provisioning leaves GPUs idle. Adding CPU cores is cost-effective to improve performance. Because CPU cores are approximately 100–1,600x cheaper than GPU compute, increasing the CPU allocation typically adds on"
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "EXHIBIT 18",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 18: CPU under-provisioning leaves GPUs idle. Adding CPU cores is cost-effective to improve performance. Because CPU cores are approximately 100–1,600x cheaper than GPU compute, increasing the CPU allocation typically adds on"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "EXHIBIT 19",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 20: The transition from 8-channel to 16-channel DDR architectures has potential to double memory interface content required per CPU By contrast, general-purpose servers leave roughly half of memory slots empty (\\~50% occup"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "EXHIBIT 21",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 21: AI servers utilize nearly all DIMM slots to maximize accelerator performance, while traditional servers prioritize TCO and leave many slots unpopulated. The shift toward AI servers will drive higher average DIMM slot occ"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "EXHIBIT 21",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 21: AI servers utilize nearly all DIMM slots to maximize accelerator performance, while traditional servers prioritize TCO and leave many slots unpopulated. The shift toward AI servers will drive higher average DIMM slot occ"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "Exhibit 23",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 22: The spec upgrade of MRDIMM versus RDIMM Comparison of Traditional RDIMM and MRDIMM in Terms of Specifications Comparison of RDIMM vs. MRDIMM ## TrendForce"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "EXHIBIT 24",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 26: MRDIMM adoption in the DDR5 era will nearly triple memory interface chips dollar content per module. We expect MRDIMM penetration to surpass 25% by 2030, a level that remains modest compared with the adoption trajectory"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "EXHIBIT 24",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 26: MRDIMM adoption in the DDR5 era will nearly triple memory interface chips dollar content per module. We expect MRDIMM penetration to surpass 25% by 2030, a level that remains modest compared with the adoption trajectory"
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "EXHIBIT 26",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 26: MRDIMM adoption in the DDR5 era will nearly triple memory interface chips dollar content per module. We expect MRDIMM penetration to surpass 25% by 2030, a level that remains modest compared with the adoption trajectory"
  },
  {
    "figure_id": "F026",
    "report_id": "R001",
    "label": "EXHIBIT 26",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 26: MRDIMM adoption in the DDR5 era will nearly triple memory interface chips dollar content per module. We expect MRDIMM penetration to surpass 25% by 2030, a level that remains modest compared with the adoption trajectory"
  },
  {
    "figure_id": "F027",
    "report_id": "R001",
    "label": "EXHIBIT 27",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 27: Intel led the migration to MRDIMM with Granite Rapids in 2H24, while AMD enters directly to MRDIMM Gen2 in 2026, with Venice as the first MRDIMM-capable platform EXHIBIT 28: DRAM suppliers have established solid MRDIMM"
  },
  {
    "figure_id": "F028",
    "report_id": "R001",
    "label": "EXHIBIT 27",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 27: Intel led the migration to MRDIMM with Granite Rapids in 2H24, while AMD enters directly to MRDIMM Gen2 in 2026, with Venice as the first MRDIMM-capable platform EXHIBIT 28: DRAM suppliers have established solid MRDIMM"
  },
  {
    "figure_id": "F029",
    "report_id": "R001",
    "label": "EXHIBIT 29",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 29: The core memory interface chips market is a textbook oligopoly, with top 3 players consolidating 90+% of market share Market landscape of the core memory interface chips in 2024 ## COMPLEMENTARY SUPPORTING CHIPS: A MOR"
  },
  {
    "figure_id": "F030",
    "report_id": "R001",
    "label": "EXHIBIT 30",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 30: Besides the three leading players with full chipsets, a range of analog and discrete suppliers also provide complementary supporting chips ## EVALUATION OF THREE CORE MEMORY INTERFACE CHIP PLAYERS Montage, Renesas, and"
  },
  {
    "figure_id": "F031",
    "report_id": "R001",
    "label": "EXHIBIT 31",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 31: Three industry leaders remain closely matched in DDR5 RDIMM and MRDIMM offerings. However, Montage and Renesas hold a first-mover advantage in MRDIMM memory interface chips Renesas' Memory Interface Management Outlook"
  },
  {
    "figure_id": "F032",
    "report_id": "R001",
    "label": "Exhibit 32",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 32: Renesas' AI Infrastructure - Mid-to-Long Revenue Target EXHIBIT 33: Within AI infrastructure, Renesas' Memory Interface ICs' Mid-Term Revenue Target EXHIBIT 34: Renesas - Memory Interface ICs Revenue Trend"
  },
  {
    "figure_id": "F033",
    "report_id": "R001",
    "label": "Exhibit 32",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 32: Renesas' AI Infrastructure - Mid-to-Long Revenue Target EXHIBIT 33: Within AI infrastructure, Renesas' Memory Interface ICs' Mid-Term Revenue Target EXHIBIT 34: Renesas - Memory Interface ICs Revenue Trend Renesas -"
  },
  {
    "figure_id": "F034",
    "report_id": "R001",
    "label": "EXHIBIT 34",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 34: Renesas - Memory Interface ICs Revenue Trend Renesas - Memory Interface ICs Revenue Growth EXHIBIT 35: Renesas' AI Infrastructure Revenue by Product Renesas' AI Infrastructure Revenue by Product Timing clock IC reven"
  },
  {
    "figure_id": "F035",
    "report_id": "R001",
    "label": "EXHIBIT 35",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 35: Renesas' AI Infrastructure Revenue by Product Renesas' AI Infrastructure Revenue by Product Timing clock IC revenue is excluded from February 2026 onward following Renesas' divestiture of the business to SiTime (SITM,"
  },
  {
    "figure_id": "F036",
    "report_id": "R001",
    "label": "EXHIBIT 36",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 36: Well-established ecosystem ties and close collaboration requirements have formed high barriers that safeguard incumbents in the core memory interface chips sector ## MEMORY INTERFACE CHIP ECOSYSTEM High Barriers. Deep In"
  },
  {
    "figure_id": "F037",
    "report_id": "R001",
    "label": "EXHIBIT 36",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 36: Well-established ecosystem ties and close collaboration requirements have formed high barriers that safeguard incumbents in the core memory interface chips sector ## MEMORY INTERFACE CHIP ECOSYSTEM High Barriers. Deep In"
  },
  {
    "figure_id": "F038",
    "report_id": "R001",
    "label": "EXHIBIT 36",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 36: Well-established ecosystem ties and close collaboration requirements have formed high barriers that safeguard incumbents in the core memory interface chips sector ## MEMORY INTERFACE CHIP ECOSYSTEM High Barriers. Deep In"
  },
  {
    "figure_id": "F039",
    "report_id": "R001",
    "label": "EXHIBIT 37",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 38: Alibaba is one of the pioneers in adopting CXL for AIDC"
  },
  {
    "figure_id": "F040",
    "report_id": "R001",
    "label": "EXHIBIT 38",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 39: The potential TAM of CXL chips can reach USD 1.7Bn by 2030, though the deployment timeline remains uncertain"
  },
  {
    "figure_id": "F041",
    "report_id": "R001",
    "label": "EXHIBIT 38",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 39: The potential TAM of CXL chips can reach USD 1.7Bn by 2030, though the deployment timeline remains uncertain"
  },
  {
    "figure_id": "F042",
    "report_id": "R001",
    "label": "EXHIBIT 39",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 39: The potential TAM of CXL chips can reach USD 1.7Bn by 2030, though the deployment timeline remains uncertain ## SOCAMM2 - NVIDIA BESPOKE DRAM FORMAT FOR ITS CPU PLATFORMS In our latest SOCAMM2 report, we argue that NVI"
  },
  {
    "figure_id": "F043",
    "report_id": "R001",
    "label": "EXHIBIT 40",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 40: Spec comparison across DDR5 RDIMM, MRDIMM, and SOCAMM2 ## EXHIBIT 41: configuration comparison between SOCAMM2 and DDR5 RDIMM \\- \\~133mm x \\~31mm x \\~2.5mm • 288 pins on edge connector"
  },
  {
    "figure_id": "F044",
    "report_id": "R001",
    "label": "EXHIBIT 41",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 41: configuration comparison between SOCAMM2 and DDR5 RDIMM \\- \\~133mm x \\~31mm x \\~2.5mm • 288 pins on edge connector • Vertical, insertion socket"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "EXHIBIT 7",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: French hydropower production EXHIBIT 8: French water reservoir and hydro storage levels (TWh) ## TOTAL PRODUCTION EXHIBIT 9: France's power production (TWh)"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "EXHIBIT 14",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 14: Hydropower production EXHIBIT 15: Spain - Water reservoirs and hydro storage levels (TWh) ## TOTAL PRODUCTION EXHIBIT 16: Spain's power production"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "EXHIBIT 21",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 21: Hydropower production EXHIBIT 22: Portugal – Water reservoirs and hydro storage levels (TWh) ## TOTAL PRODUCTION EXHIBIT 23: Portugal - Total production"
  },
  {
    "figure_id": "F048",
    "report_id": "R002",
    "label": "EXHIBIT 37",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 37: Hydro pumped storage production (TWh) in Austria EXHIBIT 38: Austrian water reservoir and hydro storage levels (TWh) ## ITALY We note that the format of ENTSOE and Terna data for Italy appears to have changed between 2"
  },
  {
    "figure_id": "F049",
    "report_id": "R002",
    "label": "EXHIBIT 43",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 43: Italy – Water reservoirs and hydro storage levels (TWh) ## TOTAL PRODUCTION EXHIBIT 44: Italy power production"
  },
  {
    "figure_id": "F050",
    "report_id": "R002",
    "label": "EXHIBIT 52",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 52: Estimated load factor based on power production and average capacity EXHIBIT 53: Finland – Water reservoirs and hydro storage levels (TWh) ## TOTAL PRODUCTION EXHIBIT 54: Finland power production"
  },
  {
    "figure_id": "F051",
    "report_id": "R002",
    "label": "EXHIBIT 55",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 57: 1H European power demand (Germany, France, Italy, Spain and Great Britain)"
  },
  {
    "figure_id": "F052",
    "report_id": "R002",
    "label": "EXHIBIT 57",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 57: 1H European power demand (Germany, France, Italy, Spain and Great Britain) EXHIBIT 58: European Union monthly power demand (TWh) ## GAS DEMAND AND SUPPLY"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "EXHIBIT 57",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 59: Europe\\* total gas demand (mcm/d)"
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "EXHIBIT 59",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 59: Europe\\* total gas demand (mcm/d) EXHIBIT 60: Europe\\* industrial gas demand (mcm/d) EXHIBIT 61: Europe\\* LDZ gas demand (mcm/d)"
  },
  {
    "figure_id": "F055",
    "report_id": "R002",
    "label": "EXHIBIT 59",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 59: Europe\\* total gas demand (mcm/d) EXHIBIT 60: Europe\\* industrial gas demand (mcm/d) EXHIBIT 61: Europe\\* LDZ gas demand (mcm/d) EXHIBIT 62: Europe\\* gas-to-power gas demand (mcm/d)"
  },
  {
    "figure_id": "F056",
    "report_id": "R002",
    "label": "EXHIBIT 60",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 60: Europe\\* industrial gas demand (mcm/d) EXHIBIT 61: Europe\\* LDZ gas demand (mcm/d) EXHIBIT 62: Europe\\* gas-to-power gas demand (mcm/d) EXHIBIT 63: Gas storage levels stands at 50% of total capacity"
  },
  {
    "figure_id": "F057",
    "report_id": "R002",
    "label": "EXHIBIT 61",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 61: Europe\\* LDZ gas demand (mcm/d) EXHIBIT 62: Europe\\* gas-to-power gas demand (mcm/d) EXHIBIT 63: Gas storage levels stands at 50% of total capacity EXHIBIT 64: German industrial gas demand (TWh) (over 26 weeks) Ger"
  },
  {
    "figure_id": "F058",
    "report_id": "R002",
    "label": "EXHIBIT 62",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 62: Europe\\* gas-to-power gas demand (mcm/d) EXHIBIT 63: Gas storage levels stands at 50% of total capacity EXHIBIT 64: German industrial gas demand (TWh) (over 26 weeks) Germany industry annual demand (TWh) EXHIBIT 65"
  },
  {
    "figure_id": "F059",
    "report_id": "R002",
    "label": "EXHIBIT 63",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 63: Gas storage levels stands at 50% of total capacity EXHIBIT 64: German industrial gas demand (TWh) (over 26 weeks) Germany industry annual demand (TWh) EXHIBIT 65: Germany: weekly industrial gas consumption Industrial"
  },
  {
    "figure_id": "F060",
    "report_id": "R002",
    "label": "EXHIBIT 64",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 66: LNG tankers crossing the strait of Hormuz"
  },
  {
    "figure_id": "F061",
    "report_id": "R002",
    "label": "Exhibit 66",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 66: LNG tankers crossing the strait of Hormuz EXHIBIT 67: LNG Transits (number of vessels) EXHIBIT 68: Commercial shipping routes"
  },
  {
    "figure_id": "F062",
    "report_id": "R002",
    "label": "Exhibit 66",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 66: LNG tankers crossing the strait of Hormuz EXHIBIT 67: LNG Transits (number of vessels) EXHIBIT 68: Commercial shipping routes Note: Voyage time is calculated for laden Suezmax tankers traveling at 14 knots without"
  },
  {
    "figure_id": "F063",
    "report_id": "R002",
    "label": "EXHIBIT 67",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 67: LNG Transits (number of vessels) EXHIBIT 68: Commercial shipping routes Note: Voyage time is calculated for laden Suezmax tankers traveling at 14 knots without extended chokepoint delays. ## I. REQUIRED DISCLOSURES"
  },
  {
    "figure_id": "F064",
    "report_id": "R003",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "While disrupted supply chains can explain part of today's disconnect, the more important distortion is the release of government strategic reserves distorting commercial inventories (Exhibit 6) plus perhaps some ability of the Trump administration to verbally "
  },
  {
    "figure_id": "F065",
    "report_id": "R003",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 2: Pre-shale crack spreads were a fifth (20%) and post-shale crack spreads are a third (33%)"
  },
  {
    "figure_id": "F066",
    "report_id": "R003",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 2: Pre-shale crack spreads were a fifth (20%) and post-shale crack spreads are a third (33%) If crack spreads are defined as: $$ \\text { Crack } = (2 \\times \\text { Gas } + 1 \\times \\text { Diesel } - 3 \\times \\text { Oil"
  },
  {
    "figure_id": "F067",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 3: Back-solving for oil price from gasoline and diesel yields good fit EXHIBIT 4: Post Covid-era...crack-implied oil price during Russia-Ukraine war was elevated \\~10%...today's elevation is massive."
  },
  {
    "figure_id": "F068",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 3: Back-solving for oil price from gasoline and diesel yields good fit EXHIBIT 4: Post Covid-era...crack-implied oil price during Russia-Ukraine war was elevated \\~10%...today's elevation is massive. EXHIBIT 6: Oil pr"
  },
  {
    "figure_id": "F069",
    "report_id": "R003",
    "label": "EXHIBIT 4",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 4: Post Covid-era...crack-implied oil price during Russia-Ukraine war was elevated \\~10%...today's elevation is massive. EXHIBIT 6: Oil prices embed commercial (OECD in this case) inventories and seemingly ignore strate"
  },
  {
    "figure_id": "F070",
    "report_id": "R003",
    "label": "EXHIBIT 5",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 6: Oil prices embed commercial (OECD in this case) inventories and seemingly ignore strategic (government) inventories such as SPRs O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspe"
  },
  {
    "figure_id": "F071",
    "report_id": "R004",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 3: ... across all regions, we now see Gucci largely straddling the pricing umbrella formed between the ‘accessible luxury’ price points (exemplified by Burberry) and the more crowded ‘core luxury’ price points occupied by P"
  },
  {
    "figure_id": "F072",
    "report_id": "R004",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 4: However, this readjustment in pricing architecture will likely generate near-term price-mix headwinds on organic growth performance"
  },
  {
    "figure_id": "F073",
    "report_id": "R004",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 6: Fashion media articles with static advertisements published prior to the Mercato's price change in early-May provide further evidence of Gucci's price change, with static prices listed on media outlets (left) differing f"
  },
  {
    "figure_id": "F074",
    "report_id": "R004",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: Coach - Histogram - France Weekly Handbag Mix Changes - Histogram Coach, in France - (03-Jul-26)"
  },
  {
    "figure_id": "F075",
    "report_id": "R004",
    "label": "EXHIBIT 7",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: Coach - Histogram - France Weekly Handbag Mix Changes - Histogram Coach, in France - (03-Jul-26) EXHIBIT 8: Burberry - Histogram - France Weekly Handbag Mix Changes - Histogram Burberry, in France - (03-Jul-26) EXHIB"
  },
  {
    "figure_id": "F076",
    "report_id": "R004",
    "label": "EXHIBIT 8",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 8: Burberry - Histogram - France Weekly Handbag Mix Changes - Histogram Burberry, in France - (03-Jul-26) EXHIBIT 9: Gucci - Histogram - France Weekly Handbag Mix Changes - Histogram Gucci, in France - (03-Jul-26) EXHIB"
  },
  {
    "figure_id": "F077",
    "report_id": "R004",
    "label": "EXHIBIT 8",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 8: Burberry - Histogram - France Weekly Handbag Mix Changes - Histogram Burberry, in France - (03-Jul-26) EXHIBIT 9: Gucci - Histogram - France Weekly Handbag Mix Changes - Histogram Gucci, in France - (03-Jul-26) EXHIB"
  },
  {
    "figure_id": "F078",
    "report_id": "R004",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: Prada - Histogram - France"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "EXHIBIT 10",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 12: Louis Vuitton - Histogram - France EXHIBIT 13: Dior - Histogram - France Weekly Handbag Mix Changes - Histogram Dior, in France - (03-Jul-26)"
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "EXHIBIT 11",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: Prada - Histogram - France EXHIBIT 12: Louis Vuitton - Histogram - France EXHIBIT 13: Dior - Histogram - France Weekly Handbag Mix Changes - Histogram Dior, in France - (03-Jul-26) EXHIBIT 14: Chanel - Histogram - Fr"
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "EXHIBIT 11",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: Prada - Histogram - France EXHIBIT 12: Louis Vuitton - Histogram - France EXHIBIT 13: Dior - Histogram - France Weekly Handbag Mix Changes - Histogram Dior, in France - (03-Jul-26) EXHIBIT 14: Chanel - Histogram - Fr"
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "EXHIBIT 13",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 15: Coach - Histogram - France Weekly Handbag Mix Changes - Histogram Coach, in France - (26-Jun-26)"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "EXHIBIT 15",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 15: Coach - Histogram - France Weekly Handbag Mix Changes - Histogram Coach, in France - (26-Jun-26) EXHIBIT 16: Burberry - Histogram - France Weekly Handbag Mix Changes - Histogram Burberry, in France - (26-Jun-26) EXHIBI"
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "EXHIBIT 16",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 16: Burberry - Histogram - France Weekly Handbag Mix Changes - Histogram Burberry, in France - (26-Jun-26) EXHIBIT 17: Gucci - Histogram - France Weekly Handbag Mix Changes - Histogram Gucci, in France - (26-Jun-26) EXHI"
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "EXHIBIT 16",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 19: Prada - Histogram - France"
  },
  {
    "figure_id": "F086",
    "report_id": "R004",
    "label": "EXHIBIT 18",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 20: Louis Vuitton - Histogram - France"
  },
  {
    "figure_id": "F087",
    "report_id": "R004",
    "label": "EXHIBIT 18",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 20: Louis Vuitton - Histogram - France Weekly Handbag Mix Changes - Histogram Dior, in France - (26-Jun-26) EXHIBIT 21: Dior - Histogram - France"
  },
  {
    "figure_id": "F088",
    "report_id": "R004",
    "label": "EXHIBIT 19",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 22: Chanel - Histogram - France"
  },
  {
    "figure_id": "F089",
    "report_id": "R004",
    "label": "EXHIBIT 20",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 20: Louis Vuitton - Histogram - France Weekly Handbag Mix Changes - Histogram Dior, in France - (26-Jun-26) EXHIBIT 21: Dior - Histogram - France EXHIBIT 22: Chanel - Histogram - France Weekly Handbag Mix Changes - Histo"
  },
  {
    "figure_id": "F090",
    "report_id": "R004",
    "label": "EXHIBIT 21",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 21: Dior - Histogram - France EXHIBIT 22: Chanel - Histogram - France Weekly Handbag Mix Changes - Histogram Chanel, in France - (26-Jun-26) ## I. REQUIRED DISCLOSURES Bernstein is part of a joint venture between SG (SG)"
  },
  {
    "figure_id": "F091",
    "report_id": "R005",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 1: European Defense has been extremely volatile since 2025... EU Defense Coverage Average Performance, since Jan 2025, in € EXHIBIT 2: ... But most stocks are trading in line with the early 2026 valuations EU Defense Cove"
  },
  {
    "figure_id": "F092",
    "report_id": "R005",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 1: European Defense has been extremely volatile since 2025... EU Defense Coverage Average Performance, since Jan 2025, in € EXHIBIT 2: ... But most stocks are trading in line with the early 2026 valuations EU Defense Cove"
  },
  {
    "figure_id": "F093",
    "report_id": "R005",
    "label": "EXHIBIT 5",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 5: Cyber will face easier comps from Q2'26 Cyber - Quarterly Revenue yoy Growth EXHIBIT 6: Thales: Q2'26 preview"
  },
  {
    "figure_id": "F094",
    "report_id": "R005",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: ...and operating profits Rheinmetall - Bernstein Operating Profit Estimates vs. VA Consensus, in €m"
  },
  {
    "figure_id": "F095",
    "report_id": "R005",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: ...and operating profits Rheinmetall - Bernstein Operating Profit Estimates vs. VA Consensus, in €m Indicative percentage of the difference between Bernstein's estimates and VA consensus"
  },
  {
    "figure_id": "F096",
    "report_id": "R005",
    "label": "EXHIBIT 10",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: ...and operating profits Rheinmetall - Bernstein Operating Profit Estimates vs. VA Consensus, in €m Indicative percentage of the difference between Bernstein's estimates and VA consensus EXHIBIT 12: Rheinmetall: Q2'26"
  },
  {
    "figure_id": "F097",
    "report_id": "R006",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 3: Although inflation expectations rose sharply following the West Asia conflict, the recent ceasefire is expected to ease concerns and support a moderation in inflation expectations India - Inflation expectations (%)"
  },
  {
    "figure_id": "F098",
    "report_id": "R006",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 3: Although inflation expectations rose sharply following the West Asia conflict, the recent ceasefire is expected to ease concerns and support a moderation in inflation expectations India - Inflation expectations (%)"
  },
  {
    "figure_id": "F099",
    "report_id": "R006",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 4: India's merchandise trade deficit has remained elevated at \\~\\$28 Bn in recent months... Trade deficit (\\$ Bn)"
  },
  {
    "figure_id": "F100",
    "report_id": "R006",
    "label": "EXHIBIT 4",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 6: Sustained FII outflows have continued to weigh on the INR"
  },
  {
    "figure_id": "F101",
    "report_id": "R006",
    "label": "EXHIBIT 5",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: Government expenditure has remained broadly in line with historical trends in the early part of the year..."
  },
  {
    "figure_id": "F102",
    "report_id": "R006",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 8: ...and a similar trend for tax collections"
  },
  {
    "figure_id": "F103",
    "report_id": "R006",
    "label": "EXHIBIT 7",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 9: Incremental demand for government securities from banks moderated in FY26, as reflected in their declining share of the outstanding G-sec stock"
  },
  {
    "figure_id": "F104",
    "report_id": "R006",
    "label": "EXHIBIT 7",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 9: Incremental demand for government securities from banks moderated in FY26, as reflected in their declining share of the outstanding G-sec stock Ownership pattern of G-sec (% of total) ■ SCBs ■ Insurance ■ RBI ■ Pension"
  },
  {
    "figure_id": "F105",
    "report_id": "R006",
    "label": "EXHIBIT 8",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 10: As a result, RBI emerged as the marginal buyer through large-scale open market operations (OMOs), driving its share of outstanding government securities to a multi-year high of 18%"
  },
  {
    "figure_id": "F106",
    "report_id": "R006",
    "label": "EXHIBIT 10",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 10: As a result, RBI emerged as the marginal buyer through large-scale open market operations (OMOs), driving its share of outstanding government securities to a multi-year high of 18% ## BANKING SECTOR"
  },
  {
    "figure_id": "F107",
    "report_id": "R006",
    "label": "EXHIBIT 10",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 10: As a result, RBI emerged as the marginal buyer through large-scale open market operations (OMOs), driving its share of outstanding government securities to a multi-year high of 18% ## BANKING SECTOR \\- Credit growth"
  },
  {
    "figure_id": "F108",
    "report_id": "R006",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 14: The recovery in system credit growth has been broad-based across segments, with the strongest momentum visible in industrial and services lending"
  },
  {
    "figure_id": "F109",
    "report_id": "R006",
    "label": "EXHIBIT 13",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 13: The strength in system-wide credit growth has also been reflected in the provisional business updates released by banks Loan growth (1Q27, % YoY) EXHIBIT 14: The recovery in system credit growth has been broad-based ac"
  },
  {
    "figure_id": "F110",
    "report_id": "R006",
    "label": "EXHIBIT 15",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 15: Credit card debt and spending continue to remain weak... EXHIBIT 16: ...despite a marginal pickup in card additions Credit card additions (TTM, Mn)"
  },
  {
    "figure_id": "F111",
    "report_id": "R006",
    "label": "EXHIBIT 15",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 15: Credit card debt and spending continue to remain weak... EXHIBIT 16: ...despite a marginal pickup in card additions Credit card additions (TTM, Mn) EXHIBIT 17: Consumer sentiment remains subdued amid a challenging ma"
  },
  {
    "figure_id": "F112",
    "report_id": "R006",
    "label": "EXHIBIT 17",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 17: Consumer sentiment remains subdued amid a challenging macro backdrop... RBI Urban consumer confidence indices ■ Current situation index ■ Future expectations index UPI P2M spends (TTM, % YoY) EXHIBIT 19: Fresh TD rat"
  },
  {
    "figure_id": "F113",
    "report_id": "R006",
    "label": "EXHIBIT 18",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 19: Fresh TD rates moderated during Apr–May'26 after witnessing a sharp increase in March, while fresh loan yields saw a marginal uptick Fresh lending and deposit rate (All SCBs, %) EXHIBIT 20: Outstanding TD rates and loa"
  },
  {
    "figure_id": "F114",
    "report_id": "R006",
    "label": "EXHIBIT 18",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 22: ...we do not see any material margin risk arising from the higher issuance, particularly given the relatively low share of CDs in overall deposits"
  },
  {
    "figure_id": "F115",
    "report_id": "R006",
    "label": "EXHIBIT 19",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 22: ...we do not see any material margin risk arising from the higher issuance, particularly given the relatively low share of CDs in overall deposits EXHIBIT 21: Although CD issuance rebounded in June following a softer May"
  },
  {
    "figure_id": "F116",
    "report_id": "R006",
    "label": "EXHIBIT 22",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 22: ...we do not see any material margin risk arising from the higher issuance, particularly given the relatively low share of CDs in overall deposits EXHIBIT 21: Although CD issuance rebounded in June following a softer May"
  },
  {
    "figure_id": "F117",
    "report_id": "R006",
    "label": "EXHIBIT 21",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 21: Although CD issuance rebounded in June following a softer May... CD Issuances (% YoY) (INR Tn, as % of deposits (RHS)) CD Issuances EXHIBIT 23: Additionally, the widening gap between loan yields and deposit rates is"
  },
  {
    "figure_id": "F118",
    "report_id": "R006",
    "label": "EXHIBIT 23",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 23: Additionally, the widening gap between loan yields and deposit rates is expected to provide a cushion against any potential pressure from CD funding costs All SCBs- Spread of loan yields over TD rates (%) EXHIBIT 24: A"
  },
  {
    "figure_id": "F119",
    "report_id": "R006",
    "label": "EXHIBIT 24",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 24: Asset quality trends are expected to remain largely benign in the current quarter, broadly in line with the trends witnessed during the last few quarters ## Credit cost (Provision expense as % of loans in bps, PSBs+PVBs)"
  },
  {
    "figure_id": "F120",
    "report_id": "R006",
    "label": "EXHIBIT 25",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 26: The banking sector has continued to demonstrate relative resilience, with Bank NIFTY down 3% YTD versus a 7% decline in the broader NIFTY index Stock price change -CYTD (%)"
  },
  {
    "figure_id": "F121",
    "report_id": "R006",
    "label": "EXHIBIT 26",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 26: The banking sector has continued to demonstrate relative resilience, with Bank NIFTY down 3% YTD versus a 7% decline in the broader NIFTY index Stock price change -CYTD (%) ## METRICS THAT MATTER ## SECTOR CONTROVERSIE"
  },
  {
    "figure_id": "F122",
    "report_id": "R006",
    "label": "Exhibit 55",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 29: The outperformance of PSBs began to show signs of moderation in 4QFY26, with PVBs regaining earnings momentum after an extended period of weaker growth..."
  },
  {
    "figure_id": "F123",
    "report_id": "R006",
    "label": "EXHIBIT 27",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 29: The outperformance of PSBs began to show signs of moderation in 4QFY26, with PVBs regaining earnings momentum after an extended period of weaker growth... PSBs and PVBs - PAT growth"
  },
  {
    "figure_id": "F124",
    "report_id": "R006",
    "label": "EXHIBIT 29",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 31: With the key drivers of PSB outperformance—surplus liquidity and ultra-low credit costs—nearing exhaustion, we continue to expect a gradual convergence in performance between PSBs and PVBs over the next few quarters."
  },
  {
    "figure_id": "F125",
    "report_id": "R006",
    "label": "EXHIBIT 29",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 31: With the key drivers of PSB outperformance—surplus liquidity and ultra-low credit costs—nearing exhaustion, we continue to expect a gradual convergence in performance between PSBs and PVBs over the next few quarters. PSB"
  },
  {
    "figure_id": "F126",
    "report_id": "R006",
    "label": "EXHIBIT 30",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 32: HDFCB reported healthy growth of \\~15% in both loans and deposits for 1Q27, with deposit growth continuing to be driven by term deposits and credit growth benefiting from the broader recovery in system lending"
  },
  {
    "figure_id": "F127",
    "report_id": "R006",
    "label": "EXHIBIT 33",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 35: ICICI Bank's RoA expanded to 2.4% in 4QFY26... EXHIBIT 36: ...aided by exceptionally low credit costs during the quarter, which the bank attributed to higher recoveries and write-backs"
  },
  {
    "figure_id": "F128",
    "report_id": "R006",
    "label": "EXHIBIT 34",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 34: ...supported by an early recovery in non-mortgage retail lending ICICI Bank- Non mortgage retail loans (% YoY) EXHIBIT 35: ICICI Bank's RoA expanded to 2.4% in 4QFY26... EXHIBIT 36: ...aided by exceptionally low credit"
  },
  {
    "figure_id": "F129",
    "report_id": "R006",
    "label": "EXHIBIT 35",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 37: Axis has continued to build on its growth momentum, delivering \\~19% YoY growth in 1Q27—comfortably ahead of peers such as HDFC and KMB and well above system growth"
  },
  {
    "figure_id": "F130",
    "report_id": "R006",
    "label": "EXHIBIT 36",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 36: ...aided by exceptionally low credit costs during the quarter, which the bank attributed to higher recoveries and write-backs ICICI Bank- RoA (%) ICICI- Provisions as % of average loans (bps) EXHIBIT 37: Axis has con"
  },
  {
    "figure_id": "F131",
    "report_id": "R006",
    "label": "EXHIBIT 38",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 40: KMB's 1Q27 provisional business update pointed towards a weak growth quarter..."
  },
  {
    "figure_id": "F132",
    "report_id": "R006",
    "label": "EXHIBIT 38",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 40: KMB's 1Q27 provisional business update pointed towards a weak growth quarter... KMB- Loans and Deposits (% YoY)"
  },
  {
    "figure_id": "F133",
    "report_id": "R006",
    "label": "EXHIBIT 39",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 41: ...with the bank facing a potential trade-off between growth and margins/profitability KMB - RoA (%) QoQ changes in NIM (bps)"
  },
  {
    "figure_id": "F134",
    "report_id": "R006",
    "label": "EXHIBIT 41",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 41: ...with the bank facing a potential trade-off between growth and margins/profitability KMB - RoA (%) QoQ changes in NIM (bps) EXHIBIT 42: This assumes greater significance as the bank had recently started delivering NI"
  },
  {
    "figure_id": "F135",
    "report_id": "R006",
    "label": "EXHIBIT 42",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 42: This assumes greater significance as the bank had recently started delivering NIM outcomes that were in line with, or better than, peers after a prolonged period of relative underperformance EXHIBIT 43: SBI has maintai"
  },
  {
    "figure_id": "F136",
    "report_id": "R006",
    "label": "EXHIBIT 43",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 43: SBI has maintained a healthy growth trajectory over the last few quarters, consistently delivering loan growth ahead of both ICICI Bank and HDFC Bank Loan growth (% YoY) NII growth (% YoY) EXHIBIT 45: As a result, ma"
  },
  {
    "figure_id": "F137",
    "report_id": "R006",
    "label": "EXHIBIT 44",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 45: As a result, margin trends and their implications for sustaining a 1%+ RoA are likely to remain under scrutiny SBI - RoA (%)"
  },
  {
    "figure_id": "F138",
    "report_id": "R006",
    "label": "EXHIBIT 45",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 47: Given the broad-based moderation in portfolio stress seen in 4QFY26... IndusInd Bank- Credit cost"
  },
  {
    "figure_id": "F139",
    "report_id": "R006",
    "label": "EXHIBIT 46",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 48: ...a continuation of similar asset quality trends would provide further boost to the profitability"
  },
  {
    "figure_id": "F140",
    "report_id": "R006",
    "label": "EXHIBIT 47",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 47: Given the broad-based moderation in portfolio stress seen in 4QFY26... IndusInd Bank- Credit cost (Provision expense as % of average loans) EXHIBIT 48: ...a continuation of similar asset quality trends would provide fu"
  },
  {
    "figure_id": "F141",
    "report_id": "R006",
    "label": "EXHIBIT 48",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 48: ...a continuation of similar asset quality trends would provide further boost to the profitability IndusInd Bank- RoA (%) BAF - Credit cost (Annualized, % of avg. AuF) EXHIBIT 49: Bajaj Finance saw a sharp decline in c"
  },
  {
    "figure_id": "F142",
    "report_id": "R006",
    "label": "EXHIBIT 49",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 51: With decline in credit costs already factored in, what would matter for SBI Cards in the growth in receivables..."
  },
  {
    "figure_id": "F143",
    "report_id": "R006",
    "label": "EXHIBIT 49",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 51: With decline in credit costs already factored in, what would matter for SBI Cards in the growth in receivables... SBI Cards total receivables (% YoY) EXHIBIT 52: ...and within that the share of revolvers"
  },
  {
    "figure_id": "F144",
    "report_id": "R006",
    "label": "EXHIBIT 50",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 52: ...and within that the share of revolvers SBI Cards- Receivables mix (% of total)"
  },
  {
    "figure_id": "F145",
    "report_id": "R006",
    "label": "EXHIBIT 52",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 52: ...and within that the share of revolvers SBI Cards- Receivables mix (% of total) EXHIBIT 53: Paytm's net payment margin (NPM) declined to 9 bps in 4Q26 (vs. 9.6 bps in 3Q26), reflecting the (known) PIDF discontinuatio"
  },
  {
    "figure_id": "F146",
    "report_id": "R006",
    "label": "EXHIBIT 53",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 55: A continuation of the 4Q26 trend of pick-up in disbursement growth... AHFCs - Disbursements growth (% YoY)"
  },
  {
    "figure_id": "F147",
    "report_id": "R006",
    "label": "EXHIBIT 54",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 56: ...and a stabilization in AUM growth would be a key positive HFCs - AuM growth (% YoY)"
  },
  {
    "figure_id": "F148",
    "report_id": "R006",
    "label": "EXHIBIT 54",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 56: ...and a stabilization in AUM growth would be a key positive HFCs - AuM growth (% YoY) ## I. REQUIRED DISCLOSURES"
  },
  {
    "figure_id": "F149",
    "report_id": "R006",
    "label": "EXHIBIT 55",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 55: A continuation of the 4Q26 trend of pick-up in disbursement growth... AHFCs - Disbursements growth (% YoY) EXHIBIT 56: ...and a stabilization in AUM growth would be a key positive HFCs - AuM growth (% YoY) ## I. REQU"
  },
  {
    "figure_id": "F150",
    "report_id": "R007",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: We model revenue growth and ARR growth to continue decelerating through FY28"
  },
  {
    "figure_id": "F151",
    "report_id": "R007",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: We model revenue growth and ARR growth to continue decelerating through FY28 Revenue and ARR dollar and growth trajectory BofA GLOBAL RESEARCH ## Cannibalization risk ## Increased AI usage at the cost of higher-margin"
  },
  {
    "figure_id": "F152",
    "report_id": "R007",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: Total revenue to grow \\~9% from FY26-FY28E, driven primarily by Subscription growth of 9-11% Total revenue and segment revenue growth estimates, FY24-FY28E Exhibit 7: Total subscription revenue to grow 9-11% from FY26-"
  },
  {
    "figure_id": "F153",
    "report_id": "R007",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: Total revenue to grow \\~9% from FY26-FY28E, driven primarily by Subscription growth of 9-11% Total revenue and segment revenue growth estimates, FY24-FY28E Exhibit 7: Total subscription revenue to grow 9-11% from FY26-"
  },
  {
    "figure_id": "F154",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 5: Denso's semiconductor business is almost entirely exposed to the automotive market"
  },
  {
    "figure_id": "F155",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 5: Denso's semiconductor business is almost entirely exposed to the automotive market 17/67"
  },
  {
    "figure_id": "F156",
    "report_id": "R008",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 4: Gartner estimates Denso's semiconductor revenue at JPY 208 bn in 2025 EXHIBIT 5: Denso's semiconductor business is almost entirely exposed to the automotive market 17/67 ## Denso's semiconductor business strategy Den"
  },
  {
    "figure_id": "F157",
    "report_id": "R008",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 6: Denso identified semiconductors as one of its ‘Societal Value Expansion Domains’ in the mid-term plan announced in Mar-2026 \"Developing People, Co-Creating with Partners\" to Lead New Value Creation Partner Collaboratio"
  },
  {
    "figure_id": "F158",
    "report_id": "R008",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 6: Denso identified semiconductors as one of its ‘Societal Value Expansion Domains’ in the mid-term plan announced in Mar-2026 \"Developing People, Co-Creating with Partners\" to Lead New Value Creation Partner Collaboratio"
  },
  {
    "figure_id": "F159",
    "report_id": "R008",
    "label": "EXHIBIT 7",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: Denso has historically pursued minority equity investments to strengthen semiconductor supply security and strategic partnerships Direction of Partner Collaboration ## Continuously advance strategic partnerships to e"
  },
  {
    "figure_id": "F160",
    "report_id": "R008",
    "label": "EXHIBIT 7",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 7: Denso has historically pursued minority equity investments to strengthen semiconductor supply security and strategic partnerships Direction of Partner Collaboration ## Continuously advance strategic partnerships to e"
  },
  {
    "figure_id": "F161",
    "report_id": "R008",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 8: The global semiconductor market is expected to grow from USD 0.8 tn in 2026 to USD 2.2 bn in 2030, implying a CAGR of 21.6% EXHIBIT 9: Growth is expected to be driven primarily by memory and ASIC/ASSP markets, which be"
  },
  {
    "figure_id": "F162",
    "report_id": "R008",
    "label": "EXHIBIT 8",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 10: The 'Data processing (compute)' segment, which includes chips for AI servers, is expected to remain the primary driver of market growth"
  },
  {
    "figure_id": "F163",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 11: The share of the 'Data processing (Compute)' application category out of total semiconductor market is projected to exceed 50% by 2030 We assess the attractiveness of the 63 semiconductor segments formed by the combina"
  },
  {
    "figure_id": "F164",
    "report_id": "R008",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 12: Discrete × Automotive, Discrete × Industrial, and Analog × Industrial rank in the top 20-40% of the 63 device-application combinations,"
  },
  {
    "figure_id": "F165",
    "report_id": "R008",
    "label": "EXHIBIT 16",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 16: Among Japanese power semiconductor companies, we focus on Fuji Electric, Rohm, Mitsubishi Electric, Toshiba, and Renesas, while onsemi, Infineon, and STM represent potential US and European candidates Note 1: Market cap"
  },
  {
    "figure_id": "F166",
    "report_id": "R008",
    "label": "EXHIBIT 17",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 17: Semiconductor device portfolio by candidate as of 2025 By application, automotive remains the largest end market across all of the companies under review, although exposure outside automotive varies meaningfully by pla"
  },
  {
    "figure_id": "F167",
    "report_id": "R008",
    "label": "EXHIBIT 18",
    "figure_type": "source_exhibit",
    "context": "EXHIBIT 18: Semiconductor application portfolio by candidate as of 2025 ■ Automotive ■ Industrial ■ Consumer ■ Data processing (Compute) ■ Data processing (Storage) ■ Wired Communication ■ Wireless Communication Finally, we assess"
  },
  {
    "figure_id": "F168",
    "report_id": "R009",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: MSCI China's P/E at 10.3x is $12\\%$ below long-term average Forward P/E valuation of MSCI China Index BofA GLOBAL RESEARCH Consensus forecast for MSCI China earnings growth BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F169",
    "report_id": "R009",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: China's consumer confidence retreated in Mar-Apr 2026 China consumer confidence index (CCI)"
  },
  {
    "figure_id": "F170",
    "report_id": "R009",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: China's consumer confidence retreated in Mar-Apr 2026 China consumer confidence index (CCI) Exhibit 4: Industrial profit growth accelerated to 18.8% YoY in 5M26 Industrial profit growth (YTD) vs PPI inflation BofA GL"
  },
  {
    "figure_id": "F171",
    "report_id": "R009",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: We prefer brokers/industrials/tech sectors over consumer/utilities in 3Q26"
  },
  {
    "figure_id": "F172",
    "report_id": "R009",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: KOSPI, ChiNext, and Nikkei 225 outperformed in 2Q26 while HSCEI, HSI and MSCI China lagged Comparison of key global market performance BofA GLOBAL RESEARCH Exhibit 7: IT significantly outperformed in 2Q26, while consum"
  },
  {
    "figure_id": "F173",
    "report_id": "R009",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: AI hardware and semis stocks were among the top market cap gainers Top 10 market cap gainers in MSCI China (2Q26)"
  },
  {
    "figure_id": "F174",
    "report_id": "R009",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: AI hardware and semis stocks were among the top market cap gainers Top 10 market cap gainers in MSCI China (2Q26) BofA GLOBAL RESEARCH Exhibit 9: Energy, internet and consumer stocks were among the top market cap loser"
  },
  {
    "figure_id": "F175",
    "report_id": "R009",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: AI hardware and semis stocks were among the top market cap gainers Top 10 market cap gainers in MSCI China (2Q26) BofA GLOBAL RESEARCH Exhibit 9: Energy, internet and consumer stocks were among the top market cap loser"
  },
  {
    "figure_id": "F176",
    "report_id": "R009",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 12: IT, Real Estate, and Utilities are above their long-term P/E levels in 2Q26 Forward P/E valuation of major MSCI China sectors ## Valuation and earnings revision Exhibit 11: P/E is at 15x for CSI 300 and 10x for MSCI Chin"
  },
  {
    "figure_id": "F177",
    "report_id": "R009",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 13: Net earnings upgrade accounted for 2% of total companies in 2Q26, vs 13% in 1Q MSCI China performance vs index earnings revision QoQ"
  },
  {
    "figure_id": "F178",
    "report_id": "R009",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Exhibit 13: Net earnings upgrade accounted for 2% of total companies in 2Q26, vs 13% in 1Q MSCI China performance vs index earnings revision QoQ BofA GLOBAL RESEARCH Exhibit 14: Energy and Materials saw the highest net upgrades, w"
  },
  {
    "figure_id": "F179",
    "report_id": "R009",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Exhibit 13: Net earnings upgrade accounted for 2% of total companies in 2Q26, vs 13% in 1Q MSCI China performance vs index earnings revision QoQ BofA GLOBAL RESEARCH Exhibit 14: Energy and Materials saw the highest net upgrades, w"
  },
  {
    "figure_id": "F180",
    "report_id": "R009",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: EM funds' exposure to South Korea and Taiwan stocks soar Market allocations by active global EM funds (%) Exhibit 17: Active funds' UW positions on China narrowed Active and passive global EM funds' exposure to China s"
  },
  {
    "figure_id": "F181",
    "report_id": "R009",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 18: SSE new account opening +60% YoY in 1H26"
  },
  {
    "figure_id": "F182",
    "report_id": "R009",
    "label": "Exhibit 18",
    "figure_type": "source_exhibit",
    "context": "Exhibit 18: SSE new account opening +60% YoY in 1H26 New account openings at the Shanghai Stock Exchange ('000) BofA GLOBAL RESEARCH Exhibit 20: Major shareholders' stock selling edged down in June Share reductions by major shareh"
  },
  {
    "figure_id": "F183",
    "report_id": "R009",
    "label": "Exhibit 18",
    "figure_type": "source_exhibit",
    "context": "Exhibit 22: Southbound capital flows to HK rebounded in June Cumulative southbound capital flows to HK stocks since 2026 (HKD bn)"
  },
  {
    "figure_id": "F184",
    "report_id": "R009",
    "label": "Exhibit 20",
    "figure_type": "source_exhibit",
    "context": "Exhibit 19: Equity fund issuances hit a fresh YTD high in June Issuances of new mutual funds (bn shares) BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F185",
    "report_id": "R009",
    "label": "Exhibit 22",
    "figure_type": "source_exhibit",
    "context": "Exhibit 21: ETF selling by China's \"national team\" accelerates Cumulative capital flows to China's domestic ETF funds (USD bn) BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F186",
    "report_id": "R009",
    "label": "Exhibit 19",
    "figure_type": "source_exhibit",
    "context": "Exhibit 23: Mainland investors continue to exit HK ETFs at a fast pace. Changes in shares of HK equity ETFs listed in China mainland (bn shares) BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F187",
    "report_id": "R009",
    "label": "Exhibit 21",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: IPO financing value in HK rebounded in June"
  },
  {
    "figure_id": "F188",
    "report_id": "R009",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: IPO financing value in HK rebounded in June IPO financing value in HK (HKD bn) and A-share market (RMB bn) Exhibit 25: Restricted stock unlocks in HK expected to surge in 3Q26 Monthly amount of lock-up expiration in HK"
  },
  {
    "figure_id": "F189",
    "report_id": "R009",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 26: Hong Kong liquidity conditions show marginal MoM improvement, but are yet to turn supportive"
  },
  {
    "figure_id": "F190",
    "report_id": "R009",
    "label": "Exhibit 27",
    "figure_type": "source_exhibit",
    "context": "Exhibit 27: We expect credit and GDP growth to edge down in 2026E China's credit growth cycle leads GDP growth Credit growth multiplier leads sequential GDP growth BofA GLOBAL RESEARCH BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F191",
    "report_id": "R009",
    "label": "Exhibit 27",
    "figure_type": "source_exhibit",
    "context": "Exhibit 27: We expect credit and GDP growth to edge down in 2026E China's credit growth cycle leads GDP growth Credit growth multiplier leads sequential GDP growth BofA GLOBAL RESEARCH BofA GLOBAL RESEARCH Bank sector loan growt"
  },
  {
    "figure_id": "F192",
    "report_id": "R009",
    "label": "Exhibit 29",
    "figure_type": "source_exhibit",
    "context": "Exhibit 29: Loan growth declined to a record low of 5.5% YoY in May YoY growth of various types of financing BofA GLOBAL RESEARCH Exhibit 30: Retail loan growth dropped to -0.9% YoY in May-26 YoY household loan and deposit growth"
  },
  {
    "figure_id": "F193",
    "report_id": "R009",
    "label": "Exhibit 29",
    "figure_type": "source_exhibit",
    "context": "Exhibit 29: Loan growth declined to a record low of 5.5% YoY in May YoY growth of various types of financing BofA GLOBAL RESEARCH Exhibit 30: Retail loan growth dropped to -0.9% YoY in May-26 YoY household loan and deposit growth"
  },
  {
    "figure_id": "F194",
    "report_id": "R009",
    "label": "Exhibit 31",
    "figure_type": "source_exhibit",
    "context": "Exhibit 31: SHIBOR and bond yields edged down 10-20bp in 1H26 China's policy rate, interbank rate and bond yields Exhibit 32: Deposit pricing has been cut more aggressively in 2024-25 Major banks' average time deposit pricing vs C"
  },
  {
    "figure_id": "F195",
    "report_id": "R009",
    "label": "Exhibit 31",
    "figure_type": "source_exhibit",
    "context": "Exhibit 33: MSCI China declined YTD despite the RMB appreciation RMB-USD FX rate vs MSCI China Index"
  },
  {
    "figure_id": "F196",
    "report_id": "R009",
    "label": "Exhibit 33",
    "figure_type": "source_exhibit",
    "context": "Exhibit 33: MSCI China declined YTD despite the RMB appreciation RMB-USD FX rate vs MSCI China Index BofA GLOBAL RESEARCH Exhibit 34: China FX reserve has risen to the highest level since 2016 China's FX rate and FX reserve BofA"
  },
  {
    "figure_id": "F197",
    "report_id": "R009",
    "label": "Exhibit 33",
    "figure_type": "source_exhibit",
    "context": "Exhibit 33: MSCI China declined YTD despite the RMB appreciation RMB-USD FX rate vs MSCI China Index BofA GLOBAL RESEARCH Exhibit 34: China FX reserve has risen to the highest level since 2016 China's FX rate and FX reserve BofA"
  },
  {
    "figure_id": "F198",
    "report_id": "R009",
    "label": "Exhibit 35",
    "figure_type": "source_exhibit",
    "context": "Exhibit 35: Higher oil price has driven up China's inflation China's PPI correlates with the movement in Brent oil price BofA GLOBAL RESEARCH Exhibit 36: Industrial profit growth accelerated to 18.8% YoY in 5M26 Industrial profit"
  },
  {
    "figure_id": "F199",
    "report_id": "R009",
    "label": "Exhibit 35",
    "figure_type": "source_exhibit",
    "context": "Exhibit 35: Higher oil price has driven up China's inflation China's PPI correlates with the movement in Brent oil price BofA GLOBAL RESEARCH Exhibit 36: Industrial profit growth accelerated to 18.8% YoY in 5M26 Industrial profit"
  },
  {
    "figure_id": "F200",
    "report_id": "R009",
    "label": "Exhibit 37",
    "figure_type": "source_exhibit",
    "context": "Exhibit 37: NBS PMI hovered above 50 in May and Jun 2026 China Purchasing Managers' Index (PMI) Exhibit 38: Exports growth was more than $15\\%$ YoY in 5M26 YoY growth in China YTD imports/exports in USD terms BofA GLOBAL RESEARC"
  },
  {
    "figure_id": "F201",
    "report_id": "R009",
    "label": "Exhibit 37",
    "figure_type": "source_exhibit",
    "context": "Exhibit 39: Retail sales weakened swiftly in Apr-May YoY growth in YTD retail sales and online retail sales"
  },
  {
    "figure_id": "F202",
    "report_id": "R009",
    "label": "Exhibit 39",
    "figure_type": "source_exhibit",
    "context": "Exhibit 39: Retail sales weakened swiftly in Apr-May YoY growth in YTD retail sales and online retail sales Exhibit 40: FAI growth fell to -4.1% YoY in 5M26 YoY growth in YTD Fixed Asset Investment BofA GLOBAL RESEARCH BofA GLOB"
  },
  {
    "figure_id": "F203",
    "report_id": "R009",
    "label": "Exhibit 39",
    "figure_type": "source_exhibit",
    "context": "Exhibit 39: Retail sales weakened swiftly in Apr-May YoY growth in YTD retail sales and online retail sales Exhibit 40: FAI growth fell to -4.1% YoY in 5M26 YoY growth in YTD Fixed Asset Investment BofA GLOBAL RESEARCH BofA GLOB"
  },
  {
    "figure_id": "F204",
    "report_id": "R009",
    "label": "Exhibit 41",
    "figure_type": "source_exhibit",
    "context": "Exhibit 41: Youth unemployment at 15.6% in May-26 was slightly higher than May-25 China: overall unemployment and youth unemployment BofA GLOBAL RESEARCH Exhibit 42: Consumer confidence indices declined in Mar-Apr before reboundin"
  },
  {
    "figure_id": "F205",
    "report_id": "R009",
    "label": "Exhibit 42",
    "figure_type": "source_exhibit",
    "context": "Exhibit 43: Property market saw continued double-digit YoY decline in activities in 2026 YTD YoY change in residential floor space (in bn sqm)"
  },
  {
    "figure_id": "F206",
    "report_id": "R009",
    "label": "Exhibit 43",
    "figure_type": "source_exhibit",
    "context": "Exhibit 43: Property market saw continued double-digit YoY decline in activities in 2026 YTD YoY change in residential floor space (in bn sqm) BofA GLOBAL RESEARCH Exhibit 44: Property price decline narrowed in 1Q, but widened in"
  },
  {
    "figure_id": "F207",
    "report_id": "R009",
    "label": "Exhibit 44",
    "figure_type": "source_exhibit",
    "context": "Exhibit 44: Property price decline narrowed in 1Q, but widened in May Residential property price index (previous month = 100) BofA GLOBAL RESEARCH ## Earnings growth remains challenged Consensus EPS growth forecast for MSCI China"
  },
  {
    "figure_id": "F208",
    "report_id": "R009",
    "label": "Exhibit 45",
    "figure_type": "source_exhibit",
    "context": "Exhibit 46: $71\\%$ companies missed earnings expectations by over $5\\%$ in annual results FY25 results vs consensus estimates BofA GLOBAL RESEARCH BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F209",
    "report_id": "R009",
    "label": "Exhibit 45",
    "figure_type": "source_exhibit",
    "context": "Exhibit 47: Consensus expects strong 2026E earnings growth in autos, materials, IT, and industrials sectors MSCI China constituents' earnings analysis by sector"
  },
  {
    "figure_id": "F210",
    "report_id": "R009",
    "label": "Exhibit 49",
    "figure_type": "source_exhibit",
    "context": "Exhibit 49: Media and auto sectors had the worst earnings cut in 2Q, banks and metals & mining had the best upward revision Percentage of companies that had net earnings upgrade Exhibit 50: Auto and online retail sectors dropped 2"
  },
  {
    "figure_id": "F211",
    "report_id": "R009",
    "label": "Exhibit 49",
    "figure_type": "source_exhibit",
    "context": "Exhibit 51: Valuation declined at most sectors in 2Q26, except for electronic equipment Forward P/E valuations"
  },
  {
    "figure_id": "F212",
    "report_id": "R009",
    "label": "Exhibit 51",
    "figure_type": "source_exhibit",
    "context": "Exhibit 51: Valuation declined at most sectors in 2Q26, except for electronic equipment Forward P/E valuations BofA GLOBAL RESEARCH Exhibit 52: Electronic equipment is expensive compared to its long-term average valuation BofA G"
  },
  {
    "figure_id": "F213",
    "report_id": "R009",
    "label": "Exhibit 51",
    "figure_type": "source_exhibit",
    "context": "Exhibit 51: Valuation declined at most sectors in 2Q26, except for electronic equipment Forward P/E valuations BofA GLOBAL RESEARCH Exhibit 52: Electronic equipment is expensive compared to its long-term average valuation BofA G"
  },
  {
    "figure_id": "F214",
    "report_id": "R009",
    "label": "Exhibit 53",
    "figure_type": "source_exhibit",
    "context": "Exhibit 53: BofA China Investment Compass and historical stock market performance Each phase in our Compass typically lasts for 2-5 quarters BofA GLOBAL RESEARCH MSCI China performance correlated to GDP and liquidity cycles Stock"
  },
  {
    "figure_id": "F215",
    "report_id": "R009",
    "label": "Exhibit 54",
    "figure_type": "source_exhibit",
    "context": "Exhibit 54: Economic growth: YoY growth in nominal and real GDP Nominal GDP growth has decelerated over the past 19 years BofA GLOBAL RESEARCH Exhibit 55: Sequential change in nominal GDP growth vs MSCI China MSCI China performanc"
  },
  {
    "figure_id": "F216",
    "report_id": "R009",
    "label": "Exhibit 54",
    "figure_type": "source_exhibit",
    "context": "Exhibit 56: Interbank liquidity: SHIBOR vs time deposit rate Deposit spread = 3M SHIBOR – 3M time deposit rate"
  },
  {
    "figure_id": "F217",
    "report_id": "R009",
    "label": "Exhibit 56",
    "figure_type": "source_exhibit",
    "context": "Exhibit 56: Interbank liquidity: SHIBOR vs time deposit rate Deposit spread = 3M SHIBOR – 3M time deposit rate BofA GLOBAL RESEARCH Exhibit 57: Interbank deposit spread vs MSCI China MSCI China performance has positive correlation"
  },
  {
    "figure_id": "F218",
    "report_id": "R009",
    "label": "Exhibit 56",
    "figure_type": "source_exhibit",
    "context": "Exhibit 58: BofA breakdown of 40 sectors and their major large-cap stocks Our sector analysis is based on the 40-sector breakdown"
  },
  {
    "figure_id": "F219",
    "report_id": "R010",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: NVDA is owned by 78% of active funds of S&P 500 index, vs. non-NVDA peer average of 81% NVDA ownership of active funds in S&P 500 vs. other key tech peers BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F220",
    "report_id": "R010",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: NVDA is owned by 78% of active funds of S&P 500 index, vs. non-NVDA peer average of 81% NVDA ownership of active funds in S&P 500 vs. other key tech peers BofA GLOBAL RESEARCH Exhibit 6: NVDA's total investments of \\~\\"
  },
  {
    "figure_id": "F221",
    "report_id": "R011",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Industry loan YoY growth – for use in vs outside HK Total loans and advances - YoY growth Total loans and advances for use in HK - YoY growth Total loans for use outside HK - YoY growth Figure 2: Industry loan YoY grow"
  },
  {
    "figure_id": "F222",
    "report_id": "R011",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Industry mortgage YoY growth"
  },
  {
    "figure_id": "F223",
    "report_id": "R011",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Industry loan YoY growth – HKD vs FCY loans Figure 3: Industry mortgage YoY growth Figure 4: Industry LDR and CASA %"
  },
  {
    "figure_id": "F224",
    "report_id": "R011",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Industry LDR and CASA % Figure 5: Industry LDR by currency – HKD vs FCY Figure 6: Daily average 1M SOFR and HIBOR"
  },
  {
    "figure_id": "F225",
    "report_id": "R011",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Industry LDR and CASA % Figure 5: Industry LDR by currency – HKD vs FCY Figure 6: Daily average 1M SOFR and HIBOR Figure 7: Daily average 3M SOFR and HIBOR"
  },
  {
    "figure_id": "F226",
    "report_id": "R011",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Industry LDR and CASA % Figure 5: Industry LDR by currency – HKD vs FCY Figure 6: Daily average 1M SOFR and HIBOR Figure 7: Daily average 3M SOFR and HIBOR Figure 8: 1M SOFR-HIBOR gap vs. USD/HKD FX rates"
  },
  {
    "figure_id": "F227",
    "report_id": "R011",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Daily average 1M SOFR and HIBOR Figure 7: Daily average 3M SOFR and HIBOR Figure 8: 1M SOFR-HIBOR gap vs. USD/HKD FX rates Figure 9: 1M SOFR-HIBOR gap vs. aggregate balance + EFBN"
  },
  {
    "figure_id": "F228",
    "report_id": "R011",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Daily average 3M SOFR and HIBOR Figure 8: 1M SOFR-HIBOR gap vs. USD/HKD FX rates Figure 9: 1M SOFR-HIBOR gap vs. aggregate balance + EFBN Figure 10: The composite interest rate was 1.26% in May 2026"
  },
  {
    "figure_id": "F229",
    "report_id": "R011",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: 1M SOFR-HIBOR gap vs. USD/HKD FX rates Figure 9: 1M SOFR-HIBOR gap vs. aggregate balance + EFBN Figure 10: The composite interest rate was 1.26% in May 2026 Figure 11: Implied deposit spreads increased MoM in May o"
  },
  {
    "figure_id": "F230",
    "report_id": "R011",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: 1M SOFR-HIBOR gap vs. aggregate balance + EFBN Figure 10: The composite interest rate was 1.26% in May 2026 Figure 11: Implied deposit spreads increased MoM in May on higher HIBOR"
  },
  {
    "figure_id": "F231",
    "report_id": "R011",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: The composite interest rate was 1.26% in May 2026 Figure 11: Implied deposit spreads increased MoM in May on higher HIBOR"
  },
  {
    "figure_id": "F232",
    "report_id": "R011",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Mortgage delinquency ratio – over 3M/6M Figure 13: Bankruptcy and petitions vs unemployment rate"
  },
  {
    "figure_id": "F233",
    "report_id": "R011",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Mortgage delinquency ratio – over 3M/6M Figure 13: Bankruptcy and petitions vs unemployment rate"
  },
  {
    "figure_id": "F234",
    "report_id": "R012",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Net length across commodity markets decreased by \\$9 billion, largely driven by crude oil market"
  },
  {
    "figure_id": "F235",
    "report_id": "R012",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Net length across commodity markets decreased by \\$9 billion, largely driven by crude oil market All data as of June 30, 2026, except LME data as of July 3, 2026, and TTF/EUA/UKE date as of June 26, 2026. USD/oz (avera"
  },
  {
    "figure_id": "F236",
    "report_id": "R012",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: The estimated value of global commodity market open interest stabilised over the week USD billion, estimated open interest across tracked commodity markets Figure 3: Net length across commodity markets decreased by \\$9"
  },
  {
    "figure_id": "F237",
    "report_id": "R012",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 6: The estimated value of open interest across energy markets decreased by 1% WoW Figure 5: The CTA net long positioning in COMEX Gold increased by 6% over the week Figure 4: Latest projections indicate increasing positioni"
  },
  {
    "figure_id": "F238",
    "report_id": "R012",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: The estimated value of open interest across energy markets decreased by 1% WoW Figure 5: The CTA net long positioning in COMEX Gold increased by 6% over the week Figure 4: Latest projections indicate increasing positioni"
  },
  {
    "figure_id": "F239",
    "report_id": "R012",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 7: The estimated value of open interest across environmental markets decreased by 3% WoW USD billion, estimated open interest across tracked environmental markets Figure 9: The estimated value of open interest across base"
  },
  {
    "figure_id": "F240",
    "report_id": "R012",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 8: The estimated value of open interest across precious metals increased by 3% WoW USD billion, estimated open interest across tracked precious metals markets"
  },
  {
    "figure_id": "F241",
    "report_id": "R012",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 10: The estimated value of open interest in agri markets plateaued over the week USD billion, estimated open interest across tracked agricultural markets"
  },
  {
    "figure_id": "F242",
    "report_id": "R012",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: The estimated value of open interest in agri markets plateaued over the week USD billion, estimated open interest across tracked agricultural markets Figure 11: The estimated value of open interest in crude oil decreas"
  },
  {
    "figure_id": "F243",
    "report_id": "R012",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Petroleum products estimated open interest value increased by 5% WoW"
  },
  {
    "figure_id": "F244",
    "report_id": "R012",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Petroleum products estimated open interest value increased by 5% WoW USD billion, estimated open interest across tracked petroleum products markets Figure 13: The estimated value of open interest in natural gas markets"
  },
  {
    "figure_id": "F245",
    "report_id": "R012",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 13: The estimated value of open interest in natural gas markets increased by 1% WoW USD billion, estimated open interest across tracked natural gas metals markets 10 year range and average exclude 2022 Figure 15: The estim"
  },
  {
    "figure_id": "F246",
    "report_id": "R012",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 15: The estimated value of open interest in soft markets increased by 4% WoW Figure 14: The estimated value of open interest in grains & oilseeds markets decreased by 1% WoW USD billion, estimated open interest across tracke"
  },
  {
    "figure_id": "F247",
    "report_id": "R012",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 16: The estimated open interest value across livestock markets decreased by 3% WoW USD billion, estimated open interest across tracked livestock markets"
  },
  {
    "figure_id": "F248",
    "report_id": "R012",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 16: The estimated open interest value across livestock markets decreased by 3% WoW USD billion, estimated open interest across tracked livestock markets When the z-score (indicator of momentum) reaches 0, known as the swit"
  },
  {
    "figure_id": "F249",
    "report_id": "R012",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: The estimated open interest value across livestock markets decreased by 3% WoW USD billion, estimated open interest across tracked livestock markets When the z-score (indicator of momentum) reaches 0, known as the swit"
  },
  {
    "figure_id": "F250",
    "report_id": "R012",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Price momentum (z-scores) and trading signals across major commodities Figure 18: Price momentum across commodity markets and trading signals Optimal lookback period of each momentum strategy combined with a mean rever"
  },
  {
    "figure_id": "F251",
    "report_id": "R012",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Energy sectoral standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms All data as of June 30, 2026, except TTF as of June 26, 2026. Figure 2"
  },
  {
    "figure_id": "F252",
    "report_id": "R012",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 21: NYMEX WTI Crude Oil position and price"
  },
  {
    "figure_id": "F253",
    "report_id": "R012",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: NYMEX WTI Crude Oil position and price Figure 22: ICE Brent Crude Oil position and price Figure 23: ICE Dubai Crude Oil position and price"
  },
  {
    "figure_id": "F254",
    "report_id": "R012",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: NYMEX WTI Crude Oil position and price Figure 22: ICE Brent Crude Oil position and price Figure 23: ICE Dubai Crude Oil position and price Figure 24: ICE TTF Natural Gas position and price LHS: TWh; RHS: \\$/MWh"
  },
  {
    "figure_id": "F255",
    "report_id": "R012",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: NYMEX WTI Crude Oil position and price Figure 22: ICE Brent Crude Oil position and price Figure 23: ICE Dubai Crude Oil position and price Figure 24: ICE TTF Natural Gas position and price LHS: TWh; RHS: \\$/MWh"
  },
  {
    "figure_id": "F256",
    "report_id": "R012",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23: ICE Dubai Crude Oil position and price Figure 24: ICE TTF Natural Gas position and price LHS: TWh; RHS: \\$/MWh Figure 25: Weekly change in total OI due to price/flows USD million Figure 27: Weekly change in total O"
  },
  {
    "figure_id": "F257",
    "report_id": "R012",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Figure 24: ICE TTF Natural Gas position and price LHS: TWh; RHS: \\$/MWh Figure 25: Weekly change in total OI due to price/flows USD million Figure 27: Weekly change in total OI from changes in contracts (flows) USD million Figu"
  },
  {
    "figure_id": "F258",
    "report_id": "R012",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 25: Weekly change in total OI due to price/flows USD million Figure 27: Weekly change in total OI from changes in contracts (flows) USD million Figure 26: Weekly change in total OI from changes in prices USD million ##"
  },
  {
    "figure_id": "F259",
    "report_id": "R012",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 27: Weekly change in total OI from changes in contracts (flows) USD million Figure 26: Weekly change in total OI from changes in prices USD million ## Environmental markets"
  },
  {
    "figure_id": "F260",
    "report_id": "R012",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Environmental markets standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms Figure 29: ICE EUA position and price LHS: n of contracts; RHS:"
  },
  {
    "figure_id": "F261",
    "report_id": "R012",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 30: Weekly change in total OI due to price/flows"
  },
  {
    "figure_id": "F262",
    "report_id": "R012",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Weekly change in total OI from changes in contracts (flows) USD million"
  },
  {
    "figure_id": "F263",
    "report_id": "R012",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Figure 30: Weekly change in total OI due to price/flows Figure 31: Weekly change in total OI from changes in prices USD million Figure 32: Weekly change in total OI from changes in contracts (flows) USD million ## Metals mark"
  },
  {
    "figure_id": "F264",
    "report_id": "R012",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "Figure 31: Weekly change in total OI from changes in prices USD million Figure 32: Weekly change in total OI from changes in contracts (flows) USD million ## Metals markets USD million"
  },
  {
    "figure_id": "F265",
    "report_id": "R012",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 33: Metals sectoral standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms Figure 34: Base Metals standardised level chart 0-10 standardized scal"
  },
  {
    "figure_id": "F266",
    "report_id": "R012",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Precious Metals standardised level chart"
  },
  {
    "figure_id": "F267",
    "report_id": "R012",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Precious Metals standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms Figure 36: COMEX Gold position and price LHS: n of contracts; RHS: \\$/"
  },
  {
    "figure_id": "F268",
    "report_id": "R012",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "Figure 36: COMEX Gold position and price LHS: n of contracts; RHS: \\$/t oz All data as of June 30, 2026. Figure 37: COMEX Copper position and price LHS: n of contracts; RHS: \\$/lb"
  },
  {
    "figure_id": "F269",
    "report_id": "R012",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: COMEX Copper position and price LHS: n of contracts; RHS: \\$/lb Figure 38: LME Copper position and price LHS: n of contracts; RHS: \\$/MT Figure 39: Weekly change in total OI due to price/flows USD million"
  },
  {
    "figure_id": "F270",
    "report_id": "R012",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: COMEX Copper position and price LHS: n of contracts; RHS: \\$/lb Figure 38: LME Copper position and price LHS: n of contracts; RHS: \\$/MT Figure 39: Weekly change in total OI due to price/flows USD million Figure 40"
  },
  {
    "figure_id": "F271",
    "report_id": "R012",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 42: Weekly change in total OI from changes in contracts (flows)-industrial and bulk metals"
  },
  {
    "figure_id": "F272",
    "report_id": "R012",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "Figure 39: Weekly change in total OI due to price/flows USD million Figure 40: Weekly change in total OI from changes in prices USD million Figure 41: Weekly change in total OI from changes in contracts (flows) USD million Figu"
  },
  {
    "figure_id": "F273",
    "report_id": "R012",
    "label": "Figure 40",
    "figure_type": "source_exhibit",
    "context": "Figure 43: Weekly change in total OI from changes in contracts (flows)-precious metals"
  },
  {
    "figure_id": "F274",
    "report_id": "R012",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 41: Weekly change in total OI from changes in contracts (flows) USD million Figure 42: Weekly change in total OI from changes in contracts (flows)-industrial and bulk metals Figure 43: Weekly change in total OI from chan"
  },
  {
    "figure_id": "F275",
    "report_id": "R012",
    "label": "Figure 42",
    "figure_type": "source_exhibit",
    "context": "Figure 42: Weekly change in total OI from changes in contracts (flows)-industrial and bulk metals Figure 43: Weekly change in total OI from changes in contracts (flows)-precious metals ## Agricultural markets USD million"
  },
  {
    "figure_id": "F276",
    "report_id": "R012",
    "label": "Figure 44",
    "figure_type": "source_exhibit",
    "context": "Figure 44: Agriculture commodities sectoral standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms All data as of June 30, 2026. Figure 45: Grains & oil"
  },
  {
    "figure_id": "F277",
    "report_id": "R012",
    "label": "Figure 45",
    "figure_type": "source_exhibit",
    "context": "Figure 45: Grains & oilseeds standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms All data as of June 30, 2026. Figure 46: Softs standardised level ch"
  },
  {
    "figure_id": "F278",
    "report_id": "R012",
    "label": "Figure 46",
    "figure_type": "source_exhibit",
    "context": "Figure 46: Softs standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms All data as of June 30, 2026. Figure 47: Livestock standardised level chart 0-10"
  },
  {
    "figure_id": "F279",
    "report_id": "R012",
    "label": "Figure 47",
    "figure_type": "source_exhibit",
    "context": "Figure 47: Livestock standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms All data as of June 30, 2026. Figure 48: Weekly change in total OI due to pr"
  },
  {
    "figure_id": "F280",
    "report_id": "R012",
    "label": "Figure 47",
    "figure_type": "source_exhibit",
    "context": "Figure 49: Weekly change in total OI from changes in prices USD million Figure 50: Weekly change in total OI from changes in contracts (flows) USD million"
  },
  {
    "figure_id": "F281",
    "report_id": "R012",
    "label": "Figure 48",
    "figure_type": "source_exhibit",
    "context": "Figure 48: Weekly change in total OI due to price/flows Figure 49: Weekly change in total OI from changes in prices USD million Figure 50: Weekly change in total OI from changes in contracts (flows) USD million Figure 51: Wee"
  },
  {
    "figure_id": "F282",
    "report_id": "R012",
    "label": "Figure 49",
    "figure_type": "source_exhibit",
    "context": "Figure 52: Weekly change in total OI from changes in contracts (flows)-softs and livestock"
  },
  {
    "figure_id": "F283",
    "report_id": "R012",
    "label": "Figure 50",
    "figure_type": "source_exhibit",
    "context": "Figure 50: Weekly change in total OI from changes in contracts (flows) USD million Figure 51: Weekly change in total OI from changes in contracts (flows) - grains and oilseeds Figure 52: Weekly change in total OI from changes i"
  },
  {
    "figure_id": "F284",
    "report_id": "R012",
    "label": "Figure 51",
    "figure_type": "source_exhibit",
    "context": "Figure 53: The Global Commodities Inventory Monitor is estimated on a global and ex-China basis, showing apparent inventories on a days of use basis"
  },
  {
    "figure_id": "F285",
    "report_id": "R012",
    "label": "Figure 53",
    "figure_type": "source_exhibit",
    "context": "Figure 54: The Ex-US natural gas Global Commodity Inventory Monitor is estimated on a global and ex-China basis, showing apparent inventories on a days of use basis LHS: Inventories in days of use; RHS: BCOM Price index"
  },
  {
    "figure_id": "F286",
    "report_id": "R012",
    "label": "Figure 54",
    "figure_type": "source_exhibit",
    "context": "Figure 55: China's share of world commodity inventories % Figure 56: The Global and Ex-China Commodities Inventory Monitors reported in standardised form"
  },
  {
    "figure_id": "F287",
    "report_id": "R012",
    "label": "Figure 55",
    "figure_type": "source_exhibit",
    "context": "Figure 55: China's share of world commodity inventories % Figure 56: The Global and Ex-China Commodities Inventory Monitors reported in standardised form Z-scores of global commodities inventories as days of use Figure 57: The"
  },
  {
    "figure_id": "F288",
    "report_id": "R012",
    "label": "Figure 55",
    "figure_type": "source_exhibit",
    "context": "Figure 58: Sectoral Global Commodities Inventory Monitors Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F289",
    "report_id": "R012",
    "label": "Figure 56",
    "figure_type": "source_exhibit",
    "context": "Figure 58: Sectoral Global Commodities Inventory Monitors Z-scores of global commodities inventories as days of use NB-incorporates historical revisions to standardised metals inventories"
  },
  {
    "figure_id": "F290",
    "report_id": "R012",
    "label": "Figure 57",
    "figure_type": "source_exhibit",
    "context": "Figure 59: Sectoral Ex-China Commodities Inventory Monitors Z-scores of global commodities inventories as days of use NB-incorporates historical revisions to standardized metals inventories"
  },
  {
    "figure_id": "F291",
    "report_id": "R012",
    "label": "Figure 58",
    "figure_type": "source_exhibit",
    "context": "Figure 60: Global commodities inventory seasonality Inventories as days of use Figure 61: Global commodities inventory seasonality (Ex-natural gas)"
  },
  {
    "figure_id": "F292",
    "report_id": "R012",
    "label": "Figure 59",
    "figure_type": "source_exhibit",
    "context": "Figure 61: Global commodities inventory seasonality (Ex-natural gas) Inventories as days of use Figure 62: Ex-China commodities inventory seasonality"
  },
  {
    "figure_id": "F293",
    "report_id": "R012",
    "label": "Figure 60",
    "figure_type": "source_exhibit",
    "context": "Figure 63: Ex-US natural gas Ex-China commodities inventory seasonality"
  },
  {
    "figure_id": "F294",
    "report_id": "R012",
    "label": "Figure 61",
    "figure_type": "source_exhibit",
    "context": "Figure 61: Global commodities inventory seasonality (Ex-natural gas) Inventories as days of use Figure 62: Ex-China commodities inventory seasonality Z-scores of global commodities inventories as days of use Figure 63: Ex-US na"
  },
  {
    "figure_id": "F295",
    "report_id": "R012",
    "label": "Figure 62",
    "figure_type": "source_exhibit",
    "context": "Figure 65: Oil inventories on a days of use basis"
  },
  {
    "figure_id": "F296",
    "report_id": "R012",
    "label": "Figure 63",
    "figure_type": "source_exhibit",
    "context": "Figure 63: Ex-US natural gas Ex-China commodities inventory seasonality Z-scores of global commodities inventories as days of use ## Inventories by commodity Figure 65: Oil inventories on a days of use basis Figure 66: US Nat"
  },
  {
    "figure_id": "F297",
    "report_id": "R012",
    "label": "Figure 65",
    "figure_type": "source_exhibit",
    "context": "Figure 65: Oil inventories on a days of use basis Figure 66: US Natural Gas inventories Figure 67: US Natural Gas inventories on a days of use basis Days"
  },
  {
    "figure_id": "F298",
    "report_id": "R012",
    "label": "Figure 65",
    "figure_type": "source_exhibit",
    "context": "Figure 65: Oil inventories on a days of use basis Figure 66: US Natural Gas inventories Figure 67: US Natural Gas inventories on a days of use basis Days Figure 68: Copper inventories"
  },
  {
    "figure_id": "F299",
    "report_id": "R012",
    "label": "Figure 66",
    "figure_type": "source_exhibit",
    "context": "Figure 66: US Natural Gas inventories Figure 67: US Natural Gas inventories on a days of use basis Days Figure 68: Copper inventories Figure 69: Copper inventories on a days of use basis"
  },
  {
    "figure_id": "F300",
    "report_id": "R012",
    "label": "Figure 67",
    "figure_type": "source_exhibit",
    "context": "Figure 67: US Natural Gas inventories on a days of use basis Days Figure 68: Copper inventories Figure 69: Copper inventories on a days of use basis Figure 71: Aluminium inventories on a days of use basis Days"
  },
  {
    "figure_id": "F301",
    "report_id": "R012",
    "label": "Figure 68",
    "figure_type": "source_exhibit",
    "context": "Figure 68: Copper inventories Figure 69: Copper inventories on a days of use basis Figure 71: Aluminium inventories on a days of use basis Days Figure 70: Aluminium inventories"
  },
  {
    "figure_id": "F302",
    "report_id": "R012",
    "label": "Figure 69",
    "figure_type": "source_exhibit",
    "context": "Figure 69: Copper inventories on a days of use basis Figure 71: Aluminium inventories on a days of use basis Days Figure 70: Aluminium inventories Figure 72: Zinc inventories"
  },
  {
    "figure_id": "F303",
    "report_id": "R012",
    "label": "Figure 71",
    "figure_type": "source_exhibit",
    "context": "Figure 71: Aluminium inventories on a days of use basis Days Figure 70: Aluminium inventories Figure 72: Zinc inventories Figure 73: Zinc inventories on a days of use basis"
  },
  {
    "figure_id": "F304",
    "report_id": "R012",
    "label": "Figure 70",
    "figure_type": "source_exhibit",
    "context": "Figure 70: Aluminium inventories Figure 72: Zinc inventories Figure 73: Zinc inventories on a days of use basis Figure 74: Nickel inventories"
  },
  {
    "figure_id": "F305",
    "report_id": "R012",
    "label": "Figure 72",
    "figure_type": "source_exhibit",
    "context": "Figure 72: Zinc inventories Figure 73: Zinc inventories on a days of use basis Figure 74: Nickel inventories Figure 75: Nickel inventories on a days of use basis"
  },
  {
    "figure_id": "F306",
    "report_id": "R012",
    "label": "Figure 73",
    "figure_type": "source_exhibit",
    "context": "Figure 73: Zinc inventories on a days of use basis Figure 74: Nickel inventories Figure 75: Nickel inventories on a days of use basis Figure 76: Lead inventories Thousand mt"
  },
  {
    "figure_id": "F307",
    "report_id": "R012",
    "label": "Figure 74",
    "figure_type": "source_exhibit",
    "context": "Figure 74: Nickel inventories Figure 75: Nickel inventories on a days of use basis Figure 76: Lead inventories Thousand mt Figure 77: Lead inventories on a days of use basis Days"
  },
  {
    "figure_id": "F308",
    "report_id": "R012",
    "label": "Figure 75",
    "figure_type": "source_exhibit",
    "context": "Figure 75: Nickel inventories on a days of use basis Figure 76: Lead inventories Thousand mt Figure 77: Lead inventories on a days of use basis Days Figure 78: Corn inventories"
  },
  {
    "figure_id": "F309",
    "report_id": "R012",
    "label": "Figure 76",
    "figure_type": "source_exhibit",
    "context": "Figure 76: Lead inventories Thousand mt Figure 77: Lead inventories on a days of use basis Days Figure 78: Corn inventories Figure 79: Corn inventories on a days of use basis"
  },
  {
    "figure_id": "F310",
    "report_id": "R012",
    "label": "Figure 77",
    "figure_type": "source_exhibit",
    "context": "Figure 77: Lead inventories on a days of use basis Days Figure 78: Corn inventories Figure 79: Corn inventories on a days of use basis Figure 80: Wheat inventories"
  },
  {
    "figure_id": "F311",
    "report_id": "R012",
    "label": "Figure 78",
    "figure_type": "source_exhibit",
    "context": "Figure 78: Corn inventories Figure 79: Corn inventories on a days of use basis Figure 80: Wheat inventories Figure 81: Wheat inventories on a days of use basis"
  },
  {
    "figure_id": "F312",
    "report_id": "R012",
    "label": "Figure 79",
    "figure_type": "source_exhibit",
    "context": "Figure 79: Corn inventories on a days of use basis Figure 80: Wheat inventories Figure 81: Wheat inventories on a days of use basis Figure 85: Cocoa global inventories on a days of use basis Days"
  },
  {
    "figure_id": "F313",
    "report_id": "R012",
    "label": "Figure 80",
    "figure_type": "source_exhibit",
    "context": "Figure 80: Wheat inventories Figure 81: Wheat inventories on a days of use basis Figure 85: Cocoa global inventories on a days of use basis Days Figure 82: Cotton inventories"
  },
  {
    "figure_id": "F314",
    "report_id": "R012",
    "label": "Figure 81",
    "figure_type": "source_exhibit",
    "context": "Figure 81: Wheat inventories on a days of use basis Figure 85: Cocoa global inventories on a days of use basis Days Figure 82: Cotton inventories Figure 83: Cotton inventories on a days of use basis Figure 84: Cocoa global in"
  },
  {
    "figure_id": "F315",
    "report_id": "R012",
    "label": "Figure 85",
    "figure_type": "source_exhibit",
    "context": "Figure 85: Cocoa global inventories on a days of use basis Days Figure 82: Cotton inventories Figure 83: Cotton inventories on a days of use basis Figure 84: Cocoa global inventories"
  },
  {
    "figure_id": "F316",
    "report_id": "R012",
    "label": "Figure 83",
    "figure_type": "source_exhibit",
    "context": "Figure 83: Cotton inventories on a days of use basis Figure 84: Cocoa global inventories Figure 86: Coffee inventories"
  },
  {
    "figure_id": "F317",
    "report_id": "R012",
    "label": "Figure 83",
    "figure_type": "source_exhibit",
    "context": "Figure 83: Cotton inventories on a days of use basis Figure 84: Cocoa global inventories Figure 86: Coffee inventories Figure 87: Coffee inventories on a days of use basis"
  },
  {
    "figure_id": "F318",
    "report_id": "R012",
    "label": "Figure 84",
    "figure_type": "source_exhibit",
    "context": "Figure 84: Cocoa global inventories Figure 86: Coffee inventories Figure 87: Coffee inventories on a days of use basis Figure 88: Sugar global inventories"
  },
  {
    "figure_id": "F319",
    "report_id": "R012",
    "label": "Figure 86",
    "figure_type": "source_exhibit",
    "context": "Figure 86: Coffee inventories Figure 87: Coffee inventories on a days of use basis Figure 88: Sugar global inventories 1,000 tonnes Figure 89: Sugar global inventories on a days of use basis"
  },
  {
    "figure_id": "F320",
    "report_id": "R012",
    "label": "Figure 87",
    "figure_type": "source_exhibit",
    "context": "Figure 87: Coffee inventories on a days of use basis Figure 88: Sugar global inventories 1,000 tonnes Figure 89: Sugar global inventories on a days of use basis Figure 90: Soybean inventories"
  },
  {
    "figure_id": "F321",
    "report_id": "R012",
    "label": "Figure 88",
    "figure_type": "source_exhibit",
    "context": "Figure 88: Sugar global inventories 1,000 tonnes Figure 89: Sugar global inventories on a days of use basis Figure 90: Soybean inventories Figure 91: Soybean inventories on a days of use basis"
  },
  {
    "figure_id": "F322",
    "report_id": "R012",
    "label": "Figure 89",
    "figure_type": "source_exhibit",
    "context": "Figure 89: Sugar global inventories on a days of use basis Figure 90: Soybean inventories Figure 91: Soybean inventories on a days of use basis Figure 92: Soybean Meal inventories"
  },
  {
    "figure_id": "F323",
    "report_id": "R012",
    "label": "Figure 90",
    "figure_type": "source_exhibit",
    "context": "Figure 90: Soybean inventories Figure 91: Soybean inventories on a days of use basis Figure 92: Soybean Meal inventories Figure 93: Soybean Meal inventories on a days of use basis Days"
  },
  {
    "figure_id": "F324",
    "report_id": "R012",
    "label": "Figure 91",
    "figure_type": "source_exhibit",
    "context": "Figure 91: Soybean inventories on a days of use basis Figure 92: Soybean Meal inventories Figure 93: Soybean Meal inventories on a days of use basis Days Figure 94: Soybean Oil inventories 1,000 tonnes"
  },
  {
    "figure_id": "F325",
    "report_id": "R012",
    "label": "Figure 92",
    "figure_type": "source_exhibit",
    "context": "Figure 92: Soybean Meal inventories Figure 93: Soybean Meal inventories on a days of use basis Days Figure 94: Soybean Oil inventories 1,000 tonnes Figure 95: Soybean Oil inventories on a days of use basis Days"
  },
  {
    "figure_id": "F326",
    "report_id": "R012",
    "label": "Figure 93",
    "figure_type": "source_exhibit",
    "context": "Figure 93: Soybean Meal inventories on a days of use basis Days Figure 94: Soybean Oil inventories 1,000 tonnes Figure 95: Soybean Oil inventories on a days of use basis Days"
  },
  {
    "figure_id": "F327",
    "report_id": "R012",
    "label": "Figure 94",
    "figure_type": "source_exhibit",
    "context": "Figure 94: Soybean Oil inventories 1,000 tonnes Figure 95: Soybean Oil inventories on a days of use basis Days ## ICE Brent crude oil Contracts (futures and options)"
  },
  {
    "figure_id": "F328",
    "report_id": "R012",
    "label": "Figure 96",
    "figure_type": "source_exhibit",
    "context": "Figure 96: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 97: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl Figure 98: Weekly change in OI from changes in contracts & p"
  },
  {
    "figure_id": "F329",
    "report_id": "R012",
    "label": "Figure 96",
    "figure_type": "source_exhibit",
    "context": "Figure 96: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 97: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl Figure 98: Weekly change in OI from changes in contracts & p"
  },
  {
    "figure_id": "F330",
    "report_id": "R012",
    "label": "Figure 97",
    "figure_type": "source_exhibit",
    "context": "Figure 97: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl Figure 98: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 99: Open interest share by trader type % Figu"
  },
  {
    "figure_id": "F331",
    "report_id": "R012",
    "label": "Figure 98",
    "figure_type": "source_exhibit",
    "context": "Figure 98: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 99: Open interest share by trader type % Figure 100: Seasonal Managed Money net length Lots (1,000) Figure 101: Price"
  },
  {
    "figure_id": "F332",
    "report_id": "R012",
    "label": "Figure 99",
    "figure_type": "source_exhibit",
    "context": "Figure 99: Open interest share by trader type % Figure 100: Seasonal Managed Money net length Lots (1,000) Figure 101: Price momentum ## NYM WTI crude oil"
  },
  {
    "figure_id": "F333",
    "report_id": "R012",
    "label": "Figure 100",
    "figure_type": "source_exhibit",
    "context": "Figure 100: Seasonal Managed Money net length Lots (1,000) Figure 101: Price momentum ## NYM WTI crude oil Contracts (futures and options)"
  },
  {
    "figure_id": "F334",
    "report_id": "R012",
    "label": "Figure 102",
    "figure_type": "source_exhibit",
    "context": "Figure 102: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 103: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl"
  },
  {
    "figure_id": "F335",
    "report_id": "R012",
    "label": "Figure 103",
    "figure_type": "source_exhibit",
    "context": "Figure 103: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl Figure 104: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F336",
    "report_id": "R012",
    "label": "Figure 104",
    "figure_type": "source_exhibit",
    "context": "Figure 104: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 105: Open interest share by trader type % Figure 106: Seasonal Managed Money net length"
  },
  {
    "figure_id": "F337",
    "report_id": "R012",
    "label": "Figure 104",
    "figure_type": "source_exhibit",
    "context": "Figure 104: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 105: Open interest share by trader type % Figure 106: Seasonal Managed Money net length Figure 107: Price momentum"
  },
  {
    "figure_id": "F338",
    "report_id": "R012",
    "label": "Figure 105",
    "figure_type": "source_exhibit",
    "context": "Figure 105: Open interest share by trader type % Figure 106: Seasonal Managed Money net length Figure 107: Price momentum ## NYM RBOB Gasoline"
  },
  {
    "figure_id": "F339",
    "report_id": "R012",
    "label": "Figure 106",
    "figure_type": "source_exhibit",
    "context": "Figure 106: Seasonal Managed Money net length Figure 107: Price momentum ## NYM RBOB Gasoline Contracts (futures and options)"
  },
  {
    "figure_id": "F340",
    "report_id": "R012",
    "label": "Figure 108",
    "figure_type": "source_exhibit",
    "context": "Figure 108: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 109: Gross PMPU position and price LHS: lots (1,000), RHS: USc/gal"
  },
  {
    "figure_id": "F341",
    "report_id": "R012",
    "label": "Figure 109",
    "figure_type": "source_exhibit",
    "context": "Figure 109: Gross PMPU position and price LHS: lots (1,000), RHS: USc/gal Figure 110: Weekly change in OI from changes in contracts & price Figure 111: Open interest share by trader type % US\\$ million (futures and options)"
  },
  {
    "figure_id": "F342",
    "report_id": "R012",
    "label": "Figure 110",
    "figure_type": "source_exhibit",
    "context": "Figure 110: Weekly change in OI from changes in contracts & price Figure 111: Open interest share by trader type % US\\$ million (futures and options) Figure 112: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F343",
    "report_id": "R012",
    "label": "Figure 110",
    "figure_type": "source_exhibit",
    "context": "Figure 110: Weekly change in OI from changes in contracts & price Figure 111: Open interest share by trader type % US\\$ million (futures and options) Figure 112: Seasonal Managed Money net length Lots (1,000) Figure 113: Price"
  },
  {
    "figure_id": "F344",
    "report_id": "R012",
    "label": "Figure 112",
    "figure_type": "source_exhibit",
    "context": "Figure 112: Seasonal Managed Money net length Lots (1,000) Figure 113: Price momentum LHS: Z-score, RHS: USc/gal ## ICE Gasoil"
  },
  {
    "figure_id": "F345",
    "report_id": "R012",
    "label": "Figure 112",
    "figure_type": "source_exhibit",
    "context": "Figure 112: Seasonal Managed Money net length Lots (1,000) Figure 113: Price momentum LHS: Z-score, RHS: USc/gal ## ICE Gasoil Contracts (futures and options)"
  },
  {
    "figure_id": "F346",
    "report_id": "R012",
    "label": "Figure 114",
    "figure_type": "source_exhibit",
    "context": "Figure 114: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 115: Gross PMPU position and price LHS: lots (1,000), RHS: USD/T"
  },
  {
    "figure_id": "F347",
    "report_id": "R012",
    "label": "Figure 115",
    "figure_type": "source_exhibit",
    "context": "Figure 115: Gross PMPU position and price LHS: lots (1,000), RHS: USD/T Figure 116: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F348",
    "report_id": "R012",
    "label": "Figure 116",
    "figure_type": "source_exhibit",
    "context": "Figure 116: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 117: Open interest share by trader type % Figure 118: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F349",
    "report_id": "R012",
    "label": "Figure 116",
    "figure_type": "source_exhibit",
    "context": "Figure 116: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 117: Open interest share by trader type % Figure 118: Seasonal Managed Money net length Lots (1,000) Figure 119: Price"
  },
  {
    "figure_id": "F350",
    "report_id": "R012",
    "label": "Figure 117",
    "figure_type": "source_exhibit",
    "context": "Figure 117: Open interest share by trader type % Figure 118: Seasonal Managed Money net length Lots (1,000) Figure 119: Price momentum LHS: Z-score, RHS: USD/T ## NYM Natural Gas"
  },
  {
    "figure_id": "F351",
    "report_id": "R012",
    "label": "Figure 118",
    "figure_type": "source_exhibit",
    "context": "Figure 118: Seasonal Managed Money net length Lots (1,000) Figure 119: Price momentum LHS: Z-score, RHS: USD/T ## NYM Natural Gas Contracts (futures and options)"
  },
  {
    "figure_id": "F352",
    "report_id": "R012",
    "label": "Figure 120",
    "figure_type": "source_exhibit",
    "context": "Figure 120: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 121: Gross PMPU position and price LHS: lots (1,000), RHS: USD/mmbtu"
  },
  {
    "figure_id": "F353",
    "report_id": "R012",
    "label": "Figure 121",
    "figure_type": "source_exhibit",
    "context": "Figure 121: Gross PMPU position and price LHS: lots (1,000), RHS: USD/mmbtu Figure 122: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F354",
    "report_id": "R012",
    "label": "Figure 122",
    "figure_type": "source_exhibit",
    "context": "Figure 122: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 123: Open interest share by trader type % Figure 124: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F355",
    "report_id": "R012",
    "label": "Figure 122",
    "figure_type": "source_exhibit",
    "context": "Figure 122: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 123: Open interest share by trader type % Figure 124: Seasonal Managed Money net length Lots (1,000) Figure 125: Price"
  },
  {
    "figure_id": "F356",
    "report_id": "R012",
    "label": "Figure 123",
    "figure_type": "source_exhibit",
    "context": "Figure 123: Open interest share by trader type % Figure 124: Seasonal Managed Money net length Lots (1,000) Figure 125: Price momentum LHS: Z-score, RHS: USD/mmbtu ## ICE Endex TTF Natgas"
  },
  {
    "figure_id": "F357",
    "report_id": "R012",
    "label": "Figure 124",
    "figure_type": "source_exhibit",
    "context": "Figure 124: Seasonal Managed Money net length Lots (1,000) Figure 125: Price momentum LHS: Z-score, RHS: USD/mmbtu ## ICE Endex TTF Natgas Contracts in MWh (futures and options)"
  },
  {
    "figure_id": "F358",
    "report_id": "R012",
    "label": "Figure 126",
    "figure_type": "source_exhibit",
    "context": "Figure 126: Weekly change in open interest by trading group US\\$ billion (futures and options, contracts in MWh) Figure 127: Gross commercial position and price LHS: MWh (million), RHS: EUR/MWh Figure 128: Weekly change in OI fr"
  },
  {
    "figure_id": "F359",
    "report_id": "R012",
    "label": "Figure 126",
    "figure_type": "source_exhibit",
    "context": "Figure 129: Open interest share by trader type %"
  },
  {
    "figure_id": "F360",
    "report_id": "R012",
    "label": "Figure 127",
    "figure_type": "source_exhibit",
    "context": "Figure 130: Seasonal Investment funds net length"
  },
  {
    "figure_id": "F361",
    "report_id": "R012",
    "label": "Figure 128",
    "figure_type": "source_exhibit",
    "context": "Figure 128: Weekly change in OI from changes in contracts & price US\\$ billion (futures and options, contracts in MWh) Figure 129: Open interest share by trader type % Figure 130: Seasonal Investment funds net length Figure 13"
  },
  {
    "figure_id": "F362",
    "report_id": "R012",
    "label": "Figure 129",
    "figure_type": "source_exhibit",
    "context": "Figure 129: Open interest share by trader type % Figure 130: Seasonal Investment funds net length Figure 131: Price momentum LHS: Z-score, RHS: EUR/Mwh ## ICE EUA"
  },
  {
    "figure_id": "F363",
    "report_id": "R012",
    "label": "Figure 130",
    "figure_type": "source_exhibit",
    "context": "Figure 130: Seasonal Investment funds net length Figure 131: Price momentum LHS: Z-score, RHS: EUR/Mwh ## ICE EUA Figure 137: Price momentum LHS: Z-score, RHS: EUR/MtCO2e. Contracts (futures and options)"
  },
  {
    "figure_id": "F364",
    "report_id": "R012",
    "label": "Figure 132",
    "figure_type": "source_exhibit",
    "context": "Figure 132: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 133: Gross commercial position and price LHS: lots (1,000), RHS: EUR/MtCO2e Figure 134: Weekly change in OI from changes in co"
  },
  {
    "figure_id": "F365",
    "report_id": "R012",
    "label": "Figure 132",
    "figure_type": "source_exhibit",
    "context": "Figure 132: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 133: Gross commercial position and price LHS: lots (1,000), RHS: EUR/MtCO2e Figure 134: Weekly change in OI from changes in co"
  },
  {
    "figure_id": "F366",
    "report_id": "R012",
    "label": "Figure 134",
    "figure_type": "source_exhibit",
    "context": "Figure 134: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 135: Open interest share by trader type % Figure 136: Seasonal Investment funds net length"
  },
  {
    "figure_id": "F367",
    "report_id": "R012",
    "label": "Figure 134",
    "figure_type": "source_exhibit",
    "context": "Figure 134: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 135: Open interest share by trader type % Figure 136: Seasonal Investment funds net length"
  },
  {
    "figure_id": "F368",
    "report_id": "R012",
    "label": "Figure 135",
    "figure_type": "source_exhibit",
    "context": "Figure 135: Open interest share by trader type % Figure 136: Seasonal Investment funds net length ## CMX Gold Contracts (futures and options)"
  },
  {
    "figure_id": "F369",
    "report_id": "R012",
    "label": "Figure 135",
    "figure_type": "source_exhibit",
    "context": "Figure 135: Open interest share by trader type % Figure 136: Seasonal Investment funds net length ## CMX Gold Contracts (futures and options)"
  },
  {
    "figure_id": "F370",
    "report_id": "R012",
    "label": "Figure 138",
    "figure_type": "source_exhibit",
    "context": "Figure 138: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 139: Gross PMPU position and price LHS: lots (1,000), RHS: USD/t oz."
  },
  {
    "figure_id": "F371",
    "report_id": "R012",
    "label": "Figure 139",
    "figure_type": "source_exhibit",
    "context": "Figure 139: Gross PMPU position and price LHS: lots (1,000), RHS: USD/t oz. Figure 140: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F372",
    "report_id": "R012",
    "label": "Figure 140",
    "figure_type": "source_exhibit",
    "context": "Figure 140: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 141: Open interest share by trader type % Figure 142: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F373",
    "report_id": "R012",
    "label": "Figure 140",
    "figure_type": "source_exhibit",
    "context": "Figure 140: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 141: Open interest share by trader type % Figure 142: Seasonal Managed Money net length Lots (1,000) Figure 143: Price"
  },
  {
    "figure_id": "F374",
    "report_id": "R012",
    "label": "Figure 141",
    "figure_type": "source_exhibit",
    "context": "Figure 141: Open interest share by trader type % Figure 142: Seasonal Managed Money net length Lots (1,000) Figure 143: Price momentum LHS: Z-score, RHS: USD/t oz. ## CMX Silver"
  },
  {
    "figure_id": "F375",
    "report_id": "R012",
    "label": "Figure 142",
    "figure_type": "source_exhibit",
    "context": "Figure 142: Seasonal Managed Money net length Lots (1,000) Figure 143: Price momentum LHS: Z-score, RHS: USD/t oz. ## CMX Silver Contracts (futures and options)"
  },
  {
    "figure_id": "F376",
    "report_id": "R012",
    "label": "Figure 144",
    "figure_type": "source_exhibit",
    "context": "Figure 144: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 145: Gross PMPU position and price % Figure 146: Weekly change in OI from changes in contracts & price"
  },
  {
    "figure_id": "F377",
    "report_id": "R012",
    "label": "Figure 144",
    "figure_type": "source_exhibit",
    "context": "Figure 144: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 145: Gross PMPU position and price % Figure 146: Weekly change in OI from changes in contracts & price US\\$ million (futures a"
  },
  {
    "figure_id": "F378",
    "report_id": "R012",
    "label": "Figure 145",
    "figure_type": "source_exhibit",
    "context": "Figure 145: Gross PMPU position and price % Figure 146: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 147: Open interest share by trader type % Figure 148: Seasonal Managed Mon"
  },
  {
    "figure_id": "F379",
    "report_id": "R012",
    "label": "Figure 146",
    "figure_type": "source_exhibit",
    "context": "Figure 146: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 147: Open interest share by trader type % Figure 148: Seasonal Managed Money net length Lots (1,000) Figure 149: Price"
  },
  {
    "figure_id": "F380",
    "report_id": "R012",
    "label": "Figure 147",
    "figure_type": "source_exhibit",
    "context": "Figure 147: Open interest share by trader type % Figure 148: Seasonal Managed Money net length Lots (1,000) Figure 149: Price momentum ## CMX Copper"
  },
  {
    "figure_id": "F381",
    "report_id": "R012",
    "label": "Figure 148",
    "figure_type": "source_exhibit",
    "context": "Figure 148: Seasonal Managed Money net length Lots (1,000) Figure 149: Price momentum ## CMX Copper Contracts (futures and options)"
  },
  {
    "figure_id": "F382",
    "report_id": "R012",
    "label": "Figure 150",
    "figure_type": "source_exhibit",
    "context": "Figure 150: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 151: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 152: Weekly change in OI from changes in contracts &"
  },
  {
    "figure_id": "F383",
    "report_id": "R012",
    "label": "Figure 150",
    "figure_type": "source_exhibit",
    "context": "Figure 150: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 151: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 152: Weekly change in OI from changes in contracts &"
  },
  {
    "figure_id": "F384",
    "report_id": "R012",
    "label": "Figure 152",
    "figure_type": "source_exhibit",
    "context": "Figure 152: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 153: Open interest share by trader type % Figure 154: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F385",
    "report_id": "R012",
    "label": "Figure 152",
    "figure_type": "source_exhibit",
    "context": "Figure 152: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 153: Open interest share by trader type % Figure 154: Seasonal Managed Money net length Lots (1,000) Figure 155: Price"
  },
  {
    "figure_id": "F386",
    "report_id": "R012",
    "label": "Figure 153",
    "figure_type": "source_exhibit",
    "context": "Figure 153: Open interest share by trader type % Figure 154: Seasonal Managed Money net length Lots (1,000) Figure 155: Price momentum LHS: Z-score, RHS: USc/lb ## NYM Platinum"
  },
  {
    "figure_id": "F387",
    "report_id": "R012",
    "label": "Figure 154",
    "figure_type": "source_exhibit",
    "context": "Figure 154: Seasonal Managed Money net length Lots (1,000) Figure 155: Price momentum LHS: Z-score, RHS: USc/lb ## NYM Platinum Contracts (futures and options)"
  },
  {
    "figure_id": "F388",
    "report_id": "R012",
    "label": "Figure 156",
    "figure_type": "source_exhibit",
    "context": "Figure 156: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 157: Gross PMPU position and price LHS: lots (1,000), RHS: USD/t oz."
  },
  {
    "figure_id": "F389",
    "report_id": "R012",
    "label": "Figure 157",
    "figure_type": "source_exhibit",
    "context": "Figure 157: Gross PMPU position and price LHS: lots (1,000), RHS: USD/t oz. Figure 158: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 159: Open interest share by trader type %"
  },
  {
    "figure_id": "F390",
    "report_id": "R012",
    "label": "Figure 158",
    "figure_type": "source_exhibit",
    "context": "Figure 158: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 159: Open interest share by trader type % Figure 160: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F391",
    "report_id": "R012",
    "label": "Figure 158",
    "figure_type": "source_exhibit",
    "context": "Figure 158: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 159: Open interest share by trader type % Figure 160: Seasonal Managed Money net length Lots (1,000) Figure 161: Price"
  },
  {
    "figure_id": "F392",
    "report_id": "R012",
    "label": "Figure 160",
    "figure_type": "source_exhibit",
    "context": "Figure 160: Seasonal Managed Money net length Lots (1,000) Figure 161: Price momentum LHS: Z-score, RHS: USD/t oz. ## CBOT Corn"
  },
  {
    "figure_id": "F393",
    "report_id": "R012",
    "label": "Figure 160",
    "figure_type": "source_exhibit",
    "context": "Figure 160: Seasonal Managed Money net length Lots (1,000) Figure 161: Price momentum LHS: Z-score, RHS: USD/t oz. ## CBOT Corn Contracts (futures and options)"
  },
  {
    "figure_id": "F394",
    "report_id": "R012",
    "label": "Figure 162",
    "figure_type": "source_exhibit",
    "context": "Figure 162: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 163: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu"
  },
  {
    "figure_id": "F395",
    "report_id": "R012",
    "label": "Figure 163",
    "figure_type": "source_exhibit",
    "context": "Figure 163: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu Figure 164: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F396",
    "report_id": "R012",
    "label": "Figure 164",
    "figure_type": "source_exhibit",
    "context": "Figure 164: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 165: Open interest share by trader type % Figure 166: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F397",
    "report_id": "R012",
    "label": "Figure 164",
    "figure_type": "source_exhibit",
    "context": "Figure 164: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 165: Open interest share by trader type % Figure 166: Seasonal Managed Money net length Lots (1,000) Figure 167: Price"
  },
  {
    "figure_id": "F398",
    "report_id": "R012",
    "label": "Figure 165",
    "figure_type": "source_exhibit",
    "context": "Figure 165: Open interest share by trader type % Figure 166: Seasonal Managed Money net length Lots (1,000) Figure 167: Price momentum LHS: Z-score, RHS: USc/bu ## CBOT Soybeans"
  },
  {
    "figure_id": "F399",
    "report_id": "R012",
    "label": "Figure 166",
    "figure_type": "source_exhibit",
    "context": "Figure 166: Seasonal Managed Money net length Lots (1,000) Figure 167: Price momentum LHS: Z-score, RHS: USc/bu ## CBOT Soybeans Contracts (futures and options)"
  },
  {
    "figure_id": "F400",
    "report_id": "R012",
    "label": "Figure 168",
    "figure_type": "source_exhibit",
    "context": "Figure 168: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 169: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu"
  },
  {
    "figure_id": "F401",
    "report_id": "R012",
    "label": "Figure 169",
    "figure_type": "source_exhibit",
    "context": "Figure 169: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu Figure 170: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 171: Open interest share by trader type %"
  },
  {
    "figure_id": "F402",
    "report_id": "R012",
    "label": "Figure 170",
    "figure_type": "source_exhibit",
    "context": "Figure 170: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 171: Open interest share by trader type % Figure 172: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F403",
    "report_id": "R012",
    "label": "Figure 170",
    "figure_type": "source_exhibit",
    "context": "Figure 170: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 171: Open interest share by trader type % Figure 172: Seasonal Managed Money net length Lots (1,000) Figure 173: Price"
  },
  {
    "figure_id": "F404",
    "report_id": "R012",
    "label": "Figure 172",
    "figure_type": "source_exhibit",
    "context": "Figure 172: Seasonal Managed Money net length Lots (1,000) Figure 173: Price momentum LHS: Z-score, RHS: USc/bu ## CBOT Wheat"
  },
  {
    "figure_id": "F405",
    "report_id": "R012",
    "label": "Figure 172",
    "figure_type": "source_exhibit",
    "context": "Figure 172: Seasonal Managed Money net length Lots (1,000) Figure 173: Price momentum LHS: Z-score, RHS: USc/bu ## CBOT Wheat Contracts (futures and options)"
  },
  {
    "figure_id": "F406",
    "report_id": "R012",
    "label": "Figure 174",
    "figure_type": "source_exhibit",
    "context": "Figure 174: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 175: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu Figure 176: Weekly change in OI from changes in contracts & pr"
  },
  {
    "figure_id": "F407",
    "report_id": "R012",
    "label": "Figure 175",
    "figure_type": "source_exhibit",
    "context": "Figure 175: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu Figure 176: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 177: Open interest share by trader type %"
  },
  {
    "figure_id": "F408",
    "report_id": "R012",
    "label": "Figure 176",
    "figure_type": "source_exhibit",
    "context": "Figure 176: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 177: Open interest share by trader type % Figure 178: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F409",
    "report_id": "R012",
    "label": "Figure 177",
    "figure_type": "source_exhibit",
    "context": "Figure 177: Open interest share by trader type % Figure 178: Seasonal Managed Money net length Lots (1,000) Figure 179: Price momentum"
  },
  {
    "figure_id": "F410",
    "report_id": "R012",
    "label": "Figure 177",
    "figure_type": "source_exhibit",
    "context": "Figure 177: Open interest share by trader type % Figure 178: Seasonal Managed Money net length Lots (1,000) Figure 179: Price momentum LHS: Z-score, RHS: USc/bu ## ICE Sugar No. 11"
  },
  {
    "figure_id": "F411",
    "report_id": "R012",
    "label": "Figure 178",
    "figure_type": "source_exhibit",
    "context": "Figure 178: Seasonal Managed Money net length Lots (1,000) Figure 179: Price momentum LHS: Z-score, RHS: USc/bu ## ICE Sugar No. 11 Contracts (futures and options)"
  },
  {
    "figure_id": "F412",
    "report_id": "R012",
    "label": "Figure 180",
    "figure_type": "source_exhibit",
    "context": "Figure 180: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 181: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F413",
    "report_id": "R012",
    "label": "Figure 181",
    "figure_type": "source_exhibit",
    "context": "Figure 181: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 182: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 183: Open interest share by trader type %"
  },
  {
    "figure_id": "F414",
    "report_id": "R012",
    "label": "Figure 182",
    "figure_type": "source_exhibit",
    "context": "Figure 182: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 183: Open interest share by trader type % Figure 184: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F415",
    "report_id": "R012",
    "label": "Figure 182",
    "figure_type": "source_exhibit",
    "context": "Figure 182: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 183: Open interest share by trader type % Figure 184: Seasonal Managed Money net length Lots (1,000) Figure 185: Price"
  },
  {
    "figure_id": "F416",
    "report_id": "R012",
    "label": "Figure 184",
    "figure_type": "source_exhibit",
    "context": "Figure 184: Seasonal Managed Money net length Lots (1,000) Figure 185: Price momentum LHS: Z-score, RHS: USc/lb ## ICE Cotton No. 2"
  },
  {
    "figure_id": "F417",
    "report_id": "R012",
    "label": "Figure 184",
    "figure_type": "source_exhibit",
    "context": "Figure 184: Seasonal Managed Money net length Lots (1,000) Figure 185: Price momentum LHS: Z-score, RHS: USc/lb ## ICE Cotton No. 2 Contracts (futures and options)"
  },
  {
    "figure_id": "F418",
    "report_id": "R012",
    "label": "Figure 186",
    "figure_type": "source_exhibit",
    "context": "Figure 186: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 187: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F419",
    "report_id": "R012",
    "label": "Figure 187",
    "figure_type": "source_exhibit",
    "context": "Figure 187: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 188: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F420",
    "report_id": "R012",
    "label": "Figure 188",
    "figure_type": "source_exhibit",
    "context": "Figure 188: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 189: Open interest share by trader type % Figure 190: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F421",
    "report_id": "R012",
    "label": "Figure 188",
    "figure_type": "source_exhibit",
    "context": "Figure 188: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 189: Open interest share by trader type % Figure 190: Seasonal Managed Money net length Lots (1,000) Figure 191: Price"
  },
  {
    "figure_id": "F422",
    "report_id": "R012",
    "label": "Figure 189",
    "figure_type": "source_exhibit",
    "context": "Figure 189: Open interest share by trader type % Figure 190: Seasonal Managed Money net length Lots (1,000) Figure 191: Price momentum LHS: Z-score, RHS: USc/lb ## ICE Coffee"
  },
  {
    "figure_id": "F423",
    "report_id": "R012",
    "label": "Figure 190",
    "figure_type": "source_exhibit",
    "context": "Figure 190: Seasonal Managed Money net length Lots (1,000) Figure 191: Price momentum LHS: Z-score, RHS: USc/lb ## ICE Coffee Contracts (futures and options)"
  },
  {
    "figure_id": "F424",
    "report_id": "R012",
    "label": "Figure 192",
    "figure_type": "source_exhibit",
    "context": "Figure 192: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 193: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F425",
    "report_id": "R012",
    "label": "Figure 193",
    "figure_type": "source_exhibit",
    "context": "Figure 193: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 194: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F426",
    "report_id": "R012",
    "label": "Figure 194",
    "figure_type": "source_exhibit",
    "context": "Figure 194: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 195: Open interest share by trader type % Figure 196: Seasonal Managed Money net Lots (1,000)"
  },
  {
    "figure_id": "F427",
    "report_id": "R012",
    "label": "Figure 194",
    "figure_type": "source_exhibit",
    "context": "Figure 194: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 195: Open interest share by trader type % Figure 196: Seasonal Managed Money net Lots (1,000) Figure 197: Price moment"
  },
  {
    "figure_id": "F428",
    "report_id": "R012",
    "label": "Figure 195",
    "figure_type": "source_exhibit",
    "context": "Figure 195: Open interest share by trader type % Figure 196: Seasonal Managed Money net Lots (1,000) Figure 197: Price momentum LHS: Z-score, RHS: USc/lb ## ICE Cocoa"
  },
  {
    "figure_id": "F429",
    "report_id": "R012",
    "label": "Figure 196",
    "figure_type": "source_exhibit",
    "context": "Figure 196: Seasonal Managed Money net Lots (1,000) Figure 197: Price momentum LHS: Z-score, RHS: USc/lb ## ICE Cocoa Contracts (futures and options)"
  },
  {
    "figure_id": "F430",
    "report_id": "R012",
    "label": "Figure 198",
    "figure_type": "source_exhibit",
    "context": "Figure 198: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 199: Gross PMPU position and price LHS: lots (1,000), RHS: USd/MT"
  },
  {
    "figure_id": "F431",
    "report_id": "R012",
    "label": "Figure 199",
    "figure_type": "source_exhibit",
    "context": "Figure 199: Gross PMPU position and price LHS: lots (1,000), RHS: USd/MT Figure 200: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F432",
    "report_id": "R012",
    "label": "Figure 200",
    "figure_type": "source_exhibit",
    "context": "Figure 200: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 201: Open interest share by trader type % Figure 202: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F433",
    "report_id": "R012",
    "label": "Figure 200",
    "figure_type": "source_exhibit",
    "context": "Figure 200: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 201: Open interest share by trader type % Figure 202: Seasonal Managed Money net length Lots (1,000) Figure 203: Price"
  },
  {
    "figure_id": "F434",
    "report_id": "R012",
    "label": "Figure 201",
    "figure_type": "source_exhibit",
    "context": "Figure 201: Open interest share by trader type % Figure 202: Seasonal Managed Money net length Lots (1,000) Figure 203: Price momentum ## CME Live Cattle"
  },
  {
    "figure_id": "F435",
    "report_id": "R012",
    "label": "Figure 202",
    "figure_type": "source_exhibit",
    "context": "Figure 202: Seasonal Managed Money net length Lots (1,000) Figure 203: Price momentum ## CME Live Cattle Contracts (futures and options)"
  },
  {
    "figure_id": "F436",
    "report_id": "R012",
    "label": "Figure 204",
    "figure_type": "source_exhibit",
    "context": "Figure 204: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 205: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F437",
    "report_id": "R012",
    "label": "Figure 205",
    "figure_type": "source_exhibit",
    "context": "Figure 205: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 206: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F438",
    "report_id": "R012",
    "label": "Figure 206",
    "figure_type": "source_exhibit",
    "context": "Figure 206: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 207: Open interest share by trader type % Figure 208: Seasonal Managed Money net length"
  },
  {
    "figure_id": "F439",
    "report_id": "R012",
    "label": "Figure 206",
    "figure_type": "source_exhibit",
    "context": "Figure 206: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 207: Open interest share by trader type % Figure 208: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F440",
    "report_id": "R012",
    "label": "Figure 207",
    "figure_type": "source_exhibit",
    "context": "Figure 207: Open interest share by trader type % Figure 208: Seasonal Managed Money net length Lots (1,000) ## CME Lean Hogs Contracts (futures and options)"
  },
  {
    "figure_id": "F441",
    "report_id": "R012",
    "label": "Figure 209",
    "figure_type": "source_exhibit",
    "context": "Figure 209: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 210: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 211: Weekly change in OI from changes in contracts &"
  },
  {
    "figure_id": "F442",
    "report_id": "R012",
    "label": "Figure 209",
    "figure_type": "source_exhibit",
    "context": "Figure 209: Weekly change in open interest by trading group US\\$ million (futures and options) Figure 210: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb Figure 211: Weekly change in OI from changes in contracts &"
  },
  {
    "figure_id": "F443",
    "report_id": "R012",
    "label": "Figure 211",
    "figure_type": "source_exhibit",
    "context": "Figure 211: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 212: Open interest share by trader type % Figure 213: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F444",
    "report_id": "R012",
    "label": "Figure 211",
    "figure_type": "source_exhibit",
    "context": "Figure 211: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 212: Open interest share by trader type % Figure 213: Seasonal Managed Money net length Lots (1,000) ## Disclosures"
  },
  {
    "figure_id": "F445",
    "report_id": "R012",
    "label": "Figure 212",
    "figure_type": "source_exhibit",
    "context": "Figure 212: Open interest share by trader type % Figure 213: Seasonal Managed Money net length Lots (1,000) ## Disclosures ## History of Investment Recommendations:"
  },
  {
    "figure_id": "F446",
    "report_id": "R014",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Mobis: 1-year fwd. P/E trend Figure 2: Mobis: net profit trend Wbn, %"
  },
  {
    "figure_id": "F447",
    "report_id": "R014",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Mobis: 1-year fwd. P/E trend Figure 2: Mobis: net profit trend Wbn, %"
  },
  {
    "figure_id": "F448",
    "report_id": "R014",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Mando: 1-year fwd. P/E trend Figure 4: Mando: net profit trend Price Performance"
  },
  {
    "figure_id": "F449",
    "report_id": "R014",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Mando: 1-year fwd. P/E trend Figure 4: Mando: net profit trend Price Performance — 204320.KS Price (W) — KOSPI (rebased)"
  },
  {
    "figure_id": "F450",
    "report_id": "R014",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Mando: net profit trend Price Performance — 204320.KS Price (W) — KOSPI (rebased) Company Data"
  },
  {
    "figure_id": "F451",
    "report_id": "R015",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 1: TOPIX Bank Index and JGB 10-year yield Figure 2: Share price performance (1M)"
  },
  {
    "figure_id": "F452",
    "report_id": "R015",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: YoY growth in domestic loans and deposits Figure 9: YoY growth in outstanding lending in Japan (average balance; by subsegment) Figure 10: YoY growth in outstanding lending at city banks by borrower category"
  },
  {
    "figure_id": "F453",
    "report_id": "R015",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: YoY growth in domestic loans and deposits Figure 9: YoY growth in outstanding lending in Japan (average balance; by subsegment) Figure 10: YoY growth in outstanding lending at city banks by borrower category Figure"
  },
  {
    "figure_id": "F454",
    "report_id": "R015",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Growth in outstanding lending (consolidated-basis, excl. public loans) and monthly BoJ statistics"
  },
  {
    "figure_id": "F455",
    "report_id": "R015",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: YoY growth in outstanding lending at city banks by borrower category Figure 11: YoY growth in outstanding lending at regional banks by borrower category Note: Total for tier I and tier II regional banks. Figure 12: G"
  },
  {
    "figure_id": "F456",
    "report_id": "R015",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Lending interest rates at city banks Figure 14: Lending interest rates at regional banks"
  },
  {
    "figure_id": "F457",
    "report_id": "R015",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Lending interest rates at city banks Figure 14: Lending interest rates at regional banks Figure 15: 3M TIBOR: Since 2000"
  },
  {
    "figure_id": "F458",
    "report_id": "R015",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Lending interest rates at city banks Figure 14: Lending interest rates at regional banks Figure 15: 3M TIBOR: Since 2000 Figure 16: 3M TIBOR: After NIRP"
  },
  {
    "figure_id": "F459",
    "report_id": "R015",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Lending interest rates at regional banks Figure 15: 3M TIBOR: Since 2000 Figure 16: 3M TIBOR: After NIRP Figure 17: Number of corporate bankruptcies (as of May 2026)"
  },
  {
    "figure_id": "F460",
    "report_id": "R015",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15: 3M TIBOR: Since 2000 Figure 16: 3M TIBOR: After NIRP Figure 17: Number of corporate bankruptcies (as of May 2026) Note: Universe of companies with liabilities of at least ¥10mn that undergo legal proceedings."
  },
  {
    "figure_id": "F461",
    "report_id": "R015",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: 3M TIBOR: After NIRP Figure 17: Number of corporate bankruptcies (as of May 2026) Note: Universe of companies with liabilities of at least ¥10mn that undergo legal proceedings."
  },
  {
    "figure_id": "F462",
    "report_id": "R015",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Number of corporate bankruptcies (as of May 2026) Note: Universe of companies with liabilities of at least ¥10mn that undergo legal proceedings. Figure 20: Holdings of foreign bonds (most recent for May 2026)"
  },
  {
    "figure_id": "F463",
    "report_id": "R015",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Holdings of foreign bonds (most recent for May 2026) Figure 21: Trading in foreign bonds (most recent for May 2026)"
  },
  {
    "figure_id": "F464",
    "report_id": "R015",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Holdings of foreign bonds (most recent for May 2026) Figure 21: Trading in foreign bonds (most recent for May 2026) Figure 22: Balance, duration, and simple estimates of appraisal gains/losses for foreign bonds"
  },
  {
    "figure_id": "F465",
    "report_id": "R015",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Holdings of foreign bonds (most recent for May 2026) Figure 21: Trading in foreign bonds (most recent for May 2026) Figure 22: Balance, duration, and simple estimates of appraisal gains/losses for foreign bonds Notes"
  },
  {
    "figure_id": "F466",
    "report_id": "R015",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 25: Valuations relative to Europe, US (FY2026 BBG consensus) Figure 26: Performance relative to Europe, US Figure 27: Change in Japanese yield curve Figure 28: Effective Federal Funds rate and midpoint for FF rate outloo"
  },
  {
    "figure_id": "F467",
    "report_id": "R015",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 29: US corporate loan credit spreads (all industries, long-term history)"
  },
  {
    "figure_id": "F468",
    "report_id": "R015",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 30: US corporate loan credit spreads (all industries, short-term history)"
  },
  {
    "figure_id": "F469",
    "report_id": "R015",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 31: USD short-long interest-rate spread (average during period)"
  },
  {
    "figure_id": "F470",
    "report_id": "R015",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: US corporate loan credit spreads (all industries, long-term history) Figure 30: US corporate loan credit spreads (all industries, short-term history) Figure 31: USD short-long interest-rate spread (average during per"
  },
  {
    "figure_id": "F471",
    "report_id": "R015",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: USD funding cost (via yen investment) (average during period) Figure 33: Basis cost Figure 34: Factor analysis of short-term dollar funding cost Figure 35: Origination volume of residential mortgages and other KPIs"
  },
  {
    "figure_id": "F472",
    "report_id": "R015",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 36: Housing starts (YoY)"
  },
  {
    "figure_id": "F473",
    "report_id": "R015",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "Figure 36: Housing starts (YoY) Note: Figures for owner-occupied & detached houses for sale. The most recent data for housing starts is YoY comparison of Apr-May."
  },
  {
    "figure_id": "F474",
    "report_id": "R015",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 37: Number of accounts at internet banks Figure 38: Monthly deposit balance at Rakuten Bank"
  },
  {
    "figure_id": "F475",
    "report_id": "R015",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "Figure 39: Margin trading related income at SBI Securities and market-wide outstanding margin transactions"
  },
  {
    "figure_id": "F476",
    "report_id": "R015",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: Number of accounts at internet banks Figure 38: Monthly deposit balance at Rakuten Bank Figure 39: Margin trading related income at SBI Securities and market-wide outstanding margin transactions Figure 40: FX reven"
  },
  {
    "figure_id": "F477",
    "report_id": "R015",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: Monthly deposit balance at Rakuten Bank Figure 39: Margin trading related income at SBI Securities and market-wide outstanding margin transactions Figure 40: FX revenue at SBI Securities and OTC retail margin FX trad"
  },
  {
    "figure_id": "F478",
    "report_id": "R015",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "Figure 39: Margin trading related income at SBI Securities and market-wide outstanding margin transactions Figure 40: FX revenue at SBI Securities and OTC retail margin FX trading volume (as of May 2026) Note: The most recent d"
  },
  {
    "figure_id": "F479",
    "report_id": "R016",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: J&T historical P/E valuation band (Non-IFRS) Figure 2: J&T historical P/E valuation band (IFRS)"
  },
  {
    "figure_id": "F480",
    "report_id": "R016",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: J&T historical P/E valuation band (Non-IFRS) Figure 2: J&T historical P/E valuation band (IFRS)"
  },
  {
    "figure_id": "F481",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: J&T share price performance vs Hang Seng Index Figure 4: China Parcel Service / Logistics Stock Performance – 2026 Year-to-date ## Positive Drivers"
  },
  {
    "figure_id": "F482",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: J&T share price performance vs Hang Seng Index Figure 4: China Parcel Service / Logistics Stock Performance – 2026 Year-to-date ## Positive Drivers Positive driver #1: J&T's systematic cost leadership, rooted in Chin"
  },
  {
    "figure_id": "F483",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: J&T Cost per parcel by region (US\\$/parcel) Figure 6: J&T SEA cost breakdown (US\\$/parcel) Figure 7: J&T China cost breakdown (US\\$/parcel)"
  },
  {
    "figure_id": "F484",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: J&T Cost per parcel by region (US\\$/parcel) Figure 6: J&T SEA cost breakdown (US\\$/parcel) Figure 7: J&T China cost breakdown (US\\$/parcel) Figure 8: J&T New Market cost breakdown (US\\$/parcel)"
  },
  {
    "figure_id": "F485",
    "report_id": "R016",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: J&T SEA cost breakdown (US\\$/parcel) Figure 7: J&T China cost breakdown (US\\$/parcel) Figure 8: J&T New Market cost breakdown (US\\$/parcel) In Southeast Asia, J&T has rapidly increased automated sorting machines fr"
  },
  {
    "figure_id": "F486",
    "report_id": "R016",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: J&T China cost breakdown (US\\$/parcel) Figure 8: J&T New Market cost breakdown (US\\$/parcel) In Southeast Asia, J&T has rapidly increased automated sorting machines from 52 to 73 in one year (as of end-1Q26), providi"
  },
  {
    "figure_id": "F487",
    "report_id": "R016",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: J&T Automated Sorting Machines by Region Figure 10: SEA: Number of line-haul vehicles (as of 1Q26) Figure 11: China: Number of line-haul vehicles (as of 1Q26)"
  },
  {
    "figure_id": "F488",
    "report_id": "R016",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: J&T Automated Sorting Machines by Region Figure 10: SEA: Number of line-haul vehicles (as of 1Q26) Figure 11: China: Number of line-haul vehicles (as of 1Q26) Figure 12: New Markets: Number of line-haul vehicles (a"
  },
  {
    "figure_id": "F489",
    "report_id": "R016",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: SEA: Number of line-haul vehicles (as of 1Q26) Figure 11: China: Number of line-haul vehicles (as of 1Q26) Figure 12: New Markets: Number of line-haul vehicles (as of 1Q26) Figure 13: Total: Number of line-haul veh"
  },
  {
    "figure_id": "F490",
    "report_id": "R016",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: China: Number of line-haul vehicles (as of 1Q26) Figure 12: New Markets: Number of line-haul vehicles (as of 1Q26) Figure 13: Total: Number of line-haul vehicles (as of 1Q26) Positive driver #2: J&T's regional spon"
  },
  {
    "figure_id": "F491",
    "report_id": "R016",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: New Markets: Number of line-haul vehicles (as of 1Q26) Figure 13: Total: Number of line-haul vehicles (as of 1Q26) Positive driver #2: J&T's regional sponsor model is a scalable, capital-efficient engine for rapid ma"
  },
  {
    "figure_id": "F492",
    "report_id": "R016",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Capex as % of revenue comparison among Tongda players Figure 15: J&T Market Share Gain by Region Positive driver #3: J&T's SEA leadership is underpinned by scale, platform-neutrality, and the ability to capture both"
  },
  {
    "figure_id": "F493",
    "report_id": "R016",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Capex as % of revenue comparison among Tongda players Figure 15: J&T Market Share Gain by Region Positive driver #3: J&T's SEA leadership is underpinned by scale, platform-neutrality, and the ability to capture both"
  },
  {
    "figure_id": "F494",
    "report_id": "R016",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Urbanization Rate % (ASEAN vs China) Figure 17: Market size of SEA's e-commerce retail market by transaction value (US\\$B) Figure 18: SE Asia and China Internet Users (% of Population)"
  },
  {
    "figure_id": "F495",
    "report_id": "R016",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Urbanization Rate % (ASEAN vs China) Figure 17: Market size of SEA's e-commerce retail market by transaction value (US\\$B) Figure 18: SE Asia and China Internet Users (% of Population)"
  },
  {
    "figure_id": "F496",
    "report_id": "R016",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Market size of SEA's e-commerce retail market by transaction value (US\\$B) Figure 18: SE Asia and China Internet Users (% of Population)"
  },
  {
    "figure_id": "F497",
    "report_id": "R016",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Express delivery market comparison: SEA vs China (Bn of parcels) Figure 20: Competitive landscape of SEA Express delivery market in FY25"
  },
  {
    "figure_id": "F498",
    "report_id": "R016",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Express delivery market comparison: SEA vs China (Bn of parcels) Figure 20: Competitive landscape of SEA Express delivery market in FY25 Figure 21: Competitive landscape of SEA Express delivery market in 2022"
  },
  {
    "figure_id": "F499",
    "report_id": "R016",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Competitive landscape of SEA Express delivery market in FY25 Figure 21: Competitive landscape of SEA Express delivery market in 2022 Figure 22: SEA remains the highest contributing region for J&T (adj. EBITDA)"
  },
  {
    "figure_id": "F500",
    "report_id": "R016",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Competitive landscape of SEA Express delivery market in FY25 Figure 21: Competitive landscape of SEA Express delivery market in 2022 Figure 22: SEA remains the highest contributing region for J&T (adj. EBITDA)"
  },
  {
    "figure_id": "F501",
    "report_id": "R016",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: Competitive landscape of SEA Express delivery market in 2022 Figure 22: SEA remains the highest contributing region for J&T (adj. EBITDA) J&T's New Markets—Brazil, Mexico, Saudi Arabia, UAE, and Egypt—are rapidly evo"
  },
  {
    "figure_id": "F502",
    "report_id": "R016",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23: New Market Transaction Volume of e-commerce retail market Figure 24: New Markets Parcel volume of express delivery industry (MM parcels) Figure 25: GDP Per Capita (USD): New Markets vs SEA"
  },
  {
    "figure_id": "F503",
    "report_id": "R016",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23: New Market Transaction Volume of e-commerce retail market Figure 24: New Markets Parcel volume of express delivery industry (MM parcels) Figure 25: GDP Per Capita (USD): New Markets vs SEA Figure 26: Mercado Libre"
  },
  {
    "figure_id": "F504",
    "report_id": "R016",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Figure 24: New Markets Parcel volume of express delivery industry (MM parcels) Figure 25: GDP Per Capita (USD): New Markets vs SEA Figure 26: Mercado Libre - Total Unique active Buyers on the rise Figure 27: Mercado Libre - A"
  },
  {
    "figure_id": "F505",
    "report_id": "R016",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 28: J&T New Markets unit economics"
  },
  {
    "figure_id": "F506",
    "report_id": "R016",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Mercado Libre - Total Unique active Buyers on the rise Figure 27: Mercado Libre - Argentina, Brazil and Mexico among top regions exhibiting GMV growth (FX- Neutral Y/Y Growth) Figure 28: J&T New Markets unit economic"
  },
  {
    "figure_id": "F507",
    "report_id": "R016",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 27: Mercado Libre - Argentina, Brazil and Mexico among top regions exhibiting GMV growth (FX- Neutral Y/Y Growth) Figure 28: J&T New Markets unit economics China remains the global benchmark for e-commerce and express de"
  },
  {
    "figure_id": "F508",
    "report_id": "R016",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: China express monthly industry revenue Figure 30: China express monthly industry volume (daily) Figure 31: China express monthly industry ASP"
  },
  {
    "figure_id": "F509",
    "report_id": "R016",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: China express monthly industry revenue Figure 30: China express monthly industry volume (daily) Figure 31: China express monthly industry ASP Figure 32: Monthly ASP changes of Tongda players"
  },
  {
    "figure_id": "F510",
    "report_id": "R016",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Figure 30: China express monthly industry volume (daily) Figure 31: China express monthly industry ASP Figure 32: Monthly ASP changes of Tongda players Figure 33: Chinese express delivery players market share by parcel volume"
  },
  {
    "figure_id": "F511",
    "report_id": "R016",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "Figure 31: China express monthly industry ASP Figure 32: Monthly ASP changes of Tongda players Figure 33: Chinese express delivery players market share by parcel volume (%) Figure 34: J&T China: parcel volume and Y/Y growth t"
  },
  {
    "figure_id": "F512",
    "report_id": "R016",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Monthly ASP changes of Tongda players Figure 33: Chinese express delivery players market share by parcel volume (%) Figure 34: J&T China: parcel volume and Y/Y growth trend ## Positive driver #6: The strategic part"
  },
  {
    "figure_id": "F513",
    "report_id": "R016",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 33: Chinese express delivery players market share by parcel volume (%) Figure 34: J&T China: parcel volume and Y/Y growth trend ## Positive driver #6: The strategic partnership with SF unlocks powerful synergies, acceler"
  },
  {
    "figure_id": "F514",
    "report_id": "R016",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: J&T Express FY25 Revenue Contribution by Region ## Risk driver #2: Margin pressure and yield erosion in Southeast Asia as the market matures and service differentiation narrows J&T's scale leadership in SEA paradoxical"
  },
  {
    "figure_id": "F515",
    "report_id": "R016",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "Figure 36: Shopee E-commerce GMV and Gross Orders ## Company Background ## Company Background and Evolution Founded in Indonesia in 2015 by Mr. Jet Li (a former executive at OPPO Electronics), J&T Global Express has rapidly evolv"
  },
  {
    "figure_id": "F516",
    "report_id": "R016",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: J&T's Regional Sponsor Model. ## Business segments J&T's business is organized into three primary segments: Southeast Asia: This is J&T's largest and most established region, covering Indonesia, Vietnam, Malaysia, the"
  },
  {
    "figure_id": "F517",
    "report_id": "R016",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: J&T Express Delivery Process Illustration Figure 39: J&T Cross-Border Service Process ## Management Profile and Shareholding Structure"
  },
  {
    "figure_id": "F518",
    "report_id": "R016",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: J&T Express Delivery Process Illustration Figure 39: J&T Cross-Border Service Process ## Management Profile and Shareholding Structure"
  },
  {
    "figure_id": "F519",
    "report_id": "R016",
    "label": "Figure 40",
    "figure_type": "source_exhibit",
    "context": "Figure 40: J&T Express Shareholding Structure # Financial analysis and forecasts ## Income Statement"
  },
  {
    "figure_id": "F520",
    "report_id": "R016",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 42: China: Industry parcel volume growth vs GDP growth"
  },
  {
    "figure_id": "F521",
    "report_id": "R016",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 42: China: Industry parcel volume growth vs GDP growth In New Markets, we forecast a revenue CAGR of 75% in 2025-28E, as J&T is still in the early stage of market penetration and management indicates the company is showing"
  },
  {
    "figure_id": "F522",
    "report_id": "R016",
    "label": "Figure 43",
    "figure_type": "source_exhibit",
    "context": "Figure 43: J&T cumulative share buyback since Oct'2024 (no. of shares) # Investment Thesis, Valuation and Risks J&T Express - H (Overweight; Price Target: HK\\$13.00) ## Investment Thesis"
  },
  {
    "figure_id": "F523",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: HMC: 12m forward P/E bands Figure 2: HMC: 12m forward P/B bands ## Investment Thesis, Valuation and Risks"
  },
  {
    "figure_id": "F524",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: HMC: 12m forward P/E bands Figure 2: HMC: 12m forward P/B bands ## Investment Thesis, Valuation and Risks Hyundai Motor Company (Overweight; Price Target: W640,000) ## Investment Thesis"
  },
  {
    "figure_id": "F525",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Kia: 12m forward P/E bands Figure 4: Kia: 12m forward P/B bands # Investment Thesis, Valuation and Risks"
  },
  {
    "figure_id": "F526",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Kia: 12m forward P/E bands Figure 4: Kia: 12m forward P/B bands # Investment Thesis, Valuation and Risks Kia Corp (Overweight; Price Target: W260,000) ## Investment Thesis"
  },
  {
    "figure_id": "F527",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Iceberg 10-city real time secondary daily sales 冰山指数实时二手每日成交 (十大城市)"
  },
  {
    "figure_id": "F528",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Iceberg tier-1 cities secondary listing volume 冰山指数二手挂牌量 (一线城市) No. of secondary listings ('000 units) - Tier 1 cities # 2. Mainland China – leading indicators from Centraline Figure 3: Centraline secondary asking pric"
  },
  {
    "figure_id": "F529",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Centraline secondary manager confidence index in tier-1 cities vs three-month rolling secondary sales # 3. Mainland China – Weekly primary sales registrations"
  },
  {
    "figure_id": "F530",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Centraline secondary manager confidence index in tier-1 cities vs three-month rolling secondary sales # 3. Mainland China – Weekly primary sales registrations Figure 5: 60-city weekly primary sales registrations (一手网签)"
  },
  {
    "figure_id": "F531",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 6: 60-city weekly primary sales registrations (一手网签) Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival."
  },
  {
    "figure_id": "F532",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: 60-city weekly primary sales registrations (一手网签) – compared with 2019-24 Figure 6: 60-city weekly primary sales registrations (一手网签) Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Fe"
  },
  {
    "figure_id": "F533",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: 12-city daily secondary sales registrations (二手网签) Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average Secondary sales 7-day moving average - 12-city Figure 9: Tier-1 cities - secondary listin"
  },
  {
    "figure_id": "F534",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: 12-city daily secondary sales registrations (二手网签) Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average Secondary sales 7-day moving average - 12-city Figure 9: Tier-1 cities - secondary listin"
  },
  {
    "figure_id": "F535",
    "report_id": "R020",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average Secondary sales 7-day moving average - 12-city Figure 9: Tier-1 cities - secondary listings and inventory months ## 5. Hong Kong – Residential market"
  },
  {
    "figure_id": "F536",
    "report_id": "R020",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Midland weekend appointment volume (in 15 housing estates) Figure 11: Centraline – No. of secondary listings (for sale) Figure 12: Hong Kong weekly secondary transactions in 35 major estates"
  },
  {
    "figure_id": "F537",
    "report_id": "R020",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Midland weekend appointment volume (in 15 housing estates) Figure 11: Centraline – No. of secondary listings (for sale) Figure 12: Hong Kong weekly secondary transactions in 35 major estates Figure 13: Hong Kong se"
  },
  {
    "figure_id": "F538",
    "report_id": "R020",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Centraline – No. of secondary listings (for sale) Figure 12: Hong Kong weekly secondary transactions in 35 major estates Figure 13: Hong Kong secondary home prices (Centa-city Leading Index, or CCL) Figure 14: Cent"
  },
  {
    "figure_id": "F539",
    "report_id": "R020",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Hong Kong weekly secondary transactions in 35 major estates Figure 13: Hong Kong secondary home prices (Centa-city Leading Index, or CCL) Figure 14: Centa Valuation Index (CVI) vs secondary home prices (CCL) 1m rolli"
  },
  {
    "figure_id": "F540",
    "report_id": "R020",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Hong Kong secondary home prices (Centa-city Leading Index, or CCL) Figure 14: Centa Valuation Index (CVI) vs secondary home prices (CCL) 1m rolling W/W"
  },
  {
    "figure_id": "F541",
    "report_id": "R020",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15: Centa-Salesman Index (CSI) vs. secondary home prices (CCL) Net arrivals over departures # 6. Hong Kong – Tourist arrivals and resident departures"
  },
  {
    "figure_id": "F542",
    "report_id": "R020",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Hong Kong seven-day rolling average total tourist arrivals minus resident departures ## 7. Share price update Figure 17: Mainland China Property – Weekly share price performance (%)"
  },
  {
    "figure_id": "F543",
    "report_id": "R020",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type"
  },
  {
    "figure_id": "F544",
    "report_id": "R020",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Short interest in Mainland China / Hong Kong Property – 30-day moving average"
  },
  {
    "figure_id": "F545",
    "report_id": "R020",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Hong Kong Property & Conglomerates – Weekly share price performance (%) Figure 19: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type Figure 20: Short interest in Mai"
  },
  {
    "figure_id": "F546",
    "report_id": "R020",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type Figure 20: Short interest in Mainland China / Hong Kong Property – 30-day moving average"
  },
  {
    "figure_id": "F547",
    "report_id": "R020",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: HK property average southbound holdings as a % of free float Southbound holding (%) ## 8. Credit recommendations"
  },
  {
    "figure_id": "F548",
    "report_id": "R020",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22: JACI China HY Property Index: Performance since 2026 (January 2026 = 100)"
  },
  {
    "figure_id": "F549",
    "report_id": "R021",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Global memory makers' share price performance, including SOX (Philadelphia Semiconductor Index) # Investment Thesis, Valuation and Risks Samsung Electronics (Overweight; Price Target: W480,000) ## Investment Thesis"
  },
  {
    "figure_id": "F550",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Share price performance Figure 4: 5-day share price performance Note: Share prices as of July 6. Figure 5: 1-month share price performance Note: Share prices as of July 6."
  },
  {
    "figure_id": "F551",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: 5-day share price performance Note: Share prices as of July 6. Figure 5: 1-month share price performance Note: Share prices as of July 6. Figure 6: 3-month share price performance Note: Share prices as of July 6."
  },
  {
    "figure_id": "F552",
    "report_id": "R023",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: 1-month share price performance Note: Share prices as of July 6. Figure 6: 3-month share price performance Note: Share prices as of July 6. Figure 7: 6-month share price performance Note: Share prices as of July 6."
  },
  {
    "figure_id": "F553",
    "report_id": "R023",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: 3-month share price performance Note: Share prices as of July 6. Figure 7: 6-month share price performance Note: Share prices as of July 6. Figure 8: Share price performance by theme Note: Share prices as of July 6"
  },
  {
    "figure_id": "F554",
    "report_id": "R023",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: 6-month share price performance Note: Share prices as of July 6. Figure 8: Share price performance by theme Note: Share prices as of July 6. Weighted average basis. Figure 9: Germany flat glass price trend Figure 1"
  },
  {
    "figure_id": "F555",
    "report_id": "R023",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Share price performance by theme Note: Share prices as of July 6. Weighted average basis. Figure 9: Germany flat glass price trend Figure 10: Dubai crude oil price trend Figure 11: Netherlands natural gas price tre"
  },
  {
    "figure_id": "F556",
    "report_id": "R023",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Germany flat glass price trend Figure 10: Dubai crude oil price trend Figure 11: Netherlands natural gas price trend Figure 12: Southeast Asia caustic soda price trend"
  },
  {
    "figure_id": "F557",
    "report_id": "R023",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Dubai crude oil price trend Figure 11: Netherlands natural gas price trend Figure 12: Southeast Asia caustic soda price trend Figure 13: Southeast Asia PVC market trend"
  },
  {
    "figure_id": "F558",
    "report_id": "R023",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Netherlands natural gas price trend Figure 12: Southeast Asia caustic soda price trend Figure 13: Southeast Asia PVC market trend Figure 14: Australia thermal coal price"
  },
  {
    "figure_id": "F559",
    "report_id": "R023",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Southeast Asia caustic soda price trend Figure 13: Southeast Asia PVC market trend Figure 14: Australia thermal coal price"
  },
  {
    "figure_id": "F560",
    "report_id": "R023",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Southeast Asia PVC market trend Figure 14: Australia thermal coal price ## Important Disclosures"
  },
  {
    "figure_id": "F561",
    "report_id": "R025",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Unimicron BT revenue and mix ## Technology Jerry Tsai AC JPM Securities (Taiwan) Limited"
  },
  {
    "figure_id": "F562",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: China PMDI export volume/ ASP"
  },
  {
    "figure_id": "F563",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: China PMDI export volume/ ASP Figure 2: China MDI - BZ spread (Rmb/t) Figure 3: US Ethane vs. Asia PE Spot"
  },
  {
    "figure_id": "F564",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: China PMDI export volume/ ASP Figure 2: China MDI - BZ spread (Rmb/t) Figure 3: US Ethane vs. Asia PE Spot Figure 4: Wanhua Qtrly Earnings"
  },
  {
    "figure_id": "F565",
    "report_id": "R028",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: China MDI - BZ spread (Rmb/t) Figure 3: US Ethane vs. Asia PE Spot Figure 4: Wanhua Qtrly Earnings"
  },
  {
    "figure_id": "F566",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Retail Imbalance in SPCX As of July 8 $^{th}$ Figure 2: Cumulative Retail Imbalance in SPCX As of July 8 $^{th}$ Figure 3: Momentum Crowding off its recent highs..."
  },
  {
    "figure_id": "F567",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Retail Imbalance in SPCX As of July 8 $^{th}$ Figure 2: Cumulative Retail Imbalance in SPCX As of July 8 $^{th}$ Figure 3: Momentum Crowding off its recent highs... As of Jul 7 $^{th}$ Figure 4: ... recently"
  },
  {
    "figure_id": "F568",
    "report_id": "R031",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Cumulative Retail Imbalance in SPCX As of July 8 $^{th}$ Figure 3: Momentum Crowding off its recent highs... As of Jul 7 $^{th}$ Figure 4: ... recently"
  },
  {
    "figure_id": "F569",
    "report_id": "R031",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Momentum Crowding off its recent highs... As of Jul 7 $^{th}$ Figure 4: ... recently Figure 5: Retail Investor Daily Purchases by Stocks and ETFs \\$M, as of Jul 8 $^{th}$"
  },
  {
    "figure_id": "F570",
    "report_id": "R031",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: ... recently Figure 5: Retail Investor Daily Purchases by Stocks and ETFs \\$M, as of Jul 8 $^{th}$ Figure 6: Retail Imbalance in SCO As of July 8 $^{th}$ Figure 7: Cumulative Retail Imbalance in SCO As of July $8^{"
  },
  {
    "figure_id": "F571",
    "report_id": "R031",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Retail Investor Daily Purchases by Stocks and ETFs \\$M, as of Jul 8 $^{th}$ Figure 6: Retail Imbalance in SCO As of July 8 $^{th}$ Figure 7: Cumulative Retail Imbalance in SCO As of July $8^{\\text{th}}$ ## Retail C"
  },
  {
    "figure_id": "F572",
    "report_id": "R031",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Retail Imbalance in SCO As of July 8 $^{th}$ Figure 7: Cumulative Retail Imbalance in SCO As of July $8^{\\text{th}}$ ## Retail Cash Activity – Overview Figure 8: Retail Single Stock Activity by Themes"
  },
  {
    "figure_id": "F573",
    "report_id": "R031",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Retail Single Stock Activity by Themes Figure 9: Retail Cumulative Purchases in Mag 7 + PLTR (\\$B) Figure 10: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Note: The last we"
  },
  {
    "figure_id": "F574",
    "report_id": "R031",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Retail Cumulative Purchases in Mag 7 + PLTR (\\$B) Figure 10: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Note: The last weekly data point includes a holiday, Jul 3. Figu"
  },
  {
    "figure_id": "F575",
    "report_id": "R031",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Note: The last weekly data point includes a holiday, Jul 3. Figure 11: Retail ETF Activity by Themes Buying / Selling of ETFs a"
  },
  {
    "figure_id": "F576",
    "report_id": "R031",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Retail Activity in CUPR Figure 15: Retail Activity in HIVE"
  },
  {
    "figure_id": "F577",
    "report_id": "R031",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Retail Activity in CUPR Figure 15: Retail Activity in HIVE Figure 16: Retail Activity in SERV"
  },
  {
    "figure_id": "F578",
    "report_id": "R031",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Retail Activity in CUPR Figure 15: Retail Activity in HIVE Figure 16: Retail Activity in SERV ## Macro & Fundamental Stories"
  },
  {
    "figure_id": "F579",
    "report_id": "R031",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15: Retail Activity in HIVE Figure 16: Retail Activity in SERV ## Macro & Fundamental Stories Figure 18: Cumulative Retail Imbalance in GEV"
  },
  {
    "figure_id": "F580",
    "report_id": "R031",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Retail Activity in SERV ## Macro & Fundamental Stories Figure 18: Cumulative Retail Imbalance in GEV As of July 7 $^{th}$ Figure 19: Retail Imbalance in CAT"
  },
  {
    "figure_id": "F581",
    "report_id": "R031",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Cumulative Retail Imbalance in GEV As of July 7 $^{th}$ Figure 19: Retail Imbalance in CAT As of July 7 $^{th}$ Figure 20: Cumulative Retail Imbalance in CAT"
  },
  {
    "figure_id": "F582",
    "report_id": "R031",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Cumulative Retail Imbalance in GEV As of July 7 $^{th}$ Figure 19: Retail Imbalance in CAT As of July 7 $^{th}$ Figure 20: Cumulative Retail Imbalance in CAT As of July 7 $^{th}$ Figure 21: Retail Imbalance in CMI"
  },
  {
    "figure_id": "F583",
    "report_id": "R031",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Retail Imbalance in CAT As of July 7 $^{th}$ Figure 20: Cumulative Retail Imbalance in CAT As of July 7 $^{th}$ Figure 21: Retail Imbalance in CMI Figure 22: Cumulative Retail Imbalance in CMI As of July 7 $^{th}$"
  },
  {
    "figure_id": "F584",
    "report_id": "R031",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Cumulative Retail Imbalance in CAT As of July 7 $^{th}$ Figure 21: Retail Imbalance in CMI Figure 22: Cumulative Retail Imbalance in CMI As of July 7 $^{th}$ Figure 23: Retail Imbalance in TER"
  },
  {
    "figure_id": "F585",
    "report_id": "R031",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: Retail Imbalance in CMI Figure 22: Cumulative Retail Imbalance in CMI As of July 7 $^{th}$ Figure 23: Retail Imbalance in TER As of July 7 $^{th}$ Figure 24: Cumulative Retail Imbalance in TER"
  },
  {
    "figure_id": "F586",
    "report_id": "R031",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22: Cumulative Retail Imbalance in CMI As of July 7 $^{th}$ Figure 23: Retail Imbalance in TER As of July 7 $^{th}$ Figure 24: Cumulative Retail Imbalance in TER As of July 7 $^{th}$ Figure 25: Retail Imbalance in KLAC"
  },
  {
    "figure_id": "F587",
    "report_id": "R031",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23: Retail Imbalance in TER As of July 7 $^{th}$ Figure 24: Cumulative Retail Imbalance in TER As of July 7 $^{th}$ Figure 25: Retail Imbalance in KLAC As of July 7 $^{th}$ Figure 26: Cumulative Retail Imbalance in KLA"
  },
  {
    "figure_id": "F588",
    "report_id": "R031",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Figure 24: Cumulative Retail Imbalance in TER As of July 7 $^{th}$ Figure 25: Retail Imbalance in KLAC As of July 7 $^{th}$ Figure 26: Cumulative Retail Imbalance in KLAC As of July 7 $^{th}$ Figure 27: Retail Imbalance in LR"
  },
  {
    "figure_id": "F589",
    "report_id": "R031",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 25: Retail Imbalance in KLAC As of July 7 $^{th}$ Figure 26: Cumulative Retail Imbalance in KLAC As of July 7 $^{th}$ Figure 27: Retail Imbalance in LRCX Figure 28: Cumulative Retail Imbalance in LRCX As of July 7 $^{t"
  },
  {
    "figure_id": "F590",
    "report_id": "R031",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Cumulative Retail Imbalance in KLAC As of July 7 $^{th}$ Figure 27: Retail Imbalance in LRCX Figure 28: Cumulative Retail Imbalance in LRCX As of July 7 $^{th}$ Figure 29: Retail Imbalance in INTC"
  },
  {
    "figure_id": "F591",
    "report_id": "R031",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 27: Retail Imbalance in LRCX Figure 28: Cumulative Retail Imbalance in LRCX As of July 7 $^{th}$ Figure 29: Retail Imbalance in INTC As of July 7 $^{th}$ Figure 30: Cumulative Retail Imbalance in INTC"
  },
  {
    "figure_id": "F592",
    "report_id": "R031",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Cumulative Retail Imbalance in LRCX As of July 7 $^{th}$ Figure 29: Retail Imbalance in INTC As of July 7 $^{th}$ Figure 30: Cumulative Retail Imbalance in INTC As of July 7 $^{th}$ Figure 31: Retail Imbalance in M"
  },
  {
    "figure_id": "F593",
    "report_id": "R031",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Retail Imbalance in INTC As of July 7 $^{th}$ Figure 30: Cumulative Retail Imbalance in INTC As of July 7 $^{th}$ Figure 31: Retail Imbalance in MRVL As of July 7 $^{th}$ Figure 32: Cumulative Retail Imbalance in M"
  },
  {
    "figure_id": "F594",
    "report_id": "R031",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Figure 30: Cumulative Retail Imbalance in INTC As of July 7 $^{th}$ Figure 31: Retail Imbalance in MRVL As of July 7 $^{th}$ Figure 32: Cumulative Retail Imbalance in MRVL As of July $7^{\\text{th}}$ Figure 33: Retail Imbalanc"
  },
  {
    "figure_id": "F595",
    "report_id": "R031",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "Figure 31: Retail Imbalance in MRVL As of July 7 $^{th}$ Figure 32: Cumulative Retail Imbalance in MRVL As of July $7^{\\text{th}}$ Figure 33: Retail Imbalance in AMAT Figure 34: Cumulative Retail Imbalance in AMAT As of July"
  },
  {
    "figure_id": "F596",
    "report_id": "R031",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Cumulative Retail Imbalance in MRVL As of July $7^{\\text{th}}$ Figure 33: Retail Imbalance in AMAT Figure 34: Cumulative Retail Imbalance in AMAT As of July 7 $^{th}$ Figure 35: Retail Imbalance in SWKS"
  },
  {
    "figure_id": "F597",
    "report_id": "R031",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 33: Retail Imbalance in AMAT Figure 34: Cumulative Retail Imbalance in AMAT As of July 7 $^{th}$ Figure 35: Retail Imbalance in SWKS As of July 7 $^{th}$ Figure 36: Cumulative Retail Imbalance in SWKS"
  },
  {
    "figure_id": "F598",
    "report_id": "R031",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "Figure 34: Cumulative Retail Imbalance in AMAT As of July 7 $^{th}$ Figure 35: Retail Imbalance in SWKS As of July 7 $^{th}$ Figure 36: Cumulative Retail Imbalance in SWKS As of July 7 $^{th}$ Figure 37: Retail Imbalance in A"
  },
  {
    "figure_id": "F599",
    "report_id": "R031",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Retail Imbalance in SWKS As of July 7 $^{th}$ Figure 36: Cumulative Retail Imbalance in SWKS As of July 7 $^{th}$ Figure 37: Retail Imbalance in AVGO As of July 7 $^{th}$ Figure 38: Cumulative Retail Imbalance in A"
  },
  {
    "figure_id": "F600",
    "report_id": "R031",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "Figure 36: Cumulative Retail Imbalance in SWKS As of July 7 $^{th}$ Figure 37: Retail Imbalance in AVGO As of July 7 $^{th}$ Figure 38: Cumulative Retail Imbalance in AVGO As of July 7 $^{th}$ Figure 39: Retail Imbalance in Q"
  },
  {
    "figure_id": "F601",
    "report_id": "R031",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: Retail Imbalance in AVGO As of July 7 $^{th}$ Figure 38: Cumulative Retail Imbalance in AVGO As of July 7 $^{th}$ Figure 39: Retail Imbalance in QCOM"
  },
  {
    "figure_id": "F602",
    "report_id": "R031",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: Cumulative Retail Imbalance in AVGO As of July 7 $^{th}$ Figure 39: Retail Imbalance in QCOM Figure 41: Retail Imbalance in AAPL As of July 7 $^{th}$"
  },
  {
    "figure_id": "F603",
    "report_id": "R031",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "Figure 39: Retail Imbalance in QCOM Figure 41: Retail Imbalance in AAPL As of July 7 $^{th}$ Figure 42: Cumulative Retail Imbalance in AAPL"
  },
  {
    "figure_id": "F604",
    "report_id": "R031",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 41: Retail Imbalance in AAPL As of July 7 $^{th}$ Figure 42: Cumulative Retail Imbalance in AAPL As of July 7 $^{th}$ Figure 43: Retail Imbalance in MU"
  },
  {
    "figure_id": "F605",
    "report_id": "R031",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 41: Retail Imbalance in AAPL As of July 7 $^{th}$ Figure 42: Cumulative Retail Imbalance in AAPL As of July 7 $^{th}$ Figure 43: Retail Imbalance in MU As of July 7 $^{th}$ Figure 44: Cumulative Retail Imbalance in MU"
  },
  {
    "figure_id": "F606",
    "report_id": "R031",
    "label": "Figure 42",
    "figure_type": "source_exhibit",
    "context": "Figure 42: Cumulative Retail Imbalance in AAPL As of July 7 $^{th}$ Figure 43: Retail Imbalance in MU As of July 7 $^{th}$ Figure 44: Cumulative Retail Imbalance in MU As of July $7^{\\text{th}}$ Figure 45: Retail Imbalance in"
  },
  {
    "figure_id": "F607",
    "report_id": "R031",
    "label": "Figure 43",
    "figure_type": "source_exhibit",
    "context": "Figure 43: Retail Imbalance in MU As of July 7 $^{th}$ Figure 44: Cumulative Retail Imbalance in MU As of July $7^{\\text{th}}$ Figure 45: Retail Imbalance in WDC Figure 46: Cumulative Retail Imbalance in WDC As of July 8 $^{t"
  },
  {
    "figure_id": "F608",
    "report_id": "R031",
    "label": "Figure 44",
    "figure_type": "source_exhibit",
    "context": "Figure 44: Cumulative Retail Imbalance in MU As of July $7^{\\text{th}}$ Figure 45: Retail Imbalance in WDC Figure 46: Cumulative Retail Imbalance in WDC As of July 8 $^{th}$ ## Retail Activity in Options"
  },
  {
    "figure_id": "F609",
    "report_id": "R031",
    "label": "Figure 45",
    "figure_type": "source_exhibit",
    "context": "Figure 45: Retail Imbalance in WDC Figure 46: Cumulative Retail Imbalance in WDC As of July 8 $^{th}$ ## Retail Activity in Options Figure 47: Top 40 Equities with Most Delta Bought (in \\$Mn)"
  },
  {
    "figure_id": "F610",
    "report_id": "R031",
    "label": "Figure 46",
    "figure_type": "source_exhibit",
    "context": "Figure 46: Cumulative Retail Imbalance in WDC As of July 8 $^{th}$ ## Retail Activity in Options Figure 47: Top 40 Equities with Most Delta Bought (in \\$Mn) Figure 48: Top 40 Equities with Most Delta Sold (in \\$Mn) Figure 49:"
  },
  {
    "figure_id": "F611",
    "report_id": "R031",
    "label": "Figure 47",
    "figure_type": "source_exhibit",
    "context": "Figure 47: Top 40 Equities with Most Delta Bought (in \\$Mn) Figure 48: Top 40 Equities with Most Delta Sold (in \\$Mn) Figure 49: Top 40 Equities with Most Gamma Bought (in \\$Mn) Figure 50: Top 40 Equities with Most Gamma Sold"
  },
  {
    "figure_id": "F612",
    "report_id": "R031",
    "label": "Figure 48",
    "figure_type": "source_exhibit",
    "context": "Figure 48: Top 40 Equities with Most Delta Sold (in \\$Mn) Figure 49: Top 40 Equities with Most Gamma Bought (in \\$Mn) Figure 50: Top 40 Equities with Most Gamma Sold (in \\$Mn) # Retail Investors Options Activity by Sectors"
  },
  {
    "figure_id": "F613",
    "report_id": "R031",
    "label": "Figure 49",
    "figure_type": "source_exhibit",
    "context": "Figure 49: Top 40 Equities with Most Gamma Bought (in \\$Mn) Figure 50: Top 40 Equities with Most Gamma Sold (in \\$Mn) # Retail Investors Options Activity by Sectors Figure 51: Retail Options Trading Share"
  },
  {
    "figure_id": "F614",
    "report_id": "R031",
    "label": "Figure 50",
    "figure_type": "source_exhibit",
    "context": "Figure 50: Top 40 Equities with Most Gamma Sold (in \\$Mn) # Retail Investors Options Activity by Sectors Figure 51: Retail Options Trading Share Figure 52: Retail Options Volume (Calls and Puts) Figure 53: Retail Options Volu"
  },
  {
    "figure_id": "F615",
    "report_id": "R031",
    "label": "Figure 51",
    "figure_type": "source_exhibit",
    "context": "Figure 51: Retail Options Trading Share Figure 52: Retail Options Volume (Calls and Puts) Figure 53: Retail Options Volume (Calls and Puts), Information Technology Figure 54: Retail Options Volume (Calls and Puts), Communicat"
  },
  {
    "figure_id": "F616",
    "report_id": "R031",
    "label": "Figure 52",
    "figure_type": "source_exhibit",
    "context": "Figure 52: Retail Options Volume (Calls and Puts) Figure 53: Retail Options Volume (Calls and Puts), Information Technology Figure 54: Retail Options Volume (Calls and Puts), Communication Services Figure 55: Retail Options V"
  },
  {
    "figure_id": "F617",
    "report_id": "R031",
    "label": "Figure 53",
    "figure_type": "source_exhibit",
    "context": "Figure 53: Retail Options Volume (Calls and Puts), Information Technology Figure 54: Retail Options Volume (Calls and Puts), Communication Services Figure 55: Retail Options Volume (Calls and Puts), Health Care Figure 56: Ret"
  },
  {
    "figure_id": "F618",
    "report_id": "R031",
    "label": "Figure 54",
    "figure_type": "source_exhibit",
    "context": "Figure 54: Retail Options Volume (Calls and Puts), Communication Services Figure 55: Retail Options Volume (Calls and Puts), Health Care Figure 56: Retail Options Volume (Calls and Puts), Financials Figure 57: Retail Options"
  },
  {
    "figure_id": "F619",
    "report_id": "R031",
    "label": "Figure 55",
    "figure_type": "source_exhibit",
    "context": "Figure 55: Retail Options Volume (Calls and Puts), Health Care Figure 56: Retail Options Volume (Calls and Puts), Financials Figure 57: Retail Options Volume (Calls and Puts), Discretionary Figure 58: Retail Options Volume (C"
  },
  {
    "figure_id": "F620",
    "report_id": "R031",
    "label": "Figure 56",
    "figure_type": "source_exhibit",
    "context": "Figure 56: Retail Options Volume (Calls and Puts), Financials Figure 57: Retail Options Volume (Calls and Puts), Discretionary Figure 58: Retail Options Volume (Calls and Puts), Staples Figure 59: Retail Options Volume (Calls"
  },
  {
    "figure_id": "F621",
    "report_id": "R031",
    "label": "Figure 57",
    "figure_type": "source_exhibit",
    "context": "Figure 57: Retail Options Volume (Calls and Puts), Discretionary Figure 58: Retail Options Volume (Calls and Puts), Staples Figure 59: Retail Options Volume (Calls and Puts), Energy Figure 60: Retail Options Volume (Calls and"
  },
  {
    "figure_id": "F622",
    "report_id": "R031",
    "label": "Figure 58",
    "figure_type": "source_exhibit",
    "context": "Figure 58: Retail Options Volume (Calls and Puts), Staples Figure 59: Retail Options Volume (Calls and Puts), Energy Figure 60: Retail Options Volume (Calls and Puts), Materials # Appendix: Alternative Data Points on Retail A"
  },
  {
    "figure_id": "F623",
    "report_id": "R031",
    "label": "Figure 59",
    "figure_type": "source_exhibit",
    "context": "Figure 59: Retail Options Volume (Calls and Puts), Energy Figure 60: Retail Options Volume (Calls and Puts), Materials # Appendix: Alternative Data Points on Retail Activity Figure 61: Retail Brokerage Volume Hit Record \\~37% i"
  },
  {
    "figure_id": "F624",
    "report_id": "R031",
    "label": "Figure 61",
    "figure_type": "source_exhibit",
    "context": "Figure 61: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F625",
    "report_id": "R031",
    "label": "Figure 61",
    "figure_type": "source_exhibit",
    "context": "Figure 61: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F626",
    "report_id": "R032",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: CoWoS allocation breakdown by CoW vendor Exhibit 4: Global CoWoS demand breakdown: 2026e vs. 2027e Global CoWoS capacity demand by key customer Exhibit 5: Global CoWoS demand Y/Y growth profile"
  },
  {
    "figure_id": "F627",
    "report_id": "R032",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Global CoWoS demand Y/Y growth profile Exhibit 6: Global CoWoS capacity expansion by year end and by vendor Exhibit 7: Global CoWoS consumption, by customer NVIDIA Broadcom AMD Xilinx AWS/Annapurna AWS/Alchip Marvell"
  },
  {
    "figure_id": "F628",
    "report_id": "R032",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: Global CoWoS capacity expansion by year end and by vendor Exhibit 7: Global CoWoS consumption, by customer NVIDIA Broadcom AMD Xilinx AWS/Annapurna AWS/Alchip Marvell GUC MediaTek Intel Habana Others ## Exhibit 8: AI"
  },
  {
    "figure_id": "F629",
    "report_id": "R032",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: (old) Blackwell chip vs. GB NVL72 rack shipment Exhibit 11: (new) Blackwell chip vs. GB NVL72 and HGX equivalent rack shipment Exhibit 12: Rubin chip shipments vs. VR NVL72 rack shipments"
  },
  {
    "figure_id": "F630",
    "report_id": "R032",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: (old) Blackwell chip vs. GB NVL72 rack shipment Exhibit 11: (new) Blackwell chip vs. GB NVL72 and HGX equivalent rack shipment Exhibit 12: Rubin chip shipments vs. VR NVL72 rack shipments # AI semis – stock implica"
  },
  {
    "figure_id": "F631",
    "report_id": "R032",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: (new) Blackwell chip vs. GB NVL72 and HGX equivalent rack shipment Exhibit 12: Rubin chip shipments vs. VR NVL72 rack shipments # AI semis – stock implications, P/E multiples, revenue exposure Exhibit 13: P/E multipl"
  },
  {
    "figure_id": "F632",
    "report_id": "R032",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 15: TSMC's AI-related revenue 2024-29e CAGR could reach 60%"
  },
  {
    "figure_id": "F633",
    "report_id": "R032",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Exhibit 13: P/E multiple trend of AI semis Exhibit 14: We still expect AI chip revenue to rise QoQ Data center/HPC semi revenue: NVIDIA + AMD Exhibit 15: TSMC's AI-related revenue 2024-29e CAGR could reach 60% ■ General-purpos"
  },
  {
    "figure_id": "F634",
    "report_id": "R032",
    "label": "Exhibit 14",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: AI GPU H100 per GPU per hour as of end-March"
  },
  {
    "figure_id": "F635",
    "report_id": "R032",
    "label": "Exhibit 15",
    "figure_type": "source_exhibit",
    "context": "Exhibit 17: AI ASIC equivalent computing power – 16x Inferentia 2 per hour Exhibit 18: NVIDIA 5090 graphic cards pricing has rebounded recently, mainly in response to market expectations for price hikes and strong AI inference dem"
  },
  {
    "figure_id": "F636",
    "report_id": "R032",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: AI GPU H100 per GPU per hour as of end-March Exhibit 17: AI ASIC equivalent computing power – 16x Inferentia 2 per hour Exhibit 18: NVIDIA 5090 graphic cards pricing has rebounded recently, mainly in response to mark"
  },
  {
    "figure_id": "F637",
    "report_id": "R032",
    "label": "Exhibit 17",
    "figure_type": "source_exhibit",
    "context": "Exhibit 17: AI ASIC equivalent computing power – 16x Inferentia 2 per hour Exhibit 18: NVIDIA 5090 graphic cards pricing has rebounded recently, mainly in response to market expectations for price hikes and strong AI inference dem"
  },
  {
    "figure_id": "F638",
    "report_id": "R033",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: Forecast ROE and P/B of 7 major electronic component companies Note: e=MS ## Apr-Jun results preview Ibiden (4062.T): We forecast F3/27 1Q OP of ¥21.6bn (FactSet consensus: ¥20.2bn). We anticipate +¥4.1bn QoQ growth, m"
  },
  {
    "figure_id": "F639",
    "report_id": "R033",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: Global MLCC market forecasts Note: e=MS estimates Exhibit 5: MLCC market share Exhibit 6: MLCC market share (CY25) ## Murata leads the way in small, high-capacitance MLCCs for AI servers"
  },
  {
    "figure_id": "F640",
    "report_id": "R033",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: MLCC market share Exhibit 6: MLCC market share (CY25) ## Murata leads the way in small, high-capacitance MLCCs for AI servers Exhibit 7: MLCC maximum capacitance by size"
  },
  {
    "figure_id": "F641",
    "report_id": "R033",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Exhibit 9: Total OP since the Global Financial Crisis Exhibit 10: Sales and OP for electronic components companies"
  },
  {
    "figure_id": "F642",
    "report_id": "R033",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Exhibit 13: Total sales by major applications for our coverage ■ Smartphone ■ Computers ■ AV/Office ■ Automotive ■ Industrial ■ Others Note: Apps classification is based on our assumption Exhibit 14: Total sales YoY by major appli"
  },
  {
    "figure_id": "F643",
    "report_id": "R033",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Exhibit 15: Our OP forecasts vs. FactSet consensus"
  },
  {
    "figure_id": "F644",
    "report_id": "R033",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: OP forecast comparison Exhibit 17: 1-year forward consensus OP and share price ## Niterra (5334, OW, PT ¥12,600) For Niterra, we forecast F3/27 OP of ¥158.2bn (company guidance: ¥150bn; FactSet consensus: ¥154.0bn)."
  },
  {
    "figure_id": "F645",
    "report_id": "R033",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: OP forecast comparison Exhibit 17: 1-year forward consensus OP and share price ## Niterra (5334, OW, PT ¥12,600) For Niterra, we forecast F3/27 OP of ¥158.2bn (company guidance: ¥150bn; FactSet consensus: ¥154.0bn)."
  },
  {
    "figure_id": "F646",
    "report_id": "R033",
    "label": "Exhibit 18",
    "figure_type": "source_exhibit",
    "context": "Exhibit 18: OP forecast comparison Exhibit 19: 1-year Forward consensus OP and share price ## Minebea Mitsumi (6479, EW, PT ¥5,300) We forecast F3/27 OP of ¥121.5bn for Minebea Mitsumi (company guidance: ¥120bn; FactSet consensu"
  },
  {
    "figure_id": "F647",
    "report_id": "R033",
    "label": "Exhibit 18",
    "figure_type": "source_exhibit",
    "context": "Exhibit 18: OP forecast comparison Exhibit 19: 1-year Forward consensus OP and share price ## Minebea Mitsumi (6479, EW, PT ¥5,300) We forecast F3/27 OP of ¥121.5bn for Minebea Mitsumi (company guidance: ¥120bn; FactSet consensu"
  },
  {
    "figure_id": "F648",
    "report_id": "R033",
    "label": "Exhibit 20",
    "figure_type": "source_exhibit",
    "context": "Exhibit 20: OP forecast comparison Exhibit 21: 1-year forward consensus OP and share price ## Mabuchi Motor (6592, EW, PT ¥1,750)"
  },
  {
    "figure_id": "F649",
    "report_id": "R033",
    "label": "Exhibit 20",
    "figure_type": "source_exhibit",
    "context": "Exhibit 20: OP forecast comparison Exhibit 21: 1-year forward consensus OP and share price ## Mabuchi Motor (6592, EW, PT ¥1,750) For Mabuchi Motor, we forecast F12/26 OP of ¥27.2bn (company guidance: ¥26bn; FactSet consensus: ¥"
  },
  {
    "figure_id": "F650",
    "report_id": "R033",
    "label": "Exhibit 22",
    "figure_type": "source_exhibit",
    "context": "Exhibit 22: OP forecast comparison Exhibit 23: 1-year forward consensus OP and share price ## TDK (6762, OW, PT ¥4,900) We forecast F3/27 OP +¥63.3bn YoY to ¥335.8bn (guidance: ¥295bn, FactSet consensus: ¥307.7bn). By segment, w"
  },
  {
    "figure_id": "F651",
    "report_id": "R033",
    "label": "Exhibit 22",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: OP forecast comparison"
  },
  {
    "figure_id": "F652",
    "report_id": "R033",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: OP forecast comparison Exhibit 25: 1-year forward consensus OP and share price We forecast F3/27 OP +¥7.1bn YoY to ¥49.1bn (guidance: ¥48.5bn, FactSet consensus: ¥43.4bn). By segment, we forecast OP +¥6.9bn to ¥37.1b"
  },
  {
    "figure_id": "F653",
    "report_id": "R033",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 26: OP forecast comparison"
  },
  {
    "figure_id": "F654",
    "report_id": "R033",
    "label": "Exhibit 25",
    "figure_type": "source_exhibit",
    "context": "Exhibit 26: OP forecast comparison Exhibit 27: 1-year forward consensus OP and share price ## Nihon Dempa Kogyo (6779, EW, PT ¥4,900)"
  },
  {
    "figure_id": "F655",
    "report_id": "R033",
    "label": "Exhibit 26",
    "figure_type": "source_exhibit",
    "context": "Exhibit 26: OP forecast comparison Exhibit 27: 1-year forward consensus OP and share price ## Nihon Dempa Kogyo (6779, EW, PT ¥4,900) We forecast F3/27 OP +¥1.2bn YoY to ¥4.6bn (guidance: ¥4bn), assuming sales growth momentum pi"
  },
  {
    "figure_id": "F656",
    "report_id": "R033",
    "label": "Exhibit 28",
    "figure_type": "source_exhibit",
    "context": "Exhibit 28: OP forecast comparison Exhibit 29: 1-year forward consensus OP and share price ## Meiko (6787, EW, PT ¥39,200) We forecast F3/27 OP +¥14bn YoY to ¥38.6bn (guidance: ¥38bn, FactSet consensus: ¥38.1bn). We assume upsid"
  },
  {
    "figure_id": "F657",
    "report_id": "R033",
    "label": "Exhibit 28",
    "figure_type": "source_exhibit",
    "context": "Exhibit 28: OP forecast comparison Exhibit 29: 1-year forward consensus OP and share price ## Meiko (6787, EW, PT ¥39,200) We forecast F3/27 OP +¥14bn YoY to ¥38.6bn (guidance: ¥38bn, FactSet consensus: ¥38.1bn). We assume upsid"
  },
  {
    "figure_id": "F658",
    "report_id": "R033",
    "label": "Exhibit 30",
    "figure_type": "source_exhibit",
    "context": "Exhibit 30: OP forecast comparison Exhibit 31: 1-year forward consensus OP and share price ## Hirose Electric (6806, OW, PT ¥36,600)"
  },
  {
    "figure_id": "F659",
    "report_id": "R033",
    "label": "Exhibit 30",
    "figure_type": "source_exhibit",
    "context": "Exhibit 30: OP forecast comparison Exhibit 31: 1-year forward consensus OP and share price ## Hirose Electric (6806, OW, PT ¥36,600) Our F3/27 OP forecast is ¥47.3bn (+¥4.3bn YoY; company forecast ¥46.0bn, FS consensus ¥49.8bn)."
  },
  {
    "figure_id": "F660",
    "report_id": "R033",
    "label": "Exhibit 32",
    "figure_type": "source_exhibit",
    "context": "Exhibit 32: OP forecast comparison Exhibit 33: 1-year forward consensus OP and share price ## Japan Aviation Electronics Industry (6807, EW, PT ¥2,600)"
  },
  {
    "figure_id": "F661",
    "report_id": "R033",
    "label": "Exhibit 32",
    "figure_type": "source_exhibit",
    "context": "Exhibit 32: OP forecast comparison Exhibit 33: 1-year forward consensus OP and share price ## Japan Aviation Electronics Industry (6807, EW, PT ¥2,600) Our F3/27 OP forecast is ¥8.9bn (flat YoY; company forecast ¥9.5bn, FS conse"
  },
  {
    "figure_id": "F662",
    "report_id": "R033",
    "label": "Exhibit 34",
    "figure_type": "source_exhibit",
    "context": "Exhibit 34: OP forecast comparison Exhibit 35: 1-year forward consensus OP and share price ## CMK (6958, EW, PT ¥790)"
  },
  {
    "figure_id": "F663",
    "report_id": "R033",
    "label": "Exhibit 34",
    "figure_type": "source_exhibit",
    "context": "Exhibit 34: OP forecast comparison Exhibit 35: 1-year forward consensus OP and share price ## CMK (6958, EW, PT ¥790) Our F3/27 OP forecast is ¥3.2bn (+¥0.4bn YoY; company forecast ¥3.2bn, FS consensus ¥3.5bn). We forecast build"
  },
  {
    "figure_id": "F664",
    "report_id": "R033",
    "label": "Exhibit 36",
    "figure_type": "source_exhibit",
    "context": "Exhibit 36: OP forecast comparison Exhibit 37: 1-year forward consensus OP and share price ## Daishinku (6962, UW, PT ¥840) Our F3/27 OP forecast is ¥1.0bn (–¥0.1bn YoY; company forecast ¥1.4bn, FS consensus ¥1.4bn). We forecast"
  },
  {
    "figure_id": "F665",
    "report_id": "R033",
    "label": "Exhibit 36",
    "figure_type": "source_exhibit",
    "context": "Exhibit 36: OP forecast comparison Exhibit 37: 1-year forward consensus OP and share price ## Daishinku (6962, UW, PT ¥840) Our F3/27 OP forecast is ¥1.0bn (–¥0.1bn YoY; company forecast ¥1.4bn, FS consensus ¥1.4bn). We forecast"
  },
  {
    "figure_id": "F666",
    "report_id": "R033",
    "label": "Exhibit 38",
    "figure_type": "source_exhibit",
    "context": "Exhibit 38: OP forecast comparison Exhibit 39: 1-year forward consensus OP and share price ## Hamamatsu Photonics (6965, EW, PT ¥3,000)"
  },
  {
    "figure_id": "F667",
    "report_id": "R033",
    "label": "Exhibit 38",
    "figure_type": "source_exhibit",
    "context": "Exhibit 40: OP forecast comparison"
  },
  {
    "figure_id": "F668",
    "report_id": "R033",
    "label": "Exhibit 40",
    "figure_type": "source_exhibit",
    "context": "Exhibit 40: OP forecast comparison Exhibit 41: 1-year forward consensus OP and share price ## Kyocera (6971, EW, PT ¥4,000) We forecast F3/27 OP up ¥14.5bn YoY to ¥132.6bn (guidance ¥130.0bn, FactSet consensus ¥125.8bn). By segm"
  },
  {
    "figure_id": "F669",
    "report_id": "R033",
    "label": "Exhibit 40",
    "figure_type": "source_exhibit",
    "context": "Exhibit 40: OP forecast comparison Exhibit 41: 1-year forward consensus OP and share price ## Kyocera (6971, EW, PT ¥4,000) We forecast F3/27 OP up ¥14.5bn YoY to ¥132.6bn (guidance ¥130.0bn, FactSet consensus ¥125.8bn). By segm"
  },
  {
    "figure_id": "F670",
    "report_id": "R033",
    "label": "Exhibit 42",
    "figure_type": "source_exhibit",
    "context": "Exhibit 42: OP forecast comparison Exhibit 43: 1-year forward consensus OP and share price ## Taiyo Yuden (6976, UW, PT ¥12,500)"
  },
  {
    "figure_id": "F671",
    "report_id": "R033",
    "label": "Exhibit 42",
    "figure_type": "source_exhibit",
    "context": "Exhibit 42: OP forecast comparison Exhibit 43: 1-year forward consensus OP and share price ## Taiyo Yuden (6976, UW, PT ¥12,500) We forecast F3/27 OP up ¥25.2bn YoY to ¥45.2bn (guidance ¥30.0bn, FactSet consensus ¥40.2bn). In ML"
  },
  {
    "figure_id": "F672",
    "report_id": "R033",
    "label": "Exhibit 44",
    "figure_type": "source_exhibit",
    "context": "Exhibit 44: OP forecast comparison Exhibit 45: 1-year forward consensus OP and share price ## Murata Mfg (6981, OW, PT ¥12,500)"
  },
  {
    "figure_id": "F673",
    "report_id": "R033",
    "label": "Exhibit 44",
    "figure_type": "source_exhibit",
    "context": "Exhibit 44: OP forecast comparison Exhibit 45: 1-year forward consensus OP and share price ## Murata Mfg (6981, OW, PT ¥12,500) We expect OP to increase by ¥150bn YoY, to ¥431.9bn, in F3/27 (guidance: ¥380.0bn, FS consensus: ¥42"
  },
  {
    "figure_id": "F674",
    "report_id": "R033",
    "label": "Exhibit 46",
    "figure_type": "source_exhibit",
    "context": "Exhibit 46: OP forecast comparison Exhibit 47: 1-year forward consensus OP and share price ## Nichicon (6996, EW, PT ¥4,700) We forecast OP +¥2.9bn YoY to ¥9.4bn in F3/27 (guidance: ¥8.7bn, FS consensus: ¥9.8bn), with capacitor"
  },
  {
    "figure_id": "F675",
    "report_id": "R033",
    "label": "Exhibit 46",
    "figure_type": "source_exhibit",
    "context": "Exhibit 46: OP forecast comparison Exhibit 47: 1-year forward consensus OP and share price ## Nichicon (6996, EW, PT ¥4,700) We forecast OP +¥2.9bn YoY to ¥9.4bn in F3/27 (guidance: ¥8.7bn, FS consensus: ¥9.8bn), with capacitor"
  },
  {
    "figure_id": "F676",
    "report_id": "R033",
    "label": "Exhibit 48",
    "figure_type": "source_exhibit",
    "context": "Exhibit 48: OP forecast comparison Exhibit 49: 1-year forward consensus OP and share price ## Nippon Chemi-Con (6997, UW, PT ¥3,500) Our F3/27 OP forecast of ¥7.0bn (guidance: ¥8.0bn, FS: ¥7.4bn) looks to a YoY rise of ¥3.6bn. A"
  },
  {
    "figure_id": "F677",
    "report_id": "R033",
    "label": "Exhibit 48",
    "figure_type": "source_exhibit",
    "context": "Exhibit 48: OP forecast comparison Exhibit 49: 1-year forward consensus OP and share price ## Nippon Chemi-Con (6997, UW, PT ¥3,500) Our F3/27 OP forecast of ¥7.0bn (guidance: ¥8.0bn, FS: ¥7.4bn) looks to a YoY rise of ¥3.6bn. A"
  },
  {
    "figure_id": "F678",
    "report_id": "R033",
    "label": "Exhibit 50",
    "figure_type": "source_exhibit",
    "context": "Exhibit 50: OP forecast comparison Exhibit 51: 1-year forward consensus OP and share price ## KOA (6999, EW, PT ¥3,000) Our F3/27 OP forecast of ¥3.2bn looks to a YoY fall of ¥0.4bn (guidance: ¥2.8bn, FS consensus: ¥3.2bn). Our"
  },
  {
    "figure_id": "F679",
    "report_id": "R033",
    "label": "Exhibit 50",
    "figure_type": "source_exhibit",
    "context": "Exhibit 50: OP forecast comparison Exhibit 51: 1-year forward consensus OP and share price ## KOA (6999, EW, PT ¥3,000) Our F3/27 OP forecast of ¥3.2bn looks to a YoY fall of ¥0.4bn (guidance: ¥2.8bn, FS consensus: ¥3.2bn). Our"
  },
  {
    "figure_id": "F680",
    "report_id": "R033",
    "label": "Exhibit 52",
    "figure_type": "source_exhibit",
    "context": "Exhibit 52: OP forecast comparison Exhibit 53: 1-year Forward consensus OP and share price ## Ibiden: Key Financial Data Exhibit 54:"
  },
  {
    "figure_id": "F681",
    "report_id": "R033",
    "label": "Exhibit 52",
    "figure_type": "source_exhibit",
    "context": "Exhibit 52: OP forecast comparison Exhibit 53: 1-year Forward consensus OP and share price ## Ibiden: Key Financial Data Exhibit 54:"
  },
  {
    "figure_id": "F682",
    "report_id": "R035",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Orbital compute technology supply chain Exhibit 3: Orbital Compute Ecosystem ## What is orbital compute? A rack of compute in space. Orbital compute consists of placing meaningful compute payloads in space – AI acceler"
  },
  {
    "figure_id": "F683",
    "report_id": "R035",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: Orbital Compute Roadmap ## Who are the key players? While NASA is an independent agency of the US federal government responsible for the United States' civil space program and for research in aeronautics and space, sev"
  },
  {
    "figure_id": "F684",
    "report_id": "R035",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Global Public and Private Space Enablers"
  },
  {
    "figure_id": "F685",
    "report_id": "R035",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Global Public and Private Space Enablers ## The space computing economics"
  },
  {
    "figure_id": "F686",
    "report_id": "R035",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Global Public and Private Space Enablers ## The space computing economics"
  },
  {
    "figure_id": "F687",
    "report_id": "R035",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Global Public and Private Space Enablers ## The space computing economics"
  },
  {
    "figure_id": "F688",
    "report_id": "R035",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: Projected SpaceX Launch Costs/Kg Over Time (MSe)"
  },
  {
    "figure_id": "F689",
    "report_id": "R035",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: Projected SpaceX Launch Costs/Kg Over Time (MSe) Historical Costs & SpaceX Projection"
  },
  {
    "figure_id": "F690",
    "report_id": "R035",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: Projected SpaceX Launch Costs/Kg Over Time (MSe) Historical Costs & SpaceX Projection ## The compute payload The more credible architecture is a purpose-built compute satellite, not a standard data-center rack launch"
  },
  {
    "figure_id": "F691",
    "report_id": "R035",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: Projected SpaceX Launch Costs/Kg Over Time (MSe) Historical Costs & SpaceX Projection ## The compute payload The more credible architecture is a purpose-built compute satellite, not a standard data-center rack launch"
  },
  {
    "figure_id": "F692",
    "report_id": "R035",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: Common orbit choices – why dawn-dusk SSO is the sweet spot for compute ## 3. Thermal system: cooling becomes a radiator problem Space avoids terrestrial water cooling, cooling towers and air-based cooling systems, but"
  },
  {
    "figure_id": "F693",
    "report_id": "R035",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: Google's illustrative system: 81-satellite cluster in a 1km radius at a mean altitude of 650 km, with nearest-neighbor distances varying roughly between 100-200m ## 6. Storage and orchestration: software becomes the co"
  },
  {
    "figure_id": "F694",
    "report_id": "R035",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 12: What has to be redesigned? ## Mapping the technology supply chain Orbital compute systems rely on a complex web of ground infrastructure, including gateway stations, antenna arrays, network operations centers, terrestr"
  },
  {
    "figure_id": "F695",
    "report_id": "R050",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Weekly Orders ## Companies Mentioned: BYD (1211.HK; HK\\$83.8; 1; 06 Jul 26; 16:10) BYD (002594.SZ; Rmb87.54; 1; 06 Jul 26; 15:00) Geely Automobile (0175.HK; HK\\$18.64; 1; 06 Jul 26"
  },
  {
    "figure_id": "F696",
    "report_id": "R051",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: Starship's increased scale vs. Falcon and full reusability could drive launch costs into hundreds of dollars per kg SpaceX Starship BofA GLOBAL RESEARCH Exhibit 2: Falcon's demonstrated booster recovery and reflight ca"
  },
  {
    "figure_id": "F697",
    "report_id": "R051",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Falcon's demonstrated booster recovery and reflight capability has driven sea change in launch cadence and cost to orbit Landed Falcon 9 booster BofA GLOBAL RESEARCH ## (+) Sticky relationships with US, int'l customers"
  },
  {
    "figure_id": "F698",
    "report_id": "R051",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: BofAe AI segment capex exceeds \\$560bn by 2031E in base case driven principally by orbital compute, while bull case deployment could require \\$830bn of AI capex investment in 2031E BofAe AI segment capex by case, \\$ bn"
  },
  {
    "figure_id": "F699",
    "report_id": "R051",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: BofAe base and bull cases forecast Falcon to be retired in the early 2030s replaced by Starship"
  },
  {
    "figure_id": "F700",
    "report_id": "R051",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: BofAe base and bull cases forecast Falcon to be retired in the early 2030s replaced by Starship BofAe forecast Falcon launches by case, 2026E-2031E BofA GLOBAL RESEARCH ## Starship: step changes in capacity and cost St"
  },
  {
    "figure_id": "F701",
    "report_id": "R051",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: Connectivity capex to ramp with Starship availability, moderating as a % of revenue by 2031 Connectivity Capital expenditures, 2025A-2031E BofA GLOBAL RESEARCH ## Connectivity ## Starlink Broadband Starlink is position"
  },
  {
    "figure_id": "F702",
    "report_id": "R051",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: SpaceX's Connectivity offerings are enabled by a proliferated constellation of approximately 10,000 satellites Starlink deployment BofA GLOBAL RESEARCH There is a natural segmentation of the market. Terrestrial network"
  },
  {
    "figure_id": "F703",
    "report_id": "R051",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 12: Initial penetration could favor more rural geographies including central and eastern Europe % of population in rural areas by geography BofA GLOBAL RESEARCH ## Wireless Satellite direct-to-device (D2D) technology addre"
  },
  {
    "figure_id": "F704",
    "report_id": "R051",
    "label": "Exhibit 15",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: The company addresses an AI TAM of \\$26.5tn, inclusive of \\$22.7tn from enterprise applications"
  },
  {
    "figure_id": "F705",
    "report_id": "R051",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: The company addresses an AI TAM of \\$26.5tn, inclusive of \\$22.7tn from enterprise applications SpaceX AI TAM expectations BofA GLOBAL RESEARCH ## Terrestrial Compute SpaceX's terrestrial compute strategy is increasing"
  },
  {
    "figure_id": "F706",
    "report_id": "R051",
    "label": "Exhibit 18",
    "figure_type": "source_exhibit",
    "context": "Exhibit 19: Per Sensor Tower, as of June 2026, X had 179mn global mobile monthly active users (61mn MAUs in the US) X Monthly Active Users vs Major Social Platforms (mn)"
  },
  {
    "figure_id": "F707",
    "report_id": "R051",
    "label": "Exhibit 19",
    "figure_type": "source_exhibit",
    "context": "Exhibit 19: Per Sensor Tower, as of June 2026, X had 179mn global mobile monthly active users (61mn MAUs in the US) X Monthly Active Users vs Major Social Platforms (mn) BofA GLOBAL RESEARCH ## X to benefit from AI integration X c"
  },
  {
    "figure_id": "F708",
    "report_id": "R051",
    "label": "Exhibit 20",
    "figure_type": "source_exhibit",
    "context": "Exhibit 20: 2026 X ARPU remains relatively low versus major social platforms and suggests meaningful growth opportunity X Global ARPU vs Major Social Platforms (\\$), 2026 Note: Estimates based on Sensor Tower June 2026 MAU estimat"
  },
  {
    "figure_id": "F709",
    "report_id": "R051",
    "label": "Exhibit 21",
    "figure_type": "source_exhibit",
    "context": "Exhibit 21: Grok is xAI's large language model and AI assistant, integrated into X and available through Grok products Snapshot of Grok Platform BofA GLOBAL RESEARCH Exhibit 22: Per Sensor Tower, as of June 2026, standalone Grok a"
  },
  {
    "figure_id": "F710",
    "report_id": "R051",
    "label": "Exhibit 21",
    "figure_type": "source_exhibit",
    "context": "Exhibit 21: Grok is xAI's large language model and AI assistant, integrated into X and available through Grok products Snapshot of Grok Platform BofA GLOBAL RESEARCH Exhibit 22: Per Sensor Tower, as of June 2026, standalone Grok a"
  },
  {
    "figure_id": "F711",
    "report_id": "R051",
    "label": "Exhibit 23",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: Within two years of its initial release, Grok achieved frontier-level performance in scientific reasoning GPQA Diamond score of various Grok models BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F712",
    "report_id": "R051",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: Within two years of its initial release, Grok achieved frontier-level performance in scientific reasoning GPQA Diamond score of various Grok models BofA GLOBAL RESEARCH ## Grok monetization spans consumer and enterpris"
  },
  {
    "figure_id": "F713",
    "report_id": "R051",
    "label": "Exhibit 27",
    "figure_type": "source_exhibit",
    "context": "\\- Both terrestrial and orbital data center builds, as well as Terafab, will impact this increase, with orbital becoming a bigger portion of capex over time as Starship launches ramp \\- This investment is critical to sustaining SpaceX's rapid growth trajectory"
  },
  {
    "figure_id": "F714",
    "report_id": "R054",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "4. Launch Risks ## 1) Existing launch capabilities already market-leading SPCX is the global leader in orbital launch services. More than any other organization, SPCX has achieved space access at scale, transforming an entire industry. SpaceX designs, manufact"
  },
  {
    "figure_id": "F715",
    "report_id": "R054",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Today, SPCX's existing launch capabilities are supported by a wide range of critical and difficult to replicate assets which we summarize below: Falcon 9 – Falcon 9 stands as the world's first orbital-class rapidly reusable rocket, fundamentally transforming t"
  },
  {
    "figure_id": "F716",
    "report_id": "R054",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Falcon Heavy – Falcon Heavy represents one of the most powerful operational rockets in the world, generating over five million pounds of thrust at liftoff through its 27 Merlin engines across three reusable Falcon 9 boosters. With a payload capacity of approxi"
  },
  {
    "figure_id": "F717",
    "report_id": "R054",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Kennedy Space Center and Cape Canaveral, Florida – SpaceX's Florida operations represent the most comprehensive commercial launch infrastructure in the United States, spanning two active lau"
  },
  {
    "figure_id": "F718",
    "report_id": "R054",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Kennedy Space Center and Cape Canaveral, Florida – SpaceX's Florida operations represent the most comprehensive commercial launch infrastructure in the United States, spanning two active launch sites, Launch Complex 39A (LC-39A) and Space Launch Complex 40 (SL"
  },
  {
    "figure_id": "F719",
    "report_id": "R054",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Vandenberg Space Force Base, Space Launch Complex 4 – Space Launch Complex 4 East at Vandenberg Space Force Base serves as SpaceX's critical West Coast launch facility, uniquely positioned to support polar and high-inclination orbit missions essential for Star"
  },
  {
    "figure_id": "F720",
    "report_id": "R054",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9. Vandenberg Space Force Base, California Figure 10. Autonomous Drone Ship – Recovery Fleet ## 2) The ‘space disruptor’ disrupting itself through Starship While many competitors are trying to develop rocket technologies that are roughly Falcon 9-compet"
  },
  {
    "figure_id": "F721",
    "report_id": "R054",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "## 2) The ‘space disruptor’ disrupting itself through Starship While many competitors are trying to develop rocket technologies that are roughly Falcon 9-competitive, SPCX is disrupting its own launch business with the fully and rapidly reusable Starship. As d"
  },
  {
    "figure_id": "F722",
    "report_id": "R054",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Full and rapid reusability: Starship's core design innovation is its full and rapid approach to reusability: both stages return to Earth for catch and rapid refurbishment. The Super Heavy bo"
  },
  {
    "figure_id": "F723",
    "report_id": "R054",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "## 3) Falling launch costs open up new growth markets SPCX has already demonstrated a history of driving huge reductions in launch costs through the Falcon 9. With the first successful launch of Falcon 1 in 2008, SPCX became the first private company to succes"
  },
  {
    "figure_id": "F724",
    "report_id": "R054",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "## What drives the Starship unit cost advantage over time? ■ Payload capacity: The transition from SpaceX's Falcon class of rockets to the Starship launch system represents an unprecedented leap in orbital delivery capabilities, driving a massive unit cost adv"
  },
  {
    "figure_id": "F725",
    "report_id": "R054",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ■ Booster reusability: Central to SpaceX's cost reduction strategy is the reusability of key hardware, most notably first-stage boosters, which dramatically lowers per-launch costs by minimi"
  },
  {
    "figure_id": "F726",
    "report_id": "R054",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "The Broadband Constellation: With \\~9,600 satellites today expanding to 15,000+ more capable next generation V3 satellites over the next few years. The broadband constellation principally services two end markets globally: nomadic broadband (including to homes"
  },
  {
    "figure_id": "F727",
    "report_id": "R054",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Within the US market, for example, we believe a Build or Buy scenario is more likely than an MVNO scenario given the disinterest expressed by the national wireless carriers. While the market has assigned a greater probability to build, we see Buy as a logical "
  },
  {
    "figure_id": "F728",
    "report_id": "R054",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## 3) Expansion into full end-to-end mobile service offering SpaceX has not publicly committed to a specific path for scaling into full mobile services, but our view is that the company woul"
  },
  {
    "figure_id": "F729",
    "report_id": "R054",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "5) Enterprise AI Risks ## 1) Compute allocation influences overall monetization SpaceX's decisions around the mix of compute for inference, hosting and training workloads ultimately determine the shape of its AI revenue trajectory. AI solutions & infrastructur"
  },
  {
    "figure_id": "F730",
    "report_id": "R054",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 25. Citi Est. Rental Pricing GPU vs. SpaceX Contracted Rates (\\$/GPU/hr) © 2026 Citi Inc. No redistribution witho"
  },
  {
    "figure_id": "F731",
    "report_id": "R054",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 25. Citi Est. Rental Pricing GPU vs. SpaceX Contracted Rates (\\$/GPU/hr) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 26. Citi Est. SPCX AI Solutions & Infrastructure Revenue Breakdown: Intelligence vs. Compute-as-a-Servi"
  },
  {
    "figure_id": "F732",
    "report_id": "R054",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Grok's competitive API pricing could become an increasingly important factor in helping SPCX differentiate against LLM peers that have had a head start in enterprise, particularly as rapid g"
  },
  {
    "figure_id": "F733",
    "report_id": "R054",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "In enterprise adoption, Grok trails other US frontier models. Grok's initial consumer-orientated applications on X and the consumer Grok app is likely to have contributed to xAI lagging peers in the enterprise. The share of US businesses using Grok was 3% in M"
  },
  {
    "figure_id": "F734",
    "report_id": "R054",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "In addition to providing an immediate \\~\\$4B ARR lift to SPCX's top line, the Cursor acquisition (see announcement) should improve SpaceX's standing in the AI landscape given Cursor's position as one of the frontier AI coding platforms, its high-caliber AI tal"
  },
  {
    "figure_id": "F735",
    "report_id": "R054",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "people two years ago to now over 700. In addition to the sheer engineering talent added, Cursor is expected to accelerate SPCX's goal of building the best coding models and agentic products. Cursor leadership first joined xAI in mid-March with the hiring of An"
  },
  {
    "figure_id": "F736",
    "report_id": "R054",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "## We see four linked suppositions that underpin SpaceX's differentiated argument: (1) launch costs should decline structurally with Starship rapid reusability; (2) orbital solar power removes the largest long-term operating cost for terrestrial solutions (i.e"
  },
  {
    "figure_id": "F737",
    "report_id": "R054",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "4) SpaceX Partnership with Tesla ## 1) Extreme vertical integration explained SPCX believes one of its strengths is “Extreme Vertical Integration” which enables the company to operate at uniquely high velocity and super cost efficiency at scale. SPCX sees itse"
  },
  {
    "figure_id": "F738",
    "report_id": "R054",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## 2) Overview of Terafab Terafab is a multi-year, capital-intensive chip manufacturing initiative led by SpaceX in partnership with Tesla and Intel, announced in March 2026 (Tesla collabora"
  },
  {
    "figure_id": "F739",
    "report_id": "R054",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "## A) Why Terafab? Terafab functions as both a supply chain de-risking and margin capture strategy, addressing what SPCX sees as one of the key constraints to AI scaling: chip supply, data center infrastructure, and power. By insourcing chip manufacturing, Spa"
  },
  {
    "figure_id": "F740",
    "report_id": "R054",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "It is well understood by now that the semiconductor industry is facing persistent shortages across logic and memory driven by insatiable AI demand. From the logic perspective, TSMC faces prolonged tightness in advanced nodes (specifically N3 and N2) and advanc"
  },
  {
    "figure_id": "F741",
    "report_id": "R055",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## QM updates of Taobao app As of May 2026, Taobao MAU was 984mn, +1% yoy, and DAU was 417mn, +1% yoy. Time spent was 280mn, +7% yoy, and average time spent per MAU was 284mins, +6% yoy, per Questmobile. Figure 4. Taobao MAU © 2026 Citi Inc. No redistribution "
  },
  {
    "figure_id": "F742",
    "report_id": "R055",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "As of May 2026, Taobao MAU was 984mn, +1% yoy, and DAU was 417mn, +1% yoy. Time spent was 280mn, +7% yoy, and average time spent per MAU was 284mins, +6% yoy, per Questmobile. Figure 4. Taobao MAU © 2026 Citi Inc. No redistribution without Citi's written permi"
  },
  {
    "figure_id": "F743",
    "report_id": "R055",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Taobao DAU © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Taobao app time spent © 2026 Citi Inc. No redistribution without Citi's written permissio"
  },
  {
    "figure_id": "F744",
    "report_id": "R055",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Taobao app time spent © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Taobao app average time spent per MAU © 2026 Citi Inc. No redistribution witho"
  },
  {
    "figure_id": "F745",
    "report_id": "R056",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Tencent Cloud Hunyuan major milestones and achievements in 2026 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Tencent HY tokens processed on OpenRouter by products (bn) © 2026 Citi Inc. No redistribution without Citi"
  },
  {
    "figure_id": "F746",
    "report_id": "R056",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Based on SensorTower tracking, we aggregate 210 games among Tencent's game portfolio to derive a total domestic iOS grossing of US\\$1.42bn in 2Q26, -19% qoq and -1% yoy coming off from previous peak during CNY period. In 2Q26, HoK generated an estimated iOS gr"
  },
  {
    "figure_id": "F747",
    "report_id": "R056",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Similarly, SensorTower suggested that iOS grossing for Peacekeeper Elite also came off from CNY peak at US\\$223mn in 2Q26, comparing to US\\$344mn in 1Q26 and US\\$270mn in 2Q25, On the contrary, Delta Force's domestic iOS grossing remained steady at US\\$182mn i"
  },
  {
    "figure_id": "F748",
    "report_id": "R056",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9. HoK monthly iOS grossing Figure 10. Peacekeeper Elite monthly iOS grossing Figure 11. Delta Force monthly iOS grossing ## Three new games released during 2Q26"
  },
  {
    "figure_id": "F749",
    "report_id": "R056",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10. Peacekeeper Elite monthly iOS grossing Figure 11. Delta Force monthly iOS grossing ## Three new games released during 2Q26 Figure 12. Number of mobile games launched domestically by quarter"
  },
  {
    "figure_id": "F750",
    "report_id": "R056",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11. Delta Force monthly iOS grossing ## Three new games released during 2Q26 Figure 12. Number of mobile games launched domestically by quarter Per our tracking, Tencent released 3 domestic titles during 2Q26, compared with 6 games launched in 2Q25 and "
  },
  {
    "figure_id": "F751",
    "report_id": "R056",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "## AI-powered anti-addiction engine for minor protection Reported by Sina Finance dated Jul 4 (link), Tencent Games announced minor protection measures during summer 2026 on Jul 3. In addition to existing requirements and regulations to limit weekly gaming tim"
  },
  {
    "figure_id": "F752",
    "report_id": "R056",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "## Grossing performance of other overseas titles Figure 14. PUBG Mobile iOS + Google Play overseas grossing Figure 15. LoL: Wild Rift iOS + Google Play oversea grossing Figure 16. All-platform grossing of CODM worldwide Figure 17. All-platform grossing of six "
  },
  {
    "figure_id": "F753",
    "report_id": "R056",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15. LoL: Wild Rift iOS + Google Play oversea grossing Figure 16. All-platform grossing of CODM worldwide Figure 17. All-platform grossing of six Supercell titles Figure 18. Tencent mobile games pipeline"
  },
  {
    "figure_id": "F754",
    "report_id": "R056",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16. All-platform grossing of CODM worldwide Figure 17. All-platform grossing of six Supercell titles Figure 18. Tencent mobile games pipeline © 2025 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F755",
    "report_id": "R056",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## QM of music platforms As of May 2026, MAU of Kugou Music ranked No.1 at 201mn, -9% yoy, vs QQ Music at 194mn (+1% yoy) and Soda Music at 167mn (+75% yoy). As of May 2026, DAU of Soda Musi"
  },
  {
    "figure_id": "F756",
    "report_id": "R056",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "As of May 2026, MAU of Kugou Music ranked No.1 at 201mn, -9% yoy, vs QQ Music at 194mn (+1% yoy) and Soda Music at 167mn (+75% yoy). As of May 2026, DAU of Soda Music (59mn) surpassed QQ Music (51mn) and Kugou Music (49mn). Time spent of Kugou Music, QQ Music,"
  },
  {
    "figure_id": "F757",
    "report_id": "R056",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21. DAU (k) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 22. Time spent (k mins) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 23. Average time spent per MAU (mins) © 2026 Citi Inc. No redis"
  },
  {
    "figure_id": "F758",
    "report_id": "R056",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22. Time spent (k mins) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 23. Average time spent per MAU (mins) © 2026 Citi Inc. No redistribution without Citi's written permission. ## Buyback update till Jul 3 (US\\$3.2bn in 2"
  },
  {
    "figure_id": "F759",
    "report_id": "R056",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 28. SOTP valuation of Tencent Figure 29. Tencent – Forward PE Figure 30. Tencent – PE Band"
  },
  {
    "figure_id": "F760",
    "report_id": "R056",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29. Tencent – Forward PE Figure 30. Tencent – PE Band ## Companies Mentioned: Tencent Holdings (0700.HK; HK\\$461.2; 1; 07 Jul 26; 16:10)"
  },
  {
    "figure_id": "F761",
    "report_id": "R057",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "AI Power Architecture Is Evolving, Making BBU An Increasingly Important Part of Next Gen AIDC We believe AI infrastructure is entering a new power architecture cycle as rack power density continues to increase. Historically, datacenters relied on centralized U"
  },
  {
    "figure_id": "F762",
    "report_id": "R057",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "We believe AI infrastructure is entering a new power architecture cycle as rack power density continues to increase. Historically, datacenters relied on centralized UPS systems to provide backup power at the facility level. However, the transition toward rack-"
  },
  {
    "figure_id": "F763",
    "report_id": "R057",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "We believe the BBU market benefits from two growth drivers – higher content value per rack and broader industry adoption. Based on our bottom-up framework, we estimate BBU content value increases from c.US\\$15-16K per GB300 rack today to US\\$17-18K for Rubin, "
  },
  {
    "figure_id": "F764",
    "report_id": "R057",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Estimated Content Value Per Rack by Generation Figure 5. BBU Penetration Based on Our Estimates ## Initiate Dynapack (3211.TWO) at Buy with TP of NT\\$800 We initiate coverage of Dynapack with a Buy rating and a TP of NT\\$800, as we view it as one of "
  },
  {
    "figure_id": "F765",
    "report_id": "R057",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "We initiate coverage of Dynapack with a Buy rating and a TP of NT\\$800, as we view it as one of the most direct beneficiaries of the structural expansion in the BBU market. We expect the company to benefit from accelerating BBU adoption, rising content value a"
  },
  {
    "figure_id": "F766",
    "report_id": "R057",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6. Earnings Estimate vs. BBG © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Dynapack: Earnings and YoY © 2026 Citi Inc. No redistribution without Citi's written permission. \\*Adjusted earnings exclude non-operating gains"
  },
  {
    "figure_id": "F767",
    "report_id": "R057",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7. Dynapack: Earnings and YoY © 2026 Citi Inc. No redistribution without Citi's written permission. \\*Adjusted earnings exclude non-operating gains from real estate disposal in 2021 and 2024. Figure 8. Dynapack: Forward P/E vs. Earnings Growth Figure 9."
  },
  {
    "figure_id": "F768",
    "report_id": "R057",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "\\*Adjusted earnings exclude non-operating gains from real estate disposal in 2021 and 2024. Figure 8. Dynapack: Forward P/E vs. Earnings Growth Figure 9. Peer Comp: Forward P/E vs. Earnings CAGR ## Why We Prefer Dynapack over AES While AES remains the dominant"
  },
  {
    "figure_id": "F769",
    "report_id": "R057",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Its value is not necessarily to run the rack for hours, but to bridge short outrages, ride through grid fluctuations, and to protect the rack while upstream UPS, generator, or power-management systems respond. The BBU content value should scale with AI rack po"
  },
  {
    "figure_id": "F770",
    "report_id": "R057",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Its value is not necessarily to run the rack for hours, but to bridge short outrages, ride through grid fluctuations, and to protect the rack while upstream UPS, generator, or power-management systems respond. The BBU content value should scale with AI rack po"
  },
  {
    "figure_id": "F771",
    "report_id": "R057",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13. BBU Is More Ideal for Close-to-Load Backup Power Support © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 14. 3kW BBU Figure 15. BBU in A Power Rack Historically, datacenters have relied heavily on centralized UPS as the "
  },
  {
    "figure_id": "F772",
    "report_id": "R057",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 14. 3kW BBU Figure 15. BBU in A Power Rack Historically, datacenters have relied heavily on centralized UPS as the main backup power system during outages. However, as AI datacenters "
  },
  {
    "figure_id": "F773",
    "report_id": "R057",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "BBU is not a formally mandatory component in every GB200/GB300 deployment based on public NVIDIA specifications. However, given the rack-scale power architecture of NVL72 systems and the growing adoption of OCP ORv3 (short for “Open Compute Project Open Rack S"
  },
  {
    "figure_id": "F774",
    "report_id": "R057",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "We believe HVDC would raise the value of BBU systems. As AI rack power rises from 100KW+ toward several hundred kW in future platforms, backup power requirements should also increase. Higher-power racks require greater battery capacity, higher discharge-rate c"
  },
  {
    "figure_id": "F775",
    "report_id": "R057",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "■ Key players include AES (6781.TW; Buy-rated), Dynapack (3211.TWO; Buy-rated), STL (4931.TWO; not covered), Sysgration (5309.TWO; not covered), BorgWarner (BWA.US; not covered), and Flex (FLEX.US; not covered). Player such as Flex also engage in downstream po"
  },
  {
    "figure_id": "F776",
    "report_id": "R057",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "For Rubin Ultra, rack power could reach 600KW, representing a step-change in AI rack power density. At this power level, lower-power BBU modules would become impractical due to the large number of modules required. We hence assume the adoption of 25KW BBU modu"
  },
  {
    "figure_id": "F777",
    "report_id": "R057",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Few drivers in this stage include 1) AI rack power density continues to rise. Higher rack power makes short-duration ride through protection more important. 2) OCP ORv3 defines a BBU shelf architecture, with BBU shelf connected to the rack-level DC bus. We bel"
  },
  {
    "figure_id": "F778",
    "report_id": "R057",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "We believe Dynapack is well positioned to benefit from rising BBU demand driven by AIDC infrastructure buildout. As AI server racks move from traditional low-power racks to high-density GPU racks, rack level consumption is increasing significantly. This create"
  },
  {
    "figure_id": "F779",
    "report_id": "R057",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23. Estimated Content Value Per Rack by Generation © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 24. BBU Penetration Based on Our Estimates © 2026 Citi Inc. No redistribution without Citi's written permission. For Dynapack"
  },
  {
    "figure_id": "F780",
    "report_id": "R057",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "We think Dynapack's BBU opportunity is not only a volume growth story but also a content value expansion story – as AI rack power rises, the required backup power per rack should increase, suggesting higher BBU content value per rack over time. Furthermore, we"
  },
  {
    "figure_id": "F781",
    "report_id": "R057",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Note: Market share of Panasonic is based on Panasonic's investor presentation. AES, Dynapack and STL market share is based on our estimates. Per Dynapack, the majority of products selling to PSU operators are 3KW and 5.5KW BBU modules in 2026E and they expect "
  },
  {
    "figure_id": "F782",
    "report_id": "R057",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26. Dynapack: BBU Products Pipeline © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 27. Dynapack: Group Sales and YoY Figure 28. Dynapack: IT Sales and Non-IT Sales YoY ## What Are Dynapack's Competitive Advantages vs. Other"
  },
  {
    "figure_id": "F783",
    "report_id": "R057",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 27. Dynapack: Group Sales and YoY Figure 28. Dynapack: IT Sales and Non-IT Sales YoY ## What Are Dynapack's Competitive Advantages vs. Other BBU suppliers? 1. Strong battery-pack know"
  },
  {
    "figure_id": "F784",
    "report_id": "R057",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "1. Strong battery-pack know-how – it has a long operating history as a lithium-ion battery-pack maker, specializing in pack design, cell integration, battery management, safety validation, and customized manufacturing. 2. Strong partnership with PSU operators "
  },
  {
    "figure_id": "F785",
    "report_id": "R057",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "## Investment positive #2 – Intact margin expansion from rising non-IT sales In contrast, BBU products are still in an early growth stage and require highly customized designs, higher reliability standards, stricter safety validation, and closer collaboration "
  },
  {
    "figure_id": "F786",
    "report_id": "R057",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "In contrast, BBU products are still in an early growth stage and require highly customized designs, higher reliability standards, stricter safety validation, and closer collaboration with PSU operators and CSPs. We estimate BBU GPM to be 30-35%, benchmarked wi"
  },
  {
    "figure_id": "F787",
    "report_id": "R057",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "This partnership model allows Dynapack to gain access to a broader downstream customer base. Major PSU operators usually serve multiple CSPs, ODMs, and AI server programs. By working with more than one PSU customer, Dynapack can participate in multiple end-cus"
  },
  {
    "figure_id": "F788",
    "report_id": "R057",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "We also think PSU operators would have strong incentives to work with specialized BBU pack suppliers instead of fully internalizing the battery-packs as PSU vendors' core strength is power conversion, rectifiers, power shelves, rack-level distribution and syst"
  },
  {
    "figure_id": "F789",
    "report_id": "R057",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35. BBU FY26 Sales Comparison - Panasonic Is 10x Larger Than Dynapack Figure 36. Delta (2308.TW) AI Server Power Sales Estimates © 2026 Citi Inc. No redistribution without Citi's written permission. ## Would PSU Operators Fully Vertically Integrate into"
  },
  {
    "figure_id": "F790",
    "report_id": "R057",
    "label": "Figure 40",
    "figure_type": "source_exhibit",
    "context": "Net gearing remains negative throughout our forecast period, indicating that the company maintains a net cash balance. We believe that their capacity expansion is not overly dependent on external financing and the company still has room to fund capacity ramp-u"
  },
  {
    "figure_id": "F791",
    "report_id": "R057",
    "label": "Figure 40",
    "figure_type": "source_exhibit",
    "context": "Dynapack's cash conversion lowered to 55 days in 2025, down from 2022's 86 days. We forecast it to further improve to 48 days in 2026E and 38 days in 2027E. This improvement is mainly supported by stronger payable days and better inventory discipline. Figure 4"
  },
  {
    "figure_id": "F792",
    "report_id": "R057",
    "label": "Figure 44",
    "figure_type": "source_exhibit",
    "context": "Our target P/E of 32x is also close to the high end of historical forward P/E range of 14-31x since the stock re-rated in 2025, which we view as justified in view of Dynapack's exposure to secular AI datacenter power demand, potential BBU content value increas"
  },
  {
    "figure_id": "F793",
    "report_id": "R057",
    "label": "Figure 44",
    "figure_type": "source_exhibit",
    "context": "We believe Dynapack is likely to re-rate from its historical valuation range, supported by its transition from a mature IT battery pack supplier to an AIDC BBU beneficiary and aggressive capacity expansion, driving strong margin expansion and robust earnings m"
  },
  {
    "figure_id": "F794",
    "report_id": "R057",
    "label": "Figure 45",
    "figure_type": "source_exhibit",
    "context": "Figure 45. Dynapack: Forward P/B vs. ROE Figure 46. Peer Comp: Forward P/E vs. Earnings CAGR © 2026 Citi Inc. No redistribution without Citi's written permission. ## Key Downside Risks to Our Price Target/Rating Are: 1. Slower-than-expected BBU adoption in AID"
  },
  {
    "figure_id": "F795",
    "report_id": "R057",
    "label": "Figure 47",
    "figure_type": "source_exhibit",
    "context": "Established in 1998 and listed on the Taipei Exchange in 2004, Dynapack is a Taiwan-based lithium-ion battery pack manufacturer, focusing on customized battery pack design, engineering, manufacturing and system integration. Dynapack's headquarters is located i"
  },
  {
    "figure_id": "F796",
    "report_id": "R057",
    "label": "Figure 47",
    "figure_type": "source_exhibit",
    "context": "Figure 47. Dynapack: Battery Packs for IT Products Figure 48. Dynapack: BBU Product (3.2KW) Figure 49. Dynapack: Sales of IT vs. Non IT © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 50. Dynapack: Production Presence © 2026 Citi I"
  },
  {
    "figure_id": "F797",
    "report_id": "R057",
    "label": "Figure 49",
    "figure_type": "source_exhibit",
    "context": "Figure 49. Dynapack: Sales of IT vs. Non IT © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 50. Dynapack: Production Presence © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 51. Dynapack: Key Milestones"
  },
  {
    "figure_id": "F798",
    "report_id": "R057",
    "label": "Figure 52",
    "figure_type": "source_exhibit",
    "context": "Chung Tsung Ming (Chairman) – Chairman Chung has a finance and accounting background with an MBA from National Chengchi University and a bachelor's degree in accounting from the National Taiwan University. Prior to Dynapack, he was a partner at Deloitte. He ha"
  },
  {
    "figure_id": "F799",
    "report_id": "R057",
    "label": "Figure 52",
    "figure_type": "source_exhibit",
    "context": "Lin Yu Hui (CFO) – Ms. Lin serves as senior finance executive and the company's spokesperson. She holds a master's degree in Accounting from National Taiwan University. She was the manager of the audit department at Deloitte before joining the firm. Figure 52."
  },
  {
    "figure_id": "F800",
    "report_id": "R057",
    "label": "Figure 54",
    "figure_type": "source_exhibit",
    "context": "Figure 54. AES: Sales Growth and Y/Y © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 55. AES: Margins Trend © 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F801",
    "report_id": "R057",
    "label": "Figure 54",
    "figure_type": "source_exhibit",
    "context": "Figure 54. AES: Sales Growth and Y/Y © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 55. AES: Margins Trend © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 56. AES: Earnings Growth and Y/Y © 2026 Citi I"
  },
  {
    "figure_id": "F802",
    "report_id": "R057",
    "label": "Figure 55",
    "figure_type": "source_exhibit",
    "context": "Figure 55. AES: Margins Trend © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 56. AES: Earnings Growth and Y/Y © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 57. AES: Forward P/E and Earnings Growth © "
  },
  {
    "figure_id": "F803",
    "report_id": "R057",
    "label": "Figure 56",
    "figure_type": "source_exhibit",
    "context": "Figure 56. AES: Earnings Growth and Y/Y © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 57. AES: Forward P/E and Earnings Growth © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 58. AES: Earnings Estimat"
  },
  {
    "figure_id": "F804",
    "report_id": "R058",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: The share price of Xinyi Solar vs. solar glass industry inventory Figure 2: Solar glass - monthly supply-demand analysis (DBe)"
  },
  {
    "figure_id": "F805",
    "report_id": "R058",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: The share price of Xinyi Solar vs. solar glass industry inventory Figure 2: Solar glass - monthly supply-demand analysis (DBe)"
  },
  {
    "figure_id": "F806",
    "report_id": "R058",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Polysilicon industry inventory (at polysilicon producers)"
  },
  {
    "figure_id": "F807",
    "report_id": "R058",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Polysilicon industry inventory (at polysilicon producers)"
  },
  {
    "figure_id": "F808",
    "report_id": "R058",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Polysilicon industry monthly output and average capacity utilization rate"
  },
  {
    "figure_id": "F809",
    "report_id": "R058",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Polysilicon supply-demand analysis (DBe)"
  },
  {
    "figure_id": "F810",
    "report_id": "R058",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Polysilicon industry inventory (at polysilicon producers)"
  },
  {
    "figure_id": "F811",
    "report_id": "R058",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Polysilicon spot prices"
  },
  {
    "figure_id": "F812",
    "report_id": "R058",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Polysilicon spot prices"
  },
  {
    "figure_id": "F813",
    "report_id": "R058",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Polysilicon spot prices"
  },
  {
    "figure_id": "F814",
    "report_id": "R058",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Polysilicon futures price"
  },
  {
    "figure_id": "F815",
    "report_id": "R058",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Wafer monthly output and industry average capacity utilization rate"
  },
  {
    "figure_id": "F816",
    "report_id": "R058",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Wafer monthly output and industry average capacity utilization rate"
  },
  {
    "figure_id": "F817",
    "report_id": "R058",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Wafer monthly output and industry average capacity utilization rate"
  },
  {
    "figure_id": "F818",
    "report_id": "R058",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Wafer spot prices"
  },
  {
    "figure_id": "F819",
    "report_id": "R058",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Wafer spot prices"
  },
  {
    "figure_id": "F820",
    "report_id": "R058",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Wafer spot prices"
  },
  {
    "figure_id": "F821",
    "report_id": "R058",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Wafer unit net profit tracker"
  },
  {
    "figure_id": "F822",
    "report_id": "R058",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Cell monthly output and industry average capacity utilization rate Figure 21: Cell weekly industry inventory"
  },
  {
    "figure_id": "F823",
    "report_id": "R058",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Cell monthly output and industry average capacity utilization rate Figure 21: Cell weekly industry inventory"
  },
  {
    "figure_id": "F824",
    "report_id": "R058",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 23: Cell spot prices"
  },
  {
    "figure_id": "F825",
    "report_id": "R058",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23: Cell spot prices"
  },
  {
    "figure_id": "F826",
    "report_id": "R058",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 23: Cell spot prices"
  },
  {
    "figure_id": "F827",
    "report_id": "R058",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Figure 24: Cell unit net profit trackers"
  },
  {
    "figure_id": "F828",
    "report_id": "R058",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Module monthly output and industry average capacity utilization rate"
  },
  {
    "figure_id": "F829",
    "report_id": "R058",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Module monthly output and industry average capacity utilization rate"
  },
  {
    "figure_id": "F830",
    "report_id": "R058",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Module spot prices"
  },
  {
    "figure_id": "F831",
    "report_id": "R058",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Module spot prices"
  },
  {
    "figure_id": "F832",
    "report_id": "R058",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Module spot prices"
  },
  {
    "figure_id": "F833",
    "report_id": "R058",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Figure 30: Module prices for utility-scale and distributed solar"
  },
  {
    "figure_id": "F834",
    "report_id": "R058",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Figure 33: TOPCon – Highest efficient commercial solar modules (June 2026)"
  },
  {
    "figure_id": "F835",
    "report_id": "R058",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 33: TOPCon – Highest efficient commercial solar modules (June 2026)"
  },
  {
    "figure_id": "F836",
    "report_id": "R058",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "Figure 34: Solar glass - industry operating capacity and inventory days"
  },
  {
    "figure_id": "F837",
    "report_id": "R058",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "Figure 37: Solar glass - annual capacities and utilization trend"
  },
  {
    "figure_id": "F838",
    "report_id": "R058",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Solar glass - monthly supply-demand analysis (DBe)"
  },
  {
    "figure_id": "F839",
    "report_id": "R058",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "Figure 38: Solar glass spot prices"
  },
  {
    "figure_id": "F840",
    "report_id": "R058",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: Solar glass spot prices"
  },
  {
    "figure_id": "F841",
    "report_id": "R058",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: Solar glass spot prices"
  },
  {
    "figure_id": "F842",
    "report_id": "R058",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "Figure 41: China monthly solar installations"
  },
  {
    "figure_id": "F843",
    "report_id": "R058",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 41: China monthly solar installations"
  },
  {
    "figure_id": "F844",
    "report_id": "R058",
    "label": "Figure 41",
    "figure_type": "source_exhibit",
    "context": "Figure 41: China monthly solar installations"
  },
  {
    "figure_id": "F845",
    "report_id": "R058",
    "label": "Figure 42",
    "figure_type": "source_exhibit",
    "context": "Figure 42: China monthly solar installations (YoY)"
  },
  {
    "figure_id": "F846",
    "report_id": "R058",
    "label": "Figure 44",
    "figure_type": "source_exhibit",
    "context": "Figure 44: China Solar Sector - valuation comparison"
  },
  {
    "figure_id": "F847",
    "report_id": "R058",
    "label": "Figure 45",
    "figure_type": "source_exhibit",
    "context": "Figure 45: GCL Technology – one-year forward P/B bands"
  },
  {
    "figure_id": "F848",
    "report_id": "R059",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla) Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend Figure 4: Weekly HIMA (mainly AITO) new orders trend"
  },
  {
    "figure_id": "F849",
    "report_id": "R059",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla) Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend Figure 4: Weekly HIMA (mainly AITO) new orders trend Figure 5: Weekly"
  },
  {
    "figure_id": "F850",
    "report_id": "R059",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend Figure 4: Weekly HIMA (mainly AITO) new orders trend Figure 5: Weekly Li Auto new orders trend Figure 6: Weekly NIO group new orders trend"
  },
  {
    "figure_id": "F851",
    "report_id": "R059",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Weekly HIMA (mainly AITO) new orders trend Figure 5: Weekly Li Auto new orders trend Figure 6: Weekly NIO group new orders trend Figure 7: Weekly Tesla new orders trend"
  },
  {
    "figure_id": "F852",
    "report_id": "R059",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Weekly Li Auto new orders trend Figure 6: Weekly NIO group new orders trend Figure 7: Weekly Tesla new orders trend ## Appendix 1"
  },
  {
    "figure_id": "F853",
    "report_id": "R059",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Weekly NIO group new orders trend Figure 7: Weekly Tesla new orders trend ## Appendix 1 ## Important Disclosures For disclosures pertaining to recommendations or estimates made on securities other than the primary su"
  },
  {
    "figure_id": "F854",
    "report_id": "R060",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Embodied robots from Codroid: Codroid 02 (LHS) and C05-L (RHS)"
  },
  {
    "figure_id": "F855",
    "report_id": "R060",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Financials (quarterly): net profit reached a record high in 1Q26, primarily driven by non-operating fair value changes in equity investments"
  },
  {
    "figure_id": "F856",
    "report_id": "R060",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Estun was the largest robot manufacturer in the China industrial robot market in 1Q26 (by unit)"
  },
  {
    "figure_id": "F857",
    "report_id": "R060",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Estun was the largest robot manufacturer in the China industrial robot market in 1Q26 (by unit)"
  },
  {
    "figure_id": "F858",
    "report_id": "R060",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Chinese robot makers led by Estun have been gaining shares in the China industrial robot market (market share over time)"
  },
  {
    "figure_id": "F859",
    "report_id": "R060",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Chinese robot makers led by Estun have been gaining shares in the China industrial robot market (market share over time)"
  },
  {
    "figure_id": "F860",
    "report_id": "R060",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Estun's market share in China - Quarterly (LHS) and yearly (RHS) - Estun has higher shares in large 6-axis robots"
  },
  {
    "figure_id": "F861",
    "report_id": "R060",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 9: DCF assumptions and target prices"
  },
  {
    "figure_id": "F862",
    "report_id": "R060",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 9: DCF assumptions and target prices"
  },
  {
    "figure_id": "F863",
    "report_id": "R060",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: DCF model for A shares"
  },
  {
    "figure_id": "F864",
    "report_id": "R060",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Discount of Estun's H shares against A shares has widened"
  },
  {
    "figure_id": "F865",
    "report_id": "R060",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Comp sheet for listed peers"
  },
  {
    "figure_id": "F866",
    "report_id": "R061",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: VNET revenue and YoY growth"
  },
  {
    "figure_id": "F867",
    "report_id": "R061",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: VNET revenue and YoY growth"
  },
  {
    "figure_id": "F868",
    "report_id": "R061",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: VNET revenue and YoY growth"
  },
  {
    "figure_id": "F869",
    "report_id": "R061",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Current capacity under construction & delivery pipeline"
  },
  {
    "figure_id": "F870",
    "report_id": "R061",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Current capacity under construction & delivery pipeline"
  },
  {
    "figure_id": "F871",
    "report_id": "R061",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Current capacity under construction & delivery pipeline"
  },
  {
    "figure_id": "F872",
    "report_id": "R061",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Revenue & YoY growth forecasts"
  },
  {
    "figure_id": "F873",
    "report_id": "R061",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: VNET's wholesale data center portfolio"
  },
  {
    "figure_id": "F874",
    "report_id": "R061",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: VNET's wholesale data center portfolio"
  },
  {
    "figure_id": "F875",
    "report_id": "R061",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Wholesale capacity utilized"
  },
  {
    "figure_id": "F876",
    "report_id": "R061",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Wholesale capacity utilized"
  },
  {
    "figure_id": "F877",
    "report_id": "R061",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Wholesale utilization rate"
  },
  {
    "figure_id": "F878",
    "report_id": "R061",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Retail capacity utilized"
  },
  {
    "figure_id": "F879",
    "report_id": "R061",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15: Retail utilization rate"
  },
  {
    "figure_id": "F880",
    "report_id": "R061",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Adj.EBITDA margin & cash gross margin forecasts"
  },
  {
    "figure_id": "F881",
    "report_id": "R061",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Capex & capex to revenue ratio"
  },
  {
    "figure_id": "F882",
    "report_id": "R061",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Capex & capex to revenue ratio"
  },
  {
    "figure_id": "F883",
    "report_id": "R061",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22: China cloud hyperscalers' capex"
  },
  {
    "figure_id": "F884",
    "report_id": "R061",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 24: Major downstream customers capex"
  },
  {
    "figure_id": "F885",
    "report_id": "R061",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: China data center share by power capacity in 2025"
  },
  {
    "figure_id": "F886",
    "report_id": "R061",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: China data center share by power capacity in 2025"
  },
  {
    "figure_id": "F887",
    "report_id": "R061",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: China data center share by power capacity in 2025"
  },
  {
    "figure_id": "F888",
    "report_id": "R061",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 27: Third-party IDC players' revenue"
  },
  {
    "figure_id": "F889",
    "report_id": "R061",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Unit capex breakdown by region Figure 33: COGS breakdown and development yield # Valuation and risks We use DCF model for valuation, which in our view is the most appropriate method as it effectively captures the lon"
  },
  {
    "figure_id": "F890",
    "report_id": "R061",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Unit capex breakdown by region Figure 33: COGS breakdown and development yield # Valuation and risks We use DCF model for valuation, which in our view is the most appropriate method as it effectively captures the lon"
  },
  {
    "figure_id": "F891",
    "report_id": "R061",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: 12mth-fwd EV/EBITDA"
  },
  {
    "figure_id": "F892",
    "report_id": "R061",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: 12mth-fwd EV/EBITDA"
  },
  {
    "figure_id": "F893",
    "report_id": "R061",
    "label": "Figure 36",
    "figure_type": "source_exhibit",
    "context": "Figure 36: 12mth-fwd EV/sales"
  },
  {
    "figure_id": "F894",
    "report_id": "R061",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: 12mth-fwd P/B"
  },
  {
    "figure_id": "F895",
    "report_id": "R061",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 38: Short ratio (days to cover)"
  },
  {
    "figure_id": "F896",
    "report_id": "R061",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "Figure 39: BBG consensus revenue"
  },
  {
    "figure_id": "F897",
    "report_id": "R062",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: All Ring's revenue growth outlook Exhibit 2: All Ring's margin trend ## Earnings changes, valuation and risks"
  },
  {
    "figure_id": "F898",
    "report_id": "R062",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: All Ring's revenue growth outlook Exhibit 2: All Ring's margin trend ## Earnings changes, valuation and risks ## Forecast changes We revise our 2026E-28E EPS by $+7.2\\% / -6.0\\% / -11.6\\%$ mainly as we factor in 1) s"
  },
  {
    "figure_id": "F899",
    "report_id": "R062",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Taiex vs. All Ring Exhibit 6: Forward P/E Exhibit 7: Forward P/B"
  },
  {
    "figure_id": "F900",
    "report_id": "R062",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Taiex vs. All Ring Exhibit 6: Forward P/E Exhibit 7: Forward P/B Exhibit 8: P/B vs. ROE"
  },
  {
    "figure_id": "F901",
    "report_id": "R062",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: Forward P/E Exhibit 7: Forward P/B Exhibit 8: P/B vs. ROE ## Investment Thesis - All Ring (6187.TWO)"
  },
  {
    "figure_id": "F902",
    "report_id": "R062",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Forward P/B Exhibit 8: P/B vs. ROE ## Investment Thesis - All Ring (6187.TWO) All Ring is one of the key suppliers of semiconductor equipment in Taiwan, primarily utilized in back-end advanced packaging processes. Th"
  },
  {
    "figure_id": "F903",
    "report_id": "R064",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: Year-over-year PPI inflation edged up from May to June Exhibit 2: Food CPI inflation was roughly unchanged from May to June Exhibit 3: Goods inflation moderated mainly on lower energy prices in June"
  },
  {
    "figure_id": "F904",
    "report_id": "R064",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: Year-over-year PPI inflation edged up from May to June Exhibit 2: Food CPI inflation was roughly unchanged from May to June Exhibit 3: Goods inflation moderated mainly on lower energy prices in June Exhibit 4: PPI"
  },
  {
    "figure_id": "F905",
    "report_id": "R064",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Food CPI inflation was roughly unchanged from May to June Exhibit 3: Goods inflation moderated mainly on lower energy prices in June Exhibit 4: PPI inflation edged up from May to June, mainly due to higher downstream"
  },
  {
    "figure_id": "F906",
    "report_id": "R064",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: Goods inflation moderated mainly on lower energy prices in June Exhibit 4: PPI inflation edged up from May to June, mainly due to higher downstream prices ## The China Economics Team Andrew Tilton GS (Asia) L.L.C."
  },
  {
    "figure_id": "F907",
    "report_id": "R066",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: TSE Standard net buying 2-year chart as of Jun 26 2026, JPY bn Exhibit 2: TSE Growth net buying 2-year chart as of Jun 26 2026, JPY bn ## GS Covered Japan SMID Stocks"
  },
  {
    "figure_id": "F908",
    "report_id": "R066",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: TSE Standard net buying 2-year chart as of Jun 26 2026, JPY bn Exhibit 2: TSE Growth net buying 2-year chart as of Jun 26 2026, JPY bn ## GS Covered Japan SMID Stocks Exhibit 3: GS covered SMID stocks ranked by month"
  },
  {
    "figure_id": "F909",
    "report_id": "R066",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Median / mean CEO approval ratings Exhibit 7: Over 85% of SMID companies now have approval ratings over 80% Exhibit 6: Disparity historically higher amongst SMIDs"
  },
  {
    "figure_id": "F910",
    "report_id": "R066",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Over 85% of SMID companies now have approval ratings over 80% Exhibit 6: Disparity historically higher amongst SMIDs Exhibit 8: Volatility of yoy changes in SMID CEO approval ratings ■ Volatility of YoY changes in AG"
  },
  {
    "figure_id": "F911",
    "report_id": "R066",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: Disparity historically higher amongst SMIDs Exhibit 8: Volatility of yoy changes in SMID CEO approval ratings ■ Volatility of YoY changes in AGM CEO approval rating ## Exhibit 9: Top 15 SMID companies by CEO approv"
  },
  {
    "figure_id": "F912",
    "report_id": "R066",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: Volatility of yoy changes in SMID CEO approval ratings ■ Volatility of YoY changes in AGM CEO approval rating ## Exhibit 9: Top 15 SMID companies by CEO approval rating yoy change"
  },
  {
    "figure_id": "F913",
    "report_id": "R066",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: Banks index 52-week equal-weighted cumulative weekly performance and best-worst spreads The criteria we have used in our analysis of the liquid Japanese equities market can be summarized as follows: ■ Total universe co"
  },
  {
    "figure_id": "F914",
    "report_id": "R067",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: COST core comp, y/y Core Comp consists of global SSS, ex. gas & FX Exhibit 2: COST core comp growth trends Core Comp consists of global SSS, ex. gas & FX"
  },
  {
    "figure_id": "F915",
    "report_id": "R067",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: COST core comp, y/y Core Comp consists of global SSS, ex. gas & FX Exhibit 2: COST core comp growth trends Core Comp consists of global SSS, ex. gas & FX Exhibit 3: COST monthly negative cannibalization impact ## C"
  },
  {
    "figure_id": "F916",
    "report_id": "R067",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: COST core comp growth trends Core Comp consists of global SSS, ex. gas & FX Exhibit 3: COST monthly negative cannibalization impact ## Category Detail Fresh Foods was up +MSD (vs. +HSD in May, +HSD in April, and +MSD"
  },
  {
    "figure_id": "F917",
    "report_id": "R068",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: Price increased YTD LCD TV panel price trend ## AI TV, Gaming monitor, E-paper smart tracker Verena Jeng GS (Asia) L.L.C."
  },
  {
    "figure_id": "F918",
    "report_id": "R068",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Changhong 100D8S Pro Exhibit 3: Insta360's Mic Pro with e-paper display Exhibit 4: Specification of Changhong 100D8S Pro"
  },
  {
    "figure_id": "F919",
    "report_id": "R068",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Changhong 100D8S Pro Exhibit 3: Insta360's Mic Pro with e-paper display Exhibit 4: Specification of Changhong 100D8S Pro"
  },
  {
    "figure_id": "F920",
    "report_id": "R069",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: We expect L'Oréal Luxe to return to its high-single-digit growth algorithm L'Oréal Luxe Organic Sales Growth"
  },
  {
    "figure_id": "F921",
    "report_id": "R069",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: L'Oréal Luxe margin has been under pressure since FY23 L'Oréal Luxe Adjusted EBIT margin Exhibit 2: Lancome is the largest L'Oréal Luxe brand, followed by YSL and Armani L'Oréal Luxe sales by brand, 2025 Exhibit 3: W"
  },
  {
    "figure_id": "F922",
    "report_id": "R069",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: The fragrance business was 3.5x larger in FY25 vs FY10 L'Oréal fragrance sales (EURm) and organic sales growth"
  },
  {
    "figure_id": "F923",
    "report_id": "R069",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: Fragrance now accounts for $15\\%$ of annual sales vs $9\\%$ in FY10 L'Oréal group sales by category"
  },
  {
    "figure_id": "F924",
    "report_id": "R069",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: The fragrance business was 3.5x larger in FY25 vs FY10 L'Oréal fragrance sales (EURm) and organic sales growth Exhibit 6: Fragrance now accounts for $15\\%$ of annual sales vs $9\\%$ in FY10 L'Oréal group sales by catego"
  },
  {
    "figure_id": "F925",
    "report_id": "R069",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: There is significant headroom for Gucci beauty to grow at least to the size of YSL Fashion House vs Beauty sales for key L'Oréal Luxe brands and Gucci"
  },
  {
    "figure_id": "F926",
    "report_id": "R069",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: There is significant headroom for Gucci beauty to grow at least to the size of YSL Fashion House vs Beauty sales for key L'Oréal Luxe brands and Gucci Exhibit 8: YSL beauty is c10x the size than it was at the beginning"
  },
  {
    "figure_id": "F927",
    "report_id": "R069",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: Prada grew 3.5x over 2021-24"
  },
  {
    "figure_id": "F928",
    "report_id": "R069",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Exhibit 8: YSL beauty is c10x the size than it was at the beginning of the license Exhibit 10: Prada grew 3.5x over 2021-24 ## What to expect at Q2 results?"
  },
  {
    "figure_id": "F929",
    "report_id": "R069",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: Q2/H1 26 GSe vs Company-compiled and Visible Alpha Consensus Data"
  },
  {
    "figure_id": "F930",
    "report_id": "R070",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Biz Message and DA both appear to have continued YoY growth in 2Q Exhibit 3: Core ad demand remains healthy and Talk Biz remains the key driver of Platform resilience Exhibit 4: Top line growth momentum should be sup"
  },
  {
    "figure_id": "F931",
    "report_id": "R070",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: We expect Kakao to sustain solid OP margin above $10\\%$ level in 2Q"
  },
  {
    "figure_id": "F932",
    "report_id": "R070",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: We expect Kakao to sustain solid OP margin above $10\\%$ level in 2Q ## Earnings revision"
  },
  {
    "figure_id": "F933",
    "report_id": "R070",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: Top line growth momentum should be supported by Platform Biz, but we expect Portal Biz impact from AXZ deconsolidation from May to slightly offset revenue growth Exhibit 5: We expect Kakao to sustain solid OP margin ab"
  },
  {
    "figure_id": "F934",
    "report_id": "R071",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Icotyde Patients Primarily Expected to be Either New to Branded Systemic or Switching from Oral Branded"
  },
  {
    "figure_id": "F935",
    "report_id": "R071",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Icotyde Patients Primarily Expected to be Either New to Branded Systemic or Switching from Oral Branded Q3. Among NEW patients initiating on a branded systemic agent, what percent would you anticipate prescribing the f"
  },
  {
    "figure_id": "F936",
    "report_id": "R071",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Q3. Among NEW patients initiating on a branded systemic agent, what percent would you anticipate prescribing the following:"
  },
  {
    "figure_id": "F937",
    "report_id": "R071",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: Dermatologists Suggest the Access Success Rate is 2:1, Albeit Early Days with Many Still in Process"
  },
  {
    "figure_id": "F938",
    "report_id": "R071",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: The 30-minute Fasting Post Dosing Has Overwhelmingly Not Been a Barrier"
  },
  {
    "figure_id": "F939",
    "report_id": "R071",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Efficacy and Oral Administration are the Top Drivers of Icotyde Prescribing"
  },
  {
    "figure_id": "F940",
    "report_id": "R071",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Efficacy and Oral Administration are the Top Drivers of Icotyde Prescribing ## Valuation and Risks Valuation: We arrive at our 12-month price target of \\$275 based on a 20x P/E multiple on our Q5-Q8 EPS."
  },
  {
    "figure_id": "F941",
    "report_id": "R072",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2: Flows Through the Strait of Hormuz Stand at $42\\%$ of Normal Levels (7-Day Moving Average) Oil exports are estimated by taking an average of S&P and Kpler data on the daily number of oil tankers crossing the Strait of"
  },
  {
    "figure_id": "F942",
    "report_id": "R072",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 926mb"
  },
  {
    "figure_id": "F943",
    "report_id": "R072",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 926mb Exhibit 4: Global Imports of Iranian Oil Have Edged Up Since the US Sanctions Waiver But Remain 0.8m"
  },
  {
    "figure_id": "F944",
    "report_id": "R072",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: We Estimate Gulf Crude Production Losses in June at Around 10.5mb/d"
  },
  {
    "figure_id": "F945",
    "report_id": "R072",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: We Estimate Gulf Crude Production Losses in June at Around 10.5mb/d"
  },
  {
    "figure_id": "F946",
    "report_id": "R072",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: Global Imports of Iranian Oil Have Edged Up Since the US Sanctions Waiver But Remain 0.8mb/d Below Year-Ago Levels Exhibit 5: We Estimate Gulf Crude Production Losses in June at Around 10.5mb/d Excludes Neutral Zone."
  },
  {
    "figure_id": "F947",
    "report_id": "R072",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Our Global Visible Stocks Counter Has Bottomed Mid-June and Now Stands Only 0.2mb/d Below Its Year-Ago Level"
  },
  {
    "figure_id": "F948",
    "report_id": "R072",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Our Global Visible Stocks Counter Has Bottomed Mid-June and Now Stands Only 0.2mb/d Below Its Year-Ago Level ## 3) Russia Runs and Flows Exhibit 8: Russia Total Refinery Outages Are 3.2mb/d Above Their Historical Seaso"
  },
  {
    "figure_id": "F949",
    "report_id": "R072",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 9: Russia Refinery Runs Have Declined by 2.0mb/d Since Year Ago Exhibit 10: Russia Retail Diesel/Gasoline Prices Have Increased by $12\\% / 10\\%$ Over the Last Two Months"
  },
  {
    "figure_id": "F950",
    "report_id": "R072",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: Russia Crude Exports Increased by 1.3mb/d Year-to-Date While Refined Products Exports Decreased by 0.8mb/d"
  },
  {
    "figure_id": "F951",
    "report_id": "R072",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Exhibit 12: Russia Net Exports of Crude/Condensate Are Up 1.7mb/d From Their Average Seasonal Level, While Net Exports of Refined Products Are Down 1.0mb/d Driven by Gasoil/Diesel"
  },
  {
    "figure_id": "F952",
    "report_id": "R072",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: Russia Retail Diesel/Gasoline Prices Have Increased by $12\\% / 10\\%$ Over the Last Two Months Exhibit 11: Russia Crude Exports Increased by 1.3mb/d Year-to-Date While Refined Products Exports Decreased by 0.8mb/d Exh"
  },
  {
    "figure_id": "F953",
    "report_id": "R072",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11: Russia Crude Exports Increased by 1.3mb/d Year-to-Date While Refined Products Exports Decreased by 0.8mb/d Exhibit 12: Russia Net Exports of Crude/Condensate Are Up 1.7mb/d From Their Average Seasonal Level, While Net"
  },
  {
    "figure_id": "F954",
    "report_id": "R073",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: We estimate FY26 compute capex by use case to inform our Azure estimates Exhibit 2: Our estimate of external vs. internal compute allocation ## 2) Capex and Internal Silicon"
  },
  {
    "figure_id": "F955",
    "report_id": "R073",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: We estimate FY26 compute capex by use case to inform our Azure estimates Exhibit 2: Our estimate of external vs. internal compute allocation ## 2) Capex and Internal Silicon On internal silicon: The near-term bear ca"
  },
  {
    "figure_id": "F956",
    "report_id": "R073",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: Hyperscalers' 2026/2027 capex estimates have increased by $36\\% / 55\\%$ since January AMZN, GOOGL, and META capex refers to additions to PP&E; MSFT capex includes fin leases ## What our forecasts imply for revenue/GW O"
  },
  {
    "figure_id": "F957",
    "report_id": "R073",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: We see a scenario where Microsoft pulls levers to realize steady or improving revenue/GW, which would drive upside to our estimates Exhibit 5: We estimate Microsoft will scale to \\~40 GW of capacity by mid 2030 ## 3)"
  },
  {
    "figure_id": "F958",
    "report_id": "R073",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: We see a scenario where Microsoft pulls levers to realize steady or improving revenue/GW, which would drive upside to our estimates Exhibit 5: We estimate Microsoft will scale to \\~40 GW of capacity by mid 2030 ## 3)"
  },
  {
    "figure_id": "F959",
    "report_id": "R074",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: Outdoor advertising has been the most resilient ‘traditional’ medium amid media share shifts... Change in ad market share, 2013-18 / 2018-23 / 2023-25 Exhibit 4: ...with OOH expected to grow \\~5% over 2026-31, driven b"
  },
  {
    "figure_id": "F960",
    "report_id": "R074",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: ...with OOH expected to grow \\~5% over 2026-31, driven by Digital OOH Global OOH advertising revenue growth, 2026-31 CAGR Based on WPP Media's half year 2026 forecasts Exhibit 5: There is a strong correlation between g"
  },
  {
    "figure_id": "F961",
    "report_id": "R074",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Exhibit 5: There is a strong correlation between global real GDP growth and global out-of-home advertising growth, with an R-squared of 0.78... Global out-of-home advertising growth vs. global real GDP growth correlation, 2005-25E"
  },
  {
    "figure_id": "F962",
    "report_id": "R074",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: ...implying broadly mid-single-digit global OOH growth going forward Global out-of-home advertising growth vs. global real GDP growth (\\%, yoy)"
  },
  {
    "figure_id": "F963",
    "report_id": "R074",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: ...implying broadly mid-single-digit global OOH growth going forward Global out-of-home advertising growth vs. global real GDP growth (\\%, yoy) ## Competitive environment remains supportive with recent M&A activity We"
  },
  {
    "figure_id": "F964",
    "report_id": "R074",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Exhibit 9: Gulf carriers are now operating at $\\sim -25\\%$ below pre-conflict capacity, an improvement from $\\sim -50\\%$ at the end of March Flights in key gulf hubs (7d-MA and daily data, %yoy) Data as of 9 June 2026 Exhibit 10:"
  },
  {
    "figure_id": "F965",
    "report_id": "R074",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Exhibit 10: Flight schedules for Middle East airlines have begun to recover, although the timing of a full recovery continues to be pushed back Latest and last weeks' schedules for EU - Middle East capacity (7d-MA, %yoy) Exhibit 1"
  },
  {
    "figure_id": "F966",
    "report_id": "R074",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 12: JCDecaux: Changes to estimates"
  },
  {
    "figure_id": "F967",
    "report_id": "R074",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "Exhibit 15: ...while we forecast JCDecaux's FCF generation returning to historical levels as capex normalises"
  },
  {
    "figure_id": "F968",
    "report_id": "R074",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Exhibit 15: ...while we forecast JCDecaux's FCF generation returning to historical levels as capex normalises JCDecaux FCF (€mn), 2014-30E ## Valuation and key risks"
  },
  {
    "figure_id": "F969",
    "report_id": "R074",
    "label": "Exhibit 14",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: JCDecaux's share price performance, LTM Indexed"
  },
  {
    "figure_id": "F970",
    "report_id": "R074",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: JCDecaux's share price performance, LTM Indexed Exhibit 17: JCDecaux's 12m fwd P/E, 2016-26 Exhibit 18: JCDecaux's 12m fwd EV/EBITDA, 2016-26"
  },
  {
    "figure_id": "F971",
    "report_id": "R074",
    "label": "Exhibit 16",
    "figure_type": "source_exhibit",
    "context": "Exhibit 16: JCDecaux's share price performance, LTM Indexed Exhibit 17: JCDecaux's 12m fwd P/E, 2016-26 Exhibit 18: JCDecaux's 12m fwd EV/EBITDA, 2016-26 Key risks include: (i) faster- or slower-than-expected recovery – driven"
  },
  {
    "figure_id": "F972",
    "report_id": "R074",
    "label": "Exhibit 17",
    "figure_type": "source_exhibit",
    "context": "Exhibit 17: JCDecaux's 12m fwd P/E, 2016-26 Exhibit 18: JCDecaux's 12m fwd EV/EBITDA, 2016-26 Key risks include: (i) faster- or slower-than-expected recovery – driven by better/worse GDP growth or stronger/weaker audience recove"
  },
  {
    "figure_id": "F973",
    "report_id": "R074",
    "label": "Exhibit 21",
    "figure_type": "source_exhibit",
    "context": "Exhibit 21: Stroeer: Changes to estimates Exhibit 22: We forecast Stroeer's group organic revenue growth at c.5% over the mid-term... Stroeer organic revenue growth by division, 2021-30E Exhibit 23: ...with gradual expansion in EB"
  },
  {
    "figure_id": "F974",
    "report_id": "R074",
    "label": "Exhibit 22",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: We expect JCDecaux to grow EBITDA at a \\~+5% 2026-30 CAGR vs. Stroeer \\~+4%"
  },
  {
    "figure_id": "F975",
    "report_id": "R074",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: We expect JCDecaux to grow EBITDA at a \\~+5% 2026-30 CAGR vs. Stroeer \\~+4% Exhibit 25: Stroeer's share price performance, LTM Indexed Exhibit 26: Stroeer's 12m fwd P/E, 2016-26"
  },
  {
    "figure_id": "F976",
    "report_id": "R074",
    "label": "Exhibit 24",
    "figure_type": "source_exhibit",
    "context": "Exhibit 24: We expect JCDecaux to grow EBITDA at a \\~+5% 2026-30 CAGR vs. Stroeer \\~+4% Exhibit 25: Stroeer's share price performance, LTM Indexed Exhibit 26: Stroeer's 12m fwd P/E, 2016-26 Exhibit 27: Stroeer's 12m fwd EV/EBI"
  },
  {
    "figure_id": "F977",
    "report_id": "R074",
    "label": "Exhibit 25",
    "figure_type": "source_exhibit",
    "context": "Exhibit 25: Stroeer's share price performance, LTM Indexed Exhibit 26: Stroeer's 12m fwd P/E, 2016-26 Exhibit 27: Stroeer's 12m fwd EV/EBITDA, 2016-26 Key risks to our view and price target include: (i) A better-than-expected"
  },
  {
    "figure_id": "F978",
    "report_id": "R074",
    "label": "Exhibit 26",
    "figure_type": "source_exhibit",
    "context": "Exhibit 26: Stroeer's 12m fwd P/E, 2016-26 Exhibit 27: Stroeer's 12m fwd EV/EBITDA, 2016-26 Key risks to our view and price target include: (i) A better-than-expected economic environment, which we would expect to drive a more p"
  },
  {
    "figure_id": "F979",
    "report_id": "R077",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: cRPO coverage ratio remains at historical levels Exhibit 2: Subscription revenue growth guidance reflects a moderated pace of organic deceleration ## 1. Core Workflows"
  },
  {
    "figure_id": "F980",
    "report_id": "R077",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Exhibit 1: cRPO coverage ratio remains at historical levels Exhibit 2: Subscription revenue growth guidance reflects a moderated pace of organic deceleration ## 1. Core Workflows We are constructive on ServiceNow's ability to l"
  },
  {
    "figure_id": "F981",
    "report_id": "R077",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Exhibit 4: ServiceNow subscription revenue by workflow based on market share gain ## 2. AI Adoption At Knowledge in May 2026, ServiceNow increased it's Now Assist ACV target to \\$1.5bn (up from \\$1bn prior and vs. \\$750mn+ of ACV"
  },
  {
    "figure_id": "F982",
    "report_id": "R077",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: GAAP EPS Analysis"
  },
  {
    "figure_id": "F983",
    "report_id": "R077",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Exhibit 6: GAAP EPS Analysis Exhibit 7: Large cap names across industries benchmark at mid 20s P/E and \\~1.5x P/E/G, vs. our discounted estimate of ServiceNow at 21x/0.67x ## Valuation and Key Risks We maintain our Buy rating."
  },
  {
    "figure_id": "F984",
    "report_id": "R077",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Exhibit 7: Large cap names across industries benchmark at mid 20s P/E and \\~1.5x P/E/G, vs. our discounted estimate of ServiceNow at 21x/0.67x ## Valuation and Key Risks We maintain our Buy rating. We reduce our 12-month price"
  },
  {
    "figure_id": "F985",
    "report_id": "R080",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 3: C2Q26 MCO passenger deplanements would increase $1\\%$ y/y v. GSe estimate for $+1\\%$ y/y increase in C2Q26 DIS reported domestic attendance growth, assuming June trends approximate the average of April and May MCO passen"
  },
  {
    "figure_id": "F986",
    "report_id": "R081",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: H share brokers declined by $3\\%$ on average since Guotai Haitong's result pre-announcement on July 3 Figure 3: A share brokers declined by $3\\%$ on average since Guotai Haitong's result pre-announcement on July 3"
  },
  {
    "figure_id": "F987",
    "report_id": "R081",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: H share brokers declined by $3\\%$ on average since Guotai Haitong's result pre-announcement on July 3 Figure 3: A share brokers declined by $3\\%$ on average since Guotai Haitong's result pre-announcement on July 3 Fi"
  },
  {
    "figure_id": "F988",
    "report_id": "R081",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 5: H share brokers were trading at 0.74x PB lately"
  },
  {
    "figure_id": "F989",
    "report_id": "R081",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: A share brokers declined by $3\\%$ on average since Guotai Haitong's result pre-announcement on July 3 Figure 4: A share brokers were trading at 1.15x PB lately Figure 5: H share brokers were trading at 0.74x PB latel"
  },
  {
    "figure_id": "F990",
    "report_id": "R081",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: A share brokers were trading at 1.15x PB lately Figure 5: H share brokers were trading at 0.74x PB lately ## Investment Thesis We have an OW rating on CMS-H. Our analysis suggests CMS is gaining market share in the b"
  },
  {
    "figure_id": "F991",
    "report_id": "R083",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Different providers on the same model of MiniMax M3 offer different API quality ## CSP & inference platform distribution: margin retention versus model quality"
  },
  {
    "figure_id": "F992",
    "report_id": "R083",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Different providers on the same model of MiniMax M3 offer different API quality ## CSP & inference platform distribution: margin retention versus model quality Open weights give overseas cloud and inference platfor"
  },
  {
    "figure_id": "F993",
    "report_id": "R083",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Different providers on the same model of MiniMax M3 offer different API quality ## CSP & inference platform distribution: margin retention versus model quality Open weights give overseas cloud and inference platfor"
  },
  {
    "figure_id": "F994",
    "report_id": "R088",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 1 Introduction As essential inputs for technologies including batteries, wind turbines, solar panels and semiconductors, critical raw materials (CRMs) are a strategic priority in European Union trade and industrial policy. Rising demand for these materials,"
  },
  {
    "figure_id": "F995",
    "report_id": "R088",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: CRM demand projections in three IEA scenarios Stated policies (STEPS) -- Net Zero emissions (NZE) Announced pledges (APS) □ STEPS–NZE range a) Growth of worldwide CRM demand relative"
  },
  {
    "figure_id": "F996",
    "report_id": "R088",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Main exporters of CRMs by production stage, 2024 Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024"
  },
  {
    "figure_id": "F997",
    "report_id": "R088",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Main exporters of CRMs by production stage, 2024 Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024"
  },
  {
    "figure_id": "F998",
    "report_id": "R088",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Main exporters of CRMs by production stage, 2024 Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024"
  },
  {
    "figure_id": "F999",
    "report_id": "R088",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024 Figure 5: EU shares of CRM exports by CRM and production stage, 2024"
  },
  {
    "figure_id": "F1000",
    "report_id": "R088",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024 Figure 5: EU shares of CRM exports by CRM and production stage, 2024"
  },
  {
    "figure_id": "F1001",
    "report_id": "R088",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024 Figure 5: EU shares of CRM exports by CRM and production stage, 2024 The EU's own extraction and processing capacity remains limited. The EU share of global e"
  },
  {
    "figure_id": "F1002",
    "report_id": "R088",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 5: EU shares of CRM exports by CRM and production stage, 2024 The EU's own extraction and processing capacity remains limited. The EU share of global extraction is negligible for most CRMs, lower than 10 percent, while it"
  },
  {
    "figure_id": "F1003",
    "report_id": "R088",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Alignment of strategic project allocation with demand and dependency Nickel Copper Cobalt Graphite Lithium REE"
  },
  {
    "figure_id": "F1004",
    "report_id": "R088",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Alignment of strategic project allocation with demand and dependency Nickel Copper Cobalt Graphite Lithium REE We then analyse the potential contribution of strategic projects to the CRMA targets by constructing projec"
  },
  {
    "figure_id": "F1005",
    "report_id": "R088",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Share of forecast 2030 demand potentially covered by strategic projects In July 2024, the EU and the European Bank for Reconstruction and Development signed an agreement on a new facility to provide equity investment f"
  },
  {
    "figure_id": "F1006",
    "report_id": "R088",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: EU strategic raw material partnerships To assess the effectiveness of EU CRM external policies (Figure 10), we empirically estimate the impact of EU strategic partnerships and bilateral agreements on CRM exports to the"
  },
  {
    "figure_id": "F1007",
    "report_id": "R088",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Estimation of the effects of EU CRM policies on CRM exports to the EU ## 4 Comparative approaches to CRM policy With the importance of CRMs only set to increase, other major economies, including Japan and the United St"
  },
  {
    "figure_id": "F1008",
    "report_id": "R088",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Japan and US CRM partnership networks a) Japan's critical mineral partnerships b) US critical mineral partnerships Thus, these economies are competing for inputs with the EU using building blocks: financial and admin"
  },
  {
    "figure_id": "F1009",
    "report_id": "R088",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Japan and US CRM partnership networks a) Japan's critical mineral partnerships b) US critical mineral partnerships Thus, these economies are competing for inputs with the EU using building blocks: financial and admin"
  },
  {
    "figure_id": "F1010",
    "report_id": "R089",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## RECENT ECONOMIC DEVELOPMENTS AND PROGRAM PERFORMANCE 3. The economic outlook remains positive but is subject to greater uncertainty due to the war in the Middle East. \\- Growth is expected to moderate to 6 percent in 2026 under the baseline, from 6.5 percen"
  },
  {
    "figure_id": "F1011",
    "report_id": "R089",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "3. The economic outlook remains positive but is subject to greater uncertainty due to the war in the Middle East. \\- Growth is expected to moderate to 6 percent in 2026 under the baseline, from 6.5 percent in 2025, reflecting weaker external demand amid the wa"
  },
  {
    "figure_id": "F1012",
    "report_id": "R089",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Sources: BCEAO and IMF staff calculations. \\- The current account deficit is now widening after reaching near balance in 2025. The current account deficit narrowed to 0.6 percent of GDP in 2025, supported by a record trade surplus due to both high export price"
  },
  {
    "figure_id": "F1013",
    "report_id": "R089",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "4. The authorities plan a modest relaxation of the fiscal deficit to enable a targeted and tailored policy response to the conflict. A successful reduction of the fiscal deficit to 3 percent of GDP was achieved in 2025, supported in part by additional measures"
  },
  {
    "figure_id": "F1014",
    "report_id": "R089",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "4. The authorities plan a modest relaxation of the fiscal deficit to enable a targeted and tailored policy response to the conflict. A successful reduction of the fiscal deficit to 3 percent of GDP was achieved in 2025, supported in part by additional measures"
  },
  {
    "figure_id": "F1015",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## ECONOMIC OUTLOOK AND RISKS 7. The medium-term outlook remains favorable. Growth is projected to average about 6.6 percent over the medium term, supported by strong household consumption and investment, as well as a further expansion of the hydrocarbon and m"
  },
  {
    "figure_id": "F1016",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "remains exposed to spillovers from increased insecurity in the Sahel region, which could be exacerbated by a prolonged commodity price shock. ## Figure 1. Côte d'Ivoire: Medium Term Outlook, 2022–31 GDP growth is expected to be supported by extractive industri"
  },
  {
    "figure_id": "F1017",
    "report_id": "R089",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "## A. Fiscal Policy: Maintaining Progress in Domestic Revenue Mobilization 9. Sustained effort will be needed to safeguard recent gains in revenue mobilization and ensure resilience to adverse conditions, while preserving space for priority spending in support"
  },
  {
    "figure_id": "F1018",
    "report_id": "R089",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "\\- 2025 budget outturn. Tax revenue increased by about 1 percent of GDP in 2025, meeting the end-December floor on tax revenue. While revenue was below the original 15 percent of GDP projection, largely due to higher-than-expected nominal GDP, nominal domestic"
  },
  {
    "figure_id": "F1019",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "completed in August 2023, found that the BCEAO continued to have well established audit arrangements and a strong control environment. Implementation of a priority recommendation, to align the BCEAO's Statute with the Cooperation Agreement of December 21, 2019"
  },
  {
    "figure_id": "F1020",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 21. Fund TA will continue to support Côte d'Ivoire's reform agenda beyond the program period. TA under the EFF/ECF-supported program has primarily focused on domestic revenue mobilization, although the authorities have not yet confirmed follow-up TA on corp"
  },
  {
    "figure_id": "F1021",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Côte d'Ivoire: Capacity to Repay the Fund A. Total Fund Credit Outstanding B. Total Debt Service to the Fund C. Largest Peaks"
  },
  {
    "figure_id": "F1022",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "5. Good progress was also made on the structural reform agenda. Revenue mobilization was supported by the adoption of a MTRS in 2024, which has anchored specific reforms including the rationalization of VAT exemptions and the shift to market valuation as the b"
  },
  {
    "figure_id": "F1023",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Tax Revenue and Overall Balance Annex I. Figure 1. Côte d'Ivoire: Key Achievements under the EFF/ECF and RSF (Percent of GDP unless otherwise indicated)"
  },
  {
    "figure_id": "F1024",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Tax Revenue and Overall Balance Annex I. Figure 1. Côte d'Ivoire: Key Achievements under the EFF/ECF and RSF (Percent of GDP unless otherwise indicated) Annex I. Figure 2. Côte d'Ivoire: RSF Reform Measures"
  },
  {
    "figure_id": "F1025",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Annex I. Figure 1. Côte d'Ivoire: Key Achievements under the EFF/ECF and RSF (Percent of GDP unless otherwise indicated) Annex I. Figure 2. Côte d'Ivoire: RSF Reform Measures"
  },
  {
    "figure_id": "F1026",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Annex I. Figure 2. Côte d'Ivoire: RSF Reform Measures ## Annex II. Debt Management Strategy"
  },
  {
    "figure_id": "F1027",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Annex I. Figure 2. Côte d'Ivoire: RSF Reform Measures ## Annex II. Debt Management Strategy The authorities' innovative and effective public debt management strategy has enabled Côte d'Ivoire to reduce its debt vulnerabilities and advance its development objec"
  },
  {
    "figure_id": "F1028",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "5. Recommended policy response. Against this backdrop, policy trade-offs are more binding. There are buffers to help cushion the impact of this adverse shock—regional reserve coverage is above 8 months as of end-April 2026 and the regional domestic debt market"
  },
  {
    "figure_id": "F1029",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Tax Revenue and Overall Balance Note: Overall balance, including grants, payment order basis Sources: Ivoirian authorities and IMF staff calculations."
  },
  {
    "figure_id": "F1030",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Tax Revenue and Overall Balance Note: Overall balance, including grants, payment order basis Sources: Ivoirian authorities and IMF staff calculations."
  },
  {
    "figure_id": "F1031",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Note: Overall balance, including grants, payment order basis Sources: Ivoirian authorities and IMF staff calculations. ## Annex V. Implementation of the Medium-Term Revenue Strategy"
  },
  {
    "figure_id": "F1032",
    "report_id": "R089",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "18. Given Côte d'Ivoire's continued access to international capital markets, a tailored stress test for market financing is applied. $^{8}$ Moody's raised the country's credit rating one notch to Ba2 in March 2024 (confirming it in March 2026), Standard and Po"
  },
  {
    "figure_id": "F1033",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "31. The authorities remain appropriately focused on strengthening resilience to debt sustainability risks. While the oil price shock is expected to lead to a temporary deterioration in fiscal balances in 2026–27, the authorities are committed to returning the "
  },
  {
    "figure_id": "F1034",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## AUTHORITIES' VIEWS 32. The authorities welcome the assessment of Côte d'Ivoire's public and external debt as being at low risk of debt distress. They view this upgrade as a testament to their sound and careful debt management and the tangible results of sus"
  },
  {
    "figure_id": "F1035",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "32. The authorities welcome the assessment of Côte d'Ivoire's public and external debt as being at low risk of debt distress. They view this upgrade as a testament to their sound and careful debt management and the tangible results of sustained fiscal consolid"
  },
  {
    "figure_id": "F1036",
    "report_id": "R089",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Côte d'Ivoire: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026–36 Figure 2. Côte d'Ivoire: Indicators of Public Debt Under Alternative Scenarios, 2026–36"
  },
  {
    "figure_id": "F1037",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Côte d'Ivoire: Indicators of Public Debt Under Alternative Scenarios, 2026–36 TOTAL public debt benchmark"
  },
  {
    "figure_id": "F1038",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Côte d'Ivoire: Indicators of Public Debt Under Alternative Scenarios, 2026–36 TOTAL public debt benchmark Most extreme shock 1/ Historical scenario"
  },
  {
    "figure_id": "F1039",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Côte d'Ivoire: Indicators of Public Debt Under Alternative Scenarios, 2026–36 TOTAL public debt benchmark Most extreme shock 1/ Historical scenario"
  },
  {
    "figure_id": "F1040",
    "report_id": "R089",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Côte d'Ivoire: Indicators of Public Debt Under Alternative Scenarios, 2026–36 TOTAL public debt benchmark Most extreme shock 1/ Historical scenario \\* Note: The public DSA allows for domestic financing to cover the additional financing needs generate"
  },
  {
    "figure_id": "F1041",
    "report_id": "R089",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ The most extreme stress test is the test that yields the highest ratio in or before 2036. The stress test with a one-off breach is also presented (if any), while the one-off breach is deemed"
  },
  {
    "figure_id": "F1042",
    "report_id": "R089",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Côte d'Ivoire: Drivers of Debt Dynamics – Baseline Scenario Gross Nominal PPG External Debt (In percent of GDP; DSA vintages) Debt-creating flows (Percent of GDP) Public Debt Unexpected Changes in Debt 1/ (past 5 years, percent of GDP) Gross Nomin"
  },
  {
    "figure_id": "F1043",
    "report_id": "R089",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Debt-creating flows (Percent of GDP) 1/ Difference between anticipated and actual contributions on debt ratios. Unexpected Changes in Debt 1/ (past 5 years, percent of GDP) 2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively l"
  },
  {
    "figure_id": "F1044",
    "report_id": "R089",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively low private external debt for average low-income countries, a ppt change in PPG external debt should be largely explained by the drivers of the external debt dynamics equatio"
  },
  {
    "figure_id": "F1045",
    "report_id": "R089",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Contribution to Real GDP Growth (Percent, 5-year average) ## Figure 4. Côte d'Ivoire: Realism Tools 3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 19"
  },
  {
    "figure_id": "F1046",
    "report_id": "R089",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is found on the horizontal axis; the percen"
  },
  {
    "figure_id": "F1047",
    "report_id": "R089",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is found on the horizontal axis; the percent of sample is found on the vertical axis. 1/ Bars refer to annu"
  },
  {
    "figure_id": "F1048",
    "report_id": "R089",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "1/ Bars refer to annual projected fiscal adjustment (right-hand side scale) and lines show possible real GDP growth paths under different fiscal multipliers (left-hand side scale). Public and Private Investment Rates (Percent of GDP) Figure 5. Côte d'Ivoire: M"
  },
  {
    "figure_id": "F1049",
    "report_id": "R089",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Côte d'Ivoire: Market-Financing Risk Indicators 1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections"
  },
  {
    "figure_id": "F1050",
    "report_id": "R089",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Côte d'Ivoire: Market-Financing Risk Indicators 1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections"
  },
  {
    "figure_id": "F1051",
    "report_id": "R089",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections."
  },
  {
    "figure_id": "F1052",
    "report_id": "R089",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections."
  },
  {
    "figure_id": "F1053",
    "report_id": "R089",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023"
  },
  {
    "figure_id": "F1054",
    "report_id": "R089",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023 (Percent of GDP, unless otherwise in"
  },
  {
    "figure_id": "F1055",
    "report_id": "R089",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023 (Percent of GDP, unless otherwise in"
  },
  {
    "figure_id": "F1056",
    "report_id": "R090",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Why Are We Talking about Gold in Central Bank Reserves Now? Gold $^{2}$ has been prominent in the balance sheets of many central banks largely because of the institutional and historical legacy of the gold-standard era and subsequent postwar monetary arrang"
  },
  {
    "figure_id": "F1057",
    "report_id": "R090",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The evidence from the most recent Reserve Advisory and Management Partnership (RAMP) survey $^{4}$ suggests that the expansion of gold holdings has not generally been guided by formal quantitative allocation frameworks. Most central banks report that the size "
  },
  {
    "figure_id": "F1058",
    "report_id": "R090",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The evidence from the most recent Reserve Advisory and Management Partnership (RAMP) survey $^{4}$ suggests that the expansion of gold holdings has not generally been guided by formal quantitative allocation frameworks. Most central banks report that the size "
  },
  {
    "figure_id": "F1059",
    "report_id": "R090",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Panel 1: countries that increased gold reserves Panel 2: countries that kept gold reserves unchanged Panel 3: countries that decreased gold reserves Panel 4: Gold producers vs. non-gold producers The distribution of gold purchases across countries further high"
  },
  {
    "figure_id": "F1060",
    "report_id": "R090",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Panel 2: countries that kept gold reserves unchanged Panel 3: countries that decreased gold reserves Panel 4: Gold producers vs. non-gold producers The distribution of gold purchases across countries further highlights that recent accumulation has been driven "
  },
  {
    "figure_id": "F1061",
    "report_id": "R090",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## The Enduring Appeal: A Deep and Liquid Global Market, No Credit Risk Gold's liquidity is evidenced by substantial trading volumes in major bullion markets. Its daily average trading volume in London is about \\$134 billion (Figure 3, panel 1, 2), providing c"
  },
  {
    "figure_id": "F1062",
    "report_id": "R090",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Daily Average Gold Market Trading Volume in London Panel 1: Daily volume in USD billions Panel 2: Daily volume in troy oz. millions Is gold a hedge, a diversifier, or a safe haven? Following Baur and Lucey (2010), we define a hedge as an asset that i"
  },
  {
    "figure_id": "F1063",
    "report_id": "R090",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Similarly, gold's correlation with US inflation surprises is predominantly negative, with the exception of the period between the end of the global financial crisis and the start of the COVID-19 pandemic. This suggests that gold does not provide a consistent h"
  },
  {
    "figure_id": "F1064",
    "report_id": "R090",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: Correlation between gold price (percent change) and assets/indices. 3-month and 10-year yields are derived from zero-coupon curves. 10-year US term premium is the Federal Reserve Bank of New York Adrian, Crump, and Moench (2013) Treasury premium. S&P 500"
  },
  {
    "figure_id": "F1065",
    "report_id": "R090",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: Correlation between gold price (percent change) and assets/indices. 3-month and 10-year yields are derived from zero-coupon curves. 10-year US term premium is the Federal Reserve Bank of New York Adrian, Crump, and Moench (2013) Treasury premium. S&P 500"
  },
  {
    "figure_id": "F1066",
    "report_id": "R090",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Panel 1: Gold Price (USD/oz) vs. VIX Panel 2: Gold Price (USD/oz) vs. Geopolitical Index Panel 3: Correlation between Gold Price, VIX, and Geopolitical Index Note: Figure 5, panel 3: correlation between gold price (percent change), VIX (change), and Geopolitic"
  },
  {
    "figure_id": "F1067",
    "report_id": "R090",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: Figure 5, panel 3: correlation between gold price (percent change), VIX (change), and Geopolitical Threat Index (change). VIX is the Chicago Board Options Exchange Volatility Index. Geopolitical index is from Caldara and Iacoviello (2021). Period definit"
  },
  {
    "figure_id": "F1068",
    "report_id": "R090",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Figure 6. Gold and Tail Risk Panel 1: Gold price distribution by VIX Note: VIX = Chicago Board Options Exchange Volatility Index. Panel 2: Gold price distribution by VIX Is gold a safe haven against tail risks? Kernel density estimations conditional on the "
  },
  {
    "figure_id": "F1069",
    "report_id": "R090",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Gold is an asset providing high returns while bearing significant market risk. Returns on gold, calculated as the change in gold price, are substantially higher than those of traditional reserve assets with long duration (Figure 7, panel 1), despite being an a"
  },
  {
    "figure_id": "F1070",
    "report_id": "R090",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## The Fading Promise: Gold as a Portfolio Risk Diversifier Gold can be a useful addition to reserves from the portfolio management perspective, although its diversification benefits vary with the duration of the portfolio and the prevailing regime. Regression"
  },
  {
    "figure_id": "F1071",
    "report_id": "R091",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "The methodology was developed in collaboration with Cindy Laura Stahl, a researcher at the University of St. Gallen. The scores across pillars are averaged to arrive at an overall metric. Applying our measure to a sample of publicly listed US companies, we cla"
  },
  {
    "figure_id": "F1072",
    "report_id": "R091",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "The AI adoption leaders in our sample are concentrated in the tech sector, but breakout performers exist across industries. More importantly, the TSR lift cannot be dismissed as a “shovel-seller” effect: the numbers we find are industry-adjusted, meaning that "
  },
  {
    "figure_id": "F1073",
    "report_id": "R091",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "AI Leaders Are Seeing a Productivity Dividend The productivity engine behind the value. Underlying this fundamental performance is a productivity advantage: revenue per employee is growing 4 percentage points faster at AI leaders than at laggards, on an indust"
  },
  {
    "figure_id": "F1074",
    "report_id": "R091",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "For CEOs, this raises an obvious question: How are these leaders deploying this productivity to create higher value than peers? # What AI Leaders Do: Save, Scale, Innovate We observe three distinct ways in which AI leaders create value, differentiated by wheth"
  },
  {
    "figure_id": "F1075",
    "report_id": "R091",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "## Becoming an AI Leader Save, scale, and innovate describe what leaders do with AI once they’ve reached the top. But how do they get there in the first place? To trace the journey, we examined how the three pillars of our score—AI tech, AI talent, and AI depl"
  },
  {
    "figure_id": "F1076",
    "report_id": "R092",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "## Canadians Are Spending More Than They Earn Across income tiers, Canadian households raised their spending by roughly the same proportion between 2021 and 2025: up 27% in the lowest band, 19% in the middle, and 24% at the top. (See Exhibit 1.) What separated"
  },
  {
    "figure_id": "F1077",
    "report_id": "R092",
    "label": "EXHIBIT 02",
    "figure_type": "source_exhibit",
    "context": "Top 20% ## EXHIBIT 02 ## Bottom 80% of Earners Sliding Deeper Into Negative Savings Average yearly household savings (\\$K, nominal) The middle 60% moved from a modest positive savings position to spending more than their income, a deterioration of roughly \\$7 "
  },
  {
    "figure_id": "F1078",
    "report_id": "R092",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "## Asset Gains Are Sustaining Spending, but Not Equally With household budgets under pressure, asset gains have enabled sustained spending across the top 80%. These cohorts saw total assets grow by 13% to 26%, helped by rising market valuations. (See Exhibit 3"
  },
  {
    "figure_id": "F1079",
    "report_id": "R092",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "## Borrowing Is Filling the Gap The last support is credit. When income lags and savings thin, households borrow to keep up. The middle 60% saw the fastest growth in liabilities, up 22%. (See Exhibit 4.) Asset gains have kept their net wealth positive on paper"
  },
  {
    "figure_id": "F1080",
    "report_id": "R092",
    "label": "EXHIBIT 04",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 04 ## All Households Leaning on Debt But Lowest 20% Most Underwater The lowest-income band added 17% to its liabilities against a shrinking asset base, cutting net wealth by roughly \\$35 thousand per household. Together, the data point to a growing "
  },
  {
    "figure_id": "F1081",
    "report_id": "R093",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "There is a demographic aspect to that growth: millennials prefer discounters over mainstream grocers in most markets. In large developed markets (including the US, Europe, Australia, Canada, and Japan), this population comprises 275 million people, more than a"
  },
  {
    "figure_id": "F1082",
    "report_id": "R093",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "\\- Nascent. In these markets, discounters have yet to establish a serious presence; they typically have market shares of less than 15%. And some of these markets—including in the US, Sweden, and Australia—are still essentially white spaces. They present an opp"
  },
  {
    "figure_id": "F1083",
    "report_id": "R094",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "be on eliminating waste and reinvesting the savings in the form of lower prices or improved service. To pursue E2E product excellence, grocers should adopt several key measures. Set ambitious goals. To pursue and maintain E2E process excellence, leaders need t"
  },
  {
    "figure_id": "F1084",
    "report_id": "R094",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "day or week—leaders can celebrate progress with their teams at regular intervals, building enthusiasm, instilling the right behaviors, and giving management a handy way to monitor progress. \\- Team Engagement. To build team engagement, grocers need to articula"
  },
  {
    "figure_id": "F1085",
    "report_id": "R094",
    "label": "EXHIBIT 3",
    "figure_type": "source_exhibit",
    "context": "Note: A zone is an area that consists of approximately five to eight groups of six to eight stores each. $^{1}$ The duration of the batch-by-batch rollout depends on the size of the store network. # WHAT GAMIFIED TRAINING LOOKS LIKE MANY GROCERS ARE planning t"
  },
  {
    "figure_id": "F1086",
    "report_id": "R095",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "Define a clear vision and strategy. The leadership team needs to establish the aspiration for how the private-label business will fit into the organization and—more important—into the overall brand architecture. Grocers can choose from three models: \\- The fir"
  }
]