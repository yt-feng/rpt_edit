# Tech Hardware - Asia Pacific
# The essence of FAU: alignment and
## FAU: lots of new entrants, but few likely winners

FAU acts as a highway connecting fiber to the optical engine for data transmission, and is essential to pluggable transceiver/NPO/CPO. Currently, FAUs are mostly supplied by legacy Asia supply chains, and FAU for CPO is 100% supplied by a Chinese vendor. We see more new entrants aiming to ramp up CPO/FAU-related components – e.g. fiber array, micro lens, prism, etc. However, in our view, not many of them could succeed due to high entry barriers, and we see Largan's progress as faster than other new entrants as it has moved on to certification after sampling/testing for two quarters. We highlight two key bottlenecks: (1) micron-level alignment, i.e. controlling the pitch tolerance at ≤ ±0.5μm or even lower to ensure low-loss transmission; and (2) automatic alignment and testing to deliver consistent tolerance while lift efficiency. We note this know-how will take years of accumulated experience in precision optic manufacturing, mass production, as well as strong in-house automation capability.

## CPO to take off in '28-29; FAU at 5-10% BOM/ \$8bn TAM

Based on our checks, Nvidia's CPO switch volume may remain relatively low near-term, and a meaningful volume could happen in 2028-29, on rising penetration at scale-up. BofA tech team expects Nvidia CPO switch shipments to reach 14k/52k/190k units in 2026/27/28E. Among key components, we expect FAU to contribute 5-10% of the BOM, with the ASP ranging from US\$80-200. The TAM for FAU in Nvidia CPO switches could hit US\$8bn by 2030E. Amid multiple new optical solutions, we believe pluggable will remain a mainstream in scale-out into 2028-30. Within scale-up, the penetration of NPO and CPO depends on key CSPs' preference as well as CPO's overall yield and cost.

## GlassBridge: in early stage, not a replacement for FAU

Amid market's concern about potential threat from Corning's GlassBridge solution (to replace FAU), we argue that GlassBridge is still at an early stage, and is unlikely to be adopted in current and next-generation CPO design. Although GlassBridge could indeed improve the assembly yield, several bottlenecks need to be addressed, including misalignment with PIC due to the waveguide's uneven surface, rising manufacturing difficulty when channel numbers rise to $70+$ , etc. Also, under GlassBridge solution, a fiber array is still needed but likely with a lower precision-alignment requirement.

## Upgrade Largan to Buy, Neutral on Sunny Optical

We see the datacom supply chain as a more closed ecosystem vs consumer electronics, given much higher requirements. Besides capability, customer engagement is another key. We upgrade Largan to Buy from Neutral on faster progress at CPO (see Largan report). We reiterate Neutral on Sunny Optical given the lack of concrete projects.

## 14 July 2026

Equity

Katherine Zhu >>
BofA (Hong Kong)

Robert Cheng >>
BofA (Taiwan)

Doris Kao >>
BofA (Taiwan)

For acronyms, please refer to Exhibit 13

## FAU in CPO: \$8bn TAM by '30 on volume take-off from '28

Based on our supply chain check, Nvidia's CPO switch shipment may remain relatively low near-term, and a meaningful volume likely takes off in 2028-29 following rising penetration at scale-up. BofA tech team expects volume to reach 14k/52k/190k units in 2026/27/28E. Among key components, optical engine (OE) acts as the core to convert electric and light signals, while FAU acts as a highway connecting optical fiber and optical engine for data transmission. Outside of CPO switch, external laser source (ELS) is responsible for projecting laser that helps drive light signal through optical fiber, while MPO/MMC are connectors that connect optical fibers housed in the shuffle box to external ports. Looking at the BOM of a CPO switch, optical engine, ELS, and FAU are likely contribute $40 - 55\%$ , $10 - 15\%$ and $5 - 10\%$ of the total BOM, respectively.

