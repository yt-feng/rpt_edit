# Bringing More Light to Scale-Up Networks: An Updated Scale-Up Primer
## WHAT'S CHANGED


The scale-up market is set to be a \~\$70bn opportunity by 2030, over 4x the size estimated a year ago, as capex and cluster sizes grow. We explore recent debates/technology evolutions, with conclusion being copper is likely to remain for longer, but CPO is eventual, making recent sell-offs overdone.

Architectures in flux as scale-up network grows. As AI models grow in complexity and scale, the demand for high-performance computing infrastructure has surged, with \$70bn+ opportunity estimated over 4x the estimate we put forth last year. The scale-up network is critical because it allows accelerators to operate as a single system, eliminating communication bottlenecks and enabling the scale, speed, and efficiency required to train today's frontier AI models. With such a large opportunity, there are multiple different architectures being contemplated, from the interconnect fabric (NVLink, UAL, SUE) to the transmission technology (many forms of copper and optical interconnect). Given the concentration of buyers, adoption of any of these technologies creates meaningful opportunity, and we do not expect uniformity in approaches.

Copper to remain for longer, but optics in scale-up will happen. Copper remains the favored transmission technology in scale-up, given latency, power consumption, cost and openness of ecosystem. However, as signalling speeds increase, electrical losses, insertion loss and noise become progressively more difficult to manage, requiring increasingly sophisticated SerDes, digital signal processors, retimers and equalisation techniques simply to preserve signal integrity. As scale-up domains extend beyond a single rack, copper requires increasingly complex SerDes and signal conditioning to maintain performance, driving higher power consumption and lower efficiency. As a result, we see the key catalysts for eventual optical adoption in scale-up: (1) multi-rack scale-up architectures, (2) rising electrical I/O power consumption, (3) increasing bandwidth density requirements, and (4) continued growth in bandwidth demands from larger, more communication-intensive AI workloads. These trends should increasingly favor near-package and co-packaged optical solutions over time, with adoption strongest in scale-up in the 2029 and beyond period (we do see small adoption in 2028). We do not see 2028 introductions as delayed, but we do not see more meaningful adoption of CPO until Feynman generation of NVDA technology.


For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

We remain constructive on scale-up networking semis, where XPU proliferation creates a greenfield opportunity across switching, copper and optics. NVIDIA is our Top Pick in semis and we are also positive on Broadcom ahead of its 2027–28 ASIC ramps and the associated networking pull-through. We remain OW Astera as a leading pure-play beneficiary and are excited for the ramp of Scorpio, UALink and optics, though valuation is high at this point. We expect Marvell to gain scale-up share but remain sidelined on valuation and limited XPU visibility, while Semtech offers attractive copper and linear-optics exposure but still needs to prove execution. Overall, we see positive structural tailwinds across the group given the size of the opportunity, with ratings driven more by valuation and execution record.

We have rebuilt our LITE / COHR / GLW models to incorporate Co-packaged optics (CPO) adoption percentages and see next catalyst for optical as OCP in October; upgrading KEYS on thesis that it will be a beneficiary from diversity of architectures. GLW, LITE, COHR are the clearest beneficiaries of the eventual move of optical into the scale-up domain (evidenced by NVDA investments). We think Q2 earnings may not be a material catalyst given current supply constraints and concerns around delays / smaller adoption of CPO in 2028 (which has caused recent underperformance). However, we think the catalyst for enthusiasm about CPO will be OCP in October, meaning we would be more constructive on the names coming out of earnings and into that event. In terms of actionability now, we upgrade KEYS to OW (see separate note). Reason being, KEYS, a test & measurement leader benefits from the diversity of architectures (each of which needs to be tested), which this note clearly highlights that diversity is likely to take place. With multiple in-line with historical times of stronger investment cycles, we see it as still having room for positive movement as estimates get revised upwards (from strong incrementals on spending on AI, semis, A&D and edge AI / 6G).

Exhibit 1: Scale-Up Market Estimate Has 4x'd Y/Y

[[KC_IMAGE_001]]

Source: Dell'Oro. Note: Excludes NICs, Pluggables/Optics, and Cables

Exhibit 2: CPO Penetration to Come Later to Scale-Up, But Post 2028, Should Be Meaningful Adoption

[[KC_IMAGE_002]]

Source: Dell'Oro.

## Analysis

## Table of Contents:

1) Scale-Up Opportunity Continues to Grow Rapidly

2) Growth Driven By Multiple Vectors

3) How We View the Architecture Progression

4) What are the Interconnect / Fabric solutions? (e.g. NVLink, UALink, SUE)

5) What are the Transmission Approaches As Industry Eventually Hits "Copper

Wall"? (e.g. Copper, Optical, CPO, NPO)

6) Common Questions / Debates

7) Stock Takeaways / CPO Adoption EPS Analysis

## Scale-Up Opportunity Continues to Grow Rapidly

The primer from MS last year around the scale-up network opportunity noted the newness of the opportunity as high-speed communication between accelerators was extended further into the rack or between racks (allows them to function as one large supercomputer, accessing the same memory and processing the same workload). A year later, with capex data points being revised up and new generations of accelerator architectures being introduced that expand the size of the scale-up cluster, the scale-up opportunity estimated to be \$17bn by 2029 last year is now expected to be \$73bn by 2030, a 4x multiplier.

Exhibit 3: Scale-Up Market Estimate Has 3x'd Y/Y

[[KC_IMAGE_003]]

Source: Dell'Oro. Note: Excludes NICs, Pluggables/Optics, and Cables

## Growth Driven By Multiple Vectors

Clusters getting bigger. Last year, our primer noted the emerging opportunity as scale-up moved from 8 GPU's to full rack at 72 GPU's with Blackwell. However, with Vera Rubin

noting 144 GPU's in a scale-up cluster and 576 with Rubin Ultra (and a potential doubling of that with Feyman), the cluster sizes and need for scale-up connections have increased materially. This is true not only in the NVDA ecosystem, but in Google's TPU and AMZN's Tranium ecosystem as well.

Exhibit 4: Increase in Scale-Up Networking TAM / Complexity In Large Part Due to Increase in XPU's in the Cluster (NVDA Example Below)


Source: MS estimates.

Hitting limits with copper reach as trying to involve more accelerators. Copper has traditionally been preferable in data center architectures, given it is cheaper, more reliable (electrical vs. optical signals), and uses less power. However, the speeds of AI networks are beginning to push the limitations of copper (see below).

