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
Policy Research Working Paper

11081

# Firm-Level Climate Change Adaptation Micro Evidence from 134 Nations

Claudia Berg

Luca Bettarelli

Davide Furceri

Michael Ganslmeier

Arti Grover

Megan Lang

Marc Schiffbauer

![](images/0e83253dee83b116cd666559c6f6cca3e51fca18cf8ebaec678ceea4e4fa6e9d.jpg)

WORLD BANK GROUP

POLICY RESEARCH WORKING PAPER 11081

## Abstract

Are firms adapting to climate change? This paper studies this question by combining geocoded World Bank Enterprise Survey data with spatially granular weather data to estimate temperature response functions for nearly 160,000 firms in 134 countries over a 15-year period. Our results show that market imperfections in low- and middle-income countries constrain firms' ability to adapt. Small and medium-size firms in low- and low-middle income countries are most vulnerable, with revenues declining by 12 percent in years with temperatures $0.5^{\circ}$ C above historical averages. The impact is equally strong for manufacturing and services firms and result from declines in labor productivity and wages. Heat-sensitive sectors and less resilient firms are more severely affected, reinforcing the causal interpretation. Unique firm-level information on policy constraints including limited financing, burdensome regulations, and unsafe conditions suggest that such factors raise adaptation costs, undermining economic resilience to climate change.

# Firm-Level Climate Change Adaptation: Micro Evidence from 134 Nations

Claudia Berg $^{1}$ , Luca Bettarelli $^{2}$ , Davide Furceri $^{3}$ , Michael Ganslmeier $^{4}$ , Arti Grover $^{5}$ , Megan Lang $^{1}$ , and Marc Schiffbauer $^{1}$

$^{1}$ 1: World Bank, 2: University of Palermo, 3: International Monetary Fund, 4: University of Exeter, 5: IFC

KEYWORDS: CLIMATE ADAPTATION, FIRMS, TEMPERATURE, RESILIENCE
JEL CODES: D22, Q56, Q54, O12, O14
©2024 The World Bank and International Monetary Fund.

## 1 Introduction

Empirical studies have documented a robust association between extreme weather and reductions in national economic growth (e.g., Burke, Solomon M Hsiang, and Miguel 2015, Somanathan et al. 2021). Extreme weather may reduce economic activity by affecting the performance of firms. Economic theory predicts that rational, forward-looking firms should make self-protective investments. However, firms operating in low- and middle-income countries face a host of market imperfections that may constrain their ability to adapt. Understanding which types of firms are best able to cope with weather shocks and which features of the business environment support firm-level adaptation is critical for designing well-targeted policies for private sector climate resilience.

To this end, we combine granular satellite weather data with global firm-level data to study the impact of rising temperatures on firms' performance, ability to adapt, and the policy constraints hindering their adaptation capacity. We use standardized, repeated cross-sectional microdata from the World Bank's Enterprise Survey (WBES, Enterprise Survey 2023) covering 134 countries and more than 160,000 firms—of which more than half operate in low and low-middle income countries—over a 15-year period. We assess the marginal effect of weather deviations from historical trends on corporate revenues and the associated transmission channels such as firmsâ investments, labor productivity, wages, energy intensity, and propensity to innovate. The data also enable us to estimate how firmsâ characteristics and the policy constraints they encounter influence their capacity to adapt to higher temperatures.

This study is among the first to use granular satellite weather data combined with microeconomic data to assess the economic impact of climate change at a global scale, particularly in low- and middle-income countries. The integration of granular climate and firm-level data is critical for identifying the causal economic effects of temperature shocks as it enables us to measure temperature deviations at firmsâ specific locations and account for firm-level heterogeneities, addressing key endogeneity concerns. Our empirical strategy relies on computing location-specific differences between temperatures within firms' fiscal year and historical average temperatures from 1980–2008. We use these temperature differences to estimate heterogeneous, nonlinear firm responses along multiple dimensions of firm performance. Our identifying assumption is that temperature deviations are as good as random after conditioning on country by sector by year fixed effects, firm size (a general proxy for firm quality), and firms' location-specific historical mean temperatures.

