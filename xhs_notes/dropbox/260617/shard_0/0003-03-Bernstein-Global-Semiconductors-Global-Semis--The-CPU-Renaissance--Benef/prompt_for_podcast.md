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
## Global Semiconductors

# Global Semis: The CPU Renaissance? Beneficiaries of a \$223bn TAM...

![](images/c15715ec8e7725297e11b775fe31986ecfbcac262506fbb1829a534278cb7d2b.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/f48d98cd7df38dde88ba377a4e34228dce716523af699cc83d05450dea28a8b9.jpg)

Stacy A. Rasgon, Ph.D.

+1 213 559 5917

stacy.rasgon@bernsteinsg.com

![](images/cc172ff0a28fa6c488b3565f2c30d4a4a8c054b438782c1bea510edf4460bcfc.jpg)

Qingyuan Lin, Ph.D.

+852 2123 2654

qingyuan.lin@bernsteinsg.com

![](images/90d1524aa4ab5108828e2fdafaeb91d4879a738fead769f6442881261e08b4d3.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/af230e66cbbb16cf0271b8c30234566bdbdf831e7fb4fef1df63745d2c26cffa.jpg)

Juho Hwang

+852 2123 2632

juho.hwang@bernsteinsg.com

![](images/78d976dccf9438bc3ac40a0c3373da6538ad7ae862b7819e82e01d458eb1eb0c.jpg)

Jack Lin

+852 2123 2683

jack.lin@bernsteinsg.com

![](images/7183edd2bde0465ae1406e8a09ccea8697c91d4e7c46e2fd513f585dce0ad11a.jpg)

Carmine Milano, CFA

+44 20 7762 1857

carmine.milano@bernsteinsg.com

![](images/98dd8b4d1ef5189aef7d9c8d255c02505c3bc407ea6d240a6336141bbf45682e.jpg)

Alrick Shaw

+1 917 344 8454

alrick.shaw@bernsteinsg.com

![](images/86f7e0edb60c3f016bb93d104e0a5721e42b074a2d76f4320a5a7a3f8877827f.jpg)

Arpad von Nemes

+1 917 344 8461

arpad.vonnemes@bernsteinsg.com

![](images/7999bdf232fe65a11876b02b6bf3c4f902c666697797e401c14c3e06b568fb68.jpg)

Francis Ma

+852 2123 2626

francis.ma@bernsteinsg.com

The shift from gen AI paradigm from 1.0 (chatbot) to 2.0 (agent) greatly increases server CPU demand. As discussed in SoftBank, Arm: From GenAI to Agentic AI; Initiating with Outperform Ratings, Agentic AI involves heavily autonomous task orchestration and execution, which boosts the CPU workload vs. GPU. With the shift from chatbot to agentic AI, the CPU:GPU ratio for AI data center is surging from 1:4 or 1:8 to 1:1 or higher.

