# U.S. Multi Industry & Electrical Equipment
# Data Center Chillers (1/3): Primer and free cooling economics

Chillers are a critical part of data center cooling infrastructure both in liquid-cooled and air-cooled environments. They are responsible for creating chilled facility water that then pumps to CDUs to extract heat from the coolant or to CRAHs to reduce the temperature of air blowing through the data center. We size this as a \~\$8B market in 2026 (fully loaded cost including installation and ancillaries), but the growth outlook can vary significantly based on how you think chiller penetration changes. Assuming no such changes (our base case), we project a \~20% CAGR for the market with 2030 estimated at \~\$16.5B.

We often hear debates of when it makes sense to use air-cooled vs. water cooled units. As a quick primer, both types of chillers operate using a refrigerant cycle, but air-cooled units reject heat from the refrigerant into ambient air, while water-cooled units reject to another water loop (either a cooling tower or a dry cooler). Air-cooled units are lower capex, but much less energy efficient. Water-cooled units need more upfront investment and consume large quantities of water (if a cooling tower is used), but tend to consume less power for the same tonnage. So it really is a sensitivity analysis of what you think your operating conditions and input costs will be when making the decision.

To illustrate this, we looked at how much it would cost to run an 800 ton chiller (roughly 2.5 MW) - assuming it was air-cooled or water-cooled. When the compressor of the chiller ran 24X7, annual operating costs were roughly 25% higher for an air-cooled chiller vs. a water-cooled unit, implying a \~3 year payback on the cost differential. So water-cooled units are always better, right?

It is not that simple. This dynamic can change quite drastically when you take free-cooling into account. Free-cooling is a when the ambient temperature drops enough for the data center operator to tone down (and in some cases switch off) the compressor in the chiller. It's a bit of a misnomer, the cooling isn't entirely free (you still need some power) but it's a fraction of what you'd need with the compressor running at 100%.

Energy consumption drops significantly for both air-cooled and water-cooled units. However, water costs stay relatively constant for water-cooled chillers (assuming a cooling tower is used). So as you spend more time in a free cooling environment, you may run into a situation where it is actually cheaper to operate an air-cooled chiller vs. a water-cooled chiller. This could be why we are hearing people talk about air-cooled chillers gaining share in the market.

We also spent some time benchmarking chiller offerings by key players available or announced in the market (like we did with our earlier primer on CDUs). We do not find the differences to be as stark; while there are some variations between companies, and they all have their own edge, we think these variations in specs are far outweighed by the overwhelming supply shortage and demand we are seeing for chillers today.

This is the first of our three part series on chillers. In part two, we will discuss “chiller gate” in more depth and in part three dive into the economics of servicing a chiller unit.

## BERNSTEIN TICKER TABLE


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate TT Outperform with a target price of \$550.

We rate CARR Market-perform with a target price of \$75.

We rate JCI Outperform with a target price of \$176.

We rate VRT Outperform with a target price of \$416.

Annual Operating costs (water + power)

EXHIBIT 1: When should you buy an air-cooled vs. water-cooled chiller?
Annual OpEx differential in an 800-ton chiller (air-cooled vs. water-cooled)

[[KC_IMAGE_001]]

If cooling tower needs to be active (which we think it does) to enable free cooling in a water-cooled chiller, water usage makes an air-cooled chiller seem more attractive in free-cooling heavy environments
However, this is based on national averages for power and water costs; reality-will look quite different based on the region of operation
Source: Bernstein Analysis and Estimates

EXHIBIT 2: Trade-offs by chiller type and regional variation
Deciding between air-cooled and water-cooled chillers based on geography

[[KC_IMAGE_002]]

Note: Power costs are \$10.25, \$6.26, \$6.7, \$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from EIA; Water costs are \$12.5, \$11, \$20, \$10 for NoVa, DFW, ATL, ORD pulled from regional sites (actual industrial rates may vary); Numbers by region assume an 800-ton chiller operating


[[KC_IMAGE_003]]


Source: Bernstein Analysis

## What is a chiller?

A chiller is a piece of equipment, which, as the name suggests, reduces the temperature of a stream of matter (usually a liquid). In the context of a data center, chillers are useful not only for liquid cooling (to cool the FWS) but also in air cooled environments where cold water flows to a CRAH to reduce the temperature of air that flows through it. Any chiller runs through a refrigerant compression cycle; this has four stages of operation as described below.

Evaporator: The warm liquid that needs to be chilled exchanges heat with cold liquid refrigerant in the chiller. This refrigerant picks up heat from the warm water and cools it, evaporating in the process.