Another novel feature of our study is that the standardized firm-level data include manufacturing and services firms, as well as a rich set of firm-level characteristics and measures of the business environment. For instance, it includes measures of firms' main sales markets, the resilience of firms' production processes, firms' access to finance, the quality of electricity services, the level of local security and political stability, and the quality of the local regulatory environment. Interacting these measures with location-specific weather data allows us to describe which types of firms and policy reforms are best able to “weather the storm”.

We document large, negative impacts of higher-than-average temperatures on revenues for firms in low and low-middle income countries. Small and medium-size firms as well as startups are most vulnerable to rising temperatures. These firms exhibit a 12% decline in revenues when annual average temperatures are $0.5^{\circ}$ C higher than the historical average. The impact is equally significant for manufacturing and services firms and driven by declines in labor productivity, which also result in lower wages. Firms in heat-sensitive sectors and with less resilient production processes are more affected, supporting our empirical identification. Consistent with the findings in Carleton et al. (2022), we find that income significantly flattens the temperature-revenue curve. In low and low-middle income countries, firms facing limited access to finance, burdensome local business regulations, and unsafe conditions are more vulnerable to temperature increases, weakening economies' resilience to climate change.

Taken together, our results highlight two novel facts about economic resilience to rising heat. First, the performances of most manufacturing and services firms in low- and low-middle income countries has been affected by rising temperatures, with substantial differences in the degree of vulnerabilities depending on firms' specific characteristics. Second, local policy constraints including finance, business regulation, and the quality of public goods affect firms' adaptive capacity, undermining developing countries' economic resilience. Our results underline the importance of designing local context-specific policies to support climate adaptation in the private sector.

## 2 Literature

In the last decades, deteriorating climate conditions have encouraged scholars to investigate the economic costs of climate change. Studies find that increasing average temperatures by 1°C reduces global output and productivity by about 1-3% in hot regions (Nordhaus, 2006; Stern 2008; Bansal and Ochoa 2011; Graff Zivin and Neidell 2012). In contrast, cold countries may benefit from warmer temperatures (Tol, 2021). Along this line, Burke, Solomon M Hsiang, and Miguel (2015) present evidence that the productivity of countries increases along with temperatures until an annual average threshold of 13°C, with countries' productivity declining significantly at higher temperatures. As hotter regions are on average poorer, climate change is also expected to hit developing regions harder (Dell, Jones, and Olken 2012; Letta, Montalbano, and R. Tol 2018; Newell, Prest, and Sexton 2021). In fact, many developing nations face greater natural disaster risks such as typhoons and are exposed to extreme heat and precipitation (Bakkensen and Barrage 2018; Solomon M. Hsiang and Jina 2018). Moreover, climate risks in the developing world are amplified by weak governance capacity (Acemoglu and Robinson 2013; La Porta, Lopez-de-Silanes, and Shleifer 2008; Allcott, Collard-Wexler, and D. O'Connell 2016; Chong et al. 2014).

A recent study by Bilal and Kanzig (2024) suggests that previous evidence based on country-level temperature data could underestimate the real effect of climate on the economy. The authors propose the use of aggregate global temperature—as it accounts for correlated local temperatures and spillover effects across countries—and find that the peak effect of warming temperatures reduces economic activity by about 12% in the medium term, approximately twelve times larger than what was previously estimated.

While these studies provide important insights, the reliance on cross-country data does not allow to adequately address institutional and other differences across countries that matter for the economic impact of climate change but are typically unobservable, raising endogeneity concerns (see, for example, Durlauf, Johnson, and Temple 2009; Hauk and Wacziarg 2009). Cross-country data also neglect subnational variation in (the impact of) climate change which has been found to be substantial (Bettarelli et al. 2024).

