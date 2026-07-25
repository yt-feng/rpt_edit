# Surprising Lessons from Scaling Renewables in the US and China

By Maurice Berns, Rina Su, Ross LaFleur, Khushboo Goel, Cédric Hazevoets, and Eden Cottee-Jones

ARTICLE APRIL 07, 2026 12 MIN READ

As global demand for electricity rises, driven in part by the rapid buildout of AI data centers, the pace of the energy transition increasingly depends on whether low-carbon power is available to meet that demand. Solar and wind energy, core technologies in the transition, have scaled rapidly in many countries over the past decade, most notably in China and the US. And yet, deployment is uneven in both nations. Some provinces and states have seen a massive ramp-up in solar and wind capacity; others have witnessed halting or stalled progress, even where the underlying resources are abundant.

This reality reveals an important but overlooked dynamic. Certainly, national energy policies are impactful, and the diverging approaches of the US and China will influence the overall trajectory of renewables in each nation in the years ahead. But the vastly different geographic concentration of solar and wind capacity across provinces and states within each country tells us that national policy is only one piece of the puzzle. Other factors also help shape how renewable buildout does or does not advance.

To understand exactly what these drivers are, we conducted an in-depth analysis of China and the US, the world's number one and number two producers of renewable energy today. We examined 70 explanatory variables related to renewable energy scale-up, drawing on more than 100,000 data points across all 50 US states and 31 Chinese provinces from 2014 to 2024. $^{1}$

What stood out most wasn't that the business case matters for scaling renewables—it was which parts of the business case matter most. Our model pinpointed empirically the specific elements that had the greatest impact in both countries. Several are especially noteworthy:

\- Cheap Land. Access to affordable land was far and away the biggest factor in both China and the US, reflecting the core role it plays in making the economics of a project work.

\- Existing Solar and Wind Capacity. We observed a definite association between a strong foundation of renewable energy in a state or province and successful scaling over our study period. This finding suggests that even regions that start from a small base can create a virtuous cycle, with early investments generating momentum that attracts further investment and growth.

\- A Robust Grid. Both the reliability of the grid and investment in utility infrastructure had a clear connection to renewable scaling. Nevertheless, the dynamics related to the grid—the foundational infrastructure for delivering renewable energy—were complex, differing in US states as compared to Chinese provinces.

By revealing the conditions that enable renewable energy to scale, these data-driven insights offer guidance for private- and public-sector players. Companies can use them to inform smarter decisions about where and how to deploy capital, and governments and regulators can draw on them to design policies that advance the deployment of low-carbon energy.

# The Renewables Story in China and the US

A close look at renewables at the province and state level reveals some surprises. $^{2}$ For example, even though China is the global leader in overall renewable energy production, the top five regions by share of electricity from renewables at the end of 2024 were US states. And both countries exhibited wide variations in renewable penetration—from less than 1% to 64% across the 50 US states and 31 Chinese provinces—with especially pronounced differences in the US. (See Exhibit 1.)

## EXHIBIT 1

The Share of Electricity from Wind and Solar Sources Within the US and China Varies Widely

Share of electricity generated from wind and solar across US states and Chinese provinces, 2024 (% of TWh)


[[KC_IMAGE_001]]

Sources: US Energy Information Administration; National Bureau of Statistics of China; BCG Henderson Institute analysis.
Note: This analysis covers mainland China's 31 province-level regions (22 provinces, five autonomous regions, and four municipalities). Wind and solar adoption is defined as the share of electricity generated in-state or in-province from wind and solar (excluding electricity imports). TWh = terawatt-hours.

With that variability in mind, the BCG Henderson Institute created a model to tease out the factors that influence renewable energy buildout. Essentially the analysis quantifies how important specific factors were in predicting wind and solar expansion from the end of 2014 through 2024. The model does not prove that any one factor directly caused renewable scaling, but it does identify factors that are clearly associated with renewable uptake and therefore should be integrated into decision making. (See the sidebar, “Modeling Renewable Scaling.”)

## - Modeling Renewable Scaling

Our research followed a three-step process to identify key factors underlying the adoption of wind and solar energy across Chinese provinces and US states.

First, on the basis of a literature review and more than 20 expert interviews, we built a comprehensive set of hypotheses about likely drivers of renewable deployment, including legacy mix, local economy, regulatory enablers, and infrastructure maturity. Second, we gathered data across all 81 states and provinces in our study set for each hypothesis. Third, we developed and ran a model to assess the influence of those variables. We used 2014 as the baseline year and modeled the share of growth from the end of 2014 through the end of 2024 predicted by specific variables.

