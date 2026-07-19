# Asia Communication Infrastructure
## 800VDC Architecture for Next-Generation AI Data Centers
## CITI'S TAKE

In this Super-Sector report, we outline likely implications of the 800VDC transition and potential Asia beneficiaries in the grey space and IT rack power/cooling in AI datacenters. As GPU rack power density approaches 1MW, we forecast 800VDC to reach 79% of new global DC capacity by 2030E, with SST demand surging from 901 MVA in 2027E to 37,152 MVA in 2030E to replace traditional LV transformers. 800VDC architecture is driving combined BESS and BBU battery demand at an 80%+ CAGR through 2030E. We see this as a multi-layer investment opportunity across six segments: DC operators riding AI demand tailwind; power equipment names riding SST architecture upcycle; BESS and BBU suppliers benefiting from rising battery demand; IT rack power/cooling vendors (incl. BBU, MLCC) benefiting from surging power density and cooling requirement; liquid cooling providers capturing structural thermal upgrades; and power semiconductor suppliers underpinning the entire conversion chain.

Traditional AC Chain Gives Way to SST — GPU rack power density has grown nearly 100x since 2020, rendering conventional AC distribution physically unviable. We project 800VDC adoption to reach 79% of new global data center capacity by 2030E, displacing legacy power architecture while creating new equipment categories including SST, BESS, BBU, and new cooling solutions.

Data Center Operators — We expect the near-term AI demand tailwind to be intact. We like China DC market leaders GDS and VENT. In Australia, we think NextDC and CDC/Infratil are positioned to incorporate 800VDC into future builds.

Power Equipment — We see Delta as uniquely positioned with end-to-end grid-to-chip portfolio. Hyosung, Sieyuan and TGOOD should benefit from LV transformer and SST for domestic buildout and export opportunities. Hongfa should ride rising relay products for 800VDC migration. Hitachi Energy India, GE Vernova T&D India, CG Power and Industrial should benefit from India domestic demand and exports.

BESS — 800VDC battery demand could accelerate at an 80%+ CAGR in 2027-30E; Sungrow (SST launch July 2026), BYD, CATL and EVE Energy are key beneficiaries.

IT Rack Power & Cooling — We forecast BBU content value per rack to rise from US\$4-5K in 2022 to US\$33-34K by 2029E, with Panasonic, Dynapack and AES the direct plays. We see Murata, SEMCO and Yageo as key MLCC beneficiaries. We also believe Taiwan and Chinese rack cooling players may benefit from IT cabinets and liquid cooling upgrade.

Cooling Solutions— Higher rack power densities make liquid cooling a structural necessity. LG Electronics, Daikin and Envicool are key names to watch.

Power Semiconductors — VIS leads at high-voltage front end; UMC leveraged to PMIC/BCD specialty nodes; Renesas could benefit via Transphorm GaN acquisition. For China, SG Micro, CR Micro and Silan Micro could benefit from SiC/GaN demand.


[[KC_IMAGE_001]]


Air Ma $^{AC}$

Angela Hsu $^{AC}$

Anusha Madireddy $^{AC}$

Desmond Law $^{AC}$

Eric Lau $^{AC}$

Graeme McDonald $^{AC}$

Howard Penny $^{AC}$


Jamie Wang $^{AC}$

Jeff Chung $^{AC}$

Karen Huang $^{AC}$

Kevin Chen $^{AC}$

Laura (Chia Yi) Chen $^{AC}$

Masahiro Shibano $^{AC}$

Michael Hung $^{AC}$


Peter Lee $^{AC}$


Takayuki Naito $^{AC}$

Takero Fujiwara $^{AC}$

## Contents

800VDC Architecture for Next-Generation AI Data Centers 3
Nvidia's 800VDC Architecture: Four Generations, from Multi-Stage AC to a Single Integrated DC Conversion 4
Traditional AC Chain Has Four Lossy Conversion Stages — All of Which Collapse into One under 800VDC 7
Key Equipment Demand Projection in 800VDC Transition 9
Key Beneficiaries across Infrastructure Stack within a Data Center 12
Deep Dive into Key Asia Beneficiaries in 800VDC Transition 14
Data Center Operators 14
Power Equipment 15
Battery Energy Storage System 19
IT Rack Power and Cooling 21
Cooling Solutions 27
Power Semiconductors 28
Glossary 31
Appendix A-1 33

## 800VDC Architecture for Next-Generation AI Data Centers

In this report, we outline likely implications of the 800V DC transition in AI infrastructure and potential beneficiaries in Asia.

The rapid proliferation of AI workloads is fundamentally reshaping the power infrastructure of modern data centers. GPU rack power density has grown nearly 100-fold compared to traditional web servers — from 10kW per rack in 2020, to 120kW with Blackwell, and should exceed 1MW with the forthcoming Rubin Ultra and Kyber platforms by 2028. This near-exponential trajectory does not merely cause an incremental engineering challenge; it represents a structural inflection point that renders conventional power distribution architectures physically and economically unviable.

In response, the industry is converging on 800VDC as the optimal power distribution standard for next-generation AI infrastructure. By delivering power at higher voltage, 800VDC dramatically reduces current levels, copper requirements, and conversion losses across the entire power chain from the utility grid to the compute chip.

Figure 1. 800VDC Architecture Key Potential Asia Beneficiaries (data as at 16-Jul-2026)


Source: dataCentral, Citi

# Nvidia's 800VDC Architecture: Four Generations, from Multi-Stage AC to a Single Integrated DC Conversion

NVIDIA's reference architecture defines 4 generations of data center power distribution, each representing a step-change reduction in conversion stages (Figure 1). Today's incumbent 415VAC architecture routes power through five or more sequential stages (transformer, LV switchboard, AC UPS, PDU, and in-rack PSU) before reaching the compute chip at 54VDC. The first transition step, 800VDC White Space Retrofit, inserts an LV Rectifier and a dedicated HVDC Power Sidecar rack into existing facilities, converting AC to 800VDC at the row level without disturbing grey-space infrastructure. The subsequent Hybrid Power Distribution phase moves rectification further upstream, eliminates the central AC UPS, and distributes 800VDC across the full data hall via a common DC busway. The terminal state — MV to 800VDC via solid-state transformer (SST) — eliminates the LV transformer layer entirely, converting grid-level medium voltage (e.g., 35kVAC) directly to 800VDC in a single device rated up to 7.5MVA at ≥98.5% efficiency.

Figure 2. Nvidia 800 VDC Architecture for Next-Generation AI Infrastructure

[[KC_IMAGE_002]]

Source: Nvidia, Citi

Citi's proprietary projection for global data center buildout shows total capacity in service growing from 122GW in 2026E to 241GW by 2030E. North America and China are the primary buildout destinations, with hyperscaler self-build capacity surging alongside the buildout.

On an incremental basis, Citi projects annual new capacity additions at 21–32GW per year from 2026E through 2030E, suggesting the build cycle is entering a sustained high-volume phase rather than a single-year spike. North America contributes 7–13GW of incremental capacity annually, China 5–7GW, and hyperscaler self-build 3–5GW.

Figure 3. Total DC Capacity in Services (GW)

[[KC_IMAGE_003]]

Source: Citi Estimates

Figure 4. Incremental DC Capacity in Services (GW)

[[KC_IMAGE_004]]

Source: Citi Estimates

From a GPU chipset requirement perspective, demand for 800VDC-enabled capacity is rising steeply as a share of total new builds, underpinned by Nvidia's Rubin Ultra roadmap remaining intact. We project 800VDC's adoption demand based on the GPU rack deployment requirement at $16.0\%$ in 2027E, accelerating to $58.3\% / 72.9\% / 79.1\%$ in 2028E/29E/30E, reflecting the rising demand of the HVDC power rack driven by the commercial launch of 800VDC GPU platforms.

