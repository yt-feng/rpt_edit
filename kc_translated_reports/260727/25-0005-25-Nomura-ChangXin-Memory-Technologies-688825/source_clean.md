## The DRAM in the Chinese crown; initiate at Buy CXMT should continue to gain market share as global supply of memory could remain tight
## Initiate coverage at Buy with and a TP of CNY116

We initiate coverage of CXMT – China's largest DRAM maker – at Buy with a TP of CNY116. We expect CXMT's market share gain to accelerate considering that the global supply of memory is unlikely to ease in the coming years. Supported by capacity expansion, node migration, and ASP hikes, we forecast CXMT to post 63%/74% sales/net profit to parent CAGRs in 2026-28F. Our TP of CNY116 is based on 20x 2028F EPS of CNY5.8. We assign a 20x target P/E multiple as we expect CXMT to trade at 2x the valuation of its major US competitor, Micron ([MU US, Not rated]; which has traded at \~10x over the past five years), owing to market share gains and the higher valuation multiples in China's market. Downside risks include: 1) worsening of end demand; 2) intensifying competition from domestic peers such as YMTC (unlisted); 3) insufficient supply of IC and components (e.g., CPUs); and 4) escalation of geopolitical tensions between the US and China.

## Demand could continue to outpace supply in the foreseeable future; CXMT appears well-positioned to gain market share

We estimate that strong demand for agentic AI will drive a more than sevenfold increase in global memory usage (with 60%+ bit CAGR) over 2026-30F, even after accounting for potential adoption of memory-efficiency technologies (discounting memory usage by 4x). However, expansion of semiconductor capacity faces multiple bottlenecks (e.g., clean rooms, equipment, materials, and talents). Memory makers are expanding capacity at a 30-40% bit CAGR over 2026-30F, but that could still be insufficient. We forecast CXMT to record bit expansion at a 40-45% CAGR over 2026-30F and its global DRAM market share to increase from \~10% currently to \~18% by end-2028F.

## Impact from the MATCH Act (or potential US sanctions) is worth monitoring

The MATCH Act is a US export legislation designed to restrict China's access to advanced chip-making technologies by coordinating with allies to curb exports of crucial equipment and materials and preventing foreign firms from servicing machines already in China. Although CXMT may still have access to sufficient DUV domestically without using EUV to develop its upcoming 12-16nm nodes, whether it can get key foreign-made equipment (localization rate now is around $40\%$ , according to our estimates) and materials (such as photoresist) is worth monitoring, in our view. In the worst case, we assume CXMT's capacity expansion in Shanghai (potentially $30 - 40\%$ of its total capacity by 2028F) could be pushed out.


Source: Company data, NOM estimates


Market Cap (USD mn)


Donnie Teng - NIHK

Frank Fan - NIHK

## Asia Technology

CW Chung - NIHK

## Key data on ChangXin Memory Technologies


Source: Company data, NOM estimates


Source: Company data, NOM estimates

## Company profile

CXMT is the largest DRAM maker in China, and the forth largest in the global market, next to Samsung, Hynix and Micron.


Our TP CNY116 is based on 20x 2028F EPS of CNY5.8. We assign a 20x target P/E multiple as we expect CXMT to trade twice the valuation of its major US competitor, Micron, which has traded at \~10x over the past five years, due to CXMT's market share gains and the higher valuation multiples in the China market. The benchmark index is CSI300

## Risks that may impede the achievement of the target price

Downside risks include: (1) worsening of end demand; (2) intensifying competition from domestic peers such as YMTC; (3) insufficient supply of IC and components such as CPUs; and (4) escalation of geopolitical tensions between the US and China.

## ESG

