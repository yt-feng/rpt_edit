# Honing the edge of advanced silicon test
## Beneficiary of structural AI/HPC testing growth and enabler of new technologies; initiate at Buy
## Initiate coverage at Buy with TP of TWD11,100, implying \~73% upside

We initiate coverage of Hon. Precision (Hon) with a Buy rating and a target price of TWD11,100, based on 40x average 2027-28F EPS of TWD277. Our target P/E multiple is at the high end of Hon's historical trading band of 19-52x since its IPO, which we consider undemanding given a 58% net earnings CAGR through 2026-28F. The stock is currently trading at 29x 2027F EPS of TWD219, compared with semiconductor-backend equipment and test interface vendors (2027E Bloomberg consensus average P/E 37x). Hon is an equipment manufacturer focusing on IC test handlers and active thermal control systems (ATC) used in the final test (FT) or system level test (SLT), and AI/HPC/ASIC make up c.80% of its tool orders. We expect Hon to capitalize on an extended testing time for AI/HPC chips due to increased chip design complexity and larger package footprints, and increasing testing capex by AI OSATs and semiconductor manufacturing reshoring in the US indicate potential upside to Hon's ATC/handlers. We estimate Hon to record a revenue CAGR of 59% and model EPS at TWD134/TWD219/TWD336 for 2026-28F. A major downside risk to our view is CoWoS and backend testing capacity expansion slowdown.

## Clear ATC upgrades down the road could boost ASP; handler upgrades in sight with new technologies on the horizon

A clear visibility of ATC roadmap and well execution, in our view, put Hon in a more favorable position for AI/HPC clients looking to initiate new chip development. We believe Hon should enjoy an ASP uptrend from AI/HPC customers' migration to more powerful ATC in view of increasingly stringent thermal requirements, and GPU-on-GPU SolC stack for a leading AI GPU customer's 2028E platform could make such advancement more imperative. We also think OSATs may have to upgrade the handlers beyond 2027-28F for internal mechanics to support large packages (e.g., 10-11x reticle-size interposers, CoPoS, embedded multi-die interconnect bridge [EMIB]), and the emergence of co-packaged optics (CPO) test insertions and micro-channel lids (MCL) could also drive new purchases of dedicated handlers. In addition to AI/HPC, we observe growing testing contents in mobile application processors (APs) and CPUs as well thanks to advanced packaging or multi-die layouts, and believe Hon should be a key beneficiary of a strong FT handler foothold in these areas.


Source: Company data, NOM estimates

24 July 2026

Rating
Starts at
Buy

Target price
Starts at
TWD 11,100.00

Closing price 22 July 2026 TWD 6,405.00


## Relative performance chart


[[KC_IMAGE_001]]

Source: LSEG, NOM


Semiconductor


Vivian Yang - NITB

## Key data on Hon. Precision, Inc.

Income statement (TWDmn)


Source: Company data, NOM estimates

Cashflow statement (TWDmn)


Source: Company data, NOM estimates

## Company profile

Founded in 1999, Hon. Precision (Hon) is a dedicated semiconductor equipment manufacturer focusing on IC test handlers and active thermal control systems (ATC) for IC backend testing. Hon's client base spans across major IC design houses, outsourced semiconductor assembly and test vendors (OSATs), and integrated device manufacturers (IDMs) worldwide.

## Valuation Methodology

Our TP of TWD11,100 is derived from 40x average 2027-28F EPS, at the higher end of historical trading band (19-52x) since IPO. The benchmark of this stock is TAIEX.

## Risks that may impede the achievement of the target price

Downside risks to our call include: 1) CoWoS and backend testing capacity expansion slowdown; 2) slower-than-expected product refresh, platform performance upgrade, or ramp-up by the AI chip end customers; 3) fiercer-than-expected market competition in test handlers; and 4) weaker-than-expected end-market demand, particularly AI servers.

## ESG

Hon. Precision has built its sustainability framework around three pillars: environmental protection based on the TCFD framework to assess energy/greenhouse gas management and water source risks, a "happy workplace" for employees, and social participation. All of these are overseen by a dedicated sustainable development unit that coordinates ESG risk responses and reports regularly to the Board of Directors.

## FT and SLT are Hon's equipment addressable markets

The semiconductor backend processes are punctuated by a few test insertions that sort out defective silicon as early as possible, serving as a gate to ensure output quality – chip probe (CP), final test (FT), burn-in test (BIT), and system-level test (SLT), and the entire backend flows start with CP at the wafer level before the individual dies are cut out of the wafer and undergo subsequent assembly (Fig. 1). A detailed description of the IC backend testing process is elaborated in our Anchor Report, and here we only focus on FT and SLT, which are Hon's addressable segments.

Fig. 1: An illustration of semiconductor manufacturing and backend testing flows

[[KC_IMAGE_002]]

Source: CHPT, NOM

FT is a mandatory procedure, and depending on IC customers' configurations, there could be two or more FT steps during the manufacturing cycle (e.g., nVidia's [NVDA US, Not rated] AI GPUs require two FT steps, one before BIT and the other after BIT). FT is carried out after IC assembly (on substrates, lead frames, or wire bond) and chip packages are capable of accommodating larger input voltages or electric current than bare dies. FT measures electrical properties of chips given pre-programmed inputs to identify product functionality (“pass or fail” is the terminology) and sort functional products by grade (also known as “binning”), all within the shortest possible time frame (usually hundreds or thousands of seconds), as chip vendors may want to control test charges (measured by “hourly rates”) which are amortized expenses of costly testers.

There are three primary parameters that form a sequential filtering system in FT for logic circuits, and the focuses are on whether outputs are “correct”. By contrast, analog/mixed-signal IC testing places more emphasis on the “measurement accuracy” of select parameters (e.g. linearity and signal-to-noise ratio).

1. Direct current (DC) test: The DC test is the first phase in FT and consumes the least time amongst the three phases. It measures the steady-state electrical characteristics of a chip using direct current and ensures the physical silicon structure is intact. The DC test does not validate logic or speed, however. The primary metrics measured during this phase include: 1) Open/Short test which verifies all pins are properly connected to the internal circuitry (no “open”) and that no pins are accidentally welded together (no “short”); 2) Leakage current which ensures a pin does not “bleed” excessive current into the substrate when it is given a specific voltage level; 3) Power consumption which detects electric current drain inefficiency; and 4) Output voltage level which confirms the chip can drive signals out at the correct voltage thresholds required to communicate with other components.

2. Function test: The subsequent function test is to check whether logic operation works properly. During the function test, the tester floods the chip with pre-programmed binary inputs (i.e., test vectors) and records the outputs generated by the chip to compare the results against the expected mathematical truth table. Function tests are typically executed at a nominal, conservative clock speed to isolate pure logical errors from high-speed timing anomalies.

3. Alternating current (AC) test: The AC test introduces the critical dimension of “time”, evaluating how the chip performs under dynamic, high-frequency AC conditions and checking the output signals’ “waveform”, because a chip might have perfect structure and flawless logic responses at slow speeds. AC test pushes the silicon to its physical limits by measuring sub-nanosecond timing parameters to ensure signals propagate cleanly across the die without corruption. Major test items include propagation delay, setup and hold times, rise and fall times, and maximum frequency. The AC test is also the foundation of “binning”, sorting out the best-performing chips and lower-tiered ones.

On the other hand, SLT is an optional procedure, during which a chip is inserted into a system test board designated by a chip vendor to simulate how it works in the real-world scenario. The test board is a modified version of the actual commercial motherboard that eventually houses the silicon and is equipped with other components such as memory and peripherals. The SLT boots a full operating system like Linux or Android and runs heavy, asynchronous software workloads to replicate genuine user environments (Fig. 2). Throughout the process, SLT measures functional and behavioral metrics rather than raw structural data, including system stability, workload execution throughput, thermal throttling thresholds, and high-speed interface bit error rates (BER).

SLT has gained traction industry-wide because it exposes defect classes that the preceding stages structurally cannot (Fig. 3). DC test, Function test, and AC test are largely deterministic and exercise the device in isolation, at fixed patterns and controlled conditions. They are effective at catching hard, static failures but are poorly suited to intermittent, workload-dependent or interaction-level defects – issues only manifest when multiple IP blocks operate concurrently under realistic power, thermal, and timing stress, or under specific software-induced corner cases. As chip complexity has grown with heterogeneous integration, multi-core coherency, and higher-speed interfaces, these system-level “test escapes” could result in a larger share of field returns, which has steered SLT from a niche practice in automotive/mobile applications toward broader adoption across compute, AI accelerator, and networking chips, where the cost of a return merchandise authorization (RMA) far outweighs the cost of additional test screening.

Fig. 2: SLT acknowledges that software is part of the system, and recreates the end-use environment as closely as possible

