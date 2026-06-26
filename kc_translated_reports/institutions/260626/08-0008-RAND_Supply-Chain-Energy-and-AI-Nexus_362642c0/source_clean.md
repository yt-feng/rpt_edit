# 兰德公司：AI缺的不是芯片，是电网里的天然气轮机

ISMAEL ARCINIEGAS RUEDA, RAHIM ALI, FRANK ANDUJAR LUGO, KARISHMA V. PATEL, ROBIN WANG

# Supply Chain, Energy, and AI Nexus

Evaluating AI Energy Supply Chain Vulnerabilities

For more information on this publication, visit www.rand.org/t/RRA4707-1.

## About RAND

RAND is a research organization that develops solutions to public policy challenges to help make communities throughout the world safer and more secure, healthier and more prosperous. RAND is nonprofit, nonpartisan, and committed to the public interest. To learn more about RAND, visit www.rand.org.

## Research Integrity

Our research integrity is grounded in RAND's core values of quality and objectivity. Rigorous quality assurance procedures, conflict of interest screening, and transparency in funding ensure that every study is objective and nonpartisan. Learn more at www.rand.org/integrity.

RAND's publications do not necessarily reflect the opinions of its research clients and sponsors.

Published by the RAND Corporation, Santa Monica, Calif.


RAND $^{®}$ is a registered trademark.

## Limited Print and Electronic Distribution Rights

This publication and trademark(s) contained herein are protected by law. This representation of RAND intellectual property is provided for noncommercial use only. Unauthorized posting of this publication online is prohibited; linking directly to its webpage on rand.org is encouraged. Permission is required from RAND to reproduce, or reuse in another form, any of its research products for commercial purposes. For information on reprint and reuse permissions, visit www.rand.org/about/publishing/permissions.

The past few years have seen rapid advances in the capabilities of artificial intelligence (AI) models and increasingly widespread use of such models. The resulting increase in demand for AI computational resources is already posing challenges for data center construction in the United States, primarily because it is difficult to find and access reliable power grid capacity. To anticipate the constraints these challenges may place on future AI growth, we seek to answer the following questions in a series of RAND reports:

• What will the U.S. additional power capacity be by 2030?

\- What are the key constraints to scaling the U.S. power grid to meet additional demand?

\- What sites or regions in the United States have favorable or unfavorable characteristics for maximizing available energy capacity for AI data centers? What is an estimate of the maximum amount of power available for AI data centers at a single site by 2030?

\- What are the existing electrical equipment supply chain vulnerabilities that may constrain frontier AI data center development?

In this report, we first provide an inventory of critical electrical equipment required for frontier AI data center operations, in which we define frontier AI data centers as a subset of hyperscale data centers that are designed to consume over 100 megawatts (MW) and are used primarily for AI training and operation. $^{1}$ The inventory of equipment includes components at the front of the meter, behind the meter, and off-grid operations equipment, commonly referred to as bridge power. $^{2}$ Next, we introduce a methodology to estimate supply chain vulnerabilities using open-source data, which we used to identify the most vulnerable electric equipment. With this methodology, we develop a ranking of supply chain vulnerabilities across the inventory. Then, we quantitatively evaluate the impact of these vulnerabilities by examining supply chain risks in the context of the inability of the United States to meet frontier AI energy demand using case studies of different supply chain threats. $^{3}$ Finally, we conclude with policy recommendations.

## Center on AI, Security, and Technology


## Funding

This research was independently initiated and conducted within the Center on AI, Security, and Technology using income from operations and gifts from philanthropic supporters. A complete list of donors and funders is available at www.rand.org/CAST. RAND donors and grantors have no influence over research findings or recommendations.

## Acknowledgments

We would like to thank the leadership of the RAND Center on AI, Security, and Technology—Sella Nevo, Jeff Alstott, and Kyle Evans—for their guidance on this publication; Jason Etchegaray for managing the quality assurance process; and our reviewers Toby Sytsma, Konstantin Pilz, and David Rode for their thoughtful feedback. We are also thankful to several industry stakeholders with whom we held discussions about the topic for their insights.

## Issue

The anticipated growth in artificial intelligence (AI) development requires additional power capacity. Data center operators often prefer that this additional capacity comes from connections to the grid because such connections offer improved reliability, resilience, and cost-effectiveness that is not available from on-site electricity generation. $^{4}$ However, stakeholders have identified major challenges facing the U.S. grid, especially concerning the integration of large volumes of energy resources. The North American Electric Reliability Corporation (NERC) $^{5}$ warns that more than half of North America faces a substantial risk of energy shortfalls within the next five to ten years, the result of increasing electricity demand from data centers, decarbonization through electrification, and industrial growth. $^{6}$ Although many initiatives to increase generation capacity are in progress, the pace of these efforts may pose challenges in terms of meeting future energy demands. And progress can be hindered by supply chain vulnerabilities in the procurement of critical electrical equipment for front-of-the-meter (FTM), behind-the-meter (BTM), and off-grid (usually referred to as bridge power [BP]) projects to supply AI energy demand. This report addresses the following research questions:

\- What is the critical equipment required for meeting frontier AI energy demand?

• What are the supply chain vulnerabilities of this equipment?

\- What could be the impact of those vulnerabilities on the U.S. power grid's ability to meet AI demand by 2030?

## Approach

We used a mixed-methods approach for this research, as follows:

\- We conducted a rapid literature review, which highlighted the existing major research gaps between (1) component-level needs for AI energy build-out and (2) supply chain analysis directly informing component-level assessments. This report provides contributions to closing those gaps.

\- We developed an inventory of critical equipment required for powering frontier AI data centers. Our analysis covered equipment not only for grid-connected data centers (FTM and BTM) but also for BP.

\- We developed a methodology to assess the supply chain vulnerabilities of the inventory of critical equipment by introducing a supply chain vulnerability index and visualization maps to rank the vulnerability of the equipment.

\- We developed a case-study approach to quantitatively evaluate the impact of vulnerabilities on the risk of not meeting AI demand using a framework based on examining supply chain risk as a function of the following three elements: threats, vulnerabilities, and consequences.

## Key Findings

\- We found that several pieces of equipment, such as natural gas turbines, that may be required for FTM installations are also required by off-grid BP installations, which indicates that data centers cannot eliminate supply chain constraints by moving off-grid.

\- We introduced a composite supply chain vulnerability score composed of several metrics, which allows for a ranking of the different equipment across several years. Using this score, we identified the following:

\- For the FTM generation category in 2025, steam turbines, geothermal production wells, and solar panel parts are at the top of the vulnerability ranking. Battery technologies and chemistries also show elevated 2025 composite vulnerability. See Table 4.2.

\- In the FTM transmission category, conductors and wires and reactive power compensators show the highest 2025 composite vulnerability. See Table 4.3.

\- For BTM, there is a concentration of backup power components at the top of the supply chain vulnerability ranking in 2025. See Table 4.4.

\- We found that generation components demonstrate systematically higher composite vulnerability scores in 2025 than transmission components do. This divergence likely reflects fundamental market structure differences. Transmission equipment represents more established, standardized technology, whereas generation components often involve specialized, technologically advancing systems with more limited production sources and higher barriers to entry for new manufacturers.

\- We identified that the main source of supply chain vulnerabilities varies significantly across equipment and time, which implies that effective supply chain resilience strategies must be tailored to the specific vulnerability profile of each equipment. For instance, turbine generators show a vulnerability mainly arising from market concentration; for transformers, the main source of vulnerability is volume volatility. Tables 4.2, 4.3, and 4.4 provide a deeper analysis of vulnerability profiles for transformers, natural gas turbines, and batteries.

\- We developed a decisionmaking framework that matches critical components to target policy interventions and therefore recognizes the heterogeneity in the supply chain vulnerabilities across components.

\- We developed case studies and sensitivity analysis to quantitatively estimate the impact of supply chain considerations on the ability of the U.S. power grid to meet AI frontier demand. We measured this case study against a base case in which there were supply chain delays similar to what is currently reported by stakeholders.

\- We estimate that supply chain–related threats to FTM components (natural gas generation, storage, transformers) have the potential to result in approximately a 7 percent to 31 percent decrease in available net capacity by 2030 in comparison with a base case of no additional delays in the procurement of natural gas turbines, batteries, and transformers.

\- We estimate that supply chain–related threats to BTM components (batteries) have the potential to result in approximately an 8 percent decrease in available net capacity by 2030 in comparison with a base case of no additional delays in the procurement of BTM batteries.

\- We estimate that a further move off-grid to meet the energy gap using BP would translate to an additional need for aeroderivative turbines of 91 to 123 110-MW turbines or 451 to 611 30-MW turbines by 2027, as well as 1,582 to 1,690 110-MW turbines or 7,909 to 8,449 30-MW turbines by 2030, which would further stress the supply chain.

## Policy Recommendations

## Our suggested recommendations are as follows:

\- Implement a decision framework for responding to observed supply chain vulnerabilities with proportionate policy actions. The metrics developed in this research can be used to systematically distinguish appropriate response options according to patterns observed in supply chain vulnerabilities by type, magnitude, and duration. As critical components meet distinguishing criteria, responses can move across different levels, such as routine monitoring, targeted resilience efforts, and proactive strategic intervention. The U.S. Department of Energy (DOE) should adopt a decision framework, such as the one provided in Table 6.1, to have a targeted approach to address supply chain issues.

\- The U.S. government should prioritize supply chain policy interventions in generation systems, given their more acute supply chain vulnerability with respect to transmission and critical impact across all supply options (FTM, BTM, and BP). Specifically, priority should be given to the most vulnerable generation components as listed in Table 4.2.

\- Consider improving the monitoring capabilities to inform intervention by increasing the granularity of trade data for certain electrical components, such as natural gas turbines and transformer types. The U.S. International Trade Commission and U.S. Customs and Border Protection should work together to increase the specificity of certain Harmonized Tariff Schedules and Schedule B codes, at the ten-digit level. This report provides Figures 4.7 (for transformers) and 4.8 (for turbines), the most supply chain-vulnerable components that could be targeted for additional trade data granularity.

\- Consider enhancing supply chain mapping capabilities by designing reasonable disclosure requirements for firms transacting or handling key critical components. The U.S. Securities and Exchange Commission and U.S. Department of Homeland Security should drive a consultative process with utilities, producers, and other

government partners to ensure a common language and understanding that leads to improved visibility and coordination around supply chain risks while calibrating the potential burden of additional reporting requirements against the perceived benefits of improving decisive insights. $^{7}$ The supply chain vulnerability heat maps in Figures 4.3 and 4.5 could be used to select the equipment that may merit additional reporting.

\- Consider developing a reserve of high-demand, low-supply electric grid components to proactively buffer against supply chain shocks. Building on proven models for strategic reserves across critical sectors for guidance on technical operations, $^{8}$ including GridAssurance for transmission equipment, the Strategic Petroleum Reserve for energy security, the National Defense Stockpile for critical minerals, and the Strategic National Stockpile for medical supplies, DOE and the Federal Energy Regulatory Commission (FERC) should coordinate with utilities and large loads, such as data centers, to identify and maintain reserves of the most-critical grid components. A transparent selection process and cost recovery mechanism would ensure that these reserves enhance resilience while remaining economically sustainable.

\- Consider developing incentives for utilities and large loads to adopt codes and standards that increase the standardization of critical equipment as a measure to mitigate supply chain constraints, such as market concentration. DOE and the U.S. Department of the Interior should work with consensus-driven organizations, such as the National Electric Code or the Institute of Electrical and Electronics Engineers, and utilities to develop codes and standards that encourage standardization and adoption. Figures 4.3 and 4.5 provide the critical components most likely to benefit from standardization because of their high market concentration.

\- Consider developing a mechanism for collaboration and transparency between utilities and large loads to improve load forecasting and therefore better manage the procurement of scarce equipment (e.g., turbines). DOE and FERC should facilitate the development of those collaborations to facilitate long-term partnerships that help mitigate supply chain issues.

\- Consider encouraging, whenever possible, the substitution of storage equipment with chemistries with high supply chain vulnerabilities (e.g., lithium) with chemistries of lower vulnerabilities (e.g., sodium). DOE should work with research organizations and utilities to develop potential commercialization opportunities for storage chemistries with lower vulnerability.

About This Report ....iii
Summary....v
Figures and Tables....xi
Chapter 1. Introduction....1
Background and Motivation....1
Key Assumptions and Limitations....2
Report Outline....4
Chapter 2. Literature Review ....5
General Findings: Persistent Gaps in Component-Level Detail and Quantitative Analysis....6
Critical Electric Power Components Required by AI Data Centers....8
Projected Equipment Requirements....9
Supply Chain Vulnerabilities for AI-Critical Electrical Equipment....9
Chapter 3. Inventory of Critical Electric Power Components....11
Approach to Developing Inventory....11
Front-of-the-Meter Systems and Components....14
Behind-the-Meter Systems and Components....16
Bridge Power Systems and Components....17
Benefits of Inventory Development....18
Chapter 4. Supply Chain Vulnerability Estimation....19
Methods for Examining Supply Chain Vulnerability....20
Results and Findings....28
Chapter 5. Assessing Supply Chain Risks for Frontier AI Data Center Expansion Using Case Studies....48
Estimating Consequences for Frontier AI Data Center Expansion....49
Threat Scenarios Affecting Frontier AI Data Center Expansion....51
Supply Chain Impact....56
Impact for Off-Grid Systems....57
Chapter 6. Policy Recommendations....60
Recommendations....60
Appendix A. Literature Review Methodology....70
Seed Literature....70
Key Words for Source Identification....71
Search Protocols....75
Structured Queries for Evidence Extraction....75
Synthesis....76
Appendix B. Inventory of Critical Components....78
Appendix C. Example of Supply Chain Vulnerability Assessment Calculation....90

Example Vulnerability Calculation....90
Sensitivity Analysis....92
Appendix D. Supply Chain Vulnerability Assessment....93
Abbreviations....100
Glossary....101
References....103
About the Authors....109

## Figures

Figure 2.1. Literature Review Workflow ....5
Figure 3.1. Schematic of the General Energy Infrastructure Categories....13
Figure 4.1. Process for Matching HTS Codes to Critical Components....22
Figure 4.2. Composite Vulnerability Indicator Calculation....26
Figure 4.3. Vulnerability Map for FTM Components....30
Figure 4.4. Aggregate Trends in Vulnerability for FTM Components....33
Figure 4.5. Vulnerability Map for BTM Components....36
Figure 4.6. Aggregate Trends in Vulnerability for BTM Components....38
Figure 4.7. Vulnerabilities for Transformer-Related Components for FTM and BTM....41
Figure 4.8. Vulnerabilities for Turbine-Related Components for FTM and BTM....44
Figure 4.9. Vulnerabilities for Battery-Related Components for FTM and BTM....47
Figure 5.1. Approach to Measure Supply Chain Risk....49
Figure D.1. Vulnerability Scores for FTM Systems....94
Figure D.2. Vulnerability Scores for BTM Systems....96

## Tables

Table 2.1. Summary of Identified Research Gaps....7
Table 3.1. High-Level Overview of FTM Systems....15
Table 3.2. High-Level Overview of BTM Systems....17
Table 4.1. Description and Interpretation of Vulnerability Metrics....24
Table 5.1. Historical Procurement Delays of Components....51
Table 5.2. Mapping of Supply Chain Threats to Vulnerability Indicators....54
Table 5.3. Equations and Variables to Calculate Component Delay Based on the Threat....55
Table 5.4. Threat Scenario Impact on FTM Net Generation Capacity....57
Table 5.5. Threat Scenario Impact on BTM Effective Generation Capacity....57
Table 6.1. Recommended Response Options, by Critical Component....63
Table A.1. Seed Literature Source Summary....71

Table A.2. Mapping of Research Questions to Specific Keyword Combinations and Thematic Groups .....73
Table A.3. Sources Identified by Category and Search Protocol .....75
Table B.1. Inventory FTM: Transmission .....78
Table B.2. Inventory FTM: Generation .....80
Table B.3. Inventory BTM: Transformer .....84
Table B.4. Inventory BTM: Thermal Management .....85
Table B.5. Inventory BTM: Supporting Data Center Equipment .....85
Table B.6. Inventory BTM: Power Management .....85
Table B.7. Inventory BTM: Power into the Racks .....86
Table B.8. Inventory BTM: Power Transfer .....87
Table B.9. Inventory BTM: Backup Power .....87
Table C.1. Calculate Annual Metrics .....90
Table C.2. Aggregate HTS-Level Metrics to the Component Level .....91
Table C.3. Apply Metric Weights and Compute the Composite Vulnerability Score .....91
Table C.4. Sensitivity Analysis Results .....92

