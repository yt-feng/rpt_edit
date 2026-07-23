# MEASURING GLOBAL TRADE POLICY ACTIVITY $^{1}$
## Abstract

This paper introduces the Trade Policy Activity (TPA) Index, a novel indicator measuring evolving global trade policy dynamics since the Global Financial Crisis. Using a Dynamic Factor Model on comprehensive trade policy data covering 197 countries and territories, we document a structural shift around 2019 with a substantial expansion in the use of trade policies. The TPA Index also identifies cyclical episodes of heightened activity and reveals interconnections between different types of measures. We are also able to identify systematic differences in trade policy deployment among groups of economies. Additionally, we employ MIDAS (Mixed Data Sampling) regressions with high-frequency data to develop nowcasting capabilities for trade policy activity, enabling real-time identification of potential policy shifts. These results contribute to the trade policy measurement literature and offer a tool for monitoring global trade policy developments in real time.

JEL codes: F13, C32, C38, C53
Keywords: Trade policy, Dynamic factor models, Nowcasting

## 1 INTRODUCTION

Global trade policy is changing rapidly, with economies adopting various tariff and non-tariff measures that can significantly affect global trade and economic growth (IMF, 2025; WTO, 2025). In this environment, accurate and timely data on global trade policy dynamics is increasingly important for both policy and economic analysis. While there are several initiatives aimed at monitoring changes in trade and trade-related policies globally, notably by the WTO through its Trade Monitoring Database and the IMF in collaboration with the Global Trade Alert, what is currently missing is an indicator that is able to efficiently extract coherent insights from the plethora of information on measures and different policy tools (e.g. tariffs, quantitative restrictions, subsidies) across a large number of countries and products, thus capturing global trade-policy dynamics in a timely and overarching fashion. In this paper, we aim to fill this knowledge gap.

Our approach relies on detailed trade policy information starting from the Global Financial Crisis for up to 197 countries and territories and seeks to develop a novel indicator that tracks global trade policy over time and enables real-time monitoring of trade policy developments. The underlying data draws from two monitoring exercises – the WTO's Trade Monitoring Database (TMDB) and the Global Trade Alert (GTA). They track information on tariffs, other import and export restrictions, trade remedies, customs-related procedures, trade-related investment measures, subsidies and other trade-related policies, allowing for a comprehensive view of trade policy dynamics. They also differ in their methodological approaches and verification methods, making them complementary for the purposes of this exercise. For example, TMDB relies mainly on official government sources and undergoes extensive verification to track implemented measures while GTA also scouts news outlets for policy announcements.

Based on this broad set of information, we apply a Dynamic Factor Model (DFM) to extract a common factor across diverse trade policy measures and capture overall policy dynamics – i.e. overall trade policy activity. We also accommodate idiosyncratic variation in different types of measures through a block structure and identify patterns specific to each category (clearly trade-facilitating versus all other measures). We also distinguish by groups of countries, notably G20 and non-G20. Importantly, the model incorporates both nonlinear deterministic trends and stationary factors to distinguish between long-term structural shifts and cyclical components in the use of trade policy. By adapting this established macroeconomic modeling framework to high-frequency trade policy data in an innovative manner, our approach offers an advancement in the tracking of overall policy activity globally and over time.


Our results remain robust to several additional tests, including alternative specifications and approaches to extracting the underlying trend, possible compositional effects or consideration of alternative time periods. For example, inclusion of additional policies beyond the core scope of trade policy, such as FDI policies or capital flow restrictions, or consideration of additional trade-policy intensity measures (such as the number of implementing countries) do not significantly alter the results. Similarly, the exclusion of subsidies from the estimation does not impact the overall dynamics, and results also remain robust to considering alternative cut-off periods used for the estimation.

This exercise contributes to three broad strands of literature. First, it contributes to the literature measuring trade policy. Following the theoretical foundations established by Anderson and Neary (2005), Kee, Nicita and Olarreaga (2009) developed country-level indicators of trade policy restrictiveness across numerous economies. $^{3}$ These indicators have the merit of providing a theory-consistent measure of trade restrictions imposed at and behind the border, but they rely on data available with significant time lags, making them unsuitable for regular monitoring. $^{4}$ They also do not take into account dynamics in facilitating trade policy measures. Other exercises aiming to provide more up-to-date indicators of trade policy also either capture partial aspects of trade policy, do not identify common dynamics, or face temporal limitations. $^{5}$ We address these constraints by developing a parsimonious global indicator of trade policy that i) exploits a DFM to extract common dynamics at monthly frequency, ii) enables timely monitoring in rapidly evolving environments and iii) provides an alternative to existing partial or low-frequency measures of trade policy changes at the global level.

Second, we extend the application of Dynamic Factor Models to the domain of trade policy analysis. While DFMs have been widely applied in macroeconomic forecasting and business cycle analysis (Forni et al., 2000; Giannone et al., 2008, 2010), their use in identifying common trade policy dynamics represents a novel application. Specifically, we build on earlier approaches that control for idiosyncrasies in particular subgroups of series through a block structure (e.g., Bańbura et al., 2011; Bok et al., 2018; Bańbura et al., 2023), adapting this framework to distinguish between trade-facilitating and other measures. We additionally introduce new elements to account for both structural and cyclical components of trade policy dynamics, allowing us to disentangle persistent policy shifts from temporary fluctuations. This methodological innovation addresses an important challenge in the trade policy literature—the need to synthesize diverse policy instruments into a coherent, timely indicator while preserving their distinct characteristics. $^{6}$

Finally, we contribute to the rapidly expanding literature on geoeconomic fragmentation (e.g., Aiyar et al., 2023, 2024; Fernandez-Villaverde et al., 2024; Gopinath et al., 2024) by offering a distinct methodological focus. By specifically examining trade policy in its different forms, we measure the magnitude and direction of trade policy changes rather than broader geoeconomic fragmentation or geopolitical tensions. $^{7}$ This approach provides a more precise measurement of trade policies based on actual changes, complementing broader indices that capturegeopolitical tensions or uncertainty. As such, our index offers granular insights into the concrete manifestations of trade policy evolution, also enabling a deeper understanding of how specific trade measures evolve over time. Furthermore, by incorporating related uncertainty indices and relevant textual information into the nowcasting of our TPA index, we are able to produce more timely updates of the indicators and account for trade policy uncertainty and broader measures of trade policy expectations. $^{8}$ Our methodology also distinctively incorporates both trade-facilitating and other measures, enabling analysis of policy dynamics associated with their potential co-movement patterns documented in previous research (Giordani et al., 2016; Ederington and Ruta, 2016; Egger et al. 2022; Evenett et al., 2022). $^{9}$

The rest of the paper is structured as follows. Section 2 provides a brief overview of the data used for the construction of the input indicators. Section 3 outlines the methodology used. Section 4 presents the results and introduces our new Trade Policy Activity (TPA) Index. Section 5 presents the results of a series of robustness checks. Section 6 describes the data and methodology for the nowcasting of the TPA and Section 7 concludes.

## 2 DATA

## Data Sources

To construct a new global indicator of trade-policy activity, we require timely and accurate data on different types of trade-policy measures for a large sample of countries. We rely on two main data sources that have such characteristics and are key references for monitoring trade policy developments, namely the WTO Trade Monitoring Database (TMDB) and the Global Trade Alert (GTA) database. The TMDB database, created in October 2008, has been tracking trade policy measures implemented by WTO Members and Observers through formal WTO channels, i.e., communications by the governments and records by the WTO Secretariat, based on publicly available official sources, including government websites, other international organizations' websites or press releases (WTO, 2024). The GTA database, developed by the University of St. Gallen, compiles announced and implemented measures from a variety of publicly available sources, including press articles (GTA, 2022). Both databases were created in the aftermath of the Global Financial Crisis to help monitor trade policy measures adopted by governments and provide complementary trade policy information.

Both databases include information on a wide array of trade-related policy measures. The TMDB includes data on import and export restrictions (such as tariffs, quantitative restrictions and other taxes), trade remedies (i.e., anti-dumping, countervailing and safeguard measures), customs-related procedures, trade-related investment measures (such as local content requirements) and other trade measures. The GTA database covers an even wider range of measures that can affect trade, including subsidies, such as financial and in-kind grants, state loans or state aid, which have been used to monitor industrial policies (e.g., Evenett et al., 2024) and other measures that may potentially affect cross-border commercial flows. $^{10}$ For the purpose of constructing a new trade-policy indicator, only trade-policy related measures are considered (see Table A1.1 in the Annex for the list of all the measures captured in each database and those included in the baseline). $^{11}$ Combining the information from both data sources allows us to cover a wider and more timely set of policies that may affect trade and develop a single trade-policy indicator that captures the multi-faceted nature of policy changes. In addition, given that certain trade-policy measures may be under- or over-represented in a particular data source, combining them can help correct for potential idiosyncratic biases of each database.

