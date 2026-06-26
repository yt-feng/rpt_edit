你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Climate Shocks, Debt Defaults and Investment in Climate Adaptation – Squaring an Impossible Trilemma

Constance de Soyres, Emmanuella Obeng, and Joanne Tan
WP/26/128

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/06e427f7bc727ea2901e2170a27ae16147a1dfdd072e8c308fef5ac1a34b6495.jpg)

# IMF Working Paper African Department

# Climate Shocks, Debt Defaults and Investment in Climate Adaptation – Squaring an Impossible Trilemma Prepared by Constance de Soyres, Emmanuella Obeng and Joanne Tan

Authorized for distribution by Pablo Lopez
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Climate disasters tend to be associated with increased sovereign default risk. Countries face an “impossible trilemma”: scale up adaptation investment, keep debt sustainable amidst high borrowing costs and avoid the higher risk of default from delayed adaptation. Using a global panel of disaster event-level shocks, we find that a 1pp increase in disaster related losses as a share of GDP raises the odds of sovereign default by approximately 2-3 percent. An additional US\$1 billion in cumulative Official Development Assistance (ODA) is associated with a 0.13 point gain in a country’s adaptive capacity. Using average marginal effects and our predicted margins we then map concessional ODA finance to default probability and translate these relationships into a practical budgeting yardstick for calibrating needed ODA to sovereign default risk reduction targets. In a context of declining ODA, our findings highlight the crucial role of well-designed support in climate adaptation policies.

JEL Classification Numbers:

Q54; H63; O19; C23

Keywords:

Climate shocks; sovereign defaults; climate adaptation; concessional finance

Author's E-Mail Address:

cdesoyres@imf.org; eobeng@colorado.edu; jtan@imf.org

## Contents

Abstract....2   
Introduction....4   
Literature Review....5   
Data....6   
Stylized Facts....8   
Empirical Strategy and Results....11   
Conclusion....17   
References....18   
Appendix....20

## 1. Introduction

Climate disasters are increasing in both frequency and severity. The impact of these climate shocks on sovereign debt defaults remains an important research topic. Volz et al. (2020) map the transmission channels from what they term physical and transition risks to sovereign risk through: (i) macroeconomic impacts, (ii) fiscal impacts of disasters and fiscal pressures from adaptation and mitigation policies, (iii) climate related risks and financial sector stability, (iv) depletion of natural capital, and (v) impacts of climate change on trade and political stability. Because debt typically rises after disasters via financing recovery and reconstruction costs (Mejia, 2014), any combination of these channels can amplify sovereign risk and push climate vulnerable countries toward default. In fact, recent analysis revealed that climate shocks would further hurt long-term debt sustainability unless countries invest in adaptation (Calcaterra et al., 2025b) to reduce future damages. However, adaptation is costly and generally involves high upfront costs. If adaptation is financed by debt at market terms, it could increase debt ratios today and accentuate debt vulnerabilities. On the contrary, delaying investments in adaptation could preserve debt ratios today but at the cost of increased vulnerabilities to these shocks in the future. Hence, an “impossible trilemma” is faced by countries that cannot strengthen their resilience to climate shocks without an impact on debt sustainability.

