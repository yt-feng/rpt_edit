<table><tr><td colspan="2">TELECOM &amp; NETWORKING EQUIPMENT</td></tr><tr><td>North America</td><td></td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

# Bringing More Light to Scale-Up Networks: An Updated Scale-Up Primer

## WHAT'S CHANGED

<table><tr><td>Keysight Technologies Inc (KEYS.N)</td><td>From</td><td>To</td></tr><tr><td>Rating</td><td>Equal-weight</td><td>Overweight</td></tr><tr><td>Price Target</td><td>$350.00</td><td>$400.00</td></tr></table>

The scale-up market is set to be a \~\$70bn opportunity by 2030, over 4x the size estimated a year ago, as capex and cluster sizes grow. We explore recent debates/technology evolutions, with conclusion being copper is likely to remain for longer, but CPO is eventual, making recent sell-offs overdone.

Architectures in flux as scale-up network grows. As AI models grow in complexity and scale, the demand for high-performance computing infrastructure has surged, with \$70bn+ opportunity estimated over 4x the estimate we put forth last year. The scale-up network is critical because it allows accelerators to operate as a single system, eliminating communication bottlenecks and enabling the scale, speed, and efficiency required to train today's frontier AI models. With such a large opportunity, there are multiple different architectures being contemplated, from the interconnect fabric (NVLink, UAL, SUE) to the transmission technology (many forms of copper and optical interconnect). Given the concentration of buyers, adoption of any of these technologies creates meaningful opportunity, and we do not expect uniformity in approaches.

Copper to remain for longer, but optics in scale-up will happen. Copper remains the favored transmission technology in scale-up, given latency, power consumption, cost and openness of ecosystem. However, as signalling speeds increase, electrical losses, insertion loss and noise become progressively more difficult to manage, requiring increasingly sophisticated SerDes, digital signal processors, retimers and equalisation techniques simply to preserve signal integrity. As scale-up domains extend beyond a single rack, copper requires increasingly complex SerDes and signal conditioning to maintain performance, driving higher power consumption and lower efficiency. As a result, we see the key catalysts for eventual optical adoption in scale-up: (1) multi-rack scale-up architectures, (2) rising electrical I/O power consumption, (3) increasing bandwidth density requirements, and (4) continued growth in bandwidth demands from larger, more communication-intensive AI workloads. These trends should increasingly favor near-package and co-packaged optical solutions over time, with adoption strongest in scale-up in the 2029 and beyond period (we do see small adoption in 2028). We do not see 2028 introductions as delayed, but we do not see more meaningful adoption of CPO until Feynman generation of NVDA technology.

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Meta A Marshall</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Meta.Marshall@morganstanley.com</td><td>+1 212 761-0430</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr><tr><td colspan="2">Antonio Jaramillo</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Antonio.Jaramillo@morganstanley.com</td><td>+1 212 761-4438</td></tr></table>

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

We remain constructive on scale-up networking semis, where XPU proliferation creates a greenfield opportunity across switching, copper and optics. NVIDIA is our Top Pick in semis and we are also positive on Broadcom ahead of its 2027–28 ASIC ramps and the associated networking pull-through. We remain OW Astera as a leading pure-play beneficiary and are excited for the ramp of Scorpio, UALink and optics, though valuation is high at this point. We expect Marvell to gain scale-up share but remain sidelined on valuation and limited XPU visibility, while Semtech offers attractive copper and linear-optics exposure but still needs to prove execution. Overall, we see positive structural tailwinds across the group given the size of the opportunity, with ratings driven more by valuation and execution record.

We have rebuilt our LITE / COHR / GLW models to incorporate Co-packaged optics (CPO) adoption percentages and see next catalyst for optical as OCP in October; upgrading KEYS on thesis that it will be a beneficiary from diversity of architectures. GLW, LITE, COHR are the clearest beneficiaries of the eventual move of optical into the scale-up domain (evidenced by NVDA investments). We think Q2 earnings may not be a material catalyst given current supply constraints and concerns around delays / smaller adoption of CPO in 2028 (which has caused recent underperformance). However, we think the catalyst for enthusiasm about CPO will be OCP in October, meaning we would be more constructive on the names coming out of earnings and into that event. In terms of actionability now, we upgrade KEYS to OW (see separate note). Reason being, KEYS, a test & measurement leader benefits from the diversity of architectures (each of which needs to be tested), which this note clearly highlights that diversity is likely to take place. With multiple in-line with historical times of stronger investment cycles, we see it as still having room for positive movement as estimates get revised upwards (from strong incrementals on spending on AI, semis, A&D and edge AI / 6G).

Exhibit 1: Scale-Up Market Estimate Has 4x'd Y/Y  
![](images/86d6d69e30c9045b960559a4b8348faad7134372d336b61b193979220791d7fa.jpg)  
Source: Dell'Oro. Note: Excludes NICs, Pluggables/Optics, and Cables

Exhibit 2: CPO Penetration to Come Later to Scale-Up, But Post 2028, Should Be Meaningful Adoption  
![](images/37117731fbd1cf7b0391c18d0e6a3a694e21470cd23cdcd5e2ac3e459dd8ed31.jpg)  
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
![](images/d2607b8992bacb93f1b887af502da5f7a3bb4ffa12483bc932084fbd146210b4.jpg)  
Source: Dell'Oro. Note: Excludes NICs, Pluggables/Optics, and Cables

## Growth Driven By Multiple Vectors

Clusters getting bigger. Last year, our primer noted the emerging opportunity as scale-up moved from 8 GPU's to full rack at 72 GPU's with Blackwell. However, with Vera Rubin

noting 144 GPU's in a scale-up cluster and 576 with Rubin Ultra (and a potential doubling of that with Feyman), the cluster sizes and need for scale-up connections have increased materially. This is true not only in the NVDA ecosystem, but in Google's TPU and AMZN's Tranium ecosystem as well.

Exhibit 4: Increase in Scale-Up Networking TAM / Complexity In Large Part Due to Increase in XPU's in the Cluster (NVDA Example Below)

<table><tr><td>Metric</td><td>NVL72 Optical Scale-Out</td><td>NVL576 Hybrid</td><td>NVL576 Full CPO</td><td>Feynman Hybrid 200G</td><td>Feynman Full CPO 400G</td><td>Feynman Full CPO 200G</td></tr><tr><td>Configuration</td><td>NVL72</td><td>NVL576</td><td>NVL576</td><td>NVL1152</td><td>NVL1152</td><td>NVL1152</td></tr><tr><td>Total GPUs</td><td>72</td><td>576</td><td>576</td><td>1,152</td><td>1,152</td><td>1,152</td></tr><tr><td>Racks</td><td>1</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td></tr><tr><td>GPUs per rack</td><td>72</td><td>72</td><td>72</td><td>144</td><td>144</td><td>144</td></tr><tr><td>Low-latency domain</td><td>72</td><td>576</td><td>576</td><td>1,152</td><td>1,152</td><td>1,152</td></tr><tr><td>Scale-up BW/GPU (Tb/s)</td><td>N/A</td><td>14.4</td><td>14.4</td><td>28.8</td><td>28.8</td><td>28.8</td></tr><tr><td>Scale-out BW/GPU (Tb/s)</td><td>1.6T</td><td>1.6T</td><td>1.6T</td><td>3.2T</td><td>3.2T</td><td>3.2T</td></tr><tr><td>Scale-out oversubscription</td><td>2:1</td><td>1.5:1</td><td>1.5:1</td><td>1:1</td><td>1:1</td><td>1:1</td></tr><tr><td>SerDes (Gb/s)</td><td>100</td><td>200</td><td>200</td><td>200</td><td>400</td><td>200</td></tr><tr><td>Scale-up medium</td><td>Copper</td><td>Hybrid</td><td>CPO</td><td>Hybrid</td><td>CPO</td><td>CPO</td></tr><tr><td>Scale-out medium</td><td>Plug/CPO</td><td>Plug/CPO</td><td>Plug/CPO</td><td>CPO</td><td>CPO</td><td>CPO</td></tr><tr><td>Intra-rack OEs (A)</td><td>-</td><td>-</td><td>10,368</td><td>-</td><td>20,736</td><td>41,472</td></tr><tr><td>Inter-pod OEs (B)</td><td>-</td><td>9,072</td><td>9,072</td><td>36,288</td><td>18,144</td><td>36,288</td></tr><tr><td>Scale-out OEs (C)</td><td>144</td><td>768</td><td>768</td><td>2,304</td><td>1,152</td><td>2,304</td></tr><tr><td>Total OEs (pod)</td><td>144</td><td>9,840</td><td>20,208</td><td>38,592</td><td>40,032</td><td>80,064</td></tr><tr><td>OEs per rack</td><td>144</td><td>1,230</td><td>2,526</td><td>4,824</td><td>5,004</td><td>10,008</td></tr><tr><td>OEs per GPU</td><td>2</td><td>17</td><td>35</td><td>34</td><td>35</td><td>70</td></tr></table>

Source: MS estimates.

Hitting limits with copper reach as trying to involve more accelerators. Copper has traditionally been preferable in data center architectures, given it is cheaper, more reliable (electrical vs. optical signals), and uses less power. However, the speeds of AI networks are beginning to push the limitations of copper (see below).

We would note that the funeral for copper has been delayed multiple times as innovations have helped extend the life of copper, namely: PAM4, allowing more bits to travel, more powerful digital signal processors (DSPs), allowing for greater signal correction, and retimers, that help with weakening electrical signals, improved connectors / packaging.

Looking forward, the main debate today is whether copper's life can further be extended with 448G SERDES, PAM6 modulation, 200G retimers, etc. Broadcom has demonstrated next-gen technologies that still extend copper to 6m lengths, challenging NVDA focus on CPO for cross-rack connectivity with Vera Rubin Ultra.

Exhibit 5: Reach is Primary Challenge of Copper

