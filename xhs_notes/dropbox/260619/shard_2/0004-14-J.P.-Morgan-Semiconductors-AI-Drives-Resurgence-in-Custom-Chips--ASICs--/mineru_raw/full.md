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

![](images/ee65c994990bb6a18e03ec96d098a632e2a73c0870119eefe436eac253998a27.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["SoftBank Group"] --> B["Project &quot;Izanagi&quot; AI XPU (CPU/GPU) ASIC Chip"]
  B --> C["Functional Specification"]
  C --> D["Broadcom ASIC Partner"]
  D --> E["ARM CPU IP"]
  D --> F["Graphcore AI Accelerator IP"]
  E --> G["Al Accelerator IP"]
  F --> H["Al Accelerator IP"]
  G --> I["PCI Block"]
  H --> I
  I --> J["PCI Block"]
    style I fill:#f9f,stroke:#333
    style J fill:#ccf,stroke:#333
```
</details>

Source: JPM

Meta/ARM CPU Announcement Is NOT the Broadcom ASIC – Meta Project Is CPU-only....The Broadcom ASIC Is a Full-Blown AI XPU (CPU+AI Accelerator)

Merchant (Semi Co.) Chip Design Flow  
![](images/e6397fe66d9d4dd0b38e82df5bc5834bd61d6759b38e3419b414d42cd3188c39.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Behavioral/Functional Model (RTL)"] --> B["RTL Simulation"]
  B --> C["Logic Synthesis (RTL to Logic Gate)"]
  C --> D["Floor Planning"]
  D --> E["Place and Route"]
  E --> F["Parasitic Extraction"]
  F --> G["Static Timing Analysis"]
  G --> H["GDSII Tape-Out"]
  H --> I["To Mask Shop/Foundry"]
    
    B <--> J["Functional Verification"]
    C <--> K["Verification\nPhysical Timing\nFunctional Simulation\nHW Verific"]
    E <--> L["IP Blocks\nI/O\nCPU\nRAM\nLogic Cells"]
```
</details>

ASIC Chip Design Flow  
![](images/adcadd0d06ef7cddeb9bd89c538dbdf84dea85124b19a581845da0f03a6b30ed.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Behavioral/Functional Model (RTL)"] --> B["RTL Simulation"]
    B <--> C["Functional Verification"]
  D["Logic Synthesis (RTL to Logic Gate)"] --> E["Floor Planning"]
    E <--> F["Verification"]
  G["Static Timing Analysis"] --> H["GDSII Tape-Out"]
  I["Parasitic Extraction"] --> H
  J["Place and Route"] --> E
  K["IP Blocks"] --> L["I/O"]
  K --> M["CPU"]
  K --> N["RAM"]
  K --> O["Logic Cells"]
  K --> P["Custom"]
  Q["ASIC Chip Design Partner *AVGO *MRVL"] --> R["Static Timing Analysis"]
  S["IP Blocks"] --> T["I/O"]
  S --> U["CPU"]
  S --> V["RAM"]
  S --> W["Logic Cells"]
  S --> X["Custom"]
  Y["Verification"] --> Z["Physical Timing"]
  Y --> AA["Functional Simulation"]
  Y --> AB["HW Verific"]
  AC["To Mask Shop/Foundry"] --> AD["Static Timing Analysis"]
```
</details>

COT Chip Design Flow (System OEM/Cloud Titan Does 85-100% of Design And IP)  
![](images/0c6453e3ffde270a80dbfca3d97783a000dab0ef865be2ecab17bfb6ba81a066.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Behavioral/Functional Model (RTL)"] --> B["RTL Simulation"]
  B --> C["Logic Synthesis (RTL to Logic Gate)"]
  C --> D["Floor Planning"]
  D --> E["Place and Route"]
  E --> F["Parasitic Extraction"]
  F --> G["Static Timing Analysis"]
  G --> H["GDSII Tape-Out"]
  H --> I["To Mask Shop/Foundry"]
    
    subgraph OEM
  J["Cloud Titan"] --> B
  K["In-House"] --> C
  L["Design Team"] --> C
    end
    
    subgraph IP Blocks
  M["I/O"] --> N["Logic Cells Custom"]
  O["CPU"] --> N
  P["RAM"] --> N
    end
    
    subgraph Verification
  Q["Physical Timing"] --> R["Functional Simulation"]
  S["HW Verific"] --> T["Verification"]
    end
    
    style A fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
```
</details>

## Example ASIC Designs:

1) Google TPU (AVGO ASIC)  
2) Google VCU (MRVL ASIC)  
3) Meta TPU (AVGO ASIC)  
4) AMZN 3 $^{rd}$ Gen (MRVL ASIC)  
5) Google CPU (MRVL ASIC)  
6) Cisco Switching (AVGO/MRVL)  
7) Nokia 5G BTS (AVGO/MRVL)  
8) Samsung 5G BTS (MRVL ASIC)

## Example COT Designs:

1) Apple A and M series CPU  
2) AMZN 1 $^{st}$ /2 $^{nd}$ Generation SoC  
3) Tesla DOJO AI SoC  
4) Cisco - Cloud Scale SoC

## Broadcom Update On ASIC Pipeline

- Google TPU orders continue to add to the CY27 backlog - currently around 6.5M+ V7/V8 shipments....\~\$100B in revenues  
- Google Near-term – 3K wafer starts per week TPUv7 (Ironwood) – sets up for strong 2H26 (along with initial V8 ramp)...support Google Internal and Anthropic.  
Meta ramping first 3nm program (Athena) NOW, “Iris” 3nm Mid-CY26, “Arke” End CY26, “Astrid” 1H27 - added new 2nm program for 2H27 ramp.....total five programs – 1GW CY27  
OpenAI (2nm/3nm) and Softbank/ARM XPU first silicon both out of fab – functionality looks good....on track for end of year/CY27 ramp – OpenAI 1GW in CY27  
Google/AVGO assessing v8i “next-gen” – 4 compute die, 12 HBM stacks- extend life of TPUv8i for 6 more months....then ramp next gen v9/v10 2nm TPU (4 compute, 16 HBM)...either strategy will NOT result in revenue “air-pocket” in CY28 (70%+ growth CY28)

## Marvell Update on ASIC Pipeline

XPU ASIC Trainium 3 (3nm) production commenced last quarter – on track to ramp mid-CY26.....Trainium 4 (2nm) on track to ramp 2H CY27  
Celestial CPO solution (Tied to Trainium 4) have seen upside to 2H27 orders  
XPU ASIC Microsoft Maia 3nm – taping out soon – program set to ramp beginning CY27 (full ASIC engagement - FE/BE design)  
XPU attach: multi-billion dollar /multi-year win for Google SmartNIC/DPU ASIC – ramp CY27 - CXL controller ASIC – ramp 2H26  
XPU attach: early engagement on “LPU” offload inference engine (recall MRVL did 1 $^{st}$ gen Groq LPU ASIC due to strong SRAM memory IP) – No wins yet, but expected

## Disclosures

Gartner: All statements in this report attributable to Gartner represent JPM's interpretation of data opinion or viewpoints published as part of a syndicated subscription service by Gartner, Inc., and have not been reviewed by Gartner. Each Gartner publication speaks as of its original publication date (and not as of the date of this report). The opinions expressed in Gartner publications are not representations of fact, and are subject to change without notice.

## Disclosures

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables, are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

## Disclosures

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.  
For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

## Disclosures

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Securities LLC (“JPMS”) acts as authorized participant for substantially all U.S.-listed ETFs. To the extent that any ETFs are mentioned in this report, JPMS may earn commissions and transaction-based compensation in connection with the distribution of those ETF shares and may earn fees for performing other trade-related services, such as securities lending to short sellers of the ETF shares. JPMS may also perform services for the ETFs themselves, including acting as a broker or dealer to the ETFs. In addition, affiliates of JPMS may perform services for the ETFs, including trust, custodial, administration, lending, index calculation and/or maintenance and other services.

Options and Futures related research: If the information contained herein regards options- or futures-related research, such information is available only to persons who have received the proper options or futures risk disclosure documents. Please contact your JPM Representative or visit https://www.theocc.com/components/docs/riskstoc.pdf for a copy of the Option Clearing Corporation's Characteristics and Risks of Standardized Options or https://www.finra.org/sites/default/files/2020-08/Security\_Futures\_Risk\_Disclosure\_Statement\_2020.pdf for a copy of the Security Futures Risk Disclosure Statement.

Changes to Interbank Offered Rates (IBORs) and other benchmark rates: Certain interest rate benchmarks are, or may in the future become, subject to ongoing international, national and other regulatory guidance, reform and proposals for reform. For more information, please consult:
https://www.JPM.com/global/disclosures/interbank\_offered\_rates

Private Bank Clients: Where you are receiving research as a client of the private banking businesses offered by JPM Chase & Co. and its subsidiaries (“JPM Private Bank”), research is provided to you by JPM Private Bank and not by any other division of JPM, including, but not limited to, the JPM Corporate and Investment Bank and its Global Research division.

Legal entity responsible for the production and distribution of research: The legal entity identified below the name of the Reg AC Research Analyst who authored this material is the legal entity responsible for the production of this research. Where multiple Reg AC Research Analysts authored this material with different legal entities identified below their names, these legal entities are jointly responsible for the production of this research. Where more than one legal entity is listed under an analyst's name, the first legal entity is responsible for the production unless stated otherwise. Research Analysts from various JPM affiliates may have contributed to the production of this material but may not be licensed to carry out regulated activities in your jurisdiction (and do not hold themselves out as being able to do so). Unless otherwise stated below in the legal entity disclosures, this material has been distributed by the legal entity responsible for production, or where more than one legal entity is listed under the analyst's name, the first legal entity will be responsible for distribution. If you have any queries, please contact the relevant Research Analyst in your jurisdiction or the entity in your jurisdiction that has distributed this research material.

## Legal Entities Disclosures and Country-/Region-Specific Disclosures:

Argentina: JPM Chase Bank N.A Sucursal Buenos Aires is regulated by Banco Central de la República Argentina (“BCRA”- Central Bank of Argentina) and Comisión Nacional de Valores (“CNV”- Argentinian Securities Commission - ALYC y AN Integral N°51).

Australia: JPM Securities Australia Limited (“JPMSAL”) (ABN 61 003 245 234/AFS Licence No: 238066) is regulated by the Australian Securities and Investments Commission and is a Market Participant of ASX Limited, a Clearing and Settlement Participant of ASX Clear Pty Limited and a Clearing Participant of ASX Clear (Futures) Pty Limited. This material is issued and distributed in Australia by or on behalf of JPMSAL only to "wholesale clients" (as defined in section 761G of the Corporations Act 2001). A list of all financial products covered can be found by visiting https://www.jpmm.com/research/disclosures. JPM seeks to cover companies of relevance to the domestic and international investor base across all Global Industry Classification Standard (GICS) sectors, as well as across a range of market capitalisation sizes. If applicable, in the course of conducting public side due diligence on the subject company(ies), the Research Analyst team may at times perform such diligence through corporate engagements such as site visits, discussions with company representatives, management presentations, etc. Research issued by JPMSAL has been prepared in accordance with JPM Australia’s Research Independence Policy which can be found at the following link: JPM Australia - Research Independence Policy.

## Disclosures

Brazil: Banco JPM S.A. is regulated by the Comissao de Valores Mobiliarios (CVM) and by the Central Bank of Brazil. Ombudsman JPM: 0800-7700847 / 0800-7700810 (For Hearing Impaired) / ouvidoria.jp.morgan@jpmchase.com.  
Canada: JPM Securities Canada Inc. is a registered investment dealer, regulated by the Canadian Investment Regulatory Organization and the Ontario Securities Commission and is the participating member on Canadian exchanges. This material is distributed in Canada by or on behalf of JPM Securities Canada Inc.  
Chile: Inversiones JPM Limitada is an unregulated entity incorporated in Chile.  
China: JPM Securities (China) Company Limited has been approved by CSRC to conduct the securities investment consultancy business.  
Colombia: Banco JPM Colombia S.A. is supervised by the Superintendencia Financiera de Colombia (SFC). Any reference in this material to products or services offered abroad by entities other than the Bank in Colombia is included exclusively for descriptive purposes. Such references do not constitute, and should not be construed as, promotional activity or the provision of financial products or services within Colombian territory, as defined under applicable Colombian regulation.  
Dubai International Financial Centre (DIFC): JPM Chase Bank, N.A., Dubai Branch is regulated by the Dubai Financial Services Authority (DFSA) and its registered address is Dubai International Financial Centre - The Gate, West Wing, Level 3 and 9 PO Box 506551, Dubai, UAE. This material has been distributed by JPM Chase Bank, N.A., Dubai Branch to persons regarded as professional clients or market counterparties as defined under the DFSA rules.  
European Economic Area (EEA): Unless specified to the contrary, research is distributed in the EEA by JPM SE (“JPM SE”), which is authorised as a credit institution by the Federal Financial Supervisory Authority (Bundesanstalt für Finanzdienstleistungsaufsicht, BaFin) and jointly supervised by the BaFin, the German Central Bank (Deutsche Bundesbank) and the European Central Bank (ECB). JPM SE is a company headquartered in Frankfurt with registered address at TaunusTurm, Taunustor 1, Frankfurt am Main, 60310, Germany. The material has been distributed in the EEA to persons regarded as professional investors (or equivalent) pursuant to Art. 4 para. 1 no. 10 and Annex II of MiFID II and its respective implementation in their home jurisdictions (“EEA professional investors”). This material must not be acted on or relied on by persons who are not EEA professional investors. Any investment or investment activity to which this material relates is only available to EEA relevant persons and will be engaged in only with EEA relevant persons.  
Hong Kong: JPM Securities (Asia Pacific) Limited (CE number AAJ321) is regulated by the Hong Kong Monetary Authority and the Securities and Futures Commission in Hong Kong, and JPM Broking (Hong Kong) Limited (CE number AAB027) is regulated by the Securities and Futures Commission in Hong Kong. JPM Chase Bank, N.A., Hong Kong Branch (CE Number AAL996) is regulated by the Hong Kong Monetary Authority and the Securities and Futures Commission, is organized under the laws of the United States with limited liability. Where the distribution of this material is a regulated activity in Hong Kong, the material is distributed in Hong Kong by or through JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited.  
India: JPM India Private Limited (Corporate Identity Number - U67120MH1992FTC068724), having its registered office at JPM Tower, Off. C.S.T. Road, Kalina, Santacruz - East, Mumbai – 400098, is registered with the Securities and Exchange Board of India (SEBI) as a ‘Research Analyst’ having registration number INH000001873. JPM India Private Limited is also registered with SEBI as a member of the National Stock Exchange of India Limited and the Bombay Stock Exchange Limited (SEBI Registration Number – INZ000239730) and as a Merchant Banker (SEBI Registration Number - MB/INM000002970). Telephone: 91-22-6157 3000, Facsimile: 91-22-6157 3990 and Website: http://www.jpmipl.com. JPM Chase Bank, N.A. - Mumbai Branch is licensed by the Reserve Bank of India (RBI) (Licence No. 53/ Licence No. BY.4/94; SEBI - IN/CUS/014/ CDSL : IN-DP-CDSL-444-2008/ IN-DP-NSDL-285-2008/ INBI00000984/ INE231311239) as a Scheduled Commercial Bank in India, which is its primary license allowing it to carry on Banking business in India and other activities, which a Bank branch in India are permitted to undertake. For non-local research material, this material is not distributed in India by JPM India Private Limited. Compliance Officer: Ashutosh Sharma; ashutosh.j.sharma@jpmchase.com; +912261575002. Grievance Officer: Ramprasadh K, jpmipl.research.feedback@JPM.com; +912261573000. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Please visit Terms and Conditions and Most Important Terms and Conditions (MITC). The annual Compliance audit report is available at http://www.jpmipl.com/#research.  
Indonesia: PT JPM Sekuritas Indonesia is a member of the Indonesia Stock Exchange and is registered and supervised by the Otoritas Jasa Keuangan (OJK).  
Korea: JPM Securities (Far East) Limited, Seoul Branch, is a member of the Korea Exchange (KRX). JPM Chase Bank, N.A., Seoul Branch, is licensed as a branch office of foreign bank (JPM Chase Bank, N.A.) in Korea. Both entities are regulated by the Financial Services Commission (FSC) and the Financial Supervisory Service (FSS). For non-macro research material, the material is distributed in Korea by or through JPM Securities (Far East) Limited, Seoul Branch.  
Japan: JPM Securities Japan Co., Ltd. and JPM Chase Bank, N.A., Tokyo Branch are regulated by the Financial Services Agency in Japan.  
Malaysia: This material is issued and distributed in Malaysia by JPM Securities (Malaysia) Sdn Bhd (18146-X), which is a Participating Organization of Bursa Malaysia Berhad and holds a Capital Markets Services License issued by the Securities Commission in Malaysia.  
Mexico: JPM Casa de Bolsa, S.A. de C.V. and JPM Grupo Financiero are members of the Mexican Stock Exchange and are authorized to act as a broker dealer by the National Banking and Securities Exchange Commission. (“Bolsa Mexicana de Valores”) and the Institutional Stock Exchange (“Bolsa Institucional de Valores”), and it is authorized to act as a broker dealer by the National Banking and Securities Exchange Commission (“Comisión Nacional Bancaria y de Valores”).

