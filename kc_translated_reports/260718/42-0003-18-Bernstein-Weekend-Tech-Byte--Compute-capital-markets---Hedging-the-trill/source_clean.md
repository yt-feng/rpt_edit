# Weekend Tech Byte: Compute capital markets - Hedging the trillion dollar AI capex cycle
## By Gautam Chhugani & Madison Rezaei
## FINANCIALIZATION OF COMPUTE

Spot compute markets include transactions for immediate access to available GPU capacity, where compute resources are rented at prevailing market prices for near-term workloads and delivery. Compute derivatives, just like other commodity derivatives, allow participants to lock GPU rental prices through forward position in GPU capacity. Buyers can lock their cost of training and inferencing workloads, sellers can forward sell their capacity before it is built, and lenders can hedge the capital they have committed to GPU buildouts. Over the last few months, both CME Group and Intercontinental Exchange announced plans to roll out regulated GPU compute futures, subject to CFTC review. The notable feature is not simply the futures contracts themselves but the broader market structure forming around them. Compute is acquiring, layer by layer, the same architecture every traded commodity market has (Exhibit 1):

\- Exchanges: Exchanges offer a centralized venue to match long and short positions for compute future contracts, building a transparent orderbook for a series of derivative contracts (across maturities, GPU models etc). Offshore exchanges have had a head start in offering derivative contracts on GPU compute prices due to their light-touch regulatory structure, however onshore platforms like Kalshi, ICE and CME (all not covered) are now catching up. Kalshi already offers event

contracts based on GPU prices, while ICE and CME have announced plans to roll out regulated GPU compute futures in late 2026, subject to CFTC review.

\- Indices: Financial markets tend to settle around a few accepted reference prices because everyone wants to transact against the same benchmark. The current compute market is fragmented across different private and public players, without a transparent spot or forward pricing curve. Platforms like Silicon Data (partnered with CME), Ornn (partnered with ICE, Kalshi) and Compute Desk (partnered with Architect) are trying to aggregate data on GPU prices, standardize them for different variations and build benchmarks for GPU pricing.

\- Liquidity and participation: We are seeing constant product launches tailored for various market participants - hyperscalers (compute buyer), neoclouds (compute seller), lenders and arbitrageurs. Initial liquidity on existing products remain nascent and dominated by speculative flows. However, as regulatory structure around compute markets evolve and participants realize the product-market fit for compute markets, liquidity should follow.

We think the closest parallel for compute is power. Electricity was once dismissed as untradeable as it cannot be stored, varies by location and quality - until standardized hubs and reference prices turned forward procurement into a financial market. Compute is following the same sequence, because it shares the same physics - GPU hours cannot be stored, capacity varies by location, chip

generation and tenant. So the forward curve reflects expected scarcity rather than storage cost, and hedging is the only way to carry price risk.

Platforms are now trying to solve the problem of standardizing compute (benchmarks and per GPU hour approach), develop both cash settled and physical delivery rails for forward contracts and build structured financial products on underlying compute. Our view is that benchmarks and distribution are the key factors for growth of compute markets - not different from any commodity financial markets.

EXHIBIT 1: Participants in the compute market

[[KC_IMAGE_001]]

Source: Architect, Bernstein analysis

## THE COMMODITY TEST FOR COMPUTE - CLOSEST ASSET CLASS PARALLEL

The closest parallel for compute is the existing market for commodities, particularly electricity.

\- Fungibility & measurable supply - imperfect but workable: Fungibility means that individual units of an item are completely interchangeable. An H100 hour from Ohio (for instance) is not identical to that from Texas, due to different networking, SLA requirements, and deployment environments. Compute markets are broadly following two approaches for fungibility (i) rolling out contracts with standardized terms across chip models, server interfaces, duration etc; and (ii) allowing parties to directly negotiate the grade, timing and location of compute capacity using a basis (price adjustment) on the standard futures price.

\- Storability - Compute is non-storable: An unused GPU-hour disappears forever, with no possibility of warehousing, shipping or holding inventory against future demand. This makes compute resemble electricity where forward markets reflect expected scarcity rather than inventory dynamics.

