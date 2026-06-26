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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Beyond the AI Divide

# A Simple Approach to Identifying Global and Local Overperformers in AI Preparedness

Pierre Mandon

POLICY RESEARCH WORKING PAPER 11073

## Abstract

This paper examines global disparities in artificial intelligence preparedness, using the 2023 Artificial Intelligence Preparedness Index developed by the International Monetary Fund alongside the multidimensional Economic Complexity Index. The proposed methodology identifies both global and local overperformers by comparing actual artificial intelligence readiness scores to predictions based on economic complexity, offering a comprehensive assessment of national artificial intelligence capabilities. The findings highlight the varying significance of regulation and ethics frameworks, digital infrastructure, as well as human capital and labor market development in driving artificial intelligence overperformance across different income levels. Through case studies, including Singapore, Northern Europe, Malaysia, Kazakhstan, Ghana, Rwanda, and emerging demographic giants like China and India, the analysis illustrates how even resource-constrained nations can achieve substantial artificial intelligence advancements through strategic investments and coherent policies. The study underscores the need for offering actionable insights to foster peer learning and knowledge-sharing among countries. It concludes with recommendations for improving artificial intelligence preparedness metrics and calls for future research to incorporate cognitive and cultural dimensions into readiness frameworks.

# Beyond the AI Divide:

A Simple Approach to Identifying Global and Local Overperformers in AI Preparedness

Pierre Mandon (World Bank Group) $^{1}$

Keywords: AI Preparedness; Economic Complexity; Peer Learning; Policy Overperformance.
JEL codes: F63; H11; O33; O38.

The transformative potential of artificial intelligence (AI) is reshaping economies, societies, and global competitiveness (Brynjolfsson and Unger, 2023), making its adoption a critical priority for nations worldwide. $^{2}$ The most prominent accounting and consulting firms claim that AI is projected to contribute significantly to the global economy, with estimates ranging from US2.6 trillion to US4.4 trillion annually (Chui et al., 2023), to US15.7 trillion by 2030, driven by productivity and consumption gains (PwC, 2017). Some recent NBER publications $^{3}$ highlight that AI has the potential to significantly boost productivity and economic growth by automating tasks and driving innovation. However, the realization of these gains depends on complementary policies, institutions, and societal adaptation to ensure equitable and sustainable outcomes (Aghion, Jones, and Jones, 2019; Trammell and Korinek, 2023; Acemoglu, 2024). To summarize, AI, and particularly generative AI, has the potential to boost economic growth and productivity but poses risks of labor market disruptions, including premature de-professionalization—where skilled jobs are replaced or diminished before workers can fully capitalize on their expertise—and challenges for developing economies, such as reduced opportunities for high-skill job creation, increased inequality, and difficulties in integrating AI technologies into less-developed industrial and educational systems (Liu, 2024).

Such substantial socio-economic impacts underscore the critical importance for countries to adopt and integrate AI technologies to remain competitive and keep a sovereign public policy. $^{4}$ However, the benefits of AI are not uniformly distributed. The 2023 Government AI Preparedness Index (AIPI) from the International Monetary Fund (IMF) reveals significant disparities in AI preparedness and readiness among nations, highlighting a growing divide between those equipped to leverage AI and those at risk of falling behind (Cazzaniga et al., 2024). $^{5}$ Related to this, Liu and Wang (2024) highlight that middle-income countries exhibit unexpectedly high engagement with generative AI tools relative to their economic scale, while low-income economies are notably underrepresented. In this context, it becomes imperative to identify effective strategies for enhancing a country's AI readiness. This paper aims to explore such strategies, providing a framework for nations to efficiently bolster their AI capabilities and ensure inclusive growth in the evolving digital landscape.