Recent disaster episodes show how large the associated economic and fiscal losses can be. In the wake of Hurricane Ivan, which struck Grenada in 2004, total losses were estimated at about US\$1.1 billion representing 200 percent of GDP. As a result, debt levels spiraled from 80 percent of GDP in 2003 to 95 percent of GDP in 2004, and the country undertook a debt restructuring over 2004-2006. More recently, Hurricane Beryl (2024) was estimated to have cost about a third of Grenada's GDP. $^{1}$ In Dominica, Hurricane Maria (2017) caused about US\$931 million in damages and US\$380 million in losses, which represented about 226 percent of 2016 GDP, leading to significant negative effects on the performance of their economy, a surge in debt and a projected 21 percent external current account deficit for 2018. $^{2}$ In 2019, Cyclones Idai and Kenneth devastated Mozambique, Malawi and Zimbabwe with losses amounting to over \$873 million in buildings, equipment, infrastructure and crops. $^{3}$ The World Bank mounted a \$191.7 million emergency recovery and resilience operation in an attempt to cut fiscal losses from these cyclones. $^{4}$ The impact of climate-related events is not limited to the developing world. They caused an estimated €208 billion in economic losses across Europe between 1980 and 2024, with over one quarter of the cost incurred between 2021 and 2024. $^{5}$ There have been more than 400 climate-related events in the U.S. since 1980, with total damages exceeding US\$2.9 trillion. $^{6}$ These episodes reveal how climate shocks can strain sovereign balance sheets in advanced and developing economies alike, with significant fiscal consequences: damaging physical assets and infrastructure and requiring substantial expenditures on relief programs and reconstruction costs. The Global Commission on the Economy and Climate (2016) estimated that roughly US\$90 trillion in sustainable climate resilient infrastructure will be needed by 2030, underscoring the sizeable fiscal challenge. $^{7}$

Climate disasters tend to depress output growth and cause losses that countries do not fully recover from (Felbermayr & Gröschl, 2014; Strobl, 2011; Hsiang & Jina, 2014) and raise consumer price inflation with persistent effects on food prices (Parker, 2017). They also widen fiscal gaps through recovery and reconstruction costs (Mejia, 2014), affect firm-level productivity and the cost of debt (Cevik & Miryugin, 2023; Kling et al., 2021) and cause sovereign distress (Agarwala et al., 2021; Beirne et al., 2021; Cevik & Jalles, 2022a; Kling et al., 2018; Klusak et al., 2023; Seghini, 2024a) which may lead to debt defaults. Against this backdrop, we examine whether investing in climate adaptation using concessional financing can help build resilience, reduce disaster-induced damages and lower default probability without imperiling debt sustainability.

To address this question, the paper proceeds in three steps. First, we revisit the relationship between climate shocks and sovereign debt defaults by estimating the impact of shocks on default probabilities with a methodology adapted for rare events. Using a cross-country database of climate shocks merged with default episodes (Asonuma & Trebesch, 2016), we find that climate shocks have a positive statistically and economically significant impact on default probability, robust across different estimations, income groups and to the use of an alternative default dataset from the Bank of Canada/Bank of England which allows splits by creditor type. $^{8}$ Second, we assess whether a country's adaptive capacity (the ability to absorb and recover from climate shocks) mitigates the economic damages from climate disasters. Holding other factors constant, higher adaptive capacity is associated with a reduced marginal economic impact of additional disasters. Finally, we examine whether access to concessional financing contributes to building adaptive capacity by estimating panel regressions of adaptive capacity on Official Development Assistance (ODA) disbursements. We find that ODA (in both nominal US\$ terms and in percent of GDP) tends to be positively associated with improvements in adaptive capacity. We then map the estimated coefficients to implied changes in damages and default probabilities using a partial equilibrium, back-of-the-envelope calculation. We find that ODA is associated with stronger adaptive capacity, which in turn tends to attenuate damages and lower default probability. Given that ODA disbursements are likely endogenous, despite the inclusion of controls, our results should be interpreted as associations, rather than causal effects.

Our contributions are threefold: First, we replace broad structural vulnerability measures used in past empirical work with climate event-level macroeconomic loss measures tying the climate-default link to realized shocks. Second, we address rare event bias in sovereign default estimations by using a methodology tailored to such events. Third, we extend the empirical contribution by pricing the policy lever. We translate the estimated coefficients into budget relevant US dollar magnitudes and ODA to GDP ratios required to offset the climate disaster-induced increases in default probability. This allows us to evaluate how access to concessional financing can strengthen adaptive capacity and attenuate the effect of climate shocks on sovereign default probabilities. The remainder of the paper is structured as follows: we give an overview of the literature in Section 2, discuss our data and methodology in Section 3, and some stylized facts in Section 4. Section 5 presents the empirical strategy and results. Section 6 concludes.

## 2. Literature Review

