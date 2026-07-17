# U.S. Multi Industry & Electrical Equipment

# Liquid Cooling in Data Centers: What comes after single phase DTC? With CoolIT's 15kW cold plate, does anything even need to?

![](images/ac3bf935477a62b394e15aafca65c19ef8764e9c69c2e77aa1336bc4350f6804.jpg)

![](images/4ca769075ad28f5d23efeb1b41acc515d775d5e8fb0c0c902563a37aeb67e6da.jpg)

![](images/51350124eb3cc60bdd30d8a547ca1ef4c91cf3f6c3bdda5010bae35fe689e0c5.jpg)

![](images/db2f771299f0e602494784460e24006b32d57fd9430a37396125136126389e46.jpg)

![](images/8a7c3d78630a74c06e1c5024ac0ff9829d438be0c3571fd0f414840f5c033009.jpg)

Varun Govindaraj
+1 917 344 8543
varun.govindaraj@bernsteinsg.com

Chad Dillard
+1 917 344 8469
chad.dillard@bernsteinsg.com

Alasdair Leslie
+44 20 7762 4952
alasdair.leslie@bernsteinsg.com

Miguel Marques, CFA
+1 917 344 8432
miguel.marques@bernsteinsg.com

Om Kela
+44 20 7550 2192
om.kela@bernsteinsg.com

Specialist Sales

![](images/be6255847588a25760c890157e4b2322337b1aeb1be1df6680213d1179d89e60.jpg)

Steve Song
+1 917 344 8401
steve.song@bernsteinsg.com

When you hear the term “liquid cooling” today, most people are referring to single phase direct to chip (DTC). It’s called single phase because the coolant stays in a liquid state (and doesn’t undergo a phase change to vapor). The broader market seems to believe we are coming up on a theoretical limit on future generations of GPUs being cooled with single phase (especially as you start to reach TDPs around Rubin Ultra which are above \~2.5kW). Two technologies are seen as successors to single-phase DTC; (i) two-phase DTC and (ii) direct to die. These have been explained in more detail below.

Two-phase DTC: The more likely to see commercial viability in the next \~12- 18 months around the same time as Rubin Ultra. Undergoes a phase change (evaporation) of the coolant in a cold plate enabling it to capture more heat vs. single phase DTC operating at similar conditions. Most major players are likely investing in the space, either directly (e.g., VRT, CoolIT) or through partnerships (e.g., JCI with Accelsius, Carrier with ZutaCore, etc.). Still has real engineering challenges to solve for (backward flow, refrigerant choice, etc.) so it is by no means a done deal.

Direct-to-die: Eliminates the need for cold plates entirely by cooling through the silicon die itself. Far more technically complex and R&D is extremely early stage but could theoretically offer materially better heat flux vs. DTC. We do not expect to see anything happen at scale before 2030. Microsoft and TSMC are both making investments and have signalled activity (potentially manufacturing in 2026) but we're yet to hear anything about widespread adoption because of more practical challenges (e.g., deionized water causing corrosion to silicon).

