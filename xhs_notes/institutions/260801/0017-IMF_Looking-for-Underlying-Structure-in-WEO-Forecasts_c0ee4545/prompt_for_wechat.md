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
# Looking for Underlying Structure in WEO Forecasts

Yurii Sholomytskyi

WP/26/164

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/dfea5f848bd6acd835e36beab01ca51eca372225732b7932b9fdb7afac325f16.jpg)

# IMF Working Paper Institute for Capacity Development

# Looking for Underlying Structure in WEO Forecasts

Prepared by Yurii Sholomytskyi

Authorized for distribution by Ali Alichi
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management. The views expressed herein are those of the author and should not be attributed to the IMF, its Executive Board, or its management.

ABSTRACT: This paper examines the statistical properties of the IMF's World Economic Outlook (WEO) projections over 1999–2023 for 29 economies. The optimism of WEO growth forecasts is well established; we confirm it and look behind it at two features of how the forecasts are built. First, the growth of the systemic economies (the United States and China) appears to be underutilized in the projections: forecasts embed less of the cross-country growth comovement present in the data, a gap we term forecast fragmentation that did not narrow over the sample. Second, the conditional growth-inflation link present in the historical data is weakly represented in the projections. These patterns suggest that structural models, in which such cross-country and real-nominal linkages can be verified through estimation, could be a useful complement to expert judgment, serving as a baseline check for medium-term anchors.

RECOMMENDED CITATION: Sholomytskyi, Y. (2026). “Looking for Underlying Structure in WEO Forecasts.” IMF Working Paper WP/26/164, International Monetary Fund.

<table><tr><td>JEL Classification Numbers:</td><td>C53, E37, F33, F47</td></tr><tr><td>Keywords:</td><td>IMF; World Economic Outlook; Forecast error; Optimism bias; Forecast fragmentation</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>ysholomytskyi@imf.org</td></tr></table>

WORKING PAPERS

# Looking for Underlying Structure in WEO Forecasts

Prepared by Yurii Sholomytskyi

## Contents

Glossary 2   
I. Introduction 3   
II. Literature review 4   
III. Empirical strategy 5   
A. Data construction and horizon selection 5   
B. Testing for inertia and optimism 6   
C. Testing for spillovers and synchronization 8   
D. Testing for model coherence 8   
IV. Empirical results 9   
A. Structural optimism vs. historical inertia 9   
B. Long-run steady state bias 10   
C. The anatomy of optimism: level versus timing 11   
D. Spillovers and forecast fragmentation 12   
E. Model coherence and information use 13   
F. Evolution of forecast performance over time 15   
V. Conclusion 16   
References 18   
A Detailed statistical results 19   
A.I Structural optimism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.II Spillovers and synchronization 20   
A.III Inflation-GDP coupling 23   
A.IV Error decomposition 24   
A.V The reality check 24   
A.VI Counterfactual benchmark 24   
A.VII Forecast bias statistics 25   
A.VIII Evolution of forecast performance 27   
A.IX Robustness checks 29   
B Data and sample 31   
B.I Variable definitions 31   
B.II Sample composition 31

## Glossary

BVAR Bayesian Vector Autoregression
DSGE Dynamic Stochastic General Equilibrium
GDP Gross Domestic Product
GPM Global Projection Model
HP Hodrick–Prescott filter
IMF International Monetary Fund
MG Mean Group (estimator)
MONA Monitoring of Fund Arrangements (database)
OECD Organisation for Economic Cooperation and Development
PCA Principal Component Analysis
PCPI Consumer Price Index
RMSE Root Mean Square Error
VAR Vector Autoregression
WEO World Economic Outlook

## I. Introduction

Governments, markets, and the IMF itself rely on the Fund's macroeconomic projections to inform policy and to frame the global outlook. Because of the Fund's role in surveillance and stabilization, the precision of these projections bears directly on debt sustainability analysis and fiscal planning across its membership.

That WEO projections deviate systematically from subsequent outcomes, most visibly through a tendency to over-predict growth, is well documented; their causes are less settled. Do forecast errors reflect institutional memory, with projections anchored to historical averages? Do they reflect a structural optimism that persists independently of the business cycle? And how far are they shaped by a top-down global narrative, as opposed to factors specific to individual country desks?