## Background and Motivation

Robust and reliable access to energy is fundamental for the continued rollout of artificial intelligence (AI) infrastructure. However, many critical energy-related supply chains face vulnerabilities, such as bottlenecks, delays, supplier monopolies, or the potential for foreign coercion. The United States has encountered supply chain–related challenges for electric components across generation, transmission, and distribution systems. For example, a 2022 survey by the American Public Power Association reported a severe mismatch between the supply and demand of distribution transformers in the United States. $^{9}$ Domestic manufacturing capacity has struggled to keep pace with demand, resulting in prolonged delivery timelines, shrinking stockpiles, and a surge in postponed or abandoned infrastructure projects across public power utilities. Transformer lead times, which averaged just two to three months in 2020, ballooned to roughly one year by 2022, with some utilities facing delays exceeding three years. These escalating wait times were largely attributed to coronavirus disease 2019 (COVID-19) pandemic–induced disruptions in global supply chains, which by 2023 had pushed delivery estimates to as long as 30 months. $^{10}$ Meanwhile, the delivery of gas-fired turbines ordered in 2025 can take as many as seven years, with costs rising more than two-and-a-half times compared with pre-pandemic prices. $^{11}$

In this report, we aim to identify electric power components that are critical for supporting AI data centers to highlight potential vulnerabilities in the supply chains of these components, to quantitatively assess the impact of these vulnerabilities on the risk of not meeting AI demand, and to propose possible courses of action for policymakers. To do so, we developed an inventory of critical power grid components through open-source data (specifically, through a review of academic and industry literature). We differentiate between critical components for front-of-the-meter (FTM), behind-the-meter (BTM), and bridge power (BP) solutions (which cover ways to power data centers before their connection to the grid). We then provide an estimation of supply chain vulnerabilities, highlight the relative vulnerabilities across components, and use case studies to quantitatively assess the impact of those vulnerabilities on the power grid's ability to meet frontier AI data center energy demands. We develop a

decisionmaking framework in which policy recommendations are matched to critical components to allow for targeted solutions, given differences in sources of vulnerability across components.

## Key Assumptions and Limitations

Our approach has several assumptions and limitations, outlined below.

## Assumptions

\- Our analysis has a time horizon of 2030, and therefore we assume that the topology of the grid is stable as well and focus on available commercial technologies. We assume also that our inventory of critical components is general enough to cover most of the components in grids where frontier AI data centers will be established.

\- Our methodology for supply chain assessment in Chapter 4 is based on capturing the movement of goods between countries, assuming imports are a sizable representation of supply chains for critical components. We justify this assumption by choosing a comprehensive suite of indicators and identifying domestic capacity for comparison where we can. For example, only 20 percent of U.S. demand for transformers was met by domestic manufacturing in 2024. $^{12}$ Where this assumption does not hold, our international supply chains may appear stable in the framework while facing other supply chain challenges. Future iterations of this framework could add demand and domestic sourcing data upon availability to obtain a more holistic picture of supply chain issues.

\- We make the following assumptions to quantitatively evaluate the impact of vulnerabilities on meeting AI demand. First, we assume that additional disruptions on supply chain will affect only new projects to be added to the pipeline, which is likely to be an underestimation of disruptions. Second, we assume that the impact will be reflected in procurement delays and subsequently in the completion dates of projects; we did not consider other impacts, such as project cancellations. Third, we assume that the procurement delays of equipment (such as transformers) affect in a similar fashion all projects to be connected to the grid; we did not consider that some utilities and data centers may have mitigation measures already in place, such as preferred relationships with the equipment providers or access to pools of equipment.

## Limitations

\- The inventory of critical components is meant to be general, not specific to a particular electric grid or project. It is possible that specific projects, such as new technology pilot demonstrations associated with data centers, may include equipment not in our inventory. $^{13}$

\- The supply chain vulnerability assessment and results are largely shaped by data availability, quality, and structure and so have some limitations. First, by relying on U.S. International Trade Commission (USITC) trade data, the analysis uses the most suitable publicly available source for tracking international flows, but it effectively infers vulnerabilities by goods that cross borders, omitting intrafirm trade, domestic production, stockpiles, and non-U.S. sourcing that manufacturers may rely on as buffers. Second, when trade codes are applied to shipments, they can range from highly specific to broad catch-all families of goods, often mixing items used in the power system with other applications. Because these codes underpin how component movements are observed, the accuracy of trade-code-to-component mappings directly affects the ability to trace supply chains specific to the power grid. Third, the customs and bill of lading process involves corrections, retractions, and reassignments of Harmonized Tariff Schedule (HTS) codes, quantities, and values, affecting data quality. These limitations underlie the motivation for using a more holistic vulnerability framework that combines several metrics rather than relying on a single indicator to flag or explain vulnerabilities.

\- Our assessment of the impact of supply chain vulnerabilities on power grid available capacity is limited by our approach of using case studies. First, we did not estimate the probabilities of occurrence of the scenarios described in the case studies, so the quantitative ranges of impact presented can be seen only as conditional estimates, given the case studies. Second, we limit our analysis to a small subset of components FTM and BTM because of data availability limitations. Third, we anchor the consequences of supply chain vulnerabilities on the procurement of equipment on historical data of previous supply chain disruptions. Fourth, we based our analysis on the impact of supply chain vulnerabilities on the completion of grid generation projects, as we rely on developed methodologies of grid generation completion rates developed in previous RAND research. Our analysis of impact on off-grid projects was limited to a mostly qualitative description.

## Further Research

Our framework provides the most comprehensive systematic assessment of grid-wide supply chain vulnerabilities feasible, given available data. Future iterations of this work could be strengthened by

\- integrating grid-specific operational data, such as installation lead times, failure rates, and functional substitutability across components

\- conducting supplier audits, capacity surveys, and stress tests to add analytical approaches, including probabilistic forecasting, scenario design, and evaluation of mitigation strategies, linking trade-based indicators more directly to system reliability and resilience outcomes

\- measuring the impact of supply chain vulnerabilities on off-grid projects and quantitatively estimating the impact on AI demand.

## Report Outline

In this report, we discuss existing supply chain vulnerability in electric equipment affecting frontier AI data centers and their impact. In Chapter 2, we briefly review the results of our rapid literature review. In Chapter 3, we present the methodology used to develop an inventory of critical equipment for FTM, BTM, and BP frontier AI critical electric equipment. In Chapter 4, we develop a methodology to identify supply chain vulnerabilities in the equipment listed in Chapter 3. In Chapter 5, we discuss the risks of not meeting frontier AI energy demand because of supply chain issues. We focused on a subset of threats that could affect the vulnerabilities identified in Chapter 4, leading to consequences that could increase the risk of the United States not meeting AI frontier demand. In Chapter 6, we provide policy recommendations to address these impacts and a decision framework matching policies to components. Appendix A provides an overview of the methodology used for the literature review. Appendix B provides a list of all electrical critical components required to power AI Data centers, both on the grid and off-grid. Appendix C provides an example of a supply chain vulnerability calculation. Appendix D provides a list of the supply chain vulnerability metrics computed for each of the critical components.

The rapid expansion of AI applications is expected to drive significant increases in energy demand across the United States, particularly through the development of large-scale AI data centers. Anticipating and supporting this growth requires a thorough understanding of both the electric power needs of these facilities and the robustness of the supply chains for critical electrical equipment. The purpose of this literature review is to synthesize existing knowledge regarding the power requirements of AI data centers, identify the most essential electrical components, and highlight vulnerabilities within relevant supply chains.

Background research conducted for previous RAND reports and consultations with industry stakeholders consistently identified supply chain challenges as a potential bottleneck in meeting the energy demands of large-scale AI data centers. However, earlier investigations primarily focused on broader questions of capacity and grid scalability, leaving supply chain vulnerabilities relatively under-explored. The sources reviewed in prior studies revealed distinct bodies of literature: Some centered on AI development and data center operations, others on the requirements and technological evolution of electrical equipment, and yet others on supply chain dynamics. Despite this breadth, the relationships among these areas—and their implications at the level of specific electrical components—remained unclear. These gaps highlight the need for a dedicated literature review that systematically maps the knowledge landscape and clarifies linkages between these fields.

Figure 2.1. Literature Review Workflow

[[KC_IMAGE_001]]


This literature review assessed more than 1,700 academic papers and approximately 250 gray literature sources to address the following three research questions regarding AI data center power equipment needs and supply chain issues:

\- Research Question 1: What are the critical electric power components required by AI data centers, including BTM, FTM equipment, and BP solutions?

\- Research Question 2: What are the projected equipment requirements, based on relevant AI energy need forecast?

\- Research Question 3: What supply chain vulnerabilities currently exist for the procurement of AI-critical electrical equipment?

The review began with an evaluation of 38 expert-recommended sources to define the scope, followed by the identification of more than 1,700 academic papers and 250 gray literature items using 17 targeted keyword combinations. Structured searches were conducted for post-2020 materials, and standardized queries were used to extract relevant data for each research question. Findings were then synthesized and analyzed across all sources. The literature review workflow is presented in Figure 2.1. Details of the full methodology are provided in Appendix A.

## General Findings: Persistent Gaps in Component-Level Detail and Quantitative Analysis

Across both the academic and gray literature, the findings reveal that although the high-level categories of critical electric power components and supply chain risks for AI data centers are well recognized, detail concerning component-level requirements and vulnerability mapping is limited. The academic research on this nascent cross-disciplinary topic remains largely conceptual, while gray literature more closely tracks practical developments and operational realities.

Overall, although there is consensus on an increasing energy demand and the types of critical components required, such as uninterruptible power supply (UPS) systems, transformers, battery energy storage, and advanced grid-integration technologies, our review reveals persistent gaps across all three research questions. $^{14}$ Among these questions, the identification of critical electric power components (Research Question 1) is relatively well covered, which can inform a comprehensive inventory of main categories and their functions. No studies compiled a comprehensive list of electrical equipment components directly relevant to AI data center operations and demand across the spectrum of FTM, BTM and BP. $^{15}$ Quantitative analysis of projected equipment requirements (Research Question 2) and systematic mapping of supply chain vulnerabilities and their impact on AI energy demand (Research Question 3) are less developed, with a persistent lack of detailed component estimates and product-specific quantitative assessments.

Despite the breadth of sources reviewed, persistent research and knowledge gaps remain across all three research questions (see Table 2.1). Both the academic and gray literature provide thorough identification of core categories for electric power components and general supply chain challenges, yet they fall short in offering component-level technical specifications. $^{16}$ For example, neither domain provides consistent quantitative estimates for transformer counts, generator capacities, or detailed replacement cycles required to support escalating AI data center energy demands. Furthermore, systematic mapping of supply chain vulnerabilities—including identification of single points of failure, geographic origin dependencies, and the detailed propagation of risks across component sub-tiers—is rarely undertaken. This can result in limited practical utility for policymakers who are evaluating targeted interventions.

Table 2.1. Summary of Identified Research Gaps


## Critical Electric Power Components Required by AI Data Centers

Academic sources consistently underscore the complexity and robustness required of electrical infrastructure to support modern AI data centers. $^{17}$ Studies highlight the vital role of both BTM and FTM components, including sophisticated UPS systems, advanced batteries, generators, power conversion units, cooling infrastructure, smart grid interfaces, and transformers. The literature notes that most research and industry focus is on BTM infrastructure, with FTM requirements and standards remaining under-explored. Additionally, academic works emphasize the need for millisecond-scale performance, gigawatt-scale pulsing load management, and advanced protection schemes specific to the demands of high-density AI workloads. $^{18}$ These are the areas in which existing frameworks are insufficient.

At the same time, industry reports, consultancy studies, and government documents provide a more operational and pragmatic perspective on critical electrical infrastructure. These sources affirm the necessity of both grid-side (FTM) systems—substations, transformers, transmission and distribution lines, switchgear, and metering/protection—and facility-side (BTM) systems, such as generators, battery energy storage systems, UPS units, and hybrid microgrids. $^{19}$ There is frequent reference to dual-feed substations, modular redundancy architectures (N+1, 2N), and automated transfer switches for ensuring fault-tolerant, high-availability power. Gray literature further details the increasing deployment of advanced cooling systems (liquid, immersion), smart transformers, and grid-interactive technologies. $^{20}$

Overall, the gray literature sources provide details on component categories, but there is limited coverage for performance benchmarks and technical specifications. The functional boundary between FTM and BTM equipment is often only implicitly defined.

## Projected Equipment Requirements

Academic literature is in agreement in terms of projecting steep growth in AI-related data center electricity demand, with forecasts suggesting that AI data centers could account for up to 12 percent of U.S. electricity use and 8 percent globally by 2030. Drivers include exponential AI workload expansion, increased hardware density, and hyperscale facility growth. These macro-level projections and scenario analyses rarely translate into quantitative estimates for specific electrical equipment needs. Most studies present system-wide or site-wide capacities, generalized equipment categories, and economic impact estimates.

The industry discussions paint a similar picture of urgency for addressing future equipment needs; as with academic sources, however, most gray literature stops short of giving granular, engineering-level procurement specifications. Reports cite typical data center site sizes of 100–500 megawatts (MW) and anticipate substantial grid expansion to meet surging demand. Equipment counts, ratings, and replacement cycles are not systematically mapped from energy projections. The literature review identified few studies or articles with detailed inventories.

## Supply Chain Vulnerabilities for AI-Critical Electrical Equipment

The academic studies in our literature review identify significant supply chain vulnerabilities affecting the procurement of AI-critical electrical infrastructure, but there is limited empirical evidence on component-specific case studies or trade data. Most assessments are sectoral or macro-level. Key risks emerging from the peer-reviewed papers include supply-demand imbalances, material shortages, market concentration among a limited set of global suppliers, and heavy reliance on imports, especially from East Asia. Many papers reference broad categories of supply chain risk but lack detailed mapping to specific equipment, such as transformers, switchgear, or batteries.

Recent industry analyses and government reports bring operational details to supply chain vulnerability assessment, documenting long lead times, acute shortages, foreign supplier concentration, and geopolitical disruptions. Reports highlight dependence on imported transformers, batteries, semiconductors, and cooling equipment, as well as critical raw materials sourced from a handful of countries. Hyperscaler procurement strategies, regulatory actions, and real-world disruptions (such as pandemic-related delays and tariff shocks) are more frequently discussed in industry and governmental sources. In general, systematic, component-level supply chain mapping remains an acknowledged gap, but the literature review process identified supply chain studies from the U.S. Department of Energy (DOE) and the European Commission that adopted rigorous methodology and had comprehensive coverage of electrical equipment, but

these studies do not reflect the latest component-level needs or supply chain dynamics driven by the development of AI build-out. $^{21}$

To meet the anticipated electric power needs for large-scale AI data centers (i.e., data centers requiring greater than 100 MW of power), significant build-out of additional power capacity will be needed. We estimated in previous research that the power demand for AI data centers globally could reach 327 GW by 2030, of which 237 GW are expected in the United States alone. $^{22}$ This build-out of additional power capacity will require the procurement of components both for electric grid infrastructure (e.g., high voltage transmission lines, power plant generating units) and for infrastructure at the data center level (e.g., step-down transformers, diesel generators) to support a reliable supply of electric power. These challenges will also affect off-grid bridge power data centers. The suppliers of these components include a mix of domestic and global entities; however, in this study, we specifically examined potential supply chain risks and challenges from the lens of global suppliers. To better understand and examine these potential supply chain vulnerabilities, we developed an inventory of critical components that would be needed to meet the electric power demands for large-scale AI data center expansion both on the grid and off-grid. In this chapter, we describe the approach used to develop the inventory, the organizational structure of the inventory, and the benefits of developing the inventory to identify supply chain vulnerabilities. In Appendix B, we include the full list of the components included in the inventory. It is worth noting that supply chain challenges are dependent not only on the ability to procure components but also on the skilled labor needed to install those components. There is considerable evidence demonstrating that the skilled labor market in the United States is facing shortages in the manufacturing and construction industry. $^{23}$ While this is an important factor in the overall calculus of electric power availability, skilled labor shortages in this context are primarily a domestic issue and outside the scope of this research, since our focus was on global supply chain risks.

## Approach to Developing Inventory

