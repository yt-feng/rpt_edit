你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：约 850 字，允许上下浮动 15%。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# Global AI Trend Tracker

Global Markets Research

27 May 2026

EQUITY: TECHNOLOGY

# Google's next-gen AI network for TPUv8t / v8i...

...And implications for the AI networking value chain

# TPU v8t & v8i's networking architecture may lead to stronger demand for OCS and benefit Google's TPU supply chain

Google (GOOG US, Not rated) released its eighth-generation tensor processing unit (TPU) at its Cloud Next 2026 in April, and the company for the first time distinguished its TPU products into training (TPU 8t) and inference (TPU vi). TPU 8t improves large-scale pre-training performance with SparseCore cores and Virgo network topology, while TPU 8i is designed for real-time reasoning and complex decision-making, with CAE (Collectives Acceleration Engine) and new Boardfly topology solving the latency bottleneck of long context reasoning to a certain extent. We think the purpose-built networks for TPUv8t and v8i reflect the AI market trend of decoupling network architecture for training and inference, in order to better unlock their performance in different scenarios, while reducing cost and power consumption at the same time. We think Boardfly network brings incremental demand for optical circuit switches (OCS0 at both the scale-up and the scale-out level). Meanwhile, as a technology leader in optical networks, we expect Google's stronger TPU shipments of would accelerate its adoption of all the mainstream optical communication solutions, including 1.6T pluggable transceivers, NPO (near-field packaged optics) and CPO (co-packaged optics). We think this is positive for Google's TPU supply chain, including substrate and PCB suppliers such as VGT (300476 CH/2476 HK, Buy), as well as optical communication solution providers.

# Google introduced Virgo Network and Boardfly topology for TPU 8t and 8i, respectively, aiming at lower latency and higher bandwidth

Regarding networking solutions, TPU 8t still uses 3D Torus topology (similar to TPU v7) to connect chips at the scale-up level to form a pod with up to 9,600 cards, and we think that there are still 48 OCS in each pod, but the number of ports may increase to $300^{*}300$ (from 288\*288). Google introduced Virgo Network, a flat two-layer non-blocking topology, for TPU V8t scale-out network. According to the company, this new network architecture enables up to 4x increased data center network (DCN) bandwidth and uses high-radix switches that reduce network layers by allowing more ports per switch. Moreover, Google has designed a new network topology, called Boardfly, for the TPU 8i cluster that can connect up to 1,152 of chips. The network connects 8 boards via copper cabling and further scales to 36 groups (up to 1,024 active chips) linked through OCS.

# Growth of CPU demand accelerates in agentic era

In addition, both eighth-generation TPU chips will be working with Google's self-developed ARM-based Axion CPU as the main controller. We think CPUs may become the key to running large AI clusters in the future, due to the exponential growth of inference workloads. According to comments from Intel's CEO during the company's 1Q26 earnings call, the CPU-to-GPU attach rate used to be 1:8, which has increased to 1:4 now, and may increase to 1:1 in the future. We think this reflects growing demand for CPUs in AI clusters for the agentic era.

# Research Analysts

# China Technology

# Bing Duan - NIHK

bing.duan1@NOM.com

+852 2252 2141

# Joel Ying, CFA - NIHK

joel.ying@NOM.com

+852 2252 2153

# Introduction to TPU V8i & V8t

On 22 April 2026, Google released its eighth-generation TPU at the Cloud Next 2026 conference, which is divided into the TPU 8t training chip and the TPU 8i inference chip. From the perspective of Google's chip development path, the current divergence between training and inference architecture requirements is widening, with training clusters focusing on optimizing computing power and inference clusters focusing on optimizing HBM bandwidth and memory capacity. The current mainstream large language models (LLM) are all MoE architectures, which require long context reasoning and the chain of thought scheme, and the importance of communication efficiency, memory access speed, and low-latency synchronization between chips far exceeds that of single-chip computing power. Therefore, Google designed the training chip and the inference chip separately and optimized their internal architectures to achieve high computing performance and low latency for the training chip, and high memory and low power consumption for the inference chip.

Fig. 1: Development path of Google TPU 

<table><tr><td></td><td>TPU</td><td>TPU chips per superpod</td><td>Topology</td><td>ICI bandwidth per TPU chip</td><td>ICI optical transceiver</td><td>Optical lane rate</td><td>OCS</td></tr><tr><td>2018</td><td>v2</td><td>256</td><td>2D Torus</td><td>800GB/s</td><td>None</td><td>NA</td><td>None</td></tr><tr><td>2020</td><td>v3</td><td>1024</td><td>2D Torus</td><td>800GB/s</td><td>400G AOC</td><td>50G</td><td>None</td></tr><tr><td>2022</td><td>v4</td><td>4096</td><td>3D Torus</td><td>600GB/s</td><td>400G OSFP</td><td>50G</td><td>OCS</td></tr><tr><td>2023</td><td>v5p</td><td>8960</td><td>3D Torus</td><td>1200GB/s</td><td>800G OSFP</td><td>100G</td><td>OCS</td></tr><tr><td>2025</td><td>v7</td><td>9216</td><td>3D Torus</td><td>1200GB/s</td><td>800G OSFP</td><td>200G</td><td>OCS</td></tr><tr><td>2026</td><td>V8t</td><td>9600</td><td>3D Torus</td><td>2400GB/s</td><td>NA</td><td>400G</td><td>OCS</td></tr><tr><td>2026</td><td>V8i</td><td>1152</td><td>Boardfly</td><td>2400GB/s</td><td>NA</td><td>400G</td><td>OCS</td></tr></table>

Source: Google, NOM

TPU 8t improves large-scale pre-training performance with SparseCore and Virgo network topology. TPU 8i is designed for real-time reasoning and complex decision-making, and its CAE acceleration engine and new Boardfly topology solve the latency bottleneck of long context reasoning to a certain extent, allowing AI to evolve from single-next-word prediction to scene simulation and deep logical reasoning, and AI responses will become more timely and coherent. Supported by the computing power of Google's self-developed ARM Axion architecture CPUs, Boardfly topology has achieved a double leap in energy efficiency.

The SparseCore is a specialized accelerator designed to handle the irregular memory access patterns of embedding lookups. The MoE LLM only activates a small number of parameters each time, and although the hybrid expert technology is highly energy efficient, it produces a large number of irregular memory accesses. SparseCore technology is specifically designed to handle this task, working with the Matrix Multiply Unit (MXU) to keep the chip running at high load. Moreover, TPU 8t minimizes exposed vector operation time by implementing more balanced Vector Processing Unit (VPU) scaling. In terms of computing, TPU 8t introduces native 4-bit floating point (FP4) to overcome memory bandwidth bottlenecks, doubling MXU throughput while maintaining accuracy for LLMs even at lower-precision quantization. In terms of memory, TPU 8t adopts de-intermediated TPU Direct technology, and HBM memory can directly talk to the Network Interface Card (NIC), bypassing the CPU and DRAM, resulting in 10x faster memory access speed than the previous generation TPU. Overall, TPU 8t solves several key bottlenecks in training tasks: efficiently processing sparse data, reducing data handling overhead between memory and compute units, and optimizing network communication between large-scale chip clusters. Google claims that compared with the previous generation, the "performance per dollar" of the 8T in training scenarios can be improved by up to 2.7x.

