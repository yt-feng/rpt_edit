# Beyond the First Bond: Market Access and Debt Dynamics in Frontier Economies

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026


WP/26/153

# IMF Working Paper Africa Department

# Beyond the First Bond: Market Access and Debt Dynamics in Frontier Economies

Prepared by Hasan Cetin, Sanan Mirzayev

Authorized for distribution by Edward Gemayel

July 2026

# IMF Working Papers describe research in progress by the author(s) and are published to elicit

author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: We examine market entry and post-entry debt dynamics in Frontier Economies by grouping countries based on the durability of market access using a two-step framework combining first Eurobond issuance with reliance on private external creditors, validated through unsupervised K-means clustering. A discrete-time event LOGIT model finds that favorable global liquidity conditions and investor appetite open issuance windows for countries, but domestic pull factors – income, institutions, growth, and reserve buffers – ultimately determine the success of market entry. Post-entry, Frontier Economies shift rapidly toward market borrowing, with a looser fiscal stance as a new financing source is unlocked. Alongside increased exposure to rollover and global financial cycle risks, a debt decomposition exercise shows a worsening interest–growth differential and rising debt, driven mainly by primary deficits and higher interest burdens. Results underscore the need for credible medium-term fiscal frameworks, stronger debt management, and reserve buffers to manage the transition to market financing.

RECOMMENDED CITATION: Cetin, H., and Mirzayev, S., 2026 “Beyond the First Bond: Market Access and Debt Dynamics in Frontier Economies”, IMF WP/26/153. International Monetary Fund, Washington, D.C

JEL Classification Numbers:

F34, G12, H63, O11

Keywords:

Market Access; Frontier Economies; Debt Dynamics; Debt

Sustainability; Debt Sustainability Framework

Author's E-Mail Address:


# Beyond the First Bond: Market access and Debt Dynamics in Frontier Economies

Prepare by Hasan Cetin and Sanan Mirzayev $^{1}$

## Contents

Introduction ....6
Figure 1: Eurobond Issuances by EMDEs, 2005–23....7

Defining Criteria for Market Access ....8
Step 1: Defining Sustained Market Access Windows....9
Table 1: Tale of Two Countries....11
Table 2: Private External Disbursements Before and After Market Entry....11
Step 2: Identifying Frontier Economies in the Market Access Group....12
Figure 2: Matching Rate for Cutoff Lengths....13
Table 3: Country Classification....13

Stylized Facts ....14
Table 4: Correlation: Per capita Real GDP and Share of Private External Debt....14
Governance and Sequenced Market Entry....14
External Financing Mix....15
Figure 3: Governance, Market Access, Evolution of External Financing in EMDEs....15
Public Debt....16
Figure 4: Decomposition of Public Debt in EMDEs....17

Gateway to Markets: Determinants of Entry....17
Table 5: Determinants of First Market Entry....20
Figure 5: Evolution of Predicted Probability for Market Entry....21

Post-Entry Debt Accumulation ....22
Figure 6: Debt Dynamics in Frontier Economies after Market Entrance....24
Figure 7: Growth Performance before and after Market Entry....25

Conclusion....26

References ....28

Annex I. Data ....31

Annex II. Regression Results....37

Annex III. Expanded Stylized Facts ....39
Figure A.1: Governance, Market Access, Evolution of External Financing in EMDEs – Simple Averages ....39
Figure A.2: Decomposition of Public Debt in EMDEs – Simple Averages....39
Figure A.3: Spreads and Maturities before and after Market Entry....40

## Glossary


## Introduction

The ability to reliably access international capital markets to finance development needs and navigate external shocks has been a defining feature in differentiating among Emerging Markets and Developing Economies (EMDEs). $^{1}$ On the one end of the spectrum is the group of Emerging Markets that has relatively durable access to international credit markets, allowing them greater policy flexibility in financing their needs and managing macroeconomic volatility. On the other end are the low-income countries (LICs) that are effectively cut off from those markets, relying almost exclusively on limited official and multilateral external financing. In between these two groups there is a set of countries – generally referred to as Frontier Economies – that have tapped the international bond markets relatively recently, but whose access remains precarious, particularly when global financial conditions tighten.

Through the decade following the Global Financial Crisis (GFC), amid low global interest rates and the search for yield, a number of Frontier Economies successfully tapped into international bond markets for the first time. The COVID-19 pandemic and the subsequent sharp global monetary tightening served as a stress test, exposing structural deficiencies and market's waning confidence in their ability to weather these shocks. As many of these countries were completely cut off from international capital markets, the discussion around maintaining market access during global downturns has once again come to the fore.

Starting in 2022, sharp global capital reallocation triggered by post-pandemic monetary tightening cycles in advanced economies overlapped with sizeable external debt repayment obligations coming due in Frontier Economies, resulting in widening sovereign spreads. In certain cases, spreads increased to distressed levels, practically shutting some of these economies out of international bond markets. Sovereign issuances among Frontier Economies, particularly those in the lower-income group, declined sharply from their peak in 2021 (Figure 1), with only one Eurobond issuance in 2022–23. $^{2}$ Several sovereigns defaulted on their external obligations and resorted to debt restructuring, while acute financing needs forced others to turn to the International Monetary Fund (IMF) for emergency funding.

Against this background, we examine market access and debt dynamics in Frontier Economies. The analysis proceeds in three steps. First, we differentiate countries into non-market access to market access, proceeding to bifurcate the latter into recurrent market access countries and Frontier Economies. Through an iterative process and unsupervised K-means clustering technique we define a criterion for Frontier Economies, subject it to robustness checks, and demonstrate that the market entry year is structurally meaningful. We then provide stylized facts on key economic features and debt portfolios across these distinct country groups. Second, we estimate a discrete-time event LOGIT model to identify the macroeconomic fundamentals and global conditions associated with market entry. Third, we analyze whether market entry instills discipline or facilitates debt build-up as governments in Frontier Economies gain access to a new source of financing that was previously unavailable to them. Finally, we examine whether there are marked differences between Frontier Economies that use the IMF's Debt Sustainability Framework for Market Access Countries (MAC-Frontiers) and those that use the framework for LICs (LIC-Frontiers).

Figure 1: Eurobond Issuances by EMDEs, 2005–23 (number of issuances per year)

[[KC_IMAGE_001]]

Source: World Bank IDS and author's calculations
Note: Eurobond issuances in Frontier Economies peaked in 2021, declining sharply over the next two years as global financial conditions tightened. Despite upcoming external debt maturities, nearly no low-income frontier Economy managed to issue a Eurobond in 2022-23. The data underpinning the charts excludes issuances below US\$250 million

