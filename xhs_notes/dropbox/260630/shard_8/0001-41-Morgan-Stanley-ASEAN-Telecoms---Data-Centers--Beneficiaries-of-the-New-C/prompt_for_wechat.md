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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
![](images/769d01335e1eb576bb53053fa7cfc432b4248775c2fda88349ec4ec20039e335.jpg)

June 29, 2026 12:00 AM GMT

Investor Presentation | Asia Pacific

# ASEAN Telecoms & Data Centers: Beneficiaries of the New Computing Paradigm

We are at a historic inflection in AI infrastructure build-out, driven by Nvidia GPUs and the rise of agentic AI frameworks like OpenClaw. ASEAN sits at a unique intersection of this megatrend: abundant land, competitive power, strategic subsea cable connectivity. and growing sovereign AI mandates.

This presentation provides investors with a practical “Data Centers 101,” including AI data centers’ anatomy and economics, the value chain, Singtel’s AI infrastructure positioning, and the potential emergence of orbital data centers as a long-tail disruptor.

## Related Report:

ASEAN Telecoms and Media: Beneficiaries of New Compute Paradigm (19 Mar 2026)

MS ASIA (SINGAPORE) PTE.+

Da Wei Lee
Equity Analyst
Dawei.Lee@morganstanley.com

+65 6834-6510

Asia Summer School 2026

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

![](images/6667d6bbf2244e90a95ee829f5d22d5a922a7cd8e8c85b56bcca5eaf622b4282.jpg)

## Data Centers: Transforming Power into Computing

Scarce inputs
Land, grid interconnect, power price, water, permits and fiber access.

Facility layer
Shell, substations,
UPS, generators,
cooling and physical
security.

IT layer

Racks, servers, GPUs, storage, switching and customer workloads.

Monetization
MW leased, price per kW, power pass-through, cross-connects and services.

1. MW is the core capacity unit, but revenue is a function of leased load, price, power structure, and utilization.

2. AI shifts the bottleneck from space to power density, cooling, and networks.

3. Equity exposure is a supply chain, not only data center landlords.

24x7

![](images/58a519bbfda59d0427e18544bf667fe673d24e16733cd8fd570103c4d65c2950.jpg)

Mission-critical workload expectation

Primary capacity unit sold or built

KPI bridge

Capacity → Leasing → Utilization → EBITDA → ROIC

Source: MS.

Revenue depends on contracted capacity, billing model, power pass-through, ramp schedule, interconnection services. and customer mix.

PUE

ROIC

Efficiency bridge between IT load and site power

The investor lens on growth capex

Power train

## Data Centers: The DC Anatomy

A data center is not just a shell building.
It is a tightly engineered system that makes IT equipment reliable, dense and connected.

![](images/f467158434d8131798976b86e527e110bae876572296ccdb85a91afe9d14c69c.jpg)

![](images/621bd9f1253f954a1b6ee35b347f5b4154b56e248736812dede7ce6ddc796d67.jpg)  
UPS cabinets, batteries, switchgear and generators bridge grid outages and keep racks online.

![](images/186d3a36e2d329b17f038239ff434bcf5ac82d266bc867ac071fbad4a9b5db39.jpg)

![](images/25363caf427256c4ec123da1d672d9f1fd899a29b84bf3c20165a81dd04b5a39.jpg)  
Connectivity
Meet-me rooms, fiber, cross-connects and cloud on-ramps make the facility valuable to tenants.  
Thermal management
Chillers, CRAH/CRAC units, airflow containment and liquid loops remove heat from dense racks.

![](images/0b6543ce3386868837333f1f7479ae2a2d4dbb54543dd1adff9abaf571ab5505.jpg)  
Controls & security  
24x7 monitoring, access control, fire suppression and SLAs protect uptime and compliance.  
The hardest assets to replicate are often power access, cooling design, network density, and operating track record – not the building shell.  
Source: MS.

Data Centers: Workload Management  
![](images/7937961144b008142be714c81bc4a55778e1b1a03c8839a03fb5097fbbae894e.jpg)