## Disclosures

New Zealand: This material is issued and distributed by JPMSAL in New Zealand only to "wholesale clients" (as defined in the Financial Markets Conduct Act 2013). JPMSAL is registered as a Financial Service Provider under the Financial Service providers (Registration and Dispute Resolution) Act of 2008.

Philippines: JPM Securities Philippines Inc. is a Trading Participant of the Philippine Stock Exchange and a member of the Securities Clearing Corporation of the Philippines and the Securities Investor Protection Fund. It is regulated by the Securities and Exchange Commission.

Singapore: This material is issued and distributed in Singapore by or through JPM Securities Singapore Private Limited (JPMSS) [MDDI (P) 057/08/2025 and Co. Reg. No.: 199405335R], which is a member of the Singapore Exchange Securities Trading Limited, and/or JPM Chase Bank, N.A., Singapore branch (JPMCB Singapore), both of which are regulated by the Monetary Authority of Singapore. This material is issued and distributed in Singapore only to accredited investors, expert investors and institutional investors, as defined in Section 4A of the Securities and Futures Act, Cap. 289 (SFA). This material is not intended to be issued or distributed to any retail investors or any other investors that do not fall into the classes of “accredited investors,” “expert investors” or “institutional investors,” as defined under Section 4A of the SFA. Recipients of this material in Singapore are to contact JPMSS or JPMCB Singapore in respect of any matters arising from, or in connection with, the material.

South Africa: JPM Equities South Africa Proprietary Limited and JPM Chase Bank, N.A., Johannesburg Branch are members of the Johannesburg Securities Exchange and are regulated by the Financial Services Conduct Authority (FSCA).

Taiwan: JPM Securities (Taiwan) Limited is a participant of the Taiwan Stock Exchange (company-type) and regulated by the Taiwan Securities and Futures Bureau. Material relating to equity securities is issued and distributed in Taiwan by JPM Securities (Taiwan) Limited, subject to the license scope and the applicable laws and the regulations in Taiwan. To the extent that JPM Securities (Taiwan) Limited produces research materials on securities not listed on the Taiwan Stock Exchange or Taipei Exchange (“Non-Taiwan Listed Securities”), these materials shall not constitute securities recommendations for the purpose of applicable Taiwan regulations, and, for the avoidance of doubt, JPM Securities (Taiwan) Limited does not act as broker for Non-Taiwan Listed Securities. According to Paragraph 2, Article 7-1 of Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers (as amended or supplemented) and/or other applicable laws or regulations, please note that the recipient of this material is not permitted to engage in any activities in connection with the material that may give rise to conflicts of interests, unless otherwise disclosed in the “Important Disclosures” in this material.

Thailand: This material is issued and distributed in Thailand by JPM Securities (Thailand) Ltd., which is a member of the Stock Exchange of Thailand and is regulated by the Ministry of Finance and the Securities and Exchange Commission. The registered address is 548 One City Center Building, 50th Floor, Ploenchit Road, Lymphini, Pathum Wan, Bangkok 10330.

UK: Research is produced in the UK by JPM Securities plc (“JPMS plc”) which is a member of the London Stock Exchange and is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority or JPM Markets Limited (“JPMML Ltd”) which is authorised and regulated by the Financial Conduct Authority. Unless specified to the contrary, this material is distributed in the UK by JPMS plc and is directed in the UK only to: (a) persons having professional experience in matters relating to investments falling within article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) (Order) 2005 (“the FPO”); (b) persons outlined in article 49 of the FPO (high net worth companies, unincorporated associations or partnerships, the trustees of high value trusts, etc.); or (c) any persons to whom this communication may otherwise lawfully be made; all such persons being referred to as "UK relevant persons". This material must not be acted on or relied on by persons who are not UK relevant persons. Any investment or investment activity to which this material relates is only available to UK relevant persons and will be engaged in only with UK relevant persons. A description of JPM EMEA’s policy for prevention and avoidance of conflicts of interest related to the production of Research can be found at the following link: JPM EMEA - Research Independence Policy.

U.S.: JPM Securities LLC (“JPMS”) is a member of the NYSE, FINRA, SIPC, and the NFA. JPM Chase Bank, N.A. is a member of the FDIC. Material published by non-U.S. affiliates is distributed in the U.S. by JPMS who accepts responsibility for its content.

General: Additional information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities

## Disclosures

and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by

changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.