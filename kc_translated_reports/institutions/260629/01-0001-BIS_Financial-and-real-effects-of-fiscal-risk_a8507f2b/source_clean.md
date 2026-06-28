# BIS Working Papers No 1364
# Monetary and Economic Department

Keywords: fiscal risk, sovereign yields, safe assets, Bayesian VAR; local projections, monetary–fiscal interactions

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).


# Financial and Real Effects of Fiscal Risk\*


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


AEs. While the bond data includes 60 countries, only 12 countries that have at least 84 months of available data within the panel period for our chosen baseline fiscal risk shock series–based on 5-year bonds—are retained in the monthly panel. $^{5}$ The monthly frequency for the panel is chosen to maximize availability of macroeconomic and financial data across sample countries (as macroeconomic indicators from national sources are typically available at the monthly frequency at most), while exploiting the higher frequency of our shock series to the greatest extent possible.

We include standard aggregate macroeconomic indicators that are broadly available across countries at the monthly frequency. Principally, these comprise Industrial Production, Composite PMI $^{6}$ , headline CPI and policy interest rate series published by national sources, while 1-year ahead inflation expectations data are Consensus forecasts from monthly polls of professional forecasters. The set of financial indicators we use includes monthly averages of nominal effective exchange rates, government bond yields based on monthly averages of benchmark bid yields in local currency terms, and stock prices based on monthly averages of local currency market-capitalization weighted composites from major national stock exchanges. For details on data sources for country-level aggregates, see Appendix B.

## 3 Estimation

We rely on two econometric models to estimate fiscal risk shocks across countries and their impact on financial and macroeconomic variables. We explain below each of the models used in our analysis and the estimation routines we employ.

## 3.1 Bayesian Vector Autoregressions

To assess the impact of fiscal risk shocks on asset prices and macroeconomic outcomes such as industrial production and GDP growth, we estimate a vector autoregression (VAR) with sign restrictions to recover structural shock series for fiscal risk. For each country in our sample of corporate and sovereign bond yields, we estimate the following daily VAR model:

$$
y _ {t} = \sum_ {j} A _ {j} y _ {t - j} + \mu_ {0} + u _ {t},\tag{1}
$$

where $y_{t}$ is a vector of two variables, $A_{j}$ are matrices of autoregressive parameters, $\mu_{0}$ is a vector of constant terms, and the error term $u_{t} = B\epsilon_{t}$ is a function of the impact matrix B and the structural shocks $\epsilon_{t}$ with zero mean and an identity variance-covariance matrix, such that these shocks are uncorrelated. The two endogenous variables included in the country-specific VAR model are: (i) median yield for sovereign bonds, and (ii) median yield for the safest corporate bonds in each country. The VAR model has four lags (j = 4). $^{7}$ We estimate the model using Bayesian techniques and the Minnesota prior (Giannone, Lenza, and Primiceri, 2015), with prior mean for the autoregressive parameters reflecting unit-root non-stationarity of the variables.

Sign Restrictions. The identification of fiscal risk shocks relies on sign restrictions in a partial identification sense as in Rubio-Ramirez, Waggoner, and Zha (2010). We set sign restrictions such that a fiscal risk shock is assumed to raise sovereign debt yields while reducing yields for the safest bonds in the same country. These sign restrictions are motivated by the evidence in Cram, Kung, and Lustig (2024) showing that institutional investors tend to re-balance away from long-maturity sovereign bonds and into safe corporate bonds of similar maturity during episodes characterized by outsize government spending that is not offset by explicit or implicit promises of future fiscal surpluses.

What risks to sovereign bonds do our shocks capture? When fiscal authorities spend without a clear plan to repay through future surpluses, holding sovereign debt becomes risky for two reasons. First, if governments are out of fiscal space, new government spending increases sovereign default risk (Ghosh et al., 2013). Second, new government spending leads to an increase in inflation risk if monetary policy rates do not rise to account for higher spending. $^{8}$ While unexpected inflation lowers the real value of future coupons for both corporate and sovereign bonds equally (Ang, Bekaert, and Wei, 2008), our shocks capture a crucial structural asymmetry between these issuers. When a government faces higher inflation, a sizeable fraction of its expenditures automatically rise due to heavily indexed transfer programs and automatic stabilizers, whereas revenues remain less contemporaneously elastic (Hilscher, Raviv, and Reis, 2022). This automatic drop in the primary balance reduces fiscal space and can more than offset the relief from inflation eroding the real value of nominal liabilities. By contrast, "safe" investment-grade firms are insulated from these inflation-induced fiscal pressures as they have fewer indexed cost obligations, maintain pricing power, and possess operational flexibility to shift production across borders to escape domestic cost shocks. As a result, severe inflation spikes induce a rise in sovereign risk premia but do not necessarily translate in higher credit risk premia for the safest corporates. By enforcing negative comovement in yields, our sign restrictions filter out symmetric inflation risk shocks and explicitly isolate realizations of sovereign default risk induced by inflation risk.

The bond yield divergence sign restrictions are grounded in two primary theoretical microfoundations: i) incomplete pass-through of sovereign risk to safe corporates, and ii) the pricing of government bonds as assets that earn a convenience yield. First, theoretical frameworks of sovereign default explicitly limit the pass-through of sovereign distress to the private sector. Uribe (2006) demonstrates that a government can choose to explicitly default on its obligations without expropriating private corporate assets, allowing a default risk premium to emerge strictly within the sovereign yield. Furthermore, even when a sovereign-bank nexus exists—where a drop in the expected value of government bonds depletes domestic bank capital—the tightening of corporate credit conditions is not one-for-one. As modeled by Corsetti et al. (2013), because financial intermediary balance sheets are globally diversified, corporate borrowing costs rise by only a fraction of the increase in the sovereign spread, contributing to divergence in sovereign and safe corporate bond yields. In open economy settings, this insulation is even stronger; Arel-lano (2008) assumes that the sovereign lacks the full capacity to tax or expropriate from globally diversified multinational corporations, structurally shielding safe international corporate bonds from domestic fiscal limits.

Second, the divergence is theoretically consistent with the compression of sovereign convenience yields. An extensive literature establishes that the demand for government bonds derives heavily from the non-pecuniary liquidity and safety services they provide. To quantify this premium, one popular measure of the convenience yield (e.g., Krishnamurthy and Vissing-Jorgensen, 2012) is derived as the yield spread between highly rated AAA corporate bonds and government bonds. When fiscal risk materializes, the information-insensitive safety property of sovereign bond weakens. Consequently, the marginal utility of its liquidity services declines, compressing the convenience yield. Our identification scheme captures this exact spread compression. As sovereign yields rise to clear the market, the institutional demand for safety—as documented empirically by

Cram, Kung, and Lustig (2024)—shifts toward highly rated corporate bonds, bidding down their yields and fulfilling our sign restriction.

Bayesian Estimation. The sign restrictions are applied on the contemporaneous impulse responses. For each country, we sample 1000 independent draws from the posterior distribution to estimate model parameters and recover the shock series in standardized form for each draw. For our baseline local projection analysis in section 3.2, we follow Fry and Pagan (2011) and use the daily median target shock values estimated from the Bayesian VAR (BVAR) as our baseline fiscal policy shocks. The median target shocks are those for which yield responses to structural shocks are the closest to the median response over a 30-days horizon. $^{9}$ We then aggregate the shocks to a monthly and quarterly frequency for shock validation and local projections by summing up the shock series across days in each month or quarter.

Shock Validation. We validate our shock series both graphically and statistically. Graphical validation is performed by comparing the estimated shocks to known events that may trigger a re-assessment of the fiscal position of a country. Statistical validation includes correlation analysis with well-established monetary policy shock series and alternative measures of fiscal shocks, as well as regression-based tests for predictability using past macroeconomic variables.

Figure 1 shows the evolution of the estimated structural fiscal risk shocks for the US in 2025. Positive values of the shock series indicate days when bond markets participants perceived a worsening of the US fiscal situation, while negative values suggest improvements. We marked key events that may have had important fiscal implications along the timeline to highlight how our shock series line up with such events. For our shocks to effectively capture fiscal developments, the series should exhibit pronounced changes in response to events that have the potential to significantly alter a country's fiscal situation.

A few events stand out in Figure 1. The announcement of US tariffs on April 2 (referred to as "Liberation day" in the plot) was perceived by bond market participants as an event that would improve the fiscal situation of the United States. This perception likely stemmed from the expectation that tariff revenues would help reduce the fiscal deficit by generating additional tax income, outweighing the potential revenue losses caused by


[[KC_IMAGE_001]]

Figure 1: Estimated fiscal risk shocks for the U.S. in 2025

Notes: This figure shows the evolution of fiscal risk shocks in the US in 2025. The thick line represents the median target shock from the distribution of shocks recovered following the estimation of the model in equation (1). The shaded area stands for the 90% interval from the distribution of shocks. Several important events are highlighted in the figure using vertical dotted lines, with positive shocks labelled and red and negative shocks labelled in blue: (i) President Trump's inauguration day, (ii) the announcement of "Liberation" day tariffs, (iii) the US-UK trade deal, (iv) the adoption of the Big Beautiful Bill legislation, (v) the start of the US government shutdown, and (vi) the end of the shutdown.

reduced economic activity following the introduction of the tariff. In contrast, the spike in the shock series on the day of "US-UK trade deal" (May 8) reflects negative adjustments in market sentiment of fiscal risk, as the trade deal reduced the effective tariff rate and signaled that tariff revenues may be lower than expected going forward since more countries were expected to get tariff rate reductions thereafter. Similarly, the adoption of "Big Beautiful Bill (BBB)" (July 3) appears to coincide with a significant positive fiscal risk shock, potentially due to concerns about the fiscal sustainability of the adopted tax legislation.

Significant changes in our shock series also line up with events that are relevant for bond markets in terms of impact of inflation on sovereign bonds versus safest sovereign bonds. The "July CPI report" released on August 12 showed that inflation was settling at levels above 2 percent, suggesting that persistent inflation may be weighing down on sovereign bonds due to a worsening of primary balances induced by increases in nominal inflation-indexed government outlays such as social security. Interestingly, the "Inauguration day" (January 20) and the "Shutdown start" (October 1) did not correspond to a notable change in the fiscal policy shock series. This shows that our series is not necessarily a reflection of political risks. Nonetheless, the resolution of political uncertainty when the shutdown ended (November 12) did result in a spike in fiscal risk shocks, suggesting that the resolution was perceived to increase unsustainable fiscal spending, as there was


[[KC_IMAGE_002]]

Figure 2: Estimated fiscal risk shocks for Notable Fiscal Events

Notes: This figure shows the evolution of fiscal risk shocks for two well-known events: Spain during the Eurozone crisis peak (June–July 2012) and the United Kingdom around the Brexit referendum (June 2016). The thick line represents the median target shock from the distribution of shocks recovered following the estimation of the model in equation (1). The shaded area stands for the 90% interval from the distribution of shocks.

no significant reduction in spending commitments by the US government following the shutdown.

Figure 2 provides two further validation cases of well-known events beyond the US: Spain during the Eurozone crisis peak (June–July 2012) and the United Kingdom around the Brexit referendum (June 2016). In the left panel, the Spanish fiscal risk shock series exhibits pronounced movements around the key events of that period. The announcement that Spain would request a €100 billion ESM bailout on June 25 coincides with a positive fiscal risk shock, reflecting market participants' recognition of significant bank-sovereign linkages in Spain, while the EU summit agreement on bank recapitalization on June 29 is associated with a negative shock. The announcement from the summit that the ESM could recapitalize banks directly reduced pressures for banks to sell of Spanish debt, and was associated with improved perceptions of Spain's fiscal outlook. A similar pattern emerges around the formal approval of Spain's bailout on July 20, which registers as a positive shock—likely reflecting residual uncertainty about implementation, while Mario Draghi's "Whatever it takes" speech on July 26 corresponds to a sharp negative fiscal risk shock, consistent with the view that the ECB's commitment to defend the euro substantially reduced perceived sovereign fiscal stress in the periphery. $^{10}$

