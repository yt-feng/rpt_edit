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
# JPM

## Server

JPM proprietary server CPU shipment model

In this note, we introduce a JPM proprietary server CPU shipment model and forecast total server CPU shipments to grow from 26mn units in 2025 to 68mn by 2028 (38% CAGR). We segment server CPU demand into three buckets: (1) AI headnode CPUs, (2) agentic-AI server CPUs, and (3) general-purpose server CPUs. With AI accelerator shipments projected to show a \~50% CAGR over FY25–28 based on our CoWoS estimates by the semi team (link), we see a step-function increase in AI headnode CPU demand, reinforced by a rising CPU-to-accelerator attachment trend. While general-purpose server CPUs should continue to show a steady \~5% CAGR, agentic-AI CPUs are the breakout growth vector, with 155% CAGR expected over 2025–28. Net-net, we believe overall general server shipments can sustain 20%+ growth in the coming years. This super-cycle is positive for TSMC, Unimicron, ASPEED, Lotes, Wiwynn, Tripod, GUC, ASE, and memory vendors, such as SK Hynix and Samsung Electronics, across Asia Technology.

\- Server CPU landscape reshaped by AI-led demand. We forecast AI accelerator shipments to rise from 7.6mn units in 2024 to 32.5mn by 2028, with increasing headnode CPU attach rates due to more complex AI accelerators. The accelerator-to-CPU ratio is also compressing—from \~4:1 in legacy HGX servers to \~2:1 in NVL72 compute trays, and potentially \~1:1 in next-generation TPU designs. ARM-based CPUs are taking share, driven by Nvidia's Vera and Google's Axion, and we estimate ARM could represent \~90% of AI headnode CPU demand by 2028. We also expect ARM to gain share in agentic-AI servers, as hyperscalers lean into in-house CPU roadmaps for emerging workloads. As a result, we model ARM-based CPUs reaching \~43% of the blended server CPU market by 2028 (up from \~22% in 2025). That said, we still expect the x86 CPU market to see an accelerated 25% CAGR over the period (vs. flattish to LSD CAGR in the prior cycle).

\- New AI inference orchestration drives agentic-AI server demand. As AI workloads shift from training towards inference, we expect hyperscalers to deploy more general-purpose servers around accelerators to improve Total Cost of Ownership (TCO). The incremental demand shows up primarily in external storage servers (e.g., KV cache) and compute servers that handle query orchestration around GPUs. While there is no fixed accelerator-to-CPU server ratio, our back-of-the-envelope analysis suggests \~0.5x (1 CPU for two accelerators) this year, with the ratio rising over time as accelerator complexity increases. This will become the key incremental driver of general server demand (>50% of the general server CPU market by 2028 vs. <10% last year).

\- Stocks leveraged to the super server CPU upcycle. There is a high correlation between server CPU, BMC, substrate, and socket demand. We expect ASPEED, Lotes, and Unimicron to be the key beneficiaries of this super server CPU cycle, driven by strong unit demand, continued content upgrades, and potential product price hikes. AMD's continued m/s gain in x86 server CPUs also bodes well for TSMC and ASE as the key foundry/OSAT vendor. DRAM vendors could benefit from the increasing DIMM/SOCAMM demand. In the downstream, we believe the server PCB makers (e.g. Tripod) and general server ODMs (e.g. Wiwynn, Inventec) could also benefit from the strong server demand.

See page 9 for analyst certification and important disclosures, including non-US analyst disclosures.

## Technology - Hardware

Albert Hung AC
(886-2) 2725-9875
albert.hung@jpmchase.com
JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Gokul Hariharan AC
(852) 2800-8564
gokul.hariharan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Anthony Leng
(886-2) 2725-9240
anthony.leng@JPM.com
JPM Securities (Taiwan) Limited

Jennifer Hsieh
(886-2) 2725-9868
jennifer.hsieh@JPM.com
JPM Securities (Taiwan) Limited

## Table Of Contents

