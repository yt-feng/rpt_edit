# US Communications Infrastructure
# Data Center Interconnection: A literal network effect

If you've been paying attention to any players in the data center colocation market, it'd be hard to miss conversations on interconnection. Interconnection is simply linking networks to one another and handing off data, keeping the traffic off of the public internet. Players do this to minimize costs, lower latency, and increase security. It's an \~\$8B market, but measurement has always been a bit wishy-washy...we recently unearthed a new data source and constructed our own proprietary database, giving us new insight into the players. Spoilers: EQIX is even stronger than you think and AMT's CoreSite is a great asset.

For enterprise colo data centers, interconnection is a high-margin (70-90%), high-moat layer that shifts a data center from being commoditized power and space to being a true network hub. Cross connects (whether physical or virtual) are cheap to make, sticky for customers, and multiply in value as campuses fill - a literal network effect.

Historically this segment was more buying criteria than revenue driver, but with AI's emergence, interconnect is becoming a real growth story. Data is getting heavier, models bigger, and workloads increasingly latency sensitive...interconnection is increasingly dictating not only a data center's right to win, but also its own meaningful revenue stream.

In our new dataset, we look at 645 of the most critical interconnected enterprise collocation facilities in the world. Across them, we register 21,000+ interconnections from various network providers across a series of categories: Cloud On-Ramps, Tier 1 / Global Transit providers, Content / CDNs, US + Can ISPs, Global ISPs, Interconnect Economy Players, and Neoclouds.

Our overwhelming takeaway is that EQIX has more, denser facilities than anyone else - 222 facilities with an average of 58 interconnect partners per site, supporting 513k revenue-generating interconnections (as of 1Q26). The next closest is CoreSite (owned by AMT) with 29 facilities and an average of 46 providers per site. DLR comes in second in terms of total networks, but fourth on a per-facility average (34), expected given their relatively recent shift to enterprise.

60% of our observed cloud on-ramps are in an EQIX facility. In fact, 57% of the facilities with 3+ on-ramps belong to EQIX; DLR is a distant second with 23%. This is both meaningful and hard to replicate.

There is a geographic angle - EQIX's footprint overindexes towards interconnection in the U.S., where the average cross-connect is \~\$342 relative to \~\$197 in the rest of the world (EQIX proxies). DLR has some exceptionally strong, dense European facilities - their Frankfurt hub has 611 networks (Equinix Sao Paulo next highest at 586), but inherently lower cross-connect prices.

So what does this analysis mean for investors? EQIX's interconnect moat is sizeable, defensible, and valuable. We maintain our Outperform on the stock with a target price of \$1,222 and feel that there's still room despite its run this year (+39% YTD). We believe there may be even further upside as interconnect continues to grow, which would bolster both top and bottom line for EQIX.


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We value DLR on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$232 price target is based on 27x our 2027E AFFO per share of \$8.52.

We value EQIX on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$1,222 price target is based on 25x our 2027E AFFO per share of \$48.63.

We value AMT on a Price to NTM Adjusted Funds From Operations (AFFO) per share multiple. Our \$207 price target is based on 18x our 2027E AFFO per share of \$11.49.

## DETAILS

## INTERCONNECTION CONTEXT

## A BRIEF HISTORY ON INTERCONNECTION AND WHY IT EXISTS TODAY

Originally, data centers were glorified computer closets. But with the advent of the internet, the market realized it needed neutral hosts where telcos and ISPs could meet and swap traffic. This was the origin of the “meet-me room” (MMR $^{1}$ ), when cross-connects became critical pieces of fiber. Then clouds / SaaS / content platforms came into being, and they too needed to swap traffic - the carrier hotels with meet me rooms were the logical locations...an interconnection moat began to form.

Now, we're in the world of multicloud, edge, and AI, where interconnection is critical infrastructure. For an enterprise, data center capacity is no longer only about the building, it's also about the access and proximity to an increasingly broad partner set. Today, it's both colocation buying criteria and a product in itself.

## FLAVORS OF INTERCONNECTION

We have a few different types of interconnection, serving different purposes within the ecosystem.