This paper takes up these questions with WEO vintages from 1999 to 2023, decomposing forecast errors into components tied to historical trends and global factors. The optimism of WEO growth forecasts is by now well documented; we confirm it and locate its source, and take it as the point of departure for our two main results, which concern features the accuracy-focused literature has left largely unexamined: how forecasts propagate global spillovers, and whether they preserve the structural link between growth and inflation.

We confirm that growth forecasts are persistently optimistic and, beyond the known bias, show that the optimism is a level bias rather than a by-product of the forecast's deviation from recent history. In a panel that controls for country-specific effects, forecasts exceed realized growth by about half a percentage point on average. The bias is unconditional: it holds whether the initial forecast stance was optimistic or pessimistic relative to the country's recent history, and the size of a forecast's departure from that history carries no predictive power for the eventual error. Forecasters do lean on recent history in setting the medium-term level, but that anchoring does not generate the optimism, which is present across the cyclical positions a country may occupy relative to its own past.

First, the projections carry the growth spillovers from the systemic economies only partially – a gap we term forecast fragmentation. Our primary evidence is a direct comparison of loadings: the average country's growth moves with US growth by 0.84 point-for-point in the data but only 0.34 in the forecasts, so the projections embed under half of the US spillover, and the China loading is understated too; both shortfalls are statistically significant. The US shortfall does not narrow over the sample – the forecasts captured about two-thirds of the US spillover before 2010 and well under half after, even as the Fund adopted more global models; the larger post-2010 shortfall is amplified by the pandemic spike in realized comovement, but the under-capture is present in the calm pre-pandemic 2010s too, where the forecasts embed almost none of it. Two further measures point the same way: a single global factor explains about 61 percent of the cross-country variance in realized growth against about 45 percent in the forecasts, and forecast errors remain correlated with realized US growth—the latter on the verge of conventional significance despite the few year-level clusters. Both corroborate

the spillover-loading result.

Second, the paper examines the structural consistency of the projections. A forecast is a conditional mean, so the unpredictable supply shocks that flatten the realized growth-inflation correlation are mostly absent from it, leaving the predictable demand-side comovement; an internally consistent forecast should therefore reproduce the positive conditional relationship in the data. The conditional growth-inflation slope within the forecasts is instead essentially flat, in contrast to the positive structural link present in the data, pointing to a disconnection between the real and nominal sides of the projections.

The remainder of the paper is organized as follows. Section II reviews the relevant literature on forecast evaluation and behavioral patterns; Section III details the data construction and econometric framework; Section IV presents the empirical results; and Section V concludes with policy implications.

## II. Literature review

The evaluation of multilateral forecasts has produced a large literature on systematic biases. Timmermann (2007) provides a foundational analysis of the WEO, noting that forecasts meet basic quality standards yet systematically overpredict real GDP growth. He also observes that countries with the largest output gaps are overpredicted most, pointing to flaws in the estimation of potential output and long-run trends.

Celasun, Lee, Mrkaic, and Timmermann (2021) update the evaluation for 2004–2017. Short-term WEO forecasts are accurate and largely unbiased, while two- to five-year-ahead projections remain upward-biased and often underperform a naïve historical average. They also document that country-level errors are correlated with errors in projecting external factors, such as the terms of trade and growth in the United States and China, suggesting scope to incorporate global information more fully across country projections.

Other work isolates the mechanisms behind these biases. Hellwig (2018) studies overfitting, showing that longer-term forecasts revert to the mean too slowly, a tendency to read short-term upswings as structural improvements. Carriere-Swallow and Marzluf (2023) trace forecast errors, especially in IMF-supported programs, to excessive optimism about the effects of policy adjustment, arguing that an incomplete account of macro-financial feedback overstates the gains from stabilization.

Tsuchiya (2023) examines World Bank growth forecasts for 130 countries between 1999 and 2019. Performance improved after the 2008–09 crisis and current-year forecasts are mostly unbiased, but next-year forecasts shifted from conservative to optimistic after the crisis. The degree of optimism is not closely tied to region or income level, which suggests the bias is built into the modeling process itself.

Comparisons of the IMF and the OECD show closely synchronized forecasts. Lewis and Pain (2014) find that OECD and IMF errors are highly correlated during global shocks such as the Great Financial Crisis, so both institutions miss cyclical turning points together. Eicher et al. (2019) evaluate

IMF forecasts in crises using the MONA database: the forecasts outperform naive approaches and add information, yet about two-thirds of the variables they examine fail standard tests of forecast efficiency, with the biases in growth, investment, and government expenditure most pronounced in low-income countries.

