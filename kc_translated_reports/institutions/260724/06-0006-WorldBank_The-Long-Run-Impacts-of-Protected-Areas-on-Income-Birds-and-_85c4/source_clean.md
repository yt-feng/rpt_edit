# The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa
## Abstract

Protected areas cover $17\%$ of the world's land surface, yet credible evidence on their long-run economic and ecological impacts remains scarce. This paper estimates the effects of South Africa's protected areas on household income, bird biodiversity, and tourism consumer surplus. For the income and biodiversity analyses, it develops a machine-learning counterfactual approach that recovers the present-day impacts of protected areas created up to 100 years ago. Short-run impacts of newer protected areas are small and statistically insignificant, while older protected areas generate large gains. Prior research may have severely underestimated the benefits of protected areas by only estimating the short-run effects of newly established protected areas. In aggregate, this paper estimates that protected areas increase annual household income by approximately R300 billion (roughly 10% of 2011 GDP). This yields approximately 7.6 million job-equivalents attributable to South Africa's protected areas. Different types of protected areas play complementary roles in conserving different categories of threatened birds, demonstrating the value of South Africa's entire protected area network. A structural travel cost model estimates that South Africa's national parks generate R7.7 billion per year (2023 rand) in recreational value for domestic and international tourists. These results suggest that in South Africa there is little tradeoff between wildlife conservation and economic development. Realizing the economic and ecological benefits of protected areas, however, requires patience: returns to conservation accumulate over decades, not years.


# The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa\*

Dennis Engist $^{\dagger}$ Gabriel Englander $^{\ddagger}$ Alan Lee $^{\S}$ Frederik Noack $^{\P}$

Authorized for distribution by Florence Kondylis, Research Manager, Development Research Group, Development Economics, World Bank Group

JEL classi ication: Q56, Q57, Q26, O13, C21

Keywords: Protected areas, Household income, Biodiversity conservation, Tourism, South Africa

## 1 Introduction

Protected areas are the principal instrument for conserving biodiversity (Gurney et al., 2023; Watson et al., 2014). Collectively spanning more than $17\%$ of the world's land surface, they represent one of the largest deliberate allocations of land to a single policy objective, with potentially far-reaching consequences for the economies of surrounding communities (UNEP-WCMC and IUCN, 2024). Yet robust causal evidence on their economic and ecological consequences remains limited. Because protected areas are typically established in locations with high biodiversity or low economic opportunity costs, simple correlations between protection, biodiversity, and development outcomes are prone to selection bias and reverse causality. While protected areas such as national parks contribute to human well-being through recreational opportunities, tourism revenue, and biodiversity benefits, they may also impose substantial economic costs by restricting local land use and limiting resource extraction (Bahrami, Gustafson, and Steiner, 2025).

These concerns raise a central policy dilemma. Governments may optimally locate protected areas in regions where conservation is inexpensive, but where biodiversity benefits and economic spillovers are limited (Pfaff et al., 2015; Grupp et al., 2023). This challenge is particularly acute because many global biodiversity hotspots are concentrated in developing and emerging economies, where conservation competes directly with poverty reduction and economic development objectives (Myers et al., 2000). Understanding whether protected areas simultaneously promote biodiversity conservation and local economic welfare is therefore critical for global conservation policy.

We study these questions in South Africa, one of the world's most biologically diverse countries and a globally recognized biodiversity hotspot. South Africa hosts exceptional levels of plant, bird, and invertebrate diversity and supports iconic megafauna including elephants, lions, and rhinoceroses. The country maintains an extensive protected area network, covering approximately $11\%$ of its terrestrial land surface and consisting of national parks, provincial nature reserves, and a rapidly expanding system of private conservation areas (Figure 1). Despite well-developed management systems, many protected areas face pressures from poaching, land encroachment, and surrounding economic deprivation, potentially limiting conservation effectiveness.

South Africa simultaneously faces severe socio-economic challenges, including high unemployment and persistent inequality. Nature-based tourism represents a major economic sector, with protected areas serving as key attractions. Protected areas contribute to human well-being through tourism revenues accruing to local communities and substantial recreational consumer surplus enjoyed by domestic and international visitors. Biodiversity spillovers may further affect surrounding communities through ecosystem services and wildlife-related damages (Gulati et al., 2021; Noack, Engist, and Larsen, 2025). Conversely, conservation restrictions may constrain agricultural expansion and resource-based livelihoods in rural regions. Whether protected areas alleviate or exacerbate local economic challenges, therefore, remains an open empirical question.

Quantifying the causal impacts of protected areas is difficult because protection is not randomly assigned. Standard approaches in economics rely on two-way fixed effects (TWFE) designs that compare outcomes before and after protected area establishment relative to contemporaneous changes in outcomes in non-protected areas. However, many of the world's most important protected areas were established decades before modern socio-economic and biodiversity data became available. For example, Kruger National Park was formally established in 1926. Consequently, TWFE approaches primarily identify short-run impacts of newly-established protected areas and implicitly assume that conservation effects do not evolve over time and that older and newer protected areas are comparable.


[[KC_IMAGE_001]]

Figure 1: A map of South Africa with protected areas in green, national parks labelled in black, and major cities labelled in blue.

To overcome these limitations, we develop a complementary identification strategy grounded in the literature on economic geography and long-run development. We assemble a spatial dataset of pre-protection geographic variables that are known to shape long-run economic outcomes (Gollin, Parente, and Rogerson, 2002; Bleakley and Lin, 2012; Nunn and Puga, 2012; Dell, Jones, and Olken, 2012; Jedwab and Moradi, 2016; J Vernon Henderson et al., 2018; Donaldson, 2018), consisting of predictors of economic activity determined before the establishment of South Africa's first national park. These variables include historical railway networks, early twentieth-century economic agglomerations, climatic conditions, agricultural suitability, and terrain ruggedness.

Using machine-learning prediction algorithms trained exclusively on locations distant from protected areas, we estimate counterfactual household income based solely on pre-protection characteristics. This counterfactual prediction represents what income would have been in the absence of protected areas. Comparing predicted and observed incomes allows us to recover both short- and long-run economic impacts of protected areas. We apply the same framework to bird biodiversity outcomes while incorporating additional ecological predictors such as ecoregions.

We find that protected areas generate positive long-run economic and ecological effects. Old protected areas significantly increase local household income, while recently established protected areas exhibit small and statistically insignificant short-run impacts. National parks produce larger income gains than other types of protected areas. Simultaneously, protected areas preserve threatened bird species and shift bird communities toward species reliant on intact natural habitats. Finally, a key motivation for establishing protected areas, including national parks, is their contribution to human well-being through recreational value. Visitors derive enjoyment that is not fully captured by entrance fees but is at least partially reflected in their willingness to travel long distances to visit a protected area. These benefits may be substantial, as they are a direct and intended consequence of establishing protected areas. We use a structural travel-cost model to estimate that South Africa's national park system generates approximately R7.7 billion annually in tourism consumer surplus, with domestic visitors capturing roughly one-quarter of the total.

The concordance between our machine-learning counterfactual approach and conventional TWFE estimates is reassuring, but the larger effects estimated for long-established protected areas could still reflect spatial selection into conservation. That is, early planners may have preferentially protected locations with inherently higher economic or ecological potential. We test this selection concern directly using predicted counterfactual outcomes based solely on pre-protection characteristics. We find no evidence that older protected areas were placed in more favorable locations, which suggests that their larger impacts primarily reflect dynamic processes that unfold over decades.

A growing interdisciplinary literature evaluates the impacts of protected areas on development and conservation outcomes (Sims, 2010; Ferraro and Hanauer, 2014; Andam et al., 2010; Pfaff et al., 2015; Grupp et al., 2023; Geldmann et al., 2013; Gray et al., 2016; Denny, Englander, and Hunnicutt, 2024; Baylis, Garcia, and Heilmayr, 2026). Our paper contributes to this literature by jointly quantifying economic, biodiversity, and recreational welfare impacts within a unified causal framework—an integration that prior analyses have not attempted. More fundamentally, the existing literature predominantly relies on short-run variation in protection status. Our findings suggest that this risks substantially underestimating the long-run benefits of conservation.

Taken together, our results suggest that protected areas can simultaneously enhance biodiversity conservation and generate substantial economic benefits. These findings provide cautious optimism that biodiversity-rich emerging economies can leverage conservation investments to support both ecological sustainability and economic development.

## 2 Household Income

We estimate the impact of South African protected areas on household income using data from the South African census, which provides monthly household income for 4,277 electoral wards in 2001 and 2011 (Statistics South Africa, 2011a). South Africa did not release income data from its 2021 census or from censuses before 2001 at the ward level. This narrow temporal window of 2001 to 2011 illustrates the limits of TWFE models in this setting: they only allow estimation of short-term effects of the small number of protected areas established in this period. For this reason, we complement the TWFE panel estimation with a cross-sectional regression and a machine learning approach to capture the long-term effects of the full protected area network.

In all models and specifications, we use log-transformed total household income per ward as the outcome. We use total rather than per capita income to capture not only individual income gains, but also the aggregate economic effects of labor migration. Our treatment variables are the log-transformed area (in square meters) of protected areas within the ward and, separately, within a 15 km buffer surrounding the ward. We select 15 km as the buffer distance because the average ward area of $285 \, km^2$ corresponds roughly to a square with 15 km sides, so the buffer extends spillover detection to approximately one ward-length beyond each ward's boundary. This specification allows us to capture both the direct local impacts of protected areas and the spatial spillover effects on neighboring communities. In the cross-sectional and machine learning estimations, we further subset the treatment variable in three ways: all protected areas pooled together, national parks versus other types of protected areas, and protected areas separated into age groups by the year in which they were established. To correct for spatial autocorrelation and generated regressors, we calculate standard errors using spatial block bootstrapping across all models. Specifically, because our machine learning approach relies on predicted counterfactuals as inputs, standard analytical errors would ignore the sampling variation from this first-stage estimation and artificially deflate our confidence intervals. By resampling spatial blocks and re-estimating the entire procedure for each draw, the bootstrap accurately accounts for both local spatial dependence and the additional uncertainty introduced by the generated regressors.

In the TWFE model, the treatment exposure of electoral wards is restricted to the protected areas established from 2002 to 2011, with 2001 serving as the baseline. Year and ward fixed effects (i.e., binary variables for each year and each electoral ward) absorb annual income shocks common across all wards and all time-invariant differences between wards, respectively. The resulting estimates stem from comparing the change in income from 2001 to 2011 between electoral wards with different levels of expansion of protected areas. To avoid further limiting the sample, in the TWFE approach we only estimate the pooled specification, grouping all protected areas together.

To estimate the long-term effects of the full set of protected areas, we deploy two distinct strategies. First, we use the household income data as a repeated cross-sectional outcome in an Ordinary Least Squares (OLS) linear regression, controlling for an extensive set of covariates. These covariates are not determined by protected areas; they consist of environmental characteristics (e.g., temperature, elevation, ruggedness, distance to rivers) and historical infrastructure (e.g., distance to railways in 1925, distance to metropolitan centers in 1921 — see Figure B.1). By explicitly controlling for these determinants of income, we absorb differences in economic potential across wards. This approach relies on the assumption that, conditional on these controls, the placement of protected areas is quasi-random, so that the residual variation explained by the protected area treatment variables is the causal effect of protected areas on income. Importantly, this assumption does not require that the controls capture all determinants of household income—only that they are sufficient to render the placement of protected areas uncorrelated with unobserved determinants of income.

Second, we apply the same core logic using a more sophisticated machine learning approach. Rather than using the environmental and historical variables simply as linear controls, we train an XGBoost algorithm to predict household income based on these variables. Crucially, we train it only on untreated electoral wards: those that are located, on average, more than 15 km away from the nearest protected area and do not contain any protected areas (see Figure B.2 for a map of training wards). We then use the trained model to predict income for all wards, which yields a counterfactual income level in the absence of protected areas (see Tables C.1 and C.2 and Figure B.3 for XGBoost model parameters and out-of-fold performance of the income and nightlights predictions). We achieve out-of-fold $R^{2}$ -values of 0.34 for household income prediction, and 0.3 for nighttime lights. While traditional in-sample spatial regressions demonstrate that fundamental geographic characteristics can explain up to 35% of the within-country variation in economic activity (J Vernon Henderson et al., 2018), an out-of-fold $R^{2}$ of 0.34 is robust and aligns with the performance of established spatial machine learning applications predicting local economic well-being (Yeh et al., 2020). The difference between observed and predicted income is then regressed on our protected area treatment variables. As in the cross-sectional linear approach, we run separate estimations for all protected areas, protected areas by type, and protected areas by age group.

Across both the cross-sectional regression and machine learning approaches, we find positive and statistically significant effects of protected areas on household income (Figure 2, left panel titled “All”; see Table C.3, C.4, C.5, C.6, C.7, and C.8 for full income and nightlights regression output tables). An additional 1% of protected area within an electoral ward leads to an approximately 0.2% increase in income, while an additional 1% of protected area in the 15 km buffer surrounding the ward leads to a 0.1% increase in income. When separating the effects by type, we observe consistently positive impacts from both national parks and other protected areas (middle panel titled “Type”). The machine learning estimation reveals a particularly striking spatial pattern for national parks: while proximity to a national park generates highly positive spillover effects (up to a 0.25% income increase per additional 1% of protected area in the 15 km buffer), there is a smaller or null effect from having a national park inside the ward itself, depending on the model.


