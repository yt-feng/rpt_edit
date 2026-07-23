July 21, 2026 02:47 PM GMT

Greater China Semiconductors | Asia Pacific

# 2026 Shanghai WAIC takeaways: SuperPods enabled by China's scale-up technology

Domestic AI competition is moving up the stack—from accelerator specifications to SuperPods, workload scheduling, and full-system utilization.

From new accelerators to system-level scaling: WAIC 2026 featured fewer major chip launches and a much broader range of SuperPod solutions. Almost every domestic accelerator vendor displayed a 64- or 128-card scale-up system, enabled by Chinese AI GPU vendors' proprietary scale-up technology (vs. global peers – Nvidia's NVLink or AMD's UALink). See Exhibit 4 for the scale-up technology comparison. As we wrote in China's AI Accelerators – Who's Poised to Win?, although Chinese AI GPUs are limited by wafer process at the chip level, they are strong in optical networking and server rack design at the system level (Exhibit 11).

Competition in China's AI computing market is shifting from standalone chip specifications toward interconnects, memory sharing, and system reliability: In WAIC 2025, focus was on: 1) strong inference demand, 2) AI applications expanding beyond chatbots, 3) Huawei's launch of the 384-NPU CloudMatrix 384, and 4) new accelerators from multiple domestic vendors.

## Other highlights:

\- AI server systems: Huawei scales up beyond 1,000 NPUs: Huawei's Atlas 950 expands the scale-up domain from 384 Ascend 910C processors to 1,024 next-generation Ascend 950DT NPUs, combined with hybrid copper-and-optical interconnects and optical-path protection, Atlas 950 represents an important hardware foundation for domestic large-model training.

\- AI GPU chips: Prefill and Decode (P/D) disaggregation emerges as a new inference theme: Separating computing-intensive prefill from bandwidth- and latency-sensitive decoding enables operators to optimize hardware allocation and schedule independently. Details in the following section.

\- Along with the WAIC, we also hosted a China Tech Tour on July 16–17. Please see our China Tech Tour: Key Takeaways.

Stock implications: Within domestic AI computing, we prefer Cambricon (OW), Iluvatar (OW), and Hygon (OW), given strong order visibility and solid supply chain; we remain EW on MetaX. Among key enablers, we prefer SMIC (OW) for advanced-node capacity expansion; we are EW on Hua Hong, where strong AI PMIC demand should support specialty-wafer pricing. Continued investment in domestic memory and logic manufacturing benefits semiconductor equipment; our preferred plays are NAURA (OW), AMEC (OW), ACM Research (OW), and ASMPTc (OW).

MS TAIWAN LIMITED+
Charlie Chan
Equity Analyst
Charlie.Chan@morganstanley.com +886 2 2730-1725

Henry Zhao
Research Associate
Henry.Zhao@morganstanley.com +852 2239-7731

Daisy Dai, CFA
Equity Analyst
Daisy.Dai@morganstanley.com +852 2848-7310

Daniel Yen, CFA
Equity Analyst
Daniel.Yen@morganstanley.com +886 2 2730-2863

Lucas Wang
Research Associate
Lucas.Wang@morganstanley.com +886 2 2730-2875

Tiffany Yeh
Equity Analyst
Tiffany.Yeh@morganstanley.com +886 2 7712-3032

Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

![](images/7ad1e459a4513a7b3985904424f2c8d285eb0b3dbf25acb53f15ec5d0cf4674d.jpg)  
GREATER CHINA TECHNOLOGY SEMICONDUCTORS
Asia Pacific
Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Key Takeaways from 2026 WAIC

## Huawei Ascend: scaling the SuperPod beyond 1,000 NPUs

Huawei unveiled its next-generation Atlas 950 SuperPod at WAIC, marking another significant step-up in its scale-up architecture: Based on our checks at the event, the new system is primarily designed for Huawei's next-generation Ascend 950DT series, rather than the currently shipping 950PR series. Compared with the CloudMatrix 384 platform introduced in 2025, which connected 384 Ascend 910C processors, the Atlas 950 expands the scale-up domain to 1,024 NPUs. The system comprises 16 computing cabinets, each housing 64 NPUs, together with four dedicated UnifiedBus interconnect cabinets supporting all-to-all communication across the SuperPod.