At the European Central Bank, Kontogeorgos and Lambrias (2019) find that staff projections outperform naive models but show persistent errors during recoveries, echoing the inertia found in WEO evaluations, where forecasters stay anchored to pre-shock trajectories even after a structural break.

This paper extends that literature beyond point-forecast accuracy to the structure and internal coherence of multilateral projections, in four ways. First, we measure how far forecasts carry US and China spillovers to other countries, and summarize the resulting cross-country comovement with a principal-component synchronization gap. Second, we decompose the optimism bias to separate errors in the speed of cyclical recovery from errors in long-term trends. Third, using a Bayesian VAR benchmark, we show that the forecasts anchor the real and nominal sides (GDP and inflation) independently, in contrast to the equilibrium relationship in the historical data. Fourth, by extending the evaluation to 2023, we cover the post-pandemic inflation surge and the shift in inflation-forecasting behavior that came with it.

## III. Empirical strategy

The empirical approach exploits the panel structure of WEO vintages to decompose forecast errors along three dimensions: the nature of the bias, the structure of the error (temporal and spatial), and the coherence of the model. We test three hypotheses:

1. Nature of bias: whether errors are driven by inertia (anchoring to historical averages) or by an unconditional positive bias (optimism).

2. Anatomy of error: Whether the source of this bias is temporal (misjudging trends vs. cycles) or spatial (synchronized global errors vs. idiosyncratic errors).

3. Structural coherence: Whether forecasts exhibit internal consistency between real and nominal variables (inflation-growth coupling) compared to mechanical benchmarks.

## A. Data construction and horizon selection

We construct a database of World Economic Outlook (WEO) vintages spanning 1999 to 2023. For each country i and vintage v, we extract the forecasted path for real GDP growth $y^{F}$ and inflation $\pi^{F}$ over the projection horizon $h = 0, \ldots, 5$ (the current-year nowcast through the five-years-ahead terminal that the WEO reports). The accuracy and synchronization metrics use the sub-windows defined below, while the medium-term anchor of Section IV.B uses the terminal five-years-ahead forecast $v + 5$ .

We compare results across two forecast horizons to separate the effects of recent global shocks from long-term institutional trends:

\- The 3-year horizon ( $h \leq 2$ ): This recovery-inclusive sample lets us include the most recent vintages (2021–2023). Because the realized data end in 2023, these vintages can only be evaluated over shorter windows. The sample captures the post-COVID recovery and the 2022 energy shock, which weigh heavily on the synchronization measures.

\- The 5-year horizon ( $h \leq 4$ ): This is the institutional medium-term standard. A five-year evaluation needs realized data through 2028, so the sample is restricted to vintages released before 2019. It serves as a benchmark for normal cyclical fluctuations, excluding the unusual synchronization of the early 2020s.

To match the information set available to forecasters, we separate historical data visible at vintage v from forecast data. Realized outcomes $(y^{A})$ are defined using the January 2024 vintage, providing a consistent benchmark that incorporates subsequent data revisions. Because actuals are drawn from a single recent vintage, measured forecast errors embed subsequent data revisions as well as genuine forecast misses; this is standard in the WEO-evaluation literature, but it implies that errors at longer horizons partly reflect revision noise.

## B. Testing for inertia and optimism

To determine whether forecast errors reflect a reluctance to deviate from historical trends (inertia) or an unconditional bias (optimism), we estimate the following panel fixed-effects model:

$$
E _ {i, v} = \alpha + \gamma_ {i} + \beta D _ {i, v} + \varepsilon_ {i, v}\tag{1}
$$

where $E_{i,v} = y_{i,v}^{A} - y_{i,v}^{F}$ represents the forecast error (with a negative value indicating over-prediction) $\alpha$ is the common intercept, and $\gamma_i$ are country fixed effects. The key explanatory variable, $D_{i,v}$ , measures the deviation of the forecast from the country's recent history. Specifically, $D_{i,v} = \bar{y}_{i,v}^{F} - \bar{y}_{i,v}^{H}$ , where $\bar{y}^F$ is the average forecasted growth over the projection horizon and $\bar{y}^H$ is the average realized growth over the preceding five years.

Country fixed effects ( $\gamma_{i}$ ) isolate within-country variation, so the estimates are not confounded by permanent cross-country differences in potential growth (for example, emerging versus advanced economies). This is the advantage of the panel over a pooled regression. As a robustness check against common global shocks, we also report a specification that augments Equation (1) with year effects, and one that splits the sample by income group (Appendix Table 13).

