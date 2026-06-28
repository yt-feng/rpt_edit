你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

We include standard aggregate macroeconomic indicators that are broadly available across countries at the monthly frequency. Principally, these comprise Industrial Production, Composite PMI $^{6}$ , headline CPI and policy interest rate series published by national sources, while 1-year ahead inflation expectations data are Consensus forecasts from monthly polls of professional forecasters. The set of financial indicators we use includes monthly averages of nominal effective exchange rates, government bond yields based on monthly averages of benchmark bid yields in local currency terms, and stock prices based on monthly averages of local currency market-capitalization weighted composites from major national stock exchanges. For details on data sou

[中间内容因长度限制已省略]

tage regression is:

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