To improve model performance, we rigorously screened the input variables. Initially, we performed correlation analysis, applying statistical and practical tests to exclude variables with weak or inconsistent relationships. Then we assessed the significance of each variable through permutation-based importance, which quantifies each variable's explanatory power by measuring accuracy loss when values are randomly shuffled. Next, we used Recursive Feature Elimination to iteratively remove redundant or low-value variables. This step involved conducting thousands of iterations as well as applying nonlinear tree-based algorithms (specifically Random Forest, Gradient Boosting, and XGBoost) to capture the complex, nonlinear interactions inherent in renewable energy adoption. Finally, to understand each variable's impact, we used SHAP analysis, a technique that illustrates the significance and direction of each variable. Sensitivity testing further validated the robustness of our model.

We found it challenging to model a handful of variables that likely play a role in scaling renewables. For example, permitting complexity and resulting interconnection delays are well-known barriers to renewable buildout. However, given the wide range of state policies in the US and the limited availability of some permitting data in China, we were not able to build a reliable dataset on this variable, so we excluded it from the modeling.

# What Matters—and What Doesn’t—for Scaling Renewables

Examining the key drivers associated with renewable expansion reveals striking similarities between US states and Chinese provinces, along with a few notable distinctions. Some findings from our model align with intuition, but others challenge it. For instance, although access to abundant solar or wind resources matters, it isn't one of the top two factors driving growth in either the US or China. (See Exhibit 2.)

## EXHIBIT 2

The Top Drivers Influencing Wind and Solar Scaling in the US and China Are Similar

Relative importance of wind and solar adoption drivers across US states and Chinese provinces


[[KC_IMAGE_002]]

Source: BCG Henderson Institute analysis.
Note: Drivers are listed in descending order by combined share of scaling in the US and China. All listed drivers had a positive or neutral impact on scaling except two in China: reliability of power grid and higher GDP per capita. Both of those drivers influenced the scaling of wind and solar in China in a negative direction, meaning that worse-performing local grids and lower GDP per capita were associated with higher wind and solar adoption.

## Cheap Land

The single strongest signal across both countries is the cost of rural land, which accounts for 20% to 21% of modeled growth over the period from 2014 through 2024.

During our study period, the average increase in wind and solar capacity for the ten US states with the cheapest land was 24%, versus just 9% for the ten states with the most expensive land.

Indeed, New Mexico, the state with the cheapest land, had the greatest growth in solar and wind capacity (40%). We observed similar patterns in the China data.

## Existing Renewable Capacity

The model's second-strongest signal across both countries is the presence of a preexisting base of installed wind and solar. This variable explains roughly 12% to 15% of growth over the study period—a striking indication of the positive impact of an experience curve. In China, the three provinces where solar and wind already had a 10% share of the generation mix in 2014 were among the top ten performers for capacity additions over the following decade: Gansu added a further 23%, Jilin 20%, and Inner Mongolia 14%.

This finding does not mean, however, that regions with little existing capacity realistically lack any major renewable opportunity. Instead, it implies that returns on early deployment may compound over time. Each round of buildout can improve the economics and execution of the next, creating a virtuous cycle in which regions that move earlier accelerate faster.

## A Robust Grid

Two drivers in our model capture the robustness of the grid: reliability and investment level. For investment in the grid, the story is straightforward. In both the US and China, the level of investment in utility infrastructure is clearly associated with the scale-up of renewables. The top ten US states for grid investment as a share of GDP experienced six times the rate of solar and wind capacity growth that the bottom ten states did (18% versus 3%).

With regard to grid reliability, as reflected in the frequency and duration of power outages, the story is more complex. Our model showed a clear association between reliability and scaling in US states (where it explained 14% of the buildout) and in Chinese provinces (where it explained 9%). However, the direction of that association differed. In the US, more reliable grids were associated with successful scaling over the ten-year period. In Chinese provinces, the opposite was true: less robust grids were associated with more scaling.

A closer look at the dynamics on the ground explains the seeming contradiction. The Chinese central government has encouraged renewables investment in poorer provinces by strengthening power infrastructure—not through conventional local grid upgrades, but by building high-voltage transmission lines that span hundreds of kilometers from inland provinces to coastal economic powerhouses. As a result, while local grid quality in these provinces remains limited, the high-capacity transmission network is strong, enabling electricity to be exported to distant cities and major industrial hubs.

## Growth in Power Demand

The Chinese efforts to make renewable power generated in rural locations available to faster-growing areas also helps explain another finding.

In China, the model found little connection between power demand growth and solar and wind scaling. In the US, however, the reverse is true. Growth of power demand explained 13% of renewable expansion over the study period, demonstrating that a rising load can strengthen the investment case for renewables. When demand is flat or declining, independent system operators and companies may need to retire older—yet still economically viable—assets to justify new projects. But when demand is increasing, companies can add wind and solar to meet incremental load, yielding a more attractive business case and lower overall systems costs.

