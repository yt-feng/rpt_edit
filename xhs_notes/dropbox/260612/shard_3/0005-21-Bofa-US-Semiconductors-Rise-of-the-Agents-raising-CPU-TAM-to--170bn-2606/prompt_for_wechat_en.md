You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
## US Semiconductors

# Rise of the Agents: raising CPU TAM to \$170bn

Price Objective Change

## CPU reborn: Agentic AI drives 5x demand

Based on our analysis and recent industry discussions at BofA Global Tech Conference (see our conf takeaways), we raise our CY2030E server CPU TAM to \$170bn+ (from \$125bn), implying nearly 5x growth and +37% CAGR over CY25-30E (vs. +29% prior). We view the emergence of agentic AI as a powerful demand accelerant that expands the CPU opportunity and lifts both x86incumbents and ARM challengers. Against this backdrop, we raise our AMD PO to \$560 from \$500 on higher CPU/GPU estimates, ARM to \$335 from \$245 on greater l-t chiplet potential; INTC is double-upgraded to Buy with a \$135 PO (see our ), with higher estimates now reflecting both n-t CPU and l-t foundry upsides. NVDA remains our top sector pick on full-stack AI leadership, benefiting from tight CPU-GPU-networking integration, also poised to benefit from agentic CPU. QCOM is expected to announce new AI CPUs at its Jun-24 AI Day in NYC, but we maintain Underperform given tough competition and limited SAM.

## Agentic workloads shift complexity to CPUs from XPUs

Agentic AI differs from traditional genAI by shifting from a single prompt-response workflow to a multi-step system that plans, reasons, retrieves info, uses tools, executes code simultaneously. While XPUs remain critical for inference, many orchestration and decision-making functions are latency-sensitive, sequential, and I/O-intensive—making them better suited for CPUs. Our new CPU model uniquely segments the \$170bn TAM by application (1. standalone agentic CPU; 2. head/compute node CPU for AI clusters; 3. traditional/laaS), as well as by vendor (AMD, INTC, NVDA, ARM merchant, ARM custom). We expect head/compute nodes in AI clusters to use higher frequency and stronger but fewer cores, while agentic and traditional applications will rely on higher core counts.

## Double-upgrading INTC, while AMD top CPU pick

Our INTC double-upgrade is based on higher confidence in INTC's opportunity to help address industry constraints in leading edge wafers/packaging, plus larger agentic CPU TAM. We now see CY30 EPS power \$6+ vs \$3-4 prior, though execution is key. Recent CDNS 14A node IP sign-up and Terafab engagements are additional supportive data points. For AMD, we raise est/PO to \$560, top CPU pick on incumbency + pipeline + upcoming AI day (Venice launch). NVDA remains top sector pick on full-stack leadership.

## ARM/QCOM: CPU share gainers but flag val'n/competition

For ARM, we now use a FY31/CY30E sum-of-parts valuation, see total company value of \~\$335 (\$229 IP + \$106 chip), and we see the stock as fairly valued. QCOM has potential to announce new AI CPUs and lead customers at its Jun-24 AI Day, but we flag tough CPU competition amid already established incumbents.

## Key debate: TAM substitution vs expansion

Debate centers on whether CPUs take share from GPUs/accelerators or contribute to overall AI TAM expansion. We see expansion dominating: CPU demand scales with system complexity, as is the case with reasoning/agentic AI. Additional debates include durability of the 30%+ AI capex CAGR and mix shifts to custom silicon (CPUs and XPUs).

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 29 to 33. Analyst Certification on page 27. Price Objective Basis/Risk on page 26.
12983146

## 11 June 2026

Equity

United States

Semiconductors

Vivek Arya

Research Analyst

BofAS

vivek.arya@bofa.com

Duksan Jang

Research Analyst

BofAS

duksan.jang@bofa.com

Michael Mani

Research Analyst

BofAS

michael.mani@bofa.com

Liam Pharr

Research Analyst

BofAS

liam.pharr@bofa.com

Exhibit 1: PO/Rating Changes  
PO/Rating Changes

<table><tr><td colspan="4">PO/Rating Changes</td></tr><tr><td>Ticker</td><td>OLD</td><td>NEW</td><td>RATING</td></tr><tr><td>AMD</td><td>$500</td><td>$560</td><td>BUY</td></tr><tr><td>ARM</td><td>$245</td><td>$335</td><td>NEUTRAL</td></tr><tr><td>INTC</td><td>$96</td><td>$135</td><td>BUY from U/P</td></tr><tr><td>NVDA</td><td>$350</td><td>$350</td><td>BUY</td></tr><tr><td>QCOM</td><td>$165</td><td>$165</td><td>U/P</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

