# 0005-OECD_MNE-Responses-to-the-Global-Minimum-Tax_52c08ab9

This work is issued under the responsibility of the Secretary-General of the OECD and does not necessarily reflect the official views of OECD Member countries.


## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Abstract

The Global Minimum Tax (GMT), implemented in 2024, represents a significant change in the international tax system. This paper uses a difference-in-differences framework to assess the short-term impact of the GMT, including on effective tax rates, investment and employment. Based on group-level Orbis data, the analysis finds that in the first year after the introduction of the GMT, relatively low-taxed MNEs experienced a statistically significant increase in their effective tax rates of 1.7 percentage points. The increase for all firms is 1.4 percentage points. However, this increase was not accompanied by a reduction in investment or employment. The analysis indicates no anticipatory responses. Heterogeneity analyses suggest that the effects on effective tax rates are driven by MNEs which were more likely to have engaged in tax planning and MNEs with higher profit-to-substance ratios. The point estimates in terms of ETRs suggest that the GMT resulted in an increase of EUR 79bn-109bn in tax revenue globally in the first year of its implementation, equivalent to 2.4-3.4% of global corporate income tax revenue.

# Acknowledgements

This paper was carried out under the supervision of Kurt Van Dender and Pierce O'Reilly. The authors would like to thank the delegates of the OECD Working Party No. 2 on Tax Policy Analysis and Tax Statistics for their valuable comments and insights. This paper has greatly benefited from the thoughtful feedback provided by Saskia Kohlhase, and by Dirk Schindler. The authors would also like to thank Laura Arnemann, Clara Gascon, and Ana-Cinta González Cabral from the OECD's Centre for Tax Policy and Administration, Valentine Millot and Sébastien Turban from the OECD Economics Department as well as participants of the 2025 NTA Conference, and the OECD Applied Economics Work-in-Progress Seminar for all the comments and feedback provided. The authors also thank Tabea Kreuziger and Yunis Griebenow for excellent research assistance. Finally, the authors are grateful to Karena Garnier, Carrie Tyler, and Alexandra Le Cam for their excellent editorial and administrative support.

## Table of contents

Abstract 3
Acknowledgements 4
Executive summary 7
1 Introduction 9
2 Institutional setting 11
2.1 Overview of the GloBE rules 11
2.2 Timeline of GMT introduction 13
3 Expected impacts 14
4 Data and methodology 17
4.1 Empirical strategy 17
4.2 Data and sample description 20
5 Results 22
5.1 Effects of the GMT on consolidated ETRs 22
5.2 Effects of the GMT on investment and employment 24
5.3 Robustness and placebo tests 26
5.4 Heterogeneity 29
5.5 Additional margins of response 31
6 Estimation of increased tax revenue 33
7 Conclusions 35
References 36
Annex A. Additional figures and tables 40
FIGURES
Figure 1. Top-up tax calculation 12
Figure 2. GMT rule order 12

Figure 3. Timeline of GMT implementation 13
Figure 4. Definition of the treatment and control group across the revenue distribution 18
Figure 5. Raw means and treatment effect for ETRs 23
Figure 6. Treatment effects for taxation and pre-tax profit 24
Figure 7. Raw means and treatment effect for investment and employment 25
Figure 8. Treatment effects on subsidiary counts 32

Figure A A.1. Distribution of consolidated ETRs of MNEs 40
Figure A A.2. Assignment into treatment and control 40
Figure A A.3. Distribution of treatment and control across industries and HQ jurisdictions 41
Figure A A.4. Treatment effect for investment in intangibles 42

## TABLES

Table 1. Possible effects of the GMT 15
Table 2. Descriptive statistics 21
Table 3. Baseline regression results 23
Table 4. Robustness checks - ETRs 28
Table 5. Placebo tests – ETR 28
Table 6. Heterogeneity estimates – ETRs 30
Table 7. Heterogeneity estimates – ETRs impact decomposition by Size and IIR status 31
Table 8. Estimates of global tax revenue impacts of the GMT 34

Table A A.1. Additional regression results 43
Table A A.2. Robustness checks – Investment and employment 44
Table A A.3. Placebo tests – Investment and employment 45
Table A A.4. Heterogeneity estimates – Investment and employment 45
Table A A.5. Heterogeneity estimates – Size and IIR status – Investment and employment 46

# Executive summary

This paper provides an early empirical, ex-post assessment of how multinational enterprises (MNEs) have responded to the announcement and introduction of the Global Minimum Tax (GMT). This fundamental change in international taxation was agreed in 2021 by around 140 jurisdictions through the OECD/G20 Inclusive Framework with implementation starting in 2024. The GMT ensures that large multinational enterprises (MNEs) with revenues above EUR 750m face an effective tax rate (ETR) of at least $15\%$ in every jurisdiction where they operate. Although the GMT's potential effects on MNE behaviour have been widely debated, evidence to date has largely been based on ex-ante projections.

This paper analyses the realised responses of MNEs after the implementation of the GMT using published financial data and exploiting the EUR 750m threshold to identify causal effects. Specifically, the paper uses group-level financial and ownership data from the Orbis database and implements a difference-in-differences strategy that compares MNEs just above and below the scope-defining revenue threshold. The paper evaluates whether the GMT has affected MNE effective tax rates (ETRs), investment, and employment, and whether firms adjusted their behaviour in anticipation of the reform. In doing so, the paper substantially extends the existing academic literature on the effects of the GMT and the investment effects of corporate taxation more broadly. The findings can inform future international tax policy and contribute to ongoing analyses of the GMT.

Key results are as follows:

\- The implementation of the GMT resulted in a statistically significant rise in consolidated ETRs among in-scope MNEs. The analysis finds an increase of between 1 and 2 percentage points. Previously low-taxed MNEs are estimated to experience an increase in consolidated ETRs of around 1.7 percentage points. For all in-scope MNEs, the estimate is an increase of 1.4 percentage points. This increase appears to be driven by higher tax payments rather than reductions in profits.

\- The impact of the GMT appears to be stronger for MNEs potentially more exposed to top-up taxation. The increase in ETRs is concentrated in MNEs operating in sectors with higher tax-planning intensity, in MNEs with high intangible asset shares, and in MNEs with comparably high profit-to-substance ratios.

\- The paper finds no evidence that the GMT has significantly reduced investment or employment at the MNE group level, or that firms changed their behaviour in anticipation of the reform during the years 2022–2023 (when details of the reform were available, but the rules had not taken effect). The absence of short-run real-economic effects is consistent with several potential explanations, including the design of the GMT's substance-based carveout, which may limit its effect on marginal tax rates.

\- The GMT is estimated to have increased corporate income tax (CIT) revenues by a similar order of magnitude than ex-ante estimates, though by less than forecast. The paper provides an assessment of additional global corporate tax revenue generated by the GMT based on the estimates of the increases in MNE ETRs. Applying the measured effective tax-rate increase to global profits of large MNE groups suggests that the GMT raised EUR 79-109bn in additional revenue in 2024, equivalent to an increase of 2.4-3.4% of global corporate income tax. These short-term estimates are somewhat lower than ex-ante estimates of the longer-run revenue effects reported in Hugger et al. (2024[1]), while being of a similar order of magnitude.

\- The results in the paper are based on early data and are likely to change in subsequent years, and so should be considered with caution. The GMT's revenue effects are likely to evolve as jurisdictions complete their implementation of the rules, as the substance-based carveout is gradually reduced, and as the UTPR as well as the Side-by-Side agreement become fully operational. The results should also be interpreted in light of the limitations of the data used. The effects described represent short-run effects and MNEs might adjust their behaviour only gradually over time. Additionally, the paper focuses on group-level effects. Although in-scope MNEs do not appear to have changed their total investment in response to the GMT, they could have reshuffled their activities across jurisdictions. Complementary analysis using jurisdiction-level data will therefore be important to determine the extent of such reallocation responses.

## 1 Introduction

The Global Minimum Tax (GMT) constitutes a fundamental change in international corporate taxation. The reform was agreed by around 140 member jurisdictions of the Inclusive Framework on BEPS in October 2021 (OECD, 2021[2]). The GMT is designed to ensure that large MNEs with revenues above EUR 750m are subject to a $15\%$ effective minimum tax rate on their excess profits regardless of where they operate. After the announcement of the reform and the publication of the associated model rules in late 2021, implementation of the GMT began in January 2024. Over 50 jurisdictions have enacted or drafted legislation to adopt the GMT as of early 2025. Given the significant changes in the taxation of large MNEs introduced through the GMT, its impact has been intensely debated. $^{1}$


