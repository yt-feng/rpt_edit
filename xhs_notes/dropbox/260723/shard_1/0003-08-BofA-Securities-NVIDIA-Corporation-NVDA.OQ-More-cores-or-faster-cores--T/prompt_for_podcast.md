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
# More cores or faster cores? The NVDA vs AMD agentic CPU debate

Maintain Rating: BUY | PO: 350.00 USD | Price: 207.29 USD

## Emerging battle in \$170bn server CPU market

Today NVDA provided its most detailed disclosure yet on its Vera CPU architecture, introducing a new framework for evaluating AI infrastructure: max single-threaded performance at scale. Vera combines 88 custom Olympus ARM-based cores, 1.2TB/s memory bandwidth and 3.4TB/s on-die fabric bandwidth, with NVDA arguing that agentic AI increasingly depends on CPU latency, memory responsiveness and GPU utilization. NVDA's choice of a monolithic compute die (which it claims provides scalable coherency) also stands in contrast to AMD's proven chiplet architecture. AMD's AI 2026 Day on Thursday (see our preview) provides the industry the first major opportunity for a public-technical response in a server CPU TAM that could 4x towards \$170bn by 2030E (see our industry report).

## NVDA: Faster agents beat more agents (# of cores)

NVDA's core argument is that agentic AI consists of repeated CPU↔GPU loops involving tool calls, code execution, retrieval and orchestration, where each step depends on completion of the previous one. In this framework, faster per-core performance directly improves agent response times, GPU utilization and overall AI-factory productivity. NVDA Vera CPU also benefits from "co-design" across six other AI building blocks including Rubin GPU, Groq LPX, Spectrum switches, and BlueField storage/NICs.

## AMD: More agents beat faster agents

AMD argues production AI increasingly resembles a distributed software platform composed of databases, APIs, vector stores, orchestration engines, caches and middleware. In this environment, the primary constraint becomes the number of concurrent workflows that can be sustained inside a fixed power envelope. AMD estimates EPYC 9965 (Turin) delivers \~2.4x the rack-level throughput of NVIDIA's Vera baseline in a modeled 100kW deployment, with EPYC 6 (Venice) projected at \~3.3x.

## A parallel debate: x86 versus ARM

The CPU discussion extends beyond core counts into software ecosystems. NVDA's position implies ISA becomes secondary if superior microarchitecture delivers better agent performance. AMD and INTC are likely to argue that agentic AI increasingly intersects with enterprise software stacks, where x86 benefits from decades of optimization, validation and compatibility across databases, middleware, security platforms and enterprise applications. As AI expands from model inference into enterprise workflows, software incumbency could become an important differentiator.

## Our view: Defining the next CPU KPI

The key question for investors is whether agentic AI is primarily constrained by \*\*time-to-complete an agent\*\* or \*\*number-of-agents-per-rack\*\*. NVDA's framework is rooted in latency, per-thread progress, and GPU utilization. AMD's framework is rooted in concurrency, throughput, and service density. Our expectation is that AMD's Thursday event will be less about benchmark comparisons and more about establishing the industry's preferred metric.

## 22 July 2026

Equity

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

## Stock Data

<table><tr><td>Price</td><td>207.29 USD</td></tr><tr><td>Price Objective</td><td>350.00 USD</td></tr><tr><td>Date Established</td><td>20-May-2026</td></tr><tr><td>Investment Opinion</td><td>C-1-7</td></tr><tr><td>52-Week Range</td><td>164.07 USD - 236.54 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>5,157,375 USD / 24,880.0</td></tr><tr><td>Free Float</td><td>96.2%</td></tr><tr><td>Average Daily Value (mn)</td><td>30162.66 USD</td></tr><tr><td>BofA Ticker / Exchange</td><td>NVDA / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>NVDA US / NVDA.OQ</td></tr><tr><td>ROE (2027E)</td><td>95.9%</td></tr><tr><td>Net Dbt to Eqty (Jan-2026A)</td><td>-1.4%</td></tr></table>

Exhibit 1: NVDA argues Vera provides the max single threaded performance critical for agentic AI Single-threaded core versus throughput quadrant and Vera CPU positioning  
![](images/f4c975a706b4d77cbf102af90c3621592d9c2cc2ba0ef1414748c453ba900935.jpg)  
Source: NVDA  
BofA GLOBAL RESEARCH

## Glossary:

AI – Artificial Intelligence

AMD – Advanced Micro Devices

API – Application Programming Interface

ARM – Advanced RISC Machines

CPU – Central Processing Unit

GPU – Graphics Processing Unit