We developed the inventory of components through open-source data, leveraging academic and industry literature. We specifically focused on identifying components necessary for operating and interconnecting large loads. First, we identified the main components of the

electric power grid and data centers. For instance, resources from such organizations as the U.S. Energy Information Administration, Congressional Research Service, and National Laboratory of the Rockies provide descriptions and overviews of the systems and components that comprise the electric power grid, including how electricity is generated and transmitted to reach customers and how the electric grid is transforming for modern needs. $^{24}$ Second, we supplemented the initial list of systems and components with subcomponents of those systems and components. For example, sources from DOE describe how natural gas turbines consist of a compressor, combustion system, and turbine. $^{25}$ When applicable, we also reviewed literature that focused on supply chain considerations for electric grid components, such as a report by the National Infrastructure Advisory Council that describes the shortage of electric grid power transformers. $^{26}$ Lastly, we input our initial draft of the inventory to ChatGPT-5's large language model (LLM) trained up to October 10, 2025, to validate the list of components in the inventory and identify any potential gaps or components that were not initially captured through the literature review. Although the LLM did not identify or flag any issues with the initial inventory, it suggested the addition of new components, such as power-smoothing and conditioning components, and the addition of components that supplemented existing components, such as magnetic energy storage coils.

We organized the inventory of components into three categories, shown in Figure 3.1:

\- FTM refers to components that are part of the electric grid transmission or generation system. $^{27}$ These components are typically owned and operated by electric utilities, independent power producers, or electric grid service providers.

\- BTM refers to components serving electric power systems that are located at the data center. These components are owned and operated by the entity managing the data center, not the electric utility.

\- BP refers to a temporary power source used to support a system during a transition period, such as power grid buildup or power grid maintenance.

Figure 3.1. Schematic of the General Energy Infrastructure Categories

[[KC_IMAGE_002]]

NOTE: BP is meant as a stopgap power solution until a more permanent alternative is secured.

We developed the inventory by first identifying the high-level systems that comprise each of the three categories. Examples of systems included in the FTM category are transmission lines, natural gas power plants, and substations. For each system, we list the components that comprise that system. For instance, natural gas power plants include several components, such as generators, gas turbine system, exhaust system, fuel supply system, boiler, and cooling system.

Our inventory of critical components has the following limitations. First, the systems, components, and subcomponents are not granular enough to list the raw materials needed for the build-out of the electric grid, such as steel or concrete. Second, the inventory is meant to be general and not specific to a particular electric grid or project. For example, some electric utilities may not rely on some power generation sources, such as hydropower, and some data centers may not use certain backup power systems, such as UPS batteries. Lastly, novel backup power and generation solutions may not have a standard approach, and the components that comprise those systems may vary. We attempted to obtain feedback from industry and government stakeholders; engagement was more limited among industry equipment providers than among government stakeholders. $^{28}$ The feedback received was addressed and incorporated accordingly, noting individual component recommendations.

## Front-of-the-Meter Systems and Components

The FTM components are categorized into two groups: Transmission and Generation. The components included in the Transmission group are ones that comprise the network of infrastructure used to transmit high-voltage electricity from power generation facilities to substations at demand centers. The components included in the Generation group are ones that comprise the infrastructure systems used to convert energy sources (e.g., natural gas, coal, wind, water) into electrical energy that is fed into the transmission substation. The distribution system components are not considered in this report, since most frontier AI data centers are likely to connect directly to the transmission system, driven by either regulation or power transmission constraints. $^{29}$ Across both generation and transmission, we identified 16 systems, as listed in Table 3.1, that would be needed for the FTM build-out of electric power infrastructure used for AI data centers.

Table 3.1. High-Level Overview of FTM Systems


When developing the inventory of the FTM components, our goal was to identify components that would be most critical for AI data centers. Given that AI data centers are energy-intensive facilities (i.e., consuming megawatts of electricity) and require a reliable and uninterrupted supply of electric power of 99.995 percent for the highest reliability standards, $^{30}$ nearly all components that would be used for the build-out and expansion of the electric grid would also be critical for AI data centers. For example, to meet the electricity needs for AI data centers, development of new generation systems and expansion of existing power generation infrastructure will be required. At the same time, components that support grid reliability and transmission of high-voltage are also critical; therefore, components such as high-voltage transmission lines, substations, and controls systems are needed. It is important to note that the FTM inventory is intended to be inclusive of all geographic locations where the development of AI data centers is planned. For example, electric utilities in Texas rely more on natural gas and wind, therefore systems and components pertaining to hydropower generation are not likely to be relevant in that region. However, in other regions, such as California, hydroelectric power represents approximately 15 percent to 20 percent of the electric power capacity, and therefore components and systems pertaining to hydropower generation would be relevant.

## Behind-the-Meter Systems and Components

BTM refers to the components that fall under the data center's primary responsibility (i.e., all assets from the point of grid interconnection through the server infrastructure). BTM electric components play a crucial role in maintaining adequate power to allow the graphics processing units (GPUs) and servers to operate as intended and maximize their performance or operating life. Frontier AI requires operation at an extremely high level of reliability. This reliability is typically achieved through multiple levels of redundancy. Therefore, supply chain vulnerabilities for the components could significantly influence the feasibility of potential future frontier AI projects, and establishing the appropriate component inventory and level of granularity is crucial.

We developed the BTM component list based on findings from the literature and from industry expert elicitation during previous RAND research. Using this industry feedback, we further developed the inventory by including backup generation sources, such as small modular nuclear reactors and fuel cells, that have garnered attention due to supply chain bottlenecks and delays in grid interconnections.

The components were grouped based on their primary function into the following groups: backup or supplemental power generation (i.e., BTM power generation), power management equipment, power transfer equipment, thermal management equipment, substation components, transformers, and other data center supporting equipment (see Table 3.2). Although this grouping can describe any data center, larger capacity generation, the need of various levels of power transformers and additional power smoothing, and reliability of the components are characteristic of frontier AI scale data centers.

Table 3.2. High-Level Overview of BTM Systems


The levels of reliability and scale of these data centers lend themselves to the use of microgrids in some instances. Microgrids are defined as a group of interconnected generation and load points within a clearly defined electrical boundary differentiating themselves by the local nature of the network. Typically, microgrids are expected to have the ability to island themselves and serve as a single controllable entity from the grid's perspective. $^{31}$ From an electrical component standpoint, a microgrid leverages the components already listed for BTM systems and might integrate some from FTM systems. $^{32}$ Microgrids could operate in alternating current, direct current, or a hybrid of the two, the implementation of any of which requires careful consideration and design to maintain the power reliability requested by frontier AI data centers. $^{33}$

## Bridge Power Systems and Components

Because of the rapid growth of AI data centers, grid interconnections can be a bottleneck, with connection times taking up to seven years. Under such circumstances, temporary power solutions, also known as BP solutions, have emerged. These systems use properly sized generation to meet demand and, in some cases, involve building up a microgrid to support the generation infrastructure and leverage multiple generation sources. Although BP systems are meant as temporary, they leverage the same components as those used in BTM or FTM systems and therefore do not have their own dedicated component list. They could be composed of BTM power generation components or some of the FTM generation systems, such as geothermal power generation, if conditions are favorable. $^{34}$ Examples of typical generation leveraged include small modular generators, larger higher efficiency dual fuel turbines, energy storage, and solar. After the data center has achieved grid connection, the BP systems could be removed, be recommissioned as grid generation, or undergo a partial transition to permanent equipment to support as backup power. $^{35}$

## Benefits of Inventory Development

The inventory of critical components for FTM, BTM, and BP systems serves two main functions. First, the inventory is used to estimate and evaluate potential supply chain vulnerabilities through quantitative metrics, as described in more detail in the next chapter. Second, the inventory helps to identify components that overlap between FTM, BTM, and BP systems. This distinction is important because components that are critical across multiple system types may face heightened supply chain vulnerability due to increased demand and competing procurement priorities. In such cases, electric grid operators and data center operators may compete for the same components. Competition among multiple stakeholders for the same component may influence component pricing dynamics. This phenomenon has been documented in such industries as automotive manufacturing. For example, consider semiconductors, which are used for UPS and power distribution systems in data centers and in automotive power electronics. Large volume purchases of semiconductors at premium prices by data center operators have constrained the supply of this component for other sectors, such as the automotive industry. $^{36}$

Supply chains are critical for ensuring the reliable provision of the critical components defined in Chapter 3. From a procurement perspective, reliable supply of these components depends on supply chains that are characterized by a steady flow of goods, predictable pricing, and dependable sourcing to meet demand and support project needs. On an ongoing basis, reliability in supply chains ensures supply resilience and mitigates procurement challenges that result in project delays, operational disruptions, and budget overruns. More acutely, supply shocks materializing from logistic disruptions, natural disasters, disease outbreaks, critical input shocks, productivity shocks, changes in commodity prices, shifting trade policy, changes in labor supply, and increased demand competition can lead to negative impacts on supply availability and costs. $^{37}$ The impact of these shocks depends on the level of exposure to the shock, the magnitude of the shock, and existing vulnerabilities in the supply chain.

Vulnerabilities in the supply chain are likely to correlate with either unfavorable levels of or unexpected changes in substitutability, supplier concentration, volume flows, and pricing that make the supply chain less robust or less reliable in the face of supply shocks or increasing demand. Therefore, monitoring these levels or detecting changes in supply chains can help identify and anticipate vulnerable areas to address to ensure supply resilience.

In the analysis in this chapter, we identify and quantitatively assess international supply chain vulnerabilities across the critical components, developing metrics that track corresponding aspects of vulnerability and introducing a weighted composite indicator to flag particularly vulnerable components based on trends. The activities we performed were as follows:

\- Indicator Identification: For supplier concentration, we track market concentration; for volume flows, we track volume volatility; and for pricing, we track price volatility. We also added an indicator to detect changes in the flow of imports to capture shifts in overall trade that could affect or signal declining supply availability.

\- Quantitative Assessment: We compared metrics across years to assess how vulnerabilities are becoming more or less significant across time, surfacing pain points that require attention. The vulnerability assessment is set up in such a way that vulnerability could be tracked and updated from year to year into the future.

\- Visualization: The assessment and key findings are summarized in this chapter. We developed heat maps of vulnerability that allow easy visualization of vulnerabilities across indicators and across electrical components and systems, which we include in Appendix C.

Successful procurement of components can depend on import supply, domestic sourcing, and demand competition. As demand for U.S. power surges by 116 percent and domestic manufacturing faces challenges in keeping pace, $^{38}$ imports are playing an important role in supply. $^{39}$ For example, in 2024, domestic manufacturing only met 20 percent of U.S. demand for transformers; $^{40}$ in 2025, imports were estimated to account for 80 percent of U.S. power transformer supply. $^{41}$ Our analysis focuses on imports, using the most suitable publicly available source for tracking international flows into the United States. Future iterations of this framework could add demand and domestic sourcing data when available to obtain a more holistic picture of supply chain issues, especially where international supply chains remain stable but supply chain challenges emerge primarily from changing demand pressures.

## Methods for Examining Supply Chain Vulnerability

To assess supply chain vulnerabilities, we developed a quantitative framework that systematically evaluates trade patterns related to each component over time and then compares the relative risk across components. This includes identifying relevant trade codes for tracking the movement of components where possible and calculating indicators to assess vulnerability based on flows in volume and monetary value. The indicators are calculated for each component in each year and then compared with other years to detect unexpected changes in the supply that might signal increasing vulnerabilities and decreasing reliability in the supply chain. An example of how this calculation is applied to a component is included in Appendix C.

## Data

In our assessment, 172 of the critical components defined in Chapter 3 (63 FTM and 109 BTM components) were matched to economic trade codes using the HTS sourced from the U.S. Census and managed by the USITC. $^{42}$ Although these codes capture only the movement of goods between countries—essentially a subset of the supply chain—they also represent the best publicly available data suited for this analysis. Some organizations are making attempts to achieve higher quality data that capture more segments of the supply chain, to varying degrees of reliability, as part of a growing field of supply chain intelligence. $^{43}$ These data can be useful, for example, for firm-level supply chain analysis; however, for the goals of our research question, these data are not suitably exhaustive. As a result, our overall approach provides a view of the cross-border movement of the systems, the components, and their component parts that is translated into indicators reflecting where the greatest supply chain vulnerabilities may be faced.

HTS trade codes are ten-digit codes used by U.S. Customs and Border Protection (CBP) to determine applicable duties, taxes, and tariffs on imported goods, whereas Schedule B codes are the ten-digit classification codes used by the United States to categorize and track exports, serving as the export counterpart to HTS codes. Both code systems share the same structure in which the first six digits align with the international Harmonized System codes and the last four digits are specific to the United States. The primary purpose of these codes is to manage customs; calculate fees, duties, and tariffs; and monitor cross-border trade. We harness their capabilities for statistical purposes. This presents a need to strategically identify the components across as many as 38,698 available codes, depending on the source.

## Matching Components to Trade Codes

Figure 4.1 demonstrates the process of matching HTS codes to the critical components identified in Chapter 3, relying on three sources: the International Trade Administration (ITA) Energy Trade Database, $^{44}$ the USITC HTS code database, $^{45}$ and USITC Customs Rulings Online Search System (CROSS) database. $^{46}$ The process applied after identifying critical components begins with the ITA Energy Trade Dashboard, which maintains 589 HTS import classifications, as well as 385 Schedule B export classifications related to the energy sector. The dashboard was built to track the movement of what the ITA considers primary energy, energy equipment, and materials for battery supply chains. The list offers a strong starting place for identifying codes but was developed for its own purposes and with its own assumptions, so we adopt it for our purposes and build on it. We expand on the list with a manual search through the USITC HTS code database with a particular focus on components left unmatched by the universe offered from the ITA dashboard. $^{47}$ Finally, for clarification and validation, we rely on the USITC

CROSS rulings database, which publishes binding classification rulings and corrections issued by CBP in publicly available correspondence with importers for specific goods and services for customs and duty purposes. This results in an exhaustive list of HTS codes for each critical component, which provides the basis for extracting trade import data to calculate our metrics.

In some cases, more than one HTS code is matched to a critical component based on inclusive criteria. For example, some transformer categories in the critical components accommodate a range of transformer categories that are differentiated by voltage in the HTS code database, or a device used for monitoring falls under a broader family of goods identified in the HTS code database. Multiple HTS mappings increase analytical complexity but give a more comprehensive view of supply chain dependence than relying on a single code. They make it possible to identify vulnerabilities across all products that can perform each component's function in the power grid.

Figure 4.1. Process for Matching HTS Codes to Critical Components

[[KC_IMAGE_003]]


## Calculating Indicators

Supply chain vulnerability manifests through multiple dimensions. A component's supply chain may be structurally vulnerable due to high supplier concentration, while another might face risks from upside price or downside volume volatility or the accumulation of a backlog of imports over time. As opposed to pure price or volume volatility, upside and downside volatility capture volatility that could tighten supply. This is the tendency for supply or prices to move in an adverse direction, such as falling import volumes or rising prices that signal increasing strain or unreliability in the supply chain.

To explore how different characteristics of supply may contribute to a component's supply chain vulnerability, we compute four metrics to capture how key characteristics trend over time. The metrics are calculated based on monetary and volume flows captured in the USITC

DATAWEB database, which tracks quarterly import data for the United States for HTS codes. $^{48}$ The calculated metrics are described below and summarized in Table 4.1:

\- Market Structure and Concentration: We develop two metrics to explore market structure and concentration. First, the Herfindahl-Hirschman Index (HHI) of market concentration is commonly used in the trade literature, academic research, and industry analysis to assess how concentrated imports are across supplying countries. Higher HHI values mean that a shock in one or two exporting countries could sharply affect availability and could structurally be more exposed to disruption. The metric is calculated by squaring and summing the percentage shares of each HTS code by country, producing an annual concentration index that is then aggregated by value-weight to the component level. The equation below shows that HHI for each component k is the average of the sum of squared market share s for each country c in year t for each HTS code h. $H_{k}$ is the respective count of HTS codes matched to critical component k.

$$
M a r k e t c o n c e n t r a t i o n = H H I _ {k, t} = \frac {1}{| H _ {k} |} \sum_ {h \in H _ {k}} \sum_ {c \in C} s _ {h, c, t} ^ {2}
$$

Second, we calculate the number of distinct countries providing imports in a given year based on observed positive trade flows and then aggregate to the component-level with value weights. This complements the HHI because when a component is sourced from many countries, a disruption in one or two locations has more potential to be offset or absorbed by alternative supplying countries. It adds a view into the breadth of supplying that could be used to substitute or diversify sourcing. A shrinking set of source countries may indicate increasing concentration and emerging supply vulnerabilities even before HHI or prices fully react.

