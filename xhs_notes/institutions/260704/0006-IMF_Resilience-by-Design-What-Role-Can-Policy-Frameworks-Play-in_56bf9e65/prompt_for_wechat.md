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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Resilience by Design:

# What Role Can Policy Frameworks Play in the Middle East and Central Asia?

Hasan Dudu, Troy Matheson, Dirk Muir, Karmen Naidoo, Salem Nechi, and Pedro Rodriguez

WP/26/138

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/dd097a36b770095ee06c0c409980f793a9652c265ab229d14ccff7e68b0b18c7.jpg)

# IMF Working Paper MCD

Resilience by Design:
What Role Can Policy Frameworks Play in the Middle East and Central Asia?
Prepared by Hasan Dudu, Troy Matheson, Dirk Muir, Karmen Naidoo, Salem Nechi, and Pedro Rodriguez\*

Authorized for distribution by Roberto Cardarelli
February 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: The changing global economic landscape is likely to expose the Middle East, North Africa, and Pakistan (MENAP) and Caucasus and Central Asia (CCA) regions to more frequent external shocks, putting a premium on resilient and flexible macroeconomic policy frameworks. By using empirical analysis and model-based scenarios, this paper highlights the important roles of policy frameworks in stabilizing MENAP and CCA economies against adverse global shocks. Two messages stand out from the analysis. First, as countries make progress toward diversifying their exports and deepening domestic financial markets, credible inflation-targeting monetary policy regimes that allow greater exchange rate flexibility could enable faster adjustment to adverse global shocks. Second, adopting strong fiscal rules could help better anchor long-term expectations, reduce risk premiums, and help support countercyclical fiscal responses.

RECOMMENDED CITATION: Dudu, Hasan, Troy Matheson, Dirk Muir, Karmen Naidoo, Salem Nechi, Pedro Rodriguez. 2026. “Resilience by Design: What Role Can Policy Frameworks in the Middle East and Central Asia?” IMF Working Paper WP/26/138, Washington DC.

JEL Classification Numbers:

E17, F47, E52, H60

Keywords:

Shocks; Macrodynamics; Fiscal; Monetary; Policy Frameworks

Author's E-Mail Address:

hdudu@imf.org; TMatheson@imf.org; DMuir@imf.org; knaidoo2@imf.org; snechi@imf.org; PRodriguez@imf.org

## Contents

## FIGURES

Figure 1. Monetary Policy Trilemma....5
Figure 2. Exchange Rate Regimes....6
Figure 3. Share of Economies with Formal Fiscal Rules, 1985–2024....7
Figure 4. Determinants of Sovereign Spreads....8
Figure 5. Impact of Adverse Global Shocks by Exchange Rate Regime....9
Figure 6. Impact of Global Shocks and Country Characteristics....10
Figure 7. Impact of Adverse Global Shocks on Real GDP: Different Fiscal Frameworks....11
Figure 8. Impact of Adverse Global Shocks on Primary Balance and Spreads: Different Fiscal Frameworks...11
Figure 9. Historical Shocks: Real GDP Losses....14
Figure 10. Real GDP Losses....16
Figure 11. Country Characteristics: MENAP and CCA Compared to Emerging Markets and Advanced Economies....18

Figure A- 1. MENAP & CCA: Exchange Rate Regimes....20
Figure A- 2. MENAP & CCA: Strength of Fiscal Rules, 2023....20
Figure A- 3. Real sector variables (percentage difference from the baseline, 2025-2026 Average)....22
Figure A- 4. External Sector Variables (percentage difference from the baseline, 2025-2026 Average)....22
Figure A- 5. Monetary Variables (percentage point difference from the baseline, 2025-2026 Average)....23
Figure A- 6. Fiscal Variables (percentage point difference from the baseline, 2025-2026 Average)....23
Figure A- 7. Comparison of model results with observed changes after the Global Financial Crisis and Covid Shock....Error! Bookmark not defined.

## TABLES

Table 1. Monetary policy frameworks of MCD countries in the current policy scenario....12
Table 2. Scenario assumptions....13

