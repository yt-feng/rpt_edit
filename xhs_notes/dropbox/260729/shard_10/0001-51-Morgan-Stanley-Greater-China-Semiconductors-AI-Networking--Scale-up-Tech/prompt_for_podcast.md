你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
July 27, 2026 09:00 PM GMT

Greater China Semiconductors | Asia Pacific

# AI Networking: Scale-up Technology Enables China's AI Supernodes

Following our WAIC takeaways, we further examine China's emerging scale-up landscape, the role of optical interconnect, and implications for the domestic interconnect supply chain.

AI Supernodes enabled by scale-up are becoming the focus of China's AI computing landscape. Alongside our China WAIC takeaways, we provide an in-depth follow-up study of China's scale-up technology development. As we wrote in China's AI Accelerators – Who's Poised to Win?, Chinese AI GPUs are strong in optical networking and server rack design at the system level, although they remain constrained by wafer process technology at the chip level (Exhibit 6). These chip-level constraints are shifting competition in China's AI computing market from standalone chip specs to system solutions. WAIC 2026 featured fewer chip launches and more supernode solutions. Leading domestic accelerator vendors displayed rack-scale or multi-rack supernodes with scale-up domains of 64 accelerators or more, mostly enabled by proprietary scale-up technologies.

China's scale-up landscape is rapidly broadening, led by proprietary fabrics but spanning multiple system architectures (Exhibit 4). A year ago, our US semis team published Semiconductors: Scaling the AI Opportunity: A Scale-Up Network Primer (29 Aug 2025); China is now catching up quickly in scale-up technology. Huawei remains the domestic scale leader, with Atlas 950 using UnifiedBus 2.0 to connect 1,024 NPUs in the demonstrated configuration and designed to scale to 8,192 NPUs. Biren's next-gen BR2xx NPO architecture targets up to 1,024 GPUs through BLink 2.0. Sugon's scaleX640 connects 640 accelerators in a single rack. Moore Threads' (not covered) MTT C256 supports 128 GPUs in one rack and 256 across two racks through MT-Link 2.0, while MetaX, Alibaba and Enflame support 64- to 128-accelerator domains through MetaXLink-E, ICN, and GCU-LARE, respectively.

Stock implications: We believe Montage (OW, covered by Daniel Yen) is set to benefit from higher PCIe interconnect content in larger, distributed supernodes. As systems scale across racks, denser and longer PCIe links among CPUs, xPUs, switches, NICs and peripherals should support demand for PCIe retimers and PCIe switch chips. We also expect China AI GPU vendors, such as Hygon (OW, covered by Daisy Dai) (along with its ecosystem partner Sugon), Cambricon and Iluvatar (both OW, covered by Charlie Chan), to introduce or leverage scale-up technology to improve their AI server rack performance.

(Continued below.)

MS ASIA LIMITED+
Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

Charlie Chan
Equity Analyst
Charlie.Chan@morganstanley.com +886 2 2730-1725

Daniel Yen, CFA
Equity Analyst
Daniel.Yen@morganstanley.com +886 2 2730-2863

Daisy Dai, CFA
Equity Analyst
Daisy.Dai@morganstanley.com +852 2848-7310

Henry Zhao
Research Associate
Henry.Zhao@morganstanley.com +852 2239-7731

Tiffany Yeh
Equity Analyst
Tiffany.Yeh@morganstanley.com +886 2 7712-3032

Lucas Wang
Research Associate
Lucas.Wang@morganstanley.com +886 2 2730-2875

![](images/dd22589970793d1d7f100e4c057bd8610c35ea5e6f568c2d8eba607abae29d1d.jpg)  
GREATER CHINA TECHNOLOGY SEMICONDUCTORS
Asia Pacific
Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## China AI Interconnect - Scale-up

## Global AI server scale-up technology trend

## What is scale-up networking?

Scale-up networking refers to high-speed communication between GPUs/accelerators within the same server or rack. Interconnecting accelerators allow them to function as one large supercomputer, accessing the same memory and processing the same workload. This differs from scale-out networking, which connects multiple systems across a broader data center infrastructure.

