# Creditors' Seniority and Sovereign Risk: Evidence from Debt Composition

IMF Working Papers describe policy-related analysis and research being developed by IMF staff members and are published to elicit comments and to encourage debate. The views expressed in Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL


# IMF Working Paper Finance Department

# Creditors' Seniority and Sovereign Risk: Evidence from Debt Composition

Prepared by Chiara Ferrero, Sansan Vincent de Paul Kambou, Kady Keita

Authorized for distribution by Joseph Thornton
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper shows that creditor composition has economically meaningful implications for both the likelihood of sovereign debt crises and access to international capital markets. A central finding is the asymmetric role of IMF lending relative to other creditor groups. We show that debt owed to the IMF and the World Bank is, on average, the most senior, followed by debt owed to official bilateral creditors. Private creditors, notably bondholders and commercial banks, are on average junior to official creditors, with commercial banks being the least prioritized group for repayments. Beyond characterizing the seniority hierarchy, our empirical analysis shows that creditor composition has economically meaningful implications for sovereign risk. Our results show that IMF credit outstanding as a share of Gross National Income (GNI) is robustly and negatively associated with the probability of a debt crisis, with this stabilizing effect weakening progressively as debt stocks rise. Turning to sovereign borrowing costs, we find that IMF lending is negatively associated with sovereign bond spreads.

RECOMMENDED CITATION: Ferrero C., Kambou S. V. P., Keita K. (2026): “Creditors Seniority and Sovereign Risk: Evidence from Debt Composition” IMF Working Paper No WP/26/161.


# Creditors Composition and Sovereign Risk: Evidence from Debt Composition

Prepared by Chiara Ferrero, Sansan Vincent de Paul Kambou, Kady Keita $^{1}$

## Table of Contents

Table of Contents....2
1. Introduction....4
2. Data....6 Figure 1: Scatter Plots of Sovereign Bond Spreads and Debt Composition by Creditor Type....7
3. Evidence on the Seniority Structure of Debt....8 Figure 2: Composition of Sovereign External Debt by Creditor Group....8 Measuring Seniority....9 Stylized Facts on Seniority....10 Figure 3: Creditors' RPDs (Overall sample)....12 Figure 4: Creditors' RPDs (Low- and middle-income countries)....12
4. Creditor Composition and Sovereign Risk: Empirical Strategy and Results....14 Creditor Composition and Debt crises....14 Table 1 : Baseline Estimates of the Effect of Creditor Composition on Debt Crises....16 Table 2: IV-Estimates of the Effect of Creditor Composition on Debt Crises....18 Table 3: Non-Linear Effects of IMF Credit Outstanding on Sovereign Debt Crises....20 Creditors Composition and Market Access....20 Sovereign bonds spreads....20 Table 4: Baseline Estimates of Creditor Seniority's Impact on Bonds Spreads....22
5. Robustness Tests....24 Alternative samples....24 Table 5: Robustness Tests with Alternative Sample....24 Additional controls....25 Alternative estimation Methods....26
6. Conclusion....27
Appendices....28 Appendix A....28 Table A1: Overview of control variables....28 Table A2: Descriptive statistics....29 Table A3: Share of Senior Debt and the Sovereign Debt Crisis....29 Table A4: Share of Senior Debt and Borrowing Costs....30 Figure A1: Analysis of Creditors' RPDs in Countries with an IMF Program....31 Figure A2: Analysis of Creditors' RPDs in Countries During Financial Crises....32 Figure A3: Percentile distribution of external debt stock as % of GNI....32 Appendix B....33

Table B1: Robustness Test - Additional controls .... 33
Table B2: Robustness Test - Additional controls .... 33
Table B3: Robustness Test - Alternative estimation methods .... 34
References.... 36

## 1. Introduction

Global debt as share of GDP peaked at 258 percent of GDP in 2020 during the COVID emergency, and decreased afterwards, remaining however at levels higher than pre-COVID $^{2}$ . As nations face high levels of public debt, the role of the composition of debt, particularly the hierarchy between senior and subordinated claims, is crucial to understand debt dynamics that can affect the cost of accessing new credit as well as the sustainability of debt.

The hierarchy between senior and subordinated claims, or the seniority structure of debt, refers to the priority with which creditors are repaid when a debtor country is unable to repay all obligations on time. The legal and de facto seniority structure of debt may differ, with the de facto structure being dependent not only on the legal contracts, but also on established conventions. Schlegl et al. (2019) have provided evidence on the de facto seniority structure of debt. The authors show that sovereign borrowers selectively default on their creditors, and they find that the IMF and multilateral creditors hold the most senior status, while unexpectedly finding that bilateral official loans are treated as less senior than Bonds creditors. The latter finding differs from the general convention that bilateral official loans are at least as senior as private loans, in line for example with the comparability of treatment principle of the Paris Club.

Given potential differences in how countries prioritize repayments to different creditors, the composition of debt could affect the cost of new credit and the outcome of debt restructuring negotiations. Indeed, the manner of restructuring negotiations is not independent of the creditor hierarchy, as it may be affected by the presence of preferred creditors, the share of senior debt in the total debt stock, and the need, during periods of severe stress, to preserve sources of financing that could continue to lend when markets withdraw.

As a result, the composition of debt by creditor type can be an important determinant of sovereign risk, although existing theoretical and empirical literature has documented an ambiguous effect of creditors seniority on sovereign financing. On one hand, the intervention of multilateral creditors can play a catalytic role by facilitating access to financing during crises (Corsetti et al., 2006; Boz, 2011). On the other hand, an excessive share of senior debt can lead to a subordination effect, increasing the risk premiums demanded by junior creditors (Dell’Erba et al., 2013; Steinkamp and Westermann, 2014). The works of Broner et al. (2014) illustrate the potential conflicts and inefficiencies generated by the presence of multiple creditors with various seniority statuses, which can lead to debt crises. Additionally, the models of Diamond & Rajan (2001) and Gennaioli et al. (2014) demonstrate how seniority can influence market liquidity and exacerbate financial crises during times of stress. This perspective is complemented by the analysis of Arellano & Ramanarayanan (2012), which considers the effect of a country's reputation on its financing costs and access to credit, taking into account the debt structure. In the European context, Steinkamp and Westermann (2014) have shown that an increase in the share of multilateral loans in public debt is correlated with a rise in sovereign bond spreads, reflecting an increased risk premium for subordinate creditors. These findings are particularly relevant for developing economies, where dependence on official creditors is more marked and access to financial markets may be more volatile (Saravia, 2010). Sometimes, this dependence prompts governments to austerity to avoid high restructuring costs, although in some cases, increased senior debt can lead to more lenient fiscal policy (Corsetti & Dedola, 2016; Cheelo et al., 2023). Corsetti and Dedola's (2016) modeling underscores this idea, finding that creditor seniority can not only affect borrowing costs but also alter the incentives of states to generate budget surpluses or restructure their debt during crises.

Building on this literature, our paper empirically revisits the de facto seniority structure of debt and investigates how the composition of debt by creditor type can impact countries' likelihood to experience debt crises and their ability to tap international capital markets.

By exploiting disaggregated debt data from 119 emerging markets and developing economies from 1980 to 2022, we show that on average the IMF and the World Bank are the most senior creditors. Unlike in the results of Schlegl et al. (2019), we find that sovereigns facing repayment difficulties are more likely to default on private claims, such as bondholders or commercial banks, than on official bilateral creditors. Commercial banks in turn are the least likely to see their repayments prioritized. The seniority of bilateral creditors is in line with general convention, which draws from the Paris Club principles on comparability of treatment, the G20 Common Framework, and the important role of bilateral lenders during crises.

