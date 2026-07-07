你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
ECONOMIC POLICY UNCERTAINTY
AND CARBON EMISSIONS
IN EMERGING MARKETS

Nuobu Renzhi, John Beirne, and Le Ngoc Dang

NO. 854

July 2026

ADB ECONOMICS

WORKING PAPER SERIES

# Economic Policy Uncertainty and Carbon Emissions in Emerging Markets

Nuobu Renzhi, John Beirne, and Le Ngoc Dang

No. 854 | July 2026

The ADB Economics Working Paper Series presents research in progress to elicit comments and encourage debate on development issues in Asia and the Pacific. The views expressed are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent.

Nuobu Renzhi (renzhinuobu@gmail.com) is an assistant professor and assistant dean at the School of Economics, Capital University of Economics and Business, Beijing. John Beirne (jbeirne@adb.org) is a principal economist at the Economic Research and Development Impact Department, Asian Development Bank. Le Ngoc Dang (ngoc.dangle@hvtc.edu.vn) is a lecturer at the Academy of Finance, Ha Noi.

© 2026 Asian Development Bank
6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines
Tel +63 2 8632 4444; Fax +63 2 8636 2444
www.adb.org

Some rights reserved. Published in 2026.

ISSN 2313-6537 (print), 2313-6545 (PDF)

Publication Stock No. WPS260312-2

DOI: http://dx.doi.org/10.22617/WPS260312-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## Note:

ADB recognizes “China” as the People’s Republic of China.

## ABSTRACT

This paper empirically examines the impact of economic policy uncertainty (EPU) on carbon emissions in 13 emerging market economies (EMEs), using panel local projections over the period 1990 to 2023. The results indicate that rising EPU significantly increases carbon emissions. However, the impact varies across economic and institutional characteristics. Specifically, EMEs with lower initial carbon emissions, higher energy intensity, carbon pricing mechanisms, greater financial development, higher trade openness, stronger political stability, greater renewable energy reliance, and higher research and development intensity exhibit a weaker response to EPU. Moreover, high-income EMEs experience a muted response in emissions, whereas lower-income EMEs face a more pronounced impact. Additionally, EMEs with low climate vulnerability see a stronger positive response in emissions compared to their high-vulnerability counterparts. These findings highlight the critical role of institutional and structural factors in shaping the emissions response to EPU, offering important policy insights for mitigating environmental risks in uncertain economic conditions.

Keywords: economic policy uncertainty, carbon emissions, emerging market economies

JEL codes: O13, Q54, Q58

## I. INTRODUCTION

Economic policy uncertainty (EPU) has become an increasingly significant concern in recent years, particularly in emerging market economies (EMEs), where fluctuations in policy uncertainty can substantially affect macroeconomic outcomes (Baker, Bloom, and Davis 2016). While much of the existing literature has focused on the effects of EPU on economic growth, investment, and financial markets, its impact on environmental outcomes, particularly carbon emissions, remains underexplored. Given that EMEs now account for around 60% of global carbon emissions (based on data from the 2024 Global Carbon Project), it is crucial to understand how EPU influences carbon emissions in these economies given that they play a central role in global efforts to mitigate climate change.

Our paper is motivated by the observation that EPU can affect a wide range of economic decisions and outcomes. Given the connection between economic activity, energy use, and environmental performance, EPU may be related to carbon emissions, a fact that warrants empirical examination. Broadly, policy uncertainty influences firms' financial decisions, investment strategies, and consumer behavior, all of which affect energy consumption and carbon emissions. Despite growing attention to the relationship between EPU and carbon emissions, there remains limited empirical evidence on the dynamic impacts of EPU on emissions, particularly from the perspective of EMEs. This paper aims to fill this gap in the literature by employing panel local projections (Jordà 2005) to estimate the impulse responses of carbon emissions to changes in EPU across 13 EMEs from 1990 to 2023, while also identifying the institutional and structural factors that shape the impact of EPU. By examining how economic and institutional characteristics affect the emissions response, this paper seeks to offer more granular insights into the relationship between policy uncertainty and environmental outcomes.

