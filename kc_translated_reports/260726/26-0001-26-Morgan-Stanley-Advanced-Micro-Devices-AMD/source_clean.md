# AMD advancing AI event recap and takeaways

With customer announcements earlier this week, the breaking news from the event was a substantial increase in TAM forecast for GPU and CPU; customer testimonials point to confidence on Helios, in a very positive event.

## Key Takeaways

2030 server CPU TAM increased to \~\$220bn (50% CAGR), up from \$120bn on the last earnings call (35% CAGR), and \$60bn (18% CAGR) at the Analyst Day last year.

\- Announced new collaboration with Cerebras for disaggregated inference, and should be an interesting alternative to Nvidia+Groq.

Helios adoption appears to be progressing smoothly at key customers, with coding agents a clear accelerant to the AMD GPU ecosystem.

The extent of demand growth in CPUs was the most bullish datapoint from the event, an area where AMD has clear leadership today.

Customer testimonials reinforce a strong ramp for Helios into 2027, but longer-term competitiveness vs market leaders will take time. AMD has tackled some of the most daunting challenges in GPU head on with the acquisition of ZT's rack engineering business, and customer warrant structures that (while expensive) should accelerate adoption to some extent. We expect AMD to do well, but still don't see it in the lead in this generation. Meanwhile, CPU strength is evident, and the company's market share confidence is noteworthy.

Below, we summarize key announcements from the keynote, and our thoughts on the stock from here.

Compute leadership: Helios, EPYC and Instinct series. AMD officially launched its Helios product, combining 72 Instinct MI455X GPUs with 18 6th Gen EPYC "Venice" CPUs and Pensando NICs. AMD can enable up to $30\%$ more inference tokens per dollar versus Nvidia, enabled by with $15\%$ more compute, $50\%$ more HBM capacity/ bandwidth, and $50\%$ more scale-out bandwidth. Helios is now in full production, with shipments starting end of Q3 and ramping through Q4.

AMD also introduced MI430X, a variant with native FP64 hardware delivering 288 TFLOPS for HPC and sovereign AI workloads – this chip is already part of exascale systems at Oak Ridge National Labs in the U.S. and at CSN/Genci in Europe.

## Cerebras CEO Andrew Feldman announced a joint disaggregated-inference

solution pairing Helios racks with Cerebras' wafer-scale engines, targeting 5x throughput improvement for ultra-low-latency, available later this year via Cerebras Cloud. We are excited for this opportunity for both companies, and the partnership


## Advanced Micro Devices (AMD.O, AMD US)


Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates


e = MS estimates, a = Actual Company reported data

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

could be key to taking on NVIDIA, which will be able to offer integration between standard GPUs and SRAM-based approaches through its Groq acquisition.

On CPUs, 6th Gen EPYC "Venice" ships in three variants tuned for different server classes: Venice HF for GPU host nodes, a 256-core version for "agent sandbox" workloads (density-optimized, up to 512 threads/socket), and a 128-core version for general enterprise servers. AMD is citing up to 1.8x higher performance than Turin, more than 2x agents per watt versus x86 competition, and up to 3.3x rack-level performance per watt versus competing Arm CPUs. A representative from Meta was on stage to discuss a fourth consecutive EPYC generation and described MI300/350/450 as a progressively deeper co-design relationship.

Roadmap, AMD also gave some additional color on the next products in the roadmap: Zen 7-based "Florence," "Ferrara" and "Fidenza" CPUs in 2028, Zen 8-based "Ravenna" in 2030; MI500 series GPUs in 2027 (>2,000x inference performance improvement over four years) and MI600 in 2028; and Helios 500 and Helios 600 rack platforms tied to those GPU generations.

Open platforms: ROCm and ROCm.ai. AMD introduced rocm.ai, an agentic layer on top of ROCm intended to let existing coding agents (Claude, Codex, Cursor) understand AMD hardware and ROCm natively, automating kernel selection, tuning and optimization. AMD demoed a 38% tokens-per-second improvement optimizing MiniMax M3 on MI355 and cited 2.4x average training speedups and a 3.3x inference speedup on DeepSeek models versus ROCm 7. AMD emphasized that ROCm releases now ship every six weeks rather than every four months, and highlighted default enablement across Hugging Face, PyTorch, JAX, vLLM and SGLang. We heard specially from a number of AMD's instinct customers about the strides they have been able to make with AMD hardware as a result of AI.

Powering AI everywhere: enterprise, client and physical AI. For enterprise, AMD launched the air-cooled MI350P, intended to compete with Nvidia RTX 6000. The company showed an internal LLM query routing use case between MI350P and EPYC that enabled a 4-3% token cost reduction. AT&T's CTO was on stage to discuss the launch of Otel 2.0, an open-source telecom model trained on AMD hardware.

On the client side, AMD launched Ryzen AI Halo (120GB unified memory, supporting models up to 200B parameters) and previewed "Gorgon Halo" (192GB unified memory, up to 300B parameters), bundled with a year of Hugging Face Pro.