Montage's PCIe 6.x/CXL3.x x16 AEC has completed interoperability testing, and targets supernode and inter-rack deployments. Chinese systems deploying more xPUs per unit of compute could further increase PCIe content. Beyond standardized PCIe connectivity, multi-rack scale-up should also accelerate demand for domestic optical interconnect.

Exhibit 1: Scale-up interface data rate per lane  
![](images/53c5673f2c51a5384612efc093a5fba10396a889b2c00b0af27535a2e9ee6bb3.jpg)  
Source: Company data, MS

Exhibit 2: Scale-up bandwidth per accelerator  
![](images/65eda2f56788940eeca47d09be96801327ce2a0133dd458790863fb5d99b22aa.jpg)  
Source: Company data, MS

Exhibit 3: US AI networking scale-up technologies

<table><tr><td>Technology</td><td>NVLink5</td><td>UALink 1.0</td><td>SUE</td><td>PCIe Gen 6</td><td>ICI</td><td>NeruonLink</td></tr><tr><td>Purpose</td><td>GPU-GPU; CPU-GPU</td><td>xPU-xPU</td><td>xPU-xPU</td><td>Primarily CPU-XPU;xPU-xPU</td><td>TPU interconnect</td><td>Trainiuminterconnect</td></tr><tr><td>Bandwidth</td><td>100 GB/s</td><td>100 GB/s</td><td>100 GB/s</td><td>64 GT/s</td><td>50-100 c B/S</td><td>not standardized</td></tr><tr><td>Latency</td><td>10-20 nm</td><td>&lt;100 nm</td><td>-</td><td>-</td><td>varies</td><td>varies</td></tr><tr><td>Ecosystem</td><td>NVIDIA (proprietary)</td><td>Open standard</td><td>Open standard</td><td>Open standard</td><td>Google (proprietary)</td><td>Amazon (proprietary)</td></tr><tr><td>Scalability</td><td>576 GPUs</td><td>1,024 xPUs</td><td>1,024 xPUs</td><td>varies</td><td>varies</td><td>64 Trainium</td></tr></table>

Source: Company data, MS

Exhibit 4: AI supernode scale-up solutions