1. Physical cross-connects (inside the facility): the most basic building block: a direct, point-to-point cable between two parties in the same data center, usually fiber or copper via a patch panel or meet-me room. Physical cross-connects are simple, predictable, and offer low-latency, private connectivity between an enterprise and a carrier, cloud on-ramp, or another tenant. Economically, they are sold as recurring monthly connections with a one-time install fee, and once in place they tend to be very sticky because they underpin production traffic. For AI, these links often tie GPU clusters to nearby storage, network providers, and cloud on-ramps within the same campus.
2. Data center interconnect (between facilities): extends the idea beyond a single building, linking multiple data centers within a campus so they can share workloads and data. At the short end, campus and metro connects make several sites in a city behave like one logical platform; at the long end, inter-market and regional connects support replication, disaster recovery, and performance across geographies. This layer lets customers design active-active architectures, spread AI training and inference across sites, and treat a provider's footprint as a single resource rather than isolated buildings.
3. Virtual cross-connections and software-defined network fabrics: Virtual cross-connects (VXCs) take the cross-connect concept and implement it in software over an existing network fabric. Instead of running a new cable each time, a customer uses a portal or API to create a private Layer 2 connection between two endpoints on the fabric — for example, between their port in a colo facility and a cloud region, or between two different data centers. The key differences versus physical cross-connects are provisioning speed and flexibility: VXCs can often be set up or removed in minutes, and capacity can be adjusted without touching any physical cabling. That makes them a useful tool for AI and multicloud workloads, where teams may need to test new data paths, connect to additional regions, or scale bandwidth for specific training runs without waiting on manual changes. Importantly, while the provisioning is virtual in a VXC, the termination is still physical.

EXHIBIT 1: Global Registered Network Connections by Provider (Units)

