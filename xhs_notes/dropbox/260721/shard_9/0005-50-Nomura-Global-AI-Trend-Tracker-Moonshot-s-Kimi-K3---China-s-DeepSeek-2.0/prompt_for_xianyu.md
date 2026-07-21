你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
EQUITY: TECHNOLOGY

## Moonshot's Kimi K3 – China's DeepSeek 2.0 moment?

And what are the implications for the global AI supply chain?

Kimi K3 – a 2.8T parameter SOTA open-source LLM launched before WAIC, targeting the frontier position in the endless LLM competitive landscape

On 16 July 2026, the day before WAIC (the World AI Conference, China's flagship AI conference) 2026 opening in Shanghai, Moonshot AI (unlisted), one of the leading AI labs in China, released Kimi K3 (full model weights will be released on 27 July) — a 2.8-trillion-parameter open-source LLM (Large Language Model). Kimi K3 is the largest open-source LLM by far, and its key features include native vision (multimodal) support, 1M-token context, and always-on reasoning. Built on its Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), as well as the scaled-up Mixture of Experts (MoE) architecture (Fig. 1), K3 achieved 2.5x improvement in overall scaling efficiency compared to Kimi K2. On Artificial Analysis's independent Intelligence Index, K3 scores 57, ranking #3–4 among 189 models, behind Claude Fable 5 and GPT-5.6 Sol (a gap Moonshot itself concedes), but at parity with Claude Opus 4.8 and GPT-5.5 (Fig. 2). K3 pricing is USD3/mn token input (USD0.30 cache-hit) and USD15/mn token output, i.e., \~USD0.94 per task — roughly half of Opus 4.8 and a third of Fable 5 (Fig. 3), but \~4x K2.6 (Moonshot's previous flagship model), signaling a pivot from low-cost LLM to high cost-performance LLM.

## How does Kimi K3 change the LLM competitive landscape? Will China's LLM players disrupt global market?

K3's key breakthrough is that the model is engineered for long-horizon agentic work, not just chat. On Moonshot AI's official website, there are use cases on complex agentic task, including an unattended chip-design process in 48-hours, end-to-end knowledge work, in-depth industry research with interactive visualisation. For example, Kimi K3 has now joined a Chinese elite LLM club in the global market, together with Zhipu (2513 HK, Not rated), DeepSeek (unlisted), etc, and their target markets now span the full price stack (premium/economy/low-end), in our view. On cost-per-task, K3 (USD0.94) sits at parity with GPT-5.6 Sol (USD1.04), well below Opus 4.8 (USD1.80) and Fable 5 (\~USD2.75), but far above GLM-5.2 (USD0.32–0.47) and DeepSeek V4 Pro (USD0.04). According to Open Router's statistics, Chinese models already exceed 45% of the global developers' token volume (<2% a year ago, link). We think China's LLM players (including both close-source and open-source) will continue to gain traction in the global market, providing highly cost-efficient models which could fulfil the demand for a wide range of IT workloads. Meanwhile, top tier global LLMs could also accelerate their innovation, targeting the most complex workloads (i.e. science) and maintaining their technology & pricing premium, in our view. Moreover, due to geopolitical risks and the decoupling trend, we think the sovereign AI trend will become more popular, as most countries/enterprises would find it too risky to rely on only a small elite club for all Gen AI workloads in the future. Therefore, we think leading LLM players from both China and US would thrive, as long as they can stay ahead of the technology curve.

Is this DeepSeek moment 2.0? Will global AI supply chain demand be weakened? Our views on computing, networking, IDC/Cloud, and software/application On 17 July, the stock market experienced a significant decline, and although the sell-off already started before the K3 launch, we read the event as another catalyst that fuelled the sell-off, as in our view it might have evoked bad memories about the DeepSeek R1 launch 1.5 years ago (see our report: Our view on DeepSeek LLM). We think the rise of a frontier model from China's AI lab, which has been caught in the supply constraints of advanced chips, cast further doubts about computing power demand in the global AI supply chain. However, we think competition and innovation in the global

## Research Analysts

Asia Pacific Technology

Bing Duan - NIHK
bing.duan1@NOM.com
+852 2252 2141

CW Chung - NIHK
cwchung@NOM.com
+852 2252 6075

Aaron Jeng, CFA - NITB
aaron.jeng@NOM.com
+886(2) 21769962

Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

Donnie Teng - NIHK
donnie.teng@NOM.com
+852 2252 1439

Ethan Zhang - NIHK
ethan.zhang@NOM.com
+852 2252 2157

China Internet & New Media

Jialong Shi - NIHK
Jialong.shi@NOM.com
+852 2252 1409

Rachel Guo - NIHK  
rachel.guo@NOM.com  
+852 2252 1400

LLM market will not stop, as we are getting closer to achieving AGI (Artificial General Intelligence), which could lead to a wider adoption of generative AI application in the consumer and enterprise markets. Both frontier AI labs and the hyperscale AI cloud platform companies might continue to invest in this stage in order to stay in the game, and as tscaling laws continue, we read this competition as a positive for the AI infrastructure value chain.

For the computing segment, we believe pre-training and post-training scaling laws are still effective, and the intense competition between leading LLM players will underpin continued strong demand for advanced computing power. In our recent Asia AI Semi & Server report, we noted that the AI cycle has not reached the cycle peak yet, given hyperscalers' spending upside into 2027F (despite having insufficient FCF), and our global new data center build tracking shows further upside. We reiterate our Buy ratings for: 1) TSMC (2330 TT), AI chip enabler), 2) ASE (3711 TT), upside from WoS and CoW, 3) ASPEED (5274 TT), outright CPU beneficiaries, 4) MediaTek (2454 TT), TPU upside, 5) GWC (6488 TT), SiC opportunities in Feynman, 6) KYEC (2449 TT), beneficiary of AI chip testing, 7) EMC (2383 TT)/TUC (6274 TT), CCL benefiting from AI upgrade trends and more price upside from being one of the major supply bottlenecks, and 8) ZDT (4958 TT), an emerging AI PCB/HDI maker. Our Korea Technology analyst CW Chung also noted that the global memory industry is experiencing a very severe shortage situation due to unprecedented strong demand from the AI industry, and his preferred stock is Samsung Electronics (005930 KS, Buy).

For the networking segment, we believe there are structural winners from the large scale AI factory and demand for super node, and we like: 1) optical transceiver & component leaders Zhongji InnoLight (300308 CH, Buy) and Suzhou TFC (300394 CH, Buy); and 2) optical chip supplier Yuanjie Tech (688498 CH, Neutral).