![](images/63be5d5fdffd76f8c4361948db8efe9c0899cc6f765d24f6412b25ec24b3a4d3.jpg)  
Latency tolerant / Low Power Density

Source: MS.

![](images/f790b31f366f08475fa2027c6f94fc8b26392e1f4aebda0e63285e5ae00d579e.jpg)

AI inference

![](images/c45273fde970217c38a6393cd6a80d56660eebb863584805ddcf376e68923645.jpg)  
AI training

## Why this matters

Different workloads imply different siting logic, contract structures, and capex intensity.

AI training can be centralized near cheap power. Inference is more latency-sensitive and may favor regional hubs closer to users and data sovereignty zones.

Do not treat every MW as equal. A leased AI-ready MW may require a very different capex and cooling spec.

Higher Power Density

Data Centers: Business Models

<table><tr><td>Retail colocationMany enterprise customers</td><td>Operator sells smaller blocks plus connectivity. Higher interconnection revenue; more operational complexity.</td><td>Power/cooling</td><td>Security</td><td>Cross-connects</td></tr><tr><td>Wholesale colocationLarge tenants / hyperscalers</td><td>Operator sells MW-scale suites or buildings. Longer leases; lower customer count; pre-leasing matters.</td><td>Large MW suites</td><td>Long leases</td><td>Ramp schedules</td></tr><tr><td>Build-to-suit / hyperscaler-ownedSingle tenant or owner-operated</td><td>Hyperscaler controls design and capex. Third parties may provide land, power shells or JVs.</td><td>Tenant design</td><td>Custom power</td><td>Dedicated campus</td></tr><tr><td>GPU cloud / AI factoryCompute as a service</td><td>Provider controls facility and GPUs, then sells ca or API/compute access to enterprises and AI labs</td><td>GPUs</td><td>Orchestration</td><td>AI services</td></tr></table>

Source: MS.

## ASEAN Data Centers: Formation of Data Center Clusters

## Connectivity

Fiber routes, subsea cables, cloud on-ramps

## Power

Availability, price, reliability, emissions

## Demand

Enterprises, cloud regions, data sovereignty

## Policy

## Land

tax incentives, permitting, regulation

Campus scale, zoning, noise buffers

## Climate

Water, ambient temperature, natural disasters, wars

The best locations maximize connectivity and customer access while minimizing power, land and permitting risk.

Source: MS.

## ASEAN Data Centers: Singapore Is a Submarine Cable Hub

![](images/c0252e7867484333f66825c04672c11ef787657b2987e4017bb16435f748eedf.jpg)  
Source: TeleGeography, MS.

## ASEAN Data Centers: Key Changes in the Stack

## Power density moves from room-level planning to rack-level thermodynamics

Traditional enterprise rack

5-15 kW

GPUs / accelerators

Compute engines

AI GPU rack today

40-200 kW

Next-gen AI platforms

hundreds of kW+

HBM memory

Model state + throughput

High-speed networking

Cluster scale-out

Cooling progression for higher density racks

Air

Direct-to-chip

Immersion

Power distribution

High-current delivery

Liquid cooling loop

Heat removal

## Training

Massive, centralized clusters; economics tilt toward cheap power, high utilization and low-latency intra-cluster networking.

## Inference

Workloads can be more distributed; latency, data sovereignty and proximity to enterprises matter more.

The winners are not only builders of square footage. They are operators with secure power, liquid-cooling expertise, dense fiber and customers willing to commit to high-density capacity.

Source: MS.

## ASEAN Data Centers: Rise of the New Computing Paradigm

## Evolving AI Hardware Stack

![](images/cbf55c202440813ac14c814e80d1c8b8c6864e63e3716a41c590a57338907a26.jpg)

## Surge in Global Hyperscalers' Capex

![](images/88e14be9fde940f0817f5461011490f14e931ffbdf891c9d24d565fd998badf3.jpg)

## Rise of Agentic AI

![](images/a68ad63622ed583156e5cc65283e62a485638ad8fd250791cc34a396b84e07cc.jpg)  
Source: Company data, MS.

