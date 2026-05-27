# The AI Infrastructure Narrative Is Shifting from GPU Clusters to Composable AI Factories, and Computex 2026 Will Prove It

The next phase of artificial intelligence infrastructure will not be defined by how many GPUs a company can procure. It will be defined by how well it can orchestrate compute, memory, networking, cooling, and power delivery as a single, integrated system. This is the central thesis emerging from the latest research on the upcoming Computex 2026 and GTC Taipei events, and it represents a fundamental break from the previous investment cycle.

For the past two years, investor attention has been narrowly fixated on GPU shipments, high-bandwidth memory capacity, CoWoS packaging constraints, and the physical delivery of rack-scale systems like the Blackwell NVL72. Those were the bottlenecks of an era when scaling meant adding more accelerators. That era is ending. The data center is no longer a collection of servers; it is becoming a single, composable machine—an AI factory—where every subsystem must be jointly optimized.

The implications for the supply chain are profound. Taiwan's technology ecosystem, long valued for its single-component manufacturing prowess, will now be judged by its ability to deliver complete AI systems. The companies that can integrate racks, power shelves, liquid cooling loops, optical interconnects, and telemetry controllers will capture disproportionate value. Those that remain component suppliers risk being commoditized. This article unpacks the architectural transition, the emerging bottlenecks, and the strategic questions that every investor in the AI supply chain must now answer.


![Report chart 1](assets/source_image_01.jpg)

## The Rack Is No Longer a Server Cabinet; It Is a Modular Block in a Pod-Scale Compute Domain

The most consequential architectural shift on display at Computex 2026 will be the move from server-level design to rack-level and ultimately pod-level design. This is not an incremental improvement. It is a change in the fundamental unit of system architecture.

Blackwell GB200 NVL72 was the first major step in this direction, turning the rack itself into the system boundary. Rubin takes this logic much further. Based on NVIDIA's previous announcements, the company is now defining several distinct rack categories: GPU racks for compute acceleration, Vera CPU racks for agentic AI orchestration, LPU racks for specialized inference, CMX context-memory racks for expanded memory hierarchy, Spectrum networking racks for scale-out fabric, power racks for high-voltage delivery, and cooling infrastructure racks for liquid thermal management.

This is no longer a conventional server deployment model. It is a composable AI factory model, where each rack type serves a specific function within a larger, coordinated system. The GPU rack remains the compute anchor, but it is no longer the entire story. Rubin NVL72 and Rubin Ultra NVL144/NVL576 extend the same logic as the GB system, but at far higher power density and network complexity. The Vera Rubin Ultra NVL576, for example, combines eight separate MGX NVL racks, each with 72 Rubin Ultra GPUs, into a single 576-GPU NVLink domain using copper and direct optical connections.

The strategic implication is clear: the "rack" is becoming only one module inside a larger pod-scale compute domain. Investors who track only GPU shipments will miss the expanding opportunity in every other rack category. The value is shifting from the chip to the system, and from the system to the orchestration layer that ties it all together.


![Report chart 2](assets/source_image_02.jpg)

## Vera CPU Signals That AI Orchestration, Not Just Acceleration, Is Becoming a Hardware Bottleneck

Perhaps the most underappreciated theme at Computex 2026 will be NVIDIA's CPU strategy. Vera CPU is not designed to take on Intel and AMD in the general-purpose server market. Instead, it is purpose-built to control the AI factory orchestration layer.

In agentic AI, the CPU workload extends far beyond feeding GPUs. It includes request scheduling, agent workflow control, tool-call coordination, memory indexing, retrieval management, simulation, networking control, and system telemetry. The CPU becomes the "traffic controller" for AI factories. As inference workloads become longer, more persistent, and more interactive, CPU-side memory bandwidth and capacity matter more, not less.

The SOCAMM design is critical here. It gives Vera a denser, lower-power, high-bandwidth memory architecture that is likely better suited for AI orchestration than conventional DIMM-heavy server designs. With production preparation of approximately 2 million units expected in 2026, Vera CPU represents a meaningful new demand vector for the supply chain. It raises content opportunities in sockets, thermal modules, BMC controllers, and memory interfaces.

The strategic question is whether Vera cannibalizes or complements GPU demand. The evidence suggests the latter. As AI inference becomes more agentic and CPU-intensive, CPU demand expands alongside GPU demand. The two are becoming complementary rather than substitutive. Investors should watch for Vera rack demonstrations from major ODMs, as these will signal how quickly the ecosystem is adapting to a CPU-driven orchestration layer.


![Report chart 3](assets/source_image_03.jpg)

## Networking and Co-Packaged Optics Reveal That Data Movement, Not Compute, Is Becoming the Binding Constraint

As AI systems scale from single racks to pods, the bottleneck shifts from chip compute to data movement. This is the second major theme that Computex 2026 will validate.

NVIDIA's Spectrum-X roadmap points toward Ethernet becoming a specialized AI fabric rather than a generic data center network. Hyperscalers prefer Ethernet economics and operational familiarity, but AI requires much tighter congestion control, telemetry, routing, and workload-aware optimization. The networking rack is becoming as strategic as the compute rack.

Co-packaged optics will be one of the most debated topics at the show. For Rubin Ultra, CPO becomes more important because the physical scale of NVL576 exceeds what copper can handle efficiently. The practical adoption curve is likely phased: pluggable optics and linear-pluggable optics in 2025-2026, switch-side CPO and direct optical links in 2026-2027, and broader optical scale-up fabrics after Rubin Ultra.

