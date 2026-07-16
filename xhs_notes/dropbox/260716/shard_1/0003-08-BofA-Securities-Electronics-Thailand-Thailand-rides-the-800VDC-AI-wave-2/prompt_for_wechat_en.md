You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Electronics - Thailand

# Thailand rides the 800VDC AI wave

Industry Overview

## AI infrastructure enters its next upgrade cycle

The AI buildout is moving beyond chips. As systems become larger and rack power rises from tens of kilowatts toward 600kW and eventually 1MW-class systems, the bottlenecks are shifting to the infrastructure around the compute. Power delivery, cooling and data movement now need to scale at the same pace as the chips themselves.

## 800VDC and optical connectivity become the next enablers

We see two major technology shifts. 800VDC addresses the power problem by reducing current, copper use and conversion losses as rack power rises. Optical connectivity addresses the data problem as copper becomes harder to scale at higher speeds and longer distances. Together, these changes expand the opportunity beyond GPUs into analog ICs, power semiconductors, power racks, cooling, facility infrastructure and photonics.

## Benefits begin before full 800VDC adoption

Data centers are expected to upgrade gradually, since replacing everything at once would be too costly and disruptive. They start with the most urgent step, improving power equipment around AI racks so these can handle more electricity, then use 800VDC more widely as a more efficient way to deliver power and redesign the facility later. Thailand can benefit throughout this transition, as each stage requires more power electronics, cooling systems, semiconductor assembly, complex PCBs and other supporting hardware already linked to the country's manufacturing base.

## Thailand is better-positioned than it first appears

Thailand is not a leading-edge chip-design or wafer-fabrication hub, but it has a meaningful role in the downstream supply chain. The country already has manufacturing exposure across power electronics, semiconductor assembly and testing, complex PCBs, optical products, storage, transformers and cooling fluids. As more value shifts into the hardware around AI chips, this manufacturing base becomes increasingly relevant.

## Stock implications extend across Thai and foreign equities

For stock implications, we look at all Thai-listed companies that could gain benefit from 800VDC AI wave. Thai names include DELTA, HANA, KCE, SMT, CCET, AMATA, WHA PSP and TRT.

## 14 July 2026

Equity
ASEAN | Thailand
Electronics

Suppapong lemkongaek, CFA, CMT ^^^
Research Analyst
Kiatnakin Phatra Securities
+66 2 305 9925
suppapong.iemk@kkpfg.com

## Narumon Ekasamut ^^^^

Research Analyst
Kiatnakin Phatra Securities
+66 2 305 9086
narumon.ekas@kkpfg.com

## AI: Artificial Intelligence

AC: Alternating Current

DC: Direct Current

AC/DC: Alternating Current to Direct Current

PSU: Power Supply Unit

VRM: Voltage Regulator Module

PDU: Power Distribution Unit

UPS: Uninterruptible Power Supply

ESS: Energy Storage System

BESS: Battery Energy Storage System

SST: Solid-State Transformer

MV: Medium Voltage

LV: Low Voltage

HVDC: High-Voltage Direct Current

800VDC: 800-Volt Direct Current

IBC: Intermediate Bus Converter

BBU: Battery Backup Unit

PCS: Power Conversion System

CDU: Coolant Distribution Unit

DLC: Direct Liquid Cooling

GPU: Graphics Processing Unit

CPU: Central Processing Unit

DPU: Data Processing Unit

NIC: Network Interface Card

HBM: High Bandwidth Memory

PCB: Printed Circuit Board

EMS: Electronics Manufacturing

Services

Si: Silicon

SiC: Silicon Carbide

GaN: Gallium Nitride

Source: KKPS

## Executive summary

Exhibit 1: AI's Two Bottlenecks: 800VDC Power and Optical Connectivity
AI compute growth is pushing demand into power and connectivity, creating new opportunities for Thailand's electronics

![](images/1d9150eb52eea1eb80c6afce08ab463ab5ef10189bced3097c58b0a5ab4505d6.jpg)

BofA GLOBAL RESEARCH

## AI infrastructure is moving into its next bottleneck

AI investment has moved from GPUs to memory and is now reaching a new constraint: the infrastructure around the chips. As AI systems become larger, rack power is rising from tens of kilowatts toward 600kW and eventually 1MW-class systems. At the same time, more chips need to exchange much larger amounts of data. In our view, this creates two parallel upgrade cycles in data centers: 800VDC for power delivery and optical connectivity for data movement.