In the right panel, the Brexit referendum period for the United Kingdom shows that the Leave vote on June 23 is associated with a positive fiscal risk shock, reflecting market concerns about the fiscal consequences of a potential economic slowdown following the UK's departure from the EU. Chancellor Osborne's prior speech announcing consolidation measures to "balance books" on June 15 registers as a negative shock, while the S&P downgrade of the UK sovereign rating to AA on June 28 coincides with a further positive shock, reflecting that our shocks incorporate repricing of fiscal risk by participants when new information is released. Large fiscal risk shocks were also associated with two other well-known episodes of fiscal risk repricing –the 2016 Trump election in the US and the 2022 Liz Truss mini-budget in the UK, as shown in Appendix Figure E.1


Table 1: Correlation of US fiscal policy shocks with Treasury and monetary policy shocks
Notes: This table reports correlation coefficients between our measures of median target shocks for the US and various other existing measures of shocks affecting US Treasury yields that may correlate with fiscal risk shocks. The table also includes p-values for the correlation coefficients. Last two columns of the table show correlation coefficients and their p-values based only on the dates when the shock is estimates in existed studies. Other coefficients and p-values in the table are based on the entire sample, with zero values inserted in the other shock series for days outside the respective shock dates. Daily data was used to compute values in this table.

Aside from graphical validation, we report a battery of statistical tests aimed at further validating our shocks series. Table 1 reports the correlation between the fiscal risk shocks that we recover for the US and Treasury and monetary policy shocks series constructed in other papers. Since the frequency of our shock series is daily while the frequency of Treasury and monetary policy shock series is specific to dates of Treasury auctions or monetary policy announcements, we report two correlation coefficients for each shock in Table 1. First, we fill with zeros the shock series that are not daily and compute the correlation between this daily shock series and our daily median target shock series. Second, we compute the correlation between shocks on dates specific to each shock series from other papers. For example, in the case of Treasury supply shocks from Phillot (2025) we compute the correlation between our shocks and these shocks only on Treasury auction dates used to construct the supply shock series. Table 1 shows that irrespective of the frequency of the data, the correlation coefficients between our shock series and other shocks that may influence sovereign bonds are close to zero or statistically indistinguishable from zero at a 5 per cent level. While low or no correlation with other shock series is not a pre-requisite for our shocks to capture fiscal risk, it is nonetheless reassuring that our shocks are capturing innovations in yields that existing measures do not seem to map. The maximum correlation of 0.3351 is achieved with treasury demand shocks (Ray, Droste, and Gorodnichenko, 2024) on dates of treasury demand shock, which is statistically significant at the 1 per cent level. This relatively low correlation is benign for our identification as it is precisely shifts in demand for Treasuries that underpin our sign restrictions. Furthermore, in Appendix D we report pairwise correlations between our country-specific fiscal risk shocks and the country-specific monetary policy shocks in Choi, Willems, and Yoo (2024). Correlations are close to zero and statistically insignificant for nearly all countries in our sample.


Table 2: Correlation of US fiscal policy shocks with other shocks
Notes: This table reports correlation coefficients between our measures of median target shocks for the US and various other existing measures of shocks that may impact the fiscal outlook. The table also includes p-values for the correlation coefficients. The correlations are computed based on monthly shock data.

We also report in Table 2 how our shock series compare to other prominent shock series that may impact the fiscal situation of the US. These shock series have a monthly frequency and we compute the correlation coefficients using the monthly aggregates of our shock series, where aggregation is done by summing up the daily shocks within a month. As in the case of Table 1, the correlation coefficients are either close to zero, statistically indistinguishable from zero at the 5 per cent level, or modest as is the case of the correlation with oil supply news shocks which stands at 0.2301. This evidence is reassuring from an identification stand point, as it indicates that our shock series are not capturing other shocks (e.g., monetary policy shocks) that may be responsible for variation in bond yields in the days when we identify our shocks.

Beyond correlations, we assess orthogonality of our shock series to macroeconomic and financial news preceding the day of the shock by testing whether our fiscal risk shock series are predictable by other observables, following Bauer and Swanson (2023). We run predictability exercises at quarterly, monthly, and daily frequencies, aggregating daily shocks by summation to match lower-frequency predictors where necessary. We estimate panel OLS regressions with country and time fixed effects and report our results in Appendix D. We find that lagged changes in CPI and GDP do not predict quarterly shocks. Similarly, regressions that include lagged forecasts of GDP and CPI, lagged changes in policy rates, and lagged deficit forecasts yield coefficients that are statistically indistinguishable from zero. At the daily frequency, equity market performance immediately prior to the shock date has no predictive content either. Taken together, these results indicate that our shocks are orthogonal to standard macroeconomic and financial indicators used in the literature.

## 3.2 Local Projections

We use a local projections procedure to estimate the macro-financial impact of a 1 percentage point increase in 5-year government bond yields due to a fiscal risk shock. Impulse response functions are estimated using a standard local projections framework as in Jordà (2005), extended to a panel setting with country fixed effects. For each outcome variable y and forecast horizon $h \in \{0, 1, \ldots, H\}$ , the following regression is estimated separately:

$$
y _ {i, t + h} - y _ {i, t - 1} = \alpha_ {i} ^ {(h)} + \beta^ {(h)} s _ {i, t} + \sum_ {\ell = 1} ^ {L _ {y}} \phi_ {\ell} ^ {(h)} \Delta y _ {i, t - \ell} + \sum_ {\ell = 1} ^ {L _ {c}} \gamma_ {\ell} ^ {(h) \prime} \mathbf {x} _ {i, t - \ell} + \varepsilon_ {i, t + h} ^ {(h)}\tag{2}
$$

where $s_{i,t}$ is the monthly fiscal risk shock for country i at time t, $\alpha_{i}^{(h)}$ is a country fixed effect, $x_{i,t-\ell}$ is a vector of lagged control variables, and $\varepsilon_{i,t+h}^{(h)}$ is the regression residual, which is serially correlated by construction for h > 0. $^{11}$

The left-hand side $y_{i,t+h} - y_{i,t-1}$ is the long-difference of the outcome variable from period t - 1 to $t + h$ , so that the sequence of estimated coefficients $\{\hat{\beta}^{(h)}\}_{h=0}^{H}$ directly traces the cumulative impulse response relative to the pre-shock baseline. For log-transformed outcomes the coefficient approximates a percentage change (multiplied by 100); for rate variables it is in matching units.

Our baseline empirical model is estimated using monthly panel data, for the following macro-financial indicators. Dependent variables $y_{i,t}$ include macroeconomic outcomes, such as, headline CPI, industrial production, Composite PMI, Consensus 1-year ahead inflation expectations of professional forecasters and trade-weighted nominal exchange rates. We also use aggregate indicators of financial conditions as dependent variables, such as, the 10-year government bond yields, the term spread between 10- and 1-year government bond yields, and stock prices. Four lags of the following control variables $x_{i,t}$ are included in regressions for all dependent variables: headline CPI, industrial production, the 5-year sovereign CDS spread, and the 1-year government bond yield. Two lags of each dependent variable is included in the respective regression, except for dependent variables that are also control variables (headline CPI and industrial production).

Two-Stage Local Projections. We adopt a two-stage local projections (2SLS-LP) procedure, which enables us to normalize fiscal risk shocks by percentage point units (of 5-year government bond yields). Structural fiscal risk shocks recovered from the BVAR methodology are measured in standard deviations that are difficult to interpret, as the underlying structural shock from the VAR is only identified up to a constant diagonal matrix.

In the first stage, the realized 5-year sovereign yield is projected onto the fiscal risk shock (the external instrument), and the full set of lagged controls from equation (2). The fitted values $\widehat{yield5Y_{i,t}}$ capture the component of the 5-year yield that is attributable to fiscal risk surprises, controlling for lagged indicators of the macro-financial state and autocorrelation. As reported in the preceding section, our external instrument, the monthly fiscal risk shock, cannot be predicted by macroeconomic and financial indicators, providing evidence for instrument validity. At the same time, we affirm the relevance of the external instrument for the 5-year government yields used in the first stage. $^{12}$

In the second stage, the LP regressions (2) are estimated with fitted 5-year government bond yield values $\widehat{yield5Y_{i,t}}$ :

$$
y _ {i, t + h} - y _ {i, t - 1} = \alpha_ {i} ^ {(h)} + \delta^ {(h)} \widehat {\mathbf {y i e l d 5 Y}} _ {i, t} + \sum_ {\ell = 1} ^ {L _ {y}} \phi_ {\ell} ^ {(h)} \Delta y _ {i, t - \ell} + \sum_ {\ell = 1} ^ {L _ {c}} \gamma_ {\ell} ^ {(h) \prime} \mathbf {x} _ {i, t - \ell} + \varepsilon_ {i, t + h} ^ {(h)}\tag{3}
$$

The coefficients $\{\hat{\delta}^{(h)}\}_{h=0}^{H}$ then trace the cumulative response of each outcome variable to a 1 percentage point increase in the 5-year sovereign yield that is caused by a fiscal risk shock. This interpretation is cleaner than the reduced-form coefficient because it explicitly scales all responses to an economically interpretable unit of sovereign yield movement, facilitating interpretation of effect magnitude and comparison across countries.

However, sharper interpretation comes at the cost of wider standard errors, arising from the need to account for estimation uncertainty in the first stage. For inference under the 2SLS-LP procedure, we rely on an IV-corrected, country-clustered sandwich variance estimator. The IV correction in the second stage accounts for first stage sampling uncertainty. Standard errors are also cluster-robust to deal with serially correlated and

heteroskedastic errors in the second stage. $^{13}$

## 4 Panel IRF Estimates

Equation 3 is estimated separately for each outcome variable, and the coefficients represent IRF estimates of the cumulative response to a 1 percentage point increase in the 5-year sovereign yield attributable to a fiscal risk shock. IRF estimates are shown in Figure 3.

Consumer prices (log headline CPI) rise immediately following the shock, with the point estimate rising by 1% to 1.5% in the ten months after the shock, before fading and turning negative, becoming statistically indistinguishable from 0 after about ten months. One-year ahead inflation expectations also rise by about 0.5 percentage points (pp), with the increase statistically significant for about five months, before dissipating. Industrial production indices, our primary real activity indicator of choice, show a brief positive response in the first four months after the shock, reflecting the temporary effects of fiscal policy associated with fiscal risk shocks, before turning negative thereafter. $^{14}$ The prompt but short-lived increase in industrial production is consistent with results in Gargiulo, Inoue, and Rossi (2025) who show that business conditions improve improve within the first quarter after surprise increases in government spending, with a peak around 80 days after the shock. Our results, suggest that adverse effects of fiscal risk shocks on real activity are persistent in the medium-term, becoming statistically significant negative after about 16-18 months.

Yields rise across the yield curve following a fiscal risk shock. Long term 10-year yields show a persistent positive response, rising by 0.5–1.0pp in the first year after the shock, before dissipating gradually. The increase partly reflects an increase in the term spread between 10- and 1-year sovereign bonds, with the positive statistically significant impact for about the first ten months. The trade-weighted nominal exchange rate depreciates significantly after 6 months and continues to do so persistently. Equity prices fall persistently after the shock, although the effects are imprecisely estimated. Declines in equity prices could reflect two complementary channels: a discount-rate effect, whereby higher sovereign yields raise the risk-free rate and compress equity valuations, and a forwardlooking tax-burden channel, whereby markets price in higher future taxes needed to service the expanded debt stock.

Discussion. Taken together, the 2SLS-LP estimates suggest that a fiscal-risk-induced increase in sovereign yields is inflationary at first. Initial inflationary pressures are consistent with a boost to real activity, reflecting fiscal policy-related demand drivers, and elevated inflation expectations. In these aspects, our results suggest that fiscal risk shocks have similar near-term macroeconomic effects as unfunded fiscal shocks as formalized in Bianchi, Faccini, and Melosi (2023) (among others). In their model, unfunded fiscal shocks lead to short-term boosts in output, inflation and inflation expectations, as a rise in fiscal transfers adds persistently to public debt stocks while central banks accommodate resultant inflation. For open economies, our results suggest that the exchange rate is an additional driver of inflation after fiscal risk shocks, with depreciating trade-weighted nominal rates boosting imported inflation.