Accelerating server CPU growth cycle on AI inference cycle 3
Top-down methodology.... 3
Strong accelerator demand + Rising CPU attach rate = Exponential AI server headnode CPU growth.... 4
Agentic AI CPUs becoming a new driver for server CPU demand.... 5
Triangulating top-down forecasts with bottom-up estimates.... 7
Faster ramp of Arm-based CPUs driven by rising Arm-based CPU attach rate.... 7

# Accelerating server CPU growth cycle on AI inference cycle

We introduce our proprietary server CPU demand model. We segment CPU demand into three buckets—(1) AI server headnode CPUs, (2) regular server CPUs, and (3) agentic-AI CPUs—and forecast total server CPU shipments to grow from 26mn units in 2025 to 68mn by 2028 (38% CAGR). As AI applications transition from training toward inference, we expect agentic-AI and AI headnode CPU demand to drive a “super” general server CPU cycle.

We also size the server CPU TAM by combining our shipment forecast with ASP assumptions across the three sub-segments. Given ongoing supply tightness and continued CPU upgrade cycles, we assume \~10% annual CPU price increases. As a result, we forecast server CPU TAM to show a 53% CAGR over 2025–28, reaching \~US\$100bn by 2028, driven by both volume growth and sustained ASP expansion.

Figure 1: Server CPU shipment trend and CAGR  
![](images/6daa82b23fb440e837aa8b09eb858a3dc26776372cebe3ba13822ff0c5656677.jpg)  
Source: JPM estimates.Gartner®.

Figure 2: Server CPU revenue TAM forecast and CAGR  
![](images/ee995ae482a8b769d61e153d5f7ffd7fcd56c3c1382948d36ffca87939a8c38e.jpg)  
Source: Gartner®. JPM estimates.

## Top-down methodology

We have anchored the total server CPU shipments for 2024 using Gartner data and forecast the server CPU demand for the respective segments over the coming years. We forecast AI server headnode CPU demand based on our AI accelerator forecast by the JPM semi team (link) (led by Gokul Hariharan) and the ratio of AI accelerators to headnode CPUs per server node. We assume no agentic AI activity in 2024 and derive the implied regular server CPU demand for 2024.

For the year 2025 and 2026, we assume non-AI server headnode CPU shipments (regular servers plus agentic AI CPUs) grow at 11%/30% YoY to 23mn/29mn, up from 20mn in 2024. This, coupled with 3mn/7mn of AI server headnode demand, could lead to 26mn/36mn total server CPU shipments (up 16%/42% YoY) in 2025/2026.

Beyond 2026, we anticipate 42%/32% YoY growth in total server CPU shipments, driven by rising attach rates of agentic AI CPUs relative to AI accelerators, strong AI server demand, and a 5% CAGR in regular server CPUs. Overall, we forecast a 38% CAGR in server CPU shipments through 2025-2028.

Table 1: Server CPU forecast - top-down methodology

