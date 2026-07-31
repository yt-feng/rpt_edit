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
# Drivers of Private Consumption in Singapore

Sandile Hlatshwayo

SIP/2026/075

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 29, 2026. This paper is also published separately as IMF Country Report No 26/186.

2026
JUL

![](images/d1e2cb7d2ed436ea64e36ab97f3a1fe6f3c9e553927c6ac7b5ca4c0dad246168.jpg)

# IMF Selected Issues Paper Asia Pacific Department Drivers of Private Consumption in Singapore Prepared by Sandile Hlatshwayo

Authorized for distribution by Masahiro Nozaki
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 29, 2026. This paper is also published separately as IMF Country Report No 26/186.

ABSTRACT: Private consumption ratios differ markedly across advanced economies, with Singapore recording one of the lowest of its peer group. Using a sample of 31 advanced economies and a rich set of potential drivers, the analysis finds that slow-moving structural factors like demographics, economic structure, and development levels are important correlates of these differences, while cyclical factors appear to play a more limited role. Relative to other advanced markets, Singapore's lower old age dependency ratio, lower labor share, high real GDP per capita, and role as a financial hub all weigh on its consumption ratio.

RECOMMENDED CITATION: Hlatshwayo, S. (2026). Drivers of private consumption in Singapore (IMF Selected Issues No. 26/075). International Monetary Fund.

<table><tr><td>JEL Classification Numbers:</td><td>E21, D12, O53</td></tr><tr><td>Keywords:</td><td>Private consumption, household saving, Singapore, external balances</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>SHlatshwayo@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# Drivers of Private Consumption in Singapore

Singapore

Prepared by Sandile Hlatshwayo $^{1}$

## SINGAPORE

SELECTED ISSUES

June 29, 2026

Approved By
Asia Pacific
Department

Prepared By Sandile Hlatshwayo (APD)

## CONTENTS

DRIVERS OF PRIVATE CONSUMPTION IN SINGAPORE 2
A. Introduction 2
B. Methodology 3
C. Findings 4
D. Conclusion 7

## TABLE

1. Drivers of Private Consumption (Percent of GNDI) \_\_\_\_ 8

## ANNEXES

I. Data Definitions and Sources 9

II. Key Drivers of Differences in Private Consumption to GNDI for Singapore and

References 11

## DRIVERS OF PRIVATE CONSUMPTION IN SINGAPORE $^{1}$

Private consumption ratios differ markedly across advanced economies, with Singapore recording one of the lowest of its peer group. Using a sample of 31 advanced economies and a rich set of potential drivers, the analysis finds that slow-moving structural factors like demographics, economic structure, and development levels are important correlates of these differences, while cyclical factors appear to play a more limited role. Relative to other advanced markets, Singapore's lower old age dependency ratio, lower labor share, high real GDP per capita, and role as a financial hub all weigh on its consumption ratio.

## A. Introduction

1. Singapore's private consumption ratio is low and has fallen over time relative to other advanced economies (see Figure 1). In 2024, Singapore's private consumption as a share of gross national disposable income (GNDI) was 38 percent, down from 46 percent in 1990. Across a sample of advanced economies, its share is the lowest but comparable to economies like Ireland and Denmark. Prior analysis has shown that Singapore's high level of development, rapidly aging population, and low labor share contribute to its low consumption ratio (Qureshi, 2016; Yoo, 2021).

Figure 1. Private Consumption Trends Across Advanced Economies  
![](images/c6316003bd5d92297ea200d3b955cd39b270a40bbb5b962331db382047694ad8.jpg)

![](images/33d6d0f9ce3afd2055f9d4e34fdb6dd2486bfbdfe441ce08cfef81c6d4565dfc.jpg)  
Sources: IMF WEO, CEIC, OECD, and IMF staff calculations.

2. To understand the fundamental determinants of Singapore's consumption ratio, this analysis builds on prior research and introduces three novel contributions to the literature. The analysis includes a rich variety of drivers like uncertainty, demographics, development levels, structural features, and cyclical factors, drawing on prior literature. It also adds three novel contributions to the subset of the literature that focuses on Singapore's private consumption rate. First, it introduces a time-varying control for financial center intensity, measured using gross external assets and liabilities relative to GDP to account for the role of large cross-border balance sheets in shaping saving and consumption behavior in highly integrated financial hubs like Singapore. This improves on prior approaches that relied on ad hoc dummy indicators for financial hubs. Second, it explores how being a financial hub interacts with an economy's small geographic size, under the

