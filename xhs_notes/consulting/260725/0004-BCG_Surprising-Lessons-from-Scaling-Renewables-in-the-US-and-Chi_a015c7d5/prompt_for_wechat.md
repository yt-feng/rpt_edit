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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/cc24a09428b7174daa1804db9ceed1a390e4e62758480ddfbada3b28ef57f17b.jpg)

ENERGY TRANSITION

# Surprising Lessons from Scaling Renewables in the US and China

By Maurice Berns, Rina Su, Ross LaFleur, Khushboo Goel, Cédric Hazevoets, and Eden Cottee-Jones

ARTICLE APRIL 07, 2026 12 MIN READ

As global demand for electricity rises, driven in part by the rapid buildout of AI data centers, the pace of the energy transition increasingly depends on whether low-carbon power is available to meet that demand. Solar and wind energy, core technologies in the transition, have scaled rapidly in many countries over the past decade, most notably in China and the US. And yet, deployment is uneven in both nations. Some provinces and states have seen a massive ramp-up in solar and wind capacity; others have witnessed halting or stalled progress, even where the underlying resources are abundant.

This reality reveals an important but overlooked dynamic. Certainly, national energy policies are impactful, and the diverging approaches of the US and China will influence the overall trajectory of renewables in each nation in the years ahead. But the vastly different geographic concentration of solar and wind capacity across provinces and states within each country tells us that national policy is only one piece of the puzzle. Other factors also help shape how renewable buildout does or does not advance.

To understand exactly what these drivers are, we conducted an in-depth analysis of China and the US, the world's number one and number two producers of renewable energy today. We examined 70 explanatory variables related to renewable energy scale-up, drawing on more than 100,000 data points across all 50 US states and 31 Chinese provinces from 2014 to 2024. $^{1}$

What stood out most wasn't that the business case matters for scaling renewables—it was which parts of the business case matter most. Our model pinpointed empirically the specific elements that had the greatest impact in both countries. Several are especially noteworthy:

\- Cheap Land. Access to affordable land was far and away the biggest factor in both China and the US, reflecting the core role it plays in making the economics of a project work.

\- Existing Solar and Wind Capacity. We observed a definite association between a strong foundation of renewable energy in a state or province and successful scaling over our study period. This finding suggests that even regions that start from a small base can create a virtuous cycle, with early investments generating momentum that attracts further investment and growth.

\- A Robust Grid. Both the reliability of the grid and investment in utility infrastructure had a clear connection to renewable scaling. Nevertheless, the dynamics related to the grid—the foundational infrastructure for delivering renewable energy—were complex, differing in US states as compared to Chinese provinces.

By revealing the conditions that enable renewable energy to scale, these data-driven insights offer guidance for private- and public-sector players. Companies can use them to inform smarter decisions about where and how to deploy capital, and governments and regulators can draw on them to design policies that advance the deployment of low-carbon energy.

# The Renewables Story in China and the US

A close look at renewables at the province and state level reveals some surprises. $^{2}$ For example, even though China is the global leader in overall renewable energy production, the top five regions by share of electricity from renewables at the end of 2024 were US states. And both countries exhibited wide variations in renewable penetration—from less than 1% to 64% across the 50 US states and 31 Chinese provinces—with especially pronounced differences in the US. (See Exhibit 1.)

## EXHIBIT 1

The Share of Electricity from Wind and Solar Sources Within the US and China Varies Widely

Share of electricity generated from wind and solar across US states and Chinese provinces, 2024 (% of TWh)

![](images/6208c120d62c9f9de8b83e3095bc0ee5ddee91c715945b99281c0560926bce6f.jpg)  
Sources: US Energy Information Administration; National Bureau of Statistics of China; BCG Henderson Institute analysis.
Note: This analysis covers mainland China's 31 province-level regions (22 provinces, five autonomous regions, and four municipalities). Wind and solar adoption is defined as the share of electricity generated in-state or in-province from wind and solar (excluding electricity imports). TWh = terawatt-hours.

