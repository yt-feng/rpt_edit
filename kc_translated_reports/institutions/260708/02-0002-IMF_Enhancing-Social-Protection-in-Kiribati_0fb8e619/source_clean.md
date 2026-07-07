# Enhancing Social Protection in Kiribati

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on April 24, 2026. This paper is also published separately as IMF Country Report No 26/100.

2026
JUL


# IMF Selected Issues Paper Asia Pacific Department

Enhancing Social Protection in Kiribati Prepared by Ni Wang (APD)

Authorized for distribution by Corinne Deléchat
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on April 24, 2026. This paper is also published separately as IMF Country Report No 26/100.

ABSTRACT: Kiribati expanded social protection spending in response to COVID, drastically reducing poverty. Concurrently, an increase in untargeted social protection receipts has supported spending on goods that do not enhance human development and may have negative externalities. Causal evidence is established based on discontinuity in age-eligibility with a control function approach. We discuss policy options to enhance social protection taking into account logistical and capacity constraints.

RECOMMENDED CITATION: Ni Wang. 2026. Enhancing Social Protection in Kiribati. IMF Selected Issues Paper SIP/2026/057.

JEL Classification Numbers:

C26, D12, I32, I38

Keywords:

Social protection, unemployment benefits, copra subsidy, household income and consumption survey, targeting and efficiency

Author's E-Mail Address:


# Enhancing Social Protection in Kiribati

Kiribati

Prepared by Ni Wang $^{1}$

## KIRIBATI


April 24, 2026


Prepared by Ni Wang (APD).

Department

## CONTENTS

ENHANCING SOCIAL PROTECTION IN KIRIBATI 2
A. Introduction 2
B. Social Protection Programs in Kiribati 4
C. Social Protection Benefits and Spending: 2019 vs 2023 5
D. What to Spend on, and How Much? Extensive and Intensive Margins 7
E. Conclusions and Policy Recommendations 9

## References.

## TABLES

1. Poisson Pseudo Maximum Likelihood Estimates of Spending Semi-Elasticities in 2019/20 HIES \_\_\_\_ 12
2. Poisson Pseudo Maximum Likelihood Estimates of Spending Semi-Elasticities in 2023/24 HIES \_\_\_\_ 12
3. Logit Estimates of Spending Odds Semi-Elasticities in 2023/24 HIES \_\_\_\_ 13
4. Estimates of Spending Semi-Elasticities Conditional on Spending>0 in 2023/24 HIES \_\_\_\_ 14
5. PPML with Control Function Estimates of Spending Semi-Elasticities in 2023/24 HIES \_\_\_\_ 15
6. Diagnostic Statistics for the PPML with Control Function Approach (2023/24 HIES) 15
7. Logit with Control Functions: Estimates of Spending Odds Semi-Elasticities in 2023/24 HIES \_\_\_\_ 16
8. Control Function Estimates of Spending Semi-Elasticities Conditional on Spending >0 in 2023/24 HIES \_\_\_\_ 17
9. Diagnostic Statistics for the Hurdle Model with Control Function Approach (2023/24 HIES) \_\_\_\_ 18

## ANNEX

I. Robustness and Causal Inference 19

# ENHANCING SOCIAL PROTECTION IN KIRIBATI

Kiribati expanded social protection spending in response to COVID, drastically reducing poverty. Concurrently, an increase in untargeted social protection receipts has supported spending on goods that do not enhance human development and may have negative externalities. We discuss policy options to enhance social protection taking into account logistical and capacity constraints.

## A. Introduction

1. Kiribati is a remote, geographically dispersed Pacific Atoll country facing large human development and public infrastructure investment needs. Kiribati has a population of 127 thousand people, located in islands spanning 3.4mn km $^{2}$ of ocean. Shipping costs and lack of connectivity and infrastructure, especially on the outer islands, limit market sizes and service delivery. As a result, the economy is dependent on public spending funded by large but volatile fishing license revenues. Key social safety nets, including free education up to age 15, health care, unemployment, senior citizen and disability benefits, are provided by the government. The country is vulnerable to weather shocks and the long-run threat of rising sea levels, and the cost of building resilience to rising sea levels is very high (IMF 2025, Selected Issues Paper).