System-level computing and memory capacity have increased materially: Each 64-NPU computing cabinet delivers up to 64 PFLOPS of FP8 performance and 128 PFLOPS of FP4 performance, implying aggregate SuperPod performance of approximately 1 EFLOPS FP8 and 2 EFLOPS FP4. Each computing cabinet contains around 6TB of HBM, translating into approximately 96TB across the 16 computing cabinets. By combining HBM with external DRAM through memory pooling, Huawei indicated that total addressable memory capacity could reach 256TB. The larger memory pool should be particularly relevant for large-model training, where model parameters, optimizer states, and intermediate data increasingly exceed the capacity of individual accelerator nodes.

UnifiedBus 2.0 is the key architectural upgrade, extending a common communication and memory protocol across physical layers: Within each blade, eight NPUs are connected through a full-mesh topology. At the cabinet level, eight blades—or 64 NPUs—are connected through a Clos fabric using a fully orthogonal, midplane-free design. Across cabinets, four UnifiedBus interconnect cabinets provide the optical scale-up fabric for the full 1,024-NPU system. The resulting architecture therefore remains physically hierarchical, but is logically flatter: rather than treating the rack and interconnect layers as separate communication domains, UnifiedBus provides common addressing, memory semantics and load/store operations across the entire SuperPod.

Overall, Atlas 950 moves Huawei's SuperPod architecture from several hundred to more than 1,000 tightly interconnected NPUs, laying the hardware foundation for large-model training on the next-generation 950DT platform. The use of copper links within computing cabinets and optical links between cabinets balances short-distance bandwidth and power efficiency with longer-distance scalability. Huawei has also incorporated optical-path protection so that a single-link failure does not interrupt system operation. This is important because, as cluster size rises, communication efficiency and fault tolerance become increasingly critical to maintaining effective computing utilization and stable training performance.

Exhibit 1: Huawei showcased its new Atlas 950 SuperPod at 2026 WAIC  
![](images/ea2ee4f22925c994fbc4831c76f55f1b985808a3e9e4841a3f9c23ea3d16cce7.jpg)  
Source: Company data, MS

Exhibit 2: NPU blade (tray) of Atlas 950 SuperPod  
![](images/0e4eb0ce22ccfba6776cc82ed629b97d97cf2dabd6559da0045679c58d2e71b4.jpg)  
Source: Company data, MS

Exhibit 3: The reverse side of Atlas 950 mainly showcases the optical interconnects adopted by UBlink  
![](images/e26d9de7e9756f384fb667ca0e431c16809c713c27f7227a8d78cee27ba01e3d.jpg)  
Source: Company data, MS

## A flourishing SuperPod landscape

If WAIC 2025 was primarily a showcase for domestic AI accelerators, WAIC 2026 demonstrated that the competitive focus has shifted from individual chips toward system-level scale-up: Nearly every domestic AI GPU and ASIC vendor displayed a SuperPod solution, typically co-developed with server ODMs and networking partners. As a result, we observed several similar or identical system designs appearing across different booths. This reflects the increasingly modular nature of China's AI server ecosystem: accelerator vendors provide the computing platform and software stack, while ODMs integrate servers, interconnects, cooling and power infrastructure into rack- or cluster-level solutions.

Scale-up configurations of 64–128 accelerators have become increasingly common: Compared with earlier domestic systems centered on eight-card servers or relatively small clusters, the latest solutions seek to connect multiple computing trays or racks within a higher-bandwidth scale-up domain. The broader adoption of 64- and 128-card architectures suggests that domestic vendors are placing greater emphasis on collective communication efficiency, memory sharing and system-level utilization. However, the repeated appearance of similar ODM-developed platforms also indicates that differentiation will increasingly depend on interconnect performance, software optimization, fault tolerance, and effective application throughput—not simply the number of accelerators connected.