Recent literature has extended the level of granularity of analyses to the sub-national level, leading to more accurate estimates. Kotz, Levermann, and Wenz (2024) use a sample of 1,600 regions worldwide over the past 40 years to project sub-national damages from temperature and precipitation, including daily variability and extremes. They suggest a reduction in global output of 19% by 2050, compared to a scenario without climate impact. Burke and Tanutama (2019) assemble panel data on economic output from over 11,000 districts across 37 countries and find that district-level growth declines for higher average temperatures. Carleton et al. (2022) use subnational data from 40 countries to investigate the age-specific mortality-temperature relationships and suggest a nonlinear effect, whereby extreme cold and hot temperatures increase mortality rates.

We contribute to this literature by using more granular spatial data combined with firm-level information. The more granular spatial data can help address endogeneity concerns since the effect of climate change can vary at a very granular spatial level such as within provinces or districts due to correlations of local geographies with climate and economic activity—more districts with higher elevations, for example, typically have lower average temperatures and economic activity while coastlines have milder climates and higher activity. Moreover, firm-level data allow assessing how the impact of climate change differs across firms given their ability to adapt. Young or small firms, for example, often face tighter financial constraints or higher costs to access construction permits needed to invest into more resilient buildings.

At the firm-level, Somanathan et al. (2021) find that rising heat days in India between

1998 and 2010 have reduced formal manufacturing firms' revenues by about $2\%$ per year. Severe reductions in manufacturing output due to extreme heat have also been documented among Chinese plants (Zhang et al. 2018) and at the global level (N. Pankratz, Bauer, and Derwall 2023). For the U.S., Addoum, Ng, and Ortiz-Bobea (2020) find no significant impact of temperature exposure on establishment-level sales or productivity using granular climate data from 1990 to 2015. Beyond temperatures, Keiller and Van Reenen (2024) demonstrate that natural disasters adversely affect firm performance. Cevik and Miryugin (2022) find that firms in more climate vulnerable countries have a lower profitability and access to debt financing. A detrimental impact of climate risks on the firm's financial position is also documented by Venturini (2022), Bansal, Ochoa, and Kiku (2016), Addoum, Ng, and Ortiz-Bobea 2020, and N. Pankratz, Bauer, and Derwall (2023). Huang, Kerstein, and Wang (2018) find that the impact of climate risks on firms is larger in climate vulnerable sectors such as food, healthcare, communications, business services, or transportation. Recent studies also use transcripts from conference calls to quantify the degree of exposure of firms to different climate risks and link it with firm-level outcomes (Li et al. 2020; Sautner et al. 2023). These single-country studies carefully identify local marginal effects but are unable to sketch out the cross-sectional gradient of how firms worldwide are coping with similar shocks.

Several studies also use survey data to measure how rising heat affects labor productivity. Somanathan et al. (2021) collect high-frequency survey data in India. They document that an additional day above $35^{\circ}$ C in the six preceding days has caused a 2.7% decrease in daily output among textile workers in sites without climate control while worker efficiency has still declined by 1.1% in climate-controlled garment plants. The latter stems from absenteeism, with each heat day raising worker absenteeism by 0.5% and reducing output by 1.4%. Similarly, Graff Zivin and Neidell (2014) find that extreme heat reduces hours worked in heat-sensitive industries in the U.S. Adhvaryu, Kala, and Nyshadham (2020) exploit differences in temperatures across workplaces within the same factory in India due to selected use of lighting technology—low heat-emitting LED bulbs—and find large adverse efficiency effects for indoor temperatures above 28 $^{\circ}$ C. Rode et al. (2022) use data from several large economies to show that increasing temperature impacts on workers disutility. And Park, N. Pankratz, and Behrer (2024) find that temperatures above 32 $^{\circ}$ C in California, U.S., have increased workplace injuries in construction, indoor manufacturing, and warehousing by 9%.