Our empirical results show that while a positive conditional correlation exists between debt from other creditor groups and the likelihood of a debt crisis, this is not true in the case of an increase in debt outstanding to the IMF as share of Gross National Income (GNI) $^{3}$ . The mitigating effect of IMF loans on the likelihood of debt crisis remains significant for countries with debt stock surpassing 100 percent.

Moreover, the results show that an increase in borrowing from the IMF is associated with an improvement in market access proxies, as measured by bond spreads. Instead, an increase in borrowing from more junior creditors is associated with an increase in bonds spreads. The estimation of this impact however, may be affected by selection bias, as countries' characteristics may affect both their access to markets and the composition of their debt. While we are able to address this issue in the case of IMF borrowing with an instrumental variable strategy, the case of other multilateral creditors and other lending comprises different rules and agencies and addressing the bias is less straightforward, and the subject of further research on this topic.

The remainder of the paper is organized as follows: Section 2 describes the data. Section 3 introduces new evidence regarding the seniority structure of debt. Section 4 describes our empirical strategy and the results of the analysis. Section 5 delves into robustness tests to validate the reliability of our findings. Finally, Section 6 concludes by summarizing our main findings.

## 2.Data

This analysis uses annual data spanning the period from 1980 to 2022, including 119 emerging market and developing economies. We categorize external creditors into five distinct groups based on the World Bank's classification as used in the International Debt Statistics: (i) bilateral creditors; (ii) multilateral institutions, excluding the IMF; (iii) bondholders $^{4}$ ; (iv) long-term commercial bank loans and credits, which include syndicated bank loans and supplier credits extended by exporters and other vendors of goods; and (v) the International Monetary Fund (IMF) $^{5}$ . We use data on debt stocks from IDS, and debt defaults from the BoC-BoE sovereign default database (see Beers et al., 2023). In the context of the IMF, the BoC-BoE sovereign default database generally reports payments overdue for at least 6 months as payments in arrears, although the IMF has ultimately never incurred ultimate losses on its loans as even in instances of delayed payments, the IMF has eventually been repaid. $^{6}$

To measure sovereign risk, we employ a dummy variable indicating sovereign debt crises as defined by Laeven and Valencia (2020). $^{7}$ We use bond yield spreads from the JPM EMBIG index $^{8}$ , and data on sovereign ratings, calculated using the average ratings from the three primary credit rating agencies: Moody's, Fitch, and Standard & Poor's (S&P). $^{9}$ Additionally, our analysis incorporates a range of control variables, including GDP per capita, GDP growth, the VIX index, which measures expected stock market volatility, the ratio of short-term debt to total external debt, a dummy variable for prior debt restructurings, a dummy variable indicating banking crises, and foreign direct investment (FDI) flows, among others. Tables A1 and A2 in the Appendix provide a detailed overview of all the variables used in our analysis, accompanied by descriptive statistics.

To provide an initial descriptive overview, Figure 1 complements the summary statistics by providing descriptive evidence on the relationship between sovereign bond spreads and the composition of external debt. The simple pairwise correlations point to some differences across creditor groups. IMF debt is weakly negatively correlated with EMBI spreads, while multilateral debt excluding the IMF is essentially uncorrelated with spreads. By contrast, bilateral debt displays a more pronounced negative correlation with spreads, whereas private debt is positively correlated with sovereign spreads. Although purely descriptive, these patterns are consistent with the paper's broader argument that creditor composition is associated with different market perceptions of sovereign risk. These figures should not, however, be interpreted as evidence of causality, since debt composition itself may be shaped by underlying macroeconomic conditions and market access.

Figure 1: Scatter Plots of Sovereign Bond Spreads and Debt Composition by Creditor Type

[[KC_IMAGE_001]]


[[KC_IMAGE_002]]


[[KC_IMAGE_003]]


[[KC_IMAGE_004]]

Source: Authors' calculations based on data from the World Bank's International Debt Statistics (IDS) and JPM's Emerging Markets Bond Index Global (EMBIG).

## 3.Evidence on the Seniority Structure of Debt

The distribution of creditors has undergone significant changes over the last 45 years. The 1990s were marked by a notable increase in the share of bonds relative to bank loans and commercial credits, particularly following the Brady debt restructuring agreements. Although bilateral creditors and the IMF experienced a slight decline after the 1990s, the overall share of official lending, including other multilaterals, has remained broadly steady. As shown in Figure 2, new lenders such as China have also strengthened their role.

Figure 2: Composition of Sovereign External Debt by Creditor Group

[[KC_IMAGE_005]]

Source: Authors' calculations based on data from the World Bank's International Debt Statistics (IDS)

Against this backdrop, we look at whether creditors' treatment has also changed over time. Traditionally, multilateral institutions such as the IMF and the World Bank have enjoyed senior creditor status, followed by bilateral creditors grouped within the Paris Club and private creditors (bondholders and commercial banks). The seniority of the IMF and of multilateral creditors is usually supported by the Paris Club, with multilateral credit excluded from restructuring. The de-facto senior status is seen as supporting the stabilizing role of multilateral institutions, perceived as lenders of last resort (Fischer, 1999 and Steinkamp and Westermann, 2014). In addition, the IMF and WB have implemented policies on arrears that regulate lending to countries in arrears (IMF, 2015 and 2022).

However, seniority of creditors may have changed over time, as creditors implemented policies to deal with arrears, the international financial system evolved, new creditors like China increased their global role, and a succession of systemic shocks (2008 crisis, Covid-19 pandemic) took place. $^{10}$ In the following, we empirically evaluate the seniority of the main groups of lenders over time.

## Measuring Seniority

Recent research by Schlegl et al. (2019) has explored the treatment of creditors in default scenarios. The authors propose two indicators to evaluate seniority, based on arrears to different types of creditors (relative percentage of amounts in arrears indicator) and on the magnitude of creditors' losses, and provide empirical evidence confirming that multilateral institutions like the IMF and World Bank are senior creditors. However, the authors find that, contrary to conventional understanding, bilateral creditors are not senior to private creditors. The authors also find that the average haircut on official creditors' debt is higher than the one on private creditors.

