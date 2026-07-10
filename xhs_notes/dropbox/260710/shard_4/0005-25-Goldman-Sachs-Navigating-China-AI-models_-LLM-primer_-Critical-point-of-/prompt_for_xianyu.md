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
NAVIGATING CHINA AI MODELS

# LLM primer: Critical point of intelligence for global proliferation

## From DeepSeek's moment last year (on cost efficiency) to Zhipu's GLM moment this year (on model intelligence)

China's AI open-source/open-weight models are reaching a critical point of intelligence performance vs. global proprietary models, with a significant ramp up in domestic enterprise & global SME adoption that will enable a positive data flywheel of further model improvement, in our view. We evaluate How these models achieve such performance at low costs/tight computing resources; Why they pursue an open-source/open-weight approach and how they monetize; What the key addressable markets are, as global enterprises shift from 'token-maxxing' to ROI-first, where we highlight two favored ARR quadrants for Chinese models; and Who the potential long-term winners will be under our Competitive Positioning framework. We note any stricter access to China's future most frontier models for overseas markets, Western markets' policies on China models, and access to high-end computing in model training as three key swing factors/risks to our China AI model token/revenue growth trajectory.

We introduce our Chinese AI model Competitive Positioning framework based on pricing power, cost advantage and financial strength, overlaying with token scale and market share progressions, and identify Knowledge Atlas (Zhipu, initiation) and DeepSeek (private) as the strongest positioned in foundation models, and Bytedance (private) in multi-modal.

Ronald Keung, CFA
+852-2978-0856
ronald.keung@gs.com
GS (Asia) L.L.C.

Damian Xie
+852-2978-1398
damian.xie@gs.com
GS (Asia) L.L.C.

Eric Sheridan
+1(917)343-8683
eric.sheridan@gs.com
GS & Co. LLC

Iris Xiao
+852-2978-0202
iris.xiao@gs.com
GS (Asia) L.L.C.

Allen Chang
+852-2978-2930
allen.k.chang@gs.com
GS (Asia) L.L.C.

Steve Qiu
+852-2978-2672
steve.qiu@gs.com
GS (Asia) L.L.C.

![](images/1bfc1791e5c812750eb8296124bec5ed4f3a3c1dce818f487154884bcf647c04.jpg)

## □ □ □ □

Lincoln Kong, CFA
+852-2978-6603
lincoln.kong@gs.com
GS (Asia) L.L.C.

Luqing Zhou
+852-3465-4207
luqing.zhou@gs.com
GS (Asia) L.L.C.

Timothy Zhao
+852-2978-2673
timothy.zhao@gs.com
GS (Asia) L.L.C.

Eunice Liu
+852-2978-7472
eunice.liu@gs.com
GS (Asia) L.L.C.

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

## Table of Contents

Dissecting China open-source models unit economics today and path to profitability 4
PM Summary 5
Comparing China’s key LLM players 11
Decoding China’s AI model tokens & our forecasts on token/revenue share 12
How do Chinese models achieve competitive performance at low costs/tight computing resources? 13
Why are Chinese models pursuing an open source/open weight approach, and ways to monetize? 20
What are the key addressable markets, domestically and internationally, and key risks? 23
Who are best positioned to be the long term winners? Introducing our Competitive Positioning framework 26
Foundation models 26
Multi-modal generation models 32
Key upside and downside risks 37
China’s key AI players at a glance 40
Price Target Methodology & Risks 47
Disclosure Appendix 49

![](images/6c8258692efba398aef3e3e5195e50d6b3ab715b4116cbdae74c6254ba03c320.jpg)

![](images/1c1c4ddfe3159cb29c0c99db550d9e86ef948e49a372121f7b3d30454cdaaca4.jpg)  
1) The calculation of China cloud revenues includes Alibaba, Tencent, ByteDance, Baidu, and Kingsoft Cloud. 2) China CSP capex breakdown is based on GS Greater China Tech team estimates; 3) Companies included are for illustrative purposes and may not be an exhaustive list.

Source: Company data, GS Global Investment Research