<table><tr><td>Technology</td><td>Transmission Distance</td><td>Typical Data Rate / Lane</td><td>Power Consumption</td><td>Cost</td><td>Advantages</td><td>Disadvantages</td></tr><tr><td>DAC (Direct Attach Copper)</td><td>&lt; 1 m</td><td>25-50G PAM4</td><td>Very low</td><td>Lowest</td><td>Simple, low cost, near-zero power consumption</td><td>Very short reach; distance drops sharply beyond 200G/400G</td></tr><tr><td>ACC (Active Copper Cable)</td><td>2-2.5 m</td><td>50-106G PAM4</td><td>2.5-5 W</td><td>Low</td><td>Low power, simple structure, lower cost than AEC</td><td>Limited equalization capability; reach still short</td></tr><tr><td>AEC (Active Electrical Cable)</td><td>3-7 m; up to ~9 m (extended versions)</td><td>50-106G PAM4</td><td>6-12 W (800G); ~20 W for 1.6T</td><td>Medium</td><td>Longer reach, strong signal integrity, high reliability, hot- pluggable</td><td>Higher cost and power than ACC; shorter reach than optical solutions</td></tr><tr><td>AOC (Active Optical Cable)</td><td>5-30 m</td><td>50-106G PAM4</td><td>10-18 W</td><td>High</td><td>Long reach, immune to electromagnetic interference, lightweight</td><td>Higher cost and power; less economical for very short in-rack connections</td></tr><tr><td>CPO (Co-Packaged Optics)</td><td>2-10 m (within package/system)</td><td>&gt;100G PAM4 or 256G</td><td>&lt;5 pJ/bit</td><td>Very high</td><td>Extremely high bandwidth density, very low energy per bit</td><td>Complex packaging, high cost, immature supply chain</td></tr></table>

Source: Semivision.

The bottleneck has shifted to I/O. While AI accelerators have seen remarkable improvements in computational performance over the past decade, the limiting factor for large-scale AI systems is increasingly shifting toward data movement. Modern AI training and inference require thousands of GPUs to operate as a single distributed system, meaning overall performance depends not only on the speed of individual accelerators but also on how efficiently they communicate with one another. As compute capability continues to outpace improvements in networking and memory subsystems, the industry is experiencing a transition to a connectivity bottleneck.

Exhibit 6: Compute capabilities outpace connectivity  
![](images/41281c6b8c4e81e80f597c25894ff4c8a64554926dc1e4501ad49b254f462a5d.jpg)  
Source: Gholami et al. 2024, MS

The fundamental challenge is that communication distances are increasing while electrical reach is shrinking. Every new generation of AI accelerators increases I/O speeds, with SerDes lane rates progressing from 100G today toward 200G and eventually 400G. While these higher signalling rates deliver substantially greater bandwidth, they also reduce the distance over which electrical signals can travel while maintaining signal integrity. At the same time, AI clusters continue to expand in scale, with scale-up domains growing from traditional 8-GPU servers to 72-GPU racks with NVIDIA Blackwell, 144-GPU systems with Vera Rubin, and potentially more than 1,000 accelerators in future architectures. The result is a fundamental engineering challenge: the physical distances over which GPUs must communicate are increasing at precisely the same time that higher signalling speeds make long-distance electrical communication increasingly difficult.

Exhibit 7: Data Center Switch Revenue by port Speed  
![](images/8fb760e1a234460db3593e1282ca2208eb677ecfd2540c757d0ee9deb6532711.jpg)  
Source: 650 Group

## How We View the Architecture Progression

Copper where you can, optics when you must. Copper interconnects remain the preferred medium for short-reach connectivity because they provide the lowest latency, lowest power consumption and lowest cost. However, as signalling speeds increase, electrical losses, insertion loss and noise become progressively more difficult to manage, requiring increasingly sophisticated SerDes, digital signal processors, retimers and equalization techniques simply to preserve signal integrity. This phenomenon is often referred to as the industry's "copper wall."

In our view, copper's longevity continues to be underestimated. While higher signalling speeds are undoubtedly making electrical transmission more challenging, successive innovations including more capable SerDes, improved connectors, retimers and active copper technologies have consistently extended copper's useful life beyond expectations. We continue to expect direct-attached copper to remain the preferred solution for intra-rack scale-up connectivity for several more product generations before a broader transition to optical technologies becomes necessary.

We expect a meaningful transition to optical interconnects in scale-up no earlier than 2028. While optics offers clear advantages in bandwidth density and reach, the cost premium remains significant and the supply chain is still maturing. In our view, adoption will be driven less by incremental increases in signalling speeds and more by architectural changes in AI infrastructure. As scale-up domains extend beyond a single rack, copper requires increasingly complex SerDes and signal conditioning to maintain performance, driving higher power consumption and lower efficiency. We see the key catalysts for optical adoption as: (1) multi-rack scale-up architectures, (2) rising electrical I/O power consumption, (3) increasing bandwidth density requirements, and (4) continued growth in bandwidth demands from larger, more communication-intensive AI workloads. These trends should increasingly favor near-package and co-packaged optical solutions over time.

XPU vendor roadmaps. NVIDIA is expected to lead the industry's transition to optical scale-up interconnects. We expect Rubin Ultra (2027) to represent an intermediate step, with GPUs within each 72-GPU rack remaining interconnected via copper NVLink while optical links connect multiple racks into a larger 576-GPU NVLink domain. This hybrid

approach preserves copper's cost and latency advantages for short-reach communication while deploying optics only where longer distances make electrical interconnects increasingly challenging. We expect Feynman (2028) to mark the first meaningful deployment of fully optical scale-up connectivity as NVLink domains expand to 1,152 GPUs. Checks point to limited deployment of Rubin Ultra with CPO, making Feynman, more likely scaling in 2029 as the adoption catalyst for CPO.

The broader XPU ecosystem is likely to follow one to two years behind NVIDIA. AMD appears to be targeting optical scale-up with its MI550/MI650 platforms around the 2027-2028 timeframe, while we view Trainium 5 (post-2028) as the earliest likely opportunity for AWS. Broadcom's custom ASIC customers are also likely to adopt optics around 2028+, although Broadcom remains the most conservative on CPO, arguing continued advances in SerDes will extend copper's useful life. Google is the notable exception, as its TPU architecture relies on an Optical Circuit Switch (OCS) Torus topology rather than a traditional switched scale-up network, which may delay or reduce the need for CPO.

Exhibit 8: CPO Penetration in Scale-Up Likely Takes to 2029 to be Material  
![](images/e40466bb0deafee2cecaecca8b17242381dd7a90973cd0127efa06446fd4fe31.jpg)  
Source: Dell'Oro.

Exhibit 9: Primarily Scale-Out Opportunity Until 2029  
![](images/0756f1b41cbc5497ddd93f39b9d4e1d8bb677f14fe6215cd9c1ade6bfe27aeb5.jpg)  
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

![](images/4024df8ff1427ae43c4f968735acbfea30027754e8c27357629d3b9c821ce232.jpg)  
Source: MS

The clearest non-NVIDIA beneficiaries in 2026 are Astera Labs and Broadcom. Astera is supplying the PCIe-based scale-up switch for AWS Trainium 3 through Scorpio-X, which has begun shipping and should ramp more meaningfully in 2H26. We view this as an important bridge ahead of native UALink. Broadcom is also well positioned through AMD's MI400/Helios platform, where AMD is using UAL tunneled over Ethernet with Broadcom's Tomahawk switch silicon.

Looking into 2027, we expect the non-NVIDIA scale-up ecosystem to further take shape. The main paths are Ethernet, UALink, and NVLink Fusion, with PCIe likely remaining a transitional solution. The key debate is which protocol customers will use. We expect adoption to be determined by technical performance, software and ecosystem support, and the strategic partnerships underpinning each XPU platform.

Based on our XPU forecasts, we expect PCIe to remain the largest non-NVIDIA scale-up fabric in 2027, while Ethernet should be the fastest-growing. PCIe's lead reflects Trainium, which we expect to be the largest switched non-NVIDIA ASIC platform next year. Ethernet should begin to establish a more meaningful presence in scale-up through the ramp of AMD's MI400/Helios platform, initial Broadcom-enabled ASIC deployments and early adoption of Microsoft's Maia. Broadcom and Marvell are well positioned as Ethernet switch suppliers. PCIe should also continue to grow rapidly, supported by Trainium 3 and broader adoption of PCIe/custom fabrics globally, benefiting Astera Labs, which has noted more than ten customers engaged on its Scorpio scale-up platform. NVLink should continue growing alongside NVIDIA accelerator shipments, although at a more modest rate given its already dominant base.

Exhibit 11: Switched Fabric Protocol Share  
![](images/1811a3a78cbbeb8df5609a5c9b9bf915739f6a8a8b748e0ee4f60c7111340e86.jpg)  
Source: MS  
Note: We estimate share using our XPU unit estimates. We assume MI400, MSFT Maia and AVGO XPU customers use Ethernet

UALink remains a key swing factor in the non-NVIDIA ecosystem. While the UALink specifications have now been ratified, the key gating factor is commercial silicon and switch availability. If native UALink switches arrive on schedule and are performant, we think it's possible that AMD and AWS could be among the earliest adopters, creating a meaningful opportunity for Astera Labs and Marvell. If UALink slips or customers prefer another protocol, Broadcom's Ethernet-based approach and NVIDIA's NVLink Fusion ecosystem should gain share. Ultimately, we view PCIe as a transitional fabric. While PCIe deployments should continue growing over the next several years, we believe hyperscalers will eventually migrate toward open, purpose-built AI fabrics. Whether that is UAL or Ethernet is still a debate.

## NVLink Fusion represents NVIDIA's strategy for extending its ecosystem beyond