There are several reasons as to why both databases may differ in the coverage of trade policy developments and capture different, yet complementary, dynamics. First, the scope of the type of trade-policy measures covered differs, with GTA tracking a broader set than TMDB (such as subsidies) $^{12}$ as well as measures applied to specific firms, and those adopted by subnational bodies. As such, TMDB covers changes in policy measures most directly associated with trade policy and affecting the economy as a whole (i.e., national measures applied broadly). Second, while TMDB relies mainly on official government sources and undergoes extensive verification processes, its mandate is narrower compared to that of GTA, which additionally scouts unofficial news outlets. As such, TMDB benefits from an additional layer of quality control, ensuring precise coverage of different measures across countries as stipulated by their respective laws. Meanwhile, GTA benefits from additional sources independent of government notifications or review but may also be influenced by transparency of the governmental process of notifying the public about new measures (as they rely on public announcements by the authorities). Third, while TMDB records implemented measures only, GTA also includes policy announcements, potentially providing early signals of possible policy action. Fourth, TMDB data is released twice a year (with new measures for a given period being added subsequently), while GTA data includes ongoing updates with measures being added as they are discovered over time. $^{13}$ Overall, the strength of TMDB is accuracy and quality control as it provides data on effectively implemented measures of a traditionally trade-related scope, as communicated and verified by governments. In comparison, the strength of GTA is that it tracks a broader array of measures, including in areas outside of traditional trade policy, that are announced publicly (but not necessarily implemented) and close-to-real-time updates. As such, these two sources capture different number of measures and dynamics over time (see Annex 1) and, when combined, may help better capture the overall dynamics in global trade policy.

For these reasons, in the exercise envisioned in this paper, the two databases will be complementary in terms measures covered and provide additional information on policy dynamics. More specifically, this paper aims to extract meaningful information from each data source by capturing the common dynamics through estimation of a global factor using a dynamic factor model (see the next section).

## Data Construction

To generate input variables used in the model, we first calculate the total count of new trade-policy measures introduced globally and the average number of products affected by those measures in a given month and year, by type, and data source (see Table A1.2 in the Annex for the list of variables). $^{14}$ The former set of variables (total counts) allow us to capture the extensive margin of the trade policy activity while the latter (average number of products) further gauge the extent of their application. In the robustness checks, we also test if our results hold when including a wider set of variables accounting for measures' reach, such as the number of implementing countries, or, alternatively, retaining the total counts of measures only (Section 5).

During the data construction process, we also need to account for data collection features that could impact trade policy dynamics unrelated to changes in policies. For example, as mentioned above, the GTA database allows for continuous updates of the data, with some measures added retroactively to the earlier years. If the stock of all measures at the end of the sample period was to be used directly, this may create a potential temporal bias as earlier periods would systematically contain more recorded measures due to more time being available for their discovery. To address this issue, we construct consecutive "as-of" data snapshots instead of using the complete dataset as of 2024. In addition, we implement a consistent 12-month discovery window—chosen based on GTA (2018) findings about peak discovery rates—for all observations. Under this approach, a measure is only included in our dataset if it was discovered within 12 months of its announcement date. For example, a measure announced in October 2022 is only included if it was discovered by October 2023. To implement this adjustment, we obtained precise discovery dates for each measure directly from the GTA team.

This approach enables us to compare trade-policy dynamics over time within a consistent discovery window. However, incomplete discovery periods still pose a challenge for accurately assessing the trends in the latest months and could result in systematic undercounting of measures at the end of the period. To address this issue, we exploit historical discovery patterns to calculate an adjustment for each calendar month, accounting for possible future discovery of measures. By calculating the average historical ratio of measures discovered within the 12-month reporting period after the time that has already elapsed, we can identify the proportion of measures likely to be discovered in the future. $^{15}$ This adjustment factor is then applied to the observed number of measures to account for incomplete discovery in the latest months. This approach leverages historical data to account for the truncated discovery windows to provide a more accurate representation of the likely trends in the latest period. $^{16}$

The new global indicator we have developed comprises a mix of trade-enhancing or -facilitating measures and measures that can restrict, distort or otherwise affect trade. To additionally account for possible different dynamics in those measures that clearly facilitate trade compared to all other trade measures, we also employ the classifications provided by each source $^{17}$ to divide measures into “Facilitating” and “Other”. Facilitating measures refer to any actions that clearly reduce restrictiveness, discrimination, or other distortions or otherwise ease trade (e.g., through more efficient border procedures) and the reduction of previously imposed restricting measures. The latter category includes: i) measures that restrict trade, i.e., any policy that directly reduces the amount of exports or imports according to Deardorff (2014), such as tariff increases, bans, or quotas; or ii) other remaining measures that have more ambiguous effect on trade and depend more closely on the measure’s design (e.g., increases in subsidies or the use of remedial measures), regardless of whether such measures are justified on economic or other grounds. $^{18}$ This additional categorization allows us to methodologically account for possible idiosyncratic covariation of the same type and to help better identify events associated with particular peaks of trade policy activity.

The raw data used for the construction of our variables is until May 2025, and it can be updated regularly in the future. The evolution of the time series and the extracted trends for individual variables are presented in Figure A1.1 in Annex 1. After initial data construction, we perform further data treatment steps to construct the input variables used in our model. This is explained in the next section.

## 3 METHODOLOGY

Dynamic factor models (DFMs) provide a framework for analyzing high-dimensional time series data by capturing common movements through a small number of unobserved factors. The underlying assumption is that co-movement in observed variables stems from these latent factors, while allowing for series-specific components. DFMs have become particularly valuable in policy analysis and economic forecasting, as they can efficiently process large datasets while reducing dimensionality and extracting meaningful signals.

We develop a DFM model to analyze changes in trade policy over time. The model explicitly accounts for both trending behavior and structural relationships between different types of measures. After removing seasonality using X-13ARIMA-SEATS (U.S. Census Bureau (2019)), we let $y_{t}^{*} = [y_{1t}^{*}, ..., y_{nt}^{*}]'$ denote the $n \times 1$ vector of deseasonalized time series, where i = 1, ..., n indices the individual time series variables (see Table A.1.2 in the Annex for the list). $^{19}$ The model for $y_{t}^{*}$ takes the form:

$$
y _ {t} ^ {*} = \phi (t) + \varLambda f _ {t} + \varepsilon_ {t}\tag{1}
$$

where $\phi(t)=[\phi_{1}(t),...,\phi_{n}(t)]'$ is a $n\times1$ vector of deterministic nonlinear time trends, $f_{t}\in R^{r}$ represents r factors with $2r+1\leq n$ that are uncorrelated with $\phi(t)$ , $\Lambda$ is an $n\times r$ matrix of factor loadings, and $\varepsilon_{t}=[\varepsilon_{1t},...,\varepsilon_{nt}]'$ is a stationary $n\times1$ vector of disturbances, uncorrelated with $f_{t}$ and $\phi(t)$ at all leads and lags. $^{20}$

The factors follow a stationary VAR(1) process: $^{21}$

$$
f _ {t} = A f _ {t - 1} + Q u _ {t}\tag{2}
$$

where $u_{t} \sim N(0, I_{r})$ .

As the factors are assumed to be stationary, they cannot have any deterministic or stochastic trend, and, in that sense, they are uncorrelated with $\phi(t)$ . As trade policy activity can undergo long-term and short-term changes over time, we wish to consider a trended version of the factor to capture both those structural shifts and short-term oscillations in trade policy. Hence, we let $f_{t}^{*}=f_{t}+\phi_{F}(t)$ , where $\phi_{F}(t)$ is a factor-specific trend and

$$
y _ {t} ^ {*} = \varLambda f _ {t} ^ {*} + \varepsilon_ {t} = \varLambda \phi_ {F} (t) + \varLambda f _ {t} + \varepsilon_ {t},\tag{3}
$$

which implies $\phi(t)=\Lambda\phi_{F}(t)$ . This entails that, after recovering the factor loadings from the cyclical component of the model, we can add the nonlinear trend back to the factor to consider potential level shifts in trade policies.

Following Bańbura et al. (2011), Bok et al. (2018) and Bańbura et al. (2023), we further impose a block restriction on the structure of the factor loadings. That is, we consider that the model includes a Global Factor loaded by all variables, alongside Local Factors loaded exclusively by facilitating or other measures, as defined earlier. This approach allows us to extract the common co-movements between trade policies, but also any idiosyncratic covariation that could exist between measures of the same nature. These factors maintain mutual independence. With measures ordered by category, the loading matrix takes the form:

$$
\Lambda = \left[ \begin{array}{c c c} \Lambda_ {g, f} & \Lambda_ {f, f} & 0 \\ \Lambda_ {g, o} & 0 & \Lambda_ {o, o} \end{array} \right]\tag{4}
$$