We find that while conducive global liquidity conditions catalyze market entry, domestic economic fundamentals and institutional quality ultimately determine whether a non-market access country can successfully utilize the window of opportunity. A comparison of pre- and post-entry policy behavior in Frontier Economies reveals that countries tend to restrain borrowing in the run up to market entry, while a looser fiscal stance tends to set in afterwards as new financing source softens spending constraints. Debt drivers in the aftermath of market entry exhibit a similar pattern for MAC-Frontiers and LIC-Frontiers, as the negative interest-growth differential narrows and weakens debt dynamics. We further find that access to international bond markets does not necessarily translate into meaningful improvements in growth dynamics relative to the rest of the world.

The paper contributes to three interrelated strands of the literature on sovereign market access in developing countries. In the market access literature, the classification of countries along the access spectrum has relied on both price-based and quantity-based approaches. Price-based measures use sovereign spreads or yields to infer constraints to market access, suggesting that as borrowing rates increase, particularly through rapid widening of spreads, bond issuances decline and access is eventually lost when rates reach a point beyond which borrowers cannot afford to borrow or lenders unwilling to lend (Guscina et.al., 2017). Quantity-based measures focus on actual issuance volumes and frequencies (Gelos et.al., 2004). $^{3}$ This paper departs from existing approaches by defining market access through the durability of market access and compositional shifts in external debt portfolios rather than through a static issuance criterion, spread threshold, or composite financial index, and validates the resulting taxonomy using unsupervised clustering. On determinants of market entry, this paper contributes by modeling entry as a discrete-time event, which directly estimates the probability of first market entry conditional on not having entered yet, thereby capturing the sequential nature of transition from non-market access to Frontier status. Finally, on post-entry debt dynamics, the paper contributes by providing a systematic comparison of pre- and post-entry debt dynamics across subgroups of Frontier Economies (LIC-Frontiers and MAC-Frontiers), using a standard debt decomposition framework to trace the evolution of specific channels through which debt accumulates.

## Defining Criteria for Market Access

We borrow the theological purgatory concept in setting the framework to identify Frontier Economies. Accordingly, market access EMDEs are classified into those in heaven and those in the transitional purgatory state waiting for the final destination. Those in heaven classification are defined as Recurrent Market Access Countries (RMACs) that have built a deep and institutionalized integration with international bond markets over decades, borrowing with relative ease. The ones in the purgatory transition state are defined as Frontier Economies that have left behind the state of near-complete reliance on official and multilateral financing and entered the international bond markets. However, their presence in the markets is relatively recent and nascent, particularly during episodes of global financial tightening.

In this paper, the framework defines Frontier Economies specifically through the lens of durability of market access. It follows that true market access is not just tapping international markets but establishing a recurrent and resilient presence in them, including at times of global downturns – i.e. reaching the heaven.

This conceptual framework is operationalized in a sequenced two-step methodology. First, a criterion developed to define sustained market access windows, with the aim to group countries into market access and non-market access categories. Second, countries that are considered to meet the criterion divided into two groups based on the longevity of the access: RMACs and Frontier Economies. The second step helps distinguish countries in purgatory state with nascent market access from those in heaven that have reached recurrent state and enjoy high and reliable private creditor participation. An unsupervised K-means clustering technique is employed to ensure that the durability-based distinction is empirically and economically meaningful and well aligned with structural, macroeconomic, and financial indicators.

## Step 1: Defining Sustained Market Access Windows

The proposed framework in this paper is grounded on continued reliance on private external financing. In this regard, it employs a form of quantity-based measure but adds a dimension on evolution of overall external debt portfolio over time to specifically capture relative reliance on private external borrowing in country's financing mix. In this approach, access to markets or a loss of market access for a given EMDE should meaningfully alter the composition of debt portfolio and financing patterns. Hence, the market access is conditioned on both entering the market by at least one Eurobond issuance but also maintaining the share of private external financing in total debt inflows. In essence this is similar to the IMF Poverty Reduction and Growth Trust (PRGT) market access graduation criterion, which requires countries to demonstrate “durable and substantial” access. $^{4}$

The methodology takes the first Eurobond issuance as the market entry point and then tracks the share of private external credit in total external public borrowing to establish sustained market access window. Defining sustained access windows separates countries who regularly re-access private external creditors from those that have not yet established market entry and those who tapped the markets at some point but failed to maintain sustained access. The identification process is designed to capture economic essence of structural change in financing sources and patterns. The algorithmic process is defined as follows:

1. Identify the first year of Eurobond issuance to establish market entry

2. Use the share of private external public debt in that year as the base value (private\_share $_{base}$ )

3. Search forward through subsequent years $(t+1, t+2, \ldots)$ to evaluate whether following condition holds – where the private share in one year after base year is greater than half of the private share in base year $^{5}$ :

$$
\text { private\_share } _ {t + 1} \geq \frac {1}{2} \text { private\_share } _ {\text { base }}
$$

4. If the condition holds, update the base year by taking the maximum of the current base and the new value for the private share, and repeat with the next value:

$$
\text { private\_share } _ {\text { new   base }} = \max \left\{\text { private\_share } _ {\text { current   base }}, \text { private\_share } _ {t} \right\}
$$

5. If the condition holds for a minimum of five consecutive years, define this as a sustained market access window for this country

6. Repeat the processes 1 to 5 iteratively for all countries in the sample from 1980 to 2024 to capture all potential access windows

7. Discard the windows if there is no new private credit disbursement within the window or if the share of private debt is in a consistent decline relative to the preceding year in the window

8. Finally, classify the countries based on their latest sustained market access window: if a country's most recent window is ending in 2021 or later the country is considered as market access. $^{6}$

The example of two real world EMDE cases help demonstrate the methodology clearly (Table 1). Country A issued its first Eurobond in 2011, when the share of private debt increased to 8 percent of its total external public debt stock. Over the next twelve years, Country A continued to issue Eurobonds and borrow from other private non-bonded external creditors, increasing the share consistently and peaking at 45 percent in 2023. As the share of external private debt has not halved at any point from its peak or declined consistently over the years, the country is considered to meet the market access criterion. In contrast, Country B is classified as non-market access because it fails to meet these conditions. Although it entered the market with a Eurobond issuance in 2018, the share of external private debt more than halved from peak of 30 percent and declined consistently in each subsequent year.

To confirm that market entry is indeed a meaningful marker for differentiating between market access and non-market access countries, we test whether countries experience an observable and significant structural shift in external borrowing patterns toward international private creditors after entering the market. In other words, we would expect a marked shift from official to private external borrowing. To test this hypothesis, we compare the five-year average of private external disbursements in market access countries before (t-5 to t-1) and after (t+1 to t+5) the entry year. $^{7,8}$

Table 1: Tale of Two Countries Country A


Country B