## I. Introduction

Trade protectionism and geopolitical fragmentation are reshaping the global economy and contributing to heightened global uncertainty and downside risks (IMF, 2025a; IMF, 2025b; World Bank, 2025). This changing global landscape is likely to expose the Middle East, North Africa and Pakistan (MENAP) and Caucasus and Central Asia (CCA) regions to more frequent adverse external shocks.

An economy's ability to respond to shocks ultimately depends on a complex interplay of factors: its economic structure, openness to trade and financial flows, and the design and strength of its policy institutions. Policy frameworks are especially important, as they determine the tools available to restore growth and stabilize inflation. In the MENAP and CCA regions, monetary policy frameworks generally place stronger emphasis on exchange rate stability as an objective than in other advanced and emerging market economies, whereas fiscal frameworks tend to be weaker, with few countries having formal fiscal rules. $^{1}$

Monetary policy frameworks are particularly important in determining how economies adjust to global shocks. Under credible inflation-targeting regimes with flexible exchange rates, policy interest rates can focus on domestic stabilization while exchange-rate movements act as automatic stabilizers, cushioning terms-of-trade and financial shocks (Broda, 2004; Carrière-Swallow et al., 2016). Empirical evidence shows that these frameworks can deliver lower inflation volatility and faster recoveries from external shocks, provided credibility is strong, and financial markets are sufficiently developed (Vega and Winkelried, 2005; Ball and Sheridan, 2003). By contrast, fixed or pegged regimes can import credibility from an anchor currency and help to contain inflation, but often at the cost of policy flexibility. These frameworks perform well when supported by disciplined fiscal policy, ample reserves, and synchronized cycles with the anchor economy—as in Hong Kong SAR and Jordan (Chiu, 2001; IMF, 2024 Jordan Article IV)—but are vulnerable when fiscal dominance, currency mismatches, or credibility gaps emerge, as illustrated by Argentina’s crisis in 2001 (IEO, 2004) and Lebanon’s collapse in 2019 (IMF, 2019; Financial Times, 2025 Lebanon).

Fiscal policy frameworks play a complementary and equally vital role in macroeconomic stabilization. Countries that enter downturns with stronger fiscal positions and well-established buffers are typically able to implement countercyclical policies without jeopardizing debt sustainability. Empirical evidence confirms that fiscal space and credible fiscal rules enhance resilience: economies with stronger frameworks experience smaller output losses and faster recoveries during crises (Auerbach and Gorodnichenko, 2012; Bova et al., 2016; IMF, 2020). Medium-term fiscal frameworks are particularly effective in linking short-term budget decisions to long-term sustainability goals, improving transparency and predictability (Harris and Sánchez, 2020; IMF, 2018). When supported by realistic forecasts and institutional enforcement, such frameworks help anchor expectations, reduce sovereign risk premia, and sustain investor confidence (Debrun and Kumar, 2007; Eyraud et al., 2018). Cross-country experience suggests that countries with more robust fiscal rules and frameworks enjoy lower sovereign spreads—often by several hundred basis points—underscoring the importance of fiscal credibility for macroeconomic stability (Debrun et al., 2013; World Bank, 2022).

Against this backdrop, this paper investigates how monetary and fiscal policy frameworks influence how MENAP and CCA economies respond following adverse global shocks. It combines empirical evidence from a global panel with model-based simulations employing the IMF's MCDMOD framework. Together, these approaches assess both the empirical and structural dimensions of resilience under different policy regimes—fixed versus (inflation targeting with) flexible exchange rates and strong versus weak fiscal frameworks. Two key messages emerge from the analysis. First, economies with flexible exchange rates generally experience smaller and less persistent output declines after adverse global shocks, particularly where financial markets are deeper and exports are more diverse. Although MENAP and CCA economies still lag other regions in export diversification and financial depth, ongoing progress in these areas over the coming years suggests that the benefits of moving to more flexible exchange rate regimes will become greater in the future. Second, strong fiscal rules (legally based, transparent, enforced, and resilient to shocks) can better anchor long-term expectations, reduce risk premia, and help support countercyclical fiscal responses to better stabilize output following adverse shocks.