INTC – Intel Corporation

ISA – Instruction Set Architecture

KPI – Key Performance Indicator

kW - Kilowatt

LPX – Groq's Language Processing Unit variant

NIC – Network Interface Card

NVDA – NVIDIA

TAM – Total Addressable Market

TB/s – Terabytes per second

Exhibit 2: Companies mentioned
Companies mentioned in this report

<table><tr><td>BofA Ticker</td><td>Bloomberg ticker</td><td>Company name</td><td>Price</td><td>Rating</td></tr><tr><td>NVDA</td><td>NVDA US</td><td>NVIDIA</td><td>US$ 207.29</td><td>C-1-7</td></tr><tr><td>AMD</td><td>AMD US</td><td>Advanced Micro</td><td>US$ 544.43</td><td>C-1-9</td></tr><tr><td>ARM</td><td>ARM US</td><td>Arm Holdings</td><td>US$ 289.73</td><td>C-2-9</td></tr><tr><td>INTC</td><td>INTC US</td><td>Intel</td><td>US$ 105.45</td><td>C-1-9</td></tr></table>

Source: BofA Global Research

BofA GLOBAL RESEARCH

## Price objective basis & risk

## Advanced Micro Devices, Inc (AMD)

Our \$620 PO is based on 47x our 2027E non-GAAP EPS. Our PO basis is now towards middle/upper range of historical 13x-58x, but is well supported by AMD's 50%+ annual EPS CAGR potential and its AI CPU/GPU share gain potentials, modestly offset by slower growth in cyclical PC/embedded/console markets.

Downside risks: 1) Execution on first rack-scale product (MI400 Series), 2) Timing/Magnitude of Middle East AI Projects, 3) Lumpy nature of consumer and enterprise spending that could create delays in acceptance and success of new products, 4) High reliance on one outsourced manufacturing partner, 5) Maturity of current game console cycle.

Upside risks are greater share gain potential in the PC and server processor market against competitors.

## Arm Holdings (ARM)

Our \$460 PO is based on conceptual sum-of-parts valuation that values the IP business at \$342 (2.5x CY30E PEG, discounted back 2 years) and the chiplet business at \$118 (31x CY30E PE, discounted back 2 years), with both multiples in-line with competitive peer range/average. Our PO implies 130x total company CY28E PE which is still within ARM's historical 35x-147x range, given longer-term data center content and silicon/chiplet (AGI CPU) opportunities, offset by high SoftBank dependence and opex ramp.

Upside risks: 1) better than expected smartphone/PC/server unit shipment, 2) faster adoption of higher-royalty rate v9 and CSS IP at customers, 3) faster share gains and ramp of AGI CPU chiplet lineup, 4) further proliferation of AI data centers and hyperscale-specific custom products, 5) Qualcomm/Nuvia content expansion post-settlement, 6) small floating volume.

Downside risks: 1) historically cyclical nature of semiconductor units, 2) high exposure to mature smartphone market, 3) competition against established x86 and other custom Arm-based CPU offerings in the data center, 4) emerging competition from RISC-V in low-end consumer markets, 5) rising geopolitical tensions and deterioration of Arm China relationship, 6) ongoing Qualcomm/Nuvia litigation, 7) small trading float.

## Intel (INTC)

Our \$160 price objective is based on 31x CY30E EPS power of \$6+, discounted back two years, given the company's key server CPU and external foundry wafer/packaging opportunities that extend far out. Our PO implies 10.7x our total company 2028E EV/S which is well above historical 1.7x-4x range but we view as appropriate given increasing server CPU and external foundry opportunity, offset by near-/medium-term manufacturing ramp-up uncertainties.

Upside risks to our price objective are 1) key external foundry packaging/wafer deals that could significantly boost sales/utilization, 2) greater than expected yields/ramps at 18A and upcoming 14A nodes, resulting in greater GM/utilization profile, 3) stronger than expected PC market from Windows 10 refresh or AI uplift, 4) geopolitical tensions boosting sentiment for domestic manufacturing asset.

Downside risks to our price objective are 1) lower than yield/ramp at Intel Foundry, particularly for its new 18A and upcoming 14A nodes, 2) lack of material external foundry customer in wafer processing, 3) weaker-than-expected trends in a mature PC market, which is largest revenue generator for Intel, 4) accelerated share loss to major CPU competitors.

## NVIDIA Corporation (NVDA)

Our \$350 PO is based on 26x CY27E PE ex cash, within NVDA's historical 25x-56x forward year PE range, which we believe is justified by NVDA's leading share in fast-growing AI compute/networking markets, offset by lumpiness in global AI projects, cyclical gaming market, and concerns around access to power.

