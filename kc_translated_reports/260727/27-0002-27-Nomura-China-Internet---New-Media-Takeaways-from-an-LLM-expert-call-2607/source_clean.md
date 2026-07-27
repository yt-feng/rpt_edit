# China Internet & New Media
# Takeaways from an LLM expert call
## Key highlights

The NOM China internet team held a group call with an expert from a leading Chinese large language model (LLM) player. According to the expert, the next phase of competition among Chinese LLM developers will be shaped by three interrelated trends: continued model scaling, deeper model-harness integration and greater emphasis on system-level token economics. DeepSeek (unlisted) appears positioned at the intersection of these trends, according to the expert, seeking to narrow the capability gap with overseas frontier models while maintaining a structurally lower cost base and substantially lower token prices.

## Model scaling continues, but efficiency also matters

Chinese LLM are likely to move toward multi-trillion-parameter architectures, supported by larger compute clusters, supernodes, high-speed interconnects and optical networking. The expert views approximately 3tn parameters as the next practical milestone for Chinese LLMs.

However, pure parameter scaling is approaching diminishing returns. Beyond parameter scale, model competitiveness will increasingly depend on architectural and post-training efficiency, memory management, reliable tool use and long-horizon task performance.

## Model-harness integration strengthens the data flywheel

According to the expert, DeepSeek's decision to delay the official release of V4 partly reflects the need for further debugging and optimization at the agent-harness layer. Its goal is to build an integrated product comparable to Claude Code (developed by Anthropic [unlisted]) or Codex (developed by OpenAI [unlisted]), covering both professional software development and broader knowledge-work tasks.

Deeper model-harness integration could also create a proprietary data flywheel. Task trajectories, tool calls, user corrections, execution failures and real-world workflows can be converted into feedback for model and product improvement. Competitive advantage is therefore shifting from the standalone model toward the integrated model-agent system.

## DeepSeek's structural cost optimization supports its price leadership

DeepSeek positions itself as a price-performance leader. The expert estimates its blended inference cost at below CNY0.8 per million tokens, assuming a 60% cache-hit rate and excluding model-training compute, training-related personnel expenses and other R&D costs, versus a blended selling price of approximately CNY1.3 per million tokens. This implies an inference contribution gross margin of around 40%, despite a reported price reduction of approximately 75% for the V4 generation.

The expert attributes DeepSeek's cost advantage to more efficient attention and memory management, including KV-cache offloading to NVMe SSDs, as well as higher infrastructure utilization and large-scale deployment on domestic accelerators. DeepSeek is effectively using architectural and infrastructure optimization to lower its cost curve and pass part of the savings to customers through lower token prices.

## AI-in-the-loop is shortening model leadership cycles

According to the expert, the competitive lead of a single model generation has narrowed from approximately six months to three to four months. AI-in-the-loop is a major driver of this acceleration. Automated evaluation, LLM-as-a-Judge, multi-model scoring and teacher-model feedback are becoming more important than traditional manual annotation.

Therefore, looking ahead, sustainable differentiation of LLM players should therefore


China Internet & New Media


## Jialong Shi - NIHK


Bing Duan - NIHK


come from compute scale, proprietary user interactions and the ability to extract high-quality training signals automatically from real-world workflows.

DeepSeek's overseas growth is developer-led, complementing overseas frontier models

The expert estimates DeepSeek's ARR reached approximately USD520mn as of June 2026, with overseas markets contributing around $47 - 48\%$ . Overseas users are concentrated in Europe and the US, followed by Japan, South Korea and Australia. Adoption remains developer-led, with individual developers and small and medium-sized project teams representing the core customer base, while large-enterprise penetration remains relatively limited.

One emerging pattern is model layering. Developers may use Claude Code or Codex with premium overseas models for initial planning, architecture design and complex reasoning, before switching to DeepSeek for sustained code generation and execution. DeepSeek therefore does not need to replace frontier models across the entire workflow; it can initially capture the token-intensive execution layer, where usage is higher and price sensitivity is greater.

This complementary positioning could still pressure overseas model pricing, according to the expert, as users become more comfortable routing tasks between premium and lower-cost models. Premium pricing should remain defensible for tasks where reliability and completion quality outweigh cost, but good-enough, lower-cost models embedded in agent workflows could capture a disproportionate share of token volume.

## Open source is a distribution lever

According to the expert, although an open-source strategy weighs on direct commercialization, it could lower adoption barriers, expand overseas reach and facilitate deployment across multiple clouds and hardware platforms, and allow overseas customers to retain greater control over data, infrastructure and customization. Besides, at the industry level, capable open-source alternatives make it more difficult for closed-model providers to maintain high API premiums.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.
