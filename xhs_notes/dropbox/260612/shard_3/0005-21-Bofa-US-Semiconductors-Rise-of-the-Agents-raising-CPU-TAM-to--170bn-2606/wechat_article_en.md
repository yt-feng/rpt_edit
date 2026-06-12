# Agentic AI Is Not Taking from the GPU TAM—It Is Expanding the CPU Opportunity to $170 Billion

The central question for semiconductor investors over the next five years is not whether artificial intelligence will continue to drive data center spending, but which silicon architectures will capture the value as the nature of AI workloads fundamentally changes. The answer is more nuanced than the prevailing narrative that GPUs dominate everything. A new analysis from a leading global investment bank projects that the server CPU total addressable market will reach $170 billion by 2030, nearly five times its current size, driven by a single structural shift: the rise of agentic AI. This is not a story of CPUs stealing share from GPUs. It is a story of AI system complexity creating a new, parallel demand vector for general-purpose compute that did not meaningfully exist before.

The conventional view has been that AI compute is synonymous with accelerator compute. Training large language models and running inference at scale have been dominated by GPUs and other XPUs. But agentic AI—systems that plan, reason, retrieve information, use tools, and execute multi-step tasks autonomously—introduces a fundamentally different compute profile. These workloads are latency-sensitive, sequential, and I/O-intensive. They require orchestration, state management, and decision-making logic that accelerators are not designed to handle efficiently. The CPU, long dismissed as a commodity component in the AI era, is being reborn as the central orchestrator of autonomous systems.

This report examines the strategic implications of that rebirth. It identifies which companies are best positioned, where the unresolved analytical questions remain, and how investors should think about the distinction between TAM substitution and TAM expansion.


![Report chart 1](assets/source_image_01.jpg)

## The CPU Market Is Being Reorganized into Three Distinct Demand Pools, Each with Different Architecture Requirements

The traditional server CPU market, valued at roughly $30 billion in 2030 under this new model, represents the legacy base: on-premise deployments, multi-tenant cloud workloads, and general-purpose enterprise computing. This segment is mature, growing slowly, and dominated by x86 incumbents. It is not the source of the explosive growth.

The first new pool is the AI cluster compute node, or head node, segment. In large-scale AI training and inference clusters, CPUs serve as the control and management layer. They handle job scheduling, data management, user access, and the coordination of GPU accelerators. This segment is projected to reach $70 billion by 2030. These CPUs require high frequency and strong single-thread performance, but they do not need the highest core counts. They are the traffic controllers of the AI factory floor.

The second new pool is the agentic AI standalone node, also projected at $70 billion. These servers are dedicated to running autonomous agent loops. They require high core counts to manage parallel reasoning tasks, large memory bandwidth to maintain state and context, and tight integration with vector databases and external tools. This is where the CPU reclaims its role as the primary compute engine, not a supporting actor to accelerators.

The critical insight is that these three pools have different architectural requirements, different vendor dynamics, and different growth trajectories. A single CPU strategy will not capture all three. Incumbents that excel in traditional enterprise workloads may struggle to optimize for agentic orchestration. ARM challengers that are winning in hyperscale head nodes may not have the software ecosystem for traditional on-premise deployments. The market is fragmenting, and that fragmentation creates both opportunity and risk.


![Report chart 2](assets/source_image_02.jpg)

## ARM Is the Fastest Gainer, but the Market Share Story Is More Complex Than a Simple Shift from x86

By 2030, the analysis projects that ARM-based processors will account for roughly 50 percent of server CPU value share, split between merchant ARM chips at 36 percent and custom ARM designs at 15 percent. Intel and AMD are each expected to hold approximately 25 percent. This represents a dramatic shift from 2025, when Intel held 41 percent share and ARM merchant chips were just emerging.

The ARM merchant segment includes processors from NVIDIA, Qualcomm, and ARM's own designs. NVIDIA's Vera CPU, expected to ramp in the coming years, is particularly interesting because it blurs the line between CPU and accelerator vendor. NVIDIA is already the dominant player in AI accelerators, and its entry into the CPU market via ARM architecture positions it to offer the most tightly integrated full-stack solution for agentic workloads. The report notes that NVIDIA remains the top sector pick precisely because of this full-stack leadership, which includes CPU, GPU, and networking integration.

The ARM custom segment includes chips like AWS Graviton, Google Axion, and Microsoft Cobalt. These are designed by hyperscalers for their own data centers, optimized for their specific workloads. The growth of custom silicon is a double-edged sword for merchant vendors: it expands the overall ARM ecosystem and validates the architecture, but it also removes addressable revenue from the merchant market. The report projects that custom ARM CPUs will grow at a 91 percent CAGR through 2030, the fastest of any segment.