\- (Downside) Volume Volatility: Downside volume volatility measures the risk of supply contraction, or how much import volumes fall below their typical levels over time. Rather than treating all fluctuations equally, this metric focuses only on negative deviations from the mean, capturing the extent to which import quantities drop relative to their recent average. For each HTS code, annual total quantities are calculated, and a three-year rolling window is used to compute the downside semivariance, or the average squared deviation of values below the mean. The square root of this semivariance is then divided by the mean to form a coefficient of downside variation (CDV), which is averaged to the component level. The equation below shows the calculation for each component $k$ , where $\sigma$ is the downside standard deviation in import volume and $\mu$ is the average import volume for HTS $h$ over a three-year window before year $t$ . $H_{k}$ is the respective count of HTS codes matched to component $k$ . High downside volatility indicates that import volumes frequently fall below expected levels, complicating forecasting, inventory planning, and contracting. This can result in procurement challenges, such as stockouts, costly overstocking, or backlogs in supply in response to continuous or increasing demand.

$$
D o w n s i d e v o l u m e v o l a t i l i t y = C D V _ {k, t} = \frac {1}{| H _ {k} |} \sum_ {h \in H _ {k}} \frac {\sigma_ {h , t}}{\mu_ {h , t}}
$$

\- (Upside) Price Volatility: Upside price volatility measures the risk of price spikes, or how much import prices rise above their typical levels over time. Like downside volume volatility, it uses a semivariance approach but focuses on positive deviations from the mean (price increases). For each HTS code, annual average unit prices are calculated, $^{49}$ and a three-year rolling window is used to compute the upside semivariance, or the average squared deviation of prices above the mean. The square root of this semivariance is divided by the mean to form a coefficient of upside variation (CUV), which is then averaged to the component level. The equation is analogous to that for volume volatility but substitutes unit price for import volume. High upside price volatility indicates that prices frequently spike above expected levels, exposing energy projects to budgeting risk, contract renegotiations, and potential delays. Large price swings often coincide with underlying physical or policy stress in the supply chain.

\- Import decline: This indicator is designed to capture actual or potential constraints in a supply chain by measuring supply declines. The metric sums annual quantities per HTS, calculates year-over-year quantity changes, sums negative changes, then aggregates to the component level. Persistent or sharp declines in import volumes for a component suggest that something in the supply chain is tightening: for example, demand being rationed, orders canceled, or upstream production constrained. Tracking import decline helps flag components at the point at which the physical flow of goods is shrinking, which can precede shortages, backlogs, or longer lead times even if prices have not fully adjusted yet.

Table 4.1. Description and Interpretation of Vulnerability Metrics


$^{49}$ Unit values are used as a proxy for unit prices by dividing the value of imports by the volume of imports when pricing data are not readily available.

After calculating the metrics for each component, we discuss in the next section how metrics are transformed and combined to assess overall vulnerability. As the only metric for which a higher value represents less vulnerability, we invert our interpretation of overall vulnerability before combining it with the other metrics to maintain a consistent logic in assessment. An example applying the calculations to a metric is included in Appendix C.

## Assessing Vulnerability

Supply chains are characterized by the movement of goods over time. Vulnerability emerges when the pattern for a component diverges from what is expected or “normal” for a component. To support strategic planners and policymakers, this assessment focuses on time trends in vulnerability from January 2016 to December 2025, capturing how abnormal each component’s behavior is relative to its history and which characteristics contribute most to that abnormality. We chose this time frame to ensure a period long enough to capture multiple shocks and structural shifts, including trade policy changes, pandemic disruptions, and energy market shifts, so that abnormalities can be benchmarked against a recent history rather than a single episode. In addition, a decade of data provide sufficient observations per component to support reasonable statistical stability while still reflecting on recent sourcing patterns.

We create a composite vulnerability score by calculating z-scores for each metric for each component that describes the relative ranking of each year compared with other years. The composite vulnerability score is essentially a single overall “abnormality” score. The z-scores are a measure of how many standard deviations that value of metric is above or below an expected mean. All z-scores are scaled to a range between -3 and +3 to facilitate comparability across metrics and components. This scaling preserves the relative ranking of each component while preventing extreme values from dominating the composite score. To ensure directional consistency, all metrics are oriented so that higher z-scores indicate greater vulnerability. Metrics that naturally imply resilience when they increase (such as the number of importing countries) are inverted by multiplying their z-scores by -1. This ensures that all metrics contribute to the composite index in the same direction. Dynamic metrics (price volatility, volume volatility, and import decline) are given a time-based z-score comparing a value in a given year with a component’s history between 2016 and 2025. Static metrics (HHI and number of importing countries) are given a peer-based z-score comparing a value in a given year with the market structure of other components within the same year. We then combine these metric-level z-scores into a single composite z-score using predefined weights:

$$
Z _ {c o m p o s i t e} = \sum_ {i = 1} ^ {n} w _ {i} Z _ {i},
$$

where Z represents z-scores for each metric i, $w_{i}$ represents the designated weight for each metric i, n is the number of metrics, and $Z_{composite}$ is the composite vulnerability score.

The structural z-scores of HHI and importer count are weighed as one-quarter of the composite score (1/8, respectively), while the dynamic z-scores of price volatility, volume volatility, and import decline are each treated equally to detect instability and downturn detection in trade flows (1/4, respectively). Peer-based z-scores for the structural metrics HHI and number of importing countries are calculated relative to which side of the meter they are, rather than by subsystem. This allows us to compare overall relative vulnerability by energy system, as planners are likely to work with them. Time-based z-scores for the dynamic metrics import decline, volume volatility, and price volatility are calculated within-component, comparing a value in one year with a component's history. Metrics are calculated, compared, and analyzed for components within the context of FTM and BTM systems separately. Figure 4.2 represents the composite vulnerability indicator calculation more explicitly.

Figure 4.2. Composite Vulnerability Indicator Calculation

[[KC_IMAGE_004]]

\* z-scores for structural metrics are calculated on a peer basis, comparing values across components in a given year
\*\* z-scores for dynamic metrics are calculated on an time basis, comparing values in a given year with other years

The composite vulnerability score detects changes in the changing character and reliability of a component's supply chain. The weighting aims to flag how sourcing of components is becoming more unstable or unpredictable over time while still elevating poor substitutability and market concentration as an issue. Appendix C includes a weight-sensitivity analysis on the FTM components, showing robustness in outcomes when correlating to an equal weighting strategy (Table C.4).

The composite z-score acts as a vulnerability index, summarizing how unusually stressed each component's supply chain looks relative to its historical pattern, as well as structurally compared with other components. This method captures how supply chain vulnerabilities are more or less concerning this year compared with a component's baseline. A high z-score implies a component's supply could be more at risk to shocks or facing unexpected constraints, signaling a problem that may warrant monitoring and early intervention.

## Other Limitations

The assessment and results are largely shaped by data availability, quality, and structure. Several critical assumptions and uncertainties shape this analysis. First, trade data capture only terminal links in supply chains, which potentially underestimates true dependencies. By relying on USITC trade data, the analysis uses the most suitable publicly available source for tracking international flows, but it effectively infers vulnerabilities by goods that cross borders. This omits intrafirm trade, domestic production, stockpiles, and non-U.S. sourcing that manufacturers may rely on as buffers. High-quality data on these other forms of supply would meaningfully complement the analysis and clarify where alternative sourcing or inventories could offset identified vulnerabilities. At present, the North American Industry Classification System (NAICS) production dataset is the best available U.S. production source, but it is not granular enough to reveal component-level trends. In addition, the trade data used, which track sources by country, may effectively mask transshipments or imports diverted to evade tariffs or other trade barriers, obscuring indicators measuring market power, such as HHI and the number of importing countries.

Second, data structure introduces limitations. When trade codes are applied to shipments, they can range from highly specific to broad catch-all families of goods, often mixing items used in the power system with other applications. Because these codes underpin how component movements are observed, the accuracy of trade-code-to-component mappings directly affects the ability to trace supply chains specific to the power grid. For example, several HTS codes have been created that specifically identify wind energy components, such as hubs, generators, gearboxes, and towers. In contrast, natural gas turbines are distinguished only by aviation versus non-aviation use, despite their importance in power generation. Because HTS codes are primarily designed for duties, taxes, and tariffs rather than system relevance, more-granular codes based on power sector characteristics—such as voltage class, size, material composition, or functional role—would improve traceability and support a more precise vulnerability assessment.

Third, the customs and bill of lading process involves corrections, retractions, and reassignments of HTS codes, quantities, and values, affecting data quality. The published series can contain zeros or missing entries that bias analysis toward more actively traded codes. Additionally, reported unit prices embed currency movements, duties, and freight, so price volatility can be a noisy proxy for underlying cost risks. These limitations underlie the motivation for using a more holistic vulnerability framework that combines several metrics rather than relying on a single indicator to flag or explain vulnerabilities. Despite these limitations, this framework provides the most comprehensive systematic assessment of grid-wide supply chain vulnerabilities feasible, given available data. Future iterations of this work could be strengthened by

\- integrating grid-specific operational data, such as installation lead times, failure rates, and functional substitutability across components

\- conducting supplier audits, capacity surveys, and stress tests, which could also include such analytical approaches as probabilistic forecasting, scenario design, and evaluation of mitigation strategies, linking trade-based indicators more directly to system reliability and resilience outcomes.

## Results and Findings

In this section, we present general findings across all of the components and all years, as well as findings for specific components of interest, including those related to transformers, turbines, and batteries. For general findings, we reflect on patterns in z-scores for metrics across the ten-year time frame $^{50}$ . This informs a big-picture understanding of vulnerability dynamics across the energy sector over the past ten years, separating findings based on FTM and BTM systems.

For a deeper analysis, we choose specific components and reflect on the most recent dynamics from 2023 to 2025. Here, we demonstrate the value of the assessment framework in its ability to explain recent levels of vulnerability for specific components. For the specific component findings, we focus on components in the turbine, transformer, and battery category given their key role, discussed in Chapter 2, in generating electricity (turbine), storing electricity (battery), and transmitting it (transformer). Comprehensive heatmaps for all 172 components, categorized by energy system, are included in Appendix D.

## General Findings

This section is organized around figures and tables that present component-level and aggregate-level analyses for the FTM and BTM to explore different angles of vulnerability across components. We begin each subsection with a heatmap showing component-level annual trends by metric. Then, in an aggregate-level analysis, we identify shares of components experiencing the same vulnerability point to systemic shocks in which entire supply chains are simultaneously exposed to the same event. At the same time, what explains vulnerability for individual components can be unique, requiring different types of intervention. Each subsection ends with an analysis of the components with the highest-ranking composite vulnerabilities.

## Front-of-the-Meter Findings

In this section, Figure 4.3 presents a heatmap of the calculated annual z-scores for each component among the Generation and Transmission categories, ordered by 2025 composite vulnerability scores, with components experiencing the most acute supply chain stress at the top. Figure 4.4 follows, summarizing the aggregate annual trends in metrics across all components, while Tables 4.2 and 4.3 present a deeper dive into composite scores for the top-ranking vulnerable components in 2025.

## Aggregate Findings

From left to right, Figure 4.3 presents the composite score for each component, with each following panel presenting the decomposition of import decline, volume volatility, price volatility, HHI, and number of importing countries, respectively. Notably, HHI and the number of importing countries remain relatively the same color (green for low vulnerability, white for neutral, and red for high vulnerability) over time, while import decline, volume volatility, and price volatility are more dynamic over the same period. This dynamic supports the logic used to determine relative vulnerability.

The Figure 4.3 heatmap illustrates how the composite score draws from different metrics. Highly concentrated supply chains have less flexibility to absorb demand shocks or adapt to changing market conditions, making them more susceptible to dynamic disruptions over time. For example, steam turbines, geothermal production wells, and gas turbines are among components with the highest composite vulnerability scores in 2025. The high HHI and low number of import countries also show a greater dependence on a few countries. In general, market concentration is applicable to a higher proportion of generation components versus transmission components. This could reflect fundamental differences in market structure in which transmission equipment represents an established, standardized technology with more-diversified supplier bases, whereas generation components often involve more-specialized manufacturing methods and frequently evolving requirements, resulting in more limited production sources and higher barriers to entry for new manufacturers. As discussed in greater detail later in this chapter, this is particularly visible for battery chemistries and technologies, as opposed to more-assembled battery management systems.

Figure 4.3. Vulnerability Map for FTM Components

[[KC_IMAGE_005]]


[[KC_IMAGE_006]]

NOTE: The “Production Well” entry on the previous page refers to geothermal production wells.

Figure 4.4 presents the proportion of components that are exposed to various levels of vulnerability, by metric from year to year. Vulnerability levels correspond to the heatmap in Figure 4.3, with high vulnerability signified by red, low vulnerability by green, and neutral vulnerability or not enough data in gray.

The most prominent observation in Figure 4.4 is that temporal patterns from 2019 to 2020 show peak composite vulnerability across components in both categories. Composite vulnerability appears to peak, particularly among transmission components, in 2019. High volume volatility in 2020 indicates synchronized import disruptions aligned with well-known pandemic-era trade shocks. Broad exposure to price volatility shows a lag in effect, peaking in the wake of the pandemic in 2021. Import decline becomes a less critical vulnerability between 2021 and 2022, likely as supply bounces back. The common patterns across generation and transmission components suggest a broad-based supply chain shock affecting categories rather than isolated disruptions during onset and recovery of the pandemic. In contrast, vulnerabilities from 2016 to 2018 and 2022 to 2025 appear less systemic, with individual components experiencing vulnerability affected by more diverse sources of vulnerability.

In 2025, vulnerability systematically creeps up among generation components (38 percent high vulnerability) compared with transmission components (22 percent high vulnerability). The higher vulnerability appears to be correlated to price volatility, volume volatility, and higher levels of market volatility. This reinforces the fundamental market structure. As pandemic shocks alleviate and demand for components increase, generation equipment with specialized manufacturing techniques have more limited production sources and may take longer to recover.

Figure 4.4. Aggregate Trends in Vulnerability for FTM Components

[[KC_IMAGE_007]]


## Top-Ranking Components

Table 4.2 presents the components with the highest-ranking scores for generation in 2025. Steam turbines (1.21), geothermal production wells (1.11), and solar panel parts (0.93) rank at the top. From 2023 to 2025, these components appear to be increasing in vulnerability, especially among solar panel parts, which have below average levels of vulnerability in 2023 and 2024. Battery technologies and chemistries (0.49) also rank relatively high in 2025 but show more variation in 2023 and 2024.

Table 4.2. Highest-Ranking Critical Components for Generation, by Composite Vulnerability in 2025


$^{b}$ The HTS codes used to define nacelles and other wind energy–related parts include shared classifications across related products.

Table 4.3 presents the top-ranked transmission components. Conductors and wires (0.72), transmission lines (0.72), and reactive power compensation (0.41) show the highest 2025 composite vulnerability. At the same time, a greater proportion of transmission components have more moderate scores compared with generation.

Table 4.3. Highest-Ranking Critical Components for Transmission, by Composite Vulnerability in 2025


$^{a}$ The HTS codes used to define conductors, wires, and transmission lines include shared classifications across related products.

Altogether, the FTM findings show that policy interventions should prioritize addressing vulnerability among generation supply chains, given their strategic importance and more acute vulnerability. Components showing both high structural concentration (persistent red in HHI) and high 2025 composite vulnerability are at risk of facing compounding and cascading risks in which a disruption in one location can affect supply for many entities. In Chapter 6, we discuss how the character of supply chain vulnerabilities could inform strategic priorities. Such priorities can include diversifying sourcing for affected components, incentivizing domestic manufacturing capabilities, and exploring alternative technologies or materials that could reduce dependence on the most vulnerable supply chains. However, some strategies may be more or less appropriate given the duration, intensity, and structure of a disruption.

## Behind-the-Meter Findings

In parallel with the FTM findings, Figure 4.5 presents a heatmap of the calculated annual z-scores for each component across the BTM systems. The chart is similarly ordered by composite vulnerability scores, with components experiencing the most acute supply chain stress in 2025 at the top. Figure 4.6 summarizes the aggregate annual trends in metrics across all components, and Table 4.4 presents the top-ranking BTM vulnerable components in 2025.

## Aggregate Findings