The methodology outlined in this paper is straightforward: it evaluates AI preparedness at the country level using the AIPi and compares it to each country's assessed level of economic complexity. This approach identifies countries that outperform in AI preparedness and readiness relative to their economic complexity for a given income level, aiming to uncover the factors driving their overperformance. Economic complexity refers to the knowledge intensity of an economy, captured by the diversity and sophistication of the goods and services it produces. The Economic Complexity Index (ECI), initially developed by Hidalgo and Hausmann (2009), measures this complexity by analyzing a country's export mix, reflecting its capabilities to produce and export diverse, high-value products. More recently, the ECI expanded to technology, based on patents data, and research, based on research papers (Stojkoski, Koch, and Hidalgo, 2023), since trade data can miss key information about innovative activities.

Using this methodology, we categorize distinct groups of AI overperformers based on their Economic Complexity Index (ECI) and their preparedness and readiness levels. Notably, overperformers are not simply the countries with the highest AIPI scores but those that (i) meet a minimum AIPI threshold and (ii) outperform their predicted scores given their economic complexity. Among high-income economies, global overperformers include Australia, Japan, the Netherlands, New Zealand, three of the four Asian Tigers (Hong Kong SAR, China; Singapore; and the Republic of Korea), and Northern European countries such as Denmark, Finland, and Norway—aligning with findings on the long-term determinants of AIPI detailed later. Upper-middle-income local overperformers comprise Albania, China, Costa Rica, Indonesia, Kazakhstan, Malaysia, and Ukraine. Finally, lower-middle- and low-income local overperformers include Ghana, India, Morocco, Rwanda, Sri Lanka, Tunisia, and Viet Nam.

From this list of AI overperformers, we observe that AI regulation and ethics consistently emerge as top drivers of AI preparedness across income groups, emphasizing the universal importance of institutions in managing AI integration. In low- and lower-middle-income countries (LICs/LMICs), regulation and workforce development dominate, reflecting foundational priorities amid resource constraints, while digital infrastructure and innovation receive less emphasis. For upper-middle-income countries (UMICs), regulation and human capital remain critical, but digital infrastructure becomes increasingly significant as technological capacities expand. High-income countries (HICs) prioritize regulation alongside well-established digital infrastructure and innovation systems, supported by advanced workforce readiness strategies.

This progression illustrates how AI preparedness strategies align with the unique capacities and priorities of each income group, offering tailored policy pathways for countries aiming to enhance their AI readiness. By understanding these patterns, policy makers can adopt fitted strategies to develop their countries' AI ecosystems based on their specific economic and institutional contexts and might effectively bridge the gap in the global AI divide.

The rest of the paper is organized as follows: Section II outlines the data and methodology, Section III presents the main empirical findings, Section IV examines how different categories of countries overperform in AI preparedness, and Section V concludes and opens avenue for future research on AI preparedness.

## II- Data and Methodology

## II.a- Data

The AIPI serves as our main output of interest and is designed by the IMF to assess the readiness of 174 countries to adopt and integrate AI technologies as of 2023 (Cazzaniga et al., 2024). It is built around four core pillars that are deemed essential for smooth AI adoption: (i) digital infrastructure, (ii) human capital and labor market policies, (iii) innovation and economic integration, and (iv) regulation and ethics. Each dimension is calculated by averaging a set of normalized sub-indicators that capture specific aspects relevant to AI readiness, such as internet accessibility (pillar i), STEM education (pillar ii), R&D investment (pillar iii), and adaptable legal frameworks (pillar iv). $^{6}$ The global AIPI index, scaled from 0 to 1, combines these four pillars, each contributing up to 0.25. Higher scores indicate greater AI preparedness, providing stakeholders with a benchmark for identifying areas needing improvement to enhance AI integration across economies. The AIPI focuses on AI adoption preparedness rather than invention leadership—dominated by China and the United States, $^{7}$ as highlighted in the “Draghi Report”—thereby enabling a comparative assessment of preparedness levels across all economies.