CXMT provides details of its ESG policy on the company website (https://www.cxmt.com/en/sustainable.html). CXMT recognizes: (1) its duty in preserving and protecting the environment and strictly follows government law and regulations; (2) it is committed to complying with all labor laws and ensuring a free, equal and fair working environment for its employees; and (3) it indicates that integrity and compliance are the basic requirements for the survival and healthy development of the company by following the highest standards of compliance and business ethics to achieve sustainable business development goals.

# AI evolution could drive exponential memory demand growth

Why cloud AI and agentic AI may generate a lot of memory and networking demand

The memory industry entered a structural growth phase following the launch of ChatGPT [owned by OpenAI (unlisted)] in December 2022, which triggered considerable growth in GPU and high-bandwidth memory (HBM) demand. In modern workloads like AI and high-performance computing, memory is one of the primary performance bottlenecks as memory bandwidth cannot keep up with processor speed, where the rate of improvement in processor performance outpaces the rate of improvement in memory performance due to limited I/O and decreasing signal integrity. This disparity limits the overall system performance, as the processor spends more time waiting for data from memory, leading to a bottleneck.

Fig. 1: Performance of LLM, computer chips, memory, and interconnect

[[KC_IMAGE_001]]

Source: NOM

To break through the bottleneck, the industry relies on several workarounds, including memory content and bandwidth improvement as well as higher throughput from communication networking:

\- High bandwidth memory (HBM): Stacking more memory chips vertically directly on the processor package to increase bandwidth and drastically reduce distance and latency.

\- Caching: Utilizing smaller, ultra-fast on-chip memory (like SRAM) to hold frequently accessed data closer to the logic compute die.

\- Memory-on-logic or compute-in-memory: Packaging or moving the computing logic as close as possible or directly to the memory storage area to prevent data from having to travel across the chip.

\- Compute express link (CXL): Specialized interconnect technologies that allow processors to pool and access memory dynamically.

\- More interconnects for both copper and optical: As copper interconnects hit physical scaling limits and traditional packages run out of die shoreline, next-generation hardware is exploring optical interconnects to separate GPUs and HBMs. This bypasses traditional physical constraints, multiplying HBM capacity and reducing electro-optical data travel times.

\- Model compression: Reducing model size through techniques like quantization (lowering precision) or pruning to make them fit entirely into on-chip cache or HBM.

Subsequently, the adoption of retrieval-augmented generation (RAG) and agentic AI applications has accelerated demand for conventional servers and SSDs, and initiated a triple memory supercycle (commodity DRAM, HBM, and SSD) since 3Q25.

As AI semiconductor demand shifts from training toward inference workloads, memory demand is entering a period of exponential expansion. This reflects the rapid growth in KV-cache memory requirements, driven by increases in user base, user engagement time, AI task complexity, reasoning-token consumption, and the emergence of agentic AI, where token usage per user is surging exponentially (Fig. 2 - 3). Memory demand effectively scales as the multiplicative function of these variables (a1 x a2 x a3 x a4 x ...), implying that memory demand could rise by several thousand-fold over the next five years, in our view.

Fig. 2: Token usage trend by different LLM providers

[[KC_IMAGE_002]]

Source: Company data, NOM estimates

Fig. 3: Estimated token consumption by prompt cases


Source: NOM estimates

## How agentic AI works and how much memory may be consumed if considering the memory efficiency technologies

When an end user asks an agentic AI to complete a task, we expect the request flows through eight distinct stages (Fig. 4).

## Stage 1: User request arrives

The user's prompt is tokenized, batched, and queued for inference. The orchestrator parses the request and prepares an execution plan for the agentic pipeline.

## Stage 2: Model weight loading

The model's parameters are loaded (or already resident) into accelerator memory. For large models, weights may be shared across multiple GPUs using tensor or pipeline parallelism.

## Stage 3: Prefill/prompt processing

All input tokens are processed in parallel through the transformer layers. Attention matrices are computed and the KV cache is initialized for subsequent autoregressive decoding.

## Stage 4: Reasoning and planning

The model generates a chain-of-thought plan, deciding which tools to call and in what order. Each new token extends the KV cache, and memory pressure grows with sequence length.

## Stage 5: Tool execution

The agent invokes external tools such as web search, code execution sandboxes, file I/O, or API calls. This stage runs primarily on the CPU side and barely touches GPU memory.

## Stage 6: Context integration

Tool results are tokenized and appended to the conversation. The model re-processes the expanded context window. The KV cache grows significantly, making this one of the most memory-intensive stages.

## Stage 7: Multi-step iteration

Agentic loops repeat stages 4 through 6 multiple times. Each iteration further grows the context window. Memory pressure peaks here, potentially approaching HBM capacity limits.

## Stage 8: Response generation

Final autoregressive decoding produces the output tokens. The response is detokenized, formatted, and streamed back to the user through the API gateway.

Fig. 4: Workflow and key bottlenecks of an agentic AI task


Source: NOM

To complete the complicated agentic AI tasks throughout the above-mentioned eight stages of work flow, the modern AI system now heavily relies on a layered memory hierarchy, with each tier trading off speed against capacity. This results in the optimized usage of all different types of memories. We categorise and summarise the memory tiers relevant to agentic AI workloads, including the emerging high bandwidth flash (HBF) technology in Fig. 5. Each stage activates different memory tiers at different scales. After a complete agentic task run, we expect the peak concurrent memory consumption at stage 7 (multi-step iteration), when memory pressure is at its highest, particularly when the more complicated task requiring multiple steps of iteration repeatedly (Fig. 6).

Fig. 5: AI memory hierarchy


Source: NOM

Fig. 6: Different types of memories used in an agentic AI task work flow
HBF is not yet ready for mass production


Stage 2: Model Weight Loading


4 Stage 3: Prefill / Prompt Processing


Stage 4: Reasoning & Planning


Stage 5: Tool Execution


Stage 6: Context Integration


Stage 7: Multi-Step Iteration


Stage 8: Response Generation


Source: NOM

We note that three different layers of memories will be consumed in the eight stages of running the agentic AI tasks, including per task used memory (mainly SRAM, HBM and DDR, used for end user-specific KV cache), shared memory (mainly HBM, DDR, and SSD for model weights, checkpoint, and KV reuse pool), and persistent storage (mainly SSD and HDD for cold data storage once the data are generated as well as RAG and KV cold pool). For the memory demand trend in the future driven by agentic AI, there are two major variables that may impact the demand trend, including:

1. The concurrent agentic AI task numbers per year (+): This includes the number of AI users, the agentic AI adoption rate, the agentic AI tasks per annum globally, the average duration time of an agentic AI task.

2. The memory usage discount driven by memory efficiency technologies (-): This includes KV quantization, GOA (grouped query attention), PagedAttention, prompt/prefix caching, MLA (multi-head latent), TurboQuant, etc.

Several memory-efficiency technologies could dramatically reduce the memory footprint of AI inference. Critically, these techniques stack multiplicatively – combining attention architecture compression with KV cache quantization and memory management yields compound reductions of 4-40x. However, the practical memory savings is unlikely to exceed 5x, as weight KV quantization, converting weights and activations of running LLMs and neural networks from high-precision data types such as 32-bit floating points (FP32) or 16-bit floating points (FP16) into lower-precision integers such as 8-bit (INT8) or 4-bit (INT4), is the single-largest factor, in our view, while KV compression adds on top but is smaller than weight adjustments.

We estimate that the demand for concurrent agentic AI will drive task numbers per year to grow strongly during 2026-30F, i.e., increase 50x higher by 2030F vs 2026F, although with the memory usage discount driven by memory-efficiency technologies, which would still drive the memory usage for agentic AI tasks by more than 10x. In a scenario in which the demand for non-AI applications does not grow, AI applications could still drive a memory demand CAGR of more than 60% over 2026-30F (growing by more than 7x), on our assumptions. Key risks include: agentic AI usage and adoption rate by end-users falling short of our expectations; and memory-efficiency technologies driving more memory savings than we currently forecast.

Fig. 7: Major memory efficiency technologies


Source: Company data, NOM

Fig. 8: Memory usage in different stages of agentic AI work flow
This includes the per-task and shared memory used in the different stages, but not the cold storage for data saving.


Source: NOM estimates
Multiple tasks can be done concurrently through different users who can share the memory pool, but the cold data from all the different users need to be stored accumulatively.

Fig. 9: Average memory usage per task can be done concurrently within a year


[[KC_IMAGE_003]]

Source: NOM estimates

## Fig. 10: Memory usage for agentic AI tasks in 2026-30F

As concurrent agentic AI task numbers could grow meaningfully, this may overcome the impact of memory efficiency technologies and drive strong memory demand.


[[KC_IMAGE_004]]

Source: NOM estimates

## AI demand could potentially grow if AI bots run tasks themselves

According to the Cloudfare CEO's comment (news link), the rapid increase in agentic internet traffic has implied that “bots have now passed human traffic online for the first time in the Internet's history”. Hence, we raise the qualitative question “what if the AI bots can run tasks themselves without the constraint by human beings”? In this case, the demand upside could be much bigger, as the constraint only depends on:

1. Whether human beings authorized AI bots to do so (security concern);

2. The limitation of infrastructure including utility, semiconductor chips, data centers, etc., and most importantly, talents;

## 3. Capex limitations of capex cloud companies, enterprises and end-users.

In the most extreme case, in our view, we may need to seriously consider that the demand potentiality of agentic AI could be enormous, while in the coming years, semi capacity expansion is facing its biggest bottleneck – the shortfall in clean rooms, equipment, materials, and most importantly, humans.

Fig. 11: Bots vs human web traffic
Bots now generate more web traffic than humans.

[[KC_IMAGE_005]]

Source: Cloudfare

## DRAM-on-logic wafer-on-wafer (WoW) stacking an emerging trend that could grow meaningfully in late 2027F

AI inference is a memory-bound task in the smart-edge domain requiring high memory bandwidth and energy efficiency with modest compute power in between 45 and 100+TOPS. Based on our assumptions, the DRAM-on-logic WoW can achieve 1TB/s bandwidth for throughput higher than 100 TPS (tokens per second). We believe this technology could gain strong momentum from late 2027F, led by AI agents in the automotive smart cockpit, premium smartphone/PCs, and robotics segments. CXMT and GigaDevice co-work on the DRAM-on-logic production and design to address the rising demand for edge AI/physical AI in China, as China is one of the largest markets that is likely to replicate its successful experience on expanding the consumer AIoT market into the physical AI market, driven by the increasing amount of smart car, robotics, Clawbot, and industry/medical applications.

Fig. 12: Difference between MCM vs WoW for edge AI chips

[[KC_IMAGE_006]]

Source: NOM

Fig. 13: Different types of WoW stacking

[[KC_IMAGE_007]]

Source: Company data, NOM

Fig. 14: Key WoW projects in 2026-28F in China


Source: NOM, NOM

## China's DRAM production self-sufficiency rate remains low

According to WSTS, China accounted for \~25% of global DRAM market in 2025. However, according to our estimates, the market share of Chinese domestic DRAM makers (including CXMT and other domestic players) in terms of production revenue was only \~10% of the global DRAM market. Thus, the self-sufficiency rate of DRAM production by domestic players was only around 30% in 2025, which implies the domestic DRAM makers such as CXMT still have meaningful room to grow market share in China.

Fig. 15: China's DRAM market share vs domestic China's DRAM production market share in 2025

[[KC_IMAGE_008]]


## Memory supply growth is likely lower than demand growth due to physical constraints

We assume a memory demand CAGR of 60% over 2026-30F; in contrast, we expect an industry supply CAGR of around 30-40%; thus whether the undersupply can realistically be resolved is worth monitoring, in our view.

At present, the industry is striving to narrow this widening supply-demand gap through multiple software- and architecture-level optimizations, as we have noted in the section on memory efficiency technologies. However, we believe these solutions merely slow the pace of growth rather than reversing the trend. Therefore, every available approach – including NAND offloading (which offers over 100x higher capacity despite slower speeds) and the adoption of ultra-high-bandwidth NAND (HBF) – will likely need to be deployed simultaneously, in our view. But this may also cause the NAND supply to be even tighter and may not be able to help relieve the already tight DRAM supply effectively.

## What are CXMT's technology capabilities and pricing?

We estimate CXMT's current mainstream technology in 2026F is around the 1x-1y node (around 16-17nm), with the yield rate of its DDR5 product at around $80\%$ and DDR4 at $90\%+$ . The company is likely pushing forward the technology to 1z-1a node (around 10-15nm) with HBM3 mass production capability from 2027F onwards.

For 15nm and 10nm node development, we expect CXMT to continue pushing the technology migration forward without using EUV. However, the photoresist supply for sub-12nm node could be a concern, as the high-end photoresist is now mostly supplied by Japan-based companies. For HBM, we believe CXMT has sent HBM3 samples to the leading ICT company and other companies in China, but qualification could take time. On the other hand, HBM3e technology is under development.

When it comes to pricing, our channel checks with some of the leading domestic smartphone and PC/server OEM companies indicate that CXMT's pricing is lower than that of the leading overseas DRAM companies, but not significantly. We estimate the pricing is around 0-20% lower, primarily due to Beijing's policy to support local tech companies that can procure memories with a more favorable price. However, considering that CXMT's mainstream technology lags the leading overseas DRAM companies' by around five years, we estimate its gross die per wafer could be only a few hundred dies vs more than one thousand dies for the leading overseas DRAM companies. Hence, we estimate CXMT's 2026F wafer ASP at around USD14-15k. However, we expect CXMT's bit growth per wafer to improve further in 2027-28F due to its node migration from 16-17nm to 14-15nm, thereby increasing the ASP further to USD21-25k (Fig. 16-18).

Fig. 16: CXMT – shipment breakdown by technology node

[[KC_IMAGE_009]]

Source: DRAMexchange, NOM

Fig. 17: CXMT: shipment breakdown by density

[[KC_IMAGE_010]]

Source: DRAMexchange, NOM

Fig. 18: CXMT's wafer pricing trend

[[KC_IMAGE_011]]

Source: Company data, NOM estimates

## How much capacity can CXMT expand by 2028F?

CXMT plans to actively develop and launch next-generation products (beyond LPDDR5X/DDR5, such as HBM3 production) to serve future customer demand. The company raised CNY57.9bn (approximately USD8.55bn) via IPO on the Shanghai Stock Exchange's STAR Market on 27 July. Once an over-allotment (green shoe) option is exercised, the maximum fund raised will climb to CNY66.6bn (USD9.83bn). It costs around USD100mn for every 1kwpm capacity expansion for DRAM (Fig. 19), and we estimate CXMT had 280kwpm of capacity in Heifei and Beijing as of end-2025, and will increase to 350kwpm by end-2026F. It is likely to add an additional 100kwpm capacity each in 2027F and 2028F, which would make its total capacity to reach 550kwpm by end-2028F. On the other hand, CXMT is also building up HBM packaging capacity in Shanghai (Xingpu Tianying) potentially with 50kwpm of packaging capacity with room for further DRAM production capacity expansion (Fig. 20).

Based on our capacity forecasts, and assuming CXMT runs its fabs at full capacity utilization in 2026-30F, the wafer shipment CAGR over 2026-30F would be around 20-25%. Assuming CXMT upgrades its technology node every two years, the bit growth CAGR would be around 40-45%. Although CXMT's bit CAGR is higher than the industry average of 30-40%, it could still be below the market demand CAGR of over 60%. That said, we expect CXMT to continue to gain market share from its global peers (Fig. 21).

Fig. 19: Capex requirement for 1kwpm capacity expansion

[[KC_IMAGE_012]]

Source: NOM estimates

Fig. 20: CXMT capacity trend

[[KC_IMAGE_013]]

Source: NOM estimates

Fig. 21: CXMT: bit growth and wafer shipment growth

[[KC_IMAGE_014]]

Source: NOM estimates, DRAMexchange

## Global DRAM supply/demand dynamics remain favorable as demand is too strong but capex spending is lagging behind

In general, we acknowledge market concerns around the risk of a sharp DRAM market correction precipitated by unmanageable capacity expansion, considering the cyclical nature of the industry. However, historically, DRAM companies' capital intensity (capex-to-sales ratio) has remained mostly in the 25-45% range over the past 15 years. However, in view of the strong AI-driven memory demand since Sep-2025, capital intensity may drop significantly to only 15% in 2026F (Fig. 22). This implies that the DRAM market is likely to be able to absorb a much higher capex across the DRAM makers, which includes domestic DRAM companies such as CXMT.

However, as memory prices have gone up significantly since Sep-2025, we expect memory companies and their customers to gradually understand that it would be healthier for memory prices to stabilize in the coming quarters. Indeed, we have seen long-term memory supply agreements (LTAs) being reached between memory companies and their key customers. Thus, from 2028F onwards, we think memory companies will focus more on reasonable capacity expansion to drive sales and steadily improved earnings rather than pushing for memory prices to significantly grow from current levels. We also expect memory companies to meet varied customer demands rather than solely AI demand in order to maintain healthy supply/demand dynamics (Fig. 23).

Fig. 22: Historical DRAM capex to market (dollar amount) ratio
The capital intensity of DRAM production is currently too low due to the much bigger DRAM market

[[KC_IMAGE_015]]

Source:WSTS, Gartner, DRAMexchange, NOM estimates

Fig. 23: DRAM supply demand outlook


Source: Company data, NOM estimates

## Key risk to CXMT: MATCH Act (or potential US sanctions) is worth monitoring

The MATCH Act, or any type of US sanction such as the Entity List, could be a potential downside risk to our investment thesis for CXMT. Although CXMT may continue to have access to sufficient DUV domestically without using EUV to develop its upcoming 12-16nm nodes, whether it can get key foreign-made equipment and materials is worth monitoring, in our view.

Based on our assumptions, we estimate CXMT's current domestic equipment localization rate is around $40\%$ . If CXMT were to be prohibited from importing foreign-made equipment and forced to increase its localization rate urgently, it would likely negatively impact CXMT's production yield rate. On the other hand, for materials such as photoresist, currently most of the high-end products are dominated by Japan-based companies such as TOK (4186 JP, Neutral), JSR (unlisted), and Shin-etsu (4063 JP, Neutral) without any substitution in China. If CXMT were to be prohibited from importing Japan-made photoresist, it might be unable to further migrate its production node to sub-15nm.

Consequently, in the worst case scenario, we assume CXMT's capacity expansion in Shanghai (which is linked with the company's advanced node (sub-15nm) and HBM production), could be pushed out. Potentially, there could be two DRAM production phases in Shanghai (100kwpm per phase), along with HBM packaging capacity of 50kwpm. If the 200kwpm capacity in 2027F/28F were removed, we expect CXMT's revenue and net profit to the parent company would be down by $13\% / 30\%$ and $14\% / 33\%$ , respectively.