[[KC_IMAGE_002]]

Figure 2: The effect on monthly household income of all protected areas (left panel), of protected areas by type (middle panel), and of protected areas by age (right panel). Coefficient estimates as dots, 90% confidence intervals in dark color, and 95% confidence intervals in light color. Orange (“Ward”) represents effect of protected areas located inside a ward; purple (“Buffer”) represents effect of protected areas located in a 15 km buffer area surrounding each ward. Squares indicate results from the panel TWFE approach, circles the results from the cross-sectional linear regression (OLS), and diamonds the machine learning (ML) approach.

As we move from the oldest to the youngest groups of protected areas (right to left), the coefficients tend to decrease in magnitude and statistical significance. The youngest group (protected areas established between 2002 and 2011) is the only treatment variable that permits direct comparison between the cross-sectional, ML, and TWFE approaches (see Table C.9 for full income and nightlights TWFE regression output tables). Tellingly, none of the estimated effects for these recently established protected areas are significantly different from zero. This confirms that empirical analyses constrained to the short time horizons of modern outcomes data likely underestimate the long-run economic benefits of conservation.

To corroborate these findings, we estimate the identical specifications using nightlight density as an alternative proxy for local economic activity (J. Vernon Henderson, Storeygard, and Weil (2012), see Figure B.4 for results). Overall, the nightlight estimates align well with the household income results. Most notably, the nightlight data confirms the overall positive effect of protected areas, as well as both the lack of short-term impacts for the most recently established protected areas (2002 and later) and the increasing effect size with protected area age. However, there are some notable differences. For example, the effect of the oldest protected areas in the buffer and ward only partially replicate the pattern observed in the income estimation. This might be due to nightlights imperfectly proxying for household income, particularly in rural areas. Still, the general consistency across two independent measures of economic well-being reinforces the robustness of the estimated long-run economic effects of protected areas.

To estimate the aggregate economic contribution of South African protected areas to household income, we calculate the difference between observed income and the counterfactual income (without protected areas) for each ward across all cross-sectional regression and machine learning specifications (Figure 3). Averaging these differences across specifications and summing them nationally, we estimate that protected areas generated R25.3 billion in monthly household income in 2011. This translates to an annual contribution of approximately R303 billion, representing about $10\%$ of South Africa's nominal GDP of R3 trillion in 2011 (Statistics South Africa, 2011b). One point of comparison for our aggregate estimate is the World Travel and Tourism Council's estimate, based on national accounting data, that the tourism industry contributed $8.2\%$ of South Africa's GDP in 2023 (World Travel and Tourism Council, 2024). Our estimate captures the impact of protected areas on household income through all channels, including but not limited to tourism.

Following the World Bank's More and Better Jobs methodology (World Bank Group, 2026), we divide the additional R303 billion in income by the average annual wage among employed workers in our data (R40,025) to express it in job-equivalents. This yields approximately 7.6 million job-equivalents attributable to South Africa's protected area network—a labor-market-scaled measure of the employment that the associated income flow would sustain at prevailing local wages.


[[KC_IMAGE_003]]

Figure 3: The monthly household income contribution of South African protected areas in billions of 2011 rand (R), calculated using different methods (shapes) and specifications (grey shading). Circles indicate results from the cross-sectional linear regression (OLS) and diamonds the machine learning (ML) method. Horizontal line indicates average contribution across models and specifications.

## 3 Bird Biodiversity

We estimate the impact of protected areas on bird diversity using bird observation data from the Southern African Bird Atlas Project 2 (SABAP2) (Brooks et al., 2022). This citizen science project collects bird presence data across South Africa, as well as Lesotho, Eswatini, Namibia, Botswana, Zimbabwe and Mozambique. It has been running since 2007, which we set as the beginning of our analysis period. In the data, Southern Africa is divided into $5 \times 5$ arc minute rectangles (approx. $9 \times 9$ km) referred to as pentads. Within these pentads, volunteers record species seen during the observation period on observation cards. Here, we use only full protocol cards, which require the observer to follow specific rules like a minimum observation time of two hours, recording all species present, and requiring good birding conditions and a minimum skill level. Full protocols allow researchers to infer both the presence and absence of species. These observation cards are publicly available. In total, we use 292,974 full-protocol cards, distributed roughly evenly between 2007 and 2025 (see Figures B.5 and B.6 for spatial and temporal distribution of cards).

We define the treatment variable as the share of protected area per pentad per time period, and match these treatment exposures to the observation cards. We calculate the observed species richness for each card across four International Union for Conservation of Nature (IUCN) threat levels: critically endangered and endangered (CR+EN, combined due to rarity), vulnerable (VU), near threatened (NT), and least concern (LC). We further split LC species into urban avoiders and urban adaptors (see Tables C.10, C.11, C.12, C.13, C.14, and C.15 for a complete list of species in each category). Urban avoiders are birds whose presence tends to decline with increased levels of development and for which towns, suburbs and heavily built-up areas reduce habitat quality or suitability. On the other hand, urban adaptors are species that are able to use, tolerate, or benefit from urban and developed environments (Lee, Jackson, and Reynolds, 2021). Because the observation effort of SABAP2 volunteers, the timing of their observations, and their experience levels vary across cards, we adjust species richness using a negative binomial regression. This regression controls for hours observed, total cards submitted by the observer, month, and hour of the day. The residuals from this regression serve as our primary outcome variable (see Figures B.7, B.8, B.9, and B.10 for species distribution and effort bias adjustments). Like in the income estimation, we use spatial block bootstrapping to calculate standard errors over all estimation steps, as the sampling variation from effort adjustment (and machine learning prediction) would be ignored otherwise and artificially reduce the confidence intervals.

Before proceeding to formal estimations, the spatial distribution of the raw pentad-level adjusted species richness already reveals striking geographic patterns. The positive impact of large protected areas on biodiversity is visually apparent without statistical modeling. For instance, Kruger National Park exhibits a stark contrast in adjusted species richness compared to its immediate surroundings (see Figure B.11). Furthermore, aerial imagery of the park's western boundary reveals a sharp discontinuity in land cover that aligns perfectly with the park's borders, confirming that these regional biodiversity differences are driven by conservation boundaries and anthropogenic land-use changes rather than natural ecological gradients alone (see Figure B.12).

To estimate the impact of protected areas on bird biodiversity, we broadly follow the methodology used for the income estimation. As in the income analysis, we use a TWFE model to estimate the short-term impacts of newly-established protected areas and a cross-sectional OLS regression and machine learning approach to estimate the long-term impacts of the entire protected area network. While the income data is limited to 2001 and 2011, the SABAP2 data covers the period 2007 to 2025, which includes more newly-established protected areas to provide treatment variation for the TWFE estimation. The outcome variables are adjusted species richness by IUCN threat level (with LC species divided into urban avoiders and urban adaptors), and the treatment is the share of protected areas over time, controlling for year and pentad fixed effects.

For the cross-sectional approach, we estimate an OLS regression controlling for spatial ecoregions in addition to all the covariates from the income estimation (see Figure B.13). Spatial ecoregion classifications account for macro-environmental constraints, such as climate, topography, and broad vegetation structures as defined by the South African Department of Water Affairs and Forestry (Kleynhans, Thirion, and Moolman, 2005). These variables are key predictors of avian biodiversity (Betts et al., 2019; Fink et al., 2020). We perform separate analyses pooling all protected areas together, separating national parks from other types of protected areas, and separating protected areas into age groups. The newest age cohort aligns with the TWFE panel period. Adjusted species richness by IUCN threat category remains the outcome.

For the machine learning approach, we train an XGBoost model to predict adjusted species richness per pentad. Consistent with the income estimation, we train the model exclusively on never-treated units—defined here as pentads with a centroid located more than 10 km from any protected area (approximately one pentad-length). Figure B.14 displays the training pentads. We then predict baseline richness for all pentads and calculate the difference between the card-reported adjusted richness and the prediction (see Tables C.16, C.17, C.18, C.19, and C.20, as well as Figure B.15 for XGBoost model parameters and out-of-fold performance of IUCN category-specific predictions). This difference serves as the outcome variable in regressions on all (pooled) protected areas, as well as protected areas by type, age, management, and size cohort. The out-of-fold predictive performance of the XGBoost models varies with species prevalence. The models achieve strong $R^{2}$ values of 0.52 and 0.56 for least concern urban adopters and urban avoider species, demonstrating that our geographic covariates successfully capture the fundamental carrying capacity of these environments. Conversely, predictive power is lower for highly threatened categories (e.g., $R^{2} = 0.09$ for critically endangered and endangered species), reflecting the inherent stochasticity, zero-inflation, and localized micro-habitat dependencies of rare species.

We further analyze how differences in protected area management affect bird biodiversity using a land cover-change based indicator as an objective measure of protected area performance. Because formal management assessments (such as METT) are sparse and rely on subjective reporting, the observed conversion of natural to artificial surfaces provides an independent metric for evaluating a protected area's effectiveness at resisting anthropogenic pressures (Geldmann et al., 2019). Protected areas with a low share of change (below the median) from natural to artificial surfaces between 2014 and 2020 are classified as high management effectiveness, whereas protected areas with a high share (above the median) of land cover change are classified low management (see Figure B.16 for map of protected areas by land cover management index). In addition, we test the impact of protected area size by estimating separate effects by surface area quartile.

Protected areas positively impact threatened species and urban avoiders, while negatively impacting urban adaptor species. Figure 4 presents the estimated effects by threat level and protected area group (see Tables C.21, C.22, C.23, C.24, C.25, C.26, and C.27 for full bird biodiversity regression output tables). For critically endangered and endangered species (CR+EN, first row), the effect is statistically significant and positive. This result is driven by protected areas established before 1977, and particularly those established before 1953. Medium-aged protected areas show no significant effect on this group, though they do positively affect vulnerable and near threatened species. National parks are highly effective at preserving endangered species but play a smaller role than other protected areas in supporting vulnerable and near threatened populations.

Protected areas also positively impact least concern species that struggle in urban and developed enenvironments (LC Urban Avoiders, fourth row). Conversely, protected areas negatively affect least concern species that are adaptable to urban and developed environments (LC Urban Adaptors, last row). Since these adaptable generalists tolerate anthropogenic land-use changes, their reduced presence inside protected areas aligns with conservation goals to prioritize the protection of specialized and sensitive natural habitats.

Consistent with the income estimation, the newest protected areas exhibit minimal impact across all species groups, and coefficients align closely between the three models. This again underscores how the dominant empirical approach in the literature may underestimate the long-run effects of protected areas.

Analyzing the effect of management effectiveness, we find that generally, protected areas with low loss of natural surface area have a more positive impact on threatened species and urban avoiders and a more negative impact on urban adaptors (see Figure B.17 and Tables C.28 and C.29 for full results). However, this pattern does not always hold, as near-threatened species benefit more from low management protected areas.

Finally, we estimate the effect by size of protected areas. We find that most of the effect is driven by large and very large protected areas (i.e., protected areas of above-median size; see Figure B.18 and Tables C.30 and C.31 for full results).


[[KC_IMAGE_004]]

Figure 4: The effect on bird species richness of all protected areas (left panels), protected areas by type (middle panels) and protected areas by age (right panels). Bird species richness is calculated by IUCN threat level: critically endangered and endangered (CR+EN, red), vulnerable (VU, orange), near threatened (NT, light green), least concern urban avoiders (LC Urban Avoiders, dark green), and least concern urban adaptors (LC Urban Adaptors, darkest green). Coefficient estimates as dots, 90% confidence intervals in dark color, and 95% confidence intervals in light color. Coefficients represent the estimated increase in the number of species present in that category. Squares indicate results from the panel TWFE approach, diamonds the results from the cross-sectional linear regression (OLS), and circles the results from the machine learning (ML) approach.

## Case Study: Addo Elephant National Park and Great Fish River Nature Reserve

Established in 1931, Addo Elephant National Park (Addo) is one of South Africa's oldest protected areas. Originally set up to protect the remaining 11 elephants in Addo, it is now famous for hosting the “Big 5” species (elephant, buffalo, rhino, leopard, and lion) and a range of other wildlife (South African National Parks, 2025a). Today, it covers 1,640 km $^{2}$ , not counting a marine protected area that also hosts whales and sharks, making Addo the only protected area in South Africa where visitors can find the complete “Big 7”.

Great Fish River Nature Reserve (Great Fish) is a protected area in Eastern Cape Province. It is made up of the Andries Vosloo Kudu Reserve, the Sam Knott Reserve, and the Double Drift Reserve, covering more than $450 \, km^2$ . It hosts a large number of mammals like antelopes, buffalos, jackals and leopards, and is also a popular bird watching spot with over 247 bird species present (Siyabona Africa, 2025).