We find a significant increase in the share of private creditor disbursements in new borrowing across both RMACs and Frontier Economies following the entry year, with post-access averages exceeding pre-access levels by 18-20 percentage points (Table 2). This shift is particularly pronounced among Frontier Economies, where the median growth rate in the share of private disbursements exceeds 200 percent, reflecting a sharp reorientation toward private financing after market entry. RMACs exhibit relatively moderate, though still substantial increases, consistent with their higher baseline exposure to private capital markets. Overall, the findings indicate that the entry year captures a structural transition in sovereign borrowing behavior rather than a transitory or cyclical fluctuation, lending strong support to the empirical relevance of the defined criterion.

Table 2: Private External Disbursements Before and After Market Entry


Applied to the sample of 92 EMDEs, the methodology above identifies 36 non-market access (NMACs) and 56 market access countries. $^{9,10}$ The latter are then divided into two groups: RMACs and Frontier Economies. This distinction separates countries in the transitional purgatory state, characterized by nascent market access, from those in heaven, which have achieved recurrent and relatively reliable access to international capital markets.

## Step 2: Identifying Frontier Economies in the Market Access Group

Following an iterative process and unsupervised K-means clustering exercise, the paper specifies 20 years as the meaningful cutoff for differentiating countries in heaven from those in the transitional purgatory state. To validate the empirical significance and structural integrity of the classifications, we apply fundamental-based K-means clustering technique to all 92 countries. The unsupervised technique determines whether countries cluster naturally into groups based on a set of macroeconomic and financial indicators. By grouping countries into distinct macroeconomic profiles without a prior classification bias and solely based on readily available data, the exercise helps validate that the 20-year threshold is supported by structural, data-driven clustering.

First, country-level averages of six core macroeconomic and institutional variables are computed over 1996–2024. $^{[11]}$ These averages are standardized, projected via principal component analysis (retaining enough components to capture over 80% of the variance), and clustered into three groups using K-means; the resulting clusters – interpreted as RMACs, Frontier Economies, and NMACs – are held fixed throughout the analysis. To ensure that the algorithmic clustering is not distorted by choice of specific variables, we expand the clustering exercise to cover over 20 macroeconomic variables (see Annex I for details). The resulting cluster assignments are consistent with the baseline. We then vary the threshold T, which defines sustained market access based on the first year of continuous bond market participation since 1980, and reclassify countries into RMACs, Frontier Economies, and NMACs for each value of T.

For each threshold, we compute the maximum alignment (matching rate) between this market-access classification and the fixed fundamentals-based clusters using the Hungarian algorithm. We then compare the matching rate across candidate threshold years. The year that produces the highest matching rate is the one most closely aligned with the machine-determined grouping. We find that the alignment between market-access definitions and fundamentals increases with the required length of sustained market access and reaches a clear plateau at around 19–23 years (Figure 2). For shorter access windows, countries are frequently indistinguishable in terms of fundamentals, while

Figure 2: Matching Rate for Cutoff Lengths

[[KC_IMAGE_002]]

Source: WEO, World Bank IDS, WDI and WGI Databases

extending the access requirement beyond two decades yields little additional improvement in classification accuracy. We therefore adopt 20 years of sustained market access as the reasonable cutoff separating RMACs from Frontier Economies, as this duration is where're market access most consistently aligns with underlying macroeconomic and institutional fundamentals.

Further, for analytical purposes, we divide Frontier Economies into two subgroups depending on whether they use the LIC-DSF or the MAC-SRDSF, defined as LIC-Frontiers and MAC-Frontiers, respectively. The resulting country classifications are summarized in Table 3 below.

Table 3: Country Classification


## Stylized Facts

The stylized facts document the distinct profiles of the four country groups, along with the sequencing of market entry and the evolution of external financing. To ensure that analytical indicators provide representative averages of each group, we use latest available real GDP per capita as the weighting factor. The rationale for the choice is that GDP per capita is highly correlated with the private share of external public debt, which is used in this paper as a proxy for market access. $^{12}$ Weighing the countries by income levels provides measures that better reflect differences in market access status across groups (Table 4). $^{13}$ For completeness, we also report stylized facts using simple averages, with no meaningful impact on results, as shown in Annex III.

## Table 4: Correlation: Per capita Real GDP and Share of Private External Debt


## Governance and Sequenced Market Entry

It is well established that investors attach significant weight to economic governance and institutional quality when assessing country's creditworthiness (Abate et al., 2021; Presbitero et al., 2015). Prior extensive research from the IMF suggests that strong policy frameworks and perceived institutional quality are key factors in a country's ability to tap international capital markets and maintain creditor confidence. $^{14}$ We choose the composite of World Bank's Worldwide Governance Indicators (WGI) as a proxy variable to capture governance quality.

Across country groups, a clear hierarchy can be observed in terms of weighted WGI averages (Figure 3, left chart). RMACs maintain the highest governance scores throughout the period, with relatively limited variation over time. In contrast, both MAC-Frontiers and LIC-Frontiers experience gradual and sustained improvements in governance, narrowing the gap with RMACs. Importantly, these improvements preceded market entry by several years, suggesting that strengthening governance is a prior condition rather than a contemporaneous outcome of market entry. Finally, in contrast to market access country groups, the NMAC group maintains low and stagnant WGI averages with no systematic improvement over the period, suggesting weak institutional quality remains a barrier to market entry.

Market entry seems to follow a clear sequence, with RMACs largely establishing access prior to 2000. MAC-Frontiers started entering market shortly before the GFC, while the majority of LIC-Frontiers start tapping markets with a lag of a few years, in early 2010s. All Frontier Economies in the sample issued at least one Eurobond by 2019 (Figure 3, center chart).

## External Financing Mix

First, the chart suggests that there is an observed hierarchy among country groupings in terms of the share of private external financing (Figure 3, right chart). RMACs consistently rank at the top, with a higher share of private external debt, followed by MAC-Frontiers and LIC-Frontiers. NMACs remain at the bottom, with low and stagnant share of private financing, reflecting their near-complete reliance on concessional external financing.

Second, market entry in Frontier Economies is accompanied by a marked reallocation of external debt toward private creditors. The relatively stagnant share of private external debt from the 1990s to the late 2000s in MAC-Frontiers and LIC-Frontiers starts to increase rapidly thereafter, peaking around the COVID-19 pandemic and pointing to a structural shift in external financing. RMACs also experienced an acceleration in the share of private financing around the same period, suggesting favorable global monetary conditions and elevated investor risk appetite for EMDEs. The parallel rise suggests that global “search-for-yield” forces amplified the effects of improved domestic fundamentals, allowing Frontier Economies to shift toward private external financing once market access was established.

Figure 3: Governance, Market Access, Evolution of External Financing in EMDEs

[[KC_IMAGE_003]]

Source: WEO and IDS databases and authors' calculations