## 800VDC expands the opportunity across the whole power chain

Traditional data-center power systems were built for much lower rack power. As power rises, pushing more current through the system requires more copper and creates more heat loss. 800VDC addresses this by using higher voltage and lower current, while gradually moving power conversion away from the compute rack toward dedicated power racks and, longer term, facility-level infrastructure. The transition should therefore increase demand across server-board power, PSUs, power racks, cooling, energy storage, protection systems and new technologies such as SSTs and SSCBs. BofA estimates the AI analog semiconductor market will likely grow from US\$7.9bn in CY25 to around US\$28bn by CY30.

## Optics address the second constraint as copper reaches its limits

Power is only one part of the problem. Larger AI systems also require much more data to move between chips and racks. Copper remains suitable for short distances but becomes harder to scale as data rates rise because of signal loss, reach and power constraints. This is driving greater use of optical transceivers, silicon photonics and other optical networking technologies. BofA estimates optical connectivity TAM could reach around US\$88bn by 2030, or roughly 80% of AI connectivity spending.

## Thailand could benefit through downstream manufacturing

Thailand does not need to manufacture the leading AI chip to participate in this cycle. Its opportunity sits in the hardware around the chip, including power electronics, semiconductor assembly and testing, complex PCBs, optical products, storage, transformers and cooling fluids. This gives the Thai electronics sector exposure to both the power and connectivity upgrades discussed in this report.

For stock implications, Thai-listed equities include HANA, DELTA, KCE, SMT, CCET, WHA, AMATA, PSP and TRT.

## AI's insatiable appetite for power

AI investment has moved through distinct waves, each defined by a different bottleneck. The first was the GPU, the engine of AI computation. Attention then shifted to memory, as high-bandwidth memory (HBM) became the constraint on how fast those GPUs could be fed. With each bottleneck addressed, the next has come into view. Today it is the electricity these systems consume, and the heat that comes with it.

A single rack of Nvidia's newest AI servers will soon draw more electricity than a thousand American homes. A standard server rack draws 10 to 15 kilowatts, closer to what a dozen homes use. The gap is nearly a hundredfold, and it points to where the AI race is really headed. It is not a contest for chips so much as a contest for power.

Exhibit 2: Rack power across Nvidia generations

Power capacity per rack (kilowatts) across various generations of Nvidia platforms vs. a traditional server rack

![](images/d789143254cbac924c14aa96cbeb188f77839378722683dafb5040c486a67692.jpg)  
Source: BofA Global Research estimates, Nvidia, Company reports  
BofA GLOBAL RESEARCH

The power demand is no longer just about the GPU. As AI evolves, it needs more types of work to be done. First, AI is trained (this means building the model). Then it is used to answer questions (this is called inference). Now, AI is also starting to handle more complex tasks, where it breaks a problem into steps and uses tools to solve it.

Because of this, the system needs more supporting parts. These include CPUs (which manage and control the system), switches (which move data between chips), network cards (which connect the system to other machines), and memory (which stores data close to where it is used).

The GPU remains the main compute engine, but it cannot work efficiently without this surrounding hardware. In the densest configurations, networking switches alone can account for close to one-fifth of total rack power. The implication is that AI power demand is becoming a full-rack issue, not just a GPU issue.

Exhibit 3: Nvidia power budget analysis
Power budget broadens across the rack

<table><tr><td>Component (in kW)</td><td>H100(2022)</td><td>GB200Blackwell(2024)</td><td>Vera Rubin(2026)</td><td>Rubin Ultra(2027)</td><td>Feynman (2028+)</td></tr><tr><td>GPU</td><td>22.4</td><td>86.4</td><td>129.6</td><td>518.4</td><td>1036.8</td></tr><tr><td>CPU</td><td>2.4</td><td>10.8</td><td>12.6</td><td>25.2</td><td>100.8</td></tr><tr><td>Switch</td><td>3</td><td>14.4</td><td>19.8</td><td>54.5</td><td>288</td></tr><tr><td>NIC</td><td>0.8</td><td>1.8</td><td>2.2</td><td>4.3</td><td>28.8</td></tr><tr><td>DPU</td><td>0.2</td><td>1.4</td><td>2.7</td><td>5.4</td><td>28.8</td></tr><tr><td>Overhead</td><td>2.7</td><td>6</td><td>9.7</td><td>37.8</td><td>51.4</td></tr><tr><td>Total Rack Power</td><td>32</td><td>121</td><td>177</td><td>646</td><td>1535</td></tr></table>