US-China- Tech Diffusion Cycle  
![](images/3477baade9f95f4cc0888c6fe10fb004ce7dd2f04c41671a4cf75ca59746b670.jpg)

![](images/3aabb40806168325b74ab19f258883f39762732f02c65c10490307a74eba558d.jpg)

## ASEAN Data Centers: Global AI Infrastructure Supply Chain Players

![](images/acf60d8cf5428312773072c340fdc80420e4ab12c95af44596652ec34afd2d65.jpg)

## AI Applications

![](images/5bf4aa3242fb0d6fa6c5ac7d3806e40710e471a1b4020fe5d59ea453f6a2e5bf.jpg)

## Data Center Value Chain

## Power Generation

## Fossil Baseload

\- Gulf (TH) - J-Power (JP)
- GPSC (TH) - Shikoku Electric (JP)

\- Sembcorp (SG) - Chugoku Electric (JP)
- KEPCO (KR) - Tohoku Electric (JP)

## Clean Power

\- Gulf (TH)
- GPSC (TH)

\- Origin Energy (AU)
- AGL Energy (AU)

\- Sembcorp (SG)

## Nuclear

• J-Power (JP)

• Shikoku Electric (JP)

\- Chugoku Electric (JP)

• Tohoku Electric (JP)

## Power Equipment

• GE Vernova (US)

• Simens Energy (US)

\- Bloom Energy (US)

\- Doosan Enerbility (KR)

Source: TeleGeography, MS.

## Grid + Energy Storage

## Grid Operators

• Tenaga (MY) • Shikoku Electric (JP)

\- Chugoku Electric (JP)

\- APA Group (AU)
- Chugoku Electric (JP)
- Tohoku Electric (JP)

## Batteries

\- CATL (CH)
- BYD (CH)

• LG Energy (KR)

\- SK Innovation (KR)
- Samsung SDI (KR)
- Panasonic (JP)

## Grid Equipment

\- XJ Electric (CH)

• NARI Tech (CH)

• LS Electric (KR)

## Commercial Applications

## Hyperscalers

\- Google (NA)

\- Microsoft (NA)

\- Meta (NA)

\- Amazon (NA)

Localisation

• Gulf (TH)

\- SEA (SG)

\- Grab (SG)

## Data Center

## Hyperscalers

\- Tencent (CH)
- Amazon (NA)
- Google (NA)
- Microsoft (NA)
- Oracle (NA)

## Data Center Technology

## Server

## Processor

## System Brands / End User Devices

\- Apple
- Google
- Microsoft
- Meta
- Tesla
- AWS
- Dell
- HP
- Supermicro

## Semi Production

## Integrated Device Management (IDM)

## 1. IC Design

\- Nvidia (NA)
- MediaTek (TW)
- Aspeed (TW)

## • SK Hynix (KR)

## 2. Foundries

• TSMC (TW)
• Samsung (KR)

## Design Services

• Andes(TW)
• GlobalUnichip (TW)

## Equipment

• AlChip (TW)

\- ASE (TW)
- KYEC (TW)

• Verisilicon (CH)

## Colocation

## 3. Outsourced Semi Assembly & Test

• Disco(JP)

\- Equinix (NA) - Keppel DC (SG)
- GDC (CH) - Gulf (TH)

## DC Operators

• Advantest (JP)

• ASM Pacific (HK)

\- FII (CH)
- Quanta(TW)
- Wistron (TW)
- Wiwynn (TW)
- Giga-Byte (TW)
- Lenovo (HK)

## ODM/EMS

## Server Components

## Power Supply

\- Delta (TW)
- Lite-On tech (TW)

## Printed Circuit Board

• Gold Circuit (TW)
• Shennan (CH)

## Thermal Solution

\- Asia Vital Components (TW)
  - Sunonwealth (TW)
  - Auras (TW)

## Passive Component

\- Yageo (TW)

## Sovereign AI

\- AIS (TH)

\- Singtel (SG)

\- Telkom (ID)

• Telkom Malaysia (MY)

## Telcos

\- Singtel (SG)
- Globe (PH)
- Telcom (ID)
- AIS (TH)

## Network

• Nvidia InfiniBand (NA)

## Switch

\- Arista (NA)
- Juniper (NA)

## DCI (Routing/Optical)

• Juniper (NA)

\- Cisco (NA)

• Ciena (NA)

• Infinera (NA)

## Others

\- Venture (SG)

## Memory/Storage

\- Western
Digital (NA)
- Seagate (NA)
- SK Hynix (KR)
- Micron (NA)

## Transceiver

\- Innolight (CH)

• Eoptolink (CH)

\- Landmark (TW)

• TFC Optical (CH)

## Enterprise

\- Meta (NA)
- SEA (SG)
- SAP (NA)

## Internal Power

Uninterruptible Power Supply (UPS)
• Delta (TW)
• Huawei (CH)
• Mitsubishi Electric\* (JP)

## Power Electronics

\- Mitsubishi Electric\* (JP)
  - Delta (TW)

## Cooling

## Liquid Cooled

• Non-covered/private\*: XYL, Asperitas, Submer, TT, LiquidStack, VRT, Green Revolution,

## Air Cooled

\- Mitubishi Electric (JP)
- Daikin (JP)

• Schneider Electric (EU)

## ASEAN Data Centers: Emerging AI Infrastructure Hub

## Global DC Market Growing Double-Digits

![](images/91d5654b38588c1a7a307009c7e3f050e0e1d397c9c4d4c2b95223c3992a7649.jpg)

## US Remains Most Saturated DC Market

Global DC Market (MW per mn pop)  
![](images/e01942e790a8e21c8cd0e84c319a5f59c29ea43fba7887d65787af8ad39cae5b.jpg)

## MY>TH>SG in terms of DC Capacity

ASEAN DCs Capacity (MW)  
![](images/4da97e5d050964b799c89efcdbca37d06fe14142ec02f2f28af8d02b1740ac22.jpg)  
Source: Company data, MS.

## Singapore Remains Most Saturated DC Market

ASEAN DCs MW per pop (mn)  
![](images/8bad9a10c9ba232d056e2fa6496f8f085b2b73b57b1e040331c1ee5547724251.jpg)

## ASEAN Data Centers: Singtel's AI Factory Stack

## Integrated stack: more than colocation

Four layers that convert regional connectivity and capacity into AI workloads.

Orchestration

Paragon

Platform layer to coordinate AI workloads, networks and enterprise deployments.

GPUaaS & AlaaS

RE:AI

On-demand GPU capacity and AI services, with NVIDIA ecosystem access and partner reach.

AI DC platform

Nxera

High-density, sustainable and AI-ready campuses in Singapore, Thailand, Indonesia and Malaysia.

Connectivity

Network Fabric

APAC telco, subsea and edge connectivity for low-latency AI adoption.

Enabled outcome: sovereign AI applications and enterprise workflows

## Investor read-through

Why the stack matters for monetization, customer capture and differentiation.

## Move up the value chain

Beyond wholesale colo: adds GPUaaS / AlaaS, orchestration and managed AI services.

## Sovereign AI wedge

Targets government and regulated enterprises needing local, secure AI infrastructure.

## Replicable playbook

JVs combine Singtel blueprint + NVIDIA platform with local power, land and telco partners.

## Connectivity advantage

Telco networks, subsea cables and edge locations create a low-latency demand funnel.

Source: Company data, MS. Note: We have not included STT GDC's contribution in Singtel's Digital Infraco

## ASEAN Data Centers: Singtel – The Leading AI DC Platform

## Singtel's First Phase Organic Pipeline

![](images/4ae38879ed4ace5cd48efc06b58f6d2f21200a8e850f611274b7d8857dce18f8.jpg)

## Singtel's Digital Infraco's EBITDA grow $>30\%$

![](images/ebc16fa3c49cae00c33a9cb40e3e3d250ca465543e8177b6d6e94d33ea7a236b.jpg)

## Singtel's Digital InfraCo to be $>10\%$ of SOTP

Digital InfraCo Enterprise Valuation  
![](images/457536c96e07b820fb535ee542c39392e1c01dfd32f76887e587a061fcebcd62.jpg)