This is the first paper to estimate the realised responses of MNEs to the announcement and implementation of the GMT. The unprecedented nature of the GMT reform, which transforms the tax treatment of MNEs globally through a multilateral approach, makes understanding its impacts of first-order policy importance. The paper provides an early assessment of the impact of the GMT and can support the evidence base on the reform of international corporate taxation. In addition, the paper contributes to the literature on the real impacts of taxation on business investment. Papers in this literature have traditionally focused on country-level CIT reforms (Chodorow-Reich, Zidar and Zwick, 2024[3]; Desai, Goolsbee and Hassett, 2004[4]; Zwick and Mahon, 2017[5]; Harju, Koivisto and Matikka, 2022[6]), leaving open the possibility of MNEs shifting profit across borders to avoid the effects of unilateral tax changes. Some more recent papers have considered spillovers of CIT reforms on MNE activities in other jurisdictions (Hanappi, Millot and Turban, 2023[7]; Hanappi and Whyman, 2023[8]; De Vito et al., 2023[9]), while others have considered the impact of the international tax environment on the location of profits and assets (Keen, Liu and Pallan, 2023[10]; Chodorow-Reich et al., 2024[11]; Bilicka, Devereux and Güçeri, 2024[12]). This paper provides the first assessment of group-level impacts on MNE investment where a major tax reform was multilaterally co-ordinated and likely to apply to most MNE activities globally.

The paper also contributes to the large literature on GMT impacts which has so far focused on ex-ante estimates. Most of these empirical studies focus on the effects on corporate tax revenue (Devereux et al., 2020[13]; Barake et al., 2021[14]; IMF, 2023[15]; Joint Committee on Taxation, 2023[16]; Hugger et al., 2024[1]). However, these estimates have to rely on extrapolations of pre-implementation data and are subject to considerable uncertainty regarding the extent of jurisdictions' implementation and MNE behavioural responses such as changes in profit shifting patterns. This paper presents first estimates of additional tax revenue from the GMT using post-implementation data. Additional theoretical papers also study revenue impacts and their distribution across country groups (Janeba and Schjelderup, 2023[17]; Haufler, Okoshi and Schindler, 2025[18]). Others study the potential MNE responses to the GMT such as expected reductions in profit shifting (Johannesen, 2022[19]; Ferrari et al., 2023[20]; Bratta, Santomartino and Acciari, 2024[21]; Fuest et al., 2025[22]). Several papers investigate how the GMT might impact investment (OECD, 2020[23]; UNCTAD, 2022[24]), with some highlighting the potential positive impacts on investment outside of low tax jurisdictions (Keen, Liu and Pallan, 2023[10]), and others focusing on the potential negative impact on investment, especially for intangible intensive firms (Bilicka, Devereux and Güçeri, 2024[12]). This paper offers the first ex-post analysis of GMT effects on ETRs at the group-level, as well as group-level investment and employment. There also exist studies that focus on potential responses of tax jurisdictions, with some papers pointing to the increased space for jurisdictions to raise tax rates due to reduced tax competition (Hebous and Keen, 2022[25]), and others stressing the incentives for jurisdictions to implement Qualified Domestic Minimum Top-up Taxes (QDMTTs) (Devereux, 2023[26]). Although not the direct focus of this paper, the analysis nonetheless captures indirectly the impacts of such jurisdiction-level changes on MNE ETRs.

The rest of the paper proceeds as follows. It begins with a description of the institutional setting in Section 2, followed by a discussion of possible responses to the GMT based on the existing literature in Section 3. Section 4 provides a description of the data used for the analysis and the empirical methodology. Section 5 describes the main results, as well as heterogeneity and robustness checks. In Section 6, the estimation results are applied to provide a first estimate of the revenue impacts of the reform. Section 7 concludes.

## 2 Institutional setting

The GMT introduces a system of top-up taxes to ensure a minimum level of effective taxation for large MNEs. The GMT is governed by the Global Anti-Base Erosion (GloBE) Rules. The GloBE rules were agreed in October 2021 by around 140 jurisdictions which make up the OECD/G20 Inclusive Framework on Base Erosion and Profit Shifting. While the participating jurisdictions are not obliged to implement the rules, they commit to consistent application of the rules if they choose to do so and accept the application of the rules by other members. The GloBE rules establish a coordinated system of minimum taxation that ensures that large MNE groups are subject to a minimum ETR of at least 15% on their excess profits in every jurisdiction in which they operate. Excess profits are defined as those profits exceeding a profitability threshold defined over assets and payroll. The rules are set out in detail in OECD (2021[27]), complemented by a Commentary and Administrative Guidance that has been updated several times (OECD, 2022[28]). An update in early 2026 introduced simplifications and permanent safe harbours which will be incorporated into the Commentary to the GloBE Model Rules (OECD, 2026[29]). This section provides a high-level overview of the GloBE Rules as of July 2026 focusing on the scope of the rules, the calculation of the top-up taxes, and the rule order in collecting top-up taxes. The section also summarises the timeline leading to the implementation of the GMT starting in 2024, with a view to informing the identification of the potential effects of the GMT in this paper.

## 2.1 Overview of the GloBE rules

The GMT applies to MNE groups with annual revenues of EUR 750m or more, with certain exclusions. Companies with more than EUR 750m in revenues in two of the four preceding years and with at least one foreign subsidiary are generally in scope of the GMT. There exists a small number of exclusions including for Governmental Entities, International Organisations, Non-profit Organisations, Pension Funds, and MNE groups in the initial phase of their international activity. Additional exclusions apply to income from international shipping activities as well as for Investment Funds and Real Estate Investment Vehicles if they are the Ultimate Parent Entity (UPE) of the MNE group. Commencing in 2026, MNE Groups subject to the Side-by-Side Safe Harbour discussed below are also excluded from certain parts of the system.

The GMT applies top-up taxes based on ETRs calculated at the level of MNE subgroups, comprising all entities of the MNE group located in a jurisdiction. Where an in-scope MNE profit is subject to an ETR below the 15% rate in any jurisdiction where it is operating, a top-up tax equal to the difference between the 15% rate and the ETR in the jurisdiction can be levied (see Figure 1). Since tax bases differ across jurisdictions, the GloBE rules rely on financial accounts to build a consistent approach to calculating the ETR for each MNE subgroup. This “GloBE ETR” is computed by dividing all covered taxes of entities located in the jurisdiction by their total GloBE Income. Covered taxes are based on annual tax expense of all entities in a subgroup of in-scope MNEs. Similarly, GloBE Income combines all profits and losses of the entities in a subgroup. Both are calculated by applying certain agreed adjustments to the financial accounting figures to address certain book-tax differences. $^{2}$ Common causes for such adjustments are e.g. prior-period losses, provisions that allow for accelerated (tax) depreciation, or certain tax incentives that qualify for preferential treatment under the GloBE rules. In addition, the tax base is reduced by the Substance-Based Income Exclusion (SBIE), which excludes a ‘routine’ return from top-up taxation. The SBIE is based on the amount of tangible assets and payroll reported in a jurisdiction. After a transitional period, the SBIE equals the sum of 5% of the value of tangible assets and 5% of the value of payroll.

Figure 1. Top-up tax calculation

[[KC_IMAGE_001]]

Note: Simplified formula for the calculation of top-up taxes at the subgroup level. Source: Hugger et al. (2024[1])

Top-up taxes due under the GMT are distributed across jurisdictions based on an agreed rule order. Figure 2 shows the order of top-up tax collection under the GloBE rules. If top-up tax is levied on the profit an MNE reports in a jurisdiction, that jurisdiction can itself collect the top-up tax in priority to other jurisdictions, by implementing a Qualified Domestic Minimum Top-up Tax (QDMTT, Panel 1 of the Figure). Any top-up tax remaining after the application of QDMTTs can be collected by the UPE jurisdiction under the Income Inclusion Rule (IIR, Panel 2). If the IIR has not been implemented by the UPE jurisdiction, top-up taxes can also be collected under the IIR by an intermediate parent entity (IPE, Panel 3). Finally, if any top-up tax remains, it can be imposed by multiple jurisdictions under the UTPR (Panel 4), a backstop ensuring that all low-taxed income is captured under the GMT. Each jurisdiction which has adopted the UTPR can collect top-up tax in proportion to the amount of substance of the MNE group in the jurisdiction, where substance is measured by tangible assets and employees at equal weights. These interlocking rules mean that the top-up tax collected by a given jurisdiction depends on the actions of other jurisdictions.

