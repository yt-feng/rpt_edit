#11
# Poverty and Disability: Evidence from Africa
## Abstract

This paper examines the relationship between disability and poverty among working-age adults in Africa, using nationally representative household surveys from 27 countries that include the Washington Group Short Set of Questions on Functioning. The paper provides the most comprehensive cross-country analysis of disability in Africa to date, documenting disability prevalence, sociodemographic patterns, and the association between disability and poverty at both national and regional levels. Results show that disability is more common among women, rural residents, and older adults, and is closely linked with poverty. Prevalence is 3.6 per cent among women compared to 2.3 per cent among men, 3.4 per cent in rural areas versus 2.6 per cent in urban areas, and 4.4 per cent among adults aged 34–49 compared to 2.3 per cent among those aged 18–33. Weighted probit regressions demonstrate a robust association between disability and an elevated risk of both asset poverty and multidimensional poverty in most countries, even after adjusting for sociodemographic characteristics. These findings underscore the imperative to systematically mainstream disability inclusion into national poverty reduction strategies and directly address the needs of persons with disabilities through targeted interventions.

Key words

Asset poverty, multidimensional poverty, disability, functional difficulties, Africa, Washington Group Short Set on Functioning

## Contents

1. Introduction......3
2. Disability prevalence......7
2.1 Concepts, data and definitions......7
2.2 Functional difficulties by domain and degree of severity......11
2.3 Disability prevalence by demographic characteristics......15
2.4 Disability prevalence by asset-based wealth quintiles......17
3. Disability and probability of living in poverty......21
3.1 Empirical approach......21
3.2 Regression results......23
4. Conclusions and policy discussion......28
References......30
Annex: Data sources and coverage......33

## 1. Introduction

Well-being and development are inextricably linked to poverty eradication. Over the past three decades, significant progress has been made in reducing extreme poverty, which has fallen from around 40 per cent to less than 10 per cent globally. However, in the past decade, this progress has slowed (Figure 1, panel A). The COVID-19 outbreak only partially explains this change in trajectory because the slowdown began before the pandemic. The explanation is rather in the concentration of extreme poverty in fragile, conflict-affected, and post-conflict states and among the most vulnerable groups, such as refugees, internally displaced persons, ethnic minorities, and persons with disabilities. This paper focuses on one of these vulnerable groups — persons with disabilities — and examines the impact of disability on poverty, with two phenomena known to form a complex mutually reinforcing relationship (Banks, Kuper, and Polack 2017; Groce et al. 2011; Pinilla-Roncancio and Alkire 2021).


## Figure 1. Evolution of extreme poverty

A.
Poverty headcount ratio at \$2.15 a day (% of population)

[[KC_IMAGE_001]]

B.
Number of poor people at \$2.15 a day (mln)


[[KC_IMAGE_002]]

Source: Author's calculations based on the World Development Indicators of the World Bank.

Another notable feature of extreme poverty is its increasing concentration on the African continent, where the majority of the world's poor now reside. As shown in Figure 1, the current poverty rate in Sub-Saharan Africa exceeds 37 per cent, and while the poverty rate is stagnating, the number of poor people is growing (Figure 1, panel B), reaching 464 million people in 2024. The United Nations (2023) warns that if current trends persist, Sustainable Development Goal (SDG) 1 “End poverty in all its forms everywhere” will not be achieved by 2030. By that time, 575 million people, or seven per cent of the global population, will still be living in extreme poverty, with a significant concentration in Africa. Africa is also most affected by multidimensional poverty, i.e. deprivations in essential aspects of wellbeing, such as education, health and standards of living, affecting 553 million people (United Nations and Oxford Poverty and Human Development Initiative 2024). This calls for special attention to the region in poverty eradication efforts and underlying analytical work. Consequently, this paper centres its empirical analysis on African countries, aiming to describe correlates of disability and analyse its relationship with poverty, with the ultimate objective of providing inputs for policies and activities aimed at effective poverty reduction.

Quantitative studies on the link between poverty and disability based on representative samples or censuses are available for only a few African countries. In one of the most comprehensive studies, Hosseinpoor et al. (2013) analyse how disability prevalence relates to household wealth in 49 countries, including 16 in Africa $^{1}$ . They find that in 43 of these countries, disability prevalence is higher among poorer strata. Mitra, Posarac, and Vick (2013) and Pinilla-Roncancio and Alkire (2021) extend the analysis to multidimensional poverty. $^{2}$ Mitra, Posarac, and Vick (2013) show that persons with disabilities are more likely to experience multiple deprivations, have lower educational attainment, lower employment rates, and higher medical expenditures. Similar links between disability, poverty, education, and employment were identified in studies from South Africa (Loeb et al. 2008), Uganda (Hoogeveen 2005) and Zambia (Trani and Loeb 2012). Trani et al. (2015) demonstrate that in Morocco and Tunisia, persons with disabilities, particularly women, girls, and rural residents, are more likely to be deprived of basic capabilities. Filmer (2008) studied the association between poverty and disability in 14 countries, including five in Africa $^{3}$ , identifying low schooling attainment as a major pathway. Extra costs related to disability are examined by Mont et al. (2022) for seven countries $^{4}$ ; and by Asuman, Ackah, and Agyire-Tettey (2021) for Ghana, where these costs are estimated to be as high as 26 per cent of annual household consumption expenditure, increasing the poverty rate among households with persons with disabilities in Ghana from 38.5 per cent to 52.9 per cent.

Overall, existing literature on the poverty-disability nexus in Africa identifies a strong link between the two phenomena. This is corroborated in a systematic review by Banks, Kuper, and Polack (2017), who examined studies on poverty and disability in low- and middle-income countries, finding that 81 per cent of studies support a positive association between poverty and disability. However, many African countries are underrepresented in this stream of research, and studies that include African countries often rely on outdated data or narrow definitions of poverty and disability.

Correspondingly, this paper has three objectives. The first is to provide stylized facts on disability in African countries by offering population-level estimates of disability prevalence among adults and examining systematic differences across sex, residence (rural vs. urban), and asset-based wealth, with a lower position on the wealth distribution proxying poverty. While country-specific statistics on disability prevalence are available, they are often scattered across sources and difficult to compare due to the differences in the definition of disability and questionnaires used to collect disability statistics. Furthermore, the information on disability prevalence disaggregated by income or wealth is rarely available. Currently the most comprehensive resource - the Disability Data Initiative and the Disability Data Reports (Hanass-Hancock et al. 2023; Mitra and Yap 2022; 2021) - offer harmonized information on adults with disabilities for many developing countries, including 18 African countries, with the poverty captured through the multidimensional poverty index (MPI). $^{5}$ Multidimensional poverty rates by disability status are also available in the United Nations (2024) report monitoring the progress towards SDGs for persons with disabilities but include only 14 African countries. This paper complements these efforts by expanding the country coverage for African countries $^{6}$ , adding asset poverty in the stratification and controlling for sociodemographic characteristics.

