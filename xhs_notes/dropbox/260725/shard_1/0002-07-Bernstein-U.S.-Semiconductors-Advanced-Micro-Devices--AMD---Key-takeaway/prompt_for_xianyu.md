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
U.S. Semiconductors

# Advanced Micro Devices (AMD): Key takeaways from the Advancing AI Event

![](images/d59c934873a6ef0231143f0aaa494115d919f137a4c9ae17258ddbc53e4948f9.jpg)

Stacy A. Rasgon, Ph.D.

+1 213 559 5917

stacy.rasgon@bernsteinsg.com

![](images/624cf9e0c77a2c4e48cf1a69fcaa2f1b5d49f4498845605180a29169da3c286e.jpg)

Alrick Shaw

+1 917 344 8454

alrick.shaw@bernsteinsg.com

![](images/5ec0eae57677071b169db025ebff6d2543948e1a1a95b08d1afa3bf1898d9081.jpg)

Arpad von Nemes

+1 917 344 8461

arpad.vonnemes@bernsteinsg.com

![](images/1cabf128b51440aeff76a17e98a4a5d987b31d777a2a6a71e6c550562a497403.jpg)

Eva Zhang

+1 212 845 7839

eva.zhang@bernsteinsg.com

AMD held its Advancing AI event from July 22-23, culminating in a keynote by CEO Dr. Lisa Su and investor Q&A. We thought the event was generally quite positive with key announcements around new customer partnerships, updates on the product portfolio and roadmap, increased TAM outlooks. We summarize the main announcements below.

Helios (MI450) officially launched with (unsurprisingly) strong performance benchmarks, both vs. Vera Rubin and vs. MI350 (though as always with this sort of thing we take them with a grain of salt) (Exhibit 1, Exhibit 2). An updated Helios roadmap was also provided with an annual release cadence of successive rack-scale systems with MI500/MI600 series expected to launch in 2027 and 2028, respectively (Exhibit 3). The near-term MI455X ramp is still expected to start in 3Q and ramping into 4Q of this year.

AMD announced Anthropic as a third major customer for its Helios architecture, joining OpenAI and Meta. As part of the strategic partnership with Anthropic, AMD will invest up to \$5B (so no warrants) and the companies will collaborate on ROCm. Anthropic will deploy up to 2GW of compute, with deployment of the first $1^{st}$ GW starting in 1H27 with the goal of deploying almost the full 1GW in 2027. AMD also announced a partnership with Microsoft to deploy Helios at scale on Azure, although not providing specific targets.

CPU 2030 TAM raised to \$220B vs the prior \$120B they provided only 3 months ago (Exhibit 4), implying an >50% CAGR from \$26B in 2025, with the vast majority of growth driven by agentic AI. They also see the Accelerator TAM growing to \$1.4T by 2030 (\~45% CAGR from \$200B in 2025) mainly driven by inference spend with the overall compute TAM growing to \~\$2T (\~40% CAGR from \$365B in 2025).

Management provided color on its CPU product roadmap. AMD's CPU portfolio of next gen Venice CPUs addresses varying requirements via several Venice variants tailored to GPU servers / host nodes (Venice HF/Verano), Agentic CPU servers (high core count, high ASP Venice 256c) and general purpose CPU servers (Venice SP7/SP8/Venice-X) (Exhibit 5). Management remains confident that AMD's CPU portfolio is strong and believes that a favorable competitive position vs. both x86 and Arm-based CPUs will help them to gain further market share.

Cerebras and AMD announced a partnership for ultra-low latency inference. As inference workloads are becoming more heterogeneous with customer requirements varying widely across latency, throughput, token capacity, cost and scale, the AMD-Cerebras partnership seeks to combine the throughput from AMD Instinct GPUs, with ultra-fast token generation capabilities of Cerebras (Exhibit 6, Exhibit 7). This announcement is perhaps unsurprising given that NVDA is taking a similar (although likely more integrated) approach with Groq. While sparse on technical details, Cerebras plans to deploy the first joint solution in its own data center and making it available to customers initially via Cerebras Cloud in 2H26.

(continued on next page)

AMD introduced ROCm.AI, an AI-driven development platform that aims to speed up development and workload-specific GPU performance optimization and programming via AI (and which they seem to view as their answer to the NVIDIA CUDA moat; we shall see...) The solution draws on the core ROCm software stack of compilers, libraries and frameworks and has integrations with AI coding agents which can use expert skills to help generate code to optimize GPU performance (Exhibit 8).