We would note that the funeral for copper has been delayed multiple times as innovations have helped extend the life of copper, namely: PAM4, allowing more bits to travel, more powerful digital signal processors (DSPs), allowing for greater signal correction, and retimers, that help with weakening electrical signals, improved connectors / packaging.

Looking forward, the main debate today is whether copper's life can further be extended with 448G SERDES, PAM6 modulation, 200G retimers, etc. Broadcom has demonstrated next-gen technologies that still extend copper to 6m lengths, challenging NVDA focus on CPO for cross-rack connectivity with Vera Rubin Ultra.

Exhibit 5: Reach is Primary Challenge of Copper


Source: Semivision.

The bottleneck has shifted to I/O. While AI accelerators have seen remarkable improvements in computational performance over the past decade, the limiting factor for large-scale AI systems is increasingly shifting toward data movement. Modern AI training and inference require thousands of GPUs to operate as a single distributed system, meaning overall performance depends not only on the speed of individual accelerators but also on how efficiently they communicate with one another. As compute capability continues to outpace improvements in networking and memory subsystems, the industry is experiencing a transition to a connectivity bottleneck.

Exhibit 6: Compute capabilities outpace connectivity

[[KC_IMAGE_004]]

Source: Gholami et al. 2024, MS

The fundamental challenge is that communication distances are increasing while electrical reach is shrinking. Every new generation of AI accelerators increases I/O speeds, with SerDes lane rates progressing from 100G today toward 200G and eventually 400G. While these higher signalling rates deliver substantially greater bandwidth, they also reduce the distance over which electrical signals can travel while maintaining signal integrity. At the same time, AI clusters continue to expand in scale, with scale-up domains growing from traditional 8-GPU servers to 72-GPU racks with NVIDIA Blackwell, 144-GPU systems with Vera Rubin, and potentially more than 1,000 accelerators in future architectures. The result is a fundamental engineering challenge: the physical distances over which GPUs must communicate are increasing at precisely the same time that higher signalling speeds make long-distance electrical communication increasingly difficult.

Exhibit 7: Data Center Switch Revenue by port Speed

[[KC_IMAGE_005]]

Source: 650 Group

## How We View the Architecture Progression

Copper where you can, optics when you must. Copper interconnects remain the preferred medium for short-reach connectivity because they provide the lowest latency, lowest power consumption and lowest cost. However, as signalling speeds increase, electrical losses, insertion loss and noise become progressively more difficult to manage, requiring increasingly sophisticated SerDes, digital signal processors, retimers and equalization techniques simply to preserve signal integrity. This phenomenon is often referred to as the industry's "copper wall."

In our view, copper's longevity continues to be underestimated. While higher signalling speeds are undoubtedly making electrical transmission more challenging, successive innovations including more capable SerDes, improved connectors, retimers and active copper technologies have consistently extended copper's useful life beyond expectations. We continue to expect direct-attached copper to remain the preferred solution for intra-rack scale-up connectivity for several more product generations before a broader transition to optical technologies becomes necessary.

We expect a meaningful transition to optical interconnects in scale-up no earlier than 2028. While optics offers clear advantages in bandwidth density and reach, the cost premium remains significant and the supply chain is still maturing. In our view, adoption will be driven less by incremental increases in signalling speeds and more by architectural changes in AI infrastructure. As scale-up domains extend beyond a single rack, copper requires increasingly complex SerDes and signal conditioning to maintain performance, driving higher power consumption and lower efficiency. We see the key catalysts for optical adoption as: (1) multi-rack scale-up architectures, (2) rising electrical I/O power consumption, (3) increasing bandwidth density requirements, and (4) continued growth in bandwidth demands from larger, more communication-intensive AI workloads. These trends should increasingly favor near-package and co-packaged optical solutions over time.

XPU vendor roadmaps. NVIDIA is expected to lead the industry's transition to optical scale-up interconnects. We expect Rubin Ultra (2027) to represent an intermediate step, with GPUs within each 72-GPU rack remaining interconnected via copper NVLink while optical links connect multiple racks into a larger 576-GPU NVLink domain. This hybrid

approach preserves copper's cost and latency advantages for short-reach communication while deploying optics only where longer distances make electrical interconnects increasingly challenging. We expect Feynman (2028) to mark the first meaningful deployment of fully optical scale-up connectivity as NVLink domains expand to 1,152 GPUs. Checks point to limited deployment of Rubin Ultra with CPO, making Feynman, more likely scaling in 2029 as the adoption catalyst for CPO.


Exhibit 8: CPO Penetration in Scale-Up Likely Takes to 2029 to be Material

[[KC_IMAGE_006]]

Source: Dell'Oro.

Exhibit 9: Primarily Scale-Out Opportunity Until 2029

[[KC_IMAGE_007]]

Source: Dell'Oro. Note: Excludes NICs, Pluggables/Optics, and Cables

## What are the Interconnect / Fabric solutions?

Scale-up Fabric Ecosystem:

\- NVLink (NVIDIA): NVIDIA's proprietary scale-up interconnect used across GB200/GB300 and future Vera Rubin systems. NVLink delivers the highest bandwidth and lowest latency for GPU-to-GPU communication and remains the dominant scale-up fabric given NVIDIA's leadership in AI accelerators. The trade-off is a closed ecosystem available only with NVIDIA GPUs.

\- NVLink Fusion (NVIDIA, Marvell, Astera Labs and partners): An extension of NVLink that enables third-party CPUs, XPUs and custom ASICs to connect into the NVIDIA ecosystem. Rather than replacing NVLink, Fusion expands NVIDIA's addressable market by allowing hyperscalers to build semi-custom AI systems while remaining compatible with NVSwitch. Partners include Marvell, Astera Labs, MediaTek, Alchip, Synopsys, Cadence, Fujitsu and Qualcomm

\- SUE / ESUN (Broadcom, Marvell, broader Ethernet ecosystem): Ethernet-based scale-up networking designed to bring the openness and ecosystem benefits of Ethernet to rack-scale AI. Broadcom's Scale-Up Ethernet (SUE) leverages Tomahawk switch silicon, while the broader ESUN initiative is being developed through the Open Compute Project with support from Broadcom, Marvell, AMD, NVIDIA, Cisco, Meta, Arista, Arm, and others.

\- PCIe (Astera Labs, Broadcom, Marvell): The incumbent server interconnect used for CPU-GPU and device connectivity that is increasingly being extended into AI scale-up through PCIe fabric switches. Astera's Scorpio P and Scorpio X target this opportunity today, particularly for Amazon Trainium and other custom AI platforms. We view PCIe as a bridge technology before native AI fabrics become broadly available.