We also observed greater architectural diversity in rack-level interconnects, including orthogonal and conventional cable-tree solutions: In an orthogonal architecture, front and rear boards are arranged perpendicular to each other, allowing high-speed connectors to mate directly across the two planes. Domestic vendors including Huawei and ZTE increasingly favor midplane-free orthogonal designs, which eliminate the large central PCBs used in conventional backplanes. This can reduce the manufacturing and yield challenges associated with a large, high-layer-count midplane and shorten certain electrical paths. The trade-off is greater mechanical and connector-design complexity, while achievable bandwidth still depends on connector density, channel loss and signal-integrity engineering.

## Domestic AI server configurations remain centered on GPU-to-CPU ratios of

approximately 4:1 or 8:1. We believe this partly reflects the current workload mix. China's agentic AI demand has yet to scale materially, while many deployments remain focused on conventional model inference or selected training workloads. Domestic accelerators also currently deliver lower per-card computing performance than leading overseas products, meaning that accelerator throughput—not host-CPU capacity—is often the primary system bottleneck. As agentic workloads expand and require more data preprocessing, orchestration, retrieval and tool execution, demand for additional CPU resources could rise, potentially changing the optimal CPU-to-accelerator configuration over time.

Exhibit 4: Comparison of some key SuperPod solutions at 2026 WAIC

<table><tr><td>Solution</td><td>Vendor / Partner</td><td>Scale</td><td>Architecture Highlights</td><td>Key Differentiator</td></tr><tr><td>Atlas 950</td><td>Huawei</td><td>1,024 Ascend 950DT NPUs</td><td>16 compute cabinets + 4 UnifiedBus cabinets; UnifiedBus 2.0 unified memory semantics; hybrid copper + optical interconnect; up to 256TB pooled memory</td><td>Largest scale-up domain showcased at WAIC, emphasizing large-model training and unified memory architecture</td></tr><tr><td>MTT C256 SuperPod</td><td>Moore Threads</td><td>128-256 S series GPGPU</td><td>Single-level scale up with cabletree connections.</td><td>Focus on scalable domestic GPU clusters for AI training and inference</td></tr><tr><td>Yunsui SL64-O</td><td>Enflame + ZTE</td><td>64 L600 AI accelerators</td><td>Co-developed rack-level solution using midplane-free orthogonal architecture integrating compute, networking and cooling</td><td>Demonstrates ODM-driven ecosystem collaboration and modular SuperPod deployment</td></tr><tr><td>Xijing S6000</td><td>MetaX + ZTE</td><td>64 C600 AI accelerators</td><td>Similar as Yunsui SL64-o, using midplane-free orthogonal architecture</td><td>Equipped with latest MetaX AI training + inference accelerator, C600 chip</td></tr></table>

Source: Company data, MS

Exhibit 5: Enflame showed its SuperPod solution, co-developed with ZTE  
![](images/b834e21fb641ff2aa530035748c701e50d2dad5b29ac7892d2234f8cd2b64a67.jpg)  
Source: Company data, MS

Exhibit 6: Midplane-free orthogonal designs at WAIC  
![](images/62dd0a52e01a6b83a9f71077c6d48e861dc0eb4bb319fd5c72496fe517927f81.jpg)  
Source: Company data, MS

## P/D disaggregation enables more efficient heterogeneous inference

Reducing token costs while improving utilization of available accelerator resources was another recurring theme at WAIC: Large-model inference consists of two workloads with materially different characteristics. Prefilling processes the input prompt in parallel, generates the initial KV cache, and is primarily compute-intensive. Decoding generates subsequent tokens sequentially, repeatedly accessing model weights and the expanding KV cache, making it more sensitive to memory bandwidth, latency and batch scheduling. Running both phases on the same accelerator pool can create resource contention and utilization imbalances as model sizes, prompt lengths and concurrent requests increase.

P/D disaggregation addresses this mismatch by placing prefilling and decoding on separate accelerator pools: This allows operators to configure and schedule each pool according to its workload characteristics, preventing long prefilling requests from interrupting latency-sensitive decoding jobs. It also enables heterogeneous deployment using different accelerators for each phase. One configuration discussed at WAIC allocated approximately 90% of domestic accelerator capacity to prefilling and 10% of H2O capacity to decoding, reportedly increasing throughput 54% and reducing P90 time-to-first-token 64%. Actual benefits will depend on model architecture, workload patterns, scheduling, and interconnect performance.

