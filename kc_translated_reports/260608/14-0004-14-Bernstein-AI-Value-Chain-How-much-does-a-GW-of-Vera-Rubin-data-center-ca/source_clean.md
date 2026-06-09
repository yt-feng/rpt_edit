# U.S. Semiconductors
# AI Value Chain: How much does a GW of Vera Rubin data center capacity actually cost?

Based on a series of conversations with industry experts as well as third-party data on physical infrastructure, we update our estimates of rack-level AI data center economics for the Vera Rubin NVL 72 architecture. This note includes our analysis and key takeaways. Excel backup is available on request.

We estimate that a typical VR / NVL72 rack costs \~\$9.1M per rack. This estimate is notably higher than the \~\$8M figure reported in the media, which appears to be based on stale memory prices. We believe the disconnect is largely coming from HBM - we land at a similar figure if we use HBM 4 price of \~\$16.6 / GB, but we expect the price to increase to \$53 / GB in 2027, when Vera Rubin will be shipping in volume, and we further believe Nvidia will pass these costs on to end customers. Overall, we believe memory / storage costs will be close to \~\$3.2M, higher than the \$2M implied by historical prices. Investors should also modify estimates as memory prices change.

Even with increased memory costs, the GPU remains the largest contributor to cost.

We believe \~\$4M in cost is coming from the GPU (ex. HBM). Costs are less transparent outside of compute and memory / storage, but we believe that networking comprises \$1.2M of the remaining \~\$2M, led by NVLink and SpectrumX switches. Cooling and power delivery costs were also significant at \~\$150k each.

We estimate all-in AI data center capex of \~\$47B per GW. Given that the Vera Rubin NVL 72 rack is rated for 220 kW, our estimate that the rack consumes \~80% of data center power, and coupled with \$15B in physical infrastructure costs per GW, this points to all-in AI data center capex of \~\$47B per GW.

Notably, this appears to represent a continued acceleration in FP8 performance per dollar. The Vera Rubin NVL72 rack performs at 2,520 PLOPS, up from 720 for Blackwell, implying meaningful acceleration in compute capacity, both on a per GW and a per \$ basis

Given the shorter depreciation lifespan of IT Hardware such as servers and networking compared to mechanical & electrical equipment or land & buildings, and given that operating costs are relatively low, the true economic costs are likely even more heavily weighted towards servers and networking compared to what cash capex would imply. Even at an elevated cost of \$0.15/kWH, it costs \~\$1.3B in electricity to run a GW of data center capacity for a year. Personnel costs are also negligible, leaving \~\$7.2B in annual depreciation as the dominant operating cost.

Looking forward, we expect cost per GW to continue to increase, pointing to increases in power demand that lag the growth in hyperscalar capex. We also see major increases in DRAM and power content and believe substrate content is also increasing.

Available compute continues to accelerate, which could help to unlock further AI adoption.


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
3037.TT, 2308.TT, 2382.TT, 2360.TT estimate is Reported EPS; NVDA, DLR, EQIX valuation is Adjusted P/E (x); CRWV valuation is EV/EBITDA (x); NVDA base year is 2026;
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

NVDA (OP, US\$315.00): We rate Nvidia Outperform, PT=US\$315.00.

Unimicron (OP, NT\$990.00): We rate Unimicron Outperform, PT=NT\$990.00.

Delta (OP, NT\$2,620.00): We rate Delta Outperform, PT=NT\$2,620.00.

Quanta (UP, NT\$250.00): We rate Quanta Underperform, PT=NT\$250.00.

Chroma (OP, NT\$1,660.00): We rate Chroma Outperform, PT=NT\$1,660.00.

Digital Realty (OP, \$232): We rate DLR Outperform, PT=\$232.

Equinix (OP, \$1,222): We rate Equinix Outperform, PT=\$1,222.

Coreweave (UP, \$67): We rate Coreweave Underperform, PT=\$67.

# DETAILS

