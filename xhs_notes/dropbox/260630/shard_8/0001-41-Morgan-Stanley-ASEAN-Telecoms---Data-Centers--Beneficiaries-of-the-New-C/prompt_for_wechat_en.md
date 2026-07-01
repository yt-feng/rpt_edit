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

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which a

[中间内容因长度限制已省略]

5, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

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
