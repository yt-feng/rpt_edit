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
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/393bccd27efdbe85b292d818e7db8520c710f7265d3f5932df101508fe89d102.jpg)

# BIS Working Papers No 1364

Financial and real effects of fiscal risk

by Denis Gorea, Ding Xuan Ng and Fabrizio Zampolli

# Monetary and Economic Department

June 2026

JEL classification: E31, E52, E62, G12, H63

Keywords: fiscal risk, sovereign yields, safe assets, Bayesian VAR; local projections, monetary–fiscal interactions

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# Financial and Real Effects of Fiscal Risk\*

Denis Gorea

Ding Xuan Ng

Fabrizio Zampolli

BIS

BIS and MAS

BIS

June 18, 2026

## Abstract

This paper estimates the macroeconomic and financial effects of fiscal risk shocks using a novel identification from bond yields. We first recover country-specific fiscal risk shocks from a daily Bayesian VAR model in sovereign and safe corporate bond yields, identified via contemporaneous sign restrictions that capture portfolio rebalancing away from government debt toward private safe assets. We then estimate the effects of these shocks using a local-projections framework applied to a monthly panel of twelve economies. Fiscal risk shocks generate stagflationary dynamics. Inflation and inflation expectations rise on impact, while industrial production increases only temporarily before declining persistently. Sovereign yield curves steepen, exchange rates depreciate and equity prices fall. These effects are significantly stronger when monetary policy remains accommodative – leading to persistently negative real interest rates – and when sovereign risk premia are already elevated.

Keywords: fiscal risk; sovereign yields; safe assets; Bayesian VAR; local projections; monetary–fiscal interactions.
JEL codes: E31, E52, E62, G12, H63.

## 1 Introduction

Rising public debt levels have renewed concerns about fiscal sustainability and the macroeconomic consequences of fiscal stress. Episodes in which investors reassess the safety of government debt can raise sovereign borrowing costs, tighten financial conditions more broadly and destabilise inflation expectations. Yet these effects are difficult to identify empirically because government bond yields also respond to monetary policy, inflation news and global risk sentiment, among other factors. In this paper, we develop a novel identification strategy to isolate fiscal risk shocks from bond market data and estimate their macroeconomic and financial effects across twelve countries with sufficiently long daily bond-yield time series.

We define fiscal risk shocks as unanticipated current or future fiscal policy changes that prompt investors to reprice sovereign risk. These changes can stem from fiscal policy actions, policy announcements about future policies (including those not directly related to fiscal policy), or news that change beliefs about future deficit and debt dynamics, on which the associated repayment risk depends. To identify these shocks, we use daily sovereign and corporate bond yield data from the S&P Global Evaluated GSAC Bond Pricing database to estimate country-specific Bayesian VARs. Following Rubio-Ramirez, Waggoner, and Zha (2010), we impose sign restrictions to isolate innovations that raise sovereign bond yields while lowering the yields of the safest corporate bonds of comparable maturity. The identifying assumption – motivated by the institutional portfolio rebalancing channel in Cram, Kung, and Lustig (2024) – is that adverse news or unexpected fiscal policy changes that reduce the relative safety of government debt also induces investors to rebalance toward the highest-grade private assets of similar maturity.

Having identified fiscal risk shocks, we trace their effects by using a two-stage local projections framework applied to a balanced panel of economies for which sufficiently long bond yield data exist. The first stage uses the fiscal risk shock series as an external instrument to isolate specific movements in five-year sovereign bond yields that are directly attributable to shifts in fiscal risk. This procedure scales the shocks to a common and economically interpretable unit - i.e. a one percentage point increase in sovereign yields caused by fiscal risk. The second stage then estimates the response of a broad set of macroeconomic and financial variables, including industrial production, consumer prices, inflation expectations, exchange rates, term spreads and equity prices. The regressions include country fixed effects and macro-financial controls to account for cross-country heterogeneity and prevailing conditions, including the monetary policy stance.

