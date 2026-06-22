# Memory Is Becoming the Next Cost Bottleneck in AI — and That Changes the Investment Logic

The artificial intelligence industry has spent the last two years fixated on GPU supply constraints. The dominant narrative has been simple: more compute, more scale, more spending. But a less visible, more structural pressure is now building beneath the surface. Memory — specifically high-bandwidth memory (HBM) — is becoming a binding constraint on AI economics, and the implications are far more complex than a simple price increase.

The core insight from our latest analysis is this: memory has shifted from being a passive input to an active variable in the AI cost equation. And the mechanism through which this cost propagates is not linear. Because HBM is embedded inside GPU/XPU systems, its price increase gets amplified by the gross margin structure of accelerator suppliers. The result is a compounding cost burden on hyperscalers that is roughly 30% higher than the raw memory price hike alone would suggest. This is not a transient pricing cycle. It is a structural recalibration that will reshape profit pools, supplier relationships, and investment returns across the AI value chain.

The conventional wisdom has been that memory suppliers are passive beneficiaries of AI demand. That view is now outdated. Memory suppliers are in a position to demand higher prices — but they face a strategic trade-off between short-term profit maximization and the long-term health of the AI ecosystem. How they resolve this tension will determine which companies win and which get squeezed.


![Report chart 1](assets/source_image_01.jpg)

## HBM Prices Must Rise Sharply Because Conventional DRAM Now Generates Nearly 3x the Gross Profit Per Wafer

The most immediate driver of HBM price increases is not demand. It is relative profitability. Since the third quarter of 2025, conventional DRAM prices have risen approximately 4.5x. HBM prices, locked into annual contracts, have not moved. The result is a glaring divergence in wafer-level economics.

Our analysis shows that deploying capacity to conventional DRAM today generates over 2x the revenue and nearly 3x the gross profit per wafer compared to HBM. This is not a marginal difference. It is a structural incentive for memory suppliers to allocate capacity away from HBM and toward conventional DRAM. Both Samsung and Micron have already confirmed in their earnings calls that conventional DRAM margins have pulled ahead of HBM margins. As conventional DRAM prices continue to climb, this gap widens further.

The implication is straightforward: memory suppliers will not accept this profit asymmetry indefinitely. They will demand significantly higher HBM prices in the next contract cycle — our estimate is 2 to 2.5x year-over-year — to narrow the margin gap. But here is the strategic nuance. A full 3x increase would be required to equalize revenue per wafer. We model a less aggressive increase because memory suppliers recognize that excessively high HBM costs could damage the AI ecosystem on which their long-term demand depends. SK hynix has explicitly stated it will pursue "optimal allocation between HBM and general DRAM," not revenue maximization.

This creates a fascinating tension. Memory suppliers have pricing power, but they also have a vested interest in not overusing it. The final negotiated price will reflect not just supply-demand dynamics, but a strategic judgment about how much cost the AI value chain can absorb without triggering a demand slowdown.


![Report chart 2](assets/source_image_02.jpg)

## The GPU Markup Mechanism Amplifies the HBM Cost Burden by 4x for Hyperscalers

This is the most underappreciated dynamic in the memory debate. HBM is not sold directly to hyperscalers as a standalone component. It is packaged inside GPUs and XPUs, becoming part of the cost of goods sold for accelerator suppliers like NVIDIA. When the cost of HBM rises, it does not simply pass through to customers. It interacts with the accelerator supplier's gross margin target.

Consider the math. If HBM represents 5% of a server rack's selling price, and HBM costs increase by a certain amount, the accelerator supplier faces a choice. It can pass through the cost increase dollar-for-dollar, but that would compress its gross margin percentage. Alternatively, it can raise the rack price by a multiple of the cost increase to defend its gross margin. Assuming a 75% gross margin target, the required price increase is approximately 4x the HBM cost increase.

Our analysis of a representative high-end rack configuration shows that the raw HBM price increase alone would require a 6% rack price increase. But with the markup mechanism, the rack price increase jumps to 24%. When combined with higher conventional DRAM and NAND costs — which hyperscalers often source directly and therefore avoid the markup — the total data center capex increase reaches approximately 30%.

This is not a theoretical exercise. It is a real negotiation pressure that is happening now. Hyperscalers are confronting a fundamental question: should they accept the amplified cost, or should they restructure their procurement to avoid it? The answer to that question will reshape competitive dynamics across the supply chain.


![Report chart 3](assets/source_image_03.jpg)

## Hyperscalers Will Seek to Recalibrate Costs, Potentially Benefiting ASIC Suppliers Like MediaTek

The 30% capex increase is not a deal-breaker for AI investment. Hyperscalers face competitive pressure to deploy AI infrastructure, and funding remains available. But it does force a recalibration. The ROI analysis that justified the original investment plan must now be re-run with a significantly higher "I."