Attention/FFN disaggregation could represent the next stage, although we did not observe meaningful demonstrations or benchmark results at WAIC: This approach further divides decoding execution into attention nodes, which repeatedly access a growing KV cache and are highly sensitive to HBM capacity and bandwidth, and FFN nodes, which perform more compute-intensive operations using relatively fixed model weights—or selected experts in an MoE model. In theory, this could enable high-bandwidth, high-capacity memory systems for attention and more computing-oriented accelerators for FFN. However, frequent activation transfers between the two pools introduce substantial interconnect and synchronization requirements, making A/F disaggregation an emerging rather than production-ready architecture today.

## Iluvatar unveils Tiangai 300 for full-stage AI inference

Iluvatar launched its Tiangai 300 series at WAIC, expanding its product positioning toward both prefilling and decoding inference: The accelerator supports FP4, FP8, and BF16 data formats and increases memory capacity to 144GB. Based on our supply chain checks, Tiangai 300 will adopt HBM3E with approximately 4TB/s of memory bandwidth, which should improve its ability to handle the bandwidth-sensitive decoding phase alongside computing-intensive prefilling workloads. Iluvatar indicated that the architecture can execute matrix and vector operations in parallel, enabling faster long-context processing. Based on the company's testing of domestic LLMs, including DeepSeek V3.2 and GLM 5.2, Tiangai 300 delivered higher prefilling and decoding performance than Nvidia's H100.

Exhibit 7: Iluvatar's new Tiangai 300 chip shown at WAIC  
![](images/b7ae0bd7809c046a28967c1d2199016ee2816b046e3079ae9a911c4a45f9a984.jpg)  
Source: Company data, MS

## Oriental Computing: 3D stacking offers an alternative path beyond process scaling

A private company, Oriental Computing, showcased its DF1000, a software-defined near-memory 3D AI chip built using a domestic 14nm-class process. Conceptually similar to Huawei's T(Tao)-scaling vision, the design uses wafer-level hybrid bonding to vertically stack DRAM and logic dies, shortening data transfer distances and addressing the memory-wall bottleneck without relying solely on leading-edge process migration. The company claims memory bandwidth of 6.4TB/s and BF16 performance of 520TFLOPS, while a 128-card cluster has completed full-function stability validation. We view the product as another example of domestic vendors using architecture and advanced packaging to offset process-node constraints.

Exhibit 8: Oriental Computing unveiled a 3D stacking AI computing chip  
![](images/01cf8560b14c8df78d635ec97db041eb8278ed4b3b3366981a51631ca0f13b87.jpg)  
Source: Company data

## China Tech Tour: Key Takeaways

We hosted meetings with a number of Chinese semiconductor and AI semiconductor companies on July 16–17. Below, we summarize our key takeaways.

## OmniVision: New growth engines beyond smartphone CIS

Emerging-market CIS: Management remains constructive on action cameras, machine vision, AR/VR, and medical imaging, supported by specification upgrades and rising content. Action-camera CIS content can reach approximately US\$40 per device, versus US \$15–20 for earlier products. Machine vision is migrating from low-resolution sensors toward tens-of-megapixel products for high-precision inspection and humanoid robots, materially increasing system content. Disposable endoscopes support attractive profitability in medical imaging, while professional cameras could become another growth driver from 2027–28.

Automotive and smartphone CIS: Automotive demand should recover after a seasonally weak first quarter, supported by overseas ADAS adoption. Tight supply for select products allows OmniVision to prepare price increases and pass through potential foundry cost inflation, while customer localization requirements should support greater use of domestic manufacturing. By contrast, management remains cautious on smartphones given weak Android shipments, fewer model launches and specification downgrades amid higher memory costs. Higher-resolution products provide some support, but smartphones are unlikely to drive near-term growth.

Analog: Data center optical modules offer the clearest path toward scale and profitability. Customized analog products carry ASPs of approximately US\$2–3 per chip, with potential content of around US\$30 in a 1.6T NPO system. OmniVision is developing photodetectors, TIAs, SerDes and other optoelectronic-conversion products, supported by recently acquired communications expertise. Initial products have started ramping, with broader adoption expected over the next two years. Domestic substitution and overseas component shortages create further opportunities, although most products remain in development or early qualification.