<table><tr><td>Unit in millions</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2025-28 CAGR</td></tr><tr><td colspan="7">1. AI SERVER HEADNODE</td></tr><tr><td>Global AI accelerator Shipments (mn)</td><td>7.6</td><td>9.6</td><td>16.1</td><td>25.2</td><td>32.5</td><td>50%</td></tr><tr><td>YoY</td><td></td><td>27%</td><td>67%</td><td>56%</td><td>29%</td><td></td></tr><tr><td>Avg accelerators per CPU in headnodes</td><td>4.1</td><td>3.0</td><td>2.3</td><td>2.2</td><td>1.9</td><td></td></tr><tr><td>Headnode Server CPUs Needed (mn)</td><td>1.8</td><td>3.2</td><td>7.1</td><td>11.3</td><td>16.8</td><td>74%</td></tr><tr><td>YoY</td><td></td><td>73%</td><td>124%</td><td>59%</td><td>48%</td><td></td></tr><tr><td colspan="7">2. REGULAR SERVER GROWTH (non AI workloads)</td></tr><tr><td>Traditional server unit for non AI workload (mn)</td><td>11.6</td><td>11.9</td><td>12.5</td><td>13.1</td><td>13.8</td><td></td></tr><tr><td>YoY</td><td>2%</td><td>3%</td><td>5%</td><td>5%</td><td>5%</td><td></td></tr><tr><td>CPU per server</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td></td></tr><tr><td>non AI workload CPU (mn)</td><td>20.3</td><td>20.9</td><td>21.9</td><td>23.0</td><td>24.2</td><td>5%</td></tr><tr><td>YoY</td><td></td><td>3%</td><td>5%</td><td>5%</td><td>5%</td><td></td></tr><tr><td colspan="7">3. AGENTIC AI CPU CLUSTERS</td></tr><tr><td>CPU per accelerator ratio</td><td>0.0</td><td>0.17</td><td>0.45</td><td>0.68</td><td>0.83</td><td></td></tr><tr><td>TOTAL AGENTIC AI CPUs (mn)</td><td>0.0</td><td>1.6</td><td>7.3</td><td>17.1</td><td>27.0</td><td>155%</td></tr><tr><td>YoY</td><td></td><td></td><td>352%</td><td>134%</td><td>58%</td><td></td></tr><tr><td colspan="7">Total server CPU shipment (mn)</td></tr><tr><td>Total server CPU shipment</td><td>22.1</td><td>25.7</td><td>36.3</td><td>51.4</td><td>67.9</td><td>38%</td></tr><tr><td>YoY</td><td></td><td>16%</td><td>42%</td><td>42%</td><td>32%</td><td></td></tr><tr><td>Total server CPU shipment excl. AI server headnodes serve</td><td>20.3</td><td>22.5</td><td>29.2</td><td>40.1</td><td>51.1</td><td>31%</td></tr><tr><td>YoY</td><td></td><td>11%</td><td>30%</td><td>37%</td><td>27%</td><td></td></tr></table>

Source: JPM estimates. Gartner®data for 2024 total server CPU shipments. Global AI accelerator shipments are based on our CoWoS estimates by the semi team (link).

## Strong accelerator demand + Rising CPU attach rate = Exponential AI server headnode CPU growth

We have seen a rising attach rate of AI server headnode CPUs. The number of AI accelerators per CPU in each AI server decreases from 4:1 to 2:1 and even 1:1 in the future generations, especially in AI ASIC servers. We attribute this to the rising requirement of CPU orchestration in AI servers due to the increasing complexity of AI server architectures. Of note, the AI accelerator forecasts are based on the CoWoS estimates by the JPM semi team (link) (led by Gokul Hariharan).

\- Nvidia GPU servers: Accelerator to CPU ratio declines to 2:1 in NVL72 compute trays from 4:1 in HGX servers. We also see CPU demand in the NVLink switch tray of the NVL72 server rack. Interestingly, we see an increase in the accelerator to CPU ratio in the HGX servers in future generations (from 4:1 to 8:1), likely due to the relatively lower CPU requirements of the HGX server architecture.

\- AMD GPU servers: Our research indicates 4:1 GPU to CPU ratios in the MI300 series and AMD MI455 Helio servers.

\- Google TPU servers: Our research indicates that there are two designs for TPU v8 servers with 1:1 and 2:1 TPU-to-CPU ratios, and that there could be a 1:1 for future generations. We assume a 50%/50% mix for 1:1 and 2:1 design for TPU v8 generation.

\- AWS Trainium servers: Our research indicates that the Trainium to CPU ratio will decline to 4:1 for the T3 liquid cooling project from 16:1 for the T2 and air-cooled T3 projects.

\- MSFT/Meta/other AI ASIC servers: We assume 4:1 accelerators to CPU ratio for the rest of the AI ASIC servers.

The rising attach rate of AI server headnode CPUs, combined with strong AI accelerator demand, could drive exponential growth of AI server headnode CPU demand. Overall, we forecast AI server headnode CPU to grow at a $\sim 74\%$ CAGR in 2025-2028.

Table 2: AI server headnode CPU forecast

