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
# China AI Intelligence

# Key themes in H226E: model capability, monetization, and token ROI

## Three key themes

Investor interest in China AI models has increased after the listing of Zhipu and MiniMax in early 2026, with market debates becoming more sophisticated across model iteration, monetisation and competition. We set out three key themes to watch in H226E: 1) while we expect continued improvement in model intelligence led by coding capability, we flag early signs that SOTA models may defend their leadership, thanks to data flywheel and improving user stickiness due to better productisation and the rising adoption of AI in model R&D (e.g. recursive self-improvement); 2) we expect model-layer monetisation to continue to ramp, as coding TAM expands beyond developers, while progress in multimodality may be overlooked; and 3) we expect an increasing focus on token ROI, and the shift of enterprises and users from tokenmaxing to token optimisation should drive tiered demand and widen divergence in the pricing power of state-of-the-art (SOTA) vs. other models, while Chinese models may benefit from this trend given their structural cost efficiency (note).

## Coding remains the clearest path for model intelligence improvement

We reiterate our view that coding is the core capability underpinning model intelligence with a clear path to drive the capability frontier. We view AI coding as among the most tractable domains for RL-based post-training, given its relatively verifiable outcomes, scalable synthetic data and real-task feedback from AI coding agents. We note emerging Chinese AI labs are more proactive in productisation by building coding-agent products/harnesses, which should create a potential data flywheel and improve user stickiness via accumulated project context, skills and preferences. We note rising adoption of AI in model R&D, where stronger coding capability could accelerate model iterations (early progress in recursive self-improvement). This could allow models with SOTA coding capabilities to reinforce their leadership.

## Vast monetisation potential, increasing ROI discipline