The remainder of this paper proceeds as follows: Section II describes monetary and fiscal policy frameworks in the MENAP and CCA regions; Section III explores how policy frameworks tend to impact macroeconomic adjustment in a global sample; Section IV presents model-based evidence on how adjustments to policy frameworks in MENAP and CCA economies can help to mitigate the impact of global shocks; and Section V concludes with a summary of the findings.

## I. Policy Frameworks in the Middle East and Central Asia

## A. Monetary Frameworks

The “impossible trinity,” or the Mundell–Fleming Trilemma, highlights the inherent constraints on a country’s monetary policy objectives (Obstfeld, Shambaugh, and Taylor 2005). It holds that policymakers cannot simultaneously maintain a fixed exchange rate, free capital mobility, and domestic monetary policy autonomy. Only two of these three objectives can be pursued at the same time, as a country fundamentally has only two relevant monetary policy instruments at its disposal—the interest rate and capital controls. Each combination of these objectives offers distinct pros and cons with tradeoffs that depend on country-specific circumstances.

Figure 1. Monetary Policy Trilemma  
![](images/004c1168d364c3607d39303cb0f76e2a48ca2ab24774c14b224730d484f51a82.jpg)  
Sources: Aizenman, Chinn, and Ito (2010); and IMF staff calculations.
Note: The country-level indexes for monetary independence, exchange rate stability, and financial openness range between 0 and 1 and are averaged across the subregions displayed in the triangle. AE = advanced economies; CCA = Caucasus and Central Asia; EM = emerging market; FX = foreign exchange; GCC = Gulf Cooperation Council; ME&CA = Middle East and Central Asia; MENAP = Middle East, North Africa and Pakistan; OE = oil exporters; OI = oil importers.

Figure 1 displays indexes that capture the three dimensions of the impossible trinity (Aizenman, Chin, and Ito 2008). Monetary policy autonomy is measured by the correlation between a home country's money market interest rate and that of a base country. Exchange rate stability is gauged by the standard deviation of changes in the exchange rate (in log terms) relative to a base country. Financial openness reflects the extent of legal and regulatory restrictions on cross-border financial transactions (Chinn and Ito 2006 and 2008). $^{2}$

Monetary policy frameworks in the MENAP region reflect a clear preference for exchange rate stability (see Annex I, Figure A-1). In the Gulf Cooperation Council (GCC) countries and other MENA oil exporters, this is maintained primarily through currency pegs, with GCC countries favoring more open capital accounts. $^{3}$ MENAP oil importers also prioritize exchange rate stability, typically using managed regimes that preserve some degree of monetary policy autonomy thanks to less open capital accounts. By contrast, CCA countries lean toward greater monetary autonomy, coupled with more open capital accounts. According to the IMF's Annual Report on Exchange Arrangements and Exchange Restrictions (IMF 2023), about half of MENAP and CCA countries operate under some form of de facto peg. $^{4}$ Although recent years have seen a gradual shift toward greater exchange rate flexibility, most countries in the region continue to favor managed regimes that balance exchange rate stability with some room for adjustment (Figure 2), partly because of limited financial market development and shallow currency markets.

Figure 2. Exchange Rate Regimes  
1. CCA and MENAP Region: Share of Exchange Rate Regimes, 2023
(Percent)  
![](images/d772c2e89fde6d36bb0b63655848ae6be2085d2100de4f277e6cb3461c016457.jpg)

2. Share of Exchange Rate Regimes, 2023 (Percent)  
![](images/df705c59d26c0dda1006fc8bd5d95df88998c776442d0e3f32e11c63f4f920cc.jpg)  
Sources: IMF, The Annual Report on Exchange Arrangements and Exchange Restrictions database; and IMF staff calculations.
Note: AE = advanced economies; CCA = Caucasus and Central Asia; EMDE = emerging market and developing economies; GCC = Gulf Cooperation Council; MENAP = Middle East, North Africa and Pakistan; OE = oil exporters; OI = oil importers.

## B. Fiscal Frameworks

