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

<table><tr><td>Provider</td><td>Model</td><td>Release Date</td><td>AA Intelligence Index</td><td>Input Price (US$/M tokens)</td><td>Cache Hit Price (US$/M tokens)</td><td>Output Price (US$/M tokens)</td><td>Blended Price (US$/M tokens)</td></tr><tr><td>Zhipu</td><td>GLM-5.2 (max)</td><td>2026/06/16</td><td>51.1</td><td>$1.4</td><td>$0.26</td><td>$4.4</td><td>$0.90</td></tr><tr><td>Zhipu</td><td>GLM-5.1</td><td>2026/04/07</td><td>40.2</td><td>$1.4</td><td>$0.26</td><td>$4.4</td><td>$0.90</td></tr><tr><td>MiniMax</td><td>MiniMax-M3</td><td>2026/06/01</td><td>44.4</td><td>$0.3</td><td>$0.06</td><td>$1.2</td><td>$0.22</td></tr><tr><td>MiniMax</td><td>MiniMax-M2.7</td><td>2026/03/18</td><td>38.1</td><td>$0.3</td><td>$0.06</td><td>$1.2</td><td>$0.22</td></tr><tr><td>Kimi</td><td>Kimi K2.6</td><td>2026/04/20</td><td>42.8</td><td>$1.0</td><td>$0.16</td><td>$4.0</td><td>$0.70</td></tr><tr><td>DeepSeek</td><td>DeepSeek V4 Pro (peak-period pricing)</td><td>2026/06/29</td><td rowspan="2">31.2</td><td>$0.9</td><td>$0.007</td><td>$1.7</td><td>$0.35</td></tr><tr><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>2026/04/24</td><td>$0.4</td><td>$0.004</td><td>$0.9</td><td>$0.18</td></tr><tr><td>DeepSeek</td><td>DeepSeek V4 Flash (High) (peak-period pricing)</td><td>2026/06/29</td><td rowspan="2">37.4</td><td>$0.3</td><td>$0.006</td><td>$0.6</td><td>$0.12</td></tr><tr><td>DeepSeek</td><td>DeepSeek V4 Flash (High)</td><td>2026/04/24</td><td>$0.1</td><td>$0.003</td><td>$0.3</td><td>$0.06</td></tr><tr><td>Alibaba</td><td>Qwen3.7 Max</td><td>2026/05/19</td><td>46.0</td><td>$2.5</td><td>$0.25</td><td>$7.5</td><td>$1.43</td></tr><tr><td>Alibaba</td><td>Qwen3.6 Max Preview</td><td>2026/04/20</td><td>40.0</td><td>$1.3</td><td>$0.13</td><td>$7.8</td><td>$1.13</td></tr><tr><td>Tencent</td><td>Hy3-preview</td><td>2026/04/23</td><td>26.1</td><td>$0.1</td><td>$0.03</td><td>$0.3</td><td>$0.06</td></tr><tr><td>Anthropic</td><td>Claude Claude Fable 5 (with Fallback)</td><td>2026/07/01</td><td>60.0</td><td>$10.0</td><td>$1.00</td><td>$50.0</td><td>$7.70</td></tr><tr><td>Anthropic</td><td>Claude Sonnet 5 (max) (through August 31, 2026)</td><td>2026/06/30</td><td>53.4</td><td>$2.0</td><td>$0.20</td><td>$10.0</td><td>$1.54</td></tr><tr><td>Anthropic</td><td>Claude Sonnet 5 (max) (starting September 1, 2022)</td><td>2026/06/30</td><td>53.4</td><td>$3.0</td><td>$0.30</td><td>$15.0</td><td>$2.31</td></tr><tr><td>Anthropic</td><td>Claude Opus 4.8 (max)</td><td>2026/05/28</td><td>55.7</td><td>$5.0</td><td>$0.50</td><td>$25.0</td><td>$3.85</td></tr><tr><td>Anthropic</td><td>Claude Opus 4.7 (max)</td><td>2026/04/16</td><td>53.5</td><td>$5.0</td><td>$0.50</td><td>$25.0</td><td>$3.85</td></tr><tr><td>Anthropic</td><td>Claude Sonnet 4.6 (max)</td><td>2026/02/17</td><td>47.2</td><td>$3.0</td><td>$0.30</td><td>$15.0</td><td>$2.31</td></tr><tr><td>Anthropic</td><td>Claude 4.5 Haiku</td><td>2025/10/15</td><td>23.7</td><td>$1.0</td><td>$0.10</td><td>$5.0</td><td>$0.77</td></tr><tr><td>OpenAI</td><td>GPT-5.5 (xhigh)</td><td>2026/04/23</td><td>54.8</td><td>$5.0</td><td>$0.50</td><td>$30.0</td><td>$4.35</td></tr><tr><td>Google</td><td>Gemini 3.1 Pro Preview</td><td>2026/02/19</td><td>46.5</td><td>$2.0</td><td>$0.20</td><td>$12.0</td><td>$1.74</td></tr></table>

Source: Company data, Artificial Analysis. Note: Data as of 9 July 2026. The blended price is calculated using cached input, uncached inpu

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
