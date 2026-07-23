You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
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

Analog: Data center optical modules offer the clearest path toward scale and profitability. Customized analog products carry ASPs of approximately US\$2–3 per chip, with potential content of around US\$30 in a 1.6T NPO system. OmniVision is developing photodetectors, TIAs, SerDes and other optoelectronic-conversion products, supported by recently acquired communications expertise. Initial products have started ramping, with broader adopti

[中间内容因长度限制已省略]

iconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$168.50</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$582.50</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$279.00</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb75.74</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$3,670.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb896.00</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$405.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb744.60</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb102.42</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,855.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb110.05</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$461.50</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.50</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,410.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$134.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$155.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$339.50</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$171.70</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb65.28</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb99.89</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb32.87</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb344.53</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$46.00</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb84.69</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$27.44</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb101.12</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb88.77</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb65.28</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb25.29</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb98.51</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$858.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,410.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$14,100.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$99.90</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$165.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb106.00</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb475.53</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$123.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$309.00</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb219.60</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$476.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$141.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$583.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$65.10</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$753.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb51.47</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$155.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$111.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$196.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb120.46</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb421.86</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$998.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$523.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$12.69</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,500.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,875.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$252.61</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$6,655.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