Rising temperatures have also been estimated to raise firms' input costs. N. M. C. Pankratz and Schiller (2022) find that exposures to high temperatures at supplier locations in a sample of large multinational firms reduce downstream firms operating income over assets by 0.6%. Using plant-level data from the U.S. Census Bureau, Ponticelli, Xu, and Zeume (2023) find that warmer than average temperatures increase energy costs and decrease productivity in small manufacturing plants (see also Birkie, Trucco, and Campos 2017; Cevik and Miryugin 2022). Moreover, the World Bank (2004) estimates that rising energy demand from additional cooling needs in commercial buildings rises 11-fold by 2037 implying surging energy costs for firms.

Our work also links to studies investigating strategies to adapt/respond to climate risks (Burke, Zahid, et al. 2024). Risk reduction is generally pursued through technical measures such as maintenance, materials, facilities, assets and process engineering, risk monitoring and assessment (Berkhout 2012; Hertin et al. 2003; Weinhofer and Busch 2013), or by adopting establishment-level climate controls (Gasbarro and Pinkse 2016; Somanathan et al. 2021; Zhao et al., 2024). Moreover, infrastructure investments such as new roads, sea walls, bridges, water treatment facilities, or power generation plants support firms to cope with climate risks (Hallegatte, Rentschler, and Rozenberg 2019; Hsiao 2023; He et al. 2021). Bettarelli et al. (2024) show that firms facing financial constraints are more exposed to climate uncertainty.

We contribute to the literature by combining highly granular climate data with firm-level data from nearly 160,000 firms in 134 countries from 2006 to 2023 to estimate the economic costs of increasing temperatures at the global level. It is thus one of the first studies to use, at a global scale, granular Satellite weather data combined with rich firm-level data, which is key to address endogeneity concerns. The paper most similar to ours is Kassa and

Woldemichael (2024) who also use global WBES data to analyze the effect of heat on firm productivity, finding larger impacts in large firms, manufacturing, and low-income countries. In contrast to previous studies, we make four major contributions. First, we allow for non-linear temperature response functions and model heterogeneities in country or firm typologies and temperature levels. Second, we assess the impact of yearly deviations of temperatures from locations' long-term trends and its transmission channels such as investment, labor productivity, labor compensation, or energy costs. Third, we assess which types of firms are more exposed to climate change / less able to adapt accounting for firm characteristics, such as firms' size, age, main sales market, resilience, and economic activity. Fourth, we assess how policy failures raise firms' transaction costs to investment in adaptation—including access to finance, security, and business regulations—which is key to design effective policies supporting economic resilience.

## 3 Firm Choices: Location and Adaptation Investments

The impact of local weather on a firm's performance depends on where the firm locates and what self-protective measures it takes. Some firms may choose to gamble by investing little in self-protection while others may incur significant costs, for instance purchasing backup power generators or investing in redundant supply chains. In this section, we discuss the joint decision made by firms concerning where to locate and how much to invest in self-protection. As we discuss below, our empirical work focuses on the set of firms who are operating in a given location at a given point in time.

Within a country, locations differ along many dimensions. Some locations may be close to final consumers while other locations may be close to export ports. Given that firms and workers compete for scarce land, the hedonic compensating differentials literature predicts that areas with productive features will have higher rents and higher wages in equilibrium, while other areas will feature lower wages and higher rents.

Each firm knows its own production function and calculates its expected profit in each location. The site selection literature models firms as if they calculate their expected flow profits at each discrete location and then choose the location that offers the highest expected present discounted value of profits. Conditional on selecting a location, the firm has an incentive to make customized investments to self-protect from expected weather realizations. For example, a firm that locates close to the equator will anticipate th

[中间内容因长度限制已省略]