hypothesis that geographically smaller financial hub countries have higher savings rates given limited domestic investment opportunities. Third, it includes a time-varying control to help account for the role of pension systems.

## B. Methodology

3. To examine the drivers of variation in private consumption rates across countries, we use two-way fixed effects regressions. The sample includes 31 advanced economies over the period from 1990 to 2024. $^{2}$ The baseline estimating equations take the following form:

$$
\begin{array}{r l} c _ {i, t} = \alpha + \beta_ {1} ^ {\prime} D e m o g r a p h i c s _ {i, t} + \beta_ {2} L a b o r I n c o m e S h a r e + \beta_ {3} R e a l G D P p e r C a p i t a _ {i, t - 1} \\ & + \beta_ {4} ^ {\prime} C y c l i c a l F a c t o r s + \beta_ {5} G o v e r n m e n t C o n s u m p t i o n _ {i, t} + \beta_ {6} P e n s i o n S y s t e m s _ {i, t} \\ & + \beta_ {7} F i n a n c i a l C e n t e r I n t e n s i t y _ {i, t} + \delta_ {i} + \theta_ {t} + \varepsilon_ {i, t} \end{array}
$$

Where $c_{i,t}$ denotes private consumption as a share of GNDI in country i and year t; demographics is a vector of controls including the population growth rate, old age dependency ratio, and aging speed (measured as the difference between the old-age dependency ratio 20 years ahead and the ratio in year t); cyclical factors include real growth, household credit/GDP, interest rates, changes in terms of trade, and the unemployment rate; a measure of net contributions made to pension schemes as a share of GDP; financial center intensity is the log of gross assets and liabilities/GDP; $\delta_{i}$ denotes country fixed effects that absorb time-invariant cross-country heterogeneity; $\theta_{t}$ denotes year fixed effects that absorb common global shocks in year t; and $\varepsilon_{i,t}$ is the error term. See Annex I for more detail on data definitions and sources. The estimated standard errors are robust to heteroskedasticity.

4. The empirical results should be interpreted with several caveats. First, in order to compile a broad and consistently available panel, the dependent variable uses GNDI as the denominator rather than household personal disposable income. Household personal disposable income is the household resource concept most relevant for consumption decisions but it is not available for the full sample in earlier years. While GNDI is preferable to GDP as a denominator because it better captures income available to residents, it remains an imperfect proxy. Second, several explanatory variables, including income uncertainty and financial center intensity are constructed proxies and may be measured with error. Third, the pension indicator captures variation in net contributions as a share of GDP for pension programs where there are transfers between current contributors and current beneficiaries, as in defined benefit schemes. However, for defined contribution schemes where no such redistributive transfers occur, the indicator is set to zero and does not capture varying levels of intensity in defined contribution schemes that can drive consumption lower in some economies. As a complement, staff also conducts an analysis using pension parameters to explain variation in saving behavior across markets, drawing on the IMF's 2026 External Balance Assessment pension tool. Finally, the empirical approach identifies partial

correlations rather than general equilibrium causal effects, and some coefficients may still reflect omitted factors not fully captured by the controls.

## C. Findings

5. Structural characteristics like demographics, economic structure, and income levels play important roles in driving private consumption patterns across advanced economies. Table 1 shows the results of the analysis. The analysis finds that, amongst advanced economies, structural factors like a more elderly population and higher labor income shares are associated with higher consumption ratios, while higher GDP per capita levels, greater financial center intensity, and faster population growth are associated with lower consumption ratios. Cyclical factors, including stronger output growth and higher returns on savings, also drive down consumption but are less important. In particular:

\- The coefficient on the old-age dependency ratio is positive and is statistically significant across most specifications. In the preferred specification shown under Column 8 of Table 1, a one percentage point (ppt) increase in the old-age dependency ratio is associated with a 0.41 ppt increase in the consumption ratio. This result is in line with findings in the literature that demographics are an important driver of consumption dynamics (Modigliani and Brumberg, 1954). Population growth, by contrast, is negative and significant in most specifications, with a 1 ppt increase associated with a roughly 0.23 ppt lower consumption ratio. Aging speed has an unexpectedly positive sign and is not statistically significant across the specifications. This finding contrasts with prior literature that found that faster aging tends to lower consumption. One factor that may be attenuating the results is a statistical convergence in the projected variation across countries' aging patterns of UN population forecasts relative to prior forecast vintages. However, broadly speaking, the demographic patterns are consistent with the life-cycle model of consumption and savings: a larger elderly population tends to be associated with higher dissaving and consumption, while economies with fast-growing populations and associated labor force dynamics have lower consumption ratios.

\- For labor share, a one ppt increase in the share of labor compensation in national income is significantly associated with a 0.44 ppt higher consumption-to-GNDI ratio. This is consistent with Yoo (2021) and highlights that economies with large corporate sectors and a large share of foreign-owned multinationals have a smaller portion of resources that accrue to domestic households (Figure 2). $^{3}$

\- Higher-income economies have lower consumption ratios. In the preferred specification, a one log unit increase in lagged real GDP per capita is significantly associated with a 4.4 ppt lower consumption ratio, which squares with findings that higher-income economies and the higher-income households within them have a lower marginal propensity to consume, including

because of higher bequest and precautionary saving motives (Agarwal and Qian, 2014; De Nardi, 2004; De Nardi et al., 2010; Jappelli and Pistaferri, 2014).

\- For cyclical and policy-related factors, a one ppt increase in real GDP growth is significantly associated with a 0.15 ppt lower consumption ratio in the preferred specification, broadly in line with prior findings (Masson et al., 1998), while a one ppt increase in household credit-to-GDP is associated with about a 0.04 ppt higher consumption ratio (Mian et al., 2017). A one ppt increase in the real short-term deposit rate is significantly associated with a 0.17 ppt lower consumption ratio; a higher real return on deposits strengthens incentives to save and defer consumption and may also be related to the composition of households' balance sheets (Cloyne et al., 2020). Improvements in terms-of-trade lower consumption, which could reflect that the positive income shocks from terms-of-trade increases largely accrue to corporates and not households. Higher income uncertainty tends to reduce consumption, consistent with real options 'wait-and-see' effects (Baker et al., 2016) but the size of the effect becomes statistically insignificant and much smaller once a broader set of controls is included. Year fixed effects that absorb major global shocks may also capture income uncertainty. The unemployment rate and government consumption/GDP are not statistically significant.

\- For pensions, the control is a rough proxy for pension-induced household saving. A one ppt increase in net contributions associated with defined benefit or pay-as-you-go systems is associated with about a 1.1 ppt lower consumption-to-GNDI ratio. As previously noted, however, the pension control does not capture the behavioral dimension of defined contribution pension systems, where mandatory contribution rates, fund generosity, and the extent of consumption-smoothing facilitated by such schemes vary considerably and can influence household saving and consumption outcomes. A separate analysis using the pension toolkit from the 2026 External Balance Assessment methodology shows that Singapore's defined contribution pension system can help explain up to 1.6 percent of GDP of its current account surplus.

\- The effect of increases in financial center intensity is large and negative: a one log unit increase in the log financial-center measure is significantly associated with about a 1.9 ppt lower consumption ratio. Despite the difference in construction of the measures, this is close to results from studies that use dummy indicators for financial centers. Namely, relative to non-financial centers, Qureshi (2016) finds that financial centers are associated with a higher private saving rate of around 2 percent of GDP and IMF (2017) external balance estimates show that financial centers are associated with a higher current account balance of about 3 percent of GDP.

\- Finally, small geographic size does not appear to drive higher saving conditional on being a financial hub. The interaction term between a small state dummy indicator and the financial center intensity measure is positive, significant, and fully offsets the negative base effect of the financial center measure, suggesting that large financial hubs that are also small geographically have higher consumption rates relative to physically larger financial hubs. To assess the robustness of this finding, the shares of global population and output were used as alternative measures for small economies. The interaction effect for financial center intensity with output shares is insignificant, but the interaction term for population shares produces a net positive

Sources: External Wealth of Nations and IMF staff calculations.

result that lends some credence to the idea that countries with smaller populations have lower consumption and higher savings, conditional on being financial centers. $^{4}$ Neither of the population share nor the output share indicators are statistically significant on their own.

