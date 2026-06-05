# The Data Center Power Architecture Is Being Rewritten, and the Winners Are Those Who Control the Rack

The 2026 Taipei Computex was not a product launch event. It was a declaration that the data center industry has entered a structural transition phase where power, cooling, and optical interconnect are no longer supporting functions but the primary determinants of system performance and cost. The dominant narrative from the show floor is that the era of incremental improvements in server infrastructure is over. What we are witnessing is a fundamental rewriting of how power is delivered, how heat is removed, and how data moves within and between racks. For investors, the critical insight is not which component supplier has the highest market share today, but which companies are positioned to own the architectural decisions that will define the next generation of AI data centers.

The urgency of this transition is driven by a single, relentless force: the power density of AI accelerators. As chip thermal design power pushes beyond 2 kilowatts per unit, the traditional 48V power distribution architecture and air cooling are hitting hard physical limits. The industry is now converging on a new baseline: 800V high-voltage direct current power racks, liquid-to-liquid cooling for the highest-density deployments, and a multi-year migration from pluggable optics to co-packaged optics for scale-out networking. These three shifts are interconnected, and the companies that can integrate them into a coherent system-level solution will capture disproportionate value.

This article distills the key strategic signals from Computex 2026, interprets what they mean for the competitive landscape, and identifies the unresolved questions that will shape investment decisions over the next 18 to 36 months.


![Report chart 1](assets/source_image_01.jpg)

## The Shift to 800V HVDC Power Racks Is a Structural Tipping Point, Not a Niche Trend

The most consequential hardware transition on display at Computex was the widespread adoption of 800V DC power racks. Multiple suppliers, including Delta, Lite-on, and Vertiv, showcased systems aligned with Nvidia's reference design. This is not a minor specification upgrade. Moving from 48V to 800V distribution reduces current by more than an order of magnitude, which directly cuts resistive losses, allows for thinner copper cabling, and enables power delivery at the megawatt scale within a single rack.

The strategic implication is clear: power infrastructure has become a competitive bottleneck. Hyperscalers are no longer willing to accept the inefficiency and space consumption of legacy power architectures. The 800V rack is the industry's answer to the problem of feeding 100-kilowatt-plus racks without requiring a dedicated substation per row. Delta's emphasis on customizable configurations, including optional PDU integration, signals that the market is moving toward a solution where the power rack is not a commodity but a tailored system component.

For investors, the key question is who captures the value in this transition. The power rack itself is a system integration challenge, combining high-voltage conversion, battery backup, and monitoring. Delta's leadership position, with initial shipments expected in the second half of 2026, suggests that companies with deep expertise in high-voltage power electronics will benefit disproportionately. However, the transition also creates opportunities for connectivity players. As power racks scale, the power whips and connectors that link the rack to the server trays must be upgraded to handle higher currents and voltages. Bizlink, for example, is positioned to benefit from this ancillary but essential component upgrade cycle.

The timeline is also instructive. While 800V racks are shipping in 2026, the next generation of power technology is already visible on the horizon. Solid-state transformers and fuel cells were demonstrated at Computex, with commercialization likely around 2028. This means the current transition is not a one-time event but the first phase of a multi-year power architecture evolution. Companies that win the 800V cycle may not automatically win the SST cycle, but they will have the customer relationships and system integration credibility to compete.


![Report chart 2](assets/source_image_02.jpg)

## Liquid-to-Liquid Cooling Is Moving from Lab to Commercial Deployment, but the Adoption Curve Will Be Steeper Than the Industry Expects

The cooling track at Computex revealed a clear bifurcation in the market. For the next 12 to 18 months, liquid-to-air cooling will remain the dominant solution. It is simpler, cheaper, and sufficient for the current generation of AI accelerators. However, the number of liquid-to-liquid CDU samples on display was significantly higher than last year, and the specifications were notably more aggressive. Delta, Auras, and Vertiv all showcased CDUs exceeding 1 megawatt of cooling capacity, with commercialization expected in the second half of 2027.

This is a critical signal. The industry is preparing for a thermal environment that does not yet exist at scale. The reason is forward-looking: next-generation AI chips are expected to push beyond 2 kilowatts per unit, at which point liquid-to-air cooling becomes thermally inadequate. The hyperscalers are already planning their 2028 data center builds, and they are specifying liquid-to-liquid cooling as a requirement, not an option.

The strategic implication for component suppliers is significant. Jentech's micro-channel lid, currently under sample testing, is designed to support thermal design power above 2 kilowatts. Auras is developing two-phase liquid cooling cold plates. These are not incremental improvements; they are architectural changes that require new manufacturing processes and quality standards. The companies that can deliver reliable, high-volume thermal management solutions for 2-plus kilowatt chips will have pricing power and long-term customer lock-in.

But there is a tension in the timeline. The industry is developing liquid-to-liquid solutions for a chip generation that has not yet been formally announced. This creates a risk of over-investment in cooling capacity that may take longer to utilize than expected. The conservative view is that liquid-to-air will have a longer tail than the optimists assume, and that the transition to liquid-to-liquid will be more gradual, driven by the highest-density racks first. The aggressive view is that the hyperscalers will force the pace, demanding liquid-to-liquid readiness in all new builds starting in 2028.

Investors need to watch the actual deployment timelines of next-generation AI chips. If the chip roadmaps slip, the cooling transition will slip with them. But if the chips arrive on schedule, the cooling suppliers that have invested in liquid-to-liquid capability will be in a position of scarcity.


![Report chart 3](assets/source_image_03.jpg)

