## Rating Buy
## Special Report
# Data Centers in Space Part 4

Following up on our initiation last week, we take a closer look at orbital data centers and continue our Data Centers in Space series, introducing a refreshed cost model (Excel available upon request) and further analysis around optical/lasers, spectrum, solar, radiator, and compute density. We factor in the latest disclosures from SpaceX regarding its AI1 satellite and Starmind constellation. Our high-level conclusion is the physics checks out and the biggest challenge will be cost/scale, which we think SpaceX can achieve through extreme vertical integration. Combined with Starship launches scaling up, we envision a scenario in the early 2030s where cost can be on par with terrestrial.

Figure 1: SpaceX AI1 satellite design

[[KC_IMAGE_001]]

Source : Company website

## Valuation & Risks


## Optical lasers & spectrum

## Starmind

The AI1 satellites will rely on optical inter-satellite links (OISLs) to route traffic within the Starmind constellation and then into the Starlink constellation, whose laser mesh network then backhauls traffic to ground stations. As such, AI1 satellites do not require a complex multi-panel phased-array antenna onboard (i.e., no meaningful spectrum needed for communication except for possibly some Ka-band as a backup for telemetry). We estimate there are >10,000 Starlink satellites in orbit now with V2 minis each having 3 optical terminals capable of handling \~600 Gbps of capacity (200 Gbps per terminal). For the upcoming V3 satellites, we suspect there may be at least 2-3 Tbps of capacity per satellite. With the quantity of data increasing, we also anticipate SpaceX augmenting and/or upgrading its ground station network.

Figure 2: Starlink mini laser terminal

[[KC_IMAGE_002]]

Source : Company reports

Leading providers of optical terminals are Tesat-Spacecom (subsidiary of Airbus), Mynaric (acquired earlier this year), SA Photonics (acquired by CACI in 2021) and SpaceX (uses internally but also started selling “mini” laser terminals externally - Muon Space and Starcloud have announced plans to use).

## Starlink

Using such an architecture, this means the space-to-ground layer will bear the burden of a lot more traffic. Optical links make the Starmind constellation itself spectrum-free, but data that leaves the laser mesh network must ultimately funnel through Starlink's gateways, and orbital data centers change the shape of that data flow. Starlink's Gen1/Gen2 gateway authorizations were sized for a consumer broadband business whose traffic is asymmetrical (downlink heavy). As such, SpaceX is increasingly utilizing more unconventional spectrum bands beyond Ku-/Ka- such as:

E-band: already using for gateway backhaul; uplink+downlink

■ V-band: authorized for advanced user terminals and gateway; uplink +downlink

■ W-band: authorized for gateway backhaul; primarily uplink

D-band: proposed for gateway backhaul mainly for Al; primarily uplink

Higher bands historically face severe rain fade, oxygen absorption, and atmospheric attenuation that make them unreliable for consumer user terminals so it appears Starlink is mostly using them for high-capacity gateway backhaul links (where large dishes, site diversity, and optical inter-satellite routing can mitigate these issues), prioritizing proven Ku-/Ka- for consumer antennas while gradually adding V- for advanced users as hardware and regulations mature.

Separately, the FCC recently adopted new standards for satellites, replacing the 1990s-era Equivalent Power Flux Density (EPFD) limits that forced LEO systems like Starlink to severely restrict power and beam density to protect GEO satellites. Instead, the new rules use performance-based protection criteria that account for today's adaptive coding/modulation, beamforming, and real-world coordination. In the key Ku-/Ka- bands (10.7–12.7 GHz, 17.3–18.6 GHz, 19.7–20.2 GHz), this allows operators to run at higher power and many more co-frequency satellites/ beams serving the same area (e.g., 7–8 instead of effectively 1). The FCC cited up to 7× more capacity from the same number of satellites.

## Solar power

## Current solutions