The second objective is to shed further light on the disability-poverty relationship in Africa through econometric analysis permitting to control for confounding factors such as sociodemographic characteristics. Furthermore, in this paper, poverty is measured using two complementary approaches showing both asset poverty and deprivations in a broader set of conditions necessary for well-being. The first poverty measure is based on a wealth index constructed from consumer goods ownership and household characteristics such as cooking facilities, water, and sanitation (similar to Filmer and Pritchett 1999). The second measure is the multidimensional poverty index (MPI), inspired by Amartya Sen's work (e.g. Sen 1993), and implemented following the same approach as in Mitra and Yap (2021) who adapted it to the disability context by mapping the available questions in the surveys and censuses with the provisions of the United Nations Convention on the Rights of Persons with Disabilities (UNCRPD) and SDGs.

The multidimensional poverty measures capture the complexity of poverty by considering multiple dimensions of deprivation, such as education, health, and living conditions. This is crucial for studying disability, as individuals with disabilities may have incomes above the poverty line but still experience multiple deprivations affecting their well-being and opportunities in different ways than persons without disabilities.

The third objective of the paper is to take a regional view on country-level results with the aim of drawing out salient features of the disability-poverty nexus in Africa. The analysis feeds into policy recommendations for addressing the interaction between disability and poverty which is critical for ensuring inclusive growth and development and leaving no one behind.

The remainder of the paper is structured as follows. Section 2 starts with the concept of disability and how it is operationalized in this paper. It then provides estimates of the prevalence of disability by functional domains, sociodemographic characteristics and asset-based wealth quintiles for each country with available data and for the African region. Section 3 turns to the econometric analysis of the impact of disability on poverty, and reports country-specific and regional results. Section 4 concludes with policy discussion.


[[KC_IMAGE_003]]


# Disability prevalence

## 2.1 Concepts, data and definitions

This paper follows the UNCRPD, which defines persons with disabilities as those who have “long-term physical, mental, intellectual or sensory impairments which in interaction with various barriers may hinder their full and effective participation in society on an equal basis with others” (United Nations 2006). Central to this definition are the interactions between an individual with a health condition and that individual’s environmental and personal factors, visually shown in Figure 2.


## Figure 2.

Disability in International Classification of Functioning, Disability and Health


[[KC_IMAGE_004]]

Contextual factors
Source: World Health Organization (2001).

The concept is operationalized using a measurement tool developed by the Washington Group $^{7}$ , which provides internationally comparable and tested questions on functional difficulties compatible with the UNCRPD definition of disability. The Washington Group has developed and tested a short questionnaire, also known as the Washington Group Short Set (WGSS). $^{8}$ It starts with an optional introduction as follows: “The next questions ask about difficulties you may have doing certain activities because of a health problem.” It then has questions covering six different domains as follows:

1. Do you have difficulty seeing, even if wearing glasses?

2. Do you have difficulty hearing, even if using a hearing aid?

3. Do you have difficulty walking or climbing steps?

4. Do you have difficulty remembering or concentrating?

5. Do you have difficulty with self-care (such as washing all over or dressing)?

6. Do you have difficulty communicating?

The WGSS uses a four-level scale (no difficulty, some difficulty, a lot of difficulty, or cannot do at all) to capture individuals' degree of functional difficulty in each of the six domains.

A systematic analysis of African countries was made possible thanks to recent efforts in mainstreaming the WGSS into national household surveys and censuses. The analysis is based on the Demographic and Health Surveys (DHS) supported by USAID and the Multiple Indicator Cluster Surveys (MICS) developed by UNICEF and implemented in collaboration with national authorities. The sample covers 27 countries accounting for 57 per cent of the continent's population. All surveys have been undertaken relatively recently, between 2016 and 2023. $^{9}$ The surveys are nationally representative, and their samples are extensive. Table A1 of the Annex lists the countries included in the analysis, the survey used, the year of data collection, the total number of respondents with information on disability, as well as the number of respondents disaggregated by the sociodemographic characteristics used in the analysis.

The survey data are affected by several limitations. The most important one is related to age. MICS omit older adults (age 50 and above) from the sample because their primary focus is on children and the population of reproductive age, particularly women. Furthermore, the Child Functioning Module for children age 17 and below used in MICS differs from the WGSS. To overcome these limitations, the paper restricts all analyses to adults age 18-49 and the results are applicable only to this group.

It is also important to keep in mind potential differences between MICS and DHS surveys arising from MICS not allowing responses by proxy to the men's questionnaire and the women's questionnaire that contain the WGSS. As a result, the MICS questionnaire does not contain the option "Cannot do at all" for question "6. Do you have difficulty communicating?" $^{10}$ , thus underestimating the prevalence of functional difficulties related to communications. While questions related to other functional domains do include the option of responding "Cannot do at all", people with the most severe limitations (e.g. those who are deaf or with severe difficulty in cognition) are less likely to be covered by MICS data collection. $^{11}$ These differences may have implications for the prevalence estimates, including cross-country comparisons and the pooling of data at the regional level. Furthermore, the MICS approach may have implications for the analysis of the relationship between disability and poverty, which is likely to be biased downwards in MICS datasets because under-sampled individuals with the most severe limitations are likely to be at a high risk of poverty. Finally, the paper undertakes analysis at the individual level while certain information in both MICS and DHS is collected at the household level (e.g. assets and household characteristics). The paper therefore makes an implicit assumption of an equal division of intra-household assets.

Turning to the definition of disability, the WGSS captures information on functional difficulties at four levels, namely:

1. no difficulty, 2. some difficulty, 3. a lot of difficulty, or 4. cannot do at all, allowing for multiple ways of creating dichotomous variables capturing the presence or absence of disability. The paper follows the Washington Group recommendation in defining persons with disability as those who respond to at least one of the six questions with a lot of difficulty or cannot do it at all, and correspondingly persons without disabilities are defined as those who experience no difficulty or some difficulty (Washington Group on Disability Statistics 2021); this approach is also referred to as cut-off 3.

