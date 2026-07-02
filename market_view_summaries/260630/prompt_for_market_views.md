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
    "title": "HSBC：油价下跌不是万灵药，全球经济的“暗流”才真正决定胜负",
    "digest": "[wechat_article.md]\n# HSBC：油价下跌不是万灵药，全球经济的“暗流”才真正决定胜负\n\n油价跌了。布伦特原油从冲突高峰回落至每桶80美元附近，霍尔木兹海峡在停火协议延长后逐步恢复通航。市场松了一口气，政策制定者也面露宽慰之色。\n\n但HSBC全球首席经济学家Janet Henry团队在最新发布的《Crosscurrents》报告中明确指出：油价回落只是消除了最坏情景，全球经济真正的胜负手，藏在三条彼此对冲的“暗流”之中——人工智能投资的狂热、厄尔尼诺对粮食供给的威胁，以及各国财政与货币政策的分道扬镳。\n\n这不是一份“油价跌了，全球就安全了”的报告。恰恰相反，它告诉我们：即便地缘风险暂时缓解，2026-2027年的全球经济仍将是一个高度分化的世界——有人受益，有人承压，而大多数决策者面临的挑战远未结束。\n\n以下是我们从这份报告中提炼出的核心判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油价下跌只解了近忧，远虑在于三条“暗流”正在重塑全球增长格局\n\nHSBC维持2026年全球GDP增速2.5%的预测不变——这是自疫情以来最慢的一年。2027年2.7%的预测也未被上调。表面看，油价回落似乎没有改变大局，但数字背后的“成分”发生了剧烈变化。\n\n最显著的上调发生在美国：2027年GDP增速从2.0%上调至2.3%。最大的下调则落在印度（从6.8%降至6.4%）和巴西（从2.2%降至1.7%）。欧洲同样被大幅下修：欧元区2026年增速从0.7%腰斩至0.3%。\n\n为什么？因为油价只是“明流”，真正驱动这些修正的是三条暗流：\n\n第一，AI相关的出口与投资热潮正在制造巨大的国别分化。台湾地区2026年GDP增速被上调至惊人的10.2%，直接受益于AI芯片与半导体生态的持续扩张。美国同样受益，其AI投资带来的财富效应和资本支出正在对冲能源冲击\n\n[... middle omitted ...]\n\n、厄尔尼诺影响或全球利率分化，欢迎来我们的微信群里继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价降温，但别急着松口气\n\n🌍 全球经济暗流涌动\n\n油价从高点回落，布伦特跌到80美元附近，但全球经济并没有因此平静。某外资投行最新研报指出，影响2026-27年增长的力量远不止能源价格——AI投资潮、厄尔尼诺冲击、各国财政分化，都在同时发力。\n\n1️⃣ 消费：分化加剧\n- 美国消费者靠退税和科技股财富效应撑着，韧性还在\n- 中国家庭受地产拖累，消费偏弱\n- 全球实际工资承压+信贷收紧，未来几个季度消费可能继续降温\n\n2️⃣ 食品通胀：新风险浮现\n柴油和化肥涨价已影响亚洲农业产出，更大的威胁来自厄尔尼诺。下半年到2027年，印度、巴西等新兴市场食品价格可能明显上涨，连发达国家也躲不开进口成本上升。\n\n3️⃣ AI：爆发但分布不均\n- 台湾和美国是AI投资最大受益者，出口和GDP继续被拉动\n- 但AI建设本身推高铜、芯片等成本，苹果CEO库克6月已表示组件涨价“不可避免”\n- 需求侧通胀压力可能比供给侧的效率提升来得更快\n\n4️⃣ 央行路径分化\n- 油价回落让欧洲央行和英国央行暂停加息，2027年可能降息\n- 但多个亚洲经济体下半年仍有加息压力\n- 美元在能源冲击中走强，预计还会继续\n\n5️⃣ 两个场景\n- 基\n\n[... middle omitted ...]\n\n be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.\n\n# Executive summary\n\n## Ceasefire extended, lower oil\n\n[... middle omitted ...]\n\n5f9e3e72a4d1aaadf6b0217a6.jpg)\n\nNewsletters Subscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points"
  },
  {
    "id": "R002",
    "title": "NOM：全球资金流向正在发出一个被忽视的信号",
    "digest": "[wechat_article.md]\n# NOM：全球资金流向正在发出一个被忽视的信号\n\n全球资金流向正在经历一次微妙但值得警惕的切换。NOM最新一期高频资金流监测数据揭示了一个关键事实：涌入美国股票基金的外资规模在6月下旬骤然减速，从上一周的39亿美元骤降至14亿美元，降幅超过60%。与此同时，新兴市场基金却保持了稳定的资金流入。\n\n这不是一个孤立的数据波动。它可能标志着全球投资者风险偏好的结构性再平衡，以及AI主题从普涨到分化的临界点。对于正在评估下半年资产配置的决策者而言，这份周度报告提供了一个不可忽视的早期信号。\n\nNOM亚洲外汇策略团队在6月最后一周发布的这份报告中，没有给出任何方向性判断。但数据本身就在说话。\n\n> **KC评论：** NOM的这份报告没有结论，但数据层面的减速信号非常清晰。完整报告包含了从月度、周度到日度的多层次资金流图表，以及韩国、台湾等关键市场的零售资金拆解。这些细颗粒度的数据，往往比一个简单的“买入/卖出”评级更能揭示市场情绪的边际变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国股票基金的资金流入正在快速降温，但并非撤离\n\nNOM数据显示，6月19日至25日当周，海外资金流入美国股票基金（ETF和共同基金）的规模为14亿美元，较前一周的39亿美元显著收窄。这是连续第二周流入规模从高位回落。\n\n然而，从月度数据看，6月至今（截至25日）的累计流入仍高达115亿美元，高于5月的88亿美元和4月的31亿美元。这意味着，资金流入的绝对水平并不低，但边际增量正在快速衰减。\n\n这种“总量尚可、增量收缩”的组合，通常出现在市场情绪从狂热回归理性的过渡阶段。投资者不再急于追涨，但尚未形成系统性撤离的共识。NOM报告中的月度图表清楚展示了这一趋势：1月和2月美国股票基金分别流入96亿和46亿美元，3月甚至出现小幅净流出，4\n\n[... middle omitted ...]\n\nynamics。欢迎来知识星球微信群中继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球资金悄悄转向，科技股波动下谁在接盘？\n\n资金流向变了\n\n最近全球资金流向出现微妙变化，某外资投行最新数据显示，6月19-25日期间，外资流入美股基金明显放缓，仅有14亿美元，远低于前一周的39亿美元。\n\n与此同时，新兴市场基金依然坚挺，同期流入18亿美元，和前一周的19亿美元基本持平。\n\n1️⃣ 美股热度降温\n科技股和AI板块波动加剧，外资对美股的态度明显谨慎起来。6月至今流入115亿美元，虽然比5月的88亿美元多，但周度数据已显示减速信号。\n\n2️⃣ 新兴市场保持韧性\nEM基金连续两周保持约18-19亿美元的稳定流入，6月累计已达29亿美元。资金似乎在寻找分散配置的方向。\n\n3️⃣ 韩国散户大幅收缩\n韩国个人投资者上周仅净买入4900万美元的美股资产，相比前一周的9.9亿美元大幅下降。之前连续两个月净卖出后，6月才刚转为净买入。\n\n4️⃣ 台湾转向美债\n台湾投资者上周净买入6100万美元的美元计价债券基金，扭转了前一周9500万美元的净卖出。6月整体仍为净卖出11亿美元。\n\n这个节奏很有意思：全球资金在科技股高位波动时，正在重新评估配置。新兴市场意外成为避风港，而亚太散户也在调整策略。\n\n大家最近关注哪\n\n[... middle omitted ...]\n\n 22 and 26 June, down from a larger purchase of USD990mn in the previous week.\n\n\\- Taiwan's investors net bought USD61mn of USD-denominated bond funds between 22 and 29 June, after net selling\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R003",
    "title": "GS：信用债市场真正的故事不是崩盘，而是分化",
    "digest": "[wechat_article.md]\n# GS：信用债市场真正的故事不是崩盘，而是分化\n\n当市场还在争论信用利差是否过于狭窄、风险是否被低估时，GS最新发布的宏观信用报告给出了一个反直觉的核心判断：**信用债市场当前最值得关注的不是系统性风险，而是结构性分化。**\n\n这份由GS信用策略主管Amanda Lynam执笔的报告，在2026年中这个时间节点上，提出了一个对机构投资者至关重要的观察框架。报告的核心主张可以概括为一句话：**在利率中枢抬升的新常态下，信用市场的定价逻辑已经发生根本性转变，真正的alpha机会不在于判断利差方向，而在于理解不同板块、评级和区域之间的分化程度。**\n\n对于手握重金的保险、养老金以及企业司库而言，这份报告的价值不在于预测市场走向——事实上，GS对利率和利差的总体判断相当温和——而在于它提供了一个在当前环境下如何重新定义“风险”与“机会”的思维框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利差极窄但收益率极具吸引力：这不是矛盾，而是新常态\n\nGS报告最核心的洞察，或许在于它解释了为什么信用利差可以在历史低位徘徊，而投资者却并未因此感到不安。\n\n关键数据点在于：从2010年到2021年，美元投资级信用利差平均占全部收益率的43%；而今天，这个比例只有15%。在欧元投资级市场，这一转变更为剧烈——从84%骤降至23%。\n\n这意味着什么？**当前信用债的吸引力几乎完全来自无风险利率本身，而非信用风险溢价。** 养老金和保险公司作为“基于收益率”的买家，其需求深度远超历史任何时期。GS估算，仅在美国公司债市场，这类投资者就持有至少40%的流通名义金额。\n\n> **KC评论：** 这不是一个简单的“利差太窄所以市场高估”的故事。当10年期美债收益率预期在4.4%附近波动时，即使利差小幅走阔，对总收益率的影响也远小于利率变动\n\n[... middle omitted ...]\n\n的损失率估算感兴趣，欢迎来我们的知识星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n信用利差很窄，但别只看表面\n\n**分散化，不是崩盘**\n\n**信用市场正在“分裂”，机会藏在细节里**\n\n最近看了一份某外资投行的信用研报，核心观点很清晰：市场整体不会崩，但内部正在剧烈分化。\n\n**1/ 利差窄≠没机会**\n现在IG（投资级）信用利差处于历史低位，但全收益率因为无风险利率高企而显得有吸引力。为什么利差下不去？因为养老金和保险公司这类“收益导向”买家深度参与，光在美元债市场，它们就持有至少40%的存量。而且，这些机构的配置需求还在增长——美元IG长端收益率5.7%，比美国寿险平均持仓收益率4.8%高出一截。\n\n**2/ 利率才是主角**\n2010-2021年，美元IG利差占全收益的43%，现在只剩15%。利率波动对信用市场的影响前所未有。如果利率波动率大幅上升，信用投资者会要求更宽的利差作为补偿。研报预计10年期美债年底在4.4%附近，这能给IG利差提供支撑。\n\n**3/ 美元信用债>欧元，但边界在模糊**\n今年以来美元IG和HY（高收益）的超额收益略好于欧元区，但差距在缩小。研报认为欧元区增长和通胀组合更差，预计欧元信用会继续跑输。但跨区域发债越来越频繁，比如今年美国公司占了欧元IG发行量的\n\n[... middle omitted ...]\n\net, we estimate this cohort of investors owns at least 40% of the notional outstanding. And beyond the current (and large) size of these holdings, we see scope for allocations to high quality \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "JPM：银行股最大的风险不是坏账，是AI黑客",
    "digest": "[wechat_article.md]\n# JPM：银行股最大的风险不是坏账，是AI黑客\n\n当市场还在为利率曲线、信贷周期和资本充足率争论不休时，JPM一份长达数十页的研报抛出了一个完全不同的风险排序：全球银行股估值中，目前最大的未被定价风险不是信用风险，而是网络安全风险。\n\n这不是一个遥远的威胁。报告指出，前沿AI模型——如Anthropic在2026年4月发布的Claude Mythos Preview和GPT-5.5——已将发现零日漏洞的时间从数月缩短至数小时。英国AI安全研究所的评估显示，Mythos在专家级黑客任务上的成功率达到了73%，而2025年4月之前没有任何模型能够完成这些任务。\n\n更值得注意的是，谷歌威胁情报集团在2026年5月首次确认，已发现一个威胁行为者使用了其认为是由AI开发的零日漏洞。这意味着AI驱动的网络攻击已从理论进入实践。\n\n对于银行投资者而言，这意味着传统的估值框架可能需要重新审视。JPM提出，在“神话时代”（Mythos-class era）的网络安全威胁下，银行股定价的核心变量正在从盈利能力和资本充足率，转向基础设施韧性和流动性管理能力。\n\n> **KC评论：** 这份报告的核心信号很清晰——网络风险正在从“运营问题”升级为“估值因子”。投资者需要关注的不仅是银行赚了多少钱，而是它们在面对AI驱动的网络攻击时，存款是否会在社交媒体时代瞬间流失。这直接决定了银行的资金成本和生存概率。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nJPM的分析框架中，银行应对AI网络攻击的能力并非均匀分布。报告明确指出，地缘政治和规模将成为关键的分化因素。\n\n美国大型银行处于明显优势地位。美国是AI发展的中心，拥有最先接触到最前沿AI模型的机会。Anthropic在2026年4月宣布\n\n[... middle omitted ...]\n\n在思考银行股的风险重定价，欢迎来我们的星球和微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI让银行更危险了，不是贷款那种\n\n银行最大的隐形炸弹\n\n前沿AI模型（比如Mythos、GPT-5.5）已经把发现系统漏洞的时间从几个月压缩到几小时。银行面临的核心问题，正在从“信用风险”转向“网络安全引发的流动性风险”。\n\n1/ 谁最脆弱？\n- 还在用几十年前COBOL代码的老系统银行\n- 依赖外部供应商但对方修复速度慢的银行\n- 多次并购后遗留多个旧平台的银行\n- 拿不到最新AI防护技术的银行\n\n2/ 为什么流动性比信用更危险？\n社交媒体的传播速度，叠加AI攻击能力，银行挤兑可能会比CS事件更剧烈。某外资投行认为，应该用“存款流失压力测试”来评估银行韧性，而不是只看资本充足率。\n\n3/ 怎么判断银行安全？\n外部很难直接评估IT基础设施，所以研究者把“IT支出占运营成本比例”作为参考指标。2025年全球银行平均约17%，但美国大行绝对支出更高、技术更新更快，欧洲银行相对落后。\n\n4/ 一些有意思的趋势\n- 物理安全键（硬令牌）可能回归，因为AI让远程钓鱼太容易\n- 新加坡银行已开始对数字交易设置冷静期\n- 量子计算威胁下，以太坊已启动“后量子防护”路线图，目标2029年\n\n5/ 保险越来越重要\n2025年\n\n[... middle omitted ...]\n\ngh the lens of the capital framework is not the best approach. In our view, there should be an increased focus on cybersecurity driven liquidity risk and this should be tested through increase\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 28 Jun 2026 06:47 PM BST\n\nDisseminated 29 Jun 2026 12:15 AM BST"
  },
  {
    "id": "R005",
    "title": "GS：最高法院5-4裁决，美联储独立性的真正考验刚刚开始",
    "digest": "[wechat_article.md]\n# GS：最高法院5-4裁决，美联储独立性的真正考验刚刚开始\n\n这份由GS首席经济学家Jan Hatzius与政治政策分析师Alec Phillips联合署名的最新报告，在8月最高法院就美联储理事Lisa Cook去留问题作出5-4裁决后迅速发布。市场普遍关注的是“Cook能否留任”这个短期结果，但GS团队却在字里行间给出了一个更值得推敲的判断：**这轮诉讼的终点不在Cook本人，而在美联储的独立性能否经受住总统更换理事的实质性挑战。**\n\n报告的核心价值不在于预测Cook案的最终胜负，而在于拆解了最高法院多数意见与异议意见之间的真实分歧，并由此推断出未来12-18个月美联储治理结构面临的不确定性。对于任何持有美债、关注利率路径或配置全球宏观资产的投资者而言，这都不是一个可以忽略的次要议题。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 5-4的票数不是全部，多数意见的措辞比表面数字更关键\n\nGS团队在报告中明确指出，尽管1月口头辩论时市场预期最高法院可能以接近共识的方式支持Cook留任，但最终5-4的投票结果比预期更接近。然而，报告随即给出了一个重要的分层判断：**多数意见的措辞远比投票数字所暗示的要坚定。**\n\n多数意见写道，法院“拒绝为这个国家（以及世界）最重要的金融机构之一的状态制造疑虑”，并强调核心问题是“所提出的解职理由是否真正表明不称职……或者它仅仅代表一种试图换上一个更合意人选的努力”。GS认为，这种措辞本身就是对美联储独立性的一种实质性背书。\n\n相比之下，多数异议意见主要聚焦于程序性问题，而非Cook案本身的实质是非。这意味着，那些投下反对票的大法官，未必会在案件的最终审理中作出不利于Cook的裁决。\n\n> **KC评论：** 多数意见的措辞是这份报告最值得逐字阅读的部分。GS团队实际上在提醒读者：法院\n\n[... middle omitted ...]\n\n，跟踪Cook案的最新进展，以及它对全球资产配置的潜在影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储独立性获关键背书，但博弈远未结束\n\n封面：美联储独立，暂保\n\n副标题：一场5:4判决背后的博弈\n\n---\n\n最近投行研报，详细拆解了美国最高法院的一则重要裁决——关于美联储理事Lisa Cook能否留任。结论很明确：美联储的独立性暂时保住了，但后面的路还很长。\n\n**1. 法官们到底怎么判的？**\n\n- 5:4 的票数，比市场预期的要接近。但多数意见书特意写了句话，翻译过来就是：“法院不会去动摇这个国家（乃至全球）最重要金融机构的地位。”\n- 意思是：我们不是来拆台的，我们想保护美联储的独立性。\n\n**2. 那4个反对票是啥意思？**\n\n- 投反对的法官，大部分不是真的反对Cook留任，而是觉得“程序上不对”。\n- 比如有人觉得，下级法院不该急着发禁令，应该先让案子走完流程。\n- 所以，这4票≠对Cook的实质反对，更像是在说“你们别急，程序要对”。\n\n**3. 所以美联储真的安全了吗？**\n\n- 研报说：不确定性降低了，但没消除。\n- Cook的案子会回到地方法院继续审理，至少还要几个月。\n- 而且，总统发帖说“这事没完”，大概率会继续上诉。\n- 所以，这个案子明年大概率还会回到最高法院。\n\n**4.\n\n[... middle omitted ...]\n\nnd in part on the underlying facts in the case.”\n\n## MAIN POINTS:\n\n1. The Supreme Court ruled 5-4 to deny the Trump Administration's application to stay a preliminary injunction against Fed Go\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "Citi：耐克若切断中国经销商线上渠道，最大赢家不是它自己",
    "digest": "[wechat_article.md]\n# Citi：耐克若切断中国经销商线上渠道，最大赢家不是它自己\n\n7月1日，耐克将发布第四财季业绩。对很多投资者而言，这只是一次常规财报。但对关注中国运动鞋服赛道的人来说，这可能是一个决定未来两年板块格局的关键时刻。\n\nCiti在最新一份研报中，围绕耐克中国线上分销策略的三种可能情景，给出了明确的股票含义推演。这份报告的价值不在于预测耐克会选哪条路，而在于它揭示了一个被市场低估的结构性问题：耐克在中国市场积累的“线上分销能力”，远比它自己想象的更难被替代。\n\n这不是一个简单的“品牌方要不要直营”的决策。这是一场关于渠道权力转移、本土化运营壁垒、以及反垄断风险的博弈。而在这场博弈中，最值得关注的，可能不是耐克本身，而是那些站在它对立面的中国品牌和竞争对手。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 市场已经在为最坏情景定价，而耐克即将给出答案\n\n上周，耐克中国最大经销商宝胜国际（Topsports）的股价持续下跌。即便公司在周四晚间发布了澄清公告，周五股价依然没有止住跌势。\n\nCiti的分析师认为，这种市场行为传递了一个清晰的信号：投资者已经在为“耐克将终止与宝胜的线上分销合作”这一最坏情景定价。宝胜的线上业务约占集团总销售的22%，如果这部分业务被直接砍掉，对公司的冲击将是实质性的。\n\nCiti将耐克可能的表态划分为三种情景，并给出了相应的股票含义：\n\n- 情景一：耐克明确表示将终止中国零售商的线上分销权。这将是市场已经部分定价的“坏消息”成为现实。Citi认为，耐克将在2027财年因此在中国市场丢失份额。利好中国品牌和其他国际品牌（如安踏、李宁、阿迪达斯中国、彪马中国），利空耐克中国生态链公司。\n- 情景二：耐克重申与头部中国零售商合作，优化线上分销。这将是双赢局面，耐克中国市场份额有望稳定。利好宝胜及其他耐克中国\n\n[... middle omitted ...]\n\n动态。欢迎来星球微信群继续讨论，一起跟踪这个事件的后续发展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNike中国线上策略的三个剧本\n\nNike线上策略的三条路\n\n市场正在定价最悲观的可能\n\n最近滔搏的股价持续下跌，市场已经在消化一个预期：Nike可能终止和中国头部零售商的线上分销合作。对滔搏来说，这涉及集团约22%的销售额。7月1日早上的业绩会，Nike管理层大概率会给方向。\n\n**剧本一：终止线上分销合作**\n如果Nike真这么干，反而是利好安踏、李宁、Adidas这些竞争品牌。原因有三：\n1. 中国零售商积累的直播带货、即时零售、私域电商这些能力，Nike自己的DTC渠道很难短期复制\n2. 零售商失去Nike线上业务后，线下大店也会失去全渠道吸引力，资源会转向Adidas和国产品牌\n3. 这种终止合作的行为，可能被认定为限制竞争，面临反垄断审查风险\n结果就是Nike在中国市场份额大概率继续流失\n\n**剧本二：继续合作优化线上**\n如果Nike表态继续和头部零售商合作，那就是双赢。可能的合作方向包括：整合小分销商的线上业务、加强线上线下产品差异化、更严格的价格监控。这对滔搏和其他Nike生态公司是利好。\n\n**剧本三：模糊表态**\n如果管理层不给明确方向，市场会继续按最坏情况定价，结果和剧本一类似。\n\n有\n\n[... middle omitted ...]\n\nly 1, HKT, with three likely scenarios (detailed below). If Nike confirms its intention to terminate China retailers' online distributorship, we expect positive stock implication on Chinese & \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R007",
    "title": "GS：亚洲正迎来一个“油跌、钱紧、科技热”的罕见窗口",
    "digest": "[wechat_article.md]\n# GS：亚洲正迎来一个“油跌、钱紧、科技热”的罕见窗口\n\n过去几周，亚洲市场正在经历一场罕见的“三重奏”：油价暴跌、美元走强、科技出口狂飙。GS在最新发布的《Asia Views》报告中，给出了一个看似矛盾但逻辑自洽的核心判断：亚洲正站在一个“宏观压力缓解、但政策工具箱收紧”的十字路口。这不是一个简单的“利好出尽”或“利空出尽”的故事，而是一个需要精细拆解的结构性窗口。\n\n这份报告最值得关注的判断是：亚洲的通胀压力正在快速消退，但央行的紧缩倾向并未同步降温。与此同时，以AI为核心的科技出口正在重塑部分经济体的增长曲线，而中国则陷入“出口独大、内需疲弱”的罕见分化。对于投资者而言，关键不再是判断方向，而是识别哪些经济体能够从“油跌”和“科技热”中真正受益，哪些仍被“美元压力”和“内需塌陷”所拖累。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油价暴跌是“解药”，但不是“万能药”：亚洲的通胀故事正在重写\n\n布伦特原油从4月底接近120美元/桶的高位，暴跌至报告撰写时的72美元/桶。GS大宗商品团队预计四季度油价将稳定在80美元/桶。这轮油价的“近乎回吐”是亚洲进口国最直接的利好。\n\n但GS同时指出，成品油价格仍高于战前水平，因为海湾地区和俄罗斯的炼油设施受损，炼油利润空间依然宽裕。这意味着，终端消费者感受到的降价幅度可能不及原油期货的跌幅。对于菲律宾等能源补贴有限的经济体，通胀压力虽已见顶，但回落速度可能慢于预期。\n\n> **KC评论：** 油价暴跌是“雪中送炭”，但并非“久旱甘霖”。报告隐含的判断是，亚洲各国央行之所以还能维持鹰派立场，正是因为“油跌”给了它们一个观察窗口，而不是立即转向宽松的理由。完整报告中关于各国通胀目标偏离度的图表（Exhibit 4）值得细看，它揭示了哪些经济体有放松空间，哪些仍在危险区\n\n[... middle omitted ...]\n\n迎加入我们的微信群继续讨论，一起拆解这些报告背后的真实含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价暴跌、美元走强、科技狂飙\n\n亚洲正在经历三个变化\n\n油价终于降了，但别高兴太早\n\n1️⃣ 油价从4月高点120美元跌到72美元，几乎是“回吐”了战争涨幅。但炼油产品价格还是偏高，因为海湾和俄罗斯的炼油设施受损，利润空间依然大。预计Q4回到80美元。\n\n2️⃣ 美元又硬起来了。新任美联储主席Warsh偏鹰，FOMC对利率预期上调，美元接近3月高点。亚洲经济体压力不小，尤其是那些没怎么补贴能源的国家——菲律宾CPI冲到7.2%。\n\n3️⃣ 科技支出才是真正的“主线”。AI相关资本开支预估接近1万亿美元，韩国、台湾、马来西亚、新加坡的贸易顺差都超过GDP的10%。韩国消费有望回暖，台湾经济增长约10%，是40年来最强。\n\n中国：出口猛，内需冷\n\n5月出口同比增19%，但零售跌0.6%，固定资产投资跌4.1%。国内需求年增速只有1-2%，全靠出口撑着。政策上，央行更强调价格型调控，加速人民币国际化。\n\n亚洲央行：多数偏紧\n\n日本已加息，菲律宾、印尼再加，韩国预计7月首次加息。印度是例外，市场预期加息但央行在“推后”，同时鼓励资本流入稳汇率。\n\n接下来看什么？\n\n- 油价回落，各国可能减少补贴，释放财政空间\n- 日\n\n[... middle omitted ...]\n\n the war, more so for refined products where margins are likely to remain wide due to damage to facilities both in the Gulf and in Russia. Furthermore, a hawkish shift at the Fed – both in ter\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R008",
    "title": "摩根斯坦利：MS：中国正等待的不是刺激，而是“花钱的方向”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国正等待的不是刺激，而是“花钱的方向”\n\n当市场仍在猜测中国是否会推出新一轮大规模消费刺激时，MS最新一期中国情绪追踪报告给出了一个更克制的判断：北京正在准备的是以资本支出为核心的财政发力，时间窗口在第三季度，但重点投向是AI和电网，而非消费。\n\n这个判断对当前市场叙事构成了一次清晰的纠偏。如果你还在用“消费复苏强度”来评估中国资产，这份报告提醒你，政策层关注的变量，可能和你不在同一个频道上。\n\n报告由首席中国经济学家邢自强团队撰写，核心观点可以浓缩为一句话：二季度经济仍在温和放缓，但政策层正在为下半年积蓄弹药，只是这些弹药将主要打向供给端的基础设施，而非需求端的消费补贴。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二季度GDP增速可能只有4.4%，但这不是最值得担心的事\n\nMS对二季度实际GDP增速的追踪值为4.4%，低于全年5%左右的官方目标。但报告没有将这一点渲染为风险信号，而是将其理解为两个暂时性逆风叠加的结果。\n\n第一个逆风是财政节奏滞后。二季度约60%的债券额度尚未使用，8000亿元准财政基建资金几乎没有动用。这不是政策意愿问题，而是执行节奏问题。\n\n第二个逆风是能源价格。全球石油供需正在逐步再平衡，这意味着此前对国内石化行业形成的成本压力有望缓解，同时也能通过改善贸易条件间接支撑出口。\n\n报告的核心逻辑是：这两个逆风在下半年都可能转为顺风。财政发力将从三季度开始加速，能源价格压力减轻也将改善企业利润和出口竞争力。\n\n> **KC评论：** 4.4%这个数字本身不重要，重要的是MS认为下半年的边际变化方向是向上的。但要注意，这里有两个关键假设：一是财政确实能如期加速，二是全球油价不会出现新的供给冲击。这两个假设目前都还没有被验证，这也是为什么完整报告里对财政执行细节和全球能\n\n[... middle omitted ...]\n\n型的资产定价含义——感兴趣，欢迎来我们的星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n政策转向在即，下半年盯紧两大主线\n\n📌 三季度财政发力，AI和电网优先\n\n某外资投行最新研报判断，北京将从三季度开始加大以资本支出为核心的财政投放，重点方向是AI和电网，而非消费。简单说，下半年政策重心更偏向“投基建”和“硬科技”，而不是刺激买买买。\n\n1️⃣ 经济现状：高端制造稳，内需有点冷\n- 新兴产业PMI虽然小幅回落至52.2，但今年均值仍高于2024-25年，说明高端制造韧性还在\n- 出口端，集装箱吞吐量增速放缓到3%，但研报认为这不代表出口变弱——科技产品更多走空运，海运数据有失真\n- 内需方面，二手房交易又软了，端午旅游也是“人流量大、钱包没跟上”，汽车和家电零售受高基数压制，同比压力不小\n- 好消息是，水泥和钢筋需求在6月边际改善，建筑活动小幅回暖\n\n2️⃣ 财政：钱还没花出去，但很快要加速\n- 5月财政数据确认了“收入不错、支出拖沓”的格局，收入同比+6.8%，支出却同比-1.6%\n- 6月政府债和政策行债发行依然偏弱，说明财政落地还没明显加速\n- 但发改委6月已经开了座谈会，讨论“六网”建设的项目回报和资金支持，细节敲定后，三季度基建投放大概率提速\n- 目前约60%的债券额度未用，8000\n\n[... middle omitted ...]\n\nrage of 51.1. Container throughput growth has slowed to \\~3%Y in May and June (Exhibit 3). We do not think it necessarily points to weaker exports, in view of the higher concentration of tech \n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R009",
    "title": "NOM：美元下半年会跌，但真正的赢家不是欧元",
    "digest": "[wechat_article.md]\n# NOM：美元下半年会跌，但真正的赢家不是欧元\n\n过去几个月，美元在美联储鹰派预期和中东局势缓和的夹缝中走出一波反弹。市场普遍认为，美联储年内还有加息空间，美国经济韧性足以支撑美元维持强势。但NOM最新发布的中期外汇展望报告给出了一个截然不同的判断：美元的强势在下半年很难持续，DXY指数年底将回落至98附近，2027年甚至可能跌至92.7。这背后不是地缘政治的转向，而是美联储政策路径与市场定价之间正在积累的预期差。\n\n这份报告的核心主张清晰而直接：全球外汇市场的焦点正在从中东地缘风险回归到央行动作与利率定价的相对变化上。对于G10货币，NOM认为最大的机会来自那些央行仍有加息空间、同时资本流动动能正在改善的货币——欧元、日元、新西兰元和澳元。而对于亚洲（不含日本）市场，人民币、新台币和新加坡元将跑赢韩元、印尼盾和印度卢比。\n\n这些判断的背后，是NOM对美联储年内不会加息的坚定预期。报告指出，市场目前定价了约40个基点的加息，但NOM认为，下半年美国增长和通胀动能的逐季放缓，将给美联储主席沃什提供向鹰派回击的机会。如果相对美国收益率下降40个基点，美元将面临系统性贬值压力。\n\n> **KC评论：** NOM这个判断的核心逻辑不是美国经济要崩，而是市场对美联储的定价太鹰了。如果下半年通胀数据确实走软，美联储按兵不动，美元就会补跌。但这里有一个关键假设尚未验证——沃什是否真的会“向鹰派回击”？报告没有完全展开的是，如果沃什选择观望而非主动打压加息预期，美元的下行节奏可能会慢于NOM的预测。完整报告里对沃什第一次会议讲话中“被忽略的鸽派元素”做了详细拆解，这部分值得仔细阅读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧元是G10中最大的受益者，但前提是市场重新定价ECB\n\nNOM对欧元的态度是G10中最乐观的之一\n\n[... middle omitted ...]\n\n信群里继续讨论，和志同道合的读者一起跟踪这些关键信号的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球汇率正在悄悄转向\n\n美元弱了，这些货币要强\n\n2026下半年，G10和亚洲货币的赢家与输家\n\n📌 某外资投行最新研报显示，下半年外汇市场焦点将从地缘风险转向央行行动。核心判断：美联储不会加息，美元将在下半年走弱。\n\n1️⃣ G10货币：谁赢谁输？\n- 看好：欧元、日元、新西兰元、澳元\n  - 欧元：市场对美联储加息过度定价，而欧央行仍偏鹰派。资本流入欧元区正在改善，加上经常账户盈余，欧元有望受益于“去美元化”趋势。\n  - 日元：短期可能继续承压，但中期风险平衡转向日元升值。日本央行加息预期升温，财务省仍有干预能力，空头头寸已极度拥挤。\n  - 新西兰元：经济刚走出衰退，央行接近开启加息周期。短期头寸极度做空，外资持有新西兰国债比例低但正在上升，构成支撑。\n  - 澳元：贸易条件改善，资本流入债券市场强劲。若“去美元化”主题重现，澳元可能成为赢家。\n- 承压：英镑、加元、瑞典克朗\n  - 英镑：最鸽派的央行前景+财政担忧。新首相面临支出与税收难题，政策不确定性可能压制投资。\n  - 加元：通胀更软、劳动力市场疲软，央行加息门槛高。美加贸易谈判进展缓慢构成额外压力。\n  - 瑞典克朗：通胀低于目标，国内增长\n\n[... middle omitted ...]\n\neir hiking cycles and where there is room for portfolio flow momentum to improve (EUR, JPY, NZD and AUD on the latter point). We see others as more vulnerable on central bank disappointment (G\n\n[... middle omitted ...]\n\nof NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International plc, UK. All rights reserved."
  },
  {
    "id": "R010",
    "title": "NOM：德里的电动车新政，正在给CNG天然气写下“终局”",
    "digest": "[wechat_article.md]\n# NOM：德里的电动车新政，正在给CNG天然气写下“终局”\n\n一份来自印度首都的政策文件，可能正在改写整个城市天然气分销行业的估值逻辑。2026年6月29日，德里内阁批准了其“2026-2030电动车政策”，并于7月1日正式生效。NOM在第一时间发布的研报中给出了一个直接而冷静的判断：这项政策对德里最大的天然气分销商IGL的CNG（压缩天然气）业务，构成了“终局价值风险”。\n\n这不是一个关于补贴多少、销量增速放缓多少的温和讨论。这是一份关于“一个核心业务模式在特定市场内，何时以及以多快的速度走向终结”的研究。对于任何关注印度能源转型、基础设施资产定价，乃至全球城市治理范式的投资者而言，这份研报的价值不在于预测一家公司的季度盈利，而在于揭示一个正在发生、且可能被其他城市复制的结构性拐点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 从“鼓励你买”到“只准你卖电的”：政策逻辑的质变\n\n要理解这份政策的冲击力，需要先看清其与前身——2020年德里电动车政策的根本差异。NOM在报告中用了一个清晰的对比表格。2020年政策的核心哲学是“激励引导”，政府提供购车补贴和税费减免，希望人们自愿转向电动车。结果如何？2024年电动车在新车注册中的渗透率目标为25%，实际只达到约13%。\n\n2026年政策的核心哲学则变成了“强制要求”。它不再只是发钱，而是直接设立了硬性的注册禁令。从2027年1月1日起，德里将只允许新的电动三轮车（包括自动人力车）和小型货物运输车注册，汽油、柴油、CNG和混合动力车型一律禁止。从2028年4月1日起，同样的禁令将适用于两轮车。政策目标更是激进：到2027年，95%的新增个人车辆注册必须是电动车。\n\n这不再是政策风向的微调，而是游戏规则的彻底改写。当政府从“引导者”变为“执法者”，整个市场的需求曲\n\n[... middle omitted ...]\n\n方便人工快速把握全球市场的动态。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n德里新规：CNG车要被淘汰了？\n\nCNG面临终结风险\n\n德里电动车新政2026-2030，CNG车增量被彻底封杀。\n\n1/ 政策变了：从补贴引导变成强制淘汰\n2020版是“我补贴你，你考虑买电动车”\n2026版是“我不让你注册燃油/CNG新车，你只能买电动”\n2027年1月起：新三轮车、小货运车只能电动\n2028年4月起：新两轮车也只能电动\n目标：2027年95%新车注册必须是电动（上次2024年目标25%都没实现，实际只有13%）\n\n2/ 补贴结构：真金白银给到位\n车价300万卢比以下：免100%道路税+注册费\n两轮补贴：第1年3万/第2年2万/第3年1万卢比\n三轮补贴：第1年5万/第2年4万/第3年3万卢比\n报废旧车换购电动：最高10万卢比\n补贴直接打到受益人银行账户\n\n3/ 对CNG公司的冲击\nIGL：最受伤。CNG车/出租车占其CNG销量的65%，三轮车CNG占比已不到20%。新规后德里CNG新车增量将结构性下滑，但现有车队短期影响有限。IGL未来增长得靠周边扩张和家庭燃气。\nMGL：主要在孟买，短期无直接冲击。但如果马哈拉施特拉邦跟进，风险就会来。孟买连柴油车都没禁，CNG暂时安全。\n古吉拉特燃气：\n\n[... middle omitted ...]\n\n 2028 onwards: only new electric two-wheelers (no petrol/CNG) will be eligible for registration in Delhi.\n\n• 31 Mar 2030: policy expires.\n\n## Incentives structure\n\n\\- 100% road tax and registr\n\n[... middle omitted ...]\n\ns information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved."
  },
  {
    "id": "R011",
    "title": "JPM：韩国3.1万亿美元押注，存储器行业进入“超级周期”还是“产能陷阱”？",
    "digest": "[wechat_article.md]\n# JPM：韩国3.1万亿美元押注，存储器行业进入“超级周期”还是“产能陷阱”？\n\n当韩国政府与三星、SK集团共同宣布一项高达4755万亿韩元（约合3.1万亿美元）的长期投资计划时，全球半导体产业的目光再次聚焦于存储器。这份由JPM分析师Jay Kwon团队发布的报告，并未停留在对投资数字的简单罗列，而是试图回答一个更本质的问题：在AI需求看似无底洞的当下，存储器行业面临的究竟是前所未有的机遇，还是正在重蹈历史覆辙？\n\n报告的核心判断是，韩国存储器双雄的巨额投资，本质上是一场关于“供给短缺”与“竞争壁垒”的豪赌。但市场对此的反应却相当复杂——消息公布当日，韩国存储器股价反而下跌。这种“利好出尽”的走势背后，隐藏着更深层的担忧：当供给以数倍于历史的速度扩张，当客户开始抱怨价格过高并诉诸法律，这个行业的游戏规则是否正在被改写？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 3.1万亿美元的“建设宣言”：速度与规模的双重颠覆\n\n这份投资计划的震撼力不在于数字本身，而在于其时间表和执行意图。JPM报告指出，三星和SK集团计划建设的产能规模，将是当前全球DRAM装机容量的两倍。更关键的是，建设节奏被大幅提前——三星将龙仁工厂的投产时间从2045-2047年提前至2033-2040年，SK集团则将第四座工厂的投产时间从2045年拉近到2033年，整整缩短了12年。\n\n这意味着，在2020年代末期之后，存储器产能的投放速度将比历史上任何时期都快。报告估算，仅前道晶圆设备支出就将占到总投资的60-70%，达到约1.86-2.17万亿美元。如此庞大的资本开支，其背后的逻辑是韩国政府和企业对“AI存储器需求将长期超过供给”这一判断的坚定信仰。\n\n> **KC评论：** 这份投资计划不是普通的产能扩张，而是一次“时间压缩”。过去20年\n\n[... middle omitted ...]\n\n？集体诉讼的风险是否被市场低估？欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国砸3万亿美金，押注AI存储\n\n**3万亿美金，存储大棋**\n\n韩国政府+三星+SK集团，联手宣布了史上最大规模半导体投资计划。总金额高达4,755万亿韩元（约3.1万亿美金），目标直指AI时代的存储霸权。\n\n**这钱怎么花？**\n\n1️⃣ **三星：2,655万亿韩元**\n- 龙仁半导体集群（1,650万亿）：DRAM产能大跃进\n- 天安/温阳（56万亿）：HBM先进封装\n- 龟尾（60万亿）：人形机器人量产线\n- 加上光州新厂、显示器、电池等布局\n\n2️⃣ **SK集团：2,100万亿韩元**\n- 龙仁（600万亿）：DRAM产能提前12年\n- 清州（100万亿）：NAND扩产\n- AI数据中心（1,000万亿）：15GW规模，分两期建设\n\n**为什么现在砸钱？**\n\n核心矛盾：**供给跟不上需求**。研报指出，当前存储产能仅能满足需求的一半，且缺口还在扩大。三星和SK掌门人明确表态：要打破产能瓶颈，守住韩国在AI存储的领导地位。\n\n**市场怎么看？**\n\n短期市场反应偏负面，但研报认为中长期值得关注。按15%-25%的资本密集度测算，这3万亿美金投资可能带来12-20万亿美金的累计收入机会——对比过去\n\n[... middle omitted ...]\n\nillars (link). The genesis of the investment stems from retaining the current AI leadership (especially in AI semiconductors) and leapfrogging as an AI export country through nurturing and dev\n\n[... middle omitted ...]\n\nd herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is"
  },
  {
    "id": "R012",
    "title": "JPM：工业利润的双速引擎，一个在飞驰，一个在熄火",
    "digest": "[wechat_article.md]\n# JPM：工业利润的双速引擎，一个在飞驰，一个在熄火\n\n中国5月工业利润数据出炉，同比增速18.8%，看似稳健。但JPM这份最新研报揭示了一个核心判断：这轮利润增长不是“普涨”，而是一场结构性的“双速分化”——高科技和上游原材料行业利润飞驰，而消费相关行业却几乎熄火。对于投资者和产业决策者而言，真正的挑战在于：这种分化是暂时的周期错位，还是中国经济转型的长期底色？\n\n这份报告的价值不在于告诉你利润在增长，而在于指出了一个容易被总量数据掩盖的关键信号：利润增长的质量和可持续性，正面临来自终端需求的根本性约束。读懂这份报告，需要关注的不是18.8%这个数字本身，而是数字背后的“温差”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利润增长的两大引擎：AI周期与上游成本红利\n\n5月工业利润增长最显著的特征是“双引擎”驱动。第一个引擎是高科技制造业，尤其是与全球AI周期紧密相关的电子设备制造。报告数据显示，计算机、通信和其他电子设备制造业1-5月利润累计同比飙升103.9%，高技术制造业整体利润增长44.7%。这背后是全球AI投资浪潮对存储芯片、电子专用材料等产品的强劲需求，半导体供应链的快速改善成为最直接的受益者。\n\n第二个引擎来自上游原材料。非有色金属行业利润同比增长117.1%，化学原料及制品利润增长71.6%。这与全球能源价格高位运行、以及AI和新能源产品对铜、铝等基础金属的需求拉动密切相关。上游企业不仅享受了量价齐升，还受益于成本端相对可控，利润空间显著扩大。\n\n> **KC评论：** 这两个引擎的本质不同。高科技的利润增长来自“技术溢价”和全球需求共振，可持续性较强；而上游利润更多依赖价格周期，一旦全球能源价格回落，利润弹性可能迅速逆转。报告后面提到能源风险缓解，恰恰暗示了上游利润的“脆弱性”。\n\n![研\n\n[... middle omitted ...]\n\n题，欢迎加入我们的知识星球与微信群，每天获取最新研判与数据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n工业利润，正在“分层”修复\n\n工业利润两极化\n\n高增长背后，消费端还在拖后腿\n\n---\n\n1 月到 5 月，工业企业利润累计同比增长 18.8%，看起来不错。但拆开看，增长主要靠两股力量：科技制造（尤其是电子设备）和上游原材料。消费相关的行业，利润还在承压。\n\n**1. 谁在赚钱？**\n\n📈 电子设备制造利润同比 +103.9%，AI 周期和存储芯片需求是核心驱动力。高技术制造整体利润 +44.7%。\n\n📈 有色金属（铜、铝）利润 +117.1%，受益于 AI 和新能源对上游材料的需求拉动。\n\n📈 化工行业利润 +71.6%，全球能源价格高位支撑。\n\n**2. 谁在亏钱？**\n\n📉 家具利润 -58.4%，汽车 -19.8%，服装 -11.4%。消费端 PPI 还在负区间（-0.8%），企业很难把成本转嫁出去。\n\n📉 库存积压：产成品库存同比 +8.8%，应收账款 +7.7%，说明回款变慢、周转压力上升。\n\n**3. 后续怎么看？**\n\n研报观点：两极化还会持续。AI+ 和产业升级政策会继续支撑高技术制造，但消费端修复需要更大力度的财政支持。能源价格回落（布伦特预期 80 美元/桶）可能给下游行业一些喘息空间\n\n[... middle omitted ...]\n\n (from 24.7% in April). In Jan-May, sales revenue rose 5.5% oya, while costs rose more slowly at 4.7%, supporting net profit margin. That said, accounts receivable climbed 7.7% oya and finishe\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R013",
    "title": "摩根斯坦利：MS：中国顺差遇上欧盟防御，真正的风险不是关税战",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国顺差遇上欧盟防御，真正的风险不是关税战\n\n欧盟与中国的贸易摩擦正在升级，但这一次的剧本与2018年中美贸易战截然不同。MS首席中国经济学家邢子林（Robin Xing）团队在最新发布的研报中给出了一个核心判断：中国与欧盟之间的贸易紧张不会走向全面脱钩，但会以一种更制度化、更行业化的方式持续发酵。而真正值得关注的，不是关税清单本身，而是中国内部需求结构失衡正在将贸易顺差变成一个结构性变量——这意味着，即便没有新的贸易摩擦，中国与主要贸易伙伴之间的张力也会自然上升。\n\n这份报告的价值不在于预测短期关税博弈，而在于揭示了一个长期逻辑：中国的经常账户顺差正在从“政策驱动”转向“结构驱动”。当住房投资进入长期下行、基础设施刺激空间收窄、而居民储蓄率居高不下时，过剩储蓄必然会表现为外部顺差。这不是一个可以靠汇率调整或短期让步解决的问题。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧盟的“工具箱”已经升级，但它的目标不是脱钩\n\n欧盟正在构建一套比2024年电动车反补贴调查更系统的对华贸易管理框架。MS团队梳理了欧盟近年来的政策工具演变，发现一个清晰的趋势：从个案式的反倾销反补贴，转向“制度化的经济安全管控”。\n\n核心工具包括：外国补贴条例（FSR）在政府采购中的使用、国际采购工具（IPI）首次针对中国医疗器械、碳边境调节机制（CBAM）覆盖钢铁铝材和化工品、以及清洁能源补贴和汽车采购中不断强化的本地化要求。\n\n这套组合拳的特点是：不突然、不全面、但不可逆。它不像美国那样动辄威胁加征全面关税，而是通过法律程序、技术标准、采购规则等“软性壁垒”逐步收紧。这意味着，中国企业面临的不是在某个时间点被一次性打击，而是在多个行业、多个环节、持续面临准入成本的上升。\n\n> **KC评论：** 对于关注\n\n[... middle omitted ...]\n\n后续欧盟政策动向的持续跟踪感兴趣，欢迎来星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中欧贸易摩擦，不只是关税问题\n\n中欧贸易博弈，比你想的更深\n\n一份投行研报的拆解\n\n最近中欧贸易关系有点微妙。某外资投行最新研报指出，摩擦正在升级，但不会失控。核心逻辑是：\n\n1️⃣ 欧盟工具箱在扩大\n不只是反补贴调查，欧盟现在用更系统化的工具：外国补贴条例（FSR）审查中企投标、国际采购工具（IPI）限制市场准入、碳边境调节机制（CBAM）覆盖钢铁铝业。清洁能源领域还加了本地化要求。这意味摩擦会更“制度化”、更精准。\n\n2️⃣ 压力集中在这些行业\n按研报框架，欧盟对华逆差大+自身竞争力强的行业最危险。汽车（中国电动车挑战传统优势）、机械电气、化学品首当其冲。钢铁和基础金属则是结构性产能过剩。\n\n3️⃣ 中国顺差有深层原因\n研报观点：不是简单的贸易政策。房地产投资长期下滑，国内储蓄率高但需求弱，过剩储蓄只能转化为外部顺差。除非消费端有决定性转向，否则顺差会持续。\n\n4️⃣ 双方都有牌但都不想掀桌\n中国反制工具：猪肉、乳制品、白兰地调查，航空汽车市场准入。欧盟依赖中国稀土和清洁能源供应链。双方会法律博弈，但不会决裂。\n\n5️⃣ 人民币不会大升值\n研报判断：地产下行+消费转型难，快速升值只会挤压出口和就业，加剧通\n\n[... middle omitted ...]\n\n should concentrate where the EU runs widening bilateral deficits but still has globally competitive industries — autos, machinery & electrical equipment, and chemicals.\n\nThe toolkit has widen\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R014",
    "title": "NOM：中国二季度GDP增速或骤降至4.1%，出口繁荣掩盖了内需的真实收缩",
    "digest": "[wechat_article.md]\n# NOM：中国二季度GDP增速或骤降至4.1%，出口繁荣掩盖了内需的真实收缩\n\n中国经济在2025年二季度正经历一场“冷热不均”的剧烈分化。NOM东方国际证券最新发布的研报给出了一个让市场难以忽视的判断：在经历了短暂的一季度反弹后，中国二季度实际GDP增速将从一季度的5.0%明显放缓至4.1%。这一预测并非危言耸听，而是基于对供给端和需求端双重指标的交叉验证。\n\n更值得警惕的是，这份报告揭示了一个核心矛盾：出口在AI超级周期的推动下表现强劲，但这种繁荣更多体现在价格而非实物量上，且未能有效传导至国内生产与消费。与此同时，国内零售与固定资产投资增速已再次转负，房地产市场持续探底，居民消费信心受挫。这些信号叠加在一起，指向一个结论：当前经济的真实动能，比官方GDP数字所呈现的要弱得多。\n\n这份NOM研报的价值，不在于它给出了一个悲观的数字，而在于它拆解了这个数字背后的结构性失衡——出口的“虚假繁荣”与内需的“真实萎缩”正在同时发生。对于产业决策者和投资者而言，理解这种分化的根源，远比争论GDP增速是否达标更为重要。\n\n> **KC评论：** NOM这个4.1%的预测，比市场主流预期要低。关键在于，他们认为二季度名义GDP增速可能因为通胀回升而稳定，但实际增长动能显著下滑。这意味着企业营收增长可能更多来自价格因素，而非销量扩张，利润质量需要仔细审视。完整报告中还有对GDP平减指数由负转正的分析，这个指标对理解企业盈利环境非常关键。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 供给端与需求端均指向放缓，但需求端的信号更为严峻\n\n从生产端看，工业和服务业产出增速在4-5月已明显下滑。NOM测算，工业增加值和服务业生产指数在二季度的季度平均增速可能分别仅为4.5%和4.5%，较一季度的6.1%和5.1%显著回落。考虑到这两个行业\n\n[... middle omitted ...]\n\n趣，欢迎来我们的微信群继续讨论，一起追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nQ2经济放缓，但没那么糟\n\n**4.1%的GDP增速**\n\n**Q2实际GDP增速预计从Q1的5.0%降至4.1%**\n\n---\n\n1/ 4-5月数据已经确认Q1的反弹是短期的，6月也没看到明显回升。工业和服务业增速都下来了，分别从6.1%和5.1%降到4.5%。\n\n2/ 需求端更弱。零售和固投4-5月平均增速已经转负，分别-0.2%和-9.5%。出口虽然冲到16.7%，但一半是芯片涨价撑的，实际量没那么多。\n\n3/ 出口强≠工业好。AI超级周期推高了芯片价格，但对真实工业产出拉动有限。中东冲突还严重影响了石油化工产业链的开工。\n\n4/ 消费承压的三个原因：以旧换新政策的透支效应、地产持续低迷、K型分化加剧。6月零售预计只有0.9%，汽车销售还是两位数负增长。\n\n5/ 地产投资还在深跌，6月预计-25%。一线城市二手房价格连续3个月环比涨0.4%，上海从1月低点累计涨了1.9%，但二线只是温和改善。\n\n6/ CPI和PPI通胀都在走高，6月预计1.2%和4.0%。但通胀主要是外部因素推的（油价、芯片），不是内需真复苏。GDP平减指数可能13个季度来首次转正。\n\n7/ 政策预期：投资持续下滑，政府债券发行加速和\n\n[... middle omitted ...]\n\ne again, as aggregate domestic demand is being weighed on by payback effects from the trade-in program, the prolonged property slump and a worsening of the double K-shapes. Based on an examina\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R015",
    "title": "Citi：地产股回调不是终点，而是下一轮选股的起点",
    "digest": "[wechat_article.md]\n# Citi：地产股回调不是终点，而是下一轮选股的起点\n\n当市场被周度二手房成交量环比下降10%和季末流动性收紧所惊吓，地产板块再次遭遇抛售时，Citi却在6月下旬的行业会议后给出了一个反直觉的结论：**他们正在变得更加积极**。\n\n这份由Citi分析师Griffin Chan和Cindy Li主笔的报告，并非简单喊多。它建立在一个关键的时间差判断上——市场当前的悲观情绪，忽略了一个即将到来的结构性窗口：从9月开始，主要开发商将集中推出新盘，而7月政治局会议很可能释放更明确的政策支撑信号。\n\n换句话说，Citi认为，地产股最恐慌的时刻可能已经过去，但真正的分化才刚刚开始。投资者需要关注的不是整个板块是否见底，而是谁能在“销量复苏但利润承压”的新常态中，证明自己的商业模式可以穿越周期。\n\n这份报告最值得被记住的判断是：**2026年上半年将是开发商盈利能力的“压力测试”，但那些在土地市场保持纪律、在核心城市拥有产品溢价能力的公司，将在下半年迎来估值修复的窗口。**\n\n以下是Citi这份研报的核心洞察与未解问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月销售数据已经出现“隐形的分化”——5家公司实现两位数增长，但行业整体仍在收缩\n\n市场对地产板块的普遍印象是“还在跌”。从行业总量看，5月整体销售额同比下降约15%，这确实是事实。但Citi的研报揭示了一个被总量掩盖的关键分化：在19家参与会议的开发商中，有5家在5月份实现了超过10%的同比增长，另有5家预计将从9月起恢复增长。\n\n这5家逆势增长的公司——中国海外发展、金茂、华润置地、中国金茂和招商蛇口——并非靠大量新盘入市，而是依靠**现有项目的去化能力提升**。这意味着在核心城市，那些产品定位精准、品牌信任度高的开发商，正在从竞争对手手中抢走份额。\n\n> \n\n[... middle omitted ...]\n\n7月政治局会议的详细推演感兴趣，欢迎来我们的微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n头部房企5月销售回暖，但利润压力不小\n\n市场在等新盘放量\n\n📌 5月销售数据亮眼，但利润承压是主旋律\n\n最近某外资投行开了场地产策略会，19家房企到场聊了聊。虽然6月二手房成交量环比跌了10%，但投行反而对下半年更乐观了。核心逻辑：销量有韧性、7月低基数、9月新盘集中推、政策面偏暖。\n\n1️⃣ 销售：5家企业前5月销售额同比增超10%\n- 中海、金茂、华润、CICC、招商蛇口表现不错，靠的是核心城市存量项目去化\n- 9月开始更多新盘入市，叠加去年7月低基数，预计有6家房企能延续同比正增长\n- 但行业整体前5月销售额还是跌了15%，主要因为新推盘太少\n\n2️⃣ 土地：供应大幅缩减，优质地块溢价\n- 重点城市土地供应面积同比降32%，创20年新低\n- 前5月上市房企拿地金额同比降48%\n- 中海、金茂、建发、绿城计划下半年土地市场降温时再出手\n- 越秀、保利上半年就很积极，华润在深圳持续拿地\n\n3️⃣ 盈利预警：上半年业绩大概率下滑\n- 中海1H25利润占全年68%，金茂77%，高基数下1H26预计跌35-40%\n- 龙湖、保利置业可能亏损，主要靠卖库存房利润薄\n- 华润相对稳，因为有成都商场REITs上市带来约\n\n[... middle omitted ...]\n\ne, Jinmao & COLI. We are more positive on C&D after its product upgrades, accelerated lands (HZ, Suzhou) & expansion in SZ in Jun.\n\nPositive takeaways — [1] sales: 5 names posted >10% sales gr\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R016",
    "title": "Citi：电池材料6月数据低于预期，但7月已开始修复",
    "digest": "[wechat_article.md]\n# Citi：电池材料6月数据低于预期，但7月已开始修复\n\n这份来自Citi的最新实地调研报告，揭示了一个关键信号：中国电池产业链在经历了6月的生产放缓后，7月正在温和复苏。但更值得关注的是，这个信号背后的结构性含义——它并不等同于需求全面回暖，而是产业链在库存周期和价格预期双重压力下的自我调整。\n\n报告的核心判断是：6月电池产量环比仅增1%，低于此前调研预期的3%，主要受锂价下行趋势和电池厂中报前库存管理影响。但7月头部电池厂商（除中创新航外）的排产预计环比增长5%，恢复了温和增长节奏。Citi认为这合理，因为6-7月本身需求加速不明显，而8月在新增产能和传统旺季（金九银十）支撑下，产量有望进一步提速。\n\n对于产业决策者和投资者，这份报告的价值不在于“6月弱”或“7月修复”这个结论本身，而在于它提供了一个观察产业链真实运行状态的窗口——当数据与预期出现偏差时，偏差背后的驱动因素是什么？这些因素是暂时的还是结构性的？\n\n> **KC评论：** 这份报告最值得看的不是7月环比增长5%这个数字，而是Citi如何在“6月数据低于预期”这个事实基础上，给出了一个既合理又留有谨慎余地的解读框架。完整报告里还有正极、负极、锂盐等各环节的7月排产预测对比图，这些数据比单一电池产量更能反映产业链全貌。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 6月数据低于预期，问题出在库存管理而非需求崩塌\n\n6月电池产量环比仅增1%，与调研预期的3%形成差距。Citi将其归因于两个因素：锂价下行趋势和中报前的库存管理。\n\n这两个因素的本质都是“预期管理”。锂价下行意味着下游厂商有动机推迟采购、降低库存，因为等待更便宜的价格可以改善当期利润表。中报前的库存管理则更直接——在披露半年度业绩之前，主动压缩库存可以减少营运资金占用、改善现金流指标。\n\n[... middle omitted ...]\n\n节排产数据背后的博弈逻辑感兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月电池排产不及预期，7月有望回暖\n\n📊 排产信号：弱中有稳\n\n某外资投行最新调研显示，6月电池月度产出环比仅增长1%，低于此前预测的3%环比增幅。原因主要有两点：锂价下行趋势下企业谨慎排产，叠加中报季前的库存管理。\n\n7月排产怎么看？头部电池厂（不含中创新航）预计环比增长5%，恢复温和增长节奏。考虑到每年6-7月本就是需求淡季，这个增速还算合理。\n\n🔋 关键材料排产分化\n\n1️⃣ **正极材料**：7月排产预计环比+5%\n2️⃣ **负极材料**：7月排产预计环比+6%\n3️⃣ **锂资源**：7月排产预计环比-3%\n\n正负极材料同步回暖，锂资源反而下滑，说明下游采购更倾向于去库存，而非主动补库。\n\n📆 关键时间节点\n\n研报判断，8月电池产出有望加速，主要受益于：\n- 新增产能陆续投产\n- 传统“金九银十”旺季预期\n\n整体来看，当前排产数据偏弱但未失速，产业链正在等待需求端更明确的信号。\n\n大家对下半年电池材料需求怎么看？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n# China Battery Materials\n\n# China Battery Supply Chain on \n\n[... middle omitted ...]\n\n July, resuming a modest growth rate. We think this is reasonable considering demand acceleration is relatively shy during June-July each year, and we estimate the monthly battery output shoul\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R017",
    "title": "Citi：苹果看上长鑫存储，中国DRAM的“全球第四极”叙事就此成立",
    "digest": "[wechat_article.md]\n# Citi：苹果看上长鑫存储，中国DRAM的“全球第四极”叙事就此成立\n\n一份来自《金融时报》的报道，在6月最后一个周末悄然改变了中国半导体产业的一个关键叙事。苹果正在寻求美国政府批准，向中国DRAM制造商长鑫存储（CXMT）采购内存芯片。审批结果尚不可知，但Citi在第一时间发布的研报中给出了一个极其明确的判断：苹果的“考虑”本身，已经是对长鑫存储技术能力最有力的背书。这份背书，足以将长鑫存储从“国产替代故事”升级为“可信的全球第四大DRAM制造商”。\n\n这不是一个关于“能不能获批”的新闻，这是一个关于“市场认知如何被重塑”的拐点信号。对于关注中国半导体产业链的投资者来说，Citi这份报告的核心洞察不在于苹果能否成功，而在于长鑫存储的LPDDR5X产品已经达到10667Mbps的速度，具备了进入高端移动、平板和笔记本应用的资质。苹果的主动接触，意味着这家中国公司在产品可靠性上通过了全球最严苛的消费电子客户的初步筛选。\n\n> **KC评论：** 很多人把注意力放在“美国会不会批准”这个政治博弈上，但Citi的视角完全不同。它告诉我们，苹果的“意向”本身就是一项巨大的信息增量。这意味着长鑫存储的产品在技术指标和良率上已经达到了可以进入苹果供应链的水平。政治审批是一个变量，但技术能力的确认是基本面变化。这个基本面变化，才是驱动供应链公司估值的核心。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 苹果的“意向”比“获批”更重要，它验证了长鑫存储已跨越技术分水岭\n\nCiti报告最值得关注的第一层判断，是它如何看待这则新闻的实质意义。报告明确写道：“Regardless of whether Apple gets the purchase approval, its consideration of CXMT as a \n\n[... middle omitted ...]\n\n，也方便人工快速把握市场动态。欢迎来知识星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n苹果找长鑫存储买内存？\n\n一颗DRAM的认可\n\n苹果想买国产DRAM，这波信号很关键\n\n某外资投行最新研报说，苹果正在寻求美国政府批准，想从长鑫存储（CXMT）采购DRAM内存。这家公司目前被列入美国国防部1260H清单，但苹果主动去谈，本身就是一次“背书”。\n\n这事还没定论，但研报观点很明确：无论批不批，苹果愿意考虑，已经说明长鑫的产品可靠性和技术实力到了全球前三以外的“第四极”水平。\n\n1️⃣ **从“国产替代”到“全球第四”**\n\n过去市场看长鑫，更多是国产替代逻辑。但苹果这种级别的客户愿意把它放进供应链候选名单，意味着它的LPDDR5X（12Gb/16Gb，速度达10667Mbps）已经能跑高端手机、平板和笔记本。\n\n研报认为，这种市场认知转变，比最终能不能拿到苹果订单更重要。\n\n2️⃣ **设备端和封测端跟着受益**\n\n苹果的“兴趣”对长鑫供应链是正面信号。研报特别点名了两类受益方：\n\n- **后端设备**：ASMPT，核心逻辑是先进封装（TCB、光子学）需求上升，行业重心往后端转移\n- **封测代工（OSAT）**：长电科技（JCET）是首选，先进封装收入占比60-70%，具备2.5D、3D、存储\n\n[... middle omitted ...]\n\ne global No.4 DRAM maker’. We expect the news to be positive for CXMT and its supply chain, including the equipment vendors and OSAT providers. Within our coverage we prefer ASMPT and JCET.\n\nA\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R018",
    "title": "GS：DRAM周期正从“涨不涨”切换为“涨多少”",
    "digest": "[wechat_article.md]\n# GS：DRAM周期正从“涨不涨”切换为“涨多少”\n\n2026年6月，当市场还在争论半导体周期是否见顶时，GS发布的最新DRAM情绪指标给出了一个不太一样的信号：整体指向“温和积极”，且与4月持平。\n\n这个结论没有太多惊喜。真正值得关注的，是这份报告内部几个数据点构成的隐含叙事——它们指向一个判断：DRAM周期正在从“价格是否上涨”切换为“上涨的斜率、持续性和结构性分配”。\n\n这不是一个简单的周期延续问题。它意味着投资者需要调整分析框架：过去两年靠“有没有涨价”判断景气度的做法，正在让位于更精细的定价权、需求结构和HBM（高带宽存储器）定价博弈。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. DDR5现货溢价正在重塑合约定价的锚定逻辑\n\n5月以来，DDR5现货价格累计上涨20%，对5月合约价的溢价已达到25%。DDR4的溢价更激进，达到45%。\n\n现货溢价本身并不罕见。但这次的不同在于：DDR5作为新一代主流DRAM，其现货价格正在成为合约谈判的参考锚点，而非传统的合约价引导现货。GS在报告中指出，投资者对2027年HBM定价的预期持续上升，部分原因正是“当前强劲的常规DRAM定价，可能在明年HBM定价谈判中被纳入考量”。\n\n这意味着，DDR5的现货溢价不仅仅是短期供需失衡的信号，它正在向上游传导，重塑整个存储器定价体系。\n\n> **KC评论：** 市场习惯用合约价判断趋势，但合约价是滞后的。DDR5现货溢价持续扩大，意味着下游客户正在为“拿不到货”支付更高溢价。这背后是AI服务器对DDR5的刚性需求，而非投机性囤货。完整报告中的DDR5现货价格走势图（Exhibit 2）值得仔细看，它展示了这一溢价的持续性。\n\n---\n\n![研报原图 2](assets/source_image_02.jpg)\n\n[... middle omitted ...]\n\n提供更清晰的答案：涨价是否正在接近下游的承受极限。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nDRAM 情绪回暖，几个信号值得看\n\nDRAM 回暖了？\n\n5月数据给出积极信号\n\n最近某外资投行更新了6月DRAM情绪指标，整体指向温和正面，和4月持平。几个关键数据点值得关注：\n\n1️⃣ DDR5 现货价格从5月初开始走强，相比5月1日上涨了20%，目前比5月合约价还溢价25%。DDR4 同期也涨了11%，溢价幅度更夸张，达45%。\n\n2️⃣ 中国手机出货量连续两个月同比正增长，5月同比+19%。不过研报提到，团队预计2季度可能因为内存涨价压制需求，出货量同比下滑14%。\n\n3️⃣ 南亚科（Nanya）5月营收同比暴增730%，连续10个月保持三位数增长。主要靠DDR4涨价驱动。\n\n4️⃣ 韩国5月DRAM出口再创历史新高，环比+21%，同比+370%。受益于内存涨价+美国和中国云厂商的强劲需求。\n\n5️⃣ 服务器ODM（广达、纬颖等）5月营收同比+53%，AI服务器和ASIC服务器出货持续放量。\n\n6️⃣ 研报还上调了2027年HBM涨价预期，从同比+14%上调到+44%。理由是当前传统DRAM价格强势，可能会传导到HBM定价谈判中。\n\n整体看，短期DDR5/DDR4现货走强、需求端有支撑，长期HBM预期也\n\n[... middle omitted ...]\n\nto rise, likely due to the expectations that the currently strong conventional DRAM pricing could be taken into account when discussing HBM pricing for next year.\n\nExhibit 1: GS DRAM Sentiment\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "Citi：三星十年1000万亿韩元投资，韩国半导体设备商才是真正的“卖铲人”",
    "digest": "[wechat_article.md]\n# Citi：三星十年1000万亿韩元投资，韩国半导体设备商才是真正的“卖铲人”\n\n当全球市场还在争论AI资本开支何时见顶时，一份来自韩国本土的产业信号正在被低估。\n\n2026年6月29日，三星集团将在青瓦台正式公布一项规模空前的投资计划：未来十年，向半导体与AI领域投入约1000万亿韩元。这不是一个普通的扩产计划。Citi在最新发布的研报中明确指出，这笔投资的核心受益者并非三星电子本身，而是一批韩国半导体设备制造商——Wonik IPS、TES、Eugene Technology、TechWing等。\n\n市场讨论AI芯片、讨论HBM、讨论先进封装，但真正决定这些技术能否落地的，是制造设备。而韩国正试图通过国家意志，把半导体设备供应链的主动权留在本土。\n\n这份报告的真正价值，不在于告诉你三星要花多少钱，而在于揭示了三个被市场忽视的结构性变化：第一，韩国政府正在用“国家项目”的框架加速半导体产业地理重塑；第二，三星的投资节奏被大幅前置，Yongin集群的完工时间从2048年提前至2034-2035年；第三，Citi对韩国设备商的估值逻辑，已经隐含了一个“多年代际向上周期”的假设。\n\n以下是我们从Citi这份报告中提炼出的核心判断与关键追问。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这笔投资不是“三星的”，而是“青瓦台的”——产业地理重塑正在改变供应链逻辑\n\nCiti在报告中反复提及一个关键背景：青瓦台将于6月29日宣布“韩国大跃进的三大超级项目”，其中核心是在湖南地区建立半导体集群。三星的投资计划，是配合这一国家战略的落地。\n\n具体来看，1000万亿韩元的投向分布如下：约360万亿韩元用于龙仁半导体集群的6座晶圆厂，约300万亿韩元用于光州和全罗南道的4-5座晶圆厂，超过350万亿韩元用于牙山AI数据中心，超\n\n[... middle omitted ...]\n\n细估值模型、风险收益比，以及韩国半导体供应链的全球竞争格局。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n三星砸1万万亿布局半导体\n\n韩国半导体大棋局\n\n三星未来十年投资超1千万亿韩元\n\n---\n\n最近韩国媒体爆料，三星集团将在6月29日的国家简报会上宣布一项重磅计划：未来十年投入约1,000万亿韩元，主攻半导体和AI！\n\n这个规模有多大？拆开看更清楚：\n\n📍 龙仁集群：6座晶圆厂，约360万亿韩元\n📍 光州·全罗南道：4-5座晶圆厂，约300万亿韩元\n📍 忠清地区：封装研发+生产基地，超56万亿韩元\n📍 牙山：AI数据中心，超350万亿韩元\n\n而且龙仁工厂的完工时间从2048年提前到2034-2035年，明显在提速。\n\n这波是韩国“三大超级项目”的一部分，政府主导、企业跟进。SK集团6月30日也要在光州发布西南地区投资计划，三星7月2日继续在牙山办投资说明会。\n\n投行研报认为，这种政府+财阀的联合发力，会持续推动韩国半导体供应链增长。看好韩国半导体设备商，尤其是受益于AI需求和新建厂计划的标的。\n\n📌 重点关注标的（研报观点）：\n• Wonik IPS / TES / Eugene Technology：前道设备商\n• TechWing：后道设备商，HBM测试设备是关键\n\n比如Eugene Technology\n\n[... middle omitted ...]\n\n the promising AI demand outlook and accelerated green-field capacity expansion plans.\n\nSamsung Group to Invest \\~W1,000tr Over the Next Decade Mainly on Semiconductor & AI – According to dome\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R020",
    "title": "GS：中国楼市正在走出“政策底”，但真正的考验在供给端",
    "digest": "[wechat_article.md]\n# GS：中国楼市正在走出“政策底”，但真正的考验在供给端\n\n中国房地产市场在2026年6月最后一周交出了一份让市场意外但又不敢轻信的答卷。GS最新一期周度数据显示，端午假期后，新房和二手房交易量分别环比反弹38%和27%，双双超越节前6月周均水平。这份反弹在数据层面干净利落，但真正让专业投资者需要停下来思考的，不是“涨了多少”，而是“涨在哪个结构里”。\n\n新房同比仍跌17%，二手房同比转正至+6%；上半年新房累计成交同比下滑14%，而二手房几乎持平。这组数字背后，中国楼市正在经历从“规模驱动”到“存量主导”的不可逆切换。GS这份周报的核心判断可以浓缩为一句话：市场情绪在边际修复，但资产定价仍处于历史低谷，真正的胜负手不在需求端，而在供给端的出清节奏。\n\n> **KC评论：** 这份报告最值得关注的不是单周反弹，而是二手房已经连续多月跑赢新房。这意味着中国房地产市场的定价权正在从开发商转向业主和流通环节。贝壳这类平台的价值逻辑，可能比开发商更值得重新审视。完整报告中对贝壳2Q26 GTV的测算，恰恰指向了这一结构性变化的量化证据。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 交易量反弹确认了“政策底”，但新房与二手房的分化才是真正的信号\n\nGS周报覆盖的约75个城市数据显示，第26周新房成交面积环比增长38%，但同比仍下降17%。二手房表现更为强劲，环比增长27%，同比转正至+6%。更关键的是，二手房上半年累计成交同比持平，而新房则下滑14%。\n\n这种分化并非短期波动。从GS提供的长周期对比看，2026年上半年新房成交较2024年同期低15%，较2023年低43%；而二手房较2024年高18%，较2023年高10%。两组数据放在一起，结论清晰：中国住房需求并未消失，但正在大规模向存量市场迁移。\n\n背后的驱动力不\n\n[... middle omitted ...]\n\n们在微信上的讨论群，一起追踪中国房地产市场的每一次关键变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月地产数据回暖，但别急着下结论\n\n**成交量反弹了**\n\n节后新房/二手房成交环比+38%/+27%，超过节前6月周均水平24%/3%。\n\n**1. 新房还在“去库存”节奏**\n\n6月新房成交同比-17%，上半年累计同比-14%。供应端也在收缩，6月新推盘量环比-3%、同比-16%。\n\n**2. 二手房的韧性更强**\n\n6月二手房成交同比+6%，上半年累计同比持平。中介的价格乐观情绪在上升，但房东端还不明显。\n\n**3. 库存压力在缓解**\n\n20城库存环比持平，去化周期27.3个月，低于5月均值28.5个月。\n\n**4. 政策端在加码**\n\n河南、海南发布城市更新方案：河南重点推进城中村改造、2005年前老旧小区改造，目标2030年新增5万套保障性租赁住房；海南计划“十五五”期间投入1400亿用于城市更新，2026年投资220亿。\n\n**5. 竣工和开工还在降**\n\n某外资投行跟踪模型显示，6月竣工同比-20%，新开工同比-20%以上，上半年整体压力仍在。\n\n**6. 板块估值在历史低位**\n\n覆盖的央国企开发商股价周跌6%，当前股价较2026年末NAV折价42%（港股）/36%（A股），P/B约0.4倍\n\n[... middle omitted ...]\n\no be renovation focus. Acquisition of completed housing inventory for affordable housing usages was also promoted, aiming to add over 50,000 units of affordable rental housing by 2030. 2) For \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R021",
    "title": "摩根斯坦利：MS：中国需求真的在拖累矿业吗？数据告诉你答案",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国需求真的在拖累矿业吗？数据告诉你答案\n\n当大多数市场参与者将目光聚焦于中国房地产的持续疲软和国内消费的放缓时，一份来自MS的月度矿业报告揭示了一个更为复杂的图景：中国经济的“两速”分化正在重塑全球大宗商品的定价逻辑。出口驱动的生产端依然坚挺，而国内消费和投资却在持续走弱。对于矿业投资者而言，这意味着简单的“中国需求强则矿业强”的框架已经失效，取而代之的是一场关于结构性分化的精准博弈。\n\n这份报告的核心判断是：尽管中国宏观环境出现软化迹象，但特定商品——尤其是铝和铜——正受益于供给端的约束和结构性需求（如电网、AI算力基础设施），而铁矿石和钢铁则深陷房地产和基建的泥潭。投资者需要从“看中国总量”转向“看商品个体”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 房地产的“余震”仍在，但最坏的时刻可能尚未到来\n\nMS的数据显示，5月份中国新开工面积同比下降24.7%，虽然较4月的-27.1%略有收窄，但销售面积（GFA sold）的降幅却从-10.3%扩大至-14.1%。更令人担忧的是，该机构的中国房地产团队预计三季度将更加疲弱。高能级城市的二手房实时销售数据自5月中旬开始走弱，且近期加速下滑。\n\n> **KC评论：** 市场普遍认为房地产已经触底，但这份报告给出了相反的信号——政策效果正在递减，积压需求已经释放完毕，而新的可售资源在减少。这意味着三季度地产相关的大宗商品需求可能面临二次探底，而不是温和复苏。完整报告中对房地产“余震”的量化分析值得深入阅读。\n\n报告进一步指出，固定资产投资（FAI）5月同比下降12.5%，较4月的-9.4%进一步恶化。公路FAI下滑13.8%，反映出基建项目的“空窗期”——一季度前置发力后，项目储备出现断层。这与政府债券发行放缓相互印证，表明短期内财政刺激的\n\n[... middle omitted ...]\n\n迎来我们的星球微信群里继续讨论，一起追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国五月数据：经济慢下来了\n\n📊 最新数据速读\n\n5月经济信号很明确：出口制造还行，内需消费投资都在走弱。零售数据转负，地产依旧脆弱。\n\n1️⃣ 地产是最大拖累\n- 新开工面积同比-24.7%（4月-27.1%）\n- 销售面积同比-14.1%（4月-10.3%）\n- 研报团队预计3季度会更弱，高线城市二手房从5月中旬开始明显降温\n\n2️⃣ 工业品分化明显\n- 粗钢产量同比-2.7%，表观消费-8.5%\n- 铝产量同比+1.7%，产能接近天花板\n- 水泥产量同比-8.1%，价格持续疲软\n- 煤炭产量同比-1.7%，矿难后安全管控收紧\n\n3️⃣ 贸易数据有亮点\n- 铝出口同比+16%，创近一年半新高\n- 铁矿石进口98Mt，港口库存开始下降\n- 煤炭进口同比-8%，但价差重新打开\n\n4️⃣ 政策预期\n- 二季度GDP预计4.4%\n- 三季度可能加大财政支出，重点在AI算力、数据中心、智能电网\n\n你们觉得地产什么时候能企稳？欢迎一起讨论\n\n#学习笔记\n\n[source_mineru.md]\nJune 28, 2026 07:57 PM GMT\n\n# Australia Materials | Asia Pacifi\n\n[... middle omitted ...]\n\nre FAI slump reflect a project-pipeline lull post-1Q front-loading. They see 2Q GDP tracking at 4.4% YoY, and expect policy to step up capex-focused fiscal rollout from 3Q, particularly suppor\n\n[... middle omitted ...]\n\nkel Industries (NIC.AX)</td><td>E (04/09/2025)</td><td>A$0.90</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R022",
    "title": "摩根斯坦利：MS：奢侈品最危险的阶段已过，但反弹不会普照所有人",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：奢侈品最危险的阶段已过，但反弹不会普照所有人\n\n纽约的投资者正在重新打量欧洲奢侈品。在上周MS于纽约举办的投资人会议上，超过20位机构投资者密集讨论了LVMH、历峰、爱马仕、法拉利、开云、Inditex和阿迪达斯。讨论的核心不再是“要不要买奢侈品”，而是“买谁，以及为什么现在”。\n\n这份研报传递的最关键信号是：奢侈品板块的情绪正在从“全面回避”转向“选择性进场”。但这不是一个普涨的信号。MS团队发现，多头和空头在每一个名字上都形成了清晰的对峙线，而胜负手取决于三个变量：中国市场的恢复节奏、美国财富效应能否持续外溢，以及香奈儿这个19亿美元营收的巨兽究竟是在做大蛋糕还是切分蛋糕。\n\n对于产业决策者和投资人而言，现在需要做的不是判断板块整体是否触底，而是识别哪些品牌在下一轮周期中拥有不可复制的结构性优势。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 纽约投资者的新共识：科技财富的外溢效应是奢侈品最真实的短期催化剂\n\nMS团队在纽约一周的密集会面中，观察到最显著的变化是：投资者开始认真考虑将资金从过度集中的科技组合中分散到非科技板块，而奢侈品是这一“财富效应外溢”最直接的受益者。\n\n报告特别提到韩国市场——那里呈现出最清晰的“AI财富-个人奢侈品消费”相关性。中东市场的重新开放和国际旅行的再加速也被视为重要的正向催化剂。这些信号叠加起来，构成了一个相对完整的短期叙事：全球高净值人群的财富池在扩大，而奢侈品是这些新增财富最自然的流向之一。\n\n但这份研报的可贵之处在于，它没有停留在情绪层面。MS团队明确指出，虽然情绪确实在改善，但离“一致看多”还有距离。空头方提出的三个质疑至今没有得到满意回答：第一，没有中国，这个板块还能不能转？第二，没有中产消费者，头部品牌还能不能维持增长？第三，在一个行业增速只\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n奢侈品现在能看了吗\n\n华尔街开始聊奢侈了\n\n纽约投资人正在重新关注奢侈品\n\n上周某外资投行在纽约跟20多家机构聊了一圈，发现一个有意思的信号：科技股涨得太集中，大家开始琢磨要不要往非科技板块挪一点钱。\n\n其中奢侈品是被反复提到的方向。逻辑很直接——科技带来的财富效应，最终会溢出到消费上。韩国就是个典型例子，AI造富和奢侈品消费的关联度已经非常清晰。\n\n🧠 几个关键观察：\n\n1️⃣ **LVMH 被当成“默认首选”**\n多头觉得它是四大奢侈品集团里最稳妥的选择。爱马仕太贵太拥挤，历峰有点结构性隐忧，开云还在反转期。LVMH二季度F&LG部门销售预期最近5周首次被上调，虽然幅度不大（从0%到2%），但方向变了。Dior也预计转正，这将是近三年首次。\n\n2️⃣ **爱马仕在跌，但有人觉得是机会**\n当前33.8倍PE，远低于10年均值44.5倍。多头认为非皮具品类增速放缓是周期性的，爱马仕的长期优势恰恰在于能吸引中产消费者而不稀释品牌。但空头担心它正在向香奈儿让出市场份额，而且配货比在下降——这是个结构性问题。\n\n3️⃣ **历峰是全场最热的票**\n几乎没有空头。新CEO上任改善了公司治理，卡地亚和梵克雅宝在珠宝赛\n\n[... middle omitted ...]\n\nstors for almost an entire week). One of the arguments often mentioned during our meetings was the willingness to potentially deploy new money to non tech sectors (as portfolios have become in\n\n[... middle omitted ...]\n\n Ferragamo Spa (SFER.MI)</td><td>U (02/12/2026)</td><td>€10.81</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R023",
    "title": "摩根斯坦利：MS：GlassBridge不是AI光模块的敌人，但FAU厂商的护城河正在变浅",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：GlassBridge不是AI光模块的敌人，但FAU厂商的护城河正在变浅\n\nAI数据中心的光互联赛道，正在经历一次技术路线的微妙转向。2025年9月就已经出现在行业视野中的一项技术——康宁的GlassBridge玻璃光互连组件，在2026年6月正式发布后，引发了市场对CPO（共封装光学）产业链的重新定价。\n\nMS在最新发布的研报中给出了一个层次分明的判断：GlassBridge对现有FAU（光纤阵列单元）制造商构成潜在颠覆，但对AI光模块公司的直接影响在未来1-2年内非常有限。这个结论看似平衡，但真正值得深挖的是它背后隐含的产业逻辑变化——当光纤直接耦合到光子集成电路（PIC）成为可能，传统的光纤组装方案在密度、可扩展性和可拆卸性上的劣势正在被技术演进所放大。\n\n这份报告的核心价值不在于告诉你“谁赢谁输”，而在于它揭示了一个更根本的问题：在AI数据中心向更高带宽、更低功耗演进的过程中，光学互连的物理瓶颈正在从“能不能做”转向“怎么做得更密、更省、更可维护”。而GlassBridge的出现，恰恰是对这一转向的技术回应。\n\n> **KC评论：** MS的这份报告值得细读的地方在于，它没有简单地把GlassBridge定义为“颠覆者”或“过客”，而是给出了一个动态的时间框架——短期对光模块公司影响有限，中期对FAU厂商构成结构性挑战。这种分时间维度的判断，在技术分析中比“利好/利空”的二元结论更有参考价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. GlassBridge不是突然出现的黑天鹅，而是康宁100亿美元光子学计划的一部分\n\n市场对GlassBridge的担忧，很大程度上源于对新技术突然出现的恐慌。但MS在报告中明确指出，这项技术早在2025年9月就有媒体报道，并非全新概念。更重要的是\n\n[... middle omitted ...]\n\ne的产业化进程，拆解它对AI光模块和FAU产业链的真实影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n玻璃桥技术来了，FAU厂商有压力吗\n\n封面：玻璃桥技术解析\n\n副标题：对AI光模块的影响有多大？\n\n某外资投行最新研报拆了Corning的GlassBridge技术，聊聊它对AI光模块和FAU厂商的影响。\n\n1/ 什么是GlassBridge？\nCorning在6月24日首尔会议上正式发布了GlassBridge，它是一种玻璃基光纤到PIC的连接平台。简单说，就是把光纤直接连到光子集成电路（PIC）上，跳过传统的长光纤组件。\n\n2/ 对FAU厂商的冲击\n传统光纤阵列单元（FAU）在高密度场景下组装复杂、扩展困难。GlassBridge作为晶圆级、被动对准的替代方案，支持更高密度和可拆卸集成。研报判断：在CPO（共封装光学）演进中，FAU厂商面临被颠覆的风险。\n\n3/ 对AI光模块公司影响有限\nGlassBridge在CPO和NPO（近封装光学）中都能用。研报认为未来1-2年对AI光模块公司影响很小，因为NPO的广泛应用可能抵消CPO带来的风险。\n\n4/ 时间线仍不确定\n这不是全新概念——2025年9月就有消息，Corning在分析师日也提过100亿美元光子学目标。但实际商用时间表未定，导致FAU相关公司股价波\n\n[... middle omitted ...]\n\n uncertain, resulting in volatility for companies with high option value from FAU.\n\nOn June 24, Corning officially launched its GlassBridge glass optical interconnect assembly at the AI Data C\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$348.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R024",
    "title": "摩根斯坦利：MS：奢侈品行业正在经历一场“有条件的回暖”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：奢侈品行业正在经历一场“有条件的回暖”\n\n纽约的投资者正在重新审视奢侈品。但这一次，他们的热情带着明确的条件句。\n\nMS上周在纽约举办了超过20场投资者会议，覆盖了欧洲消费品板块中奢侈品、运动服饰、零售和眼镜等子行业。结论并不简单：看多情绪在升温，但远非一致。最值得关注的变化是什么？报告指出，投资者首次对LVMH核心部门F&LG（时尚与皮具）的2Q26销售预期在过去五周内出现了上调——这是数月来的第一次。虽然幅度不大（从接近0%的同店增长上调至约2%），但方向性转变本身就是一个信号。\n\n但与此同时，反对的声音同样有力：没有中国，这个行业能行吗？没有中产阶级消费者，LV和Gucci还能维持增长吗？在一个全行业增速仅为约+2%（固定汇率）的背景下，年营收190亿美元的Chanel到底是在做大蛋糕，还是在抢别人的份额？\n\n这份报告的价值不在于给出一个“买还是卖”的简单答案，而在于它清晰地勾勒出了当前奢侈品投资的核心矛盾——行业正在从“普涨”切换到“精选”阶段，而每一家公司的叙事都将被严格审视。\n\n> **KC评论：** MS的这份调研报告，本质上是一次对“市场情绪温度计”的精确测量。它告诉我们，华尔街的机构资金正在从“全面回避”转向“选择性下注”。但这个选择的标准非常苛刻——不再是“谁的故事好听”，而是“谁的数据能兑现”。完整报告里关于各家公司2Q26的sell-side与buy-side预期对比图表，是理解这种“预期差”的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nLVMH被多数投资者视为“奢侈品四大天王”中的默认多头。原因很直接：历峰被认为估值过高且过于拥挤，爱马仕首次面临潜在的结构性问题，开云则是一个充满风险的转型故事。LVMH成为\n\n[... middle omitted ...]\n\n势反转？这些问题，只有在完整的数据和持续跟踪中才能找到答案。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n奢侈品的“牛市”信号来了？聊聊最近机构在讨论什么\n\n**🧐 奢侈品的拐点到了吗？**\n\n最近跟几家外资投行的分析师聊了一圈，发现纽约的机构投资者们对欧洲奢侈品板块的热情明显升温。上周我们密集见了20多家投资者，讨论最集中的就是LVMH、爱马仕、历峰这些名字。\n\n**1/ 为什么突然开始关注奢侈品？**\n\n核心逻辑有两个：\n- 科技股涨太多了，组合越来越集中，大家开始想往非科技板块挪钱。\n- 科技创造的“财富效应”正在溢出到奢侈品消费——韩国就是最典型的例子，AI带动的财富增长直接拉动了个人奢侈品支出。\n\n**2/ LVMH：最“安全”的默认选项**\n\n在四大奢侈品集团里，LVMH被很多投资者当作“默认做多”的选择。\n- 爱马仕太贵太共识\n- 历峰可能第一次面临结构性挑战\n- 开云还在转型期\n\n关键是，LVMH的F&LG（时装皮具）部门的销售预期在最近五周首次开始上调——虽然只是从0%到+2%的改善，但这是个象征性的转折点。\n\n**3/ 爱马仕：是机会还是陷阱？**\n\n看多的人说：现在33.8倍的远期PE，比过去10年平均的44.5倍便宜太多了，是个不错的进场点。\n看空的人说：爱马仕正在面临结构性挑战——消费者\n\n[... middle omitted ...]\n\nstors for almost an entire week). One of the arguments often mentioned during our meetings was the willingness to potentially deploy new money to non tech sectors (as portfolios have become in\n\n[... middle omitted ...]\n\n Ferragamo Spa (SFER.MI)</td><td>U (02/12/2026)</td><td>€10.81</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "摩根斯坦利：MS：GlassBridge不是AI光模块的利空，但FAU厂商的护城河正在变窄",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：GlassBridge不是AI光模块的利空，但FAU厂商的护城河正在变窄\n\n2026年6月24日，康宁在首尔一场AI数据中心光通信技术会议上正式发布了GlassBridge。这个看起来像玻璃基板互联组件的产品，在随后的几个交易日里引发了市场对AI光模块和光纤阵列单元（FAU）厂商的重新定价。部分FAU相关标的出现了明显波动，光模块公司也受到波及。\n\nMS在最新发布的研报中给出了一个清晰但容易被市场误读的判断：GlassBridge对AI光模块公司的影响在未来1-2年内极为有限，但它对FAU厂商的长期技术路线确实构成了实质性挑战。这份报告的价值不在于确认了“新技术出现”，而在于它帮助投资者区分了真正的结构性风险与短期的情绪误判。\n\n市场往往高估新技术的短期冲击，同时低估其长期重塑供应链的能力。MS的分析框架正好提供了这样一个分层视角。\n\n> **KC评论：** 这份研报最值得读的部分并不是结论本身，而是它如何用“时间窗口”和“应用场景”两个维度来拆解同一个技术对不同公司的差异化影响。完整报告中有几张关键图表，展示了GlassBridge在CPO和NPO两种架构下的渗透路径，这些细节是理解风险定价的核心。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. GlassBridge的本质不是替代光模块，而是改变光纤与芯片的连接方式\n\n要理解GlassBridge的影响，首先要搞清楚它到底解决了什么问题。传统的光模块架构中，光纤通过一个较长的光纤阵列单元（FAU）连接到光子集成电路（PIC）。FAU本质上是一个精密的光纤排列与固定组件，它负责将多根光纤精确对准到PIC上的光波导接口。随着数据中心对带宽密度的要求指数级上升，单根光纤的传输速率在提升，但同时需要连接的光纤数量也在暴增。FAU在高光纤数场景下变\n\n[... middle omitted ...]\n\n题的产业决策者和投资者一起，持续追踪这一技术变革的演进路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nGlassBridge来了，FAU厂商有点慌\n\n光互联新变量\n\n某外资投行最新研报解析了一项新光学技术——GlassBridge。它由康宁在6月正式发布，本质上是一种“光纤直连PIC”的互联方案，可能改变AI光模块和光纤阵列（FAU）的竞争格局。\n\n**1. GlassBridge是什么？**\n它直接把光纤对准光子芯片（PIC），而不是像传统方案那样通过长长的光纤阵列再连接。优点是：密度更高、更易规模化、支持可拆卸系统集成。\n\n**2. 对FAU厂商是利空？**\n是的。研报指出，在CPO（共封装光学）演进中，GlassBridge可能颠覆现有FAU技术路线。传统FAU在超高光纤数下组装复杂，而GlassBridge是晶圆级、被动对准方案，更适合未来需求。\n\n**3. 对AI光模块厂商影响有限**\n因为GlassBridge既可用于CPO，也可用于NPO（近封装光学）。如果NPO应用更广，反而能对冲CPO对光模块的潜在冲击。所以未来1-2年影响很有限。\n\n**4. 时间表还不确定**\n研报强调：GlassBridge早在2025年9月就有消息，康宁在分析师日也将其纳入100亿美元光子学目标，但真正商用时间表仍不\n\n[... middle omitted ...]\n\n uncertain, resulting in volatility for companies with high option value from FAU.\n\nOn June 24, Corning officially launched its GlassBridge glass optical interconnect assembly at the AI Data C\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$348.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "NOM：人民币中间价模型指向6.79，但逆周期因子才是真正的胜负手",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型指向6.79，但逆周期因子才是真正的胜负手\n\n当市场还在为美元走势争论不休时，一份来自NOM亚洲外汇策略团队的报告，给出了一个值得中国资产持有者认真对待的信号。\n\n这份由Craig Chan领衔发布的研报，核心是一个技术性极强的判断：NOM的人民币中间价预测模型显示，最新一期的模型预测值为6.7882，较此前的6.8175低了293个基点。换言之，模型本身指向人民币升值。但报告同时给出了另一个数字——引入逆周期因子调整后的预测值为6.7965，仅比前次官方中间价低210个基点。这47个基点的差异，就是政策意图与市场力量之间的博弈空间。\n\n对于任何关注人民币资产定价的人来说，这组数字传递的信息远比表面看起来丰富。它意味着，如果完全由模型驱动，人民币汇率本应走得更强；但政策层面通过逆周期因子，正在有意识地放缓这个节奏。\n\n这不仅仅是一个汇率预测的更新，它实际上是理解当前中国宏观经济政策框架的一个窗口。在出口承压、内需修复尚不稳固、外部地缘不确定性持续的背景下，人民币汇率的管理逻辑已经从“单向升值”转向了“区间稳定”与“预期管理”并重。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型与现实的差距，暴露了政策层的核心关切\n\nNOM报告中最引人注目的，不是预测值本身，而是模型预测与引入逆周期因子后预测值之间的差额。这47个基点的差距，本质上是一个“政策溢价”。\n\n理解这一点，需要先明白逆周期因子的作用机制。它不是一个公开透明的公式，而是央行在每日中间价报价模型中引入的一个调节参数。当市场情绪过度悲观、人民币面临单边贬值压力时，逆周期因子会被用来引导中间价走强，以稳定预期；反之，当市场情绪过于乐观、人民币升值过快时，它也可以被用来抑制升值速度。\n\nNOM报告给出的数据表明，当前阶段，\n\n[... middle omitted ...]\n\n果你对这些问题感兴趣，欢迎来星球微信群里继续讨论。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，外资投行怎么看\n\n📊 最新模型预测\n\n某外资投行刚更新了亚洲（除日本）外汇研报，核心看点是人民币中间价预测。\n\n模型显示，最新预测值为6.7882，比上次预测低293个基点，比官方收盘价低47个基点。如果加入逆周期因子，预测值调整到6.7965，比上次定盘价低210个基点。\n\n简单说，研报认为人民币中间价有进一步走低的可能。\n\n🔍 三个关键逻辑\n\n1️⃣ 模型调整方向明确\n从6.8175调到6.7882，幅度不小。逆周期因子虽然会平滑波动，但方向没变。\n\n2️⃣ 近期走势验证\n研报附了近期模型误差图（未含逆周期因子），说明模型在跟踪实际走势上有一定准确度。\n\n3️⃣ 下半年事件密集\n研报列出了几个重要时间节点：\n- 7月底：政治局经济工作会议\n- 10月：国庆黄金周\n- 11月：APEC深圳会议\n- 12月：中央经济工作会议+政治局会议\n- 年底：中美高层会晤\n\n这些事件都可能成为汇率波动的催化剂。\n\n📌 一点思考\n\n模型预测只是参考，实际走势要看政策组合拳。逆周期因子的存在，说明管理层对汇率稳定有明确诉求。\n\n下半年事件密集，汇率弹性可能会加大，但大幅单边贬值的概率不高。\n\n欢迎一起讨论你对下\n\n[... middle omitted ...]\n\n171096f23070dc60a59ecaa1512a0cf1fb865cb77e213ac9.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/103b34d6f01ca8350c5d94c95d4e6da0a8353\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R027",
    "title": "Citi：AI缺的不是算力，是变压器和燃气轮机",
    "digest": "[wechat_article.md]\n# Citi：AI缺的不是算力，是变压器和燃气轮机\n\n全球AI军备竞赛正在遭遇一个意想不到的瓶颈：不是芯片，不是算法，而是变压器、燃气轮机和开关柜。Citi在2026年6月发布的这份名为《Overcoming Gridlock 2.0》的重磅报告中，给出了一个核心判断：电力基础设施的供应瓶颈，正在从根本上改变AI数据中心建设的选址逻辑、技术路线和商业模型。而市场对这一瓶颈的持续时间和规模，仍然存在系统性低估。\n\n报告提到，全球已有超过2500GW的可再生能源、储能和大型负荷项目在电网并网排队中停滞。仅电网投资一项，到2030年每年就需要增加约4000亿美元。这不是一个周期性问题，而是一个结构性缺口。\n\n这份报告的核心价值不在于罗列数据，而在于它提供了一个完整的分析框架：当“速度优先”成为电力获取的第一原则时，整个产业链的赢家和输家将被重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电力瓶颈正在重塑AI数据中心的选址逻辑，得天然气者得天下\n\n传统上，数据中心的选址取决于网络延迟、土地成本和税收优惠。但Citi报告揭示了一个更底层的变量：电力获取的速度。\n\n报告明确指出，“速度优先”正在推动从集中式电网向分布式系统的转变。“自带发电”（BYOG）模式，尤其是基于美国天然气的自备供电，正在成为主流。这不是一个边缘趋势，而是核心逻辑的切换。\n\nCiti全球能源业务负责人Cathy Shepherd在报告访谈中透露，能源公司正在直接与超大规模云服务商合作，将数据中心选址在现有天然气资源和基础设施附近。这解释了一个现象：为什么得克萨斯州成为AI数据中心建设的焦点——不是因为它的网络，而是因为它紧邻二叠纪盆地。\n\n> **KC评论：** 这意味着，未来几年美国数据中心的增量电力需求，将主要由天然气满足。但这不是一个简\n\n[... middle omitted ...]\n\n的知识星球和微信群继续讨论，一起追踪电力瓶颈下的产业链重塑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心电力困局：AI背后的电网瓶颈\n\n**封面短标题：** 电网瓶颈深度拆解\n\n**封面副标题：** 当AI算力撞上电力基础设施天花板\n\n---\n\n**1. 电力需求正在“突然爆发”**\n\nAI数据中心是这轮电力需求增长的核心推手。某外资投行最新研报指出，AI驱动的数据中心电力需求，将从2023年的4.3GW（约占12%）飙升至2030年的约110GW（占比70%）。这不是线性增长，而是指数级跃迁。\n\n与此同时，能源安全焦虑加速了可再生能源和电动车的普及，进一步挤压本已紧张的电网容量。\n\n**2. 最大的瓶颈不在发电，在输配电**\n\n研报揭示了一个关键矛盾：全球有超过2500GW的可再生能源、储能和大型负荷项目滞留在电网并网队列中。\n\n核心瓶颈是硬件设备——大型电力变压器、高压开关柜、发电机升压变压器等。这些关键设备的交货周期已拉长到24-48个月，部分甚至长达3-4年。价格方面，大型变压器在过去五年上涨了约80%，需求自2019年以来增长了270%以上。\n\n**3. “自带发电”成为新常态**\n\n由于电网扩容速度跟不上需求，“自带发电”（BYOG）模式正在美国快速普及。开发商直接在数据中心旁边建天然气发电\n\n[... middle omitted ...]\n\ng\n\nCathy Shepherd\nGlobal Head of Energy\nCiti Corporate Banking\n\nJP Coviello\nHead of Portfolio Strategy\nChief Investment Office, Citi Wealth\n\nHobey Kuhn\nMacro Portfolio Strategist\nChief Investm\n\n[... middle omitted ...]\n\n in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.</td></tr><tr><td colspan=\"2\">ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST</td></tr></table>"
  },
  {
    "id": "R028",
    "title": "GS：供应链拥堵已回到疫情前，但真正的考验还没来",
    "digest": "[wechat_article.md]\n# GS：供应链拥堵已回到疫情前，但真正的考验还没来\n\n全球供应链的核心矛盾，正在从“能不能运”转向“运了有没有人买”。GS最新一期供应链拥堵指数（GS Supply Chain Congestion Scale）给出了一个看似平淡、实则意味深长的读数：截至2026年6月29日当周，周度拥堵指数环比下降7%，瓶颈规模连续维持在“2”的水平——这个数字，已经基本回到了2020年2月疫情爆发前的基准线。\n\n这不是一个“一切恢复正常”的信号。这是一份提醒市场重新定义“正常”的报告。\n\n当拥堵指数从2021年底/2022年初的峰值“10”一路回落到“2”，市场早已不再讨论港口瘫痪、一箱难求。但GS在报告末尾埋下了一个关键追问：关税和地缘政治冲突将如何影响货运需求、时间节奏以及全球贸易的再平衡？如果供应链压力继续缓解，指数有可能在2026年更稳定地进入“1”区间——那意味着，我们正在进入一个“后拥堵时代”的全新博弈。\n\n> **KC评论：** GS这份周报的核心价值不在于告诉你“拥堵缓解了”——这件事市场已经price in。真正值得细读的是，当物理瓶颈消失后，哪些运输子行业会成为新的风向标。报告专门列出了“拥堵保持低位时值得关注的运输子板块”，但并没有给出完整结论。这正是需要深入阅读的地方。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 西海岸铁路联运量加速增长，但速度指标仍在恶化\n\n最值得关注的信号来自美国西海岸的铁路网络。GS追踪的两大一级铁路公司——联合太平洋（UNP）和伯灵顿北方圣塔菲（BNSF）——的联运量同比增速在6月最后一周进一步加速至14%，高于前一周的11%。其中BNSF达到15%，UNP为12.5%。\n\n但矛盾的是，铁路的运营质量指标并未同步改善。UNP的终端停留时间从19.4小时小幅上升至19.9小\n\n[... middle omitted ...]\n\n星球和微信群中继续讨论，一起追踪这些关键信号背后的趋势演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国供应链到底松了没？最新数据来了\n\n📊 供应链拥堵指数更新\n\n某外资投行最新研报显示，截至6月29日当周，美国供应链拥堵指数环比下降7%，拥堵等级维持在“2”级（峰值是10级），基本回到疫情前水平。\n\n—————————————————\n\n🔍 几个关键数据点：\n\n1️⃣ 西海岸等待卸货的集装箱船数量维持在1艘（已连续多周低位），但东海岸积压从3艘上升至4艘，值得关注。\n\n2️⃣ 西海岸铁路联运量同比增速加快至+14%（前值+11%），说明货运需求仍在。\n\n3️⃣ 底盘停留时间小幅上升：20英尺集装箱从4.4天→5.1天，40/45英尺从6.3天→6.5天。\n\n4️⃣ 亚洲→美西航线运费环比大涨19%，同比转正至+3%，这是近期少见的上涨。\n\n—————————————————\n\n📌 研报核心判断：\n\n如果供应链压力继续缓解，指数有望在2026年更稳定地维持在“1”级区间。但关税和地缘冲突对货运需求的影响仍是关键变量。\n\n—————————————————\n\n💡 个人观察：\n\n运费环比大涨19%是个信号，可能反映旺季前补库需求。但整体数据看，供应链已从“高度紧张”回到“接近正常”，和2021-2022年完全不\n\n[... middle omitted ...]\n\n/w; Exhibit 2). For this week’s scale and index, the number of container ships waiting to dock and unload goods along the West Coast remained unchanged at 1, while backlogs along the East Coas\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R029",
    "title": "摩根斯坦利：MS：AI ASIC正在取代GPU，成为亚洲最值得下注的赛道",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI ASIC正在取代GPU，成为亚洲最值得下注的赛道\n\n这份MS最新发布的“Three Actionable Ideas”报告，表面上给出了三只风格迥异的个股推荐——一家台湾芯片设计服务商、一家日本汽车半导体巨头、一家印度多元化企业集团。但把这些看似分散的机会放在一起看，一个清晰的共同主线浮出水面：AI基础设施的下一波增长，正从通用GPU转向定制化ASIC，而亚洲供应链中那些能够承接这种结构性转移的公司，正在获得超出市场预期的定价权。\n\n这不是一个关于“AI概念股”的故事。这是一个关于算力需求从训练侧向推理侧迁移、从通用向专用转移、从美国向亚洲供应链深度扩散的产业逻辑。MS在这份报告中，用三只看似无关的个股，拼出了一张AI基础设施投资的完整地图。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI ASIC的长期增速正在超越GPU，设计服务商成为最大受益者\n\n报告对Global Unichip Corp（世芯-KY，3443.TW）的推荐，是理解整个AI基础设施投资逻辑的起点。MS将其评级设为“Overweight”，核心论据不只是2026年谷歌CPU的营收贡献，而是2027年来自特斯拉AI5、亚马逊边缘AI芯片以及SanDisk SSD控制器的增量收入。\n\n这里的关键洞察在于：市场当前对AI芯片的关注仍然高度集中在英伟达的GPU上，但MS认为，设计服务市场将随着AI ASIC的长期增长而爆发，其增速将超过AI GPU。这不是一个短期的周期性判断，而是一个结构性判断——当AI应用从训练走向推理，从云端走向边缘，从大模型走向垂直场景，定制化芯片的需求将系统性上升。\n\n> **KC评论：** 大多数投资者把“AI芯片”等同于“GPU”，但GPU是通用计算平台，而ASIC是专用芯片。当AI应用进\n\n[... middle omitted ...]\n\n务板块的现金流拆解感兴趣，欢迎来我们的星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI芯片的下一站：设计服务\n\nAI ASIC vs GPU\n\n谁才是长期赢家？\n\n最近读了一份某外资投行的研报，讲了三个有意思的方向，分享给大家一起讨论。\n\n1/ 芯片定制化是长期趋势\n研报认为，AI ASIC（专用芯片）的增速会超过AI GPU（通用芯片）。原因很简单：大厂都在自研芯片，定制化需求爆发。比如某设计服务公司，除了Google的CPU订单，2027年还有Tesla、Amazon和SanDisk的新项目，想象空间不小。\n\n2/ 数据中心带飞半导体\n一家日本半导体公司，数据中心业务占比从个位数跳到16%，直接拉高了它的中期增长预期。研报判断，数据中心会是未来几年半导体行业的核心驱动力。\n\n3/ 印度的“孵化器”逻辑\n印度一家综合性企业，业务覆盖交通、数字基建、能源转型等多个领域。研报预测未来5年收入和利润增速都在20%以上。这种多赛道布局，有点像“印度版的三星”。\n\n总结下来，三个关键词：AI定制化、数据中心、印度基建。每个方向都值得持续跟踪。\n\n欢迎一起讨论～\n\n#学习笔记\n\n[source_mineru.md]\nJune 28, 2026 10:00 PM GMT\n\nAsia | Asia Pa\n\n[... middle omitted ...]\n\nts to the low teens. We forecast CY26 data center revenue at 16% of the mix, well above the broad-based semiconductor peer average.\n\nOW – Adani Enterprises (ADEL.NS): AEL is India's premier in\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R030",
    "title": "Citi：康宁的“玻璃桥”技术，对中国光模块龙头影响有限",
    "digest": "[wechat_article.md]\n# Citi：康宁的“玻璃桥”技术，对中国光模块龙头影响有限\n\n市场对康宁新发布的GlassBridge光纤连接技术反应热烈，不少投资者担忧这会颠覆中国光模块企业的竞争格局。Citi最新研报给出了一个更冷静的判断：短期冲击可控，长期替代路径清晰但遥远。这份报告的核心洞察是，真正决定行业格局的，不是一项新连接技术本身，而是技术切换带来的系统性成本与客户锁定效应。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 当前CPO方案已定型，GlassBridge在2028年前不具备进入量产的条件\n\nCiti认为，康宁在2026年6月正式发布的GlassBridge技术，本质上是为下一代NPO（近封装光学）和CPO（共封装光学）架构设计的替代方案，目标是取代当前CPO方案中使用的iFAU（集成光纤阵列单元）。但关键判断在于：当前两大主流CPO方案——Quantum和Spectrum——的设计已经冻结，进入量产阶段，不会因GlassBridge的出现而更改。\n\n更值得注意的是，预计在2026年下半年最终确定的2027年下半年CPO方案（用于英伟达Rubin Ultra Kyber平台），也大概率不会采纳GlassBridge。Citi给出的理由是，GlassBridge需要经历CPO/NPO系统的评估周期、高速AI集群环境下的现场测试和可靠性验证，这些流程在1到2年内难以完成。\n\n> **KC评论：** Citi的分析逻辑很清晰——新技术在半导体行业从来不是“发布即替代”。CPO方案的定型周期长达18-24个月，客户一旦完成设计锁定，更换连接方案意味着重新设计光芯片的波导布局、修改点尺寸转换器、调整凸块结构。这些切换成本构成了强大的技术惯性。对于投资者来说，真正需要关注的不是技术发布本身，而是技术进入客户设计验证窗口的时间点。\n\n这背后\n\n[... middle omitted ...]\n\n来星球微信群中继续讨论这些未解问题，跟踪技术验证的最新进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n康宁新连接技术，光模块玩家影响几何？\n\nGlassBridge 来了，短期不必慌\n\n某外资投行最新研报：康宁6月24日发布GlassBridge™，一种光纤到PIC的新型连接方案，用玻璃基板波导解决硅光芯片与光纤的尺寸匹配问题。目标直指NPO/CPO架构，但研究团队认为：短期影响有限。\n\n1/ 现有CPO方案（Quantum和Spectrum）已定型量产，不受影响。2H27的Rubin Ultra Kyber方案也将在今年下半年确认设计，不太可能被替换。\n\n2/ GlassBridge要真正落地，还得通过CPO/NPO验证、可靠性测试、良率爬坡，不确定性很大。未来1-2年基本没影响。\n\n3/ 2028-2030年CPO/NPO商用化过程中，GlassBridge可能竞争新增部署的iFAU，而非存量市场。2030年后，如果晶圆级光子封装在良率和损耗上成熟，被动光学组件行业才可能面临真正的范式转变。\n\n4/ 切换成本高。采用GlassBridge需要PIC设计者重构光学布局、重新设计模斑转换器、修改凸点结构，生态惯性是很大阻力。\n\n5/ 国内光模块公司影响评估：\n- 天孚通信：iFAU长期替代风险可控，主动光引擎\n\n[... middle omitted ...]\n\nst and yield ramp. Among our covered names, TFC's long-term risk in iFAU is well contained by its ramping active optical engines' contribution. DSBJ, Eoptolink, Accelink and T&S remain largely\n\n[... middle omitted ...]\n\nk to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party."
  },
  {
    "id": "R031",
    "title": "摩根斯坦利：MS：AI ASIC正在超越GPU，但真正的机会在三个不起眼的名字",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI ASIC正在超越GPU，但真正的机会在三个不起眼的名字\n\n当市场还在为英伟达的下一代GPU争论不休时，一份来自MS的研报提出了一个值得认真对待的判断：AI ASIC的长期增速将超过AI GPU。这不是一个遥远的预测，而是已经体现在三个具体公司身上的现实。\n\n这份2026年6月28日发布的“Three Actionable Ideas”报告，表面上给出了三个独立推荐——Global Unichip、Renesas和Adani Enterprises。但将它们放在一起看，一个清晰的逻辑浮现出来：AI基础设施的竞争正在从“算力军备竞赛”转向“定制化效率竞赛”，而真正受益的，不是那些被广泛讨论的巨头，而是那些在特定垂直领域建立了不可替代性的公司。\n\n报告的历史数据显示，该策略自推出以来累计跑赢基准9533个基点，平均持有期绝对回报4.3%，12个月平均绝对回报16.1%。这些数字本身已经说明问题。但更值得追问的是：为什么是这三个？它们之间有什么共同逻辑？这份报告没有直接说出来的结构性变化是什么？\n\n> **KC评论：** MS的“Three Actionable Ideas”是一个持续更新的选股策略，不是一次性推荐。其核心优势在于用系统化的方法寻找被低估的结构性机会，而不是追逐短期热点。理解这个框架，比知道具体哪三只股票更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI ASIC正在成为比GPU更重要的长期叙事，但市场还没有充分定价\n\nMS对Global Unichip的推荐，核心逻辑在于AI ASIC（专用集成电路）的长期增速将超过AI GPU。这是一个反直觉的判断——当市场普遍认为GPU是AI计算的核心时，报告指出定制化芯片正在成为更重要的增长引擎。\n\n报告明确提到，Global\n\n[... middle omitted ...]\n\n读、原始图表，以及与其他产业决策者的深度交流机会。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n三家亚太公司，研报里挖出的新线索\n\n三个值得跟踪的研究方向\n\n1/ 设计服务赛道在变宽\n投行研报点名了一家台湾公司，认为它不只是靠单一客户撑业绩。2026年谷歌CPU贡献大，但2027年还有特斯拉AI5、亚马逊边缘AI芯片、SanDisk存储控制器这些增量。长期看，AI定制芯片（ASIC）的增速可能超过通用GPU——设计服务市场正在被重新定义。\n\n2/ 数据中心拉动传统芯片商\n日本一家老牌半导体公司，过去增长预期在个位数，现在被数据中心业务拉到了低两位数。研报估算其2026年数据中心收入占比将达16%，远超同类公司平均水平。传统芯片厂靠数据中心翻盘，这个逻辑值得留意。\n\n3/ 印度综合性平台的故事\n印度一家企业被定义为“国家级孵化器”，覆盖交通基建、数字基建、能源转型、自主制造等多个十年维度主题。研报预测未来5年收入复合增速19%，EBITDA增速32%。多业务线叠加增长，观察它的执行节奏。\n\n✨ 研究笔记 | 研报解读\n\n#学习笔记\n\n[source_mineru.md]\nJune 28, 2026 10:00 PM GMT\n\nAsia | Asia Pacific\n\n## Three Actionable\n\n[... middle omitted ...]\n\nts to the low teens. We forecast CY26 data center revenue at 16% of the mix, well above the broad-based semiconductor peer average.\n\nOW – Adani Enterprises (ADEL.NS): AEL is India's premier in\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R032",
    "title": "GS：印度国防板块的下一轮上涨，不靠估值靠订单",
    "digest": "[wechat_article.md]\n# GS：印度国防板块的下一轮上涨，不靠估值靠订单\n\n当市场还在争论印度股市整体是否估值过高时，GS最新的一份亚太路演反馈给出了一个更具体的信号：投资者对印度国防板块的兴趣已经从“能不能买”转向了“买什么、什么时候买”。这不仅是情绪的变化，更意味着该板块正在进入一个由订单兑现和盈利增长驱动的新阶段。\n\n这份报告来自于GS印度股票研究团队在3月底对新加坡和香港约25位机构投资者的路演。核心发现是：投资者对国防板块的讨论深度和具体程度，远超对金属矿业板块的关注。他们不再满足于“印度国防支出会增长”这个宏观叙事，而是开始逐一拆解每家公司的订单管线、执行能力、技术壁垒和估值合理性。这种从“板块”到“个股”的聚焦，本身就是市场成熟的标志。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 国防板块的讨论重心已从“为何看好”转向“谁更值得买”\n\nGS团队发现，与上一次路演相比，投资者对国防板块的提问发生了根本性转变。上一次，大家还在问“印度国防支出是否会因为财政平衡而减少”；而这一次，投资者普遍认同“无论财政如何在消费和资本开支之间平衡，国防支出都会持续增长”。共识形成后，讨论自然下沉到个股层面。\n\n在大型股中，Solar Industries是被讨论最多的股票。投资者普遍认可其“国防板块中的清晰买入标的”地位，但焦点集中在两个看似矛盾的问题上：股价近期上涨能否持续，以及公司能否成功从一家炸药企业转型为复杂的平台级国防供应商。投资者对Solar Industries参与MALE无人机项目竞标、155毫米炮弹和反无人机系统(Bhargavastra)的市场空间，以及硝酸铵价格下跌对盈利的影响，都表现出高度兴趣。\n\n在中型股中，PTC Industries成为焦点。这家公司之所以吸引关注，在于其陡峭的盈利增长轨迹——GS预计其FY27-FY\n\n[... middle omitted ...]\n\n你可以与来自产业和投资一线的朋友继续讨论这些尚未解答的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n军工防务，逻辑变了\n\n**封面：军工逻辑变了**\n\n**副标题：新加坡投研会上的新共识**\n\n上个月和某外资投行在新加坡、香港跑了25场会，聊了聊印度军工和金属。信息密度很高，直接上干货。\n\n**1/ 军工：共识在变强**\n\n大部分投资者开场就是聊防务。问得最多的是：FY27的大订单在哪？Q1订单弱是为什么？但大家基本都同意一个判断：就算印度整体市场不好，就算美伊关系缓和，防务开支还是会继续涨。不管财政怎么平衡消费和基建，这块不会砍。\n\n**2/ 几个核心讨论点**\n\n- **Solar Industries**：大票里讨论最多。大家认同它是防务里最清晰的买入标的，但也在问股价涨了这么多，能不能持续？订单执行怎么样？MALE无人机投标进展如何？155mm炮弹和反无人机系统（Bhargavastra）的TAM有多大？还有，从炸药商变成复杂平台商，R&D能力跟得上吗？多数人觉得估值贵，但盈利增长和资产负债表能撑住。\n\n- **PTC Industries**：中盘股里最火。增长曲线太陡了。大家问订单积压、产能投产时间、竞争壁垒。有人拿它跟Howmet Aerospace和PCC比，问商业模式和产品差异。钛合金和高\n\n[... middle omitted ...]\n\n on the stocks with category leadership or unique proposition. Overall, investors agreed that the Defense sector has performed well even in the backdrop of overall weak India market performanc\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R033",
    "title": "摩根斯坦利：化工周期比市场预期的来得更快",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：化工周期比市场预期的来得更快\n\n化工行业正在经历一个不被市场充分定价的转折。摩根斯坦利在最新发布的亚洲化工行业深度报告中，给出了一个与当前市场共识有明显差异的判断：亚洲石化裂解装置的利润率已经非常接近周期中段水平，而这一修复速度远快于华尔街的模型预期。更重要的是，该机构认为约有半数利润率回升具有粘性，不会随着成本端通胀的消退而全部回吐。\n\n这份报告发布于2026年6月28日，距离摩根斯坦利自2025年第三季度以来一直保持的“非共识看多”立场已近一年。在化工板块经历了长达数年的资本开支下行、产能出清与利润率压缩之后，报告认为行业正在进入一个真正意义上的修复周期——不是短暂反弹，而是结构性改善。\n\n对于关注制造业、大宗商品周期以及亚太资产配置的投资者而言，这份报告值得认真拆解。以下几层逻辑尤其关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利润率修复的速度和幅度，市场尚未充分定价\n\n摩根斯坦利报告中最核心的实证发现是：亚洲石化裂解装置的整合利润率已经非常接近周期中段水平，而市场此前普遍认为这一修复需要更长时间。报告特别指出，尽管石脑油供应在增加，但过去三周中大部分时间石脑油成本在下降，这为利润率修复提供了额外支撑。\n\n这一判断之所以重要，是因为它直接挑战了当前市场对化工板块盈利能力的普遍悲观预期。如果利润率确实已经接近周期中段，那么当前估值所隐含的盈利假设就存在显著的上修空间。\n\n> **KC评论：** 市场对化工板块的定价往往滞后于实际利润率变化。摩根斯坦利的这一判断意味着，如果后续财报季数据验证了利润率修复的趋势，板块估值可能面临系统性重估。完整报告中包含了详细的利润率拆分和不同情境下的敏感性分析，这些是理解修复幅度边界的关键。\n\n![研报原图 2](assets/source_image_\n\n[... middle omitted ...]\n\n欢迎来知识星球微信群中继续讨论，一起跟踪这些关键信号的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n化工周期拐点，比你想的来得快\n\n化工底部确认\n\n亚洲化工的裂解价差，已经快回到周期中段了。\n\n某外资投行最新研报判断：行业盈利修复比市场预期的更快。过去两年，亚洲有10%的烯烃产能被永久关闭或长期检修，新产能也在推迟——供给端终于开始收敛。\n\n📌 三个核心逻辑：\n\n1️⃣ 自由现金流正在回血\n过去三个季度，多数亚洲化工企业开始报告正向自由现金流，资本开支削减了近三分之一。市场对2026/2027年FCF的预期也在持续上调。这是近三年来第一次出现盈利上调周期。\n\n2️⃣ 行业自律增强\n四个国家出现了产能和股权层面的整合，行业纪律在改善。那些有国内市场需求和成本优势的企业，会在这一轮中跑赢。\n\n3️⃣ 估值还在低位\n亚洲化工股目前交易在1倍市净率附近，接近历史低谷。而盈利已经在边际改善，研报认为即将到来的财报季可能会让市场重新定价。\n\n📌 谁更受益？\n研报偏好石脑油路线的化工企业（相对于天然气路线），因为它们在周期复苏中弹性更大。提到的代表公司包括：暹罗水泥、三井化学、中石化（H股）、万华化学。\n\n📌 一点补充\n研报也提醒，最近几周石脑油成本在下降，价差可能从高位回落，但预计18-24个月内会重新回到中周期盈利水\n\n[... middle omitted ...]\n\necovering in the past two quarters and Street capex estimates have halved for 2026-2028, pointing to a recovery cycle.\n\nWe expect margins to cool off from recent highs but see a path to mid-cy\n\n[... middle omitted ...]\n\nsero) Tbk PT (SMGR.JK)</td><td>U (11/18/2024)</td><td>Rp1,465</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R034",
    "title": "GS：美国供应链已经“正常”到让人忽略，但运费正在悄悄反弹",
    "digest": "[wechat_article.md]\n# GS：美国供应链已经“正常”到让人忽略，但运费正在悄悄反弹\n\n当大多数市场参与者还在用2021-2022年的记忆来想象供应链紧张时，GS最新的供应链拥堵指数给出了一个反直觉的信号：拥堵水平已经回到疫情前基线，但运费正在以每周19%的速度反弹。\n\n这份截至2026年6月29日的周度报告显示，GS供应链拥堵指数连续第二周维持在“2”的水平——这个数字在2021年12月/2022年1月的峰值是“10”。更关键的是，GS自己判断：“如果供应链压力继续缓解，指数可能在2026年稳定在‘1’的区间。”\n\n换句话说，供应链已经不是问题。但问题恰恰在于，市场对“供应链已正常”这件事的交易已经充分定价，而新的边际变化——运费反弹、东海岸船舶积压、以及关税对贸易流的潜在冲击——正在被忽视。\n\n这份报告的核心价值不在于告诉你“供应链恢复了”，而在于它提供了一套高频指标体系，让你能在大多数人还没反应过来之前，捕捉到下一个拐点的早期信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 拥堵指数已回疫情前，但“正常”本身就是一个需要重新定义的基准\n\nGS的周度拥堵指数从2021-2022年的峰值“10”一路回落，6月最后一周维持在“2”。如果只看绝对水平，这个数字已经接近2020年2月的疫情前基线。但这里有一个容易被忽略的细节：GS使用的基线是2020年2月3日——那是疫情冲击全球供应链之前的一周。换句话说，当前供应链的“正常”程度，是以一个没有疫情、没有关税战、没有地缘冲突的世界为参照的。\n\n而现实世界早已不是那个世界。\n\n> **KC评论：** GS的基线选择本身就隐含了一个判断——当前供应链的“正常”是相对于一个已经回不去的基准。读者需要追问的是：如果基线本身是历史性的，那么“回到基线”是否意味着供应链已经真正适应了新的地缘和贸易\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国供应链堵车指数，回到疫情前水平\n\n📦 供应链恢复中\n\n6月29日，美国供应链拥堵指数小幅下降7%，瓶颈等级维持在“2”。这个水平已经接近疫情前的流畅状态，远低于2021年底的峰值“10”。\n\n🚢 港口拥堵情况\n- 西海岸等待卸货的集装箱船数量不变，仍为1艘\n- 东海岸积压船只从3艘增加到4艘\n- 整体来看，港口压力已经大幅缓解\n\n🚂 铁路运输表现\n- 西海岸铁路联运量同比+14%，比上周的+11%继续加速\n- BNSF铁路联运量同比+15%，UNP铁路+12.5%\n- 铁路停留时间略有上升，但仍处于可控范围\n\n📊 其他关键指标\n- 底盘停留时间小幅增加，20英尺集装箱从4.4天升至5.1天\n- 海运价格（中国→美西）环比+19%，同比+3%\n- 门到门运输时间稳定在47天，远低于高峰期80+天\n\n💡 核心观察\n研报认为，如果供应链压力继续缓解，2026年指数可能稳定在“1”的水平。但关税和地缘政治仍是影响货运需求的关键变量。\n\n你觉得供应链恢复会持续吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\nTRACKING U.S. SUPPLY CHAIN CONGESTION\n\n# G\n\n[... middle omitted ...]\n\n/w; Exhibit 2). For this week’s scale and index, the number of container ships waiting to dock and unload goods along the West Coast remained unchanged at 1, while backlogs along the East Coas\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R035",
    "title": "NOM：小红书首次下滑背后，中国互联网正在经历一场AI替代",
    "digest": "[wechat_article.md]\n# NOM：小红书首次下滑背后，中国互联网正在经历一场AI替代\n\n中国移动互联网的流量格局正在发生一个值得警惕的转折。\n\n根据NOM最新发布的5月App追踪报告，中国移动互联网大盘仍在增长——月活跃智能设备用户同比增长1.2%至12.8亿，总使用时长同比增长10.1%。但这些宏观数字之下，几个关键信号正在浮现。\n\n其中最引人注目的，是小红书自NOM2020年开始追踪以来，首次出现月度总使用时长同比下降。尽管日活跃用户仍有3%的增长，但人均日使用时长下滑了4%，导致总时长录得1%的负增长。\n\n这绝不是孤例。百度App总使用时长同比暴跌21%，日活下降21%。腾讯视频总时长下降31%，日活下降22%。携程、去哪儿、飞猪等旅游App的总时长跌幅均在14%-19%之间。京东App在618大促季仍录得10%的总时长同比下降。\n\n这些数据指向一个共同的问题：用户正在从哪些App流失，又流向了哪里？\n\n> **KC评论：** NOM的这份月度追踪报告，表面看是流量数据汇总，实际上揭示了一个正在发生的结构性变化——AI正在替代传统App的功能价值。这不是周期性的波动，而是用户行为习惯的迁移。完整报告中有大量细分赛道的DAU和时长图表，能帮助读者直观看到哪些App在“失血”，哪些在“造血”。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 小红书遇到的不只是增长瓶颈，而是AI对“种草”逻辑的根本挑战\n\n小红书的首次时长下滑，NOM给出的解释是“AI逆风”。这个判断值得认真对待。\n\n小红书的核心价值在于“信息发现”——用户通过搜索和推荐获取关于消费、旅行、生活方式等各类信息。但这一功能正在被AI聊天机器人替代。当用户可以直接向DeepSeek、豆包或通义千问提问“周末北京周边哪里适合亲子游”，或者“油痘肌适合什么洗面奶”，他\n\n[... middle omitted ...]\n\n——特别是关于“AI替代”这个主题，还有很多值得拆解的细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n小红书首遇“滑铁卢”？用户时长首次下滑\n\n小红书，用户时长首次下降\n\nDAU还在涨，但人均刷的时间变少了\n\n某外资投行的最新App追踪报告，把5月的互联网数据扒了个底朝天。\n\n1️⃣ **小红书：DAU涨了，但时长“失守”**\n- 5月小红书总使用时长同比下滑1%，这是自2020年有追踪数据以来的首次。\n- 原因很微妙：DAU（日活）虽然增长了3%，但人均单日使用时长却下降了4%。\n- 研报推测，用户可能正在转向AI聊天机器人获取信息，这对小红书“信息发现”的核心定位构成了挑战。\n- 为了应对，小红书拿下了2026年世界杯的独家网络直播权，意图拓宽用户群。\n\n2️⃣ **电商：618也救不了疲态**\n- 淘宝和京东的时长环比虽然因618大促反弹（+17%和+19%），但同比数据很一般。\n- 淘宝时长同比仅增7%，京东更是同比下滑10%（去年搞外卖拉高了基数）。\n- 拼多多时长同比增13%，相对稳健，因为它全年低价策略，不太依赖大促刺激。\n\n3️⃣ **AI赛道：豆包一骑绝尘，DeepSeek重回第二**\n- 字节跳动的豆包，5月DAU达到1.58亿，同比暴涨3.6倍，继续领跑。\n- DeepSeek在4月底发\n\n[... middle omitted ...]\n\nABA US, Buy)] and JD (JD US, Buy) app rebounded by 17% and 19% sequentially, respectively, in May, driven by 618 promotions (which started in mid-May). But the y-y trend looks lackluster – Tao\n\n[... middle omitted ...]\n\nlable upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R036",
    "title": "Citi：康宁的GlassBridge，短期不必恐慌，但长期格局已埋下伏笔",
    "digest": "[wechat_article.md]\n# Citi：康宁的GlassBridge，短期不必恐慌，但长期格局已埋下伏笔\n\n2026年6月24日，康宁正式发布了GlassBridge技术。消息一出，市场对国内光通信产业链的担忧迅速升温：这是否意味着CPO（共封装光学）架构中的关键连接件iFAU将被替代？国内相关供应商是否面临灭顶之灾？\n\nCiti在第一时间发布的研报给出了一个清晰且克制的判断：**GlassBridge在接下来1-2年内不会对现有CPO方案和供应链产生实质性冲击，但它的出现，为2028-2030年后的行业格局埋下了真正需要关注的伏笔。**\n\n这份报告的价值，不在于它给出了一个简单的“利好”或“利空”结论，而在于它用技术、生态和商业逻辑，分层拆解了“一个新技术出现后，产业真实会发生什么”。对于决策者而言，真正重要的不是GlassBridge本身，而是它揭示的行业演进路径。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 当前CPO方案已经锁定，GlassBridge短期内无法插队\n\nCiti的核心判断首先建立在时间线上。报告明确指出，当前用于量产的两代CPO方案——Quantum和Spectrum——其设计已经最终确定，不会受到GlassBridge的影响。而对于预计在2027年下半年部署的Rubin Ultra Kyber CPO方案，其设计也将在今年下半年确认，同样不太可能被GlassBridge取代。\n\n这意味着，任何关于GlassBridge会颠覆现有供应链的担忧，在时间上都不成立。从技术验证到客户导入，再到大规模量产，GlassBridge还需要经历CPO/NPO（近封装光学）系统的评估周期、高速AI集群环境下的现场可靠性测试，以及良率爬坡。这些环节至少需要1-2年时间。\n\n> **KC评论：** Citi的逻辑其实是在说，大型科技公司的芯\n\n[... middle omitted ...]\n\n。欢迎加入我们的社群，在微信群里继续深入讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n康宁新方案，短期别慌\n\nGlassBridge 短期影响有限\n\n某外资投行最新研报分析了康宁刚发布的 GlassBridge 技术，结论是：**近一两年，对国内光通信公司影响不大**。\n\n1️⃣ **GlassBridge 是什么？**\n康宁在 6 月 24 日正式发布了 GlassBridge，这是一种基于离子交换波导的玻璃连接器，用来解决硅光芯片和光纤之间的尺寸不匹配问题，目标是替代 CPO 架构中的 iFAU 方案。\n\n2️⃣ **为什么短期不用慌？**\n- 当前 CPO 方案（Quantum 和 Spectrum）已定稿量产，不会受影响\n- 2027 下半年的 CPO 方案设计将在今年下半年确认，也不太可能被替换\n- GlassBridge 还需要通过 CPO/NPO 评估期和高速 AI 集群的可靠性测试，不确定性很大\n- 从生态角度看，采用 GlassBridge 需要 PIC 设计方重构光口布局、重新设计模斑转换器，切换成本高，短期渗透阻力大\n\n3️⃣ **对国内公司的影响**\n- **天孚通信**：iFAU 的长期替代风险被其快速增长的有源光引擎业务对冲，预计 2026-2028 年有源光引擎贡\n\n[... middle omitted ...]\n\nst and yield ramp. Among our covered names, TFC's long-term risk in iFAU is well contained by its ramping active optical engines' contribution. DSBJ, Eoptolink, Accelink and T&S remain largely\n\n[... middle omitted ...]\n\nk to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party."
  },
  {
    "id": "R037",
    "title": "摩根斯坦利：MS：化工周期比市场预期的来得更快，也更粘",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：化工周期比市场预期的来得更快，也更粘\n\n化工行业正在经历一场多数投资者尚未定价的变化。MS在最新发布的亚洲化工行业深度报告中，给出了一个在当下市场环境里显得相当有分量的判断：亚洲裂解装置的利润率已经非常接近周期中段水平，而这个修复速度比市场普遍定价的要快得多。\n\n这份报告发布于2026年6月底，距离MS首次在2025年第三季度转为看多化工行业已经过去三个季度。在当时，这还是一个非共识的立场。而现在，报告的核心观点已经不只是“看好”，而是“修复正在发生，且部分修复具有结构性”。\n\n对于一家在化工领域拥有多年跟踪经验的投行而言，这个判断的分量在于：它不是在说“底部到了”，而是在说“中段正在被重新定义”。\n\n> **KC评论：** 市场对化工股的定价仍然停留在“周期底部”的叙事里。但MS认为，利润率修复的速度和幅度都超过预期，而且其中约一半的改善是可持续的。这意味着，如果投资者继续用底部估值框架来给这些公司定价，他们可能正在错过一个周期拐点。完整报告中的图1和图2分别展示了整合利润率与估值水平的关系，值得仔细对比。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮修复的核心驱动力不是需求，而是供给端的结构性出清\n\n过去一年，亚洲约有10%的烯烃产能被永久关闭、暂停运营或处于超长检修期。这不是一个小数字。在化工这样一个资本密集、产能刚性极强的行业里，10%的产能退出意味着供给曲线已经发生了实质性位移。\n\n与此同时，新增产能的投放持续推迟。市场原本预期更高的供给增量，但现实是，资本支出的削减力度超出了预期。MS的数据显示，亚洲化工企业的资本支出在2026至2028年间几乎被砍半，而同期市场对自由现金流的预期却在持续上调。\n\n这个组合值得留意：供给退出在加速，新增产能被推迟，而企业的资本纪律在增强。这\n\n[... middle omitted ...]\n\n估值逻辑有进一步兴趣，欢迎来星球和微信群继续讨论。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n化工周期，比想象中来得快\n\n化工周期来了\n\n亚洲裂解价差已接近中周期水平\n\n最近翻到某外资投行的化工研报，观点挺有意思。\n\n1️⃣ 周期比预期更早见底\n亚洲石化裂解价差已经非常接近中周期水平。过去一年，约10%的烯烃产能被永久关闭、停产或延长检修。新产能持续推迟，行业供给端开始收缩。\n\n2️⃣ 现金流改善明显\n亚洲化工企业过去三个季度开始报告正自由现金流，资本开支削减了近1/3。2026-2027年自由现金流预期持续上调，这是近三年来首次出现盈利上调周期。\n\n3️⃣ 成本曲线分化\n非制裁原油供应增加，将抬高中国民营炼化企业的现金成本曲线，反而利好亚洲其他地区生产商。石脑油基化工企业比天然气基玩家更有弹性，对复苏周期的敏感度更高。\n\n4️⃣ 估值仍处低位\n大宗化工品估值仍接近周期底部，但基本面已在改善。印度、东南亚及部分化工价值链开始出现盈利上调，行业整合也在加速。\n\n研报看好石脑油基化工企业、拥有强势国内市场的公司、以及成本曲线优势明显的企业。\n\n欢迎一起讨论化工周期的投资逻辑。\n\n#学习笔记\n\n[source_mineru.md]\nJune 28, 2026 07:00 AM GMT\n\nAsia – Che\n\n[... middle omitted ...]\n\necovering in the past two quarters and Street capex estimates have halved for 2026-2028, pointing to a recovery cycle.\n\nWe expect margins to cool off from recent highs but see a path to mid-cy\n\n[... middle omitted ...]\n\nsero) Tbk PT (SMGR.JK)</td><td>U (11/18/2024)</td><td>Rp1,465</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R038",
    "title": "GS：印度国防股的下一轮催化，不在订单，在交付",
    "digest": "[wechat_article.md]\n# GS：印度国防股的下一轮催化，不在订单，在交付\n\n当大多数市场参与者还盯着印度国防部的季度订单公告时，GS最新一期亚太路演反馈揭示了一个更微妙的信号：投资者对印度国防板块的关切点，正在从“订单数量”转向“交付质量”。\n\n这份来自GS印度研究团队的路演纪要，覆盖了新加坡和香港约25位机构投资者。核心发现是：投资者普遍认可印度国防支出的结构性上升趋势，但开始对短期订单疲软、估值支撑和盈利兑现能力提出更尖锐的问题。这不是一个简单的“看好”或“看空”信号，而是一个市场正在进入“验证期”的标志。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 国防板块的共识已经形成，市场现在需要的是“超预期”的证据\n\nGS团队在路演中观察到，投资者对印度国防板块的讨论起点高度一致：政府国防支出将继续增长，不论财政在消费与资本开支之间如何平衡。在这一点上，几乎没有分歧。\n\n但共识的背面是焦虑。Q1FY27订单流入疲软，让投资者开始追问：这个结构性故事，是否已经充分定价？GS团队注意到，相比上一次路演，关于估值的质疑明显减少，取而代之的是对“催化剂”和“执行细节”的追问。这恰恰说明市场已经从“要不要买”进入了“买什么、什么时候买”的阶段。\n\n对于投资者而言，这意味着：单纯押注国防板块beta的阶段可能已经过去。未来的超额收益，将来自那些能够证明自己不只是“受益者”，而是“执行者”的公司。\n\n> **KC评论：** GS的这份路演反馈，本质上是一张“市场情绪温度计”。它告诉我们，印度国防板块已经从“讲故事”阶段进入“验证故事”阶段。验证的关键，不是政府明年花多少钱，而是公司今年能交付多少。这正是完整报告中各公司订单执行细节、产能爬坡时间表的价值所在。\n\n## 2. Solar Industries的争议：估值贵，但增长和资产负债表是“通行证”\n\n在所\n\n[... middle omitted ...]\n\n也方便人工快速把握市场动态。欢迎来知识星球和微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n军工与金属：新加坡香港路演笔记\n\n封面：投资人最关心什么\n\n副标题：25家机构的核心关注点拆解\n\n最近和某外资投行分析师聊了他们在新加坡、香港的路演反馈，见了约25家机构投资者。分享几个有意思的观察：\n\n**1️⃣ 军工板块仍是焦点**\n- 投资人最关心FY27的潜在大单节奏\n- Q1FY27订单流入偏弱，大家想知道原因\n- 普遍认为国防支出会持续增长，不受消费与基建平衡影响\n- 对无人机、雷达电子市场兴趣浓厚\n\n**2️⃣ 金属板块偏谨慎**\n- 想搞清楚钢价走势和需求增长方向\n- 扁平材比长材更弱，大家想找原因\n- 目前处于“等等看”的观望状态\n\n**3️⃣ 选股逻辑变了**\n- 相比上次路演，估值问题问得少了\n- 更关注有“品类领导者”地位或独特护城河的公司\n- 对高增长轨迹的标的格外有兴趣\n\n**4️⃣ 几家被重点讨论的公司**\n\n🔹 Solar Industries（最热的大盘股）\n- 股价涨太快能否持续？订单执行情况如何？\n- 关注155mm炮弹TAM和反无人机系统\n- 从炸药商转型复杂平台商，大家看好但觉得贵\n\n🔹 PTC Industries（最热的中盘股）\n- 订单积压、产能投产时间线是核心\n\n[... middle omitted ...]\n\n on the stocks with category leadership or unique proposition. Overall, investors agreed that the Defense sector has performed well even in the backdrop of overall weak India market performanc\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R039",
    "title": "NOM：小红书首次下滑，中国互联网的“AI替代”开始兑现了",
    "digest": "[wechat_article.md]\n# NOM：小红书首次下滑，中国互联网的“AI替代”开始兑现了\n\n中国互联网行业正在经历一个微妙但关键的转折点。NOM最新发布的5月App追踪报告揭示了一个此前从未出现的信号：小红书，这个被誉为“中国版Instagram”的平台，自2020年有追踪数据以来，首次出现了用户总使用时长同比下降。\n\n这个1%的跌幅看似不大，但它指向的结构性变化，可能比618大促期间电商增速放缓、旅游出行App全面走弱、甚至长视频持续萎缩都更具长期意义。\n\nNOM的这份月度报告，核心判断可以浓缩为一句话：**AI正在从“补充工具”变成“替代入口”，它最先冲击的，不是搜索或电商，而是那些以“信息发现”为核心价值的内容平台。**\n\n这不是一个遥远的担忧。数据已经落地。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 小红书“首次下滑”背后，是AI对信息发现入口的替代已经实质发生\n\n根据QuestMobile数据，小红书的月总使用时长在5月同比下降1%。拆分来看，日活跃用户仍有3%的增长，但每位日活用户的日均使用时长下降了4%。这是典型的“用户还在，但黏性在流失”的信号。\n\nNOM在报告中直接给出了判断：小红书可能正在经历与其他信息门户（如搜索）同样的“AI逆风”——用户越来越多地转向AI聊天机器人来获取信息和知识，这直接威胁到小红书最核心的价值主张：内容发现与种草。\n\n这个逻辑值得认真对待。小红书的本质是一个基于UGC的内容搜索引擎，用户带着“想买什么”“想去哪里”“怎么解决某个问题”的意图打开它。而AI聊天机器人，尤其是具备联网搜索和深度推理能力的模型，正在以更直接、更高效的方式满足同样的需求。\n\n> **KC评论：** 小红书的“首次下滑”不是孤立事件。它可能是中国互联网“AI替代”从概念验证走向数据验证的第一个里程碑。完整报告里还包含了\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n小红书史上首次：用户时长下降1%\n\n**用户时长首降**\n\n小红书首次出现用户时长下降\n\n某外资投行5月App追踪报告显示，小红书月总使用时长同比下滑1%，这是自2020年有追踪数据以来的首次下降。\n\n**核心数据拆解：**\n1. DAU仍在增长，同比+3%，达到1.22亿\n2. 但人均单日使用时长下降了4%\n3. 一增一减，总时长反而微降\n\n**背后逻辑很清晰：**\n研报认为，小红书正在经历“AI替代效应”——用户越来越多地转向AI聊天工具获取信息和知识，而这正是小红书的核心价值主张。\n\n**几个有意思的观察：**\n- 电商App表现一般，即使618促销也没拉起来，淘宝时长同比+7%，京东反而-10%\n- 旅行类App集体下滑，携程-19%、飞猪-15%，航油附加费上涨可能是主因\n- 字节系继续蚕食用户时间，时长份额从32.6%涨到39.2%，已超越腾讯系\n\n**AI赛道值得关注：**\n- 豆包DAU达1.58亿，同比3.6倍增长\n- DeepSeek V4发布后重回第二，DAU 3050万\n- 蚂蚁的“阿福”靠免费体检报告解读服务，DAU环比+11%\n\n不过小红书也在自救，拿下了2026年世界杯独家直播权\n\n[... middle omitted ...]\n\nABA US, Buy)] and JD (JD US, Buy) app rebounded by 17% and 19% sequentially, respectively, in May, driven by 618 promotions (which started in mid-May). But the y-y trend looks lackluster – Tao\n\n[... middle omitted ...]\n\nlable upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R040",
    "title": "摩根斯坦利：MS：中国真正的考验不在出口，而在内需能否接棒",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国真正的考验不在出口，而在内需能否接棒\n\n当市场还在为中美关税的反复拉锯而焦虑时，另一个战场已经悄然升温。MS最新发布的亚太投资者报告，将聚光灯打向了一个被许多人低估的风险点：中国与欧盟之间的贸易摩擦。报告的核心判断非常清晰：中国面临的核心挑战，并非外部需求的骤然熄火，而是国内需求能否在外部压力升级之前，真正形成有效的支撑。这不再是一个关于“出口好不好”的问题，而是一个关于“增长引擎切换”的命题。\n\n这份由首席中国经济学家邢自强执笔的报告，其价值不在于预测一个具体的冲突结果，而在于提供了一个全新的分析框架：将中国与欧盟的贸易动态，与中国内部经济结构的冷热不均，放在同一个坐标系里审视。当外需面临的结构性压力开始显性化，国内“生产强、消费弱”的分化格局能否被打破，将成为决定未来12个月资产定价的核心变量。\n\n> **KC评论：** 大部分关于贸易摩擦的分析，要么聚焦于中美，要么停留在对关税影响的静态测算。MS这份报告的独特之处，在于它把欧盟的“工具包”扩张和中国内部需求的“温差”联系了起来。这意味着，评估风险不能只看出口订单的即时波动，更要看国内政策能否在外部压力加码前，把内需的短板补上。完整报告对中国与欧盟关键贸易品类的“依赖度-脆弱性”矩阵拆解，是理解这一判断的底层数据支撑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧盟的“去风险”正从口号转向工具箱，中国面对的贸易压力点正在扩散\n\n报告用大量篇幅展示了欧盟对华贸易赤字的持续扩大这一基本面事实。数据显示，欧盟对华贸易逆差在过去几年里显著走阔，这直接触发了布鲁塞尔的政策反应。从2024年5月的“大学定向辩论”，到2025年6月的G7领导人声明和欧洲理事会结论，措辞从“中国是伙伴，但现状不可持续”升级为“解决大规模和持续性的全球失衡问题”\n\n[... middle omitted ...]\n\n态。欢迎来我们的星球和微信群里，一起追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中欧贸易，正在微妙转弯\n\n中欧贸易新信号\n\n压力点与约束线\n\n最近某外资投行出了一份亚太区研报，专门拆解了中国与欧盟之间的贸易新格局。信息量很大，帮你划重点👇\n\n**1/ 欧盟的“不舒服”在扩大**\n中欧贸易逆差在持续走宽，欧盟的焦虑感上升了。研报引用了多个欧盟官方表态，关键词是“de-risking, not decoupling”——要降低风险，但不是脱钩。中国是伙伴，但现状不可持续。\n\n**2/ 压力点集中在哪？**\n- 贸易逆差最大的领域，就是压力最大的领域。\n- 欧盟自身想保护的竞争力领域，比如电动汽车、电池供应链。\n- 欧盟的工具箱这几年已经扩了，比如《外国补贴条例》（FSR）就是新手段。\n\n**3/ 但冲突也有“天花板”**\n研报指出几个约束因素：\n- 欧盟内部达成共识需要时间，比如电动汽车反补贴税从2023年9月宣布到2024年10月才完成。\n- 过于激进的限制可能引发反制、供应链摩擦，反而拖慢自身电动化进程。\n- 中国手里也有反制工具，比如稀土磁材。\n\n**4/ 再看中国经济这边**\n- 高端制造/出口依然坚挺，6月新兴产业PMI（EPMI）还不错，新订单稳定。\n- 但内需继续软化：二手房销\n\n[... middle omitted ...]\n\nemarks from EU\n\n![](images/ef86a85811e97e284e7be6c4b03ec2ac5c82940ee3265135c55fabab93c4e2f2.jpg)\n\n## READ-OUT: COLLEGE ORIENTATION DEBATE 29 MAY 2026\n\n![](images/e6fa63feb8b7bebf6d7bf5ed5298e5\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R041",
    "title": "Bernstein：美国建筑市场正在被“巨型项目”重塑，而非住宅本身",
    "digest": "[wechat_article.md]\n# Bernstein：美国建筑市场正在被“巨型项目”重塑，而非住宅本身\n\n美国非住宅建筑开工数据在5月呈现出一种罕见的“量价背离”：按金额计算，总开工同比飙升约60%，但按面积计算，却同比下滑了约8%。这是Bernstein最新发布的美国机械与建筑设备研报中揭示的一个核心信号。这份报告的价值不在于罗列数据，而在于指出一个正在发生的结构性变化——美国建筑市场的增长引擎，正在从分散的、由利率驱动的住宅和商业地产，转向集中的、由政策与能源转型驱动的“巨型项目”。\n\n对于关注机械设备、建筑材料、租赁服务和工业股的投资者而言，这不仅仅是一个月度数据更新。它意味着传统的需求分析框架需要被修正。过去，人们习惯用住宅开工、商业地产空置率和利率走向来预测卡特彼勒、联合租赁或建筑材料公司的业绩。但现在，一个价值140亿美元的LNG出口设施在路易斯安那州破土动工，就能在一个月内贡献全美非住宅开工总额的约40%。这种“项目集中度”的跃升，正在从根本上改变行业的竞争逻辑和盈利模式。\n\n> **KC评论：** 这份研报最值得看的判断是：美国建筑市场的“beta”正在从“广泛复苏”转向“结构分化”。市场整体开工面积在下降，但巨型项目的金额和占比却在飙升。这意味着，能否抓住这些集中、大型、高门槛的项目，将成为区分公司优劣的关键。你手里的机械设备股或建材股，到底是在为那些几十亿美元的LNG工厂、数据中心和公共基础设施供货，还是在为那些越来越难赚钱的仓库和公寓楼服务？答案决定了它们的估值天花板。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 巨型项目正在成为市场的主导力量，其占比远超历史均值\n\nBernstein的数据显示，5月美国巨型项目（通常指价值超过10亿美元的项目）开工金额高达约330亿美元，同比增长约420%，环比增长约100%。更关键\n\n[... middle omitted ...]\n\n工快速把握市场动态。欢迎在星球微信群里继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国5月建筑业数据：超级项目爆发式增长\n\n**超级项目狂飙420%**\n\n5月美国建筑业数据出炉，超级项目开工量同比暴增约420%，远超4月的+150%。当月超级项目总规模约330亿美元，环比翻倍。\n\n**1/ 非住宅：金额涨面积跌**\n5月非住宅开工金额同比+60%，但面积却下滑约10%。这说明通胀推动单价大幅上涨（+40%），实际施工量反而在收缩。仓储和“其他”类别拖累明显，制造业和办公类表现不错。\n\n**2/ 住宅：持续低迷**\n住宅开工金额同比-7%，面积-4%。独栋和多户住宅都在跌，只有双户住宅逆势增长15%。住房负担能力仍低于2019-2020年水平，2026年早期数据还显示小幅恶化。\n\n**3/ 超级项目构成**\n当月最大项目是路易斯安那州一个140亿美元的LNG出口设施，占超级项目总量的40%。过去12个月，LNG、公共基础设施和数据中心是超级项目主力（约65%），制造业占比从23%下降，主要受电动车相关项目拖累。\n\n**4/ 值得关注的点**\n超级项目占非住宅开工总量的30%，远高于过去12个月均值20%。这个比例如果持续，建筑设备、工程服务等领域会持续受益。但非住宅面积收缩的信号也需要留意\n\n[... middle omitted ...]\n\n6c.jpg)\n\nChad Dillard\n+1 917 344 8469\nchad.dillard@bernsteinsg.com\n\n![](images/9294510dbed8ff599ddd8af1a13ba15d4d4cf2a6ba725312b3924351332bf9d2.jpg)\n\nMiguel Marques, CFA\n+1 917 344 8432\nmiguel\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R042",
    "title": "摩根斯坦利：MS：村田不是靠涨价，是在重新定义MLCC的护城河",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：村田不是靠涨价，是在重新定义MLCC的护城河\n\n当市场上大多数投资者还在追问“MLCC会不会像2018年那样集体提价”时，MS在2026年6月的新加坡和香港投资者路演中发现了一个更值得关注的信号。\n\n这份覆盖20家日本电子元件公司的研报，核心判断不是供需紧张，也不是周期拐点。它指向一个更根本的分化：那些通过涨价追求短期利润最大化的公司，与那些通过持续提升产品竞争力来扩大价值捕获的公司，其企业价值差距正在不可逆地拉大。\n\n对于关注AI产业链、日本电子板块或被动元件定价逻辑的读者来说，这份报告提供了一个观察框架：高价值MLCC的竞争，已经不再是产能竞赛，而是材料和工艺能力的分层。\n\n> **KC评论：** MS这个判断的核心不在于“AI服务器需要更多MLCC”，而在于“只有村田能稳定量产所有关键型号”。这意味着，当其他厂商还在追赶现有产品时，村田已经在量产下一代产品。这种差距不是价格竞争能弥补的，而是结构性的技术壁垒。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 投资者问错了问题：真正驱动村田ASP增长的不是涨价，是产品组合重构\n\nMS在路演中发现一个有趣的现象：投资者几乎全部关注“通用型MLCC的价格涨幅有多大”，而对高附加值产品带来的盈利扩张潜力关注甚少。\n\n报告给出的数字很清晰。村田计划在F3/27财年将面向AI/数据中心的MLCC销售额同比增长85-90%，其中销量增长约40%，ASP增长约50%。但关键解释在于：这50%的ASP增长并非对同一产品提价，而是高单价、高附加值产品占比提升带来的结构性变化。\n\n背后的技术逻辑更值得注意。每一代新GPU对MLCC的总电容需求大约翻倍，而安装空间却几乎没有增加。这意味着，市场对小型化、高电容、高附加值MLCC的需求将持续增长。村田在这方面的工艺\n\n[... middle omitted ...]\n\narket dynamics。欢迎来星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC 的涨价值得追吗？\n\n**MLCC 的逻辑变了**\n\n刚读完某外资投行最新 MLCC 研报，信息量很大。简单拆一下核心逻辑。\n\n1️⃣ **涨价 ≠ 提价，是结构升级**\n\nMLCC 涨价不是因为公司主动提价，而是高附加值产品占比提升。比如 AI 服务器用的超小尺寸、高容量 MLCC，单价本身就高。村田预计 F3/27 年 AI 相关 MLCC 收入同比增 85-90%，其中 ASP 增长约 50%，但这是“产品组合优化”带来的，不是同一颗料涨价。\n\n2️⃣ **只有少数人能吃到 AI 红利**\n\n研报判断，AI 服务器需要 1608 尺寸 100μF、1005 尺寸 47μF 等高端 MLCC，目前只有村田能稳定量产全部规格。太阳诱电虽在追赶，但等到它能量产时，村田可能已经量产更小、更高容量的产品了。高端市场的护城河在持续拉大。\n\n3️⃣ **短期涨价 vs 长期竞争力**\n\n一个有意思的观察：日系厂商不轻易对通用品提价，因为短期利润最大化反而会降低进入门槛，给中韩台厂商机会。而一些中韩台厂商靠提价赚快钱，研发投入不足，长期会丢失份额。研报认为，这种“提价派”和“产品力派”的估值差距会越来越明显。\n\n[... middle omitted ...]\n\nntinuously enhance product competitiveness is likely to become more pronounced\n\nWhile we expect Ibiden to continue expanding earnings, market consensus appears too high. Our rating remains UW.\n\n[... middle omitted ...]\n\nmi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥5,590</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS MUFG"
  },
  {
    "id": "R043",
    "title": "摩根斯坦利：AI对内存的饥渴，正在改写软件行业的估值逻辑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI对内存的饥渴，正在改写软件行业的估值逻辑\n\n当一家存储芯片公司的季度收入同比暴涨350%，从90亿美元跃升至410亿美元，市场的第一反应往往是“又一个AI基建周期的受益者”。但摩根斯坦利在最新一期《Software Snippets》中给出了一个更值得深思的判断：这轮内存需求的爆发，其结构性可能远大于周期性。\n\n这份报告的核心洞察不在于Micron的财务数字本身，而在于数字背后正在发生的、软件工作负载的深层演变。AI正在从“一问一答”的聊天工具，进化为能够规划、调用工具、阅读文档、保持会话历史、生成子代理并迭代趋近结果的Agent系统。这种从“对话式”到“工作流式”的转变，意味着每一次交互消耗的内存和存储，不再是线性增长，而是指数级膨胀。\n\n> **KC评论：** 市场习惯用“资本开支周期”来理解半导体需求，但摩根斯坦利暗示了一个更本质的变化——AI的“记忆需求”正在从周期性变成结构性。如果Agent成为AI的主流形态，每个Agent都需要长期保持上下文、记忆和工具调用历史，那么内存消耗将不再是“每次对话重置”的临时需求，而是持续存在的固定成本。这对整个软件栈的架构设计、成本模型和定价逻辑，都意味着根本性的重塑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nMicron的财报中最值得关注的细节，不是收入数字本身，而是其背后16份已签署的长期战略客户协议。在半导体行业，长期协议通常意味着两件事：一是需求的确定性足够高，客户愿意锁价锁量；二是供应端开始出现结构性紧张，客户不得不提前锁定产能。\n\n摩根斯坦利的全球半导体团队将此称为“Chipflation——一场记忆体危机”。这个判断的潜台词是：如果内存供给持续偏紧，拥有规模化产能和先进工艺的厂商将\n\n[... middle omitted ...]\n\n”等未解问题有进一步兴趣，欢迎来我们的星球和微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI这一轮，不只是算力在狂欢\n\nAI吃内存，胃口越来越大\n\n内存需求可能进入结构性增长期\n\n---\n\n最近某外资投行出了一份软件板块周报，几个点很有意思，分享给大家。\n\n1️⃣ **AI变“持久”了，内存需求结构升级**\n\n美光刚发了Q3财报，营收同比暴增近350%，达到410亿美元。这背后不只是AI数据中心在扩建，更关键的是AI本身在进化。\n\n从单次对话、简单问答，变成能规划、调工具、读文档、记上下文、生子任务、不断迭代的“智能体”系统。AI越来越“持久”、越来越像完整工作流，就需要更多内存来存和取上下文。\n\n研报判断：这一波内存需求，可能比过去更“结构性”，而非周期性。证据是美光签了16个长期战略客户协议。\n\n2️⃣ **SAP CEO：3-4年后，SAP内部可能没人写代码了**\n\n接受澳洲媒体采访时，SAP CEO Christian Klein说：软件开发是受AI冲击最大的岗位。因为AI编程工具和智能体太强了。\n\n他更强调“劳动力重塑”而非简单减员：“我们需要懂业务、会‘氛围编程’的产品经理，软件开发者需求下降，但数据科学家需求上升。”\n\n这跟SAP在Sapphire 2026大会上的“质量优先”招聘\n\n[... middle omitted ...]\n\n academic publishing (\\*MS Research\\*, #RELX, #Informa, #Wolters Kluwer)\n\n1) Micron blows past 3Q26 earnings expectations as agentic AI's demands rise (#Software): US-listed memory and data st\n\n[... middle omitted ...]\n\nTieto Oyj (TIETO.HE)</td><td>U (01/12/2026)</td><td>€19.06</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R044",
    "title": "摩根斯坦利：MS：AI对内存的“永不满足”胃口，正在改变整个软件业的底层逻辑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI对内存的“永不满足”胃口，正在改变整个软件业的底层逻辑\n\n美光科技最新一季财报让市场不得不重新审视一个问题：AI对内存的需求，究竟是一次性基建周期，还是结构性重置的开始？\n\n6月24日，美光发布2026财年第三季度业绩，营收达到410亿美元，同比增长近350%。一年前，这个数字还只有约90亿。MS在最新一期《Software Snippets》中指出，表面原因是AI数据中心的建设，但更值得关注的软件业信号，藏在工作负载本身的变化里。\n\nAI正在从“一问一答”的聊天模式，转向真正的智能体系统——这些系统会规划任务、调用工具、读取文档、保留会话历史、生成子代理，并反复迭代直至达成目标。这种端到端的持续性工作流，对内存的需求不再是一次性的，而是持续、连贯、结构性的。\n\n美光已经签下了16份长期战略客户协议。这组数字背后，是MS半导体团队近期提出的一个核心问题：这一波内存需求是否比过去更少周期性，更多结构性？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 智能体AI正在把“一次性查询”变成“持久会话”，内存需求从脉冲式变成连续流\n\n理解美光这轮增长的真正含义，需要先理解AI工作模式的演化。\n\n过去两年，大语言模型的主流应用是“提示-响应”模式：用户输入一个prompt，模型生成一段回答，然后对话结束。这种模式对内存的需求是脉冲式的——每次推理需要一定的显存和带宽，但任务完成后资源即可释放。\n\n但智能体AI完全不同。一个典型的智能体工作流包含：理解用户意图、拆解为子任务、调用外部工具（如搜索引擎、数据库、代码解释器）、读取并理解文档内容、保持对多轮对话上下文的记忆、生成中间结果并自我校验、根据反馈调整策略。整个过程可能持续数分钟甚至数小时，期间需要持续保持大量上下文数据在高速存储中。\n\nMS认为，\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI对内存的胃口，比想象中大\n\nAI吃掉了多少内存？\n\nAI正在从“问一句答一句”变成“自己规划、调用工具、读文档、保留对话历史、生成子任务、反复迭代”的智能体系统。这个过程对内存的需求指数级增长——某外资投行最新研报指出，这种需求可能从周期性变成结构性。\n\n1️⃣ **内存需求的结构性拐点**\n美国存储公司美光最新季度营收同比暴增近350%，从约90亿美元飙到410亿美元。表面看是AI数据中心建设，但研报更关注工作负载本身的变化——AI越像“智能体”，需要的上下文存储和检索就越多。美光已签下16份长期战略客户协议，暗示需求可能不再像过去那样周期波动。\n\n2️⃣ **SAP CEO：3-4年后可能没人写代码了**\nSAP掌门人表示，软件开发是受AI冲击最大的岗位。“3-4年内，SAP内部可能不再有人类开发者。”但他强调这不是简单裁员，而是岗位重塑——需要更懂业务的产品经理来“vibe code”，需要更多数据科学家。SAP在2026年Sapphire大会上提出了3:1替换比例（1个顶级AI专家替换3个传统员工）。\n\n3️⃣ **学术出版界的AI效率革命**\nSpringer Nature举办的科技活动显示，学\n\n[... middle omitted ...]\n\n academic publishing (\\*MS Research\\*, #RELX, #Informa, #Wolters Kluwer)\n\n1) Micron blows past 3Q26 earnings expectations as agentic AI's demands rise (#Software): US-listed memory and data st\n\n[... middle omitted ...]\n\nTieto Oyj (TIETO.HE)</td><td>U (01/12/2026)</td><td>€19.06</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R045",
    "title": "摩根斯坦利：MS：AI算力基建的下一个瓶颈不是芯片，是电和地",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI算力基建的下一个瓶颈不是芯片，是电和地\n\n全球AI基础设施的建设正站在一个历史性的拐点上。英伟达GPU的持续迭代与Agentic AI框架的崛起，正在将算力需求推向一个前所未有的量级。当市场目光仍聚焦于芯片性能竞赛与模型参数规模时，MS在一份面向亚太投资者的专题报告中，提出了一个关键的判断：真正的稀缺资源，正在从硅片转向土地、电力与冷却能力。而东南亚，正处在这场结构性变迁的独特交汇点。\n\n这份报告的价值不在于复述“AI浪潮来了”的共识，而在于它为投资者提供了一个框架：如何在一个物理资源而非技术性能成为瓶颈的时代，重新定位基础设施投资的价值链。报告的核心洞察可以浓缩为一句话：未来的算力之争，本质上是能源与空间之争。\n\n> **KC评论：** MS这个判断的意义在于，它把投资者的注意力从“谁的芯片更强”转向了“谁能把电和地变成可租用的算力”。对于非技术背景的决策者来说，这意味着评估一家数据中心运营商的价值，不再主要看它用了什么服务器，而是看它拿了多少地、签了多少电力协议、拿到了哪些审批。这是理解这份报告所有后续分析的基石。\n\n报告的叙事逻辑非常清晰：先拆解数据中心的物理构成与商业模式，再分析东南亚作为新兴枢纽的禀赋条件，最后落到具体标的——尤其是新加坡电信Singtel的AI基础设施布局。这种从宏观产业趋势到微观公司价值的推导，正是金字塔原理的典型应用。以下是我们从中提炼的几个关键层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化的本质是算力密度从“房间级”跃迁到“机架级”，改变了整个选址逻辑\n\n传统企业数据中心的单机架功耗通常在5-15千瓦。而一个AI GPU机架，当前的需求已飙升至40-200千瓦，下一代平台更是直奔数百千瓦级别。这不仅仅是数字的放大，而是整个工程范式的切换。\n\n[... middle omitted ...]\n\n讨论这份报告没有完全展开的细节，以及它对资产定价的潜在影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI基建新主战场：东南亚数据中心\n\n东南亚，正在成为AI算力的新枢纽\n\n最近翻到一份外资投行的研报，把东南亚数据中心讲得特别透。核心逻辑很简单：AI时代算力需求暴增，但全球数据中心最饱和的是美国，东南亚反而成了稀缺的价值洼地。\n\n为什么是东南亚？三个硬条件：\n1️⃣ 土地充足、电力成本低\n2️⃣ 海底光缆枢纽（新加坡是核心节点）\n3️⃣ 各国开始推“主权AI”战略，数据本地化需求上升\n\n数据中心不是“盖房子”那么简单。\n研报拆得很细：\n- 传统机柜：5-15kW\n- AI GPU机柜：40-200kW（直接翻4倍）\n- 下一代AI平台：几百kW起步\n\n功率密度变了，整个供应链都得重做。冷却从风冷→液冷→浸没式，供电从普通配电→高压直流。\n\n更关键的是，AI训练和推理的选址逻辑完全不同：\n- 训练：靠近廉价电力，集中式大型集群\n- 推理：靠近用户，低延迟+数据主权重要\n\n所以东南亚的定位很清晰：既是训练基地（电便宜），又是推理节点（靠近亚太市场）。\n\n研报重点提了Singtel的AI工厂布局，从连接层→数据中心→GPU即服务→编排平台，四层堆叠。还通过收购STT GDC（50个数据中心、673MW在运）快速扩张\n\n[... middle omitted ...]\n\n including AI data centers’ anatomy and economics, the value chain, Singtel’s AI infrastructure positioning, and the potential emergence of orbital data centers as a long-tail disruptor.\n\n## R\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R046",
    "title": "摩根斯坦利：MLCC真正的赢家不是提价，而是产品迭代",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MLCC真正的赢家不是提价，而是产品迭代\n\n2026年6月，摩根斯坦利分析师在新加坡和香港与机构投资者举行了31场一对一会议和两场午餐会。讨论的焦点不是宏观经济，不是地缘政治，而是两个看似不起眼的电子元器件：MLCC（多层陶瓷电容）和ABF封装基板。\n\n但这份路演纪要透露出的信号，远比元器件本身重要。它指向一个正在发生的结构性分化：那些靠涨价赚快钱的公司，与那些通过持续产品迭代构筑护城河的公司，其企业价值差距正在急剧拉大。\n\n投资者几乎把所有注意力都放在了“普通MLCC能涨多少价”上，却忽视了真正驱动盈利增长的引擎——AI服务器对高端MLCC的需求正在以每年接近翻倍的速度扩张。这个误判，可能正在制造一个显著的定价偏差。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 投资者盯着价格，但真正的利润藏在产品结构里\n\n摩根斯坦利的调研发现了一个有趣的认知错位。在与机构投资者的交流中，几乎所有问题都围绕着一个主题：普通MLCC还能涨多少价？很少有人问：AI服务器带来的高端MLCC增长能持续多久？\n\n这种关注点的错位，恰恰是超额收益的来源。\n\n报告的核心判断非常清晰：村田制作所的MLCC业务，即便不主动提价，其ASP（平均售价）也会因产品结构改善而显著增长。具体来说，在AI服务器加速器板卡上，每一代新GPU对MLCC的总容值需求大约翻倍，而安装空间却在缩小。这推动了对小型化、高容值、高附加值MLCC的持续需求。\n\n村田对此做了三件事：优化钛酸钡（关键材料）的粒径并使其均匀化、增加层数、缩小外部电极宽度以增加介电层体积。这些技术细节听起来很技术性，但结果很直接——它让村田成为目前唯一能稳定量产AI服务器所需全部高端MLCC的企业。\n\n> **KC评论：** 投资者习惯用“价格涨没涨”来判断元器件公司的景气度，但\n\n[... middle omitted ...]\n\n信群继续讨论，围绕这些尚未完全回答的问题，一起跟踪行业变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC 不是涨价，是结构变了\n\nAI 服务器拉出第二曲线\n\n📌 当所有人都在问“MLCC 会不会涨价”，真正的故事是：产品结构在变，而不是单纯提价。\n\n某外资投行近期在新加坡和香港和机构投资者开了 31 场一对一会议，核心讨论 MLCC 和 ABF 载板。几个关键判断值得关注👇\n\n1️⃣ **村田的 ASP 增长 ≠ 涨价**\n- 研报认为，村田 MLCC 的 ASP 增长来源于高附加值产品占比提升，而非对同一产品提价。\n- AI 服务器加速卡每代 GPU 需要的 MLCC 总容量约翻倍，但安装空间有限，推动小尺寸、高容值 MLCC 需求。\n- 预计 F3/27 村田 AI/数据中心 MLCC 销售同比增 85-90%，其中量增约 40%，ASP 增约 50%——后者来自产品组合升级。\n\n2️⃣ **高附加值 MLCC 市场：村田一家独大**\n- 2025 年 AI 服务器高附加值 MLCC 市占率：村田 40.8%、三星电机 22.5%、太阳诱电 11.3%。\n- 1608 尺寸 100μF、1005 尺寸 47μF、0603 尺寸 10μF 等需求激增，但只有村田能稳定量产全部规格。\n- 太阳诱电产能增\n\n[... middle omitted ...]\n\nntinuously enhance product competitiveness is likely to become more pronounced\n\nWhile we expect Ibiden to continue expanding earnings, market consensus appears too high. Our rating remains UW.\n\n[... middle omitted ...]\n\nmi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥5,590</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS MUFG"
  },
  {
    "id": "R047",
    "title": "摩根斯坦利：MS：AI基建的下一站不在美国，在东盟",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI基建的下一站不在美国，在东盟\n\n当全球资本还在争论美国数据中心是否已经过热时，一份来自MS的投资者演示材料提出了一个值得深思的判断：AI基础设施建设的下一个结构性机会，可能出现在一个被多数投资者低估的区域——东盟。\n\n这不是一个关于“东南亚是否值得关注”的泛泛之谈。报告的核心主张非常具体：东盟正处在AI基础设施建设的独特交汇点上——拥有充足的廉价土地和电力、战略性的海底光缆连接、以及正在崛起的主权AI需求。这三个要素的组合，在全球范围内几乎找不到第二个区域同时具备。\n\n更为关键的是，这份报告不是停留在宏观叙事层面。它提供了一套完整的“数据中心投资指南”，从资产解剖到商业模式拆解，再到具体标的的估值分析，最后甚至讨论了一个可能改变游戏规则的长期变量——轨道数据中心。\n\n我们将其核心判断提炼为以下五个层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI数据中心的核心瓶颈已经从“空间”转向“功率密度”，这改变了整个投资逻辑\n\n传统数据中心的核心指标是面积和机柜数量。但AI训练和推理的需求完全不同。报告指出，一个AI GPU机架的功率密度已经从传统企业级机架的5-15千瓦飙升至40-200千瓦，下一代平台甚至可能达到数百千瓦级别。\n\n这意味着什么？简单说，过去建数据中心像建仓库，核心是“能放多少货”。现在建数据中心更像建发电厂，核心是“能接入多少电和怎么散热”。\n\n> **KC评论：** 投资者需要重新理解数据中心的“产能单位”。过去看数据中心，核心指标是面积和机柜数。现在要看MW（兆瓦）的可用容量和利用率。一个能支持200千瓦/机架的数据中心，其资本开支结构和运营逻辑与支持5千瓦的完全不同。这份报告里有一张“DC Anatomy”图，详细拆解了从电网连接到机柜散热的全链条，值得仔细研究。\n\n[... middle omitted ...]\n\n微信群里继续讨论这些未解问题，我们会持续追踪并分享后续观点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n东南亚数据中心：新算力时代的赢家\n\nAI算力基建的下一站\n\n东南亚正成为全球AI基础设施建设的独特交汇点\n\n1/ AI数据中心不是普通仓库\n- 核心瓶颈从空间转向电力密度、散热和网络\n- 传统企业机柜5-15kW，AI机柜已到40-200kW，下一代直接数百kW\n- 液冷从可选变成必须：直接芯片冷却、浸没式冷却正成为标配\n\n2/ 东南亚凭什么？\n- 土地充裕、电价有竞争力、海底电缆枢纽地位突出\n- 新加坡是东南亚海底光缆最密集节点\n- 马来西亚、泰国、印尼正成为数据中心新集群\n- 各国主权AI需求催生本地化部署\n\n3/ 别把每个兆瓦混为一谈\n- AI训练需要靠近廉价电力，集中化部署\n- AI推理更看重延迟，需要靠近用户和数据主权区域\n- 一个AI就绪的兆瓦，其资本开支和散热规格完全不同\n\n4/ 赢家不止是建房子的\n- 运营商需要掌握稳定电力、液冷技术、密集光纤\n- 新加坡电信的AI工厂模式值得关注：从托管到GPU即服务再到AI编排\n- 收购STT GDC后，运营规模达673MW，覆盖12个市场\n\n5/ 太空数据中心是远期期权\n- 地面瓶颈是电力，轨道有无限太阳能和散热优势\n- 但需解决发射成本、辐射防护、轨道\n\n[... middle omitted ...]\n\n including AI data centers’ anatomy and economics, the value chain, Singtel’s AI infrastructure positioning, and the potential emergence of orbital data centers as a long-tail disruptor.\n\n## R\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R048",
    "title": "IMF对爱尔兰发出罕见警告：繁荣背后，跨国公司依赖正成为最大风险",
    "digest": "[wechat_article.md]\n# IMF对爱尔兰发出罕见警告：繁荣背后，跨国公司依赖正成为最大风险\n\n爱尔兰经济正站在一个罕见的十字路口。一方面，2025年国内经济增速约4%，财政持续盈余，就业市场虽有所降温但仍处于历史较好水平。另一方面，国际货币基金组织在2026年6月发布的最新国别磋商报告中，用了一个不常见的措辞——“不能将韧性视为理所当然”。\n\n这份报告的核心判断值得每一个关注全球产业链和发达国家财政可持续性的读者认真对待：爱尔兰当前的强劲表现，很大程度上建立在跨国公司税收和投资的集中度之上，而这一模式在日益碎片化的全球环境中正变得脆弱。更关键的是，IMF认为爱尔兰需要利用当前“窗口期”进行结构性改革，否则繁荣可能难以持续。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 跨国公司依赖既是增长引擎，也是结构性脆弱的核心来源\n\n爱尔兰的经济表现与跨国公司深度绑定。2025年，由跨国公司主导的出口表现强劲，企业所得税收入持续支撑财政盈余。但IMF明确指出，这种依赖是“脆弱性的关键来源”。\n\n报告的论证逻辑很清晰：地缘经济碎片化加剧、供应链重组、贸易和资本流动的重新配置，都会对爱尔兰这种高度全球化的经济体产生不对称冲击。跨国公司并非不忠诚，但它们作为全球性实体，会根据税收、监管和地缘风险的变化调整布局。一旦全球税收协调或地缘格局发生重大变化，爱尔兰的财政收入和经济增长可能面临双重压力。\n\n> **KC评论：** 这里的关键不是跨国公司会不会离开，而是“依赖”本身就是一种无法对冲的风险。投资者需要关注的是，爱尔兰财政盈余中来自跨国公司企业所得税的部分是否可持续。报告中的财政数据表显示，2025年一般政府盈余占GNI*的比例为3.3%，但结构性赤字已经达到-1.8%，这意味着剔除周期性因素后，财政基础并不像表面那么健康。\n\n---\n\n![研报图表\n\n[... middle omitted ...]\n\n，或者希望每天收到类似的分析，欢迎加入我们的社群。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n爱尔兰经济，撑得住吗？🇮🇪\n\n📌 短期韧性仍在\n📌 但长期挑战不少\n\n最近翻到IMF对爱尔兰的最新评估，发现这个“欧洲硅谷”的处境，比想象中复杂。\n\n1️⃣ 增长放缓，但没崩\n2025年国内经济（修正后的GNI*）增长了约4%，消费和投资都不错。但2026年预计增速会降到2%左右，通胀压力也上来了，能源价格是主要推手。\n\n2️⃣ 外资依赖，是双刃剑\n跨国公司贡献了大部分企业税，让财政有钱。但一旦全球供应链重组或地缘风险加剧，爱尔兰这种高度开放的经济体首当其冲。\n\n3️⃣ 房地产和基建，老问题还在\n住房短缺、电网老化、绿色转型需要大笔钱。IMF建议加快公共投资，但得管好预算，别超支。\n\n4️⃣ 非银行金融，风险在积聚\n爱尔兰有庞大的非银行金融部门，杠杆和流动性错配可能放大风险。央行需要持续盯着。\n\n5️⃣ 财政空间，要省着用\n目前财政有盈余，但老龄化、绿色转型都是长期支出。IMF建议拓宽税基（比如提高个税、增值税），别光靠跨国公司的企业税。\n\n2026年GDP预计会小幅负增长（受跨国公司利润波动影响），但修正后的国内需求还能保持正增长。失业率会从4.7%微升到5%，整体就业市场还算稳定。\n\n你觉得爱尔兰这种“小\n\n[... middle omitted ...]\n\n and policies. Based on information available at the time of these discussions, the staff report was completed on June 10, 2026.\n\n• An Informational Annex prepared by the IMF staff.\n\nThe docum\n\n[... middle omitted ...]\n\n1, 2022. The FSSA and accompanying Reports on the Observation of Standards and Codes (ROSCs) are available at https://www.imf.org/en/Publications/CR/Issues/2022/07/07/Ireland-Financial-System-Stability-Assessment-520469."
  },
  {
    "id": "R049",
    "title": "IMF：爱尔兰的AI红利，比关税更值得关注",
    "digest": "[wechat_article.md]\n# IMF：爱尔兰的AI红利，比关税更值得关注\n\n当全球目光聚焦于美国关税政策的反复与地缘贸易谈判的博弈时，一份来自国际货币基金组织（IMF）的最新爱尔兰国别报告，提出了一个更具结构性的判断：对爱尔兰这样的小型开放经济体而言，贸易政策调整带来的更多是贸易流向的重新分配，而真正能驱动产出和出口增长的引擎，是人工智能驱动的生产率提升。这份报告通过一个多区域、多部门的可计算一般均衡模型，量化了贸易政策、AI和能源转型三大力量对爱尔兰的长期影响。其核心结论对于理解全球知识密集型经济体的未来竞争逻辑，具有超越爱尔兰一国的启示意义。\n\n报告直言，当前的关税和贸易协定冲击，主要效果是“重新路由”贸易伙伴和行业间的流向，对爱尔兰整体GDP和出口的宏观影响相当温和。相比之下，AI驱动的生产率提升则能带来强劲的产出和出口增长，尤其在知识密集型部门，同时也会引发显著的跨行业劳动力重新配置。而碳定价政策，则可能在AI推高能源需求和排放的背景下，成为平衡增长与脱碳目标的关键工具。\n\n> **KC评论：** 这份报告的价值在于，它用一个统一的框架，同时考察了三个通常被分开讨论的变量。它揭示了一个关键权衡：AI带来的增长红利，可能会被其催生的能源需求部分抵消。理解这三者如何互动，比孤立地看任何一个政策都更重要。完整报告中的图表和分行业数据，清晰地展示了这种权衡的量化程度。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 贸易战对爱尔兰的冲击，远小于市场直觉\n\n在关税与贸易协定情景下，IMF模型得出的结论可能会让一些投资者感到意外：美国在2025年底实施的关税，对爱尔兰整体经济的负面影响非常有限。报告显示，即使在最极端的组合情景（美国关税叠加欧盟与南方共同市场、欧盟与印度的自贸协定）下，爱尔兰实际GDP的增幅也低于0.20%。\n\n这背后的机制是什么？核心\n\n[... middle omitted ...]\n\n所有原始图表，并参与我们关于AI、贸易与能源转型的深度讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI、关税、碳税…三件事怎么影响爱尔兰？\n\nAI冲击下的爱尔兰\n\n某外资投行最新研报，把AI、贸易摩擦、能源转型放在一起看爱尔兰。信息量很大，逻辑很清晰，我帮你拆成三条。\n\n1️⃣ 贸易关税：效果不大，主要是“改道”\n- 美国加关税，全球GDP只降0.13%，出口降2.84%\n- 对爱尔兰影响更小，因为它的王牌出口（药品）被加税少\n- 同时欧盟和印度、南美签FTA，又能把贸易流拉回来一些\n- 结论：关税更多是“谁跟谁做生意”的调整，总量影响有限\n\n2️⃣ AI生产率提升：这才是真正的增长引擎\n- 高场景下，爱尔兰GDP可以涨11%、出口涨15%\n- 受益最大的是知识密集型服务业（金融、保险、商业服务）\n- 但代价是劳动力会大规模跨行业流动，需要配套政策\n- 而且AI会推高能源需求，碳排放压力加大\n\n3️⃣ 碳定价：用来对冲AI带来的排放\n- 如果AI高增长但不加碳价，爱尔兰的碳排放会明显上升\n- 研报模拟了在AI场景下加碳价，把排放“锁”在基准水平\n- 单独减碳20%的场景下，GDP会下降约1.4%，出口降9%\n- 碳价能推动电力结构转向可再生能源，但短期有经济成本\n\n💡 三件事合在一起看，核心矛盾是：AI带\n\n[... middle omitted ...]\n\nLAND\n\nSELECTED ISSUES\n\nJune 10, 2026\n\nApproved By\n\nPrepared by Mohammad Khabbazan (ICD)\n\nEuropean Department\n\n## CONTENTS\n\nESTIMATING THE IMPACTS OF AI, TRADE POLICY, AND THE ENERGY TRANSITION\n\n[... middle omitted ...]\n\nelligence in G7 Economies. OECD Artificial Intelligence Papers No. 41, Paris.\n\nWorld Trade Organization (WTO) and International Monetary Fund (IMF). 2026. WTO–IMF Tariff Tracker. WTO Tariff & Trade Data Platform, Geneva."
  },
  {
    "id": "R050",
    "title": "世界银行：毛里塔尼亚的韧性不是运气，是制度",
    "digest": "[wechat_article.md]\n# 世界银行：毛里塔尼亚的韧性不是运气，是制度\n\n当一个经济体在战争、边境封锁、大宗商品价格剧烈波动的夹击下，仍能保持宏观稳定、让公共债务从52%降至40%，外界往往将其归因于“资源禀赋”或“外部援助”。但世界银行与IMF联合发布的这份毛里塔尼亚最新融资安排评估报告揭示了一个更深刻的判断：这一轮韧性，核心驱动力是制度性改革，而非资源周期。\n\n2026年6月，IMF执行董事会批准了毛里塔尼亚新一轮42个月的ECF/EFF安排，总额9580万美元。这并非简单的续贷。该机构同时完成了RSF的第五次也是最后一次审查，标志着该国在气候韧性领域的制度框架已初步成型。报告传递的核心信号是：一个长期依赖资源出口、被列为“脆弱国家”的西非经济体，正在通过财政规则法制化、社会登记系统数字化、国有企业监督透明化，构建一套能够抵御外部冲击的制度护城河。\n\n对于关注新兴市场债务、资源型经济体转型、以及全球南方治理范式的读者而言，这份报告的真正价值不在于毛里塔尼亚本身，而在于它提供了一个“小国如何在大国博弈与气候冲击中守住底线”的可复制样本。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮增长放缓揭示了一个结构性拐点：非资源部门正在接过接力棒\n\n2025年毛里塔尼亚实际GDP增速从2024年的6.3%回落至4.0%。表面看是“减速”，但拆解数据后会发现，这恰恰是经济结构改善的证明。\n\n放缓的直接原因在于采掘业收缩——2025年该部门预计下降0.6%，而2023年曾增长12.2%。大宗商品价格波动、GTA天然气项目相关进口下降，共同压低了资源板块的贡献。但非采掘业GDP仍保持了5.1%的增长，虽低于2024年的7.3%，却远高于疫情前水平。\n\n真正值得关注的是：非资源部门的扩张正在逐步消化资源部门的波动性。2021年非采掘业占GDP比重尚不足70\n\n[... middle omitted ...]\n\n如果你对“小国治理转型”这一主题感兴趣，欢迎加入我们的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n毛里塔尼亚，IMF又给了9千万美元\n\n🌍 穷国也能逆袭？\n\nIMF刚批了毛里塔尼亚新一笔42个月贷款，总额9580万美元。不是白给，是带着条件来的。\n\n1️⃣ 先看成绩单\n- 2022-2026年的老项目，执行得不错\n- 非矿业经济增长一直稳，通胀降了\n- 经常账户赤字收窄，外汇储备够用\n- 财政纪律也守住了，债务占GDP从52%降到40%\n\n2️⃣ 新项目三大支柱\n- 稳住宏观：加强财政制度、政策框架\n- 减贫+增长：靠私营部门带动，不是靠政府砸钱\n- 治理升级：国企改革、反腐、透明度\n\n3️⃣ 有意思的细节\n- 毛里塔尼亚搞了个“社会登记册”，能精准找到最穷的40%人口发钱\n- 油价涨了，政府没直接补贴油价，而是给穷人发定向现金\n- 国企数据以前是黑洞，现在要用IMF工具定期汇报\n\n4️⃣ 风险还在\n- 中东冲突推高石油进口成本\n- 马里边境冲突影响贸易通道\n- 气候变化：干旱、洪水，都需要钱去适应\n\n🌟 核心逻辑：穷国要发展，光靠借钱不行。得把制度建起来，让钱花对地方，让私营企业长出来。\n\n你觉得这套“贷款+改革”的模式，对发展中国家真的有效吗？\n\n#学习笔记\n\n[source_mineru.md]\n#\n\n[... middle omitted ...]\n\nlity, Cancellation of the Current Arrangements Under the Extended Fund Facility and the Extended Credit Facility, and Fifth Review Under the Resilience and Sustainability Facility Arrangement,\n\n[... middle omitted ...]\n\nram performance and the authorities' steadfast commitment, we would appreciate Executive Directors' support for the approval of the new 42-month ECF/EFF arrangements, and the completion of the Fifth Review under the RSF."
  },
  {
    "id": "R051",
    "title": "IMF：西班牙需要的不只是资本缓冲，而是贷款发放时的“刹车”",
    "digest": "[wechat_article.md]\n# IMF：西班牙需要的不只是资本缓冲，而是贷款发放时的“刹车”\n\n当西班牙房价在疫情期间加速攀升、高风险房贷占比持续上升时，一个核心问题浮出水面：西班牙银行体系目前看似健康的资产负债表，是否足以抵御下一轮房地产下行周期？\n\n国际货币基金组织（IMF）在2026年6月发布的一份Selected Issues Paper中给出了一个明确的判断：不够。这份题为《The Case for Borrower-Based Macroprudential Measures in Spain》的报告，通过贷款级数据和压力测试，论证了一个被西班牙央行至今未采纳的政策工具——借款人导向的宏观审慎措施（BBMs）——为何在当前时点变得必要。\n\n这不是一份泛泛的风险警示。它直接指向一个关键的制度缺口：西班牙是欧元区银行业联盟中少数几个尚未激活任何BBM的国家之一。当18个欧元区国家已至少实施一项LTV或LSTI上限时，西班牙仍然完全依赖资本缓冲来吸收损失。IMF认为，这种“事后吸收”而非“事前预防”的框架，可能正在积累系统性脆弱性。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 房价上涨与贷款标准放松的组合，正在制造一个未被资本缓冲覆盖的风险敞口\n\n西班牙的总体家庭杠杆率确实低于欧元区平均水平，这常常被引用来证明“西班牙没有房贷风险”。但IMF指出，这个总量指标掩盖了结构性问题：自2023年以来，新发放贷款中贷款价值比（LTV）超过80%的占比持续上升。换句话说，平均数据看似健康，但边际上的贷款质量正在恶化。\n\n报告的核心逻辑链条是：持续强劲的房价上涨，加之地缘政治不确定性，可能在未来某个时点引发房价调整。而一旦房价下跌，那些高LTV贷款的借款人将面临负资产风险，违约概率将显著上升。问题是，西班牙现有的逆周期资本缓冲（CCyB，将于2026年\n\n[... middle omitted ...]\n\n集。既方便直接喂给AI分析，也方便人工快速把握全球市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n西班牙房贷风险在上升，央行该出手吗\n\n**房贷风险暗涌**\n\n西班牙房价涨了，高风险贷款占比也在悄悄升高\n\n---\n\n最近翻到IMF一篇关于西班牙房贷市场的分析，信息量很大，简单拆解一下核心逻辑：\n\n**1. 表面平静，水下有暗流**\n- 西班牙家庭整体杠杆率在欧元区算低的，看上去很健康\n- 但新发放贷款中，LTV（贷款房价比）超过80%的比例从2023年开始持续上升\n- 这意味着新买房的人首付更低，杠杆更高，违约风险在积累\n\n**2. 为什么现在讨论这个？**\n- 西班牙目前没有激活“借款人端宏观审慎工具”（BBMs）\n- 但欧元区18/21个国家都已经在用这类工具了\n- IMF建议：早用比晚用好，等风险积累到一定程度再收紧，反而更容易引发市场波动\n\n**3. 哪种工具最有效？**\n- 研究用了西班牙的贷款级数据和压力测试\n- 结论很明确：LTV上限（比如贷款不超过房价80%）对降低违约风险效果最大\n- 如果同时加一个收入上限（比如月供不超过月收入40%），效果更好\n- 这两者互补：LTV管的是“你亏了银行能收回多少”，收入上限管的是“你会不会还不起”\n\n**4. 和现有政策不冲突**\n- 西班牙已经在逐步\n\n[... middle omitted ...]\n\nby Romain Duval\n\nJune 2026\n\nIMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information av\n\n[... middle omitted ...]\n\ntr><tr><td>Income growth</td><td>6.0</td><td>5.1</td><td>4.2</td><td>4.4</td><td>4.0</td><td>4.0</td></tr><tr><td>House prices</td><td>8.5</td><td>7.6</td><td>6.7</td><td>-4.3</td><td>-11.0</td><td>-5.6</td></tr></table>"
  },
  {
    "id": "R052",
    "title": "IMF：西班牙地方财政的顺周期陷阱，需要一个支出增长锚",
    "digest": "[wechat_article.md]\n# IMF：西班牙地方财政的顺周期陷阱，需要一个支出增长锚\n\n西班牙的自治区（Autonomous Communities）承担了全国超过四分之一的公共支出，尤其是在教育和医疗这两个与长期人力资本最相关的领域。然而，IMF最新一份Selected Issues Paper揭示了一个令人不安的事实：过去二十年，西班牙地方政府的公共支出不仅没有起到稳定经济的作用，反而在衰退期间大幅削减了教育和医疗开支——这在欧元区主要国家中几乎是独一无二的。\n\n这份由IMF欧洲部经济学家Carlo Pizzinelli撰写的报告，核心判断清晰而锐利：西班牙现行的多重地方财政规则没有实现两个基本目标——避免顺周期支出和确保债务可持续性。而欧盟新经济治理框架的落地，恰好为改革提供了一个制度窗口。\n\n报告建议，将地方财政规则的核心从复杂的赤字、债务、支出增速多重目标，简化为一个以支出增长为锚的单一规则。这不仅是技术调整，更是一次财政哲学的重塑。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 西班牙地方政府的顺周期支出，在欧元区是一个异类\n\n报告通过2004至2024年的面板数据回归发现，西班牙自治区的总支出与地区GDP之间存在显著的正相关关系——这意味着经济好的时候多花钱，经济差的时候少花钱。更令人警惕的是，这种顺周期特征在2008年全球金融危机之后变得更加明显。\n\n> **KC评论：** 顺周期支出本身并不罕见，罕见的是西班牙地方政府的支出顺周期主要集中在教育和医疗领域。报告对比了欧元区其他主要国家，发现这些国家的教育和医疗支出基本是逆周期或非周期的——经济下行时，中央政府会通过转移支付维持这些基本公共服务的稳定。而西班牙的自治区在危机中被迫削减了这些最不应该削减的开支。\n\n这种做法的代价是长期的。报告引用文献指出，衰退期间削减教育和\n\n[... middle omitted ...]\n\n便喂给AI做进一步分析，也方便你快速把握全球资本市场的脉搏。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n地区财政规则，该改改了\n\n地区支出，别跟着经济周期起舞\n\n地方财政的顺周期陷阱，是时候拆解了\n\n最近IMF一篇关于西班牙自治区财政规则的研究，把地方财政管理的老问题翻出来晒了晒。核心发现很直接：现行框架没做到两件事——避免顺周期支出和确保债务可持续。\n\n1/ 西班牙自治区的支出大头是教育和医疗，占GDP约18%。这些是刚需，不该随经济好坏大起大落。但数据打脸：2004-2024年，地区总支出与GDP正相关，经济下行时反而砍支出，尤其是教育和医疗。\n\n2/ 对比欧元区同类国家，西班牙的教育医疗支出顺周期特征突出。而理论上，这类支出应该“无周期”——既不需要逆周期刺激，也不该顺周期收缩。砍教育和医疗会延长衰退，造成人力资本长期损伤（经济学叫“滞后效应”）。\n\n3/ 问题根源：现行规则同时盯着赤字、支出增长和债务三个目标，内部矛盾。比如经济差时，要控赤字就得砍支出，但支出砍的是教育和医疗。而且规则缺乏有效执行机制，违规成本低。\n\n4/ 解决方案方向：把规则核心换成“支出增长上限”，与欧盟新框架对齐。关键设计：\n- 支出增速锚定长期GDP趋势，而非当年经济表现\n- 高负债地区（超13%GDP债务门槛）适用更紧的支出上\n\n[... middle omitted ...]\n\nf Autonomous Communities: Its Macroeconomic Effects and the Role of the National Fiscal Rule\\* Prepared by Carlo Pizzinelli\n\nAuthorized for distribution by Romain Duval\nJune 2026\n\nIMF Selected\n\n[... middle omitted ...]\n\nendent variables include lags 2 to 10. Instruments for regional GDP growth include growth of neighboring regions and Spain&#x27;s trading partner growth.</td></tr></table>\n\nSources: IGAE, INE, and IMF staff calculations."
  },
  {
    "id": "R053",
    "title": "兰德公司：兰德报告：英国司法融资的“危机-修复”循环，正在耗尽最后一点改革空间",
    "digest": "[wechat_article.md]\n# 兰德公司：兰德报告：英国司法融资的“危机-修复”循环，正在耗尽最后一点改革空间\n\n英国刑事司法系统正陷入一个自我强化的恶性循环：法庭积压突破8万件，监狱超容运行超过12年，而政府每增加一笔拨款，几乎都流向了“灭火”而非“防火”。兰德公司最新发布的《为正义融资》报告，系统性地揭示了这一结构性困境，并提出了一个在主流政策辩论中常被忽视的出路——私人资本与结果导向的融资模式。但报告更深层的追问是：在财政纪律与政治周期双重约束下，这些试验能否从“漂亮案例”走向“系统解法”？\n\n这份报告的核心判断值得每一位关注公共财政与治理效率的读者认真对待：英国司法系统的根本问题不是缺钱，而是缺一种能够将资金从前端预防导向后端成本的融资机制。传统的政府预算拨款模式，在应对日益复杂的犯罪类型和不断膨胀的案件量时，已经显示出系统性的失灵。\n\n> **KC评论：** 这不是一份关于“司法危机”的泛泛之谈，而是一份关于“钱从哪里来、花到哪里去、效果如何衡量”的硬核分析。报告没有停留在“多拨钱”的简单呼吁，而是拿出了具体的金融工具与案例数据。对于关注政府效率、社会影响力投资或公共管理创新的读者，这份报告提供了难得的实操视角。完整报告包含多个未在本文展开的融资模型对比图表，值得细读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n报告开篇即点明一个反直觉的事实：尽管英国政府在过去几年中大幅增加了对监狱基础设施的资本投入——2025年支出审查承诺在2024-2030年间投入70亿英镑用于监狱建设，新增1.4万个床位——但根据英国国家审计署的预测，到2027年底，监狱需求仍将超过可用容量1.24万个位置。这意味着，即便所有在建项目按时交付，缺口依然存在。\n\n这一数据揭示了一个更深层的结构性矛盾：司法系统的需\n\n[... middle omitted ...]\n\n便喂给AI进行深度分析，也方便你快速把握全球市场与政策动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n英国司法系统快撑不住了：钱去哪了？\n\n**资金缺口**\n司法经费被挤占，系统快转不动了\n\n**刑事案件积压8万件，监狱常年满员**\n\n英国刑事司法系统正面临一场隐形危机。投行研报指出，英格兰和威尔士的刑事案件积压已接近8万件，监狱占用率连续12年超过95%。这不是小修小补能解决的问题。\n\n**司法经费被“遗忘”了**\n\n1. 经费缩水：司法部实际开支比2007年峰值低了14%，人均降幅达24%。同期政府总支出反而涨了10%。\n2. 人员流失：法院永久员工减少30%，缓刑服务人员缺口达30%。\n3. 需求激增：性犯罪案件一年增加11%，欺诈案飙升33%，但法院处理能力跟不上。\n\n**钱都花哪了？**\n\n政府选择把有限的资金砸向“救火”——建新监狱、增加法庭开庭日。但预防性投入严重不足。研报算了一笔账：每投1英镑免费早期法律咨询，能为政府省下2.71英镑下游成本。\n\n**私人资本能帮忙吗？**\n\n研报介绍了几个创新融资模式：\n- 社会影响债券：投资者先出钱，政府按效果付费。HMP Peterborough试点显示，重新犯罪率降了8.4%，投资者拿回了本金和回报。\n- 社会企业模式：Skill Mill雇佣1\n\n[... middle omitted ...]\n\nnstrained resources and increasing complexity. This latest briefing, ‘Financing justice’, examines a fundamental question: whether the way we fund justice today is capable of meeting the deman\n\n[... middle omitted ...]\n\nn of new Electronic Monitoring services. He also leads PA and the PA Foundation's award-winning Second Chance Programme, working with a group of rehabilitation charities to enable innovative approaches to rehabilitation."
  },
  {
    "id": "R054",
    "title": "兰德公司：仅半数校长认为课后班与课堂衔接，结构性断层比想象中更深",
    "digest": "[wechat_article.md]\n# 兰德公司：仅半数校长认为课后班与课堂衔接，结构性断层比想象中更深\n\n当教育系统将课后项目视为弥补疫情学习损失的关键抓手时，一份来自兰德公司的全国性调查给出了一个耐人寻味的数据：在全国范围内，仅有约半数的公立学校校长认为，他们学校的课后项目在学术上与课堂内的教学是“对齐”的。更值得关注的是，这个比例背后隐藏着深刻的阶层、学段和治理结构差异。\n\n这份基于对全美1038名K-12公立学校校长调查的报告，并非一份简单的“现状描述”。它揭示了美国公立教育体系中一个长期被忽视的结构性断层：课后项目究竟应该扮演“看护者”的角色，还是“教学延伸”的角色？不同学校、不同学生的答案截然不同，而这种差异本身，正在加剧教育公平的老问题。\n\n> **KC评论：** 这份报告的核心洞察不在于“一半校长说没对齐”，而在于“谁在说对齐，谁在说没对齐”。当高贫困学校和城市学校的校长更倾向于认为课后班与课堂对齐时，这并非他们做得更好，而可能恰恰反映了课后项目的功能分化——弱势群体的孩子被投入更多“补课式”课后班，而优势群体的孩子则拥有更多“去学术化”的探索时间。这是教育公平的一个新维度。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 学术对齐的“及格线”之下，是功能定位的根本分歧\n\n报告的核心发现是，在拥有课后项目的校长中，仅有52%同意或强烈同意其课后项目与学校日教学在学术上对齐。这意味着，如果再算上那24%根本未提供课后项目的学校，全美实际上只有不到四成的学校同时具备课后项目且校长认为其具备学术对齐性。\n\n这一数据本身并不令人意外，但报告通过开放式问题的分析，揭示了“不及格”背后的深层原因。约五分之一的校长坦承，他们的学校根本没有任何对齐的努力。其中，绝大多数是小学的校长，他们明确表示，课后项目的定位就是“看护”、“玩耍”或提供“非学术性的”兴趣活\n\n[... middle omitted ...]\n\n欢迎加入我们的社群，与数百位产业决策者和投资者一同深度阅读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n课后托管，不只是“看孩子”\n\n课后托管 ≠ 纯看孩子\n\n很多学校课后托管跟课堂学习是“两张皮”，但最新的全国调研发现，有策略地做“学术对齐”，效果可能更好。\n\n1️⃣ 过半校长说“有对齐”\n全国抽样调查显示，52%的校长认为课后项目与课堂学习有衔接。但实际算下来，全美只有不到一半的学校同时提供课后托管+有学术对齐。\n\n2️⃣ 谁更在意“对齐”？\n- 中学>小学（67% vs 46%）\n- 高贫困学校>低贫困学校\n- 城市>郊区\n\n推测原因：小学课后更多是看护/玩乐，而高年级和弱势群体更倾向用课后补短板。\n\n3️⃣ 自己人带 vs 外部机构\n校内老师带的课后项目，学术对齐比例更高（59%），外部机构只有45%。因为校内老师更熟悉教学内容和节奏。\n\n4️⃣ 怎么做对齐？\n- 校内辅导+作业帮助\n- 目标明确的技能训练\n- 趣味但融入学科的拓展活动\n\n关键是：不是把课堂搬过来，而是用课后灵活的时间做“有设计感的学习”。\n\n5️⃣ 最大挑战\n约1/5校长说“完全没对齐”，其中3/4是小学。很多课后项目跟学校是“两张皮”，校长也无权干涉。\n\n一个有意思的发现：专门配一个“课后-课堂联络员”的学校，对齐效果明显更好。\n\n[... middle omitted ...]\n\ne\n\n## KEY FINDINGS\n\nJust over half of surveyed principals with after-school programs (ASPs) agreed that their after-school programming was academically aligned to instruction provided during t\n\n[... middle omitted ...]\n\n reflect the opinions of its research clients and sponsors. RAND® is a registered trademark.\n\nFor more information on this publication, visit www.rand.org/t/RRA4386-2.\n\n© 2026 The Fund for Public Schools\n\n## www.rand.org"
  },
  {
    "id": "R055",
    "title": "波士顿咨询：CPG与零售的AI竞赛，赢家已经拉开差距",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CPG与零售的AI竞赛，赢家已经拉开差距\n\nAI在消费行业的渗透已经不是新闻。真正值得关注的问题是：为什么有些公司已经将AI转化为实实在在的利润率提升，而绝大多数还在“试点泥潭”里打转？\n\n波士顿咨询与消费品论坛联合发布的最新报告，基于对39位CPG和零售高管的调研，给出了一个方向性的判断：**行业正在加速分化，赢家与追赶者的差距不是由技术投入规模决定的，而是由“AI能否嵌入核心商业决策流程”决定的。**\n\n这份报告最值得关注的信号不是AI的应用场景清单，而是两个关键数字：**CPG公司如果规模化部署全部相关AI应用，可以带来220至350个基点的EBIT提升；零售商对应的数字是180至360个基点。** 在消费行业利润率普遍承压的当下，这个量级意味着AI不再是锦上添花的效率工具，而是决定未来5年竞争格局的结构性变量。\n\n问题是，大多数公司离这个价值池还很远。\n\n> **KC评论：** 报告给出的EBIT提升区间是“假设所有相关AI应用都规模化部署”的理论值。现实是，75%的CPG公司仍停留在试点阶段。这意味着，率先突破规模化瓶颈的公司将获得不对称的竞争优势，而追赶者会陷入“越试点越焦虑”的困境。完整报告中有这些价值池的详细拆解，包括每个AI应用的具体EBIT贡献测算，值得仔细研究。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 零售业已出现“两速世界”，CPG还在试点泥潭中挣扎\n\n报告最直观的发现是行业成熟度的严重分化。\n\n在零售样本中，45%的公司已经进入规模化部署阶段，但同样有40%的公司几乎还没开始。这种“两头大、中间小”的分布说明零售业已经形成了清晰的分水岭。领先者没有在所有领域平均用力，而是集中资源在需求预测、补货、定价和运输优化这几个价值最容易验证的环节。\n\nCPG的情况更令人担忧。**76\n\n[... middle omitted ...]\n\n身更大。而这，正是我们在社群中持续探讨的方向。\n\n---\n\n`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPG和零售AI：赢家这样拉开差距\n\nAI落地，谁在真赚钱？\n\n赢家靠聚焦核心商业，不是堆项目\n\n某外资投行联合机构调研了39家CPG和零售高管，发现一个残酷现实：\n\n1️⃣ 大部分公司还在试点阶段\n- 约75%的CPG企业仍处于“试水”模式\n- 零售业两极分化：45%已在规模化，40%还没开始\n- 差距不在技术，在“敢不敢聚焦核心业务”\n\n2️⃣ 价值池真实存在\n- CPG企业全面落地AI，EBIT可提升2.2-3.5个百分点\n- 零售商可提升1.8-3.6个百分点\n- 未来随着AI从“辅助决策”升级到“自动执行”，价值可能再扩大1.7倍\n\n3️⃣ 赢家做对了三件事\n- 不撒网，把AI钉在“创新加速、需求感知、品种优化、货架执行”这几个核心\n- 敢设高目标：不是用现有能力倒推，而是设定18个月后要达成的效果\n- 从第一天就衡量ROI，避免“试点成功、规模翻车”的陷阱\n\n4️⃣ 最有意思的发现\n- 46%的零售商认为“品种优化”最重要，但只有34%真正在规模落地\n- 近半数CPG把“从创意到上市”列为战略核心，但只有11%在创新环节部署了AI\n- 超过一半的公司根本不正式衡量AI投入的回报\n\n5️⃣ 下一步机\n\n[... middle omitted ...]\n\ned in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder wit\n\n[... middle omitted ...]\n\nsit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.\n\n© Boston Consulting Group 2026. All rights reserved.\n\n![](images/393cf78540024fd65398c9dc43a8044708373b99b3ce606ce1793ce362eb210b.jpg)"
  },
  {
    "id": "R056",
    "title": "波士顿咨询：农业AI不是新工具，而是新氮气时刻",
    "digest": "[wechat_article.md]\n# 波士顿咨询：农业AI不是新工具，而是新氮气时刻\n\n当1898年英国科学家克鲁克斯爵士警告世界氮肥即将枯竭时，他预言的是农业的一场硬约束危机。11年后哈伯找到了从空气中固氮的方法，博世将其工业化。那一次技术突破之所以重塑了全球食物体系，不是因为解决了一个具体问题，而是因为它解除了农业增长的上限，引发了一整条创新链的连锁反应：种子遗传学、机械化、农艺学，每一层都在前一层的基础上叠加，最终改变了人类如何种地、如何交易、如何吃饭。\n\n波士顿咨询在2026年6月发布的最新研报中提出了一个判断：今天我们正在面对农业的第二个“氮气时刻”。但这一次的上限不是化学元素，而是信息与决策的密度。农业智能——即AI在从育种到零售的全链条上的自主决策能力——正在以同样的方式解除农业增长的另一重硬约束。\n\n**这份报告最值得看的判断是：农业AI压缩的不是成本，而是信息不对称和专家溢价。过去一百多年支撑农业价值链上各环节利润来源的核心资产——谁更懂、谁先知道、谁能判断——正在被重新定价。这不是效率改进，是竞争基础的重写。**\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 农业面临的三重威胁中，AI是唯一同时回应三者的变量\n\n波士顿咨询将当前全球农业食物体系面临的威胁归纳为三类：气候波动性、地缘政治重组、以及监管范式转移。这三者不是独立的风险清单，它们共同指向同一个问题：农业的生产函数正在变得不可预测。\n\n气候让降水、温度和季节规律变得不可靠。地缘政治让供应链冲击从偶发事件变成永久特征——中美关税、乌克兰战争、霍尔木兹海峡的化肥供应中断，这些不再是黑天鹅，而是新常态。监管则要求整个行业建立一个从未有过的数据基础设施：欧盟的森林砍伐规则、Scope 3碳报告、碳市场协议，都在要求企业精确、可验证地回答“每一粒粮食从哪里来、在什么条件下种出来的、用了什\n\n[... middle omitted ...]\n\n行深度拆解，包括所有原始图表和未在本文中展开的竞争分析细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 正在重塑全球粮食系统\n\n**AI 农业革命**\n\n**信息差正在消失，这是农业的新氮肥时刻**\n\n1/ **农业正面临三重威胁**\n气候波动让降雨、温度变得难以预测；地缘政治重组使供应链冲击成为常态，比如乌克兰战争重塑了小麦地图，霍尔木兹海峡的关闭影响了化肥供应；监管范式转变，欧盟的森林砍伐规则和碳报告要求农业拥有从未有过的大规模数据基础设施。\n\n2/ **AI 农业智能是第四个力量**\n它不仅仅是精准农业，而是用代理型 AI 自主决策、行动，从研究、种植到分销零售全面介入。BCG 认为，这正在侵蚀过去几十年支撑农业利润的信息不对称和专业知识溢价。\n\n3/ **四个维度同时发挥作用**\n- **感知**：把物理世界变成数据，比如 InnerPlant 让大豆自己发出光学信号报告压力\n- **决策**：把数据变成正确建议，FarmerChat 已服务 83 万非洲和印度农民，把每次咨询成本从 35 美元降到 35 美分\n- **行动**：自动执行，约翰迪尔的 See & Spray 用计算机视觉区分作物和杂草，减少一半化学用量，2025 年覆盖 500 万英亩\n- **创造**：用生成式 AI 设计新性状\n\n[... middle omitted ...]\n\neiling; after that, its decline would be simple arithmetic. His appeal was direct: unless chemistry could produce nitrogen from the atmosphere itself, mass starvation would follow.\n\nEleven yea\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R057",
    "title": "波士顿咨询：AI正在重置全球制造业的选址逻辑，高成本国家并非必然输家",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI正在重置全球制造业的选址逻辑，高成本国家并非必然输家\n\n当全球制造业CEO们还在争论“要不要把工厂搬出中国”时，一份来自波士顿咨询（BCG）的最新研报提出了一个更具颠覆性的判断：真正决定制造业竞争力的变量，已经从“哪里劳动力最便宜”变成了“哪里能最快部署未来工厂”。\n\n这不是一个渐进式的优化建议。BCG的量化模型显示，在食品加工领域，一家德国工厂通过部署未来工厂（FoF）能力，可以比搬到中国获得高达14个百分点的成本优势。而在电子行业，即便完成同样的智能化改造，留在德国依然比搬到中国贵15个百分点。\n\n差异如此悬殊，意味着过去二十年支撑全球供应链布局的底层逻辑——劳动力成本套利——正在被改写。未来工厂不是锦上添花的效率工具，而是重新划分全球制造业版图的力量。\n\nBCG这份报告基于对1000家制造商的全球调研、42个成本与定性因素的复合指数，以及横跨54个国家、47个行业的竞争力评分模型。它给出的不是笼统的“回岸制造”或“AI赋能”口号，而是一套可量化的决策框架：哪些行业、哪些地区、在什么条件下，升级工厂能打败搬迁。\n\n以下是这份报告最值得关注的五个核心洞察。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 未来工厂对高成本地区的成本压缩幅度，远超多数CEO的预期\n\nBCG的三个典型案例揭示了未来工厂的真实威力。一家德国咖啡烘焙包装公司，通过自动化、智能过程控制、预测性维护和集中数据协调，劳动力成本下降近60%，总转换成本下降超过40个百分点。一家美国制药公司，在片剂和胶囊制造中整合数字过程控制、物联网监控、高级分析和数字质量管控，劳动力成本降低超过60%，总转换成本下降30个百分点。一家韩国电池制造公司，通过连续混合、优化涂布和AI质量控制，劳动力成本降低约30%，转换成本下降超过25个百分点。\n\n这些\n\n[... middle omitted ...]\n\n份报告的完整解读与原始图表，以及每日更新的投行研报精华。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在改写工厂选址逻辑\n\n工厂选址，逻辑变了\n\n高成本地区反而可能更优\n\n如果还用“哪里人工便宜就去哪里”的老思路看制造业选址，可能会错过这波结构性变化。某外资投行最新研报发现，AI驱动的“未来工厂”正在重塑全球制造竞争力，高成本地区通过技术升级，反而可能比搬到低成本地区更划算。\n\n1/ 成本压缩空间惊人\n研报给出几个真实案例：\n- 德国咖啡烘焙厂：自动化+智能控制，劳动力成本降近60%，总生产成本降超40%\n- 美国药企：数字孪生+物联网监控，劳动力成本降60%+，总生产成本降30%\n- 韩国电池厂：AI质检+流程再造，劳动力成本降30%，总生产成本降25%\n\n2/ 选址逻辑彻底变了\n过去比的是人工+物流，现在比的是“能否把工厂改造成高生产力系统”。关键变量不再是劳动力成本，而是：\n- 自动化能压缩多少成本\n- 靠近市场的物流优势\n- 当地数字化基础设施和人才储备\n\n3/ 不同行业结论不同\n- 食品加工：德国升级未来工厂后，比搬到中国成本低14%\n- 汽车零部件：升级后可达成本持平\n- 电子组装：搬到中国仍然更优，即使升级也有15%的成本差距\n\n4/ 哪些地方更具竞争力？\n美国在数字化基础设施和人才上领先\n\n[... middle omitted ...]\n\non costs and unlocking productivity savings of up to 60%. And the stakes extend beyond the factory floor: roughly \\$1.03 trillion of manufacturing value is at risk of relocation out of Western\n\n[... middle omitted ...]\n\nto receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.\n\n![](images/c15d76c3c79ea815b6de791771c2af1ee6009da44e8c911ee9f367e6d60810a0.jpg)"
  },
  {
    "id": "R058",
    "title": "波士顿咨询：商业地产正在错过每年2000亿美元的“暗价值”",
    "digest": "[wechat_article.md]\n# 波士顿咨询：商业地产正在错过每年2000亿美元的“暗价值”\n\n商业地产行业正站在一个十字路口。一边是延续数十年的“买入并持有”传统模式，另一边是每年高达2000亿美元的潜在收益增量——相当于行业年回报率提升三分之一。波士顿咨询(BCG)在最新发布的研报中提出了一个尖锐的判断：大部分商业地产投资者正在系统性地错过短中期优化带来的价值，而问题不在于信息不足，而在于思维方式与运营模式的代际落后。\n\n这份报告的核心洞察，用一个物理学比喻来概括——“暗价值”。就像暗物质无法被直接观测但其引力效应真实存在一样，商业地产中因僵化的持有策略而损失的价值也无法被传统报表捕捉，但它正在每年吞噬2000亿美元。BCG的结论是：学会像大宗商品交易商那样思考，是解锁这笔价值的关键。\n\n为什么是现在？因为AI正在以前所未有的速度降低数据分析和市场扫描的成本。那些曾经只有顶级对冲基金才能负担的实时定价模型、套利识别工具和供需预测系统，如今已经变得触手可及。但行业的态度却远远落后于技术的变化。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 行业最大的敌人不是市场波动，而是根深蒂固的“持有惰性”\n\n商业地产的长期持有模式并非没有道理。对于养老基金、保险公司等机构投资者而言，稳定的现金流、通胀对冲和分散化配置是核心诉求。BCG的数据显示，即便是在流动性最好的美国市场，自2000年以来，54%的投资者平均持有资产超过五年。在欧洲和亚洲，这一比例更高。全球约60%的商业地产资本配置在“核心”或“核心+”策略上，目标就是可预测的长期收益。\n\n但这种合理性正在变成一种“持有惰性”。问题不在于长期持有本身，而在于持有期间几乎完全放弃了主动管理的机会。报告指出，大多数投资者仍然以年度为单位进行资产估值，决策流程缓慢且层级化，面对市场信号的反应周期以季度甚至年度计算\n\n[... middle omitted ...]\n\n全展开的“文化变革代价”“AI竞争加剧”等问题进行持续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n商业地产投资者，正在错过每年2000亿的“暗价值”\n\n投研笔记｜商业地产“暗价值”\n\n最近读到一篇很有意思的研报，讲商业地产领域存在一种“暗价值”——就像物理里的暗物质，看不见摸不着，但它的影响真实存在。\n\n💰 每年全球商业地产投资者错过的价值，约2000亿美元。\n\n📍 核心逻辑其实很清晰：\n\n1️⃣ 传统“买入持有”模式正在被挑战\n过去大家都把商业地产当长期配置，追求稳定收租。美国54%的投资者持有资产超过5年，其他地区比例更高。这本身没有错，但问题是——持有期内那些中短期优化机会，几乎被完全忽略了。\n\n2️⃣ “暗价值”从哪来？\n研报梳理了6个驱动因素：区位差异、资产质量差异、时间差、行业可重构性弱、缓冲空间、资本流动。每一个都在制造套利机会，但传统玩家因为信息不对称和高交易成本，根本抓不住。\n\n3️⃣ AI正在改变游戏规则\nAI大幅降低了数据分析工具的成本。以前只有对冲基金玩得转的实时估值、供需模型、市场情绪监测，现在商业地产玩家也可以用了。关键是——谁能把数据变成决策优势。\n\n4️⃣ 改变需要三步走\n用对工具（实时估值+市场感知）、改变文化（从规避风险到管理风险）、改革治理（决策权下放到一线）。研报还\n\n[... middle omitted ...]\n\n on an estimated \\$200 billion of value worldwide each year. We call this “dark value” because, like dark matter in physics, its effects can be seen in lost opportunities, but it can’t be meas\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R059",
    "title": "波士顿咨询：保险业正在经历一次投资者偏好的结构性转向",
    "digest": "[wechat_article.md]\n# 波士顿咨询：保险业正在经历一次投资者偏好的结构性转向\n\n全球保险业在过去五年里交出了一份让股东满意的答卷。15%的年化总股东回报率，自2017年以来首次超过了行业自身的股权成本。这组数据本身并不令人意外，毕竟疫情后的复苏、利率环境的改善都在推高收益。但波士顿咨询在刚刚发布的《2026保险价值创造者报告》中揭示了一个更值得关注的变化：投资者正在系统性地从财产与意外险和再保险转向人寿与健康和综合险，同时将资金从美国市场向欧洲和亚太迁移。\n\n这不是一次短期的板块轮动。它背后是保险行业底层逻辑的松动——定价周期的拐点、技术渗透的加速、以及全球资本对“确定性”的重新定价。对于保险公司的管理层、投资者以及关注金融行业趋势的决策者而言，理解这个转向的驱动力和持续时间，比跟踪季度保费数字重要得多。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 行业整体回报改善背后，是“质”而非“量”的驱动\n\n过去五年，全球保险业的年化TSR达到15%，高于整体市场平均水平。但波士顿咨询的这份早期报告明确指出，这个数字并非来自保费规模的扩张，而是来自两个结构性因素的叠加：疫情冲击逐步消退带来的赔付正常化，以及净投资收益率的显著提升。\n\n这意味着行业增长的可持续性取决于利率环境和承保纪律。如果利率进入下行通道，而定价竞争重新加剧，15%的TSR可能难以维持。报告已经给出了一个早期信号：商业财产险的费率正在松动，这将在未来几年内压缩财产险公司的股本回报率。\n\n> **KC评论：** 对于关注保险板块的投资者来说，核心问题不是“保险股还能不能涨”，而是“哪些细分赛道在利率下行周期中依然能维持回报率”。波士顿咨询的后续报告将提供区域和细分市场的详细拆解，这是完整报告的核心价值所在。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n##\n\n[... middle omitted ...]\n\n以及再保险趋势报告。这些内容将提供更细颗粒度的数据、案例和竞争格局拆解。\n\n我们每天会由AI agent加上人工review，筛选和解读全球顶级投行和咨询机构的最新报告，生成中文摘要与KC评论，包含当天最新数据图表合集。这些材料既方便喂给AI做进一步分析，也方便人工快速把握市场动态。如果你希望获取完整报告原文、原始图表，或者想就保险行业的结构性转向做更深入的讨论，欢迎加入社群，我们每天都会更新国际投行和咨询机构的中文解读与原始数据图表。\n\n[note.md]\n全球保险业，风向悄悄变了\n\n风向真的变了\n\nBCG最新全球保险价值创造报告，用数据说了一个关键趋势：保险业正在走出过去五年的低回报期，股东回报首次跑赢资金成本。\n\n1/ 回报格局在翻转\n- 财险和再保险过去五年表现最强，但2025年增速已放缓\n- 寿险和健康险反而在2025年跑赢，靠的是投资收益红利\n- 关键信号：投资者开始从财险转向寿险、健康险和综合险\n\n2/ 区域重心在迁移\n- 欧洲五年TSR达20.3%，亚太一年TSR高达35.3%\n- 背后逻辑：美国市场波动加大，资金在“寻找质量”\n- 欧洲和亚太成了新的回报锚点\n\n3/ 三个趋势值得盯\n- AI正在重塑承保、理赔、人才等核心环节\n- 财险面临费率走软+竞争加剧，并购将成主要出路\n- 老龄化+客户偏好变化，推动寿险向“保障+灵活利益”产品转型\n\n研报说这是“早期信号”，但数据已经清晰：全球保险的资金流向和增长逻辑，正在重新洗牌。\n\n如果你也在关注保险赛道的结构性变化，欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n![](images/86ab63d857975a9af2b53ab989043cccc3a842bd5e1eca74\n\n[... middle omitted ...]\n\n on available—but not yet complete for the full year—data. Subsequent installments will provide a more detailed segment- and region-specific analysis as well as offer deep dives into the prope\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R060",
    "title": "麦肯锡：88%企业试了AI，81%没赚到钱",
    "digest": "[wechat_article.md]\n# 麦肯锡：88%企业试了AI，81%没赚到钱\n\n2026年2月，麦肯锡发布了第二版《组织状态报告》（The State of Organizations 2026），基于对全球15个国家、16个行业、超过10,000名高管的调研。这份报告的核心判断，值得每一个产业决策者认真对待：**企业正面临技术、经济和劳动力三大结构性力量的叠加冲击，但绝大多数组织尚未准备好应对。**\n\n报告最引人注目的数据是：88%的组织正在实验AI，但81%没有报告任何有意义的利润改善。这组数字背后，不是AI本身的问题，而是组织转型的滞后。麦肯锡的结论很直白——企业需要的不是“插电即用”的AI工具，而是一场“双重转型”：技术转型与组织转型同步推进。\n\n这不仅仅是AI的问题。地缘政治碎片化、贸易格局重组、劳动力期望变化，都在迫使企业重新思考“如何组织工作”这个根本问题。报告提出了九大组织变革方向，但核心主线只有一个：**在不确定的世界里，持续绩效和价值创造，比短期收益更重要。**\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. AI落地的真正瓶颈不是技术，是组织\n\n报告揭示了一个反直觉的事实：企业对AI的投入热情很高，但转化率极低。86%的领导者认为自己的组织在将AI融入日常运营方面准备不足。更关键的是，六分之一的组织没有明确的C级负责人来推动AI落地。\n\n这意味着什么？AI战略在多数企业里仍处于“散点实验”阶段——某个团队用AI做客服，另一个团队用AI写报告，但没有人从全局视角重新设计端到端的业务流程。\n\n> **KC评论：** 麦肯锡的报告里有一个值得反复咀嚼的细节——一位高管提到，在AI上每花1美元技术投入，就需要花5美元在“人”上。这5美元不是培训费，而是组织重构的成本。完整报告里有一张关于“AI代理如何与人类协作”的图表，展示了不\n\n[... middle omitted ...]\n\n、以及与其他机构观点的对比分析感兴趣，欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n组织转型2026：AI重塑正当时\n\nAI重塑组织力\n\n三股力量正在改写企业生存法则\n\n📌 技术、经济、劳动力三大板块同时震动，组织转型不再是可选项。\n\n某外资投行最新调研覆盖15国、1万+高管，发现这3个核心信号：\n\n1️⃣ AI落地≠价值兑现\n88%企业在试水AI，但81%没看到实质利润增长。\n86%高管坦言组织尚未准备好日常运营AI化。\n关键卡点：AI自身风险（46%）、合规伦理（44%）、组织变革管理（39%）。\n\n2️⃣ 经济不确定性倒逼“韧性”升级\n近3/4受访者表示地缘政治已显著影响业务。\n43%企业承认资产剥离时机过晚。\n破局方向：用数字化工具预判风险、动态调配资源。\n\n3️⃣ 人才策略必须重新定义\n仅20%领导者认可非金钱激励能驱动绩效。\n72%组织自认没准备好应对即将到来的变革。\n值得关注：55%高管认为赋能员工AI能力将带来指数级效率提升。\n\n🔍 三个关键趋势：\n— 从短期韧性转向持续生产力\n— 共享服务中心向AI优先的虚拟平台进化\n— 领导者需要“由内而外”的自我成长\n\n最意外发现：仅30%组织能做到跨企业资源重新配置。这意味着大多数企业还在用旧地图找新大陆。\n\n#学习笔记\n\n[sour\n\n[... middle omitted ...]\n\n performance edge\n53 Sharpening the focus on diversity and inclusion\n57 Reinventing leadership: Leading from the inside out\n64 Business as change: Managing continuous transformation in the org\n\n[... middle omitted ...]\n\nro, Sasha Goluskin, Scott Brugmans, Tarek Bakali, Tristan Allen, Yueyang Chen, and Zoe Fox.\n\nState of Organizations 2026\nBy McKinsey\nFebruary 2026\nCopyright © McKinsey & Company\n\nwww.McKinsey.com\n\nX @McKinsey\nf @McKinsey"
  },
  {
    "id": "R061",
    "title": "麦肯锡：AI已铺开，但企业级价值仍卡在“最后一公里”",
    "digest": "[wechat_article.md]\n# 麦肯锡：AI已铺开，但企业级价值仍卡在“最后一公里”\n\n三年前，生成式AI引爆了新一轮人工智能浪潮。三年后的今天，麦肯锡2025年全球AI调研给出了一个看似矛盾但意味深长的画面：88%的受访者表示其所在组织已在至少一个业务职能中常规使用AI，这一比例较去年的78%显著上升。然而，近三分之二的受访者坦言，他们的组织尚未开始将AI规模化推广至企业全境。\n\n这意味着什么？AI工具已从实验室进入办公室，但从“用起来”到“产生企业级价值”，中间横亘着一道尚未被多数企业跨越的鸿沟。这道鸿沟不是技术问题，而是组织能力、战略定力和工作流重构的问题。\n\n麦肯锡这份基于近2000名全球受访者的调研报告，揭示了一个正在形成但尚未定型的新竞争格局：谁先跨越这道鸿沟，谁就可能在下一轮产业洗牌中占据结构性优势。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. AI使用广度在扩大，但深度仍然有限——多数企业停留在“多点开花”而非“系统性嵌入”\n\n88%的AI使用率听起来很高，但这更像是一个“广度指标”。麦肯锡的调研进一步追问了AI在组织内的渗透深度，结果并不乐观：只有约三分之一的企业进入了规模化阶段，其余企业仍处于实验或试点状态。\n\n一个更值得关注的信号是：AI正在向更多业务职能扩散。超过三分之二的受访者表示其组织在超过一个职能中使用AI，一半的受访者报告在三个或更多职能中使用AI。从职能分布看，IT、营销与销售、知识管理是AI使用最密集的前三大领域。\n\n但“用得多”不等于“用得深”。麦肯锡指出，多数企业尚未将AI深度嵌入工作流和业务流程中，因此难以实现企业层面的实质性收益。这就像一家工厂采购了大量先进设备，但只把它们摆放在车间角落，而未重新设计生产线。\n\n> **KC评论：** 对投资者和产业决策者而言，真正需要关注的不是“有多少企业在用AI”，\n\n[... middle omitted ...]\n\n领取完整研报解读与原始图表，继续探讨那些尚未完全回答的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n88%的企业在用AI，但大部分还在“试水”\n\n企业AI落地，仍在早期\n\n某外资投行2025全球AI调研出炉，核心结论很清晰：\n\nAI普及率创新高（88%的企业至少在一个业务线使用AI），但真正大规模部署的只有1/3。大多数公司还卡在“试点-规模”的鸿沟里。\n\n1️⃣ AI Agent是最大亮点，但还没铺开\n- 62%的企业在试水AI Agent（能自主规划、执行任务的智能体）\n- 但只有23%在规模化部署，且通常只集中在1-2个部门\n- IT和知识管理是Agent落地最快的领域\n\n2️⃣ 高绩效公司的秘密\n- 不仅追求效率，更把增长和创新作为AI目标\n- 重新设计工作流，而非简单替换\n- 80%的企业把“提效”作为目标，但真正出成绩的公司，往往同时追求“增长”和“创新”\n\n3️⃣ 规模越大，落地越深\n- 收入超50亿美元的公司，近一半已进入规模化阶段\n- 小公司（收入<1亿美元）只有29%做到\n\n4️⃣ 风险意识在提升\n- 51%的企业遇到过AI负面后果（最突出是“不准确”）\n- 高绩效公司反而更常遇到问题——因为它们用得深、用得多，也更积极管理风险\n\n5️⃣ 就业影响：看法分化\n- 32%认为AI会减少岗位\n\n[... middle omitted ...]\n\nenting views from QuantumBlack, AI by McKinsey.\n\n![](images/141f59898df2bfea1468933f22a89a5a75ecc870ea8ae9bb62bd41674f917f4a.jpg)\n\n## Key findings\n\n1. Most organizations are still in the exper\n\n[... middle omitted ...]\n\n![](images/d9bf5174d8802996597740b869f79604f19761ff29c6ddf9b3288f34159e888d.jpg)\n\nFind more content like this on the McKinsey Insights App\n\n![](images/04cc9211788e331e3cee66333e67c499b4f7f6ee9b6af2b9927b40b2e6a1eff2.jpg)"
  },
  {
    "id": "R062",
    "title": "木头姐ARK：#515: Are Prediction Markets Going Mainstream Again?, & More",
    "digest": "[note.md]\n# 木头姐ARK：#515: Are Prediction Markets Going Mainstream Again?, & More\n\nIs the boom in prediction markets structural or the result of momentary catalysts? Hosted across the US, Canada, and Mexico, the 2026 FIFA World Cup is the latest test. The notional volume of prediction markets hit an all-time high of $13 billion, or ~$675 billion at an annual rate, during the first full week of group play ended June 15. Year-to-date, the broader market is on pace for notional volume of ~$330 billion at an annual rate, more than quadrupling the $71 billion in 2025. In the early days of prediction markets, the 2024 US national election caused the initial spike. Now, the World Cup is the prime mover. Importantly, volume is ratcheting higher in the aftermath of each event.\n\n来源：https://www.ark-invest.com/newsletters/issue-515\n\n[source_mineru.md]\n# 木头姐ARK：#515: Are Prediction Markets Going Mainstream Again?, & More\n\nSource: ARK Invest RSS feed\nType: Newsletters\nPublished: Mon, 29 Jun 2026 19:30:00 GMT\nUpdated: 2026-06-29T23:34:19.300+00:00\nURL: https://www.ark-invest.com/newsletters/issue-515\n\n## Feed摘要\n\nIs the boom in prediction markets structural or the result of momentary catalysts? Hosted across the US, Canada, and Mexico, the 2026 FIFA World Cup is the latest test. The notional volume of prediction markets hit an all-time high of $13 billion, or ~$675 billion at an annual rate, during the first full week of group play ended June 15. Year-to-date, the broader market is on pace for notional volume of ~$330 billion at an annual rate, more than quadrupling the $71 billion in 2025. In the early days of prediction markets, t\n\n[... middle omitted ...]\n\non in 2025. In the early days of prediction markets, the 2024 US national election caused the initial spike. Now, the World Cup is the prime mover. Importantly, volume is ratcheting higher in the aftermath of each event."
  },
  {
    "id": "R063",
    "title": "木头姐ARK：#514: SpaceXAI Launches, & More",
    "digest": "[note.md]\n# 木头姐ARK：#514: SpaceXAI Launches, & More\n\nIn its heavily anticipated initial public offering (IPO), SpaceX issued $75 billion worth of new shares the largest IPO of all time. Appreciating to more than $2 trillion in equity market cap, a lofty valuation relative to backward-looking financials, investors have focused on its out-of-this-world prospective return on capital.\n\n来源：https://www.ark-invest.com/newsletters/issue-514\n\n[source_mineru.md]\n# 木头姐ARK：#514: SpaceXAI Launches, & More\n\nSource: ARK Invest RSS feed\nType: Newsletters\nPublished: Mon, 15 Jun 2026 21:12:00 GMT\nUpdated: 2026-06-29T23:34:21.380+00:00\nURL: https://www.ark-invest.com/newsletters/issue-514\n\n## Feed摘要\n\nIn its heavily anticipated initial public offering (IPO), SpaceX issued $75 billion worth of new shares the largest IPO of all time. Appreciating to more than $2 trillion in equity market cap, a lofty valuation relative to backward-looking financials, investors have focused on its out-of-this-world prospective return on capital.\n\n## 原始材料\n\nIn its heavily anticipated initial public offering (IPO), SpaceX issued $75 billion worth of new shares the largest IPO of all time. Appreciating to more than $2 trillion in equity market cap, a lofty valuation relative to backward-looking financials, investors have focused on its out-of-this-world prospective return on capital."
  },
  {
    "id": "R064",
    "title": "木头姐ARK：#513: Kalshi Launches Perpetuals As Robinhood’s Rothera Exchange Goes Live, & More",
    "digest": "[note.md]\n# 木头姐ARK：#513: Kalshi Launches Perpetuals As Robinhood’s Rothera Exchange Goes Live, & More\n\nKalshi's launch of perpetual futures marks a watershed moment for the structure of the US crypto market. For the first time, US investors can access a Commodity Futures Trading Commission (CFTC)-regulated perpetual contract, a product that has dominated international crypto trading for years.\n\n来源：https://www.ark-invest.com/newsletters/issue-513\n\n[source_mineru.md]\n# 木头姐ARK：#513: Kalshi Launches Perpetuals As Robinhood’s Rothera Exchange Goes Live, & More\n\nSource: ARK Invest RSS feed\nType: Newsletters\nPublished: Mon, 08 Jun 2026 21:23:00 GMT\nUpdated: 2026-06-29T23:34:18.993+00:00\nURL: https://www.ark-invest.com/newsletters/issue-513\n\n## Feed摘要\n\nKalshi's launch of perpetual futures marks a watershed moment for the structure of the US crypto market. For the first time, US investors can access a Commodity Futures Trading Commission (CFTC)-regulated perpetual contract, a product that has dominated international crypto trading for years.\n\n## 原始材料\n\nKalshi's launch of perpetual futures marks a watershed moment for the structure of the US crypto market. For the first time, US investors can access a Commodity Futures Trading Commission (CFTC)-regulated perpetual contract, a product that has dominated international crypto trading for years."
  },
  {
    "id": "R065",
    "title": "木头姐ARK：#512: Blue Origin Explosion Highlights Launch Capacity Constraints In Race To The Moon, & Mor",
    "digest": "[note.md]\n# 木头姐ARK：#512: Blue Origin Explosion Highlights Launch Capacity Constraints In Race To The Moon, & More\n\nLast week, ahead of its fourth mission, Blue Origin’s New Glenn rocket exploded during a test fire at its launch site in Florida. The explosion severely damaged Launch Complex 36, Blue Origin’s only operational orbital launch pad for New Glenn. While the company is building additional launch infrastructure and investigating the root cause, the damage is likely to delay the vehicle’s next flight by at least one year.\n\n来源：https://www.ark-invest.com/newsletters/issue-512\n\n[source_mineru.md]\n# 木头姐ARK：#512: Blue Origin Explosion Highlights Launch Capacity Constraints In Race To The Moon, & More\n\nSource: ARK Invest RSS feed\nType: Newsletters\nPublished: Mon, 01 Jun 2026 21:55:00 GMT\nUpdated: 2026-06-29T23:34:19.260+00:00\nURL: https://www.ark-invest.com/newsletters/issue-512\n\n## Feed摘要\n\nLast week, ahead of its fourth mission, Blue Origin’s New Glenn rocket exploded during a test fire at its launch site in Florida. The explosion severely damaged Launch Complex 36, Blue Origin’s only operational orbital launch pad for New Glenn. While the company is building additional launch infrastructure and investigating the root cause, the damage is likely to delay the vehicle’s next flight by at least one year.\n\n## 原始材料\n\nLast week, ahead of its fourth mission, Blue Origin’s New Glenn r\n\n[... middle omitted ...]\n\noperational orbital launch pad for New Glenn. While the company is building additional launch infrastructure and investigating the root cause, the damage is likely to delay the vehicle’s next flight by at least one year."
  },
  {
    "id": "R066",
    "title": "木头姐ARK：#511: Anthropic Is Paying $1.25 Billion Per Month To Access SpaceX’s Compute Capacity, & More",
    "digest": "[note.md]\n# 木头姐ARK：#511: Anthropic Is Paying $1.25 Billion Per Month To Access SpaceX’s Compute Capacity, & More\n\nAnthropic paying SpaceX, longevity research including GLP-1s, AI's first autonomous mathematical breakthrough, and Anthropic's announcement about investing in special purpose vehicles.\n\n来源：https://www.ark-invest.com/newsletters/issue-511\n\n[source_mineru.md]\n# 木头姐ARK：#511: Anthropic Is Paying $1.25 Billion Per Month To Access SpaceX’s Compute Capacity, & More\n\nSource: ARK Invest RSS feed\nType: Newsletters\nPublished: Tue, 26 May 2026 15:15:00 GMT\nUpdated: 2026-06-29T23:34:19.114+00:00\nURL: https://www.ark-invest.com/newsletters/issue-511\n\n## Feed摘要\n\nAnthropic paying SpaceX, longevity research including GLP-1s, AI's first autonomous mathematical breakthrough, and Anthropic's announcement about investing in special purpose vehicles.\n\n## 原始材料\n\nAnthropic paying SpaceX, longevity research including GLP-1s, AI's first autonomous mathematical breakthrough, and Anthropic's announcement about investing in special purpose vehicles."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "The 1Q26 GDP figures released in late May (1.1% q-o-q sa) underlined a recovery of domestic demand components, after three consecutive quarters of sluggish performance. The acceleration in household and government consumption as well as investments are consist"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "exhibit 2",
    "context": "Hydropower generation – also concentrated in the SE region – is negatively affected and the power shortage is usually offset by the more intense use of thermal plants, which are also more costly to operate. Brazil has expanded and diversified its power-generat"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 9",
    "context": "\\- Foreign inflows into EM-focused ETFs $^{[3]}$ totaled USD1.8bn between 19 and 25 June, following inflows of USD1.9bn in the previous week. In MTD June, foreign investors net bought USD2.9bn of EM funds (mainly into EM equity funds USD2.3bn), surpassing infl"
  },
  {
    "figure_id": "F004",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Credit spreads are hovering at the tight end of the historical range, while all-in yields are elevated Index-level spreads (left panel) and yields (right panel) for the Bloomberg USD and EUR IG Corporate indices Note:"
  },
  {
    "figure_id": "F005",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Credit spreads are hovering at the tight end of the historical range, while all-in yields are elevated Index-level spreads (left panel) and yields (right panel) for the Bloomberg USD and EUR IG Corporate indices Note:"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 3: In both the IG and HY markets, USD credit has slightly outperformed its EUR peer on an excess return basis Year-to-date excess returns for the Bloomberg IG and HY Corporate indices (USD and EUR markets)"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 4: BBBs have been the best performing rating cohort across IG, year-to-date Year-to-date cumulative excess returns for the rating specific cohorts of the Bloomberg USD (left panel) and EUR (right panel) IG Corporate indices"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Bond-level dispersion is near historically compressed levels in IG, while HY dispersion is more elevated"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Bond-level dispersion is near historically compressed levels in IG, while HY dispersion is more elevated Bond-level ((75th percentile - 25th percentile) / 50th percentile) dispersion for EUR and USD IG (left panel) and E"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Against a backdrop of elevated USD IG issuance, the share of supply from the Technology sector has reached a new high USD IG supply and the share represented by the Technology sector"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 6: Against a backdrop of elevated USD IG issuance, the share of supply from the Technology sector has reached a new high USD IG supply and the share represented by the Technology sector Note: As of June 26, 2026."
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Against a backdrop of elevated USD IG issuance, the share of supply from the Technology sector has reached a new high USD IG supply and the share represented by the Technology sector Note: As of June 26, 2026. Exhibit"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Amended PIK and new non-accrual volume are two leading indicator metrics we monitor closely in private credit Combined ‘stress rate’ for the Cliffwater Direct Lending Index Note: Captures data through 1Q2026 (most rece"
  },
  {
    "figure_id": "F014",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 2: Anthropic dashboard of open-"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 2: Anthropic dashboard of open-"
  },
  {
    "figure_id": "F016",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 3: Geopolitical tensions are increasingly accompanied by state-sponsored cyberattacks a) Geopolitical threats and geopolitical acts indices b) Cyberattacks over time, by threat actor type c) State-sponsored cyberattacks"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 3: Geopolitical tensions are increasingly accompanied by state-sponsored cyberattacks a) Geopolitical threats and geopolitical acts indices b) Cyberattacks over time, by threat actor type c) State-sponsored cyberattacks"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 3: Geopolitical tensions are increasingly accompanied by state-sponsored cyberattacks a) Geopolitical threats and geopolitical acts indices b) Cyberattacks over time, by threat actor type c) State-sponsored cyberattacks"
  },
  {
    "figure_id": "F019",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Oil prices have nearly round-tripped to pre-war levels, but refined product prices remain elevated Exhibit 2: Dollar strengthened to near 2026 highs 2. The energy-driven pickup in inflation has remained manageable in"
  },
  {
    "figure_id": "F020",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Asia CPI inflation has moved up, but less dramatically than in 2021-22"
  },
  {
    "figure_id": "F021",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 3: Asia CPI inflation has moved up, but less dramatically than in 2021-22 Exhibit 4: Inflation is in line with or modestly above targets in most of the region \\* For Hong Kong and Malaysia, we use avg. annualized CPI in"
  },
  {
    "figure_id": "F022",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Asia CPI inflation has moved up, but less dramatically than in 2021-22 Exhibit 4: Inflation is in line with or modestly above targets in most of the region \\* For Hong Kong and Malaysia, we use avg. annualized CPI in"
  },
  {
    "figure_id": "F023",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Surging tech exports from key Asian suppliers Exhibit 6: Exports by far the largest driver of China's recent growth 5. China's exports power on amid weak domestic activity. In May, both retail sales (-0.6% yoy) and f"
  },
  {
    "figure_id": "F024",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 7: CNY stands out among Asian FX in 2026"
  },
  {
    "figure_id": "F025",
    "report_id": "R007",
    "label": "Exhibit 6",
    "context": "Exhibit 8: We still expect tightening by several Asian central banks in coming months"
  },
  {
    "figure_id": "F026",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: PMI for emerging sectors stays solid despite some softening Exhibit 2: EPMI new orders remained solid Exhibit 3: Container throughput growth slowed in May-June"
  },
  {
    "figure_id": "F027",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: PMI for emerging sectors stays solid despite some softening Exhibit 2: EPMI new orders remained solid Exhibit 3: Container throughput growth slowed in May-June Exhibit 4: Auto and home appliance sales growth are su"
  },
  {
    "figure_id": "F028",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: EPMI new orders remained solid Exhibit 3: Container throughput growth slowed in May-June Exhibit 4: Auto and home appliance sales growth are suppressed by a high base Exhibit 5: Holiday spending is still constraine"
  },
  {
    "figure_id": "F029",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Container throughput growth slowed in May-June Exhibit 4: Auto and home appliance sales growth are suppressed by a high base Exhibit 5: Holiday spending is still constrained by a weak labor market Exhibit 6: Slow f"
  },
  {
    "figure_id": "F030",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Auto and home appliance sales growth are suppressed by a high base Exhibit 5: Holiday spending is still constrained by a weak labor market Exhibit 6: Slow fiscal rollout in May Exhibit 7: Fiscal execution yet to ac"
  },
  {
    "figure_id": "F031",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Holiday spending is still constrained by a weak labor market Exhibit 6: Slow fiscal rollout in May Exhibit 7: Fiscal execution yet to accelerate Exhibit 8: Policy bank bond issuance remained muted in June Policy Ba"
  },
  {
    "figure_id": "F032",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Slow fiscal rollout in May Exhibit 7: Fiscal execution yet to accelerate Exhibit 8: Policy bank bond issuance remained muted in June Policy Bank Bond Net Issuance (Rmb bn) Exhibit 9: Improved policy transmission wi"
  },
  {
    "figure_id": "F033",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Fiscal execution yet to accelerate Exhibit 8: Policy bank bond issuance remained muted in June Policy Bank Bond Net Issuance (Rmb bn) Exhibit 9: Improved policy transmission with narrower interest rate corridor Exh"
  },
  {
    "figure_id": "F034",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 11: Renewed softening in secondary housing sales"
  },
  {
    "figure_id": "F035",
    "report_id": "R008",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Improved policy transmission with narrower interest rate corridor Exhibit 10: Primary housing sales remain lackluster Exhibit 11: Renewed softening in secondary housing sales Exhibit 12: Capacity utilization droppe"
  },
  {
    "figure_id": "F036",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Primary housing sales remain lackluster Exhibit 11: Renewed softening in secondary housing sales Exhibit 12: Capacity utilization dropped significantly in crude oil distillation... Exhibit 13: ...and asphalt produc"
  },
  {
    "figure_id": "F037",
    "report_id": "R008",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Renewed softening in secondary housing sales Exhibit 12: Capacity utilization dropped significantly in crude oil distillation... Exhibit 13: ...and asphalt production Exhibit 14: Cement shipment improves on the mar"
  },
  {
    "figure_id": "F038",
    "report_id": "R008",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Capacity utilization dropped significantly in crude oil distillation... Exhibit 13: ...and asphalt production Exhibit 14: Cement shipment improves on the margin in June... Exhibit 15: ...as is rebar demand"
  },
  {
    "figure_id": "F039",
    "report_id": "R008",
    "label": "Exhibit 13",
    "context": "Exhibit 13: ...and asphalt production Exhibit 14: Cement shipment improves on the margin in June... Exhibit 15: ...as is rebar demand ## Disclosure Section"
  },
  {
    "figure_id": "F040",
    "report_id": "R008",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Cement shipment improves on the margin in June... Exhibit 15: ...as is rebar demand ## Disclosure Section"
  },
  {
    "figure_id": "F041",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 1: DRAM bit demand vs bit supply Figure 2: NAND bit demand vs bit supply Figure 3: DRAM bit demand vs bit consumption vs bit supply in absolute terms"
  },
  {
    "figure_id": "F042",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 1: DRAM bit demand vs bit supply Figure 2: NAND bit demand vs bit supply Figure 3: DRAM bit demand vs bit consumption vs bit supply in absolute terms Figure 4: NAND bit demand vs bit consumption vs bit supply in absol"
  },
  {
    "figure_id": "F043",
    "report_id": "R011",
    "label": "Figure 2",
    "context": "Figure 2: NAND bit demand vs bit supply Figure 3: DRAM bit demand vs bit consumption vs bit supply in absolute terms Figure 4: NAND bit demand vs bit consumption vs bit supply in absolute terms \\- A class-action lawsuit has"
  },
  {
    "figure_id": "F044",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "Figure 5: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index) %"
  },
  {
    "figure_id": "F045",
    "report_id": "R011",
    "label": "Figure 4",
    "context": "Figure 5: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index) % Companies Discussed in This Report (all prices in this report as of market close on 29 June 2026, unless otherwise indica"
  },
  {
    "figure_id": "F046",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Widening EU trade deficit with China since 2021 Exhibit 2: Europe faces a dual headwind from China: rising competitive pressure domestically and weak export demand externally."
  },
  {
    "figure_id": "F047",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Widening EU trade deficit with China since 2021 Exhibit 2: Europe faces a dual headwind from China: rising competitive pressure domestically and weak export demand externally. ## EU-China Trade Tensions: A Primer"
  },
  {
    "figure_id": "F048",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Widening EU trade deficit with China since 2021 Exhibit 2: Europe faces a dual headwind from China: rising competitive pressure domestically and weak export demand externally. ## EU-China Trade Tensions: A Primer ##"
  },
  {
    "figure_id": "F049",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: EU-China trade balance by product Exhibit 4: EU trade balance with China is worsening over time ## How would potential tensions unfold? Navigating preferences, dependencies, and chokepoints"
  },
  {
    "figure_id": "F050",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: EU-China trade balance by product Exhibit 4: EU trade balance with China is worsening over time ## How would potential tensions unfold? Navigating preferences, dependencies, and chokepoints A gradual, institutionaliz"
  },
  {
    "figure_id": "F051",
    "report_id": "R015",
    "label": "Figure 1",
    "context": "Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors. ## Other takeaways: Figure 1. 5M26 Contracted Sales (YoY change) – Five Names Posted more than 10%yoy g"
  },
  {
    "figure_id": "F052",
    "report_id": "R015",
    "label": "Figure 1",
    "context": "Figure 1. 5M26 Contracted Sales (YoY change) – Five Names Posted more than 10%yoy growth Figure 2. May 2026: more names reported positive contracted sales growth in May-26 © 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F053",
    "report_id": "R015",
    "label": "Figure 4",
    "context": "Figure 4. China Property – Listed Property Names' Contracted Sales in May 2026 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. China Property Sector — Quant Screen on Investor Position (1-month change by 19-Jun-2026) © 2026 Citi"
  },
  {
    "figure_id": "F054",
    "report_id": "R016",
    "label": "Figure 1",
    "context": "Cynthia Wu Figure 1. Monthly battery production pipeline turns out to be +1% MoM in Jun-26 Figure 2. Cathode production is forecasted to be +5% MoM in Jul-26 Figure 3. Anode production is forecasted to be +6% MoM in Jul-26"
  },
  {
    "figure_id": "F055",
    "report_id": "R016",
    "label": "Figure 1",
    "context": "Figure 1. Monthly battery production pipeline turns out to be +1% MoM in Jun-26 Figure 2. Cathode production is forecasted to be +5% MoM in Jul-26 Figure 3. Anode production is forecasted to be +6% MoM in Jul-26 © 2026 Citi Inc. No redistribution without Citi'"
  },
  {
    "figure_id": "F056",
    "report_id": "R016",
    "label": "Figure 2",
    "context": "Figure 2. Cathode production is forecasted to be +5% MoM in Jul-26 Figure 3. Anode production is forecasted to be +6% MoM in Jul-26 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Lithium production is forecasted to be -3% MoM i"
  },
  {
    "figure_id": "F057",
    "report_id": "R016",
    "label": "Figure 3",
    "context": "Figure 3. Anode production is forecasted to be +6% MoM in Jul-26 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Lithium production is forecasted to be -3% MoM in Jul-26 ## Appendix A-1"
  },
  {
    "figure_id": "F058",
    "report_id": "R017",
    "label": "Figure 1",
    "context": "Figure 1. Share Price Movement by Sector © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Share Price Movement – 1 Week © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Share Price Movement – 1 Mont"
  },
  {
    "figure_id": "F059",
    "report_id": "R017",
    "label": "Figure 2",
    "context": "Figure 2. Share Price Movement – 1 Week © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Share Price Movement – 1 Month © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Share Price Movement – 3 Mont"
  },
  {
    "figure_id": "F060",
    "report_id": "R017",
    "label": "Figure 3",
    "context": "Figure 3. Share Price Movement – 1 Month © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Share Price Movement – 3 Months © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Share Price Movement – 6 Mo"
  },
  {
    "figure_id": "F061",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4. Share Price Movement – 3 Months © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Share Price Movement – 6 Months -20% 0% 20% 40% 60% 80% 100% 120% 140% 160% 180% 200% 220% 240% © 2026 Citi Inc. No redistribution without"
  },
  {
    "figure_id": "F062",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: DDR5 pricing has been showing an upward trend since early May and is trading at +25% premium over May contract pricing DDR5 16Gb spot pricing trend \\* DRAM spot pricing as of June 26 Exhibit 3: DDR4 pricing has been sh"
  },
  {
    "figure_id": "F063",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Taiwan server ODM monthly revenue rose by +53% yoy (-3% mom) in May Taiwan server ODM monthly revenue trend"
  },
  {
    "figure_id": "F064",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Aspeed's monthly revenue increased by $+69\\%$ yoy $(+0\\%$ mom) in May Aspeed monthly revenue trend Exhibit 6: Korea DRAM exports up by +370% yoy (+21% mom) in May Korea monthly DRAM export revenue trend"
  },
  {
    "figure_id": "F065",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Korea DRAM exports up by +370% yoy (+21% mom) in May Korea monthly DRAM export revenue trend Exhibit 7: China smartphone shipment increased by +19% yoy (+7% mom) in May"
  },
  {
    "figure_id": "F066",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Aspeed's monthly revenue increased by $+69\\%$ yoy $(+0\\%$ mom) in May Aspeed monthly revenue trend Exhibit 6: Korea DRAM exports up by +370% yoy (+21% mom) in May Korea monthly DRAM export revenue trend Exhibit 7: Ch"
  },
  {
    "figure_id": "F067",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Nanya's monthly revenue increased by $+730\\%$ yoy $(+9\\%$ mom) in May Nanya monthly revenue trend"
  },
  {
    "figure_id": "F068",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "Exhibit 9: Supreme's monthly revenue increased $+253\\%$ yoy $(+54\\%$ mom) in May Supreme monthly revenue trend Exhibit 10: As our latest 2Q26E DRAM ASP estimate for SEC is for an around +46% qoq increase, we estimate the second d"
  },
  {
    "figure_id": "F069",
    "report_id": "R018",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Nanya's monthly revenue increased by $+730\\%$ yoy $(+9\\%$ mom) in May Nanya monthly revenue trend Exhibit 9: Supreme's monthly revenue increased $+253\\%$ yoy $(+54\\%$ mom) in May Supreme monthly revenue trend Exhibit"
  },
  {
    "figure_id": "F070",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Supreme's monthly revenue increased $+253\\%$ yoy $(+54\\%$ mom) in May Supreme monthly revenue trend Exhibit 10: As our latest 2Q26E DRAM ASP estimate for SEC is for an around +46% qoq increase, we estimate the second d"
  },
  {
    "figure_id": "F071",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary GFA sold last week was +38% wow and -17% yoy in c.75 cities Exhibit 2: Primary GFA sold YTD on average was -14% yoy in c.75 cities, and -15%/-43% vs. 2024/2023 level ## Secondary market: Week 26/YTD volumes w"
  },
  {
    "figure_id": "F072",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Secondary GFA sold last week was $+27\\%$ wow and $+6\\%$ yoy in c.20 cities Average weekly volume of secondary property sales Exhibit 4: Secondary GFA sold YTD was flat yoy in c.20 cities, while +18%/+10% vs. 2024/2023"
  },
  {
    "figure_id": "F073",
    "report_id": "R020",
    "label": "Exhibit 2",
    "context": "Exhibit 3: Secondary GFA sold last week was $+27\\%$ wow and $+6\\%$ yoy in c.20 cities Average weekly volume of secondary property sales Exhibit 4: Secondary GFA sold YTD was flat yoy in c.20 cities, while +18%/+10% vs. 2024/2023"
  },
  {
    "figure_id": "F074",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Exhibit 7: Inventory balance was flat wow, $-4.8\\%$ from end-25 levels c.20 cities' total inventory breakdown by city tier"
  },
  {
    "figure_id": "F075",
    "report_id": "R020",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Inventory balance was flat wow, $-4.8\\%$ from end-25 levels c.20 cities' total inventory breakdown by city tier Exhibit 8: Inventory month was $-0.3\\%$ wow, representing $-2.1\\%$ from end-25 levels c.20 cities' invento"
  },
  {
    "figure_id": "F076",
    "report_id": "R020",
    "label": "Exhibit 7",
    "context": "Exhibit 9: GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model"
  },
  {
    "figure_id": "F077",
    "report_id": "R020",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model Jan-Feb refers to average level in Jan and Feb. Exhibit 10: ...suggesting completions at a c.2"
  },
  {
    "figure_id": "F078",
    "report_id": "R020",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model Jan-Feb refers to average level in Jan and Feb. Exhibit 10: ...suggesting completions at a c.2"
  },
  {
    "figure_id": "F079",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Chinese PMI and IP Exhibit 4: Chinese CPI and PPI Exhibit 5: Chinese power generation"
  },
  {
    "figure_id": "F080",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Chinese PMI and IP Exhibit 4: Chinese CPI and PPI Exhibit 5: Chinese power generation Exhibit 6: Chinese new loans and M2 supply"
  },
  {
    "figure_id": "F081",
    "report_id": "R021",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Chinese CPI and PPI Exhibit 5: Chinese power generation Exhibit 6: Chinese new loans and M2 supply Exhibit 7: China – Excavator sales"
  },
  {
    "figure_id": "F082",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Chinese power generation Exhibit 6: Chinese new loans and M2 supply Exhibit 7: China – Excavator sales Exhibit 8: China – infrastructure spending"
  },
  {
    "figure_id": "F083",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Chinese new loans and M2 supply Exhibit 7: China – Excavator sales Exhibit 8: China – infrastructure spending Exhibit 9: Transportation infrastructure new orders reported by large infrastructure construction groups"
  },
  {
    "figure_id": "F084",
    "report_id": "R021",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China – Excavator sales Exhibit 8: China – infrastructure spending Exhibit 9: Transportation infrastructure new orders reported by large infrastructure construction groups Exhibit 10: Building construction new orde"
  },
  {
    "figure_id": "F085",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "Exhibit 8: China – infrastructure spending Exhibit 9: Transportation infrastructure new orders reported by large infrastructure construction groups Exhibit 10: Building construction new order trend for CSCEC and MCC ## China"
  },
  {
    "figure_id": "F086",
    "report_id": "R021",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Transportation infrastructure new orders reported by large infrastructure construction groups Exhibit 10: Building construction new order trend for CSCEC and MCC ## China – Property Update ## Mixed May Home sales imp"
  },
  {
    "figure_id": "F087",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China – Property sales and new starts Exhibit 12: Chinese Property – Monthly units sold in Tier 1 cities Exhibit 13: Chinese Property – Monthly units sold in Tier 2 cities"
  },
  {
    "figure_id": "F088",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China – Property sales and new starts Exhibit 12: Chinese Property – Monthly units sold in Tier 1 cities Exhibit 13: Chinese Property – Monthly units sold in Tier 2 cities Exhibit 14: Chinese Property – Monthly uni"
  },
  {
    "figure_id": "F089",
    "report_id": "R021",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Chinese Property – Monthly units sold in Tier 1 cities Exhibit 13: Chinese Property – Monthly units sold in Tier 2 cities Exhibit 14: Chinese Property – Monthly units sold in Tier 3 cities Exhibit 15: Chinese Prope"
  },
  {
    "figure_id": "F090",
    "report_id": "R021",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Chinese Property – Monthly units sold in Tier 2 cities Exhibit 14: Chinese Property – Monthly units sold in Tier 3 cities Exhibit 15: Chinese Property – Total inventory months Exhibit 16: Chinese Property – YTD new"
  },
  {
    "figure_id": "F091",
    "report_id": "R021",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Chinese Property – Monthly units sold in Tier 3 cities Exhibit 15: Chinese Property – Total inventory months Exhibit 16: Chinese Property – YTD new starts, by city tier Exhibit 17: Chinese Property – YTD sales"
  },
  {
    "figure_id": "F092",
    "report_id": "R021",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Chinese Property – Total inventory months Exhibit 16: Chinese Property – YTD new starts, by city tier Exhibit 17: Chinese Property – YTD sales Exhibit 18: Chinese Property – YTD completion"
  },
  {
    "figure_id": "F093",
    "report_id": "R021",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Chinese Property – YTD new starts, by city tier Exhibit 17: Chinese Property – YTD sales Exhibit 18: Chinese Property – YTD completion ## China – Steel and Iron Ore Update"
  },
  {
    "figure_id": "F094",
    "report_id": "R021",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Chinese Property – YTD sales Exhibit 18: Chinese Property – YTD completion ## China – Steel and Iron Ore Update ## May - MoM Uptick, But Still Lower YoY China's May finished-steel net exports rose \\~10% MoM day-adjus"
  },
  {
    "figure_id": "F095",
    "report_id": "R021",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Consumption of steel in China 2025 MSe China Steel Demand Drivers Exhibit 20: Steel product inventory at distributors Exhibit 21: GP/t for mills at spot prices"
  },
  {
    "figure_id": "F096",
    "report_id": "R021",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Consumption of steel in China 2025 MSe China Steel Demand Drivers Exhibit 20: Steel product inventory at distributors Exhibit 21: GP/t for mills at spot prices Exhibit 22: Total steel inventory in China (traders +"
  },
  {
    "figure_id": "F097",
    "report_id": "R021",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Steel product inventory at distributors Exhibit 21: GP/t for mills at spot prices Exhibit 22: Total steel inventory in China (traders + mills) Exhibit23: Spread between Chinese export prices and domestic prices"
  },
  {
    "figure_id": "F098",
    "report_id": "R021",
    "label": "Exhibit 21",
    "context": "Exhibit 21: GP/t for mills at spot prices Exhibit 22: Total steel inventory in China (traders + mills) Exhibit23: Spread between Chinese export prices and domestic prices Exhibit24: Shanghai steel futures prices"
  },
  {
    "figure_id": "F099",
    "report_id": "R021",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Total steel inventory in China (traders + mills) Exhibit23: Spread between Chinese export prices and domestic prices Exhibit24: Shanghai steel futures prices Exhibit25: Chinese exports vs. international HRC price s"
  },
  {
    "figure_id": "F100",
    "report_id": "R021",
    "label": "Exhibit23",
    "context": "Exhibit23: Spread between Chinese export prices and domestic prices Exhibit24: Shanghai steel futures prices Exhibit25: Chinese exports vs. international HRC price spread Exhibit26: Asian steel contract prices vs. East Asian"
  },
  {
    "figure_id": "F101",
    "report_id": "R021",
    "label": "Exhibit24",
    "context": "Exhibit24: Shanghai steel futures prices Exhibit25: Chinese exports vs. international HRC price spread Exhibit26: Asian steel contract prices vs. East Asian spot Exhibit27: Implied China iron ore production (62% Fe equivalent"
  },
  {
    "figure_id": "F102",
    "report_id": "R021",
    "label": "Exhibit25",
    "context": "Exhibit25: Chinese exports vs. international HRC price spread Exhibit26: Asian steel contract prices vs. East Asian spot Exhibit27: Implied China iron ore production (62% Fe equivalent) Exhibit 28: CISA member mill vs. NBS (r"
  },
  {
    "figure_id": "F103",
    "report_id": "R021",
    "label": "Exhibit26",
    "context": "Exhibit26: Asian steel contract prices vs. East Asian spot Exhibit27: Implied China iron ore production (62% Fe equivalent) Exhibit 28: CISA member mill vs. NBS (restated) average daily steel output Exhibit29: China – Iron or"
  },
  {
    "figure_id": "F104",
    "report_id": "R021",
    "label": "Exhibit27",
    "context": "Exhibit27: Implied China iron ore production (62% Fe equivalent) Exhibit 28: CISA member mill vs. NBS (restated) average daily steel output Exhibit29: China – Iron ore prices Iron ore concentrate 66% Fe dry / China domestic E"
  },
  {
    "figure_id": "F105",
    "report_id": "R021",
    "label": "Exhibit 28",
    "context": "Exhibit30: Iron ore inventories at China's major ports"
  },
  {
    "figure_id": "F106",
    "report_id": "R021",
    "label": "Exhibit29",
    "context": "Exhibit 32: China's iron ore stock at ports and stock-to-consumption ratio"
  },
  {
    "figure_id": "F107",
    "report_id": "R021",
    "label": "Exhibit30",
    "context": "Exhibit30: Iron ore inventories at China's major ports Exhibit31: Chinese iron ore miners' average daily output and operating rate Exhibit 32: China's iron ore stock at ports and stock-to-consumption ratio Exhibit33: Brazilia"
  },
  {
    "figure_id": "F108",
    "report_id": "R021",
    "label": "Exhibit31",
    "context": "Exhibit31: Chinese iron ore miners' average daily output and operating rate Exhibit 32: China's iron ore stock at ports and stock-to-consumption ratio Exhibit33: Brazilian and West Australian freight rates Exhibit34: Rebar ut"
  },
  {
    "figure_id": "F109",
    "report_id": "R021",
    "label": "Exhibit 32",
    "context": "Exhibit 32: China's iron ore stock at ports and stock-to-consumption ratio Exhibit33: Brazilian and West Australian freight rates Exhibit34: Rebar utilization rate Exhibit35: Electric arc furnace (EAF) capacity utilization rat"
  },
  {
    "figure_id": "F110",
    "report_id": "R021",
    "label": "Exhibit33",
    "context": "Exhibit33: Brazilian and West Australian freight rates Exhibit34: Rebar utilization rate Exhibit35: Electric arc furnace (EAF) capacity utilization rate EAF Capacity Utilization Rate Exhibit 36: Iron ore prices: -discount/+pr"
  },
  {
    "figure_id": "F111",
    "report_id": "R021",
    "label": "Exhibit34",
    "context": "Exhibit34: Rebar utilization rate Exhibit35: Electric arc furnace (EAF) capacity utilization rate EAF Capacity Utilization Rate Exhibit 36: Iron ore prices: -discount/+premium vs. 62% Fe (%) ## China – Coal Update"
  },
  {
    "figure_id": "F112",
    "report_id": "R021",
    "label": "Exhibit35",
    "context": "Exhibit35: Electric arc furnace (EAF) capacity utilization rate EAF Capacity Utilization Rate Exhibit 36: Iron ore prices: -discount/+premium vs. 62% Fe (%) ## China – Coal Update ## Domestic Coal Prices Firm as Summer Demand O"
  },
  {
    "figure_id": "F113",
    "report_id": "R021",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Chart of the Week – Coal Inventory at China's big 6 IPPs Groups Exhibit 38: Data for the week"
  },
  {
    "figure_id": "F114",
    "report_id": "R021",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Data for the week Exhibit 39: China vs. regional FOB thermal coal prices Exhibit40: China's coking coal prices – Mine-mouth vs. FOR Exhibit41: Coal inventory at QHD port"
  },
  {
    "figure_id": "F115",
    "report_id": "R021",
    "label": "Exhibit 39",
    "context": "Exhibit 39: China vs. regional FOB thermal coal prices Exhibit40: China's coking coal prices – Mine-mouth vs. FOR Exhibit41: Coal inventory at QHD port Exhibit 42: Coal inventory at Bohai Rim ports"
  },
  {
    "figure_id": "F116",
    "report_id": "R021",
    "label": "Exhibit40",
    "context": "Exhibit40: China's coking coal prices – Mine-mouth vs. FOR Exhibit41: Coal inventory at QHD port Exhibit 42: Coal inventory at Bohai Rim ports Exhibit 43: Water level of Three Gorges Dam"
  },
  {
    "figure_id": "F117",
    "report_id": "R021",
    "label": "Exhibit41",
    "context": "Exhibit41: Coal inventory at QHD port Exhibit 42: Coal inventory at Bohai Rim ports Exhibit 43: Water level of Three Gorges Dam Exhibit 44: China's weekly coal arrivals"
  },
  {
    "figure_id": "F118",
    "report_id": "R021",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Coal inventory at Bohai Rim ports Exhibit 43: Water level of Three Gorges Dam Exhibit 44: China's weekly coal arrivals ## Major Theme of the Month"
  },
  {
    "figure_id": "F119",
    "report_id": "R021",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Water level of Three Gorges Dam Exhibit 44: China's weekly coal arrivals ## Major Theme of the Month ## Metals in the Eye of El Niño NOAA has confirmed an El Niño for this year and raised the probability of a very st"
  },
  {
    "figure_id": "F120",
    "report_id": "R021",
    "label": "Exhibit 45",
    "context": "Exhibit 47: Weather patterns influence Yunnan's hydro generation with prolonged droughts bringing deeper troughs at the start of the year ## Disclosure Section"
  },
  {
    "figure_id": "F121",
    "report_id": "R021",
    "label": "Exhibit 46",
    "context": "Exhibit 46: El Niño shows a correlation with increased weather-related disruptions Exhibit 47: Weather patterns influence Yunnan's hydro generation with prolonged droughts bringing deeper troughs at the start of the year ## Disc"
  },
  {
    "figure_id": "F122",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "## Commodities Strategy Views ## 1. What the AI market is telling us about power scarcity The AI market signals that power access is a revenue and cost constraint in addition to being an infrastructure concern. Frontier model providers continue to strike bespo"
  },
  {
    "figure_id": "F123",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "The AI market signals that power access is a revenue and cost constraint in addition to being an infrastructure concern. Frontier model providers continue to strike bespoke compute-and-power deals with infrastructure owners, while hyperscalers are using their "
  },
  {
    "figure_id": "F124",
    "report_id": "R027",
    "label": "Figure 3",
    "context": "## 2. Energy security through energy transition Geopolitical stress around the Middle East, along with price volatility and spikes, reinforces the case for reducing marginal LNG and oil exposure. The IEA's recent “Southeast Asia Energy Outlook 2026” reinforces"
  },
  {
    "figure_id": "F125",
    "report_id": "R027",
    "label": "Figure 6",
    "context": "Obtaining power supply for a data center is now a complex, tall order: Can we get firm power that is flexible enough to accommodate the massive demand and supply swings, without destabilizing the grid or triggering political backlash? This shift is now visible"
  },
  {
    "figure_id": "F126",
    "report_id": "R027",
    "label": "Figure 6",
    "context": "The demand and supply growth shocks go beyond just (a) volume growth; they also include (b) availability and (c) volatility issues. (a) Volume: The U.S. Federal Energy Regulatory Commission (FERC) said more than 50GW of data center capacity was operating in th"
  },
  {
    "figure_id": "F127",
    "report_id": "R027",
    "label": "Figure 8",
    "context": "At first glance, onsite generation, or bring your own generation (BYOG), has become an obvious solution, mostly using natural gas to power turbines, engines, or fuel cells. Nonetheless, a key consideration in the current market is the durability of long-term p"
  },
  {
    "figure_id": "F128",
    "report_id": "R027",
    "label": "Figure 8",
    "context": "Nonetheless, a key consideration in the current market is the durability of long-term power demand, because there was an overbuild of natural gas-fired generation around the 2000 period. The power industry remembers the early-2000s gas-build cycle, when a data"
  },
  {
    "figure_id": "F129",
    "report_id": "R027",
    "label": "Figure 10",
    "context": "Permitting is already a necessarily extensive process to safeguard consumers and the power network. The wait in the U.S. is worsened by some degree of duplicative applications, the need to address technical challenges for large loads, and cost-of-living concer"
  },
  {
    "figure_id": "F130",
    "report_id": "R027",
    "label": "Figure 12",
    "context": "Wood Mackenzie estimates a 707.5GVA annual shortfall in 2025, based on global transformer supply of 2,358.5GVA and an assumed 30% deficit, implying that some current demand is being deferred until additional supply comes online. The global supply estimate is d"
  },
  {
    "figure_id": "F131",
    "report_id": "R027",
    "label": "Figure 12",
    "context": "Figure 12. 2025 market share by capacity total 2,358.5GVA However, we estimate the cumulative shortage will keep rising and peak in 2028 at 1,698.8 GVA — equal to 47% of annual supply in that year — and persist in the run-up to 2030. For supply growth, the top"
  },
  {
    "figure_id": "F132",
    "report_id": "R027",
    "label": "Figure 16",
    "context": "\\- Rising energy share from renewables globally. Ariston Advisory forecasts around 4,000GW of new power generating capacity in 2025–2027 driven by more renewable energy uses and catering to increasing electricity demand. \\- Replacement of aging infrastructures"
  },
  {
    "figure_id": "F133",
    "report_id": "R027",
    "label": "Figure 18",
    "context": "generation costs, but are too large to be in population centers, where power demand is large. However, if the speed-to-power problem does not improve significantly, other power consumers could increasingly adopt BYOG as well. Data centers are large loads that "
  },
  {
    "figure_id": "F134",
    "report_id": "R027",
    "label": "Figure 19",
    "context": "Equipment manufacturers accelerating investments to deal with the supply-chain bottleneck Power equipment manufacturers are facing significant challenges in scaling production of turbines and engines to meet rising order volumes. Lead times for some equipment "
  },
  {
    "figure_id": "F135",
    "report_id": "R027",
    "label": "Figure 21",
    "context": "## Scott Gruber Separately, we believe the market for behind-the-meter power from third-party suppliers will grow toward 25GW in 2030, with the vast majority of capacity deployed at data centers. With uncertainty toward timing of grid connect and rising reside"
  },
  {
    "figure_id": "F136",
    "report_id": "R027",
    "label": "Figure 22",
    "context": "Over the past decade, oilfield services companies developed and deployed small-scale mobile turbines as well as gas reciprocating engines to convert cheap, abundant natural gas into power to run hydraulic frac pumps. The midstream industry also has experience "
  },
  {
    "figure_id": "F137",
    "report_id": "R027",
    "label": "Figure 25",
    "context": "## Variable costs The next largest cost line item is natural gas. Each technology's heat rate is the primary determinant of natural gas consumed. At a flatlined \\$4.0 gas cost (\\$/MMBtu), the gas cost makes up 31%, 32%, and 25%, respectively, for CCGT, recips,"
  },
  {
    "figure_id": "F138",
    "report_id": "R027",
    "label": "Figure 27",
    "context": "Fuel availability and pipelines can become the next bottleneck, shifting constraints from somewhere along the power infrastructure to natural gas infrastructure. Bottlenecks appear more often at the local lateral or facility level, rather than at the interstat"
  },
  {
    "figure_id": "F139",
    "report_id": "R027",
    "label": "Figure 28",
    "context": "We still appear to be in early stages of project development for two reasons. First, our U.S. Utilities team forecasts 96GW of net natural gas generation needed to support power demand growth, where data centers represent 1/3 of total U.S. power demand growth."
  },
  {
    "figure_id": "F140",
    "report_id": "R027",
    "label": "Figure 29",
    "context": "## We're here because of years of underinvestment Rising natural gas demand and pipeline underinvestment have created the most attractive commercial environment in recent memory, with U.S. natural gas pipeline capacity effectively full. We analyzed the top-50 "
  },
  {
    "figure_id": "F141",
    "report_id": "R027",
    "label": "Figure 30",
    "context": "The global surge in AI adoption is reshaping energy landscapes, with distinct regional approaches and challenges emerging in the power markets of the U.S., Europe, China and Australia. Their unique regulatory frameworks, existing energy infrastructure, and str"
  },
  {
    "figure_id": "F142",
    "report_id": "R027",
    "label": "Figure 31",
    "context": "While each region faces different sets of political/regulatory challenges, this contest for speed to power creates opportunity for electric wires and generation investments. ## ERCOT: Texas Large load approval moves from ad hoc review to batch study: ERCOT's a"
  },
  {
    "figure_id": "F143",
    "report_id": "R027",
    "label": "Figure 32",
    "context": "For ERCOT, the issue with their stakeholders isn't utility bill affordability, unlike many other regions in the U.S. with data center growth prospects. There are over 300GW of projects requesting grid access via the ERCOT batch study process, but the grid can'"
  },
  {
    "figure_id": "F144",
    "report_id": "R027",
    "label": "Figure 33",
    "context": "This constraint is forcing Texas to be selective on which load it will allow to connect to the grid based on 1) transmission limitations, 2) site location, 3) neighboring load, and 4) load shaping, along with anticipated grid expansion plans. Beyond grid conne"
  },
  {
    "figure_id": "F145",
    "report_id": "R027",
    "label": "Figure 34",
    "context": "developers, utilities (wires companies), data centers, state governors, and others. We think the PJM approach should yield positive outcomes, but is not a complete solution to the problems being faced. Working through policy challenges: PJM is well aware of th"
  },
  {
    "figure_id": "F146",
    "report_id": "R027",
    "label": "Figure 35",
    "context": "The Midwest is an attractive data center market, but has some physical constraints such as transmission and gas pipelines, as well as local politics. The region has several advantages such as relatively reasonable grid policy, access to gas, and frameworks for"
  },
  {
    "figure_id": "F147",
    "report_id": "R027",
    "label": "Figure 36",
    "context": "## Structural system differences: fuel, policy and cost Europe's data centre opportunity sits within a structurally different power system to the U.S., defined by limited access to low-cost domestic fossil fuels and stronger policy commitment to decarbonisatio"
  },
  {
    "figure_id": "F148",
    "report_id": "R027",
    "label": "Figure 36",
    "context": "Figure 36. Europe has de-industrialized, creating spare capacity power generation ## Data centre growth part of electrification investment cycle Europe is undergoing an investment cycle to support electrification in transport, heating, and industry demand. Dat"
  },
  {
    "figure_id": "F149",
    "report_id": "R027",
    "label": "Figure 38",
    "context": "Structural constraints – long connection queues, renewable intermittency, and high energy costs – are not easily resolved, meaning a portion of announced capacity risks remaining “bragawatts” rather than realised load. In this context, we see data centres as a"
  },
  {
    "figure_id": "F150",
    "report_id": "R027",
    "label": "Figure 40",
    "context": "## Country-level view – system tightness matters Figure 40. Portuguese power demand stands out Pierre Lau, CFA Bella Tian Air Ma Asian Utilities & Clean Energy ## 3. China Power Plant Equipment"
  },
  {
    "figure_id": "F151",
    "report_id": "R027",
    "label": "Figure 42",
    "context": "Australian Energy and Utilities Australia's Energy Market Operator (AEMO) estimates that in FY25 (year ending June 2025), data centers consumed 3.9 terra-watt hours (TWh) of electricity, with 98% of this coming from NEM (East and Central Coast of Australia, an"
  },
  {
    "figure_id": "F152",
    "report_id": "R028",
    "label": "Exhibit 2",
    "context": "TRACKING U.S. SUPPLY CHAIN CONGESTION # GS Supply Chain Congestion Scale: June 29th; Index Higher W/W, Bottleneck Scale Unchanged at ‘2’ GS Supply Chain Congestion Scale Week of 6/29/2026 Scale is based solely off weekly metrics to give more granularity on hig"
  },
  {
    "figure_id": "F153",
    "report_id": "R028",
    "label": "Exhibit 9",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F154",
    "report_id": "R028",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F155",
    "report_id": "R028",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 4/1\\* container ships backed up this week on the East/West Coast West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - June 2026 \\*East Coast is estimated via satellite data - includes container ships"
  },
  {
    "figure_id": "F156",
    "report_id": "R028",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~14% YoY on average in June West Coast Class 1 Rail Inter"
  },
  {
    "figure_id": "F157",
    "report_id": "R028",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~14% YoY on average in June West Coast Class 1 Rail Inter"
  },
  {
    "figure_id": "F158",
    "report_id": "R028",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast"
  },
  {
    "figure_id": "F159",
    "report_id": "R028",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast Rate is \\$ per FEU (Forty-Foot Equivalent Unit) ## Lagged Monthly Indicators (May Data) San Pedro's Bay Container Dwell \\- Container weighted"
  },
  {
    "figure_id": "F160",
    "report_id": "R028",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days Exhibit 12: % of Containers Dwelling More than 5 Days Exhibit 13: Rail Container Dwell Time, Days"
  },
  {
    "figure_id": "F161",
    "report_id": "R028",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days Exhibit 12: % of Containers Dwelling More than 5 Days Exhibit 13: Rail Container Dwell Time, Days \"Big Three\" West Coast Ports' Inbound Loaded Containe"
  },
  {
    "figure_id": "F162",
    "report_id": "R028",
    "label": "Exhibit 12",
    "context": "Exhibit 14: West Coast Ports' Inbound Loaded Containers +30% YoY in April"
  },
  {
    "figure_id": "F163",
    "report_id": "R028",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Door to Door Shipping Days, China to US"
  },
  {
    "figure_id": "F164",
    "report_id": "R028",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted"
  },
  {
    "figure_id": "F165",
    "report_id": "R028",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted LMI Capacity and Utilization ## ■ LMI Transportation Capacity Index Transportation capacity contracted in May at a slower rate compared to April given the"
  },
  {
    "figure_id": "F166",
    "report_id": "R028",
    "label": "Exhibit 17",
    "context": "Exhibit 17: PMI: Manufacturing Suppliers' Delivery Times, YoY, Seasonally Adjusted ## Appendix Given the importance supply chain fluidity has on retailers, consumer goods companies, inflationary pricing, etc., we think this scale'"
  },
  {
    "figure_id": "F167",
    "report_id": "R028",
    "label": "Exhibit 19",
    "context": "Exhibit 18: The weekly composite index (light blue) leads the monthly (dark blue); expect future monthly updates to confirm recent weekly trends Exhibit 19: Our combined scale averaged ‘108’ in May, indicating a bottleneck score o"
  },
  {
    "figure_id": "F168",
    "report_id": "R028",
    "label": "Exhibit 18",
    "context": "Exhibit 20: GS Legacy Supply Chain Congestion Scale (incorporates monthly and weekly data)"
  },
  {
    "figure_id": "F169",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Cumulative outperformance Exhibit 3: Weekly hit ratio Three Actionable Ideas are not and should not be considered a portfolio: Each investment idea is chosen based on its own merit and without any consideration of th"
  },
  {
    "figure_id": "F170",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Three Actionable Ideas – Still in effect"
  },
  {
    "figure_id": "F171",
    "report_id": "R029",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Number of ideas, by market Exhibit 7: Idea performance, by market"
  },
  {
    "figure_id": "F172",
    "report_id": "R031",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Cumulative outperformance Exhibit 3: Weekly hit ratio Three Actionable Ideas are not and should not be considered a portfolio: Each investment idea is chosen based on its own merit and without any consideration of th"
  },
  {
    "figure_id": "F173",
    "report_id": "R031",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Three Actionable Ideas – Still in effect"
  },
  {
    "figure_id": "F174",
    "report_id": "R031",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Number of ideas, by market Exhibit 7: Idea performance, by market"
  },
  {
    "figure_id": "F175",
    "report_id": "R033",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Integrated margins are below mid-cycle levels Exhibit 2: Commodity chemical valuations remain near trough levels despite improving fundamentals ## Chemical: The Cycles in Perspective"
  },
  {
    "figure_id": "F176",
    "report_id": "R033",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Integrated margins are below mid-cycle levels Exhibit 2: Commodity chemical valuations remain near trough levels despite improving fundamentals ## Chemical: The Cycles in Perspective Exhibit 3: EBITDA/ton for Asian c"
  },
  {
    "figure_id": "F177",
    "report_id": "R033",
    "label": "Exhibit 2",
    "context": "Exhibit 5: Asian commodity stocks are trading at 1x one-year forward price-to-book"
  },
  {
    "figure_id": "F178",
    "report_id": "R033",
    "label": "Exhibit 3",
    "context": "Exhibit 6: .We see an improving FCF profile and a renewed focus on balance sheet and capital allocation"
  },
  {
    "figure_id": "F179",
    "report_id": "R033",
    "label": "Exhibit 4",
    "context": "Exhibit 7: Asian chemical plants have been lowering plant runs and volumes, as well as cutting capacity since 2021"
  },
  {
    "figure_id": "F180",
    "report_id": "R033",
    "label": "Exhibit 5",
    "context": "Exhibit 8: PE – incremental supply-demand gap set to narrow in the near term"
  },
  {
    "figure_id": "F181",
    "report_id": "R033",
    "label": "Exhibit 6",
    "context": "Exhibit 9: Rise in the Street's 2028 EPS estimates indicates a structural turnaround as capacity consolidates"
  },
  {
    "figure_id": "F182",
    "report_id": "R033",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Asian chemical plants have been lowering plant runs and volumes, as well as cutting capacity since 2021 Exhibit 8: PE – incremental supply-demand gap set to narrow in the near term Exhibit 9: Rise in the Street's 202"
  },
  {
    "figure_id": "F183",
    "report_id": "R033",
    "label": "Exhibit 8",
    "context": "Exhibit 8: PE – incremental supply-demand gap set to narrow in the near term Exhibit 9: Rise in the Street's 2028 EPS estimates indicates a structural turnaround as capacity consolidates ## How Spreads Are Moving Exhibit 10: Pr"
  },
  {
    "figure_id": "F184",
    "report_id": "R033",
    "label": "Exhibit 9",
    "context": "Exhibit 12: PET spreads have significantly outperformed YTD"
  },
  {
    "figure_id": "F185",
    "report_id": "R033",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Product spreads are beginning to recover across key chemical chains Exhibit 11: PE spreads are near cyclical average (ex-Covid period) Exhibit 12: PET spreads have significantly outperformed YTD"
  },
  {
    "figure_id": "F186",
    "report_id": "R033",
    "label": "Exhibit 11",
    "context": "Exhibit 11: PE spreads are near cyclical average (ex-Covid period) Exhibit 12: PET spreads have significantly outperformed YTD Exhibit 14: Integrated phenolic spreads have softened in the past month; back to pre-crisis levels"
  },
  {
    "figure_id": "F187",
    "report_id": "R033",
    "label": "Exhibit 12",
    "context": "Exhibit 12: PET spreads have significantly outperformed YTD Exhibit 14: Integrated phenolic spreads have softened in the past month; back to pre-crisis levels ## Valuation Methodology and Risks"
  },
  {
    "figure_id": "F188",
    "report_id": "R033",
    "label": "Exhibit 13",
    "context": "Exhibit 14: Integrated phenolic spreads have softened in the past month; back to pre-crisis levels ## Valuation Methodology and Risks ## China Petroleum & Chemical Corp. (0386.HK) ■ E&P business - DCF (WACC of 9.6% and long-term g"
  },
  {
    "figure_id": "F189",
    "report_id": "R034",
    "label": "Exhibit 2",
    "context": "TRACKING U.S. SUPPLY CHAIN CONGESTION # GS Supply Chain Congestion Scale: June 29th; Index Higher W/W, Bottleneck Scale Unchanged at ‘2’ GS Supply Chain Congestion Scale Week of 6/29/2026 Scale is based solely off weekly metrics to give more granularity on hig"
  },
  {
    "figure_id": "F190",
    "report_id": "R034",
    "label": "Exhibit 9",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F191",
    "report_id": "R034",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F192",
    "report_id": "R034",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 4/1\\* container ships backed up this week on the East/West Coast West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - June 2026 \\*East Coast is estimated via satellite data - includes container ships"
  },
  {
    "figure_id": "F193",
    "report_id": "R034",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~14% YoY on average in June West Coast Class 1 Rail Inter"
  },
  {
    "figure_id": "F194",
    "report_id": "R034",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~14% YoY on average in June West Coast Class 1 Rail Inter"
  },
  {
    "figure_id": "F195",
    "report_id": "R034",
    "label": "Exhibit 9",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast"
  },
  {
    "figure_id": "F196",
    "report_id": "R034",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast Rate is \\$ per FEU (Forty-Foot Equivalent Unit) ## Lagged Monthly Indicators (May Data) San Pedro's Bay Container Dwell \\- Container weighted"
  },
  {
    "figure_id": "F197",
    "report_id": "R034",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days Exhibit 12: % of Containers Dwelling More than 5 Days Exhibit 13: Rail Container Dwell Time, Days"
  },
  {
    "figure_id": "F198",
    "report_id": "R034",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days Exhibit 12: % of Containers Dwelling More than 5 Days Exhibit 13: Rail Container Dwell Time, Days \"Big Three\" West Coast Ports' Inbound Loaded Containe"
  },
  {
    "figure_id": "F199",
    "report_id": "R034",
    "label": "Exhibit 12",
    "context": "Exhibit 14: West Coast Ports' Inbound Loaded Containers +30% YoY in April"
  },
  {
    "figure_id": "F200",
    "report_id": "R034",
    "label": "Exhibit 14",
    "context": "Exhibit 15: Door to Door Shipping Days, China to US"
  },
  {
    "figure_id": "F201",
    "report_id": "R034",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted"
  },
  {
    "figure_id": "F202",
    "report_id": "R034",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted LMI Capacity and Utilization ## ■ LMI Transportation Capacity Index Transportation capacity contracted in May at a slower rate compared to April given the"
  },
  {
    "figure_id": "F203",
    "report_id": "R034",
    "label": "Exhibit 17",
    "context": "Exhibit 17: PMI: Manufacturing Suppliers' Delivery Times, YoY, Seasonally Adjusted ## Appendix Given the importance supply chain fluidity has on retailers, consumer goods companies, inflationary pricing, etc., we think this scale'"
  },
  {
    "figure_id": "F204",
    "report_id": "R034",
    "label": "Exhibit 19",
    "context": "Exhibit 18: The weekly composite index (light blue) leads the monthly (dark blue); expect future monthly updates to confirm recent weekly trends Exhibit 19: Our combined scale averaged ‘108’ in May, indicating a bottleneck score o"
  },
  {
    "figure_id": "F205",
    "report_id": "R034",
    "label": "Exhibit 18",
    "context": "Exhibit 20: GS Legacy Supply Chain Congestion Scale (incorporates monthly and weekly data)"
  },
  {
    "figure_id": "F206",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Integrated margins are below mid-cycle levels Exhibit 2: Commodity chemical valuations remain near trough levels despite improving fundamentals ## Chemical: The Cycles in Perspective"
  },
  {
    "figure_id": "F207",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Integrated margins are below mid-cycle levels Exhibit 2: Commodity chemical valuations remain near trough levels despite improving fundamentals ## Chemical: The Cycles in Perspective Exhibit 3: EBITDA/ton for Asian c"
  },
  {
    "figure_id": "F208",
    "report_id": "R037",
    "label": "Exhibit 2",
    "context": "Exhibit 5: Asian commodity stocks are trading at 1x one-year forward price-to-book"
  },
  {
    "figure_id": "F209",
    "report_id": "R037",
    "label": "Exhibit 3",
    "context": "Exhibit 6: .We see an improving FCF profile and a renewed focus on balance sheet and capital allocation"
  },
  {
    "figure_id": "F210",
    "report_id": "R037",
    "label": "Exhibit 4",
    "context": "Exhibit 7: Asian chemical plants have been lowering plant runs and volumes, as well as cutting capacity since 2021"
  },
  {
    "figure_id": "F211",
    "report_id": "R037",
    "label": "Exhibit 5",
    "context": "Exhibit 8: PE – incremental supply-demand gap set to narrow in the near term"
  },
  {
    "figure_id": "F212",
    "report_id": "R037",
    "label": "Exhibit 6",
    "context": "Exhibit 9: Rise in the Street's 2028 EPS estimates indicates a structural turnaround as capacity consolidates"
  },
  {
    "figure_id": "F213",
    "report_id": "R037",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Asian chemical plants have been lowering plant runs and volumes, as well as cutting capacity since 2021 Exhibit 8: PE – incremental supply-demand gap set to narrow in the near term Exhibit 9: Rise in the Street's 202"
  },
  {
    "figure_id": "F214",
    "report_id": "R037",
    "label": "Exhibit 8",
    "context": "Exhibit 8: PE – incremental supply-demand gap set to narrow in the near term Exhibit 9: Rise in the Street's 2028 EPS estimates indicates a structural turnaround as capacity consolidates ## How Spreads Are Moving Exhibit 10: Pr"
  },
  {
    "figure_id": "F215",
    "report_id": "R037",
    "label": "Exhibit 9",
    "context": "Exhibit 12: PET spreads have significantly outperformed YTD"
  },
  {
    "figure_id": "F216",
    "report_id": "R037",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Product spreads are beginning to recover across key chemical chains Exhibit 11: PE spreads are near cyclical average (ex-Covid period) Exhibit 12: PET spreads have significantly outperformed YTD"
  },
  {
    "figure_id": "F217",
    "report_id": "R037",
    "label": "Exhibit 11",
    "context": "Exhibit 11: PE spreads are near cyclical average (ex-Covid period) Exhibit 12: PET spreads have significantly outperformed YTD Exhibit 14: Integrated phenolic spreads have softened in the past month; back to pre-crisis levels"
  },
  {
    "figure_id": "F218",
    "report_id": "R037",
    "label": "Exhibit 12",
    "context": "Exhibit 12: PET spreads have significantly outperformed YTD Exhibit 14: Integrated phenolic spreads have softened in the past month; back to pre-crisis levels ## Valuation Methodology and Risks"
  },
  {
    "figure_id": "F219",
    "report_id": "R037",
    "label": "Exhibit 13",
    "context": "Exhibit 14: Integrated phenolic spreads have softened in the past month; back to pre-crisis levels ## Valuation Methodology and Risks ## China Petroleum & Chemical Corp. (0386.HK) ■ E&P business - DCF (WACC of 9.6% and long-term g"
  },
  {
    "figure_id": "F220",
    "report_id": "R041",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The Y/Y change was mainly driven by warehouses EXHIBIT 4: Latest month's % Y/Y Change in Square Footage EXHIBIT 5: Price Per Square Foot"
  },
  {
    "figure_id": "F221",
    "report_id": "R041",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The Y/Y change was mainly driven by warehouses EXHIBIT 4: Latest month's % Y/Y Change in Square Footage EXHIBIT 5: Price Per Square Foot"
  },
  {
    "figure_id": "F222",
    "report_id": "R041",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Price Per Square Foot EXHIBIT 6: Non Residential Construction Seasonality EXHIBIT 7: Value of Total Construction Starts (\\$ '000s) EXHIBIT 8: Value of Non Building + Non-Residential Construction Starts"
  },
  {
    "figure_id": "F223",
    "report_id": "R041",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 9: The % of end markets (measured in value and ex resi) with a positive growth rate remained at 55% and below the historical median of 60%"
  },
  {
    "figure_id": "F224",
    "report_id": "R041",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Value of Total Construction Starts (\\$ '000s) EXHIBIT 8: Value of Non Building + Non-Residential Construction Starts % of Non-Resi End Markets with a Positive Growth Rate - Value EXHIBIT 9: The % of end markets (meas"
  },
  {
    "figure_id": "F225",
    "report_id": "R041",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: The % of end markets (measured in sq ft and ex resi) with a positive growth rate increased from \\~45% the prior month to \\~55%, in line with the historical median of \\~55% % of Non-Resi End Markets with a Positive Growth"
  },
  {
    "figure_id": "F226",
    "report_id": "R041",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: The \\$ Value of Construction Starts has Increasingly Been Driven by Price Inflation Square Footage ('000s)"
  },
  {
    "figure_id": "F227",
    "report_id": "R041",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 12: Non-Resi Construction Starts Square Footage Declined and the TTM value followed"
  },
  {
    "figure_id": "F228",
    "report_id": "R041",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 14: Warehouse Starts declined in the latest read"
  },
  {
    "figure_id": "F229",
    "report_id": "R041",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 14: Warehouse Starts declined in the latest read SPOTLIGHT ON MANUFACTURING CONSTRUCTION STARTS EXHIBIT 15: Manufacturing Construction Starts had a significant rebound in the latest read"
  },
  {
    "figure_id": "F230",
    "report_id": "R041",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 15: Manufacturing Construction Starts had a significant rebound in the latest read TTM SQUARE FOOTAGE Manufacturing Plants, Warehouses, Labs SQUARE FOOTAGE Manufacturing Plants, Warehouses, Labs"
  },
  {
    "figure_id": "F231",
    "report_id": "R041",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 16: Mega Projects value starts per month"
  },
  {
    "figure_id": "F232",
    "report_id": "R041",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 16: Mega Projects value starts per month EXHIBIT 17: Mega Projects accounted for \\~30% of all non residential starts in May(vs \\~20%TTM) EXHIBIT 18: LNG is currently the largest contributor to mega projects, followed by"
  },
  {
    "figure_id": "F233",
    "report_id": "R041",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Mega Projects value starts per month EXHIBIT 17: Mega Projects accounted for \\~30% of all non residential starts in May(vs \\~20%TTM) EXHIBIT 18: LNG is currently the largest contributor to mega projects, followed by"
  },
  {
    "figure_id": "F234",
    "report_id": "R041",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 19: Largest Project List of Nonresidential Building over the last 12 months"
  },
  {
    "figure_id": "F235",
    "report_id": "R041",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 23: Housing affordability, which has historically anchored construction starts, declined in the latest read, and remains well below pre-pandemic levels"
  },
  {
    "figure_id": "F236",
    "report_id": "R041",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 23: Housing affordability, which has historically anchored construction starts, declined in the latest read, and remains well below pre-pandemic levels We would like to thank Federico Anchieri for his hard work and signifi"
  },
  {
    "figure_id": "F237",
    "report_id": "R041",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: After Adjusting for the Lead Time of Economic Profits, it Suggests Non-Residential Construction Starts Will Continue to Decline Through At Least The Next 12 Months EXHIBIT 23: Housing affordability, which has historica"
  },
  {
    "figure_id": "F238",
    "report_id": "R042",
    "label": "Exhibit 5",
    "context": "Exhibit 4: MLCC market share Exhibit 5: MLCC market share (CY25) ## Disclosure Section"
  },
  {
    "figure_id": "F239",
    "report_id": "R042",
    "label": "Exhibit 4",
    "context": "Exhibit 4: MLCC market share Exhibit 5: MLCC market share (CY25) ## Disclosure Section The information and opinions in MS were prepared by MS MUFG Securities Co., Ltd. and its affiliates (collectively, \"MS\"). For important disc"
  },
  {
    "figure_id": "F240",
    "report_id": "R043",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Micron's y/y revenue growth has rapidly accelerated in recent quarters ## TECHNOLOGY - SOFTWARE & SERVICES Europe"
  },
  {
    "figure_id": "F241",
    "report_id": "R043",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Informa historical NTM adj. P/E valuation (consensus) 3) SAP CEO: \"there is a chance that in 3-4 years there is actually no one developing software inside SAP any more\" (#Software, #SAP): Speaking to the Australian Fin"
  },
  {
    "figure_id": "F242",
    "report_id": "R043",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Key week ahead events Coverage Valuation vs. European Market Exhibit 4: European Software NTM P/E vs STOXX Europe 600 ## Long-Term Valuation Charts Exhibit 5: Amadeus P/NTM Earnings"
  },
  {
    "figure_id": "F243",
    "report_id": "R043",
    "label": "Exhibit 4",
    "context": "Exhibit 4: European Software NTM P/E vs STOXX Europe 600 ## Long-Term Valuation Charts Exhibit 5: Amadeus P/NTM Earnings Exhibit 6: Capgemini P/NTM Earnings Exhibit 7: Dassault Systemes P/NTM Earnings"
  },
  {
    "figure_id": "F244",
    "report_id": "R043",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Amadeus P/NTM Earnings Exhibit 6: Capgemini P/NTM Earnings Exhibit 7: Dassault Systemes P/NTM Earnings Exhibit 8: HBX Group International P/NTM Earnings"
  },
  {
    "figure_id": "F245",
    "report_id": "R043",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Capgemini P/NTM Earnings Exhibit 7: Dassault Systemes P/NTM Earnings Exhibit 8: HBX Group International P/NTM Earnings Exhibit 9: Indra P/NTM Earnings"
  },
  {
    "figure_id": "F246",
    "report_id": "R043",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Dassault Systemes P/NTM Earnings Exhibit 8: HBX Group International P/NTM Earnings Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings"
  },
  {
    "figure_id": "F247",
    "report_id": "R043",
    "label": "Exhibit 8",
    "context": "Exhibit 8: HBX Group International P/NTM Earnings Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings"
  },
  {
    "figure_id": "F248",
    "report_id": "R043",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings Exhibit 12: Nemetschek Group P/NTM Earnings"
  },
  {
    "figure_id": "F249",
    "report_id": "R043",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings Exhibit 12: Nemetschek Group P/NTM Earnings Exhibit 13: Netcompany P/NTM Earnings"
  },
  {
    "figure_id": "F250",
    "report_id": "R043",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings Exhibit 12: Nemetschek Group P/NTM Earnings Exhibit 13: Netcompany P/NTM Earnings Exhibit 14: RELX P/NTM Earnings"
  },
  {
    "figure_id": "F251",
    "report_id": "R043",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Nemetschek Group P/NTM Earnings Exhibit 13: Netcompany P/NTM Earnings Exhibit 14: RELX P/NTM Earnings Exhibit 15: Sage Group P/NTM Earnings"
  },
  {
    "figure_id": "F252",
    "report_id": "R043",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Netcompany P/NTM Earnings Exhibit 14: RELX P/NTM Earnings Exhibit 15: Sage Group P/NTM Earnings Exhibit 16: SAP P/NTM Earnings"
  },
  {
    "figure_id": "F253",
    "report_id": "R043",
    "label": "Exhibit 14",
    "context": "Exhibit 14: RELX P/NTM Earnings Exhibit 15: Sage Group P/NTM Earnings Exhibit 16: SAP P/NTM Earnings Exhibit 17: Temenos P/NTM Earnings"
  },
  {
    "figure_id": "F254",
    "report_id": "R043",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Sage Group P/NTM Earnings Exhibit 16: SAP P/NTM Earnings Exhibit 17: Temenos P/NTM Earnings Exhibit 18: Tieto P/NTM Earnings"
  },
  {
    "figure_id": "F255",
    "report_id": "R043",
    "label": "Exhibit 16",
    "context": "Exhibit 16: SAP P/NTM Earnings Exhibit 17: Temenos P/NTM Earnings Exhibit 18: Tieto P/NTM Earnings Exhibit 19: Wolters Kluwer P/NTM Earnings"
  },
  {
    "figure_id": "F256",
    "report_id": "R043",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Temenos P/NTM Earnings Exhibit 18: Tieto P/NTM Earnings Exhibit 19: Wolters Kluwer P/NTM Earnings ## Coverage Company Guidance"
  },
  {
    "figure_id": "F257",
    "report_id": "R043",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Tieto P/NTM Earnings Exhibit 19: Wolters Kluwer P/NTM Earnings ## Coverage Company Guidance Exhibit 20: Company Forward Guidance (1/2)"
  },
  {
    "figure_id": "F258",
    "report_id": "R043",
    "label": "Exhibit 22",
    "context": "## Disclosure Section The information and opinions in MS were prepared or are disseminated by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) and/or MS & Co. International plc, authorized by the Prudential Regulation Autho"
  },
  {
    "figure_id": "F259",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Micron's y/y revenue growth has rapidly accelerated in recent quarters ## TECHNOLOGY - SOFTWARE & SERVICES Europe"
  },
  {
    "figure_id": "F260",
    "report_id": "R044",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Informa historical NTM adj. P/E valuation (consensus) 3) SAP CEO: \"there is a chance that in 3-4 years there is actually no one developing software inside SAP any more\" (#Software, #SAP): Speaking to the Australian Fin"
  },
  {
    "figure_id": "F261",
    "report_id": "R044",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Key week ahead events Coverage Valuation vs. European Market Exhibit 4: European Software NTM P/E vs STOXX Europe 600 ## Long-Term Valuation Charts Exhibit 5: Amadeus P/NTM Earnings"
  },
  {
    "figure_id": "F262",
    "report_id": "R044",
    "label": "Exhibit 4",
    "context": "Exhibit 4: European Software NTM P/E vs STOXX Europe 600 ## Long-Term Valuation Charts Exhibit 5: Amadeus P/NTM Earnings Exhibit 6: Capgemini P/NTM Earnings Exhibit 7: Dassault Systemes P/NTM Earnings"
  },
  {
    "figure_id": "F263",
    "report_id": "R044",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Amadeus P/NTM Earnings Exhibit 6: Capgemini P/NTM Earnings Exhibit 7: Dassault Systemes P/NTM Earnings Exhibit 8: HBX Group International P/NTM Earnings"
  },
  {
    "figure_id": "F264",
    "report_id": "R044",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Capgemini P/NTM Earnings Exhibit 7: Dassault Systemes P/NTM Earnings Exhibit 8: HBX Group International P/NTM Earnings Exhibit 9: Indra P/NTM Earnings"
  },
  {
    "figure_id": "F265",
    "report_id": "R044",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Dassault Systemes P/NTM Earnings Exhibit 8: HBX Group International P/NTM Earnings Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings"
  },
  {
    "figure_id": "F266",
    "report_id": "R044",
    "label": "Exhibit 8",
    "context": "Exhibit 8: HBX Group International P/NTM Earnings Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings"
  },
  {
    "figure_id": "F267",
    "report_id": "R044",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings Exhibit 12: Nemetschek Group P/NTM Earnings"
  },
  {
    "figure_id": "F268",
    "report_id": "R044",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Indra P/NTM Earnings Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings Exhibit 12: Nemetschek Group P/NTM Earnings Exhibit 13: Netcompany P/NTM Earnings"
  },
  {
    "figure_id": "F269",
    "report_id": "R044",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Informa P/NTM Earnings Exhibit 11: IONOS P/NTM Earnings Exhibit 12: Nemetschek Group P/NTM Earnings Exhibit 13: Netcompany P/NTM Earnings Exhibit 14: RELX P/NTM Earnings"
  },
  {
    "figure_id": "F270",
    "report_id": "R044",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Nemetschek Group P/NTM Earnings Exhibit 13: Netcompany P/NTM Earnings Exhibit 14: RELX P/NTM Earnings Exhibit 15: Sage Group P/NTM Earnings"
  },
  {
    "figure_id": "F271",
    "report_id": "R044",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Netcompany P/NTM Earnings Exhibit 14: RELX P/NTM Earnings Exhibit 15: Sage Group P/NTM Earnings Exhibit 16: SAP P/NTM Earnings"
  },
  {
    "figure_id": "F272",
    "report_id": "R044",
    "label": "Exhibit 14",
    "context": "Exhibit 14: RELX P/NTM Earnings Exhibit 15: Sage Group P/NTM Earnings Exhibit 16: SAP P/NTM Earnings Exhibit 17: Temenos P/NTM Earnings"
  },
  {
    "figure_id": "F273",
    "report_id": "R044",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Sage Group P/NTM Earnings Exhibit 16: SAP P/NTM Earnings Exhibit 17: Temenos P/NTM Earnings Exhibit 18: Tieto P/NTM Earnings"
  },
  {
    "figure_id": "F274",
    "report_id": "R044",
    "label": "Exhibit 16",
    "context": "Exhibit 16: SAP P/NTM Earnings Exhibit 17: Temenos P/NTM Earnings Exhibit 18: Tieto P/NTM Earnings Exhibit 19: Wolters Kluwer P/NTM Earnings"
  },
  {
    "figure_id": "F275",
    "report_id": "R044",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Temenos P/NTM Earnings Exhibit 18: Tieto P/NTM Earnings Exhibit 19: Wolters Kluwer P/NTM Earnings ## Coverage Company Guidance"
  },
  {
    "figure_id": "F276",
    "report_id": "R044",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Tieto P/NTM Earnings Exhibit 19: Wolters Kluwer P/NTM Earnings ## Coverage Company Guidance Exhibit 20: Company Forward Guidance (1/2)"
  },
  {
    "figure_id": "F277",
    "report_id": "R044",
    "label": "Exhibit 22",
    "context": "## Disclosure Section The information and opinions in MS were prepared or are disseminated by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) and/or MS & Co. International plc, authorized by the Prudential Regulation Autho"
  },
  {
    "figure_id": "F278",
    "report_id": "R046",
    "label": "Exhibit 5",
    "context": "Exhibit 4: MLCC market share Exhibit 5: MLCC market share (CY25) ## Disclosure Section"
  },
  {
    "figure_id": "F279",
    "report_id": "R046",
    "label": "Exhibit 4",
    "context": "Exhibit 4: MLCC market share Exhibit 5: MLCC market share (CY25) ## Disclosure Section The information and opinions in MS were prepared by MS MUFG Securities Co., Ltd. and its affiliates (collectively, \"MS\"). For important disc"
  },
  {
    "figure_id": "F280",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "Ireland's infrastructure has been falling behind... Note: Other transport equipment and intangible assets are excluded due to large distortions in the Irish data. Grey lines show individual advanced euro area countries. ...and its current favorable demographic"
  },
  {
    "figure_id": "F281",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "## RECENT DEVELOPMENTS 2. Despite trade and geopolitical tensions and elevated uncertainty, the Irish economy has continued to grow strongly. After posting 4.8 percent growth in 2024, real GNI\\* (an appropriate measure of the Irish economy) $^{1}$ is estimated"
  },
  {
    "figure_id": "F282",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "## RECENT DEVELOPMENTS 2. Despite trade and geopolitical tensions and elevated uncertainty, the Irish economy has continued to grow strongly. After posting 4.8 percent growth in 2024, real GNI\\* (an appropriate measure of the Irish economy) $^{1}$ is estimated"
  },
  {
    "figure_id": "F283",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "2. Despite trade and geopolitical tensions and elevated uncertainty, the Irish economy has continued to grow strongly. After posting 4.8 percent growth in 2024, real GNI\\* (an appropriate measure of the Irish economy) $^{1}$ is estimated to have increased by a"
  },
  {
    "figure_id": "F284",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "Sources: Eurostat, Haver Analytics, and IMF staff calculations. Sources: Eurostat, Haver Analytics, and IMF staff calculations. ...the manufacturing PMI is signaling improvement. Figure 2. Ireland: Real Sector Developments (concluded) Sources: Markit, and IMF "
  },
  {
    "figure_id": "F285",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "Sources: Eurostat, Haver Analytics, and IMF staff calculations. ...the manufacturing PMI is signaling improvement. Figure 2. Ireland: Real Sector Developments (concluded) Sources: Markit, and IMF calculations. 3. Inflation remained close to 2 percent in 2025 b"
  },
  {
    "figure_id": "F286",
    "report_id": "R048",
    "label": "Figure 3",
    "context": "Sources: Markit, and IMF calculations. 3. Inflation remained close to 2 percent in 2025 but has accelerated since March 2026 due to higher energy prices. In 2025, the average headline inflation (HICP) stood at 2.1 percent and core inflation was marginally high"
  },
  {
    "figure_id": "F287",
    "report_id": "R048",
    "label": "Figure 3",
    "context": "3. Inflation remained close to 2 percent in 2025 but has accelerated since March 2026 due to higher energy prices. In 2025, the average headline inflation (HICP) stood at 2.1 percent and core inflation was marginally higher at 2.2 percent. Inflation rose notic"
  },
  {
    "figure_id": "F288",
    "report_id": "R048",
    "label": "Figure 3",
    "context": "...as did the energy and food price inflation. Sources: Eurostat, Haver Analytics, and IMF calculations. ## Figure 3. Ireland: Inflation (concluded) Sources: Eurostat, Haver Analytics, and IMF staff calculations. Sources: CSO; Eurostat; Haver Analytics; and IM"
  },
  {
    "figure_id": "F289",
    "report_id": "R048",
    "label": "Figure 3",
    "context": "Sources: Eurostat, Haver Analytics, and IMF calculations. ## Figure 3. Ireland: Inflation (concluded) Sources: Eurostat, Haver Analytics, and IMF staff calculations. Sources: CSO; Eurostat; Haver Analytics; and IMF staff calculations. ## 4. The labor market ex"
  },
  {
    "figure_id": "F290",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "Sources: CSO; Eurostat; Haver Analytics; and IMF staff calculations. ## 4. The labor market exhibits signs of easing. Employment growth slowed from 2.7 percent in 2024 to 2.2 percent in 2025, with declines recorded in some sectors, e.g., ICT and professional s"
  },
  {
    "figure_id": "F291",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "## 4. The labor market exhibits signs of easing. Employment growth slowed from 2.7 percent in 2024 to 2.2 percent in 2025, with declines recorded in some sectors, e.g., ICT and professional services. Vacancy rates were broadly unchanged overall, with higher va"
  },
  {
    "figure_id": "F292",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "Figure 4. Ireland: Labor Market ...and unemployment has edged up. Unemployment Rate Sources: Eurostat, Haver Analytics, and IMF calculations. Figure 4. Ireland: Labor Market (concluded) Real wage growth has slowed... Sources: CSO, Eurostat, Haver Analytics, an"
  },
  {
    "figure_id": "F293",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "Sources: Eurostat, Haver Analytics, and IMF calculations. Figure 4. Ireland: Labor Market (concluded) Real wage growth has slowed... Sources: CSO, Eurostat, Haver Analytics, and IMF calculations. The vacancy to unemployment ratio has declined... ...and job pos"
  },
  {
    "figure_id": "F294",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "Figure 4. Ireland: Labor Market (concluded) Real wage growth has slowed... Sources: CSO, Eurostat, Haver Analytics, and IMF calculations. The vacancy to unemployment ratio has declined... ...and job postings are trending down. 5. Robust corporate tax revenue c"
  },
  {
    "figure_id": "F295",
    "report_id": "R048",
    "label": "Figure 5",
    "context": "6. Bank credit has continued to strengthen on the back of robust mortgage loans and amid still-high house price growth. Interest rates on loans have been on a declining trend overall since 2024, reflecting the ECB's easing cycle, but lending rates to NFCs edge"
  },
  {
    "figure_id": "F296",
    "report_id": "R048",
    "label": "Figure 5",
    "context": "Lending rates are trending down... combination of factors, including steady income growth, increased housing supply, and house price dynamics, have underpinned the mortgage lending activity, with lending standards broadly unchanged. Residential property price "
  },
  {
    "figure_id": "F297",
    "report_id": "R048",
    "label": "Figure 5",
    "context": "Figure 5. Ireland: Credit Developments and Real Estate Prices Sources: CBI, and IMF staff calculations. Note: Credit only considers loans by banks to Irish Residents. Sources: CSO, Eurostat, Haver Analytics, and IMF staff calculations. Sources: CSO and IMF sta"
  },
  {
    "figure_id": "F298",
    "report_id": "R048",
    "label": "Figure 6",
    "context": "11. The headline fiscal balance is projected to remain in surplus during 2026–31. The new Medium-Term Fiscal and Structural Plan (MTFSP) projects an average annual revenue growth of about 6 percent during 2026–30, driven by increases in income taxes (including"
  },
  {
    "figure_id": "F299",
    "report_id": "R048",
    "label": "Figure 6",
    "context": "## Figure 6. Ireland: Fiscal Projections and Stances With excess CIT, the fiscal balance is projected to remain in surplus... ...and the near-term fiscal stance is moderately expansionary. 1/ Fiscal impulse is measured as the change in structural primary balan"
  },
  {
    "figure_id": "F300",
    "report_id": "R048",
    "label": "Figure 8",
    "context": "1/ Fiscal impulse is measured as the change in structural primary balance (SPB) as a percent of potential GDP. The SPB excludes excess CIT revenues and the one-off payment of €14 billion from the CJEU ruling. 12. The favorable outlook in the near to medium ter"
  },
  {
    "figure_id": "F301",
    "report_id": "R048",
    "label": "Figure 7",
    "context": "Ireland has a progressive PIT system... ...and has room to introduce additional PIT bands. reduced VAT rates, implying a significant VAT policy gap of nearly 35 percent. $^{8}$ The local property tax rates remain relatively low despite recent reforms, resultin"
  },
  {
    "figure_id": "F302",
    "report_id": "R048",
    "label": "Figure 7",
    "context": "...and has room to introduce additional PIT bands. reduced VAT rates, implying a significant VAT policy gap of nearly 35 percent. $^{8}$ The local property tax rates remain relatively low despite recent reforms, resulting in low recurrent revenues and a high r"
  },
  {
    "figure_id": "F303",
    "report_id": "R048",
    "label": "Figure 7",
    "context": "Figure 7. Ireland: PIT, VAT and Property Tax Structure Sources: Revenue Commissioners, and IMF staff calculations. Sources: Taxes in Europe database v4; and IMF staff calculations. Reduced VAT rates create a sizable VAT policy gap... Sources: European Commissi"
  },
  {
    "figure_id": "F304",
    "report_id": "R048",
    "label": "Figure 8",
    "context": "Sources: Taxes in Europe database v4; and IMF staff calculations. Reduced VAT rates create a sizable VAT policy gap... Sources: European Commission and IMF staff calculations. ...recurrent property tax revenue is low. \\- Aging and climate costs: While Ireland'"
  },
  {
    "figure_id": "F305",
    "report_id": "R048",
    "label": "Figure 8",
    "context": "\\- Aging and climate costs: While Ireland's current age structure is favorable, the European Commission projects the share of the old-age population to double from 2022 to 2070. Consequently, total age-related expenditures are projected to increase by 6 percen"
  },
  {
    "figure_id": "F306",
    "report_id": "R048",
    "label": "Figure 10",
    "context": "group and reached an agreement to sell its stake in PTSB. Capital positions of the domestic banks have strengthened further, benefitting also from the finalization of Basel III reforms, and are above the regulatory requirements. The 2025 EBA stress test confir"
  },
  {
    "figure_id": "F307",
    "report_id": "R048",
    "label": "Figure 10",
    "context": "7.7 percent in 2025Q4. Vulnerabilities, however, persist in certain portfolios, particularly related to leveraged finance to firms and the CRE sector. Asset quality should remain a key area of supervisory focus, given the macroeconomic risks, including from es"
  },
  {
    "figure_id": "F308",
    "report_id": "R048",
    "label": "Figure 10",
    "context": "Sources: CBI and IMF staff calculations. Sources: CBI, Haver Analytics, and IMF staff calculations. ## Figure 10. Ireland: Balance Sheets, Bank Profitability and Asset Quality (concluded) 23. Macroprudential policy settings remain appropriate. The CCyB rate is"
  },
  {
    "figure_id": "F309",
    "report_id": "R048",
    "label": "Figure 10",
    "context": "Sources: CBI, Haver Analytics, and IMF staff calculations. ## Figure 10. Ireland: Balance Sheets, Bank Profitability and Asset Quality (concluded) 23. Macroprudential policy settings remain appropriate. The CCyB rate is maintained at 1.5 percent, a level consi"
  },
  {
    "figure_id": "F310",
    "report_id": "R048",
    "label": "Figure 11",
    "context": "...and productivity in the construction sector is low. ## Figure 11. Ireland: Housing Market Challenges Housing investment has been subdued... Sources: Eurostat, CSO, Haver Analytics, and IMF staff calculations. Note: \\* percent of GNI\\*. ## 28. Sustained prod"
  },
  {
    "figure_id": "F311",
    "report_id": "R048",
    "label": "Figure 11",
    "context": "## Figure 11. Ireland: Housing Market Challenges Housing investment has been subdued... Sources: Eurostat, CSO, Haver Analytics, and IMF staff calculations. Note: \\* percent of GNI\\*. ## 28. Sustained productivity growth is closely linked to the availability o"
  },
  {
    "figure_id": "F312",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "3. The growth pattern observed in 2025 reflects the structural characteristics of the Irish economy, notably the dominant role of MNEs and the concentration of external activity in a small number of sectors, firms, and products. Because of the disproportionate"
  },
  {
    "figure_id": "F313",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "companies abroad through profit repatriation. However, it is a significant contributor to corporate tax revenue and swings in MNE value added affect the economy through the fiscal channel. This structure helps explain why sharp swings in exports and GDP—such a"
  },
  {
    "figure_id": "F314",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "Annex I. Figure 2. Ireland: Export Performance Sources: Haver Analytics and IMF staff calculations. Exports to the United States Exports to the European Union Sources: Haver Analytics and IMF staff calculations. Sources: Haver Analytics and IMF staff calculati"
  },
  {
    "figure_id": "F315",
    "report_id": "R048",
    "label": "Figure 1",
    "context": "## Annex V. Sovereign Risk and Debt Sustainability Framework Annex V. Figure 3. Ireland: Public Debt Structure Indicators Debt by Currency (Percent of GDP) Note: The perimeter shown is consolidated public sector. Public Debt by Holder (Percent of GDP) Note: Th"
  },
  {
    "figure_id": "F316",
    "report_id": "R048",
    "label": "Figure 3",
    "context": "Annex V. Figure 3. Ireland: Public Debt Structure Indicators Debt by Currency (Percent of GDP) Note: The perimeter shown is consolidated public sector. Public Debt by Holder (Percent of GDP) Note: The perimeter shown is general government. Public Debt by Gover"
  },
  {
    "figure_id": "F317",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "Public Debt by Governing Law, 2025 (Percent) Note: The perimeter shown is general government. Debt by Instruments (Percent of GDP) Public Debt by Maturity (Percent of GDP) Note: The perimeter shown is general government. Note: The perimeter shown is general go"
  },
  {
    "figure_id": "F318",
    "report_id": "R048",
    "label": "Figure 4",
    "context": "Note: The perimeter shown is general government. Contribution to Change in Public Debt Annex V. Figure 4. Ireland: Baseline Scenario (Percent of GDP unless indicated otherwise)"
  },
  {
    "figure_id": "F319",
    "report_id": "R048",
    "label": "Figure 6",
    "context": "(Percent of GDP) Annex V. Figure 6. Ireland: Realism of Baseline Assumptions Public Debt Creating Flows Bond Issuances (Bars, debt issuances (RHS, 3-Year Debt Reduction (Percent of GDP) %GDP); lines, avg marginal interest rates (LHS, percent))"
  },
  {
    "figure_id": "F320",
    "report_id": "R048",
    "label": "Figure 7",
    "context": "3/ Data cover annual observations from 1990 to 2019 for MAC advanced and emerging economies. Percent of sample on vertical axis. 4/ The Laubach (2009) rule is a linear rule assuming bond spreads increase by about 4 bps in response to a 1 ppt increase in the pr"
  },
  {
    "figure_id": "F321",
    "report_id": "R048",
    "label": "Figure 7",
    "context": "4/ The Laubach (2009) rule is a linear rule assuming bond spreads increase by about 4 bps in response to a 1 ppt increase in the projected debt-to-GDP ratio. Pension Financing Needs Total Benefits Paid Commentary: Currently, public expenditures on pensions in "
  },
  {
    "figure_id": "F322",
    "report_id": "R048",
    "label": "Figure 7",
    "context": "Pension Financing Needs Total Benefits Paid Commentary: Currently, public expenditures on pensions in Ireland are significantly below the EU averages, thanks to Ireland's relatively favorable age structure. However, according to the European Commission's 2024 "
  },
  {
    "figure_id": "F323",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "## C. Tariff and Trade Agreements: Re-Shaping Global Trade 8. Trade policy shocks affect Ireland primarily through trade reallocation rather than through large aggregate output effects. Consistent with standard trade theory, the tariff shock has negative globa"
  },
  {
    "figure_id": "F324",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "8. Trade policy shocks affect Ireland primarily through trade reallocation rather than through large aggregate output effects. Consistent with standard trade theory, the tariff shock has negative global effects in the model: world real output declines by 0.13 "
  },
  {
    "figure_id": "F325",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "Figure 1. Ireland: Real GDP and Price Index Impacts in Tariff and Trade Agreements Scenarios"
  },
  {
    "figure_id": "F326",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "12. Sectoral results show that the largest adjustments are concentrated in a small set of highly traded activities. Under the U.S. tariff scenario, several export-oriented sectors expand strongly in the U.S. market while contracting in other destinations, cons"
  },
  {
    "figure_id": "F327",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "12. Sectoral results show that the largest adjustments are concentrated in a small set of highly traded activities. Under the U.S. tariff scenario, several export-oriented sectors expand strongly in the U.S. market while contracting in other destinations, cons"
  },
  {
    "figure_id": "F328",
    "report_id": "R049",
    "label": "Figure 4",
    "context": "13. Sectoral reallocation of factors supports smooth adjustment. In the trade scenarios, sectors that expand under favorable market-access conditions absorb additional labor and capital, Figure 4. Ireland: Selected Sectoral Labor Movement in Tariff and Trade A"
  },
  {
    "figure_id": "F329",
    "report_id": "R049",
    "label": "Figure 5",
    "context": "## D. Artificial Intelligence and Productivity Gains 14. AI adoption scenarios reshape Ireland's production and trade structure by amplifying sector-specific productivity differentials. Productivity gains are concentrated in knowledge-intensive and digitally e"
  },
  {
    "figure_id": "F330",
    "report_id": "R049",
    "label": "Figure 5",
    "context": "15. AI-driven productivity gains generate sizable aggregate output effects in Ireland. Real GDP rises materially across the AI variants, ranging from 2.50 percent under the low-AI scenario to 6.89 percent under medium AI and 10.12 percent under high AI, reflec"
  },
  {
    "figure_id": "F331",
    "report_id": "R049",
    "label": "Figure 7",
    "context": "## 17. AI adoption triggers differentiated sectoral responses in real output and exports, reflecting the uneven distribution of AI-related efficiency improvements. Sectors that are more knowledge-, data-, and technology-intensive experience the largest gains, "
  },
  {
    "figure_id": "F332",
    "report_id": "R049",
    "label": "Figure 8",
    "context": "Figure 8. Ireland: Renewable Share in Electricity Productions and CO2 Emission in AI-Driven Productivity Gains Scenarios"
  },
  {
    "figure_id": "F333",
    "report_id": "R049",
    "label": "Figure 8",
    "context": "Figure 8. Ireland: Renewable Share in Electricity Productions and CO2 Emission in AI-Driven Productivity Gains Scenarios"
  },
  {
    "figure_id": "F334",
    "report_id": "R049",
    "label": "Figure 9",
    "context": "## 20. The aggregate shifts are underpinned by substantial sectoral labor reallocation, as AI raises labor demand unevenly across activities. Employment contracts in some sectors—including pharmaceuticals, where labor declines by about 2 percent under low AI a"
  },
  {
    "figure_id": "F335",
    "report_id": "R049",
    "label": "Figure 9",
    "context": "pharmaceuticals, where labor declines by about 2 percent under low AI and by over 7 percent under high AI—as productivity gains reduce labor requirements in highly capital-intensive production (Figure 9). At the same time, labor shifts toward fast-growing acti"
  },
  {
    "figure_id": "F336",
    "report_id": "R049",
    "label": "Figure 10",
    "context": "21. Carbon pricing scenarios illustrate how policy interventions can reshape Ireland's growth, trade, and energy outcomes by internalizing emissions costs, both on a standalone basis and when combined with AI-driven productivity gains. In the first three scena"
  },
  {
    "figure_id": "F337",
    "report_id": "R049",
    "label": "Figure 10",
    "context": "22. Real GDP and price responses reflect the interaction between productivity gains and carbon costs. When combined with carbon pricing, AI adoption continues to yield sizable output gains: real GDP increases range from about 2.43 to 9.79 percent, slightly bel"
  },
  {
    "figure_id": "F338",
    "report_id": "R049",
    "label": "Figure 12",
    "context": "Figure 12. Ireland: Real Export and Export Price Impacts in Carbon Pricing Policy Scenarios"
  },
  {
    "figure_id": "F339",
    "report_id": "R049",
    "label": "Figure 12",
    "context": "Figure 12. Ireland: Real Export and Export Price Impacts in Carbon Pricing Policy Scenarios"
  },
  {
    "figure_id": "F340",
    "report_id": "R049",
    "label": "Figure 13",
    "context": "Figure 13. Ireland: Selected Sectoral Real Output and Real Export Impacts in Carbon Pricing Policy Scenarios ## 25. These sectoral adjustments are reflected in factor incomes and labor reallocation, driven by changes in relative profitability across activities"
  },
  {
    "figure_id": "F341",
    "report_id": "R049",
    "label": "Figure 13",
    "context": "Figure 13. Ireland: Selected Sectoral Real Output and Real Export Impacts in Carbon Pricing Policy Scenarios ## 25. These sectoral adjustments are reflected in factor incomes and labor reallocation, driven by changes in relative profitability across activities"
  },
  {
    "figure_id": "F342",
    "report_id": "R049",
    "label": "Figure 14",
    "context": "## 25. These sectoral adjustments are reflected in factor incomes and labor reallocation, driven by changes in relative profitability across activities. When carbon pricing is combined Figure 14. Ireland: Selected Sectoral Labor Movement in Carbon Pricing Poli"
  },
  {
    "figure_id": "F343",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "29. Carbon pricing policy can play a central role in ensuring that productivity-driven expansion does not translate into persistently higher emissions or an unsustainable energy mix. The results underscore the importance of continuing investment in renewable e"
  },
  {
    "figure_id": "F344",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "Annex I. Figure 1. Ireland: Nesting Structure in Non-Fossil-Fuel Production Annex I. Figure 2. Ireland: Nesting Structure in Fossil-Fuel Production ## Annex I. Figure 3. Ireland: Export Structure Domestic (D) Export (E)"
  },
  {
    "figure_id": "F345",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "## Annex I. Figure 3. Ireland: Export Structure Domestic (D) Export (E) Output (Y) Annex I. Figure 4. Ireland: Intermediate Input Structure Intermediate Input ( $M_{n}$ )"
  },
  {
    "figure_id": "F346",
    "report_id": "R049",
    "label": "Figure 4",
    "context": "Export (E) Output (Y) Annex I. Figure 4. Ireland: Intermediate Input Structure Intermediate Input ( $M_{n}$ ) ## Annex II. Sectoral Mapping"
  },
  {
    "figure_id": "F347",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "3. Moreover, considerable challenges including infrastructure and governance gaps, limited economic diversification, together with severe climate-related natural disasters hinder more sustainable and inclusive growth. $^{3}$ Despite recent progress, gaps in hu"
  },
  {
    "figure_id": "F348",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Text Figure 2. Estimates for Additional Spending to Achieve SDGs in 2030 Text Figure 1. Social Spending (Percent of GDP) 4. Against this backdrop, the authorities are requesting successor ECF/EFF arrangements to provide temporary financing, support macroeconom"
  },
  {
    "figure_id": "F349",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "4. Against this backdrop, the authorities are requesting successor ECF/EFF arrangements to provide temporary financing, support macroeconomic adjustment, and advance their development and institutional reform agenda. Fund financing will help meet actual and pr"
  },
  {
    "figure_id": "F350",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "Sources: Mauritanian authorities; and IMF staff calculations. beverages inflation continues to drive the surge in inflation. Tobacco products also contributed to the increase in inflation, followed by housing. $^{6}$ 6. The external position improved markedly,"
  },
  {
    "figure_id": "F351",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "7. The overall fiscal deficit narrowed, driven by stronger revenue performance while spending remained broadly contained. The deficit declined from 1.4 percent of GDP in 2024 to 0.3 percent of GDP in 2025. End-December 2025 revenues (including grants) reached "
  },
  {
    "figure_id": "F352",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "Text Figure 5. Ouguiya per US Dollar—Official and Parallel Market Sources: Mauritanian authorities; and IMF staff calculations. Text Figure 6. Exchange Rates Sources: Mauritanian authorities; and IMF staff calculations. 10. FX market activity has expanded sign"
  },
  {
    "figure_id": "F353",
    "report_id": "R050",
    "label": "Figure 6",
    "context": "Text Figure 6. Exchange Rates Sources: Mauritanian authorities; and IMF staff calculations. 10. FX market activity has expanded significantly, with both total volumes and interbank trading increasing markedly. Total FX market turnover rose from US\\$2.4 billion"
  },
  {
    "figure_id": "F354",
    "report_id": "R050",
    "label": "Figure 7",
    "context": "\\- Tax policy: Efforts are underway to reform the VAT, $^{17}$ assess the public sector wage structure to determine the effective tax base and to tax all earned income according to the law; and strengthen the capacities and resources of the Tax Policy Unit (TP"
  },
  {
    "figure_id": "F355",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "## 66. Staff takes note of the authorities' intention to cancel the current ECF/EFF arrangements, and supports their request for the new 42-month ECF/EFF arrangements, as well as the completion of the fifth review under the RSF. All RMs under this review have "
  },
  {
    "figure_id": "F356",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "## Figure 1. Mauritania: Real Sector Developments, 2014–2026 Real GDP growth has slowed in 2025... ...non-extractive GDP also slowed as growth in the financial sector moderated and growth in fisheries slowed. Non-Extractive GDP (Contribution to growth, in perc"
  },
  {
    "figure_id": "F357",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "The non-extractive sector remained predominant. Nominal GDP (In billions of MRU) ... while the extractives sector saw a significant drop in real terms on a decrease in gold activity. Inflation has increased, driven by increases in the price of food and beverag"
  },
  {
    "figure_id": "F358",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Nominal GDP (In billions of MRU) ... while the extractives sector saw a significant drop in real terms on a decrease in gold activity. Inflation has increased, driven by increases in the price of food and beverages as demand from neighboring Mali increases. So"
  },
  {
    "figure_id": "F359",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Inflation has increased, driven by increases in the price of food and beverages as demand from neighboring Mali increases. Sources: Mauritanian authorities; and IMF staff estimates and projections. ## Figure 2. Mauritania: External Sector Developments, 2014–20"
  },
  {
    "figure_id": "F360",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Sources: Mauritanian authorities; and IMF staff estimates and projections. ## Figure 2. Mauritania: External Sector Developments, 2014–2026 Terms of trade improved further in 2025 as gold prices continued to rise. Export performance was supported by higher gol"
  },
  {
    "figure_id": "F361",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "The financial account balance decreased amid lower FDI and continued outflows from commodity exporters. Financial Account (In percent of GDP) Official reserves remained above the adequacy threshold... BCM's FX interventions continued to decline as FX volumes t"
  },
  {
    "figure_id": "F362",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "(In percent of GDP) Official reserves remained above the adequacy threshold... BCM's FX interventions continued to decline as FX volumes traded directly in the FX interbank market increased. Sources: Mauritanian authorities; and IMF staff estimates and project"
  },
  {
    "figure_id": "F363",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "BCM's FX interventions continued to decline as FX volumes traded directly in the FX interbank market increased. Sources: Mauritanian authorities; and IMF staff estimates and projections. Figure 3. Mauritania: Fiscal Sector Developments, 2014–2025 (Percent of G"
  },
  {
    "figure_id": "F364",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "Figure 3. Mauritania: Fiscal Sector Developments, 2014–2025 (Percent of GDP, unless otherwise indicated) The fiscal balance improved in 2025 with the implementation of the fiscal anchor. ...and 2025 execution of public investment was higher, driven by domestic"
  },
  {
    "figure_id": "F365",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "While current expenditures contracted further. Current Expenditures The fiscal deficit was financed mainly through domestic securities issuance... ...while public sector debt relative to GDP decreased. Debt Stock and Debt Service Sources: Mauritanian authoriti"
  },
  {
    "figure_id": "F366",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "Current Expenditures The fiscal deficit was financed mainly through domestic securities issuance... ...while public sector debt relative to GDP decreased. Debt Stock and Debt Service Sources: Mauritanian authorities; and IMF staff estimates and projections. ##"
  },
  {
    "figure_id": "F367",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "...while public sector debt relative to GDP decreased. Debt Stock and Debt Service Sources: Mauritanian authorities; and IMF staff estimates and projections. ## Figure 4. Mauritania: Monetary Sector Indicators, 2016–2026 Private credit growth has been accelera"
  },
  {
    "figure_id": "F368",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "## Figure 4. Mauritania: Monetary Sector Indicators, 2016–2026 Private credit growth has been accelerating... BCM continued to keep monetary conditions tight... ...credit to the government has also increased... Commercial Banks' Credit to the Economy ...while "
  },
  {
    "figure_id": "F369",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "...while reserve money grew in tandem with the growth in the economy ... ...with the T-bills rate reflecting more issuance for banks at market-determined rates. Key Interest Rates (In percent) Sources: Mauritanian authorities, and IMF staff calculations. ## Fi"
  },
  {
    "figure_id": "F370",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "...with the T-bills rate reflecting more issuance for banks at market-determined rates. Key Interest Rates (In percent) Sources: Mauritanian authorities, and IMF staff calculations. ## Figure 5. Mauritania: Financial Sector Indicators, 2017–2025 (In percent)"
  },
  {
    "figure_id": "F371",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "## Figure 5. Mauritania: Financial Sector Indicators, 2017–2025 (In percent) Capital Adequacy Ratio Asset quality is weaker than in some peers ... Non-Performing Loans to Total Loans ...with an uptick in NPLs in the last year, which later stabilized... Provisi"
  },
  {
    "figure_id": "F372",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "\\- Non-PPG external debt broadly remained unchanged at 7.1 percent of GDP. The decline in the GTA-related loan and SNIM's non-guaranteed debt as a share of GDP was offset by the increase in external borrowing by commercial banks. PPG External Debt by Debtor (I"
  },
  {
    "figure_id": "F373",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Sources: Mauritanian authorities and IMF staff estimates. Notes: Excluding drawn SDR allocation. 8. Official non-Paris Club bilateral and multilateral creditors other than IMF and IDA represented 74.6 percent of PPG external debt at end-2025. This is 2.3 perce"
  },
  {
    "figure_id": "F374",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "21. Mauritania's CI calculation is weighed down by large externally financed extractive sector imports, which reduce the import coverage of reserves. The large scale of the offshore gas project and the expansion of the privately owned gold mine complex have ge"
  },
  {
    "figure_id": "F375",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "growth and development strategy and continue to make progress in implementing the policies needed to achieve them. ## AUTHORITIES' VIEWS 32. The authorities agreed with staff's assessment that Mauritania's risk of external debt distress remain moderate. They e"
  },
  {
    "figure_id": "F376",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "## AUTHORITIES' VIEWS 32. The authorities agreed with staff's assessment that Mauritania's risk of external debt distress remain moderate. They endorsed the IMF staff's recommendation that maintaining this moderate level of risk is essential to preserving the "
  },
  {
    "figure_id": "F377",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "32. The authorities agreed with staff's assessment that Mauritania's risk of external debt distress remain moderate. They endorsed the IMF staff's recommendation that maintaining this moderate level of risk is essential to preserving the country's macroeconomi"
  },
  {
    "figure_id": "F378",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 1. Mauritania: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026–2036 Note: \"Yes\" indicates any change to the size or interactions of the default settings for the stress tests. \"n.a.\" indicates that the stress "
  },
  {
    "figure_id": "F379",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Note: \"Yes\" indicates any change to the size or interactions of the default settings for the stress tests. \"n.a.\" indicates that the stress test does not apply. \\* Note: All the additional financing needs generated by the shocks under the stress tests are assu"
  },
  {
    "figure_id": "F380",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections. ## Sources: Country aut"
  },
  {
    "figure_id": "F381",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "1/ The most extreme stress test is the test that yields the highest ratio in or before 2036. The stress test with a one-off breach is also presented (if any), while the one-off breach is deemed away for mechanical signals. When a stress test with a one-off bre"
  },
  {
    "figure_id": "F382",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Sources: Country authorities; and staff estimates and projections. Figure 2. Mauritania: Indicators of Public Debt Under Alternative Scenarios, 2026–2036 PV of Debt-to-Revenue Ratio Debt Service-to-Revenue Ratio Baseline TOTAL public debt benchmark Most extrem"
  },
  {
    "figure_id": "F383",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "3/ Given the relatively low private external debt for average low-income countries, a ppt change in PPG external debt should ## Figure 3. Mauritania: Drivers of Debt Dynamics – Baseline Scenario Gross Nominal PPG External Debt (in percent of GDP; DSA vintages)"
  },
  {
    "figure_id": "F384",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "Gross Nominal Public Debt (in percent of GDP; DSA vintages) Debt-Creating Flows (percent of GDP) Unexpected Changes in Debt 1/ (past 5 years, percent of GDP) 1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs"
  },
  {
    "figure_id": "F385",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "2/ Distribution across LICs for which LIC DSAs were produced. be largely explained by the drivers of the external debt dynamics equation. ## Figure 4. Mauritania: Realism Tools 3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-"
  },
  {
    "figure_id": "F386",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "## Figure 4. Mauritania: Realism Tools 3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is f"
  },
  {
    "figure_id": "F387",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is found on the horizontal axis; the percent of sample is found on the vertical axis. Fiscal Adjustment and"
  },
  {
    "figure_id": "F388",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "1/ Bars refer to annual projected fiscal adjustment (right-hand scale) and lines show possible real GDP growth paths under different fiscal multipliers (left-hand side scale). Public and Private Investment Rates 1/ (Percent of GDP) 1/ The gap for either variab"
  },
  {
    "figure_id": "F389",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "1/ The gap for either variable between the previous and the current DSA is due to a reassessment of projections in light of new information. Contribution to Real GDP Growth (Percent, 5-year average) Figure 5. Mauritania: Qualification of the Moderate Category,"
  },
  {
    "figure_id": "F390",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "1/ The gap for either variable between the previous and the current DSA is due to a reassessment of projections in light of new information. Contribution to Real GDP Growth (Percent, 5-year average) Figure 5. Mauritania: Qualification of the Moderate Category,"
  },
  {
    "figure_id": "F391",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "Figure 5. Mauritania: Qualification of the Moderate Category, 2026–2036 Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and "
  },
  {
    "figure_id": "F392",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "Figure 5. Mauritania: Qualification of the Moderate Category, 2026–2036 Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and "
  },
  {
    "figure_id": "F393",
    "report_id": "R050",
    "label": "Figure 6",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and debt service/revenue thresholds, x is 12 percent and y is 35 percent. Do"
  },
  {
    "figure_id": "F394",
    "report_id": "R050",
    "label": "Figure 6",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and debt service/revenue thresholds, x is 12 percent and y is 35 percent. Do"
  },
  {
    "figure_id": "F395",
    "report_id": "R050",
    "label": "Figure 6",
    "context": "Domestic Debt Service-to-Revenues incl. grants Figure 6. Mauritania: Indicators of Domestic Public Debt, 2021–2036 (Percent) Historical realizations Median of average projected values over the first five years of the forecast period across countries using the "
  },
  {
    "figure_id": "F396",
    "report_id": "R050",
    "label": "Figure 6",
    "context": "Domestic Debt Service-to-Revenues incl. grants Figure 6. Mauritania: Indicators of Domestic Public Debt, 2021–2036 (Percent) Historical realizations Median of average projected values over the first five years of the forecast period across countries using the "
  },
  {
    "figure_id": "F397",
    "report_id": "R051",
    "label": "Figure 1",
    "context": "## A. Introduction 1. House prices in Spain have been rising over the past decade, with a sharp increase since the COVID-19 pandemic. After the major correction that followed the global financial crisis (GFC), the housing market stabilized and gradually recove"
  },
  {
    "figure_id": "F398",
    "report_id": "R051",
    "label": "Figure 1",
    "context": "1. House prices in Spain have been rising over the past decade, with a sharp increase since the COVID-19 pandemic. After the major correction that followed the global financial crisis (GFC), the housing market stabilized and gradually recovered, but prices hav"
  },
  {
    "figure_id": "F399",
    "report_id": "R051",
    "label": "Figure 2",
    "context": "7. Another important complementarity to be considered is with prevailing capital-based measures. In Spain, two key measures are currently in place: the countercyclical capital buffer (CCyB), which has been set at 1 percent, effective October 2026, and the capi"
  },
  {
    "figure_id": "F400",
    "report_id": "R051",
    "label": "Figure 3",
    "context": "where i, r, b, t index loans, provinces, banks, and origination quarters. $LS^{1}$ is a dummy that takes the value one for loans with LTV above 80 percent, while $LS^{j}$ is an income-based lending-standard 20. In a second step, the baseline model is augmented"
  },
  {
    "figure_id": "F401",
    "report_id": "R051",
    "label": "Figure 3",
    "context": "20. In a second step, the baseline model is augmented with an interaction between each lending-standard dummy and the originating bank's capital ratio at the time of issuance. This extension assesses whether lender capitalization affects the default risk assoc"
  },
  {
    "figure_id": "F402",
    "report_id": "R051",
    "label": "Figure 3",
    "context": "Marginal Impact of Each indicator, Entered Jointly (Percentage points) Sources: European DataWarehouse and authors' calculations. Note: The chart reports the estimated difference in delinquency probability, in percentage points, between loans exceeding each th"
  },
  {
    "figure_id": "F403",
    "report_id": "R051",
    "label": "Figure 5",
    "context": "26. Borrower leverage and debt service burdens in new originations have risen in recent years (Figure 5). Although households have deleveraged on average since the pandemic—with the average LTI ratio for mortgage loans peaking at 4.9 in 2020Q2 and declining to"
  },
  {
    "figure_id": "F404",
    "report_id": "R051",
    "label": "Figure 5",
    "context": "## Figure 5. Characteristics of Spanish Mortgage Portfolio by Vintage Legacy exposures remain significant, with a material portion of outstanding loans that were originated during the 2005–06 housing boom. Mortgages have historically been predominantly issued "
  },
  {
    "figure_id": "F405",
    "report_id": "R051",
    "label": "Figure 5",
    "context": "Legacy exposures remain significant, with a material portion of outstanding loans that were originated during the 2005–06 housing boom. Mortgages have historically been predominantly issued at floating rates, although the share of fixed-rate loans has increase"
  },
  {
    "figure_id": "F406",
    "report_id": "R051",
    "label": "Figure 5",
    "context": "Mortgages have historically been predominantly issued at floating rates, although the share of fixed-rate loans has increased following the 2022 ECB hiking cycle. High-risk lending has risen, with recent increases in both high-LTV... ...and high-LTI mortgage s"
  },
  {
    "figure_id": "F407",
    "report_id": "R051",
    "label": "Figure 5",
    "context": "...and high-LTI mortgage segments. Figure 5. Characteristics of Spanish Mortgage Portfolio by Vintage (Concluded) Borrowers' repayment capacity has weakened since 2018... Sources: Bank of Spain and IMF staff calculations. ... and this deterioration is evident "
  },
  {
    "figure_id": "F408",
    "report_id": "R051",
    "label": "Figure 5",
    "context": "Figure 5. Characteristics of Spanish Mortgage Portfolio by Vintage (Concluded) Borrowers' repayment capacity has weakened since 2018... Sources: Bank of Spain and IMF staff calculations. ... and this deterioration is evident even among high-LTV borrowers. 27. "
  },
  {
    "figure_id": "F409",
    "report_id": "R051",
    "label": "Figure 6",
    "context": "sensitivity of financial distress to the initial DSTI ratio, and the Spanish internal-rating based (IRB) banks' 2024Q4 reported default rates for demographic factors. $^{12}$ Calibrated on this basis, the model successfully replicates Spanish IRB banks' report"
  },
  {
    "figure_id": "F410",
    "report_id": "R051",
    "label": "Figure 7",
    "context": "where the numerator of the first term is an indicator function equal to 1 if equation (2) equals 1 and $\\Pr(FD_{i,t})$ is the (scalar, continuous) probability of financial distress (from equation 1), $PD_{i,t}$ is then the bucket's probability of default. The "
  },
  {
    "figure_id": "F411",
    "report_id": "R051",
    "label": "Figure 7",
    "context": "Figure 7. Stress Test Results Annualized loss rates in the outstanding portfolio could rise from about 30 bps under the baseline to 150 bps in the adverse scenario... ....with the most recent vintages appearing particularly vulnerable—loss rates for these coho"
  },
  {
    "figure_id": "F412",
    "report_id": "R051",
    "label": "Figure 7",
    "context": "$$ L G D _ {i, t} = N P V \\big (L _ {i, t}, r _ {t} ^ {t y p e, M}, r _ {t} ^ {f}, T _ {t, s} \\big) - (1 - \\delta) \\times \\frac {\\widetilde {P _ {\\iota , t + n}}}{\\left(1 + r _ {t} ^ {f} + s p r e a d\\right) ^ {n}}\\tag{4} $$ 36. While Spanish banks appear broa"
  },
  {
    "figure_id": "F413",
    "report_id": "R051",
    "label": "Figure 9",
    "context": "37. Losses are heavily concentrated in recent vintages, underscoring the importance of acting pre-emptively—before lending standards further loosen significantly—to mitigate risks to the mortgage portfolio. Mortgages originated during 2025Q3-2027Q2 would face "
  },
  {
    "figure_id": "F414",
    "report_id": "R052",
    "label": "Figure 1",
    "context": "The transposition of the EU economic governance framework to national legislation provides an opportunity to reform the subnational fiscal rule, especially with regard to its regional component. While compliance by autonomous communities has improved in the la"
  },
  {
    "figure_id": "F415",
    "report_id": "R052",
    "label": "Figure 2",
    "context": "8. Several studies have also examined the historical track record of compliance with the subnational fiscal rule and the implications for fiscal policy. Agrimón and Hernández de Cos (2012) examine an earlier version of the national fiscal rule, in place betwee"
  },
  {
    "figure_id": "F416",
    "report_id": "R052",
    "label": "Figure 3",
    "context": "Note: The left plot reports average spending as a share of GDP over 2022–2024. The right plot reports the average composition of spending by autonomous communities in different programs by its economic classification over 2022–2024. 10. Autonomous communities'"
  },
  {
    "figure_id": "F417",
    "report_id": "R052",
    "label": "Figure 3",
    "context": "Sources: IGAE, INE, and IMF staff calculations. Note: Net transfers are computed as transfers (current and capital) from other public sector entities minus transfers to other public sector entities (current and capital) minus 50 percent of the central governme"
  },
  {
    "figure_id": "F418",
    "report_id": "R052",
    "label": "Figure 3",
    "context": "Sources: IGAE, INE, and IMF staff calculations. revenues (known as liquidaciones)—which had fallen due to the economic crisis, also contracted sharply and persistently. This led to a long-lasting slump in autonomous communities' revenues, which recovered their"
  },
  {
    "figure_id": "F419",
    "report_id": "R052",
    "label": "Figure 6",
    "context": "Note: The grey lines report the interest spending in percent of GDP (left plot) and the effective interest rate on debt (right plot) of individual autonomous communities. The black lines represent the respective variables for the consolidated regional governme"
  },
  {
    "figure_id": "F420",
    "report_id": "R052",
    "label": "Figure 7",
    "context": "$$ where Expenditure and GDP are expressed in constant 2019 prices. For both series, the cyclical component is constructed by extracting the trend of the natural logarithm through a Hodrick-Prescott filter, using a smoothing weight of 100. The vector $X_{t}$ r"
  },
  {
    "figure_id": "F421",
    "report_id": "R052",
    "label": "Figure 6",
    "context": "autocorrelation in the dependent variable. $^{[11]}$ Spending has strong persistence, as the estimated coefficient on the lagged value t-1 is around 0.7 for all three expenditure definitions. Nevertheless, while the coefficient on the output gap is about half "
  },
  {
    "figure_id": "F422",
    "report_id": "R052",
    "label": "Figure 8",
    "context": "autocorrelation in the dependent variable. $^{[11]}$ Spending has strong persistence, as the estimated coefficient on the lagged value t-1 is around 0.7 for all three expenditure definitions. Nevertheless, while the coefficient on the output gap is about half "
  },
  {
    "figure_id": "F423",
    "report_id": "R052",
    "label": "Figure 9",
    "context": "Note: The plots report the estimated coefficients and 95 percent confidence intervals from linear regressions of the cyclical component of public spending on health and education on the output gap for (i) Spain, (ii) Spain's autonomous communities, (iii) Italy"
  },
  {
    "figure_id": "F424",
    "report_id": "R052",
    "label": "Figure 10",
    "context": "where the coefficient of interest is $\\beta$ . Higher values of $\\beta$ reflect a stronger reaction of the primary balance to the debt level and thus a larger weight put on debt stabilization in the conduct of fiscal policy. As discussed below, the estimated v"
  },
  {
    "figure_id": "F425",
    "report_id": "R052",
    "label": "Figure 11",
    "context": "equal to 1.7 percent, in line with staff's medium-term projection for Spain. For most communities, real borrowing rates in line with those faced by Spain's central government prior to the pandemic would imply stationarity. However, the debt dynamics of 6 commu"
  },
  {
    "figure_id": "F426",
    "report_id": "R052",
    "label": "Figure 11",
    "context": "equal to 1.7 percent, in line with staff's medium-term projection for Spain. For most communities, real borrowing rates in line with those faced by Spain's central government prior to the pandemic would imply stationarity. However, the debt dynamics of 6 commu"
  },
  {
    "figure_id": "F427",
    "report_id": "R052",
    "label": "Figure 12",
    "context": "30. Historical compliance with fiscal targets has been mixed. Recent analysis by AlReF (2025) on the fulfillment of fiscal targets finds that over 2013–2019 a substantial share of communities in each year did not comply with either the deficit or expenditure t"
  },
  {
    "figure_id": "F428",
    "report_id": "R052",
    "label": "Figure 12",
    "context": "31. Figure 12 visually corroborates this assessment. In the top left panel, the deficit rule had limited compliance in the version in force between 2008–2012, when it was the sole fiscal target for autonomous communities. In some years, no community reached th"
  },
  {
    "figure_id": "F429",
    "report_id": "R052",
    "label": "Figure 12",
    "context": "Sources: Ministry of Finance and IMF staff calculations. Figure 12. Fiscal Rule Targets and Outcomes of Autonomous Communities Debt: Deviations from Individual Objectives (Percent of GDP) - Only Deficit Target Met Figure 13. Deficit and Spending Growth Targets"
  },
  {
    "figure_id": "F430",
    "report_id": "R052",
    "label": "Figure 13",
    "context": "Debt: Deviations from Individual Objectives (Percent of GDP) - Only Deficit Target Met Figure 13. Deficit and Spending Growth Targets of Autonomous Communities by Year (Percent of GDP, Percent) Sources: Ministry of Finance and IMF staff calculations. Note: The"
  },
  {
    "figure_id": "F431",
    "report_id": "R052",
    "label": "Figure 2",
    "context": "Oates, W. E. (1999). \"An essay on fiscal federalism.\" Journal of Economic Literature, 37(3), 1120–1149. Organisation for Economic Co-operation and Development. (2024). Going granular with regional and municipal fiscal data: OECD and EU countries. Paris: OECD R"
  },
  {
    "figure_id": "F432",
    "report_id": "R052",
    "label": "Figure 2",
    "context": "Pérez, J. J., & Prieto, R. (2015). \"Risk factors and the maturity of subnational debt: An empirical investigation for the case of Spain.\" Public Finance Review, 43(6), 786–815. Sources: Ministry of Finance and IMF staff calculations. Note: Series from budget e"
  },
  {
    "figure_id": "F433",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "## Just over Half of Principals with ASPs Agreed That the Programming Aligned Academically to School-Day Instruction We first asked principals whether after-school programming is available to students at their school and, if so, where it occurs (i.e., off-site"
  },
  {
    "figure_id": "F434",
    "report_id": "R054",
    "label": "Figure 3",
    "context": "## Principals Reporting the Availability of School- or District-Provided After-School Programming Were More Likely to Report Academic Alignment To determine whether academic alignment was related to (1) where an ASP occurs or (2) who provides the ASP, we explo"
  },
  {
    "figure_id": "F435",
    "report_id": "R054",
    "label": "FIGURE 3",
    "context": "On one end of the spectrum, about one-fifth of principals reported that there were no efforts to align learning occurring during the school day and in ASPs. In most of these cases, principals said that their ASPs were not academic in nature. Notably, three-fou"
  },
  {
    "figure_id": "F436",
    "report_id": "R054",
    "label": "FIGURE 4",
    "context": "FIGURE 4 Percentage of principals Illustrative Examples of Degrees of Academic Alignment Between Schools and Their ASPs in their closed-ended survey response $^{3}$ —sometimes noted that the organizations running their ASPs had their own curricula and activiti"
  },
  {
    "figure_id": "F437",
    "report_id": "R054",
    "label": "Figure 5",
    "context": "## ASPs Deliver Academic Content Through Tutoring, Enrichment Activities, and Homework Help Sessions, Although the Extent of Alignment Varies Within and Across These Approaches Principals' responses suggest that there are several vehicles through which ASPs ca"
  },
  {
    "figure_id": "F438",
    "report_id": "R054",
    "label": "Figure 6",
    "context": "Homework help sessions, cited by about one-fifth of responding principals, appeared to be a weak academic alignment strategy. Like tutoring, principals described homework help as inherently academic. However, principals generally described this after-school su"
  },
  {
    "figure_id": "F439",
    "report_id": "R054",
    "label": "Figure 8",
    "context": "## Sharing Student Data with ASPs Facilitates Stronger Academic Alignment Principals' responses also suggest that sharing data across school and ASP settings can support academic alignment (Figure 8). About 50 principals said that their schools shared data gen"
  },
  {
    "figure_id": "F440",
    "report_id": "R054",
    "label": "Figure 9",
    "context": "## Sharing student data to inform after-school programming \"A system is in place for teachers and after-school providers to easily share information about student performance and areas of need. . . . After an in-class assessment, the classroom teacher shares t"
  },
  {
    "figure_id": "F441",
    "report_id": "R055",
    "label": "Exhibit 1",
    "context": "The next competitive separation will not come from adding more solutions, nor from building more sophisticated models. It will come from applying AI more deeply to the core commercial initiatives that build sustainable advantage: faster innovation, higher-fide"
  },
  {
    "figure_id": "F442",
    "report_id": "R055",
    "label": "Exhibit 1",
    "context": "AI's impact is expanding across the demand value chain. CPG companies and retailers have long used analytics and machine learning in areas such as product recommendations, pricing, and demand forecasting. What has changed is the range of work that AI can now a"
  },
  {
    "figure_id": "F443",
    "report_id": "R055",
    "label": "Exhibit 2",
    "context": "So far, companies have moved fastest where the economics are clearest. In CPG, that movement has occurred in demand and supply forecasting and revenue growth management optimization. Retailers have advanced furthest in how they manage availability, forecasting"
  },
  {
    "figure_id": "F444",
    "report_id": "R055",
    "label": "Exhibit 2",
    "context": "So far, companies have moved fastest where the economics are clearest. In CPG, that movement has occurred in demand and supply forecasting and revenue growth management optimization. Retailers have advanced furthest in how they manage availability, forecasting"
  },
  {
    "figure_id": "F445",
    "report_id": "R055",
    "label": "Exhibit 3",
    "context": "For the leaders, the value pool is material and likely to grow. BCG experience with clients in scaling individual initiatives suggests that scaling the full set of relevant AI initiatives across the demand value chain can deliver 220 to 350 basis points of cum"
  },
  {
    "figure_id": "F446",
    "report_id": "R055",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 ## Potential Value Today Total prize at scale today Note: Numbers may not add up due to rounding Total prize at scale today We do not formally measure ROI of AI investments"
  },
  {
    "figure_id": "F447",
    "report_id": "R055",
    "label": "Exhibit 4",
    "context": "Total prize at scale today Note: Numbers may not add up due to rounding Total prize at scale today We do not formally measure ROI of AI investments As agentic capabilities mature and as AI moves from decision support to workflow orchestration, the full-scale o"
  },
  {
    "figure_id": "F448",
    "report_id": "R055",
    "label": "EXHIBIT 4",
    "context": "This is where the pilot trap becomes real. A pilot can succeed in a controlled environment where it operates with selected data, dedicated teams, simplified workflows, and limited integration. At scale, the same initiative must handle live data, legacy systems"
  },
  {
    "figure_id": "F449",
    "report_id": "R055",
    "label": "Exhibit 5",
    "context": "2x to 5x ROI for Best in Class, but the Rest Rarely Measure It Note: Numbers may not add up to 100% due to rounding. Respondents were asked, “What was the realized ROI of your Consumer AI investments targeted in 2025?” # Recommended CEO Considerations: Six que"
  },
  {
    "figure_id": "F450",
    "report_id": "R055",
    "label": "Exhibit 6",
    "context": "The shift is already visible. Leading CPGs are integrating real-time consumer sentiment analysis into concept design and building cross-functional teams from the start of the innovation process, reducing handoff friction that slows development downstream. In r"
  },
  {
    "figure_id": "F451",
    "report_id": "R055",
    "label": "EXHIBIT 7",
    "context": "Agents optimize across all levers, making cross functional trade-offs within guardrails Agents continuously filter data and signal, and surface prioritized actions that replace the fixed cadence 3 Agents follow guardrails; humans intervene on the basis of risk"
  },
  {
    "figure_id": "F452",
    "report_id": "R055",
    "label": "Exhibit 8",
    "context": "Companies should monitor cost inflation. As AI scales, token spending and model usage can become a significant recurring operating cost. The risk profile, however, is not uniform across AI transformations. At the deploy level, broad workforce access can create"
  },
  {
    "figure_id": "F453",
    "report_id": "R056",
    "label": "Exhibit 1",
    "context": "## Three Threats Three of Four Structural Drivers Are Reshaping the Global Agrifood System, and One—Agricultural Intelligence—Offers a Response ## Climate volatility ## Regulatory paradigm shift ## Agricultural intelligence ## Geopolitical realignment"
  },
  {
    "figure_id": "F454",
    "report_id": "R056",
    "label": "Exhibit 2",
    "context": "# The Role of Agricultural Intelligence Agricultural intelligence uses agentic AI to sequence decisions and act autonomously, with minimal human handoff at each step. Going beyond the precision agriculture of the past two decades, it acts on behalf of humans i"
  },
  {
    "figure_id": "F455",
    "report_id": "R057",
    "label": "EXHIBIT 1",
    "context": "## EXHIBIT 1 How the Factory of the Future Significantly Lowers Conversion Costs Coffee roasting and packaging company Germany Note: FoF = Factory of the Future. Other conversion costs include cost of energy, depreciation costs, and other operational expenditu"
  },
  {
    "figure_id": "F456",
    "report_id": "R057",
    "label": "EXHIBIT 2",
    "context": "## EXHIBIT 2 # FoF Impact Is Greater in High-Cost Regions but Varies by Sector FoF impact on production costs in China and Germany to serve the German market Food processing Note: FoF = Factory of the Future. Cost includes conversion costs (cost of energy, lab"
  },
  {
    "figure_id": "F457",
    "report_id": "R057",
    "label": "Exhibit 4",
    "context": "global manufacturing survey, 87% of respondents indicated that access to talent and skills becomes more critical to sustaining a FoF deployment. And 69% said the same of infrastructure—with digital infrastructure ranking as the most critical component within i"
  },
  {
    "figure_id": "F458",
    "report_id": "R057",
    "label": "Exhibit 5",
    "context": "6. Business Context. This includes brownfield versus greenfield investment and other decisions that influence which production locations are most competitive. To capture how business context interacts with the five factors above, we built a Manufacturing Compe"
  },
  {
    "figure_id": "F459",
    "report_id": "R057",
    "label": "Exhibit 6",
    "context": "\\- Infrastructure and utilities (access to electricity, access to water and utilities, digital and tech infrastructure, logistics providers, road conditions) \\- Market and supply chain (market size, market growth, presence of competitors, availability of raw m"
  },
  {
    "figure_id": "F460",
    "report_id": "R057",
    "label": "Exhibit 7",
    "context": "In greenfield settings, by contrast, FoF capabilities can be embedded from the outset, making site selection more responsive to underlying differences in operating cost and initial one-offs (cost of land and factory building). Here, the Germany-versus-China co"
  },
  {
    "figure_id": "F461",
    "report_id": "R057",
    "label": "EXHIBIT 7",
    "context": "Americas. Tariff-driven trade realignments are creating short-term uncertainty—most companies have deferred strategic decisions on production location waiting for clarity that has yet to materialize. Beyond these immediate dynamics, investing in the FoF and it"
  },
  {
    "figure_id": "F462",
    "report_id": "R058",
    "label": "Exhibit 1",
    "context": "## EXHIBIT 1 Even in the US, Most Investors Hold Commercial Real Estate for the Long Term Share of property sales held for a given period before disposal (by volume, \\$B) Sources: CoStar; BCG analysis. Note: Amounts apply to the price when assets were disposed"
  },
  {
    "figure_id": "F463",
    "report_id": "R058",
    "label": "Exhibit 2",
    "context": "approximately 500 C-suite executives across industries worldwide. We’ve found that most players are currently still at zero or step one on a value capture ladder, meaning they allocate capital for the long term and revalue assets on a yearly basis. (See Exhibi"
  },
  {
    "figure_id": "F464",
    "report_id": "R058",
    "label": "Exhibit 3",
    "context": "# The Importance of Acting Systematically Some commercial real estate investors already use optimization strategies similar to those of commodity traders and hedge funds. For instance, they may “flip” an asset for a quick profit. But most use these strategies "
  },
  {
    "figure_id": "F465",
    "report_id": "R058",
    "label": "Exhibit 4",
    "context": "\\- Industry Reconfigurability. Due to high transaction costs, substantial regulations, long development cycles, and information asymmetry, commercial real estate players are slow to respond to supply and demand signals. This weak reconfigurability increases as"
  },
  {
    "figure_id": "F466",
    "report_id": "R060",
    "label": "Exhibit 1",
    "context": "These findings raise questions about how organizations can build a “test, learn, and adapt” mindset and a culture of continuous improvement, and about how leaders redefine roles and responsibilities in a world in which machines can think, orchestrate, decide, "
  },
  {
    "figure_id": "F467",
    "report_id": "R060",
    "label": "Exhibit 2",
    "context": "One way to tackle such concerns is to build a responsive risk framework that proactively addresses both technical and ethical challenges. Winning employees' buy-in is another path to accelerating adoption at scale. This can be done by identifying high-impact A"
  },
  {
    "figure_id": "F468",
    "report_id": "R060",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 A majority of survey respondents agreed that AI capabilities will bring exponential productivity gains. Organizations' desired outcomes of developing an Al-savvy workforce, % of respondents (n = 7,904) Faster and widespread access to information"
  },
  {
    "figure_id": "F469",
    "report_id": "R060",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F470",
    "report_id": "R060",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F471",
    "report_id": "R060",
    "label": "Exhibit 6",
    "context": "Finally, regulatory and geopolitical complexities can impede progress. As AI-native GBS drives cross-border data flows, companies need to navigate data privacy, local AI regulations, and geopolitical risk. These factors now shape GBS footprint strategy, determ"
  },
  {
    "figure_id": "F472",
    "report_id": "R060",
    "label": "Exhibit 8",
    "context": "This obstacle is more pronounced in North America (32 percent) and Europe (29 percent) than in the Asia-Pacific region (23 percent). Cultural resistance hits hardest where energy runs low: 45 percent of employees in fatigued organizations see it as a barrier, "
  },
  {
    "figure_id": "F473",
    "report_id": "R060",
    "label": "Exhibit 9",
    "context": "When it comes to workflow redesign, our surveys suggest that resource allocation is often neglected. While a lack of resources and insufficient investment in change are sometimes cited as obstacles to process optimization, the respondents to our survey downpla"
  },
  {
    "figure_id": "F474",
    "report_id": "R060",
    "label": "Exhibit 10",
    "context": "Longer-term impact can be achieved by prioritizing workflows with the highest strategic impact. For example, for product development, this can entail better product–market fit, faster launch cycles, and an optimized innovation pipeline. For integrated planning"
  },
  {
    "figure_id": "F475",
    "report_id": "R060",
    "label": "Exhibit 11",
    "context": "Effective portfolio management requires frequent divestitures of underperforming businesses. Organizations can free up capacity to take bold bets by shedding areas where they are no longer the best owner or letting go of activities that are no longer core to s"
  },
  {
    "figure_id": "F476",
    "report_id": "R060",
    "label": "Exhibit 11",
    "context": "Exhibit 11 The majority of survey respondents, particularly executives, said they are clear about their organization's must-win battles. Organizations' visibility on must-win battles, % of respondents (n = 10,018) McKinsey & Company Organizations that make por"
  },
  {
    "figure_id": "F477",
    "report_id": "R060",
    "label": "Exhibit 12",
    "context": "The priorities can be new geographic markets, products and services, innovation, customer engagement, or price positioning. Leaders then need to ensure that resources are reallocated decisively and identify low-impact and noncore activities for divestment to f"
  },
  {
    "figure_id": "F478",
    "report_id": "R060",
    "label": "Exhibit 13",
    "context": "Build a culture that puts equal weight on employee performance and well-being The goal here is to ensure employees feel energized rather than contained. High performers who sustain their performance over time are driven by purpose, adaptability, and recovery r"
  },
  {
    "figure_id": "F479",
    "report_id": "R060",
    "label": "Exhibit 14",
    "context": "There are stakeholder benefits, too, including for customers and investors. One in four organizations (24 percent) report that prioritizing D&I initiatives leads to broader customer and market appeal, while 31 percent say these initiatives enhance corporate re"
  },
  {
    "figure_id": "F480",
    "report_id": "R060",
    "label": "Exhibit 15",
    "context": "As shown in Exhibit 15, one-third of reflective leaders report adopting externally developed AI systems across most departments (versus 28 percent of steady, 29 percent of those who reflect less), and 61 percent personally champion AI adoption (versus 53 perce"
  },
  {
    "figure_id": "F481",
    "report_id": "R061",
    "label": "Exhibit 1",
    "context": "# AI use continues to broaden but remains primarily in pilot phases Our latest survey shows a larger share of respondents reporting AI use by their organizations, though most have yet to scale the technologies. The share of respondents saying their organizatio"
  },
  {
    "figure_id": "F482",
    "report_id": "R061",
    "label": "Exhibit 1",
    "context": "## Exhibit 1 Reported use of AI in at least one business function continues to increase. Phase of AI use among organizations using AI in 2025 $^{1}$ In 2017, the definition for AI use was using AI in a core part of the organization's business or at scale. In 2"
  },
  {
    "figure_id": "F483",
    "report_id": "R061",
    "label": "Exhibit 2",
    "context": "Organizations are also beginning to explore opportunities with AI agents—systems based on foundation models capable of acting in the real world, planning and executing multiple steps in a workflow. Twenty-three percent of respondents report their organizations"
  },
  {
    "figure_id": "F484",
    "report_id": "R061",
    "label": "Exhibit 4",
    "context": "## McKinsey commentary Michael Chui Senior fellow AI agents have been the subject of intense buzz and excitement. Already, about a quarter of our survey respondents report that they have started scaling at least one agentic AI system, but usually only in one o"
  },
  {
    "figure_id": "F485",
    "report_id": "R061",
    "label": "Exhibit 4",
    "context": "## For most organizations, AI use remains in pilot phases The use of AI overall is broadening within organizations. Respondents increasingly report that their organizations are using AI in more business functions (Exhibit 4). More than two-thirds of respondent"
  },
  {
    "figure_id": "F486",
    "report_id": "R061",
    "label": "Exhibit 5",
    "context": "However, many companies—particularly smaller ones—have yet to integrate AI deeply across their workflows. While only one-third of all respondents say they are scaling their AI programs across their organizations, larger companies—both in terms of revenues and "
  },
  {
    "figure_id": "F487",
    "report_id": "R061",
    "label": "Exhibit 6",
    "context": "## AI as a catalyst for innovation ## Exhibit 6 Respondents most often cite benefits from AI in innovation, employee and customer satisfaction, and competitive differentiation. Note: Figures may not sum to 100%, because of rounding. $^{1}$ Asked only of respon"
  },
  {
    "figure_id": "F488",
    "report_id": "R061",
    "label": "Exhibit 7",
    "context": "Cost decrease within business units from AI use, past 12 months, by function, $^{1}$ % of respondents While reported cases of enterprise-wide EBIT impact are limited, many respondents say they are seeing cost benefits from individual AI use cases—especially in"
  },
  {
    "figure_id": "F489",
    "report_id": "R061",
    "label": "Exhibit 8",
    "context": "Revenue increase within business units from AI use, past 12 months, by function, $^{1}$ % of respondents Revenue increases resulting from AI use are most commonly reported in use cases within marketing and sales, strategy and corporate finance, and product and"
  },
  {
    "figure_id": "F490",
    "report_id": "R061",
    "label": "Exhibit 9",
    "context": "High performers have bold ambitions to transform their business: AI high performers are more than three times more likely than others are to say their organization intends to use AI to bring about transformative change to their businesses (Exhibit 9). Exhibit "
  },
  {
    "figure_id": "F491",
    "report_id": "R061",
    "label": "Exhibit 10",
    "context": "Note: Figures may not sum to 100%, because of rounding. McKinsey & Company Objectives of AI efforts at respondents' organizations, $^{1}$ % of respondents Organizations seeing the greatest impact from AI often aim to achieve more than cost reductions from thes"
  },
  {
    "figure_id": "F492",
    "report_id": "R061",
    "label": "Exhibit 11",
    "context": "Respondents who say their organizations are using AI to spur growth and/or innovation are more likely than others are to report achieving a range of qualitative enterprise-level benefits from their AI use. Exhibit 11 # High performers are nearly three times as"
  },
  {
    "figure_id": "F493",
    "report_id": "R061",
    "label": "Exhibit 12",
    "context": "Exhibit 12 High performers are much more likely than others are to have taken AI agents to the scaling phase. Respondents who describe their organization's use of AI agents as ‘scaling’ or ‘fully scaled’ in the given business function, $^{1}$ % of respondents "
  },
  {
    "figure_id": "F494",
    "report_id": "R061",
    "label": "Exhibit 13",
    "context": "The findings also show that AI high performers' use of AI is more often championed by their leaders. High performers are three times more likely than their peers to strongly agree that senior leaders at their organizations demonstrate ownership of and commitme"
  },
  {
    "figure_id": "F495",
    "report_id": "R061",
    "label": "Exhibit 14",
    "context": "## McKinsey & Company High performers are more likely than others are to say their organizations have defined processes to determine how and when model outputs need human validation. Organizations seeing the largest returns from AI are more likely than others "
  },
  {
    "figure_id": "F496",
    "report_id": "R061",
    "label": "Exhibit 15",
    "context": "Finally, high-performing organizations are investing more in AI capabilities. More than one-third of high performers say their organizations are committing more than 20 percent of their digital budgets to AI technologies (Exhibit 15). These resources are helpi"
  },
  {
    "figure_id": "F497",
    "report_id": "R061",
    "label": "Exhibit 16",
    "context": "As organizations expand their use of AI, respondents share differing perspectives on how AI might affect their workforce size in the year ahead. Looking at the functions in which organizations are using AI, a plurality of respondents observed little to no chan"
  },
  {
    "figure_id": "F498",
    "report_id": "R061",
    "label": "Exhibit 17",
    "context": "Expectations differ on the impact of AI on the size of respondents' enterprise-wide total workforce. While a plurality of respondents expect to see little or no effect on their organizations' total number of employees in the year ahead, 32 percent predict an o"
  },
  {
    "figure_id": "F499",
    "report_id": "R061",
    "label": "Exhibit 18",
    "context": "At the same time, most respondents—and an even larger share from larger companies—note that their organizations hired for AI-related roles over the past year (Exhibit 18). While the talent needs differ by company size overall, software engineers and data engin"
  },
  {
    "figure_id": "F500",
    "report_id": "R061",
    "label": "Exhibit 19",
    "context": "Over the past six years, our research has consistently found that few risks associated with the use of AI are mitigated by most respondents' organizations. In our latest findings, the share of respondents reporting mitigation efforts for risks such as personal"
  }
]