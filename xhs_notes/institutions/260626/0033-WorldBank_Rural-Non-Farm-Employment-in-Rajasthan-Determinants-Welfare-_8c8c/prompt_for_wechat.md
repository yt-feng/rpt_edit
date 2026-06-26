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
# Rural Non-Farm Employment in Rajasthan

Determinants, Welfare Effects, and Enterprise Performance

Francis Addeah Darko

Akankshita Dey

S. K. Ritadhi

Policy Research Working Paper 11080

## Abstract

This paper examines rural non-farm employment in Rajasthan, India, using multiple surveys and administrative data. The analysis covers three key aspects: individual and district-level determinants of participation in non-farm activities, the relationship between non-farm employment and household welfare, and barriers faced by rural enterprises. The findings show that secondary education strongly predicts participation in non-farm activities, particularly in skilled service sector jobs. However, women and socially marginalized groups face significant barriers in accessing non-farm employment, especially in higher-paying occupations. Households with members in regular non-farm employment, particularly in services, show significantly higher consumption levels, while casual non-farm work yields welfare levels similar to agricultural labor. Rural enterprises face multiple constraints, with lack of local demand and limited access to credit emerging as key barriers to business performance. The results suggest that although non-farm employment can substantially improve household welfare, access to better-paying opportunities remains highly unequal. Policy interventions should ad-dress both human capital development and structural barriers to create more inclusive access to non-farm employment opportunities.

# Rural Non-Farm Employment in Rajasthan: Determinants, Welfare Effects, and Enterprise Performance

Francis Addeah Darko\*

Akankshita Dey $^{\dagger}$

S. K. Ritadhi $^{\dagger}$

JEL: J43, O17, R23  
Keywords: Non-farm employment, welfare, enterprise, rural

## 1 Introduction

Rural non-farm employment (RNFE) has emerged as a critical pathway for economic development and poverty reduction in developing countries, particularly in regions where agricultural productivity growth alone cannot sustain rising rural incomes and living standards (Haggblade et al., 2010). The structural transformation literature has long recognized that the transition from a predominantly agrarian economy to one with a more diversified rural economy is fundamental to the development process (Timmer, 2009), with several key mechanisms explaining RNFE's vital role in development. At the household level, income diversification and risk management represent primary channels through which RNFE contributes to development. RNFE provides rural households with opportunities to diversify income sources beyond agriculture, reducing vulnerability to weather shocks and crop failures (Barrett et al., 2001). This diversification is particularly valuable in contexts where formal insurance markets are underdeveloped, as non-farm income can help smooth consumption across agricultural seasons and during periods of low farm productivity (Ellis, 2000). The poverty reduction and economic mobility impacts of such diversification are well-documented, with evidence showing that households with access to non-farm income have higher consumption levels and lower poverty rates (Lanjouw and Murgai, 2009). For landless households and those with marginal landholdings, non-farm employment, particularly in salaried positions, provides higher and more stable returns compared to agricultural labor (Reardon et al., 2007).

At the macro level, RNFE plays a crucial role in rural-urban linkages and structural transformation by facilitating the development of economic connections through trade, services, and labor mobility (Tacoli, 2004). The growth of rural non-farm activities helps reduce rural-urban migration pressures by creating local employment opportunities (de Janvry and Sadoulet, 2001) while absorbing surplus agricultural labor as farming productivity increases. Furthermore, rural non-farm enterprises stimulate local economic development by generating demand for goods and services, creating multiplier effects in the rural economy (Hazell and Haggblade, 1993) and strengthening agricultural value chains through processing, transport, and marketing services. RNFE also drives important social development outcomes through multiple channels. It enhances women's economic empowerment by providing opportunities, particularly in contexts where cultural norms restrict female participation in agriculture (Kabeer, 2012), leading to greater household decision-making power and resource control. Additionally, the non-farm sector's higher skill requirements create incentives for rural households to invest in education (Foster and Rosenzweig, 2004), fostering human capital accumulation with positive intergenerational effects on poverty reduction.