Compressor: The most energy intensive part of a chiller. A compressor (scroll, screw, centrifugal) compresses the gaseous refrigerant, increasing its temperature. This is done to create a higher temperature gradient which makes heat transfer easier at a later stage.

Condenser: The hot, high-pressure, gaseous refrigerant comes into thermal contact with another stream of heat rejection (usually cool water in the case of a water-cooled chiller or ambient air in the case of an air-cooled chiller). The difference in temperature between the hot refrigerant and the cool heat sink facilitates heat rejection from the former to the latter. The refrigerant temperature lowers, and it condenses as a result (reverting to a liquid state).

Expansion valve: High pressure, liquid refrigerant passes through an expansion valve. This rapidly reduces pressure, which in turn reduces the temperature of the refrigerant (but keeps it in a liquid state). From here, the liquid refrigerant flows back to the evaporator and the cycle repeats.

EXHIBIT 3: Physics of Chiller Operation

[[KC_IMAGE_004]]


## Types of chillers

In general, comparisons are made between two types of chillers - air-cooled and water-cooled. The differences due to how the condenser rejects heat to the environment; if air is used it is air-cooled, if water is used (either through a dry cooler, or more commonly a cooling tower) it is water-cooled. There are some performance trade-offs from choosing one type of chiller vs. another. Air-cooled units are much less energy efficient (\~30% worse than water-cooled unit) but have lower up front capex and do not require any water to operate. In contrast, water cooled chillers are much better at heat transfer to the environment, so the compressor needs to do less work reducing their energy bill. But they do need water in most cases (although some dry cooler configurations solve that issue) which can shift the balance (especially in free-cooling environments where power usage for both air-cooled and water-cooled chillers drops significantly while water consumption stays relatively constant). We explore this cost-benefit analysis later in our note.

EXHIBIT 4: Air-cooled vs. Water-cooled Chillers

[[KC_IMAGE_005]]

Source: Bernstein Analysis and Estimates, Company Reports

More as a point of clarification, we would also like to highlight the different types of compressors in chillers. OEMs regularly talk about scroll vs. screw vs. centrifugal chillers, and it is worth understanding how they differ. Scroll chillers generally do not see data center applications; they are small, simple, silent units with limited ability to scale. Screw compressors are mid-sized units and see data center deployment. They are more complex and better at handling variable loads. Finally, centrifugal compressors see deployment in large scale data center environments; most OEM flagship products launched today are centrifugal chillers. These are the most complex, and require significant engineering to stand up but also deliver the most cooling power.

EXHIBIT 5: Comparison of compressors

[[KC_IMAGE_006]]

Source: Images from Atlas Copco and Engineeringlearn.com

Most appropriate for data center loads

Source: Bernstein Analysis

## How big is the market?

We have seen a wide dispersion of market sizes for chillers. Part of it also depends on what you are referencing - just the unit, or all the ancillary pieces that come with it? We have used a top-down estimate to size the overall market using GW added as a starting point. While we do have a base / bull / bear case for chillers in the exhibit below, these are based on variation in chiller penetration (not in terms of GW added). Our approach is as follows.

First, we look at new GW capacity being added each year. This creates a thermal baseline in terms of power consumed. Most of that power is released from chips, with an additional factor (assumed to be 1.2x in our model) to account for power wastage and headroom for safety. Next, we assume a cost per ton of \$1,500. This is a blend of both air cooled and water cooled chiller capex and includes the unit, engineering + commissioning + any supporting equipment that is needed (pumps, cooling towers, etc.). Finally, we multiply this by the share of GW that are cooled using chillers (75% in 2026 since it is how the majority of cooling takes place, but with base, bear, and bull cases for chillers based on how that could evolve). We size the fully loaded market for chillers at \~\$8B in 2026, growing to \~\$16.5B in 2030 assuming chillers continue to cool the same share of DC compute. In our bear case, where dry coolers steal share, the number drops to \~\$9B, while in the bull case where chillers gain share we size it at \~\$20B. This implies annual growth rates of \~20%, <5%, and >25% in the base, bear, and bull cases respectively.

Naturally, this model is sensitive to any assumptions you may have (especially GW added which can vary substantially between sources). The benefit of our approach is that one can relatively easily modify these assumptions and see what the market would be accordingly.

EXHIBIT 6: Chiller Market Size (Fully loaded) by Scenario

[[KC_IMAGE_007]]

