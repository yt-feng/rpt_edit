# Unpacking TPU-As-A-Service

GOOGL is about to embark on a major new initiative to scale AI outside of its datacenter walls via a new economic model, initially with Anthropic, but potentially with others down the road. We think this effort could boost '28 cons. gross profit by 15% and OI by more.

The Key Take-Away: Google is about to kick off one of its largest new business models with the help of several partners, to increase AI capacity industry-wide. Most investors are aware of TPU-aaS given the commentary on the recent earnings call, but the magnitude of how big this effort could be is likely underappreciated by the Street. Semiconductor buysiders have a decent handle on this theme, but we think now is the time for the consumer internet buyside to take notice. TPU-aaS is where Google takes inventory and sells TPUs directly to customers as a merchant vendor. One only has to look at the \$811B (up +\$479B Q/Q) in purchase commitments buried in the 10-Q this week, the \$275B+ increase in backlog in the past 6 months, or AVGO's commitment of 20+ GWs, to start to see how massive this could be. We are raising our Google Cloud revenue and OI estimates significantly with this report, after a full rebuild of our model. We'd also point out that this effort may reverse some future capex growth (potentially downside to our \$500B '28 estimate), as this asset-light approach to AI infrastructure helps GOOGL's capital efficiency.

The TPU-aaS effort has implications for many companies across the AI ecosystem including:

\- Anthropic: gains additional control of its business model, vertically integrates, and is less exposed to restrictions around hyperscaler service agreements.

\- Broadcom: opens a substantial new revenue pool and diversifies its business to other partners (consistent with our semiconductor research team's companion report on this topic today).

\- Blackstone and others: allows the companies to scale up their investments into new AI infrastructure and financial vehicles.

\- Fluidstack: massively increases its footprint as a colo managed service provider (what the industry calls "smart hands", or managed kubernetes) outside of Google's walls. In our view, Fluidstack's recent fundraise may signal its intentions to become a TPU neocloud.

We view this new business model as a win-win across the ecosystem and should allow TPU to become more of an industry standard for AI developers and other AI labs.


Price Target USD 425.00 Unchanged

Price (23-Jul-26) USD 317.69

Potential Upside/Downside +33.8% Source: Bloomberg, BARC


[[KC_IMAGE_001]]

Source: IDC
Link to BARC Live for interactive charting

## U.S. Internet


BCI, US

## Background On TPU-As-A-Service

Two major announcements have happened in the past quarter that could be material to GOOGL financials over the coming years. The first was on May 18 $^{th}$ where Blackstone and Google Cloud set up a JV run by a former Google exec to provide TPU-as-a-service to customers, with the first 0.5 GWs coming online in '27 and more capacity into the future $^{1}$ . This was followed up by another mega-deal announcement forming an AI XPV Platform between Broadcom and Blackstone/Apollo, enabling as much as 20 GWs of AI capacity through 2028, with the first >1 GW coming online starting in "mid-2026" $^{2}$ . The latter will involve AI labs bringing both TPUs and other custom ASICs (OpenAI's Jalepeno, etc.) online.

For purposes of this report we only really care about the portion that flows through Google's P+L. These two entities could bring online 15-20 GWs of TPU-as-a-service AI cloud capacity outside of what Google is doing inside GCP.

## First Off, What Is TPU-As-A-Service (TPU-aaS)?

Historically, the only way an AI lab or enterprise customer could access AI specific compute running on Google's TPUs was via Google Cloud Platform (GCP). Customers would enter into agreements with Google to rent AI capacity on various terms. However, this is starting to change in '26 with the new "off platform" structures noted above. In the very near future, AI labs who are the largest buyers of AI compute (Anthropic, OpenAI, Meta, etc.) will be able to buy compute through a new vehicle that allows for more direct control. Broadcom explained it best in their press release: "It also establishes a scalable framework for future deployments of XPU-based compute capacity and networking to enable frontier model training and inference at the lowest cost and lowest power, significantly lowering per-token delivery costs."3 The XPU cost through this new entity is likely to be comparable to buying the same capacity through the existing cloud providers, but offers more control to the AI labs.

## TPU-aaS Entity Structure

Noted above, this new AI XPV Platform was announced in early June by Broadcom, Blackstone, and Apollo. Because we are conducting the analysis from the perspective of impact to GOOGL's shareholders, we are calling it TPU-as-a-service (while Broadcom calls it XPU as it involves non-TPU compute as well, like OpenAI's upcoming Jalepeno chip).

The XPV structure looks a lot like other AI lab compute structures, with a few key layers of the stack. First, Blackstone/Apollo would set up a SPV (special purpose entity) which is financed with equity and debt (collateralized by the compute assets). This SPV would subsequently buy the TPUs from Google, which are co-designed with Broadcom and manufactured by TSMC. These compute assets would go into a datacenter provided by another entity and managed by Fluidstack. Anthropic would then lease the capacity from the SPV at predetermined rates. We have attempted to illustrate this structure below.

FIGURE 1. A Hypothetical 1 GW TPU-aaS Structure

[[KC_IMAGE_002]]

Source: BARC Estimates, Company Disclosures

## What Is Google's Incentive?


## What Is Anthropic's Incentive? (Or Other AI Labs?)

Large AI labs have scaled on the back of cloud computing contracts, and while this has been a great "asset-light" way of building their businesses, limitations exist. GCP and AWS provide compute services to Anthropic and others, but that's basically it; the AI lab has zero rights beyond what is laid out in the agreement with the hyperscaler.

For Anthropic, the incentives around controlling its own infrastructure have many benefits to its business model. These include: 1) the company can customize compute more effectively at various layers, and owning compute (via SPV) allows much deeper root access to the TPUs that would not likely be granted within GCP, 2) the company can more easily vertically integrate, and 3) while unlikely to happen, controlling the compute insulates Anthropic's business model from any discrepancies in terms stated in hyperscaler cloud service agreements (i.e., violations of AUPs which can result in termination of said agreement).