However, in contrast to models of unfunded fiscal shocks, our estimates show that the rise in real activity is short-lived, even as inflationary pressures persist for the full year after the shock. At the same time, aggregate financial conditions tighten—as seen via higher government bond yields across maturities and decline in equity prices—with effects persisting more than a year after a shock. The rise in government bond yields, especially at longer maturities, is consistent with expected currency depreciation in line with uncovered interest rate parity (UIP) theory, rising inflation risk (see Fernández-Villaverde et al. (2015), Bretscher, Hsu, and Tamoni (2020)), sovereign default risk (see Corsetti et al. (2013) and government bond term premia (see Dai and Philippon (2005), Kumar and Baldacci (2010)), while declines in equity prices could be due to greater uncertainty about future fiscal policy (see Pástor and Veronesi (2012), Croce et al. (2012)) or reduced confidence about long-term potential growth. $^{15}$ Persistently tighter financial conditions outweigh the policy-associated demand boost after several months, leading to negative net effects on real output. Even as the rise in fiscal risk begins to weigh negatively on real activity indicators, the inflation impact remains positive for the entire year after the shock, supported by elevated inflation expectations and persistent exchange rate depreciation.


[[KC_IMAGE_003]]

Figure 3: Baseline 2SLS local-projection impulse response functions

Notes: Impulse response functions to a 1-percentage-point fiscal-risk-driven increase in the 5-year government bond yield, estimated via 2SLS-LP as in equation (3). The shock is the 5-year bond median-target fiscal risk shock, where daily shock estimates are summed by reference month. Horizons $h = 0, \dots, 24$ months. Shaded bands: 67% IV-corrected clustered confidence intervals. Long-difference outcome transform. Panel of 12 qualifying countries.

Eventually, negative aggregate demand effects from persistently higher interest rates and tighter financial conditions offset inflation expectations, bringing down price pressures after about one year. Thereafter, contractionary aggregate demand effects of higher borrowing costs dominate, suppressing real activity and exerting disinflationary pressure. These patterns are broadly consistent with a fiscal stress narrative in which higher sovereign borrowing costs tighten financial conditions, dampen asset prices, and put downward pressure on activity. $^{16}$ Moreover, the dissipation of inflation expectations and inflation pressures after the first year suggests that within our sample, fiscal risk shocks have not led to persistent increases in inflation expectations that could result from expectations of debt monetisation.

## 4.1 Robustness

Comparison with reduced form estimation. As a first robustness check, the 2SLS-LP estimates in equation (3) are compared against a reduced form estimator in which the raw fiscal risk shock $s_{i,t}$ is used as a direct regressor without running a separate first stage, as in equation 2. Unsurprisingly, the two approaches yield identical point estimates subject to the first-stage scaling factor, as the 2SLS-IV estimator is mathematically equivalent to a direct IV procedure, which scales the reduced-form responses by the first-stage coefficient (see Figure F.1 in the Appendix). Indeed, reduced form estimates are more precise than 2SLS-LP estimates, a consequence of first-stage estimation uncertainty propagating into the second-stage residuals (and accounted for by the IV-sandwich correction). Notably, under reduced form estimates, persistent declines in stock prices are statistically significant.

Robustness to alternative fiscal risk shock measures. The broad observations from Figure 3 are robust to the use of alternative measures of fiscal risk shocks, beyond our chosen baseline shock–5-year bond median target shocks. Figure F.2 from Appendix F.2 shows that estimated IRFs are similar when 10-year or 1-year bonds rather than 5-year bonds are used, or when more lags are included in Equation 1 in the estimation of mediantarget fiscal risk shocks. In addition, results are robust to the addition of bilateral nominal exchange rates (with the USD) as an endogenous variable in Equation 1, to account for potential transmission from exchange rate appreciation to higher sovereign yields, without a corresponding increase in fiscal risk.

Results are also robust to replacing the level of safe corporate bond yields with the spread between government bond yields and safe corporate bond yields (both at 5-year maturity) in our identification strategy. $^{17}$ Because government bond yields and safe corporate bond yields move closely together at this maturity, the two measures are highly collinear, and the estimated IRFs are very close to the baseline.

Robust inference. Two complementary checks confirm that the main results are insensitive to the choice of inference procedure in our baseline results.

First, baseline asymptotic standard errors as shown in Figure 3 are compared against bootstrap confidence intervals obtained via a panel Moving Block Wild Bootstrap (MBWB) adapted from Gonçalves and Kilian (2004). The original MBWB procedure, designed for time-series structural VARs, constructs bootstrap pseudo-samples by multiplying all residuals within overlapping blocks of length m by a common Rademacher random variable $v_{b}^{(j)} \in \{-1, +1\}$ , thereby preserving within-block serial correlation while exchanging second-moment information across blocks. $^{18}$ The panel adaptation applies independent block-sign draws within each country, so that cross-sectional independence is maintained while each country's own autocorrelation structure is respected; the block length is set to m = 4 months and B = 1,000 replications are used. Figure F.3 in the Appendix shows baseline IRF estimates with MBWB standard errors. Across all outcome variables, the MBWB credible bands closely track the asymptotic IV confidence intervals, and no variable changes its sign or significance classification, confirming that the clustered sandwich estimator provides reliable finite-sample inference for the panel.

Second, following Cieslak and Pang (2021), a distinction is drawn between sampling uncertainty—arising from variation in outcomes conditional on the estimated shock series—and shock estimation uncertainty—arising from the fact that the fiscal risk shock series $\{s_{i,t}\}$ is itself an estimated object rather than a directly observed instrument. Shock estimation uncertainty is quantified by re-estimating the full LP over multiple simulated draws of the shock series, each representing an alternative realisation consistent with the structural model's identification restrictions. As seen in Figure F.4 in the Appendix, the resulting distribution of impulse response functions is found to be extremely tight: the point estimates from the baseline shock series fall well inside the simulation envelope for all horizons and outcome variables, indicating that estimation uncertainty in the shock series contributes negligibly to overall uncertainty in the IRF estimates. Sampling uncertainty, captured by the IV-sandwich standard errors, therefore constitutes the dominant source of inferential uncertainty throughout the analysis.

## 5 Passive vs Active Monetary Policy Responses

Figure 3 shows that a rise in fiscal risk leads to persistently elevated inflation and inflation expectations, along with a short-term increase in real output, consistent with the effects of unfunded fiscal shocks under the fiscal theory of the price level. In these models, the macroeconomic effects of unfunded fiscal spending depend importantly on the monetary authority's response to inflation generated by such spending. In particular, Leeper (1991) and Bianchi, Faccini, and Melosi (2023) show that under a fiscally-dominant regime, characterized by a fiscal authority that undertakes unfunded fiscal policy alongside a central bank accommodative of such policy, unfunded fiscal shocks have persistent effects on inflation and inflation expectations.

We investigate if the macroeconomic and financial impact of fiscal risk shocks depends on the monetary policy response to fiscal risk shocks. To capture episodes of monetary accommodation, we construct a binary indicator $D_{i,t}^{MP}$ that equals unity in country-month observations classified as passive monetary policy regimes—periods in which the central bank's policy rate consistently undershoots a Taylor-rule-implied benchmark after a positive fiscal risk shock, thereby accommodating the inflationary pressures that may accompany a fiscal expansion rather than offsetting them through active tightening.

Formally, the passive monetary policy indicator is defined as:

$$
D _ {i, t} ^ {M P} = \mathbf {1} \left\{\Delta s _ {i, t} > 0 \quad \text { and } \quad \sum_ {k = 1} ^ {8} \mathbf {1} \left\{\tau_ {i, t + k} <   c _ {i, t + k} \right\} \geq 6 \right\},\tag{4}
$$

where $\Delta s_{i,t} > 0$ denotes a positive fiscal risk shock. $\tau_{i,t+k}$ is the Taylor rule residual—the deviation of the realized policy rate from its forward-looking rule-implied counter-

part:

$$
\tau_ {i, t + k} = i _ {i, t + k} - \mathbb {E} \Big [ i _ {i, t + k} \Big | \pi_ {i, t + k} ^ {f c}, g _ {i, t + k} ^ {f c} \Big ]\tag{5}
$$

A negative $\tau_{i,t+k}$ indicates that the realized policy rate lies below the level consistent with prevailing macroeconomic expectations—monetary policy is accommodative relative to its estimated systematic component. The conditional expectation $E[i_{i,t+k} \mid \pi_{i,t+k}^{fc}, g_{i,t+k}^{fc}]$ in equation (5) is estimated from the forward-looking Taylor rule closely following Orphanides (2003, 2004).

$$
i _ {i, t} = \alpha_ {i} + \rho_ {i} i _ {i, t - 1} + \beta_ {i} \pi_ {i, t} ^ {f c} + \gamma_ {i} g _ {i, t} ^ {f c} + \varepsilon_ {i, t},\tag{6}
$$

Here $i_{i,t}$ is the short-term policy rate, $\pi_{i,t}^{fc}$ and $g_{i,t}^{fc}$ are Consensus Economics one-year-ahead forecasts of CPI inflation and real GDP growth, and $\rho_{i}$ is the interest-rate smoothing parameter. Equation (6) is estimated by OLS with Newey–West HAC standard errors (12 lags) on the pre-sample period 2000–2012, which pre-dates the LP estimation window and thereby avoids in-sample endogeneity. $^{19}$ For the sample period, Taylor-rule-implied policy rates are then calculated as $\hat{i}_{i,t} = \hat{\alpha}_{i} + \hat{\rho}_{i} i_{i,t+k-1} + \hat{\beta}_{i} \pi_{i,t+k}^{fc} + \hat{\gamma}_{i} g_{i,t+k}^{fc}$ , and $\hat{\tau}_{i,t}$ as deviations of actual policy rates from $\hat{i}_{i,t}$ . $c_{i,t+k}$ is a regime-dependent threshold that is used to set the passive monetary policy indicator in equation (4):

$$
c _ {i, t} = \left\{ \begin{array}{l l} \operatorname{se} (\hat {i} _ {i, t}) & \text { if } i _ {t} > 0, \\ 0 & \text { otherwise }. \end{array} \right.\tag{7}
$$

When policy rates $i_{t}$ are above the zero lower bound (assumed for simplicity to be 0 for all countries), monetary policy is considered to be accommodative if the actual policy rates are more than one standard error below its Taylor-rule-implied level, or $\tau_{i,t+k} = i_{i,t} - E[i_{i,t+k} \mid \pi_{i,t+k}^{fc}, g_{i,t+k}^{fc}] < \text{se}(\hat{i}_{i,t})$ . At the zero lower bound, a looser threshold of 0 is applied to take into account the central bank's constraints on further easing. $^{20}$

Endogeneity concerns. A genuine empirical challenge to estimating the impact of accommodative monetary policy $D_{i,t}^{MP}$ arises from potential endogeneity concerns with characterizing monetary policy responses that depend on future realizations of the policy rate after the shock. If shocks to inflation and output over this window simultaneously drive $D_{i,t}^{MP}$ and predict the LP outcome $y_{i,t+h}$ , the regime indicator would be correlated with the LP residual $\varepsilon_{i,t+h}$ and OLS/LP would be inconsistent.

$\tau_{i,t+k}$ overcomes these concerns by capturing discretionary policy deviations—the component of the actual policy rate that cannot be attributed to any macroeconomic information available to professional forecasters at $t+k$ . To see this, let $\epsilon_{t+1},\ldots,\epsilon_{t+k}$ denote the macro shocks realized between t and $t+k$ . Because Consensus Economics forecasters observe the full history of publicly available macroeconomic data at each forecast date, their inflation and output forecasts at $t+k$ aggregate all information accumulated up to that date—including the propagated effects of the fiscal risk shock $s_{i,t}$ and all intervening macro shocks:

$$
\mathbb {E} \Big [ i _ {i, t + k} \big | \pi_ {i, t + k} ^ {f c}, g _ {i, t + k} ^ {f c} \Big ] = \mathbb {E} \Big [ i _ {i, t + k} \big | s _ {i, t}, \epsilon_ {t + 1}, \ldots , \epsilon_ {t + k} \Big ].\tag{8}
$$

Assuming that professional forecasters observe all macro-relevant information at each forecast date, Equation (8) implies that $\tau_{i,t+k}$ is the residual after projecting out all macro news through $t + k:^{21}$

$$
\tau_ {i, t + k} = i _ {i, t + k} - \mathbb {E} \left[ i _ {i, t + k} \mid s _ {i, t}, \epsilon_ {t + 1}, \dots , \epsilon_ {t + k} \right], \Rightarrow \tau_ {i, t + k} \perp (s _ {i, t}, \epsilon_ {t + 1}, \dots , \epsilon_ {t + k}).
$$

Economically, $\tau_{i,t+k}$ captures only discretionary policy deviations—the component of the actual policy rate that cannot be attributed to any macroeconomic information available to professional forecasters at $t+k$ . Since $D_{i,t}^{MP}$ is a deterministic function of $(s_{i,t}, \tau_{i,t+1}, \ldots, \tau_{i,t+8})$ , and the LP residual satisfies $\varepsilon_{i,t+h} \in \sigma(\epsilon_{t+1}, \ldots, \epsilon_{t+h})$ up to the LP projection, this implies:

$$
\mathbb {E} \left[ D _ {i, t} ^ {M P} \varepsilon_ {i, t + h} \right] = 0 \quad \forall h \geq 1.\tag{9}
$$

Both factors of the indicator—the positive-shock indicator $1[\Delta s_{i,t} > 0]$ , which is orthogonal to future LP error terms by the fiscal risk shock identification assumption, and the threshold-count term, which depends only on discretionary Taylor residuals purged of macro news—are orthogonal to $\varepsilon_{i,t+h}$ .

Estimation. Building on equation (3), the second-stage LP is further augmented to test for differential transmission under passive monetary policy by adding i) an indicator for positive fiscal risk shocks- $D_{i,t}^{+}=1\{s_{i,t}>0\}$ denotes an indicator that equals unity when the underlying fiscal risk shock is positive and zero otherwise, ii) an indicator passive monetary policy $D_{i,t}^{MP}$ as defined in equation (4), as well as iii) the interaction of both $D_{i,t}^{+}$ and $D_{i,t}^{MP}$ with $y_{i,t}^{\widehat{y_{i,t}}}$ . These variables are added to the instrument set in the first stage, and the augmented second-stage regression model is:

$$
\begin{array}{r l r} & & {y _ {i, t + h} - y _ {i, t - 1} = \alpha_ {i} ^ {(h)} + \delta^ {(h)} \widehat {\mathrm{yield5Y}} _ {i, t} + \gamma^ {(h)} \left(D _ {i, t} ^ {+} \cdot \widehat {\mathrm{yield5Y}} _ {i, t}\right) + \pi^ {(h)} D _ {i, t} ^ {+}} \\ & & {+ \gamma_ {A} ^ {(h)} \left(D _ {i, t} ^ {M P} \cdot \widehat {\mathrm{yield5Y}} _ {i, t}\right) + \pi_ {A} ^ {(h)} D _ {i, t} ^ {M P}} \\ & & {+ \sum_ {\ell = 1} ^ {L _ {c}} \gamma_ {\ell} ^ {(h) \prime} \mathbf {x} _ {i, t - \ell} + \sum_ {\ell = 1} ^ {L _ {y}} \phi_ {\ell} ^ {(h)} \Delta y _ {i, t - \ell} + \varepsilon_ {i, t + h} ^ {(h)}} \end{array}\tag{10}
$$

In equation (10), $\delta^{(h)}$ captures the baseline 2SLS response on negative-shock episodes $(D_{i,t}^{+}=0)$ . $\hat{\gamma}^{(h)}$ tests whether the economic impact of fiscal risk shocks depends on the sign of the shock. Effectively, $\hat{\gamma}^{(h)}$ is the asymmetry differential: the additional marginal response on positive-shock episodes relative to negative ones following a 1-percentage-point fiscal-risk-driven increase in yield5Y (conditional on $D_{i,t}^{MP}=0$ ). The level control $\pi^{(h)}D_{i,t}^{+}$ absorbs unconditional mean differences in outcomes between sign regimes.

Estimates of $\hat{\gamma}^{(h)}$ show that the asymmetric effects of positive relative to negative shocks are very small in magnitude, although they are statistically significant across multiple outcome variables. Positive fiscal risk shocks generate slightly larger upward pressure on CPI inflation and inflation expectations relative to mirror-image episodes of declining fiscal risk, while long-end yields and equity prices are slightly more sensitive to adverse fiscal surprises than to equivalent improvements in fiscal risk. See details in Appendix G.

Of primary interest is the coefficient parameter $\hat{\gamma}_{A}^{(h)}$ , which can be interpreted as an 'accommodation premium': the additional response of outcome y to a 1-percentage-point fiscal-risk-driven yield increase that accrues specifically in passive monetary policy episodes, conditional on a positive underlying fiscal risk shock. The level control $\pi_{A}^{(h)}D_{i,t}^{MP}$ controls for unconditional mean differences in outcomes attributable to monetary policy accommodation episodes. Conditional on a positive underlying fiscal risk shock, Figure 4 reports the differential response of outcome y during passive monetary policy episodes, relative to active monetary policy episodes. Two broad observations can be made.

First, accommodative monetary policy boosts demand in the year after an increase in fiscal risk, but intensifies stagflationary dynamics in the medium-run. The differential economic impact of passive versus active monetary policy responses after a positive fiscal risk shock are relatively benign in the first five months after the shock, consistent with the view that an accommodative monetary response, identified as a fall in the real interest rate, allows demand to expand in the short run, as fiscal spending is not crowded out by higher borrowing costs. In the short run, the differential response for both inflation and inflation expectations are statistically insignificant, as both active and passive monetary policy responses lead to inflationary pressures of similar magnitude.

However, stagflationary effects of fiscal risk shocks are significantly more pronounced within the first year after the shock if monetary policy is passive. Real activity begins to decline more significantly after six months, with the extent of the drag increasing persistently. Moreover, by around horizon h = 10, price pressures begin to accumulate by more, implying a persistent stagflationary dynamic. The greater increase in price levels reflects greater currency depreciation in the short run and elevated inflation expectations after about ten months. Headline CPI is about 1.8% higher one year after the shock when monetary policy accommodates the positive fiscal risk shock. Moreover, stagflationary effects persist in the medium term, while inflation expectations are up to 1.5pp higher after two years. $^{22}$ Notably, higher inflation and weaker real activity persist even after monetary policy stops being accommodative and the real policy rate rises about 20 months after the shock.

Second, accommodative monetary policies provides only a temporary cushion against a tightening of aggregate financial conditions after an increase in fiscal risk. For around ten months after the shock, the 'accommodation premium' on long-end government bonds is negative, with yields for 10-year bonds rising by about 0.2pp less than when monetary policy is active. Similarly, in the ten months following a positive fiscal risk shock, the term spread (between 10- and 1-year government bonds) rises by about 0.2pp less, and stock prices fall by up to 8% less, relative to when monetary policy is active. With monetary accommodation limiting interest rate increases at least in the short-term, there is greater immediate currency depreciation, possibly indicating increased retrenchment of capital flows.

However, accommodative monetary policy does not insulate the economy against tightening financial conditions beyond the first year. Even if accommodative monetary policy caps increases in short-term interest rates, $\hat{\gamma}_{A}^{(h)}$ for the term spread turns positive after approximately ten months, and remains so. Effectively, passive monetary policy responses are associated with a steepening of the yield curve, and the negative impact on 10-year bond yields dissipates. This tightens financial conditions for borrowers whose funding costs are typically indexed to the long end of the curve—such as corporate issuers and mortgage holders—even as the policy rate itself continues to be accommodative. Moreover, against a depreciated currency, yields must eventually rise in line with UIP. Finally, the boost to equity prices also disappears after about 15 months. Together, the real activity reversal, the persistence of inflation, and the term-spread widening are consistent with a fiscal-dominance narrative in which passive monetary policy amplifies rather than absorbs the adverse macro-financial consequences of fiscal risk shocks.

We obtain similar results on the effects of passive monetary policy after positive fiscal risk shocks when using a simpler measure of $D_{i,t}^{MP}$ -defined as episodes where the central bank does not raise the nominal policy rate sufficiently to prevent the ex-post real rate from being persistently negative after a fiscal risk shock. See Appendix H.


[[KC_IMAGE_004]]

Figure 4: Monetary accommodation premium $\hat{\gamma}_A^{(h)}$ : passive vs. active monetary policy episodes

Notes: Estimated accommodation premium $\hat{\gamma}_{A}^{(h)}$ from equation (10) at each horizon $h = 0, \ldots, 23$ months. A positive value indicates a larger response to a 1-pp fiscal-risk-driven yield increase during passive monetary policy episodes ( $D_{i,t}^{MP} = 1$ ) relative to active episodes, conditional on a positive underlying fiscal risk shock. Shaded bands: 67% IV-corrected clustered confidence intervals.

## 6 Country Heterogeneity in Fiscal Conditions

The macro-financial transmission of fiscal risk shocks is likely to depend on the prevailing fiscal conditions within countries. When public debt is already elevated or market participants perceive fiscal sustainability to be fragile, the same shock can trigger a non-linear tightening of financial conditions: sovereign spreads widen disproportionately and risk premia on private credit co-move with sovereign spreads through bank balance-sheet and collateral channels (Corsetti et al., 2013; Sims, 2011). $^{23}$

In our context, it is difficult to test for cross-country heterogeneity driven by variation in levels of public debt-to-GDP directly. $^{24}$ Instead, we test whether the impact of a fiscal risk shock depends on the country's prevailing sovereign market conditions by using lagged CDS spreads (lagging to avoid simultaneity) as a time-varying indicator of fiscal conditions. $^{25}$ Specifically, we augment the second-stage local projection with an interaction between the instrumented yield change and the country's lagged CDS spread state:

$$
y _ {i, t + h} - y _ {i, t - 1} = \alpha_ {i} ^ {(h)} + \gamma_ {h} \left(\widehat {\Delta \text {yield5}} Y _ {i, t} \times \bar {z} _ {i, t} ^ {c d s}\right) + \delta_ {h} \bar {z} _ {i, t} ^ {c d s} + \mathbf {X} _ {i, t} ^ {\prime} \Pi_ {h} + \varepsilon_ {i, t + h} ^ {(h)},\tag{11}
$$

$\bar{z}_{i,t}^{cds} = (\bar{c}_{i,t} - \mu_{cds}) / \sigma_{cds}$ is the z-score of the 4-month moving average of CDS spreads, and $X_{i,t}$ includes the standard lag controls from the baseline specification, which already include 4 CDS lags in the baseline. $\gamma_{h}$ is the parameter of interest: a positive $\gamma_{h}$ implies that fiscal risk shocks have larger macro-financial impact when sovereign risk premia are already elevated.

Figure 5 presents the estimated differential impulse responses $\hat{\gamma}_h\times (z_{90} - z_{10})$ across eight outcome variables. Each panel plots the difference in the impulse response between a high-CDS state $(\mathrm{p}90,\approx 127~\mathrm{bp})$ and a low-CDS state $(\mathrm{p}10,\approx 12~\mathrm{bp})$ , scaled to match the magnitude of the p10-p90 CDS spread contrast. Economically, this differential can be interpreted as the additional impact of a fiscal risk shock when the country resembles Mexico in its sovereign risk conditions relative to the impact when the country resembles Switzerland, holding all else equal.

