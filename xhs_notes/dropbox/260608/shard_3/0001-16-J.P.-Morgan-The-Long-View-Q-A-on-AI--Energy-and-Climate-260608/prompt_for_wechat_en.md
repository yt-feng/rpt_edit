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
# The Long View

Q&A on AI, Energy and Climate

On May 26th, we hosted Thomas Spencer, co-author of the IEA's Key Questions on Energy & AI. In this Q&A, we address crucial aspects of the IEA's work:

- How Will Data Centres' (DC) Energy Demand Evolve? In the IEA's Base Case, DC double their share of global electricity from 1.5% to 3% by 2030 (485 → 950 TWh). The US absorbs 45% of incremental demand, followed by other advanced economies and China. The path to 2030 is capped on the upside by physical bottlenecks (memory, turbines) and supported by capex/adoption momentum. Cumulative DC capex of \$3.9trn through 2030 includes \$780bn of energy-related spend, with renewables (360 TWh) and gas (340 TWh) leading new generation. Beyond 2030, scenarios diverge materially.   
- How Much Compute Does AI Need? “Unprecedented” efficiency gains are outpaced by workload intensity. Per-query energy has fallen an order of magnitude, but the Jevons Paradox is in full force. Agentic Reasoning tasks consume \~50 Wh vs. \~0.3 Wh for simple text queries — pointing to the importance of new inference workloads in future demand.

\- Where Can AI Boost Energy Efficiency? Existing AI use cases in industry, energy, transport and buildings could deliver savings equal to 3% of global final energy consumption by 2035. We detail corporate examples across the four industries.

\- Will AI Boost Energy Innovation? AlphaFold's 2024 Nobel Prize suggests AI will foster breakthroughs, and most technologies needed for Net Zero have yet to be invented. Batteries, catalysts for synthetic fuels, $\mathrm{CO}_{2}$ capture materials, and cement are four key areas of AI-led innovation potential.

\- Will AI Have a Net Positive Energy and Climate Footprint? IEA and Stern project emission reductions exceeding DC energy demand, but neither accounts for rebound effects. NGOs warn of greenwashing; a recent study on AI-contrails shows technology is just one part of the equation — AI alone will not solve climate action.

\- Will AI Negatively Impact Affordability? Concerns around the price of electricity are growing, however impacts effectively depend on local conditions.

\- Will Local Opposition Block Datacentres? 98 local moratoriums and souring public sentiment have become a material, and accelerating risk that is already reshaping project siting, timelines, costs, and economics.

\- What Should Investors Engage Upon? The credibility of Big Tech clean energy commitments, the GHG Protocol Scope 2 overhaul (hourly vs. annual matching), and ITU-T L.1801 disclosure standards are key topics for sustainable investors.

\- Who are the EMEA Top Picks? CapGoods and IT Hardware OW-rated companies are well positioned: Legrand, Schneider Electric, Siemens, Siemens Energy, Prysmian; ASML, ASM International, Infineon and Nokia.

![](images/3bd8215c76f18ed1154bb8fb4254873b87e3073212e0917024e6a8bbd7d8b588.jpg)

# Sustainable Investing Research

# EMEA Sustainable Investing Research

Hugo Dubourg AC

(33-1) 4015 4471

hugo.dubourg@jpmchase.com

Jean-Xavier Hecker

(33-1) 4015 4472

jean-xavier.hecker@JPM.com

Noemie de la Gorce, CFA

(44-20) 7134-4229

noemie.delagorce@JPM.com

JPM Securities plc

Contents 

<table><tr><td>Executive Summary</td><td>2</td></tr><tr><td>How Will Data Centres’ Energy Demand Evolve?</td><td>5</td></tr><tr><td>How Much Compute Does AI Need?</td><td>10</td></tr><tr><td>Where Can AI Boost Energy Efficiency?</td><td>16</td></tr><tr><td>Will AI Boost Energy Innovation?</td><td>30</td></tr><tr><td>Will AI have a net positive energy &amp; climate footprint?</td><td>34</td></tr><tr><td>Will AI Negatively Impact Affordability Through Higher Electricity Prices?</td><td>41</td></tr><tr><td>What Should Investor Engagement Focus On?</td><td>44</td></tr><tr><td>Who are the EMEA Top Picks?</td><td>51</td></tr></table>

# Executive Summary

# How Will Data Centres' Energy Demand Evolve?

