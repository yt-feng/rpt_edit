# Agentic AI Will Reshape the Semiconductor Landscape by Making CPU and Memory the New Bottlenecks

The transition from generative AI to agentic AI represents a fundamental architectural shift that most observers are still underestimating. While generative AI focused on producing content through GPU-intensive inference, agentic AI requires autonomous systems that reason, plan, use tools, and execute multi-step workflows. This shift does not merely add more GPU demand—it fundamentally changes which components become constrained and where value accrues in the technology stack. According to a detailed analysis by a global research institution, agentic AI could create up to $238 billion in CPU opportunity and generate demand for 221 exabytes of DRAM by 2030 under a bull-case scenario. These numbers are not extrapolations of existing trends; they reflect a structural re-architecture of computing itself.

The critical insight is that the bottleneck is moving from GPU compute to CPU orchestration and memory capacity. In a generative AI workload, the GPU dominates because the task is single-threaded inference—generate text from a prompt. In an agentic workload, the system must call APIs, retrieve data from memory, execute code, verify results, and coordinate multiple sub-agents. Each of these steps requires CPU cycles, not GPU cycles. The report estimates that in a typical agentic workload, tool calls and actions can account for 50-70% of total compute demand, with the remaining 30-50% going to reasoning and inference. This means the CPU, long considered a mature and commoditized component, becomes a strategic bottleneck.

This matters now because the industry is at an inflection point. Hyperscaler capital expenditure is accelerating, and the 2Q26 capex cycle will be the telltale sign of whether infrastructure spending is translating into monetizable agentic applications. The memory cycle is also peaking, with DRAM contract prices expected to peak around 4Q26. Those who understand the architectural shift can position ahead of the market's realization that CPU and memory suppliers will capture disproportionate value in the agentic era.

![Report chart 1](assets/source_image_01.jpg)

## The CPU Becomes the Orchestrator, Not a Peripheral Component

The agentic AI architecture fundamentally redefines the role of the CPU from a supporting actor to the central orchestrator. In the three-pillar model described in the report, the GPU handles core model capabilities—reasoning, drafting, and understanding—while the CPU manages the control layer: routing work across tools, enforcing guardrails, managing workflows, and coordinating multi-agent systems. This is not a marginal change; it is a complete inversion of the compute hierarchy.

The report draws on research from Georgia Tech and Intel to illustrate this shift. In a generative AI workload, GPU compute dominates, with CPU usage primarily limited to data loading and basic coordination. In an agentic workload, the CPU becomes the primary compute consumer. Consider a simple agent task: a user asks an AI assistant to research a company, summarize its financials, check recent news, and draft an email. Each of these sub-tasks requires separate API calls, data retrieval from memory, code execution for analysis, and coordination of results. The GPU may only be invoked once for the final summary generation, while the CPU handles the entire orchestration pipeline.

The research implication is direct. Companies that design high-performance CPU architectures—whether through x86, ARM, or RISC-V—stand to benefit from a multi-year upgrade cycle driven by agentic workloads. The report identifies CPU exposure across the stack, including traditional server CPU suppliers and emerging ARM-based designs. The key metric to watch is not just core count but memory bandwidth and I/O throughput, as the CPU must manage increasingly complex data flows between memory, storage, and GPU accelerators.

![Report chart 2](assets/source_image_02.jpg)

## Memory Demand Shifts from Capacity to Bandwidth and Persistence

Agentic AI creates a fundamentally different memory demand profile than generative AI. Generative AI workloads are largely stateless—each inference is independent, and memory requirements scale with model size. Agentic workloads are stateful and context-dependent. An agent must maintain session memory, retrieve from a knowledge base, access portfolio data, and store intermediate results. This creates demand for both high-bandwidth memory (HBM) for GPU-accelerated inference and high-capacity DRAM for CPU-side memory pools.

The report quantifies this shift with striking numbers. Under the bull case, agentic AI could drive 221 exabytes of DRAM demand by 2030. To put this in context, total DRAM demand in 2025 is estimated at approximately 336 exabytes including HBM. This represents a structural acceleration in demand growth, not a cyclical uptick. The report projects HBM demand growing at a 134% CAGR from 2023 to 2027, reaching 56 exabytes by 2027. But this is only part of the story. Commodity DRAM demand for agentic workloads—used in CPU memory pools, caching layers, and session storage—will also grow significantly.

The memory cycle is currently in a supply-driven phase, with DRAM contract prices expected to peak in 4Q26. However, the report argues that this cycle is different from previous ones because of long-term agreements (LTAs). Traditional memory LTAs were short-term and flexible, with pricing frequently renegotiated. Current LTAs are 3-5 year commitments with pre-agreed volume allocations, pricing formulas, and sometimes prepayments or collateral. This structural change means memory companies have greater revenue visibility and margin protection, which could lead to a valuation re-rating.

The report uses Apple's stock performance from 2013-2025 as a playbook. Apple's buybacks and dividends drove approximately 70% of its excess compounded return versus the S&P proxy during that period. The logic is that memory companies with sustained free cash flow from LTA-backed revenue will be able to return more capital to shareholders, driving valuation expansion even as cyclical pricing peaks.

![Report chart 3](assets/source_image_03.jpg)

## The Memory Valuation Re-rating Depends on LTA Penetration, Not Just Pricing