[[KC_IMAGE_003]]

Source: Teradyne, NOM

Fig. 3: Traditional test coverage becomes more challenging, and SLT's strategic importance is emerging

[[KC_IMAGE_004]]

Source: Teradyne, NOM

The SLT phase is less expensive than FT given no usage of multi-million-dollar testers, but it is very time-consuming and could take minutes or even hours to execute per device. At high volumes, the throughput mismatch could become the binding constraint on SLT adoption, since running every unit through hours of system-level workloads is economically impractical for most product lines. As such, the industry leans toward parallel testing inside automated SLT handlers, and potentially the integration of adaptive testing backed by machine learning algorithm which selectively routes only silicons at risk to extended SLT screening while the bulk of the chips proceed through a shortened or standard flow (Fig. 4). This “smart SLT” approach preserves most of the defect-screening benefit while containing the test time and cost overhead, and is emerging as a key differentiator among OSATs and IDMs competing on both quality (defined by defective parts per million, or DPPM) and test cost per unit.

Fig. 4: Adaptive SLT could further reduce the overall cost (time) of test

[[KC_IMAGE_005]]

Source: AEM, NOM

## IC test trios: ATE, prober/handler, and test interface

The semiconductor testing is not carried out by one single tool but a tightly integrated system also known as “test cell”. The test cell consists of three major parts: automated test equipment (ATE), prober/handler, and application-specific test interfaces. In SLT, the ATE is replaced with a system test board on which test sockets are equipped, housed inside an SLT handler.

\- Automated test equipment (ATE): ATE, or simply “tester”, is the sophisticated core workstation of the test cell that feeds precise electrical stimulus signals (e.g. voltages, currents, or high-frequency waveforms) into the device under test (DUT) and monitors the output responses. The tester compares the chip’s real-time performance running on pre-programmed inputs against engineering design

specifications to identify defectives. In the ATE architecture, the mainframe houses the tester's power supply, central cooling unit and the system controllers, and the test head houses the test interfaces.

\- Prober/handler: The prober or the handler is the mechanical automation arm of the test cell that operates with the ATE to ensure a continuous, high-speed, and unmanned silicon test flow. The test head is flipped and pneumatically or hydraulically docked into the core mechanical nest of the prober/handler. The prober and the handler are used in different testing scenarios – the prober is present in CP and handles uncut wafers, using microscopic pins to physically contact with individual die before they are singulated, while the handler picks up chip packages (in FT or SLT) from trays, inserts them into the test sockets, and physically sorts them into different bins based on the tester's verdict.

\- Test interface: The test interface is the physical and electrical “bridge”, customized based on the silicon layout/package, to connect the generic tester to the DUT. A probe card paired with pogo pins (or MEMS pins for fine-pitch applications) is used in CP, while a load board with test sockets is adopted in FT.

Fig. 5: A test cell in chip probe

[[KC_IMAGE_006]]

Source: MJC, NOM

Fig. 6: A test cell in final test

[[KC_IMAGE_007]]

Source: SAE Technical Papers "Thermal Management and Control in Testing Packaged Integrated Circuit (IC) Devices", NOM

The IC test squad is not complete without “role players”

Beside the aforementioned trios, we note there are also tools supplementing temperature management to prevent undesired shifts in chip performance and physical properties under different thermal conditions, and specialized plug-in modules to expand or reconfigure the tester's scope.

\- Thermal chuck: During CP, the chuck is the flat, rigid metallic platform that holds the silicon wafer in place using vacuum suction. A thermal chuck is a chuck with built-in heating elements and internal cooling channels to uniformly control the temperature of the wafer under test when mimicking different thermal conditions in operations. A thermal chuck must demonstrate extreme planarity (i.e., very meagre warpage) at extreme temperature swings to avoid poor electrical contacts or wafer crack by probe needles.

\- Active thermal control system (ATC): ATC is a dynamic temperature management system integrated into the handler. When a tester boots up workloads, the DUT could undergo a spike in internal power density and instantaneously heat up. ATC detects the thermal conditions of the chip under test and instantly adjusts its cooling/heating action to counteract the chip's internal power fluctuations.

\- Instruments: The tester is essentially a modular chassis populated by a cluster of instruments that define its initial testing scope. However, if a silicon requires test coverage beyond this built-in set, specialized instruments can be added to the tester to extend its capabilities. These modular instruments are notably critical for high-

performance domains like analog/mixed-signal and high-speed digital, and we observe optical instruments are introduced in CPO test insertions to assist with photonic test items (e.g., optical insertion loss, spectrum/wavelength and polarization effects).

Fig. 7: The thermal chuck is integrated into the wafer prober
Thermal chuck (left; by ATT Systems) and wafer prober (right; by FormFactor)

[[KC_IMAGE_008]]


Fig. 8: The ATC is integrated into the handler

[[KC_IMAGE_009]]

Source: Company data, NOM

Fig. 9: The instrument helps expand dedicated test coverage

[[KC_IMAGE_010]]

Source: Keysight, NOM
Source: FormFactor, NOM

Fig. 10: Semiconductor test equipment and interface maker overview


Source: Company data, NOM

## Hon specializes in handlers and ATC, and provides tailored test kits

Hon has established itself as a powerhouse in the semiconductor backend testing arena, focusing specifically on AI/HPC and ASIC sectors. The company specializes in FT/SLT handlers (more focus on FT; primarily pick-and-place handlers, which use suction to transfer the DUT and press it into the test sockets) and ATC. Hon offers both dual-temp (high temperature [up to 170°C] and ambient temperature [around 25°C]) and tri-temp (high temperature, ambient temperature, and low temperature [down to -70°C]) ATC capabilities, based on three types of cooling system:

\- Liquid-cooling (ATC3 series) supports a cooling capacity of up to 3,000W and a temperature control range of $25^{\circ}\mathrm{C} - 150^{\circ}\mathrm{C}$ . AI GPUs and most AI ASICs adopt ATC3.

\- Refrigerant-cooling (ATC5 series) supports a cooling capacity of 50-4,000W and a temperature control range of -70°C-175°C. Select AI ASIC customers and chips with application scenarios in radical environments (e.g. automobile and space) adopt ATC5.

\- Air-cooling (ATC6 series) supports a cooling capacity of 30-50W and a temperature control range of 25°C-130°C. ATC6 could be used in low-power applications like Android APs.

Fig. 11: Hon's ATC portfolio

[[KC_IMAGE_011]]

Source: Company data, NOM

Fig. 12: Hon's ATC solutions and application scenarios

[[KC_IMAGE_012]]

Source: Company data, NOM

In addition to the standalone machinery, Hon has a highly integrated test support ecosystem by selling socket layout kits (SLKs) and cold plates that are customized based on chip microstructure to guarantee an optimized contact force (Fig. 13). Hon typically derives c.20% of revenue from jigs and modules, which we believe the bulk is cold plates. SLK is a mechanical conversion interface to help a handler adapt to test module changeover on a test head for precise electrical connections. A cold plate is installed onto the SLK to help with thermal transfer during the test stage.

The majority of Hon's cold plates have a channel pitch of 500um. While AI/HPC chip thermal design power (TDP) continues to skyrocket, thermal dissipation during the test stage becomes an issue, and the convective heat transfer coefficient is the predominant factor of liquid cooling performance; it is also inversely correlated to channel pitch. Hon therefore introduced a microchannel cold plate (MCCP) in 2Q26, which can shrink the channel geometry to 150-200um. We think Hon could enjoy a $15\%$ higher ASP from MCCP vs. mainstream cold plates.

Fig. 13: Hon's product offerings include IC test handler, ATC, SLK, and cold plates

[[KC_IMAGE_013]]

Source: Company data, NOM

Fig. 14: Hon's revenue mix

[[KC_IMAGE_014]]

Source: Company data, NOM estimates

# Rising design complexity and expanded footprints of AI/HPC chips spur structural testing growth

## AI/HPC applications continue to lengthen testing time

We believe rising chip design complexity and expanded package footprints are the two most critical catalysts driving AI/HPC chips to foster structural growth in the semiconductor testing process, an often overlooked element in the manufacturing value chain because of its relatively low proportion in cost structure. The semiconductor industry is currently undergoing a paradigm shift in layout/architecture by embracing chiplet-based design philosophy, 2.5D advanced packaging to stitch multiple-reticle-sized interposers and 3D IC stacking to increase performance per area (measured by transistor density), as conventional geometric scaling slows, costs for chip design and yielding large die continue to rise at more advanced logic nodes (Fig. 15, Fig. 16, and Fig. 17), and any single chip inevitably faces the physical limit of reticle size (26x33mm exposure field size, or 858mm²). In a seminar at SEMICON Taiwan 2025, TSMC (2330 TT, Buy) estimated compute performance per reticle improvement by 80x from N28 to A16, and the incorporation of advanced packaging could enlarge the gain to \~320x at >9.5x-reticle CoWoS (Fig. 18).