Based on a series of conversations with industry experts, supply chain checks, and third party data on out-of-rack costs of land and physical infrastructure, we update our estimates of GB200/NVL72 AI data center rack-level economics for the Vera Rubin NVL72 architecture. This note includes our analysis and key takeaways. See AI Value Chain: How much does a GW of data center capacity actually cost, and what goes into it? for our original view on the Blackwell cycle, and our Black Book for our updated perspective: Artificial Intelligence: The AI Infrastructure Value Chain

# We believe the Vera Rubin NVL 72 to be an \~\$9.1M rack. This estimate is notably higher than the \~\$8M figure reported in the media, which we believe to be based on stale memory prices. For our breakdown of rack costs, see:

Exhibit 1. We construct a bottom-up estimate of Vera Rubin NVL 72 rack costs, and land at \$9.1M. Notably, this is notably higher than the \$8M figure which has been widely reported in the media. We believe the disconnect is largely coming from memory prices: if we use the historical HBM 4 price of \~\$16.6 / GB, we land at a similar figure. However, we expect HBM 4 prices to increase to \$53/GB by 2027, when Vera Rubin will be shipping in volume. Moreover, we believe that Nvidia likely has some form of dynamic pricing mechanism, and will pass on this increase to customers instead of absorbing it as a hit to margin. As a result, we believe memory / storage costs will be close to \~\$3.2M, significantly higher than the \$2M implied by historical prices. This also serves as a reminder that our own cost breakdown will rapidly become stale, and investors using these estimates will need to frequently reflect volatility in memory prices in order for numbers to be accurate. That said, even with the increase in memory price, the GPU (ex. HBM) remains the largest part of cost, accounting for \~\$4M. Costs are less transparent outside of compute and memory / storage, but we believe that networking comprises \$1.2M of the remaining \~\$2M, while cooling and power delivery costs are also significant.

\- GPU / CPU. Our views are consistent with widespread reporting that the Rubin GPUs are selling for \$55k per GPU $^{1}$ . At 72 GPUs per rack, this implies \$3.96M in GPU cost alone, nearly half of the rack cost. Similarly, the Vera CPU is reportedly selling for \$5k per CPU, pointing to \$180k in total cost for 36 CPUs per rack.

\- Memory and storage. We expect memory and storage costs to land at \$3.2M per rack (about 35% of rack costs), significantly above the \~\$2M implied by using historical prices. We believe this is the main driver of the differentiation between our estimate of \$9.1M in rack costs, vs. media reports that this is a \~\$8M rack. This also serves as reminder that, given continued volatility in DRAM and NAND prices, our own estimates will likely become stale relatively quickly, and that investors following the space should frequently reflect fluctuations in DRAM and NAND prices in order to maintain accurate forecasts.

\- High-Bandwidth Memory (HBM). Nvidia's published spec (link) lists 20.7 TB of HBM 4 (Exhibit 2). We currently model HBM 4 is priced at \$16.63 / GB $^{2}$ (for more details on HBM, see: Global Memory: Price increase more than expected in 2QCY26). However, we expect HBM 4 prices to increase to \$48 / GB in 2027, when Vera Rubin will be shipping in volume. Moreover, Nvidia may have a dynamic pricing mechanism. As a result, instead of absorbing the cost increase as a hit to margin, Nvidia should be able to pass on the increase to end customers, and likely even collect a \~10% markup, pointing to \~\$53/GB for HBM in the BOM paid by customers. Reflecting this price increase increases the HBM contribution from \$344k to \$1.1M, which we believe to be the biggest driver in our differentiation from the widely reported \~\$8M rack cost figure.

