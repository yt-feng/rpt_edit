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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Credit Expansion in the Caucasus and Central Asia

Etibar Jafarov and Chingis Matayev

WP/26/137

IMF Working Papers describe research in progress by the authors and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the authors and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/7291339ac7f2d2b507bfbeebbcce049e746127967bba018400e8721760266178.jpg)

# IMF Working Paper Middle East and Central Asia Department

Credit Expansion in the Caucasus and Central Asia Prepared by Etibar Jafarov and Chingis Matayev\*

Authorized for distribution by Amina Lahreche
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the authors and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper analyzes credit developments in the Caucasus and Central Asia (CCA) using several complementary approaches. First, it estimates long-run equilibrium credit levels based on economic fundamentals, providing benchmarks to assess whether observed credit levels are broadly aligned with country characteristics. Second, it applies statistical “gap” measures to identify periods of unusually rapid credit expansion that may signal emerging financial vulnerabilities. Third, it uses the Kalman filter to decompose credit into trend and cyclical elements conditional on macro variables. The results suggest there is scope for further financial deepening in all CCA economies, but the speed of household credit expansion warrants close monitoring. A comparative “horse race” of alternative indicators suggests that no single measure consistently outperforms others across countries, implying that combining various credit gap measures enhances the robustness of risk assessments.

RECOMMENDED CITATION: Jafarov, Etibar, and Chingis Matayev, 2026, “Credit Expansion in the Caucasus and Central Asia,” IMF Working Paper No. 26/137 (Washington: International Monetary Fund)

<table><tr><td>JEL Classification Numbers:</td><td>C23, E32, E44, G28, O16</td></tr><tr><td>Keywords:</td><td>Credit growth; credit cycles; credit gaps; financial deepening;financial stability; early warning indicators; Caucasus and Central Asia</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>ejafarov@imf.org;c.matayev@qmul.ac.uk</td></tr></table>

WORKING PAPERS

# Credit Expansion in the Caucasus and Central Asia

Prepared by Etibar Jafarov and Chingis Matayev $^{1}$

## Contents

I. Introduction ....4
II. Stylized Facts about Credit in CCA ....5
III. Long Run Equilibrium Approach ....9
Literature review ....9
Empirical Model ....10
Data ....11
Panel Estimation Strategy: Fixed Effects VS. Mean Group Estimators ....12
Estimation Results ....13
Results (Deviation from benchmark) ....14
IV. Speed of Credit Growth – Statistical Gap Measures ....17
V. Disaggregating Credit Dynamics: Households vs. Corporates ....20
Household Credit ....20
Corporate Credit ....21
VI. Multivariate Filter (MVF) Credit Gap ....25
VII. Which Credit Gap is Better? ....26
Methodology ....27
Crisis Data ....28
Results ....28
VIII. Conclusion ....30
References ....32
Annex I. Equilibrium (Large Economies) ....35
Annex II: Multivariate Filter Estimation for Kazakhstan ....37
Annex III. Banking Sector Crisis Episodes ....44
FIGURES
1. Evolution of Total, Household, and Corporate Credit Across CCA Economies ....7
2. Credit Decomposition by Currency of Denomination ....8
3. Deviation from the Equilibrium Level Credit -to-GDP Ratio ....16
4. Credit Gap Measures for the CCA Economies ....19
5. Household Credit Gap Measures for the CCA Economies ....23
6. Corporate Credit Gap Measures for the CCA Economies ....24
7. Comparison of MVK and Other Gap measures for the CCA Economies ....26
8. AUC by Horizon ....30

3. Deviation from the Equilibrium Level Credit -to-GDP Ratio 36
TABLE
1 Regression Results for the Panel Estimates 14

## I. Introduction

Credit dynamics play a central role in shaping financial stability outcomes. Historically, periods of rapid credit growth have often preceded episodes of financial stress, while persistently low levels of credit relative to fundamentals can constrain investment, financial inclusion, and long-term growth. For policymakers, the challenge lies in distinguishing between sustainable financial deepening and excessive credit expansion that heightens vulnerability to macroeconomic shocks and raises the risk of banking crises. This challenge is particularly acute in emerging market and transition economies, where significant financial deepening is ongoing and credit cycles are often amplified by macroeconomic volatility and external shocks.

