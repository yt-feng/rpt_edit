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
# Understanding Economic Growth in The Gambia: Challenges and Policy Implications

Ali- Al-Sadiq, Nour Bouzouita, and Chie Aoyagi

SIP/2026/067

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 22, 2026. This paper is also published separately as IMF Country Report No 26/176.

# IMF Selected Issues Paper African Department

# Understanding Economic Growth in The Gambia: Challenges and Policy Implications Prepared by Ali- Al-Sadiq, Nour Bouzouita, and Chie Aoyagi

Authorized for distribution by Eva Jenkner
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 22, 2026. This paper is also published separately as IMF Country Report No 26/176

ABSTRACT: This paper highlights past, current and future drivers of The Gambia's growth and suggests reforms to enhance growth potential and productivity. The Gambia needs to accelerate structural reforms to boost total factor productivity (TFP). Key policy options include strengthening governance and institutional capacity; maintaining macroeconomic stability through prudent fiscal and monetary policies; raising agricultural productivity; fostering private sector-led growth through improvements in the business environment and access to finance; promoting economic diversification; investing in human capital; and addressing critical infrastructure gaps.

RECOMMENDED CITATION: Al-Sadiq, Ali, Nour Bouzouita, and Chie Aoygai. 2026. Understanding Economic Growth in The Gambia: Challenges and Policy Implications. IMF Selected Issues Paper SIP/2026/067

JEL Classification Numbers:

O11, O40, O47, O55, E23.

Keywords:

The Gambia, Economic Growth, Total Factor Productivity, Potential growth, Government Effectiveness

Author's E-Mail Address:

AAlsadiq@imf.org; nbouzouita@imf.org; CAoyagi@imf.org

SELECTED ISSUES PAPERS

# Understanding Economic Growth in The Gambia: Challenges and Policy Implications

The Gambia

Prepared by Ali- Al-Sadiq, Nour Bouzouita, and Chie Aoyagi

## THE GAMBIA

SELECTED ISSUES

June 22, 2026

Approved By

Prepared by Ali- Al-Sadiq, Nour Bouzouita, and Chie Aoyagi.

African Department

## CONTENTS

## UNDERSTANDING ECONOMIC GROWTH IN THE GAMBIA: CHALLENGES AND

POLICY IMPLICATIONS 2

A. Introduction 2

B. Background 3

C. Empirical analysis \_\_\_\_ 5

D. Conclusion 16

## FIGURES

1. Economy's Structure and Export Diversification 4

2a. Impulse Response: Accumulated Impulse Responses of Real GDP to Generalized One

S.D. Innovations 8

2b. Impulse Response: Accumulated Impulse Responses of Credit to Private Sector to

Generalized One S.D. Innovations 9

## TABLES

1. Event Study: Before and After the 2017 Regime Change \_\_\_\_ 10

2. Summary of GMM Estimates of Governance on GDP Per Capita (SSA) \_\_\_\_ 15

References 17

## ANNEX

I. Short- and Long-run Impact of Governance Indicators 19

## APPENDIX

I. Tables 21

Source: IMF WEO database.

# UNDERSTANDING ECONOMIC GROWTH IN THE GAMBIA: CHALLENGES AND POLICY IMPLICATIONS $^{1}$

The Gambia's economic activity has grown at a rate comparable to peers over recent decades, but the income gap with neighboring countries remains large. As contributions from labor and capital to potential growth are expected to decline, The Gambia needs to accelerate structural reforms to boost total factor productivity (TFP). Successful implementation of structural reforms could yield substantial benefits. Key policy options include strengthening governance and institutional capacity; maintaining macroeconomic stability through prudent fiscal and monetary policies; raising agricultural productivity; fostering private sector-led growth through improvements in the business environment and access to finance; promoting economic diversification; investing in human capital; and addressing critical infrastructure gaps.

## A. Introduction

## 1. The Gambia has made commendable progress with lifting growth and incomes.

Following a prolonged period of stagnation due to domestic political autocracy and weak governance, the democratic transition in 2017 marked a turning point for the country's economic recovery. The Gambia's growth has outperformed that of the SSA since 2017, averaging around 5.4 percent, supported by reforms aimed at restoring macroeconomic

![](images/e34a763c8e22e1f66e6e846adb5dfd30c2bfd33b70c97635d11b0dc0852cfd02.jpg)

stability and rebuilding investor confidence. This strong performance has translated into sustained

increases in GDP per capita, which increased from about US\$600 in 2015 to approximately US\$940 in 2024.

