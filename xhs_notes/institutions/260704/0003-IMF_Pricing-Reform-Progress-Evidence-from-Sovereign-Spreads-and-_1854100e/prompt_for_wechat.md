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
# Pricing Reform Progress: Evidence from Sovereign Spreads and Consensus Forecasts

Ken Miyajima

WP/26/141

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/e14ec91c95d51284c8198ecd850f4bce3355d3d793e827a84a206bddde1a34be.jpg)

# IMF Working Paper Middle East and Central Asia Department

# Pricing Reform Progress: Evidence from Sovereign Spreads and Consensus Forecasts Prepared by Ken Miyajima\*

Authorized for distribution by Nathan Porter
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Investors reward reform progress. Econometric results suggest that holistic reforms, fiscal spending discipline, and monetary policy credibility are associated with a tightening of Qatar's external sovereign credit spreads. In particular, investors may view fiscal spending discipline as an integral part of Qatar's holistic reform and economic diversification. Greater broad-based reform progress also boosts the resilience of sovereign credit spreads to external shocks. The findings support fiscal and monetary policy reforms as part of the broader reform agenda in a holistic manner, as planned under the Third National Development Strategy.

E44 – Financial Markets and the Macroeconomy

G15 – International Financial Markets

H63 – Debt; Debt Management; Sovereign Debt

JEL Classification Numbers:

O53 – Economywide Country Studies: Middle East, North Africa, and Mediterranean Countries

P48 – Political Economy; Legal Institutions; Property Rights (within economic development context)

Consensus Forecasts; Economic Diversification; Fiscal Discipline;

Keywords:

Monetary Policy Credibility; Qatar National Development Strategy;

Reform Progress; Sovereign Credit Quality; MENA Region

Author's E-Mail Address:

kmiyajima@imf.org

WORKING PAPERS

# Pricing Reform Progress: Evidence from Sovereign Spreads and Consensus Forecasts

Prepared Ken Miyajima

## Contents

## Pricing Reform Progress: Evidence from Sovereign Spreads and Consensus Forecasts

A. Introduction......3
II. The Literature......4
III. Estimation Strategy and Data......6
IV. Baseline Panel Results......7
V. Extension: Impact of Reforms on Sovereign Credit Quality......8
Indicator of reform......8
Estimated Impact of Reforms......9
VI. Summary Discussions......13

Appendix Table and Figure......15

References......19

## FIGURES

Figure 1. External Sovereign Credit Spreads in MENA .... 3
Figure 2. Global and Domestic Uncertainty .... 4
Figure 3. Indicators of Reform in MENA .... 10
Figure 4. Impact of Economic Reforms on External Sovereign Credit Spreads in MENA .... 12
Figure A1. Actual and Predicted External Sovereign Credit Spreads in MENA .... 16

## TABLES

Table 1. Determinants of External Sovereign Credit Spreads in MENA....8
Table A1. Determinants of External Sovereign Credit Spreads in MENA....15
Table A2. Constituencies of Five Sub-Components....16
Table A3. Determinants of External Sovereign Credit Spreads in the GGC and Qatar....17
Table A4. Determinants of External Sovereign Credit Spreads in MENA....18

## A. Introduction