2. The expansion of social protection during the COVID-19 pandemic $^{1}$ supported households amid increased costs of living and contributed to a sharp reduction in poverty. The 2019/20 and 2023/24 Household Income and Expenditure Surveys (HIES) show that the poverty rate fell from 21.9 to 5.5 percent, and inequality declined as the Gini coefficient fell from 27.8 to 24.7. Poverty declined across all regions, including outer islands where reductions reached around 20 percentage points, and the urban–rural poverty gap narrowed. Extreme poverty (US2.15/day, 2017 PPP) was almost eliminated (0.04 percent in 2023/24). On non-monetary measures, sanitation deprivation fell from 56 percent to 35 percent between both surveys, while access to electricity and water and asset ownership (e.g., vehicles) improved.

3. Between 2019 and 2023, growth in social transfers was transformative for lower-income households, driving most of their increase in household income. Bottom-quartile households saw only modest increases in copra-related income and remittances, while formal labor income (excluding copra) was broadly unchanged. This reflects limited access to formal employment, particularly for outer-island low-income households reliant on coconut farming, and for some low-income Tarawa residents constrained by low educational attainment and limited employment opportunities. In contrast, income growth of richer households (those in top 3 quartiles of the income distribution) was mainly driven by work income, often in government and the formal sector, though they also benefited from social transfers.


[[KC_IMAGE_001]]

Contributions to Average Total Household Income Growth (From 2019 to 2023; in percentage point)


[[KC_IMAGE_002]]


[[KC_IMAGE_003]]

Contributions to Average Total Household Expenditure Growth
(From 2019 to 2023; in percentage point)


[[KC_IMAGE_004]]


4. As a result of higher income, all households increased spending on food and substances (tobacco, alcohol, and kava), with limited growth in other spending categories. This suggests that a non-trivial share of the growing income was spent on goods that do not increase human development and may have negative health consequences. This motivates an examination of how additional benefits impact spending decisions.

5. This paper analyzes the effect of social transfers on household spending and draws policy implications. Section B describes Kiribati's current social protection programs, their progressivity, and cross-country comparisons. Section C documents how the relationship between social transfers and household spending changed between 2019 and 2023. Section D focuses on the 2023/24 HIES round and explores how social benefits affect the probability of spending on different categories (extensive margin) and how much to spend, conditional on spending (intensive margin). An age-eligibility-based fuzzy regression discontinuity strategy establishes a causal link between unemployment receipts and substance spending. Section E concludes with policy recommendations to strengthen efficiency, improve targeting and program coordination, and mitigate negative externalities.

## B. Social Protection Programs in Kiribati

## 6. Social protection programs in Kiribati include:

\- Copra subsidies, which aim to support the income of outer-island residents by purchasing copra at AUD 4/kg (doubled from AUD 2/kg in 2022), around four times the global market price, to produce coconut oil at state-owned coconut processing plants. Copra subsidy is the largest benefit, at 9 percent of GDP in 2025.

\- Unemployment benefits, introduced in 2022 via a Support Fund for Unemployment (SFU), which provide AUD 50 per person per month for people aged 18-60 who are not formally employed. Because of high informality in Kiribati, unemployment benefits reached close to universal coverage—about 95 percent of people in 2023/24 lived in a household with at least one SFU recipient, with about 2.4 beneficiaries per recipient household. The payments are paid on quarterly basis due to payment capacity constraints. Unemployment benefits stood at about 5 percent of GDP in 2025.

\- Senior citizen allowance, a fixed cash transfer for age-eligible elderly people. In 2020, the age requirement was reduced from 65 to 60 and the amount approximately tripled to AUD 200-300 per month per person. Senior citizen benefits were at 4 percent of GDP in 2025.

\- Disability allowance for people with permanent disabilities, introduced in 2020. Disability allowance is the smallest benefit in the aggregate, amounting to just 1 percent of GDP in 2025.

While senior citizen allowances and disability allowances belong to the traditional type of social assistance (the definition that this paper follows), the Government of Kiribati considers SFU as a form of social assistance as well. Benefit delivery is highly cash-dependent and is gradually transitioning towards digital payments. $^{2}$ Kiribati also has a contributory pension system via the Kiribati Provident Fund.

## 7. Kiribati social protection programs exhibit different degrees of progressivity.

Unemployment benefits, senior citizen and disability allowances decline with household consumption, though unemployment benefits are less well targeted, with a flatter decline across consumption levels. In contrast, copra benefits and contributory pensions increase with household consumption. $^{3}$ The substantial heterogeneity in progressivity across programs indicates scope for enhancing the efficiency and equity of social spending.


[[KC_IMAGE_005]]


## 8. Traditional social assistance—senior citizen and disability allowances—has broad coverage, but overall social spending is high, with some overlap across programs. About 30