The supply chain implications are significant. Optical engines, silicon photonics PICs, fiber array units, active alignment equipment, optical connectors, fiber management, and liquid-compatible photonic packaging all become more important. However, the mapping between fiber array units and optical engines is not mechanically one-to-one. One optical engine usually requires a fiber attach interface, but the mapping depends on transmit/receive layout, lane count, wavelength-division multiplexing architecture, and whether fibers are shared, split, or aggregated.

This creates a complex and non-linear opportunity set. Investors accustomed to simple unit-drive models will need to think in terms of system-level bandwidth requirements and the specific optical architectures that hyperscalers adopt. The report does not fully resolve which CPO architecture will dominate, leaving a meaningful analytical gap for those who want to position ahead of the adoption curve.

## Cooling and Power Delivery Are Becoming the Practical Deployment Constraints for Rubin-Class Systems

The most tangible bottleneck for Rubin deployment may not be silicon at all. It is the electrical and thermal infrastructure required to support it.

Rubin NVL72 rack estimates point toward 180 to 220 kilowatts of thermal design power. For context, Hopper racks operated around 40 to 60 kilowatts with air or hybrid cooling. Blackwell NVL72 pushed into the 120 to 180 kilowatt range, making direct liquid cooling standard. Rubin pushes beyond 200 kilowatts, and Rubin Ultra may move toward several hundred kilowatts per pod.

Power delivery is simultaneously shifting. At 54 volts, a 216-kilowatt rack implies approximately 4,000 amps of current, which becomes difficult to manage in copper, busbars, connectors, and thermal systems. This explains why NVIDIA is pushing toward 800-volt DC architecture, power racks, 110-kilowatt power shelves, battery backup unit support, and DC data center architecture.

The future rack is not just a server cabinet. It is an electrical-thermal machine requiring coordinated power conversion, backup energy, liquid flow, telemetry, and safety systems. Companies that can deliver integrated power and cooling solutions—power shelves, busbars, cooling distribution units, manifolds, quick disconnects, and sensors—are becoming system-level players, not just component suppliers.

The report provides a useful framework for tracking this transition across generations. Hopper used traditional AC power supplies and air cooling. Blackwell introduced rack power shelves and emerging busbar architectures. Rubin is pushing 54-volt busbars to their practical limits, and Rubin Ultra will likely necessitate an 800-volt DC transition. Each step creates new opportunities and new risks for the supply chain.

## What the Report Leaves Unanswered: The Open Questions That Define the Next Investment Cycle

For all its analytical rigor, the report leaves several meaningful questions unresolved. These are not weaknesses in the analysis; they are the natural boundaries of any forward-looking research. They are also the questions that will separate informed investors from those who simply extrapolate past trends.

First, the Vera CPU production estimate of 2 million units in 2026 is significant, but it does not specify how this volume maps to revenue, margin, or supply chain value capture. Is Vera a high-margin, low-volume product for hyperscaler deployments, or will it penetrate enterprise markets? The answer determines which suppliers benefit most.

Second, the CPO adoption curve is described as phased, but the timing and volume of each phase remain uncertain. Will hyperscalers adopt switch-side CPO aggressively in 2026, or will they wait for broader optical scale-up fabrics after Rubin Ultra? The difference of one year in adoption timing can dramatically alter the revenue trajectories for optical component suppliers.

Third, the power architecture transition to 800-volt DC is described as increasingly necessary, but the report does not specify the timeline or the technical hurdles. How quickly can data centers retrofit existing facilities? What are the safety and regulatory implications? These questions matter for investors evaluating power equipment suppliers.

Fourth, the report identifies multiple rack categories but does not quantify the relative value of each. Is the GPU rack still the largest value pool, or do power racks and cooling infrastructure capture a growing share? The answer determines where investors should focus their attention.

These open questions are not gaps. They are invitations for deeper analysis. The full report contains the charts and data that allow investors to build their own scenarios.

## A Decision Framework for the AI Factory Era

For investors trying to navigate this transition, the report implies a clear but demanding framework. The old framework asked: Which company has the most GPU exposure? The new framework requires answering three questions in sequence.

First, which architectural layer is becoming the binding constraint? In 2024, it was CoWoS capacity and HBM supply. In 2025, it was Blackwell rack delivery. In 2026 and beyond, the binding constraints are likely to be networking bandwidth, power delivery capacity, and cooling infrastructure. Each constraint creates a temporary pricing advantage for suppliers in that layer.

Second, which companies are moving from component supply to system integration? The value chain is compressing. Companies that can deliver complete rack solutions, integrated power and cooling systems, or end-to-end networking fabric will capture a larger share of total system value. Companies that remain single-component suppliers face margin pressure as their products become standardized.

Third, what is the adoption timeline for each architectural innovation? Vera CPU adoption, CPO penetration, and 800-volt DC deployment all have different S-curves. Getting the timing right matters more than getting the direction right. Early adoption creates pricing power; late adoption creates volume but lower margins.

This framework does not provide easy answers. It provides the structure for asking better questions. The full report provides the data to answer them.

## Join the Community to Read the Full Report and Review the Original Charts

This article has synthesized the strategic argument underlying the Computex 2026 preview. But the full report contains the detailed charts, power and cooling comparison tables, rack configuration breakdowns, and supply chain mapping that allow investors to build their own conviction. The original analysis from Citi includes specific ODM demonstrations, power density projections across generations, and the analyst certification that underpins the research. To access the complete document and the supporting data, join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