![](images/c80384e057e7a3d0216b9f2f1190ffd497eb3992556363157f4c3adcdb633102.jpg)

## Dissecting China open-source models unit economics today and path to profitability

Exhibit 1: Unit economics for China's value-for-money agentic model and top performing coding model, vs. hypothetical economics for global SOTA model UNIT ECONOMICS OF TWO-TIERED CHINA AI MODELS (PER 1M BLENDED TOKENS)

## IN ABSOLUTE US\$ BILLIONS

Source: Company data, GS Global Investment Research

We estimate aggregate of US\$10bn ARR for China AI model industry by year-end FY26E; we estimate to reach US\$125bn for FY30E

US\$7bn inference costs for China AI model industry in FY26E, we estimate US\$55bn by FY30E, which translates into hyperscalers'/neo-clouds' revenues

US\$4bn training costs for China AI model industry in FY26E, US\$20bn by FY30E, as model sizes continue to scale up

Negative EBIT margin for China AI model companies in FY26E; we estimate to reach 18% EBIT margin/US\$23bn profit pool by FY30E

## PM Summary

## From DeepSeek's moment last year (on cost efficiency) to Zhipu's GLM moment this year (on model intelligence)

China's AI open-source/open-weight models are reaching a critical point of intelligence performance vs. global proprietary models, with a significant ramp up in domestic enterprise adoption and a proliferation of global consumer and SME demand. In this report, we evaluate How these models achieve such performance at low costs/tight computing resources; Why they pursue an open source/open weight approach and how they monetize; What the key addressable markets are, where we highlight two favoured ARR quadrants and risk factors; and Who the potential long-term winners will be under our Competitive Positioning framework.

We believe Chinese models are reaching a critical ‘good enough’ stage for agentic tasks/specific coding scenarios, and rising fragmentation in China’s AI model landscape (but the strong will get stronger). While pricing power remains strong for models with frontier performance/multi-modal, the lower-end segment is in a price war; nevertheless, Agentic AI is driving explosive demand for these value-for-money models at the lower-end. Access to computing will be a swing factor, where US/China regulations, balance sheet and inference efficiency are key.

Accordingly, we introduce our Chinese AI model Competitive Positioning framework based on pricing power, cost advantage and financial strength, overlaying with token scale and market share progressions, and identify Knowledge Atlas (Zhipu, initiation) and DeepSeek (private) as the strongest positioned in foundation models, and Bytedance (private) in multi-modal.

How do Chinese models achieve competitive performance at low costs/tight computing resources? By leveraging smaller-sized parameter models for equivalent benchmark performance, and Mixture-of-Expert and new architectural innovations. Chinese AI models are bifurcating into a two-tiered market where performance and time to market are key to pricing power, thereby leading to two ‘ARR maximising’ quadrants based on token adoption and pricing. A positive flywheel is taking effect for top Chinese AI models driven by increasing actual real world coding adoption, and reducing their reliance on model distillation practices.

Why are Chinese models pursuing an open source/open weight approach, and ways to monetize? Open source allows for greater flexibility in model training/deployment, and allows for the widest adoption and an open community. We believe open source models' disclosed ARRs are likely understating total deployment and revenue potentials, and we expect more shifts to open weight (with Community License, i.e., commercial terms if for commercial use) among Chinese AI models down the road.

What are the key addressable markets, domestically and internationally, and key risks? We highlight two favoured ARR quadrants and estimate China/China AI models market to see token growth of 25X by 2030E; the coding landscape to consolidate while the agentic/low-end segment could remain fragmented. International (going global) should be a key upside, with the potential for higher pricing and global proliferation, especially in non-US markets as global enterprises increasingly pivot from a token-maxing to a ROI-first model that prioritizes clear task boundaries, number of agents per day, back-end process automation and actual output over pure computational token volume. Key risk factors are market access/anti-distillation and regulations, including any stricter access to China's future most frontier models for overseas markets, access to highest-end leased computing equipment (used for training), market access to western markets, further restriction lists/entity list designations (but this could be positive for China's path to further AI self-sufficiency across software/CPU/ASICs), and competition from SLM/threat from AI architectures.

