# Asia Communication Infrastructure

## 800VDC Architecture for Next-Generation AI Data Centers

## Overview

In this report, we outline likely implications of the 800VDC transition and potential Asia beneficiaries in the grey space and IT rack power/cooling in AI datacenters. As GPU rack power density approaches 1MW, we project 800VDC to reach 79% of new global DC capacity by 2030E, with SST demand surging from 901 MVA in 2027E to 37,152 MVA in 2030E to replace traditional LV transformers. 800VDC architecture is driving combined BESS and BBU battery demand at an 80%+ CAGR through 2030E. We see this as a multi-layer opportunity across six segments: DC operators; power equipment names; BESS and BBU suppliers; IT rack power/cooling vendors; liquid cooling providers; and power semiconductor suppliers.

Traditional AC Chain Gives Way to SST — GPU rack power density has grown nearly 100x since 2020, rendering conventional AC distribution physically unviable. We project 800VDC adoption to reach 79% of new global data center capacity by 2030E, displacing legacy power architecture while creating new equipment categories including SST, BESS, BBU, and new cooling solutions.

Data Center Operators — We expect the near-term AI demand tailwind to be intact. We observe China DC market leaders GDS and VENT. In Australia, we think NextDC and CDC/Infratil are positioned to incorporate 800VDC into future builds.

Power Equipment — We see Delta as uniquely positioned with end-to-end grid-to-chip portfolio. Hyosung, Sieyuan and TGOOD should benefit from LV transformer and SST for domestic buildout and export opportunities. Hongfa should ride rising relay products for 800VDC migration. Hitachi Energy India, GE Vernova T&D India, CG Power and Industrial should benefit from India domestic demand and exports.

BESS — 800VDC battery demand could accelerate at an 80%+ CAGR in 2027-30E; Sungrow (SST launch July 2026), BYD, CATL and EVE Energy are key participants.

IT Rack Power & Cooling — We forecast BBU content value per rack to rise from US\$4-5K in 2022 to US\$33-34K by 2029E, with Panasonic, Dynapack and AES the direct plays. We see Murata, SEMCO and Yageo as key MLCC participants. We also believe Taiwan and Chinese rack cooling players may benefit from IT cabinets and liquid cooling upgrade.

Cooling Solutions— Higher rack power densities make liquid cooling a structural necessity. LG Electronics, Daikin and Envicool are key names to watch.

Power Semiconductors — VIS leads at high-voltage front end; UMC leveraged to PMIC/BCD specialty nodes; Renesas could benefit via Transphorm GaN acquisition. For China, SG Micro, CR Micro and Silan Micro could benefit from SiC/GaN demand.

## Contents

800VDC Architecture for Next-Generation AI Data Centers 3
Nvidia's 800VDC Architecture: Four Generations, from Multi-Stage AC to a Single Integrated DC Conversion 4
Traditional AC Chain Has Four Lossy Conversion Stages — All of Which Collapse into One under 800VDC 7
Key Equipment Demand Projection in 800VDC Transition 9
Key Participants across Infrastructure Stack within a Data Center 12
Deep Dive into Key Asia Participants in 800VDC Transition 14
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

Figure 1. 800VDC Architecture Key Potential Asia Participants (data as at 16-Jul-2026)

[Table omitted for brevity - contains company names, tickers, ratings, and financial metrics]

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: dataCentral, Citi

# Nvidia's 800VDC Architecture: Four Generations, from Multi-Stage AC to a Single Integrated DC Conversion

NVIDIA's reference architecture defines 4 generations of data center power distribution, each representing a step-change reduction in conversion stages (Figure 1). Today's incumbent 415VAC architecture routes power through five or more sequential stages (transformer, LV switchboard, AC UPS, PDU, and in-rack PSU) before reaching the compute chip at 54VDC. The first transition step, 800VDC White Space Retrofit, inserts an LV Rectifier and a dedicated HVDC Power Sidecar rack into existing facilities, converting AC to 800VDC at the row level without disturbing grey-space infrastructure. The subsequent Hybrid Power Distribution phase moves rectification further upstream, eliminates the central AC UPS, and distributes 800VDC across the full data hall via a common DC busway. The terminal state — MV to 800VDC via solid-state transformer (SST) — eliminates the LV transformer layer entirely, converting grid-level medium voltage (e.g., 35kVAC) directly to 800VDC in a single device rated up to 7.5MVA at ≥98.5% efficiency.

