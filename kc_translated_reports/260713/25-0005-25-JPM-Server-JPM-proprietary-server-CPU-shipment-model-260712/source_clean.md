# JPM
## Server

In this note, we introduce a JPM proprietary server CPU shipment model and forecast total server CPU shipments to grow from 26mn units in 2025 to 68mn by 2028 (38% CAGR). We segment server CPU demand into three buckets: (1) AI headnode CPUs, (2) agentic-AI server CPUs, and (3) general-purpose server CPUs. With AI accelerator shipments projected to show a \~50% CAGR over FY25–28 based on our CoWoS estimates by the semi team (link), we see a step-function increase in AI headnode CPU demand, reinforced by a rising CPU-to-accelerator attachment trend. While general-purpose server CPUs should continue to show a steady \~5% CAGR, agentic-AI CPUs are the breakout growth vector, with 155% CAGR expected over 2025–28. Net-net, we believe overall general server shipments can sustain 20%+ growth in the coming years. This super-cycle is positive for TSMC, Unimicron, ASPEED, Lotes, Wiwynn, Tripod, GUC, ASE, and memory vendors, such as SK Hynix and Samsung Electronics, across Asia Technology.

\- Server CPU landscape reshaped by AI-led demand. We forecast AI accelerator shipments to rise from 7.6mn units in 2024 to 32.5mn by 2028, with increasing headnode CPU attach rates due to more complex AI accelerators. The accelerator-to-CPU ratio is also compressing—from \~4:1 in legacy HGX servers to \~2:1 in NVL72 compute trays, and potentially \~1:1 in next-generation TPU designs. ARM-based CPUs are taking share, driven by Nvidia's Vera and Google's Axion, and we estimate ARM could represent \~90% of AI headnode CPU demand by 2028. We also expect ARM to gain share in agentic-AI servers, as hyperscalers lean into in-house CPU roadmaps for emerging workloads. As a result, we model ARM-based CPUs reaching \~43% of the blended server CPU market by 2028 (up from \~22% in 2025). That said, we still expect the x86 CPU market to see an accelerated 25% CAGR over the period (vs. flattish to LSD CAGR in the prior cycle).

\- New AI inference orchestration drives agentic-AI server demand. As AI workloads shift from training towards inference, we expect hyperscalers to deploy more general-purpose servers around accelerators to improve Total Cost of Ownership (TCO). The incremental demand shows up primarily in external storage servers (e.g., KV cache) and compute servers that handle query orchestration around GPUs. While there is no fixed accelerator-to-CPU server ratio, our back-of-the-envelope analysis suggests \~0.5x (1 CPU for two accelerators) this year, with the ratio rising over time as accelerator complexity increases. This will become the key incremental driver of general server demand (>50% of the general server CPU market by 2028 vs. <10% last year).

\- Stocks leveraged to the super server CPU upcycle. There is a high correlation between server CPU, BMC, substrate, and socket demand. We expect ASPEED, Lotes, and Unimicron to be the key beneficiaries of this super server CPU cycle, driven by strong unit demand, continued content upgrades, and potential product price hikes. AMD's continued m/s gain in x86 server CPUs also bodes well for TSMC and ASE as the key foundry/OSAT vendor. DRAM vendors could benefit from the increasing DIMM/SOCAMM demand. In the downstream, we believe the server PCB makers (e.g. Tripod) and general server ODMs (e.g. Wiwynn, Inventec) could also benefit from the strong server demand.

See page 9 for analyst certification and important disclosures, including non-US analyst disclosures.

## Technology - Hardware

JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

JPM Securities (Taiwan) Limited

JPM Securities (Taiwan) Limited

## Table Of Contents

Accelerating server CPU growth cycle on AI inference cycle 3
Top-down methodology.... 3
Strong accelerator demand + Rising CPU attach rate = Exponential AI server headnode CPU growth.... 4
Agentic AI CPUs becoming a new driver for server CPU demand.... 5
Triangulating top-down forecasts with bottom-up estimates.... 7
Faster ramp of Arm-based CPUs driven by rising Arm-based CPU attach rate.... 7