In the 800VDC adoption transition roadmap, sidecar dominates the early phase, with 3.9GW in 2027E and 12.9GW in 2028E, as existing facilities are retrofitted at the row level without large-scale grey-space reconstruction. We estimate SST-based builds could start in 2028E and accelerate to 11.5GW in 2029E and 17.8GW in 2030E, with SST adoption demand of total new capacity reaching 55.4% by 2030E.

Figure 5. Global Data Center Build-out with 800VDC Adoption Requirement by GPU Chip

[[KC_IMAGE_005]]

Source: Citi Estimates

Figure 6. Global Data Center Build-out by Architecture Type

[[KC_IMAGE_006]]

Source: Citi Estimates

On the cost side, according to SemiAnalysis' projection, the sidecar retrofit phase carries a modest near-term premium of +US\$0.40M/MW versus today's baseline. Going forward, with the transition to SST deployment, the total electrical cost per MW falls by US\$0.70M versus baseline as the central UPS, LV transformer, and LV switchgear are eliminated.

Figure 7. Total Electrical Content per MW Could Slightly Drop
\$M/MW (Grey + White space) · Right axis: System Efficiency %

[[KC_IMAGE_007]]

Source: SemiAnalysis, Citi

# Traditional AC Chain Has Four Lossy Conversion Stages — All of Which Collapse into One under 800VDC

We delve into AI data centers' power structure in grey space. The traditional architecture routes utility AC power to IT server in white space through the following major parts:

■ Transformer & MSB: after utility power intake, transformers convert medium-voltage grid power to low-voltage AC, then LV MSB performs power distribution.

■ UPS: provides power conditioning and short-term power backup. In double-conversion topology, the UPS performs AC→DC→AC conversion, introducing \~3–5% losses and requiring significant floor space and battery infrastructure.

■ PDU: distributes conditioned AC power to rack rows, with metering and circuit protection.

■ Rectification/inversion in-rack: PSU shelf inside each compute rack performs the final AC-to-DC conversion, outputting low-voltage DC to compute racks.

Besides, another important part in the data center power system is the back-up power, which is dominated by diesel generator set (GenSet) currently.

800VDC SST architecture replaces the lengthy AC chain with a single integrated device. The SST performs all necessary functions — power factor correction (PFC), voltage step-down, rectification/inversion, power control, etc — within a single compact unit. It accepts medium-voltage AC directly from the utility grid and outputs 800VDC to the DC distribution network, which feeds compute racks without further conversion until the final voltage step-down at the GPU board level. Between the SST and the IT server sits the sidecar or battery rack — a purpose-built intermediate module that serves as the intelligence and resilience layer of the 800VDC power chain.

Figure 8. Traditional power distribution architecture vs SST architecture

[[KC_IMAGE_008]]

Source: Citi

Implications of the 800VDC architecture span following structural dimensions:

\- Copper consumption saving: Doubling the distribution voltage from 415VAC to 800VDC halves the current required to deliver the same power, which translates directly into substantially thinner, lighter cables that dramatically reduce the cost of high-grade copper throughout the facility.

■ Equipment layers eliminated: UPS, LV transformer, PDU, and in-rack PSU shelf are all removed from the primary power path, reducing both capital cost and maintenance complexity.

■ PUE improvement: Elimination of AC/DC rectification across a MW-scale data center improves end-to-end power delivery efficiency and lowers cooling requirement, which significantly reduce operational PUE.

■ Native energy storage integration: Rather than a centralised UPS battery bank, energy storage is distributed natively on the 800VDC bus, creating a layered, resilient power architecture purpose-built for the dynamic demands of AI workloads. An 800VDC DC architecture also facilitates green energy sources and storage systems to connect directly to the facility power bus, which is a strategic enabler of hyperscalers with binding carbon neutrality commitments.

■ Footprint reduction: Grey-space power equipment, which in traditional facilities can consume 30–40% of total building area, is dramatically compressed — a critical advantage as power infrastructure increasingly rivals compute in space consumption.

## Key Equipment Demand Projection in 800VDC Transition

We estimate an outline of per-GW data center IT load normalised comparison of equipment capacity requirements across the two architectures, translating the qualitative architectural differences into concrete capacity demand metrics.

There are four major categories that define the traditional AC power chain — LV transformer/MSB, UPS and associate UPS battery, and PDU/RPP — will be integrated into a STT system in the 800VDC architecture. For every 1GW of new 800VDC data center IT load built, approximately 2,083 MVA of LV transformer procurement, 1,563 MW of UPS procurement, 1,500 MW of PDU procurement, and 326 MWh of UPS battery procurement are permanently forgone relative to the traditional architecture, on our estimates.

The 800VDC SST architecture introduces the following new major demand categories that have no precedents in traditional data center procurement:

■ BBU power at 840 MW/GW (housed in the sidecar or in battery rack, providing high-rate millisecond-to-second buffering), BBU battery at 76 MWh/GW (the energy storage element of the rack-level buffer).

■ BESS power requires 1,500 MW/GW at the facility level with BESS battery at 530 MWh/GW serving as facility-level energy storage, replacing the centralised UPS battery and adding peak shaving capability.

■ A DC distribution system of 1,500MW/GW will replace the traditional PDU.

■ Notably, the SST replaces the LV Transformer & MSB on a one-for-one MVA basis (2,083 MVA/GW in both architectures) — confirming that the total power conversion capacity requirement is unchanged, but the device performing that conversion is entirely different, with materially higher efficiency and functional integration.

Backup GenSet remains constant across both architectures. At 2,063 MVA/GW in both the traditional and 800VDC columns, the GenSet requirement is the sole equipment category that is genuinely architecture-neutral — driven purely by the total facility load (IT load × PUE × redundancy) rather than the AC/DC topology of the power distribution system. Backup GenSet can also be replaced by large scale energy storage batteries in the future when the economic yield becomes reasonable.

Figure 9. Key Power Equipment Capacity Requirements Per GW IT Load of Data Center Build-out


Source: Citi

## SST Demand Surges as LV Transformer Market Structurally Declines

We estimate total global transformer-equivalent capacity demand (SST + LV transformer combined) could grow from \~43,920 MVA in 2026E to \~67,000 MVA in 2030E, driven by 21.1GW (2026E) to 32.2 GW (2030E) data center buildout. Within this total, the compositional shift is dramatic: LV transformer demand progressively cedes share to SST as penetration accelerates. SST demand grows from 901 MVA in 2027E to 37,152 MVA in 2030E, while LV transformer demand drops from 55,380 MVA in 2027E to 29,909 MVA in 2030E.

## GenSet Capacity Demand Grows Steadily

GenSet demand is architecture-agnostic: whether a data center runs on 415VAC or 800VDC, it requires the same diesel backup generation capacity to cover full-facility load (IT + cooling + ancillary) in the event of a grid outage.

Total incremental GenSet capacity demand grows from 43,481 MVA in 2026E to 66,390 MVA in 2030E — a compound annual growth rate of 11% over the four-year period. This growth is a direct function of the absolute volume of new data center capacity being added globally. The implication is that GenSet manufacturers should face a straightforward, durable demand tailwind through 2030E.

Figure 10. Transformer Capacity Demand: SST to Replace LV Transformer/MSB

[[KC_IMAGE_009]]

Source: Citi Estimates

Figure 11. Backup GenSet Capacity Incremental Demand Driven by DC Buildout

[[KC_IMAGE_010]]

Source: Citi Estimates

## BESS and BBU Emerge as High-Growth New Categories While UPS Faces Structural Decline

We believe combined BESS and BBU battery capacity demand is negligible in 2026 (reflecting the early-stage 800VDC transition phase, which retains legacy UPS infrastructure), but should accelerate sharply from 2027 as native 800VDC deployments ramp. We estimate that BESS battery demand grows from 2,292 MWh in 2027E to 13,499 MWh in 2030E and BBU battery demand grows from 329 MWh in 2027E to 1,938 MWh in 2030E, representing a 2027–30E CAGR of 80%+ for BESS and BBU battery demand in the global data center buildout.