Fig. 15: The cost per yielded die vs node migration The cost per yielded die continues to increase when entering into more advanced nodes

[[KC_IMAGE_015]]


Fig. 16: Cost reduction by using chiplets vs SoC solution

[[KC_IMAGE_016]]

Source: TSMC, NOM
Source: NOM

Fig. 17: Skyrocketing chip design cost moving to more advanced nodes

[[KC_IMAGE_017]]

Source: IBS, NOM

Fig. 18: Advanced packaging is an approach to bring the subsystem performance further up

[[KC_IMAGE_018]]

Source: TSMC, NOM

fundamentally altered the economics and mechanics of semiconductor manufacturing. Die-to-die interconnect in chiplets or 2.5D/3D packaging is a complex jigsaw puzzle replacing traditional seamless on-die communication, because engineers must ensure robust signal and power integrity, and thermal management and mechanical stress control also become crucial in such layouts. Consequently, semiconductor testing is no longer just a routine quality-control process at the end of the production flows; it has become an indispensable, high-stakes discipline that directly dictates commercial success.

Device complexity increase will require a longer testing time by nature, and if we take nVidia AI GPUs as an example and index the FT time of Hopper to 1, we estimate 4x for Blackwell and \~7x for Rubin. The prolonged testing time and higher hourly rates should add to testing content in the cost structure, and we estimate the testing content (defined as the sum of FT, BIT and SLT) in nVidia Rubin could rise to 3.3% of the cost vs. 2.5% for Blackwell and 1.9% for Hopper, leveraging our supply chain analysis. A lengthening testing time presents an outright tailwind to semiconductor testing equipment makers, in our view, given the need by OSATs to keep up with throughputs.

Fig. 19: Increasing testing content in the logic manufacturing cost of nVidia AI GPUs

[[KC_IMAGE_019]]

Source: Company data, NOM estimates

## AI/HPC chips are larger – handler redesign becomes imperative

We highlight that FT handlers could eventually undergo mechanical redesign and OSATs have to upgrade the tools if chip packages expand to a certain bar. Thus far, AI/HPC is the primary driver of package footprints. With logic dies already approaching a physical limit closer to the reticle size, nVidia and other AI accelerator makers understand incremental performance gains must come at the sub-system level rather than the chip level, and consequently are targeting to stack more logic dies and more HBM cubes onto interposers to construct a more powerful computing chip system. nVidia has moved from Ampere/Hopper (both 2x reticle-size interposer), to Blackwell in 2024 which houses two reticle-size compute complexes and eight HBM cubes on a 3.3x reticle-size interposer, and soon to Rubin in 2026E which houses two reticle-size compute complexes, two I/O dies, and eight HBM cubes on a 5x reticle-size interposer.

We believe the horizontal expansion of AI chip footprint is unlikely to halt as TSMC continues to unfold its CoWoS roadmap to introduce larger interposers (and therefore larger IC substrates underneath). According to TSMC, it is bringing 5.5x reticle size CoWoS into production in 2026 with a >98% yield. Previously, TSMC suggested its 9.5x CoWoS-L with SolC and 12 HBM stacks would enter production in 2027E (Fig. 20; Tech Symposium 2025), and during the symposium this year, the company extended the roadmap to 14x reticle size CoWoS (20 HBM stacks) production by 2028 and aims for >14x reticle size CoWoS (24 HBM stacks) in production by 2029 (Fig. 21).

Fig. 20: TSMC's CoWoS roadmap laid out in 2025 Technology Symposium

[[KC_IMAGE_020]]

Source: TSMC, NOM

Fig. 21: TSMC updates its CoWoS roadmap

[[KC_IMAGE_021]]

Source: TSMC, NOM

We note “the bar” is correlated to “how many chip packages that a matrix tray can accommodate” during the FT stage. A matrix tray is a plastic carrier that holds IC packages in a rigid grid of rows and columns, and the robotic arm of a handler will move the vacuum suction nozzle over the input matrix tray, suctions up untested chips (DUT), and places DUT into the test socket. The dimension of the tray generally conforms to the standard proposed by the Joint Electron Device Engineering Council Solid State Technology Association (JEDEC in short). The current standard tray is specified at 135.9x322.6mm, but if a chip package measures 120x125mm, one standard tray can carry only two pieces of DUT. The JEDEC acknowledges the industry trend of moving toward larger package footprints (notably in recent years, propelled by AI/HPC), and has added two new types of tray (also known as “mega tray”) in recent issues: 258x537.6mm and 380x387.6mm.

Hon has progressed the development of large-package handlers based on the new JEDEC standards, and the current planning is to begin shipments of tools capable of handling >120x150mm packages in 2H26E, and a handler solution for 250x250mm package in 2H27E, to position itself early for the next round of handler upgrades. Hon also targets to add more automation functionalities for better integration with unmanned factories (e.g., overhead hoist transfer [OHT] and autonomous mobile robot [AMR]) to boost throughputs. Our ‘napkin math’ indicates that a 120x150mm package could house an interposer sizing up to 10-11x reticle, which ties with TSMC’s CoWoS roadmap in 2027-28, whereas our supply chain checks have not yet picked up such a large AI chip in the pipeline.

Fig. 22: IC matrix tray
Fig. 23: JEDEC adds two new types of tray to address larger package size
The left one is the current standard tray (135.9x322.6mm), and the one in the middle measures to 258x537.6mm and the right one measures to 380x387.6mm

[[KC_IMAGE_022]]

Source: Sunrise, NOM


[[KC_IMAGE_023]]

Source: JEDEC, NOM

## AI/HPC chips are also hotter – more powerful ATC is necessary

We believe Hon will capitalize on the ASP uptrend from AI/HPC customers' migration to more powerful ATC (greater cooling capacity), since the sub-system performance gain from more dies in a package comes at the cost of more stringent thermal requirements.

Using nVidia AI GPUs as an example, the maximum TDP of Blackwell Ultra (B300) is

1,400W, which can be supported by Hon's ATC3.5 (cooling capacity of up to 2,000W). However, we think the TDP of Rubin (R100) may start from 1,800W, leaving little margin for ATC3.5 and likely initiating an upgrade to ATC3.6 (up to 3,000W). Admittedly, comparing TDP to ATC maximum cooling capacity is sometimes more biased than “power density” (also better known as “heat flux” in thermal physics), because TDP only tells us “how much heat is generated” and power density/heat flux provides us “how concentrated the hotspot is” and “how fast the heat transfer is”.

We foresee further elevating thermal challenges moving to Feynman (F100), slated to come onstream in 2028E. nVidia at GTC unveiled its plan to adopt 3D stacking starting from the Feynman platform (report). Vertical chip stacking (SolC platform at TSMC) theoretically could augment transistor counts per package, an outright indicator of computing power, without extra footprints (vs CoWoS/2.5D packaging that expands horizontally to accommodate more chips). AMD (AMD US, Not rated) believes 3.5D chip modules (i.e., 2.5D packaging + 3D hybrid bond) could enable shorter data paths and improved interconnect energy efficiency, and estimates \~80% more active silicon in a given module footprint than sheer 2.5D packaging (Fig. 24). We think the 3D logic stacking approach may also lie in other custom AI chip future roadmap (Fig. 25).

Currently, AMD leads the adoption of SolC at TSMC (starting from MI300-series), and in the latest MI450, we believe AMD stacks four top dies (four XCD) on two reticle-sized active interposers (I/O dies), in which each top die scales to about 1/3 reticle size (Fig. 26). nVidia will be more aggressive in chip specs by stacking a reticle-sized GPU die on top of another for the Feynman platform, the first-ever GPU-on-GPU SolC stacking (report), which would lead to higher computational power even with limited growth in interposer reticle stitching size (c.6x reticle, see footprint in Fig. 27; up from c.5x in Rubin). Such an industry practice theoretically exacerbates thermal dissipation challenges, and we expect it could trigger a migration to more powerful ATC3.7. According to Hon, it has ATC with a maximum cooling capacity of up to 7,000-8,000W ready, and is working on engineering en route to >10kW (Fig. 28).

Fig. 24: 3.5D packaging offers a more dense chiplet module

[[KC_IMAGE_024]]

Source: AMD, NOM

Fig. 25: Broadcom introduced face-to-face 3D hybrid bond on its 3.5D platform

[[KC_IMAGE_025]]

Source: Broadcom, NOM

Fig. 26: Floorplan of AMD MI455 and cross section

[[KC_IMAGE_026]]

Source: Company data, NOM

Fig. 27: The floor plan and cross-section chart of nVidia's Feynman GPU

