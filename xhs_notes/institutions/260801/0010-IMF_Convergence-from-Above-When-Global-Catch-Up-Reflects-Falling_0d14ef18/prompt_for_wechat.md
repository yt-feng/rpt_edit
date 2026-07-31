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
# Convergence from Above: When Global Catch-Up Reflects Falling Back

Patrick A. Imam

WP/26/159

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/d3207bebb70983be16cc15f44a4009a88c9e670c62355ed04213f1ca9a87be03.jpg)

# IMF Working Paper Institute for Capacity Development

# Convergence from Above: When Global Catch-Up Reflects Falling Back

Prepared by Patrick A. Imam\*

Authorized for distribution by Ali Alichi

July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Convergence is usually interpreted as evidence of catch-up: poorer economies grow faster because they are moving toward richer ones. This paper argues that the same empirical pattern can arise from a different source. If country-specific long-run trajectories shift over time, narrowing income gaps may reflect not only upward movement from below, but also adjustment from above. We develop a framework in which economies converge toward evolving rather than fixed steady-state paths, and construct empirical proxies for these paths using cross-country data. Economies above their predicted trajectories subsequently grow more slowly and are more likely to move downward within the world income distribution. Supporting evidence links positive overshooting to selected downside-adjustment episodes, especially banking-sector distress and loss of frontier position. The evidence suggests that observed convergence partly reflects compression from the top, not only catch-up from below.

RECOMMENDED CITATION: Imam, Patrick A. 2026. “Convergence from Above: When Global Catch-Up Reflects Falling Back.” IMF Working Paper No. 26/159, International Monetary Fund, Washington, DC.

JEL Classification Numbers:

O11, O47, O57, F43, E13

Keywords:

Convergence; Relative Decline; Macroeconomic Fragility; Distribution Dynamics; Steady States; Structural Transformation

Author's E-Mail Address:

pimam@imf.org

WORKING PAPERS

# Convergence from Above: When Global Catch-Up Reflects Falling Back

Prepared by Patrick A. Imam

## Contents

I. Introduction......3
II. Motivating Facts: Convergence, Stagnation, and Falling Back......6
III. A Model of Convergence with Moving Steady States......8
IV. Empirical Framework and Results......12
V. Convergence, Fragility, and Distribution Dynamics......24
VI. Conclusion......25
References......26
Appendix A. Dynamic Convergence with Moving Steady States......28
Appendix B: Supplementary Empirical Results and Robustness Analysis......33

## I. Introduction

One of the most influential ideas in economics is that poor countries should grow faster than rich ones. Since Solow (1956), the negative relationship between initial income and subsequent growth has generally been interpreted as evidence of catch-up. Economies below their long-run potential accumulate capital, adopt existing technologies, and gradually narrow income gaps with richer economies. In this interpretation, convergence is more than a statistical regularity. It is often taken as a broad measure of development progress itself.

Yet the historical evidence has never sat entirely comfortably with such a simple interpretation. Growth paths are not smooth escalators. Countries advance, stall, reverse, and sometimes spend decades moving sideways. Pritchett's (1997) phrase “divergence, big time” captured one side of this instability. The recent return of unconditional convergence, emphasized by Kremer, Willis, and You (2021) and Patel, Sandefur, and Subramanian (2021), captures another. But the coexistence of these facts raises a deeper question. If convergence has returned, what kind of convergence is it? A negative relationship between initial income and subsequent growth does not tell us whether poorer economies are rising or richer economies are falling back.

The world economy over the last half century presents two facts that are usually discussed separately. On the one hand, convergence appears alive. Many poorer economies, especially in East and Southeast Asia, have grown rapidly relative to the industrial frontier, and cross-country income gaps have narrowed in important dimensions. On the other hand, several advanced economies have entered prolonged periods of stagnation, relative decline, or repeated downward revision in long-run growth expectations. Japan after the early 1990s, parts of Europe after the euro-area crisis, and more recently economies such as Germany and Finland all point toward a common phenomenon. Economies that previously sustained relatively high-income levels increasingly struggle to maintain earlier growth trajectories. Similar though distinct patterns can also be observed across parts of the middle-income world, particularly in Latin America, where repeated episodes of stalled convergence and recurrent “lost decades” have interrupted earlier expectations of sustained catch-up.

The standard interpretation is that these developments simply offset one another. Poorer economies catch up while richer economies slow naturally near the frontier. But this interpretation misses a more basic ambiguity. It tells us only that initially richer economies grow more slowly. That pattern may reflect successful catch-up from below. It may also reflect something quite different. Economies whose relative income levels appear high compared with those implied by current fundamentals may gradually adjust toward lower long-run paths.

Economists have long focused on how poor countries catch up; much less attention has been paid to the possibility that some rich countries may, quietly and gradually, fall back. This paper develops a framework for analyzing this second mechanism. “Convergence from above” $^{1}$ is not meant to describe ordinary slow growth among rich countries. It refers to a specific dynamic. An economy lies above the income level implied by its current fundamentals, and subsequent growth is weak because the economy is adjusting toward that lower benchmark.

The mechanism studied here is distinct from three related ideas. It is not simply beta-convergence, since two economies with the same initial income may differ in their position relative to the trajectory implied by current fundamentals. It is not primarily a convergence-club argument, since the emphasis is not on assigning countries to fixed long-run regimes, but on allowing country-specific trajectories to move over time. Nor is it merely a boom-bust story. Some episodes of overshooting may indeed reflect temporary booms, favorable

terms-of-trade movements, or credit expansions. But the mechanism of interest is broader: economies may move above their long-run trajectory because the benchmark itself has weakened.

The central idea is simple. Standard growth models describe economies converging toward steady states determined by productivity, demographics, investment, and human capital. But steady states are not fixed objects. Productivity growth weakens, demographic structures deteriorate, industrial composition changes, technologies diffuse unevenly, and economies may become less effective at using existing technologies. When these shifts occur, the level of income consistent with long-run equilibrium can decline. An economy can therefore become “too rich” relative to its fundamentals even if actual income does not rise. In practice, the adjustment often first appears not through crisis, but through repeated downward revisions in expectations about future productivity and long-run growth.

Such dynamics are less historically unusual than the standard convergence narrative sometimes suggests. Macroeconomists routinely reason in this way elsewhere. Housing markets appear expensive because local fundamentals weaken rather than because prices rise. Potential output is revised downward after persistent stagnation. In each case, the observed level remains temporarily high because the benchmark has moved. This paper applies the same logic to cross-country income dynamics.

The argument developed here is therefore narrower than it may first appear. The paper does not suggest that all stagnation reflects convergence from above, nor that slower growth among richer economies explains convergence more generally. Rather, the claim is that observed convergence may reflect two conceptually distinct processes simultaneously: upward mobility from below and downward adjustment from above. The convergence literature has overwhelmingly emphasized the first mechanism, even though the second may also be quantitatively relevant for understanding the evolution of the world income distribution.

The central issue is therefore not whether convergence occurs, but whether convergence itself has been systematically misread. To address this question, the paper develops an extension of the neoclassical growth framework in which steady-state paths evolve over time. Relative to earlier work on asymmetric convergence dynamics, the novelty is not simply that adjustment differs above and below the steady state. It is that economies may systematically enter the above-steady-state region because the steady-state path itself shifts downward.

The framework clarifies why standard convergence regressions may combine conceptually distinct forms of adjustment. The empirical analysis follows directly from these implications. We estimate country-specific steady-state paths as functions of investment, demographics, and human capital; construct an overshooting measure given by the gap between actual income and predicted steady-state income; and examine how this gap predicts subsequent growth and transition probabilities within the world income distribution. The overshooting gap is not interpreted as a direct observation of the true steady state. It is a disciplined empirical proxy for the distance between observed income and the income level implied by a parsimonious set of long-run fundamentals. The empirical question is whether this gap contains information about subsequent growth and relative mobility beyond that contained in initial income alone.

The distributional analysis is central. Following Quah (1993, 1996), convergence is treated as a statement about movements within the full cross-country distribution, not merely the sign of a coefficient in a growth regression. This distinction matters because similar convergence coefficients may arise from very different underlying processes. A world in which poorer economies move upward is economically different from one in which the upper tail of the distribution compresses because previously successful economies fail to sustain earlier trajectories.

The empirical results support the existence of convergence from above. Economies above their predicted long-run trajectories subsequently experience weaker growth, while adjustment from above appears slower and more persistent than convergence from below. In our preferred accounting exercise, compression near the top accounts for a material share of observed convergence, with a point estimate close to one-third over the full 1960–2019 sample.

The paper contributes to the convergence literature associated with Barro and Sala-i-Martin (1992), Mankiw, Romer, and Weil (1992), and Durlauf, Johnson, and Temple (2005) by distinguishing convergence from below and convergence from above. It also relates to Quah's (1993, 1996) distribution-dynamics approach and to work emphasizing instability and discontinuity in long-run growth experience, including Pritchett (1997) and Johnson and Papageorgiou (2020). The paper is also related to work on resource-based overshooting, convergence clubs, and multiple steady states, but differs in its emphasis on evolving country-specific trajectories and on the possibility that upward and downward adjustment coexist within measured convergence itself.

The policy relevance is immediate. Weak growth may reflect temporary cyclical weakness, temporary adjustment after a boom, or movement toward a lower long-run trajectory. Distinguishing between these cases matters for forecasting, debt sustainability analysis, and assessments of medium-term potential. The broader implication is simple. Convergence may reflect progress at the bottom, decline at the top, or both. The purpose of this paper is to distinguish these mechanisms and to show that doing so changes how we interpret global development.

The remainder of the paper proceeds as follows. Section II presents motivating facts on convergence, stagnation, and relative decline. Section III develops a model of convergence with moving steady-state paths. Section IV constructs empirical proxies for long-run trajectories, estimates the dynamics of adjustment, and uses an accounting exercise to distinguish the contributions of catch-up from below and compression from above. Section V discusses implications for convergence, fragility, and global development dynamics. Section VI concludes.

## II. Motivating Facts: Convergence, Stagnation, and Falling Back

The return of convergence has been among the most consequential developments in the modern world economy. After decades in which divergence frequently appeared the more natural description of global development, many poorer economies have grown faster than richer ones since the early 1990s. Kremer, Willis, and You (2021) document a broad revival of unconditional convergence, while Patel, Sandefur, and Subramanian (2021) suggest that the extent of catch-up is historically unusual in both scale and breadth.

Viewed in isolation, these findings appear reassuring. Standard growth theory predicts that economies below the frontier should grow rapidly through capital accumulation, structural transformation, and technology diffusion. Yet the broader macroeconomic landscape of the same period looks considerably less straightforward. The decades that witnessed renewed convergence also produced prolonged stagnation, repeated downward revisions in estimates of potential growth, and persistent productivity slowdowns across parts of the advanced and middle-income world. Japan remains the clearest case. Following one of the most successful convergence episodes in modern economic history, growth slowed sharply after the early 1990s and never returned to earlier rates. Hayashi and Prescott (2002), Summers (2014), and Gordon (2016), among others, increasingly interpreted the slowdown not as a temporary cyclical interruption, but as evidence of deeper structural weakness linked to demographics, productivity, investment, and declining dynamism.

Comparable patterns emerged elsewhere through different channels. Southern Europe experienced prolonged stagnation after the euro-area crisis despite earlier expectations of continued convergence within Europe. In the United Kingdom, weak productivity growth after the global financial crisis became sufficiently persistent that concern gradually shifted away from cyclical recovery toward the possibility that underlying productive capacity itself had weakened. Haldane (2017) described the productivity slowdown as one of the defining macroeconomic puzzles of the post-crisis era. More recently, concerns about Germany and Finland have reflected a similar pattern: not a sudden collapse, but a gradual weakening of the growth model that previously supported high relative income levels.

Nor is the phenomenon confined to advanced economies. Latin America's recurrent “lost decades” revealed how periods of temporarily favorable external conditions could sustain income levels that later proved difficult to maintain. Rodríguez and Sachs (1999), studying resource-rich economies, explicitly describe cases in which economies converge “from above” after overshooting relative to lower steady states. Rodrik (2016) argues that premature deindustrialization may weaken one of the principal historical mechanisms through which economies converged toward the frontier. These episodes differ in their proximate causes. Some involve demographic aging, others commodity dependence, weak diffusion, declining industrial dynamism, institutional rigidities, financial excess, or persistent productivity weakness. What links them is less obvious but potentially more important: in each case, expectations about sustainable long-run performance appear to shift downward over time. The issue is not simply that countries sometimes grow slowly. It is that the benchmark against which their income levels should be assessed may itself have moved.

These examples are illustrative. They show why the mechanism is plausible, but they do not establish it. The formal analysis below therefore uses the full cross-country panel to ask whether economies above estimated long-run trajectories subsequently display weaker growth and whether descriptive distributional evidence is consistent with greater downward mobility within the world income distribution.

This feature is difficult to reconcile with interpretations of convergence that implicitly treat steady states as relatively stable objects. Temporary recessions are entirely consistent with standard growth theory. Repeated downward revisions in estimates of potential growth are conceptually different. Fernald, Inklaar, and Ruzic (2025), for example, argue that the advanced-economy productivity slowdown reflects broad and persistent forces rather than temporary post-crisis weakness. More recent debates on secular stagnation and slowing productivity growth similarly emphasize that medium-term growth expectations and estimates of potential output may shift persistently over time rather than reverting automatically toward earlier trends (Summers 2014; Gordon 2016).

A striking feature of modern development experience is therefore not simply that growth rates differ across countries, but that growth trajectories themselves appear unstable. Economies advance, stall, reverse, and sometimes spend decades adjusting to weaker paths than previously anticipated. Pritchett (1997) emphasized that discontinuity and divergence are central features of modern growth experience rather than peripheral anomalies. Johnson and Papageorgiou (2020) similarly argue that cross-country growth dynamics display substantially greater instability and heterogeneity than conventional converg

[中间内容因长度限制已省略]

0s</td><td>370</td><td>33</td><td>28</td><td>14</td><td>95</td></tr><tr><td>2010s</td><td>370</td><td>6</td><td>28</td><td>11</td><td>83</td></tr></table>

Note. Banking-crisis and downside-risk episode counts. Source: Global Macro Database crisis chronologies. Counts refer to event onsets. Country-periods already within the relevant event are excluded from the event-specific risk set. The number of at-risk observations may therefore differ across outcomes.

Table A7. Descriptive dynamic response profile around the initial trajectory gap

<table><tr><td>h (years)</td><td> $\beta^{+} (\omega_{\text{pos}})$ </td><td>(SE)</td><td> $\beta^{-} (\omega_{\text{neg}})$ </td><td>(SE neg)</td><td>N</td></tr><tr><td>-3</td><td>+0.8450***</td><td>(0.0374)</td><td>+0.7039***</td><td>(0.0527)</td><td>7417</td></tr><tr><td>-2</td><td>+0.6168***</td><td>(0.0209)</td><td>+0.5439***</td><td>(0.0310)</td><td>7495</td></tr><tr><td>-1</td><td>+0.3470***</td><td>(0.0168)</td><td>+0.3248***</td><td>(0.0129)</td><td>7573</td></tr><tr><td>1</td><td>-0.0998***</td><td>(0.0259)</td><td>-0.1037***</td><td>(0.0183)</td><td>7648</td></tr><tr><td>2</td><td>-0.2030***</td><td>(0.0505)</td><td>-0.1875***</td><td>(0.0303)</td><td>7648</td></tr><tr><td>3</td><td>-0.2810***</td><td>(0.0723)</td><td>-0.2641***</td><td>(0.0470)</td><td>7648</td></tr><tr><td>5</td><td>-0.3670***</td><td>(0.0884)</td><td>-0.3244***</td><td>(0.0673)</td><td>7503</td></tr><tr><td>7</td><td>-0.4079***</td><td>(0.0796)</td><td>-0.3466***</td><td>(0.0877)</td><td>7213</td></tr><tr><td>10</td><td>-0.3783***</td><td>(0.1210)</td><td>-0.3041***</td><td>(0.1032)</td><td>6778</td></tr><tr><td>15</td><td>-0.2742**</td><td>(0.1084)</td><td>-0.2060**</td><td>(0.1036)</td><td>6053</td></tr></table>

Note. Local-projection coefficients at horizons $h = 1 \ldots 5$ . Country and period fixed effects; Driscoll-Kraay standard errors.

Table A8. Whole-pipeline country-bootstrap inference.

<table><tr><td>Coefficient</td><td>Point estimate</td><td>Bootstrap SE</td><td>95% CI lo</td><td>95% CI hi</td><td>p (boot, two-sided)</td><td>N</td></tr><tr><td> $\beta(\omega < 0)$  catch-up slope</td><td>-0.0760</td><td>0.0201</td><td>-0.1180</td><td>-0.0393</td><td>0.0000</td><td>1387</td></tr><tr><td> $\beta(\omega \geq 0)$  adjustment-from-above slope</td><td>-0.0419</td><td>0.0187</td><td>-0.0772</td><td>-0.0071</td><td>0.0133</td><td>1387</td></tr><tr><td>Asymmetry:  $\beta(\omega \geq 0) - \beta(\omega < 0)$ </td><td>+0.0340</td><td>0.0304</td><td>-0.0226</td><td>+0.0914</td><td>0.2667</td><td>1387</td></tr></table>

Note. Complete countries are resampled with replacement. Within each replication, the first-stage trajectory equation is re-estimated, the trajectory gap and its positive and negative components are reconstructed, and the second-stage growth regression is re-estimated.

Table A9. Robustness — quantile regressions for $\omega^{+}$ and $\omega^{-}$ .

<table><tr><td>Quantile τ</td><td>β(ω&lt;0)</td><td>(SE)</td><td>β(ω≥0)</td><td>(SE)_pos</td><td>Asymmetry Δβ</td><td>N</td></tr><tr><td>0.25</td><td>-0.0429</td><td>(0.0111)</td><td>-0.0638</td><td>(0.0116)</td><td>-0.0209</td><td>1387</td></tr><tr><td>0.50</td><td>-0.0643</td><td>(0.0101)</td><td>-0.0103</td><td>(0.0106)</td><td>+0.0539</td><td>1387</td></tr><tr><td>0.75</td><td>-0.1069</td><td>(0.0127)</td><td>+0.0129</td><td>(0.0135)</td><td>+0.1198</td><td>1387</td></tr></table>

Note. Quantile regressions at $\tau\in\{0.25,0.50,0.75\}$ of the conditional forward-growth distribution.

Table A10. Romano–Wolf adjusted p-values for the preferred downside-risk specifications

<table><tr><td>Adverse outcome</td><td>|t| on ω+</td><td>Naive p</td><td>Romano-Wolf adjusted p</td><td>Survives α=0.05 FWE</td><td>Survives α=0.10 FWE</td></tr><tr><td>Stagnation (g&lt;0 next 5y)</td><td>5.022</td><td>0.0000</td><td>0.0000</td><td>yes</td><td>yes</td></tr><tr><td>Large decline (g&lt;-5% next 5y)</td><td>4.260</td><td>0.0000</td><td>0.0000</td><td>yes</td><td>yes</td></tr><tr><td>Decline next 10y</td><td>9.766</td><td>0.0000</td><td>0.0000</td><td>yes</td><td>yes</td></tr><tr><td>Loss of frontier proximity</td><td>5.339</td><td>0.0000</td><td>0.0000</td><td>yes</td><td>yes</td></tr><tr><td>Banking crisis next 5y</td><td>3.987</td><td>0.0001</td><td>0.0000</td><td>yes</td><td>yes</td></tr><tr><td>Currency crisis next 5y</td><td>1.150</td><td>0.2502</td><td>0.4375</td><td>no</td><td>no</td></tr><tr><td>Sovereign-debt crisis next 5y</td><td>1.234</td><td>0.2170</td><td>0.4375</td><td>no</td><td>no</td></tr></table>

Note. Step-down correction with 1000 bootstrap replications.

Table A11. Within-country permutation test for $\omega^{+}$ .

<table><tr><td>Adverse outcome</td><td>Observed  $\beta(\omega^{+})$ </td><td>Permutation mean β</td><td>Permutation on SD</td><td>Permutation p (one-sided)</td><td>Permutation 95th pct</td><td>N obs</td><td>B (valid perms)</td></tr><tr><td>Stagnation</td><td>+0.4319</td><td>-0.1877</td><td>0.3517</td><td>0.0300</td><td>+0.3900</td><td>1117</td><td>500</td></tr><tr><td>Banking crisis</td><td>+1.3807</td><td>+0.1666</td><td>0.4321</td><td>0.0020</td><td>+0.8111</td><td>1110</td><td>500</td></tr><tr><td>Sovereign-debt crisis</td><td>+0.8522</td><td>+0.1144</td><td>0.4914</td><td>0.0520</td><td>+0.8576</td><td>1132</td><td>500</td></tr><tr><td>Loss of frontier</td><td>+1.3205</td><td>+0.0128</td><td>0.3398</td><td>0.0000</td><td>+0.5606</td><td>1532</td><td>500</td></tr></table>

Note. Randomization inference under the null that the positive trajectory gap has no association with the specified subsequent adverse outcome..

![](images/f1f47f2bf8812c02ba5246bafd5b74c2178e1e09ec32d64594c8728e35a88053.jpg)

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