Conceptually, EPU can influence carbon emissions through several mechanisms. Earlier studies have shown that heightened policy uncertainty discourages investment, delays production decisions, and reduces aggregate economic activity (Bloom, 2009). Under this mechanism, lower output and energy demand would be expected to reduce carbon emissions. However, this perspective assumes that uncertainty primarily affects the volume of economic activity as opposed to altering the composition of investment or the pace of economic adjustment.

Policy uncertainty could also slow the transition toward a low-carbon economy through its effects on the composition and timing of investment rather than solely its overall level. Investments in renewable energy, energy efficiency, and clean technologies typically involve high upfront costs, long payback periods, and dependence on stable policy environments. Under heightened uncertainty, firms may postpone replacing existing carbon-intensive capital or defer investments in cleaner technologies, prolonging reliance on more emissions-intensive production processes (e.g. Yu et al., 2025). Governments could also delay environmental regulations or public investment in green infrastructure, further slowing structural decarbonization. While the empirical analysis in this paper does not directly disentangle the contractionary effect on economic activity from the effect of slower structural adjustment, the results should be interpreted as reduced-form evidence of the net impact of EPU on emissions.

Our baseline results indicate that carbon emissions increase significantly following a rise in EPU. Specifically, a 1-standard deviation increase in EPU leads to a maximum increase of 0.03% in carbon emissions. This finding aligns with the broader literature, which has identified a positive relationship between EPU and carbon emissions (e.g., Benlemlih and Yavaş 2024, Chiou et al. 2025). These baseline estimates serve as a key benchmark for analyzing heterogeneous effects conditioned on various economic and institutional factors. Additionally, we find our results are robust to a range of sensitivity checks, including alternative model specifications and the inclusion of additional controls.

Importantly, we observe significant heterogeneity in the response to EPU across different economies, with the magnitude and persistence of the impact varying depending on each economy's structural and institutional characteristics. Specifically, economies with lower initial carbon emissions, higher income, higher energy intensity, carbon pricing mechanisms, greater financial development, higher trade openness, stronger political stability, greater reliance on renewable energy, and higher research and development (R&D) intensity tend to exhibit a weaker response to EPU. This suggests these economies may be better equipped to manage the adverse environmental impacts of EPU. Furthermore, we find the effects of EPU on carbon emissions also vary by income level: high-income EMEs experience a weaker response in emissions, whereas low-income EMEs face a more persistent and pronounced effect. This highlights the vulnerability of lower-income economies to policy-induced environmental changes. In addition, we observe that EMEs with lower climate vulnerability show a stronger positive response to EPU, in contrast to those with higher climate vulnerability, which may face more severe challenges in balancing economic and environmental priorities.

Our findings underscore the importance of considering structural and institutional factors when assessing the effects of EPU on environmental outcomes. The heterogeneity observed in the responses to EPU emphasizes the critical role of these factors in shaping the emissions trajectory in EMEs. As such, policymakers in EMEs need to account for their specific institutional and structural characteristics when designing policies to mitigate the adverse effects of EPU on carbon emissions. The remainder of this paper is structured as follows. Section II discusses the related literature. Section III describes the data and empirical methodology. Section IV presents the baseline results with robustness checks. Section V presents the results of the extended analysis. Section VI concludes.

## II. RELATED LITERATURE

Our paper is mainly related to the strand of the literature on the economic consequences of EPU. EPU can be broadly defined as “the economic risk associated with ill-defined future governmental policies and regulatory frameworks” (Al-Thaqeeb and Algharabali 2019). Such uncertainty affects economic decision-making at the national, corporate, and individual levels. Businesses often adopt a “wait-and-see” approach during periods of elevated EPU, delaying investment and spending decisions. It follows that our paper is linked to the implications of real options theory for investment, which argues that firms tend to delay investment when uncertainty is high, preferring to wait for clearer information (Dixit and Pindyck 1994, Bloom 2009). As investment for cleaner energy sources such as renewables is capital-intensive and requires substantial upfront outlays, this may be postponed when uncertainty is high, leading to higher carbon emissions, at least in the short run. Related theoretical work suggests higher uncertainty also leads to a higher cost of capital and tighter credit conditions, which hampers investment (Bernanke 1983; Gilchrist, Sim, and Zakrajšek 2014).