Data centres accounted for approximately 1.5% of global electricity consumption in 2025, with demand growing at four times the rate of broader electricity consumption since 2017. Under the IEA Base Case, data centre electricity consumption is projected to roughly double from around 485 TWh in 2025 to 950 TWh by 2030, representing just under 10% of global electricity demand growth over the period. The United States is expected to account for 45% of this incremental demand, followed by other advanced economies (19%) and China (6–7%).

Four scenarios — Base, Lift-Off, Headwinds, and High Efficiency — converge through 2030 due to binding physical constraints, including IT hardware supply (notably memory), grid connection wait times of 4–5 years, gas turbine availability, transformer lead times, and skilled labour shortages. Cumulative data centre capex is estimated at \$3.9 trillion between 2026 and 2030, of which roughly 20% (\~\$780bn) is energy-related. Renewables are expected to contribute the largest share of new generation (\~360 TWh by 2030), with gas a close second (\~340 TWh), particularly in the US. Onsite battery storage and UPS capacity are projected to grow from \~5 GW today to 20–25 GW by 2030.

# How Much Compute Does AI Need?

AI energy efficiency gains are progressing at a pace described as unprecedented in energy history. Per-query energy consumption has fallen by an order of magnitude annually in recent years: Google's median Gemini text prompt consumes 0.24 Wh, OpenAI's average ChatGPT query 0.34 Wh — broadly comparable to a 2011 Google search (0.3 Wh). Hardware performance per watt has improved 30–40% annually over the past decade, and best-in-class hyperscale facilities now achieve PUE ratios of 1.1–1.2 versus 1.5–1.7 for older facilities. The IEA estimates that replacing all Google search queries by GenAI text queries would only represent 1% of current DC.

These gains are being outpaced by a shift toward far more energy-intensive workloads. While simple text queries consume 0.05–0.3 Wh, reasoning queries consume \~1 Wh, and agentic tasks with reasoning enabled can consume \~50 Wh per task. This Jevons paradox dynamic — whereby efficiency improvements drive broader adoption and more sophisticated use cases — explains why aggregate AI electricity consumption continues to climb despite per-task efficiency gains.

The IEA flags but does not deeply explore which workloads will fill its 2030 AI data center projections; our AI-assisted thought experiment finds that per-query economics (text, image, search) explain less than 5% of projected inference demand, with four high-intensity workload classes — agentic, video/multimodal, ambient assistants, and embedded enterprise inference — accounting for 75–85% of the build-out and quantifying the optimism baked into the IEA's base case.

# Will AI Boost Energy Efficiency?

The widespread adoption of well-documented AI applications could deliver energy savings equivalent to approximately 3% of global final energy consumption by 2035. Sector-level potential includes: oil & gas (methane leak detection, \~10% cost

reduction in oilfield development); power (up to \$110bn in annual savings by 2035, 30–50% reduction in outage durations, \~3% efficiency gains at fossil plants); industry (8% energy savings in light industry by 2035); transport (energy savings of up to 20%, equivalent to 120 million cars); and buildings (\~300 TWh of electricity savings by 2035, equivalent to Australia and New Zealand combined).

Notable corporate deployments include Saudi Aramco (\$2bn TRV from AI in 2024), Equinor (\$130m direct AI value in 2025), Veolia (90% N $_2$ O reduction across 120+ wastewater plants), E.ON (70 AI use cases, 30,000 smart substations), Heidelberg Materials (€380m saved in 2025), and Schneider Electric (\~10% electricity savings across 600+ Swedish schools).

These elements will likely represent material drivers of energy- and cost-efficiency gains for energy-intensive industries. We are therefore optimistic about their adoption wherever the benefits can be captured/monetized by companies exposed to new AI solutions. In turn, the adoption of these technologies will likely benefit electrification and solution providers including CapGoods and IT Hardware companies mentioned in this report.

# Will AI Boost Energy Innovation?

There is much discussion around the potential for AI to boost innovation. The 2024 Nobel Prize in Chemistry was awarded to David Baker, Demis Hassabis and John Jumper. The two latter, Google Deepmind researchers, contributed to the development of AlphaFold2, an AI model designed to solve a 50-year-old problem: predicting proteins' complex structures.

AI's potential to accelerate innovation is highest where four conditions align: high-complexity design spaces, strong structured datasets, straightforward verification, and receptive markets with drop-in pathways.

Batteries, catalysts for synthetic fuels, $CO_{2}$ capture materials, and cement represent four key areas of AI-led innovation potential, though commercial scaling remains constrained by industrial qualification, capital costs, and regulatory frameworks rather than discovery itself.

