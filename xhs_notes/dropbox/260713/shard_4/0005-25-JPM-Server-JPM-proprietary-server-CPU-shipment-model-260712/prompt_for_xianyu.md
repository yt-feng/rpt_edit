你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

As we mi

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