Strong fiscal frameworks can help anchor private sector expectations of future fiscal policy by lending credibility to official (budget) projections and commitments. Adopting credible medium-term fiscal frameworks and fiscal rules can help achieve this objective and indirectly contribute to lower sovereign spreads and higher credit ratings (Acalin and others 2025; Badinger and Reuter 2017; Sawadogo 2020; Islamaj, Penaloza, and Sommers 2024).

Some economies in the MENAP and CCA regions (for example, Mauritania, Oman, Saudi Arabia, and Tajikistan) operate under informal fiscal rules, but few have formally adopted rules that are codified in legislation. According to the IMF's updated Fiscal Rules Dataset (Alonso and others forthcoming), only one-quarter of economies in the MENAP and CCA regions have formal operational fiscal rules, compared to two-thirds in emerging market and developing economies, and over 80 percent in advanced economies (Figure 3).

Although the adoption of a fiscal rule is not necessarily conducive to stronger fiscal frameworks (as unwarranted deviations from it may undermine its credibility), “strong” fiscal rules can bolster the credibility of official projections and anchor private sector expectations of future fiscal policy (Chapter 2, October 2025 World Economic Outlook). Based on the IMF’s Fiscal Rule Strength Index, the MENAP and CCA regions are generally behind other regions, with their fiscal strength below the average for advanced and other emerging markets (the only exception being Georgia) (Annex I, Figure A-2).

![](images/2bab90cde16926a4b13d5f9b927ef3254c55a6ce825db7da28194860be1b777c.jpg)  
Sources: IMF, Fiscal Rule dataset; and IMF staff calculations.
Note: AE = advanced economy; CCA = Caucasus and Central Asia; EM = emerging market; MENAP = Middle East, North Africa and Pakistan.

## C. Fiscal Rules and Sovereign Spreads

To highlight the importance of fiscal rules, this section explores the role of strong fiscal rules and other macroeconomic and institutional factors in explaining the variation in sovereign spreads across countries, using a panel regression. Based on a global sample of 57 countries over the period of 1996–2021, the regression specification includes fixed effects and a control for global financial market volatility, with clustered standard errors. A strong (weak) fiscal rule is defined as a score in the top (bottom) third of the IMF Fiscal Rule Strength Index distribution.

The results from this analysis show that countries with strong fiscal rules typically enjoy lower sovereign spreads (by about 85 basis points) compared to those with weak or no fiscal rules (Figure 4). Over and above the presence of strong fiscal rules, differences in spreads across countries are determined by the strength of government institutions (proxied by a corruption index and a political risk score that captures government stability and rule of law, among other factors), the size of economic buffers (the presence of a sovereign wealth fund and the level of reserves), and debt levels. For example, large buffers help explain why GCC countries benefit from better creditworthiness while lacking formal fiscal rules. By contrast, despite having fiscal rules, several economies in the CCA region exhibit weaker creditworthiness compared to other emerging markets, mainly because of relatively weaker governance indicators.

Figure 4. Determinants of Sovereign Spreads (Coefficient estimates, Basis points)  
![](images/7a3d2b187367c096a455c5a81c56f6d4eb1c145ab85a131e201d197ea576a175.jpg)  
Sources: IMF, World Economic Outlook database; IMF, Fiscal Rules Database (Alonso and others, forthcoming); Bloomberg L.P.; World Bank, Worldwide Governance Indicators; and IMF staff calculations. Note: The political risk score ranges from 0 to 100, where a higher score means lower political risk.

## II. Policy Frameworks and Macroeconomic Adjustment: An Empirical Analysis

This section explores how monetary and fiscal policy frameworks have affected macroeconomic adjustment in a global sample of countries following adverse global shocks.

## A. Methodology

The analysis uses a local projections approach (Jordà 2005) applied to a global panel over the past three and a half decades to estimate how real output, current account, and the fiscal balance have responded to adverse global shocks under different monetary and fiscal policy frameworks. Global shocks are captured by a 1 standard deviation rise in the GDP-weighted World Uncertainty Index (Ahir, Bloom and Furceri 2022), equivalent to a jump from the 10th to 50th percentile of the historical distribution of the indicator (building on Chapter 2 of the April 2025 Regional Economic Outlook: Middle East and Central Asia).