The functional distinction between BESS and BBU is critical to understanding their respective demand drivers. BBU — housed within the sidecar rack or battery rack — operates at the rack level in white space, providing millisecond-to-second buffering of GPU load swings via high-rate lithium batteries or supercapacitors.

BESS operates at the facility level, providing minute-scale backup power (replacing the centralised UPS), peak shaving of large cluster-level load ramps, and optionally grid frequency response services. The combined architecture represents a fundamental shift from centralised, AC-domain backup toward distributed, DC-native energy management — creating durable demand for LFP battery cells, battery management systems, and DC-coupled power conversion equipment across the value chain.

Figure 12. BESS and BBU Become Important Parts in 800VDC Architecture

[[KC_IMAGE_011]]

Source: Citi Estimates

Figure 13. ...While UPS to Be Replaced in SST Architecture

[[KC_IMAGE_012]]

Source: Citi Estimates

We believe UPS capacity demand — which remains elevated in 2026–27E as the sidecar retrofit phase retains legacy grey-space UPS infrastructure — should enter a sustained downtrend from 2028 as facility-level SST builds eliminate the UPS from the primary power path entirely. This decline will not be cyclical but structural within the 800VDC architectural paradigm.

# Key Beneficiaries across Infrastructure Stack within a Data Center

We map the physical and functional anatomy of an AI data center in Figure 14, from site infrastructure to rooftop mechanical systems, and identify the key equipment categories that should stand to benefit from the structural transition to 800VDC. We organise the investment implications across six major dimensions.

Data Center Operators: DC operators are the primary demand aggregators of this transition. Their campuses house every layer of the architecture illustrated from MV switchgear intake through to server halls, and their ability to deliver high-density, power-ready data centers to hyperscaler tenants is the central commercial proposition. When AI rack densities escalate and 800VDC becomes the delivery standard in the future, operators with flexible grey-space design and power infrastructure upgrade capability should command premium lease rates and stronger tenant retention.

Power Equipment: The power infrastructure layer — comprising MV switchgear/RMU, transformers, backup generators, UPS systems, and PUD/RPP — is the most directly disrupted segment. Under 800VDC, centralised AC UPS and LV transformers are progressively retired, replaced by upstream MV rectifiers and ultimately SST. This represents both displacement risk for incumbent AC equipment vendors and a significant new market for DC-native power conversion equipment manufacturers.

Battery Energy Storage Systems: The facility-level BESS becomes structurally more important under 800VDC, replacing the centralised UPS as the primary power resilience mechanism. China's dominant position in LFP battery manufacturing translates into a direct supply chain advantage, in our view. It is a meaningful revenue opportunity for battery system integrators serving the data center vertical.

IT Rack Power and Cooling: The GPU upgrade cycle is the primary demand driver for IT rack infrastructure including rack-level BBU. As successive GPU generations (Blackwell, Rubin, Kyber) deliver step-change improvements in compute density and performance, the associated rack system's power and cooling related components require corresponding upgrades. Vendors supplying high-density rack enclosures, power whips, and structured cooling solutions are incremental beneficiaries of this generational refresh cycle.

Cooling Solutions: Higher rack power densities enabled by 800VDC directly necessitate a parallel upgrade in thermal management. As per-rack power crosses the 100kW threshold, traditional air-cooling architectures become thermally insufficient. Liquid cooling solutions become standard deployment requirements rather than optional upgrades. Cooling solution providers with established data center verticals should benefit from this co-investment cycle alongside the power architecture transition.

Power Semiconductors: The shift to high-voltage DC conversion is a direct demand catalyst for wide-bandgap power semiconductors. SSTs, MV rectifiers, and high-efficiency DC/DC converters all rely on silicon carbide (SiC) and gallium nitride (GaN) devices to achieve the switching frequencies and efficiency levels required at 800VDC. This positions SiC/GaN device manufacturers as a key enabling layer of the entire 800VDC ecosystem.

## Figure 14. Data Center Architecture Layout and Key Asia Beneficiaries for 800VDC Transition

Delta (2308.TW)
Sieyuan Electric (002028.SZ)
TBEA (600089.SS)
TGOOD (300001.SZ)
Dongfang Electric (1072.HK)
Yantai Jereh (002353.SZ)
Hongfa (600885.SS)
Inovance (300124.SZ)
Weichai Power (2338.HK)
Mitsubishi Electric (6503.T)
Hyundai Electric (267260.KS)
Hyosung Heavy (298040.KS)
LS Electric (010120.KS)
Hitachi Energy India (HITN.NS)
GE Vernova T&D India (GETD.NS)
CG Power (CGPO.NS)
Siemens Energy India (SIEE.NS)


[[KC_IMAGE_013]]


Source: Citi

Delta (2308.TW)
LGE (066570.KS)
Envicool (002837.SZ)
Shenling (301018.SZ, Not Covered)
Dakin (6367.T)

Delta (2308.TW)
Lenovo (0992.HK)
ZTE (0763.HK)
BYD Electronics (0285.HK)
Dynapack (3211.TWO)
AES (6781.TW)
Panasonic HD (6752.T)
Yageo (2327.TW)
SEMCO (009150.KS)
Murata (6981.T)

## Battery Energy Storage System

BYD (1211.HK)
Sungrow (300274.SZ)
CATL (300750.SZ/3750.HK)
EVE Energy (300014.SZ)

VIS (5347.TWO)
UMC (2303.TW)
Renesas (6723.T)
SG Micro (300661.SZ)
CR Micro (688396.SS)
Silan Micro (600460.SS)
InnoScience (2577.HK, Not Covered)


# Deep Dive into Key Asia Beneficiaries in 800VDC Transition


We address the key Asia beneficiaries in data center operation, power grid and plant equipment, battery energy storage system, IT rack power and cooling, data center cooling solutions, semis and passive components in this section.

## Data Center Operators

In the China data center market, we like GDS and VNET. We see the transition as a positive demand catalyst in the near term, with manageable capex implications in the medium term, underpinned by the flexibility of their existing grey-space infrastructure and the competitive advantage of a mature domestic equipment supply chain.

AI demand remains the primary catalyst. We view that hyperscaler cluster rental pricing has stabilised and is showing early signs of reacceleration into 2H26, underpinned by sustained growth in LLM training and inference workloads, supporting accelerating EBITDA delivery for both GDS and VNET as committed pipelines convert to revenue in the coming years. The demand story remains intact as we outlined in our June's China Data Centers report.

800VDC commercial rollout in China is still in early stage. Domestic AI chip platforms (Huawei Ascend, domestic alternatives) have not yet been standardised on 800VDC power delivery, and rack power densities in China's AI compute ecosystem remain below the thresholds that are driving urgent 800VDC adoption. Thus, we believe there is minimal near-term capex pressure for GDS and VNET.

Capex impact likely manageable with a China supply chain advantage. Based on SemiAnalysis' phase analysis, the net capex differential of 800VDC versus traditional AC infrastructure is modest. Chinese IDC operators benefit from additional cost advantages: domestic LFP battery manufacturers provide best-in-class BESS at globally competitive prices, while domestic power equipment vendors offer structural pricing advantages. We believe GDS and VNET should be able to execute any future 800VDC transition at a meaningful discount to global capex benchmarks.

Grey-space design provides built-in upgrade flexibility. Well-designed grey-space infrastructure is compatible with row-level sidecar retrofit without structural rebuild. When domestic tenant demand for 800VDC materialises, GDS and VNET could respond with targeted, low-disruption upgrades on a campus-by-campus basis, avoiding stranded asset risk.

In Australia, NextDC (NXT AX, Buy) and CDC—owned by Infratil (IFT AX, Buy)—are among the leading DC operators. Both companies develop and operate data centers across Australia and New Zealand, serving hyperscalers, cloud providers, and colocation customers. Recent contract wins have lifted contracted capacity to roughly 700MW for NextDC and 1GW for CDC, reflecting strong demand for AI and cloud infrastructure. Both operators continue to expand their development pipelines, and future facilities could incorporate 800V DC power architecture to improve sellable capacity and enhance energy efficiency.

