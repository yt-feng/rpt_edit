# Semiconductor Back-end Process and Package Trends

We held a seminar on the topic with Professor Fumihiro Inoue from Yokohama National University. He is a leading Japanese researcher in the field of advanced packages. AI application has significantly expanded the market for advanced packages. Professor Inoue believes that optimization of the overall system will be important for package technology as well. Below we summarize the content of his presentation.

Fumihiro Inoue:

• Professor, Yokohama National University

\- Semiconductor and Quantum Integrated Electronics Research Center, Deputy Center Head and Professor

• Cross-Appointment Professor, Hokkaido University

• LSTC, 3D Packages Deputy Division Head

• 2011-21 imec Researcher

\- Main research areas: Semiconductor back-end process, chiplets, 3D integration, process development

AI system configuration: In contrast to traditional CPU-centric configurations in PCs, smartphones, and other devices, AI systems utilize a configuration with memory (DRAM, SSD, and HBM) that conduct high-speed data interaction with CPU and GPU devices. CPU importance is growing again amid future expansion of the edge AI market, in addition to cloud AI. Chiplets, which integrate multiple chips, are essential systems for the realization of AI systems due to the increasing difficulty of delivering cost and power consumption improvements for monolithic devices via finer processes. Chiplets connect individual devices manufactured at high productivity using optimal technology nodes and facilitate advantages in power consumption and costs and optimal interconnection designs. Back-end processes are not just simple assembly steps and actually generate added value. While GPU computation performance has been steadily rising each year, data movements between GPUs, GPU and memory (HBM), and racks have become bottlenecks. It is necessary to review the AI system concept to resolve these issues. AI will be experiencing transformation from a "computation device" to a "communication system."

Dominance structure in cloud AI: NVIDIA builds a software ecosystem based on CUDA. It provides "platforms" rather than just standalone GPUs. TSMC has an overwhelming position in supply capacity for advanced processes and advanced packages and influences the possibility of shipping AI GPUs. Participants and clients have confidence in the combination of NVIDIA (design) and TSMC (production, mounting). The next hurdles are interconnections and power. Co-packaged optics (CPO) technology offers a "solution" to the limits of copper interconnections. NVIDIA and TSMC are leaders in co-packaged optics as well. (continued next page)

TSMC's COUPE connects EIC (electronic integrated circuits) and PIC (photonic integrated circuits) using TSMC-SolC bonding technology. It supports high-precision connections between chips. Results announced at the ECTC event in 2025 were low impedance in the chip-chip interface, bond density of at least 16 times, and 85% reduction of stray capacity. This format raises speed by 170% or more at the same power consumption and can reduce power usage by 40%. SolC narrow-pitch bonding improves power integrity and signal integrity and is suitable for high-speed data communications. COUPE utilizes a shared 3D multilayer structure as the substrate and supports grating coupler (GC) and edge coupler (EC) types. It exhibits structural flexibility. For optical design, the GC type curtails optical loss with an embedded microlens at the optical-path end, rear-side metal reflection panel under the GC, and optimized anti-reflection coating (ARC) surface. Process optimization has reduced insertion loss from the COUPE additional optical path to effectively zero dB.

The real significance of co-packaged optics (CPO) is not "replacement of copper interconnections with light." Reduced power for SerDes (conversion from parallel communication to serial communication (Ser) and restoration (Des)), I/O, and re-timer (repair and regeneration of digital signals degraded and distorted on the transmission path) components that account for the bulk of power usage is a major issue. Co-packaged optics changes the I/O position and role. The key point is "the extent to which it is possible to lower power usage for connecting to the outside" rather than "how quickly it is possible to carry out calculations."

There is interest in technologies from Broadcom, Marvell, and Ayar Labs for the future "I/O-driven era."

Japanese companies possess global top-level materials and parts but are lagging in systems and mounting. They have core technologies. However, their package design and volume-production mounting capabilities premised on co-packaged optics are weak. There is also an absence of simultaneous optimized design of light, electricity, and heat, and the concept of "how to integrate and sell" is lacking. Japanese companies have approached co-packaged optics as a future technology and research theme and thereby divorced design, mounting, and business perspectives from the research initial stage. Globally, meanwhile, co-packaged optics is on the cusp of volume production, and the industry is advancing in "architecture x package" building.

## Cloud AI isn't everything

Chiplets are progressing. On the business front, key issues are (1) advances in standardization but limited genuine compatibility, (2) under-developed analysis for EDA and PPA, (3) lack of clarity regarding responsibility roles and yield risk when defects occur, (4) pursuit of vertically integrated models by TSMC, Intel, and Samsung and lack of an open model leader, and (5) many cases of activity stopping at the prototype level because of inability to overcome test, supply, and cost issues after functional verification (volume production wall). The industry has moved into an era in which technology advantages are not enough to win. Trustworthy rules, frameworks, and partnerships will determine whether businesses succeed or not.

Cloud AI is currently the centerpiece of AI systems. However, it is not a perfect solution from power, latency, communication cost, and geopolitical and infrastructure control perspectives. It is not possible to handle everything in the cloud. In particular, edge AI is necessary in industrial, automotive-based, robot, and infrastructure monitoring areas. Role division is cloud AI for learning and consolidation and edge AI for inference and immediate decisions. The AI semiconductor market was worth US$236bn in 2025 (including cloud AI at roughly US$160bn and edge AI at about US$80bn). According to the VLSI forecast, this should expand to US$371bn in 2028 with cloud AI at US$250bn and edge AI at US$120bn.

