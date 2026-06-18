# China and Japan Semiconductors
# Global Semis: SOCAMM2 - Innovative but niche, limited impact on memory interface chip TAM

Nvidia recently released their latest ARM-based server CPU called Vera, in which they used a new memory package format called SOCAMM2. As this new package uses much less memory interface chip content, some investors are concerned that this will reduce the TAM for Montage/Renesas. We believe the SOCAMM2 format will likely remain niche to Nvidia and thus only bring HSD to LT% impact to the memory interface chip TAM, reiterate Outperform on Montage and Renesas.

SOCAMM is a DRAM package customized for NVIDIA rather than a disruptive new standard. In Nvidia's Grace CPU design, they use LPDDR5x instead of DDR5 to reduce the power consumption. From Grace to Vera, the shift from soldered LPDDR5x to modular SOCAMM2 provides modularity flexibility and expands the total capacity/bandwidth. However, SOCAMM2 advantages are tightly aligned with NVIDIA's rack-level optimization, where maximizing performance-per-watt is paramount. Critically, these benefits come with trade-offs in capacity, bandwidth, and ecosystem maturity compared with MRDIMM, therefore we expect this solution will remain niche mainly to Nvidia, which we estimated to only have HSD to LT% in volume in the next few years.

Other high-end ARM-based CPU and x86 server CPU likely will remain using MRDIMM if they want to enjoy better capacity and bandwidth. NVIDIA's adoption reflects its full-stack control and greenfield design, enabling re-design at rack level for their specific target. In contrast, x86 and other ARM CPU vendors are already fully integrated with the DDR ecosystem, they will face prohibitive switching costs across memory controllers, platform design, and ecosystem requalification, alongside loss of backward compatibility. Meanwhile, MRDIMM continues to offer superior bandwidth (up to 1.6TB/s vs 1.2TB/s per CPU) and capacity (up to 16TB vs 1.5TB per CPU) over SOCAMM2, making it difficult for the high end x86 server CPU design to shift module selection.

Economic impact on interface chip suppliers is modest. SOCAMM2 introduces incremental chipset content versus soldered LPDDR, but value per module is only a few dollars, far below DDR5 MRDIMM's interface silicon content at 50-70 USD, thus indeed if SOCAMM2 became mainstream the memory interface chip TAM will reduce. Yet if the package design will remain niche to Nvidia, then the impact to TAM will be limited to the Nvidia CPU vol share (HSD to LT%). Small incremental MRDIMM adoption could easily offset that impact. Additionally, SOCAMM2 also use some memory interface chip so the shift from LPDDR5 to SOCAMM2 within Nvidia actually brings some upside to the memory interface TAM. Rambus holds first-mover advantage at this stage, but we expect Renesas and Montage to catch up quickly given the relatively low technical barriers in SOCAMM2 interface chips.

We maintain Outperform on Montage and Renesas, with conviction reinforced by limited substitution risk. SOCAMM2 does not alter the structural dominance of DDR in the broader server market. For Montage, concerns around displacement are overstated, and the durability of MRDIMM-led growth remains the core investment thesis underpinning our positive view.


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
6723.JP estimate is Adjusted EPS; 6723.JP valuation is Adjusted P/E (x);
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Montage Technology as Outperform and set a target price of CNY 220 for A shares, based on a 44x P/E multiple applied to 2BF (2027Q2–2028Q1) earnings. Given the company's high-growth profile and the anticipated new product launch cycle in 2027, we believe a 2BF P/E multiple provides a proper valuation anchor that captures the inflection in the company's earnings trajectory.

For H shares, we set a target price of HKD 320. The H share premium reflects that global investors favor Montage as a scarce China AI-exposed name without direct geopolitical risks, unlike many other Chinese semiconductor companies that face entity list restrictions or export control headwinds. At our target price, the implied P/E multiple on 2BF EPS for H shares is 56.4x.

Renesas: We rate Renesas Outperform, with PT = ¥4,200. With a market cap slightly above Montage's, Renesas appears significantly undervalued: its memory interface revenue, comparable in scale to Montage's, accounts for only single-digit % of total company revenue—the high-growth business is obscured by its broad product lines. We see re-rating opportunity for Renesas.

## DETAILS

## NVIDIA CPU DRAM TECH ROADMAP: FROM SOLDERED LPDDR TO MODULAR SOCAMM2

