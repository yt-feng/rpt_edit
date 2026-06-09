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
# Asia Insights

Economics - Asia ex-Japan

## Shipbuilding one year on: China's lead endures as Washington turns to allies

The maritime dispute between Washington and Beijing has evolved broadly as we anticipated in our June 2025 special report and remains largely unresolved. The USTR's Section 301 docking fees took effect on 14 October 2025, while Beijing retaliated instantly, and the two sides agreed at the Xi-Trump summit in Busan to suspend the measures for one year. President Trump's state visit to Beijing last month left this arrangement intact but did not extend or institutionalise it, leaving the suspension set to expire on 10 November 2026, with no successor framework currently in place.

On the order book, the widely reported narrative of a decline in China's market share requires careful examination. The headline share did swing sharply, falling from around three quarters of new orders in 2024 to a trough in mid-2025, before recovering to around $63\%$ for the whole year and close to $70\%$ in Q1 2026. We believe the dominant driver was a cyclical contraction in global ordering concentrated in segments where China is strongest, rather than a structural shift driven by Washington's threatened sanctions. China's shipyards continue to hold close to $70\%$ of the global orderbook by tonnage so far in 2026, and we maintain our core view that this lead will persist. The principal near-term risk remains geopolitics rather than demand, while the longer-term challenge is an inevitable softer phase following the current upswing.

## The swing in orders reflects primarily the cycle and less the policy

The most widely cited statistic of the past year, namely that China's share of new shipbuilding orders has roughly halved, requires a closer look. On a Clarksons Research compensated-gross-tonnage basis, the share fell from around $3/4$ in 2024 to a trough in mid-2025, when South Korea briefly led monthly ordering, before recovering to around $63\%$ for the year. China's Ministry of Industry and Information Technology (MIIT) reports a higher $69\%$ on a deadweight basis, which structurally flatters China, given its order mix. The early data for 2026 reinforce rather than undermine this trajectory, with China taking around $70\%$ of global orders by compensated gross tonnage (CGT) in Q1, even as total global contracting rose by some $40\%$ y-o-y. We read this V-shaped profile (Figure 1) as the product of three forces of differing weight and persistence.

## Policy-driven diversion was real but is partly temporary

Between the April and October 2025 fee schedule (the window between the initial USTR announcement and its actual implementation), owners facing an uncertain charge structure had a rational incentive to steer orders linked to US trade lanes away from the “China-built” designation, and the major liner alliances reconfigured their rotations to limit Chinese-built calls at American ports. We believe this behaviour accounts for much of South Korea’s surge in H1 2025, but it represents a hedge against policy uncertainty rather than a durable reallocation of demand.

## The cyclical mismatch carries heavy weight and is routinely overlooked

Global ordering fell sharply in 2025 (down $27\%$ by CGT, according to Clarksons), and the contraction was concentrated in tankers and bulkers, which are precisely the segments in which China has the largest share (Figure 2). In the first ten months of the year, product-tanker orders fell by close to $85\%$ y-o-y, while crude-tanker orders declined by around $31\%$ (Source: CSSC & Clarksons Research), and the only major segment to grow over the full year, containerships, is likewise one that China has a stranglehold. Much of the apparent quarterly share loss was therefore a statistical artefact of a shrinking and unfavourably weighted denominator, which in our view is the single most underappreciated feature of the 2025 data (Figure 3). China's exports of ships also recorded a historical high in 2025 (Figure 4).

## Research Analysts

## Asia Economics

Harrington Zhang - NIHK

harrington.zhang@NOM.com

+852 2252 2057

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

Fig. 1: Shares of China and South Korea in global ship orderings by compensated gross tonnage  
![](images/b906e3bf6d7e0c24fa2944e2ebb50e081fcefd04b293315b76a2466f30300e96.jpg)

<details>
<summary>bar chart</summary>

| Year | China (%) | South Korea (%) |
| :--- | :--- | :--- |
| 2023 | 58.7 | 29.0 |
| 2024 | 70.0 | 17.0 |
| 2025 | 63.0 | 20.5 |
| Q1 2026 | 71.0 | 18.0 |
</details>

Source: Clarksons, NOM Global Economics

Fig. 2: Shipbuilding orders in major categories  
![](images/e88c1174dc4b870ab23a0b1162d0f1bd241a5d187107a32d4b8520a10f7fb4d5.jpg)

