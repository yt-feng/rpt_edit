你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
## Americas Technology: Hardware: AI Project Pulse: May 2026

## AI Project Pulse

Monthly updates in the AI project space across neoclouds, sovereigns, and enterprise

Explore >

![](images/e0bcec9b415a4abb5c40cce83f2018ad1caeccda79be245eba9590c936185f6b.jpg)

We summarize recent announcements and developments in the AI project space across neoclouds, sovereigns, and enterprise made in May 2026. This represents select project announcements and is not indicative of the total AI infrastructure opportunity.

Key highlights in May 2026 include:

■ Neoclouds expanding software & orchestration layers: Recent neocloud M&A activity (IREN/Mirantis, Nebius/Eigen AI) has been focused on adding vertically integrating orchestration and optimization layers to into GPU compute capacity. This evolution signals a strategic pivot from providing compute capacity (primarily for model building and research labs) to providing the seamless, production-ready infrastructure and managed inference services (essential for scaling enterprise AI workloads).  
- Enterprises demand for on-premise and hybrid AI deployments is broadening. At Dell Technologies World on 5/19, DELL highlighted several on-premise & hybrid infrastructure deployments across industries including manufacturing (Samsung, Mazda), financial services (Hudson River Trading), and healthcare (Eli Lilly’s LillyPod supercomputer).

Neoclouds & data center operators

Headlines presented in reverse chronological order.

IREN enters into \$1.6 bn purchase agreement with DELL (5/26/26): IREN has entered into purchase agreements for \$1.6 bn in air-cooled, Blackwell-based systems, as part of its previously announced 5-year AI cloud contract with NVIDIA.

Key Details: Assuming 14kW per DGX B200 rack, we estimate IREN is acquiring \~26K B200 GPUs (45MW/14kW per DGX B200 rack\*8 GPUS per rack) assuming \~\$500k per DGX B200 rack, which is consistent with the disclosed \$1.6 bn

## Katherine Murphy

+1(212)902-1151

katherine.a.murphy@gs.com

GS & Co. LLC

## Michael Ng, CFA

+1(212)902-8618 | michael.ng@gs.com

GS & Co. LLC

## Zorayda Montemayor

+1(212)357-6403

zorayda.montemayor@gs.com

GS & Co. LLC

purchase price.

Blackstone/Google Announce JV for TPU Cloud (5/18/26): Blackstone and Google have entered into a joint venture to create a new U.S.-based company dedicated to providing compute-as-a-service powered by Google Cloud's Tensor Processing Units (TPUs).

■ Key Details: 500 MW of initial capacity; first capacity expected to come online in 2027 with plans to scale significantly over time; Google will supply hardware, including TPUs, as well as software and service  
■ Size: Initial \$5 billion equity commitment from Blackstone.

Akamai signs \$1.8bn cloud contract with Anthropic (5/8/26): Akamai Technologies has secured a landmark \$1.8 billion, seven-year agreement with Anthropic to provide cloud infrastructure services. Akamai will support Anthropic's need for low-latency AI model deployment across global markets, complementing Anthropic's existing centralized training capacity.

■ Key Details: Cloud Infrastructure Services, edge network with over 4,200 points of presence, Akamai Cloud Inference, and Akamai Inference Cloud utilizing NVIDIA RTX PRO 6000 Blackwell servers and BlueField-3 data processing units  
■ Key Partners: Akamai Technologies and Anthropic  
■ Size: \$1.8 billion commitment over seven years  
■ Location: Global (over 130 countries)

NVIDIA and IREN Announce Strategic Partnership (5/7/26): NVIDIA and IREN have entered into a strategic partnership, targeting the deployment of up to 5 gigawatts of NVIDIA DSX-aligned capacity. The collaboration combines NVIDIA's DSX AI factory architecture with IREN's expertise in power, land, and data center operations to expand access for AI-native and enterprise customers. As part of the agreement, NVIDIA received a five-year right to purchase up to 30 million shares of IREN ordinary stock at \$70 per share, representing a potential investment of up to \$2.1 billion.

■ Key Details: NVIDIA DSX-aligned AI infrastructure, DSX AI factories, integration of compute, networking, software, and power, and a five-year stock purchase agreement for NVIDIA.  
■ Size: Up to 5 gigawatts of infrastructure deployment and a potential \$2.1 billion investment right.  
■ Previously Announced Partners: IREN has previously announced DELL as a key server vendor in its data center build outs.

## GPU-as-a-Service Cloud Vultr Announces Collaboration with SUSE and SMCI

(5/6/26): Vultr has partnered with SUSE (open-source software company that develops and sells enterprise-grade Linux operating systems, cloud computing platforms, and container management solutions) and Supermicro (AI hardware vendor) to debut a unified Cloud-to-Edge architectural framework for global AI scaling. This strategic initiative integrates high-performance hardware, localized cloud infrastructure, and unified Kubernetes management to solve the complexities of operating AI workloads

across distributed environment.

Key Details: Three layers of cloud: (1) Cloud and Near-Edge layer leveraging Vultr's 33 global regions and NVIDIA GPUs; (2) a Metro Edge layer utilizing Supermicro's CPU and GPU-capable edge servers validated with SUSE Linux; and (3) a Control Layer using SUSE Edge for GitOps-driven management of thousands of sites.

IREN acquires Mirantis (5/5/26): IREN has signed a definitive agreement to acquire Mirantis (provider of cloud infrastructure, Kubernetes-based orchestration and enterprise support services) for approximately \$625 million in ordinary shares to enhance its AI Cloud delivery capabilities across its renewable-powered data center portfolio in the U.S. and Canada.