Satellites mainly use multi-junction or silicon solar cells. Multi-junction delivers higher performance (\~30% or higher efficiency) by stacking different materials such as gallium arsenide (GaAs) and germanium (Ge) which enable broader spectrum capture of sunlight; these materials also provide greater radiation resistance. However, the production of these two materials is highly concentrated in China especially gallium which can be produced as a byproduct aluminum refining and similarly for germanium, as a byproduct of zinc smelting. Spectrolab (subsidiary of Boeing), AZUR Space (based in Germany; acquired by 5N Plus in 2021), and SolAero (acquired in 2022) are leading providers of multi-junction space grade cells. Silicon is materially cheaper (up to 80%) benefitting from much larger industrial scale but performs worse (usually 15-20% efficiency), and is not as durable due to lower radiation resistance. Within silicon, the main type of cell is referred to as a passivated emitter and rear cell (PERC). Taiwan Solar Energy Corp (TSEC) is a supplier of this type of cell to SpaceX. Amazon LEO also uses PERC but it is unclear who the supplier is.

## What's coming next?

In the next few years, we think a new type of approach can emerge for satellites: heterojunction (HJT). This type of cell combines crystalline silicon with thin layers of amorphous silicon to improve performance. Interestingly, HJT uses a simpler (5-7 steps vs. typical 12-13), lower-temperature production process that could save up to 70% on energy usage although upfront equipment costs will be higher; there is also potential to remove silver from the coating and use copper instead, saving cost. Performance wise, efficiency has been recorded to be as high as 27% and the symmetrical design allows the cell to absorb almost equal light from both sides. Lastly, HJT is very radiation hardened and degrades slowly in orbit. In the US, Solestial (recently acquired by York Space Systems) is working on development of ultrathin, flexible silicon HJT solar cells, leveraging equipment from Meyer Burger.

Beyond HJT, the use of perovskite tandem cells may be the future. Perovskite is a synthetic crystal structure that essentially can be printed or sprayed onto a surface, meaning it is very lightweight and theoretically as efficient as multi-junction. Solar cells today are all rigid but with perovskite, the ability to utilize thin-film or flexible panels becomes possible. Rigid (whether multi-junction or silicon) means the cells are mounted onto a honeycomb-like substrate made of aluminum or carbon fiber composite. These panels then are stacked and use mechanical hinges and springs to unfold once in orbit.

In China, Drinda (2865.HK) showcased a dedicated “space PV” zone at SNEC in May, highlighting its efforts to develop perovskite-based solar solutions for space applications. The company displayed its perovskite/TOPCon tandem technology (with \~33.5% small-area efficiency), alongside flexible CPI-based substrates and a commercial satellite model. The company has been an early mover in the space-based solar business. Xuntian, a subsidiary of the company, plans to manufacture and deploy 12-15 satellites in 2026 (with an order backlog of 54 satellites). GCL’s (3800.HK) booth design and product display at SNEC reflected a clear shift in focus beyond traditional PV, with both battery materials (cathode and anode) and space solar prominently positioned at the front of its exhibition area. For space solar, the company showcased a flexible perovskite solar cell sample alongside satellite-related use cases.

## SpaceX roadmap

SpaceX is currently building a solar cell manufacturing facility in Bastrop, Texas near Austin, as part of a much larger ambition for domestic solar cell production. Bastrop is targeting 10 GW in solar cell capacity with two floors (5 GW each). The facility is permitted for \~1.1m square feet, with potential expansion to 1.6 million, and is co-located with SpaceX's existing Starlink production site. Construction on the solar factory began in late March 2026, with equipment installation having already begun. The plant aims for production ramp-up and "reasonable volume" by the end of 2027. Our understanding is that the plant will initially produce silicon solar cells, delivering around 19% efficiency.

Figure 3: SpaceX ODC satellite production site

[[KC_IMAGE_003]]

Source : Company website

Looking ahead, SpaceX may switch to HJT or perovskite cells but we suspect this will not occur in the near-term option as they likely can not secure the appropriate equipment in time for the AI1 satellite deployment. Ultimately, Elon Musk has indicated plans to put up 100 GW of domestic solar cell capacity within three years.

## Radiator

## Thermal management

Satellites operate in the vacuum of space, meaning there's no air or medium for heat to dissipate via conduction or convection like on Earth. Instead, satellites rely on thermal radiation to reject excess heat generated by onboard electronics and other components. Radiators function by emitting electromagnetic energy, primarily in the infrared spectrum, which carries away heat as photons. The process follows the Stefan-Boltzmann law, where the rate of heat radiation is dependent on temperature and surface area.