where $\Lambda_{g,}$ denote the loadings on the global factor, and $\Lambda_{f,}$ and $\Lambda_{0,}$ denote the loadings on the local factor for facilitating and other measures, respectively.

The estimation procedure consists of two sequential steps. $^{22}$ As the trend is exogenous, we first remove it from each time series using a local regression approach. That is, we fit a local quadratic regression where the least-squares objective function is weighted by the inverse of the distance between points to capture local patterns in the data more effectively (see Cleveland et al. (1992), and Li and Racine (2007)). This approach allows for greater flexibility than a global parametric approach, as it does not restrict the functional form of the trend. $^{23}$ To assess the robustness of this approach (which constitutes our baseline), we experimented with different choices of weights, i.e., setting weights to 0 if the distance is larger than a given threshold, and with the trend-filtering approach of Tibshirani (2014), a fully data-driven nonparametric method for trend estimation, obtaining very similar results.

Under the assumption of trend exogeneity, our estimator of the trend is consistent and asymptotically normal. We then define the detrended series as $y_{t} = [y_{1t}, \ldots, y_{nt}]' = [y_{1t}^{*} - \phi_{1}(t), \ldots, y_{nt}^{*} - \phi_{n}(t)]'$ , which satisfies $y_{t} = \Lambda f_{t} + \varepsilon_{t}$ .

After the trend has been removed, we follow the approach in Bańbura and Modugno (2014), and construct a joint likelihood based on the distribution of u and $\varepsilon$ . The approach is relatively simple to implement and allows for potential missing values in some of the series, which account for about 0.2% of our total sample size. The approach in Bańbura and Modugno (2014) further requires the assumptions that $\varepsilon$ is independent of u, and that $\varepsilon \sim N(0,R)$ , where R is a diagonal matrix that collects all the variances of $\varepsilon$ .

The parameter of interest is then set to be $\theta = (\Lambda, A, R, Q)$ , which represents the collection of all unknown parameters in the model. $\Lambda$ are the factor loadings; A collects the auto-regressive coefficients of the factors' dynamics; R is the diagonal matrix that collects the variances of $\varepsilon$ ; and Q is a matrix that captures the covariance structure between the shocks to each factor.

Given our assumptions, $y_{it}$ is a linear combination of two stationary and independent Gaussian random variables. It is therefore itself stationary and follows a normal distribution. Hence, before fitting the joint likelihood, we need to ensure that removing a nonlinear deterministic trend effectively removes all sources of nonstationarity from our time series. We therefore test each one of them for stationarity using both the unit root test of Kwiatkowski et al. (1992) and the Augmented

Dickey-Fuller (ADF) test (see Dickey and Fuller, 1979). Neither test can reject that the time series are stationary. $^{24}$

The joint likelihood of y and f is then written as:

$$
l (Y, F; \theta) = \prod_ {t = 1} ^ {T} f _ {\varepsilon | R} (y _ {t} - \varLambda f _ {t}) f _ {u | Q} (f _ {t} - A f _ {t - 1})\tag{5}
$$

We maximize this using the expectation-maximization (EM) algorithm. At each iteration j, the expectation step computes $L\big(\theta,\theta^{(j)}\big)=E_{\theta^{(j)}}[l(Y,F;\theta)|\Omega_{T}]$ , where $\Omega_{T}\subseteq Y$ accounts for missing data. In the maximization step, we then compute $\theta^{(j+1)}=\operatorname{argmax}_{\theta}L\big(\theta,\theta^{(j)}\big)$ . The implementation combines the Kalman smoother with multivariate regressions when $f_{t}$ is observed.

To recover trends in the factors, we define $\Phi_{t}$ as a $n \times T$ matrix of normalized trends from the initial data, and $\Phi_{F}$ as the factor trend. The relationship $Y_{t} + \Phi_{t} = \Lambda(F_{t} + \Phi_{F}) + \varepsilon_{t}$ holds, where $\Lambda\Phi_{F} = \Phi_{t}$ since $\varepsilon_{t}$ is stationary. The factor trend can then be recovered as $\Phi_{F} = (\Lambda' \Lambda)^{-1}(\Lambda' \Phi_{t})$ .

Hence, we have that

$$
f _ {t} ^ {*} = f _ {t} + \Phi_ {F},\tag{6}
$$

is the trended global factor.


## 4 RESULTS

Baseline Results: The Overall Trade Policy Activity Index

This section presents the new Trade-Policy Activity (TPA) Index that aims to capture in a systematic fashion the dynamics in overall trade policy activity worldwide over time.

The Index plotted in Figure 1 is based on the trended global factor in Equation 6 that is normalized to a reference period at the start of the sample (with the mean value for the period January 2010-December 2011 set to 0) for ease of interpretation. The baseline value of 0 represents average trade policy activity during the reference period. Scale normalization facilitates comparison across the different index variants presented in the paper. Changes in the index reflect the temporal evolution of global trade policy, with values rising above 0 indicating heightened activity and values below 0 indicating reduced activity relative to the baseline. $^{26}$ As shown in the figure below, the index captures fluctuations in trade policy, including structural shifts, reflected in the trend (dashed grey line), and the short-term changes associated with specific events, reflected in the global factor (black line). $^{27}$

Figure 1 Trade-Policy Activity (TPA) Index

[[KC_IMAGE_001]]

Note: Trade-Policy Activity (TPA) Index (black line) refers to the global factor estimated using the block structure by type of measure (i.e. facilitating and other) and including a trend (dashed grey line) added after the estimation. The factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0). The trend (shown in grey dashed line) is a local quadratic trend whereby regression is weighted by the distance between points. The raw data is until May 2025 in the baseline and the indicator is smoothed using a moving average over the last three months.

Overall, the index has shown a flat trend for nearly two decades before a marked pick-up around 2019, and a rising trajectory thereafter. The change largely corresponds to the period marked after the COVID-19 pandemic and the combination of a larger use of border and behind-the-border measures to achieve trade and non-trade objectives, heightened trade policy tensions among large economies and the overall rise in the level of geopolitical risk. $^{28}$


## Understanding the Role of Different Types of Measures

The global index captures the common movement in all types of trade policy measures, including measures that facilitate trade, such as more efficient border procedures, and those that could restrict or distort it, such as greater import or export restrictions and subsidies. It also accounts for the idiosyncratic variation within those two types of measures through the introduction of local factors by measure type (see Equation 4). This approach allows us to reflect the fact documented in the trade literature that facilitating and other trade policy measures may move in tandem across different trading partners or even for the same economy, which could be for several reasons (explained below). To study this aspect, we use the factor loadings on different measures obtained from the baseline regression and re-estimate the global factor using only the loadings for a given measure type, i.e., facilitating and other measures, respectively (see Figure 2).

Figure 2 The Role of Facilitating and Other Measures

[[KC_IMAGE_002]]

Note: Our baseline result is depicted by the grey line. "Facilitating Measures" ("Other Measures") refer to the estimates of the global factor that loads exclusively on facilitating (other) measures while using factor loadings from the baseline regression accounting for both types of measures. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

These estimates follow a similar pattern as the baseline, illustrating that facilitating and other measures tend to coincide at the global level, but may display distinct patterns in specific periods. For example, the factor loading on facilitating measures displays a spike around the implementation of the TFA in 2017, while other measures do not display such dynamics. $^{32}$ During the periods of crisis – such as the COVID-19 pandemic and the war in Ukraine – the adoption of facilitating measures accelerated alongside other measures, as many countries aimed to compensate for shock-induced shortages of certain goods, such as medical equipment and raw materials, by taking measures that ease trade. In addition, the latest period, in the first months of 2025, has shown acceleration in the use of other measures. As part of robustness checks and extensions, we go a step further and distinguish between a subset of other measures that directly restrict trade – following the definition of Deardorff (2014) – from the overall set of other measures to study further differences in their dynamics (see Figure 4).

While certain types of measures that can affect trade often lead to more measures of a similar nature (as witnessed by recent increases in industrial policies – see e.g., Evenett et al. 2024), there are several reasons why facilitating and other measures may move together as well. First, during crises, restrictive measures and the like may be implemented alongside facilitating measures to ensure adequate supply of certain goods (e.g., food, medical supplies, and personal protective equipment). Countries may impose export restrictions or use domestic subsidies on food products or medical devices while simultaneously facilitating imports for those goods to address shortages and ensure adequate supply (e.g., Giordani et al. 2016; Evenett et al. 2022). Second, as explained above, countries may accompany the use of facilitating measures with an increase in the use of other measures that can restrict trade to moderate changes in market access (so-called "policy substitution", as shown e.g. in Ederington and Ruta, 2016, and Beverelli et al., 2019). Third, when some countries adopt measures that restrict or otherwise distort trade, other countries may, in certain cases, implement facilitating measures to compensate for lost market opportunities or reduce distortions. This would result in the increase in both facilitating and other measures at the global level. $^{33}$ As such, we consider it meaningful to capture both types of measures in the overall indicator of global trade policy activity.