Figure 4.5 presents a heatmap across BTM components. A higher proportion of backup power components are shaded in red at the top of the ranking, revealing that supply chain vulnerability in 2025 is not evenly distributed. This category includes advanced materials and specialized energy storage technologies. These components also appear to be more vulnerable to market concentration risks. The HHI and number of importing columns reveal that a few countries dominate the market, particularly for fuel cell–related components, turbines, and generators.

Figure 4.5. Vulnerability Map for BTM Components

[[KC_IMAGE_008]]


[[KC_IMAGE_009]]


Figure 4.6 shows the aggregate trends in the proportion of components that are exposed to various levels of vulnerability by metric from year to year. Vulnerability levels correspond to the heatmap in Figure 4.5, with high vulnerability signified by red, low vulnerability by green, and neutral vulnerability or not enough data in gray. Across these components, a higher level of components appear to be exposed to vulnerabilities in the first half of the decade, driven by high levels of declining imports. Price volatility appears prevalent from 2016 to 2017. Similar to trends in FTM components (Figure 4.2), volume volatility appears alongside peak vulnerability from 2019 to 2020 during the pandemic. Composite vulnerability across components appears to diminish from 2021 to 2024.

Figure 4.6. Aggregate Trends in Vulnerability for BTM Components

[[KC_IMAGE_010]]


Table 4.4 presents the 15 most vulnerable BTM components assessed by 2025 composite vulnerability. Two-thirds of the most vulnerable components are associated with the backup power system, followed by almost one-third associated with power management, and one component out of 15 associated with power transfer. Metering components, cables, tanks and valves are among the most vulnerable components. Each of these components has been steadily growing in vulnerability over time.

Table 4.4. Highest-Ranking BTM Components, by Composite Vulnerability in 2025


$^{a}$ The HTS codes used to define cables and medium voltage cables include shared classifications across related products.

Altogether, these findings indicate that BTM energy supply chains face acute challenges with vulnerability, particularly in terms of backup power and power management technologies. In some cases, where import vulnerability appears high or data are missing—such as with fuel cell technologies and industrial gas turbines—it should be noted that U.S. companies play an important role in the market, demonstrating how domestic manufacturing data could complement this analysis. Nonetheless, the assessment illustrates how international sourcing is evolving.

## Specific Findings

In this section, we provide further details on three key component types related to transformers, turbines, and batteries in the FTM and BTM contexts. The analysis is used to explain existing or emerging supply chain challenges to components and to demonstrate the value of the supply chain vulnerability assessment framework. At a component level, the framework demonstrates how effective supply chain resilience strategies should be tailored to a specific vulnerability profile: for example, addressing structural concentration where it exists while developing responsive mechanisms to manage volume instability and import decline in other cases. Although the results show z-scores from 2023 to 2025 for conciseness, we made

calculation comparisons across the past ten years, from 2016 to 2025. A summary of z-scores for all 172 components by system type across the BTM and FTM systems is included in Appendix D.

## Transformers

Figure 4.7 shows vulnerability for transformer-related components from 2023 to 2025. In 2025, large power and potential transformers have the highest composite vulnerability score among FTM and BTM transformer-related components, respectively. However, the level of vulnerability reflected among z-scores is low relative to other components. Transformer imports are increasing in 2025, as denoted by the green values. Yet the demand for pole-mounted distribution transformers, for example, have seen surges by 41 percent, $^{51}$ implying supply chains are facing overwhelming demand pressures even if they appear stable. These findings demonstrate the potential value of expanding this framework to include demand and domestic supply chain data to get a full picture of what is affecting procurement challenges.

The modest elevation in 2023 or 2024 appears driven primarily by temporary volume volatility, but these spikes resolve by 2025. The negative import decline metrics suggest that imports of transformers are likely increasing in response to growing demand. For example, voltage and current transformers demonstrate relief in supply chain vulnerabilities over time with composite scores of 0.88 in 2023, 0.15 in 2024, and -0.75 in 2025, and large power transformers show composite scores of 0.50 in 2023, 0.44 in 2024, and 0.19 in 2025. Both types of transformers appear to experience notable volume volatility in 2023 and 2024, but increases in imports appear to relieve supply challenges to an extent. Large power transformers appear to come from a few countries without one country necessarily dominating the market (signified by relatively green HHI values).

Figure 4.7. Vulnerabilities for Transformer-Related Components for FTM and BTM


## Turbines

Figure 4.8 presents how vulnerability changes across metrics for turbine-related components from 2023 to 2025, showing more-concerning trends in which multiple factors simultaneously contribute, particularly among FTM components. Across both sides of the meter, turbines have positive composite vulnerability in 2025. Steam and gas turbines (including specialized aeroderivative, radial, micro, and industrial) are among the most vulnerable turbine-related components. For FTM gas turbines, a simultaneous decline in reported imports (1.86 in 2025) and an increase in volume volatility (1.97) appear to contribute. For BTM, radial gas, micro, and industrial gas turbines are defined by similar HTS codes. Underlying all turbine components, market concentration amplifies the possibility of these supply chain risks, with all but BTM gas turbine parts shaded in red. This suggests that supplier diversification may be an important mitigation strategy.

Figure 4.8. Vulnerabilities for Turbine-Related Components for FTM and BTM


## Batteries

Figure 4.9 presents the vulnerability scores across battery-related components from 2023 to 2025. Battery supply chains present a relatively stable vulnerability landscape, with most components operating near or below historical stress levels in the 2023–2025 period compared with prior periods. FTM battery systems and BTM batteries experienced a high import decline and volume volatility compared with other years in 2023, but overall composite vulnerability appears to be neutral, suggesting temporary supply chain issues. Otherwise, supply chains for battery systems are characterized by low concentration and reasonable supplier diversity.

Further away from their assembled form, battery technologies and chemistries are an exception, experiencing a mix of import decline, volume volatility, price volatility, and market concentration over the same period. In 2023, import declines had a z-score of 1.62, and volume volatility had a z-score of 1.17. In 2025, price volatility appears at 1.76. HHI and the number of countries importing remain relatively high throughout the period. Many of these battery inputs represent raw materials that depend on certain countries for sourcing, explaining the high market concentration. Among other mitigation strategies, national labs are known to be partnering with industry to improve domestic sourcing and next-generation battery alternatives. $^{52}$

Figure 4.9. Vulnerabilities for Battery-Related Components for FTM and BTM


## Chapter 5. Assessing Supply Chain Risks for Frontier AI Data Center Expansion Using Case Studies

In Chapters 3 and 4, we discussed the components that are critical for the expansion of frontier AI data centers and the supply chain vulnerabilities of those components. Although vulnerability is an important factor in determining the susceptibility of a component to potential supply chain-related disruptions, it does not, on its own, provide a comprehensive characterization of supply chain risk. Using a framework described in risk management doctrine developed by the U.S. Department of Homeland Security, we examine supply chain risk as a function of the following three elements: threats, vulnerabilities, and consequences. $^{53}$ In the context of frontier AI data center expansion, we measure consequences through potential delays in the ability to procure selected components for FTM, BTM, and BP electric infrastructure. Using different threat scenarios as case studies, we examine how the delays in procurement of certain critical components will affect the completion rate of generation projects and therefore the ability of the electric grid to meet the power demand for frontier AI data centers. Our quantitative analysis is focused on grid-connected projects (FTM and BTM). For BP, we describe the potential impacts mostly qualitatively because of the limited availability of quantitative data. Figure 5.1 summarizes our approach. The analysis presented in this chapter contributes to the literature by introducing an approach to quantitatively estimate how supply chain risk could affect the ability for the United States to meet AI electric power demand.

Figure 5.1. Approach to Measure Supply Chain Risk

[[KC_IMAGE_011]]


## Estimating Consequences for Frontier AI Data Center Expansion

Several academic and industry sources describe a gap in the electric power supply to meet the required demand from AI data centers. A 2025 RAND report estimates that available capacity will increase to 82 gigawatts (GW) by 2030, indicating a generation shortfall in the United States' capability to power 158 to 253 GW of AI data center demand. $^{54}$

Potential supply chain–related challenges can exacerbate this shortfall and further increase the gap between the electric power required and the electric power expected to be provided. Using the results from the 2025 report, we performed a sensitivity analysis to estimate how delays in procurement of specific electric grid components can affect the completion of select electric power generation projects starting and ending in 2025 and 2030, respectively. We conducted the analysis for three components: transformers, natural gas turbines, and batteries. Although this analysis can be completed for other components, we selected these components because of the availability of open-source historical data on procurement delays.

We conducted the sensitivity analysis as follows: First, for FTM components, we determined which electric power generation projects would be affected by procurement delay of the component. We assumed that projects in progress (i.e., projects started before 2025) in the

interconnection pipeline will not be affected from procurement delays, and the impact will only be reflected in additional projects (i.e., projects started between 2025 and 2030). For natural gas turbines, we assumed that the delay would decrease the completion rates of natural gas generation projects. For batteries, we assumed that the delay will affect all hybrid projects (i.e., projects with renewable energy generation and storage) and projects with only electric power generation storage. For transformers, we assumed that the delay would reduce the completion rates of all generation projects because it would affect the interconnection process. If a project was affected by multiple delays from different components (i.e., natural gas turbine and transformers), we used the larger value of the delays (i.e., the worst-case scenario).

For the BTM analysis, we used a similar approach but specifically focused on the impacts to generation storage projects. Adapting a methodology from the 2025 RAND report, we examined how BTM generation storage projects would be affected by procurement delays of batteries. $^{55}$ As described in Chapter 3, batteries are one of many components used in both FTM and BTM systems, which has two implications. First, both projects, FTM and BTM, may compete for the same component. Second, BTM projects may experience similar procurement delays as FTM projects for selected components. We assumed that the delay in procuring batteries results in delays to the completion of BTM electric generation storage projects, which therefore further decreases the net available capacity of electric power to meet the required demand for AI data centers. $^{56}$ This approach can also be applied to other components not included in this analysis.

Next, we used open-source data and collected historical procurement delay data for the three components. In Table 5.1, we list the range delays for each component and types of electric power generation projects affected by delays in procuring those components.

Table 5.1. Historical Procurement Delays of Components


SOURCES: For natural gas, Diana DiGangi, “Georgia Power Receives Natural Gas Turbine as Delays Loom,” Utility Dive, August 21, 2025; for transformers, Morgan Bazilian and Kyri Baker, “Supply-Chain Delays, Rising Equipment Prices Threaten Electricity Grid,” The Conversation, November 14, 2025, and Chopra and Boucher, 2024; and for battery, Neeraj Arora, Mark A. Lazaroff, Thomas V. D'Ambrosio, and Maggie E. Curran, “A 2024 Update on Utility-Scale Energy Storage Procurements,” Morgan Lewis, March 4, 2024.
$^{a}$ The numbers in parentheses refer to the most recent delay range identified, while the maximum additional delays are the difference of the two values.
$^{b}$ Specific to BTM projects.

Lastly, for each case study, we used the corresponding delay data to perform a sensitivity analysis to estimate the impact on the completion rate of electric power generation projects. We accounted for the delays by modifying the forecast completion dates of the affected projects across three threat scenarios, which are described in further detail in the next section. The modification of the forecast completion dates of projects results in a decrease in the availability of net generation capacity for a given year. Because we assumed that all three scenarios only affected the completion time, we only accounted for decreases in net generation capacity and did not consider other impacts (e.g., delays in the completion or availability of transmission systems).

## Threat Scenarios Affecting Frontier AI Data Center Expansion

Supply chains are susceptible to multiple types of threats and adverse events, including man-made or natural disasters, economic disruptions from political actors, and uncertainty in market demands. $^{57}$ In the context of this analysis, we consider threats or adverse events that can affect the ability of the U.S. electric grid to meet the increasing electricity demand of frontier AI data centers by 2030. As discussed in several reports, the United States may not be able to meet the AI frontier data center energy demand by 2030, resulting in a shortfall of electric power generation. $^{58}$ Supply chain impacts can exacerbate these shortfalls and have different

implications depending on the type of threat and the component. In this section, we explore three types of supply chain threats: geopolitical, market or economic, and operational. Although other threats can be considered, we selected these three threats for the analysis based on historical evidence demonstrating their impacts on supply chain disruptions that affect electric grid infrastructure.

## Geopolitical Threats

Geopolitical supply chain threats are driven by political, strategic, or security-related actions and conditions between different countries or regions. These threats can manifest through various mechanisms, including trade barriers and sanctions, restrictions to inputs and resources, and shifts in international partnerships. $^{59}$ Recent examples include the Russian invasion of Ukraine, U.S. tariffs on imports from select countries, and Chinese export restrictions on select materials. The Ukraine conflict, for instance, resulted in an increase in demand for electric infrastructure components, such as transformers and substations. $^{60}$ The increased demand exacerbated the overwhelmed U.S. market for electric grid equipment, which extended procurement times for large transformers from six to 12 weeks in 2020 to 52 to 86 weeks in 2023. $^{61}$ Although these delays involved a combination of other factors beyond the Russia-Ukraine war, the procurement delays demonstrate how geopolitical threats can worsen market conditions for critical electric grid components.

## Market or Economic Threats

Market or economic threats are driven by market dynamics or economic conditions that affect the availability, cost, procurement, and timing of goods. These conditions affect the ability of suppliers to produce and deliver goods at a predictable cost. These threats can manifest in the form of price volatility, fluctuations in demand, financial constraints, and manufacturing limitations. $^{62}$ For example, consider the procurement of large power transformers. The production of large power transformers relies on raw materials, such as grain-oriented electrical steel, copper wire, and insulating material. The production of electric vehicles relies on non-oriented electrical steel, which is manufactured from the same facilities as grain-oriented electrical steel. Therefore, increases in demand and production of electric vehicles can influence the production and availability of electrical steel used for large power transformers. $^{63}$ This example demonstrates the different market or economic factors that can influence the production and availability of certain components that are critical for electric grid power.

## Operational Threats

Operational supply chain threats are driven by the inability to move, handle, or store goods. Examples include constraints in transportation, damage to storage and/or handling infrastructure, workforce constraints, and operational failures. These threats can manifest in the form of long lead times, higher costs, and changes to material quality. $^{64}$ The COVID-19 pandemic serves as an example to demonstrate how operational threats can adversely affect the supply chain of critical electric grid components. Labor shortages in manufacturing, warehousing, and shipping created constraints in the ability to produce and deliver components, such as transformers, as well as raw materials, such as electrical steel, aluminum, and copper, which are used in the manufacturing of these transformers and other electric grid components. $^{65}$

Across the three threat scenarios, the relative importance of supply chain vulnerabilities varies, resulting in some vulnerabilities influencing supply chain disruptions more than others. For instance, consider geopolitical threats. Factors such as the number of suppliers, the market concentration, and the geographic location of suppliers may have more significance than other indicators, such as price volatility. We considered a hypothetical scenario and mapped the supply chain vulnerabilities across the three threat scenarios using a binary classification to indicate which threats are most relevant for each component, as listed in Table 5.2. This binary classification was established based on an author-led qualitative assessment of the three threat scenarios, which was informed by historical impacts on supply chains for select electric grid components. Additionally, it is important to note that the mapping is based on direct linkages to the vulnerability indicators. In theory, all threat scenarios could indirectly be linked to all vulnerability indicators. For the purpose of this analysis, we chose to focus only on direct linkages.

Table 5.2. Mapping of Supply Chain Threats to Vulnerability Indicators


When calculating the delays for a given threat scenario using the supply chain vulnerability metrics, our approach was as follows:

\- Step 1. Map supply chain vulnerability metrics to threat scenarios (reference Table 5.2).

\- Step 2. Collect the normalized scores for each vulnerability metric (as described in Chapter 4) for a given threat scenario.

\- Step 3. Calculate an aggregated vulnerability score (referred to as the effective vulnerability score), which aggregates the historical scores by the vulnerability year index. Note: A higher weight is applied to the most recent data.

\- Step 4. Calculate the total vulnerability score by taking the sum of the effective vulnerability scores across each metric.

\- Step 5. Estimate the additional delay by prorating the maximum historical component procurement delay by the normalized total vulnerability score (Table 5.3).

Table 5.3. Equations and Variables to Calculate Component Delay Based on the Threat


NOTE: The vulnerability scores A1, A2, . . . , D2, D3 are calculated based on the identified z-scores from the vulnerability assessment, where the values were grouped into no impact, low, medium, and high with scores of 0, 1, 3, and 5, respectively. The range of no impact, low, medium, and high are based on the z-scores as follows: less than 0, less than 0.5, less than 2, and anything higher than 2.