For detailed company analysis, PO/rating change and valuation discussion, see pg. 10-17.

See glossary on page 23.

## Contents

AI Compute Table of Hierarchy 3

\$170bn+ Server CPU TAM 5

Market share outlook analysis 6

Traditional vs. AI Head Node (Compute) vs. Agentic Rack 7

CPUs now 8%+ of Data Center Systems TAM 9

AMD: Maintain Buy, raise PO to \$560 from \$500 10

AMD CPU Advantages 10

Upcoming catalyst: Advancing AI 2026 (July) 11

INTC: Upgrade to Buy from U/P, PO \$135 12

Fully established IDM by CY30, EPS power \$6+ 12

ARM: Reit. Neutral, raise PO to \$335 14

Sum-of-Parts Valuation: IP & Chip Businesses 14

NVDA: Maintain Buy, top AI sector pick 15

Rising content, increasing opp'ty, solid supply visibility 15

Vera Rubin now in full production, lowest token cost 15

Vera CPU: head node vs. agentic AI likely 50/50 opp'ty 16

NVDA content \$/GW rising materially gen-over-gen 16

RTX Spark for personal agentic AI, for top 10% Windows 16

QCOM: U/P on competitive landscape 17

Role of CPUs in Agentic AI 18

CPUs in training 18

CPUs in inference 19

CPUs in Agentic AI 20

Agentic AI is system-led, not CPU or GPU-led 21

AI CPUs expand system TAM, not replace 21

## AI Compute Table of Hierarchy

Below, we present our latest table of hierarchy for global data center systems TAM of \~\$2.1Tn, of which CPUs make up \~\$170bn of the total value.

Within this, we break out CPUs in three different categories (more detail in following pages):

1. Traditional/on-prem/multi-tenant cloud CPUs: \~\$30bn  
2. AI cluster compute/head node CPUs: \~\$70bn  
3. AI agentic standalone node CPUs: \~\$70bn

Exhibit 2: Of the total \$2.1Tn CY30 DC Systems TAM, we see AI CPUs representing \~\$140bn of the value (split roughly 50/50 across compute/head node and agentic AI node), non-AI CPUs \~\$30bn

Data Center Systems TAM – Breakout by: AI vs. non-AI; AI CPUs vs. non-AI CPUs