[[KC_IMAGE_027]]

Source: Company data, NOM estimates

Fig. 28: Hon's ATC roadmap to address greater TDP by AI/HPC chips

[[KC_IMAGE_028]]

Source: Company data, NOM

## Intel's EMIB might open a new window for large AI chip test demand

We believe some AI ASIC customers might have started evaluating Intel's (INTC US, Not rated) EMIB-T (embedded multi-die interconnect bridge with TSV) as a logic+HBM integration alternative because of concerns about insufficient capacity support at TSMC. According to Intel, EMIB-T targets HBM4/4E and logic chiplet interconnectivity with the lowest possible cost, and the company's roadmap is to scale to the integration of >8x reticle size total top silicon area on a \~120x120mm substrate by 2026E and >12x reticle size top silicon area on a >120x180mm substrate by 2028E (Fig. 29). If successful, Intel's EMIB-T might open a new demand window for large AI chip testing. We reckon that Hon should have FT handlers under engineering verification at Intel Foundry.

We think Google's (GOOGL US, Not rated) potential reliance on Intel's EMIB-T for the next-generation TPU v9 (partnering with MediaTek [2454 TT, Buy]) could be a critical litmus test for Intel's advanced packaging capabilities. Based on our supply chain analysis, this signpost project will feature a substrate body size within 120x120mm (see the floor plan in our report), not yet necessitating the transition to mega tray configuration.

A (much) less important side project at Intel EMIB might be Intel's laptop SoCs that will incorporate nVidia's RTX dies using NVLink, as a result of their partnership (report). As Hon has been an important FT handler supplier for computing applications for years, we believe Hon might have potential to participate in this client CPU project, likely at a higher price than those shipped to Taiwan-based OSATs.

Fig. 29: EMIB roadmap
Source: Intel, NOM

## Continued CoWoS capacity growth at TSMC, fueled by AI/HPC

