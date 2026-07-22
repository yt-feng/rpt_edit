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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
BCG

# Australia's Digital Infrastructure Challenge:

Can data centres unlock sustainable long-term growth?

MAY 2026

![](images/85e89984bd7cb2e064b1f3561bce738f7ef8dfcfe62e5d9f471cc067dbb3435c.jpg)

![](images/4941b6306d9f0b3cd0c909ef7e4736acdfa35cd2da9811249def7520a45f92ca.jpg)

## About this report

AI is driving an unprecedented surge in demand for computing power and the data centres that underpin it. Deploying new applications, managing growing data volumes and building new models all depend on reliable, large-scale digital infrastructure.

In this report, we explore the role that digital infrastructure could play in Australia's future economic development. We examine the growth of the global data centre market, Australia's competitive position, and the opportunities associated with a thriving domestic digital infrastructure sector. We also consider the emerging challenges, system constraints and trade-offs that are becoming more pronounced as demand for computing capacity accelerates both locally and globally.

This report draws on BCG experience, analysis and frameworks, including interviews with over 20 senior digital infrastructure executives and a survey with senior executives across relevant industries.

## Executive summary

As generative AI accelerates and new applications scale rapidly, global demand for computing power is still outpacing supply, even though computing capacity is expected to be 2.5X by 2030.

Australia is already one of the largest data centre locations in Asia Pacific, with approximately 1.8 GW of installed capacity in 2025 and the potential to capture even more growth and associated investment. Australia’s renewable energy potential, strong subsea connectivity, and stable and secure political, business and regulatory environment provide the foundations for a thriving data centre destination that addresses secure sovereign needs and can meet both Asia Pacific and global demand.

By strengthening its digital infrastructure market, Australia could build a reliable capability for its industries to increasingly rely on, and attract global investment from data centre developers, hyperscalers and colocation providers.

The opportunity is significant: developing 2.5 GW of additional compute capacity by 2030 could generate \$100+ billion in locally-retained economic impact from the construction of data centres and new energy generation to match, and indirectly stimulated local supply chain activity. Once operational, approx. \$8 billion - \$10 billion per year in local economic activity could be stimulated by ongoing data centre operations.

To date, various structural factors have helped to attract digital infrastructure investment into Australia. However, as GenAI drives unprecedented growth in data centre market capacity, and in an increasingly competitive regional market, these factors alone will not be enough to continue to secure investment.

Australia is now approaching an important inflection point. As demand for digital infrastructure accelerates, a number of emerging pressures and constraints that have not materially affected growth are becoming more pronounced. Australia has an opportunity to position itself to capture this opportunity, but will need to proactively address four key challenges:

\- The power paradox - managing the increasing need for electricity availability: Data centres are becoming a large and fast-growing source of electricity demand at the same time as Australia is navigating the broader energy transition. Australia’s renewable and storage pipeline is strong, but new Final Investment Decisions (FIDs) of wind, solar and gas have largely stalled in recent years due to challenging economics, permitting and community issues. Data centre demand could accelerate the build-out by underwriting projects and unlocking economic viability. However, the pace of demand growth relative to the time required to deliver new supply creates a growing challenge. Realising the data centre opportunity for Australia will require careful balancing of energy reliability, affordability, decarbonisation and investment considerations, particularly as governments, energy providers and the technology sector navigate how new AI and therefore energy demand interacts with an already evolving energy system.

\- The chicken-or-egg dilemma - investment sequencing and delivery certainty: The scale and speed of investment required to support future data centre growth is creating increasing interdependencies between developers, customers, energy providers and governments. Developers are often hesitant to commit significant upfront capital without long-term customer commitments, while customers seek greater certainty around delivery timelines, power availability and infrastructure readiness before making long-term decisions. As demand accelerates, balancing these competing risk positions is becoming more important, particularly in an environment where approval processes, energy delivery timelines and market signals continue to evolve.