![](images/f49c76f933abbd9324831823429bfacd926d1f2f77b792cfbf6fee6e576e0aff.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | Value |
| :--- | :--- |
| Total Data Center Systems TAM: $2.1Tn 2030E | |
| AI Data Center Systems TAM: $1.7Tn | |
| Non-AI DC Systems TAM: $363bn | |
| AI Servers: $1.3Tn | |
| AI Networking: $305bn | |
| Storage: $81bn | |
| AI Accelerators: $1.1Tn | HBM: $168bn |
| AI Accelerators: $1.1Tn | AI CPU: $140bn |
| AI Accelerators: $1.1Tn | Other: $51bn |
| Trad'I Cloud CPU: $30bn | |
| AI Cluster Compute/Head Nodes: $70bn | |
| AI Agentic Standalone Nodes: $70bn | |
</details>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

The below infographic highlights how the role of the CPU evolves across different server architectures:

1. Traditional Server: The CPU is the primary "jack-of-all-trades," managing the OS, applications, and direct I/O for general workloads. (\~\$30bn CY30E TAM)  
2. AI Server Cluster: The CPU's role bifurcates into a Head Node for cluster orchestration and management, and a Compute Node focused on supervising and feeding data to GPUs. (\~\$70bn CY30E TAM)  
3. Agentic Server: The CPU becomes the central orchestrator for autonomous actions, managing the high-level reasoning loops, memory state, and tool integration required for AI agents. (\~\$70bn CY30E TAM)

Exhibit 3: We flag three key roles of CPUs in servers: 1. Traditional, 2. AI compute/head node, 3. AI agentic node Role of the CPU in different server architectures

## ROLE OF THE CPU IN DIFFERENT SERVER ARCHITECTURES

![](images/5921956c0b3ae0bfcc72d8cfe094531f1cb859aa478a5674699824c21d3ca917.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["CPU"] --> B["RAM"]
  A --> C["DISKS"]
  A --> D["NETWORK I/O"]
  A --> E["STORAGE ACCESS"]
  A --> F["OPERATING SYSTEM (Linux, Windows)"]
  A --> G["WEB HOSTING (Nginx, Apache)"]
  A --> H["DATABASES (SQL, NoSQL)"]
  A --> I["APPLICATIONS"]
  A --> J["GENERAL-PURPOSE COMPUTING, MULTIT- & CONTEXT SWITCHING"]
  A --> K["DIRECTLY EXECUTING APPLICATIONS"]
  A --> L["MANAGING SYSTEM RESOURCES"]
```
</details>

![](images/0c5bb3a321c14dcf30409ddc01de2f75c818a34fca57cf5f7ef18da7be2664d4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["AI SERVER (CLUSTER ARCHITECTURE)"] --> B["HEAD NODE (Control & Management)"]
    B <--> C["CPU"]
  C --> D["JOB SCHEDULING (Slurm, Kubernetes)"]
  C --> E["USER ACCESS"]
  C --> F["DATA MANAGEMENT"]
  C --> G["MONITORING"]
    B <--> H["COMPUTE NODE (Accelerator Coordination)"]
  H --> I["GPU ACCELERATORS"]
  I --> J["ACCELERATOR COORDINATOR & SUPERVISOR"]
    J <--> K["PCIe/NVLink"]
  K --> L["MASSIVE DATA STREAMS"]
  L --> M["FEEDING DATA TO GPUs"]
  L --> N["MANAGING HIGH-BANDWIDTH INTERCONNECTS"]
  L --> O["PREPARING TRAINING/INFERENCE DATASETS"]
  L --> P["MINIMAL COMPUTATION FOR AI MODELS (GPUs do heavy lifting)"]
```
</details>

![](images/d364ae53275cf36cb9e1b8ce3e32d01d21263508ec3312a8213bc2ee3d2c8aa3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["AGENTIC SERVER (Autonomous Actions)"] --> B["CPU"]
  B --> C["PERCEPTION & ENVIRONMENTS"]
  B --> D["PERCEPTION & ENVIRONMENTS"]
  B --> E["PLANING & DECISION-MAKING"]
  B --> F["ACTION EXECUTION (API Calls, Tool Usage)"]
  B --> G["STATE MANAGEMENT & MEMORY (RAM, Vector DB)"]
  B --> H["AGENT LOGIC & REASONING (Running LLMs/Complex Code)"]
  B --> I["Central Thinking Engine & TASK ORCHESTRATOR"]
  C --> J["RUNNING AUTONOMOUS AGENT LOOPS"]
  D --> K["COMPLEX REASONING & PLANNING"]
  E --> L["MANAGING AGENT MEMORY"]
  F --> M["ORCHESTRATING EXTERNAL TOOLS & SERVICES"]
  G --> N["INTERACTING WITH VECTOR DATABASES"]
```
</details>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## \$170bn+ Server CPU TAM

Given the rising role of CPUs in AI head node (compute node) and agentic AI, we now expect server CPU TAM to reach \~\$170bn by CY30E from \~\$35bn in CY25 (+37% CAGR), versus prior \~\$125bn outlook (+29% CAGR).

Notably, we break out the market into 4 different vendor/types: 1) INTC, 2) AMD, 3) ARM (merchant), and 4) ARM (custom/ASIC).

- For ARM merchant CPUs, we now assume ASPs that are \~1.25x higher than average AMD CPUs, given ARM merchant almost only caters to hyperscale/AI applications, versus AMD mostly hyperscale with a bit of enterprise exposure.  
- For ARM custom CPUs, we now assume ASPs that are \~75% of typical AMD solutions, given continued mix shift toward hyperscale solutions (higher ASPs), but merchant server CPUs typically carry 40-60% GM (i.e. 40-60% is COGS or the cost that AWS/Google would theoretically be paying for their custom CPUs)

Exhibit 4: We see total server CPU TAM reaching \$170bn+ by CY30 from \$35bn in CY25, growing at +37% CAGR  
Server CPU TAM (by revenue, units, ASP)

<table><tr><td>Server CPU TAM</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>CY25-30 CAGR</td></tr><tr><td colspan="10">Revenue ($bn)</td></tr><tr><td>Total</td><td>$19.5</td><td>$22.5</td><td>$35.2</td><td>$59.6</td><td>$89.8</td><td>$110.4</td><td>$138.2</td><td>$170.1</td><td>37.1%</td></tr><tr><td>INTC</td><td>$13.2</td><td>$13.6</td><td>$14.4</td><td>$19.8</td><td>$24.7</td><td>$29.6</td><td>$35.1</td><td>$41.2</td><td>23.4%</td></tr><tr><td>AMD</td><td>$5.6</td><td>$7.1</td><td>$9.6</td><td>$16.4</td><td>$22.2</td><td>$28.6</td><td>$35.7</td><td>$43.6</td><td>35.4%</td></tr><tr><td>ARM</td><td>$0.7</td><td>$1.8</td><td>$11.2</td><td>$23.4</td><td>$42.9</td><td>$52.2</td><td>$67.5</td><td>$85.4</td><td>50.0%</td></tr><tr><td>ARM Merchant</td><td>$0.0</td><td>$0.7</td><td>$10.3</td><td>$19.5</td><td>$34.8</td><td>$38.2</td><td>$47.9</td><td>$60.6</td><td>42.6%</td></tr><tr><td>NVDA</td><td></td><td>$0.7</td><td>$10.3</td><td>$19.5</td><td>$33.7</td><td>$35.4</td><td>$39.0</td><td>$42.2</td><td>32.7%</td></tr><tr><td>ARM</td><td></td><td></td><td></td><td></td><td>$0.7</td><td>$1.8</td><td>$5.9</td><td>$12.3</td><td></td></tr><tr><td>QCOM</td><td></td><td></td><td></td><td></td><td>$0.4</td><td>$0.9</td><td>$3.0</td><td>$6.1</td><td></td></tr><tr><td>ARM Custom (Graviton, Axion, Cobalt, etc.)</td><td>$0.7</td><td>$1.0</td><td>$1.0</td><td>$3.9</td><td>$8.1</td><td>$14.1</td><td>$19.6</td><td>$24.8</td><td>91.0%</td></tr><tr><td colspan="10">Units (mn)</td></tr><tr><td>Total</td><td>24.5</td><td>24.2</td><td>29.2</td><td>39.3</td><td>49.0</td><td>57.1</td><td>66.0</td><td>74.7</td><td>20.7%</td></tr><tr><td>INTC</td><td>18.5</td><td>16.9</td><td>17.9</td><td>21.1</td><td>23.2</td><td>24.9</td><td>26.7</td><td>28.6</td><td>9.7%</td></tr><tr><td>AMD</td><td>4.8</td><td>5.5</td><td>7.2</td><td>10.4</td><td>12.5</td><td>14.5</td><td>16.3</td><td>18.1</td><td>20.2%</td></tr><tr><td>ARM</td><td>1.2</td><td>1.8</td><td>4.0</td><td>7.9</td><td>13.3</td><td>17.7</td><td>22.9</td><td>28.0</td><td>47.4%</td></tr><tr><td>ARM Merchant</td><td>0.0</td><td>0.2</td><td>2.6</td><td>4.6</td><td>7.2</td><td>8.2</td><td>10.9</td><td>14.2</td><td>40.9%</td></tr><tr><td>NVDA</td><td>0.0</td><td>0.2</td><td>2.6</td><td>4.6</td><td>6.7</td><td>7.1</td><td>7.7</td><td>8.1</td><td>25.9%</td></tr><tr><td>ARM</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.3</td><td>0.7</td><td>2.2</td><td>4.1</td><td></td></tr><tr><td>QCOM</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.2</td><td>0.4</td><td>1.1</td><td>2.0</td><td></td></tr><tr><td>ARM Custom (Graviton, Axion, Cobalt, etc.)</td><td>1.2</td><td>1.6</td><td>1.5</td><td>3.3</td><td>6.1</td><td>9.5</td><td>12.0</td><td>13.8</td><td>56.6%</td></tr><tr><td colspan="10">ASP ($)</td></tr><tr><td>Total</td><td>$797</td><td>$931</td><td>$1,204</td><td>$1,517</td><td>$1,833</td><td>$1,934</td><td>$2,095</td><td>$2,277</td><td>13.6%</td></tr><tr><td>INTC</td><td>$716</td><td>$804</td><td>$801</td><td>$941</td><td>$1,065</td><td>$1,186</td><td>$1,311</td><td>$1,442</td><td>12.5%</td></tr><tr><td>AMD</td><td>$1,164</td><td>$1,299</td><td>$1,322</td><td>$1,581</td><td>$1,778</td><td>$1,976</td><td>$2,183</td><td>$2,401</td><td>12.7%</td></tr><tr><td>ARM</td><td>$589</td><td>$998</td><td>$2,790</td><td>$2,972</td><td>$3,225</td><td>$2,956</td><td>$2,950</td><td>$3,049</td><td>1.8%</td></tr><tr><td>ARM Merchant</td><td></td><td>$4,000</td><td>$4,000</td><td>$4,240</td><td>$4,820</td><td>$4,658</td><td>$4,393</td><td>$4,255</td><td>1.2%</td></tr><tr><td>NVDA</td><td></td><td>$4,000</td><td>$4,000</td><td>$4,240</td><td>$5,000</td><td>$5,000</td><td>$5,100</td><td>$5,202</td><td>5.4%</td></tr><tr><td>ARM</td><td></td><td></td><td></td><td></td><td>$2,249</td><td>$2,476</td><td>$2,729</td><td>$3,002</td><td></td></tr><tr><td>QCOM</td><td></td><td></td><td></td><td></td><td>$2,249</td><td>$2,476</td><td>$2,729</td><td>$3,002</td><td></td></tr><tr><td>ARM Custom (Graviton, Axion, Cobalt, etc.)</td><td>$589</td><td>$649</td><td>$666</td><td>$1,191</td><td>$1,336</td><td>$1,484</td><td>$1,637</td><td>$1,801</td><td>22.0%</td></tr><tr><td colspan="10">Value Share (%)</td></tr><tr><td>Total</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td></td></tr><tr><td>INTC</td><td>68%</td><td>61%</td><td>41%</td><td>33%</td><td>28%</td><td>27%</td><td>25%</td><td>24%</td><td></td></tr><tr><td>AMD</td><td>29%</td><td>32%</td><td>27%</td><td>28%</td><td>25%</td><td>26%</td><td>26%</td><td>26%</td><td></td></tr><tr><td>ARM</td><td>4%</td><td>8%</td><td>32%</td><td>39%</td><td>48%</td><td>47%</td><td>49%</td><td>50%</td><td></td></tr><tr><td>ARM Merchant</td><td>0%</td><td>3%</td><td>29%</td><td>33%</td><td>39%</td><td>35%</td><td>35%</td><td>36%</td><td></td></tr><tr><td>NVDA</td><td></td><td>3%</td><td>29%</td><td>33%</td><td>38%</td><td>32%</td><td>28%</td><td>25%</td><td></td></tr><tr><td>ARM</td><td></td><td></td><td></td><td></td><td>1%</td><td>2%</td><td>4%</td><td>7%</td><td></td></tr><tr><td>QCOM</td><td></td><td></td><td></td><td></td><td>0%</td><td>1%</td><td>2%</td><td>4%</td><td></td></tr><tr><td>ARM Custom (Graviton, Axion, Cobalt, etc.)</td><td>4%</td><td>5%</td><td>3%</td><td>7%</td><td>9%</td><td>13%</td><td>14%</td><td>15%</td><td></td></tr></table>

BofA GLOBAL RESEARCH

## Market share outlook analysis

From a market share perspective, we continue to expect ARM to be the fastest gainer through CY30 as multiple new merchant (i.e. ARM AGI, NVDA Vera, QCOM CPU) and custom (i.e., AWS Graviton 5, Google Axion, Microsoft Cobalt) programs ramp.

Exhibit 5: We expect INTC/AMD to each represent \~25% value share, ARM merchant \~35%, ARM custom \~15% by CY30  
Server CPU TAM (\$mn) and Value Market Share Outlook  
![](images/59b9b87d80f9f8ee1d9630ff6ba3e943d8a7ce8bb7a6ef41ade4354286811b5c.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Intel (%) | AMD (%) | Arm Merchant (%) | Arm Custom (%) |
| :--- | :--- | :--- | :--- | :--- |
| 2025 | 40.9 | 27.2 | 29.2 | 1.8 |
| 2026E | 33.2 | 27.5 | 32.7 | 6.5 |
| 2027E | 27.5 | 24.7 | 38.7 | 9.1 |
| 2028E | 26.8 | 25.9 | 34.6 | 12.7 |
| 2029E | 25.4 | 25.8 | 34.6 | 14.2 |
| 2030E | 24.2 | 25.6 | 35.6 | 14.6 |
Total: $170,121
$138,242
Note: The chart displays a stacked bar chart with values in parentheses and percentages indicating the proportion of each segment within the total revenue.
</details>

Source: BofA Global Research estimates, Mercury Research, IDC  
BofA GLOBAL RESEARCH

\- INTC (\~25% value share): We see share declining to just \~24% of total server CPU value by CY30 from \~41% in CY25, though we expect INTC's continued relative strength in traditional enterprise workloads.

However, we see continued \$ revenue growth of +20% CAGR between CY26-30, particularly as INTC navigates through the industry-wide supply shortages, benefits from ASP expansion. By CY28, next-next-gen Coral Rapids should ramp and could begin to narrow the performance gap vs. competition.

\- AMD (\~25% value share): We see share of \~25-27% generally through CY30, given AMD's continued performance lead at the high-end (high-frequency, high-core-count AI head node and agentic node), offset by relative stronger ramps of ARM-based processors launching beginning CY27E.

Particularly, we flag AMD's leading core count portfolio, given higher co

[中间内容因长度限制已省略]

ions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
