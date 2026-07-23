# The Case for Memory, and why “open-source” expands TAM
## Chinese Open LLMs are no threat to memory demand

Latest releases in open-source models, including China's Kimi K3 launched July 16, reinforce our bullish thesis on memory/MU. From a high level, we view the aggressive Chinese open-model API pricing (up to 5-350x cheaper than Western models) as reflective of business-model choices, not necessarily reflective of hardware costs. Importantly, these models, using various efficiency techniques (more below), are able to reduce compute/GPU intensity, but require the same or more memory as their model weights and active parameters increase. We also flag that every open-weight download also creates a new customer-side memory socket that wouldn't exist in a closed-model setting.

## Chinese models charge less, but still require same memory

Chinese open-model API pricing is aggressive, with Tencent Hunyuan at \$0.06/mn input vs. Claude Opus 4.8 at \$15/mn, and even Moonshot AI's latest Kimi K3 charging only \$3/mn despite 'similar' performance. However, we flag API price is a business-model choice, not necessarily a hardware-cost read-through. For instance, Kimi K3 still requires \~1.4 TB of HBM per serving instance to run. This is similar to OpenAI's 'oss-120b' open model with the same MXFP4 native precision (for like-for-like compression) with 120B total parameters (23x smaller than Kimi K3) requiring \~63GB of weight memory to run (22x smaller). In other words, often times API pricing actually scales with total memory weight and active parameters, even for open Chinese LLMs. "Open" refers to weight distribution, not deployment cost, and customers still need to purchase HBM, DRAM, NAND to run the model on their own hardware.

## Efficiency techniques, subsidies likely help lower pricing

Where Chinese models do have pricing/cost advantage is often not hardware-related. We estimate Chinese cost advantage in architectural efficiency (MoE sparsity, MLA/hybrid attention, native FP8/MXFP4 quantization, as well as up to 1.5-2x advantage in physical infra efficiency (lower Chinese electricity, labor, and land costs). Rest of the pricing differential could come from state-linked capital subsidies and cloud revenue/FCF at Chinese CSPs (Alibaba, Tencent, Baidu). Interestingly, Moonshot's Kimi K3 paused new subscriptions within just 48 hours of K3's launch, likely as GPU capacity ran out (or to cut costs/losses), and Xiaomi in May 2026 cut its MiMo model pricing by $99\%$ (likely unprofitable), likely as an effort to grab market share.

## CXMT not a threat, reit. MU Buy ahead of buyback resume

We reiterate Buy on MU with \$1,550 PO. While China-based CXMT is aggressively expanding capacity (now low-10% of global wafer capacity), we view limited competition in AI memory. CXMT primarily addresses the underserved consumer/commodity DRAM segment, not HBM3E/HBM4. It also remains unclear whether US OEMs will receive gov't approval to source from CXMT any time soon. Critically, MU's CHIPS Act buyback restrictions expire around Dec-26 (two years after the first funding tranche received Dec-24), opening the door to large-scale repurchases – given its \$120-130bn/yr+ FCF outlook over the next few years. A 40% payout policy would result in \~\$50-60bn/yr of buybacks, or \~5-6% of its \~\$1Tn market cap per year.

## 20 July 2026

Equity
Semiconductors

BofAS

BofAS

BofAS

BofAS

CXMT: ChangXin Memory Technologies

## Contents

Memory is still critical in open models 3
Chinese models charge less, but may not cost much less 3
Open models continue to grow in weight size 4
Open models expand memory endpoints vs. closed 5
Scaling gains much faster than efficiency gains 6
China models create disruption but also expand market, beneficial for semis 8
Glossary: 9

## Memory is still critical in open models

## Chinese models charge less, but may not cost much less

Chinese open-model API pricing is very competitive. Latest Kimi K3 charges \$3/M input and \$15/M output vs. Claude Opus 4.8 and GPT-5.6 at roughly 5x that.

However, we flag API price is a business-model choice, not necessarily a hardware-cost readout. Kimi K3 still requires a 64+ accelerator super-node with \~1.4 TB of HBM per serving instance to run – that memory content is required whether Moonshot charges \$3 or \$30 per million tokens.

OpenAI's similar open model with MXFP4 native precision (for like-for-like compression) with 120B total parameters (23x smaller than Kimi K3) requires \~63GB of weight memory to run (22x smaller), in-line with the memory requirements of K3 if model sizes were the same.

Exhibit 1: Global token usage increased on average by +6% per week since 2025, or +9% per week since 2026, with China models accounting for \~70% of the tokens in July 2026
Weekly Token Usage by Major Models (API) via OpenRouter


[[KC_IMAGE_001]]

Source: BofA Global Research, OpenRouter

## Cost advantage often comes from non-hardware efficiency

We suspect much of Chinese LLM cost advantages (up to 5-50x vs. western) actually come from non-hardware efficiencies.

## Architectural efficiency (2-3x)

\- Extreme MoE sparsity: Qwen3-Coder-Next activates just 3B of 80B total parameters (\~3.75%); Kimi K3 activates \~1.8%. Compute per decoded token in Chinese LLMs is a fraction of what a comparable dense model would need.

\- MLA/hybrid attention: DeepSeek's MLA and Kimi's KDA compress KV cache 10-90x vs. standard attention, so batch density is also much higher — more concurrent users per GPU.

\- Native low-bit quantization: Kimi K2 Thinking ships W4A16, K3 ships MXFP4, DeepSeek trains natively in FP8. That's another 2x throughput vs. FP16 of Meta Llama 4 or Google Gemma 4 open models.

Combined, net architectural efficiency could reach 2-3x per token vs. an equivalently sized Western model that ships in BF16/FP8 native, without these efficiency gains.

Input-side infrastructure cost (\~1.5-2x)


\- Chinese labor: Engineering salaries 40-60% lower than US equivalents

\- Land/real estate: Data center capex and related land/shell/power spend meaningfully lower in interior China (Ningxia, Guizhou)

Combined, net input-cost advantage could also reach 1.5-2x per token, depending on the underlying compute bill.

Competition, subsidies for market share

Lastly, we flag Moonshot AI paused new subscriptions within just 48 hours of K3's launch, because GPU capacity ran out or potentially just to cut costs/losses.

If K3's low price genuinely reflected proportional hardware savings, we expect Moonshot to have provisioned enough capacity. As such, actual hardware cost per query at Kimi K3 could be higher than the much cheaper API price implies, and Moonshot may be subsidizing to grab market share.

There are similar cases, such as Xiaomi cutting its MiMo model pricing by 99% in May 2026, likely as an effort to grab market share.

Exhibit 2: Open models continue to grow in weight size (i.e. memory), with their API input/output cost generally also increasing with the weight Key Open Models Pricing and Weight Memory


Source: BofA Global Research estimates

## Open models continue to grow in weight size

Frontier open-weight model size continues to increase sharply (closed models often do not publish model weight data):

\- DeepSeek-V3 at 671B (Dec 2024)

\- Kimi K2 at 1T (mid-2025)

\- DeepSeek-V4-Pro at 1.6T (Apr 2026)

\- Kimi K3 at 2.8T parameters (Jul 16, 2026) — the largest open-weight model ever released

## Larger weights flow directly to memory demand.


Weight memory scales with total parameters (such as K3's 2.8T parameters), not active parameters.

Even with industry compression/quantization from FP8 to MXFP4 delivering a 2x saving, model sizes have grown \~4x more in parameter growth, more than offsetting the

efficiency gains from compression. For instance, Kimi K3 (July 2026) in native MXFP4 requires 2x the memory of DeepSeek-V3 in FP8 (December 2024).

## Active parameters reduce compute, not memory

With the use of MoE (i.e. using just active parameters), Kimi K3 activates only 16 of 896 experts at a time, i.e. it only activates 50B of its total 2.8T parameters per token. This greatly reduces the total compute requirement during the inference process.

However, the model still needs to keep nearly the entire expert pool (i.e. the entire model weight) resident in nearby memory. In fact, HBM capacity scales much more closely with total parameters, than with active parameters.

This is because MoE routers select experts dynamically per token, so every expert (i.e. total weight) must remain resident in fast memory regardless of activation sparsity. As a result, doubling total parameters requires double HBM per instance, which is why K3 needs 64+ accelerators while V3 needed just 8.

## Larger model weight drives multi-tier memory

Lastly, larger weights force multi-tier memory hierarchies: hot experts in HBM, inactive experts spilled to CPU LPDDR5X/DDR5, cold KV cache to enterprise NAND. Every tier gets more content per deployment.

Exhibit 3: Open MoE model total parameters and active parameters per token continue to scale upward, resulting in larger weight for memory storage
Open MoE models total parameters (bn) vs. active parameters per token (bn)

[[KC_IMAGE_002]]

Source: BofA Global Research estimates

## Open models expand memory endpoints vs. closed

The mechanism is simple: a closed model has one deployment footprint; an open model has as many footprints as it has downloads.

For instance when OpenAI serves GPT-5.6 (closed model), the model weights live in a small number of Microsoft Azure data centers. Every user in the world — millions of them — hits that same shared HBM pool. Total memory content is set by peak concurrent demand across all users combined, and can be amortized because usage patterns diversify across time zones and workloads.

But when Moonshot releases Kimi K3 weights (open model), or DeepSeek releases V3, or OpenAI releases gpt-oss-120b, the weights get downloaded and loaded into memory on every buyer's own hardware. An enterprise running gpt-oss-120b needs its own 80 GB of HBM3E. A sovereign cloud running DeepSeek-V3 provisions its own 8× H200 cluster (\~1.1 TB of HBM). Moonshot's own guidance for K3 calls for 64+

accelerators per serving instance — and that footprint gets replicated by every enterprise, government, and cloud that downloads the weights. None of that memory would have been purchased if the same intelligence were only available through a closed API, because the customer would have rented compute cycles rather than owned the hardware.

As a result for open models, both model weights and KV cache must be resident in fast memory to serve inference — they cannot be shared across separately owned clusters. Unlike a shared API where 10,000 users effectively share one copy of the weights in HBM, 10,000 enterprises self-hosting the same open model means 10,000 copies of the weights loaded into 10,000 separate HBM pools. Each deployment also needs its own KV cache capacity scaled to its own user base — and at the 128K–1M context windows common in 2026, KV cache per active user session can exceed 40 GB, so this scales with concurrency on every endpoint independently.

## Memory endpoints benefit from cheaper API pricing

Open models having separate memory endpoints also benefit end memory deployment, as Chinese LLM labs charge cheaper API pricing and thus drive overall demand up. In other words:

\- Cheaper Chinese API pricing = more inference workload volume + more open-weight enterprise self-hosting + more memory sockets deployed globally.

While frontier model labs are spending capital to grab share, the market is likely expanding its aggregate compute and memory capacity in the process; and every enterprise that downloads Qwen, GLM, Hunyuan, or MiMo instead of paying for Claude Opus creates a new customer-side memory footprint that wouldn't exist in a pure closed-API world.

Overall, closed models consolidate memory demand; open models multiply it — and the compression from efficiency innovations doesn't offset multiplication by endpoint count.

## Scaling gains much faster than efficiency gains

Lastly, we highlight workload intensity and overall demand gained by Jevons Paradox are far greater than the efficiency gains from MoE, quantization, KV cache compression techniques.

Exhibit 4: Latest multi-agent workloads generate up to 200,000x more output tokens per query than traditional non-reasoning chat workloads (GPT-4o)
Tokens per query by different model workloads


[[KC_IMAGE_003]]

Source: BofA Global Research estimates

Exhibit 5: Newer releases of open models generally feature much larger total parameters, context windows, and weight memory gen-over-gen
List of key LLMs and their model weights


Source: BofA Global Research estimates

## China models create disruption but also expand market, beneficial for semis

While there is no perfect way to rank models, we rely on third party benchmarks that rank models along various AI, coding and agentic scores.

The most recent ranking (as of Jul-4) suggests that per the AI index:

1. US frontier models from Anthropic and OpenAI retain the lead, especially after the approval given to Anthropic's Fable 5 model;

2. China-based models now occupy 8 of the top 16 spots. The highest spot is occupied by GLM 5.2, a 750 Billion parameter/1mn context window open weight model delivered by Zhipu or Z.ai. The success of Chinese models indicates that last year's shock waves created by the success of China's DeepSeek was a sign of things to come, and not just a one off. It's debatable how much western model distillation was used in training the China models, per media reports, but the fact is China's models are likely only months and not years behind US technology despite China not having access to the latest in compute, networking and memory chips;

3. NVDA is also becoming a major contributor to the open source community. We believe NVDA's efforts not only help it improve its hardware, but they also help to expand the medium/smaller size AI adopters who lack resources in engaging with frontier labs.

As reference in Open-Source Models - the model's weights, code, and training methodology are broadly available, allowing developers to inspect, modify, fine-tune, and self-host the model. Open-source models typically maximize transparency, innovation, and ecosystem adoption, but offer less direct control to the creator.

Open-Weight Models - the trained model weights are released for download and deployment, but parts of the training data, code, or methodology may remain proprietary. Open-weight models strike a balance between openness and commercialization by enabling self-hosting while preserving some intellectual property.

Proprietary (Closed) Models - Neither the model weights nor training details are publicly available; customers access the model only through APIs or cloud services. Proprietary models typically offer the strongest monetization and control, but may face greater pricing pressure as open-source and open-weight alternatives improve.

Exhibit 6: AI ranking between top proprietary, open source and open weight models
Models shaded in red are from China, the green shaded model ifs from Nvidia


Source: Artificial Intelligence Index, BofA Global Research

## Glossary:

AIME – American Invitational Mathematics Examination

BF16 – Brain Float 16-bit

CHIPS Act – Creating Helpful Incentives to Produce Semiconductors Act

CPU – Central Processing Unit

CSA – Compressed Sparse Attention (DeepSeek)

CSP – Cloud Service Provider

CXL – Compute Express Link

CXMT – ChangXin Memory Technologies

DDR5 – Double Data Rate 5th generation

DRAM – Dynamic Random Access Memory

EECS – Electrical Engineering and Computer Science (UC Berkeley)

FP4 / FP8 / FP16 – Floating Point 4-bit / 8-bit / 16-bit

GLM – General Language Model (Zhipu / Z.ai)

GPQA – Graduate-level Google-Proof Q&A

GPU – Graphics Processing Unit

GQA – Grouped-Query Attention

HBM – High Bandwidth Memory

HBM3E / HBM4 – High Bandwidth Memory, 3rd-gen Extended / 4th generation

HCA – Heavily Compressed Attention (DeepSeek)

HLE – Humanity's Last Exam

INT4 – Integer 4-bit

KDA – Kimi Delta Attention (Moonshot)

KV cache – Key-Value cache

LLM – Large Language Model

LPDDR5X – Low-Power DDR5 Extended

MHA – Multi-Head Attention

MIT – Massachusetts Institute of Technology (also open-source software license)

MLA – Multi-head Latent Attention (DeepSeek)

MMLU – Massive Multitask Language Understanding

MoE – Mixture of Experts

MQA – Multi-Query Attention

MTP – Multi-Token Prediction

MU – Micron Technology

MXFP4 – Microscaling FP4 (OCP standard)

NAND – Not-AND flash memory

NVFP4 – NVIDIA FP4

NVLink-C2C – NVIDIA Link Chip-to-Chip

OEM – Original Equipment Manufacturer

oss – open-source software (e.g., gpt-oss)

PO – Price Objective

PTQ – Post-Training Quantization

QAD – Quantization-Aware Distillation

QAT – Quantization-Aware Training

SMIC – Semiconductor Manufacturing International Corporation

SSD – Solid State Drive

SWE-Bench – Software Engineering Benchmark

TSMC – Taiwan Semiconductor Manufacturing Company

W4A16 – 4-bit Weights, 16-bit Activations

WFE – Wafer Fab Equipment

YMTC – Yangtze Memory Technologies Corporation


## Price objective basis & risk

## Micron Technology, Inc (MU)

Our \$1550 PO is based on a sum-of-parts valuation that values: (1) traditional cyclical memory business at \$1,040/sh at 3x CY28E P/B, toward the high-end of MU's long-term range 0.8x-3.1x as we are potentially in a memory upcycle, and (2) AI HBM business at 31x CY28E PE, in-line with AI compute peer group median.

Downside risks: (1) larger than expected memory ASP decline, (2) greater competition from China newcomers, (3) share loss to large competitors, (4) softening of demand across major end markets such as data center, smartphones, or PCs.