In addition to their conservation value, these protected areas provide multiple economic benefits to local communities. Tourism is a major source of revenue, not only through accommodations and entrance fees but also activities like game-watching tours. Great Fish provides additional income sources, like the local sale of harvested wildlife meat.


[[KC_IMAGE_005]]

Figure 5: The income contribution of Addo Elephant National Park and Great Fish River Nature Reserve (2011 rand). Circles indicate results from the cross-sectional linear regression (OLS) and diamonds the machine learning (ML) method. Grey shadings indicate results from different specifications. Results are further disaggregated by whether the protected area is treated as the first in its area (“First Mover”) or as an additional protected area alongside existing ones (“Marginal”). The horizontal lines and blue text in each figure indicate the average contribution across all methods and specifications.

We estimate the localized impact of Addo and Great Fish on household income using the coefficients from our national analysis (Section 2). By applying these estimates to the specific ward-level and 15 km buffer exposures of these parks, we calculate their distinct income contributions. We report these values under two assumptions: treating the park as the sole protected area in the region (“First Mover”) versus treating it as an addition to the existing conservation network (“Marginal”).

For Addo, we estimate a contribution of approximately R57.8 million (2011 rand) to the monthly income of surrounding communities (Figure 5). An earlier study from 1995 estimated the total yearly tourism impact of Addo to be between US\$83 and 110 million, which broadly aligns with the magnitude of our estimate (Kayser, Sobrevila, and Ledec, 2011). Our estimate implies that Addo directly and indirectly accounts for roughly 19% of local income. For Great Fish, the estimated contribution is approximately R9.2 million per month, representing about 14% of total income in nearby communities.

Both protected areas also play critical roles in preserving threatened avian populations. Applying our national biodiversity estimates from Section 3, we find that Addo and Great Fish support significantly higher richness of threatened and urban avoider bird species compared to surrounding unprotected areas (Figure 6). Addo, in particular, encompasses massive tracts of pristine habitats—ranging from thick inland bush and old-growth forests to undisturbed coastal dunes—that provide essential refuge for globally threatened and range-restricted species unable to persist in heavily modified or disturbed landscapes.


[[KC_IMAGE_006]]

Method ● OLS ◆ ML Specification ● All ● Type ● Age

Figure 6: The contribution of Addo and Great Fish to bird species richness by threat level, with least concern (LC) split into urban avoiders and urban adaptors. Dots indicate calculations from different models and specifications. Horizontal lines indicate the overall mean by protected area and species group; the value displayed above each line is the estimated increase in the number of species present in that category.

Finally, Section 4 estimates the collective recreational value of South Africa's national parks (other protected areas are not included in this analysis due to limited data). It also calculates the loss in recreational value if Addo were removed from the park system, but all other national parks continued to welcome visitors. By this measure, Addo generates R887 million per year (2023 rand) in tourism consumer surplus. This benefit that tourists receive from having access to Addo is comparable in size to the income gains that Addo delivers to nearby households—roughly R1.3 billion (2023 rand), or R62 million per month (2011 rand) as reported above (Statistics South Africa, 2026).

## 4 Tourism Consumer Surplus

To estimate the recreational value of South Africa's national parks to visitors, this study applies a travel cost discrete choice model to administrative visitor data from the South African National Parks agency. The data contain the number of visitors to each of 19 national parks, from 253 origin countries and territories and 9 South African provinces, in each year from 2012 through 2024. Other non-national-park protected areas are excluded from this analysis, as comparable visitation data by origin are not available. The analysis begins by computing the least-cost travel route for each origin–park-year combination, accounting for international and domestic airfares, fuel costs, car rental, the value of travel time, and park entry fees—approximately 2.1 million route options for international visitors and 100,000 for domestic visitors. Because travel costs vary across origins, parks, and years, the model can estimate how sensitively visitors respond to the price of reaching a park. Consumer surplus—the difference between what potential visitors would be willing to pay for access to the park system and the costs of reaching and entering it—captures the net recreational value of that access. For example, visitors who travel long distances at great expense reveal a high willingness to pay for access, and thus a large consumer surplus.

(a) Marginal value of each park


[[KC_IMAGE_007]]

(b) Domestic consumer surplus by province


[[KC_IMAGE_008]]

(c) Consumer surplus by country of origin
Figure 7: Tourism consumer surplus from South African national parks. Panel (a) shows the marginal consumer surplus from each park, calculated by removing it from the choice set. Panels (b) and (c) show total consumer surplus from access to all parks, by South African province and by country of origin, respectively. All values are annual averages over the period 2012–2024, expressed in millions of 2023 rand (R). In panel (c), data are missing for Guinea, Kosovo, and South Sudan. Province and country boundaries from World Bank (2025b) and World Bank (2025a).

The model estimates visitor demand as a function of travel cost using a discrete choice framework in which each potential visitor selects from the set of 19 national parks or chooses not to visit any national park in South Africa (Berry, 1994). The specification controls for permanent differences across parks (such as size and location) and for annual changes in each origin country or province (such as exchange rate movements or economic conditions). Because the cost of traveling to a park differs by roughly an order of magnitude between domestic and international visitors, we estimate separate travel cost coefficients for the two groups, each capturing behavioral responses to cost variation within that group. The data only include visits to Table Mountain and West Coast National Parks for the final two years, so their consumer surplus estimates reflect this shorter observation window.

We estimate that a 1% increase in the cost of traveling to a park reduces visits to that park by 1.4% for domestic visitors and 2.1% for international visitors (Table C.32). These price responses fall within the range reported by prior multi-site recreation-demand studies (Herriges and Phaneuf, 2002; Lupi, Haefen, and Cheng, 2022). The estimated parameters allow us to recover, for each origin–park-year combination, the monetary value travelers receive from having access to the full set of national parks, net of their travel costs. Aggregating across all origins and years, tourism consumer surplus from South Africa's national parks averages approximately R7.7 billion per year (2023 rand), of which international visitors capture roughly R5.8 billion and domestic visitors approximately R1.9 billion. International tourists thus account for about three-quarters of total tourism consumer surplus despite taking far fewer trips than domestic visitors: 8.7 million international park visits over the sample period, compared with 23.1 million domestic. Each international trip generates a larger consumer surplus, reflecting the much higher cost international visitors are willing to bear to reach these parks.

Consumer surplus grew steadily from R5.9 billion in fiscal year 2012–13 to R11.0 billion in 2017–18, declined sharply to R1.4 billion in 2020–21 due to COVID-19 travel restrictions, and recovered to R11.4 billion by 2023–24—the highest in the sample.

To assess the contribution of individual parks, the analysis computes the welfare loss that all visitors would experience if a given park were removed while all other parks remained available. By this measure, Kruger National Park dominates the system, generating approximately R4.4 billion per year in tourism consumer surplus—almost three times that of the next most valuable park (Figure 7a). Garden Route National Park ranks second at R1.6 billion per year, followed by Addo Elephant National Park at R887 million. Together, these three parks account for nearly 90% of total tourism consumer surplus. The remaining parks each generate up to R117 million (Augrabies Falls) per year, collectively representing a diverse portfolio of recreational assets spread across the country.

Among South African provinces, residents of Gauteng receive the largest total consumer surplus (R528 million per year), reflecting the province's large population and high rate of national park visitation (Figure 7b). Mpumalanga ranks second in total surplus (R432 million per year) and first in per capita terms (R65 per person per year), driven by its proximity to Kruger. Western Cape (R312 million) and Limpopo (R263 million) follow, with per capita surplus of R40 and R38, respectively.

International tourism consumer surplus concentrates among visitors from a small number of wealthy source countries (Figure 7c). Visitors from Germany receive the largest surplus at R2.2 billion per year, followed by France (R541 million), the United Kingdom (R435 million), the Netherlands (R430 million), and the United States (R312 million). Among African nations, visitors from Mozambique benefit the most (R136 million per year), reflecting geographic proximity. Australia (R130 million), Italy (R122 million), Belgium (R116 million), and Switzerland (R110 million) complete the top ten international source countries.

## 5 Discussion

This study quantifies the long-run economic, bird biodiversity, and recreational welfare impacts of protected areas in South Africa. By applying machine-learning counterfactual estimation, the analysis recovers long-run causal effects that standard approaches cannot deliver. The results indicate that protected areas generate substantial and broad-based benefits: higher household incomes in surrounding communities, increased presence of threatened bird species, and approximately R7.7 billion per year in recreational consumer surplus from national parks alone.

Perhaps the most striking finding is the sharp divergence between short-run and long-run impacts. Across both the income and bird biodiversity analyses, recently established protected areas have small and statistically insignificant effects, while older protected areas generate large and statistically significant gains. For household income, none of the estimated effects for protected areas established between 2002 and 2011 differ significantly from zero—yet older protected areas tend to have the opposite result. The bird biodiversity results mirror this pattern: the newest protected areas show minimal impact across all threat categories, whereas protected areas established before 1953 drive the largest increases in critically endangered and endangered species.

One potential explanation for this divergence is spatial selection: if the most economically or ecologically promising locations received protection first, larger effects for older protected areas could reflect inherent locational advantages rather than dynamic treatment effects. To test this, we use our XGBoost model to predict counterfactual household income and threatened bird richness for each protected area using only pre-protection characteristics. Then we fit a linear regression line of the predictions against the years protected areas were declared. Under the spatial selection hypothesis, these predicted baseline outcomes should decline with declaration year, as progressively less favorable locations enter the protected area network over time. Figure 8 shows the opposite: predicted baseline income of protected areas is flat across declaration years, and more recently established protected areas actually possess higher predicted bird diversity potential. The outsized success of older protected areas is therefore unlikely to reflect favorable site selection and instead implies that tourism infrastructure, complementary private investment, and gradual ecosystem recovery require decades to materialize. Empirical approaches confined to estimating short-run effects of newly-established protected areas—the dominant strategy in the literature—risk severely underestimating the long-run benefits of conservation.


[[KC_IMAGE_009]]

Figure 8: Predicted household income (left) and predicted threatened bird richness (right) by protected area across declaration years. Counterfactual predictions are based on an XGBoost machine learning model using solely pre-protection geographic and historical characteristics (see Figure B.19 for model performance of threatened bird prediction). Circles indicate predicted household income (left panel) and adjusted threatened species richness per protected area (right panel). Colors indicate protected area age group (the startof data/within data corresponding to 2001 onwards for income and 2007 onwards for bird biodiversity), size of circles indicates size of the protected area in hectares, and the dark blue line represents a linear fit over the income and biodiversity predictions per protected area.

The aggregate economic contribution of South African protected areas is large. The analysis estimates that protected areas increase annual 2011 household income by approximately R300 billion, representing roughly $10\%$ of South Africa's nominal GDP in that year. This estimate captures the cumulative effect of the entire protected area network, including both direct local impacts and spatial spillovers extending into nearby communities. Our results suggest that the economic returns to conservation investment accumulate substantially over time and that the full fiscal and welfare accounting of protected areas extends beyond direct tourism revenues.

The biodiversity results reveal complementary roles for different categories of protected areas within South Africa's conservation network. National parks and the oldest protected areas are effective at preserving critically endangered and endangered species but contribute less to populations of vulnerable and near-threatened species. Conversely, intermediate-age and non-national-park protected areas—including provincial reserves and private conservation areas—increase the presence of vulnerable and near-threatened species. This functional differentiation demonstrates how South Africa's diverse portfolio of protected area types, varying in age, governance structure, and ecological context, collectively help conserve a broad suite of species. The finding also suggests that expanding protected area coverage need not replicate the characteristics of flagship national parks to deliver meaningful conservation gains; smaller and more recently established reserves could fill complementary ecological niches.

South Africa's national parks generate roughly R7.7 billion per year (2023 rand) in tourism consumer surplus, of which international visitors capture about three-quarters and South Africans capture the remainder. The international share is large, reflecting the substantial willingness of long-haul travelers to bear high travel costs to reach these parks. But domestic visitors still receive nearly R2 billion per year in surplus despite far lower per-trip willingness to pay, because they take roughly three times as many trips as international visitors (23.1 million versus 8.7 million over the sample period) and live close enough to parks to face only modest travel costs. South Africa's national parks therefore deliver meaningful recreational value to both populations, complicating the view that nature-based tourism in developing countries is only enjoyed by rich-world international travelers.

Several limitations warrant discussion. First, the machine-learning counterfactual approach assumes that pre-protection geographic and historical characteristics sufficiently capture the determinants of economic and ecological outcomes. While the close agreement between machine-learning and TWFE estimates for recently established protected areas supports this assumption, unobserved confounders correlated with both protection decisions and long-run outcomes cannot be fully excluded. Second, the household income analysis relies on census data from only two waves (2001 and 2011), limiting the precision of temporal comparisons. Third, the data used in the bird biodiversity analysis enables estimation of the effects of protected areas on species presence, but not on abundances, i.e., the number of individuals of each species. Fourth, the tourism consumer surplus model captures only recreational use values from national parks and does not account for non-use values or visits to provincial and private reserves. Fifth, the tourism model treats each observed trip as a visit to a single national park. We partially address this issue for international visitors by assigning only a fraction of long-haul travel costs to a park visit based on average trip length. Sixth, the tourism demand estimates rely on a conditional logit specification, which imposes the independence of irrelevant alternatives assumption and therefore restricts substitution patterns across parks. This affects both the aggregate consumer surplus estimates and, especially, the park-specific marginal values computed by removing one park from the choice set.