Singtel's Digital InfraCo Not Priced In  
Value of Associates vs Singtel's EV  
![](images/f00313fdbfa847fb1245d5d0faf9232c98bb7607f561273bb82aebef65e114c9.jpg)  
Source: Company data, MS. Note: We have not included STT GDC's contribution in Singtel's Digital Infraco

## ASEAN Data Centers: Singtel Scaling through Acquisition of STT GDC

## Overview of STT GDC

Operational scale and footprint acquired by the consortium.

50 data centers \~673MW in operation

12 markets

## Footprint by market

Operational count / presence; asterisk = upcoming or pipeline market.

India 23

UK 11

Singapore 6

Philippines 5

Thailand 2

Japan 1

Vietnam 1

Indonesia 1

Malaysia\*

Germany\*

Italy\*

S. Korea\*

## Capacity / footprint bridge

A fast path from regional pipeline to a global AI data-center platform.

Nxera base

STT operating

>400MW medium-term pipeline

STT pipeline

+673MW current capacity +\~1.7GW pipeline across markets

Combined platform

\~2.8GW design capacity / 12 markets

## Transaction snapshot

EV S\$13.8bn; S\$6.6bn cash for 100% of STT GDC. Singtel contributes S\$740mn for 25% stake.

Equity-accounted; no dividend impact. Expected close in 2H26 per management.

Additional Singtel capex: \~S\$400-500mn over the next three years.

## Why it matters for Singtel

Capacity access: scarce operating MW + pipeline

\- Customer base: global hyperscalers and blue-chip enterprises

\- Footprint: 12 markets anchored by SG, India and UK

Value read-through: \~4% Singtel EV uplift based on MSe

Strategic read-through: access to constrained capacity, multi-market customer relationships and geographic optionality, while retaining a partnership-led model.

Source: Company data, MS.

Hardware in orbit

## ASEAN Data Centers: Moving Computing to Space

## Think small GPU satellites/modular computing containers linked optically

![](images/8ec1baeb4227c52e7389b77f80556249a35f8ff21469f3f4e565a398478890df.jpg)  
H100-class GPU demonstrator  
2

Launch & deploy  
![](images/4ecc2d1093562975c3f198e8a5b51af715c07c871690aebd7d428c2b6854b956.jpg)  
Reusable rockets + rideshare missions  
3 Modular computing

![](images/9866296e89a4403ef8b36e02672ab950260e648509357cda05188117c0d3698e.jpg)  
GPU containers dock to power/cooling

4 Long-term scale  
![](images/66ef161683f4b181d406843d349e410f44944e0832e120dcbde31f36d307a9a1.jpg)  
Distributed nodes first; GW platforms later

## Why space?

Terrestrial bottleneck is power. Orbit offers abundant solar energy and radiative heat rejection.

## What has to work?

Launch cost, radiation shielding, thermal design, orbital debris, security and replacement cycles.

## Investor framing

A long-duration call option on AI power scarcity — not a near-term substitute for terrestrial DCs.

Core idea: move the demand source (computing) closer to abundant solar power instead of bringing scarce power to computing.

## ASEAN Data Centers: Key Diligence Checklist

## Ten questions to ask before underwriting data center-driven earnings growth

Capacity bridge What is operational, under construction, power-secured and merely planned? Cooling What rack density can the facility support today and after retrofit?
Power What grid connection dates, PPAs, redundancy design and utility dependencies are in place? Utilization How long from commissioning to stabilized EBITDA?
Leasing How much is pre-leased, to whom, for how long, and with what ramp schedule? Funding How are projects financed - balance sheet, JV, project debt, asset recycling?
Pricing Is billing per kW, per kWh, shell-and-power, or bundled service? Is power passed through? Customer risk What is tenant concentration and credit quality?
Capex/MW What is the all-in cost per MW and how exposed is it to electrical/cooling equipment inflation? Returns What is the stabilized EBITDA, ROIC and downside if leasing is delayed?

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Regi

[中间内容因长度限制已省略]

nal Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