2. However, The Gambia's economic growth needs to be strengthened and sustained to ensure long-term development and poverty reduction. Despite some progress, the country continues to lag behind other nations in the Sub-Saharan Africa (SSA) region. In 2024, The Gambia's per capita

![](images/f3797a1c8f99c11e3ab5e2705d9c4309952c3cd2ccd335a59c5bdf9f5e67be14.jpg)

income remained roughly half the regional average and significantly below that of its neighboring countries. This disparity highlights structural weaknesses in the economy and the need for diversification beyond agriculture. Accelerating growth in non-agricultural sectors—such as manufacturing, tourism, and other services—is essential to reduce economic volatility, enhance resilience, and create meaningful employment opportunities for the country's young and rapidly expanding population.

3. This paper highlights past, current and future drivers of The Gambia's growth and suggests reforms to enhance productivity. Section B documents recent economic developments. A growth accounting is undertaken in Section C to identify the contributions of factors accumulation and total factor productivity (TFP) growth to the Gambia's economic performance. The determinants of growth are econometrically identified in Section D. Section E estimates potential GDP for The Gambia. Finally, policy recommendations are discussed in Section F.

## B. Background

4. The Gambia continues to face severe economic and developmental challenges, remaining among the poorest nations in the world. According to the 2024 United Nations Human Development Index (HDI), the country ranks 171st out of 191 countries, reflecting persistently low levels of income, limited access to quality education, and inadequate health outcomes with no significant improvement over the past ten years. As of the most recent data, The Gambia's HDI is approximately 0.52, reflecting low levels of income, educational attainment, and health outcomes that contribute to limited human development. By contrast, the average HDI for Sub-Saharan Africa (SSA) is higher—about 0.55—indicating that many SSA countries have achieved comparatively better progress in key human development dimensions such as life expectancy, education, and standard of living. These challenges are deeply interconnected and reinforce cycles of poverty, constraining human capital development and limiting productivity across the economy. High levels of vulnerability, particularly among rural communities, youth and women, further exacerbate inequality and undermine social and economic inclusion, posing significant obstacles to sustainable development.

![](images/6dbc5e38eaf8d6e1a66479edc6730faae5499aa83d0a3b0a810bb6ad29696504.jpg)

![](images/f3e85f24ea443a8fd1f88017ee2b6372e31f22ae5191098c3634e67c18faaed4.jpg)

5. The economic structure has changed but still shows strong dependence on agriculture and tourism. The Gambian economy has experienced dynamic changes in the past decade, with agriculture's share in GDP value added dropping from 35 percent in 2010 to 22 percent in 2023.

![](images/c0f51080bb8bb4992d16ad2ed6b9b706df94999c9703006ce6db8cc8cec26595.jpg)

However, the agricultural sector remains a cornerstone of economic activity and employs a significant portion of the population. Tourism also continues to be a major pillar of the economy, contributing significantly to foreign exchange earnings, employment, and economic activity. This heavy reliance makes the economy highly vulnerable to external shocks such as climate change and natural disasters, fluctuating commodity prices, and global travel disruptions and tourism demand. Efforts to diversify into other sectors—such as manufacturing, information and communication technology, and other services—have been limited, underscoring the need for targeted policies and investment to build a more resilient and diversified economic base. These structural weaknesses contribute to substantial output volatility, which in turn undermines overall macroeconomic performance and long-term growth prospects. The standard deviation of nominal and real GDP growth between 2000-2024 is among the highest in the region.

Figure 1. Economy's Structure and Export Diversification

6. The Gambia remains acutely exposed to climate change and environmental risks, with low-lying coastal geography and a heavy reliance on rain-fed agriculture intensifying macroeconomic vulnerabilities. Severe flooding in July-August 2022—the heaviest in decades—affected more than 50,000 people, displaced over 7,000 residents in Banjul Area, and damaged infrastructure and homes, disrupting commerce and heightening public spending needs for recovery and water-management projects. In the 2024 rainy season, erratic rainfall patterns culminated in intense floods that killed at least 11 people, displaced over 5,000, and undermined agricultural output, while prolonged dry spells and drought episodes have reduced crop yields and heightened food insecurity, pressuring household incomes and import bills. These climate shocks have constrained growth in the agriculture and tourism sectors, increased fiscal demands for disaster response and resilience building, and underscore the need for continued external support and investment in climate-resilient infrastructure and early-warning systems to protect livelihoods and long-term economic stability.

7. The Gambia has a young and fast-growing population. Population growth is strong with 2.5 percent per annum. The population is young with one third below the age of 15 and only 6 percent over the age of 65. According to UNICEF estimations, The Gambia is among the top 20 countries with the largest youth share in their respective populations. In addition, the average family size has increased relative to a decade ago, which requires the creation of more jobs to absorb young job seekers.