The wildcard, CoolIT's 15kW single phase cold plate: About a month ago, CoolIt also announced that they're proven single-phase DTC could work with a cold plate rated at 15kW under relatively standard operating conditions (1.2 lpm, $45^{0}\mathrm{C}$ inlet temperatures, thermal paste, PG25 coolant, etc.). This is counter to the narrative that single phase won't work at GPU TDPs $>2.5\mathrm{kW}$ (CoolIT's number is 6x that). While the technology was tested in a lab scale setup as per their white paper, we do think this is a credible product. If it can be commercialized at scale, it essentially pushes out the need for two-phase DTC well beyond 2030. Most technological evolution on power and cooling in a data center is driven by necessity, and if we don't NEED two-phase or direct-to-die anymore, it's easier for data center operators to continue using single-phase cooling setups. If the 15kW cold plate can be commercialized, we think it has mixed implications on white space cooling equipment (CDUs and cold plates). On one side, there's less of a structural shift to new technologies that could create pricing pressure on these components (because the innovation premium starts to dry up) and commoditization may be accelerated. To be clear, it is unlikely to materially impact revenues or margins in the next couple of years since demand far outstrips supply, but it is a risk beyond that. It depends on how quickly competitors can replicate CoolIT's approach (which may not be immediate since they do have a patent on the underlying technology). On the positive side (for cold plates in particular), it does eliminate the obsolescence risk (since there's no real need for direct-to-die) for the foreseeable future.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">15 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>VRT (Vertiv)</td><td>O</td><td>USD</td><td>304.57</td><td>416.00</td><td>117.8%</td><td>USD</td><td>4.20</td><td>6.52</td><td>9.21</td><td>72.6</td><td>46.7</td><td>33.1</td></tr><tr><td>NVT (nVent)</td><td>O</td><td>USD</td><td>159.46</td><td>220.00</td><td>92.6%</td><td>USD</td><td>3.34</td><td>4.84</td><td>6.26</td><td>47.7</td><td>33.0</td><td>25.5</td></tr><tr><td>TT (Trane)</td><td>O</td><td>USD</td><td>480.20</td><td>555.00</td><td>(11.2)%</td><td>USD</td><td>13.06</td><td>14.98</td><td>17.82</td><td>36.8</td><td>32.0</td><td>26.9</td></tr><tr><td>CARR (Carrier)</td><td>M</td><td>USD</td><td>68.74</td><td>75.00</td><td>(30.1)%</td><td>USD</td><td>2.57</td><td>2.79</td><td>3.20</td><td>26.7</td><td>24.6</td><td>21.5</td></tr><tr><td>JCI (Johnson Controls)</td><td>O</td><td>USD</td><td>142.76</td><td>173.00</td><td>13.4%</td><td>USD</td><td>3.78</td><td>4.97</td><td>5.93</td><td>37.8</td><td>28.7</td><td>24.1</td></tr><tr><td>ETN (Eaton)</td><td>O</td><td>USD</td><td>412.86</td><td>534.00</td><td>(7.3)%</td><td>USD</td><td>12.07</td><td>13.45</td><td>16.37</td><td>34.2</td><td>30.7</td><td>25.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,572.40</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate VRT Outperform with a TP of \$416

We rate NVT Outperform with a TP of \$220

We rate TT Outperform with a TP of \$555

We rate JCI Outperform with a TP of \$173

We rate CARR Market-Perform with a TP of \$75

We rate ETN Outperform with a TP of \$534

## RECAP: OVERVIEW OF SINGLE-PHASE DTC COOLING

The predominant format of liquid cooling today is single-phase DTC. DTC stands for Direct-To-Chip. It involves cold plates (which are aptly named slabs of metal that have reduced temperature due to refrigerant that circulates inside them) coming into contact with GPUs to extract heat. Inside the cold plates, liquid flows through arrays and flow loops with the intent of maximizing the amount of heat they are able to extract from the GPU. Coolant Distribution Units (CDUs) pump low temperature coolant (usually a water - propylene glycol mix in single-phase setups) through the cold plates and recollect the spent liquid once they have extracted heat from the server.

The heat is then extracted from the coolant (making it cold again) and the process repeats. It is called single phase because the coolant stays in a single phase (liquid) and does not change phases from to gas via evaporation. This loop (i.e., circulating from the CDU through cold plates in the server) is called the TCS or technology cooling system. Once spent coolant reaches the CDU, it passes through a heat exchanger where it transfers heat to another cooling loop called the FWS or Facility Water System. The FWS connects to a chiller or dry cooler to reject this heat outside a data center. However, as rack power densities continue to increase, single phase DTC is seemingly reaching the theoretical limit of how much heat it can extract.

EXHIBIT 1: Direct-to-chip process overview  
![](images/2c4e37f46042efa82aa1e3cfb37d55b3d51374b2357eeece474515518a0a1ad2.jpg)  
Source: Bernstein Analysis

Generally, at current surface areas of GPUs, single-phase DTC has been expected to hit its thermal limit at GPU TDPs of between 2 - 2.5kW. Rubin GPUs start to push against this 2 - 2.5kW limit, and Rubin Ultra is expected to surpass it. After this point, the technological consensus has been that more aggressive forms of heat transfer (e.g., two-phase or direct to die) would be needed instead.

There is also the alternative of just reducing the temperature of the coolant flowing through the cold plate, but in the interest of managing energy consumption, this has not been preferred. Immersion cooling is also not considered a viable alternative since it involves submerging the server in coolant which is unweildy and much harder to maintain than current tray based approaches. So the two real options are either two-phase DTC or “direct to die” which are explained below.

EXHIBIT 2: Liquid cooling format by GPU TDP  
![](images/0a7cde6e0e570d6e5e11833ef041b6a4a7993162e54662b7505c3ca5b9b7ec7b.jpg)  
Source: Bernstein Analysis and Estimates

EXHIBIT 3: Multiple formats of liquid cooling delivery  
![](images/25a1c747c341062d8c9a38cfb55bd20a47bc57642906968a1e7cff50e97dd082.jpg)

Coolant evaporates (phase changes) when it absorbs heat from GPUs (extracting much more heat than single-phase)

Microfluidics channels etched directly into the silicon wafers

Source: Bernstein Analysis and Estimates

<table><tr><td colspan="2">Mechanics of heat transfer</td></tr><tr><td colspan="2">Q = m * c * ΔT + m * L</td></tr><tr><td>Sensible Heat(normal heating)</td><td>Latent Heat(Heat needed to change phase from liquid to vapor)</td></tr><tr><td>Q = Total heat energy absorbed by the liquid (measured in kilo-Joules)</td><td></td></tr><tr><td>m = Mass of the liquid (measured in kg)</td><td></td></tr><tr><td>C = Specific heat capacity (amount of heat required to raise temperature of 1kg of liquid by 1°C, measured in kilo-Joules/kg-0C)</td><td></td></tr><tr><td>ΔT = Temperature change (measured in °C)</td><td></td></tr><tr><td>L = Specific latent heat (amount of heat required to boil the liquid, measured in Joules/0C)</td><td></td></tr></table>

EXHIBIT 4: Sensible vs. latent heat; what's the difference?  
Illustration (consider water as an example)  
1 kg of water heats up by $1^{\circ}$ C

## TWO PHASE DTC

## Overview

As the name suggests, two-phase DTC cooling involves two phases of matter in the cooling process. In single-phase DTC, the TCS coolant (a water glycol mix) remains in a liquid state through the entire heat transfer process as it passes through the cold plate. However, in two-phase DTC, the coolant (another compound, not water-based) evaporates into a gaseous state in the cold plate before being cooled again into a liquid and repeating the cycle. The process of evaporation is able to capture a large amount of heat without a significant change in the underlying temperature of a refrigerant.

To understand how this works, we need to define a few scientific terms; sensible heat and latent heat. Sensible heat refers to the amount of heat needed to increase the temperature of a substance without a phase change. Latent heat refers to the amount of heat needed to cause a phase change (e.g., liquid to gas via evaporation) while maintaining the temperature of the matter undergoing a phase change.

$Q_{sensible heat} = m * c * \Delta T$ where m is the mass of the substance, c is it's specific heat (i.e., the amount of heat needed to increase temperature of 1 kilogram of material by $1^{0}C$ ), and $\Delta T$ is the change in temperature.

$Q_{latent heat} = m * L$ where m is still the mass of the substance while L is the specific “latent” heat (i.e., the amount of heat needed to cause a phase change of 1 kg of material). Notice how the temperature change doesn’t matter like with sensible heat; this is because when a phase change takes place, it happens at constant temperatures. If a coolant or refrigerant has a large enough latent heat, it can essentially capture a lot more thermal load while maintaining relatively constant temperatures vs. sensible heat transfer. This is the same principle applied in a refrigerant compression cycle, where refrigerant evaporates when it captures heat and condenses before cycling back into the system.

$$
Q = (1) \times (4. 1 8) \times (1) = 4. 1 8 \mathrm{kJ}
$$

Core principle of single-

phase DTC (coolant just

"heats" up) - amount of

heat taken out is 4.18 kJ

1 kg of water boils up (constant temperature process)

$$
\mathrm{Q} = (1) \times (2 2 6 0) = 2 2 6 0 \mathrm{kJ}
$$

Core principle of two-phase

DTC (coolant "boils") – amount

of heat taken out is 2260 kJ

Source: Bernstein Analysis and Estimates

EXHIBIT 5: Two-phase cooling mechanism (illustrative)  
![](images/d73523a0c71428fa5f86f654213f53cc360c151b17aae578fa48db791d98b331.jpg)  
Source: Bernstein Analysis; images generated using AI to showcase representative process

## Advantages of Two Phase DTC

The key advantage of two-phase DTC is the higher heat flux vs. single phase operations; you can just capture a lot more heat under the same conditions when the coolant can evaporate (often >3x). This allows you to develop GPUs with much higher TDPs while maintaining the same footprint. Since evaporation also maintains the coolant at the same temperature, you have an even, uniform thermal profile through the cold plate which helps manage hotspots better. Depending on the coolant used and the chip TDP, you can also use smaller pumps, less volume of coolant, and spend less energy pumping it through the system compared to similar thermal loads with single phase. Since these refirgerants / coolants are not likely to be water-based, they are also less likely to see corrosion or bacterial growth. It also enables the coolant to be dielectric (not electrically conducting), so in case of a liquid leak it does not fry the GPU. And by nature, two phase coolants evaporate when spilt, vs. pool on the tray.

## Disadvantages of Two Phase DTC

The biggest engineering problem to solve relates to flow in a two phase system. Most matter flows from regions of high pressure to regions of low pressure. With liquids this is simple, even in a complex microchannel array within a cold plate. However, when evaporation takes place, gas could create high pressure pockets, which push it in the opposite direction vs. where it should be flowing. This has still not been resolved at scale. Another disadvantage is complexity; a two-phase system has significantly more variables than a single phase CDU / cold plate setup. Refrigerants / coolants that meet required properties are often PFAS (forever chemicals) which are not ideal for deployment. So there is still research that needs to happen to develop and then produce these compounds at scale.

## Who's leading the pack on R&D?

It's hard to say because companies offer differing levels of visibility. From what we've publicly seen, Vertiv and Accelsius are the closest to having commercially ready products. Accelsius in fact advertises CDUs on their website. Zutcore focuses heavily on the topic but we've not seen specific products on their website (although they do have demos). We know CoolIT is also doing work in the space; they also presented on the topic at the OCP forum a couple of years ago. Boyd has a history of two-phase expertise, even if not for CDUs specifically while Schneider recently put out a blog post on the topic. JCI and Carrier have invested in Accelsius and Zutacore respectively. We've not seen announcements from nVent and Trane yet, although as NVIDIA reference design partners we believe they'll have the products when they need to.

## EXHIBIT 6: Two-phase R&D status by liquid cooling players

![](images/2a606d848c2a234cd162f0ed84253b5a7ad99e862c666b10d82ad2a96e35ef0d.jpg)

## Source: Bernstein Analysis, Company Reports

## EXHIBIT 7: Key challenges preventing two-phase commercialization

![](images/059ab2dfef1844ba80ca53dbc7fd7539aa3d9284eb3db987e8ac00cbf0d2e845.jpg)  
Source: Bernstein Analysis

## 1 Concurrent management of fluid and vapor is a fundamental challenge

\- Two-phase cooling requires dual-path channel array on the cold plates (larger diameter for low-density vapor and smaller diameters for liquid)

\- This leads to flow maldistribution – where some channels predominantly carry vapor and some liquid on the plate, which can lead to localized hotspots (which can then lead to non-uniform cooling)

## 2 High degree of control complexity

• Active management of multiple variables is required: refrigerator temperature, avoidance of vapor superheating, condensate cooling, and overall system pressure

\- Modern GPU workloads are non-steady: inference batching creates rapid power transients (0 ->100% in milliseconds) which requires constant monitoring

\- This requires finely calibrated sensors and control algorithms than single-phase; control software complexity can be a significant burden

## 3 Polyfluoroalkyl substances (PFAS) regulations

\- Industry currently relies on PFAS refrigerants, which face increasing regulatory scrutiny due to environmental considerations

\- This could create potential compliance, reporting, and long-term supply chain risks for data center operators

## 4 Technology remains in the early stages of commercialization

\- Two-phase DTC remains in early pilot phase currently, with Zutacore (\$100M Series C with Carrier as one investor) and Accelsius (\$65M Series B with JCI as one investor)

\- If GPU power envelopes (Feynman / Kyber) rise beyond $6\mathrm{kW}+$ (Blackwell Ultra is $1.4\mathrm{kW}$ ), then two-phase would become a necessity

## DIRECT-TO-DIE LIQUID COOLING Overview

Direct-to-die (D2D) is a new age evolution of traditional liquid cooling ecosystem where coolant is brought significantly closer to the heat-generation chip transistors. Instead of transferring heat through a thermal interface material (TIM) and thus a cold plate, microchannels are etched directly into the silicon wafer (on which the chip is housed). Coolant then flows through this channel array, and removes heat almost at the source.

D2D cooling thus also simplifies the thermal stack. As the cooling structure becomes physically integrated with the chip package, the need for traditional cold plates (as used currently) can be reduced or even fundamentally eliminated. As GPU thermal design power (TDP) continues to rise, the architecture offers a potential pathway to support future generations of TDP that may be difficult to manage using conventional cold plate based single and two-phase DTC alone.

EXHIBIT 8: Direct-to-die cooling | What it means and why it matters?  
![](images/297a9047bc28b4e024afe1ae1556bfe437c59073049fab33148e53c660060911.jpg)  
By embedding cooling features directly within the silicon die (which houses the GPU), thermal resistance is minimized; enabling higher heat removal (than traditional cold plate approaches)  
Source: Bernstein Analysis

## Advantages of Direct-to-Die

The primary advantage of direct-to-die cooling is the reduction in thermal resistance. By bringing the coolant within micrometer-scale distances of the active transistors, heat is removed before it spreads across the package, thereby enabling significantly higher heat removal compared to traditional cold plate designs. This makes the technology particularly attractive for next-generation GPU architectures where thermal design power (TDP) is increasing at a rapid pace.

Another major benefit is hotspot management - traditional liquid cooling can lead to localized (non-uniform) temperature peaks across the chip surface (due to non-uniform heating). D2D systems route coolant directly beneath high-power regions, allowing targeted heat removal and improving temperature uniformity across the GPU surface.

Additionally, the use of finely etched microchannels creates substantial surface area for heat transfer, improving cooling efficiency without increasing package footprint. The approach also eliminates thermal interface material (TIM) and its associated thermal resistance. From a facility perspective, direct-to-die cooling can enable higher coolant inlet temperatures (upto 45 °C) compared to traditional liquid cooling approaches. This may reduce chiller dependence, improve Power Usage Effectiveness (a measure of data center operational efficiency), and support more energy-efficient data center operations overall.

## Challenges of Direct-to-Die

The biggest challenge is manufacturing complexity. Creating a precise microchannel array within the silicon wafer requires advanced semiconductor fabrication techniques such as deep reactive ion etching (DRIE), adding process steps, yield considerations, and costs to the overall process. Unlike a conventional cold plate, the cooling structure becomes tightly integrated with the semiconductor package, increasing both design and manufacturing complexity right from the start.

Coolant quality requirements are also significantly more stringent. Since coolant flows extremely close to active silicon, contamination and particulate buildup could potentially damage the chip surface or compromise long-term reliability. This often requires semiconductor-grade loop cleanliness, tighter filtration standards, and more rigorous fluid management than conventional liquid cooling systems.

Another challenge relates to pressure management and mechanical reliability. Finely-etched microchannels generate higher flow resistance than larger cold plate structures, potentially increasing pumping requirements and leading to wardage. Integrity of package seals and long-term reliability become more critical because the cooling system is integrated directly within the package architecture.

## Who's leading the pack on R&D?

D2D is still in the very early stages of formulation, let alone commercialization. Among publicly disclosed efforts, Microsoft and Corintis have provided some of the strongest proofs of concept, demonstrated by bio-inspired (leaf vein architecture) etched into the backside of GPU dies. The prototype has yielded thermal capacity performance of $>1000 \, W/cm^{2}$ while utilizing deionized water and eliminating the need for a TIM. TSMC is the other major player who has announced developments in the space. Through its CoWoS ecosystem, the company has demonstrated a structure with microchannels etched directly into silicon surface.

At present, the industry appears to be treating D2D as a long-term scaling solution rather than an immediate replacement for conventional cold plate cooling. As GPU TDPs continue to climb, commercialization (and then adoption) is likely to accelerate, particularly in environments where thermal constraints become the primary bottleneck to future performance gains. Deployment today seems to be theoretical, with most solutions currently in prototyping, validation, or early-pilot stages.

EXHIBIT 9: Thermal advantages of direct-to-die are partially offset by manufacturing and operational complexity

<table><tr><td></td><td>Theme</td><td>Benefits</td><td>Practical challenges</td></tr><tr><td>1</td><td>Manufacturing complexity</td><td>Finely etched channels (50 – 200 μm) create far greater surface area for heat absorption</td><td>Deep-reactive ion etching (DRIE) fabrication process adds process steps and tool time – raising production costs</td></tr><tr><td>2</td><td>Coolant purity</td><td>Deionized water&#x27;s (could evolve to dielectric refrigerant in future) high conductivity and low viscosity maximizes heat removal per unit of flow</td><td>Requires semiconductor-grade loop cleanliness and sub-5 μm particulate filtration else silicon erodes</td></tr><tr><td>3</td><td>Thermal resistance</td><td>Eliminates TIM entirely; coolant reaches within ~200 μm of active transistors; cuts thermal resistance by ~25%+</td><td>Can lead to warping of setup during assembly; seals need to be able to withstand this level of pressure</td></tr><tr><td>4</td><td>Hotspot uniformity</td><td>Automatic routing of coolant to high-density hotspot zones (designs inspired by biology)</td><td>Flow maldistribution due to unnoticed manufacturing defects can create non-uniformity and leakage</td></tr><tr><td>5</td><td>Biogrowth elimination</td><td>Deionized water&#x27;s lack of nutrients prevents algae / bacteria colonization</td><td>The same deionized water is corrosive to metal manifolds; any leak near live silicon risks immediate galvanic corrosion</td></tr><tr><td>6</td><td>Higher inlet temperature</td><td>45 °C coolant inlet temperatures reduce chiller load and improve data center power effectiveness</td><td>Narrower thermal margin implies any flow disruption or workload spike has less headroom before breaching system limits</td></tr></table>

Source: Bernstein Analysis

EXHIBIT 10: Direct-to-die is slowly but steadily moving from a conceptual stage to manufacturable

<table><tr><td colspan="2">Company</td><td>Microsoft + ✱CORINTIS</td><td>tsmc</td></tr><tr><td rowspan="3">Details</td><td>Year</td><td>Sep 2025</td><td>May 2024 / 2025</td></tr><tr><td>Place</td><td>OCP Summit 2025</td><td>IEEE ECTC 2024 (base paper), ECTC 2025 (full design)</td></tr><tr><td>Description</td><td>Bio-inspired channel array (leaf veins / arterial topology) etched into the back of GPU die; routes more coolant through hotspots</td><td>Proprietary elliptical micropillar array architecture (CoWoS); MEMS-fabricated into back of GPU die</td></tr><tr><td rowspan="4">Technical performance</td><td>Heat flux</td><td>&gt;1000 W/cm2</td><td>&gt;250 W/cm2</td></tr><tr><td>Pressure drop</td><td>55% lower (vs. traditional microchannel arrays)</td><td>Undisclosed; but minimized via compartmentalized layout</td></tr><tr><td>Coolant</td><td>Standard de-ionized water(no new facility infrastructure needed)</td><td>40 °C de-ionized water(enables chiller-free facility operation)</td></tr><tr><td>TIM elimination</td><td>Full(no need of TIM)</td><td>Full(no need of TIM)</td></tr><tr><td rowspan="2">Testing &amp; future</td><td>Validation stage</td><td>Live MS Teams workload on a production server; passed</td><td>Full-scale vehicle with simulated AI workload heaters;NASA helium leak test passed</td></tr><tr><td>Commercialization timeline</td><td>Currently manufacture 100k units;plans to scale to 1M+ units by 2026/27</td><td>To begin production from 2027 onwards</td></tr></table>

Source: Bernstein Analysis

EXHIBIT 11: Rounding up | Is direct-to-die cooling better technology?

<table><tr><td></td><td>Claim</td><td>Evidence</td><td>Verdict</td></tr><tr><td>1</td><td>Can potentially replace cold plates as primary heat exchanger</td><td>Confirmed in tests (Microsoft / Corintis, TSMC)</td><td>Yes!</td></tr><tr><td>2</td><td>Eliminates Thermal Interface Material (TIM) resistance</td><td>Confirmed in tests (Microsoft / Corintis, TSMC); no TIM is needed</td><td>Yes!</td></tr><tr><td>3</td><td>Achieves higher thermal capacity than traditional liquid cooling</td><td>Confirmed in tests (Microsoft / Corintis, TSMC); upto 3x cooling than single-phase DTC</td><td>Yes!</td></tr><tr><td>4</td><td>Acceptance amongst large-scale hyperscaler deployments</td><td>Not yet (Corintis expects to produce 100k units; TSMC slated to commence production in 2027)</td><td>Maybe</td></tr><tr><td>5</td><td>Eliminates CDUs, manifolds, cooling loop components</td><td>Incorrect (the entire liquid cooling system remains as-is, except the cooling interface between the coolant and the GPU)</td><td>No!</td></tr></table>

Source: Bernstein Analysis

## SINGLE PHASE - IS THE THEORETICAL LIMIT REAL?

CoolIT has recently (early June 2026) published a white paper on a 15kW single-phase cold plate. Now to put that into context, consensus seems to believe that you'd need to switch over to two-phase DTC somewhere between Rubin and Rubin Ultra (whenever TDP's per GPU start to go beyond \~2.5kW). If you believe CoolIT's technology, however, we actually don't need to switch over for the good part of another decade (assuming chips TDP's continue to go up). From our research, the only proprietary piece of engineering here is CoolIT's "split flow" technology. This seems to be a design solution that allows coolant to reach hotter parts of the GPU more rapidly (translating to better thermal efficiency and lower resistance). The results were published on the basis of 1.2 lpm flow rates and "industryleading internal geometries, proven massmanufacturing techniques and standard thermal interface materials, in this case, thermal paste" as per the white paper so we do not think there's anything particularly differentiated beyond this technology. This is also based on $45^{0}\mathrm{C}$ inlet cooling temperatures (so in line with where NVIDIA expects operating conditions to be). If this is the case, we believe it reduces the existential risk of cold plates going away from direct-to-die. Most technology innovation on the power / cooling side in data centers happens because it needs to, not because it leads to marginal improvements (e.g., liquid cooling and 800V DC) so if cold plates can handle 15kW per GPU, we don't really see the need for continued innovation in both two-phase (so some private, two-phase players like Accelsius or Zutacore may customer interests decline) or direct to die (which is still largely at a conceptual stage). R&D dollars would be better spent elsewhere. The question we're struggling with is why other players are unable to match CoolIT's products. Is Split-Flow so unique (it is patented) that other names in liquid cooling are not able to replicate a similar version of it? CoolIT is clearly operating under standard operating conditions in their test ecosystem. We have heard the 15kW cold plate has a marginally larger surface area compared to the previously announced 4kW unit and that explains some of the improved performance but it certainly doesn't explain a 4x improvement so there's definitely more in there. We'd be curious to see how this materializes in terms of orders for CoolIT (and Ecolab if and when the deal goes through). The 15kW cold plate is still tested as a concept (so there isn't at scale manufacturing happening yet) and we'd be curious to understand how the economics and pricing of this unit compare to other cold plate manufacturers (which the market lacks visibility on). We're not saying two-phase or Direct-to-Die won't ever happen, but if this product proves to be commercially feasible to produce (we're comfortable with technical feasibility) it will likely push out other technologies because continuing with single phase cooling is the path of least resistance.