Disability prevalence at the country level is calculated as follows:

$$
D i s a b i l i t y P r e v a l e n c e _ {c} = \frac {N u m b e r o f a d u l t s w i t h d i s a b i l i t e s _ {c}}{N u m b e r o f s u r v e y e d a d u l t s _ {c}}\tag{1}
$$

where subscript c denotes a country. The disability prevalence is calculated for the entire working-age population (age 18-49) of a country and for within-country subgroups based on age, sex, rurality, and asset ownership. Disability is captured at the level of the individual (as opposed to the household). All tabulations and regressions take into account the complex survey design and use Taylor linearized variance for computing all standard errors and confidence intervals. Strata with one sampling unit are centred at the grand mean.

When the analysis is undertaken at the regional level, the data from 27 countries are pooled in a single dataset. $^{12}$ To ensure that the pooled survey data reflect the actual demographic weight of each country, all individual survey weights were rescaled to match the size of the total working-age population of each country. Specifically, for an individual i in country c, the rescaled weight $w_{ic}^{*}$ is calculated as follows:

$$
w _ {i c} ^ {*} = \frac {w _ {i c}}{\sum_ {i} w _ {i c}} * N _ {c}\tag{2}
$$

where $w_{ic}$ is the original survey weight and $N_{c}$ is the total working-age population of country $c^{13}$ . With this adjustment, the sum of rescaled weights in each country is proportionate to the working-age population, allowing regional prevalence estimates to be interpreted as working-age population-weighted averages across all countries.

In addition to the primary analysis based on the survey data from 27 countries, Table 2A in the Annex lists a further set of 25 countries that have some information on disability prevalence. Most of the additional sources do not follow the WGSS or do not make the data publicly available, resulting in differences in disability definition and sample selection, which cannot be aligned with the definitions used in this paper or analysed in depth. Hence, the information for the additional 25 countries obtained from secondary sources is reported separately, in the Annex. The reason for the inclusion of this information in the paper is twofold. The first reason is completeness: the paper gathers disability prevalence estimates for 52 African countries. Even if countries kept in the Annex have different samples and definitions of disability, it is convenient to have a one-stop reference for all countries. The second reason is the importance of highlighting the gap in disability data across African countries. While more than half of the countries on the continent have included the WGSS questions on functional difficulties in recent surveys and censuses, and Zambia went even further – implementing a dedicated National Disability Survey – in ten countries the surveys or nationally representative censuses with disability questions date back more than a decade, eight countries have recent disability data but do not follow standardized and tested methodology, and for two countries (Republic of the Congo and Libya) the information on disability prevalence is not available at all.

## 2.2 Functional difficulties by domain and degree of severity

Table 1 provides nationwide estimates of the prevalence of functional difficulties by degree of severity for the working-age population (age 18-49). The prevalence of any functional difficulty (considering any functional domain and any level of difficulty) ranges from 6.0 per cent in Senegal, 6.1 per cent in Nigeria, and 8.4 per cent in the United Republic of Tanzania to as high as 45.9 per cent in Sao Tome and Principe, 45.7 per cent in the Central African Republic, and 43.5 per cent in Ghana. This large variation is likely to stem from the resources at the disposal of persons with disabilities, their environment, and historical background. The WGSS questions take into account assistive devices, asking, for example, “Do you have difficulty seeing, even if wearing glasses?” Consequently, in countries with higher availability and affordability of glasses, the rate for functional difficulties in vision is likely to be lower. In countries with a history of violent conflict, prevalence of functional difficulties is likely to be higher. The WGSS improves cross-country comparability by replacing culturally variable definitions of disability with harmonized and tested questions on functioning (seeing, hearing, walking, cognition, self-care, and communication) and the training of enumerators. The responses might nonetheless be influenced by cultural attitudes towards disability and the expected use of survey results.

In all countries, the share of persons with functional difficulties declines with the degree of severity. Narrowing down to persons reporting some difficulty, the prevalence estimates range from 4.7 per cent in Senegal to 38.5 per cent in Sao Tome and Principe, and for persons with a lot of difficulty the prevalence is from 0.5 per cent in Nigeria to 10.3 per cent in the Central African Republic. The share of persons who cannot perform at all in at least one domain is in the range from 0.1 per cent to 0.8 per cent. The last column shows disability prevalence which, by definition, sums up persons reporting “a lot of difficulty” and “cannot do at all” in any domain. The prevalence of disability is in the range from 0.7 per cent in Nigeria to 10.9 per cent in the Central African Republic, with estimates for Kenya and South Africa (3.0 and 3.1 per cent, respectively) being around the regional mean.

For the analysis at the regional level, a pooled multi-country dataset was constructed, preserving the original complex survey design. Primary sampling units and strata identifiers were made unique across countries, and individual survey weights were rescaled by the national working-age population in 2024. Regional prevalences were then estimated using Taylor linearized variance estimation that accounts for clustering and stratification. Based on data from 27 countries with nationally representative surveys containing the WGSS, the disability prevalence among working-age adults in Africa is 3.1 per cent, out of which 2.8 per cent of respondents reported a lot of difficulty in at least one of the six functional domains, and 0.3 per cent reported that they cannot perform at all in at least one of the functional domains. In Africa, the share of working-age adults that reported some difficulty in any functional domain stands at 14.5 per cent, while the share of working-age adults with any difficulty in at least one domain is 17.5 per cent. The regional prevalence estimates are below the means of corresponding cross-country estimates due to the influence of Nigeria, which has one of the lowest disability prevalence but a high weight in the aggregation due to the size of its population.

Table 1.
Prevalence of functional difficulties by degree of severity


Note: Calculations are adjusted for the complex survey design. The sample includes adults (age 18-49). Prevalence by degree of severity counts individuals by the highest degree of difficulty they experience. Disability includes individuals who responded that they have either “a lot of difficulty” or “cannot do at all” in any domain. All countries follow the Washington Group Short Set (WGSS) on Functioning. DHS stands for Demographic and Health Survey, and MICS stands for Multiple Indicator Cluster Survey. Prevalence estimates for Africa are calculated from a pooled dataset, taking into account the original survey design, with individual weights rescaled by the working-age population of each country.