![](images/8c7823c84e9fa6042b3c5033f57a34ed707d05716a6d323ef721f55d34b11034.jpg)

## C. Empirical analysis

## Growth Accounting

8. We conduct a growth accounting exercise to identify the contributions of supply factors to The Gambia's growth: namely labor, physical capital, and total factor productivity. $^{2}$ The analysis covers the period 1995-2024.

9. Growth accounting can be used to assess the extent to which observed output growth has been driven by factor accumulation versus TFP gains. The convention is to assume a (Cobb-Douglas) constant returns to scale aggregate production function, so that:

$$
Y _ {t} = A _ {t} K _ {t} ^ {\alpha} L _ {t} ^ {1 - \alpha}
$$

where Y is aggregate output, A is total factor productivity, K is the physical capital stock, Lis units of labor, and $\alpha$ is the elasticity of output with respect to the physical capital stock.

Expressing the equation in terms of units of labor (denoted in small case letters), and taking logs and their difference give:

$$
l n y _ {t} = l n A _ {t} + \alpha l n K _ {t} + (1 - \alpha) l n L _ {t}
$$

Where growth in output per unit of labor is the sum of growth in total factor productivity (growth in A) and growth in capital-labor ratio weighted by $\alpha$ . Estimates of TFP are sensitive to the value $\alpha$ , which is the elasticity of output with respect to the capital-labor ratio.

To compute the stock of capital (K), we use the perpetual inventory equation:

$$
K _ {t} = (1 - \delta) K _ {t - 1} + I _ {t}
$$

Where $I_{t}$ is investment at time t and $\delta$ its depreciation rate. The initial capital stocks, investments and the depreciation rates are necessary and sufficient to determine the capital stocks at each point in time. The total initial capital stock is set to equal 0.7 times real GDP. The depreciation rate is set to 5 percent per year, in line with the literature on low-income countries that posits depreciation rates between 3 percent and 5 percent per year. $^{3}$ In line with the literature on low-income countries, we assume that the elasticity of capital to output 0.3. Data on real GDP, total investment, and labor come from the World Bank.

10. Overall real GDP growth over 1995-2024 was mostly driven by the accumulation of factors of production, with TFP growth contributing little on average. The accumulation of human capital consistently provided the most important contribution to real GDP growth. Physical capital accumulation's contribution to real growth during the 1990s was low, reflecting relatively low investments compounded by the civil unrest at the time. During the following decade, the contribution of physical capital accumulation picked up, fueled by large public investments, and significantly contributed to real growth. Finally, TFP contributions have been volatile and often negative, underscoring the lack of sustained productivity gains.

![](images/9b66dfadad5fea1d961d68710511fc7a38690b04759eabf003265e400861385d.jpg)

## Vector Autoregression (VAR)

11. This section uses a Vector Autoregression (VAR) model to examine the dynamic interactions between economic growth and several macroeconomic and financial variables in The Gambia. The VAR framework allows all variables to be treated as endogenous and captures their joint evolution over time without imposing strong structural restrictions.

$$
Y _ {i, t} = A (L) Y _ {i, t} + C X _ {i, t} + u _ {i, t}
$$

where $Y_{i,t}$ is a vector of endogenous variables with p lags. We consider the following variables: bank credit to private sector, total remittances, foreign aid, FDI, real GDP, inflation rates, and lending rates as endogenous variables. $X_{i,t}$ is a vector of exogenous variables (real effective exchange rate) and $u_{i,t}$ is a vector of structural error terms.

12. The analysis uses quarterly data covering the period 2003Q1–2024Q4. Real GDP growth is measured as the quarterly growth rate of real GDP. To control for scale effects and reduce potential non-stationarity, FDI, remittances, and credit to the private sector are expressed as ratios to GDP. Where appropriate, variables are transformed into logarithms prior to estimation. All data come from the World Bank and the Central Bank of The Gambia. $^{4}$

13. All impulse responses in our VAR analysis come from a typical estimation where we chose the lag order of two. $^{5}$ The IRFs are generated to trace the effect of a one-standard-deviation shock to each variable on real GDP growth. Confidence intervals are computed using bootstrap methods to assess statistical significance.

## Results

14. Figure 2a presents accumulated impulse responses of real GDP to one-standard-deviation structural shocks, with 95 percent confidence intervals.

