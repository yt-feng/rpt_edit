# Weekend Tech Byte: Compute capital markets - Hedging the trillion dollar AI capex cycle

Gautam Chhugani +91 226 842 1416 gautam.chhugani@bernsteinsg.com

Madison Rezaei +1 917 344 8622 madison.rezaei@bernsteinsg.com

Mark L. Moerdler, Ph.D. +1 917 344 8506 mark.moerdler@bernsteinsg.com

Richard Nguyen +33 1 42 13 54 22 richard.nguyen@bernsteinsg.com

Peter Weed +1 917 344 8390 peter.weed@bernsteinsg.com

Mark Shmulik +1 917 344 8508 mark.shmulik@bernsteinsg.com

Harshita Rawat, CFA +1 917 344 8485 harshita.rawat@bernsteinsg.com

Stacy A. Rasgon, Ph.D. +1 213 559 5917 stacy.rasgon@bernsteinsg.com

Mark C. Newman +1 212 845 7822 mark.newman@bernsteinsg.com

Nikhil Devnani, CFA +1 917 344 8425 nikhil.devnani@bernsteinsg.com

Laurent Yoon +1 917 344 8502 laurent.yoon@bernsteinsg.com

Mahika Sapra +91 226 842 1408 mahika.sapra@bernsteinsg.com

Sanskar Chindalia +91 226 842 1445 sanskar.chindalia@bernsteinsg.com

Harsh Misra +91 226 842 1457 harsh.misra@bernsteinsg.com

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
![](images/f4414f08be71332755c3df6940dcc2eccb87de698cdf4d6f7d6196478fe796a1.jpg)  
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

<table><tr><td></td><td>Silicon Data</td><td>Ornn</td><td>Kalshi</td></tr><tr><td>Model (Data aggregation)</td><td>Aggregated and Normalized</td><td>Wholesale transaction based</td><td>Prediction Markets</td></tr><tr><td>Methodology</td><td>Gather global data points, use statistical techniques for normalization</td><td>Only cleared/settled transaction data</td><td>Price emerges from event trading contracts - positions forecast future price</td></tr><tr><td>Core product</td><td>SDH100RT index family (per SKU, tier, tenor)</td><td>OCPI reference index</td><td>Market implied forward curve from event contracts</td></tr><tr><td>Partners</td><td>CME - compute futures</td><td>ICE - compute futures + Kalshi contracts + AX* perps</td><td>Ornn (Kalshi contracts settle on Ornn index)</td></tr></table>

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

<table><tr><td></td><td>CME &amp; ICE</td><td>Architect (AX)</td><td>Architect - American Innovation Exchange</td><td>Kalshi</td></tr><tr><td>Contracts</td><td>Futures</td><td>Perps</td><td>EFP and Futures</td><td>Binary/Event contracts</td></tr><tr><td>Settlement</td><td>Cash settled</td><td>Cash settled</td><td>Physical (GPUs) or Cash</td><td>Cash (Binary payout)</td></tr><tr><td>Index</td><td>CME - Silicon Date ICE - Ornn</td><td>Ornn</td><td>Compute Desk</td><td>Ornn</td></tr><tr><td>Regulation</td><td>CFTC regulated - DCM, traditional clearing houses</td><td>Offshore (Bermuda), outside CFTC purview</td><td>US-DCM, Compute futures pending CFTC review</td><td>CFTC regulated - DCM (event driven binary options)</td></tr></table>

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

![](images/24e8a3a55d02f0cd27a8efbc1861bb49a493249e45ffc640d9fa53da356997aa.jpg)  
Based on Bloomberg Silicon Data Index Source: Bloomberg, Bernstein analysis

EXHIBIT 5: Ornn compute index across GPU families  
![](images/5cb02a76d8e980c339a722726d3a9e9e3ef38b1ef01d2d6c1d64ea8f1dcebdfd.jpg)  
Source: Ornn, Bernstein analysis

EXHIBIT 6: B200 forward curve on Kalshi  
![](images/f818d745ddc0d1938acdd47728702bd7446e88d4fbf1262283972930f3457745.jpg)  
Forward prices as provided on Kalshi website
Source: Kalshi, Bernstein analysis

EXHIBIT 7: H100 spot pricing  
![](images/6e75415f4d03ec41dc44a1109dcde52965de2d2fb740d8a29457a4613ba9a36b.jpg)  
Silicon Data sourcing: Combination of internal tracking by Silicon Data with commonly observed public-market pricing  
Source: Silicon Data, Bernstein analysis