\- The shackles of micro decisions - managing concentration and long-term infrastructure planning: Data centre investment is increasingly concentrating in major hubs such as Sydney and Melbourne, where existing infrastructure, connectivity and demand present strong commercial advantages, but the cumulative impact can place increasing pressure on energy, land and network infrastructure in a relatively small number of locations. This raises broader questions around how growth could be balanced across the country; how infrastructure planning could better align across energy, connectivity and land use; and how the trade-offs between market-led development and more coordinated long-term planning approaches could be reconciled.

\- The data centre race - competing for global data centre investment: Competition for data centre investment across the Asia-Pacific region is intensifying as governments move to capture growing AI and digital infrastructure demand. While Australia has many structural advantages, longer and more fragmented approval and grid connection processes could create challenges for time-sensitive investment decisions, particularly relative to faster-moving Asian markets. As competition intensifies, Australia will increasingly need to balance speed, coordination, regulatory detail and long-term infrastructure planning if it seeks to remain competitive in an increasingly contested Asia-Pacific market.

Addressing these four challenges is achievable but will require coordinated action. With its Asia Pacific peers already active in this attractive global market, Australia will need to act decisively to capture this new economic opportunity. Australia could also miss an important opportunity to bring economic activity and digital infrastructure and capabilities to communities outside the popular data-centre hubs of Sydney and Melbourne.

![](images/4ebc29a9d67d27edc1ed480c4bfbbb761bbb91a5140ac9e35dd733a9693748ca.jpg)

# 1. Context: Demand for computing power is growing rapidly

## Global demand for computing power is driving demand for data centre capacity

The rapid adoption of AI, the expansion of digital services and continued cloud migration are driving computing demand at an unprecedented pace worldwide. As a result, global data centre market capacity is projected to grow by nearly 2.5X from 87 GW today to 233 GW by 2030 (see Exhibit 1).

This growth is likely to be driven by hyperscalers, including companies that build their own data centre capacity and companies that lease capacity.

Growth is also likely to come from co-location operators, which build shared digital infrastructure for hyperscalers, enterprise and edge customers, and AI-focused cloud providers (including Neoclouds), which require specialised infrastructure to facilitate high-performance computing operations. Other companies, such as OpenAI and Anthropic, are investing billions into computing power globally by partnering with hyperscalers, tech giants and colocation providers.

Exhibit 1: The market for data centres is set to grow nearly 2.5x in five years

Global data centre market capacity (GW, critical IT load)

![](images/aee27bc55d43fa6301f7de7c235db7bf58aa6e014f39395a1ce27919fd1429bf.jpg)  
Note: Global outlook excludes China and crypto Source: datacenterHawk; BCG Global Data Center Model

With this unprecedented level of investment accelerating the development of digital infrastructure globally, questions are emerging about an AI investment bubble. The potential for market correction is indicated by various signals, such as peaking capital expenditure (as hyperscalers build ahead of demand), weaker near-term monetisation, and development execution risks (due to bottlenecks and rising build complexity).

A significant share of contracted capacity is underwritten by AI companies whose valuations remain largely unrealised — creating a circular dynamic in which rising equity enables new infrastructure commitments, which in turn justify further build-out.

However, the sector fundamentals remain robust. Despite debate around the current investment cycle, there are strong signals that data centre demand will remain sustainable. Vacancy rates are very low and pipelines are largely pre-sold, de-risking near-term occupancy for quality assets. The AI mix is still evolving — inference workloads are still expanding, sustaining megawatt demand even as the workload profile evolves.

Critically, data centre capacity is flexible and easily repurposed even if large-scale AI training normalises. Sites can pivot to enterprise AI, cloud, storage and traditional workloads, meaning demand is broader than any single use case. Even in a moderation scenario, value does not disappear; it shifts toward enabling layers (power solutions, cooling retrofits, and operations software) reinforcing the resilience of the broader ecosystem (see Exhibit 2).

## Exhibit 2: Data centre economics remain strong with pre-sold pipelines and rising AI demand

## Signals DC bubble may burst soon

\- Demand visibility is weaker than supply momentum: training/inference demand is real, but monetisation is still forming; a slowdown in enterprise ROI realisation would flow quickly into capacity deferrals