NVIDIA GPUs. It enables third-party CPUs, XPUs and custom ASICs to connect directly into NVLink. Both Astera Labs and Marvell are ecosystem partners, positioning them to benefit if adoption accelerates. Marvell's recently announced strategic partnership with NVIDIA further reinforces its positioning as a key AI connectivity partner. For Astera, the opportunity comes through a protocol translation chip that sits alongside each XPU and converts its native protocol into NVLink. Unlike Scorpio-X, which is shared across multiple accelerators, the NVLink Fusion chip attaches one-to-one with each XPU, creating a different economic model with lower ASPs but substantially higher attach rates. Management has indicated that the content opportunity is broadly comparable to Scorpio-X, despite the different architecture. Based on current announcements, we think AWS will be pursuing a dual-track strategy for Trainium 4, supporting both UALink and NVLink Fusion. Our thinking for now is this will probably remain a more niche solution for the ecosystem overall, but is certainly additive to NVIDIA - and is something that could lead to higher NVDA GPU adoption if ASICs fall short.

2028: The Market Opens Up. The ramp of AMD MI-series platforms, AWS Trainium, Microsoft Maia and Broadcom-enabled ASICs, and others should materially expand the addressable market outside NVIDIA. We continue to see significant runway for Ethernet, particularly as Broadcom's ASIC customers ramp and adopt Ethernet-based scale-up solutions. UALink represents the largest source of upside for Astera Labs and Marvell. If the standard is commercially ready and broadly adopted across AMD, AWS and other custom XPUs, it has the potential to become the leading open alternative to NVLink. However, we believe the market remains far from settled, with customers likely to evaluate UALink, Ethernet and NVLink Fusion in parallel before converging on a preferred architecture. Google remains the architectural outlier. Its TPU architecture relies on ICI and OCS-based torus topologies rather than traditional switched scale-up fabrics. Whether this ultimately proves advantageous as AI clusters continue to scale remains an important question.

The non-NVIDIA ecosystem remains largely undecided. Over the next two years, architectural decisions made by hyperscalers and ASIC customers will determine which fabrics emerge as industry standards, creating a significant greenfield opportunity for Broadcom, Marvell and Astera Labs.

Exhibit 12: Non-NVLink Fabrics Set to Grow Rapidly, but the Market Mix Remains in Flux

![](images/19e2bde4f89d1ac2cd7e14af6129d19bdeafad70e8a594802ca91913ee2ad115.jpg)  
Source: Dell'Oro, MS.
Note: Non-NVLink from 2028-2030 is an estimate from Dell'Oro and includes Ethernet, UAL, and others. Excludes NICs, Pluggables/Optics, and Cables

## What are the Transmission Approaches As Industry Eventually Hits "Copper Wall"?

Co-packaged optics (CPO) is emerging as a critical architectural shift for AI datacenter networking, driven by the rising power, bandwidth, and density constraints of traditional pluggable optical modules. AI clusters require massive scale-out connectivity across racks, but today's switch architecture forces high-speed electrical signals to travel 15 to 30 centimeters across a circuit board before reaching front-panel optical modules. As speeds rise, those electrical signals degrade more quickly, requiring more advanced DSPs, retimers, and correction circuitry to preserve signal integrity. CPO addresses this constraint by moving optical engines into the same package as the switch ASIC, reducing the electrical path to only a few millimeters and enabling lower-power short-reach SerDes, simplified signal processing, and higher front-panel bandwidth density.

Reduced interconnect power is the most tangible near-term benefit, with CPO potentially lowering optical interconnect power consumption by roughly 50-80%, while also freeing front-panel space and reducing reliance on discrete optical modules. Adoption also shifts value toward suppliers with control over optical engines, silicon photonics, external lasers, and advanced packaging, given the need to precisely integrate electronic chips, photonic chips, fiber arrays, lasers, and thermal management. Key participants include Broadcom and NVIDIA in switch platforms, Lightmatter, Ayar Labs, Marvell/Celestial AI, and POET in optical engines and photonics, TSMC, GlobalFoundries, and Tower in silicon photonics foundry capacity, and Lumentum, Coherent, and Sivers in laser supply.

Source: Broadcom  
Exhibit 13: CPO brings the optical engine next to the ASIC, reducing interface losses and shortening the electrical path  
![](images/954d6ca07cf1637b39695a845853b30d376f61fadb479a2d4134189c93056d2a.jpg)

Exhibit 14: CPO Will First Start at 2.5D CPO, But Eventually Evolve Towards Full 3D CPO, Likely 2030 and Beyond  
![](images/7a9eed1b92759bfae67273e7f03c3e6551de6e1594f7f1a0d6fc7b9027001786.jpg)  
Source: Fibermall.

Near-packaged optics (NPO) sits between pluggables and CPO, moving the optical engine close to the switch or GPU ASIC while keeping it outside the ASIC package. For optical suppliers such as LITE and COHR, the NPO opportunity is centered on selling the core optical building blocks needed to replace copper links at 1.6T and 200G-per-lane, including high-power CW lasers, external laser source modules, InP-based laser content, 200G VCSEL-based solutions, and potentially more integrated optical engine content. Customer interest appears strongest among non-NVIDIA-class architectures that need to solve copper reach, power, and signal integrity constraints but may not yet be ready to accept the tighter vendor coupling and manufacturing complexity of full CPO. Compared with CPO, NPO offers a more open and serviceable architecture because optics can remain socketed or separately sourced from the GPU / XPU or switch silicon, limiting lock-in risk and preserving a broader merchant optical ecosystem. Performance and power efficiency likely sit below full CPO but materially above front-panel pluggables, making NPO a

credible intermediate architecture and a potentially attractive near-term demand driver for optical component vendors as scale-up networking moves increasingly toward optical connectivity.

Exhibit 15: NPO moves the optical engine near the compute package, improving reach and efficiency while preserving a more serviceable / open architecture / ecosystem than CPO

![](images/557706e01dba04644e96cc2e44a49462efc5feee615c934a5481e79da68184e5.jpg)  
Source: Cisco.

Exhibit 16: NPO decouples the optical engine from the switch chip and then assembles them on the same system board

![](images/6868cebf8ce39adb2b65dd5cd9936bf0437b062e5a2d4d896ea37c1cddec7b86.jpg)  
Source: Fibermall.

Active copper cables occupy the middle of the data center interconnect spectrum, sitting above passive DACs and below optical solutions in reach, power, and cost. Two architectures matter for investors, with AECs using retimers, equalization, and clock data recovery to restore signal integrity across longer copper links, while ACCs use a lower-power redriver approach that amplifies the analog signal but has less ability to remove jitter. AEC is currently the dominant active copper configuration because it offers stronger signal integrity, with typical reach of roughly 7 to 9 meters and support for intra-rack and rack-to-rack AI connectivity, while ACC is more focused on shorter intra-rack links of roughly 3 meters where very low power and latency are the priorities. Investor relevance is tied to AI cluster architecture, where copper remains attractive for short-reach scale-up and selected scale-out links because it can deliver better reliability, lower power, and lower total cost of ownership than laser-based optical modules when distance

requirements are manageable. AECs can reduce interconnect power by roughly 50% versus pluggable optical transceivers, are materially smaller and lighter than passive DACs, and are gaining traction as clusters scale from 400G to 800G, with 1.6T commercialization becoming the next step. At 200G per lane, reach likely compresses from roughly 7 meters toward closer to 5 meters, but the value proposition can strengthen because higher speeds increase the need for signal conditioning and drive ASP uplift for active cable silicon. Adoption also appears increasingly broad across hyperscalers and NeoClouds, with active copper becoming a standard option for dense in-rack and multi-rack deployments where customers want to avoid the cost, power, and operational complexity of optics. From a stock perspective, active copper should be viewed as complementary to LPO, NPO, and CPO rather than directly competitive, as AI data centers are likely to use a heterogeneous mix of interconnects based on reach, power budget, latency, reliability, and serviceability. Optical will remain essential as distances increase and scale-up domains expand across racks, but active copper should retain an important role inside the rack and near-rack environment, supporting vendors exposed to retimers, redrivers, cable assemblies, and validated active cable platforms.

Exhibit 17: ACC prioritizes efficiency inside the rack, while AEC extends reach at higher power and latency

## Active Copper Cable (ACC)

![](images/4e620a0ac95ea4bb093f5d54388a5a810b9bb36698250f8a5b5bb3339c9705c0.jpg)

\- Pure analog solution

\- Extreme low cost, power, latency

\- <2m copper for inside rack ■ High performance at cost of power, latency

![](images/cce65dd2f14a90a4b878c1970b34c86e0d1589fc60f22eeab45eaa736273e460.jpg)

\- <5m reach at 1.6T

Enabled by ACC product offerings

Enabled by AEC DSP product offerings

Source: Marvell

OCS, or optical circuit switching, is a higher-efficiency optical networking layer for AI clusters, routing light directly from one port to another rather than relying on EPS, or electronic packet switching, which converts traffic into electrical signals for processing inside traditional switch silicon. Investor relevance centers on lower power, lower forwarding latency, and better long-term upgrade economics, since an OCS can often support higher link speeds over time without requiring a full switch silicon refresh. Adoption is most compelling in AI training environments where traffic patterns are relatively predictable, making OCS a good fit for scale-up pods, upper layers of scale-out networks, and large inter-data-center transfers where bandwidth, power, and network