The results in Figure 5 indicate that the transmission of fiscal risk shocks is amplified when sovereign credit conditions are already under pressure. The most striking differential is in inflation dynamics: in the high-CDS environment, fiscal risk shocks generate a more persistently inflationary impulse, with the CPI differential widening steadily across the 24-month horizon rather than dissipating after the first year. This pattern is consistent with inflation expectations becoming de-anchored in fiscally stressed environments: when investors already price a non-trivial probability of eventual debt monetization, a further fiscal risk shock reinforces those expectations, and a persistent pass-through to realized prices. The differential response of inflation expectations is correspondingly large and precisely estimated: countries in the high-CDS environment see inflation expectations rise by approximately 0.15–0.18 percentage points more than their low-CDS counterparts over a two-year horizon. The exchange rate depreciates by a greater extent in the short-term, but this is imprecisely estimated. The real policy rate differential suggests somewhat larger monetary accommodation in the high-CDS environment at medium horizons, consistent with the passive-MP mechanism from Section 5 being more likely to bind when sovereign risk is already elevated.

The yield curve and term-spread dynamics also diverge sharply by fiscal state. Long-term yields increase by more in high-CDS environments at shorter horizons, reflecting a larger risk-premium component in the sovereign yield response: when fiscal credibility is already fragile, the same shock triggers a greater repricing of duration and credit risk. The term spread differential rises and peaks around six to nine months before partially reverting, consistent with short rates being partially anchored by central bank policy even in stressed environments while the long end of the yield curve incorporates the heightened fiscal risk premium. These differential yield and spread responses strengthen the financial-conditions tightening channel through which fiscal risk shocks generate output losses. Equity prices exhibit a larger and more sustained differential decline in the high-CDS state: the differential fall in stock prices accumulates over the medium term to roughly four to five percentage points wider than in the low-CDS environment.


[[KC_IMAGE_005]]

Figure 5: State-dependent effects of fiscal risk shocks: high vs. low CDS environment (p90 vs. p10)

Notes: Impulse response functions from equation (11), scaled by $(z_{90}-z_{10})$ to represent the difference in macro-financial transmission between a country at the 90th percentile of the (lagged) CDS distribution (approximately 127 basis points; comparable to Mexico) and one at the 10th percentile (approximately 12 basis points; comparable to Switzerland). Specifically, each panel plots $\hat{\gamma}_{h}\times(z_{90}-z_{10})$ where $\hat{\gamma}_{h}$ is the horizon-h interaction coefficient in equation (11). Shaded bands: 67% IV-corrected clustered confidence intervals. Horizons $h=0,\ldots,23$ months. Panel of 12 qualifying countries, 1,718 non-missing observations. The moderator $\bar{z}_{i,t}^{cds}$ is the mean of CDS lags 1–4; lags 1–4 are also included as level controls.

## 7 Conclusion

This paper develops a new, market-based identification strategy for fiscal risk shocks that exploits the opposite-signed response of sovereign yields and the yields of the safest private private bonds to unexpected changes in fiscal policy that hinder fiscal sustainability. This approach allows us to isolate the repricing of sovereign risk that is distinct from other drivers of yield changes.

Using the resulting shock series across twelve countries with sufficiently long daily bond yields series, we show that fiscal risk repricing systematically propagates to the macroeconomy through financial conditions, inflation expectations and exchange rates. Fiscal risk shocks raise inflation and inflation expectations on impact, consistent with a temporary demand impulse and exchange rate depreciation. However, the increase in sovereign yields quickly spills over to private funding conditions. As a result, the initial output boost is short-lived and gives way to a persistent contraction. Furthermore, the transmission is state- and policy-dependent: the effects of the shocks are amplified when monetary policy is accommodative vis-a-vis an increase in inflation and when the initial sovereign risk premium is high.

A key contribution of our analysis is that it helps unpack the "black box" of the debt-valuation mechanism emphasised in the fiscal theory of the price level. By tracing how news relevant to fiscal sustainability are priced into sovereign bonds and then transmitted through other financial prices, and the economy more generally, the results provide a market-based account of how perceived fiscal imbalances leads to changes in the general price level.

Two limitations of our analysis point to future extensions. First, the available sample of individual bond data is limited both in time series length and cross-country coverage. As additional observations accumulate, the estimated impulse responses should become more precise. Second, our fiscal risk shock series aggregate heterogeneous fiscal risk events. With longer and richer samples, future work should be able to distinguish types of fiscal risk shocks – for example, those associated with fiscal expansions from those that reflect adverse fiscal news without near-term stimulus – and assess whether and how their macroeconomic effects differ.

## References

Acharya, Viral, Itamar Drechsler, and Philipp Schnabl. 2014. “A pyrrhic victory? Bank bailouts and sovereign credit risk.” The Journal of Finance 69 (6):2689–2739.

Almeida, Heitor, Igor Cunha, Miguel A Ferreira, and Felipe Restrepo. 2017. “The real effects of credit ratings: The sovereign ceiling channel.” The Journal of Finance 72 (1):249–290.

Ang, Andrew, Geert Bekaert, and Min Wei. 2008. “The term structure of real rates and expected inflation.” The Journal of Finance 63 (2):797–849.

Arellano, Cristina. 2008. “Default risk and income fluctuations in emerging economies.” American Economic Review 98 (3):690–712.

Augustin, Patrick, Hamid Boustanifar, Johannes Breckenfelder, and Jan Schnitzler. 2018. "Sovereign to corporate risk spillovers." Journal of Money, Credit and Banking 50 (5):857–891.

Azzimonti, Marina. 2018. “Partisan conflict and private investment.” Journal of Monetary Economics 93:114–131.

Baker, Scott R, Nicholas Bloom, and Steven J Davis. 2016. “Measuring economic policy uncertainty.” The Quarterly Journal of Economics 131 (4):1593–1636.

Bassetto, Marco and Thomas J Sargent. 2020. “Shotgun wedding: Fiscal and monetary policy.” Annual Review of Economics 12 (1):659–690.

Bauer, Michael D and Eric T Swanson. 2023. “A reassessment of monetary policy surprises and high-frequency identification.” NBER Macroeconomics Annual 37 (1):87–155.

Bernardini, Marco, Selien De Schryder, and Gert Peersman. 2020. “Heterogeneous government spending multipliers in the era surrounding the Great Recession.” The Review of Economics and Statistics 102 (2):304–322.

Bi, Huixin, Eric M Leeper, and Campbell Leith. 2013. “Uncertain fiscal consolidations.” The Economic Journal 123 (566):F31–F63.

Bianchi, Francesco, Renato Faccini, and Leonardo Melosi. 2023. “A fiscal theory of persistent inflation.” The Quarterly Journal of Economics 138 (4):2127–2179.

Bianchi, Francesco, Renato Faccini, Leonardo Melosi, and Nils Wehrhöfer. 2026. “Lack of Trust and Fiscal Dominance: Evidence from a Firm Survey Experiment.” Discussion Paper 21595, CEPR.

Bianchi, Francesco and Cosmin Ilut. 2017. “Monetary/fiscal policy mix and agents’ beliefs.” Review of Economic Dynamics 26:113–139.

Bianchi, Francesco and Leonardo Melosi. 2019. “The dire effects of the lack of monetary and fiscal coordination.” Journal of Monetary Economics 104:1–22.

Bocola, Luigi. 2016. “The pass-through of sovereign risk.” Journal of Political Economy 124 (4):879–926.

Bretscher, Lorenzo, Alex Hsu, and Andrea Tamoni. 2020. “Fiscal policy driven bond risk premia.” Journal of Financial Economics 138 (1):53–73.

Cardamone, Dario. 2025. “The Macroeconomic Effects of Sovereign Risk: New Evidence from US Debt Ceiling Episodes.” Working Paper.

Choi, Sangyup, Tim Willems, and Seung Yong Yoo. 2024. “Revisiting the monetary transmission mechanism through an industry-level differential approach.” Journal of Monetary Economics 145:103556.

Cieslak, Anna and Hao Pang. 2021. “Common shocks in stocks and bonds.” Journal of Financial Economics 142 (2):880–904.

Cochrane, John H. 2022. “A fiscal theory of monetary policy with partially-repaid long-term debt.” Review of Economic Dynamics 45:1–21.

Corsetti, Giancarlo, Keith Kuester, André Meier, and Gernot J Müller. 2013. “Sovereign risk, fiscal policy, and macroeconomic stability.” The Economic Journal 123 (566):F99–F132.

Cram, Roberto Gomez, Howard Kung, and Hanno Lustig. 2024. “Government Debt in Mature Economies: Safe or Risky?” Jackson Hole Economic Symposium Proceedings.

Croce, Mariano Max, Howard Kung, Thien T Nguyen, and Lukas Schmid. 2012. “Fiscal policies and asset prices.” The Review of Financial Studies 25 (9):2635–2672.

Dai, Qiang and Thomas Philippon. 2005. “Fiscal policy and the term structure of interest rates.” Working Paper 11574, National Bureau of Economic Research.

Farhi, Emmanuel and Jean Tirole. 2018. “Deadly embrace: Sovereign and financial balance sheets doom loops.” The Review of Economic Studies 85 (3):1781–1823.

Fernández-Villaverde, Jesús, Pablo Guerrón-Quintana, Keith Kuester, and Juan Rubio-Ramírez. 2015. “Fiscal volatility shocks and economic activity.” American Economic Review 105 (11):3352–3384.

Fry, Renee and Adrian Pagan. 2011. “Sign restrictions in structural vector autoregressions: A critical review.” Journal of Economic Literature 49 (4):938–960.

Gargiulo, Valeria, Atsushi Inoue, and Barbara Rossi. 2025. “A New Approach to Fiscal Multipliers: Time Variation and High Frequency Shocks.” Discussion Paper 20670, CEPR.

Gennaioli, Nicola, Alberto Martin, and Stefano Rossi. 2014. “Sovereign default, domestic banks, and financial institutions.” The Journal of Finance 69 (2):819–866.

Ghosh, Atish R, Jun I Kim, Enrique G Mendoza, Jonathan D Ostry, and Mahvash S Qureshi. 2013. “Fiscal fatigue, fiscal space and debt sustainability in advanced economies.” The Economic Journal 123 (566):F4–F30.

Giannone, Domenico, Michele Lenza, and Giorgio E Primiceri. 2015. “Prior selection for vector autoregressions.” Review of Economics and Statistics 97 (2):436–451.

Gonçalves, Silvia and Lutz Kilian. 2004. “Bootstrapping autoregressions with conditional heteroskedasticity of unknown form.” Journal of Econometrics 123 (1):89–120.

Hilscher, Jens, Alon Raviv, and Ricardo Reis. 2022. “Inflating away the public debt? An empirical assessment.” The Review of Financial Studies 35 (3):1553–1595.

Jordà, Óscar. 2005. “Estimation and Inference of Impulse Responses by Local Projections.” American Economic Review 95 (1):161–182.

Känzig, Diego R. 2021. “The macroeconomic effects of oil supply news: Evidence from OPEC announcements.” American Economic Review 111 (4):1092–1125.

Krishnamurthy, Arvind and Annette Vissing-Jorgensen. 2012. “The aggregate demand for treasury debt.” Journal of Political Economy 120 (2):233–267.

Kumar, Manmohan S and Emanuele Baldacci. 2010. “Fiscal deficits, public debt, and sovereign bond yields.” IMF Working Paper 10/184, International Monetary Fund.

Leeper, Eric M. 1991. “Equilibria under ‘active’ and ‘passive’ monetary and fiscal policies.” Journal of Monetary Economics 27 (1):129–147.

Lucas, Robert E. and Nancy L. Stokey. 1983. “Optimal fiscal and monetary policy in an economy without capital.” Journal of Monetary Economics 12 (1):55–93.

Montiel Olea, José Luis and Mikkel Plagborg-Møller. 2021. “Local Projection Inference is Simpler and More Robust Than You Think.” Econometrica 89 (4):1789–1823.

Orphanides, Athanasios. 2003. “Historical monetary policy analysis and the Taylor rule.” Journal of Monetary Economics 50 (5):983–1022.

——. 2004. “Monetary Policy Rules, Macroeconomic Stability, and Inflation: A View from the Trenches.” Journal of Money, Credit and Banking 36 (2):151–175.

Pástor, Žuboš and Pietro Veronesi. 2012. “Uncertainty about Government Policy and Stock Prices.” The Journal of Finance 67 (4):1219–1264.

