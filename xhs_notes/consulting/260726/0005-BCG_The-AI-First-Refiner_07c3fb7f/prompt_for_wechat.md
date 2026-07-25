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

Executive Perspectives

## Outperforming Through Volatility: AI in Refining

Refining

April 2026

## Introduction

We meet often with CEOs to discuss AI, a topic that is both fascinating and rapidly evolving. After working with more than 2,000 clients over the past two+ years, we are sharing our latest insights in a new series designed to help CEOs navigate AI. For refining leaders, the question is no longer whether AI matters, but how to use it to outperform through volatility and create durable competitive advantage.

The refining sector is under structural pressure. Long-term demand is expected to decline, while net refining capacity could still grow by 2030, even after closures, sustaining pressure on margins. At the same time, geopolitics, sanctions, regulation, and trade dislocations are amplifying volatility. AI offers a new set of levers—moving refineries from periodic, siloed optimization to real-time, margin-driven decisioning and closed-loop workflows across planning, operations, logistics, maintenance, and safety. For a reference mid-quartile player, that can translate into \~\$0.5–1.2/bbl of EBIT uplift by 2030. Against this backdrop, three questions matter most:

• What does it mean to operate as an AI-first refinery end to end?

\- Where are leading refiners already creating value today in planning and scheduling, operations, logistics and trading, maintenance and reliability, turnarounds, and HSSE?

\- What pragmatic steps should companies take to move from isolated pilots to scaled transformation?

Advances in AI, generative AI, and agentic AI are enabling refiners to shift from isolated tools to embedded capabilities

In this Executive Perspective, we outline how AI-first refineries can outperform in a structurally challenged and volatile market

![](images/9f54b3568e8625accb90fc764dd18f65a79567d612b8ac7fbeea8bacb9defc0f.jpg)

## Executive summary l AI-first refineries will outperform in a structurally challenged and volatile market

## WHY

AI adoption is now critical for refineries facing structural pressures

\- The refining outlook is tightening, long-term demand is expected to decline, while net refining capacity could grow by 2030—even after closures—sustaining pressure on margins. Geopolitics, sanctions, regulation, and trade dislocations are amplifying volatility.

\- At the same time, recent advances in AI and computing are opening new value pools that were previously inaccessible. For a reference mid-quartile player, AI can unlock \~\$0.5–1.2/bbl of EBIT uplift by 2030.

## WHAT

\- AI is moving refineries from periodic, siloed optimization to real-time, margin-driven decisioning and closed-loop workflows across planning, operations, logistics, maintenance, and safety.

\- The impact is already visible across the value chain: planning and scheduling can deliver \~\$0.15–0.30/bbl, operations \~\$0.1–0.5/bbl, logistics/trading \~\$0.2–0.3/bbl, and maintenance/reliability \~\$0.05–0.1/bbl.

\- Proven deployments show material results, including +\$80M from a \~300 kbpd refinery in operations, >\$80M annual margin opportunity in logistics/trading, and 5%-15% maintenance cost reduction with 62% inspection-efficiency gains.

## HOW

\- Start with the highest-value workflows—planning and scheduling, operations, and maintenance and reliability—where AI directly improves margin and reduces value leakage.

## Winning refineries anchor AI in P&L impact through focused formations

\- Build the foundations to scale: standardized data, digital twins, enterprise platforms, and workflow integration are critical to embed AI into day-to-day execution.

\- Redesign processes and the operating model—don’t just deploy tools—to capture value at scale, with governance, value tracking, and capability building embedded from day one.

## Long-term oil demand is set to decline across a spectrum of scenarios

## Refined products global demand (Mbpd)

![](images/3d8c1ba93defb8075cd5282de6762548758c99adcc1ff5e040943149416a4b23.jpg)

Actual demand and mix will be defined by future regulations and how pledges translate into policies

1. IEA STEP scenario. 2. IEA APS scenario, emission reduction is from 2022 to 2050. 3. Scenario slope of IEA NZE has been adjusted in order to reflect a stronger emission reduction effort from 2030. Temperature rises and CO2 reduction for cases 2 and 3 are approximate and derived by linear interpolation from IEA STEPS and IEA APS scenarios, not bottom-up climate modeling.
Source: IEA WEO 2024; IEA WEO 2025; BP; ExxonMobil; BCG Oil Long Term Model; BCG analysis.

