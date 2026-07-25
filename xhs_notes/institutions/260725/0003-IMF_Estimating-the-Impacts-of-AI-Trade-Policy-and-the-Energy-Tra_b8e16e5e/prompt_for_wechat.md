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
# Estimating the Impacts of AI, Trade Policy, and the Energy Transition: An Application to Ireland

Mohammad Khabbazan

SIP/2026/070

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 10, 2026. This paper is also published separately as IMF Country Report No 26/157.

2026
JUL

![](images/99bcf49310234c50ae445e443753e8d365e9ce169d53681858673002ef5f4a59.jpg)

# IMF Selected Issues Paper European Department

# Estimating the Impacts of AI, Trade Policy, and the Energy Transition: An Application to Ireland Prepared by Mohammad Khabbazan

Authorized for distribution by Ms. Yan Sun
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 10, 2026. This paper is also published separately as IMF Country Report No 26/157.

ABSTRACT: Developments in trade policy, AI, and the energy transition are shaping small open economies. This paper uses a static, multi-region, multi-sector computable general equilibrium model to assess the impacts of these forces on Ireland in the long run through three channels: (i) current tariffs and trade agreements, (ii) AI-driven productivity gains, and (iii) carbon pricing, abstracting from short-run dynamics and frictions. The findings suggest that (i) the current trade policy shocks primarily redirect trade across partners and sectors, with modest aggregate output and export effects; (ii) AI-driven productivity gains can generate strong output and export growth, particularly in knowledge-intensive sectors, while inducing significant sectoral labor reallocation and distributional implications across factors of production which needs to be managed; (iii) carbon pricing can play a key role in addressing rising energy demand from AI and offsetting emissions, by shifting production toward lower-emission activities and increasing the renewable share in electricity generation.

RECOMMENDED CITATION: Khabbazan, Mohammad. 2026. “Estimating the Impacts of AI, Trade Policy, and the Energy Transition: An Application to Ireland.” IMF Selected Issues Paper (SIP/2026/070). Washington, DC, International Monetary Fund.

JEL Classification Numbers:

D58; F15; F17; O33; Q58.

Keywords:

Artificial Intelligence; Carbon Pricing; Computable General Equilibrium Model; Ireland; Tariffs; Trade Policy.

Author's E-Mail Address:

mmkhabbazan@imf.org

SELECTED ISSUES PAPERS

# Estimating the Impacts of AI, Trade Policy, and the Energy Transition: An Application to Ireland

Prepared by Mohammad Khabbazan $^{1}$

## IRELAND

SELECTED ISSUES

June 10, 2026

Approved By

Prepared by Mohammad Khabbazan (ICD)

European Department

## CONTENTS

ESTIMATING THE IMPACTS OF AI, TRADE POLICY, AND THE ENERGY TRANSITION: AN APPLICATION TO IRELAND 3
A. Introduction 3
B. Model Framework and Scenario Design 4
C. Tariff and Trade Agreements: Re-Shaping Global Trade 7
D. Artificial Intelligence and Productivity Gains 10
E. Carbon Pricing Policy and Trade-Offs 15
F. Concluding Remarks 20

## FIGURES

1. Real GDP and Price Index Impacts in Tariff and Trade Agreements Scenarios 7
2. Real Export and Export Price Impacts in Tariff and Trade Agreements Scenarios 8
3. Selected Sectoral Real Output and Real Export Impacts in Tariff and Trade Agreements Scenarios 10
4. Selected Sectoral Labor Movement in Tariff and Trade Agreements Scenarios 10
5. Real GDP and Price Index Impacts in AI-Driven Productivity Gains Scenarios 11
6. Real Export and Export Price Impacts in AI-Driven Productivity Gains Scenarios 12
7. Selected Sectoral Real Output and Real Export Impacts in AI-Driven Productivity Gains Scenarios 13
8. Renewable Share in Electricity Productions and CO2 Emission in AI-Driven Productivity Gains Scenarios 14
9. Selected Sectoral Labor Movement in AI-Driven Productivity Gains Scenarios 15
10. Real GDP and Price Index Impacts in Carbon Pricing Policy Scenarios 16
11. Renewable Share in Electricity Productions and Carbon Price in Carbon Pricing Policy Scenarios 17
12. Real Export and Export Price Impacts in Carbon Pricing Policy Scenarios 18
13. Selected Sectoral Real Output and Real Export Impacts in Carbon Pricing Policy Scenarios 19

