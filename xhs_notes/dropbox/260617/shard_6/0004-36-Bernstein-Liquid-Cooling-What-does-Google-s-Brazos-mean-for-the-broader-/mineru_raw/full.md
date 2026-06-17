# U.S. Multi Industry & Electrical Equipment

# Liquid Cooling: What does Google's Brazos mean for the broader CDU ecosystem?

![](images/525fff8d4371ff18c2f54fbaf4fb61631ddf53d598066a60042f55babe97e04e.jpg)

Varun Govindaraj

+19173448543

varun.govindaraj@bemsteinsg.com

![](images/94668d6524268dae327f9bddfa44559aa56979487d3e665c8deac543f3074181.jpg)

Chad Dillard

+19173448469

chad.dillard@bernsteinsg.com

![](images/e74941676de997deb2fb7986016fbba2c48636da842597bfd2629a09ce48685b.jpg)

Alasdair Leslie

+44 20 7762 4952

alasdair.leslie@bernsteinsg.com

![](images/24bb9817d82ab5cdb363cba5bb99fdfe73b9f77a122daa5086d10422588cc8b3.jpg)

Madison Rezaei

+19173448622

madison.rezaei@bernsteinsg.com

## Specialist Sales

![](images/9461c6306ed343985afae7d2fd63e51991e6e9c334b1816239374979cd25fec4.jpg)

Steve Song

+19173448401

steve.song@bernsteinsg.com

Google recently released early specifications for a liquid-to-air (L2A) CDU named "Brazos". Like project "Deschutes" that came before it in 2025, Brazos simply announces a CDU reference design for the Open Compute Project's vendor ecosystem (which counts Vertiv, nVent, and Boyd as members) to produce. It is not a competing product to Vertiv/Boyd/nVent/Motivair's existing L2A CDU lines that Google will manufacture; hyperscalers are not in the business of making this equipment.

Prima facie, the specifications on Brazos-class CDUs seem relatively low. At 60kW of cooling capacity, it cannot even cool one Blackwell rack (which requires \~120kW of cooling capacity). Interestingly, Brazos-class CDUs are designed to draw DC power (vs. many other L2A CDUs that are designed for AC power instead).

We believe these CDUs are designed to be OCP compliant, and fit into legacy hyperscaler deployments which tend to have DC power infrastructure already. The cooling capacity of 60kW does not work well for frontier training models, but can support inference at that range. Given concerns around how quickly data center capacity can get up and running, creating an inference ecosystem that can run in existing facilities with simple L2A CDU retrofits seems like a good move (especially when inference looks set to grow faster than training through 2030). While not explicitly stated, we infer that this is the primary purpose of the Brazos project.

While hard to quantify, we see two mid-term risks for CDU manufacturers. First, there is real commoditization risk of the inference CDU ecosystem. Brazos specs are meaningfully easier to deliver than Deschutes. While there will be a service attach, margins will be lower vs. flagship training CDUs. The deciding factor here is inference rack densities; we are unsure what this looks like for purpose-built inference silicon from hyperscalers. If it remains around 60 kW/rack, then a meaningful share could be cooled by L2A Brazos-style CDUs. If not, larger Deschutes-class CDUs will be needed instead (which we would expect have higher margin and stickier service attach).

Second, we may also see some hyperscaler demand shift from greenfield to retrofits, especially if projects get delayed. While we do not see that in stranded capacity numbers in our data center capacity tracker, there has been some anecdotal input from companies that they are seeing a few customers (both hyperscalers and colos) push out deliveries because of a lack of readiness / project delays. We're not saying this WILL happen, but we think having these standardized L2A CDUs creates optionality for hyperscalers if they need to accelerate retrofits to meet inference demand in the future.

We do not view this announcement by Google as imminently alarming for CDU manufacturers, especially those that focus on technical excellence at the top of the stack. Some level of CDU commoditization was always expected by the market. While we think this announcement accelerates the commoditization trend for lower spec. products, we still believe an innovation premium exists for flagship CDUs, and expect it to continue as top-tier liquid cooling technology evolves.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">16 Jun 2026</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>VRT (Vertiv)</td><td>O</td><td>USD</td><td>299.60</td><td>416.00</td><td>132.8%</td><td>USD</td><td>4.20</td><td>6.52</td><td>9.21</td><td>71.4</td><td>45.9</td><td>32.5</td></tr><tr><td>NVT (nVent)</td><td>O</td><td>USD</td><td>167.34</td><td>218.00</td><td>113.2%</td><td>USD</td><td>3.34</td><td>4.79</td><td>6.19</td><td>50.0</td><td>34.9</td><td>27.0</td></tr><tr><td>SU.FP (Schneider)</td><td>O</td><td>EUR</td><td>276.95</td><td>310.00</td><td>7.3%</td><td>EUR</td><td>8.43</td><td>10.22</td><td>11.95</td><td>32.9</td><td>27.1</td><td>23.2</td></tr><tr><td>ETN (Eaton)</td><td>O</td><td>USD</td><td>407.71</td><td>534.00</td><td>(3.9)%</td><td>USD</td><td>12.07</td><td>13.29</td><td>16.32</td><td>33.8</td><td>30.7</td><td>25.0</td></tr><tr><td>SPX</td><td></td><td></td><td>7,511.35</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,577.98</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Vertiv Outperform with a target price of \$416.

We rate nVent Outperform with a target price of \$218.

We rate Schneider Outperform with a target price of €310.

We rate Eaton Outperform with a target price of \$534.

## DETAILS

## Context