Our estimation results show that fiscal risk shocks have sizeable real and financial effects. Inflation is found to increase on impact, consistent with the view that some adverse fiscal risk events are associated with fiscal expansions that temporarily increase output, while also raising inflation expectations. However, the output response is short-lived, as higher sovereign yields across the yield curve tighten financial conditions for the broader economy. Meanwhile, price pressures take longer to dissipate because inflation expectations remain elevated and exchange rate depreciation raises imported inflation. Over the medium-term, fiscal risk shocks become contractionary: within about six quarters, higher yields and borrowing costs lead to a persistent slowdown in real activity and decline in equity valuations.

The effects of fiscal risk shocks depend on the monetary policy response and on the initial level of sovereign risk. The impact on inflation and the subsequent decline in output are amplified when monetary policy is accommodative – defined as episodes in which central banks adjust monetary policy rates by less than expected under an estimated Taylor rule after a positive fiscal risk shock. In these episodes, accommodative monetary policy provides only a temporary cushion against higher borrowing costs since yields rise significantly across maturities after about one year. The inflationary impact of fiscal risk shocks is also more intense in countries that already experience elevated sovereign risk as measured by sovereign CDS spreads. In such countries, the responses of inflation and inflation expectations are larger and more persistent, while equity valuations and term spreads both fall in the medium-term, signalling potential negative impact on potential growth.

To support the interpretation of these effects as responses to genuine repricing of fiscal risk rather than anticipated policy changes or other confounding factors, we subject our shock series to an extensive battery of validation tests. Narrative validation confirms that the shocks align with major fiscal events, such as the 2025 U.S. tariff announcements and the passing of the "Big Beautiful Bill," the eurozone debt crisis in the early 2010's and the UK Brexit referendum of 2016, while remaining distinct from political noise such as government shutdowns. Furthermore, following Bauer and Swanson (2023), we show that the shocks are orthogonal to lagged macroeconomic indicators and professional forecasts, confirming that our identification strategy successfully isolates unanticipated repricing of fiscal risk.

Our main results are robust to alternative model specifications and inference methods. The estimated impulse responses remain broadly unchanged when fiscal risk shocks are obtained from alternative VAR specifications, including models with additional variables, different sovereign and corporate bond maturities and longer lag structures. The results are also robust to Bayesian standard error estimates and to accounting for uncertainty in

the estimation of the shock series.

Related literature. This paper contributes to two strands of literature. First, it adds to the growing body of research examining the interaction between sovereign risk and macro-financial conditions. Existing studies show that sovereign debt plays a "benchmark" role in financial markets and that changes in sovereign risk affect private borrowing costs, asset prices and real activity. Almeida et al. (2017) find that a sovereign rating downgrade is associated with rising cost of debt for firms, while Acharya, Drechsler, and Schnabl (2014) show that there is significant co-movement between bank CDS and sovereign CDS when sovereigns experience a spike in default risk and public debt ratios are high. Augustin et al. (2018) show that corporate credit risk spikes during sovereign distress events, particularly for firms that are more dependent on banks or governments. Cardamone (2025) finds that increases in U.S. sovereign risk have stagflationary effects and depress stock and corporate bond prices. We contribute to this literature by developing a new identification strategy that isolates market-based repricing of sovereign risk across several economies at a daily frequency. Our findings show that such shocks raise sovereign yields, reduce equity prices and generate a combination of higher inflation and weaker medium-term economic activity.

Second, the paper contributes to the literature on fiscal-monetary interactions. Classic contributions show that the macroeconomic effects of fiscal policy depends on the joint behaviour of fiscal and monetary authorities, especially when fiscal policy is active and monetary policy is passive (Sargent and Wallace, 1984; Leeper, 1991; Sims, 1994; Woodford, 1995). More recent work studies how fiscal imbalances, debt valuation and inflation expectations interact under alternative policy regimes (Bianchi and Ilut (2017); Bianchi and Melosi (2019); Bassetto and Sargent, 2020; Cochrane, 2022; Bianchi, Faccini, and Melosi, 2023; Smets and Wouters, 2024). We contribute to this literature by highlighting the role of financial markets in the transmission of fiscal risk. Much of the fiscal theory of the price level derives conditions under which fiscal imbalances affect the price level, but generally abstracts from the market mechanisms through which fiscal stress is priced and transmitted. In these models, the price level adjusts to restore the government's intertemporal budget constraint, while the chain of events linking fiscal news to inflation and output is often left implicit. We provide evidence that this transmission operates through sovereign risk premia, portfolio rebalancing, exchange rates, equity valuations, and the yield curve. These financial channels influence both the inflationary and contractionary effects of fiscal risk shocks. Consistent with this view, we find that fiscal risk shocks are more inflationary and more contractionary when monetary policy accommodates the shock and when sovereign risk premia are already elevated. These findings highlight the role of monetary credibility and fiscal space in influencing the transmission of fiscal stress.