However, several interrelated constraints impede RNFE development. Infrastructure and market access limitations, including poor electricity access, inadequate roads, and limited telecommunications, increase operating costs and reduce the competitiveness of rural enterprises. These physical constraints are compounded by credit constraints arising from limited collateral and underdeveloped rural financial markets, which restrict investment and growth potential. Skills and education gaps further hinder development by preventing rural workers from accessing higher-productivity non-farm employment, with the skills mismatch being particularly acute for marginalized groups. Finally, social and institutional barriers, including gender and social discrimination, along with weak governance, create additional obstacles for rural enterprises, especially those operated by women and marginalized groups.

India's rural economy has witnessed a remarkable transformation since independence, with the share of agricultural employment declining from over 80 percent in the 1950s to approximately 58 percent by 2011-12 (Thomas, 2020). This structural shift has been particularly pronounced after the economic liberalization of the 1990s, driven by rising agricultural productivity, declining farm sizes, and expanding non-farm opportunities (Binswanger-Mkhize, 2013). The pattern of this transformation has varied significantly across states, influenced by factors such as agro-climatic conditions, infrastructure development, and proximity to urban centers (Himanshu et al., 2018). While some states like Gujarat and Punjab have seen a shift towards manufacturing, others have experienced growth primarily in construction and services (Mehrotra and Parida, 2021). Within this national context, Rajasthan presents a unique case study of rural transformation, shaped by its distinct geographical, social, and economic characteristics.

Rajasthan's rural economy has undergone significant structural transformation in recent decades, characterized by a steady decline in agricultural employment and a concurrent rise in non-farm activities. This transition has been particularly notable in a state where agricultural productivity is constrained by arid conditions, with approximately 60 percent of the state's land area covered by the Thar Desert (Varghese et al., 2019). The share of agricultural employment in rural Rajasthan declined from 75 percent in the early 1980s to approximately 62 percent by 2011-12 (Joshi and Kumar, 2019). This shift reflects multiple underlying factors, including limited agricultural potential due to water scarcity, with the state receiving an average annual rainfall of only $574\mathrm{mm}$ compared to the national average of $1,186\mathrm{mm}$ (Sharma and Singh, 2021). Additionally, declining average farm sizes—from 4.1 hectares in 1970-71 to 1.8 hectares in 2015-16—have made agricultural income increasingly inadequate for sustaining rural households (Mathur and Rathore, 2020).

The growth in rural non-farm employment in Rajasthan has been notably heterogeneous across sectors, regions, and social groups. Traditional handicrafts and artisanal activities, deeply rooted in Rajasthan's cultural heritage, have emerged as significant employers, contributing approximately 12 percent to rural non-farm employment (Vyas and Mehta, 2018). Construction has shown substantial growth, particularly in regions surrounding urban centers like Jaipur, Udaipur, and Jodhpur, with its share in rural employment increasing from 4.5 percent in 1993-94 to over 15 percent by 2011-12 (Kumar and Sharma, 2020). Tourism-related activities have created significant non-farm opportunities in rural areas near heritage sites and wildlife sanctuaries, though these opportunities often exhibit seasonal variations (Rathore and Singh, 2019).

However, access to non-farm opportunities remains highly unequal. Education plays a crucial role, with workers having secondary education being three times more likely to secure regular non-farm employment compared to those with primary education only (Sharma et al., 2018). Gender disparities are particularly pronounced in Rajasthan, with female labor force participation in rural areas declining from 35 percent in 1993-94 to 28 percent in 2011-12, despite male workers' increasing movement into non-farm employment (Gaur and Joshi, 2021). This gendered trend reflects both cultural norms and limited suitable employment opportunities for women. Regional variations within Rajasthan are stark. Eastern Rajasthan, benefiting from better connectivity to Delhi-NCR and relatively better rainfall, has seen faster growth in rural non-farm employment compared to western regions (Singh and Mathur, 2022). Districts with better infrastructure and proximity to urban centers show significantly higher non-farm employment growth, with rural areas within $50\mathrm{km}$ of major cities having 40 percent higher non-farm employment rates compared to more remote regions (Sharma and Kumar, 2021). State-specific initiatives like the Rajasthan Rural Non-Farm Development Programme (RNFDP) and various tourism-based livelihood programs have attempted to address these disparities, though significant challenges remain in ensuring equitable access to quality non-farm employment opportunities.