Fig. 24: CXMT: Capacity trend, with and without the Shanghai fab

[[KC_IMAGE_016]]

Source: NOM estimates

Fig. 25: CXMT: Sales trend, with and without the Shanghai fab

[[KC_IMAGE_017]]

Source: Company data, NOM estimates

Fig. 26: CXMT: Net profit trend, with and without the Shanghai fab

[[KC_IMAGE_018]]

Source: Company data, NOM estimates

## Key domestic equipment, material, and OSAT partners

According to CXMT's prospectus and our research, owing to CXMT not being on the US's Entity List, we estimate its current domestic equipment localization rate remains less than $40\%$ , and will evaluate the domestic suppliers carefully by considering different aspects, including the impact on production yield rate and profitability. Below are some key domestic equipment, material and OSAT partners of CXMT.

## Equipment

Etching: AMEC (688012 CH, rating suspended) and Naura (002371 CH, rating suspended) are key domestic suppliers, while AMEC has superior performance, particularly on high-aspect ratio etching.

ALD: Leadmircro (688147 CH)

Wafer bonding: Piotech (688072 CH, Not rated) and Wisdom (unlisted) are potential suppliers, while Piotech has more superior performance.

Inspection: Jingce (300567 CH, Not rated) and Skyverse (688361 CH, Not rated)