# Will AI Have a Net Positive Energy & Climate Footprint?

Under the IEA's Widespread Adoption Case, AI-enabled emissions reductions in end-use sectors could exceed data centre emissions by 2035. However, this pathway is not guaranteed: it assumes that sector-wide barriers (limited data, poor interoperability) are largely overcome and explicitly excludes rebound effects.

A material distinction exists between traditional AI and generative AI. Schneider Electric analysis indicates generative AI consumes 6–14x more energy than traditional AI. Of 154 documented climate-benefit claims, 97% relate to traditional AI and only 3% to consumer generative systems, with no verifiable substantial emissions reductions attributable to generative AI.

The contrails case study illustrates that technological solutions alone are insufficient: a Google–American Airlines trial achieved a 62% reduction in contrail formation on successfully executed flights, but only 11.6% across all eligible flights due

to operational adoption barriers.

# Will AI Negatively Impact Affordability?

The IEA finds no systematic relationship between load growth and retail electricity prices across major markets from 2019–2024 — but national averages can mask sharp localised pressures in data centre clusters.

In the short term (0–3 years), price pressure is concentrated, not universal. In constrained markets, wholesale tightening and transmission congestion can drive prices higher. Long-term outcomes diverge based on whether jurisdictions pursue integrated, anticipatory growth (neutral to downward pressure) or reactive growth in constrained systems (sustained upward pressure). A cross-cutting concern is that colocation and onsite generation can shift costs onto other consumers.

