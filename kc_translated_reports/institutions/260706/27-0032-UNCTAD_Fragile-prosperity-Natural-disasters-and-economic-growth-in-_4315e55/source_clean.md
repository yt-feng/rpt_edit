#12
# Fragile Prosperity: Natural Disasters and Economic Growth in Small Island Developing States
## Abstract

This study re-examines the complex link between climate-related disasters and economic growth in developing countries, with a focus on the specific vulnerabilities of Small Island Developing States (SIDS). It underscores the importance of combining diverse disaster metrics to fully capture the risks faced by SIDS. Using system GMM estimation, the analysis reveals that SIDS experience disproportionately severe medium-term growth setbacks compared to other developing nations, even after accounting for standard growth determinants. This can be linked to sector-specific pathways of vulnerability, as storms have a relatively more pronounced impact on services growth, and floods on industrial value-added growth.

## Key words

Natural disasters, economic growth, climate change, small island developing states (SIDS), vulnerability.

## Contents

1. Introduction......3
2. Literature review......5
3. Data and related sources......8
3.1 Natural disasters' metrics......8
3.2 SIDS specificities through the lenses of disaster metrics......12
3.3 Dependent and control variables......14
4. Model specifications and estimation strategy......16
4.1 Introducing Disaster Variables into the Growth Model......16
4.2 Estimation Methodology......18
5. Results......21
6. Robustness checks......27
6.1 Capital Investment......27
6.2 Subsample Stability......28
7. Conclusions......30
References......31
APPENDIX......33

# 1. Introduction

Natural disasters are becoming a more prominent feature of our day-to-day lives. Scientific evidence has unequivocally warned that rising temperatures trigger an increase in the frequency and intensity of weather and climate extremes, with natural hazards entailing harsh socioeconomic impacts on the most vulnerable economies like Least Developed Countries (LDCs) or Small Island Developing States (SIDS) (Coronese et al., 2019; IPCC, 2022; UNCTAD, 2022). $^{1}$ Moreover, this trend will continue to intensify as anthropogenic greenhouse gas emissions progressively destabilize the climate system and surface temperatures break record after record.

Against this background, several initiatives have been implemented to enhance the monitoring and assessment of disaster risks under the Sendai Framework for Disaster Risk Reduction. $^{2}$ A range of alternative indicators have been proposed to gauge related countries’ vulnerabilities, including the Economic and Environmental Vulnerability Index, the University of Notre Dame’s Global Adaptation Initiative (ND-GAIN) Index and the Multidimensional Vulnerability Index (United Nations, 2024a, 2024b). Moreover, after years of intense negotiations, the 27th Conference of the Parties (COP 27) of the United Nations Framework Convention on Climate Change (UNFCCC) agreed to establish a fund for responding to loss and damage associated with the adverse effects of climate change, including extreme weather events and slow onset events (UNCTAD, 2023).

If the ongoing improvements in disaster risk monitoring and the operationalization of the loss and damage fund testify to the growing relevance of this issue in international debates, the analysis of the impacts of natural disasters on macroeconomic variables warrants further research. In particular, the understanding of the nexus between natural disasters and economic growth – i.e. the key driver of countries' capacity to sustainably mobilize resources for reconstruction and recovery – remains partial, or at best nuanced. The need for a fine-grained understanding of the relationship between natural disasters and growth is all the more pronounced in the case of LDCs and SIDS, for which data limitations have been most prevalent.

Hazards are defined as natural processes, such as storms or wildfires, that can trigger disasters only upon interaction with human-made features such as settlements, agriculture, infrastructure and the like (Chaudhary and Piracha, 2021). While acknowledging this important conceptual distinction, henceforth we refer to “natural disasters” in line with most of the literature concerned with the socio-economic impacts of natural hazards.


This paper contributes to filling this knowledge gap by empirically assessing the extent to which SIDS' specificities translate into a differentiated pattern of impacts of climate-related natural disasters on economic growth. $^{3}$

The paper is structured as follows: Sections 2 and 3 outline related literature and discuss methodological issues, particularly those related to the measurement of natural disasters, and of SIDS' specific vulnerabilities. Section 4 presents the econometric specification, and Section 5 examines the results. Sections 6 and 7 provide some robustness checks and conclusions, respectively.


[[KC_IMAGE_001]]


# 2. Literature review

Natural disasters exert complex wide-ranging impacts on macroeconomic variables, from physical asset destruction to fiscal effects, and from productivity losses to reduced human capital investment, via health and education disruptions (Skidmore, 2022a; Ehlers et al., 2025). Disasters' effects on GDP growth play an important role in this respect, as growth represents not only the path to recovery, but also a key driver of countries' capacity to mobilize financial resources for reconstruction in a sustainable way. While a large body of literature has been devoted to this subject, its conclusions have so far offered a nuanced and somewhat inconclusive picture.

On the one hand, theoretical considerations do not provide a decisive answer on the relationship between natural disasters and GDP growth (Cavallo et al., 2013). In the aggregate neoclassical framework (i.e. the so-called augmented Solow model), the destruction of human or physical capital provoked by a disaster can trigger short-run growth spurts, as it triggers a temporary acceleration of investment to regain the steady-state equilibrium; however, this temporary adjustment is unlikely to affect the long-term growth determinant, namely technological progress. Endogenous growth theory offers even less clearcut predictions: in Schumpeterian models, natural disasters could even lead to higher growth by inducing reinvestments in new and more efficient vintages of capital; in so-called “AK models” with constant returns to capital/knowledge, the rate of growth would be unchanged, while in endogenous growth models with increasing returns, disasters would trigger a permanently lower growth path.