The Side-by-Side package agreed in 2026 adds different treatment of MNEs headquartered in jurisdictions with tax regimes already incorporating a system of minimum taxation. These pre-existing systems need to achieve similar outcomes as the GMT. MNEs falling under the Side-by-Side Safe Harbour are not subject to the IIR or UTPR. Where subsidiaries are located in QDMTT jurisdictions, however, MNEs falling under the Safe Harbour will still be subject to those QDMTTs. This treatment commences in 2026. As of January 2026, the only jurisdiction with a tax regime qualifying for this safe harbour is the United States which have benefited from a temporary safe-harbour before the agreement on the Side-by-Side package. This implies that the GMT only changes the taxation of US MNEs compared to a pre-GMT situation to the extent that subgroups of these MNEs operate in jurisdictions that have implemented a QDMTT.

Figure 2. GMT rule order

[[KC_IMAGE_002]]

Note: QDMTT stands for Qualified Domestic Minimum Top-Up Tax. IIR stands for the Income Inclusion Rule. UPE stands for Ultimate Parent Entity. IPE stands for Intermediate Parent Entity and CE stands for Constituent Entity.
Source: OECD (2023[30])

## 2.2 Timeline of GMT introduction

The GMT was introduced as part of the discussions on a Two Pillar Solution to Address the Tax Challenges of the Digital Economy, under the auspices of the OECD/G20 Inclusive Framework on Base Erosion and Profit Shifting (BEPS). Key steps towards the announcement and implementation of the GMT are summarised in Figure 3. The BEPS project was initiated in 2013 to address the erosion of corporate tax bases through corporate tax avoidance and evasion. The Final Reports published in 2015 listed 15 Actions that aimed to reduce tax avoidance opportunities of multinational companies. $^{3}$ In 2016, the Inclusive Framework on BEPS was established inviting all jurisdictions to participate and further develop the work on BEPS.

Discussion on a global minimum tax began as part of a second phase of the work of the Inclusive Framework. The minimum tax was proposed as part of a process to develop a Two Pillar Solution to Address the Tax Challenges of the Digital Economy. A first discussion paper from 2019 included suggestions about potential revenue-based scoping thresholds with a blueprint report providing additional detail (OECD, 2020[31]). In October 2021, the Inclusive Framework on BEPS formally approved an international tax agreement stemming from these negotiations (OECD, 2021[2]). This outcome statement outlined the design of the GloBE rules which implement the GMT, including the revenue threshold of EUR 750m used for identification in this paper. This was followed by the publication of more detailed model rules two months later. This credible announcement of the GMT is used in this paper to test for announcement responses starting in 2022. A key first step towards the implementation of the GMT was the approval of the Council Directive (EU) 2022/2523 in December 2022 which formalised the implementation in the EU member states. The directive introduced the GloBE rules for fiscal years starting in or after January 2024. Similar steps were taken by several other large economies. Some jurisdictions also chose to only implement parts of the GloBE rules, such as the QDMTT. As of today, more than 50 jurisdictions have taken steps towards implementation of the GMT. Given its design, the implementation in the EU and many other large economies including Australia, Canada, Japan, Korea and the UK, as well as several major investment hubs imply that a high share of large MNEs will be subject to the GMT. $^{4}$

Figure 3. Timeline of GMT implementation

[[KC_IMAGE_003]]

Note: High-level summary of selected milestones towards the implementation of the Global Minimum Tax.

## 3 Expected impacts

The proposed empirical approach first estimates whether the GMT increased the ETRs of affected MNEs and proceeds to estimate changes in other outcomes as a second step. This reflects the expectation that increases in corporate tax rates are necessary for other MNEs responses to be observed. A number of existing papers have predicted that the GMT would have a quantitatively significant impact on tax revenues or ETRs of MNEs based on ex-ante analysis (Devereux et al., 2020[13]; Barake et al., 2021[14]; IMF, 2023[15]; Joint Committee on Taxation, 2023[16]; Hugger et al., 2024[1]; Janeba and Schjelderup, 2023[17]). However, given the uncertainty surrounding these ex-ante estimates, the estimation of the impact on MNE ETRs in the first year following GMT implementation is an important test of whether the predictions have been borne out in practice.

The ETR in this paper is a backward-looking measure of the effective average tax rates. It is measured as the ratio of reported taxes at the consolidated level in a given fiscal year to the corresponding measure of pre-tax profit. Although many papers focus on forward-looking effective marginal or average tax rates as being relevant to firm investment decisions, such forward-looking rates are difficult to measure at the MNE group level (see e.g., Devereux and Griffith (2003[32]) for an early contribution). In addition, companies in practice often rely on measures such as average book-ETRs as a heuristic to also evaluate incremental investment decisions according to survey-based evidence (Graham et al., 2017[33]). This implies that the backward-looking ETR used in this paper is likely to be a good proxy for the tax rates relevant for investment decisions.

The academic literature suggests that corporate tax rates may impact investment through two channels. Firstly, the neoclassical model of investment behaviour predicts that corporate tax rates reduce investment by increasing the user cost of capital (Hall and Jorgenson, 1967[34]). Several studies have predicted that the increased rates of taxation associated with the GMT will result in reductions in real investment based on this channel (Keen, Liu and Pallan, 2023[10]). Alternatively, increases in corporate tax rates can reduce investment by tightening companies' financial constraints (Dobbins and Jacob, 2016[35]; Egger, Erhardt and Keuschnigg, 2020[36]). $^{5}$ However, the magnitude of investment responses to top-up taxation may importantly depend on the nature and extent of profit-shifting behaviours of MNEs (Juranek, Schindler and Schneider, 2023[37]; Clifford, Miethe and Semelet, 2025[38]). For instance, if low-tax outcomes are associated with infra-marginal profit-shifting behaviour, investments may not be significantly affected.

An important distinction exists between investment responses measured at the level of the entire MNE group and responses measured at the level of entities of an MNE group in each jurisdiction. Since top-up taxation under the GMT applies based on ETRs measured at the jurisdictional level, a degree of reallocation of investment and employment may be expected within MNE groups. Thus, for example, potentially considerable investment responses may be observed at the level of particularly low-taxed jurisdictions, group-level responses may be much more muted. Some papers have found empirically that certain forms of profit shifting result in investments being reallocated between affiliates across jurisdictions, and do not find that restricting profit-shifting opportunities leads significant changes in investment at the level of MNE groups (de Mooij and Liu, 2020[39]; Knoll et al., 2021[40]). Finally, many of the empirical studies have relied on tax reforms in one jurisdiction, leaving tax rates in other jurisdictions unchanged (Zwick and Mahon, 2017[5]; Maffini, Xing and Devereux, 2019[41]). Given the unprecedented nature of the coordinated change in MNE taxation, the existing literature studying the effects of corporate taxation on investment might not apply in the context of the GMT.

Overall, there are several key scenarios for what may be expected in the first and second estimation steps. These scenarios are summarised in Table 1, separately presenting the expected effects on ETRs, investment and employment.

\- Scenario (a), described in the first row, consists of the GMT not having any impact on MNEs' ETRs and consequently also no change in the other outcome variables. Such a situation may arise if MNEs either have ETRs above the $15\%$ minimum floor in all jurisdictions in which they operate, if they have sufficient substance (in the form of payroll and tangible assets) to protect any low-tax profits under the GMT's substance carveouts (De Simone and Olbert, 2021[42]), or if the intended effect of the GMT is diminished in other ways.

\- Scenario (b), described in the second row of Table 1, consists of the GMT having a positive impact on MNEs' ETRs, but no further impact on the other outcomes. Such a scenario may arise if MNEs' investment and employment decisions are relatively insensitive to top-up taxation under the GMT. This may occur, for instance, if low-tax outcomes are not associated with significant reductions to returns on marginal investments, e.g. because of the substance carveout (Schjelderup and Stähler, 2023[43]; Gschossmann et al., 2025[44]), or if the GMT leads to a costly reduction in profit-shifting activities which, at the margin lead to tax savings which are offset by reduced profit shifting costs (Juranek, Schindler and Schneider, 2023[37]), leaving overall incentives unchanged.

\- Scenario (c) would occur if an increase in ETRs would be associated with a reduction in investment or employment, in line with a model in which the GMT increases the user cost of capital or increases firms' financial constraints.