\- Deployment bottlenecks can strand capacity: grid access, permitting, and energisation sequencing can delay usable MW, pushing out revenue while capex is already sunk

\- Higher build complexity increases execution risk: rising rack densities and cooling transitions (liquid/hybrid) increase commissioning risk and extend time-to-stabilised operations

\- Significant share of contracted capacity is underwritten by AI companies: valuations remain largely paper-based/ unrealised - creating a circular dynamic where rising equity enables new infrastructure commitments, which in turn justify further build-out

Source: Industry interviews; BCG analysis

## The global data infrastructure landscape is being reshaped by AI workloads, energy availability and regulatory shifts

Historically, data centres had to be built in proximity to end-users to overcome latency constraints (delays in data travelling between locations). However, a growing share of workloads – particularly in GenAI – are increasingly latency-tolerant, which means the need to develop digital infrastructure near end-users is not as much of a constraint. For example, AI model training workloads are insensitive to latency, which means data centres serving these workloads can be located anywhere in the world (see Exhibit 3). This shift allows developers to exercise greater flexibility when selecting sites.

## → Signals DC bubble may stay resilient

\- Vacancy is ultra-low and pipelines are largely pre-sold: current market tightness and pre-leasing de-risk near-term occupancy for quality assets

\- AI mix shift is still early: the share of AI (especially inference) is expanding, creating sustained MW pull even as the workload profile evolves

\- Capacity is flexible and repurposable: even if "training" normalises, sites can pivot to enterprise AI, cloud, storage, and traditional workloads; demand is broader than one use case

\- The value moves to enabling layers, not a hard stop: even in a moderation scenario, spend rotates toward power solutions, cooling retrofits, modular adds, operations software, and maintenance (i.e., resilience of ecosystem value pools)

While more traditional enterprise (including cloud) and high-performance computing workloads are likely to remain important drivers of demand, latency-tolerant GenAI inference workloads are likely to be a key force behind data centre capacity expansion and are estimated to account for approximately three-quarters of global market growth (2026-2030). $^{1}$ This is largely due to the increasing adoption of GenAI inference use cases (including agentic AI) and a consistent rise in demand for GenAI model training. Australian-hosted data centres could theoretically serve selection of these workloads for customers both locally and in most parts of the Asia-Pacific region.

Exhibit 3: A growing share of workloads – particularly in GenAI – are latency-tolerant and will drive future growth  
![](images/1becfaace7b0d571c26d824cf63313b3a559a6798f94341afef1045254e5e4cb.jpg)  
Note: Mapped workloads are illustrative & non-exhaustive, acceptable latencies are indicative ranges; RTT = round-trip time (ms), metric for latency; CAGR = compound annual growth rate; HPC = high-performance computing; growth rates exclude China. CAGRs represent global market.
Source: Desktop research; expert interviews; BCG Global Data Center model, March 2026 update; BCG analysis

GenAI training and inference workloads require energy-intensive, high-density computing clusters that can scale over time. With power availability the number one constraint on new capacity, the market is shifting towards the development of larger and more centralised data centre campuses. However, global grid connection timelines can often stretch for years and are constraining data centre expansion despite strong growth in demand.

At the same time, regulators in some countries are tightening data sovereignty and residency requirements, increasing the need for in-country or in-region data centre capacity for select workloads. Additionally, some governments are positioning data centres as critical national infrastructure with policy support and streamlined planning pathways.

These combined factors of latency-tolerant AI workloads, global energy constraints and increased regulatory requirements are reshaping the investment landscape for digital infrastructure. As a result, capital is increasingly flowing into markets that can deliver viable sites alongside a credible combination of power availability, connectivity and political stability.

## The Asia-Pacific region is becoming increasingly competitive for data centre investment

