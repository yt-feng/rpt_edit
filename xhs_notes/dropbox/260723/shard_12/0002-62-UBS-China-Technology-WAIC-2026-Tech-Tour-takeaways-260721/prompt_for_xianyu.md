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
## China Technology WAIC 2026 Tech Tour takeaways

## Strengthening AI ecosystem and tech supply chain capability

UBS's World Artificial Intelligence Conference (WAIC) 2026 Tech Tour concluded last week. We held C-level/IR meetings with 12 companies in LLM (MiniMax, Zhipu, Phancy and Xunce), GPU (Biren), networking (Montage and Xizhi), analog (Southchip and Dosilicon), OSAT (JCET), ODM (Huaqin) and semi equipment (PowerTech). We made multiple booth visits and attended keynote events. Notable takeaways: 1) strong interest: over 40 institutional investors participated in our tour and reportedly over 1,100 exhibitors and 400k+ attendees participated in WAIC 2026; 2) Global collaboration: China announced the creation of WAICO (World Artificial Intelligence Cooperation Organization), involving 29 countries, and signed initiatives on AI governance. China signed cUS\$3bn of new contracts with overseas companies; 3) rapid progress in China LLM iteration, including Kimi K3 and Qwen 3.8-Max models; 4) evolving domestic AI infrastructure offerings including super computing (e.g. Biren), SuperPod (e.g. Huawei, Huaqin) and networking (e.g. Xizhi); and 5) positive feedback from supply chain on AI infra related end demand. The tour strengthened our confidence and improved visibility on rapid growth for China's major AI tech supply chain companies in 2026E and beyond.

## WAIC 2026: major AI related hardware/semi products/solutions showcased

AI infra computing and SuperPod. Huawei brought its Atlas 950 SuperPod with 1,024 chips. Sugon showcased its SuperPoD solution, Sugon 8000, which enables 100k-chip interconnect. Other SuperPod products released includes MetaX (XiJing S600), ZTE (OEX), and Alibaba (Panjiu AL128 empowered by Zhenwu M890), etc. Networking. Xizhi released a 51.2T CPO switch prototype and brought its full-stake optical interconnect solution. Applications. We noted edge AI applications across AI smartphone (ZTE's Nubia), AI workstation (eg. Moore Threads' AIBOOK), autonomous driving (eg. MetaX's robotaxi solution, BYD's self-designed Xuanji A3) and robotics.

## Key takeaways from tech supply chain companies

Compute. Chinese AI accelerator companies noted stronger demand from domestic customers (including CSPs), due to tight supply in China and domestic CSPs willingness to adopt domestic computing cards. For tier-2 AI accelerator suppliers, most are working on H100/H200 equivalent chips and iterate the SuperPod technology to overcome the challenges of single cards. Networking. Montage said DDR5 Gen3/4 memory interface chip contributions continue to increase in 2026, with Gen5 chip shipments likely in H226. The company flagged rising demand for CXL/MRDIMM from end customers. Advanced packaging. Including the ramp-up of its advanced packaging fab (JME) in Jiangyin, JCET recently announced it would build an advanced packaging fab in Shanghai with a total investment of Rmb7.8 bn, implying a strong demand outlook. The company is upbeat on the AI power related packaging business for overseas and domestic customers and expects total TAM to increase multiple times in 2025-27F. Analog. Southchip noted muted demand from consumer electronics applications, while it is building advanced analog solutions to fulfil AI power and memory applications. Server ODMs. Huaqin reported stronger demand for data centre applications in 2026, mainly driven by switches, AI servers and SuperPod deployment.

## Stock recommendations

Within China AI LLM, our top pick is Zhipu (positive fundamentals and an attractive valuation) and we have a Buy on MiniMax. In the AI related Chinese tech semiconductor supply chain, we prefer UBS APAC Key Call NAURA (Buy; WFE localisation), JCET (advanced packaging) and Han's Laser (PCB equipment). In China's hardware supply chain, we prefer Apple related companies Luxshare, Lens Tech and AAC.

## Equities

China Semiconductors

Jimmy Yu
Analyst
jimmy.yu@ubs.com
+86-21-3866 8880

Wei Xiong
Analyst
S1460518100005
wei.xiong@ubs.com
+86-21-3866 8883

Yongwei Lai
Analyst
S1460524110001
yongwei.lai@ubs.com
+86-21-3866 8780

Xinlei Li
Analyst
S1460522090008
xinlei.li@ubs.com
+86-21-3866 8805

Charles Chen
Analyst
S1460524020001
charles-za.chen@ubs.com
+86-21-3866 8907

Qing Luo
Associate
S1460125090001
qing-za.luo@ubs.com
+86-213-866 5000

Edward Liu
Analyst
edward.liu@ubs.com
+852-3712 3981

## Key takeaways

Figure 1: Companies we met during the pre-WAIC tour and their positions in the AI value chain  
![](images/1d4984d76f16618697bdeb73aab2a4a4e295c5774d1a57b646e7b840b5b44005.jpg)  
Source: UBS-S estimates

## New releases at WAIC 2026

## Computing

