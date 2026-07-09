## BIS Working Papers No 1366
# Assessing the effects of recent provisioning rules on consumer credit allocation in Colombia

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).


# Assessing the Effects of Recent Provisioning Rules on Consumer Credit Allocation in Colombia\*

DIEGO CUESTA - MORA♦ FREDY GAMBOA-ESTRADA§ CAMILO SANCHEZ - QUINTO $^{L}$

## Abstract

Colombia's post-pandemic recovery in 2021–2022 was marked by rapid consumer credit growth, followed by deteriorating credit quality indicators amid tightening financial conditions. In January 2023, the Superintendence of Finance of Colombia (SFC) introduced higher provisioning requirements for long-term consumer loans to enhance financial resilience against credit risk materialization and to help moderate the rapid expansion of consumer credit observed prior to the reform. From the perspective of credit institutions (CIs), increased provisions imply higher expenses and potential profitability pressures, which could lead to adjustments in lending strategies. This study evaluates the effect of that regulatory policy on consumer credit dynamics and CI soundness. We find that the measure increased CIs' provision coverage ratio, indicating progress toward the policy's resilience objective, but it did not significantly affect overall credit supply conditions for longer-maturity loans in terms of loan amounts, interest rates, and collateral requirements. However, these average effects mask notable heterogeneity across institutions. Smaller lenders tightened credit supply for loans whose maturity exceeds 108 months by reducing loan amounts and lowering loan-to-value ratios, while larger lenders absorbed the higher provisioning costs without altering credit terms.

JEL Classification: E51, E60, G21, G28.

Keywords: Loan-loss provisions, credit supply, consumer loans, credit risk.

## 1. Introduction

The Colombian economy experienced a notable recovery during 2021 and 2022 following the severe contraction caused by the Covid-19 pandemic. This rebound was accompanied by real credit growth across all segments, with consumer credit expanding particularly rapidly. A breakdown of this segment shows that personal loans and credit card lending accounted for the largest share of this dynamism. At the same time, the stance of monetary policy led to a broad-based increase in lending rates across consumer credit products. Moreover, throughout 2022, newly disbursed loans were increasingly granted at maturities longer than five years, even though the overall stock of consumer credit continues to be dominated by loans with maturities shorter than five years (Cuesta-Mora et al., 2022).

From the second half of 2022 onward, however, the acceleration in consumer credit coincided with a deterioration in credit quality indicators, including rising short-term delinquency rates. Although loan-loss provisions continued to grow, their pace slowed relative to the previous year; nonetheless, the provision coverage ratio remained at historically high levels. These developments unfolded against a macroeconomic outlook characterized by rising inflation, tighter monetary conditions, slowing economic activity, and increasing unemployment. Given that 2023 was expected to bring a further deceleration of the economy, with interest rates remaining elevated and inflation above the Central Bank of Colombia's target, pressures on households' repayment capacity intensified, raising concerns about the sustainability of consumer credit growth and underscoring the importance of continued monitoring of these trends.

In response to these challenges, the Superintendence of Finance of Colombia (SFC)—the regulatory authority overseeing the financial system—issued External Circular 026 of 2022 on November 29, 2022. This regulation introduced new guidelines for credit institutions (CIs) on the provisioning of consumer loan risk, aiming to promote the healthy and sustainable growth of this portfolio while recognizing the potential deterioration in borrowers' repayment capacity amid economic slowdown and persistent inflation. Effective January 1, 2023, CIs were required to incorporate the risk associated with long-term leverage into the calculation of individual provisions for new consumer loans, excluding credit cards, revolving credit, and pensioner loans. Specifically, for new loans with maturities exceeding 72 months and 108 months, provisions had to be increased by 10% and 40%, respectively, relative to the amounts calculated under the existing expected loss model.

Regulatory changes of this type are commonly expected to influence credit supply conditions and the characteristics of newly originated loans. Existing literature on macroprudential and supervisory interventions in Colombia finds that tighter regulatory requirements—particularly those related to countercyclical provision schemes for commercial loans—can affect loan supply and its characteristics (López et al., 2014; Gómez et al., 2020; Morais et al., 2021; Cabrera et al., 2025). Nevertheless, empirical evidence on the effects of provisioning-based regulatory measures remains limited, especially in the context of emerging economies and consumer credit portfolios. Therefore, the introduction of maturity-specific provisioning requirements provides an opportunity to examine how higher regulatory costs associated with long-term lending affect consumer loan supply decisions and the allocation of credit across maturities.

The contribution of this paper is threefold. First, using granular supervisory data, it evaluates the effects of the 2022 macroprudential policy measure that updated the expected loss-based provisioning rules on supply conditions of new long-term loans, including loan amounts, interest rates, and collateral requirements. Second, it examines the heterogeneity of institutional responses by analyzing how lenders with different market positions adjusted to the higher provisioning requirements applied at the 72- and 108-month thresholds. Third, the analysis employs advanced matching methodologies that address issues such as imbalance, inefficiency, model dependence, and bias that typically arise in widely used causal inference techniques like propensity score matching, which have been prevalent in prior studies on Colombia (López et al., 2014). By doing so, we provide new insights into the interaction between regulatory measures, credit market behavior, and financial stability in emerging economies.

Our results indicate that the introduction of maturity-specific provisioning requirements did not lead to a contraction in the supply of long-term consumer credit. Contrary to concerns that higher provisioning costs would reduce loan amounts or tighten contract terms, we find no significant effects on loan volumes, interest rates, or collateral requirements for those loans in terms of loan-to-value ratios. Instead, the regulation increased coverage ratios, thereby strengthening the capacity of credit institutions to absorb potential losses. However, we also find that smaller institutions tightened credit standards for loans with maturities above 108 months—reducing both disbursed capital and loan-to-value (LTV) ratios. These asymmetric responses highlight the importance of financial institutions' market share in the consumer credit segment and their balance sheet strength in shaping the transmission of provisioning-based regulation. Taken together, the results suggest that macroprudential policies focused on broad, system-wide provisioning requirements may have more pronounced effects on credit supply conditions than maturity-specific provisioning schemes that target only a narrow segment of the loan portfolio. Additionally, because the policy measure studied in this paper coincided with a period of contractionary monetary policy, its effects on credit supply were marginal, and the policy rate likely had a stronger influence on the dynamics of consumer loans. Overall, these findings suggest that the reform improved the preparedness of CIs for potential defaults on longer-term loans, thereby supporting their overall resilience against credit risk materialization.

This article consists of five sections including this introduction. The second section describes the background on changes of the provisioning framework in Colombia and reviews prior literature. The third section describes the data and presents descriptive statistics. The fourth section presents the econometric approach and the main results. The last section summarizes the findings and discusses policy implications.

## 2. Contextual background and literature overview

## 2.1. Background on changes to the loan portfolio provisioning framework in Colombia