For the IDC and cloud sector, we like companies which can build a thriving AI cloud ecosystem, such as Alibaba (BABA US, Buy). We also like IDC operators which may benefit from large AI Cloud companies' rising capex, including GDS (GDS US, Buy) and VNET (VNET US, Buy).

For the software and application segment, we think there are still uncertainties about the LLM disruptions, but some vertical leaders which can leverage the Gen AI solutions and strengthen their industry “moat” could stand out in the longer term. We like Kingdee (268 HK, Buy) and Kingsoft Office (688111 CH, Buy) in this sector.

# Kimi K3 at a glance: Architecture, Use cases, Pricing & performance

The first open 3T-class model, built for scaling efficiency

K3 extends Moonshot's run at the open scaling frontier — its models have set the upper bound of open-source LLM's parameters (2.8T), built on Kimi Delta Attention and Attention Residuals, with native vision capabilities and a 1-million-token context window, according to company. According to Moonshot's official website, Kimi K3 is built on its Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), two architectural updates designed to improve how information flows across sequence length and model depth. K3 has also scaled up Mixture of Experts (MoE) sparsity, effectively activating 16 out of 896 experts when paired with a Stable LatentMoE framework. Together with refined training and data recipes, these structural changes yield an approximate 2.5x improvement in overall scaling efficiency compared to Kimi K2, allowing the model to convert compute into intelligence more effectively.

Fig. 1: Kimi K3 architecture  
![](images/937e41c1ba2a9bcb0f0f0e690b2962ac522ce244728eb5be5c5e1f1a9354501b.jpg)  
Kimi K3 architecture: the Stable LatentMoE and KDA modules (left), the AttnRes operation $\alpha$ (top right), and the Block Attention Residuals backbone (right).  
Source: Company data, NOM

On Artificial Analysis' website (link), K3's intelligence score ranked No.3, after the recently released frontier models – Anthropic's (unlisted) Fables 5 and OpenAI's (unlisted) GPT-5.6. Meanwhile, Kimi K3's cost per task was \~USD0.94, lower than the Fable 5's USD2.75 and GPT-5.6's 1.04, but meaningfully higher than its domestic peers (i.e. Zhipu GLM-5.2 was priced at USD0.32-0.47), according to Artificial Analysis.

![](images/f98ecf526c6875cabc5579b9a9acf18f3a56807f065d9e7912f2a0424ab54fc9.jpg)  
Source: Artificial Analysis, NOM

Fig. 3: Capability vs price scorecard — K3 vs. other frontier models

<table><tr><td>Benchmark (harness caveats apply)</td><td>Kimi K3</td><td>Claude Fable 5</td><td>Opus 4.8</td><td>GPT-5.5</td><td>GLM-5.2</td></tr><tr><td>AA Intelligence Index (rank of 189)</td><td>57 (#3–4)</td><td>#1 tier</td><td>K3-tier</td><td>K3-tier</td><td>51</td></tr><tr><td>GDPval-AA v2 (Elo, real occupational tasks)</td><td>1668</td><td>1760</td><td>1600</td><td>1494</td><td>1514</td></tr><tr><td>AA-Briefcase (Elo, long-horizon agent)</td><td>1547</td><td>#1</td><td>below K3</td><td>below K3</td><td>below K3</td></tr><tr><td>AutomationBench-AA</td><td>~53% (#1)</td><td>below K3</td><td>below K3</td><td>below K3</td><td>below K3</td></tr><tr><td>DeepSWE (official leaderboard, mini-SWE-agent)</td><td>67.3</td><td>n/a</td><td>n/a</td><td>n/a</td><td>blog-cited</td></tr><tr><td>Cost per AA task</td><td>$0.94</td><td>~$2.75</td><td>$1.80</td><td>n/a</td><td>$0.32–0.47</td></tr><tr><td>Output speed / verbosity</td><td>62 tok/s; ~2x median tokens</td><td>faster</td><td>faster</td><td>n/a</td><td>n/a</td></tr></table>

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

We think the AI Cloud platforms could benefit from the LLM development trend in three ways: 1) MaaS 

[中间内容因长度限制已省略]

ai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and

employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
