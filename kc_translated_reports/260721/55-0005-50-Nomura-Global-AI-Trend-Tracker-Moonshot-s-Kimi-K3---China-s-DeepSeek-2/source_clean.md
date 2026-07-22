## Moonshot's Kimi K3 – China's DeepSeek 2.0 moment?

Kimi K3 – a 2.8T parameter SOTA open-source LLM launched before WAIC, targeting the frontier position in the endless LLM competitive landscape

On 16 July 2026, the day before WAIC (the World AI Conference, China's flagship AI conference) 2026 opening in Shanghai, Moonshot AI (unlisted), one of the leading AI labs in China, released Kimi K3 (full model weights will be released on 27 July) — a 2.8-trillion-parameter open-source LLM (Large Language Model). Kimi K3 is the largest open-source LLM by far, and its key features include native vision (multimodal) support, 1M-token context, and always-on reasoning. Built on its Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), as well as the scaled-up Mixture of Experts (MoE) architecture (Fig. 1), K3 achieved 2.5x improvement in overall scaling efficiency compared to Kimi K2. On Artificial Analysis's independent Intelligence Index, K3 scores 57, ranking #3–4 among 189 models, behind Claude Fable 5 and GPT-5.6 Sol (a gap Moonshot itself concedes), but at parity with Claude Opus 4.8 and GPT-5.5 (Fig. 2). K3 pricing is USD3/mn token input (USD0.30 cache-hit) and USD15/mn token output, i.e., \~USD0.94 per task — roughly half of Opus 4.8 and a third of Fable 5 (Fig. 3), but \~4x K2.6 (Moonshot's previous flagship model), signaling a pivot from low-cost LLM to high cost-performance LLM.

## How does Kimi K3 change the LLM competitive landscape? Will China's LLM players disrupt global market?

K3's key breakthrough is that the model is engineered for long-horizon agentic work, not just chat. On Moonshot AI's official website, there are use cases on complex agentic task, including an unattended chip-design process in 48-hours, end-to-end knowledge work, in-depth industry research with interactive visualisation. For example, Kimi K3 has now joined a Chinese elite LLM club in the global market, together with Zhipu (2513 HK, Not rated), DeepSeek (unlisted), etc, and their target markets now span the full price stack (premium/economy/low-end), in our view. On cost-per-task, K3 (USD0.94) sits at parity with GPT-5.6 Sol (USD1.04), well below Opus 4.8 (USD1.80) and Fable 5 (\~USD2.75), but far above GLM-5.2 (USD0.32–0.47) and DeepSeek V4 Pro (USD0.04). According to Open Router's statistics, Chinese models already exceed 45% of the global developers' token volume (<2% a year ago, link). We think China's LLM players (including both close-source and open-source) will continue to gain traction in the global market, providing highly cost-efficient models which could fulfil the demand for a wide range of IT workloads. Meanwhile, top tier global LLMs could also accelerate their innovation, targeting the most complex workloads (i.e. science) and maintaining their technology & pricing premium, in our view. Moreover, due to geopolitical risks and the decoupling trend, we think the sovereign AI trend will become more popular, as most countries/enterprises would find it too risky to rely on only a small elite club for all Gen AI workloads in the future. Therefore, we think leading LLM players from both China and US would thrive, as long as they can stay ahead of the technology curve.

Is this DeepSeek moment 2.0? Will global AI supply chain demand be weakened? Our views on computing, networking, IDC/Cloud, and software/application On 17 July, the stock market experienced a significant decline, and although the sell-off already started before the K3 launch, we read the event as another catalyst that fuelled the sell-off, as in our view it might have evoked bad memories about the DeepSeek R1 launch 1.5 years ago (see our report: Our view on DeepSeek LLM). We think the rise of a frontier model from China's AI lab, which has been caught in the supply constraints of advanced chips, cast further doubts about computing power demand in the global AI supply chain. However, we think competition and innovation in the global


Bing Duan - NIHK

CW Chung - NIHK


Donnie Teng - NIHK

Ethan Zhang - NIHK

China Internet & New Media

Jialong Shi - NIHK

Rachel Guo - NIHK

LLM market will not stop, as we are getting closer to achieving AGI (Artificial General Intelligence), which could lead to a wider adoption of generative AI application in the consumer and enterprise markets. Both frontier AI labs and the hyperscale AI cloud platform companies might continue to invest in this stage in order to stay in the game, and as tscaling laws continue, we read this competition as a positive for the AI infrastructure value chain.

For the computing segment, we believe pre-training and post-training scaling laws are still effective, and the intense competition between leading LLM players will underpin continued strong demand for advanced computing power. In our recent Asia AI Semi & Server report, we noted that the AI cycle has not reached the cycle peak yet, given hyperscalers' spending upside into 2027F (despite having insufficient FCF), and our global new data center build tracking shows further upside. We reiterate our Buy ratings for: 1) TSMC (2330 TT), AI chip enabler), 2) ASE (3711 TT), upside from WoS and CoW, 3) ASPEED (5274 TT), outright CPU beneficiaries, 4) MediaTek (2454 TT), TPU upside, 5) GWC (6488 TT), SiC opportunities in Feynman, 6) KYEC (2449 TT), beneficiary of AI chip testing, 7) EMC (2383 TT)/TUC (6274 TT), CCL benefiting from AI upgrade trends and more price upside from being one of the major supply bottlenecks, and 8) ZDT (4958 TT), an emerging AI PCB/HDI maker. Our Korea Technology analyst CW Chung also noted that the global memory industry is experiencing a very severe shortage situation due to unprecedented strong demand from the AI industry, and his preferred stock is Samsung Electronics (005930 KS, Buy).

For the networking segment, we believe there are structural winners from the large scale AI factory and demand for super node, and we like: 1) optical transceiver & component leaders Zhongji InnoLight (300308 CH, Buy) and Suzhou TFC (300394 CH, Buy); and 2) optical chip supplier Yuanjie Tech (688498 CH, Neutral).

