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
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
# Weather Shocks and Rural Economic Linkages

Evidence from Rajasthan's Agricultural and Non-Agricultural Sectors

Francis Addeah Darko

Akankshita Dey

S. K. Ritadhi

POLICY RESEARCH WORKING PAPER 11079

## Abstract

This study examines the complex relationships between rainfall shocks, agricultural productivity, and rural economic activity in Rajasthan, India's largest state. Using district-level agricultural data from 1990 to 2015, enterprise surveys from 2010 to 2016, and household consumption data from 2014 to 2016, the research analyzes three key relationships. First, positive rainfall shocks increase agricultural productivity by approximately 7 percent compared to negative shocks, with irrigation infrastructure significantly moderating this effect. Second, these weather-induced agricultural productivity changes have substantial spillover effects on rural non-farm enterprises, particularly those engaged in retail trade. Specifically, positive rainfall shocks in-crease enterprise revenues by 25.7 percent and value-addition by

30.3 percent, primarily through increased local demand for non-tradable goods. Third, rural household consumption responds positively to favorable rainfall conditions, with monthly per capita expenditures increasing by 6 percent during positive rainfall shocks. This increase is predominantly driven by higher spending on luxury goods rather than essential items, supporting the demand-side channel through which weather shocks affect non-farm enterprise performance. These findings highlight the strong interconnections between agricultural conditions and non-farm economic activity in rural areas, with important implications for policies aimed at building rural economic resilience in the context of increasing weather variability.

# Weather Shocks and Rural Economic Linkages: Evidence from Rajasthan's Agricultural and Non-Agricultural Sectors

Francis Addeah Darko\*

Akankshita Dey $^{\dagger}$

S. K. Ritadhi $^{\dagger}$

JEL: Q54, O13, Q12
Keywords: Rainfall shock, agricultural productivity, non-farm enterprise, rural economy

## 1 Introduction

Agriculture continues to be a vital sector in the rural economy of India. It contributed around 18 percent of India's GDP in 2021 to 2022 (Reserve Bank of India, 2022) and engaged nearly 42 percent of the total workforce (Ministry of Statistics and Program Implementation, 2022). Despite the relatively low share of agriculture in GDP, the high share of employment still indicates its importance in the rural economy and its low productivity. Empirical evidence finds that agricultural growth has a strong impact on rural poverty reduction in India. Dev and Muntashir (2019) showed that a 1 percent rise in the growth of agriculture reduces rural poverty by 0.45 percent, which was the highest impact compared to growth in other sectors. Agriculture has a strong multiplier effect owing to backward and forward linkages. It generates effective demand for inputs and services such as fertilizers, machinery, and industrial goods and it also stimulates agro-processing and rural services (Pingali, 2019). Around half of the rural households still derive their major source of income from agriculture, according to the latest estimates (NSSO, 2021).

Rajasthan, the largest state in terms of area, is one of the most diverse agricultural systems in India. The state has unique geo-climatic conditions that influence its agricultural contribution to the Indian economy, with a preponderance of oilseed, pulses and coarse cereals (Swain et al., 2012). ICRISAT estimates suggest that 54 percent of Rajasthan's total area is cultivated, with 20 percent considered less cultivated, and the rest unsuitable for agricultural production, and the sequelae for farmers' condition in various climatic zones it has from the arid Thar desert to the eastern plains (Rathore, 2004). Among the major constraints to meeting the agricultural potential present in Rajasthan, the limitations of water stand out; with less than half of the cultivated area is irrigated, and the tutelary rains differ from $300\mathrm{mm}$ in the western region to more $1000\mathrm{mm}$ on the eastern border (Rathore et al., 2013). A study of the long-term rain data indicates that the districts face 15 percent positive rain shock probability and 19 percent negative shock probability. The crops are diversified, and at least seven crops characterize the agricultural system: wheat, millets, maize, chickpeas, pulses, mustard and soybean (Singh et al., 2016). The variability in rainfall and the consequent weather shocks not only affect crop yields, but also significantly hinder the potential for economic diversification in rural communities, exacerbating vulnerabilities across both agricultural and non-farm sectors.