On monetisation, AI coding TAM continues to expand, shifting from developer tools into broader productivity tools for knowledge workers, with feature innovation (e.g. app plugins, Claude Tag) to integrate with more workflow and accelerate adoption. Progress in multimodality is also worth noting, with Chinese models demonstrating early leadership in video-generation capability and monetisation (e.g. US\$500m ARR for Kuaishou's Kling in May). As enterprise adoption shifts from tokenmaxing to ROI discipline, we are more positive on Chinese models' global share-gain potential, supported by rising recognition (e.g. GLM-5.2) and visible ROI advantages, especially in high-volume, repetitive coding and agentic workflows. However, we acknowledge compute supply remains the key bottleneck for the pace of ARR ramp-up.

## Diverging valuation among listed companies

The price performances of Zhipu and MiniMax post IPO has shown a widening divergence, reflecting Zhipu's strengthening leadership in SOTA coding models (e.g. GLM-5.2) and clearer monetisation potential in coding use cases. While we do not rule out the possibility of MiniMax catching up in model performance, underpinned by its advantages in compute power access and R&D efficiency, we expect its valuation discount to continue in the near term, while we will continue to monitor inflection in future model iterations. Amid rising token demand, we raise our 2026E revenue/ARR forecasts significantly for both companies. Our PTs for Zhipu/MiniMax is revised to HK \$2,200/HK\$500, from HK\$1,160/HK\$1,000, implying 85x/20x P/ARR based on December 2026E ARR of US\$1.5bn/US\$1.0bn.

## Equities

China

Internet Services

Wei Xiong

Analyst

wei.xiong@ubs.com

+86-21-3866 8883

Kenneth Fong

Analyst

kenneth-kc.fong@ubs.com

+852-3712 3890

Charles Chen

Analyst

S1460524020001

charles-za.chen@ubs.com

+86-21-3866 8907

## COMMENTARY

## Clear path for model capability improvement in AI coding

We believe AI coding is among the most tractable domains for RL-based post-training, given its relatively verifiable outcomes through code execution, unit tests and automated graders, while scalable synthetic data and real-task feedback from coding agents could further support continued model improvement.

We note early adoption of AI coding in frontier model R&D, with stronger coding capabilities potentially helping accelerate future model iterations, forming an early path toward recursive self-improvement (RSI). This is illustrated by Anthropic's latest report, "When AI builds itself", which suggests that coding agents are increasingly being used in AI model R&D, including optimizing code for training small models and running experiments. OpenAI's Codex disclosures also points to a similar trend in internal adoption.

Figure 1: AI coding is moving deeper into frontier model R&D  
![](images/a4e06f09e0723131fd66a980c69e5762db99fb48feb2ab3238c1b5810a646558.jpg)  
Source: Company data

## Productisation and early data flywheel

On top of further developing their base models, we note that emerging Chinese AI labs are becoming more proactive in launching first-party coding agent products/harnesses, including Zhipu's ZCode, MiniMax Code and DeepSeek's reported Code Harness team build-out (news). We believe this could create an early data flywheel, as user interactions and real-task workflows can feed back into model improvement. Meanwhile, accumulated project context, skills and user preferences could also improve user stickiness over time, in our view.

Figure 2: Chinese AI labs are increasingly launching first-party coding-agent products / harnesses

<table><tr><td>Company</td><td>Coding agent</td><td>Launch date</td><td>Coding agent progress</td></tr><tr><td>Emerging AI labs</td><td></td><td></td><td></td></tr><tr><td>Zhipu</td><td>Zcode</td><td>1-Jul-26</td><td>Launched ZCode, a first-party coding-agent / harness product for GLM models. It is positioned as a desktop agent for coding workflows, supporting long-horizon tasks, SSH remote development and mobile control.</td></tr><tr><td>Moonshot AI(Kimi)</td><td>Kimi Code</td><td>May-26</td><td>Released Kimi Code CLI, a terminal-based coding agent that can read and edit code, run shell commands, search files, fetch web pages and choose next steps based on execution feedback.</td></tr><tr><td>MiniMax</td><td>MiniMax Code</td><td>29-May-26</td><td>Renamed its MiniMax Agent desktop app to MiniMax Code, adding a dedicated CLI shortcut and positioning it more clearly as a coding-agent product.</td></tr><tr><td>DeepSeek</td><td>Developing</td><td>20-May-26</td><td>Reportedly started building a native coding-agent product via a new Code Harness team, with the product informally referred to as DeepSeek Code.</td></tr><tr><td>Internet leaders</td><td></td><td></td><td></td></tr><tr><td>Tencent</td><td>CodeBuddy</td><td>9-Sep-25</td><td>Launched CodeBuddy Code, an AI CLI coding agent, adding CLI format to CodeBuddy&#x27;s existing plugin / IDE product suite.</td></tr><tr><td>Alibaba</td><td>Qwen Code</td><td>22-Jul-25</td><td>Open-sourced Qwen Code, a terminal coding agent adapted for Qwen models and agentic coding workflows.</td></tr><tr><td>ByteDance</td><td>TRAE</td><td>Jul-25</td><td>Released TRAE Agent, an LLM-based software engineering agent with CLI support for general-purpose coding tasks and repository-level workflows.</td></tr><tr><td>Baidu</td><td>Comate</td><td>Jun-25</td><td>Released Comate AI IDE, expanding Comate from AI coding assistant toward AI IDE / coding-agent workflows with multimodal capabilities and multi-agent collaboration.</td></tr></table>

Source: Company data

## AI coding TAM expansion continues

We observe that AI coding TAM continues to expand, as coding agents shift from developer tools to broader productivity tools for knowledge workers. OpenAI's latest Codex usage update provides clear evidence of this trend: Codex use started with developers, but as it expanded toward more general knowledge work, non-developer users became the fastest-growing user group. By early Jun-2026, non-developer individual users had increased 137x since Aug-2025, while non-developer organizational users increased 189x and OpenAI's non-developer internal users increased 12x.

Meanwhile, we believe continued feature innovation could further accelerate adoption beyond software engineers. For example, OpenAI's Codex plugins extend coding agents into role-specific workflows across data analytics, creative production, sales, product design, public equity investing and investment banking, while Anthropic's Claude Tag brings Claude into Slack as a team-based agent with access to selected channels, tools, data and codebases. We also observed similar features in China's coding agent products (e.g., Zhipu's Zcode and Kimi Code/Work).

