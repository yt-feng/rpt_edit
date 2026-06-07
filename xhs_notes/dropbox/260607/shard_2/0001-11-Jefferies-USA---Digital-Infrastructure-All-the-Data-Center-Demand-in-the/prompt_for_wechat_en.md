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
# All the Data Center Demand in the World, Still Not Enough Supply

Demand for data centers continues to outpace supply, with hyperscaler capex accelerating and chip volume forecasts implying GWs of capacity ahead of feasible data center delivery. Demand is not the issue, but the supply chain is. Our DC Capacity data pulls show only 8.9 GW was lit in '25, while data center demand was nearly 21.1 GW, a \~12 GW deficit, highlighting a tight DC market, and supporting a favorable backdrop for DC REITs and AI DC Developers.

Demand Signals Are Unambiguous Across Every Metric: Hyperscaler capex is on pace for \$770B in CY26E, up 74% YoY and nearly 5x the \$156B deployed in CY23. Combined cloud backlog surged to \$2T in 1Q26, growing 3x faster than capex since CY23. Bottom-up accelerator sales volumes from our semiconductor team imply \~30 GW of global AI power demand in 2026E from GPU/XPU shipments alone, with 19 GW going to North America, nearly 2x the 10.3 GW of new capacity we expect to come online.

Six Physical Supply Constraints Set the Ceiling on Deliverable Capacity: Our proprietary DC Capacity Delivery Model calibrates supply ceilings across six constraint categories. We estimate EPC/Labor as the binding constraint in 2026E, with a ceiling of 10.4 GW. Cooling is nearly co-binding at 11.4 GW and becomes the binding constraint from 2028E onward.

Structural Undersupply Benefits Operators, Suppliers, and New Entrants Across the DC Ecosystem: With vacancy rates at 1-3% across primary markets and wholesale rents accelerating, the demand/supply imbalance continues to benefit operators, suppliers, and new entrants alike. DC REITs (DLR, EQIX, IRM) have realized meaningful growth in leasing volumes and pricing over the past several years, with rents and bookings accelerating alongside AI-driven demand. Supply chain tightness is equally favorable for equipment suppliers, where order growth continues to outpace revenue delivery across cooling, electrical, and power transformer manufacturers, with backlogs expanding at 2-4x the rate of revenue. The demand and supply imbalance is also supporting the emergence of new entrants, including those from the Bitcoin mining industry. CORZ, CIFR, HUT, RIOT, and WULF are converting existing infrastructure to serve AI/HPC workloads, leveraging energized sites and established grid connections to deliver capacity on compressed timelines that other developers, constrained by the multi-year interconnection queue and equipment lead times, struggle to match. See our initiation, AI Data Center Developers: Fresh Faces, Same Math, for more detail on the BTC-to-HPC thesis.

Our Data Validates the Trend; With the Data Center Industry Exiting 2025 With a 12 GW Deficit: According to Aterio's comprehensive site database, only 3.4 GW of lit data center capacity came online that were not hyperscaler self-builds in North America in 2025, against 15.6 GW of leases signed (per Data Center hawk), a 12.2 GW deficit. This gap has been growing significantly, from 2.9 GW in 2023 to 4.3 GW in 2024 and nearly tripling to 12.2 GW in 2025. From 2021 to 2025, the cumulative deficit has reached 20.4 GW of undelivered data center capacity, a trend we expect to worsen as demand continues to outpace the supply chain's ability to deliver. We expect hyperscalers to continue to commit to capacity further into the future. Currently, they tend to commit to capacity deliverable within 12-18 months, but we could see that widen to 24+ months given supply constraints.

Exhibit 4 - In 2025, Data Center Leases Signed Exceeded Actual Delivered Capacity by Over 12 GWs   
![](images/c239a5ae31a91c35998063ba9ad36e0d319f7947745ef7d6073fd806f37242c4.jpg)

<details>
<summary>bar</summary>

