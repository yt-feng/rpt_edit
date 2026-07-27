你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/77a141bbe8f97c634c21c4edd78cb6b200a3efc6a91634e37c693d5aab461e81.jpg)

ADB Green and Blue Bonds Newsletter

ISSUE No. 11 | July 2026

In this issue: CHALLENGES • HIGHLIGHTS • CASE STUDIES

"We greatly value the strong and consistent support of our investors for our green and blue bond program, enabling us to mobilize more than \$15 billion over the past decade. This enduring partnership provides additional resources as we scale up investments to strengthen climate resilience, reduce disaster risks, and address environmental degradation."

—Tobias Hoschka, ADB Treasurer

“ADB’s blue and green bonds facilitate private capital towards the region’s most pressing climate, nature, and environmental needs. From our green bond for glacier awareness to our wider portfolio supporting themes such as clean energy, ocean health, and climate-resilient and nature-positive infrastructure, these instruments enable ADB to translate finance into investable solutions and drive resilient, sustainable growth across Asia and the Pacific.”

—Yevgeniy Zhukov, ADB Director General for Climate Change and Sustainable Development

## Growing the Market for Green and Blue Investment

Discussions on global climate and nature finance are entering a decisive phase as economies transition from commitment to implementation under their post-2025 climate and biodiversity frameworks. In Asia and the Pacific, the stakes are most critical. The region remains as a major driver for global growth and among the world's most vulnerable to climate impacts, highlighting the need for long-term capital flows supporting climate and nature-positive investments.

In 2025, global climate records continued to break, with the year confirmed as one of the 3 warmest years ever recorded. According to the World Meteorological Organization, global average surface temperatures in 2025 reached 1.4°C above the 1850–1900 average,

ADB's Commitment to Nature-Positive Finance  
![](images/804a41a5e4528b291baede356c7ba736f92a30caeb101f6caa716ca20cd2853e.jpg)  
COP26 = 26th UN Climate Change Conference of the Parties.
Source: Asian Development Bank (ADB).

marking the years 2023 to 2025 as the warmest 3-year period on record. $^{1}$ This global trend is mirrored across Asia and the Pacific where extreme heat and weather events persisted through 2025. In Southeast Asia and South Asia, heat waves were earlier than usual and lasted longer, causing school closure, severe health risks, and widespread disruptions across multiple countries. $^{2}$ Based on Asian Development Bank (ADB) estimates, climate change could trigger a 17% decline in gross domestic product across Asia and the Pacific by 2070, potentially reaching 41% by the end of the century. $^{3}$ This underscores the escalating economic risks associated with worsening climate, and the necessity of scaling climate finance, especially for adaptation.

Building on the New Collective Quantified Goal to deliver \$300 billion in annual climate finance for developing countries, the 30th United Nations Climate Change Conference of the Parties (COP30) in Belém, Brazil adopted the Global Mutirão Decision. $^{4}$ This landmark agreement commits to mobilizing \$1.3 trillion in climate finance annually by 2035 and launches a 2-year work program to strengthen climate finance implementation.

The financing gap for nature continues to widen. While the 16th Conference of the Parties for the Convention on Biological Diversity (CBD COP16) successfully established the Cali Fund, a Bloomberg report released ahead of the 2024 summit estimated that \$942 billion is needed annually to halt and reverse the ongoing decline in biodiversity. $^{5}$ To help address this issue, ADB is scaling up the Nature Solutions Finance Hub (NSFH). With the approval of the Natural Capital Fund, funded by the Global Environment Facility (GEF), ADB expects significant progress in nature finance throughout 2025, aligning with the Environment Action Plan launched in November 2024.

To facilitate market expansion for blue finance, ADB has partnered with other leading institutions: International Capital Market Association, United Nations Global Compact, United Nations Environment Programme Finance Initiative, and International Finance Corporation. This collaboration led to ADB's issuance of the guidance document, Bonds to Finance the Sustainable Blue Economy: A Practitioner's Guide. The guide builds on existing market standards that underpin the global sustainable bond markets and provides market consistency and transparency in financing the blue economy.

ADB continues to seek innovative financial solutions, and issuing thematic bonds is one way to broaden its investment base and grow local bond markets. In 2024, during CBD COP16 in Cali, Colombia, ADB issued its first biodiversity and nature theme bond for \$100 million. The bond will finance nature-based solutions, including biodiversity protection, nature mainstreaming, and livelihood support.

## Expanding Climate Finance Pathways Through the Glaciers to Farms Program