With that variability in mind, the BCG Henderson Institute created a model to tease out the factors that influence renewable energy buildout. Essentially the analysis quantifies how important specific factors were in predicting wind and solar expansion from the end of 2014 through 2024. The model does not prove that any one factor directly caused renewable scaling, but it does identify factors that are clearly associated with renewable uptake and therefore should be integrated into decision making. (See the sidebar, “Modeling Renewable Scaling.”)

## - Modeling Renewable Scaling

Our research followed a three-step process to identify key factors underlying the adoption of wind and solar energy across Chinese provinces and US states.

First, on the basis of a literature review and more than 20 expert interviews, we built a comprehensive set of hypotheses about likely drivers of renewable deployment, including legacy mix, local economy, regulatory enablers, and infrastructure maturity. Second, we gathered data across all 81 states and provinces in our study set for each hypothesis. Third, we developed and ran a model to assess the influence of those variables. We used 2014 as the baseline year and modeled the share of growth from the end of 2014 through the end of 2024 predicted by specific variables.

To improve model performance, we rigorously screened the input variables. Initially, we performed correlation analysis, applying statistical and practical tests to exclude variables with weak or inconsistent relationships. Then we assessed the significance of each variable through permutation-based importance, which quantifies each variable's explanatory power by measuring accuracy loss when values are randomly shuffled. Next, we used Recursive Feature Elimination to iteratively remove redundant or low-value variables. This step involved conducting thousands of iterations as well as applying nonlinear tree-based algorithms (specifically Random Forest, Gradient Boosting, and XGBoost) to capture the complex, nonlinear interactions inherent in renewable energy adoption. Finally, to understand each variable's impact, we used SHAP analysis, a technique that illustrates the significance and direction of each variable. Sensitivity testing further validated the robustness of our model.

We found it challenging to model a handful of variables that likely play a role in scaling renewables. For example, permitting complexity and resulting interconnection delays are well-known barriers to renewable buildout. However, given the wide range of state policies in the US and the limited availability of some permitting data in China, we were not able to build a reliable dataset on this variable, so we excluded it from the modeling.

# What Matters—and What Doesn’t—for Scaling Renewables

Examining the key drivers associated with renewable expansion reveals striking similarities between US states and Chinese provinces, along with a few notable distinctions. Some findings from our model align with intuition, but others challenge it. For instance, although access to abundant solar or wind resources matters, it isn't one of the top two factors driving growth in either the US or China. (See Exhibit 2.)

## EXHIBIT 2

The Top Drivers Influencing Wind and Solar Scaling in the US and China Are Similar

Relative importance of wind and solar adoption drivers across US states and Chinese provinces

![](images/f6716b9294711c7ed73a2f55a5d3d53e59a4a7e221aab3dab9980a1defa6e170.jpg)  
Source: BCG Henderson Institute analysis.  
Note: Drivers are listed in descending order by combined share of scaling in the US and China. All listed drivers had a positive or neutral impact on scaling except two in China: reliability of power grid and higher GDP per capita. Both of those drivers influenced the scaling of wind and solar in China in a negative direction, meaning that worse-performing local grids and lower GDP per capita were associated with higher wind and solar adoption.

## Cheap Land

The single strongest signal across both countries is the cost of rural land, which accounts for 20% to 21% of modeled growth over the period from 2014 through 2024.

During our study period, the average increase in wind and solar capacity for the ten US states with the cheapest land was 24%, versus just 9% for the ten states with the most expensive land.

Indeed, New Mexico, the state with the cheapest land, had the greatest growth in solar and wind capacity (40%). We observed similar patterns in the China data.

## Existing Renewable Capacity

The model's second-strongest signal across both countries is the presence of a preexisting base of installed wind and solar. This variable explains roughly 12% to 15% of growth over the study period—a striking indication of the positive impact of an experience curve. In China, the three provinces where solar and wind already had a 10% share of the generation mix in 2014 were among the top ten performers for capacity additions over the following decade: Gansu added a further 23%, Jilin 20%, and Inner Mongolia 14%.