Fig. 2: TPU 8t ASIC block diagram   
![](images/22524d3bfe91baad58cbdf154b3f08709f9931bca0326dc5903ad01a8a8748db.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Host"] --> B["gBMC"]
    B --> C["PCIe Gen5 x16"]
    B --> D["PCIe Gen2 x1"]
    C --> E["Sparse core"]
    D --> F["Sparse core"]
    G["Chip manger"] --> H["HBM3E Ctrl"]
    G --> I["HBM3E Stack"]
    J["TensorCore"] --> K["VPU + Vmem"]
    K --> L["XLU"]
    K --> M["XLU"]
    K --> N["MXU"]
    K --> O["TCS"]
    O --> P["XLU"]
    O --> Q["MXU"]
    R["8-hi"] --> S["HBM3E stack"]
    R --> T["HBM3E Stack"]
    U["Memory and DMA interconnect"] --> V["HBM3E Ctrl"]
    U --> W["HBM3E Stack"]
    X["ICI"] --> Y["ICR Router"]
    X --> Z["3x Link Stack + MAX2 PHY"]
    X --> AA["3x Link Stack + MAX2 PHY"]
    AB["6x224G SerDes octals"] --> AC["Zebra package"]
    AD["Compute"] --> AE["Interconnect"]
    AF["Memory and DNA"] --> AG["Interconnect"]
    AH["Storage"] --> AI["Storage"]
    AJ["Logic chiplet"] --> AK["Logic chiplet"]
    AL["SerDes chiplet"] --> AM["SerDes chiplet"]
```
</details>

Source: Google, NOM

TPU 8i is a new chip designed for inference tasks, with the most notable feature being the tilt of resource allocation towards memory. Although its peak hash rate is lower than that of 8t, it is equipped with a 384MB on-chip SRAM cache (3x that of 8t), higher HBM memory capacity (288GB), and greater bandwidth. Google claimed that TPU 8i can host a larger KV Cache entirely on silicon, significantly reducing the idle time of the cores during long-context decoding. In addition, when an LLM performs inference, chips need to frequently synchronize data and summarize results, a process called collective communication. Chains-of-thought require multiple computing cores to frequently synchronize intermediate results, and traditional synchronization operations have extremely high latency. Therefore, TPU 8i uses the CAE, which aggregates results across cores with near-zero latency, specifically accelerating the reduction and synchronization steps required during auto-regressive decoding and chain-of-thought processing. For each TPU 8i chip, there are two Tensor Cores (TC) on-core dies and one CAE on the chiplet die, replacing four SparseCores (SCs) on core dies in the previous-generation Ironwood TPU. CAE further reduces the on-chip latency of collectives by 5x. Lower latency per collective operation means less time spent waiting, directly contributing to higher throughput required to run millions of agents concurrently.

Fig. 3: TPU 8i ASIC block diagram   
![](images/75e8ab3a037fae501ca14c3eacabd9a761a756d2a6a1670686a1594792f677ed.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Host"] --> B["gBMC"]
    B --> C["PCIe Gen5 x16"]
    B --> D["PCIe Gen2 x1"]
    C --> E["Chip manger"]
    D --> E
    E --> F["TensorCore"]
    F --> G["XLU"]
    F --> H["VPU + Vmem"]
    F --> I["MXU"]
    G --> J["TCS"]
    H --> K["XLU"]
    H --> L["MXU"]
    J --> M["TensorCore"]
    K --> N["TCS"]
    L --> O["XLU"]
    M --> P["Memory and DMA interconnect"]
    N --> Q["Memory and DMA interconnect"]
    O --> P
    P --> R["HBM3 Ctrl"]
    P --> S["HBM3 Ctrl"]
    P --> T["HBM3 Ctrl"]
    P --> U["HBM3 Ctrl"]
    P --> V["HBM3 Ctrl"]
    R --> W["HBM3E stack"]
    S --> X["HBM3E stack"]
    T --> Y["HBM3E stack"]
    U --> Z["HBM3E stack"]
    V --> AA["HBM3E stack"]
    W --> AB["8-hi"]
    X --> AB
    Y --> AB
    Z --> AB
    AB --> AC["HBM3E stack"]
    AB --> AD["HBM3E stack"]
    AB --> AE["HBM3E stack"]
    AB --> AF["HBM3E stack"]
    AC --> AG["HBM3E stack"]
    AD --> AH["HBM3E stack"]
    AE --> AI["HBM3E stack"]
    AF --> AJ["HBM3E stack"]
    AG --> AK["ICI Router"]
    AG --> AL["6x Link Stack"]
    AK --> AM["SC-CAE"]
    AL --> AM
    AM --> AN["6x200G SerDes octals + PCS"]
    AN --> AO["TN1 TC"]
    AN --> AP["TN2 TC"]
    AO --> AQ["Chiplet"]
    AP --> AQ
```
</details>

Source: Google, NOM

Fig. 4: Comparison of TPU v7, TPU v8t and TPU v8i 

<table><tr><td></td><td>TPU v7</td><td>TPU 8t</td><td>TPU 8i</td></tr><tr><td>Primary workload</td><td>High-performance ASIC for training and inference</td><td>Focus on large-scale training</td><td>Focus on large-scale inference</td></tr><tr><td>Design of die</td><td>Dual die</td><td>Single die</td><td>Dual die</td></tr><tr><td>HBM capacity</td><td>192GB HBM3E</td><td>216GB HBM</td><td>288GB HBM</td></tr><tr><td>HBM bandwidth</td><td>7.3TB/s</td><td>6.5TB/s</td><td>8.6TB/s</td></tr><tr><td>on-chip SRAM</td><td>-</td><td>128MB</td><td>384MB</td></tr><tr><td>Core feature</td><td>SparseCore, shared memory</td><td>SparseCore and LLM decoder engine, native FP4, Vrigo network</td><td>CAE, large SRAM, Boardfly network</td></tr><tr><td>Pod size</td><td>9216</td><td>9600</td><td>1152</td></tr><tr><td>Network topology</td><td>3D Torus</td><td>3D Torus</td><td>Boardfly</td></tr><tr><td>Peak FP4 PFLOPs</td><td>4.6</td><td>12.6</td><td>10.1</td></tr></table>

Source: Google, NOM

With the explosive growth of inference workloads, CPUs are the key to determining the efficiency and cost of AI systems. Data orchestration and memory management of inference tasks are highly dependent on the CPU, and the "logical scheduling" and "serial processing" used by AI Agents to perform complex tasks such as reading databases, running code, and parsing documents are the expertise of CPUs. According to comments from the Intel CEO during the company's 1Q26 earnings call, the CPU-to-GPU attach rate used to be 1:8, which has increased to 1:4 now, and may increase to 1:1 in the future. We think this reflects growing demand for CPU in AI clusters for agentic era.

Axion is Google's first custom ARM architecture-based CPU designed specifically for data centers, announced in 2024. For AI inference, Axion's dedicated optimizations can significantly boost performance, enabling AI workloads to run faster and more efficiently, according to management. The Axion product portfolio now includes three options: N4A, C4A, and C4A metal. Compared to virtual machines using mainstream x86 architecture CPUs, N4A offers twice the cost-performance ratio and leads in energy efficiency by up to 80% per watt, according to Google. In the TPU v8 series, Google is the first to use the Axion CPU as the main computing header, effectively reducing data preprocessing latency and ensuring the TPU computing engine runs at full capacity.

Fig. 5: AI inference performance on Axion CPU

# AI Inference Performance on Google Axion

Prompt Encoding & Tokens Generated /Sec

# Gemma-3-12b

Arm Neoverse based Google Axion

c4a-highmem with 48 vCPU

$$
+29 \%
$$

Better Performance over

AMD Turin

c4d-highmem-48 vCPU

$$
+23 \%
$$

Better Performance over

Intel Granite Rapids

c4-highmem-48 vCPU

Model Format: w8a8 | Benchmark: Throughput Serving | Serving Framework: vLLM | Concurrency: 1 and 16

(Compared to x86 based Instances)

Source: Google, NOM

# TPU V8i & V8t networking solutions

TPU 8t still uses 3D Torus topology to connect chips at the scale-up level to form a pod. The pod volume has increased to 9,600 cards (vs. 9216 cards for Ironwood), and the single-card scale-up bidirectional bandwidth is 19.2Tb (2x that of Ironwood), and we think that there are still 48 OCS in each pod, but the number of ports may increase to 300\*300. To support the massive data requirements of TPU 8t, Google introduced Virgo Network for scale-out networking. This new networking architecture enables up to 4x increased data center network (DCN) bandwidth on TPU 8t training over DCN. Built on high-radix switches that reduce network layers by allowing more ports per switch, Virgo Network employs a flat, two-layer non-blocking topology. Compared with traditional datacenter networks, this significantly reduces latency by minimizing network tiers. It features a multi-planar design with independent control domains to connect TPU 8t chips. The TPU 8t racks also connect with the Jupiter north-south fabric to access compute and memory services. Virgo Network can connect more than 1 million TPU chips into a single training cluster, with a single network architecture connecting 134,000 chips.

Fig. 6: Virgo Network architecture   
![](images/4890ee838e7f057546970b9aeaf2ad2537789258c143d358e6cd543c6f4265a1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph Virgo Network
        A["1"] --> B["2-layer switching"]
        B --> C["3"]
        D["2"] --> E["3"]
        F["3"] --> G["3"]
        H["3"] --> I["3"]
        J["3"] --> K["3"]
        L["3"] --> M["3"]
        N["3"] --> O["3"]
        P["3"] --> Q["3"]
        R["3"] --> S["3"]
        T["3"] --> U["3"]
        V["3"] --> W["3"]
        X["3"] --> Y["3"]
        Z["3"] --> AA["3"]
        AB["3"] --> AC["3"]
        AD["3"] --> AE["3"]
        AF["3"] --> AG["3"]
        AH["3"] --> AI["3"]
        AJ["3"] --> AK["3"]
        AL["3"] --> AM["3"]
        AN["3"] --> AO["3"]
        AP["3"] --> AQ["3"]
        AR["3"] --> AS["3"]
        AT["3"] --> AU["3"]
        AV["3"] --> AW["3"]
        AX["3"] --> AY["3"]
        AZ["3"] --> BA["3"]
        BB["3"] --> BC["3"]
        BD["3"] --> BE["3"]
        BF["3"] --> BG["3"]
        BH["3"] --> BI["3"]
        BJ["3"] --> BK["3"]
        BL["3"] --> BM["3"]
        BN["3"] --> BO["3"]
        BP["3"] --> BQ["3"]
        BR["3"] --> BS["3"]
        BT["3"] --> BU["3"]
        BV["3"] --> BW["3"]
       

[中间内容因长度限制已省略]

operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