This paper takes a three-pronged approach to analyzing credit developments in the CCA. First, it estimates long-run equilibrium levels of credit-to-GDP based on structural characteristics such as income, demographics, and financial depth. These benchmarks indicate whether credit is broadly aligned with fundamentals, or whether structural under- or over-lending is present. Second, it constructs statistical measures of credit gaps, which capture cyclical deviations of credit from their trend. These indicators focus on the pace of credit expansion and provide timely signals of potential vulnerabilities associated with unusually rapid credit growth, including underpricing of risk and relaxed underwriting standards. Third, it applies a state-space framework estimated via a multivariate Kalman filter, allowing the trend to evolve with macroeconomic conditions. Unlike univariate (statistical) credit gap measures, this approach distinguishes cyclical credit excesses from financial deepening conditional on macroeconomic developments and post-crisis normalization. $^{1}$

A common critique of the equilibrium approach is that the credit-to-GDP ratios in most CCA countries were at low levels for much of the sample period, rendering comparisons with equilibrium benchmarks redundant. However, equilibrium estimates remain informative for three reasons. First, they gauge the scope for sustainable financial deepening, helping distinguish between catch-up dynamics from overheating. Second, they allow meaningful cross-country comparisons, showing whether differences in credit depth reflect structural fundamentals or financial underdevelopment. Third, they complement statistical gap indicators by addressing the level dimension: while statistical gap measures focus on near-term momentum, equilibrium benchmarks signal when convergence may be reaching its limits given the income growth path.

To assess the usefulness of different cyclical indicators, the paper then compares how these statistical credit gap measures perform in terms of predicting banking sector stress episodes. This exercise highlights the strengths and limitations of individual gap measures and provides guidance on their interpretation. By combining both perspectives, the paper provides a richer assessment of financial stability risks than relying on either approach alone. Equilibrium benchmarks capture the level dimension of credit sustainability, while statistical gaps capture the momentum dimension of credit expansion. The Kalman-filter-based gap complements these measures by isolating cyclical excesses after accounting for the effects of macro-shocks.

Together, they help identify situations in which credit is both high relative to fundamentals and deviating from its trend—a combination that has historically been associated with heightened crisis risk.

The contribution of this paper is twofold. First, it applies a consistent framework to measure equilibrium credit levels, benchmarked against advanced and emerging market reference countries, and credit gaps across CCA economies. Second, it evaluates the ability of different indicators to signal risks, using a comparative “horse race” to assess their reliability in signaling banking distress. It draws policy implications for credit monitoring in the region, emphasizing the value of a dual framework that captures both structural and cyclical aspects of credit dynamics.

The remainder of the paper is structured as follows. Section II briefly overviews some stylized facts about credit market developments in CCA, Section III presents results from the equilibrium analysis, Section IV discusses the statistical gap measures, and Section V provides credit gap estimates using the Kalman filter. Section VI evaluates the relative performance of alternative indicators in a comparative exercise. Section VII concludes.

## II. Stylized Facts about Credit in CCA

Credit-to-GDP ratios in the Caucasus and Central Asia remain relatively low by international standards, but have experienced periods of rapid growth, sometimes followed by sharp reversals. Figure 1 illustrates the evolution of total, household, and corporate credit across CCA economies, while Figure 2 shows the composition by currency of denomination. Several common features stand out.

\- First, overall credit penetration is modest but heterogeneous across countries. Armenia and Georgia display the highest credit-to-GDP ratios, approaching 60–70 percent in some recent years, reflecting deeper economic transformation and financial intermediation relative to regional peers as well as declines in GDP during the COVID pandemic. By contrast, credit-to-GDP in Kyrgyzstan and Tajikistan remains in the range of 10–25 percent, suggesting shallower financial systems. Uzbekistan, Kazakhstan and Azerbaijan lie in between, with the latter two economies experiencing pronounced credit booms followed by contractions, before credit started to recover in recent years.

\- Second, household credit has recently become the main driver of credit growth across much of the region. In most countries, household lending now exceeds corporate credit. Household loans have long accounted for the larger share of private sector credit in Georgia and the Kyrgyz Republic, and overtaken corporate lending in Armenia, following the rapid growth since 2022. In Kazakhstan, the deleveraging of the corporate sector after the banking stress of the late 2000s, combined with robust household borrowing, has also shifted the composition of credit toward households. Similar dynamics are observed in Tajikistan and Azerbaijan. Only in Uzbekistan does corporate lending significantly exceed household lending, though the latter is expanding faster from a low base.

\- Third, credit cycles in the region have been highly volatile. Kazakhstan, Azerbaijan, and Tajikistan experienced sharp credit contractions following banking sector stresses in late 2000s-mid-2010s, with the credit-to-GDP ratios falling by 15–20 percentage points in Azerbaijan and Kazakhstan. Armenia and Georgia also saw temporary corrections, but the broader trend has been sustained credit deepening. These episodes highlight the vulnerability of the region to boom-bust dynamics.