\- UALink (AMD-led consortium; Astera Labs, Marvell and others): An open, memory-semantic interconnect purpose-built for AI scale-up. Backed by the hyperscalers, AMD, Astera Labs, Marvell and other industry partners, UALink is designed to become the leading open alternative to NVLink. The UALink specifications have now been ratified, including the recently announced UALink 2.0 update, but commercial silicon and broad deployments are still expected from 2027 onward.

2026: The Market Begins to Broaden. As expected, 2026 marks the beginning of the non-NVIDIA scale-up opportunity. While NVLink continues to dominate given NVIDIA's accelerator share and leadership in switched scale-up architectures, alternative XPUs are beginning to create meaningful opportunities for third-party networking vendors. The emergence of alternative XPUs creates a greenfield opportunity for networking suppliers outside of NVIDIA's proprietary NVLink ecosystem. While NVIDIA will continue to capture the majority of scale-up spending through NVLink, we see significant opportunity across AMD, AWS Trainium and the growing custom ASIC ecosystem, where networking standards remain in flux and multiple suppliers can participate.

Exhibit 10: MS Accelerator Unit Share Estimates

Accelerator Unit Share 2026 Estimate


[[KC_IMAGE_008]]

Source: MS

The clearest non-NVIDIA beneficiaries in 2026 are Astera Labs and Broadcom. Astera is supplying the PCIe-based scale-up switch for AWS Trainium 3 through Scorpio-X, which has begun shipping and should ramp more meaningfully in 2H26. We view this as an important bridge ahead of native UALink. Broadcom is also well positioned through AMD's MI400/Helios platform, where AMD is using UAL tunneled over Ethernet with Broadcom's Tomahawk switch silicon.

Looking into 2027, we expect the non-NVIDIA scale-up ecosystem to further take shape. The main paths are Ethernet, UALink, and NVLink Fusion, with PCIe likely remaining a transitional solution. The key debate is which protocol customers will use. We expect adoption to be determined by technical performance, software and ecosystem support, and the strategic partnerships underpinning each XPU platform.

Based on our XPU forecasts, we expect PCIe to remain the largest non-NVIDIA scale-up fabric in 2027, while Ethernet should be the fastest-growing. PCIe's lead reflects Trainium, which we expect to be the largest switched non-NVIDIA ASIC platform next year. Ethernet should begin to establish a more meaningful presence in scale-up through the ramp of AMD's MI400/Helios platform, initial Broadcom-enabled ASIC deployments and early adoption of Microsoft's Maia. Broadcom and Marvell are well positioned as Ethernet switch suppliers. PCIe should also continue to grow rapidly, supported by Trainium 3 and broader adoption of PCIe/custom fabrics globally, benefiting Astera Labs, which has noted more than ten customers engaged on its Scorpio scale-up platform. NVLink should continue growing alongside NVIDIA accelerator shipments, although at a more modest rate given its already dominant base.

Exhibit 11: Switched Fabric Protocol Share

[[KC_IMAGE_009]]

Source: MS
Note: We estimate share using our XPU unit estimates. We assume MI400, MSFT Maia and AVGO XPU customers use Ethernet

UALink remains a key swing factor in the non-NVIDIA ecosystem. While the UALink specifications have now been ratified, the key gating factor is commercial silicon and switch availability. If native UALink switches arrive on schedule and are performant, we think it's possible that AMD and AWS could be among the earliest adopters, creating a meaningful opportunity for Astera Labs and Marvell. If UALink slips or customers prefer another protocol, Broadcom's Ethernet-based approach and NVIDIA's NVLink Fusion ecosystem should gain share. Ultimately, we view PCIe as a transitional fabric. While PCIe deployments should continue growing over the next several years, we believe hyperscalers will eventually migrate toward open, purpose-built AI fabrics. Whether that is UAL or Ethernet is still a debate.

## NVLink Fusion represents NVIDIA's strategy for extending its ecosystem beyond

NVIDIA GPUs. It enables third-party CPUs, XPUs and custom ASICs to connect directly into NVLink. Both Astera Labs and Marvell are ecosystem partners, positioning them to benefit if adoption accelerates. Marvell's recently announced strategic partnership with NVIDIA further reinforces its positioning as a key AI connectivity partner. For Astera, the opportunity comes through a protocol translation chip that sits alongside each XPU and converts its native protocol into NVLink. Unlike Scorpio-X, which is shared across multiple accelerators, the NVLink Fusion chip attaches one-to-one with each XPU, creating a different economic model with lower ASPs but substantially higher attach rates. Management has indicated that the content opportunity is broadly comparable to Scorpio-X, despite the different architecture. Based on current announcements, we think AWS will be pursuing a dual-track strategy for Trainium 4, supporting both UALink and NVLink Fusion. Our thinking for now is this will probably remain a more niche solution for the ecosystem overall, but is certainly additive to NVIDIA - and is something that could lead to higher NVDA GPU adoption if ASICs fall short.

2028: The Market Opens Up. The ramp of AMD MI-series platforms, AWS Trainium, Microsoft Maia and Broadcom-enabled ASICs, and others should materially expand the addressable market outside NVIDIA. We continue to see significant runway for Ethernet, particularly as Broadcom's ASIC customers ramp and adopt Ethernet-based scale-up solutions. UALink represents the largest source of upside for Astera Labs and Marvell. If the standard is commercially ready and broadly adopted across AMD, AWS and other custom XPUs, it has the potential to become the leading open alternative to NVLink. However, we believe the market remains far from settled, with customers likely to evaluate UALink, Ethernet and NVLink Fusion in parallel before converging on a preferred architecture. Google remains the architectural outlier. Its TPU architecture relies on ICI and OCS-based torus topologies rather than traditional switched scale-up fabrics. Whether this ultimately proves advantageous as AI clusters continue to scale remains an important question.

The non-NVIDIA ecosystem remains largely undecided. Over the next two years, architectural decisions made by hyperscalers and ASIC customers will determine which fabrics emerge as industry standards, creating a significant greenfield opportunity for Broadcom, Marvell and Astera Labs.

Exhibit 12: Non-NVLink Fabrics Set to Grow Rapidly, but the Market Mix Remains in Flux


[[KC_IMAGE_010]]

Source: Dell'Oro, MS.

## What are the Transmission Approaches As Industry Eventually Hits "Copper Wall"?