<table><tr><td>AI accelerator unit (mn)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>Note</td></tr><tr><td>NVDA</td><td>4.5</td><td>6.2</td><td>8.9</td><td>10.0</td><td>11.6</td><td></td></tr><tr><td>HGX (x86 base)</td><td>4.3</td><td>2.6</td><td>3.0</td><td>2.1</td><td>2.0</td><td></td></tr><tr><td>NVL72 (ARM base)</td><td>0.1</td><td>3.6</td><td>5.9</td><td>7.9</td><td>9.6</td><td></td></tr><tr><td>AMD</td><td>0.5</td><td>0.7</td><td>0.7</td><td>1.5</td><td>2.3</td><td></td></tr><tr><td>TPU</td><td>1.7</td><td>1.8</td><td>4.4</td><td>8.9</td><td>11.6</td><td></td></tr><tr><td>v4/5/6/7</td><td>1.7</td><td>1.7</td><td>2.7</td><td>1.7</td><td>-</td><td></td></tr><tr><td>v8</td><td>-</td><td>0.1</td><td>1.7</td><td>7.2</td><td>8.6</td><td></td></tr><tr><td>v9</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3.0</td><td></td></tr><tr><td>AWS</td><td>0.8</td><td>1.5</td><td>1.9</td><td>3.5</td><td>3.5</td><td></td></tr><tr><td>Inferentia 2</td><td>0.5</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>Trn 2</td><td>0.3</td><td>1.5</td><td>0.6</td><td>-</td><td>-</td><td></td></tr><tr><td>Trn 3</td><td>-</td><td>-</td><td>1.3</td><td>3.5</td><td>-</td><td></td></tr><tr><td>Trn 4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3.5</td><td></td></tr><tr><td>Meta</td><td>-</td><td>-</td><td>0.3</td><td>0.5</td><td>1.1</td><td></td></tr><tr><td>Microsoft</td><td>-</td><td>-</td><td>0.2</td><td>0.8</td><td>0.8</td><td></td></tr><tr><td>Others</td><td></td><td></td><td>0.2</td><td>0.4</td><td>0.8</td><td></td></tr><tr><td>Total AI accelerator units (mn)</td><td>7.4</td><td>10.1</td><td>16.5</td><td>25.6</td><td>31.7</td><td></td></tr><tr><td>Avg number of accelerators per CPU</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td></td></tr><tr><td>NVDA</td><td>3.9</td><td>2.5</td><td>2.4</td><td>2.4</td><td>2.3</td><td>8 GPU to 2 CPU</td></tr><tr><td>HGX (x86 base)</td><td>4.0</td><td>4.0</td><td>4.0</td><td>8.0</td><td>8.0</td><td>2 GPU to 1 CPU; R200 changed to 8:1 GPU/CPU ratio</td></tr><tr><td>NVL72 (ARM base)</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td></td></tr><tr><td>AMD</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td></td></tr><tr><td>TPU</td><td>4.0</td><td>3.8</td><td>1.5</td><td>1.5</td><td>1.3</td><td></td></tr><tr><td>v4/5/6/7</td><td>4.0</td><td>4.0</td><td>1.5</td><td>1.5</td><td>1.5</td><td>Assume v4/v5 4:1 &amp; v6/7 2:1</td></tr><tr><td>v8</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>v8 has two versions, 1:1 or 2:1</td></tr><tr><td>v9</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td></td></tr><tr><td>AWS</td><td>5.3</td><td>14.5</td><td>14.3</td><td>10.0</td><td>2.0</td><td>Assume average 8 Inferentia to 2 CPUs</td></tr><tr><td>Inferentia 2</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td></td></tr><tr><td>Trn 2</td><td>16.0</td><td>16.0</td><td>16.0</td><td>16.0</td><td>16.0</td><td></td></tr><tr><td>Trn 3</td><td>13.6</td><td>13.6</td><td>13.6</td><td>10.0</td><td>6.4</td><td rowspan="2">80% air cooling (16:1) and 20% liquid cooling (4:1), 50%/50% and 20%/80% AC/LC ratio in 2027/28 JPMe</td></tr><tr><td>Trn 4</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td>Meta</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td></td></tr><tr><td>Microsoft</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td></td></tr><tr><td>Others</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td></td></tr><tr><td>Blended ratio</td><td>4.0</td><td>3.2</td><td>2.3</td><td>2.3</td><td>1.9</td><td></td></tr><tr><td>AI headnode CPU units (mn)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td></td></tr><tr><td>NVDA</td><td>1.1</td><td>2.4</td><td>3.7</td><td>4.2</td><td>5.1</td><td></td></tr><tr><td>AMD</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.4</td><td>0.6</td><td></td></tr><tr><td>TPU</td><td>0.4</td><td>0.5</td><td>2.9</td><td>5.9</td><td>8.7</td><td></td></tr><tr><td>AWS</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.4</td><td>1.7</td><td></td></tr><tr><td>Meta</td><td>-</td><td>-</td><td>0.1</td><td>0.1</td><td>0.3</td><td></td></tr><tr><td>Microsoft</td><td>-</td><td>-</td><td>0.1</td><td>0.2</td><td>0.2</td><td></td></tr><tr><td>Others</td><td>-</td><td>-</td><td>0.1</td><td>0.1</td><td>0.2</td><td></td></tr><tr><td>Total</td><td>1.8</td><td>3.2</td><td>7.1</td><td>11.3</td><td>16.8</td><td></td></tr></table>