Cleaning: ACM Research (ACMR US, suspended)

Stripper: Mattson Technology (BEST, 688729 CH, Not rated)

C-SAM/SAT for back-end package: SBT (688392 CH, Not rated)

## Material

Semi wafer: Eswin (688783 CH, Not rated) and NSIG (688126 CH, Neutral)

Chemicals: Yoke (002409 CH, Not rated) and Konfoong (300666 CH, Not rated)

Gas: G-Gas (688548 CH, Not rated)

CMP pad/slurry: Dinglong (300054 CH, Buy) and Anji (688019 CH, Buy)

## OSAT partners

DRAM: Payton (under 000021 CH, Not rated), Xinfeng (unlisted), JCET (600584 CH, Buy), TFME (002156 CH, Buy), and TSHT (002185 CH, Buy)

HBM: Xinpu Tianying (CXMT in-house, Not rated), Xinfeng, JCET and TFME.

## Major customers and revenue breakdown of CXMT

CXMT sells primarily through a distributor-led model (85%+ of revenue via distributors, remainder direct sales). Top-5 customer concentration: 74.12% (2023), 67.30% (2024), and 68.08% (2025) of the company's main business revenue.

Named end-customers include: Alibaba Cloud, ByteDance, Tencent, Lenovo, Xiaomi, Transsion, Honor, OPPO, and vivo. The company also notes that GigaDevice Group (controlled by Chairman Zhu Yiming) is a customer.