Disability prevalence by functional domain varies greatly across countries, but the ranking by functional domain shows some similarities (Table 2). At the country level, the most frequently reported type of disability is related to seeing (14 out of 27 countries), followed by mobility and cognition, which are the most reported in 9 and 8 countries, respectively. The least reported types of disability are in the domain of hearing, self-care, and communicating. For example, in Kenya, disability related to seeing affects 1.2 per cent of working-age adults, disability related to mobility and cognition are reported by 0.8 per cent of working-age respondents, followed by hearing, communicating, and self-care (with disability prevalence of 0.4, 0.4 and 0.3, respectively). The share of working-age adults with disability in more than one domain ranges from 0.1 per cent in Nigeria to 2.1 per cent in the Central African Republic.

At the African regional level, based on the pooled dataset weighted by working-age population, the most frequent disabilities are in the domain of cognition (1.1 per cent), seeing (1.0 per cent) and mobility (0.9 per cent), followed by hearing (0.3 per cent), communication (0.3 per cent) and self-care (0.2 per cent). The prevalence of multiple disabilities in the working-age population in Africa is 0.5 per cent.


[[KC_IMAGE_005]]


Table 2.
Disability prevalence by functional domain


Note: Calculations are adjusted for the complex survey design. The sample includes adults (age 18-49). Disability is defined as reporting either “a lot of difficulty” or “cannot do at all” for any of the functional domains. Individuals reporting difficulties in two or more domains are counted under each domain reported, and in the column “multiple domains”. Prevalence estimates for Africa are calculated from a pooled dataset, taking into account the original survey design, with individual weights rescaled by the working-age population of each country.

## 2.3 Disability prevalence by demographic characteristics

Table 3 analyses the heterogeneity in the prevalence of disability by age, sex, and place of residence. The statistical significance for differences is calculated using Pearson's chi-squared test, accounting for clustering and stratification, and denoted using stars (\* p<0.10, \*\* p<0.05, \*\*\* p<0.01). The first three columns show the sample split into two groups by age, namely older adults (age 34-49) and younger adults (age 18-33). In all countries, older adults have higher disability prevalence than younger adults, and the results are strongly statistically significant. The difference in disability prevalence between older adults and younger adults is highest in Madagascar and the Central African Republic (6.7 and 6.5 percentage points, respectively) and lowest in Nigeria and Senegal (0.3 and 0.6 percentage points, respectively).

There is a large variation in disability prevalence by sex (column 5-7 of Table 3). While in most countries (14 out of 27) disability prevalence is higher among women than men, in ten countries the difference is not statistically significant, and in three countries (the Gambia, Malawi, and Mali) men have a higher disability prevalence than women. In absolute terms, the highest difference in disability prevalence between women and men is found in the Central African Republic, Sao Tome and Principe, and Madagascar (8.4, 5.9, and 5.2 percentage points, respectively).

Concerning spatial disparities (reported in the last three columns of Table 3), the disability prevalence is significantly higher in rural populations than in urban populations in twelve countries, and lower among rural population compared with urban populations in three countries (Benin, Mauritania, and Mozambique). In the remaining twelve countries, the results are not statistically significant. The largest spatial gap in the prevalence of disability is in Eswatini, where the prevalence among urban residents is 3.9, rising to 8.0 for rural residents (4.1 percentage points difference), followed by the Central African Republic where prevalence in the urban areas is 8.7 per cent and in the rural areas 12.4 per cent (3.7 percentage points difference) and the Gambia with 1.7 per cent for urban areas and 4.1 per cent for rural areas (2.4 percentage points difference).

Turning to the regional results for Africa, based on 27 countries, disability is significantly more prevalent among older adults, women, and rural populations. Disability prevalence for older adults is 4.4 in comparison to 2.3 for younger adults, implying 2.1 percentage points age gap in disability. Disability prevalence for women stands at 3.6 in comparison to 2.3 for men, hence the gender gap in disability is 1.3 percentage points. Finally, disability prevalence for rural residents is 3.4 and for urban residents at 2.6, with the spatial gap in disability standing at 0.8 percentage points.

Table 3.
Disability prevalence by age, sex, and location


Note: Calculations are adjusted for the complex survey design. The ample includes adults (age 18-49). Disability is defined as reporting either “a lot of difficulty” or “cannot do at all” for any of the functional domains. Confidence intervals (95%) are reported in brackets, in the second row for each country. Statistical significance for differences is based on Pearson’s chi-squared test and denoted with stars: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01. Prevalence estimates for Africa are calculated from a pooled dataset, taking into account the original survey design, with individual weights rescaled by the working-age population of each country.

## 2.4 Disability prevalence by asset-based wealth quintiles

This section aims to test whether disability prevalence is different among poorer individuals compared with wealthier ones. The surveys used, DHS and MICS, primarily focus on population, health, nutrition, and fertility, and do not contain information on income or expenditure, making it impossible to construct a poverty variable based on an absolute threshold level of consumption. It is feasible, however, to construct a wealth index that can capture long-term wealth through information on household assets and characteristics and then use it to rank households from asset-poor to asset-rich, thus creating a relative measure of wealth. The wealth index does not provide information on absolute poverty, yet it has been shown that the index produces internally consistent results and can be as effective predictor variable as expenditure, e.g. in the context of school enrolment (Filmer and Pritchett 2001).

The DHS and MICS datasets include a precalculated wealth index, which is used in this study as one of the measures of poverty. The procedure for constructing the wealth index is similar in DHS (Rutstein 2008) and MICS (UNICEF 2016). The index is constructed using information on household ownership of assets (such as televisions, bicycles, or cars), housing characteristics (such as floor and roof materials), and access to services (such as water supply or sanitation). All categorical variables are first transformed into binary indicators and then examined using principal component analysis (PCA). To account for structural differences between rural and urban contexts, PCA is applied separately to the rural and urban samples. The first principal component is retained, and the resulting factor scores $f_{j}$ are used as weights in calculating each household's wealth score as $W_{i} = \sum_{j}(a_{ij} * f_{j})$ where $a_{ij}$ indicates the presence or absence of asset $j$ in household $i$ . These scores are standardized within rural and urban areas, then combined into a single national distribution from which households are ranked and divided into quintiles (poorest, poorer, middle, richer, and richest). This provides a relative measure of household wealth within the survey population.

Table 4 reports disability prevalence, corresponding confidence intervals and the difference in disability prevalence between the highest (richest) and the lowest (poorest) wealth quintiles. At the level of the region, using a pooled dataset of 27 African countries weighted by the working-age population, disability prevalence among working-age individuals increases with asset poverty. The disability prevalence in the lowest (poorest) wealth quintile is 3.8 per cent, declining to 3.5 per cent in the second quintile, 3.3 per cent in the third quintile and 2.8 per cent in the fourth quintile. Among working-age adults in Africa, disability prevalence in the fifth wealth quintile is 2.2 per cent, which is 1.6 percentage points lower than the disability prevalence in the first quintile (standing at 3.8 percent), meaning that the prevalence of disability among the poorest adults is significantly higher than that among the wealthiest adults.