NVIDIA's server CPU platform is undergoing a key memory architecture transition. The current Grace CPU uses soldered LPDDR5X — high-bandwidth, power-efficient mobile DRAM physically bonded to the motherboard. While this delivers excellent performance-per-watt, it sacrifices field upgradeability: if memory fails or capacity needs change, the entire board must be replaced.

SOCAMM2 (Small Outline Compression Attached Memory Module 2) solves this by packaging LPDDR5X into a detachable, standardized module with a compression connector. Originally a proprietary NVIDIA design (SOCAMM1), the standard has been adopted by JEDEC under specification JESD328, with Samsung, Micron, and SK Hynix all developing compliant modules.

The transition from soldered LPDDR to SOCAMM2 enables multi-vendor memory sourcing and field serviceability for NVIDIA's server platforms for the first time, a critical requirement for hyperscaler adoption.

Micron has already demonstrated SOCAMM2 modules scaling from 128 GB to 256 GB per module using 32Gb LPDDR5X dies on 1 $\gamma$ process technology.

EXHIBIT 1: In the Grace generation, LPDDR5 is soldered directly onto the board, making it non-replaceable and preventing any changes to the memory configuration

[[KC_IMAGE_001]]


Source: NVIDIA reports, Bernstein analysis

EXHIBIT 2: In the Vera generation, SOCAMM2 uses modular LPDDR5x connected to the board via a compression/ pressure connector, enabling a replaceable memory format

[[KC_IMAGE_002]]


Source: NVIDIA reports, Bernstein analysis

EXHIBIT 3: Diagram of NVIDIA Vera CPU and SOCAMM2 layout

[[KC_IMAGE_003]]


Source: NVIDIA website, Bernstein analysis

## NVIDIA HALVES INITIAL VERA RUBIN SOCAMM2 CAPACITY

During the recent ComputeX, NVIDIA and SK Hynix unveiled that Vera Rubin NVL72 will ship with 96GB SOCAMM2 modules instead of originally specified 192GB, reducing rack-level CPU aggregated memory from \~55TB to \~28TB.

This spec adjustment reflects supply-side constraints in a nascent SOCAMM2 ecosystem, not weakening demand. LPDDR5x supply remains extremely tight. As an emerging niche product, SOCAMM2 has limited capacity in both memory manufacturers and interface chips vendor. By shipping lower-density modules, NVIDIA can deploy more racks under the same DRAM supply, accelerating the time-to-market.

Shipping 96GB modules delivers meaningful rack-level cost savings, lowering the system price from \$7.6Mn to \$6.8Mn per rack (estimated by SemiAnalysis). Clients requiring the full 1.5TB spec can upgrade to larger-capacity modules, when supply matures and pricing normalizes.

The move validates SOCAMM2's modularity advantage over Grace's soldered LPDDR. Had Vera used soldered memory, NVIDIA would have been forced to either delay shipments or permanently lock in a lower spec. SOCAMM2's detachable design explicitly enables the “install now, upgrade later” flexibility.

EXHIBIT 4: Leading memory manufacturers all begin to provide SOCAMM2 modules starting in 2026


Source: companies reports, Bernstein analysis

## TECHNOLOGY COMPARISON: DDR5 RDIMM/MRDIMM VS. LPDDR5X SOCAMM2

The three server memory architectures diverge meaningfully across the bandwidth, capacity, power, cost and ecosystem maturity. In summary, SOCAMM2 excels in power efficiency and compact design, closely aligning with NVIDIA's overarching strategy of rack-level vertical integration and maximizing tokens per second per watt. By comparison, DDR DIMMs maintain advantage in bandwidth and capacity, backed by a more established and mature ecosystem.

EXHIBIT 5: Spec comparison across DDR5 RDIMM, MRDIMM, and SOCAMM2


The pricing reflects the contract rates for 2Q26 as updated by TrendForce in May 2026. As MRDIMM and SOCAMM2 are still in the early sampling stage, their ASPs represent sample pricing, which is expected to decline to normalized levels as production volume increases.

Source: companies reports, Bernstein analysis

EXHIBIT 6: Architecture comparison between SOCAMM2 and DDR5 RDIMM

[[KC_IMAGE_004]]


- \~133mm x \~31mm x \~2.5mm
• 288 pins on edge connector
• Vertical, insertion socket


[[KC_IMAGE_005]]