## AMEC: Memory visibility remains strong; advanced logic opportunities broaden

Memory clients' orders: Management sees memory foundries as the segment with the strongest three-year demand visibility, driven more by localization and technology migration than global memory pricing. The DRAM client continues to add capacity and purchase R&D tools, while the NAND client is focused on technology upgrades and equipment replacement. Near-term NAND demand depends partly on replacing high-aspect-ratio etching and PECVD equipment, with larger expansion linked to next-generation 3D NAND. Several preliminary awards are converting into purchase orders and shipments, although a meaningful portion of potential 2027 demand has yet to be formally placed.

Advanced logic and localization: Management expects domestic advanced-logic investment to remain strong over the next five years. Equipment localization is already above 10%, while select production lines could reach 25–30%. AMEC is developing platforms for FinFET, GAA and 3D architectures and indicated that certain product launches are only around six months behind the global leader.

Product expansion and execution: Beyond etching, AMEC highlighted progress in ALD, CMP, inspection, and metrology. Overseas component lead times are lengthening, but management expects year-end deliveries to remain on schedule. Price negotiations from major clients have become less aggressive, operating expenses remain controlled, and R&D intensity should decline as new platforms are commercialized.

## Hua Hong: Pricing recovery and new capacity support growth

Utilization and pricing: Hua Hong's three 8-inch fabs are operating at approximately 110% utilization, while the first 12-inch fab also maintains high loading. Foundry prices have increased\~10–15% across both platforms since late last year, with further increases possible into 2027. Demand remains broad-based and is currently led by server-related applications, while power semiconductors are relatively weaker. Management will reduce loading for weaker power products rather than repurpose dedicated capacity.

Capacity ramp: The 9A fab currently has around 60kwpm of capacity, with the full 83kwpm expected to be ready by 3Q26 and fully loaded by 1H27. Focused mainly on 40–55nm products, it is targeted to become profitable by end-2027. Construction of 9B has begun, with 10–20kwpm expected by year-end and volume production starting in 2027. The fab will ultimately provide 55kwpm focused on 40–28nm. Depreciation will rise next year, but management expects revenue growth to outpace depreciation.

Acquisition and localization: The Rmb8.4bn HLMC Fab 5 acquisition is expected to close in August–September. The fab has 40kwpm of capacity, with profitability improving after Hua Hong assumed operational control. Hua Hong views 28nm as the practical limit for specialty processes, with potential applications including logic, NOR flash, MCUs and CIS.

## Iluvatar: Tiangai 300 Broadens Inference Coverage

Product roadmap: In addition to launching new products at WAIC, Iluvatar joined our meeting. Management is awaiting core customer feedback on Tiangai 300 and indicated that certain performance metrics exceed H100, although the product remains behind Blackwell. Tiangai 150 primarily targets prefilling, while Tiangai 300 extends into decoding and post-training. Iluvatar is also developing a SuperPod with fewer than 200 accelerators. Tiangai 400 is scheduled to tape out in 2027 and will benchmark against the Blackwell generation.

Shipments and customers: Iluvatar expects to ship approximately 100,000 cards this year, with next year's volume expected to be no lower. The company is initially prioritizing scalable inference deployments rather than aggressively pursuing large training clusters. Some Internet customers are already using its products, while recent fundraising by domestic LLM developers could support stronger accelerator spending next year. Management prefers large customers capable of meaningful deployments, given the engineering resources required to support smaller installations.

Supply chain and costs: Iluvatar targets an approximately 50:50 split between overseas and domestic production capacity next year, subject to US policy and domestic

manufacturing progress. Localization should increase longer term, supported by dual-die architectures and inter-die connectivity developed since 2023. The July placement was mainly intended to secure supply-chain resources and support 2027 growth. Iluvatar has around Rmb10bn in cash and is negotiating additional credit facilities. Memory already represents more than half of card cost, while foundry prices are also rising; Tiangai 300 pricing may therefore include HBM cost pass-through mechanisms.

## JCET: Accelerating advanced packaging expansion