<td>1.013</td><td>-0.422</td><td>26.527</td><td>1.350</td></tr><tr><td>Lebanon</td><td>17.308</td><td>1.927</td><td>-0.475</td><td>0.327</td><td>-0.176</td></tr><tr><td>Lesotho</td><td>13.693</td><td>0.524</td><td>-0.605</td><td>0.000</td><td>-0.138</td></tr><tr><td>Mauritania</td><td>23.339</td><td>0.257</td><td>0.228</td><td>25.247</td><td>7.349</td></tr><tr><td>Mongolia</td><td>-0.412</td><td>1.592</td><td>0.446</td><td>0.303</td><td>-0.181</td></tr><tr><td>Morocco</td><td>18.220</td><td>1.523</td><td>0.072</td><td>23.151</td><td>10.834</td></tr><tr><td>Myanmar</td><td>26.815</td><td>0.862</td><td>0.077</td><td>86.675</td><td>10.318</td></tr><tr><td>Nepal</td><td>20.467</td><td>0.598</td><td>0.426</td><td>23.168</td><td>3.016</td></tr><tr><td>Nicaragua</td><td>26.765</td><td>0.868</td><td>0.157</td><td>56.045</td><td>14.374</td></tr><tr><td>Nigeria</td><td>26.642</td><td>0.578</td><td>-0.107</td><td>75.821</td><td>3.360</td></tr><tr><td>Pakistan</td><td>22.973</td><td>0.944</td><td>-0.030</td><td>98.888</td><td>18.077</td></tr><tr><td>Papua New Guinea</td><td>24.867</td><td>0.309</td><td>0.267</td><td>0.000</td><td>0.000</td></tr><tr><td>Philippines</td><td>26.727</td><td>0.734</td><td>-0.132</td><td>3.011</td><td>1.014</td></tr><tr><td>Samoa</td><td>25.957</td><td>0.083</td><td>0.035</td><td>0.000</td><td>0.000</td></tr><tr><td>Senegal</td><td>24.855</td><td>0.064</td><td>0.326</td><td>30.705</td><td>5.042</td></tr><tr><td>Solomon Is.</td><td>24.447</td><td>0.448</td><td>0.146</td><td>0.000</td><td>0.000</td></tr><tr><td>Tajikistan</td><td>13.115</td><td>1.728</td><td>-0.433</td><td>26.219</td><td>10.284</td></tr><tr><td>Tanzania</td><td>23.265</td><td>0.671</td><td>0.198</td><td>0.245</td><td>0.159</td></tr><tr><td>Timor-Leste</td><td>25.297</td><td>0.992</td><td>-0.039</td><td>0.000</td><td>0.000</td></tr><tr><td>Tunisia</td><td>18.953</td><td>0.991</td><td>0.028</td><td>19.587</td><td>-1.872</td></tr><tr><td>Ukraine</td><td>8.473</td><td>1.936</td><td>0.471</td><td>0.302</td><td>-0.214</td></tr><tr><td>Uzbekistan</td><td>13.930</td><td>1.125</td><td>0.006</td><td>45.213</td><td>11.234</td></tr><tr><td>Vietnam</td><td>25.326</td><td>0.645</td><td>-0.137</td><td>12.750</td><td>-2.177</td></tr><tr><td>Zambia</td><td>21.241</td><td>0.761</td><td>0.077</td><td>11.278</td><td>6.952</td></tr><tr><td>Zimbabwe</td><td>18.963</td><td>1.209</td><td>0.600</td><td>4.663</td><td>4.139</td></tr></table>

Table A6: Temperature and Hot Days Data for Lower Middle Income Countries

