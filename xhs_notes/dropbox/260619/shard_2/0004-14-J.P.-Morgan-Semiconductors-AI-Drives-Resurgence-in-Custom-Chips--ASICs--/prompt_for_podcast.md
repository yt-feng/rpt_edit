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
![](images/192fc9cb5eb29430afa4a96d2f3de235bf109a247a4dbcd1c65351538c92b95c.jpg)

<details>
<summary>text_image</summary>

JPM
</details>

# Semiconductors

# AI Drives Resurgence in Custom Chips (ASICs) - ASIC Market Overview/Update

Harlan Sur AC

415-315-6700

harlan.sur@JPM.com

JPM Securities LLC

Mayur Ramdhani

212-622-1664

mayur.ramdhani@JPM.com

JPM Securities LLC

See the end pages of this presentation for analyst certification and important disclosures.

## ASIC – Application Specific Integrated Circuit:

\- A chip that is designed for a specific CUSTOMER for a specific application or platform:

• Example: Apple iPhone A19 processor chip (Apple does complete design)  
• Example: Nokia Reef Shark BTS processor chip (Nokia, Marvell, Broadcom)  
• Example: Google TPU AI processor (Google, Broadcom)  
• Example: Amazon Trainium 3 AI processor (AWS, Marvell, Alchip)

## ASSP - Application Specific Standard Product (sometimes called “merchant”)

• A chip that is designed for multiple customers for a specific application:

• Example: Qualcomm snap-dragon mobile processor family  
• Example: NVIDIA AI GPU, AMD AI GPU

## GP - General Purpose products – multiple customers/multiple applications

• A chip that is designed for multiple customers for multiple applications

• Example: Intel/AMD PC or server CPU  
• Example: Infineon, STMicro, Onsemi – power semiconductors/Microcontrollers  
• Example: Samsung, Hynix, Micron – memory/storage

![](images/60db2429403424455be923caba00e209cbd9fe43e0be0b71f5259bb8f992330d.jpg)

<details>
<summary>sankey diagram</summary>

| Category | Sub-category | Amount |
| -------- | ----------- | ------ |
| Total Semi Industry Revenues CY25 | $805B | $805B |
| Application Specific | $351B | $351B |
| General Purpose | $454B | $454B |
| Application Specific Standard Products (ASSPs) | $282B | $282B |
| Application Specific Integrated Circuits (ASICs) | $68B | $68B |
| Memory | - | - |
| Microprocessor | - | - |
| Analog | - | - |
| Power | - | - |
| AI GPUs (NVDA, AMD) | - | - |
| Qualcomm Snapdragon | - | - |
| In vehicle SDV Processor | - | - |
| Networking switch IC | - | - |
| Optical DSP IC | - | - |
| Google TPU AI Processor | - | - |
| Nokia Reef Shark 5G RAN | - | - |
| Amazon Trainium XPU | - | - |
| Apple A19 iPhone CPU | - | - |
| Apple iPhone wireless charging | - | - |
| Microsoft Maia AI processor | - | - |
</details>

## Value proposition of doing your own custom chip or ASIC:

- Customer OWNS the software stack  
- If you own the software stack, can custom tune the silicon to the specific software stack and driver better system level performance (compute performance/power)  
- The economics (high volume applications and /or high ASP infrastructure platforms lend themselves well to ASICs) – need to drive ROI/Justification of customer silicon chip design team:  
- Apple is the poster child for custom ASICs – they create/own the entire software stack/applications layer, they own the entire system design, they can differentiate on platform performance/low power and they ship 250M units per year (strong ROI on internal chip design R&D) – leverage investments into PC CPUs, watch CPUs, etc...  
- Game consoles (Sony/Microsoft) – same value prop as Apple – relative high volumes  
- Base station RAN processor ASICs – small volumes, but VERY HIGH ASPs, leverage across entire network/subscriber base drives ROI  
- Google TPU AI processor, Amazon Trainium AI processor, Meta MTIA processor, Microsoft Maia AI processor – low volumes, but VERY VERY HIGH ASPs – token generation/AI monetization will drive strong ROI

## Example: AI GPU Versus AI Custom ASIC Processor

AI ASICs/XPUs Offer Competitive Performance, Economics and Power Efficiency

<table><tr><td></td><td>NVIDIA B200 Blackwell</td><td>NVIDIA B300 Blackwell Ultra</td><td>Google/ Broadcom TPU7x Ironwood</td></tr><tr><td>Compute performance (FP8 TFLOPS)</td><td>4500</td><td>5000</td><td>4614</td></tr><tr><td>Memory capacity per chip (HBM3E)</td><td>192</td><td>288</td><td>192</td></tr><tr><td>HBM bandwidth per chip (TBps)</td><td>7.7</td><td>8.0</td><td>7.4</td></tr><tr><td>TDP (Watts)</td><td>1000</td><td>1200</td><td>1000</td></tr><tr><td>ASP</td><td>$35,000</td><td>$40,000</td><td>$13,000</td></tr><tr><td>TFLOPS per $</td><td>0.13</td><td>0.13</td><td>0.35</td></tr><tr><td>TFLOPS per Wattt</td><td>4.50</td><td>4.17</td><td>4.61</td></tr></table>

<table><tr><td>Compute Platform Partner</td><td>Scenario</td><td>DC Capex per GW</td><td>Compute Partner Revenue per GW</td><td>Compute Capex</td><td>Networking Capex</td></tr><tr><td rowspan="2">NVIDIA</td><td>Low case</td><td>$45</td><td>$20</td><td>$16</td><td>$4</td></tr><tr><td>High case</td><td>$55</td><td>$30</td><td>$24</td><td>$6</td></tr><tr><td rowspan="2">AMD</td><td>Low case</td><td>$35</td><td>$15</td><td>$14</td><td>$2</td></tr><tr><td>High case</td><td>$40</td><td>$20</td><td>$18</td><td>$2</td></tr><tr><td rowspan="2">Broadcom</td><td>Low case</td><td>$30</td><td>$10</td><td>$7</td><td>$3</td></tr><tr><td>High case</td><td>$40</td><td>$15</td><td>$11</td><td>$5</td></tr></table>

Source: Company reports, JPM

## Chip and Rack Architectures – TPU7x Ironwood ASIC vs. Nvidia Blackwell GPU