Figure 2. Nvidia 800 VDC Architecture for Next-Generation AI Infrastructure

Source: Nvidia, Citi

Citi's proprietary projection for global data center buildout shows total capacity in service growing from 122GW in 2026E to 241GW by 2030E. North America and China are the primary buildout destinations, with hyperscaler self-build capacity surging alongside the buildout.

On an incremental basis, Citi projects annual new capacity additions at 21–32GW per year from 2026E through 2030E, suggesting the build cycle is entering a sustained high-volume phase rather than a single-year spike. North America contributes 7–13GW of incremental capacity annually, China 5–7GW, and hyperscaler self-build 3–5GW.

Figure 3. Total DC Capacity in Services (GW)

Figure 4. Incremental DC Capacity in Services (GW)

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi Estimates

From a GPU chipset requirement perspective, demand for 800VDC-enabled capacity is rising steeply as a share of total new builds, underpinned by Nvidia's Rubin Ultra roadmap remaining intact. We project 800VDC's adoption demand based on the GPU rack deployment requirement at 16.0% in 2027E, accelerating to 58.3% / 72.9% / 79.1% in 2028E/29E/30E, reflecting the rising demand of the HVDC power rack driven by the commercial launch of 800VDC GPU platforms.

In the 800VDC adoption transition roadmap, sidecar dominates the early phase, with 3.9GW in 2027E and 12.9GW in 2028E, as existing facilities are retrofitted at the row level without large-scale grey-space reconstruction. We estimate SST-based builds could start in 2028E and accelerate to 11.5GW in 2029E and 17.8GW in 2030E, with SST adoption demand of total new capacity reaching 55.4% by 2030E.

Figure 5. Global Data Center Build-out with 800VDC Adoption Requirement by GPU Chip

Figure 6. Global Data Center Build-out by Architecture Type

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi Estimates

On the cost side, according to SemiAnalysis' projection, the sidecar retrofit phase carries a modest near-term premium of +US\$0.40M/MW versus today's baseline. Going forward, with the transition to SST deployment, the total electrical cost per MW falls by US\$0.70M versus baseline as the central UPS, LV transformer, and LV switchgear are eliminated.

Figure 7. Total Electrical Content per MW Could Slightly Drop

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: SemiAnalysis, Citi

# Traditional AC Chain Has Four Lossy Conversion Stages — All of Which Collapse into One under 800VDC

We delve into AI data centers' power structure in grey space. The traditional architecture routes utility AC power to IT server in white space through the following major parts:

■ Transformer & MSB: after utility power intake, transformers convert medium-voltage grid power to low-voltage AC, then LV MSB performs power distribution.

■ UPS: provides power conditioning and short-term power backup. In double-conversion topology, the UPS performs AC→DC→AC conversion, introducing ~3–5% losses and requiring significant floor space and battery infrastructure.

■ PDU: distributes conditioned AC power to rack rows, with metering and circuit protection.

■ Rectification/inversion in-rack: PSU shelf inside each compute rack performs the final AC-to-DC conversion, outputting low-voltage DC to compute racks.

Besides, another important part in the data center power system is the back-up power, which is dominated by diesel generator set (GenSet) currently.

800VDC SST architecture replaces the lengthy AC chain with a single integrated device. The SST performs all necessary functions — power factor correction (PFC), voltage step-down, rectification/inversion, power control, etc — within a single compact unit. It accepts medium-voltage AC directly from the utility grid and outputs 800VDC to the DC distribution network, which feeds compute racks without further conversion until the final voltage step-down at the GPU board level. Between the SST and the IT server sits the sidecar or battery rack — a purpose-built intermediate module that serves as the intelligence and resilience layer of the 800VDC power chain.

Figure 8. Traditional power distribution architecture vs SST architecture

© 2026 Citi Inc. No redistribution without Citi's written permission.
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