Qatar's sovereign credit quality has strengthened alongside ongoing reform implementation over the past decade. This paper asks what role Qatar's reform process has played in this strengthening of sovereign credit quality, a commonly used dynamic and forward-looking measure of economic resilience perceived by investors (Longstaff et al., 2011; Chernov et al., 2020; among others). A key indicator of sovereign credit quality, the credit default swap spread, has generally tightened in the past decade, from around 100 basis points to 40 basis points for Qatar, remaining tighter than those of its Gulf Cooperation Council (GCC) peers and significantly more so than other Middle East and North African (MENA) economies' (Figure 1, left panel). Qatar's sovereign credit rating was upgraded to AA (or equivalent) by all three major agencies (S&P in 2022; both Fitch and Moody's in 2024) and currently maintains a stable outlook. Qatar's first-ever US\$2.5 billion green bond issuance in 2024 (which marked the nation's return to the Eurobond market after four years) and another US\$3 billion conventional bond issuance in early-2025 were both 5–6 times oversubscribed by a diverse investor base from Asia, Europe, MENA, and the US. In addition to ongoing reform implementation under the Third National Development Strategy, Qatar has demonstrated resilience to external shocks in recent years aided by a favorable medium-term outlook underpinned by liquefied natural gas (LNG) production expansion (Figure 1, right panel).

Figure 1. External Sovereign Credit Spreads in MENA
(Basis point)  
![](images/b4e80f62f94000f79a3645771352cffd16a69ebb254f8464d56028d4d0c61d1e.jpg)  
...and has generally tightened underpinned by ongoing reforms and the favorable economic outlook.

![](images/5245d61497b6a8ac77c76618a8d26c66211e8de678e89117ee1c086614f296ec.jpg)  
Sources: Bloomberg and IMF staff calculations.

Reform momentum could be an important form of reassurance to markets about the prospects for economic stability, growth, and price stability. Global economic and policy uncertainty has risen to unprecedented levels, placing a premium on broad-based, careful, and coordinated implementation of reforms. So far, domestic uncertainty has remained contained in Qatar, reflecting economic and policy stability. Further reforms to boost productivity, enhance the business environment, and leverage digitalization and climate actions should continue to anchor domestic stability and enhance growth and resilience to external shocks.

## Figure 2. Global and Domestic Uncertainty

...heightened global uncertainty ...

![](images/077dd25103c1d7c83ddc54d56be59bf40289262808f48988005a0103fd70609c.jpg)

...while doemstic uncertainty has remained more contained in the region, especially Qatar.

Indicator of Doemstic Uncertainty in MENA and the US 1/ (Qatar period average = 1)

![](images/745846cf28c911c47116cb8b9e2b44bac9b6fef12783a982b4f135d01ed3cc71.jpg)  
Sources: Ahir, Bloom, and David Furceri. 2022. "World Uncertainty Index." NBER Working Paper 29763 and IMF staff calculations.  
1/ Annual average of monthly data. January–February for 2025.

Against this backdrop, this paper proposes a practical framework for assessing reform impact on a country's perceived resilience, finding a strong association between broad-based (not narrow) reform efforts and credit quality. Investors' perception of a country's resilience is proxied by external sovereign credit spreads. A standard econometric approach is used to estimate how these spreads are associated with indicators of reform progress, measured in terms of both the level of progress, and the balance of reforms, while accounting for other key determinants including macroeconomic conditions, oil prices, and global risk taking. The analysis is conducted using monthly data for six GCC states and twelve other MENA countries over the past decade with a specific focus on Qatar.

The rest of the paper is structured as follows. Section B discusses relevant literature while section C outlines the data and estimation strategy. Section D discusses baseline results while Section E discusses extensions. Section F summarizes findings and discusses policy implications for Qatar.

## II. The Literature

The economic literature has studied emerging market external sovereign credit spreads using a wide range of determinants. The literature has built upon foundational work that initially emphasized the role of macroeconomic fundamentals. More recent contributions have incorporated global financial conditions, market sentiment and, increasingly, the role of macroeconomic expectations (forecasts). Reforms have increasingly been recognized as a key driver when they are credible, tightening sovereign credit spreads by both reducing the expected probability of default through improved fundamentals and lowering perceived uncertainty.

Seminal work established the importance of country-specific macroeconomic variables in explaining sovereign risk premia. Edwards (1984) provided an early framework linking macroeconomic indicators to sovereign default risk. Subsequent research solidified the role of key fundamentals. The negative impact of high public debt levels on the sovereign's creditworthiness is supported by studies including Cline (1995) and

Reinhart and Rogoff (2009). The positive influence of economic growth on a country's ability to service debt is demonstrated in numerous studies including Cantor and Packer (1996). The negative effects of persistent fiscal and current account deficits on sovereign risk premiums are well-documented (e.g., Edwards, 1984; Min, 1998). While inflation's direct impact might be less clear, higher inflation rates are often viewed as a proxy for a lack of fiscal and monetary policy discipline and can contribute to political instability, thereby widening sovereign spreads. Our model will include these commonly used factors.

The literature has increasingly recognized the significant impact of global factors on sovereign risk premia. The crucial role of global risk appetite (often proxied by the VIX, or the implied volatility of a US stock option), global liquidity, and contagion was emphasized by authors including González-Rozada and Yeyati (2008), Kaminsky and Reinhart (2000), and Calvo and Reinhart (1996). Reinhart and Reinhart (2009) discuss capital flows bonanzas driven by external factors. Eichengreen and Mody (1998) highlight that investor sentiment can play a key role in dictating launch spreads. Our model will include oil prices and VIX to capture the influence of key global factors in MENA.

A more recent strand of the literature explicitly incorporates macroeconomic forecasts to capture the forward-looking nature of investor assessments. While not exclusively focused on forecasts, early work implicitly acknowledged the role of expectations by examining the impact of anticipated policy changes. Studies directly using survey-based forecasts have shown that expected improvements in macroeconomic variables are associated with tighter sovereign spreads (Cimadomo et al., 2014). In addition, forecast variables could alleviate the issue of potential reverse causality. $^{1}$ The availability and quality of forecast data for a broad range of countries can be a limitation, although this paper leverages forecasts of major macroeconomic variables for 18 MENA economies from FocusEconomics.

Finally, the literature finds that economic reforms are associated with tightening sovereign credit spreads, reflecting improved underlying economic strength and resilience, reducing uncertainty. Announcements and implementation of fiscal consolidation measures approved by legislative bodies often lead to a significant decline in sovereign credit spreads through confidence effects (David et al., 2022). Reforms in monetary policy institutions that enhance independence and credibility help the central bank anchor inflation expectations better, reduce uncertainty, and tighten the risk premium demanded by investors. Reforms that enhance a country's economic complexity tend to lower sovereign risk in the long run (Gomez-Gonzalez et al., 2025) while political and institutional reforms that improve economic fundamentals and investor confidence represent critical factors (Ajovalasit et al., 2024; Eichler, 2014).

## III. Estimation Strategy and Data

Sovereign credit spreads can be modeled using both dynamic and static approaches. A dynamic specification with the lagged dependent variable (LDV) is commonly used, where LDV captures persistence and the coefficients on the remaining control variables represent short-run effects. When panel data have a short time dimension, dynamic fixed effects estimators face the issue of Nickell bias, while the application of Generalized Method of Moments (GMM) approaches can be sensitive to instrument proliferation, weak instruments, or exhibit poor finite-sample properties. Simpler approaches that do not include LDV, or static specifications, are also used to estimate determinants of sovereign credits, including by Costantini et al. (2014), Csontó (2014), Eichler (2014), Jeanneret (2018), Li et al. (2024), Ordu-Akkaya and Özyıldırım (2025), Sy (2002), and Vu et al. (2015). Aside from pragmatism, one motivation for static approaches is to let the coefficients capture the long-run total effect and the contemporaneous impact, especially with large T and small N. Static approaches need to be complemented by appropriate standard errors to account for heteroskedasticity, autocorrelation consistent, and/or clustering (see ¶14).

We follow the latter strand of studies and specify the static baseline panel model with the form of equation (1).

$$
y _ {i, t} = \alpha + \beta_ {j} \sum_ {j} x _ {i, j, t} + \gamma_ {k} \sum_ {k} z _ {k, t} * (1 + \theta_ {l} \sum_ {l} D _ {l, t}) + \delta_ {i} + \varepsilon_ {i, t}\tag{1}
$$

The dependent variable $y_{i,t}$ is the external sovereign credit spreads in basis points of the country i in time t. EMBIG spreads, the tenors of which vary depending on the bonds included in each country's index are used for MENA ex-GCC. Credit default swap spreads (CDS), with 5-year tenors, are used for the GCC states for greater data availability. Among independent variables, domestic factors $x_{i,j,t}$ ( $j=1,2,\ldots$ ) are macroeconomic forecasts—real GDP growth, inflation (both in percent, year on year), overall fiscal and external current account balances and public debt (all in percent of GDP), news-based domestic uncertainty index (index value), and indicators of reform progress (average level to measure overall progress, and standard deviation of 5 sub-indices to measure the balance of reforms). External common factors $z_{k,t}$ (k=1,2) are real oil prices (US dollar per barrel, deflated by US inflation) and VIX (index value), both in log. Variables $D_{l,t}$ ( $l=1,2,\ldots$ ) represent either country group dummies or regime dummies, the latter capturing progress in economic diversification (1 when the share of hydrocarbon exports is relatively high) and macroeconomic resilience (1 when sovereign credit ratings, domestic uncertainty index, or public debt to GDP is relatively high). $\delta_{i}$ and $\varepsilon_{i,t}$ are the country fixed effects, which are time-invariant, and the error term. $\alpha$ , $\beta$ , $\gamma$ , and $\theta$ are parameters to be estimated.

An unbalanced panel of data with mixed frequencies for 18 MENA countries is used. In this paper, estimated coefficients on macroeconomic forecasts, oil prices, and investor sentiment (VIX) are used to assess the impact of reforms. In addition, it considers indices of reform progress in five key areas in terms of both average level and standard deviation—Bolen and Sobel (2020) find that the latter variable (standard deviation) capturing the extent of holistic reforms has strong explanatory power. Sovereign credit spreads, macroeconomic forecasts, domestic uncertainty, oil prices, and VIX are monthly. Indicators of reform progress (average and standard deviation), share of hydrocarbon exports, and sovereign credit ratings are annual and repeated for 12 months. Monthly data span December 2014–September 2025, dictated by the availability of forecast data, and cover six GCC and twelve other MENA countries.

Raw data are processed as follows. Monthly forecasts for current and following years are, with moving weights, converted into 12-month constant horizon, similar to Chan et al. (2015) and Gadanecz et al. (2018). Raw data exhibit large variation due to the heterogeneity in the included country sample, complicating the use in a panel format. As an option to mitigate such a challenge, all data are standardized by country into z-score (i.e., distance from the average in the number of standard deviations). The transformation involves demeaning and removing country fixed effects. Finally, 1 percent of data in each tail is dropped (“winsorized”).

The data are generally stationary and errors are adjusted for serial correlation. Results from the Fisher-type augmented Dickey–Fuller test show that the data are generally stationary. The balance of reform, available only annually, is repeated for 12 months and therefore is not stationary—we proceed with the data as such without applying adjustment measures. Serial correlation would emerge from the 12-month moving average transformation discussed above, in addition to the persistence of the dependent variable. Indeed, the Wooldridge test applied to the baseline multivariate specification confirms panel autocorrelation. We therefore use Newey-West standard errors (with 12 lags, accounting for serial correlation from the 12-month moving transformation) which yield results that are similar to results from the Driscoll–Kraay standard errors (which additionally account for cross-sectional dependence).

## IV. Baseline Panel Results

Baseline panel results are presented in two ways. To check how well the model works, that is, whether the estimated coefficients yield expected signs with statistical significance, baseline panel results are obtained by introducing the control variables one by one—univariate models—and also by introducing all of them in one go—a multivariate model.

Baseline panel univariate regression results broadly yield expected signs (Table 1, “Univariate”; and Table A1, models 1–12). When one regressor is used at a time, tightening of sovereign credit spreads is associated with improvements in the forecasts of economic conditions (higher GDP growth, better fiscal and current account balances, and lower inflation), lower domestic uncertainty, greater progress in reform (a higher average index value), more holistic reform (lower standard deviation of index values), and lower global risk aversion (VIX), all statistically significant at least at the 5 percent level. Higher oil prices are associated with tighter sovereign spreads for oil exporters, but they have little systematic impact on oil importers. Surprisingly, public debt-to-GDP forecasts do not show systematic association with sovereign credit spreads.

A baseline m

[中间内容因长度限制已省略]

</td><td>0.159(0.106)</td></tr><tr><td colspan="5">VIX and credit ratings, public debt, and domestic uncertainty</td></tr><tr><td>VIX</td><td>0.322 ***(0.039)</td><td>0.341 ***(0.049)</td><td>0.271 ***(0.036)</td><td>0.331 ***(0.053)</td></tr><tr><td>VIX, ratings = H (total effect)</td><td></td><td>0.271 ***(0.058)</td><td></td><td></td></tr><tr><td>VIX, debt to GDP = H (total effect)</td><td></td><td></td><td>0.416 ***(0.083)</td><td></td></tr><tr><td>VIX, domestic uncertainty = H (total effect)</td><td></td><td></td><td></td><td>0.435 ***(0.058)</td></tr><tr><td>Dummy (ratings, debt/GDP, DU)</td><td></td><td>0.037(0.088)</td><td>0.136(0.113)</td><td>0.071(0.064)</td></tr><tr><td>Intercept</td><td>-0.037(0.053)</td><td>-0.045(0.059)</td><td>-0.099(0.061)</td><td>-0.052(0.070)</td></tr><tr><td>Number of observations</td><td>2013</td><td>2013</td><td>2013</td><td>1297</td></tr></table>

## References

Ajovalasit, Samantha, Andrea Consiglio, Giovanni Pagliardi, and Stavros Zenios. 2024 “Incorporating political risk into analysis of sovereign debt sustainability.” Bruegel.

Bolen, J. Brandon and Russell S. Sobel. 2020. "Does balance among areas of institutional quality matter for economic growth?" Southern Economic Journal 86(4): 1418–45.

Calvo, Sara, and Carmen Reinhart. 1996. "Capital flows to Latin America: Is there evidence of contagion effects?" World Bank Policy Research Working Paper 1619.

Cantor, Richard, and Frank Packer. 1996. “Determinants and impact of sovereign credit ratings.” Economic Policy Review, 2 (2), 37–53.

Chan, Tracy, Ken Miyajima, and M.S. Mohanty. 2015. “Emerging market local currency bonds: Diversification and stability.” Emerging Markets Review, 22, 126–39.

Chernov, Mikhail, Lukas Schmid, and Andres Schneider. 2020. “A Macrofinance View of U.S. Sovereign CDS Premiums.” Journal of Finance, 75, 5, pp. 2809–44.

Cimadomo, Jacopo, Peter Claeys, and Marcos Poplawski-Ribeiro. 2014. “How do financial institutions forecast sovereign spreads?” European Central Bank Working Paper Series 1750.

Cline, William R. 1995. International debt reexamined. Peterson Institute for International Economics.

Costantini, Mauro, Matteo Fragetta, and Giovanni Melina. 2014. “Determinants of sovereign bond yield spreads in the EMU: An optimal currency area perspective.” European Economic Review, 70, 337–49.

Csontó, Balázs. 2014. “Emerging market sovereign bond spreads and shifts in global market sentiment.” Emerging Markets Re-view, 20, 58–74.

David, Antonio, Jaime Guajardo, and Juan Yépez. 2022. “The rewards of fiscal consolidations: Sovereign spreads and confidence effects.” Journal of International Money and Finance, 123, May, 102602.

Edwards, Sebastian. 1984. “LDC foreign borrowing and default risk: An empirical investigation, 1976-80.” The American Economic Review, 74 (4), 726–34.

Eichengreen, Barry, and Ashoka Mody. 1998. "What explains changing spreads on emerging market debt?" in Capital Flows and the Emerging Economies: Theory, Evidence, and Controversies. ed. Sebastian Edwards. 107–134. University of Chicago Press.

Eichler, Stefan. 2014. “The political determinants of sovereign bond yield spreads.” Journal of International Money and Finance, 46, September, 82–103.

Gadanecz, Blaise, Ken Miyajima, and Chang Shu. 2018. “Emerging market local currency sovereign bond yields: The role of exchange rate risk.” International Review of Economics and Finance, 57, 371–401.

Gomez-Gonzalez, Jose E., Jorge M. Uribe, and Óscar M. Valencia. 2025. “Sovereign debt cost and economic complexity.” Journal of International Financial Markets, Institutions and Money, 99, March, 102121.

González-Rozada, Martin, and Eduardo Levy Yeyati. 2008. “Global factors and emerging market spreads.” The Economic Journal, 118 (533), 1917–36.

IMF (2025). Qatar: 2024 Article IV Consultation Staff Report. Country Report No. 25/47

Jeanneret, Alexandre. 2018. “Sovereign credit spreads under good/bad governance.” Journal of Banking and Finance, 93, 230–46.

Kaminsky, Graciela, and Carmen Reinhart. 2000. “On crises, contagion, and confusion.” Journal of International Economics, 51, 145–68.

Laubach, Thomas. 2009. “New evidence on interest rate effects of budget deficits and debt.” Journal of the European Economic Association. 7 (4), 858–85.

Li, Pei, Leo Tang, and C. Bryan Cloyd. 2024. “Political polarization and state government bonds.” Global Finance Journal, 63, 101039.

Longstaff, Francis A., Jun Pan, Lasse H. Pedersen, and Kenneth J. Singleton. 2011. “How Sovereign Is Sovereign Credit Risk?” American Economic Journal: Macroeconomics 3, pp. 75–103.

Min, Hong G. 1998. “Determinants of emerging market bond spread: Do economic fundamentals matter?” World Bank Working Paper 1899.

Ordu-Akkaya, Beyza Mina, and Süheyla Özyıldırım. 2025. “Commodity dependence: Providing information on emerging market CDS spreads when economic indicators are absent.” Emerging Markets Review, 67, 101299.

Reinhart, Carmen, and Vincent Reinhart. 2009. “Capital flow bonanzas: An encompassing view of the past and present.” NBER International Seminar on Macroeconomics, Vol. 5, Issue 1, pp. 1–314.

Reinhart, Carmen. M. and Rogoff, Kenneth S. 2009. This time is different: Eight centuries of financial folly. Princeton University Press.

Sy, Amadou. 2002. “Emerging market bond spreads and sovereign credit ratings: reconciling market views with economic fundamentals.” Emerging Markets Review, 3, 380–408.

Vu, Huong, Rasha Alsakka, and Owain ap Gwilym. “The credit signals that matter most for sovereign bond spreads with split rating.” Journal of International Money and Finance, 53, 174–91.

![](images/ec645b995e9398817bc943c7b38a441c9ebfc35a051aa10b61a7c918529d2eb2.jpg)
"""