Among Australian real estate names, Goodman Group (GMG AX, Buy) and Stockland (SGP AX, Buy) offer growing exposure to the DC theme through large development pipelines. Both are investing in DC projects, either directly or through partnerships, with Stockland developing assets alongside EdgeConneX in a 50/50


joint venture. For both companies, the key value driver is likely to be development profit rather than recurring operating income, given their broader and diversified property portfolios. Goodman is advancing a global 6.4GW power bank with more than 500MW of near-term projects, and data centers could become a major earnings contributor, rising from around 10% of revenue in FY26 to 50–60% by FY29–30E. Stockland currently has no meaningful earnings exposure but could see data centers contribute 2–3% of earnings between FY28 and FY30, with further upside possible from future developments. As these projects are built out, both developers could incorporate 800V DC power architecture to improve sellable capacity.

## Power Equipment

## Power Grid Equipment

The Asia power grid equipment sector is supported by strong global demand, particularly for high-voltage transformers and switchgear serving the robust capital expenditure cycle in AC data-center development.

## We highlight major companies by country:

Taiwan: Delta Electronics (2308 TW, Buy) has successfully transformed from a traditional power supply manufacturer into a comprehensive AI infrastructure provider, offering solutions that span the entire power delivery chain from grid to chip. Delta's portfolio covers AC/DC conversion, HVDC power systems, rack-level power infrastructure, battery backup solutions, and liquid cooling technologies. This end-to-end capability positions the company uniquely within the AI data center ecosystem, as few competitors can provide integrated solutions across both power and thermal management. As data center operators increasingly prioritize efficiency, reliability, and deployment speed, Delta's ability to deliver a complete power architecture solution should become an increasingly important competitive advantage.

AI-related infrastructure, including power systems, power management equipment, and thermal solutions—is estimated to contribute 25-30% of Delta's total revenue in 2026, making it the company's largest growth engine. We expect this contribution to increase further as hyperscalers and cloud service providers accelerate the buildout of next-generation AI clusters. While near-term deployments are likely to focus on ±400V HVDC architectures, we anticipate initial shipment volumes to begin ramping in 2H26. The more meaningful inflection point should occur from 2027 onward, when 800V DC systems begin broader commercialization alongside the scaling of Nvidia's Rubin platform and other next-generation AI infrastructure deployments.

As rack power density continues to increase, the industry's transition toward higher-voltage architecture appears less a technology upgrade and more a structural necessity. Given Delta's leadership across the power infrastructure stack and its expanding exposure to AI power systems, we view the company as one of the direct and compelling beneficiaries of the multi-year transition to 800V DC data center architectures.

Korea: All major transformer and switchgear players, such as Hyundai Electric (267260 KS, Buy), Hyosung Heavy (298040 KS, Buy) and LS Electric (010120 KS, Buy), are getting more orders related to 800VDC applications. Regarding SST development, Hyosung Heavy developed 22.7kV SST technology back in 2022; for 800V DC architecture and data center applications, the company is in pilot and demonstration stage with a US hyperscaler; this phase is expected to be completed within 2026E. For Hyundai Electric, it is in an R&D phase for SST and has a three-year target. It has secured LV transformer orders for datacenter projects this year, which will be delivered from 2029. For LS Electric, it has developed prototype that


has been installed on an in-house test bed, though it is difficult to specify the schedule of commercial sales.

China: Sieyuan Electric (002028 CH, Buy) is a leading China high-voltage transformer and switchgear manufacturer; it has received orders for the former from data centers in the US. We believe China companies have competitive advantages in terms of lead time and production costs versus foreign peers. Sungrow (300274 CH, Buy) has launched new product for power distribution systems at AIDC; new orders are expected to be received in 2H26E and shipment would likely be made in 2027E. TGOOD (300001 CH, Buy) launched an AIDC integrated power supply product in June 2026, which can transform 110kV to 200-800V power supply for domestic customers, but it could also be an emerging LV transformer player in the future as it has a competitive cost structure with rising market share in non-US markets. Inovance (300124 CH, Buy) and Hongfa (600885 CH, Buy) have exposure to SST and power relay products.

Although a relatively late entrant to the space, Inovance has begun developing SST products targeting 800V DC AI data center applications. The company recently announced a collaboration with HCCCAP, a company incubated by Tsinghua University's carbon nanomaterials laboratory, to develop integrated power supply solutions for both AIDC and ESS. The partnership leverages HCCCAP's high-power pulse supercapacitor technology, which is designed to deliver power density of up to 100kW/kg. The solution is designed to provide millisecond-level response capabilities, enabling transient power support, peak-load buffering, and fail-safe backup function features that could become increasingly important as AIDC moves toward higher-voltage and higher-power-density architectures. That said, we believe commercialization remains at an early stage and therefore expect only limited revenue contribution from Inovance's 800V DC AIDC-related products in 2026-27. While we think the company is taking the right strategic steps to build exposure to next-generation power infrastructure, meaningful financial benefits are unlikely to materialize until broader adoption of 800V DC architectures gains traction over the longer term.

Hongfa is already a key supplier of relay products for AIDC infrastructure, with current exposure primarily through automatic transfer switches (ATS). As the industry transitions toward 800V DC power architectures, however, the company's addressable market should broaden significantly.

We expect Hongfa to supply a more comprehensive range of relay products across multiple power infrastructure components, including power distribution units (PDUs), battery backup units (BBUs), solid state transformers (SSTs), and other high-voltage power management systems. Such expansion would increase both content per deployment and the company's participation across the AI data center power chain.

According to management, revenue from 800V DC AI data center relay products could reach Rmb1.0-1.5bn in 2026. This estimate is based on several key assumptions: (1) relay content of approximately Rmb80,000-100,000 per MW of data center capacity, (2) global data center capacity reaching around 40GW, (3) 800V DC penetration rising to roughly 50%, and (4) Hongfa maintaining an approximately 50% market share in the relevant relay segment.

Commercialization could begin in earnest in 2H26, when Hongfa starts supplying 800V HVDC relay products to North American end customers through power infrastructure partners, such as Delta Electronics and other power management solution providers.


## Anusha Madireddy


Reflecting the growing adoption of AI infrastructure and next-generation power architectures, we expect AIDC-related revenue to increase from approximately 4-5% of total sales in 2025 to 8-10% in 2026E, before rising further to the mid-teen percentage range in 2027E. As 800V DC deployments scale, Hongfa's expanding product portfolio and strong position in the relay market should enable it to capture an increasing share of the power infrastructure value chain.

Japan: Mitsubishi Electric (6503 T, Buy) plans to expand its high-voltage transformer production capacity in Japan, North America and Southeast Asia. The expansion will be primarily through upgrading existing facilities plus partial expansion, not large-scale, completely new built ones. Mitsubishi Electric's cumulative high-voltage transformer production capacity, from the base in 2024, would be +15% in 2025, +30% in 2026E, +45% in 2027E and +50% in 2028E by spending US\$193m globally.

India: We believe India's DC market is approaching a critical inflection point, with accelerating demand, supportive government policies, and large-scale infrastructure expansion all converging. Global technology leaders, including Microsoft, Amazon, and Meta, have collectively announced commitments of approximately US\$67.5 billion toward AI and data center infrastructure in India, highlighting the country's growing importance within the global digital economy. Based on publicly disclosed company roadmaps, announced, planned, and early-stage capacity additions now exceed 8GW, with a majority expected to come online by 2032.

We believe India's leading transformer and T&D OEMs are well positioned to benefit from this buildout. Hitachi Energy India (HITN NS, Buy), GE Vernova T&D India (GETD NS, Buy), CG Power and Industrial Solutions (CGPO NS, Buy), and Siemens Energy India (SIEE NS, Neutral) have historically focused on domestic transmission projects and intra-group exports. However, all four companies are now actively expanding into the DC segment, representing a meaningful broadening of their addressable markets.