Several empirical studies have typically found adverse impacts of EPU on sentiment and broader economic activity (Bloom 2014; Baker, Bloom, and Davis 2016; Li, Su, and Wang 2022). High uncertainty leads households and businesses to adopt risk-averse behaviors, thereby reducing consumption, slowing economic growth, and increasing unemployment (Caggiano, Castelnuovo, and Figueres 2017; Al-Thaqeb, Algharabali, and Alabdulghafour 2020). While substantial work already exists on the impact of EPU on economic activity and prospects, studies examining the effects of EPU on longer-term development goals, such as green economy transition and reducing carbon emissions, remain scarce. Our paper focuses on this aspect, notably from an emerging economy perspective.

A further strand of the related literature exists on the foundations of economy-specific EPU and the role of global shocks, whereby major global financial crises and geopolitical pressures have tended to be associated with heightened economic uncertainty. These would include, for example, the 2008 global financial crisis, the coronavirus disease pandemic, Russia's war in

Ukraine, and United States global trade tariffs in 2025. Policy responses by national authorities in periods of elevated global uncertainty are fraught with difficulty, with economy-specific EPU rising as a result (Rodrik 1991, Aizenman and Marion 1993, Bloom 2009, 2014). EPU can also be the result of idiosyncratic factors and economy-specific financial volatility or political instability (Ozturk and Sheng 2018).

Our paper also relates to the literature on carbon pricing as a mechanism for achieving lower emissions, which has grown in recent years. Following the 2015 Paris Climate Agreement, many economies implemented regulatory measures to curb carbon emissions, with carbon pricing emerging as one of the most effective market-based instruments. Carbon pricing not only reduces emissions but also promotes clean technology investments. Best, Burke, and Jotzo (2020) provide empirical evidence that economies with carbon pricing policies have experienced a 2-percentage point reduction in the annual growth rate of carbon dioxide $(\mathrm{CO}_{2})$ emissions compared to those without such policies. This underscores the importance of regulatory frameworks in shaping emission trajectories.

However, evaluating the impact of carbon pricing on emission reductions remains complex (Sumner, Bird, and Dobos 2011; Meckling, Sterner, and Wagner 2017; Haites 2018). This complexity arises from variations in coverage and stringency across jurisdictions, as well as interactions with other climate policies, such as renewable energy incentives (Narassimhan et al. 2018; Somanathan et al. 2021). Meanwhile, Wang et al. (2025) find that climate policy uncertainty can amplify carbon market volatility, thus presenting a challenge to energy transition and achieving climate targets.

Other work has examined the role of trade openness in shaping emissions. While trade facilitates economic growth, it can also lead to increased carbon emissions via heightened industrial activity. Several studies suggest greater trade openness exacerbates $CO_{2}$ emissions (e.g., Antweiler, Copeland, and Taylor 2001; McAusland 2008; Ertugrul et al. 2016; Mutascu 2018). However, the impact varies across economies, with some studies finding trade openness has heterogeneous effects based on economy-specific factors, such as comparative advantages and regulatory frameworks (Dinda and Coondoo 2006). Our paper builds on this work by considering how the extent of trade openness in emerging economies impacts the effect of EPU on emissions.

In addition, several studies have noted that R&D investment in green technologies can significantly reduce emissions, supporting the transition to a low-carbon economy. Fethi and Rahuma (2019) found that increased R&D spending negatively correlated with carbon emissions. Similarly, Khan et al. (2020) demonstrated that renewable energy adoption, income levels, and environmental innovation contributed to long-term emissions reduction. However, other studies suggest economic innovation alone is insufficient to reduce emissions, particularly in the absence of stringent environmental regulations (Wang and Zhang 2022).