TCO matter more than ultra-fast packet-by-packet reconfiguration. Within OCS, micro-electro-mechanical systems, or MEMS, is the most mature architecture today and uses tiny movable mirrors to steer light between ports; the advantage is faster switching versus liquid-crystal alternatives, lower insertion loss, and earlier volume readiness, which makes MEMS better suited for near-term hyperscale deployments. Liquid crystal on silicon, or LCoS, takes a different approach by using voltage-controlled liquid crystal to change how light is directed through the switch; its main advantage is longer expected service life, which can improve ownership cost over time, but switching latency is slower and manufacturing still requires precise optical alignment. Waveguide-based OCS and piezoelectric OCS are more future-oriented approaches, with waveguide designs offering faster switching potential but currently facing higher insertion loss and cost, while piezoelectric designs offer very low insertion loss but remain expensive and less mature. For optical suppliers, the key point is that OCS expands the revenue opportunity beyond transceivers and CPO light sources into higher-value systems and precision optical content, including MEMS mirrors, LCoS switching elements, collimator arrays, calibration systems, beam displacers, and other optical assemblies. LITE appears more levered to MEMS-based OCS, while COHR is more relevant to LCoS-based OCS and broader precision optical content. Demand is still concentrated and execution-heavy, but OCS should be viewed as a complementary growth vector alongside pluggable optics, NPO, and CPO, giving optical suppliers another path to monetize AI networking growth as customers optimize for power, latency, upgrade flexibility, and total cost of ownership.

Exhibit 18: Google's Palomar OCS highlights its leadership in bringing optical circuit switching from lab architecture to production-scale data center networks

![](images/c32ea0847d9eb116591baa8a98ebeb9655b5f19df70324bb45b960a36ec1de8c.jpg)

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
![](images/e603590e45a39aea5c00ebcceeeb64a6ba29f856b9c4d0fab4bd5eae292ef840.jpg)  
Source: MS

(CPO) ecosystem over

the last couple of weeks as timing questions re-emerged. However, debating timeline of adoption misses that optical content is largely correlated to bandwidth needs – e.g., the more bandwidth, the more optics, whether that takes the form of co-packaged optics

(CPO), near-packaged optics (NPO), or other optical formats. While given commitments of capacity as part of NVDA's equity investments in LITE, COHR, GLW likely prevent just instantly swapping one set of demand for another, we do think that these three vendors remain beneficiaries of the increase in optical content, particularly as it enters the scale-up domain.

Exhibit 20: It Will Take Time, but Copper Eventually Reaches Limits within Scale-Up Networks

![](images/9233b565220f53863a7beb9f659ec4344074e181a3cf54c441dea78df46dad9d.jpg)  
Source: 650 Group.

![](images/f53c7299df5fa13776c56fe63309059bbb3ac430bc018fe7c406baa4bc92a6f1.jpg)

What about Amazon's Resilient Network Graph (RNG)? To give a basic description, Amazon noted in an academic paper over the last couple of weeks that they were deploying a new network architecture in most of their data centers that moves away from traditional architectures (e.g. fat tree or tiers of switching / routing) and moves towards a flatter, more mesh network, where adaptive routing and ShuffleBoxes help with traffic management. This network design requires significant adaptive routing / software expertise, a move away from recent history, where more networking has been added, but with more open source software. Given value of software work Amazon has done, and the proprietary nature of their network designs, we don't yet see major adoption beyond Amazon.

AWS's RNG (Resilient Network Graphs) architecture marks a material shift from conventional fat-tree data center networking, replacing a hierarchical fabric where traffic moves through upper aggregation layers with a flatter quasi-random graph designed to create broader path diversity across routers. Conventional fat-tree networks are easier to route but require additional router layers, can concentrate congestion near the top of the hierarchy, and create more fragility when important routers fail. RNG uses quasi-random connectivity, ShuffleBox passive optical components, and Spraypoint routing to make flatter networks practical at production scale, reducing router count by 69%, improving throughput by up to 33%, and projecting a 40% reduction in network equipment electricity consumption. Adoption has moved quickly from production validation to global default design, with AWS's first quasi-random production network going live near Dublin at the end of 2024, refined through two additional deployments, and becoming the default architecture for most new AWS data centers globally by April 2026. Moving from initial deployment to default architecture in about 18 months suggests a high level of confidence in the design and highlights how aggressively AWS is reworking the physical network layer to support AI-scale infrastructure.

Exhibit 21: Traditional fat-tree network topology (a) vs. AWS's flatter quasi-random graph topology (b)  
![](images/24032698a94c12a03fb2ebe5d4d59863a0ce29bb98e37565d450954c04b74d34.jpg)  
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

<table><tr><td colspan="7">FY28 Adj. EPS Sensitivity ($)</td></tr><tr><td rowspan="2"></td><td colspan="6">Scale Out Adoption (%)</td></tr><tr><td></td><td>7.6%</td><td>12.6%</td><td>17.6%</td><td>22.6%</td><td>27.6%</td></tr><tr><td rowspan="5">Scale UpAdoption (%)</td><td>1.5%</td><td>$22.62</td><td>$24.29</td><td>$25.97</td><td>$27.65</td><td>$29.32</td></tr><tr><td>2.5%</td><td>$23.04</td><td>$24.72</td><td>$26.39</td><td>$28.07</td><td>$29.74</td></tr><tr><td>3.5%</td><td>$23.46</td><td>$25.14</td><td>$26.81</td><td>$28.49</td><td>$30.16</td></tr><tr><td>4.5%</td><td>$23.88</td><td>$25.56</td><td>$27.23</td><td>$28.91</td><td>$30.58</td></tr><tr><td>5.5%</td><td>$24.30</td><td>$25.98</td><td>$27.65</td><td>$29.33</td><td>$31.01</td></tr></table>

<table><tr><td colspan="7">FY28 Adj. EPS Downlift / Uplift vs FY28 Consensus (%)</td></tr><tr><td rowspan="2"></td><td colspan="6">Scale Out Adoption (%)</td></tr><tr><td></td><td>7.6%</td><td>12.6%</td><td>17.6%</td><td>22.6%</td><td>27.6%</td></tr><tr><td rowspan="5">Scale Up Adoption (%)</td><td>1.5%</td><td>(22.3%)</td><td>(16.6%)</td><td>(10.8%)</td><td>(5.1%)</td><td>0.7%</td></tr><tr><td>2.5%</td><td>(20.9%)</td><td>(15.1%)</td><td>(9.4%)</td><td>(3.6%)</td><td>2.1%</td></tr><tr><td>3.5%</td><td>(19.4%)</td><td>(13.7%)</td><td>(7.9%)</td><td>(2.2%)</td><td>3.6%</td></tr><tr><td>4.5%</td><td>(18.0%)</td><td>(12.2%)</td><td>(6.5%)</td><td>(0.7%)</td><td>5.0%</td></tr><tr><td>5.5%</td><td>(16.5%)</td><td>(10.8%)</td><td>(5.0%)</td><td>0.7%</td><td>6.5%</td></tr></table>

Source: Company data, MS

Exhibit 23: COHR: CPO Scale Out / Scale Up FY28 Adj. EPS Sensitivity

<table><tr><td colspan="7">FY28 Adj./Core EPS Sensitivity ($)</td></tr><tr><td rowspan="2"></td><td colspan="6">Scale Out Adoption (%)</td></tr><tr><td></td><td>7.5%</td><td>12.5%</td><td>17.5%</td><td>22.5%</td><td>27.5%</td></tr><tr><td rowspan="5">Scale Up Adoption (%)</td><td>1.5%</td><td>$10.83</td><td>$11.16</td><td>$11.49</td><td>$11.82</td><td>$12.15</td></tr><tr><td>2.5%</td><td>$10.95</td><td>$11.28</td><td>$11.61</td><td>$11.94</td><td>$12.27</td></tr><tr><td>3.5%</td><td>$11.08</td><td>$11.41</td><td>$11.74</td><td>$12.07</td><td>$12.40</td></tr><tr><td>4.5%</td><td>$11.20</td><td>$11.53</td><td>$11.86</td><td>$12.19</td><td>$12.52</td></tr><tr><td>5.5%</td><td>$11.33</td><td>$11.66</td><td>$11.99</td><td>$12.32</td><td>$12.65</td></tr></table>

<table><tr><td colspan="7">FY28 Adj./Core EPS Downlift / Uplift vs FY28 Consensus (%)</td></tr><tr><td rowspan="2"></td><td colspan="6">Scale Out Adoption (%)</td></tr><tr><td></td><td>7.5%</td><td>12.5%</td><td>17.5%</td><td>22.5%</td><td>27.5%</td></tr><tr><td rowspan="5">Scale Up Adoption (%)</td><td>1.5%</td><td>(16.6%)</td><td>(14.0%)</td><td>(11.5%)</td><td>(9.0%)</td><td>(6.4%)</td></tr><tr><td>2.5%</td><td>(15.6%)</td><td>(13.1%)</td><td>(10.5%)</td><td>(8.0%)</td><td>(5.5%)</td></tr><tr><td>3.5%</td><td>(14.7%)</td><td>(12.1%)</td><td>(9.6%)</td><td>(7.0%)</td><td>(4.5%)</td></tr><tr><td>4.5%</td><td>(13.7%)</td><td>(11.2%)</td><td>(8.6%)</td><td>(6.1%)</td><td>(3.5%)</td></tr><tr><td>5.5%</td><td>(12.7%)</td><td>(10.2%)</td><td>(7.7%)</td><td>(5.1%)</td><td>(2.6%)</td></tr></table>

Source: Company data, MS

Exhibit 24: GLW: CPO Scale Out / Scale Up FY28 Adj. EPS Sensitivity

<table><tr><td colspan="7">FY28 Adj./Core EPS Sensitivity ($)</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="5">Scale Up Adoption (%)</td></tr><tr><td>4.0%</td><td>8.0%</td><td>12.0%</td><td>16.0%</td><td>20.0%</td></tr><tr><td rowspan="5">Scale OutAdoption (%)</td><td>0.0%</td><td>$5.08</td><td>$5.28</td><td>$5.48</td><td>$5.67</td><td>$5.87</td></tr><tr><td>5.0%</td><td>$5.11</td><td>$5.30</td><td>$5.50</td><td>$5.70</td><td>$5.90</td></tr><tr><td>10.0%</td><td>$5.13</td><td>$5.33</td><td>$5.53</td><td>$5.72</td><td>$5.92</td></tr><tr><td>15.0%</td><td>$5.16</td><td>$5.35</td><td>$5.55</td><td>$5.75</td><td>$5.95</td></tr><tr><td>20.0%</td><td>$5.18</td><td>$5.38</td><td>$5.58</td><td>$5.78</td><td>$5.97</td></tr></table>