Similar positive and statistically significant relationship between poverty and disability is observed in 16 out of 27 countries in the study: disability prevalence among working-age adults is significantly higher in the poorest quintile than in the wealthiest quintile. The largest difference is observed in Tunisia, where the poorest adults are four times more likely to live with functional limitations than the wealthiest adults; in Eswatini, Kenya, and Nigeria where the poorest are more than three times likelier to live with functional limitations than the wealthiest adults; and in the Gambia, Ghana, and South Africa where the prevalence of disability among poor adults is more than twice as high as that among wealthy adults, with wealth being measured by the asset-based wealth index.

In nine countries, the relationship between asset-based wealth and disability prevalence among working-age adults is not statistically significant. In two countries (Benin and Mauritania), the relationship is negative and statistically significant, implying that the wealthiest adults are more likely to live with functional limitations than the poorest adults, which is contrary to expectations. Two reasons may potentially lead to results that are unexpected or not statistically significant. First, the relationship discussed above is unconditional and does not take into account demographic characteristics such as age, sex, and location, that may influence the results. Second, asset-based index captures only part of the potential deprivations, and a broader measure of poverty can show a different pattern. Both explanations will be explored in the next section.

Table 4.
Disability prevalence by asset-based wealth quintiles


Note: Calculations are adjusted for the complex survey design. The sample includes adults (age 18-49). Disability is defined as reporting either “a lot of difficulty” or “cannot do at all” for any of the functional domains. Confidence intervals (95%) are reported in brackets. Statistical significance for the difference between the lowest and the highest wealth quintile is based on Pearson’s chi-squared test and denoted with stars: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01. Prevalence estimates for Africa are calculated from a pooled dataset, taking into account the original survey design, with individual weights rescaled by the working-age population of each country.

# Disability and probability of living in poverty

## 3.1 Empirical approach

Poverty and disability form a complex, mutually reinforcing relationship (Pinilla-Roncancio 2015, Banks et al. 2017). Disability can lead to poverty through multiple channels. Impairments, coupled with cultural and environmental barriers, limit access for persons with disabilities to education and employment (Mitra et al. 2013), social networks, political and legal processes (Pente et al. 2024), healthcare (Kuper and Heydt 2019) and financial services (United Nations 2024). Persons with disabilities also have to bear high extra costs associated with disability (Mitra et al. 2017) and have lower priority in the distribution of food, land, and water (International Disability Alliance 2023). $^{14}$ This leads to a lower level of human capital, limiting opportunities for work and income generation, and reinforcing the poverty cycle.

Poverty can, in turn, increase the risk of disability (Pinilla-Roncancio et al. 2020). Poor people have lower educational attainment and more dangerous working conditions. They are more likely to have unsafe living conditions and experience malnutrition and poor health (World Health Organization and World Bank 2011). These conditions, coupled with limited access to healthcare, create a higher risk of illness, accident, and impairment (Yeo 2001). Persons with disabilities, even those that are not monetarily poor, are still more likely to experience multiple deprivations such as social isolation and discrimination, and lower education, employment, and psychological well-being (United Nations 2018).

The objective of this section is to estimate the association between poverty and disability, controlling for sociodemographic characteristics but leaving aside the identification of the causal links and pathways. $^{15}$ The estimation is based on weighted probit $^{16}$ regressions modelling the probability of poverty as a function of disability status, controlling for age, sex, urban/rural location, and sub-national region. The following estimated equation is run separately for each country:

$$
P r (P o v e r t y _ {i} = 1) = \beta_ {1} D i s a b i l i t y _ {i} + \beta_ {i} X _ {i} ^ {\prime} + \varepsilon_ {i}\tag{3}
$$

where $Poverty_{i}$ is a binary variable indicating whether adult i is poor, $Disability_{i}$ is a binary variable indicating the presence of disability (defined as having at least a lot of difficulties in any of the functional domains), $X_{i}^{\prime}$ is a vector of control variables, including sex, age, rurality, and sub-national region, and $\varepsilon_{i}$ is an error term. The individual sampling weights, adjusted for clustering and stratification, and provided with the datasets were used to account for the complex survey design and ensure unbiased population estimates and correct variance estimation using Taylor linearization. After the probit estimation, the average marginal effects of disability status on the probability of being poor were calculated and reported in the results section.

For the analysis undertaken at the regional level, the data from 27 countries are pooled into a single dataset, with individual weights rescaled by the working-age population of each country (see Eq.(2)).

$Poverty_{i}$ is measured in two different ways, including asset poverty and multidimensional poverty. Individuals are considered asset poor if they belong to the two lowest quintiles of the asset-based wealth index (discussed in section 2.4). In addition to the asset-based wealth index, this paper employs a Multidimensional Poverty Index (MPI) to capture deprivations beyond economic assets. While the wealth index reflects individuals' relative economic standing within the sample, the MPI identifies absolute deprivations in health, education, and living standards. Using both measures provides a more comprehensive assessment of poverty and allows an examination of whether disability is associated with broader capability deprivation not fully captured by asset ownership.

Individuals are considered multidimensionally poor if they experience deprivations across multiple dimensions of well-being above a selected cut-off. Each dimension can be measured through different indicators. Alkire and Foster (2011) provide a flexible approach that can be adopted to various situations through the selection of dimensions, indicators, and deprivation cut-off. This paper follows Mitra and Yap (2021) in selecting three dimensions, namely education, health, and standards of living, and setting indicators, their weights, and the cut-off point (k > 1 out of maximum possible 3). Indicators were identified by Mitra and Yap (2021) specifically for the disability context by mapping the available questions in the household surveys and censuses with the provisions of the UNCRPD and SDGs. The dimensions, underlying indicators, and their weights are presented in Table 5.

Table 5. Multidimensional poverty index: indicators and weights


Source: Adapted from Mitra and Yap (2021).

The MPI used in this paper differs slightly from the Global MPI developed by the Oxford Poverty and Human Development Initiative and United Nations Development Programme (Alkire et al. 2024). The Global MPI contains three dimensions and ten indicators, while this study uses the same dimensions but adapts indicators and cut offs to the available data. Furthermore, for ease of results interpretation, the MPI used in this study refers to the prevalence (headcount ratio) of multidimensional poverty, while the Global MPI combines both prevalence and intensity of poverty in a single headline index.