Co-packaged optics (CPO) is emerging as a critical architectural shift for AI datacenter networking, driven by the rising power, bandwidth, and density constraints of traditional pluggable optical modules. AI clusters require massive scale-out connectivity across racks, but today's switch architecture forces high-speed electrical signals to travel 15 to 30 centimeters across a circuit board before reaching front-panel optical modules. As speeds rise, those electrical signals degrade more quickly, requiring more advanced DSPs, retimers, and correction circuitry to preserve signal integrity. CPO addresses this constraint by moving optical engines into the same package as the switch ASIC, reducing the electrical path to only a few millimeters and enabling lower-power short-reach SerDes, simplified signal processing, and higher front-panel bandwidth density.

Reduced interconnect power is the most tangible near-term benefit, with CPO potentially lowering optical interconnect power consumption by roughly 50-80%, while also freeing front-panel space and reducing reliance on discrete optical modules. Adoption also shifts value toward suppliers with control over optical engines, silicon photonics, external lasers, and advanced packaging, given the need to precisely integrate electronic chips, photonic chips, fiber arrays, lasers, and thermal management. Key participants include Broadcom and NVIDIA in switch platforms, Lightmatter, Ayar Labs, Marvell/Celestial AI, and POET in optical engines and photonics, TSMC, GlobalFoundries, and Tower in silicon photonics foundry capacity, and Lumentum, Coherent, and Sivers in laser supply.

Source: Broadcom
Exhibit 13: CPO brings the optical engine next to the ASIC, reducing interface losses and shortening the electrical path

[[KC_IMAGE_011]]


Exhibit 14: CPO Will First Start at 2.5D CPO, But Eventually Evolve Towards Full 3D CPO, Likely 2030 and Beyond

[[KC_IMAGE_012]]

Source: Fibermall.

Near-packaged optics (NPO) sits between pluggables and CPO, moving the optical engine close to the switch or GPU ASIC while keeping it outside the ASIC package. For optical suppliers such as LITE and COHR, the NPO opportunity is centered on selling the core optical building blocks needed to replace copper links at 1.6T and 200G-per-lane, including high-power CW lasers, external laser source modules, InP-based laser content, 200G VCSEL-based solutions, and potentially more integrated optical engine content. Customer interest appears strongest among non-NVIDIA-class architectures that need to solve copper reach, power, and signal integrity constraints but may not yet be ready to accept the tighter vendor coupling and manufacturing complexity of full CPO. Compared with CPO, NPO offers a more open and serviceable architecture because optics can remain socketed or separately sourced from the GPU / XPU or switch silicon, limiting lock-in risk and preserving a broader merchant optical ecosystem. Performance and power efficiency likely sit below full CPO but materially above front-panel pluggables, making NPO a

credible intermediate architecture and a potentially attractive near-term demand driver for optical component vendors as scale-up networking moves increasingly toward optical connectivity.

Exhibit 15: NPO moves the optical engine near the compute package, improving reach and efficiency while preserving a more serviceable / open architecture / ecosystem than CPO


[[KC_IMAGE_013]]

Source: Cisco.

Exhibit 16: NPO decouples the optical engine from the switch chip and then assembles them on the same system board


[[KC_IMAGE_014]]

Source: Fibermall.

Active copper cables occupy the middle of the data center interconnect spectrum, sitting above passive DACs and below optical solutions in reach, power, and cost. Two architectures matter for investors, with AECs using retimers, equalization, and clock data recovery to restore signal integrity across longer copper links, while ACCs use a lower-power redriver approach that amplifies the analog signal but has less ability to remove jitter. AEC is currently the dominant active copper configuration because it offers stronger signal integrity, with typical reach of roughly 7 to 9 meters and support for intra-rack and rack-to-rack AI connectivity, while ACC is more focused on shorter intra-rack links of roughly 3 meters where very low power and latency are the priorities. Investor relevance is tied to AI cluster architecture, where copper remains attractive for short-reach scale-up and selected scale-out links because it can deliver better reliability, lower power, and lower total cost of ownership than laser-based optical modules when distance

requirements are manageable. AECs can reduce interconnect power by roughly 50% versus pluggable optical transceivers, are materially smaller and lighter than passive DACs, and are gaining traction as clusters scale from 400G to 800G, with 1.6T commercialization becoming the next step. At 200G per lane, reach likely compresses from roughly 7 meters toward closer to 5 meters, but the value proposition can strengthen because higher speeds increase the need for signal conditioning and drive ASP uplift for active cable silicon. Adoption also appears increasingly broad across hyperscalers and NeoClouds, with active copper becoming a standard option for dense in-rack and multi-rack deployments where customers want to avoid the cost, power, and operational complexity of optics. From a stock perspective, active copper should be viewed as complementary to LPO, NPO, and CPO rather than directly competitive, as AI data centers are likely to use a heterogeneous mix of interconnects based on reach, power budget, latency, reliability, and serviceability. Optical will remain essential as distances increase and scale-up domains expand across racks, but active copper should retain an important role inside the rack and near-rack environment, supporting vendors exposed to retimers, redrivers, cable assemblies, and validated active cable platforms.

Exhibit 17: ACC prioritizes efficiency inside the rack, while AEC extends reach at higher power and latency

## Active Copper Cable (ACC)


[[KC_IMAGE_015]]


\- Pure analog solution

\- Extreme low cost, power, latency

\- <2m copper for inside rack ■ High performance at cost of power, latency


[[KC_IMAGE_016]]


\- <5m reach at 1.6T

Enabled by ACC product offerings

Enabled by AEC DSP product offerings

Source: Marvell

OCS, or optical circuit switching, is a higher-efficiency optical networking layer for AI clusters, routing light directly from one port to another rather than relying on EPS, or electronic packet switching, which converts traffic into electrical signals for processing inside traditional switch silicon. Investor relevance centers on lower power, lower forwarding latency, and better long-term upgrade economics, since an OCS can often support higher link speeds over time without requiring a full switch silicon refresh. Adoption is most compelling in AI training environments where traffic patterns are relatively predictable, making OCS a good fit for scale-up pods, upper layers of scale-out networks, and large inter-data-center transfers where bandwidth, power, and network