Source: BofA Global Research estimates, Nvidia  
BofA GLOBAL RESEARCH

At a basic level, the constraint comes from physics. AI chips need to exchange data at very high speed, but copper links can only carry that data over short distances. To make the system work as one large compute engine, vendors have to place more AI accelerators, CPUs, networking chips and memory closer together. Performance therefore comes from higher rack density, and higher rack density comes with more power and heat.

Nvidia's move from Hopper (old generation chip model) to Blackwell (new generation chip model) shows the trade-off. Rack power density increased by more than 3x, while system performance improved by roughly 50x. The performance gain is large, but it is achieved by packing more compute and networking hardware into the same rack.

This trend is not limited to Nvidia. AMD's latest accelerators are also moving toward 1,400-1,800W per chip, pushing rack power above 100kW. In-house ASICs from Google and Amazon may be more efficient for specific workloads, but their total rack power is also rising as systems scale. Higher power density is therefore an industry trend, not an Nvidia-specific issue.

Exhibit 4: Power consumption of other merchant GPUs and custom ASIC platforms Rising power is industry-wide, not just Nvidia

<table><tr><td>Company</td><td>Platform</td><td>Chip</td><td>Per-Chip Power (W)</td><td>Total Rack Power (kW)</td></tr><tr><td>Nvidia</td><td>Vera Rubin NVL144</td><td>Rubin</td><td>1800</td><td>177</td></tr><tr><td>AMD</td><td>Helios</td><td>MI400X/MI455X</td><td>2000</td><td>173</td></tr><tr><td>AMD</td><td>MI350X rack</td><td>MI355X</td><td>1400</td><td>107</td></tr><tr><td>AWS</td><td>Trainium 3 UltraServer</td><td>Trainium 3</td><td>1000</td><td>100</td></tr><tr><td>Google</td><td>Ironwood Cube</td><td>TPU v7</td><td>1000</td><td>79</td></tr><tr><td>Intel</td><td>Gaudi rack</td><td>Gaudi 3</td><td>1000</td><td>51</td></tr></table>

Source: BofA Global Research estimates, AMD, Intel, AWS, Google, Nvidia  
BofA GLOBAL RESEARCH

The implication for data centers is that buying more chips is no longer enough. Each rack must receive far more power than before, and the traditional power-delivery chain is reaching its practical limits. This is where the case for 800VDC begins.

## Why does the world need 800VDC?

The case for 800VDC starts with a simple equation: power equals voltage times current, or $P = V \times I$ .

Power is what the rack needs. Voltage is the pressure that pushes electricity through the system. Current (or intensity) is the amount of electricity flowing through the conductor. When rack power rises, either voltage or current must rise with it.

For many years, data centers could rely on the existing low-voltage architecture and simply push more current through the system. That worked when racks consumed tens of kilowatts. It becomes much harder when AI racks move toward hundreds of kilowatts and eventually megawatt-class power.

## Exhibit 5: Power equation

Higher power consumption will end with higher voltage

Power = Voltage x Intensity

![](images/91e7b8283cfc56451f93d2c1a3fa0379db83b69bf6b3f2337d4dd5feddefcc1b.jpg)

More Power = More Current

Problems: ① Copper Mass ② Heat Loss

That's why V needs to increase and the world wants 800VDC

## Source: KKPS

BofA GLOBAL RESEARCH

The first problem is copper. Higher current needs larger conductors, busbars and connectors. At 600kW, a legacy 48V architecture would require around 12,500 amps of current. At that level, the copper busbar can become extremely large and heavy. This is difficult to fit inside the rack and expensive to scale across a large data center.

The second problem is heat loss. Electrical losses rise with the square of current. In simple terms, doubling current can increase heat loss by around four times. This wasted energy does not create compute output. It becomes heat that the data center must remove.

800VDC solves this by raising the voltage. For the same amount of power, higher voltage means lower current. A 600kW rack at 800V requires only around 750 amps, compared with around 12,500 amps at 48V.

## Exhibit 6: Benefits of 800VDC for the system

800VDC results in less copper and less heat