Figure 3: AI coding agent adoption is broadening beyond developers  
![](images/ec1be9b83ce57e4521cb610aa5963a5403d97de5669ede261e4a12cc0b4c2cc3.jpg)

![](images/94f0c30736b8ddc6f1b89a3b8991d9a16d1c495c343b38cdcc08148f9e1f30cd.jpg)  
Source: OpenAI (How agents are transforming work). Note: The above data refers to 28-day active users indexed to 1 Aug. 2025

As enterprise adoption shifts from tokenmaxing to ROI discipline, we are more positive on Chinese models' global share-gain potential, with more visible ROI advantages in coding and agentic workflows, especially for high-volume, repetitive inference tasks, as evidenced by rising integrations across overseas apps and platforms (see our APAC Focus report on China AI models' cost efficiency).

Figure 4: LLM Token Expenditure Index  
![](images/b8d5d9f9500f05d8aebdad1548e0f5e744f00b57b5f33560068f5df0edd487e6.jpg)  
Source: SiliconData. Note: Data as of 1 July 2026. Normalized blended rate drawn from observations across frontier API providers, open-weight inference platforms, brokered dedicated-instance markets and self-hosted reference deployment

Figure 5: China vs US AI model token usage trend on OpenRouter  
![](images/b9c18ca2c4a39322be8a5b903487166d73d89c67f547c8a1c9e1da29ace3de69.jpg)  
Source: OpenRouter. Note: Data as of 1 July 2026

Figure 6: Overseas apps and platforms are increasingly integrating Chinese AI models