\- Finally, under Scenario (d), firms may attempt to protect low-tax profits by taking advantage of the substance carveout under the GMT which could act as a production subsidy in some circumstances (Schjelderup and Stähler, 2023[43]). In this case, a relatively smaller or null ETR response may be expected but associated with an increase in tangible asset investment and employment.

Table 1. Possible effects of the GMT


Note: The table considers three key scenarios of impacts of the GMT on MNE ETRs and economic activity. (+) denotes an anticipated increase in the outcome variable while (-) denotes an anticipated decrease in the outcome variable.


## 4.1 Empirical strategy

This paper uses a difference-in-differences approach to identify the effects of the GMT. As specified in the GloBE rules, only MNE groups with consolidated revenues above EUR 750m are in scope of the GMT (see Section 2). The identification strategy exploits this revenue requirement to assign companies to a treatment and a control group. The difference-in-differences strategy compares the outcomes of companies more likely to be in scope of the GMT (the treatment group) with those of companies less likely to be in scope of the GMT (the control group) to identify the impact of the GMT. Since only multinationals are in scope of the GMT, the approach restricts attention to companies with at least one foreign subsidiary, in line with the definition of an MNE in the GloBE rules.


Figure 4. Definition of the treatment and control group across the revenue distribution

[[KC_IMAGE_004]]


The DiD estimation strategy relies on comparing changes in the outcomes of the two groups over time, while controlling for potential confounding factors. The following model is estimated at the level of MNE i and year t:

$$
Y _ {i t} = \sum_ {\tau = 2 0 1 6} ^ {2 0 2 4} \theta_ {\tau} \mathbf {1} [ t = \tau ] \times T r e a t e d _ {i} + \alpha_ {i} + \mu_ {t} + X _ {i t} ^ {\prime} \delta + \varepsilon_ {i t}\tag{1}
$$

where $Treated_{i}$ is a dummy equal to one if MNE i is assigned to the treatment group. The coefficients $\theta_{\tau}$ measure the change in the outcome variable $Y_{it}$ for treated companies relative to companies in the control group in year $\tau$ . The coefficient for the year 2018 is normalised to zero. A number of additional variables control for potential confounding factors. Company fixed effects indicated by $\alpha_{i}$ control for time-invariant differences across companies. Year fixed effects ( $\mu_{t}$ ) are included to control for time trends or shocks that affect all companies in the sample similarly. The vector $X_{it}$ comprises a set of additional control variables, including industry-year fixed effects to account for industry-specific time trends, interaction terms between dummies for the accounting practice of the company and the different sample years to account for some potentially relevant changes in accounting rules applicable to some companies within the sample period, and GDP growth in the companies' headquarter jurisdiction to control for the impact of the economic cycle. $^{7}$ Standard errors in the regressions are clustered at the MNE level.

The regression design can identify both potential announcement effects and implementation effects of the GMT. Announcement effects would be measured through statistically significant differences in the development of the treatment and control group captured via the coefficients $\theta_{2022}$ and $\theta_{2023}$ .⁸ Effects of the implementation of the GMT would be captured by the coefficient $\theta_{2024}$ .

The main outcome variables for which the effect of the GMT is estimated are the consolidated ETRs, investment, and employment growth of in-scope MNEs. The first outcome variable considered is the consolidated ETR. It is calculated as tax expense divided by pre-tax profits at the level of the MNE group. The variable therefore measures the average tax burden of an MNE, regardless of where profits are reported, or where taxes are paid. ETRs are only calculated for companies with positive profits, to avoid issues in the interpretation of negative ETRs. Observations with negative tax expense are generally included in the sample, but the dependent variables are all winsorised at the 5 $^{th}$ and 95 $^{th}$ percentile to reduce the impact of outliers. A second set of outcome variables assess the effect of the GMT on investment and employment growth. The dependent variables used in these DiD estimations are the log-change in tangible fixed assets to measure investment effects, and the log change in employment to capture effects of the GMT on employment.

A second model is estimated to summarise the average effects of the announcement and implementation of the GMT on treated companies. This second DiD model is specified as follows:

$$
Y _ {i t} = \alpha_ {i} + \mu_ {t} + \theta^ {A} P o s t A n n o u n c e m e n t _ {t} \times T r e a t e d _ {i}
$$

$$
+ \theta^ {I} P o s t I m p l e m e n t a t i o n _ {t} \times T r e a t e d _ {i} + X _ {i t} ^ {\prime} \delta + \varepsilon_ {i t}\tag{2}
$$


The main identifying assumption behind the DiD estimation strategy is that the outcomes of companies in the treatment and control groups would have followed the same trends in the absence of the introduction of the GMT. The main threat to this strategy is either differential underlying trends between the two groups or time-varying shocks which coincide with the GMT. To validate the strategy, several checks are presented. Firstly, a potential concern might be that the introduction of Country-by-Country reporting (CbCR), introduced starting in 2016, relied on a similar revenue threshold as the GMT. $^{9}$ This reform may have led to certain firms choosing to bunch below the threshold at least in some years as documented by Hugger (2024 $[46]$ ). As discussed above, the GMT analysis in this paper excludes companies with revenues close to the threshold of EUR 750m where selection around the threshold is most likely. Specifically, the ‘donut hole’ between EUR 650m and EUR 800m covers the main bunching region identified in Hugger (2024 $[46]$ ). Additionally, non-random assignment into the treatment and control groups threatens the identification strategy only if it would have generated different trends in the absence of the GMT. The paper therefore tests for parallel trends in the period prior to the announcement of the GMT (see Sections 5.1-5.2). In addition, placebo tests are presented, comparing results using the DiD strategy for groups of firms which are either not in-scope of the GMT (non-MNEs), for firms which are much less likely to be affected (firms with higher ETRs), and for placebo treatment years (2020 and 2021, see Section 5.3). All of these tests serve to validate the DiD.

## 4.2 Data and sample description

The main dataset used for the analysis draws on consolidated financial statements taken from the Orbis database. This data includes all key financials used in the analysis, such as pre-tax profits, tax expense, the number of employees, or the stock of tangible fixed assets and reflects consolidated totals for the MNE groups in the sample. The financial information is paired with historic information on ownership links to construct MNE owner-subsidiary networks on an annual basis. The information on company networks is used to identify multinationals via the existence of foreign subsidiaries, and to identify corporate ultimate owners for each MNE group within a given year. Only observations at the ultimate owner level are retained in the dataset since the unit of observation is the full MNE group. The coverage of parent-subsidiary relationships includes links to subsidiaries located in investment hubs and other jurisdictions where unconsolidated financial data is often not available. This information on parent-subsidiary links as well as the consolidated financials used in this paper are generally regarded as high quality (see e.g. Bachas et al. (2023[47]) and Olbert, Spengel and Weck (2024[48])). $^{10}$ Information on the accounting standard used for each financial report and the industry classification of each company are also taken from Orbis. Annual GDP growth rates are compiled from OECD, IMF and World Bank databases.

To ensure that the assignment of MNEs to treatment and control groups accurately captures exposure to the GMT, the sample is restricted in several ways. First, the baseline sample is restricted to non-financial corporate entities, since the revenues listed in the balance sheets of banks and other financial companies do not necessarily align with the revenue definition relevant for the GloBE rules. $^{11}$ Second, companies from the shipping sector are excluded, to account for the International Shipping Income exclusion in the GloBE rules. Finally, the GMT applies top-up taxes to companies that have profits taxed at rates below 15% at jurisdiction-level MNE subgroups. Since this paper relies on aggregated data, low-taxed profit cannot be identified at the subgroup level. To overcome this limitation, the baseline sample focuses on companies with below-median consolidated ETRs as such companies are more likely to also have some low-taxed profit in their constituent subgroups compared to companies with higher average ETRs. In an alternative estimate, we also include MNEs with high consolidated ETRs. While these are less likely to be affected by the GMT, these MNEs could still be subject to top-up taxation on operations in individual low-tax jurisdictions since the GMT operates at a jurisdiction-by-jurisdiction basis. Figure A A.1. in the Annex shows the distribution of ETRs for the relevant MNEs.


Table 2. Descriptive statistics


## 5 Results

The section proceeds in steps to analyse the potential announcement and implementation effects of the GMT in line with the methodology outlined in Section 4. Section 5.1 focuses on the effects of the GMT on consolidated ETRs. Any observed changes in these ETRs could in turn be associated with responses in MNEs' total investment and employment, which are estimated in Section 5.2. The robustness of the baseline results reported in Sections 5.1 and 5.2 is tested in Section 5.3. Section 5.4 studies potential heterogeneities in the responses to the GMT across MNEs with different characteristics and Section 5.5 looks at additional potential margins of response related to the structure of in-scope MNEs.