Data centre developers, and hyperscalers in particular, typically prioritise investing in markets that offer speed of execution, cost competitiveness and greater policy predictability. As a result, more capital is flowing into digital infrastructure hubs in the Asia-Pacific. Asia-Pacific markets are using different approaches to attract future investment, which will be increasingly GenAI-focused (Exhibit 4). For example, Singapore is a leading regional hub despite land and power constraints, with data centre investment supported by tightly managed capacity releases, selective approvals, and a strong emphasis on efficiency and sustainability. Malaysia is positioning itself as a major regional market and as Singapore's ‘overflow’ by offering robust tax incentives and sustainable-development guidelines. India is strengthening its position as a hub for digital infrastructure with an emerging national policy framework and established state-level incentives aiming at capturing global AI and cloud investment.

The competitive dynamics are continuing to expand across the Asia-Pacific. Japan is aligning its data centre strategy with decarbonisation priorities, supporting regional expansion beyond Tokyo with grid-planning initiatives. South Korea is dispersing capacity beyond Seoul via grid access reforms and a 2025 Power Grid Special Act. Thailand and Indonesia are also mobilising; Thailand with sovereign cloud initiatives and BOI tax exemptions, and Indonesia using a centralised National Data Centre strategy backed by licensing simplification and proposed tax incentives for providers and equipment importers.

Across the region, the pattern is consistent: markets with clear, integrated policy frameworks spanning strategy, infrastructure and incentives are capturing higher levels of investment.

Exhibit 4: Data centre investment settings across the Asia-Pacific

<table><tr><td></td><td>Strategy &amp; CoordinationNational data centre strategy and policy direction</td><td>EnablersEase of permitting, grid access, land and infrastructure readiness</td><td>IncentivesPublic investments and financial incentives for data centres</td></tr><tr><td>Singapore</td><td>Selective capacity allocation reinforces Singapore&#x27;s role as a trusted, sustainability-led hub</td><td>Strong planning discipline and high efficiency standards support green development</td><td>Energy-efficient equipment grants covering 30-70% of cost, capped at SGD$30k per company</td></tr><tr><td>Malaysia</td><td>AI-related projects prioritised; non-AI data centers face constraints</td><td>Scalable capacity, renewable energy access, and supportive permitting underpin growth</td><td>Investment Tax Allowance or reduced corporate tax rates for 5-10 years</td></tr><tr><td>India</td><td>National capacity target under policy draft and state-led support drive development</td><td>Planned plug-and-play zones and pre-provisioned infrastructure improve delivery readiness</td><td>Proposed tax holiday for 20 years underway</td></tr><tr><td>Japan</td><td>Decarbonisation and energy-security priorities increasingly shape DC strategy</td><td>Regional siting and grid-planning initiatives support expansion beyond Tokyo/Osaka</td><td>Government support increasingly favors energy-efficient and regionally distributed digital infrastructure</td></tr><tr><td>South Korea</td><td>No specific data center strategy or capacity targets in place</td><td>Grid access granted outside the metro area to disperse new DC beyond Seoul</td><td>Free Economic Zones, high-tech infrastructure incentives, and 2025 Power Grid Special Act grid-expansion initiatives</td></tr><tr><td>Thailand</td><td>Government remains supportive of cloud and AI infrastructure investment</td><td>Industrial estates, c

[中间内容因长度限制已省略]

g infrastructure. Increasingly location-flexible AI workloads also create opportunities for Australia to compete for a larger share of Asia-Pacific and global demand over time.

At the same time, the sector is approaching an important inflection point locally. As data centre demand accelerates, emerging pressures around energy availability, investment sequencing, infrastructure concentration, planning and delivery timelines are becoming more pronounced. These are not simple challenges to navigate, nor are there straightforward solutions. Many of the trade-offs emerging in Australia are also being observed internationally as governments, energy providers, hyperscalers and infrastructure developers adapt to the scale and pace of AI-driven growth.

Australia is already seeing progress across a number of these areas, and the country retains many of the structural advantages that have supported growth in the sector to date. However, as competition for global digital infrastructure investment intensifies, how Australia balances infrastructure readiness, delivery certainty, energy transition priorities, regional development opportunities and international competitiveness will increasingly shape its ability to capture future investment.

The next few years will determine how Australia positions itself for the next phase of global digital infrastructure and AI development and shapes its potential as a trusted digital infrastructure destination for the Asia-Pacific region.