Figure 2a. Impulse Response: Accumulated Impulse Responses of Real GDP to Generalized One S.D. Innovations
95% CI using analytic asymptotic S.E.s  
![](images/1086d7517d87116132028a612a91e83eb2e2bc55eaf920562d9fdbd93a055ddd.jpg)

![](images/6b7326e745185ba1b2835957ad9bb7083dd8163921ecfc020b16b1b86817c322.jpg)

![](images/f2fa8ab9f3eec78688411bf9f7d4def6e040cdc43e34ea45ee971a4cbb192b76.jpg)  
Source: authors' estimations.

![](images/db9ea7c39665d107a3ea61f9c71f19f561da881538e60168aa2864d3762eb6a4.jpg)

\- Growth Response to FDI Shocks. A positive shock to FDI leads to a gradual increase in real GDP growth. The response is statistically insignificant on impact but becomes positive after approximately four quarters, reaching a peak between six and eight quarters before gradually dissipating. This pattern suggests that FDI affects growth primarily through medium-term investment and productivity channels rather than immediate demand effects.

\- Growth Response to Remittance Shocks. Growth responds positively and immediately to a remittance shock. The effect is strongest within the first two quarters and fades after approximately four to six quarters. The short-lived nature of the response is consistent with remittances supporting growth mainly through consumption smoothing and aggregate demand rather than sustained investment.

\- Growth Response to Credit Shocks. A shock to credit to the private sector generates a positive but delayed response in GDP growth. The effect becomes noticeable after two to four quarters and remains modest throughout the horizon. This finding suggests that while financial intermediation supports growth, its quantitative impact remains limited, reflecting the shallow depth of the financial sector.

Figure 2b. Impulse Response: Accumulated Impulse Responses of Credit to Private Sector to Generalized One S.D. Innovations
95% CI using analytic asymptotic S.E.s - Transmission Channels. Additional impulse responses indicate that remittance shocks are associated with an increase in private sector credit, suggesting that a part of remittance inflows enter the domestic financial system. In contrast, FDI shocks have a weaker and less immediate effect on credit, consistent with the enclave nature of some foreign investment.

![](images/baa213b2badcc1754809bff46f2fb5511fe3bde15e8e40ea28e0d2c9cb7e2302.jpg)

![](images/2a27c5451f2ef1713dbd8c510d96b36fde1a589577b8eea7823d7083f268995f.jpg)

![](images/e4db6f40991d2e43f456886bf6093888fbb13e5dd0e15ae4558fdd0f7b1acc43.jpg)  
Source: authors' estimations.

![](images/ce5ac23f9f10da218ab78f9962dbcceddea9b24e617e84178182f0d66c709f05.jpg)

## Event Study Analysis

15. To complement the VAR analysis, we conduct an event study for The Gambia centered on the 2017 regime change. The analysis compares average values of key macroeconomic, governance, fiscal, external, and social indicators across two periods: the pre-transition period (2013–2016) and the post-transition period (2018–2024). The event year 2017 is excluded from both periods to avoid capturing transition dynamics. Data on our variables come from the World Bank's 2026 Economic Development Indicators (See Appendix Table 10). We also report a pre-COVID window (2018–2019) to isolate the transition eff

[中间内容因长度限制已省略]

