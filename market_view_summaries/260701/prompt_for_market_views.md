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
  "智库/国际机构": 3
}

报告摘要：
[
  {
    "id": "R001",
    "title": "IMF警告：AI正在把金融业网络安全变成一个“机器速度”战场",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF警告：AI正在把金融业网络安全变成一个“机器速度”战场\n\n2026年6月，IMF发布了一份注定不会平静的金融部门网络安全报告。这份由IMF货币与资本市场部主任Tobias Adrian领衔撰写的Note，没有选择讲述一个关于“新型攻击技术”的故事。它讲的是另一件事：AI正在以机器速度放大金融体系已有脆弱性的传染半径——而现有的防御体系、监管框架和国际协调机制，都还没有准备好应对这个速度级别。\n\n这份报告的核心判断值得每一位金融机构决策者和政策制定者认真对待：**金融稳定的核心威胁不在于AI创造了全新的攻击方式，而在于它让已有的脆弱性被更快、更广、更频繁地发现和利用，从而将操作层面的弱点转化为系统性事件。**\n\n换句话说，过去一个银行被攻破可能只是一家银行的问题。但在AI时代，一个云服务商的漏洞被AI同时发现并利用，可能在几分钟内波及整个支付体系、清算系统和核心交易基础设施。\n\n这不是科幻。报告引用的数据已经显示了清晰的趋势。\n\n> **KC评论：** 这份报告最值得读的部分不是它的结论——结论其实很清晰——而是它如何论证“规模效应”这个关键变量。完整报告中，作者用大量图表和案例展示了攻击速度、漏洞发现时间、横向移动时间等指标在过去18个月的变化曲线。这些数据本身比任何判断都更有说服力。建议读者重点关注Figure 1和Box 1的Claude Mythos案例，后者是2026年4月刚刚发生的真实事件。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 攻击窗口从小时级压缩到分钟级，金融体系的基础设施却还是按天运转\n\n报告引用了CrowdStrike 2026年全球威胁报告的数据：AI驱动的攻击者活动在2024至2025年间增加了89%，但更令人警醒的是另一个指标——攻击者在被入侵网络内横向移动的平均时间（“brea\n\n[... middle omitted ...]\n\n在AI时代的金融安全问题上，信息的时效性和分析深度同样重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在改写金融业网络攻防规则\n\nAI重塑金融网络安全\n\n最近IMF出了一份很扎实的研报，讲AI怎么改变金融业的网络安全格局。不是那种吓唬人的标题党，但信息量很大，我帮你拆成3个核心点👇\n\n1️⃣ 核心风险不是新攻击，而是规模效应\nAI并没有发明全新的网络攻击方式，但它让漏洞发现和利用的速度、频率、广度都指数级上升。原来一个漏洞可能几个月才被利用，现在几周甚至几天。更可怕的是，AI可以同时攻击多个目标，把单个机构的漏洞变成系统性风险。研报提到一个数据：2024-2025年，AI驱动的攻击活动增长了89%。\n\n2️⃣ 金融业最脆弱的是“共享基础设施”\n银行、支付系统、交易所都在用同样的云服务、操作系统、开源软件。AI攻击可以同时打击这些共同依赖的基础设施。过去几年已经出现过TARGET系统宕机、英国央行RTGS技术问题，AI会让这类事件更频繁、更同步。研报强调：关键不是防住所有攻击，而是控制“爆炸半径”——也就是一次攻击能造成的最大损害范围。\n\n3️⃣ 攻防不对称在加剧，防御必须“机器速度”\n攻击者用AI可以几分钟内完成横向移动和数据窃取，而人类响应需要几小时甚至几天。一个案例：某前沿AI模型在测试中自主完成了\n\n[... middle omitted ...]\n\n those of the author(s), although they do not necessarily represent the views of the IMF, or its Executive Board, or its Management.\n\nABSTRACT: Artificial intelligence (AI) is reshaping cyber \n\n[... middle omitted ...]\n\ncompanies-shared-in-2025/\n\nWorld Economic Forum. 2026. “Anthropic’s Mythos Moment: How Frontier AI is Redefining Cybersecurity.” April 20.\n\n![](images/683d8ade2d3912a66e819972633a5a13ae1de010a9500b7c0138e3a76d7dc882.jpg)"
  },
  {
    "id": "R002",
    "title": "IMF：洪都拉斯通过了压力测试，但能源补贴仍是最大隐患",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：洪都拉斯通过了压力测试，但能源补贴仍是最大隐患\n\n一份来自国际货币基金组织（IMF）的国别报告，通常不会成为全球财经读者的焦点。但当这份报告的主角是一个正在经历“油电双重冲击”的中美洲经济体，且其改革进程恰好处于新旧政府交接的关键窗口期时，报告中的判断就具备了超越单一国家的参考价值。\n\n2026年6月发布的IMF洪都拉斯第四、五次审议报告，核心结论是：**该国经济在2025年表现出超预期的韧性，但2026年的外部环境已发生根本性转变，真正的考验刚刚开始。**\n\n报告传递了一个清晰但微妙的信号：洪都拉斯在过去一年交出了不错的成绩单——GDP增长3.8%，通胀回落至目标区间，财政赤字远低于预期，国际储备显著增厚。然而，这些成绩大多建立在2025年相对有利的外部条件之上：创纪录的咖啡价格、强劲的侨汇流入、以及尚未恶化的全球油价。\n\n进入2026年，剧本已经重写。全球石油供给冲击推高了国内能源价格，而潜在的强厄尔尼诺现象则为农业和基础设施带来了新的气候风险。IMF的这份报告，本质上是一份“压力情景下的政策路线图”——它肯定了新政府延续改革的政治意愿，但也毫不避讳地指出了最脆弱的环节：国有电力公司ENEE的财务黑洞，以及能源补贴体系的扭曲。\n\n对于关注新兴市场债务、大宗商品传导机制以及国际援助有效性的读者而言，这份报告的价值不在于洪都拉斯本身，而在于它提供了一个**小国如何在“外部冲击叠加内部结构性问题”时进行政策权衡**的典型案例。\n\n> **KC评论：** 很多人觉得IMF国别报告太细、太技术，但如果你把洪都拉斯看作一个“压力测试样本”，就能读出更多东西。当全球油价上涨、侨汇可能回落、气候风险上升时，一个财政空间有限、电力系统亏损、且正在进行政治交接的国家，其政策选择几乎是所有新兴市场的缩影。完整报告里对“石油冲击传导机制”和“厄尔尼诺影响”的两张图，\n\n[... middle omitted ...]\n\n里，我们持续追踪全球资本流动、政策变化和资产定价的底层逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nIMF给了洪都拉斯2.4亿美元，为什么？\n\n一个经济体的韧性\n\nIMF刚刚放款2.42亿美元给洪都拉斯，这是EFF/ECF安排的第四、五次审查通过后的资金。背后是洪都拉斯2025年经济表现超预期，但2026年压力不小。\n\n1️⃣ 2025年，洪都拉斯经济很稳\n- GDP增速3.8%，靠的是历史高位的咖啡价格和大量侨汇支撑消费\n- 财政赤字只占GDP的0.7%，远低于目标1.5%——说明财政纪律执行得不错\n- 通胀回落到4%的目标区间，外汇储备也明显增加\n\n2️⃣ 但2026年，外部环境变差了\n- 全球石油供给冲击推高油价，预计通胀会反弹到5.7%\n- 经济增长预计放缓到3.3%\n- 还有强厄尔尼诺风险，对农业和基础设施是个考验\n\n3️⃣ 结构改革有亮点，也有拖延\n- 11/17个结构性基准达标，主要集中在近几个月\n- 电力公司ENEE的欠款指标没达标，但洪方已采取整改措施，IMF给了豁免\n- 反洗钱/反恐融资立法已提交国会，等待FATF评估\n\n4️⃣ 接下来要看三个关键点\n- 能源补贴要更精准，不能一刀切\n- 外汇分配机制要逐步过渡回银行间市场\n- 财政要继续收紧，但也要留空间应对油价冲击\n\n一个有意思的细节\n\n[... middle omitted ...]\n\n been released and are included in this package:\n\n• A Press Release including a statement by the Chair of the Executive Board.\n\n\\- The Staff Report prepared by a staff team of the IMF for the \n\n[... middle omitted ...]\n\n sixth and final reviews, and approval of the exchange restriction. Finally, we thank the Fund for its continued support under the EFF/ECF arrangements, and for the valuable technical assistance and capacity development."
  },
  {
    "id": "R003",
    "title": "IMF：卢森堡的“低债务幻觉”正在被赤字吞噬",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：卢森堡的“低债务幻觉”正在被赤字吞噬\n\n当一个国家长期以“低公共债务”作为信用名片时，市场往往容易忽视其财政结构的真实变化。IMF在2026年6月发布的卢森堡第四条磋商报告中给出了一个值得警惕的判断：卢森堡的财政缓冲正在被结构性支出扩张和收入放缓双重挤压，而市场尚未对此充分定价。\n\n这份报告的核心信号不是“卢森堡要出事”，而是“低债务经济体同样面临财政纪律松散的陷阱”。对于关注欧洲资产配置、跨境金融监管趋势以及小型开放经济体韧性的读者来说，这不仅仅是一份国别报告，更是一份关于“财政幻觉如何形成并可能被打破”的案例研究。\n\n卢森堡的GDP在2025年仅增长0.6%，而同期政府支出增速达到3.7%，公共消费占GDP比重持续上升。更关键的是，IMF预计2028年政府赤字将扩大至GDP的3.0%，而公共债务将从2024年的26.3%攀升至32.0%。在一片“低债务”的赞美声中，斜率的变化往往比绝对值更重要。\n\n> **KC评论：** 市场习惯用“卢森堡债务率不到30%”来安慰自己，但IMF的预测显示，如果现行政策不变，五年内卢森堡的债务率将上升近6个百分点。对于一个经济体量小、外部冲击传导快的国家，这个速度并不慢。完整报告中的债务可持续性分析（Annex IV）给出了更细致的压力测试情景，值得关注。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮增长放缓的真正原因不是周期，而是公共部门对私人部门的挤出\n\nIMF报告反复使用一个关键词：“public sector playing a dominant role”。这不是一句客气的描述，而是对增长质量的根本性质疑。\n\n数据显示，2024年卢森堡国内总需求增长2.5%，其中私人消费贡献3.2%，但公共消费贡献高达4.9%。更值得关注的是，同期固定资产投资下降2.0%，\n\n[... middle omitted ...]\n\n细情景分析感兴趣，欢迎加入社群，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n卢森堡经济怎么了？IMF最新诊断\n\n增长乏力，但底子还在\n\n2026年IMF对卢森堡的年度体检报告出炉了，几个关键判断值得关注👇\n\n1️⃣ 增长慢下来了\n- 2025年GDP只涨了0.6%\n- 失业率突破6%，通胀回到2.5%以上\n- 财政从盈余0.9%直接跌到赤字2%\n- 公共部门成了增长主力，私人部门偏弱\n\n2️⃣ 底子仍然厚\n- 政府债务只有GDP的26%，非常健康\n- 银行资本充足率25.2%，不良贷款仅1.4%\n- 金融系统抗压能力不错，压力测试过关\n\n3️⃣ 未来怎么走\n- 2026年预计GDP回升到1.2%，2027年1.7%\n- 中期潜在增速约2%\n- 关键靠私人部门发力，不能光靠政府花钱\n\n4️⃣ 政策建议\n- 财政上要控制经常性支出，扩大税基\n- 金融上盯紧流动性、杠杆和集中度风险\n- 结构上推AI应用、解决住房问题、提高劳动力灵活性\n\n卢森堡的情况有点像“高收入国家的中年危机”——底子好但增长动力不足，需要靠改革重新激活。\n\n你们觉得这种“底子好但增长慢”的经济体，最该优先做什么？\n\n#学习笔记\n\n[source_mineru.md]\nIMF Country Report No. 26/\n\n[... middle omitted ...]\n\noncluded the Article IV consultation with Luxembourg.\n\n\\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 22, 2026, following discussions t\n\n[... middle omitted ...]\n\nees further temporary financial aid for households envisaging the installation of non-fossil fuel boilers or an energy retrofit in their homes. This is a good example of how a temporary measure can have a lasting impact."
  },
  {
    "id": "R004",
    "title": "波士顿咨询：商业财产险的下一场战役，不在承保，在组合管理",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：商业财产险的下一场战役，不在承保，在组合管理\n\n财产与意外险（P&C）公司正站在一个关键的十字路口。当整个行业的目光都集中在生成式AI如何改造核保和理赔流程时，波士顿咨询（BCG）在2026年6月发布的一份报告中提出了一个更尖锐的判断：真正未被开采的、能带来持续竞争优势的富矿，位于组织金字塔的顶端——组合管理（Portfolio Management）。\n\n这不是一个关于技术替代人的故事。这是一个关于“速度”和“粒度”如何重构保险业竞争壁垒的故事。BCG基于对超过50位P&C商业保险高管的调研，给出了一个具体的量化信号：率先拥抱智能体AI（Agentic AI）进行组合管理的公司，有望实现毛保费增长1%-3%，综合成本率改善1%-2.5%，股本回报率提升1%-2%。在承保周期趋紧、波动性加剧的当下，这些数字足以拉开一个身位。\n\n但真正值得决策者关注的，不是这些数字本身，而是其背后的逻辑：为什么传统的组合管理在今天失效了？智能体AI提供的究竟是一个新工具，还是一种新的管理范式？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 传统组合管理的四个死穴，正在侵蚀保险公司的风险调整后回报\n\nBCG的报告直指核心：当前大多数商业P&C公司的组合管理，本质上是一套“后视镜系统”。它擅长解释过去，却无力预测和塑造未来。报告归纳了四个相互关联的致命弱点。\n\n第一，可见性碎片化且浅薄。核保、理赔、风险工程和再保险数据各自为政，沉没在不同的系统中。管理层看到的报告是按险种和区域汇总的宏观视图，缺乏识别边际变化或风险集中度早期信号的颗粒度。当一个客户的财产险和意外险组合出现风险偏移时，系统无法在它造成实际损失前发出预警。\n\n第二，组合再平衡是向后看的。CFO和CRO可以测试主要的资本和再保险情景，但无法模拟增长、风险暴露和资本配\n\n[... middle omitted ...]\n\n有更多信息，而在于更高效地理解信息。我们试图帮你做到这一点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI保险管家来了，组合管理不用靠玄学\n\n**封面：** 保险组合管理新解法\n**副标题：** 投行研报拆解，AI如何让承保更聪明\n\n---\n\n**1. 问题：为什么传统组合管理总是慢半拍？**\n\n商业财产险公司正面临一个尴尬困境：全球风险波动越来越快，但内部数据还躺在不同系统里“各自为政”。\n\n- 承保、理赔、再保险数据互不相通，风险集中度像盲人摸象\n- 组合调整只看历史，等发现不对时，市场早已转向\n- 前线核保员的工具还停留在旧风险偏好上，策略执行层层打折\n- 风险质量问题只有等到大额损失才浮出水面\n\n**2. 解法：Agentic AI打造“永动机”式组合管理**\n\n投行研报提出一个五步飞轮模型，让AI代理像保险管家一样，7x24小时盯着组合：\n\n**第一步：修复现有保单**\nAI代理逐单扫描，找出定价漏洞、条款遗漏、续保优化点。比如财产险查估值明细，工伤险对比实际人力成本。关键是人机协同，高层可设定审查权限。\n\n**第二步：优化资本分配**\n结合内部组合、竞争对手费率、第三方风险信号，实时测试不同资本配置方案对回报率的影响。CEO们可以在沙盘上推演再保险策略。\n\n**第三步：自动更新指引**\n\n[... middle omitted ...]\n\nompetitive advantage for those who invest the time to build it.\n\nP&C executives are under pressure to improve risk-adjusted return on equity while managing complex, multiline businesses in an \n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R005",
    "title": "波士顿咨询：零售银行真正的AI红利，不在降本，而在重新定义客户关系",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：零售银行真正的AI红利，不在降本，而在重新定义客户关系\n\n过去两年，几乎每一家零售银行都在谈生成式AI。但波士顿咨询这份题为《AI-First Banks Are Rewriting the Rules of Retail Banking》的研报，给出了一个值得所有银行决策者停下来思考的判断：真正拉开差距的，不是谁先用上了大模型，而是谁能把AI嵌入到“获取客户、服务客户、执行交易”三大核心流程中，并以此重构银行与客户之间的关系。\n\n这不是一份罗列技术趋势的报告。它更像一份“AI-first银行”的作战手册：哪些投入真正产生了可量化的业务结果，哪些做法只是“拿着锤子找钉子”，以及最关键的一点——为什么大部分银行的AI价值仍然停留在零散用例，而少数银行已经开始在营收、成本、客户深度上实现系统性跃迁。\n\n以下是我们基于这份报告的核心提炼与解读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 零售银行的结构性优势，正在被消费端的AI体验倒逼\n\n零售银行之所以被波士顿咨询视为AI部署的“天然沃土”，有三个结构性原因：数字化程度相对较高、数据资产丰富（尽管被遗留系统束缚）、以及客户对AI应用的接受度正在快速提升。\n\n但报告同时点出一个令人不安的现实：零售消费者正在用“购物、旅行、数字媒体”领域的AI原生体验来对标银行服务。当ChatGPT可以在几秒内给出投资建议，当电商平台可以基于用户行为实时调整推荐，银行如果还在用“我们正在测试AI客服”来回应，客户耐心正在快速耗尽。\n\n> **KC评论：** 这其实是零售银行目前最容易被低估的风险。消费者不会因为你是银行就降低预期。波士顿咨询的数据显示，64%的用户已经在用AI做购买决策。这意味着，如果银行在搜索、推荐、交互体验上无法达到“AI原生”水准，用户流失可能不是渐进式的\n\n[... middle omitted ...]\n\n希望获得完整研报解读与原始图表，欢迎加入我们的社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n银行迎来AI改造窗口期，先发优势明显\n\nAI优先银行正在改写规则\n\n投行研报指出，零售银行正处在GenAI和Agentic AI的关键窗口期。相比其他行业，银行拥有更成熟的数字化基础、更丰富的数据资产、更高的客户AI接受度——但大多数银行还没把价值真正释放出来。\n\n1/ 为什么银行适合AI改造？\n- 数字化程度高，数据积累深厚（虽然很多在旧系统里）\n- 客户对AI应用的接受度已经上来了\n- 结构上就适合做智能增强和体验重塑\n\n2/ AI优先银行在做什么？\n- 获客端：用合成客户画像验证产品设计，投放前就测试定价和话术，新客产品销售额提升40%+\n- 服务端：70%+人工话务量由语音机器人处理，成本只有传统方式的1/5\n- 运营端：非标文件实现无人处理，周转时间降低70%\n- 信贷端：智能核保引擎把报价时间压缩到原来的1/10-1/5\n- 风控端：AI驱动的反洗钱流程，成本降低50%\n\n3/ 怎么落地？\n- 选3-4个核心业务场景深度改造，别撒胡椒面\n- 先做业务价值再搭平台，别反着来\n- 从Day 1就设计风控流程，别等上线再补\n- 早期集中力量建AI能力中心，成熟后再分散到业务线\n\n4/ 关键提醒\n研\n\n[... middle omitted ...]\n\nlore the impact of GenAI and Agentic AI in retail banking and the approach followed to deliver impact. We address key questions faced by bank executives:\n\n\\- Why are GenAI and Agentic AI imper\n\n[... middle omitted ...]\n\nholesale Banking\nMunich\n\n## Javier Perez Moino\n\nMD & Partner\nAI in Customer Acquisition\nMadrid\n\n## Matthew Barton\n\nMD & Partner\nAI in Collections\nPhiladelphia\n\n## Yogesh Mishra\n\nMD & Sr. Partner\nAI in Tech\nDallas\n\n## BOG"
  },
  {
    "id": "R006",
    "title": "波士顿咨询：CPG巨头正在为“研发失落的十年”买单",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CPG巨头正在为“研发失落的十年”买单\n\n大型消费品公司过去十年把6%到15%的营收投入广告，却只拿出1.5%做研发。这个战略选择，正在变成一场估值灾难。波士顿咨询（BCG）最新研报指出，从2022年底到2025年底，大型食品饮料公司的三年累计股东总回报中位数约为-5%，而同期标普500的累计总回报接近90%。表现最差的CPG公司，累计股东回报甚至低于-20%。\n\n这不是周期性的业绩波动。这是结构性的战略清算。\n\nBCG的报告标题直截了当：“Processed and Pressured: CPG's Lost Decade of R&D”。核心判断只有一个：消费者向更健康、更简单产品的结构性迁移，已经暴露了CPG巨头至少十年的研发投入不足。而过去依赖规模和营销肌肉的成功公式，正在加速瓦解。\n\n> **KC评论：** 这份报告最有冲击力的不是数据本身，而是它把“研发投入不足”从一个财务指标提升到了战略清算的高度。它回答了一个关键问题：为什么CPG巨头在通胀、供应链危机等外部冲击过去后，仍然无法恢复增长？答案藏在1.5%的研发占比里。完整报告提供了跨行业对比图表，以及达能、雀巢等公司的具体案例拆解。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 1.5%的研发投入与6-15%的广告支出，这个剪刀差已经维持了十年\n\nBCG的数据显示，从2015年到2025年，全球CPG行业平均研发投入仅占营收的1.5%。同期，广告和促销支出占比高达6%到15%。更关键的是，这期间全球CPG研发支出年均增速仅为1.2%，而广告和促销支出增速为2.6%，是研发的两倍多。\n\n这不是某个季度的偏差，而是一个持续十年的战略选择。\n\n对比其他行业，这个差距更加刺眼。根据纽约大学斯特恩商学院2026年1月的数据，制药行业研发投入占比21%\n\n[... middle omitted ...]\n\n在具体公司中的应用案例、以及那些“弱信号”如何被识别和放大。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n大牌食品的“研发债”该还了\n\n食品巨头正在为“偏科”买单\n\n过去十年，大食品公司把💰砸在广告和渠道上，研发只投了营收的1.5%，而同期广告费占了6%-15%。现在这个模式玩不转了。\n\n1️⃣ 消费者变了\n健康意识觉醒+GLP-1减肥药普及，大家开始躲着超加工食品。数据显示，超加工食品增速正在跑输整个食品饮料大盘。\n\n2️⃣ 新玩家抢地盘\n益生菌汽水、植物基乳品这些爆款，基本都来自小品牌和初创公司。大牌在麦片、零食等品类持续丢份额，输给了小品牌和零售商自有品牌。\n\n3️⃣ 监管在加码\n美国政府新推出的膳食指南明确建议少吃超加工食品，130多项州级法案正在路上。Yuka这类食品评分App在美国已有2500万用户，每月还涨60万。\n\n4️⃣ 市值在缩水\n过去三年，大食品公司股东回报中位数是-5%，而标普500涨了90%。投资者已经用脚投票。\n\n💡 怎么办？\n研报给出了三条路径：评估品牌暴露风险、重建消费者信任、重启创新引擎。核心是重新分配资本——过去十年忙着回购股票，未来十年得把钱投回研发。\n\n达能是个正面案例，过去两年研发投入增加32%，营收增速4%+，股东回报领先同行。小品牌也在证明，创新真的能卖得动。\n\n#学\n\n[... middle omitted ...]\n\nuctural shift that many big CPG manufacturers have so far failed to navigate is consumers' growing preference for healthier and simpler products and for greater transparency about ingredients,\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R007",
    "title": "波士顿咨询：价值创造领导力已从科技转向重资产，这不是短期波动",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：价值创造领导力已从科技转向重资产，这不是短期波动\n\n全球股票市场在过去五年间实现了年均约12%的总股东回报（TSR），市场韧性超出多数投资者预期。但波士顿咨询（BCG）最新发布的2026年价值创造者排名揭示了一个更值得关注的结构性变化：引领市场回报的行业和公司，已经不再是过去十年投资者所习惯的那些。\n\n这不是一次简单的板块轮动，也不是市场情绪的短期切换。BCG的报告明确指出，这是一场由AI部署阶段、地缘政治重构和资本成本重置共同驱动的价值创造领导力转移。对于产业决策者和长期投资者而言，理解这一转移的内在逻辑，比预测下一个季度的市场方向更为重要。\n\n**这份报告最值得关注的判断是：资产密集型行业（矿业、油气、航空航天与国防、建筑、银行）已取代科技驱动型行业，占据了价值创造排名的顶端。而在科技板块内部，硬件和电子元件持续跑赢，软件与IT服务则从去年排名的第四位骤降至第31位。**\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nBCG的排名基于2021至2025年五年间的年均TSR，样本覆盖全球35个行业的2368家公司。报告发现，资产密集型行业的中位数TSR显著领先。技术硬件以20%的年均TSR位居榜首，建筑业16%、矿业15.8%紧随其后。相比之下，软件与IT服务的中位数TSR虽仍有15.7%，但排名从去年的第四位跌至第31位，降幅高达27个位次。\n\n这一排名的剧烈变动，其背后力量并非市场情绪的随机漂移。BCG将其归因于三个结构性驱动力：\n\n第一，AI价值当前正加速向物理基础设施层集中。AI部署的现阶段是资本密集型的，需要芯片、数据中心、电力基础设施和物理连接。硬件制造商、电子元件生产商和能源供应商是直接受益者。而软件公司面临的货币化路径则更为不确定——许多\n\n[... middle omitted ...]\n\n。在信息密度和时效性上，这是一个传统研究报告无法替代的工具。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026研报：价值创造正在大迁移\n\n价值创造，正在换赛道\n\n资产重行业逆袭，科技让位\n\nBCG最新研报揭示了一个有意思的变化：过去十年领跑的科技行业，在价值创造排名中退位了。取而代之的，是采矿、油气、军工、建筑、银行这些“重资产”行业。\n\n1/ AI的价值，流向了物理基础设施\nAI部署进入资本密集型阶段，芯片、数据中心、电力设施、物理连接成为直接受益者。硬件和电子元件表现强劲，而软件和IT服务排名从第4位骤降至第31位——AI变现路径还不清晰，反而开始颠覆软件价值链。\n\n2/ 地缘政治重塑资本流向\n全球国防支出加速，能源安全成战略重点，供应链碎片化推动基建投资。油气、采矿、金属、建筑、军工——这些行业占了前6名中的5席。\n\n3/ 高利率环境利好银行\n持续的高息环境改善了银行净息差，推动估值上升。市场似乎预期这种顺风足以对冲信贷风险。\n\n但行业不是命运\nBCG数据指出：35个行业中，有32个行业的头部公司收益率跑赢市场中位数。即使在垫底行业，也能诞生优秀选手。关键还是公司层面的战略、资本配置和执行能力。\n\n最大挑战：期望溢价\n美国非金融公司的市场价值与基本面价值之间的差距，已超过2000年互联网泡沫峰值。企业面\n\n[... middle omitted ...]\n\nn a decade, the companies and sectors leading that performance are not the ones investors have come to expect.\n\nBCG's 2026 Value Creators ranking reveals that leadership in value creation has \n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R008",
    "title": "波士顿咨询：中美AI正在分裂世界，企业必须选边站",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：中美AI正在分裂世界，企业必须选边站\n\n2026年6月，波士顿咨询发布了一份长达15页的研报，标题直白得有些残酷：“The Great Divide: How the US and China Are Splitting the AI World”。这不是关于技术路线差异的温和讨论，而是一份关于“技术主权”如何重塑全球商业格局的硬核分析。\n\n报告最值得关注的判断只有一个：中美AI技术栈正在从“可兼容”走向“不可兼容”。2024年，企业还能在两个生态之间灵活切换；到了2026年，这种中立空间正在急剧收窄。对于全球CEO和政策制定者而言，选边站的时间窗口正在关闭。\n\n这份报告的核心证据来自六个维度的量化对比——资本、人才、知识产权、数据、能源、算力。波士顿咨询的结论是：美国在资本部署和人才密度上保持领先，中国在算力追赶和实体经济渗透上加速逼近。但真正重要的不是谁领先，而是两个生态正在各自形成闭环，彼此依赖度持续下降。\n\n> **KC评论：** 波士顿咨询这份报告的价值不在于告诉你“美国领先还是中国领先”，而在于它用数据证明了“两个生态正在互斥”。对于企业来说，这意味着过去那种“在美国买芯片、在中国做应用、在东南亚部署”的全球化AI策略，可能很快就不成立了。完整报告里有一张非常关键的“生态系统互锁图”，展示了美国科技巨头之间超过1.5万亿美元的交叉投资和商业承诺，这张图值得仔细看。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 美国策略：用资本堆出规模，但系统性风险正在累积\n\n美国AI策略的核心逻辑是“赢在规模”。这听起来像一句口号，但波士顿咨询用数字给出了具体定义：2025年美国前20大科技公司的资本支出超过4000亿美元，2026年预计突破8000亿美元。相比之下，中国同口径的数字是630亿美元和预计增长后\n\n[... middle omitted ...]\n\n原始图表感兴趣，欢迎加入社群，获取完整的研报解读与持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国vs中国，AI世界正在分裂\n\nAI分裂进行时\n\n中美AI栈正在“脱钩”，企业可能很快就要被迫选边站\n\n1️⃣ 美国策略：砸钱赢规模\n- 2025年科技巨头CAPEX超4000亿美元（中国仅630亿），2026年预计破8000亿\n- 数据中心容量50+GW（中国31GW，欧盟12GW）\n- 三大云商未来合同收入超1.4万亿美元，翻倍有余\n- 投资网络紧密：AI实验室、芯片商、云商互相持股、签多年合同，总金额超1.5万亿\n\n2️⃣ 中国策略：快速跟进+实体经济渗透\n- 在算力上持续缩小差距\n- 系统化将知识产权优势转化为“快跟随者”模式\n- 重点放在AI在实体经济的快速落地（制造业、公共服务等）\n- 自研芯片加速推进，减少对美依赖\n\n3️⃣ 两大生态正在“不可逆分裂”\n- 2024年还能两边混用，现在中立越来越难\n- 美国主导模型层和基础设施层，中国主攻基础研究和应用层\n- 企业选AI栈=选市场+选风险敞口\n\n💡 企业怎么办？\n- 冗余：至少签两家模型供应商\n- 模块化：换模型不换代码\n- 异质性：美国闭源模型+开源自托管模型搭配用\n- 保持对出口管制、技术突破的“观察清单”\n\nAI不再是你去竞争的东西，而是\n\n[... middle omitted ...]\n\ns a source of national power, their AI strategies have diverged. Each country is developing an AI technology stack designed to reduce its dependence on the other—which also means their stacks \n\n[... middle omitted ...]\n\nphysical AI are rising in relevance—hence this piece’s broader use of “AI” rather than generative AI alone.\n\n2 OpenAI has since pivoted toward leasing capacity from third parties rather than owning data centers directly."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Recent observational evidence suggests that AI is increasingly becoming embedded in the threat landscape. For example, CrowdStrike (2026) reports that activity by AI-enabled adversaries increased by 89 percent between 2024 and 2025, but the average time requir"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF警告：AI正在把金融业网络安全变成一个“机器速度”战场｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "2. The new authorities have strongly affirmed their commitment to continuing the Fund-supported program, which remains a key policy anchor, especially in the context of a changed external environment and heightened external risks. Implementation of the structu"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## RECENT ECONOMIC DEVELOPMENTS 4. Inflation had remained within the Central Bank of Honduras (BCH)'s tolerance range (4±1 percent) prior to the conflict in the Middle East. $^{1}$ Headline inflation ended 2025 just under 5.0 percent and had declined to 3.5 pe"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "...as higher global oil prices passed through quickly to domestic fuels prices. effects (Text Figure 1). $^{2}$ The passthrough of higher global oil prices has since exerted upward pressure on headline inflation, which increased to 5.6 percent in April, with t"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "...as higher global oil prices passed through quickly to domestic fuels prices. effects (Text Figure 1). $^{2}$ The passthrough of higher global oil prices has since exerted upward pressure on headline inflation, which increased to 5.6 percent in April, with t"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "aimed at improving coordination and delivery across programs, reduction of external funding for Red Solidaria, and reverification of beneficiary eligibility. Tax revenues declined as a share of GDP due to lower indirect taxes in 2025, $^{4}$ marginally missing"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "percent year-to-date through April. After declining 5 percent in 2025, the value of energy imports increased 7 percent year-to-date through March. 7. Reserve coverage and FX market dynamics strengthened further (Text Figure 2). Net international reserves (NIR)"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Text Figure 2. International Reserves and Foreign Exchange Market Developments Reserves have accumulated organically in 2025 and early 2026, in the absence of significant external disbursements. Remittances surged in H1 2025 and remained dynamic throughout 202"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Remittances surged in H1 2025 and remained dynamic throughout 2025 and into 2026Q1. FX supply in the BCH auction has fully met demand since July 2025. Reserve accumulation dynamics in 2025 and early 2026 are a stark contrast to recent years. Cumulative Change "
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "FX supply in the BCH auction has fully met demand since July 2025. Reserve accumulation dynamics in 2025 and early 2026 are a stark contrast to recent years. Cumulative Change in BCH Net International Reserves (Millions of USD, through end-December) Sources: C"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "8. Credit growth moderated in 2025 but is showing signs of potential recovery. Private sector credit growth fell below 7 percent (year-on-year) in December 2025, reflecting weaker demand (election-related uncertainty, strong remittances) and past tightening of"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "19. The authorities have strengthened the FX allocation mechanism further. The BCH published an update to regulations for the FX auction (met end-September 2025 SB), increasing the threshold for FX bids not requiring documentation from USD 10,000 to USD 50,000"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Real Effective Exchange Rate (Index: December 2011=100) ...and while the exchange rate has moved to the stronger end of the band, the band continues to crawl. Text Figure 4. Exchange Rate Developments Driven by nominal exchange rate depreciation since resumpti"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "...and while the exchange rate has moved to the stronger end of the band, the band continues to crawl. Text Figure 4. Exchange Rate Developments Driven by nominal exchange rate depreciation since resumption of the crawl and a weaker USD ... ...the real effecti"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Driven by nominal exchange rate depreciation since resumption of the crawl and a weaker USD ... ...the real effective exchange rate has adjusted in 2025 and early 2026. Sources: Haver, Central Bank of Honduras; and IMF staff calculations. 20. The BCH will cont"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sources: Haver, Central Bank of Honduras; and IMF staff calculations. 20. The BCH will continue to follow a data-driven monetary and exchange rate policy approach, adjusting policies as necessary to contain inflationary pressures and maintain external stabilit"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sources: Haver, Central Bank of Honduras; and IMF staff calculations. 20. The BCH will continue to follow a data-driven monetary and exchange rate policy approach, adjusting policies as necessary to contain inflationary pressures and maintain external stabilit"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "45. Staff supports the authorities' request for Board approval for the retention of the exchange restriction arising from measures implemented by the BCH limiting the allocation of FX at the auction since its reintroduction. While the conditions of the auction"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Honduras: Real Sector Developments Output rebounded quickly to pre-pandemic levels in 2021 but remains below the prior trend. Consumption, smaller contractions in real exports, and some inventory build-up supported growth in 2025. Services, especiall"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Services, especially the banking sector, continue to be the main driver of growth. Headline inflation had remained within the tolerance range $4 \\pm 1$ percent prior to the oil price shock. Labor force participation picked up in 2025, and aggregate unemploymen"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Headline inflation had remained within the tolerance range $4 \\pm 1$ percent prior to the oil price shock. Labor force participation picked up in 2025, and aggregate unemployment rate further declined... ...although the gap between male and female unemployment"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "...although the gap between male and female unemployment rates widened. Sources: BCH; Haver Analytics; IMF World Economic outlook; INE survey; and IMF staff estimates. Figure 2. Honduras: External Sector Developments The current account moved to a surplus in 2"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: BCH; Haver Analytics; IMF World Economic outlook; INE survey; and IMF staff estimates. Figure 2. Honduras: External Sector Developments The current account moved to a surplus in 2025... ...supported by remittances and record-high coffee prices. The te"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Honduras: External Sector Developments The current account moved to a surplus in 2025... ...supported by remittances and record-high coffee prices. The terms of trade improved significantly in 2025 prior to the oil price shock. Continued exchange rat"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The terms of trade improved significantly in 2025 prior to the oil price shock. Continued exchange rate crawl has contributed to a depreciation of the real effective exchange rate. Remittances surged in 2025... ..... contributing to a strengthening of reserve "
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The terms of trade improved significantly in 2025 prior to the oil price shock. Continued exchange rate crawl has contributed to a depreciation of the real effective exchange rate. Remittances surged in 2025... ..... contributing to a strengthening of reserve "
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Continued exchange rate crawl has contributed to a depreciation of the real effective exchange rate. Remittances surged in 2025... ..... contributing to a strengthening of reserve buffers. Sources: BCH; Haver Analytics; IMF World Economic Outlook; INE survey; "
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "..... contributing to a strengthening of reserve buffers. Sources: BCH; Haver Analytics; IMF World Economic Outlook; INE survey; and IMF staff estimates. Figure 3. Honduras: Fiscal Developments Fiscal discipline has been maintained after the pandemic... ...wit"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: BCH; Haver Analytics; IMF World Economic Outlook; INE survey; and IMF staff estimates. Figure 3. Honduras: Fiscal Developments Fiscal discipline has been maintained after the pandemic... ...with the central government deficit contained in 2025. The pr"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Honduras: Fiscal Developments Fiscal discipline has been maintained after the pandemic... ...with the central government deficit contained in 2025. The primary balance outperformed in 2025 as capital expenditure slowed... ...while tax revenues slight"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The primary balance outperformed in 2025 as capital expenditure slowed... ...while tax revenues slightly decreased as a percent of GDP. Compressed bond spreads supported external issuance in 2024 and reopening the sustainable Eurobond in 2025. Sources: Ministr"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Compressed bond spreads supported external issuance in 2024 and reopening the sustainable Eurobond in 2025. Sources: Ministry of Finance; Bloomberg; and IMF staff estimates. Public debt has declined since the recovery from the pandemic. Figure 4. Honduras: Mon"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Public debt has declined since the recovery from the pandemic. Figure 4. Honduras: Monetary and Financial Sector Developments The policy rate increases of 2024 transmitted to interbank rates. While policy rate in Honduras is high relative to the region, recent"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Honduras: Monetary and Financial Sector Developments The policy rate increases of 2024 transmitted to interbank rates. While policy rate in Honduras is high relative to the region, recent pickup in inflation has lowered the real rate. The central ban"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "tracked the observed exchange rate well for nearly a decade, it diverged beginning in 2020, reaching a peak divergence in 2024 of about 9 percent. Since exchange rate crawl restarted in late 2024, the divergence has largely closed, reaching about 2 percent in "
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Annex IV. Recent Developments in the Foreign Exchange Auction 1. The rates of allocation of foreign exchange (FX) in the Central Bank of Honduras (BCH) auction have improved markedly since late 2024. After the BCH suspended the interbank FX market and reint"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: Central Bank of Honduras; and IMF staff calculations. 3. As supply and demand have converged, price discovery has begun in the FX auction. Under the crawling band exchange rate regime, the BCH sets the \"base price\" on a weekly basis, which determines "
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "resilient, even under severe stress scenarios combining an economic slowdown, weaker credit growth, higher commodity prices, and lower remittance inflows. Text Figure 1. Honduras: Public and Publicly Guaranteed Debt 1/ (Percent of GDP) Sources: Country authori"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "7. The NIIP series was revised by the BCH to incorporate improved coverage. The NIIP series was revised to incorporate methodological and coverage improvements in foreign direct investment liabilities and private nonfinancial external debt, led by the Central "
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "the public financial sector. These obligations are expected to be met through a combination of rollover operations and regular market issuance, in line with the authorities' debt management strategy to smooth the redemption profile and mitigate refinancing ris"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "• Consistency between public investment and growth. The contribution of public investment to real GDP growth remains marginal across the previous and current DSA. Public investment is expected to remain at around 4 percent of GDP in the medium term. ## COUNTRY"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "16. Market-financing risk indicators suggest low liquidity risks (Figure 5). The maximum gross financing needs over a 3-year period under the baseline projection horizon are expected to be around 7 percent of GDP, well below the benchmark value of 14 percent. "
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "3/ Includes official and private transfers and FDI. Figure 1. Honduras: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026-36 Baseline - Historical scenario"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "3/ Includes official and private transfers and FDI. Figure 1. Honduras: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026-36 Baseline - Historical scenario"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Honduras: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026-36 Baseline - Historical scenario"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Honduras: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026-36 Baseline - Historical scenario Note: \"Yes\" indicates any change to the size or interactions of the default settings for the stress tests. \"n.a.\""
  },
  {
    "figure_id": "F048",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections. 1/ The most extreme str"
  },
  {
    "figure_id": "F049",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt are based on baseline 10-year projections. 1/ The most extreme str"
  },
  {
    "figure_id": "F050",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "1/ The most extreme stress test is the test that yields the highest ratio in or before 2036. The stress test with a one-off breach is also presented (if any), while the one-off breach is deemed away for mechanical signals. When a stress test with a one-off bre"
  },
  {
    "figure_id": "F051",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ The most extreme stress test is the test that yields the highest ratio in or before 2036. The stress test with a one-off breach is also presented (if any), while the one-off breach is deemed"
  },
  {
    "figure_id": "F052",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Honduras: Drivers of Debt Dynamics—Baseline Scenario Gross Nominal PPG External Debt (In percent of GDP; DSA vintages) Debt-Creating Flows (Percent of GDP) Unexpected Changes in Debt 1/ (Past 5 years, percent of GDP) 1/ Difference between anticipa"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Unexpected Changes in Debt 1/ (Past 5 years, percent of GDP) 1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively low private external debt for average "
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively low private external debt for average low-income countries, a ppt change in PPG external debt shoul"
  },
  {
    "figure_id": "F055",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively low private external debt for average low-income countries, a ppt change in PPG external debt should be largely explained by the drivers of the external debt dynamics equatio"
  },
  {
    "figure_id": "F056",
    "report_id": "R002",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Figure 4. Honduras: Realism Tools 3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is fou"
  },
  {
    "figure_id": "F057",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is found on the horizontal axis; the percent of sample is found on the vertical axis. Fiscal Adjustment and"
  },
  {
    "figure_id": "F058",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Public and Private Investment Rates (Percent of GDP) Contribution to Real GDP Growth (Percent, 5-year average) Figure 5. Honduras: Market Financing Risk Indicators 1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads "
  },
  {
    "figure_id": "F059",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Contribution to Real GDP Growth (Percent, 5-year average) Figure 5. Honduras: Market Financing Risk Indicators 1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data."
  },
  {
    "figure_id": "F060",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Honduras: Market Financing Risk Indicators 1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections."
  },
  {
    "figure_id": "F061",
    "report_id": "R002",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Honduras: Market Financing Risk Indicators 1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections."
  },
  {
    "figure_id": "F062",
    "report_id": "R002",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "1/ Maximum gross financing needs (GFN) over 3-year baseline projection horizon. 2/ EMBI spreads correspond to the latest available data. Sources: Country authorities; and staff estimates and projections. Historical realizations"
  },
  {
    "figure_id": "F063",
    "report_id": "R002",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. Historical realizations"
  },
  {
    "figure_id": "F064",
    "report_id": "R002",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. Historical realizations Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023 As a ratio t"
  },
  {
    "figure_id": "F065",
    "report_id": "R002",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. Historical realizations Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023 As a ratio t"
  },
  {
    "figure_id": "F066",
    "report_id": "R002",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Historical realizations Median of average projected values over the first five years of the forecast period across countries using the LIC DSF with non-zero domestic debt, end-2023 As a ratio to domestic debt stock in prev. year (RHS) Sources: Country authorit"
  },
  {
    "figure_id": "F067",
    "report_id": "R002",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：洪都拉斯通过了压力测试，但能源补贴仍是最大隐患｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F068",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Change in Real Value Added by Sector (Percentage points) integration, including the Savings and Investment Union, would strengthen Luxembourg's growth prospects. 49. It is proposed that the next Article IV consultation with Luxembourg takes place on the standa"
  },
  {
    "figure_id": "F069",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1. Luxembourg: Real Sector Sources: STATEC and IMF staff calculations. Note: Non-market activities refer to public sector activities. Investment Contribution to Real GDP Growth (Percent year over year, contributions in percentage points) 2023Q3 2023Q"
  },
  {
    "figure_id": "F070",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: STATEC and IMF staff calculations. Note: Non-market activities refer to public sector activities. Investment Contribution to Real GDP Growth (Percent year over year, contributions in percentage points) 2023Q3 2023Q4 2024Q1 2024Q2 2024Q3 2024Q4 2025Q1 "
  },
  {
    "figure_id": "F071",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "2023Q3 2023Q4 2024Q1 2024Q2 2024Q3 2024Q4 2025Q1 2025Q2 2025Q3 2025Q4 Sources: Haver Analytics, EC and IMF staff calculations. GDP Evolution, by Sector Value Added by the Financial Sector (Index, 2015=100) Domestic Employment Growth (Percent, quarter over quar"
  },
  {
    "figure_id": "F072",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Value Added by the Financial Sector (Index, 2015=100) Domestic Employment Growth (Percent, quarter over quarter, seasonally adjusted) Figure 2. Luxembourg: Labor Market Sources: STATEC and IMF staff calculations. Sources: Central Service of Statistics and Econ"
  },
  {
    "figure_id": "F073",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Domestic Employment Growth (Percent, quarter over quarter, seasonally adjusted) Figure 2. Luxembourg: Labor Market Sources: STATEC and IMF staff calculations. Sources: Central Service of Statistics and Economic Studies and IMF staff calculations. Figure 3. Lux"
  },
  {
    "figure_id": "F074",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Domestic Employment Growth (Percent, quarter over quarter, seasonally adjusted) Figure 2. Luxembourg: Labor Market Sources: STATEC and IMF staff calculations. Sources: Central Service of Statistics and Economic Studies and IMF staff calculations. Figure 3. Lux"
  },
  {
    "figure_id": "F075",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Luxembourg: Labor Market Sources: STATEC and IMF staff calculations. Sources: Central Service of Statistics and Economic Studies and IMF staff calculations. Figure 3. Luxembourg: Inflation Sources: STATEC and IMF staff calculations."
  },
  {
    "figure_id": "F076",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Central Service of Statistics and Economic Studies and IMF staff calculations. Figure 3. Luxembourg: Inflation Sources: STATEC and IMF staff calculations. Figure 4. Luxembourg: Fiscal Sector General Government: Total Revenue (Percent of GDP)"
  },
  {
    "figure_id": "F077",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Central Service of Statistics and Economic Studies and IMF staff calculations. Figure 3. Luxembourg: Inflation Sources: STATEC and IMF staff calculations. Figure 4. Luxembourg: Fiscal Sector General Government: Total Revenue (Percent of GDP) Contribut"
  },
  {
    "figure_id": "F078",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Sources: STATEC and IMF staff calculations. Figure 4. Luxembourg: Fiscal Sector General Government: Total Revenue (Percent of GDP) Contribution to Real Revenue Growth (Percent, adjusted by GDP Deflator) General Government: Total Expenditure (Percent of GDP) Co"
  },
  {
    "figure_id": "F079",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Sources: STATEC and IMF staff calculations. Figure 4. Luxembourg: Fiscal Sector General Government: Total Revenue (Percent of GDP) Contribution to Real Revenue Growth (Percent, adjusted by GDP Deflator) General Government: Total Expenditure (Percent of GDP) Co"
  },
  {
    "figure_id": "F080",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Luxembourg: Fiscal Sector General Government: Total Revenue (Percent of GDP) Contribution to Real Revenue Growth (Percent, adjusted by GDP Deflator) General Government: Total Expenditure (Percent of GDP) Contribution to Real Expenditure Growth (Perce"
  },
  {
    "figure_id": "F081",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Contribution to Real Expenditure Growth (Percent, adjusted by GDP Deflator) Central Government Fiscal Aggregates and Tax Base (Index 2015=100) CIT from Financial Sector (Percent of GDP) Sources: EBA and Financial Soundness Indicator Database. Sources: EBA and "
  },
  {
    "figure_id": "F082",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sources: EBA and Financial Soundness Indicator Database. Sources: EBA and Financial Soundness Indicator Database. Figure 5. Luxembourg: Banking Sector Tier 1 Capital Ratio (Percent) Return on Equity (Percent) Tier 1 Capital Ratio (Percent)"
  },
  {
    "figure_id": "F083",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sources: EBA and Financial Soundness Indicator Database. Sources: EBA and Financial Soundness Indicator Database. Figure 5. Luxembourg: Banking Sector Tier 1 Capital Ratio (Percent) Return on Equity (Percent) Tier 1 Capital Ratio (Percent) Liquidity Coverage R"
  },
  {
    "figure_id": "F084",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Luxembourg: Banking Sector Tier 1 Capital Ratio (Percent) Return on Equity (Percent) Tier 1 Capital Ratio (Percent) Liquidity Coverage Ratio (Percent)"
  },
  {
    "figure_id": "F085",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Return on Equity (Percent) Tier 1 Capital Ratio (Percent) Liquidity Coverage Ratio (Percent) ## Figure 6. Luxembourg: External Sector"
  },
  {
    "figure_id": "F086",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Return on Equity (Percent) Tier 1 Capital Ratio (Percent) Liquidity Coverage Ratio (Percent) ## Figure 6. Luxembourg: External Sector Q4-2002 Q4-2006 Q4-2010 Q4-2014 Q4-2018 Q4-2022 Q4-2025"
  },
  {
    "figure_id": "F087",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Tier 1 Capital Ratio (Percent) Liquidity Coverage Ratio (Percent) ## Figure 6. Luxembourg: External Sector Q4-2002 Q4-2006 Q4-2010 Q4-2014 Q4-2018 Q4-2022 Q4-2025 Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations."
  },
  {
    "figure_id": "F088",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Liquidity Coverage Ratio (Percent) ## Figure 6. Luxembourg: External Sector Q4-2002 Q4-2006 Q4-2010 Q4-2014 Q4-2018 Q4-2022 Q4-2025 Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations. Sources: Haver Analytics, Central Bank of Luxem"
  },
  {
    "figure_id": "F089",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Figure 6. Luxembourg: External Sector Q4-2002 Q4-2006 Q4-2010 Q4-2014 Q4-2018 Q4-2022 Q4-2025 Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations. Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations. F"
  },
  {
    "figure_id": "F090",
    "report_id": "R003",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Q4-2002 Q4-2006 Q4-2010 Q4-2014 Q4-2018 Q4-2022 Q4-2025 Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations. Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations. Figure 7. Luxembourg: Structural Sector Lu"
  },
  {
    "figure_id": "F091",
    "report_id": "R003",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Sources: Haver Analytics, Central Bank of Luxembourg and IMF staff calculations. Figure 7. Luxembourg: Structural Sector Luxembourg Linkdeln Hiring Rate (Percent, SA) Sources: Luxembourg authorities; IMF staff estimates and projections. 1/ Contribution to GDP "
  },
  {
    "figure_id": "F092",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Annex IV. Sovereign Risk and Debt Sustainability Analysis Debt by Currency (Percent of GDP) Note: The perimeter shown is general government. Public Debt by Holder (Percent of GDP) Note: The perimeter shown is general government. Public Debt by Governing Law, 2"
  },
  {
    "figure_id": "F093",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Debt by Currency (Percent of GDP) Note: The perimeter shown is general government. Public Debt by Holder (Percent of GDP) Note: The perimeter shown is general government. Public Debt by Governing Law, 2025 (Percent) Note: The perimeter shown is general governm"
  },
  {
    "figure_id": "F094",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: The perimeter shown is general government. Public Debt by Governing Law, 2025 (Percent) Note: The perimeter shown is general government. Debt by Instruments (Percent of GDP) Public Debt by Maturity (Percent of GDP) Note: The perimeter shown is general go"
  },
  {
    "figure_id": "F095",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Public Debt by Governing Law, 2025 (Percent) Note: The perimeter shown is general government. Debt by Instruments (Percent of GDP) Public Debt by Maturity (Percent of GDP) Note: The perimeter shown is general government. Note: The perimeter shown is general go"
  },
  {
    "figure_id": "F096",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: The perimeter shown is general government. Annex IV. Figure 4. Luxembourg: Baseline Scenario (Percent of GDP unless indicated otherwise) Contribution to Change in Public Debt %GDP); lines, avg marginal interest rates (LHS, percent)) (Lines, real growth u"
  },
  {
    "figure_id": "F097",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Annex IV. Figure 4. Luxembourg: Baseline Scenario (Percent of GDP unless indicated otherwise) Contribution to Change in Public Debt %GDP); lines, avg marginal interest rates (LHS, percent)) (Lines, real growth using multiplier (LHS); bars, fiscal adj. (RHS)) A"
  },
  {
    "figure_id": "F098",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "%GDP); lines, avg marginal interest rates (LHS, percent)) (Lines, real growth using multiplier (LHS); bars, fiscal adj. (RHS)) Annex IV. Figure 5. Luxembourg: Realism of Baseline Assumptions Historical Output Gap Revisions 2/ Public Debt Creating Flows 3-Year "
  },
  {
    "figure_id": "F099",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "%GDP); lines, avg marginal interest rates (LHS, percent)) (Lines, real growth using multiplier (LHS); bars, fiscal adj. (RHS)) Annex IV. Figure 5. Luxembourg: Realism of Baseline Assumptions Historical Output Gap Revisions 2/ Public Debt Creating Flows 3-Year "
  },
  {
    "figure_id": "F100",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Regulatory balance. Implement AI regulation in a risk-based and proportionate manner, preserving trust and safety while avoiding unnecessary barriers to productivity-enhancing adoption, particularly in high-value service sectors. Overall, AI provides Luxemb"
  },
  {
    "figure_id": "F101",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Overall, AI provides Luxembourg a promising opportunity to lift productivity and sustain growth, but realizing these gains will require proactive policies to manage labor-market transitions and ensure that benefits are broadly shared. ## Annex VI. Figure 1. Lu"
  },
  {
    "figure_id": "F102",
    "report_id": "R003",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：卢森堡的“低债务幻觉”正在被赤字吞噬｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "\\- In casualty, it’s an assessment of claims, legal, and reserve patterns that point to a renewal action, tighter terms, or a different attachment point. \\- In workers' compensation, it compares declared payroll, class mix, field safety information, and true l"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：商业财产险的下一场战役，不在承保，在组合管理｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F105",
    "report_id": "R005",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：零售银行真正的AI红利，不在降本，而在重新定义客户关系｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F106",
    "report_id": "R006",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Most food and beverage companies have long pursued a strategy that prioritized scale and marketing muscle. The bet was that size and strength could keep heritage brands relevant without breakthrough product and ingredient innovation. These companies put their "
  },
  {
    "figure_id": "F107",
    "report_id": "R006",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "\\- An increasing array of digital- and AI-enabled shopping apps and interfaces These trends are not abating; in fact, they are picking up speed and catalyzing other market forces. UPF categories, which play an outsized role for most major CPG manufacturers, ha"
  },
  {
    "figure_id": "F108",
    "report_id": "R006",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Sources: NielsenIQ data; Babak Ravandi et al., \"Prevalence of processed foods in major US grocery stores,\" Nature Food, January 13, 2025; BCG analysis. Note: Highly processed according to FPro (Food Processing) score. Across multiple categories, large brands c"
  },
  {
    "figure_id": "F109",
    "report_id": "R006",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "## How Companies Can Adapt The big strategic question involves capital allocation. For the past decade, returning free cash flow to shareholders through dividends and buybacks has been the default value creation tool for many large CPG companies. This model wo"
  },
  {
    "figure_id": "F110",
    "report_id": "R006",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：CPG巨头正在为“研发失落的十年”买单｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F111",
    "report_id": "R007",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Regional patterns reflect these shifts. While the US continues to dominate in scale and mega-cap concentration, Asia remains overrepresented among top-performing companies, and Europe lags despite signs of stabilization. ## Industry Is Not Destiny While the se"
  },
  {
    "figure_id": "F112",
    "report_id": "R007",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 3 In the Long Run, High-Quality Growth Is Essential for Value Creation Sources of TSR for top-quartile performers among industrial businesses, 2005–2025 (%) Sources: S&P Capital IQ, BCG ValueScience® Center. Note: Top quartile of the 2026 BCG Value "
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：价值创造领导力已从科技转向重资产，这不是短期波动｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F114",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "The US strategy can best be described as winning through scale. In practice, this has meant an acceleration in capital deployment over the past 18 months, with the center of gravity shifting from frontier model development toward the data center infrastructure"
  },
  {
    "figure_id": "F115",
    "report_id": "R008",
    "label": "EXHIBIT 2",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 2 AI VC investment $^{1}$ (2023–2026 YTD, \\$B) Tech company R&D spend $^{2}$ (2024, \\$B) AI lab valuation $^{3}$ (2025–2026 YTD, \\$B) $^{3}$ Values for China based on PitchBook data as baseline plus consideration for the government's role as VC inve"
  },
  {
    "figure_id": "F116",
    "report_id": "R008",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "AI VC investment $^{1}$ (2023–2026 YTD, \\$B) Tech company R&D spend $^{2}$ (2024, \\$B) AI lab valuation $^{3}$ (2025–2026 YTD, \\$B) $^{3}$ Values for China based on PitchBook data as baseline plus consideration for the government's role as VC investor based on"
  },
  {
    "figure_id": "F117",
    "report_id": "R008",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "What's new is the sheer scale of spending by US tech giants on the infrastructure to serve those models: CAPEX by the top technology companies surpassed \\$400 billion in 2025—compared with \\$63 billion in China—and is estimated to exceed \\$800 billion in 2026."
  },
  {
    "figure_id": "F118",
    "report_id": "R008",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "## The US Speeds Ahead on Tech CAPEX Tech CAPEX (TOP 20 TECH COMPANIES BY COUNTRY, \\$B) Tech CAPEX intensity (TOP 20 TECH COMPANIES BY COUNTRY, CAPEX TO REVENUE RATIO) $^{1}$ Note: US companies are Apple, Microsoft, NVIDIA, Amazon, Meta, Alphabet, Broadcom, Sa"
  },
  {
    "figure_id": "F119",
    "report_id": "R008",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Note: US companies are Apple, Microsoft, NVIDIA, Amazon, Meta, Alphabet, Broadcom, Salesforce, Oracle, Adobe, ServiceNow, Accenture, IBM, AMD, Cisco, Qualcomm, Texas Instruments, Danaher, Intuit, Palantir; Chinese companies are Tencent, CATL, NetEase, Luxshare"
  },
  {
    "figure_id": "F120",
    "report_id": "R008",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "This shift is premised on China’s ability to remain competitive at the level of foundation models despite its limited access to the highest-end computing power. Indeed, since the release of DeepSeek R1 in January 2025, top-performing Chinese models have kept u"
  },
  {
    "figure_id": "F121",
    "report_id": "R008",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Epoch AI; Artificial Analysis; BCG Institute analysis. $^{1}$ Assuming 3 to 1 ratio of input to output tokens, which are differently priced. China has stayed close to the US on model quality benchmarks while making its models multiple times cheaper th"
  },
  {
    "figure_id": "F122",
    "report_id": "R008",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "This trend may accelerate the bifurcation of AI technologies all the way down to the hardware layer. More cost-efficient Chinese models running on cheaper Chinese chips could become an attractive package for any country looking to deploy AI affordably. China’s"
  },
  {
    "figure_id": "F123",
    "report_id": "R008",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Share of AI patents filed $^{1}$ (2020–2024) manufacturing, services, public administration, and everyday life, with policy goals of more than 70% penetration of AI-enabled “intelligent terminals” and agents by 2027 and more than 90% by 2030. Robotics is one o"
  },
  {
    "figure_id": "F124",
    "report_id": "R008",
    "label": "Exhibit 8",
    "figure_type": "source_exhibit",
    "context": "The rest of the world is paying close attention to the development of the US and Chinese stacks. For most countries, decisions are focused on which layers of the stack to procure or even allow from which companies (and, by implication, the superpowers with whi"
  },
  {
    "figure_id": "F125",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 9 ## The EU Is Strongest Among Middle Powers $^{1}$ The chart is not evenly scaled to the versions in Exhibit 1 and Exhibit 8, as each dimension is independently reindexed to the highest value in our dataset excluding the US and China. The EU is pri"
  },
  {
    "figure_id": "F126",
    "report_id": "R008",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：中美AI正在分裂世界，企业必须选边站｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]