These findings indicate that the impact of innovation on emissions depends on policy frameworks and the level of technological diffusion. While the literature on carbon emissions considers empirically the role of R&D and technological advancement, the link to EPU remains relatively unexplored, however. Our paper builds upon this strand of the literature by examining how R&D investment affects the impact of EPU on carbon emissions.

## III. DATA AND METHODOLOGY

## A. Data

We use available yearly data with an unbalanced panel for 13 EMEs spanning from 1990 to 2023. $^{1}$ The core dependent variable, $CO_{2}$ emissions, is measured as consumption-based emissions in metric tons per capita, sourced from the Global Carbon Budget. To capture EPU, we employ the widely cited Economic Policy Uncertainty Index developed by Baker, Bloom, and Davis (2016), which quantifies uncertainty using textual analysis of over 2,000 newspapers. Following standard practice (Gulen and Ion 2016; Attig et al. 2021), monthly EPU values are averaged to construct an annualized index.

To account for potential heterogeneity in the effects of EPU on carbon emissions, we incorporate several fundamental and institutional characteristics. Specifically, we control for energy consumption (kilogram of oil equivalent per capita), energy intensity (energy use per unit of gross domestic product [GDP]), renewable energy consumption (share of total final energy consumption), trade openness (exports plus imports as a percentage of GDP), and R&D expenditure (percentage of GDP). These data are obtained from the World Bank's World Development Indicators database.

Additionally, we incorporate institutional and financial characteristics, including political stability, measured using the Political Stability and Absence of Violence/Terrorism Index from the World Bank's Worldwide Governance Indicators database; financial development, captured by the Financial Development Index from the International Monetary Fund (IMF), which assesses the depth, access, and efficiency of financial institutions and markets; and climate vulnerability, measured using the Notre Dame Global Adaptation Initiative (ND-GAIN) vulnerability index.

Finally, we incorporate control variables for domestic fundamentals: we include the real GDP growth rate as a measure of domestic output growth and year-on-year changes in the consumer price index as an indicator of inflation.

## B. Ec

[中间内容因长度限制已省略]

ls. Review of Economic Studies, 82 (3): 991–1030.

Dinda, Soumyananda and Dipankor Coondoo. 2006. Income and Emission: A Panel Data-Based Cointegration Analysis. Ecological Economics, 57 (2), 167–181.

Dixit, Avinash and Robert Pindyck. 1994. Investment Under Uncertainty. Princeton, NJ: Princeton University Press.

Ertugrul, Hasan, Murat Cetin, Fahri Seker, and Eyup Dogan. 2016. The Impact of Trade Openness on Global Carbon Dioxide Emissions: Evidence from the Top Ten Emitters Among Developing Countries. Ecological Indicators, 67, 543–555.

Fethi, Sami and Abdulhamid Rahuma. 2019. Eco-Innovation and CO2 Emissions: Evidence from Oil-Exporting Countries. Environmental Science and Pollution Research, 26 (25), 25377–25389.

Gilchrist, Simon, Jae Sim, and Egon Zakrajšek. 2014. Uncertainty, Financial Frictions, and Investment Dynamics. Journal of Finance, 69 (3), 1213–1252.

Grossman, Gene and Alan Krueger. 1991. Environmental Impacts of a North American Free Trade Agreement. Working Paper 3914. Cambridge, MA: NBER.

Gulen, Huseyin and Mihai Ion. 2016. Policy Uncertainty and Corporate Investment. The Review of Financial Studies, 29 (3), 523–564.

Haites, Erik. 2018. Carbon Taxes and Greenhouse Gas Emissions Trading Systems: What Have We Learned? Climate Policy, 18 (8), 955–966.

Jordà, Óscar. 2005. Estimation and Inference of Impulse Responses by Local Projections. American Economic Review, 95 (1), 161–182.

Khan, Zeeshan, Shahid Ali, Muhammad Umar, Dervis Kirikkaleli, and Zhilun Jiao. 2020. Consumption-Based Carbon Emissions and International Trade in G7 countries: The Role of Environmental Innovation and Renewable Energy. Science of the Total Environment, 730, 138945.

