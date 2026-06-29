## Physical AI: From NeuralAxis blueprint to Unitree

On 15 June 2026 we visited Unitree (Unlisted) to update on the company's latest developments (Takeaways from Unitree visit ahead of its listing). This report frames Physical AI commercialisation around two complementary layers: a "system-architecture blueprint and safety doctrine" for landing Physical AI in the real world, and, following the test release of Unitree's WVLA2.0 (World-model Vision-Language-Action) embodied large model, our read on how Unitree turns that blueprint into a shipping product and a commercial roadmap through model fusion and hardware-software co-design.

## NeuralAxis by NXP: The reflex-first blueprint for physical AI

The NeuralAxis (Neural Axis Architecture) framework was proposed by NXP (NXPI US, Not rated), unveiled by President and CEO Rafael Sotomayor at the COMPUTEX 2026 keynote. Its premise is that Physical AI's binding constraint is not scaling language-model reasoning but engineering a low-latency reflex layer akin to human unconscious response, consistent with Moravec's paradox. NeuralAxis mirrors the human nervous system across three decoupled yet coordinated tiers: a reasoning layer (cortex, \~300ms), a coordination layer (cerebellum) for motion control and balance, and a reflex layer (spinal cord, as low as 40ms) pushed to the edge near actuators—jointly delivering low latency, distributed control and high energy efficiency. The implication for humanoids is most acute: rather than a central brain, reflex processors are distributed to joints, hands and feet, enabling local autonomous decisions—grip-force control, ankle balancing—and chained recovery of balance, grasping, posture and gait within 40ms, while decoupling reasoning from motion control preserves stable locomotion as new skills are added. The same blueprint compresses drone glass-to-glass latency to within 20ms and segments software-defined-vehicle control into reasoning, coordination and safety-critical zonal execution. On commercialisation, our industry checks indicate meaningful manufacturing productivity uplift versus conventional automation and a likely sharp rise in diagnostic-robot sales.

From blueprint to product: WVLA2.0's world-model-VLA fusion and co-design

While the NeuralAxis document defines Physical AI's architecture blueprint and safety doctrine, Unitree's WVLA2.0 minutes show how that blueprint becomes a product through model fusion and hardware-software co-design. WVLA2.0, the first commercially deployable iteration after two years of development, fuses the WMA (World-Model Action) model's predictive capability with VLA's end-to-end action generation, diverging from peers betting solely on VLA. The architecture upgrades high-level task comprehension, 2D/3D spatial-semantic reasoning, dynamics-constrained action generation and disturbance resistance. Perception fuses four parallel visual streams—an RealSense (Unlisted) depth camera, a Livox (Unlisted) MID360 LiDAR (Light Detection And Ranging) and two side cameras—into a 360-degree representation, with position updates within 10ms under interference. On co-design, post-inference action parameters are dispatched via CAN (controller area network) bus to the G1's 23-degree-of-freedom joints, leveraging Unitree's "cerebellum" motion control; single-arm grasping of sub-2kg objects holds positioning error within 5mm. Lightweighting caps edge compute below 100 TOPS, running fully on the G1 EDU's NVIDIA (NVDA US, Not rated) Jetson Orin NX without cloud dependence, avoiding latency- and disconnection-driven task interruption, in management's account.

## Embodiment-free data capture becomes mainstream

The data-collection paradigm is shifting decisively toward "embodiment-free" capture as the mainstream approaches. In a single-take demo, a WVLA2.0-equipped G1 autonomously completed six tasks in a disturbed meeting room without teleoperation,


Frank Fan - NIHK

## Donnie Teng - NIHK


evidencing long-horizon execution and a perception-prediction-decision-action closed loop at \~90ms per inference, roughly ten iterations per second. Our industry checkssuggest some limitations: blind spots and rear-area perception gaps, elevated noise, slow execution and imprecise fine manipulation, alongside a lack of quantified continuous success-rate benchmarks. Management guides industrial manufacturing—joint-motor assembly, loading, fixture handling—as the earliest landing zone given Unitree's in-house factories, followed by logistics sorting, flexible 3C assembly, and later home and healthcare scenarios, where open, unstructured environments raise difficulty sharply. Management views Unitree's differentiation as full-stack in-house integration plus large-scale real-machine data from its global fleet—an asset cloud-only model vendors cannot replicate.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.


We, Frank Fan and Donnie Teng, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.