## Refinery capacity growth is set to outpace demand, putting sustained pressure on the margins

Net refining capacity growth 2026-2030 $^{1,2,3}$ (Mbpd)  
![](images/b9a637212465249b1db7f5eef25fd16e07837a40195766aade556f4d70c76aed.jpg)

1. Not probability weighted. 2. CDU + Condensate. 3. Including both expansion projects of existing refineries and new refineries, including projects that roll over from 2025, and excluding capacity added or closed in 2025.

Note: Excluding greenfield refinery projects under approval or prior stages. Probability category attribution subject to available information at the time of elaboration of the slide.

Source: GlobalData 2025; IEA WEO 2025; Wood Mackenzie; BCG Oil Long Term Model; BCG Global Refining Model; BCG Analysis.

![](images/3a8077e176c84ecedeae776c9dcf1a63a7c777c85e6283cbbd6d2211d5ac4a05.jpg)

![](images/6c4e8e09c10d3c35116b44d61d24185c0ae2b844ba69a66bc0a2ad2c306f4929.jpg)

![](images/ec9fb0c6272a8766af49db5472e3ea0e02c1c746ae8eaeddf2a73887446ca6d1.jpg)

## Supply exceeds demand even in the conservative Brown scenario, where demand decline is minimal

## Even if we exclude capacities with "low" probability, supply exceeds most optimistic demand growth scenario

## Supply-demand dynamics de-

averaged by refined product (e.g., jet fuel, naphtha demand more resilient)

## However, margins are expected to be highly volatile in the near term

![](images/7783d65933564e52f33fd4519eac7ec58ccf2ba6ada925a08708275117291ba3.jpg)

Electrification of transport

Market dynamic

Faster EV and hybrid uptake...

Margin impact

... erodes
gasoline demand
and caps margin
upside

![](images/1bae23dedeef96e0fff3781ec6954f79ca82b6dd05be0b68573ee4bb1d42d3fc.jpg)

Chinese
exports

Potentially higher export quotas...

... pressure
regional margins
through
oversupply
and price
competition

![](images/f834a18b719ce88b24baa16ef0a15f0feac9ac37c96f16df88fe9080da2c8ac6.jpg)

Global growth and tariffs

Uneven economic growth and trade barriers across regions ...

...create margin
volatility from
uneven demand
and product
flows

![](images/ab2e1947548995d60558c7514127f5230886483af1061ce243222a00254707cb.jpg)

Evolving Russian sanctions

US sanctions on Rosneft/Lukoil and the EU's 2026 product ban...

...potentially
disrupt trade and
amplify margin
volatility

![](images/e3718616db7b5e0286aecef9438977f9cd894d03615aef1a938c5c190b8ac6a0.jpg)

New capacity startups

Accelerating startups of large-scale refining capacity....

...exacerbates oversupply and compresses margins

![](images/ae0bf5b89f0b55cc077345d98b0736ab874cfc0a18c2e9b9d9d75032fa553243.jpg)

IMO
MEPC83 $^{1}$

Tightening emissions standards $^{2}$ across the global fleet...

... require
operational
reinvestments
with penalties for
non-compliance

![](images/3958c13a584103993997e7d386f4d06d444c4f6bbaa110fe26b86c8d42ab588a.jpg)

## Rapid advances in AI and high-performance computing have the potential to fundamentally transform the refining industry

## — Deterministic

Rules-based

![](images/84cc360a1470747de671478ab539af0a027fd65105c79c21d2bee81bff7c61ff.jpg)

## Systems follow a programmed set of rules

When column pressure exceeds threshold, system triggers predefined shutdown or alarm

Machine Learning

![](images/ffeffbaa8107c892b0ddf8923a3d5d37c712bdcf13c7ba10979e3117527c5219.jpg)

Deep Learning (via multi-layer neural networks)

![](images/1d7ffcaa7b2ee8c1ef69fba64df99d13150317ba03ef95cd8ef6b008f3518333.jpg)

Systems automatically learn from data without being explicitly programmed (e.g., to predict values or identify correlations)

ML models predict heat exchanger fouling or compressor failure weeks in advance, enabling planned intervention

Probabilistic

Generative AI (e.g., via transformer-based model)

![](images/765f5ab891e8b34175506a3027db9790c9681733b56a51d54318d0544ca3811e.jpg)