Despite extensive research on rural non-farm employment (RNFE), significant knowledge gaps persist that limit our understanding and ability to design effective policies. These gaps span multiple dimensions of the rural non-farm sector and its role in development, particularly in how individual characteristics interact with local economic conditions. While research has separately examined the roles of education, gender, and social identity in determining access to non-farm employment (Lanjouw and Murgai, 2016), we have limited understanding of how these individual characteristics interact with district-level factors such as infrastructure, market access, and financial development. This interaction is crucial for understanding why similar individuals might experience different outcomes across locations. The operational dynamics of rural enterprises represent another critical area requiring further investigation. While we understand broad constraints facing rural enterprises, we lack detailed evidence on enterprise lifecycle dynamics, including factors determining their growth trajectories and survival rates (Banerjee and Duflo, 2014). This gap is particularly acute for informal enterprises, which constitute the majority of rural non-farm businesses but are often excluded from standard enterprise surveys. Additionally, the role of technology and digitalization in transforming rural non-farm opportunities remains understudied. While digital technologies are rapidly penetrating rural areas, we have limited understanding of how they affect non-farm employment opportunities and enterprise performance (Foster and Rosenzweig, 2022).

The human capital dimension of RNFE presents several interconnected challenges. Our understanding of skill requirements and returns to different types of skills in rural non-farm employment remains incomplete. While education's importance is well-documented, we lack detailed evidence on which specific skills are most valuable for different types of non-farm employment and how these skill requirements are evolving (Klasen, 2019). This knowledge gap extends to gender-specific challenges. While women's lower participation in non-farm employment is well-documented, we lack comprehensive understanding of how household responsibilities, social norms, and local economic conditions interact to influence women's participation decisions (Chatterjee et al., 2015). The broader economic context of RNFE also requires deeper examination, particularly regarding its relationship with agricultural transformation and migration patterns. While theoretical links between agricultural transformation and non-farm employment are well-established, empirical evidence on how changes in agricultural productivity and commercialization affect local non-farm employment opportunities remains limited (Barrett et al., 2017). Similarly, while rural-urban migration is extensively studied, we lack detailed understanding of how temporary migration affects household decisions regarding non-farm enterprise creation and employment (de Janvry and Sadoulet, 2019). Emerging challenges and policy effectiveness represent the final frontier in RNFE research. The impact of climate change on rural non-farm employment is particularly concerning. While climate change's effects on agriculture are well-studied, its implications for rural non-farm activities and their role in climate adaptation strategies remain poorly understood (Carleton and Hsiang, 2016). Furthermore, while numerous programs aim to promote rural non-farm employment, evidence on their relative effectiveness and cost-efficiency remains limited (Mansuri and Rao, 2013), hampering our ability to design and implement successful interventions.

This research addresses several interconnected questions about rural non-farm employment in India. The primary inquiry examines the determinants of rural non-farm employment by investigating how individual characteristics interact with district-level factors, with particular attention to historically understudied complementarities between personal attributes (such as education, gender, and social identity) and local economic conditions. A second key question explores whether participation in non-farm activities leads to improved household welfare, specifically focusing on consumption patterns and poverty reduction. The study also investigates the constraints faced by rural micro-enterprises, seeking to understand both the qualitative and quantitative measures of enterprise performance and the various barriers that might impede their growth. Finally, the research examines whether the historical predictors of rural non-farm employment identified in earlier periods (1999-2011) remain relevant in more recent years, utilizing contemporary data from 2015 to assess the stability and evolution of these relationships. This multi-faceted approach allows for a comprehensive understanding of both the historical patterns and contemporary dynamics of rural non-farm employment in India.

## 2 Data

This analysis uses data from five distinct sources. The historical data on individual employment and household consumption is obtained from nationally representative employment surveys (focusing on the Rajasthan component); an alternate household and individual employment survey is used to gauge the more recent relationship between individual characteristics and rural non-farm employment. The data on micro-enterprise performance is gathered from an establishment level survey of micro-enterprises. Data on bank branches and bank credit are obtained from the Basic Statistical Returns (BSR) published annually by the Reserve Bank of India; and finally, data on annual district-level rainfall is obtained from the ICRISAT's district-level database.

## 2.1 Employment-Unemployment Surveys