The relationship between weather patterns and agricultural productivity has become increasingly critical to understand as climate variability intensifies. Research demonstrates that rainfall variations significantly influence agricultural output through multiple pathways. Auffhammer et al. (2012) found that changes in monsoon timing and intensity can reduce rice yields by up to 23 percent in major growing regions of India, while Zaveri et al. (2020) documented that rainfall variability explains approximately 20 percent of year-to-year crop yield fluctuations across India's semi-arid regions. The impact operates through several mechanisms: rainfall directly affects soil moisture content, temperature variations influence crop phenology and growing season length, and extreme weather events can cause both immediate crop damage and longer-term effects on soil quality and water availability (Ray et al., 2015). Kumar et al. (2021) demonstrated that even in years with normal total rainfall, irregular distribution during critical growth stages can reduce crop yields by 15-30 percent. Birthal et al. (2015) showed that factors such as soil organic matter content, irrigation access, and crop diversification strategies can moderate these impacts, though implementing such measures often requires substantial investment and technical capacity.

The interconnections between farm and non-farm sectors represent another crucial dimension of rural economic development. Haggblade et al. (2010) documented that agricultural growth typically generates significant multiplier effects, with each dollar of additional agricultural income generating 0.60 to 0.80 dollars in second-round income gains in rural non-farm activities. Foster and Rosenzweig (2004) showed that agricultural productivity growth creates substantial positive spillovers for rural non-farm enterprises, particularly in areas with well-developed market access. These relationships significantly influence rural household welfare and operate through various channels, including increased demand for agricultural inputs, processing services, and consumer goods. Rising agricultural incomes often translate into increased demand for locally produced non-farm goods and services (Reardon et al., 2007). Davis et al. (2017) found that regions with stronger intersectoral linkages demonstrate greater resilience to economic shocks and more inclusive patterns of growth, making this understanding crucial for policymakers designing rural development interventions.

The relationship between weather shocks and the incidence and performance of rural non-farm enterprises is a critical knowledge gap in the literature on rural economic development, particularly with regard to developing countries where the rural economy and livelihoods are highly dependent on the weather. While there is much literature on the effects of weather, particularly temperature and precipitation, on agriculture and farming, there is much less literature on the effects, or spillover impacts of these shocks on rural non-farm enterprises. In their 2014 paper, Dell, et al. cite various studies demonstrating the effects of temperature and precipitation on agricultural productivity and incomes, but they acknowledge a lack of understanding of the transmission pathways to other rural economic sectors. This knowledge gap is a particularly critical concern in light of the fact that non-farm enterprises account for from 35 percent to as high as 50 percent of rural household income in developing country contexts (Binswanger-Mkhize, 2013). In the very few studies that have been conducted, the relationships are complex. For example, Santangelo (2019) find that shocks to the productivity of agricultural activities can have widespread and consequential impacts on rural enterprises as a result of shifts in local demand and labor supply. Dercon (2014) similarly argues that identifying the wider effects of weather shocks, in addition to their impact on agricultural systems, is critical for the development of effective rural policies.

The current analysis addresses three key linkages associated with the rural economy in the state of Rajasthan. First is the impact of rainfall or weather variability on agricultural productivity wherein a farm productivity variable is constructed at the aggregate level which combines both the crop yields and the corresponding monetary values. The second is the impact of weather shocks on the non-farm enterprise in particular with respect to its total revenue, the value added by it and its distinctive operational characteristics. The third key link is how household consumption responds to agricultural productivity losses due to weather shocks, wherein this linkage is explored at the aggregate consumption level and at its individual expenditure variety. The analysis utilizes three key datasets, namely, the district-level ICRISAT database for 14 crops from 1990 to 2015, two rounds of the nationally-representative survey on unincorporated enterprises from the National Sample Survey Organisation (2010-11 and 2015-16), and the Consumer Pyramids survey datasets from the Centre for Monitoring Indian Economy (2014-2016).

This research makes several significant contributions to understanding rural economic resilience in the context of weather variability. As climate change intensifies the frequency and severity of weather shocks, understanding their comprehensive economic impacts becomes crucial for policy design. The study's findings on how weather variations affect both farm and non-farm sectors provide valuable insights for developing integrated rural development policies, particularly important for regions like Rajasthan where agricultural vulnerability to climate variability is high (Auffhammer and Carleton, 2018). By quantifying the relationships between agricultural conditions and non-farm enterprise performance, it provides evidence-based guidance for designing interventions that can enhance rural economic resilience, addressing a critical gap identified by Pingali et al. (2019) regarding the need for policies that support both agricultural adaptation and rural economic diversification.

