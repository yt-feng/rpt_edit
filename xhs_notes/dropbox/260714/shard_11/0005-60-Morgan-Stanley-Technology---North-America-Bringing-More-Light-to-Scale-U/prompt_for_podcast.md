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
Sou

[中间内容因长度限制已省略]

ectations.

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
"""