Our primary analysis exploits rich data collected by various rounds of the National Sample Survey Organization's (NSS) household surveys. These are nationally representative surveys conducted every 5 years, covering every state and district in India, with a sample size exceeding 80,000 households in each round. The data includes individual characteristics such as labor force participation, sector of employment, and employment type, in addition to gender, age and education levels. Household characteristics such as household location (urban or rural), landholdings, religion, caste and size are also included. Each household (individual) is accorded a weight, reflecting the inverse of the frequency of being sampled. We use the sampling weights to aggregate the individual (household) data to the level of districts and construct district-level characteristics of interest such as urbanization, and the fraction of manufacturing and public employment in the district. The latter in particular permits us to test for complementarities between individual and district characteristics.

We use four rounds of the NSS data – namely data from the “thick” rounds conducted in 1999-00, 2004-05, 2009-10 and 2010-11. $^{1}$ Since there has been a significant change in the number of districts during this period, we aggregate district boundaries corresponding to those in 1991.

## 2.2 Micro-Enterprise Survey

We consider the survey on unincorporated non-agricultural enterprises to gauge the problems faced by micro-enterprises. This is a rich dataset covering enterprises which are not registered under either the Factories Act of 1948, or the Companies Act of 1956 – the two premier law statutes which govern corporate entities in India. The enterprises by definition thus operate in the informal sector. The operation of these enterprises are of particular interest as a third of the rural non-farm labor force during the period of our study report being “self-employed” (engaged in proprietorship), while a fourth report being employed as “casual workers”. This suggests that informal small and micro-enterprises are accounting for a substantial fraction of the rural non-farm employment observed in the data.

The micro-enterprise survey is also conducted by the NSS and covers all states and districts in India, accounting for over 50 million establishments, providing employment to 100 million individuals. The survey includes data on key measures of enterprise performance such as operating expenses, raw materials, fixed capital, workers, wage payments, revenues and gross-value addition. Qualitative measures of enterprise performance such as whether the establishment is expanding, shrinking or a recent entrant, in addition to outstanding credit (and its source) are also 

[中间内容因长度限制已省略]

07* (.004)</td><td>-.057*** (.006)</td><td>-.012* (.006)</td><td>.185*** (.018)</td></tr><tr><td>Observations</td><td>387972</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td></tr><tr><td>R2</td><td>.57</td><td>.43</td><td>.43</td><td>.29</td><td>.43</td><td>.10</td><td>.15</td><td>.11</td><td>.23</td></tr><tr><td colspan="10">Panel B: Bank</td></tr><tr><td></td><td>(1) LFP</td><td>(2) Non Farm</td><td>(3) Informal Non-Farm</td><td>(4) Formal Non-Farm</td><td>(5) Labour</td><td>(6) Small Business</td><td>(7) Business</td><td>(8) Self Employed</td><td>(9) White Collar</td></tr><tr><td>Bank Account</td><td>.255*** (.012)</td><td>-.010 (.009)</td><td>-.050*** (.010)</td><td>.055*** (.006)</td><td>-.025** (.010)</td><td>.002 (.003)</td><td>.010*** (.003)</td><td>.010*** (.003)</td><td>.009*** (.003)</td></tr><tr><td>Female</td><td>-.357*** (.011)</td><td>-.045*** (.016)</td><td>-.138*** (.014)</td><td>.040*** (.009)</td><td>-.138*** (.013)</td><td>.003 (.004)</td><td>-.005 (.003)</td><td>.006 (.005)</td><td>.036*** (.005)</td></tr><tr><td>Female*Bank</td><td>-.219*** (.015)</td><td>-.027 (.017)</td><td>.052*** (.014)</td><td>-.027*** (.009)</td><td>.031** (.014)</td><td>.002 (.004)</td><td>-.010*** (.003)</td><td>-.023*** (.005)</td><td>.025*** (.006)</td></tr><tr><td>Observations</td><td>387972</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td></tr><tr><td>R2</td><td>.58</td><td>.43</td><td>.43</td><td>.29</td><td>.43</td><td>.10</td><td>.15</td><td>.11</td><td>.22</td></tr><tr><td>Dep Var Mean</td><td>.43</td><td>.47</td><td>.30</td><td>.16</td><td>.31</td><td>.02</td><td>.04</td><td>.04</td><td>.05</td></tr></table>