We think TSMC's CoWoS capacity growth is one proxy for Hon's handler sales volume trend as both are primarily fueled by AI/HPC demand, and we estimate \~100% of CoWoS capacity each year is allocated to AI/HPC applications (vs. c.80% of Hon's handler tool orders come from AI/HPC). But we note that there is not necessarily a mathematical relationship between CoWoS capacity builds and handler purchases given varying output per interposer wafer for different AI accelerators and the throughput factor in handlers.

To date, TSMC's supply is apparently still constrained across the front-end and the back-end given the demand strength from AI, and the company has expressed its commitment to expanding its capacity in due course, citing that it “works very hard to meet all the demand” and “doesn’t leave any business on the table” (see remarks from 4Q25 and 1Q26 results). We observe TSMC has turned more aggressive on CoWoS capacity planning (or more precisely, “CoW” capacity) in recent months in response to surging AI chip demand, and lifted the capex guidance again in the July earnings call (report), which should indirectly underscore the growth trajectory of Hon’s handler business.

In our most recent Asia AI Semi & Server Anchor Report, our supply chain checks suggest TSMC will likely expand its CoWoS capacity to 1,100kpcs in 2026F (or c.130kwpm by the end of 2026F) and bring this up to 2,000kpcs in 2027F. Although TSMC has turned more aggressive in its CoWoS plan, our contrarian view is that “WoS” (not controlled by TSMC) and many small components (e.g. IC substrates) would very likely become a bigger bottleneck than “CoW” (controlled by TSMC) in 2027F. We only assume 1,800kpcs of CoWoS output in 2027F (despite our assumption of a TSMC target of 2,000kpcs).

While we have no clear bottom-up estimates about how TSMC is going to expand its CoWoS capacity beyond 2027F, we had tried to triangulate a possible trajectory in our Asia AI Semi & Sever Anchor Report, based on TSMC's AI semi growth guidance and our assumptions of manufacturing content added. TSMC's guidance might hint an annual CowoS capacity of 2,500-3,500kpcs by 2029F, vs 680kpcs in 2025, and this would suggest a 40-50% capacity CAGR over 2025-29F compared to a >80% CAGR planned for 2022-27E. If the expansion track prevails, we expect Hon's ATC/handler sales to continue to benefit from associated backend testing capex investments by TSMC and its ecosystem partners beyond 2027F.

Fig. 30: TSMC turning more aggressive on CoW capacity expansion
Source: Company data, NOM estimates

Fig. 31: But the output will be constrained by "WoS"
Source: Company data, NOM estimates

Fig. 32: TSMC's CoWoS output breakdown
Source: Company data, NOM estimates

Fig. 33: TSMC's CoWoS output allocation
Source: Company data, NOM estimates

## CoPoS might unlock another wave of handler upgrades

We believe the high-volume production of “chip-on-panel-on-substrate (CoPoS)” or fan-out panel-level packaging (FOPLP) to enable larger interposer-based integration (Fig. 34; and consequently greater substrate/package size) might drive another round of IC test handler upgrades for Hon, given possible adjustments to the underlying mechanical structure. We have flagged in our Asia AI Semi & Server Anchor Report that CoPoS is one of TSMC’s countering measures to stay ahead of its competition in advanced packaging by offering more reasonable economics for larger-size 2.5D packaging.

TSMC showcased its production roadmap to 14x reticle size CoWoS by 2028E and >14x reticle size CoWoS in 2029E during the Technology Symposium in April 2026 (report). Our back-of-the-envelope calculation shows only one or two interposers output per CoWoS wafer when the CoW sizes are up to 14x reticle, making the economics a puzzle to us. Facing the challenge from alternative options like Intel's EMIB-T, we understand TSMC has the incentive to “work very hard to meet all the demand” and “not leave any business on the table”, but apparently “CoWoS” is not an economically viable solution at such a large CoW size. We note that AMD believes interposers at >8x reticle size are moving toward panel level packaging for better economics (report); our “napkin math” shows that for an 8x reticle size interposer, a round 300mm carrier would produce 5-6 units vs 9-10 units on a square 300mm panel.

As such, we believe TSMC does have the motivation to get CoPoS ready earlier vs our prior projection of mass production in 2029F (report) if TSMC's AI customers do not compromise their chip design floor plans. The current status of 310x310mm CoPoS is mini-line build-out by mid-2026F, and TSMC management currently expects a volume ramp-up in two-to-three years from now. How quick can TSMC complete the development and turn that into high-volume production is noteworthy, in our view.

If TSMC manages to bring CoPoS online by 2H28F, we reason that Hon may see initial handler orders for large packages incoming in 2H27F, contemplating about 12 months of lead time from engineering qualification to volume ramp. Yet the initial driver may not be a leading AI GPU customer's 2028E platform based on our current perception of the physical architecture. The substrate body size of Feynman may fall within 120x125mm (Fig. 27) and fit well into the current JEDEC matrix tray.

Fig. 34: Larger interposers drive the shift to FOPLP
Source: AMD, NOM

The commercialization pathway to CoWoP is much longer without guarantee of success, although an even larger chip package could galvanize handler refreshes. We delved into nVidia's innovative "chip-on-wafer-on-PCB (CoWoP)" in our Asia AI Semi & Server Anchor Report in August 2025, explaining that the CoW module is directly mounted onto a substrate-like PCB (SLP), which thereby eliminates the ABF substrate between the CoW module and high-density interconnect (HDI) PCB in the current configuration (Fig. 35). Switching from an IC substrate to an HDI PCB will essentially enlarge the package footprint and hence could galvanize new ATC/handler purchases for new mechanical designs (e.g. the shift to mega trays) and more challenging thermal requirements which are clearly a boon to Hon's equipment sales. Although we think SLP makers such as Unimicron (3037 TT, Buy) and Zhen Ding (4958 TT, Buy; Avary [002938 CH, Not rated] is its subsidiary) will continue to stay involved in the development given their past records of supplying to iPhone mainboards from 2017, ensuring low warpage and decent flatness when manufacturing CoWoP SLP, which is much larger and thicker than iPhone SLP, could be very challenging, and new materials might be considered.

In addition, as IC substrates bridge the line/space (L/S) differential between chips and PCBs, the removal of IC substrates might need extra RDLs build-up underneath CoW interposers. The bump pitch matching and coefficient of thermal expansion (CTE) matching between ICs and SLPs will be critical for CoWoP, and it could take a long time to resolve detailed technical issues.

We thus believe this project might remain in the R&D stage for the upcoming Rubin Ultra and Feynman. We will closely monitor the progress of this project, and would not be surprised if nVidia makes changes to adapt to real-world challenges.

Fig. 35: CoWoP replaces ABF substrate + HDI PCB with SLP
Source: NOM

## Emerging OSATs' 2.5D engagements bode well for Hon, too

We render that more 2.5D/CoW engagements and capacity additions by OSATs could be a production driver for Hon's handler business, aside from TSMC's expansion. We first wrote about TSMC's prudent approach to CoW capacity expansion in our Asia AI Semi & Server Anchor report in August 2025, and noted that such planning was critical for OSATs as it had driven most AI chip customers to look for alternative CoW suppliers. We estimate ASE (3711 TT, Buy) could form 25kwpm of FOCoS capacity by end-2026F, from 5kwpm installed by end-2025.

Amkor (AMKR US, Not rated) is also an alternate CoW partner, and management has highlighted over a dozen 2.5D engagements (silicon interposer-based, as per Amkor's definition) and expected high-density fan-out RDL devices (i.e., organic interposer-based) ramping up production in 2026E and bridge-type solution for AMD in 2027E (see Amkor's Investor Day 2026). Our industry checks suggest Amkor might have a c.15kwpm of 2.5D/SWIFT capacity by end-2026F.

Despite many 2.5D/molded interposer-based packages in the pipeline of OSATs are for CPUs owing to more relaxed technological requirements (e.g., RDL line/space) and the absence of expensive HBM content (report), these chip packages are naturally more complicated than conventional FCBGA and could prolong the testing time. We elaborate about CPU opportunities in the subsequent section.

Fig. 36: 2.5D advanced packaging solution comparison


Source: Company data, NOM

Fig. 37: Major CoW projects at OSATs


Source: Company data, NOM

## Hon to benefit from increasing testing spending by AI OSATs

We expect Hon's ATC/handler business to benefit from an increase in testing capex by AI OSATs as large package footprints remain the pillar of AI accelerators, and OSATs are aggressively adding floor space and tester capacity in response to the exponential surge in total test time per devices. We compile the capex plans and estimates of major OSATs with testing service exposure to North American AI chip customers, which appear poised to grow significantly in 2026-27E. Although some of them do not break down spending budgets to the assembly and testing stage, directionally we expect higher dollar spend on testing, with potential upside, contemplating TSMC's more aggressive CoWoS expansion plans and OSATs' participation in the full 2.5D turnkey. Meanwhile, SEMI also projects global test equipment spending to record a c.20% CAGR over 2025-28E. We believe all these factors indicate a robust ATC/handler growth trend for Hon through 2028F. For its near-term trajectory, we compare Hon's equipment set revenue patterns to leading-edge SoC tester TAM projections provided by Advantest and Teradyne as well, in view of the 1-for-1 relationship between tester sales and ATC/handler sales, which both imply robust y-y growth for Hon's equipment business.

Fig. 38: AI OSAT capex trend
Source: Company data, Bloomberg Finance LP, NOM estimates

Fig. 39: Increasing test equipment spending
Source: SEMI, NOM

Fig. 40: Hon's equipment set revenue vs. SoC tester estimates by Advantest
Source: Company data, NOM estimates

Fig. 41: Hon's equipment set revenue vs. SoC tester TAM estimates by Teradyne
Note: Teradyne has not yet broken down ATE TAM of USD12-14bn in 2026E. We assume 80% of TAM goes to SoC testers based on historical patterns.
Source: Company data, NOM estimates

## Hon likely records more progress in SLT handlers

Hon historically focused the vast majority of its business engagements on FT handlers (70-80% handler revenue comes from FT), but traditional ATE-driven FT alone may be no longer sufficient to detect all structural and functional defects since logic chip packages become more complicated. Hon has been making inroads into the SLT handler market by leveraging its competency in customization and ATC, and we believe a US CPU/GPU customer is one of its longstanding customers in SLT handlers.

We are aware that Hon has started an engineering collaboration with a US AI GPU vendor in SLT handlers for future-generation AI GPUs, and yet we have not factored this into our earnings estimates given the uncertainty of success; the segment is currently dominated by Chroma (2360 TT, Buy). In our view, Hon's new SLT handler opportunities could lie

squarely within ASIC customers whose broader adoptions of SLT on top of mandatory FT has ballooned.

## Mobile APs and CPUs also undergo architectural changes

We believe Hon could monetize the rising design complexity in certain mobile APs and CPUs due to the shift from a monolithic to a multi-die layout, and advanced packaging adoption originally pioneered in the AI/HPC space. The architectural changes could prolong testing time and therefore are clear positives to tester and handler purchases/upgrades. Meanwhile, chip performance boosts may drive additional ATC demand for more precise temperature control during the testing stage. Despite Hon's relatively small revenue contribution from mobile communication (10% of tool orders in 2025), our supply chain checks suggest Hon has a very strong foothold in FT handlers in mobile APs, supporting flagship mobile AP customers' products, and some high-end devices need air-cooling ATC as well.

## Apple's WMCM and SolC-MH could foster Hon's ATC/handler sales, and its packaging innovation endeavor is worth monitoring

We assume Apple's AP demand would remain strong despite declining Android units (report) and more importantly, Apple's upcoming A20 Pro package shift to wafer-level multi-chip module (WMCM; report) will likely be the spotlight of ATC/handler upgrades in the mobile communication vertical in 2026F. We believe Hon will be the FT handler supplier for WMCM-based AP, to pair with the tester from Teradyne, and the test handler will require an ATC capable of thermal management up to 3,000W, vs. no ATC setup for the current InFO-PoP test handler. The ATC capability, in our view, could be more than sufficient to resolve potential self-heating issue of DUT, given that AP TDP usually ranges within 10-15W. We project \~50% boost to WMCM handler set ASP vs. InFO-PoP.

WMCM is a chip-last (RDL-first) fan-out scheme, which is comparable to TSMC's CoWoS-R process (yet without substrates), and RDL-first enables build-up of more RDLs at finer line/space (L/S) than InFO and therefore ensures better chip performance. We expect the WMCM process to shrink RDL L/S of A20 Pro to 5/5um, compared with InFO-PoP at 10/10um, with identical three layers of RDL (Fig. 42). In the July 2025 report, we believed Apple would not grow its RDL layer count in A20 Pro likely because: 1) consumer applications do not require as many RDL layers as AI/HPC applications, whose layer count is typically more than five; or 2) Apple might utilize A20 Pro/WMCM as an experimental platform for potential future changes in packaging architecture.

As discussed in the “Global Advanced Packaging – The evolution of CoWoS, SolC and InFO” report, our supply chain analysis suggests Apple has been likely working on a few hybrid bonding/SoIC projects for M-series silicon. Apple debuted M5 Pro and M5 Max in March 2026 (press), and we witness that Apple disaggregates CPU and GPU blocks in the previous monolithic die into discrete sub-dies, and TSMC uses SolC-MH to bond CPU and GPU chiplets onto a passive interposer using bump-less face-to-face hybrid bonding (Fig. 43). While the SolC-MH architecture is somewhat similar to 2.5D CoW, the M5 Pro/M5 Max can achieve substantially higher die-to-die interconnect density by replacing micro-bumps (2.5D CoW) with bump-less hybrid bonding, and reduce the parasitic losses (or “chiplet tax”) in chiplet-based layout.

We reason the shift to disaggregated die design could spark more stringent requirement for multi-zone thermal control during the testing stage, and thus the test equipment maker could enjoy a potential upgrade to ATC/hander. Furthermore, we believe it is worth monitoring the supply chain dynamics about whether Apple could bring SoIC in junction with WMCM (possibly with more RDL layers) to its M-series (or even mobile APs) beyond 2027F, given Apple's endeavor to foster chip packaging innovations at TSMC. More complicated, powerful silicons are apparently tailwinds to the backend testing supply chain including Hon's ATC/handlers.


Fig. 42: WMCM places memory and AP side by side
Source: Company data, NOM estimates
Source: TechSearch International
- Hybrid bonding combines a common CPU chiplet with different GPU chiplets (e.g. Pro and Max)

Fig. 43: A cross section of SolC-MH in Apple M5 Pro and M5 Max

\- Hybrid bonding of separate CPU and GPU chips to Si base die to form a single SoIC with very low die-to-die latency

\- Reduces die cost and increases yield by dividing chip design into 2 smaller chips

Source: Besi, TechSearch International, NOM

## CPU testing growth recipe – higher volume meets more complexity

There have been growing discussions about server CPUs since 2H25 thanks to agentic AI, including insufficient supply as well as a crowd-out effect on client CPU production. Server CPU covers plain CPU for non-AI general servers, head-node CPUs paired with accelerators, and CPUs used for AI workloads (but not with accelerators). We believe the second and third categories are driving substantial demand for server CPUs, especially the last one after the agentic AI boom. Notably, AMD in May 2026 doubled its server CPU TAM forecast from USD60bn (provided in November 2024) to USD120bn+ by 2030E. We think Hon's handlers could ride on a stronger CPU demand volume, as it has been the primary handler vendor to support a US CPU customer.

We also observe changes in server CPU floor plans which could bring structural tailwinds to backend testing and Hon's handler sales, in our view. nVidia and some ARM-based CPUs by CSPs are moving from monolithic designs to multi-die or chiplets and possibly utilizing more advanced packaging technologies to facilitate faster die-to-die interconnects, such as molded interposers by TSMC's CoWoS-R and Amkor's S-SWIFT. nVidia's CEO Jensen Huang at the COMPUTEX keynote speech this year also spent more time on Vera CPUs and mentioned that "Agent is a new workload. We built CPUs for humans in the past. We need CPUs for agents, agentic systems. The properties are different – why would the old CPUs be the same?". See our Asia AI Semi & Server Anchor Report for more details about CPU architecture revolutions.

nVidia's Vera CPU packages one compute die, one I/O die and four memory interface chiplets on a 2.2x reticle-sized organic interposer. nVidia emphasizes all 88 Olympus compute cores are in one monolithic compute mesh without “chiplet tax” in core-to-core communication, and builds separate dies for memory controllers and I/Os to maximize the compute die area utilization for compute purposes. We think the chip design philosophy to offload memory controller blocks from the core compute complex may eventually become a common practice by ARM-based CPU designers and even AI accelerators (e.g., TPU v9 has independent memory fabrics, in our view; MediaTek has publicly illustrated such a concept, Fig. 44) to leave the precious die area to core compute.

We also flagged demand upside from Google's ARM-based CPU “Axion N4A” (on TSMC 3nm; codenamed “Cypress”) to the Asia supply chain in August and December last year, which was in part driven by the CPU adoption shift in TPU 8t/8i from x86-based to Google Axion. We believe the supply chain logistics of Axion N4A are handled by GUC (3443 TT, Neutral), and KYEC (2449 TT, Buy) supports the FT stage using Advantest's ATE paired with Hon's ATC/handler, as well as the SLT stage using Chroma's handler. The current project in production has a monolithic layout, but our industry checks suggest the next generation may be a dual-die configuration, still utilizing FCBGA package, for releases in 2028F.

Admittedly, those changes in CPU layouts may not stipulate very large substrate sizes to foster transitions to mega trays and handler mechanical refreshes, but we argue that

chiplet-based or multi-die floor plans will trade monolithic simplicity for a highly complex testing paradigm to validate die-to-die interconnect efficiency at a longer testing time. Moreover, the multi-die layout naturally distributes the thermal load across the package and hence poses an intricate thermal management challenge to the ATC. The system must deploy ultra-precise, multi-zone active thermal heads to dynamically balance the wildly mismatched self-heating conditions across dies to prevent inflicting thermal damages on the chip package. Hon, in our view, possesses one-of-a-kind ATC capabilities to stand out as early in the engineering phases.

Fig. 44: Offloading memory controller interface blocks to chiplets
Source: MediaTek, NOM

Fig. 45: An overview of CPU layout
Source: Company data, NOM estimates

# Service flexibility and a well-extended thermal control roadmap to trump competition

We believe Hon's ATC/handlers can stand out among both regional and global peers in particularly high-power AI/HPC applications, due to: 1) unmatched customization; 2) pioneering ATC know-how; and 3) proximate flexibility in servicing the semiconductor backend cluster in Taiwan. The adjacency to the completed semiconductor ecosystem in Taiwan and more timely field engineering than overseas counterparts is an advantage shared by most Taiwan-based equipment makers, in our view. While IC test handlers alone might initially seem like simple mechanical automation which is often oversimplified as mere robotic arms picking and placing devices under test, the reality under the hood is a sophisticated combination of high-precision micro-mechanics and solid knowledge in thermal physics.

Theoretically the tier-one ATE maker Advantest could have enjoyed a natural installed base advantage in test handlers sales since handlers are used along with tester, and Advantest has advanced technological capabilities in mechatronics to optimize the coordination of handlers and testers. This is particularly valid in memory testing, where the testing relies on extreme parallelism (i.e. high throughputs on fairly standardized interfaces). Advantest was able to build up a large handler market share in the past when it leveraged its memory tester installed base, before it gradually lost ground to emerging memory handler specialists like Techwing (089030 KS, Not rated).

Hon's ATC/handler business serves primarily logic semi (it only had 1-2% of tool orders from memory in 2025), where the inherent advantage of Advantest disappears entirely. Logic packages are of high varieties than commodity memory, featuring varying physical dimensions, ball counts/pitches, etc., and this requires deep, early-stage collaboration during the new product introduction (NPI) phase as well as close-knit communication with specialized test interfaces (load boards and sockets) to build bespoke mechanics inside handlers. Specialized handler makers such as Hon can thrive on engineering fluidity. By contrast, Advantest does not devote many resources to tailor handlers given that handlers are essentially “sidekicks” (1-2% of total revenue) and IC testers are its core business lines. This may also explain why Teradyne does not have its own handler business units given a great exposure to logic testing.

Handler customization is especially important and necessary in the realm of AI/HPC and ASICs due to large die sizes, complex multi-die packaging (e.g. 2.5D/CoWoS) and ultra-high pin counts, and Hon is an expert in these areas (72% of tool orders from AI/HPC and ASICs in 2025). Hon engages directly into the embryonic development phases of AI/HPC and ASICs through tight NPI collaborations with end customers backed by a robust IP portfolio of more than 600 patents filed globally across thermal control, high-throughput, and active optical inspection (AOI), and ships early configurations to end customers' R&D labs for engineering validation and joint developments. We summarize Hon's NPI status (data as of 2Q25) in Fig. 46.

Furthermore, the handler is more than a sheer mechanical sorter in AI/HPC testing as the accompanying ATC becomes an active execution environment. Hon's dual-temp and tri-temp ATC cover a broad spectrum of operating temperatures and cooling systems (liquid-cooling, refrigerant-cooling, and air-cooling), and the company continues to move forward in capabilities with an extended roadmap to 7,000-8,000W readiness and >10kW in the engineering pipeline (Fig. 28). A clear visibility of ATC roadmap and well execution, in our view, puts Hon in a more favorable position for AI/HPC clients looking to initiate new chip development.

Fig. 46: Hon's NPI status by application and end-customer location
Note: Data as of 2Q25.
Source: Company data, NOM

Fig. 47: Comparison of major global tester and handler makers (ex-China)


Note: Market cap data as of July 17, 2026
Source: Company data, Bloomberg Finance LP, NOM estimates

## Hon is not absent from the manufacturing reshoring trend

We reason that Hon has strategically positioned itself in the semiconductor reshoring trend thanks to an extension of subsidiary network to the US in 2022, and to Germany in 2025 to close geographical gap and enhance service efficiency and localized supports. While the company's core equipment manufacturing hubs remain heavily anchored in Greater China to maximize production efficiency, these overseas subsidiaries could be vital beachheads for future expansions aligned to customer requests.

The global semiconductor manufacturing supply chain is undergoing a structural reshuffle owing to chip vendors' diversification needs in tandem with their home countries' government incentives. For instance, the US government has exerted aggressive industrial regimes including the CHIPS and Science Act and tariff pressures to rebuild (or replicate, to some extent) the domestic hardware ecosystem. American companies such as Apple and nVidia have touted homegrown supply programs (news and news).

Hon's US subsidiary is located in Austin, Texas, thereby placing itself amidst one of the burgeoning silicon clusters in the US, in our view, since a few American advanced chip designers like AMD and Tesla (TSLA US, Not rated) have campuses there. In Germany, we note that Hon's presence is to target distinct demand profiles and focus on the automotive and MEMS chip testing sectors in Europe.

As Hon derives >50% of revenue from US end-customers, we think the most critical reshoring movements are TSMC's (advanced logic fabrication/packaging) and Amkor's (advanced packaging) expansion plans in Arizona, US, and KYEC's recent decision to build a factory in the US (news). TSMC's plan, as of March 2025, was to build an advanced logic semiconductor production cluster with six wafer fabs and two advanced packaging facilities (press release). The company recently unveiled plan to invest an additional USD100bn in Arizona (report). According to TSMC, it has already started N4 mass production at Phase 1 and plans to move in tools in 2H26E at Phase 2 for N3 volume production in 2H27E; it has also started Phase 3 fab build (for N2) and will start the construction of wafer fab Phase 4 and an advanced packaging factory (AP1) this year (Fig. 48). As for Amkor, the company looks to invest USD7bn in an advanced packaging greenfield factory in Arizona, close to TSMC's fabrication complex, with high-volume manufacturing for the first phase slated to begin in 2028E and reach full-scale build-out by 2030E (Fig. 49).

Additionally, TSMC and Amkor have announced a long-term partnership in advanced backend services in the US (news and news) likely because end-to-end regional supply would require coordination of wafer fabs and advanced packaging and test. Our current assumption is that TSMC might tilt the majority of new advanced logic capacity toward more lucrative AI/HPC silicon production, and advanced packaging capacity to CoW (rather than the full CoWoS turnkey) to better justify a more hefty outlay compared to investments in Taiwan, and Amkor's new site thus would shoulder more burden on WoS assembly and share backend testing workloads with KYEC. When TSMC, Amkor and KYEC start to tool the new sites and ramp up production, likely from 2028F, we expect Hon to benefit from another wave of machinery spending. We also believe Hon might have been mulling over potential factory setup in the US, likely for final tool assembly, while leaving the module production in Taiwan.

Fig. 48: TSMC is investing in the US
Source: TSMC, NOM

Fig. 49: Amkor is also building a backend megasite in the US
Source: Amkor, NOM

Fig. 50: Hon's global footprint enable localized support, and Hon might be mulling over potential factory setup in the US
Source: Company data, NOM

## Hon has a dominant position in high-end China AI and automotive testing

Hon derives about 20% of revenue from China, where the company focuses on AI/HPC and automotive verticals given more rigorous thermal control requirements during the test phase. Indigenous handler suppliers in China are mainly Changchuan (300604 CH, Not rated) and JHT (603061 CH, Not rated). We believe Hon's test handlers have a strong foothold in high-end Chinese AI/HPC and automotive chips, thanks to its superior temperature control capabilities at extremely high/low temperature (up to 170°C/down to -70°C) and greater cooling capacity (potentially up to 7,000-8,000W). China domestic counterparts' ATC are based on refrigerant-cooling or air-cooling and have not yet developed liquid-cooling ATC which are ideal for AI/HPC chip testing because of a faster heat transfer. We compare Hon, Changchuan, JHT, and other Chinese tester/handler vendors in Fig. 51.

Hon's ATC/handlers are well positioned to capitalize on China's efforts to foster domestic AI/HPC silicon, in our view. China has shifted toward 2.5D advanced packaging, which aggregates more mature silicons to achieve target computing performance, to bypass tightening US curbs on its procurement of advanced wafer fabrication equipment. JCET (600584 CH, Buy) and SJ Semi (688820 CH, Not rated) are both very aggressive with 2.5D capacity expansion. As such, the testing complexity could skyrocket and unsanctioned backend testing equipment suppliers should be the beneficiaries, in our view.

Fig. 51: Comparison of Hon and Chinese indigenous tester and handler makers


Source: Company data, Bloomberg Finance LP, NOM estimates

Fig. 52: China OSAT capex trend
Source: Company data, Bloomberg Finance LP, NOM

## The unsung hero of new technology deployments

We believe the role of semiconductor testing has also evolved into a foundational anchor that actively drives next-generation hardware architectures, in addition to a sheer post-manufacturing checkpoint, and Hon is poised to not only monetize the new technology adoption, but also steer the development. We see CPO and MCL emerging on the horizon, moving from R&D innovations to possibly support future chip-level/system-level interconnects and thermal dissipation respectively, but both will likely require an overhaul of current semiconductor backend test flows and simultaneously modifying and retrofitting testing tools (e.g., ATE and handlers). We think TSMC and its OSAT ecosystem partners have the incentives to raise investments in CPO and MCL from 2027F, in preparation for possibly broader adoption starting from Feynman in the earliest (scheduled fo 2H28E), and we thus expect Hon to ride on the spending wave with ASP upgrade tailwinds in 2027-28F.

## New handler opportunity to start with CPO test insertion 4

We expect Hon's ATC/handlers to play a role in CPO testing, likely starting from test insertion 4 optical/electrical co-test (O/E co-test). O/E co-test is a multimodal test that simultaneously validates the optical and electrical properties of a CPO module housing switch ASIC and optical engines (OEs).

Any undetected defect in a single optical component would force manufacturers to scrap an entire expensive CPO switch module, and therefore testing cannot wait until final assembly. Strategically inserting tests early to validate known good optical/electrical dies and inspecting packages is the only way to manage the intense thermal-mechanical vulnerability of CPO and ensure viable manufacturing yield. As far as we are concerned, at the moment, there are four test insertions during TSMC and its ecosystem partners' CPO production, with two occurring under the scrutiny of TSMC and the subsequent two occurring at OSATs. See details of test insertions in our Anchor Report.

We think Hon could collaborate with ATE maker Teradyne in test insertion 4, with Teradyne's tester responsible for feeding electrical signals for testing; optical testing would be carried out by dedicated instruments (potentially by Keysight [KEYS US, Not rated]), in our view. Hon's handler will first facilitate optical alignment from an external laser source (ELS) to OE, via a receptacle or fiber array unit (FAU), and this process could be quite time-consuming and complicated. After setting up alignment, Hon's handler would enable the tester and instrument to test switch ASIC and OEs in one single touchdown. An ATC is also required in test insertion 4. Hon aims to complete the engineering verification by end-2026E and begin shipments in 2027E to address volume ramp-up in 2028E. Yet given fluid supply chain dynamics and uncertainty about CPO ramp-up timeline, we do not factor in contribution from CPO in detail. Any substantial progress could present an upside to our earnings forecasts beyond 2028F, in our view.

## Hon's current business with CPO FT is electrical test only

We note that Hon has already shipped ATC/handlers for electrical tests (E/E test) of CPO switches in production (e.g., nVidia Spectrum-X and Quantum-X). The E/E test is executed on switch ASIC and OE together, or switch ASIC and OEs on a standalone basis.

Fig. 53: CPO insertion flow
Note: This is a conceptual illustration, not specific to any company or project.
Source: NOM

Fig. 54: CPO insertion flow and potential suppliers


Source: NOM

Fig. 55: Hon's role in CPO test insertions


Source: Company data, NOM

Fig. 56: How CPO switches are tested in the current CPO FT vs. CPO test insertion 4
Source: Company data, NOM

## MCL may require changes to ATC/handler and testing flows

We think the thermal challenges arising from Feynman's first-ever GPU-on-GPU SolC stacking could again spark industry evaluation and discussion of MCL adoption as the structure may drive chip TDP easily above 3,000W, and more importantly, a sharp leap in power density/heat flux on fairly limited expansion in interposer/substrate size. We believe there would be significant coordination of workflows and clarification of responsibilities as the supply chain reshuffles and prepares for MCL, and Hon could largely lead in technological breakthrough. We believe a dedicated new handler is a must for MCL-based packages, and Hon could have the tool platform ready in 4Q26F at the earliest.

Currently, liquid cooling cold plates are placed on heat spreaders, with a layer of TIM2 in between. Liquid coolant traverses through the channels on cold plates and removes heat from the processors underneath. The convective heat transfer coefficient is the predominant factor of liquid cooling performance, directly correlated to the fluid flow rate and inversely correlated to channel pitch. Nevertheless, higher flow rates or narrow channel dimensions come at the cost of higher pressure drop between the liquid inlet and outlet, which could consume more energy to pump the coolant.

An MCL integrates coolant channels on a cold plate into a lid cover or heat spreader (“microchannels”) and eliminates the use of cold plate and TIM2 layer. The traditional heat dissipation path of “Die→TIM1→Lid→TIM2→Cold Plate”, is thus shortened to “Die→TIM1→MCL”. The elimination of the use of TIM2 and the boundary between heat spreader (lid) and cold plate can reduce thermal resistance and upgrade cooling performance (Fig. 57). The MCL use could be necessary, since the traditional single-phase liquid cooling cold plates could reach their heat dissipation limits when AI chip TDP approaches 3,000W. An extensive technology discussion of MCL and advanced cooling alternatives can be found in our October 2025 Asia AI Thermal Anchor Report.

Assembly of MCL on top of a chip package will likely be done by CoWoS makers (TSMC and its alliance). Currently, TSMC and its OSAT partners attach a heat spreader as the last step of CoWoS, and a cold plate is attached to the IC package by ODM and/or EMS providers. The heat sink/cold plate attachment equipment is subject to modification to fit in a new heat spreader design as well. The adoption of MCL could affect how chips are tested to ensure no coolant leakage after CoWoS assembly, and testing equipment might undergo reconfiguration for thermal controls and ensure no excess contact force exerted on the MCL leading to damage.

Fig. 57: MCL and its cross-section view
Source: Micromachines, Volume 13 (2022), Issue 1 “Evaluation and Optimization of a Cross-Rib Micro-Channel Heat Sink”, NOM

## Earnings forecasts and financial analysis We expect a 70% net earnings CAGR over 2025-28F

After strong 116% y-y revenue growth in 2025 driven by a US AI GPU vendor's OSAT partner's testing ramp-up and capacity expansion to support strong demand for the AI GPU platform, we expect Hon's revenue to increase by 90% y-y in 2026F, since the Asia AI OSAT supply chain continues the capacity expansion for not only the US customer's AI GPU platform refresh, but also AI ASIC camp's strong ramp-up (notably a top US CSP). In addition, Apple's migration in chip package technologies (e.g. WMCM) adds to the strong momentum. We expect Hon's revenue to witness a 69% CAGR over 2025-28F given the structural testing trend of increased complexity and longer time and its endeavor to expand factory space.

We model Hon's equipment set shipments based on its productivity and loadings, and is aware of the company's plan to grow total factory floor space by $50\%$ p.a. in the next few years (we estimate $40 - 45\%$ equipment set capacity growth p.a.). We summarize Hon's current factory and upcoming plans in Fig. 73. For equipment manufacturers, there is always lead time between equipment shipments and revenue recognition, given the need for tool installation, pilot runs and verifications, and Hon generally books revenue three to six months after tool shipments. We factor the two-quarter lag into our earnings model.

We note that Hon's equipment set sales include handler, ATC and cold plates in one set, and based on Hon's estimates, the current equipment set ASP comprises 42% from handlers, 33% from ATC and 23% from cold plates. We see fairly limited growth in handler ASP before the mechanical refresh advent steered by large-package handlers or MCL handlers. Most of the incremental ASP, in our view, will be underpinned by ATC upgrades in tandem with AI/HPC customers' chip roadmaps. We therefore project Hon's equipment set blended ASP will grow from TWD12mn in 2025F to TWD20mn in 2028F.

The initial equipment set opportunities from MCL and CPO test insertion 4 (albeit likely small) might kick in from late-2026F at the earliest, but we have not yet contemplated the detailed contribution of MCL or O/E co-testing in our earnings estimates as the supply chain dynamics remain fluid, and we have to continue monitoring the development and viability of new technologies.

On the profitability front, we project a rather stable GM profile across Hon's major product lines, and believe tool upgrades (notably ATC) are the predominant factors to the company's GM upswings. Our current assumptions consider a steady step-up in ASP to reflect continued ATC upgrades along with AI/HPC customers' roadmap primarily. Despite not in our estimates as yet, we believe MCL and CPO test insertion tools could be accretive to Hon's GM at a higher-than-average ASP. We, hence, model GM of 56.7%/56.9%/56.9% in 2026F/27F/28F, vs 56.5% in 2025.

Blending in a 60% opex CAGR over 2025-28F (we note that Hon expects 50% headcount growth in 2026E and continues to expand factory spaces), we anticipate Hon to enjoy operating leverage from rapid top-line expansion and grow its OPM to 51.1% in 2028F from 49.7% in 2025. In all, we estimate the company to deliver a 70% EPS CAGR over 2025-28F and are aware that a successful ramp-up of new technologies (MCL or CPO test insertion) into 2028F could drive a significant earnings upgrade.

We anticipate a stable cash conversion cycle (CCC) for Hon, and model Hon to dial up capex to TWD1.5bn/TWD2.4bn/TWD3.7bn in 2026F/27F/28F vs an average spending of TWD210mn a year during 2023-25, due to its intention to grow factory spaces. That said, we think Hon will keep its earnings payout ratio at \~70% in coming years.

Fig. 58: Hon's revenue trend
Source: Company data, NOM estimates

Fig. 59: Hon's net profit and y-y growth
Source: Company data, NOM estimates

Fig. 60: Hon – P&L


Source: Company data, NOM estimates

Fig. 61: Hon's revenue breakdown by segment


Source: Company data, NOM estimates

Fig. 62: NOM forecasts vs Bloomberg consensus for 2026-28F


Source: Bloomberg Finance L.P. consensus, NOM estimates

## Valuation methodology and risks

We derive our target price of TWD11,100 based on 40x average 2027-28F EPS of TWD278. Our target P/E multiple is at the high end of Hon's historical trading band of 19-52x since its IPO, which we consider undemanding given a $58\%$ net earnings CAGR through 2026-28F. We believe a structurally extended testing time for AI/HPC chips and more stringent thermal requirements during test will continue to drive Hon's revenue and earnings expansion, alongside the company's efforts to enlarge its production capacity. Although we do not factor in contribution from CPO test insertions or MCL in detail, a successful ramp-up of new technologies and associated testing approach changes could drive further upgrades to earnings estimates beyond 2028F.

We select Hon's peers from semiconductor backend equipment and test interface vendors for valuation comparison. Hon is currently trading at 29x 2027F EPS and 19x 2028F EPS, respectively, and we view this apparently very attractive compared to an average valuation level of 39x by semiconductor back-end testing equipment makers and 35x by test interface peers, all based on 2027E EPS.

Major downside risks to our call include: 1) CoWoS and back-end testing capacity expansion slowdown; 2) slower-than-expected product refresh, platform performance upgrade, or ramp-up by the AI chip end customers; 3) fiercer-than-expected market competition in test handlers; and 4) weaker-than-expected end-market demand, particularly for AI servers.