## Huawei showcased the Ascend Atlas 950 SuperPoD

\- Huawei showcased the Ascend Atlas 950 SuperPoD at WAIC 2026, positioning it as a next-generation AI infrastructure platform for trillion-parameter model training and inference. Built on Ascend 950PR chips and the UnifiedBus interconnect architecture, the 1024-card SuperPoD delivers 1 EFLOPS FP8 and 2 EFLOPS FP4 compute, and provides 256TB of unified memory addressing. Its high-bandwidth (TB-level) NPU interconnect and ultra low latency (3μs) help remove communication bottlenecks across compute and memory resources, making it better suited for Agentic AI workloads, MoE models, long-context inference and low-latency serving.

\- Huawei also highlighted its open software ecosystem, including CANN and Mind-series software, with 67 community projects, over 12.44 million lines of code and 3,500 monthly active developers.

\- Commercially, Huawei said that over 750 Ascend 384 SuperPoD systems have been deployed across verticals including internet, telecoms, finance, education, healthcare, transport and manufacturing.

Figure 2: Huawei's SuperPod roadmap

<table><tr><td></td><td>Cloud Matrix 384</td><td>Atlas 950 Server</td><td>Atlas 950 SuperPoD*</td><td>Atlas 950 SuperPoD**</td><td>Atlas 960 SuperPoD</td></tr><tr><td>Launch time</td><td>2025</td><td>2026</td><td>2026</td><td>2026</td><td>2027</td></tr><tr><td>Num. of accelerator</td><td>384</td><td>64</td><td>1,024</td><td>8,192</td><td>15,488</td></tr><tr><td rowspan="2">Computing power</td><td rowspan="2">300PFLOPS (BF16)</td><td>64PFLOPS(FP8)</td><td>1EFLOPS(FP8)</td><td>8EFLOPS(FP8)</td><td>30EFLOPS(FP8)</td></tr><tr><td>128PFLOPS(FP4)</td><td>2EFLOPS(FP4)</td><td>16EFLOPS(FP4)</td><td>60EFLOPS(FP4)</td></tr><tr><td>Memory bandwidth</td><td>3.2TB/s</td><td>4TB/s</td><td>4TB/s</td><td>4TB/s</td><td>9.6TB/s</td></tr></table>

Source: Company data. \* Exhibited version at WAIC 2026. \*\* Maximum version released by Huawei

AI accelerator design companies, including Hygon, MetaX, Moore Threads and Enflame, showcased rack-level scale-up solutions.

## Networking

Xizhi, together with Centec, released a 51.2T CPO switch prototype based on the domestic supply chain. The company also exhibited other optical interconnect solutions, such as NPO and full-optical interconnect SuperPoD.

KiwiMoore showcased its SuperPod interconnect solutions, including Scale-out interconnect, Scale-up XPU interconnect and optical interconnect full-stack solutions (e.g. NPO). The company also released its direct interconnect solution between domestic GPU and domestic RDMA network cards and IBGDA solutions in cooperation with Biren Technology, a domestic GPGPU design company.

Besides, server/solution providers, including Sugon, ZTE, Sugon, Ruijie and Unisplendour also brought their SuperPoD solutions to the exhibition.

## Edge AI

ZTE brought its AI smartphone cooperated with ByteDance, Nubia, to the booth. The AI-native smartphone is empowered by Doubao large model. Moore Threads showcased its AI Cube, AI laptop and agentic OS system, empowered by its self-designed SoC with 50TOPS (@INT8) computing power. Rockchip displayed its main control chips, AI co-processor chip and self-designed RKNN3 Toolkit at WAIC 2026, and showcased its edge AI applications, including AI-empowered TVs and AI Cubes.

Together with CalmCar, a China auto intelligence solution provider, MetaX released a L4 robotaxi auto intelligence solution based on MetaX's GPGPU products. Shenji showcased its edge AI SoC product portfolio, including SoC for advanced autonomous driving (L2++), with NIO as the major customer, along with solutions for pan-"Physical AI" applications including robotics. Black Sesame brought its edge AI SoC product portfolio, including A200 series and C1200 series, to WAIC. BYD showed its in-house designed AD SoC, Xuanji, a 4nm chip with 700 TOPS computing power.

## Key takeaways from corporate meetings

## LLM and related companies

## Knowledge Atlas Technology/ Zhipu (2513.HK, Buy)

\- ARR ahead of plan with recent H-share placement to support compute ramp-up. Management said that Zhipu's ARR (annual recurring revenue) reached US\$1bn as of July, ahead of its internal 2026 year-end target, supported by both rapid token usage growth and API price increases. While compute power remains the key constraint, management believes the recent H-share placement (HK \$31bn) could drive further compute expansion, and also considers compute leasing as a way to leverage larger-scale compute resources.

\- Price increases and inference optimisation to support margin expansion, while compute cost uncertainty remains a swing factor. Management indicated that API price increases and continued efforts on inference optimisation could support margin expansion, while acknowledging that the pace of margin improvement remains subject to compute leasing cost uncertainty, especially given tight domestic compute supply and rising rental prices.