Perotti, Roberto. 1999. “Fiscal policy in good times and bad.” The Quarterly Journal of Economics 114 (4):1399–1436.

Phillot, Maxime. 2025. “US treasury auctions: A high-frequency identification of supply shocks.” American Economic Journal: Macroeconomics 17 (1):245–273.

Ramey, Valerie A and Sarah Zubairy. 2018. “Government spending multipliers in good times and in bad: evidence from US historical data.” Journal of Political Economy 126 (2):850–901.

Ray, Walker, Michael Droste, and Yuriy Gorodnichenko. 2024. “Unbundling quantitative easing: Taking a cue from treasury auctions.” Journal of Political Economy 132 (9):3115–3172.

Rubio-Ramirez, Juan F, Daniel F Waggoner, and Tao Zha. 2010. “Structural vector autoregressions: Theory of identification and algorithms for inference.” The Review of Economic Studies 77 (2):665–696.

Sargent, Thomas J and Neil Wallace. 1984. “Some unpleasant monetarist arithmetic.” In Monetarism in the united kingdom. Springer, 15–41.

Sims, Christopher A. 1994. “A simple model for study of the determination of the price level and the interaction of monetary and fiscal policy.” Economic theory 4 (3):381–399.

Sims, Christopher A. 2011. “Stepping on a rake: The role of fiscal policy in the inflation of the 1970s.” European Economic Review 55 (1):48–56.

Smets, Frank and Raf Wouters. 2024. “Fiscal backing, inflation and US business cycles.” In Federal Reserve Bank of San Francisco, vol. 1.

Uribe, Martín. 2006. “A fiscal theory of sovereign risk.” Journal of Monetary Economics 53 (8):1857–1875.

Woodford, Michael. 1995. “Price-level determinacy without control of a monetary aggregate.” In Carnegie-Rochester conference series on public policy, vol. 43. Elsevier, 1–46.

## Appendix

## A S&P Global Evaluated GSAC Bond Pricing Data

In this appendix, we explain all the steps we took to get from the raw bond-level data to the median bond yields used in the empirical analysis to recover fiscal risk shocks. To ensure the quality and consistency of the data used in our analysis, we apply several filtering and data processing techniques to the raw data.

## A.1 Data Filtering

Sovereign bonds. We collect sovereign bond data from the S&P Global Evaluated GSAC Bond Pricing Data by filtering in observations that have the field classification equal to "Government". This samples both local government bonds, sovereign bonds, and agency bonds in some countries. To restrict the sample to sovereign bonds only, we use information on institutional names available in the variable called shortName to classify institutions issuing bonds into Sovereign and Non-sovereign entities. The classification is done using the Grok LLM and checked by a human after completion for correctness. Once local and agency bonds are filtered out, we restrict our sovereign bond sample to bonds for which couponType is equal to "Fixed", where coupon is not negative and applicableYieldType is equal to "YTM", such that the yields reported in the database are based on yield to maturity calculations performed consistently across bonds by the S&P Global.

Corporate bonds. For corporate bonds, we restrict our sample to include only bonds for which the field classification is NOT one of the following: "Financials", "Asset Finance", "Mortgage Finance", "Government", "Consumer Finance", "Collective Investment Vehicle". This filter is meant to ensure that we focus only on corporate bonds from non-financial firms, since bonds from financial firms are more likely to reflect borrowing conditions of sovereigns, as many financial institutions hold sovereign bonds as assets. Similarly, we exclude bonds issued by firms for which classification is equal to "Utilities", "Basic Materials", or "Energy". This filter is necessary because in many jurisdictions in our sample firms operating in these industries are owned by the government, or the government has a golden share that allows it to influence borrowing decisions of such firms. The rest of the filters we apply to the corporate bonds sample (i.e., based on couponType, coupon and applicableYieldType) are similar to those for sovereign bonds that we described above.


Table A.1: Sovereign and corporate bond currencies by country

Notes: This table table reports the currencies of bonds used to construct median yields for our analysis. Currencies are based on the most common currency among the sovereign bonds of maturity close to five years. The column called Country contains ISO 3166-1 alpha-3 codes, while the column called Bond currency contains ISO 4217 currency codes.

## A.2 Data processing

After the filters above are implemented, we process the data as follows. We sort sovereign bonds by couponCurrency in each country in our data and keep only the bonds with the most common currency in that country. We then sample only from corporate bonds that have couponCurrency in the same currency as the most common currency for sovereign bonds. Table A.1 lists the currencies that are most common in each country included in our sample used to estimate fiscal risk shocks. The US dollar is the most common currency across sovereign bonds and corporate bonds for 17 out of 60 countries in the sample of bonds with maturity of around five years. The euro is the most common bond currency for another 15 countries. The remaining currencies listed in Table A.1 represent local currencies of the respective countries included in our sample.

Next, since our baseline estimation uses 5-year yields to construct measures of fiscal risk shocks, we select all sovereign and corporate bonds with a remaining time to maturity between four and six years at the dates when yields are reported. In the remaining set of sovereign and corporate bonds, a few bonds have yields below -2% on some dates. We treat these bond yields as measurement noise and drop those yields from the sample. And since we want yields to reflect borrowing conditions unadjusted for inflation, we also focus in our sample only on bonds that are not inflation linked, that is, for which the variable isInflationLinked is equal to False.

The data processing described above gives us a sample of bonds with similar maturities, currency and coupon types for each date and country. We use the median yield of this sample for sovereign bonds in a given country on a given date. For corporate bonds, we rely on the top 20 bonds that have the lowest yields on a given date for each country to construct the median yield for the safest corporate bonds in a country. This ensures that we capture the safest bonds, where safety is measured by the relatively lower yields that theses corporate bonds pay. In Section A.3, we discuss how using a sampling based on A-rated corporate bonds when computing median corporate bond yields compares to our approach of using only the top 20 safest bonds.

After obtaining the two sets of median yields (i.e., sovereign and corporate), we merge the series by date for each country in our sample. We then apply a few filters to remove outliers and breaks in the series. First, we truncate the corporate bond median yields on dates where the spread between the corporate bond yield and sovereign bond yield is greater than 10 percentage points. Next, for each country, we identify and extract the longest consecutive sequence of dates in the time series of yields where gaps between dates do not exceed five days. To this achieve this, we create a group identifier that increments whenever a gap larger than five days is detected. The group with the largest number of observations is then selected for further analysis, ensuring the time series of yields is as continuous as possible. If no valid group is identified for a country, the country is dropped from our sample. After the longest batch of data is identified, we fill gaps in the time series by creating a complete daily date range between start and end date and then forward-filling the missing yield values from the last available observation. This procedure is necessary for our BVAR model to be estimated at a daily frequency, with consecutive daily lags, as it fills in data for weekends and public holidays where we assume that yields are stale. Lastly, we winsorize the median sovereign and corporate bond yields at the top and bottom 0.1 percentile, to reduce the influence of extreme outliers without completely removing them.


[[KC_IMAGE_006]]

Figure A.1: Comparison of yields for the U.S.
Notes: This figure plots yields for the median sovereign and corporate bond series that we constructed based on bond data for the US together with the yield for the ICE BofA AAA US Corporate Index.

## A.3 Median yields

Figure A.1 illustrates the evolution of the five-year sovereign and corporate bond median yields obtained for the US after applying the filters and data processing procedures described above. The figure shows that there is a small spread between yields for sovereign bonds and yields for the safest corporate bonds. The spread changes in time, reflecting variations in fiscal policies which helps us identify structural shocks in our BVAR setup. Reassuringly, the spread almost disappears between late 2021 and the first half of 2022 – a period when the US government engaged in large unfunded fiscal expansions (Cram, Kung, and Lustig, 2024).

The figure also shows the effective yield for the ICE BofA AAA US Corporate Index, retrieved from the FRED database of the Federal Reserve Bank of St Louis. This index is based on AAA-rated corporate bonds, which are typically considered the safest among corporate bonds in terms of their credit quality. During the COVID-19 recession, represented by the shaded area in the figure, the yield for the ICE BofA AAA US Corporate Index surged, whereas the median yield for our selection of the safest corporate bonds remained stable. This difference in observed behavior of corporate yields during episodes of bond market instability is reassuring, as it suggests that our median corporate yield series do not suffer from a flight-to-safety phenomenon that the larger sample of AAA-rated bonds seems to exhibit.

We also test whether using bond credit ratings to construct our median corporate bond series would improve its performance. To this end we merge our corporate bond data with ratings information from S&P Ratings and restrict our sample of corporate bonds to those that have at least one "A" in their rating. We then pick the set of twenty bonds with lowest yields per date from this restricted sample, similar to how we constructed our baseline corporate bond yield, and compute the median daily yield for this subset of lowest yielding corporate bond instruments that have a maturity of around five years. The correlation between this median and our baseline median corporate yield is very high. In the case of the US, this correlation is equal to 0.9977 over the sample period. One downside of using the ratings filter we describe here is that the median yield series constructed using ratings exhibits a flight-to-safety phenomenon in 2020, albeit much smaller than the one exhibited by ICE BofA AAA US Corporate Index, as shown in Figure A.1. We illustrate this issue in Figure A.2. The figure shows that in March 2020, the median yield constructed using corporate bond ratings spikes by nearly 100 basis points. As a result, we decided against using ratings to further filter bonds the we included in our safest corporate bond sample that is used to construct median corporate bond yields.


[[KC_IMAGE_007]]

Figure A.2: Comparison of corporate bond yields for the U.S. in 2020

Notes: This figure contrasts the evolution in 2020 of our baseline median corporate bonds yield for the safest US corporate bonds with a similarly constructed median corporate bond yield using all US corporate bonds in our sample that have at least an A in their rating.

## B Macro-financial data

Details on macroeconomic, financial and banking sector variables used in the various local projections estimates are specified in table B.1.


Table B.1: Outcome variables
Notes: This table describes the variables used in the local projection regressions, the sources from which we obtained these variables and the transformations we applied to the raw data.

## C Median target shocks vs. median of distribution of shocks

Following Fry and Pagan (2011), we select the shock series that come closest in terms of impulse response they produce to the median impulse response across the set of responses produced by all shocks. We term this shock - the median target shock. Unsurprisingly, the median target shock does not necessarily correspond to the sample crosssectional median for all shocks, but the two series are closely aligned. Figure C.1 plots the two median shocks for the US in 2025. The median target shock (blue dotted line) barely deviates from the cross-sectional median of shocks (red line), and in days when these two medians do not coincide, the deviation is minimal, as can be seen during the day circled with red in the figure.


[[KC_IMAGE_008]]

Figure C.1: Median target shock vs. median of shocks for the U.S. in 2025
Notes: This figure juxtaposes two shock series recovering using the model in equation (1) estimated for the US: (i) the median target shocks recovered from the median daily impulse responses, and (ii) the median across shocks recovered in a given day when estimating the model. A deviation point between the two series is highlighted using a red circle.

While the differences may be small between the two series, these differences can cumulate to large differences over a long horizon if one adds up the shocks over that horizon. Figure C.2 shows that the cumulative median target shock contains a non-trivial deviation from zero if cumulated over the entire sample for the US. This deviation is due to numerical error. Importantly, over periods shorter than one quarter the deviation is minuscule. When we adjust the series to remove the numerical error, the median target shock observations add up to zero over the entire sample and their evolution across the entire period mimics more closely the cross-sectional median of shocks. Since we cumulate shocks at frequencies that do not exceed one quarter, we decided to use as benchmark the unadjusted cumulative median target shock series for each country in our sample. Reasuringly, our main results from local projections are robust to using the median of sample shocks instead of median target shocks.


[[KC_IMAGE_009]]

Figure C.2: Cumulated shocks for the U.S. - median targets vs. sample medians
Notes: This figure shows the cumulative version across time of three shocks: (i) the median target shock, (ii) the median target shock adjusted for numerical error introduced during estimation, and (iii) the median across shocks in a given day.

## D Validation of fiscal risk shocks