EXHIBIT 8: LLM Token Expenditure Index from Silicon Data  
![](images/1427fb0766cf18ab6ccd9514b81392e6cb1319d42fade84d9a03f327d6be087e.jpg)  
Source: Silicon Data, Bloomberg, Bernstein analysis

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">16 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>HOOD (Robinhood)</td><td>O</td><td>USD</td><td>106.02</td><td>130.00</td><td>(17.6)%</td><td>USD</td><td>2.12</td><td>2.65</td><td>3.70</td><td>50.0</td><td>40.1</td><td>28.6</td></tr><tr><td>COIN (Coinbase )</td><td>O</td><td>USD</td><td>160.49</td><td>330.00</td><td>(80.0)%</td><td>USD</td><td>4.85</td><td>5.97</td><td>13.20</td><td>33.1</td><td>26.9</td><td>12.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,533.77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Robinhood Markets Inc

Robinhood is scaling up rapidly and is a cyclical business. As a consequence, we value HOOD using a $\sim 35x$ Price/2027E Earnings to arrive at our price target of \$130.

## Coinbase Global Inc.

We value COIN using a 25x Price/2027E Earnings, in-line with the average of similar crypto/fintech/broker peers, to arrive at our price target of \$330.

## RISKS

## Robinhood Markets Inc

Robinhood faces regulatory risks on its revenue model, particularly its PFOF model from SEC and other regulatory bodies. This also applies to the crypto trading business.

SEC has historically been harsh on crypto trading businesses, with focus on token trading platforms, as some tokens maybe considered securities.

Digital assets are a new asset class, with limited price history i.e Bitcoin itself is less than 14 years old. The remaining digital assets industry reflected by smart contracts and other blockchain applications is even younger and still evolving into its utility phase.

## Coinbase Global Inc.

1. Risk of fresh competition from international exchanges (e.g., Binance) and brokers (e.g., Robinhood, Schwab) causing pricing & market share pressure in the US home market.

2. Any delay in passing key regulation to establish the Digital assets regulatory framework in the U.S including risk of regulatory volatility from political changes (e.g., mid-term US elections).

3. Digital Assets are a new asset class with limited price history and often display high-beta volatility to changes in macro including any recessionary challenges in the US.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price

Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.2%</td><td>15.3%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>35.8%</td><td>16.2%</td></tr><tr><td>Underperform</td><td>SELL</td><td>13.1%</td><td>13.6%</td></tr></table>

As of June 30, 2026. All figures are updated quarterly.

## PRICE CHARTS / RATINGS AND PRICE TARGET HISTORY

Prior to April 1, 2024, Bernstein & Co., LLC. issued the ratings and price target information in the graph(s) below for the following companies: Coinbase Global Inc..