Who are best positioned to be the long term winners within China's AI model companies? We expect players with the largest ARR scale with a gross margin advantage + financial strength to be the long-term winners. We highlight independent AI model companies mostly stand out in our Competitive Positioning framework in pricing power + cost advantage (in aggregate represent over US\$200bn in implied valuations, based on latest market cap/funding rounds), where Zhipu and DeepSeek are the most strongly positioned in text based foundation models, while ByteDance leads in multi-modal capabilities based on our framework.

## Signposts we are looking for into 2H 2026

\- Harness/agentic applications: We expect China AI model companies to increasingly focus on positioning their harness/agentic applications as key entry points, especially in coding (e.g. Zhipu's ZCode, Tencent's Workbuddy, and Alibaba's Qoder which are aggregate platforms that support the full suite of AI models) as model companies attempt to close the loop in capturing more real-life coding and agentic data for scaling. Co-work and industry expert agentic products could be the next priorities. Enterprises will increasingly focus on overall cost per task instead of headline pricing per token, with an openness to using different models (multiple-models approach).

\- Multiple large parameter high-end coding model launches and potentially stricter access to the most advanced Chinese AI models outside of China: We anticipate multiple new Chinese AI model launches over 2H26 with significantly larger total parameter sizes of 2-5 trillion across Chinese AI model players. Coding/programming segment competition will intensify as Chinese models try to challenge Zhipu GLM's leadership via training on high-quality real-life coding data (where available) and scaling to larger parameter model sizes. We also expect a potential shift from an open-source to an open-weight approach for best-performing models (i.e. from free-for-all use cases to requiring revenue sharing/a take rate for commercial use). The addition of multi-modal/visual understanding will be the next upgrades amongst Chinese AI foundation models (e.g. for GLM, DeepSeek), while MiniMax M3 already excels in these given the multi-modal focus of MiniMax from the start. That said, we note press reports on potential future restrictions on overseas access to China's most advanced AI models (both closed and open source if at the frontier level) as cutting-edge artificial intelligence is increasingly being seen as a critical national asset.

Continued suppressed API pricing for the lower end agentic-focused segment: While DeepSeek recently announced an increase in peak-hour pricing from mid-July, we expect API pricing and therefore gross margins to remain under pressure at the lower-end pricing segment (around US\$0.1-0.2 per 1M tokens) into the second half, as China's AI model players have significant cash buffers post-fund raising to subsidize competitive pricing at zero/negative gross margins in the near term. As a result, we see financial strength as one of the three most important metrics (alongside pricing power and cost efficiencies) in assessing a Chinese AI model company, where cash on hand, net cash as % of assets and valuation multiples will be the critical financial strength metrics for long-term success. This said, we are Buy-rated on MiniMax as the company stands out on cost efficiency/cost advantage metrics under our Competitive Positioning framework. With its M3 model well positioned in the favored ARR maximizing quadrant (attractive pricing + high token volumes), alongside its discounted valuation at 13X P/2026E year-end ARR (vs. China/global peers which command multiples several times higher at similar ARR stage), we believe risk-reward is skewed to the upside and reiterate our Buy rating. Key swing factors for MiniMax to improve its overall competitive positioning will hinge on its pricing power and financial strength. We expect its H3 video generation model performance (imminent launch in a more favorable industry landscape vs. text models) and time-to-market for its next M3 updates (focusing on further coding intelligence level uplift from post-training/reinforcement learning, we estimate over July-Aug, and a larger parameter size M3 model later in 2H 2026) will be the next key drivers.

Multi-modal/video-generation models to see further ARR ramp-up from global adoption: We expect continued healthy industry pricing and gross margins within video generation (unlike foundation text) where key players ByteDance's SeeDance, Kuaishou's (Buy) Kling and MiniMax's Hailuo/upcoming H3 models to enjoy healthy growth over 2H 2026 amid new functionality breakthroughs (combination of video-generation with LLM) and tight computing resources where demand significantly outpaces capacity. According to China news reports like LatePost and 36Kr, ByteDance's Seedance gross margins have been at a healthy $70 \%$ at its latest US $\$ 2$ bn+ ARR run-rate.

We also expect increasing domestic ASICs supply, tighter access to overseas computing resources and potential market access limitations (could mirror TikTok's trajectory where rapid expansion in western markets was followed by more regulations/focus on ensuring data security where computing will have to be conducted within local jurisdictions).

## Our assessment of AI model companies: ARR scale x gross margin advantage + financial strength

■ Largest ARR scale (Token scale x pricing power)

■ Gross margin advantage (Training & Inference efficiency, Technology)

■ Financial strength (Balance sheet, Access to computing)

Accordingly, we lay out our Competitive Positioning framework for AI model players based on quantifiable metrics, 1) Pricing Power (amongst which, based on Time-to-market of model launch, Arena score based on actual usage cases and pricing

level), 2) Cost advantage (based on token volume scale, throughput/cache hit rate, parameter sizes/activation ratio and our estimate of inference gross margins), and 3) Financial strength (based on cash on-hand, net cash as % of assets, and valuation multiples).

