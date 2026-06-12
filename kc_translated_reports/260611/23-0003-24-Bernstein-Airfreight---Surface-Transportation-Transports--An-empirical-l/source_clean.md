# Airfreight & Surface Transportation
# Transports: An empirical look at how much of the fulfillment market Supply Chain by Amazon could realistically eat
## Specialist Sales

Over the last several weeks, the market has been trying to gauge the potential for Amazon Supply Chain Services and what it could mean for the shipping market (UPS and FDX). In today's note, we lay out the supply chain math behind the structural limitations of a forward deployed inventory model and quantify what percent of the market might realistically use "Supply Chain by Amazon."

Background and context. Supply chains are engineered around specific strategic priorities that vary greatly across industries. Design choices reflect the product's characteristics (value density, shelf life, damage sensitivity, handling requirements), customer requirements (order quantity, speed, reliability, customization, kitting), and demand patterns (volatility, seasonality, geographic concentration). They are also shaped by cost-to-serve economics, as shippers work to minimize the sum of transport costs, inventory handling costs (including storage and real estate), and soft costs like financing, obsolescence, and markdowns. Because these factors vary across verticals, Amazon's supply chain is not suitable for many industries.

Our thesis: Amazon's forward-deployed (local-stocking) model is only suitable for a subset of supply chains. That model wins on “cheap-to-carry, fast-to-sell, low-value-density” assortments where the shipper lacks the volume to extract a strategic carrier discount. It is structurally uneconomic for “expensive-to-carry, slow-to-sell, high-value-density, heterogeneous” assortments (unless turns are unrealistically high). The decision between the two models comes down to the trade-off between Holding Costs, Slotting Costs, and Transport Savings (Exhibit 1). We reached this conclusion by building a comprehensive, transparent toy model to pressure-test the thesis and then abstracting the key findings to package in a more compact, tunable model (Exhibit 2). The key structural determinants on which companies might be able to use a forward inventory model like Amazon's are product value and how much of the transport savings can be realized (sensitivities in Exhibit 4). The cost wedge that decides it is not transportation, it is inventory carrying cost plus fixed slotting footprint.

We estimate an upper boundary of $\sim 20\%$ of current physical retail sales could be suitable for a forward-deployed model (Exhibit 5). Tolerance to data protection and service failure limit the realistic market to low-to-mid single digits (Exhibit 6), with sector level considerations laid out in Exhibit 7. Our goal here is to present a framework an investor can use to reach a conclusion on how big of a risk this is — as such, while we present our view, there is as much value in the analytical framework (and if you think more than 1 one in 5 suitable shippers might take the plunge, then the risk is higher).


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
AMZN estimate is Reported EPS; AMZN valuation is Reported P/E (x);
Note - target price not adjusted for FDX Freight split
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We do not see a significant risk to UPS and FDX parcel volume from Amazon's Supply Chain Services launch. Amazon has built an amazing fulfillment model, but supply chain constraints limit the addressable market to \~20% of the market (based on retail sales). Of that amount, data and service tolerance factors would likely further limit the risk to a low-to-mid single digit number. Like all things Amazon, one has to pay attention, but the inventory hit to higher value shippers will likely mean continued demand for longer distance transportation networks.

## DETAILS

Over the last several weeks, the market has been trying to gauge the potential for Amazon Supply Chain Services and what it could mean for the shipping market (UPS and FDX). In today's note, we lay out the supply chain math behind the structural limitations of a forward deployed inventory model and quantify what percent of the market might realistically use "Supply Chain by Amazon."

## BACKGROUND AND CONTEXT

Before we dig into the model, we are going to set the stage by saying that supply chains are not one size fits all. There is no one supply chain to rule them all. Supply chains are engineered around specific strategic priorities that vary greatly across industries. Design choices reflect the product's characteristics (value density, shelf life, damage sensitivity, handling requirements), customer requirements (order quantity, speed, reliability, customization, kitting), and demand patterns (volatility, seasonality, geographic concentration). They are also shaped by cost-to-serve economics, as shippers work to minimize the sum of transport costs, inventory handling costs (including storage and real estate), and soft costs like financing, obsolescence, and markdowns. High-velocity, low-value goods favor dense, forward-deployed networks that minimize last-mile cost and cycle time, while high-value, slow-moving assortments favor centralized inventory to preserve pooling benefits and reduce holding cost. Network topology (number and type of nodes), the balance between in-house assets and outsourced capacity, and the level of automation are all tuned to that specific mix of product, service promise, and economics. As a result, a grocery chain, a fashion retailer, and a B2B industrial distributor may all “ship boxes,” but the underlying supply chains are built to do very different jobs—and those structural differences determine whether a model like Amazon’s forward-deployed network is a natural fit or a fundamental mismatch. However impressive one thinks the pipes that Amazon has built may be, they may not work for every supply chain...but how do you support that conclusion with data?