Hitachi Energy India estimates that its current addressable opportunity in AI-driven DC infrastructure accounts for roughly 10-15% of total DC capex. Through its "Grid-to-Rack" strategy, management aims to expand this exposure by an additional 15-20%, potentially increasing its addressable share to 25-35% of total AI DC infrastructure spend. To support this strategy, the company has announced a Rs10 billion capex program focused on localizing technologies tailored to India's AI DC requirements.

GE Vernova T&D India has already established an early track record in the DC market through supplies made to its parent company for US DC projects. This provides the company with valuable technical credentials and reference projects as it seeks to expand its presence in the domestic DC market.

CG Power and Industrial Solutions entered the DC export market in January 2025, securing a Rs9 billion order linked to a US DC project. We view this as an important validation of the company's DC product capabilities and a positive milestone as it positions itself for a larger role in India's rapidly expanding DC ecosystem.

Siemens Energy India is also expanding its DC product portfolio, with an increasing focus on solutions that support the growing power requirements of next-generation AI and hyperscale facilities.

With all four major India T&D OEMs actively broadening their DC offerings, we see DC-related TAM expansion as a key structural growth driver for the sector over the


coming years. The combination of accelerating domestic capacity additions, rising AI infrastructure investment, and increasing localization of DC supply chains should create a meaningful long-term opportunity for India's power equipment leaders.

## Power Plant Equipment

On power plant equipment, we are constructive, as the order mix shifts increasingly towards non-coal generation. Representatives in this space include Yantai Jereh Oilfield Services (002353 SZ, Buy), which benefits from the rapid expansion of AIDC in the US, capitalizing on two critical market shortages — power supply and gas turbines. Unlike many peers, Jereh has proactively secured a diversified and reliable gas turbine supply base, sourcing from industry heavyweights including GE Vernova, Baker Hughes, Siemens, and Kawasaki. This strategic procurement advantage has enabled Jereh to leverage its robust gas turbine power generator inventory to win incremental AIDC orders, positioning it ahead of competitors constrained by the prevailing gas turbine supply deficit.

Beyond equipment supply, Jereh is deeply embedded in the DC supply chain, offering integrated "Gas Turbine + Energy Storage" bundles and operating as a full EPC turnkey provider and equipment manufacturer for power integrated services. In early May, Jereh further strengthened its supply chain resilience by establishing a joint venture with FTAI, converting retired CFM56 jet engines into gas turbine power generators — securing yet another stable and cost-effective turbine source while gaining a unique entry point into the high-growth data center power market.

Dongfang Electric (1072 HK, Buy) should also stand to benefit meaningfully from rising demand for gas turbines from its North American datacenter customer.

In the power generation/backup segment, Weichai Power (2338 HK, Buy) provides critical onsite/backup power solutions for data centers. Its gas engines support high-power requirements in hybrid setups alongside 800VDC systems, ESS, and grid connections—essential for reliability in AI infrastructure buildout. Its products also provide an alternative to backup systems.

Power generation for AI data centers should be a key growth driver for Weichai going forward. We expect power generation for AI data centers to contribute 5%/8%/12% of its total revenue and 21%/38%/43% of total earnings in 202E/27E/28E. Further reading: Weichai Power (2338.HK) - Powering up more AIDCs; Lift up 26-28E NP by 4/13/56% and TP to HK\$50

Mgmt. expects 2–3 MW of gas engines to be launched in mid-2026 with mass delivery in 3Q/4Q26, and 5 MW of gas engines to see prototype & validation by end-2026 (link). As for profitability of gas engines (2-3 MW), mgmt. indicated their GPM is better than diesel engines GPM (35-40%), given higher ASP of US\$600k/MW versus diesel engine's Rmb1mn/MW. Gas engines production can share core engine line with diesel engines. The production line does not need large-scale reconstruction, with low conversion cost and strong flexible production capacity.


## Battery Energy Storage System

Battery energy storage systems (BESS) are quickly becoming essential infrastructure for AI factories. Unlike traditional data centers, AI factories are built to manufacture intelligence at scale. They run power-dense training and inference workloads, increasingly support agentic and reasoning models, and must deliver predictable performance even as compute demand shifts rapidly. In NVIDIA DSX, the platform for AI factories, BESS is part of the broader AI factory power architecture rather than a standalone add-on. Properly designed BESS can help AI factories connect faster, operate more reliably, reduce stress on the grid and onsite generation, and manage the fast-changing load profiles created by large-scale AI workloads.

BESS is an integrated system that combines battery cells with power conversion systems (PCS) inverters, advanced telemetry, and dynamic control schemes. The batteries store energy, but the inverters and controls make the system grid-interactive, shaping how power is absorbed, injected, and regulated in real time. BESS is a smart, controllable power asset, not a passive energy reservoir.

Figure 15. BESS design for AI factories

[[KC_IMAGE_014]]

Source: Nvidia, Citi

1GW of data centers for AI computing would need approximately 3.3GWh of BESS for backup power supply for grid-friendly data centers, according to Sungrow. The company projected that this emerging application could add 10-20GWh to BESS demand in the US in 2026, and demand could double yoy in 2027E. We see Sungrow as a key beneficiary as the company is one of the leading ESS suppliers in the US with 10-20% market share. At present, energy storage is being integrated into data center projects primarily because it grants priority in the project queue—projects equipped with storage can proceed ahead of others. Large-scale deployment of energy storage systems in data centers is likely to start from 2027 after the industry forms unified industry standards.

Among energy storage and inverter manufacturers we want to highlight: Sungrow (300274 CH, Buy), BYD (1211 HK, Buy), CATL (300750.SZ/3750.HK, Buy), and EVE Energy (300014.SZ, Buy).

Sungrow is supported by broadening product demand — including the launch of its new SST product line in July 2026 — as the US market transitions to 800VDC architecture. Sungrow planned to launch its 10kV SST product on 9 July 2026. This is a mature, market-ready version designed for immediate deployment based on extensive discussions held with potential clients across Europe, the US, and the domestic market. SST is a programmable, digital, and intelligent power supply component, which can drive the power electronics industry’s evolution from the analog and digital eras. The commercialization of STT is based on the essential technical foundation including the rapid advancements in high-frequency transformer materials and the SiC power device technology as well as comprehensive upgrades in fiber optics, DSP chips, and insulation technologies.

Sungrow possesses technical expertise in the fields of power electronics and new energy, thereby enabling the industrialization of SSTs. Sungrow's SST application is not limited to data center usage, it will also be applied to EV charging piles, energy storage, solar and wind power, and DC microgrids, etc.

BYD is a leading player in energy storage systems and battery solutions. It supplies high-safety LFP blade batteries, supporting DC-coupled systems, peak shaving, backup power, grid stabilization, and integration with high-voltage DC architectures in AI/data center environments.

Energy storage is a high-growth segment within BYD's broader new energy business. According to mgmt., ESS revenue accounted for around $10\%$ of total BYD revenue ( $>60\mathrm{GWh}$ shipment) in 2025, which we anticipate to rise to $12\% / 15\%$ of total revenue (150/200GWh) in 2027E/28E. Further reading: BYD (1211.HK) - May/Jun inventory estimate; 2Q-3Q earnings re-rating conditions almost mature, in our view

BYD continues to roll out large-scale ESS solutions (e.g., high-capacity containerized systems) tailored for reliable power in data centers and digital infrastructure. It has a strong track record in global deployments, with a focus on safety, high power density, and integration for modern DC-heavy environments.

CATL, as one of the leading players in ESS and battery solutions, is also pivoting from a pure ESS provider to a vertically integrated energy infrastructure solution provider for AI data centers, establishing an ecosystem to capitalize on the significant power demand from AI data centers in the long term.