percent of senior citizen and disability transfers accrue to Kiribati households in the bottom consumption quintile, and almost 50 percent of people in the bottom quintile live in a household where at least one member receives these transfers, indicating high coverage and incidence, respectively. At the same time, spending on traditional social assistance is higher than in comparator countries and other Pacific Islands. Unemployment benefits are much higher than in the OECD. In addition, around 94 percent of the copra subsidy recipient households also receive unemployment benefits.


[[KC_IMAGE_006]]


[[KC_IMAGE_007]]


## C. Social Protection Benefits and Spending: 2019 vs 2023

9. This paper uses the two HIES waves to document how spending responses have changed between 2019/20 and 2023/24. Given the possibility of zero spending on certain categories (e.g. education, health, substance), Poisson Pseudo Maximum Likelihood (PPML) estimator is used, which allows consistent estimation of semi-elasticities in the presence of heteroskedasticity and zeros in the dependent variable. The specification $^{4}$ includes a rich set of fixed effects (village fixed effects; household head ethnicity, education, gender, age, marital status, and labor force status; indicators for home ownership, church donations, and car ownership). Additional controls include non-transfer income, household size, and the number of children and seniors, ensuring that estimates capture the marginal association between transfer receipts and spending behavior conditional on household characteristics and location.

## 10. Key findings $^{5}$ are as follows:

\- In 2019, social protection receipts were positively associated with spending on food, health, and business expenditure. Copra income, the largest benefit at the time, was associated with higher spending on food and business expenditure, but also with increased expenditure on alcohol/ tobacco, pointing to mixed effects on human development. Senior citizen allowance receipts were associated with higher household spending on food, health and business, alongside lower spending on alcohol/tobacco, suggesting that these transfers supported human development. Pension income was associated with higher spending on education and health, as well as kava.

\- In 2023, the link between social protection and human development spending is less clear. Unemployment benefits, now the largest, are associated with lower spending on education and high spending on substances, including alcohol, tobacco, and kava. Copra income remains positively associated with spending on food and business expenditure, and pension income is associated with higher spending on education and kava. Senior and disability allowances are no longer statistically significantly associated with a specific type of spending.


11. A causal effect of unemployment benefits on alcohol, tobacco, and kava spending is established using fuzzy regression discontinuity (Annex I). Instruments are constructed based on the number of household members who are eligible for unemployment benefits given their age (19-59). Estimation is implemented via a control-function (two-stage residual inclusion) approach with PPML in the second stage. Results (Tables 5-6) confirm a statistically significant causal effect of unemployment receipts on substance spending, with larger estimated semi-elasticities than in baseline regressions. For technical details see Annex I.

## D. What to Spend on, and How Much? Extensive and Intensive Margins

12. The impact of social protection receipts on the decision to spend or not is explored in a hurdle model. Around 11 percent of households did not report any substance spending. The shares of households not reporting spending on education, health (both largely government-provided), and business expenditure are 28 percent, 79 percent, and 51 percent, respectively. It is thus useful to separately consider the decision to spend or not (extensive margin) and the decision on how much to spend (intensive margin). An indicator variable for bottom quartile (by per capita consumption) households and its interaction with unemployment receipts are used to examine whether poorer households have different spending responses to unemployment receipts than richer households. $^{6}$

## 13. Bottom-quartile households are significantly less likely to spend on alcohol and

13. Bottom quartile households are significantly less likely to spend on alcohol and tobacco given unemployment receipts. $^{7}$ Overall, the extensive margin estimation yields similar patterns to the level regressions, where unemployment receipts are found to be associated with lower probability of spending on education (as well as health and business although the magnitudes are small) and higher probability of spending on substances. Importantly, the said association with alcohol/tobacco spending is much weaker among bottom-quartile households, with a statistically significant negative coefficient on the interaction term between unemployment receipts and the bottom-quartile dummy.


## 14. As a result, the overall average marginal effect of unemployment receipts on substance spending is smaller among bottom-quartile households. On average, an additional

AUD in SFU receipts is associated with 34 cents in alcohol/tobacco spending in the top three quartiles and 25 cents in the bottom quartile. $^{8}$ A similar result was found for kava, but the difference between households in the bottom quartile versus the top three quartiles is not statically significant. The causality relation between unemployment benefits and substance spending is also confirmed using the fuzzy regression discontinuity approach and are robust to the inclusion of additional controls and use of other functional forms for estimation (see Annex I and Tables 7-9).