## Co-Packaged Optics Are Coming, But Copper Will Have a Longer Life Than the Market Currently Prices In

The optics discussion at Computex was the most nuanced and strategically important of the three major transitions. The headline is that CPO and NPO switches are coming for scale-out architectures. Multiple customer projects are underway, and 3.2T NPO for scale-out will be mainstream next year. The 6.4T CPO generation, with the optical engine on the substrate, is likely for 2028.

However, Jensen Huang's comment at the show that "use copper when you can" and that "we've made copper sexy again" is a deliberate counter-narrative. Nvidia's view is that copper still has significant runway in scale-up systems, and that CPO will be introduced primarily for rack-to-rack interconnects in the Feynman era. This is not a rejection of optics; it is a prioritization of cost and reliability for the highest-volume interconnects.

The emergence of XPO from Amphenol, Foxconn, and Arista adds another layer of complexity. XPO delivers four times the density of standard OSFP and enables 204.8T switching. Combined with co-packaged copper, this could extend copper's lifecycle within the rack by several years. The implication is that the death of copper has been greatly exaggerated. For scale-up, where distance is short and bandwidth density is paramount, copper may remain competitive through the end of the decade.

For investors, this creates a non-linear opportunity set. Pluggable transceivers will continue to dominate scale-out for the next two years, benefiting PCB companies like ZhenDing. But the CPO transition will begin in scale-out first, creating a window for companies that can supply both technologies. The unresolved question is when CPO crosses the cost-performance threshold for volume deployment. If CPO costs fall faster than expected, the copper extension narrative collapses. If CPO costs remain high, pluggable optics will have a longer lifecycle than the bulls assume.

## What the Report Does Not Fully Answer: The Integration Risk of Multi-Vendor Power, Cooling, and Optical Systems

The Computex exhibits showed impressive individual components. Delta demonstrated an integrated power and cooling module that cuts deployment time by 50 percent. Vertiv showed a similar integrated approach. Wiwynn and Ayar Labs showcased a scale-up CPO tray. But the report does not fully address the system-level integration risk that hyperscalers will face when they try to combine these technologies from multiple vendors.

A data center rack in 2028 will have an 800V power rack from one vendor, a liquid-to-liquid CDU from another, and an optical interconnect from a third. The interfaces between these subsystems are not standardized. The power rack must communicate with the cooling system to manage thermal load. The optical interconnect must be physically compatible with the rack's power and cooling architecture. The control software must orchestrate all three.

The report highlights that Delta and Vertiv are introducing integrated solutions that combine power, cooling, and connectivity. This is a strategic response to the integration problem. The companies that can offer a full rack solution will have a significant advantage over component-only suppliers. But the report does not quantify how much of the market will shift toward integrated solutions versus best-of-breed component selection.

This is the critical unknown for investors. If hyperscalers prefer integrated solutions, the winners will be the large system integrators like Delta. If hyperscalers prefer to mix and match best-in-class components, then specialist suppliers in cooling and optics will have more pricing power. The next 12 months of customer announcements and design wins will be decisive.

## A Decision Framework for Investors: Map the Technology Timeline to the Revenue Inflection Points

For investors trying to position in this transition, a simple but powerful framework is to map each technology shift to its revenue inflection point and identify which companies have exposure at each stage.

First, the power transition is the most imminent. 800V racks begin shipping in the second half of 2026. Revenue for power component suppliers and connectivity players will inflect in 2027. This is the highest-conviction near-term opportunity, but it is also the most crowded trade.

Second, the cooling transition is a 2028 story. Liquid-to-liquid CDUs will not generate meaningful revenue until late 2027 at the earliest. The component suppliers, such as those making micro-channel lids and cold plates, will see revenue earlier, but the volume will be small. The risk is that the market prices the 2028 opportunity too early, creating valuation risk if chip roadmaps slip.

Third, the optics transition is the longest and most uncertain. Pluggable transceivers will generate revenue through 2027. NPO will begin in 2027. CPO will not be material until 2028 at the earliest. The copper extension argument means that the total addressable market for optics may grow more slowly than the bulls expect. The best-positioned companies are those that can supply both copper and optical solutions.

The framework also highlights a risk that is often overlooked: the winners in one transition may not be the winners in another. The company that wins the power rack transition may not have the thermal management expertise to win the cooling transition. Investors need to assess each company's capability across all three domains, not just its current market share.

## The Unresolved Analytical Questions That Should Drive Further Research

Several important questions remain unanswered by the Computex exhibits and the report. First, what is the total cost of ownership advantage of 800V power racks compared to 48V systems at the data center level, not just the rack level? The headline numbers are compelling, but the full system cost, including transformers, switchgear, and backup power, needs to be modeled to determine the true economic incentive for migration.

Second, how will the hyperscalers' preference for integrated solutions versus best-of-breed components evolve? The report shows that integrated solutions exist, but it does not provide data on customer adoption rates or willingness to pay a premium for integration.

Third, what is the realistic timeline for CPO cost parity with pluggable optics? The report mentions that pluggable transceivers will dominate for two more years, but it does not provide a cost curve or a crossover point. This is the single most important variable for optical component investors.

Fourth, how will the trade and tariff environment affect the supply chain for these new technologies? Many of the key suppliers are based in Taiwan and China. The report acknowledges tariff risk for Delta but does not analyze the broader supply chain exposure for the entire ecosystem.

These questions are not weaknesses of the report; they are the natural consequence of an industry in transition. The answers will emerge over the next 12 months as design wins are announced and production ramps begin.

Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