## 5.1 Effects of the GMT on consolidated ETRs

Trends in the raw means of the ETRs provide a first indication of the potential effects of the GMT. Panel A of Figure 5 plots the raw means of MNE-level ETRs from 2016 to 2024, where the black solid line represents the mean of MNEs in the treatment group, and the red dashed line represents the mean of MNEs in the control group in each year. The outcome variable is normalised to zero in 2018. Prior to 2021, the trends of ETRs look entirely parallel between the treatment and control groups. Starting in 2021, there is a slight divergence with ETRs in the treatment group trending somewhat above those in the control group. This divergence, however, becomes substantially larger after the implementation of the GMT in the last year of the sample period.

The corresponding DiD estimates test whether these developments are driven by the announcement or implementation of the GMT or whether they can be attributed to confounding factors. The results for this difference-in-differences estimation are presented in Panel B of Figure 5. The figure plots the coefficients $\theta_{\tau}$ , where $\tau \in (2016, \dots, 2024)$ , from the specification in Equation (1) (see Section 4). The dependent variable is the consolidated ETR. The coefficient estimates are statistically insignificant between 2016 and 2021, supporting the assumption of parallel pre-trends underpinning the estimation strategy. Coefficients also remain insignificant between 2022 and 2023 with point estimates implying no statistically significant announcement response on the consolidated ETRs of in-scope MNEs. In contrast, the coefficient for 2024 is positive and statistically significant at the $1\%$ level, indicating an increase in consolidated ETRs after the implementation of the GMT.

The estimates suggest no announcement effect, but a positive effect of GMT implementation on the ETRs of in-scope MNEs. Table 3 summarises the regression results, with Column (1) showing the coefficient estimates for ETRs following Equation (1). These estimates suggest an increase in consolidated ETRs of around 1.9 ppts post implementation for companies exposed to the GMT compared to companies below the revenue threshold. The DiD estimation based on Equation (2) is reported in Column (4) of Table 3. This specification also suggests no announcement effect (coefficient $\theta^A$ not being significantly different from zero, with a point estimate of -0.002), but a statistically significant positive implementation effect with a point estimate of a 1.7 ppts increase in the ETR compared to the pre-implementation period. This point estimate is equivalent to a $12\%$ increase in the consolidated ETR relative to the pre-reform treated mean.

Figure 5. Raw means and treatment effect for ETRs

[[KC_IMAGE_005]]


[[KC_IMAGE_006]]

Note: Panel A shows raw means of ETRs for the treatment group and control group in each year of the sample period. The definition of the treatment and control group is based on the EUR 750m revenue threshold (see Section 4). Panel B shows the coefficients $\theta_{\tau}$ on $Treated_{i} \times Year_{t}$ for ETRs, as defined in Equation (1). The vertical lines indicate 95 percent confidence intervals for the coefficient estimates. The dashed red lines in both panels indicate the announcement of the GMT in 2021, the solid red lines indicate the implementation of the GMT in 2024. Outcome variables are normalised to zero in 2018.

Table 3. Baseline regression results


Note: Columns (1) to (3) report estimated coefficients $\theta_{\tau}$ where $\tau \in (2016, \ldots, 2024)$ from Equation (1). Columns (4) to (6) report the estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2). The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. All specifications include year and company fixed effects as well as additional controls following Equations (1) and (2). Standard errors are clustered at the company level and are reported in parenthesis.

Additional analysis suggests that the increase in ETRs is driven by higher tax payments, not by a reduction in profit levels. Figure 6 plots DiD estimation results based on Equation (1), where the dependent variables are the log change in tax payments (Panel A), and the log change in pre-tax profits (Panel B). Effectively separating the two components of the ETR helps to disentangle whether the effects of the GMT are driven by changes in the numerator (tax payments) or the denominator (pre-tax profits). The results reported in Figure 6 suggest that the increase in ETRs of in-scope MNEs is caused by a relative

Panel A: Log change taxation

increase in their tax expense in 2024 and not a change in pre-tax profits, since profit levels did not decline in the treatment group relative to the control group. The corresponding coefficients are shown in Columns (1) and (2) of Table A A.1. in the Annex. The magnitude of the estimated log-change in taxation observed is also consistent with the observed change in ETRs. $^{12}$ The estimation results based on Equation (2), reported columns (4) and (5) of Table A A.1., confirm these findings. $^{13}$ The increase in ETRs is in line with Scenarios (b) and (c) in Table 1 which both predict an ETR response. Scenarios (b) and (c) differ, however, in their assumptions regarding potential changes in investment and employment growth. These responses are investigated in the following subsection.

Panel B: Log change pre-tax profits
Figure 6. Treatment effects for taxation and pre-tax profit

[[KC_IMAGE_007]]


[[KC_IMAGE_008]]

Note: The charts show the coefficients $\theta_{\tau}$ on $Treated_{i} \times Year_{t}$ as defined in Equation (1) for the log change in taxation (Panel A) and the log change in pre-tax profits (Panel B). The vertical lines indicate 95 percent confidence intervals for the coefficient estimates. The dashed red lines in both panels indicate the announcement of the GMT in 2021, the solid red lines indicate the implementation of the GMT in 2024. Outcome variables are normalised to zero in 2018. The sample only includes observations which are also used for the regressions estimating ETR impacts.

## 5.2 Effects of the GMT on investment and employment

Changes in the tax burden of companies in scope of the GMT could trigger changes in total investment and employment. The effects of the GMT on the investment and employment growth of in-scope MNEs are again assessed based on the DiD specification presented in Section 4.

The estimations suggest no significant change in investment or employment for in-scope MNEs. The raw means plotted in Panels A and C of Figure 7 for investment and for employment growth suggest similar developments for the treatment and control groups over the sample period. In line with the perception of a low-growth environment in recent years (see e.g., Dlugosch et al. (2025[49]), downward trends in investment and employment growth for both groups can be observed. Investment experienced comparably high volatility in the sample period. Part of this was likely driven by adjustments in IFRS accounting rules which changed the accounting for leased equipment and led to an increase in tangible fixed assets reported by affected companies from 2018 to 2019. $^{14}$ The DiD estimates presented in Panels B (investment) and D (employment growth) for pre-reform years both confirm that the parallel trend assumption for the pre-GMT period holds. For both measures of MNE activity, the estimations also show no statistically significant response to GMT-announcement or implementation. Columns (2) and (3) of Table 3 summarise the coefficient estimates for the individual years. The coefficients for the specification in Equation (2), showing average effects of GMT announcement and implementation compared to the pre-GMT period, are reported in columns (4) and (5). Again, they suggest no announcement or implementation effects. $^{15}$

Figure 7. Raw means and treatment effect for investment and employment
Panel A: Raw means, investment

[[KC_IMAGE_009]]


Panel B: DiD coefficients, investment

[[KC_IMAGE_010]]

Panel D: DiD coefficients, employment growth

Panel C: Raw means, employment growth

[[KC_IMAGE_011]]


[[KC_IMAGE_012]]

Note: Panels A and C show raw means of log changes for tangible fixed assets and employment for the treatment group and control group in each year of the sample period. The definition of the treatment and control group is based on the EUR 750m revenue threshold (see Section 4). Panels B and D show the coefficient $\theta_{\tau}$ on $Treated_{i} \times Year_{t}$ for log changes for tangible fixed assets and employment, as defined in Equation (1). The vertical lines indicate 95 percent confidence intervals for the coefficient estimates. In all panels, the dashed red lines indicate the announcement of the GMT in 2021, the solid red lines indicate the implementation of the GMT in 2024. Outcome variables are normalised to zero in 2018.

Overall, the results presented above are in line with Scenario (b) of Table 1 in Section 3 which predicts a positive impact of the GMT on ETRs with no changes in investment or employment. The estimates presented appear to rule out a short-run investment response to the GMT which might have been expected based on recent estimates of the investment effects of unilateral reforms in the literature.


## 5.3 Robustness and placebo tests

A series of robustness checks support the internal validity of the findings presented above. These exercises test whether the results described are robust to changes in the exact sample used, the set of control variables included, and the definition of the treatment and control group. Results of these robustness checks are summarised in Table 4 for ETRs and Table A A.2. in the Annex for investment and employment growth. They generally validate the results from the baseline estimations.


Second, the results are robust to the inclusion of a series of additional control variables to the baseline model. The inflation rate of the headquarter jurisdiction is used to further proxy for economic uncertainty faced by the MNEs. This variable can also help to mitigate potential effects of exchange rate changes on the euro-denominated outcome variables. To control more directly for potential currency effects, the interaction between a set of dummies for the original reporting currency of the MNE and year dummies is included. Different paths in terms of total profitability or the development of revenues between the treatment and control group could also lead to differences in outcomes over time. To alleviate such concerns, the return on revenues or the log of lagged revenues are tested as additional MNE-level controls. None of these additional controls lead to substantial changes in the results compared to the baseline estimates (see columns (6) to (9) of Table 4 and Table A A.2.).


Table 4. Robustness checks - ETRs


Note: This table presents robustness checks for the estimates of ETR impacts. The different columns report estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2) for a number of alternative samples. Some estimations include additional control variables as indicated in the main text (columns (6)-(9)). The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. The dependent variable is the consolidated ETR at the MNE group level. All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.