## Accounting for the Economic Weight of Adopting Countries

Our baseline Trade-Policy Activity Index aims to capture dynamics in trade policy activity worldwide, regardless of the size of the adopting economies, to help identify broad-based policy trends. Yet, measures taken by certain countries – for instance, with a large contribution to the global economy – may influence more the global policy environment. Hence, we present additional results that aim to account for the size of the implementing economy. Specifically, we report the estimates from regressions undertaken separately on the sample of the world's largest economies (G20) and other (non-G20) economies (Figure 3).


Figure 3 Trade-Policy Activity (TPA) Index: G20 versus non-G20

[[KC_IMAGE_003]]

Note: Our baseline result is depicted by the grey line. The figure shows the global factor estimated separately on a sample of G20 economies (green line) and non-G20 economies (yellow line). Divergent patterns across countries may reflect differences in trade-policy activity but may also be influenced by differential coverage of countries, including over time, in input indicators. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

## 5 ROBUSTNESS AND EXTENSIONS

We undertake several checks to ensure the robustness of our results and introduce further extensions. These are reported in this section and Annex 2.

First, we test an alternative specification whereby instead of estimating a global factor using block restriction on the structure of the factor loadings following Equation 4, we estimate a model with one global factor only. This helps us ensure that the dynamics captured by the model are not driven by our choices of block structure. The results are robust and shown in Figure A2.3 in Annex 2.

Second, we consider the robustness of our approach to trend extraction explained in Section 3. Specifically, we experimented with different choices of weights, i.e., setting weights to 0 if the distance is larger than a given threshold, and with the trend-filtering approach of Tibshirani (2014), a fully data-driven nonparametric method for trend estimation. The overall shape of the global factor is robust to the choice of trend extraction method (Figure A2.4 in Annex 2). Yet, some differences emerge, particularly at the beginning and end of the sample period. Reassuringly, the local quadratic trend used in the baseline yields a factor that lies between the different extremes. This suggests that it offers a balanced approach being less influenced by end-point effects.

Third, we also consider the robustness of results by adding or removing additional input indicators. In that respect, we first add input indicators that account for the number of countries implementing a given type of measure. This also serves as an additional measure of intensity (on top of the number of products affected) and helps us gauge that the trend in the global factor is not driven by measures adopted by only a few countries. The results are similar while the factor shows an even stronger upward trajectory since 2019 once we also account for the number of implementing countries (see Panel A in Figure A2.5). This is consistent with the broad-based increase in trade policy activity following the COVID-19 pandemic, reflected in the results for G20 and non-G20 economies reported above. We also test the opposite approach and estimate the global factor using the counts of measures without any intensity measures. The results remain similar to the baseline (Panel B in Figure A2.5).

In a similar vein, we also consider how the results change if only input indicators for one type of measures are used in the estimation. In the main analysis, we estimate a global factor using the factor loadings from the baseline estimation, while setting the loadings for one type of measure to zero, respectively, to understand better the dynamics associated with different types of measures. In an alternative approach, we restrict the sample of input indicators to one type of measure only (i.e., facilitating or other, respectively) and re-estimate the global factor without allowing the factor loadings to be influenced by other types of policies. The results remain very similar to those reported earlier (see Panel A in Figure A2.6). As an additional test, we also include all additional measures in the GTA that are not directly related to trade (i.e., MAST chapters CAP, F, FDI, G, MIG in the UNCTAD (2019) classification and an unknown policy instrument). The results again remain very similar to the baseline (see Panel B in Figure A2.6), which suggests that, to the extent that GTA captures those policies, our findings are robust to considering a broader set of policies with a possibly similar purpose.


Figure 4 Alternative Composition of Measures: The Role of Trade-Restrictive Measures?

[[KC_IMAGE_004]]

Note: Our baseline result is depicted by the grey line. The figure reports results when the global factor is estimated on the sample of facilitating and other measures, respectively, as in Figure 2 and additionally provides an estimate for the sub-sample of measures within the latter category that have a restrictive character. These are tariffs and non-tariff measures under MAST chapters E, C, I and certain subcomponents of P (excluding tax-based export incentive, export subsidy, trade finance, other export incentive, export-related non-tariff measure, nes) that are labelled "amber" or "red" in GTA and "other measures" or "trade remedy" in TMDB. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Finally, we want to ensure that our indicator is not unduly influenced by a specific end period. As such, we also estimate the global factor using the same starting date (i.e., January 2010) and alternative end periods (i.e., October 2022 and October 2020) instead of the baseline period. The results remain very similar (Figure A2.7): the factor follows the same pattern across those different variants with spikes being less pronounced when the longest sample period is used. We also conduct a test to ensure that the application of our adjustment to account for the incomplete discovery of measures in the GTA towards the end of a given period does not influence our results through its possible effect on the factor loadings on the different variables. As such, we re-estimate the global factor using the adjusted data while keeping the factors loadings from a regression through October 2024, prior to the application of the end-of-period adjustment (see Table A1.3 in the Annex). The results remain virtually unchanged (see Figure A2.9 in Annex 2), suggesting the adjustment to the selected time series does not unduly affect the factor loadings.

## 6 NOWCASTING TRADE POLICY ACTIVITY

The practical usefulness of the TPA index could be further enhanced by exploring its potential for real-time monitoring and early detection of trade policy developments. As trade policy information is collected with inherent lags, complementary high-frequency data may offer valuable insights in this regard. This section presents an exploratory analysis using high-frequency textual information and relevant economic predictors to assess the feasibility of nowcasting the TPA index and detecting signals of potential policy shifts. While this represents a preliminary investigation using relatively simple methods, the exercise demonstrates one possible direction for enhancing the TPA's practical applications and illustrates how the index's inherent real-time properties might be augmented.

We use the term "nowcasting" to describe our one-month-ahead predictions of trade policy activity. We follow Bańbura, Giannone, Modugno and Reichlin (2013, 2023), who define now-casting as "the prediction of the present, the very near future and the very recent past." This broader definition emphasizes timeliness rather than a strict forecast horizon. $^{35}$ In the case of trade policy, the contemporaneous monthly series is rarely fully observable in real time, while partial data (e.g. GTA announcements and selected high-frequency proxies) are available. Our choice to adopt the broader definition is, hence, deliberate: it captures the real-time monitoring purpose of our work, namely reconstructing the current and very near-future state of trade policy activity before it is observable in official data.

## Data and Methodology for Nowcasting

We build our baseline nowcast on 23 trade-policy-related predictors, which we group into three categories later. These are incorporated into a MIDAS (Mixed Data Sampling) framework, chosen for its simplicity and strong performance in mixed-frequency settings (Ghysels and Qian, 2019). While more complex estimation techniques, such as regularized regressions or ensemble methods may be considered in future work, this framework provides a suitable basis for the current analysis. The predictors are sourced from various datasets and categorized into three groups. High-frequency weekly textual measures based on trade-policy-related search terms form the core of the model, and monthly economic and uncertainty indicators are included as complementary variables to enhance predictive performance. $^{36}$ For high frequency data of trade-policy-related topics, we turn to searches from Google Trends and use weekly time series to track policy-related topics or keywords $^{37}$ as a proxy for public and media discourse on trade policy, following the approach of Choi and Varian (2012). Given that certain policies are widely discussed prior to their official announcement and implementation, search interest can serve as an early indicator of policy direction and potential shifts. $^{38}$

In that context, a set of Google Trends topics is selected to capture public attention towards three key dimensions of trade policy: (i) direct discussions on trade policy instruments (e.g., tariffs, export controls), (ii) institutional references related to trade policies (e.g., WTO, trade agreements), and (iii) indirect references to possible trade policy shifts (e.g., protectionism, liberalization). This classification is guided by prior trade policy literature that exploits relevant linguistic terms to capture trade policy (Caldara et al., 2020; Ahir et al., 2022; Hoekman and Nicita, 2021; Evenett and Fritz,

2022; IMF, 2023) and emphasizes the importance of these dimensions in portraying policy activity. Several google trend topics are excluded due to multicollinearity or a lack of meaningful variation. $^{39}$ The final high-frequency dataset used in the nowcasting exercise includes 17 variables. To complement, we include monthly commodity index data in the analysis, as is found to be sensitive to policy changes and commonly viewed as an early indicator of shifts in economic activity, mainly due to its broad industrial use (Miranda-Pinto et al., 2024). Specifically, we keep the copper price index, the total commodity index, and the non-energy commodity index to capture forward-looking economic dimensions. $^{40}$ We also include uncertainty indices that are closely linked to global and trade policy developments, such as the Geopolitical Risk Index and the Trade Policy Uncertainty Index. These indicators are incorporated in the spirit of Fernández-Villaverde et al. (2024), capturing the role of policy-related uncertainty. All variables are expressed in growth rates to maintain stationarity. All predictors used are obtained from publicly available sources covering the period from January 2010 to June 2025 and are listed in detail in Annex 3.