[[KC_IMAGE_001]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 2: Global Interconnected Sites by Provider (Units)

[[KC_IMAGE_002]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 3: Average and Median Networks by Facility by Provider (Units)

[[KC_IMAGE_003]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 4: Densest Global Interconnection Sites by Registered Network Count

[[KC_IMAGE_004]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 5: Average Registered Network per Site by Provider (Units)
Average Registered Network per Site by Provider (Units)

[[KC_IMAGE_005]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

## INTERCONNECTION PARTNERS

Interconnection is fundamentally about who an operator can put “across the aisle” from an enterprise rack. The richer the mix, the more valuable every incremental port and cross-connect becomes. Enterprise colo providers that assemble diverse, carrier-neutral ecosystems can monetize the same piece of real estate multiple times through cross-connects, ports, and virtual links, while also making their campuses the default location for new workloads.

For our database, we have assessed \~80 specific providers across seven categories.

- Hyperscalers: Amazon (AWS), Google (GCP), $^{2}$ Microsoft (Azure), Oracle (OCP), $^{3}$ IBM Cloud, $^{4}$ Alibaba (on ramps only for first four) $^{5}$
- Tier 1 Global Transit Partners: Lumen, Arelion, Cogent, NTT, GTT, Zayo, Tata, TI Sparkle, Orange International, Telxius, PCCW Global, Vodafone Global Network, DT ICSS
- Content + CDN Providers: Cloudflare, $^{6}$ Akamai, Fastly, Netflix, $^{7}$ Meta, $^{8}$ Apple, $^{9}$ Valve, Twitch, ByteDance
• US / Canada ISPs: Comcast, Charter, AT&T, Verizon, T-Mobile, $^{10}$ Cox, Altice USA, Frontier, Bell Canada, Rogers, Telus

- Global ISPs: BT, Vodafone (consumer), Telefónica, $^{11}$ Iliad/Free, Sky, Liberty Global, KPN, Swisscom, Proximus, Telia (consumer), Telenor, $^{12}$ Türk Telekom; Singtel, Telstra, KDDI, SoftBank, $^{13}$ Reliance Jio, Airtel, SK Broadband, KT, Claro, Telmex
- Interconnect Economy Players: Hurricane Electric, Internet2, Megaport, Zscaler, $^{14}$ PacketFabric, Zenlayer, ESnet, and GÉANT
- Neoclouds: CoreWeave, Nebius, Lambda, Crusoe, Together AI, Vultr, Voltage Park, IREN, Applied Digital, NVIDIA NGC $^{15}$

EXHIBIT 6: % of Interconnected Facilities That Have at Least 1 Provider per Category


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 7: Average Number of Providers by Category Per Interconnected Building (Units)


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 8: AWS Cloud On-Ramps by Provider(Units, % of total provider locations)
AWS Cloud On-Ramps by Provider (Units, % of total provider locations)

[[KC_IMAGE_006]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 10: GCP Cloud On-Ramps by Provider (Units, % of total provider locations)
GCP Cloud On-Ramps by Provider (Units, % of total provider locations)

[[KC_IMAGE_007]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 9: Azure Cloud On-Ramps by Provider(Units, % of total provider locations)
Azure Cloud On-Ramps by Provider (Units, % of total provider locations)

[[KC_IMAGE_008]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

EXHIBIT 11: OCI Cloud On-Ramps by Provider (Units, % of total provider locations)
OCI Cloud On-Ramps by Provider (Units, % of total provider locations)

[[KC_IMAGE_009]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

## INTERCONNECTION IN AN AI WORLD

AI workloads change the physics of the data center: they increase power density, flip traffic patterns from north-south to heavily east-west, and massively increase the amount of data that needs to move quickly and repeatedly. Training large models requires shuttling huge datasets and model checkpoints between storage and GPU clusters, sometimes across multiple regions or clouds, and inference at scale benefits from being close to end users and data sources.

This intensifies several structural trends that favor interconnection-rich enterprise colo:

\- Data gravity and bandwidth: Moving multi-petabyte datasets over the public internet is slow and costly; private DCI and cross-connect fabrics are the only realistic way to keep GPUs fed without creating bottlenecks.

- Hybrid and multicloud AI: Enterprises are blending on-prem, colo, and hyperscale resources; they need a neutral staging ground where they can connect securely to multiple clouds and partners with low switching costs.
- Edge-connected AI: Inference increasingly runs near the edge (e.g., for video, industrial, or telco use cases), requiring robust metro and regional interconnection back to core training hubs for model updates and telemetry.

The net result is that “just” having a big powered shell is not enough. The winners in enterprise colo will be those that pair AI-ready power and cooling with dense, programmable interconnection fabrics that let customers architect AI pipelines flexibly and at scale.

EXHIBIT 12: Neocloud Interconnect Presence by Provider (Units)

[[KC_IMAGE_010]]


Source: PeeringDB, Company filings, Bernstein Data Center Interconnection Model, Bernstein Analysis and Estimates

## INTERCONNECTION ECONOMICS

Interconnection is one of the best businesses inside the data center business: it is high-margin, recurring, and benefits from the network effects discussed above. Cross-connects typically carry a recurring monthly charge plus a one-time install fee. The cost to provision and maintain those links (labor, panels, fiber, ports, and overhead) is modest relative to revenue, so gross margins on interconnection services are typically materially higher than on power and space. As a campus densifies, each new tenant adds disproportionate economic value because they are a potential cross-connect counterparty for every other tenant, driving up interconnection revenue per cabinet and lowering churn through ecosystem lock-in. This remains true even as cross-connects move from physical to virtual.

For a bullish enterprise colo thesis, the key point is that AI and cloud do not just drive more racks; they drive more ports per rack and more value per port. Providers that invest in carrier-neutral ecosystems, robust metro and inter-market fabrics, and automated provisioning should see interconnection as an expanding share of revenue and an even larger contributor to incremental EBITDA.

## INTERCONNECTION BY PROVIDER

EQIX has significant interconnection revenue - \$1.6B in 2025, growing at \~9% CAGR. DLR is much smaller with \$4'79M, growing around 8%. CoreSite is a much smaller company than either of the others, but is growing interconnection revenue at a healthy 13%

EXHIBIT 13: EQIX Interconnection Revenue Overview (\$M, %)

[[KC_IMAGE_011]]


Source: Company filings, Bernstein Analysis

EXHIBIT 14: DLR Interconnection Revenue Overview(\$M, %)

[[KC_IMAGE_012]]


Source: Company filings, Bernstein Analysis

EXHIBIT 15: Coresite Interconnection Revenue Overview (\$M, %)

[[KC_IMAGE_013]]


Source: Company filings, Bernstein Analysis

EXHIBIT 16: Interconnection Count by Company (Thousands)

[[KC_IMAGE_014]]


Source: Company filings, Bernstein Analysis

EXHIBIT 17: Monthly Interconnection Price by Company (\$)

[[KC_IMAGE_015]]


Source: Company filings, Bernstein Analysis

EXHIBIT 18: EQIX Monthly Interconnection Pricing (\$)
(\$)

[[KC_IMAGE_016]]


Source: Company filings, Bernstein Analysis

EXHIBIT 19: Interconnection Rev as % of Enterprise Revenue (%)
Interconnection Rev as % of Enterprise Revenue (%)

[[KC_IMAGE_017]]


Coresite Enterprise Revenues assumed to be Total Rev without Interconnection component
Source: Company filings, Bernstein Analysis and Assumptions

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 20: DLR Income Statement Overview
All values in millions, except per share data


Source: Company filings, Bernstein Analysis and Assumptions

EXHIBIT 21: EQIX Income Statement Overview
All values in millions, except per share data


Source: Company filings, Bernstein Analysis and Estimates

EXHIBIT 22: AMT Income Statement Overview
All values in millions, except per share data


Source: Company filings, Bernstein Analysis and Estimates