15. Finally, as a robustness check, spending across categories is compared for households eligible for unemployment benefits versus senior citizens' benefits. The charts below compare (potential) SFU recipient households and senior citizen allowance recipient households, based on the number of age-eligible household members for each benefit. Relative to an average non-recipient household, spending on kava and tobacco on average increases markedly faster than spending on food as the number of SFU-age-eligible people in the household increases. However, spending on substances does not increase substantially more than spending on food with the number of senior citizens in the household.


$$
\frac {\partial \mathrm{E} (\mathrm{y} _ {\mathrm{i}})}{\partial \text {SFUIncome} _ {\mathrm{i}}} = \frac {\partial \mathrm{P} (\mathrm{y} _ {\mathrm{i}} > 0)}{\partial \text {SFUIncome} _ {\mathrm{i}}} \times \exp \left((\widehat {\log y _ {1}})\right) + \mathrm{P} (\widehat {\mathrm{y} _ {1} > 0}) \times \frac {\partial \mathrm{E} (\mathrm{y} _ {\mathrm{i}} | \mathrm{y} _ {\mathrm{i}} > 0)}{\partial \text {SFUIncome} _ {\mathrm{i}}},
$$

## E. Conclusions and Policy Recommendations

16. Social protection benefits play an important role in pursuing inclusive growth in Kiribati and have contributed to a substantial, rapid reduction in poverty. Given limited access to education, difficulties in reaching formal labor markets, and lack of scale economies, especially on rural areas and on outer islands, social benefits ensure that most I-Kiribati have access to basic income. These benefits provide an opportunity to pursue education, start a business, and enter the formal labor force. In an environment where means testing is not feasible due to capacity constraints, the current approach has been effective in supporting the population during the extraordinary negative shocks of the COVID-19 pandemic in 2020 and the cost-of-living crisis in 2022 and 2023.

17. However, given the need to maintain fiscal sustainability while addressing the investment needs of climate-resilient infrastructure, it is important to enhance efficiency of social benefits while balancing their policy objectives. Some instruments—most notably unemployment benefits and the copra subsidy—operate at very large scale with limited targeting, leading to leakage to better-off households and potential distortions. Efficiency would be improved if desired outcomes (such as poverty reduction, better health, and education) could be achieved at lower fiscal cost. This implies assessing programs jointly along several criteria primarily focusing on coverage (whether beneficiaries and benefit shares are concentrated among poorer households), and efficiency (how much poverty and inequality are reduced per dollar spent), while ensuring that the overall social protection program is fiscally sustainable. IMF 2022 provides a detailed overview on how to design and institutionalize a spending review.

## 18. A reform agenda should include:

\- Increasing excises on tobacco and alcohol and introducing an excise on kava. These revenue measures would curb spending with negative public health externalities. They would help improve human development and should supplement expenditure measures.

\- Continuing copra subsidy reforms. The copra subsidy should be reformed to avoid distorting agricultural production. It could shift more towards low-income households by introducing caps or progressively replacing broad price support with targeted cash transfers.

\- Reviewing the adequacy and efficiency of social benefits. A review of social benefits could rationalize overlaps between programs (e.g. copra subsidy and unemployment benefits), reduce potential benefit leakage, and improve targeting.

19. Improving delivery and administration systems is central to both efficiency and equity. Reducing cash dependence, strengthening beneficiary identification and records, and modernizing payment channels would help lower administrative costs, improve timeliness and transparency, and enable agile support without expanding untargeted transfers. Overall, the design of social protection should avoid introducing market distortions, supporting spending with negative externalities, or providing higher benefits to richer households. While true targeting (e.g. means testing) has

prohibitively high administrative costs in Kiribati, targeting could be improved by tightening program eligibility, for example by capping the copra subsidy and preventing copra and unemployment benefits from accruing to the same households. IMF, 2019 provides further details on the trade-offs involved in different approaches to targeting. Overall, policies should ensure that scarce public resources are redirected toward high-impact services and well-targeted transfers that primarily benefit lower-income households.

## References


Terza, J. V., Basu, A., & Rathouz, P. J. (2008). Two-stage residual inclusion estimation: Addressing endogeneity in health econometric modeling. Journal of Health Economics, 27(2), 531-543.

Santos Silva, J. M. C., & Tenreyro, S. (2006). The log of gravity. Review of Economics and Statistics, 88(4), 641–658.