## 2 Data

Our analysis relies on data obtained from multiple sources. We describe below each of the sources and explain briefly how the data was processed. Appendix A provides more details on the data and the exact filters applied.

Bond data. Our main data source is the S&P Global Evaluated GSAC Bond Pricing Data which contains information on over 215,000 local government, sovereign, agency and corporate bonds across 70 currencies between 2010 and 2025. The data set has information on prices and yields for each bond, as well as other detailed instrument characteristics such as ISIN, face value, maturity, coupon value, type and payment frequency. S&P Global sells the bond pricing data to its clients and strives to have comprehensive coverage even for most difficult-to-price securities. To achieve this, the bond price data integrates inputs from four sources. First, buy and sell trades are drawn from FINRA's TRACE database. Second, dealer runs are used to supplement the data and provide parsed prices, spreads, yields, and discount margins. For USD-denominated bonds, dealer-run bid-ask spreads may be adjusted to reflect prevailing execution dynamics. Third, the database also relies on contributions via agreements with a large number of market participants for real-time prices, iBoxx index constituent contributions, third party providers, and bank feeds (including end-of-day books of records). Last, interdealer broker quotes are used to supplement coverage, particularly for local government and sovereign debt.

We construct our sovereign bond sample by first filtering bonds classified as government bonds, ensuring that our sample includes solely sovereign bonds and not bonds of local government entities or government agencies. We also restrict our sample to bonds with fixed non-negative coupons for which S&P Global reports a yield-to-maturity for both corporate and sovereign bonds. For corporate bonds, we restrict our sample to include only non-financial firms and also exclude bonds issued by firms classified as Utilities, Basic Materials, and Energy. This filter is meant to ensure that we focus only on corporate bonds of firms that are less likely to hold large quantities of sovereign bonds, as is the case for financial firms, and firms that are less likely to be owned or influenced via a golden share structure by governments, such as energy firms. Appendix A.1 contains more details of the exact filtering procedures we applied to the raw data.

After implementing our preliminary set of filters, we construct a harmonized bond sample across countries by aligning the coupon currency across sovereign and corporate issues within in each country. $^{1}$ We further restrict our sample of bonds to non-inflation-linked securities and focus only on bonds with remaining time to maturity of around five years. $^{2}$ For each country-date, we then compute the median yield of sovereign bonds that have close to a five year maturity. For corporate bonds, we obtain the median from a subset of the lowest-yielding 20 bonds to proxy the safest firms issuing bonds at the same maturity of five years. $^{3}$ The composition of the subset of safest corporate bonds is allowed to change every day, but in practice remains relatively constant as safe borrowers turn out to be persistently safe across our sample period. $^{4}$

We then merge the two median yield series by date and apply additional data quality controls: truncating corporate yield medians on days with unusually wide corporate-sovereign spreads (above 10 percentage points), retaining for each country the longest near-continuous sequence of observations of yields with only short gaps of below five days and discarding countries without such a valid sequence. To obtain a daily panel suitable for estimation using an autoregressive model with consecutive lags, we forward-fill missing values within sample for each country, recognizing that yields may be stale over weekends and holidays where we see missing observations in the raw data. Finally, we winsorize both sovereign and corporate medians at the top and bottom 0.1 percentile to mitigate the influence of outliers without removing observations. Appendix A.2 describes in greater detail the data processing steps used to prepare our bond-level data for estimation.

Macroeconomic data. We construct an unbalanced monthly panel of aggregate macroeconomic and financial indicators used to estimate the economic impact of fiscal risk shocks. The monthly panel spans 2012-2025, and includes 12 economies primarily comprised of

