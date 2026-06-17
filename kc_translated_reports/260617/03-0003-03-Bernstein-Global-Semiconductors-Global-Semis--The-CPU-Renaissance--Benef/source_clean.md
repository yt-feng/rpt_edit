## Global Semiconductors
# Global Semis: The CPU Renaissance? Beneficiaries of a \$223bn TAM...

The shift from gen AI paradigm from 1.0 (chatbot) to 2.0 (agent) greatly increases server CPU demand. As discussed in SoftBank, Arm: From GenAI to Agentic AI; Initiating with Outperform Ratings, Agentic AI involves heavily autonomous task orchestration and execution, which boosts the CPU workload vs. GPU. With the shift from chatbot to agentic AI, the CPU:GPU ratio for AI data center is surging from 1:4 or 1:8 to 1:1 or higher.

We raise server CPU TAM to \$223bn (\$137bn in 2030 in the base case, 6x of the 2025 TAM of \$37bn. This assumes \$3.5tn of AI data center capex, and 1:1 CPU:GPU pairing ratio for inference. An alternative approach with 120mn CPU cores/GW yields similar TAM. Our previous forecast of \$137bn is now the bear case (assuming \$3tn AI capex, 1:2 CPU:GPU), while the upside now sits at \$330bn (\$4tn AI capex, 1.5:1 CPU:GPU).

Raising Arm PT to \$500, as Arm is the structural beneficiary of the renaissance of CPUs for agentic AI. Arm architecture is suitable for agentic AI workload given its unparalleled power efficiency. In addition, Arm is shifting from just IP provider to CPU maker, aiming to capture \$15bn revenue by CY2030, but we now forecast \$22bn as we revise CPU TAM to \$223bn in 2030 (from \$137bn). Arm's 2030 EPS (FYE31) is now lifted to \$11.79 (\$9.83 prior). Based on 42x P/E (40x prior), we lift Arm's PT to \$500 (21% upside). Given the lifted PT of Arm, we also raise SoftBank PT to ¥11,200 (58% upside), based on 30% discount to pro-forma NAV of \$572bn.

Updating numbers, raising AMD and INTC PTs. Both companies should benefit from stronger (and more sustained) server demand, though AMD's products remain superior for now (and we believe they will continue their share gain trajectory). Our existing AMD model was already consistent with a stronger server CPU environment and estimates move marginally, however we are now bringing our INTC model inline with those assumptions and are raising estimates more materially; we also roll valuation horizon forward for both to CY27/28 avg (vs CY27 prior) given we are about halfway through the year. Our AMD PT moves to \$600; INTC to \$100. We rate AMD OP, INTC MP.

Hygon will benefit from strong x86 CPU demand and gain share in China. We expect China to outpace global x86 growth from 2028 onward, with the easing of advanced-node supply constraints in China and accelerating AI investment unlocking CPU potential. We expect Hygon to steadily expand its share of China's x86 server CPU market, exceeding $35\%$ by 2030, as it increasingly penetrates into CSPs, beyond its traditional customer base of government and SOEs, supported by improved interoperability with domestic AI chips and potentially constrained supply from global vendors. We updated Hygon projection to reflect that, revising up 2027/2028 EPS to CNY 3.6 / 6.3, raising PT to CNY 450.

What could go wrong? We're still assessing if foundry/memory capacity will be sufficient to support the CPU growth. Additionally, the value of GPU/accelerator embeds the value of HBM & the markup charged by NVDA, etc. now but the high cost of memory including HBM may prompt hyperscalers to source directly from memory suppliers. Our projection is based on CPU/accelerator value & will have a downside risk if that happens.


## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

688041.CH estimate is Reported EPS; 688041.CH valuation is Reported P/E (x); ARM, NVDA base year is 2026;

In the ticker table, 2026 represents FY27/3 for SoftBank and FY26/3 for ARM.

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate SoftBank (PT=¥11,200) and Arm (PT=\$500.00) Outperform.

AMD (Outperform, \$600.00): Expectations remain high, but exposure to AI demand driving both a CPU and GPU story can provide substantial growth.

INTC (Market-Perform, \$100.00): Server strength is helping the company get back on their feet, and narrative/headlines may fuel the vibe for now.

NVDA (Outperform, \$315.00): The datacenter opportunity is enormous, and still early.

We rate Hygon (PT=CNY 450.00) Outperform: we raise our PT from CNY 280 to CNY 450, based on 2028E EPS of CNY 6.30 (+32% vs Bern. Old) and 71x P/E (Previously was Outperform, 80x P/E based on 2027E EPS CNY 3.48, PT CNY 280).

## DETAILS

We raise our 2030 server CPU TAM to \$223bn on the back of higher AI investments and strong CPU:GPU pairing ratio, and our prior forecast of \$137bn is now moved to the bear case (Exhibit 1). On the back of that, we raise PTs for Arm, SoftBank, AMD, Intel, Hygon. Our Server CPU Industry model can be downloaded here: Server CPU Industry Model. Updated Arm financial model can be downloaded here: Arm (Arm.US).

EXHIBIT 1: We believe 2030 server CPU TAM will be \$223bn in the base case of \$3.5tn AI capex.


Source: Company disclosures, Mercury, Bernstein estimates and analysis.

## RENAISSANCE OF CPU IN THE AGENTIC AI PARADIGM

Since the rise of LLM, GPU/ASIC accelerators have been the core of AI computing. While training clusters once required a dense 4:1 ratio to handle heavy data-loading, the focus shifted toward eliminating the 'CPU tax' that plagued high-scale inferencing. In custom inference-optimized deployments like Google's TPU v6e and Meta's Grand Teton, the GPU-to-CPU socket ratio moved to 8:1.

Agentic AI is pushing the CPU back to center stage (Exhibit 2) because AI systems are no longer just running a model once and returning an answer. The GPU still performs the dens maths, but the CPU increasingly determines whether the system as a whole can orchestrate the surrounding workflow efficiently — feeding data, scheduling tasks, coordinating tool calls, manage memory and avoid accelerator idling.

This is why the next generation of AI infrastructure is likely to see more balance in terms of hardware pairing, meaning CPU is no longer a small support component attached to a large pool of accelerators in the agentic era. We expect the GPU-to-CPU ratio potentially narrowing back to 1:1 from a very GPU-heavy 4:1 or 8:1 configurations. The 2026 hardware roadmaps are already moving in that direction:

• AMD Venice: 1 CPU to 4 MI455X GPUs per compute tray.
• NVIDIA Vera: 1 CPU to 2 Rubin GPUs (4 GPU dies) per superchip.
- Google TPU7x: 1 CPU to 4 TPU chips per scale-up unit.

The GPU/CPU pairing is especially important in agentic workloads because inference is turning into a loop instead of a single pass. A request may trigger retrieval, planning, tool use, intermediate reasoning, another model call, and then action, which means the GPU does the heavy compute while the CPU keeps the workflow moving efficiently; if the CPU is weak, expensive GPUs can sit underutilized, and the overall system becomes slower and less efficient.

Agentic AI also increases pressure on networking and distributed infrastructure, which strengthens the CPU's role even further (Exhibit 3, Exhibit 4). As workloads stretch across servers, clusters, and locations, the system has to move state, manage traffic, and coordinate resources in real time, so the CPU becomes critical not only inside the server but across the wider data-center fabric that supports autonomous AI execution.

Arm CPUs stand out in this environment because the new bottleneck is not only peak performance but efficient orchestration under power and space limits. As operators need more CPU capacity to support growing numbers of AI agents, Arm's pitch around performance per watt, high core density, and scalable data-center compute becomes more compelling, which is why agentic AI is helping bring CPUs back into focus and giving Arm a stronger strategic role in the next phase of AI infrastructure.

EXHIBIT 2: Arm argues that agentic AI shifts more work back to the CPU: accelerators generate tokens, but CPUs orchestrate the agents, memory and workflows needed to deliver answers, making Arm's efficient CPU architecture increasingly critical in AI data centers

[[KC_IMAGE_001]]


Source: Arm

EXHIBIT 3: CPU is expected to play a more important role within inference, in the agentic area.

[[KC_IMAGE_002]]


Source: Ciena estimates, Bernstein analysis.

EXHIBIT 4: Agentic AI shifts compute balance toward CPUs, with CPU share rising from \~14% in Traditional LLMs to 50%, highlighting CPUs' growing orchestration role alongside GPUs in AI workloads at scale
CPU:GPU ratio shift in Agentic AI

[[KC_IMAGE_003]]


Source: TrendForce, Bernstein analysis

EXHIBIT 5: AI infrastructure TAM expands sharply by CY30, led by data center accelerators reaching \$1T, while data center CPU also quadruples from \$33bn to \$137bn.

[[KC_IMAGE_004]]


Source: Mercury, Company reports, Bernstein estimates and analysis.

EXHIBIT 6: We expect the server CPU market to grow from US\$37bn in 2025 to US\$223bn in 2030, accelerating at a 43% CAGR, driven by Agentic AI adoption.

[[KC_IMAGE_005]]


Source: Mercury, Company reports, Bernstein analysis and estimates

## RAISING 2030 SERVER CPU TAM FORECAST TO \$223BN

Within our initiation of Arm, we forecast the CY30 data center CPU TAM of \$137bn, well above both Arm's own estimates of \$100bn and AMD's \$120bn, on the basis that agentic workloads require much more CPU intensity.

Since our initiation, there are quite a few incremental developments, including better-than-expected agentic AI adoption, and higher-than-expected AI GW and capex spending. Nvidia also guided for a \$20bn revenue from Vera CPU which should also be positive for Arm. The other notable data point that was provided by Nvidia was the annual AI infrastructure spending forecasts of over \$1tn by 2027 and \$3-4tn towards the end of the decade.

Based on these data points, we revise our top-down estimates for the server CPU TAM to \$223bn (Exhibit 7), with the following assumptions:

- AI capex of \$3.5 tn in 2030, implying 70 GW AI data center deployment at \$50bn / GW
- AI GPU (including ASIC accelerator) market of \$1.6 tn, or 45% of AI DC capex
• CPU:GPU unit ratio of 1:1 for inferencing and 0.5:1 for training, and CPU ASP as 13% of GPU
- This results in server CPU TAM of \$223bn, including \$174bn for agentic AI workload and \$49bn for non-AI workload

We also did a sanity check based on an alternative method of CPU core count:

- According to Arm, agentic AI workload requires 120mn CPU cores / GW, vs. traditional data center requiring only 30mn cores / GW
- This translates into 8.4bn server CPU cores for 70 GW AI data center deployment in 2030
- AI CPU TAM would be \$168bn in 2030 assuming \$20/core (likely conservative), similar to the \$174bn calculated above

Our sensitivity analyses suggest that even a rather conservative take of this figure implies a meaningful agentic CPU opportunity.

- In the bear case, the main assumptions are \$3tn AI capex, combined with a CPU-to-GPU ratio of 0.5x for inference. The server CPU TAM then would be \$137bn, matching our previous forecast which now looks somewhat conservative.
- In the bull case, we assume \$4tn AI capex, combined with a CPU-to-GPU ratio of 1.5x for inference. The resulting server CPU TAM would be \$330bn.

A sensitivity table for various assumptions is also listed in (Exhibit 8). Investors can play with these assumptions in the updated CPU TAM model.

EXHIBIT 7: We believe 2030 server CPU TAM will be \$223bn in the base case of \$3.5tn AI capex.


Source: Company disclosures, Mercury, Bernstein estimates and analysis.

## EXHIBIT 8: Our sensitivity analysis on CPU tie ratio and AI infra TAM suggests a range of \$137bn-\$330bn.

Total Server CPU TAM (USD bn)


This sensitivity assumes non-AI CPU CAGR of 9.5%.
Source: Bernstein estimates and analysis.

## ARM: STRUCTURAL BENEFICIARY OF SERVER CPU TAM

## ARM'S SHARE GAIN IN SERVER CPU

## Why Arm could gain share from x86 in server CPU?

The core economic case is performance per watt and total cost of ownership. AWS states Graviton delivers up to 40% better price performance versus comparable x86 instances, up to 20% lower cost, and up to 60% lower energy consumption for equivalent workloads on certain use cases. Microsoft Azure notes that each vCPU on Cobalt 100 maps to a full physical core, making performance more predictable for server workloads versus x86 designs that use hyperthreading to inflate vCPU counts.

Beyond economics, hyperscalers gain architectural control. Designing in-house CPUs lets them shape the memory subsystem, I/O, accelerator interconnects, and security offload to fit their own infrastructure rather than relying on the roadmap of a merchant silicon vendor. This is why each major CSP has now committed to a multi-generation internal CPU program built on Arm Neoverse cores.

Above all, power consumption is one of the biggest reasons that Arm CPUs are much more likely to be adopted in AI data centers. The world is facing an energy issue that not enough electricity is available to power the new data centers. According to our forecast, AI accelerator power will almost 3x to reach 37 GW to be deployed in 2028. Including the power for CPU, memory, networking, etc, the total power consumption of AI data center would surpass 50 GW. As we can't do much to cut down power consumption of GPU/AI accelerators, using Arm server to reduce power consumption becomes the only viable choice.

EXHIBIT 9: We estimate AI accelerator GPU power reaches \~37GW in 2028 versus 12.8GW in 2025, a 43% CAGR over 2025–2028E. If we assume GPUs to account for \~70% of server power, total AI data center demand scales from \~18GW in 2025 to \~53GW in 2028.

[[KC_IMAGE_006]]


Source: Company reports, Bernstein analysis and estimates

EXHIBIT 10: CPU represents between 40% and 60% of power consumption in a general server, but only 5–10% in an AI server, where most power is consumed by AI accelerators.

[[KC_IMAGE_007]]


Source: Bernstein analysis and estimates

## CSP CPU Roadmaps and Arm Penetration

AWS, Microsoft, and Google have each built Arm-based CPU programs (Exhibit 1.1) that are deepening Arm's data center presence across generations. According to Arm, their penetration at data centers has surpassed 50% among top hyperscalers with over 1bn Neoverse cores deployed.

- AWS: As the largest IaaS provider with 47% market share as of 2024, AWS is also the dominant deployer of Arm-based instances, with 57.2% of Arm instances across the public cloud as of 2024 year-end being deployed at AWS. AWS was the first mover to deploy Arm processors on public cloud, debuting their first arm-based instance back in 2018. As of December 24, according to Liftr Insights, Arm-based Graviton represented 25% of the total instances deployed at AWS.
- Microsoft Azure: As the second largest IaaS provider with 17% market share as of 2024, Azure also heavily deploys Arm-based instances, with an estimated 33% of chips being Arm-based as of Q4 2024. This is a rapid ramp considering their first Arm processor Cobalt 100 debuted only in 2024. (What performance and efficiency does Microsoft Azure Cobalt 100 VMs deliver using Arm Neoverse performance? - Arm Newsroom)
- Google GCP: Google was the third biggest IaaS provider as of 2024 with 7% market share, and they too have ramped Arm instances rapidly, with an estimated 21% share of all instances being Axion, which was introduced in 2024.

## Why Nvidia uses Arm CPUs

Nvidia's motivation for Arm is distinct from the hyperscalers: in AI and HPC systems, the critical bottleneck is more in data movement between the CPU, memory pool, and GPU - rather than raw CPU instruction throughput or enterprise application compatibility. Nvidia says its Grace CPU (72 Neoverse V2 cores per die, 144 cores in the Grace CPU Superchip using dual-die NVLink-C2C delivering up to 1.0 TB/s of LPDDR5X memory bandwidth) benefits from the NVLink-C2C interconnect that carries up to 900 GB/s bidirectional bandwidth between the CPU and Blackwell GPU - versus PCIe Gen 5's \~128 GB/s. The second-generation NVLink-C2C used in GB200 racks achieves 1.8 TB/s of bidirectional bandwidth, 7x faster than PCIe Gen 6. (NVIDIA Grace CPU Delivers World-Class Data Center Performance and Breakthrough Energy Efficiency | NVIDIA Technical Blog, NVIDIA Grace CPU and Arm Architecture | NVIDIA)

Grace was first deployed in the GH200 Grace-Hopper Superchip for HPC/AI clusters starting in 2023. The major inflection came in 2025 when Nvidia standardized on the DGX GB200 rack form factor - bundling one Grace CPU with two Blackwell GPUs per Superchip, with each DGX GB200 rack containing 36 Grace CPUs and 72 Blackwell GPUs, totaling 2,592 Arm Neoverse V2 cores per rack. This shift from the standalone HGX/MGX GPU tray format toward integrated DGX rack-scale deployment materially increased Arm CPU unit volume in AI server shipments.

The Nvidia Vera CPU (successor to Grace, launching with Rubin GPUs in 2026) further raises the bar: Vera delivers up to 1.2 TB/s of memory bandwidth — twice the bandwidth at half the power compared to traditional x86 CPUs - and is built on Nvidia's proprietary Olympus CPU cores, a custom Arm architecture designed for Reinforcement Learning and agentic AI workloads. Vera enables software environments to run up to 50% faster with twice the efficiency of conventional CPU infrastructure. (Next Gen Data Center CPU | NVIDIA Vera CPU)

EXHIBIT 11: Compariison of Server CPU specifications for Arm ASICs, Nvidia custom CPUs and x86.


Source: Company disclosures, Bernstein analysis.

EXHIBIT 12: We expect Arm's market share to continue the strong trend of growth.

[[KC_IMAGE_008]]


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 13: Roadmap of CPUs based on Arm IP

[[KC_IMAGE_009]]


Source: Company disclosures, Bernstein analysis

## ARM AGI CPU: DRASTIC CHANGE IN BUSINESS MODEL TO CAPTURE THE GROWING OPPORTUNITY

At Arm Everywhere event in March 2026, Arm announced an important strategic move to provide their own silicon, the Arm AGI CPU, after decades of monetizing primarily through IP licensing and royalties, making clear that the silicon offering will complement - rather than replace - its existing IP and CSS businesses.

Their rationale was that not every client can design CPUs of their own, so companies like Meta, - which Arm identified as the first customer, lead partner and co-developer - and OpenAI can just buy Arm's CPUs, while other CSPs such as Amazon, Google and Microsoft who can keep licensing Arm IPs for their CPU endeavours. Alongside Meta and OpenAI, they also confirmed many other partners including Cerebras, Cloudflare, F5, Positron, Rebellions, SAP and SK Telecom. These customers are expected to deploy Arm AGI CPU for agentic usage. Arm partners with OEMs and ODMs, as well as other supply chain partners across cloud, memory, networking, manufacturing and many other aspects, such as AWS, Broadcom, Google, Marvell, Micron, Nvidia, Samsung, SK hynix and TSMC among many others.

Financially, the model change is clearly margin dilutive in percentage terms, but very likely accretive in gross profit dollars and operating profit dollars. Management's event target was for the AGI CPU business to reach \$15bn of revenue by FY31, with total company revenue of \$25bn and non-GAAP EPS of \$9, with AGI CPU OPM is expected to exceed 30% by FY31. We believe the key point is that Arm is choosing to trade some margin rate for a dramatically larger profit pool. Just as importantly, management said the required engineering investment is already largely embedded in today's cost base, meaning the near-term P&L is already carrying much of the R&D burden, while the revenue opportunity from silicon only starts to appear from much later on to bring the operating leverage once volume scales.

Our estimate bases on a more aggressive assumption and we forecast \$22bn chip value as of FY31 (Exhibit 14) which roughly equates to c. 4.9mn CPU units based on \$4.6k ASP in FY31. We believe Arm silicon should generate \$7.7bn OP (or 52% of corporate OP) in FY31 in our forecast (Exhibit 15).

## How we frame the server CPU model for Arm

Our key assumptions on how we think of the server CPU demand are as follows. First of all, we assume that the big 3 CSPs (AWS / Google Cloud / Azure) continue to mainly use their own captive ASIC CPU chips.

Also, for Nvidia, we believe that aside from the CPUs bundled within the superchips (CPUs packaged with GPUs), Nvidia is to release standalone CPU racks for agentic workloads, but the important distinction being these will be entirely sold in rack-scale and as a system, rather than bare-metal CPUs.

Lastly, Arm AGI CPU will address the need for merchant CPU for any CSPs and/or customers who elect to build their own systems based on Arm architected CPUs, instead of buying a full system from a third-party vendor (including Nvidia), to suit their specific computing needs.

EXHIBIT 14: We now forecast Arm AGI CPU sales to reach \$22bn by FY31.

[[KC_IMAGE_010]]


EXHIBIT 15: We believe OP contribution from Arm silicon could go as high as \$7.7bn as of FY31.

[[KC_IMAGE_011]]


Source: Company disclosures, Bernstein estimates and analysis.
Source: Company disclosures, Bernstein estimates and analysis.

Our Arm server CPU model is built bottom-up across four distinct sets of demand: 1. Nvidia-related Arm CPUs, 2. hyperscaler in-house CPUs, 3. Arm's own CPU silicon business, and 4. other merchant / enterprise Arm CPUs. We believe this segmentation enables us to identify the different adoption driver, volume logic, royalty profile as well as strategic implications for Arm. At a high level, we estimate the server CPU TAM rising sharply towards the end of the decade as agentic demand shifts the balance between accelerators and CPUs. Our bottom-up 2030 server CPU TAM is \$223bn, of which we estimate Arm to take \$123bn (Exhibit 16).

In terms of the different demands, firstly on Nvidia, we break it down further into GPU-attached racks and standalone CPU racks. The former is based largely on our CoWoS-based GPU estimates and the attach rate (or rather, how much GPU is sold in rack-scale instead of standalone), and the latter is based on how much agentic demand will be met by Nvidia CPUs, and how many CPUs are to be attached as a result. We model it to grow significantly from 1.2mn units in CY25 to 6.1mn units in CY30 (Exhibit 17).

EXHIBIT 16: We estimate a 2030 server CPU TAM of \$223bn, of which we believe Arm will be around \$123bn.
EXHIBIT 17: We estimate Nvidia-related Arm CPU units to grow by 5x by 2030.

[[KC_IMAGE_012]]


Source: Company disclosures, Mercury, Bernstein estimates and analysis.


[[KC_IMAGE_013]]


Source: Company disclosures, Bernstein estimates and analysis.

For hyperscaler in-house CPUs, such as AWS Graviton and Google Axion, we model it as a function of server unit assumptions as well as ODM-direct server exposures, and applying Arm penetration within the CSP server base. In our model, we assume Arm penetration to grow from 25% in CY25 to 36% in CY30 (Exhibit 18).

Including other / merchant Arm CPUs including Arm's own AGI CPU, our bottom up TAM estimates for 2030 closely matches the top-down \$123bn, of which in Nvidia related demand comprises \$58bn, CSP ASIC portion \$39bn, Arm AGI CPU \$22bn (Exhibit 19), with the majority still being Nvidia / CSP-related custom chip demand.

EXHIBIT 18: We expect a stable increase in Arm's share within CSP CPUs, reaching 36% in 2030.

[[KC_IMAGE_014]]


Source: Company disclosures, Mercury, IDC, Bernstein estimates and analysis.

EXHIBIT 19: Within the estimated 2030 TAM of \$123bn, Nvidia / CSP demand comprises the majority.

[[KC_IMAGE_015]]


Source: Company disclosures, Bernstein estimates and analysis.

## ARM'S ROYALTY IN SERVER CPUS

## Royalty increase in Arm server CPUs driven by core count and increased royalty rate

Even before the AGI CPU contribution, Arm's cloud CPU royalty model is already becoming materially more attractive. Arm said in its Q3 2026 earnings that cloud AI / general-purpose data-center royalty revenue grew more than $100\%$ YoY, Neoverse deployments surpassed 1bn cores, and Arm's share among top hyperscalers was expected to approach $50\%$ .

The first driver is that core counts are rising fast (Exhibit 20). AWS Graviton 5 now has 192 cores, up 2x versus Graviton 4; NVIDIA Vera has 88 Arm-based cores versus 72 for Grace; and Microsoft's Cobalt 200 has 132 cores. At Arm Everywhere event, management indicated that the next wave of cloud CPUs could move into the 200-300 core range and, in some cases, toward 500 cores over time.

We think the underlying reason is the same one driving the AGI CPU opportunity: the workload mix is changing. Agentic and always-on inference shifts more of the bottleneck toward orchestration, memory handling and coordination work, which in turn increases the need for higher core count, power-efficient CPUs in AI clusters. Arm themselves said the shift toward agent-based inference is redefining AI data-center designs and raising demand for CPU chips with even more power-efficient cores.

EXHIBIT 20: Core count for server-side CPUs is increasing.

[[KC_IMAGE_016]]


Source: Company disclosures, Bernstein analysis.

The second driver is higher royalty per core. Currently, Arm's licensees pay roughly \$0.50/core for first-generation v9 server CPUs, around \$1/core for first-generation CSS (Compute Subsystem), and potentially \$1.50/core for later CSS generations, with more upside in future generations. In other words, Arm is not only getting paid on more cores, but on more valuable cores, and CSS is central to that step-up.

Arm describes CSS as pre-integrated, pre-validated, performance-validated subsystem products that help partners reach production silicon faster. In other words, CSS sits above the core level: it wraps CPU cores with coherent interconnect, MMU/NOC system IP, memory channels, and I/O so a chip company does not have to assemble the whole server platform from scratch.

The company has said CSS adoption is a major tailwind to royalty growth, and customers can save substantial engineering effort and accelerate time-to-market by up to roughly a year. Arm also says CSS customers have reported getting from kickoff to working silicon in 13 months and saving 80 engineering years by offloading non-differentiated design and validation work. That higher value proposition is what allows Arm to charge materially higher royalties than for core IP alone.

CSS includes more than Neoverse cores alone, bundling the cores with CMN mesh, system IP, system management, power management, software, and development tools needed to bring a platform to market quickly. Arm positions this as the fastest path to production silicon for cloud, AI, 5G, and networking chips because partners can focus on customization instead of rebuilding the common infrastructure around the cores.

The cadence of product refreshes also matters. Management's notes suggest server CPUs used to refresh every two to three years, but increasingly move on an annual cadence, which in practice makes CSS more valuable because customers need faster turn times to stay on the latest node and architecture. That dynamic should support both more frequent licensing activity and a faster mix shift toward higher-royalty generations.

In cloud specifically, the early evidence of that shift is already visible. Microsoft's Cobalt family is explicitly built on Neoverse CSS. Company also mentioned that CSS should exceed 10% of cloud AI royalty by FY27, and rise above 30% by FY29 and exceed 50% by FY31. If that progression is broadly right, the royalty mix should keep skewing toward higher-value server designs over the next several years.

In conclusion, we see strong growth in Arm's server royalty revenue (Exhibit 22), reaching \$1.8bn in FY31 from \~\$135mn in FY25, driven by the increasing core count as well as higher per-core royalty rate, resulting in as structural server CPU royalty growth even before giving Arm any credit for its own AGI CPU silicon revenue.

EXHIBIT 21: We expect per-chip royalty to drop in FY26-FY27 due to Grace / Vera, but expect strong growth going forward due to increase in royalty rate.

[[KC_IMAGE_017]]


Source: Company disclosures, IDC, Mercury, Bernstein estimates and analysis.

EXHIBIT 22: We expect a strong growth in cloud royalty revenue.

[[KC_IMAGE_018]]


Source: Company disclosures, Bernstein estimates and analysis.

## FINANCIALS AND VALUATION CHANGE

Exhibit 23 summarizes our estimate changes. We keep our estimates for all the segments other than server CPUs.

In terms of valuation, Arm has rerated significantly over the past month, and Arm's current share price now implies 174x multiple on 1-year forward P/E, which is near +5 $\sigma$ of historical trading range (Exhibit 24). As such, we believe it to be more sensible to value Arm on FY31E financials, when the Arm AGI CPU business is expected to normalize to some degree. CY2030 is also where most of the discussion on CPU TAM anchors on including Arm's TAM estimates as well as our own.

Therefore, we shift the valuation anchor from our usual Q5-Q8 EPS framework to FY31E EPS, as the market debate is increasingly centred on the company's FY31 opportunities. We value the IP businesses at 70x and silicon businesses at 40x (30x prior, raised in expectation of acceleration in CPU market growth) respectively, blend the multiples by net income contribution to derive a 54.5x FY31E P/E, and discount that back 2.75 years at a 10% WACC to reconcile the anchor year with our usual 24-month forward valuation horizon.

## Put simply, we use the equivalent multiple of 42x on FY31 EPS of \$11.86 to derive the PT of \$500 (Exhibit 28) and reiterate Outperform.

Within this valuation framework, we believe two of the biggest swing factor for Arm would be how much the total AI capex spending would be, as well as how much market share Arm silicon is able to take. Our sensitivity analyses (Exhibit 26, Exhibit 27) suggest an FY31E EPS range of \$9-\$16, and a valuation range of \$379-\$677.

EXHIBIT 23: Arm: Summary of estimate changes


Source: Company disclosures, Bloomberg, Bernstein estimates and analysis.

EXHIBIT 24: Arm has rerated significantly over the past month, and is currently valued at +5SD of historical range, on a 1-year forward P/E basis.

[[KC_IMAGE_019]]


Source: Bloomberg, Bernstein analysis and estimates

EXHIBIT 25: As such, we feel it's more sensible to value Arm on FY31E EPS, on which the company anchors their projection. On FY31E EPS, the stock currently trades at 44x, close to +3SD of YTD range.

[[KC_IMAGE_020]]


Source: Bloomberg, Bernstein analysis.

EXHIBIT 26: Our sensitivity analysis implies FYE31 EPS range of \$9.0-\$16.1.
Sensitivity analysis - Arm EPS


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 27: Our sensitivity analysis implies a valuation range of \$379-\$677 as a result.
Sensitivity analysis - Arm Valuation


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 28: Taking the blended average of P/E multiple for the two segments yields an implied target P/E of 42x, and a target price of \$500.


Source: Company disclosures, Bernstein estimates and analysis.

## SOFTBANK: AN INDIRECT BENEFICIARY OF AGENTIC AI CPU

Following the uplift to our forecasts and price target for Arm, we correspondingly raise our estimates for SoftBank's NAV, given Arm remains one of its largest consolidated subsidiaries. Excluding Arm and share price movements in SoftBank's listed equity holdings, we keep the rest of our SoftBank forecasts unchanged (Exhibit 29, Exhibit 30). Reflecting the higher NAV, we raise our price target to ¥11,200 (vs. ¥8,200 previously), based on a 30% NAV discount. We reiterate our Outperform rating on the stock.

EXHIBIT 29: SoftBank: Summary of estimate changes


Source: Company disclosures, Bloomberg, Bernstein estimates and analysis.

EXHIBIT 30: SoftBank Valuation: Scenario Analysis


SoftBank's share price as of 16th June 2026; Arm's share price as of $15^{\text{th}}$ June 2026.
Source: Company disclosures, Bloomberg, Bernstein estimates and analysis.

## X86 WILL ALSO ENJOY THE TAILWIND FROM AGENTIC AI SERVER CPU WORKLOAD

Intel and AMD are currently benefitting from incredibly strong server demand, a function of both cyclical recovery following several years of post-COVID shortfalls as well as (more recent) a sharp upward revision in demand related to agentic AI requirements (Exhibit 31) with both Intel and AMD benefitting.

We note the company's response (or even awareness) of the potential for agentic AI to drive CPU demand differed. Intel appeared caught significantly off-guard (they were in fact selling off supposedly “excess” tooling last July on the belief that demand would remain subdued, and were surprised at the end of last year where they had to scramble (suffering shortfalls in Q1 though they are in the process of correcting their mistake now). AMD was more proactive in securing capacity, and their sequential x86 share gains accelerated in Q1 as Intel found themselves constrained (Exhibit 32). However, Intel also benefited from the demand environment, that was so strong in fact that they managed to sell previously-written-off parts they had (presumably) trashed, but which still found homes as customers proved willing to buy up anything they could get their hands on.

At their analyst day in November AMD laid out expectations for a \~\$60B CPU TAM by 2030 on the rise of agentic AI. Clearly the pace and trajectory of the ramp surprised them as well though as they doubled the number in May on their Q126 earnings call to \$120B. And the company is also benefitting not only from the demand environment but also their competitive positioning as they continue to take share given their superior product portfolio (Intel hopes to close the gap in a few years on the launch of Coral Rapids, but admits that their current offerings leave something to be desired).

We update numbers and price targets for AMD and Intel today. Both companies should benefit from stronger (and more sustained) server demand, though AMD's products remain superior for now (and we believe they will continue their share gain trajectory). Changes to our estimates can be found in Exhibit 33 (AMD) and Exhibit 34 (Intel). Our existing AMD model was already consistent with a stronger server CPU environment and estimates move marginally, however we are now bringing our INTC model inline with those assumptions and are raising estimates more materially; we also roll valuation horizon forward for both to CY27/28 avg (vs CY27 prior) given we are about halfway through the year. Our AMD PT moves to \$600; INTC to \$100. We rate AMD OP, INTC MP.

EXHIBIT 31: Agentic AI has driven a sharp upward revision in x86 server CPU growth this year

[[KC_IMAGE_021]]


Source: Mercury Research, Bernstein estimates and analysis

EXHIBIT 32: AMD's x86 share gains accelerated in Q1 as Intel found themselves constrained

[[KC_IMAGE_022]]


Source: Mercury Research, Bernstein analysis

EXHIBIT 33: AMD - Bernstein annual changes to estimates


Source: Bernstein estimates and analysis

EXHIBIT 34: Intel - Bernstein annual changes to estimates


Source: Bernstein estimates and analysis

## WHAT COULD GO WRONG?

Our projection above does not consider production capacity, but it is possible that capacity of TSMC and Intel, and to a lesser degree Samsung may be insufficient to support the projected growth. The capacity at TSMC is particularly critical, as most suppliers find TSMC their top choice given TSMC's leading technology, efficiency and execution. At the same time, nearly all GPU/accelerator suppliers are using TSMC for production too and they also find TSMC's capacity insufficient to fulfill their needs. TSMC and these customers together need to strike a balance between these needs, as AI needs both CPU and GPU/accelerator to grow.

Memory capacity can be another bottleneck. CPU needs to be paired with an adequate amount of memory to perform its functions, and so does GPU/accelerator too. Memory capacity hence can be another bottleneck that makes our projection above too high.

We are trying to answer both questions now and will update investors with any notable findings.

Another important but less known consideration is HBM is packaged together with GPU/accelerator. The cost of HBM is therefore part of the COGS of these chips. This cost is then “marked up” by NVIDIA, etc. so that these GPU/accelerator suppliers can command high margins, often as high as 60s to 70s% gross margin, on the entire packaged chip. For AI hyperscalers, the burden from this “markup” was smaller before, but is becoming much heavier quickly as memory price surge is propagating to HBM too. Hyperscalers hence will attempt to source HBM directly from memory suppliers to avoid this “markup”. Alchip and MediaTek are offering this business model in their ASIC business currently. They perform necessary qualification & test to ensure HBM sourced by hyperscalers is compatible with the rest of ASIC chips, and have proven this business model is technologically feasible. Should hyperscalers adopt this model broadly, HBM value will be removed and the size of GPU/accelerator will become smaller. Since our CPU projection above anchors on GPU/accelerator market size, the business model of hyperscalers sourcing HBM directly is a downside risk to our projection.

## CHINA X86 SERVER CPU MARKET DYNAMICS

## CHINA TAM VS GLOBAL TAM

China's share of global x86 server CPU TAM is entering a period of near-term compression before a structurally driven recovery over the medium term. Historically steady at \~30% during 2020–2024, we expect China's share will decline to a trough of \~21–23% in 2026–2027, as illustrated in Exhibit 35. We attribute this near-term compression primarily to structural constraints in China's AI server build-out. Limited access to AI chips, driven by export control on leading global GPUs as well as supply shortages of domestic alternatives due to foundry capacity constraints, has slowed the pace of AI infrastructure deployment in China. Moreover, China CSP capex expansion has been comparatively more moderate than US hyperscalers, which are aggressively investing in AI infrastructure, particularly rapid deployment of servers for agentic AI workloads. This dynamic is further amplified by global CPU vendors prioritizing supply allocation toward large US CSPs and AI labs, where demand visibility and monetization pathways are stronger, thereby boosting CPU attach rates for AMD and Intel in those markets. As a result, China's TAM growth lags that of the Rest of World in the early phase of the cycle (China +30.6% CAGR in 2025–2028 vs. RoW +34.8%), leading to a temporary demand share loss. However, we expect this dynamic to reverse in the outer years: as domestic AI chip supply improves and AI investment accelerates, China's TAM growth re-accelerates (+36.3% CAGR in 2028–2030 vs. RoW +26.6%), driving a recovery in share to \~27% by 2030. Overall, the chart highlights a near-term dislocation followed by a catch-up phase, with China remaining a meaningful contributor to global x86 server CPU demand over the medium term.

EXHIBIT 35: China's share of global x86 server CPU TAM is entering a period of near-term compression, before structurally recovery after 2027

[[KC_IMAGE_023]]


Source: Gartner, Mercury, Bernstein analysis and estimates

## INCREASING LOCALIZATION SHARE

The China x86 server CPU market is undergoing a steady shift toward domestic substitution, with Hygon consistently gaining share and poised for further acceleration. Exhibit 36 shows Hygon's share has increased from LSD in the early 2020s to \~20% by 2026–2027, primarily driven by localization requirements from government and state-owned enterprise (SoE) customers. This policy-driven adoption has provided a stable foundation for domestic CPU penetration, even as overall China TAM growth remains constrained in the near term. Looking ahead, we expect Hygon's share gains to accelerate

meaningfully from 2028 onward, with domestic share rising to \~35% by 2029–2030. This inflection is underpinned by continued product improvements (e.g., performance and ecosystem compatibility) and, importantly, better interoperability with domestic AI accelerators, which should make Hygon platforms increasingly viable for cloud service providers (CSPs) beyond the traditional government/SoE customer base. At the same time, tight global supply conditions are likely to persist, with AMD and Intel prioritizing higher-value and more strategic US customers. This supply allocation dynamic further reinforces the opportunity for Hygon to expand its footprint in China, driving a structurally higher level of self-sufficiency in the domestic x86 server CPU market over the medium term.

EXHIBIT 36: Hygon has been consistently gaining share and poised for further acceleration after 2027

[[KC_IMAGE_024]]


Source: Mercury, companies reports, Bernstein analysis and estimates

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 37: Arm: Income Statement


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 38: Arm: Balance Sheet


Source: Company reports, Bernstein analysis and estimates

EXHIBIT 39: Arm: Cash Flow Statement


Source: Company reports, Bernstein analysis and estimates

EXHIBIT 40: SoftBank: Income Statement


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 41: SoftBank: Balance Sheet


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 42: SoftBank: Cash Flow Statement


Source: Company disclosures, Bernstein estimates and analysis.

EXHIBIT 43: Bernstein AMD Income Statement


Source: Company reports, Bernstein estimates and analysis

EXHIBIT 44: Bernstein AMD Balance Sheet and Cash Flow Statement


Source: Company reports, Bernstein estimates and analysis

## EXHIBIT 45: Bernstein INTC Income Statement

Intel: Income Statement (\$M)


Source: Company reports, Bernstein estimates and analysis

EXHIBIT 46: Bernstein INTC Balance Sheet and Cash Flow Statement


## EXHIBIT 47: Bernstein NVDA Income Statement

NVIDIA: Income Statement


Source: Company reports, Bernstein estimates and analysis

## EXHIBIT 48: Bernstein NVDA Balance Sheet

NVIDIA: Balance Sheet


Source: Company reports, Bernstein estimates and analysis

## EXHIBIT 49: Bernstein NVDA Cash Flow Statement

NVIDIA: Cash Flow Statement


Source: Company reports, Bernstein estimates and analysis

## EXHIBIT 50: Bernstein NVDA Revenue Model

NVDA: Revenue Model (\$M)


Source: Company reports, Bernstein estimates and analysis

EXHIBIT 51: Bernstein Hygon Income Statement


Source: WIND, Bernstein analysis and estimates

EXHIBIT 52: Bernstein Hygon Balance Sheet


Source: WIND, Bernstein analysis and estimates

EXHIBIT 53: Bernstein Hygon Cash Flow Statement


Source: WIND, Bernstein analysis and estimates