Revenue is split by product: The LPDDR series accounted for 66.43% of 2025 revenue (up from 74.54% in 2023), while the DDR series contributed 31.87% (up from 20.16%), reflecting the ramp-up in DDR5 server products. For HBM, we expect CXMT has sent HBM3 samples to the leading ICT company and other companies in China, but qualification could take time. On the other hand, HBM3e technology is under development.

Fig. 27: CXMT: revenue breakdown by end applications in 2026F

[[KC_IMAGE_019]]

Source: NOM estimates

Fig. 28: CXMT: capacity breakdown by different specs of DDR in 2026F

[[KC_IMAGE_020]]

Source: NOM estimates

## Earnings forecast

We estimate CXMT had 280kwpm capacity by end-2025, and will increase to 350kwpm by end-2026F. CXMT is likely to add additional 100kwpm each in 2027F and 2028F, which would take its total capacity to 550kwpm by end-2028F. On the other hand, CXMT is also planning to build HBM packaging capacity in Shanghai (Xingpu Tianying), with 50kwpm capacity potentially (packaging only rather than DRAM production). As we expect CXMT to run at full capacity over the coming two years, we believe the key variable for wafer output should be mainly yield rate. We expect CXMT's yield rate could be volatile in between 75-85% depending on its technology migration progress and product mix (e.g., DDR5 has a lower yield rate than DDR4, and HBM production initially may carry a lower yield rate).