At COP30 in Belém, the Asian Development Bank and the Green Climate Fund (GCF) formalized the Glaciers to Farms (G2F) Regional Program. The program mobilizes \$3.5 billion in total financing—including \$250 million in grants and concessional finance from the GCF—to support climate-resilient development in Central and West Asia.

The G2F Program supports governments in addressing accelerating climate risks across agriculture, water, health, and social protection sectors in one of the world's fastest-warming regions. It does so by strengthening the capacity of key ministries for climate-informed public investment planning, advancing the development of bankable adaptation projects, and piloting innovative financing instruments such as outcome-based resilience bonds.

The program also strengthens the enabling environment for climate finance through targeted mentoring for financial institutions and agricultural enterprises, including micro, small, and medium-sized enterprises. It also promotes regional cooperation through a knowledge platform and the Glaciers Community of Practice to address shared risks such as glacier melt and water scarcity.

## Building Momentum to Scale Climate Finance

ADB continues to demonstrate long-term commitment and leadership in climate action, with an updated target for its climate finance to reach 50% of its total annual committed financing volume by 2030. At COP30, ADB and other multilateral development banks (MDBs) issued a joint statement reaffirming their collective commitment to work as a system and help client economies build resilient, economically sound development pathways in the face of intensified climate shocks and ecosystem degradation. $^{6}$

ADB's Climate Change Action Plan 2023–2030 (CCAP) continues to guide the expansion of the institution's climate operations. This growth is driven by robust climate finance mobilization, deeper integration of climate across operations, enhanced collaboration across ADB, and strengthened strategic external partnerships.

In 2025, ADB committed \$13.5 billion in climate finance from its resources—about 51% of its total committed financing. This included \$8.8 billion for mitigation and \$4.5 billion for adaptation, and marked a significant increase from the \$11.1 billion in climate finance achieved in 2024. Of the \$13.5 billion, private sector operations contributed \$1.6 billion. From 2019 to 2025, ADB committed \$55.4 billion in cumulative climate finance from its resources. Furthermore, in line with its

2021 commitment. Since 2023, all projects that ADB approved were assessed and confirmed as aligned with the Paris Agreement.

Complementing the CCAP, ADB is implementing its Disaster Risk Management Action Plan 2024–2030 and Environmental Action Plan 2024–2030. Together, these action plans strengthen direction and provide an integrated platform to address the triple planetary crisis of biodiversity loss, climate change, and pollution in a coherent, coordinated manner.

## Blue Bonds

In 2021, ADB expanded its green bond framework to include blue bonds for ocean health investments, setting a new replicable market standard for blue financing. $^{7}$ The Green and Blue Bond Framework is underpinned by ADB's Ocean Finance Framework, which aligns with the International Capital Market Association's Green Bond Principles and the Sustainable Blue Economy Finance Principles, of which ADB is a signatory. ADB's inclusion criteria for eligible investments have been independently verified by the Center for International Climate and Environmental Research – Oslo Shades of Green (CICERO), which assigned the new green and blue bond framework as CICERO Medium Green. $^{8}$

The expansion supports ADB's Action Plan for Healthy Oceans and Sustainable Blue Economies, which has three priorities:

• to conserve and restore critical marine habitats and species,

• to reduce marine pollution, and

• to build blue economies.

Based on this framework, ADB has issued about \$612 million of blue bonds denominated in Australian dollar, New Zealand dollar, and Swedish krona.

## Green Bonds

ADB continues to help finance climate change mitigation and adaptation projects, raising about \$15 billion since the launch of its green bond program in 2015. ADB's green bond issuances have been diverse, with transactions printed across currencies that include the Australian dollar, Brazilian real, Canadian dollar, euro, Georgian lari, Ghanaian cedi, Hong Kong dollar, Indian rupee, Kazakhstan tenge, Mexican peso, Nigerian naira, Norwegian krone, Peruvian sol, pound sterling, South African rand, Swedish krona, Turkish lira, Ukrainian hryvnia, and US dollar.

## Eligible Project Selection Criteria

Green bonds have proven to be an effective tool for promoting ADB's strategic priorities on climate change, as outlined in the Operational Plan for Strategy 2030. These priorities include climate change mitigation, climate and disaster resilience, and environmental sustainability.

Climate change mitigation projects include those in the following sectors:

\- renewable energy (i.e., solar, wind, geothermal, and small hydropower with capacity below 20 megawatts),

• energy efficiency, and

• sustainable transport (excluding roads).

Climate change adaptation projects include those in the following sectors:

• energy infrastructure resilience,

• water supply and other urban infrastructure and services,

• sustainable transport, and

agriculture.

Eligible blue bonds are funded, in whole or in part, by ADB projects that contribute to ocean health. The distance from the project to the ocean is considered as a secondary screening criterion, as appropriate. Examples of blue bond projects typically include, but are not limited to, the following sectors:

## Ecosystem and Natural Resources Management

\- Ecosystem management and natural resources restoration

• Sustainable fisheries management

• Sustainable aquaculture

## Pollution Control

• Solid waste management

• Resource efficiency and circular economy

• Nonpoint source pollution

• Wastewater management

## Sustainable Coastal and Marine Development

\- Ports and shipping

• Marine renewable energy

Eligible projects for green and blue bond financing are continually identified by ADB energy, climate change, and environmental specialists. For green bonds, this process follows the joint MDB approach to tracking and reporting climate change mitigation and adaptation finance, along with additional selection criteria for “green” projects that deliver environmentally sustainable growth. For blue bonds, eligible projects consider the selection criteria, including the project’s classification to identify “blue” projects. These criteria are defined by ADB’s Green and Blue Bond Framework.

## Use of Proceeds

Net proceeds from green and blue bonds are allocated within ADB's treasury to special subportfolios linked to ADB's lending operations for eligible projects. While the green and blue bonds are outstanding, the balances of these subportfolios are reduced at the end of each quarter with respect to eligible projects. Pending such disbursements, the subportfolios are invested in liquid instruments, in accordance with ADB's liquidity policy.

ADB Green Bond Commitment by Country, as of 31 December 2025

![](images/56b595af4f38713d8941c349f4a799aaf3750cac96de6c7c4c17f87bea2496f8.jpg)  
Source: Asian Development Bank estimates.  
ADB Green Bond Commitment by Sector, as of 31 December 2025
(%)

![](images/392a0c0614221c44e0975d0a024a386b839c2e8e43a2d7564a1e2ecbe995b3a3.jpg)  
Source: Asian Development Bank estimates.  
ADB Blue Bond Commitment by Country, as of 31 December 2025

![](images/59ccc3f0cb54d77c53af6b1ae61b542470290bbf644c4212dfccf4016f2ee511.jpg)  
Source: Asian Development Bank estimates.

ADB Blue Bond Commitment by Objective, as of 31 December 2025
(%)  
![](images/bb5b16a46185b87f1d0b6da6c2842b05493b5f240eaf4f069b0c88f65c17ce6d.jpg)  
Source: Asian Development Bank estimates.

Outstanding Green Bond Issuances as of 31 December 2025