Not exhaustive

Agentic AI (e.g., using GenAI and tools)

Systems use existing content to create new variations

GenAI synthesizes sensor trends, lab assays, and shift logs to recommend optimal crude blends and operating envelopes

Systems respond to environments and prompts, to plan then auto-execute tasks

Agentic AI continuously monitors unit constraints and margins, selects optimal setpoints, and makes adjustments via control systems

## AI is already driving a step-change in the efficiency and efficacy of core functions of the refining value chain

![](images/a775452c2b809b84bf6016f5793e597601d7aab69ec8cd800797b9dad9047c33.jpg)

## Planning and Scheduling

![](images/61824938ac611ccfa7461d2c6a00774c1a4bc1f246ecdfc95237930edc37ff2b.jpg)

## Operations

![](images/3354800a8fd9dada1f73b62872c1b4fd4fe28cb13662cefbb59ad0e641246287.jpg)

## Logistics and Trading

![](images/3d31c6940cfcfb2dc5f69b379ac311ee7cf764f6a3c937f1287cf48fb5442aa9.jpg)

## Maintenance and Reliability

![](images/a0ddce36e4cb2ea9bed53db21b7ccaef5e518f1a2ea8f8c66caecb60d45f13a0.jpg)

## Turnarounds and Projects

![](images/f72e7694db58f9c4655ce98748ba56ef7c669f2fde1f5873a6c6f763c537bbdb.jpg)

## HSSE $^{1}$

1. Health, Safety, Sustainability, and Environment.
Note: Business support functions are excluded.
Source: BCG analysis

## From...

\- Periodic constraint-based planning using LP models and offline simulations, with limited response to real-time disruptions

\- Advanced process control optimizing individual units with manual, cross-unit coordination

• Conservative blending and manual quality checks

\- Deterministic planning with static demand and inventory assumptions with reliance on buffers

\- Predictive maintenance based on historical data and expert judgement

\- Capex decisions based on deterministic business cases and static schedules, updated periodically

\- Safety managed through audits, procedures, and lagging/ leading indicators

\- Rules-based energy management and emissions tracking driven by expert judgment

## To...

Not exhaustive

• Real-time, AI-driven planning continuously reoptimizing production, logistics, and product slate using live plant and market data

\- Autonomous, plant-wide closed-loop optimization, AI-driven blending optimizing quality, yield, and cost in real time

\- AI-enabled stochastic optimization dynamically balancing inventories and logistics across scenarios to maximize margin

\- AI agents orchestrating maintenance end-to-end predicting failures and prioritizing interventions

\- AI continuously stress-testing scope and sequencing across thousands of scenarios identifying optimal paths much more quickly

\- AI-enabled continuous risk sensing and incident prediction

\- Model-driven, scenario-based optimization under real-time constraints

## AI is unlocking several high-impact applications across the refining value chain

## 1 Planning and Scheduling

## 2 Operations

<table><tr><td>AI-driven crude slate and margin optimizer</td><td><img src="images/c51183590e82ef097bf5c3f5ededfac1694d140d195dae89a3982235cfe08e4a.jpg"/> AI-assisted real-time optimization, control room</td><td>AI inventory reconciliation and loss detection</td></tr><tr><td><img src="images/f177c340d09331cf29ea89e20881f74b952629b0fd95e02b2abba16e46c24b39.jpg"/> AI-based short-interval scheduling optimizer</td><td>Lab and quality analytics for spec giveaway prevention</td><td>Integrated logistics network and transport optimization</td></tr><tr><td><img src="images/e9d7ed857314c71cbfbd405113cf4bffab3ca04643080d44b440341651678e76.jpg"/> Automated plan-to-actual root cause diagnosis and learning</td><td><img src="images/1e68302b85e52f15f35e3894e2c3fc646598f23936a60c06e514016776fe4c6e.jpg"/> AI energy management optimizer</td><td><img src="images/7f7f15cca81bc75d50ec6d3e322b93c41727ebb76a733bbe2f701f2a9b70d0da.jpg"/> Market structure prediction for proactive trades</td></tr><tr><td>Automated multi-scenario refinery planning and feasibility</td><td></td><td></td></tr></table>

## 3 Logistics and Trading

## 4 Maintenance and Reliability

## 5 Turnarounds and Projects

## 6 HSSE

