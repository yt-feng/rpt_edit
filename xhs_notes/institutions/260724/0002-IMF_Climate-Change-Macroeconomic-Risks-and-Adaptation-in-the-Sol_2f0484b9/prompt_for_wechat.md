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
# Climate Change, Macroeconomic Risks, and Adaptation in the Solomon Islands

Emanuele Massetti and Filippos Tagklis

SIP/2026/069

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 10, 2026. This paper is also published separately as IMF Country Report No 26/167.

2026
JUL

![](images/6f41f75f63b82d569c9c9f7f1ca428cab9d6b150c3bfeef8805551c52122327f.jpg)

# IMF Selected Issues Paper Asia Pacific Department

# Climate Change, Macroeconomic Risks, and Adaptation in the Solomon Islands Prepared by Emanuele Massetti and Filippos Tagklis (FAD)

Authorized for distribution by Nada Choueiri
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 10, 2026. This paper is also published separately as IMF Country Report No 26/167.

ABSTRACT: The Solomon Islands faces growing macroeconomic challenges from climate change. Rising temperatures, changing marine ecosystems, and sea-level rise are expected to affect economic growth, public finances, and key export sectors over the coming decades. This paper combines climate projections and empirical evidence to assess these risks and evaluate adaptation priorities. While fisheries are projected to face declining productivity and coastal areas increasing exposure to inundation, sustainable forestry management could generate economic gains. The findings underscore the need for efficient adaptation policies, strengthened resource management, and robust decision-making frameworks to enhance long-term economic resilience.

RECOMMENDED CITATION: Massetti, Emanuele, and Filippos Tagklis. 2026. "Climate Change, Macroeconomic Risks, and Adaptation in the Solomon Islands." Selected Issues Paper (SIP/26/069), 2026 Article IV Consultation, International Monetary Fund, Washington, DC.

<table><tr><td>JEL Classification Numbers:</td><td>Q54, Q58, O44, E62</td></tr><tr><td>Keywords: [Type Here]</td><td>Climate change; adaptation; Solomon Islands; sea-level rise; fisheries; forestry; macroeconomic impacts; climate resilience; coastal adaptation; sustainable development; Pacific Island Countries.</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>ftagklis@imf.org; emassetti@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# Climate Change, Macroeconomic Risks, and Adaptation in the Solomon Islands

Solomon Islands

Prepared by Emanuele Massetti and Filippos Tagklis $^{1}$

# SOLOMON ISLANDS

SELECTED ISSUES

June 10, 2026

Approved By

Nada Choueiri

Prepared By Emanuele Massetti and Filippos Tagklis

## CONTENTS

## CLIMATE CHANGE, MACROECONOMIC RISKS, AND ADAPTATION IN THE

SOLOMON ISLANDS \_\_\_\_ 2

A. Climate Trends and Projections \_\_\_\_ 2

B. Macroeconomic Impacts 8

C. Effective and Efficient Adaptation Policy \_\_\_\_ 16

## BOXES

1. The Impact of Climate Change on the Forestry Sector \_\_\_\_ 11

2. Estimating the Cost of Sea Level Rise \_\_\_\_ 15

3. Policies to Facilitate Private Adaptation \_\_\_\_ 17

## FIGURES

1. Historical Temperature and Precipitations for Solomon Islands \_\_\_\_ 3

2. Projected Annual Temperature, Total Annual Precipitations for the Solomon Islands 4

3. Projected Changes of Extreme Precipitation and Dry Periods \_\_\_\_ 5

4. Sea-Level Rise Projections Relative to 2000 level (meters)\_\_\_\_6

5. Projected Changes of Exploitable Fish Biomass in the Solomon Islands' Waters \_\_\_\_7

6. Impact of Warming Trends on Real GDP, Solomon Islands (percentage) \_\_\_\_ 9

7. Cumulative Density Functions of Population and Economic Variables, at Different