Figure 2. Labor Share and Financial Center Intensity Across Advanced Economies

![](images/c842faff65d16746ff9c648eb431ea1cfe6a38dbbdb20dccd6cbc1c6b3d9366c.jpg)  
Sources: Penn World Tables and IMF staff calculations.

![](images/dbcd24d927d59fdda45ca818d55a886b3a19211c2fbf7c8d71e946e9fbb00ebe.jpg)

6. For Singapore, its demographics, low labor share, high level of development, low household credit, and financial center status reduce its 2024 consumption relative to peers. Using the preferred specification, Figure 3 shows the decomposition of the key drivers comparing

Singapore's lower consumption rate to that of the average for other advanced economies in 2024. The most important driver is Singapore's old age dependency ratio, which is lower than in other advanced economies at present despite its rapidly aging population. Singapore's labor share ranks second in importance and is amongst the lowest in the sample at 10 ppts below the average for the rest of the sample. Other important factors are Singapore's higher level of real GDP per capita, financial center status, and lower household credit to GDP. See Annex II for a comparison of

![](images/e772c2b4dd92372f5d17d2f34887a88762645701cf8be7bde797b2e0447b20f3.jpg)  
Note: Middle bars show coefficients' estimated contribution of various drivers for Singapore's 2024 consumption rate relative to other advanced economies' average 2024 consumption rate based on a panel fixed effects regression for 31 advanced economies over the period from 1990 to 2024.

Singapore's private consumption rate to other financial centers. The drivers are similar to those shown in Figure 3, except for the financial center intensity indicator given that Singapore's financial center intensity is lower than the average of other financial centers.

7. Over the past two decades, the decline in Singapore's consumption ratio was driven by similar factors. Figure 4 shows that the decline in Singapore's consumption ratio between 2002 (a

peak year) and 2024 includes a higher level of development, falling labor share $^{5}$ , and growing prominence as a financial hub, as well as global shocks captured by the year fixed effects contribution. The impacts of the year fixed effects are particularly significant and negative around the time of the Covid-19 pandemic when health-related policy interventions and associated preventative behavior lowered household consumption. At the same time, Singapore's old age dependency ratio has increased, partially offsetting the pull factors.

![](images/0f4247f7cb5e63ab81004938eaebfe66e90c8650b787e4b096555a8f83109a52.jpg)  
Note: Middle bars show coefficients' estimated contribution for various drivers of Singapore's 2002 consumption rate relative to Singapore's 2024 consumption rate based on a panel fixed effects regression for 31 advanced economies over the period from 1990 to 2024. Years selected based on peak consumption in 2002 and the most recent year in the sample.

## D. Conclusion

8. The analysis suggests that Singapore's low private consumption-to-GNDI ratio is primarily a structural phenomenon. Relative to other advanced

[中间内容因长度限制已省略]

d>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="10">Robust standard errors in parentheses; R-squared is within R-squared; constant, country, and time fixed effects not shown; *p&lt; 0.10, **p&lt; 0.05, ***p&lt; 0.01</td></tr></table>

## Annex I. Data Definitions and Sources