\- Pursuing frontier model capability remains a key priority. Management reiterated that pursuing frontier model capability remains a key priority. Beyond parameter scaling, management also identified broader dimensions of scaling to support further intelligence improvement, including data, infrastructure and hardware capability.

## MiniMax (0100.HK, Buy)

\- Accelerating ARR ramp amid strong API demand. Management said MiniMax's ARR continued to ramp quickly, from cUS\$100m at end-2025 to cUS \$150m announced at the Q1 earnings call, more than doubling before the M3 release, with management remaining confident in achieving its US\$1bn ARR target by end-2026. This was mainly driven by rapid growth in the API and Token Plan business, while 2C subscription revenue also remained solid. As a result, revenue contribution from API/Token Plan increased to nearly half of total revenue in May, vs c.30% in 2025.

\- Multiple inference optimisation efforts to support healthy gross margin. Although MiniMax's latest flagship text model, M3, has nearly doubled parameter size vs. the M2.7, management said gross margin could remain healthy supported by continued inference engineering optimisation and refined cluster operations, in addition to benefits from early compute procurement.

\- Scaling up parameters further to pursue better model capability. With the proven path of parameter scaling from M2 to M3, management plans to scale up model parameters further and better leverage its compute resource advantages. In addition, management emphasised further model capability improvement through post-training, especially in coding capability.

## Phancy (6288.HK, Not Rated)

\- Well positioned for the AI industry tailwind as an AI infrastructure layer for heterogeneous compute optimisation. Management has positioned as an enterprise AI infrastructure provider, with core capabilities in pooling, orchestration and scheduling of heterogeneous compute. Management believes the company is well positioned to capture industry tailwinds from rapid AI compute demand growth and the rising need to manage heterogeneous compute resources, especially in China's domestic chip environment. Its Hami vGPU and ModelHub are the two key building blocks: Hami improves GPU / accelerator utilisation through virtualisation, pooling, slicing and memory overcommit, while ModelHub helps adapt and accelerate open-source models on domestic chips.

\- Token factory opportunity driven by rising demand for lower cost, higher quality token output. In the context of enterprises shifting from token maximising to more ROI-focused AI deployment, Phancy aims to help cloud providers, AIDC operators and enterprise customers convert physical compute into high-quality token output more efficiently. The company's public cloud / API business is positioned as a "token factory", while its private cloud / AI Platform helps enterprises deploy and manage AI infrastructure with better utilisation and lower hardware waste.

\- Neutral ecosystem positioning and standardised delivery as differentiators. Management identified Phancy's neutral positioning as a key advantage in serving enterprise customers as it is not tied to any single model vendor or chip vendor, allowing it to match customer workloads with the most suitable models and compute resources. This is especially relevant in China's heterogeneous domestic compute environment, where different chips and software stacks are often difficult to manage together. Management also highlighted improving standardisation in private cloud delivery, with most platform deployments now delivered in a more scalable and repeatable way, supporting better operating leverage over time.

## Xunce (3317.HK, Not Rated)

\- Expanding from financial real-time data infrastructure to cross-industry data tokenisation. Management has positioned Xunce as an AI real-time data infrastructure and analytics provider, helping enterprises govern, standardise and process private-domain data, then convert it into vertical scenario tokens for large-model applications. The company started from financial / asset-management scenarios, where real-time accuracy and regulatory requirements are high, and has since expanded into other industries including healthcare, pharma, manufacturing, energy and telecoms. Management views its role as supporting enterprise AI adoption by connecting private data, business rules and workflow context with general-purpose models.

\- Token OS enables more measurable and auditable enterprise data usage. Xunce's Token OS converts raw enterprise data into scenario-specific tokens that embed private know-how, permission rules and business workflows, before these tokens are used by customer-selected models or agents. Management noted that tokenisation can make enterprise data usage more measurable and auditable, helping customers trace token consumption and value generation across workflows.

## AI hardware/semiconductor supply chain

## Montage (6809.HK, Buy/688008.SH, Not Rated)

\- Demand remains strong, while the near term upside could be capped by supply constraints in upstream packaging materials, such as BT substrate and e-glass cloth, while management expects the tightness to gradually ease from H226 although a tight balance should persist in the near term.

\- Product wise, for RCD management expects a rapid ramp for DDR5 Gen3 and Gen4, with shipments of Gen5 starting in Q2. Among new product lines, MRCD/MDB (for MRDIMM) have become the key revenue contributors, although management expects meaningful volume growth when next-generation X86 CPU platforms ramp, likely in late 2026 or early 2027. Management has been engaged with certain ARM-based customers on MRDIMM adoption, while viewing SOCAMM as complementary rather than competitive with MRDIMM remaining the mainstream server memory solution due to its superior capacity and bandwidth. Management expects PCIe retimer to continue benefiting from rising 8-card AI server demand, with PCIe retimer 6.0 qualification progressing well ahead of next-generation CPU launches and potentially offering more opportunities in overseas markets. CXL MXC remains the key focus. Montage is working closely

[中间内容因长度限制已省略]

d not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/e7d73d788b460864f9c471ad9a3531c1decc067a331993c5000a2d268134291b.jpg)
"""