| Year | Colocation Leases Signed (DC Hawk) | Lit Colocation Capacity (Aterio) | Gap |
|------|------------------------------------|----------------------------------|-----|
| 2017 | 0                                  | 0                                | 0   |
| 2018 | 0                                  | 0                                | 0   |
| 2019 | 0                                  | 0                                | 0   |
| 2020 | 0                                  | 0                                | 0   |
| 2021 | 0                                  | 0                                | 0   |
| 2022 | 2                                  | 1                                | -1  |
| 2023 | 4                                  | 1                                | -3  |
| 2024 | 6                                  | 2                                | -5  |
| 2025 | 15                                 | 3                                | -12 |
</details>

Source: Aterio, Data Center Hawk, JEF

Exhibit 5 - Under Construction GW in North America is Over 6x the Capacity Delivered in 2025   
![](images/c521906525f6b2404dc5fddd45b486077b508a4fd852b4ef0c558a54cea5f90e.jpg)

<details>
<summary>bar_line</summary>

| Year | Hyperscaler Self Builds (Construction) | Colocation (Construction) | Under Construction / Annual Lift Capacity |
|---|---|---|---|
| 2010 | 0.0 | 0.0 | 0.0 |
| 2011 | 0.0 | 0.0 | 1.0 |
| 2012 | 0.0 | 0.0 | 1.5 |
| 2013 | 0.0 | 0.0 | 1.5 |
| 2014 | 0.0 | 0.0 | 1.5 |
| 2015 | 0.0 | 0.0 | 1.5 |
| 2016 | 0.0 | 0.0 | 2.0 |
| 2017 | 0.0 | 0.0 | 1.5 |
| 2018 | 0.0 | 0.0 | 2.5 |
| 2019 | 0.0 | 0.0 | 2.5 |
| 2020 | 0.0 | 0.0 | 2.5 |
| 2021 | 0.0 | 0.0 | 3.5 |
| 2022 | 0.0 | 0.0 | 4.5 |
| 2023 | 0.0 | 0.0 | 5.5 |
| 2024 | 1.4x | 1.4x | 6.7x |
| Jun-26 | 6.7x | 4.5x | 8.5x |
</details>

Source: JEF, Aterio

Jonathan Petersen \* | Equity Analyst

(212) 284-1705 | jpetersen@JEF.com

Stephen Volkmann, CFA \* | Equity Analyst

(212) 284-2031 | svolkmann@JEF.com

Julien Dumoulin-Smith \* | Equity Analyst

+1 (281) 774-2066 | jds@JEF.com

Brent Thill \* | Equity Analyst

(415) 229-1559 | bthill@JEF.com

Blayne Curtis \* | Equity Analyst

+1 (212) 336-7493 | bcurtis@JEF.com

Roger Samuel, CFA ^ | Equity Analyst

+612 9364 2931 | rsamuel@JEF.com

Paul Zimbardo \* | Equity Analyst

+1 (212) 778-8497 | pzimbardo@JEF.com

Aniket Shah, PhD \* | Head of Sust. & Transition Strategy

(212) 323-3976 | ashah14@JEF.com

Edison Lee, CFA ‡ | Equity Analyst

852 3743 8009 | edison.lee@JEF.com

Stephanie Dossmann § | Equity Analyst

+33 1 8665 6367 | sdossmann@JEF.com

Mike Prew || | Equity Analyst

44 (0) 20 7029 8422 | mprew@JEF.com

Sarim Chaudhry || | Equity Analyst

+44 (0)20 7029 8423 | schaudhry1@JEF.com

Jan Aygul \* | Equity Associate

+1 (917) 344-1839 | jaygul@JEF.com

Matthew Roberts \* | Equity Associate

+1 (212) 778-8524 | mroberts1@JEF.com

Our Top Picks to Play DC Supply Chain Tightness (see inside for more details): DLR, EQIX, CORZ, WULF, CAT, ETN, WCC, PRIM, MTZ, NI, ETR, GEV, CRDO, AMZN, CRWV, GOOGL, MSFT, MRL SM, BBOX LN, SGRO LN.