Figure 1 aggregates the implied medium-term anchors (the forecast five years beyond the current year, $v + 5$ , the longest horizon the WEO reports) across all countries in our sample and sets them against a trailing average of recent realized history and the eventual realized outcome.

The figure shows two features. First, the global median anchor (solid blue) tracks the real-time trailing mean of recent inflation and growth (orange) closely: the institution's implied long-run view is, in effect, recent realized history extended forward. Second, that anchor moves little relative to the realized outcome (red), which swings through the 2009 and 2020 recessions and the post-2020 inflation surge; the forecasts neither lead nor match these turns. We return to this long-run level below, where the growth optimism turns out to sit in the level of the projected recovery, not in its year-to-year shape.

Anchor stability vs fundamentals: GDP Growth  
![](images/74fca3fb275eafc2d3db9d9a0d486fb73b6d06e3ca107d6029375aeaa1bf8bce.jpg)

![](images/1d1b2889ff8f90f432263858fb159be7ea7651fee839530511b95d1ddcc258d5.jpg)  
Figure 1: Stability of medium-term anchors over time. The grey dots are individual country medium-term forecasts (five years ahead, $v+5$ ) and the shaded band their interquartile range; the solid blue line is the global median anchor; the orange line is the global real-time trend (a 10-year trailing mean of realized history); the red line is the realized outcome, plotted at its target calendar year.

The interpretation of the regression coefficients is as follows:

\- If forecast errors are driven by inertia, we would expect $\beta > 0$ . This would imply that when forecasters predict growth above the historical trend ( $D > 0$ ), they are still under-reacting to a structural improvement, leading to a positive forecast error (reality exceeds the forecast).

\- If forecast errors reflect conditional optimism, we expect $\beta < 0$ . This would imply that deviations from history are generally unfounded, leading to larger negative errors when forecasts are optimistic.

\- If the bias is structural, we expect a significant common intercept $\alpha < 0$ (indicating a persistent over-prediction across all countries) combined with an insignificant $\beta$ , suggesting the bias exists regardless of the cyclical position relative to history.

## C. Testing for spillovers and synchronization

We measure forecast synchronization and its drivers in two steps. First, we compute the share of varia

[中间内容因长度限制已省略]

teral trade). This measure explains more of a country's growth than the US factor alone (54 versus 40 percent in the data), and the forecasts carry less of this genuine trade channel too (44 versus 54 percent), so the synchronization gap does not stem from summarizing the common cycle by the US and China (Panel C).

Coherence under cleaner identification. Following McLeay and Tenreyro (2020), we restrict the coherence test to credible inflation targeters, where monetary policy offsets demand shocks and the growth-inflation link is more cleanly identified. The contrast is unchanged: the data slope stays near 0.13 and the within-forecast slope near zero (Table 14).

Table 14: Spillover Content and Coherence Robustness

<table><tr><td colspan="3">Panel A: first principal component regressed on US and China growth</td></tr><tr><td></td><td>Realized</td><td>Forecast</td></tr><tr><td> $R^2$  (US, China explain the factor)</td><td>0.80</td><td>0.50</td></tr><tr><td>Loading on US growth</td><td>4.98</td><td>1.21</td></tr><tr><td>Loading on China growth</td><td>1.93</td><td>1.75</td></tr></table>

Panel B: coherence test, inflation-targeting subsample (n = 14)

<table><tr><td></td><td>IT sample</td><td>Full sample</td></tr><tr><td>Data BVAR slope  $\beta_{GDP\rightarrow\pi}$ </td><td>0.126</td><td>0.135</td></tr><tr><td>Within-forecast conditional slope</td><td>0.009</td><td>-0.016</td></tr></table>

Panel C: mean variance share explained (US factor vs. trade-weighted partners)

<table><tr><td></td><td>Realized</td><td>Forecast</td></tr><tr><td>Mean  $R^{2}$  from US growth</td><td>0.40</td><td>0.24</td></tr><tr><td>Mean  $R^{2}$  from trade-weighted partner growth</td><td>0.54</td><td>0.44</td></tr></table>