<table><tr><td>App / Platform</td><td>Product category</td><td>Key functions</td><td>Timing</td><td>Integration details</td></tr><tr><td>Fireworks AI</td><td>AI inference / model hosting platform</td><td>Open-model AI infrastructure for training / fine-tuning and high-throughput inference, with serverless, on-demand and reserved deployments plus OpenAI / Anthropic-compatible APIs</td><td>Kimi / MiniMax / Qwen: 10-12 Jun 2026; GLM-5.2: 16 Jun 2026</td><td>Fireworks announced day-zero GLM-5.2 availability. Its changelog / model library also lists Kimi K2.7 Code, MiniMax M3, Qwen 3.7 Plus and other Chinese models on the platform.</td></tr><tr><td>Vercel AI</td><td>Developer tool / AI gateway</td><td>Developer AI gateway providing one API key for hundreds of models, unified billing / observability, provider routing / fallback, spend controls, BYOK and drop-in SDK compatibility</td><td>GLM-5.2: 16 Jun 2026; GLM-5.2 Fast via Wafer: 24 Jun 2026</td><td>Vercel added GLM-5.2 to AI Gateway on 16 Jun under model ID zai/glm-5.2. On 24 Jun, it added GLM-5.2 Fast via Wafer, a model inference / hosting platform offering serverless and dedicated inference.</td></tr><tr><td>Cloudflare Workers AI</td><td>Serverless AI / edge inference platform</td><td>Serverless GPU inference on Cloudflare&#x27;s global network, with open-source model access through Workers / API, pay-as-you-use pricing and integrations with AI Gateway, Vectorize and Workers</td><td>16 Jun 2026</td><td>Cloudflare announced GLM-5.2 availability on Workers AI, highlighting agentic coding, function calling and reasoning. The initial context window was 262k, with plans to expand later.</td></tr><tr><td>OG Private Computer</td><td>Decentralised AI compute / verifiable inference</td><td>Decentralised AI compute network for router / direct inference, provider marketplace access, wallet-based settlement, TEE-backed verification and chatbot, image and speech service types</td><td>18 Jun 2026; Kimi added the following day</td><td>OG announced GLM-5.2 availability on Private Computer, highlighting end-to-end encryption for prompts, code and outputs, as well as verifiable compute. Qwen-3.7 Plus was also available, with Kimi 2.7 Code added shortly thereafter.</td></tr><tr><td>Notion</td><td>Notes / AI workspace</td><td>All-in-one workspace for docs, wikis / knowledge base, databases, project management, enterprise search, meeting notes and agents</td><td>Mid-Jun 2026</td><td>Notion announced GLM-5.2 availability, particularly for long-horizon tasks. The model is served through Baseten, which also confirmed that Notion is offering GLM-5.2 via its inference platform.</td></tr><tr><td>Perplexity</td><td>AI answer engine / Enterprise AI / APIs</td><td>AI answer engine and enterprise research platform spanning web research, internal-file / app search, agentic Computer workflows and developer APIs</td><td>Mid- to late Jun 2026</td><td>Perplexity&#x27;s Agent API model list includes perplexity/glm-5.2 and perplexity/kimi-k2.7-code, making both models available through its Agent API.</td></tr><tr><td>Devin / Cognition</td><td>AI coding / software engineering agent</td><td>Autonomous AI software engineer for writing, running and testing code, resolving tickets / bugs, migrations / refactors, PR review, codebase Q&amp;A and engineering support</td><td>24 Jun 2026</td><td>Devin announced that Kimi K2.7 and GLM-5.2 are available in Devin Desktop and CLI.</td></tr><tr><td>Coinbase</td><td>Crypto exchange / digital asset platform</td><td>Retail and institutional crypto / asset trading platform, with custody, staking, payments, wallets, developer infrastructure and onchain services</td><td>Late Jun 2026;</td><td>Coinbase co-founder and CEO Brian Armstrong said the company is experimenting with GLM-5.2 and Kimi 2.7 as default open-weight models through its internal LLM gateway, aiming to reduce AI spend without restricting engineers&#x27; token usage.</td></tr><tr><td>Fello AI</td><td>Multi-model AI assistant / consumer app</td><td>All-in-one AI chatbot app for Mac, iPhone and iPad, with multi-model chat, web search, file / PDF analysis, image generation / editing, multilingual chat and cross-device sync</td><td>25 Jun 2026</td><td>Fello AI 6.7.0 added GLM-5.2, MiniMax M3, DeepSeek V4 and Qwen 3.7 Max, alongside new Podcast and Travel Skills and broader file support.</td></tr><tr><td>Poe / Quora</td><td>Multi-model chatbot / bot platform</td><td>Consumer and developer AI aggregation platform for accessing multiple models / bots, generating text, images, video and audio, web search, multi-bot chat, bot / app creation, workflows and Poe API</td><td>Live on platform; no single announcement date found</td><td>Poe pages show access to GLM-5.2, DeepSeek V4 Flash / Pro. Kimi K2.7 Code, MiniMax M3 and other Chinese models via providers such as Novita AI.</td></tr></table>

Source: Company data

Figure 7: Model intelligence and API prices of key AI models

<table><tr><td>Provider</td><td>Model</td><td>Release Date</td><td>AA Intelligence Index</td><td>Input Price (US$/M tokens)</td><td>Cache Hit Price (US$/M tokens)</td><td>Output Price (US$/M tokens)</td><td>Blended Price (US$/M tokens)</td></tr><tr><td>Zhipu</td><td>GLM-5.2 (max)</td><td>2026/06/16</td><td>51.1</td><td>$1.4</td><td>$0.26</td><td>$4.4</td><td>$0.90</td></tr><tr><td>Zhipu</td><td>GLM-5.1</td><td>2026/04/07</td><td>40.2</td><td>$1.4</td><td>$0.26</td><td>$4.4</td><td>$0.90</td></tr><tr><td>MiniMax</t

[中间内容因长度限制已省略]

 is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