AMD also announced a host of smaller offerings in Enterprise, Personal and Physical AI. AMD announced new products addressing several challenges in enterprise AI deployment including power & cooling, cost and ease of deployment for the enterprise with its Instinct 350P GPU which it positions as a cost-effective, easy-to-deploy solution for on-prem datacenters for non-frontier workloads. Other new products include personal AI compute solutions which can run model sizes from 24B to 200B parameters (Ryzen AI400, Ryzen AI Max) as well as a new developer-oriented platform (Gorgon Halo). Lastly, AMD introduced KRIA AI Robotics, a turnkey robotics developer platform.

Overall we found the event to be quite positive, and continue to see fundamental strength with the company benefitting from fundamental upside in both CPU and GPU trajectories. We rate AMD Outperform, \$600 PT.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">23 Jul 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>AMD (Advanced Micro)</td><td>O</td><td>USD</td><td>539.69</td><td>600.00</td><td>223.7%</td><td>USD</td><td>4.17</td><td>6.98</td><td>14.61</td><td>129.3</td><td>77.4</td><td>36.9</td></tr><tr><td>SPX</td><td></td><td></td><td>7,408.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

AMD (OP, \$600): Expectations remain high, but exposure to AI demand driving both a CPU and GPU story can provide substantial growth.

## DETAILS

EXHIBIT 1: AMD's benchmarks showed strong performance vs. Vera Rubin (although we typically take these sorts of things with a grain of salt)...

## AMD Helios Delivers The Most Powerful Rackscale AI Infrastructure

![](images/5c3a032739e669021a33e5930df95543596a52aa49c3a61fa0cf7016a2c2962c.jpg)  
Source: AMD

EXHIBIT 2: ... and vs. MI355, particularly in low-latency use cases

## Instinct MI455X Delivers Generational Increase In Inference Throughput

![](images/76ee224dbb6c8cc3a0f7de1ca6d1e7cfb417e1e5965d068be3e2b4d635b5e515.jpg)  
Source: AMD

EXHIBIT 3: AMD targets an annual release cadence for its rack-scale GPUs  
![](images/0eb92a71f326a75b5a3eb3129bdfd44d1e72d8e63ac687aaba56856dd9bfd96a.jpg)  
Source: AMD

EXHIBIT 4: AMD raised its CPU TAM to \$220B in 2030 from \$120B not too long ago  
![](images/adb5a133623d55d8f84758fa7e9ddcc20e536f8d72326fe3b630bff14701e28f.jpg)  
Source: AMD

EXHIBIT 5: AMD's latest generation Venice CPU will be offered in several variants catering to a GPU server, agentic and general purpose workloads

AMD EPYC

EPYC "Venice" The Best Server CPU Portfolio

GPU SERVERS "HOST NODE"

AGENT CPU SERVERS "SANBOXES"

GENERAL PURPOSE CPU SERVERS

"Venice" HF RDIMM / MRDIMM

"Venice" 256c

"Venice" SP7

"Venice" SP8

"Venice-X"

"Verano"
LPDDR

High Frequency CPU to GPU Bandwidth

High Core Count Low Power

High Performance High Density

Balanced Performance & Power

Technical Compute & HPC

Source: AMD

EXHIBIT 6: The AMD - Cerebras offering seeks to combine high-throughput with ultra-low latency...

## The Most Powerful Solution For Ultra Low Latency Inference

AMD INSTINCT

High-Throughput Scalable Engine

Wafer-scale, Ultra Low Latency Engine

432 GB HBM4 Capacity

23.3 TB/s Memory Bandwidth

44 GB on-chip SRAM

72 GPU Domain

21,000 TB/s Memory Bandwidth

900,000 AI Cores

Source: AMD

## EXHIBIT 7: ... offering higher TPS/W across a wide latency band

## AMD × cerebras Ultra-Fast Inference, Higher TPS/W on Leading AI Models

THROUGHPUT PER WATT (tokens/s/W)

Up to 5x TPS/kW

Helios + Cerebras

Cerebras

ULTRA LOW LATENCY
INTERACTIVITY (TOKENS / SECOND / USER) Kimi 2.6 1T Model

Source: AMD

EXHIBIT 8: ROCm.AI optimizes GPU performance across both training and inference workloads

## Accelerating Inference with ROCm.AI

Parallelization & Scheduling
Expert parallelism, DP-attention,
Compute communications overlap

RELEASE-TO-RELEASE IMPROVEMENT
INFERENCE

Memory Management
Paged attention, KV cache quantization,
Unified attention (prefill + decode)

3.3x

average performance improvement

Optimized Kernels
MHA prefill, MLA decode, Block-scale fused MoE

DeepSeek-R1 GLM-5 Kimi-K2.5 ROCm.AI vs ROCm 7

Source: AMD

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 9: Bernstein AMD Income Statement