To better illustrate the approach, we include an example calculation using the Market or Economic threat scenario for gas turbines:

\- Step 1. Using Table 5.2, we identify that the relevant vulnerability metrics for the Market or Economic threat scenario are Import Decline, Price Volatility, Volume Volatility, and HHI. This means that R1, R2, R3, and R5 are assigned a value of 1, and R4 is assigned a value of 0.

\- Step 2. We collect the z-scores for the relevant vulnerability metrics, as listed in Figure 4.8. In the example of gas turbines, the highest z-scores for the Price Volatility metric are 1.7, 2.17, and 1.46 for 2023, 2024, and 2025, respectively. Next, we assign a ranking of medium, high, medium for the three z-scores and assign numerical values of 3, 5, and 3. These values are assigned to the A1, A2, and A3 variables, respectively. We use the same process for the Volume Volatility, HHI, Import Decline, and Number of Countries vulnerability metrics. $^{66}$

\- Step 3. We calculate the effective vulnerability score using the equations in Table 5.3. For Price Volatility (T1), the effective vulnerability score is $14(3 + 5 + 3 * 2)$ . The effective vulnerability score for Volume Volatility (T2), HHI (T3), Number of Countries (T4), and Import Decline (T5) are 12, 18, 12, and 15, using the same process.

\- Step 4. The total score for gas turbines under this threat scenario is the sum of the effective vulnerability scores that apply (i.e., Price Volatility, Volume Volatility, HHI, and Import Decline). Therefore, the Total Score (TT) is 59.

\- Step 5. Assuming the maximum possible delay of two years and the total score of 59, we estimate a maximum additional delay for gas turbines due to a market or economic threat to be 14.2 months. We calculate this value by normalizing the total score of 59 by the maximum possible score of 100 and then multiplying by the maximum delay of two years.

## Supply Chain Impact

Although historical evidence confirms the occurrence of the three threats included in our analysis, accurately forecasting their likelihood remains challenging because of data limitations. Therefore, we considered supply chain risk under the assumption that these threats occur using three case studies. We used the range of procurement delay times identified by the rubric in Table 5.3 to quantify the impact of those delays on the net available capacity. We estimated a range of net available capacity by incorporating the additional delays calculated from the average vulnerability of the system and the highest vulnerability component for which we had high confidence of the supply chain matches. $^{67}$ In Tables 5.4 and 5.5, we present the results of this analysis for FTM and BTM, respectively. The variations in Net Cumulative Capacity display how the threat scenarios could affect the energy available to meet demand.

Table 5.4. Threat Scenario Impact on FTM Net Generation Capacity


$^{a}$ The base case was developed in Arciniegas Rueda, van Soest, et al., 2025.

Table 5.5. Threat Scenario Impact on BTM Effective Generation Capacity


$^{a}$ The base case was developed in Arciniegas Rueda, van Soest, et al., 2025.

## Key Findings

\- In our analysis of FTM components, supply chain–related threats have the potential to result in approximately a 7 percent to 31 percent decrease in available net capacity by 2030 with respect to the base case because of further delays in the procurement of natural gas components, batteries, and transformers. $^{68}$

\- In our analysis of BTM components, supply chain–related threats have the potential to result in up to an 8 percent decrease in available net capacity by 2030 with respect to the base case because of delays in the procurement of batteries.

## Impact for Off-Grid Systems

In this section, we discuss how supply chain challenges can also affect anticipated projects that are off-grid due to competition in procuring the same type of equipment considered for both FTM and BTM systems contributing to effective generation capacity. According to estimates from previous RAND research, there is a shortfall in power grid generation capacity in terms of the United States' capability to power 158 to 253 GW of expected AI demand by 2030. $^{69}$ The supply chain threats discussed in the sensitivity analysis above could result in an additional shortfall of 1 to 4 GW by 2027, increasing to 3 to 14 additional GW by 2030. $^{70}$

Data centers can consider an option to use electric power off-grid and meet their electric power needs using BP projects. Below, we discuss the implications of BP projects using examples for three critical components: natural gas turbines, transformers, and batteries.

## Natural Gas Turbines

BP refers to a temporary power source (usually natural gas) used to support a system during a transition period, such as electric power grid buildup or electric power grid maintenance. An alternative for BP generation demand is to use natural gas aeroderivative turbines. One study, for instance, reported that more than 400 MW of natural gas new generation demand come from data centers. $^{71}$ It is important to note that other alternatives to natural gas exist (e.g., geothermal).

If we assume that the estimated power gap in our projections are not met by the power grid but instead met with BP natural gas aeroderivative turbines, the additional demand can be calculated. Assuming no additional disruptions, we estimate that supporting data centers averaging 100 MW working with BP within the 2027 to 2030 period would require approximately 81 additional 110-MW turbines by 2027 and 1,554 110-MW turbines by 2030 (alternatively, 30-MW turbines would require 405 by 2027 and 7,770 by 2030) in the base case.

Under the threat scenarios, this would translate into a need of 91 to 123 110-MW turbines (or 451 to 611 30-MW turbines) by 2027 and 1,582 to 1,690 110-MW turbines (or 7,909 to 8,449 30-MW turbines) by 2030. $^{72}$ This demand side need on turbines will likely further stress supply chains and may lead to some of the data centers currently on the pipeline not being completed as planned. Therefore, there is an AI demand side impact of supply chain vulnerabilities that we do not address in this report and that will be an area of future research.

## Transformers

Large power transformers are required to step down power from high voltage to the medium voltage used in transferring power within the distribution network of the data centers. The power demand gap means that projects need to plan to operate with BP for some period. Projects

operating with BP can provide some flexibility for large power transformer demand, since they could start operating without their grid interconnection and could delay the completion of the interconnection.

In data centers, large power transformers are typically designed in the range of 50 to 100 megavolt-amperes (MVA) and have one more redundant transformer than required to service the data center. $^{73}$ The increase in the demand-generation gap of 10.2 to 13.7 GW by 2030 is equivalent to 204 to 273 larger 100-MVA transformers or 407 to 548 smaller 30-MVA transformers. Although these would account for less than 5 percent of the total data center large power transformer demand, it could be large enough to help decrease transformer lead times if the shortfall is taken to be flexible for BP-served data centers.

These observations do not hold true for other types of power transformers that have experienced increased lead times, such as medium-to-low-power step down transformers whose role is still important whether the data center is designed with interconnection or bridge power in mind. Therefore, going off-grid will not fully resolve the supply chain constraints on transmission electrical equipment for data centers. Transformer supply chain issues could also have an AI data center demand side that we do not address in this report and that is an area for future research.

## Batteries

Under any of the threats considered, the increased requirement of BP would also likely increase the need for energy storage to support the continuous operation of the data centers. Additionally, BP alternatives designed with intermittent energy sources would require additional storage capacity compared with their grid interconnected counterparts to guarantee a level of satisfactory continuous operation. This means that the need for additional BP could increase the demand for additional energy storage, which could further strain the supply chain.

Supply chains are a product of entities buying and selling goods from one another, so our recommendations focus on improving how these interactions are monitored, coordinated, and supported when vulnerabilities arise. Because supply chains are decentralized and largely governed by market forces, effective policy responses must balance private-sector flexibility with public-sector foresight in light of growing demands and must consider existing fragility from aging infrastructure and catastrophic events. The recommendations that follow translate the findings of our vulnerability assessment into actionable steps for DOE, the Federal Energy Regulatory Commission (FERC), the Department of Commerce, ITA, and industry partners. They aim to strengthen resilience by improving visibility into supply chain risks, clarifying decisionmaking processes, and developing targeted interventions. These recommendations range from a risk-tiered decision framework, to enhanced monitoring and data transparency standards, to building strategic reserves and domestic production incentives. Together, these measures provide a framework for proportionate, evidence-based action that supports both market efficiency and grid reliability.

## Recommendations

## 1. Implement a decision framework for responding to observed supply chain vulnerabilities.

DOE and FERC should adopt a decision framework for responding to observed supply chain vulnerabilities consistent with broader federal approaches to critical supply chain resilience, such as those modeled in provisions of the 2022 CHIPS and Science Act and DOE's Critical Materials Assessment. The framework would implement a risk-tiering logic by classifying electricity components into tiers of vulnerability based on quantitative metrics (e.g., HHI, importer count, volatility, import decline, composite z-scores) and linking each tier to proportionate policy responses.

This approach translates national resilience principles into component-level decision rules for the electricity sector by defining measurable criteria that trigger escalation from monitoring to targeted resilience investments to strategic intervention. It ensures that DOE and FERC can prioritize resources toward the most critical and most persistent vulnerabilities.

The analysis in Chapters 4 and 5 illustrates how each type of vulnerability uniquely contributes under different threat scenarios. However, temporal patterns are also important in determining the appropriate policy response or action. Four fundamental temporal patterns surface in the analysis:

\- Cyclical behavior patterns reflect typical industry and demand-supply dynamics that can be managed through standard procurement practices. These are characterized by regular volatility, project-driven fluctuations, and moderate z-scores that do not necessarily intensify over time. Routine monitoring may be sufficient until risk assessment flags concerning early warning signals.

\- Intermediate or sustained instability patterns represent components showing moderate but persistent volatility or import decline that could evolve into structural vulnerabilities if left unaddressed. These patterns warrant targeted resilience measures, such as supplier diversification programs, coordinated procurement pools, enhanced data collection, and time-limited incentives for domestic production or refurbishment capacity. These actions are designed to stabilize supply chains before vulnerabilities become structural.

\- Structural supply chain issues represent deteriorating supply chain fundamentals that require active strategic intervention. These are often characterized by persistent HHI over multiple years, low or shrinking importer counts, sustained import decline over two or more years, and high volatility over time. These patterns warrant such interventions as supplier development programs, domestic production incentives, technology substitution initiatives, and public-private partnerships.

\- Temporary, broad-based supply chain shocks, such as those observed during the 2020–2021 pandemic, can be differentiated from intermediate or structural issues by their duration and breadth. Temporary shocks typically manifest as sharp spikes across multiple unrelated components and are followed by normalization in import levels as supply chains recover. For these cases, enhanced inventory buffers and contract flexibility can be important tools for mitigating impacts.

Cyclical or short-term challenges are unlikely to require policy actions beyond routine monitoring, whereas more intermediate or more structural supply chain issues may require progressively more-intensive interventions. To demonstrate these distinctions, Table 6.1 presents response options based on example criteria but should only be interpreted as illustrative. More research is needed to validate what levels of vulnerability correspond to different policy options. After narrowing to components with positive composite vulnerability in 2025, the decision framework can be summarized as follows:

\- Active strategic interventions. Components meeting two or more of these criteria require strategic supply chain restructuring:

\- composite z > 1.0 for three years

\- high HHI (>1.5) with declining importers

– sustained import decline (>0.75 for two years)

– three or more metrics >0.75 in 2025.

\- Targeted resilience measures. Components with moderate, sustained instability meeting these criteria should trigger proactive resilience actions:

\- composite scores greater than 0.2 in 2024 and 2025

\- at least two consecutive years of elevated dynamic metrics (volume volatility, price volatility, or import decline).

\- Recommended actions include supplier diversification programs, coordinated procurement pools, enhanced data collection, time-limited incentives for domestic production or refurbishment capacity, and leveraging the scenario analysis methodology used in Chapter 5 to identify the potential impact of supply chain disruptions.

\- Regular monitoring. All other components showing relatively normal market variation managed through standard procurement and monitoring practices.

A decision framework would provide DOE and FERC with a structured, data-driven method to prioritize interventions, consistent with national supply chain resilience strategies that have been proposed across other critical sectors, such as semiconductors and critical minerals. It would also ensure that responses are proportionate, evidence-based, and aligned with broader federal resilience objectives.

Table 6.1. Recommended Response Options, by Critical Component


2. Prioritize policy interventions for supply chains pertaining to generation systems, given their supply chain vulnerabilities compared with transmission systems and critical influence across FTM, BTM, and BP systems. Specifically, priority should be given to the most vulnerable generation components as listed in Table 4.2.

Our analysis in Tables 4.2 and 4.3 shows that although there are supply chain vulnerabilities at both generation and transmission, generation components demonstrate systematically higher composite vulnerability scores in 2025. This divergence likely reflects fundamental market structure differences. Transmission equipment represents more established, standardized technology, whereas generation components often involve specialized manufacturing processes with more limited production sources and higher barriers to entry for new manufacturers. For instance, the generation components show both high structural concentration (persistent red in HHI) and high composite vulnerability. Table 4.2 identifies the generation components that are most vulnerable to supply chain disruptions. Strategic policy interventions could include

\- fostering new market entrants in highly concentrated sectors, such as nuclear components and specialized turbines

\- investing in domestic manufacturing capabilities for critical generation technologies

\- exploring alternative technologies or materials that could reduce dependence on the most vulnerable supply chains while maintaining performance requirements for grid reliability.

The U.S. government should prioritize its interventions in fixing supply chain generation issues.

3. To increase the quality of monitoring capabilities to inform intervention, increase the granularity of trade data for certain critical electrical components, such as natural gas turbines and transformer types. We provide Figure 4.7 for transformers and Figure 4.8 for turbines, the most supply chain–vulnerable components that could be targeted for additional trade data granularity.

Organizations such as USITC and CBP should work together to increase the specificity of certain HTS and Schedule B codes at the ten-digit level. When trade codes are applied to shipments, they can range from highly specific to broad catch-all families of goods, often resulting in mixing items used in the power system with other applications. Because these codes underpin how component movements are observed, the accuracy of trade-code-to-component mappings directly affects the ability to trace supply chains specific to FTM, BTM, and BP systems. For example, several HTS codes have been created that specifically identify wind energy components, such as hubs, generators, gearboxes, and towers. In contrast, HTS codes associated with natural gas turbines are currently distinguished only by aviation versus non-aviation use, despite their importance in electric power generation.

Our results in Table 5.4 indicate that supply chain disruptions for gas turbine procurement can have a significant impact on the ability of the electric power grid to meet frontier AI data center demand. To find mitigating solutions, it is necessary to have more-granular data. Because HTS codes are primarily designed for duties, taxes, and tariffs rather than system relevance, more-granular codes based on power sector characteristics (e.g., voltage class, size, material composition, or functional role) would improve traceability and support a more precise vulnerability assessment.

4. Enhance supply chain mapping capabilities by designing reasonable disclosure requirements for firms transacting or handling key critical components. The supply chain vulnerability heat maps in Figures 4.3 and 4.5 could be used to select the equipment that may merit additional reporting.

The U.S. Securities and Exchange Commission (SEC) or the U.S. Department of Homeland Security should drive a consultative process with utilities, producers, and other government partners to ensure a common language and understanding of disclosure process that lead to improved visibility and coordination around supply chain risks. While the trade codes in this analysis only capture the movement of goods between countries, which essentially represents a subset of the supply chain, they also represent the best publicly available data suited for this analysis. Mandated disclosures could provide the basis for a more comprehensive supply chain mapping and vulnerability assessment.

These types of disclosures are not uncommon and typically are required by federal agencies, such as the SEC or the Departments of Homeland Security, Commerce, or Energy; sector-specific regulators; or legislative action at the state or federal level. We recognize that mandated disclosure could be costly, so the potential burden of additional reporting requirements should be evaluated against the perceived benefits of improving decisive insights. The level of detail in disclosures should also respect principles of competitiveness. $^{74}$ We suggest using the results in Figures 4.3 and 4.5 to select equipment that may merit additional reporting.

5. Develop a reserve of highly vulnerable electric grid components for high demand, high vulnerability components to mitigate structural risks and prepare for systemic supply chain shocks.

Findings from the vulnerability assessment reveal that turbines (for example, substation systems) exhibit persistent structural vulnerabilities—high supplier concentration, long lead times, and limited domestic manufacturing capacity—while also being exposed to temporary global shocks that can rapidly constrain supply. Establishing a reserve would therefore serve a dual purpose by supporting domestic production with a stable demand signal and as a

preparedness measure to ensure rapid recovery from temporary disruptions or catastrophic events.

This recommendation represents a targeted, data-driven intervention consistent with the “active intervention” tier of the decision framework proposed in Recommendation 1. It builds on proven models for strategic reserves across other critical sectors, including GridAssurance for transmission equipment, the Strategic Petroleum Reserve for energy security, the National Defense Stockpile for critical minerals, and the Strategic National Stockpile for medical supplies. These programs demonstrate that selective, well-governed reserves can mitigate concentrated supply risks, accelerate recovery from disruptions, and provide a stable demand signal to incentivize domestic manufacturing.