## 3.2 Regression results

Table 6 reports the average marginal effects of probit regressions. The regressions estimate the probability of living in poverty as a function of disability status, first unconditionally, and then factoring in a number of controls identified as important by the preceding literature (sex, age, place of residence, and sub-national region). $^{17}$ The first two columns report results of regressions where the dependent variable is asset poverty, a relative measure, defined as falling in the two lowest quintiles of the asset-based wealth index, the following two columns show regression results where the dependent variable is the MPI, and the last column contains in-sample prevalence of disability for ease of reference. The preferred specifications are those including controls; the results of unconditional probit regressions of disability status on asset poverty and disability status on multidimensional poverty are provided for completeness and for comparison with results where demographic characteristics are taken into account.

The numbers reported in Table 6 are the average marginal effects on the dummy variable identifying disability, and hence can be interpreted as the average difference in the probability of poverty between persons with disabilities and persons without disabilities, while keeping all other parameters constant. For example, in Chad, living with a disability increases the probability of being asset poor by 5 percentage points (second column) or by 4 percentage points when age, rural/urban residence, sex, and sub-national location are taken into account (third column). In twelve out of 27 countries, disability among adults is strongly associated with asset poverty, raising the probability of asset poverty by 3 to 13 percentage points, depending on the country.

Taking into account the demographic characteristics, such as age, sex, rural/urban location, and sub-national region, the largest difference in the probability of asset poverty between persons with and without disabilities is found in Eswatini (13 percentage points) and Nigeria (11 percentage points), followed by Ghana, Kenya, Mali, and Tunisia (7 percentage points) and Uganda (6 percentage points) (third column of Table 6). In the Central African Republic and South Africa, adults with disabilities are 5 percentage point more likely to be asset poor, in Chad and Rwanda this number stands at 4 percentage points, and in Zimbabwe – 3 percentage points. In almost all cases with significant results, adding demographic controls slightly reduces the magnitude of the effect of the disability status, suggesting that age, rural/urban residence, sex, and sub-national location are significant correlates of poverty that need to be taken into account.

Some results are not statistically significant or suggest a negative relation between asset poverty and disability. In Benin, Lesotho, and Mauritania, the coefficients are negative and statistically significant, contrary to expectations. Noting that these three countries are among the poorest on the continent, $^{18}$ the potential reason may be in the cut-off set at the bottom 40 per cent of the asset-based wealth index, thus comparing asset-poor individuals with individuals that are better off in terms of assets but still own very little. Indeed, when the cut off is increased to 60 per cent, that is, individuals are considered asset poor if they belong to the three lowest wealth quintiles, the coefficients are no longer significant and negative. In the other eleven countries, the results with asset poverty as the dependent variable (third column of Table 6) are not statistically significant. This, however, does not prove the absence of a relationship between poverty and disability. A lack of statistical significance should not necessarily be interpreted as evidence of no relationship, but rather as a reflection of design-based adjustments and data limitations. Survey-adjusted models typically produce larger standard errors than unweighted regressions because they incorporate clustering, stratification, and unequal sampling weights.

When poverty is measured through the MPI (columns 4 and 5 of Table 6), the results suggest a strong and statistically significant impact of disability status on the multidimensional poverty experienced by the African working-age adults. In the regressions accounting for sociodemographic characteristics, the results are significant in 16 out of 27 countries, with the sign of the coefficients on disability always positive, i.e. the disability status is associated with a higher risk of poverty (column 5 of Table 6). The additional risk of poverty attributable to disability is highest in Nigeria, where working-age adults with disabilities are 16 percentage points more likely to be multidimensionally poor than adults without disabilities, followed by South Africa with 15 percentage points difference, Kenya with 11 percentage points difference and Eswatini with 10 percentage points difference. Living with disability in Ghana increases the risk of multidimensional poverty among working-age adults by 9 percentage points, in Sierra Leone – by 8 percentage points, in Uganda – by 7 percentage points, and in Chad, Comoros, Mali, and the United Republic of Tanzania – by 6 percentage points. Slightly smaller differences in the risk of multidimensional poverty are found in Benin, Mozambique, and Rwanda where working-age adults with disabilities are 5 percentage points more likely to be multidimensionally poor than their peers without disabilities, in Tunisia, where this difference stands at 4 percentage points, and in the Central African Republic with a 2-percentage-points difference. These numbers imply a sizable total effect at the national level, given that disability prevalence (in sample) ranges from 0.7 to 9.6 per cent (last column of able 6).

The regional results for Africa are based on the pooled dataset comprising 27 countries weighted by working-age population and taking into account the original survey design. African working-age adults with disabilities face higher risk of asset poverty and multidimensional poverty than their peers without disabilities, even after controlling for sociodemographic characteristics. The difference in probability of asset poverty is 4 percentage points higher for adults with disabilities, and the difference in probability of multidimensional poverty is 9 percentage points higher. These numbers are both statistically and economically significant, given that they add up to an already high unconditional probability of poverty. The headcount of multidimensional poverty in Africa is 58 per cent (in sample), which increases to 67 per cent for persons with disabilities.

Table 6.
Association between disability and poverty: Average marginal effects of a probit model


Note: Average marginal effects of probit regressions. \* p<0.1, \*\* p<0.05, \*\*\* p<0.01. Calculations are adjusted for the complex survey design, and strata with one sampling unit are centred at the grand mean. Robust standard errors are reported in the second row for each country, followed by the number of observations. The sample includes adults age 18-49. Controls include sex, age, place of residence (urban vs rural), and sub-national region. Regressions for Africa are based on a pooled dataset, taking into account the original survey design, with individual weights rescaled by the working-age population of each country. Disability prevalence (last column) is calculated for the same sample as the MPI regressions with controls.


# Conclusions and policy discussion

This paper compiles and analyses the largest dataset to date on disability and poverty in Africa. It includes disability prevalence figures for 52 countries, with detailed analysis for 27 countries that have standardized, internationally comparable data from nationally representative surveys using the Washington Group Short Set of Questions on Functioning. For these 27 countries, the paper provides national prevalence estimates for working-age adults, disaggregated by functional domain, sociodemographic characteristics, and wealth quintiles. The findings show that disability is more common among older adults, rural residents, women, and people from poorer households. At the regional level, the population-weighted prevalence of disability among working-age adults in Africa is 3.1 per cent, rising to 17.5 per cent when mild functional difficulties are included. The most frequent difficulties are in cognition, seeing, and mobility. Prevalence is higher for women than men (3.6 vs. 2.3 per cent), higher in rural compared to urban areas (3.4 vs. 2.6 per cent), and increases with age.

