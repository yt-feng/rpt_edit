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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa

Dennis Engist

Gabriel Englander

Alan Lee

Frederik Noack

POLICY RESEARCH WORKING PAPER 11430

## Abstract

Protected areas cover $17\%$ of the world's land surface, yet credible evidence on their long-run economic and ecological impacts remains scarce. This paper estimates the effects of South Africa's protected areas on household income, bird biodiversity, and tourism consumer surplus. For the income and biodiversity analyses, it develops a machine-learning counterfactual approach that recovers the present-day impacts of protected areas created up to 100 years ago. Short-run impacts of newer protected areas are small and statistically insignificant, while older protected areas generate large gains. Prior research may have severely underestimated the benefits of protected areas by only estimating the short-run effects of newly established protected areas. In aggregate, this paper estimates that protected areas increase annual household income by approximately R300 billion (roughly 10% of 2011 GDP). This yields approximately 7.6 million job-equivalents attributable to South Africa's protected areas. Different types of protected areas play complementary roles in conserving different categories of threatened birds, demonstrating the value of South Africa's entire protected area network. A structural travel cost model estimates that South Africa's national parks generate R7.7 billion per year (2023 rand) in recreational value for domestic and international tourists. These results suggest that in South Africa there is little tradeoff between wildlife conservation and economic development. Realizing the economic and ecological benefits of protected areas, however, requires patience: returns to conservation accumulate over decades, not years.

![](images/0c97b62bceb01e1685cc5420d4c5eb2c06aafff9e25474d9676d54e1c975b044.jpg)

# The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa\*

Dennis Engist $^{\dagger}$ Gabriel Englander $^{\ddagger}$ Alan Lee $^{\S}$ Frederik Noack $^{\P}$

Authorized for distribution by Florence Kondylis, Research Manager, Development Research Group, Development Economics, World Bank Group

JEL classi ication: Q56, Q57, Q26, O13, C21

Keywords: Protected areas, Household income, Biodiversity conservation, Tourism, South Africa

## 1 Introduction

Protected areas are the principal instrument for conserving biodiversity (Gurney et al., 2023; Watson et al., 2014). Collectively spanning more than $17\%$ of the world's land surface, they represent one of the largest deliberate allocations of land to a single policy objective, with potentially far-reaching consequences for the economies of surrounding communities (UNEP-WCMC and IUCN, 2024). Yet robust causal evidence on their economic and ecological consequences remains limited. Because protected areas are typically established in locations with high biodiversity or low economic opportunity costs, simple correlations between protection, biodiversity, and development outcomes are prone to selection bias and reverse causality. While protected areas such as national parks contribute to human well-being through recreational opportunities, tourism revenue, and biodiversity benefits, they may also impose substantial economic costs by restricting local land use and limiting resource extraction (Bahrami, Gustafson, and Steiner, 2025).

These concerns raise a central policy dilemma. Governments may optimally locate protected areas in regions where conservation is inexpensive, but where biodiversity benefits and economic spillovers are limited (Pfaff et al., 2015; Grupp et al., 2023). This challenge is particularly acute because many global biodiversity hotspots are concentrated in developing and emerging economies, where conservation competes directly with poverty reduction and economic development objectives (Myers et al., 2000). Understanding whether protected areas simultaneously promote biodiversity conservation and local economic welfare is therefore critical for global conservation policy.

We study these questions in South Africa, one of the world's most biologically diverse countries and a globally recognized biodiversity hotspot. South Africa hosts exceptional levels of plant, bird, and invertebrate diversity and supports iconic megafauna including elephants, lions, and rhinoceroses. The country maintains an extensive protected area network, covering approximately $11\%$ of its terrestrial land surface and consisting of national parks, provincial nature reserves, and a rapidly expanding system of private conservation areas (Figure 1). Despite well-developed management systems, many protected areas face pressures from poaching, land encroachment, and surrounding economic deprivation, potentially limiting conservation effectiveness.