Downside risks are: 1) weakness in consumer driven gaming market, 2) Competition with major public firms, internal cloud projects and other private companies in AI and accelerated computing markets, 3) Larger than expected impact from restrictions on compute shipments to China, or additional restrictions placed on activity in the region, 4) Lumpy and unpredictable sales in new enterprise, data center, and autos markets, 5) Potential for decelerating capital returns, and 6) Enhanced government scrutiny of NVDA's dominant market position in AI chips.

## Analyst Certification

I, Vivek Arya, hereby certify that the views expressed in this research report accurately reflect my personal views about the subject securities and issuers. I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or view expressed in this research report.

## Special Disclosures

BofA is currently acting as financial advisor to One Investment Management Ltd in connection with the proposed acquisition with PayPay Corporation, a subsidiary of SoftBank Group Corp., of shares of T&D Financial Life Insurance Company, a consolidated subsidiary of T&D Holdings, Inc., which was announced on June 4, 2026.

BofA is currently acting as joint financial advisor to ABB Ltd in connection with the sale of its Robotics Division to SoftBank Group Corp, which was announced on October 8, 2025.

## Disclosures

## Important Disclosures

## NVIDIA (NVDA) Price Chart

![](images/a52a100a609212cb1678dcb58e370dd3de0fd4880fac7119109226abcc7e80dc.jpg)  
B: Buy, N: Neutral, U: Underperform, PO: Price Objective, NA: No longer valid, NR: No Rating

The Investment Opinion System is contained at the end of the report under the heading "Fundamental Equity Opinion Key". Dark grey shading indicates the security is restricted with the opinion suspended. Medium grey shading indicates the security is under review with the opinion withdrawn. Light grey shading indicates the security is not covered. Chart is current as of a date no more than one trading day prior to the date of the report.

Advanced Micro (AMD) Price Chart  
![](images/7bcf6c995cfb6a272d514b5760aece6986128ad6794d441ecb1f6829d80498f0.jpg)  
B: Buy, N: Neutral, U: Underperform, PO: Price Objective, NA: No longer valid, NR: No Rating

The Investment Opinion System is contained at the end of the report under the heading "Fundamental Equity Opinion Key". Dark grey shading indicates the security is restricted with the opinion suspended. Medium grey shading indicates the security is under review with the opinion withdrawn. Light grey shading indicates the security is not covered. Chart is current as of a date no more than one trading day prior to the date of the report.

Arm Holdings (ARM) Price Chart  
![](images/290dc36e6f937f468d11472f6823463000a413834d17bf402dc47c4d69375098.jpg)  
B: Buy, N: Neutral, U: Underperform, PO: Price Objective, NA: No longer valid, NR: No Rating

The Investment Opinion System is contained at the end of the report under the heading "Fundamental Equity Opinion Key". Dark grey shading indicates the security is restricted with the opinion suspended. Medium grey shading indicates the security is under review with the opinion withdrawn. Light grey shading indicates the security is not covered. Chart is current as of a date no more than one trading day prior to the date of the report.

BofAS or an affiliate has received compensation for investment banking services from this issuer within the past 12 months: Advanced Micro, Arm Holdings, Intel.

Equity Investment Rating Distribution: Technology Group (as of 30 Jun 2026)  
Intel (INTC) Price Chart  
![](images/069f00e0d8fb0caf84f7ae4c801cbbfd1337a3c8ff57cbf44a55a4602fc65d54.jpg)  
B: Buy, N: Neutral, U: Underperform, PO: Price Objective, NA: No longer valid, NR: No Rating

The Investment Opinion System is contained at the end of the report under the heading "Fundamental Equity Opinion Key". Dark grey shading indicates the security is restricted with the opinion suspended. Medium grey shading indicates the security is under review with the opinion withdrawn. Light grey shading indicates the security is not covered. Chart is current as of a date no more than one trading day prior to the date of the report.

<table><tr><td>Coverage Universe</td><td>Count</td><td>Percent</td><td>Inv. Banking Relationships  $^{R1}$ </td><td>Count</td><td>Percent</td></tr><tr><td>Buy</td><td>243</td><td>60.60%</td><td>Buy</td><td>123</td><td>50.62%</td></tr><tr><td>Hold</td><td>87</td><td>21.70%</td><td>Hold</td><td>45</td><td>51.72%</td></tr><tr><td>Sell</td><td>71</td><td>17.71%</td><td>Sell</td><td>21</td><td>29.58%</td></tr></table>

