## Asian Tech
## 2026 Computex Takeaways Part 1

In this note, we summarize the highlights from NVIDIA's GPU Technology Conference (GTC) and QCOM's keynote sessions at Computex.

\- Few new product introductions, other than the much awaited N1X for Windows PCs, bringing agents to the client device: Overall, the event was light on new product reveals, with NVIDIA announcing its first processor for Windows PCs, N1X or RTX Spark, designed in partnership with Mediatek. This chip has been in the works for \~2 years and should span desktop, notebook and Workstation categories of Windows PCs, bringing high-end token processing capabilities to the PC. NVIDIA envisions this to become a key enabler in bringing AI Agents to client devices with 1 petaflops of AI capability, and the ability to run 120b parameter LLMs at up to 1M context window. We believe the re-imagining of the application suite (for agentic AI) and compatibility of legacy x86 applications (something that has held back Qualcomm's ARM PC growth) are still key factors in determining the success of this product in the medium term. On PCs overall, the key watch point is whether the increasing edge AI adoption will stimulate incremental PC unit shipments. For Mediatek, this is a small (1-2%) revenue driver (largely royalty-based for the ARM CPU and other connectivity chip sales), but it could establish its presence in the Compute space, after its recent success with Chrome/Googlebook. Qualcomm did not introduce any new products during its keynote, with a passing mention of its Dragonfly AI Server racks, likely to be introduced in late June, at its analyst day. Our supply chain checks indicate that Qualcomm's inference-focused ASICs and Datacenter CPUs are likely for Bytedance and one US hyperscaler, with volumes ramping in 2027.

\- Agentic AI workloads as key focus, split between edge and cloud, will be interesting to watch: Both keynotes from NVIDIA and Qualcomm spent a lot of time on agentic AI workloads (as expected), given the rapid rise of AI agents. NVIDIA framed the AI agent as comprising four components—LLM (brain), Harness (body/orchestration), Tools, and Runtime (working environment)—noting that GPUs, CPUs and DPUs are all part of the hardware stack required for agentic AI. In addition, NVIDIA highlighted its move towards being the full-stack enabler of agentic AI infrastructure and software for enterprises (CUDA-X libraries, Nemotron open models, etc., in addition to various forms of compute) and highlighted indicative agentic workloads such as a partnership with Cadence on a chip-design super-agent that accelerates verification cycles by \~40x, from weeks to hours. Qualcomm’s CEO, Cristiano Amon, highlighted the staggering growth in token consumption, projecting a 40x growth from 2026 to 2030. Qualcomm expects agentic AI to redesign how applications are written for personal devices like smartphones and expects agents to work across multiple devices in the future, rather than be tethered to one primary device. Interestingly, QCOM expects agentic AI workload to be distributed between on-device and cloud over time (unlike now, where almost 100% of the AI workload resides in the cloud), which could trigger a replacement cycle for edge devices. Qualcomm indicated that several

## Technology and Telecoms

## Gokul Hariharan AC


JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Albert Hung AC


JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hòng Kong) Limited

## William Yang AC


JPM Securities (Taiwan) Limited

## Jennifer Hsieh


JPM Securities (Taiwan) Limited

## Anthony Leng


JPM Securities (Taiwan) Limited

## Megan Hsueh


JPM Securities (Taiwan) Limited

## David Chou


JPM Securities (Taiwan) Limited

## Jason Chen


JPM Securities (Taiwan) Limited

## Subham Singhania


workloads such as coding/webpage creation could run with 30-60% less tokens and potentially run faster using a device-cloud hybrid approach. In this context, what Apple announces at its WWDC next week could be more important, potentially giving momentum to the idea of a resurgence in edge-based AI compute. In the near term, we believe the quest for faster LLMs is likely to keep most of compute on the cloud.