Given that many of our predictors are available at higher—notably weekly—frequencies, predicting a monthly target poses the challenge of preserving informational content without excessive aggregation. MIDAS (Mixed Data Sampling) regressions offer a suitable framework in this context as they allow high-frequency predictors to enter the model directly through parsimonious distributed lag polynomials. This approach avoids overparameterization and mitigates complications related to lag-order selection. Thus, we employ Autoregressive Distributed Lag – Mixed Data Sampling (ADL-MIDAS) with polynomial parameter profiling, as developed in Ghysels and Qian (2019). This approach estimates the MIDAS regression via ordinary least squares (OLS), incorporating a beta polynomial weighting scheme.

From equation (6) above, the estimated trended factor is given by:

$$
\hat {f} _ {t} ^ {*} = \hat {f} _ {t} + \widehat {\varPhi} _ {F}.
$$

In Equation (7), we consider forecasting the cyclical component of the model through an h-step-ahead high-frequency regressor ADL-MIDAS model, applied to our monthly/weekly data structure. $^{41}$

$$
\hat {f} _ {\mathrm{t+h}} ^ {\mathrm{L}} = a _ {\mathrm{h}} + \phi_ {1} \hat {f} _ {\mathrm{t}} ^ {\mathrm{L}} + b _ {\mathrm{h}} C \left(\mathrm{L} ^ {\frac {1}{\mathrm{m}}}; \theta_ {\mathrm{h}}\right) \mathrm{x} _ {\mathrm{t}} ^ {\mathrm{H}} + \rho_ {\mathrm{h}} \mathrm{x} _ {\mathrm{t}} ^ {\mathrm{L}} + e _ {\{\mathrm{t+h} \}} ^ {\mathrm{L}},\tag{7}
$$

where $C\left(L^{\left\{\frac{1}{m}\right\}};\theta_{h}\right)$ is a weighting function parameterized by $\theta_{h}$ that aggregates high-frequency data. It is based on the Beta probability density function which involves two parameters:

$$
c (j; \theta_ {1}, \theta_ {2}) = f (j / j _ {\max}; \theta_ {1}, \theta_ {2}) / \sum [ j = 0 \text {to} j _ {\max} - 1 ] f (j / j _ {\max}, \theta_ {1}, \theta_ {2})\tag{8}
$$

$$
f (x, a, b) = (x ^ {\wedge} (a - 1) (1 - x) ^ {\wedge} (b - 1) \Gamma (a + b)) / (\Gamma (a) \Gamma (b))\tag{9}
$$

To account for more recent information, we add leads to Ghysels and and Qian (2019)'s model, following the approach of Andreou, Ghysels, and Kourtellos (2013). Adding leads allows us to include as much up-to-date information as possible when making nowcasts. For example, if we are nowcasting the next month's outcome and are already in the first two weeks of that month, we may have access to partial weekly information about what has happened during that month. By including leads, we can incorporate this partial information into our model, thereby improving forecast accuracy. For instance, with $\frac{i}{m}$ additional observations, the horizon h shrinks to $h - \frac{i}{m}$ , and the above equation becomes:

$$
\hat {f} _ {\left\{t + h | T + \frac {i}{m} \right\}} ^ {\{L \}} = a _ {h - \frac {i}{m}, T} + \phi_ {1} \hat {f} _ {t} ^ {L} + b _ {h - \frac {i}{m}, T} C \left(L ^ {\{\frac {1}{m} \}}; \theta_ {h - \frac {i}{m}, T}\right) x _ {t + \frac {i}{m}} ^ {H} + \rho_ {h} x _ {t} ^ {L} + e _ {\left\{t + h | T + \frac {i}{m} \right\}} ^ {\{L \}},\tag{10}
$$

where $\hat{f}_{\left\{t+h|T+\frac{i}{m}\right\}}^{\{L\}}$ is the (low-frequency) monthly estimated global factor from in Section 3 at horizon h, $a_{h-\frac{i}{m}T}$ is the intercept capturing the baseline level, and $x_{t+\frac{i}{m}}^{H}$ and $x_{t}^{L}$ are the high- and low-frequency predictors, respectively. Standard assumptions are imposed on the error term, including homoskedasticity and normality, for simplicity.

As outlined earlier, in our nowcasting exercise, we focus on the stationary component of the TPA Index, as short-term volatility is more relevant for real-time assessment. The long-term trend component is more persistent and likely less sensitive to high-frequency shocks in the short run. To recover the full index, we simply extrapolate ahead the trend component estimated in Section 3 and add it to the nowcasted stationary part. This extrapolation is done by a quadratic approximation of the trend over the previous 36 months of data. The length of the estimation window is chosen as a trade-off between incorporating enough past information to accommodate potential future changes in the trend, and the scenario in which the current trend would simply continue unchanged in the future. This extrapolation approach — based on the same assumptions used in Section 3 — yields low out-of-sample forecast errors (below 0.1 across rolling windows of varying lengths s), validating its empirical adequacy.

## Nowcasting the Trade-Policy Activity Index

This section shows a first set of nowcasting results for the overall Trade-Policy Activity Index. Standard pre-estimation procedures are applied, ensuring stationarity, addressing seasonality and multicollinearity, removing outliers, and selecting appropriate lag structures. $^{42}$ We report the baseline prediction results based on a one-step-ahead specification, with the forecast horizon set to h = 1.

We employ a recursive estimation approach with an expanding window: starting from an initial 100-month sample, we gradually increase the sample size by adding one additional month at each step, which helps ensure stable estimates. Specifically, to nowcast the index for January 2020, we estimate the model parameters using all available data up to December 2019 and perform a one-step-ahead nowcast. As we move to the next period, we update the dataset by incorporating the actual value for January 2020, re-estimate the model, and nowcast February 2020. This iterative process ensures that our predictions continuously adapt to the latest available information.

For the model selection, we consider a set of standard monthly predictors used in the trade policy literature, including commodity prices and uncertainty indices (see e.g., Bown and Crowley, 2013; Baker et al., 2016, Caldara et al., 2020/2022). $^{43}$ For the selection of the high-frequency text-based predictors from Google Trends, we follow a simple approach. Specifically, we evaluate each such predictor individually by estimating the ADL-MIDAS model that includes one high-frequency predictor at a time, along with lower-frequency controls. We rank the predictors by ascending RMSE (Root Mean Squared Error). Detailed results are presented in Annex Table A4.1. We then implement a high-frequency predictor selection strategy based on a forward-ranking with step-wise forward selection. Specifically, we start with the predictor that produces the lowest individual RMSE, and iteratively expand the model by adding the next-best predictor. This approach reflects the logic of marginal contribution $^{44}$ , allowing us to assess whether increasing the number of predictors enhances forecast performance, while ensuring sufficient high-frequency information for timely prediction. We find that after including three best predictors $^{45}$ , the RMSE reaches the minimum value. To verify that no further improvement occurs with even larger predictor sets, we report in Annex Table A4.2 the performance of all models with varying numbers of predictors. This confirms that the current selection of high-frequency predictors delivers the best predictive performance within our framework.

The nowcasting result is plotted in Figure 5. From April 2019 to June 2025, the nowcasted values are shown as a solid red line (referred to as one-step predictions). The actual values are displayed as a solid black line to evaluate model performance. In most monthly comparisons, the nowcasts accurately predict the direction in which trade policy activity evolves and provide more timely signals of turning points observed in the actual data compared to the AR (1) forecasts. $^{46}$ For example, in July 2020, the one-step-ahead nowcast reached its bottom before recovering, signalling an increase in trade policy activity one months before the AR (1) prediction. This timely signal may be attributed to significant changes in policy dynamics during the second quarter of 2020, as governments and international organizations responded to the COVID-19 pandemic with a range of measures, which may have been picked up by search engine results due to media coverage. Similarly, from December 2021 to January 2023, trade policy activity remained at a relatively high level. The nowcasting model detected the initial sharp increase concurrently with the actual rise in the index, and earlier than the AR (1) prediction—potentially reflecting policy adjustments in response to geopolitical tensions.

Comparing the estimated series with the actual values (solid black line) indicates that the ADL-MIDAS model performs well in capturing the dynamics of trade policy activity and in providing timely alerts about turning points.

Figure 5 Nowcasting with MIDAS: Trade-Policy Activity Index

[[KC_IMAGE_005]]

Note: Authors calculations. The time series data begins in January 2017 to enhance the visibility of the nowcasting period and its results. Commodity indices, uncertainty indices, and three most relevant weekly data are put as predictors in the one-step predictions shown by the solid red line. The trend component (dashed grey line) represents the actual trend extracted from the index. The Trade-Policy Activity (TPA) Index (black line) refers to the actual index constructed in the Section 4. The estimated trend (dashed red line) is the extrapolated quadratic trend recursively estimated by the last 36 previous observations in the actual trend. The shaded light red area represents the 90 percent prediction intervals constructed using a bootstrap procedure (see footnote 44).