This finding does not mean, however, that regions with little existing capacity realistically lack any major renewable opportunity. Instead, it implies that returns on early deployment may compound over time. Each round of buildout can improve the economics and execution of the next, creating a virtuous cycle in which regions that move earlier accelerate faster.

## A Robust Grid

Two drivers in our model capture the robustness of the grid: reliability and investment level. For investment in the grid, the story is straightforward. In both the US and China, the level of investment in utility infrastructure is clearly associated with the scale-up of renewables. The top ten US states for grid investment as a share of GDP experienced six times the rate of solar and wind capacity growth that the bottom ten states did (18% versus 3%).

With regard to grid reliability, as reflected in the frequency and duration of power outages, the story is more complex. Our model showed a clear association between reliability and scaling in US states (where it explained 14% of the buildout) and in Chinese provinces (where it explained 9%). However, the direction of that association differed. In the US, more reliable grids were associated with successful scaling over the ten-year period. In Chinese provinces, the opposite was true: less robust grids were associated with more scaling.

A closer look at the dynamics on the ground explains the seeming contradiction. The Chinese central government has encouraged renewables investment in poorer provinces by strengthening power infrastructure—not through conventional local grid upgrades, but by building high-voltage transmission lines that span hundreds of kilometers from inland provinces to coastal economic powerhouses. As a result, while local grid quality in these provinces remains limited, the high-capacity transmission network is strong, enabling electricity to be exported to distant cities and major industrial hubs.

## Growth in Power Demand

The Chinese efforts to make renewable power generated in rural locations available to faster-growing areas also helps explain another finding.

In China, the model found little connection between power demand growth and solar and wind scaling. In the US, however, the reverse is true. Growth of power demand explained 13% of renewable expansion over the study period, demonstrating that a rising load can strengthen the investment case for renewables. When demand is flat or declining, independent system operators and companies may need to retire older—yet still economically viable—assets to justify new projects. But when demand is increasing, companies can add wind and solar to meet incremental load, yielding a more attractive business case and lower overall systems costs.

## Missing Connections

The strong connections that our model identified are valuable signals. But it’s equally telling when a relationship that you might expect to be vigorous turns out to be weak—or nonexistent. Consider the role of regulatory renewables targets. Although state-level targets in the US seemed to be connected to rollout in the short term, they had no measurable impact over the long term.

We also found little connection between renewable scaling and the degree to which the state or province relied on resources from other regions inside or outside the country for power. Evidently, although energy security is a major energy transition driver at the national level, it has minimal impact at the state or provincial level.

# Insights from Two Breakout Regions

The state of Texas and China's Gansu province enjoyed robust large-scale renewable growth from 2015 through 2024. An examination of both brings the findings in our model to life. (See Exhibit 3.)

## EXHIBIT 3

Both Texas and Gansu Have Rapidly Increased Their Share of Solar-and Wind-Based Power Generation

Texas tripled its share of solar and wind in 10 years
Annual power generation, 2015–2024 (TWh) $^{1}$

Gansu's share of solar and wind doubled in 10 years
Annual power generation, 2015–2024 (TWh) $^{1}$

![](images/88ccfb085007807c31ad12ff8afe6f0465e164b246482957d8b70aa83d8f737d.jpg)  
Sources: US Energy Information Administration; National Bureau of Statistics of China; expert interviews; BCG Henderson Institute analysis. Note: TWh = terawatt-hours. Because of rounding, not all bar segment totals add up to 100%. $^{1}$ Does not include power imports.  
$^{2}$ Includes hydropower, geothermal, nuclear, biomass, and wood-derived fuels. $^{3}$ Includes natural gas, coal, and petroleum products.

## The Path to Scale in Texas

In Texas, over just a decade, wind and solar tripled their share of the state's power generation, from about $10\%$ in 2015 to roughly $30\%$ in 2024. Four key findings in our model played significant roles in the buildout.