<details>
<summary>stacked bar chart</summary>

| Carrier Type | China | South Korea | Japan | Europe | RoW |
| ------------ | ----- | ----------- | ----- | ------ | --- |
| Bulker       | 67    | 0           | 28    | 0      | 5   |
| Tanker       | 58    | 21          | 14    | 5      | 5   |
| Container    | 53    | 39          | 10    | 0      | 2   |
| LPG carrier  | 48    | 47          | 5     | 0      | 0   |
| LNG carrier  | 21    | 71          | 1     | 2      | 0   |
</details>

Source: Wind, NOM Global Economics

## The post-truce unwinding drove the recovery

Once the Trump-Xi Busan understanding established a twelve-month buffer, the incentive to avoid Chinese yards faded and China's share climbed through the closing months of 2025 and into 2026. We regard this as the clearest evidence that the earlier dip was contingent on sentiment and the order mix rather than reflecting a permanent loss of competitiveness.

Fig. 3: Global ship orders fell in 2025 from the historical high in 2024  
![](images/0917689b194fb39bf6158bed9405be984d5825e382d390aafa5bf6d7a9e270a8.jpg)

<details>
<summary>bar chart</summary>

| Year | Global ship orders in compensated gross tonnage (mn CGT) |
| :--- | :--- |
| 2022 | 42 |
| 2023 | 41.5 |
| 2024 | 76.5 |
| 2025 | 56.5 |
</details>

Source: Clarksons, NOM Global Economics

Fig. 4: China's exports of ships made a historical high in 2025  
![](images/6699e3cf71cffa336c81ae45a3ad1960998159d5658727a66b12e6cf93916dd2.jpg)

<details>
<summary>bar chart</summary>

| Year | Total exports of ships (USD bn) |
| :--- | :--- |
| 2001 | 1.8 |
| 2003 | 2.0 |
| 2005 | 3.0 |
| 2007 | 8.0 |
| 2009 | 19.0 |
| 2011 | 39.0 |
| 2013 | 42.0 |
| 2015 | 36.0 |
| 2017 | 26.0 |
| 2019 | 23.0 |
| 2021 | 25.0 |
| 2023 | 20.0 |
| 2025 | 21.0 |
| 2027 | 21.0 |
| 2029 | 17.0 |
| 2031 | 21.0 |
| 2033 | 21.0 |
| 2035 | 27.0 |
| 2037 | 43.0 |
| 2041 | 55.0 |
</details>

Source: General Administration of Customs, NOM Global Economics

## Beijing's deepening commitment towards green shipbuilding

Green-fuel-capable vessels – spanning LNG, methanol, LPG, ethane-based and electric propulsion – accounted for 80.2% of China's new international shipbuilding orders in Q1 2026, according to the MIIT, representing an increasingly successful hedge into the high-value segments where China has historically lagged. China's position within this transition is anchored by a series of milestone deliveries in Q1 2026, including the 15,000-TEU methanol dual-fuel "Kun" series containership and the 174,000 cubic-metre "Tianshan" LNG carrier. As the global fleet transitions toward alternative fuels under the IMO's

greenhouse gas framework and the EU's FuelEU Maritime regulation, China's early and aggressive positioning means that its structural share could even rise as a natural consequence of the energy transition, independent of policy or cyclical factors.

## The Strait of Hormuz and the Q1 2026 tanker surge

The closure of the Strait of Hormuz generated a powerful demand pulse in tanker ordering. The transmission mechanism operates through tonne-miles rather than cargo volumes. As Gulf crude is re-routed via longer alternative paths, each vessel is occupied for more days per voyage, while dozens of tankers trapped inside the strait are physically removed from the trading fleet. The combination of a structurally constrained fleet, a rough doubling of some freight rates from year-earlier levels, and the expectation that a prolonged inventory replenishment cycle will sustain elevated demand, even after the strait reopens, created a compelling case for new orders, particularly given \~20% of the crude tanker fleet is over 20 years old. BIMCO and Clarksons data show that tanker orders tripled year-on-year in Q1 2026, with tankers accounting for 32% of total contracts, the highest proportion since Q2 2017. MIIT data show China captured this surge disproportionately, with its yards taking over 90% of new VLCC orders.

## Japan's continued decline in commercial shipbuilding

