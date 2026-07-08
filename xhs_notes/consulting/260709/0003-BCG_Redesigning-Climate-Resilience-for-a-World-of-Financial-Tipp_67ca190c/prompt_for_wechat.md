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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/8c528b98795362b7c843370cf86d997dc4071575c6e427a2bd37f0363c1961de.jpg)

CLIMATE CHANGE AND SUSTAINABILITY

# Redesigning Climate Resilience for a World of Financial Tipping Points

By Maurice Berns, Edmond Rhys Jones, Nadine Moore, Lorenzo Fantini, Charmian Caines, Aashay Patil, and Eden Cottee-Jones

ARTICLE JULY 08, 2026 8 MIN READ

Climate-driven losses do not occur in isolation. They cascade through financial systems in ways conventional models miss and risk triggering abrupt shifts at financial tipping points. We’ve now reached a point where the systems designed to manage the impacts of climate events through our financial and social infrastructure—insurance, reinsurance, credit, commodity hedging, municipal and sovereign debt—are struggling to keep up with a world of more frequent crises. And these crises are now impacting a broad range of sectors, from agricultural commodities to municipal bonds and sovereign credit markets. Addressing this challenge requires cooperation among businesses, insurers, and policy makers.

In response, both the public and private sectors need a new approach to climate resilience. The first generation of climate resilience strategy focused on reducing physical damage. While this work is ongoing, the next stage must build financial resilience that helps economies absorb shocks, manage losses, and keep recovery moving. It also must strengthen societal resilience, so that climate costs do not substantially impact households, local demand, and public finances. In short, new indicators are needed that cover financial and societal stresses, as well as physical.

Consider the insurance industry, where global insured losses from natural catastrophes have quadrupled since 2000. In the same timeframe, key mechanisms to syndicate those losses—reinsurance and capital markets—have decreased by nearly two-thirds relative to those losses. But addressing financial tipping points requires resilience strategies that go beyond insurance. Leaders need to identify indicators of systemic risk, strengthen the financial systems that absorb and distribute losses, and ensure that the costs of climate change do not fall most heavily on those least equipped to bear them.

There is no single template to meet this challenge. Every community and value chain faces a different mix of physical hazards, financial fragility, and social vulnerability. Strategies need to be co-developed by coalitions of governments, financial institutions, businesses, and capital markets—today, we often see actions being taken piecemeal. So, what are some of the potential actions for each dimension of resilience?

# Physical Resilience: Follow the Financial Faultlines

Physical resilience is the capacity of assets, infrastructure, and essential services to withstand climate shocks, recover quickly, and continue functioning after direct physical damage. Investments in physical resilience are typically driven by environmental hazard assessments such as flood probability, wildfire exposure, and potential wind damage. These assessments should certainly continue, but they should be complemented with an analysis of associated financial and societal risk indicators.

For example, in the US, five states receive roughly 80% of combined federal and state disaster-mitigation funding. These include the most disaster-prone states in the country, such as Florida, Louisiana, and California. But a second group—Mississippi, North Carolina, Oklahoma, and others

Sources: National Oceanic and Atmospheric Administration; Federal Emergency Management Agency; US Department of Agriculture; US Department of Housing and Urban Development; individual state government websites; "Next to Fall: The Climate Driven Insurance Crisis is Here—and Getting Worse", Senate Budget Committee; BCG analysis. $^{3}$ Includes spending on programs that boost property resilience, with a focus on hazard mitigation against disaster recovery. Excludes funding for areas that have limited bearing on property damages, such as agriculture, energy, transportation, health care, water quality, biodiversity, and others. Log scale used to account for the spread in state resilience expenditure. $^{2}$ Refers to the bottom 20% of states by share of homeowner insurance policies not renewed by insurers in a particular year; data for 2023. $^{3}$ As per the "Expected Annual Loss – Building Value" metric in FEMA's National Risk Index.

—already show comparably high homeowners’ insurance non-renewal rates despite lower physical hazard scores. (See Exhibit 1.) A major disaster in one of these states could produce financial fallout well beyond what the physical damage alone would suggest, because the local mechanisms for responding to losses are already thin.

EXHIBIT 1 Integrating Financial Stress Indicators Changes Adaptation Spending Priorities  
![](images/2bfd09da97b347232e56da697c51787a7b28bab8dcd192ab99323e5d56322be0.jpg)