Sargan, J. D. (1958). The estimation of economic relationships using instrumental variables. Econometrica, 26(3), 393–415.

World Bank. 2024. Beyond Copra. World Bank

Table 1. Kiribati: Poisson Pseudo Maximum Likelihood Estimates of Spending Semi-Elasticities in 2019/20 HIES


Table 2. Kiribati: Poisson Pseudo Maximum Likelihood Estimates of Spending Semi-
Elasticities in 2023/24 HIES


Table 5. Kiribati: PPML with Control Function Estimates of Spending Semi-Elasticities in 2023/24 HIES


Table 6. Kiribati: Diagnostic Statistics for the PPML with Control Function Approach (2023/24 HIES)


Table 8. Kiribati: Control Function Estimates of Spending Semi-Elasticities Conditional on Spending>0 in 2023/24 HIES


## Annex I. Robustness and Causal Inference

1. To address endogeneity concerns, we develop an identification strategy for causal effects by exploiting the discontinuity in age eligibility for SFU. Despite the rich set of controls and fixed effects, SFU receipts could still be endogenous and correlated with omitted factors determining spending patterns. We construct a series of instrumental variables that indicate whether the number of people aged 19-59 in each household is no less than one, two, and so on. These instruments are meant to capture exogenous variation in SFU receipts due to discontinuity in age eligibility. Put differently, the identification relies on the imperfect discontinuity (i.e., fuzzy regression discontinuity) in SFU receipt (treatment intensity) across otherwise similar households who have members close enough in age but vary in eligibility of SFU solely due to the age differences. An apparent concern is that the publicly available HIES data uses five-year grouping for age, and that five years in age difference may not be small enough for the instruments to be truly exogenous. However, the Sargan overidentification test cannot reject the null that the instruments are endogenous, alleviating the concern that coarse age grouping might make the instruments contaminated with age-varying omitted factors that correlate with both SFU receipts and the dependent variable (Tables 6 and 9).

2. Given model nonlinearity, estimation is implemented by a control function approach and inference implemented with bootstrap. The control function approach used is also known as two-stage residual inclusion, analogous to the two-stage least square estimator for linear regression models. In the first stage, linear fixed-effect regressions are used to estimate the relationship between SFU receipts and the age-eligibility instruments. Residuals from the first stage capture the component of SFU receipts that are endogenous as this component is not explained by the exogenous instruments. In the second stage, the first-stage residuals are included as a control, while all else (including the endogenous variable, SFU receipts) is unchanged from the equation without instruments. $^{1}$ The second stage is estimated with the same estimator as the estimation without instruments. The control functions tend to be highly significant, pointing to endogeneity in SFU receipts that are unaddressed in the regression without instruments. Standard errors, p-values, and confidence intervals for the estimated coefficients are obtained by repeated estimation on village-clustered bootstrapped samples.

3. We confirm the causal effect of SFU receipts on spending patterns. Table 3 shows that the estimated semi-elasticity of spending on substances on SFU receipts remains highly significant in the control-function approach, and the magnitude increases. This might be counterintuitive given the expectation that omitted factors could lead to positive correlation between SFU receipts and substance spending that is not causal, as a result of which the estimation bias should be upward. In Kiribati, employment opportunities and supply of goods and services tend to concentrate in Tarawa, where the capital is located, and therefore a negative correlation between unemployment and substance spending could arise due to geographical factors.

4. The control function approach is also used to establish the causality of the spending decision impact of SFU receipts (extensive vs. intensive margin). Again, we implement a two-stage residual inclusion strategy in which SFU receipts are first predicted using the age-eligibility instruments, and the resulting first-stage residual is then included in the second-stage logit equation in addition to SFU receipts. By conditioning on this residual, the second stage nets out the endogenous component of SFU receipts that would otherwise be correlated with unobserved determinants of household spending, restoring the exogeneity needed for causal interpretation. Inference is conducted using village-clustered bootstrap standard errors to account for the non-random nature of the generated regressor, which is the control function. Both SFU receipts and its interaction with bottom quartile dummy have unchanged signs and remain significant (Tables 7-8).

5. The estimated effects of SFU receipts on spending level and spending decision regarding substances are robust against additional controls and functional forms. Additional controls such as value of household durables and number of rooms in the dwelling do not lead to measurable differences in the key estimates either in the PPML regression or the hurdle model. Different functional forms, such as a simple linear regression in terms of level and a probit model for the extensive margin, do not materially change the results. Neither does redefining the instruments as indicators for the exact number of age-eligible people.