Energy storage system business laid the foundation of the ecosystem – CATL has been dedicated in the ESS space for years, from pioneering LFP battery for ESS, to pursuing larger battery size from 314Ah to 587Ah, and now to launching its first validated sodium-ion energy system, showcasing its ambition against the backdrop of AI-driven power demand surges.

To midstream power conversion – CATL invested approximately US\$600mn for a 49% stake in Zhongheng Technology in April 2026, and therefore a \~17.4% stake in subsidiary Zhongheng Electric, to leverage Zhongheng's HVDC and solid-state

transformer strengths. Zhongheng Electric is a leading Chinese power solutions provider deeply integrated into the AI data center ecosystem driven by Nvidia, and its HVDC power technologies are used to cool and power next-generation GPU racks.

Going further downstream – Associated CATL funds reportedly agreed to buy up to a 38.1% stake in data center operator VNET Group, with a value of up to US\$942mn (Bloomberg, May 13, 2026). We view that the strategic acquisition indicates CATL's ambition to secure a foothold in the AIDC and data center infrastructure space.

EVE Energy is also one of the pioneers of energy storage systems, and ESS has been a major contributor to its business, contributing \~40% of topline revenue in 2025. EVE Energy keeps gearing up the R&D process and ventures into the rising AI space with competitive ESS battery products; it unveiled its comprehensive battery backup units (BBU) in June 2026 to cater for the differentiated demand emerging from AI data centers.

## IT Rack Power and Cooling

## Battery Backup Unit

BBU becomes increasingly essential under HVDC architecture: We believe the transition toward 800V HVDC architecture could further strengthen the importance of BBU in next-generation AI data centers. Under traditional AC power architectures, centralized UPS remains the primary backup solution, requiring multiple AC/DC and DC/AC conversion stages before power reaches IT equipment. By contrast, HVDC distributes high-voltage DC directly to the rack, making battery-based backup a more ideal extension of the rack-level DC power path.

As AI rack power increases from today's 100-150kW toward several hundred kilowatts in future platforms, power continuity becomes increasingly critical. A brief interruption can disrupt the high-value GPUs operating within a rack. We therefore believe backup power needs to move closer to the load to minimize conversion losses, improve ride-through response and simplify rack-level power delivery. Under HVDC architecture, BBU can be integrated directly into the DC distribution system, reducing reliance on multiple power conversion stages while improving overall system efficiency.

Importantly, we believe HVDC not only increases BBU adoption but could also drive up its content value. Higher rack power requires larger battery capacity, higher discharge power, more complex battery management system (BMS), thermal management, protection, and high-voltage safety design. We expect future BBU products are likely to evolve from relatively simple battery modules into integrated high-power subsystems with significantly greater content and system value.

Figure 16. Increasing Adoption of BBU in AIDC

[[KC_IMAGE_015]]


Figure 17. BBU Becomes Increasingly Essential under HVDC Power Architecture

[[KC_IMAGE_016]]


Figure 18. Estimated Content Value Per Rack by Generation

[[KC_IMAGE_017]]

Source: Citi, Citi Estimates

Figure 19. BBU Penetration Based on Our Estimates

[[KC_IMAGE_018]]


## We highlight major players by country:


Japan: Panasonic (6752 T, Buy) is a high-market-share supplier of battery backup units (BBUs) for servers and is already conducting R&D on high-output BBUs designed for dedicated power supply racks — a key component of the emerging 800VDC architecture. The company plans to be ready for mass production by FY3/27. In parallel, Panasonic expects to begin mass production of capacitor backup units (CBUs), which utilise supercapacitors to absorb temporary peak loads, also within FY3/27.

As a medium-term target, Panasonic has guided for ¥950 billion in sales across its combined BBU/CBU business by FY3/29, of which approximately ¥200 billion is expected to be contributed by next-generation products, including high-output BBUs and CBUs.

We estimate that data center-related businesses — including BBU/CBU — could account for more than 20% of Panasonic's adjusted operating profit by FY3/28, a rising earnings mix that we believe could help drive a re-rating of the stock.

Taiwan: Dynapack (3211 TT, Buy) has long-standing experience in lithium-ion battery pack design, battery management systems, safety certifications, and customized manufacturing. We believe BBU provides a meaningful growth opportunity beyond its mature consumer electronic battery-pack business and the company is well positioned to benefit from rising BBU demand driven by AIDC infrastructure buildout.

We estimate BBU sales likely contributed 35% of Dynapack's group sales in 2025 and could accelerate to 55%/67% of group sales in 2026E/2027E. We forecast Dynapack's sales to rise at a 34% CAGR in 2025-28E, boosted by the ongoing ramp-up of higher-power BBU products, rising rack power density leading to higher content value and penetration of BBUs, and the company's share gains.


A majority of products sold to PSU operators are 3KW and 5.5KW BBU modules in 2026 and the company expects to start selling small volume of higher-KW products (8.5KW, 12.4KW) in 4Q26. The products for HVDC (25KW BBU) could begin mass production in 2027, further fueling topline growth. Further reading: Taiwan Electronic Components & Equipment - Riding the AIDC BBU Growth Cycle; Initiate Dynapack at Buy.

AES (6781 TT, Buy) is also a direct beneficiary of AIDC BBU adoption, in our view. BBU now contributes $>70\%$ of sales and should remain the key earnings driver as AI rack power continues to rise. We expect AES to benefit from higher BBU content per rack and deep CSP engagement as the industry transitions from conventional 48V systems to HVDC architecture.

We expect high-voltage (+/-400V and 800V) BBU solutions to enter volume production in early 2027, supported by next-generation AI racks with higher power density. The transition raises technical barriers, which should favor established suppliers with proven system integration capability. We estimate AES's sales to rise at a $24\%$ CAGR in 2025-28E.

## Rack Cooling

Lenovo (0992 HK, Buy) and ZTE (0763 HK, Neutral) should benefit from IT rack cooling requirement upgrade, driven by higher power density requirement amid the 800VDC transition. We see increasing participation of China's electronic supply chain to join the Nvidia 800VDC ecosystem, especially the MGX platform, to provide components for power systems and cooling solutions.

We see 800VDC adoption and the associated rack density and thermal management requirements it drives as potential multi-year tailwinds for Lenovo's ISG order intake. Lenovo has invested meaningfully in Neptune liquid cooling technology, its proprietary direct liquid cooling (DLC) architecture, which is already deployed at scale at several hyperscalers' data centers globally. As per-rack power densities cross the 100kW threshold and approach 600kW+ with Blackwell and future GPU generations, Neptune-equipped rack solutions should become a prerequisite, rather than a premium option — expanding Lenovo ISG's addressable market and improving its solution ASPs. The shift toward differentiated, high-density AI rack systems with integrated liquid cooling represents a meaningful mix-shift opportunity toward higher-margin, solution-oriented revenue for Lenovo, in our view.

ZTE's data center business supplies high-density IT rack enclosures, integrated power distribution modules, and liquid cooling units to domestic cloud and telco data center customers. The 800VDC transition reinforces demand across all three product lines simultaneously: higher-density GPU deployments drive IT cabinet upgrades; the shift from AC UPS to DC-native power delivery creates replacement demand for ZTE's modular power systems; and rising rack thermal loads necessitate liquid cooling co-deployment. ZTE's established relationships with China's major telco operators provide a natural distribution channel for its integrated data center infrastructure products.

Lead Wealth, under BYD Electronics (285 HK, Sell), is one of the MGX electronica ecosystem companies for 800VDC data centers. It provides power system components such as power shelf, cold plate, UQD, CDU, manifold, PDP, busbar, etc. The company can leverage its precision mechanical capability and CNC capacity to support the ramp. But currently, contribution is still small.

## MLCC