The following baseline specification is used:

$$
\begin{array}{r l} y _ {i, t + h} - y _ {i, t - 1} = & \beta_ {1} ^ {h} U N C _ {i, t} + \beta_ {2} ^ {h} U N C _ {i, t} * P o l i c y F r a m e w o r k _ {i} + \sum_ {j = 1} ^ {2} \gamma_ {1} ^ {h} U N C _ {i, t - j} \\ & + \sum_ {j = 1} ^ {2} \gamma_ {2} ^ {h} (y _ {i, t - j} - y _ {i, t - j - 1}) + \theta_ {i} ^ {h} X _ {i, t} + \alpha_ {i} ^ {h} + \varepsilon_ {i, t} ^ {h} \end{array}
$$

where $y_{i,t}$ is the dependent variable of interest (real output, current account balance, primary balance, or sovereign spreads) for country i in year t; PolicyFramework is a dummy variable indicating either the exchange rate regime (fixed vs. floating), or the fiscal policy fram

[中间内容因长度限制已省略]

Assessing the Emerging Global Financial Architecture: Measuring the Trilemma's Configurations over Time.” Working Paper Series #14533, National Bureau of Economic Research (NBER).

Aizenman, Joshua, Menzie D. Chinn, and Hiro Ito. 2010. The Emerging Global Financial Architecture: Tracing and Evaluating New Patterns of the Trilemma Configuration. Journal of International Money and Finance 29 (4): 615–41.

Alonso, Virginia, Clara Arroyo, Ozlem Aydin, Vybhai Balasundharam, Hamid R. Davoodi, Gabriel Hegab, Anh M. Nguyen, Natalia. Salazar, Galen Sher, Alexandra Solovyeva, and Nino Tchelishvili. Forthcoming. “Fiscal Rules and Fiscal Councils: Recent Trends and Revisions since the Pandemic.” IMF Working Paper, International Monetary Fund, Washington, DC.

Andrle, Micale, Patrick Blagrave, Pedro Espaillat, Keiko Honjo, Benjamin L Hunt, Mika Kortelainen, René Lalonde, Douglas Laxton, Eleonara Mavrodeidi, Dirk V Muir, Susanna Mursula, and Stephen Snudden. 2015. “The Flexible System of Global Models – FSGM.” IMF Working Paper 15/64, International Monetary Fund, Washington, DC.

Badinger, Harald, and Wolf Heinrich Reuter. 2017. "The Case for Fiscal Rules." Economic Modelling 60: 334–43.

Ball, L., Sheridan, N. (2003). "Does Inflation Targeting Matter?" NBER Working Paper 9577.

Bova, E., Carcenac, N., & Guerguil, M. (2016). “Fiscal Rules at a Glance.” IMF Background Paper.

Broda, C. (2004). “Terms of Trade and Exchange Rate Regimes in Developing Countries.” Journal of International Economics, 63(1), 31–58.

Carrière-Swallow, Y., Gruss, A., Magud, N., & Valencia, F. (2016). “Monetary Policy Credibility and Exchange Rate Pass-Through.” IMF Working Paper 16/240.

Chinn, Menzie. D. and Hiro Ito. 2006. "What Matters for Financial Development? Capital Controls, Institutions, and Interactions." Journal of Development Economics 81 (1): 163–192 (October).

Chinn, Menzie. D. and Hiro Ito. 2008. "A New Measure of Financial Openness." Journal of Comparative Policy Analysis 10 (3): 309–322.

Chiu, P. (2001). “Hong Kong’s Experience in Operating the Currency Board System.” IMF Seminar on Exchange Rate Regimes.

Chowdhury, Mohammad Tarequl H., Prasad Sankar Bhattacharya, Debdulal Mallick, and Mehmet Ali Ulubaşoğlu. 2014. “An Empirical Inquiry into the Role of Sectoral Diversification in Exchange Rate Regime Choice.” European Economic Review 67: 210–27.