## THE CRUX OF THE MATTER

Our thesis is based on the idea that the Amazon Supply Chain Services model forward deploys inventory closer to the customer to shorten lead times and lower transport costs at the expense of having more investment in inventory and facilities. The primary risk to UPS or FDX from Amazon “opening its supply chain” is the idea that other shippers will want to use that model. For a retailer operating out of a more traditional fulfillment center set up (call it 2-4 fulfillment centers + longer distance shipping via common carrier), the decision comes down The trade-off between a “local” inventory model like Amazon vs. a more “central” model across Holding Costs, Slotting Costs, and Transport Savings (as illustrated in Exhibit 1):

## EXHIBIT 1: The crux of our thesis: going local with something like Amazon SCS only makes sense if transport savings more than offset the cost of having and managing more inventory

i.e. negative $\Delta$ means local stocking is cheaper overall

# Δ (Local – Central) = Holding penalty + Slotting penalty – Transport savings

Forward deployment works only when delivery savings outweigh the inventory and operating cost of fragmenting stock across more nodes.

## Holding penalty

- Unit value — higher-value inventory makes each extra unit of safety stock more expensive to carry.
- Turn rate — slower-moving assortments lose more from breaking pooling and duplicating inventory across nodes.
- Network fragmentation — more stocking points increase required safety stock via the square-root-of-n effect.

## Slotting penalty

- Cube and handling profile — bulky, fragile, or awkward items consume more labor and constrained forward capacity.
• Assortment breadth — long-tail SKU sets are harder to justify in high-cost forward locations.
• Facility economics — dense, automated nodes favor standardized, parcel-friendly inventory over special-case product flows.

## Transport savings

- Distance to customer — the closer stock sits to demand, the more linehaul and last-mile cost can be reduced.
- Order urgency — categories where faster delivery changes conversion or loyalty create more economic upside.
- Parcelability — small, standard items capture the biggest savings from Amazon's high-density sortation and delivery network.

Source: Bernstein

We built a comprehensive, transparent toy model to pressure-test the thesis. The intent of the analysis is to expose the relationships underpinning supply chain trade-offs, and we were not trying to build an absolute forecast with any precision. The model compares two archetypes—a single pooled central node and a multi-node forward-deployed network—holding service levels constant and asking how the cost to serve changes when inventory is fragmented. Incremental inventory in the local model is driven by a damped square-root-of-n effect (partial loss of pooling), forward nodes carry a higher slotting cost because their space is scarcer and more operationally expensive, and forward deployment yields a transport benefit by shortening average delivery distance and lowering factor cost. At the SKU level, this structure favors low-value, high-turn, parcel-friendly items and penalizes high-value, slow-turn, bulky assortments; we then scale that intuition to retail verticals using industry sales weights and suitability scores, and further haircut the “structural” opportunity by asking what share of shippers are realistically willing to share data with Amazon and accept platform dependence. Once we had the comprehensive model built, we ran a number of sensitives and narrowed down the 10-12 key assumptions that matter. While the comprehensive model relies on over 50+ assumptions, we wanted to abstract away the noise and make the primary assumptions visible and tunable. The base calculation of the abstract model is shown below in Exhibit 2.

EXHIBIT 2: Quantifying the tradeoffs on whether a merchant might want to move to a forward-deployed inventory model like Amazon

Forward-Deploy Breakeven — How the Companion Model Computes the Decision

One equation: $\Delta$ (Local - Central) = Holding penalty + Slotting penalty - Transport savings $\rightarrow$ forward-deploy wins when $\Delta < 0$

INPUTS


DECISION


[[KC_IMAGE_001]]


WHAT THE STRUCTURE TELLS YOU

## Holding dominates

Spreading stock over 20 nodes multiplies safety stock by $\sim$ √N. At \$2,240/unit it is the single largest cost — and rises with value.