Compared with China's advancement and South Korea's steady position, Japan's marginalisation in commercial shipbuilding has accelerated over the past year. According to BIMCO and Clarksons data, Japanese yards captured approximately $1\%$ of global newbuilding contracting in Q1 2026, the lowest share since at least 1996, driven by capacity constraints and uncompetitive lead times. Japan's new export orders fell a further $15\%$ in FY2025, marking a fourth consecutive annual decline, with the Japan Ship Exporters' Association attributing the weakness to a persistent labour shortage (Source: Nikkei). Tokyo has responded by designating shipbuilding a strategic sector and targeting a doubling of annual capacity by 2035, backed by roughly JPY1trn in planned public and private investment. In our view, the implication for Washington's allied-yards strategy could be significant here: if Japan cannot contribute meaningfully to commercial shipbuilding, then the allied pillar rests almost entirely on Korean capacity.

## We expect structural dominance to endure as the cycle turns up

The unfolding data are consistent with the central view from our June 2025 report, that Washington's actions would impose costs at the margin without derailing China's trajectory. Beijing's moat remains intact, as China's yards hold around 64% of the global orderbook, and China has secured around 62% of orders for green-fuel-capable vessels. Our base case, to which we attach a probability of 2/3, is that the “Busan truce” will be eventually rolled over or softened around the autumn when President Xi is scheduled to pay a reciprocal state visit to Washington DC, since neither side derives much benefit from what has proven to be a high-cost and low-yield fight. The more gradual challenge lies not in the current cycle but in the cyclicality of newbuilding demand itself, since the present strength in ordering will, in time, give way to a softer phase; this is a statement about cycle position rather than China's competitive standing, which we expect to hold.

As for the rebound itself, we think two forces carry roughly equal weight: 1) the reassertion of China's structural and segment-mix advantage, as the recovery has been led by renewed tanker and bulker ordering, which are precisely the segments where China's share had previously declined; and 2) a reduction in precautionary avoidance of China-built ships and geopolitical risks, as owners increasingly regard the Beijing-Washington dé tente as relatively durable, as the Trump state visit and the expectation of Xi's reciprocal visit have lent the truce a credibility it lacked through the uncertainty of 2025. We would caution against attributing the swings to either single channel alone.

## The American revival increasingly relies on allies and their shipyards

While China's competitive position has strengthened, Washington has not been idle, and the pillar of the White House's strategy that has advanced fastest is not domestic self-sufficiency over the past year but the relocation of allied capital and expertise into US shipyards, which we read as an implicit acknowledgement that the country cannot rebuild capacity on its own. South Korea is the clear leader in this respect. As part of its July 2025 trade agreement, Seoul committed a USD150bn package to support shipbuilding in the US under the banner of "Make American Shipbuilding Great Again (MASGA)", and this commitment was tied directly to a reduction in its US tariffs. We think the structural detail matters a great deal: the package is constructed predominantly from government-backed guarantees and loans, with the US retaining project-selection authority, a design that secures allied financing while concentrating control on the American side.

The flagship project is Hanwha's planned investment of around USD5bn to expand the Philadelphia shipyard towards twenty vessels a year, and substantive contracts have begun to materialise. In early 2026, Hanwha won a subcontract for concept-design work on the Navy's Next-Generation Logistics Ship, and President Trump also signalled that the Navy could partner with Hanwha on a new frigate class. HD Hyundai and Samsung Heavy Industries are also participating in the MASGA framework. We would note that the programme has proceeded despite Beijing's previously announced but now-suspended sanctions on Hanwha's US subsidiaries, an early read on both the limits of Beijing's tolerance and the resilience of the arrangement. As discussed above, Japan remains a step behind, with its contribution still concentrated in naval maintenance and repair without a shipbuilding investment framework of comparable scale.

## The submarine constraint frames the entire allied strategy

