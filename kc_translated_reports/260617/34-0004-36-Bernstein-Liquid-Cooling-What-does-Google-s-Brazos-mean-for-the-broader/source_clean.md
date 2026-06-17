# U.S. Multi Industry & Electrical Equipment
# Liquid Cooling: What does Google's Brazos mean for the broader CDU ecosystem?
## Specialist Sales

Google recently released early specifications for a liquid-to-air (L2A) CDU named "Brazos". Like project "Deschutes" that came before it in 2025, Brazos simply announces a CDU reference design for the Open Compute Project's vendor ecosystem (which counts Vertiv, nVent, and Boyd as members) to produce. It is not a competing product to Vertiv/Boyd/nVent/Motivair's existing L2A CDU lines that Google will manufacture; hyperscalers are not in the business of making this equipment.

Prima facie, the specifications on Brazos-class CDUs seem relatively low. At 60kW of cooling capacity, it cannot even cool one Blackwell rack (which requires \~120kW of cooling capacity). Interestingly, Brazos-class CDUs are designed to draw DC power (vs. many other L2A CDUs that are designed for AC power instead).

We believe these CDUs are designed to be OCP compliant, and fit into legacy hyperscaler deployments which tend to have DC power infrastructure already. The cooling capacity of 60kW does not work well for frontier training models, but can support inference at that range. Given concerns around how quickly data center capacity can get up and running, creating an inference ecosystem that can run in existing facilities with simple L2A CDU retrofits seems like a good move (especially when inference looks set to grow faster than training through 2030). While not explicitly stated, we infer that this is the primary purpose of the Brazos project.

While hard to quantify, we see two mid-term risks for CDU manufacturers. First, there is real commoditization risk of the inference CDU ecosystem. Brazos specs are meaningfully easier to deliver than Deschutes. While there will be a service attach, margins will be lower vs. flagship training CDUs. The deciding factor here is inference rack densities; we are unsure what this looks like for purpose-built inference silicon from hyperscalers. If it remains around 60 kW/rack, then a meaningful share could be cooled by L2A Brazos-style CDUs. If not, larger Deschutes-class CDUs will be needed instead (which we would expect have higher margin and stickier service attach).

Second, we may also see some hyperscaler demand shift from greenfield to retrofits, especially if projects get delayed. While we do not see that in stranded capacity numbers in our data center capacity tracker, there has been some anecdotal input from companies that they are seeing a few customers (both hyperscalers and colos) push out deliveries because of a lack of readiness / project delays. We're not saying this WILL happen, but we think having these standardized L2A CDUs creates optionality for hyperscalers if they need to accelerate retrofits to meet inference demand in the future.

We do not view this announcement by Google as imminently alarming for CDU manufacturers, especially those that focus on technical excellence at the top of the stack. Some level of CDU commoditization was always expected by the market. While we think this announcement accelerates the commoditization trend for lower spec. products, we still believe an innovation premium exists for flagship CDUs, and expect it to continue as top-tier liquid cooling technology evolves.


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Vertiv Outperform with a target price of \$416.

We rate nVent Outperform with a target price of \$218.

We rate Schneider Outperform with a target price of €310.

We rate Eaton Outperform with a target price of \$534.

## DETAILS

## Context

Hyperscalers have historically pushed the "Open Compute Project" or OCP, a non-profit that published open-source specifications for data center hardware. Founded by Meta, it now has participation from Google, Microsoft, and Oracle (although Amazon is a notable missing name) and a host of other vendors. In 2025, Google published details of Project Deschutes as a part of the OCP; this was a set of technical specifications and standards for compliant Liquid to Liquid (L2L) CDUs (with 2MW of cooling capacity at a $3^{0}\mathrm{C}$ approach temperature). Vertiv, nVent, and Boyd all now have Deschute-compliant units available in their product catalogs. Yesterday, Google announced that they would specify another CDU design - this time for Liquid to Air (L2A CDUs) named project Brazos (in line with Google naming these projects after rivers). This note walks through implications for the broader CDU ecosystem.

## L2L vs. L2A: What's the difference?

In our CDU primer earlier this week, we focused mostly comparing on flagship L2L CDUs. L2L units are named as such because they reject heat between two liquid loops (the technology cooling system and facility water system). In contrast, the L2A configuration we are talking about today only has one liquid loop (the technology cooling system) which rejects heat as air into the "hot aisle" of a data center. A CRAH or CRAC (Computer Room Air Handler or Computer Room Air Conditioner) then blows the hot air out of the hall / building. Generally, L2L cooling is preferred for all greenfield builds or situations where rack densities cross 150kW (it is much more energy efficient). In contrast, L2A builds are preferred when retrofitting an existing data center because it does not need the facility water system loop (eliminating the need for complex piping retrofits) or when cooling capacities range between 40kW to -150kW (below which plain old - but cold - air can be used to extract heat from the chips). Both L2A and L2L are still types of liquid cooling (i.e., they need cold plates and coolant to extract heat from chips), they simply differ in terms of how they reject heat from the TCS to the outside of the data center.

EXHIBIT 1: Distinction between Liquid-to-Air and Liquid-to-Liquid CDUs

[[KC_IMAGE_001]]


Source: Bernstein Analysis and Estimates

## Thoughts on Brazos specifications

When we look at the specifications offered by Brazos, prima facie it does not look that impressive or demanding. 60kW of capacity cannot cool even a single Blackwell rack (which requires \~120kW of cooling power) - players like nVent, Motivair, and CoolIT go far higher on their cooling power for L2A CDUs. The power feed is DC (not AC) and designed to be pulled directly from busbars which is distinct from most other L2A CDUs available in the market today which are designed for AC use.