## Slotting is structural

Grows with SKU breadth, not unit value. Robotics (lower slot-cube) trims it, but cannot offset the holding penalty alone.

## Transport is the only win

Last-mile savings help, but are bounded by the recoverable per-unit gap — here just \$300k. It rarely outweighs the penalties, and is very difficult to scale.

Inv = average inventory units. frac = share of demand that loses pooling across nodes (default 20%). Parameters calibrated so the companion reconciles to the full toy model at base case.

Companion to SCS Toy Model V5

Source: Bernstein

## EXHIBIT 3: Our abstract toy model calculates the cost differential of deploying inventory locally

## Forward-Deploy Breakeven — Simple Companion Model

One decision: does stocking locally beat shipping from a central hub? $\Delta = Holding penalty + Slotting penalty - Transport savings$ . Local wins when $\Delta < 0$ .

INPUTS (edit yellow cells)


Total units shipped per year

Inventory value per unit (holding-cost driver)

Assortment breadth per local node

Forward-deploy footprint (1 = central)

Per-unit transport saving vs central long-haul

Shelf space per SKU — LOWER for robotic/Kiva

Slow-moving share that loses pooling

Pooled hub stock, calibrated to full model

Local = Central×[1+frac×(Vnodes-1)]

Extra inventory × value × holding rate

SKUs × slot cube × (nodes-1) × \$/cu ft

Demand × \$/unit × discount (negative = saving)

Negative $\Delta \rightarrow$ local stocking cheaper overall

Source: Bernstein

## EXHIBIT 4: The key structural determinants on which companies might be able to use a forward inventory model like Amazon's are product value and how much of the transport savings can be realized

## Breakeven map: unit value × transport-saving multiplier (Δ \$/yr)

Teal = forward-deploy wins ( $\Delta < 0$ ). Saving multiplier scales the recoverable \$10/unit baseline (1.0 $\times$ = full \$10; >1.0 $\times$ = extra line-haul/zone-skip savings — unbounded, not a % of cost). Local wins only in the low-value / high-multiplier corner.


Source: Bernstein

## ESTIMATING THE ADDRESSABLE MARKET

We now turn our attention to market sizing. We estimate an upper boundary of $\sim 20\%$ of retail sales could be suitable for a forward deployed model (Exhibit 5). Tolerance to data protection and service failure limit the realistic market to low-to-mid single digits (Exhibit 6), with sector level considerations laid out in Exhibit 7. Our goal here is to present a framework an investor can use to reach a conclusion on how big of a risk this is - as such, while we present our view there is as much value in the analytical framework (and if you think more than 1 one in 5 suitable shippers might take the plunge, then the risk is higher). There two sets of issues to consider:

\- Suitability: What percent of industry sales under consideration could use the Amazon supply chain model? We assign each retail vertical a 0–1 suitability score based on how its typical products line up with the conditions under which forward deployment beats centralization—low unit value, medium-to-high turns, parcel-friendly form factor, and meaningful transport savings after accounting for higher inventory and slotting costs.

\- Tolerance: How many companies in that industry would A) trust Amazon with the data and B) be OK riding second fiddle on the Amazon platform. For these factors, one has to take a more common sense approach. We apply data and platform tolerance scores (0–1) by asking, for each vertical, what fraction of shippers would realistically be willing to share detailed demand and customer data with Amazon and accept operational dependence on its network, including the risk that their boxes may be prioritized behind Amazon's own.

EXHIBIT 5: Directionally, we believe around 20% of retail sales ex auto could one day be suitable to a forward deployed model, but data and service tolerance will significantly limit the uptake


Potential store base retail at risk

Percent already sold online

Incremental market opportunity

21%

2%

20%


Percent already sold online

Incremental market opportunity

4%

2%

2%