\- Price volatility - high, hence demand for hedging is real: Volatility is a prerequisite for any derivative market to grow.

GPU chip shortages and hardware generation change (e.g., H100 to B200) cause price volatility in compute markets. On one side sit neoclouds/cloud operators, many owning large fleets of depreciating GPUs. On the other side, we have AI labs and enterprises whose economics depend on future costs of compute, hence there is a presence of both natural buyers and natural sellers in the market.

The market structure for compute markets is still evolving with constant new product announcements and strategic partnerships. The market is still trying to solve for three key questions - (i) Standardizing compute: standardizing the spot and forward pricing curve for compute and building commonly accepted indices; (ii) Product-market fit: building various financial products like futures, perpetuals, event prediction contracts and determining the right fit for different participants; and (iii) Settlement: building infrastructure for both cash and physical settlement of contracts. Industry participants are experimenting with multiple approaches to build a market structure that integrates pricing, product and settlement. We outline a few approaches in the next sections.

## STANDARDIZING COMPUTE - BUILDING BENCHMARKS

Every commodity market begins by answering: what exactly is one unit? Oil solved it decades ago through standardization - a specific grade, quantity and delivery specification. Compute is beginning to solve the same problem but the task of an index provider is similar to an electricity market operator - taking a highly heterogeneous product and building a tradeable reference price for it. The problem is that raw compute prices are not comparable across the market as the same H100 can be priced differently (Exhibit 7) depending on whether rented from neocloud, hyperscaler tiers or public listings. This spread reflects material differences in technical factors (networking) or non technical factors (SLA, support, value add, counterparty quality).

The solution comes from building a benchmark that takes scattered, non-comparable prices from various sources and produces one number the market can transact on. The process can be envisaged in 3 steps:

Step 1 - Data collection and standardization: The index provider needs to define the 'unit', for instance, NVIDIA H100 SXM 80GB (includes server, memory, bandwidth etc.). Further specifications include tier (neocloud/hyperscaler), type of lease (on-demand/committed term) and normalization steps for region and configuration. To ensure that the index moves because of the market and not because of error in sampling, all observations/transactions are normalized to the 'reference unit'. Silicon Data (Exhibit 2) collects a broad set of data -150K daily verified pricing records across 50 regions/countries covering 50-100 platforms across hyperscalers, neoclouds and marketplaces, (link). The data undergoes capture and standardization across pricing structures (lease type/duration), providers and locations and granular hardware specifications and then normalizes prices of heterogeneous physical units to a standard configuration to ensure only comparable price signals are aggregated. Ornn works on transaction based pricing basis ‘negotiated transaction prices’ between data centers and compute buyers tracking rental pricing across GPU models with pricing normalized across hardware configuration, provider, and deployment context.

Step 2 - Benchmark/index: The standardized data becomes a reference index. Silicon Data indices capture prices on every business day, use statistical techniques to filter out stale or non-representative data and undergoes validation procedures to ensure integrity of the index. The need for a benchmark has prompted even legacy financial exchanges such as CME, ICE to partner with Silicon Data and Ornn. CME/Silicon Data and ICE/Ornn partnerships focus on financialization of the compute market and that largest demand will come from investors looking to hedge AI spending rather than physical delivery of GPUs. CME and ICE are leveraging their established positions and existing ecosystem to promote trading activity.

A new exchange focused on AI compute, Architect (private) has multiple partnerships - (i) Ornn for its compute perpetuals whose benchmarks are based on live GPU data from spot markets, which is already live. AX is Architect's offshore (Bermuda-regulated) exchange for perpetual futures across traditional assets and compute; (ii) ComputeDesk (brand of The Compute Index Inc.) for ComputeConnect, and EFP (Exchange for Physical) network that links compute futures on the AI Exchange with actual GPU capacity delivery via Compute Desk's Compute Clear platform.

Step 3 - Forward curves: As compute cannot be stored (electricity analogy), there is no cost of carry to pin forward prices to spot prices and the curve must be derived from market observations. Forward curve is currently published by Silicon Data and Kalshi (Exhibit 6). The shape of the curve is based on expectation of future scarcity rather than a function of inventory. The two main concepts regarding the curve are:

\- Curve in Contango: Upward sloping with future prices above spot prices, means that the market expects scarcity to persist or worsen.

\- Curve in Backwardation: Downward sloping with future prices below spot prices, means the market expects supply wave to come in and hardware depreciation to take a toll, hence, buyers expect to pay less later.

EXHIBIT 2: Data collection methodologies for compute price calculation


\*AX - Architect's offshore AX Exchange;
Silicon Data, Ornn, Kalshi, Architect, ICE, CME - not covered
Source: Company websites, ICE, CME, Bernstein analysis

## PRODUCTS - FUTURES, PERPETUALS, EVENT CONTRACT

A layered market of financial instruments is now emerging for compute, with different instruments tailored for different use cases. Players like ICE, CME, Architect and Kalshi are developing a series of derivative products on compute prices (Exhibit 3) including index settled futures, physically settled futures, perpetual futures and compute event contracts. These products are still at a nascent stage of adoption as companies are still building the required distribution and settlement infrastructure.

ICE, CME, Architect's American Innovation Exchange (Index settled futures) CME (using Silicon Data), ICE (using Ornn) and Architect (using Compute Desk) have announced futures contracts on GPU rental rates targeted for late 2026, pending regulatory review. Index settled futures are standardized contracts on GPU rental price indexes, just like futures on other commodities. Buyers of compute lock in training and inference costs, sellers forward-sell capacity that they are planning to build and lenders can hedge the value of GPU collateral. The contracts are quoted in dollars per GPU hour and get settled in cash against the benchmark index. No hardware changes hands as contracts settle in dollars against the reference index, exactly like cash-settled equity derivatives.

Kalshi and Polymarket (Event contracts) Prediction market platforms like Kalshi (CFTC-regulated) and Polymarket offer event contracts on GPU rental prices. For example, a typical compute event contract listed on Kalshi can be “Price of NVIDIA B200 above \$7 by end of 2026?” - specifying the GPU model, prices and duration. The contract pays \$1 if the price is above \$7 on the settlement date and \$0 if not. Further, if the contract is trading at \$0.4, there is a 40% implied probability that B200 rental rates will exceed \$7 by the end of the year. Hence, compute contracts on prediction markets also help in building a probability distribution of future GPU prices. Kalshi is now aggregating data across multiple live contracts to derive a forward pricing curve for different GPU models.

## Architect's ComputeConnect (Exchange-for-physical)

Architect has announced ComputeConnect, an exchange that turns cash-settled compute futures into real, delivered GPU capacity. Exchange for physical products allows a futures position to be converted into actual GPU capacity through a physical settlement system. ComputeConnect operates with a network of neoclouds and capacity providers, allowing physical settlement (actual GPU capacity) through bilateral negotiations. Participants can swap a futures position for compute delivery, by negotiating the grade, timing and location of the physical delivery. Other compute market derivative products like index-settled futures, event contracts and perpetuals are mostly cash settled, only providing economic exposure to the participants and with no mechanism to actually fulfill their delivery requirements.

Architect's AX Perpetual Futures exchange: Architect's AX exchange already lists perpetual-style compute futures in the offshore markets. Perpetual futures are contracts with no expiry that track the spot index through a funding-rate mechanism, a structure that evolved in crypto markets. Perpetuals are among the early derivative products built for compute due to faster launch (via offshore structures) and bootstrapped liquidity from speculative flow. When perps trade above the tracked index, longs periodically pay shorts, which pushes the price back down (and vice versa). A persistent positive funding rate means the market is bullish on spot prices. Perpetual contracts can be a good hedge for neoclouds selling capacity on demand without having exposure to one future date or an enterprise buying on-demand compute.

EXHIBIT 3: Summary of market players by underlying financial structure and market mechanism


Forward curves are only live on Kalshi currently, rest may launch in future
Source: Company websites, Bernstein analysis

## SETTLEMENT INFRASTRUCTURE - CASH VS PHYSICAL DELIVERY