Disability and poverty reinforce one another, creating a vicious cycle. In Africa, disability prevalence is higher among the poor, and the likelihood of both asset and multidimensional poverty is higher among persons with disabilities. In the poorest asset quintile, disability prevalence is on average 3.8 per cent—1.6 percentage points higher than in the richest quintile (2.2 per cent). Even after adjusting for sociodemographic factors, disability remains strongly associated with poverty: adults with disabilities are, on average, 4 percentage points more likely to be asset poor and 9.4 percentage points more likely to be multidimensionally poor. At the country level, the positive and statistically significant association between disability status and multidimensional poverty holds in 16 out of 27 countries analysed.

These findings underline that eliminating extreme poverty is not possible without addressing the specific challenges faced by persons with disabilities. Ending poverty among persons with disabilities is also essential to ensuring their rights to dignity, opportunity, and full societal participation. And while economic growth is an important vehicle for poverty elimination, growth alone will not close the gap between persons with and without disabilities (Groce and Kett 2013; Lewis, Mitra, and Yap 2022), calling for active government participation. Policy responses should pursue a twin-track strategy that combines the mainstreaming of disability across all sectors with targeted measures. Mainstreaming recognises disability as a cross-cutting issue affecting broad population groups, whereas targeted interventions focus on the specific needs of persons with disabilities to ensure their equal participation (United Nations 2024).

Based on this twin-track approach and guided by the findings, the paper suggests five action areas. First, disability inclusion should be fully integrated into national poverty reduction strategies and development frameworks, with clear objectives, budgetary commitments, and attention to intersectional disadvantages. Mainstreaming across sectors—including labour, health, education, and social welfare—is essential to making progress.

Second, governments should strengthen continuous data collection that links disability, poverty, and socioeconomic conditions. Standardized measures, such as the WGSS, should be included in national censuses, labour force surveys, and household surveys, as well as event-specific data collection efforts, such as surveys on the impact of pandemics or natural disasters. It is critical to continue international surveys, such as DHS and MICS, while ensuring their samples are nationally representative, including by age group. Expanded information, particularly on the onset of disability, support received, and environmental barriers, is especially important for analysing pathways between disability and poverty and designing better policies.

Third, poverty-reduction policies must be evaluated for their impact on persons with disabilities. Disability-disaggregated data collection should be incorporated from the design stage of policies to improve accountability and efficiency. Furthermore, understanding the extra costs of disability is critical, as poverty among persons with disabilities and members of their households is likely to be underestimated when these costs and unmet needs are ignored. Inclusion of these extra costs can help adequately and fairly evaluate the poverty level among persons with disabilities and adjust benchmarks for accessing disability-related entitlements and the targeting of interventions.

Fourth, inclusive employment and economic empowerment should be actively promoted. This includes expanding employment, entrepreneurship, and self-employment opportunities for persons with disabilities through microfinance and grants, incentivizing employers and introducing quotas where appropriate, and ensuring vocational training for persons with disabilities is both accessible and aligned with labour market demand.

Finally, governments should improve access to social protection for persons with disabilities. Acknowledging the fiscal constraints of many African countries, the elimination of chronic poverty requires adequate support of persons with disabilities through social safety nets. Programmes such as targeted cash transfers, health insurance, inclusive pension schemes, and other social protections for persons with disabilities, particularly those who are unemployed or work in the informal sector, can help mitigate chronic poverty.

By implementing comprehensive policies that target poverty reduction and promote inclusion, accessibility, and equality, African governments can improve the socioeconomic outcomes for persons with disabilities and advance their rights to dignity, opportunity, and full participation in society.

## References


Alkire, Sabina, Usha Kanagaratnam, and Nicolai Suppa. 2024. The Global Multidimensional Poverty Index (MPI) 2024. Country Results and Methodological Note.


Banks, Lena Morgon, Hannah Kuper, and Sarah Polack. 2017. “Poverty and Disability in Low- and Middle-Income Countries: A Systematic Review.” PLOS ONE 12 (12): e0189996. https://doi.org/10.1371/journal.pone.0189996.

Carpenter, B., Kamalakannan, S., Patchaiappan, K., Theiss, K., Yap, J., Hanass-Hancock, J., Murthy, GVS, Pinilla-Roncancio, M., Rivas Velarde, M., and Mitra, S. 2024. The Disability Statistics – Estimates Database: an innovative database of internationally comparable statistics on disability inequalities. International Journal of Population Data Science. Vol. 8(6). https://doi.org/10.23889/ijpds.v8i6.2478.

DDI. 2024. Disability Statistics – Estimates Database (DS-E Database). Disability Data Initiative collective. Fordham University: New York, USA. https://ds-e.disabilitydatainitiative.org/DS-E/.

ESCWA. 2023. Disability in the Arab Region 2023.

Filmer, Deon. 2008. “Disability, Poverty, and Schooling in Developing Countries: Results from 14 Household Surveys.” World Bank Economic Review 22 (1): 141–63. https://doi.org/10.1093/wber/lhm021.


Filmer, Deon, and Lant H. Pritchett. 2001. “Estimating Wealth Effects without Expenditure Data-or Tears: An Application to Educational Enrollments in States of India.” Demography 38 (1): 115–32. https://doi.org/10.2307/3088292.

Groce, Nora, Gayatri Kembhavi, Shelia Wirz, Raymond Lang, Jean-Francois Trani, and Maria Kett. 2011. “Poverty and Disability – A Critical Review of the Literature in Low and Middle-Income Countries.” SSRN Electronic Journal, ahead of print. https://doi.org/10.2139/ssrn.3398431.

Groce, Nora, and Maria Kett. 2013. “The Disability and Development Gap.” SSRN Scholarly Paper No. 3385372. Rochester, NY. https://doi.org/10.2139/ssrn.3385372.

Hanass-Hancock, Jill, G. V. S. Murthy, Michael Palmer, Monica Pinilla-Roncancio, Minerva Rivas Velarde, and Sophie Mitra. 2023. “The Disability Data Report 2023.”

Hoogeveen, Johannes G. 2005. “Measuring Welfare for Small but Vulnerable Groups: Poverty and Disability in Uganda.” Journal of African Economies (United Kingdom) 14 (4): 603–31. https://doi.org/10.1093/jae/eji020.