Robinhood Markets Inc (HOOD) Rating History for Bernstein as of 07/16/2026  
![](images/dea90f598d84e2efefef7591adbbdbd58422226eac746a8d9e5ce0d8fbd9051c.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Coinbase Global Inc. (COIN) Rating History for Bernstein as of 07/16/2026  
![](images/06361df31c5faac37fce300e965a4776e35750bfb9d2e60c87ab5770528ec3dd.jpg)

Robinhood Markets Inc and Coinbase Global Inc. are covered by both the Autonomous and Bernstein brands. For the research ratings and price target history please go to https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

All price target and closing price data in the chart(s) above are denominated in the currency noted in the Ticker Table of this report.

## CONFLICTS OF INTEREST

All statements in this report attributable to Gartner represent Bernstein's interpretation of data, research opinion or viewpoints published as part of a syndicated subscription service by Gartner, Inc., and have not been reviewed by Gartner. Each Gartner publication speaks as of its original publication date (and not as of the date of this report). The opinions expressed in Gartner publications are not representations of fact, and are subject to change without notice.

Gautam Chhugani and Stacy A. Rasgon maintains long positions in various crypto currencies.

Certain affiliates of Bernstein act as market maker or liquidity provider in the equities securities of: Robinhood Markets Inc and Coinbase Global Inc..

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

Separate branding is maintained for “Bernstein” and “Autonomous” research products.

\- Bernstein produces a number of different types of research products including, among others, fundamental analysis and quantitative analysis under both the “Autonomous” and “Bernstein” brands. Recommendations contained within one type of research product may differ from recommendations contained within other types of research products, whether as a result of differing time horizons, methodologies or otherwise. Furthermore, views or recommendations within a research product issued under one brand may differ from views or recommendations under the same type of research product issued under the other brand. The Research Ratings System for the two brands and other information related to those Rating Systems are included

in the previous section.

\- Autonomous operates as a separate business unit within the following entities: Bernstein Institutional Services LLC, Bernstein Autonomous LLP, Bernstein (Hong Kong) Limited 盛博香港有限公司 and Bernstein (India) Private Limited. For information relating to “Autonomous” branded products (including certain Sales materials) please visit: www.autonomous.com. For information relating to Bernstein branded products please visit: www.bernsteinresearch.com.

Analysts are compensated based on aggregate contributions to the research franchise as measured by account penetration, productivity and proactivity of investment ideas. No analysts are compensated based on performance in, or contributions to, generating investment banking revenues.

This report has been produced by an independent analyst as defined in Article 3 (1)(34)(i) of EU 596/2014 Market Abuse Regulation (“MAR”) and the same article of MAR as it forms part of United Kingdom domestic law by virtue of the European Union (Withdrawal) Act 2018.

To our readers in the United States: Bernstein Institutional Services LLC, a broker-dealer registered with the U.S. Securities and Exchange Commission (“SEC”) and a member of the U.S. Financial Industry Regulatory Authority, Inc. (“FINRA”) is distributing this publication in the United States and accepts responsibility for its contents. Where this material contains an analysis of debt product(s), such material is intended only for institutional investors and is not subject to the US independence and disclosure standards applicable to debt research prepared for retail investors.

Bernstein Institutional Services LLC may act as principal for its own account or as agent for another person (including an affiliate) in sales or purchases of any security which is a subject of this report. This report does not purport to meet the objectives or needs of any specific individuals, entities or accounts.

To our readers in Canada: If this publication pertains to a Canadian domiciled company, it is being distributed in Canada by Bernstein (Canada) Limited, which is licensed and regulated by the Canadian Investment Regulatory Organization. If the publication pertains to a non-Canadian domiciled company, it is being distributed by Bernstein Institutional Services LLC, which is licensed and regulated by both the SEC and FINRA, into Canada under the International Dealers Exemption.

This document may not be passed onto any person in Canada unless that person qualifies as "permitted client" as defined in Section 1.1 of NI 31-103.

To our readers in Brazil: This report has been prepared by Bernstein Institutional Services LLC, and Banco BTG Pactual S.A. ("BTG") is responsible for the distribution of this report in Brazil.

To readers in the United Kingdom: This publication has been issued or approved for issue in the United Kingdom by Bernstein Autonomous LLP, authorised and regulated by the Financial Conduct Authority and located at 60 London Wall, London EC2M 5SH, +44 (0)20-7170-5000. Registered in England & Wales No OC343985.

This document is for distribution only to persons who (i) have professional experience in matters relating to investments falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the “Financial Promotion Order”), (ii) are persons falling within Article 49(2)(a) to (d) (“high net worth companies, unincorporated associations, etc.”) of the Financial Promotion Order, (iii) are outside the United Kingdom, or (iv) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the FSMA) in connection with the issue or sale of any securities may otherwise lawfully be communicated or caused to be communicated (all such persons together being referred to as “relevant persons”). This document is directed only at relevant persons and must not be acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this document relates is available only to relevant persons and will be engaged in only with relevant persons.

To our readers in the member states of the EEA: This publication is being distributed by BSG France SA, which is authorised and regulated by the Autorité de Contrôle Prudentiel et de Résolution (ACPR) and Autorité des Marchés Financiers (AMF).