| Per GW - Equipment Capacity | Traditional | 800VDC SST | Unit | Note |
|---|---|---|---|---|
| LV Transformer/MSB | 2,083 | - | MVA | Substituted by SST |
| SST | - | 2,083 | MVA | Integrated SST |
| Backup GenSet | 2,063 | 2,063 | MVA | Can be Battery |
| UPS | 1,563 | - | MW | Eliminated |
| PDU | 1,500 | - | MW | Eliminated |
| DC distribution | - | 1,500 | MW | in Sidecar/Integrated SST |
| UPS Battery | 326 | - | MWh | Eliminated |
| BBU Power | - | 840 | MW | in Sidecar/Integrated SST |
| BBU Battery | - | 76 | MWh | in Sidecar/Integrated SST |
| BESS Power | - | 1,500 | MW | Facility level |
| BESS Battery | - | 530 | MWh | Facility level |

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

## SST Demand Surges as LV Transformer Market Structurally Declines

We estimate total global transformer-equivalent capacity demand (SST + LV transformer combined) could grow from ~43,920 MVA in 2026E to ~67,000 MVA in 2030E, driven by 21.1GW (2026E) to 32.2 GW (2030E) data center buildout. Within this total, the compositional shift is dramatic: LV transformer demand progressively cedes share to SST as penetration accelerates. SST demand grows from 901 MVA in 2027E to 37,152 MVA in 2030E, while LV transformer demand drops from 55,380 MVA in 2027E to 29,909 MVA in 2030E.

## GenSet Capacity Demand Grows Steadily

GenSet demand is architecture-agnostic: whether a data center runs on 415VAC or 800VDC, it requires the same diesel backup generation capacity to cover full-facility load (IT + cooling + ancillary) in the event of a grid outage.

Total incremental GenSet capacity demand grows from 43,481 MVA in 2026E to 66,390 MVA in 2030E — a compound annual growth rate of 11% over the four-year period. This growth is a direct function of the absolute volume of new data center capacity being added globally. The implication is that GenSet manufacturers should face a straightforward, durable demand tailwind through 2030E.

Figure 10. Transformer Capacity Demand: SST to Replace LV Transformer/MSB

Figure 11. Backup GenSet Capacity Incremental Demand Driven by DC Buildout

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi Estimates

## BESS and BBU Emerge as High-Growth New Categories While UPS Faces Structural Decline

We believe combined BESS and BBU battery capacity demand is negligible in 2026 (reflecting the early-stage 800VDC transition phase, which retains legacy UPS infrastructure), but should accelerate sharply from 2027 as native 800VDC deployments ramp. We estimate that BESS battery demand grows from 2,292 MWh in 2027E to 13,499 MWh in 2030E and BBU battery demand grows from 329 MWh in 2027E to 1,938 MWh in 2030E, representing a 2027–30E CAGR of 80%+ for BESS and BBU battery demand in the global data center buildout.

The functional distinction between BESS and BBU is critical to understanding their respective demand drivers. BBU — housed within the sidecar rack or battery rack — operates at the rack level in white space, providing millisecond-to-second buffering of GPU load swings via high-rate lithium batteries or supercapacitors.

BESS operates at the facility level, providing minute-scale backup power (replacing the centralised UPS), peak shaving of large cluster-level load ramps, and optionally grid frequency response services. The combined architecture represents a fundamental shift from centralised, AC-domain backup toward distributed, DC-native energy management — creating durable demand for LFP battery cells, battery management systems, and DC-coupled power conversion equipment across the value chain.

Figure 12. BESS and BBU Become Important Parts in 800VDC Architecture

Figure 13. ...While UPS to Be Replaced in SST Architecture

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi Estimates

We believe UPS capacity demand — which remains elevated in 2026–27E as the sidecar retrofit phase retains legacy grey-space UPS infrastructure — should enter a sustained downtrend from 2028 as facility-level SST builds eliminate the UPS from the primary power path entirely. This decline will not be cyclical but structural within the 800VDC architectural paradigm.

# Key Participants across Infrastructure Stack within a Data Center

We map the physical and functional anatomy of an AI data center in Figure 14, from site infrastructure to rooftop mechanical systems, and identify the key equipment categories that should stand to benefit from the structural transition to 800VDC. We organise the implications across six major dimensions.