Source: JPM estimates. AI accelerator unit estimates are based on our CoWoS estimates by the semi team (link).

## Agentic AI CPUs becoming a new driver for server CPU demand

As we migrate towards the era of agentic AI, focusing on test-time scaling (i.e. long thinking), CPUs are playing an increasingly important role in orchestration, running tools and skills, storage, and security. For example, the Vera CPU not only sits in the NVL72 rack systems, but also serves as a standalone CPU across the entire Vera Rubin platform, including storage servers and CPU servers.

Figure 3: Stages of Intelligence  
![](images/524e116c16004864fa1fe131c0fe75b8ad6504227b08c4c7a5b393941cc00765.jpg)  
Source: Nvidia.

Figure 4: Agent = LLM + Harness; CPU plays a critical role in the agentic AI ecosystem  
![](images/1480a5d8c68bb61d6fb0579b97e7666416ca1acd7644888f4cd773caf75b7cd4.jpg)  
Source: Nvidia.

We attribute the strong general server demand this year (30-40% YoY growth on our estimates) primarily to the emerging demand for agentic AI. To quantify agentic AI demand, we assume no agentic AI activity in 2023/2024 and calculate the implied ratio of agentic AI CPUs to AI accelerators in 2025 and 2026. We then forecast the agentic AI CPU demand based on our estimates of this ratio and AI accelerator demand for 2027/2028.

To derive the implied ratio of agentic AI CPU demand to AI accelerator demand, we assume a $\sim 3\%$ CAGR for the regular server demand in 2023-2026 and derive the agentic AI CPU demand for 2025/2026 after subtracting the AI server headnode CPU and regular server CPU demand from our total server CPU demand. We expect this ratio to rapidly increase in the coming years given the fast-growing agentic AI demand.

Overall, we forecast agentic AI CPU demand to show a 155% CAGR during 2025-2028, which we view as the key growth driver of total server CPU demand.

## Triangulating top-down forecasts with bottom-up estimates

In the analysis below, we triangulate our top-down forecasts with bottom-up estimates. We anchor 2024 and 2025 Intel/AMD server CPU shipments to Gartner data. For 2025–28, we forecast x86/Arm server CPU shipments at 25%/72% CAGR, respectively. We estimate CPU demand for the remaining ASIC CPU vendors based on our industry research and our AI server headnode CPU demand framework.

Table 3: JPM server CPU bottom up estimates

<table><tr><td>Bottom up CPU unit breakdown</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2025-28 CAGR</td></tr><tr><td>x86</td><td>20.6</td><td>19.9</td><td>25.8</td><td>33.2</td><td>38.8</td><td>25%</td></tr><tr><td>ARM</td><td>1.5</td><td>5.8</td><td>10.5</td><td>18.2</td><td>29.1</td><td>72%</td></tr><tr><td>Total</td><td>22.1</td><td>25.7</td><td>36.3</td><td>51.4</td><td>67.9</td><td>38%</td></tr><tr><td>% x86</td><td>93%</td><td>78%</td><td>71%</td><td>65%</td><td>57%</td><td></td></tr><tr><td>% ARM</td><td>7%</td><td>22%</td><td>2

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