We believe passive components are poised to benefit from a structural increase in content intensity. Unlike power semiconductors, capacitors, resistors and inductors are required throughout every stage of the power delivery chain—from front-end EMI filtering and surge protection, through intermediate DC/DC conversion, to final power delivery network (PDN) stabilization near the processor. The shift to 800VDC introduces higher power density, more conversion stages, and tighter power integrity requirements, resulting in increased passive component usage per rack. As next-generation AI clusters scale in power consumption and computing density, we expect passive content per compute unit to rise meaningfully, creating a broad-based and recurring demand driver across the passive component ecosystem.

Murata (6981 JT, Buy) is the global leader in MLCCs and we believe it is increasingly well positioned to benefit from the AI data center power buildout. Beyond its dominant MLCC franchise, the company is expanding into next-generation power solutions, including vertical power delivery (VPD) technology, which brings power conversion closer to the processor to improve efficiency and reduce power loss. Murata also offers intermediate bus converters (IBCs) and front-end AC-DC power solutions, giving it exposure across both board-level components and power delivery systems.

We estimate Murata holds roughly 50% share of the AI data center MLCC supply chain, while its power business is entering early stages of commercialization. As adoption of next-generation power architecture accelerates, we believe Murata should be well positioned to expand its presence in power infrastructure alongside its established MLCC leadership. We expect AI data center applications to account for approximately 25% of MLCC revenue in FY26 and 38% in FY27, up from around 12% in FY25. Meanwhile, the power business remains small at about ¥28bn in revenue (less than 2% of sales) but is approaching a meaningful growth phase as VPD and other advanced power solutions move into volume production.

Overall, we continue to view Murata as the best-positioned player in the MLCC industry, supported by its technology leadership, market share, and growing exposure to next-generation AI power infrastructure. A key catalyst to watch is the pace of adoption of its power modules, particularly VPD-based solutions.

In Korea, Samsung Electro-Mechanics (009150 KS, Buy), leveraging its position as the world's second-largest MLCC manufacturer, is benefiting from rapidly growing demand for both AI-grade MLCCs and embedded MLCC solutions as hyperscalers and cloud service providers scale next-generation AI infrastructure.

As AI servers become increasingly power-intensive, the number and complexity of MLCCs required per system continue to rise. The transition to higher-voltage, higher-power-density architectures is driving greater demand for high-capacitance, high-voltage, and high-reliability MLCCs, creating a structural content increase per server and per rack. We believe this trend will serve as a powerful long-term demand driver for Semco's high-specification passive component portfolio, positioning the company as one of the most direct beneficiaries of the AI-driven upgrade cycle in data center power infrastructure.

We forecast Semco's MLCC ASP to increase by approximately 30% YoY in 2026E and a further 71% YoY in 2027E. This growth should be supported by sustained AI server demand, a richer product mix, and increasing MLCC content requirements across next-generation 800VDC power architectures. The transition to higher-voltage and higher-power-density systems is driving demand for more advanced


MLCCs with enhanced capacitance, voltage tolerance, and reliability characteristics.

Supply conditions for AI-grade MLCCs are also expected to tighten through 2027E, reflecting strong AI infrastructure investment and a limited number of suppliers capable of producing the specialized components required for AI servers. We believe the industry is entering a period of increasing supply-demand imbalance as hyperscalers and OEMs accelerate deployment of next-generation AI clusters.

Semco appears particularly well positioned to benefit from this trend, in our view. Customer interest remains strong for the company's newly launched 47 $\mu$ F AI server MLCCs, while demand is also rising for high-voltage MLCCs rated above 1kV, which are increasingly required to improve power conversion efficiency in 800VDC systems. In addition, the transition toward 800Gbps and 1.6Tbps optical interconnects is driving demand for ultra-high-capacitance MLCCs exceeding 100 $\mu$ F, further expanding content opportunities for Semco across the AI infrastructure value chain.

Overall, we believe Semco's technology leadership in high-value MLCC products, combined with the industry's migration toward 800VDC power architectures, should position the company as one of the most direct beneficiaries of the next wave of AI data center infrastructure investment.

In Taiwan, Yageo (2327 TT, Buy) offers one of the most comprehensive exposure to the 800VDC power architecture. Through its leading positions in MLCCs, tantalum capacitors, resistors, and magnetic components, the company participates across virtually every power conversion and power distribution stages, providing a breadth of exposure that few single-product peers can replicate. At the high-voltage front end, Yageo is benefiting from strengthening demand for high-reliability NPO MLCCs, where industry supply remains tight. Based on our industry checks, lead times have extended and key customer orders are likely to resume in 2H26. At the processor-level PDN layer, Yageo's KEMET tantalum capacitors remain a preferred solution among major hyperscaler customers due to their superior reliability and power efficiency characteristics. This business also represents one of the company's highest-margin product segments. Meanwhile, at intermediate power conversion stages, Yageo's high-capacitance MLCC portfolio should be well positioned to capture incremental demand as several Japanese and Korean competitors increasingly allocate production capacity toward premium AI-grade and automotive products, creating opportunities for market share gains in mainstream and mid-range applications.

While Yageo does not separately disclose revenue attributable to 800VDC infrastructure, the broad deployment of passive components throughout the power delivery chain creates a portfolio-wide demand uplift. AI-related revenue contribution has already increased from approximately 4% of total sales in early 2025 to around 15% in 1Q26, reflecting accelerating adoption of AI server infrastructure.

Looking further ahead, we estimate that next-generation AI rack architectures in 2027-28 could drive more than a $50\%$ increase in MLCC unit consumption per rack, accompanied by substantially higher value content due to stricter performance specifications. In parallel, tantalum capacitors are expected to become an increasingly important growth driver, with tantalum-related revenue contribution potentially exceeding $25\%$ of total sales over time.


The tantalum market backdrop remains supportive, in our view. Ongoing supply disruptions have pushed tantalum ore prices higher, leading Yageo to implement three rounds of price increases since 2025. With supply-demand conditions remaining tight, we believe additional pricing actions could follow in 2H26, providing a further tailwind to margins and earnings growth.

## Cooling Solutions

In Korea, LG Electronics (066570 KS, Buy) should benefit from the 800VDC transition through its growing exposure to AIDC cooling infrastructure.

LGE's initial focus is on supplying air-cooling solutions, including its proprietary high-efficiency chillers, to AIDC. These products could serve as the company's primary entry point in the rapidly expanding AI infrastructure market. Over time, LGE plans to commercialize liquid cooling systems, which are increasingly viewed as a necessity for next-generation AI clusters as rack power densities continue to rise beyond the practical limits of conventional air cooling.

This roadmap positions LGE to progressively expand its exposure across the data center thermal management value chain, from traditional HVAC systems to advanced liquid cooling solutions that support future 800VDC AI architectures.

The opportunity builds upon LGE's established strengths in the HVAC market. According to management, HVAC revenue has increased approximately fourfold since 2001, while commercial and industrial HVAC revenue has grown roughly 30-fold over the same period, reflecting the company's successful expansion into higher-value enterprise applications.

Supported by a global manufacturing footprint of 12 production sites, LGE can provide end-to-end HVAC solutions, encompassing product development, manufacturing, installation, and after-sales service. This global and integrated service capability should enhance its competitiveness as hyperscalers and data center operators increasingly seek reliable partners for large-scale AI infrastructure deployments.

In China, we highlight Envicool (002837 SZ, Sell) as one of China's leading liquid cooling solution providers. The company has established a comprehensive liquid cooling portfolio covering full-chain liquid cooling systems, immersion cooling solutions, coolant distribution units (CDUs), and related thermal management infrastructure designed for next-generation AI data centers and Nvidia-based AI server deployments.

The transition toward 800VDC architecture could accelerate liquid cooling adoption. As rack power density rises beyond the capability of conventional air-cooling systems, liquid cooling becomes increasingly necessary to managing higher thermal loads, while maintaining power efficiency and system reliability. This structural shift should create meaningful demand opportunities for Envicool's liquid cooling offerings over the coming years.