Because tipping points are most likely to occur in places where physical risk, financial fragility, and social vulnerability overlap, the lesson is to consider and address all three dimensions. Financial indicators—such as rising insurance premiums, homeowner’s insurance non-renewal rates, mortgage delinquency trends, municipal credit deterioration—should sit alongside physical hazard data when prioritizing adaptation investment.

# Financial Resilience: Redesign the Shock Absorbers

Financial resilience is the capacity of financial systems to absorb climate-driven losses, keep capital flowing, and continue pricing and sharing risk after a shock. Insurance covers roughly 40% of global climate losses—a share that has doubled in two decades. (See Exhibit 2.) In mature markets, it can reach 70%. But behind the primary insurance layer sit reinsurance and capital-market instruments that spread risk globally, and these backstops are not keeping pace.

## EXHIBIT 2

Losses from Natural Disasters Are Growing, with Higher Insurance Coverage Than Ever Before

ANNUAL LOSSES DUE TO NATURAL DISASTERS GLOBALLY $^{1}$ (\$B, 2024 DOLLARS, 5-YEAR MOVING AVERAGE)

![](images/775035d75945e7a1024d27f19229c4adc9a8e792cdd6495b073c3226c3a21825.jpg)  
Sources: “Natural Catastrophe and Climate Report: 2024”; Gallagher Re; BCG analysis. $^{1}$ Includes natural disasters linked to climate; excludes non-climate natural catastrophes such as earthquakes.

In fact, we found reinsurance and capital-market coverage had decreased relative to the rise in insured natural disaster losses by 60% in the last 20 years, meaning insurers are carrying more risk from climate-related losses that in the past had been syndicated more broadly. (See Exhibit 3.)

\$xx Reinsurance capital and catastrophe bonds (\$B, 2024 dollars, annual average)

# Major Sources of Insurance Capital Have Not Kept Pace with Rising Climate Losses

ANNUAL AVERAGE REINSURANCE CAPITAL $^{1}$ AND CATASTROPHE BONDS $^{2}$ AS A PROPORTION OF GLOBAL INSURED CLIMATE LOSSES $^{3}$

![](images/f86532355db80b342ce4bf8e62e60609a7029beae0c7f4547c8f5542c57fe1ae.jpg)  
Sources: “Natural Catastrophe and Climate Report: 2024”; Gallagher Re; Reinsurance Market Reports by Aon; Artemis; BCG analysis.
Note: Data adjusted for inflation using CPI-U annual average. $^{1}$ Includes only traditional (shareholder equity) reinsurer capital and excludes alternative sources of capital such as insurance-linked securities, sidecars, industry loss warranty, and collateralized reinsurance. $^{2}$ Includes only those catastrophe bonds that were specifically issued for climate- and weather-related perils. $^{3}$ Includes losses due to climate; excludes non-climate natural catastrophes such as earthquakes. $^{4}$ Comparable 2005 reinsurance capital data unavailable, but figures are annual averages in any case.

Markets around the world are grappling with similar pressures. Consider, for example, the devastating floods in Pakistan in 2022 or wildfires in California in 2025—very different contexts in terms of economic development and institutional capacity, yet both resulted in credit rating downgrades that raised borrowing costs at precisely the moment of greatest need. The pattern is consistent across both developed and developing economies: rising physical losses overwhelm financial mechanisms designed for a less volatile world.

Private insurance alone will not mitigate escalating tail risk at acceptable cost. The question is how governments, capital markets, and businesses should fill the gap—and the answer differs by market. We’ve seen several examples emerge:

\- Australia’s Cyclone Reinsurance Pool, administered by a government entity with an AUS\$10 billion guarantee, has cut reinsurance costs in cyclone-prone regions by 25% and lowered premiums for the highest-risk policyholders by 11%.

\- In the Caribbean, parametric instruments (where a payout is triggered by an environmental event) have delivered liquidity at speed. After Hurricane Melissa in 2025, the Caribbean Catastrophe Risk Insurance Facility paid out \$92 million to Jamaica within 14 days, fast enough to stabilize public services and reduce the country's economic exposure before localized damage could spread.

# Societal Resilience: Protect Affordability to Prevent Tipping Points