To our readers in Hong Kong: This publication is being distributed in Hong Kong by Bernstein (Hong Kong) Limited 盛博香港有限公司, which is licensed and regulated by the Hong Kong Securities and Futures Commission (Central Entity No. AXC846) to carry out Type 4 (Advising on Securities) regulated activities and subject to the licensing conditions mentioned in the SFC Public Register (https://www.sfc.hk/publicregWeb/corp/AXC846/details)). This publication is solely for professional investors, as defined in the Securities and Futures Ordinance (Cap. 571). The purpose of this report is solely to provide an analysis of the issuers referred to in this report and is not intended for any purpose contrary to the laws of Hong Kong.

To our readers in Singapore: This publication is being distributed in Singapore by Bernstein (Singapore) Private Limited, only to accredited investors or institutional investors, as defined in the Securities and Futures Act 2001 of Singapore ("SFA"). Recipients in Singapore should contact Bernstein (Singapore) Private Limited in respect of matters arising from, or in connection with, this publication. Bernstein (Singapore) Private Limited is regulated by the Monetary Authority of Singapore and licensed under the SFA as a capital markets services licence holder for dealing in capital markets products that are securities and collective investment schemes and an exempt financial adviser for advising on, issuing and promulgating analyses and reports on securities. Bernstein (Singapore) Private Limited is registered in Singapore with Company Registration No. 20213710W and located at 8 Marina Boulevard, #12-01, Marina Bay Financial Centre, Singapore 018981, +65-6326-7000.

To our readers in the People's Republic of China: The securities referred to in this document are not being offered or sold and may not be offered or sold, directly or indirectly, in the People's Republic of China (for such purposes, not including the Hong Kong and Macau Special Administrative Regions or Taiwan, the "PRC") in contravention of any applicable laws of the PRC.

This document does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC to any person to whom it is unlawful to make the offer or solicitation in the PRC.

We do not represent that this document may be lawfully distributed, or that any securities may be lawfully offered, in compliance with any applicable registration or other requirements in the PRC, or pursuant to an exemption available thereunder, or assume any responsibility for facilitating any such distribution or offering. In particular, no action has been taken by us which would permit a public offering of any securities or distribution of this document in the PRC. Accordingly, the securities are not being offered or sold within the PRC by means of this document or any other document. Neither this document nor any advertisement or other offering material may be distributed or published in the PRC, except under circumstances that will result in compliance with any applicable laws and regulations.

To our readers in Japan: This publication is being distributed in Japan by Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社), which is registered in Japan as a Financial Instruments Business Operator with the Kanto Local Finance Bureau (registration number: The Director-General of Kanto Local Finance Bureau (FIBO) No.3387) and regulated by the Financial Services Agency. It is also a member of Investment Management Association of Japan. This publication is solely for qualified institutional investors in Japan only, as defined in Article 2, paragraph (3), items (i) of the Financial Instruments and Exchange Act.

For the institutional client readers in Japan who have been granted access to the Bernstein website by Daiwa Group Inc. ("Daiwa"), your access to this document should not be construed as meaning that Bernstein is providing you with investment advice for any purposes. Whilst Bernstein has prepared this document, your relationship is, and will remain with, Daiwa, and Bernstein has neither any contractual relationship with you nor any obligations towards you.

To our readers in Australia: Bernstein (Hong Kong) Limited 盛博香港有限公司 is responsible for distributing research in Australia. It is regulated by the Securities and Exchange Commission under U.S. laws, by the Financial Conduct Authority under U.K. laws, which differs from Australian laws. Bernstein (Hong Kong) Limited 盛博香港有限公司 is exempt from the requirement to hold an Australian financial services license under the Corporations Act 2001 in respect of the provision of the following financial services to wholesale clients:

• providing financial product advice;

• dealing in a financial product;

\- making a market for a financial product; and

• providing a custodial or depository service.

To our readers in India: This publication is being distributed in India by Bernstein (India) Private Limited (SCB India) which is licensed and regulated by Securities and Exchange Board of India ("SEBI") as a research analyst entity under the SEBI (Research Analyst) Regulations, 2014, having registration no. INH000006378 and as a stock broker having registration no. INZ000213537. SCB India is currently engaged in the business of providing research and stock broking services. Please refer to www.bernsteinresearch.in for more information.

\- SCB India is a Private limited company incorporated under the Companies Act, 2013, on April 12, 2017 bearing corporate identification number U65999MH2017FTC293762, and registered office at Level 3A, 4th Floor, First International Financial Centre, Plot Nos C-54 and C-55, G Block, Near CBI Office, Bandra Kurla Complex, Bandra (East), Mumbai 400098, Maharashtra, India (Phone No: +91-22-68421401).

\- For details of Associates (i.e., affiliates/group companies) of SCB India, kindly email MUM-BERNSTEIN-InCompliance@bernsteinsg.com.

• SCB India does not have any disciplinary history as on the date of this report.

\- Except as noted above, SCB India and/or its Associates (i.e., affiliates/group companies), the Research Analysts authoring this report, and their relatives

• do not have any financial interest in the subject company

• do not have actual/beneficial ownership of one percent or more in securities of the subject company;

\- is not engaged in any investment banking activities for Indian companies, as such;

• have not managed or co-managed a public offering in the past twelve months for any Indian companies;

\- have not received any compensation for investment banking services or merchant banking services from the subject company in the past 12 months;

• have not received compensation for brokerage services from the subject company in the past twelve months;

\- have not received any compensation or other benefits from the subject company or third party related to the specific recommendations or views in this report; and

\- do not currently, but may in the future, act as a market maker in the financial instruments of the companies covered in the report.

\- do not have any conflict of interest in the subject company as of the date of this report.