We raise server CPU TAM to \$223bn (\$137bn in 2030 in the base case, 6x of the 2025 TAM of \$37bn. This assumes \$3.5tn of AI data center capex, and 1:1 CPU:GPU pairing ratio for inference. An alternative approach with 120mn CPU cores/GW yields similar TAM. Our previous forecast of \$137bn is now the bear case (assuming \$3tn AI capex, 1:2 CPU:GPU), while the upside now sits at \$330bn (\$4tn AI capex, 1.5:1 CPU:GPU).

Raising Arm PT to \$500, as Arm is the structural beneficiary of the renaissance of CPUs for agentic AI. Arm architecture is suitable for agentic AI workload given its unparalleled power efficiency. In addition, Arm is shifting from just IP provider to CPU maker, aiming to capture \$15bn revenue by CY2030, but we now forecast \$22bn as we revise CPU TAM to \$223bn in 2030 (from \$137bn). Arm's 2030 EPS (FYE31) is now lifted to \$11.79 (\$9.83 prior). Based on 42x P/E (40x prior), we lift Arm's PT to \$500 (21% upside). Given the lifted PT of Arm, we also raise SoftBank PT to ¥11,200 (58% upside), based on 30% discount to pro-forma NAV of \$572bn.

Updating numbers, raising AMD and INTC PTs. Both companies should benefit from stronger (and more sustained) server demand, though AMD's products remain superior for now (and we believe they will continue their share gain trajectory). Our existing AMD model was already consistent with a stronger server CPU environment and estimates move marginally, however we are now bringing our INTC model inline with those assumptions and are raising estimates more materially; we also roll valuation horizon forward for both to CY27/28 avg (vs CY27 prior) given we are about halfway through the year. Our AMD PT moves to \$600; INTC to \$100. We rate AMD OP, INTC MP.

Hygon will benefit from strong x86 CPU demand and gain share in China. We expect China to outpace global x86 growth from 2028 onward, with the easing of advanced-node supply constraints in China and accelerating AI investment unlocking CPU potential. We expect Hygon to steadily expand its share of China's x86 server CPU market, exceeding $35\%$ by 2030, as it increasingly penetrates into CSPs, beyond its traditional customer base of government and SOEs, supported by improved interoperability with domestic AI chips and potentially constrained supply from global vendors. We updated Hygon projection to reflect that, revising up 2027/2028 EPS to CNY 3.6 / 6.3, raising PT to CNY 450.

What could go wrong? We're still assessing if foundry/memory capacity will be sufficient to support the CPU growth. Additionally, the value of GPU/accelerator embeds the value of HBM & the markup charged by NVDA, etc. now but the high cost of memory including HBM may prompt hyperscalers to source directly from memory suppliers. Our projection is based on CPU/accelerator value & will have a downside risk if that happens.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">15 Jun 2026</td><td colspan="2">TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>ARM (ARM Holdings)</td><td>O</td><td>USD</td><td>412.55</td><td>500.00</td><td>160.6%</td><td>USD</td><td>1.77</td><td>2.25</td><td>3.21</td><td>233.1</td><td>183.3</td><td>128.6</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>300.00</td><td></td><td></td><td></td><td>2.28</td><td>3.12</td><td></td><td></td><td></td><td></td></tr><tr><td>9984.JP (SoftBank)</td><td>O</td><td>JPY</td><td>7,102.00</td><td>11,200</td><td>180.6%</td><td>JPY</td><td>872.47</td><td>282.49</td><td>159.10</td><td>8.1</td><td>25.1</td><td>44.6</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>8,200.00</td><td></td><td></td><td></td><td>251.35</td><td>152.44</td><td></td><td></td><td></td><td></td></tr><tr><td>688041.CH (Hygon)</td><td>O</td><td>CNY</td><td>294.31</td><td>450.00</td><td>72.0%</td><td>CNY</td><td>1.10</td><td>2.04</td><td>3.59</td><td>267.6</td><td>144.0</td><td>81.9</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>280.00</td><td></td><td></td><td></td><td>2.42</td><td>3.48</td><td></td><td></td><td></td><td></td></tr><tr><td>AMD (Advanced Micro)</td><td>O</td><td>USD</td><td>547.26</td><td>600.00</td><td>290.9%</td><td>USD</td><td>4.17</td><td>6.98</td><td>14.61</td><td>131.1</td><td>78.5</td><td>37.4</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>525.00</td><td></td><td></td><td></td><td>6.95</td><td>14.60</td><td></td><td></td><td></td><td></td></tr><tr><td>INTC (Intel)</td><td>M</td><td>USD</td><td>127.86</td><td>100.00</td><td>457.2%</td><td>USD</td><td>0.43</td><td>1.07</td><td>1.50</td><td>299.9</td><td>119.4</td><td>85.0</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>65.00</td><td></td><td></td><td></td><td>1.04</td><td>1.35</td><td></td><td></td><td></td><td></td></tr><tr><td>NVDA (NVIDIA)</td><td>O</td><td>USD</td><td>212.45</td><td>315.00</td><td>20.4%</td><td>USD</td><td>4.77</td><td>9.19</td><td>12.52</td><td>44.5</td><td>23.1</td><td>17.0</td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,511.35</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,631.42</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,032.93</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

688041.CH estimate is Reported EPS; 688041.CH valuation is Reported P/E (x); ARM, NVDA base year is 2026;

In the ticker table, 2026 represents FY27/3 for SoftBank and FY26/3 for ARM.

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate SoftBank (PT=¥11,200) and Arm (PT=\$500.00) Outperform.

AMD (Outperform, \$600.00): Expectations remain high, but exposure to AI demand driving both a CPU and GPU story can provide substantial growth.

INTC (Market-Perform, \$100.00): Server strength is helping the company get back on their feet, and narrative/headlines may fuel the vibe for now.

NVDA (Outperform, \$315.00): The datacenter opportunity is enormous, and still early.

We rate Hygon (PT=CNY 450.00) Outperform: we raise our PT from CNY 280 to CNY 450, based on 2028E EPS of CNY 6.30 (+32% vs Bern. Old) and 71x P/E (Previously was Outperform, 80x P/E based on 2027E EPS CNY 3.48, PT CNY 280).

## DETAILS

We raise our 2030 server CPU TAM to \$223bn on the back of higher AI investments and strong CPU:GPU pairing ratio, and our prior forecast of \$137bn is now moved to the bear case (Exhibit 1). On the back of that, we raise PTs for Arm, SoftBank, AMD, Intel, Hygon. Our Server CPU Industry model can be downloaded here: Server CPU Industry Model. Updated Arm financial model can be downloaded here: Arm (Arm.US).

EXHIBIT 1: We believe 2030 server CPU TAM will be \$223bn in the base case of \$3.5tn AI capex.

<table><tr><td>CY</td><td>2025</td><td>2030 Base</td><td>2030 Bull</td><td>2030 Bear</td></tr><tr><td>AI GW additions</td><td>15</td><td>70</td><td>80</td><td>60</td></tr><tr><td>AI capex intensity (bn / GW)</td><td>40</td><td>50</td><td>50</td><td>50</td></tr><tr><td>AI capex ($ bn)</td><td>600</td><td>3,500</td><td>4,000</td><td>3,000</td></tr><tr><td>AI GPU/accelerator TAM ($ bn)</td><td>240</td><td>1,575</td><td>1,800</td><td>1,350</td></tr><tr><td>Inference ratio</td><td>35%</td><td>70%</td><td>70%</td><td>70%</td></tr><tr><td>AI GPU for inferencing ($ bn)</td><td>84</td><td>1,103</td><td>1,260</td><td>945</td></tr><tr><td>CPU:GPU ratio (inference)</td><td>0.25x</td><td>1.0x</td><td>1.5x</td><td>0.5x</td></tr><tr><td>AI GPU for training ($ bn)</td><td>156</td><td>473</td><td>540</td><td>405</td></tr><tr><td>CPU:GPU ratio (training)</td><td>0.25x</td><td>0.50x</td><td>0.50x</td><td>0.50x</td></tr><tr><td>CPU:GPU cost ratio</td><td>10.0%</td><td>13.0%</td><td>13.0%</td><td>13.0%</td></tr><tr><td>CPU for agentic AI ($ bn)</td><td>6.0</td><td>174.0</td><td>280.8</td><td>87.8</td></tr><tr><td>CPU for general CPU server ($ bn)</td><td>31.3</td><td>49.4</td><td>49.4</td><td>49.4</td></tr><tr><td>CPU TAM ($ bn)</td><td>37.3</td><td>223.4</td><td>330.2</td><td>137.2</td></tr></table>

Source: Company disclosures, Mercury, Bernstein estimates and analysis.

## RENAISSANCE OF CPU IN THE AGENTIC AI PARADIGM

Since the rise of LLM, GPU/ASIC accelerators have been the core of AI computing. While training clusters once required a dense 4:1 ratio to handle heavy data-loading, the focus shifted toward eliminating the 'CPU tax' that plagued high-scale inferencing. In custom inference-optimized deployments like Google's TPU v6e and Meta's Grand Teton, the GPU-to-CPU socket ratio moved to 8:1.

Agentic AI is pushing the CPU back to center stage (Exhibit 2) because AI systems are no longer just running a model once and returning an answer. The GPU still performs the dens maths, but the CPU increasingly determines whether the system as a whole can orchestrate the surrounding workflow efficiently — feeding data, scheduling tasks, coordinating tool calls, manage memory and avoid accelerator idling.

This is why the next generation of AI infrastructure is likely to see more balance in terms of hardware pairing, meaning CPU is no longer a small support component attached to a large pool of accelerators in the agentic era. We expect the GPU-to-CPU ratio potentially narrowing back to 1:1 from a very GPU-heavy 4:1 or 8:1 configurations. The 2026 hardware roadmaps are already moving in that direction:

• AMD Venice: 1 CPU to 4 MI455X GPUs per compute tray.  
• NVIDIA Vera: 1 CPU to 2 Rubin GPUs (4 GPU dies) per superchip.  
- Google TPU7x: 1 CPU to 4 TPU chips per scale-up unit.

The GPU/CPU pairing is especially important in agentic workloads because inference is turning into a loop instead of a single pass. A request may trigger retrieval, planning, tool use, intermediate reasoning, another model call, and then action, which means the GPU does the heavy compute while the CPU keeps the workflow moving efficiently; if the CPU is weak, expensive GPUs can sit underutilized, and the overall system becomes slower and less efficient.

Agentic AI also increases pressure on networking and distributed infrastructure, which strengthens the CPU's role even further (Exhibit 3, Exhibit 4). As workloads stretch across servers, clusters, and locations, the system has to move state, manage traffic, and coordinate resources in real time, so the CPU becomes critical not only inside the server but across the wider data-center fabric that supports autonomous AI execution.

Arm CPUs stand out in this environment because the new bottleneck is not only peak performance but efficient orchestration under power and space limits. As operators need more CPU capacity to support growing numbers of AI agents, Arm's pitch around performance per watt, high core density, and scalable data-center compute becomes more compelling, which is why agentic AI is helping bring CPUs back into focus and giving Arm a stronger strategic role in the next phase of AI infrastructure.

EXHIBIT 2: Arm argues that agentic AI shifts more work back to the CPU: accelerators generate tokens, but CPUs orchestrate the agents, memory and workflows needed to deliver answers, making Arm's efficient CPU architecture increasingly critical in AI data centers  
![](images/da1dad2e98c3ec59a6eb304b7716953553c8020a3ac144e539a960864e465947.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["User"] --> B["AI agent"]
  B --> C["Answer"]
  C --> D["Cloud"]
  D --> E["Agents"]
  E --> F["AI data center"]
  F --> G["Accelerators generate tokens"]
  G --> H["CPU orchestrates"]
  H --> I["ACCELERATOR"]
  H --> J["ACCELERATOR"]
  H --> K["ACCELERATOR"]
  H --> L["ACCELERATOR"]
  H --> M["ACCELERATOR"]
  H --> N["ACCELERATOR"]
  H --> O["ACCELERATOR"]
  H --> P["ACCELERATOR"]
  H --> Q["ACCELERATOR"]
  H --> R["ACCELERATOR"]
  H --> S["ACCELERATOR"]
  H --> T["ACCELERATOR"]
  H --> U["ACCELERATOR"]
  H --> V["ACCELERATOR"]
  H --> W["ACCELERATOR"]
  H --> X["ACCELERATOR"]
  H --> Y["ACCELERATOR"]
  H --> Z["ACCELERATOR"]
  H --> AA["ACCELERATOR"]
  H --> AB["ACCELERATOR"]
  H --> AC["ACCELERATOR"]
  H --> AD["ACCELERATOR"]
  H --> AE["ACCELERATOR"]
  H --> AF["ACCELERATOR"]
  H --> AG["ACCELERATOR"]
  H --> AH["ACCELERATOR"]
  H --> AI["ACCELERATOR"]
  H --> AJ["ACCELERATOR"]
  H --> AK["ACCELERATOR"]
  H --> AL["ACCELERATOR"]
  H --> AM["ACCELERATOR"]
  H --> AN["ACCELERATOR"]
  H --> AO["ACCELERATOR"]
  H --> AP["ACCELERATOR"]
  H --> AQ["ACCELERATOR"]
  H --> AR["ACCELERATOR"]
  H --> AS["ACCELERATOR"]
  H --> AT["ACCELERATOR"]
  H --> AU["ACCELERATOR"]
  H --> AV["ACCELERATOR"]
  H --> AW["ACCELERATOR"]
  H --> AX["ACCELERATOR"]
  H --> AY["ACCELERATOR"]
  H --> AZ["ACCELERATOR"]
  H --> BA["ACCELERATOR"]
  H --> BB["ACCELERATOR"]
  H --> BC["ACCELERATOR"]
  H --> BD["ACCELERATOR"]
  H --> BE["ACCELERATOR"]
  H --> BF["ACCELERATOR"]
  H --> BG["ACCELERATOR"]
  H --> BH["ACCELERATOR"]
  H --> BI["ACCELERATOR"]
  H --> BJ["ACCELERATOR"]
  H --> BK["ACCELERATOR"]
  H --> BL["ACCELERATOR"]
  H --> BM["ACCELERATOR"]
  H --> BN["ACCELERATOR"]
  H --> BO["ACCELERATOR"]
  H --> BP["ACCELERATOR"]
  H --> BQ["ACCELERATOR"]
  H --> BR["ACCELERATOR"]
  H --> BS["ACCELERATOR"]
  H --> BT["ACCELERATOR"]
  H --> BU["ACCELERATOR"]
  H --> BV["ACCELERATOR"]
  H --> BW["ACCELERATOR"]
  H --> BX["ACCELERATOR"]
  H --> BYB["ACCELERATOR"]
  H --> BZ["BX"]
```
</details>

Source: Arm

EXHIBIT 3: CPU is expected to play a more important role within inference, in the agentic area.  
2020-2029E: Average GPU-to-CPU ratio in CSP inference clusters  
![](images/02785f21f75d2cd0b6cd6d17aa537e88df2e6ae60d420d8d44f61511ccf6aad4.jpg)

<details>
<summary>line chart</summary>

| Year | Value |
| :--- | :--- |
| 2020 | 3:1 |
| 2021 | 4:1 |
| 2022 | 6:1 |
| 2023 | 7:1 |
| 2024 | 8:1 |
| 2025 | 8:1 |
| 2026E | 5:1 |
| 2027E | 3:1 |
| 2028E | 2:1 |
| 2029E | 2:1 |
</details>

Source: Ciena estimates, Bernstein analysis.

EXHIBIT 4: Agentic AI shifts compute balance toward CPUs, with CPU share rising from \~14% in Traditional LLMs to 50%, highlighting CPUs' growing orchestration role alongside GPUs in AI workloads at scale  
CPU:GPU ratio shift in Agentic AI  
![](images/e266ef9d24a2a1ad84207c23af73eac374808aebc20202db5177dd3ab283082e.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | CPU (%) | GPU (%) |
| :--- | :--- | :--- |
| Traditional LLM | 14 | 87 |
| Agentic AI | 50 | 49 |
</details>

Source: TrendForce, Bernstein analysis

EXHIBIT 5: AI infrastructure TAM expands sharply by CY30, led by data center accelerators reaching \$1T, while data center CPU also quadruples from \$33bn to \$137bn.  
![](images/a6dc048159276a4ba6101ed7ba3751e303fd43d18cc74947b10e57eccbabb74a.jpg)

<details>
<summary>stacked bar chart</summary>

CPU/GPU TAM
| Year | DC CPU (USD bn) | DC Accelerators (USD bn) |
| :--- | :--- | :--- |
| CY2025 | 33 | 245 |
| CY2030 | 137 | 1000+ |
</details>

Source: Mercury, Company reports, Bernstein estimates and analysis.

EXHIBIT 6: We expect the server CPU market to grow from US\$37bn in 2025 to US\$223bn in 2030, accelerating at a 43% CAGR, driven by Agentic AI adoption.  
2020-2030E: Server CPU Market Size  
![](images/8e3dc68b046bf6893178f7940ca698c7caeaaac9317d8ffe2f76d670c237fd53.jpg)

<details>
<summary>bar chart</summary>

| Year | Value (USD bn) |
| :--- | :--- |
| 2020 | 14 |
| 2021 | 16 |
| 2022 | 18 |
| 2023 | 21 |
| 2024 | 25 |
| 2025 | 37 |
| 2026E | 63 |
| 2027E | 90 |
| 2028E | 131 |
| 2029E | 176 |
| 2030E | 223 |
</details>

Source: Mercury, Company reports, Bernstein analysis and estimates

## RAISING 2030 SERVER CPU TAM FORECAST TO \$223BN

Within our initiation of Arm, we forecast the CY30 data center CPU TAM of \$137bn, well above both Arm's own estimates of \$100bn and AMD's \$120bn, on the basis that agentic workloads require much more CPU intensity.

Since our initiation, there are quite a few incremental developments, including better-than-expected agentic AI adoption, and higher-than-expected AI GW and capex spending. Nvidia also guided for a \$20bn revenue from Vera CPU which should also be positive for Arm. The other notable data point that was provided by Nvidia was the annual AI infrastructure spending forecasts of over \$1tn by 2027 and 

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