![](images/ce1e65eeaeb4c044bd29cc8595800b438ab3e4354d2214ff3c5eefa73134c145.jpg)

![](images/dbfdff4a4f9db5be70dc916ec8c174d0a9186110ec39406ab776a4d010cab8f7.jpg)

## About the Authors

![](images/1948e9ad27d22fef1281434567177ba60d25112956e71d7d19861b9738d698a6.jpg)

Chris Mattey is a Managing Director and Partner of the Sydney office of Boston Consulting Group. Contact Chris by email at mattey.chris@bcg.com

![](images/090cdccab5a5dac89701407ed1043441493eb0c1c3508e36ba4e8681e7a817d0.jpg)

Shruti Gangwal is a Partner of the Sydney office of Boston Consulting Group. Contact Shruti by email at gangwal.shruti@bcg.com

![](images/13270e5f27eb9bcf2e210572ba5c100801471ebc5f19d20abe18f300e2b7253e.jpg)

Matt Abel is a Managing Director and Senior Partner of the Perth office of Boston Consulting Group. Contact Matt by email at abel.matthew@bcg.com

![](images/a1244c15ec14921ad488280fcc0e548bd0074fa876f7f9fd6a1a4943380248e4.jpg)

Anna Green is a Managing Director and Senior Partner of the Sydney office of Boston Consulting Group. Contact Anna by email at green.anna@bcg.com

Whitney Merchant is a Managing Director and Partner of the Sydney office of Boston Consulting Group. Contact Whitney by email at merchant.whitney@bcg.com

![](images/45d245c11a386cf7b66127dd867bf5f0664bc24e4634d91b8fad9b4ffaac9945.jpg)

![](images/f811ca13072b04df3f3b44aace168d9659655fba096e0128ebb6ab26f6eff458.jpg)

Blake Nicholson is an Associate of the Auckland office of Boston Consulting Group. Contact Blake by email at nicholson.blake@bcg.com

![](images/0518cc61b698e44b1b2974495dcbc2bf61de63417cd422eb9fac837134592b96.jpg)

Joe Butler is a Managing Director and Partner of the Perth office of Boston Consulting Group. Contact Joe by email at butler.joseph@bcg.com

![](images/cbd31641eda3d191eca54d2d9fa51f6a65392626d9c6f01043c31836a46d7623.jpg)

Ant Roediger a Managing Director and Senior Partner of the Sydney office of Boston Consulting Group. Contact Ant by email at roediger.anthony@bcg.com

![](images/4d258b61efdbfebc4f6b8a865c51f6d6c789ee177e70706c4a05ca43ffaafbd1.jpg)

Jan Koeleman is a Principal of the Melbourne office of Boston Consulting Group. Contact Jan by email at koeleman.jan@bcg.com

![](images/785161f93bc394e119ac0df35db4711031bccbb241ad7bf74db5ac1dfb63339b.jpg)

Miguel Carrasco is a Managing Director and Senior Partner of the Sydney office of Boston Consulting Group. Contact Miguel by email at carrasco.miguel@bcg.com

![](images/b70e93fccc929823011fc6f0c1ab7589dcd767bd3adac9d9318e18dc936b5735.jpg)

Richard Hobbs is a Partner of the Auckland office of Boston Consulting Group. Contact Richard by email at hobbs.richard@bcg.com

![](images/b49114823183dc418598fd4b61150e998c0b5c7803310047960d41795eb6f2a0.jpg)

Olivia Loa is a Senior Analyst - BCG Vantage of the Houston office of Boston Consulting Group. Contact Olivia by email at loa.olivia@bcg.com

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders – empowering organisations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organisation, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

For information or permission to reprint, please contact BCG at permissions@bcg.com.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com.

Follow Boston Consulting Group on Facebook, LinkedIn and X (formerly known as Twitter).

© Boston Consulting Group 2026. All rights reserved.

![](images/8a2989c7a8aad76eeb71df43f63a4fda1edb3fdafdb38e2da8854407404fdc94.jpg)
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