Equity Investment Rating Distribution: Global Group (as of 30 Jun 2026)

<table><tr><td>Coverage Universe</td><td>Count</td><td>Percent</td><td>Inv. Banking Relationships  $^{R1}$ </td><td>Count</td><td>Percent</td></tr><tr><td>Buy</td><td>1987</td><td>56.11%</td><td>Buy</td><td>1190</td><td>59.89%</td></tr><tr><td>Hold</td><td>797</td><td>22.51%</td><td>Hold</td><td>496</td><td>62.23%</td></tr><tr><td>Sell</td><td>757</td><td>21.38%</td><td>Sell</td><td>391</td><td>51.65%</td></tr></table>

$^{R1}$ Issuers that were investment banking clients of BofA or one of its affiliates within the past 12 months. For purposes of this Investment Rating Distribution, the coverage universe includes only stocks. A stock rated Neutral is included as a Hold, and a stock rated Underperform is included as a Sell.  
FUNDAMENTAL EQUITY OPINION KEY: Opinions include a Volatility Risk Rating, an Investment Rating and an Income Rating. VOLATILITY RISK RATINGS, indicators of potential price fluctuation, are: A - Low, B - Medium and C - High. INVESTMENT RATINGS reflect the analyst's assessment of both a stock's absolute total return potential as well as its attractiveness for investment relative to other stocks within its Coverage Cluster (defined below). Our investment ratings are: 1 - Buy stocks are expected to have a total return of at least 10% and are the most attractive stocks in the coverage cluster; 2 - Neutral stocks are expected to remain flat or increase in value and are less attractive than Buy rated stocks and 3 - Underperform stocks are the least attractive stocks in a coverage cluster. An investment rating of 6 (No Rating) indicates that a stock is no longer trading on the basis of fundamentals. Analysts assign investment ratings considering, among other things, the 0-12 month total return expectation for a stock and the firm's guidelines for ratings dispersions (shown in the table below). The current price objective for a stock should be referenced to better understand the total return expectation at any given time. The price objective reflects the analyst's view of the potential price appreciation (depreciation).

## Investment rating Total return expectation (within 12-month period of date of initial rating) Ratings dispersion guidelines for coverage cluster $^{R2}$

<table><tr><td>Buy</td><td>≥ 10%</td><td>≤ 70%</td></tr><tr><td>Neutral</td><td>≥ 0%</td><td>≤ 30%</td></tr><tr><td>Underperform</td><td>N/A</td><td>≥ 20%</td></tr></table>

$^{R2}$ Ratings dispersions may vary from time to time where BofA Global Research believes it better reflects the investment prospects of stocks in a Coverage Cluster.

INCOME RATINGS, indicators of potential cash dividends, are: 7 - same/higher (dividend considered to be secure), 8 - same/lower (dividend not considered to be secure) and 9 - pays no cash dividend. Coverage Cluster is comprised of stocks covered by a single analyst or two or more analysts sharing a common industry, sector, region or other classification(s). A stock's coverage cluster is included in the most recent BofA Global Research report referencing the stock.

Price Charts for the securities referenced in this research report are available on the Price Charts website, or call 1-800-MERRILL to have them mailed.

BofAS or one of its affiliates acts as a market maker for the equity securities recommended in the report: Advanced Micro, Arm Holdings, Intel, NVIDIA.

BofAS or an affiliate was a manager of a public offering of securities of this issuer within the last 12 months: Intel.

The issuer is or was, within the last 12 months, an investment banking client of BofAS and/or one or more of its affiliates: Advanced Micro, Arm Holdings, Intel.

BofAS or an affiliate has received compensation from the issuer for non-investment banking services or products within the past 12 months: Advanced Micro, Arm Holdings, Intel, NVIDIA.

The issuer is or was, within the last 12 months, a non-securities business client of BofAS and/or one or more of its affiliates: Advanced Micro, Arm Holdings, Intel, NVIDIA.

BofAS or an affiliate expects to receive or intends to seek compensation for investment banking services from this issuer or an affiliate of the issuer within the next three months: Advanced Micro, Arm Holdings, Intel.

BofAS together with its affiliates beneficially owns one percent or more of the common stock of this issuer. If this report was issued on or after the 9th day of the month, it reflects the ownership position on the last day of the previous month. Reports issued before the 9th day of a month reflect the ownership position at the end of the second month preceding the date of the report: Advanced Micro, Intel.

BofAS or one of its affiliates is willing to sell to, or buy from, clients the common eq

[中间内容因长度限制已省略]

ns, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and

employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