14. Selected Sectoral Labor Movement in Carbon Pricing Policy Scenarios \_\_\_\_ 19

## TABLES

1. Scenario Description \_\_\_\_ 6
2. Trade Flows in Tariff and Trade Agreements Scenarios \_\_\_\_ 9
3. Selected Macro Indicators in Tariff and Trade Agreements Scenarios \_\_\_\_ 9
4. Trade Flows in AI-Driven Productivity Gains Scenarios \_\_\_\_ 12
5. Selected Macro Indicators in AI-Driven Productivity Gains Scenarios \_\_\_\_ 14
6. Trade Flows in Carbon Pricing Policy Scenarios \_\_\_\_ 18
7. Selected Macro Indicators in Carbon Pricing Policy Scenarios \_\_\_\_ 18

## ANNEXES

I. The Economic Structure of the Model and the Key Substitution Elasticities 21
II. Sectoral Mapping 24
III. Sectoral Results 26
IV. Labor Movement 28
References 29

# ESTIMATING THE IMPACTS OF AI, TRADE POLICY, AND THE ENERGY TRANSITION: AN APPLICATION TO IRELAND $^{1}$

Developments in trade policy, AI, and the energy transition are shaping small open economies. This paper uses a static, multi-region, multi-sector computable general equilibrium model to assess the impacts of these forces on Ireland in the long run through three channels: (i) current tariffs and trade agreements, (ii) AI-driven productivity gains, and (iii) carbon pricing, abstracting from short-run dynamics and frictions. The findings suggest that (i) the current trade policy shocks primarily redirect trade across partners and sectors, with modest aggregate output and export effects; (ii) AI-driven productivity gains can generate strong output and export growth, particularly in knowledge-intensive sectors, while inducing significant sectoral labor reallocation and distributional implications across factors of production which needs to be managed; (iii) carbon pricing can play a key role in addressing rising energy demand from AI and offsetting emissions, by shifting production toward lower-emission activities and increasing the renewable share in electricity generation.

## A. Introduction

1. Artificial intelligence, trade policy shifts, and the energy transition are simultaneously reshaping the outlook for small open economies. For Ireland, these structural forces are particularly salient given the economy's openness, deep integration into global value chains, and specialization in high-value tradable sectors. Changes in tariff regimes and the emergence of new trade agreements can alter relative market access and reconfigure export patterns, while AI-driven productivity gains offer scope to strengthen competitiveness through the supply side. At the same time, productivity-led expansion raises energy demand and emissions, intensifying policy trade-offs around climate objectives and the electricity mix. Understanding how trade policy, technological change, and climate policy interact is therefore central to assessing their implications for Ireland's product and labor markets, growth prospects, and progress toward decarbonization.

2. To assess these interactions quantitatively, this paper brings trade policy, AI-driven productivity gains, and climate policies together within a single, integrated analytical framework. Using a multi-region, multi-sector computable general equilibrium model calibrated to a 2025 baseline, the analysis embeds granular tariff data and sector- and region-specific AI productivity shocks, allowing policy changes and technological advances to interact consistently through relative prices, production structures, bilateral trade flows, and factor markets. The framework highlights the distinct and interrelated channels through which trade policy re-routes activity across markets, AI amplifies growth and competitiveness through the supply side, and

carbon pricing reshapes sectoral composition and energy use. By comparing standalone and combined scenarios, the paper clarifies whether trade adjustment operates primarily through prices or quantities, how AI-driven productivity reshapes Ireland's economic structure, and the extent to which climate policy may temper productivity-led expansion—ultimately shedding light on how policy choices affect Ireland's ability to reconcile strong growth with decarbonization objectives.

## B. Model Framework and Scenario Design