For physical AI, AMD introduced the Kria AI system-on-module (built on the new Ryzen AI Embedded X100) and a turnkey Kria AI Robotics Developer Platform, claiming 3.4x better real-time results and 2.3x more concurrent agents than Nvidia's Jetson Thor.

Thoughts on the stock: We like the narrative, but see better risk reward elsewhere. While this isn't the first time that AMD has claimed technology leadership in GPU, Helios does seem to be a step forward, though it will take time for the ecosystem to mature.

Meanwhile, the pace of inflection in server CPU optimism is unprecedented. In October AMD guided to a \$60 bn CPU TAM, then revised that to \$120 in April, then to \$220 today. That pace makes us a bit nervous – after all, if its forecast was that far off 8 months ago we can't really feel certainty – but it certainly points to a very strong 12-month view, and very likely foreshadows very good data center numbers when the company reports. While we probably see a bit more encroachment from ARM-based chips vs the company's commentary, AMD still seems very well poised to gain share both within x86 and overall.

So while EW? We have to consider the very large warrant issuance as a marketing expense, given that the company is up issuing stock to customers, which wipes out most of the profits from GPU for the next few years. It's a worthwhile expense, in our view – ecosystem support is critical and AMD should do whatever it takes – but the stock simply seems very expensive vs. peers such as NVIDIA and AVGO, which have a much more entrenched position, albeit one without AMD's optionality. We are constructive, but with the large move in the stock vs. those peers, we see better alternatives elsewhere.

Exhibit 1: AMD Helios Performance Specs

[[KC_IMAGE_001]]

Source: AMD, MS

Exhibit 2: AMD MI455 performance vs MI355X

[[KC_IMAGE_002]]

Source: AMD, MS

## Risk Reward – Advanced Micro Devices (AMD.O)

Like AMD's position in server, but high AI expectations limit room for upside

## PRICE TARGET \$410.00

Our \$360 PT for AMD equals \~37x base case FY2027e MWEPS of \$11.10, reflecting further share gains at the expense of Intel, and 77% y/y growth in datacenter (\~100% in AI)


Source: Refinitiv, MS


[[KC_IMAGE_003]]


RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

[[KC_IMAGE_004]]

Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

## EQUAL-WEIGHT THESIS

We see continued share gains in notebook and server processors in 2026 and 2027 as AMD continues to execute on its product roadmap. AMD's AI story should gain momentum later this year with MI450 products, but performance leadership will be key. An area where AMD will need to prove they can deliver competitive ROI vs incumbents


[[KC_IMAGE_005]]

Source: Refinitiv, MS

## Risk Reward Themes

View descriptions of Risk Rewards Themes here

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 23 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## BULL CASE

## \$570.00

## \~40x bull case FY2027e MW EPS of \$14.27

Bull case assumes further execution for AMD. In computing and graphics, AMD continues to gain material market share, while both CPU and GPU markets remain healthier than forecasted. AMD solidifies a #2 position in the datacenter GPU market

## BASE CASE

## \$410.00

## \~37x base case FY2027e MW EPS of \$11.10

Further share gains for AMD in server compute and notebook continue to drive growth, further supported by a strengthening AI GPU story

## BEAR CASE

## \$210.00

## \~20x bear case FY2027e MW EPS of \$9.45

AMD loses momentum in AI, and Intel shows signs it's beginning to regain its footing in server. The multiple compresses as they are unable to drive meaningful revenues in AI markets beyond one or two customers

## Risk Reward – Advanced Micro Devices (AMD.O)

## KEY EARNINGS INPUTS


## INVESTMENT DRIVERS

\- AMD continues to execute to its product roadmaps, enabling it to gain share on a smaller R&D budget than INTC

\- AI ecosystem adoption takes time, and we see AMD's early success as more of a testament to the strength of the overall market thus far

## GLOBAL REVENUE EXPOSURE


[[KC_IMAGE_006]]

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS


Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

\- Datacenter GPU outperforms expectations, closing the gap with Nvidia

\- PC and server share gain accelerates; Intel's competitive response is less impressive than expected

\- Server refresh drives datacenter revenue above expectations

## RISKS TO DOWNSIDE

\- Intel's server CPUs in 2027 stifle AMD's momentum and allow it to regain share

• AMD loses graphics share to NVIDIA

• Datacenter GPU underperforms expectations

## OWNERSHIP POSITIONING


Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).


[[KC_IMAGE_007]]

◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

## Risk Reward Reference links

1. View explanation of Options Probabilities methodology -

Options\_Probabilities\_Exhibit\_Link.pdf

2. View descriptions of Risk Rewards Themes - RR\_Themes\_Exhibit\_Link.pdf

3. View explanation of regional hierarchies - GEG\_Exhibit\_Link.pdf

4. View explanation of Theme/Exposure methodology -

ESG\_Sustainable\_Solutions\_External\_Link.pdf

5. View explanation of HERS methodology - ESG\_HERS\_External\_Link.pdf