Edge AI is not a substitute for cloud AI. It is a core technology that has necessarily emerged from the limits of cloud AI. Cloud AI faces limitations in terms of infrastructure (power and environmental constraints accompanying explosive increase in computation volume), society and systems (information security and data sovereignty), and value and UX (personalization and realtime features, ultralow latency, and constant inference requests). These aspects are powerful drivers of edge AI.

HBM is a "technology that speeds up AI." In contrast, edge AI is a "technology that distributes AI in massive amounts." HBM is not suited for the edge from the perspective of power consumption, package costs, and volume scale. The main presence in edge AI is likely to be DDR x 3D layering.

Qualcomm announced a roadmap for data centers in the Agentic AI era. The structure of connecting HBM and compute via an interposer consumes power through data passage over a physical "bridge." With wider bandwidth, the additional portion consumes more energy. HBC Gen1 advocated by Qualcomm (used in Qualcomm's AI250 AI-inference chip for data centers), meanwhile, places a multilayer structure on a 2D organic substrate (it does not use TSMC's CoWoS). It realizes 133TB/s effective memory bandwidth per card without using memory devices that support the bandwidth available from HBM. The value is 18 times more than the AI200's LPDDR5.

## Areas and materials disrupted by technology innovation

Advanced packages that include HBM (such as CoWoS) currently mainly rely on a silicon interposer. Finer processing for substrate RDL and glass-core substrate mounting technology, meanwhile, are rapidly advancing. Silicon interposers face structural redundancy, scalability, and cost risks. Another risk is relative dilution of interposer value by the technology advancement pace on the substrate side. If the substrate side becomes capable of supporting the same interconnection density as the passive interconnection layer, this might undermine the assumption that the interposer is an essential part (redefining the function division).

When the organic RDL interposer is integrated into a glass-core substrate, this might reduce the usage frequency and market scale of carrier glass, temporary adhesives, and TMV (through mold via) and mega-pillar formation thick-coat resist and plating solutions (anticipated occurrence from 2030 as a timeline).

To address these technology innovations, materials manufacturers need to strengthen proposal capabilities from "selling standalone materials" to "offering process + evaluation + design." Since this response requires more than just domestic capabilities, it is essential to build back-end process co-creation sites abroad (particularly in the US).

Resonac launched the US-JOINT consortium of 10 Japanese and US companies in Silicon Valley and has defined a framework to move forward with back-end process technologies in the US.

There will also be a shift from wafers to panels and large surface areas. Since prototype approaches change with organic interposers and substrate scale, materials manufacturers are striving to attract participant companies under a "shared prototype line" banner. Resonac has launched the JOINT3 consortium that has 27 companies with the aim of building a panel-level (515 x 510mm) organic interposer prototype line.

## New era that enables CMOS2.0 and hybrid bonding

Huawei has proposed Tau Scaling Law at ISCAS2026. This is a new scaling strategy beyond Moore's Law.

Process migration confronts physical limits and increased costs. For certain regions, it is necessary to have a new strategy for improving performance amid access restrictions to EUV lithography equipment. Huawei proposes a new indicator of shrinking the signal transmission time (Tai) rather than focusing on the number of transistors. More Moore makes smaller transistors. In contrast, Huawei's Beyond Moore is a CMOS2.0-type concept. It aims to comprehensively optimize devices, circuits, chips, and systems and thereby reduce overall system delay.

The current semiconductor industry structure consists of leading companies in design, production, EDA, equipment, and mounting and test areas, such as NVIDIA and TSMC. This makes it difficult to achieve simultaneous optimization of design, process, mounting, and systems required by CMOS2.0. Certain regions, meanwhile, can develop design, production, mounting, and AI systems in a vertically integrated manner led by relevant organizations. It can optimize performance for the overall eco-system rather than achieving the top level worldwide for individual technologies. Huawei's announcement shows that certain regions have started to genuinely seek verification of this direction.

Hybrid bonding is not "next-generation bonding after bumps." Current micro-bumps (up to 40 microns) have an I/O boundary between chips, and design fundamentally takes place at the chip unit. Interconnections temporarily stop at the chip boundary. In hybrid bonding (100nm-level), however, BEOL links chips (interconnections extend beyond the boundary), and this supports design division at the interconnection layer unit and removes the boundary between chips. Hybrid bonding is not just a bonding technology. It is a technology that redefines system setup across the BEOL (bringing it outside).

## Current situation in Japan

Chiplets deliver Scale-up (higher integration = front-end process merger) x Scale-out (planar rollout = large substrates, co-packaged optics). The Scale-up portion is more important than Scale-out for functions and composition required by edge AI. Japan's current back-end process R&D activity, meanwhile, is overly skewed toward Scale-out. Panel/PLP is an excessive boom and cannot handle the edge AI trend.

For NAND, a Japanese company advocates MAS-CBA, an approach that separately manufactures NAND CMOS circuit and memory cell wafers and directly bonds them with CU. This technology significantly raises I/O speed, reduces electrical resistance, boosts writing speed, and achieves low latency and power consumption. This is a competitive technology.

Key technologies for next-generation packaging are hybrid bonding and fine-pitch substrates (glass core, bridge (EMIB-T), and advanced RDL on substrate). System mounting that does not rely on an interposer will be important (creating post-CoWoS).
