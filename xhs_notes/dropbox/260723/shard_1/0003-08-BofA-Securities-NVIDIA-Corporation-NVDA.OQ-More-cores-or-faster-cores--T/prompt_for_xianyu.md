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
FUNDAMENTAL EQUITY OPINION KEY: Opinions include a Volatility Risk Rating, an Investment Rating and an Income Rating. VOLATILITY RISK RATINGS, indicators of potential price fluctuation, are: A - Low, B - Medium and C - High. INVESTMENT RATINGS reflect the analyst's assessment of both a stock's absolute total return potential as well as its attractiveness for investment relative to other stocks within its Coverage Cluster (defined below). Our investment ratings are: 1 - Buy stocks are expected to have a total return of at least 10% and are the most attractive stocks in the coverage cluster; 2 - Neutral stocks are expected to remain flat or increase in value and are less attractive than Buy rated stocks and 3 - Underperform stocks are the least attractive stocks in a coverage cluster. An investment rating of 6 (No Rating) indicates that a stock is no longer trading on the basis of fundamentals. Analysts assign investment ratings considering, among other things, the 0-12 month total return expectation for a stock and the firm's guidelines for ratings dispersions (shown in the table below). The current price objecti

[中间内容因长度限制已省略]

he extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and

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