On the other hand, the empirical literature yields varied conclusions, depending on factors, such as the type of disasters considered, the metrics used to assess their impact, the sample of countries and time period, the focus on temporary versus long-term effects, as well as the array of methodologies employed (Botzen et al., 2019; Onuma et al., 2021; Cuaresma, 2022). In one of the seminal contributions on the subject, Skidmore and Toya (2002) show, using a cross-section of 89 countries, that climatic disasters are positively correlated with real GDP per capita growth, unlike their geological counterparts. The authors also find that higher frequencies of climatic disasters lead to stronger human capital accumulation and faster total factor productivity growth; a finding they interpret as a sign that disasters provide an incentive to update the capital stock with new vintages of technologies. The existence of similar “blessings in disguise effects” is also postulated by various studies on spatial economic resilience, underscoring effective public management as a key factor shaping the recovery (Nijkamp and Borsekova, 2019; Bănică et al., 2020). In the same vein, a study across United States’ counties estimated that disasters triggering federal aid raise per capita personal income over the long run (8 years), while local population and employment remain unaffected (Roth Tran and Wilson, 2024).

These rather benign conclusions are, however, contradicted by a wide range of other empirical studies, finding either no systematic effects, or negative ones. Cuaresma (2022), for instance, employs Bayesian model averaging techniques on a sample of 123 countries, and finds a consistent lack of partial correlation between the risk of natural disasters and economic growth, with no systematic evidence of effect heterogeneity across income levels or regions. Cavallo et al (2022) find evidence of sizeable negative effects on growth when the severity of disasters is determined by the associated mortality, but negligible effects when severity is determined by the physical intensity (which implies a more balanced sample of developed and developing economies).

Again, numerous studies – mainly based on panel data techniques suitable to address endogeneity concerns – find evidence of a negative effects of natural disasters on countries’ economic growth (Noy, 2009; Raddatz, 2009; Hochrainer, 2009; Loayza et al., 2012; Fomby et al., 2013; Felbermayr and Gröschl, 2014; Onuma et al., 2021; Naoaj, 2023; Ehlers et al., 2025). Though converging on the negative impacts of natural disasters on growth, this literature yields a nuanced picture in relation to the pattern and drivers of these results. Three main considerations stand out in this respect. First, most studies find heterogeneous impacts across countries, with nations at lower levels of income per capita and/or with lower human capital typically suffering more severe shocks (Noy, 2009; Loayza et al., 2012; Fomby et al., 2013; Felbermayr and Gröschl, 2014; Onuma et al., 2021; Naoaj, 2023). Second, distinct sectoral impacts emerge across disaster types, whereby agriculture and industry display heightened vulnerability, notably to droughts and storms (Raddatz, 2009; Loayza et al., 2012; Fomby et al., 2013; Coulibaly et al., 2020; Naoaj, 2023; Ehlers et al., 2025). Third, the negative effects on economic growth can be largely traced to the most severe disasters, while for less intense ones some studies even find positive effects (Loayza et al., 2012; Fomby et al., 2013; Felbermayr and Gröschl, 2014; Onuma et al., 2021; Naoaj, 2023). $^{4}$

Overall, the above picture points to the need to develop a more nuanced and context-specific understanding of the disaster-growth nexus, as “disasters can have differential effects depending on conditions, circumstances, study scope, and study design” (Skidmore, 2022b: 8). The present paper represents a step in that direction, unravelling the extent to which SIDS’ defining structural characteristics shape the relationship between natural disasters and growth. To the best of our knowledge, this is the first paper empirically testing whether these impacts in SIDS differ from those in other developing countries.

More broadly, our contribution is also related to the recent policy research emphasizing the unique climate vulnerabilities of SIDS, the potential risks of a “climate-debt trap”, as well as the rising magnitude of loss and damage (Ishizawa and Miranda, 2019; Slany, 2020; IPCC, 2022; Addison et al., 2022; Park and Samples, 2024; Panwar et al., 2024; Tandrayen-Ragoobur et al., 2026). Much of this literature has focused on financial gaps and proposed mechanisms to address them, in line with the progress of international negotiations on the establishment and operationalization of the Loss and Damage Fund, as well as the growing call for boosting of adaptation finance. While this paper does not directly address financing issues, an accurate understanding of the relationship between natural disasters and growth remains a precondition to develop viable forms of financial support for vulnerable countries.


[[KC_IMAGE_002]]


# Data and related sources

The present section discusses data issues and is divided into three parts. The first subsection examines disaster-related data at granular level, presents related descriptive statistics and explains the construction of the frequency and intensity measures utilized in the following econometric analysis. The second subsection links key methodological considerations with the specific traits of SIDS vulnerability, while the third discusses control variables.

## 3.1 Natural disasters' metrics

Like most of the empirical literature reviewed above, data on natural disasters is drawn from the Emergency Events Database - EM-DAT (Delforge et al., 2023). EM-DAT provides core data on individual disasters, their location, date of occurrence, and their health and economic impacts, for 26,000 disasters worldwide, from 1900 to the present. The database is compiled from various sources of information, including UN agencies, non-governmental organizations, insurance companies, research institutes, and press agencies. Disasters are recorded if they meet at least one of the following inclusion criteria: (i) at least ten deaths (including dead and missing); (ii) at least 100 affected (people affected, injured, or homeless); and (iii) a call for international assistance or an emergency declaration. These criteria confine the dataset to major disasters with considerable economic consequences.


Table 1 provides the summary statistics at individual disaster level, from which several considerations can be drawn. First, data availability differs across the various metrics of impact. Compared to the total number of climate-related disasters in the sample, the share of missing observations reaches 17 per cent in the case of the affected population, 27 per cent for the number of deaths and as much as 69 per cent for total economic damage. This limitation seems particularly pronounced in the case of droughts and storms. Second, the impacts of climate-related disasters display a marked variability across all dimensions. $^{5}$ Third, while droughts are relatively rare, they tend to have by far the most severe human and socio-economic costs. This is presumably due to their prolonged effects on agricultural markets and broader macroeconomic fundamentals, via food prices and import bill, as well as to the wide-ranging and multifaceted harm caused by water scarcity. Floods, conversely, are relatively common representing over half of the disasters in our sample, but typically entail more circumscribed impacts. A similar assessment applies to storms.

Table 1
Granular summary statistics of disaster variables, developing countries, 1979–2023


$^{5}$ The coefficient of variation reaches 23 in the case of number of deaths, nine and four for affected population and total damage respectively.

Figure 1

Looking at the evolution of climate-related disasters over time, EM-DAT data portend a substantial increase in the average frequency of climate-related disasters in developing countries, particularly between the early-1980s and the early 2000s (Figure 1). This can be primarily traced to the rising number of floods, with more gentle but still upward trends for all other disaster types. While the increase is significant—with the average frequency of climate-related disasters rising five-fold in the last 25-30 years—it would be inaccurate to attribute this solely to global warming. Enhanced reporting practices have also contributed to this trend, as highlighted by Delforge et al. (2023).


[[KC_IMAGE_003]]


Before moving to control variables, it is worth highlighting the peculiarities of droughts. Compared to other hazards in our sample, droughts differ in two key ways. First, they are a slow-onset phenomenon whose beginning is generally difficult to detect. Moreover, they are not solely a physical phenomenon; rather, their impacts can be mitigated or exacerbated by human activities through water management, supply and demand. Second, droughts tend to have a much longer duration than other disaster types (Figure 2). In our sample the median duration of droughts reaches six months, compared to less than one month for other disaster types. Both these features have a bearing on droughts' disproportionate human and socioeconomic impacts noted earlier in Table 1.


[[KC_IMAGE_004]]

excludes outside values

Based on the granular data described above, the rest of the paper uses four complementary measures to gauge countries' exposure to – or intensity of – natural disasters over a given period T. The first measure is the frequency of disasters, formally defined as

$$
F R _ {p, j} ^ {D} = \frac {\sum_ {t = 1} ^ {T} N D _ {t , j} ^ {D}}{\mathrm{T}}
$$

where $ND_{t,j}^{D}$ is the number of disasters of type D occurring in country j in year t of period p (whose length is T years). A complementary measure is also introduced to account for the fact that larger countries tend to record a higher number of disasters: the normalized frequency

$$
N _ {-} F R _ {p, j} ^ {D} = \frac {\sum_ {t = 1} ^ {T} \left. N D _ {t , j} ^ {D} \right/ _ {L a n d A r e a _ {t , j}}}{\mathrm{T}}
$$

whereby the occurrence of disasters is normalized by land area.

Since the above measures do not convey any information about disasters' human and socio-economic impact, a pair of complementary measures are also considered. The intensity of disasters is defined as

$$
I n t e n _ {p, j} ^ {D} = \frac {1}{T} \sum_ {t = 1} ^ {T} (F a t a l i t i e s _ {t, j} ^ {D} + 0. 3 A f f e c t e d _ {t, j} ^ {D})
$$

and the normalized intensity of disasters, which is defined by Loayza et al. (2012) $^{6}$ as

$$
N _ {-} I n t e n _ {p, j} ^ {D} = \frac {1}{T} \sum_ {t = 1} ^ {T} \left(\frac {F a t a l i t i e s _ {t , j} ^ {D} + 0 . 3 A f f e c t e d _ {t , j} ^ {D}}{T o t a l P o p u l a t i o n _ {t , j}}\right)
$$

Similarly to the normalized frequency, the normalized intensity is expressed as a share of the total population thereby accounting for countries' size.

Subsequent sections of the paper will employ the above metrics both in aggregate form – that is, by aggregating all climate-related disasters – and by disaster type, to shed more light on their differential impacts.

## 3.2 SIDS specificities through the lenses of disaster metrics

Considering the above metrics, the present subsection examines three facets of SIDS specificities that deserve careful consideration. First, “smallness” being a defining feature of the SIDS category, the normalization of natural disaster variables matters greatly. Figure 3 provides an easy way to visualize this point. The first panel depicts the scatterplot of frequency and normalized intensity of natural disasters for developing countries, SIDS and non-SIDS. SIDS appear to be characterized by relatively low frequency but high socio-economic impacts of natural disasters, but their situation seems only slightly different from other developing countries. By normalizing the frequency by land area on the horizontal axis (second panel), the peculiarity of SIDS surfaces markedly. Most of them appear clustered in the top right corner, with high normalized frequency and high normalized intensity, suggesting that, relative to their land size, they are disproportionately exposed to natural disasters on both accounts. This simple example points to the importance of triangulating the available metrics in a complementary way, as different choices may tease out or rather normalize crucial facets of vulnerability.

Figure 3
Frequency, intensity and normalized frequency of natural disasters in developing countries (2021–2023)
SIDS
OTHERS
Droughts Floods Storms Other Climate-Related Disasters


[[KC_IMAGE_005]]

Normalized intensity


[[KC_IMAGE_006]]


Second, compared to other developing countries SIDS tend to be more exposed to certain types of disasters and less exposed to others (Figure 4). Between 1979 and 2023, storms accounted for nearly 71 per cent of all recorded disasters in SIDS, in contrast to their 29 per cent share in all developing countries. Droughts are also somewhat over-represented in SIDS, making up 11 per cent of the total, compared to an average of 7 per cent across all developing countries. In contrast, floods are significantly under-represented in SIDS, comprising only 18 per cent of the total, while they account for 51 per cent in all developing countries. Similarly, other climate-related disasters are less common in SIDS, representing just 1 per cent of the total compared to 12 per cent in developing countries overall. Since different disaster types tend to have distinct effects on economic growth (see section 2), this pattern is crucial for accurately assessing the specific vulnerabilities of SIDS.

Figure 4
Incidence of natural disasters, by region and type (1979–2023)


Third, uneven data quality introduces potential biases and affects the suitability of the various metrics. Table 2 shows that data gaps are uneven across metrics, disaster types and regions. As is well known, data on total damages are exceptionally scarce in developing countries, and for this very reason they are not considered in the following analysis. Nonetheless, data gaps are extremely widespread for total affected people and fatalities, undermining the reliability of intensity measures. More specifically, the higher incidence of missing values for SIDS compared to other developing countries will likely to bias comparisons based on intensity measures. Similarly, the differential incidence of missing values across disaster types is likely to introduce additional biases, whose direction may be hard to predict.


## Table 2

Percentage of missing data for socio-economic impacts of disasters, by type, metrics and region, (1979–2023)


The bottom line is that triangulating metrics and exploiting their complementarities is fundamental for any empirical study on natural disasters, and all the more so if one intends to investigate the specificities of SIDS or other vulnerable country groups.

## 3.3 Dependent and control variables

After reviewing the disaster-related variables in detail, this subsection discusses other variables used in the following estimates. Except for natural disaster variables, all data are drawn from the World Bank's World Development Indicators.

The main dependent variable considered here is the average growth rate of real per capita Gross Domestic Product (GDP), over the period p. To gain further insights into the sectoral impacts of disasters, we estimate separate regressions using as dependent variables the average growth rate of real per capita Value Added in three main sectors: agriculture, forestry, and fishing; industry (including construction), and services. This multi-dimensional approach offers insights into how natural disasters affect different economic sectors. All the underlying variables are measured in constant 2015 US dollars and drawn directly from the World Development Indicators database, whereas we calculate per capita levels and growth rates.

Control variables include standard growth determinants drawn from the empirical growth literature (Durlauf et al., 2005) and closely related to those used by similar studies adopting panel techniques (Raddatz, 2009; Loayza et al., 2012). These include:

\- Initial enrolment, a measure of human capital, proxied by gross secondary school enrollment, and treated as a predetermined variable capturing the initial conditions;

\- Financial depth, measured as domestic credit to private sector as a percentage of GDP;

• Government consumption expenditure as a share of GDP;

\- Inflation, measured as the annual percentage change in Consumer Price Index with 100 added to ensure strictly positive values;

\- Trade openness, defined as the ratio of imports plus exports, divided by GDP, which is a proxy for the economy's exposure to global markets, potentially affecting recovery dynamics after disasters;

\- Terms of trade shocks, measured as the growth rate of net barter terms of trade, which can provide insights into how external economic conditions impact domestic growth.

Human capital enters the regressions as the logarithm of the initial value in period p, whereas financial depth, government consumption, inflation and trade openness enter as the logarithm of the corresponding period averages. $^{7}$ Similar to the dependent variables, terms of trade shocks are included as the average growth rate over period p, in percentage terms.

In addition to the above, all regressions include the lagged dependent variable, to account for the dynamic nature of the growth process, as well as period dummies to capture global shocks across countries (think of the COVID-19 pandemic). The descriptive statistics of all socioeconomic variables are reported in Table 3.

## Table 3


## Descriptive statistics of control variables included in the regressions


# Model Specifications and Estimation Strategy

We build on the framework of Loayza et al. (2012) and employ a GMM estimation approach to investigate the impact of natural disasters on economic growth. Subsection 4.1 introduces natural disasters into the growth equation and details the characteristics of the model. Subsection 4.2 then outlines the estimation strategy, with particular attention to its methodological underpinnings and assumptions.

## 4.1 Introducing disaster variables into the growth model

We begin with the standard empirical growth equation, pioneered by Islam (1995):

$$
y _ {j, t} = \beta_ {0} y _ {j, t - 1} + \pmb {\beta_ {1}} \pmb {X} _ {j, t} + \mu_ {t} + \lambda_ {j} + \varepsilon_ {j, t}\tag{1}
$$

where $y_{j,t}$ represents output growth (real GDP or real sectoral Value Added) in country j and year t. The vector $X_{j,t}$ includes the growth determinants listed in Subsection 3.3, while $\mu_{t}$ and $\lambda_{j}$ capture time-specific and country-specific fixed effects, respectively. Finally, $\varepsilon_{j,t}$ is the traditional error term.

The lagged dependent variable $y_{j,t-1}$ is included to account for predetermined conditions, making the model dynamic. We choose to include the lagged dependent variable rather than initial output, as the latter complicates the interpretation of coefficients. Specifically, even when the dependent variable is output growth, the model behaves like an AR (1) process for levels, causing every coefficient to reflect the impact on the speed of convergence. Moreover, $\beta_{0}$ indicates the persistence of output growth, which is critical for assessing the significance of other variables. High persistence implies that even variables with significant coefficients may have limited importance for driving growth.

It is worth noting that gross capital formation (i.e. gross domestic investment), often considered an important determinant of growth, is deliberately excluded from $X_{j,t}$ . As argued in the literature (Skidmore and Toya, 2002; Hallegatte et al., 2007), disasters can impact growth through two distinct channels: by affecting total factor productivity and through the capital channel via reconstruction efforts. Yet, to fully disentangle the two effects one would need to use a development accounting framework, since new vintages of capital may embody more productive technologies. $^{8}$ By omitting gross capital formation, the coefficients on disaster variables capture the overall effect of disasters on growth. In Section 6, capital investment will be reintroduced into the equation to distinguish between these two channels.

Before introducing the disaster measures, we transform the annual equation (1) into a 3-year period equation. This adjustment allows sufficient time for the economy to adjust to the shock created by the natural disaster. Our baseline 3-year period strikes a balance by capturing medium-term disaster impacts while ensuring a sufficiently large number of periods for the estimation.

$$
\overline {{y _ {j , p}}} = \beta_ {0} \overline {{y _ {j , p - 1}}} + \pmb {\beta_ {1}} \overline {{\pmb {X _ {j , p}}}} + \mu_ {p} + \lambda_ {j} + \varepsilon_ {j, p}\tag{2}
$$

where $\overline{y_{j,p}}$ is the average real output growth rate in period p for country j. In $\overline{X_{j,p}}$ , all variables are calculated as period averages, except for initial enrolment, which is expressed as the logarithm of enrolment rate in the first year of period p. The logarithms of financial depth, government consumption, inflation, and trade openness are taken after computing their period averages. Growth rates, namely output growth and terms of trade growth, remain expressed as percentages.

As is common in the literature (Noy, 2009; Loayza et al., 2012; Felbermayr and Gröschl, 2014; De Oliveira, 2018), we assume that disasters follow a multiplicative risk formulation, which translates to an additive form in a logarithmic equation. Accordingly, we incorporate them into equation (2) as the logarithm of the disaster variables introduced in Subsection 3.1, which are already expressed in period average form. Furthermore, since natural disaster measures are positively skewed, taking their logarithm serves the dual purpose of linearizing the relationship and minimizing the impact of extreme values on the estimation.

One important consideration when taking the logarithm of disaster measures, which have a value of 0 for countries and periods with no disasters, is ensuring that these observations are not lost during the transformation. To address this, we replace zeros for each of the four disaster measures with one-tenth of the minimum non-zero value of that measure, calculated across its five associated variables (the combined variable and the four separate disaster type variables). This ensures that the distribution of disaster variables remains undistorted.

The final baseline equation for estimation becomes

$$
\overline {{y _ {j , p}}} = \beta_ {0} \overline {{y _ {j , p - 1}}} + \pmb {\beta_ {1}} \overline {{X _ {j , p}}} + \beta_ {3} D _ {j, p} + \mu_ {p} + \lambda_ {j} + \varepsilon_ {j, p}\tag{3}
$$

where $D_{j,p}$ can represent either:

\- A aggregate metric ( $FR_{p,j}^{All}$ , $N\_FR_{p,j}^{All}$ , $Inten_{p,j}^{All}$ or $N\_Inten_{p,j}^{All}$ ) capturing all disasters combined, or

\- A vector of four disaster types (droughts, floods, storms, and other climate-related disasters), with each type measured by one of the four metrics.

## 4.2 Estimation Methodology

Moving to the characteristics of our model and the estimation strategy, the first issue with equation (3) is the presence of unobserved country- and period-fixed effects. Period-fixed effects are straightforward to handle using period dummies. However, the same does not apply to country-fixed effects for the following reasons.


Given these characteristics, we use the system GMM estimator, developed by Blundell and Bond (1998), which is well-suited for such panel data. Building on Arellano-Bond's (1991) difference GMM, the Blundell-Bond's system GMM combines equations in differences and levels into a single system. This approach addresses the weak instrumentation problem often faced with difference GMM, particularly when explanatory variables are persistent, while still removing unobserved country-fixed effects by first-differencing (Blundell and Bond, 1998; Roodman, 2009b).

With the system GMM estimation technique, the following specification choices were made based on the characteristics of our data and the post-estimation tests:

\- We use first difference transformation for equations in differences rather than orthogonal deviations. This choice is justified by the fact that the creation of 3-year periods and the use of period averages already produce a panel data structure without gaps.

\- We employ two-step estimators, which are robust to heteroskedasticity and cross-correlation of errors (while we retain the assumption of no cross-sectional correlation across countries).

\- We use Windmeijer-corrected standard errors, which are particularly important for two-step estimation as they improve precision (Windmeijer, 2005) and small sample adjustments.

\- The lagged dependent variable and initial enrolment are treated as predetermined.

\- Financial depth, government consumption, inflation, trade openness and terms of trade are treated as endogenous (since they are potentially correlated with both current and lagged error terms), while disaster variables are assumed to be strictly exogenous.

\- In line with standard practice, GMM-style instruments for the difference equation, start from the first lag of predetermined variables and the second lag of endogenous variables. For each instrument, 3 appropriate lags are used while instruments are collapsed to avoid overfitting.

\- GMM-style instruments for the level equation are the first differences of predetermined variables and lagged differences of endogenous variables. These instruments are also collapsed.

\- The following are the IV-style instruments: disaster variables, interaction terms, (discussed shortly), and period dummies that are included in the respective regressions.

We perform several tests to assess our model specification. First, the Arellano-Bond test for serial correlation is applied. Given the first-difference equations, serial correlation in first differences is expected, so a non-rejection of the null hypothesis for the AR(1) test is consistent with the model. Conversely, rejection of the null hypothesis in the AR(2) test supports the model specification by confirming the absence of second-order serial correlation. Second, the Hansen test is used to evaluate the validity of the instruments, where failure to reject the null hypothesis suggests that the instruments are likely to be valid. We also carefully monitor the instrument count to ensure overfitting is avoided (Roodman, 2009a, 2009b).

Unveiling the impact of disasters on SIDS and their unique vulnerabilities is particularly challenging. While the effect of each explanatory variable for growth in our model may potentially differ between SIDS and non-SIDS, estimating a fully SIDS-specific system GMM model with many variables is not feasible given the limited number of SIDS (only 28 countries). Instead, we isolate SIDS-specific impacts by introducing interaction terms between a SIDS dummy and disaster variables. This allows us to formally test whether disasters have systematically different effects in SIDS compared to other developing countries. This does not imply that the effects of non-interacted control variables are identical in SIDS and non-SIDS, but rather that we adopt a parsimonious specification identifying only the SIDS-specific disaster effect vis-à-vis the average effect across all developing countries. $^{10}$

The SIDS dummy itself is not included in the regression because system GMM already accounts for unobserved country-specific effects and SIDS-specific effects are a subset of these. Moreover, we prefer system GMM over difference GMM because while the SIDS interaction terms are not entirely time-invariant (due to disaster variables), they are partially so because the SIDS dummy itself is time-invariant. Had we used difference GMM, such time-invariant regressors would disappear after differencing.


[[KC_IMAGE_007]]


## 5. Results

The estimation of equation (3) yields the results summarized in Table 4 when using system GMM, and in Appendix Table A.2, when utilizing Ordinary Least Square (OLS) or Within-Group (WG) estimators. Thereafter we will focus on the discussion of system GMM results.

Starting with aggregate disaster variables (columns 1-4), system GMM estimates are in line with Loayza et al (2012): irrespective of the natural disaster metric utilized (frequency or intensity, normalized or not), natural disaster variables display a positive but non-significant coefficient. Among control variables, as expected, the coefficients of government consumption and inflation are negative and highly significant, while the one for trade openness is positive and significant. Neither the lagged dependent variable, nor the remaining controls yield a statistically significant coefficient (broadly similar to Table 2 of Loayza et al (2012), where neither initial output nor education had a statistically significant coefficient). $^{11}$ Moreover, the serial-correlation tests AR(1) and AR(2), as well as the Hansen test, support the specification of the model.

These results remain consistent when the various disaster types are separately included in the regressions (columns 5-8): none of the disaster variables is statistically significant, with droughts being the only disaster type yielding a negative coefficient. Loayza et al. (2012) find a significant negative coefficient for droughts and a positive significant coefficient for floods in their sample of 68 developing countries. We argue that the lack of significance in our results reflects the greater heterogeneity in our sample of 107 developing countries, where different countries exhibit differential effects of disasters.

Table 4


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Period fixed effects are included (coefficients not reported)

To formally tease out SIDS specificities in relation to the disaster-growth nexus, in Table 5 we introduce interaction terms between a SIDS dummy and the relevant disaster variables. This step leaves earlier results qualitatively unchanged in terms of coefficients, significance, and plausibility of the specification, but allows for a formal test of whether SIDS are more adversely impacted by disasters compared to the average developing country. When aggregating all climate-related disasters, the inclusion of the interaction term highlights that SIDS tend to suffer significantly more than the average developing country, when the disaster variables are not normalized (columns 1 and 3); however, this “penalty” becomes insignificant if the intensity of disasters is assessed relative to land or population size (columns 2 and 4). This finding essentially mirrors the visual intuition of Figure 3: the same disaster hitting two countries of widely different size will have a disproportionate impact on the growth trajectory of the smaller one; normalization, however, will obscure this aspect.

Interestingly, the comparison between SIDS and other developing countries becomes more nuanced when climate-related disasters are disaggregated by type, as in columns 5-8. In this respect, the following pattern emerges, irrespective of the metric utilized to capture natural disasters:

1. SIDS's economic growth appears to be significantly less affected by droughts, compared to other developing countries. Besides, the magnitude of related coefficients for SIDS and non-SIDS suggests that the net effect of droughts in the former might be tentatively positive.

2. Conversely, SIDS' growth trajectory tends to be more severely affected by both floods and storms, with an overall net negative impact in both cases. Even after controlling for the standard growth determinants, a 10 per cent increase in the 3-year period average frequency of storms and floods is associated with a 0.1 per cent reduction in SIDS medium-term growth of GDP per capita. This finding is of particular relevance, since – as seen in section 3.2 – floods and storms respectively account for 18 and 71 per cent of all climate-related disasters occurring in SIDS. $^{12}$

Table 5


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Period fixed effects are included (coefficients not reported)

To shed further light on SIDS specificities and on the channels through which disasters affect their economic trajectory, in Table 6 the dependent variable is replaced with the corresponding growth in sectoral value added for agriculture, forestry and fisheries; industry (including construction) and services. $^{13}$ After controlling for the standard growth determinants discussed earlier, we focus here on the comparison between natural disasters' impact on SIDS and other developing countries, across economic sectors and by distinct disaster type.

Droughts have statistically negative effects on non-SIDS developing countries only when using the normalized frequency (as in Table 5), and this can be traced to their adverse impacts on both agriculture and services sectors. Results for droughts suggest that, at least when using intensity measures (normalized or not), in SIDS the services sector tends to be spared from the negative repercussions of droughts. Indeed, the corresponding interaction terms have positive and significant coefficients, whose size exceeds the coefficient for non-SIDS developing countries. Our interpretation of this finding is that, as the primary sector suffers from drought (albeit far less than in other developing countries), activities in the case of SIDS can shift more easily towards the services sector, which is structurally characterized by shallow intersectoral linkages with drought-exposed activities. $^{14}$

As for floods, while they display insignificant coefficients for non-SIDS developing countries, their interaction with the SIDS dummy yields a statistically significant negative impact on industrial value-added growth. Moreover, this finding holds irrespective of the disaster metrics adopted. This indicates that SIDS heightened vulnerability to floods may be largely explained by their damaging impact on industrial growth. Moving to the comparison between the effect of storms on developing countries and SIDS, Table 6 suggests that – irrespective of the disaster metric used – storms take a significantly harder toll on services’ growth in SIDS. Considering the incidence of storms in SIDS, as well as the preponderant contribution of services to their economies, this is arguably the main driver of SIDS’ heightened vulnerability to natural disasters. For instance, even if climate-resilient infrastructure may resist, one could think of the costly disruptions that storms entail for key activities such as tourism, trade and transport, which constitute the backbone of SIDS economies.

Table 6


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Period fixed effects and control variables are included as in Table 5 (coefficients not reported)


# Robustness checks

In this section, we conduct two robustness checks. For each, we replicate Table 5 using alternative specifications. While all variables from Table 5 are included in the regressions, we present only the coefficients for disaster variables and their SIDS interaction terms, due to space constraints and considering that our focus is the SIDS-specific traits of vulnerability. Full regression tables can be found in Tables A.3 and A.4 in the Appendix. For all robustness checks, the Hansen test and Arellano-Bond autocorrelation tests confirm the validity of our model specifications.

## 6.1 Capital Investment

Our first robustness check involves including capital investment as an additional endogenous control variable. The aim is to compare the results in Table 7, part 1 with those in Table 5 to assess whether reconstruction efforts in SIDS mitigate the impact of natural disasters. $^{15}$ Specifically, we ask: are reconstruction efforts “building back better”?

If reconstruction efforts mitigate the impacts of disasters, we expect to observe the following changes:

1. For positive disaster impacts, the coefficient of the disaster variable should decrease, as investment is expected to capture part of the effects of reconstruction activity rather than the disaster itself.

2. For negative disaster impacts, the coefficient should further decrease, as the partly offsetting reconstruction efforts are no longer reflected in the disaster and interaction coefficients, but rather explicitly accounted for through capital investment.

Examining the point estimates of Frequency in Table 7, part 1, including capital investment as a control variable produces the following changes in SIDS:

\- The net effect of all climate-related disasters improves from -0.46 to -0.35.

\- The net effect of droughts decreases from 1.35 to 1.10.

\- The negative impact of floods is lessened, with the net effect improving from -0.75 to -0.43.

\- The net effect of storms remains negative and virtually unchanged, moving slightly from -0.71 to -0.73.

Similar patterns are observed with other metrics, although including capital investment reduces the significance of the coefficients in the regressions using Intensity and Normalized Intensity measures.

For droughts, reconstruction efforts in SIDS appear to reduce the positive effects. However, for all disasters combined and floods, the net impact becomes less negative instead of more negative. If reconstruction efforts were truly effective and if capital formation positively influenced growth, we would expect these coefficients to become more negative, as the direct impact of disasters would be isolated from any positive effects of reconstruction.

The fact that the coefficients become less negative suggests that reconstruction efforts in SIDS are either limited or ineffective in mitigating the negative impacts of disasters. This is likely to reflect structural constraints in SIDS, such as limited financial resources, weak institutional capacity or the scale of destruction relative to the size of their economies, which collectively hinder effective post-disaster recovery. This highlights yet another facet of SIDS' vulnerability.

## 6.2 Subsample Stability

Given concerns regarding the lower quality of EM-DAT data before 2000, we test whether the SIDS differences identified in Table 5 hold across a subsample of post-2000 data.

With fewer observations (533), some significance is lost. However, the signs of the coefficients remain robust and are mostly still significant. The results, presented in Table 7, part 2, confirm that being a SIDS provides a relative advantage when facing droughts but poses a considerable disadvantage when confronted with storms and floods.

Table 7
Robustness Checks. SIDS Interactions, Dependent Variable: GDPpc growth, Estimation Method: System GMM


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Period fixed effects and control variables are included as in Table 5 (coefficients not reported)

# 7. Conclusions

This study reassesses the complex relationship between climate-related disasters and economic growth in developing countries, with the aim of unpacking the specific facets of vulnerability faced by SIDS. It provides a close analysis of different disasters' metrics and their suitability to capture SIDS' specificities. It then formally tests the extent to which SIDS' characteristics translate into a differentiated impact of climate-related disasters compared to other developing countries. The analysis points to four take-away messages.

First, it underscores the need to triangulate various disaster metrics complementarily, and to pay special attention to related normalization practices, in order to fully capture the risks faced by vulnerable countries. Moreover, considering the pervasiveness of data gaps, our analysis also highlights the imperative of scaling up data collection efforts – including through advanced technologies such as satellite imagery – to enhance the monitoring of disasters’ impacts. These efforts are all the more indispensable to ensure the effective working of the recently established Loss and Damage Fund.

Second, using system GMM estimation, this analysis reveals that, even after accounting for standard growth determinants, SIDS experience disproportionately severe medium-term growth setbacks compared to other developing nations. In this respect, we formally test and vindicate the presence of a heightened vulnerability of SIDS to climate-related natural disasters, but this is clearly visible only when using disaster measures that do not mask the effect of smallness, namely those that are not normalized. A key implication, considering that storms account for the lion's share of climate-related disasters hitting SIDS, is that disaster preparedness and climate-resilient infrastructure cannot but be top priorities for SIDS economies.

Third, our study confirms that diverse disaster types entail distinctive shocks on the medium-term growth trajectory of SIDS and other developing countries alike. Hence, detailed and disaggregated assessments of related risks are required not only to ensure adequate preparedness, but also to anticipate potential economic impacts and develop effective economic policy responses.

Last, our study shows that the interplay between disaster patterns and sectoral dynamics plays a fundamental role in shaping related economic shocks on the country's medium-term growth trajectory. In the case of SIDS, whose economies are poorly diversified and highly dependent on volatile services exports (notably through tourism), economic diversification emerges as a key avenue to mitigate the exposure to shocks and build endogenous resilience.

## References

Addison S et al. (2022). Addressing loss and damage: practical insights for tackling multidimensional risks in LDCs and SIDS. International Institute for Environment and Development (IIED). London. (accessed 16 December 2025).

Arellano M and Bond S (1991). Some Tests of Specification for Panel Data: Monte Carlo Evidence and an Application to Employment Equations. The Review of Economic Studies. 58(2):277–297, [Oxford University Press, Review of Economic Studies, Ltd.].

Bănică A, Kourtit K and Nijkamp P (2020). Natural disasters as a development opportunity: a spatial economic resilience interpretation. Review of Regional Research. 40(2):223–249.

Blundell R and Bond S (1998). Initial conditions and moment restrictions in dynamic panel data models. Journal of Econometrics. 87(1):115–143.

Botzen WJW, Deschenes O and Sanders M (2019). The Economic Impacts of Natural Disasters: A Review of Models and Empirical Studies. Review of Environmental Economics and Policy. 13(2):167–188, The University of Chicago Press.

Cavallo E, Galiani S, Noy I and Pantano J (2013). Catastrophic Natural Disasters and Economic Growth. The Review of Economics and Statistics. 95(5):1549–1561, The MIT Press.

Cavallo EA, Becerra O and Acevedo L (2022). The impact of natural disasters on economic growth. Handbook on the Economics of Disasters. Edward Elgar Publishing: 150–192.

Chaudhary MT and Piracha A (2021). Natural Disasters—Origins, Impacts, Management. Encyclopedia. 1(4):1101–1131.

Coronese M, Lamperti F, Keller K, Chiaromonte F and Roventini A (2019). Evidence for sharp increase in the economic damages of extreme natural disasters. Proceedings of the National Academy of Sciences. 116(43):21450–21455.

Coulibaly T, Islam M and Managi S (2020). The Impacts of Climate Change and Natural Disasters on Agriculture in African Countries. Economics of Disasters and Climate Change. 4(2):347–364.

Cuaresma JC (2022). Natural disasters and economic growth: revisiting the evidence. Handbook on the Economics of Disasters. Edward Elgar Publishing: 134–149.

De Oliveira VH (2018). Natural disasters and economic growth in Northeast Brazil: evidence from municipal economies of the Ceará State. Instituto de Pesquisa e Estratégia Econômica do Ceará (IPECE). Fortaleza: 271–293.

Delforge D et al. (2023). EM-DAT: the Emergency Events Database December. Available at https://www.researchsquare.com/article/rs-3807553/v1 (accessed 9 December 2024).

Durlauf SN, Johnson PA and Temple JRW (2005). Chapter 8 Growth Econometrics. In: Aghion P, and Durlauf S N, eds. Handbook of Economic Growth. Elsevier: 555–677.

Ehlers T, Frost J, Madeira C and Shim I (2025). Macroeconomic impact of weather disasters: a global and sectoral analysis. BIS Working Papers. BIS Working Papers, Bank for International Settlements.

Felbermayr G and Gröschl J (2014). Naturally negative: The growth effects of natural disasters. Journal of Development Economics. Special Issue: Imbalances in Economic Development. 11192–106.

Fomby T, Ikeda Y and Loayza NV (2013). The growth aftermath of natural disasters. Journal of Applied Econometrics. 28(3):412–434, John Wiley & Sons, Ltd.

Hallegatte S, Hourcade J-C and Dumas P (2007). Why economic dynamics matter in assessing climate change damages: Illustration on extreme events. Ecological Economics. Special Section: Ecological-economic modelling for designing and evaluating biodiversity conservation policies. 62(2):330–340.

Hochrainer S (2009). Assessing The Macroeconomic Impacts Of Natural Disasters: Are There Any? Policy Research Working Paper No. 4968. The World Bank. Washington DC. (accessed 7 December 2024).

IPCC (2022). AR6 Climate Change 2022: Impacts, Adaptation and Vulnerability. IPCC. (accessed 10 March 2022).

Ishizawa OA and Miranda JJ (2019). Weathering Storms: Understanding the Impact of Natural Disasters in Central America. Environmental and Resource Economics. 73(1):181–211.

Islam N (1995). Growth Empirics: A Panel Data Approach. The Quarterly Journal of Economics. 110(4):1127–1170, Oxford University Press.

Loayza NV, Olaberría E, Rigolini J and Christiaensen L (2012). Natural disasters and growth: Going beyond the averages. World Development. 40(7):1317–1336.

MacFeely S, Peltola A, Barnat N, Hoffmeister O and Hopp D (2021). Constructing a criteria-based classification for Small Island Developing States: an investigation. UNCTAD Research Paper No. 66. UNCTAD. Geneva. (accessed 18 May 2021).

Naoaj MS (2023). From Catastrophe to Recovery: The Impact of Natural Disasters on Economic Growth in Developed and Developing Countries. European Journal of Development Studies. 3(2):17–22.

Nijkamp P and Borsekova K, eds. (2019). Resilience and Urban Disasters: Surviving Cities. New horizons in regional science. Edward Elgar Publishing. Cheltenham, UK; Northampton, MA, USA.

Noy I (2009). The macroeconomic consequences of disasters. Journal of Development Economics. 88(2):221–231.

Onuma H, Shin KJ and Managi S (2021). Short-, Medium-, and Long-Term Growth Impacts of Catastrophic and Non-catastrophic Natural Disasters. Economics of Disasters and Climate Change. 5(1):53–70.

Panwar V, Wilkinson E and Noy I (2024). The price of a changing climate: extreme weather and economic loss and damage in SIDS. ODI Policy Brief. Overseas Development Institute. London. (accessed 16 December 2025).

Park SK and Samples TR (2024). The sovereign climate debt trap and natural disaster clauses. American Business Law Journal. 61(4):243–260.

Raddatz C (2009). The Wrath Of God: Macroeconomic Costs Of Natural Disasters. Policy Research Working Papers, The World Bank.

Roodman D (2009a). A Note on the Theme of Too Many Instruments. Oxford Bulletin of Economics and Statistics. 71(1):135–158.

Roodman D (2009b). How to do Xtabond2: An Introduction to Difference and System GMM in Stata. The Stata Journal. 9(1):86–136, SAGE Publications.

Roth Tran B and Wilson D (2024). The Local Economic Impact of Natural Disasters. Federal Reserve Bank of San Francisco, Working Paper Series. Federal Reserve Bank of San Francisco. 1.000-61.

Skidmore M (2022a). A taxonomy of natural disasters. Handbook on the Economics of Disasters. Edward Elgar Publishing: 13–28.

Skidmore M (2022b). Handbook on the Economics of Disasters. Edward Elgar Publishing. Cheltenham, UK; Northampton, MA, USA.

Skidmore M and Toya H (2002). Do Natural Disasters Promote Long-Run Growth? Economic Inquiry. 40(4):664–687.

Slany A (2020). Multiple disasters and debt sustainability in Small Island Developing States. UNCTAD Research Paper No. 55. UNCTAD. Geneva. (accessed 9 December 2024).

Tandrayen-Ragoobur V, Moncada S and Fauzel S, eds. (2026). Environmental and Socioeconomic Vulnerabilities and Resilience in Small States. Europa International Perspectives. Routledge. Abingdon.

UNCTAD (2022). The Least Developed Countries Report 2022: The Low-Carbon Transition and Its Daunting Implications for Structural Transformation. United Nations publication. Sales No. E.22. II.D.40. New York and Geneva.

UNCTAD (2023). The Least Developed Countries Report 2023: Crisis-Resilient Development Finance. United Nations publication. Sales No. E.23.II.D.27. New York and Geneva.

United Nations (2024a). Handbook on the Least Developed Country Category: Inclusion, Graduation and Special Support Measures. UN Department of Economic and Social Affairs, United Nations. New York.

United Nations (2024b). High level panel on the development of a Multidimensional Vulnerability Index - Final report. United Nations. New York.

Windmeijer F (2005). A finite sample correction for the variance of linear efficient two-step GMM estimators. Journal of Econometrics. 126(1):25–51.


## APPENDIX.

Table A.1
Descriptive statistics of disaster variables included in the regressions


Table A.2


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Period fixed effects are included (coefficients not reported)

Table A.3


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Period fixed effects are included (coefficients not reported)


## Table A.4


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Period fixed effects are included (coefficients not reported)

@UNCTAD
@UNCTAD
unctad.org/facebook
unctad.org/youtube
unctad.org/flickr
unctad.org/linkedin