TCO matter more than ultra-fast packet-by-packet reconfiguration. Within OCS, micro-electro-mechanical systems, or MEMS, is the most mature architecture today and uses tiny movable mirrors to steer light between ports; the advantage is faster switching versus liquid-crystal alternatives, lower insertion loss, and earlier volume readiness, which makes MEMS better suited for near-term hyperscale deployments. Liquid crystal on silicon, or LCoS, takes a different approach by using voltage-controlled liquid crystal to change how light is directed through the switch; its main advantage is longer expected service life, which can improve ownership cost over time, but switching latency is slower and manufacturing still requires precise optical alignment. Waveguide-based OCS and piezoelectric OCS are more future-oriented approaches, with waveguide designs offering faster switching potential but currently facing higher insertion loss and cost, while piezoelectric designs offer very low insertion loss but remain expensive and less mature. For optical suppliers, the key point is that OCS expands the revenue opportunity beyond transceivers and CPO light sources into higher-value systems and precision optical content, including MEMS mirrors, LCoS switching elements, collimator arrays, calibration systems, beam displacers, and other optical assemblies. LITE appears more levered to MEMS-based OCS, while COHR is more relevant to LCoS-based OCS and broader precision optical content. Demand is still concentrated and execution-heavy, but OCS should be viewed as a complementary growth vector alongside pluggable optics, NPO, and CPO, giving optical suppliers another path to monetize AI networking growth as customers optimize for power, latency, upgrade flexibility, and total cost of ownership.

Exhibit 18: Google's Palomar OCS highlights its leadership in bringing optical circuit switching from lab architecture to production-scale data center networks


[[KC_IMAGE_017]]


## Common Questions / Debates

Is the biggest hurdle to CPO the technology or just not wanting to be locked into a proprietary ecosystem? There are a few considerations here: 1) Vendor lock-in, 2) Cost, 3) Feasibility. We would note the cost / feasibility points have traditionally ranked above vendor lock-in, but as we near CPO solutions, that has become more significant. The copper and optical transceiver ecosystems (for scale-out in the case of optical transceivers) are diversified, and while supply chains have remained tight, produce far

lower margins than XPU vendors today. As a result, concentrating more of the economics into the XPU vendor has generally been viewed unattractively. Additionally, with packaging ecosystem needing to come together, the second biggest consideration has been feasibility and whether the risk / reward of adoption works (e.g. Google has often commented that power savings are not worth the additional quality / failure risk).

Can CPO be avoided longer term? While we left OFC this year noting that there was meaningful resistance from the hyperscalers to CPO, NVDA's promotion of CPO with the Spectrum-6 switch as part of their Vera Rubin Ultra design introductions kept investors encouraged on the prospects. We would note, that do the extent that cluster sizes are not important, you can push out CPO adoption for a very long time. Additionally, if just passing elephant flows around, OCS can be a somewhat more reliable option (even if limited). However, if you 1) want to be able to scale XPUs in a cluster, 2) run into I/O problems, you will eventually need to move to optical vs. copper interconnects as you move towards cross rack clusters.

Is the scale-up Ethernet opportunity actually attractive for branded switching vendors? In general, given less complicated requirements within a scale-up network, as just transferring traffic within a GPU / XPU cluster, the switching needs are less complicated. The speed of the chips needs to be high, but the software can be more simplified. This lends itself to more simplified switching, which can largely be done by white / blue boxes. As a result, while there is a lot of volume in the scale-up Ethernet opportunity, we don't find it as attractive for branded vendors like ANET until we get to multi-rack solutions in the 2028+ period.

Do we need as big of scale-up clusters with inference or just with training? In general, the importance of the size of the scale-up cluster is more important with training vs. inference. Reason being, in training, every accelerator is working towards solving the same problem, with advanced synchronization and latency needs that can only be achieved in a scale-up cluster. However, frontier models still want 100+ XPUs for inference in the scale-up network, which as a result, will continue to advance the conversation on scale-up architectures, regardless of whether mix of workloads adjusts between training / inference.

## Does it matter if NPO / LPO / OCS to

higher level, no.
Incremental optical use cases in scale-up are a positive. There has been meaningful volatility in LITE, COHR, GLW and the rest of the co-packaged optics

Exhibit 19: Optical Content Increasing, Discussion Is More Around Timing

[[KC_IMAGE_018]]

Source: MS

(CPO) ecosystem over

the last couple of weeks as timing questions re-emerged. However, debating timeline of adoption misses that optical content is largely correlated to bandwidth needs – e.g., the more bandwidth, the more optics, whether that takes the form of co-packaged optics

(CPO), near-packaged optics (NPO), or other optical formats. While given commitments of capacity as part of NVDA's equity investments in LITE, COHR, GLW likely prevent just instantly swapping one set of demand for another, we do think that these three vendors remain beneficiaries of the increase in optical content, particularly as it enters the scale-up domain.

Exhibit 20: It Will Take Time, but Copper Eventually Reaches Limits within Scale-Up Networks


[[KC_IMAGE_019]]

Source: 650 Group.


[[KC_IMAGE_020]]


What about Amazon's Resilient Network Graph (RNG)? To give a basic description, Amazon noted in an academic paper over the last couple of weeks that they were deploying a new network architecture in most of their data centers that moves away from traditional architectures (e.g. fat tree or tiers of switching / routing) and moves towards a flatter, more mesh network, where adaptive routing and ShuffleBoxes help with traffic management. This network design requires significant adaptive routing / software expertise, a move away from recent history, where more networking has been added, but with more open source software. Given value of software work Amazon has done, and the proprietary nature of their network designs, we don't yet see major adoption beyond Amazon.

AWS's RNG (Resilient Network Graphs) architecture marks a material shift from conventional fat-tree data center networking, replacing a hierarchical fabric where traffic moves through upper aggregation layers with a flatter quasi-random graph designed to create broader path diversity across routers. Conventional fat-tree networks are easier to route but require additional router layers, can concentrate congestion near the top of the hierarchy, and create more fragility when important routers fail. RNG uses quasi-random connectivity, ShuffleBox passive optical components, and Spraypoint routing to make flatter networks practical at production scale, reducing router count by 69%, improving throughput by up to 33%, and projecting a 40% reduction in network equipment electricity consumption. Adoption has moved quickly from production validation to global default design, with AWS's first quasi-random production network going live near Dublin at the end of 2024, refined through two additional deployments, and becoming the default architecture for most new AWS data centers globally by April 2026. Moving from initial deployment to default architecture in about 18 months suggests a high level of confidence in the design and highlights how aggressively AWS is reworking the physical network layer to support AI-scale infrastructure.

Exhibit 21: Traditional fat-tree network topology (a) vs. AWS's flatter quasi-random graph topology (b)

[[KC_IMAGE_021]]

Source: Amazon Science Blog

## Stock Takeaways / CPO Adoption EPS Analysis

2026–2027: Copper is the story. The emergence of alternative XPUs creates a greenfield opportunity for networking suppliers outside of NVIDIA's proprietary NVLink ecosystem. While NVIDIA will continue to capture the majority of scale-up spending through NVLink, we see significant opportunity across AMD, AWS Trainium and the growing custom ASIC ecosystem, where networking standards remain in flux and multiple suppliers can participate (see What are the Solutions).