In our view, the reliance on allied yards is ultimately a symptom of a binding capacity constraint, and nowhere is that constraint clearer than in submarines, which is an area where the US still holds a clear and enduring advantage over the PLA Navy. Following its review, the administration reaffirmed the first pillar of AUKUS, preserving the sale of three Virginia-class attack submarines to Australia from the early 2030s. The June 2026 Shangri-La trilateral announcement revised the composition to three in-service hulls rather than the original mix of new and pre-owned submarines. The industrial arithmetic is unforgiving: the base must reach 2.33 attack boats per year to sustain both the US fleet and the Australian transfers, whereas the current rate is around 1.2-1.3 according to the Congressional Research Service (Figure 5). With Virginia-class construction, the Columbia programme (ballistic missile submarines), the commercial revival and the AUKUS commitments all competing for the same scarce docks, supply chains and skilled workers, we think the dependence on Korean and Japanese capacity reflects a hard constraint rather than a policy preference, and that this is precisely why the allied route has advanced more quickly than domestic rebuilding.

Fig. 5: US attack-submarine output falls short of the AUKUS requirement (ships per year)  
![](images/c45bd92fbf6997b204c1a615931c0e1681eec014b4b79d72ddf7c888a90c5387.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | Actual build (vessels per year) | Shortfall to requirement (vessels per year) |
|---|---|---|
| Virginia-class submarine/yr | 1.30 | 1.03 |
</details>

Note: The attack-submarine is Virginia-class nuclear-powered attack submarines.
Source: US Congressional Research Service, NOM Global Economics

Fig. 6: US Navy shipbuilding: FY2027 request more than doubles FY2026 (+USD38.6bn, +142%)  
![](images/92a6cf4541b68cbe8bd3d8531bb5f80c75c157c675cd1b71b6e082c73d1f4120.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (USD bn) |
| :--- | :--- |
| FY2026 (enacted) | 27.2 |
| FY2027 (request) | 65.8 |
</details>

Source: US Department of the Navy, NOM Global Economics

## A leadership change exposes an unresolved strategy

The abrupt dismissal of Navy Secretary John Phelan on 22 April 2026 exposed an unresolved tension at the heart of the revival agenda. The proximate trigger may be Phelan's public suggestion that the Navy should consider building warships in allied yards abroad to ease the domestic labour shortage, which seemingly crossed Trump's "built in America" line. The distinction that matters is where the ships are built, not primarily who builds them: it is one thing to welcome foreign capital into US yards, as the Korean investment programme does, and quite another to construct American warships overseas. Acting Navy Secretary Hung Cao has since recast the foreign role in deliberately narrower terms, endorsing a model under which allied partners build only non-sensitive modules

while US shipyards retain final assembly and the integration of classified systems. The episode leaves the FY2027 budget request, which seeks USD65.8bn for shipbuilding against the USD27.2bn enacted for FY2026, pointing to clear intent, even as Washington has yet to settle how far the allied role can extend (Figure 6).

Taken together, the evidence over the past year is for the most part consistent with predictions we made a year ago and points to a contest that is intensifying in ambition but narrowing in effect. China's structural lead has, if anything, not only endured but also widened through the cycle, reinforced by capacity expansion and a decisive pivot toward green tonnage. Washington's allied-yards strategy is advancing but remains constrained by the same industrial bottlenecks it is designed to overcome. Our base case remains one in which the suspension survives its 10 November expiry, but that date represents the principal near-term risk to this otherwise stable equilibrium (for detail of the suspended measures, see Figure 7 and Figure 8).

Fig. 7: The USTR's port fee schedule for Chinese operators and Chinese-built vessels
Now suspended under the Busan agreement until 10 November 2026

<table><tr><td rowspan="2">Effective date</td><td>Chinese vessel operators or vessels owned by Chinese entity</td><td colspan="2">Chinese-built vessels*</td></tr><tr><td>USD per net tonne</td><td>USD per net tonne</td><td>USD per container fee</td></tr><tr><td>17-Apr-2025</td><td>0</td><td>0</td><td>0</td></tr><tr><td>14-Oct-2025</td><td>50</td><td>18</td><td>120</td></tr><tr><td>17-Apr-2026</td><td>80</td><td>23</td><td>153</td></tr><tr><td>17-Apr-2027</td><td>110</td><td>28</td><td>195</td></tr><tr><td>17-Apr-2028</td><td>140</td><td>33</td><td>250</td></tr></table>

Note: The fee will be charged up to five times per year, per vessel.  
A vessel owner of China means any entity whose country of citizenship is identified as the People's Republic of China (PRC), Hong Kong, or Macau on the Vessel Entrance or Clearance Statement or its electronic equivalent.  
\*For operators of Chinese-built vessels, the fee is dete

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