For the IDC and cloud sector, we like companies which can build a thriving AI cloud ecosystem, such as Alibaba (BABA US, Buy). We also like IDC operators which may benefit from large AI Cloud companies' rising capex, including GDS (GDS US, Buy) and VNET (VNET US, Buy).

For the software and application segment, we think there are still uncertainties about the LLM disruptions, but some vertical leaders which can leverage the Gen AI solutions and strengthen their industry “moat” could stand out in the longer term. We like Kingdee (268 HK, Buy) and Kingsoft Office (688111 CH, Buy) in this sector.

# Kimi K3 at a glance: Architecture, Use cases, Pricing & performance

The first open 3T-class model, built for scaling efficiency

K3 extends Moonshot's run at the open scaling frontier — its models have set the upper bound of open-source LLM's parameters (2.8T), built on Kimi Delta Attention and Attention Residuals, with native vision capabilities and a 1-million-token context window, according to company. According to Moonshot's official website, Kimi K3 is built on its Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), two architectural updates designed to improve how information flows across sequence length and model depth. K3 has also scaled up Mixture of Experts (MoE) sparsity, effectively activating 16 out of 896 experts when paired with a Stable LatentMoE framework. Together with refined training and data recipes, these structural changes yield an approximate 2.5x improvement in overall scaling efficiency compared to Kimi K2, allowing the model to convert compute into intelligence more effectively.

Fig. 1: Kimi K3 architecture

[[KC_IMAGE_001]]

Kimi K3 architecture: the Stable LatentMoE and KDA modules (left), the AttnRes operation $\alpha$ (top right), and the Block Attention Residuals backbone (right).
Source: Company data, NOM


[[KC_IMAGE_002]]

Source: Artificial Analysis, NOM

Fig. 3: Capability vs price scorecard — K3 vs. other frontier models


Source: Company data, NOM

## Use cases: long-horizon coding, knowledge work, and reasoning

Kimi K3 features include long-horizon coding, Kernel Optimization, Game Dev and Digital Creation, etc, according to the company. Kimi K3 has strong long-horizon coding performance, which can operate with minimal human oversight, sustain long engineering sessions, navigate massive repositories, and orchestrate terminal tools. Kimi K3 also

excels in tasks blending software engineering with visual reasoning, which leverages screenshots and visuals to optimize game dev, frontend, and CAD, according to company.

\- Autonomous coding & systems work. The company showcased several use cases on its official blog for autonomous coding & system work: (i) a 24-hour sandboxed GPU-kernel bake-off across four tasks (AttnRes, KDA, a 512-head-dim MLA kernel) on H200 and an alternative-vendor GPGPU, where K3 was competitive with Fable 5 (with fallback) and substantially ahead of Opus 4.8, GPT-5.6 Sol and GPT-5.5 — notably, an early K3 handled the majority of the team's own kernel-optimisation work; (ii) MiniTriton, a from-scratch Triton-like GPU programming compiler (tile-level IR over MLIR, PTX codegen) built from scratch; and (iii) a 48-hour unattended chip-design run on open-source EDA (Nangate 45nm): $4\mathrm{mm}^2$ , 100MHz timing closure, 1.46M cells, >8,700 tok/s simulated decode for a nano model of its own architecture.

\- Knowledge work. Production-styled cases: an interactive 42-year ASIC-industry research site built over 120+ rounds of recursive self-improvement (2.8k+ web pulls, 87 quarterly reports, 99 PDFs); a 391-event gravitational-wave analysis orchestrating 20+ concurrent subagents; astrophysics code reproduction (I–Love–Q relations) compressing an estimated one-to-two weeks of expert work into \~2 hours; native-multimodal video editing, including cutting its own teaser from 56 source clips.