Hyperscalers have historically pushed the "Open Compute Project" or OCP, a non-profit that published open-source specifications for data center hardware. Founded by Meta, it now has participation from Google, Microsoft, and Oracle (although Amazon is a notable missing name) and a host of other vendors. In 2025, Google published details of Project Deschutes as a part of the OCP; this was a set of technical specifications and standards for compliant Liquid to Liquid (L2L) CDUs (with 2MW of cooling capacity at a $3^{0}\mathrm{C}$ approach temperature). Vertiv, nVent, and Boyd all now have Deschute-compliant units available in their product catalogs. Yesterday, Google announced that they would specify another CDU design - this time for Liquid to Air (L2A CDUs) named project Brazos (in line with Google naming these projects after rivers). This note walks through implications for the broader CDU ecosystem.

## L2L vs. L2A: What's the difference?

In our CDU primer earlier this week, we focused mostly comparing on flagship L2L CDUs. L2L units are named as such because they reject heat between two liquid loops (the technology cooling system and facility water system). In contrast, the L2A configuration we are talking about today only has one liquid loop (the technology cooling system) which rejects heat as air into the "hot aisle" of a data center. A CRAH or CRAC (Computer Room Air Handler or Computer Room Air Conditioner) then blows the hot air out of the hall / building. Generally, L2L cooling is preferred for all greenfield builds or situations where rack densities cross 150kW (it is much more energy efficient). In contrast, L2A builds are preferred when retrofitting an existing data center because it does not need the facility water system loop (eliminating the need for complex piping retrofits) or when cooling capacities range between 40kW to -150kW (below which plain old - but cold - air can be used to extract heat from the chips). Both L2A and L2L are still types of liquid cooling (i.e., they need cold plates and coolant to extract heat from chips), they simply differ in terms of how they reject heat from the TCS to the outside of the data center.