This paper is related to the following strands of literature. First, our paper is related to the growing literature that documents how climate vulnerability is priced into sovereign risk premia via bond spreads and ratings. Using the ND-GAIN vulnerability indices, Beirne et al. (2021), Cevik & Jalles (2022a, 2022b, 2023), and Kling et al. (2018) show that climate risk is a first-order driver of sovereign credit conditions, with more exposed sovereigns facing higher borrowing costs. For developing countries, Cevik & Jalles (2022b) quantify an effect of about 15.55 basis points on spreads, while Kling et al. (2018) estimate that for the V20 group, the sovereign debt cost is about 1.174 percent higher, translating to over US\$62 billion in the past decade. $^{9}$ Klusak et al. (2023) project systematic climate induced downgrades to sovereign credit ratings under warming scenarios as early as 2030. Using monthly Emerging Market Economies (EME) data, Boehm (2022) finds that rising temperatures undermines sovereign credit. A $1^{\circ}\mathrm{C}$ anomaly lowers EMBI returns by about 0.46 percentage points on average, implying higher borrowing costs. We build on this strand by shifting the outcome from spreads/ratings to the default event itself, employing a robust methodology and exploiting realized economic damages (in percent of GDP) as the climate shock.

A second strand of the literature studies sovereign debt sustainability in the context of climate shocks and how adaptation can reshape debt dynamics. Cheng & Chang (2025) highlight that disaster shocks raise sovereign risk through higher external debt service or government expenditure; Agarwala et al. (2021) emphasize that disasters destroy assets and public infrastructure which require significant expenditure on repair and reconstruction; Seghini (2024b) shows that climate-related costs can tip highly indebted countries into unsustainable territory. Stress testing and debt sustainability frameworks indicate that higher disaster frequency strain public finances. For a global sample of countries, Calcaterra et al. (2025b) find that expected debt servicing costs increase by up to 3 percent of GDP under high climate impact scenarios, with considerable country heterogeneity and that long-run debt trajectories of highly impacted countries become unsustainable. They also show that appropriately calibrated adaptation can lower these debt pressures and the implied risk premia. However, if financed on non-concessional terms, it can tighten the primary balance and push up the debt stabilizing fiscal adjustment. $^{10}$ To extend the analysis, this paper focuses on adaptation investment financed on concessional terms using ODA as a share of GDP. Model-based papers formalize the mechanism. Mallucci (2022) embeds adaptation capital into a sovereign default environment for seven Caribbean countries and finds that countries exposed to climate shocks may need contractual innovations like disaster clauses and concessional finance to continually access financial markets as risks increase. A complementary literature (Duffy, 2025) augments a standard sovereign default framework for emerging economies with endogenous public adaptation capital that accumulates over time and reduces disaster damages, showing that higher disaster frequency raises default risks and spreads while adaptation lowers both. They highlight that default risk tightens the fiscal space and budget, and this may in turn increase the costs of climate change by limiting investments in adaptation. They argue that debt relief type instruments like low-cost loans and adaptation linked bonds could expand the fiscal space, raise adaptation and lower disaster induced losses. In these frameworks, adaptation is not merely a resilience policy but a tool that can be used to reduce future damages that tighten sovereign balance sheets and constrain nations. This paper shows empirically, in a broad cross-country panel, that adaptation can dampen disaster damages.

Finally, our paper complements papers and policy reports that highlight the importance of concessional financing to raise adaptation at the scale necessary for sovereigns subject to climate shocks and debt vulnerabilities. Inger Anderson (United Nations Environment Programme, UNEP) underscores that scaling climate finance must begin with investing in adaptation and prioritizing grants, concessional and non-debt creating instruments to avoid adding to vulnerable countries' debt burden. $^{11}$ Complementing this, the UNEP Adaptation Gap Report (2025) cautions that although about 70 percent of international public adaptation in 2022–2023 was concessional, nonconcessional debt instruments still dominated flows, raising affordability and equity concerns and risking an adaptation investment trap that could deepen vulnerabilities. $^{12}$ Bhattacharya et al., (2023) argue that concessional finance, while scarce, is the most vital resource for a climate resilient society, calling for a fivefold increase by 2030. Echoing this, the IMF's 2023 Climate Staff Note quantifies the 2030 concessional adaptation finance needs at about US\$30 billion for Low-Income Countries (LICs) and US\$10 billion for Small Developing States (SDS) with total grant requirements for mitigation and adaptation at around US\$42 billion per year. $^{13}$ We contribute to this strand of literature by translating our empirical results into a policy relevant implication for ODA, by linking cumulative ODA and ODA as a share of GDP to improvements in adaptive capacity, reductions in disaster damages and implied declines in debt default probability of vulnerable countries.