International Disability Alliance. 2023. Access to WASH for Women and Girls with Disabilities in French-Speaking West African Countries.

Kuper, Hannah, and Phyllis Heydt. 2019. The Missing Billion: Access to Health Services for 1 Billion People with Disabilities. London School of Hygiene & Tropical Medicine.

Lewis, Emily, Sophie Mitra, and Jaclyn Yap. 2022. “Do Disability Inequalities Grow with Development? Evidence from 40 Countries.” Sustainability (Basel, Switzerland) 14 (9): 5110-. https://doi.org/10.3390/su14095110.


Mitra, Sophie, Aleksandra Posarac, and Brandon Vick. 2013. “Disability and Poverty in Developing Countries: A Multidimensional Study.” Word Development 41: 1–18.

Mitra, Sophie, and Jaclyn Yap. 2021. The Disability Data Report 2021. https://www.ssrn.com/abstract=4492005.

Mitra, Sophie, and Jaclyn Yap. 2022. The Disability Data Report 2022. https://doi.org/10.2139/ssrn.4492005.


Montes, Jose, and Rachel Swindle. 2021. Who Is Disabled in Sub-Saharan Africa? Poverty and Equity Notes No. 40. World Bank

Pente, Vladimir Y., Anita Jeyam, Stevens Bechange, et al. 2024. “Electoral Participation of People with and without Disabilities in Urban Communities in Cameroon and Senegal.” African Journal of Disability. https://doi.org/10.4102/ajod.v13i0.1399.

Pinilla-Roncancio, Monica. 2015. “Disability and Poverty: Two Related Conditions. A Review of the Literature.” Revista de La Facultad de Medicina 63 (3Sup). https://doi.org/10.15446/revfacmed.v63n3sup.50132.


Rutstein, Shea O. 2008. “The DHS Wealth Index: Approaches for Rural and Urban Areas.” DHS Working Papers.


Trani, Jean-Francois, and Mitchell Loeb. 2012. “Poverty and Disability: A Vicious Circle? Evidence from Afghanistan and Zambia.” Journal of International Development 24 (S1): S19–52. https://doi.org/10.1002/jid.1709.

UNICEF. 2016. “Review of Options for Reporting Water, Sanitation and Hygiene Coverage by Wealth Quintile.” MICS Methodological Paper 4. https://mics.unicef.org/sites/mics/files/2024-05/MICS%20Methodological%20Paper%204.pdf.

United Nations. 2006. Convention on the Rights of Persons with Disabilities.

United Nations. 2018. Disability and Development Report 2018: Realizing the Sustainable Development Goals by, for and with Persons with Disabilities. United Nations.


United Nations. 2024. Disability and Development Report 2024: Accelerating the Realization of the Sustainable Development Goals by, for and with Persons with Disabilities. United Nations. https://social.desa.un.org/sites/default/files/publications/2024-06/Final-UN-DDR-2024-Executive%20Summary.pdf.

United Nations, and Oxford Poverty and Human Development Initiative. 2024. Global Multidimensional Poverty Index 2024: Poverty Amid Conflict. https://hdr.undp.org/system/files/documents/hdp-document/mpireport2024en.pdf.

Washington Group on Disability Statistics. 2021. “Creating Disability Severity Indicators Using the WG Short Set on Functioning.” https://www.washingtongroup-disability.com/fileadmin/uploads/wg/WG\_Document\_\_5G\_-\_Analytic\_Guidelines\_for\_the\_WG-SS\_\_Severity\_Indicators\_-\_STATA\_.pdf.

World Health Organization. 2001. International Classification of Functioning, Disability and Health. WHO. https://icd.who.int/browse/2025-01/icf/en.

World Health Organization and World Bank. 2011. World report on disability 2011. https://iris.who.int/handle/10665/44575.

Yeo, Rebecca. 2001. “Chronic Poverty and Disability.” Background Paper Number 4, Chronic Poverty Research Centre.

## Data and Stata code

Author gratefully acknowledges the Stata code for calculating the disability prevalence and MPI for the DHS data received from Disability Data Initiative as part of its Disability Statistics - Estimates Database https://www.ds-e.disabilitydatainitiative.org/DS-E/ and https://github.com/bscarp/DDI/tree/main/Estimate%20scripts, the code for calculating the disability prevalence for the MICS data written by the team in UNICEF and downloaded from GitHub https://github.com/micseagle/STATA and the code for the DHS data analysis written by the team of the DHS Program and downloaded from GitHub https://github.com/DHSProgram/DHS-Indicators-Stata.

All data were obtained from public sources and are freely available or available upon request. The specific sources for each country are provided in Table A1 and A2 of the Annex.

DHS: Demographic and Health Surveys (DHS) Datasets, the DHS Program, accessed from https://dhsprogram.com.

MICS: Multiple Indicator Cluster Surveys (MICS) Datasets, UNICEF, accessed from https://mics.unicef.org.

Population and GDP: Population, total; and population by age group; GDP per capita (constant 2015 US\$), UNCTAD Data Hub, accessed from https://unctadstat.unctad.org.

Poverty: Poverty headcount ratio at \$2.15 a day (2017 PPP) (% of population), World Development Indicators, World Bank, accessed from https://databank.worldbank.org/

# Annex: Data sources and coverage

## Table A1. Disability data coverage by demographic characteristics

Number of respondents with information on functional difficulties


Note: Unweighted data. DHS stands for Demographic and Health Surveys accessible at https://www.dhsprogram.com/. MICS means Multiple Indicator Cluster Surveys accessible at https://mics.unicef.org/.

Table A2.
Prevalence of functional difficulties in countries not included in the primary analysis


Note: Disability prevalence is from secondary sources, which are based on varying definitions and samples. Asterisk next to the country name (\*) indicates disability questions other than the WGSS. In case of Djibouti, Ethiopia, Liberia, Mauritius, Morocco and Namibia disability is defined as having at least one response “a lot of difficulty” or “cannot do at all” in any functional domain. (\*\*) In case of Cabo Verde the prevalence refers to any level of difficulty. Sample coverage varies and is reported in the last column if available. DDI stands for the Disability Data Initiative, accessible at https://www.disabilitydatainitiative.org and UNSD refers to United Nations Statistics Division’s data on disability, accessible at https://unstats.un.org/unsd/demographic-social/sconcerns/disability/statistics.


@UNCTAD
@UNCTAD
unctad.org/facebook
unctad.org/youtube
unctad.org/flickr
unctad.org/linkedin