As CXMT's mainstream technology has lagged the leading overseas DRAM companies by around five years, its gross die per wafer, on our assumptions, could be only a few hundred dies vs the leading overseas DRAM companies of over 1,000 dies. Thus, we estimate CXMT's wafer ASP at around USD14-15k in 2026F. However, we expect CXMT's bit growth per wafer will improve in 2027-28F due to its node migration from 16-17nm to 14-15nm. Thus, we forecast ASP will increase further to USD21-25k. Hence, we estimate that CXMT's sales will grow 35-400% in 2026-28F with net profit to the parent company growing 40-6,000% over the same period.

Fig. 29: CXMT: capacity and utilization rate

[[KC_IMAGE_021]]

Source: Company data, NOM estimates

Fig. 30: CXMT: wafer price

[[KC_IMAGE_022]]

Source: Company data, NOM estimates

Fig. 31: CXMT: P&L


Source: Company data, NOM estimates

## Valuation and risks

We initiate coverage of CXMT with a Buy rating with TP of CNY116 is based on 20x 2028F EPS of CNY5.8. Our 20x target P/E is based on: 1) the valuation in China being 1-3x higher than in the US market based on Bloomberg consensus numbers for ACMR Shanghai (688082 CH, Not rated) vs ACMR (ACMR US, rating suspended) (Fig. 32); and 2) Micron's historical two-year forward P/E range of around 5-15x with midpoint of 10x. Thus, if we assume CXMT is trading at 2x Micron's valuation (as we view Micron as one of CXMT's closest competitors), its P/E could be around 10-30x, with a midpoint of 20x (Fig. 33).

On the other hand, as CXMT's bit production growth is running at around 20% ahead of global DRAM bit growth for the coming year, on our estimates, we expect CXMT's market share would increase from the current \~10% to \~18% by end-2028F, which would result in a market share closer to Micron's 20%+. Thus, CXMT's market share could be approaching that of Micron's as time goes by. Micron currently is trading at USD960bn market cap (as of 20 July 2026).

Downside risks: 1) deteriorating server, PC, smartphone and automotive demand; 2) rising competition from domestic peers such as YMTC (unlisted), as YMTC is also developing DDR5 and could be ready for sampling by end-2026F, but initially it could be mainly for its internal SSD usage; 3) insufficient IC and components supply, such as CPU; and 4) rising geopolitical tensions between the US and China, which would put CXMT's business development, capacity expansion, and technology migration at risk.