ALAB: Pure-play AI networking exposure; attention shifts from Scorpio to ecosystem breadth. We expect Scorpio to drive a strong 2H26 ramp, but investor attention is already moving toward UALink adoption and customer diversification beyond the initial hyperscaler programs. We continue to view Astera as one of the best pure-play exposures to AI connectivity and remain impressed by its ability to expand content per accelerator from roughly \$50–\$100 at IPO to more than \$1,000. Scorpio X is now shipping, providing the next major leg of content growth. The copper-to-optics transition is an important watch item, but we do not view replacement as imminent. Copper should retain meaningful intra-rack runway, while Astera builds its optical roadmap through their small acquisitions and organic development. Near-term execution remains centered on Scorpio and broadening the customer base; optics provides longer-term optionality rather than an immediate risk to the core thesis.

SMTC: A developing beneficiary of both copper longevity and linear optics. Semtech offers exposure to both sides of the connectivity transition. CopperEdge extends short-reach copper at up to 90% lower power than DSP-based AECs, supporting our view that copper remains viable longer than many expect. At the same time, FiberEdge and DirectEdge TIAs and drivers benefit from the move toward 800G, 1.6T and linear optical architectures. Semtech's components complement high-quality SerDes rather than competing with switch or DSP vendors, allowing the company to benefit as lane rates increase regardless of the underlying platform. The HieFo acquisition adds InP lasers and gain chips, expanding Semtech from analog front-end components toward a more complete optical chipset for 3.2T, NPO and CPO applications. Near-term upside depends on converting CopperEdge and FiberEdge design wins into revenue; longer term, HieFo could materially increase content per optical module and improve Semtech's strategic position in the supply chain.

AVGO: Scale-up networking is an underappreciated extension of the XPU opportunity. The Broadcom narrative remains centered on custom XPUs, but we see a sizable opportunity to pull through scale-up networking content alongside those wins. Because Broadcom designs the ASIC and owns a broad portfolio spanning Ethernet switches, PCIe, SerDes, NICs and optics, it is well positioned to bundle the surrounding connectivity architecture for its customers. This gives Broadcom an advantage as newer custom ASIC programs move from silicon development into rack-scale deployments. Broadcom is also a technology leader in CPO and next-generation switching, despite taking a conservative view on adoption. Management believes 200G, and eventually 400G, SerDes can extend copper within the rack, supporting our view that broad scale-up CPO adoption is more likely around 2028–29. Scale-out customers can adopt CPO earlier for power savings, but the economics may not yet justify a broad transition.

MRVL: Broad fabric optionality, with optics as the core differentiator. Marvell already has a leading position in scale-out optics and is positioning across all three potential scale-up paths: UALink, ESUN and NVLink Fusion. Its recently announced strategic partnership with NVIDIA reinforces Marvell's role in custom XPUs, scale-up networking and silicon photonics, while the Celestial AI acquisition adds a purpose-built photonic fabric for optical scale-up. Marvell's ability to support multiple fabrics limits dependence on any single standard, while Celestial AI provides a credible path toward leadership in merchant optical scale-up as the market transitions around 2028. The key debate is execution - integrating the acquired technology and converting its broad customer pipeline into volume deployments.

CRDO (NC) AEC leadership today, with optics emerging as a second growth engine. Credo remains one of the cleanest exposures to copper durability through its ZeroFlap AEC franchise. The current revenue base remains primarily scale-out, but Blue Heron gives Credo direct scale-up optionality across UALink, ESUN and Ethernet as those architectures begin to ramp. Credo's optical expansion also reduces the risk from an eventual copper-to-optics transition. The DustPhotonics acquisition, ZeroFlap optical transceivers and new optical DSP portfolio broaden the company's exposure across 800G, 1.6T and 3.2T connectivity. Management expects more than 80% FY2027 revenue growth and over \$600 million from optical products, making optics a meaningful second growth engine rather than simply a defensive hedge. The key watch item is execution across several new product categories while sustaining momentum in the core AEC business.

## APH (NC)

2028+: Optics becomes the opportunity. While timing of optics coming further into scale-up is up for debate, one where we believe the adoption will begin in '28, but be slow given production capacity with Ultra Rubin, the fact that optics will eventually come into scale-up is more fact. If you want to have larger GPU / XPU cluster sizes and you want to resolve eventual I/O bottlenecks, network builders will have to incorporate optics. As we move towards Feynman and Interposer architectures in 2029 and beyond periods, optics in scale-up becomes unavoidable.

Rebuilt LITE / COHR / GLW models sensitize for CPO adoption. While we previously had a

CPO line-item for LITE / COHR models, we have more accurately built these models to reflect CPO penetration percentages.

GLW: Cleanest architecture-agnostic way to play optical scale-up, with management explicitly framing 2028 as the likely starting point and expecting early adoption to look hybrid rather than a binary copper-to-optics transition. Passive photonics content across FAUs, PMF, ELS fiber and GlassBridge should remain relevant across 2D CPO, 2.5D CPO and NPO, while the company's support for open-reference architectures helps preserve ecosystem breadth even as optics moves closer to the package.

LITE: Levered to the optical engine and laser content required as scale-up bandwidth moves beyond what pluggables can efficiently support, with management calling NPO an intermediate step and CPO the likely next-generation convergence point. Scale-up optical shipments are expected to begin in late 2027, with products in market in early 2028, and management sizes the first scale-up opportunity at 3–4x initial scale-out CPO, with a much larger lane opportunity as optics moves inside the rack.

COHR: Broad exposure across the full CPO/NPO component stack, including high-power CW lasers, external laser source modules, FAUs, polarization-maintaining fiber, isolators and thermoelectric coolers. Management has been the most aggressive on scale-up sizing, describing the opportunity as orders of magnitude larger than scale-out, while its support for multiple architectures across InP, silicon photonics and VCSEL-based solutions positions the company to benefit regardless of whether customers move through NPO, 2D CPO or more advanced 2.5D CPO structures.

KEYS: Upgrading KEYS to OW as a play on AI investment and broadening architectures vs. a play on a particular architecture. KEYS sees over half of their revenue come from R&D / lab use cases, and has seen their AI revenue (mid-teens % of revenue) increase as not only have investment cycles shortened, but the variety of architectures has increased (e.g. Ethernet vs. Infiniband). Bottom line, customers are ramping 800G, accelerating 1.6T R&D, and already planning for 3.2T, while also optimizing for speed, power, density, scale-up networking, and scale-out architectures. We believe this concurrency matters because it raises test intensity, broadens the number of customer programs KEYS can serve, and reduces reliance on any single product cycle. Faster innovation cadence and greater system complexity should support a longer growth runway than investors typically assign to test and measurement. Given there will be a growing mix of all of these architectures, we prefer the play on the diversity of architectures vs. one particular (since architecture debate unlikely to be solved for multiple years). We see the path to achieving our PT through estimate revisions as testing density increases and incremental margins improve.