Chip Architecture  
![](images/2d1efea17d4f65cce4ce3bca1aa2385da1dea85518034a16406744c10bde51e7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Host"] --> B["TPU7x Ironwood"]
  C["gBMC"] --> D["PCIe Gen5 x16"]
  C --> E["PCIe Gen2 x1"]
  D --> F["Memory and DMA Interconnect"]
  E --> F
  F --> G["Chip Manager"]
  F --> H["HBM3 Ctrl"]
  F --> I["HBM3 Ctrl"]
  F --> J["HBM3 Ctrl"]
  F --> K["HBM3 Ctrl"]
  F --> L["Sparse Core"]
  F --> M["Sparse Core"]
  F --> N["HBM3 Stack"]
  F --> O["HBM3 Stack"]
  F --> P["HBM3 Stack"]
  F --> Q["HBM3 Stack"]
  F --> R["HBM3 Stack"]
  F --> S["HBM3 Stack"]
  F --> T["8-hi"]
    
  U["TensorCore"] --> V["VPU + Vmem"]
  V --> W["XLU"]
  V --> X["XLU"]
  V --> Y["MXU"]
  V --> Z["TCS"]
  Z --> AA["XLU"]
  Z --> AB["XLU"]
    
  AC["TensorCore"] --> AD["VPU + Vmem"]
  AD --> AE["XLU"]
  AD --> AF["MXU"]
  AD --> AG["TCS"]
  AG --> AH["XLU"]
  AG --> AI["MXU"]
    
  J --> AJ["Memory and DMA Interconnect"]
  AJ --> AK["Sparse Core"]
  AJ --> AL["Sparse Core"]
  AJ --> AM["HBM3 Ctrl"]
  AJ --> AN["HBM3 Ctrl"]
  AJ --> AO["HBM3 Ctrl"]
  AJ --> AP["HBM3 Ctrl"]
    
  AJ --> AQ["8-hi"]
    
  AR["ICR Router"] --> AS["6× Link stack"]
  AR --> AT["6×112G SerDes octals + PCS"]
    
  AU["CPU Host"] --> AV["Data Center Networking (DCN) Uplinks"]
  AV --> AW["Power In"]
    
  AX["Copper Intra-rack ICI Interconnects"] --> AY["Optical inter-rack ICI (Interchip Interconnect)"]
  AY --> AZ["Heat Out (Air & Liquid)"]
    
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#fcc,stroke:#333
    style F fill:#cff,stroke:#333
    style AG fill:#fcc,stroke:#333
    style AH fill:#fcc,stroke:#333
    style AI fill:#fcc,stroke:#333
    style AJ fill:#fcc,stroke:#333
    style AK fill:#fcc,stroke:#333
    style AL fill:#fcc,stroke:#333
    style AM fill:#fcc,stroke:#333
    style AN fill:#fcc,stroke:#333
    style AO fill:#fcc,stroke:#333
    style AP fill:#fcc,stroke:#333
    style AQ fill:#fcc,stroke:#333
    style AR fill:#fcc,stroke:#333
```
</details>

Rack Architecture

![](images/d400064e39afd134176fba32b4e99fe657d62ed3312f0f291cb01f2bc559a079.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Nvidia Blackwell"] --> B["NVSwitch"]
  B --> C["SHARP In Network Compute"]
  C --> D["NVLink 5 1,800 GB/s"]
  D --> E["NVLink-C2C Up to 900GB/s Coherent CPU-GPU Interface"]
  E --> F["Grace CPU"]
  F --> G["JPM"]
    
    subgraph NVP
        H["Compute Density 4x more TFLOPs/mm² vs Hopper"]
        I["NVFP4 Tensor cores 15 PetaFLOPS Dense NVFP4"]
        J["288GB HBM3E Memory (8 Stacks, Up to 8 TB/s)"]
    end
    
    subgraph NVP_CPU
        K["GPC"]
        L["GPC"]
        M["GPC"]
        N["GPC"]
        O["GPC"]
        P["GPC"]
        Q["GPC"]
        R["GPC"]
        S["GPC"]
        T["GPC"]
        U["GPC"]
        V["GPC"]
        W["GPC"]
        X["GPC"]
        Y["GPC"]
        Z["GPC"]
        AA["GPC"]
        AB["GPC"]
    end
    
    subgraph JPM
        AC["Power shelves"]
        AD["8x Dual GH200 Compute Trays"]
        AE["9x NVLink Switch Trays"]
        AF["8x Dual GH200 Compute Trays"]
        AG["Power shelves"]
    end
```
</details>

<table><tr><td>AI accelerators units (MM)</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>NVIDIA GPUs</td><td>1.7</td><td>4.5</td><td>6.2</td><td>8.9</td><td>9.9</td></tr><tr><td>AMD GPUs</td><td>0.1</td><td>0.5</td><td>0.7</td><td>0.6</td><td>1.0</td></tr><tr><td>Google TPUs</td><td>1.2</td><td>1.7</td><td>1.8</td><td>4.5</td><td>8.0</td></tr><tr><td>AWS Inferenta + Trainium</td><td>0.3</td><td>0.8</td><td>1.5</td><td>1.9</td><td>3.3</td></tr><tr><td>Meta MTIA</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.3</td><td>0.5</td></tr><tr><td>Microsoft MAIA</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.2</td><td>0.7</td></tr><tr><td>Total</td><td>3.3</td><td>7.4</td><td>10.1</td><td>16.3</td><td>23.3</td></tr><tr><td>Growth Y/Y%</td><td></td><td>128%</td><td>36%</td><td>62%</td><td>43%</td></tr><tr><td>GPU % total units</td><td>55%</td><td>67%</td><td>68%</td><td>58%</td><td>47%</td></tr><tr><td>ASIC/XPU % total units</td><td>45%</td><td>33%</td><td>32%</td><td>42%</td><td>53%</td></tr></table>

![](images/10013a6e85d28069e63cf1852b8fa0bfd3e1039ad12a59e474778c77658dbb4f.jpg)

<details>
<summary>bar chart</summary>

| Year | GPU Units | ASIC/XPU Units |
| :--- | :--- | :--- |
| 2023 | 1.8 | 1.5 |
| 2024 | 5.0 | 2.5 |
| 2025 | 6.8 | 3.3 |
| 2026E | 9.5 | 6.8 |
| 2027E | 10.9 | 12.5 |
</details>

Source: Company reports, JPM

Demand is rising for custom ASICs because many of the large OEMs/CSPs/Hyperscalers are looking for more differentiation, better performance, lower power consumption, and overall lower cost of ownership versus off-the-shelf chip solutions (or ASSPs) – Broadcom (#1 80-85% share high-end ASIC mkt) and Marvell (#2 10-12% share high-end ASIC mkt) should continue to dominate this opportunity.  
These same customers do not have the capabilities to do large, complex system-on-a-chip (SOC) designs, nor do they have the broad IP portfolio of on-chip design blocks, like high-speed SERDES capabilities or high-speed memory interface technology. They need to engage with semiconductor companies that have the IP and chip design expertise.  
The digital custom AI ASIC market is a \~60-\$70B market opportunity in CY26 growing at a 40-50%+ CAGR over the next few years :

■ Cloud/Hyperscale ASICS (AI processors, SmartNICs, Security/Video processors, Networking/Storage acceleration)

We estimate Broadcom will drive \$60B+ in total AI revenue in FY26 (up significantly from \~\$20B in FY25) as new products/programs ramp (Meta MTIA 3nm ASIC programs, Google TPUv7/V8 3nm, Anthropic (TPU), OpenAI, and Softbank/ARM)....tracking \$150B+ AI revs in FY27  
We expect Marvell to drive \~\$9.3B of data center revenue in CY26 (up from \~\$6.1B in CY25), and \~\$14.6B in CY27 – strong optical DSP shipments (800G/1.6T, coherent lite, initial CPO ramp) and continued Amazon Trainium 3 and 4 ASIC engagement and start of Microsoft 3nm Maia ASIC ramp....overall 25+ XPU/XPU attach ASIC wins.

<table><tr><td>ASIC Customers</td><td>Programs</td><td>Technology</td><td>Status</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>28nm Technology</td><td>Deployed</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>16nm Technology</td><td>Deployed</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>16nm Technology</td><td>Deployed</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>7nm Technology</td><td>Deployed</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>5nm Technology</td><td>Deployed</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>3nm Technology v6</td><td>Ramping Now</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>3nm/2nm Next Gen v7</td><td>Tape Out 1H25, Ramp 2H26</td></tr><tr><td>Cloud Titan A</td><td>AI Chip</td><td>2nm/sub-2nm Next Gen v8</td><td>CY27/CY28</td></tr><tr><td>Cloud Titan A</td><td>VCU Chip</td><td>12nm/5nm Technology</td><td>Deployed/In Design</td></tr><tr><td>Cloud Titan A</td><td>Switching</td><td>7nm technology</td><td>Deployed</td></tr><tr><td>Cloud Titan A</td><td>ARM CPU</td><td>5nm Technology</td><td>2024</td></tr><tr><td colspan="4"></td></tr><tr><td>Cloud Titan B</td><td>DPU</td><td>7nm/5nm/3nm</td><td>2021/2022/2023</td></tr><tr><td>Cloud Titan B</td><td>Video Trans</td><td>7nm technology</td><td>2021/2022</td></tr><tr><td>Cloud Titan B</td><td>Storage</td><td>5nm</td><td>2023</td></tr><tr><td>Cloud Titan B</td><td>Security</td><td>7nm technology</td><td>2021</td></tr><tr><td>Cloud Titan B</td><td>AI Chip</td><td>7nm and 5nm</td><td>Deploying</td></tr><tr><td>Cloud Titan B</td><td>AI Chip</td><td>3nm Technology</td><td>End CY25 ramp</td></tr><tr><td>Cloud Titan B</td><td>AI Chip</td><td>3nm Technology</td><td>Mid CY26 ramp</td></tr><tr><td>Cloud Titan B</td><td>AI Chip</td><td>2nm Technology</td><td>CY27 ramp</td></tr><tr><td colspan="4"></td></tr><tr><td>Cloud Titan C</td><td>Security</td><td>7nm technology</td><td>2020/2021</td></tr><tr><td>Cloud Titan C</td><td>DPU</td><td>7nm/5nm technology</td><td>2022/2024</td></tr><tr><td>Cloud Titan C</td><td>Storage</td><td>5nm technology</td><td>2023</td></tr><tr><td>Cloud Titan C</td><td>AI Chip</td><td>3nm Technology</td><td>CY26 ramp</td></tr><tr><td>Cloud Titan C</td><td>AI Chip</td><td>2nm Technology</td><td>CY27 ramp</td></tr><tr><td colspan="4"></td></tr><tr><td>Cloud Titan D</td><td>AI Chip</td><td>5nm technology</td><td>2024/2025</td></tr><tr><td>Cloud Titan D</td><td>AI Chip</td><td>3nm Technology</td><td>CY26 ramp</td></tr><tr><td>Cloud Titan D</td><td>AI Chip</td><td>2nm Technology</td><td>CY27 ramp</td></tr><tr><td>Cloud Titan D</td><td>Storage</td><td>5nm technology</td><td>2023/2024</td></tr><tr><td colspan="4"></td></tr><tr><td>AI Compute OEM (OpenAI)</td><td>AI Chip</td><td>3nm/2nm 3DSOIC</td><td>2026</td></tr><tr><td>SoftBank/Arm</td><td>AI Chip</td><td>3nm/2nm 3DSOIC</td><td>2026</td></tr><tr><td>Asia Hyperscaler#2</td><td>AI Chip</td><td>3nm</td><td>CY26 ramp</td></tr><tr><td>Asia Hyperscaler#3</td><td>AI Chip</td><td>3nm</td><td>CY27 ramp</td></tr></table>

Source: JPM Research

## Broadcom ASIC Pipeline:

100+ Cumulative 7nm/5nm/3nm/2nm Designs

Powerful 2nm/3nm ASIC platform (faster time to market):

\* 50-120B+ transistors per chip  
\* 2nm/3nm/5nm chiplet architecture  
\* 50/100/200G Proven SERDES I/O  
\* Broadest IP Portfolio  
\* Adv Pkg (HBM 3/4, 2.5/3D SOIC)  
\* Co-pkg Electro/Optical (CPO)

## Marvell ASIC Pipeline:

70+ Cumulative 12nm/5nm/3nm/2m Designs
Starting to Engage on <2nm

\* 50-120B+ transistors per chip  
\* 50/100G Proven SERDES I/O  
\* SRAM memory IP (LPU)  
\* Broad IP Portfolio  
\* Adv Pkg

Broadcom AI ASIC Pipeline

<table><tr><td></td><td>ASIC Supplier</td><td>Generations Won</td><td>Ramp Timing/Duration</td></tr><tr><td>Google TPU AI ASIC processor family</td><td>Broadcom 7nm, 5nm, 3nm, 2nm</td><td>V1, V2, V3, V4, V5, V6, V7, V8</td><td>Ramping now through CY28</td></tr><tr><td>Meta MTIA AI ASIC processor family</td><td>Broadcom 7nm, 5nm, 3nm, 2nm</td><td>Gen 1, Gen2, Gen 3 and follow-ons</td><td>Ramping now through CY28</td></tr><tr><td>Bytedance AI Video/AI Networking</td><td>Broadcom 5nm, 3nm</td><td>Gen 1, Gen2 and follow-ons</td><td>Ramping now through CY28</td></tr><tr><td>OpenAI XPU AI ASIC processor family</td><td>Broadcom 2nm and 3nm</td><td>Gen1 and Gen 2 on 3DSOIC pkging</td><td>Ramping CY26-CY29</td></tr><tr><td>SoftBank/Arm XPU AI ASIC processor family</td><td>Broadcom 2nm and 3nm</td><td>Gen 1 and Gen 2 on 3DSOIC pkging</td><td>Ramping CY26-CY29</td></tr><tr><td>Anthropic/TPU Rackscale</td><td>Broadcom 3nm</td><td>TPUv6p - Ironwood</td><td>Ramp 2H CY26</td></tr><tr><td>Customer #7 AI ASIC XPU (Asia Hyperscale Customer)</td><td>Broadcom 3nm, 2nm</td><td>Gen 1, Gen 2</td><td>Ramping End 26</td></tr><tr><td>Customer #8 AI ASIC XPU (Asia Hyperscale Customer)</td><td>Broadcom 3nm, 2nm</td><td>Gen 1, Gen2</td><td>Ramping CY27</td></tr></table>

Marvell AI ASIC Pipeline

<table><tr><td>Amazon AI ASIC processor family</td><td>Marvell 5nm/3nm/2nm</td><td>Gen 2, Gen 3, Gen 4 and follow-ons</td><td>Ramping Now</td></tr><tr><td>Microsoft Maia AI ASIC processor family</td><td>Marvell 3nm/2nm</td><td>Gen 2 and follow-ons</td><td>Ramping End CY26</td></tr><tr><td>Google AI ARM CPU processor family</td><td>Marvell 5nm/3nm</td><td>Gen 1 and follow-ons</td><td>Ramping Now</td></tr><tr><td>Cloud/Hyperscale FBNIC (SmartNic)</td><td>Marvell 5nm/3nm</td><td>Gen 1 and follow-ons</td><td>Ramp 2H25</td></tr><tr><td>Other XPU Attach (SmartNIC, Fabric, Memory)</td><td>Marvell 3nm/2nm</td><td>Gen 1 and follow-ons</td><td>Ramping CY26</td></tr></table>

Source: JPM Research

![](images/00b8e79b10a787e85af5a537094302d18f9ba453cb9af07c7d8c563c676c8695.jpg)

<details>
<summary>text_image</summary>

200 GE I/F
MAX
MAX
HBM
MAX
MAX
Compute Die
MAX
MAX
HBM
MAX
MAX
DDR
MAX
MAX
MAX
Compute Die
MAX
MAX
MAX
SRAM Die
MAX
MAX
PCIe I/F
HBM
MAX
MAX
HBM
MAX
CXL
</details>

Source: Broadcom and JPM

## Broadcom Has Developed a 2nm/3nm AI ASIC Reference Platform to Enable Customers Fast Time to Market:

• 2nm/3nm/5nm compute die  
• 100/200Gbps I/O die  
• 2.5D/3D SOIC (chip stacking)

• 2nm/3nm chip stacking  
• Advanced substrate manuf capability in CY26

• Chip-to-Chip I/O connectivity

• AI/Compute/IO/Memory/Interface IP

• Rackscale system expertise ramping CY26

## Broadcom is working with 3 of its 5 AI ASIC customers on next-gen 3D SOIC chip stacking ASIC programs

![](images/5697dcbcf1cb9039b41ab69257c4edf0ab749bf70685b06c84390d0469847e29.jpg)

<details>
<summary>text_image</summary>

Enhancing XPUs with custom HBM architecture
Standard HBM
XPU
HBM
HBM
Custom HBM
XPU
cHBM
cHBM
cHBM
Custom vs. standard HBM
Higher performance D2D I/O
70% lower interface power
25% more XPU silicon area
33% more HBM stacks
Superior TOO
</details>

Source: Marvell and JPM

## Marvell has a strong IP portfolio of 5nm, 3nm, and 2nm

Recently unveiled HBM memory IP differentiation that drives:

• 33% more HBM stacks per package  
• 70% lower interface power  
• 25% more XPU silicon area  
• Marvell has won numerous HBM4 ASIC logic base die programs with DRAM suppliers

![](images/ee65c99

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by

changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