Under the Kunming–Montréal Global Biodiversity Framework of the Convention on Biological Diversity, most countries, including South Africa, committed to protecting at least 30% of the world's land and marine areas by 2030 (Convention on Biological Diversity, 2026a; Convention on Biological Diversity, 2026b). Achieving this “30×30” target will require a rapid expansion of protected areas, yet policymakers in biodiversity-rich developing countries face difficult tradeoffs between conservation and economic development. The results of this analysis suggest that these tradeoffs may be less severe than commonly assumed—but only over sufficiently long time horizons. Short-run analyses, which dominate the existing evidence base, systematically understate the returns to conservation. Achieving the full economic and ecological potential of newly-established protected areas will likely require patient public investment, sustained management capacity, and complementary infrastructure development over decades. The diversity of South Africa’s protected area network further demonstrates that conservation gains need not depend exclusively on large national parks; a heterogeneous system of public, provincial, and private reserves can collectively deliver broad benefits to people and wildlife.

## References

Amadeus for Developers (2025). Flight Offers Search API and Self-Service Developer Guides. https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/quick-start/.

Andam, Kwaw S, Paul J Ferraro, Katharine RE Sims, Andrew Healy, and Margaret B Holland (2010). "Protected areas reduced poverty in Costa Rica and Thailand". Proceedings of the National Academy of Sciences 107(22), pp. 9996–10001.

Bahrami, Golnaz, Matthew Gustafson, and Eva Steiner (2025). When Locking In Biodiversity Locks Up Land. https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=5006269. SSRN Working Paper.

Baylis, Kathy, Alberto Garcia, and Robert Heilmayr (2026). “Causal Inference for Biodiversity Conservation”. Review of Environmental Economics and Policy 20(1), pp. 000–000.

Becker, Richard A., Allan R. Wilks, Ray Brownrigg, Thomas P. Minka, and Alex Deckmyn (2025). maps: Draw Geographical Maps. R package version 3.4.3. URL: https://CRAN.R-project.org/package=maps.


Berry, Steven T. (1994). “Estimating Discrete-Choice Models of Product Differentiation”. The RAND Journal of Economics 25(2), pp. 242–262.


Bleakley, Hoyt and Jeffrey Lin (2012). “Portage and path dependence”. The Quarterly Journal of Economics 127(2), pp. 587–644.


Bushlore (2019). Vehicles Rental Rates 2019 South Africa. https://bushlore.com/wp-content/uploads/2018/11/Bushlore-Rates-2019-South-Africa.pdf. Accessed September 3, 2025.

Condylios, Steve, Bruno Mioto, and Bryan Shalloway (2025). priceR: Economics and Pricing Tools. R package version 1.0.2. URL: https://CRAN.R-project.org/package=priceR.

Convention on Biological Diversity (2026a). Kunming-Montreal Global Biodiversity Framework. Accessed April 13, 2026. URL: https://www.cbd.int/gbf.

— (2026b). List of Parties. Accessed April 13, 2026. URL: https://www.cbd.int/parties.

Dell, Melissa, Benjamin F Jones, and Benjamin A Olken (2012). “Temperature shocks and economic growth: Evidence from the last half century”. American Economic Journal: Macroeconomics 4(3), pp. 66–95.


Department of Mineral Resources and Energy (2024). Overview of the Petrol and Diesel Market in South Africa Between 2013 and 2022. https://www.dmre.gov.za/Portals/0/Energy\_Website/files/media/explained/Overview-of-Petrol-and-Diesel-Market-in-SA-between-2013-and-2022.pdf. Directorate: Energy Economics and Statistics; accessed September 2, 2025.

— (2025). Petrol Price Archive. https://www.dmre.gov.za/energy-resources/energy-sources/pretoleum/petrol-price-archive. Downloaded September 2, 2025.

DFFE EGIS (2020). South African National Land Cover Change Assessment, 2014–2020 [Raster]. https://www.dffe.gov.za/egis. Department of Forestry, Fisheries and the Environment, Environmental Geographic Information Systems. Downloaded March 24, 2026.

— (2025). Protected Areas [Shapefile], Version Q3 2025. https://www.dffe.gov.za/egis. Department of Forestry, Fisheries and the Environment, Environmental Geographic Information Systems. Downloaded December 15, 2025.

Donaldson, Dave (2018). “Railroads of the Raj: Estimating the impact of transportation infrastructure”. American Economic Review 108(4-5), pp. 899–934.

FAO and IIASA (2021). Global Agro-Ecological Zones version 4 (GAEZ v4): Suitability and Attainable Yield. Food and Agriculture Organization of the United Nations and International Institute for Applied Systems Analysis. Suitability index, 1981–2010, CRUTS32 climate, historical RCP, rainfed, high input with CO₂ fertilization. Downloaded October 21, 2024. URL: https://gaez.fao.org.

Federal Reserve Bank of St. Louis (2025). Kerosene-Type Jet Fuel Prices: U.S. Gulf Coast [WJFUELUS-GULF]. https://fred.stlouisfed.org/series/WJFUELUSGULF. Source: U.S. Energy Information Administration via FRED; downloaded August 26, 2025.

Ferraro, Paul J and Merlin M Hanauer (2014). “Quantifying causal mechanisms to determine how protected areas affect poverty through changes in ecosystem services and infrastructure”. Proceedings of the National Academy of Sciences 111(11), pp. 4332–4337.

Fink, Daniel, Tom Auer, Alison Johnston, Viviana Ruiz-Gutierrez, Wesley M. Hochachka, and Steve Kelling (2020). “Modeling avian full annual cycle distribution and population trends with citizen science data”. Ecological Applications 30(3), e02056. DOI: 10.1002/eap.2056.

Geldmann, Jonas, Megan Barnes, Lauren Coad, Ian D Craigie, Marc Hockings, and Neil D Burgess (2013). "Effectiveness of terrestrial protected areas in reducing habitat loss and population declines". Biological Conservation 161, pp. 230–238.


Giraud, Timothée (2022). “osrm: Interface Between R and the OpenStreetMap-Based Routing Service OSRM”. Journal of Open Source Software 7(78), p. 4574. DOI: 10.21105/joss.04574. URL: https://doi.org/10.21105/joss.04574.

Gollin, Douglas, Stephen Parente, and Richard Rogerson (2002). “The role of agriculture in development”. American Economic Review 92(2), pp. 160–164.

Gray, Claudia et al. (2016). “Local biodiversity is higher inside protected areas”. Nature Communications 7, p. 12306.

Grupp, Tristan, Prakash Mishra, Mathias Reynaert, and Arthur A van Benthem (2023). An Evaluation of Protected Area Policies in the European Union. National Bureau of Economic Research Working Paper Number 31934.


Harris, Ian, Timothy J Osborn, Phil Jones, and David Lister (2020). “Version 4 of the CRU TS monthly high-resolution gridded multivariate climate dataset”. Scientific Data 7(1). Downloaded June 27, 2024., p. 109.

Henderson, J Vernon, Tim Squires, Adam Storeygard, and David Weil (2018). “The Global Distribution of Economic Activity: Nature, History, and the Role of Trade”. The Quarterly Journal of Economics 133(1), pp. 357–406.

Henderson, J. Vernon, Adam Storeygard, and David N. Weil (2012). “Measuring Economic Growth from Outer Space”. American Economic Review 102(2), pp. 994–1028.

Herriges, Joseph A and Daniel J Phaneuf (2002). “Inducing Patterns of Correlation and Substitution in Repeated Logit Models of Recreation Demand”. American Journal of Agricultural Economics 84(4), pp. 1076–1090.

International Energy Agency (2025). Fuel Economy in South Africa. https://www.iea.org/articles/fuel-economy-in-south-africa. Accessed September 2, 2025.

Jarvis, Andy, Hannes I. Reuter, Andrew Nelson, and Edward Guevara (2008). Hole-filled SRTM for the Globe Version 4. CGIAR Consortium for Spatial Information (CGIAR-CSI). Retrieved via Google Earth Engine (dataset id: CGIAR/SRTM90\_V4). Downloaded October 22, 2024. URL: https://srtm.csi.cgiar.org.

Jedwab, Remi and Alexander Moradi (2016). “The permanent effects of transportation revolutions in poor countries: evidence from Africa”. Review of Economics and Statistics 98(2), pp. 268–284.

Kayser, Dominique, Claudia Sobrevila, and George Ledec (2011). Addo Elephant National Park: From Planning to the Implementation of a Successful Conservation and Socio-Economic Model. Accessed April 29, 2026. URL: https://www.thegef.org/sites/default/files/publications/AENP-web\_0.pdf.

Khaiid (2025). Most Crowded Airports: Busiest Airports Dataset. https://www.kaggle.com/datasets/khaiid/most-crowded-airports. Downloaded August 25, 2025.

Kleynhans, C. J., C. Thirion, and J. Moolman (2005). A Level I and II River Ecoregion Classification System for South Africa, Lesotho and Swaziland. Report No. N/0000/00/REQ0104. Resource Quality Services, Department of Water Affairs and Forestry (DWAF), Pretoria, South Africa.


Li, Xuecao, Yuyu Zhou, Min Zhao, and Xia Zhao (2020). “A harmonized global nighttime light dataset 1992–2018”. Scientific Data 7(1). Version 8. Downloaded October 11, 2024., p. 168.

Lupi, Frank, Roger H von Haefen, and Li Cheng (2022). “Distributional Effects of Entry Fees and Taxation for Financing Public Beaches”. Land Economics 98(3), pp. 509–519.

MDB (2011). Electoral Ward Shapefile. Municipal Demarcation Board of South Africa. Accessed October 11, 2024. URL: https://dataportal-mdb-sa.opendata.arcgis.com/datasets/12d2deb98816451ab7c4dc09cdfeee6b/about.


Myers, Norman, Russell Mittermeier, Cristina Mittermeier, Gustavo da Fonseca, and Jennifer Kent (2000). "Biodiversity hotspots for conservation priorities". Nature 403, pp. 853–858.

Natural Earth (2019). World Coastlines, 1:10 Million [Shapefile]. Processed and distributed by the World Bank Development Economics Data Group (DECDG). Data downloaded March 22, 2023. URL: https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-coastline/.

Noack, Frederik, Dennis Engist, and Ashley Larsen (2025). “The Value of Biodiversity: Evidence from Migratory Birds”. Available at SSRN 5473586.

Nunn, Nathan and Diego Puga (2012). “Ruggedness: The blessing of bad geography in Africa”. Review of Economics and Statistics 94(1), pp. 20–36.

OpenStreetMap Contributors (2024). South Africa Railways [Shapefile]. https://data.humdata.org/dataset/hotosm\_zaf\_railways. Humanitarian OpenStreetMap Team, Humanitarian Data Exchange. Downloaded October 11, 2024.

Padilla, A. D. et al. (2021). Compilation of Geospatial Data (GIS) for the Mineral Industries and Related Infrastructure of Africa. https://doi.org/10.5066/P97EQWXP. Data release. U.S. Geological Survey. Downloaded October 21, 2024.

Pfaff, Alexander, Juan Robalino, Diego Herrera, and Catalina Sandoval (2015). “Protected Areas’ Impacts on Brazilian Amazon Deforestation: Examining Conservation-Development Interactions to Inform Planning”. PloS one 10(7), e0129460.

Resource Quality Services, Department of Water and Sanitation (2006). Rivers of South Africa – All Drainage Regions, 1:500 000 [Shapefile]. https://www.dws.gov.za/iwqs/gis\_data/river/All.html. Downloaded January 17, 2025.

Ryan, Jeffrey A. and Joshua M. Ulrich (2025). quantmod: Quantitative Financial Modelling Framework. R package version 0.4.28. URL: https://cran.r-project.org/web/packages/quantmod/quantmod.pdf.

SA 4x4 Rentals (2019). Rates. https://sa4x4rentals.com/rates/. Accessed September 3, 2025.

SANParks (2025). GPS Waypoints pages for South African National Parks (SANParks). https://www.sanparks.org/parks/. Park-specific waypoint pages accessed via individual park page→Travel Information → GPS Waypoints. For example, https://www.sanparks.org/parks/addo-elephant/travel/gps-waypoints. Accessed August 29, 2025.

Shkolnik, Dmitry (2019). airportr: Convenience Tools for Working with Airport Data. R package version 0.1.3. URL: https://CRAN.R-project.org/package=airportr.

Sims, Katharine RE (2010). “Conservation and development: Evidence from Thai protected areas”. Journal of Environmental Economics and Management 60(2), pp. 94–114.

Siyabona Africa (2025). The Landscape of the Great Fish River. Accessed January 20, 2025. URL: https://www.nature-reserve.co.za/great-fish-river-landscape.html.

Small, Kenneth A. and Harvey S. Rosen (1981). “Applied Welfare Economics with Discrete Choice Models”. Econometrica 49(1), pp. 105–130.