\- CPU DRAM. The VR spec includes 54 TB in LPDDR5X CPU memory. While the 2Q26 contract price for mobile LP5X is \$11.43 / GB, our channel checks suggest that Nvidia's SOCAMM architecture includes a 30% premium over mobile DRAM prices. As a result, we price DRAM at \$14.85 / GB, and land at \$802k per rack in CPU DRAM content. We also expect LPDDR price to rise further in 2H26, but likely peak and the fall some time in 2027 or 2028. This presents a cost uncertainty to Nvidia. The possible shortage of LPDDR may also limit the shipment of VR, & standalone Vera CPU. Accordingly, Nvidia may choose to install a lower default DRAM capacity but allow customers install more after VR or standalone Vera CPU is shipped so that customers can balance their need against the latest memory price to determine the optimal DRAM capacity for them. Alternately, Nvidia may choose to price VR & standalone Vera dynamically based on the latest DRAM price reflect uncertainties.

\- Direct-attached storage. Direct-attached storage is somewhat less transparent, given that storage is excluded from Nvidia's specs and there is likely room for configuration variance. However, for GB200 NVL72, we anchor to Super Micro's data sheet (link), which lists 8 E1.S drives for each of the 18 compute trays, or a total of 144 slots. Assuming each of those slots are 15.36 TB (in line with the Solidigm D7-PS1010), and each tray has another 2 TB M.2 boot drive, that points to 2.2 PB of total NAND content for Blackwell. For Vera Rubin, we assume constant E1.S content and add 16.9 GB / GPU in ICMS content, for 3.5 PB in total NAND. Assuming TLC NAND prices of \$0.37 / GB (which assumes a 30% premium over current client prices, consistent with the premium paid for DRAM), we land at \$1.3M per rack in storage content.