\- Except as noted above, the subject company has not been a client of SCB India during twelve months preceding the date of distribution of this research report. Neither SCB India nor its Associates (i.e., affiliates/group companies) have received compensation for products or services other than investment banking, merchant banking or brokerage services from the subject company in the past twelve months.

\- The principal research analyst(s) who prepared this report, members of the analysts' team, and members of their households are not an officer, director, employee or advisory board member of the companies covered in the report.

\- Our Compliance officer / Grievance officer is Ms. Rupal Talati, who can be reached at +91-22-68421451, or MUM-BERNSTEIN-InCompliance@bernsteinsg.com / Scbin-investorgrievance@bernsteinsg.com

\- The Research investor charter and Terms & Conditions of SCB India are available on its website and may be accessed at Bernstein (India) Private Limited (https://bernsteinresearch.in/) for your reference.

\- Disclaimer: Registration granted by SEBI, and certification from NISM, is in no way a guarantee of performance of the intermediary or provide any assurance of returns to investors. Investments in securities market are subject to market risks. Read all the related documents carefully before investing.

To our readers in Switzerland: This document is provided in Switzerland by or through Bernstein Autonomous LLP, and is provided only to qualified investors as defined in article 10 of the Swiss Collective Investment Scheme Act (“CISA”) and related provisions of the Collective Investment Scheme Ordinance and in strict compliance with applicable Swiss law and regulations. The products mentioned in this document may not be suitable for all types of investors. This document is based on the Directives on the Independence of Financial Research issued by the Swiss Bankers Association (SBA) in January 2008.

To our readers in the Middle East: Bernstein Autonomous LLP, DIFC branch has its principal office at Gate Village 06, DIFC, Dubai, UAE. Bernstein Autonomous LLP, DIFC branch is regulated by the Dubai Financial Services Authority (DFSA) with the registration number CL10040 and is provisioned for Arranging Deals in Investments and Advising on Financial Products. All communications and services are directed at Professional Clients and Market Counterparties only (as defined in the DFSA rulebook). Persons other than Professional Clients and Market Counterparties, such as Retail Clients, are not the intended recipients of our communications or services.

## LEGAL

All research publications are disseminated to our clients through posting on the firm's password protected websites, bernsteinresearch.com and autonomous.com. Certain, but not all, research publications are also made available to clients through third-party vendors or redistributed to clients through alternate electronic means as a convenience.

This publication has been published and distributed in accordance with the Firm's policy for management of conflicts of interest in investment research, a copy of which is available from Bernstein Institutional Services LLC, Director of Compliance, 245 Park Avenue, New York, NY 10167. Additional disclosures and information regarding Bernstein's business are available on our website www.bernsteinresearch.com.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. This publication is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of, or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or which would subject any of the entities referenced herein or any of their subsidiaries or affiliates to any registration or licensing requirement within such jurisdiction. This publication is based upon public sources we believe to be reliable, but no representation is made by us that the publication is accurate or complete. We do not undertake to advise you of any change in the reported information or in the opinions herein. This publication was prepared and issued by entity referred to herein for distribution to eligible counterparties or professional clients. This publication is not an offer to buy or sell any security, and it does not constitute investment, legal or tax advice. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with their professional advisors in light of their specific circumstances. The value of investments may fluctuate, and investments that are denominated in foreign currencies may fluctuate in value as a result of exposure to exchange rate movements. Information about past performance of an investment is not necessarily a guide to, indicator of, or assurance of, future performance.

This report is directed to and intended only for our clients who are “eligible counterparties”, “professional clients”, “institutional investors” and/or “professional investors” as defined by the aforementioned regulators, and must not be redistributed to retail clients as defined by the aforementioned regulators. Retail clients who receive this report should note that the services of the entities noted herein are not available to them and should not rely on the material herein to make an investment decision. The result of such act will not hold the entities noted herein liable for any loss thus incurred as the entities noted herein are not registered/ authorised/ licensed to deal with retail clients and will not enter into any contractual agreement/arrangement with retail clients. This report is provided subject to the terms and conditions of any agreement that the clients may have entered into with the entities noted herein. All research reports are disseminated on a simultaneous basis to eligible clients through electronic publication to our client portal.

The information in this report was prepared by Bernstein solely for the internal business use of our clients. Clients may store, display, analyze, reformat and print the information in this report for this limited use only. Clients may not copy, alter, create derivative works, resell, reverse engineer, commercially exploit, share or distribute any part of the information contained herein for any purpose without Bernstein's express written consent. These restrictions include extracting data or using the content to develop indices or other products. Further, you may not use this report, or any portion of this report, to train or finetune any third-party machine learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.