Since 2002, Colombia's prudential regulation evolved from a reactive, cyclical approach to a risk-sensitive, forward-looking framework that integrates countercyclical buffers and loan-loss provisions based on expected loss models. This transition reflects a broader trend toward prudential regulation aligned with global standards (e.g., Basel III, IFRS 9), aiming to enhance financial stability and reduce systemic risk.

Prior to 2002, loan-loss provisioning in Colombia was governed by accounting and supervisory rules that required CIs to increase provisions mainly in response to observed loan delinquency and did not account for macroeconomic conditions. As a result, during economic expansions CIs maintained low levels of provisions, whereas they were sharply increased during downturns, which destabilized earnings and weakened capital adequacy. In 2002, Colombia's financial regulation on loan-loss provisioning evolved to address systemic vulnerabilities caused by procyclicality. SFC introduced a comprehensive reform of the credit risk management framework in 2002, known as the Sistema de Administración de Riesgo de Crédito (SARC, External Circular 11). SARC established a structured approach to identifying, measuring, and monitoring credit risk at the institutional level, requiring credit institutions to develop internal processes, information systems, and governance arrangements to support risk management. Its implementation was carried out in phases, allowing institutions to progressively adapt their systems and reporting capabilities.

Within this broader risk management framework, the SFC later in 2007 introduced a countercyclical provisioning tool—drawing inspiration from Spain’s 2000 model. The objective was to maintain a stable ratio of provisions-to-loan portfolio throughout credit cycles, thereby reducing volatility and strengthening financial resilience. Under the mechanism, banks accumulated additional provisions during credit expansions and released them during downturns. These countercyclical provisions (CIC) were defined as the difference between current and long-term average provisions. By mitigating the procyclicality of profits and fostering stability in the entity’s credit growth, these measures enhanced resilience of the financial system—a desirable outcome for regulators—while reducing uncertainty regarding future dividends and profitability $^{1}$ , which is advantageous for shareholders.

To ensure practical implementation, SARC introduced a standardized provisioning methodology, known as the reference model for expected loss (Chapter 31 of the Circular Básica Contable y Financiera). $^{2}$ To establish individual provisions that reflect borrowers' credit risk, CIs distinguish across loan portfolio segments. For the housing and microcredit segments, CIs must provision at least 1% of the combined loan portfolio and then apply the deterministic model. In contrast, for commercial and consumer segments, CIs follow the individual provisioning model, which combines procyclical individual (CIP) and countercyclical individual (CIC) components. The CIP represents the portion of the provision that reflects the current credit risk of each borrower, whereas the CIC accounts for potential deterioration in asset quality under adverse economic conditions.

Within the individual provisioning model, CIs must distinguish two phases—accumulation and decumulation—which govern the evolution of CIC over the credit cycle. The calculation of provisions differs across these phases, and transitioning from accumulation to decumulation requires meeting specific conditions, such as a sustained increase in provisions and moderate growth in the consumer loan portfolio (Appendix A). Despite these phase-dependent rules, the input used to compute provisions remains unchanged: loan exposure, risk matrices, adjustment factors, and expected loss. Loan exposure is determined by the outstanding balance of the loan, while risk matrices and adjustment factors are predefined by regulation and vary across loan sub-segments, collateral types, and borrower risk ratings.

Expected loss is computed as shown in Equation 1, where the probability of default (PD) represents the likelihood that a borrower will default within the next 12 months. This parameter is critical because it captures the forward-looking credit risk of the portfolio. PD is estimated using transition matrices under both normal conditions and stress scenarios (Appendix B). The exposure at default (EAD) measures the total exposure at the time of default—including principal, accrued interest, and other receivables—and is essential because it determines the magnitude of potential losses if default occurs, directly linking credit risk to the size of the outstanding obligation. The loss given default (LGD) indicates the proportion of exposure that is not recoverable after default; LGD is assigned based on the number of days past due following classification in the default category (Appendix C).

$$
E x p e c t e d L o s s = P D * E A D * L G D\tag{1}
$$

Since 2007, the provisioning framework for consumer credit (i.e., the individual provision model) has undergone incremental adjustments aimed at strengthening its sensitivity to emerging risks. In 2012, the SFC introduced a temporary additional provision for consumer loans, activated when delinquency indicators deteriorated, thereby reinforcing buffers during periods of rising household credit risk. Subsequently, in 2016, the framework was refined to account explicitly for loan maturity, requiring expected losses on new consumer loans—excluding credit cards and revolving credit lines—to increase with the remaining repayment horizon. This change recognized that longer maturities expose lenders to greater uncertainty over the credit cycle and updated the expected loss formula to include a fourth term that is triggered when the remaining maturity of a loan exceeds 72 months.

In November 2022, the SFC released External Circular 026, which introduced new instructions for the establishment of provisions for risk on consumer loan portfolios. The new framework requires CIs to incorporate a factor that captures the additional risk associated with higher borrower leverage at longer maturities. For new loans—excluding credit cards, revolving credit lines and payroll loans to pensioners—granted since January 2023, an additional provisioning percentage of 10% applies when the loan maturity is greater than 72 months (6 years), and 40% when the maturity is greater than 108 months (9 years).

According to External Circular 026, these measures aim to promote the sound and sustainable growth of the consumer loan portfolio and to recognize the potential impact on borrowers' repayment capacity in the context of economic slowdown and persistent inflation. Following this update, expected losses for consumer loans should be calculated as shown in Equation 2 where the maturity adjustment (MA)—introduced in the 2016 regulatory update—accounts for loan term risk in expected loss calculations. The MA equals 1 for loans with a remaining maturity shorter than 72 months, and $MA = \frac{m}{72}$ otherwise, where $m$ denotes the remaining maturity in months. Additionally, CIs were also required to conduct a forward-looking analysis of potential deterioration in the consumer loan portfolio and, if necessary, establish an additional general provision no later than December 31, 2022.

$$
E x p e c t e d L o s s = P D * E A D * L G D * M A * K\tag{2}
$$

Longer maturities generally imply greater uncertainty and increased exposure to adverse conditions, making this adjustment essential for risk-sensitive provisioning. The $K$ factor captures additional risk associated with higher leverage at longer maturities, enhancing the model's sensitivity to structural vulnerabilities in consumer credit portfolios, particularly under scenarios of prolonged debt accumulation. The $K$ factor is calculated as follows:

$$
K = \left\{ \begin{array}{c c} 1 & i f m \leq 7 2 \\ 1. 1 i f 7 2 <   m \leq 1 0 8 \\ 1. 4 & i f m > 1 0 8 \end{array} \right\}\tag{3}
$$

By design, the introduction of the K factor increases the marginal cost of supplying long-maturity consumer credit, particularly for loans extending beyond six and nine years. This discrete and maturity-specific adjustment to expected loss calculations provides a natural setting to assess how higher regulatory provisioning requirements influence loan supply decisions and the allocation of credit across maturities in the consumer loan market.

## 2.2. Related literature