\- What about HDDs? Our analysis is focused on server racks and thus server direct-attached storage. Given the dramatic increase in NAND prices, direct-attached storage is now a far more material portion of costs than during our analysis last year, when NAND was 75% cheaper and NAND content was also lower. Furthermore, NAND availability has also been a growing concern (albeit somewhat insulated by AI buyers' willingness to pay a premium and outbid the smartphone and PC industries for limited supply). However, data center operators appear hesitate to substitute NAND for HDDs for direct-attached storage, as the drop-off in performance remains a concern, especially since using lower-performance storage can increase the burden on memory, when DRAM and HBM are also scarce. Moreover, because HDDs are physically larger and consume more power compared to NAND, incorporating HDDs within-rack (as opposed to on external storage arrays) could require significant redesign, which may not be possible for some of the tier 2 CSPs. With that said, less latency-sensitive cold storage use cases (such as the later stages of SSN attention networks) are often stored on external storage arrays, which actually account for the majority of storage capacity. In external storage, we have seen greater adoption of HDDs, consistent with the industry average of 20% NAND and 80% HDDs in terms of GB storage capacity. For a primer on the HDD industry, see: Global Hard Disk Drives: It's HAMR time! A primer on the HDD industry and why STX is poised to reap outsized rewards.


- Networking. There is likely more variance in networking architectures (and thus costs), especially given replacing the SpectrumX top of rack switch with a third party scale-out switch appears to be one of the more common deviations from Nvidia's reference architecture among hyperscale customers. However, based on our conversations with industry participants, we see \~13% of rack costs in networking costs as typical, including 8% for scale-up and 5% in scale-out. Within that, we estimate \~\$250k for NVlink switches across 18 chips (9 switch trays and 2 NVSwitch chips each), \~\$240k in cabling, and \~\$380k in backplanes and other scale-up content. Similarly, we estimate the SpectrumX Switch at \~\$200k, and believe it to be about half of the total cost of the scale-out fabric.
- Cooling, power delivery. We estimate power content as ramping from \~\$50k per rack for GB200 to \~\$150k for VR (Exhibit 4 - for more details, see: Delta Electronics 1Q26: adding capacity for long-term AI demand. PT raise to NT\$2,620). Based on conversations with industry contacts, we estimate cooling at \~\$160k (2% of total rack cost).
- Others. Our conviction levels are lower for some of the components which are a smaller part of the BOM, as they are more likely to be excluded from the specs and harder to size top-down. Notably, while multilayer ceramic capacitors (MLCCs) have become a hotly debated topic, we were unable to form a high conviction view. However, based on industry conversations, our best guess is that the rack chassis costs \~\$100k, and there is perhaps another \$100k in other rack content, landing at a \$9.1M BOM.

Given that the Vera Rubin NVL 72 rack is rated for 220 kW, and that we believe the rack consumes \~80% of data center power, that points to 3.6k racks per GW, or \$32B in rack cost per GW. Coupled with \$15B in physical infrastructure costs per GW, this points to all-in AI data center capex of \~\$47B per GW - Exhibit 5.

\- \~\$9.1M in cost per rack translates to \$32B in rack cost per GW. We observe that, without redundancy, the VR rack is designed for 220 kW per rack, up from 130 kW for GB200. We maintain our estimate from GB200 that the rack is 78% of the data center power load $^{3}$ , implying 281 kW in total data center power consumption per rack, or that a GW of power can support 3,557 racks. This in turn implies 32.3B in rack cost per GW.

\- \$47B per GW in total capex. Based on our conversations with data center operators, we see \$12-15B / GW in physical infrastructure costs on new builds for top-tier facilities. We roll over our prior estimate of \$15B / GW for Blackwell, and get to an all-in AI data center capex of \$47B per GW.

Notably, this appears to represent a continued acceleration in FP8 performance per dollar. At Nvidia's quoted specs, the Vera Rubin NVL72 rack performs at 2,520 PLOPS, up from 720 for Blackwell. This implies a pretty meaningful acceleration in compute capacity, both on a per GW and a per \$ basis (Exhibit 6). With that said, our general view is that in a heavily compute constrained environment, it continues to make sense to run GPUs for as long as possible, even if older GPUs are offering worse price/performance than newer ones. As a result, data center operators are likely to prioritize new data center builds to house new GPUs as much as possible. However, if data center operators are unable to build the capacity to house newer chips due to power or physical infrastructure constraints, they may need to think seriously about unplugging older GPUs in order to bring new GPUs online. For more details, see: AI Value Chain: Can you really run a GPU for 6 years?

Given the shorter depreciation lifespan of IT Hardware such as servers and networking compared to mechanical & electrical equipment or land & buildings, and given that operating costs are relatively low, the true economic costs are likely even more heavily weighted towards servers and networking compared to what cash capex would imply.

Even at an elevated cost of \$0.15/kWH, it costs \~\$1.3B in electricity to run a GW of data center capacity for a year. Personnel costs are also negligible, with even the largest data centers reportedly operating with 8-10 people costing \$30-80k per year each. By contrast, even on a 6 year depreciation cycle, capex costs \~\$7.9B in annual depreciation. Given the relatively high cost of capex relative to ongoing operating costs, and the fact that hardware has a shorter depreciation lifespan than physical infrastructure (Exhibit 7), the true TCO economics may actually be even more heavily weighted towards servers, storage and networking compared to what cash expenditure would imply.

Looking forward, we expect cost per GW to continue to increase, pointing to increases in power demand that lag the growth in hyperscalar capex. We also see major increases in DRAM and power content and believe substrate content is also increasing.

- On our numbers, cost per GW is increasing 9% in the Rubin cycle. While this represents an acceleration from 8% for Blackwell, consensus expects hyperscalar and neocloud capex to decelerate to 10% in 2027E (Exhibit 8), implying that flattish power capacity adds will be sufficient to support continued growth. While this appears disappointing compared to expectations for power capacity additions to continue to accelerate, we suspect that the disconnect may actually be because there could still be upside to consensus expectations for hyperscale capex. With that said, industry contacts also appear less worried about power constraints compared to this time last year, as solutions to circumvent power constraints appear to be working. For more details on the data center project pipeline, see: US Industrials & Tech: The Data Center Project Pipeline - Capacity, Construction & Cancellations (April '26)
- DRAM and power content increases stand out; we believe substrate content is also increasing. On a cycle-to-cycle basis, we observe that power content has significantly outpaced the increase in total rack value, with power content growing from 1.0% of the rack to 1.6%, amid greater power loads and the early stages of 800VDC adoption (Exhibit 4, again). We continue to see Delta as one of the main beneficiaries of increasing power content, despite increasing efforts from Vertiv to capture share in the space. Likewise, the CPU DRAM spec has increased 320% in TB terms, which is a dramatic increase in content even before considering the recent increases in DRAM price; notably, this significantly outpaces the \~50% increase in NAND and HBM content. We have also heard some feedback that usage of CXL memory for KV caching is increasing, which could drive further DRAM content increases. While this appears to still be exploratory and we are unable to size the potential impact, this further supports the view that DRAM could benefit disproportionately, if supply allows. While PCB / substrate content is harder to dimension, given that they appear upstream from several different components, we continue to expect content growth, especially for ABF substrates, and are positive on Ibiden and Unimicron (for more details, see: ABF Substrate: Renaissance of CPU drives ABF shortage; Lifting Ibiden PT to ¥23,900).

Available compute continuing to accelerate. End user adoption appears to have accelerated in 2026, driving dramatic growth among AI labs, with Anthropic reporting run-rate revenue increasing from \$9B at the end of 2025 to \$47B in May (link). This has come despite compute constraints that have caused the company to forego customers and revenues rather than

overextend on compute (link). With the Rubin cycle driving a further step-up in available compute, we believe that this could help to unlock further AI adoption.

For reference: Exhibit 9 includes a map of AI server supply chain. Exhibit 10 includes companies in the AI server hardware supply chain. Detailed discussions of competition landscape in each sub-segment can be found in the following notes: server ODM/OEMs, power components, liquid cooling, copper connectors and optical transceivers.

EXHIBIT 1: Nvidia Datacenter GPU Rack Capex Breakdown by ARchitecture


Since Hopper reference architecture is at the server level instead of the rack level, there is more variance in rack architectures. Source: Expert Conversations, Company Disclosures, Literature Search, Channel Checks, Bernstein estimates and analysis

EXHIBIT 2: Nvidia Published and Estimated Specs


Published figures in blue, Bernstein estimates in red
Source: Nvidia Website, Bernstein estimates and analysis

EXHIBIT 3: NAND prices stabilized in May, but volatility remains elevated compared to historical trends
NAND Wafer (3D TLC 512Gb) Spot & Contract Price

[[KC_IMAGE_001]]

Source: DRAMeXchange & Bernstein analysis

EXHIBIT 4: AI server power component TAM
Power component TAM for Nvidia server


Power TAM in AIDC (US\$M)


Source: Bernstein estimates and analysis

EXHIBIT 5: Datacenter Infrastructure Capex Breakdown


Source: Omdia, Expert Conversations, Channel Checks, Company Disclosures, Literature Search, Bernstein estimates and analysis

EXHIBIT 6: Rack-level Price Performance


Source: Nvidia specs, Bernstein estimates and analysis

EXHIBIT 7: Hyperscalar Disclosures on Depreciation Lifespans for Relevant Categories


Source: Company Filings, Bernstein analysis

EXHIBIT 8: Consensus expects hyperscalers to grow their total capex by 69% YoY in 2026 and another 13% in 2027, which saw a notable uplift vs. the numbers in Nov 2025

[[KC_IMAGE_002]]


Source: Company reports, Bloomberg (estimates) and Bernstein analysis

EXHIBIT 9: AI Server Supply Chain

[[KC_IMAGE_003]]


Note: Bernstein covers Quanta, Delta Electronics, Unimicron, Chroma ATE, TSMC, Samsung, SK hynix, Micron, NVIDIA, AMD, Broadcom, DISCO, Ibiden, BE Semi, but not the rest.
Source: Nvidia, SK hynix, Bernstein analysis

EXHIBIT 10: Summary of AI supply chain companies


Source: Bernstein covers Dell, SuperMicro, HPE, Quanta, Luxshare, Delta, but not the rest