Exhibit 1 - Data Center Capacity Additions in North America (GW)   
![](images/8b2d4703361956c1dd72521eb2c74014fcce24407f53c9c23fd526f88f6f7f2f.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Colocation (Delivered GWs) | Hyperscaler Self Builds (Delivered GWs) |
|---|---|---|
| 2011 | 0.3 | 0.2 |
| 2012 | 0.3 | 0.2 |
| 2013 | 0.5 | 0.3 |
| 2014 | 0.3 | 0.7 |
| 2015 | 0.6 | 0.8 |
| 2016 | 0.3 | 0.9 |
| 2017 | 0.8 | 1.1 |
| 2018 | 0.6 | 1.1 |
| 2019 | 0.4 | 2.1 |
| 2020 | 0.3 | 2.2 |
| 2021 | 0.3 | 2.0 |
| 2022 | 0.3 | 1.6 |
| 2023 | 0.3 | 2.7 |
| 2024 | 0.3 | 3.9 |
| 2025 | 3.4 | 5.5 |
</details>

Source: JEF, Aterio

Exhibit 2 - Installed Data Center Capacity Total in North America (GW)   
![](images/752d3709188b48a4c42a3a269559f8c5da762de76c77ccec32bcebc51a8c9267.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Colocation | Hyperscaler Self Builds |
|---|---|---|
| 2011 | 5 | 1 |
| 2012 | 6 | 1 |
| 2013 | 6 | 1 |
| 2014 | 7 | 2 |
| 2015 | 7 | 2 |
| 2016 | 8 | 3 |
| 2017 | 8 | 4 |
| 2018 | 9 | 5 |
| 2019 | 10 | 6 |
| 2020 | 11 | 9 |
| 2021 | 12 | 11 |
| 2022 | 13 | 12 |
| 2023 | 14 | 15 |
| 2024 | 17 | 19 |
| 2025 | 20 | 24 |
</details>

Source: JEF, Aterio

Exhibit 3 - Top 15 Data Center Operators/Owners in North America by Power (GW)   
![](images/42d97dec3050d59fe6df1fc333b0d42cd4817cc8a4bd0b876fa1e9f35099900b.jpg)

<details>
<summary>bar</summary>

| Company | Value |
| :--- | :--- |
| Amazon Aws | 10.6 |
| Microsoft | 5.5 |
| Google | 5.2 |
| Facebook | 4.8 |
| Digital Realty | 2.5 |
| Qts Data Centers | 2.5 |
| Cyrusone | 1.2 |
| Vantage Data Centers | 1.2 |
| Switch Data Centers | 1.2 |
| Xai | 0.9 |
| Aligned Data Centers | 0.9 |
| Equinix | 0.7 |
| Ntt Global Data Centers | 0.6 |
| Cloudhq | 0.6 |
| Centersquare | 0.6 |
</details>

Source: JEF, Aterio

# Table of Contents

<table><tr><td>Best Investments in a Data Center Supply Constraint World</td><td>4</td></tr><tr><td>Our Data Center Capacity Model</td><td>7</td></tr><tr><td>Data Center Demand is Robust</td><td>8</td></tr><tr><td>Supply Chain Constraints: What are They and Which Companies?</td><td>13</td></tr><tr><td>What About the NIMBYs?</td><td>19</td></tr><tr><td>International Opportunity: If We Can&#x27;t Build it Here, Build it Over There</td><td>21</td></tr></table>

# Best Investments in a Data Center Supply Constraint World

# Jon Petersen (REITs and Digital Infrastructure)

- CORZ is the pioneer of the BTC-to-AI data center developer movement, as the company was the first to make the pivot with a 590 MW development for CoreWeave. The company trades at a discount to peers, despite having the largest powered land bank to drive future growth.   
- DLR is a data center REIT with a combined wholesale and enterprise Colo platform seeing meaningful demand acceleration as AI workloads scale. Enterprise Colo bookings have accelerated from roughly \~\$50M per quarter to nearly \~\$100M per quarter, with AI now representing \~33-50% of aggregate bookings and \~20% of enterprise Colo activity, up from low-teens levels last year.   
- EQIX operates the most interconnected data center platform globally, enabling low-latency infrastructure across its ecosystem and positioning it as the natural hub for inference and edge compute. Four of the top five neocloud providers and eight of the top ten AI labs are deployed across its network.   
- WULF is an AI data center developer that repositioned its BTC mining land sites to turn key data centers built for neoclouds and hyperscalers. Management's deep experience and legacy in the power & utilities market positions the company well to continue to procure powered land sites and build AI data centers.

# Stephen Volkmann (Machinery and Industrials)

\- CAT remains our top pick in Machinery despite upside from power gen already largely baked into estimates and consensus. We see upside in the gas cycle, which will need to come given increased demand from data centers.

# Blayne Curtis (Semiconductors)

\- CRDO: We believe AEC adoption across XPU and CPU platforms is still in its early stages, supporting durable unit growth through C28+. Ramp of the 1.6T AECs in late '26 and early '27 should provide a material ASP uplift, bolstering our above-consensus revenue forecasts. ZF Optics provides a meaningful NT revenue opportunity, expanding the addressable market and diversifying the portfolio beyond electrical.

# Brent Thill (Internet Software)

- AMZN. We believe the stock screens as a mispriced AI/cloud/retail compounder, with AWS positioned to reaccelerate as AI capacity comes online, backlog converts to revenue, and Anthropic/OpenAI-related demand scales. Retail and ads remain durable margin drivers, while Trainium, Bedrock, Kiro, and longer-term opportunities like Leo add incremental upside that we believe is not fully reflected in the stock.   
- CRWV. CRWV is one of the best in the industry at scaling HPC infrastructure, with 1GW of active capacity today and plans to scale toward 8GW by FY30. The company already counts many of the largest hyperscalers, including MSFT, META and GOOGL, as well as leading AI natives such as OpenAI, Cursor and Anthropic, as customers. At a \$63B market cap versus \$99B of RPO and a multi-trillion-dollar AI infrastructure buildout ahead, we view valuation as compelling. We believe the stock can inflect in 2H as margins inflect and RPO continues to benefit from unrelenting AI demand.

- GOOGL. One of the best-positioned AI platforms given its vertically integrated stack spanning custom silicon/TPUs, Gemini models, developer tooling, and scaled consumer/enterprise surfaces. Gemini traction, combined with Google's unmatched data moat across Search, YouTube, Android, Workspace, and Cloud, creates a structural advantage that is difficult to replicate and should support durable AI monetization across both advertising and Cloud.   
- MSFT. MSFT is positioned to be an enterprise AI winner, with a differentiated end-to-end stack across Copilot, Azure AI, identity, and infrastructure supporting durable double-digit revenue and operating income growth despite elevated AI investment. Copilot paid seats are scaling, Azure AI demand continues to build, and we believe investor concerns around AI-related margin pressure are likely to prove overstated as monetization broadens.

# Julien Dumoulin-Smith (Power and Utilities)

- GEV. Provider of natural gas turbine and power generation infrastructure as well as grid electric components and wind turbines. Long lead cycle generation remains a key constraint but is not the critical path item for many projects. We are bullish on the long-term services value in the 2030s that is not fully appreciated.   
- NI. Indiana focused regulated utility with innovative 'GenCo' structure which allows for premium returns on building generation for hyperscalers. Current customers are Amazon and Alphabet with potential for more, as well as expansions.   
- PRIM. Engineering, procurement, and construction (EPC) company focused with power generation, power delivery, and pipeline focus. Renewables has been a challenging area for the company but are well positioned to execute on simple cycle gas combustion turbine (CT) build out. Access to skilled labor is the single most significant constraint in the power and thus data center ecosystem from our conversations.

# Stephanie Dossman (European REITs)

\- MRL has accelerated its pivot from traditional real estate to DC development in Iberia since 2024. The group is backed by well-located land and strong partnerships across both energy (notably Solaria) and operations, with Edge and CoreWeave. We expect +15% FFOps CAGR over 2025-32E and +11% NTAs CAGR over 2025-32E.

# Edison Lee (Chinese Tech and Telecom)

\- VNET is well-positioned to benefit from the China AI demand surge, supported by its rich power resources in Ulanqab - a desirable location for AI demand. Recent improving D-S dynamics in China also generates a more favorable project economics for IDC operators. Trading at \~10x 2026E EV/EBITDA vs 22% EBITDA Cagr (2026-29E), VNET remains highly attractive (here and here).

# Roger Samuel (Australian TMT)

\- MP1 AU: Megaport is transforming into a neocloud, benefiting from rising AI demand. Given that its core networking business already has a presence in over 1100 data centres around the world, Megaport is able to spread AI servers across these data centres and connect them using its mesh network. Latest note here

\- IFT AU/IFT NZ: Infratil owns a 50% stake in CDC, the largest data centre operator in Australia. Recently CDC signed the largest deal ever in the country: a 555MW contract with a US customer at premium pricing to its peers. With over 1.6GW in data centre pipeline, CDC is well-positioned to deliver further large contracts, especially when there is a power constraint in the US.

# Mike Prew (UK REITs)

- BBOX - Tritax management has incubated a power-backed, comprehensive DC business with 1GW of potential DC capacity. We think the DC business provides real alpha for BBOX and the flagship Manor farm scheme alone is expected to contribute £58m pa in rental income.   
- SGRO - SEGRO, has the scale and is poised to deliver 1.2GW of capacity over the next decade, with rental potential of £200m pa and development yields on cost 8-12%. Reflecting its development-led growth model but lower yield vs. income-led peers.

# Our Data Center Capacity Model

North American data center capacity increased by 8.9 GW in 2025A to 44.7 GW, and we estimate that another 10.3 GW will be lit in 2026E, reaching a total installed base of 55.0 GW. This marks a significant acceleration from the 1.4 to 3.5 GW per year delivered from 2017 to 2022. Looking further out, we model capacity additions growing from 12.1 GW in 2027E to 15.1 GW by 2030E, bringing total North American installed capacity to 109.3 GW, implying a \~20% CAGR off the 2025A base.

The mix between hyperscaler self-builds and leased capacity is shifting. Hyperscalers accounted for 62% of the 8.9 GW delivered in 2025A, and we expect their share of new builds to increase to 65% in 2026E before moderating to 45% by 2030E as third-party colocation developers accelerate delivery. On an installed capacity basis, hyperscaler self-builds accounted for \~55% of total capacity in 2025A and are expected to peak near 57% in 2026E to 2027E, then decline to \~54% by 2030E as colocation supply catches up. The leased share of new capacity additions dips from 38% in 2025A to 35% in 2026E, then recovers to 55% by 2030E, reflecting a structural rebalancing as developers convert contracted MW into commissioned capacity. On the installed base, leased capacity stabilizes near 43% through 2027E, then increases to \~46% by 2030E. We expect the leased data center market to outgrow owner-occupied builds through the forecast period, supported by hyperscaler demand for third-party capacity as a capital-efficient complement to self-builds.

Exhibit 6 - JEF Data Center Demand Model 

<table><tr><td>North American Data Center Capacity</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td colspan="22">TOTAL INSTALLED CAPACITY (MW)</td></tr><tr><td>Leased</td><td>4,900</td><td>5,300</td><td>5,700</td><td>6,300</td><td>6,600</td><td>7,300</td><td>7,600</td><td>8,400</td><td>9,100</td><td>9,600</td><td>10,900</td><td>11,700</td><td>13,000</td><td>14,400</td><td>16,900</td><td>20,300</td><td>23,900</td><td>28,700</td><td>34,600</td><td>41,600</td><td>49,900</td></tr><tr><td>Hyperscaler Self Build</td><td>6

[中间内容因长度限制已省略]

ular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