Specifically for FAU, we believe its TAM in Nvidia CPO switch could reach US\$8bn by 2030E, based on an assumption of 1.4mn units of CPO switch and 115 units of 1.6T equivalent OEs per switch. Our check suggests FAU's ASP ranges from US\$80-200, depending on current specs. General FAU consists of fiber array (V-groove and optical fiber), lid, substrate and casing, etc, while some high-end FAU also integrate optical components like micro lens, prism and MT ferrules. For example, Spectrum 6810 adopts 36 channels of dFAU, and dFAU pricing could be in the range of US\$150-200. With volume gradually rising into 2030, the ASP could fall to US\$100. However, as specs migrate to 70-100 channels and potential multi-layer design, FAU could witness content value upside.

Exhibit 1: We expect Nvidia CPO switch shipment to reach 14k/52k/190k units in 2026/27/28E
Nvidia CPO switch shipment, 2026-30E

[[KC_IMAGE_001]]

Source: BofA Global Research estimates

Exhibit 3: We estimate FAU value per switch could reach US\$6-7k Nvidia CPO switch BOM analysis


Source: BofA Global Research estimates

Exhibit 2: Spectrum 6810 features 36 FAUs (include 4 redundancy)
Nvidia CPO switch component summary


Source: Company data, BofA Global Research

Exhibit 4: FAU roughly contributes $5 - 10\%$ BOM of a Nvidia CPO switch Nvidia Quantum and Spectrum CPO switch BOM analysis

[[KC_IMAGE_002]]

Source: BofA Global Research estimates

Exhibit 5: We expect FAU's TAM for CPO switch to reach US\$8bn by 2030E
FAU (for CPO) TAM analysis, 2026-30E


[[KC_IMAGE_003]]

Source: BofA Global Research estimates
Exhibit 6: We see dFAU ASP at around USD180 in recent 1-2 years
dFAU ASP trend (36-channel, 3.2T equivalent), 2026-30E


[[KC_IMAGE_004]]

Source: BofA Global Research estimates

Exhibit 7: FA likely to contribute 50% of the BOM, followed by micro lens at \~30%
BOM analysis of FAU (with micro lens, prism etc)

[[KC_IMAGE_005]]

Source: BofA Global Research estimates

Exhibit 8: Key FAU suppliers are mostly located in Asia (China, Japan, Taiwan)
Key suppliers in CPO supply chain


Source: BofA Global Research

## Alignment and automation lift entry barrier

FAU acts as a highway connecting optical fiber to the optical engine for data transmission, and is essential to pluggable transceiver/NPO/CPO. Currently, FAUs are mostly supplied by legacy Asia supply chains, while FAU for CPO is 100% supplied by Chinese vendors. We highlight two key bottlenecks faced by the supply chain: (1) micron-level alignment, i.e. controlling the pitch error tolerance at $\leq\pm0.5\mu m$ (or even $\leq\pm0.3\mu m$ ) to ensure light signal efficiency; and (2) automatic alignment to deliver consistent accuracy while lifting efficiency.

## Alignment: solving the pitch tolerance

Fiber array used in FAU acts as a multi-lane highway for light, allowing multiple data channels to be connected simultaneously with the optical engine for conversion of electronic and light signals. Under a fiber array, multiple optical fibers are densely seated on a V-groove (features parallel and microscopic V-shaped channels). The process requires highly precise alignment to achieve low-loss transfer. To compare, an optical

transceiver usually has a pitch tolerance (i.e. alignment accuracy) of $\pm0.5\mu m$ to $\pm1.0\mu m$ . NPO's pitch tolerance is likely at $\leq\pm0.5\mu m$ , while CPO's pitch tolerance could be $\leq\pm0.3\mu m$ . As V-groove and fiber also have their own geometric tolerance, alignment error could accumulate linearly when channel numbers rise. V-groove's etching depth and angle variation could introduce misalignment from channel to channel. Even if a V-groove is perfectly etched, optical fiber could also lead to alignment difficulties. A single-mode fiber generally has a diameter of 80-125 $\mu m$ (core at 6-10 $\mu m$ ); any diameter variation of a fiber could cause it to sit higher or lower on a V-groove, leading to alignment mismatch. Additionally, for dFAU, maintaining positioning tolerance after multiple detach/plug processes is also key.

This level of precision alignment usually requires years of accumulation, deep know-how in optic coupling and mass production experiences. Although smartphone optic suppliers could leverage their active alignment (AA) know-how used in lens/module, the level of precision still has a big gap (for example, telephoto camera's AA tolerance is $\leq \pm 5\mu \mathrm{m}$ ).

## Automation: crucial when channel numbers continue rising

As optical fiber channel numbers are expected to increase to 60-100 from the current 20-36 channels while CPO volume is waiting for take-off in 2028-29, fiber array alignment based on labor-intensive process looks increasingly difficult. Thus, automation becomes crucial. It could not only reduce labor intensity and lift efficiency, but more importantly help troubleshoot alignment issues and improve accuracy. As the industry has no standard automation/testing at current stage, suppliers able to ramp up automation faster or have in-house automation capability could have a better edge.

Exhibit 9: FAU assembles PM fibers on a V-groove to direct light, and leverages micro lens and prism to project light onto PIC
Illustration of FAU under grating coupler solution

[[KC_IMAGE_006]]


Exhibit 10: CPO has the lowest pitch error tolerance at ≤ ±0.3μm
FAU spec summary under different applications


Source: BofA Global Research
Source: FOCI

## GlassBridge not a threat near-term, also not a replacement

We note market's concern about Corning's GlassBridge, a wafer-based fiber-to-PIC technology, which could be an alternative solution to FAU. We argue that GlassBridge is still at an early stage and is unlikely to be adopted in current and next-generation CPO design. Although GlassBridge could indeed improve the assembly yield, several bottlenecks need to be addressed, including misalignment with PIC due to the waveguide's uneven surface (due to edge coupling), rising manufacturing difficulty when channel numbers rise to 70+, etc. Further, GlassBridge uses edge coupling technology – i.e. horizontal coupling, with light projected directly into the PIC horizontally. Compared with grating coupling (vertical coupling), edge coupling is not able to conduct wafer-scale testing, leading to potentially lower efficiency. The horizontal design also faces space limitations and demands an extreme alignment requirement.

Exhibit 11: GlassBridge is a wafer-based fiber-to-PlC technology platform
Corning's GlassBridge connector

[[KC_IMAGE_007]]


Exhibit 12: Edge coupling is more efficient in insertion loss, but faces limitation in terms of wafer-level testing and spatial constraint
Comparison of grating coupling and edge coupling


Source: BofA Global Research
Source: Corning

Exhibit 13: Summary of acronyms used in this report
Acronym


Source: BofA Global Research
Source: BofA Global Research

Exhibit 14: Stocks mentioned in this report
Stocks mentioned


## Investment Rationale

## Largan Precision

We have a Buy rating on Largan, eyeing on rising visibility on potential CPO project gain. We believe CPO will drive valuation a re-rating and a potential earning upside from 2028E. Besides, legacy business should stay resilient thanks to iPhone's multi-year spec upgrade cycle.

## Price objective basis & risk

## Largan Precision (LGANF)

Our PO of NT\$5,600 is based on 25x 2028E P/E. 25x is at Largan's historical peak P/E during last earnings upcycle. We believe CPO take-off from 2028 will drive another new multi-year earnings upcycle for Largan, justifying our valuation multiple.

Downside risks are: 1) weaker than expected end-demand, which leads to pressured topline and margin on lower utilization rate, 2) more intense competition from Greater China competitors including Sunny Optical, Genius and AAC, 3) slower than expected spec upgrade, and 4) slower than expected progress at CPO.

Upside risks are: 1) better than expected end demand and faster than expected spec upgrade, 2) higher than expected ASP and market on competitors' inferior execution, 3) eased competition from key peers, and 4) faster than expected progress at CPO.

## Sunny Optical (SNPTF)

We set our PO at HK\$69, on 17x 2026E P/E, we view 17x, around -0.5SD, is justified by potentially slower margin improvement amid uncertainties at smartphone shipment and spec into 2026, while reflect business diversification into datacom.

Downside risk: (1) demand at consumer electronics further deteriorate with continuous de-spec, (2) slower than expected share gain at iPhone, (3) slower-than-expected auto momentum and slower ADAS penetration, (4) intensified competition at both smartphone and auto. (5) Government subsidy is removed.

Upside risk: (1) better than expected demand/spec at consumer electronics, (2) faster than expected share gain at iPhone, (3) strong auto momentum and faster ADAS penetration, (4) eased competition at both smartphone and auto, and (5) faster than expected progress at datacom.