3. The paper aims to quantify Ireland's adjustment to trade shocks, AI-related productivity changes, and climate policy using a multi-region, multi-sector computable general equilibrium (CGE) model. The analysis is implemented in CGE-MOD (Khabbazan and Von Hirschhausen, 2021), a static general equilibrium framework designed to capture economy-wide spillovers through relative prices, trade flows, sectoral reallocation, and factor markets. The model features nested constant elasticity of substitution (CES) technologies and a standard Armington trade structure: inputs are differentiated by origin, while domestic output is allocated between domestic and export markets via constant elasticity of transformation (CET) functions, so trade shocks operate through wedges between import and domestic prices that induce substitution, trade diversion, and resource reallocation across sectors. Labor and capital are mobile across sectors within each region, while an immobile natural-resource factor anchors fossil-fuel supply, allowing for region-specific supply responses and the emergence of natural-resource rents. Annex I presents the economic structure of the model and the key substitution elasticities, calibrated using standard values from the literature. All factor incomes—labor, capital, and natural resources—as well as tax revenues accrue to the representative household in the model, so changes in household income reflect their combined evolution.

## 4. The framework features an explicit treatment of energy, allowing emissions to

respond through both activity and composition channels. Electricity generation is disaggregated by technology, including renewables, nuclear, fossil-fuel-based generation, and other sources, so that changes in relative costs induce substitution across power technologies, while $CO_{2}$ emissions are linked to fuel use through fixed emissions coefficients. The model also allows for carbon pricing and emissions trading systems, ensuring that policy-driven changes in carbon costs are transmitted consistently through production decisions, energy use, and emissions outcomes. This structure is essential for interpreting scenarios in which shifts in the electricity generation mix either reinforce or offset changes driven by aggregate economic activity.

5. The model is benchmarked to the Global Trade Analysis Project (GTAP) database and calibrated to a 2025 baseline. Specifically, the GTAP 11 Power dataset is used as the benchmark, providing internally consistent data on production, consumption, bilateral trade, energy use, and CO $_{2}$ emissions. To align the analysis with Ireland's policy questions, the global economy is aggregated into eight regions—Ireland, the rest of the European Union, the United States, the United Kingdom, China, India, Mercosur, and the rest of the world—and 44 economic sectors (see Annex II for the sector mapping). Baseline calibration draws on historical data and projections for GDP and CO $_{2}$ emissions over 2017–25, using IMF projections (IMF, 2024) to anchor regional macroeconomic paths. Regional factor endowments—labor, capital, and natural resources—are

scaled using a common adjustment factor to match projected aggregates, and where relevant, sector-specific production features and either market-based carbon pricing or taxes on $CO_{2}$ -emitting intermediate inputs are incorporated to ensure consistency with emissions projections and the energy mix. For Ireland, an initial economy-wide carbon price of around USD 72.3 per ton of $CO_{2}$ is incorporated in the baseline, reflecting both EU Emissions Trading System pricing and domestic carbon taxation. $^{2}$ Policy simulations are conducted as comparative statics relative to this baseline, and results should therefore be interpreted as medium-to-long-run reallocations rather than short-run dynamics. The 2025 baseline abstracts from the U.S. tariff increases, which are introduced only in the counterfactual tariff scenarios.

## 6. Several counterfactual scenarios are of main interest in the case of Ireland and are organized into three groups. These are:

• Tariff and Trade Agreements scenarios include the end-2025 tariffs imposed by the United States

and counterfactual trade agreements between the EU and Mercosur and between the EU and India, as well as a combination of these policy changes. Tariff inputs are drawn from the WTO Tariff & Trade Data (TTD) platform, using the WTO–IMF Tariff Tracker that records changes in effectively applied duties at the tariff line level and provides standardized aggregations to HS 6 and GTAP product categories with implementation dates. Trade agreements are modeled as reductions in

![](images/c2ea553e38d5a01551a3e2d396a264b9f34895c2cf9d5fe65eed6ec589cc5979.jpg)

bilateral goods tariffs to zero for the relevant partners; non-tariff barriers are not included, so the scenarios isolate the general equilibrium effects of tariff changes operating through relative prices, trade diversion, and sectoral reallocation (see Table 1).

