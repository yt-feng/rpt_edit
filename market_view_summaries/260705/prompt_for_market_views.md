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
  "战略咨询": 3,
  "智库/国际机构": 0
}

报告摘要：
[
  {
    "id": "R001",
    "title": "波士顿咨询：波士顿咨询揭示AI就业悖论，软件工程师反而因AI需求增长",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：波士顿咨询揭示AI就业悖论，软件工程师反而因AI需求增长\n\n未来两到三年，美国50%到55%的岗位将被AI重塑。这个数字来自波士顿咨询（BCG）旗下Henderson Institute最新发布的研报。但真正值得关注的不是这个比例本身，而是它背后的判断：AI对就业的影响，不是简单的“替代”与“被替代”的二选一，而是一场关于岗位定义、工作方式和价值分配的系统性重构。这份报告基于微观经济模型，将AI对劳动力市场的影响拆解为替代、增强和需求扩张三种力量，并给出了一个对CEO们极具操作性的框架。它提醒我们，那些急于裁员以换取短期效率的公司，很可能正在为竞争对手铺路。\n\n**KC评论：** 这份报告的核心洞察在于，它把AI对就业的影响从“有多少岗位会消失”这个焦虑问题，转向了“哪些岗位会被重新定义，以及企业如何管理这种转变”。对于决策者来说，这是一个更具建设性的视角。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 近六成岗位的自动化潜力低于平均水平，AI不会成为“万能替代者”\n\n报告首先计算了美国所有岗位的平均任务自动化潜力——40%。这意味着，如果一个岗位中超过40%的任务可以被当前AI能力自动化，那么它才进入需要重点关注的区间。而结果令人意外：57%的岗位自动化潜力低于这个阈值。这些岗位高度依赖人类的身体在场、动手操作或持续的人际互动，AI对它们的颠覆性影响有限。这包括大量需要物理接触的医疗护理、需要现场判断的维修技工、以及依赖情感共鸣的咨询顾问等。\n\n**KC评论：** 这一结论直接反驳了“AI将取代一切白领工作”的极端叙事。报告通过任务层面的微观分析，揭示了一个关键事实：许多看似“知识密集”的工作，其核心价值恰恰在于那些难以被结构化、需要人类判断和情感投入的部分。对于企业而言，这意味着在考虑AI部署时，首先\n\n[... middle omitted ...]\n\n对冲基金、资管机构、战略咨询和智库的朋友，我们期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI不会抢走你的工作，但会重塑它\n\n**重塑而非替代**\n\n未来2-3年，美国50%-55%的工作将被AI重塑\n\n---\n\n最近读到某外资投行的一份研报，讲AI对就业的影响。结论比我想象的乐观很多，分享几个核心逻辑：\n\n1️⃣ **AI更多是“增强”而非“替代”**\n- 未来2-3年，50%-55%的工作会被AI重塑\n- 但5年内真正被替代的工作只有10%-15%\n- 大部分人会保留岗位，只是工作方式彻底变了\n\n2️⃣ **为什么不是大规模失业？**\n关键看两个变量：\n- **替代vs增强**：像客服这种结构化工作容易被替代；软件工程师需要系统判断力，AI只是辅助工具\n- **需求弹性**：AI降低生产成本后，如果需求会扩大（比如软件需求永远不够），岗位反而可能增加\n\n3️⃣ **最有趣的发现：**\n- 43%的工作任务自动化潜力超过40%\n- 但真正被替代的岗位集中在“结构化+低人际互动”的类型\n- 需要物理在场、复杂人际判断的工作反而更安全\n\n4️⃣ **给管理者的建议**\n- 别急着裁员：AI替代不了那么多岗位时裁员，只会损失人才\n- 先做增强再做替代：否则员工会抵触变革\n- 重点投资技能提升：让员工学\n\n[... middle omitted ...]\n\near vision for how the transformation is managed, including a scaled, strategic approach to upskilling and reskilling and the restructuring of career ladders.\n\nThis shift is already happening—\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R002",
    "title": "麦肯锡：私募股权已经驶入更硬的地面，不是所有车都能开过去",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "麦肯锡",
    "digest": "[wechat_article.md]\n# 麦肯锡：私募股权已经驶入更硬的地面，不是所有车都能开过去\n\n2025年，全球私募股权市场的交易总价值突破1万亿美元，创下历史新高。单笔超过5亿美元的大型交易激增44%，史上最大一笔PE私有化交易——550亿美元收购Electronic Arts——在这一年落地。退出端同样火爆，IPO退出交易量几乎翻倍。\n\n但这份麦肯锡《2026全球私募市场报告》给出的核心判断，与这些数字传递的乐观情绪截然不同：**雾散了，但地面变硬了。** 过去几年被视作“周期性调整”的种种困难——交易数量下降、持有期拉长、回报率低迷、LP流动性枯竭——正在成为这个行业的结构性特征。2025年的交易额反弹，更像是暴风雨后的一次集中释放，而非趋势反转。\n\n对于GP和LP而言，真正的考验才刚刚开始。当廉价杠杆和多重扩张不再提供免费推力，当超过16000家公司被持有超过四年、历史最高，当DPI占AUM的比例跌至10%的历史最低点——私募股权已经从一个靠“上车”就能赚钱的行业，变成了一个需要真正驾驶技术的赛场。\n\n这份报告的价值，不在于它描述了2025年发生了什么，而在于它提供了一个清晰的判断框架：什么样的GP能在新地形上继续前进，什么样的GP注定要掉队。\n\n> **KC评论：** 麦肯锡的这份报告是2026年全球私募市场最值得精读的年度文件之一。它不只是数据堆砌，而是提供了一个完整的分析框架：从交易、运营、融资到LP分配，每个环节都给出了可操作的方向。但单篇报告只能覆盖顶层逻辑，每天的国际信源汇编会把当天全球投行、咨询公司和国际机构的报告整理成中文摘要、KC评论和图表合集，适合喂给AI追问，也适合人工快速扫描市场变化。扫码加入知识星球，每天获取一手国际信源。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 2025年的交易狂欢掩盖了一个事实：交易数量在下降\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n雾散了，路变硬了\n\n看清了，更难走了\n\n2026全球私募市场，玩法已经变了\n\n---\n\n1️⃣ 2025年发生了什么？\n- 大额交易（5亿美金以上）涨了44%，总额破万亿，超过2021年\n- 但中小型buyout数量反而下降了5%，北美最明显\n- 退出回暖，IPO退出量翻倍，但持有期还在拉长\n\n2️⃣ 最扎心的数字\n- 16,000+公司被持有超4年，历史最高\n- 52%的portfolio公司属于“超期服役”\n- 平均持有期已超6.5年\n- LP的DPI（现金回款）占AUM仅6%，而2015-19年平均是16%\n\n3️⃣ 赚钱逻辑变了\n- 过去靠杠杆+估值扩张（贡献59%回报）\n- 未来靠运营创造价值（operational alpha）\n- 买贵了？没关系，但得有能力改好公司\n\n4️⃣ AI开始“真干活”\n- 目前只有6%的GP觉得AI影响大\n- 但70%的人觉得3-5年内会翻天覆地\n- 不是噱头，是加速器和放大镜\n\n5️⃣ 谁在赢？\n- 超50亿美金的大基金占比越来越大\n- 小而美的基金份额在缩水\n- specialist（专注特定赛道）比generalist表现更好\n- 半流动性产品募资翻倍到2040\n\n[... middle omitted ...]\n\nrove most effective? And when—at long last—would the fog begin to clear?\n\nNow, in 2026, the fog has burned off. A harder terrain has revealed itself: What had been a smooth surface for years h\n\n[... middle omitted ...]\n\n credits\n\nCover and page 2: © Twenty47studio/Getty Images\nPage 3: © Serhii Prystupa/Getty Images\nPage 35: © Jose A. Bernat Bacete/Getty Images\nPage 55: © SW Photography/Getty Images\nPage 67: © Franckreporter/Getty Images"
  },
  {
    "id": "R003",
    "title": "麦肯锡：麦肯锡2025技术趋势，AI不是主角，而是激活其他技术的引擎",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "麦肯锡",
    "digest": "[wechat_article.md]\n# 麦肯锡：麦肯锡2025技术趋势，AI不是主角，而是激活其他技术的引擎\n\n如果你只打算读一份关于2025年技术趋势的报告，麦肯锡全球研究院（MGI）刚刚发布的第五版年度《技术趋势展望》可能是最值得花时间的一份。它不追逐热点，不制造焦虑，而是用一套严谨的量化框架——专利、研究、新闻、搜索、股权投资、人才需求六个维度——对13项前沿技术做了全景扫描。\n\n这份报告最值得看的判断是什么？不是AI本身有多强，而是AI正在成为其他所有技术的“激活器”。换句话说，2025年的技术叙事不再是一个个孤立的赛道，而是一张由AI串联起来的、相互赋能的网络。工厂里的机械臂、医院里的个性化药物、偏远风电场的维护，背后都是AI+机器人、AI+生物工程、AI+沉浸式现实的组合拳。\n\n报告给出了一个清晰的信号：技术投资在经历了2023年的整体回调后，2024年已经出现明显反弹。13个趋势中有10个的股权投资在2024年实现增长。但更值得关注的不是总量，而是结构——哪些技术获得了“超额”关注，哪些技术正在从实验室走向商业场景，以及哪些技术组合正在催生新的商业范式。\n\n以下是这份报告的核心洞察，以及它们对企业决策者的含义。\n\n> **KC评论：** 麦肯锡这份报告的价值不在于告诉你“AI很重要”——这已经是共识。它真正有用的地方，是用数据告诉你：AI正在如何改变其他技术的商业化节奏和投资回报预期。如果你只看AI本身，可能会错过更大的机会——那些被AI激活的、原本增长缓慢但壁垒极高的技术领域。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 最值得关注的不是AI本身，而是“Agentic AI”的爆发式增长\n\n报告首次将“Agentic AI”单独列为一项趋势。这不是概念炒作，而是有数据支撑的。2024年，Agentic AI的股权投资达到11亿美\n\n[... middle omitted ...]\n\ne fund、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2025科技趋势，这13个方向值得看\n\n**13个前沿方向**\n\n今年麦肯锡继续追踪13个改变商业格局的前沿科技趋势，分成三组：\n\n**AI革命组**\n1. 智能体AI（Agentic AI）— 2024年股权投资1.1亿美元，岗位增长985%\n2. 人工智能（含生成式AI）\n\n**算力与连接组**\n3. 专用半导体\n4. 先进连接技术\n5. 云与边缘计算\n6. 沉浸式现实\n7. 数字信任与网络安全\n8. 量子技术\n\n**前沿工程组**\n9. 机器人未来\n10. 移动出行未来\n11. 生物工程未来\n12. 太空技术未来\n13. 能源与可持续发展技术\n\n**几个有意思的发现**\n\n1. **AI是放大器，不是孤岛**。它加速机器人训练、推动生物工程发现、优化能源系统，跟其他趋势组合才产生最大价值。\n\n2. **自主系统从试点走向实用**。机器人+数字代理开始学习、适应、协作，不只是执行任务。\n\n3. **人机关系在演变**。从替代转向增强，技术更懂人的意图，边界越来越模糊。\n\n4. **规模化是硬仗**。数据中心电力、供应链延迟、人才短缺、政策摩擦…技术之外的真实世界挑战。\n\n5. **大国科技竞赛加剧**。各\n\n[... middle omitted ...]\n\ng)\n\nCompute and connectivity frontiers 26\n03 Application-specific semiconductors 27\n04 Advanced connectivity 34\n05 Cloud and edge computing 41\n06 Immersive-reality technologies 48\n07 Digital t\n\n[... middle omitted ...]\n\nock the investment and coordination required to scale next-generation energy technologies while maintaining affordability and reliability?\n\n![](images/8d8b8ab4e0f252bf0b1a8762dd24679e26276db08f1ecd44793275fca56533c7.jpg)"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Over the next two to three years, 50% to 55% of jobs in the US will be reshaped by AI. For many employees, this will mean that they retain the same or a similar role but face radically new expectations for how they work and what they produce. For company leade"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "# Task Automation Doesn’t Have to Mean Job Loss ## EXHIBIT 2 Agentic AI May Drive High Levels of Task Automation in 43% of Jobs Sources: Revelio Labs; O\\*NET; US Bureau of Labor Statistics; BCG Henderson Institute analysis. Substitution Versus Augmentation. To"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "This dynamic is not new. Economists have long observed that efficiency improvements can increase total consumption rather than reduce it, a phenomenon often referred to as Jevons Paradox. When the cost of a resource falls, usage can rise. The same logic applie"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Call center representatives illustrate bounded demand. The volume of inbound interactions is largely determined by the size of the customer base and the frequency of service needs. When AI reduces the cost of handling routine inquiries, the number of interacti"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Third, skill thresholds will rise. Redesigned roles will demand that employees demonstrate greater expertise, oversight, and accountability, increasing the premium on domain knowledge and sound judgment. As Exhibit 7 illustrates, the more durable roles tend to"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Scaling agentic systems requires specialized integration talent, including forward-deployed engineers, systems integrators, and project managers who tailor systems to enterprise-specific contexts. These technical experts are embedded directly with business tea"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：波士顿咨询揭示AI就业悖论，软件工程师反而因AI需求增长｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "A look at larger deals, a critical metric in assessing overall industry health, is revealing. For buyout and growth deals larger than \\$500 million, 2025 was a record year, increasing 44 percent versus 2024 to \\$1.1 trillion, higher than 2021's previous peak. "
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Geographical perspective sharpens the picture. In North America, buyout deal value increased 29 percent, accounting for 57 percent of total global buyout deal value (Exhibit 2). Europe also saw an increase (8 percent), but APAC declined (3 percent). This type "
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "1. Bigger deals are back: Deployment pressure is combining with buyers paying more for quality. The rebound in deal value occurred because acquirers are paying more, rather than doing more deals. The median EBITDA multiples that buyout firms paid reached a rec"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "That imperative is becoming more acute because buyout sizes are rising without a corresponding increase in leverage. Even as financing costs have eased, buyers are contributing more equity in absolute terms. $^{2}$ This means GPs can rely even less on leverage"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "The 98 percent increase in IPO exit value was nearly all due to larger (above \\$2.5 billion) IPOs, which grew 148 percent, from \\$98 billion in 2024 to \\$246 billion in 2025. The year 2025 was also the second-highest year on record among large (more than \\$2.5"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "LPs demand more than paper returns. Their understandable imperative is causing LPs and GPs alike to turn to a full suite of liquidity solutions, such as partial realizations and a more robust secondaries market. ## Exhibit 6 The difference between median valua"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Analysis by StepStone Group indicates that, for deals done between 2010 and 2022, leverage and multiple expansion comprised 59 percent of returns. The remaining 41 percent came from revenue growth and EBITDA margin expansion net of dividends and debt paydown ("
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "When looking at regions, fundraising in the largest and most mature market, North America, increased in 2025. North American fundraising in closed-end structures rose 8 percent. In contrast, Europe fell 41 percent, and APAC declined 49 percent to \\$49 billion."
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Precise values for nontraditional PE fundraising are hard to come by. One helpful proxy is to look at the broader private capital AUM reported by GPs. By that measure, AUM across all alternative forms of capital grew approximately 10 to 15 percent year on year"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Growth in these channels is likely to increase. Our survey of more than 1,300 financial advisors in the United States showed that they expect retail investors to increase allocations to private markets. For example, 42 percent of registered investment advisors"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Scale has become an increasingly important advantage. Larger buyout and growth platforms have again benefited disproportionately, often at the expense of the smallest managers. In 2020, funds smaller than \\$500 million raised \\$79 billion (17 percent of total "
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 11",
    "figure_type": "source_exhibit",
    "context": "Exhibit 11 Larger managers continued to account for a greater share of capital raised in 2025, compared with their smaller counterparts. Global buyout and growth fundraising $^{1}$ $^{1}$ Excludes secondaries, funds of funds, turnaround private equity funds, p"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "## 1. Recent public-market outperformance has overshadowed muted PE returns. PE returns have not only trended downward over time; they appear to be at a historic low. Buyout fund IRRs reached a post-2002 trough between 2022 and 2025, averaging 5.7 percent on a"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Recent buyout performance shows how longer holding periods are weighing on returns. From January 2022 through September 2025, buyout funds generated average returns of about Exhibit 13 Five-year rolling distribution to paid-in capital as a share of assets unde"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Exhibit 14",
    "figure_type": "source_exhibit",
    "context": "Why? The same survey revealed that 77 percent of LPs indicated that they planned to either maintain or increase their allocation to buyouts over the next three years, driven mainly by expected increases in returns and better comparable performance than other a"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Class A assets (where deal volumes grew 34 percent year over year in the United States). Lower-quality segments continue to face distress amid concerns about structural obsolescence (such as outdated layouts or weaker amenities) and difficulty in conversion to"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "in process and gradual, as evidenced by moderating appraisal uncertainty in private markets (reflected in transaction amounts and deal volumes) and continued discounts to net asset value (NAV) in public markets (at a median of 18 percent). $^{3}$ These dynamic"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "After sharp drawdowns in 2023 and an uneven recovery in 2024, returns turned modestly positive in 2025 across most real estate strategies. Debt and core-plus categories led the rebound (with 4.8 percent and 1.5 percent annual returns, respectively), while oppo"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "## AI: Accelerating from pilot to production Generative AI is catalyzing value creation across the real estate ecosystem. Agentic AI represents the next wave, enabling a more effective partnership between humans and autonomous AI systems, deploying human judgm"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "\\$10 billion in secured and convertible debt within six months. The investment thesis, therefore, is no longer simply exposure to data centers (and capitalization of demand), but advantages in power access, tenant mix, capital structure, and geographic positio"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "This trend of growing interest in specialized residential segments is reflected outside of the United States, as well. For example, although more nascent, demand for senior housing is emerging in the Middle East due to rising life expectancy, increasing preval"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Leading capital allocators are acquiring embedded property management, property development, and asset-level execution capabilities. ## Exhibit 7 Real estate funds above \\$5 billion have offered a greater degree of downside protection and lower performance dis"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "LPs are increasingly seeking to capture the benefits of scale. One primary enabler is to streamline their GP roster; 17 percent of institutions expect to decrease the number of managers in their rosters (in the short term), continuing a steady, multiyear trend"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Within global infrastructure deal activity, traditionally real estate–focused sectors (such as data centers, student housing, and logistics) have increased their share of total infrastructure volume in recent years (25 percent in 2025) (Exhibit 9). Importantly"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Compared with total global infrastructure needs through 2040 (where the energy and digital sectors account for about 40 percent of the \\$106 trillion needed), the composition of recent deal value shows an outsize presence of private capital in these infrastruc"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Deconstructing 2025 data, we can observe that fundraising dipped in the Asia-Pacific regions but grew robustly in Europe, rising by approximately 65 percent. In North America, it increased by approximately 285 percent (Exhibit 2). And in both Europe and North "
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "## LPs increase allocations LPs are increasingly including infrastructure investments in their core strategies. Indeed, in McKinsey's recent survey of approximately 300 global LPs, we found that 51 percent of respondents plan to raise their allocations to infr"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "There are strong indications that the infrastructure industry is maturing. Those markers include levels of dry powder—which are moderating—and an increasing willingness by GPs to deploy more capital and strategically pivot toward bigger, more sophisticated tra"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "McKinsey & Company ## Exhibit 5 LPs increasingly prefer value-added strategy in infrastructure. Target asset allocation expectations, $^{1}$ 2026 Value added is the most prominent asset class LPs intend to increase allocation to, with 56% of LPs indicating the"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "McKinsey & Company ## Exhibit 6 Fundraising for core plus and value-added strategies grew the fastest over the past several years. ## Dry powder moderates In recent decades, LPs' demand for infrastructure has outpaced deal supply, contributing to fund fragment"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "## Bigger, more innovative deals GPs are not only deploying more capital, they are concentrating more of it on big deals. As the market matures, total deal value in 2025 rose by 23 percent (even as deal count declined by about 24 percent), and average deal siz"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "## Exhibit 7 Infrastructure is entering a moderate growth phase, with declining dry powder leading to healthier deployed-to-uncalled capital ratio. McKinsey & Company Dry powder as % of assets under management sponsors over the past few years to commit to mult"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "Deal theses are broadening across key dimensions: up the risk spectrum (driven by LP demand), into intersections between infrastructure verticals, and into infrastructure services. That dynamic is consistent with the expanding conception of what “infrastructur"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "Yet as infrastructure evolves from traditional assets to more complex, intersecting verticals, challenges will mount as holding periods lengthen. Capital cycles in infrastructure investing are already trending longer, characterized by more measured exit activi"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Comprehensive data on private credit deal volumes across strategies and geographies is limited by the opaque nature of activity in the sector. Even so, the segment with the clearest disclosure—direct lending—suggests the market’s direction. Direct lending volu"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Exhibit 2 First lien spread per unit of leverage has declined since 2022. Global private credit first lien New-issue median leverage, turns McKinsey & Company ## Fundraisers: The evolution of capital formation"
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Global private credit first lien New-issue median leverage, turns McKinsey & Company ## Fundraisers: The evolution of capital formation By traditional fundraising metrics, private credit softened in 2025: closed-end fundraising fell 16 percent year over year t"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Fundraising trends for closed-end funds varied meaningfully by strategy. Direct lending funds fell 28 percent, $^{15}$ likely driven in part by the strategy's prevalence in open-end-fund structures, as well as by a shift in investor preferences away from a mor"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "## Exhibit 4 Private credit fundraising for closed-end funds in 2025 continued to trend toward concentration. McKinsey & Company capital continued to accelerate in the first quarter of 2026 and is shaping up to be one of the prime tests for the asset class ove"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "麦肯锡视觉摘要 1",
    "figure_type": "external_card",
    "context": "麦肯锡｜麦肯锡：私募股权已经驶入更硬的地面，不是所有车都能开过去｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "## Wind farm maintenance crew Energy and sustainability Wind farms need to maintain peak efficiency year-round, maximizing clean-energy output while minimizing downtime and operational costs Immersive reality Technicians use augmented reality goggles that prov"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Immersive reality Technicians use augmented reality goggles that provide visual guidance to help them maintain and repair complex turbine systems safely Advanced connectivity Low-Earth-orbit satellites provide technicians with access to real-time data and clou"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "McKinsey & Company Note: Data includes private-market and public-market capital raises across venture capital and corporate and strategic M&A (including joint ventures), private equity investments (including buyouts and private investment in public equity), an"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "This report lays out considerations for all 13 technology trends. For easier consideration of related trends, we grouped them into three broader categories: the AI revolution, compute and connectivity frontiers, and cutting-edge engineering. Of course, there's"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "麦肯锡视觉摘要 1",
    "figure_type": "external_card",
    "context": "麦肯锡｜麦肯锡：麦肯锡2025技术趋势，AI不是主角，而是激活其他技术的引擎｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]