For the periods beyond May 2025 – the cut-off time for our DFM estimated index - we generate forecasts for the subsequent month. Our predictor dataset extends through June 2025, allowing us to employ a one-step-ahead nowcasting approach. This means that the index for month t+1 is forecasted using observed values of the monthly predictors in t and weekly predictors in t with some observable leads in t+1. $^{47}$ The resulting forecasted index is used as a lagged predictor for predicting the index for the next month t+1. This procedure implies that while the predictors are observed in real time, the target variable is recursively forecasted from May onwards.

The results indicate an uptick in trade policy activity that seems to correspond to the general perceptions of the international trade environment in 2025. $^{48}$ Following a decline in the global trade policy activity during the third quarter of 2024, the model anticipates a renewed increase toward the end of 2024 and into 2025—consistent with patterns observed in current trade monitoring. While we focus on one-step-ahead nowcasting in this paper, the ADL-MIDAS framework can be extended to forecast multiple steps ahead. However, the approach is more suited to short-term projections. For longer horizons, more structural or system-based methods could be considered.

## 7 CONCLUSION

This paper applies a DFM methodology to develop a new indicator – Trade-Policy Activity (TPA) Index – to help better trace trade policy changes at the global level over time and signal emerging trade policy developments. Building on two comprehensive data sources covering diverse trade policy measures, our approach captures the complex nature of modern trade policy making. Through methodological adaptations, the framework identifies both structural changes and cyclical movements in trade policy. It also enables the construction of sub-indicators for different policy types (trade-facilitating and other measures) and economic groups (G20 and non-G20 economies).

The TPA Index offers several valuable applications that leverage its unique construction and real-time properties. First, as a comprehensive measure of global trade policy, the index serves as a useful control variable for empirical research, enabling scholars to account for the broader policy environment when studying the effects of specific trade measures. This addresses a persistent challenge where omitted variable bias from unmeasured policy activity can confound causal inference. Second, the index is inherently well-suited for real-time monitoring and nowcasting applications. The underlying Dynamic Factor Model framework naturally accommodates mixed-frequency data from different monitoring sources and provides timely updates as new trade policy measures become available, making it valuable for tracking emerging policy trends as they unfold. Our analysis demonstrates that this capability can be further enhanced by incorporating complementary high-frequency predictors—such as Google Trends data and economic indicators—with preliminary results showing improved forecast accuracy in detecting turning points such as the policy activity uptick anticipated for early 2025. Third, the index provides a foundation for rigorous econometric analysis of trade policy impacts through event studies and local projections leveraging high-frequency nature of the indicator after carefully addressing endogeneity concerns specific to a particular setting.

Our work offers several promising avenues for future research and extensions. First, the scope of variables, measures and sources could be progressively expanded over time to capture additional sources of trade-policy variation and – potentially – further reflect the differential measure intensity. Second, further disaggregation could provide insights at country, country-pair, or sectoral levels to support broader empirical applications in the trade and macroeconomics literatures. Third, the TPA Index could be tested empirically to examine relationships between trade policy activity and key economic outcomes, including trade flows, output, productivity, and economic growth. Finally, numerous possibilities exist to explore alternative nowcasting approaches, such as nonlinear MIDAS models, machine learning-based forecast combinations, or structurally motivated specifications that incorporate theoretical insights on trade and policy uncertainty.

Ahir, H., Bloom, N., & Furceri, D. (2022), The World uncertainty index. National Bureau of Economic Research Working Paper.

Aiyar, S., D. Malacrino, and A. F. Presbitero (2024), "Investing in friends: The role of geopolitical alignment in FDI flows," European Journal of Political Economy.

Aiyar, S., J. Chen, C. H. Ebeke, R. Garcia-Saltos, T. Gudmundsson, A. Ilyina, A. Kangur, T. Kunaratskul, S. L. Rodriguez, M. Ruta, T. Schulze, G. Soderberg, and J. P. Trevino (2023), "Geoeconomic Fragmentation and the Future of Multilateralism," Working Paper 2023/001, International Monetary Fund: Washington DC.

Anderson, J. E. and J. P. Neary (2005), Measuring the Restrictiveness of International Trade Policy, Cambridge: MIT Press.

Andreou, E., Ghysels, E., and Kourtellos, A. (2013), Should macroeconomic forecasters use daily financial data and how?. Journal of Business & Economic Statistics, 31(2), 240-251.

Bagwell, K., and Staiger, R. W. (2003), "Protection and the business cycle." Advances in Economic Analysis & Policy, 3(1), 1-43.

Bańbura, M., & Modugno, M. (2014), Maximum likelihood estimation of factor models on datasets with arbitrary pattern of missing data. Journal of Applied Econometrics, 29(1), 133-160.

Bańbura, Marta, Domenico Giannone, and Lucrezia Reichlin. 2011. "193 Nowcasting." In The Oxford Handbook of Economic Forecasting. Oxford University Press.

Bańbura, Marta, Domenico Giannone, Michele Modugno and Lucrezia Reichlin (2013), Chapter 4 - Now-Casting and the Real-Time Data Flow, Editor(s): Graham Elliott, Allan Timmermann, Handbook of Economic Forecasting, Elsevier, Volume 2, Part A.

Bańbura, M., Belousova, I., Bodnár, K., Tóth, M. B. (2023), Nowcasting employment in the euro area, ECB Working Paper 2815, European Central Bank (ECB), Frankfurt a. M., https://doi.org/10.2866/634513


Blanchard, E. and Matschke, X. (2015), "U.S. Multinationals and Preferential Market Access." Review of Economics and Statistics, 97(4), 839-54.

Blanchard, E. J, C. P Bown, R. C Johnson, (2025), Global Value Chains and Trade Policy, The Review of Economic Studies, https://doi.org/10.1093/restud/rdaf017

Bok, B., Caratelli, D., Giannone, D., Sbordone, A. M., and Tambalotti, A. (2018). Macroeconomic nowcasting and forecasting with big data. Annual Review of Economics, 10(1):615–643.

Bown, C. and M. Crowley (2013), Import protection, business cycles, and exchange rates: Evidence from the Great Recession, Journal of International Economics, 2013, Vol. 90, Issue 1, 50-64.

Caldara, D., M. Iacoviello, P. Molligo, A. Prestipino, and A. Raffo (2020), "The Economic Effects of Trade Policy Uncertainty," Journal of Monetary Economics, 109, pp.38-59.


Cebrián E., and J. Domenech (2024), Addressing Google Trends inconsistencies, Technological Forecasting and Social Change 202, 123318.

Cerdeiro, D. A., and Nam, R. J. (2018). A multidimensional approach to trade policy indicators. International Monetary Fund. Cleveland, W.S, E. Grosse and W. M. Shyu (1992) Local regression models. Chapter 8 of Statistical Models in S eds J.M. Chambers and T.J. Hastie, Wadsworth & Brooks/Cole.

Choi H. and H. Varian (2012), "Predicting the Present with Google Trends," The Economic Record, The Economic Society of Australia, Vol. 88(s1), pp. 2-9, June.

Deardorff, A. V. (2014), Terms of Trade: Glossary of International Economics, (2nd Edition) 2nd Revised ed. Edition

Dickey, D.A., and Fuller, W. A. (1979) Distribution of the Estimators for Autoregressive Time Series with a Unit Root. Journal of the American Statistical Association, 74(366), 427-431.


Egger, Peter H.; Masllorens, Gerard; Rocha, Nadia; Ruta, Michele (2022), Scarcity Nationalism during COVID-19: Identifying the Impact on Trade Costs. Economics Letters.

Estefania-Flores, J., D. Furceri, S. A Hannan, J. D. Ostry, A. K. Rose, (2022), A Measurement of Aggregate Trade Restrictions and their Economic Effects, International Monetary Fund: Washington DC.

Evenett S, Fiorini M, Fritz J, Hoekman, B., Lukaszuk, P., Rocha, N., Ruta, M., Santi, F., Shingall, A., (2022), Trade policy responses to the COVID-19 pandemic crisis: Evidence from a new data set. World Economy 2022; 45: 342–364. https://doi.org/10.1111/twec.13119

Evenett, S., A. Jakubik, F. Martín, and M. Ruta (2024), "The return of industrial policy in data," The World Economy, Vol. 47, No. 7, pp. 2762–2788.

Fajgelbaum, P. D. and A. K. Khandelwal (2022), "The Economic Impacts of the US–China Trade War," Annual Review of Economics, 14 (Volume 14, 2022), 205–228.

Fajgelbaum, P., P. Goldberg, P. Kennedy, A. Khandelwal, and D. Taglioni, (2024), "The US-China trade war and global reallocations," American Economic Review: Insights, 6 (2), 295–312.