JCET Group is accelerating its AI chip packaging expansion: This includes a CNY7.8 billion (US\$1.1 billion) investment in a new advanced packaging and testing plant in Shanghai Lingang, strengthening capacity for AI computing, high-performance chips. Besides this newly announced fab, JME based in Jiangyin is also for 2.5D packaging; that fab achieved Rmb200mn revenue last year. Management believes we are Chinese AI GPU ramp-up is in early innings amid a multi-year structural trend.

JCET follows the market regarding OSAT pricing: Despite tight supply of substrate, there is limited impact on production, while could affect newly added capacity.

The company maintained its Rmb10bn capex target for this year and sees 2027 capex as likely to be higher: 1Q26 utilization was around 80% and 2Q26 utilization improved sequentially.

## Key Charts for Chinese AI Semis

Exhibit 9: We expect China's AI GPU TAM to grow to US\$91bn by 2030  
![](images/8923fc6dec2cc8de5c4fd127095d400ab5c928aca99bee2172f541d62d3c7546.jpg)  
China CSP Telecom operator Sovereign & SOEs Others Overseas capex  
Source: Company data, MS estimates

Exhibit 10: We expect China's AI chip self-sufficiency to reach 70% in 2030e  
![](images/b3954184bb5aaaeb5e944b72fdcac0982288efd9860f9af8bb7f170d61b350d3.jpg)  
Source: Company data, MS estimates

Exhibit 11: Relative strengths of AI industries in the US and China  
![](images/bbf210b65a34c50370c3da68f34035cdce38f94677c3eb3c2fc38fc4758f461c.jpg)  
Source: MS

Exhibit 12: Average token price for China's mainstream AI LLMs  
![](images/561784ac9e365c1e48cd0b4c71046cf8dfde05dd97023c1507e0a4a24148c958.jpg)  
Source: Company data, MS

Exhibit 13: Surge in ByteDance (Volcano Engine/Doubao) tokens indicates high AI demand  
![](images/83004de0832990080643f5fca6ddaa621d9686d2f2b77909a69f9473a9149670.jpg)  
Source: Company data, MS. ByteDance numbers represent monthly run-rate based on daily numbers.

Exhibit 14: Chinese CSPs' capex will be a key demand driver for Chinese AI GPUs  
![](images/297274f83572aee4d8f4ddadc26ddbb161835cacd851d7b9f08524d25e90cf37.jpg)  
Source: Company data, MS (E) estimates

Exhibit 15:  
Domestic chips have lower TCO and comparable per token cost (AI LLM inference) vs. NVIDIA's processors for China  
![](images/a606ab2c8b11fcf071f4d3e59f6393f1c53e08b5818e9913b28f9f6fe8ee42eb.jpg)  
Source: Company data, MS estimates

This report references U.S. Executive Order 14032 and/or entities or securities that are designated thereunder. U.S. persons may be prohibited from buying certain securities of entities named in this report. Readers are solely responsible for ensuring that their investment activities are carried out in compliance with applicable laws.

This report references export controls and/or entities that may be subject to export control restrictions. Readers are solely responsible for ensuring that their investment or trade activities are carried out in compliance with applicable laws.

This report references U.S. Executive Order 14105 and/or entities that may be in scope of such order. U.S. persons may be prohibited from engaging in certain transactions or otherwise require certain other transactions be notified to the U.S. Department of Treasury. Readers are solely responsible for ensuring that their investment or trade activities are carried out in compliance with applicable laws.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Charlie Chan; Daisy Dai, CFA; Tiffany Yeh; Daniel Yen, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: ACM Research Inc, Advanced Micro-Fabrication Equipment Inc, Advanced Wireless Semiconductor Co, Alchip Technologies Ltd, AllRing Tech Co., AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMPT Ltd, Cambricon Technology Corporation, Dosilicon Co Ltd, FOCI Fiber Optic Communications Inc, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Hangzhou Silan Microelectronics Co. Ltd., King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, Montage Technology Co Ltd, Parade Technologies Ltd, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, SG Micro Corp., Shanghai Fudan Microelectronics, Silergy Corp., Silicon Motion, TSMC, UMC, Unigroup Guoxin Microelectronics Co Ltd, Vanguard International Semiconductor, WIN Semiconductors Corp, Winbond Electronics Corp, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Alchip Technologies Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co.