EXHIBIT 12: Overview of CoolIT 15kW cold plate (1/2)

## A potential breakthrough for single-phase DTC | CoolIT's 15kW cold plate

![](images/944836d548bd235a116dd153f0638ad91bc81a807128e03507526715d6281526.jpg)  
Showcased in early June 2026 at Computex, CoolIT announced development of a 15kW single-phase cold plate design (\~4x thermal capacity of existing cold plates)

Source: Bernstein Analysis, Company Reports

A proprietary “Split-Flow” microchannel architecture creates two counter-flowing coolant streams: improving temperature uniformity across the GPU die and increasing efficiency of heat transfer (from the GPU to the coolant)

Complementing this is a “variable fin pitch skived” cold plate design, featuring greater fin density over hotspot regions and lower flow resistance elsewhere

The platform supports coolant inlet temperatures as high as 45°C and has standard flow and thermal paste specs.

The result is a thermally optimized architecture that simultaneously increases cooling capacity and reduces pressure-drop penalties

Although currently validated on a thermal test vehicle, scaling deployment could materially increase the viable heat-flux of single-phase DTC, extending relevance for next-gen. GPU platforms through the 2030s

## EXHIBIT 13: Overview of CoolIT 15kW cold plate (2/2)

![](images/29d8cf70c5eaf2eba4529a739040c61b285ace4236477dfede507a1e1e2aa1e2.jpg)  
Source: Bernstein Analysis and Estimates, Company Reports

## Commentary

## 1 Demonstrated in a controlled laboratory environment

• Commercial-scale manufacturability and deployment economics to be validated

## 2 Enabled on a larger die footprint

\- Die used in the demo was larger than that of a conventional GPU, enabling a greater surface area for heat absorption

## 3 Performance achieved under industry-standard operational parameters

\- Standard coolant flow rates (\~1.2 L/min per kW)

• Standard coolant (PG25)

\- Split Flow architecture (coolant flow split into two paths when it enters the cold plate)

## 4 Greatly reduced the need for 2-phase DTC and direct-to-die for the next decade

\- By achieving 15kW thermal capacity within single-phase, the demo materially extends the feasibility of DTC liquid cooling for the next generation of Al infra

## IMPLICATIONS FOR CDU / COLD PLATE ECOSYSTEM MORE BROADLY?

We are of the opinion that both CDUs and cold plates will, in the longer-term, see product commoditization. Our point of view from our primers (cold plates, CDUs) was that cold plates are more exposed because they do not have the service attach that CDUs do to drive multi-year aftermarket revenues on the installed based. However, we do not think this commoditization will be immediate, because of technological shifts like single-phase to two-phase (which allows OEMs to add an innovation premium), ever-increasing operational requirements (higher power ratings, lower approach temperature differentials), and supply chain constraints (where demand still outstrips production capacity). We were also of the opinion that cold plates has obsolescence risk if technologies like direct-to-die become mainstream over the longer-term.

The existence of a 15kW cold plate changes that calculus. We do think the commoditization timeline could be pulled up since it removes the need for OEMs to build two-phase solutions for the foreseeable future. That then allows hyperscalers to increasingly spec out designs (both for CDUs and cold plates) because they now have a cooling roadmap that offers them material headroom on GPU TDPs. Supply shortages and rising performance requirements still offer a defense against commoditization, but defensibility does weaken in our perspective. The rate of commoditization also depends on (i) whether CoolIT is able to manufacture these products with the right unit economics at scale and (ii) how quickly competitors can meet CoolIT performance standards. On the more positive side, the development of a 15kW cold plate also reduces obsolescence risk, since DC operators aren't forced to move to direct-to-die (which adds significant compelxity).

On the whole, we are incrementally more negative on CDUs in the mid to long-term (no change to our expectations through 2028) and remain neutral on cold plates (accelerated commoditization risk is offset by lower obsolescence risk).

The authors would like to thank Sakansh Mittal for his help in preparing this report.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Vertiv Holdings Co

We value Vertiv at 32x NTM + 1 EBITDA of \$5.1B to reach our target price of \$416.

## nVent Electric PLC

We used a SOTP approach to value NVT. For the EC business, we used NTM + 1 EBITDA of \$417M and an EV/EBITDA multiple of 17x. For the SP business, we use an NTM + 1 EBITDA of \$1,074M and an EV/EBITDA multiple of 28x. Based on these assumptions, we arrive at a fair value per share of \$220.

## Trane Technologies PLC

We value Trane at 22x NTM + 1 EBITDA of \$5.7B to reach our target price of \$555.

## Carrier Global Corporation

We value Carrier using an 18x EV/EBIT ratio and an NTM + 1 EBIT estimate of \$3.9B to reach our target price of \$75.

## Johnson Controls International PLC

We value JCI using a 20x EV/EBITDA ratio and an NTM + 1 EBITDA estimate of \$5.8B to reach our target price of \$173.

## Eaton Corp PLC

We arrive at our \$534 price target by applying a 28x P/E multiple on our 2030 EPS estimate. Discounting this back, we arrive at our target price which implies a 33x P/E on our 2027 EPS. We believe this is appropriate given the long-term secular factors favoring the strength and long-term resilience of ETN's earnings algorithm.

## RISKS

## Vertiv Holdings Co

Downside: (i) Efficiency increasing to the point where less cooling needed, (ii) Unexpected slowing of data center expansion, (iii) Faster than expected shift away from NVIDIA chips to custom silicon (impacts Vertiv because of strong relationships), (iv) Tech. shift away from DTC / 800 VDC if Vertiv can't react fast enough

## nVent Electric PLC

Downside: (i) Faster than expected commoditization of CDUs / OCP makes them a commodity, (ii) Production line weakness for CDUs (given NVT is ramping), (iii) Longer than expected lead time to hire for key roles (e.g., open supply chain VP position)

## Trane Technologies PLC

Downside: (i) Price fixing lawsuit escalates for Trane, (ii) More players achieve similar level of product innovation in CDUs / broader liquid cooling, (iii) Residential / transport numbers deteriorate further than expected, (iv) Chiller headwinds (both sales and service) outweigh liquid cooling tailwind

## Carrier Global Corporation

Upside: (i) Resi / light commercial cycle turns in the US (we think this is easily the biggest driver for Carrier looking ahead), (ii) Continued growth in data centers (we'd be especially impressed if this came from CDUs) (iii) Policy changes in the UK / Germany driving heat pump uptake

Downside: (i) Escalation of price fixing lawsuit (Carrier uniquely exposed, (ii) Slowing of data center CapEx by hyperscalers, (iii) Supply of R-410A does not tighten as expected / drags out for longer

## Johnson Controls International PLC

Downside: Lean transformation does not successfully cascade through org., Data center weakness from chiller headwinds, Operating leverage <50% based on management guidance

## Eaton Corp PLC

Downside risks include: 1) lower than expected load growth impacting ETN's Electrical organic growth business, 2) interruptions to the ongoing global data center build, 3) slower than expected utility capex growth, 4) slower than expected reshoring trends, and 5) slower than expected growth/cancellations in mega projects.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

## DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.2%</td><td>15.3%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>35.8%</td><td>16.2%</td></tr><tr><td>Underperform</td><td>SELL</td><td>13.1%</td><td>13.6%</td></tr></table>

\* These figures represent the percentage of companies within each equity rating category for which affiliates of Bernstein have provided investment banking services within the previous 12 months.
As of June 30, 2026. All figures are updated quarterly.

## PRICE CHARTS / RATINGS AND PRICE TARGET HISTORY

Vertiv Holdings Co (VRT) Rating History for Bernstein as of 07/15/2026  
![](images/d58bee9025c25550bd893ca3b2d99ea0eec3937e8016bcb4b4c3e2ef354c5e21.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

nVent Electric PLC (NVT) Rating History for Bernstein as of 07/15/2026  
![](images/140069c66c749fbed1e316ce6f2b9c075e4f9d4c0cfcbf20a79723316bacf5bd.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Trane Technologies PLC (TT) Rating History for Bernstein as of 07/15/2026  
![](images/370d7bfda7e389b900cf6f8a639f0614764e8ab89506920736c4bd7992378089.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Carrier Global Corporation (CARR) Rating History for Bernstein as of 07/15/2026  
![](images/71b516c9656e57d039151719686f38f7a857378f9aa82cb9dcc3778dcf81b9ab.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Johnson Controls International PLC (JCI) Rating History for Bernstein as of 07/15/2026  
![](images/9187b86db6b39814becd11f016f0938a2c1d8c6a7e3e6de50fc668a215bfa7b3.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Eaton Corp PLC (ETN) Rating History for Bernstein as of 07/15/2026  
![](images/059f9166d76232a8a267d7a7228e93699cc149fd7e0872558cc2dd7a02ae8041.jpg)  
All price target and closing price data in the chart(s) above are denominated in the currency noted in the Ticker Table of this report.

## CONFLICTS OF INTEREST

Bernstein Autonomous LLP or BSG France SA, beneficially, has either a net long or short position of 0.5% or more of the total issued share capital of a class of common equity securities of the following MiFID eligible securities: Trane Technologies PLC, Carrier Global Corporation and Eaton Corp PLC.

SG and/or its affiliates beneficially own 0.5% or more of [the total issued share capital/any class of common equity securities] with a net [long/short] position of: Johnson Controls International PLC.

AB and/or its affiliates beneficially own 1% or more of a class of common equity securities of the following company: Eaton Corp PLC.

Bernstein and/or affiliates have received compensation for non-investment banking securities-related products or services in the previous twelve months from the following clients: Carrier Global Corporation.

Certain affiliates of Bernstein act as market maker or liquidity provider in the equities securities of: Vertiv Holdings Co, nVent Electric PLC, Trane Technologies PLC, Carrier Global Corporation, Johnson Controls International PLC and Eaton Corp PLC.

Certain affiliates of Bernstein act as market maker or liquidity provider in the debt securities of: Carrier Global Corporation and Eaton Corp PLC.

## OTHER MATTERS

The legal entity(ies) employing the analyst(s) listed in this report, and their location, can be determined by the country code of their phone number, as follows:

+1 Bernstein Institutional Services LLC; New York, New York, USA

+44 Bernstein Autonomous LLP; London UK

+212 SG Africa Technologies & Services; Casablanca, Morocco

+33 BSG France S.A.; Paris, France

+34 BSG France S.A.; Madrid, Spain

+41 Bernstein Autonomous LLP; Geneva, Switzerland

+49 BSG France S.A.; Frankfurt, Germany

+91 Bernstein (India) Private Limited; Mumbai, India

+852 Bernstein (Hong Kong) Limited 盛博香港有限公司; Hong Kong, China

+65 Bernstein (Singapore) Private Limited; Singapore

+81 Bernstein Japan KK; Tokyo, Japan

Where this report has been prepared by research analyst(s) employed by a non-US affiliate, such analyst(s), is/are (unless otherwise expressly noted below) not registered as associated persons of Bernstein Institutional Services LLC or any other SEC-registered broker-dealer and are not licensed or qualified as research analysts with FINRA. Accordingly, such analyst(s) may not be subject to FINRA's restrictions regarding (among other things) communications by research analysts with a subject company, interactions between research analysts and investment banking personnel, participation by research analysts in solicitation and marketing activities relating to investment banking transactions, public appearances by research analysts, and trading securities held by a research analyst account.

Where this report has been prepared by research analyst(s) employed by SG Africa Technologies & Services (part of the SG group of companies), it has been prepared on behalf of a Bernstein company under a Global Services Agreement in place between Bernstein and SG.

## CERTIFICATION

Each research analyst listed in this report, who is primarily responsible for the preparation of the content of this report, certifies that all of the views expressed in this publication accurately reflect that analyst's personal views about any and all of the subject securities or issuers and that no part of that analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views in this publication.

## II. ADDITIONAL GLOBAL CONFLICT DISCLOSURES

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e., the private side) within the Firm, and into other areas, units, groups or affiliates (i.e., public side) of the Firm.

## III. OTHER IMPORTANT INFORMATION AND DISCLOSURES

Separate branding is maintained for “Bernstein” and “Autonomous” research products.

\- Bernstein produces a number of different types of research products including, among others, fundamental analysis and quantitative analysis under both the “Autonomous” and “Bernstein” brands. Recommendations contained within one type of research product may differ from recommendations contained within other types of research products, whether as a result of differing time horizons, methodologies or otherwise. Furthermore, views or recommendations within a research product issued under one brand may differ from views or recommendations under the same type of research product issued under the other brand. The Research Ratings System for the two brands and other information related to those Rating Systems are included in the previous section.

\- Autonomous operates as a separate business unit within the following entities: Bernstein Institutional Services LLC, Bernstein Autonomous LLP, Bernstein (Hong Kong) Limited 盛博香港有限公司 and Bernstein (India) Private Limited. For information relating to “Autonomous” branded products (including certain Sales materials) please visit: www.autonomous.com. For information relating to Bernstein branded products please visit: www.bernsteinresearch.com.

Analysts are compensated based on aggregate contributions to the research franchise as measured by account penetration, productivity and proactivity of investment ideas. No analysts are compensated based on performance in, or contributions to, generating investment banking revenues.

This report has been produced by an independent analyst as defined in Article 3 (1)(34)(i) of EU 596/2014 Market Abuse Regulation (“MAR”) and the same article of MAR as it forms part of United Kingdom domestic law by virtue of the European Union (Withdrawal) Act 2018.

To our readers in the United States: Bernstein Institutional Services LLC, a broker-dealer registered with the U.S. Securities and Exchange Commission (“SEC”) and a member of the U.S. Financial Industry Regulatory Authority, Inc. (“FINRA”) is distributing this publication in the United States and accepts responsibility for its contents. Where this material contains an analysis of debt product(s), such material is intended only for institutional investors and is not subject to the US independence and disclosure standards applicable to debt research prepared for retail investors.

Bernstein Institutional Services LLC may act as principal for its own account or as agent for another person (including an affiliate) in sales or purchases of any security which is a subject of this report. This report does not purport to meet the objectives or needs of any specific individuals, entities or accounts.

To our readers in Canada: If this publication pertains to a Canadian domiciled company, it is being distributed in Canada by Bernstein (Canada) Limited, which is licensed and regulated by the Canadian Investment Regulatory Organization. If the publication pertains to a non-Canadian domiciled company, it is being distributed by Bernstein Institutional Services LLC, which is licensed and regulated by both the SEC and FINRA, into Canada under the International Dealers Exemption.

This document may not be passed onto any person in Canada unless that person qualifies as "permitted client" as defined in Section 1.1 of NI 31-103.

To our readers in Brazil: This report has been prepared by Bernstein Institutional Services LLC, and Banco BTG Pactual S.A. ("BTG") is responsible for the distribution of this report in Brazil.

To readers in the United Kingdom: This publication has been issued or approved for issue in the United Kingdom by Bernstein Autonomous LLP, authorised and regulated by the Financial Conduct Authority and located at 60 London Wall, London EC2M 5SH, +44 (0)20-7170-5000. Registered in England & Wales No OC343985.

This document is for distribution only to persons who (i) have professional experience in matters relating to investments falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the “Financial Promotion Order”), (ii) are persons falling within Article 49(2)(a) to (d) (“high net worth companies, unincorporated associations, etc.”) of the Financial Promotion Order, (iii) are outside the United Kingdom, or (iv) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the FSMA) in connection with the issue or sale of any securities may otherwise lawfully be communicated or caused to be communicated (all such persons together being referred to as “relevant persons”). This document is directed only at relevant persons and must not be acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this document relates is available only to relevant persons and will be engaged in only with relevant persons.

To our readers in the member states of the EEA: This publication is being distributed by BSG France SA, which is authorised and regulated by the Autorité de Contrôle Prudentiel et de Résolution (ACPR) and Autorité des Marchés Financiers (AMF).

To our readers in Hong Kong: This publication is being distributed in Hong Kong by Bernstein (Hong Kong) Limited 盛博香港有限公司, which is licensed and regulated by the Hong Kong Securities and Futures Commission (Central Entity No. AXC846) to carry out Type 4 (Advising on Securities) regulated activities and subject to the licensing conditions mentioned in the SFC Public Register (https://www.sfc.hk/publicregWeb/corp/AXC846/details)). This publication is solely for professional investors, as defined in the Securities and Futures Ordinance (Cap. 571). The purpose of this report is solely to provide an analysis of the issuers referred to in this report and is not intended for any purpose contrary to the laws of Hong Kong.

To our readers in Singapore: This publication is being distributed in Singapore by Bernstein (Singapore) Private Limited, only to accredited investors or institutional investors, as defined in the Securities and Futures Act 2001 of Singapore ("SFA"). Recipients in Singapore should contact Bernstein (Singapore) Private Limited in respect of matters arising from, or in connection with, this publication. Bernstein (Singapore) Private Limited is regulated by the Monetary Authority of Singapore and licensed under the SFA as a capital markets services licence holder for dealing in capital markets products that are securities and collective investment schemes and an exempt financial adviser for advising on, issuing and promulgating analyses and reports on securities. Bernstein (Singapore) Private Limited is registered in Singapore with Company Registration No. 20213710W and located at 8 Marina Boulevard, #12-01, Marina Bay Financial Centre, Singapore 018981, +65-6326-7000.

To our readers in the People's Republic of China: The securities referred to in this document are not being offered or sold and may not be offered or sold, directly or indirectly, in the People's Republic of China (for such purposes, not including the Hong Kong and Macau Special Administrative Regions or Taiwan, the "PRC") in contravention of any applicable laws of the PRC.

This document does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC to any person to whom it is unlawful to make the offer or solicitation in the PRC.

We do not represent that this document may be lawfully distributed, or that any securities may be lawfully offered, in compliance with any applicable registration or other requirements in the PRC, or pursuant to an exemption available thereunder, or assume any responsibility for facilitating any such distribution or offering. In particular, no action has been taken by us which would permit a public offering of any securities or distribution of this document in the PRC. Accordingly, the securities are not being offered or sold within the PRC by means of this document or any other document. Neither this document nor any advertisement or other offering material may be distributed or published in the PRC, except under circumstances that will result in compliance with any applicable laws and regulations.

To our readers in Japan: This publication is being distributed in Japan by Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社), which is registered in Japan as a Financial Instruments Business Operator with the Kanto Local Finance Bureau (registration number: The Director-General of Kanto Local Finance Bureau (FIBO) No.3387) and regulated by the Financial Services Agency. It is also a member of Investment Management Association of Japan. This publication is solely for qualified institutional investors in Japan only, as defined in Article 2, paragraph (3), items (i) of the Financial Instruments and Exchange Act.

For the institutional client readers in Japan who have been granted access to the Bernstein website by Daiwa Group Inc. ("Daiwa"), your access to this document should not be construed as meaning that Bernstein is providing you with investment advice for any purposes. Whilst Bernstein has prepared this document, your relationship is, and will remain with, Daiwa, and Bernstein has neither any contractual relationship with you nor any obligations towards you.

To our readers in Australia: Bernstein (Hong Kong) Limited 盛博香港有限公司 is responsible for distributing research in Australia. It is regulated by the Securities and Exchange Commission under U.S. laws, by the Financial Conduct Authority under U.K. laws, which differs from Australian laws. Bernstein (Hong Kong) Limited 盛博香港有限公司 is exempt from the requirement to hold an Australian financial services license under the Corporations Act 2001 in respect of the provision of the following financial services to wholesale clients:

• providing financial product advice;

• dealing in a financial product;

\- making a market for a financial product; and

• providing a custodial or depository service.

To our readers in India: This publication is being distributed in India by Bernstein (India) Private Limited (SCB India) which is licensed and regulated by Securities and Exchange Board of India ("SEBI") as a research analyst entity under the SEBI (Research Analyst) Regulations, 2014, having registration no. INH000006378 and as a stock broker having registration no. INZ000213537. SCB India is currently engaged in the business of providing research and stock broking services. Please refer to www.bernsteinresearch.in for more information.

\- SCB India is a Private limited company incorporated under the Companies Act, 2013, on April 12, 2017 bearing corporate identification number U65999MH2017FTC293762, and registered office at Level 3A, 4th Floor, First International Financial Centre, Plot Nos C-54 and C-55, G Block, Near CBI Office, Bandra Kurla Complex, Bandra (East), Mumbai 400098, Maharashtra, India (Phone No: +91-22-68421401).

\- For details of Associates (i.e., affiliates/group companies) of SCB India, kindly email MUM-BERNSTEIN-InCompliance@bernsteinsg.com.

• SCB India does not have any disciplinary history as on the date of this report.

\- Except as noted above, SCB India and/or its Associates (i.e., affiliates/group companies), the Research Analysts authoring this report, and their relatives

• do not have any financial interest in the subject company

• do not have actual/beneficial ownership of one percent or more in securities of the subject company;

\- is not engaged in any investment banking activities for Indian companies, as such;

• have not managed or co-managed a public offering in the past twelve months for any Indian companies;

\- have not received any compensation for investment banking services or merchant banking services from the subject company in the past 12 months;

• have not received compensation for brokerage services from the subject company in the past twelve months;

\- have not received any compensation or other benefits from the subject company or third party related to the specific recommendations or views in this report; and

\- do not currently, but may in the future, act as a market maker in the financial instruments of the companies covered in the report.

\- do not have any conflict of interest in the subject company as of the date of this report.

\- Except as noted above, the subject company has not been a client of SCB India during twelve months preceding the date of distribution of this research report. Neither SCB India nor its Associates (i.e., affiliates/group companies) have received compensation for products or services other than investment banking, merchant banking or brokerage services from the subject company in the past twelve months.

\- The principal research analyst(s) who prepared this report, members of the analysts' team, and members of their households are not an officer, director, employee or advisory board member of the companies covered in the report.

\- Our Compliance officer / Grievance officer is Ms. Rupal Talati, who can be reached at +91-22-68421451, or MUM-BERNSTEIN-InCompliance@bernsteinsg.com / Scbin-investorgrievance@bernsteinsg.com

\- The Research investor charter and Terms & Conditions of SCB India are available on its website and may be accessed at Bernstein (India) Private Limited (https://bernsteinresearch.in/) for your reference.

\- Disclaimer: Registration granted by SEBI, and certification from NISM, is in no way a guarantee of performance of the intermediary or provide any assurance of returns to investors. Investments in securities market are subject to market risks. Read all the related documents carefully before investing.

To our readers in Switzerland: This document is provided in Switzerland by or through Bernstein Autonomous LLP, and is provided only to qualified investors as defined in article 10 of the Swiss Collective Investment Scheme Act (“CISA”) and related provisions of the Collective Investment Scheme Ordinance and in strict compliance with applicable Swiss law and regulations. The products mentioned in this document may not be suitable for all types of investors. This document is based on the Directives on the Independence of Financial Research issued by the Swiss Bankers Association (SBA) in January 2008.

To our readers in the Middle East: Bernstein Autonomous LLP, DIFC branch has its principal office at Gate Village 06, DIFC, Dubai, UAE. Bernstein Autonomous LLP, DIFC branch is regulated by the Dubai Financial Services Authority (DFSA) with the registration number CL10040 and is provisioned for Arranging Deals in Investments and Advising on Financial Products. All communications and services are directed at Professional Clients and Market Counterparties only (as defined in the DFSA rulebook). Persons other than Professional Clients and Market Counterparties, such as Retail Clients, are not the intended recipients of our communications or services.

## LEGAL

All research publications are disseminated to our clients through posting on the firm's password protected websites, bernsteinresearch.com and autonomous.com. Certain, but not all, research publications are also made available to clients through third-party vendors or redistributed to clients through alternate electronic means as a convenience.

This publication has been published and distributed in accordance with the Firm's policy for management of conflicts of interest in investment research, a copy of which is available from Bernstein Institutional Services LLC, Director of Compliance, 245 Park Avenue, New York, NY 10167. Additional disclosures and information regarding Bernstein's business are available on our website www.bernsteinresearch.com.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. This publication is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of, or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or which would subject any of the entities referenced herein or any of their subsidiaries or affiliates to any registration or licensing requirement within such jurisdiction. This publication is based upon public sources we believe to be reliable, but no representation is made by us that the publication is accurate or complete. We do not undertake to advise you of any change in the reported information or in the opinions herein. This publication was prepared and issued by entity referred to herein for distribution to eligible counterparties or professional clients. This publication is not an offer to buy or sell any security, and it does not constitute investment, legal or tax advice. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with their professional advisors in light of their specific circumstances. The value of investments may fluctuate, and investments that are denominated in foreign currencies may fluctuate in value as a result of exposure to exchange rate movements. Information about past performance of an investment is not necessarily a guide to, indicator of, or assurance of, future performance.

This report is directed to and intended only for our clients who are “eligible counterparties”, “professional clients”, “institutional investors” and/or “professional investors” as defined by the aforementioned regulators, and must not be redistributed to retail clients as defined by the aforementioned regulators. Retail clients who receive this report should note that the services of the entities noted herein are not available to them and should not rely on the material herein to make an investment decision. The result of such act will not hold the entities noted herein liable for any loss thus incurred as the entities noted herein are not registered/authorised/licensed to deal with retail clients and will not enter into any contractual agreement/arrangement with retail clients. This report is provided subject to the terms and conditions of any agreement that the clients may have entered into with the entities noted herein. All research reports are disseminated on a simultaneous basis to eligible clients through electronic publication to our client portal.

The information in this report was prepared by Bernstein solely for the internal business use of our clients. Clients may store, display, analyze, reformat and print the information in this report for this limited use only. Clients may not copy, alter, create derivative works, resell, reverse engineer, commercially exploit, share or distribute any part of the information contained herein for any purpose without Bernstein's express written consent. These restrictions include extracting data or using the content to develop indices or other products. Further, you may not use this report, or any portion of this report, to train or finetune any third-party machine learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.