Note: Panel A regresses the first principal-component score of growth levels (target year × country, $h \leq 4$ for forecasts) on US and China growth. Panel B re-estimates the data BVAR slope and the within-forecast conditional slope of Section IV.E on the 14 credible inflation-targeting economies in the sample (Australia, Brazil, Canada, Chile, the United Kingdom, Indonesia, India, Mexico, New Zealand, Peru, the Philippines, Sweden, the United States, and South Africa). Panel C reports the mean (across the 28 non-US economies) $R^{2}$ from regressing each country's growth on US growth, and separately on its own trade-weighted partner growth (export-share weights from IMF IMTS bilateral trade, averaged 2000–2019 over the 29-economy set); higher for trade-weighted partners in both the data and the forecasts, and lower in the forecasts for both regressors.

## B Data and sample

## B.I Variable definitions

\- GDP Growth (NGDP\_R): Gross domestic product, constant prices (Percent change). Sourced from WEO Database variable NGDP\_R.

\- Inflation (PCPI): Inflation, average consumer prices (Percent change). Sourced from WEO Database variable PCPI.

\- WEO Vintages: All semi-annual (Spring/Fall) and available quarterly updates from 1999 to 2023.

## B.II Sample composition

The sample covers 29 economies selected to ensure broad geographic and income-level coverage, spanning advanced, emerging, and developing countries across all major regions. These economies

are among the most intensively covered in the WEO process, typically benefiting from dedicated country teams with substantial analytical resources. The findings therefore represent a conservative assessment: if systematic biases persist in forecasts for these well-resourced cases, they are likely at least as pronounced for the broader membership.

<table><tr><td>ISO Code</td><td>Country Name</td><td>Region</td></tr><tr><td>ARM</td><td>Armenia</td><td>Middle East &amp; Central Asia</td></tr><tr><td>AUS</td><td>Australia</td><td>Advanced Economies</td></tr><tr><td>BRA</td><td>Brazil</td><td>Latin America &amp; Caribbean</td></tr><tr><td>CAN</td><td>Canada</td><td>Advanced Economies</td></tr><tr><td>CHL</td><td>Chile</td><td>Latin America &amp; Caribbean</td></tr><tr><td>CHN</td><td>China</td><td>Emerging &amp; Developing Asia</td></tr><tr><td>DEU</td><td>Germany</td><td>Advanced Economies</td></tr><tr><td>DOM</td><td>Dominican Republic</td><td>Latin America &amp; Caribbean</td></tr><tr><td>EGY</td><td>Egypt</td><td>Middle East &amp; Central Asia</td></tr><tr><td>FRA</td><td>France</td><td>Advanced Economies</td></tr><tr><td>GBR</td><td>United Kingdom</td><td>Advanced Economies</td></tr><tr><td>HND</td><td>Honduras</td><td>Latin America &amp; Caribbean</td></tr><tr><td>IDN</td><td>Indonesia</td><td>Emerging &amp; Developing Asia</td></tr><tr><td>IND</td><td>India</td><td>Emerging &amp; Developing Asia</td></tr><tr><td>ITA</td><td>Italy</td><td>Advanced Economies</td></tr><tr><td>JPN</td><td>Japan</td><td>Advanced Economies</td></tr><tr><td>MEX</td><td>Mexico</td><td>Latin America &amp; Caribbean</td></tr><tr><td>MYS</td><td>Malaysia</td><td>Emerging &amp; Developing Asia</td></tr><tr><td>NZL</td><td>New Zealand</td><td>Advanced Economies</td></tr><tr><td>OMN</td><td>Oman</td><td>Middle East &amp; Central Asia</td></tr><tr><td>PAK</td><td>Pakistan</td><td>Middle East &amp; Central Asia</td></tr><tr><td>PER</td><td>Peru</td><td>Latin America &amp; Caribbean</td></tr><tr><td>PHL</td><td>Philippines</td><td>Emerging &amp; Developing Asia</td></tr><tr><td>SGP</td><td>Singapore</td><td>Advanced Economies</td></tr><tr><td>SWE</td><td>Sweden</td><td>Advanced Economies</td></tr><tr><td>TZA</td><td>Tanzania</td><td>Sub-Saharan Africa</td></tr><tr><td>USA</td><td>United States</td><td>Advanced Economies</td></tr><tr><td>VNM</td><td>Vietnam</td><td>Emerging &amp; Developing Asia</td></tr><tr><td>ZAF</td><td>South Africa</td><td>Sub-Saharan Africa</td></tr></table>

# PUBLICATIONS
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