tr><td>Gambia, The</td><td>Tanzania</td><td></td><td></td><td></td></tr><tr><td>Ghana</td><td>Togo</td><td></td><td></td><td></td></tr><tr><td>Guinea</td><td>Uganda</td><td></td><td></td><td></td></tr><tr><td>Guinea-Bissau</td><td>Zambia</td><td></td><td></td><td></td></tr><tr><td>Kenya</td><td>Zimbabwe</td><td></td><td></td><td></td></tr><tr><td>Lesotho</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Notes: Country inclusion subject to data availability across the estimation period.</td></tr><tr><td colspan="5">Table 10. The Gambia: Variable Definitions and Data Sources (Panel Models)</td></tr><tr><td>Source</td><td>Variable</td><td colspan="3">Definition</td></tr><tr><td colspan="5">Dependent variable</td></tr><tr><td>WB WDI</td><td>In(GDP per capita)</td><td colspan="3">Natural log of real GDP per capita (constant 2015 USD).Dependent variable in all panel models.</td></tr><tr><td colspan="5">Governance: World Bank WGI (range -2.5 to +2.5; higher = better governance)</td></tr><tr><td>WB WGI</td><td>Govt. effectiveness</td><td colspan="3">Quality of public services, civil service, and policy formulation.</td></tr><tr><td>WB WGI</td><td>Corruption control</td><td colspan="3">Extent to which public power is exercised for private gain.</td></tr><tr><td>WB WGI</td><td>Rule of law</td><td colspan="3">Confidence in contract enforcement, property rights, and the courts.</td></tr><tr><td>WB WGI</td><td>Regulatory quality</td><td colspan="3">Government's ability to implement sound policies promoting private sector development.</td></tr><tr><td>WB WGI</td><td>Voice &amp; accountability</td><td colspan="3">Citizens' ability to participate in selecting their government and freedom of expression.</td></tr><tr><td>WB WGI</td><td>Political stability</td><td colspan="3">Likelihood of political instability and politically motivated violence.</td></tr><tr><td colspan="5">Macroeconomic controls</td></tr><tr><td>WB WDI</td><td>In (Investment)</td><td colspan="3">Natural log of gross fixed capital formation (current USD).</td></tr><tr><td>WB WDI</td><td>In (CPI)</td><td colspan="3">Natural log of consumer price index (2010=100). Proxy for inflation in panel models.</td></tr><tr><td>WB WDI</td><td>Trade openness (% GDP)</td><td colspan="3">Sum of exports and imports as a share of GDP.</td></tr><tr><td colspan="5">External and fiscal controls</td></tr><tr><td>WB WDI</td><td>FDI (% GDP)</td><td colspan="3">Net foreign direct investment inflows as a share of GDP.</td></tr><tr><td>WDI/Authors</td><td>Remittances (% GDP)</td><td colspan="3">Remittances received as a share of GDP. Computed as 100 × remittances / nominal GDP.</td></tr><tr><td>WB WDI</td><td>Aid (% GDP)</td><td colspan="3">Net official development assistance received as a share of GDP.</td></tr><tr><td colspan="5">Robustness check (added to FE baseline, SSA only)</td></tr><tr><td>WB WDI</td><td>Education spending (% GDP)</td><td colspan="3">Government expenditure on education as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Health spending (% GDP)</td><td colspan="3">Government expenditure on health as a share of GDP.</td></tr><tr><td colspan="5">Sources: World Bank World Development Indicators (WDI); World Bank Worldwide Governance Indicators (WGI).</td></tr><tr><td>Source</td><td>Variable</td><td colspan="3">Definition</td></tr><tr><td colspan="5">Real sector</td></tr><tr><td>WB WDI</td><td>Real GDP growth (%)</td><td colspan="3">Annual percentage change in real GDP.</td></tr><tr><td>WB WDI</td><td>Real GDP per capita (USD)</td><td colspan="3">Real GDP per capita in constant USD.</td></tr><tr><td>WB WDI</td><td>Investment (% GDP)</td><td colspan="3">Gross fixed capital formation as a share of GDP.</td></tr><tr><td>WB WDI</td><td>GDP deflator (%)</td><td colspan="3">Annual % change in GDP deflator. Used instead of I(CPI) as it is directly expressed as a growth rate.</td></tr><tr><td colspan="5">External sector</td></tr><tr><td>WB WDI</td><td>FDI (% GDP)</td><td colspan="3">Net foreign direct investment inflows as a share of GDP.</td></tr><tr><td>WDI/Authors</td><td>Remittances (% GDP)</td><td colspan="3">Remittances received as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Current account (% GDP)</td><td colspan="3">Current account balance as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Trade openness (% GDP)</td><td colspan="3">Sum of exports and imports as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Debt service/exports (%)</td><td colspan="3">Total debt service as a share of exports of goods and services.</td></tr><tr><td colspan="5">Fiscal sector</td></tr><tr><td>WB WDI</td><td>Aid (% GDP)</td><td colspan="3">Net official development assistance received as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Govt. consumption (% GDP)</td><td colspan="3">Government final consumption expenditure as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Govt. expenditure growth</td><td colspan="3">Annual growth rate of general government expenditure.</td></tr><tr><td>WB WDI</td><td>Education spending (% GDP)</td><td colspan="3">Government expenditure on education as a share of GDP.</td></tr><tr><td>WB WDI</td><td>Health spending (% GDP)</td><td colspan="3">Government expenditure on health as a share of GDP.</td></tr><tr><td colspan="5">Social indicators</td></tr><tr><td>WB WDI</td><td>School enrollment (%)</td><td colspan="3">Gross school enrollment ratio (primary and secondary). Proxy for human capital.</td></tr><tr><td>WB WDI</td><td>Population growth (%)</td><td colspan="3">Annual population growth rate.</td></tr><tr><td colspan="5">Sources: World Bank World Development Indicators (WDI); World Bank Worldwide Governance Indicators (WGI).</td></tr></table>
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