Building upon this research, we replicate the relative percentage of amounts in arrears indicator computed in Schlegl et al. (2019) using the BoC-BoE data on defaults (while the authors use arrears data obtained from the World Bank's Debt Reporting System). The BoC-BoE database classifies as defaults cases in which “debt service is not paid on the due date or within a specified grace period or payments are not made within the period specified under a guarantee”. $^{11}$ This does not imply that payments are not eventually made, in the case of IMF, as mentioned above, loans have historically been ultimately repaid, so the dataset includes payments with reported protracted delays $^{12}$ . The indicator includes two elements: the first component (A) reflects the absolute scale of sovereign defaults per unit of loan from a specific creditor group, for a given country, and the second component (B) measures the absolute scale of sovereign defaults per unit of loan of all creditors, for a given country. The indicator captures the difference (A-B) between the sovereign default-to-debt ratio of a specific creditor group and the total sovereign default-to-debt ratio of all creditors, for a given country.

$$
\boldsymbol {R P I D} = \frac {\text {default} _ {i , t , k}}{\text {debt} _ {i , t , k} + \text {Sovereign default} _ {i , t , k}} - \frac {\sum_ {k} \text {default} _ {i , t , k}}{\sum_ {k} (\text {debt} _ {i , t , k} + \text {Sovereign default} _ {i , t , k})} \tag {A}\tag{1}
$$

This formula measures, for a given country i at a given time t, the difference between the default-to-debt ratio of a specific creditor group k and that of the entire creditor portfolio, ranging within [-1, 1]. This approach allows for an analysis of how creditors compare to each other in terms of seniority during periods of repayments difficulties. A negative RPID indicates a preferential treatment in debt repayment, whereas a positive RPID signals a less preferential treatment in debt repayment practices. In other words, creditors with a negative RPID are favored and experience fewer defaults rates than the average, while those with a positive RPID experience higher default rates compared to their counterparts.

This methodology mitigates the risk of the seniority ranking being affected by specific economic characteristics of the country, focusing instead on the actual status of creditors using total debt and default data. By calibrating outcomes according to each country's borrowing structure, the RPID allows for a relative comparison among creditors.

## Stylized Facts on Seniority

Figure 3 presents the RPID for various creditor groups for the overall sample of countries, and figures 4 and 5 present the results by income groups. $^{13}$

Figure 3 shows that the IMF and the World Bank display the most negative RPID values in the sample, confirming their seniority. This result is robust and consistent with the existing literature. Schlegl et al. (2019) already established the IMF as the most senior creditor, and our replication of the RPID measure, applied to an extended sample covering the period 1980–2022, corroborates this finding over a longer time horizon. The World Bank is found to benefit from a comparable seniority status.

Official bilateral creditors also display negative RPID values on average, ranking second behind multilateral creditors. This result is of particular importance as it diverges from the findings of Schlegl et al. (2019), who find that bilateral creditors are treated as less senior than private creditors. Several factors may explain this divergence from Schlegl et al. (2019). First, their analysis covers the period 1979–2006, whereas our sample extends to 2022. Second, the rise of non-Paris Club bilateral creditors since the 2000s has profoundly altered the structure of bilateral debt flows, which may affect the default dynamics observed. Third, differences in data sources and the proxies used to measure seniority — as discussed above — may introduce discrepancies in the measurement of arrears, particularly for bilateral creditors where reporting may be less systematic. Our result is instead consistent with the general convention that official bilateral loans receive preferential treatment relative to private claims, in line with the Paris Club's comparability of treatment principle and the G20 Common Framework. The Paris Club, as a coordination mechanism among official bilateral creditors, has historically structured sovereign debt restructurings around a comparability of treatment principle that implicitly preserves the relative seniority of official creditors over private ones. The G20 Common Framework, adopted in 2020, extends this logic to a broader set of bilateral creditors, including non-traditional members. Recent work has documented that the implementation of this framework has been slower than anticipated in several recent cases reflecting the coordination challenges inherent in a more fragmented and heterogeneous official creditor landscape than in previous decades (Gelpern et al., 2023; Horn, Reinhart, and Trebesch, 2021). These coordination frictions may partially explain the temporal variations observed in the RPID of creditors.

Private creditors — bondholders and commercial banks — display positive RPID values, indicating that they bear a higher-than-average share of defaults. This result is consistent with several strands of the literature and has direct and important economic implications. On one hand, Panizza et al. (2009) document that sovereign bonds in emerging markets are particularly exposed to political and economic risk fluctuations, while Trebesch and Zabel (2017) show that restructurings involving bondholders are associated with larger haircuts and longer resolution delays. On the other hand, subordinated claims imply that creditors incorporate ex ante a subordination risk premium into the conditions under which they are willing to lend. Steinkamp and Westermann (2014) showed empirically, in the European context, that an increase in the share of senior multilateral debt in the total debt stock is associated with wider sovereign bond spreads — a subordination mechanism that our results confirm in the broader context of emerging market and developing countries, with the exception of the IMF. This seniority structure also affects the dynamics of restructuring negotiations: knowing that they will be treated as junior, private creditors tend to demand stricter lending conditions, shorter maturities, and higher rates ex ante, or to withdraw from markets when stress is perceived, amplifying the sudden stop dynamics documented by Calvo (1998). We find that on average commercial banks are treated as less senior compared to bondholders. This could be explained by their exposure to higher-risk countries through syndicated loans, by more diffuse bargaining power in restructurings, and by the historical losses absorbed during the debt crises of the 1980s.

We identify overlaps between senior creditors and other creditor groups in the dynamics of sovereign defaults observed at the country-year level. These overlaps are not widespread across the full sample. Instead, they are concentrated in a limited number of countries and occur within relatively well-defined historical sequences.

A first wave spans the 1980s and the early 1990s. It mainly concerns Latin America, as well as a number of low-income countries facing balance-of-payments crises. This wave includes notable episodes in Peru (1985–1993), Vietnam (1985–1993), and Zambia (1986–1994). A second sequence emerges in the 1990s and the early 2000s, in contexts of political transition or post-conflict adjustment, for example in Bosnia and Herzegovina (1992–2000), Iraq (1990–2005), and Liberia (1998–2008). Finally, a more recent phase extends into the 2010s and 2020s, marked by prolonged episodes of distress, especially in Sudan (1981–2021), Somalia (2005–2020), and Zimbabwe (2003–2022).

The configuration of creditors involved also varies across episodes. Overlaps with bilateral creditors appear especially persistent in Sudan, Somalia, and Zimbabwe. Overlaps involving banks are more commonly observed in episodes of political transition (e.g. Peru) or conflict (e.g. Iraq). By contrast, overlaps with bondholders are concentrated in a few large-scale market default episodes, notably Argentina (2002–2003), Côte d'Ivoire (2001 and 2005–2008), and Zambia (2021–2022).


[[KC_IMAGE_006]]


Figure 3: Creditors' RPDs (Overall sample)

[[KC_IMAGE_007]]


Figure 4: Creditors' RPIDs (Low- and middle-income countries)

[[KC_IMAGE_008]]


[[KC_IMAGE_009]]


Figure 5: Creditors' RPDs (Upper middle-income countries)

[[KC_IMAGE_010]]


[[KC_IMAGE_011]]

Source: Authors' calculations. Figures 3–5 are based on data from the World Bank's International Debt Statistics (IDS) and the Bank of Canada–Bank of England Sovereign Default Database.

To rule out the hypothesis that the observed seniority structure merely reflects countries' economic characteristics, in particular a classification based on income groups, and to address the risk that changing or endogenous group definitions may bias the results, we conduct robustness checks based on subsamples defined by observed financial conditions. More specifically, we distinguish countries according to their participation in an IMF-supported program, and episodes of financial crises.

The results, reported in Appendix Figures A1 and A2, confirm the overall stability of preferred creditor status. The repayment hierarchy identified in our data therefore does not appear to be a result of the initial country classification, but rather the expression of a more general pattern of prioritization in sovereign repayment decisions. Across all subsamples, claims by the IMF and the World Bank consistently appear as the most senior, with the lowest RPIIDs. Bilateral creditors also occupy a relatively privileged position, ranking robustly behind multilateral institutions but ahead of private creditors. By contrast, bondholders, and especially commercial banks, display higher RPIIDs, indicating that they bear a larger share of repayment interruptions and therefore occupy the most junior positions in the effective repayment hierarchy.

## 4. Creditor Composition and Sovereign Risk: Empirical Strategy and Results

## Creditor Composition and Debt crises

Previous research has primarily focused on the impact of IMF programs on sovereign access to other lending, as well as sovereign debt rescheduling (e.g. Bai et al 2024, and Krahnke 2023). This study complements existing literature by exploring the influence of sovereign debt composition, particularly the seniority hierarchy among creditors, on the likelihood of debt crises and market access.

First, we analyze the likelihood of a debt crisis using a probit model, which assesses the impact of public debt ratios of each creditor group as a percentage of gross national income on the occurrence of debt crises. Second, we use an instrumental variable to address endogeneity issues for IMF lending. Finally, we investigate market access to capture investor responses to changes in creditor composition.

To assess the impact of debt composition on the likelihood of debt crises occurring, we estimate the following linear probability model:

$$
\begin{array}{r} P r o b (\boldsymbol {D e b t C r i s i s} = \mathbf {1}) = \beta_ {1} I M F _ {i, t} + \beta_ {2} M u l t i l a t e r a l _ {i, t} + \beta_ {3} B i l a t e r a l _ {i, t} + \beta_ {4} B o n d h o l d e r s _ {i, t} + \\ \beta_ {5} C o m m e r c i a l B a n k _ {i, t} + \delta X _ {i, t} + \eta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \end{array}\tag{2}
$$

In this model, the dependent variable, $Prob(Debt\ Crisis = 1)$ , is a binary variable that takes the value 1 if a debt crisis occurs in country i during year t. The regressors include IMF debt, other multilateral debt, bilateral debt, bond debt, and commercial bank debt. $^{14}$ $X_{I,t}$ represents a vector of macroeconomic variables including the logarithm of GDP per capita, capturing baseline economic development; annual GDP growth rates, proxying for cyclical fiscal capacity; the CBOE Volatility Index (VIX), the ratio of short-term external debt to total external debt, signaling near-term liquidity pressures; and net FDI flows, reflecting foreign investor confidence in institutional stability.

To address historical debt issues, we also incorporate two critical dummy variables. The first identifies countries that have undergone private or official debt restructurings within the preceding five-year window. The second flags economies with at least one systemic banking crisis in the sample period, acknowledging the dual sovereign-banking risk nexus documented in the literature (Reinhart and Rogoff, 2011). These indicators mitigate omitted variable bias by accounting for institutional memory among investors and structural vulnerabilities. Finally, country fixed effects $\eta_{i}$ control for time-invariant unobserved characteristics specific to each country, whereas year fixed effects $\mu_{t}$ capture year-specific shocks that may impact all countries. The term $\varepsilon_{i,t}$ represents the error term of the model.

Table 1 illustrates the marginal effects of sovereign debt composition, broken down by creditor type, on the probability of debt crisis. Columns 1 to 5 separately analyze the impact of each type of creditor, while column 6 provides an overview by considering all creditors simultaneously, offering a clearer understanding of how debt composition influences risk of debt crisis. As explained in more detail below, the composition of debt is not exogenously assigned to countries however, so the results in this table cannot be interpreted causally.

The results indicate that private debt, particularly the share of bonds, is positively associated with the likelihood of a sovereign debt crisis. In other words, a one percentage point increase in the share of bonds held as debt (as percentage of GNI) is associated with a rise of between 0.24 and 0.29 percentage points in the probability of a crisis. This effect can be explained by the volatility of bond markets, which are sensitive to liquidity shocks and economic fluctuations. During periods of economic downturn, bondholders demand higher returns, exacerbating financial pressures. In contrast, commercial and bank loans do not have a significant correlation with default probability, possibly due to their contractual flexibility and the long-term relationships between lenders and borrowers, which tend to be more resilient to economic turbulence, thus mitigating their influence on crisis risk.

An increase in official debt, including multilateral (other than IMF) and bilateral loans, is also positively associated with the likelihood of a debt crisis. A one percent increase in multilateral loans is associated with an increase in the probability of default by an estimated 0.30 percentage points, while an increase in bilateral loans is associated with a 0.43 percentage points increase in risk. This can be explained by the fact that these loans are often granted in contexts where the country's economic situation is already fragile, reflecting a selection bias of countries in more fragile economic conditions accessing multilateral funding, and cannot be interpreted as a causal effect of official lending on the likelihood of debt crises.

Unlike other types of debt, IMF credit outstanding is associated with a reduction in the probability of sovereign. The coefficients in columns (1) and (6) show that an increase in IMF debt is associated with a reduction in the risk of default, with an estimated effect ranging between -0.81 and -1.32 percentage points.

The IMF occupies a specific position in the creditor hierarchy. Its intervention appears to be associated with a reduction in sovereign risk, possibly because of its role as a liquidity provider, its signaling effect vis-à-vis markets, and the macroeconomic discipline associated with IMF-supported programs. This interpretation, however, should be read with caution as the observed association may still reflect selection mechanisms, since countries that turn to the IMF are often already facing macroeconomic or financial vulnerabilities. The results in this table should therefore be interpreted as conditional associations, while causal interpretation should be reserved for the instrumental-variable estimations.

In practice, the effect of an increase in senior debt could depend on the type of creditor, the nature of its intervention, and the initial conditions of the borrowing country.

These results are consistent with the literature on the “seniority conundrum.” Steinkamp and Westermann (2017) show, in the context of the European sovereign debt crisis, that sovereign spreads are positively associated with the share of multilateral loans in the total stock of public debt, interpreted as a proxy for the senior tranche of debt. Their argument is that the intervention of official creditors benefiting from preferred creditor status may reduce the expected recovery rate of private creditors by placing them in a more junior position. Private investors then require a higher risk premium to compensate for this implicit subordination.

Control variables have the expected signs. Both the logarithm of GDP per capita and GDP growth show negative and significant coefficients, suggesting that more economically developed countries and those with high growth rates have a better capacity to meet their financial obligations. The positive coefficient on the VIX volatility index, which measures uncertainty in global financial markets, reflects the positive association between financial market uncertainty and the risk of debt crises, which could be due to reduced capital flows to emerging economies reflecting investors' heightened risk aversion. Similarly, high levels of short-term debt also increase the probability of sovereign default. Additionally, as found by Laeven and Valencia (2012), banking crises weaken national financial systems, exacerbate pressures on public finances, and increase the likelihood of sovereign default, and the coefficient has positive sign as expected. Finally, foreign direct investment (FDI) appears to be negatively associated with the likelihood of debt crisis.

To focus more directly on the structure of debt, rather than the share of debt over GNI, we re-estimate the model using the share of senior creditor groups in the total stock of public debt. We further distinguish, on the one hand, the share of IMF debt in the total debt stock and, on the other hand, other senior loans, namely multilateral loans excluding the IMF and bilateral loans. The results presented in Table A4 in the Appendix show that the share of debt held by the IMF is negatively and significantly associated with the probability of a debt crisis. In column (1), a one percentage point increase in the IMF share of total debt is associated with a decline of about 0.80 percentage point in the probability of a crisis. When IMF debt and debt owed to other senior creditors are included simultaneously in column (3), the effect remains negative and statistically significant, with an estimated decline of about 0.68 percentage point. When the senior share is considered as a whole, the coefficient is positive but not significant.

Table 1 : Baseline Estimates of the Effect of Creditor Composition on Debt Crises


Robust standard errors in parentheses

$$
^ {* * *} \mathrm{p} <   0. 0 1, ^ {* *} \mathrm{p} <   0. 0 5, ^ {*} \mathrm{p} <   0. 1
$$

A key empirical challenge in this study is the non-random allocation of lending, as countries' macroeconomic conditions, structural strength, access to markets and cyclical position can affect their existing stock of debt as well as their access to new borrowing. Countries facing worsening macroeconomic conditions may be both more likely to borrow from multilateral creditors and more likely to experience an episode of sovereign distress. This creates an endogeneity problem, as lending may be jointly determined with sovereign risk by omitted factors that are difficult to observe and that evolve over time. To address this concern for the case of IMF lending, we rely on an instrumental-variable strategy designed to isolate plausibly exogenous variation. However, for other creditor categories, where we do not have an available instrument, the estimates cannot be interpreted causally and should be interpreted more cautiously as conditional correlations.

Our identification strategy exploits time variation in the IMF's aggregate lending capacity. IMF liquidity reflects the resources available for Fund lending in a given year and therefore affects the amount of financing that the IMF can extend across borrowing countries. Taken alone, however, IMF liquidity is unlikely to satisfy the exclusion restriction, because it may be correlated with broader global conditions that also affect sovereign risk. To address this concern, and following the logic of Nunn and Qian (2014), Gehring and Lang (2020), Langue (2021), and Bai et al. (2024), we interact IMF liquidity with a cross-country measure of historical exposure to IMF lending. The intuition is that changes in IMF liquidity should matter more for countries that have historically relied more heavily on IMF financing. The instrument is defined as follows:

$$
I V _ {i, t} = \text { Historical\_IMF\_Loan } _ {i, t} \times I M F \_ L i q u i d i t y _ {t}\tag{6}
$$

where $Historical\_IMF\_Loan_{i,t}$ captures a country's long-run exposure to IMF financing, measured as the average annual IMF loan-to-GDP ratio over the previous 10 years, and $IMF\_Liquidity_t$ is the ratio of the Fund's liquid assets to its liquid liabilities. This interaction generates differential exposure across countries to fluctuations in the IMF's lending capacity. Conditional on country and year fixed effects, and on the set of macroeconomic controls included in the baseline specification, the identifying assumption is that IMF liquidity affects sovereign crisis risk only through its effect on IMF lending, rather than through other country-specific channels. Under this assumption, the interaction term isolates a plausibly exogenous component of IMF lending. The IV results, reported in Table 2, show that higher IMF lending is associated with a statistically significant reduction in the probability of a sovereign debt crisis. In column (1), the coefficient on IMF lending is negative and significant, suggesting that IMF financing has a stabilizing effect on sovereign debt dynamics. In column (2), once other creditor categories are included, the magnitude of the IMF coefficient increases and remains strongly significant. In column (3), the result continues to hold in the full specification. We interpret this finding as evidence that IMF lending can reduce crisis risk by providing liquidity during periods of stress, supporting policy adjustment, and strengthening creditor confidence. However, the finding that IMF lending reduces the probability of a sovereign debt crisis can be interpreted as extending beyond the simple channel of short-term liquidity. Recent work by Balestrini (2026) shows that restructurings conducted under IMF-supported programs are accompanied by greater maturity extensions, higher haircuts, and a faster return to international capital markets. Within her analytical framework, IMF conditionality acts as a commitment mechanism that mitigates post-restructuring dilution and enhances the credibility of fiscal adjustment. This mechanism is particularly relevant here. If IMF intervention contributes to lengthening the debt profile, reducing refinancing pressures, and bolstering repayment credibility, it is then likely to decrease the probability that a liquidity strain will escalate into a full-blown sovereign debt crisis. The coefficients on other creditors' classes remain broadly positive, but as highlighted above should be interpreted as conditional correlations given that the instrument is only applicable to IMF lending.

Table 2: IV-Estimates of the Effect of Creditor Composition on Debt Crises


Robust standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Although IMF lending appears to have a stabilizing effect, this impact may be constrained under certain macroeconomic conditions, particularly when a country's overall debt level reaches critical thresholds. To check how results may change for highly indebted countries, we divide the sample based on the percentile distribution of external debt stock (see Figure A.5 in Appendix).

To examine whether this stabilizing effect varies with the level of indebtedness, we have split the sample based on the distribution of external debt stocks. The lower percentiles (10 to 40) correspond to countries with a relatively limited debt burden—ranging between 18% and 40%—and, consequently, a comparatively low risk of crisis. The intermediate percentiles correspond to debt levels falling between the 40th and 75th percentiles. Within this range, external debt represents between 43% and 68% of GDP. Finally, the upper end of the distribution comprises highly indebted countries; their percentiles (75–100) correspond to debt stocks ranging from 68% to 159% of GDP.

The empirical analysis presented in Table 3 shows that an increase in IMF lending as share of gross national income (GNI) is associated with a reduction in the probability of a debt crisis within these subsamples; however, the magnitude of the marginal effect diminishes as debt levels rise. In other words, the coefficient on IMF lending remains negative when the debt stock is above 70%, 90% and even above 100%, but its magnitude decreases. At high levels of debt, the debt burden, refinancing pressures, and concerns regarding creditor subordination may limit the marginal gains derived from increased IMF support. This observation is in line with the other findings in the paper and in the literature: the impact of creditor composition on sovereign risk depends not only on the volume of debt, but also on the position of each creditor within the repayment hierarchy and the extent to which its financing affects overall debt sustainability.

Table 3: Non-Linear Effects of IMF Credit Outstanding on Sovereign Debt Crises


Note: All estimations include control variables (logarithm of GDP per capita, GDP growth, VIX index, short-term debt as a percentage of total external debt, total debt restructuring, banking crises, and net foreign direct investment). The model also accounts for country-specific fixed effects and year fixed effects. The interaction terms in the models correspond to dummy variables that take the value of 1 based on the level of external debt stock in relation to GDP, reflecting different thresholds of debt burden (e.g., <70%, >70%, >90%, >100%, and >120%). These different dummy variables were also added in each specification. Robust standard errors in parentheses \*\*\* p<0.01, \*\* p<0.05, \* p<0.1

## Creditors Composition and Market Access

## Sovereign bonds spreads

In this section, we examine how sovereign bond spreads respond to debt composition in our sample of countries. Since lending is not randomly allocated, an estimation bias may result from omitted variables. Indeed, economic conditions in a country can influence both the amount of loans granted by creditors and the spreads of sovereign bonds, thus introducing an omitted variable bias that complicates the estimation of the causal effects of these loans on bond spreads. To address this potential endogeneity, we instrument IMF lending as in the previous section, using the country's history of IMF borrowing and IMF liquidity. Equation (3) represents the first stage, and equation (4) the second stage. As in the previous section, since we are not instrumenting for the other classes of creditors, results should not be interpreted as causal inferences.

$$
I M F _ {l o a n s _ {i t}} = \alpha_ {0} + \alpha_ {1} I V _ {i t} + \alpha X _ {i t} ^ {\prime} + \eta_ {i} + \mu_ {t} + \pmb {\varepsilon} _ {i t}\tag{3}
$$

$$
E M B I G _ {i t} = \beta_ {0} + \beta_ {1} \widehat {I M F _ {l o a n s}} _ {i t} + \sum_ {c = 1} ^ {4} \theta_ {c} C r e d i t o r _ {i, t} ^ {(c)} + \beta X _ {i t} ^ {\prime} + \eta_ {i} + \mu_ {t} + \varepsilon_ {i t}\tag{4}
$$

In the second stage, the fitted values from the first stage, which capture IMF lending, are then used to estimate the relationship between IMF lending and sovereign bond spreads. This regression also controls for the relative importance of other creditors, and incorporates fixed effects and additional control variables to isolate the specific impact of IMF lending on market reactions from the influence of the overall creditor composition. $\beta X'_{it}$ is a vector of control variables with their associated coefficients. The country-specific fixed effects i capture unobservable but time-invariant characteristics unique to each country, while the time effects $\eta_{i}$ capture time trends affecting all countries simultaneously, such as global financial crises. Finally, the random error term $\varepsilon_{it}$ represents unobserved idiosyncratic factors affecting the spread for country i at time t.

The empirical results are presented in Table 4. Column (1) reports a standard OLS regression, while column (2) presents our preferred specification — a Two-Stage Least Squares (2SLS) estimator — which corrects for the endogeneity bias arising from the potential simultaneity between IMF lending and sovereign distress. The Kleibergen-Paap rank statistic confirms the relevance of the instrument and alleviates concerns about weak identification.

Across both specifications, IMF credit outstanding is negatively and significantly associated with sovereign spreads. The 2SLS estimate is larger in magnitude than the OLS coefficient, consistent with a downward attenuation bias in OLS stemming from the endogenous nature of IMF lending — countries experiencing distress are more likely to seek IMF support, which would otherwise bias the coefficient toward zero or positive values. This negative association extends beyond a pure liquidity effect. IMF-supported programs may strengthen the credibility of macroeconomic adjustment and improve market expectations regarding the sovereign's future repayment capacity. Recent evidence (Balestrini 2026) suggests that IMF-supported restructurings are associated with larger maturity extensions, more favorable debt treatment, and faster market re-entry, while IMF conditionality may act as a commitment device that limits post-restructuring dilution. If IMF intervention reduces uncertainty about the future debt sustainability path, investors may require a lower risk premium, resulting in narrower sovereign spreads. It should nonetheless be noted that the direction of causality warrants careful interpretation: while the instrumental variable strategy addresses the most direct source of endogeneity, residual confounding from underlying macroeconomic fundamentals cannot be entirely ruled out.

The coefficients on non-IMF multilateral loans are positive and statistically significant in both columns, and the coefficient on bilateral loans becomes positive and significant in the 2SLS specification. These results may appear counterintuitive at first glance, as one might expect senior official creditors to signal creditworthiness to markets. However, this finding is more plausibly interpreted as reflecting an adverse selection effect: countries that rely more heavily on multilateral and bilateral official lenders are often those already facing tighter market access conditions or heightened solvency concerns, which simultaneously drive up sovereign spreads. In other words, the positive association likely captures the underlying risk profile of borrowing countries rather than the causal effect of official lending per se. This interpretation is consistent with the broader literature on the catalytic role of official finance and underscores the importance of appropriate instrumentation — a limitation we acknowledge explicitly.

Table 4: Baseline Estimates of Creditor Seniority's Impact on Bonds Spreads


Column 2 includes the instrument used to correct for the endogeneity bias related to IMF lending. Robust standard errors in parentheses.
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

The coefficients on bond and commercial bank loans are not statistically significant in the OLS specification but become positive and significant in the 2SLS estimates. This result is consistent with Panizza et al. (2009), who find that sovereign bonds in emerging markets are particularly sensitive to political and economic risk fluctuations. Trebesch and Zabel (2017) further document that restructurings involving bondholders are associated with significant spread increases, especially in the absence of official creditor support. Importantly, this positive association should not be interpreted as implying that bond issuance causes debt crises; rather, it reflects the fact that countries with greater exposure to private creditors tend to exhibit higher underlying credit risk, which is jointly reflected in both their creditor composition and their borrowing costs. Additionally, the results for bonds specifically may be biased by looking at two factors potentially driven by common unobserved characteristics: the cost of new borrowing and the stock of existing debt.

Beyond creditor composition, several macroeconomic factors play a significant role. Debt and currency crises are associated with significantly higher spreads, confirming the amplifying effect of crises on sovereign risk perceptions (Laeven and Valencia, 2012). Greater capital account and trade openness are associated with lower spreads in the 2SLS specification, consistent with the view that greater integration reduces country risk. A higher share of short-term debt as a percentage of GNI is positively associated with spreads, reflecting rollover risk. Past debt restructuring episodes are negatively associated with spreads in the 2SLS column, which may capture a relief effect once debt overhang is resolved. Finally, a higher GNI per capita is associated with lower spreads, consistent with the notion that macroeconomic strength reduces perceived sovereign risk.

To address concerns regarding the normalization of creditor claims and the generalizability of the baseline findings, Table A5 presents a complementary specification in which creditor exposures are expressed as shares of total external debt rather than as ratios to GNI. Here, the share of IMF debt remains negatively and significantly associated with sovereign spreads, and the share of senior creditor debt excluding the IMF is also negatively and significantly associated with sovereign spreads. The difference for other senior creditors with respect to the results where debt is expressed in share of GNI could be due to a non-linearity of this result with respect to the level of debt overall, potentially indicating that while an increase in the share of official debt in the portfolio is not necessarily associated with an increase in spreads, this may be more likely when the level of debt is higher as share of GDP.

## 5.Robustness Tests

## Alternative samples

To check the robustness of our analysis, we have made various sample adjustments taking into account specific periods that might influence the relationship between the composition of debt by creditor type and sovereign risk.


The results remain broadly stable despite these sample adjustments. In Table 5A, IMF lending remains negatively associated with the probability of a debt crisis, while multilateral loans excluding the IMF and bilateral loans remain positively and significantly associated with crisis risk. In Table 5B, which uses EMBIG spreads as the dependent variable, IMF credit outstanding is also negatively associated with market-perceived sovereign risk, whereas other exposures to official creditors are positively associated with spreads. As in the previous results however, the interpretation of the results for non-IMF creditors should remain cautious. In the absence of instruments that explicitly correct for endogeneity biases associated with these creditors, the coefficients should be interpreted as conditional associations rather than causal effects. Future research could further explore this issue by developing identification strategies that better isolate the specific effect of different creditor types on sovereign risk.

Moreover, since creditor exposures in these specifications are measured as a percentage of GNI, some positive coefficients may partly reflect a higher overall level of indebtedness, that is, the overall weight of debt, rather than only the composition of debt by creditor type.

Table 5: Robustness Tests with Alternative Sample


## Additional controls

To ensure that our results are not biased by the omission of certain potential determinants influencing the relationship between the composition of debt by creditor type and sovereign risk, we have integrated additional control variables. These variables include: institutional quality, international reserves, population density, debt service as a percentage of GNI, and terms of trade.

The estimates presented in columns $[2]$ to $[6]$ of Table B1 in the appendix, show that the effect of different creditor categories on debt crises remains robust and statistically significant, with coefficients close to those of the base model. The quality of institutions tends to reduce the risk of crises, although this effect is not always significant. Moreover, international reserves positively influence financial stability. Additionally, the inclusion of terms of trade shows their influence on sovereign risk.

## Alternative estimation Methods

Application of 2SLS-GMM: In the two models using Debt Crises and EMBIG as dependent variables, we strengthen the robustness of our estimation by applying 2SLS-GMM and incorporating, on one hand, the main instrument constructed from the product of historical IMF credit outstanding and IMF liquidity (IV = Historical IMF Credit outstanding × IMF Liquidity), and on the other hand, the lags of the potentially endogenous variables. The addition of lagged variables also helps isolate the exogenous effect of interventions while mitigating potential biases related to unobserved, time-varying factors that might simultaneously influence debt crises, bond spreads (EMBIG), and public borrowing decisions. The results, presented in Table B3 in the appendix, remain qualitatively comparable to those of the base model, confirming our initial conclusions.

## 6.Conclusion

This paper contributes to the literature on sovereign debt by providing new empirical evidence on the de facto seniority structure of creditors and its implications for sovereign risk. Using a measure of Relative Percentage in Default (RPID) — which captures the differential treatment of creditor groups during episodes of payment difficulties — we document a seniority hierarchy: multilateral creditors, notably the IMF and the World Bank, are on average treated as more senior, followed by official bilateral creditors, while private creditors — bondholders and commercial banks — are on average treated as junior. These findings are broadly consistent with Schlegl et al. (2019), although our estimates differ with respect to the relative ordering of non-multilateral creditor groups, a divergence that may reflect differences in sample composition, time period, and the granularity of the default data employed.

Beyond the characterization of seniority, our empirical analysis shows that creditor composition has economically meaningful implications for both the likelihood of sovereign debt crises and access to international capital markets. A central finding is the asymmetric role of IMF lending relative to other creditor groups. While we find a correlation between higher indebtedness to non-IMF creditors and the likelihood of debt crises, IMF lending as a share of GNI is robustly and negatively associated with crisis probability. This stabilizing effect persists across a wide range of specifications, alternative samples, and estimation strategies. The results indicate, however, that this effect weakens as debt stocks rise. While IMF lending is associated with a marked reduction in crisis probability for countries with indebtedness below 70 percent of GDP, this marginal effect declines progressively at higher debt thresholds. Fund-supported programs are intended to help members resolve BOP challenges and restore external viability, and these findings suggest that the IMF plays an important role in this sense.

The stabilizing role of IMF lending extends to sovereign borrowing costs. Our baseline estimates show that IMF lending is negatively associated with sovereign bond spreads, while higher indebtedness to other creditor groups is associated with wider spreads when debt is expressed as share of GNI. When creditor exposures are expressed as shares of total external debt, a higher share of senior debt — whether held by the IMF or by other senior official creditors — is negatively and significantly associated with sovereign spreads.

Several limitations of the present analysis warrant acknowledgment. While the instrumental variable strategy credibly addresses endogeneity concerns related to IMF lending, correcting for the non-random nature of other forms of official and private credit remains challenging. The positive association between non-IMF multilateral and bilateral loans and sovereign spreads in the baseline estimates may be due to an adverse selection effect — reflecting the risk profile of countries that rely on official creditors — rather than a causal impact of official lending on market perceptions. Future work exploiting exogenous variation in bilateral and multilateral credit flows would help sharpen these inferences.

## Appendices

## Appendix A

Table A1: Overview of control variables


Table A2: Descriptive statistics


Table A3: Share of Senior Debt and the Sovereign Debt Crisis


\*\*\* p<0.01, \*\* p<0.05, \* p<0.1


Robust standard errors in parentheses

Table A4: Share of Senior Debt and Borrowing Costs


Robust standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Figure A1: Analysis of Creditors' RPDs in Countries with an IMF Program

[[KC_IMAGE_012]]


[[KC_IMAGE_013]]


Figure A2: Analysis of Creditors' RPDs in Countries During Financial Crises

[[KC_IMAGE_014]]


[[KC_IMAGE_015]]

Source: Authors' calculations. Figures A1–A2 are based on data from the World Bank's International Debt Statistics (IDS) and the Bank of Canada–Bank of England Sovereign Default Database.

Figure A3: Percentile distribution of external debt stock as % of GNI

[[KC_IMAGE_016]]

The black dotted line represents a threshold corresponding to $70\%$ of GNI

Source: Authors' calculations. Data from the World Bank's International Debt Statistics (IDS).

## Appendix B

Table B1: Robustness Test - Additional controls


Table B2: Robustness Test - Additional controls


Robust standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Table B3: Robustness Test - Alternative estimation methods


Standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

## References

Acemoglu, D., & Robinson, J. A. (2012). Why Nations Fail: The Origins of Power, Prosperity, and Poverty. Crown Business.

Afonso, A., Arghyrou, M. G., & Kontonikas, A. (2012). The Determinants of Sovereign Bond Yield Spreads in the EMU. Journal of International Money and Finance, 31(3), 684-705.

Alfaro, L., & Kanczuk, F. (2009). Debt Maturity: Is Long-Term Debt Optimal? Review of International Economics, 17(5), 890-905.

Alfaro, L., Chanda, A., Kalemli-Ozcan, S., & Sayek, S. (2004). FDI and Economic Growth: The Role of Local Financial Markets. Journal of International Economics, 64(1), 89-112.

Arellano, C. (2008). Default Risk and Income Fluctuations in Emerging Economies. American Economic Review, 98(3), 690-712.

Arellano, C., Bai, Y., & Bocola, L. (2026). Sovereign default risk and firm heterogeneity. Journal of the European Economic Association, jvaf067.

Arellano, C., & Ramanarayanan, A. (2012). Default and the Maturity Structure in Sovereign Bonds. Journal of Political Economy, 120(2), 187-232.

Asonuma, T., & Joo, H. J. (2020). Sovereign Debt Restructurings: The Impact of Seniority and Coordination. Journal of International Economics, 123, 103305.

Asonuma, T., & Trebesch, C. (2016). Sovereign Debt Restructurings: Preemptive or Post-Default. Journal of the European Economic Association, 14(1), 175-214.

Asonuma, T., Niepelt, D., & Ranciere, R. (2019). Sovereign Bond Prices, Haircuts, and Maturity Extensions: Theory and Evidence from a New Database. IMF Working Paper, WP/19/226.

Bai, Y., Banerji, S., Wang, Z., & Zhang, W. (2024). Can participation in IMF programs facilitate sovereign debt rescheduling? The role of program size. Journal of International Money and Finance, 144, 103079.

Balestrini, T. (2026) Sovereign Defaults: Maturity Choice and Conditionality. Balestrini JMP.pdf - Google Drive

Bartik, T. J. (1991). Who Benefits from State and Local Economic Development Policies? Brookings Institution Press.

Bekaert, G., Hoerova, M., & Duca, M. L. (2013). Risk, Uncertainty, and Monetary Policy. Journal of Monetary Economics, 60(7), 771-788.

Beers, D., de Bolle, M., Kletzer, K., & Panizza, U. (2023). BoC-BoE Sovereign Default Database: Methodology and Summary Statistics. Bank of Canada & Bank of England Working Paper Series.

Bird, G., & Rowlands, D. (2001). IMF Lending: How Is It Affected by Economic, Political, and Institutional Factors? Journal of Policy Reform, 4(3), 243-270.

Bird, G., Hussain, M., & Joyce, J. P. (2004). Many Happy Returns? Recidivism and the IMF. Journal of Development Studies, 40(6), 30-52.

Blomström, M., & Kokko, A. (2003). The Economics of Foreign Direct Investment Incentives. NBER Working Paper, No. 9489.

Bolton, P., & Jeanne, O. (2009). Structuring and Restructuring Sovereign Debt: The Role of Seniority. Review of Economic Studies, 76(3), 879-902.

Boz, E. (2011). Sovereign default, private sector creditors, and the IFIs. Journal of International Economics, 83(1), 70-82.

Broner, F., Erce, A., Martin, A., & Ventura, J. (2014). Sovereign debt markets in turbulent times: Creditor discrimination and crowding-out effects. Journal of Monetary Economics, 61, 114-142. Bulow, J., &

Rogoff, K. (1989). Sovereign Debt: Is to Forgive to Forget? American Economic Review, 79(1), 43-50.

Calvo, G. A. (1998). Capital flows and capital-market crises: the simple economics of sudden stops. Journal of applied Economics, 1(1), 35-54. Çufadar, A., & Özatay, F. (2017). The Role of Public Debt Composition on Default Probability. Central Bank of Turkey Working Papers.

Copelovitch, M. S. (2010). The International Monetary Fund in the Global Economy: Banks, Bonds, and Bailouts. Cambridge University Press.


Corsetti, G., Guimaraes, B., & Roubini, N. (2006). International lending of last resort and moral hazard: A model of IMF's catalytic finance. Journal of Monetary Economics, 53(3), 441-471.

Dell'Erba, S., Hausmann, R., & Panizza, U. (2013). Debt levels, debt composition, and sovereign spreads in emerging and advanced economies. Oxford Review of Economic Policy, 29(3), 518-547.

Hausmann, R., & Panizza, U. (2013). Debt Levels, Debt Composition, and Sovereign Spreads in Emerging Markets. Oxford Review of Economic Policy, 29(3), 543-566.

Kambou, Sansan Vincent De Paul, 2025. "Debt relief instruments and external debt dynamics following natural disasters in developing countries," International Economics, Elsevier, vol. 184(C).

Diamond, D. W., & Rajan, R. G. (2001). Banks, Short-Term Debt and Financial Crises: Theory, Policy Implications and Applications. Carnegie-Rochester Conference Series on Public Policy, 54(1), 37-71.

Dreher, A., & Gassebner, M. (2012). Do IMF Programs Speed Up Recovery from Financial Crises? Kyklos, 65(4), 503-526.

Easterly, W. (2005). What Did Structural Adjustment Adjust? The Association of Policies and Growth with Repeated IMF and World Bank Adjustment Loans. Journal of Development Economics, 76(1), 1-22.

Eaton, J., & Gersovitz, M. (1981). Debt with Potential Repudiation: Theoretical and Empirical Analysis. Review of Economic Studies, 48(2), 289-309

Edwards, S. (1986). The Pricing of Bonds and Bank Loans in International Markets: An Empirical Analysis of Developing Countries' Foreign Borrowing. European Economic Review, 30(3), 565-589.

Fischer, S. (1999). On the Need for an International Lender of Last Resort. Journal of Economic Perspectives, 13(4), 85-104.

Fuchs, A., & Gehring, K. (2017). The Home Bias in Sovereign Ratings. Journal of International Money and Finance, 77, 1-22.

Gelpern, A. (2004). Building a better seating chart for sovereign restructurings. Emory LJ, 53, 1115.

Gelpern, A., Horn, S., Morris, S., Parks, B., & Trebesch, C. (2023). How China lends: A rare look into 100 debt contracts with foreign governments. Economic Policy, 38(114), 345-416.

Gennaioli, N., Martin, A., & Rossi, S. (2014). Sovereign default, domestic banks, and financial institutions. The Journal of Finance, 69(2), 819-866.

Gehring, K., & Lang, V. (2020). Stigma or cushion? IMF programs and sovereign creditworthiness. Journal of Development Economics, 146, 102507.


Horn, S., Reinhart, C. M., & Trebesch, C. (2021). China's overseas lending. Journal of International Economics, 133, 103539.


IMF (2015). The IMF's Lending Framework and Sovereign Debt—Further Considerations. IMF Policy Paper.

IMF (2022). Reviews of the Fund's Sovereign Arrears Policies and Perimeter. IMF Policy Paper.

Jeanne, O., & Zettelmeyer, J. (2001). International Bailouts, Moral Hazard, and Conditionality. Economic Policy, 16(33), 409-432.

Jordà, Ó. (2005). Estimation and Inference of Impulse Responses by Local Projections. American Economic Review, 95(1), 161-182.

Jorra, M. (2012). The Effect of IMF Lending on the Probability of Sovereign Debt Crises. Journal of International Money and Finance, 31(4), 709-725.

Laeven, L., & Valencia, F. (2012). Systemic Banking Crises Database: An Update. IMF Working Paper, WP/12/163.

Laeven, L., & Valencia, F. (2020). Systemic Banking Crises Revisited. IMF Working Paper, WP/2020/133.

Lang, V. (2021). The economics of the democratic deficit: The effect of IMF programs on inequality. The Review of International Organizations, 16(3), 599-623.

Marchesi, S., & Thomas, J. P. (1999). IMF Conditionality as a Screening Device. Economic Journal, 109(454), 111-125.

Nelson, S. C. (2014). The Currency of Confidence: How Economic Beliefs Shape the IMF's Relationship with Its Borrowers. Cornell University Press.

North, D. C. (1990). Institutions, Institutional Change and Economic Performance. Cambridge University Press.


Obstfeld, M., Shambaugh, J. C., & Taylor, A. M. (2010). Financial Stability, the Trilemma, and International Reserves. American Economic Journal: Macroeconomics, 2(2), 57-94.

Panizza, U., Sturzenegger, F., & Zettelmeyer, J. (2009). The Economics and Law of Sovereign Debt and Default. Journal of Economic Literature, 47(3), 651-698.

Reinhart, C. M., & Rogoff, K. S. (2011). This Time Is Different: Eight Centuries of Financial Folly. Princeton University Press.

Rodrik, D., & Velasco, A. (1999). Short-Term Capital Flows. Annual World Bank Conference on Development Economics, 1999, 59-90.

Roubini, N., & Setser, B. (2003). The US as a Net Debtor: The Sustainability of the US External Imbalances. Journal of Economic Perspectives, 17(4), 177-198.


Schlegl, M., Trebesch, C., & Wright, M. L. J. (2019). The Seniority Structure of Sovereign Debt. NBER Working Paper, No. 25793.

Sinha, P. (2015). Government Debt and Economic Growth: Decomposing the Cause and Effect Relationship. Journal of Economic Policy Reform, 18(1), 17-37.

Steinkamp, S., & Westermann, F. (2014). The Role of Creditor Seniority in Europe’s Sovereign Debt Crisis. Economic Policy, 29(79), 495-552.

Steinkamp, S., & Westermann, F. (2017). Multilateral loans and interest rates: further evidence on the seniority conundrum. International Journal of Finance & Economics, 22(2), 169-178.

Stock, J. H., & Yogo, M. (2005). Testing for Weak Instruments in Linear IV Regression. In Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg (pp. 80-108). Cambridge University Press.

Stone, R. W. (2002). Lending Credibility: The International Monetary Fund and the Post-Communist Transition. Princeton University Press.

Thacker, S. C. (1999). The High Politics of IMF Lending. World Politics, 52(1), 38-75.

Tirole, J. (2002). Financial Crises, Liquidity, and the International Monetary System. Princeton University Press.

Trebesch, C., & Zabel, M. (2017). The Output Costs of Hard and Soft Sovereign Default. European Economic Review, 92, 416-432.

Trebesch, C. (2019). The Lender of Last Resort: IMF Programs and Sovereign Borrowing. NBER Working Paper, No. 26091


## PUBLICATIONS