<table><tr><td>Variables</td><td>Source / Notes</td></tr><tr><td>Private consumption as a share of gross national disposable income (GNDI)</td><td>IMF WEO, CEIC, OECD</td></tr><tr><td>World Uncertainty Index (in logs)</td><td>World Uncertainty Index</td></tr><tr><td>Income uncertainty</td><td>Author&#x27;s calculations using real GDP per capita data from IMF WEO. Preferred measure is the conditional standard deviation of annual real GDP per capita growth from country-specific GARCH(1,1) models following IMF 2021; if GARCH fails, ARCH(1); if both fail, used 5-year rolling variance</td></tr><tr><td>Old-age dependency ratio</td><td>UN population data</td></tr><tr><td>Population aging speed</td><td>UN population data; author&#x27;s calculations; difference between the old-age dependency ratio 20 years ahead and its current value</td></tr><tr><td>Population growth rate</td><td>IMF WEO</td></tr><tr><td>Population share (% of world population)</td><td>World Bank</td></tr><tr><td>Output share (% of world GDP)</td><td>World Bank</td></tr><tr><td>Labor income share</td><td>Penn World Table; share of labor compensation in GDP at current national prices; for 2024, the 2023 estimates are used</td></tr><tr><td>Log real GDP per capita</td><td>IMF WEO; GDP per capita at constant PPP prices</td></tr><tr><td>Growth of real GDP per capita</td><td>IMF WEO</td></tr><tr><td>Real GDP growth</td><td>IMF WEO</td></tr><tr><td>Household credit to GDP</td><td>BIS; credit to the non-financial sector, Households &amp; NPISHs</td></tr><tr><td>Real deposit interest rate</td><td>IMF WEO</td></tr><tr><td>Annual change in the terms of trade</td><td>IMF WEO</td></tr><tr><td>Unemployment rate</td><td>IMF WEO</td></tr><tr><td>General government consumption expenditure as a share of GDP</td><td>World Bank</td></tr><tr><td>Pension adjustment as a share of GDP for defined benefit systems</td><td>OECD; IMF; author&#x27;s calculations. In line with the 2008 System of National Accounts, the adjustment for the change in pension entitlements is defined as the total value of the actual and imputed social contributions payable into pension schemes, plus the total value of contribution supplements payable out of the property income attributed to pension fund beneficiaries, minus the value of the associated service charges, minus the total value of the pensions paid out as social insurance benefits by pension schemes. The data on the pension adjustments are sourced from the OECD and are divided by nominal GDP. The indicator is set to zero for countries whose core mandatory pension pillar is funded defined contribution</td></tr><tr><td>Financial center intensity (in logs)</td><td>External Wealth of Nations Dataset; author&#x27;s calculations; gross external assets plus gross liabilities relative to GDP</td></tr><tr><td>Small geographic size dummy</td><td>Author&#x27;s classification using geographic size for smallest three economies in the sample; equals one for Singapore, Hong Kong SAR, and Luxembourg.</td></tr></table>

Annex II. Key Drivers of Differences in Private Consumption to GNDI for Singapore and Other Financial Centers, 2023  
![](images/521401684cb79e3f157219176e8b7e297e6dc1a512edbc6fde8cb95661fb8d04.jpg)  
Note: Middle bars show coefficients' estimated contribution for various drivers of Singapore's 2023 consumption rate relative to the 2023 average consumption rate of other financial centers. The comparison group of financial center economies includes Hong Kong SAR, Ireland, Luxembourg, the Netherlands, and Switzerland. This figure uses 2023 instead of 2024 to allow for more data coverage of the financial centers across the various indicators.

## References

Agarwal, S., & Qian, W. (2014). Consumption and debt response to unanticipated income shocks: Evidence from a natural experiment in Singapore. American Economic Review, 104(12), 4205-4230.

Autor, D., Dorn, D., Katz, L. F., Patterson, C., & Van Reenen, J. (2020). The fall of the labor share and the rise of superstar firms. The Quarterly Journal of Economics, 135(2), 645-709.

Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. The Quarterly Journal of Economics, 131(4), 1593-1636.

Cloyne, J., Ferreira, C., & Surico, P. (2020). Monetary policy when households have debt: new evidence on the transmission mechanism. The Review of Economic Studies, 87(1), 102-129.

De Nardi, M. (2004). Wealth inequality and intergenerational links. The Review of Economic Studies, 71(3), 743-768.

De Nardi, M., French, E., & Jones, J. B. (2010). Why do the elderly save? The role of medical expenses. Journal of Political Economy, 118(1), 39-75.

IMF. (2017). 2015 Refinements to the External Balance Assessment Methodology. Retrieved on March 27, 2026.

Jappelli, T., & Pistaferri, L. (2014). Fiscal policy and MPC heterogeneity. American Economic Journal: Macroeconomics, 6(4), 107-136.

Masson, P. R., Bayoumi, T., & Samiei, H. (1998). International evidence on the determinants of private saving. The World Bank Economic Review, 12(3), 483-501.

Mian, A., Sufi, A., & Verner, E. (2017). Household debt and business cycles worldwide. The Quarterly Journal of Economics, 132(4), 1755-1817.

Qureshi, M. (2016). Singapore's 2016 Article IV Selected Issues paper. What drives private savings in Singapore.

Yoo, J. (2021). Singapore's 2021 Article IV Selected Issues paper. Household consumption dynamics around shocks.
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