Societal resilience is the capacity of households and communities to absorb climate shocks without turning affordability stresses into wider financial and economic instability. However losses are allocated on paper, they land on households through premiums, taxes, utility bills, or reduced public services. When that burden becomes unaffordable for a significant number of households, the effects compound. Mortgage delinquencies rise, local demand weakens, fiscal capacity shrinks, and investment in future resilience drops—making the next shock harder to absorb.

The Federal Reserve Bank of Dallas found that an average homeowner's insurance premium increase between June 2022 and 2023 was associated with nearly 150,000 mortgages becoming delinquent within a year. Our own analysis shows that real insurance premiums in the highest risk US counties increased 11% from 2018–2022, while those in very low to moderate risk counties only experienced an increase of 2% to 4%. (See Exhibit 4.)

## EXHIBIT 4

The Most Hazard-Prone US Regions Have Seen Homeowner Insurance Premiums Rise 3–5x More Than Other Regions

PERCENTAGE INCREASE IN HOMEOWNERS' REAL INSURANCE PREMIUMS FROM 2018 TO $2022^{1}$ (%)

![](images/65096784efdc1a19c0b63cb02857856e6a8a6c124b5440c4463d8339b4e05b3c.jpg)  
Sources: “Property insurance and disaster risk: New evidence from mortgage escrow data,” Keys & Mulder, National Bureau of Economic Research, 2025; Federal Emergency Management Agency; American Community Survey, US Census Bureau; BCG analysis. $^{1}$ Risk categorization based on FEMA risk categories for counties. Calculation based on cost of property insurance estimated from mortgage escrow payments (not adjusted for inflation) reported to CoreLogic. Excludes counties where data not reported. Data adjusted for inflation using CPI-U annual average, all items, US city average.

In some US states, the excess losses from climate-related disasters are syndicated by flat levies across policyholders, which, depending on the distribution of wealth and risk, can result in low-risk and low-income homeowners paying the highest increase for disaster costs, in terms of share-ofwallet expenditure. To illustrate the challenge, an analysis of two hypothetical scenarios in Oregon, where excess losses were distributed by a simulated risk-based or income-based allocation, revealed significant cost burden differences across counties. (See Exhibit 5.)

Different Disaster Cost Allocation Methods Rebalance the Burden Across Oregon Counties with Varying Risk and Income Profiles

Risk-based extreme event cost distribution

![](images/dd13f03344f5a2514d39ae7aa44589b013f7eb7268f80b3521c03287781c50a6.jpg)  
Income-based extreme event cost distribution  
Sources: Federal Emergency Management Agency; US Census Bureau; BCG analysis. $^{1}$ Percentiles based on deviation in county's FEMA Risk value-based percentile rank within the state vs. state population weighted average percentile of all counties. $^{2}$ Percentiles based on deviation of county's average income vs. state's average income.

Designing cost allocation methodologies to better balance risk exposure and ability to pay can help break this cycle. And targeted investment in physical resilience for low-income communities reduces their exposure to future shocks, shrinking the pool of households most likely to default when the next event hits. If the cost of climate change falls disproportionately on those who cannot absorb it, the resulting stress—in mortgage markets, in local government finances, in household spending—becomes a transmission mechanism for wider instability.

# Who Needs to Act, and What They Can Do

Preventing climate-induced financial tipping points cannot be solved by one single entity or group. The challenge cuts across public and private sectors and all three dimensions of resilience.

Governments can realign incentives for businesses, insurance, and financial services to address this challenge. They could undertake broader risk assessments, at both national and municipal scale, to develop appropriate resilience strategies. They could also convene and develop multi-stakeholder solutions at a pace commensurate with the speed of climate change. This includes establishing backstop schemes for market-specific catastrophic climate risks—and designing those schemes with societal resilience front-of-mind.

Insurers can reconsider the way they work to achieve better outcomes. They could innovate more radically on product and fit-for-purpose solutions, act as a pathfinder when collaborating with governments and regulators, and adjust investment plans with financial tipping points in focus. This includes expanding offerings suited to sharper volatility, developing public-private partnerships at pace, and directing capital towards the most pressing physical adaptation investment opportunities.