\- AI-driven Productivity Gains scenarios implement sector- and region-specific productivity improvements that raise efficiency while reshaping sectoral factor demand and the composition of income. The calibration of productivity shocks follows published evidence on AI exposure and adoption, drawing on Cerutti et al. (2025) and OECD (2025), and is implemented under low, medium, and high variants to reflect uncertainty about the pace and breadth of diffusion. These scenarios are designed to map differences in AI intensity across sectors and countries into macroeconomic outcomes through general equilibrium adjustments in production, trade, and factor allocation (see Table 1). AI-driven productivity gains are assumed to occur across all regions, with heterogeneous sector- and country-specific magnitudes, implying that Ireland's results reflect relative rather than unilateral productivity gains.

\- Carbon Pricing Policy scenarios allow the carbon price instrument to adjust where relevant, either to offset the emissions implications of AI productivity shocks (keeping emissions at their baseline level) or to achieve a 20 percent reduction in emissions relative to baseline in the absence of AI. The policy is represented through an additional carbon price over the calibrated baseline, generating associated carbon revenues and inducing reallocation across energy sources and sectors, including through changes in the electricity mix (see Table 1). The simulations impose economy-wide carbon pricing across all sectors, while current policy coverage in Ireland remains incomplete.

7. Interpretation of the results should take into account the scope and simplifying assumptions of the modeling framework. The analysis is conducted in a static general-equilibrium setting and should therefore be interpreted as comparing alternative equilibrium outcomes in the medium to long term, rather than tracing short-run dynamics or transition paths. In this framework, AI adoption is modeled as an exogenous, sector- and region-specific productivity improvement, abstracting from the endogenous accumulation of AI capital, skills, and innovation capacity, as well as from potential labor displacement or unemployment effects. The framework abstracts from AI-specific energy use (for example, data-center demand), capturing only the indirect effects of AI through higher aggregate activity. The analysis also abstracts from uncertainty around key drivers, including future trade policy developments, the scale and diffusion of AI productivity gains, climate impacts, and climate policy responses, which could affect the results. Climate policy is represented through carbon pricing as a stylized instrument to internalize emissions costs, with both carbon pricing revenues and other tax revenues rebated lump-sum to households. Accordingly, the analysis does not incorporate the full range of Ireland's climate policy framework, including the targets and renewable energy policies set out in the Government's Climate Action Plan 2025 (Department of Climate, Energy and the Environment, 2025), for example, policies supporting onshore and offshore wind, solar, and related energy measures. Alternative policy instruments, such as regulations or subsidies, are not explicitly modeled. While these simplifying assumptions limit the analysis of adjustment dynamics and distributional frictions, they allow for a transparent characterization of the economy-wide reallocation, price, and trade channels through which trade policy, AI-driven productivity gains, and climate policies jointly shape Ireland's equilibrium outcomes.

<table><tr><td colspan="3">Table 1. Ireland: Scenario Description</td></tr><tr><td>Group</td><td>Scenario</td><td>Scenario Description</td></tr><tr><td rowspan="4">Tariff and Trade Agreements</td><td>USTar</td><td>End-2025 U.S. tariffs on trading partners, differentiated by region and sector.</td></tr><tr><td>EUMSC</td><td>EU and Ireland eliminate bilateral tariffs with Mercosur.</td></tr><tr><td>EUIND</td><td>EU and Ireland eliminate bilateral tariffs with India.</td></tr><tr><td>UST+FT</td><td>U.S. tariffs combined with EU trade agreements with Mercosur and India.</td></tr><tr><td rowspan="3">AI-driven Productivity Gains</td><td>AI-L</td><td>Low AI-driven productivity gains across all regions and sectors.</td></tr><tr><td>AI-M</td><td>Medium AI-driven productivity gains across all regions and sectors.</td></tr><tr><td>AI-H</td><td>High AI-driven productivity gains across all regions and sectors.</td></tr><tr><td rowspan="4">Carbon Pricing Policy</td><td>AIL-CP</td><td>Low AI productivity gains with carbon pricing to keep Ireland&#x27;s emissions at baseline.</td></tr><tr><td>AIM-CP</td><td>Medium AI productivity gains with carbon pricing to keep Ireland&#x27;s emissions at base</td></tr><tr><td>AIH-CP</td><td>High AI productivity gains with carbon pricing to keep Ireland&#x27;s emissions at baseline.</td></tr><tr><td>CARB20</td><td>Carbon pricing in Ireland to reduce emissions by 20 percent relative to baseline.</td></tr