Exhibit 22: LITE: CPO Scale Out / Scale Up FY28 Adj. EPS Sensitivity


Source: Company data, MS

Exhibit 23: COHR: CPO Scale Out / Scale Up FY28 Adj. EPS Sensitivity


Source: Company data, MS

Exhibit 24: GLW: CPO Scale Out / Scale Up FY28 Adj. EPS Sensitivity


Source: Company data, MS

## Model Changes

Exhibit 25: LITE: Model Changes


Source: Company data, MS

Exhibit 26: COHR: Model Changes


Source: Company data, MS

Exhibit 27: GLW: Model Changes


Source: Company data, MS


[[KC_IMAGE_022]]


## Risk Reward – Lumentum Holdings Inc (LITE.O)

AI More Embedded Into Base Case, Greater CPO Adoption is Bull Case

## PRICE TARGET \$900.00

RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

[[KC_IMAGE_023]]

Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

\- Datacom positioning attractive, particularly with ramping customer sets, but questions remain on margin contribution and impacts to earnings power
- Key questions remain on magnitude and timeline of OCS ramp and length of EML shortage.

■ Upside to multiple likely limited by optical componentry being some of names most at risk from tariffs given intricate manufacturing that should be slower to move out of Asia, with LITE concentrated in Thailand


[[KC_IMAGE_024]]


## Risk Reward Themes

Secular Growth: Positive
View descriptions of Risk Rewards Themes here

## BULL CASE

\$1,125.00

## \~25x CY28 Bull Case Earnings Power (\~\$45)

CPO penetration greater than expected. LITE able to achieve \~\$45 in CY28 EPS in our bull case as multiple business lines ramp -- including CPO seeing far greater adoption in scale-up / out than expected in early days. Exert meaningful pricing pressure, which maintains through CY28. Multiple remains at premium given growth outlook, particularly on scale-up.

## BASE CASE

## \$900.00

## \~30x CY28 P/E (\~\$30)

Broad-based AI growth. Ramps to EMLs, Telco (DCI), transceiver, OCS and CPO business concurrently. Margin benefit from EML constraints and higher blend of EML / OCS/ CPO. Our multiple is a premium to historical trading range given AI capex spend.

## BEAR CASE

\$500.00

## 20x CY28 Bear Case Earnings Power (\~\$25)

Product lines have trouble ramping. OCS and CPO do not ramp to expectations on expected timeline. EMLs demand/supply reach equilibrium sooner than expected, pressuring margins. More signs that EMLs will lose share to CW (Silicon Photonics). Multiple trades closer to traditional ranges.

## Risk Reward – Lumentum Holdings Inc (LITE.O)

## KEY EARNINGS INPUTS


## INVESTMENT DRIVERS

• Opportunities like 3D sensing still in early days

• ROADMs in early days of deployment in China

\- Position as a consolidator as leverage levers more reasonable

## GLOBAL REVENUE EXPOSURE


[[KC_IMAGE_025]]


[[KC_IMAGE_026]]

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS


Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

• Datacom ramps and revenue mix more attractive vs. expectations

\- OCS ramps quickly, bringing additional revenue / profitability source

\- AI demand remains strong, causing EML business to outperform and drive profitability

## RISKS TO DOWNSIDE

\- EML pricing falls given oversupply on reduced AI demand

• CW takes share from EML

• Cloud Light hurts ability to improve margins

• Industrial demand falls on macro

## OWNERSHIP POSITIONING


Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).


[[KC_IMAGE_027]]

◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

## Risk Reward – Coherent Corp (COHR.N)

Street Building In Material Margin Improvement as Capacity Comes Online

## PRICE TARGET \$330.00

\~28-30x Base FY28e EPS (\~\$11.50). Multiple trades at premium to historical trading range given AI exposure, trading more in-line with AI comps.


Source: Refinitiv, MS


[[KC_IMAGE_028]]


## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

\- Near-term AI/ML opportunity and potential earnings optionality as net interest expense is worked down
- Valuation reflects volatility in end demand, particularly against more challenging Analyst Day targets
- Several levers to improve earnings power, including gross margin improvements and debt reduction
- Believe in longer term growth opportunity given attractive focus on differentiated processes and diversified customer base, with meaningful exposure to AI opportunity


## Risk Reward Themes


View descriptions of Risk Rewards Themes here

## BULL CASE

## \$450.00 BASE CASE

## \~30x Bull Case CY28 Earnings Power of (\~\$15)

Multiple sees expansion if company able to gain share in datacomm; expand margins north of 42%. EPS power accounts for COHR executing on self-help story, and able to raise operating margins on the business. Able to participate more meaningfully in CPO / OCS.

## \$330.00 BEAR CASE

## \~28-30x Base Case FY28 Earnings Power of \~\$11.50

Spending trajectory healthy, but multiple capped by volatility of space. Giving more credit in earnings power for Analyst Day targets. However, given volatility in end markets, capping multiple at historical averages. Earnings power closer to \~\$11.50 and multiple trades at a premium to historical trading levels given AI exposure.

\$160.00

## 16x Bear Case FY28 EPS of \~\$10

See deterioration in pricing as too much capacity comes along. COHR is unable to execute on vision laid out at Analyst Day, limiting changes to interest expense or margin profile. Little earnings growth from FY27, causing multiple to trade slightly above 5-year minimums on the name.

## Risk Reward – Coherent Corp (COHR.N)

## KEY EARNINGS INPUTS


## INVESTMENT DRIVERS

• What is the risk of China insourcing?

\- Can 3D sensing still be an attractive market for COHR?

\- Can COHR get larger than expected synergies out of Coherent?

\- Can datacomm components capture outsized opportunity with AI?

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS


Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

\- Interest expense worked down given exit businesses or accelerated delevering

\- Pricing increases help gross margins - 1.6T AI opportunity ramps faster than expected, benefitting margins

\- Recovery in non-datacomm portions of business

## RISKS TO DOWNSIDE

\- Macro headwinds or pricing increases difficult to achieve given tariffs

• SiC market competitive

• AI build out pause, catalyzed by DeepSeek

• Competitive pressures in datacomm