EXHIBIT 2: Project Brazos Overview
What exactly is Google Brazos?

[[KC_IMAGE_002]]


Source: Bernstein Analysis, Company Reports (Google)

• Google announced a new Liquid to Air (L2A) CDU configuration called "Brazos"
- Largely aimed at servicing older environments where providers are attempting to offer higher rack densities without complexity of chiller and piping retrofits
- Offers \~60kW of cooling capacity per rack; not enough for Blackwell (which is 120kW+ per rack) or higher end training models
- As per Google: "Brazos functions as a self-contained liquid ecosystem, capturing heat via liquid at the component level and rejecting it into the data center's hot aisle using high-efficiency liquid-to-air heat exchangers. This plug-and-play architecture can be rapidly installed in any legacy facility that has sufficient power and standard air handling."
• We want to highlight that this is not new tech.; L2A cooling has existed for years before Google made this announcement

EXHIBIT 3: Brazos L2A CDU specs. seem to target inference in OCP compliant environments

[[KC_IMAGE_003]]


1 Cooling power is too low to work with Blackwell or above; seems like Brazos is more focused on inference capacity through retrofits
2 Direct DC connectivity via OCP-compliant busbar is unique to Brazos vs. other L2A CDUs; will not work in legacy colocation / enterprise builds
Source: Bernstein Analysis and Estimates, Company Reports

However, our biggest takeaway is that this design is not intended to compete with existing products. It is designed to be OCP compliant, and fit into legacy hyperscaler deployments which tend to have DC power infrastructure already and not AC. The cooling capacity of 60kW does not work well for frontier training models, but can support inference at that range. Given concerns around how quickly data center capacity can get up and running (see our data center tracker for more insight on that), creating an inference ecosystem that can run in existing facilities with simple L2A CDU retrofits seems like a smart move (especially when inference looks set to grow faster than training through 2030). While not explicitly stated, we think this is the primary use case of the Brazos project.

## Our inferred implications on the CDU market

First, it is important to state what Brazos is not. It is not a CDU that Google is building; they are not in the business of making liquid cooling equipment. It is simply a set of technical specifications / requirements they will put out for their manufacturer ecosystem to build. As per Google: "In the coming months, we will formally open-source the technical specifications, design principles, and visual assets of Brazos through industry forums. As part of a broader infrastructure portfolio that continues to leverage waterless air-cooled systems alongside liquid cooling, Brazos represents one of many innovations we are contributing to the open hardware ecosystem. We invite system architects, manufacturers, and thermal engineers to evaluate these designs to scale rack-mounted cooling infrastructure for the high-power computing demands of the future." We also do not think this creates a structural near-term shock. CDUs will continue to see extended lead-times, and we expect L2L to be where most manufacturer focus stays.

We see two major risks for the mid-term. These are hard to quantify, but also cannot be ignored. First, there is real commoditization risk of the inference CDU ecosystem. Brazos specs. are meaningfully easier to deliver than Deschutes, and we believe they don't really need the engineering premium of a Vertiv or nVent. While these players may still opt to build and service Brazos-specified units, margins will be lower. We think the service attach will still be meaningful, but hypothesize less "moaty" than they would be with training GW where the cost of failure in meaningfully higher. The deciding factor here is inference rack densities; we are unsure what this looks like for purpose-built inference silicon from hyperscaler. If it remains below 60 kW/rack, then a meaningful share could be cooled by L2A Brazos-style CDUs. If not, larger Deschutes-class CDUs will be needed instead (which we would expect have higher margin and stickier service attach). Second, we may also see some hyperscaler demand shift from greenfield to retrofits, especially if projects get delayed. While we do not see that in our stranded capacity numbers in our data center capacity tracker, there has been some anecdotal input from companies that they are seeing customers push out deliveries because of a lack of readiness / project delays. With that said, we do not view this announcement by Google as imminently alarming for CDU manufacturers, especially those that focus on technical excellence at the top of the stack. Some level of CDU commoditization was always expected by the market. While we think this announcement accelerates the commoditization trend for lower spec. products, we still believe an innovation premium exists for flagship CDUs, and expect it to continue as top-tier liquid cooling technology evolves.

EXHIBIT 4: McKinsey and Co. Estimates of GW add by category

[[KC_IMAGE_004]]


Note: Includes all provider types.
\*Per annum.
Source: McKinsey Data Center Demand Model
Source: Company Reports (McKinsey and Co.)

EXHIBIT 5: Recap: How does Liquid Cooling work?

[[KC_IMAGE_005]]


[[KC_IMAGE_006]]


[[KC_IMAGE_007]]


## Glossary of liquid cooling terms

• DTC (Direct to chip)
• TCS (Technology cooling system)
• FWS (Facility water system)
• TDP (Thermal Design Power)

Source: Bernstein Analysis

EXHIBIT 6: Recap: Our CDU outlook

## CDUs | We think CDUs are here to stay; some commoditization risk (but less than cold plates)


Source: Bernstein Analysis and Estimates, Company Reports

Practically no obsolescence risk; we think CDUs are here to stay regardless of the dominant cooling config.

Some commoditization risk; hyperscalers will specify designs but CDUs are more complex (multiple connected pieces) than cold plates which preserves pricing power

In addition, CDUs need service (which cold plates do not) which also defends margin

We think CDUs are a great business to be in, ESPECIALLY for companies that can drive the innovation roadmap vs. just become contract mfg.

We see wide dispersion of forecasts for broader CDU market; but an LSD \$B market size today growing MSD/HSD \$B in the next 5 years does not seem too improbable