<table><tr><td>Scale-up tech summary</td><td>NVIDIA</td><td>AMD</td><td>AsteraLabs</td><td>Huawei</td><td>Moore Threads</td><td>Sugon</td><td>MetaX</td><td>Alibaba</td><td>Enflame</td><td>Enflame</td><td>Biren</td><td>Biren</td></tr><tr><td>Supernode / accelerator name</td><td>GB300 NV/L72 (144 dies)</td><td>AMD Helios / Mi455X</td><td>N/A</td><td>Atlas 950 SuperPoD</td><td>MTT C256 / MTT S5000, PH100</td><td>scaleX640</td><td>Xijing S600 / C600</td><td>Panju AL128 / Zhenwu M890</td><td>Yunsui ESL64-O</td><td>NPO optical prototype</td><td>LightSphere 128 / Bili 166L</td><td>BR2xx NPO supernode (announced)</td></tr><tr><td>Scale-up solution</td><td>NVLink 5 + NVSwitch</td><td>UALink 1.0 / UALoE</td><td>Scorpio X-Series</td><td>UnifiedBus 2.0</td><td>MTLink 2.0</td><td>scaleX fabric</td><td>MetaXLink and MetaXLink-E</td><td>ALink system; MB90 implements ICN + ICN Switch 1.0</td><td>GCU-LARE</td><td>Undisclosed</td><td>Undisclosed</td><td>Blink 2.0</td></tr><tr><td>Technology foundation</td><td>Proprietary</td><td>Ethernet PHY-based, memory-semantic UALink fabric</td><td>PCIe Gen6</td><td>Proprietary</td><td>Proprietary</td><td>Open multi-vendor system architecture</td><td>Proprietary</td><td>Supports proprietary protocol and UALink</td><td>Proprietary</td><td>Undisclosed</td><td>SIPH OCS</td><td>Proprietary</td></tr><tr><td>Singal lane speed</td><td>Physical-lane rate N/A; 100GB/s per NVLink S link</td><td>200Gb/s per lane; 212.5GT/s raw signaling rate</td><td>Undisclosed</td><td>106.25Gb/s PAM4 under UB2.0 specification</td><td>112Gb/s per lane</td><td>Undisclosed</td><td>Undisclosed</td><td>112G/224G SerDes supported at AL128 platform level</td><td>Undisclosed</td><td>Undisclosed</td><td>Undisclosed</td><td>Undisclosed</td></tr><tr><td>Total bandwidth per accelerator</td><td>1.8TB/s</td><td>3.6TB/s</td><td>Undisclosed</td><td>2TB/s</td><td>800GB/s</td><td>Undisclosed</td><td>Undisclosed</td><td>800GB/s</td><td>Undisclosed</td><td>Undisclosed</td><td>Undisclosed</td><td>Undisclosed</td></tr><tr><td>Total accelerator units in supernode</td><td>72</td><td>72</td><td>Up to 80 per switch (merchant solution)</td><td>1,024 NPUs demonstrated / 8,192 NPUs announced</td><td>128 GPUs in one rack; 256 GPUs across two racks</td><td>640</td><td>64 GPUs in S600 rack; 128 GPUs through C600 MetaXLink-E</td><td>128 per rack; 64 per disclosed full-bandwidth ICN domain</td><td>64</td><td>512-plus</td><td>128</td><td>1,024</td></tr><tr><td>Physical interface</td><td>Passive copper; NVLink cable-cartridge / backplane</td><td>Electrical/copper</td><td>Electrical/copper</td><td>Hybrid: orthogonal cableless electrical interconnect intra-rack; optical interconnect inter-rack</td><td>All-copper Cable Tray</td><td>Electrical/copper</td><td>Cabless OEX electrical interconnect</td><td>Backplane-free orthogonal electrical; NPC interconnect</td><td>Cabless OEX electrical interconnect</td><td>NPO optics</td><td>SIPH optical circuit switching supplied by Lightelligence</td><td>NPO optics</td></tr><tr><td>Copper cable</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No (cableless)</td><td>Yes</td><td>Undisclosed</td><td>No (cableless)</td><td>Yes</td><td>No (cableless)</td><td>No</td><td>No</td><td>No</td></tr><tr><td>CPO</td><td>No for scale-up (Yes for scale-out)</td><td>No</td><td>No</td><td>Undisclosed</td><td>No</td><td>Undisclosed</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>NPO</td><td>No</td><td>No</td><td>No</td><td>Undisclosed</td><td>No</td><td>Undisclosed</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr></table>

Source: Company data, MS

Exhibit 5: Scale-up vs. scale-out networking  
![](images/a48bdaf32e9e9bf0d81f0283355024b34eb782fd9f4e7464001fffd2b3e38bb1.jpg)  
Source: Broadcom 2025 OCP Summit Keynote, MS

## China AI server scale-up development

In China, electrical interconnect remains the preferred option within racks, while optical becomes more important as scale-up domains extend across racks. Short electrical links offer lower cost and simpler integration within boards, trays and single-rack systems. Moore Threads' C256 uses an all-copper cable tray design, while the orthogonal zero-cable architectures by Enflame and MetaX also remain electrical. Optical interconnection becomes more attractive across racks, where copper reach, signal loss and power consumption become constraints. Huawei's Atlas 950 SuperPoD extends UnifiedBus across racks within the same SuperPoD using optical interconnect.

The transition toward optical connectivity may create demand for domestic switching and optical engine solutions designed for AI systems. At WAIC 2026, Lightelligence (not covered) showcased its new NPO/CPO switch solutions (Exhibit 8, Exhibit 9), which pair the switch ASIC from a leading domestic vendor, which we believe is Centec Communications (not covered), with Lightelligence's optical engine, including the SiPh PIC and selected EICs such as the TIA. The NPO/CPO solutions shorten the high-speed