## OWNERSHIP POSITIONING


Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

## Risk Reward – Keysight Technologies Inc (KEYS.N)

Architecture-Agnostic Play on AI

## PRICE TARGET \$400.00

Our base case valuation reflects \~33x on FY27 Base Case EPS of \~\$12. Tariff impact removed, allowing stock to trade closer to 2x P/E/G.


Source: Refinitiv, MS


## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## OVERWEIGHT THESIS

■ Architecture optionality is the core AI thesis. KEYS benefits as AI networks evolve across Ethernet, InfiniBand, copper, pluggables, LPO, NPO and CPO, with more architectures driving more test demand.
■ AI upside with lower volatility. AI revenue is scaling quickly, but KEYS also has durable support from A&D, semiconductor test and wireless, reducing reliance on one capex cycle.

■ Better growth converting into better margins. Backlog conversion, higher test density, software mix and acquisitions should support continued estimate revisions and operating leverage.

Source: Refinitiv, MS

## Risk Reward Themes

New Data Era: Positive
Secular Growth: Positive

View descriptions of Risk Rewards Themes here

## BULL CASE

## \~38x Bull Case FY27e Earnings power (\~\$13)

## \$500.00 BASE CASE

AI opportunity becomes more meaningful than expected, with demand recovery accelerating, driving to 20%+ EPS growth. Bull case earnings power of \~\$13 reflects that the company can consistently grow double digit on the top line, allowing EPS growth to near high teens. Based on multi-year cycles in wireless and A&D. Continues to trade closer to 2x P/E/G, in-line with historicals, but on higher EPS growth.

## \~33x FY27 Earnings Power (\~\$12)

## \$400.00 BEAR CASE

Broad-based strength across AI data center, 6G, A&D and semiconductor test supports above-model growth, while higher testing density and stronger mix drive healthy incremental margins. Valuing KEYS at 33x our \$12 EPS estimate yields a \$400 base case, consistent with a mid-teens EPS growth profile and an implied PEG of roughly 2x.

\$220.00

## \~20x Bear Case FY27 Earnings Power (\~\$11)

AI architecture uncertainty slows deployment and limits test density upside, while AI growth normalizes before A&D, semi and wireless can drive enough offsetting strength. Higher capex intensity and discounting to gain share weigh on margins, pushing the stock back toward cyclical T&M multiples.

## Risk Reward – Keysight Technologies Inc (KEYS.N)

## KEY EARNINGS INPUTS


## INVESTMENT DRIVERS

5G Investment, R&D Budgets

## GLOBAL REVENUE EXPOSURE

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS


Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

\- 6G spend begins sooner than expected

• AI demand broadens across portfolio

• A&D investment steps up materially globally

\- Spirent accretive

## RISKS TO DOWNSIDE

\- Elongated macro/demand headwinds, limits wireless/EISG recovery

• Acquisitions falter

\- Limited opex leverage as supply chain expenses pickup

## OWNERSHIP POSITIONING


Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

Mean MS Estimates Source: Refinitiv, MS

## Risk Reward – Corning Inc (GLW.N)

Exp'd Margin Leverage and Scale-Up Opportunity Driving Stock Towards Bull Case

## PRICE TARGET \$180.00

Our base case valuation reflects \~35x on FY28 Base Case earnings power of \~\$5.1. Our multiple represents a premium to GLW's traditional trading range over the last 10 years given AI megatrend.

## Consensus Price Target Distribution

Source: Refinitiv, MS


## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

■ Display business, which generates majority of earnings, operates efficiently. Additional currency related price increases support margins.

■ Optical business sees resumption in growth as carrier fiber deployments pick up, and also benefits from AI datacenter demand for fiber.

■ Consumer businesses see slow recovery, particularly given weaker macro


## Risk Reward Themes

Pricing Power: Positive
Secular Growth: Positive
View descriptions of Risk Rewards Themes here

## BULL CASE

## \~35x 28e MSe Bull Case Core EPS (\$6.5)

\$230.00

Upside to estimates driven higher margins / CPO adoption than expected; solar margins improve meaningfully. Our Bull Case reflects meaningful upside to Springboard and greater recognition of Solar / CPO/photonics opportunity, with a greater pass through of margins as Solar overhang quickly dissipates, CPO adoption greater than expected. Also gives credit for upside from unknown US manufacturing project. Premium to historical trading range given AI opportunity.

## BASE CASE

## \$180.00

## \~35x 28e Base Case Earning Power

Continues to see upside to optical demand; CPO material by 2028. GLW remains well exposed to various LT secular trends, with fiber pass through to margins being slightly better than expected. In this scenario, FY28e core EPS seen at \$5.1. Our multiple represents a premium to GLW's traditional trading range over the last 10 years given accelerated growth and AI opportunity.

## BEAR CASE

\$72.00

## \~16x Bear Case 28e EPS (\$4.5)

Slowdown in AI spending. Broadly speaking, growth challenged given macro headwinds, particularly in consumer exposed businesses; AI spend curtailed as bottlenecks or spending caution emerges. In this scenario, FY28e core EPS seen at \$4.5. Multiple of 16x is closer to GLW's average trading range since 2010.

## Risk Reward – Corning Inc (GLW.N)

## KEY EARNINGS INPUTS


## INVESTMENT DRIVERS

\- Optical fiber deployments from service providers

• Consumer spending (mobile devices, TVs)

\- Incremental adoption of core technologies (glass, ceramics, optical physics) across more end markets / verticals (i.e. auto glass)

## GLOBAL REVENUE EXPOSURE

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS


Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

• Acceleration in AI capex data points continue

\- Margins improve on fiber business as enter more into data center opportunity

• CPO adoption greater than expected

• Solar overhang on wafers quickly dissipates

## RISKS TO DOWNSIDE

\- Delay in fiber deployment / AI plans

• Alternatives to CPO found in scale-up

\- Macro disruption challenges pricing / margins, cash flow generation

\- Pricing discipline dissipates in display

## OWNERSHIP POSITIONING


Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

- Mean
- MS Estimates
Source: Refinitiv, MS

## Risk Reward Reference links

1. View explanation of Options Probabilities methodology -

Options\_Probabilities\_Exhibit\_Link.pdf

2. View descriptions of Risk Rewards Themes - RR\_Themes\_Exhibit\_Link.pdf

3. View explanation of regional hierarchies - GEG\_Exhibit\_Link.pdf

4. View explanation of Theme/Exposure methodology -

ESG\_Sustainable\_Solutions\_External\_Link.pdf

5. View explanation of HERS methodology - ESG\_HERS\_External\_Link.pdf