## Passive or active?

There are generally two types of radiators: passive and active. Passive radiators reject heat using nothing but material properties and geometry. This exploits the intrinsic thermal properties of materials, surfaces, and geometric configurations to manage heat flow without consuming any electrical power. The main drawback is that the radiator area is limited by the spacecraft's form factor, which caps passive heat rejection capacity. Active radiators are part of a powered thermal loop — pumps circulate fluid from cold plates on the electronics to the radiator panel. This costs power and adds failure modes, but handles much higher heat loads and holds tighter temperature control than passive designs. Nearly all satellites use passive radiator(s). Active radiators are essentially only used on space stations (ISS, Tiangong) and capsules (Dragon, Starliner).

Historically, primes built most of their own radiator panels in-house. Merchant suppliers include Advanced Cooling Technologies (ACT), Paragon Space Development, Redwire, Beyond Gravity, Iberespacio, and Admatis.

## SpaceX roadmap

SpaceX produces the radiator on current Starlink satellites in-house (passive) and will continue to do so for Al1 satellite (active). Al1 will use a double-sided active deployable liquid radiator capable of dissipating $1,400 \, W/m^{2}$ ( $700 \, W/m^{2}$ per face) covering a $110 \, m^{2}$ surface area. This type of radiator requires electrical power and/or moving parts to transport heat from the compute module to the radiator panels. This is necessary given the high power 120–150 kW payload, where heat fluxes are too high for purely passive conduction. Active radiators have typically been very low volume components so SpaceX will be the first to mass produce such a design.

## Compute density

SpaceX is targeting prototype deployments of its AI1 satellites late next year. FCC-filings outline a constellation of up to one million satellites in LEO. Because each satellite has a fixed power and heat budget, the imperative is to maximize computational density. SpaceX is targeting density of 100 kW per ton but AI1 will not meet this threshold, starting off at \~70 kW, implying about 6 MW of compute per Starship launch initially (assumed 85 ton payload capacity). SpaceX expressed openness to hosting all types of chip payloads for its AI1 satellites including Nvidia GPUs, Google TPUs, Amazon Trainium, and of course Tesla's AI chips which prioritize energy efficiency. AI1 is expected to run sustainably at about 120 kW, roughly in line with the power consumption of a NVIDIA GB300 NVL72 rack. In our model, we assume compute density improves to closer to 85-90 kW in 2032E and then 100 kW with the AI3 satellite beyond that.

## Economics can eventually be compelling

To set a baseline, we assume upfront capex for 1 GW of AI compute on the ground is \$38bn and requires \$900m in annual opex (power, maintenance, labor, etc...), translating into \$42.5bn over 5 years (based on Epoch AI analysis). Of this amount, compute represents \$21bn and we assume this carries over to orbital data centers at a 10% mark-up to account for overprovisioning in case of GPU failures. Our sense is GPU failures will not be addressed directly by maintenance but simply each satellite will just operate at lower power in the event of a failure. Therefore, the non-compute costs for terrestrial are \$21.5bn and ODC essentially has to break below this level post overprovisioning or \$19.5bn to be at parity. Looking forward, we assume the cost of terrestrial increases going forward. To illustrate, NVIDIA's CEO Jensen Huang recently commented at GTC Taipei 2026 that a new 1 GW "AI factory" could approach \$100bn in cost with roughly half being compute-related.

Using current SpaceX launch vehicles and satellite designs, we estimate the near-term cost of deploying a 1 GW space data center constellation would be 6x higher than terrestrial (ex-compute). This gap can narrow to 1.0-1.5x later by end of the decade and then eventually be cheaper in the early-mid 2030s. This reduction is primarily driven by Starship (rapid reusability) and aggressive optimization/scaling of the AI-series satellites. We also refresh the DB Orbital Data Center Model which goes deeper into the economic viability of launching AI infrastructure into orbit (Excel available upon request).

Figure 4: Terrestrial vs. orbital data center deployment cost


Source : Company reports, DB

Figure 5: Starship launch cost trajectory assumptions


Source : Company reports, DB

Figure 6: Orbital data center satellite cost trajectory assumptions


# Appendix 1