<table><tr><td>Predictive maintenance platform</td><td><img src="images/db00bf82c64c6f681d02affb4025c53dfd8d7c20125d1767b967ce27c467d24d.jpg"/></td><td>Integrated turnaround planning and resource scheduler</td><td><img src="images/40d68ff4ce944d2d6ade231cf16a64a47094b54eaf0623e9eda64b0c72c067af.jpg"/></td><td>Predictive safety risk and incident detection</td></tr><tr><td><img src="images/531ff38b320a96f5f2d3326b66c125cb6e88239f957c86b57fb5da5431386b85.jpg"/> Risk-based inspection and integrity analytics</td><td colspan="2">Turnaround execution control tower</td><td colspan="2">Carbon intensity analytics, reporting automation</td></tr><tr><td>AI maintenance planning and scheduling optimizer</td><td colspan="2">AI-assisted inspection planning and execution</td><td rowspan="2" colspan="2"></td></tr><tr><td>AI-driven equipment strategy optimizer</td><td colspan="2">MOC and compliance co-pilot</td></tr></table>

Common business support functions (legal, HR, IT, procurement)
Material opportunities exist in these functions as well, but are not Chemicals-specific and therefore out of scope of this report

## AI has potential to improve refining EBIT by over 50% by 2030

2030 AI impact on EBIT $^{1}$ (\$/bbl)  
![](images/ecb4c5f7876ab8747f38e1b78ce5cdeb44f914b36888b2802df638e08d5bec0d.jpg)

1. For a reference player- mid-quartile. Examples of Al-levers in refining: gross margin (e.g. Al-driven real-time prescriptive input of optimal operating points, maximizing throughputs and yields value and optimal scheduling plan generation with Al algorithms), energy and utilities (e.g., real-time utility network monitoring and optimization to minimize energy and H2 cost), maintenance (e.g., LLM-based agents to support maintenance operators in end-to-end execution including work order generation, image-based unit diagnostics, repair instructions, and log and report automation), CapEx run and maintenance (e.g., capital deployment optimization based on risk-based optimization of project selection supported by Al algorithms). 2. Logistics, maintenance, G&A.

![](images/6b12ecbc208e30223f2a83f2e48ff2b35e8a347914b6966093fdf212b300a4b9.jpg)

## AI improves margin and operational performance through adaptive scheduling that rapidly reoptimizes under changing conditions

## The challenge

At a Southeast Asian refiner, short-term scheduling was constrained by:

• High complexity across units, tanks, logistics, and time

\- Manual/Excel-based scheduling focused on feasibility over value maximization

\- Slow response to disruptions leading to margin leakage

## The Impact

\~0.15 - 0.30 \$/bbl
Margin uplift

![](images/940b7e3f361672a269cc7d694c07927461c560d73c04b0d9c7405b407f63ffad.jpg)

## How AI played a role

AI scheduler runs a digital twin to dynamically reoptimize short-term refinery operation schedule as operational variability occurs

## Live Detailed Digital Twin

AI uses the digital twin as the executable model of refinery state, flows and constraints

![](images/2280c6c001efbadc7ffd3fc384ecc805969bff030cf3bc1ba7b47d48a04cda63.jpg)

Inventory
management

## Operational Variability

A crude ship arrives later than scheduled

A refinery unit suddenly shuts down

AI reoptimizes routing, blending, inventory, and dispatch in minutes, dynamically updating the 30-60 day plan to be as close as LP as conditions evolve

Updated detailed 30-60 day plan

## LP plan (long term)

Increased
throughputs

Improved yields and giveaway

Access to
opportunity
crudes

Optimized
Inventory
management

Minimized
demurrage
cost

## Planning and Scheduling

## AI pinpoints margin leakage and analyzes root causes across the integrated value chain to protect refinery margin

## The challenge

At a European downstream major, operational performance analysis was challenged

• Traditional backcasting focused on isolated KPIs, not total margin

\- Limited visibility into value leakage across trading, refining, and sales

• Manual, slow root-cause analysis

## The Impact

\~1 - 3 \$/bbl
Identified opportunity $^{1}$

![](images/0d1060335ff9c7d3bbff108e43ae9d5889487fbf4aa53eb3842193018de69c19.jpg)

## How AI played a role

AI detects plan-to-actual margin leakage by comparing actual performance with reference scenarios and surface actionable drivers

## Capture