Three policy levers determine the path: cost allocation and tariff design (e.g., Virginia's new rate class for large data centre loads, effective January 2027), the pace of generation and transmission build-out, and the flexibility profile of the data centre fleet — where the IEA estimates that flexibility for just 0.1–1% of hours per year would suffice to integrate all projected new capacity through 2035.

The right question is therefore not "are data centres raising prices?" but "which jurisdictions are building the institutions to prevent data centre growth from raising consumer prices?"

# Will Local Opposition Block Datacentres?

Local opposition will not stop the AI datacentres buildout, but it has become a material, and accelerating risk that is already reshaping project siting, timelines, costs, and tax economics. Investors should now treat community and regulatory risk as a first-order variable — comparable to power availability and supply chain constraints.

# What Should Investor Engagement Focus On?

The electricity intensity of Big Tech revenues has nearly doubled over recent years, raising questions about the credibility of clean energy commitments. Among hyperscalers, only Alphabet and Microsoft have committed to 24/7 carbon-free energy by 2030, though Microsoft is reportedly reconsidering its target.

The proposed GHG Protocol Scope 2 overhaul — shifting from annual to hourly, location-matched accounting — has split Big Tech, with Meta, Amazon, and Salesforce backing an "impact accounting" approach versus Alphabet and Microsoft supporting hourly matching. IEA analysis indicates 50–80% hourly matching is cost-competitive with gas turbines in the US, with cost premia rising sharply only as procurement nears full 24/7.

The new ITU-T L.1801 standard for assessing AI environmental impact across four life-cycle stages provides a framework for investors to engage on improved disclosure.

# EMEA Top Picks

In the region, we believe CapGoods and IT Hardware are best-placed on the theme, with both sectors rated OW by JPM Equity Strategy. CapGoods OW names include

Legrand (30% datacentre exposure), Schneider Electric (26% datacentre exposure), Siemens, Siemens Energy, and Prysmian. IT Hardware OW names include ASML, ASM International, Infineon, and Nokia.

# How Will Data Centres' Energy Demand Evolve?

# A doubling DC share of electricity demand by 2030

Data centres accounted for about $1.5\%$ of global electricity consumption in 2025, with demand growing at four times the rate of broader electricity consumption since 2017. While roughly $15\%$ of current data centre demand is attributable to AI (with uncertainty), the IEA pins half the near-term growth in servers to AI-linked hardware and warns this may still underestimate AI's share of growth.

In its latest update, the IEA's Base Case sees data centre electricity consumption doubling from around 485 TWh in 2025 to around 950 TWh in 2030. That puts data centres at around one-tenth of global electricity demand growth to 2030, the fourth biggest driver of demand behind industry, EVs, appliances and space cooling. However, this is highly region specific and data centres could account for about $45\%$ of US electricity demand growth to 2030. Physical constraints (DC build, grid connection, availability of servers, memory, gas turbines) explain the IEA's unchanged outlook to 2030.

# Four Scenarios: From Headwinds to Lift-Off

The IEA's modelling approach is bottom-up and grounded in the physical shipments of servers — the core electricity-consuming equipment within data centres. Inputs to the model come from IT-sector projections for server manufacturing and shipments, both historical and forward-looking over a five-year horizon. A central variable is the annual shipment of accelerators (GPUs, TPUs, and similar specialised chips), which drive the high power intensity of AI-focused facilities. Layered on top of these physical inputs are assumptions about utilisation rates, idle power, and power usage effectiveness (PUE), which together translate IT capacity into total facility electricity consumption.

The four cases differ in their assumptions about these underlying drivers. The Base Case provides the central projection and reflects current trends in AI development, investment, and the persistence of supply-chain bottlenecks. The Lift-Off

Case assumes stronger AI adoption, surging digital services demand, and effective resolution of bottlenecks through expanded chip and energy-equipment manufacturing capacity, alongside policy progress that eases grid connection wait times. The Headwinds Case assumes slower demand growth, AI monetisation challenges that dampen investment, and persistent local and electricity-supply constraints; broader macroeconomic factors such as higher interest rates or trade restrictions could push outcomes in this direction. Finally, the High Efficiency

Case holds AI and digital services demand on the same trajectory as the Base Case but assumes that aggressive efficiency strategies — model rightsizing, continued model-efficiency gains, and a partial shift to edge computing — counterbalance demand growth.

In the updated Base Case, data centre electricity consumption grows from around 485 TWh in 2025 to roughly 950 TWh by 2030, accounting for just under 10% of global electricity demand growth over the period. Near-term physical and financial frictions mean that the Lift-Off Case tracks closer to the Base Case in the short

term, while the Headwinds and High Efficiency Cases diverge later than they did in the IEA's 2025 report, reflecting strong near-term momentum in investment and the rapid uptake of energy-intensive AI modes such as agentic AI. Beyond 2030, uncertainty widens materially in both directions.

Figure 1: Data centre demand growth has been significant and largely driven by the US ...   
Share of electricity demand (%)   
![](images/00af35dcb1316195b2b337f189d06588e05cfc609f72efd92e7dab8edb419002.jpg)

<details>
<summary>bar</summary>

| Year | USA (%) | China (%) | Europe (%) |
|---|---|---|---|
| 2005 | 1.5 | 0.5 | 0.8 |
| 2010 | 1.8 | 0.6 | 1.0 |
| 2015 | 1.8 | 0.7 | 1.0 |
| 2020 | 2.2 | 0.8 | 1.0 |
| 2024 | 3.8 | 1.0 | 1.1 |
</details>

Source: IEA (2025), Energy and AI, IEA, Paris https://www.iea.org/reports/energy-and-ai, Licence: CC BY 4.0

Figure 2: The IEA points to strong growth to the end of the decade - capped by physical constraints - with a broader range of 2035 estimates   
![](images/7927b4137e69ba29342256cfe6ae07e78df8eb9664e90c7bdcafbc2807b0c1ea.jpg)

<details>
<summary>bar</summary>

| Year   | Headwinds | High Efficiency | Base  | Lift-Off |
| ------ | --------- | --------------- | ----- | -------- |
| 2023   |           |                 |       |          |
| 2024   |           |                 |       |          |
| 2025   |           |                 |       |          |
| 2030   | 800       | 850             | 950   |          |
| 2035*  | 950       | 1000            | 1200  | 1650     |
</details>

Source: JPM based on IEA (2026), Key Questions on Energy and AI, IEA, Paris https://www.iea.org/reports/key-questions-on-energy-and-ai, Licence: CC BY 4.0

Figure 3: AI DC's electricity consumption should almost match that of conventional DC by 2030   
Data centre consumption (TWh)   
![](images/52eda81a0151ec9e3c6138fee39eb82e51f9de9e0095eaecdeb9c5f8161d6cee.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Conventional | AI-focused |
| ---- | ------------ | ---------- |
| 2025 | 350          | 150        |
| 2030 | 500          | 450        |
</details>

Source: JPM based on IEA (2026), Key Questions on Energy and AI, IEA, Paris https://www.iea.org/reports/key-questions-on-energy-and-ai, Licence: CC BY 4.0

Capacity i

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 05 Jun 2026 07:51 PM BST

Disseminated 08 Jun 2026 12:15 AM BST
"""