<table><tr><td colspan="7">FY28 Adj./Core EPS Downlift / Uplift vs FY28 Consensus (%)</td></tr><tr><td rowspan="2"></td><td colspan="6">Scale Up Adoption (%)</td></tr><tr><td></td><td>4.0%</td><td>8.0%</td><td>12.0%</td><td>16.0%</td><td>20.0%</td></tr><tr><td rowspan="5">Scale Out Adoption (%)</td><td>0.0%</td><td>(16.7%)</td><td>(13.5%)</td><td>(10.2%)</td><td>(7.0%)</td><td>(3.7%)</td></tr><tr><td>5.0%</td><td>(16.3%)</td><td>(13.1%)</td><td>(9.8%)</td><td>(6.6%)</td><td>(3.3%)</td></tr><tr><td>10.0%</td><td>(15.9%)</td><td>(12.6%)</td><td>(9.4%)</td><td>(6.2%)</td><td>(2.9%)</td></tr><tr><td>15.0%</td><td>(15.5%)</td><td>(12.2%)</td><td>(9.0%)</td><td>(5.7%)</td><td>(2.5%)</td></tr><tr><td>20.0%</td><td>(15.1%)</td><td>(11.8%)</td><td>(8.6%)</td><td>(5.3%)</td><td>(2.1%)</td></tr></table>

Source: Company data, MS

## Model Changes

Exhibit 25: LITE: Model Changes

<table><tr><td></td><td>2025A</td><td>Y/Y (%)</td><td>Q1-26A</td><td>Q2-26A</td><td>Q3-26A</td><td>Q4-26E</td><td>2026E</td><td>Y/Y (%)</td><td>2027E</td><td>Y/Y (%)</td></tr><tr><td>New Revenue</td><td>$1,645.0</td><td>21%</td><td>$533.8</td><td>$665.5</td><td>$808.4</td><td>$986.7</td><td>$2,994.4</td><td>82%</td><td>$5,667.7</td><td>89%</td></tr><tr><td>Old Revenue</td><td>$1,645.0</td><td>21%</td><td>$533.8</td><td>$665.5</td><td>$808.4</td><td>$980.5</td><td>$2,988.2</td><td>82%</td><td>$5,374.3</td><td>80%</td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>0%</td><td></td><td>5%</td><td></td></tr><tr><td>New Gross Profit</td><td>$571.5</td><td>39%</td><td>$210.3</td><td>$282.6</td><td>$386.9</td><td>$482.8</td><td>$1,362.6</td><td>138%</td><td>$2,899.2</td><td>113%</td></tr><tr><td>New Gross Margin</td><td>35%</td><td></td><td>39.4%</td><td>42.5%</td><td>47.9%</td><td>48.9%</td><td>45.5%</td><td></td><td>51.2%</td><td></td></tr><tr><td>Old Gross Profit</td><td>$571.5</td><td>39%</td><td>$210.3</td><td>$282.6</td><td>$386.9</td><td>$479.9</td><td>$1,359.7</td><td>138%</td><td>$2,746.3</td><td>102%</td></tr><tr><td>Old Gross Margin</td><td>35%</td><td></td><td>39.4%</td><td>42.5%</td><td>47.9%</td><td>49.0%</td><td>45.5%</td><td></td><td>51.1%</td><td></td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>0%</td><td></td><td>6%</td><td></td></tr><tr><td>New Operating Income</td><td>$160.1</td><td>(2207%)</td><td>$99.8</td><td>$167.7</td><td>$260.7</td><td>$349.6</td><td>$877.8</td><td>448%</td><td>$2,250.0</td><td>156%</td></tr><tr><td>New Operating Margin</td><td>10%</td><td></td><td>18.7%</td><td>25.2%</td><td>32.2%</td><td>35.4%</td><td>29%</td><td></td><td>40%</td><td></td></tr><tr><td>Old Operating Income</td><td>$160.1</td><td>(2207%)</td><td>$99.8</td><td>$167.7</td><td>$260.7</td><td>$347.6</td><td>$875.8</td><td>447%</td><td>$2,114.5</td><td>141%</td></tr><tr><td>Old Operating Margin</td><td>10%</td><td></td><td>18.7%</td><td>25.2%</td><td>32.2%</td><td>35.5%</td><td>29%</td><td></td><td>39%</td><td></td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>0%</td><td></td><td>6%</td><td></td></tr><tr><td>New Adjusted EPS</td><td>$2.06</td><td>366%</td><td>$1.10</td><td>$1.67</td><td>$2.37</td><td>$2.99</td><td>$8.42</td><td>310%</td><td>$18.37</td><td>118%</td></tr><tr><td>Old Adjusted EPS</td><td>$2.06</td><td>366%</td><td>$1.10</td><td>$1.67</td><td>$2.37</td><td>$2.97</td><td>$8.40</td><td>309%</td><td>$17.31</td><td>106%</td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>0%</td><td></td><td>6%</td><td></td></tr></table>

Source: Company data, MS

Exhibit 26: COHR: Model Changes

<table><tr><td colspan="13">($ millions, except per share data)</td></tr><tr><td></td><td>2025A</td><td>Y/Y (%)</td><td>Q1-26A</td><td>Q2-26A</td><td>Q3-26A</td><td>Q4-26E</td><td>2026E</td><td>Y/Y (%)</td><td>2027E</td><td>Y/Y (%)</td><td>2028E</td><td>Y/Y (%)</td></tr><tr><td>New Revenue</td><td>$5,810.1</td><td>23%</td><td>$1,581.4</td><td>$1,685.6</td><td>$1,805.6</td><td>$1,987.3</td><td>$7,059.9</td><td>22%</td><td>$9,438.4</td><td>34%</td><td>$12,863.1</td><td>36%</td></tr><tr><td>Old Revenue</td><td>$5,810.1</td><td>23%</td><td>$1,581.4</td><td>$1,685.6</td><td>$1,805.6</td><td>$1,983.4</td><td>$7,056.0</td><td>21%</td><td>$9,463.3</td><td>34%</td><td>$12,621.2</td><td>33%</td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td></td><td>(0%)</td><td></td><td>2%</td><td></td></tr><tr><td>New Gross Profit</td><td>$2,202.2</td><td>36%</td><td>$612.6</td><td>$657.1</td><td>$714.2</td><td>$794.9</td><td>$2,778.8</td><td>26%</td><td>$3,821.9</td><td>38%</td><td>$5,312.2</td><td>39%</td></tr><tr><td>New Gross Margin</td><td>38%</td><td></td><td>39%</td><td>39%</td><td>40%</td><td>40%</td><td>39%</td><td></td><td>40%</td><td></td><td>41%</td><td></td></tr><tr><td>Old Gross Profit</td><td>$2,202.2</td><td>36%</td><td>$612.6</td><td>$657.1</td><td>$714.2</td><td>$793.4</td><td>$2,777.3</td><td>26%</td><td>$3,832.1</td><td>38%</td><td>$5,212.4</td><td>36%</td></tr><tr><td>Old Gross Margin</td><td>38%</td><td></td><td>39%</td><td>39%</td><td>40%</td><td>40%</td><td>39%</td><td></td><td>40%</td><td></td><td>41%</td><td></td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td></td><td>(0%)</td><td></td><td>2%</td><td></td></tr><tr><td>New Operating Income</td><td>$1,036.9</td><td>68%</td><td>$308.9</td><td>$336.0</td><td>$366.1</td><td>$424.8</td><td>$1,435.8</td><td>38%</td><td>$2,126.3</td><td>48%</td><td>$3,109.1</td><td>46%</td></tr><tr><td>New Operating Margin</td><td>18%</td><td></td><td>20%</td><td>20%</td><td>20%</td><td>21%</td><td>20%</td><td></td><td>23%</td><td></td><td>24%</td><td></td></tr><tr><td>Old Operating Income</td><td>$1,036.9</td><td>68%</td><td>$308.9</td><td>$336.0</td><td>$366.1</td><td>$424.0</td><td>$1,435.0</td><td>38%</td><td>$2,132.0</td><td>49%</td><td>$3,050.8</td><td>43%</td></tr><tr><td>Old Operating Margin</td><td>18%</td><td></td><td>20%</td><td>20%</td><td>20%</td><td>21%</td><td>20%</td><td></td><td>23%</td><td></td><td>24%</td><td></td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td></td><td>(0%)</td><td></td><td>2%</td><td></td></tr><tr><td>New Adjusted EPS</td><td>$3.54</td><td>191%</td><td>$1.16</td><td>$1.29</td><td>$1.41</td><td>$1.62</td><td>$5.49</td><td>55%</td><td>$8.12</td><td>48%</td><td>$11.74</td><td>45%</td></tr><tr><td>Old Adjusted EPS</td><td>$3.54</td><td>191%</td><td>$1.16</td><td>$1.29</td><td>$1.41</td><td>$1.62</td><td>$5.48</td><td>55%</td><td>$8.14</td><td>48%</td><td>$11.52</td><td>41%</td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td></td><td>(0%)</td><td></td><td>2%</td><td></td></tr></table>

Source: Company data, MS

Exhibit 27: GLW: Model Changes