Data Center Operators: DC operators are the primary demand aggregators of this transition. Their campuses house every layer of the architecture illustrated from MV switchgear intake through to server halls, and their ability to deliver high-density, power-ready data centers to hyperscaler tenants is the central commercial proposition. When AI rack densities escalate and 800VDC becomes the delivery standard in the future, operators with flexible grey-space design and power infrastructure upgrade capability should command premium lease rates and stronger tenant retention.

Power Equipment: The power infrastructure layer — comprising MV switchgear/RMU, transformers, backup generators, UPS systems, and PUD/RPP — is the most directly disrupted segment. Under 800VDC, centralised AC UPS and LV transformers are progressively retired, replaced by upstream MV rectifiers and ultimately SST. This represents both displacement risk for incumbent AC equipment vendors and a significant new market for DC-native power conversion equipment manufacturers.

Battery Energy Storage Systems: The facility-level BESS becomes structurally more important under 800VDC, replacing the centralised UPS as the primary power resilience mechanism. China's position in LFP battery manufacturing translates into a direct supply chain advantage, in our view. It is a meaningful revenue opportunity for battery system integrators serving the data center vertical.

IT Rack Power and Cooling: The GPU upgrade cycle is the primary demand driver for IT rack infrastructure including rack-level BBU. As successive GPU generations (Blackwell, Rubin, Kyber) deliver step-change improvements in compute density and performance, the associated rack system's power and cooling related components require corresponding upgrades. Vendors supplying high-density rack enclosures, power whips, and structured cooling solutions are incremental participants of this generational refresh cycle.

Cooling Solutions: Higher rack power densities enabled by 800VDC directly necessitate a parallel upgrade in thermal management. As per-rack power crosses the 100kW threshold, traditional air-cooling architectures become thermally insufficient. Liquid cooling solutions become standard deployment requirements rather than optional upgrades. Cooling solution providers with established data center verticals should benefit from this co-investment cycle alongside the power architecture transition.

Power Semiconductors: The shift to high-voltage DC conversion is a direct demand catalyst for wide-bandgap power semiconductors. SSTs, MV rectifiers, and high-efficiency DC/DC converters all rely on silicon carbide (SiC) and gallium nitride (GaN) devices to achieve the switching frequencies and efficiency levels required at 800VDC. This positions SiC/GaN device manufacturers as a key enabling layer of the entire 800VDC ecosystem.

## Figure 14. Data Center Architecture Layout and Key Asia Participants for 800VDC Transition

[Diagram with company names and tickers]

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

# Deep Dive into Key Asia Participants in 800VDC Transition

We address the key Asia participants in data center operation, power grid and plant equipment, battery energy storage system, IT rack power and cooling, data center cooling solutions, semis and passive components in this section.

## Data Center Operators

In the China data center market, we observe GDS and VNET. We see the transition as a positive demand catalyst in the near term, with manageable capex implications in the medium term, underpinned by the flexibility of their existing grey-space infrastructure and the competitive advantage of a mature domestic equipment supply chain.

AI demand remains the primary catalyst. We view that hyperscaler cluster rental pricing has stabilised and is showing early signs of reacceleration into 2H26, underpinned by sustained growth in LLM training and inference workloads, supporting accelerating EBITDA delivery for both GDS and VNET as committed pipelines convert to revenue in the coming years. The demand story remains intact as we outlined in our June's China Data Centers report.

800VDC commercial rollout in China is still in early stage. Domestic AI chip platforms (Huawei Ascend, domestic alternatives) have not yet been standardised on 800VDC power delivery, and rack power densities in China's AI compute ecosystem remain below the thresholds that are driving urgent 800VDC adoption. Thus, we believe there is minimal near-term capex pressure for GDS and VNET.

Capex impact likely manageable with a China supply chain advantage. Based on SemiAnalysis' phase analysis, the net capex differential of 800VDC versus traditional AC infrastructure is modest. Chinese IDC operators benefit from additional cost advantages: domestic LFP battery manufacturers provide BESS at globally competitive prices, while domestic power equipment vendors offer structural pricing advantages. We believe GDS and VNET should be able to execute any future 800VDC transition at a meaningful discount to global capex benchmarks.