This section reports additional statistical diagnostics to corroborate the validity of our shock series. Table D.1 presents pairwise correlation coefficients between the country-specific fiscal risk shocks we estimate in this paper and the monetary policy shocks from the cross-country database in Choi, Willems, and Yoo (2024). To ensure comparability, we aggregate our daily fiscal risk shocks to the monthly frequency to align with the monetary policy series reported for each country in the Choi, Willems, and Yoo (2024) database. For the vast majority of countries, the estimated correlations are near zero and statistically indistinguishable from zero. The sole exception is Sweden, where the correlation is 0.4799 and statistically significant at the 1 per cent level. However, this result is based on a limited overlap of only 29 monthly observations. In light of the limited sample size and the moderate magnitude of the correlation, we opted for retaining the Swedish fiscal risk shock series in our sample without adjustment.

In addition to correlation-based statistical validation, we test whether our shock series are predicted by other economic variables. These additional tests are meant to ensure that our shocks do not violate orthogonality to non-policy information, similar to how Bauer and Swanson (2023) test for orthogonality of monetary policy shocks to macroeconomic and financial data observed before monetary policy announcement dates. We conduct these predictability exercises at three sampling frequencies – quarterly, monthly, and daily – using a broad set of macroeconomic and financial indicators relevant for sovereign and corporate bond yields. And, since our shocks are measured at the daily frequency, we align them with lower-frequency predictors by aggregating within-period observations, summing daily fiscal risk shocks to the monthly or quarterly level.


Table D.1: Correlation of fiscal policy shocks with monetary policy shocks
Notes: This table reports correlation coefficients between our measures of median target shocks for a given country and monetary policy shocks from Choi, Willems, and Yoo (2024). The table also includes p-values for the correlation coefficients and number of observations used to compute these. Correlations are computed based on monthly shock data. The column called Country contains ISO 3166-1 alpha-3 codes for each country.

Table D.2 shows that lagged changes in CPI and GDP do not predict the quarterly fiscal risk shock series. The estimates are obtained from a panel OLS specification with country and time fixed effects, where the dependent variable is the quarterly fiscal risk shock. We then estimate analogous specifications that include lagged forecasts of GDP and CPI, as well as lagged changes in policy rates, as predictors of fiscal risk shocks. The corresponding coefficients, reported in Table D.3, are statistically indistinguishable from zero at conventional levels. The significance of estimates also does not change when lagged forecasts of budget deficits are added to the regression model. Finally, we assess whether equity market performance immediately prior to the fiscal risk shock date has predictive content for the shock. As reported in Table D.4, the shocks are uncorrelated with pre-shock stock returns. Collectively, these results provide no evidence of predictability from standard macroeconomic and financial indicators.

Table E.3 shows that 5-year bond median target shocks are a relevant instrument in our 2SLS-LP procedure: the first-stage coefficient $\hat{\beta}^{\mathrm{shock}} = 0.00994$ is positive and highly significant under both OLS and within-country clustered standard errors, with the $30\%$ larger clustered SE reflecting within-country serial correlation in residuals. The strength of our baseline shock instrument seen from large partial $F$ -statistics $F = 27.03$ (OLS) and $F = t^2 = 16.00$ (country-clustered residuals) both exceeding the conventional threshold of 10, confirming its suitability for reliable two-stage estimation. The modest partial $R^2$ of 0.010 is the instrument's incremental contribution after partialling out all controls is typical of external instruments.


Table D.2: Fiscal policy shock predictors - quarterly variables
Notes: This table reports estimates of a fixed effect panel regression of median target shocks on past realizations of changes in country-specific CPI and GDP. The frequency of the data used in estimation is quarterly. Country and time fixed effects are included in the regression. $^{*}p < 0.1$ ; $^{**}p < 0.05$ ; $^{***}p < 0.01$


Table D.3: Fiscal policy shock predictors - monthly variables

Notes: This table reports estimates of fixed effect panel regressions of median target shocks on lagged forecasts of country-specific GDP, CPI and deficits, as well as lagged changes in policy rates. The frequency of the data used in estimation is monthly. Country and time fixed effects are included in regressions. $*p < 0.1$ ; $**p < 0.05$ ; $***p < 0.01$


Table D.4: Fiscal policy shock predictors - daily variables

Notes: This table reports estimates of a fixed effect panel regression of median target shocks on past realizations of changes in country-specific stock price indices. The frequency of the data used in estimation is daily. Country and time fixed effects are included in the regression. $*p < 0.1$ ; $**p < 0.05$ ; $***p < 0.01$

## E Events Identified as Fiscal Shocks

A central requirement of our identification strategy is that the extracted fiscal risk shocks should respond to news that genuinely alters the fiscal outlook of a sovereign, and not merely reflect broader financial market sentiment or monetary policy surprises. To assess this, we compare the time series of daily shocks against well-known fiscal events for a selection of countries and episodes.

Two graphical validation exercises presented in Figures 1 and 2 in the main body of the paper showed that our fiscal shocks successfully pick up well-known fiscal events in the US in 2025 (including Liberation Day tariff announcements and the adoption of the Big Beautiful Bill), in Spain during the Eurozone crisis in 2012, the in the UK during the Brexit referendum in 2016. Figure E.1 documents two further cases: the US presidential election of November 2016, around which a large positive fiscal risk shock coincides with the expectation of expansionary fiscal policy under the incoming Trump administration, and the UK Truss mini-budget of September 2022, where the announcement of £45bn in unfunded tax cuts generated a sharp and sustained spike in fiscal risk shocks followed by reversal as the measures were unwound. The Bank of England responded with emergency gilt purchases on 28 June, which staved off further sell-off dynamics and restored market functioning, which was identified as a large negative fiscal risk shock in our setup.


[[KC_IMAGE_010]]

Figure E.1: Estimated fiscal risk shocks for Notable Fiscal Events

Notes: This figure shows the evolution of fiscal risk shocks for two well-known events: the US during the first Trump election victory (November 2016) and the UK during the Truss mini-budget episode (September to October 2022). The thick line represents the median target shock from the distribution of shocks recovered following the estimation of the model in equation (1). The shaded area stands for the 90% interval from the distribution of shocks.

To provide a broader summary of the identification strategy's performance, Table E.1 and Table E.2 below list the top three positive and negative monthly fiscal risk shocks for each country in our panel, where daily shocks have been aggregated to monthly frequency by summation. Even after this temporal aggregation, the shock series continues to identify economically meaningful events with high precision. $^{26}$ Among $positive$ shocks—those reflecting unexpected fiscal deterioration—the three largest months in the full cross-country sample are the Netherlands in February 2021, driven by the announcement of a large COVID recovery budget under the incoming Rutte IV coalition; Germany in March 2012, when markets absorbed the fiscal implications of Germany's expanded contingent liabilities under the ESM firewall following the Greek PSI deal; and Austria in August 2022 and Germany in October 2011, corresponding respectively to a large energy-relief fiscal expansion and to the EFSF leverage agreement that increased Germany's contingent sovereign exposure. Among $negative$ shocks—those reflecting unexpected fiscal improvement or spread compression—the three largest months are Canada in March 2020, where the federal fiscal backstop was perceived as credible amidst the COVID shock; Germany in September 2011, driven by continued safe-haven Bund demand and spread compression during the Eurozone crisis; and Australia in March 2020, where the sovereign risk premium fell sharply as RBA and Treasury actions were seen as stabilising the fiscal outlook. $^{27}$ Flight-to-safety episodes are also picked up as negative fiscal shocks for safe asset issuers such as the United States and Germany. 'Flight to safety' episodes are picked up only if safe corporate bond yields within the same country rise while government bond yields fall. In other words, these are episodes where foreign inflows accrue largely to sovereign assets, bolstering fiscal sustainability, rather than same-country safe corporates, implying that we capture changes in sovereign-specific risk rather than broader country risk. The pattern of these peak months closely mirrors the major fiscal episodes in these countries during our time sample, providing strong evidence that our shock series successfully captures genuine, high-salience shifts in sovereign fiscal risk perceptions.


Notes: Normalised by pooled cross-country standard deviation of monthly shocks (5.23 index points). Values denote unexpected fiscal deterioration (increased sovereign risk premium). Identified from the median-target component of sovereign yield-spread innovations (5-year maturity).

Table E.1: Top Three Positive Fiscal Risk Shock Events per Country


Notes: Normalised by pooled cross-country standard deviation of monthly shocks (5.23 index points). Values denote unexpected fiscal relief (spread compression). Identified from the median-target component of sovereign yield-spread innovations (5-year maturity).

Table E.2: Top Three Negative Fiscal Risk Shock Events per Country


Table E.3: First-stage IV diagnostics: instrument relevance and strength

Notes: First stage of the 2SLS-LP estimator. The dependent variable is the 5-year government bond yield; the excluded instrument is the median-target fiscal risk shock $s_{i,t}$ . Controls include lagged values of industrial output, CPI, the 1-year yield, CDS spreads, and the shock itself (see text for lag structure). Clustered standard errors in Panel A allow for arbitrary within-country serial correlation. Partial $R^2$ measures the incremental explanatory contribution of the instrument after partialling out all controls. The partial $F$ -statistic in the OLS column is the standard $(SSR_R - SSR_U) / \hat{\sigma}^2$ test for the exclusion of $s_{i,t}$ ; the clustered column reports $F = t^2$ using the clustered $t$ -statistic. The Stock-Yogo (2005) critical value of 16.38 corresponds to a maximum IV estimator size distortion of 10% with one excluded instrument. \* $p < 0.10$ , \*\* $p < 0.05$ , \*\*\* $p < 0.01$ .

## F Robust Inference for Panel Local Projections

## F.1 Comparison with Reduced Form Estimation

As an alternative to the two-stage procedure in equation (3), the impulse responses can be recovered using a direct (one-step) estimator in which $s_{i,t}$ itself is the regressor, bypassing the explicit first-stage regression. The LP is estimated at each horizon h by exploiting the moment condition $\mathbb{E}[s_{i,t}\varepsilon_{i,t+h}^{(h)}]=0$ to identify the fiscal-risk-driven component of yield movements directly. This approach eliminates the generated-regressor problem at the cost of not enforcing the first-stage projection structure and not permitting the two-step IV-residual sandwich correction. Figure F.1 reports the resulting IRF grid alongside 67% country-clustered confidence intervals. The main qualitative findings from the 2SLS-LP are confirmed across all dimensions: (i) a positive fiscal risk shock generates a near-term rise in inflation expectations and a boost to short-run real activity; (ii) these effects reverse at horizons beyond approximately twelve months, with CPI and industrial production both declining relative to baseline; (iii) 10-year government bond yields rise persistently; and (iv) equity prices fall with a sustained negative effect from roughly six months onward. The confidence bands from the reduced form estimator are modestly narrower than those from the 2SLS-LP, consistent with the elimination of one source of estimation uncertainty, but the difference is small and does not affect any qualitative inference.

## F.2 Alternative Fiscal Risk Shock Measures

Figure F.2 examines the sensitivity of the baseline impulse response functions to the choice of shock construction by overlaying estimates obtained from five alternative median-target shock series alongside the baseline 5-year yield series. The first alternative augments the baseline BVAR with an additional endogenous variables–bilateral spot FX rates against the USD. This measure imposes the additional sign restriction (so the model remains just-identified) that a fiscal risk shock does not have an appreciationary impact on the bilateral USD FX rate, to control for possible positive effects on government bond yields through the UIP channel. The second retains the 5-year yield but extends the information set used in the BVAR identification by including additional lags, thereby relaxing the assumption that a parsimonious lag structure fully captures policymakers' information. The third and fourth alternatives replaces the 5-year yield with the q-year and 10-year yields in the BVAR estimation, capturing the shorter- and longer-horizon component of the yield curve that may be more directly relevant for investment and sovereign borrowing decisions. The fifth replaces the level of safe corporate bond yields with the spread between government bond yields and safe corporate bond yields (both at 5-year maturity).