New insights are added locally: The current study supports the existing literature on the interdependence of the rural economy with evidence on the specific channels for and magnitude of agricultural-nonagricultural linkages affected by weather shocks. Most notably, past studies ascribed this commonality to weather variables in general. The current study moves forward by examining potentially-weather dependent relationships, such as those related to agricultural economics and climate adaptation strategies. In addition, significant methodological contributions are made through the linking of multiple data sources to produce a nuanced understanding of rural economic development under climate conditions. These insights hold potential for informing climate adaptation strategies in rural economies, filling a “critical gap” identified by Barrett et al. (2017) in the need for combination strategies relying on evidence that relate solely to agricultural activities but also to climate developments in sectors engaged in non-grain-related activities. The ultimate translated goal supports the need to inform policymakers of the need to rethink the clear economic interdependence of rural activity with climactic realities.

## 2 Data and Summary Statistics

This paper combines data from three sources: namely data on non-farm enterprises based on a nationally representative enterprise survey; agricultural statistics and rainfall data from the district-level ICRISAT database; and household consumption data from a nationally representative household survey. Additional district-level covariates are sourced from the Census of India and representative household employment surveys.

## 2.1 Agricultural Productivity Data

We obtain data on district-level farm productivity and rainfall from the district-level database maintained by the International Crops Research Institute for the Semi-Arid Tropics (ICRISAT). This database contains extensive crop-wise data on acreage and output for 14 crops at the district-level, in addition to data on fertilizer usage, cultivable land, irrigation and monthly precipitation. While the data is available for a 26 year period between 1990 and 2015, we use data from 1997 to maintain consistency in the number of districts used in the analysis. $^{1}$ We use this data to construct an aggregate district-level measure for annual farm productivity. Specifically, we define FarmProd for district d and year t as:

$$
F a r m P r o d _ {d t} = \sum_ {c = 1} ^ {n} M S P _ {c t} * \frac {P r o d _ {c t}}{A r e a _ {c t}}\tag{1}
$$

In (1), c refers to the crop while Prod denotes the output, measured in thousands of tons for each crop. Area denotes the area allotted to the crop in the district for that year, measured in thousand of hectares. As we are aggregating across 14 crops, we use the federally administered minimum support price (MSP) as the crop-specific weight to convert the crop-specific yields into an uniform monetary value (scaled by area). The MSP provides the minimum price for 22 major crops in India, including both food and non-food crops. The prices are set by the federal government each year prior to the cropping season, allowing producers to know in advance the minimum price guaranteed by the government for their output. As the MSP is binding across all states and districts in India, it provides a national measure of prices which we use to convert the crop-specific yield measure into an uniform monetary value. As the MSP prices are measured as rupees per quintal, our productivity measure is scaled accordingly and measured as rupees per quintal.

Monthly data on district rainfall is also provided by ICRISAT. We aggregate the monthly data into annual data by summing monthly rainfall across all months. We use the two-decade long rainfall data for each district to obtain district-specific rainfall distributions, which we subsequently use to define positive and negative shocks for each district-year combination in Section 3.

Table 1A shows the summary statistics from the ICRISAT data. We see that $54\%$ of district area is used for agricultural activities while $20\%$ of the area in the average district is unsuited for agricultural production. On average, almost $50\%$ of a district's area under cultivation is irrigated. Over this period, a district's probability of receiving a positive rainfall shock was 0.15, and a negative rainfall shock, 0.19.

## 2.2 Non-Farm Enterprise Data

Our data on non-farm enterprises comes from two rounds of a nationally representative survey on unincorporated enterprises. These surveys are conducted by the National Sample Survey Organisation (NSS) in 2010-11, and 2010-15, and includes data from every state and district in India. The surveys are in the form of repeated cross-sections and the enterprises covered are enterprises not registered under the Companies Act of 1956. Loosely, the survey can be considered to cover informal enterprises in India.