<table><tr><td colspan="17">AMD: Income Statement ($M)</td></tr><tr><td>AMD (Calendar)</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>Q125</td><td>Q225</td><td>Q325</td><td>Q425</td><td>Q126</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td></tr><tr><td>Revenue</td><td>$ 34,639.0</td><td>$ 47,943.8</td><td>$ 82,189.4</td><td>$ 107,210.2</td><td>$ 7,438.0</td><td>$ 7,685.0</td><td>$ 9,246.0</td><td>$ 10,270.0</td><td>$ 10,253.0</td><td>$ 11,233.0</td><td>$ 11,730.2</td><td>$ 14,727.6</td><td>$ 18,885.3</td><td>$ 19,670.5</td><td>$ 21,401.8</td><td>$ 22,231.9</td></tr><tr><td>COGS</td><td>$ 17,487.0</td><td>$ 22,226.3</td><td>$ 37,857.5</td><td>$ 47,901.1</td><td>$ 3,702.0</td><td>$ 4,626.0</td><td>$ 4,466.0</td><td>$ 4,693.0</td><td>$ 4,837.0</td><td>$ 5,162.3</td><td>$ 5,379.5</td><td>$ 6,847.5</td><td>$ 8,806.5</td><td>$ 9,077.4</td><td>$ 9,851.3</td><td>$ 10,222.4</td></tr><tr><td>Gross Profit</td><td>$ 17,152.0</td><td>$ 25,717.4</td><td>$ 44,231.9</td><td>$ 59,309.1</td><td>$ 3,736.0</td><td>$ 3,029.0</td><td>$ 4,786.0</td><td>$ 5,577.0</td><td>$ 5,416.0</td><td>$ 6,070.7</td><td>$ 6,350.8</td><td>$ 7,880.0</td><td>$ 10,078.8</td><td>$ 10,583.1</td><td>$ 11,505.0</td><td>$ 12,009.3</td></tr><tr><td>R&amp;D</td><td>$ 8,091.0</td><td>$ 10,447.0</td><td>$ 12,200.0</td><td>$ 13,700.0</td><td>$ 1,728.0</td><td>$ 1,894.0</td><td>$ 2,139.0</td><td>$ 2,330.0</td><td>$ 2,397.0</td><td>$ 2,550.0</td><td>$ 2,700.0</td><td>$ 2,800.0</td><td>$ 2,900.0</td><td>$ 3,000.0</td><td>$ 3,100.0</td><td>$ 3,200.0</td></tr><tr><td>SG&amp;A</td><td>$ 4,144.0</td><td>$ 5,053.0</td><td>$ 5,700.0</td><td>$ 6,150.0</td><td>$ 886.0</td><td>$ 991.0</td><td>$ 1,069.0</td><td>$ 1,198.0</td><td>$ 1,253.0</td><td>$ 1,250.0</td><td>$ 1,250.0</td><td>$ 1,300.0</td><td>$ 1,350.0</td><td>$ 1,400.0</td><td>$ 1,450.0</td><td>$ 1,500.0</td></tr><tr><td>Amortization of Intangibles</td><td>$ 1,223.0</td><td>$ 1,160.0</td><td>$ 1,160.0</td><td>$ 1,160.0</td><td>$ 316.0</td><td>$ 308.0</td><td>$ 302.0</td><td>$ 297.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td></tr><tr><td>Licensing (Gain)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other Operating Expense/(Income)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total GAAP Operating Expenses</td><td>$ 13,458.0</td><td>$ 16,660.0</td><td>$ 19,060.0</td><td>$ 21,010.0</td><td>$ 2,930.0</td><td>$ 3,193.0</td><td>$ 3,510.0</td><td>$ 3,825.0</td><td>$ 3,940.0</td><td>$ 4,090.0</td><td>$ 4,240.0</td><td>$ 4,390.0</td><td>$ 4,540.0</td><td>$ 4,690.0</td><td>$ 4,840.0</td><td>$ 4,990.0</td></tr><tr><td>Total Pro-Forma Operating Expenses</td><td>$ 10,397.0</td><td>$ 13,495.0</td><td>$ 15,700.0</td><td>$ 17,450.0</td><td>$ 2,213.0</td><td>$ 2,429.0</td><td>$ 2,754.0</td><td>$ 3,001.0</td><td>$ 3,145.0</td><td>$ 3,300.0</td><td>$ 3,450.0</td><td>$ 3,600.0</td><td>$ 3,700.0</td><td>$ 3,850.0</td><td>$ 4,000.0</td><td>$ 4,150.0</td></tr><tr><td>Operating Income</td><td>$ 3,694.0</td><td>$ 9,057.4</td><td>$ 25,171.9</td><td>$ 38,299.1</td><td>$ 806.0</td><td>$ (134.0)</td><td>$ 1,270.0</td><td>$ 1,752.0</td><td>$ 1,476.0</td><td>$ 1,980.7</td><td>$ 2,110.8</td><td>$ 3,490.0</td><td>$ 5,538.8</td><td>$ 5,903.1</td><td>$ 6,710.5</td><td>$ 7,019.5</td></tr><tr><td>Net Interest Income (Loss)</td><td>$ 6.0</td><td>$ (44.0)</td><td>$ 60.0</td><td>$ 60.0</td><td>$ 19.0</td><td>$ 60.0</td><td>$ (37.0)</td><td>$ (36.0)</td><td>$ (37.0)</td><td>$ (37.0)</td><td>$ 15.0</td><td>$ 15.0</td><td>$ 15.0</td><td>$ 15.0</td><td>$ 15.0</td><td>$ 15.0</td></tr><tr><td>Other Non-operating Income (Loss)</td><td>$ 440.0</td><td>$ 262.0</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ 82.0</td><td>$ 358.0</td><td>$ 165.0</td><td>$ 97.0</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td></tr><tr><td>EBT before equity investment</td><td>$ 4,140.0</td><td>$ 9,275.4</td><td>$ 25,231.9</td><td>$ 38,359.1</td><td>$ 825.0</td><td>$ (74.0)</td><td>$ 1,315.0</td><td>$ 2,074.0</td><td>$ 1,604.0</td><td>$ 2,040.7</td><td>$ 2,125.8</td><td>$ 3,505.0</td><td>$ 5,553.8</td><td>$ 5,918.1</td><td>$ 6,725.5</td><td>$ 7,034.5</td></tr><tr><td>Equity in net income (loss) of investee</td><td>$ 15.0</td><td>$ 6.0</td><td>$ -</td><td>$ -</td><td>$ 7.0</td><td>$ 8.0</td><td>$ -</td><td>$ -</td><td>$ 6.0</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td><td>$ -</td></tr><tr><td>Income Before Taxes</td><td>$ 4,155.0</td><td>$ 9,281.4</td><td>$ 25,231.9</td><td>$ 38,359.1</td><td>$ 832.0</td><td>$ (66.0)</td><td>$ 1,315.0</td><td>$ 2,074.0</td><td>$ 1,610.0</td><td>$ 2,040.7</td><td>$ 2,125.8</td><td>$ 3,505.0</td><td>$ 5,553.8</td><td>$ 5,918.1</td><td>$ 6,725.5</td><td>$ 7,034.5</td></tr><tr><td>Provision for Income Taxes</td><td>$ (103.0)</td><td>$ 1,235.3</td><td>$ 3,280.2</td><td>$ 4,986.7</td><td>$ 123.0</td><td>$ (834.0)</td><td>$ 153.0</td><td>$ 455.0</td><td>$ 238.0</td><td>$ 265.3</td><td>$ 276.4</td><td>$ 455.7</td><td>$ 722.0</td><td>$ 769.4</td><td>$ 874.3</td><td>$ 914.5</td></tr><tr><td>Equity in income (loss) of ATMP JV</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>GAAP Net Income</td><td>$ 4,258.0</td><td>$ 8,046.2</td><td>$ 21,951.8</td><td>$ 33,372.4</td><td>$ 709.0</td><td>$ 872.0</td><td>$ 1,243.0</td><td>$ 1,511.0</td><td>$ 1,383.0</td><td>$ 1,775.4</td><td>$ 1,849.4</td><td>$ 3,049.4</td><td>$ 4,831.8</td><td>$ 5,148.8</td><td>$ 5,851.2</td><td>$ 6,120.0</td></tr><tr><td>Pro Forma Reconciliation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>+Amortization of Intangibles</td><td>$ 1,223.0</td><td>$ 1,160.0</td><td>$ 1,160.0</td><td>$ 1,160.0</td><td>$ 316.0</td><td>$ 308.0</td><td>$ 302.0</td><td>$ 297.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 289.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td><td>$ 290.0</td></tr><tr><td>Share Based Compensation</td><td>$ 1,612.0</td><td>$ 1,979.0</td><td>$ 2,200.0</td><td>$ 2,400.0</td><td>$ 359.0</td><td>$ 363.0</td><td>$ 412.0</td><td>$ 478.0</td><td>$ 479.0</td><td>$ 500.0</td><td>$ 500.0</td><td>$ 500.0</td><td>$ 550.0</td><td>$ 550.0</td><td>$ 550.0</td><td>$ 550.0</td></tr><tr><td>Other Adjustments</td><td>$ (339.0)</td><td>$ 392.2</td><td>$ 346.2</td><td>$ 320.2</td><td>$ 182.0</td><td>$ (762.0)</td><td>$ 8.0</td><td>$ 233.0</td><td>$ 113.0</td><td>$ 93.1</td><td>$ 93.1</td><

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