Since the global financial crisis of 2008, regulatory authorities in an increasing number of jurisdictions have required CIs to adopt an expected credit loss (ECL) provisioning framework. Under this approach, institutions must accumulate provisions from the time a loan is disbursed, rather than waiting for credit risk to materialize, as was the case under the incurred loss approach. This shift responds to concerns that delayed recognition of credit losses can exacerbate systemic vulnerabilities (Cohen and Edwards, 2017). Moreover, the ECL framework has been shown to mitigate the procyclical behavior of credit, which can amplify adverse shocks during economic downturns. A seminal paper by Jiménez et al. (2017) drew considerable attention from policymakers and scholars to the relationship between regulation and bank risk-taking. The authors examined the effects of countercyclical loan-loss provisions (CIC) in Spain on the credit cycle and found that countercyclical buffers provide additional protection during downturns. Their results show that increases in provisioning requirements contributed to smoothing credit-supply cycles.

López, Tenjo, and Zárate (2014) assessed the effectiveness of the countercyclical provisioning system (CIC tool) on credit dynamics in Colombia. Using Propensity Score Matching (PSM) models, their findings indicate that this type of macroprudential policy exerted a negative impact on credit growth across different percentiles. Cardozo, Murcia, and Vargas (2017) employed a panel data model and found that SARC strengthened bank solvency and liquidity by inducing a reduction in risk-weighted assets. Gómez et al. (2020) explored the impact of dynamic provisions on commercial credit in the run-up to the 2008 crisis. Applying a two-way fixed effects (TWFE) model restricted to firms with multiple banking relationships, they documented a negative effect of these provisions on credit growth, which varied according to specific characteristics of banks and borrowers. Morais et al. (2021) analyzed the impact of SARC on commercial credit using a bank-firm relationship panel. Their results suggest that banks tightened their credit allocation policies, affecting higher-risk debtor firms. Finally, Cabrera et al. (2025) examined the effects of the countercyclical provisioning scheme on the corporate credit portfolio over 2008–2018. They found that higher provisioning costs for downgraded loans reduced credit supply, increased collateral requirements, and tightened LGD coverage. Downgraded firms also faced investment constraints and contractions in liabilities, equity, and assets.

A large empirical literature examines how macroprudential policies affect credit dynamics. Saurina and Jiménez (2006) show that rapid credit growth increases loan losses and that countercyclical provisions enhance banking-system soundness. Drehmann and Gambacorta (2012) find that countercyclical capital buffers mitigate credit procyclicality and strengthen resilience. Tovar et al. (2012) document that reserve requirements in Latin America have modest, short-term effects on credit and complement monetary policy. Aikman et al. (2015) argue that macroprudential tools curb credit cycles through risk-cost and expectations channels. Using cross-country data, Akinci and Olmstead-Rumsey (2018) show that tighter macroprudential measures reduce credit growth, a result consistent with evidence for Latin America in Gambacorta and Murcia (2020), who also find stronger effects when paired with monetary policy. Andries et al. (2022) report that macroprudential policies reduce credit growth in the short run but support sustainable expansion in the long run. Ekinci and Özcan (2021) further show that these measures are more effective when reinforced by tighter regulatory frameworks.

Our study builds on Morais et al. (2020) and López, Tenjo, and Zárate (2014), who evaluate the effects of Colombia's provisioning framework on commercial credit. By contrast, we focus on the consumer loan segment, which is directly affected by the 2022 maturity-specific regulatory reform. In addition, we exploit supervisory data at a finer level of disaggregation, which enables us to examine how institutions adjust loan supply across the maturity distribution. Methodologically, while earlier work commonly relies on propensity score matching, we apply more advanced matching procedures that overcome limitations such as imbalance and model dependence.

## 3. Data and stylized facts

## 3.1. Data and sample description

This section describes the data used to assess the impact of the regulatory change detailed above. Our primary data source is Format 341 from the SFC, an administrative record that provides granular quarterly information on the universe of credit portfolios in Colombia, disaggregated at the debtor-institution level.

The dataset is structured along two dimensions. First, it includes debtor-level information such as legal status, identification, and main economic activity. Second, it incorporates detailed loan-level characteristics, including segment, sub-segment, loan amount (outstanding balance), interest rate, provisions, origination and maturity dates, collateral value and type, and days past due. In addition, the determinants of expected loss are reported: PD, LGD, and EAD. Technical details for all variables included in the sample are provided in Table D.1 of Appendix D.

Given that the 2022 regulatory reform applies only to recent originated consumer credit, the sample is restricted exclusively to new loans within the consumer loan portfolio. These are defined as obligations whose origination date coincides with the reporting month. Credit card operations are excluded, as this segment is not subject to the new provisioning requirements. Similarly, revolving credit is exempt from the regulation. However, because this segment cannot be explicitly isolated within the database, we exclude all loans classified as 'Other' that cannot be identified—based on their specific risk parameters—under the sub-modalities of payroll-deducted $^{3}$ , personal $^{4}$ , vehicle, or low-amount loans.

Format 341 exhibits a technical peculiarity whereby, if a borrower holds multiple obligations within the same segment, credit rating, collateral type, and financial institution, the system consolidates these operations into a single record. In such cases, the format presents aggregated values for loan amount and provisions, and weighted averages for interest rates; however, the origination and maturity dates, as well as the collateral value, correspond only to the largest loan. To avoid biases in estimating the effects on new credit supply arising from this aggregation procedure, the sample is restricted to unique records for each borrower-institution pair by segment, rating, and collateral. Specifically, only observations for which the number of underlying loans equals one are retained. $^{5}$

With the dataset constructed, an outlier-cleaning process was applied by trimming observations at the 1st and 99th percentiles for capital, interest rate, collateral value, and loan-to-value variables. Additionally, the regulation stipulates that within the payroll-deducted sub-segment, the reform does not apply to pensioners. Consequently, loans associated with these borrowers —identified through the debtor's economic sector variable—are excluded from the sample. $^{6}$ After implementing the full set of control variables and data-cleaning procedures, the final dataset for the 2022–2024 period comprises 8,120,390 newly originated loans.

Additional borrower-level variables were constructed to capture recent credit history. Specifically, dummy variables were defined to identify whether the borrower had maintained any commercial relationship with the financial system during the four quarters preceding the new loan's origination. Likewise, indicators were created to determine whether the borrower had experienced delinquency exceeding 30 days during that period, and whether the prior credit relationship was with the same institution granting the new loan. These variables help capture latent borrower risk characteristics and account for pre-existing banking relationships that may influence the supply conditions of new credit.

Finally, the database was merged with bank-level financial indicators to control for bank heterogeneity. This information, also sourced from the SFC, includes operational and size metrics such as total assets and a dummy identifying institutions with the largest market share in the consumer loan portfolio. Risk-management indicators were also incorporated, including portfolio quality by delinquency and risk.

Performance and solvency measures were added as well, such as Return on Assets (ROA), the Net Stable Funding Ratio (NSFR) as a measure of structural liquidity, and the capital adequacy ratio (CAR). Additionally, an indicator capturing whether an institution met the regulatory conditions to activate the countercyclical provision release phase was included (Appendix A).