For Intel, the outlook is more complex. The report double-upgrades Intel to Buy, citing higher confidence in the company's ability to address industry constraints in leading-edge wafers and packaging, plus the larger agentic CPU TAM. The analysis sees Intel's earnings power reaching $6 or more by 2030, up from a prior estimate of $3 to $4. But Intel's value share is still projected to decline from 41 percent to 24 percent. The growth in absolute revenue is real, but the relative position erodes as the market expands faster than Intel can capture it.

For AMD, the report maintains a Buy rating with a raised price objective of $560. AMD is seen as the top CPU pick, benefiting from incumbency, a strong product pipeline, and an upcoming AI day expected to include the Venice launch. AMD's share is projected to remain stable at roughly 25 to 27 percent through 2030, neither gaining nor losing meaningfully. The question for AMD is whether it can maintain that stability as ARM competition intensifies in the high-growth agentic segment.


![Report chart 3](assets/source_image_03.jpg)

## The Report Leaves Unresolved Whether This TAM Expansion Is Durable or Whether It Represents Peak CPU

The most important analytical question that this report does not fully answer is whether the $170 billion CPU TAM is sustainable or whether it represents a cyclical peak driven by a specific technological inflection point. The report explicitly frames the key debate as TAM substitution versus TAM expansion, and it comes down firmly on the side of expansion. But expansion itself can be temporary if the underlying workload characteristics change again.

Consider the history of compute architecture in AI. The pendulum has swung from CPUs to GPUs to specialized accelerators to heterogeneous systems. Agentic AI may favor CPUs today, but what happens when the next generation of accelerators incorporates better support for sequential reasoning and state management? What happens if agentic workloads themselves evolve to become more parallelizable, reducing the CPU advantage? The report's model extends to 2030, which is a long time in semiconductor technology. Several architectural shifts could occur within that window.

There is also the question of whether the head node and agentic node segments are truly additive or whether they represent a temporary phase in the maturation of AI infrastructure. As AI clusters become more efficient, the ratio of CPUs to accelerators may decline. As agentic frameworks become more optimized, they may offload more work to specialized hardware. The report's model assumes that CPU demand scales with system complexity, but complexity may decrease as the technology matures.

Finally, the durability of the 30 percent-plus AI capex CAGR is itself a subject of debate. If enterprise AI adoption slows, if inference costs decline faster than expected, or if a new architectural paradigm emerges, the entire TAM could be revised downward. The report acknowledges this debate but does not resolve it. Investors should view the $170 billion figure as a plausible upper bound under current trends, not a certainty.

## Investors Need a Decision Framework Based on Three Variables: Workload Profile, Vendor Integration, and Silicon Strategy

For readers trying to translate this analysis into actionable decisions, three variables matter most.

First, workload profile. Not all AI workloads are agentic, and not all agentic workloads are equally CPU-intensive. Investors should distinguish between companies that are exposed to traditional cloud CPU demand, head node demand, and agentic node demand. The growth rates and competitive dynamics differ significantly across these segments. A company that dominates traditional on-premise CPUs may see stagnant growth even as the overall TAM expands.

Second, vendor integration. The most valuable positions in this market may belong to companies that can integrate CPU, GPU, and networking into a cohesive system. NVIDIA is the clearest example, but AMD is also building a more integrated portfolio. Intel's foundry ambitions add another dimension: if Intel can become a leading-edge manufacturer for other companies' CPU designs, it captures value even as its own CPU market share declines. The report flags Intel's foundry engagements as a supportive data point for the upgrade.

Third, silicon strategy. The merchant versus custom distinction is critical. Merchant vendors capture higher ASPs but face competition from hyperscalers who can design their own chips. Custom silicon vendors capture lower ASPs but have guaranteed demand and tighter integration with their own software stacks. The report projects that custom ARM CPUs will grow the fastest, but the absolute revenue is still smaller than the merchant segment. The question is whether hyperscalers will eventually bring enough of their CPU demand in-house to meaningfully reduce the merchant opportunity.

## The Full Report Contains the Detailed Market Share Model and Vendor-Level Projections That Support This Thesis

The analysis presented here is based on a comprehensive report that includes a full TAM model by vendor, by segment, and by year through 2030. It includes unit shipment projections, ASP trends, and value share breakdowns that allow readers to stress-test the assumptions. The report also contains detailed company analyses for each of the major CPU vendors, including the specific catalysts and risks that could change the outlook.

The most interesting unresolved question that the full report explores in greater depth is the role of NVIDIA's Vera CPU. The report suggests that Vera could serve both as a head node processor and as an agentic AI CPU, effectively splitting the opportunity roughly 50/50. If NVIDIA can leverage its GPU dominance to capture a significant share of the CPU market, it could become the dominant platform for agentic AI in a way that no single vendor has achieved in previous compute eras. But the report also flags that NVIDIA's CPU ASPs are assumed to be higher than the market average, which implies a premium positioning that may not be sustainable as competition intensifies.

Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