Source: Bernstein Analysis and Estimates, McKinsey Data Center Model (for GW), CSE mag for cost per ton with 3% annual inflation

## Air vs. Water ... what's better?

Both air-cooled and water-cooled chillers have clear niches. Generally, air-cooled chillers make more sense when power costs are low (because they consume more power at a given tonnage vs. water-cooled chillers) or if water costs are high / water is limited / unavailable. In contrast, water-cooled chillers make sense in water-rich environments / when water costs are low or when power costs are high (since they are more energy efficient). When running at 100%, the extra cost of using water in a water-cooled chiller is more than offset by the savings in power.

However, this dynamic does change when you start to leverage free cooling (especially if you have a water-side economizer). In this environment, the compressor is switched off / used less, significantly reducing power consumption. But water consumption from a cooling tower continues, which keeps water costs relatively constant. At very high free cooling ratios, this could mean that the power savings from using a water-cooled chiller are actually offset by the cost of water. Given the increased focus on

water management in data centers (some counties have even capped the amount of water a data center can consume) we think it could help make the case for air-cooled chillers long-term over water-cooled units. The only exception is when the water-cooled chiller uses a dry cooler vs. a cooling tower (which JCI now advertises as possible with their new York HT chiller unit, although this likely comes with higher power costs due to higher lift).

EXHIBIT 7: Water costs can overtake power in modes with high free cooling (assumes use of cooling tower)

[[KC_IMAGE_008]]

However, this is based on national averages for power and water costs; reality-will look quite different based on the region of operation

## Source: Bernstein Analysis and Estimates

There is some variation by geography, largely dependent on the ration of power to water costs. In areas like Atlanta, where water costs seem to be high, air-cooled outperform water cooled chillers with as little as 50% free cooling while in most other key data center markets in the US, it takes more free cooling before the attractiveness flips. We are hearing from players in the space that air-cooled chillers are gaining popularity over water-cooled units (although the latter still remains important).

EXHIBIT 8: Air-cooled vs. Water-cooled; when do you deploy it?

[[KC_IMAGE_009]]

Note: Power costs are \$10.25, \$6.26, \$6.7, \$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from EIA; Water costs are \$12.5, \$11, \$20, \$10 for NoVa, DFW, ATL, ORD pulled from regional sites (actual industrial rates may vary); Numbers by region assume an 800-ton chiller operating

Source: Bernstein Analysis and Estimates, EIA

We reached our estimates on water consumption using EPA guidelines on cooling towers; $\sim 1.8$ gallon per ton-hour of cooling as evaporation and another $\sim 0.5$ gallons per ton-hour for blow down (purge of liquid to eliminate dissolved solids).

EXHIBIT 9: How much water does a water-cooled chiller use?

[[KC_IMAGE_010]]

Source: EPA, Bernstein Analysis and Estimates

## Competitor benchmarking of products

Broadly, we think Trane, JCI, and Carrier all have strong products. On the air-cooled side, JCI and Carrier have announced new products in 2026 (we have not been able to find anything from Trane). As a result, some metrics (restart time, capacity per square foot) seem to lag flagship products from competitors (although it is very likely Trane will announce a new product at some point). Vertiv is taking a different positioning to the market with a trim cooler; it still has a chiller in it but seems to operate like a dry cooler for most of the time (enabling lower energy costs). Visually, it looks like an air cooled chiller. Vertiv does have a separate chiller line as well, but we could not find it displayed on their US website.

On the water cooled side, all three major chiller players have their own areas of differentiation. Trane has the biggest product at 21MW. JCI advertises its lift of $110^{0}\mathrm{F}$ which enables use of a dry cooler even in hot climates and eliminates water usage. Carrier talks about a short restart time under 3 minutes. Many of these products still do not have full spec sheets available, so we will need to wait and see before passing a verdict. But given the current market we are in, it really doesn't matter all that much. These are all great products (unlike with CDUs where we saw meaningful differentiation among Vertiv, Trane, Carrier, JCI) and given the commentary on demand, we expect these companies to continue to see strong order booking and the broader chiller space to remain capacity-constrained.

EXHIBIT 10: Comparison of flagship air-cooler chiller specs.


1. Magnetic Bearing Chiller Available, but not on US website and capacity is 2MW; uses high GWP refrigerant
Source: Bernstein Analysis, Company Reports

EXHIBIT 11: Comparison of flagship water-cooled chiller specs


Source: Bernstein Analysis, Company Reports

The authors would like to thank Bhavik Kotecha for his contributions to this note.