Fajgelbaum, P. D, P. K. Goldberg, P. J. Kennedy, and A. K Khandelwal (2020), "The Return to Protectionism," The Quarterly Journal of Economics, 2020, 135 (1), 1–55.

Fernández-Villaverde, J., Mineyama, T., and Song, D. (2024). Are we fragmented yet? Measuring geopolitical fragmentation and its causal effects.

Forni M, Hallin M, Lippi M, Reichlin L. (2000), The generalized dynamic-factor model: identification and estimation. Rev. Econ. Stat. 82:540–54

Freund, C., A. Mattoo, M. Ruta, and A. Mulabdic (2024), "Is US trade policy reshaping global supply chains?," Journal of International Economics, 152, 104011.

Giannone, D., Reichlin, L., and Small, D. (2008), Nowcasting: The real-time informational content of macroeconomic data. Journal of Monetary Economics, 55(4):665–676.

Giordani, P. E. N. Rocha, M. Ruta (2016), Food prices and the multiplier effect of trade policy, Journal of International Economics, Volume 101, Pages 102-122.

Gopinath, G., P.-O. Gourinchas, A. F. Presbitero, and Petia Topalova (2025), “Changing global linkages: A new Cold War?,” Journal of International Economics, 153, 104042.

Grossman, G. M., and Helpman, E. (1994), "Protection for Sale." The American Economic Review, 84(4), 833-850

GTA (2018), Working with a growing data set, Technical note on the implications for proper reporting lag adjustment, Global Trade Alert, S. Evenett and J. Fritz, December 2018.

GTA (2022), The GTA handbook Data and methodology used by the Global Trade Alert initiative, 26 October 2022. Viewed at: https://gtaupload.s3.eu-west-1.amazonaws.com/Uploads/web/GTA+handbook.pdf [Last accessed on 26 March 2025.]

Ghysels, E., and Qian, H. (2019), Estimating MIDAS regressions via OLS with polynomial parameter profiling. Econometrics and Statistics, 9, 1-16.

Handley, K. and N. Limão (2017), "Policy Uncertainty, Trade, and Welfare: Theory and Evidence for China and the United States," American Economic Review, September 2017, 107 (9), 2731–83

IMF (2025), World Economic Outlook: A Critical Juncture amid Policy Shifts, International Monetary Fund (IMF), April 2025, Washington DC.

IMF (2024), World Economic Outlook (WEO) database, International Monetary Fund (IMF)

IMF (2023), Review of the Role of Trade in the Work of the Fund, International Monetary Fund (IMF), April 2023, Washington DC.

IMF, OECD, World Bank and WTO (2022), Subsidies, Trade, and International Cooperation.

Looi Kee, H., Nicita, A., and Olarreaga, M. (2009), Estimating trade restrictiveness indices. The Economic Journal, 119(534), 172-199.

Kwiatkowski, D., Phillips, P.C.B., Schmidt, P., and Shin, Y. (1992), Testing the null hypothesis of stationarity against the alternative of a unit root: How sure are we that economic time series have a unit root? Journal of Econometrics, 54(1), 159-178.

Li, Q., and J. S. Racine (2007), Nonparametric Econometrics: Theory and Practice. Princeton University Press.


OECD (2021), Jaax, A., González, J., and Mourougane, A. (2021). Nowcasting aggregate services trade. OECD Trade Policy Papers, No. 248. OECD Publishing, Paris. https://doi.org/10.1787/442ba8f8-en


Pedersen, P., and Diakantoni, A. (2020), Lessons learned and challenges ahead for the WTO trade monitoring exercise, pages 7-20.

Miranda-Pinto, J., A. Pescatori, M. Stuermer, and X. Wang (2024), Beyond Energy: Inflationary Effects of Metals Price Shocks in Production Networks, International Monetary Fund (IMF), Working Paper WP/24/215, Washington DC.

Stock, J. H., & Watson, M. W. (2002), "Forecasting Using Principal Components from a Large Number of Predictors." Journal of the American Statistical Association, 97(460), 1167–1179. Tibshirani, Ryan J. 2014. "Adaptive piecewise polynomial estimation via trend filtering." The Annals of Statistics 42(1): 285–323.

U.S. Census Bureau (2019), "X-13ARIMA-SEATS: Seasonal Adjustment Software."

UNCTAD (2019), International classification of non-tariff measures (UN).

WTO (2013), Agreement on Trade Facilitation Ministerial Decision of 7 December 2013, World Trade Organization (WTO), www.wto.org/english/thewto\_e/minist\_e/mc9\_e/desci36\_e.htm

WTO (2025), Global Trade Outlook and Statistics, World Trade Organization, Geneva, April 2025.

## ANNEX 1 Further Data Description

In the aftermath of the global financial crisis, two new trade policy monitoring initiatives were introduced to help better monitor and document new trade policy measures undertaken worldwide. $^{49}$ As such, the WTO Trade Monitoring Database (TMDB), created in October 2008, has been tracking measures implemented by WTO Members and Observers through the formal WTO channels. $^{50}$ The Global Trade Alert (GTA), created in 2009, developed by the University of St. Gallen, compiles announced and implemented measures from a variety of publicly available sources.

They are described in more detail below:

The TMDB, within its established mandate, offers detailed insights into trade policies and measures implemented at the national level. The TMDB as the repository of the WTO trade monitoring exercise, tracks trade policies and measures implemented during a predefined period, i.e., over the 12 months leading up to mid-October, and releases them on a biannual basis. The TMDB contains only implemented measures that are either officially communicated or notified by Members to the WTO, or identified by the WTO Secretariat from public sources, such as government websites, other international organizations' websites or press releases. $^{51}$ The database also includes information on the products affected, and the trading partners targeted as stipulated in the corresponding laws, regulations, or executive orders implemented by governments. TMDB trade measures are verified by WTO Members in terms of coverage, dates and content. $^{52}$ This verification ensures the accuracy and reliability of trade measures. At the same time, the verification process might become a constraint when Members interpret their commitment to transparency selectively or attempt to limit the ability of the WTO Secretariat to report on trade measures (Pedersen & Diakantoni, 2020).

GTA captures real-time information on trade-related policies and measures, including those that have been announced or implemented at the national and sub-national level, or even targeting specific firms. The coverage of trade measures covered by GTA is also broader, encompassing a wider range of trade-related areas. Additionally, GTA often takes a broader/less detailed perspective regarding some of the practical implications related to such policies, such as the definition of products covered, and the trading partners affected. The latter sometimes go beyond those stipulated in the relevant law to include those potentially affected. GTA also tends to overcount trade measures by documenting every revision or modification of trade interventions. In addition, GTA does not adhere to a predefined reporting period. It actively seeks and includes information on trade measures that are discovered at a given time but may have already occurred in the past, ensuring constant updates.

The databases differ notably in four dimensions. First, GTA encompasses a broader scope of trade policy measures, including firm-specific interventions and subnational policies, while TMDB focuses on national measures with economy-wide effects. Second, TMDB relies predominantly on official government sources with extensive verification processes, whereas GTA incorporates unofficial news outlets, trading verification depth for breadth. Third, TMDB exclusively records implemented measures, while GTA includes policy announcements, potentially providing early signals of future trade actions. Fourth, TMDB updates biannually whereas GTA provides continuous updates as measures are discovered, providing more frequent information but also requiring additional data treatment to account for different discovery rates, depending on the time elapsed since the original measure announcement. These complementary approaches—TMDB prioritizing accuracy of implemented traditional trade measures and GTA offering broader coverage with near-real-time updates—capture different yet supplementary dimensions of global trade policy developments.

Table A1.1 below provides an overview of the type of trade-policy measures covered in each database and Table A1.2 lists countries for which information is available by data source. Table A1.3 lists the time-series variables constructed from the raw data that are used in the dynamic factor model. Figure A1.1 shows the evolution in each individual time series and the extracted trends.

Table A1.1 List of Trade-Policy Measures by Data Source


Note: Table A1.1 lists the types of measures covered in each database using UNCTAD MAST classification (UNCTAD, 2019). "GTA" refers to the Global Trade Alert, "TMDB" refers to the WTO Trade Monitoring Database and "Baseline" indicates, which measures have been included in our baseline estimate of the global factor presented in this paper. \*Anti-subsidy measures in the GTA terminology corresponds to countervailing duties in the WTO terminology.

Table A1.2 Time-Series Variables in the Dynamic Factor Model


Note: The table lists the time-series variables used in the baseline specification, outlining differences in the unit, measure type and source of data. Measures are labelled as "Facilitating measures" if they are labeled as "facilitating" in the TMDB database and "green" in the GTA database, respectively, and as "Other measures", otherwise.

## Figure A1.1 Time Series Evolution and Extracted Trends of Model Variables

TMDB, number of facilitating measures

[[KC_IMAGE_006]]

GTA, number of facilitating measures