EXHIBIT 1: Distinction between Liquid-to-Air and Liquid-to-Liquid CDUs  
![](images/862b9364a8221f4910814c104e910c97b638c926ff4f9787f2fe86b10f623e4a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph L2A
  A["Rack"] -->|Spent coolant to CDU| B["CDU"]
  C["Technology Cooling System (TCS)"] -->|Primed coolant to rack| A
  D["Heat rejection to hot aisle (in room)"] --> E["CRAH/CRAC"]
  E --> F["Heat rejection outside data hall"]
  F --> G["Dumps heat into the &quot;hot aisle&quot; of a data center; then cooled or blown out by a CRAH/CRAC"]
  G --> H["Tends to be bridge / retrofit friendly; does not need plumbing / retrofit to bring the FWS in"]
  H --> I["Good for low / moderate density deployments; >40kW to possibly 150kW are manageable"]
    end
    subgraph L2L
  J["Rack"] -->|Spent coolant to CDU| K["CDU"]
  L["Technology Cooling System (TCS)"] -->|Primed coolant to rack| K
  M["Heat rejection through cooling tower / direct airflow"] --> N["Water / air-cooled chiller"]
  N --> O["Chilled Water to CDU"]
  P["Default cooling mode for frontier models; best for highest density racks"] --> Q["Generally, requires specification when the facility is designed; challenging to retrofit in"]
  Q --> R["Expect to see this config. in frontier hyperscaler builds"]
    end
```
</details>

Source: Bernstein Analysis and Estimates

## Thoughts on Brazos specifications

When we look at the specifications offered by Brazos, prima facie it does not look that impressive or demanding. 60kW of capacity cannot cool even a single Blackwell rack (which requires \~120kW of cooling power) - players like nVent, Motivair, and CoolIT go far higher on their cooling power for L2A CDUs. The power feed is DC (not AC) and designed to be pulled directly from busbars which is distinct from most other L2A CDUs available in the market today which are designed for AC use.

EXHIBIT 2: Project Brazos Overview  
What exactly is Google Brazos?  
![](images/abd215561b5950253b0b6f90e5c1bad57a8fa4dbadc60af3d7f881bffc475b51.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Air CDU"] --> B["Brazos Liquid Cooling Chassis<br>Nominal Thermal Capacity: 20 kW"]
  C["High-Efficiency Air-Liquid Heat Exchanger"] --> B
  D["Hot-Swappable Fans (FRU)"] --> B
  E["Hot-Swappable Pumps (FRU)"] --> B
  F["Telemetry Sensors (Flow, Temp, Pressure, Leak)"] --> B
  B --> G["Brazos to-Manifold Connection"]
  B --> H["Brazos to-Manifold Connection"]
  B --> I["Brazos to-Canal Vertical Manifold Assembly<br>Coolant Supply (Cold)<br>Coolant Return (Warm)"]
  B --> J["Brazos to-Manifold Connection"]
  K["Above-Rack Manifold"] --> L["Brazos to-Manifold Connection"]
  K --> M["Brazos to-Canal Vertical Manifold Assembly<br>Coolant Supply (Cold)<br>Coolant Return (Warm)"]
  K --> N["Brazos to-Canal Vertical Manifold Assembly<br>Coolant Supply (Cold)<br>Coolant Return (Warm)"]
    O["IT Rack<br>  (Liquid-Cooled Server Troyn)"] --> P["Brazos to-Manifold Connection"]
  O --> Q["BIAT"]
    R["System-Level Rack<br>Total Thermal capacity: 60 kV Nominal Load<br>Coolant compatibility: DI water or PGZ5<br>Closed-Loop Liquid-to-Air cooling<br>Operational simplicity of standard air systems<br>Independent Thermal Island Architecture"]
```
</details>

Source: Bernstein Analysis, Company Reports (Google)

• Google announced a new Liquid to Air (L2A) CDU configuration called "Brazos"  
- Largely aimed at servicing older environments where providers are attempting to offer higher rack densities without complexity of chiller and piping retrofits  
- Offers \~60kW of cooling capacity per rack; not enough for Blackwell (which is 120kW+ per rack) or higher end training models  
- As per Google: "Brazos functions as a self-contained liquid ecosystem, capturing heat via liquid at the component level and rejecting it into the data center's hot aisle using high-efficiency liquid-to-air heat exchangers. This plug-and-play architecture can be rapidly installed in any legacy facility that has sufficient power and standard air handling."  
• We want to highlight that this is not new tech.; L2A cooling has existed for years before Google made this announcement

EXHIBIT 3: Brazos L2A CDU specs. seem to target inference in OCP compliant environments  
![](images/5815d9a55e5738134abc7112fb88e2d4f9dd4907dd600846bac5db52cd8fffb8.jpg)

<details>
<summary>table</summary>

L2A Product comparison of Brazos vs. peers
| Company | Google Brazos | Boyd RAA32-10U21 | Vertiv CoolChip | nVent HRU | Motivair HDU | CoolIT AHx240 |
|---|---|---|---|---|---|---|
| Cooling Capacity 1 | 60 kW | 32 kW | 70 kW | 100 - 120 kW | 150 kW | 240 kW |
| ATD | Not stated | 24°C | 11°C | Not stated | Likely ~10°C | Not stated |
| Power Supply 2 | 40 - 60V DC | 1P AC | 1P AC | 1P AC | 1P AC | 1P AC |
</details>

1 Cooling power is too low to work with Blackwell or above; seems like Brazos is more focused on inference capacity through retrofits  
2 Direct DC connectivity via OCP-compliant busbar is unique to Brazos vs. other L2A CDUs; will not work in legacy colocation / enterprise builds  
Source: Bernstein Analysis and Estimates, Company Reports

However, our biggest takeaway is that this design is not intended to compete with existing products. It is designed to be OCP compliant, and fit into legacy hyperscaler deployments which tend to have DC power infrastructure already and not AC. The cooling capacity of 60kW does not work well for frontier training models, but can support inference at that range. Given concerns around how quickly data center capacity can get up and running (see our data center tracker for more insight on that), creating an inference ecosystem that can run in existing facilities with simple L2A CDU retrofits seems like a smart move (especially when inference looks set to grow faster than training through 2030). While not explicitly stated, we think this is the primary use case of the Brazos project.

## Our inferred implications on the CDU market

First, it is important to state what Brazos is not. It is not a CDU that Google is building; they are not in the business of making liquid cooling equipment. It is simply a set of technical specifications / requirements they will put out for their manufacturer ecosystem to build. As per Google: "In the coming months, we will formally open-source the technical specifications, design principles, and visual assets of Brazos through industry forums. As part of a broader infrastructure portfolio that continues to leverage waterless air-cooled systems alongside liquid cooling, Brazos represents one of many innovations we are contributing to the open hardware ecosystem. We invite system architects, manufacturers, and thermal engineers to evaluate these designs to scale rack-mounted cooling infrastructure for the high-power computing demands of the future." We also do not think this creates a structural near-term shock. CDUs will continue to see extended lead-times, and we expect L2L to be where most manufacturer focus stays.

We see two major risks for the mid-term. These are hard to quantify, but also cannot be ignored. First, there is real commoditization risk of the inference CDU ecosystem. Brazos specs. are meaningfully easier to deliver than Deschutes, and we believe they don't really need the engineering premium of a Vertiv or nVent. While these players may still opt to build and service Brazos-specified units, margins will be lower. We think the service attach will still be meaningful, but hypothesize less "moaty" than they would be with training GW where the cost of failure in meaningfully higher. The deciding factor here is inference rack densities; we are unsure what this looks like for purpose-built inference silicon from hyperscaler. If it remains below 60 kW/rack, then a meaningful share could be cooled by L2A Brazos-style CDUs. If not, larger Deschutes-class CDUs will be needed instead (which we would expect have higher margin and stickier service attach). Second, we may also see some hyperscaler demand shift from greenfield to retrofits, especially if projects get delayed. While we do not see that in our stranded capacity numbers in our data center capacity tracker, there has been some anecdotal input from companies that they are seeing customers push out deliveries because of a lack of readiness / project delays. With that said, we do not view this announcement by Google as imminently alarming for CDU manufacturers, especially those that focus on technical excellence at the top of the stack. Some level of CDU commoditization was always expected by the market. While we think this announcement accelerates the commoditization trend for lower spec. products, we still believe an innovation premium exists for flagship CDUs, and expect it to continue as top-tier liquid cooling technology evolves.

EXHIBIT 4: McKinsey and Co. Estimates of GW add by category  
![](images/87b2c960ee5bb8ef1871066ca9906cba7a622102beb9bcbbadae2f99fb6eea85.jpg)

<details>
<summary>stacked bar chart</summary>

Global data center demand by workload, 2025–30, gigawatts
| Year | AI compute (GW) | Non-AI (GW) | AI inference (GW) | AI training (GW) |
| :--- | :--- | :--- | :--- | :--- |
| 2025 | 38.3 | 20.9 | 23.1 | 82.3 |
| 2026 | 40.4 | 31.2 | 31.2 | 102.8 |
| 2027 | 44.9 | 43.7 | 39.5 | 128.1 |
| 2028 | 50.2 | 56.3 | 46.1 | 152.6 |
| 2029 | 56.2 | 71.5 | 52.8 | 180.5 |
| 2030 | 63.5 | 93.3 | 62.2 | 219.0 |
CAGR, 2025–30
</details>

Note: Includes all provider types.
\*Per annum.
Source: McKinsey Data Center Demand Model  
Source: Company Reports (McKinsey and Co.)

EXHIBIT 5: Recap: How does Liquid Cooling work?  
![](images/ea05cdaf5facfdeefe64105a5decee13cb907a04fd03188a54af4804eb24b608.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Cold manifold"] -->|Ultra-pure filtered water / fluid acts as coolant| B["Server"]
  A -->|Racks transfer heat through DTC contact; cold liquid is pumped through "cold plates" that physically touch chips and collect heat| C["Server"]
  A -->|Racks transfer heat through DTC contact; cold liquid is pumped through "cold plates" that physically touch chips and collect heat| D["Server"]
  E["CDU"] -->|Heat| A
  F["Hot manifold"] -->|Manifolds are entry / exit point of fluid and the rack; highly-engineered to have zero spillage of coolant| G["Server"]
  H["Controls temperature / flow of liquid entering racks"] --> I["Controllers"]
  I --> J["Information flow into facility-level monitoring system"]
  K["CDU acts as &quot;brain&quot; of cooling system; pumps and controls coolant flow"] --> L["FWS"]
  L --> M["Heat rejection equipment (Chiller, Dry cooler)"]
  M --> N["Heat"]
  N --> O["Heat is dumped externally outside the building"]
  P["Heats"] --> Q["Heat"]
  Q --> R["Heat"]
  R --> S["FWS"]
  S --> T["Heat"]
  T --> U["Heat"]
```
</details>

![](images/337adb03c0349fd6771cd51d42fde191b9c1eab47be16ee88d16bbe1d5cb2666.jpg)

<details>
<summary>text_image</summary>

Legend
Cold liquid	Hot liquid	Flow of data
</details>

![](images/464d880ef385e28adcefc58896a6e7e3f1ce71278621a599bba61cb840b58269.jpg)

<details>
<summary>text_image</summary>

Glossary of key liquid cooling equipment
Cold Plates
Coolant Distribution
Unit (CDU)
Manifold
</details>

## Glossary of liquid cooling terms

• DTC (Direct to chip)  
• TCS (Technology cooling system)  
• FWS (Facility water system)  
• TDP (Thermal Design Power)

Source: Bernstein Analysis

EXHIBIT 6: Recap: Our CDU outlook

## CDUs | We think CDUs are here to stay; some commoditization risk (but less than cold plates)

<table><tr><td>Timeframe</td><td>Near-term(2026–2028)</td><td>Mid-term(2028–2030)</td><td>Long-term(2030+)</td></tr><tr><td>Risk ofCommoditization</td><td>Low</td><td>Moderate</td><td>Moderate</td></tr><tr><td>Risk ofObsolescence</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Commentary</td><td>Near-term, we expectCDUs to be a growth driverfor anyone with exposure toliquid cooling from DCsWe expect the market tobe supply constrained;anyone with a CDU offeringwill probably see largebacklogs through 2028While there are somecommoditization risks fromprograms like OCP, ProjectDeschutes, etc. we believethe pace of productevolution largely supportsvendor pricing power</td><td>Regardless of whetherimmersion cooling or DTC isthe dominant configurationat this point, CDUs will stillbe required (so there is noobsolescence risk)We do expect the liquidcooling market to be muchmore mature at this pointand think there is largerpossibility that specs.become standardizedHowever, service quality /uptime will remainrelevant (especially if CDUsmove to the facility level vs.rack level), enabling CDUplayers to drive revenuefrom their install base vs.new equipment sales</td><td>Even in a config. with siliconetched microchannels,CDUs will remain relevant(and if anything, become more important asthe flowvolume / pressure becomecritical to finely control)We think CDUs will be ableto retain some pricingpower long-term even ifthey are fully specified byhyperscalersat this point –driven by a combination ofhigher complexity (esp.compared to cold plates)and the need for serviceonce CDUs installedGiven the high value ofracks, we do not think theservice can be outsourcedto third-party non-OEMs</td></tr></table>

Source: Bernstein Analysis and Estimates, Company Reports

Practically no obsolescence risk; we think CDUs are here to stay regardless of the dominant cooling config.

Some commoditization risk; hyperscalers will specify designs but CDUs are more complex (multiple connected pieces) than cold plates which preserves pricing power

In addition, CDUs need service (which cold plates do not) which also defends margin

We think CDUs are a great business to be in, ESPECIALLY for companies that can drive the innovation roadmap vs. just become contract mfg.

We see wide dispersion of forecasts for broader CDU market; but an LSD \$B market size today growing MSD/HSD \$B in the next 5 years does not seem too improbable

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's "affiliates" relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Vertiv Holdings Co

We value Vertiv at 32x NTM + 1 EBITDA of \$5.1B to reach our target price of \$416.

## nVent Electric PLC

We used a SOTP approach to value NVT. For the EC business, we used NTM + 1 EBITDA of \$417M and an EV/EBITDA multiple of 17x. For the SP business, we use an NTM + 1 EBITDA of \$1,063M and an EV/EBITDA multiple of 28x. Based on these assumptions, we arrive at a fair value per share of \$218.

## Schneider Electric SA

Our PT of €310 for Schneider is based on DCF with a WACC of 7.8% and a terminal growth rate of 2.5%. We think a DCF is appropriate for Schneider as it's a cash generative company and delivers stable cash flows irrespective of the point in the cycle.

## Eaton Corp PLC

We arrive at our \$534 price target by applying a 27x P/E multiple on our 2030 EPS estimate. Discounting this back, we arrive at our target price which implies a 33x P/E on our 2027 EPS. We believe this is appropriate given the long-term secular factors favoring the strength and long-term resilience of ETN's earnings algorithm.

## RISKS

## Vertiv Holdings Co

Downside: (i) Efficiency increasing to the point where less cooling needed, (ii) Unexpected slowing of data center expansion, (iii) Faster than expected shift away from NVIDIA chips to custom silicon (impacts Vertiv because of strong relationships), (iv) Tech. shift away from DTC / 800 VDC if Vertiv can't react fast enough

## nVent Electric PLC

Downside: (i) Faster than expected commoditization of CDUs / OCP makes them a commodity, (ii) Production line weakness for CDUs (given NVT is ramping), (iii) Longer than expected lead time to hire for key roles (e.g., open supply chain VP position)

## Schneider Electric SA

Key downside risks to our price target and forecasts: 1) We assume growth rate of c.12% for 2026 which assumes continued strength in Energy Management and improvement in IA. 2) Pull back in data center demand given technology changes which alter the composition of electrical infrastructure required in data centers and therefore demand for certain Schneider Electric products. 3) Imposition of additional tariffs in the US that lower demand for Schneider's products given weaker consumer buying power (we expect Schneider to be able to pass on any tariff costs, but demand may not be as elastic).

## Eaton Corp PLC

Downside risks include: 1) lower than expected load growth impacting ETN's Electrical organic growth business, 2) interruptions to the ongoing global data center build, 3) slower than expected utility capex growth, 4) slower than expected reshoring trends, and 5) slower than expected growth/cancellations in mega projects.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

• Outperform: Stock will outpace the market index by more than 15 pp  
• Market-Perform: Stock will perform in line with the market index to within +/-15 pp  
• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

• Outperform (OP): Stock will outpace the relevant index by more than 10 pp  
• Neutral (N): Stock will perform in line with the market index to within +/-10 pp  
• Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as 'Feature' (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.  
- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.  
- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.  
- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.  
- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.1%</td><td>16.5%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>36.3%</td><td>17.8%</td></tr><tr><td>Underperform</td><td>SELL</td><td>12.6%</td><td>14.9%</td></tr></table>

\* These figures represent the percentage of companies within each equity rating category for which affiliates of Bernstein have provided investment banking services within the previous 12 months.  
As of March 31, 2026. All figures are updated quarterly.

## PRICE CHARTS / RATINGS AND PRICE TARGET HISTORY

Vertiv Holdings Co (VRT) Rating History for Bernstein as of 06/16/2026  
![](images/1e6b825a7d1de5603de81ccaf0d125b35850e1a67a3d12c582e73e6bc8f1f3fc.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Price Target |
| ---------- | ------------- | ------------ |
| 06/09/2026 | $416.00       | -            |
</details>

nVent Electric PLC (NVT) Rating History for Bernstein as of 06/16/2026  
![](images/5c89548a2db24bc0cfe3d2654b2a7469170e74e98687806088dd38127fddc3e7.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Price Target |
| ---------- | ------------- | ------------ |
| 06/09/2026 | $218.00       | -            |
</details>

Schneider Electric SA (SU.FP) Rating History for Bernstein as of 06/16/2026  
![](images/158aa18e8cda4e3d028ddb92c9762c00931753a1aabca938a770eafa6f0e0d49.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Price Target |
|------------|---------------|--------------|
| 09/04/2023 | €185.00       | €185.00      |
| 02/27/2024 | €188.00       | €188.00      |
| 03/28/2024 | €188.00       | €188.00      |
| 04/01/2024 | €215.00       | €215.00      |
| 04/18/2024 | €250.00       | €250.00      |
| 06/05/2024 | €185.00       | €185.00      |
| 06/28/2024 | €250.00       | €250.00      |
| 11/01/2024 | €275.00       | €275.00      |
| 01/06/2025 | €280.00       | €280.00      |
| 02/24/2025 | €300.00       | €300.00      |
| 04/28/2025 | €290.00       | €290.00      |
| 07/09/2025 | €275.00       | €275.00      |
| 01/07/2026 | €285.00       | €285.00      |
| 02/27/2026 | €300.00       | €300.00      |
| 05/01/2026 | €310.00       | €310.00      |
</details>

Eaton Corp PLC (ETN) Rating History for Bernstein as of 06/16/2026  
![](images/a644e771b78195cee48116b1d76bfdcc9d265f1be82a38dd1aa62e05f5c60ed2.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Price Target |
| ---------- | ------------- | ------------ |
| 11/04/2024 | $382.00       |              |
| 12/20/2024 | $385.00       |              |
| 03/04/2025 | $355.00       |              |
| 07/14/2025 | $396.00       |              |
| 08/05/2025 | $410.00       |              |
| 09/11/2025 | $414.00       |              |
| 12/18/2025 | $395.00       |              |
| 02/03/2026 | $428.00       |              |
| 05/06/2026 | $509.00       |              |
| 05/25/2026 | $534.00       |              |
</details>

All price target and closing price data in the chart(s) above are denominated in the currency noted in the Ticker Table of this report.

## CONFLICTS OF INTEREST

SG and/or an affiliate(s) acted as Joint Global Coordinator and Joint deal manager in Schneider's convertible bond issue (EUR 800m, 8Y)

Bernstein Autonomous LLP or BSG France SA, beneficially, has either a net long or short position of 0.5% or more of the total issued share capital of a class of common equity securities of the following MiFID eligible securities: Eaton Corp PLC.

AB and/or its affiliates beneficially own 1% or more of a class of common equity securities of the following company: Eaton Corp PLC.

Bernstein and/or affiliates have received compensation for investment banking services in the past twelve months from Schneider Electric SA.

Bernstein and/or affiliates have received compensation for non-investment banking securities-related products or services in the previous twelve months from the following clients: Schneider Electric SA.

Bernstein and/or affiliates expect to receive or intend to seek compensation for investment banking services in the next three months from Schneider Electric SA.

Certain affiliates of Bernstein act as market maker or liquidity provider in the equities securities of: Vertiv Holdings Co, nVent Electric PLC, Schneider Electric SA and Eaton Corp PLC.

Affiliates of Bernstein managed or co-managed in the past twelve months a public offering of securities of Schneider Electric SA.

Bernstein and/or affiliates had an investment banking client relationship during the past twelve months with Schneider Electric SA.

Certain affiliates of Bernstein act as market maker or liquidity provider in the debt securities of: Schneider Electric SA and Eaton Corp PLC.

## OTHER MATTERS

The legal entity(ies) employing the analyst(s) listed in this report, and their location, can be determined by the country code of their phone number, as follows:

+1 Bernstein Institutional Services LLC; New York, New York, USA

+44 Bernstein Autonomous LLP; London UK

+212 SG Africa Technologies & Services; Casablanca, Morocco

+33 BSG France S.A.; Paris, France

+34 BSG France S.A.; Madrid, Spain

+41 Bernstein Autonomous LLP; Geneva, Switzerland

+49 BSG France S.A.; Frankfurt, Germany

+91 Bernstein (India) Private Limited; Mumbai, India

+852 Bernstein (Hong Kong) Limited 盛博香港有限公司; Hong Kong, China

+65 Bernstein (Singapore) Private Limited; Singapore

+81 Bernstein Japan KK; Tokyo, Japan

Where this report has been prepared by research analyst(s) employed by a non-US affiliate, such analyst(s), is/are (unless otherwise expressly noted below) not registered as associated persons of Bernstein Institutional Services LLC or any other SEC-registered broker-dealer and are not licensed or qualified as research analysts with FINRA. Accordingly, such analyst(s) may not be subject to FINRA's restrictions regarding (among other things) communications by research analysts with a subject company, interactions between research analysts and investment banking personnel, participation by research analysts in solicitation and marketing activities relating to investment banking transactions, public appearances by research analysts, and trading securities held by a research analyst account.

Where this report has been prepared by research analyst(s) employed by SG Africa Technologies & Services (part of the SG group of companies), it has been prepared on behalf of a Bernstein company under a Global Services Agreement in place between Bernstein and SG.

## CERTIFICATION

Each research analyst listed in this report, who is primarily responsible for the preparation of the content of this report, certifies that all of the views expressed in this publication accurately reflect that analyst's personal views about any and all of the subject securities or issuers and that no part of that analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views in this publication.

## II. ADDITIONAL GLOBAL CONFLICT DISCLOSURES

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e., the private side) within the Firm, and into other areas, units, groups or affiliates (i.e., public side) of the Firm.

## III. OTHER IMPORTANT INFORMATION AND DISCLOSURES

Separate branding is maintained for "Bernstein" and "Autonomous" research products.

- Bernstein produces a number of different types of research products including, among others, fundamental analysis and quantitative analysis under both the "Autonomous" and "Bernstein" brands. Recommendations contained within one type of research product may differ from recommendations contained within other types of research products, whether as a result of differing time horizons, methodologies or otherwise. Furthermore, views or recommendations within a research product issued under one brand may differ from views or recommendations under the same type of research product issued under the other brand. The Research Ratings System for the two brands and other information related to those Rating Systems are included in the previous section.  
- Autonomous operates as a separate business unit within the following entities: Bernstein Institutional Services LLC, Bernstein Autonomous LLP, Bernstein (Hong Kong) Limited 盛博香港有限公司 and Bernstein (India) Private Limited. For information relating to "Autonomous" branded products (including certain Sales materials) please visit: www.autonomous.com. For information relating to Bernstein branded products please visit: www.bernsteinresearch.com.

Analysts are compensated based on aggregate contributions to the research franchise as measured by account penetration, productivity and proactivity of investment ideas. No analysts are compensated based on performance in, or contributions to, generating investment banking revenues.

This report has been produced by an independent analyst as defined in Article 3 (1)(34)(i) of EU 596/2014 Market Abuse Regulation ("MAR") and the same article of MAR as it forms part of United Kingdom domestic law by virtue of the European Union (Withdrawal) Act 2018.

To our readers in the United States: Bernstein Institutional Services LLC, a broker-dealer registered with the U.S. Securities and Exchange Commission ("SEC") and a member of the U.S. Financial Industry Regulatory Authority, Inc. ("FINRA") is distributing this publication in the United States and accepts responsibility for its contents. Where this material contains an analysis of debt product(s), such material is intended only for institutional investors and is not subject to the US independence and disclosure standards applicable to debt research prepared for retail investors.

Bernstein Institutional Services LLC may act as principal for its own account or as agent for another person (including an affiliate) in sales or purchases of any security which is a subject of this report. This report does not purport to meet the objectives or needs of any specific individuals, entities or accounts.

To our readers in Canada: If this publication pertains to a Canadian domiciled company, it is being distributed in Canada by Bernstein (Canada) Limited, which is licensed and regulated by the Canadian Investment Regulatory Organization. If the publication pertains to a non-Canadian domiciled company, it is being distributed by Bernstein Institutional Services LLC, which is licensed and regulated by both the SEC and FINRA, into Canada under the International Dealers Exemption.

This document may not be passed onto any person in Canada unless that person qualifies as "permitted client" as defined in Section 1.1 of NI 31-103.

To our readers in Brazil: This report has been prepared by Bernstein Institutional Services LLC, and Banco BTG Pactual S.A. ("BTG") is responsible for the distribution of this report in Brazil.

To readers in the United Kingdom: This publication has been issued or approved for issue in the United Kingdom by Bernstein Autonomous LLP, authorised and regulated by the Financial Conduct Authority and located at 60 London Wall, London EC2M 5SH, +44 (0)20-7170-5000. Registered in England & Wales No OC343985.

This document is for distribution only to persons who (i) have professional experience in matters relating to investments falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Financial Promotion Order"), (ii) are persons falling within Article 49(2)(a) to (d) ("high net worth companies, unincorporated associations, etc.") of the Financial Promotion Order, (iii) are outside the United Kingdom, or (iv) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the FSMA) in connection with the issue or sale of any securities may otherwise lawfully be communicated or caused to be communicated (all such persons together being referred to as "relevant persons"). This document is directed only at relevant persons and must not be acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this document relates is available only to relevant persons and will be engaged in only with relevant persons.

To our readers in the member states of the EEA: This publication is being distributed by BSG France SA, which is authorised and regulated by the Autorité de Contrôle Prudentiel et de Résolution (ACPR) and Autorité des Marchés Financiers (AMF).

To our readers in Hong Kong: This publication is being distributed in Hong Kong by Bernstein (Hong Kong) Limited 盛博香港有限公司, which is licensed and regulated by the Hong Kong Securities and Futures Commission (Central Entity No. AXC846) to carry out Type 4 (Advising on Securities) regulated activities and subject to the licensing conditions mentioned in the SFC Public Register (https://www.sfc.hk/publicregWeb/corp/AXC846/details)). This publication is solely for professional investors, as defined in the Securities and Futures Ordinance (Cap. 571). The purpose of this report is solely to provide an analysis of the issuers referred to in this report and is not intended for any purpose contrary to the laws of Hong Kong.

To our readers in Singapore: This publication is being distributed in Singapore by Bernstein (Singapore) Private Limited, only to accredited investors or institutional investors, as defined in the Securities and Futures Act 2001 of Singapore ("SFA"). Recipients in Singapore should contact Bernstein (Singapore) Private Limited in respect of matters arising from, or in connection with, this publication. Bernstein (Singapore) Private Limited is regulated by the Monetary Authority of Singapore and licensed under the SFA as a capital markets services licence holder for dealing in capital markets products that are securities and collective investment schemes and an exempt financial adviser for advising on, issuing and promulgating analyses and reports on securities. Bernstein (Singapore) Private Limited is registered in Singapore with Company Registration No. 20213710W and located at 8 Marina Boulevard, #12-01, Marina Bay Financial Centre, Singapore 018981, +65-6326-7000.

To our readers in the People's Republic of China: The securities referred to in this document are not being offered or sold and may not be offered or sold, directly or indirectly, in the People's Republic of China (for such purposes, not including the Hong Kong and Macau Special Administrative Regions or Taiwan, the "PRC") in contravention of any applicable laws of the PRC.

This document does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC to any person to whom it is unlawful to make the offer or solicitation in the PRC.

We do not represent that this document may be lawfully distributed, or that any securities may be lawfully offered, in compliance with any applicable registration or other requirements in the PRC, or pursuant to an exemption available thereunder, or assume any responsibility for facilitating any such distribution or offering. In particular, no action has been taken by us which would permit a public offering of any securities or distribution of this document in the PRC. Accordingly, the securities are not being offered or sold within the PRC by means of this document or any other document. Neither this document nor any advertisement or other offering material may be distributed or published in the PRC, except under circumstances that will result in compliance with any applicable laws and regulations.

To our readers in Japan: This publication is being distributed in Japan by Bernstein Japan KK (サンフォード・C・パーンスタイン株式会社), which is registered in Japan as a Financial Instruments Business Operator with the Kanto Local Finance Bureau (registration number: The Director-General of Kanto Local Finance Bureau (FIBO) No.3387) and regulated by the Financial Services Agency. It is also a member of Investment Management Association of Japan. This publication is solely for qualified institutional investors in Japan only, as defined in Article 2, paragraph (3), items (i) of the Financial Instruments and Exchange Act.

For the institutional client readers in Japan who have been granted access to the Bernstein website by Daiwa Group Inc. ("Daiwa"), your access to this document should not be construed as meaning that Bernstein is providing you with investment advice for any purposes. Whilst Bernstein has prepared this document, your relationship is, and will remain with, Daiwa, and Bernstein has neither any contractual relationship with you nor any obligations towards you.

To our readers in Australia: Bernstein (Hong Kong) Limited 盛博香港有限公司 is responsible for distributing research in Australia. It is regulated by the Securities and Exchange Commission under U.S. laws, by the Financial Conduct Authority under U.K. laws, which differs from Australian laws. Bernstein (Hong Kong) Limited 盛博香港有限公司 is exempt from the requirement to hold an Australian financial services license under the Corporations Act 2001 in respect of the provision of the following financial services to wholesale clients:

• providing financial product advice;  
• dealing in a financial product;  
• making a market for a financial product; and  
• providing a custodial or depository service.

To our readers in India: This publication is being distributed in India by Bernstein (India) Private Limited (SCB India) which is licensed and regulated by Securities and Exchange Board of India ("SEBI") as a research analyst entity under the SEBI (Research Analyst) Regulations, 2014, having registration no. INH000006378 and as a stock broker having registration no. INZ000213537. SCB India is currently engaged in the business of providing research and stock broking services. Please refer to www.bernsteinresearch.in for more information.

• SCB India is a Private limited company incorporated under the Companies Act, 2013, on April 12, 2017 bearing corporate identification number U65999MH2017FTC293762, and registered office at Level 3A, 4th Floor, First International Financial

Centre, Plot Nos C-54 and C-55, G Block, Near CBI Office, Bandra Kurla Complex, Bandra (East), Mumbai 400098, Maharashtra, India (Phone No: +91-22-68421401).

\- For details of Associates (i.e., affiliates/group companies) of SCB India, kindly email MUM-BERNSTEIN-InCompliance@bernsteinsq.com.

• SCB India does not have any disciplinary history as on the date of this report.

\- Except as noted above, SCB India and/or its Associates (i.e., affiliates/group companies), the Research Analysts authoring this report, and their relatives

• do not have any financial interest in the subject company  
• do not have actual/beneficial ownership of one percent or more in securities of the subject company;  
• is not engaged in any investment banking activities for Indian companies, as such;  
• have not managed or co-managed a public offering in the past twelve months for any Indian companies;

• have not received any compensation for investment banking services or merchant banking services from the subject company in the past 12 months;

• have not received compensation for brokerage services from the subject company in the past twelve months;

• have not received any compensation or other benefits from the subject company or third party related to the specific recommendations or views in this report; and

\- do not currently, but may in the future, act as a market maker in the financial instruments of the companies covered in the report.

• do not have any conflict of interest in the subject company as of the date of this report.

\- Except as noted above, the subject company has not been a client of SCB India during twelve months preceding the date of distribution of this research report. Neither SCB India nor its Associates (i.e., affiliates/group companies) have received compensation for products or services other than investment banking, merchant banking or brokerage services from the subject company in the past twelve months.

\- The principal research analyst(s) who prepared this report, members of the analysts' team, and members of their households are not an officer, director, employee or advisory board member of the companies covered in the report.

\- Our Compliance officer / Grievance officer is Ms. Rupal Talati, who can be reached at +91-22-68421451, or MUMBERNSTEIN-InCompliance@bernsteinsg.com / Scbin-investorgrievance@bernsteinsg.com

\- The Research investor charter and Terms & Conditions of SCB India are available on its website and may be accessed at Bernstein (India) Private Limited (https://bernsteinresearch.in/) for your reference.

\- Disclaimer: Registration granted by SEBI, and certification from NISM, is in no way a guarantee of performance of the intermediary or provide any assurance of returns to investors. Investments in securities market are subject to market risks. Read all the related documents carefully before investing.

To our readers in Switzerland: This document is provided in Switzerland by or through Bernstein Autonomous LLP, and is provided only to qualified investors as defined in article 10 of the Swiss Collective Investment Scheme Act ("CISA") and related provisions of the Collective Investment Scheme Ordinance and in strict compliance with applicable Swiss law and regulations. The products mentioned in this document may not be suitable for all types of investors. This document is based on the Directives on the Independence of Financial Research issued by the Swiss Bankers Association (SBA) in January 2008.

To our readers in the Middle East: Bernstein Autonomous LLP, DIFC branch has its principal office at Gate Village 06, DIFC, Dubai, UAE. Bernstein Autonomous LLP, DIFC branch is regulated by the Dubai Financial Services Authority (DFSA) with the registration number CL10040 and is provisioned for Arranging Deals in Investments and Advising on Financial Products. All communications and services are directed at Professional Clients and Market Counterparties only (as defined in the DFSA rulebook). Persons other than Professional Clients and Market Counterparties, such as Retail Clients, are not the intended recipients of our communications or services.

## LEGAL

All research publications are disseminated to our clients through posting on the firm's password protected websites, bernsteinresearch.com and autonomous.com. Certain, but not all, research publications are also made available to clients through third-party vendors or redistributed to clients through alternate electronic means as a convenience.

This publication has been published and distributed in accordance with the Firm's policy for management of conflicts of interest in investment research, a copy of which is available from Bernstein Institutional Services LLC, Director of Compliance, 245 Park Avenue, New York, NY 10167. Additional disclosures and information regarding Bernstein's business are available on our website www.bernsteinresearch.com.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. This publication is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of, or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or which would subject any of the entities referenced herein or any of their subsidiaries or affiliates to any registration or licensing requirement within such jurisdiction. This publication is based upon public sources we believe to be reliable, but no representation is made by us that the publication is accurate or complete. We do not undertake to advise you of any change in the reported information or in the opinions herein. This publication was prepared and issued by entity referred to herein for distribution to eligible counterparties or professional clients. This publication is not an offer to buy or sell any security, and it does not constitute investment, legal or tax advice. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with their professional advisors in light of their specific circumstances. The value of investments may fluctuate, and investments that are denominated in foreign currencies may fluctuate in value as a result of exposure to exchange rate movements. Information about past performance of an investment is not necessarily a guide to, indicator of, or assurance of, future performance.

This report is directed to and intended only for our clients who are "eligible counterparties", "professional clients", "institutional investors" and/or "professional investors" as defined by the aforementioned regulators, and must not be redistributed to retail clients as defined by the aforementioned regulators. Retail clients who receive this report should note that the services of the entities noted herein are not available to them and should not rely on the material herein to make an investment decision. The result of such act will not hold the entities noted herein liable for any loss thus incurred as the entities noted herein are not registered/authorised/licensed to deal with retail clients and will not enter into any contractual agreement/arrangement with retail clients. This report is provided subject to the terms and conditions of any agreement that the clients may have entered into with the entities noted herein. All research reports are disseminated on a simultaneous basis to eligible clients through electronic publication to our client portal.

The information in this report was prepared by Bernstein solely for the internal business use of our clients. Clients may store, display, analyze, reformat and print the information in this report for this limited use only. Clients may not copy, alter, create derivative works, resell, reverse engineer, commercially exploit, share or distribute any part of the information contained herein for any purpose without Bernstein's express written consent. These restrictions include extracting data or using the content to develop indices or other products. Further, you may not use this report, or any portion of this report, to train or finetune any third-party machine learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.