However, despite the favorable industry backdrop, we maintain our Sell rating. We estimate the liquid cooling business will contribute only a mid-single-digit to high-single-digit percentage of total revenue in 2026, up from approximately 3% in 2025. While growth is impressive, the segment remains relatively small compared with the company's overall revenue base.

In addition, competitive intensity is rising rapidly. Domestic players such as Shenling (301018 SZ, non-rated) are aggressively expanding their presence in


liquid cooling solutions for Nvidia AI servers, which could pressure both market share and pricing over time. As a result, we view liquid cooling primarily as a volume growth story for Envicool rather than a significant margin expansion opportunity.

Notably, profitability within the liquid cooling segment has yet to demonstrate a clear advantage over the company's traditional air-cooling business. Gross margins of liquid cooling products were broadly comparable to those of air-cooling solutions last year, suggesting limited operating leverage despite strong demand growth. Execution also remains a concern. Envicool missed earnings expectations for three consecutive quarters, from 3Q25 through 1Q26, raising questions over the pace at which the company can translate industry tailwinds into consistent financial performance.

In Japan, Daikin (6367 T, Buy) is a key AI infrastructure name to watch. The company expects revenue from the North American DC cooling market to more than triple to over ¥300 billion (US\$1.9 billion) by 2030, supported by direct sales to hyperscalers such as AWS and Google, which typically carry higher margins. Even if the industry's transition to 800VDC power architecture progresses more slowly than expected, we believe Daikin remains well positioned to achieve its targets. Recent acquisitions, including Chilldyne, have strengthened its liquid-cooling capabilities, with direct-to-chip cooling solutions expected to deliver a 25%+ sales CAGR over the next five years.

Looking ahead, an important industry trend is the shift toward more efficient power architectures in data centers. Cooling accounts for more than 60% of non-IT power consumption, yet no major vendor currently offers a fully DC-native cooling system. For now, this supports strong demand for power-management components such as inverters. However, the emergence of DC-native cooling solutions could eventually disrupt parts of the existing inverter supply chain.

## Power Semiconductors

As addressed in our US tech team's note (US Semiconductors - 800V DC Transition Drives Stronger Analog Recovery), the shift to high-voltage DC conversion is a direct demand catalyst for wide-bandgap power semiconductors. SSTs, MV rectifiers, and high-efficiency DC/DC converters all rely on silicon carbide (SiC) and gallium nitride (GaN) devices to achieve the switching frequencies and efficiency levels required at 800VDC. This positions SiC/GaN device manufacturers as a key enabling layer of the entire 800VDC ecosystem.

We see 800VDC adoption driving demand for: 1) high-voltage power discrete and modules (SiC MOSFET, GaN, SJ MOSFET, and 2) PMIC and analog IC, especially for multi-phase controllers, DrMOS, high-current DC/DC, and more. CR Micro estimates (citing TrendForce) the AI server power market to grow from US\$7.4bn in 2025 to US\$32.5bn in 2027 (CAGR of 110%), leading to significant growth for power semiconductors. While international CSPs typically prefer non-Chinese semiconductor vendors in their supply chain, we believe China's domestics market is sufficiently large, accounting for roughly one-third of global server shipment, with meaningful localization potential. We see SG Micro (300661.SZ, Buy), CR Micro (688396.SS, Neutral) and Silan Micro (600460.SS, Neutral) as key beneficiaries.

We believe SG Micro stands to benefit from the industry shift towards 800VDC given its growing product portfolio for 1) server power management: high-power DC/DC, eFuse, DrMOS, 2) networking: TEC drivers, AFE, 3) signal chain: ADC/DAC, OpAmps. Content value could reach several US\$ per optical module and US\$30-


50 per server. Computing & networking revenue contribution rose from 12% in 2024 to 15% in 2025, and likely 20% in 1Q26. We expect the strong demand to become an increasingly important growth driver for the company. We also believe CR Micro and Silan Micro could benefit from accelerating SiC/GaN and high-voltage MOSFET demand, leading to improving capacity utilization and product mix.

As noted in our recent Suzhou tech tour takeaways, InnoScience is a domestic GaN supplier. Management's estimate of \~100,000 GaN chips per MW of data center power — at a data center ASP of US\$1.0–2.0 per unit — directly ties InnoScience's revenue trajectory to the 800VDC buildout cycle. The company's 8-inch Si-based GaN production line has a self-assessed 2-3 year lead over 6-inch peers and it targets 70k/month capacity by end-2027/early-2028. Although management estimates China's domestic 800VDC adoption to lag international peers, it aims to further amplify 800VDC revenue contribution through the planned mix shift from modules toward higher-margin wafers and chips.

We see Taiwanese foundries as key beneficiaries of the transition toward 800V HVDC data center architectures. Higher operating voltages are driving increased demand for advanced BCD technologies, alongside broader adoption of GaN and SiC process platforms to improve power efficiency and address increasingly stringent thermal management requirements.

Within this evolving power infrastructure, Vanguard (5347 TT, Buy) and UMC (2303 TT, Buy) occupy critical positions in the semiconductor manufacturing stack that converts high-voltage grid power into stable computing voltages for AI servers and data centers. While VIS is primarily exposed to the front-end of power distribution and conversion, UMC is more leveraged to downstream power management functions closer to the processor.

We believe VIS is particularly well positioned at the high-voltage end of the power chain. Leveraging its mature-node manufacturing platform, the company supplies key power semiconductor components such as high-voltage isolation ICs, hot-swap controllers, and power management devices used in power supplies and rack-level power conversion systems. More importantly, VIS is one of the few foundries offering a comprehensive power process portfolio across a broad voltage range. Through its licensing agreement with TSMC for 80V and 650V GaN technologies, combined with its proprietary GaN-on-QST platform, VIS supports both silicon-based and GaN manufacturing, providing solutions spanning sub-200V, 650V, and up to 1,200V applications. This positions the company as a one-stop manufacturing partner for next-generation high-efficiency power devices across the data center power architecture.

The transition to higher-voltage power distribution should drive growing content opportunities for PMICs and other power devices. We estimate revenue contribution from data center-related PMICs could increase from a single-digit percentage of VIS's sales in 2025 to a high-teen percentage in 2026, with further expansion over the following years as AI infrastructure deployment accelerates. In parallel, VIS's Singapore expansion, which plans to lift capacity to approximately 44,000 wafers per month by 2029, should provide additional room to capture rising demand for high-voltage power semiconductors and advanced power management applications.

Moving further downstream in the power architecture, voltage is progressively stepped down through multi-phase voltage regulator modules (VRMs) before reaching the processor. At this stage, the critical challenge shifts from high-voltage power conversion to precise power regulation and distribution. These functions rely on highly integrated PMICs that combine analog, logic, and power devices on a single chip, requiring sophisticated BCD and embedded high-voltage process technologies.

This is where UMC is strategically positioned. The company is leveraging its leading BCD and embedded high-voltage platforms to enable next-generation PMICs that improve power efficiency within an increasingly dense and power-intensive AI computing environment. As demand for PMICs rises alongside the adoption of 800V HVDC architectures, UMC should see increasing opportunities in specialty-node manufacturing. The company is also expanding capacity in Singapore with a focus on 22/28nm and specialty technologies, strengthening its ability to support the growing market for power management and high-power semiconductor applications.

In Japan, Renesas Electronics (6723 T, Neutral) currently supplies products for data centers that integrate power management ICs and power semiconductors. In recent years, this area has been a major driver of revenue growth for the data center segment. Renesas announced a product compatible with 800VDC architecture. Specifically, it announced a 400V-compatible product that uses GaN, gallium nitride, as a power semiconductor. This enables support for 800V by using multiple units. The GaN technology is derived from Transphorm, which was acquired in 2024. The company held its Capital Market Day in Jun-25, 2026 and commented that the AI infrastructure business, including the digital power business, could account for just under 20% of total company revenue in 2026 and c40% by 2030, thereby positioning AI infrastructure as the company's growth driver for the foreseeable future.

Glossary


## Appendix A-1