Within the last 12 months, MS has received compensation for investment banking services from ASMPT Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Montage Technology Co Ltd, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd..

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

Certain information in MS was sourced by employees of the Shanghai Representative Office of MS Asia Limited for the use of MS Asia Limited. MS is not incorporated under PRC law and the research in relation to this report is conducted outside the PRC. MS does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC. PRC investors shall have the relevant qualifications to invest in such securities and shall be responsible for obtaining all relevant approvals, licenses, verifications and/or registrations from the relevant governmental authorities themselves. Neither this report nor any part of it is intended as, or shall constitute, provision of any consultancy or advisory service of securities investment as defined under PRC law. Such information is provided for your reference only.

MS is disseminated in Brazil by MS C.T.V.M. S.A. located at Av. Brigadeiro Faria Lima, 3600, 6th floor, São Paulo - SP, Brazil; and is regulated by the Comissão de Valores Mobiliários; in Mexico by MS México, Casa de Bolsa, S.A. de C.V which is regulated by Comision Nacional Bancaria y de Valores. Paseo de los Tamarindos 90, Torre 1, Col. Bosques de las Lomas Floor 29, 05120 Mexico City; in Japan by MS MUFG Securities Co., Ltd. and, for Commodities related research reports only, MS Capital Group

Japan Co., Ltd; in Hong Kong by MS Asia Limited (which accepts responsibility for its contents) and by MS Bank Asia Limited; in Singapore by MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS) and by MS Bank Asia Limited, Singapore Branch (Registration number T14FC0118); in Australia to "wholesale clients" within the meaning of the Australian Corporations Act by MS Australia Limited A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents; in Australia to "wholesale clients" and "retail clients" within the meaning of the Australian Corporations Act by MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of ASMPT Ltd, Hua Hong Semiconductor Ltd, Montage Technology Co Ltd listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Greater China Technology Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/21/2026)</td></tr><tr><td colspan="3">Charlie Chan</td></tr><tr><td>ACM Research Inc (ACMR.O)</td><td>O (03/07/2023)</td><td>US$82.52</td></tr><tr><td>Advanced Micro-Fabrication Equipment Inc (688012.SS)</td><td>O (11/06/2023)</td><td>Rmb407.89</td></tr><tr><td>Advanced Wireless Semiconductor Co (8086.TWO)</td><td>U (07/14/2025)</td><td>NT$119.50</td></tr><tr><td>Alchip Technologies Ltd (3661.TW)</td><td>O (05/14/2021)</td><td>NT$3,490.00</td></tr><tr><td>ASE Technology Holding Co. Ltd. (3711.TW)</td><td>O (09/15/2024)</td><td>NT$633.00</td></tr><tr><td>Cambricon Technology Corporation (688256.SS)</td><td>O (04/27/2026)</td><td>Rmb1,350.02</td></tr><tr><td>Global Unichip Corp (3443.TW)</td><td>O (06/24/2026)</td><td>NT$4,115.00</td></tr><tr><td>GlobalWafers Co Ltd (6488.TWO)</td><td>E (05/19/2026)</td><td>NT$1,205.00</td></tr><tr><td>Gudeng Precision (3680.TWO)</td><td>O (11/25/2025)</td><td>NT$481.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$168.50</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$582.50</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$279.00</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb75.74</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$3,670.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb896.00</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$405.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb744.60</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb102.42</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,855.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb110.05</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$461.50</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.50</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,410.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$134.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$155.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$339.50</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$171.70</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb65.28</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb99.89</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb32.87</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb344.53</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$46.00</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb84.69</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$27.44</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb101.12</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb88.77</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb65.28</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb25.29</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb98.51</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$858.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,410.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$14,100.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$99.90</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$165.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb106.00</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb475.53</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$123.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$309.00</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb219.60</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$476.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$141.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$583.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$65.10</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$753.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb51.47</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$155.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$111.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$196.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb120.46</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb421.86</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$998.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$523.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$12.69</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,500.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,875.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$252.61</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$6,655.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS