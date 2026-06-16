# U.S. Multi Industry & Electrical Equipment
# Liquid Cooling Primer: Coolant Distribution Units (CDUs)
## Specialist Sales

As rack thermal densities in data centers continue to increase, air is no longer powerful enough to handle cooling requirements. And so liquid cooling, once a fridge modality relegated to only the highest-performance computing use cases, increasingly finds itself in the mainstream. At the core of liquid cooling, two components drive the narrative (CDUs and Cold Plates). In this note, we offer perspectives on CDUs, why they are critical, how to evaluate them, key players in the market and their offerings, and a longer term view on what the future for the equipment could look like when the market eventually cools down (pun intended).

We think CDUs are a great business to be in; the equipment is complex enough to not be entirely commoditized and has a material service attach. They are mission-critical; if a CDU fails you are looking at multiple racks burning out (which is a huge issue today when rack values continue to increase). This also creates a technical moat where customers will want reliable service; they are unlikely to go to the lowest cost provider in the market because the cost of failure far outweighs the near-term savings a cheaper service contract can deliver.

While we have not opined on the market size of CDUs, there is clearly debate on both size and growth rates. We are comfortable with an LSD \$B market size for 2026, growing double digits (mid-teens+) over the next 5 years to get to MSD-HSD \$B by 2030. We have developed a proprietary liquid cooling model for this to be modeled; but market size is highly sensitive to GW added, cost per kW of cooling and CDU useful life (all of which are seeing debates). Reach out to the authors or your Bernstein sales contact if you'd like a walkthrough of how to use it.

Looking at the actual CDUs launched in the market today, there are many players, but not everyone is innovating or has a large scale unit. Players in the NVIDIA liquid cooling ecosystem (Vertiv, nVent, Boyd, Motivair) all have great products. Trane Technologies punches above its weight. Carrier and JCI have CDUs but given they are more focused on chillers, we found their CDU breadth, specifications, and level of detail provided to not be at the same level as the other names in this list. CoolIt seems to be more of a cold plate name; their approach temperature lags competitors.

As we think about the next five years, we believe that technology roadmap visibility (which comes from being a partner of NVIDIA since they really set the direction of change) and participation in the Open Compute Project (OCP) create a right to win (because it deepens hyperscaler relationships and creates a pathway for long-term demand generation); and not many companies can say they have both.

Lastly, we think the shift to two-phase DTC cooling (from single-phase) should be closely watched. Only Vertiv and Accelsius (from the companies we have mentioned in this note) have actually announced products / published detailed perspectives. While we're still at least a year out from commercially scaled offerings (if not more), and most other companies serious about liquid cooling are likely working on a product, the step-change in engineering from this shift has the potential to disrupt the market and position occupied by key players.


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate VRT Outperform with a target price of \$416.

We rate NVT Outperform with a target price of \$218.

We rate CARR Market-Perform with a target price of \$75.

We rate TT Outperform with a target price of \$550.

We rate JCI Outperform with a target price of \$176.

We rate Schneider Outperform with a target price of €310.

We rate Eaton Outperform with a target price of \$534.

## DETAILS

EXHIBIT 1: CDU Outlook Summary

## CDUs | We think CDUs are here to stay; some commoditization risk (but less than cold plates)


Practically no obsolescence risk; we think CDUs are here to stay regardless of the dominant cooling config.

Some commoditization risk; hyperscalers will specify designs but CDUs are more complex (multiple connected pieces) than cold plates which preserves pricing power

In addition, CDUs need service (which cold plates do not) which also defends margin

We think CDUs are a great business to be in, ESPECIALLY for companies that can drive the innovation roadmap vs. just become contract mfg.

We see wide dispersion of forecasts for broader CDU market; but an LSD \$B market size today growing MSD/HSD \$B in the next 5 years does not seem too improbable

EXHIBIT 2: Comparison of Flagship Liquid-to-Liquid CDUs across OEMs