Businesses in exposed sectors—such as utilities, real estate, logistics, agriculture, and financial services, among others—can look beyond their physical resilience and review their financial and societal resilience. This may involve contributing to public-private risk pools or deploying more financial instruments designed for increased volatility, such as resilience-incentivized loan terms. They could recognize that their dependencies on consumers, suppliers, and their own workforce are vulnerabilities to climate-induced financial tipping points. Arguing that a company was hit by “a perfect storm” is less credible with investors when the risks are increasingly visible.

Whether the risk is wildfires in Europe, storm damage in Asia, or floods in Australia, solutions can be found by bringing together the right local stakeholders. We find the problem is not simply more extreme events, but often the interaction of insurer retrenchment, utility liability, a constrained rate-setting regime, and growing numbers of uninsured households. No single reform addresses all these pressures.

The response typically demands an integrated architecture: separating catastrophic tail risk from the standard insurance market and creating multi-stakeholder funding structures. This reduces friction costs, particularly litigation, which diverts billions from rebuilding. It also replaces hindsight-based liability with forward-looking, compliance-based accountability. A logic of layering the risk, sharing it broadly, cutting system costs, and aligning incentives holds real promise.

While these solutions are anchored in insurance markets, many of the principles translate to other sources of financial tipping points. These include municipal and sovereign bond markets, which play a major role in financing infrastructure to enhance resilience and are impacted when climate risks are not priced in, leading to credit rating downgrades and increased debt servicing and borrowing costs. Another example is agricultural commodity markets, where production losses triggered by climate change are compounded by concentrated supply geographies and thin market liquidity, resulting in sharp, destabilizing volatility as documented in cocoa, coffee, rice, and other staples. In all cases, the impacts flow through to businesses and consumers in the real economy.

As climate-induced losses continue to grow in a non-linear fashion, the risk of overwhelming all three dimensions of resilience grows with them. The warning signals are visible in Florida's insurance market, in cocoa trading floors, in municipal bond spreads, and in sovereign credit assessments across economies exposed to climate risks. Leaders who invest now in forward-looking tools, cross-sector coalitions, and new resilience architectures will be in the strongest position when those signals turn into shocks.

The BCG Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors

![](images/dd6d1660957e27bc11ba7ba916fda11bd7f2c8947b068680b93f6ee29c8ea1fd.jpg)

![](images/22abe8261983aac53cb54e19174515c636eeca62b28a26ad2b246614a45e28a8.jpg)

![](images/2d1a33481c300cdf5eccdfdc3837c6783ed6d5c2bc206d38c2852340b64abde5.jpg)

![](images/e630e790fe2d015f06ec15e1bb62cd1a78730f72e549f96885d25fdbf796814b.jpg)  
Managing Director & Senior Partner; Chair, Center for Energy Impact
London

## Maurice Berns

![](images/fe5876e01b7d5e31971c12da3574ceea3471c5c196c6a79a8c1128171801b804.jpg)

## Nadine Moore

Managing Director & Senior Partner
Chicago

![](images/f30871ac657fa93ade3f640f21c898295a8e49f1938d278663950abdab698fb5.jpg)

## Charmian Caines

Managing Director & Senior Partner
London

![](images/3e9b7c41ab95784cfdcab82e6dbd07657fbe4cf295fd4f2b3bdd31400685ab1f.jpg)

## Eden Cottee-Jones

BCG Institute Senior Director
London Canary Wharf

![](images/07aa6bbb0e7b5a1ccab24b282de3c285781a7396bd888abf5c3ac302ec301082.jpg)

![](images/e0421371055d4f8a4667a9ca098ff8b71dbb35cadaa35e1169e98fd12aebc19a.jpg)

## Edmond Rhys Jones

Partner & Director, Climate Policy & Regulation
London

![](images/6a0e1c070d38a06c66babc104f83a807048513f57e2d9129bc1a2ee613d4afea.jpg)

![](images/f34ae7ae41adde9a251a5d1fd4f6c8d432d8bf23e8e60d37f786daedd4eb6973.jpg)

## Lorenzo Fantini

![](images/c096e607427e79eabe240435a282f4748a927c62f7df671958048fd31c33b72f.jpg)

Managing Director & Senior Partner
Milan

![](images/802dba294c277c1463166e1478adb18b2812983ff5fbf4c41722f11d942ef0a9.jpg)  
Aashay Patil

Project Leader
Mumbai

![](images/212403769bc2bff0ef7f0c3b25307d50496b60723f1d25e945503f0c1fb85399.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
