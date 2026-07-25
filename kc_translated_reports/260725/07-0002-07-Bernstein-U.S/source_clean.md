# Advanced Micro Devices (AMD): Key takeaways from the Advancing AI Event

AMD held its Advancing AI event from July 22-23, culminating in a keynote by CEO Dr. Lisa Su and investor Q&A. We thought the event was generally quite positive with key announcements around new customer partnerships, updates on the product portfolio and roadmap, increased TAM outlooks. We summarize the main announcements below.

Helios (MI450) officially launched with (unsurprisingly) strong performance benchmarks, both vs. Vera Rubin and vs. MI350 (though as always with this sort of thing we take them with a grain of salt) (Exhibit 1, Exhibit 2). An updated Helios roadmap was also provided with an annual release cadence of successive rack-scale systems with MI500/MI600 series expected to launch in 2027 and 2028, respectively (Exhibit 3). The near-term MI455X ramp is still expected to start in 3Q and ramping into 4Q of this year.

AMD announced Anthropic as a third major customer for its Helios architecture, joining OpenAI and Meta. As part of the strategic partnership with Anthropic, AMD will invest up to \$5B (so no warrants) and the companies will collaborate on ROCm. Anthropic will deploy up to 2GW of compute, with deployment of the first $1^{st}$ GW starting in 1H27 with the goal of deploying almost the full 1GW in 2027. AMD also announced a partnership with Microsoft to deploy Helios at scale on Azure, although not providing specific targets.

CPU 2030 TAM raised to \$220B vs the prior \$120B they provided only 3 months ago (Exhibit 4), implying an >50% CAGR from \$26B in 2025, with the vast majority of growth driven by agentic AI. They also see the Accelerator TAM growing to \$1.4T by 2030 (\~45% CAGR from \$200B in 2025) mainly driven by inference spend with the overall compute TAM growing to \~\$2T (\~40% CAGR from \$365B in 2025).

Management provided color on its CPU product roadmap. AMD's CPU portfolio of next gen Venice CPUs addresses varying requirements via several Venice variants tailored to GPU servers / host nodes (Venice HF/Verano), Agentic CPU servers (high core count, high ASP Venice 256c) and general purpose CPU servers (Venice SP7/SP8/Venice-X) (Exhibit 5). Management remains confident that AMD's CPU portfolio is strong and believes that a favorable competitive position vs. both x86 and Arm-based CPUs will help them to gain further market share.

Cerebras and AMD announced a partnership for ultra-low latency inference. As inference workloads are becoming more heterogeneous with customer requirements varying widely across latency, throughput, token capacity, cost and scale, the AMD-Cerebras partnership seeks to combine the throughput from AMD Instinct GPUs, with ultra-fast token generation capabilities of Cerebras (Exhibit 6, Exhibit 7). This announcement is perhaps unsurprising given that NVDA is taking a similar (although likely more integrated) approach with Groq. While sparse on technical details, Cerebras plans to deploy the first joint solution in its own data center and making it available to customers initially via Cerebras Cloud in 2H26.


AMD introduced ROCm.AI, an AI-driven development platform that aims to speed up development and workload-specific GPU performance optimization and programming via AI (and which they seem to view as their answer to the NVIDIA CUDA moat; we shall see...) The solution draws on the core ROCm software stack of compilers, libraries and frameworks and has integrations with AI coding agents which can use expert skills to help generate code to optimize GPU performance (Exhibit 8).

AMD also announced a host of smaller offerings in Enterprise, Personal and Physical AI. AMD announced new products addressing several challenges in enterprise AI deployment including power & cooling, cost and ease of deployment for the enterprise with its Instinct 350P GPU which it positions as a cost-effective, easy-to-deploy solution for on-prem datacenters for non-frontier workloads. Other new products include personal AI compute solutions which can run model sizes from 24B to 200B parameters (Ryzen AI400, Ryzen AI Max) as well as a new developer-oriented platform (Gorgon Halo). Lastly, AMD introduced KRIA AI Robotics, a turnkey robotics developer platform.

Overall we found the event to be quite positive, and continue to see fundamental strength with the company benefitting from fundamental upside in both CPU and GPU trajectories. We rate AMD Outperform, \$600 PT.

## BERNSTEIN TICKER TABLE


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

AMD (OP, \$600): Expectations remain high, but exposure to AI demand driving both a CPU and GPU story can provide substantial growth.

## DETAILS

EXHIBIT 1: AMD's benchmarks showed strong performance vs. Vera Rubin (although we typically take these sorts of things with a grain of salt)...

## AMD Helios Delivers The Most Powerful Rackscale AI Infrastructure


[[KC_IMAGE_001]]

Source: AMD

EXHIBIT 2: ... and vs. MI355, particularly in low-latency use cases

## Instinct MI455X Delivers Generational Increase In Inference Throughput


[[KC_IMAGE_002]]

Source: AMD

EXHIBIT 3: AMD targets an annual release cadence for its rack-scale GPUs

[[KC_IMAGE_003]]

Source: AMD

EXHIBIT 4: AMD raised its CPU TAM to \$220B in 2030 from \$120B not too long ago

[[KC_IMAGE_004]]

Source: AMD

EXHIBIT 5: AMD's latest generation Venice CPU will be offered in several variants catering to a GPU server, agentic and general purpose workloads


EPYC "Venice" The Best Server CPU Portfolio

GPU SERVERS "HOST NODE"

AGENT CPU SERVERS "SANBOXES"


"Venice" HF RDIMM / MRDIMM

"Venice" 256c

"Venice" SP7

"Venice" SP8

"Venice-X"

"Verano"
LPDDR

High Frequency CPU to GPU Bandwidth

High Core Count Low Power


Balanced Performance & Power

Technical Compute & HPC

Source: AMD

EXHIBIT 6: The AMD - Cerebras offering seeks to combine high-throughput with ultra-low latency...

## The Most Powerful Solution For Ultra Low Latency Inference


Wafer-scale, Ultra Low Latency Engine

432 GB HBM4 Capacity

23.3 TB/s Memory Bandwidth

44 GB on-chip SRAM

72 GPU Domain

21,000 TB/s Memory Bandwidth

900,000 AI Cores

Source: AMD

## EXHIBIT 7: ... offering higher TPS/W across a wide latency band

## AMD × cerebras Ultra-Fast Inference, Higher TPS/W on Leading AI Models

THROUGHPUT PER WATT (tokens/s/W)

Up to 5x TPS/kW

Helios + Cerebras

Cerebras

INTERACTIVITY (TOKENS / SECOND / USER) Kimi 2.6 1T Model

Source: AMD

EXHIBIT 8: ROCm.AI optimizes GPU performance across both training and inference workloads

## Accelerating Inference with ROCm.AI

Parallelization & Scheduling
Expert parallelism, DP-attention,
Compute communications overlap

INFERENCE

Paged attention, KV cache quantization,
Unified attention (prefill + decode)

3.3x

average performance improvement

MHA prefill, MLA decode, Block-scale fused MoE

DeepSeek-R1 GLM-5 Kimi-K2.5 ROCm.AI vs ROCm 7

Source: AMD

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 9: Bernstein AMD Income Statement


## Source: Company reports, Bernstein estimates and analysis

EXHIBIT 10: Bernstein AMD Balance Sheet and Cash Flow Statement


## Source: Company reports, Bernstein estimates and analysis