[中间内容因长度限制已省略]

47</td><td>-10.56</td><td>-2.26</td><td>-6.56</td><td>-9.29</td><td>2.09</td></tr><tr><td>OMF</td><td>-15.56</td><td>0.01</td><td>0.80</td><td>-14.53</td><td>-2.47</td><td>-6.75</td><td>-9.83</td><td>-2.01</td><td>-5.55</td><td>-8.14</td><td>2.68</td></tr><tr><td>ATP</td><td>0.38</td><td>-0.02</td><td>0.12</td><td>0.48</td><td>1.12</td><td>2.98</td><td>4.16</td><td>-2.73</td><td>-7.29</td><td>-10.50</td><td>-20.74</td></tr><tr><td>WTP</td><td>-1.42</td><td>0.11</td><td>0.08</td><td>-1.23</td><td>1.27</td><td>3.52</td><td>4.75</td><td>-0.31</td><td>-0.85</td><td>-1.64</td><td>-9.00</td></tr><tr><td>OTP</td><td>0.29</td><td>0.02</td><td>0.03</td><td>0.33</td><td>2.91</td><td>7.76</td><td>11.37</td><td>2.79</td><td>7.41</td><td>10.85</td><td>-0.70</td></tr><tr><td>AFS</td><td>2.06</td><td>-0.01</td><td>-0.06</td><td>1.99</td><td>3.75</td><td>10.18</td><td>14.64</td><td>3.79</td><td>10.31</td><td>14.83</td><td>0.12</td></tr><tr><td>WHS</td><td>0.15</td><td>0.01</td><td>0.04</td><td>0.20</td><td>2.89</td><td>7.85</td><td>11.30</td><td>2.27</td><td>6.18</td><td>8.89</td><td>-3.40</td></tr><tr><td>CNS</td><td>0.33</td><td>0.00</td><td>-0.01</td><td>0.31</td><td>-1.23</td><td>-3.54</td><td>-5.06</td><td>-1.19</td><td>-3.43</td><td>-4.90</td><td>0.23</td></tr><tr><td>OSG</td><td>0.43</td><td>0.00</td><td>-0.01</td><td>0.41</td><td>-1.47</td><td>-3.70</td><td>-5.29</td><td>-1.45</td><td>-3.65</td><td>-5.22</td><td>0.10</td></tr><tr><td>EDU</td><td>0.37</td><td>0.01</td><td>0.00</td><td>0.38</td><td>-0.08</td><td>0.07</td><td>0.20</td><td>-0.08</td><td>0.07</td><td>0.20</td><td>-0.03</td></tr><tr><td>HHT</td><td>0.50</td><td>0.01</td><td>0.00</td><td>0.50</td><td>-0.84</td><td>-1.87</td><td>-2.61</td><td>-0.84</td><td>-1.86</td><td>-2.60</td><td>0.00</td></tr><tr><td>WTR</td><td>0.18</td><td>0.01</td><td>0.02</td><td>0.20</td><td>1.17</td><td>3.34</td><td>4.90</td><td>1.12</td><td>3.20</td><td>4.69</td><td>-0.31</td></tr><tr><td>TRD</td><td>-0.28</td><td>0.01</td><td>0.01</td><td>-0.26</td><td>2.02</td><td>5.52</td><td>7.84</td><td>2.04</td><td>5.56</td><td>7.89</td><td>0.04</td></tr><tr><td>CMN</td><td>-0.61</td><td>0.02</td><td>-0.05</td><td>-0.63</td><td>-0.27</td><td>-1.39</td><td>-2.08</td><td>-0.19</td><td>-1.17</td><td>-1.79</td><td>0.44</td></tr><tr><td>FIN</td><td>1.43</td><td>-0.05</td><td>-0.08</td><td>1.30</td><td>0.60</td><td>1.42</td><td>1.83</td><td>0.77</td><td>1.89</td><td>2.51</td><td>0.95</td></tr><tr><td>REA</td><td>-0.43</td><td>0.01</td><td>0.02</td><td>-0.40</td><td>2.55</td><td>6.18</td><td>8.60</td><td>2.54</td><td>6.16</td><td>8.56</td><td>-0.09</td></tr><tr><td>OBS</td><td>1.89</td><td>-0.07</td><td>-0.09</td><td>1.73</td><td>-1.28</td><td>-3.57</td><td>-5.17</td><td>-1.20</td><td>-3.36</td><td>-4.88</td><td>0.44</td></tr><tr><td>ROS</td><td>0.54</td><td>0.02</td><td>0.03</td><td>0.59</td><td>2.75</td><td>7.57</td><td>10.85</td><td>2.51</td><td>6.93</td><td>9.92</td><td>-1.34</td></tr></table>