Li, Wanli, Yueying Su, and Kaixiu Wang. 2022. How Does Economic Policy Uncertainty Affect Cross-Border M&A: Evidence from Chinese Firms. Emerging Markets Review, 52(C), 100908.

McAusland, Carol. 2008. Trade, Politics, and the Environment: Tailpipe vs. Smokestack. Journal of Environmental Economics and Management, 55 (1), 52–71.

Meckling, Jonas, Thomas Sterner, and Gernot Wagner. 2017. Policy Sequencing Toward Decarbonization. Nature Energy, 2, 918–922.

Mei, Ziwei, Liugang Sheng, and Zhentao Shi. 2026. Nickell Bias in Panel Local Projection: Financial Crises Are Worse Than You Think. Journal of International Economics, 104210.

Mutascu, Mihai. 2018. A Time-Frequency Analysis of Trade Openness and CO2 Emissions in France. Energy Policy, 115, 443–455.

Narassimhan, Easwaran, Kelly Gallagher, Stefan Koester, and Julio Rivera. 2018. Carbon Pricing in Practice: A Review of Existing Emissions Trading Systems. Climate Policy, 18 (8), 967–991.

Ozturk, Ezgi and Xuguang Sheng. 2018. Measuring Global and Country-Specific Uncertainty. Journal of International Money and Finance, 88, 276–295.

Renzhi, Nuobu and Yongjun Baek. 2020. Can Financial Inclusion Be an Effective Mitigation Measure? Evidence from Panel Data Analysis of the Environmental Kuznets Curve. Finance Research Letters, 37, 101725.

Rodrik, Dani. 1991. Policy Uncertainty and Private Investment in Developing Countries. Journal of Development Economics, 36 (2), 229–242.

Shafik, Nemat. 1994. Economic Development and Environmental Quality: An Econometric Analysis. Oxford Economic Papers, 46 (4), 757–773.

Stern, David. 2011. The Role of Energy in Economic Growth. Annals of the New York Academy of Sciences, 1219 (1), 26–39.

Somanathan, E., Rohini Somanathan, Anant Sudarshan, and Meenu Tewari. 2021. The Impact of Temperature on Productivity and Labor Supply: Evidence from Indian Manufacturing. Journal of Political Economy, 129 (6), 1797–1827

Sumner, Jenny, Lori Bird, and Hillary Dobos. 2011. Carbon Taxes: A Review of Experience and Policy Design Considerations. Climate Policy, 11 (2), 922–943.

Yu, Jian, Xunpeng Shi, Dongmei Guo, and Longjian Yang. 2021. Economic Policy Uncertainty (EPU) And Firm Carbon Emissions: Evidence from China. Energy Economics, 97, 105236.

Wang, Huiping and Runzie Zhang. 2022. Effects of Environmental Regulation on CO2 Emissions: An Empirical Analysis of 282 Cities in China. Sustainable Production and Consumption, 29, 259–272.

Wang, Xiaoqing, Fengzi Lu, Adnan Safi, and Xin Li. 2025. Unraveling the Dynamics of Carbon Price Volatility: A Comprehensive Analysis of Impacts from Climate Policy, Fossil Fuel and Renewable Energy Shocks. Energy Strategy Reviews, 62, 101966.

Zhang, Liyuan, Zhenqing Luo, Xiaoyuan Yu, Qiming Yang, and Jiancong Wang. 2025. Economic Policy Uncertainty and Corporate Green Innovation. International Review of Financial Analysis, 97, 103797.

## Economic Policy Uncertainty and Carbon Emissions in Emerging Markets

This paper examines how economic policy uncertainty (EPU) affects carbon emissions in 13 emerging market economies from 1990 to 2023. Results show that higher EPU increases emissions, though effects vary by structural and institutional factors. Economies with stronger institutions, cleaner energy, and higher development levels exhibit weaker responses. Lower-income economies face more pronounced effects, while climate vulnerability also shapes outcomes. The findings highlight how policy and structural conditions influence emissions under uncertainty and inform strategies to mitigate environmental risks.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.
"""