\- NVIDIA Vera Rubin now in full production, focus on co-design of various rack elements and token maximization: NVIDIA confirmed that Vera Rubin is now in full production, with Microsoft and Dell/CoreWeave already standing up engineering racks. Based on our checks, we believe a larger-scale rack production ramp would likely be in 4Q this year. The production efficiency leap is meaningful—VR racks can now be assembled in approximately 5 minutes compared with 2 hours for the prior Blackwell generation, due to limited cabling and fans, replaced with liquid cooling and a mid-plane PCB for interconnections. The emphasis on Vera Rubin is on the co-design of various compute elements (Vera Rubin, Vera CPU, Bluefield DPU, storage rack, Spectrum SPX rack with Co-packaged Optics, LPX for fast tokens) to enable much higher token throughput (10x higher compared to GB300s) and maximizing revenue per GW. Overall mass production timelines are largely in line with our expectations; we continue to expect Rubin shipments to be constrained by HBM4 supply and minor issues in CoWoS-L packaging through 2026 and expect \~2M units of front-end shipments, which should translate to \~10k racks of VR200 NVL 72 deliveries in 2026 (major vendors such as MSFT/Dell are expected to produce 1-2K in 2026, in our view).

\- Heavy focus on Vera CPU and designing CPUs purpose-built for agentic AI: NVIDIA's CEO Jensen Huang spent significant time detailing the Vera CPUs designed specifically for agentic AI workloads. Vera CPU delivers 1.8x agentic AI sandbox performance versus x86, with the highest instructions per clock (IPC) in the world, per management. The chip is the first to implement PCIe 6 and LPDDR5X memory at 1.2 TB/s, delivering 3x bandwidth both internally and externally while consuming 40% lower peak memory latency. On database workloads, Vera runs SQL 3x faster than x86. NVIDIA appears to be positioning standalone Vera CPU sales as a major incremental growth driver for the company, given the rise in agentic AI workloads. We believe that Vera CPU shipments should start ramping up from 2H26 (we estimate 0.6M units in 2026) but with a strong ramp (3M+ units with potential for upside) in 2027, with packaging solutions coming from TSMC, Amkor, and potentially ASE. Hon Hai and Quanta are likely to be the key standalone rack vendors, with more vendors likely to be added over time. We do expect competition to increase over the next few quarters given the rise of CPU as a new TAM, with Qualcomm and potentially Mediatek entering the fray, along with in-house projects at all major CSPs. For the semiconductor ecosystem (TSMC, OSATs such as ASE, substrate vendors), datacenter CPUs represent a very strong new TAM growth opportunity, adjacent to AI accelerators, which should prolong the supply shortages well into 2027. Meanwhile, for cooling specifically, CPU racks have more cold plates and QDs, potentially benefitting AVC and Fositek, in our view.

\- Moving beyond the compute rack to full-stack infra – NVIDIA launches DSX as a full-stack infra reference design solution to empower AI factories: NVIDIA also launched the DSX platform at the GTC, showcasing its expanded capabilities from chip/rack sales to a reference design for a full AI factory infrastructure, integrating power optimization and infra/platform software. As the capital intensity grows higher than ever (from \$20-30bn per GW in prior generations to potentially \$80-100bn per GW in the future), DSX is intended to improve AI factory efficiency and cost of ownership for CSPs. DSX MaxLPS is one of the highlighted software suites that utilizes 45-degree Celsius hot liquid cooling and optimizes GPU deployment within the same power budget (given NVIDIA believes that today’s datacenters overprovision power by up to 40%), while the DSX Flex platform can help dynamically adjust workloads based on grid conditions. DSX early adopters include CoreWeave and Lambda, among others. Key beneficiaries in the Asian tech supply chains, in our view, include liquid cooling supplier AVC and power supply vendor, Delta.

Note: NVIDIA (NVDA US) is covered by JPM analyst Harlan Sur, and Qualcomm (QCOM US) is covered by JPM analyst Samik Chatterjee.

Companies Discussed in This Report (all prices in this report as of market close on 01 June 2026, unless otherwise indicated) ASE Technology Holding Co Ltd(3711.TW/NT\$601.00/OW), Asia Vital Components(3017.TW/NT\$2,785.00/OW), Delta Electronics, Inc.(2308.TW/NT\$2,420.00/OW), Fositek(6805.TW/NT\$2,120.00/OW), MediaTek Inc.(2454.TW/NT\$4,555.00/OW), NVIDIA Corporation(NVDA/\$224.36/OW), Qualcomm(QCOM/\$228.99/N), TSMC(2330.TW/NT\$2,355.00/OW)