## 3. Data and methodology

This paper uses a variety of data sources. To implement our research strategy, we create a sovereign default variable using the comprehensive default database by Asonuma and Trebesch (2016). We define sovereign default as a failure to meet debt service obligations and a non-honoring of original debt agreements. This includes missed coupon payments and event-type restructurings with either no legal default or no unilateral default episode. While the database is at a monthly frequency, we convert default episodes to an annual basis and mark a country “in default” throughout the duration of the default spell. The default variable is equal to one when the country is considered in default, and zero otherwise. In total, there are 196 default events. A complementary default measure was constructed using the sovereign default database from the Bank of Canada/Bank of England. This dataset provides estimates of the nominal value of government debt in default by type and creditor and includes foreign and local currency denominated bank loans, bonds and debt by multilateral organizations, Paris Club and other private creditors. For each country, in a given year, the country is considered in default when the stock of arrears increases by more than 100 percent compared to the previous year, provided the previous year’s stock of arrears is positive. The default variable is set at one in those years, and zero otherwise. As robustness, we also split the default dataset by creditor (official – IMF, IBRD, IDA, Paris Club, China, other official; private – foreign currency (FX) banks, FX bonds, other private; domestic – local currency (LC) debt, domestic arrears). $^{14}$

Disaster events-level data are obtained from the Emergency Events Database (EM-DAT). EM-DAT contains data compiled from different sources on the occurrence of natural disasters, including meteorological, hydrological, climatological, geophysical and biological events across the world since 1900. A record enters the EM-DAT database if it has at least one of the following: 10 fatalities, 100 affected people, a state of emergency declared or a call for international assistance. The disasters of interest for this analysis are meteorological and hydrological disaster events: drought, extreme temperature, flood, landslide and storms. Multi-year disasters, such as droughts, enter the panel according to the year in which EM-DAT records the event and its associated damages. Our variable of interest is the economic impact variable, “Total Economic Damage”, which we aggregate across all events in a given country and year and scale by nominal GDP. $^{15, 16}$ This naturally scales the shock by the size of the economy and captures the intensity of the impact. This method also aggregates the different disasters into one severity metric per year. $^{17}$ Disaster counts ranges from 0 to 34 events per country-year. About 44 percent of country-year observations record no disasters while only a small share record more than 19 in a year. The EM-DAT database also reports data on human impact metrics (total deaths, number injured, total number of people affected) and other economic impact variables (reconstruction cos

[中间内容因长度限制已省略]

ar panel.

For the purposes of robustness, we consider the BoC/BoE sovereign debt database. Below is default probability by creditor type. Bars show the effect of our climate shock (damages, % of GDP) on the default indicator constructed from the BoC/BoE database. The estimates are from creditor specific rare events logit specification. Controls included but not shown; country income-group and year fixed effects included.

![](images/9893c8309826145fdac7c28a1c1c205ee077b75df939a2a1f0d20e5c64dece09.jpg)  
Figure A.1. Default probability split by creditor type, full sample. Notes: The figure plots predicted default probabilities separately by creditor type for the full sample. Sources: BoC/BoE sovereign default database, compiled by Authors.

As a diagnostic control, we controlled for IMF program episodes that coincided with country debt restructuring episodes. The results showed that disaster shocks continue to predict higher default probability. Disaster losses remain positively associated with next year's default, even after conditioning on IMF program status in the previous year. The IMF program dummy is included to account for programs that occur in periods of acute stress, sometimes overlapping with restructurings. We interpret this as a diagnostic control and not a causal control.

Table A.2. Rare events logit specification with a Diagnostic Control

<table><tr><td>Default dummy</td><td>(1) ALL</td><td>(2) EME</td><td>(3) LIDC</td></tr><tr><td>damage (% GDP)</td><td>0.029**(0.011)</td><td>0.023*(0.012)</td><td>0.091(0.128)</td></tr><tr><td>IMF program dummy</td><td>1.201***(0.268)</td><td>1.041***(0.384)</td><td>1.198***(0.438)</td></tr><tr><td>Observations</td><td>3031</td><td>1469</td><td>939</td></tr><tr><td>Income Group FE</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Year FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Table A.2 reports rare events logit estimates from Equation (1) including an indicator for IMF-supported programs.  
Standard errors in parentheses. Controls included but not shown. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01.

To address heterogeneity across disasters that differ in type and intensity, we construct an exogenous precision-weighted climate shock index à la Felbermayr & Gröschl (2014) by combining hazard-specific measures and indicators on droughts, extreme temperature events, floods, landslides and storms. $^{1}$ Following their methodology, each hazard component is defined as the deviation of an annual climate variable from its long run mean and the anomalies are aggregated using inverse-variance weights to prevent dominance by any single hazard. The components are drawn from established climatological sources. Drought intensity is measured using data from the Standardized Precipitation Evapotranspiration Index (SPEI-12). These are monthly gridded data at 0.5° spatial resolution, averaged over the year and sign-flipped for larger values to signify drier years. For extreme temperature/heat, we use the 2m temperature anomaly against the 1981-2010 climatology baseline from the European Center for Medium Range Weather Forecasts Reanalysis v5 (ERA5-Land). Flooding was constructed using the product of long-term floodable land share from the Joint Research Center of the European Commission 50 return period (JRC RP50 map) and precipitation anomaly vs. a 2000-2020 baseline (ERA5). Some places have a structural long-term feature and are naturally more flood prone because of topography and coastal exposure. This is captured by the JRC RP50 map. Because rainfall patterns are less stationary than extreme temperature, we anchored that to a modern satellite era to help capture the contemporary climate system better. We use the National Aeronautics and Space Administration (NASA) as the primary data source for landslide intensity. The International Best Track Archive for Climate Stewardship (IBTrACS v4) records data on individual hurricane events at 6-hour intervals. From this data source, we constructed the annual Accumulated Cyclone Energy (ACE) for storm intensity. Landslide and storm measures are normalized by land area (per 100km²) before applying precision weighting.

Below are results for the climate shock index by individual physical intensity measures (drought, heat, flood, landslide, storm) in a rare events logit specification. Only lagged storm intensity measure raises next-year default odds. Other hazards and the combined composite index created are not predictive for the full sample, EME or LIDCs. $^{2}$ In contrast, damage (% of GDP) is robustly predictive. We keep it as the baseline shock measure.

Table A.3. Default probability by individual disaster intensity measures

<table><tr><td></td><td>(1) drought</td><td>(2) heat</td><td>(3) flood</td><td>(4) landslide</td><td>(5) storm</td></tr><tr><td rowspan="2">default dummy</td><td>-0.296**</td><td>-0.337</td><td>0.009</td><td>-0.641**</td><td>0.306*</td></tr><tr><td>(0.131)</td><td>(0.275)</td><td>(0.180)</td><td>(0.276)</td><td>(0.157)</td></tr><tr><td>Observations</td><td>2638</td><td>1920</td><td>1862</td><td>2156</td><td>387</td></tr><tr><td>Country FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: Table A.3 reports estimates using separate disaster intensity measures for drought, heat, flood, landslide, and storm, in place of the aggregate damage variable. Standard errors in parentheses. Controls included but not reported. Country and Year FE included. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01

![](images/0c1ef74c429dc79e89aefd910f4cdf6a0f4265452b715ed45a78625cfd70534b.jpg)
"""