electrical path between the switch ASIC and optical engine, improving bandwidth density and power efficiency, while NPO retains greater serviceability than CPO. The same architecture can serve both scale-up and scale-out networks, with scale-up becoming increasingly relevant as tightly coupled accelerator domains extend across racks.

More broadly, scale-up is emerging as the principal area of architectural differentiation, while scale-out remains the backbone of large-scale clusters. System solutions generally use a specialized fabric to connect accelerators within a supernode, and Ethernet-based fabrics such as RoCE or UBoE, or Infiniband to connect multiple supernodes across a cluster. NVIDIA combines NVLink with InfiniBand or Spectrum-X Ethernet; AMD Helios pairs UALink with Ethernet scale-out; Huawei uses UnifiedBus within the SuperPoD, and UBoE or RoCE for scale-out between SuperPoDs.

Exhibit 6: Relative strengths of AI industries in the US and China - optical networking almost on par

![](images/6b051c1561686f0dcc6af41dd3b249b5ab5aafe2157af5af5d4d5345114f512e.jpg)  
Source: MS

Exhibit 7: Domestic chips have lower TCO and comparable per token cost (AI LLM inference) vs. NVIDIA's processors for China  
![](images/055192b3fbc91c6f6558fca2662cc7bca4736e377cb4842b830118763a1c101c.jpg)  
Source: Company data, MS estimates

## Optical interconnect is progressing towards scale-up system deployment

Enflame and Lightelligence previously demonstrated an xPU-CPO prototype that places the optical engine beside the accelerator, enabling direct optical output from the xPU and reducing the electrical distance between the compute silicon and optics. At WAIC 2026, Enflame displayed an NPO-equipped GPU-server solution targeting scale-up domains of 512 accelerators or more, developed in partnership with Lightelligence (Exhibit 10). Biren also unveiled a next-gen BR2xx-based NPO architecture designed to support a scale-up domain of up to 1,024 GPUs (Exhibit 11). Also, LightSphere X (jointly developed by Lightelligence, Biren, ZTE, and other partners) incorporates Lightelligence's SiPh interconnect and dOCS technology, enabling the accelerator domain to extend across racks and allowing the topology to be reconfigured according to workload requirements (Exhibit 12). These projects show domestic optical technology being integrated at both the accelerator optical-I/O layer and the distributed optical-switching layer, to support larger, multi-rack scale-up domains.

Exhibit 8: 51.2T CPO switch module (displayed by Lightelligence)  
![](images/893e1eadb3dc5711c3315ec7cc85944e120ba999c4d0cfcd5bb2f00c0dcab807.jpg)  
Source: Company data, MS

Exhibit 9: NPO switch module (displayed by Lightelligence)  
![](images/dd13d7678a84c10d67c9dd473492ce05895cfd1f92a601835cc54c350e2debd1.jpg)  
Source: Company data, MS

Exhibit 10: Enflame's NPO optical interconnect solution for scale-up  
![](images/2e4894ea581cb180a16bee44c72488d53ae7dfd13d0b77f4cf50a89b4b0fe0c3.jpg)  
Exhibit 12: LightSphere X (Lightelligence)  
Source: Company data

![](images/b8eb588117dc1a35e7eaf27b7e71f25ab7c209dd8bbda67f8b2981703fad3662.jpg)  
Source: Company data  
Source: Company data, MS

Exhibit 11: Biren's NPO optical interconnect solution for scale-up  
![](images/0578d99a8f86eabf333301c069373beca58abe2059023e7b125772a68c3c3b92.jpg)

## US scale-up networking ecosystem and TAM forecast

Exhibit 13: Chinese CSPs' capex will be a key demand driver for Chinese AI GPUs  
![](images/01ded04d819bafc5491d8b6efb7d17c4e2539979914d14d97088c6aa1c9a9ce8.jpg)  
Source: Company data, MS

Exhibit 14: US semi : Scale-up TAM estimate (\$mn)  
![](images/ed3fa6ffbd11bfbc31996ec3b93b551abfc53dc9039335e2911e58bdb149ed8a.jpg)  
Source: Company data, MS (E) estimates

