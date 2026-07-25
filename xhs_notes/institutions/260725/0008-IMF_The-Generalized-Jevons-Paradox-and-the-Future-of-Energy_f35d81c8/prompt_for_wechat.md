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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The Generalized Jevons Paradox and the Future of Energy

William Oman, Etienne Espagne, and Jean-Baptiste Fressoz

WP/26/157

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/7e0852b3460244e3b0b167049ccfaa2aa91fc2fef7b91c8d288b82e2ab18abfa.jpg)

IMF Working Paper
Monetary and Capital Markets Department

The Generalized Jevons Paradox and the Future of Energy Prepared by William Oman, Etienne Espagne, and Jean-Baptiste Fressoz

Authorized for distribution by Marina Moretti
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Global energy and materials are essential to the functioning of the economy and have significant implications for macroeconomics and the environment. At the same time, the world is not on track to meet Paris Agreement goals. This paper documents two stylized facts that connect these observations. First, the world economy is characterized by large embedded emissions and materials: different energies and materials are deeply entwined and interdependent. This has historically led to additive – rather than substitution – dynamics in energy and materials on a global scale. Second, historically there has been a strong positive correlation between efficiency in resource use and total resource use at a global scale. We synthesize these observations by introducing the Generalized Jevons Paradox (GJP). We argue that the GJP reflects the direct and indirect energy/material demand effects of long-term energy and material interdependencies, themselves shaped by market and geoeconomic power, trade arrangements, and financial factors. While future scenarios may diverge from historical data, including because of different population and growth trends, the GJP calls for caution in projecting energy and material flows within the energy transition framework, as it suggests that a declining share of fossil fuels in primary energy consumption can coexist with rising total fossil consumption, and thus rising global emissions – as observed since 2012. The GJP highlights the importance of policies to better allocate energy and material flows across sectors and countries and reduce supply chain vulnerabilities, but raises difficult distributional and political economy questions. Based on the GJP, the paper identifies three areas for research: the detailed analysis of the role of materials in supply chain vulnerabilities; the political economy of material flows; and multidimensional welfare analysis in decarbonization scenarios.

JEL Classification Numbers:

L72, O13, P18, Q43, Q54

Keywords:

Energy; Materials; Economic Growth; Climate Change

Author's E-Mail Address:

WOman@imf.org; Espagnee@afd.fr; jean-baptiste.fressoz@ehess.fr

# The Generalized Jevons Paradox and the Future of Energy

Prepared by William Oman, Etienne Espagne, and Jean-Baptiste Fressoz $^{1}$

## Contents

Executive Summary ....4   
Introduction ....6   
Empirics: Energy Transition or Energy Addition?....10 Present....10 Energy Transition?....10 Energy Addition....12 Past....19 Energy Transition?....19 Energy Addition....19 Hypotheses about the Future....19   
Interpretation....21 Past....21 Present....24 Hypotheses about the Future....24   
Theory: Energy Transition Framework vs. Generalized Jevons Paradox....26 Limits of the Energy Transition Framework....26 Key Concepts....28 Jevons Paradox....28 Energy Symbiosis....29 Generalized Jevons Paradox....29 Elements of Formalization....35   
Implications for Economic Research....40 Detailed Analysis of the Role of Materials in Supply Chain Vulnerabilities....40 Political Economy of Material Flows....41 Multidimensional Welfare Analysis of Scenarios....41   
Conclusion....42   
Annex I. Evolution of Global Energy Mix and Electricity Generation Mix....44   
Annex II. Empirical Relationship Between Energy Efficiency and Total Resource Use....45   
Annex III. Environmental Footprints Embedded in International Trade....48   
Annex IV. Embedded Emissions and Materials (Energy Symbiosis) Channels....49   
Annex V. Elements of Formalization: Kaya Identity....50   
References....51

## BOXES

Expected Profitability and Investment in the Solar Industry 32

## FIGURES

1. No Energy Transition, but an Energy Addition....11
2. Declining Carbon Intensity of Global Economy and Rising Emissions: 1820-2022....12
3. Strong Positive Relation Between Efficiency of Resource Use and Global Resource Use....13
4. Rising Electricity and Gas Consumption in the Oil and Gas Sectors....14
5. High Emissions Embodied in International Trade: France, UK, Norway....16
6. Consumption-Based GHG Emissions Per Capita in Lower-Carbon Economies....17
7. France: GHG Footprint Borken Down by Category....18
8. Embedded Emissions and Materials in 1850 and 1930....23
9. Embedded Emissions and Materials in 2050....25
10. Direct and Indirect Industry Linkages Challenge the Green/Brown Industry Dichotomy....28
11. Articulation of Jevons Paradox, Symbiosis and Generalized Jevons Paradox....30
12. Generalized Jevons Paradox: Key Actors and Institutional/Structural Drivers of Investment....31
AIII.1. Global Trade Flows and Ecological Pressures Across Six Planetary Boundaries....48
AIV.1. Illustration of Some of the Key Economic Channels of Embedded Emissions and Materials (Energy Symbiosis)....49

## TABLES

Table 1. Main Differences Between the Energy Transition Framework and Generalized Jevons Paradox ..... 37
Table 2. Key Features of the Energy Transition Framework and Generalized Jevons Paradox ..... 38
Table AI.1 Global Energy Mix ..... 44
Table AI.2 Electricity Generation Mix ..... 44
Table All.1 OLS and Median Quantile Regressions: Energy Efficiency and Total Emissions ..... 45
Table All.2 Theil-Sen Estimator: Energy Efficiency and Total Emissions ..... 45
Table All.3 OLS and Median Quantile Regressions: Water Use Efficiency and Total Water Use ..... 46
Table All.4 Theil-Sen Estimator: Water Use Efficiency and Total Water Use ..... 46
Table All.5 OLS and Median Quantile Regressions: Total Nitrogen Used for Agriculture and Agriculture Nitrogen Use Efficiency ..... 46
Table All.6 Theil-Sen Estimator: Total Nitrogen Used for Agriculture and Agriculture Nitrogen Use Efficiency . 47
Table All.7 OLS and Median Quantile Regressions: Share of Electricity in Total Final Energy Consumption and Total Energy (or Fossil Fuel) Consumption ..... 47
Table All.8 Theil-Sen Estimator: Share of Electricity in Total Final Energy Consumption and Total Energy (or Fossil Fuel) Consumption ..... 47

## Executive Summary

Global energy and material dynamics are essential from both a macroeconomic and environmental perspective. They matter for countries' energy and resources security (e.g., through higher or lower dependence on imported fuels or other resources), economic growth (as energy and materials are key complements in production), employment (in low-carbon energy and related sectors), balance of payments (including by reducing energy import costs and financing needs), and economic stability (e.g., via lower volatility induced by fossil fuel markets and other commodity markets). In turn, the composition and size of economic activity determine environmental impacts through the burning of fossil fuels, the release of pollution by metals mining and processing, and other channels. This is particularly important at the current juncture, as the world is not on track to meet Paris Agreement goals, and large subsidies prolong reliance on fossil fuels.

The standard framework for thinking about energy and material dynamics rests on two strong assumptions. First, global energies and materials are assumed historically to have been governed by substitution dynamics, where dominant energies and materials would have replaced each other over time, focusing on market shares. This assumption is then projected into transition scenarios about the future of energy. Second, energy and material dynamics are assumed to largely mirror technological dynamics, hence implicitly assuming away multiple sources of technological and material interdependence and path dependence. The dominant approaches to climate change mitigation frame the solution as an energy transition: substituting high-carbon energy sources with low-carbon ones, mainly through carbon pricing policies – the instruments that are expected to trigger technological progress and diffusion, and ultimately energy substitution, facilitated by trade, with no need to reduce global energy and material demand.

A more cautious interpretation of the data is possible. Despite numerous technological innovations in the $20^{th}$ and $21^{st}$ centuries, the total consumption of all energies and materials has increased over time (the only exceptions being sheep wool, asbestos, and mercury). In other words, the evidence suggests that material flows are governed by additive – rather than substitution – dynamics. This basic observation is critical, because what matters for climate change is the total quantity of GHGs in the atmosphere. In the past, eliminating some sources of energy was never a major policy or societal goal – in contrast to today, arguably. Based on this distinction, the standard framework assumes that replacing fossil electricity production with renewable electricity generation suffices to achieve decarbonization. However, while building renewable energy infrastructure to decarbonize global electricity production would generate a relatively small amount of $CO_{2}$ , downstream uses (goods, services and infrastructures powered by low-carbon electricity) entail material consumption that depends on fossil fuels and will likely continue to do so. Key examples are heavy industry, transport, food consumption, and the production of biofuels (deforestation). An important element of context is that the rapid growth in emissions in the $20^{th}$ century occurred in tandem with unprecedented economic and population growth, and it is unclear whether similar increases are replicable given different ongoing demographic and growth trends.

This paper presents evidence and analyzes mechanisms that, taken together, highlight the need for caution about the future evolution of global energy and material dynamics. First, drawing on economic history and more recent empirical evidence, it documents the existence of large and growing embedded emissions and materials: energies and materials are deeply intertwined, interdependent, and governed by additive dynamics. This results in the accumulation and entwinement of both "clean" and "dirty" technologies and materials at the level of the global economy. Second, the paper finds evidence of a strong positive

correlation between efficiency in resource use and total resource use at a global scale. To synthesize these observations, we introduce the Generalized Jevons Paradox (GJP). The latter captures the direct and indirect energy/material demand effects of the long-term energy and material interdependencies (or symbiosis) that accompany significant increases in resource use efficiency. In other words, the GJP underscores the apparent “stickiness” of global fossil and material consumption, notwithstanding the ability of a number of countries (encompassing both middle- and high-income economies) to decarbonize their electricity generation sector. The paper discusses possible drivers of the GJP: market and geoeconomic power, trade arrangements, and financial factors. The GJP therefore extends the classic Jevons Paradox by incorporating macroeconomic, institutional, and technological drivers that reinforce each other and thereby generate systemic rebound effects and material interdependencies. Importantly, the GJP should not be interpreted as an economic “law,” but rather as an empirical observation that emphasizes the need for caution in projecting future energy flows.

The GJP calls for caution in applying the Energy Transition (ET) framework, which assumes that technological substitution and efficiency improvements would naturally drive decarbonization. While technological substitution and efficiency improvements do reduce emissions to a small extent, they are not enough to get to zero emissions, as in some (growing) sectors – such as aviation, shipping, iron and steel, cement, plastics, fertilizers, agriculture, construction and arms – no (scalable) substitution with zero-emission technologies is possible in the near term or apparent in the medium term. The need for caution reflects institutional drivers of the GJP – market and geoeconomic power, trade arrangements, and financial factors – which shape investment decisions in a way that further entrenches fossil fuels in the global productive structure. The reason for this entrenchment is that, even with new, low-carbon materials, persistent material interdependencies and the continuous generation of new sources of material demand on a global scale put upward pressure on the total downstream consumption of many materials, and thus on emissions.

The analysis highlights some limitations of a technology-centered approach to climate change mitigation. It underscores the need for demand-side policy frameworks that can help better allocate energy and material flows across sectors and countries. This analysis contributes to an ongoing debate on the nature of growth, highlighting its energy, distributional and political economy underpinnings. The paper concludes by outlining avenues for future research: the detailed analysis of the role of materials in countries' supply chain vulnerabilities; the political economy of material flows; and multidimensional welfare analysis in decarbonization scenarios.

## Introduction

Global energy and material dynamics are essential from a macroeconomic perspective. Energy and materials are crucial to the functioning of the global economy. $^{1}$ They matter for countries' energy and resources security (e.g., through higher or lower dependence on imported fuels or other resources), economic growth (as energy and materials are key complements in production), supply chain resilience, employment (in low-carbon energy and related sectors), balance of payments (including by reducing energy import costs), and economic stability (e.g., via lower volatility induced by fossil fuel markets and other commodity markets).

Energy and material flows also matter for the economy through their impact on the environment. Energy accounts for over 75 percent of global emissions. In turn, climate change can affect countries' macroeconomic and financial stability (Mitra et al. 2025). Other environmental threats magnify these linkages (Gardes-Landolfini et al. 2024). The world is not on track to meet Paris Agreement goals, and large subsidies prolong reliance on fossil fuels (Black et al. 2025). There is evidence that climate change is accelerating, with temperatures and global emission records being broken year after year. In addition, biodiversity is declining at an unprecedented rate, with adverse consequences for ecosystem functioning, water availability quality, food security and nutrition, human, plant and animal health and resilience to the impacts of climate change (IPBES 2024, NGFS 2023). Climate change and biodiversity are interdependent and have compounding effects on human well-being. These interdependencies are notably reflected in the concept of planetary boundaries, seven of the nine identified boundaries having been crossed (Stockholm Resilience Centre et al. 2025). $^{2}$

Despite these growing environmental threats and the objectives of the Paris Agreement, emissions have continued to rise steadily, driven by increased fossil fuel consumption. To meet the Paris temperature objective of “well below” 2°C of warming, global greenhouse gas (GHG) emissions need to decline by around 5 percent per year over the next decades (and by around 7 percent if one accounts for the evidence of an ongoing sharp decline in carbon sinks – see Carle et al. 2025, Stock 2025, Ke et al. 2024, Pan et al. 2024, Curran and Curran 2025, Sohail et al. 2025). Over the last decades, however, the steady decline in the carbon intensity of the global economy has been accompanied by a significant rise in emissions. An important element of context is that the rapid growth in emissions in the 20 $^{th}$ century occurred in tandem with unprecedented economic and population growth, and it is unclear whether similar increases are replicable.

The persistence of fossil fuels in the global economy has implications for countries' energy security and balance of payments. It is widely agreed that a shift away from fossil fuels to renewable energy can bolster energy security by reducing dependence on imported fuels, create jobs in the low-carbon energy and related sectors, and enhance the balance of payments through lower energy import costs, while supporting economic stability via lower volatility induced by fossil fuel markets (IMF 2025a, p. 26). By contrast, many commodities exporting countries depend on the related inflows of foreign exchange to finance their imports of consumption and investment goods, including those needed for low-carbon investments (Moreno et al. 2024).

The simultaneous decrease in global carbon intensity and increase in emissions begs a question: is the conventional understanding of global energy and material dynamics accurate? Large increases in energy demand, driven by the growing world population and rising global GDP per capita, are a key reason why, in recent decades, emissions have continued to rise in tandem with falling carbon intensity. This explanation is insufficient, however, as it does not explain the level of carbon intensity. Rather, the “stickiness”

of global fossil and material consumption points to the criticality of understanding global dynamics of energy and materials – both the relationships among different forms of energy and the relationship between energy and materials – in absolute terms. Independently of the policy objective, having an accurate understanding of the drivers of energy and material flows is essential from a methodological perspective.

The conventional view is that global energy and material dynamics are – and have historically been – 

[中间内容因长度限制已省略]

aeger Publishers.

Smil, Vaclav. 2017. Energy and Civilization: A History. Cambridge, MA: The MIT Press.

Smil, Vaclav. 2022. How the World Really Works: The Science Behind How We Got Here and Where We're Going. New York: Viking Press.

Smil, Vaclav. 2024. Halfway Between Kyoto and 2050: Net Zero is a Highly Unlikely Outcome. Vancouver: Fraser Institute.

Sohail, Taimoor, Bishakhdatta Gayen, and Andreas Klocker. 2025. "Decline of Antarctic Circumpolar Current due to polar ocean freshening." Environmental Research Letters 20, no. 3: 034046.

Solow, Robert M. 1971. "The Economist's Approach to Pollution and Its Control." Science 173 (3996): 498–503.

Solow, Robert M. 1974. “The Economics of Resources or the Resources of Economics.” The American Economic Review 64 (2): 1–14.

Sorrell, Steve, John Dimitropoulos, and Matt Sommerville. 2009. “Empirical Estimates of the Direct Rebound Effect: A Review.” Energy Policy 37 (4): 1356–71. https://doi.org/10.1016/j.enpol.2008.11.026.

Sørensenrensen, Bent. 2012. A History of Energy: Northern Europe from the Stone Age to the Present Day. London: Routldege.

Stanway, David. 2023. “China climate envoy says phasing out fossil fuels 'unrealistic.'" Reuters, September 22.

Stapczynski, Stephen, Akshat Rathi, and Josh Saul. 2025. “AI-Driven Demand for Gas Turbines Risks a New Energy Crunch.” Bloomberg News, October 2.

Stern, Nicholas H. 2007. The Economics of Climate Change: The Stern Review. Cambridge: Cambridge University Press.

Stern, Nicholas H., and Joseph E. Stiglitz. 2021. “The Social Cost of Carbon, Risk, Distribution, Market Failures: An Alternative Approach.” NBER Working Paper No. 28472. Cambridge, MA: National Bureau of Economic Research.

Stiglitz, Joseph E. 1974. “Growth with Exhaustible Natural Resources: Efficient and Optimal Growth Paths.” The Review of Economic Studies 41: 123–137.

Stock, Petra. 2025. “Australian tropical rainforest trees switch in world first from carbon sink to emissions source.” The Guardian. October 15.

Stockholm Resilience Centre. 2025. “Seven of nine planetary boundaries now breached.” Retrieved from: https://www.stockholmresilience.org/news--events/general-news/2025-09-24-seven-of-nine-planetary-boundaries-now-breached.html

Tong, Dan, Qiang Zhang, Yixuan Zheng, Ken Caldeira, Christine Shearer, Chaopeng Hong, Yue Qin, and Steven J. Davis. 2019. "Committed emissions from existing energy infrastructure jeopardize 1.5 °C climate target." Nature 572, no. 7769: 373–377.

Tubiana, Laurence, Richard Baron, Samuel Leré, and Matthew Langdon. 2025. "Embodied carbon: Understanding our trade and climate co-dependency." In: Industry on the road to 2050: A report prepared for the Climate Club. Paris: Climate Club.

U.S. Printing Office. 1954. “Stockpile and Accessibility of Strategic and Critical Materials in a Time of War, Part 6: Petroleum, Gas, and Coal.” Washington DC: U.S. Printing Office.

Vogt-Schilb, Adrien, Guy Meunier, and Stéphane Hallegatte. 2018. "When starting with the most expensive option makes sense: Optimal timing, cost and sectoral allocation of abatement investment." Journal of Environmental Economics and Management 88: 210-233.

Waide, Paul, and Conrad U. Brunner. 2011. “Energy-Efficiency Policy Opportunities for Electric Motor-Driven Systems.” IEA Working Paper. Paris: International Energy Agency.

Warde, Paul. 2007. Energy Consumption in England and Wales. Consiglio Nazionale delle Ricerche Istituto di Studi sulle Società del Mediterraneo.

Weber, Pierre-François, Amandine Afota, Maria Grazia Attinasi, et al. 2025. “The Intersection between Climate Transition Policies and Geoeconomic Fragmentation.” SSRN Electronic Journal, ahead of print. https://doi.org/10.2139/ssrn.5088766.

Weissenbacher, Manfred. 2009. Sources of Power: How Energy Forges Human History. Santa Barbara, CA: Praeger Publishers.

Weitzman, Martin L. 2009. "On Modeling and Interpreting the Economics of Catastrophic Climate Change." The Review of Economics and Statistics 91 (1): 1-19.

Weitzman, Martin L. 2011. "Fat-Tailed Uncertainty in the Economics of Catastrophic Climate Change." Review of Environmental Economics and Policy.

White, Edward, Wang Xueqiao, and Cheng Leng. 2025. “China steps in to tame animal spirits as solar sector racks up billions in losses.” Financial Times, September 3.

Wiatros-Motyka, Malgorzata, and Kostanta Rangelova. 2025. Global Electricity Mid-Year Insights 2025. London: Ember Energy.

Williams, Charles W. 1840. The Combustion of Coal and the Prevention of Smoke: Chemically and Practically Considered. First edition. London: J. Weale.

Wolff, Alan W. 2025. “International trade policy in a disrupted world.” Prepared remarks delivered at the Cairo Forum 2025, Egyptian Center for Economic Studies (ECES), Cairo. Washington, DC: Peterson Institute for International Economics.

Wrigley, Anthony. 2011. Energy and the Industrial Revolution. Cambridge: Cambridge University Press.

Xue, Xiaokang, and Mathias Larsen. 2025. China's Green Leap Outward: The rapid scale-up of overseas Chinese clean-tech manufacturing investments. Baltimore, MD: Net Zero Industrial Policy Lab.

Yaworski, Nicolas. 1938. Fuel Efficiency in Cement Manufacture, 1909-1935. Works Progress Administration, National Research Project and Department of the Interior, Bureau of Mines.

Yokoi, Ryosuke, Takuma Watari, and Masaharu Motoshita. 2022. "Future greenhouse gas emissions from metal production: gaps and opportunities towards climate goals." Energy & Environmental Science 15, no. 1: 146-157.

Zhang, Shuwei. 2023. “Why China’s renewables push fuels coal power investment.” Beijing: China Dialogue.

![](images/e8451c21ef2e1886bffca169ab94d025ba700080f6149074c087e83b0c1dc967.jpg)
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