<table><tr><td colspan="11">($ millions, except per share data)</td></tr><tr><td></td><td>FY25A</td><td>Y/Y (%)</td><td>Q1-26A</td><td>Q3-26E</td><td>Q3-26E</td><td>Q4-26E</td><td>FY26E</td><td>Y/Y (%)</td><td>FY27E</td><td>Y/Y (%)</td></tr><tr><td>New Core Revenue</td><td>$16,407.5</td><td>13%</td><td>$4,344.9</td><td>$4,557.7</td><td>$4,797.6</td><td>$4,822.2</td><td>$18,522.4</td><td>13%</td><td>$22,376.6</td><td>21%</td></tr><tr><td>Old Core Revenue</td><td>$16,407.5</td><td>13%</td><td>$4,344.5</td><td>$4,600.2</td><td>$4,879.2</td><td>$4,931.8</td><td>$18,755.7</td><td>14%</td><td>$21,437.0</td><td>14%</td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>(1%)</td><td>(2%)</td><td>(2%)</td><td>(1%)</td><td></td><td>4%</td><td></td></tr><tr><td>New Core Gross Profit</td><td>$6,283.0</td><td>14%</td><td>$1,700.0</td><td>$1,820.9</td><td>$1,934.8</td><td>$1,966.4</td><td>$7,422.1</td><td>18%</td><td>$9,126.1</td><td>23%</td></tr><tr><td>New Gross Margin</td><td>38.4%</td><td></td><td>39.1%</td><td>40.0%</td><td>40.3%</td><td>40.8%</td><td>40.1%</td><td></td><td>40.8%</td><td></td></tr><tr><td>Old Core Gross Profit</td><td>$6,293.0</td><td>14%</td><td>$1,700.0</td><td>$1,838.9</td><td>$1,969.5</td><td>$2,013.7</td><td>$7,522.1</td><td>20%</td><td>$8,724.0</td><td>16%</td></tr><tr><td>Old Gross Margin</td><td>38.4%</td><td></td><td>39.1%</td><td>40.0%</td><td>40.4%</td><td>40.8%</td><td>40.1%</td><td></td><td>40.7%</td><td></td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>(1%)</td><td>(2%)</td><td>(2%)</td><td>(1%)</td><td></td><td>5%</td><td></td></tr><tr><td>New Core Operating Income</td><td>$3,160.0</td><td>25%</td><td>$876.0</td><td>$995.9</td><td>$1,095.2</td><td>$1,098.4</td><td>$4,065.6</td><td>29%</td><td>$5,339.6</td><td>31%</td></tr><tr><td>New Operating Margin</td><td>19.3%</td><td></td><td>20.2%</td><td>21.9%</td><td>22.8%</td><td>22.8%</td><td>21.9%</td><td></td><td>23.9%</td><td></td></tr><tr><td>Old Core Operating Income</td><td>$3,160.0</td><td>25%</td><td>$876.0</td><td>$1,006.3</td><td>$1,115.7</td><td>$1,135.8</td><td>$4,133.8</td><td>31%</td><td>$5,044.0</td><td>22%</td></tr><tr><td>Old Operating Margin</td><td>19.3%</td><td></td><td>20.2%</td><td>21.9%</td><td>22.9%</td><td>23.0%</td><td>22.0%</td><td></td><td>23.5%</td><td></td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>(1%)</td><td>(2%)</td><td>(3%)</td><td>(2%)</td><td></td><td>6%</td><td></td></tr><tr><td>New Core EPS</td><td>$2.54</td><td>29%</td><td>$0.70</td><td>$0.74</td><td>$0.82</td><td>$0.82</td><td>$3.09</td><td>22%</td><td>$4.15</td><td>34%</td></tr><tr><td>Old Core EPS</td><td>$2.54</td><td>29%</td><td>$0.70</td><td>$0.75</td><td>$0.84</td><td>$0.85</td><td>$3.14</td><td>24%</td><td>$3.90</td><td>24%</td></tr><tr><td>% Change</td><td>0%</td><td></td><td>0%</td><td>(1%)</td><td>(2%)</td><td>(4%)</td><td>(2%)</td><td></td><td>6%</td><td></td></tr></table>

Source: Company data, MS

![](images/ab6f0574ff47f2f5f6c2838c4c3b1f5296638b20aa8920374c943fc43c31b72d.jpg)

## Risk Reward – Lumentum Holdings Inc (LITE.O)

AI More Embedded Into Base Case, Greater CPO Adoption is Bull Case

## PRICE TARGET \$900.00

RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)  
![](images/b854e21ce8906d18e3541e5c193f9d6470901ac2ebd0f70b2b79698c8d23cd9c.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

\- Datacom positioning attractive, particularly with ramping customer sets, but questions remain on margin contribution and impacts to earnings power
- Key questions remain on magnitude and timeline of OCS ramp and length of EML shortage.

■ Upside to multiple likely limited by optical componentry being some of names most at risk from tariffs given intricate manufacturing that should be slower to move out of Asia, with LITE concentrated in Thailand

![](images/363b25975fd7938ee210f9ce31893733d02959dc161a82e2f11a3287a4d79255.jpg)

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

<table><tr><td>Drivers</td><td>Jun 2025</td><td>Jun 2026e</td><td>Jun 2027e</td><td>Jun 2028e</td></tr><tr><td>Total Revenue ($, mm)</td><td>1,645</td><td>2,994</td><td>5,668</td><td>8,681</td></tr><tr><td>Gross Margin (%)</td><td>34.7</td><td>45.5</td><td>51.2</td><td>51.5</td></tr><tr><td>Operating Margin (%)</td><td>9.7</td><td>29.3</td><td>39.7</td><td>41.4</td></tr><tr><td>EPS Growth Y/Y (%)</td><td>366.1</td><td>309.7</td><td>118.1</td><td>51.1</td></tr></table>

## INVESTMENT DRIVERS

• Opportunities like 3D sensing still in early days

• ROADMs in early days of deployment in China

\- Position as a consolidator as leverage levers more reasonable

## GLOBAL REVENUE EXPOSURE

![](images/40deacc10d50ac53896d26b875a4819f89e4cfc0c76bd6fe77f7395563f357df.jpg)

![](images/8dbeeff31c76aa8b05b5195cd95941bcf8e792d13ccdf931a9587e10ab856eff.jpg)  
Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

<table><tr><td>5/5BEST</td><td>24 MonthHorizon</td><td>5/5MOST</td><td>3 MonthHorizon</td></tr></table>

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

<table><tr><td>Inst. Owners, % Active</td><td>55.8%</td><td></td><td></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>2.1x</td><td></td><td></td></tr><tr><td>HF Sector Net Exposure</td><td>29.5%</td><td></td><td></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

MS ESTIMATES VS. CONSENSUS  
![](images/7c32f714f9de35cfd7d83b850e3d9b14aa0a365f2b287ee3029fe0e2d44f4f6a.jpg)  
◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

## Risk Reward – Coherent Corp (COHR.N)

Street Building In Material Margin Improvement as Capacity Comes Online

## PRICE TARGET \$330.00

\~28-30x Base FY28e EPS (\~\$11.50). Multiple trades at premium to historical trading range given AI exposure, trading more in-line with AI comps.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/0098bc1f69131e7aba3b84aeccef0fa8da55f7c78198ad8ca2d97eaf4534ded8.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/8077ed628a7f6faf63d410f1df61f33451fe95bc31be6d34305ad2a3fd28950a.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

\- Near-term AI/ML opportunity and potential earnings optionality as net interest expense is worked down
- Valuation reflects volatility in end demand, particularly against more challenging Analyst Day targets
- Several levers to improve earnings power, including gross margin improvements and debt reduction
- Believe in longer term growth opportunity given attractive focus on differentiated processes and diversified customer base, with meaningful exposure to AI opportunity

![](images/def25cf07cd4659b969b4dc3dd75686304a934576679d441adb3554d808d9b6d.jpg)

## Risk Reward Themes

<table><tr><td>Electric Vehicles:</td><td>Positive</td></tr><tr><td>Secular Growth:</td><td>Positive</td></tr><tr><td>Special Situation:</td><td>Positive</td></tr></table>

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

<table><tr><td>Drivers</td><td>Jun 2025</td><td>Jun 2026e</td><td>Jun 2027e</td><td>Jun 2028e</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>23.4</td><td>21.5</td><td>33.7</td><td>36.3</td></tr><tr><td>Gross Margin (%)</td><td>37.9</td><td>39.4</td><td>40.5</td><td>41.3</td></tr><tr><td>Operating Margin (%)</td><td>17.8</td><td>20.3</td><td>22.5</td><td>24.2</td></tr><tr><td>Net Debt / EBITDA</td><td>3.29</td><td>2.41</td><td>1.59</td><td>1.09</td></tr></table>

## INVESTMENT DRIVERS

• What is the risk of China insourcing?

\- Can 3D sensing still be an attractive market for COHR?

\- Can COHR get larger than expected synergies out of Coherent?

\- Can datacomm components capture outsized opportunity with AI?

GLOBAL REVENUE EXPOSURE  
![](images/a0492088e09f06fe3ea89e43dae6501abc650bcd2685ce06879e20b2d9e5e201.jpg)  
Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

<table><tr><td>5/5BEST</td><td>24 MonthHorizon</td><td>5/5MOST</td><td>3 MonthHorizon</td></tr></table>

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

<table><tr><td>Inst. Owners, % Active</td><td>57%</td><td></td><td></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>2.1x</td><td></td><td></td></tr><tr><td>HF Sector Net Exposure</td><td>29.5%</td><td></td><td></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

MS ESTIMATES VS. CONSENSUS  
![](images/86b00efc58b01aa1786d123c419987903e07aeae5fb15153fed61b6c724982ff.jpg)  
◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

## Risk Reward – Keysight Technologies Inc (KEYS.N)

Architecture-Agnostic Play on AI

## PRICE TARGET \$400.00

Our base case valuation reflects \~33x on FY27 Base Case EPS of \~\$12. Tariff impact removed, allowing stock to trade closer to 2x P/E/G.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/44cef0fb1afef5138ad710cdd0fcba5cbfe06182944cc13738b3668f331846af.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/ab590b96c85c8242f68bbac5f8db3c14918d466a6a428d2fe3d8b76a53f959ea.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## OVERWEIGHT THESIS

■ Architecture optionality is the core AI thesis. KEYS benefits as AI networks evolve across Ethernet, InfiniBand, copper, pluggables, LPO, NPO and CPO, with more architectures driving more test demand.
■ AI upside with lower volatility. AI revenue is scaling quickly, but KEYS also has durable support from A&D, semiconductor test and wireless, reducing reliance on one capex cycle.

■ Better growth converting into better margins. Backlog conversion, higher test density, software mix and acquisitions should support continued estimate revisions and operating leverage.

![](images/9e5c68550049de64ab7d7e37a395febf01f135ce262ed2645e4260ccfe3ceb08.jpg)  
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

<table><tr><td>Drivers</td><td>Oct 2025</td><td>Oct 2026e</td><td>Oct 2027e</td><td>Oct 2028e</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>8.0</td><td>28.1</td><td>11.7</td><td>7.2</td></tr><tr><td>Gross Margin (%)</td><td>64.6</td><td>68.7</td><td>68.5</td><td>67.8</td></tr><tr><td>Operating Margin (%)</td><td>25.9</td><td>29.7</td><td>31.0</td><td>30.9</td></tr><tr><td>FCF Growth Y/Y (%)</td><td>63.3</td><td>5.6</td><td>15.9</td><td>3.7</td></tr></table>

## INVESTMENT DRIVERS

5G Investment, R&D Budgets

## GLOBAL REVENUE EXPOSURE

![](images/0c6707e2d67682d6ab0ad97f64779436e1fe117e8f82f9d442050d07e8310017.jpg)  
Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

<table><tr><td>5/5BEST</td><td>24 MonthHorizon</td><td><img src="images/a7ba891ab232c1a3669bab84cff447818e71edf79d8174973e261507b3015ab8.jpg"/></td><td>3 MonthHorizon</td></tr></table>

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

<table><tr><td>Inst. Owners, % Active</td><td>55.4%</td><td></td><td></td><td></td><td></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>2.1x</td><td></td><td></td><td></td><td></td></tr><tr><td>HF Sector Net Exposure</td><td>29.5%</td><td></td><td></td><td></td><td></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

MS ESTIMATES VS. CONSENSUS  
![](images/d5ac8fb9f3100a762b868c0d2053cea57c8d171eb1dd0c6327fe15e13947844a.jpg)  
Mean MS Estimates Source: Refinitiv, MS

## Risk Reward – Corning Inc (GLW.N)

Exp'd Margin Leverage and Scale-Up Opportunity Driving Stock Towards Bull Case

## PRICE TARGET \$180.00

Our base case valuation reflects \~35x on FY28 Base Case earnings power of \~\$5.1. Our multiple represents a premium to GLW's traditional trading range over the last 10 years given AI megatrend.

## Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/8dd467db62233572a9c725808c085ec249a603a97aa0158efc1c79074a50c206.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/5632da668d59187b3e926b40b0735c621705d63d0c842b4143c6f4b1388bae3a.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 10 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

■ Display business, which generates majority of earnings, operates efficiently. Additional currency related price increases support margins.

■ Optical business sees resumption in growth as carrier fiber deployments pick up, and also benefits from AI datacenter demand for fiber.

■ Consumer businesses see slow recovery, particularly given weaker macro

![](images/1ca4a7565d7ef6cd852d5d90d66c86484f84942d909b841ac93d8e37ceee4e78.jpg)

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

<table><tr><td>Drivers</td><td>Dec 2025</td><td>Dec 2026e</td><td>Dec 2027e</td><td>Dec 2028e</td></tr><tr><td>Total Revenue ($, mm)</td><td>15,629</td><td>17,646</td><td>21,523</td><td>26,610</td></tr><tr><td>Gross Margin (%)</td><td>36.0</td><td>37.3</td><td>38.3</td><td>38.9</td></tr><tr><td>Free Cash Flow ($, mm)</td><td>1,413</td><td>1,379</td><td>1,870</td><td>2,265</td></tr><tr><td>EPS Growth Y/Y (Non-GAAP) (%)</td><td>29.0</td><td>21.7</td><td>34.4</td><td>33.3</td></tr></table>

## INVESTMENT DRIVERS

\- Optical fiber deployments from service providers

• Consumer spending (mobile devices, TVs)

\- Incremental adoption of core technologies (glass, ceramics, optical physics) across more end markets / verticals (i.e. auto glass)

## GLOBAL REVENUE EXPOSURE

![](images/0c41a5437e0eaef472ce3fdb6f656fac0e64e5298883eb90b5cc80cb2f8524fb.jpg)  
Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

<table><tr><td>5/5BEST</td><td>24 MonthHorizon</td><td>5/5MOST</td><td>3 MonthHorizon</td></tr></table>

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

<table><tr><td>Inst. Owners, % Active</td><td>51.2%</td><td></td><td></td><td></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>2.1x</td><td></td><td></td><td></td></tr><tr><td>HF Sector Net Exposure</td><td>29.5%</td><td></td><td></td><td></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

MS ESTIMATES VS. CONSENSUS  
![](images/fec9adb1e2cde7352f9c105045a4ef448c760cd7a7c6189f1f6239870fca9303.jpg)  
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

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Meta A Marshall; Joseph Moore.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

The analyst or strategist (or a household member) identified below owns the following securities (or related derivatives): Antonio Jaramillo - Arista Networks(common or preferred stock), Astera Labs Inc(common or preferred stock), Broadcom Inc.(common or preferred stock), Qualcomm Inc.(common or preferred stock), Wolfspeed, INC(common or preferred stock); Meta A Marshall - Advanced Micro Devices(common or preferred stock), Broadcom Inc.(common or preferred stock), Corning Inc(common or preferred stock), NVIDIA Corp.(common or preferred stock).

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Advanced Micro Devices, Aeva Technologies Inc, Allegro Microsystems Inc, Ambarella Inc, Analog Devices Inc., Arista Networks, Arm Holdings plc, Astera Labs Inc, Axon Enterprise Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, F5 Inc, Intel Corporation, IonQ Inc, Keysight Technologies Inc, Lumentum Holdings Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., Motorola Solutions Inc, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qorvo Inc, Qualcomm Inc., SanDisk Corporation., Semtech Corp., Silicon Laboratories Inc., Skyworks Solutions Inc, Synopsys Inc., Texas Instruments, Wolfspeed, INC, Zebra Technologies Corporation. Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Aeva Technologies Inc, Broadcom Inc., Cerebras Systems, GlobalFoundries Inc, Intel Corporation, Lumentum Holdings Inc, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Quantinuum, Semtech Corp..

Within the last 12 months, MS has received compensation for investment banking services from Advanced Micro Devices, Aeva Technologies Inc, Allegro Microsystems Inc, Amkor Technology Inc, Analog Devices Inc., Broadcom Inc., Cerebras Systems, Coherent Corp, Corning Inc, Intel Corporation, IonQ Inc, Lumentum Holdings Inc, Micron Technology Inc., Motorola Solutions Inc, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Quantinuum, Semtech Corp., Texas Instruments, Zebra Technologies Corporation.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Micro Devices, Aeva Technologies Inc, Allegro Microsystems Inc, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Arista Networks, Arm Holdings plc, Astera Labs Inc, Axon Enterprise Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, F5 Inc, GlobalFoundries Inc, Intel Corporation, IonQ Inc, Keysight Technologies Inc, Lumentum Holdings Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., Motorola Solutions Inc, Navitas Semiconductor Corp, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qualcomm Inc., Quantinuum, SanDisk Corporation., Semtech Corp., Silicon Laboratories Inc., Skyworks Solutions Inc, Synopsys Inc., Texas Instruments, Wolfspeed, INC, Zebra Technologies Corporation.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Advanced Micro Devices, Allegro Microsystems Inc, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Axon Enterprise Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, GlobalFoundries Inc, Intel Corporation, Lumentum Holdings Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., Motorola Solutions Inc, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qorvo Inc, Qualcomm Inc., Semtech Corp., Silicon Laboratories Inc., Synopsys Inc., Texas Instruments, Zebra Technologies Corporation.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Advanced Micro Devices, Aeva Technologies Inc, Allegro Microsystems Inc, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Arista Networks, Arm Holdings plc, Astera Labs Inc, Axon Enterprise Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, F5 Inc, GlobalFoundries Inc, Intel Corporation, IonQ Inc, Keysight Technologies Inc, Lumentum Holdings Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., Motorola Solutions Inc, Navitas Semiconductor Corp, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qualcomm Inc., Quantinuum, SanDisk Corporation., Semtech Corp., Silicon Laboratories Inc., Skyworks Solutions Inc, Synopsys Inc., Texas Instruments, Wolfspeed, INC, Zebra Technologies Corporation.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Advanced Micro Devices, Allegro Microsystems Inc, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Axon Enterprise Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, GlobalFoundries Inc, Intel Corporation, IonQ Inc, Lumentum Holdings Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., Motorola Solutions Inc, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qorvo Inc, Qualcomm Inc., Semtech Corp., Silicon Laboratories Inc., Synopsys Inc., Texas Instruments, Wolfspeed, INC, Zebra Technologies Corporation.

MS & Co. LLC makes a market in the securities of Aeva Technologies Inc, Ambarella Inc, Cerebras Systems, Ciena Corporation, F5 Inc, Keysight Technologies Inc, Motorola Solutions Inc, Quantinuum, Silicon Laboratories Inc..

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.
Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

## (as of June 30, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1544</td><td>42%</td><td>453</td><td>49%</td><td>29%</td><td>757</td><td>44%</td></tr><tr><td>Equal-weight/Hold</td><td>1577</td><td>43%</td><td>390</td><td>42%</td><td>25%</td><td>769</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>1</td><td>0%</td><td>33%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>544</td><td>15%</td><td>89</td><td>10%</td><td>16%</td><td>204</td><td>12%</td></tr><tr><td>Total</td><td>3,668</td><td></td><td>933</td><td></td><td></td><td>1731</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

## Important Disclosures for MS Smith Barney LLC Customers

Important disclosures regarding any material conflict of interest that can reasonably be expected to have influenced MS Smith Barney LLC's choice of a third-party research provider or the subject company of a third-party research report, are available on the MS Wealth Management disclosure website at www.morganstanley.com/online/researchdisclosures. For MS specific disclosures, you may refer to https://www.morganstanley.com/eqr/disclosures/webapp/generalresearch.

Each MS report is reviewed and approved on behalf of MS Smith Barney LLC. This review and approval is conducted by the same person who reviews the research report on behalf of MS. This could create a conflict of interest.

## Other Important Disclosures

A member of Research who had or could have had access to the research prior to completion owns securities (or related derivatives) in the Cisco Systems Inc, Micron Technology Inc., NVIDIA Corp.. This person is not a research analyst or a member of research analyst's household.

MS policy is to update research reports as and when the Research Analyst and Research Management deem appropriate, based on developments with the issuer, the sector, or the market that may have a material impact on the research views or opinions stated therein. In addition, certain Research publications are intended to be updated on a regular periodic basis (weekly/monthly/quarterly/annual) and will ordinarily be updated with that frequency, unless the Research Analyst and Research Management determine that a different publication schedule is appropriate based on current conditions.

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS produces an equity research product called a "Tactical Idea." Views contained in a "Tactical Idea" on a particular stock may be contrary to the recommendations or views expressed in research on the same stock. This may be the result of differing time horizons, methodologies, market events, or other factors. For all research available on a particular stock, please contact your sales representative or go to Matrix at http://www.morganstanley.com/matrix.

MS is provided to our clients through our proprietary research portal on Matrix and also distributed electronically by MS to clients. Certain, but not all, MS products are also made available to clients through third-party vendors or redistributed to clients through alternate electronic means as a convenience. For access to all available MS, please contact your sales representative or go to Matrix at http://www.morganstanley.com/matrix.

Any access and/or use of MS is subject to MS's Terms of Use (http://www.morganstanley.com/terms.html). By accessing and/or using MS, you are indicating that you have read and agree to be bound by our Terms of Use (http://www.morganstanley.com/terms.html). In addition you consent to MS processing your personal data and using cookies in accordance with our Privacy Policy and our Global Cookies Policy (http://www.morganstanley.com/privacy\_pledge.html), including for the purposes of setting your preferences and to collect readership data so that we can deliver better and more personalized service and products to you. To find out more information about how MS processes personal data, how we use cookies and how to reject cookies see our Privacy Policy and our Global Cookies Policy (http://www.morganstanley.com/privacy\_pledge.html). Please use the provided link to review the Terms and Conditions and Most Important Terms and Conditions for MS India Company Private Limited (https://www.morganstanley.com/assets/pdfs/about-us-global-offices/india/Terms\_and\_conditions.pdf) and the following link to review the audit report (https://ny.matrix.ms.com/eqr/research/webapp/researchdocs/MSICPL\_Morgan\_Stanley\_Research\_Audit\_Report.pdf).

If you do not agree to our Terms of Use and/or if you do not wish to provide your consent to MS processing your personal data or using cookies please do not access our research. MS does not provide individually tailored investment advice. MS has been prepared without regard to the circumstances and objectives of those who receive it. MS recommends that investors independently evaluate particular investments and strategies, and encourages investors to seek the advice of a financial adviser. The appropriateness of an investment or strategy will depend on an investor's circumstances and objectives. The securities, instruments, or strategies discussed in MS may not be suitable for all investors, and certain investors may not be eligible to purchase or participate in some or all of them. MS is not an offer to buy or sell or the solicitation of an offer to buy or sell any security/instrument or to participate in any particular trading strategy. The value of and income from your investments may vary because of changes in interest rates, foreign exchange rates, default rates, prepayment rates, securities/instruments prices, market indexes, operational or financial conditions of companies or other factors. There may be time limitations on the exercise of options or other rights in securities/instruments transactions. Past performance is not necessarily a guide to future performance. Estimates of future performance are based on assumptions that may not be realized. If provided, and unless otherwise stated, the closing price on the cover page is that of the primary exchange for the subject company's securities/instruments.

The fixed income research analysts, strategists or economists principally responsible for the preparation of MS have received compensation based upon various factors, including quality, accuracy and value of research, firm profitability or revenues (which include fixed income trading and capital markets profitability or revenues), client feedback and competitive factors. Fixed Income Research analysts', strategists' or economists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

The "Important Regulatory Disclosures on Subject Companies" section in MS lists all companies mentioned where MS owns 1% or more of a class of common equity securities of the companies. For all other companies mentioned in MS, MS may have an investment of less than 1% in securities/instruments or derivatives of securities/instruments of companies and may trade them in ways different from those discussed in MS. Employees of MS not involved in the preparation of MS may have investments in securities/instruments or derivatives of securities/instruments of companies mentioned and may trade them in ways different from those discussed in MS. Derivatives may be issued by MS or associated persons.

With the exception of information regarding MS, MS is based on public information. MS makes every effort to use reliable, comprehensive information, but we make no representation that it is accurate or complete. We have no obligation to tell you when opinions or information in MS change apart from when we intend to discontinue equity research coverage of a subject company. Facts and views presented in MS have not been reviewed by, and may not reflect information known to, professionals in other MS business areas, including investment banking personnel.

MS personnel may participate in company events such as site visits and are generally prohibited from accepting payment by the company of associated expenses unless pre-approved by authorized members of Research management.

MS may make investment decisions that are inconsistent with the recommendations or views in this report.

To our readers based in Taiwan or trading in Taiwan securities/instruments: Information on securities/instruments that trade in Taiwan is distributed by MS Taiwan Limited ("MSTL"). Such information is for your reference only. The reader should independently evaluate the investment risks and is solely responsible for their investment decisions. MS may not be distributed to the public media or quoted or used by the public media without the express written consent of MS. Any non-customer reader within the scope of Article 7-1 of the Taiwan Stock Exchange Recommendation Regulations accessing and/or receiving MS is not permitted to provide MS to any third party (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities regarding MS which may create or give the appearance of creating a conflict of interest. Information on securities/instruments that do not trade in Taiwan is for informational purposes only and is not to be construed as a recommendation or a solicitation to trade in such securities/instruments. MSTL may not execute transactions for clients in these securities/instruments.

MS is not incorporated under PRC law and the research in relation to this report is conducted outside the PRC. MS does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC. PRC investors shall have the relevant qualifications to invest in such securities and shall be responsible for obtaining all relevant approvals, licenses, verifications and/or registrations from the relevant governmental authorities themselves. Neither this report nor any part of it is intended as, or shall constitute, provision of any consultancy or advisory service of securities investment as defined under PRC law. Such information is provided for your reference only.

MS is disseminated in Brazil by MS C.T.V.M. S.A. located at Av. Brigadeiro Faria Lima, 3600, 6th floor, São Paulo - SP, Brazil; and is regulated by the Comissão de Valores Mobiliários; in Mexico by MS México, Casa de Bolsa, S.A. de C.V which is regulated by Comision Nacional Bancaria y de Valores. Paseo de los Tamarindos 90, Torre 1, Col. Bosques de las Lomas Floor 29, 05120 Mexico City; in Japan by MS MUFG Securities Co., Ltd. and, for Commodities related research reports only, MS Capital Group Japan Co., Ltd; in Hong Kong by MS Asia Limited (which accepts responsibility for its contents) and by MS Bank Asia Limited; in Singapore by MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS) and by MS Bank Asia Limited, Singapore Branch (Registration number T14FC0118); in Australia to "wholesale clients" within the meaning of the Australian Corporations Act by MS Australia Limited A.B.N. 67 003 734-576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents; in Australia to "wholesale clients" and "retail clients" within the meaning of the Australian Corporations Act by MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Telecom & Networking Equipment

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/10/2026)</td></tr><tr><td colspan="3">Meta A Marshall</td></tr><tr><td>Arista Networks (ANET.N)</td><td>O (10/31/2023)</td><td>$186.96</td></tr><tr><td>Axon Enterprise Inc (AXON.O)</td><td>O (12/03/2024)</td><td>$565.80</td></tr><tr><td>Ciena Corporation (CIEN.N)</td><td>E (10/10/2025)</td><td>$460.72</td></tr><tr><td>Cisco Systems Inc (CSCO.O)</td><td>O (04/08/2024)</td><td>$121.31</td></tr><tr><td>Coherent Corp (COHR.N)</td><td>E (12/13/2023)</td><td>$324.50</td></tr><tr><td>Corning Inc (GLW.N)</td><td>E (06/13/2024)</td><td>$190.89</td></tr><tr><td>F5 Inc (FFIV.O)</td><td>E (04/12/2022)</td><td>$430.39</td></tr><tr><td>Keysight Technologies Inc (KEYS.N)</td><td>O (07/13/2026)</td><td>$322.05</td></tr><tr><td>Lumentum Holdings Inc (LITE.O)</td><td>E (05/12/2021)</td><td>$802.01</td></tr><tr><td>Motorola Solutions Inc (MSI.N)</td><td>O (12/17/2025)</td><td>$422.88</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.
\* Historical prices are not split adjusted.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/10/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$557.89</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$20.99</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$54.87</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$77.30</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$70.47</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$395.65</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$412.97</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$399.97</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$215.08</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$68.97</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$109.84</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$42.86</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$235.81</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$88.59</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$979.30</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$13.47</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$210.96</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$292.26</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$95.96</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$85.81</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$189.16</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$70.45</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,915.92</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$136.13</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$218.63</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$60.38</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$311.46</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$35.29</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$323.39</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$384.17</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$445.50</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS