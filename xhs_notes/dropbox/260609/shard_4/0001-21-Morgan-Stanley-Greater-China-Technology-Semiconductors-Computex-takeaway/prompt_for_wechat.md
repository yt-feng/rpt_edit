你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Greater China Technology Semiconductors | Asia Pacific

# Computex takeaways: Cloud, PC and old memory

Data points suggest a stronger outlook. The memory optimization on server is more of a supply issue. Recent share price volatility should provide a good entry point.

## Key Takeaways

■ Stronger outlook for CPU, GPU and peripherals (e.g. CXL) in 2027  
■ Agentic PC has not taken off yet, but PC semis remain stable on orders/GM into 2H26  
- Old memory: stronger pricing for legacy flash into 2H26  
We continue to like cloud semis and old memory over PC semis

Cloud semis: Need more supply for strong demand: GPU servers continue to ramp up with some minor changes to specs. CPU servers see strong demand mainly on AI/agentic applications (link). The lower DRAM content on ARM servers is more of a supply issue (link), while we see stronger demand on CXL to expand RDIMM usage in x86 CPUs. CPO-related components could see earlier pull-in from 1Q27 to 4Q26.

PC semis: Agentic PC makes sense but is very expensive; better than feared 2H26 outlook: Not only are there CPU and memory upgrades in RTX Spark NB, but we also see some brands upgrading the screen to 4K. For the DT, we learned potential specs could be 128GB DRAM with 4TB SSD; starting pricing point at US\$10k. Near term, we think PC semis customers are willing to pay the price hikes on memory. This suggests the PC semis GM could remain stable even with the further wafer cost hike from foundries in 3Q.

Old memory: likely in more shortage: We believe legacy NAND (SLC), could enjoy stronger growth outlook into the next two years. SLC NAND could be used as the high performance eSSD in the datacenter (link). Meanwhile, we also believe SLC will be used by hard disk drives to enhance performance. We also noticed high-density NOR pricing hit US\$8 from the prior US\$1 at channel, likely driven by 2x content in VR vs GB.

Stock implications – stay bullish amid market volatility: We continue to like cloud semis (Aspeed, Montage, both OW), old memory (Winbond, Macronix, APMemory, Gigadevice, all OW). PC semis could see a better than feared 2H outlook. Parade (OW) and Elan (OW) have new growth drivers vs Realtek (EW), Novatek (UW), Asmedia (UW).

MS TAIWAN LIMITED+

## Daniel Yen, CFA

Equity Analyst

Daniel.Yen@morganstanley.com +886 2 2730-2863

## Charlie Chan

Equity Analyst

Charlie.Chan@morganstanley.com +886 2 2730-1725

MS ASIA LIMITED+

## Daisy Dai, CFA

Equity Analyst

Daisy.Dai@morganstanley.com +852 2848-7310

MS TAIWAN LIMITED+

## Tiffany Yeh

Equity Analyst

Tiffany.Yeh@morganstanley.com +886 2 7712-3032

MS ASIA LIMITED+

## Ethan Jia

Research Associate

Ethan.Jia@morganstanley.com +852 3963-2287

MS TAIWAN LIMITED+

## Lucas Wang

Research Associate

Lucas.Wang@morganstanley.com +886 2 2730-2875

![](images/67fff9d47a115a734b9829cf6901853402946bd7a1a9783ec796576b76728676.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## GREATER CHINA TECHNOLOGY SEMICONDUCTORS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Key takeaways

## Cloud remains strong, especially on the CPU side:

Vera CPU is built for running agents, aside from pre-training, post-training and inference. Highlights include: 1) high IPCs (instructions per clock) - 10 instructions fetched, decoded, and executed per clock; 2) high bandwidth per core - each of the 88 Olympus cores is provisioned with up to 14 GB/s of memory bandwidth; 3) high external bandwidth of 1.2 TB/s and high core-to-core bandwidth of 3.4 TB/s; 4) high energy efficiency, as the first CPU to use LPDDR5X. Vera achieves 3x more bandwidth per core vs x86 CPUs with DDR5, and 40% lower peak memory latency vs x86, 1.8x agentic sandbox performance of x86 CPUs.

During his meeting with financial analysts (link), Nvidia's CEO mentioned that they plan to sell millions of Vera CPUs; half of those will be in the headnode, and outside of headnode, the other half of the CPUs are to orchestrate workloads or to be in storage servers. When asked about the future CPU to GPU ratio, his response was that it's hard to guess the ratio, but that the AI factory is valued for tokens, so he would suggest his customers to maximize the amount of Vera Rubin NVL72 racks, and put as many CPUs as necessary, while as few CPUs as possible to support the GPUs.

We believe the 2.5mn-4mn units of Vera CPUs in preparation for not just Vera Rubin but also standalone Vera CPU servers (link) represent a strong opportunity for Aspeed from its BMC content, and will be neutral for Montage as it continues to use SOCAMM rather RDIMM modules.

Separately, during Marvell's keynote speech, Nvidia's CEO shared his view that as useful AI arrives, agents have a particular computing pattern which is disaggregated and distributed, and that connectivity is necessary in the agentic AI computing process. This reaffirms our positive view on Montage as a leader in global memory interface chips and China PCIe interconnect chips.

Exhibit 1: Nvidia Vera CPU specs  
![](images/f28d4fcceae899082d23a5847138be52565c53d9626fcf8bf3b94f48a02374bf.jpg)

<details>
<summary>text_image</summary>

NVIDIA Vera
CPU for Agents
NVIDIA-Custom Olympus Core
88-Core / 176-Threads
Spatial Multithreading
10-Wide Instruction Fetch/Decode
2MB L2 per Core / 164MB L3
250W - 450W TDP
1.2 TB/s LPDDR5X ECC
40% Lower Loaded Latency
(vs x86)
3.4 TB/s Core-to-Core BW
1.4 TB/s PCIe Gen6
1.8 TB/s NVLink C2C
</details>

Source: Nvidia

Exhibit 2: Close-up look of a Vera CPU tray  
![](images/dd891769447ef32ac7c3e753978d7ea7ecf4a537b6d27d0b7bb4dee8ad00fac5.jpg)

<details>
<summary>natural_image</summary>

Model of a satellite or spacecraft module with grid panels and labeled 'MEMSIA Hens CPU tray' (no readable text beyond label)
</details>

Source: Nvidia

## AI PC is a positive driver but could take time to materialize:

During his meeting with financial analysts, Nvidia's CEO described the future AI PC as assistants that run all the time with easy access and strong agentic capabilities. The idea is to reshape what a PC is, from what is similar to a typewriter today to becoming an assistant in the future, implying significant ASP upside per PC. He believes the future AI PC will be run by agents smart enough to fully utilize the full features of the operating system and software, and as PCs become agentic (with "useful AI"), inference takes off. AI PC is not meant to be a competition to the agents run on cloud, as the cloud AI models will still be smarter, but the on-premise AI models will be smart enough; for example, Nemotron Ultra 3 is near the frontier and as good as the frontier model 6 months ago. AI PC will be uniquely useful when handling local files and local tools compared to AI on

cloud.

While AI PC is a positive driver for the PC semi names, their price points seem expensive. Our checks with PC brands at this year's Computex (link) suggest AI PCs with N1X will need to price at US\$2,899, while N1 models will be priced at US\$1,799. Our view on PC semi names remain cautious due to compressed demand and elevated component and manufacturing costs. On the positive side, customers seem fine with price hikes, and therefore we now believe PC semis players could see a better than feared 2H outlook. Parade (OW) and Elan (OW) have new growth drivers vs Realtek (EW), Novatek (UW), Asmedia (UW).

Exhibit 3: Nvidia RTX Spark Laptops with Blackwell RTX GPU, Grace CPU, and 128GB unified memory  
![](images/8db3bc16fe905731cf3a0aab66ee645478849fc664fc3ae40e3a31044ca7381d.jpg)

<details>
<summary>text_image</summary>

Announcing NVIDIA and
Microsoft Reinvent PC
Powered by RTX Spark

Blackwell RTX GPU
1 Petaflop FP4 AI Performance

20 Core Grace CPU
Custom Built with MediaTek

128 GB Unified Memory
600 GB/s NVLink C2C

Full NVIDIA Stack
CUDA | TensorRT | NVFP4
RTX Ray Tracing | DLSS | Reflex | G-SYNC
</details>

Source: Nvidia

Exhibit 4: Nvidia's Nemotron Ultra 3 open model is cost effective and fast  
![](images/46012876a819482138ad667aa9e7f6e83e1526f53d7df94ea6d6e2a241b0cefc.jpg)

<details>
<summary>line chart</summary>