Fig. 63: Hon's consensus P/E ratio
Source: Bloomberg Finance LP, NOM

Fig. 64: Hon's consensus P/B ratio
Source: Bloomberg Finance LP, NOM

Fig. 65: Semi test sector valuation comparison


Note: Priced as of July 22, 2026.
Source: Company data, Bloomberg Finance L.P., NOM estimates

Fig. 66: Hon's share price vs Bloomberg consensus EPS revisions
Source: Company data, Bloomberg Finance L.P. consensus estimates, NOM

Fig. 67: Hon's share price vs. monthly revenue
Source: Company data, TEJ, NOM

Fig. 68: Hon's share price vs events
Source: Company data, TEJ, NOM

## Company background

Headquartered in Taichung City, Taiwan, Hon. Technology was founded in 1999 and reincorporated to the current “Hon. Precision (Hon)” in 2015. Hon is a dedicated semiconductor equipment manufacturer focusing on IC test handlers and active thermal control systems (ATC) for IC backend testing. Hon’s client base spans across major IC design houses, outsourced semiconductor assembly and test vendors (OSATs), and integrated device manufacturers (IDMs) worldwide, and the company has also established a complete global service network via subsidiaries in China, the US, and Germany as well as agencies in Korea and Southeast Asia.

Hon's primary production bases are in Taichung City, Taiwan, and two sites in China. The company has been actively seeking new land or plants to further expand the equipment and jig/module capacity. Management expects more than $25\%$ factory space expansion and more than $40\%$ equipment set capacity growth in 2026E, with a preliminary target to enlarge factory space by $50\%$ every year onwards.