## Public Debt

U-shaped Trajectory: Evolution of public debt across all country groups between 2000 and 2024 broadly in sync suggests global financial and commodity cycles were key drivers (Figure 4, solid blue line). After declining in the early 2000s, debt ratios rise markedly from the late 2000s onward, with the increase most pronounced for LIC-Frontiers. $^{15}$ NMACs and LIC-Frontiers had similar debt levels in the early 2010s, but the latter accumulated significantly higher debt over the decade, with the debt-to-GDP ratio almost doubled, suggesting the ability to tap international bond markets allows for more aggressive borrowing. Debt levels increased in all other country groups, albeit at moderate rates.

Domestic Debt: First, domestic debt is the most significant differentiator for RMACs, with local currency debt accounting for roughly 60 percent of total public debt on average, a share substantially higher than in the other groups (Figure 4, gradient blue bars). The share of domestic debt in RMACs has remained broadly stable over the last two decades, possibly indicating a ceiling for domestic-currency borrowing in EMDEs. Second, although at lower levels relative to RMACs, the role of domestic-currency financing has increased steadily over the decades for all other country groups. $^{16}$

Bondholder Flip: Market access is associated with a clear shift in creditor composition (Figure 4, orange and red bars). First, the share of private external debt has increased in Frontier Economies after market entry. Multilateral lending shares remain broadly flat over time, though persistently higher for LIC groups, while bilateral lending declines steadily across all country groups. Second, market access leads to a shift toward bonds as the dominant channel of private external borrowing. Whereas non-bonded private lending (orange bars) was the dominant form of financing prior to market entry, bond issuance (red bars) takes over thereafter, reflecting in part countries' preference for marketable instruments.

Figure 4: Decomposition of Public Debt in EMDEs

[[KC_IMAGE_004]]


[[KC_IMAGE_005]]


[[KC_IMAGE_006]]

Source: WEO and IDS databases and authors' calculations


[[KC_IMAGE_007]]


## Gateway to Markets: Determinants of Entry

The analysis in this section starts with an economic prior that transition to market access for Frontier Economies is driven by combination of domestic economic fundamentals and global financial conditions. To this end we conduct a LOGIT regression analysis, specified as discrete-time event history model, to estimate the probability of market entry for each country year given specific macroeconomic and global triggers. For Frontier Economies, the observation period starts from 1996 – the first year of available WGI data – and continues until the country enters the market. $^{17}$ For NMACs, the observations cover the 1996–2024 period.

For the model to remain unbiased, all countries in the sample should be at risk of market entry. While Frontier Economies in the sample were inherently at risk because they eventually entered the market, certain omitted variables, such as conflict, might prevent some of NMACs from being at risk of market entry regardless of their macroeconomic fundamentals or global financial conditions. Keeping these NMACs in the sample would bias the coefficients, as the model would effectively attribute their non-entry macroeconomic variables even though the failure to enter the market was due to other non-economic variables that are not captured. To eliminate this bias, the sample excludes only the NMACs that are labeled as conflict-affected states in the World Bank's 2020 Fragile and Conflict Affected States (FCS) list. For completeness, Annex II presents regression tables that include all sample countries, with results remaining robust.

All continuous variables are winsorized and standardized to reduce the influence of outliers and allow for direct comparison of coefficients. The specific lag structure of the logit regression is designed to capture the immediate impact of the global shocks (push factors) while recognizing the momentum of macroeconomic variables (pull factors):

\- Country-specific macroeconomic variables enter regressions as 3-year rolling averages (t-1, t-2, t-3) to capture sustained economic performance. $^{18}$ The variables include macroeconomic fundamentals (inflation, real GDP per capita, real GDP growth), institutional quality (WGI average), indebtedness (debt/GDP ratio), and external buffers (reserves coverage of imports).

\- Global variables enter the regressions contemporaneously at time t to capture real-time global market conditions. These variables include World Bank Commodity Index, risk-free rate (10-year US Treasury bond in real terms), and Chicago Board Options Exchange's Volatility Index (CBOE VIX).

\- FX Rate Regime: enters as a binary dummy variable (0 for pegged, 1 for floating regimes) with a 1-year lag $(t - 1)$ to control for the role of country's exchange rate regime

The model is specified by the following logistic cumulative distribution function (CDF):

$$
\begin{array}{l} \operatorname * {P r} \left(\text {Entry} _ {i t} = 1 \mid \text {Entry} _ {i, t - 1} = 0\right) \\ \qquad = \Lambda \Big (\alpha + \beta_ {1} \text {WB Commodity Index} _ {t} + \beta_ {2} \text {Risk - free rate (10Y real)} _ {t} + \beta_ {3} \text {CBOE VIX} _ {t} \\ \qquad + \beta_ {4} \overline {{\text {Inflation}}} _ {i, t - 3, t - 1} + \beta_ {5} \overline {{\text {Real GDP per capita}}} _ {i, t - 3, t - 1} + \beta_ {6} \overline {{\text {Public debt / GDP}}} _ {i, t - 3, t - 1} \\ \qquad + \beta_ {7} \overline {{\text {WGI}}} _ {i, t - 3, t - 1} + \beta_ {8} \overline {{\text {Reserves / Imports}}} _ {i, t - 3, t - 1} + \beta_ {9} \overline {{\text {Real GDP growth}}} _ {i, t - 3, t - 1} \\ \qquad + \beta_ {1 0} \text {FX Regime Dummy} _ {i, t - 1} \Big) \end{array}
$$

$$
\text { where: } \lambda (z) = \frac {e ^ {z}}{1 + e ^ {z}} \text { is   the   logistic   CDF. }
$$

Most macroeconomic and global variables are statistically significant, and signs conform to economic priors (Table 5). The pseudo $R^{2}$ value of 0.21 indicates strong predictive power, reinforced by high statistical significance (p < 0.01) for key variables such as real GDP per capita, US 10-year real rates, institutional quality, and external buffers. The results are found to be robust to consistency checks using one-year and five-year lag specifications, as well as to regressions restricted to market access countries.

The results suggest that the transition to market access is determined by the dual filter of global conditions and domestic economic fundamentals. Strong economic fundamentals, institutional strength, robust external buffers, and favorable global conditions increase the odds of market entry. Global push factors – low real risk-free rate (-0.611) and low market volatility (-0.480) – open issuance windows. The regressions suggest that a one-standard deviation increase in the risk-free rate suppresses the odds of first market entry by about 39 percent. The positive coefficient on commodity prices (0.481) indicates that the probability of market entry increases as global commodity prices rise. This effect may be particularly relevant for countries with higher reliance on commodity exports, as improved terms of trade make them more attractive to investors.