<table><tr><td rowspan="2">Country</td><td colspan="4">Temperature</td><td colspan="2">Hot Days</td></tr><tr><td>Long-Term</td><td>Deviation</td><td>Mean</td><td>Deviation SD</td><td>Mean</td><td>Deviation</td></tr><tr><td>Afghanistan</td><td>15.373</td><td></td><td>0.434</td><td>0.109</td><td>51.705</td><td>4.887</td></tr><tr><td>Burundi</td><td>21.387</td><td></td><td>0.896</td><td>-0.046</td><td>0.000</td><td>-0.069</td></tr><tr><td>Central African Republic</td><td>25.670</td><td></td><td>0.812</td><td>0.085</td><td>60.250</td><td>33.420</td></tr><tr><td>Chad</td><td>28.403</td><td></td><td>0.287</td><td>0.078</td><td>183.195</td><td>-2.202</td></tr><tr><td>Congo, Dem. Rep.</td><td>22.990</td><td></td><td>0.519</td><td>0.049</td><td>0.707</td><td>0.485</td></tr><tr><td>Ethiopia</td><td>16.810</td><td></td><td>1.341</td><td>0.206</td><td>2.006</td><td>0.456</td></tr><tr><td>Gambia, The</td><td>25.352</td><td></td><td>0.787</td><td>-0.074</td><td>4.747</td><td>1.377</td></tr><tr><td>Liberia</td><td>25.522</td><td></td><td>0.833</td><td>0.019</td><td>0.808</td><td>0.497</td></tr><tr><td>Madagascar</td><td>20.925</td><td></td><td>0.790</td><td>0.270</td><td>0.649</td><td>0.419</td></tr><tr><td>Malawi</td><td>21.141</td><td></td><td>0.560</td><td>0.073</td><td>2.574</td><td>1.825</td></tr><tr><td>Mali</td><td>27.722</td><td></td><td>0.723</td><td>0.415</td><td>125.849</td><td>-0.309</td></tr><tr><td>Mozambique</td><td>23.579</td><td></td><td>0.449</td><td>-0.138</td><td>8.972</td><td>0.106</td></tr><tr><td>Niger</td><td>28.853</td><td></td><td>1.013</td><td>-0.317</td><td>196.775</td><td>-1.854</td></tr><tr><td>Rwanda</td><td>21.038</td><td></td><td>1.104</td><td>0.261</td><td>0.346</td><td>-0.153</td></tr><tr><td>Sierra Leone</td><td>25.860</td><td></td><td>0.775</td><td>0.075</td><td>24.359</td><td>8.953</td></tr><tr><td>South Sudan</td><td>26.148</td><td></td><td>0.921</td><td>0.234</td><td>74.939</td><td>18.017</td></tr><tr><td>Sudan</td><td>29.259</td><td></td><td>1.020</td><td>0.010</td><td>199.000</td><td>-28.655</td></tr><tr><td>Togo</td><td>26.544</td><td></td><td>0.640</td><td>0.076</td><td>4.054</td><td>0.874</td></tr><tr><td>Uganda</td><td>21.512</td><td></td><td>0.578</td><td>0.123</td><td>0.550</td><td>-0.036</td></tr><tr><td>Yemen, Rep.</td><td>22.581</td><td></td><td>0.953</td><td>0.011</td><td>35.133</td><td>3.764</td></tr></table>

Table A7: Temperature and Hot Days Data for Low Income Countries

<table><tr><td></td><td>Pooled</td><td>Pre 2017</td><td>Post 2017</td><td>High Hist. CV</td><td>Low Hist. CV</td><td>Small</td><td>Medium</td><td>Large</td></tr><tr><td colspan="9">Panel A: Low-Income Countries</td></tr><tr><td>CV</td><td>-0.122(0.046)</td><td>-0.128(0.052)</td><td>-0.147(0.056)</td><td>-0.176(0.070)</td><td>-0.098(0.090)</td><td>-0.068(0.041)</td><td>-0.136(0.059)</td><td>0.113(0.096)</td></tr><tr><td colspan="9">Panel B: Middle and High-Income Countries</td></tr><tr><td>CV</td><td>-0.070(0.034)</td><td>0.108(0.071)</td><td>-0.113(0.036)</td><td>-0.063(0.034)</td><td>-0.166(0.228)</td><td>-0.034(0.041)</td><td>-0.136(0.059)</td><td>0.113(0.096)</td></tr></table>

Table A8: Regression Results using Coefficient of Variation
"""
