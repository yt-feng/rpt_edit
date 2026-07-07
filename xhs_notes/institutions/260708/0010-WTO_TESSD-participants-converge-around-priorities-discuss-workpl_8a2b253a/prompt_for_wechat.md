你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`世界贸易组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界贸易组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
19 March 2026

(26-2204)

Page: 1/31

Ministerial Conference
Fourteenth Session
Yaoundé, 26-29 March 2026

Original: English

# TRADE AND ENVIRONMENTAL SUSTAINABILITY STRUCTURED DISCUSSIONS (TESSD)

# STATEMENT BY THE TESSD CO-CONVENORS

## Addendum

This addendum includes TESSD: Insights and Outcomes from Five Years of Work – A Co Convenors' Report, accompanying the Statement by the TESSD Co-Convenors circulated in document WT/MIN(26)/22.

TESSD: INSIGHTS AND OUTCOMES FROM FIVE YEARS OF WORK – A CO-CONVENORS' REPORT

## Contents

MESSAGE FROM THE CO-CONVENORS ....3
1 EVOLUTION OF TESSD....4
2 TRADE IN SUPPORT OF CLIMATE AND ENVIRONMENT: INSIGHTS FROM TESSD....7
2.1 Clean energy transition....8
2.2 Decarbonizing industry and transport ....11
2.2.1 Energy-intensive industries (e.g. steel, aluminium, cement, construction and buildings, fertilizers)....11
2.2.2 Transport....13
2.3 Climate adaptation, water management and sustainable agriculture ....16
3 CONCLUDING REFLECTIONS FROM THE CO-CONVENORS ....19
ANNEX I: TRCMS WG OUTCOME DOCUMENT – MAIN ELEMENTS....20
1 COMPILATION AND MAPPING OF TRADE-RELATED CLIMATE POLICIES ....20
1.1 Carbon pricing and Emissions Trading Systems (ETS) ....20
1.2 Border Carbon Adjustments (BCAs) ....20
1.3 Taxes and incentives ....20
1.4 Regulatory measures – standards, certifications and labelling ....20
1.5 Voluntary actions and cooperative initiatives....20
1.6 Trade preferences and sustainability-linked instruments....21

2 AREAS FOR ENHANCING COOPERATION ....21
2.1 Information sharing and dialogue on TrCMs....21
2.2 Fostering convergence on carbon measurement standards....21
2.3 Conformity assessment and certification schemes....21
2.4 Technical assistance and capacity building....21
ANNEX II: SUBSIDIES WG OUTCOME DOCUMENT – COMPILATION OF DESIGN ELEMENTS....23
Rationale and design elements....23
Impact considerations (economic, environmental and social)....24
Implementation and governance considerations....25
ANNEX III: EGS WG OUTCOME DOCUMENT – KEY INSIGHTS....26
ANNEX IV: CIRCULAR ECONOMY-CIRCULARITY WG OUTCOME DOCUMENT – OVERVIEW....28
OVERVIEW....28

## MESSAGE FROM THE CO-CONVENORS

Over the past decade, it has become increasingly clear that environmental challenges facing our planet – from climate change and biodiversity loss to pollution and resource depletion – are deeply intertwined with the ways we trade, produce, and innovate. In response to this growing awareness, a group of WTO Members have worked together to progressively create new spaces within the multilateral trading system for trade and environmental communities to engage constructively, learn from one another, and chart a shared path forward.

This journey began in 2018 with the creation of the Friends Advancing Sustainable Trade (FAST) group by Canada and Costa Rica. Launched in Davos by nine Members $^{1}$ , FAST was founded on a simple yet ambitious premise: that trade can and should be a powerful enabler of the Sustainable Development Goals. It sought to stimulate new thinking at the intersection of trade and the environment, bridge gaps between policy communities, and encourage engagement and leadership among international organizations, business, academia, and civil society.

Building on this momentum, a group of WTO Members established the Trade and Environmental Sustainability Structured Discussions (TESSD) in 2020, as a broader, Member-driven platform for structured, transparent, and inclusive dialogue. Since then, TESSD has grown significantly, with Members from all geographies, levels of development, with specific challenges and interests, allowing it to develop a solid, and representative, technical foundation through thematic discussions, expert engagement, and sustained stakeholder participation. These discussions have deepened the understanding of key issues such as environmental goods and services, circular economy and circularity, environmental effects and trade impacts of relevant subsidies, value chain transparency, and capacity-building needs, particularly for developing and least developed Members.

The Ministerial Statement issued for the 12 $^{th}$ WTO Ministerial Conference (MC12) held in June 2022 reaffirmed Members' commitment to this agenda and underscored the importance of dialogue and information sharing on trade and environmental sustainability. It confirmed that this work is integral to the relevance, credibility, and the future of the WTO, and highlighted the need to identify concrete actions to support environmental sustainability.

This document traces the evolution of TESSD from its early origins to its current role as a platform for innovative dialogue, learning, and collaboration. It illustrates how openness, inclusiveness, and sustained technical engagement can build shared understanding among Members. Above all, it reflects a growing recognition that trade can contribute to environmental sustainability, innovation, and the development of pathways that are both more sustainable and equitable.

We hope this publication serves not only as a record of progress, but also as an invitation to continue building bridges, deepening ambition, and translating dialogue into meaningful action for present and future generations.

Nadia Theodore
Ambassador, Permanent Representative of
Canada to the WTO

Ronald Saborío
Ambassador, Permanent Representative of Costa Rica to the WTO

## 1 EVOLUTION OF TESSD

1.1. In the wake of the COVID pandemic and amid growing concerns regarding pollution, biodiversity loss and climate change, 50 WTO Members launched the Trade and Environmental Sustainability Structured Discussions in November 2020, during the WTO's inaugural Trade and Environment Week.

1.2. Recognizing that international trade and trade policy play a pivotal role in enabling the transition towards a climate

TESSD is an initiative open to all WTO Members and invited stakeholders, designed to complement and advance WTO discussions on trade and environmental sustainability. It serves as an incubator and "test lab" for new ideas, as well as a forum to examine how trade and trade policy can support environmental objectives. In doing so, TESSD seeks to identify concrete actions that participating Members may pursue individually or collectively to expand opportunities for environmentally sustainable trade.

neutral, more resource-efficient, and more circular global economy, the proponents called for environmental sustainability be established as a guiding principle in the broader WTO reform efforts. To this end, they initiated discussions to identify common topics of interest, with the aim of complementing the multilateral work taking place in other WTO bodies, particularly the Committee on Trade and Environment (CTE).

1.3. By December 2021, participation in TESSD had expanded to 71 Members. At the WTO's 12 $^{th}$ Ministerial Conference (MC12), TESSD trade ministers issued a Ministerial Statement underscoring that international trade and trade policy can and must support environmental and climate goals, while promoting environmentally sustainable patterns of production and consumption. The Statement also highlighted the importance of a just transition and reaffirmed Members' commitments to advancing the Sustainable Development Goals (SDGs).

Graphic 1: TESSD evolution timeline  
![](images/b2c153b66085666f38fe1196f6cbbeb23266edb39ea4aa7586fb7ce31257fe01.jpg)

1.4. To structure their work and identify concrete actions that Members could pursue individually or collectively to advance environmentally sustainable trade, including through voluntary actions and partnerships, participants established four Working Groups (WGs) on: (i) Trade-related Climate Measures (TrCMs); (ii) Environmental Goods and Services (EGS); (iii) Circular Economy – Circularity; and (iv) Subsidies.

1.5. Coordinated by the Co-Convenors, Canada and Costa Rica, the WGs are supported by facilitators who help shape the meeting agendas, solicit expert contributions, and prepare guiding questions to focus the discussions (see boxes describing each WG). In December 2022, a high-level stocktaking event reviewed progress, identified priorities for continued work, and affirmed TESSD's potential to positively contribute to global trade and environmental sustainability discussions.

## TESSD's 79 Co-sponsors

Albania; Argentina; Australia; Austria; Bahrain, Kingdom of; Barbados; Belgium; Brazil; Bulgaria; Cabo Verde; Canada; Chad; Chile; China; Colombia; Costa Rica; Croatia; Cyprus; Czech Republic; Denmark; Ecuador; Estonia; European Union; Fiji; Finland; France; the Gambia; Germany; Greece; Honduras; Hong Kong, China; Hungary; Iceland; Ireland; Israel; Italy; Japan; Kazakhstan; Korea, Republic of; Latvia; Liechtenstein; Lithuania; Luxembourg; Macao, China; Maldives; Malta; Mexico; Moldova, Republic of; Montenegro; Netherlands; New Zealand; North Macedonia; Norway; Panama; Peru; Philippines; Poland; Portugal; Romania; Russian Federation; Saudi Arabia, Kingdom of; Senegal; Singapore; Slovak Republic; Slovenia; Spain; Suriname; Sweden; Switzerland; Separate Customs Territory of Taiwan, Penghu, Kinmen and Matsu; Tajikistan; Thailand; Türkiye; Ukraine; United Arab Emirates; United Kingdom; United States; Uruguay; and Vanuatu.

1.6. TESSD is a pioneer initiative in its incorporation of stakeholder participation and contributions. Given the technical and crosscutting nature of trade and environment issues, inputs from experts across academia, civil society, non-government organizations (NGOs), intergovernmental organizations (IGOs), and the private sector have been essential in informing Members' work. $^{2}$ Delegations have also shared experiences and domestic practices, highlighting trade-related challenges, opportunities, and solutions.

## Working Group on TrCMs

## Facilitator: Switzerland

Overview: Members exchanged experiences and explored practical ways to enhance cooperation on the design and use of TrCMs in support of climate objectives. Discussions paid particular attention to developing country perspectives.

## Working Group on EGS

Facilitators: The Philippines and the United Kingdom

Overview: Using an objective-based approach, and with particular attention to issues of interest to developing countries, Members explored how trade in EGS can contribute to climate mitigation and adaptation. Discussion addressed sector-specific issues related to the promotion and facilitation of trade in EGS.

## Working Group on Circular Economy – Circularity

Facilitators: Japan and Türkiye

Overview: Members examined trade-related aspects of circular economy across the full product lifecycle and shared policy experiences from a broad range of sectors. Discussions included consideration of development perspectives.

## Working Group on Subsidies

Facilitators: Israel and the Republic of Korea

Overview: Members examined both the potential environmental benefits and adverse impacts of subsidies, as well as their implications for trade. Discussions focused on sharing experiences and exploring ways to improve transparency, data availability, and understanding of subsidy practices.

1.7. Over the past five years, TESSD has implemented an intensive work programme. Through 25 sets of meetings, side events, and workshops, nearly 100 delegations and stakeholders delivered more than 160 presentations, most of which – together with informal meeting summaries – are publicly available online. Additional perspectives, experiences and positions were shared through subsequent discussions. The wealth of information generated underscores the deep interlinkages between trade, sustainable development, and environmental protection. $^{3}$

1.8. The insights generated through this work are reflected in the package of substantive outcome documents developed by the four WGs and presented at the WTO's 13th Ministerial Conference (MC13) in Abu Dhabi in February 2024 (see below). The TESSD MC13 package included a Statement by the TESSD Co-convenors and an Updated Work Plan outlining the path forward in the four Working Groups. This work plan focusses on enhancing transparency, integrating development perspectives, and identifying best practices and policy opportunities, with the objective of delivering concrete outcomes by MC14.

## MC13 Working Groups Outcome Documents

\- Member Practices in the Development of Trade-related Climate Measures (TrCMs): Provides a compilation of Member practices in the development of trade-related climate measures, with focus on: (i) transparency and consultations; (ii) impact assessments; (iii) post-implementation review; and (iv) design of measures.

\- Analytical Summary of Discussions on Environmental Goods and Services and Renewable Energy: Identifies indicative lists of renewable energy goods (e.g. photovoltaic cells for solar energy, gearboxes for wind turbines, generators for hydropower, and electrolysers for green hydrogen production) and services (e.g. engineering, testing and analysis, environmental consulting, operation, maintenance and repair, and recycling). The document outlines key trade barriers and supply chain bottlenecks, highlights developing country perspectives and opportunities, and examines possible approaches to promote and facilitate trade in these goods and services.

\- Mapping Exercise: Trade and Trade Policy Aspects along the Lifecycle of Products: Maps trade and policy relevant aspects across circular economy initiatives and identifies possible trade-related actions in areas such as transparency; standards and regulations; trade facilitation; waste management; capacity building and technical assistance; and technology cooperation.

\- Compilation of Experiences and Considerations regarding Subsidy Design: Describes Members' experiences and considerations in the design of subsidies to support the low-carbon transition, including how positive environmental effects can be balanced against potential trade-distorting impacts. It also examines how subsidy design choices may disproportionately affect developing countries and least developed countries (LDCs), including through market distortions.

1.9. A key focus of TESSD has been to identify priorities from a development perspective. At its high-level plenary meeting in December 2024, Members discussed how developing countries are integrating trade and environmental sustainability into national policy frameworks, underscoring the importance of knowledge sharing, the adoption of practical solutions, and capacity building to address gaps in resources and expertise. Participants also examined how multilateral trade processes can create opportunities for developing economies to contribute to global climate and environmental objectives, reinforcing a shared understanding of the role of trade in addressing environmental challenges.

## TESSD as an incubator

With 79 Members now co-sponsoring TESSD, the initiative – alongside other WTO trade and environmental sustainability initiatives such as the Dialogue on Plastic Pollution and Environmentally Sustainable Plastics Trade and Fossil Fuel Subsidy Reform Initiative – has played a key role in advancing discussions on the mutual supportiveness of trade and environment. TESSD has helped catalyse engagement for the revitalization of the CTE and strengthened related work across other WTO bodies.

In particular, TESSD has served as an incubator for ideas on trade and environmental sustainability, generating analytical work and practical insights that has informed discussions in a range of WTO bodies. Key contributions include work on the interoperability and transparency of TrCMs, trade and climate challenges and opportunities for developing countries, regulatory cooperation, classification of environmental services, and sustainable agriculture practices and related policies.

"TESSD is a forum to share experiences, learn and borrow from replicable solutions and build domestic capacity through knowledge exchange" – Ambassador Matthew Wilson of Barbados

"TESSD has been a key initiative to address environmental sustainability within the multilateral trade framework, fostering the exchange of experiences and challenges that capture the diverse realities of its participants, generating high-value discussions that have enriched the work developed at WTO." – Ambassador Sofia Boza of Chile

"TESSD is a trailblazer at the WTO. You are searching for practical solutions and concrete actions to catalyse the trade and environment agenda. You are breaking down silos and cooperating across traditional structures and fields of expertise to find solutions to global problems" - WTO Director-General Ngozi Okonjo-Iweala

1.10. At MC14, the work of TESSD co-sponsors will be showcased through the technical outcomes developed by the different WGs. The Annex to this publication presents key elements from these outcomes, along with links to the documents in full.

1.11. The following sections provide a crosscutting overview of the substantive knowledge generated during TESSD's first five years. While not exhaustive, this overview illustrates how focused and collaborative engagement can generate valuable insights for policymakers, experts, and the broader public on the role of trade and trade policy in supporting sustainable development and advancing environmental sustainability goals.

## 2 TRADE IN SUPPORT OF CLIMATE AND ENVIRONMENT: INSIGHTS FROM TESSD $^{4}$

2.1. TESSD work has covered a wide range of topics, from the role of environmental goods and services in advancing the clean energy transition and supporting climate adaptation in sectors such as agriculture and water, to national experiences and international cooperation on carbon measurement standards and other trade-related policies for reducing industry emissions.

2.2. Members have also examined subsidy reform issues and how subsidies may be designed to benefit the environment while minimizing trade distortions, as well as the role of trade and trade policy in fostering a resource-efficient circular economy. This section is organized around three key climate topics that have received considerable attention in TESSD: the clean energy transition; reducing emissions of industry and transport; and climate adaptation, water management, and sustainable agriculture.

2.3. The section draws on Members' discussions and experience sharing, stakeholder contributions, and TESSD outcome documents. Box 1 below provides a few crosscutting, non-exhaustive insights drawn from TESSD's extensive discussions and work. These reflect overarching initial observations that illustrate the value of continued dialogue on trade and sustainability issues.

##

[中间内容因长度限制已省略]

 movement of secondary materials, recycled goods, and circular services including on waste management, can both drive and benefit from improved waste management. Effective systems for collection, sorting, and classification of end-of-life products are critical, especially in developing countries. Trade can also support investments in environmentally sound waste management and services that extend product lifetimes. The Basel Convention's Prior Informed Consent (PIC) procedure for hazardous waste, a "notice and consent" regime, was referenced in the TESSD discussions as necessary to protect human health and the environment, and prevent illegal waste trade.

## Capacity building and technical assistance

An inclusive circular economy ensures that all stakeholders benefit economically, without solely bearing the costs of pollution. Developing economies, in particular, can leverage international trade to access technologies and tools that enable circular activities. Capacity building and technical assistance are vital to scaling up a more circular economy globally and ensuring that developing countries can fully participate and benefit.

\- For example, some international projects discussed in the meetings focus on supporting SMEs in developing economies, on producing goods with minimal materials, reusing, refurbishing, or recycling, while other projects focus on building capacity on standards infrastructures, customs procedures (e.g. on transparency, or to conduct internationally recognized inspections and testing and certification).

## Technology and other trade-related aspects of cooperation

Environmentally sound technologies, goods and services may be helpful inputs, from manufacturing through end-of-life stages, supporting the production of more circular and sustainable sectors, addressing technology and infrastructure gaps. Trade-related cooperation could be international, as well as regional or bilateral. Bilateral or regional trade agreements focusing on sustainability can be a vehicle to establish trade-related cooperation in support of identified key sectors.

The present document provides an in-depth analysis of trade and circular economy, with a focus on the afore mentioned four sectors, based on discussions in TESSD. It helps illustrate, through specific examples in each of the sectors, trade aspects identified in this overview, and related Member practices on circular economy.

## Circular Economy Plans, Roadmaps or Strategies

Many Members have developed Circular Economy plans or roadmaps, under the auspices of multiple ministries, which articulate visions or strategies across a wide range of sectors and can encompass different policy tools. Some examples shared include:

\- EU: Adopted in March 2020, the second Circular Economy Action Plan is one of the main building blocks of the European Green Deal, Europe's agenda for sustainable growth. The action plan includes initiatives addressing the entire life cycle of products, including how products are designed, as well as ensuring that waste is prevented and that used resources are kept in the EU economy for as long as possible.

\- Mauritius Circular Economy Roadmap and Action Plan (2023-2033), in line with the Government Programme 2025-2029 for advancing Mauritius as a green economy that encourages recycling and fosters a circular economy.

\- Peru's Supreme Decree No. 003-2025-MINAM (published on 25 February 2025) approved the National Roadmap for Circular Economy to 2030. The National Circular Economy Roadmap (HRNEC) will seek by 2030 to generate enabling conditions to make the transition to a circular economy viable through four strategic objectives: (1) Circular governance and policies, (2) Innovation and circular business, (3) Sustainable consumption and circular culture, and (4) Circular territories and cities.

\- The Swiss Federal Assembly adopted the Parliamentary Initiative 20.433 "Strengthening Switzerland's Circular Economy" on 15 March 2024. The revisions to the Environmental Protection Act, the Energy Act, and the Federal Act on Public Procurement establish an overarching legal framework to reinforce the circular economy in Switzerland.

\- The Kingdom of Saudi Arabia's commitment to environmental sustainability, as outlined in Vision 2030 aligns with national and global goals, including reducing carbon emissions, achieving carbon neutrality and fostering a circular economy. The Kingdom of Saudi Arabia has implemented more than 30 Circular Carbon Economy initiatives across the energy system, enabling climate action while bolstering economic growth. The Circular Carbon Economy (CCE) framework is an integrated, inclusive and pragmatic approach to managing emissions.

Amongst others, Chatham House, with support from UNIDO, has conducted a global stocktake of national circular economy roadmaps, including 75 national roadmaps and 2882 individual policy actions. $^{24}$ In their analysis, they indicated that policies included in the roadmaps sometimes covered fiscal instruments such as taxes and duties, public financing or investment funds, as well as producers or products requirements.

Some regional platforms have also been focusing on Circular Economy, such as the ASEAN Framework on Circular Economy, African Circular Economy Roadmap or the Circular Economy Coalition of Latin America and the Caribbean's mission is to provide a regional platform to enhance inter-ministerial, multi-sectoral and multi-stakeholder cooperation to increase knowledge and understanding about the circular economy, facilitate training, training and technical assistance for the development of circular economy and sustainable consumption and production public policies.
"""