Source: AMD website, Bernstein analysis

- \~86mm x \~14mm x \~1mm
- 694 pins on back
• Horizontal, screw mounted

EXHIBIT 7: On x86 CPUs, DDR channels accommodate vertically inserted DIMM modules

[[KC_IMAGE_006]]


[[KC_IMAGE_007]]


Source: AMD website, Bernstein analysis

EXHIBIT 8: In contrast, SOCAMM2 employs a horizontally compressed design, enabling a more space-efficient layout. Even the last generation LPCAMM2 saves 64% of space vs. DIMM module

[[KC_IMAGE_008]]


Source: Micron, Bernstein analysis

On aggregate bandwidth, SOCAMM2 on NVIDIA Vera (\~1,229 GB/s) narrows the gap significantly versus 16-channel DDR5 RDIMM (\~819 GB/s), though it trails MRDIMM (\~1,638 GB/s). However, SOCAMM2's power advantage is substantial: at 1.05V with \~30% lower total energy consumption versus RDIMM, SOCAMM2 delivers superior bandwidth-per-watt — the metric that matters most in GPU-centric AI servers where CPU memory power competes with GPU compute for the system power budget.

The capacity trade-off is notable. SOCAMM2's total capacity of 1.5 TB (8 × 192 GB) is adequate for NVIDIA's AI server use case where HBM on the GPU handles the primary data set. However, it falls well short of x86 platforms that can deploy 8–16 TB+ via high-density RDIMM/MRDIMM configurations — a critical requirement for memory-intensive enterprise and HPC workloads.

On interface chip content, SOCAMM2 carries significantly lower value per module (\~\$3–5 for SPD and voltage regulators) compared to MRDIMM's \~\$70+ chipset. This differential is the core economic consideration for memory interface chip suppliers.

## PLATFORM ADOPTION: WHY WE BELIEVE THAT SOCAMM2 WILL REMAIN NVIDIA-SPECIFIC

We anticipate SOCAMM2 to remain largely NVIDIA-specific within the foreseeable future, rather than evolving into a broader industry standard across ARM-based and x86 server CPU ecosystems. The adoption of SOCAMM2 by NVIDIA should be understood less as a DRAM technology inflection point, but more a system-level architectural optimization tightly coupled to NVIDIA's AI platform strategy. This divergence fundamental differences in switching costs, architectural priorities, and ecosystem dependencies between NVIDIA's greenfield ARM platform and the deeply entrenched server ecosystem of mainstream suppliers.

NVIDIA's full-stack co-optimization justifies the architectural bet. NVIDIA is unique among server CPU vendors in its ability and willingness to redesign the entire compute stack from silicon on rack. The Vera CPU is not a standalone processor competing for socket share in the open server market; it is a purpose-built component within an integrated system spanning GPU, CPU, NVLink interconnect, thermal management, and rack-level power delivery. In this context, SOCAMM2 is not merely a memory module choice, but an architectural enabler within the entire NVIDIA AI rack. By adopting SOCAMM2, NVIDIA can optimize memory power consumption at the rack level, freeing thermal and electrical headroom for GPU compute. This system-level co-optimization is viable only when a single vendor controls the full stack, and it is precisely what differentiates NVIDIA's approach from the rest of server ecosystem.

Switching costs are asymmetric across CPU vendors. NVIDIA faces near-zero switching costs because it is designing the Vera platform from scratch, with no legacy DDR memory controller IP, no existing DIMM slot mechanical standards, and no backward-compatibility obligations to prior server generations. It can architect the entire memory subsystem, including controller, board layout, connector placement, and firmware, around SOCAMM2 from inception. In contrast, any CPU vendor migrating away from DDR would bear the full burden of redesigning memory controllers, re-qualifying board layouts and connectors, revalidating the supply chain, and forfeiting backward compatibility, a multi-year and multi-hundred-million-dollar undertaking with uncertain returns.