## Google's Unit Economics

We estimate Google sells each TPU for around \$20k per unit to the SPV while likely earning around a 25% gross margin, or around \$5k gross profit per unit. Each GW in '26 can host around 700k units, or \~\$14B in revenue per GW to Google. Future clusters will have next-generation TPUs (8t, 8i, 9, etc.) whereby revenue per unit and revenue per GW likely moves upward like most compute systems going forward, illustrated below.

FIGURE 2. GOOGL Likely Earning \~25% GM On External TPU-aaS Sales


Source: BARC Estimates, Company Disclosures

Broadcom has stated that this new AI XPV initiative amounts to 20 GWs over the next few years. The company has also stated that OpenAI and a few others are designing custom XPUs that would be included in this 20 GWs but separate from Google. We estimate TPU may be as much as 15 GW of the total, illustrated below.

FIGURE 3. Broadcom/Blackstone/Apollo AI XPV Platform GW Breakdown


Source: BARC Estimates, Company Disclosures

Noted above, Google also has a similar JV structure (outside of Broadcom's announced 20 GW) where it invested alongside Blackstone into a new TPU-aaS entity run by former Google infra exec Ben Treynor Sloss that amounts to another 500 MWs in 2027 and "plans to scale significantly" into the future.

Both of these result in a total of 3.7 GWs in '27 and 11.5 GWs in '28 of potential TPU-aaS external sales, illustrated below.

FIGURE 4. GOOGL Could Have $15+$ GWs Online By 2028


For illustrative purposes
Source: BARC Estimates, Company Disclosures

Based on the capacity scaling noted above, and using the ASP for the TPUs noted above, we think TPU-as-a-service revenue can reach as much as \$250B in 2028, at which point would represent 35%+ upside to current consensus Alphabet revenue and 15% to gross profit.

FIGURE 5. TPU-aaS Could Represent $15\%$ Potential Upside To Consensus Alphabet GP In '28


For illustrative purposes

Source: BARC Estimates, Company Disclosures, Bloomberg Consensus as of 7/23/26

This new structure has many benefits to Anthropic's business model (or any other AI lab/TPU customer), noted above, but it also begs the question around just how much more or less a 1 GW TPU-as-a-service cluster may cost in terms of overall capex and annual opex, relative to Anthropic's ability to just rent TPUs directly from GCP. Below we attempt to illustrate a side by side comparison.

FIGURE 6. Difference In AI Lab Unit Economics For GCP Rental Vs.Owned TPU-aaS


2026E
Source: BARC Estimates, Company Disclosures

## What's Already Been Announced

Noted above, Broadcom/Blackstone/Apollo's AI XPV initiative spans 20 GWs through 2028. It is not yet clear how big the Blackstone-Google JV TPU project (outside of the AI XPV initiative) is going to be longer term but has already announced 500 MWs in '27. We have identified the first tranches of datacenters coming online to support these efforts from TeraWulf and others, illustrated below.

We estimate Google has around \$88B of TPU revenue in the backlog as of 2Q26. This number should ramp up to over \$300B cumulative over time, but obviously some revenue starts dropping out of the backlog once TPUs have been sold through.

FIGURE 7. What's Already Been Announced From Compute DC Providers


Source: BARC Estimates, Company Disclosures

## Estimate Changes and Valuation

We have done a complete overhaul of our Google Cloud segment to factor in TPU-aaS revenues and profits. Google's CFO provided some high-level explanation of how TPU-aaS may flow through the company's financial statements last night, and combined with the new inventory line on the BS and the \$811B in purchase commitments, we can now piece together what this may look like.

We fully appreciate that our estimates are moving upwards rather dramatically on this revision, but as of now this is our best estimate of how the next three years may play out.

FIGURE 8. Estimate Changes


Source: BARC Estimates, Company Reports

We have maintained our \$425 price target by rolling back our valuation framework to straight 2027 on an average of 25x EPS and 15x EBITDA (vs. 2027/2028 hybrid previously). This updated framework takes a more near-term view of TPU-aaS impact to GOOGL shares, but we'd note that flipping to straight 2028 would result in a much higher potential valuation, illustrated below. Given all the moving pieces and the heightened capex outlook, we felt it was prudent to use 2027 for now.

FIGURE 9. GOOGL Valuation


Source: BARC Estimates, Company Reports. Price as of 4pm EST on 07/23/26

## Income Statement

FIGURE 10. GOOGL Income Statement


Source: BARC Estimates, Company Reports

GOOGL: Quarterly and Annual EPS (USD)


Consensus numbers are from Bloomberg received on 23-Jul-2026; 12:50 GMT Source: BARC

Alphabet Inc. (GOOGL)


## U.S. Internet


Note: FY End Dec
Source: Company data, Bloomberg, BARC
Price (23-Jul-2026) USD 317.69
Price Target USD 425.00
Google continues to grow revenue and EPS at a \~20% CAGR on a normalized basis. The company continues to innovate its product, and its machine learning capabilities should help advertisers get higher ROI, causing them to continue to allocate their advertising budgets to Google.

## OVERWEIGHT

## Why OVERWEIGHT?

## Upside case USD 530.00

We expect Google to continue to take share from other channels in mobile advertising, and 50% of every incremental dollar going forward. Reduction of losses in "Other Bets" could be a source of upside to estimates.


Google is migrating toward lower-margin businesses and, having benefited from the substantial improvement in mobile monetization, the growth rate may decelerate going forward.

Upside/Downside scenarios


[[KC_IMAGE_003]]


I, Ross Sandler, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.