Notes: This table presents heterogeneity in the impact of gender on rural non-farm employment across educational attainment and access to bank accounts, using 2015 data from the Consumer Pyramids. The unit of observation is rural individuals aged between 15 and 65. With the exception of column (1), the sample is restricted to individuals participating in the labour force. Educated is a dummy equaling 1 if the individual has completed secondary or higher education; Bank is a dummy equaling 1 if the individual has a bank account. Standard errors in parentheses, clustered by district.

Table C2: Heterogeneity of Rural Non-Farm Employment for Marginalized Individuals by Education and Bank Ownership

<table><tr><td colspan="10">Panel A: Education</td></tr><tr><td></td><td>(1)LFP</td><td>(2)Non Farm</td><td>(3)Informal Non-Farm</td><td>(4)Formal Non-Farm</td><td>(5)Labour</td><td>(6)Small Business</td><td>(7)Business</td><td>(8)Self Employed</td><td>(9)White Collar</td></tr><tr><td>SC/ST</td><td>.045***(.005)</td><td>.051***(.010)</td><td>.081***(.010)</td><td>-.025***(.006)</td><td>.090***(.010)</td><td>-.013***(.003)</td><td>-.013***(.003)</td><td>-.012***(.004)</td><td>.003(.003)</td></tr><tr><td>Educated</td><td>-.036***(.005)</td><td>.062***(.006)</td><td>-.074***(.006)</td><td>.143***(.007)</td><td>-.053***(.005)</td><td>-.002(.002)</td><td>.025***(.003)</td><td>.013***(.003)</td><td>.086***(.005)</td></tr><tr><td>SC/ST*Educated</td><td>-.041***(.008)</td><td>-.011(.008)</td><td>.030***(.009)</td><td>-.041***(.008)</td><td>.023***(.008)</td><td>.004(.003)</td><td>-.022***(.004)</td><td>-.006(.004)</td><td>-.009*(.005)</td></tr><tr><td>Observations</td><td>387972</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td></tr><tr><td> $R^2$ </td><td>.57</td><td>.43</td><td>.43</td><td>.29</td><td>.43</td><td>.10</td><td>.15</td><td>.11</td><td>.22</td></tr><tr><td colspan="10">Panel B: Bank</td></tr><tr><td></td><td>(1)LFP</td><td>(2)Non Farm</td><td>(3)Informal Non-Farm</td><td>(4)Formal Non-Farm</td><td>(5)Labour</td><td>(6)Small Business</td><td>(7)Business</td><td>(8)Self Employed</td><td>(9)White Collar</td></tr><tr><td>Bank Account</td><td>.118***(.009)</td><td>-.026**(.011)</td><td>-.049***(.010)</td><td>.057***(.007)</td><td>-.028***(.010)</td><td>.000(.004)</td><td>.014***(.004)</td><td>.009**(.004)</td><td>.013***(.004)</td></tr><tr><td>SC/ST</td><td>.041***(.006)</td><td>.030**(.014)</td><td>.068***(.013)</td><td>-.023***(.008)</td><td>.077***(.014)</td><td>-.014***(.004)</td><td>-.008*(.005)</td><td>-.005(.004)</td><td>-.005(.004)</td></tr><tr><td>SC/ST*Bank</td><td>-.018***(.007)</td><td>.019(.013)</td><td>.027**(.012)</td><td>-.019**(.008)</td><td>.024*(.013)</td><td>.003(.004)</td><td>-.015***(.004)</td><td>-.010**(.004)</td><td>.004(.004)</td></tr><tr><td>Observations</td><td>387972</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td><td>167419</td></tr><tr><td> $R^2$ </td><td>.57</td><td>.43</td><td>.43</td><td>.29</td><td>.43</td><td>10</td><td>.15</td><td>.11</td><td>.22</td></tr><tr><td>Dep Var Mean</td><td>.43</td><td>.47</td><td>.30</td><td>.16</td><td>.31</td><td>.02</td><td>.04</td><td>.04</td><td>.05</td></tr></table>

Notes: This table presents heterogeneity in the impact of being a social minority on rural non-farm employment across educational attainment and access to bank accounts, using 2015 data from the Consumer Pyramids. The unit of observation is rural individuals aged between 15 and 65. With the exception of column (1), the sample is restricted to individuals participating in the labour force. Educated is a dummy equaling 1 if the individual has completed secondary or higher education; Bank is a dummy equaling 1 if the individual has a bank account. Standard errors in parentheses, clustered by district.
"""