South Africa simultaneously faces severe socio-economic challenges, including high unemployment and persistent inequality. Nature-based tourism represents a major economic sector, with protected areas serving as key attractions. Protected areas contribute to human well-being through tourism revenues accruing to local communities and substantial recreational consumer surplus enjoyed by domestic and international visitors. Biodiversity spillovers may further affect surrounding communities through ecosystem services and wildlife-related damages (Gulati et al., 2021; Noack, Engist, and Larsen, 2025). Conversely, conservation restrictions may constrain agricultural expansion and resource-based livelihoods in rural regions. Whether protected areas alleviate or exacerbate local economic challenges, therefore, remains an open empirical question.

Quantifying the causal impacts of protected areas is difficult because protection is not randomly assigned. Standard approaches in economics rely on two-way fixed effects (TWFE) designs that compare outcomes before and after protected area establishment relative to contemporaneous changes in outcomes in non-protected areas. However, many of the world's most important protected areas were established decades before modern socio-economic and biodiversity data became available. For example, Kruger National Park was formally established in 1926. Consequently, TWFE approaches primarily identify short-run impacts of newly-established protected areas and implicitly assume that conservation effects do not evolve over time and that older and newer protected areas are comparable.

![](images/5622c493f7b511b973d16f58cf15ae5d6cf03a94906ed300707b22821b879816.jpg)  
Figure 1: A map of South Africa with protected areas in green, national parks labelled in black, and major cities labelled in blue.

To overcome these limitations, we develop a complementary identification strategy grounded in the literature on economic geography and long-run development. We assemble a spatial dataset of pre-protection geographic variables that are known to shape long-run economic outcomes (Gollin, Parente, and Rogerson, 2002; Bleakley and Lin, 2012; Nunn and Puga, 2012; Dell, Jones, and Olken, 2012; Jedwab and Moradi, 2016; J Vernon Henderson et al., 2018; Donaldson, 2018), consisting of predictors of economic activity determined before the establishment of South Africa's first national park. These variables include historical railway networks, early twentieth-century economic agglomerations, climatic conditions, agricultural suitability, and terrain ruggedness.

Using machine-learning prediction algorithms trained exclusively on locations distant from protected areas, we estimate counterfactual household income based solely on pre-protection characteristics. This counterfactual prediction represents what income would have been in the absence of protected areas. Comparing predicted and observed incomes allows us to recover both short- and long-run economic impacts of protected areas. We apply the same framework to bird biodiversity outcomes while incorporating additional ecological predictors such as ecoregions.

We find that protected areas generate positive long-run economic and ecological effects. Old protected areas significantly increase local household income, while recently established protected areas exhibit small and statistically insignificant short-run impacts. National parks produce larger income gains than other types of protected areas. Simultaneously, protected areas preserve threatened bird species and shift bird communities toward species reliant on intact natural habitats. Finally, a key motivation for establishing protected areas, including national parks, is their contribution to human well-being through recreational value. Visitors derive enjoyment that is not fully captured by entrance fees but is at least partially reflected in their willingness to travel long distances to visit a protected area. These benefits may be substantial, as they are a direct and intended consequence of establishing protected areas. We use a structural travel-cost model to estimate that South Africa's national park system generates approximately R7.7 billion annually in tourism consumer surplus, with domestic visitors capturing roughly one-quarter of the total.

The concordance between our machine-learning counterfactual approach and conventional TWFE estimates is reassuring, but the larger effects estimated for long-established protected areas could still reflect spatial selection into conservation. That is, early planners may have preferentially protected locations with inherently higher economic or ecological potential. We test this selection concern directly using predicted counterfactual outcomes based solely on pre-protection characteristics. We find no evidence that older protected areas were placed in more favorable locations, which suggests that their larger impacts primarily reflect dynamic processes that unfold over decades.

A growing interdisciplinary literature evaluates the impacts of protected areas on development and conservation outcomes (Sims, 2010; Ferraro and Hanauer, 2014; Andam et al., 2010; Pfaff et al., 2015; Grupp et al., 2023; Geldmann et al., 2013; Gray et al., 2016; Denny, Englander, and Hunnicutt, 2024; Baylis, Garcia, and Heilmayr, 2026). Our paper contributes to this literature by jointly quantifying economic, biodiversity, and recreational welfare impacts within a unified causal framework—an integration that prior analyses have not attempted. More fundamentally, the existing literature predominantly relies on short-run variation in protection status. Our findings suggest that this risks substantially underestimating the long-run benefits of conservation.

Taken together, our results suggest that protected areas can simultaneously enhance biodiversity conservation and generate substantial economic benefits. These findings provide cautious optimism that biodiversity-rich emerging economies can leverage conservation investments to support both ecological sustainability and economic development.

## 2 Household Income

We estimate the impact of South African protected areas on household income using data from the South African census, which provides monthly household income for 4,277 electoral wards in 2001 and 2011 (Statistics South Africa, 2011a). South Africa did not release income data from its 2021 census or from censuses before 2001 at the ward level. This narrow temporal window of 2001 to 2011 illustrates the limits of TWFE models in this setting: they only allow estimation of short-term effects of the small number of protected areas established in this period. For this reason, we complement the TWFE panel estimation with a cross-sectional regression and a machine learning approach to capture the long-term effects of the full protected area network.

In all models and specifications, we use log-transformed total household income per ward as the outcome. We use total rather than per capita income to capture not only individual income gains, but also the aggregate economic effects of labor migration. Our treatment variables are the log-transformed area (in square meters) of protected areas within the ward and, separately, within a 15 km buffer surrounding the ward. We select 15 km as the buffer distance because the average ward area of $285 \, km^2$ corresponds roughly to a square with 15 km sides, so the buffer extends spillover detection to approximately one ward-length beyond each ward's boundary. This specification allows us to capture both the direct local impacts of protected areas and the spatial spillover effects on neighboring communities. In the cross-sectional and machine learning estimations, we further subset the treatment variable in three ways: all protected areas pooled together, national parks versus other types of protected areas, and protected areas separated into age groups by the year in which they were established. To correct for spatial autocorrelation and generated regressors, we calculate standard errors using spatial block bootstrapping across all models. Specifically, because our machine learning approach relies on predicted counterfactuals as inputs, standard analytical errors would ignore the sampling variation from this first-stage estimation and artificially deflate our confidence intervals. By resampling spatial blocks and re-estimating the entire procedure for each draw, the bootstrap accurately accounts for both local spatial dependence and the additional uncertainty introduced by the generated regressors.

In the TWFE model, the treatment exposure of electoral wards is restricted to the protected areas established from 2002 to 2011, with 2001 serving as the baseline. Year and ward fixed effects (i.e., binary variables for each year and each electoral ward) absorb annual income shocks common across all wards and all time-invariant differences between wards, respectively. The resulting estimates stem from comparing the change in income from 2001 to 2011 between electoral wards with different levels of expansion of protected areas. To avoid further limiting the sample, in the TWFE approach we only estimate the pooled specification, grouping all protected areas together.

To estimate the long-term effects of the full set of protected areas, we deploy two distinct strategies. First, we use the household income data as a repeated cross-sectional outcome in an Ordinary Least Squares (OLS) linear regression, controlling for an extensive set of covariates. These covariates are not determined by protected areas; they consist of environmental characteristics (e.g., temperature, elevation, ruggedness, distance to rivers) and historical infrastructure (e.g., distance to railways in 1925, distance to metropolitan centers in 1921 — see Figure B.1). By explicitly controlling for these determinants of income, we absorb differences in economic potential across wards. This approach relies on the assumption that, conditional on these controls, the placement of protected areas is quasi-random, so that the residual variation explained by the protected area treatment variables is the causal effect of protected areas on income. Importantly, this assumption does not require that the controls capture all determinants of household income—only that they are sufficient to render the placement of protected areas uncorrelated with unobserved determinants of income.

Second, we apply the same core logic using a more sophisticated machine learning approach. Rather than using the environmental and historical variables simply as linear controls, we train an XGBoost algorithm to predict household income based on these variables. Crucially, we train it only on untreated electoral wards: those that are located, on average, more than 15 km away from the nearest protected area and do not contain any protected areas (see Figure B.2 for a map of training wards). We then use the trained model to predict income for all wards, which yields a counterfactual income level in the absence of protected areas (see Tables C.1 and C.2 and Figure B.3 for XGBoost model parameters and out-of-fold performance of the income and nightlights predictions). We achieve out-of-fold $R^{2}$ -values of 0.34 for household income prediction, and 0.3 for nighttime lights. While traditional in-sample spatial regressions demonstrate that fundamental geographic characteristics can explain up to 35% of the within-country variation in economic activity (J Vernon Henderson et al., 2018), an out-of-fold $R^{2}$ of 0.34 is robust and aligns with the performance of established spatial machine learning applications predicting local economic well-being (Yeh et al., 2020). The difference between observed and predicted income is then regressed on our protected area treatment variables. As in the cross-sectional linear approach, we run separate estimations for all protected areas, protected areas by type, and protected areas by age group.

Across both the cross-sectional regression and machine learning approaches, we find positive and statistically significant effects of protected areas on household income (Figure 2, left panel titled “All”; see Table C.3, C.4, C.5, C.6, C.7, and C.8 for full income and nightlights regression output tables). An additional 1% of protected area within an electoral ward leads to an approximately 0.2% increase in income, while an additional 1% of protected area in the 15 km buffer surrounding the ward leads to a 0.1% increase in income. When separating the effects by type, we observe consistently positive impacts from both national parks and other protected areas (middle panel titled “Type”). The machine learning estimation reveals a particularly striking spatial pattern for national parks: while proximity to a national park generates highly positive spillover effects (up to a 0.25% income increase per additional 1% of protected area in the 15 km buffer), there is a smaller or null effect from having a national park inside the ward itself, depending on the model.

![](images/16ad64f52696c9685152ae33960b3e79bd3151a341c4c0946a8b477a57ec7d8e.jpg)  
Figure 2: The effect on monthly household income of all protected areas (left panel), of protected areas by type (middle panel), and of protected areas by age (right panel). Coefficient estimates as dots, 90% confidence intervals in dark color, and 95% confidence intervals in light color. Orange (“Ward”) represents effect of protected areas located inside a ward; purple (“Buffer”) represents effect of protected areas located in a 15 km buffer area surrounding each ward. Squares indicate results from the panel TWFE approach, circles the results from the cross-sectional linear regression (OLS), a

[中间内容因长度限制已省略]

>-0.0674(0.1963)</td><td>0.2549(0.4229)</td><td>-3.309(3.602)</td><td>2.636(3.365)</td><td>-4.328***(1.378)</td></tr><tr><td>Biome 8</td><td>-0.2324**(0.1047)</td><td>0.1797(0.1445)</td><td>0.9189***(0.2635)</td><td>-4.023(2.887)</td><td>-4.813***(1.659)</td><td>2.227(1.489)</td></tr><tr><td>Biome 16</td><td>0.1127(0.0733)</td><td>0.2811(0.2113)</td><td>-0.0221(0.2197)</td><td>2.859(3.813)</td><td>-1.774(2.163)</td><td>1.289(0.9937)</td></tr><tr><td>Biome 19</td><td>0.0524(0.0678)</td><td>-0.1977(0.1444)</td><td>0.1090(0.2111)</td><td>1.626(1.646)</td><td>0.5087(1.002)</td><td>1.073(0.7678)</td></tr><tr><td>Biome 9</td><td>-0.2158(0.1354)</td><td>-0.0903(0.1268)</td><td>0.3625(0.2761)</td><td>-1.997(4.038)</td><td>-1.300(1.670)</td><td>-1.972(1.446)</td></tr><tr><td>Biome 26</td><td>0.1076(0.0867)</td><td>0.1750(0.1482)</td><td>0.0346(0.2394)</td><td>-2.552(2.427)</td><td>1.406(1.306)</td><td>-2.157*(1.116)</td></tr><tr><td>Biome 29</td><td>0.4772***(0.1728)</td><td>0.1532(0.1782)</td><td>0.2048(0.3602)</td><td>-0.6374(3.168)</td><td>-0.4228(1.713)</td><td>0.9681(1.413)</td></tr><tr><td>Biome 18</td><td>0.0640(0.1059)</td><td>0.0088(0.1404)</td><td>-0.3731**(0.1843)</td><td>-1.033(2.166)</td><td>-1.328(1.088)</td><td>1.085(1.105)</td></tr><tr><td>Fixed-effects year</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="7">Fit statistics</td></tr><tr><td> $R^2$ </td><td>0.46111</td><td>0.15866</td><td>0.22584</td><td>0.14111</td><td>0.47220</td><td>0.47523</td></tr><tr><td>Observations</td><td>292,955</td><td>292,955</td><td>292,955</td><td>292,955</td><td>292,955</td><td>292,955</td></tr></table>

Custom standard-errors in parentheses  
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1  
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.31: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–Protected Areas by Size

<table><tr><td>Dependent Variables: Model:</td><td>CR+EN (1)</td><td>VU (2)</td><td>NT (3)</td><td>LC (4)</td><td>Urban (5)</td><td>Non-urban (6)</td></tr><tr><td colspan="7">Variables</td></tr><tr><td>Size Q1 (Smallest)</td><td>-0.7726(1.119)</td><td>-2.442(2.526)</td><td>-10.01*(5.313)</td><td>24.71(100.1)</td><td>29.99(29.64)</td><td>-34.27(25.52)</td></tr><tr><td>Size Q2</td><td>-0.3939(0.3322)</td><td>-0.4034(0.3902)</td><td>0.5977(1.380)</td><td>6.909(10.51)</td><td>1.013(6.088)</td><td>1.137(3.669)</td></tr><tr><td>Size Q3</td><td>0.2214(0.4624)</td><td>0.0159(0.2742)</td><td>2.987***(1.039)</td><td>6.991(5.302)</td><td>-5.217(4.797)</td><td>2.429(3.041)</td></tr><tr><td>Size Q4 (Largest)</td><td>1.185***(0.2946)</td><td>0.0694(0.0518)</td><td>0.1057(0.1519)</td><td>-1.916(1.517)</td><td>-4.878***(0.8333)</td><td>2.589**(1.155)</td></tr><tr><td>Fixed-effects year</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="7">Fit statistics</td></tr><tr><td> $R^2$ </td><td>0.22302</td><td>0.00419</td><td>0.01723</td><td>0.00460</td><td>0.08230</td><td>0.04977</td></tr><tr><td>Observations</td><td>292,974</td><td>292,974</td><td>292,974</td><td>292,974</td><td>292,974</td><td>292,974</td></tr></table>

Custom standard-errors in parentheses  
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1  
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.32: Estimated Effect of Travel Cost on National Park Visitation

<table><tr><td></td><td>(1)Heterogeneous</td><td>(2)Pooled</td></tr><tr><td>Travel Cost (2023 R) × Domestic</td><td> $-1.028 \times 10^{-3}$  $(1.048 \times 10^{-4})$ </td><td></td></tr><tr><td>Travel Cost (2023 R) × International</td><td> $-1.286 \times 10^{-4}$  $(3.436 \times 10^{-5})$ </td><td></td></tr><tr><td>Travel Cost (2023 R)</td><td></td><td> $-2.598 \times 10^{-4}$  $(5.377 \times 10^{-5})$ </td></tr><tr><td> $R^{2}$ </td><td>0.861</td><td>0.858</td></tr><tr><td>Observations</td><td>48,415</td><td>48,415</td></tr></table>

Notes: This table presents the results from estimating Equation 10 by ordinary least squares regression. Column (1) is our primary specification, allowing the travel cost coefficient to differ between domestic and international visitors. Column (2) imposes a single travel cost coefficient as a robustness check. Both specifications include park fixed effects and origin-by-fiscal year fixed effects. Standard errors clustered at the origin level in parentheses. The main-text estimates that a $1\%$ increase in travel cost reduces visits by $1.4\%$ (domestic) and $2.1\%$ (international) are computed from the coefficients in Column (1) using Equation 13, $\eta_{ojt} = \hat{\alpha}_{g(o)} \times TC_{ojt} \times (1 - s_{ojt})$ , where $\hat{\alpha}_{g(o)}$ is the travel cost coefficient for the group (domestic or international) to which origin $o$ belongs, $TC_{ojt}$ is the travel cost for an origin-park-year, and $s_{ojt}$ is the smoothed visit share defined in Equation 9. Reported main-text values are visitor-weighted means computed separately for domestic and international visitors. The number of observations (48,415) is fewer than the total number of origin-park-year combinations (48,246 international + 1,926 domestic = 50,172) because Table Mountain and West Coast National Parks are missing data on the number of visitors for all but the final two years of our study period.
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
