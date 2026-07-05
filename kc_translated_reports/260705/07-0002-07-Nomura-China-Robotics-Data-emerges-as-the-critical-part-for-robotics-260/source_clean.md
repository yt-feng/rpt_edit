## Data emerges as the critical part for robotics

Volume-price divergence across four data types redraws the vendor map; dexterous hands sit on critical path to embodied AI

In our 28 June 2026 China Robotics – Optimus ramps; China scales up as cost curves bend lower report, we flagged that non-robot capture (tele-op, UMI, Ego) is becoming mainstream at c.20% of real-robot data cost. This report extends that call by pricing each data tier in the mix and mapping where the non-robot substitution holds — highlighting the real-machine slice remains the highest-value, most defensible pool in the mid-term.

Data becomes critical part; tele-op captures the highest hourly value in 2026E

Data collection is emerging as the critical part for humanoid robotics in 2026, with our estimated industry-level annual data demand at c.10mn hours on a c.100k-unit shipment scenario, based on our industry survey. Figure AI's (Unlisted) CEO frames the same view: "the biggest blocker for us now of going from where we're at today to like large-scale deployment is data. We need ... enormous amount of data." The four principal data types show a pronounced volume-price divergence: i) No-embodiment data — first-person (Egocentric / Ego) video plus UMI (Universal Manipulation Interface) — accounts for the largest share at 40–50% of total hours but commands only c.CNY100-300/hour (according to 36Kr [KRKR US, Not rated]), implying a 2026 addressable market of c.CNY1.0–1.5bn. ii) Real-machine tele-operation makes up c.30% of hours at c.CNY500-1,000/hour (according to 36Kr), translating into the largest single sub-market of c.CNY2.2–2.5bn — the highest-value tier on our read. iii) Failure-recovery data prices at c.CNY400–500/hour (based on industry survey) but remains a low-single-digit share as most players have yet to close the deployment feedback loop. iv) Simulation/synthetic data is the cheapest at c.CNY50 per 10,000 frames (according to DAMO), mapping to c.CNY0.5–0.6bn. We view tele-op and failure-recovery hours as the scarcest, highest-margin tiers in the near term, with Ego/UMI the fastest-growing volume pool. This tiered price-volume structure — cheap synthetic at the base, scarce tele-op and failure-recovery at the top — defines which vendors can build a durable moat.

## Closed-loop solution is a likely defensible model

Against this backdrop, we view a software-hardware closed loop — spanning collection, transmission, evaluation, training, deployment and debugging — as the structurally defensible business model for pure-play data vendors. Standalone Data-as-a-Service (DaaS) monetizes quickly on an hourly or project basis, but as customer data volumes scale, vendors lacking an evaluation stack or brain-level capability face rising vertical-integration risk from downstream humanoid OEMs. The closed-loop model captures first-party scene data, failure samples, evaluation outputs and deployment telemetry, which we see as the pre-requisites for a genuine data reinforcing-loop and recurring revenue. Upfront investment in toolchains, hardware and on-site deployment is substantial, but we regard the long-term ceiling as commensurately higher. Based on our industry survey, payoff is tightly linked to the embodied-AI inflection: industrial use-cases (handling, sortation, machine-tending, assembly) is likely to reach a qualitative breakthrough in 2027–2028F, with humanoid shipments likely to grow meaningfully in the period; household deployment likely awaits after 2030, and with hotel/serviced-apartment cleaning the earlier wedge. Public disclosures from Physical Intelligence, NVIDIA (NVDA US, Not rated) and Lightwheel triangulate the same conclusion: simulation is a force-multiplier, not a substitute for real-machine data. π0.5 posts c.94% success on multi-step household subtasks and 75–80% across long-horizon household task categories; NVIDIA's synthetic-motion pipeline lifts GR00T N1 real-robot performance by c.40% vs real-only training; and Lightwheel reports an optimal c.10:1 synthetic-to-real training ratio delivering an average c.30% model-performance uplift, with case-level task success rising from 60% to 85% under joint real-plus-sim training. Simulation already covers most


Frank Fan - NIHK


## Donnie Teng - NIHK


handling/sortation hours, while precision assembly and contact-rich or flexible-object manipulation still require real-machine fine-tuning; household scenarios remain simulation-inadequate on a standalone basis for the next three-five years, in our view.

## Size-versus-sensor trade-off defines the dexterous-hand

The reason precision assembly and contact-rich tasks resist simulation — and the reason household deployment is a post-2030 story — traces back to the hand. The dexterous-hand competitive landscape is defined by an unresolved size-versus-function trade-off: the closer the hand approximates human dimensions, the better the mapping between training-data collection and downstream operation, but shrinking form-factor leaves insufficient volume for sensor payload. Among domestic players, only one vendor is described as truly human-hand-sized, while the leading tactile-focused hand and other high-DoF designs remain visibly oversized, degrading data-to-execution coherence. Tactile technology carries its own ceiling: point-pressure sensors cannot register lateral force or slip, and current e-skin exhibits poor fidelity on lateral-force curves — even the size-leading whole-hand solution carries only c.80 pressure points. On the arm side, the market has bifurcated: harmonic-drive-plus-torque-sensor arms (e.g. the Luna/Skye family) are drifting toward industrial-manipulator territory with limited bionic character and hard-to-find humanoid use-cases (based on our industry survey). Our takeaway: high arm precision only resolves intermediate motion, whereas a sufficiently capable hand can compensate for a lower-precision arm; we prefer architectures that omit torque sensors and harmonic drives and concentrate capability at the end-effector. Transmission choices reinforce this: harmonic reducers (typical ratios 1:200–1:800) dominate, planetary reducers serve high-load leg/ankle joints, and tendon drives (c.20N/2kg) suit flexible-object handling but suffer durability limits, while linkage drives deliver force at the risk of crushing fragile items. Net-net, until hand-side dexterity and tactile fidelity close the gap, the value pool for real-machine tele-op data — and for vendors owning the closed loop that captures it — remains structurally protected, in our view.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.


We, Frank Fan and Donnie Teng, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.