# Accelerating server CPU growth cycle on AI inference cycle

We introduce our proprietary server CPU demand model. We segment CPU demand into three buckets—(1) AI server headnode CPUs, (2) regular server CPUs, and (3) agentic-AI CPUs—and forecast total server CPU shipments to grow from 26mn units in 2025 to 68mn by 2028 (38% CAGR). As AI applications transition from training toward inference, we expect agentic-AI and AI headnode CPU demand to drive a “super” general server CPU cycle.

We also size the server CPU TAM by combining our shipment forecast with ASP assumptions across the three sub-segments. Given ongoing supply tightness and continued CPU upgrade cycles, we assume \~10% annual CPU price increases. As a result, we forecast server CPU TAM to show a 53% CAGR over 2025–28, reaching \~US\$100bn by 2028, driven by both volume growth and sustained ASP expansion.

Figure 1: Server CPU shipment trend and CAGR

[[KC_IMAGE_001]]

Source: JPM estimates.Gartner®.

Figure 2: Server CPU revenue TAM forecast and CAGR

[[KC_IMAGE_002]]

Source: Gartner®. JPM estimates.

## Top-down methodology

We have anchored the total server CPU shipments for 2024 using Gartner data and forecast the server CPU demand for the respective segments over the coming years. We forecast AI server headnode CPU demand based on our AI accelerator forecast by the JPM semi team (link) (led by Gokul Hariharan) and the ratio of AI accelerators to headnode CPUs per server node. We assume no agentic AI activity in 2024 and derive the implied regular server CPU demand for 2024.

For the year 2025 and 2026, we assume non-AI server headnode CPU shipments (regular servers plus agentic AI CPUs) grow at 11%/30% YoY to 23mn/29mn, up from 20mn in 2024. This, coupled with 3mn/7mn of AI server headnode demand, could lead to 26mn/36mn total server CPU shipments (up 16%/42% YoY) in 2025/2026.


Table 1: Server CPU forecast - top-down methodology


Source: JPM estimates. Gartner®data for 2024 total server CPU shipments. Global AI accelerator shipments are based on our CoWoS estimates by the semi team (link).

## Strong accelerator demand + Rising CPU attach rate = Exponential AI server headnode CPU growth

We have seen a rising attach rate of AI server headnode CPUs. The number of AI accelerators per CPU in each AI server decreases from 4:1 to 2:1 and even 1:1 in the future generations, especially in AI ASIC servers. We attribute this to the rising requirement of CPU orchestration in AI servers due to the increasing complexity of AI server architectures. Of note, the AI accelerator forecasts are based on the CoWoS estimates by the JPM semi team (link) (led by Gokul Hariharan).

\- Nvidia GPU servers: Accelerator to CPU ratio declines to 2:1 in NVL72 compute trays from 4:1 in HGX servers. We also see CPU demand in the NVLink switch tray of the NVL72 server rack. Interestingly, we see an increase in the accelerator to CPU ratio in the HGX servers in future generations (from 4:1 to 8:1), likely due to the relatively lower CPU requirements of the HGX server architecture.

\- AMD GPU servers: Our research indicates 4:1 GPU to CPU ratios in the MI300 series and AMD MI455 Helio servers.

\- Google TPU servers: Our research indicates that there are two designs for TPU v8 servers with 1:1 and 2:1 TPU-to-CPU ratios, and that there could be a 1:1 for future generations. We assume a 50%/50% mix for 1:1 and 2:1 design for TPU v8 generation.

\- AWS Trainium servers: Our research indicates that the Trainium to CPU ratio will decline to 4:1 for the T3 liquid cooling project from 16:1 for the T2 and air-cooled T3 projects.

\- MSFT/Meta/other AI ASIC servers: We assume 4:1 accelerators to CPU ratio for the rest of the AI ASIC servers.


Table 2: AI server headnode CPU forecast


Source: JPM estimates. AI accelerator unit estimates are based on our CoWoS estimates by the semi team (link).

## Agentic AI CPUs becoming a new driver for server CPU demand

