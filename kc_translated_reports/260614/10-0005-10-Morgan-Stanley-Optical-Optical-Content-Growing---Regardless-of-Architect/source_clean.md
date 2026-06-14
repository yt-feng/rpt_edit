## Optical | North America
# Optical Content Growing – Regardless of Architecture

Recent debate about near-packaged vs. co-packaged optics (NPO/CPO) misses that optical content is largely tied to bandwidth needs. Debate likely prevents stocks from reaching bull cases in NT, but growing more encouraged on LITE, COHR, GLW as they pull back and content expansion still in early days.

## Key Takeaways

The challenges of moving to co-packaged optics (CPO) are not new, with network builders examining all alternatives in journey.
Regardless of whether 2.5D / 3D CPO or just NPO or OBO, the increase in optical content / lasers is driven by the need for more bandwidth.
■ More conservative assumptions on CPO adoption in 2028 likely keep stocks away from bull cases for now, but still seen largely as a timing issue.
- With fewer debates about bandwidth vs. architectures, we think the market has grown overly concerned on LITE / COHR / GLW and would be more positive on weakness.

Timing and exact architectures unknown, but regardless, optical content is rising. There has been meaningful volatility in LITE, COHR, GLW and the rest of the co-packaged optics (CPO) ecosystem over the last couple of weeks as timing questions re-emerged. We would note, adoption / timing have always been in question, as Tiffany Yeh / Andy Meng and myself have noted in multiple deep dives this year (see below for links), noting expectations for closer to 6-7mm optical engines of demand in 2027 (vs. some bullish investor expectations of 20-30mm). However, debating timeline of adoption misses that optical content is largely correlated to bandwidth needs – e.g., the more bandwidth, the more optics, whether that takes the form of co-packaged optics (CPO), near-packaged optics (NPO), or other optical formats. While given commitments of capacity as part of NVDA's equity investments in LITE, COHR, GLW likely prevent just instantly swapping one set of demand for another, we do think that these three vendors remain beneficiaries of the increase in optical content, particularly as it enters the scale-up domain. Lumentum echoed this sentiment in conference appearances this week and our HQ visit to Coherent yesterday noted similar takeaways.

MS & CO. LLC

## Meta A Marshall


## Antonio Jaramillo


MS TAIWAN LIMITED+

## Tiffany Yeh


[[KC_IMAGE_001]]


## TELECOM & NETWORKING EQUIPMENT


In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.


Exhibit 1: Optical Content Increasing, Discussion Is More Around Timing

[[KC_IMAGE_002]]


Source: MS

Exhibit 2: Our CPO Forecast Was Short of Bullish Expectations, but Still Points to Meaningful Growth Opportunity

[[KC_IMAGE_003]]


Source: Yole, MS estimates

What are the challenges? Does NPO solve them? We have been writing about CPO for years, with the cost / fragility of the solutions tending to be the gating item (see many of the deep dives below). The main crux of the debate being whether you can replicate a high confidence supply chain around optics equal to that of transceivers today for scale-out and copper for scale-up. According to Tiffany Yeh, with her coverage of key CPO enablers WinWay and FOCI, key bottlenecks to CPO production scaling are SolC yield (50-60%) and downstream assembly yield (20-50%). By keeping the packaging separate, in NPO you have less problems with production, assembly, and a customer can more easily fix if optics are not working. While not trivial to put the optics on the board, it is a step function easier than CPO. Additionally, the optical engine can be purchased separately from the GPU/XPU, which can allow for a more open ecosystem. We do see the market moving towards CPO/NPO, but 2028/2029 when we see bigger adoption.

Exhibit 3: Preliminary Expectations from 650 Group Put Larger Opportunity as Scale-Up

[[KC_IMAGE_004]]


[[KC_IMAGE_005]]


Source: 650 Group

CPO Notes / Deep Dives:

Coherent Corp: Takes from the Road: Demand Visibility High, Margin Levers Building (12 June 2026)