The results broadly confirm the robustness of the baseline findings: all six shock measures produce qualitatively similar impulse responses across inflation, industrial production, the nominal effective exchange rate, and financial variables such as term spreads and equity prices. The exchange-rate-adjusted and additional-lag specifications track the baseline closely throughout the 24-month horizon, suggesting that neither the FX component of yields nor lag length is a material driver of the identified effects. The 10-year shock series, however, displays a somewhat more persistent and larger inflationary response alongside a comparatively attenuated contraction in industrial production, con-


[[KC_IMAGE_011]]

Figure F.1: Direct IV local-projection impulse response functions

Notes: Impulse response functions using a direct (one-step) IV estimator that instruments yield5Y $_{i,t}$ with the median-target fiscal risk shock $s_{i,t}$ directly, bypassing the explicit first stage of equation (3). Horizons $h = 0, \dots, 23$ months. Shaded bands: 67% country-clustered confidence intervals. Long-difference outcome transform. Compare with Figure 3.

sistent with the interpretation that long-end yield surprises are transmitted more through inflation expectations channels than through short-run demand channels that dominate 5-year horizon shocks. On the other hand, the 1-year shock series generates a smaller inflation response and larger real activity response, consistent with the interpretation that changes in fiscal risk at the short-end of the yield curve should not affect long-term inflation outcomes. Because gov-safe corporate bond spreads are highly collinear with safe corporate bond yields, the estimated IRFs from using gov-safe corporate bond spreads instead of safe corporate bond yields are virtually indistinguishable from the baseline

## F.3 Asymptotic versus Bootstrap Standard Errors

The baseline inference relies on asymptotic IV-sandwich standard errors as described in Section 3.2. To assess robustness, we implement a panel version of the residual-based Moving Block Wild Bootstrap (MBWB) procedure adapted from Gonçalves and Kilian (2004). At each horizon h, the LP residuals $\{\hat{\varepsilon}_{i,t+h}^{(h)}\}$ are partitioned for each country i into $\lfloor T_{i}/m\rfloor$ overlapping blocks of length m (with m = 4 months and $T_{i}$ the number of usable time-series observations for country i). In the b-th bootstrap iteration, an independent Rademacher random variable $v_{b,i}^{(j)} \in \{-1, +1\}$ , each drawn with probability $\frac{1}{2}$ , is assigned to each block j of country i. The bootstrap residual for observation $(i, t)$ belonging to block j is set to $\hat{\varepsilon}_{i,t}^{*} = v_{b,i}^{(j)} \hat{\varepsilon}_{i,t+h}^{(h)}$ , and the bootstrap LP coefficient is recomputed by replacing the original residuals with $\hat{\varepsilon}^{*}$ in the IV projection. Repeating over B = 1,000 draws generates an empirical distribution of the coefficient that accounts for within-country serial correlation without relying on asymptotic approximations.

The "moving block" aspect of the method resamples residuals within contiguous blocks to handle serials correlation within LP residuals, while the "wild" component multiplies residuals at the block-level by random weights rather than resampling directly, which accounts for potential heteroskedasticity. The panel extension departs from the original Gonçalves and Kilian (2004) time-series formulation in that sign perturbations are drawn independently across countries, preserving cross-sectional independence while maintaining within-country temporal clustering; percentile-based credible intervals are extracted from the resulting bootstrap distribution.

Figure F.3 overlays asymptotic IV 67% confidence intervals with MBWB 67% credible bands for the baseline 2SLS-LP. The two sets of bands are closely aligned across all outcome variables and horizons: the MBWB intervals are marginally wider at the longest horizons where within-country autocorrelation in residuals is most pronounced, but no outcome variable changes its qualitative significance classification under either approach.

This concordance confirms that the analytical clustered sandwich estimator provides a reliable and computationally tractable approximation to bootstrap-based inference and that results are not an artefact of asymptotic approximations.

## F.4 Sampling Uncertainty versus Shock Estimation Uncertainty

Following Cieslak and Pang (2021), we distinguish between two conceptually distinct sources of uncertainty in the reported impulse responses. Sampling uncertainty arises from finite-sample variation of outcomes around the regression line conditional on a fixed realisation of the shock series, and is the component captured by the frequentist standard errors in equation (3). Shock estimation uncertainty arises because the fiscal risk shock series $\{s_{i,t}\}$ is itself an estimated object derived from a structural identification procedure, and alternative draws consistent with the identifying restrictions would yield different LP estimates. Cieslak and Pang (2021) evaluate this decomposition in a structural VAR setting: they first report impulse responses with residual-based Newey-West bands that treat the shock series as given (sampling uncertainty only), and then plot the distribution of IRFs across all structurally admissible solutions from the identification set, which combines sampling and shock estimation uncertainty. In their setting, shock estimation uncertainty is found to be negligible: the point estimate from the median-target solution lies well within the distribution of all retained solutions at every horizon.

We apply an analogous decomposition here by generating $N_{sim}$ alternative shock series consistent with the identifying restrictions via Monte Carlo simulation, and re-estimating equation (3) for each simulated draw. The resulting simulation envelope—shown in Figure F.4 alongside the baseline IRF and its asymptotic 67% and 90% confidence bands—represents the combined effect of sampling and shock estimation uncertainty. The simulation envelope is extremely narrow across all outcome variables and horizons: the distribution of LP coefficients across simulated shock draws is tightly concentrated around the baseline estimates, and the baseline point estimates lie comfortably within the simulation envelope in every case. This confirms that shock estimation uncertainty is a minor contributor to total inferential uncertainty in the present setting, and that the asymptotic IV-sandwich standard errors computed from the baseline shock series fully capture the relevant uncertainty for inference purposes.


[[KC_IMAGE_012]]

Figure F.2: Alternative Measures of Fiscal Risk Shocks

Notes: Impulse response functions using a direct (one-step) IV estimator with alternative shock measures. Baseline shock measure is in solid blue line; with three alternative measures in dashed lines. Red dashed line shows shock series from BVAR augmented with bilateral US FX spot rate, sign restriction that fiscal risk shocks are not associated with FX appreciation, and dropping US from the panel. Green dashed line is baseline shock with additional 4 lags added to the BVAR specification. Yellow (teal) dashed line replaces 5-year government bond yield with 10-year (1-year) government bond yield in BVAR shock estimation. Purple dotted line replaces 5-year safe corporate bond yields with 5-year gov-safe corporate bond spreads. Shaded bands: 67% country-clustered confidence intervals. Long-difference outcome transform.


[[KC_IMAGE_013]]

Figure F.3: MBWB credible intervals versus frequentist confidence intervals

Notes: Comparison of 67% frequentist IV-sandwich confidence intervals (as in Figure 3) with 67% Moving Block Wild Bootstrap (MBWB) credible intervals. MBWB parameters: block length m = 4 months, B = 500 replications, Rademacher sign draws applied independently within each country. The MBWB procedure follows the panel extension of Montiel Olea and Plagborg-Møller (2021) described in Appendix F.3.


[[KC_IMAGE_014]]

Figure F.4: Shock estimation uncertainty versus sampling uncertainty

Notes: Distribution of LP impulse response functions across $N_{sim}$ alternative shock series, estimated on a 5-country subsample (Brazil, Canada, Germany, Mexico, United States). Dark navy line: median of simulation distribution. Dashed navy line: baseline median-target LP estimate. Inner shaded band: 67% simulation envelope. Outer shaded band: 90% simulation envelope. The tightness of the simulation envelope confirms that shock estimation uncertainty contributes negligibly to total IRF uncertainty.

## G Asymmetric Effects of Fiscal Risk Shocks

The 2SLS-LP in equation (3) imposes a symmetric response to fiscal risk shocks, pooling episodes of rising and falling sovereign risk premia. However, there is evidence from the literature that the effects of changes in fiscal risk may be asymmetric, conditional on the sign of the shock. A rise in sovereign risk may weaken balance sheets, increasing liquidity risks when collateral constraints bind (see Bocola (2016), Gennaioli, Martin, and Rossi (2014)) or when banks have over-borrowed anticipating bailouts from the government (see Farhi and Tirole (2018)). At high levels or public debt or when fiscal space is assessed to be low, an increase in fiscal risk alongside fiscal expansion can trigger large output declines if households anticipate that higher yields trigger thresholds for default or a de-anchoring of inflation expectations, while a reduction in fiscal risk of the same magnitude may not lead to significant output declines if structural policy uncertainty is not resolved (see Bi, Leeper, and Leith (2013)).

To test whether the macro-financial transmission differs by shock direction, the second stage is augmented with a sign indicator and its interaction with the instrumented yield. Let $D_{i,t}^{+} = \mathbf{1}\{s_{i,t} > 0\}$ denote an indicator that equals unity when the underlying fiscal risk shock is positive—an unanticipated deterioration in fiscal positions—and zero otherwise. The augmented second-stage regression is:

$$
\begin{array}{r} y _ {i, t + h} - y _ {i, t - 1} = \alpha_ {i} ^ {(h)} + \delta^ {(h)} \widehat {\mathbf {y i e l d 5 Y}} _ {i, t} + \gamma^ {(h)} \left(D _ {i, t} ^ {+} \cdot \widehat {\mathbf {y i e l d 5 Y}} _ {i, t}\right) + \pi^ {(h)} D _ {i, t} ^ {+} \\ + \sum_ {\ell = 1} ^ {L _ {c}} \gamma_ {\ell} ^ {(h) \prime} \mathbf {x} _ {i, t - \ell} + \sum_ {\ell = 1} ^ {L _ {y}} \phi_ {\ell} ^ {(h)} \Delta y _ {i, t - \ell} + \varepsilon_ {i, t + h} ^ {(h)} \end{array}\tag{12}
$$

Here $\delta^{(h)}$ captures the baseline 2SLS response on negative-shock episodes ( $D_{i,t}^{+}=0$ ), and $\hat{\gamma}^{(h)}$ is the asymmetry differential: the additional marginal response on positive-shock episodes relative to negative ones following a 1-percentage-point fiscal-risk-driven increase in yield5Y. The level control $\pi^{(h)}D_{i,t}^{+}$ absorbs unconditional mean differences in outcomes between sign regimes.

Figure G.1 reports the estimated sequence $\left\{\hat{\gamma}^{(h)}\right\}_{h=0}^{24}$ alongside 67% IV-corrected clustered confidence bands. A positive value at horizon h indicates that a 1-percentage-point fiscal-risk-driven yield increase has a larger effect on the outcome when the underlying fiscal risk shock is positive (rising risk premia) than when it is negative (falling risk premia).

Results demonstrate that asymmetry is statistically significant across multiple outcome variables, although the magnitude of effects are small across all dependent variables. First, positive fiscal risk shocks generate persistently larger upward pressure on CPI inflation and inflation expectations relative to mirror-image episodes of declining fiscal risk, indicating that the inflationary transmission of fiscal deterioration is stronger and more durable than the disinflationary relief from fiscal improvement. Second, real activity effects are directionally asymmetric in the short run—an increase in fiscal risk dampens the boost in real activity in the initial months after the shock, seen in Figure 3—but not beyond two years. Third, long-end yields and equity prices are more sensitive to adverse fiscal surprises than to equivalent improvements in fiscal risk, pointing toward a tighter financial conditions channel under adverse fiscal surprises.

Results are similar when estimating $\{\hat{\gamma}^{(h)}\}_{h=0}^{24}$ in a model which includes the passive monetary policy indicator, as in Equation 10. An alternative test for asymmetry, that plots total effects in IRFs for positive and negative fiscal risk shocks, obtained from a specification that embeds the sign dummy in the first stage rather than the second stage, obtains similar results.


[[KC_IMAGE_015]]

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


[[KC_IMAGE_016]]

Figure H.1: Monetary accommodation premium $\hat{\gamma}_{A}^{(h)}$ : simple measure of passive monetary policy
Notes: Estimated accommodation premium $\hat{\gamma}_{A}^{(h)}$ from equation (10) at each horizon $h = 0, \ldots, 23$ months. A positive value indicates a larger response to a 1-pp fiscal-risk-driven yield increase during passive monetary policy episodes ( $D_{i,t}^{MP} = 1$ ) relative to active episodes, conditional on a positive underlying fiscal risk shock. Shaded bands: 67% IV-corrected clustered confidence intervals.