Hon's IC test handlers and ATC are used in the final test (FT) or system level test (SLT) stage of semiconductor production, for GPUs, CPUs, and application processors (AP). Hon's handlers are primarily pick-and-place handlers, which uses suction to transfer the DUT and press it into the test sockets. In ATC, Hon offers both dual-temp (high temperature [up to 170°C] and ambient temperature [around 25°C]) and tri-temp (high temperature, ambient temperature, and low temperature [down to -70°C]) ATC capabilities, based on three types of cooling system – Liquid-cooling (ATC3 series), Refrigerant-cooling (ATC5 series), and Air-cooling (ATC6 series) – with varying cooling capacity for different applications.

According to Hon, 78% of its tool orders are for AI/HPC/ASIC, 9% for automotive, 9% for mobile AP communication, 3% for consumer and 1% for memory/MEMS in 1Q26. The company sells its equipment primarily in sets, which can include test handlers, ATC systems, and customized cold plates. We estimate Hon to generate 76% of its revenue from equipment sets in 2026F, followed by 22% from jigs and modules (mainly standalone cold plate sales) and 2% from others.

Among the co-founder team, Wen-Ta Hsieh, Jung-Li Chang Chien, and Te-Kuei Weng, respectively, specialize in mechanical development, software design and production management. As of April 2026, the founding team members and their families together controlled a 51% interest in Hon.

Fig. 69: Hon's equipment offerings

## Product Lines

Source: Company data, NOM

Fig. 70: Hon's tool order mix by application
Source: Company data, NOM
■ AI/HPC/ASIC □ Automotive □ Mobile AP/Communication □ Consumer ■ Memory & MEMS

Fig. 71: Hon – global footprint
Source: Company data, NOM

Fig. 72: Hon – company milestones


Source: Company data, NOM

Fig. 73: Hon – factory sites and planning


Source: Company data, NOM

Fig. 74: Board of directors


Source: Company data, NOM
Note: Data as of May 2026.

Fig. 75: Hon's shareholder structure

Fig. 76: Share price vs SITE and QFII ownership
Note: Data of 22 July 2026.
Source: TEJ, NOM

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd., Taipei Branch (NITB), Taiwan. See Disclaimers for NOM Group entity details.