Table 5. Placebo tests – ETR


Note: Columns (1) to (3) report the estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2). The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. The dependent variable is the consolidated ETR at the MNE group level. All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.

## 5.4 Heterogeneity

To assess whether the effects documented above vary across different types of firms, the analysis explores heterogeneity along several sectoral and firm-level dimensions. Differences are examined by sectoral indicators of potential tax planning aggressiveness and by a measure of profit-shifting capacity. Heterogeneity is also assessed by the ratio of profits to tangible fixed assets, as a proxy for profits reported relative to economic substance, by firm size, and by the GMT implementation status of the headquarter jurisdiction.

The impact of the GMT on ETRs appears to be strongest among firms in sectors previously identified as more likely to engage in aggressive tax planning practices and to have arguably greater profit-shifting capacity. A heterogeneity analysis of ETR responses based on splitting the sample based on MNE presence in sectors with relatively higher or lower levels of aggressive tax planning intensity is presented in columns (2) and (3) of Table 6. The binary classification of MNEs is based on previous findings about which sectors display the most-aggressive tax practices (Altshuler, Boller and Serrato, 2024[51]). $^{21}$ In-scope firms in sectors with greater propensity for higher tax aggressiveness show an increase of 2.9 ppts in their consolidated ETR following the implementation of the GMT, whereas the effect for firms in a sector with a lower propensity to be tax aggressive is statistically insignificant. Moreover, heterogeneity is also examined by firms' intangible asset intensity. Prior research has identified intangible-intensive firms as having a greater propensity for profit shifting, as intangible assets are relatively mobile and often lack observable market prices, which can ease the allocation of profits across jurisdictions (Delis et al., 2021[52]). Columns (4) and (5) show that in-scope firms in the top quartile of the distribution of the ratio of intangible assets to total assets experience a statistically significant increase of 2.3 ppts in their consolidated ETR following the GMT. However, no statistically significant effects are observed for firms in the bottom quartile. Finally, there does not appear to be a significant heterogeneity in impacts on employment and investment, neither by sector nor by intangible asset intensity, as reported in Table A A.4. in the Annex.

Impacts on ETRs seem to be larger for firms which report more profits relative to an estimated amount of substance. Estimates in columns (6) and (7) of Table 6 show that in-scope firms in the top quartile of the profits-to-tangible-fixed-assets distribution, a proxy for profits relative to economic substance, experience an increase in consolidated ETRs of around 2.9 ppts following implementation, while the corresponding estimate for those in the bottom quartile is not statistically significant. This pattern is consistent with the design of the GMT which targets profits in excess of substance within the top-up tax calculation. As shown in Table A A.2. in the Annex, there are no significant differential effects on investment or employment between firms with higher and lower profit-to-tangibles ratio.

There does not appear to be differential GMT impacts on ETRs by size within the baseline sample. Within the baseline sample, as shown in column (1) of Table 7, MNEs below and above the median revenue of the treatment group exhibit estimated implementation effects of 1.69 and 1.80 ppts, respectively, with no statistically significant difference between the two. Similarly, columns (1) and (3) of Table A A.5. in the Annex suggest no impacts on investment or employment for both larger and smaller MNEs in the treatment group. Column (2) of Table 7 reports results for a sample where MNEs with revenues above EUR 2,000m are included in the sample. The results indicate that larger firms also experience a positive effect on consolidated ETRs of similar size. $^{22}$ Additionally, columns (2) and (5) of Table A A.5. report estimated positive impacts on investment and employment growth for the largest firms, suggestive of potential responses by MNEs seeking to take advantage of the substance-based carve-out under the GMT, thereby protecting low-taxed profits from top-up taxation. This result would be in line with Scenario (d) in Table 1 in Section 3. The results for the largest companies, however, have to be treated with more caution since they rely on comparing control-group companies with companies further away from the revenue threshold reducing the comparability between the two groups. $^{23}$

MNEs subject to IIRs in their headquarter jurisdiction show a stronger ETR response than MNEs headquartered in jurisdictions without an IIR. Most companies not in scope of an IIR are only subject to top-up taxation through QDMTTs in 2024. $^{24}$ This might result in only a fraction of total profit being covered by the GMT, depending on the exact allocation of profits within the individual MNE. $^{25}$ Column (3) of Table 7 presents the estimated coefficients when the treatment group is split into MNEs subject to an IIR and MNEs from headquarter jurisdictions that have not introduced an IIR in 2024. For MNEs subject to an IIR, the estimated treatment effect on the consolidated ETR is 2.9 ppts, so around two-thirds larger than for the full sample. In contrast, MNEs not subject to an IIR show a weaker ETR response, with a point estimate of 1.3 ppts which is only statistically significant at the 10% level.

Table 6. Heterogeneity estimates – ETRs


Note: The different columns report estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2) for a number of alternative sample splits. The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.

Table 7. Heterogeneity estimates – ETRs impact decomposition by Size and IIR status


Note: The different columns report estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2). Column (1) reports coefficients separately for firms split by size relative to the median within the treated group. Column (2) extends the sample by including firms with revenues above EUR 2,000m and reports separate effects for this group. Column (3) reports coefficients separately for firms from headquarter jurisdictions with and without IIR The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.

## 5.5 Additional margins of response

The GMT might not only affect financial outcomes, but also the structure of in-scope MNEs. MNEs in scope of the GMT could, for instance, reduce the number of their subsidiaries to lower organisational complexity and potentially compliance costs. Reduced profit shifting incentives due to top-up taxation could also lead MNEs to reduce their presence in investment hubs.

The analysis conducted in this paper does not find effects of the GMT on MNE structures. Figure 8 summarises the coefficient estimates for outcome variables related to MNE structure, namely the total number of subsidiaries of MNE groups (Panel A) and the number of subsidiaries located in investment hubs (Panel B) recorded in Orbis following Equation (1). For both measures, the coefficient estimates suggest no statistically significant announcement or implementation effect. This is confirmed by additional regression estimates based on Equation (2) which are reported in Table A A.1. The results suggest that in-scope MNEs have not responded to the GMT with a strong restructuring of their subsidiary structure before or immediately after the implementation of the reform. This null result on MNE structures may suggest that these types of adjustments might take time.

Figure 8. Treatment effects on subsidiary counts
Panel A: Log change total number of subsidiaries

[[KC_IMAGE_013]]


Panel B: Log change investment hub subsidiaries

[[KC_IMAGE_014]]

Note: The charts show the coefficients $\theta_{\tau}$ on $Treated_{i} x Year_{t}$ as defined in Equation (1) for the log change in the total number of subsidiaries of an MNE group (Panel A) and the log change in the number of subsidiaries located in investment hubs (Panel B). The vertical lines indicate 95 percent confidence intervals for the coefficient estimates. The dashed red lines in both panels indicate the announcement of the GMT in 2021, the solid red lines indicate the implementation of the GMT in 2024. Outcome variables are normalised to zero in 2018. The definition of investment hubs follows Hugger et al. (2024 $^{[1]}$ ).


# Estimation of increased tax revenue


Using an estimate of total profits for all MNEs with revenues above EUR 750m, the point estimates suggest global tax revenue could have increased in 2024 by EUR 79-109bn, with 95% confidence intervals of EUR 22-187bn. The estimates based on total profits restricted to the baseline estimation sample revenue range are the lowest, at EUR 4bn with a EUR 1-7bn 95% confidence interval. Once the estimated ETR impacts are applied to all MNEs above EUR 750m in revenue in the Orbis data, the estimated increase in tax revenues is EUR 79bn with a EUR 22-136bn 95% confidence interval. Finally, this estimate is applied to the somewhat higher estimate of total in-scope profits based on aggregated CbCRs which is likely to be most closely aligned with the GMT tax base. Using this data source, a tax revenue impact of EUR 109bn is estimated with a EUR 31-187bn 95% confidence interval. These estimates represent an increase of between 2.4% and 3.4% of total global CIT revenue, relative to 2023 values. $^{28}$