Exhibit 2: Competitive positioning framework for AI model players

<table><tr><td>Key themes</td><td colspan="3">Chinese models reaching critical stage of intelligence for wide adoption across agentic tasks/specific coding scenarios</td><td colspan="3">Fragmentation between China AI models but strong to get stronger; pricing power to come from frontier performance/multi-modal</td><td colspan="2">Agentic AI driving higher demand for value-for-money models/SLMs</td><td colspan="2">Access to computing, where balance sheet and inference efficiency are key</td></tr><tr><td>Driv

[中间内容因长度限制已省略]

on, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.

Artificial Intelligence

Ecosystems

The image contains no text. The OCR result "C" is a hallucination and does not correspond to any content in the source image. Therefore, the correct OCR output is an empty string.

Ecosystem of EV

Goldman Research Sachs

## MINDCRAFT: OUR THEMATIC DEEP DIVES

Artificial Intelligence

![](images/68223a269db9efc04510b122112ad7057ca250657dc9496773b3e5bf8b3dea0b.jpg)  
GS Research
Data Trackers  
Humanoid Robots  
Humanoid Robots

![](images/980e84cac52309c704ad87d4d3e0e66c57ad9263ab3b677a606e27c61be56171.jpg)  
Autonomous driving  
China
Self-Sufficiency  
China's Self-Sufficiency

![](images/c48422e8612932af2830476394574c7a77d8b605124bbd350c3539109d0f2e76.jpg)  
China
Biopharma  
Space

![](images/54fd4a25fc80f8cf4f22f4d7ae292913875fedab355b9eb028f7c9e15bd9c56b.jpg)  
China
Consumer  
Navigating
China Internet  
Navigating China Internet
The 'everyday app' battle in eCommerce: food/instant delivery TAM, cross-sell & eventual landscape

![](images/d68f24c46da2020e59897073854ce5fe4361f3dbc3b3b7aad2a449265c7ac33c.jpg)  
CHIPS Act Impact  
Ecosystems of EV

![](images/adabc7cb71b61fed754178a42d21a2a85b6ccd9781cf4a818f8436d63e37f45b.jpg)  
Investing in India

![](images/ed41a01fcb8397e56966841a46841adcbcb55fb9fcd5ba1535eceeccc8039ed2.jpg)  
Ecosystems

![](images/cbd6acbe8f83d9c7b4b4ed84f1d793dd43318d15124477f3483e3643de2b0704.jpg)  
Resurgent Japan  
GS Research Data Trackers

![](images/2e31eb8705225c62b745d42754bccd0d08e7f523ef867e7217d72b232deb4131.jpg)  
Autonomous driving  
China Biopharma  
China Grid Tech

![](images/c45017769fa8d6b22cc1d820a9fc2e51035652aeeefc39b4543418829297363c.jpg)  
Resurgent Japan  
Global Technology Chips Act Impact  
Market Cycles  
China Consumer
Deceleration in consumption growth amid China economy transitioning: A sustainable shift to value-focus and growing global presence