However, it is primarily the strength of domestic pull factors that determine which countries are ready to tap markets when a window of opportunity presents itself. The findings suggest that high income levels (0.920) and institutional quality (0.478) are the most significant macroeconomic predictors of first market entry, along with robust real growth (0.413) and reserve coverage (0.289). Inflation and existing public debt levels are not statistically significant in the model. This may suggest that investors are forward-looking and assign higher weight to longer-term growth potential and governance than to historical debt levels, which generally tend to be contained due to constrained external financing prior to first market entry.

Several features of the empirical design provide reasonable confidence that the estimated coefficients are not biased by potential reverse causality. First, all country-specific macroeconomic variables enter as threeyear rolling averages, creating temporal distance between regressors and the dependent variable. For reverse causality to materially bias the estimates, countries would need to systemically improve domestic pull factors in advance specifically in anticipation of debt issuance. This channel is not highly plausible for most Frontier Economies, where the timing of debut market entry tends to be opportunistic and contingent on global conditions that are difficult to forecast. The regression results are also robust to five-year lag specifications, further alleviating this concern. Second, the discrete-time event history structure drops each country from the sample upon entry, eliminating the feedback channel where market access itself could potentially improve fundamentals. Third, global push factors are among the most statistically significant determinants in the model and truly exogenous to any individual Frontier Economy's reform efforts.

Table 5: Determinants of First Market Entry


Notes: Standard errors in paranthesis. \*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Note: Dependent variable is an indicator for first market entry. Continuous macro variables enter as 3-year lagged averages; FX regime dummy as 1-year lag. FX regime data are from Ilzetzki, Reinhart, and Rogoff (2019, 2021) and are extended beyond 2019 by carrying forward the last available observation.

The evolution of predicted probabilities reveals its sensitivity to global cycles and a clear structural hierarchy among country groups (Figure 5). The chart indicates a synchronized increase in the probability of market entry, shown by the solid lines and interquartile ranges, starting after the GFC and peaking around 2012. This period was characterized by near zero US 10-year real rates, owing to aggressive quantitative easing in the aftermath of GFC and historically high commodity prices, with oil averaging near US\$100 per barrel during the 2012–13 period.

These favorable global push factors opened a window of opportunity for countries with relatively stronger pull factors to enter the market. This explains the 2012–13 peak in the predicted probabilities, which overlaps with an intense actual first-time market entries for Frontier Economies, shown by solid circles. Conversely, the sharp drop in issuances in 2015–16 is partly explained by the collapse in commodity prices, with oil prices declining by two-thirds, closing the issuance window for Frontier Economies and NMACs. The mean probabilities for Frontier Economies rebound around 2016 and peak around 2018–19, when the moderate recovery in oil prices from historic lows and Fed pivot increased the odds of market entry again, allowing several LIC-Frontiers to seize the opportunity to tap the market for the first time. The findings reinforce the notion that domestic economic fundamentals are a necessary precondition, but that the timing of the first-time market entry is highly sensitive to global financial conditions.

Figure 5: Evolution of Predicted Probability for Market Entry

[[KC_IMAGE_008]]

Source: WEO and IDS databases, and authors' calculations

Note: The chart depicts the model's predicted probability of market entry for three distinct groups. Group interquartile ranges are shown as highlighted bands around the mean predicted probabilities, represented by solid lines. Small circles show the model's predicted probability for each country in the year it first entered the Eurobond market. The apparent hierarchy across group interquartile ranges suggests that domestic pull factors play a key role in determining market entry. The probability of a MAC-Frontier economy issuing the Eurobond the first time relative to LIC-Frontier or NMACs is higher even when the global conditions are equally favorable. However, the fact that some countries manage to tap markets despite low predicted probabilities suggests that conducive global conditions can be important push factors, allowing countries to issue despite notable differences in macroeconomic fundamentals.

The hierarchy in predicted probabilities reflects heterogeneity and structural differences of macroeconomic variables across country groups. Despite the shared trend between MAC-Frontiers and LIC-Frontiers, the gap between them remains persistent, with the mean probability consistently higher in the former group, driven by stronger macroeconomic fundamentals and institutions. The trajectory of mean probability for NMACs remains broadly flat and well below the Frontier Economies. This confirms that favorable global conditions alone are not sufficient, but improving domestic economic fundamentals and governance is a precondition to enter the market even during conducive global cycles.

## Post-Entry Debt Accumulation

Does market access impose fiscal discipline or facilitate debt accumulation by softening financing constraints in Frontier Economies? The literature suggests that markets generally reward fiscal rectitude with lower borrowing costs, incentivizing governments to signal discipline to secure initial market access (Goldstein and Woglom, 1991). Even though the immediate signaling pressure subsides after the debut bond, the desire to ensure cheaper funding and preserve market access continues to incentivize governments to restrain borrowing (Ilzetzki and Thysen, 2023). However, an alternative view holds that as external financing constraints suddenly relax with market access, developmental and social spending needs in developing countries may nudge political incumbents to front-load spending while still in office, leading to excessive borrowing (Aguiar et al., 2009; Aguiar, 2023; Fatas et al., 2019).

To evaluate pre- and post-entry policy stances and debt accumulation in Frontier Economies, we compare debt dynamics in the five years before and after market entry. The analysis employs the standard sovereign debt decomposition to disentangle the contributions of different factors to change in debt levels:

$$
\Delta d _ {t} = \frac {\epsilon_ {t} d _ {t - 1} ^ {f}}{\rho_ {t}} + \frac {r _ {t} - g _ {t}}{1 + g _ {t}} d _ {t - 1} - p b _ {t} + s f a _ {t}
$$

where:

The first term in the equation captures the contribution of exchange rate and relative price effects; the second term reflects the contribution of real interest and growth differential; $pb_{t}$ captures the contribution of the primary balance; and $sfa_{t}$ represents stock-flow adjustments. To ensure that the analysis is informative the exercise discards cases with unusually high stock flow adjustments, which generally reflect data inconsistencies or one-off factors rather than persistent economic drivers of debt dynamics.

The analysis shows that market entry is followed by significant changes in debt drivers and accumulation across both groups of Frontier Economies:

MAC-Frontiers: In the five years preceding market entry, MAC-Frontiers manage to reduce their public debt-to-GDP ratio significantly, including as a signaling effort. They exhibit fiscal discipline during this period, effectively maintaining a near-primary balance. Robust growth and relatively low real interest rates during this period result in favorable interest–growth differential. Exchange rate and relative price dynamics reinforce and sustain this virtuous policy setting, providing a strong signal of creditworthiness for prospective bondholders before the Eurobond debut. Overall, public debt declines by a cumulative 10 percent of GDP on average in the five years prior to market entry (Figure 6, left column).

However, following market entry, the fiscal rectitude gives way to looser fiscal stance. In the next five years, the debt-to-GDP ratio increases by about 12 percentage points. Debt accumulation is driven primarily by a notable departure from earlier fiscal stance, with primary deficits contributing a cumulative 9 percent of GDP to debt accumulation. While fiscal loosening leads to higher borrowing costs and a larger contribution from interest rates to debt accumulation, higher commercial borrowing does not appear to spur additional economic growth. Growth remains robust but slows relative to the pre-market period. Accordingly, the negative interest–growth differential falls significantly short of offsetting the cumulative contributions from primary deficits and interest cost.

LIC-Frontiers: LIC-Frontiers present a more nuanced picture. This group of countries suffers from chronic primary deficits both prior to and after market entry, partly reflecting higher development and social spending needs. However, debt dynamics change significantly after market entry.

In the run up to the first Eurobond issuance, LIC-Frontier Economies, on average, ran sizeable primary deficits. Yet, debt remained stable, as the sizeable negative interest–growth differential dampened the impact of the loose fiscal stance. In the five years preceding market entry, the contribution of the real interest rate was practically negligible, suggesting heavy reliance on concessional multilateral and bilateral external financing and limited domestic issuance. Exchange rate and relative price dynamics also served LIC-Frontiers well, resulting in a net negative cumulative contribution. Overall, public debt remained flat prior to market entry (Figure 6, right column).

Following market entry, LIC-Frontiers start accumulating debt, with the debt-to-GDP ratio increasing by about cumulative 11 percentage points in five years. The loose fiscal stance continues after market entry, albeit at slower pace. However, the large contribution from the stock-flow adjustments suggests that the lower primary deficit contribution could be masking the true fiscal outlays from the overall public sector. Growth accelerates somewhat, but despite this acceleration the favorable interest–growth differential narrows on the back of a significantly higher interest burden. This suggests a meaningful shift in the financing mix of LIC-Frontier Economies from concessional external financing toward commercial external and domestic financing following market entry. The contribution from exchange rate and relative prices effects was relatively minor.

Figure 6: Debt Dynamics in Frontier Economies after Market Entrance

MAC-Frontiers debt drivers
(percent of GDP, 5-year cumulative contribution)


[[KC_IMAGE_009]]

LIC-Frontier debt drivers
(percent of GDP, 5-year cumulative contribution)


[[KC_IMAGE_010]]

MAC Frontiers change in public debt (percent of GDP)


[[KC_IMAGE_011]]


LIC Frontiers change in public debt (percent of GDP)

[[KC_IMAGE_012]]

Source: WEO database and authors' calculations
Note: The charts compare the evolution of debt drivers in Frontier Economies over five years prior to (t-6 to t-1) and after (t+1 to t+6) market entry. Positive signs denote contributions to debt accumulation, while negative signs indicate debt reduction.

Overall, the heterogeneity between fiscal stances in MAC-Frontiers and LIC-Frontiers prior to entry dissipates afterward, with debt drivers converging toward a similar pattern. The analysis shows that while both groups displayed notable restraint in public debt accumulation in the run-up to entry, the looser fiscal stance in LIC-Frontiers did not prevent them from tapping markets amid conducive global financial conditions. Establishing market access does not seem to exert meaningful fiscal discipline in either group of Frontier Economies, potentially suggesting that access to capital markets catalyze fiscal expansion by allowing governments to finance higher spending through a new funding source that was previously unavailable. As discussed above, the share of private disbursements in the financing mix increases by about threefold. The rapid shift in the financing mix from concessional external financing toward more expensive commercial external and domestic financing elevates the real interest burden, weighs on development and social spending, and increases exposure to global conditions and investor sentiment. Rapid debt accumulation is not accompanied by an improvement in the underlying interest–growth differential, leading to a buildup of debt vulnerabilities and concerns about debt sustainability.

Examining average growth performance in Frontier Economies relative to the world average shows that market access does not rapidly translate into a notable growth boost. In fact, across both groups of Frontier Economies, average five-year growth relative to the world average declines slightly in the first five years after the first Eurobond issuance. Comparing performance to the world average helps somewhat control for the impact of global cycles, suggesting that the looser fiscal stance enabled by new sources of financing does not help close the relative development gap faster, at least in the short-term.

Figure 7: Growth Performance before and after Market Entry

[[KC_IMAGE_013]]

Source: WEO and IDS databases, and authors' calculations

Note: The chart depicts average annual growth rate differential in Frontier Economies relative to the World average. Shaded areas indicate group interquartile range, and solid lines group averages. T0 indicate market entry years.

The pre- versus post-entry comparison should be interpreted as descriptive evidence on debt dynamics surrounding market access rather than as a causal estimate of its effects. Countries' entry into markets is not random but rather entry takes place under certain global financial conditions and potentially reflects unobserved factors, suggesting that part of the observed deterioration in debt dynamics may reflect broader effects rather than market access alone. While a difference-in-difference approach or matching exercise could in principle provide a stronger counterfactual, their application is constrained by practical limitations. First, market entry among the Frontier Economies is a relatively infrequent event concentrated in a narrow period of favorable global financial conditions, making it difficult to identify a sufficiently large and comparable control group. Second, countries that successfully entered markets exhibit systematic differences from the non-market access countries in terms of institutional quality, income levels, and growth prospects, ultimately limiting the ability to build a credible counterfactual that addresses selection bias concerns. Accordingly, the results should be interpreted as associations around market entry, rather than as evidence that market access itself caused the subsequent deterioration in debt dynamics.

## Conclusion

This paper classifies country groupings based on the durability of sovereign access to international financial markets by using a two-step framework that combines the timing of first Eurobond issuance with persistent reliance on private external creditors for public external financing. The robustness of country classifications is reinforced by an unsupervised K-means clustering exercise that indicates a plateau in fundamentals-based separation at around two decades of sustained access. A discrete-time event LOGIT regression model analysis indicates that global liquidity conditions and risk appetite act as window openers for market entry, but countries with strong domestic pull factors – higher income levels, improved institutional quality, robust growth prospects, and strong reserve buffers – are more likely to leverage favorable global financial and commodity cycles to successfully enter the market.

The post-entry evidence underscores that market access can set countries on markedly different paths. The analysis specifically shows that initial market access tends to trigger a shift in borrowing patterns among Frontier Economies. In general, these economies exhibit some fiscal rectitude and restrain public debt in the run-up to debut Eurobond issuance, partly as a signaling effort. However, debt starts to accumulate faster once access is achieved and a new source of financing is unlocked, potentially nudging countries to frontload development and social spending. For both groups of Frontier Economies, the financing mix rapidly shifts toward bonds, increasing exposure to rollover and global financial cycle risks. Debt decomposition indicates a deterioration in the interest–growth differential as borrowing costs rise, contributing to upward debt trajectories. In MAC-Frontiers, debt accumulation is driven primarily by notable deterioration in primary fiscal balance following market entry, while in LIC-Frontiers persistent deficits are combined with a higher interest burden as countries substitute away from concessional financing. Meanwhile, accessing markets does not translate into relative growth gains, at least in the short run.

The results point to the importance of carefully managing the transition to market financing by reinforcing market access with credible medium-term fiscal frameworks, strengthening debt management capacity, and rebuilding buffers to mitigate stress when global conditions tighten. Countries should avoid interpreting the first Eurobond issuance as durable access to a permanent source of financing, as the findings in this paper and an earlier IMF Departmental Paper on sovereign bond issuances (IMF, 2014) suggest that access to global financial markets can close abruptly when global financial conditions tighten. For Frontier Economies, the policy priority therefore should aim to entrench market borrowing within a well-planned and credible medium-term fiscal framework anchored in debt sustainability, supported by realistic revenue and expenditure projections and informed by debt sustainability assessments (IMF, 2022; IMF, 2024). Strengthening debt management capacity is critical to lengthen maturities, limit rollover and foreign exchange risks, and avoid bunching repayments (IMF, 2014). Without such safeguards, market access may relax financing constraints in the short run while increasing debt vulnerabilities when global financial conditions tighten.

## References

Abate, G., Brown, M., Sienaert, A., and Thomas, M., 2021, “Economic Governance Improvements and Sovereign Financing Costs in Developing Countries”, World Bank Policy Research Working Paper No. 9649

Aguiar, Mark, Amador, Manuel, and Gopinath, Gita, 2009, “Investment Cycles and Sovereign Debt Overhang”, Review of Economic Studies, Volume 76, Issue 1, 1–31

Aguiar, Mark, 2023, “The Costs and Consequences of Sovereign Borrowing”, Mundell-Fleming Lecture, Jacques Polak Annual Research Conference (Washington: International Monetary Fund).

Alexandrino da Silva, Victor Hugo, Antoun de Almeida, Luiza, and Singh, Diva, 2021, “Determinants of and Prospects for Market Access in Frontier Economies”, IMF Working Paper No. 21/137 (Washington: International Monetary Fund).

Comelli, Fabio, 2012, “Emerging Market Sovereign Bond Spreads: Estimation and Back-testing”, IMF Working Paper No. 12/212 (Washington: International Monetary Fund).

Fatas, A., Ghosh Atish, Ugo, Panizza, and Presbitero, Andrea, 2019, “The Motives to Borrow”, IMF Working Paper No. 2019/101 (Washington: International Monetary Fund).

Feyen, E., Ghosh, S., Kibuuka, K., and Farazi, S., 2015, “Global Liquidity and External Bond Issuance in Emerging Markets and Developing Economies”, World Bank Policy Research Working Paper No. 7363

Gelos, Gaston, Sahay, Ratna, and Sandleris, Guido, 2004, “Sovereign Borrowing by Developing Countries: What Determines Market Access?”, IMF Working Paper No. 04/221 (Washington: International Monetary Fund).

Guscina, Anastasia, Malik, Sheheryar, and Papaioannou, Michael, 2017. “Assessing Loss of Market Access: Conceptual and Operational Issues”, IMF Working Paper No. 17/246 (Washington: International Monetary Fund).

Haque, Tobias, Bogoev, Jane, and Smith, Greg., 2017. "Push and Pull: Emerging Risks in Frontier Economy Access to International Capital Markets", World Bank Group Discussion Paper No. 17 (Washington: International Monetary Fund).

Hartelius, Kristian, Kashiwase, Kenichiro, and Kodres, Laura, 2008. “Emerging Market Spread Compression: Is it Real or is it Liquidity?”, IMF Working Paper No. 08/10 (Washington: International Monetary Fund)

Ilzetzki, Ethan and Thysen, Heidi Christina, 2023, “Fiscal Rules and Market Discipline”, Seminar Paper for Jacques Polak Annual Research Conference (Washington: International Monetary Fund).

International Monetary Fund, 2014. “Issuing International Sovereign Bonds: Opportunities and Challenges for Sub-Saharan Africa”, Departmental Paper No. 2014/007 (Washington: International Monetary Fund).

International Monetary Fund and World Bank, 2017, “Review of the Debt Sustainability Framework for Low Income Countries: Proposed Reforms”, IMF Policy Paper and WB Board Report (Washington: International Monetary Fund and World Bank).

International Monetary Fund, 2018, “Guidance Note on the Bank-Fund Debt Sustainability Framework for Low Income Countries”, IMF Policy Paper and WB Board Report (Washington: International Monetary Fund and World Bank).

International Monetary Fund, 2022, “Staff Guidance Note on the Sovereign Risk and Debt Sustainability Framework for Market Access Countries”, IMF Policy Paper No. 2022/039 (Washington: International Monetary Fund).

International Monetary Fund, 2023, “Navigating Fiscal Challenges in Sub-Saharan Africa: Resilient Strategies and Credible Anchors in Turbulent Waters”, IMF Departmental Paper, DP/2023/007 (Washington: International Monetary Fund).

International Monetary Fund, 2024. “2024 Review of the Poverty Reduction and Growth Trust Facilities and Financing – Reform Proposals”, IMF Policy Paper No. 2024/047 (Washington: International Monetary Fund).

International Monetary Fund, 2024. “How to Develop and Implement a Medium-Term Fiscal Framework”, IMF How-To Note 2024/005

International Monetary Fund, 2025, “Debt Vulnerabilities and Financing Challenges In Emerging Markets and Developing Economies—An Overview of Key Data”, IMF Policy Paper No. 2025/002 (Washington: International Monetary Fund).

lossifov, Plamen, Ali Abbas, Niermann, Leinart, 2026, “Benchmarking Dynamically Stable Public Debt Trajectories for Low-Income Countries”, IMF Working Paper No. 26/75 (Washington: International Monetary Fund).

Presbitero, Andrea, Ghura, Daneshwar, Adedeji, Olumuyiwa, and Njie, Lamin, 2015. “International Sovereign Bonds by Emerging Markets and Developing Economies: Drivers of Issuance and Spreads,” IMF Working Paper No. 15/275 (Washington: International Monetary Fund).

Stiglitz, J., and Weiss, A., 1981, “Credit Rationing in Markets with Imperfect Information”, American Economic Review, Vol. 71(3), 393–410.

Wong, K.L., Manger, M., and Panizza, U., 2026, “Determinants of Sovereign Bond Issuance in Emerging Markets”, IHEID Working Paper 06-2026 / CEPR Discussion Paper No. 21251.

World Economic Outlook, 2025, “Emerging Market Resilience: Good Luck or Good Policies”, WEO Chapter 2 (Washington: International Monetary Fund).

World Bank, 2026, “Frontier Market Economies: Promise, Performance, and Prospects”, Global Economic Prospects, Chapter 4 (Washington: World Bank).

## Annex I. Data

## A.1 Overview

The empirical analysis combines macroeconomic, institutional, debt, and global financial data from a set of established public sources. Wherever possible, variables used jointly within a single exercise are drawn from the same source to ensure internal consistency; where this is not feasible, the choice of source is dictated by coverage of the country-year panel (92 countries; the bond-market analysis covers 1980–2024, with the cluster analysis using country-level averages over 1996–2024). Table A.1 summarizes all data sources; the remainder of this appendix provides detail on each component.

Table A.1. Data sources by variable group


## A.2 Macroeconomic aggregates

Real GDP, real GDP growth, headline (CPI) inflation, and gross general government debt are taken from the IMF World Economic Outlook (WEO) database. WEO is used as the primary source for these series because of its broad country coverage, regular updating, and the harmonized treatment of fiscal and price aggregates across reporting countries.

## A.3 Governance and institutional quality

Institutional quality is measured using the World Bank Worldwide Governance Indicators (WGI). The cluster analysis uses the simple average of the six WGI dimensions (voice and accountability, political stability and absence of violence, government effectiveness, regulatory quality, rule of law, and control of corruption), normalized to a comparable scale across countries.

## A.4 Banking, monetary, and real-sector variables (expanded cluster exercise)

The robustness exercise that expands the cluster analysis to over 20 macroeconomic variables uses the World Bank World Development Indicators (WDI) for series not available from WEO. These include domestic credit to the private sector, broad money, foreign direct investment inflows, trade openness, gross savings and investment, banking-sector depth indicators (borrowers and depositors per thousand adults), and additional fiscal aggregates (general government revenue and expenditure to GDP).

## A.5 External debt and sovereign bond issuance

External debt stocks, the share of external debt held by private creditors, and sovereign bond issuance are obtained from the World Bank International Debt Statistics (IDS) database. Bond issuance is measured using the series PPG, bonds (DIS, current US\$) (identifier DT.DIS.PBND.CD), which records gross disbursements on publicly guaranteed bonded debt at current U.S. dollar values. Because issuance is reported as a current-dollar flow, no further currency conversion is applied; consequently the underlying repayment currency is not identified in this series.

The IDS bond-issuance record is supplemented with a small number of issuances that are documented in primary sources (official statements, prospectuses, and contemporaneous market reporting) but are not captured in the DT.DIS.PBND.CD series. These are listed in Table A.2 and have been added at their reported face values without further adjustment.

Table A.2. Manually added sovereign bond issuances


These additions are quantitatively small relative to the IDS-based panel and are intended to ensure that the sovereign bond market-access classification is not affected by isolated reporting gaps. Augmenting the data in this way affects the timing of first market access for the listed countries; results are robust to dropping these manual additions.

## A.6 Debt-dynamics decomposition

For the debt-dynamics analysis, interest payments, the primary fiscal balance, and real GDP growth are taken from the IMF Public Finances in Modern History (PFMH) database. Drawing all three inputs from a single source preserves accounting consistency in the standard debt-decomposition identity; PFMH is used because it offers the longest harmonized cross-country panel of fiscal aggregates available, which matters for assessing the persistence of debt accumulation patterns over the post-1980 sample.

## A.7 Global push factors

The logit specification of market-access transitions includes three global push factors. The CBOE Volatility Index (VIX), used as a measure of global risk appetite, is obtained from the Chicago Board Options Exchange via the Federal Reserve Bank of St. Louis FRED database (series VIXCLS). The U.S. long-term interest rate is the 10-year U.S. Treasury constant maturity yield, also from FRED. The aggregate commodity price index is taken from the World Bank Commodity Markets ("Pink Sheet") release. All three series are aggregated to annual frequency to align with the country-year panel.

## A.8 Exchange-rate regime classification

The de facto exchange-rate regime classification is taken from Ilsetzki, Reinhart, and Rogoff (2019, 2021). Because the published series end in 2019, the classification is extended through the end of the sample by carrying forward each country's last observed regime. This is the standard convention in applications using these data and reflects the high persistence of de facto regimes; the small share of country-years affected makes alternative extrapolation choices immaterial for the results.

## A.9 Sample and other restrictions

The sample is restricted to countries with a population above 2 million. This restriction is applied because very small economies (i) tend to have sparser and less methodologically consistent macroeconomic data, (ii) exhibit idiosyncratic structural features (single-sector dependence, currency boards, large external transfers) that are poorly characterized by the fundamentals used in the cluster analysis, and (iii) are largely excluded from international sovereign bond markets for reasons unrelated to those fundamentals. This cutoff follows standard practice in the sovereign debt literature.

The full universe of countries entering the analysis is defined as all economies in the World Bank International Debt Statistics database with a population above 2 million. This yields 92 countries, distributed across World Bank regions as shown in Table A.3.

Table A.3. Sample composition by region


Table A.4 Expanded list of macroeconomic variables used in clustering exercise


## Annex II. Regression Results

Logit — dependent variable: market entry (event = 1)
Table A.5 Regression results excluding FCS All Countries (without FCS) — 3-lag


Only Access — 5-lag
Logit — dependent variable: market entry (event = 1)


Cluster-robust standard errors (by country) in parentheses.
Lag structure: continuous regressors = 5-year average (lagged); dummies lagged 1 year. Continuous regressors \*\*\* p<0.01, \*\* p<0.05, \* p<0.10.

Table A.6 Regression results including all sample countries


Cluster-robust standard errors (by country) in parentheses.
Lag structure: continuous regressors = 3-year average (lagged); dummies lagged 1 year. Continuous regressors have \*\*\* p<0.01, \*\* p<0.05, \* p<0.10.

All Countries (without FCS) — 5-lag
Logit — dependent variable: market entry (event = 1)


RMACs (Percent)

## Annex III. Expanded Stylized Facts

Figure A.1: Governance, Market Access, Evolution of External Financing in EMDEs – Simple Averages


[[KC_IMAGE_014]]


[[KC_IMAGE_015]]

Source: WEO and IDS databases and authors' calculations


[[KC_IMAGE_016]]


Figure A.2: Decomposition of Public Debt in EMDEs – Simple Averages

[[KC_IMAGE_017]]


[[KC_IMAGE_018]]


[[KC_IMAGE_019]]

Source: WEO and IDS databases and authors' calculations


[[KC_IMAGE_020]]


Figure A.3: Spreads and Maturities before and after Market Entry Spreads over US Treasury

[[KC_IMAGE_021]]


[[KC_IMAGE_022]]

Source: WEO and IDS databases and authors' calculations