Each survey covers in excess of 290,000 enterprises and we restrict our sample to a total of 13,000 enterprises located in the state of Rajasthan. The surveys provide enterprise weights which can be applied to make the figures representative at the national level. Based on the enterprise weights, the 2010-11 survey covered a total of 50 million enterprises and 100 million workers, reflecting approximately a fifth of the national workforce.

As our analysis is based on two survey rounds, we use the wholesale price index to inflate all monetary values to 2015-16 rupees. As we want to discern the impact of structural transformation on the performance of rural non-farm enterprises, we focus on rural enterprises in Rajasthan. This provides a final sample covering over 13,000 enterprises across the two survey rounds. The summary statistics based on this sample are presented in Table 1B. We see that the median monthly enterprise revenue is INR 15,000 (2015-16 INR), which amounts to a little over 220 USD at the prevailing nominal exchange rate. Lacking an accurate measure of enterprise profits, we instead use value-addition as a measure of profitability where value-addition is defined as revenues less operating costs. Based on this formulation, monthly value-addition is INR 5,650 or 85 USD. The median enterprise has a stock of productive capital (machinery and tools) equal to INR 7,000 or a little in excess of 100 USD.

The vast majority of the enterprises covered are own-account enterprises, implying that the owner is also the sole worker. For enterprises which hire workers, the median enterprise size is 3 workers and the median monthly wage per worker is INR 2,500 (USD 35). Most of the enterprises are owned by males and have a median age of 6 years. Only 14% of the enterprises are registered with either state or local authorities. Forty percent are trading enterprises while almost 30% are engaged in manufacturing, with the remaining operating in other service activities. Surprisingly, only 10% of the enterprises have any outstanding credit, while only 2% have any outstanding bank credit. As the second wave of the survey was undertaken in 2015-16, covering the period following the large expansion of bank accounts provided under the PMJDY scheme since 2014. $^{2}$ . This indicates that the provision of a bank account alone was possibly not sufficient to increase credit access to micro-enterprises.

Almost half the enterprises reported facing some problem in this period, mainly the lack of demand and the inability to recover financial dues. However, less than 6% mentioned facing problems due to the unavailability of electricity and less than 8% mentioned problems in accessing credit. Less than 1% of the e

[中间内容因长度限制已省略]

d>-.005(.039)</td></tr><tr><td>Observations</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td></tr><tr><td> $R^2$ </td><td>.85</td><td>.85</td><td>.85</td><td>.85</td><td>.85</td><td>.85</td></tr><tr><td>Dep Var Mean</td><td>2166.78</td><td>2166.78</td><td>2166.78</td><td>2166.78</td><td>2166.78</td><td>2166.78</td></tr></table>

Table 7: Rainfall Shock and Urban Household Expenditures

<table><tr><td></td><td>(1)</td><td>(2) Average</td><td>(3) Monthly Per</td><td>(4) Capita</td><td>(5) Expenditures (Log)</td></tr><tr><td>Positive Shock</td><td>.065(.082)</td><td>.044(.080)</td><td>.077(.079)</td><td>.073(.086)</td><td>.040(.082)</td></tr><tr><td>Positive Shock*Any Wage Labour</td><td></td><td>.054(.033)</td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Self-Employed</td><td></td><td></td><td>-.046(.053)</td><td></td><td></td></tr><tr><td>Positive Shock*Any Small Business</td><td></td><td></td><td></td><td>.007(.031)</td><td></td></tr><tr><td>Positive Shock*Any Business</td><td></td><td></td><td></td><td>-.036(.039)</td><td></td></tr><tr><td>Positive Shock*Any Informal Sector</td><td></td><td></td><td></td><td></td><td>.058*(.029)</td></tr><tr><td>Observations</td><td>18429</td><td>18429</td><td>18429</td><td>18429</td><td>18429</td></tr><tr><td> $R^2$ </td><td>.82</td><td>.82</td><td>.82</td><td>.82</td><td>.82</td></tr><tr><td>Dep Var Mean</td><td>2503.07</td><td>2503.07</td><td>2503.07</td><td>2503.07</td><td>2503.07</td></tr></table>

Table 8: Rainfall Shock and Rural Household Expenditures