## 3.2. Treatment identification and descriptive statistics

Utilizing the loan maturity variable and the filtering criteria outlined in the previous section, we distinguish between loans subject to the regulatory change (treatment) and those not affected (control). Given the regulation's tiered structure, we define two treatment groups corresponding to the 72- and 108-month thresholds. Both groups are compared against a common control group—consisting of loans with maturities of 72 months or less, as formalized in Equations (4) and (5).

$$
T r e a t m e n t _ {7 2 i} = \left\{ \begin{array}{l l} 1, & \text {if 72 months <   term of loan i\leq 108 months} \\ & 0, \text {if term of loan i\leq 72 months} \end{array} \right.\tag{4}
$$

$$
T r e a t m e n t _ {1 0 8 i} = \left\{ \begin{array}{l l} 1, & \text {if term of loan i > 108 months} \\ 0, & \text {if term of loan i \leq 72 months} \end{array} \right.\tag{5}
$$

Since the dataset consists of new loans issued each quarter, the data are structured as a pooled cross-section. We do not track individual loans over time to construct a panel, as our focus is not on the evolution of credit performance but on the conditions granted at the moment of origination. Accordingly, the composition of the treatment and control groups varies across periods, with loans classified solely based on their initial maturity term.

As is standard in impact evaluations, the validity of our analysis relies on the comparability between the treatment tiers and the control group, ensuring that observed differences can be properly identified as average treatment effects. This requirement poses a challenge in our setting, as loans naturally exhibit different characteristics depending on their maturity. As shown in Chart 1, longer-term loans tend to have higher average loan amounts, while Chart 2 indicates that average interest rates are typically higher for shorter-term loans. Recognizing these structural differences is essential: failing to account for such intrinsic characteristics could lead to spurious findings, for example, incorrectly attributing higher loan amounts or lower interest rates to the regulatory change. Additionally, although the regulation could incentivize credit institutions to shift their loans to shorter maturities, we did not observe any change in the loan distribution by maturity before and after its adoption.

When evaluating balance between the control and treatment samples, substantial disparities emerge across other observable variables, as measured by the Standardized Mean Difference (SMD). This metric, widely used to assess covariate balance, computes the difference in means relative to the pooled standard deviation. Unlike traditional t-tests, the SMD is independent of sample size and therefore avoids detecting statistically significant differences merely due to very large samples. Conventionally, an SMD value above 0.1 signals meaningful imbalances between groups.

Chart 1. Average Loan Amount by Maturity Term

[[KC_IMAGE_001]]

Source: Financial Superintendence of Colombia (SFC). Authors' calculations.

Chart 2. Average Interest Rates by Maturity Term

[[KC_IMAGE_002]]

Source: Financial Superintendence of Colombia (SFC). Authors' calculations.

Comparison between the control group and the 72-month treatment group (Treatment 72) shows considerable differences across nearly all loan-level variables, except for the credit rating, interest rate, and the coverage indicator (Table 1). Detailed descriptive statistics, including means and standard deviations for continuous variables and distributions for categorical variables are provided in Table E.1. For example, collateral values are higher in the treatment group, consistent with the lower prevalence of unsecured loans in that segment. Differences are also apparent in loan sub-modalities: the control group is heavily concentrated on personal loans, whereas the treatment group exhibits a higher share of vehicle and payroll deducted loans. At the debtor level, imbalances arise primarily across economic sectors. By contrast, the dummy variables capturing borrowers' historical relationship with the financial system appear more balanced. There is also notable heterogeneity in the distribution of financial institutions originating new loans, indicating that some lenders are more exposed to specific maturity terms.

Table 1. Covariate Balance Assessment using Standardized Mean Differences (SMD)


Source: Financial Superintendence of Colombia (SFC). Authors' calculations. Notes: \* SMD > 0.1, indicating an unbalanced covariate. For the purpose of this table, when the LTV is undefined due to a zero-collateral value, it is recorded as zero.

For the 108-month treatment group (Treatment 108), deviations from the control group are even more pronounced. All loan-level variables are unbalanced according to the SMD. Differences in average principal amounts are particularly pronounced, accompanied by lower interest rates and higher coverage levels. Regarding credit ratings, although both groups are concentrated in Category A, the treatment group exhibits a higher share of lower-quality ratings. Sub-modality patterns also differ: the treatment group contains a larger proportion of payroll-deducted loans, whereas the control group is more heavily represented in the personal-loan sub-segment. As in the 72-month tier, debtor-level differences for Treatment 108 are mainly associated with economic sector composition. Moreover, longer-term loans do not appear to be mainly driven by borrowers with prior credit relationships with the same bank. Finally, as in the 72-month tier, the concentration of originating financial institutions differs markedly between the treatment and control groups.

## 4. Econometric approach and results

## 4.1. Exact matching

Given the structural imbalances observed between the control and treatment groups, it is essential to adopt an identification strategy that ensures comparability across observable variables, thereby allowing us to isolate the policy's effect on new consumer loans. To address this issue and mitigate selection bias, we employ Exact Matching (EM) as the first step in our econometric approach.

Unlike other matching techniques —such as Propensity Score Matching—EM relies on a strict criterion: each treated unit is matched to all control units that share the same values for all covariates. This procedure partitions the data into subclasses defined by unique combinations of observable characteristics. Within each subclass, treatment and control units are identical with respect to these variables, ensuring that any remaining difference is driven solely by loan maturity, which determines treatment assignment. Observations that do not find an exact match are discarded, guaranteeing perfect covariate balance within the analyzed subsample.

We implement multiple specifications of the exact matching algorithm, varying the set of covariates according to the outcome variable of interest, as detailed in Table 2. This framework is applied consistently to both treatment comparisons: the control group versus Treatment 72 and the control group versus Treatment 108. The first specification (EM1) is used across all primary outcomes —interest rate, loan amount, coverage ratio, and LTV. For the LTV analysis, the sample is restricted to loans with non-zero collateral values, as the ratio is otherwise undefined. To ensure that loans are compared under identical macroeconomic and financial conditions, EM1 includes the reporting quarter as a mandatory matching covariate. Matches are further restricted to within the same financial institution, thereby controlling for unobserved supply-side heterogeneity, such as differences in risk appetite and credit-scoring models across lenders. To account for segment-specific lending policies, we require exact matches on the loan sub-segment. We also control for risk profiles by matching on collateral type, credit rating, PD, and LGD, ensuring that comparisons are restricted to loans with equivalent risk characteristics. Finally, at the borrower level, we match on debtor type and economic sector, thereby holding constant the borrower's economic activity across treatment and control groups.

The second specification (EM2) builds on the baseline by incorporating additional loan conditions to further refine the counterfactuals. Specifically, we include discretized values of collateral, loan amount, and interest rate, which are added to the covariate set depending on the dependent variable under analysis. Because these are continuous variables, we discretized them into percentiles to ensure comparability: loan amount and interest rate are divided into 100 percentiles while collateral is divided into 20 percentiles. $^{7}$ This partitioning enables the matching algorithm to account for more granular loan characteristics.

The specifications impose specific restrictions depending on the dependent variable under analysis to avoid over-matching. For the interest rate analysis, we include loan amount and collateral value in the covariate set to ensure that loans of comparable size and collateralization are matched. Crucially, the interest rate itself is excluded from the matching process; otherwise, treatment and control groups would be artificially balanced on the outcome variable, making the treatment effect unidentifiable. For the analysis of loan amount and coverage ratio, we instead match on the interest rate and collateral value. The same restriction applies to the coverage ratio because this indicator is a function of the loan principal (provisions divided by capital); therefore, including loan amount in the matching set would induce mechanical bias. Finally, for the LTV analysis, matches are selected solely on the interest rate (in addition to the EM1 baseline covariates), explicitly excluding both loan amount and collateral value since these variables directly compose the LTV ratio.

Table 2. Matching Specifications by Variable of Interest


Source: Financial Superintendence of Colombia (SFC). Authors' calculations. Note: An "X" denotes the covariates included in each specification.

Finally, the third specification (EM3) incorporates covariates related to the borrower's recent credit history across all outcome variables. This ensures that loans are matched between borrowers with similar profiles in terms of access to the financial system and delinquency behavior — factors that financial institutions routinely use when determining credit supply conditions. Consequently, EM3 represents the most comprehensive specification, imposing stricter matching criteria than EM1 and EM2. This additional rigor naturally results in a smaller number of matched observations, as shown in Table 2, a pattern that holds for both the 72-month and 108-month treatment comparisons. Employing these three alternative matching specifications enable us to assess the robustness of our findings.

The matching process serves a dual purpose: it isolates the subset of matched treatment and control observations that form our final analytical sample and generates the specific weights required to balance both groups across observable characteristics. These weights play a central role for the second stage of our econometric approach.

## 4.2. Difference-in-differences

Once the matched datasets are established, the next step is to identify the causal effect of the regulatory change on credit conditions. To this end, we employ a Difference-in-Differences (DiD) framework. This approach leverages the fact that we observe loans in both the control and treatment groups before the regulatory change (up to December 2022) and after its implementation. We therefore estimate the baseline specification (6) separately for the 72-month and 108-month thresholds. In each case, we use the corresponding matched subsample derived from the exact matching procedure described in the previous section, along with the appropriate treatment indicator $Treatment_{72i}$ or $Treatment_{108i}$ . The model is estimated using Weighted Least Squares (WLS), incorporating the matching weights to preserve covariate balance.

This specification includes a robust set of controls to ensure proper identification of the treatment effect. Time fixed effects are included to absorb aggregate shocks affecting all loans in each quarter, while financial-institution fixed effects account for time-invariant characteristics such as business models or risk management practices. In addition, we incorporate time-varying bank-level controls to capture institutions' most recent financial performance. Importantly, although matching enhances comparability between treatment and control groups, it does not guarantee that the outcome variables share the same baseline levels on average. Therefore, the treatment indicator must be explicitly included in the estimation.

$$
Y _ {i f t} = \alpha + \mu T r e a t m e n t _ {i} + \beta (T r e a t m e n t _ {i} * P o s t _ {t}) + \sigma_ {t} + \delta_ {f} + \Gamma X _ {f t} + e _ {i f t}\tag{6}
$$

## where:

■ $Y_{ift}$ : outcome variable for loan i of financial institution f in quarter t.

\- $Treatment_{i}$ : binary indicator representing the treatment group specific to the analysis $Treatment_{72i}$ or $Treatment_{108i}$ .

\- $Post_{t}$ : dummy variable equal to 1 for quarters following the regulatory change (post-2022), and 0 otherwise.

■ $\mu$ : captures the time-invariant baseline difference between the treatment and control groups.

■ $\beta$ : identifies the Average Treatment Effect (ATE) of the regulation.

■ $\sigma_{t}$ : time fixed effects.

■ $\delta_{f}$ : financial institution fixed effects.

\- $X_{ft}$ : vector of time-varying bank-level controls, including the countercyclical phase, size (log assets), non-performing loan (NPL) ratio, quality risk indicator (QRI), return on assets (ROA), Capital Adequacy Ratio (CAR), and the Net Stable Funding Ratio (NSFR).

■ Γ : vector of coefficients associated with the bank-level controls.

■ $e_{ift}$ : idiosyncratic error term.

The first step in our analysis is to assess whether the incorporation of parameter K into the expected loss calculation effectively impacted the Provision Coverage Ratio, thereby enhancing financial institutions' preparedness for potential credit risk materialization. As shown in Table 3, the regulation produced the expected positive effect on newly originated long-term credit. At the 72-month threshold, the regulatory change resulted in an average increase of 0.166 percentage points in the coverage ratio (Column 3) under the strictest exact matching specification (EM3), a result that is statistically significant at the $95\%$ confidence level. Importantly, the coefficients remain positive and statistically significant across all alternative matching specifications, confirming the robustness of this finding.

At the 108-month threshold, the impact is considerable stronger, with an average increase of 0.86 percentage points (Column 6), again consistently observed across all matching specifications. The larger magnitude of the effect at the 108-month threshold relative to the 72-month threshold aligns with the regulatory design: expected losses increased by 40% for loans exceeding 108 months, compared with 10% for those exceeding 72 months. Overall, these results indicate that the regulation successfully strengthened the resilience against credit risk materialization of financial institutions by bolstering their buffers against potential loan defaults.


Table 3. Effects on Provision Coverage Ratio
Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

Having confirmed that the regulation achieved its intended effect, we now turn the core of the analysis: evaluating its impact on credit conditions, specifically regarding interest rates, loan amounts, and LTV ratios.

As discussed in the introduction, higher provision requirements for long-term loans impose additional cost pressures on financial institutions. Lenders may respond by tightening the terms of new originations—either by passing on higher costs through increased interest rates, reducing exposure via smaller loan amounts, or requiring greater collateral coverage, which would exert downward pressure on LTV ratios.

Regarding interest rates, the analysis yields several noteworthy results (Table 4). Across all three matching specifications, the estimated treatment effect at the 72-month threshold is negative—a finding that contradicts our initial expectation. Although the coefficient in the second specification (EM2) is statistically significant at the 95% confidence level, this significance disappears under the strictest specification (EM3, Column 3). Accordingly, we conclude that, on average, the treatment effect on interest rates at this threshold is not statistically distinguishable from zero.

Crucially, across all three specifications, the structural baseline difference between groups—captured by the coefficient $\mu$ on the treatment indicator—consistently shows that interest rates in the treatment group are inherently higher than those in the control group. This result is particularly noteworthy because, in the raw unmatched dataset, the opposite pattern appeared: longer-term loans generally exhibited lower interest rates. The reversal underscores the value of the matching procedure: by ensuring comparability between groups, the analysis reveals that, for new consumer loans with similar borrower and risk profiles, interest rates are structurally higher for longer maturities.

At the 108-month threshold, the estimated treatment effect becomes positive; however, it remains statistically insignificant across all three matching specifications. Conversely, the structural baseline difference turns negative—consistent with patterns observed in the unmatched sample, where lower rates were more pronounced for loans exceeding 108 months—although this baseline estimate is itself not statistically significant.

Taken together, these results suggest that the regulatory change did not impact credit interest rates, indicating that financial institutions did not adjust pricing to offset the higher provision costs. These findings remain robust under an alternative specification that replaces time fixed effects with the average monetary policy rate, thereby explicitly controlling for the monetary policy stance $^{8}$ (Appendix F).

Table 4. Effects on Interest Rates


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

Turning to the analysis of loan amounts, the results for the 72-month threshold show no statistically significant treatment effect under the stricter specifications (EM2 and EM3), as shown in Table 5. Interestingly, the least restrictive specification (EM1) yields a positive and statistically significant coefficient—a finding contrary to theoretical expectations. This discrepancy highlights the importance of the stricter matching criteria used in EM2 and EM3, which control for interest rates and collateral to mitigate omitted-variable bias and improve estimation precision. Regarding the structural baseline difference, the estimate is positive and significant across all specifications, indicating that, on average, new loans in the treatment group are larger than those in the control group.

Table 5. Effects on Loan Amount (Log)


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

A similar pattern emerges at the 108-month threshold. The structural baseline difference remains positive and significant, with a larger magnitude than at 72 months. For the treatment effect, the point estimates across all three specifications are negative—consistent with the intuitive expectation of a contraction in credit supply—but none are statistically distinguishable from zero. Thus, we find no evidence that the regulatory change affected credit conditions through its impact on the amount of loans disbursed at either threshold.

Finally, focusing on the Loan-to-Value (LTV) analysis—restricted to new loans with non-zero collateral—we find no statistically significant treatment effect at the 72-month threshold (Table 6). Although the point estimates across all three matching specifications are negative, consistent with the theoretical expectation of tighter collateral requirements, none of them achieve statistical significance. By contrast, the structural baseline difference is positive and statistically significant, indicating that, on average, treated loans exhibit higher LTV ratios. This result aligns with the descriptive statistics, which show that longer-term loans typically involve larger disbursement amounts relative to the collateral pledged. Under the strictest specification (Column 3), the treatment group displays an average LTV that is 13.4 percentage points higher than that of the control group.

Results for the 108-month threshold follow a similar pattern. The structural baseline difference is even more pronounced: the treatment group exhibits an LTV premium of 28.7 percentage points over the control group in column 3. Regarding the treatment effect, the coefficients under the strictest matching specifications remain negative but statistically indistinguishable from zero. Thus, we find no evidence that the regulatory change significantly altered LTV at both thresholds.

Overall, the results evidence that institutions did not pass the higher provisioning costs onto borrowers, However, the results also show that provisioning policies targeted at specific maturity terms have more limited effects on moderating credit supply or reducing risk exposure through tighter lending conditions than broader countercyclical provisioning adjustments.

Table 6. Effects on Loan to Value (LTV)


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

The final step in validating our findings on loan amounts, interest rates, and LTV ratios is to assess the plausibility of the parallel trends assumption, the key identifying condition underlying the Difference-in-Differences identification strategy. To this end, Appendix G presents result for each outcome variable and maturity threshold, estimated using the dynamic Equation (7) applied to the strictest matched sample (EM3).

$$
\begin{array}{r l} & Y _ {i f t} = \alpha + \mu T r e a t m e n t _ {i} + \sum_ {j = - 3} ^ {- 1} \beta_ {j} \mathrm{Treatment} _ {i} * I [ j = t - t _ {0} ] + \\ & \sum_ {j = 1} ^ {8} \beta_ {j} \mathrm{Treatment} _ {i} * I [ j = t - t _ {0} ] + \sigma_ {t} + \delta_ {f} + \Gamma X _ {f t} + e _ {i f t} \end{array}\tag{7}
$$

where:

\- $t_0$ : indicates the quarter immediately preceding the introduction of changes in the calculation of provisions—that is, the fourth quarter of 2022.

■ $I[*]$ : indicator variable that equals 1 if condition $[*]$ holds.

\- $\beta_{j}$ : denotes the dynamic difference between treatment and control groups $j$ quarters relative to the regulation implementation date $t_0$ . For $\mathbf{j} < 0$ these estimates test the parallel trends assumption (i.e., whether outcomes differed significantly prior to the regulation). For $j > 0$ they quantify the dynamic treatment effect and its persistence over time.

As shown in Appendix G, the coefficients associated with the periods preceding the regulation's implementation are statistically indistinguishable from zero across all outcome variables. The absence of pre-existing differential trends supports the plausibility of the parallel trends assumption, thereby reinforcing the internal validity of the main results reported under Specification 3. Furthermore, consistent with our earlier findings, the post-treatment coefficients also lack statistical significance in every specification, confirming that the regulatory change did not induce a dynamic adjustment in credit conditions over the observed horizon.

However, while these aggregate results suggest no average impact on credit conditions, potential heterogeneity driven by the market share of financial institutions may still exist. Larger institutions, which typically hold a significant share of the consumer credit market, may have the financial capacity to absorb the increased provisioning costs without harming their operating results. As a result, these institutions may be less likely to pass these costs on to borrowers. Conversely, smaller institutions with a lower market share in the consumer credit segment, yet exposed to the same portfolio risks, may face tighter margin pressures. This could prompt them to adopt stricter standards for new loan originations to maintain profitability.

To examine this hypothesis, we estimate an augmented version of the baseline model that includes an interaction term for Market Concentration $MC_{f}$ . This binary variable takes the value of 1 if the financial institution holds more than 10 percent of the total consumer credit portfolio in the given quarter, and 0 otherwise. Among the 31 institutions in our sample, three consistently meet this criterion across all quarters. $^{9}$

Consequently, we estimate Equation (8). Relative to Equation (6), this model adds the interaction between the treatment group and financial institutions' market share in the consumer credit segment to account for baseline-level differences in treated loans that are specific to large institutions. Crucially, it also includes the triple interaction between the treatment indicator, the post-regulation period, and the market share variable. Note that the standalone $MC_{f}$ term is omitted from the equation because it is perfectly collinear with the financial institution fixed effects.

$$
\begin{array}{r} Y _ {i f t} = \alpha + \mu T r e a t m e n t _ {i} + \gamma (T r e a t m e n t _ {i} * M C _ {f}) + \beta (T r e a t m e n t _ {i} * P o s t _ {t}) + \\ \theta (T r e a t m e n t _ {i} * P o s t _ {t} * M C _ {f}) + \sigma_ {t} + \delta_ {f} + \Gamma X _ {f t} + e _ {i f t} \end{array}\tag{8}
$$

where:

\- $MC_{f}$ : a dummy variable equal to 1 for financial institutions whose share of the total consumer loan portfolio exceeds $10\%$ , and 0 otherwise.

\- $\gamma$ : captures the differential baseline gap between treatment and control loans specific to large institutions.

\- $\beta$ : identifies the Average Treatment Effect (ATE) of the regulation for smaller financial institutions (i.e., when $MC_{f} = 0$ ).

\- $\theta$ : captures the differential (marginal) effect of the regulation on large financial institutions relative to smaller ones.

\- $\beta + \theta$ : represents the total effect of the regulation for institutions with high market share (i.e., when $MC_{f} = 1$ ).

Turning to the heterogeneity analysis for interest rates, Table 7 shows that at the 72-month threshold—mirroring the aggregate findings—the treatment effect for smaller institutions is negative but statistically indistinguishable from zero at the 95% confidence level across the two strictest matching specifications. Regarding the triple interaction term, the coefficient is also negative and statistically insignificant, indicating no relative differential effect between large and small institutions. To assess the total effect for large entities, we test the linear hypothesis $H_{0}:\beta+\theta=0$ . Panel C reports the associated p-values, which indicate that the total effect is not statistically significant in any specification.

Analogous results are observed at the 108-month threshold. Consistent with the aggregate analysis, the coefficient for smaller institutions is positive but remains statistically indistinguishable from zero under all three matching specifications. Similarly, for large institutions, neither the marginal effect in the triple interaction nor the total aggregated effect is statistically significant. Overall, these findings corroborate the aggregate results: even when accounting for heterogeneity in the share of the consumer credit market, there is no evidence of an impact on interest rates for newly originated consumer loans.

Table 7. Effects on Interest Rates by Market Share


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

Regarding loan amounts (Table 8), at the 72-month threshold, the two strictest matching specifications indicate that the effect for smaller institutions is negative but statistically indistinguishable from zero, while the marginal effect for large institutions is positive. This suggests that the aggregate analysis, which reported a positive but insignificant coefficient, was largely driven by the differential behavior of large institutions. However, the hypothesis test for the total effect on large entities confirms that the impact is not statistically significant in any specification.

Striking results emerge at the 108-month threshold. For smaller entities, the treatment effect is negative and statistically significant. Specifically, the coefficient of -0.234 implies that smaller institutions reduced new-loan disbursements by approximately 20.9% $^{10}$ , consistent with the hypothesis that these lenders restricted credit supply by lowering loan sizes to manage the higher provisioning costs.

It is noteworthy that the marginal effect for large institutions is positive and significant. This helps explain why the aggregate result in Table 5 was insignificant: the contraction in loans among smaller banks was effectively offset by the opposite behavior of larger banks. However, when testing the linear hypothesis for the total effect on large institutions, the results remain statistically indistinguishable from zero under all matching specifications.

Table 8. Effects on Loan Amount (Log) by Market Share


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

In conclusion, while the aggregate estimates suggested no overall impact, the heterogeneity analysis reveals a clear asymmetry. Institutions with less market share in the consumer credit segment significantly reduced the amount of capital disbursed, indicating that credit tightening occurred exclusively among smaller lenders.

Finally, we extend this heterogeneity analysis to the Loan-to-Value (LTV) ratios presented in Table 9. At the 72-month threshold, mirroring the aggregate results, we find no statistically significant treatment effect for either small or large institutions.

However, a distinct asymmetry emerges at the 108-month threshold. Under the two strictest matching specifications, the treatment effect for smaller institutions is negative and statistically significant. Specifically, the estimates indicate a regulatory-induced reduction in LTV of 8.8 percentage points. Conversely, for large institutions, neither the marginal differential effect nor the total aggregate effect tested through the linear hypothesis is statistically significant. Thus, consistent with the findings on loan amounts, smaller entities responded to the regulation by tightening credit conditions for longer-term loans, specifically through lower LTV ratios.

Table 9. Effects on Loan to Value by Market Share


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors in parentheses, clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

## 5. Conclusions

This paper examines the effects of the introduction in 2022 of the maturity-specific provisioning rules on the allocation of newly originated consumer credit in Colombia. Using supervisory-level information from the SFC and a combination of Exact Matching and Difference-in-Differences estimators, we assess how higher expected-loss requirements for long-maturity loans affect provisioning behavior, credit supply conditions, and institutional heterogeneity across lenders. By focusing on new loan originations and controlling for borrower risk, loan characteristics, and financial institution conditions, our analysis isolates the direct impact of the new provisioning factors introduced in January 2023.

Three empirical findings stand out. First, the regulation reinforced the forward-looking buffers of financial institutions against potential losses. Second, despite the mechanical increase in provisions, the regulation did not materially affect supply conditions in terms of interest rates, loan amounts, and collateral requirements. Across all matching specifications, estimated effects are small and statistically insignificant.

These results indicate that provision changes targeted at specific maturity buckets have far more limited effects than broader, system-wide changes in provisioning rules, and that higher provisioning costs for long-term consumer credit were not transmitted to borrowers through pricing, loan size contraction, or stricter collateral requirements. While this is a positive consumer-protection outcome, it also means that the reform did not meaningfully moderate credit growth, an objective typically associated with macroprudential interventions. Third, the results also reveal meaningful heterogeneity across financial institutions. While average effects are negligible, smaller institutions—those with lower market share in the consumer credit segment and narrower margins—exhibited significant adjustments. For loans exceeding 108 months, smaller lenders reduced loan amounts and lowered LTV ratios, indicating a targeted tightening of credit supply for riskier maturity segments. In contrast, large institutions, which hold greater buffers and can absorb higher provisioning costs, exhibited no significant adjustment in pricing or lending terms. This asymmetry underscores the importance of financial institutions' market share in the consumer credit segment and balance-sheet strength in shaping institutional responses to regulatory changes.

From a policy perspective, these findings have two important implications. First, if the objective is to enhance resilience against credit risk materialization in segments of the consumer loan portfolio more exposed to long-term risk, targeted provisions—such as those introduced in November 2022—are effective and do not disrupt market functioning. Second, if the policy goal is to moderate aggregate credit growth, maturity-specific provisioning rules are unlikely to deliver meaningful effects. Instead, system-wide adjustments to expected-loss models or countercyclical buffers appear more effective, particularly when combined with complementary tools such as monetary policy.

A natural avenue for future research is to further exploit institutional heterogeneity by examining how provisioning-rule adjustments affect profitability and risk-taking across banks of different sizes and business models. Linking maturity-specific provisioning shocks to institution-level earnings dynamics, risk appetite, and balance-sheet strategies would provide a deeper understanding of how prudential tools operate across diverse financial intermediaries in emerging economies.

## REFERENCES


Akinci, O., & Olmstead-Rumsey, J. (2018). How effective are macroprudential policies? An empirical investigation. Journal of Financial Intermediation, 33, 33-57.

Andries, A. M., Melnic, F., & Sprincean, N. (2022). The effects of macroprudential policies on credit growth. The European Journal of Finance, 28(10), 964-996.

Cabrera, W., Gamba, S., Gómez, C., & Villamizar-Villegas, M. (2025). Examining Macroprudential Policy Through a Microprudential Lens: W. Cabrera et al. IMF Economic Review, 1-28.

Cardozo, P. A., Murcia, A. & Vargas, H. (2017). The macroprudential policy framework in Colombia. BIS Paper, (94i).

Cohen, B. H., & Edwards, G. (2017). The new era of expected credit loss provisioning. BIS Quarterly Review, March.

Cuesta-Mora, D. F., Clavijo-Ramírez, F., Chipatecua-Peralta, O., Gómez-Molina, A. C., Quicazán-Moreno, C. A., Baiter-Barreto, M. A., & Sarmiento-Paipilla, N. M. (2022). Informe especial de estabilidad financiera: riesgo de crédito-Segundo Semestre de 2022.

Drehmann, M., & Gambacorta, L. (2012). The effects of countercyclical capital buffers on bank lending. Applied economics letters, 19(7), 603-608.

Ekinci, M. F., & Özcan, G. (2021). Effectiveness of Macroprudential Policies: Panel Data Evidence on the Role of Institutions, Financial Structure, and Banking Regulations. In Economic Growth and Financial Development: Effects of Capital Flight in Emerging Economies (pp. 103-114). Cham: Springer International Publishing.

Gambacorta, L., & Murcia, A. (2020). The impact of macroprudential policies in Latin America: An empirical analysis using credit registry data. Journal of Financial Intermediation, 42, 100828.

Gómez, E., A. Murcia, A. Lizarazo, and J. C. Mendoza (2020): “Evaluating the impact of macroprudential policies on credit growth in Colombia,” Journal of Financial Intermediation, 42, 100843, macro prudential policies in the Americas.


López, M., F. Tenjo, and H. Zárate (2014): “Credit cycles, credit risk and countercyclical loan provisions,” Ensayos sobre Política Económica, 32, 9–17

Morais, B., G. Ormazabal, J.-L. Peydró, M. Roa, and M. Sarmiento (2021): “Forward Looking Loan Provisions: Credit Supply and Risk-Taking,” Borradores de Economia 1159, Banco de la Republica de Colombia.

Saurina, J., and G. Jiménez (2006): “Credit cycles, credit risk, and prudential regulation,” MPRA Paper 718, University Library of Munich, Germany.

Tovar Mora, C. E., Garcia-Escribano, M., & Vera Martin, M. (2012). Credit growth and the effectiveness of reserve requirements and other macroprudential instruments in Latin America.

## Appendix A: Criteria for the decumulation of countercyclical provisions (CIC)

According to Annex 1 of Chapter XXXI of the Circular Básica Contable y Financiera (CBCF), credit institutions intending to decumulate countercyclical provisions (CIC) must meet the following criteria:

1. Growth of individual provisions on riskier loans. This indicator measures the real quarterly growth of individual provisions associated with loans classified in categories B, C, D, and E (i.e., loans already exhibiting elevated risk). The regulatory threshold requires the real quarterly growth to be greater than or equal to 9%.

2. Provisioning burden relative to interest income. This criterion compares net provisions (after recoveries) recorded in the income statement to interest income from loans and leasing, accumulated over the quarter. The regulatory threshold requires net provisions to be greater than or equal to 17% of accumulated interest income.

3. Provisioning burden relative to adjusted financial margin. This indicator compares net provisions with the adjusted gross financial margin, defined as operating margin plus net credit provisions. The regulatory threshold requires net provisions to be less than or equal to 0%, or greater than or equal to 42% of the adjusted margin.

4. Credit growth. This criterion measures the real annual growth rate of the gross loan portfolio. The regulatory threshold requires the real annual growth rate to be less than 23%.

These criteria neither determine expected losses nor alter the value of individual provisions. Instead, they govern the phase of the countercyclical mechanism, dictating whether institutions continue accumulating CIC or are allowed to release it. External Circular 017 of 2023 formalized the rule that CIs must meet at least three of the four criteria for three consecutive months in order to enter the decumulation phase.

## Appendix B: The Probability of Default

The Probability of Default (PD) represents the likelihood that a borrower will enter default within a 12-month horizon. Under the SFC's reference model, PD is assigned based on borrower risk classification and loan segment and reflects the expected transition of loans into default status over the next year. PD values are obtained from regulatory transition matrices (Chapter 31 of Circular Basica Contable y Financiera).

There are two transition matrices mapping the probability that a loan migrates from its current risk category to default: one corresponding to normal economic conditions and another reflecting adverse or stress conditions. These matrices allow the provisioning framework to capture both baseline credit risk and the potential deterioration of borrower performance during unfavorable macroeconomic environments. As a result, PD is a forward-looking measure that varies systematically across loan sub-segments, borrower ratings, and economic conditions, and constitutes a central input in the calculation of expected losses for consumer credit.

Cumulative phase Matrix


Decumulation phase Matrix


Source: Financial Superintendence of Colombia (SFC).

## Appendix C: Loss Given Default

Loss Given Default (LGD) represents the proportion of the exposure that is not expected to be recovered once a borrower has defaulted. In the SFC's reference model, LGD is assigned according to the borrower's delinquency status and the characteristics of the loan following classification into default. LGD values depend on factors such as the number of days past due, recovery prospects, and the presence and quality of collateral. By incorporating LGD, the regulatory framework accounts for differences in recovery rates across consumer loans and ensures that provisioning reflects not only the probability of default but also the severity of losses when default occurs.


Source: Financial Superintendence of Colombia (SFC).

Table D.1. Variable Definitions


Source: Financial Superintendence of Colombia (SFC).

Table E.1. Covariate Balance Assessment using Standardized Mean Differences (SMD)


Source: Financial Superintendence of Colombia (SFC). Authors' calculations. Note: For categorical variables, values represent the number of observations (percentage of the subsample in parentheses). For continuous variables, values represent the mean (standard deviation in parentheses). An asterisk (\*) denotes a Standardized Mean Difference (SMD) > 0.1, indicating a substantial imbalance.

Table F.1. Effects on Interest Rates


Notes: \*\*\*, \*\*, \* denote whether coefficients are statistically significant at the 1%, 5%, and 10% levels, respectively. Standard errors clustered by entity. An “X” denotes the matched sample used for the estimation (Panel B). “FI” indicates Financial Institution. Source: Financial Superintendence of Colombia (SFC). Authors’ calculations.

Chart G.1. Results on Interest Rate

[[KC_IMAGE_003]]


[[KC_IMAGE_004]]


Chart G.2. Results on Loan Amount (log)

[[KC_IMAGE_005]]


[[KC_IMAGE_006]]


Chart G.3. Results on the Loan-to-Value (LTV) ratio

[[KC_IMAGE_007]]


[[KC_IMAGE_008]]

Source: Financial Superintendence of Colombia (SFC). Authors' calculations. Notes: the figure plots the coefficients estimated from Equation (4) along with their 95% confidence intervals, computed using standard errors clustered at the entity level. The vertical red line denotes the reference period of the analysis.