There are two settlement mechanisms in the derivatives market - cash settlement and physical settlement. In compute markets, cash settlement dominates today with every announced futures contract, perpetuals and event contracts settling is cash against a benchmark index.

Benefits of cash settlement: Cash settled products are easier to clear, margin and scale making them ideal for building financial markets for a new asset class. The contract settles based on the difference between the contract price and the benchmark index level in cash, without requiring physical settlement rails. This opens the market to a broader set of participants including lenders, market makers and arbitrageurs that might not be able to fulfill the physical settlement requirements.

Success of cash settled futures depends on the underlying benchmark. Compute capacity is still trading through private, negotiated deals, making it difficult to build a representative index for compute prices. However, compute market benchmarks continue to improve as pricing transparency improves in spot transactions and compute markets gain broader adoption.

Integrating physical settlement for compute capacity: Physical settlement anchors the futures market to the underlying asset - if futures trade above the spot price at expiry, sellers can deliver the capacity instead of cash settlement. This closes the price gap between futures and spot on contract expiry. Further, participants who require chips may prefer physically settled derivatives. Architect and ComputeDesk launched Compute Connect, the first compute exchange for physical delivery of GPU capacity. For example, an AI lab with a long position in H100 futures at \$2.3 per GPU hour, can convert its position into real capacity through ComputeConnect. The AI lab requests delivery on ComputeDesk's network of capacity sellers. The two parties negotiate an actual GPU capacity delivery agreement at the futures price, adjusted for chip configuration, location and other specifications.

## METRICS TO TRACK ON COMPUTE FINANCIAL MARKETS

Key metrics to track for compute markets - spot compute price curves, forward compute price curves and token cost curves. The market metrics are still at an early stage of development, and are built from limited heterogeneous data available for compute pricing.

\- Silicon Data and Ornn - Neocloud GPU rental index (Exhibit 4-Exhibit 5): Silicon Data and Ornn publish per hour GPU price index across GPU models like A100, H100 and B200. Silicon Data collects a broad set of data -150K daily verified pricing records across 50 regions/countries covering 50-100 platforms across hyperscalers, neoclouds and marketplaces. Ornn pricing model is based on negotiated transaction prices between data centers and compute buyers across GPU models. After data aggregation, Silicon and Ornn then standardize their data across hardware configuration, provider, and deployment context, and publish a daily index price.

\- Kalshi- forward curve (Exhibit 6): Kalshi recently launched GPU compute forward curves derived from their prediction market prices. Kalshi uses their live prediction market contracts to aggregate dispersed views on compute pricing that reflect market expectation for different maturities.

\- GPU spot pricing by tenant (Exhibit 7): Silicon Data tracks H100 pricing continuously across regions and provider types.

Using their internal price history, they have published data on how H100 rental prices have evolved over time for different parties- hyperscalers, neoclouds and marketplace.

\- Silicon Data LLM Token Expenditure Index (Exhibit 8): A daily statistical benchmark that measures the expenditure in the actively traded broad LLM market. The index is reported as price per 1 Mn tokens series, so the index level is a USD-per-million-tokens value rather than an index normalized to 100.

EXHIBIT 4: Rental index built for specific GPU models like H100, A100 and B200


[[KC_IMAGE_002]]

Based on Bloomberg Silicon Data Index Source: Bloomberg, Bernstein analysis

EXHIBIT 5: Ornn compute index across GPU families

[[KC_IMAGE_003]]

Source: Ornn, Bernstein analysis

EXHIBIT 6: B200 forward curve on Kalshi

[[KC_IMAGE_004]]

Forward prices as provided on Kalshi website
Source: Kalshi, Bernstein analysis

EXHIBIT 7: H100 spot pricing

[[KC_IMAGE_005]]

Silicon Data sourcing: Combination of internal tracking by Silicon Data with commonly observed public-market pricing
Source: Silicon Data, Bernstein analysis

EXHIBIT 8: LLM Token Expenditure Index from Silicon Data

[[KC_IMAGE_006]]

Source: Silicon Data, Bloomberg, Bernstein analysis

## BERNSTEIN TICKER TABLE


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
Source: Bloomberg, Bernstein estimates and analysis.