Thoughts on Investor Concerns Regarding CPO (10 June 2026)

AI Supply Chain: CPO and ASIC Dynamic Update (3 March 2026)

OFC 2026 Wrap-Up: Bright Lights, Big City (19 March 2026)

Framing the CPO opportunity for Soitec and Besi (3 March 2026)

Telecom & Networking Equipment: Into the Spotlight: Optical Market Opportunities (23 Feb 2026)

New Page for Networking Market; Initiate FOCI at OW (14 January 2025)

## Analysis

## Estimating Optical Content Increases

According to Nigel Van Putten, on his coverage of Soitec and Besi, the number of optical engines per GPU rises from 2 to 4 today to 17-18 in NVL576 and potentially >35 in a fully optical configuration. Today's pre-CPO setup uses 2-4 pluggable transceivers (two for the leaf, two for spine with oversubscription potentially reducing this number) per GPU, all in the scale-out network. NVL576 introduces co-packaged optics (CPO) for inter-rack scale-up traffic, lifting optical engine attach rate to \~17 per GPU, on our estimates (LITE has noted more like \~18 – content per OE for LITE is \~\$150-200). Eventually, for a fully optical variant, where the connection between GPU and the networking switch also moves to photonics, roughly doubles that to \~35. Looking ahead to Feynman architectures and Keyber rack architectures, OEs per-GPU could remain at that level if SerDes speeds move to 400G, but could double again if SerDes stays at 200G.

Exhibit 4: Market Missing That Regardless of Timing, Optical Content Increasing

[[KC_IMAGE_006]]


Source: MS

Exhibit 5: Assumptions and Calculations of Optical Engines (OEs) per Rack Architecture


Source: MS estimates

Exhibit 6: 6-7mm Optical Engines of Demand From 59K Switches in Model

[[KC_IMAGE_007]]


Source: Yole, MS (e) estimates

## Challenges Today

CPO can help surpass current transmission distance limits, but maintenance might be a challenge: In traditional architectures, optical modules (like transceivers) are typically separate from switch chips; the two components are connected via electrical interfaces. In CPO units, however, optical modules and switch/XPU chips are packaged together, enabling greater integration and direct communication over short-distance, high-speed optical connections. In our view, such packaging could also help consolidate more functions within the same area – but CPO is also facing several challenges. These include lower yields arising from technical complexity and being relatively difficult to replace for maintenance purposes.

Optical alignment and module-level test flow are identified as the current CPO testing bottlenecks: Because CPO uses single-mode fiber with a 9 m core, small tolerance errors can cause major optical loss; the FAU tolerance stack-up can reach 3.8 m, making sub-micron alignment essential. As fiber counts rise to 64 or 128, repeated alignment and FAU connection steps slow testing significantly. Therefore, test speed, alignment accuracy, and mechanism design remain key bottlenecks for CPO production.

Exhibit 7: CPO Challenges

[[KC_IMAGE_008]]


Source: WinWay.

Exhibit 8: NPO Is Just a Path Towards Eventual CPO or Interposers

[[KC_IMAGE_009]]


Source: University of Toronto / Alphawave Semi

## Challenges / Opportunity of CPO

Move to optics from copper in scale-up is an occasion to introduce CPO (not on-chip yet, but eventually on-chip). There are still a lot of technical challenges to be figured out with CPO. 1) CPO puts the optics on board, which are higher failure than the electronics, increasing the cost of failure and preventing "hot-swapping". 2) Second, high manufacturing costs – CPO carries \~8-10x higher ASPs than traditional pluggable solutions. 3) A lack of ecosystem maturity and standardization, as CPO concentrated with AVGO and NVDA vs a broad ecosystem of transceiver vendors, concentrating economics of the ecosystem even further. 4) CPO's technical complexity currently results in low yields. However, in order to accommodate the I/O and bandwidth needs, CPO will be needed (moving away from just on-board optics to on-chip optics).