AEs. While the bond data includes 60 countries, only 12 countries that have at least 84 months of available data within the panel period for our chosen baseline fiscal risk shock series–based on 5-year bonds—are retained in the monthly panel. $^{5}$ The monthly frequency for the panel is chosen to maximize availability of macroeconomic and financial data across sample countries (as macroeconomic indicators from national sources are typically available at the monthly frequency at most), while exploiting the higher frequency of our shock series to the greatest extent possible.

We include standard aggregate macroeconomic indicators that are broadly available across countries at the monthly frequency. Principally, these comprise Industrial Production, Composite PMI $^{6}$ , headline CPI and policy interest rate series published by national sources, while 1-year ahead inflation expectations data are Consensus forecasts from monthly polls of professional forecasters. The set of financial indicators we use includes monthly averages of nominal effective exchange rates, government bond yields based on monthly averages of benchmark bid yields in local currency terms, and stock prices based on monthly averages of local currency market-capitalization weighted composites from major national stock exchanges. For details on data sources for country-level aggregates, see Appendix B.

## 3 Estimation

We rely on two econometric models to estimate fiscal risk shocks across countries and their impact on financial and macroeconomic variables. We explain below each of the models used in our analysis and the estimation routines we employ.

## 3.1 Bayesian Vector Autoregressions

To assess the impact of fiscal risk shocks on asset prices and macroeconomic outcomes such as industrial production and GDP growth, we estimate a vector autoregression (VAR) with sign restrictions to recover structural shock series for fiscal risk. For each country in our sample of corporate and sovereign bond yields, we estimate the following daily VAR model:

$$
y _ {t} = \sum_ {j} A _ {j} y _ {t - j} + \mu_ {0} + u _ {t},\tag{1}
$$

where $y_{t}$ is a vector of two variables, $A_{j}$ are matrices of autoregressive parameters, $\mu_{0}$ is a vector of constant terms, and the error term $u_{t} = B\epsilon_{t}$ is a function of the impact matrix B and the structural shocks $\epsilon_{t}$ with zero mean and an identity variance-covariance matrix, such that these shocks are uncorrelated. The two endogenous variables included in the country-specific VAR model are: (i) median yield for sovereign bonds, and (ii) median yield for the safest corporate bonds in each country. The VAR model has four lags (j = 4). $^{7}$ We estimate the model using Bayesian techniques and the Minnesota p

[中间内容因长度限制已省略]

ee Bi, Leeper, and Leith (2013)).

To test whether the macro-financial transmission differs by shock direction, the second stage is augmented with a sign indicator and its interaction with the instrumented yield. Let $D_{i,t}^{+} = \mathbf{1}\{s_{i,t} > 0\}$ denote an indicator that equals unity when the underlying fiscal risk shock is positive—an unanticipated deterioration in fiscal positions—and zero otherwise. The augmented second-stage regression is:

$$
\begin{array}{r} y _ {i, t + h} - y _ {i, t - 1} = \alpha_ {i} ^ {(h)} + \delta^ {(h)} \widehat {\mathbf {y i e l d 5 Y}} _ {i, t} + \gamma^ {(h)} \left(D _ {i, t} ^ {+} \cdot \widehat {\mathbf {y i e l d 5 Y}} _ {i, t}\right) + \pi^ {(h)} D _ {i, t} ^ {+} \\ + \sum_ {\ell = 1} ^ {L _ {c}} \gamma_ {\ell} ^ {(h) \prime} \mathbf {x} _ {i, t - \ell} + \sum_ {\ell = 1} ^ {L _ {y}} \phi_ {\ell} ^ {(h)} \Delta y _ {i, t - \ell} + \varepsilon_ {i, t + h} ^ {(h)} \end{array}\tag{12}
$$

Here $\delta^{(h)}$ captures the baseline 2SLS response on negative-shock episodes ( $D_{i,t}^{+}=0$ ), and $\hat{\gamma}^{(h)}$ is the asymmetry differential: the additional marginal response on positive-shock episodes relative to negative ones following a 1-percentage-point fiscal-risk-driven increase in yield5Y. The level control $\pi^{(h)}D_{i,t}^{+}$ absorbs unconditional mean differences in outcomes between sign regimes.