<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td colspan="6">Average Monthly Per Capita Food Expenditures (Log)</td></tr><tr><td>Positive Shock</td><td>.018(.011)</td><td>.019*(.011)</td><td>-.005(.013)</td><td>.019(.012)</td><td>.018(.011)</td><td>-.008(.014)</td></tr><tr><td>Positive Shock*Any Farm</td><td></td><td>-.004(.022)</td><td></td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Wage Labour</td><td></td><td></td><td>.035**(.015)</td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Self-Employed</td><td></td><td></td><td></td><td>-.036(.027)</td><td></td><td></td></tr><tr><td>Positive Shock*Any Small Business</td><td></td><td></td><td></td><td></td><td>-.002(.034)</td><td></td></tr><tr><td>Positive Shock*Any Business</td><td></td><td></td><td></td><td></td><td>-.025(.050)</td><td></td></tr><tr><td>Positive Shock*Any Informal Sector</td><td></td><td></td><td></td><td></td><td></td><td>.039**(.015)</td></tr><tr><td>Observations</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td></tr><tr><td> $R^2$ </td><td>.89</td><td>.89</td><td>.89</td><td>.89</td><td>.89</td><td>.89</td></tr><tr><td>Dep Var Mean</td><td>1046.62</td><td>1046.62</td><td>1046.62</td><td>1046.62</td><td>1046.62</td><td>1046.62</td></tr></table>

Table 9: Rainfall Shock and Rural Household Expenditures

<table><tr><td></td><td>(1)Average</td><td>(2)Monthly</td><td>(3)Per Capita</td><td>(4)Essential Food Expenditures (Log)</td><td>(5)</td><td>(6)</td></tr><tr><td>Positive Shock</td><td>.017(.024)</td><td>.027(.026)</td><td>-.033(.023)</td><td>.018(.024)</td><td>.016(.024)</td><td>-.039(.025)</td></tr><tr><td>Positive Shock*Any Farm</td><td></td><td>-.033(.031)</td><td></td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Wage Labour</td><td></td><td></td><td>.077**(.027)</td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Self-Employed</td><td></td><td></td><td></td><td>-.037(.030)</td><td></td><td></td></tr><tr><td>Positive Shock*Any Small Business</td><td></td><td></td><td></td><td></td><td>.068(.049)</td><td></td></tr><tr><td>Positive Shock*Any Business</td><td></td><td></td><td></td><td></td><td>-.013(.049)</td><td></td></tr><tr><td>Positive Shock*Any Informal Sector</td><td></td><td></td><td></td><td></td><td></td><td>.085**(.030)</td></tr><tr><td>Observations</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td></tr><tr><td> $R^2$ </td><td>.82</td><td>.82</td><td>.82</td><td>.82</td><td>.82</td><td>.82</td></tr><tr><td>Dep Var Mean</td><td>471.23</td><td>471.23</td><td>471.23</td><td>471.23</td><td>471.23</td><td>471.23</td></tr></table>

Table 10: Rainfall Shock and Rural Household Expenditures

<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td colspan="6">Average Monthly Per Capita Luxury Expenditures (Log)</td></tr><tr><td>Positive Shock</td><td>.052***(.009)</td><td>.073***(.017)</td><td>.063**(.029)</td><td>.054***(.009)</td><td>.057***(.009)</td><td>.067*(.033)</td></tr><tr><td>Positive Shock*Any Farm</td><td></td><td>-.065(.046)</td><td></td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Wage Labour</td><td></td><td></td><td>-.017(.036)</td><td></td><td></td><td></td></tr><tr><td>Positive Shock*Any Self-Employed</td><td></td><td></td><td></td><td>-.053(.069)</td><td></td><td></td></tr><tr><td>Positive Shock*Any Small Business</td><td></td><td></td><td></td><td></td><td>-.167*(.087)</td><td></td></tr><tr><td>Positive Shock*Any Business</td><td></td><td></td><td></td><td></td><td>-.052(.087)</td><td></td></tr><tr><td>Positive Shock*Any Informal Sector</td><td></td><td></td><td></td><td></td><td></td><td>-.023(.041)</td></tr><tr><td>Observations</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td><td>7440</td></tr><tr><td> $R^2$ </td><td>.78</td><td>.78</td><td>.78</td><td>.78</td><td>.78</td><td>.78</td></tr><tr><td>Dep Var Mean</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td></tr></table>
"""