## Unify Data and Codify Logic

Ingest diverse internal, cloud, and external data sources

![](images/5ac430adeba2369060cdcc63ad207a69a78b74e15e9be5798b617bf5f89f8b31.jpg)

![](images/75535077c74195fb2c54a7049b7bf3075ad9de9c90fe5a540be5628125b5b6a1.jpg)

Internal Data

![](images/cc85c4f55cc6804fd9f58e6e7767cf94bb25656531c2f9bea114b1d91ad03b90.jpg)  
External Data  
Execution leakage  
Planning leakage

Cloud
Data

## Analyze

## Advanced Analytics + Cloud Architecture

Decision-quality gap

Structural upside gap

![](images/dc0b35d0d333921b88420ae8a1211ee6a6027316ec01507297ab8daecb373954.jpg)  
Optimize Margins

Total identified opportunity

\- Integrate trading, refining, and sales data with standardized margin calculation logic

• Establish baseline for plan and reference scenarios - Compare scenarios with plan and actual performance to size \$/bbl margin leakage

• Automate root causes analysis across leakages

## Act

![](images/31cc4622d776317e6a63c0c36372038cedd812680962997dd78fbc6e6e179620.jpg)

\- Surface margin improvement opportunities across value chain

\- Recommend actions on highest impact levers

## AI agents orchestrate real-time refinery optimization, translating plant conditions into margin actions for the control room

## The challenge

At a Latin American large refiner, operational performance was constrained by:

■ High operating variability (feed/utility swings, unit constraints)

■ Manual, slow diagnosis and response, driving margin leakage

■ Decision making was siloed, remaining unit by unit and shift by shift

## The impact

+\$80M from \~300 kbpd capacity

![](images/04d08d1a1b4a34824eed86e1c73bffb089be59cbc9485ad5ad4d95da6eef22e1.jpg)

## How AI played a role

AI agents orchestrate real-time refinery optimization by combining plant data, KPIs, alerts, and historical knowledge to detect issues early, optimize trade-offs, 

[中间内容因长度限制已省略]

ires an early focus on prioritized opportunities before expansion and scale-up

\~3 months

\~12 months

\~18 months

\- Define North Star vision

\- Prioritize value pools and identify quick wins

\- Establish governance

![](images/0bf4ef54c7b20a851b232f359360fdeba3f8d456360de8955780cc3ac2ffe252.jpg)

Phase 2 Focusing on acceleration

\- Address foundational gaps and outline people, operations, and a tech roadmap

\- Conduct pilots to prove value

\- Upskill leadership and define the shape of the organization and talent

Phase 3 Scaling lighthouse pilots

• Transform the prioritized scope end to end

• Institutionalize value tracking and adoption

\- Enable large-scale upskilling and change management

\- Launch the next wave, replicating across sites and functions

\- Move from productivity to differentiation

• Continuously scale and upgrade the foundation (including data and tech capabilities) and the workforce

Underpin the transformation journey with increasing investments in enterprise foundations including core tech and data, people, and responsible AI

## Is my organization on track to be AI future-ready? Leaders' checklist

<table><tr><td><img src="images/1a9b99c3bb245822f3b7bae60c0b815e7a06d26278f187acfdbd80a024397f4c.jpg"/></td><td>Leadership and strategy set the direction</td><td>AI is a strategic priority communicated to the organizationI have a named AI sponsor (C-level or board level)Al progress is a standing agenda item in leadership meetings</td></tr><tr><td><img src="images/fd5bc5a219a420649c0d315533f8370dd5463f4e5d06066d4cc9b520bda888a5.jpg"/></td><td>Solutions and business value determine priorities</td><td>We&#x27;ve identified functions or E2E processes where AI can create tangible valueWe prioritize use cases identified for each function, with target outcomesEach use case has a business sponsor with P&amp;L accountabilityWe track both business ROI and operational outcomes from AI cases</td></tr><tr><td><img src="images/422c63ecca55f85cd257939e6f30ced13d6f57d91d820ecd6103b49df8d808c2.jpg"/></td><td>Funding and investment back it with resources</td><td>Our leadership has a standard way to request AI funding that communicates ROII have an approved budget for AI-ready data, talent, and implementationThere is a defined three-year AI investment envelope (% of revenue)</td></tr><tr><td></td><td>Data and technology build the foundation</td><td>Named data owners/stewards exist in business units or functions (e.g., operations, maintenance)We have an active program cleaning, governing, and integrating refinery data from control business systems (including DCS/SCADA, APC, MES, CMMS)Our critical data is AI ready (structured and labeled, accessible, compliant)</td></tr><tr><td><img src="images/f7fb4e6a5c501af3c24ce3042c2c7ca19fef53da67e31ad4272ef13245989227.jpg"/></td><td>People and processes drive adoption</td><td>Our leadership team is undergoing AI fluency trainingWe have cross-functional AI teams that combine refinery domain experts (field operations, process engineering, maintenance) with OT/IT and Centers of ExcellenceThere is a change management plan to address trust, compliance, and regulationWe have an AI talent plan to attract, retain, and motivate talent</td></tr><tr><td><img src="images/ad84ff2de9cf87af50cb2a984e5fa1087044898cf66938d922082e299076129b.jpg"/></td><td>Governance and responsible AI scale with trust</td><td>Wins and lessons learned from pilots communicated visibly across the organizationWe have an AI governance council (ethics, compliance, regulatory).We operate under a responsible AI framework (safety, explainability, bias)I receive a quarterly AI impact report with business and operational outcomes</td></tr></table>