Soul of a Railway (2025). Soul of a Railway. https://sites.google.com/site/soulorailway/soul-of-a-railway. Downloaded January 17, 2025.

South African National Parks (2025a). Addo Elephant National Park: Natural and Cultural History. Accessed January 21, 2025. URL: https://www.sanparks.org/parks/addo-elephant/explore/natural-cultural-history.

— (2025b). SANParks Tourism Demographics Data. Data emailed to authors by Candice Eb on August 13, 2025.

— (2025c). South African National Parks Conservation Fees and Tariffs. Data emailed to authors by Liandi Slabbert on September 22 and 23, 2025.

South African Railways and Harbours (1925). Standard Railway Map of South Africa [Map]. https://www.digitalcommonwealth.org/search/commonwealth:pr76hs68r. Digital Commonwealth. Downloaded October 4, 2024.

Statistics South Africa (2011a). South African Census Data. https://superweb.statssa.gov.za/webapi/jsf/login.xhtml. Downloaded October 10, 2024.
— (2011b). Statistical Release: Gross Domestic Product, Fourth Quarter 2011. https://www.statssa.gov.za/publications/P0441/P04414thQuarter2011.pdf. Downloaded March 10, 2026.


— (2018). Tourism Performance Report January–December 2018. https://live.southafrica.net/media/272674/tourism-performance-report-2018\_final.pdf?downloadId=281068. PDF downloaded October 12, 2025.

— (2019). Tourism Performance Report January–December 2019. https://live.southafrica.net/media/276660/tourism-performance-report-2019\_v12062020.pdf?downloadId=333390. PDF downloaded October 12, 2025.

— (2020). Tourism Performance Report, January–December 2020. https://live.southafrica.net/media/287538/sa-tourism-performance-report-2020.pdf. PDF downloaded October 12, 2025.

— (2023). Tourism Performance Report January–December 2023. https://live.southafrica.net/media/306460/sa-tourism-performance-report-2023-final-1.pdf?downloadId=427629. PDF downloaded October 12, 2025.

— (2024). Tourism Performance Report January–December 2024. https://live.southafrica.net/media/307564/sa-tourism-performance-report-2024.pdf?downloadId=434157. PDF downloaded October 12, 2025.

(2020). Domestic Tourism Survey, 2019. https://www.statssa.gov.za/publications/P03521/P03521December2019.pdf. Downloaded September 11, 2025.

— (2026). Consumer Price Index (CPI) History. Accessed April 29, 2026. URL: https://www.statssa.gov.za/publications/P0141/CPIHistory.pdf.

Thirion, C. and M. Silberbauer (2005). Ecoregions of South Africa, Level 2 [Shapefile]. https://www.dws.gov.za/iwqs/gis\_data/ecoregions/get-ecoregions.aspx. Resource Quality Information Services, Department of Water and Sanitation. Downloaded January 20, 2026.

U.S. Environmental Protection Agency (2024). Guidelines for Preparing Economic Analyses. EPA-240-R-24-001. https://www.epa.gov/system/files/documents/2024-12/guidelines-for-preparing-economic-analyses\_final\_508-compliant\_compressed.pdf. Washington, DC.

UNEP-WCMC and IUCN (2024). Protected Planet Report 2024. Tech. rep. Cambridge, United Kingdom and Gland, Switzerland: UNEP-WCMC and IUCN. URL: https://pp-digital-report-document.s3.eu-west-2.amazonaws.com/Protected+Planet+Report+2024.pdf.

United Nations Office for the Coordination of Humanitarian Affairs (2020). South Africa – Subnational Administrative Boundaries (COD-AB) [Shapefile]. Humanitarian Data Exchange. Data downloaded October 11, 2024. URL: https://data.humdata.org/dataset/cod-ab-zaf.

Von Hippel, Paul T, Samuel V Scarpino, and Igor Holas (2016). “Robust Estimation of Inequality from Binned Incomes”. Sociological Methodology 46(1), pp. 212–251.

Watson, James EM, Nigel Dudley, Daniel B Segan, and Marc Hockings (2014). “The performance and potential of protected areas”. Nature 515(7525), pp. 67–73.

World Bank (2025a). World Bank Official Boundaries - Admin 0. https://datacatalog.worldbank.org/int/search/dataset/0038272/world-bank-official-boundaries. Downloaded on May 12, 2026.

— (2025b). World Bank Official Boundaries - Admin 1. https://datacatalog.worldbank.org/int/search/dataset/0038272/world-bank-official-boundaries. Downloaded on September 17, 2025.

— (2025c). World Development Indicators. https://databank.worldbank.org/source/world-development-indicators.

World Bank Group (2026). More and Better Jobs. Accessed April 23, 2026. URL: https://scorecard.worldbank.org/en/outcomes/more-and-better-jobs.

World Travel and Tourism Council (2024). Travel & Tourism Economic Impact 2024: South Africa. https://cdn.prod.website-files.com/6329bc97af73223b575983ac/669e6868403d739b8155064c\_EIR2024-SouthAfrica.pdf. Accessed May 8, 2026.


# Supplemental Appendix

The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa

Dennis Engist, Gabriel Englander, Alan Lee and Frederik Noack

June 26, 2026

## Contents

A Supplementary Methods 2
A.1 Household Income 2
A.2 Bird Biodiversity 5
A.3 Tourism Consumer Surplus 8
B Supplementary Figures 15
C Supplementary Tables 32

## A Supplementary Methods

## A.1 Household Income

## A.1.1 Data

## Income Data

To construct the primary dependent variable in the income estimations, we use census data from the years 2001 and 2011 at the level of electoral ward. There are 4,277 wards and the data are publicly available on the Statistics South Africa data portal (Statistics South Africa, 2011a). The income variable is reported as number of households in 12 monthly income brackets with an open-ended top bracket (R204,801 or more). To calculate the average household income and extrapolate to total ward income, we follow Von Hippel, Scarpino, and Holas (2016) and fit a parametric function over the distribution of households across income brackets to calculate the total income per ward. If this calculation provides a value that is lower than a lower-bound ward-level income (which is calculated by multiplying the population in each bracket with its lower income boundary), we calculate an alternative total income instead by multiplying the population in each bracket with the middle income value of a bracket and using $1.5 \times$ lower-bound value for the top bracket. Figure B.20 displays the distribution of log-transformed electoral-ward level household income across South Africa in 2001 and 2011. We use electoral ward boundary data from the Municipal Demarcation Board of South Africa (MDB, 2011). We use data on South African national and provincial boundaries from United Nations Office for the Coordination of Humanitarian Affairs (2020).

## Nighttime Lights Data


## Protected Areas

To determine the location of protected areas, we use a vector dataset of South African protected areas provided by the Department of Forestry, Fisheries and the Environment (DFFE EGIS, 2025). It contains the precise outline of all protected areas, public or private, and their establishment dates. However, when a given protected area expands, its boundaries are not always updated in the data.

## Predictor Variables Used in Income Analysis

Figure B.1 displays the predictor variables' values at the level of electoral ward.

Railways: We include exposure to railways as a variable in this analysis, as they play a major role in economic development. We used railway lines in 1925 as the basis to calculate this variable, because by that time the South African railway network was mature, yet Kruger National Park, the first South African national park, was only established in 1926. We reconstructed the 1925 railway lines based on a network map (South African Railways and Harbours, 1925). We first downloaded a shapefile of the modern South African railway network from Open Street Maps (OpenStreetMap Contributors, 2024). We retained modern railway lines that were present in 1925 and removed ones established after. Then, we used aerial imagery to re-trace the railway lines that existed in 1925 but no longer exist today. The 1925 network map indicates where a line existed, which we can then follow precisely on the modern aerial image, because most of the former railway lines left visible traces in the landscape. However, some narrow-gauge lines are impossible to discern on aerial images today. In those cases, we relied on regional maps to fit the railway lines into the landscape (Soul of a Railway, 2025). We also created an additional dataset of railway junctions by placing a point on every endpoint and junction of railway lines. The exact point was placed at the train station closest to the junction or endpoint. For both the railway lines and junctions, and all other variables that measure exposure by distance, we calculated the distance to these features of every point in a 1 km grid across South Africa. We then calculated the average distance of all points in an electoral ward.

Major metropolitan areas: We include historical data to calculate exposure to major metropolitan areas, which is another important determinant of economic development. For the same reason that we used railway lines before the establishment of the first national park, we used population data from the 1921 census. We located the city center of the nine major metropolitan areas listed in that census, and calculated the average distance of every electoral ward to each city center. We then combined these nine distance variables into one by weighting them by population in a gravity term, as in

$$
\mathrm{WeightedDistance} _ {i} = \sum_ {m \in \mathrm{Cities}} \frac {\mathrm{Population} _ {m}}{\mathrm{Distance} _ {i m} ^ {\alpha}}\tag{1}
$$

where $Population_{m}$ is the population of city m in 1921, $Distance_{im}^{\alpha}$ is the average distance of electoral ward i to city m to the power of $\alpha$ , which reflects the expected impact of proximity to major metropolitan areas on trade and development. As the functional form of the proximity impact is theoretically ambiguous, we use a neutral $\alpha = 1$ .

Resource deposits: We use resource deposit data for Africa from the USGS (Padilla et al., 2021).

Rivers: We use vectorized data of major rivers provided by the South African Department of Water and Sanitation (Resource Quality Services, Department of Water and Sanitation, 2006). Only rivers of order 5 or higher are included, which corresponds to major rivers.


Landscape: We use elevation, slope and ruggedness (variance of elevation) across South Africa based on data from the Shuttle Radar Topography Mission (Jarvis et al., 2008).

Coastline: We calculate distance to coastline based on global coastline data from Natural Earth (2019).

## A.1.2 Estimation

We use three approaches to estimate the effect of protected areas on income: a two-way fixed effects (TWFE) panel regression, a cross-sectional ordinary least squares (OLS) regression, and machine learning. As a robustness exercise, we repeat all specifications using the sum of nighttime light pixel values per electoral ward as an alternative outcome.

Across all specifications, we calculate standard errors using a spatial block bootstrap with 500 iterations, sampling electoral wards within $1^{\circ} \times 1^{\circ}$ grid cells. This approach robustly accounts for spatial autocorre lation and, in the machine learning estimations, properly propagates the uncertainty introduced by using a generated counterfactual outcome in the second-stage regression.

## TWFE Model

We estimate the effects of newly-established protected areas with a TWFE model. The model takes the form

$$
\begin{array}{c} \log (Y _ {i t}) = \beta_ {1} \log (\mathrm{PAWard} _ {i t}) + \beta_ {2} \log (\mathrm{PABuffer} _ {i t}) \\ + \lambda_ {i} + \delta_ {t} + \epsilon_ {i t} \end{array}\tag{2}
$$