DOE and FERC should coordinate with utilities and large loads, such as data centers, to develop a transparent process for identifying which components merit inclusion in a national or regional reserve. Selection criteria should reflect system criticality, supply chain concentration, lead times, and regional dependencies. DOE and FERC should also establish cost-recovery mechanisms that allow utilities to maintain inventories without undue financial burden, ensuring that resilience investments are both equitable and economically sustainable. A reserve program could help buffer regional pressures and support timely grid expansion. Implementation should also account for practical constraints, including component shelf life, evolving technology standards, and potential incompatibility over time. To address these challenges, DOE and FERC could adopt a rotating-inventory model, in which reserved equipment is periodically cycled into active use and replenished, maintaining both readiness and technological relevance.

The additional inventory of electrical equipment is intended to increase resilience and provide a strong, consistent demand signal for industry, but it will also be costly, and a cost-recovery plan must be accounted for. The results in Table 4.3 could be used for identifying the most supply chain-vulnerable transmission components that could be a target for additional inventory. DOE and FERC should work with utilities and large loads, such as data centers, to develop a process to select the most critical equipment for additional inventory (which may depend on a utility's service area) and provide the utilities with the means to recover their costs.

6. Develop incentives for the standardization of critical equipment as a measure to mitigate supply chain constraints, such as market concentration. Figures 4.3 and 4.5 provide the critical components most likely to benefit from standardization due to their high market concentration.

Utilities and large loads should be incentivized to come together and develop equipment standards that enable interoperability and reduce similar but non-interchangeable equipment. Standardization can mitigate supply chain vulnerabilities by reducing complexity and enabling new entrants, similar to how modular design and interoperability standards have improved

resilience in semiconductor and battery manufacturing. Our inventory in Chapter 3 identifies significant variability across components within critical systems, suggesting that increasing the standardization of designs may mitigate supply chain issues by facilitating production. For instance, our inventory analysis shows that transformer types vary significantly with voltage and other specifications. A 2024 National Infrastructure Advisory Council report also identifies the lack of standardization as a barrier to increasing production to address the scarcity of transformers. $^{75}$ Similar efforts could be made for other critical equipment identified in our study, such as gas-powered generators and wind turbines. $^{76}$ Standardization can mitigate supply chain vulnerabilities as follows:

\- Standardizing designs (e.g., maximum diameter for wind turbines) facilitates production by reducing complexity and leading to new entrants, thereby reducing market concentration on components with high HHI (see Figures 4.3 and 4.5).

\- Developing a modular approach to equipment (e.g., transformers) can reduce assembly times. DOE should work with utilities to develop new codes and standards.

DOE and the Department of the Interior should work with consensus-driven organizations, such as the National Electric Code or the Institute of Electrical and Electronics Engineers (IEEE), and utilities to develop codes and standards that encourage standardization and its adoption.

7. Encourage and/or incentivize substitution of storage equipment with chemistries with high supply chain vulnerabilities (e.g., lithium) with chemistries of lower vulnerabilities (e.g., sodium).

Findings from the vulnerability assessment reveal that generation storage components (e.g., batteries) are among the components with the highest vulnerability scores. Additionally, the risk-scenario analysis presented in Chapter 5 demonstrated that supply chain–related threats for storage components can have significant impact on the net capacity of the electric power grid to meet the demands of frontier AI data centers. It is also important to note that the supply chain vulnerabilities are not the same across all battery chemistries. For instance, batteries based on lithium depend on minerals located in certain areas of the world, whereas batteries based on sodium are less vulnerable from supply chain impacts because sodium is abundant worldwide, both on earth and in oceans. In addition, the manufacturing of sodium batteries is less complicated as compared with other battery types, which makes their supply chains more

resilient. $^{77}$ Currently, lithium batteries dominate power grid storage due to economies of scale and high energy density. $^{78}$ Alternatives such as sodium batteries, although less vulnerable to supply chain disruptions, have a lower energy density and need to operate at higher temperatures, which raises safety issues. Therefore, entities such as DOE should coordinate with researchers and utilities to develop potential commercialization opportunities for alternative storage chemistries with lower supply chain vulnerability.

8. Develop mechanisms of collaboration and transparency between utilities and large loads to improve load forecasting and better management of procurement of scarce equipment (e.g., turbines).

Large loads may consider embracing BP to sidestep the challenges faced by the U.S. power grid. However, as our inventory in Chapter 3 indicates, the supply chain problems are likely to persist when both utilities and large loads are competing for the same equipment, leading to additional price volatility, which is one of the indicators of supply chain vulnerability. For instance, Figure 4.9 shows that the price volatility indicator is medium to high for gas turbines. Increasing collaboration between utilities and large loads could allow for better load forecasting and better management of the grid's equipment. Problems with load forecasting have been identified in ERCOT, where initial demands forecasts were too high due to some of the large loads projects on the pipeline being speculative. $^{79}$ Similarly, issues with load forecasting have been raised by Grid Strategies and other organizations.

Although some supply chain threats may be out of the utilities' and data centers' control, their consequences could be mitigated by more collaboration. Utilities have a long history of collaboration to address resiliency challenges. $^{80}$ For instance, GridAssurance is an organization that pools transmission equipment available to utilities for a fee. $^{81}$ Examples of collaboration opportunities between utilities and large loads to address supply chain challenges could include

\- supply chain task forces to better forecast the demand and prioritize the procurement of critical components

\- joint procurement pools to increase purchasing power for critical electrical infrastructure components that they both require (e.g., transformers), reducing procurement times.

Pilots for collaboration agreements between utilities and developers have been announced. One example is an agreement between PPL Electric Utilities and Blackstone. $^{82}$ DOE and FERC should facilitate the development of such collaborations to facilitate long-term partnerships that help mitigate supply chain issues.

The methodology for this literature review is structured to address three core research questions:

\- Research Question 1: What are the critical electric power components required by AI data centers, including BTM, FTM equipment, and BP solutions?

\- Research Question 2: What are the projected equipment requirements, based on relevant AI energy need forecast?

\- Research Question 3: What supply chain vulnerabilities currently exist for the procurement of AI-critical electrical equipment?

To systematically address these questions, the review process integrates both academic literature and gray literature sources, drawing on prior RAND research, industry reports, government documents, and peer-reviewed articles. The literature review process was organized into several key steps:

\- Check and recycle seed literature: Begin with a review of previously identified, high-relevance publications to establish a foundational knowledge base.

\- Source identification: Broaden the search to capture both academic and gray literature relevant to each research question.

\- Structured query: Use targeted search —relevant keywords, databases, and organizational repositories—to systematically retrieve findings and data points for each research question.

\- Source-specific findings and analysis: Extract, catalog, and analyze pertinent information from each source in relation to the research questions.

\- Synthesis: Integrate insights from the diverse sources to construct cohesive answers for each research question and identify gaps or points of convergence in the existing knowledge.

## Seed Literature

First, an initial set of seed literature was assembled based on recommendations from RAND researchers with expertise in energy industry or supply chain analysis (see Table A.1). The review of seed literature served to refine and inform the scope of the comprehensive literature review by highlighting key topics, sources, and gaps relevant to the research questions.

Table A.1. Seed Literature Source Summary


In total, 38 seed sources were identified for preliminary review. The majority consisted of publications and reports released from 2020 to 2025, reflecting current developments and emerging issues at the intersection of AI, power systems, and supply chain management. Two of these sources are general topical reviews or theory-oriented works published before 2020, and two others are supply chain datasets. These were excluded from the scope of analytical insight extraction, as their content primarily serves descriptive or quantitative functions.

The seed literature reveals that although general supply chain issues for electrical equipment required in AI data centers are widely acknowledged, there is limited detail regarding specific component types or their individual supply chain characteristics: References largely focus on high-level categories and regulatory oversight rather than component-level breakdowns. Although documents covered in the seed sources signal the importance of both FTM and BTM equipment, they do not provide fine-grained analyses or comprehensive inventories. Similarly, although future years and planning horizons are frequently cited, no seed sources offer concrete projections or quantitative estimates mapping AI energy demand to specific equipment requirements. Lastly, supply chain vulnerabilities are extensively referenced, often described as high risk in government and regulatory reports, but the discussion remains generalized without detailed categorization by risk type or by individual equipment. In general, technical insights and case studies are notably absent. Because the opportunity to identify further sources through snowballing from existing references is constrained, it is clear that additional, systematic searching of both academic and gray literature is required to uncover more-granular insights.

## Key Words for Source Identification

We employed a keyword-driven search methodology. A set of 34 key terms was curated and organized into six thematic groups:

A. Core Concepts: Terms related to AI, data centers, and digital infrastructure.

B. Electric Power Components and Infrastructure: Keywords for specific equipment (e.g., transformers, UPS systems, switchgear), grid assets, and facility infrastructure.

C. Supply Chain and Vulnerabilities: Phrases addressing supply chain dynamics, risk, disruption, procurement, and resilience.

D. Market and Policy Context: Expressions reflecting regulatory oversight, market concentration, and relevant policy settings.

E. Projections and Forecasts: Words associated with energy demand projections, capacity forecasts, and scenario analysis.

F. Standards, Codes, and Government Programs: Terms connected to industry standards, harmonized codes, and government initiatives or datasets.

Using these thematic groups, keyword combinations were systematically generated to align with each of the three research questions. For Research Question 1 (critical electric components), five keyword combinations were built to target equipment-level literature spanning both FTM and BTM domains, and the keywords came from Groups A and B. For Research Question 2 (projected equipment requirements), another five keyword pairings were generated from Groups A, B, D and E, which prioritized sources focused on future technical needs and energy forecast alignment. For Research Question 3 (supply chain vulnerabilities), seven targeted keyword combinations were used to capture literature focused on risk identification, disruption, and system resilience. These seven combinations are associated with Groups A, B, C and F. The keyword combinations are summarized in Table A.2.

Table A.2. Mapping of Research Questions to Specific Keyword Combinations and Thematic Groups


NOTE: CISA = Cybersecurity and Infrastructure Security Agency.

## Search Protocols

For academic literature, searches were conducted using Elicit, an AI-powered literature review tool. Each of the 17 keyword combinations was entered as a separate chat within Elicit, and papers published before 2020 were excluded from the search scope. For each search, the 100 most relevant papers were selected based on Elicit's relevance ranking and were retained in a digital library. The metadata and citation information for these papers were exported and logged into a dedicated spreadsheet for academic sources.

Gray literature searches were performed in Perplexity, leveraging the same 17 keyword combinations and restricting the time frame to post-2020 publications. For gray literature, Perplexity was chosen to focus on high-quality reports, government documents, and industry analyses that may not be indexed in traditional academic databases, which are better covered by Elicit. Each search for relevant gray literature typically resulted in the identification of ten to 20 reports, government documents, and industry sources. These materials were manually accessed and downloaded when possible, and their bibliographic details logged into a separate spreadsheet designated for gray literature.

Finally, both spreadsheets—one for academic sources and one for gray literature—were organized to align preliminary outputs with the specific research question addressed by each search (Table A.3).

Table A.3. Sources Identified by Category and Search Protocol


## Structured Queries for Evidence Extraction

To systematically capture relevant evidence, we developed targeted queries grouped according to each research question. For both academic and gray literature, we used the same sets of query questions for evidence extraction.

## Critical Electric Power Components

\- What types of critical electric power components are identified as necessary for AI data centers?

\- Does the paper distinguish between FTM and BTM electrical equipment? If so, what distinctions are made?

\- What functions do these components serve within AI data center operations?

\- Is integration with the power grid discussed? Describe the approach.

\- What backup or redundancy systems are mentioned for AI-critical components?

## Projected Equipment Requirements

• What projections for AI data center energy demand are provided?

• How do these projections translate into equipment procurement needs?

\- Are quantitative estimates given for required electrical components (e.g., number of transformers, MW capacity of backup generators)?

• What time frames are used in the forecasts?

\- What assumptions underpin these forecasts (e.g., AI workload growth, grid integration)?

\- Are anticipated technological changes considered?

\- Does the paper reference specific datasets or models?

## Supply Chain Vulnerabilities

\- What supply chain vulnerabilities for AI-critical electrical equipment are identified?

• Is market concentration among suppliers discussed?

\- Are there dependencies on imports or specific origin countries?

\- Are vulnerabilities linked to specific components?

\- Are tariff codes or trade classifications mentioned?

• What resilience or mitigation strategies are proposed?

\- Are recent disruptions or case studies discussed?

\- Are policy or regulatory frameworks mentioned to address supply chain risk?

For academic papers, the Elicit chats that stored the 17 sets of search results were used to directly apply the query questions listed above to the abstracts or executive summaries. Each set preserves the top 100 papers from each search. Based on the query questions, Elicit generated summaries based on the 100 papers in each iteration, and relevant pieces of evidence were summarized at an aggregate level, with reference to the specific academic papers that supported different parts of the summary. We reviewed highlighted evidence and cross-referenced it with original paper content to ensure that key points were directly supported by the cited sources and accurately reflected their findings.

For gray literature, each identified source was individually queried using the same set of questions. AI assistance supported the extraction process. The query results were generated for each report or article and were recorded for further analysis.

## Synthesis

For academic sources, the outputs from the literature review tool served as the primary input for synthesis. Using the results from the structured queries, we analyzed trends, evidence, and knowledge gaps present within peer-reviewed literature. For gray literature, query results were generated and documented for each individual source, and these findings were aggregated across all selected documents to synthesize findings. We then used these aggregated results as a basis for further analysis.

The final stage of synthesis involved comparing and contrasting the key findings for each research question as derived from academic papers and gray literature sources. Given that the intersection of AI data center operations and electric power supply chains is a relatively nascent area of research, the academic literature was expected to present limitations in terms of detail, data availability, and coverage of emerging trends. Throughout the synthesis process, this understanding guided our analysis—particularly for the gray literature sources, which were scrutinized with recognition of their value in capturing practical developments, industry perspectives, and evolving challenges that may not yet be reflected in peer-reviewed publications.

A list of the relevant components identified for FTM and BTM are provided in this appendix (Tables B.1–B.9). They are broken up into FTM and BTM for ease of interpretation; however, there is overlap between the two. Additionally, for completion, multiple systems contain similar subcomponents and result in redundancy. Subcomponents are denominated by having the main component ID, a dot, and then the subcomponent identifier.

The list of FTM inventory focus on larger systems of systems that provide specific capabilities through a clearly defined means. For FTM components, the ID enumeration follows a number, letter, roman number convention to identify between a system, a component of the system, or a subcomponent of a component.

Table B.1. Inventory FTM: Transmission


Table B.2. Inventory FTM: Generation


NOTE: CCGT = combined cycle gas turbine.

Table B.3. Inventory BTM: Transformer


Table B.4. Inventory BTM: Thermal Management


Table B.5. Inventory BTM: Supporting Data Center Equipment


Table B.6. Inventory BTM: Power Management


Table B.7. Inventory BTM: Power into the Racks


Table B.8. Inventory BTM: Power Transfer


Table B.9. Inventory BTM: Backup Power


## Example Vulnerability Calculation


Step 1. Calculate annual metrics for each HTS code using annual trade data to compute the five underlying metrics (Table C.1).

Table C.1. Calculate Annual Metrics


Step 2. Aggregate HTS-level metrics to the component level using a simple average across HTS codes.

$$
\text { Component   Metric } _ {m, 2 0 2 5} = \frac {\mathrm{HTSA} _ {m , 2 0 2 5} + \mathrm{HTSB} _ {m , 2 0 2 5}}{2}
$$

Table C.2. Aggregate HTS-Level Metrics to the Component Level


Step 3. Convert each metric to a standardized z-score relative to its reference group.

\- Structural metrics (HHI, importer count): peer-based z-scores across all components in the same year.

\- Dynamic metrics (import decline, volume volatility, price volatility): time-based z-scores within the component's history (2016–2025).

$$
Z _ {m, 2 0 2 5} = \frac {X _ {m , 2 0 2 5} - \bar {X} _ {m}}{\sigma_ {m}}
$$

Metrics where higher values imply less vulnerability (e.g., number of importing countries) are inverted by multiplying by -1 so that all z-scores follow the same “higher = more vulnerable” direction.

Step 4. Apply metric weights and compute the composite vulnerability score (Table C.3).

$$
Z _ {\text {Composite}} = \frac {1}{8} Z _ {\text {HHI}} + \frac {1}{8} Z _ {\text {Importer Count}} + \frac {1}{4} Z _ {\text {Volume Volatility}} + \frac {1}{4} Z _ {\text {Price Volatility}} + \frac {1}{4} Z _ {\text {Import Decline}}
$$

Table C.3. Apply Metric Weights and Compute the Composite Vulnerability Score


## Sensitivity Analysis


Table C.4. Sensitivity Analysis Results


This appendix presents the vulnerability scores for the FTM and BTM components (Figures D.1 and D.2). Details for how metrics are calculated are in the Methods for Examining Supply Chain Vulnerability section of Chapter 4.

Figure D.1. Vulnerability Scores for FTM Systems
FTM: Transmission


Figure D.2. Vulnerability Scores for BTM Systems
BTM: Backup Power


BTM: Transformer


BTM: Thermal Management

Z-score


BTM: Supporting Data Center Equipment


BTM: Power Transfer


BTM: Power into the Racks


Available capacity is the total power output, expressed in gigawatts (GW), that is readily accessible for consumption at any given time.

Behind-the-meter (BTM) refers to energy systems located on the customer's side of the utility meter. These systems generate, store, or manage electricity without passing through the meter that measures power consumption from the grid. The term behind-the-meter contrasts with front-of-the-meter, which refers to electricity that comes from the public grid and passes through the utility meter before reaching the consumer.

Bridge power (BP) refers to a temporary power source used to support a system during a transition period, such as power grid buildup or power grid maintenance.

Effective capacity refers to technology-agnostic reliable capacity. Determined by Capacity Accreditation Factors (CAF), this metric is used by energy planners for resource adequacy assessment.

Front-of-the-meter (FTM) refers to energy systems that are connected to the utility grid and supply electricity to a broad area, typically including large-scale generation and storage facilities.

Harmonized Tariff Schedule (HTS) codes are ten-digit numbers used to classify imported products, determine customs duties, and facilitate trade. They build on the international six-digit Harmonized System code, adding four digits specific to U.S. product details, and are administered by the U.S. International Trade Commission.

Herfindahl-Hirschman Index (HHI) is an economic measure of market concentration, calculated by summing the squares of each firm's market share in an industry, indicating competition levels from perfect (0) to monopoly (10,000). U.S. Department of Justice guidelines suggest that values below 1,500 are considered unconcentrated; values between 1,500 and 2,500 are considered moderately concentrated; and values above 2,500 are considered highly concentrated.

Resource refers to a type of generation or storage, typically associated with specific technology and fuel types. For instance, “solar” refers to solar photovoltaic or thermal technologies, whereas “gas” encompasses simple-cycle and combined-cycle technologies that use gas as a fuel.

Resource adequacy refers to the ability of a power system to supply enough electricity to meet its reliability target during all hours of the year. It requires system planners to ensure that the mix of resources can meet demand during periods of high system stress.

Variable renewable energy refers to electricity generation technologies that rely on energy sources, such as solar or wind, that fluctuate over time and are not easily stored. These sources depend on changing environmental conditions, affecting their maximum output at any given time.

Volatility is the rate at which the price or volume of a good fluctuates over time.

Acemoglu, Daron, and Alireza Tahbaz-Salehi, “The Macroeconomics of Supply Chain Disruptions,” Review of Economic Studies, Vol. 92, No. 2, March 2025.

Ahrabi, Rouzbeh Reza, Alireza Mousavi, Ebrahim Mohammadi, Ryan Wu, and Aoxia Kevin Chen, “AI-Driven Data Center Energy Profile, Power Quality, Sustainable Siting, and Energy Management: A Comprehensive Survey,” Proceedings of the 2025 IEEE Conference on Technologies for Sustainability (SusTech), April 2025.

Ambrozaite, Ona, Corinna Torabi, Nathan Van Damme, Daniel Velez, and Michel Wallemacq, "Standardization of Turbine Design and Installation Vessels to Accelerate the Offshore Wind Industry in the United States," Journal of Science Policy and Governance, Vol. 25, No. 1, October 28, 2024.

American Public Power Association, “Critical Electrical Infrastructure and Supply Chain Constraints,” January 2024

Anderson, Jared, “US Gas-Fired Turbine Wait Times as Much as Seven Years; Costs Up Sharply,” S&P Global, May 20, 2025.

Arciniegas Rueda, Ismael, David Gill, and Henri van Soest, “The Cost of Misforecasting: How Ignoring Non-AI Demand Risks the Grid,” National Interest, December 11, 2025.

Arciniegas Rueda, Ismael, Henri van Soest, Hye Min Park, Austin Smidt, David Gill, Robin Wang, Kelly Klima, and Aisha Najera, Assessing the United States' Additional AI Power Capacity by 2030: Estimating Short-Term Increases in Electricity Generation and the Ability to Meet Growth in Power Demand, RAND Corporation, RR-A3845-1, 2025. As of July 9, 2025: https://www.rand.org/pubs/research\_reports/RRA3845-1.html

Arora, Neeraj, Mark A. Lazaroff, Thomas V. D'Ambrosio, and Maggie E. Curran, “A 2024 Update on Utility-Scale Energy Storage Procurements,” Morgan Lewis, March 4, 2024.

Brazilian, Morgan, and Kyri Baker, “Supply-Chain Delays, Rising Equipment Prices Threaten Electricity Grid,” The Conversation, November 14, 2025.

Boucher, Benjamin, “The Challenge of Growing Electricity Demand in the US and the Shortage of Critical Electrical Equipment,” Wood Mackenzie, May 2, 2024.


Chien, Andrew A., “GenAI: Giga\$\$\$, TeraWatt-Hours, and GigaTons of CO2,” Communications of the ACM, Vol. 66, No. 8, August 2023.

Chopra, Sagar, and Benjamin Boucher, “Supply Shortages and an Inflexible Market Give Rise to High Power Transformer Lead Times,” Wood Mackenzie, April 2, 2024.

CoreSite, “More Power! Behind-the-Meter Power Systems for Data Centers,” webpage, undated. As of May 12, 2026: https://www.coresite.com/blog/more-power-behind-the-meter-power-systems-for-data-centers

Cushman & Wakefield, 2025 U.S. Data Center Development Cost Guide, 2025.

DataWeb, “New Data Request,” U.S. International Trade Commission, undated. As of May 19, 2026: https://dataweb.usitc.gov/trade/search/Export/HTS

DiGangi, Diana, “Georgia Power Receives Natural Gas Turbine as Delays Loom,” Utility Dive, August 21, 2025.

Edelberg, Wendy, “A Taxonomy of Supply Shocks and Their Effects on Inflation,” Brookings Institution, November 24, 2025.

Enbar, Nadav, Dean Weng, Ryan Edge, and John Sterling, Microgrids: Expanding Applications, Implementations, and Business Structures, Smart Electric Power Alliance and Electric Power Research Institute, December 2016.

Evolve Data Center Solutions, “Powering Data Centers in the Modern Age: Bridge Power Solutions,” January 13, 2025.

Gérard, Frank, João Gorenstein Dedecca, Ling Ying Lee, Liliana Guevara Opinska, Jessica Yearwood, Onne Hoogland, and Christopher Andrey, Study on the Resilience of Critical Supply Chains for Energy Security and Clean Energy Transition During and After the COVID-19 Crisis, Directorate-General for Energy, European Commission, June 2021.

Glassmire, John, Hamideh Bitaraf, Stylianos Papadakis, and Alexandre Oudalov, “Accelerating Data Center Decarbonization and Maximizing Renewable Usage with Grid Edge Solutions,” Proceedings of the 2021 Design, Automation & Test in Europe Conference & Exhibition, February 2021.

Green, Alastair, Humayun Tai, Jesse Noffsinger, Pankaj Sachdeva, Arjita Bhan, and Raman Sharma, “How Data Centers and the Energy Sector Can Sate AI’s Hunger for Power,” McKinsey & Company, September 17, 2024.

Greenberg, Ezra, Erik Schaefer, and Brooke Weddle, “Tradespeople Wanted: The Need for Critical Trade Skills in the US,” McKinsey & Company, April 9, 2024.

Grid Assurance, “Grid Resilience Solution,” webpage, undated. As of May 19, 2026: https://gridassurance.com/grid-resilience-solution/

Gurtu, Amulya, and Jestin Johny, “Supply Chain Risk Management: Literature Review,” Risks, Vol. 9, No. 1, January 2021.

Hooper, Craig, “With Electrical Grids Under Assault, U.S. and Ukraine Seek Scarce Transmission Gear,” Forbes, January 4, 2023.

Howland, Ethan, “AEP Ohio Reaches Agreement with Stakeholders on Data Center Interconnection Rules,” Utility Dive, October 24, 2024.

International Trade Administration, “U.S. Energy Trade Dashboard,” database, accessed on May 27, 2025. As of May 27, 2025: https://www.trade.gov/data-visualization/us-energy-trade-dashboard


Kasiewicz, Chris, and Chris Postma, “How Utilities Can Partner with Data Centers Amid Surging Load and On-Site Generation,” Utility Dive, September 8, 2025.


Lawson, Ashley J., “Introduction to Electricity Transmission,” Congressional Research Service, IF12253, November 18, 2022.


Li, Zheqing, Yi-Hsun Hsieh, Qiang Li, Fred C. Lee, and Mohamed H. Ahmed, “High-Frequency Transformer Design with High-Voltage Insulation for Modular Power Conversion from Medium-Voltage AC to 400-V DC,” Proceedings of the 2020 IEEE Energy Conversion Congress and Exposition, October 2020.

Marbella, Lauren, and Yuan Yang, “Clean Energy When You Need It,” Fu Foundation School of Engineering and Applied Science of Columbia University, undated.

Martucci, Brian, “Are Sodium-Ion Batteries Finally Ready to Compete with Lithium?” Utility Dive, October 28, 2025.

Matz, Michael, “Argonne Battery Breakthroughs Power Success for U.S. Industry,” Argonne National Laboratory, February 18, 2026.

National Infrastructure Advisory Council, Addressing the Critical Shortage of Power Transformers to Ensure Reliability of the U.S. Grid, June 2024.

National Renewable Energy Laboratory, “Explained: Fundamentals of Power Grid Reliability and Clean Electricity,” January 2024.

NERC—See North American Electric Reliability Corporation.

Nguyen, Ruby, Mike Severson, Bo Zhang, Bjorn Vaagensmith, Md Mamunur Rahman, Angel-Lionel Toba, Paige Price, Ryan Davis, and Sophie Williams, Electric Grid Supply Chain Review: Large Power Transformers and High Voltage Direct Current Systems, U.S. Department of Energy, February 24, 2022.

North American Electric Reliability Corporation, 2024 Long-Term Reliability Assessment, December 2024.

Ontiveros, Jeremie Eliahou, Dylan Patel, and Daniel Nishball, “Datacenter Anatomy Part 1: Electrical Systems,” SemiAnalysis, Substack, October 14, 2024.

Pandey, Ajey, Jeremie Eliahou Ontiveros, and Dylan Patel, “How AI Labs Are Solving the Power Gap Crisis: The Onsite Gas Deep Dive,” SemiAnalysis, Substack, December 30, 2025.


Peng, Peng, Man Chen, Yuxuan Li, Yuxin Zhao, Ningning Li, Hao Liu, Bing Wang, Yushu Sun, and Xisheng Tang, “Research on Energy Storage Type of Uninterruptible Power Supply Technology in Internet Data Center,” Proceedings of the 2022 12th International Conference on Power and Energy Systems, December 2022.

Pesin, Michael, “DOE and Industry Team Up to Keep the Lights on for America,” Office of Electricity, U.S. Department of Energy, February 22, 2024.

Pilz, Konstantin F., Yusuf Mahmood, and Lennart Heim, AI's Power Requirements Under Exponential Growth: Extrapolating AI Data Center Power Demand and Assessing Its Potential Impact on U.S. Competitiveness, RAND Corporation, RR-A3572-1, 2025. As of May 14, 2026: https://www.rand.org/pubs/research\_reports/RRA3572-1.html

Pinto, Alisha, “Transformers Are Facing Major Cost, Supply Chain Pressures,” National Rural Utilities Cooperative Finance Corporation, March 24, 2025.

Popik, Thomas, “Ukraine’s Coming Electricity Crisis,” Foreign Affairs, February 3, 2023.

Powell, Phill, and Ian Smalley, “What Is Hyperscale?” IBM, undated. As of June 16, 2026: https://www.ibm.com/think/topics/hyperscale

Quint, Ryan, Kyle Thomas, Jiecheng Zhao, Andrew Isaacs, and Casey Baker, Practical Guidance and Considerations for Large Load Interconnections, Elevate Energy Consulting and GridLab, May 2025.

Rider, Darryl, “Winning the Race to Revenue—Bridge Power Solutions for Data Centers,” Caterpillar, April 2025.

S, Hrishikesh, “A New Semiconductor Tug of War: AI Data Centers vs. Automakers,” S&P Global, October 10, 2025.

Stansbury, Martin, Kelly Marchese, Kate Hardin, and Carolyn Amon, “Can US Infrastructure Keep Up with the AI Economy?” Deloitte, June 24, 2025.

Thomson, Jim, Marlene Motyka, Kate Hardin, and Jaya Nagdeo, Electric Power Supply Chains: Achieving Security, Sustainability, and Resilience, Deloitte, 2022.

Trabish, Herman K., “Utilities, Regulators, Look to Accelerate Pilots to Achieve Speed-to-Innovation,” Utility Dive, December 1, 2025.

U.S. Customs and Border Protection, “Customs Rulings Online Search System (CROSS),” webpage, undated. As of May 19, 2026: https://rulings.cbp.gov/home

U.S. Department of Energy, “How Gas Turbine Power Plants Work,” webpage, undated. As of May 14, 2026:
https://www.energy.gov/fecm/how-gas-turbine-power-plants-work

U.S. Department of Homeland Security, Risk Management Fundamentals: Homeland Security Risk Management Doctrine, April 2011.

U.S. Energy Information Administration, “U.S. Electric System Is Made Up of Interconnections and Balancing Authorities,” July 20, 2016.

U.S. International Trade Commission, “Harmonized Tariff Schedule,” webpage, undated. As of May 19, 2026: https://hts.usitc.gov

Voltage Voyager, “Understanding Microgrid Components and Topology: A Comprehensive Guide,” Electrical Blog, June 28, 2025. As of November 18, 2025: https://www.electrical-blog.com/microgrid-components-topology/

Wilson, John D., Sophie Meyer, Zach Zimmerman, and Rob Gramlich, “Power Demand Forecasts Revised Up for Third Year Running, Led by Data Centers,” Grid Strategies, November 2025.

Wood Mackenzie, “Power Transformers and Distribution Transformers Will Face Supply Deficits of 30% and 10% in 2025,” press release, August 14, 2025.

Xiong, Ding, and Yao Sun, “The Rising Cost of Turmoil: Geopolitical Crises and Supply Chain Risk,” Economic Letters, Vol. 255, September 2025.

Yuksel, Aytek, “Components of Microgrids,” Cummins, October 4, 2021.

Ismael Arciniegas Rueda is a senior economist at RAND and AI Energy Cluster Lead at the RAND Center on AI, Security, and Technology, where he applies quantitative methods to energy markets. His work has included providing input on where to locate AI data centers, exploring the use of AI to improve energy security, and examining the security implications of a power grid developed and governed by China. Arciniegas Rueda holds a Ph.D. in economics.

Rahim Ali is a senior technical analyst at RAND. His research interests include critical infrastructure protection and resilience planning, disaster preparedness and recovery, and infrastructure risk analysis. Ali holds an M.S. in civil and environmental engineering with a focus in advanced infrastructure systems.

Frank Andujar Lugo is a technical analyst at RAND. His research interests include energy security, climate trends adaptation and mitigation, disaster preparedness and recovery, analysis of alternatives for systems and force architecture design and optimization, and emerging technologies. Lugo holds an M.S. in mechanical engineering.

Karishma V. Patel is an adjunct policy researcher at RAND. Her work spans risk assessment and response design across public investment and project portfolios, supply chains, and critical infrastructure systems. Patel holds an M.P.A. in public administration.

Robin Wang is an assistant policy researcher at RAND. His research focuses on AI and energy infrastructure build-out, the systemic risks emerging from recent development, and government finance and equity implications of adaptation interventions. He holds an M.P.A. with a concentration in economic and public policy.