## Missing Connections

The strong connections that our model identified are valuable signals. But it’s equally telling when a relationship that you might expect to be vigorous turns out to be weak—or nonexistent. Consider the role of regulatory renewables targets. Although state-level targets in the US seemed to be connected to rollout in the short term, they had no measurable impact over the long term.

We also found little connection between renewable scaling and the degree to which the state or province relied on resources from other regions inside or outside the country for power. Evidently, although energy security is a major energy transition driver at the national level, it has minimal impact at the state or provincial level.

# Insights from Two Breakout Regions

The state of Texas and China's Gansu province enjoyed robust large-scale renewable growth from 2015 through 2024. An examination of both brings the findings in our model to life. (See Exhibit 3.)

## EXHIBIT 3

Both Texas and Gansu Have Rapidly Increased Their Share of Solar-and Wind-Based Power Generation

Texas tripled its share of solar and wind in 10 years
Annual power generation, 2015–2024 (TWh) $^{1}$

Gansu's share of solar and wind doubled in 10 years
Annual power generation, 2015–2024 (TWh) $^{1}$


[[KC_IMAGE_003]]

Sources: US Energy Information Administration; National Bureau of Statistics of China; expert interviews; BCG Henderson Institute analysis. Note: TWh = terawatt-hours. Because of rounding, not all bar segment totals add up to 100%. $^{1}$ Does not include power imports.
$^{2}$ Includes hydropower, geothermal, nuclear, biomass, and wood-derived fuels. $^{3}$ Includes natural gas, coal, and petroleum products.

## The Path to Scale in Texas

In Texas, over just a decade, wind and solar tripled their share of the state's power generation, from about $10\%$ in 2015 to roughly $30\%$ in 2024. Four key findings in our model played significant roles in the buildout.

First, our analysis identified demand growth as an important driver in the US—and it was certainly a factor in Texas, with total power generation climbing from around 450 terawatt-hours (TWh) to nearly 570 TWh. Second, access to low-cost land underpinned the scale-up of renewables in Texas. Third, in many places that affordable land boasted some of the country’s strongest and most consistent wind or ranked among the sunniest places in the US. Fourth, the state government prioritized development of grid infrastructure: Texas proactively invested in 3,600 miles of high-voltage transmission lines to connect designated Competitive Renewable Energy Zones in resource-rich, remote parts of the state to regions with high electricity demand. This buildout of transmission infrastructure, along with the state’s deregulated market structure, helped incentivize developers to invest in new generation capacity.

## Building on Advantage in Gansu

For its part, the Chinese province of Gansu posted the nation's second-highest growth in renewables capacity from 2015 through 2024, despite having only average solar and wind resources in comparison to other Chinese provinces. Scrutiny of the buildout brings three factors to the forefront.

First, the province already had a strong base of existing wind power, most notably in the form of the Jiuquan wind power base, one of the largest wind farms in the world. This made Gansu, with its well-established supply chains, local know-how in the construction sector, and proven business case, appealing for future investors. Second, Gansu province has the fourth-lowest land prices in China—one-sixth the national average. Third, even though there is little local demand, the province has directed major investment toward infrastructure, ranking it in the top six provinces in terms of share of GDP spent on utilities.

Understanding the elements of the business case that have an outsize impact on how renewables scale is a critical first step. From there, companies and governments should examine how those factors intersect with their own plans and efforts.

For companies, insights from the model can help formulate the right questions to ask about future investments and identify steps to strengthen the business case. For instance, which regions have affordable land and an ecosystem of experienced renewable players to drive efficient development? What can companies do to ensure access to reliable grid infrastructure when needed? And where is the strongest growth in demand likely to occur?

For policymakers who want to attract investment in renewables, the most critical questions center on which measures can help reduce the land costs for renewable developers and which proactive strategies pursued today can attract the transmission investment required to transmit solar and wind power tomorrow.

Policymakers and companies can also explore how to partner to improve the overall economics of renewable scaling. When public-sector actions create the conditions for viable projects—and private capital responds with scale, execution, and expertise—renewable deployment accelerates.

The authors thank Jamie Webster, Lars Holm, and Grace Keliher for their assistance in the research for this article.

The BCG Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and

experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors


Managing Director & Senior Partner; Chair, Center for Energy Impact
London


Managing Director & Partner
Beijing


## Ross LaFleur

Managing Director & Senior Partner
Dallas

Cédric Hazevoets

Alumnus


## Khushboo Goel

Partner


## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

renewables refers exclusively to solar and wind.