Table 8. Estimates of global tax revenue impacts of the GMT


Note: The table shows estimated global tax revenue impacts of the GMT for the year 2024 based on the estimated ETR impacts. The ETR estimates used in the calculations are reported in row 1 (point estimates) and row 2 (the 95% confidence interval). All results are based on specification (2) of Table 4 estimated on all MNEs (not just MNEs with low ETRs). The revenue impacts are estimated by multiplying the estimated ETR impact (rows 1 and 2) by the total amount of profit reported by MNEs in 2024 (row 3). Row 4 reports the resulting point estimate of global tax revenue impacts while row 5 reports the implied 95% confidence interval. Column (3) uses 2022 CbCR data, complemented with other sources, to calculate total in-scope profit. This profit amount is adjusted to 2024 values using growth rates observed in Orbis data between 2022 and 2024. Row 6 shows the revenue range for MNEs used to estimate profits in in row 3, and row 7 shows the dataset used. Only MNEs with positive profits are included in calculating total profit amounts.

Overall, the revenue estimates are somewhat lower than the ex-ante estimates reported in Hugger et al. (2024[1]), while being of similar order of magnitude. $^{29}$ In interpreting results, it should be noted that the ETR impacts estimated in this paper are for 2024 only and are thus unlikely to correspond to the long-term impacts. The estimates reflect the initial SBIE carveout and may rise as this carveout is gradually reduced over time. As discussed above, indirect effects through reduced profit shifting might also take time to materialise if MNEs only gradually adjust their structures. A further factor that could impact the results is the gradual implementation of the GMT. While implementation was already widespread in 2024, many countries are still implementing parts of the GMT, and the UTPR will only become effective in 2025 for most MNEs. This means that low-taxed profit in jurisdictions without QDMTT for MNEs not headquartered in an IIR-jurisdiction would be largely exempt from top-up taxation in 2024, reducing revenue below that modelled in Hugger et al. (2024[1]). Furthermore, the 2024 estimates presented in this paper pre-date the Side-by-Side agreement of 2026 which allows for a more generous treatment of certain tax incentives in the calculation of the GloBE ETR. This could result in lower tax revenues through the GMT in later years. There may be additional changes in impact over time, for instance as uncertainty over implementation by various jurisdictions and the final details of the rules is resolved.

## 7 Conclusions

This paper studies the impact of the announcement and implementation of the Global Minimum Tax at the MNE level. The GMT represents a significant change in the taxation of MNEs, with important questions about the magnitude and direction of impacts on ETRs faced by MNEs, as well as investment and employment outcomes. By utilising data covering the post-announcement and post-implementation period, this analysis moves beyond the previous literature on GMT impacts which mainly consists of ex ante assessments. It also represents a first empirical assessment of the impacts of a comprehensive corporate tax reform coordinated across a wide set of jurisdictions.

The results indicate increased ETRs of in-scope MNEs post implementation, but no negative investment or employment responses. The results suggest no announcement responses to the GMT. However, in-scope MNEs experienced an increase in their consolidated ETRs after the implementation of the GMT in 2024, driven primarily by an increase in tax liability. MNEs likely to be most affected by the reform given relatively low pre-GMT ETRs experienced an increase in their consolidated ETRs of 1.7 ppts. The increase for all firms is 1.4 ppts. These effects could either be driven through the direct effect of top-up taxation, or by a reduction in tax-motivated shifting of profits towards low-tax jurisdictions. The estimates are also used to approximate the change in corporate tax revenues due to the GMT, suggesting an additional EUR 79bn-109bn of CIT revenue globally in 2024. This represents an increase in global CIT revenue of 2.4-3.4%. However, the findings on economic activity suggest that the GMT did not induce a negative investment or employment response by MNEs, at least based on data from the first post-implementation year. The paper further finds that the changes in ETRs are more concentrated among MNEs in sectors previously found more likely to contain firms engaging in profit shifting activity, among MNEs with more profit shifting potential, as well as MNEs with higher levels of profit relative to substance. Nonetheless, there are also no significant effects on the count of subsidiaries or the presence in investment hubs for in-scope MNEs.

The analysis conducted can help to inform future international tax policy and continuing analysis of the GMT. At the same time and given the limited data available on the post-implementation period, the results represent short-run effects. MNEs might adjust their behaviour only gradually over time. The reduction of the substance exclusion over the coming years set out in the GloBE rules and the full entry into force of the UTPR might also induce the effects of the GMT to become stronger over time as the share of MNE profits under the GMT rises further. The implementation of the Side-by-Side agreement of 2026 and other recent changes could also impact the effects of the GMT in some jurisdictions. Future analysis based on additional years of data will be necessary to complement the findings presented in this paper with a longer-run perspective. Additionally, the paper finds that in-scope MNEs did not change their total investment in response to the GMT. These findings could be due to the design of the GMT and its substance carve-out which implies no change in the taxation of profits stemming from substance-heavy activities, or the effective targeting of the GMT on profit shifting activities which is less likely to impact the returns on marginal investments. Alternatively, the effects of investment and employment could be too small to be identified using the approach in this paper. It is also possible that while MNEs did not respond in terms of total investment, they have responded with a reshuffling of activities across jurisdictions. Analysis using jurisdiction-level data will be important to determine the extent of such responses.

## References

Altshuler, R., L. Boller and J. Serrato (2024), Tax Planning and Multinational Behavior, Mimeo., https://www.irs.gov/pub/irs-soi/24rptaxplanningmultinationalbehavior.pdf (accessed on 1 July 2026).

Bachas, P. et al. (2023), “Effective Tax Rates and Firm Size”, World Bank Policy Research Working Paper, Vol. 10312/February.

Barake, M. et al. (2021), “Revenue Effects of the Global Minimum Tax: Country-by-Country Estimates”, European Tax Observatory Note, No. 2. [14]

Bilicka, K., M. Devereux and I. Güçeri (2024), “Tax Policy, Investment and Profit Shifting”, NBER [12] Working Paper 33132.

Bratta, B., V. Santomartino and P. Acciari (2024), “Assessing Profit Shifting Using Country-by-Country Reports: A Nonlinear Response to Tax Rate Differentials”, National Tax Journal, Vol. 77/2, pp. 349-380, https://doi.org/10.1086/729293.

Chodorow-Reich, G. et al. (2024), “Tax Policy and Investment in a Global Economy”, NBER Working Paper 32180. [11]

Chodorow-Reich, G., O. Zidar and E. Zwick (2024), “Lessons from the Biggest Business Tax Cut in US History”, Journal of Economic Perspectives, Vol. 38/3, pp. 61-88, https://doi.org/10.1257/jep.38.3.61.

Clifford, S., J. Miethe and C. Semelet (2025), The Distribution of Profit Shifting, Elsevier BV, [38] https://doi.org/10.2139/ssrn.5355458.


De Vito, A. et al. (2023), “How Do Corporate Tax Hikes Affect Investment Allocation within Multinationals?”, Review of Finance 29/2, pp. 531-565, https://doi.org/10.1093/rof/rfaf006. [9]

Delis, F. et al. (2021), Global evidence on profit shifting: The role of intangible assets, CEPR [52] Discussion Paper 16615.


Devereux, M. (2023), “International Tax Competition and Coordination with A Global Minimum Tax”, National Tax Journal, Vol. 76/1, pp. 145-166, https://doi.org/10.1086/723198. [26]

Devereux, M. et al. (2020), “The OECD Global Anti-Base Erosion (“GloBE”) proposal”, Oxford University Centre for Business Taxation Report.


Dlugosch, D. et al. (2025), “Understanding the weakness in business investment: A cross-country analysis”, OECD Economics Department Working Papers, No. 1836, OECD Publishing, Paris, https://doi.org/10.1787/89bd437d-en.


Ferrari, A. et al. (2023), Profit-shifting frictions and the geography of multinational activity, [20] https://www.cepii.fr/PDF\_PUB/wp/2023/wp2023-15.pdf (accessed on 1 July 2026).