Debrun, X., & Kumar, M. 2007. "The Discipline-Enhancing Role of Fiscal Institutions." IMF Working Paper 07/171.

Debrun, X., Epstein, N., Symansky, S. 2013. “Rules-Based Fiscal Policy in Emerging Markets.” IMF Policy Paper.

Duttagupta, Rupa, Gilda Fernandez, and Cem Karacadag. 2005. “Moving to a Flexible Exchange Rate: How, When, and How Fast?” IMF Economic Issues 38, International Monetary Fund, Washington, DC.

Eyraud, L., Gaspar, V., Poghosyan, T. 2018. Fiscal Politics. Washington D.C.: IMF.

Financial Times. 2025. “Lebanon Passes Bank Restructuring Law in Step Toward IMF Reform.” August.

Frankel, Jeffrey. A. 2012. “Choosing an Exchange Rate Regime.” In Handbook of Exchange Rates (First Edition), edited by Jessica James, Ian W. Marsh, and Lucio Sarno. John Wiley and Sons, Inc.

Harris, J., Sánchez, A. 2020. “Medium-Term Fiscal Frameworks: Effective Design and Implementation.” World Bank Policy Note.

International Monetary Fund (IMF). 2023. Annual Report on Exchange Arrangements and Exchange Restrictions 2023. Washington, DC.

International Monetary Fund (IMF). 2025a. World Economic Outlook: Critical Juncture amid Policy Shifts. Washington, DC. April.

International Monetary Fund (IMF). 2025b. World Economic Outlook Update: Global Economy: Tenuous Resilience amid Persistent Uncertainty. Washington, DC. July.

International Monetary Fund (IMF). 2024. Jordan: Article IV Consultation and Second Review under the EFF (IMF Country Report No. 2024/345)

International Monetary Fund (IMF). 2020. Fiscal Monitor: Policies for the Recovery. Washington D.C.

International Monetary Fund (IMF). 2019. “Lebanon: Article IV Consultation—Staff Report.” IMF Country Report 19/312.

International Monetary Fund (IMF). 2018. Assessing Fiscal Space: An IMF Handbook. Washington D.C.

International Monetary Fund (IMF), Independent Evaluation Office (IEO). 2004. The IMF and Argentina, 1991–2001. Washington D.C.

Islamaj, Ergys, Agustin Samano Penaloza, and Scott Sommers. 2024. “The Sovereign Spread Compressing Effect of Fiscal Rules during Global Crises.” World Bank Policy Research Paper 10741, Washington, DC.

Jordà, Óscar. 2005. “Estimation and Inference of Impulse Responses by Local Projections.” American Economic Review 95 (1): 161–82. Levy-Yeyati, Eduardo, and Federico Sturzenegger. 2003. “To Float or to Fix: Evidence on the Impact of Exchange Rate Regimes on Growth.” American Economic Review 93 (4): 1173–93.

Levy-Yeyati, Eduardo, and Federico Sturzenegger. 2016. “Classifying Exchange Rate Regimes: 15 Years Later.” HKS Working Paper No. 16-028, August.

Obstfeld, Maurice, Jay C. Shambaugh, and Alan M. Taylor. 2005. "The Trilemma in History: Tradeoffs among Exchange Rates, Monetary Policies, and Capital Mobility." The Review of Economics and Statistics 87 (3): 423–38.

Sawadogo, Pegdéwendé Nestor. 2020. “Can Fiscal Rules Improve Financial Market Access for Developing Countries?” Journal of Macroeconomics 65: 103214.

Vega, M., Winkelried, D. (2005). “Inflation Targeting and Inflation Behavior: A Successful Story?” International Journal of Central Banking, 1(3), 1–34.

World Bank. 2025. Flagship Report: Global Economic Prospects. Washington DC. June.

World Bank. 2022. Fiscal Frameworks for Resilience and Growth. Washington D.C.

![](images/d0b81764f5bbe9468ca016b294f00d0d93dc53df201d46993c4dafb80abcb7ac.jpg)
"""