Eventually, on-chip co-packaged optics help solve the I/O problem. The core idea of CPO is to integrate optical engines directly into the package of a switch chip or other processing chips, thereby enhancing data transmission speeds, shortening the transmission distance, reducing power consumption, and minimizing latency. CPO brings together a wide range of expertise in fiber optics, digital signal processing (DSP), application-specific integrated circuit (ASIC) switches, and packaging & test to provide disruptive system value for the data center and cloud infrastructure. While there are multiple forms of CPO, including NPO, for the purposes of scale-up, bandwidth needs are advanced, creating an I/O problem, that Optical I/O or 2.5D / 3D CPO is the direction this market would be headed.

## Advantages

Lowering power consumption. Leveraging CPO architecture could help lower power consumption, as the traditional designs of transceivers require electrical signals to travel long distances over copper interconnects, leading to high power consumption and signal loss – whereas CPO significantly reduces power consumption by minimizing electrical signal transmission distances, which would further help enhance performance. Shorter electrical interconnect paths and direct optical communication lead to faster data transmission with reduced latency and fewer bandwidth constraints.

## Challenges

Low yields given challenges in packaging / overall cost of solution high. CPO's technical complexity currently results in low yields, as integrating optical modules with chips involves addressing challenges such as thermal management, signal integrity, and packaging compatibility. CPO carries \~8-10x higher ASPs than traditional pluggable solutions.

Lack of ecosystem. CPO requires collaboration and integration across the optical, semiconductor, and system design supply chains, which is unprecedented, whereas, in pluggables, standards are clearly set as this has been a very mature product in the market. Additionally, with CPO solutions being offered up primarily by Nvidia and Broadcom (both covered by Joe Moore), this would concentrate the profits of networking further into two of its largest vendors.

Challenging to troubleshoot. CPO solutions are relatively hard to maintain and replace, whereas hot-swapping is often an option for traditional transceivers. CPO switches require that power be turned off to conduct troubleshooting, which might lead to higher maintenance fees for customers and requires the network to be offline for longer, a significant challenge.

## Valuation Methodology and Risks

## Coherent Corp (COHR.N)

\~28-30x Base FY28e EPS (\~\$11.50). Multiple trades at premium to historical trading range given AI exposure, trading more in-line with AI comps.

## Risks to Upside

- Interest expense worked down given exit businesses or accelerated delevering
■ Pricing increases help gross margins
■ 1.6T AI opportunity ramps faster than expected, benefitting margins
■ Recovery in non-datacomm portions of business

## Risks to Downside

■ Macro headwinds or pricing increases difficult to achieve given tariffs
■ SiC market competitive
■ AI build out pause, catalyzed by DeepSeek
■ Competitive pressures in datacomm

## Corning Inc (GLW.N)

Our base case valuation reflects \~35x on FY28 Base Case earnings power of \~\$5.1. Our multiple represents a premium to GLW's traditional trading range over the last 10 years given AI megatrend.

## Risks to Upside

■ Acceleration in AI capex data points continue
■ Margins improve on fiber business as enter more into data center opportunity
■ CPO adoption greater than expected
■ Solar overhang on wafers quickly dissipates

## Risks to Downside

■ Delay in fiber deployment / AI plans
■ Alternatives to CPO found in scale-up
■ Macro disruption challenges pricing / margins, cash flow generation
■ Pricing discipline dissipates in display

## Lumentum Holdings Inc (LITE.O)

30x CY28 P/E of \~\$30. \~30x is a premium to historical trading range given AI growth outlook

## Risks to Upside

■ Datacom ramps and revenue mix more attractive vs. expectations
■ OCS ramps quickly, bringing additional revenue / profitability source
■ AI demand remains strong, causing EML business to outperform and drive profitability

## Risks to Downside

■ EML pricing falls given oversupply on reduced AI demand
■ CW takes share from EML
■ Cloud Light hurts ability to improve margins
■ Industrial demand falls on macro