<table><tr><td></td><td>Old way (54V)</td><td>New way (800VDC)</td><td>What this means?</td></tr><tr><td>Voltage sent through the data center</td><td>Low (54 volts)</td><td>High (800 volts)</td><td>Higher voltage moves the same power with less current</td></tr><tr><td>Electrical current (flow through the wire)</td><td>Very high</td><td>Much lower</td><td>Current is what creates copper bulk and heat, so less current fixes both</td></tr><tr><td>Copper wiring needed</td><td>Heavy, up to 200kg per rack</td><td>About 45% less</td><td>Thinner wires, less copper</td></tr><tr><td>Energy wasted as heat</td><td>High</td><td>Over 10x lower</td><td>Less wasted power</td></tr><tr><td>Bottom line</td><td>Breaks down past a few hundred kilowatts</td><td>Scales to 1MW racks and beyond</td><td>The only practical way to power today&#x27;s racks</td></tr></table>

Source: BofA Global Research, Nvidia white paper  
BofA GLOBAL RESEARCH

## The benefits of 800VDC can be explained in a simple sequence.

First, lower current means smaller conductors, lighter busbars and easier rack design. This reduces material usage and makes large-scale deployment more practical.

Second, electrical losses rise with the square of current. By reducing current, 800VDC significantly cuts power loss and waste heat in the power-delivery chain.

Third, this architecture is built for the next phase of AI scaling, where racks move from around 100kW today toward 600kW, 1MW and beyond, providing a clear path to expand infrastructure without hitting physical limits.

Fourth, today's power chain includes several conversion stages before electricity reaches the GPU. By reducing redundant conversion steps, 800VDC can improve end-to-end efficiency.

A simpler power chain also means fewer components and fewer failure points, which can reduce maintenance cost and improve total cost of ownership.

This is why 800VDC is not just a new electrical standard. It is the practical response to rising AI rack power. It does not make GPUs consume less energy. It makes that energy easier to deliver, with less copper, less heat loss and a power architecture that can scale with future AI racks.

## The path to 800VDC: A three-stage transition

Today's AI data centers are not expected to switch directly to facility-wide 800VDC. Instead, the industry is likely to transition through three stages, with the key change being that power conversion gradually moves further upstream as rack power continues to increase.

## Phase 1: Traditional AC architecture (today)

Today's data centers still follow conventional power architecture. Electricity enters the facility as AC power, passes through transformers, backup systems and power distribution equipment before reaching the compute rack. Inside the rack, AC is converted into DC and then stepped down multiple times to supply the low voltages required by GPUs.

This architecture was designed for much lower rack power. As AI racks approach hundreds of kilowatts, concentrating power conversion inside or near the compute rack consumes valuable rack space, generates additional heat and increases conversion losses. According to BofA, this architecture delivers end-to-end power efficiency of around 87.6%. See our report: Technology - Asia Pacific: HVDC for Rubin Ultra; Delta's solid R&D & position to enjoy content/shipment growth 24 November 2025.

## Phase 2: Power-rack architecture (expected next step)

The first step toward 800VDC does not require rebuilding the entire data center. Instead, the main AC/DC conversion is relocated from the compute rack to a dedicated power rack positioned nearby. The existing facility infrastructure remains largely unchanged, while the power rack converts 480V AC into 800VDC before distributing power to the compute racks.

This intermediate architecture is attractive because it removes bulky conversion equipment from the compute rack, freeing up space for AI hardware while reducing heat generation close to GPUs. Since most of the upstream electrical infrastructure can remain intact, it is considerably easier to retrofit into existing facilities. BofA estimates that end-to-end efficiency improves to approximately 89.1%.

## Phase 3: Full facility-level 800VDC architecture (longer term)

The final stage shifts power conversion even further upstream. Rather than distributing 480V or 415V AC throughout the facility, medium-voltage AC is converted directly into 800VDC and distributed across the entire data center with fewer conversion stages.

This architecture relies on Solid-State Transformers (SSTs), which combine wide-bandgap power semiconductors with high-frequency transformers to convert medium-voltage AC into regulated DC while improving efficiency, power quality and system control.

Although this delivers the cleanest and most efficient power architecture, it also requires the greatest redesign. Existing data centers would need new protection systems, safety standards and facility-level power equipment capable of handling high-voltage DC. SSTs themselves must also meet stringent requirements for high power, reliability and cost, making this a longer-term transition. BofA estimates end-to-end efficiency improves further to around 92.1%.

![](images/60d7f21c14b6150501c5a2c0d03cfc3e4febe971cfc9b310adaf233a6dc48269.jpg)

![](images/80e05d6fa8dd0ee277aee32c54c53ce8e686

[中间内容因长度限制已省略]

ons, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

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