First, our analysis identified demand growth as an important driver in the US—and it was certainly a factor in Texas, with total power generation climbing from around 450 terawatt-hours (TWh) to nearly 570 TWh. Second, access to low-cost land underpinned the scale-up of renewables in Texas. Third, in many places that affordable land boasted some of the country’s strongest and most consistent wind or ranked among the sunniest places in the US. Fourth, the state government prioritized development of grid infrastructure: Texas proactively invested in 3,600 miles of high-voltage transmission lines to connect designated Competitive Renewable Energy Zones in resource-rich, remote parts of the state to regions with high electricity demand. This buildout of transmission infrastructure, along with the state’s deregulated market structure, helped incentivize developers to invest in new generation capacity.

## Building on Advantage in Gansu

For its part, the Chinese province of Gansu posted the nation's second-highest growth in renewables capacity from 2015 through 2024, despite having only average solar and wind resources in comparison to other Chinese provinces. Scrutiny of the buildout brings three factors to the forefront.

First, the province already had a strong base of existing wind power, most notably in the form of the Jiuquan wind power base, one of the largest wind farms in the world. This made Gansu, with its well-established supply chains, local know-how in the construction sector, and proven business case, appealing for future investors. Second, Gansu province has the fourth-lowest land prices in China—one-sixth the national average. Third, even though there is little local demand, the province has directed major investment toward infrastructure, ranking it in the top six provinces in terms of share of GDP spent on utilities.

Understanding the elements of the business case that have an outsize impact on how renewables scale is a critical first step. From there, companies and governments should examine how those factors intersect with their own plans and efforts.

For companies, insights from the model can help formulate the right questions to ask about future investments and identify steps to strengthen the business case. For instance, which regions have affordable land and an ecosystem of experienced renewable players to drive efficient development? What can companies do to ensure access to reliable grid infrastructure when needed? And where is the strongest growth in demand likely to occur?

For policymakers who want to attract investment in renewables, the most critical questions center on which measures can help reduce the land costs for renewable developers and which proactive strategies pursued today can attract the transmission investment required to transmit solar and wind power tomorrow.

Policymakers and companies can also explore how to partner to improve the overall economics of renewable scaling. When public-sector actions create the conditions for viable projects—and private capital responds with scale, execution, and expertise—renewable deployment accelerates.

The authors thank Jamie Webster, Lars Holm, and Grace Keliher for their assistance in the research for this article.

The BCG Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and

experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors

![](images/ff383a761309b4127aa1ca8d0410109eabb867d30be0e28ca7841143ff54e145.jpg)

![](images/f132caa91c12d626d69098ee646795eab6673b401d5b0410dc8822907b721731.jpg)  
Maurice Berns  
Managing Director & Senior Partner; Chair, Center for Energy Impact
London

![](images/f22f125d48e99360b8d87af740947eda644df71951a213d69950afe58e7b621f.jpg)

![](images/452eda54035b6724c5175e45a9b7a976ffd72e012f74abe670e3f83628060a99.jpg)

![](images/47b1cba831838b8a5f9e8ee407b7a12aacd512fd5644b1e41475feefcd0e598c.jpg)  
Managing Director & Partner
Beijing  
Rina Su

![](images/9d05057c22811ff40a0d2c3c0f644c7ab408cc059eec3bb7d4d67f5c46070427.jpg)

## Ross LaFleur

Managing Director & Senior Partner
Dallas

Cédric Hazevoets

![](images/d93364ac55fac24df69402247aa014a36555107d43c6f284820b008f7e9f209b.jpg)  
Alumnus

![](images/29b286ce16fdaeeebaf9d4a70e19f50f5e013946ca48e357e03609828e7714a2.jpg)

## Khushboo Goel

![](images/a60fb95f9351d53980218e7c131fb36219ab53758418c8e0d75d07bb1fae4ffb.jpg)  
Partner
New York

![](images/dda242462540c95059f75253bfbc46be95c2beeaf852c05d340728415ecf862c.jpg)

![](images/16a1450b4a7eac9015be607e1d8bfae4665a670ba2843dafedea5f79231262d1.jpg)

![](images/91f798bcd0575e68c519700109277d218652e410bd3e28089952705dfa431177.jpg)  
BCG Institute Senior Director
London Canary Wharf

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

renewables refers exclusively to solar and wind.
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