![](images/7019bac37b6e91efec72f429d8a9b0d38876cc6996a9b81a8fb51bd657f66ae9.jpg)  
Investing in India  
China
Property  
Suppy Chain Shifts

![](images/5d5215068fc328c810a8559fc9458adf1e17d5d410debd6eff5ded400cb958e2.jpg)

![](images/786b5060d08bc32549c52b759023ef4ee06a4d63bae235160e261ace38f03d92.jpg)

![](images/ca8e3b7376e3e5ee5748e2a252e4fc3c00ca70f2b978491bc2fab92d8ef81cc6.jpg)

![](images/555aad7b7eb87cc44d8dbb4903a24c664d15ffe026bdb395b883d5484f26a712.jpg)  
Market
Concentration  
Trade and tariffs  
Top of Mind  
Tracking the Consumer

![](images/253899a1c513a5fa4cc8ee3c825a2774923bb7ce2ffbfa8cdff993265db426cf.jpg)

![](images/a2cc3aa38168246e362ea7d408d5aa03ef4889ccd7f2538e34055dcded54e4f3.jpg)  
Asia Economics Analyst: Shifting Tech Supply Chains in Asia — Tracing Macro Evidence  
Korea Value in Action

![](images/dbe24b62899ad4e2d9064ba1e15e7fd64dac0438ea20a4b963a43079c675a34a.jpg)  
Carbonomics  
Trade and Tariffs

![](images/2a8c0fe6e0b7a62dada08968986b95c166784c5024fd804308d747b4456d3281.jpg)  
Market Concentration  
Cybersecurity and Defense  
Computing Advances

![](images/f7ffd10944d93cdbf2a44e619112618aa2cfa87d03f8e3c6621764c301fbe544.jpg)

![](images/d669094ac811a6436280a1a3099eafcc49088fecb7f694a0fd826d103d5f898b.jpg)  
Magnificent 7

![](images/bd1aafa432967a585a8551326804caf72d67b294898e670ecb9fd3c5b0a5160c.jpg)  
The Company's Board of Directors, Inc.  
Top Projects

![](images/8eb15a0913eef606927e60c4527d7314cb5a17bf4eefae671c47b5da1b4c388e.jpg)  
Obesity  
Tracking the Consumer

![](images/61a08cb36c0543f4e6fede80536fd714dc9ae0a238ee7e05a25aef64bdcf2551.jpg)  
Geopolitics  
Korea Value in Action  
Magnificent 7

![](images/1f35d58a67ed07755721445f189def07168db59fda3bd76cf7bfbe179a3c56e1.jpg)  
Cybersecurity and defense  
Understanding China's Statistics

![](images/321cd629f46676902097dc2afb1fd2b28bdafc9a81688c9d944f92f304033dc5.jpg)  
Computing Advances  
ESG

![](images/cd8f5fa7e6e0dd587c2aca7f73d181c0028cffd432370a71784b1b695ec3f467.jpg)

![](images/aa3e2371b87efd64ec2b3cac1de059243e18173e71e68cb78c4164abc14ff126.jpg)

![](images/8bcad0d3cf915f33db2e08998abd59493c2a5b155727b935c5240c895c908d4d.jpg)

![](images/98ba2d18f8a8a14cf0890d987873f0b8d0e21e17337466324db06f711da14901.jpg)  
Geopolitics  
Understanding China's Economic Statistics Third Edition

![](images/1f380946691f0bc950cad04c21c9caad510d8477a4c93c4f57d55da83c1b331e.jpg)

![](images/c9f2bee900284c56e4ead7cd6327d1b3b31bfb8160216d0c97d8d86133e935fb.jpg)

![](images/25ed8d794806b5c836a1ffad44fc0259a4f854593338ed454e30fe69879d2fd3.jpg)

![](images/6df2154bc6ce6f7c4e13a5e5c69dda42317b5b6fa0266f8bd041018d45c3d05d.jpg)

![](images/20900415a859ab14fc4eb622d94f559bf570a6b5b683ab1ebbf026e556023bc8.jpg)  
GS Research's Theme Bookshelf
"""