## References

Aguiar, A., M. Chepeliev, E. Corong, and D. van der Mensbrugghe. 2023. The Global Trade Analysis Project (GTAP) Data Base: Version 11. Journal of Global Economic Analysis 7 (2).

Beckman, J., T. Hertel, and W. Tyner. 2011. Validating Energy-Oriented CGE Models. Energy Economics 33 (5): 799–807.

Böhringer, C., and T. Rutherford. 2010. The Costs of Compliance: A CGE Assessment of Canada's Policy Options under the Kyoto Protocol. World Economy 33 (2): 177–211.

Cerutti, E., A. Garcia Pascual, Y. Kido, L. Li, G. Melina, M. M. Tavares, and P. Wingender. 2025. The Global Impact of AI: Mind the Gap. IMF Working Paper No. 25/76, International Monetary Fund, Washington, DC.

Chepeliev, M. 2023. GTAP-Power Data Base: Version 11. Journal of Global Economic Analysis 8 (2): 100–133. Center for Global Trade Analysis, Purdue University.

Department of Climate, Energy and the Environment. 2025. "Climate Action Plan 2025." Government of Ireland. Available at: https://www.gov.ie/en/department-of-the-taoiseach/publications/climate-action-plan-progress-reports/#climate-action-plan-2025

Doorley, K., O'Connor, S., O'Shea, R., and Tuda, D. 2026. Artificial Intelligence and Income Inequality in Ireland. Jointly Published Report No. 16. Dublin: Economic and Social Research Institute (ESRI). https://doi.org/10.26504/jr16

International Monetary Fund (IMF). 2024. World Economic Outlook: Steady but Slow—Resilience amid Divergence. Washington, DC, April.

Khabbazan, M. M., and C. von Hirschhausen. 2021. The Implication of the Paris Targets for the Middle East through Different Cooperation Options. Energy Economics 104: 105629.

Khabbazan, M. M. 2022. "The EU's Gain (Loss) from More Emission Trading Flexibility—A CGE Analysis with Parallel Emission Trading Systems." Journal of Open Innovation: Technology, Market, and Complexity 8 (2): 91. https://doi.org/10.3390/joitmc8020091

Khabbazan, M. M., and M. Garcia-Escribano. Forthcoming. A CGE-Based Macroeconomic Assessment of Energy Diversification in Morocco. IMF Working Paper, International Monetary Fund, Washington, DC.

Lanz, B., and T. Rutherford. 2016. GTAP In GAMS: Multiregional and Small Open Economy Models. Journal of Global Economic Analysis 1 (2): 1–77.

Okagawa, A., and K. Ban. 2008. Estimation of Substitution Elasticities for CGE Models. Discussion Paper 08-16, Research Institute of Economy, Trade and Industry (RIETI), Tokyo.

Organisation for Economic Co-operation and Development (OECD). 2025. Macroeconomic Productivity Gains from Artificial Intelligence in G7 Economies. OECD Artificial Intelligence Papers No. 41, Paris.

World Trade Organization (WTO) and International Monetary Fund (IMF). 2026. WTO–IMF Tariff Tracker. WTO Tariff & Trade Data Platform, Geneva.
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