Other ARM-based CPU vendors lack the volume to justify a proprietary DRAM ecosystem. NVIDIA's shipment volumes for AI server CPUs, which are underpinned by GB200/300 and Vera Rubin platforms deployed at hyperscaler, provide the unit economics necessary to sustain a distinct module standard and a complete new architecture. Other ARM-based server CPU vendors, such as AWS Graviton and Ampere Computing, operate at materially lower volumes and serve broader customer bases that depend on standardized DDR infrastructure. For these vendors, adopting SOCAMM2 would mean not only migrating to a low-volume module standard, but also sourcing new controller IP and asking OEMs to redesign the rack architecture. Simultaneously, this migration will fragmente their own platform compatibility with enterprise OEMs and cloud operators. The scale economics simply do not support this drastic switch. These vendors are more likely to pursue incremental bandwidth improvements within the DDR DIMM paradigm, particularly DDR5 MRDIMM, which offers substantial performance uplift without ecosystem disruption.

x86 platforms have no incentive to pivot to SOCAMM2. Intel and AMD face the highest switching costs of any server CPU vendor, having co-evolved with the DDR DIMM ecosystem over five generations and two decades. Beyond the prohibitive engineering costs of migrating memory controllers and platform designs, the performance argument itself does not favor SOCAMM2. MRDIMM delivers superior performance in bandwidth and capacity over SOCAMM2, through a more mature and multi-vendor supply chain. MRDIMM reserves standards that many server clients have been familiar with, without any of the switching costs associated with an entirely new memory architecture. We see no plausible scenario in which x86 CPU platforms switch to SOCAMM2.

EXHIBIT 9: We project that NVIDIA CPU shipment volume will account for only MSD to low teens in total server CPU shipment

[[KC_IMAGE_009]]

Source: Mercury, Bernstein analysis and estimates

## SOCAMM2'S IMPACTS ON MEMORY INTERFACE CHIP SUPPLIERS

## A) SOCAMM2 EXPANDS TAM VS. SOLDERED LPDDR ON GRACE

Compared to NVIDIA's Grace CPU, where LPDDR5X was soldered directly to the board with zero module chipset content, the transition to detachable SOCAMM2 modules on Vera creates a new — if modest — chipset TAM. Each SOCAMM2 module requires at minimum an SPD chip and a PMIC for power management, and potentially voltage regulators and temperature sensors. These interface chips represent incremental revenue that previously did not exist on NVIDIA platforms.

## B) FAR LOWER VALUE CONTENT PER MODULE VS. DDR5 MRDIMM

SOCAMM2's chipset content (SPD + PMIC, estimated at a few dollars per module) pales in comparison to DDR5 MRDIMM's "1+10" architecture totaling \~\$50-70+ in interface silicon per module. MRDIMM will remain the mainstream high-value growth driver for interface chip suppliers. The global memory interface chip TAM will be driven predominantly by MRDIMM adoption on x86 platforms. SOCAMM2's chipset contribution to this TAM will remain a small fraction.

## C) DIFFERENTIATED IMPACT ACROSS THE THREE MAJOR SUPPLIERS

Rambus — Best positioned in SOCAMM2. Rambus has already launched a dedicated SOCAMM2 server module chipset and benefits from IP licensing royalties on new memory controller designs that must be made compatible with SOCAMM2. Management has characterized SOCAMM2 as a small near-term revenue contributor, but the strategic positioning ensures Rambus captures value across both DDR and LPDDR ecosystems.

Renesas — Natural adjacency. Renesas can leverage its deep heritage in power semiconductors and analog/mixed-signal design, particularly its industry-leading position in DIMM PMICs (estimated \~70% PMIC market share), to expand into SOCAMM2 chipsets. The PMIC and voltage regulator content on SOCAMM2 modules is a direct extension of Renesas's existing capabilities. The technical barriers to entry are lower than for DDR5 interface chips.

Montage — Most exposed but diversifying. Montage's core memory interface chips business is structurally tied to x86 DDR platforms. Each NVIDIA CPU socket adopting SOCAMM2 instead of DDR is a lost socket for Montage's high-value MRCD/MDB products. However, recent job postings for power semiconductor engineers suggest Montage may be building in-house SOCAMM2 chipset capabilities (particularly PMIC). This would represent a logical diversification, though Montage would enter a market where Rambus has first-mover advantage and where dollar content per module is an order of magnitude lower than MRDIMM.

The key mitigant: SOCAMM2 is confined to NVIDIA's ARM platforms. The x86 server CPU installed base remains committed to DDR5 RDIMM and the increasingly important MRDIMM upgrade cycle.

EXHIBIT 10: First to market: Rambus delivers SOCAMM2-compatible interface solution at current stage

[[KC_IMAGE_010]]


Source: company website, Bernstein analysis