Note: Liquid-to-liquid only; We have focused primarily on CDUs released around or after mid-2024; OEM specs are often intentionally complex; we have made our best attempt at representing data here; 1. Nominal; 2. Approach temp. differential; 3. Unclear if water / PG25; 4. Inferred from spec sheet at 690 lpm; 5. Unclear if water/PG25 rated; 6. Water rated (so actual numbers will be lower); 7. CoolIT published different specs for the same product; we have used PDP details; CHx1500 not shown as it does not have a distinct PDP; 8. $^{2}$ °C ATD available using a high-efficiency heat exchanger
Source: Bernstein Analysis and Estimates, Company Reports

## INTRODUCTION

In the past, a continuous flow of cool air over servers was sufficient to cool data centers. With time, chips and racks have grown increasingly dense, to the point where even freezing cold air blowing at gale force speeds wouldn't do the job. Needless to say, finding an alternative cooling modality became critical. And so, liquid cooling technology, which long sat at the fringe of data center infrastructure, suddenly found itself thrust into the spotlight. Looking ahead, rack densities and chip TDPs seem set to keep growing, forcing liquid cooling solutions to evolve with more rigorous server demands.

## OVERVIEW OF LIQUID COOLING

Liquid cooling encompasses multiple different types of technology, with varying levels of efficiency and at distinct stages of maturity. At their core, they share one common principle; liquid flows over a surface (directly or indirectly) and uses principles of convection to extract heat. We describe five modalities of liquid cooling below:

1. Single-phase DTC: The predominant format of liquid cooling today. DTC stands for Direct-To-Chip. It involves cold plates (which are aptly named slabs of metal that have reduced temperature due to refrigerant that circulates inside them) coming into contact with racks / chips to extract heat. Coolant Distribution Units (CDUs) pump low temperature coolant (usually a water - propylene glycol mix) through the plates and recollect the spent liquid once they have extracted heat from the server. The heat is then extracted from the coolant (making it cold again) and the process repeats. It is called single phase because the coolant stays in a single phase (liquid) and does not change phases from to gas via evaporation. This loop (i.e., circulating from the CDU through cold plates in the server) is called the TCS or technology cooling system. Once spent coolant reaches the CDU, it passes through a heat exchanger where it transfers heat to another cooling loop called the FWS or Facility Water System. The FWS connects to a chiller or dry cooler to reject this heat outside a data center. However, as rack power densities continue to increase, single phase DTC is seemingly reaching the theoretical limit of how much heat it can extract.
2. Two-phase DTC: The principles remain exactly the same as single phase DTC, but in this case the liquid coolant boils and evaporates when it comes in contact with the server after absorbing heat. Evaporation requires significant energy, so it enables the refrigerant to extract a lot of heat without having its own temperature rise too much. In most cases, the refrigerant is maintained as close to its boiling point as possible. Not yet mainstream, but a number of companies are experimenting at the lab scale and approaching commercial maturity (which is expected over the next couple of years). It is worth noting that capacities of CDUs that support two-phase liquid are limited; Accelsius for example has a relatively mature offering and their highest capacity CDU is well below 1MW (vs. 2MW+ for single phase cooling). Equipment (both CDUs and cold plates) need to be designed differently for two-phase; gas flowing through an ecosystem behaves much differently from liquid.
3. Immersion cooling: Once a competitor to DTC, now largely relegated to niche applications. Does not need cold plates; the entire server is submerged in dielectric (i.e., non-conducting) fluid which extracts heat. Has both single phase and two-phase versions. Fell off due to convenience; cold plates can rapidly be replaced and servers can still be maintained with relative ease, in contrast, immersion cooling requires a large tank to be moved, and a wet server to be extracted and dried before any work can be done on it. R&D is still taking place, but hyperscaler roadmaps clearly lean towards DTC.
4. Cold plate etched DTC: Micro-channels are etched into the surface of a cold plate to improve contact with the chip surface. Enables better heat transfer compared to traditional single phase or two-phase DTC but still very nascent tech.
5. Silicon-etched DTC: Forgoes cold plates entirely and etches cooling channels on the surface of the chip itself. Very nascent, unlikely to see commercialization before the end of the decade, although key players like Microsoft and TSMC are making investments here.

The reason we have laid out these technologies is that it has implications on the outlook of equipment that make up the liquid cooling ecosystem. CDUs and cold plates are the most important to discuss. CDUs (Coolant Distribution Units) are essentially responsible for controlling the distribution, flow, and pressure of coolant across multiple rows and racks. Cold plates receive coolant from CDUs (via a manifold) and absorb heat through their surface before returning the spent coolant to the CDU. Both these components are seeing significant demand (and shortages today) and there has been a flurry of investment activity in the space with larger players making strategic investments and acquisitions (e.g., JCI investing in Accelsius, Eaton acquiring Boyd). In today's note, we focus specifically on CDUs.

EXHIBIT 3: Overview of Liquid Cooling and Key Components

[[KC_IMAGE_001]]


[[KC_IMAGE_002]]


[[KC_IMAGE_003]]


[[KC_IMAGE_004]]


Source: Bernstein, Company Reports

EXHIBIT 4: Still Early Days for Liquid Cooling
Evolution of frontier GPU rack computing power
Rack power (kW) for frontier chips

[[KC_IMAGE_005]]


All power used by GPUs gets converted to heat; an exponential increase in heat generated translates into an exponential need for cooling

[[KC_IMAGE_006]]


Our focus for this discussion
Source: Bernstein Analysis and Estimates

EXHIBIT 5: Single Phase DTC Dominant Today, and Two-Phase Seems to be the Future


[[KC_IMAGE_007]]


OVERVIEW OF KEY PIECES OF EQUIPMENT

EXHIBIT 6: Key Equipment in Liquid Cooling Landscape


Source: Bernstein Analysis, Company Reports

Multiple pieces of equipment tie together to make liquid cooling work. A quick summary of each of these pieces of equipment is provided below (along with a deep-dive on CDUs).

1. CDUs: The beating heart of the liquid cooling ecosystem. Responsible for the interplay of two thermal loops (TCS and FWS). The TCS (or technology cooling system) pumps low-temperature coolant from the CDU to the server where it extracts heat generated by chips and recirculates it back. In the CDU, a heat exchanger transfers this collected heat from the spent coolant to the FWS (Facility Water System), effectively lowering the coolant temperature again. The heated water in the FWS then connects to a chiller or dry cooler to reject heat outside the data center.
2. Cold Plates: Pieces of metal that sit in the server and extract heat from racks by contact. Cold plates are cooled by the coolant (pumped by the CDU) that flows through them. More complex cold plate designs and geometries enable better heat transfer but also need higher pressure from the CDU. These are effectively consumable units; there is little to no service possible on them and the value of a cold plate is all in the design (fabrication is much simpler once you have a blueprint).
3. Manifolds: These are engineered pieces of equipment that control the flow of coolant from the CDU into the server / cold plate. They need to be highly engineered to ensure not even a drop of the coolant spills (because it creates electrical and fire hazards if it falls on an operating chip). The “no spill disconnect” capability of a manifold, where a cold plate or CDU can be disconnected without any spillage of coolant is a critical piece of the engineering. While an important piece of the liquid cooling ecosystem, it is not at the same level as CDUs or cold plates.
4. Coolant / refrigerant: Usually a mix of water and propylene glycol at the TCS side for single phase DTC cooling, this is responsible for capturing and rejecting heat. PG25 (a mix of 25% propylene glycol and 75% water) is the standard. While not as thermally conductive as water, it inhibits microbe growth, and has less corrosion risk, so engineers prefer using it. Some higher performance coolants also exist, but this is largely the standard. In the case of two phase DTC or immersion cooling, very different refrigerants will be needed. For example, in the case of two-phase DTC, the liquid needs to boil at relatively low temperatures. Similarly in the case of immersion cooling, the liquid needs to be non-conducting and generally exclude water to prevent corrosion risks.

5. Immersion tanks: Only needed in immersion cooling, not required for DTC. Large tanks that servers can be immersed into. Great heat transfer capabilities (especially with forced convection) but extremely tedious to maintain and service.

EXHIBIT 7: Product Coverage by Different OEMs


We think it's in JCI / Carrier's best interest to keep these as vestments as optionality for now – but not to make a full acq. unless commoditization risk for cold plates is managed
There is also a case to be made for diversification of technologies; there is uncertainty around what the mid to long-term roadmap would look like and most players (ex-Vertiv) seem to be committing to either 2-phase DTC or immersion cooling
Source: Bernstein Analysis, Company Reports

Interestingly, companies are making different implied bets on what the future of liquid cooling will look like. Vertiv is perhaps the only name in the above exhibit that is playing all angles; they try and invest everywhere to make sure regardless of which direction roadmaps go they are positioned to win. But other companies are more intentional; for example, Trane Technologies has a great single phase DTC CDU today (probably the highest capacity in the market) but has shown limited visibility on two-phase DTC. Similarly, Carrier and JCI have invested in ZutaCore and Accesius respectively which are innovating in two-phase DTC, but are not really focused on immersion. That being said, it does seem to be a great time to be a nice player that focuses on any part of the liquid cooling ecosystem; larger companies are snapping up targets with fervor (and at princely multiples) as they look to cover up any portfolio gaps they have.

## OUR PERSPECTIVE ON CDUS

We are quite bullish on the outlook for CDUs. They are central to making liquid cooling work and have practically no obsolescence risk (they are a key part of the cooling ecosystem in all five architectures we discussed earlier). They are large, highly engineered pieces of equipment with multiple interconnected pieces that require regular servicing - which creates a recurring revenue stream once installed (very similar to chillers). And because they are mission-critical (i.e., if a CDU goes down multiple racks go down with it), we also do not think customers will choose lower cost service providers because the cost of failure far outweighs the savings from a cheaper service contract. The market is heavily supply constrained today; while OEMs continue to add capacity we expect backlogs to remain elevated in the near-mid term.

It is worth noting that there is some commoditization risk (especially longer-term); hyperscalers have been specifying designs via the OCP (Open Compute Project) led by Google's Project Deschutes. But even with some inevitable pricing pressure from this on the top line, we think OEMs will have negotiating leverage on service contracts. With all this said, we are hardly at a point in the technology lifecycle where products can be completely specified because of the pace of innovation. It is still early days in the ecosystem, and we think near-term winners will be those that can continue innovating on the product roadmap (e.g., driving the shift from single-phase to two-phase DTC).

It has been challenging placing an exact size to the market; most outlooks vastly differ in both overall opportunity and growth potential. We think an LSD market size today, growing double digits annually to MSD/HSD by 2030 is a fair assumption to make. Perhaps it could even go higher, but that depends on the share of the market that switches to liquid cooling and how quickly GW come online. To help assess this, we have also developed a data center cooling model where assumptions can be plugged in (GW, share of liquid cooling, CDU cost / kW, etc.) to deliver an implied market size. If you are interested, please reach out to the author team / your Bernstein sales contact, and we will find time to walk you through how to use this model.

## EXHIBIT 8: CDU Outlook Summary

## CDUs | We think CDUs are here to stay; some commoditization risk (but less than cold plates)


Source: Bernstein Analysis and Estimates

Practically no obsolescence risk; we think CDUs are here to stay regardless of the dominant cooling config.

Some commoditization risk; hyperscalers will specify designs but CDUs are more complex (multiple connected pieces) than cold plates which preserves pricing power

In addition, CDUs need service (which cold plates do not) which also defends margin

We think CDUs are a great business to be in, ESPECIALLY for companies that can drive the innovation roadmap vs. just become contract mfg.

We see wide dispersion of forecasts for broader CDU market; but an LSD \$B market size today growing MSD/HSD \$B in the next 5 years does not seem too improbable

## COMPARISON OF KEY PLAYERS IN THE MARKET

Naturally, as liquid cooling has accelerated, every player with even a tangential play in the space has tried launching a CDU. But not all CDUs are created equal. In this section of our primer, we lay out how one should evaluate products, how CDU manufacturers try and obfuscate data to make comparisons hard, compare products across some major names, and share a POV on who we think is best positioned to win looking ahead.

First, let's talk about what matters in a CDU. There are dozens of technical specifications that are thrown around; while all matter in their own unique ways, we specifically call out four to keep an eye on:

1. CDU capacity: Usually represented in kW or MW, this represents the actual cooling power a CDU can deliver. More cooling capacity = more racks or servers that the CDU can cool. Capacity is generally represented as a “nominal” figure, which represents the amount of cooling power that a CDU can deliver when it operates under conditions as intended.

It is also sensitive to the liquid flowing through it; for example, if a CDU runs pure water vs. PG25 as the coolant it will have a higher capacity (by \~10 - 20%); but this is misleading because PG25 is probably the fluid that a hyperscaler will use when operating a CDU. Similarly, a CDU running at a high approach temperature difference will have a much higher cooling capacity than one with a low approach temperature difference; but hyperscalers almost always run at lower approach temperatures differences so the higher capacity is a meaningless number. As CDU sizes continue to grow, flagship capacities of >2MW are the new baseline.

2. Approach temperature difference (ATD): This represents the difference between the FWS and TCS loops. Essentially, an ATD of $4^{0}C$ means that chilled water in the FWS can be at $30^{0}C$ , and that will cool the TCS loop to $34^{0}C$ (the difference between these loops is the ATD). The reason you want this to be low is that it signifies efficiency; a low ATD means you need to spend less energy cooling you FWS creating cost savings. A high ATD means that your CDU is doing a bad job transferring heat between the TCS and FWS. $4^{0}C$ is a common approach temperature for flagship CDUs; $3^{0}C$ is not unheard of (especially with OCP specified CDUs) and Carrier has gone as low as $2^{0}C$ (although this is using an add-on high efficiency heat exchanger and likely under certain specific conditions).
3. Flow ratio: We define the flow ratio as the nominal flow rate of coolant in the TCS (designated in liters per minute or lpm) divided by the nominal capacity of the unit (designated in kW/MW). It signifies how much coolant flows for each unit of heat you are removing. Too low, and the chips will overheat. Too high, and you're wasting energy pumping too much fluid through the server. The gold standard of flagship CDUs today is around 1.5 lpm / kW or more.
4. Pressure head: Cold plates often have complex geometries, and fluid needs to be pushed through it with enough force. If not, it can pool or stagnate and struggle to return to the CDU from the server. For this to be done, the CDU needs to pump with enough intensity (measured by the pressure head). For bigger CDUs, a head of >50 psi seems to get the job done; hyperscalers in the OCP seem to spec. at 80 psi.

The challenge is not in getting just one of these metrics to the level hyperscalers need; that is easy to do. The issue is improving one metric has a direct, negative impact on another (either listed above or the cost to operate a unit). SO CDU OEMs need to carefully engineer offerings to meet all customer requirements while keeping operating costs reasonable.

EXHIBIT 9: CDU Assessment Criteria


Source: Bernstein Analysis and Estimates

With this as context, we ran a comparison of key CDU OEMs in the market today. While the manner of reporting makes it hard to create an apples-to-apples point of view, we have used our judgment to develop a robust point of view below.

EXHIBIT 10: Comparison of Flagship Liquid-to-Liquid CDUs across OEMs


Note: Liquid-to-liquid only; We have focused primarily on CDUs released around or after mid-2024; OEM specs are often intentionally complex; we have made our best attempt at representing data here; 1. Nominal; 2. Approach temp. differential; 3. Unclear if water / PG25; 4. Inferred from spec sheet at 690 lpm; 5. Unclear if water/PG25 rated; 6. Water rated (so actual numbers will be lower); 7. CoolIT published different specs for the same product; we have used PDP details; CHx1500 not shown as it does not have a distinct PDP; 8. $^{2}$ °C ATD available using a high-efficiency heat exchanger
Source: Bernstein Analysis and Estimates, Company Reports

Our key observations looking at the data:

- Companies in the NVDA power / cooling partner ecosystem (Vertiv, Motivair, Boyd, nVent have great coverage) - a good mix of rack-level CDUs (largely designed to be retrofit friendly) and row / perimeter units for greenfield hyperscaler builds
- Only three companies have an OCP compliant CDU based on specs from Google's Deschutes 5.0 (Vertiv, nVent, Boyd); it is surprising to not see more names there. OCP specs seem to need a very high level of engineering, so we wonder if there's a technical gap with the other players preventing them from delivering these specs.
- Most flagship CDUs deliver cooling power at 2MW or more; if a company does not have a >2MW CDU we think it impacts credibility (standalone, not skid).
- Approach temperature differentials seem to be reliably at $3^{0}\mathrm{C}$ for top tier products; while Carrier does claim a $2^{0}\mathrm{C}$ approach temperature they caveat this as needing a high-efficiency heat exchanger. It is theoretically possible for any company to lower approach temperatures, but that has an impact on cooling power delivered; Carrier's spec sheet did not have a significant amount of detail so we would believe this $2^{0}\mathrm{C}$ works only under specific circumstances and is unlikely to be a nominal number.
- Trane punches above its weight; the Giga-modular CDU seems to have the highest single unit capacity on the market and seems to be addictively modular up to 14MW.
- Carrier and JCI seem to de-prioritize CDUs vs. their chiller portfolio; they do not have anything >2MW without skids and JCI's CDU also has a higher approach temperature difference ( $5^{0}C$ vs the $4^{0}C$ standard) when you use PG25 as a coolant.

## LOOKING AHEAD

We continue to emphasize the importance of being an NVDA partner when trying to identify what drives success in liquid cooling longer-term. This is because NVIDIA largely sets power and cooling standards the rest of the industry follows (e.g., even with liquid cooling and 800V DC), and we expect they will also do so when the time comes to shift to two-phase DTC. Currently, Vertiv, nVent, Boyd (via Eaton) and Motivair (via Schneider) are all plugged into NVIDIA's roadmap. Trane is connected on the facility cooling side, but we think that still gives them visibility to white space cooling requirements. In contrast, JCI, Carrier, CoolIT, Accelsius are not looped in which we think is a detriment to their long-term right to win in CDUs specifically.

We also think having OCP compliant CDUs and working with hyperscalers through that model will help create longer-term demand. Only three companies (Vertiv, nVent, and Boyd) currently have OCP compliant CDUs on the program website. While not an immediate factor to success, OCP-compliant CDUs are high spec., and we think having this certification is a signal that these three players are (i) able to deliver the highest level of technical requirements for CDUs and (ii) are building engineering relationships with hyperscalers outside project-level conversations that will pay off in the longer-run.

Lastly, looking at two-phase DTC, we see divergent levels of investment by players. Vertiv and Accelsius seem to be furthest along with actual units being displayed. Boyd comes next; they do not have explicitly mentioned two-phase CDU products, but they do have a history of two-phase cooling more broadly they can apply here. Schneider has recently published a blog post on two-phase but we have not seen much else from them yet. nVent and Trane have no major two-phase DTC announcements, but given they are looped into the NVIDIA ecosystem we would imagine they will develop a product when they need to (and given they innovate quickly, we are comfortable in their ability to deliver when they need to). JCI and Carrier are exposed to two-phase via equity investments in Accelsius and Zutacore respectively (but no direct products of their own). Lastly for CoolIT, we were unable to find any specific mentions of two-phase DTC (at least on CDUs).

EXHIBIT 11: Partnership Outlook by CDU OEM

[[KC_IMAGE_008]]


Source: Bernstein Analysis, Company Reports

EXHIBIT 12: Two-phase DTC Outlook by CDU OEM


Source: Bernstein Analysis, Company Reports