Announcing NVIDIA Nemotron 3 Ultra
30% Lower Cost
| Model | Cost to Task Completion (USD) | % Coding Tasks Completed (%) |
|---|---|---|
| Alibaba | $250 | 22 |
| Kimi | $750 | 23 |
| NVIDIA | $500 | 21 |
| Z.ai | $750 | 22 |
| Kimi-K2.6 | $1,000 | 43 |
| GLM-5.1 | $1,500 | 60 |
| Qwen3.5 | $2,000 | 75 |
</details>

Source: Nvidia

Exhibit 5: Integrated AI vision & camera system for drones will be a major growth driver for Elan  
![](images/320ee95eac323cbaadd483e55c7a6d430d71a608eaa6b5959803746e06ef5573.jpg)

<details>
<summary>text_image</summary>

LAN
Integrated AI Vision &
Camera System
for Drones
Author: Heliangyuan Drones
High Speed Delivery Drone
Advanced Drones
Advanced Ground Control
Station
Solution & AI
Smart Accessories
System
BC
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.0000
12.
12.05
12.14
12.23
12.32
12.41
12.50
12.69
12.88
12.97
13.06
13.15
13.24
13.33
13.42
13.51
13.60
13.79
13.88
13.97
14.06
14.15
14.24
14.33
14.42
14.51
14.60
14.79
14.88
14.97
15.06
15.15
15.24
15.33
15.42
15.51
15.60
15.79
15.88
15.97
16.06
16.15
16.24
16.33
16.42
16.51
16.60
16.79
16.88
16.97
17.06
17.15
17.24
17.33
17.42
17.51
17.60
17.79
17.88
17.97
18.06
18.15
18.24
18.33
18.42
18.51
18.60
18.79
18.88
18.97
19.06
19.15
19.24
19.33
19.42
19.51
19.60
19.79
19.88
19.97
20.06
</details>

Source: Elan

Exhibit 6: Realtek's single-chip solution for ethernet and high-speed IO integration  
![](images/7ce794455039cf835afb803e3116c59cd97a7594d7338ea665b17a83c0d68e6e.jpg)

<details>
<summary>text_image</summary>

REALTEK
RTL9151AS
PCIe 60 Multi-IO Bridge Controller
Single-Chip for Ethernet and
High-Speed IO Integration
RTL9151AS
• The Only PCIe to Multi-IO Bridge Solution on the Market: BGA239
13x13mm2
• Flexible IO Configuration: 2.5GbE LAN, USB 10G, USB 5Gbps, USB 2.0,
and SATA 8
• Only 1-Lane PCIe UFP: Save PCIe Lanes for Other Applications Such as
Storage and Graphics
• Single Chip Solution: Simplifies PCB Layout Design
• Applications, Motherboards, (Mini) PCIe, NAS, Game Consoles, and More
REALTEK
</details>

Source: Realtek

## Old memory:

Kioxia shared their latest view on NAND demand and technology in the context of AI inference and especially agentic AI. Data center NAND bit demand is expected to grow at a 34% CAGR from 2025 to 2031, with AI inference CAGR at 56%, based on numbers quoted from Techinsights. In the era of agentic AI, inference becomes multi-step with increasing compute demand; long context increases data and KV cache, making storage efficiency and bandwidth critical; rack server systems grow in importance requiring frequent access to large data.

Kioxia proposed 3 key development directions for SSD products, namely super high IOPS GPU direct storage; high performance / high capacity context memory storage; and ultra high capacity training & inference data storage. The GPU direct storage solution is what we believe adopts Kioxia's proprietary SLC chip (link), which we believe is positive for legacy NAND vendors in our coverage, namely GigaDevice, Winbond, and Macronix.

More details on the GPU direct storage: HBM has very high performance but limited capacity, so there is a gap between data size and memory capacity. SSDs serve as an extension layer, but traditional data transfer goes through CPUs, which cases delays and overheads. GPU direct storage solves this by transferring data directly between SSD and

GPU. This reduces latency and improves efficiency. As a result, SSD can extend HBM with large capacity. This allows GPUs to handle larger data sets more efficiently. For example, with direct high-speed data transfer enabled by GPU direct storage, graph neural networks can stream large data sets from SSD to GPU with low latency, and RAG systems can process vector database indexing faster and more efficiently. With GPU direct storage, HBM, DRAM and SSD work together as one memory system.

Exhibit 7: Agentic AI transforms inference  
![](images/95ff56535c66cfe53842f31cc829d68ecc3f80f9497d097c60c5eb8d4e39550d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["In the Era - “Agentic AI”"] --> B["Traditional Inference AI"]
  B --> C["Simple Question / Request"]
  B --> D["AI Inference System"]
  B --> E["Multimodal Outputs"]
  C --> F["?"]
  D --> G["?"]
  E --> H["?"]
  F --> I["Document"]
  F --> J["How"]
  F --> K["Close"]
  F --> L["Smart"]
  G --> M["..."]
  H --> N["..."]
  I --> O["..."]
  J --> P["..."]
  K --> Q["..."]
  L --> R["..."]
  M --> S["Complex Objectives, Data, and Specific Expectations"]
  N --> T["Concrete Objectives and Automation Algeria"]
  O --> U["Planning & Execution & Planning & Arrangements"]
  P --> V["OBSERV"]
  Q --> W["OBSERV"]
  R --> X["OBSERV"]
  S --> Y["AGENTIC AI"]
  T --> Y
  U --> Y
  V --> Y
  W --> Y
  X --> Y
  Y --> Z["PLAN"]
  Y --> AA["IMPROVE"]
  Y --> AB["REVIEW"]
  Y --> AC["COMPRETIVE"]
  Y --> AD["EXECUTE"]
  Y --> AE["External Systems"]
```
</details>

Source: Kioxia

Exhibit 8: GPU direct storage  
![](images/9f8c21179d5e6b1b9ddea968ecfe2cc72e0030323352251f392c02eddca47053.jpg)

<details>
<summary>text_image</summary>

GPU Direct Storage
■ Expanding HBM capacity by GPU direct SSD access.
GPU Server
Direct GPU-to-SSD Access
GPU Direct Storage Server
Super High IOPS SSD
□ Designed to overcome HBM scalability and cost constraints
□ GPU-Driven IO
√ UP-5 200 MIPS/GPU
□ Small Chunk Data Access
✓ 9/2 Byte
✓ Low Latency
Best Suited Applications
Large-Scale Data for Graph Neural Networks
Accelerating Vector DB Indexing with GPU
Vector DB
</details>

Source: Kioxia

Exhibit 9: Expansion of inference AI server system  
![](images/431f0bad41ad2b747de06246d3443ffdca1d2c28ab22a4c9a9d059a722e079b6.jpg)

<details>
<summary>text_image</summary>

Expansion of Inference AI Server System - TOMORROW
Storage Server
Training & Inference Data
Context Memory
Storage Server
KV Cache
GPU Server
Leaming Snapshot
LLM Inference Cache
GPU Direct
Storage Server
New Use Case
RAG Server
Vector DB for RAG
</details>

Source: Kioxia

Exhibit 10: Key directions for SSD products  
![](images/7e09adc529af8ebab3176a9fb31b0a1009c5552cc9690c6060e4ddeddf718271.jpg)

<details>
<summary>text_image</summary>

3 Key Directions for SSD products
Super High IOPS
GPU Direct Storage
High Performance
High Capacity
Context Memory Storage
Cusing Controlled I/O/G/L Band SDD
Ultra High Capacity
■ Generative AI evolution has created and accelerated
3 direction for SSD.
Segment
Typical Usage
Super High IOPS
KIOXIA GP series
■ GPU Direct Storage
High Performance / High Capacity
KIOXIA CM series
■ Context Memory Storage
Ultra High Capacity
KIOXIA LC series
Training & Inference Data Storage
</details>

Source: Kioxia

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; 

[中间内容因长度限制已省略]

<td>NT$811.00</td></tr><tr><td>Gudeng Precision (3680.TWO)</td><td>O (11/25/2025)</td><td>NT$520.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$145.30</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$410.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$309.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb104.77</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$4,300.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb710.00</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$360.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb603.36</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb95.39</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,450.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb107.74</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$582.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.65</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,365.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$131.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$161.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$483.50</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$176.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb66.58</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$158.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb98.73</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb33.95</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$71.55</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb75.65</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$28.80</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb130.93</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb113.18</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb75.14</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb42.66</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb102.87</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,010.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,525.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$17,505.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$116.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb120.25</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb488.00</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$150.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$368.80</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb239.39</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$492.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$178.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$736.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$74.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$643.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb55.32</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$162.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$114.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$281.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb126.00</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb520.01</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,120.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$908.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$20.08</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$7,275.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,765.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$258.70</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,425.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

Tiffany Yeh

© 2026 MS
"""