Figure G.1 reports the estimated sequence $\left\{\hat{\gamma}^{(h)}\right\}_{h=0}^{24}$ alongside 67% IV-corrected clustered confidence bands. A positive value at horizon h indicates that a 1-percentage-point fiscal-risk-driven yield increase has a larger effect on the outcome when the underlying fiscal risk shock is positive (rising risk premia) than when it is negative (falling risk premia).

Results demonstrate that asymmetry is statistically significant across multiple outcome variables, although the magnitude of effects are small across all dependent variables. First, positive fiscal risk shocks generate persistently larger upward pressure on CPI inflation and inflation expectations relative to mirror-image episodes of declining fiscal risk, indicating that the inflationary transmission of fiscal deterioration is stronger and more durable than the disinflationary relief from fiscal improvement. Second, real activity effects are directionally asymmetric in the short run—an increase in fiscal risk dampens the boost in real activity in the initial months after the shock, seen in Figure 3—but not beyond two years. Third, long-end yields and equity prices are more sensitive to adverse fiscal surprises than to equivalent improvements in fiscal risk, pointing toward a tighter financial conditions channel under adverse fiscal surprises.

Results are similar when estimating $\{\hat{\gamma}^{(h)}\}_{h=0}^{24}$ in a model which includes the passive monetary policy indicator, as in Equation 10. An alternative test for asymmetry, that plots total effects in IRFs for positive and negative fiscal risk shocks, obtained from a specification that embeds the sign dummy in the first stage rather than the second stage, obtains similar results.

![](images/e33e671abf068bb6f8de56cf1fe7cd01de051ea8f0f2be13067420c059c0fc17.jpg)  
Figure G.1: Asymmetry differential $\hat{\gamma}^{(h)}$ : positive vs. negative fiscal risk shock episodes

Notes: Estimated asymmetry differential $\hat{\gamma}^{(h)}$ from equation (12) at each horizon $h = 0, \ldots, 23$ months. A positive value indicates a larger response to a 1-pp fiscal-risk-driven yield increase on positive-shock $D_{i,t}^{+} = 1$ than on negative-shock episodes. Controls include the passive-MP indicator $D_{i,t}^{MP}$ and country fixed effects. Shaded bands: 67% IV-corrected clustered confidence intervals using the generated-regressor sandwich correction.

## H Alternative Measure of Passive Monetary Policy

To capture episodes of monetary accommodation, a simpler binary indicator $D_{i,t}^{MP}$ is constructed that equals unity in country-month observations classified as passive monetary policy regimes—periods in which the central bank does not raise the nominal policy rate sufficiently to prevent the ex-post real rate from being persistently negative, thereby accommodating the inflationary pressures that may accompany a fiscal expansion rather than offsetting them through active tightening.

Formally, the indicator passiveMP $_{i,t}$ is defined as:

$$
\mathrm{passiveMP} _ {i, t} = \mathbf {1} \left[ s _ {i, t} > 0 \land \sum_ {k = 1} ^ {8} \mathbf {1} \left[ r _ {i, t + k} ^ {\text {real}} <   0 \right] \geq 6 \right],\tag{13}
$$

so that passive monetary policy is declared when the shock is positive and real rates remain negative for at least six of the eight months following the shock, indicating a sustained accommodative stance. $^{28}$

Results are shown in Figure H.1, with results similar in direction to Figure 4 for all dependent variables within a two-year horizon.

$$
r _ {i, t} ^ {\mathrm{real}} = i _ {i, t} - 1 2 \cdot \frac {\mathrm{CPI} _ {i , t + 1} - \mathrm{CPI} _ {i , t}}{\mathrm{CPI} _ {i , t}}
$$

![](images/439360dc6ad05de1e44189880082c4f9fed4ba0d4b273821e7af17858fa9f01f.jpg)  
Figure H.1: Monetary accommodation premium $\hat{\gamma}_{A}^{(h)}$ : simple measure of passive monetary policy  
Notes: Estimated accommodation premium $\hat{\gamma}_{A}^{(h)}$ from equation (10) at each horizon $h = 0, \ldots, 23$ months. A positive value indicates a larger response to a 1-pp fiscal-risk-driven yield increase during passive monetary policy episodes ( $D_{i,t}^{MP} = 1$ ) relative to active episodes, conditional on a positive underlying fiscal risk shock. Shaded bands: 67% IV-corrected clustered confidence intervals.
"""