<table><tr><td>Format</td><td>Issue Date</td><td>Maturity Date</td><td>Issue Size</td></tr><tr><td>Global</td><td>16 August 2016a</td><td>14 August 2026</td><td>$600,000,000</td></tr><tr><td>Private Placement</td><td>30 March 2017</td><td>30 March 2027</td><td>$50,000,000</td></tr><tr><td>Global</td><td>10 August 2017</td><td>10 August 2027</td><td>$500,000,000</td></tr><tr><td>Private Placement</td><td>15 November 2017</td><td>15 November 2027</td><td>A$25,000,000</td></tr><tr><td>Private Placement</td><td>26 January 2018</td><td>26 January 2028</td><td>SKr250,000,000</td></tr><tr><td>Global</td><td>26 September 2018</td><td>26 September 2028</td><td>$750,000,000</td></tr><tr><td>Private Placement</td><td>8 July 2019b</td><td>8 July 2026</td><td>SKr4,900,000,000</td></tr><tr><td>Public Offering</td><td>18 September 2019c</td><td>18 March 2030</td><td>A$220,000,000</td></tr><tr><td>Public Offering</td><td>18 October 2019</td><td>15 September 2026</td><td>£250,000,000</td></tr><tr><td>Public Offering</td><td>24 October 2019</td><td>24 October 2029</td><td>€750,000,000</td></tr><tr><td>Private Placement</td><td>30 January 2020</td><td>30 January 2053</td><td>€40,000,000</td></tr><tr><td>Private Placement</td><td>22 July 2020</td><td>22 July 2030</td><td>$50,000,000</td></tr><tr><td>Private Placement</td><td>13 October 2020</td><td>13 October 2028</td><td>SKr500,000,000</td></tr><tr><td>Private Placement</td><td>21 January 2021d</td><td>21 January 2028</td><td>SKr1,500,000,000</td></tr><tr><td>Private Placement</td><td>2 February 2021</td><td>2 February 2051</td><td>€35,000,000</td></tr><tr><td>Private Placement</td><td>5 February 2021</td><td>5 February 2026</td><td>BRL400,000,000</td></tr><tr><td>Public Offering</td><td>10 February 2021</td><td>10 February 2026</td><td>Can$1,250,000,000</td></tr><tr><td>Private Placement</td><td>18 February 2021</td><td>18 February 2061</td><td>$50,000,000</td></tr><tr><td>Private Placement</td><td>23 February 2021</td><td>23 February 2051</td><td>€40,000,000</td></tr><tr><td>Private Placement</td><td>24 February 2021</td><td>24 February 2061</td><td>€50,000,000</td></tr><tr><td>Private Placement</td><td>4 March 2021</td><td>4 March 2051</td><td>€35,000,000</td></tr><tr><td>Public Offering</td><td>16 June 2023</td><td>16 June 2028</td><td>SKr1,000,000,000</td></tr><tr><td>Public Offering</td><td>10 January 2024</td><td>10 January 2031</td><td>€1,250,000,000</td></tr><tr><td>Private Placement</td><td>1 February 2024</td><td>1 February 2034</td><td>S/40,000,000</td></tr><tr><td>Public Offering</td><td>8 February 2024e</td><td>8 February 2028</td><td>₹20,000,000,000</td></tr><tr><td>Private Placement</td><td>13 May 2024</td><td>13 May 2026</td><td>HK$200,000,000</td></tr><tr><td>Private Placement</td><td>16 May 2024</td><td>16 May 2028</td><td>SKr1,100,000,000</td></tr><tr><td>Public Offering</td><td>5 June 2024</td><td>5 June 2029</td><td>€500,000,000</td></tr><tr><td>Private Placement</td><td>5 September 2024</td><td>5 January 2026</td><td>₹32,000,000,000</td></tr><tr><td>Public Offering</td><td>17 January 2025</td><td>21 January 2027</td><td>T7,644,657,000</td></tr><tr><td>Private Placement</td><td>13 February 2025</td><td>13 February 2030</td><td>TL5,000,000,000</td></tr><tr><td>Private Placement</td><td>24 February 2025</td><td>24 February 2027</td><td>GHS160,000,000</td></tr><tr><td>Private Placement</td><td>26 February 2025</td><td>26 February 2026</td><td>HK$200,000,000</td></tr><tr><td>Private Placement</td><td>16 April 2025</td><td>16 April 2026</td><td>₹32,000,000,000</td></tr><tr><td>Private Placement</td><td>25 April 2025</td><td>25 April 2028</td><td>TL1,000,000,000</td></tr><tr><td>Public Offering</td><td>11 July 2025</td><td>11 July 2028</td><td>€1,000,000,000</td></tr><tr><td>Private Placement</td><td>28 July 2025</td><td>28 July 2026</td><td>HK$100,000,000</td></tr><tr><td>Private Placement</td><td>12 September 2025</td><td>12 September 2028</td><td>HK$780,000,000</td></tr><tr><td>Private Placement</td><td>14 October 2025</td><td>14 October 2031</td><td>A$78,000,000</td></tr><tr><td>Public Offering</td><td>20 October 2025</td><td>20 October 2028</td><td>Can$750,000,000</td></tr><tr><td>Private Placement</td><td>23 October 2025</td><td>23 October 2026</td><td>HK$150,000,000</td></tr></table>

A\$ = Australian dollar, Can\$ = Canadian dollar, € = euro, GHS = Ghanaian cedi, HK\$ = Hong Kong dollar, ₱ = Nigerian naira, R\$ = Brazilian real, ₹ = Indian rupee, S/ = Peruvian sol, £ = pound sterling, SKr = Swedish krona, T = Kazakhstan tenge, TL = Turkish lira, \$ = United States dollar.  
$^{a}$ Reopened on 23 June 2021.  
$^{b}$ Reopened on 30 August 2019, 19 November 2019, 5 February 2020, 15 February 2020, and 16 October 2020.  
$^{c}$ Reopened on 30 January 2020.  
$^{d}$ Reopened on 1 February 2021.  
$^{e}$ Reopened on 21 February 2024.  
Source: Asian Development Bank.

Outstanding Blue Bond Issuances as of 31 December 2025

<table><tr><td>Format</td><td>Issue Date</td><td>Maturity Date</td><td>Issue Size</td></tr><tr><td>Private Placement</td><td>10 September 2021</td><td>10 September 2036</td><td>A$208,000,000</td></tr><tr><td>Private Placement</td><td>10 September 2021</td><td>10 September 2031</td><td>NZ$217,000,000</td></tr><tr><td>Private Placement</td><td>22 November 2023</td><td>22 November 2048</td><td>A$40,000,000</td></tr><tr><td>Private Placement</td><td>18 September 2024</td><td>18 September 2029</td><td>SKr1,000,000,000</td></tr><tr><td>Public Offering</td><td>15 October 2025</td><td>15 October 2030</td><td>SK