This recalibration can take several forms. Hyperscalers may adjust their mix of server configurations, substituting CPU-only nodes or alternative accelerators for GPU-heavy racks. They may negotiate harder on token pricing with their cloud customers to pass through some of the cost. And most importantly, they may seek to source HBM directly from memory suppliers, bypassing the GPU markup entirely.

This last option is where the strategic opportunity lies. If hyperscalers can procure HBM directly, they eliminate the 4x markup amplification. But this requires an integration partner that can combine the memory with logic dies, packaging, and system software. Asian ASIC design service providers are well positioned to fill this role. MediaTek, which has demonstrated solid execution on its first and second TPU projects, is a direct beneficiary of this trend. Our supply chain checks suggest upside risk to our 2028 projections for the company.

The key question that remains unanswered is whether GPU suppliers will resist this unbundling by arguing that HBM integration is inseparable from their system value. They will claim that the markup is not on HBM specifically, but on the entire integrated solution. This debate is not yet resolved, and its outcome will determine whether the current GPU-centric architecture persists or gives way to a more modular, hyperscaler-controlled approach.

## What the Report Does Not Fully Answer: The Second-Order Effects on AI Demand Elasticity

Our analysis focuses on the supply side — the cost structure, the markup mechanism, and the profit redistribution. But the most consequential question is on the demand side. How elastic is hyperscaler AI investment to a 30% cost increase?

The report does not provide a definitive answer, and for good reason. The elasticity depends on the returns hyperscalers generate from AI deployments, which vary significantly by use case, customer segment, and competitive dynamics. In a scenario where AI token prices remain high and demand outstrips supply, the cost increase may be absorbed without slowing investment. In a scenario where token prices are under pressure and ROI is marginal, the cost increase could trigger a meaningful slowdown.

This uncertainty creates a critical analytical gap. The memory price increases we project are based on supplier behavior and contract negotiations. But the ultimate ceiling on those prices is set by hyperscaler willingness to pay, which itself depends on the revenue they can generate from AI. If hyperscalers push back aggressively — either by reducing orders or by investing in alternative architectures — the expected HBM price increase may not materialize in full.

Investors should watch for early signals. The pace of hyperscaler capital expenditure guidance, the evolution of AI token pricing, and the degree of vertical integration by major cloud providers will all provide clues about whether the current cost structure is sustainable.

## A Decision Framework for Investors: Three Questions to Determine Positioning

Given the complexity of the dynamics at play, investors need a clear framework to evaluate opportunities across the memory and AI value chain. We propose three diagnostic questions.

First, does the company have exposure to HBM pricing leverage? Samsung, SK hynix, and Micron will benefit from the upward earnings revision that follows HBM contract negotiations. Our forecasts for fiscal year 2027 earnings per share are 25 to 40 percent above consensus, driven by higher HBM price assumptions. As negotiations conclude in the coming months, we expect consensus to move upward, providing support for these stocks. Pure NAND suppliers like KIOXIA lack this catalyst entirely.

Second, does the company benefit from hyperscaler efforts to avoid the GPU markup? This is the MediaTek thesis. Companies that enable direct HBM sourcing or provide ASIC design services for hyperscaler-controlled architectures are positioned to capture value from the recalibration. The key risk is execution and the pace at which hyperscalers shift away from bundled GPU solutions.

Third, does the company have exposure to the conventional DRAM cycle? Conventional DRAM prices have risen 4.5x and may increase another 25 percent before peaking. Memory suppliers with higher conventional DRAM exposure relative to HBM may generate superior near-term profitability. Samsung, which leads in HBM4 technology but has indicated a focus on profit margins, may choose to allocate capacity to conventional DRAM even at the expense of HBM market share. This is a strategic choice that investors should monitor.

The framework is not static. As HBM prices adjust and the markup debate resolves, the relative attractiveness of these positions will shift. The current moment favors companies with HBM pricing leverage and those positioned to benefit from structural recalibration. The risk is that the cost burden slows AI investment, which would pressure the entire value chain.

## Join the Community to Read the Full Report and Review the Original Charts

The analysis presented here is a synthesis of a detailed research report that includes proprietary models for HBM, DRAM, NAND, and individual company forecasts. The full report contains the exhibits referenced in this article, including the wafer-level profitability comparisons, the capex impact analysis, and the market share projections across HBM generations. It also includes the complete valuation framework and price target methodology for each covered company.

The most important analytical work lies in the numbers that underpin the argument. The interaction between HBM pricing, GPU markup, and hyperscaler capex is a multi-variable problem that cannot be fully captured in a single article. The original charts reveal the sensitivity of the conclusions to changes in key assumptions — particularly the degree of markup and the mix of direct versus bundled HBM procurement.

For investors who want to test the logic against their own assumptions, the full report and models are essential. Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