As we migrate towards the era of agentic AI, focusing on test-time scaling (i.e. long thinking), CPUs are playing an increasingly important role in orchestration, running tools and skills, storage, and security. For example, the Vera CPU not only sits in the NVL72 rack systems, but also serves as a standalone CPU across the entire Vera Rubin platform, including storage servers and CPU servers.

Figure 3: Stages of Intelligence

[[KC_IMAGE_003]]

Source: Nvidia.

Figure 4: Agent = LLM + Harness; CPU plays a critical role in the agentic AI ecosystem

[[KC_IMAGE_004]]

Source: Nvidia.

We attribute the strong general server demand this year (30-40% YoY growth on our estimates) primarily to the emerging demand for agentic AI. To quantify agentic AI demand, we assume no agentic AI activity in 2023/2024 and calculate the implied ratio of agentic AI CPUs to AI accelerators in 2025 and 2026. We then forecast the agentic AI CPU demand based on our estimates of this ratio and AI accelerator demand for 2027/2028.


## Triangulating top-down forecasts with bottom-up estimates

In the analysis below, we triangulate our top-down forecasts with bottom-up estimates. We anchor 2024 and 2025 Intel/AMD server CPU shipments to Gartner data. For 2025–28, we forecast x86/Arm server CPU shipments at 25%/72% CAGR, respectively. We estimate CPU demand for the remaining ASIC CPU vendors based on our industry research and our AI server headnode CPU demand framework.

Table 3: JPM server CPU bottom up estimates


Source: Gartner®. JPM estimates.

For each vendor, we break demand into three buckets: AI server headnode CPUs, regular server CPUs, and agentic-AI CPUs. We anchor AI headnode CPU demand using our AI server headnode CPU forecast exercise (Table 2). We assume only modest agentic-AI CPU deployments in 2024/2025 and derive the implied regular server CPU demand. For 2026–28, we assume a 5% CAGR for regular server CPU demand across categories.

We then use agentic-AI CPU demand (2026–28) and the remaining CPU buckets as balancing items to reconcile our bottom-up build with the top-down totals. Overall, we expect agentic-AI CPU demand to rise across the board.

Table 4: JPM server CPU bottom-up estimates - breakdown by applications


Source: Gartner®. JPM estimates.

## Faster ramp of Arm-based CPUs driven by rising Arm-based CPU attach rate

We forecast the adoption rate of Arm-based CPUs to reach $\sim 43\%$ by 2028 vs. $\sim 22\%$ in 2025, driven by a rising adoption rate in AI server headnodes and an x86 CPU shortage. We estimate that Arm-based CPUs will account for $90\%$ of total AI server headnode CPU demand by 2028 vs. $< 10\%$ in 2024, mainly driven by the ramp of the NVL72

server architecture with the adoption of Nvidia's Arm-based CPUs and Google's adoption of its in-house CPU for its TPU servers.


Figure 5: Total server CPU - x86/ Arm-based shipment mix

[[KC_IMAGE_005]]

Source: Gartner®. JPM estimates. Other primarily consists of Arm-based CPUs.

Figure 6: AI server headnode - x86/ Arm-based shipment mix

[[KC_IMAGE_006]]

Source: Gartner®. JPM estimates.

Companies Discussed in This Report (all prices in this report as of market close on 09 July 2026, unless otherwise indicated) ASE Technology Holding Co Ltd(3711.TW/NT\$677.00/OW), ASPEED Technology Inc.(5274.TWO/NT\$13,665.00/OW), GUC(3443.TW/NT\$4,340.00/N), Lotes(3533.TW/NT\$1,955.00/OW), SK hynix(000660.KS/W2,221,000[10 July 2026]/OW), Samsung Electronics(005930.KS/W289,750[10 July 2026]/OW), TSMC(2330.TW/NT\$2,415.00/OW), Tripod Technology Corp(3044.TW/NT\$448.50/OW), Unimicron(3037.TW/NT\$875.00/OW), Wiwynn Corp(6669.TW/NT\$5,040.00/OW)