Distances from the Coastline and Different Elevations 13

8. Cost of Sea-Level Rise (in percentage of GDP), Annual Average 2020-2099 \_\_\_\_ 14

References 19

# CLIMATE CHANGE, MACROECONOMIC RISKS, AND ADAPTATION IN THE SOLOMON ISLANDS $^{1}$

This paper examines the evolving risks and adaptation challenges facing the Solomon Islands due to climate change, with emphasis on rising temperatures, changes in marine ecosystems, and sea level rise. Utilizing recent scientific data, empirical literature, and sectoral models, it assesses the projected economic impacts, including potential aggregate GDP losses, vulnerabilities in the fisheries and forestry sectors, and the costs associated with sea-level rise. The analysis underscores the necessity of robust adaptation strategies and sustainable resource management to mitigate these risks. It argues that effective adaptation requires strategic government action to prioritize resources, implement cost-efficient policies, and address market barriers that limit private adaptive responses. Drawing on macro-fiscal guidance and practical experience, the paper outlines key principles for designing climate adaptation policies—stressing the significance of climate-specific interventions and the use of cost-benefit analysis as a consistent evaluation tool. The findings aim to inform policymakers about targeted adaptation strategies to enhance economic resilience in the Solomon Islands.

## A. Climate Trends and Projections

Drawing on recent scientific data and model-based projections, this section provides an overview of the evolving risks and adaptation challenges posed by a warming climate, changes in marine ecosystems, and sea level rise.

1. Solomon Islands has a warm, humid tropical climate shaped by its position in the western tropical Pacific. Historically, mean temperatures remained fairly stable until the late 20 $^{th}$ century, after which a clear warming trend emerged consistently with broader Pacific patterns. During the 1985–2014 baseline period, which serves as a benchmark for future climate scenarios, average annual temperatures were around 26-27 °C—approximately 0.4–0.6 °C above pre-industrial levels—and are estimated to have risen by an additional \~0.5 °C by 2020 (Figure 1). $^{2}$ This gradual but persistent warming provides the background against which climate-related macroeconomic risks and policy challenges are expected to intensify over time.

2. Solomon Islands experiences high interannual rainfall variability characteristic of the western tropical Pacific. The country has a humid equatorial-to-tropical climate with substantial precipitation throughout the year. Data on historical precipitations show a recent positive trend in annual rainfall and reveal pronounced year-to-year fluctuations linked to El Nino Southern Oscillation-(ENSO) (Figure 1).

Figure 1. Historical Temperature and Precipitations for Solomon Islands  
![](images/b8b74add0f6ad46d151c74bc4011749439adc012668b158134e81f100e85a8ac.jpg)

![](images/4fd0448a0778958de60c448d46bcb1d413a4194dd2eede0fae3c5b0fbe03c681.jpg)  
Notes: The solid gray line displays annual mean temperature. The solid black line displays the 30-year moving average. The first complete 15 years of the moving average are not shown because incomplete. The last 14 years show a linear trend estimated using the last 30 years of annual data (dashed).  
Source: FADCP Climate Dataset (Massetti and Tagklis, 2024), using ERA5 reanalysis data (Hersbach and others 2023).

3. Solomon Islands is projected to experience continued warming through the end of the century, while projections of future rainfall patterns are highly uncertain. Median projections among climate models show temperature increases of 0.9–1.2 °C by 2050 and 12.2 °C by 2085, relative to the 1985–2014 baseline, depending on emissions pathways. In a high-emissions scenario (SSP3-7.0, 90th percentile), warming could reach 3°C by 2085 (Figure 2). Climate models do not project changes of total annual rainfall compared to the 1960-2015 average, suggesting that the recently observed positive trend may be transitory (Figure 2). Natural rainfall variability —rather than changes in long-run averages—suggests that economic impacts are likely to arise primarily through recurrent natural variability shocks. -2.2 °C by 2085, relative to the 1985–2014 baseline, depending on emissions pathways. In a high-emissions scenario (SSP3-7.0, 90th percentile), warming could reach 3°C by 2085.

Figure 2. Projected Annual Temperature, Total Annual Precipitations for the Solomon Islands
Temperature °C    Precipitations (mm)  
![](images/874918933f479139765022bf196af1cec9acf281c4b7f81dd449c2d09d7792fe.jpg)

![](images/a41a6221f540079c6bbb9b28c111560a5bec13b5ad04302826c00c3cca77d0b4.jpg)  
Notes: The gray line describes historical values based on reanalysis (ERA5 for temperature and precipitation). The black line describes the 30-year moving average around each year. Colored lines represent the median of 30-year moving averages of CMIP6 anomalies added to the observed value (thick black line in the year 1999). SSP3-7.0 (red) is a high emission scenario. SSP1-2.6 scenario (blue) is in line with the Paris goal to keep global mean temperature increase below 2 °C with respect to pre-industrial times. SSP2-4.5 (green) represents continuation of present trends.

4. Indices of within-year climate extremes show that intense precipitation events are the primary climate hazard for Solomon Islands and the main source of recurring macroeconomic risks. The analysis of climate extremes relies on four indicators of extreme heat (TX35), drought conditions (CDD), and intense rainfall (Rx1day and Rx5day) commonly used in the scientific literature. $^{3}$ Since 1960, there are no episodes of widespread extreme heat, and none are projected through the end of the century. $^{4}$ By contrast, short-duration heavy rainfall events, measured by maximum 1-day (Rx1day) and 5-day (Rx5day) totals, have intensified in recent decades. These extremes are often associated with tropical systems, including tropical cyclones and monsoon-related disturbances, and continue to drive recurrent flooding, landslides, and infrastructure damage. Projections indicate a slight increase in Rx1day toward the end of the century (Figure 3, left panel). The drought related index (CDD) remains low and is projected to stay at the same levels (Figure 3, right panel). Overall, the dominance of intense precipitation events—rather than extreme heat or prolonged drought—will continue to shape the country's climate risk profile (Figure 3). These patterns imply that risks are more likely to materialize through repeated flood-related

damage to infrastructure and housing rather than through heat-related shocks, reinforcing the importance of resilient public investment and land-use planning.

Figure 3. Projected Changes of Extreme Precipitation and Dry Periods  
Maximum 1-day Precipitations (mm)  
![](images/5b31b0503f528edc4ddd39f3c28869bd03da38f48bc968537242c18f6124c2d9.jpg)

![](images/42f6d7d51b14fea2a5df0a2c99a5f42bb77b0058543f1ec124248fecb51c758b.jpg)  
Changes in Extreme 1-Day Rainfall (Rx1day) Under High Emissions

Medium-term (2041-2060)  
![](images/8504ce2aa2b22569350fb5a0585d96c15fd7664491fa816329b4b89c339d1e0d.jpg)

Long-term (2081-2100)  
![](images/035657e28b48fa31efaf302563cbf6529ccbb6e225d01854123e36a86d2b0552.jpg)

Notes: The top row shows time series of Maximum 1-Day Accumulated Precipitation (left) and the maximum number of Consecutive Dry Days in a year (right). The bottom row displays Maximum of 1-Day Accumulated Precipitation projected changes relative to the 1991-2020 baseline under the SSP3-7.0 scenario from CMIP6 simulations, on a common grid of approximately 100x100 km size. An advanced method for representing ensemble robustness is based on the approach proposed in AR6, categorized into three levels. Robust Signal: Indicates significant changes where at least 80 percent of the models agree on the sign of change. Conflicting Signals: Represented by crosses, indicating significant changes where less than 80 percent of the models agree on the sign of change. No Change or No Robust Signal: Represented by dots, representing areas of low change values and/or low significance, where less than 66 percent of the models exhibit emergent signals.

5. Sea-level rise represents a critical challenge for Solomon Islands, where much of the population, essential infrastructure, and economic activity is in low-elevation coastal zones, including Honiara and other major settlements. In the western tropical Pacific, current projections from the scientific literature (Kopp and others, 2014; see (Figure 4) point to sea-level increases of roughly 0.52 meters under a low-emissions pathway (RCP2.6), 0.62 meters under a moderate pathway (RCP4.5), and up to 0.79 meters under a very high emissions scenario (RCP8.5) by 2100 relative to 2000 levels (Figure 4). Local effects could be greater than the global mean due to coastal erosion, storm-driven surges, and the influence of ENSO events, which can temporarily elevate regional sea levels. Given the concentration of population and economic activity in coastal areas, sea-level rise represents a slow-moving but potentially irreversible source of economic costs and fiscal pressure, with implications for public asset values, distribution of the population, and long-term development planning.

Figure 4. Sea-Level Rise Projections Relative to 2000 Level (Meters)  
![](images/014dd0326a80822b0769ccaba84e37f24bf848b974e08c9f1f6931955c7c7469.jpg)  
Notes: Local (solid) and Global (dotted) Sea-Level Rise (SLR) probabilistic projections until 2100 under three emission scenarios (Paris - RCP 2.6; Moderate - RCP 4.5; Extreme - RCP 8.5). Median SLR for each emission scenario. (right) local SLR probabilistic projections using the Moderate (RCP 4.5) emission scenario.  
Source: Sea-level rise projections from the CIAM model database (Diaz, 2016) based on data from Kopp and others (2014).

6. Tropical cyclones pose a recurrent risk for Solomon Islands, primarily through heavy rainfall, flooding, storm surge, and damaging winds. Although the country lies near the northern edge of the South Pacific cyclone belt, historical events—such as Cyclone Namu (1986)—demonstrate the potential for severe economic and infrastructure damage. Observations do not show a clear long-term trend in cyclone frequency in the region, but variability is high and closely linked to ENSO conditions. Climate projections indicate that while cyclone frequency is likely to remain stable or decline slightly, the intensity of the strongest cyclones is expected to increase, with heavier rainfall and higher peak wind speeds (Chand and others, 2022). Combined with sea-level rise, stronger cyclones are expected to magnify storm-surge impacts and coastal flooding.

7. Marine ecosystems around the Solomon Islands, which underpin the country's fisheries sector, are projected to undergo gradual changes. Warmer waters and shifting currents can alter fish migration routes and reduce the productivity of key stocks, while acidification may affect the health of marine food webs, and declining oxygen levels could further stress coastal ecosystems (IPCC, 2019, SROCC). These changes pose a direct risk to the country's fisheries sector, a critical component of the economy contributing around 4 percent of GDP and supporting the livelihoods and food security of a large share of the population. Projections from the Fisheries and Marine Ecosystem Model Intercomparison Project (FishMIP; FAO,2024) suggest exploitable fish biomass in Solomon Islands' waters could decline by 11 percent under both low- (SSP1-2.6) and high-emissions (SSP5-8.5) scenarios by 2050, and by up to 50 percent under high emissions (SSP5-8.5) by 2100 (Figure 5). Inertia in the climate and oceanic systems explains why impacts on fisheries of different emissions scenarios become significantly different only in the second half of the century. Projected declines in marine biomass could therefore have material macroeconomic implications through lower export earnings, reduced fiscal revenues from fisheries, and heightened food security risks, reinforcing the case for adaptive fisheries management and economic diversification.

<table><tr><td>Long-Term Projections (2081-2100)Low-emissions High-emissions</td><td>Averaged Over the Exclusive Economic Zone(EEZ)</td></tr><tr><td><img src="images/42b622896105bcfb51c953555b836f52a25abcc85cb1e26ee9e738863b18ff9e.jpg"/></td><td>Change in exploitable fish biomass (%)Scenarios Historical SSP1-2.6 SSP5-8.51950 1950 1960 1970 1980 1990 2000 2010 2020 2030 2040 2050 2060 2070 2080 2090 2100</td></tr><tr><td colspan="2">Notes: The two panels on the left show the long-term (2081-2100) projected changes in exploitable fish biomass under different emissions scenarios and in relation to the reference period (mean between 2005-2014). The panel on the right presents the time series of projected changes averaged over Solomon Islands&#x27; Exclusive Economic Zone (EEZ).Source: Fisheries and Marine Ecosystem Model Intercomparison Project (FishMIP) -https://fishmip.org, FishMIP-data and tools</td></tr></table>

Figure 5. Projected Changes of Exploitable Fish Biomass in the Solomon Islands' Waters  
![](images/fc7840f3293707fbe603254225f87e282bf05237cd1f9d5c9fb1b9ecb11b2b93.jpg)

8. Forests in the Solomon Islands are expected to grow faster than in the present due to carbon fertilization and continued favorable climate conditions for biomass growth. CO $_{2}$ fertilization – the phenomenon where elevated atmospheric carbon dioxide enhances photosynthesis (IPCC AR6 WGI, Section 12.3) – leads to faster and more robust tree growth of forests under temperature and precipitations ranges that are projected in the Solomon Islands until the end of the century. By implementing sustainable and efficient forestry practices, the sector's

growth potential can be effectively harnessed to achieve higher productivity, increased timber output, greater value added, and expanded export opportunities (see Section B).

## B. Macroeconomic Impacts

Drawing on recent empirical literature and sectoral modeling, this section summarizes the projected economic impacts of gradual climate change in the Solomon Islands. It quantifies potential losses in aggregate GDP linked to gradual temperature increases, impacts in the fishery and forestry sectors, and the cost of sea-level rise. The section highlights the importance of adaptation measures and sustainable resource management to mitigate these risks.

9. Slow onset warming, changes in productivity of fisheries and the forestry sector, and rising sea levels, are expected to have macroeconomic relevance in the Solomon Islands. This section relies on advanced analytical methods published in the peer 

[中间内容因长度限制已省略]

oastal road with expected lifetime of 40 years in an area that will be inundated in 2050). New coastal assets, like seaports, should be built factoring in projected sea level rise. Enforceable land tenure rights in the proximity of these coastal perimeters should be defined to facilitate the relocation of the population at-risk of coastal inundation.

\- A shared set of workable principles should be established to define and implement optimal adaptation solutions in the near term and refined over time to gradually support budgetary and societal trade-offs of growing complexity. CBA can provide a consistent and implementable decision-making framework, complemented by a set of rules to assess distributional implications.

## References

Albert, Simon, Kirsten Abernethy, Badin Gibbs, Alistair Grinham, Nixon Tooler, and Shankar Aswani. "Cost-effective methods for accurate determination of sea level rise vulnerability: A Solomon Islands example." Weather, Climate, and Society 5, no. 4 (2013): 285-292. Open Access.

Aligishiev, Z., M. Bellon, and E. Massetti. 2022. “Macro-Fiscal Implication of Adaptation to Climate Change.” IMF Staff Climate Note 2022.002, International Monetary Fund, Washington, DC.

Copernicus Climate Change Service, Climate Data Store, (2021): CMIP6 climate projections. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). DOI: 10.24381/cds.c866074c

Bellon, M. and E. Massetti. 2022a. "Economic Principles for Integrating Adaptation to Climate Change into Fiscal Policy." IMF Staff Climate Note 2022.001, International Monetary Fund, Washington, DC.

Bellon, M. and E. Massetti. 2022b. "Planning and Mainstreaming Adaptation to Climate Change in Fiscal Policy." IMF Staff Climate Note 2022.003, International Monetary Fund, Washington, DC.

Bondarenko M., Priyatikanto R., Tejedor-Garavito N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk B., Brinkhoff T., Tatem A., Sorichetta A. (2025). The spatial distribution of population in 2015-2030 at a resolution of 30 arc (approximately 1km at the equator) R2025A version v1. Global Demographic Data Project - Funded by The Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and Environmental Science, University of Southampton. DOI:10.5258/SOTON/WP00845

Chand, Savin; Webb, Leanne; Grose, Michael; Gooley, Geoff. Tropical cyclones and climate change: Implications for Pacific Island countries. Aspendale: CSIRO; 2022. csiro:EP2021-3604. https://doi.org/10.25919/pbtc-1y82

Diaz, Delavane B. "Estimating global damages from sea level rise with the Coastal Impact and Adaptation Model (CIAM)." Climatic Change 137, no. 1 (2016): 143-156.

FAO, 2024: Projected impacts of climate change on exploitable marine fish biomass: Results from the Fisheries and Marine Ecosystem Model Intercomparison Project (FishMIP). FAO Fisheries and Aquaculture Technical Paper No. 710. Rome, FAO. https://doi.org/10.4060/cc9783en

Favero, Alice, Robert Mendelsohn, Brent Sohngen, and Benjamin Stocker. "Assessing the long-term interactions of climate change and timber markets on forest land and carbon storage." Environmental Research Letters 16, no. 1 (2021): 014051.

Government of Solomon Islands, Ministry of Environment, Climate Change, Disaster Management and Meteorology. 2023. Solomon Islands National Climate Change Policy 2023–2032. Honiara: Government of Solomon Islands.

Harris I, Osborn TJ, Jones P and Lister D (2020). Version 4 of the CRU TS Monthly High-Resolution Gridded Multivariate Climate Dataset. Scientific Data (https://doi.org/10.1038/s41597-020-0453-3).

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023): ERA5 hourly data on single levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.adbb2d47.

IPCC, 2019: IPCC Special Report on the Ocean and Cryosphere in a Changing Climate. [H.-O. Pörtner, D.C. Roberts, V. Masson-Delmotte, and others (eds.)]. Cambridge University Press, Cambridge, UK and New York, NY, USA, 755 pp. https://doi.org/10.1017/9781009157964

Kahn, Matthew E., Kamiar Mohaddes, Ryan NC Ng, M. Hashem Pesaran, Mehdi Raissi, and Jui-Chung Yang (2021). "Long-term macroeconomic effects of climate change: A cross-country analysis." Energy Economics 104: 105624.

Kopp RE, Horton R, Little C, Mitrovica JX, Oppenheimer M, Rasmussen DJ, Strauss BH, Tebaldi, C (2014) Probabilistic 21st and 22nd century sea-level projections at a global network of tide gauge sites. Earth's Future pp 383{406}.

Massetti, E. and F. Tagklis (2024). FADCP Climate Dataset: Temperature and Precipitation. Reference Guide, Fiscal Affairs Department, International Monetary Fund, Washington DC.

Ministry of Environment, Conservation and Meteorology. 2008. Solomon Islands National Adaptation Programme of Action. Honiara: Government of Solomon Islands; United Nations Development Programme.

Mohaddes, K., and M. Raissi. 2025. "Rising Temperatures, Melting Incomes: Country-Specific Macroeconomic Effects of Climate Scenarios." PLOS Climate 4(9): e0000621. https://doi.org/10.1371/journal.pclm.0000621

Samuele Centorrino, Emanuele Massetti, Mehdi Raissi, and Filippos Tagklis. "How to Include the Effects of Rising Temperatures in Long-Term GDP Projections", IMF How To Notes 2025, 009 (2025).

Woods, D., T. McKeen, A. Cunningham, R. Priyatikanto, A. Sorichetta, A.J. Tatem and M. Bondarenko. 2024 "WorldPop high resolution, harmonised annual global geospatial covariates. Version 1.0." University of Southampton: Southampton, UK. DOI:10.5258/SOTON/WP00772
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