Note: the TAM of \~20% could overstate the suitability of Amazon SCS, as economies of scale within an existing supply chain (and associated penalties for making a supply chain smaller

Source: US Census, Bernstein estimates and analysis

EXHIBIT 6: Not all that could use Amazon SCS will – data and service tolerance will significantly limit the addressable market
Sensitivity of Addressable Market to Data / Service Tolerance (averaged)


Source: US Census, Bernstein

EXHIBIT 7: At a sector level, merchants may or may not find Supply Chain by Amazon suitable while those that do still have to get over Data and Platform tolerance issues


Source: US Census, Bernstein

## MODELING NOTES

## HOLDING PENALTY

\- What it is: the extra annual carrying cost created when inventory is moved from one pooled, centralized node into many forward-deployed nodes.

- Why it happens: fragmented inventory loses pooling benefits, so the system needs more total safety stock to maintain the same in-stock rate.
- When it is largest: high-value, slow-turn, broad-assortment categories where each extra unit of duplicated inventory is expensive to hold.

## HOW IT IS CALCULATED

• Estimate the centralized inventory position for the SKU or category.
- Apply a multi-node inventory factor to estimate inventory required in the local model.
• Take the incremental inventory: local inventory minus central inventory.
- Multiply that incremental inventory by the annual holding-cost rate.
- Formula: Holding penalty = (Inventory\_local - Inventory\_central) × carrying-cost rate.

## MODEL ASSUMPTION

- We assume local inventory scales with a damped square-root-of-nn relationship rather than the full textbook square-root law.
- Specifically: Inventorylocal=Inventorycentral×[1+frac×(nodes−1)]Inventorylocal=Inventorycentral×[1+frac×(nodes−1)].
- In the base case, nodes = 20 and frac = 20%, implying an inventory multiple of about 1.69x versus a single centralized node. The pure square-root law assumes independent demand across locations, which would blow inventory up by nn when you go from 1 node to n nodes. In reality, store demands are correlated and networks use smarter policies, so you only see a fraction of that theoretical increase. The frac assumption we built into our toy model is essentially a realism knob that adjusts down the holding penalty.
• We apply the holding-cost rate only to the incremental 0.69x of extra inventory created by fragmentation

## SLOTTING PENALTY

- What it is: the extra annual operating cost of placing inventory into scarce forward-deployed capacity instead of a lower-cost centralized node. A typical fulfillment center might have up to 30% of the floor space dedicated to the physical presentation of inventory for picking, inclusive of robotics and runway.
- Why it happens: local fulfillment space is more constrained and more operationally expensive, so each unit stored there carries a higher slotting cost.
- When it is largest: bulky, awkward, fragile, or low-turn items that consume disproportionate space relative to the delivery savings they create.

## HOW IT IS CALCULATED

• Estimate the inventory volume that must be held in the local model.
- Apply the incremental slotting cost per unit for forward-deployed capacity versus central capacity.
- Multiply the local inventory position by that cost differential.
- Formula: Slotting penalty = Inventory\_local × (slotting cost\_local - slotting cost\_central).

## MODEL ASSUMPTION

- We assume slotting is a recurring capacity cost that applies to all inventory placed into the local network, not just the incremental safety stock.
- In the toy model, this is represented as a per-unit annual slotting charge on local inventory.
- The intuition is that every unit occupying forward space displaces other inventory in a dense, high-value node, so the economic test should price that constrained capacity explicitly.
- This makes the penalty especially relevant for slow-turn, cube-heavy, or broad-assortment categories where local space is consumed without enough transport savings in return.

## TRANSPORT SAVINGS

- What it is: the reduction in delivery cost created by positioning inventory closer to the customer in a forward-deployed network and using cheaper contractor / gig delivery drivers.
- Why it happens: local inventory shortens average ship distance and shifts volume out of longer, more expensive parcel and linehaul moves.
- When it is largest: small, parcel-friendly, high-velocity items where faster and shorter delivery materially lowers last-mile cost. Doesn't work for big and bulky.

## HOW IT IS CALCULATED

- Estimate the average cost to serve an order from the centralized model from market rate cards, assuming that a shippers discount from list scales with volume (making for hire market less expensive for larger shippers).
• Estimate the average cost to serve the same order from the local model based on parcel benchmarking.
• Take the difference: central transport cost minus local transport cost.
- Multiply by the annual order or unit volume that benefits from local fulfillment.
- Formula: Transport savings = (transport cost\_central - transport cost\_local) × annual volume.

## MODEL ASSUMPTION

- We assume forward deployment creates a fixed per-order or per-unit transport benefit for demand served from local nodes.
- In the toy model, that savings is the core economic offset to the holding and slotting penalties.
- The assumption is strongest for standardized parcel items that can fully use Amazon's dense sortation and last-mile network.
- The assumption is weaker for bulky, low-density, or low-urgency products where shorter distance does not translate into enough cost savings to pay for distributed inventory.