The critical debate for memory observers is not whether prices will peak—they will, likely in 4Q26—but whether the structural shift to LTAs will sustain earnings and cash flow through the downcycle. The report provides a sensitivity analysis that quantifies the potential impact. For Samsung, if 70% of commodity DRAM revenue is covered by LTAs and those LTAs trade at 8x P/E, the implied group P/E rises to 7.1x. For SK Hynix, the same assumptions yield 7.2x. These are not dramatic re-ratings, but they represent a meaningful improvement over the historical pattern where memory companies trade at 4-6x P/E during downcycles.

The report contrasts this with the analog case study during COVID, where LTAs were renegotiated and forced inventory accumulation occurred. The current LTA frameworks are structurally different: they involve prepayments, financial guarantees, and multi-year volume commitments. This reduces the risk of a sharp earnings collapse when pricing turns. The market is currently pricing memory earnings rationally, not euphorically, which means there is room for multiple expansion if LTAs prove sticky.

The key variable to monitor is the penetration rate of LTAs across the commodity DRAM market. If hyperscalers and enterprise customers continue to lock in supply agreements, memory companies will generate sustained free cash flow even as spot prices decline. This would support higher dividend payouts and share buybacks, following the Apple playbook. The report also cites Japanese shipping companies as another example, where enhanced dividend payout ratios after COVID led to sustained outperformance.

## HBM Supply Constraints Will Persist Through 2027, Creating Pricing Power for Incumbents

The report provides detailed HBM sufficiency estimates that reveal a persistent supply-demand imbalance. In 2026, total HBM demand is estimated at 34.2 exabytes, while total supply is estimated at 35.0 exabytes, implying a sufficiency ratio of just 2.5%. By 2027, demand reaches 56.1 exabytes against supply of 53.8 exabytes, a deficit of 4%. This is despite aggressive capacity expansion from Samsung, SK Hynix, and Micron.

The sufficiency estimates incorporate yield rate assumptions that are conservative by design. Samsung's yield is assumed to improve from 50% in 2024 to 70% in 2027, while SK Hynix improves from 60% to 70%. Utilization rates are also assumed to be high, with SK Hynix and Micron at 100% throughout. Even with these optimistic assumptions, the market remains tight. The implication is that HBM pricing will remain elevated, and incumbent suppliers will maintain pricing power.

This has second-order implications for the broader memory ecosystem. Tight HBM supply means GPU suppliers like NVIDIA will prioritize allocation for their highest-margin products, potentially constraining supply for lower-end AI accelerators. It also means that memory suppliers with strong HBM exposure—particularly SK Hynix, which the report identifies as having the highest HBM revenue concentration—will benefit disproportionately.

## The Decision Framework: Three Questions Every Observer Should Ask

The report's analysis translates into a straightforward decision framework for those evaluating exposure to the agentic AI theme. There are three questions to answer.

First, where is the bottleneck moving? The answer is clear: from GPU compute to CPU orchestration and memory capacity. Observers should assess their portfolios for exposure to CPU architecture companies, memory suppliers with strong LTA coverage, and the enabling components—MLCCs, substrates, and sockets—that support higher CPU and memory content.

Second, is the memory cycle different this time? The evidence suggests yes, but only for companies with significant LTA penetration. The report's sensitivity analysis shows that the valuation re-rating depends on LTA adoption rates, not on cyclical pricing. Observers should focus on memory companies that have signed multi-year agreements with hyperscalers, as these will sustain cash flow through the pricing peak.

Third, what is the time horizon for agentic AI adoption? The report estimates that agentic AI could add $238 billion in CPU opportunity by 2030, but this is a bull-case scenario. The actual adoption curve depends on enterprise deployment of agentic applications, which in turn depends on the availability of orchestration software and memory infrastructure. The 2Q26 capex cycle will be the first major data point to validate or challenge the bull case.

## The Infrastructure Stack Is Shifting from Hardware to Applications, But the Transition Takes Time

The report presents an AI research stack that shows value moving from hardware to applications over time. In the current phase, hardware captures the majority of value—GPUs, memory, and networking. As agentic AI matures, the value shifts to orchestration layers, middleware, and applications. This is a familiar pattern from previous technology cycles, where infrastructure commoditizes and applications differentiate.

However, the transition is not immediate. The report estimates that hardware will continue to capture the majority of AI-related spending through 2027, driven by hyperscaler capex and memory LTAs. The application layer will become more significant after 2028, as agentic workflows become standardized and enterprise adoption scales.

The practical implication is that observers should not rotate out of hardware prematurely. The CPU and memory opportunity from agentic AI is front-loaded, driven by the need to build out the orchestration and memory infrastructure before applications can scale. The report's exposure list spans the entire stack—from CPU and memory suppliers to PCB manufacturers, MLCC producers, and ODM assemblers. Each component will benefit differently, but the common theme is that agentic AI increases component intensity per server.

The most overlooked opportunity may be in the enabling components. MLCCs, CPU sockets, and substrates are not typically associated with AI, but the report identifies them as critical beneficiaries. Higher CPU content means more MLCCs per server. Higher memory bandwidth means more advanced substrates. The report's exposure list includes Murata, TDK, and Yageo for MLCCs, and SEMCO and Unimicron for substrates. These are not high-growth names in isolation, but within the agentic AI context, they offer derivative exposure with lower valuation risk than the primary CPU and memory suppliers.

*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not professional advice.*

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not professional advice.</p>