where $Y_{it}$ is income in electoral ward $i$ in year $t$ , $\mathrm{PAWard}_{it}$ and $\mathrm{PABuffer}_{it}$ are the total area under protection in an electoral ward and in the 15 km buffer surrounding it (in $\mathrm{m}^2$ ), $\lambda_i$ are ward fixed effects (binary variables for each ward that absorb all time-invariant differences between wards), $\delta_t$ are year fixed effects, and $\epsilon_{it}$ is the error term. $\beta_1$ and $\beta_2$ are the coefficients capturing the effects of protected areas. As this approach relies on within-ward variation over time (i.e., changes in income in the same electoral ward), we can only estimate the effect of protected areas established between 2002 and 2011 (due to ward-level census data being unavailable for South Africa's 2021 census or for its censuses before 2001).

## OLS Model

To estimate the effect of all protected areas, including the majority of pre-2002 established protected areas, we use an OLS regression model with electoral-ward level income as a dependent variable, protected areas in a ward and in a buffer as independent variables, and economic predictor variables as controls:

$$
\begin{array}{c} \log (Y _ {i t}) = \beta_ {1} \log (\mathrm{PAWard} _ {i t}) + \beta_ {2} \log (\mathrm{PABuffer} _ {i t}) \\ + \gamma \mathbf {X} _ {i} + \delta_ {t} + \epsilon_ {i t} \end{array}\tag{3}
$$

where $Y_{it}$ is the income in electoral ward i in year t, $PAWard_{it}$ and $PABuffer_{it}$ are the total area under protection within the ward and within a 15 km buffer (in $m^{2}$ ), $X_{i}$ is a vector of the environmental and historical control variables listed in Section A.1.1, $\delta_{t}$ are year fixed effects (which absorb all ward-invariant annual changes such as macroeconomic conditions), and $\epsilon_{it}$ is the error term. The coefficients $\beta_{1}$ and $\beta_{2}$ capture the cross-sectional effect of protected areas on income, conditional on the environmental and historical control variables and year fixed effects.

In additional OLS specifications, we allow the effect of protected areas to vary by protected-area type and age category. Specifically, we estimate separate coefficients for national parks and other protected areas in one specification, and separate coefficients for each of five establishment-age categories in another:

$$
\begin{array}{r l} & {\log (Y _ {i t}) = \sum_ {c} \beta_ {1 c} \mathrm{log} (\mathrm{PAWard} _ {i c t}) + \sum_ {c} \beta_ {2 c} \mathrm{log} (\mathrm{PABuffer} _ {i c t})} \\ & {\qquad + \gamma \mathbf {X} _ {i} + \delta_ {t} + \epsilon_ {i t}} \end{array}\tag{4}
$$

In the type specification, c indexes two categories: national parks and other protected areas. In the age-category specification, c indexes five establishment-age categories: $\leq$ 1953, 1954–1977, 1978–1992, 1993–2001, and $\geq$ 2002. We apply the same type and age-category divisions in the machine learning model.

## Machine Learning Model

While the OLS model controls for spatial and historical differences, it imposes a strict functional form on how these covariates interact and affect local economies. To construct a more flexible counterfactual, we employ a two-step machine learning approach using the XGBoost algorithm.

In the first step, we train the XGBoost algorithm to predict the log of household income based exclusively on our set of environmental and historical predictors. Crucially, we restrict the training data to “purely untreated” electoral wards—defined as wards that contain zero protected area coverage and with an average point in the ward at least 15 km away from any protected area. Thus, the algorithm learns the underlying, baseline relationship between geography, historical infrastructure, and economic development in the absence of protected areas.

In the second step, we use the trained model to predict the income for all electoral wards across South Africa. This prediction represents the counterfactual income: the expected income of a ward if it had the exact same characteristics but no exposure to protected areas. We then calculate the difference between the actual observed income and this predicted counterfactual. Finally, we regress this difference on our protected area treatment variables (overall, by type, and by age) to estimate the impact of protected areas:

$$
\log (Y _ {i t}) - \log (\hat {Y} _ {i t}) = \beta_ {0} + \beta_ {1} \mathrm{log(PAWard} _ {i t}) + \beta_ {2} \mathrm{log(PABuffer} _ {i t}) + \delta_ {t} + \epsilon_ {i t}\tag{5}
$$

Because $\hat{Y}_{it}$ is a generated variable, standard regression outputs would underestimate the true level of statistical uncertainty. To ensure valid inference, the entire two-step process, including the hyperparameter tuning, model training, counterfactual prediction, and the final regressions (Equation 5), is recalculated inside every iteration of the spatial block bootstrap.

## A.2 Bird Biodiversity

## A.2.1 Data

## Bird Observation Data

We use bird observation data from the Southern African Bird Atlas Project 2 (SABAP2) (Brooks et al., 2022). The spatial unit of observation is the pentad, a $5 \times 5$ arc-minute rectangle (approximately $9 \times 9$ km). We restrict our sample to “full protocol” observation cards collected between 2007 and 2025, which requires observers to follow strict guidelines, including a minimum observation time of two hours and a comprehensive recording of all species present. 292,978 observation cards meet these criteria. We remove pelagic species from the sample (Albatrosses, Petrels, Shearwaters, Prions, Skuas, Jaegers, Terns, Noddys, Gannets, Boobys, Fritagebirds, Penguins, Tropicbirds, Cormorants, Gulls, Oystercatchers, Phalaropes, Skimmers, Sheathbills and Shags), as well as pentads that include ocean. We calculate the observed species richness for each card across four International Union for Conservation of Nature (IUCN) threat levels: critically endangered and endangered (CR+EN), vulnerable (VU), near threatened (NT), and least concern (LC). We further divide LC species into urban avoiders and urban adaptors based on their habitat preferences according to the literature and author field experience.

Urban avoiders are species that do worse in urbanised landscapes i.e. they are reported less often in urban pentads than in other pentads, and their occurrence tends to decline as the level of development increases. Towns, suburbs and heavily built-up areas appear to reduce habitat quality or suitability for these birds.

Urban adaptors are species that are able to use, tolerate, or benefit from urban and developed environments. They are reported more often in urban pentads than in other pentads, or show a positive association with increasing development. This group includes the most obvious “urban winners”, such as species that thrive around gardens, buildings, roadsides, or artificial water bodies, but also species that are not fully dependent on cities and can still occur widely outside them.

For a lot of species, there is no clear overall urban response, so they were not included as a distinct category in the analysis. For example, reporting rates that are very similar in urban and non-urban pentads suggest little measurable effect of urbanisation. In other cases, the evidence is mixed: for example, a species might be reported slightly more often in urban pentads, but show little or no positive response to increasing development, or vice versa. Some species may also use certain urban features opportunistically while still depending mostly on non-urban habitats, producing an overall pattern that is neither clearly positive nor clearly negative. There are also cases where responses to “urban” differ regionally. For example, in the Western Cape, Greater Double-collared Sunbird is responding positively to urbanisation due to the urban forest effect, but the reverse is happening elsewhere.

Because observation effort varies across cards, we adjust the five species richness variables at the card level using a negative binomial regression that controls for log-transformed hours observed and total cards submitted by the observer, and includes month and hour of the day fixed effects. The residuals from these regressions serve as our primary effort-adjusted species richness dependent variables.

## Protected Areas

As in the income estimation, we use the protected area vector dataset from the Department of Forestry, Fisheries and the Environment (DFFE EGIS, 2025). For the bird biodiversity analysis, the treatment variable is defined as the share of the pentad's total surface area that is covered by a protected area, calculated yearly.

## Ecological and Economic Predictor Variables

To isolate the impact of protected areas, we control for the identical set of historical and environmental variables used in the income analysis, averaged to the pentad level. In addition to these predictors, we include biome shares per pentad, allowing for fractional coverage at biome boundaries, to account for the primary natural determinants of bird distributions and habitat carrying capacities (Thirion and Silberbauer, 2005). See Figure B.13 for overview maps of the predictor variables at the pentad level.

## Land Cover Data and Management Quality Proxy


## A.2.2 Estimation

We follow the same three-part estimation strategy used in the income analysis, adapting the spatial unit to pentads and the treatment variable to the pentad protected area share. Across all specifications, we calculate standard errors using a spatial block bootstrap with 500 iterations, sampling pentads within $1^{\circ} \times 1^{\circ}$ grid cells.

## TWFE Model

We estimate the bird biodiversity impacts of newly-established protected areas with a TWFE panel model. The model takes the form:

$$
Y _ {i t} = \beta_ {1} \mathrm{PAShare} _ {i t} + \delta_ {t} + \lambda_ {i} + \epsilon_ {i t}\tag{6}
$$

where $Y_{it}$ is the effort-adjusted species richness for a specific threat category in pentad i in year t, $PAShare_{it}$ is the proportion of the pentad covered by protected areas, $\lambda_{i}$ are pentad fixed effects, $\delta_{t}$ are year fixed effects, and $\epsilon_{it}$ is the error term. Because this approach relies on within-pentad variation over time, the estimate $\beta_{1}$ captures the short-run effect of protected areas established between 2008 and 2025.

## OLS Model

To estimate the effects of the entire protected area network, including parks established prior to SABAP2, we use a cross-sectional OLS regression model:

$$
Y _ {i t} = \beta_ {0} + \beta_ {1} \mathrm{PAShare} _ {i t} + \gamma \mathbf {X} _ {i} + \delta_ {t} + \epsilon_ {i t}\tag{7}
$$

where $Y_{it}$ is the effort-adjusted species richness for a given threat category in pentad i and year t, $PAShare_{it}$ is the share of the pentad covered by protected areas, $X_{i}$ is a vector of the environmental and historical control variables, and $\delta_{t}$ are year fixed effects. As in the income analysis, we perform separate estimations pooling all protected areas, differentiating between national parks and other protected areas, and splitting the protected area network into five distinct age cohorts to evaluate how conservation impacts evolve over time.

To further interrogate the drivers of conservation success, we also estimate how treatment effects vary by our management quality proxy and by surface area. Using the land cover change index described above, we replace the aggregate protected area share with separate treatment variables for “high management” and “low management” protected areas. Thus, we re-run Equation 7 with two protected area share variables, where each one represents share of high and share of low management protected areas. Finally, we also divide the protected area network into surface area quartiles to evaluate how the ecological benefits of conservation scale with park size.

## Machine Learning Model

As in the income estimation, we employ an XGBoost machine learning model to estimate the effects of the entire protected area network while relaxing linear functional form assumptions.

In the first step, we train the XGBoost algorithm to predict adjusted species richness (by threat category and urban avoiders/urban adaptors) based on the full set of environmental, historical, and ecological predictors. We restrict the training dataset to “purely untreated” pentads, defined as those containing zero protected area coverage and located at least 10 km away from any protected area. We choose 10 km because a pentad is roughly 10 km across at the equator. This restriction ensures the algorithm learns the baseline ecological carrying capacity of different regions in the absence of protected areas.

In the second step, the trained model generates a predicted counterfactual species richness for each threat level and for all pentads across South Africa. We calculate the residual difference between the observed (effort-adjusted) richness and this counterfactual prediction. We then regress these residuals on the protected area treatment variables (overall share, by type, and by age cohort) to estimate the effect of protected areas:

$$
Y _ {i t} - \hat {Y} _ {i t} = \beta_ {0} + \beta_ {1} \mathrm{PAShare} _ {i t} + \delta_ {t} + \epsilon_ {i t}\tag{8}
$$

where $Y_{it}$ is the effort-adjusted species richness for a given threat level in pentad i and year t, $\hat{Y}_{it}$ is the XGBoost-predicted counterfactual effort-adjusted richness, $PAShare_{it}$ is the share of the pentad covered by protected areas, $\delta_{t}$ are year fixed effects, and $\epsilon_{it}$ is the error term.

To ensure correct inference when using a generated counterfactual outcome, we again rely on a spatial block bootstrap with 500 iterations. For the bird biodiversity analysis, this bootstrap procedure is expanded to properly account for observation effort uncertainty: within each spatial resampling iteration, the negative binomial effort-adjustment regression is re-estimated on the newly drawn sample before the XGBoost model is trained and evaluated.

## A.3 Tourism Consumer Surplus

This subsection describes the data processing and analysis used in estimating the recreational consumer surplus generated by access to the South African national park system.

## Visits Data

The primary data, provided by South African National Parks (SANParks), contain the number of visits to national parks in South Africa (South African National Parks, 2025b). The unit of observation is national park by fiscal year by origin country, territory or South African province. For example, one observation is 16 Kenyans visited Addo Elephant National Park in fiscal year 2022-23. The South African fiscal year begins on April 1st and ends on March 31st. The data used in the analysis span fiscal years 2012–13 through 2023–24; for brevity, the main text refers to this period as 2012–2024.

We harmonize park and origin names across the raw visits data before constructing the estimation sample. We combine Tsitsikamma National Park, Wilderness National Park, and Knysna National Lake Area into Garden Route National Park because these three areas were combined into the single Garden Route National Park in 2009. We assign Mduli Safari Lodge to Addo Elephant National Park because Mduli is inside the boundaries of Addo. We also standardize a small number of origin names, including Dubai as United Arab Emirates, Netherlands Antilles as Curaçao, and New Guinea as Papua New Guinea. As noted in the main text, Table Mountain and West Coast National Parks enter the data only in the final two fiscal years.

## A.3.1 Travel Cost Construction

We estimate the cost of traveling to each park in each fiscal year from each origin country, territory, or South African province. We do not include the cost of activities once visitors enter the park. This allows the estimation results to represent the value of access to the national park system, rather than the value of activities undertaken within parks.

For each international origin–park-year combination, we compare two route families and set the travel cost equal to the option with the lowest total cost. The first route family (fly-fly-drive) flies from the origin country to either O.R. Tambo International Airport or Cape Town International Airport, connects to one of 19 other South African domestic airports, and then drives to the park entrance. The second route family (fly-drive) flies from the origin country to either O.R. Tambo International Airport or Cape Town International Airport and then drives directly to the park. Each route family generates multiple candidate routes depending on the airports selected. For each candidate route, we sum the applicable airfare, driving fuel cost, travel-time cost, car-rental cost for the driving portion, and park entrance fees.

For each domestic origin–park-year combination, we compare two analogous route families and set the travel cost equal to the option with the lowest total cost. The first route family (fly-drive) allows travelers to depart from a South African airport within 200 km of their provincial capital, fly to another domestic airport, and then drive to the park. The second (single) route drives directly from the provincial capital to the park. The first route family again generates multiple candidate routes depending on the airports selected. For each candidate route, we sum the airfare (if applicable), driving fuel cost, travel-time cost, and park entrance fees.

## Park Entrances

We assign one main entrance or closest equivalent to each park using official SANParks GPS waypoints (SANParks, 2025). For example, no entrance gate is listed for Agulhas National Park so we use the coordinates of the park office.

## Driving Distances and Fuel Costs

We compute road driving distances with the osrm R package (Giraud, 2022). We combine these distances with monthly inland unleaded 95 petrol prices from South Africa's Department of Mineral Resources and Energy (Department of Mineral Resources and Energy, 2025), average those prices to the fiscal year, and convert them to 2023 R (South African rand). We use unleaded 95 petrol because it is the dominant petrol grade in South Africa's retail market (Department of Mineral Resources and Energy, 2024). To convert fuel prices to R per kilometer, we assume fuel efficiency of 10.1 liters per 100 km (kilometers), which is the International Energy Agency estimate for new large sport utility vehicles and pick-up trucks in South Africa in 2012 (International Energy Agency, 2025). We use the large sport utility vehicle and pick-up truck category because travel to some park entrances can involve rough roads which a large vehicle is required to traverse. We use the 2012 value because it corresponds to the beginning of the study period and provides a reasonable benchmark over the full sample: for the early years it likely understates fuel consumption for the average vehicle on the road (since most vehicles will have been built before 2012 and have lower fuel efficiency), while for the later years it may overstate fuel consumption, making it a plausible average value across the study period.

## Car Rental Costs for International Visitors

We estimate car-rental costs for international visitors because they typically do not own a vehicle in South Africa. (If a tour company drives a visitor to the park, then the vehicle cost would be part of the price paid to the tour company.) We estimate the daily car-rental rate as the unweighted average across vehicle types and seasons from two South African 4×4 rental companies (SA 4x4 Rentals, 2019; Bushlore, 2019). We convert the prices from 2019 R to 2023 R. We compute rental days based on driving time, assuming a maximum of 12 driving hours per day. For example, if it takes 13 hours to drive from an airport to the park entrance, then the rental duration is 4 days (2 days going and 2 days returning). We do not add car-rental cost for domestic travelers, on the assumption that domestic visitors use their own vehicles.

## International Airfares


Airport in Johannesburg and Cape Town International Airport, the two principal international gateways to South Africa.

We estimate international airfares rather than observing them for every origin-year pair because historical airfare data are proprietary and expensive. The free tier of the Amadeus self-service API permits queries for future departure dates (Amadeus for Developers, 2025). Because fuel costs constitute a relatively stable share of airfare over time, we estimate the relationship between future fares and distance×fuel price. We then use this relationship to predict historical fares for all routes and years. We download annual jet-fuel prices (Federal Reserve Bank of St. Louis, 2025), average the weekly observations to the South African fiscal year, convert nominal U.S. dollars to R using the USD/R exchange rate at the midpoint of each fiscal year (October 1) (Ryan and Ulrich, 2025), and deflate to 2023 R using the priceR R package (Condylios, Mioto, and Shalloway, 2025). On August 27, 2025, we queried round-trip economy fares for departures on November 15, 2025, February 15, 2026, May, 15 2026, and August 15, 2026, with returns one week later. We space the dates across seasons to approximate an annual average fare. We query fares to both O.R. Tambo International Airport and Cape Town International Airport from the busiest airport in each of the 10 international origins with the most observed visitors to the park system. There are 80 queries total: 4 dates from 10 origin airports to 2 South African airports. We then regress the round-trip fare on an intercept and distance multiplied by the jet-fuel price on August 22, 2025, the most immediate day with jet-fuel price data before we queried the airfares. The intercept captures fees, taxes, and fixed surcharges common to all routes, while the slope scales the marginal cost of distance as fuel prices change. We use the fitted values from this equation to predict round-trip airfares for all origin-gateway-year combinations given the corresponding historical jet-fuel prices between 2012 and 2024.

## Domestic Airfares

We estimate domestic airfares separately from international airfares, using the same approach but with separate Amadeus queries and regressions.

The first estimation concerns the middle leg of the fly-fly-drive route family for international visitors: flights between the two international gateways (O.R. Tambo International Airport and Cape Town International Airport) and 19 South African domestic airports. On August 29, 2025, we queried round-trip economy fares for all 19 domestic airports to and from both gateways, for departures on November 15, 2025, February 15, 2026, May 15, 2026, and August 15, 2026, with returns three days later rather than one week, reflecting the shorter duration of a typical domestic trip. There are 152 queries total (19 airports to 2 gateways on 4 dates). We then regress the round-trip fare on an intercept and distance multiplied by the contemporaneous jet-fuel price, and use the fitted values to predict fares for all domestic airport-gateway-year combinations.

The second domestic airfare estimation concerns the first leg of the fly-drive route family for domestic visitors. Visitors may depart from any of 21 domestic airports that are within 200 km road driving distance of their provincial capital. They may arrive at any of the 21 domestic airports. On September 4, 2025, we queried fares for a random sample of 150 airport-pair-date combinations drawn from the same departure and return dates as the first domestic airfare query. We estimate a separate regression on these data and use the fitted values to predict fares for all domestic airport pairs and years.

## Travel-Time Cost

We monetize travel time by multiplying total hours in transit by one-third of annual GDP per capita, and include this as a component of the travel cost. We use GDP per capita as a proxy for earnings and follow the standard one-third-of-wage assumption in the recreation travel-cost literature (U.S. Environmental Protection Agency, 2024). We take GDP per capita by country and year from the World Development

Indicators (World Bank, 2025c) and convert nominal U.S. dollars to 2023 R. For domestic visitors, we apply South African GDP per capita to all provinces. When country-year GDP per capita data are missing, we first fill missing years with the country's most recent non-missing observation; if no observation exists for that country, we fill with the cross-country annual mean.

We compute flight duration as great-circle distance divided by 850 km/h (Kristoffersson and Liu, 2024). We then add fixed airport-processing time to each flight leg: 3 hours before each international departure (reflecting check-in, security, and immigration) and 2 hours before each domestic departure. We compute driving durations with the osrm R package (Giraud, 2022)

## Entrance Fees

We use data from SANParks fee schedules (South African National Parks, 2025c). We assume that visitors pay to access the park for 3 days (Mukanjari, Muchapondwa, and Demeke, 2021). Entrance fees vary by park, year, and whether the visitor is South African, a Southern African Development Community (SADC) National, or an Other National. We use the applicable fee for adult visitors and convert all nominal fees to 2023 R. Because SANParks tariff schedules run from November 1 to October 31 while the fiscal year runs from April 1 to March 31, we map tariff-year fees to fiscal-year fees using a weighted average: the fiscal-year fee equals 7/12 of the preceding tariff year's fee (covering April–October) plus 5/12 of the current tariff year's fee (covering November–March).

Three parks require special treatment because they contain multiple sections with different fee schedules. For Garden Route National Park, we use the Tsitsikamma–Storms River Mouth fee. For Table Mountain National Park, we use the Cape of Good Hope / Cape Point fee. For West Coast National Park, we use the flower-season fee (August–September). Mokala National Park is missing from the entrance fee data for fiscal years 2012–13 through 2014–15 and 2020–21. For those years, we impute Mokala's fee by applying the average category-specific percentage change observed across all other parks in the adjacent year, working sequentially backward from the nearest non-missing year.

## Apportioning Travel Costs for International Visitors

For international visitors, a park visit often forms only one segment of a longer trip to South Africa. We therefore assign only a fraction $3/L_{t}$ of the international round-trip airfare and long-haul flight time to the park visit, where $L_{t}$ denotes the average length of stay (in nights) of international visitors to South Africa in fiscal year t. This apportionment avoids attributing the full cost of reaching South Africa to a single park visit. We construct annual length-of-stay values from South African Tourism annual performance reports (South African Tourism, 2013; South African Tourism, 2015; South African Tourism, 2018; South African Tourism, 2019; South African Tourism, 2020; South African Tourism, 2023; South African Tourism, 2024). Because these reports record calendar-year averages, we convert them to fiscal-year values using a weighted average that assigns a weight of 9/12 to the calendar year that overlaps with the first nine months of the fiscal year (April–December) and 3/12 to the following calendar year that overlaps with the last three months (January–March).

## Least-Cost Routes

For international visitors, we calculate that fly-drive is the cheaper option for 94% of the international origin-park-year combinations, reflecting the relatively high predicted cost of domestic flights in South Africa. For domestic visitors, we calculate that direct driving is always cheaper than fly-drive.

Among the 48,246 international origin-park-year combinations, the minimum travel cost is R8,408, for visitors from Lesotho to Bontebok National Park in fiscal year 2017–2018 (fly to Cape Town, drive to park).

The median travel cost is R15,194 (visitors from Ivory Coast to Namaqua National Park in fiscal year 2013–2014) and the maximum is R32,998 (visitors from United States Minor Outlying Islands to Kgalagadi Transfrontier Park in fiscal year 2022–2023). Among the 1,926 province-park-year combinations, the minimum travel cost is R288 (visitors from Northern Cape to Mokala National Park in fiscal year 2020–2021), the median is R2,177 (visitors from KwaZulu-Natal to Bontebok National Park in fiscal year 2020–2021), and the maximum is R5,893 (visitors from Western Cape to Mapungubwe National Park in fiscal year 2022–2023).

## A.3.2 Consumer Surplus Estimation

Having described our processing of the visits data and calculation of travel costs, we now present our estimation of tourism consumer surplus.

## Market Size and Choice Set

Our discrete choice model requires defining the total population of potential travelers from each origin country, territory, and South African province.

For international origins, we define market size as the number of international departures from each origin, drawn from the World Development Indicators (World Bank, 2025c). This measure captures the pool of travelers who could potentially visit a protected area in South Africa. Because the international departures data are missing for some origins and for the final years of the study period, we impute missing market sizes in the following manner. If an origin has observed departures in some years but not others, we fill missing years with that origin's average observed departures. If an origin has no observed departures in any year, we predict departures as follows. Among origins with non-missing departures, we regress origin-level log average departures on log average population, log average GDP per capita, and an intercept term. We use the fitted coefficients from this regression to predict departures for origins with non-missing population and GDP per capita data. For our study period, four origins—Eritrea, Gibraltar, Saint-Martin, and North Korea—have population data but not GDP per capita in the World Development Indicators. We predict departures for these origins with the coefficients from a regression of log average departures on log average population and an intercept. The departures, GDP per capita, and population data are reported by calendar year; we match each fiscal year to the calendar year in which it begins (e.g., fiscal year 2012–13 uses calendar year 2012 values). For origins missing both population and GDP per capita data, we set the market size to 10,000.

For domestic origins, we define market size as the number of overnight trips taken by residents of each South African province, using Table 6 of the Domestic Tourism Survey 2019 (Statistics South Africa, 2020). We hold provincial market sizes fixed across years.

Each origin-year choice set includes 19 inside alternatives (one for each national park) and an outside option representing the choice not to visit any South African national park in that year. We normalize the travel cost of the outside option to zero because the outside option serves as the reference option in the model. We compute the outside-option quantity as market size minus observed park visits. In one origin-year—Wallis & Futuna in fiscal year 2023–24—observed inside visits slightly exceed the market size. In that case, we reset market size to total inside visits plus one, which preserves a valid (positive) outside-option quantity while leaving the inside visit counts unchanged.

## Demand Estimation

We estimate visitor demand as a function of travel cost using the discrete choice framework of Berry (1994). Before calculating the log number of visits, we add a smoothing constant of 0.5 to the visitor count for every alternative, including the outside option, to avoid undefined values when there are zero visits to a park from a given origin in a particular year. This smoothing can be interpreted as assigning a small positive visit probability to every park-origin-year even when no visits are observed.

Let $V_{ojt}$ denote the observed number of visitors from origin o to park j in year t, and let $M_{ot}$ denote the market size from origin o in year t. We define the smoothed share as

$$
s _ {o j t} = \frac {V _ {o j t} + 0 . 5}{M _ {o t} + 1 0},\tag{9}
$$

where the denominator adds $0.5 \times 20$ to the market size to account for the smoothing constant applied to each of the 19 parks and the outside option. The smoothed outside-option share $s_{o0t}$ is defined analogously, with $V_{o0t} = M_{ot} - \sum_{j=1}^{19} V_{ojt}$ .

Following Berry (1994), the difference in log shares between an inside alternative and the outside option is linear in the model parameters, which allows us to estimate demand with ordinary least squares regression rather than maximum likelihood. Because the cost of traveling to a South African national park differs by roughly an order of magnitude between domestic and international visitors, pooling the two groups would impose a single behavioral response on populations that face very different price levels and likely differ in their underlying price sensitivity. We therefore estimate separate travel cost coefficients for the two groups. Specifically, we estimate

$$
\delta_ {o j t} \equiv \log s _ {o j t} - \log s _ {o 0 t} = \alpha_ {\mathrm{Dom}} T C _ {o j t} \mathbf {1} \{o \in \mathrm{Dom} \} + \alpha_ {\mathrm{Intl}} T C _ {o j t} \mathbf {1} \{o \in \mathrm{Intl} \} + \gamma_ {j} + \eta_ {o t} + \varepsilon_ {o j t},\tag{10}
$$

where $TC_{ojt}$ denotes least-cost travel cost, $1\{o \in Dom\}$ is an indicator variable that equals 1 for visitors from domestic origins and equals 0 otherwise, $1\{o \in Intl\}$ is an indicator variable for visitors from international origins, $\gamma_{j}$ indicates park fixed effects (binary variables for each park that absorb all time-invariant differences between parks), and $\eta_{ot}$ denotes origin-by-year fixed effects that absorb annual changes specific to each origin (such as exchange rate movements, economic conditions, and travel restrictions). The coefficients $\alpha_{Dom}$ and $\alpha_{Intl}$ capture how sensitive domestic and international visitors are to travel cost: a more negative $\alpha$ implies that demand falls more sharply as the cost of reaching a park increases. We estimate the model using the fixest R package (Bergé, Butts, and McDermott, 2026). Under the standard Type I extreme value assumption on the error term $\varepsilon_{ojt}$ —the same distributional assumption that underlies the conditional logit model—this linear specification recovers the same parameter estimates as maximum likelihood. We cluster standard errors at the origin level to allow unobserved demand shocks to be correlated across parks for visitors from the same origin. Column 1 of Table C.32 displays the results. Column 2 displays the result of estimating a single travel cost coefficient, rather than estimating separate coefficients for domestic and international visitors.

## Consumer Surplus

Given the estimated travel-cost coefficients $\hat{\alpha}_{Dom}$ and $\hat{\alpha}_{Intl}$ , we compute per-capita consumer surplus for origin o in year t as

$$
C S _ {o t} ^ {p c} = - \frac {1}{\hat {\alpha} _ {g (o)}} \log \left(1 + \sum_ {j = 1} ^ {1 9} \exp (\delta_ {o j t})\right),\tag{11}
$$

where $g(o) \in \{\text{Dom}, \text{Intl}\}$ denotes the group (domestic or international) to which origin o belongs. The summation inside the logarithm aggregates the attractiveness of all 19 parks as perceived by travelers from origin o. The inclusion of the constant 1 inside the logarithm represents the outside option of not visiting any national park. Dividing by $-\hat{\alpha}_{g(o)}$ converts the log-sum from utility units into the monetary units (2023 rand) implied by that group's marginal disutility of travel cost (Small and Rosen, 1981). The resulting quantity measures the economic benefit that a potential traveler from origin $o$ derives from access to the full set of national parks in year $t$ , given the travel costs of reaching those parks. We then compute total consumer surplus in origin $o$ and year $t$ as

$$
C S _ {o t} = M _ {o t} \times C S _ {o t} ^ {p c},\tag{12}
$$

where $M_{ot}$ denotes market size.

To estimate the marginal contribution of an individual park, we recompute the summation term after removing that park from the choice set while holding all remaining $\delta_{ojt}$ fixed. We use the same group-specific $\hat{\alpha}_{g(o)}$ to convert this difference in inclusive value into rand. The difference between the full-choice-set and reduced-choice-set consumer surplus gives the welfare loss that potential visitors would experience from losing access to that park, accounting for the fact that some visitors would substitute to other parks rather than forgo a national park visit entirely.

## Own-Price Elasticities

The main text reports that a $1\%$ increase in the cost of traveling to a park reduces visits to that park by $1.4\%$ for domestic visitors and $2.1\%$ for international visitors. This relationship is known as the own-price elasticity of demand. The own-price elasticity of park $j$ 's visit share with respect to its own travel cost in origin $o$ and year $t$ is

$$
\eta_ {o j t} = \hat {\alpha} _ {g (o)} \times T C _ {o j t} \times (1 - s _ {o j t}),\tag{13}
$$

which follows from differentiating the logit choice probability with respect to $TC_{ojt}$ . We report visitor-weighted means of $\eta_{ojt}$ separately for domestic and international visitors, weighting each origin-park-year combination by its smoothed visit count $V_{ojt} + 0.5$ .

## B Supplementary Figures


[[KC_IMAGE_010]]

Figure B.1: A selection of environmental and historical control variables at the level of electoral ward. Railway lines are based on the 1925 network, while cities represent a gravity term of population-weighted distance to 1921 metropolitan areas. Missing from this figure, but included as predictor variables in our estimations, are distance to railway junctions, distance to silver, platinum, tin, uranium, asbestos, nickel, zinc, lead, and lithium deposits. See Section A.1.1 for details.


[[KC_IMAGE_011]]


Figure B.2: Distribution of training data electoral wards in 2001 and 2011. The number of wards in the training data changes over time due to the expansion of protected areas.

[[KC_IMAGE_012]]

Figure B.3: Out-of-fold model performance of XGBoost income and nightlight prediction.


[[KC_IMAGE_013]]

Figure B.4: The effect on total nightlights per electoral ward of all protected areas (left panel), of protected areas by type (middle panel), and of protected areas by age (right panel). Coefficient estimates as dots, 90% confidence intervals in dark color, and 95% confidence intervals in light color. Orange represents effect of protected areas within ward and purple represents effect of protected areas within the 15 km buffer surrounding each ward. Squares indicate results from the panel TWFE approach, circles the results from the cross-sectional linear regression (OLS), and diamonds the machine learning (ML) approach.


[[KC_IMAGE_014]]

Figure B.5: Number of yearly SABAP2 full protocol cards in the study period.

## Number of SABAP2 full protocols per pentad


[[KC_IMAGE_015]]

Figure B.6: Spatial distribution of total number of full protocol cards per pentad.


[[KC_IMAGE_016]]

Figure B.7: Mean adjusted species richness distribution per pentad across all full protocol cards, by IUCN threat category: critically endangered and endangered (CR+EN), vulnerable (VU), near-threatened (NT), and least concern (LC), as well as total (all species) adjusted species richness.


[[KC_IMAGE_017]]

Adjusted species richness
Figure B.8: Mean adjusted species richness distribution per pentad across all full protocol cards, by LC urban avoider species, LC urban adaptor species, and total LC species.


[[KC_IMAGE_018]]

Figure B.9: Effort bias and correction across IUCN threat categories. The first row presents the number of species observed as a function of hours spent observing. The second row presents the adjusted number of species observed as a function of hours spent observing. The third row shows the residuals from the effort adjustment regression averaged per pentad, representing deviations in species richness from the mean, conditional on effort.


[[KC_IMAGE_019]]


Species richness by effort and spatial distribution

[[KC_IMAGE_020]]


[[KC_IMAGE_021]]


[[KC_IMAGE_022]]

Figure B.10: Effort bias and correction across LC subsets. The first row presents the number of species observed as a function of hours spent observing. The second row presents the adjusted number of species observed as a function of hours spent observing. The third row shows residuals from the effort adjustment regression averaged per pentad, representing deviations in species richness from the mean, conditional on effort.


[[KC_IMAGE_023]]

Figure B.11: Adjusted relative species richness for threatened species, LC urban avoiders, and LC urban adaptors, overlaid with protected area boundaries. The positive impact of large protected areas, such as Kruger National Park in the northeast, is clearly visible as a stark contrast with surrounding areas.


[[KC_IMAGE_024]]


[[KC_IMAGE_025]]

Figure B.13: A selection of environmental and historical control variables used in the bird biodiversity prediction. Railway lines are based on the 1925 network, while cities represent a gravity term of population-weighted distance to 1921 metropolitan areas. Missing from this figure, but included in the estimations, are distance to railway junctions, distance to coast, distance to silver, platinum, tin, uranium, asbestos, nickel, zinc, lead, and lithium deposits, and minimum temperature.


[[KC_IMAGE_026]]

Figure B.14: Distribution of training data pentads in selected years (2010, 2020 and 2025). The number of pentads in the training data changes over time due to the availability of full protocol cards and the expansion of protected areas.


[[KC_IMAGE_027]]

Figure B.15: Out-of-fold model performance of XGBoost bird biodiversity prediction by IUCN threat level, with Least Concern birds split into urban adaptors (“urban”) and urban avoiders (“non-urban”).

Land cover change management index


[[KC_IMAGE_028]]

Figure B.16: A map of protected areas by land cover change-based management quality proxy. Blue represents high management index, i.e., below-median share of land cover change from natural to artificial surfaces between 2014 and 2020, while red represents low management index, i.e., above-median share of land cover change from natural to artificial surfaces between 2014 and 2020.

Figure B.17: The effect on bird species richness of protected areas by proxy for management quality. Bird species richness is calculated by IUCN threat level: critically endangered and endangered (CR+EN, red), vulnerable (VU, orange), near threatened (NT, light green), least concern urban avoiders (LC Urban Avoiders, dark green), and least concern urban adaptors (LC Urban Adaptors, darkest green). Coefficient estimates as dots, 90% confidence intervals in dark color, and 95% confidence intervals in light color. Diamonds indicate the results from the cross-sectional linear regression (OLS), and circles the results from the machine learning (ML) approach.

Figure B.18: The effect on bird species richness of protected areas by surface area quartile. Bird species richness is calculated by IUCN threat level: critically endangered and endangered (CR+EN, red), vulnerable (VU, orange), near threatened (NT, light green), least concern urban avoiders (LC Urban Avoiders, dark green), and least concern urban adaptors (LC Urban Adaptors, darkest green). The effect of very small protected areas is presented on a separate scale for visual purposes. Coefficient estimates as dots, 90% confidence intervals in dark color, and 95% confidence intervals in light color. Diamonds indicate the results from the cross-sectional linear regression (OLS), and circles the results from the machine learning (ML) approach.

Figure B.19: Out-of-fold cross-validated (OOF CV) performance of XGBoost model predicting threatened bird biodiversity.

Figure B.20: Distribution of log-transformed total household income at electoral-ward level in 2001 and 2011, based on data from the South African census (Statistics South Africa, 2011a).

Figure B.21: Distribution of total nighttime light values at electoral-ward level in 2001 and 2011, based on data from Li et al. (2020).

## C Supplementary Tables

Table C.1: Optimal XGBoost Parameters for LOG GB ESTIMATE HH


Table C.2: Optimal XGBoost Parameters for LOG VALUE NIGHTLIGHTS


Table C.3: Estimated Effect of Protected Areas on Income and Nightlights using OLS with Environmental and Historical Controls–All Protected Areas


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.4: Estimated Effect of Protected Areas on Income and Nightlights using OLS with Environmental and Historical Controls–Protected Areas by Type


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.5: Estimated Effect of Protected Areas on Income and Nightlights using OLS with Environmental and Historical Controls–Protected Areas by Age


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.6: Estimated Effect of Protected Areas on Income and Nightlights using the Machine Learning Approach–All Protected Areas


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.7: Estimated Effect of Protected Areas on Income and Nightlights using the Machine Learning Approach–Protected Areas by Type


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.8: Estimated Effect of Protected Areas on Income and Nightlights using the Machine Learning Approach–Protected Areas by Age


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.9: Estimated Effect of Protected Areas on Income and Nightlights using the TWFE Approach–All Protected Areas


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by two-way fixed effects panel regression. Spatial block bootstrapped standard errors in parentheses.

Table C.10: Critically Endangered (CR) Species


Table C.11: Endangered (EN) Species


Table C.12: Vulnerable (VU) Species


Table C.13: Near Threatened (NT) Species


Table C.14: Least Concern (LC) Urban Avoider Species


Table C.15: Least Concern (LC) Urban Adaptor Species


Table C.16: Optimal XGBoost Parameters for RICHNESS CREN


Table C.17: Optimal XGBoost Parameters for RICHNESS VU


Table C.18: Optimal XGBoost Parameters for RICHNESS NT


Table C.19: Optimal XGBoost Parameters for RICHNESS URBAN


Table C.20: Optimal XGBoost Parameters for RICHNESS NONURBAN


Table C.21: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using OLS with Environmental and Historical Controls–All Protected Areas


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Bootstrapped standard errors in parentheses.

Table C.22: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using OLS with Environmental and Historical Controls–Protected Areas by Type


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Bootstrapped standard errors in parentheses.

Table C.23: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using OLS with Environmental and Historical Controls–Protected Areas by Age


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Bootstrapped standard errors in parentheses.

Table C.24: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–All Protected Areas


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.25: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–Protected Areas by Type


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1

This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.26: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–Protected Areas by Age


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.27: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the TWFE approach–All Protected Areas


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by two-way fixed effects panel regression. Spatial block bootstrapped standard errors in parentheses.

Table C.28: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using OLS with Environmental and Historical Controls–Protected Areas by High or Low management


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.29: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–Protected Areas by High or Low management


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.30: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using OLS with Environmental and Historical Controls–Protected Areas by Size


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.31: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–Protected Areas by Size


Custom standard-errors in parentheses
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.32: Estimated Effect of Travel Cost on National Park Visitation


Notes: This table presents the results from estimating Equation 10 by ordinary least squares regression. Column (1) is our primary specification, allowing the travel cost coefficient to differ between domestic and international visitors. Column (2) imposes a single travel cost coefficient as a robustness check. Both specifications include park fixed effects and origin-by-fiscal year fixed effects. Standard errors clustered at the origin level in parentheses. The main-text estimates that a $1\%$ increase in travel cost reduces visits by $1.4\%$ (domestic) and $2.1\%$ (international) are computed from the coefficients in Column (1) using Equation 13, $\eta_{ojt} = \hat{\alpha}_{g(o)} \times TC_{ojt} \times (1 - s_{ojt})$ , where $\hat{\alpha}_{g(o)}$ is the travel cost coefficient for the group (domestic or international) to which origin $o$ belongs, $TC_{ojt}$ is the travel cost for an origin-park-year, and $s_{ojt}$ is the smoothed visit share defined in Equation 9. Reported main-text values are visitor-weighted means computed separately for domestic and international visitors. The number of observations (48,415) is fewer than the total number of origin-park-year combinations (48,246 international + 1,926 domestic = 50,172) because Table Mountain and West Coast National Parks are missing data on the number of visitors for all but the final two years of our study period.