Key Details: The proposed acquisition supports: (1) faster deployment and operation of workloads on IREN's existing GPU infrastructure; (2) improves operational visibility (monitoring, performance, mgmt); (2) Technical support, service delivery; and (4) expanded customer base to emerging enterprise AI workloads.

Nebius agrees to acquire Eigen AI (5/1/26): Nebius has entered into an agreement to acquire Eigen AI, a prominent inference and model optimization company, for \~\$643 million. This strategic acquisition is designed to enhance the Nebius Token Factory by integrating Eigen AI's industry-leading optimization stack with Nebius's global compute capacity and AI cloud platform. The collaboration aims to provide enterprise-grade autoscaling endpoints and fine-tuning pipelines that deliver superior model performance and unit economics for production AI workloads.

■ Key Details: Integration of inference and post-training optimization layers into Nebius Token Factory; support for major open-source models including Llama, Qwen, Gemma, and DeepSeek; and the utilization of advanced techniques such as Sparse Attention (SpAtten) and Activation-aware Weight Quantization (AWQ).

■ Location: Amsterdam (Nebius HQ) and the San Francisco Bay Area (new engineering and research presence).

## Sovereign & Enterprise

Headlines presented in reverse chronological order.

## Spectra Supercomputer at Sandia National Laboratories Achieves Full System

Acceptance (5/18/26): Sandia National Laboratories has achieved full system acceptance for Spectra, its newest Vanguard program supercomputer featuring 128 NextSilicon Maverick-2 dual-die accelerators across 64 compute nodes, to evaluate advanced runtime-reconfigurable architectures for national security applications

■ Key Details: 64 compute nodes, 128 Maverick-2 dual-die accelerators, and runtime-reconfigurable dataflow architecture

■ Key Partners: Sandia National Laboratories, NextSilicon, Penguin Solutions, and the National Nuclear Security Administration (NNSA)

■ Location: Sandia National Laboratories

Australian neocloud Sharon AI signs \$950m cloud deal (5/18/26): Australian neocloud Sharon AI has secured a \$950 million agreement to deploy cloud computing infrastructure across multiple NextDC data centers in Australia for a global technology company over a five-year period.

Key Details: Vast Data's AI Operating System for unified storage, database, compute, and real-time processing; 1,000 NVIDIA B200 GPU supercluster; CSCO Secure AI Factory (previously announced)  
■ Location: Australia (including Sydney, Melbourne, Brisbane, Perth, Port Hedland, Canberra, Adelaide, Darwin, Sunshine Coast, and Newman)  
Timing: Revenue generation expected to begin by the end of Q3 2026, with further deployments in Q4 2026

## Dell highlights several infrastructure enterprise customers across different

industries (5/19/26): At Dell Technologies World 2026 in Las Vegas, DELL made several customer announcements including:

Mistral AI uses Dell AI Factory with Nvidia to support its AI research environment (Dell PowerRack with Dell PowerEdge XE9712 with GB200s; Dell professional services).  
Samsung Electronics uses Dell solutions for semi-conductor design, manufacturing, and automation  
Eli Lilly uses Dell hardware, architecture consulting, and integration support for its LillyPod supercomputer (1,016 Blackwell Ultra GPU supercomputer announced in February 2026). Beyond research, Dell provide on-premise compute, storage, and backups across Lilly's manufacturing footprint (digital twins, simulation).  
Hudson River Trading is using Dell AI factory for its purpose-built AI research data center in Norway (Dell IRSS with Dell PowerEdge XE9685L servers with AMD processors, HGX B200 systems, and Spectrum-X Ethernet networking), as well as standardizing its data foundation on Dell PowerScale with PowerEdge R-series servers.  
Mazda plans to use Dell PowerScale, part of the Dell AI Data Platform, to unify its model-based development and CAD storage environments into a scalable infrastructure designed to evolve into a data lake supporting AI and generative AI workloads.

## Dell announces new hardware and platform solutions to support agentic AI

workloads (5/18/26): At Dell Technologies World 2026 in Las Vegas, DELL made several product announcements including:

(1) Introduce PowerRack: integrated rack-scale solutions (compute, networking, and storage configurations) that are pre-built and validated, with the power and cooling already integrated. Dell PowerRack for compute is available now, while PowerRack for networking will be available in September 2026, and for storage in 2H 2026

(2) Other hardware product launches: Dell Pro Precision 7 R1 (mountable rack workstation), Dell PowerCool cooling distribution unit (CDU) C7000, Powerstore Elite  
(3) Support for agentic AI workloads: Dell now offers support for Nvidia's OpenShell runtime platform, which allows organizations to build, deploy, and govern agents in a secure sandboxed environment. Dell also announced Dell Deskside Agentic AI, to allow enterprise to more securely build and run autonomous agents locally.  
(4) Expanded Dell AI Data Platform capabilities: Enhancements to its orchestration and search capabilities, updates to its SQL analytics platform so it can support Nvidia Blackwell GPUs and the forthcoming Vera CPU, and integrating Dell's storage and search engines with Nvidia Omniverse.  
(5) New AI Ecosystem program: Will provide AI software companies with a structured path to validate solutions on Dell AI Factory infrastructure. Initial ecosystem partners include Google, Hugging Face, OpenAI, Palantir, Reflection, ServiceNow, and SpaceXAI.

## Disclosure Appendix

## Reg AC

I, Katherine Murphy, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Katherine Murphy GS & Co. LLC, Michael Ng, CFA GS & Co. LLC, Zorayda Montemayor GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Distribution of ratings: See the distribution of ratings disclosure above. Price chart: See the price chart, with changes of ratings and price targets in prior periods, above, or, if electronic format or if with respect to multiple companies which are the subject of this report, on the GS website at https://www.gs.com/research/hedge.html.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: Go

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