Grey-space design provides built-in upgrade flexibility. Well-designed grey-space infrastructure is compatible with row-level sidecar retrofit without structural rebuild. When domestic tenant demand for 800VDC materialises, GDS and VNET could respond with targeted, low-disruption upgrades on a campus-by-campus basis, avoiding stranded asset risk.

In Australia, NextDC (NXT AX) and CDC—owned by Infratil (IFT AX)—are among the leading DC operators. Both companies develop and operate data centers across Australia and New Zealand, serving hyperscalers, cloud providers, and colocation customers. Recent contract wins have lifted contracted capacity to roughly 700MW for NextDC and 1GW for CDC, reflecting strong demand for AI and cloud infrastructure. Both operators continue to expand their development pipelines, and future facilities could incorporate 800V DC power architecture to improve sellable capacity and enhance energy efficiency.

Among Australian real estate names, Goodman Group (GMG AX) and Stockland (SGP AX) offer growing exposure to the DC theme through large development pipelines. Both are investing in DC projects, either directly or through partnerships, with Stockland developing assets alongside EdgeConneX in a 50/50 joint venture. For both companies, the key value driver is likely to be development profit rather than recurring operating income, given their broader and diversified property portfolios. Goodman is advancing a global 6.4GW power bank with more than 500MW of near-term projects, and data centers could become a major earnings contributor, rising from around 10% of revenue in FY26 to 50–60% by FY29–30E. Stockland currently has no meaningful earnings exposure but could see data centers contribute 2–3% of earnings between FY28 and FY30, with further upside possible from future developments. As these projects are built out, both developers could incorporate 800V DC power architecture to improve sellable capacity.

## Power Equipment

## Power Grid Equipment

The Asia power grid equipment sector is supported by strong global demand, particularly for high-voltage transformers and switchgear serving the robust capital expenditure cycle in AC data-center development.

## We highlight major companies by country:

Taiwan: Delta Electronics (2308 TW) has successfully transformed from a traditional power supply manufacturer into a comprehensive AI infrastructure provider, offering solutions that span the entire power delivery chain from grid to chip. Delta's portfolio covers AC/DC conversion, HVDC power systems, rack-level power infrastructure, battery backup solutions, and liquid cooling technologies. This end-to-end capability positions the company uniquely within the AI data center ecosystem, as few competitors can provide integrated solutions across both power and thermal management. As data center operators increasingly prioritize efficiency, reliability, and deployment speed, Delta's ability to deliver a complete power architecture solution should become an increasingly important competitive advantage.

AI-related infrastructure, including power systems, power management equipment, and thermal solutions—is estimated to contribute 25-30% of Delta's total revenue in 2026, making it the company's largest growth engine. We expect this contribution to increase further as hyperscalers and cloud service providers accelerate the buildout of next-generation AI clusters. While near-term deployments are likely to focus on ±400V HVDC architectures, we anticipate initial shipment volumes to begin ramping in 2H26. The more meaningful inflection point should occur from 2027 onward, when 800V DC systems begin broader commercialization alongside the scaling of Nvidia's Rubin platform and other next-generation AI infrastructure deployments.

As rack power density continues to increase, the industry's transition toward higher-voltage architecture appears less a technology upgrade and more a structural necessity. Given Delta's leadership across the power infrastructure stack and its expanding exposure to AI power systems, we view the company as one of the direct participants of the multi-year transition to 800V DC data center architectures.

Korea: All major transformer and switchgear players, such as Hyundai Electric (267260 KS), Hyosung Heavy (298040 KS) and LS Electric (010120 KS), are getting more orders related to 800VDC applications. Regarding SST development, Hyosung Heavy developed 22.7kV SST technology back in 2022; for 800V DC architecture and data center applications, the company is in pilot and demonstration stage with a US hyperscaler; this phase is expected to be completed within 2026E. For Hyundai Electric, it is in an R&D phase for SST and has a three-year target. It has secured LV transformer orders for datacenter projects this year, which will be delivered from 2029. For LS Electric, it has developed prototype that has been installed on an in-house test bed, though it is difficult to specify the schedule of commercial sales.