This report references U.S. Executive Order 14032 and/or entities or securities that are designated thereunder. U.S. persons may be prohibited from buying certain securities of entities named in this report. Readers are solely responsible for ensuring that their investment activities are carried out in compliance with applicable laws.

This report references export controls and/or entities that may be subject to export control restrictions. Readers are solely responsible for ensuring that their investment or trade activities are carried out in compliance with applicable laws.

This report references U.S. Executive Order 14105 and/or entities that may be in scope of such order. U.S. persons may be prohibited from engaging in certain transactions or otherwise require certain other transactions be notified to the U.S. Department of Treasury. Readers are solely responsible for ensuring that their investment or trade activities are carried out in compliance with applicable laws.

## Valuation Methodology and Risks

## Montage Technology Co Ltd (6809.HK)

Base case, residual income model. Key assumptions:

■ 8.4% CoE (1.2 beta, 3.0% risk-free rate, and 4.5% risk premium)

■ 30% payout ratio

■ 19.3% medium-term growth rate

■ 4% terminal growth rate

These assumptions reflect cloud capex growth, DRAM interface technology migration, and Montage's strong position in China's datacenter semi localization. We then apply an exchange rate of 1.15 HKD:1 RMB, assuming no H-share discount vs the A-share.

## Risks to Upside

■ Faster-than-expected phase-out of US peers

■ Faster-than-expected spec migration

## Risks to Downside

■ Weaker-than-expected cloud demand

■ Slower-than-expected DRAM interface technology migration

■ Delay in new product launches

## Montage Technology Co Ltd (688008.SS)

Base case, residual income model. Key assumptions:

■ 8.4% CoE (1.2 beta, 3.0% risk-free rate, and 4.5% risk premium)

■ 30% payout ratio

■ 19.3% medium-term growth rate

■ 4% terminal growth rate

We believe these assumptions are justified, given the cloud capex growth, DRAM interface technology migration, and Montage's strong position in China's datacenter semi localization.

## Risks to Upside

■ Faster-than-expected phase-out of US peers

■ Faster-than-expected spec migration

## Risks to Downside

■ Weaker-than-expected cloud demand

■ Slower-than-expected DRAM interface technology migration

■ Delay in new product launches

## Hygon Information Technology Co., Ltd. (688041.SS)

We assume an 8.0% cost of equity (beta 1.05, risk-free rate 2.0% and risk premium 5.8%), a payout ratio of 50%, a medium-term growth rate of 25.0%, and a terminal growth rate of 5.0%, all of which are in line with other China AI chip companies under our coverage.

## Risks to Upside

■ Hygon further differentiates itself from local CPU and GPU competitors and gains significant market share in China's CPU and GPU markets

■ China AI demand is stronger than expected

■ Faster ramp-up of leading node capacity

## Risks to Downside

■ Intensified pricing competition among local GPU companies

■ China AI demand is weaker than expected

■ Slower yield improvement and capacity buildout at local leading node foundries

## Cambricon Technology Corporation (688256.SS)

Key valuation assumptions underpinning our model include: an 8.4% cost of equity (derived from a 

[中间内容因长度限制已省略]

ductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$148.60</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$597.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$276.00</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb72.90</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$3,680.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb830.20</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$436.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb770.00</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb95.31</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,820.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb98.89</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$449.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$70.65</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,350.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$126.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$157.00</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$355.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$161.60</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb60.74</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb92.22</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb32.33</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb313.59</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$44.12</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb82.35</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$24.88</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb100.00</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb84.88</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb66.00</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb24.77</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb93.22</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$773.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,385.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$14,695.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$98.70</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$166.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb104.23</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb434.03</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$125.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$322.00</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb227.45</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$518.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$132.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$615.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$61.90</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$762.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb50.31</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$160.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$116.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$203.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb115.15</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb373.90</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,035.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$598.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$12.62</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,110.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,720.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$270.90</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$6,395.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