The AIP distribution (Figure 1) reveals substantial disparities in AI preparedness and readiness across nations. Research underscores that AI readiness is influenced by a country's economic structure, infrastructure, and policy environment. For example, Liu and Wang (2024) find strong correlations between income level, digital infrastructure, and human capital with AI uptake, with higher-income nations demonstrating more advanced AI ecosystems. $^{8}$ These findings align with growing evidence of a widening divide between countries equipped to leverage AI and those at risk of being left behind (Cazzaniga et al., 2024).

Figure 1: Global distribution of AIPI (2023)  
![](images/da420063ff77a7bc4cdd57957d82ec14612f42694691104a30b28f2bafe1fde3.jpg)

Source: IMF, AIPI data mapper [https://www.imf.org/external/datamapper/AI\_PI@AIPI/ADVEC/EME/LIC]. Notes: The map is checked and validated by the World Bank Cartography Unit as of February 02, 2025.

A methodological decision in this study is the choice of the recent AIPI from the IMF over the AI Readiness Index developed by the private UK-based consulting firm Oxford Insights. $^{9}$ This decision is primarily driven by the IMF's reputation as a globally recognized multilateral institution and supposed to be accountable, which ensures greater scrutiny and transparency in the development of its products. In contrast, the outputs of private entities like Oxford Insights, though valuable, do not operate within the same level of oversight or accountability. Furthermore, the AI Readiness Index is explicitly designed to assess the extent to which governments are prepared to deploy AI in public service delivery. $^{10}$ In contrast, the AIPI aims to focus on a more comprehensive evaluation of how countries can harness AI capabilities effectively. That said, the choice of index does not significantly impact the broader contribution of this study, as the proposed methodology remains adaptable and replicable.

Employing Bayesian Model Averaging (BMA), we analyze a comprehensive set of 67 historical, political, and economic indicators from growth determinants literature to identify robust predictors of national AIPI. The BMA framework, $^{11}$ as implemented here, enables us to isolate the most robust determinants of AI preparedness from a wide range of potential predictors, as defined and built by Sala-i-Martin, Doppelhofer, and Miller (2004). $^{12}$ Figure 2 illustrates the inclusion probabilities of various covariates in the top 5,000 models. The results highlight that initial conditions—such as life expectancy, higher education levels, and economic size in 1960—along with cultural and geographic influences, including Confucian heritage and an East Asian regional dummy, are positively correlated with AIPI. Conversely, the indicator political instability, captured by the frequency of revolutions and military coups, shows a negative association with AIPI. $^{13}$

Figure 2: Model Inclusion in BMA on AIPI [hyper-g/n prior; random model prior]

![](images/38326a756cb5c6fe90399c555bbaa76f8328fe4a71d4782a49a2e7101186a939.jpg)  
Source: Author's construction, based on the AIPi and the database from Sala-i-Martin, Doppelhofer, and Miller (2004). The database is available here: https://www.openicpsr.org/openicpsr/project/116024/version/V1/view. Notes: The BMA considers a chain of three million recorded draws with one million burn-ins, by applying the birth-death sampler, using the BMS package from Zeugner and Feldkircher (2015). The figure depicts the results of BMA. The explanatory variables are ranked according to their Posterior Inclusion Probabilities (PIPs) from the highest on the top to the lowest at the bottom. The horizontal axis shows the values of cumulative posterior probability. Blue (darker in greyscale) and red (lighter in greyscale) colors denote the positive and negative sign of the estimated parameter of explanatory variable, respectively. No color means the corresponding explanatory variable is not included in the model.

The results from the BMA align with existing literature on the risks of a growing AI divide, emphasizing that established industrialized nations and East Asian economies, particularly those with Confucian cultural influences (i.e., China; Hong Kong SAR, China; Singapore; Korea; and Taiwan, China), consistently lead in AI preparedness and readiness. Conversely, politically unstable countries face significant challenges in this domain. This finding motivates the approach in the current paper to move beyond these general trends by identifying both global and local AI overperformers relative to the complexity of their economic structures. The goal is to uncover how countries can learn from these champions to effectively enhance their AI policy agendas.

To measure the economic complexity of each country, we consider ECIs for trade, technology, and research available on the Observatory of Economic Complexity (OEC) website. $^{14}$ However, since the ECI for technology, derived from patent data, is available for fewer countries (90 compared to 133 for ECI trade and 130 for ECI research), we perform a Principal Component Analysis (PCA) using only ECI trade and ECI research for 2021–22, the most recent years available. The first principal component, which explains over 50 percent of the variance, is used to represent the multidimensional economic complexity of each country. This component is then normalized and scaled between 0 and 1 across the sample of countries.

As highlighted by Hidalgo (2023), ECI offers valuable insights into a country's productive capabilities by analyzing the diversity and sophistication of its exports, and by extension, its academic research. The paper demonstrates how metrics derived from ECI, such as relatedness and complexity, can guide industrial policies and diversification strategies, positioning ECI as a critical tool for identifying opportunities for structural transformation and economic upgrading. ECI's relevance logically extends to capturing ability to adopt cutting-edge technology, such as AI preparedness and readiness, as it reflects a country's knowledge intensity, innovation capacity, and productive capabilities. Higher ECI scores suggest that economies are better equipped to adopt advanced technologies like AI due to their diversified industrial base, skilled workforce, and robust infrastructure.

Finally, the income levels of countries are classified using the World Bank's Atlas Method, incorporating updated income classifications for FY25 based on 2023 GNI per capita data. $^{15}$ This classification is crucial for distinguishing between global AI overperformers, likely concentrated among HICs, and local overperformers within LICs, LMICs, and UMICs.

## II.b- Methodology

To identify AI global and local overperformers, we adopt a two-step approach: (i) identifying countries with AIPI scores above the weighted median and average scores of their respective income groups, $^{16}$ and (ii) determining those with AIPI scores exceeding their predicted values based on their economic complexity. Formally, a weighted least square approach is considered:

$$
A I P I _ {I} = \alpha + \beta E C I _ {i} + \varepsilon_ {i},\tag{1}
$$

$$
\mathrm{where:} m i n _ {\alpha , \beta} P _ {i} (A I P I _ {i} - (\alpha + \beta E C I _ {i})) ^ {2}\tag{2}
$$

$$
\widehat {A I P I} _ {l} = \widehat {\alpha} + \widehat {\beta} E C I _ {i}\tag{3}
$$

The $\widehat{AIPI}$ index for country i is then predicted by an intercept $\hat{\alpha}$ , and the first component of the ECI on trade and research $\hat{\beta}$ , weighted by the population size of each country. Such weighting is crucial to ensure the real-world representativeness of AI preparedness and economic complexity index scores. $^{17}$ The ex-ante idiosyncratic error term ( $\varepsilon_{i}$ ) or ex-post residual term ( $\widehat{\varepsilon_{i}}$ ) captures respectively the theoretical and actual gap between observed AIP1 and predicted $\widehat{AIPI}$ scores. Accordingly, a country is classified as an overperformer if:

$$
\left\{ \begin{array}{l} A I P I _ {i} > \widehat {A I P I _ {\iota}}, o r \widehat {\varepsilon_ {\iota}} > 0 \\ A I P I _ {i} > A I P I _ {i, t h e s h o l d} \end{array} \right.\tag{4}
$$

where $A_{IPI_{i,threshold}}$ indicates the relevant average and median AICI score for country i for relevant income categories.

## III- Empirical findings

## III.a- Global overperformers

The analysis of the two charts below, one unweighted and the other weighted by population size, reveals important insights about the relationship between the AIPI and the ECI trade, research composite obtained from 125 matching countries at a global level (Figure 3). $^{18}$ A strong relationship emerges between AIPI and ECI, with $R^{2}$ values of 0.79 (unweighted) and 0.70 (weighted), indicating that approximately three-quarters of the variance in AIPI is explained by the variance in ECI, and vice versa. The partial correlations (r) of 0.89 (unweighted) and 0.84 (weighted) further indicate a very high positive linear correlation, and it is statically significant at 0.1 percent. These results highlight the strong (and expected) link between economic complexity and AI preparedness, demonstrating that greater economic sophistication—reflected in the diversity and complexity of exports and research output—significantly enha

[中间内容因长度限制已省略]

a</td><td>Sub-Saharan Africa</td><td>LIC</td><td>0.246</td><td>0.437</td><td>0.388</td><td>Yes (Local)</td></tr><tr><td>94</td><td>Saudi Arabia</td><td>Middle East and North Africa</td><td>HIC</td><td>0.459</td><td>0.577</td><td>0.528</td><td>No</td></tr><tr><td>95</td><td>Senegal</td><td>Sub-Saharan Africa</td><td>LMC</td><td>0.228</td><td>0.396</td><td>0.376</td><td>No</td></tr><tr><td>96</td><td>Serbia</td><td>Europe and Central Asia</td><td>UMC</td><td>0.500</td><td>0.537</td><td>0.561</td><td>No</td></tr><tr><td>97</td><td>Singapore</td><td>East Asia and Pacific</td><td>HIC</td><td>0.718</td><td>0.801</td><td>0.660</td><td>Yes (Global)</td></tr><tr><td>98</td><td>Slovak Republic</td><td>Europe and Central Asia</td><td>HIC</td><td>0.528</td><td>0.592</td><td>0.563</td><td>No</td></tr><tr><td>99</td><td>Slovenia</td><td>Europe and Central Asia</td><td>HIC</td><td>0.627</td><td>0.634</td><td>0.613</td><td>No</td></tr><tr><td>100</td><td>South Africa</td><td>Sub-Saharan Africa</td><td>UMC</td><td>0.588</td><td>0.497</td><td>0.607</td><td>No</td></tr></table>

Table A.2: Descriptive statistics (end)

<table><tr><td></td><td>Country</td><td>Region</td><td>Income level</td><td>ECI (multi., scaled)</td><td>AIPI (observed)</td><td>AIPI (predicted)</td><td>Overperformer</td></tr><tr><td>101</td><td>Korea, Rep.</td><td>East Asia and Pacific</td><td>HIC</td><td>0.670</td><td>0.727</td><td>0.635</td><td>Yes (Global)</td></tr><tr><td>102</td><td>Spain</td><td>Europe and Central Asia</td><td>HIC</td><td>0.776</td><td>0.648</td><td>0.689</td><td>No</td></tr><tr><td>103</td><td>Sri Lanka</td><td>South Asia</td><td>LMC</td><td>0.239</td><td>0.436</td><td>0.383</td><td>Yes (Local)</td></tr><tr><td>104</td><td>Sudan</td><td>Sub-Saharan Africa</td><td>LIC</td><td>0.041</td><td>0.233</td><td>0.251</td><td>No</td></tr><tr><td>105</td><td>Sweden</td><td>Europe and Central Asia</td><td>HIC</td><td>0.928</td><td>0.748</td><td>0.766</td><td>No</td></tr><tr><td>106</td><td>Switzerland</td><td>Europe and Central Asia</td><td>HIC</td><td>0.991</td><td>0.757</td><td>0.798</td><td>No</td></tr><tr><td>107</td><td>Taiwan, China</td><td>East Asia and Pacific</td><td>HIC</td><td>0.652</td><td>0.669</td><td>0.626</td><td>No</td></tr><tr><td>108</td><td>Tajikistan</td><td>Europe and Central Asia</td><td>LMC</td><td>0.058</td><td>0.366</td><td>0.262</td><td>No</td></tr><tr><td>109</td><td>Tanzania</td><td>Sub-Saharan Africa</td><td>LMC</td><td>0.249</td><td>0.352</td><td>0.390</td><td>No</td></tr><tr><td>110</td><td>Thailand</td><td>East Asia and Pacific</td><td>UMC</td><td>0.517</td><td>0.536</td><td>0.570</td><td>No</td></tr><tr><td>111</td><td>Togo</td><td>Sub-Saharan Africa</td><td>LIC</td><td>0.039</td><td>0.316</td><td>0.250</td><td>No</td></tr><tr><td>112</td><td>Tunisia</td><td>Middle East and North Africa</td><td>LMC</td><td>0.320</td><td>0.465</td><td>0.437</td><td>Yes (Local)</td></tr><tr><td>113</td><td>Türkiye</td><td>Europe and Central Asia</td><td>UMC</td><td>0.632</td><td>0.540</td><td>0.629</td><td>No</td></tr><tr><td>114</td><td>Uganda</td><td>Sub-Saharan Africa</td><td>LIC</td><td>0.309</td><td>0.354</td><td>0.430</td><td>No</td></tr><tr><td>115</td><td>Ukraine</td><td>Europe and Central Asia</td><td>UMC</td><td>0.356</td><td>0.512</td><td>0.487</td><td>Yes (Local)</td></tr><tr><td>116</td><td>United Arab Emirates</td><td>Middle East and North Africa</td><td>HIC</td><td>0.404</td><td>0.628</td><td>0.500</td><td>No</td></tr><tr><td>117</td><td>United Kingdom</td><td>Europe and Central Asia</td><td>HIC</td><td>0.980</td><td>0.731</td><td>0.792</td><td>No</td></tr><tr><td>118</td><td>United States</td><td>North America</td><td>HIC</td><td>1.000</td><td>0.771</td><td>0.803</td><td>No</td></tr><tr><td>119</td><td>Uruguay</td><td>Latin America and Caribbean</td><td>HIC</td><td>0.429</td><td>0.549</td><td>0.513</td><td>No</td></tr><tr><td>120</td><td>Uzbekistan</td><td>Europe and Central Asia</td><td>LMC</td><td>0.156</td><td>0.346</td><td>0.328</td><td>No</td></tr><tr><td>121</td><td>Venezuela, RB</td><td>Latin America and Caribbean</td><td>UMC</td><td>0.178</td><td>0.275</td><td>0.395</td><td>No</td></tr><tr><td>122</td><td>Viet Nam</td><td>East Asia and Pacific</td><td>LMC</td><td>0.285</td><td>0.482</td><td>0.414</td><td>Yes (Local)</td></tr><tr><td>123</td><td>Yemen, Rep.</td><td>Middle East and North Africa</td><td>LIC</td><td>0.002</td><td>0.253</td><td>0.225</td><td>No</td></tr><tr><td>124</td><td>Zambia</td><td>Sub-Saharan Africa</td><td>LMC</td><td>0.252</td><td>0.371</td><td>0.392</td><td>No</td></tr><tr><td>125</td><td>Zimbabwe</td><td>Sub-Saharan Africa</td><td>LMC</td><td>0.225</td><td>0.305</td><td>0.374</td><td>No</td></tr></table>

Source: The AIPI score for 2023 is obtained from the IMF website [https://www.imf.org/external/datamapper/datasets/AIPI] and the ECI on trade and research for 2021-22 are obtained from the OEC website [https://oec.world/en/rankings/eci/hs6/hs96?tab=ranking]. Notes: The first PCA of ECI trade and ECI research, with an eigenvalue exceeding 50 percent (normalized and scaled between 0 and 1 across the sample of countries) is reported here. Global and local overperformers are identified through a two-step approach: (i) comparing AIPI scores to the weighted median and average of income groups, and (ii) identifying scores exceeding predicted values based on economic complexity. Population size for 2023, used for the weighted analysis to obtain the AIPI predicted score, is sourced from the “wbopendata” module in Stata (Azevedo, 2020), with data for Taiwan Province of China obtained from the Statista website. For more details, see the \`\` Data and Methodology" and \`\` Empirical Findings" sections.
"""
