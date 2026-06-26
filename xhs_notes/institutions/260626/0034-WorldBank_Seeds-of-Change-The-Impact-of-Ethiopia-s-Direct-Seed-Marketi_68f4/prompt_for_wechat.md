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
# Seeds of Change

## The Impact of Ethiopia's Direct Seed Marketing Approach on Smallholders' Seed Purchases and Productivity

Dawit Mekonnen

Gashaw T. Abate

Seid Yimam

Rui Benfica

David J. Spielman

Frank Place

POLICY RESEARCH WORKING PAPER 11078

## Abstract

Several factors contribute to the limited use of improved seed varieties in Ethiopia. Among those, on the supply side, is the restricted availability of seeds in the volume, quality, and timeliness required by farmers, partly due to inadequate public and private investment in the sector. Beginning in 2011, the Government of Ethiopia introduced a novel experiment—the direct seed marketing approach—to reduce some of the centralized, state-run attributes of the country's seed market and rationalize the use of public resources. Direct seed marketing was designed to incentivize private and public seed producers to sell directly to farmers rather than through the state apparatus. This study is the first quantitative evaluation of the impact of direct seed marketing on indicators of a healthy seed system: access to quality seeds and farm-level productivity. Using a quasi-experimental difference-in-differences approach suitable to handling variation in treatment timing, the study finds that direct seed marketing led to an increase of 15 percentage points in the proportion of farmers purchasing maize seed, an increase of 45 percent in the quantity of maize seed purchased per hectare, and an increase of 18 percent in maize yield. However, there are differences across crops, with the effects of direct seed marketing on wheat seed purchases and yields being statistically insignificant. These crop-specific differences in performance are likely explained by differences in the reproductive biology of maize (particularly maize hybrids) and wheat, which tend to incentivize commercial activity in hybrid maize seed markets more than in self-pollinating wheat or open-pollinated maize markets. These differences suggest a need for nuanced policy responses, institutional arrangements, and market development strategies to accelerate the adoption of improved varieties.

# Seeds of Change: The Impact of Ethiopia's Direct Seed Marketing Approach on Smallholders' Seed Purchases and Productivity $^{1}$

Dawit Mekonnen, Gashaw T. Abate, Seid Yimam, Rui Benfica, David J. Spielman, and Frank Place

Keywords: Crop yield, Direct seed marketing, Ethiopia, seed system.

JEL classification: Q120; Q130

## 1 Introduction

As in much of Sub-Saharan Africa, agriculture is a critical sector in the Ethiopian economy. One of the key challenges the sector faces is low crop productivity, partly due to low adoption rates of improved crop technologies (Dorosh and Rashid 2013), notably productivity-enhancing improved varieties, quality seeds, complementary inputs, and management practices. Although Ethiopia experienced an increase in the adoption of improved varieties for its main cereal crops between 2010 and 2019, less than a quarter of all smallholders were using improved varieties in 2019, with a relatively higher concentration among maize producers (57 percent) and wheat producers (17 percent) (CSA 2020). Both improved variety adoption and seed replacement rates are lower for most other crops in Ethiopia (Mekonen et al. 2019). $^{2}$

Low rates of improved variety adoption and seed replacement are often associated with demand and supply constraints in the seed market. On the demand side, seed market performance is often constrained by farmers' limited awareness of traits embodied in an improved variety or by other well-documented factors such as credit and liquidity constraints, their perceptions of production and market risks or climate uncertainty, and a range of behavioral factors (Alemu, 2011; Alemu, Rashid, and Tripp 2010; Spielman and Mekonnen 2013). On the supply side, improved varieties or quality seeds are either not available at all, not supplied at the right quantity, time, or location, or do not embody the traits desired by the farmer (Alemu and Tripp 2010; Cavatassi, Lipper, and Narloch 2011; EIAR 2020; Mekonen et al. 2019; Singh et al. 2020; Spielman and Mekonnen 2013).

Ethiopia's seed market faces additional, distinct supply-side constraints. The seed sector remains largely state-controlled, with public enterprises managing crop breeding, multiplication, and seed distribution to farmers in an end-to-end system that historically offered few opportunities for private investment at any point in the supply chain (Spielman and Mekonnen 2013). Since 2011, the Government of Ethiopia, working closely with Wageningen UR, CGIAR, and other partners, has experimented with seed market liberalization to allow firms to market seed directly to farmers rather than through the state's rural administrative apparatus. This Direct Seed Marketing (DSM) approach aimed to increase and sustain the supply of improved varieties and quality seed to farmers while rationalizing the use of public resources allocated to the distribution of seed to fragmented, spatially dispersed, resource-poor smallholders that make up the vast majority of farmers (MoA/ATA 2016).

Since DSM's launch in 2011, several governmental entities—the Agricultural Transformation Agency (ATA), the Ministry of Agriculture (MoA), the regional bureaus of agriculture, development projects such as the Integrated Seed Sector Development (ISSD) initiative—have promoted and closely monitored its implementation. Benson, Spielman, and Kasa (2014) conducted an operational evaluation of the pilot DSM program and found encouraging results, ultimately recommending that the government stay the course and advance the seed sector reform process. Mekonen et al. (2019) conducted a descriptive analysis of DSM's key performance indicators, including seed availability, quality, sufficiency, price competitiveness, supply timeliness, and accountability. Their analysis documented mixed results, including differences in performance across regions and crops.

However, to date, there has been no rigorous assessment of DSM's impact on the amount of fresh seed purchased by farmers, a first-order performance indicator. Nor has there been any assessment of DSM's impact on key outcomes, such as changes in farm-level productivity. The availability of three rounds of household-level panel data from DSM and non-DSM woredas (districts) in 2012 (the beginning of DSM's pilot phase), 2016, and 2019 (after the program had expanded to more than two hundred districts) provides an opportunity to fill this gap in the evaluative literature on DSM.

This study exploits the staggered scale-up of the DSM approach over time, across districts, and in crop coverage. Using a quasi-experimental difference-in-differences econometric approach, the study finds that DSM led to a 14-percentage-point increase in the proportion of farmers purchasing maize seed, a 45 percent increase in the quantity of maize seed purchased per hectare, and an 18 percent increase in maize yield. However, the effects of DSM on seed purchase and yields are not statistically significant for wheat. The results suggest caution in scaling the DSM approach, particularly for self-pollinating crops such as wheat and open-pollinated varieties (OPVs) of maize (as opposed to hybrid maize), especially in the initial stages of implementation. While the pro-market dimension of these findings is relatively straightforward for maize—DSM for hybrid maize succeeds because farmers need to purchase fresh seed each season to capture the yield gains conferred by heterosis, a trait absent in other major crops in Ethiopia—it raises important questions about how markets for other crops will attract private investment from seed companies and how the government can reallocate budgetary resources to other development priorities.

This paper is structured as follows. Section 2 describes the conventional public seed distribution system and the key features and evolution of the DSM approach. Section 3 discusses the data and presents descriptive results. Section 4 outlines the econometric model underlying the evaluation, and section 5 presents the empirical results. Section 6 discusses the findings, and section 7 concludes with a discussion of policy implications and final remarks.

## 2 Public Seed Distribution and DSM in Ethiopia

Following the reforms to agricultural input systems and markets that began in the 1990s in Ethiopia (Dorosh and Rashid 2013), seed production and distribution were, at least in principle, opened to the private sector. In reality, however, Ethiopia's seed sector remained highly concentrated and heavily dominated by public actors such that, by 2004, no more than eight firms were active in seed production (Alemu et al., 2007), with most of them involved exclusively in hybrid maize seed multiplication and not in distribution or retail activities (Langyintuo et al. 2010). Even Pioneer, the sole multinational company present in Ethiopia's seed market for nearly three decades, $^{3}$ produced its hybrids locally and relied primarily on the public distribution system to reach farmers (Spielman and Mekonnen, 2013). Federal and regional extension and input supply agencies accounted for 80 percent of total sales of improved varieties, mostly financed with credit disbursed against public guarantees (World Bank 2006). Most private sector seed producers acted as subcontractors to the state-owned Ethiopian Seed Enterprise (ESE), which distributed seed through the regional extension system, cooperatives, and local administration.

The entire seed system supplied seed to farmers based on official demand projections, which were formally estimated at the local administrative level, aggregated upward through official channels to the regional level, and then further consolidated at the national level. These projections determined the type of varieties and quantity of seed to be produced by ESE and its partners and subsequently distributed back to farmers (Spielman and Mekonnen 2013).

Likewise, promoting new varieties and certified seeds were largely the mandate of public extension and administrative entities at the district and kebele levels (Alemu and Bishaw 2016; Spielman and Mekonnen 2013). $^{4}$ Many studies of Ethiopia’s seed system highlight the numerous bottlenecks and challenges associated with intensive state management. These include inaccurate and often ad hoc demand assessments resulting in persistent mismatches between demand and supply, large carryovers of unsold seed between seasons and years, late seed delivery to farmers, high seed prices relative to farmers’ purchasing power, and seed quality issues, among other problems (Alemu, Rashid, and Tripp 2010; Atilaw and Korbu 2012; DSA 2006; EEA/EEPRI 2006; EIAR 2020; Sahlu and Kahsay 2002; Spielman and Mekonnen 2013).

Despite the eventual emergence of a somewhat favorable policy and regulatory environment for private sector development—including a plant breeders’ rights law that came into effect in 2006 (FDRE 2006)—efforts to attract private investors to Ethiopia’s seed sector to address public sector shortcomings have been severely constrained by several factors. The primary constraint to attracting private investment is the continued existence of the state-led seed system, including the introduction of several state-owned regional seed enterprises in the early 2010s, in addition to ESE, which has effectively crowded out private sector participation. To compete in this market, private investors must invest not only in seed production but also in building distribution and marketing networks capable of competing with the public sector’s system, the low nominal prices (and declining real prices) of ESE seed, and the indirect costs of navigating the regulatory system, accessing financing from a risk-averse banking sector, and meeting high collateral requirements in financial markets (ESA, 2018; Husmann 2015; Spielman et al. 2010, 2012).

Aware of these constraints and the burden the state-run system imposed on scarce public budgetary resources, the Government of Ethiopia began experimenting with the DSM approach in the early

2010s. The DSM approach was piloted by the Integrated Seed Sector Development (ISSD) initiative, a project led by Wageningen UR, in two districts of the Amhara region. In 2012, seven additional districts were brought under DSM, while the two original districts in Amhara briefly suspended the program in 2012 but resumed it in 2013 (Mekonen et al. 2019). In 2013, the ATA and MoA expanded the approach to cover additional districts.

The DSM rollout coincided with three rounds of the Ethiopian Agricultural Commercialization Clusters (ACC) survey, the main data source used in this study (and described in the next section). The first ACC round was conducted in 2012, followed by a second round in 2016 and a third in 2019. By 2016, the number of DSM districts had reached 100, and by 2019, it had expanded to 290 across Ethiopia's four main agricultural regions (Amhara, Oromia, Tigray, and the Southern Nations, Nationalities, and Peoples (SNNP) regional state), covering about 43 percent of Ethiopia's 670 rural districts. Only one district from the initial DSM rollout in 2011-12 was included in the 2012 ACC survey round. Due to the lack of pre-intervention data, this district was excluded from the analysis.

The number of crops covered by DSM increased from one crop (maize) in 2011 to ten crops in 2019 (barley, chickpea, faba bean, horse bean, lentil, maize, sesame, sorghum, teff, and wheat), even though maize and wheat represented 98 percent of seed marketed through DSM. DSM has also grown considerably in the number of private agents (individual input dealers) participating in seed marketing over the years, from 29 in 2012 to about 1,400 in 2019 (Table 1). The approach continues to be used today.

Table 1. Evolution of the DSM approach (2011 - 2019)

<table><tr><td>Year</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td></tr><tr><td>No. of districts</td><td>2</td><td>7</td><td>33</td><td>54</td><td>83</td><td>100</td><td>132</td><td>228</td><td>290</td></tr><tr><td>No. of seed providers/agents</td><td>NA</td><td>29</td><td>124</td><td>294</td><td>456</td><td>650</td><td>800</td><td>1163</td><td>1400</td></tr><tr><td>No. of crops</td><td>1</td><td>1</td><td>1</td><td>4</td><td>6</td><td>6</td><td>7</td><td>8</td><td>10</td></tr></table>

Source: ATA (2020).  
Note: NA = not available.

DSM aims to develop a dynamic, effective, and well-regulated seed sector that provides farmers with timely access to varied, sufficient, affordable, and high-quality seed at competitive prices (Benson, Spielman, and Kasa 2014). Under DSM, both public and private seed producers are authorized to market seed directly to farmers through multiple channels such as primary cooperatives, individual or private agents, and their own trading outlets.

The model distinguishes itself from the conventional seed marketing system in many ways. First, it allows both public and private seed producers to conduct their own demand assessments and then multiply and sell seed in accordance with their assessment of the market. This is intended to address demand and supply mismatches and costly inventory carryovers and shortfalls. Second, DSM aims to considerably shorten the seed distribution chain by allowing seed producers to market directly to farmers, thereby reducing transaction costs associated with the public distribution system. Third, DSM seeks to create a competitive seed market at the final stage of distribution by allowing seed producers to promote their seed and to compete with other seed producers based on price, traits, quality, timeliness of delivery, after-sales service, and other attributes. Fourth, DSM potentially improves seed traceability, providing an accountability mechanism that renders seed producers (instead of extension agents) directly responsible to farmers for seed quality. This accountability mechanism is as important for extension agents as it is for farmers and seed providers: by removing extension agents from the seed exchange equation, extension agents reduce their exposure to reputational risks that accompany the distribution of poor-quality seed to farmers under the conventional state-led distribution system (Benson, Spielman, and Kasa 2014; Mekonen et al. 2019).

DSM's commercial orientation also aims to free up scarce public resources and reduce the time demands on seed system experts, allowing them to focus on improving the overall seed system and broaden the extension service in Ethiopia (Mekonen et al. 2019). For instance, DSM removes extension agents from assessing seed demand and distributing seed to farmers, allowing them to focus on providing better quality and more timely advisory services. Similarly, DSM removes seed system experts in the public sector from similar tasks, providing opportunities to reassign them to varietal development, quality assurance, and other necessary functions. Thus, DSM offers an opportunity to reallocate scarce public resources to activities necessary to make seed markets work effectively and efficiently for farmers and seed producers.

Since its inception, the DSM program's performance has been frequently monitored and assessed to gauge its impact on the timely provision of quality seed to farmers in appropriate quantities and at competitive prices. While results from operational assessments have been critical in informing government actors—who were initially hesitant to concede seed marketing responsibilities to private agents and facilitate the program’s expansion—these assessments do not examine higher-order outcomes such as crop productivity. This study aims to fill this important empirical gap.

## 3 Data and Descriptive Statistics

We used three rounds of the Ethiopian Agricultural Commercialization Clusters (ACCs) panel survey, which interviewed a total of 13,302 rural households in 221 districts across the four agriculturally important regions (Amhara, Oromia, Tigray, and SNNP) in 2012, 2016, and 2019. The coverage of the ACC survey expanded between 2012 and 2019 both across districts and households following the program expansion. The number of sample districts increased from 99 in 2012 to 153 in 2016 and 154 in 2019. Similarly, the number of sample households increased from 3,000 in 2012 to 4,991 in 2016 and 5,311 in 2019. Despite the gradual expansion of the sample, about 74 percent of the households (9,769 observations) were re-interviewed in at least two survey rounds. The sample households were s

[中间内容因长度限制已省略]

hiladelphia: University of Pennsylvania Press.

Spielman, D. J., D. Byerlee, D. Alemu, and D. Kelemework. 2010. “Policies to Promote Cereal Intensification in Ethiopia: The Search for Appropriate Public and Private Roles.” Food Policy 35(3): 185–94.

Spielman, D. J., and D. K. Mekonnen. 2013. Transforming Demand Assessment and Supply Responses in Ethiopia's Seed System and Market. Unpublished report prepared for the Ethiopian Agricultural Transformation Agency. IFPRI, Addis Ababa.

Spielman, D. J., and M. Smale. 2017. “Policy Options to Accelerate Variety Change among Smallholder Farmers in South Asia and Africa South of the Sahara.” IFPRI Discussion Paper 1666, Available at SSRN: https://ssrn.com/abstract=3029612

Thijssen, M. H., Z. Bishaw, A. Beshir, and W. S. de Boef. 2008. Farmers, Seeds and Varieties: Supporting Informal Seed Supply in Ethiopia. Wageningen: Wageningen UR.

World Bank. 2006. World Bank Support to the Ethiopian Seed Sector. Unpublished document. World Bank, Addis Ababa.

Table A1. Summary statistics of pre-treatment levels of control variables across DMS cohorts

<table><tr><td rowspan="2">Variables</td><td colspan="2">All sample</td><td colspan="7">DSM Cohorts</td></tr><tr><td>Mean</td><td>Control</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td></tr><tr><td>Household size (#)</td><td>5.9</td><td>5.8</td><td>6.0</td><td>5.756</td><td>6.3***</td><td>6.1**</td><td>5.5**</td><td>6.1***</td><td>6.1***</td></tr><tr><td>Number of oxen owned (#)</td><td>1.8</td><td>1.8</td><td>1.7</td><td>1.5**</td><td>2.2***</td><td>1.6*</td><td>1.7</td><td>2.0</td><td>2.0*</td></tr><tr><td>Chemical fertilizers (kg)</td><td>82.5</td><td>68.4</td><td>127.1***</td><td>107.6***</td><td>165.2***</td><td>79.4</td><td>83.2</td><td>77.9</td><td>78.0</td></tr><tr><td>Age of household (years)</td><td>46.5</td><td>46.5</td><td>44*</td><td>46.5</td><td>47</td><td>48.4*</td><td>47</td><td>47</td><td>45**</td></tr><tr><td>Gender of the head (1=female)</td><td>0.1</td><td>0.09</td><td>0.07</td><td>0.1</td><td>0.09</td><td>0.17***</td><td>0.15***</td><td>0.1</td><td>0.1</td></tr><tr><td>Education of the head (grades completed)</td><td>3.3</td><td>3.2</td><td>3.6</td><td>3.7</td><td>3.0</td><td>3.6</td><td>3.7**</td><td>3.8***</td><td>3.3</td></tr><tr><td>Farmland owned (in hectares)</td><td>1.8</td><td>1.7</td><td>1.9</td><td>1.2***</td><td>1.8</td><td>1.5**</td><td>1.8</td><td>1.9*</td><td>2.2***</td></tr><tr><td>Agricultural cooperative member (1=yes)</td><td>0.46</td><td>0.45</td><td>0.43</td><td>0.40</td><td>0.59***</td><td>0.45</td><td>0.48</td><td>0.4**</td><td>0.43</td></tr><tr><td>Number of observations</td><td>4,919</td><td>2784</td><td>96</td><td>164</td><td>468</td><td>191</td><td>370</td><td>415</td><td>428</td></tr></table>

Note: \*, \*\*, \*\*\* indicate statistical significance at 10%, 5%, and 1% level, respectively, for the differences in the variables' mean values between each treated cohort and the control group. The values of the variables from the earliest of the three survey rounds in which they appear are used to condition our parallel trend assumption.

Table A2. The impact of DSM on teff seed purchase and yield

<table><tr><td colspan="4">Impact on teff seed purchase</td><td colspan="4">Impact on the quantity of teff seed purchases per hectare</td><td colspan="4">Impact on teff yield</td></tr><tr><td>Cohort</td><td>ATT(g)</td><td>Survey year</td><td>ATT(t)</td><td>Cohort</td><td>ATT(g)</td><td>Survey year</td><td>ATT(t)</td><td>Cohort</td><td>ATT(g)</td><td>Survey year</td><td>ATT(t)</td></tr><tr><td>2015</td><td>0.056(0.087)</td><td>2016</td><td>0.008(0.092)</td><td>2015</td><td>0.164(0.324)</td><td>2016</td><td>0.032(0.322)</td><td>2015</td><td>-0.028(0.127)</td><td>2016</td><td>-0.125(0.164)</td></tr><tr><td>2017</td><td>0.024(0.121)</td><td>2019</td><td>-0.011(0.163)</td><td>2017</td><td>0.053(0.439)</td><td>2019</td><td>-0.049(0.661)</td><td>2017</td><td>0.070(0.167)</td><td>2019</td><td>0.208(0.144)</td></tr><tr><td>2018</td><td>-0.214(0.147)</td><td></td><td></td><td>2018</td><td>-0.587(0.564)</td><td></td><td></td><td>2018</td><td>0.159(0.267)</td><td></td><td></td></tr><tr><td>2019</td><td>-0.015(0.374)</td><td></td><td></td><td>2019</td><td>-0.082(1.468)</td><td></td><td></td><td>2019</td><td>0.355(0.193)</td><td></td><td></td></tr><tr><td>ATT</td><td>-0.020(0.161)</td><td></td><td>-0.002(0.083)</td><td>ATT</td><td>-0.073(0.656)</td><td></td><td>-0.009(0.346)</td><td>ATT</td><td>0.190(0.131)</td><td></td><td>0.042(0.091)</td></tr></table>

Note: ATT refers to the Average Treatment Effect on the Treated group. P-value for a pre-test of parallel trends assumption is 0.151 for seed purchase, 0.087 for quantity of seed purchase, and 0.119 for yield estimates. Control group: “never treated.” Anticipation periods: 0. Estimation method: Doubly Robust. Standard errors are reported in parentheses. Source: Authors’ calculation based on Agricultural Commercialization Clusters 2012, 2016, and 2019 survey data.

Figure A1. The impact of DSM on teff seed purchases and yield: Event study aggregation

(a) Impact on farmers' decision to purchase teff seed  
![](images/bc36834c5b30bee923d91433358bee845aa464e428e3e726724b8bad2204da8f.jpg)

(b) Impact on the quantity of teff seed farmers' purchase  
![](images/1de043e229ceeae4151969fb9d9f24c396fcd6415b182a5e2bc4d6b3cfb5dabe.jpg)  
(c) Impact on the teff yield

![](images/6d4ef86aa8e070c82902b6402db51f833060d65f301a68c0c393f9c7f6933c02.jpg)  
Note: ATT refers to the Average Treatment Effect on the Treated. DSM refers to Direct Seed Marketing. Source: Authors' estimation based on the ACC 2012, 2016, and 2019 survey data.
"""