BCG experts | Key contacts for refinery AI transformations

![](images/49f96d6eed584aa75291510e971b301564df00c841e8f1d3be84f4643b66e2e6.jpg)

## Americas

![](images/2fea1108d1d4e408856d5c94ae29b048e6429e57e29d3b9d0deffdf123cbaf70.jpg)

![](images/d9f4c662227007eaa223d47d943737951110692b42014343c17b1890cc34932b.jpg)

Ilshat
Haris

Oleg
Gubin

![](images/2e0c73599c6aca1c968532a5cf73ec6d540b20fdb27fe25278f3bdca3769e63b.jpg)

![](images/7e433f4771d95fff933834dce54477331cf6222887b8a90fd0feaa3fd4307325.jpg)

John
Florez

![](images/c649f283cc4c886cb77d09d55e64f55766d92c5e3e239a3a8c0ef8c4aca6157b.jpg)

Buddy Myers

Elisabet Assens
Gibert

![](images/bd156b9775785916be4223be7a932715f56567528a0d23121cd7aaac60c2b35b.jpg)

Wade
Barnes

## Europe, Middle East, and Africa

![](images/f59a9a5c4e481d5467c0c491efae5237d3571475a8f55dfdba5d7e5f1698f6b8.jpg)

Alex
de Mur

![](images/eb2fd72fb1cf03bcfdcfe9e51abd516aeebaa5d7671128ebffbf88360d533a82.jpg)

Alberto
de la Fuente

![](images/4fdc4000519a2288b07dcba7360843ce9a0ae29825cce9ccd516ce044171d8ad.jpg)

Jaime
Ruiz-Cabrero

![](images/bf7f0b73b454860ef570c1a752270c05682a318547b2612d5ebe0c6704bc5b0c.jpg)

Ana María
Martínez

![](images/be5c1bebff245908c9bd420d0e53c20f7d00b1058c767d4ddcdb0cd46773bd16.jpg)

Sébastien
Rexhausen

![](images/1b87192a37d8800cf1ddd130a1f5c2fad024724aea33b6a4447f897be1b7da9a.jpg)

Arthur
Akhmetov

## Asia Pacific

![](images/a0c79f7fe88e94845573074093cdc7a3deee98baa349acbbb40d27d27f567b79.jpg)

![](images/f01bdec39ea6948666f8b3add50259e5240e280e016ef8d3314827f46aea5fed.jpg)

Arun
Rajamani

Asheesh
Sastry

![](images/350145fdeb932a10f8eeb14771e19f9f64c6b62a402178e76f77dac4bc291098.jpg)

Rahool Pai
Panandiker

![](images/0b5439d2dbb41e00606d4cb54781fe18d4b6361069d261512815cb49cd920d12.jpg)

Kashmira
Jirafe

![](images/15d341a11ac51d43d7986a43bd7b45f22813761d3752b4d1fcf20ad7138db02d.jpg)

Anish
Nazimudeen

![](images/053b66f6f3422e6fdbdeb2831a68308439ace4951bddda67f394067aa8b4100c.jpg)

Achraf
El Ouali

## BOG
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