\- Fourth, the currency composition of credit has shifted over time. FX lending was historically dominant in the region, exposing borrowers and banks to exchange rate risks. However, loan dollarization has declined significantly in recent years, with the share of domestic currency loans exceeding that of loans in foreign currency in all CA countries.

Figure 1. Evolution of Total, Household, and Corporate Credit Across CCA Economies (In percent of GDP)  
![](images/4ac94eef3453d24188733ea5ade1990f6926cfc44d07951b04eed8193cb9cebf.jpg)

![](images/80ab5b4fa5ad55f32966698f763936ac6ae74250bf3cc3b72c7d1c335a3610d0.jpg)

![](images/eed12bc51686a1dfd18ed45e64aa11fe542337a9553abd2c894653924135a5e1.jpg)

![](images/b03e76fa95c4dd4cfcc1b0cd1c01c1251a9ba4a09b1a06e2d8ae2d02d9bb3ff7.jpg)

![](images/e912d8d5a212e39ca9dd695eeaceda2614948d4e040536a91eb09f15fe28d071.jpg)

![](images/d338e1cb283630630691fc9ee400c2d450570566ae7c190dc606744129840d00.jpg)

![](images/0d06505f9beb78668571d81aecdb255fe68367fbd97827f9e272987f5e8d78f8.jpg)  
Sources: BIS; IMF, International Financial Statistics; national authorities; and authors' estimates.

Figure 2. Credit Decomposition by Currency of Denomination  
![](images/9b5b94dde5cffe255be46e090af08918af829295da27373fbe033c397090d512.jpg)

![](images/1d9344845c0cace6291c596c40fecb34e0216332b024f63760cbe5da35d0203e.jpg)

![](images/4c2b05496da41d77f52e1bcf3a70b196da1c79c25235ed90137e1f857b406b55.jpg)

![](images/bc6f54b905db803e503118e5f2f95a077e15f29f20ee4a54c4879f69b65b8333.jpg)

![](images/4f72e96f9860d0859ac5302915134830587fa0546abe02da65254ab9c9cf2385.jpg)

![](images/3ba4c23706c97fb0e34f02eeda573b821e2a07fd27c05e3e5c339dade716511b.jpg)

![](images/e715c9eb798877311dcd2d4fef8151341246291bb0630ed79bd5bb67512f036c.jpg)  
Sources: National central banks, and authors' estimates.

## III. Long Run Equilibrium Approach

## Literature review

A rich literature has examined the determinants of credit deepening and how to identify credit “booms.” Early empirical work, largely focused on emerging Europe in the 2000s, established the concept of an equilibrium credit level determined by macroeconomic fundamentals. For example, Cottarelli, Dell’Ariccia, and Vladkova-Hollar (2005) analyzed bank credit growth in Central and Eastern Europe and the Balkans, finding that differences in credit-to-GDP across countries could be partly explained by fundamentals like per capita income and institutional factors (Cottarelli and others 2005).

Building on this approach, Égert, Backé, and Zumer (2006) provided a seminal study of 11 Central and Eastern European transition economies. They posited that the private credit-to-GDP ratio has a long-run equilibrium relationship with economic development and financial structure indicators. A key insight from Égert and others was that in-sample panel estimates using only transition economies can be misleading – many transition countries started the 1990s with extremely low credit levels (“initial undershooting”) and then experienced rapid catch-up growth. As a result, a panel regression solely on these countries tends to show upward-biased coefficients and instability, essentially overfitting the post-socialist credit boom adjustment. Égert and others therefore advocated using an out-of-sample panel of peer countries (in their case, small open OECD economies) to estimate stable long-run coefficients and then applying those coefficients to the transitioning countries. This provided a more reliable equilibrium benchmark, given that transition economies were expected to converge to the behavior of more advanced economies in the long run. Their results suggested that by the mid-2000s some CEE countries had nearly reached equilibrium credit levels while others’ credit levels remained well below fundamentals.

Similarly, Kiss and others (2006) examined the new EU member states and asked: was the rapid credit growth an “equilibrium convergence or a boom?” Using a dynamic panel approach (the pooled mean group estimator), they separated the equilibrium trend from any excess credit component. Kiss and others found that a large part of the credit expansion in the mid-2000s was indeed explained by fundamental catching-up, with credit-to-GDP ratios generally below levels predicted by fundamentals (indicating remaining room for financial deepening). Only in a couple of cases (e.g. the Baltic states) was credit growth significantly faster than justified by fundamentals, indicating an emerging credit boom above equilibrium. These studies set the tone and methodology for analyzing credit booms in emerging markets: estimate a long-run equilibrium credit level based on economic fundamentals and then gauge actual credit positions relative to this benchmark.

The global financial crisis renewed interest in measuring excess credit, and additional approaches emerged. The Bank for International Settlements (BIS) popularized a simpler statistical measure of the credit cycle – the “credit-to-GDP gap,” defined as the deviation of the credit/GDP ratio from its long-term trend (often estimated via a two-sided Hodrick-Prescott filter). This Basel Credit Gap (BCG) became an official guide for countercyclical capital buffers due to its empirical success in foreshadowing banking crises. However, such purely statistical gaps can at times give counterintuitive signals – for example, after a bust they may suggest large negative gaps (credit far below trend) even if the previous trend was unsustainably high.

Consequently, researchers have looked to complement the HP-filter gap with approaches grounded in economic fundamentals. One approach is a “fundamentals-based” panel regression, akin to the Égert/Kiss methodology, to assess if credit levels are excessive relative to a country’s structural features. Baba and others (2020) demonstrate this by applying both a multivariate filter and a fundamentals-based panel model to European economies, as a useful complement to the Basel gap for assessing vulnerabilities. Their work underscores that fundamentals-based equilibrium measures add important context, especially when structural shifts invalidate historical trend extrapolation.

Dell'Ariccia and others (2012) document that only one third of credit booms end in a banking crisis, while the majority do not culminate in systemic distress. Many booms occur in relatively undeveloped financial systems and coincide with financial deepening rather than pure excess. For instance, the median credit-to-GDP ratio at the start of boom episodes globally is around 19 percent, far lower than the global median of about 30 percent, consistent with the notion that credit booms often begin as catch-up growth in shallow financial systems. Nevertheless, credit booms that overshoot can still trigger crisis. In Eastern Europe, the credit surges in mid-2000s were partly an equilibrium convergence fueled by EU integration, yet overshooting in some cases led to hard landings in the late 2000s.

The literature therefore highlights two key lessons. First, it is critical to establish a long-run equilibrium credit level based on a country's income, interest rates, and financial structure to judge whether credit growth is fundamentally justified. Second, even when credit is below or near that equilibrium (indicating no structural overextension), the pace of credit expansion matters. Too rapid growth can cause instability before the long-run equilibrium is reached.

## Empirical Model

A core premise of our approach is that long-run equilibrium is not estimated solely from CCA countries' own 

[中间内容因长度限制已省略]

<td> $\rho_{\pi}$ </td><td>Beta</td><td>0.40</td><td>0.10</td><td>[0.01, 1]</td></tr></table>

## VIII. Shock Standard Deviations — Prior Distributions

All shock standard deviations are estimated with inverse-gamma prior distributions (with infinite prior standard deviation, i.e., uninformative scale).

## Domestic Shocks (Kazakhstan)

<table><tr><td>Parameter</td><td>Prior Mode</td><td>Description</td></tr><tr><td> $\sigma^{Y}$ </td><td>0.25</td><td>Output gap shock</td></tr><tr><td> $\sigma^{G}$ </td><td>0.05</td><td>Trend growth shock</td></tr><tr><td> $\sigma^{LGDP\_BAR}$ </td><td>0.05</td><td>Potential output level shock</td></tr><tr><td> $\sigma^{PIE}$ </td><td>0.25</td><td>Inflation shock</td></tr><tr><td> $\sigma^{C\_GAP}$ </td><td>0.25</td><td>Credit gap shock</td></tr><tr><td> $\sigma^{C\_BAR}$ </td><td>0.05</td><td>Trend credit level shock</td></tr><tr><td> $\sigma^{GC}$ </td><td>0.06</td><td>Trend credit growth shock</td></tr><tr><td> $\sigma^{UNR\_GAP}$ </td><td>0.25</td><td>Unemployment gap shock</td></tr><tr><td> $\sigma^{UNR\_BAR}$ </td><td>0.05</td><td>NAIRU level shock</td></tr></table>

<table><tr><td>Parameter</td><td>Prior Mode</td><td>Description</td></tr><tr><td> $\sigma^{G\_UNR\_BAR}$ </td><td>0.05</td><td>NAIRU growth shock</td></tr><tr><td> $\sigma^{PHI}$ </td><td>0.25</td><td>Risk premium shock</td></tr><tr><td> $\sigma^{PI}$ </td><td>0.15</td><td>Inflation target shock</td></tr></table>

Foreign Shocks (Russia)

<table><tr><td>Parameter</td><td>Prior Mode</td><td>Description</td></tr><tr><td> $\sigma^{Y\_E}$ </td><td>0.18</td><td>Output gap shock (RU)</td></tr><tr><td> $\sigma^{G\_E}$ </td><td>0.06</td><td>Trend growth shock (RU)</td></tr><tr><td> $\sigma^{LGDP\_BAR\_E}$ </td><td>0.04</td><td>Potential output level shock (RU)</td></tr><tr><td> $\sigma^{PIE\_E}$ </td><td>0.18</td><td>Inflation shock (RU)</td></tr><tr><td> $\sigma^{INT\_E}$ </td><td>0.20</td><td>Monetary policy shock (RU)</td></tr><tr><td> $\sigma^{R\_BAR\_E}$ </td><td>0.20</td><td>Natural real rate shock (RU)</td></tr></table>

Real Exchange Rate Shocks

<table><tr><td>Parameter</td><td>Prior Mode</td><td>Description</td></tr><tr><td> $\sigma^{Z\_GAP}$ </td><td>0.60</td><td>Real exchange rate gap shock</td></tr><tr><td> $\sigma^{Z\_BAR}$ </td><td>0.60</td><td>Real exchange rate trend shock</td></tr></table>

## Annex III. Banking Sector Crisis Episodes

Azerbaijan (2015–2017). The 2014 oil-price collapse precipitated two manat devaluations in 2015, sharply raising FX credit risk, dollarization, and pressure on bank capital and liquidity. IMF staff flagged the creation of a dedicated financial regulator (FIMSA) and a sectoral restructuring agenda as authorities revoked licenses of weaker banks and prepared an overhaul of the largest state-owned lender, the International Bank of Azerbaijan (IBA) (5). In 2017, IBA halted foreign-debt payments and entered a court-sanctioned restructuring under Azeri law; recognition proceedings in English courts document the process and timing (7). IMF surveillance subsequently described the economy as recovering “from a banking crisis and recession” (6). These sources jointly support systemic classification and anchor 2015Q1–2017Q4 as the evaluation window.

Kazakhstan (2008–2010; 2014–2017). The first wave followed a pre-GFC, wholesale-funded credit boom; when global funding dried up, multiple large banks required intervention and NPLs surged. IMF reports at the time characterized the event as a system-wide banking shock requiring comprehensive resolution and recapitalization strategies (8; 9). A second systemic wave unfolded in 2014–2017, when oil-price weakness and the 2015 move to a free float produced large tenge depreciation, revealing legacy asset-quality problems. The cleanup culminated in the 2017 rescue and merger of Kazkommertsbank (KKB) with Halyk, with staff reports noting substantial expected public support and sector consolidation (10; 11). We therefore date the windows as 2008Q3–2010Q4 and 2014Q4–2017Q4.

Kyrgyz Republic (2010). Domestic political upheaval in April–June 2010 triggered rapid deposit outflows and system-wide liquidity stress. Authorities imposed temporary administration in key banks, nationalized Asia Universal Bank (AUB) and placed it under conservatorship; IMF documents note a 30 percent deposit decline within April and supervisory measures across the system (12; 13). The combination of generalized funding pressure, state control of the largest bank, and emergency measures is consistent with a systemic episode; we date 2010Q2–2010Q4 as the core crisis phase.

Tajikistan (2015–2016). Long-standing weaknesses—directed lending, governance problems, and rising loan losses—culminated in late-2016 with a public recapitalization of two large banks amounting to about 6 percent of GDP. IMF press materials and later staff work record the fiscal cost and its impact on debt dynamics (14; 15). We treat 2015Q4–2016Q4 as the evaluation window capturing the run-up and immediate resolution phase.

Armenia, Georgia, Uzbekistan. LV report no systemic banking crises in these countries through 2017 (4). Despite periods of rapid credit growth (notably Georgia in 2017–2021) and high dollarization, macroprudential tightening and supervisory measures helped avoid generalized bank failures or large fiscal recapitalizations characteristic of LV-style systemic episodes. We therefore treat these countries as non-crisis cases in the horizon-specific evaluation, while using their histories to define tranquil observations and to document vulnerability build-ups that did not crystallize into systemic breaks.

![](images/f215817b6111823c66ad03c32d991086d7c45074c575451831827308e8cf2d01.jpg)
"""