Fuest, C. et al. (2025), “Global Profit Shifting of Multinational Companies: Evidence from Country-by-Country Reporting Micro Data”, Journal of the European Economic Association, https://doi.org/10.1093/JEEA/JVAF007. [22]


Hall, R. and D. Jorgenson (1967), “Tax Policy and Investment Behavior”, The American Economic Review, Vol. 57/3, pp. 391-414, http://www.jstor.org/stable/1812110. [34]

Hanappi, T., V. Millot and S. Turban (2023), “How does corporate taxation affect business investment?”, OECD Economics Department Working Papers, OECD Publishing, Paris, https://doi.org/10.1787/04e682d7-en.

Hanappi, T. and D. Whyman (2023), “Tax and Investment by Multinational Enterprises”, OECD Taxation Working Papers, No. 64, OECD Publishing, Paris, https://doi.org/10.1787/e817ce39-en.


Haufler, A., H. Okoshi and D. Schindler (2025), “Will the Global Minimum Tax Hurt Developing Countries”. [18]

Hebous, S. and M. Keen (2022), “Pareto-Improving Minimum Corporate Taxation”, CESifo Working Paper, No. 9633, https://www.cesifo.org/en/publications/2022/working-paper/pareto-improving-minimum-corporate-taxation (accessed on 1 July 2026).


Hugger, F. et al. (2024), “The Global Minimum Tax and the taxation of MNE profit”, OECD Taxation Working Papers, No. 68, OECD Publishing, Paris, https://doi.org/10.1787/9a815d6b-en.

Hugger, F., A. González Cabral and P. O'Reilly (2023), "Effective tax rates of MNEs: New evidence on global low-taxed profit", OECD Taxation Working Papers, No. 67, OECD Publishing, Paris, https://doi.org/10.1787/4a494083-en.

IMF (2023), “International Corporate Tax Reform”, Policy Paper No. 2023/001.


Joint Committee on Taxation (2023), “Possible effects of adopting the OECD’s Pillar Two, both worldwide and in the United States”. [16]


Keen, M., L. Liu and H. Pallan (2023), “International Tax Spillovers and Tangible Investment, With Implications for the Global Minimum Tax 2023”. [10]


Maffini, G., J. Xing and M. Devereux (2019), “The Impact of Investment Incentives: Evidence from UK Corporation Tax Returns”, American Economic Journal: Economic Policy, Vol. 11/3, pp. 361-389, https://doi.org/10.1257/pol.20170254.

OECD (2026), Tax Challenges Arising from the Digitalisation of the Economy-Global Anti-Base Erosion Model Rules (Pillar Two), Side-by-Side Package, OECD, Paris, https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/side-by-side-package.pdf (accessed on 1 July 2026).

OECD (2024), Corporate Tax Statistics 2024, OECD Publishing, Paris, https://doi.org/10.1787/9c27d6e8-en.

OECD (2023), Minimum Tax Implementation Handbook (Pillar Two), OECD Publishing, Paris, [30] https://www.oecd.org/tax/beps/minimum-tax-implementation-handbook-pillar-two.pdf (accessed on 1 July 2026).

OECD (2022), Tax Challenges Arising from the Digitalisation of the Economy – Commentary to the Global Anti-Base Erosion Model Rules (Pillar Two), First Edition: Inclusive Framework on BEPS, OECD/G20 Base Erosion and Profit Shifting Project, OECD Publishing, Paris, https://doi.org/10.1787/1e0e9cd8-en.

OECD (2021), Statement on a Two-Pillar Solution to Address the Tax Challenges Arising from the Digitalisation of the Economy, https://www.oecd.org/content/dam/oecd/en/topics/policy-issues/beps/statement-on-a-two-pillar-solution-to-address-the-tax-challenges-arising-from-the-digitalisation-of-the-economy-october-2021.pdf (accessed on 1 July 2026).

OECD (2021), Tax Challenges Arising from Digitalisation of the Economy – Global Anti-Base Erosion Model Rules (Pillar Two): Inclusive Framework on BEPS, OECD/G20 Base Erosion and Profit Shifting Project, OECD Publishing, Paris, https://doi.org/10.1787/782bac33-en. [27]

OECD (2020), Tax Challenges Arising from Digitalisation – Economic Impact [23]
Assessment: Inclusive Framework on BEPS, OECD/G20 Base Erosion and Profit Shifting Project, OECD Publishing, Paris, https://doi.org/10.1787/0e3cc2d4-en.

OECD (2020), Tax Challenges Arising from Digitalisation – Report on Pillar Two Blueprint: Inclusive Framework on BEPS, OECD/G20 Base Erosion and Profit Shifting Project, OECD Publishing, Paris, https://doi.org/10.1787/abb4c3d1-en.


Ohrn, E. (2018), “The Effect of Corporate Taxation on Investment and Financial Policy: Evidence from the DPAD”, American Economic Journal: Economic Policy, Vol. 10/2, pp. 272-301, https://doi.org/10.1257/pol.20150378.


UNCTAD (2022), World Investment Report 2022, United Nations Publications, New York. [24]

Zwick, E. and J. Mahon (2017), “Tax policy and heterogeneous investment behavior”, American Economic Review, Vol. 107/1, https://doi.org/10.1257/aer.20140855. [5]

Panel B: Probability of MNE status for treatment and control groups

## Annex A. Additional figures and tables

Figure A A.1. Distribution of consolidated ETRs of MNEs

[[KC_IMAGE_015]]


## Figure A A.2. Assignment into treatment and control

Panel A: Probability of above EUR 750m revenues for treatment and control groups


[[KC_IMAGE_016]]


[[KC_IMAGE_017]]


Figure A A.3. Distribution of treatment and control across industries and HQ jurisdictions
Panel A: Industries

[[KC_IMAGE_018]]

Panel B: Headquarter jurisdictions


[[KC_IMAGE_019]]

Note: Distribution of unique MNEs in the treatment and control group of the baseline sample across NACE codes (Panel A) and headquarter jurisdictions (Panel B). Industries and headquarter jurisdictions accounting for less than 2% of the companies in both groups are pooled into “Other”.

Figure A A.4. Treatment effect for investment in intangibles

[[KC_IMAGE_020]]

Note: The chart shows the coefficients $\theta_{\tau}$ on $Treated_{i} x Year_{t}$ as defined in Equation (1) for the log change in intangible fixed assets. The vertical lines indicate 95 percent confidence intervals for the coefficient estimates. The dashed red lines in both panels indicate the announcement of the GMT in 2021, the solid red lines indicate the implementation of the GMT in 2024. Outcome variables are normalised to zero in 2018.

Table A A.1. Additional regression results


Note: Columns (1)-(5) report estimated coefficients $\theta_{\tau}$ where $\tau \in (2016, \dots, 2024)$ from Equation (1). Columns (6)-(10) report the estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2). The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. Dependent variables are measured as log changes. All specifications include year and company fixed effects as well as additional controls following Equations (1) and (2). Standard errors are clustered at the company level and are reported in parenthesis.

Table A A.2. Robustness checks – Investment and employment
Panel A: Investment


Panel B: Employment


Note: The different columns report estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2) for a number of alternative samples. Some estimations include additional control variables as indicated (Columns (6)-(9)). The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. The dependent variables are the log change in tangible fixed assets (Panel A), and the log change in employment (Panel B). All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.

Table A A.3. Placebo tests – Investment and employment


Note: Columns (1) to (6) report the estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2). The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. The dependent variables are the log changes in tangible fixed assets (columns (1)-(3)) and the log change in employment (columns (4) to (6)) at the MNE group level. All specifications include year and company fixed effects as well as additional controls following Equation (1). Standard errors are clustered at the company level and are reported in parenthesis.

Table A A.4. Heterogeneity estimates – Investment and employment

Panel A: Investment


Panel B: Employment


Note: The different columns report estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2) for a number of alternative sample splits. The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.

Table A A.5. Heterogeneity estimates – Size and IIR status – Investment and employment


Note: The different columns report estimated coefficients $\theta^{A}$ and $\theta^{I}$ from Equation (2). Columns (1) and (3) report coefficients separately for firms split by size relative to the median within the treated group. Columns (2) and (4) extend the sample by including firms with revenues above EUR 2,000m and reports separate effects for this group. Columns (5) and (6) report coefficients separately for firms from headquarter jurisdictions with and without an IIR. The dummy variable $Treated_{i}$ takes the value of 1 for companies expected to be in scope of the GMT. All specifications include year and company fixed effects as well as additional controls following Equation (2). Standard errors are clustered at the company level and are reported in parenthesis.