[中间内容因长度限制已省略]

e986fd1394fb16d0464a6370.jpg"/></td></tr><tr><td>Pollution control</td><td>Wastewater management</td><td>171.00</td><td>135.00</td><td>101.80</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">People's Republic of China: Fujian Coastal Cities Climate-Resilient Development and Biodiversity Conservation Project (4700/FY2025/NA). Improve urban climate change resilience and biodiversity of two cities in the coastal province of Fujian through (i) enhancing capacity of institutions for coastal climate and biodiversity action, (ii) improving green and gray infrastructure and facilities, and (iii) implementing biodiversity conservation and enhancement measures in coastal mangroves and wetlands.</td><td colspan="8">By 2032:At least 4.4 million people (Fuzhou: 4.1 million, Yunxiao: 0.3 million) in project areas (2.1 million of whom are women; Fuzhou: 2.0 million, Yunxiao: 0.1 million) benefited from improved resilience in infrastructure and ecosystem services, and reduced flood risk and urban heat (2024 baseline: 0).At least 221 ha of intertidal wetland areas (Fuzhou: 154 ha, Yunxiao: 67 ha) and 7-ha mangroves restored and under improved management (Yunxiao), and at least 630 ha transformed into ecological aquaculture and farmland (Fuzhou: 130 ha, Yunxiao: 500 ha) $^b$ (2024 baseline: 0).By 2031:Stormwater detention green space and lakes improved with a detention capacity of at least 263,000  $m^3$  (Yunxiao) (2024 baseline: 0).At least 221 ha of wetlands and waterbird habitat rehabilitated, high-tide roosts created, and invasive plant species removed (Fuzhou: 154 ha, Yunxiao: 67 ha); at least 7 ha of mangrove habitat restored and at least 6.16 km (Yunxiao) of coastline ecologically repaired; and breeding habitat for endangered species (such as Chinese crested tern) on an island (Fuzhou) enhanced (2024 baseline: 0).</td><td rowspan="2">[IMAGE]</td></tr><tr><td>Ecosystem and natural resources management</td><td>Ecosystem management and natural resources restoration</td><td>267.61</td><td>142.25</td><td>79.90</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="5">Total eligibility for green bonds and allocated for water, urban infrastructure, and others</td><td>1,996.90</td><td>689.93</td><td>(68.42)</td><td></td><td></td></tr></table>

ADB = Asian Development Bank, COD = chemical oxygen demand, FY = fiscal year, ha = hectare, kg/hr = kilogram per hour, km = kilometer, kw = kilowatt, mg = milligram, mg/L = milligram/liter, MW = megawatt, $m^{3}$ = cubic meter, NA = not applicable, O&M = operation and maintenance, OP = operational priority.  
a Expected impacts or results are based on ex ante estimates.  
$^{b}$ This is the share of the total project cost financed by ADB and funded by regular ordinary capital resources.  
c This is the amount eligible for blue bond funding on commitment date.  
$^{d}$ This represents the amount of blue bond proceeds allocated for disbursements under the project. A zero (“0”) entry means no disbursements as of 31 December 2025.  
e This represents the amount of reflows. A zero (“0”) entry means no reflows as of 31 December 2025.  
f According to the GB 3838-2002 environmental quality standards for surface water in the People's Republic of China, water rated Class III is suitable for drinking and swimming, Class IV for general industrial and recreational use, and Class V for agriculture and landscaping. Class V+ means that the water is unsuitable for any purpose.  
g Under the eco-compensation scheme between Anhui and Zhejiang provinces, the central government and the two provincial governments have set up an eco-compensation fund, with water quality subject to periodic assessment at the interprovincial section.  
Source: Asian Development Bank.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area, or by using the term “country” in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

## Notes:

“\$” refers to United States dollars and “₹” refers to Indian rupees.
ADB recognizes “Hong Kong” as Hong Kong, China; “Hanoi” as Ha Noi; and “Chittagong” as Chattogram.
All photos by ADB, unless otherwise stated.

On the cover: Wind farm in Georgia. Passengers boarding a Metropolitan Rail System train in Hanoi, Viet Nam. Fisher folk in the Federated States of Micronesia. Female workers at a coffee farm in Cavite, Philippines.

## Investor Relations Contact

Asian Development Bank
Treasury Department, Funding Division
6 ADB Avenue, Mandaluyong City
1550 Metro Manila, Philippines

Email capitalmarkets@adb.org
Investor Website www.adb.org/investors
Bloomberg ADB <GO>
Tel. No. +63 2 8683 1204
Fax No. +63 2 8632 4120
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