China: Sieyuan Electric (002028 CH) is a leading China high-voltage transformer and switchgear manufacturer; it has received orders for the former from data centers in the US. We believe China companies have competitive advantages in terms of lead time and production costs versus foreign peers. Sungrow (300274 CH) has launched new product for power distribution systems at AIDC; new orders are expected to be received in 2H26E and shipment would likely be made in 2027E. TGOOD (300001 CH) launched an AIDC integrated power supply product in June 2026, which can transform 110kV to 200-800V power supply for domestic customers, but it could also be an emerging LV transformer player in the future as it has a competitive cost structure with rising market share in non-US markets. Inovance (300124 CH) and Hongfa (600885 CH) have exposure to SST and power relay products.

Although a relatively late entrant to the space, Inovance has begun developing SST products targeting 800V DC AI data center applications. The company recently announced a collaboration with HCCCAP, a company incubated by Tsinghua University's carbon nanomaterials laboratory, to develop integrated power supply solutions for both AIDC and ESS. The partnership leverages HCCCAP's high-power pulse supercapacitor technology, which is designed to deliver power density of up to 100kW/kg. The solution is designed to provide millisecond-level response capabilities, enabling transient power support, peak-load buffering, and fail-safe backup function features that could become increasingly important as AIDC moves toward higher-voltage and higher-power-density architectures. That said, we believe commercialization remains at an early stage and therefore expect only limited revenue contribution from Inovance's 800V DC AIDC-related products in 2026-27. While we think the company is taking the right strategic steps to build exposure to next-generation power infrastructure, meaningful financial benefits are unlikely to materialize until broader adoption of 800V DC architectures gains traction over the longer term.

Hongfa is already a key supplier of relay products for AIDC infrastructure, with current exposure primarily through automatic transfer switches (ATS). As the industry transitions toward 800V DC power architectures, however, the company's addressable market should broaden significantly.

We expect Hongfa to supply a more comprehensive range of relay products across multiple power infrastructure components, including power distribution units (PDUs), battery backup units (BBUs), solid state transformers (SSTs), and other high-voltage power management systems. Such expansion would increase both content per deployment and the company's participation across the AI data center power chain.

According to management, revenue from 800V DC AI data center relay products could reach Rmb1.0-1.5bn in 2026. This estimate is based on several key assumptions: (1) relay content of approximately Rmb80,000-100,000 per MW of data center capacity, (2) global data center capacity reaching around 40GW, (3) 800V DC penetration rising to roughly 50%, and (4) Hongfa maintaining an approximately 50% market share in the relevant relay segment.

Commercialization could begin in earnest in 2H26, when Hongfa starts supplying 800V HVDC relay products to North American end customers through power infrastructure partners, such as Delta Electronics and other power management solution providers.

Reflecting the growing adoption of AI infrastructure and next-generation power architectures, we expect AIDC-related revenue to increase from approximately 4-5% of total sales in 2025 to 8-10% in 2026E, before rising further to the mid-teen percentage range in 2027E. As 800V DC deployments scale, Hongfa's expanding product portfolio and strong position in the relay market should enable it to capture an increasing share of the power infrastructure value chain.

Japan: Mitsubishi Electric (6503 T) plans to expand its high-voltage transformer production capacity in Japan, North America and Southeast Asia. The expansion will be primarily through upgrading existing facilities plus partial expansion, not large-scale, completely new built ones. Mitsubishi Electric's cumulative high-voltage transformer production capacity, from the base in 2024, would be +15% in 2025, +30% in 2026E, +45% in 2027E and +50% in 2028E by spending US\$193m globally.

India: We believe India's DC market is approaching a critical inflection point, with accelerating demand, supportive government policies, and large-scale infrastructure expansion all converging. Global technology leaders, including Microsoft, Amazon, and Meta, have collectively announced commitments of approximately US\$67.5 billion toward AI and data center infrastructure in India, highlighting the country's growing importance within the global digital economy. Based on publicly disclosed company roadmaps, announced, planned, and early-stage capacity additions now exceed 8GW, with a majority expected to come online by 2032.