Fig. 32: P/E multiple of ACMR Shanghai vs ACMR US
ACMR Shanghai's P/E is trading at 1-3x of ACMR US

[[KC_IMAGE_023]]

Source: Bloomberg Finance L.P.

Fig. 33: Estimated P/E of CXMT based on Micron's
We assume CXMT's P/E is also likely trading at 1-3x of Micron's

[[KC_IMAGE_024]]

Source: Bloomberg Finance L.P.

Fig. 34: CXMT: Market share by DRAM bit production

[[KC_IMAGE_025]]

Source: Company data, NOM estimates

# Appendix: Manufacturing facilities, management team, and major shareholders

## Company profile

CXMT Corporation (长鑫科技集团股份有限公司, was originally established in May 2016 as Hefei Ruili Integrated Circuit (合肥睿力集成电路). The company name was later changed to Innotron Memory and subsequently renamed ChangXin Memory Technologies in 2019, starting with 20kwpms capacity using a 19nm process for 8GB LPDDR4 and DDR4 DRAM production initially. Following a few years of expansion, CXMT has become China's largest and the world's fourth-largest DRAM manufacturer, and the only mainland Chinese company with mass-production capability for general-purpose DRAM, headquartered in Hefei, Anhui Province, China. CXMT operates as an IDM (Integrated Device Manufacturer), integrating chip design, wafer fabrication, packaging & testing, and product sales. The company's founder and Chairman, Zhu Yiming (朱一明), is also the controlling shareholder (at 2.6% pre-IPO stake) and founder of GigaDevice Semiconductor (603986 CH, Buy). CXMT has developed four generations of proprietary DRAM technology and its products include DDR4, DDR5, LPDDR4X, LPDDR5, and LPDDR5X, serving applications in mobile terminals, PCs, servers, AI, VR, and IoT. According to company, as of 2025, CXMT held approximately \~8% global DRAM market share, up from \~4% in 2024.

During the reporting period in 2022-25, CXMT's capacity utilization rate improved steadily from $85\%$ to $95\%$ . The company recorded cumulative losses of CNY8.32bn (2022), CNY16.3bn (2023), and CNY7.1bn (2024) before turning profitable in 2025 (net profit CNY18.7bn) as DRAM prices surged. In 1Q26, CXMT's revenue surged $719\%$ y-y to CNY50.8bn, with net profit of CNY24.8bn, as DRAM prices rose sharply due to the continuous rise of global AI-driven demand. The company forecasts 1H26 revenue of CNY110-120bn and net profit of CNY50-57bn.

## Facilities and offices

CXMT operates three DRAM wafer-fabrication plants across two cities (Hefei and Beijing), with a target to increase combined monthly capacity to 300kwpm by end of 2026. The company is also expanding an HBM (High Bandwidth Memory) production facility in Shanghai, targeting production by end-2026.

Fig. 35: CXMT: production facilities and offices


Source: Company data, NOM

## Management team and Board of Directors

CXMT's Board of Directors consists of 11 members: 7 non-independent directors and 4 independent directors. The company has no controlling shareholder and no actual controller.

Fig. 36: CXMT: management team and board of directors


Source: Company data, NOM

## Major shareholders (pre-IPO)

CXMT has no controlling shareholder and no actual controller. The shareholding structure is dispersed, with a “four-pillar co-governance” structure comprising state-owned capital, the National IC Fund, industrial capital, and the founding team. The largest shareholder, Qinghui Jidian, is itself a partnership with no single controller – its executive partner Qinghui Changxin (清辉长鑫, 0.01% of Qinghui Jidian) is controlled by Chairman Zhu Yiming, while Xinrui Investment (芯睿投资, 51.09%) is controlled by Hefei Economic Development Zone SASAC, and Changxin Jicheng (长鑫集成, 48.90%) is controlled by Hefei SASAC. Combined Hefei state-owned entities hold approximately 35% of CXMT.

Fig. 37: CXMT: Major shareholders (pre-IPO)


Source: Company data, NOM

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong.

See Disclaimers for NOM Group entity details.