TMDB, number of other measures
GTA, number of other measures

GTA number of products affected by facilitating measures


GTA number of products affected by other measures

TMDB number of products affected by facilitating measures

TMDB number of products affected by other measures

[[KC_IMAGE_007]]

Note: GTA refers to the Global Trade Alert database, TMDB refers to the WTO Trade Monitoring database. Facilitating measures refer to measures that reduce restrictiveness, discrimination, or other distortions or otherwise ease trade (e.g., through more efficient border procedures). Other measures include measures that restrict or otherwise distort trade and other measures.

Table A1.3 End-of-Period Adjustment Rates for Incomplete Discovery Periods


Note: Adjustment rates are based on the average historical ratio of measures announced in each calendar month (across all years in the sample) that are discovered and recorded in the GTA data within the 12-month reporting period after the time elapsed as of June 2025. These adjustment rates are applied to the observed number of measures for each calendar month to account for potential future discovery and provide a more accurate representation of the likely trends in the latest period.

Figure A1.2 Time Series Evolution and Extracted Trends of Model Variables

[[KC_IMAGE_008]]

Note: The figure shows the estimated global factor with the end-of-period adjustment applied to the number of measures in the latest periods with incomplete discovery rates (see Table A1.3 in the Annex 1), depicted in the black line, and without the adjustment (green dashed line) to illustrate the effect of the adjustment. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

## ANNEX 2 Further Tables and Figures

Figure A2.1 Comparison of Filtered and Unfiltered Global Factor

[[KC_IMAGE_009]]

Note: "Global Factor Unfiltered" refers to the estimated factor from the baseline dynamic factor model regression. "Global Factor Filtered" refers to the estimated factor smoothed using a three-month moving average, which is used throughout the paper for clearer presentation of underlying trends. The factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.2 Estimated Global Factor and Confidence Intervals

[[KC_IMAGE_010]]

Note: The black line represents the estimated common factor from the dynamic factor model, with 90% pointwise confidence intervals constructed using bootstrap resampling methods shown as shaded regions. The bootstrap approach is a residual-based bootstrap. We generate B = 999 bootstrap samples from the estimated trend and factor, plus a bootstrap residual which is obtained by resampling from the (known) distribution of the error term in equation (3). The trend and factor estimations are then repeated on each one of the bootstrap samples, and the confidence intervals obtained using the 2.5 and 97.5 percentile at each sample point. The factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.3 Alternative Estimation

[[KC_IMAGE_011]]

Note: "Global Factor w/ blocks" refers to our baseline result with one global factor and two local factors for Facilitating and Other measures, respectively. "Global Factor w/o blocks" refers to the global factor estimated when the loadings for the local factors are set to equal zero. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.4 Alternative Approaches to Trend Extraction

[[KC_IMAGE_012]]

Note: "Local Quadratic all (baseline)" refers to our baseline result obtained using a weighted quadratic regression; "Local quadratic 1/3" refers to a result obtained from a weighted quadratic regression in which only the weights for the $33\%$ closest observations are positive, while the others are set to be equal to 0; "Quadratic" refers to a result obtained from a quadratic least-squares regression; and "Trend filter" refers to a result obtained from a fully data-driven nonparametric procedure, implemented following Tibshirani (2014). Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.5 Alternative Sample of Measures
Panel A. With Number of Implementing Countries

[[KC_IMAGE_013]]


Panel B. Number of Measures Only

[[KC_IMAGE_014]]

Note: Our baseline result is depicted by the grey line. The green line in Panel A shows the results of the estimation that, besides the input indicators used in the baseline, additionally uses input indicator on the number of countries implementing the measures for each type and by source (i.e., facilitating measures from GTA, facilitating measures from TMDB, other measures from GTA, other measures from TMDB). In Panel B the green and yellow lines correspond to an alternative estimation considering input indicators on the number of measures by type and source only (excluding the input indicators relating to the number of affected products) whereby "Global Factor w/blocks" refers to the result using the baseline estimation with one global factor and two local factors for Facilitating and Other measures respectively and "One Global Factor" refers to an alternative estimation with one global factor only. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.6 Alternative Approach to Different Types of Measures
Panel A. Trade-Policy Related Measures by Type

[[KC_IMAGE_015]]


Panel B. All Measures by Type

[[KC_IMAGE_016]]

Note: Our baseline result is depicted by the grey line. The figure reports results when only the global factor is estimated (without additional local factors) on the sample of measures of one type only, i.e., facilitating (blue line) or other (red line). Panel A shows the results of the global factor for "Facilitating measures" and "Other measures" among the trade-policy measures considered in the baseline, respectively. Panel B shows the results of the global factor for "Facilitating measures" and "Other measures", including all measures recorded in the GTA (i.e., additionally including MAST chapters CAP, F, FDI, G, MIG in UNCTAD (2019) classification), as well as unknown policy instruments. For further information on the different measures, see Table A1.1 in the Annex. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.7 Alternative Time Periods

[[KC_IMAGE_017]]

Note: Our baseline result is depicted by the grey line and covers the period starting in January 2010 and ending in May 2025. The yellow and green lines show the results of the estimation using the same start date and alternative cut-off periods, i.e., October 2020 (yellow line) and October 2022 (green line), respectively. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Figure A2.8 Alternative Approach to Accounting for Economic Size

[[KC_IMAGE_018]]


Figure A2.9 Testing the Influence of End-of-Period Adjustment on the Global Factor

[[KC_IMAGE_019]]

Note: Our baseline result is depicted by the black line. The green dashed line presents the results of the estimation using factor loadings derived from the regression through October 2024, prior to the application of any end-of-period adjustment. Each factor is normalized relative to the January 2010-December 2011 reference period (baseline = 0).

Table A3.1 Time-Series Predictors in the MIDAS Model


Note: The table lists the time-series predictors used in the nowcasting model. All raw data are used from January 2010 to June 2025. All the keywords from Google Trends data listed above are \`topics' – besides "free trade", "free trade agreements", "customs regulations", "trade protectionism", "subsidies", and "trade agreements" – for which the platform reports the relative number of searches for that concept and all associated terms across different languages and expressions (rather than exact keyword matches in the search language).

## Google Trend Data

This study uses Google Trends data to capture the weekly search intensity for a predefined set of keywords, covering the period from January, 2010, to June 2025. The data are downloaded directly from the Google Trends platform (https://trends.google.com/trends) at a weekly frequency.

When a keyword is entered as a topic (e.g., "Tariff"), the platform reports the relative number of searches for that concept, including all associated terms across different languages and expressions, rather than exact keyword matches in the search language. This ensures that conceptually related queries — such as "tariff policy," "tariff pause," or searches in non-English languages — are captured under a unified measure. In this sense, searching by topic effectively consolidates a wide range of related keyword searches into a single measure.

The values reported by Google Trends are normalized on a scale from 0 to 100, where 100 represents the peak popularity of a term within the selected time and region. As a result, these figures do not reflect absolute search volumes but rather relative keyword popularity at a particular time. Given that our goal is to use these time series to nowcast constructed indicators, after downloading the data for the keywords, we normalize them through a within-series scaling. Specifically, following the approach in Choi and Varian (2012), we compute growth rates of the normalized Google Trends index to emphasize short-term fluctuations and enhance comparability across predictors. In the future, further checks could be undertaken to ensure that the inherent characteristics of the Google Trends data are adequately handled for purposes of prediction, buildings on the recommendations from the literature (e.g., Cebrián and Domenech, 2024).

Table A4.1 Nowcast RMSE by Single High-Frequency Predictor


Note: Each root mean squared error (RMSE) value is obtained from a nowcasting model that includes only one high-frequency predictor at a time. The RMSE values are reported on a 0–100 scale for comparability. For each predictor, we estimate a restricted ADL-MIDAS model using the corresponding column from the predictor matrix, with the autoregressive component fixed at AR(1). The RMSE is computed based on out-of-sample predictions. This table facilitates relative performance comparison across predictors, where lower values indicate better nowcasting accuracy.

## Figure A4.1 Nowcasting Stationary Component of TPA


[[KC_IMAGE_020]]

Note: The nowcasting result plotted in Figure A4.1 corresponds to the nowcasted stationary target with leads in Equation 2 with h = 1. From April 2019 to May 2025, the nowcasted values are shown as a red dashed line with dots (referred to as one-step predictions). The green dotted line (referred to as AR(1) predictions) represents a simple AR(1) forecast used for comparison.

Table A4.2 Nowcast RMSE by Number of Predictors (K)


Note: The RMSE values are computed from out-of-sample forecasts using a rolling-window ADL-MIDAS regression. For each specification, we include K high-frequency predictors and all other low frequency predictors. The RMSE is calculated over the same evaluation period to ensure comparability across different values of K. We observe that ADL-MIDAS with less than 10 best-performing predictors have a better performance compared with AR(1) which has absolute RMSE at 27.07.