\- Game Development and Digital Creation. Kimi K3 built a fully procedural browser-based 3D exploration game using Three.js WebGPU and GPU compute. It procedurally generated the environment, while using a 3D asset generation tool to create the rider and horse models, producing an expansive open world with forests, a log-cabin village, snowy mountains, and dynamic weather.

## AI supply-chain impact: Global and China

We think the rise of a frontier model from China's AI lab, which has been caught in the supply constraints of advanced chips, cast further doubts about the computing power demand in global AI supply chain. However, we think competition and innovation in the global LLM market will not stop, as we are getting closer to achieving AGI (Artificial General Intelligence), which could lead to a wider adoption of generative AI application in the consumer and enterprise markets. Both frontier AI labs and the hyperscale AI cloud platform companies might continue to invest in this stage in order to stay in the game, and as scaling laws continue, we read this competition as a positive for the AI infrastructure value chain.

## Compute: scaling laws still effective, inference workloads to gain momentum

We think Kimi K3's success story does not weaken the demand for LLM training; instead, it strengthens the pre-training and post-training scaling laws, as more computing power may lead to better performance. As LLM models have yet to reach its performance limits, we think the demand for advanced computing power would remain buoyant in the global AI supply chain. Specifically, we think leading LLM players would accelerate the migration to most advanced GPU or ASIC platforms, in order to differentiate the performance of their frontier models. As leading LLMs like Kimi K3 expand their business frontiers, we think inference workloads will gain momentum, and the ASIC supply chain may continue to benefit from this trend. We reiterate our Buy ratings on: 1) TSMC (2330 TT), AI chip enabler), 2) ASE (3711 TT), upside from WoS and CoW, 3) ASPEED (5274 TT), outright CPU beneficiaries, 4) MediaTek (2454 TT), TPU upside, 5) GWC (6488 TT), SiC opportunities in Feynman, 6) KYEC (2449 TT), beneficiary of AI chip testing, 7) EMC (2383 TT)/TUC (6274 TT), CCL benefiting from AI upgrade trends and more price upside from being one of the major supply bottlenecks, 8) ZDT (4958 TT), an emerging AI PCB/HDI maker. Our Korea Technology analyst CW Chung also noted that the global memory industry is experiencing a very severe shortage situation due to unprecedented strong demand from the AI industry, and his preferred stock is Samsung Electronics (005930 KS, Buy).

## Networking: structural winner from the large scale AI factory and demand for supernode

Kimi K3 has demonstrated strong potential for long-horizon coding / agentic work, as well as multimodal applications (visual design, game development, digital creation, etc), which are heavy token consumption workloads. We think the rising adoption for large scale AI

factories will underpin the strong demand for advanced networking technologies and solutions, which play crucial roles in the large AIDC clusters. More specially, for China's AI supply chain, the SuperNode has become in important trend, which helps to close the gap of China's sub-optimal computing chip performance with global peers, leading to structural growth opportunities for the networking solution providers in China. We like Zhongji InnoLight (300308 CH, Buy), Suzhou TFC (300394 CH, Buy) in the global AI networking sector.

## IDC & AI Cloud platforms: hosting more frontier models leading to thriving ecosystem

We think the AI Cloud platforms could benefit from the LLM development trend in three ways: 1) MaaS (model-as-a-service) demand (most customers for the LLMs will consume the model / tokens from one or multiple cloud platforms); 2) stronger bargaining power (as they host a wide variety of advanced open-source LLMs) versus the exclusive closed-source model players; and 3) higher margin expansion potentials, as the AI cloud platforms provide a strong ecosystem, which not only include cloud infra, LLMs, but also application & services layers, which could fulfil the customized needs in private deployment and compliance requirements. We like Alibaba in China's AI Cloud ecosystem, and we also like GDS / VNET as the winners in China's IDC sector, as they benefit from the rising demand for IDC infra from frontier model companies' training and inference workloads.

## Software & applications: still uncertainties due to LLM's disruptions, but companies with stronger "moat" will stand out in longer-term

The software and application market is still under pressure due to market concerns about LLM disruptions. We think the advancement of frontier LLMs may help to lower the entry barriers for small AI startups or enterprises to develop their own AI applications and software, by leveraging the coding and agentic solutions, thereby curbing the competitive edge of many incumbent companies which make general-purpose software and applications. However, we believe vertical leaders which can adapt to the Generative AI market will eventually stand out, and become AI winners in the longer term. We like Kingdee (268 HK, Buy) and Kingsoft Office (688111 CH, Buy) in China's software sector.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.