We believe India's leading transformer and T&D OEMs are well positioned to benefit from this buildout. Hitachi Energy India (HITN NS), GE Vernova T&D India (GETD NS), CG Power and Industrial Solutions (CGPO NS), and Siemens Energy India (SIEE NS) have historically focused on domestic transmission projects and intra-group exports. However, all four companies are now actively expanding into the DC segment, representing a meaningful broadening of their addressable markets.

Hitachi Energy India estimates that its current addressable opportunity in AI-driven DC infrastructure accounts for roughly 10-15% of total DC capex. Through its "Grid-to-Rack" strategy, management aims to expand this exposure by an additional 15-20%, potentially increasing its addressable share to 25-35% of total AI DC infrastructure spend. To support this strategy, the company has announced a Rs10 billion capex program focused on localizing technologies tailored to India's AI DC requirements.

GE Vernova T&D India has already established an early track record in the DC market through supplies made to its parent company for US DC projects. This provides the company with valuable technical credentials and reference projects as it seeks to expand its presence in the domestic DC market.

CG Power and Industrial Solutions entered the DC export market in January 2025, securing a Rs9 billion order linked to a US DC project. We view this as an important validation of the company's DC product capabilities and a positive milestone as it positions itself for a larger role in India's rapidly expanding DC ecosystem.

Siemens Energy India is also expanding its DC product portfolio, with an increasing focus on solutions that support the growing power requirements of next-generation AI and hyperscale facilities.

With all four major India T&D OEMs actively broadening their DC offerings, we see DC-related TAM expansion as a key structural growth driver for the sector over the coming years. The combination of accelerating domestic capacity additions, rising AI infrastructure investment, and increasing localization of DC supply chains should create a meaningful long-term opportunity for India's power equipment leaders.

## Power Plant Equipment

On power plant equipment, we are constructive, as the order mix shifts increasingly towards non-coal generation. Representatives in this space include Yantai Jereh Oilfield Services (002353 SZ), which benefits from the rapid expansion of AIDC in the US, capitalizing on two critical market shortages — power supply and gas turbines. Unlike many peers, Jereh has proactively secured a diversified and reliable gas turbine supply base, sourcing from industry heavyweights including GE Vernova, Baker Hughes, Siemens, and Kawasaki. This strategic procurement advantage has enabled Jereh to leverage its robust gas turbine power generator inventory to win incremental AIDC orders, positioning it ahead of competitors constrained by the prevailing gas turbine supply deficit.

Beyond equipment supply, Jereh is deeply embedded in the DC supply chain, offering integrated "Gas Turbine + Energy Storage" bundles and operating as a full EPC turnkey provider and equipment manufacturer for power integrated services. In early May, Jereh further strengthened its supply chain resilience by establishing a joint venture with FTAI, converting retired CFM56 jet engines into gas turbine power generators — securing yet another stable and cost-effective turbine source while gaining a unique entry point into the high-growth data center power market.

Dongfang Electric (1072 HK) should also stand to benefit meaningfully from rising demand for gas turbines from its North American datacenter customer.

In the power generation/backup segment, Weichai Power (2338 HK) provides critical onsite/backup power solutions for data centers. Its gas engines support high-power requirements in hybrid setups alongside 800VDC systems, ESS, and grid connections—essential for reliability in AI infrastructure buildout. Its products also provide an alternative to backup systems.

Power generation for AI data centers should be a key growth driver for Weichai going forward. We expect power generation for AI data centers to contribute 5%/8%/12% of its total revenue and 21%/38%/43% of total earnings in 202E/27E/28E.

Management expects 2–3 MW of gas engines to be launched in mid-2026 with mass delivery in 3Q/4Q26, and 5 MW of gas engines to see prototype & validation by end-2026. As for profitability of gas engines (2-3 MW), management indicated their GPM is better than diesel engines GPM (35-40%), given higher ASP of US\$600k/MW versus diesel engine's Rmb1mn/MW. Gas engines production can share core engine line with diesel engines. The production line does not need large-scale reconstruction, with low conversion cost and strong flexible production capacity.

## Battery Energy Storage System

Battery energy storage systems (BESS) are quickly becoming essential infrastructure for AI factories. Unlike traditional data centers, AI factories are built to manufacture intelligence at scale. They run power-dense training and inference workloads, increasingly support agentic and reasoning models,
