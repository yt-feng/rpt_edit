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
Global Automation

# Humanoid Robotics: The technology frontier in 2026

![](images/39200ff8b175dcf1642586c9e6b82d56a9341f24b0b2bfe34799545fdb4a72b5.jpg)

Jay Huang, Ph.D.

+852 2123 2631

jay.huang@bernsteinsg.com

![](images/040fc9fe2e4e6f6dd4c71e53cafdf2d80716cf61711d3c4154bc4eed45238c0f.jpg)

Weibin Liang, Ph.D.

+852 2123 2666

weibin.liang@bernsteinsg.com

![](images/664993894069f74ad9aba9f8c139f59cb49d8f5b6f82a988e882ff973c9a9bf6.jpg)

Dien Wang, Ph.D.

+852 2123 2622

dien.wang@bernsteinsg.com

Humanoid robotics is entering a phase of accelerated development and at the threshold of large-scale commercial adoption. This note explains the current frontier of the industry and provides benchmarks for investors to assess progress and the numerous claims made by industry players.

We highlight the frontier and future directions in five dimensions (Exhibit 1), along which, examples of progresses from notable players are shown in Exhibit 2. In locomotion, stable walking on flat surface, which was impressive two years ago, has progressed to motions that require high dynamic full-body control and adaptive interaction with environment. Manipulation tasks have advanced from single-step pick-and-place to increasing dexterity, longer task sequence, and industrial level reliability, although in all these areas, development remains in the early stage. In the level of autonomy, remote control is largely abandoned, and autonomous short-horizon tasks and pre-defined long-horizon tasks are currently the most common. Long-horizon autonomous planning, skill transfer, and task generalization are just emerging and the focus of future development. The robotic brain paradigm has evolved from LLM/VLM to vision-language-action (VLA) models (2024-2025), which are enhanced by World Action Models (WAM) from 2026 onward. Data modality has greatly diversified, and the general trend is to move away from teleoperation (high cost, low efficiency, and hardware dependent) and prioritize egocentric, platform-agnostic data (such as human videos), and the complementary use of non-vision data.

At the center of these progresses is the evolution of robotic brain models to use World Model as the “planner”. In essence, VLA is “language to action”, while WAM is “action based on environmental state, context, and experience”. WAM predicts physically feasible future states (Exhibit 6) and then generates future actions based on those predictions. It is analogous to human brains imagining outcomes before taking actions (Exhibit 4). This way, WAM promises to improve task generalization and performance robustness (Exhibit 8, Exhibit 10, Exhibit 11). Humanoid robot players are quickly embracing the idea of teaching robots to “imagine the future”, by either developing standalone WAM or embedding World Model within an existing VLA (Exhibit 9). Currently, challenges include slower inference speed compared to VLA and the very limited non-vision data such as tactile and material properties to train WAMs.

The rise of WAM may reshape the industry ecosystem and competitive dynamics. WAM emphasizes data diversity with regard to both robot actions and environment. This type of data is more likely to be available from open sources and agnostic of hardware platforms. This potentially lowers the burden of post-training data collected from teleoperation or deployed robots. Therefore, the competitive moat partially shifts from “data ownership” to superior model architecture and data consolidation capabilities. This shift conceivably benefits independent brain / foundational WAM developers such as Physical Intelligence (private) and Nvidia. They will likely complement the brain-body integrated robot OEMs such as Figure AI, Agibot, and LimX (all private). We imagine that robot brain will evolve to be analogous to EV battery and power train — some best OEMs choose to have their own, and the rest find it better to purchase from the best third-party suppliers. The WAM paradigm may also favor players that fill the critical physical data gaps for World Models, such as PaXini (private) in tactile sensing.

![](images/38782f2f4cfa459ec3a26a0a7fc6801339806957ea37f2c18a1211f062ed7533.jpg)

![](images/ad5e5a9ec2e28dfdf56b46ccbf24eeeff691c586272262f24e00563e731a947f.jpg)  
→...  
→...

## DETAILS

EXHIBIT 1: The frontier and future directions in five dimensions of humanoid robots  
![](images/1050445966626f61b8a7f7b8a8e63f05426b6fce29c9f7128f14f32d6fe2c638.jpg)

![](images/839f4703ae58e521d9b78537cbeb3d00d280c9a68b7ce63b5ec6eddb83aef475.jpg)

![](images/b6931bd7cb120e7813a9196a2afff6b020b740832a168f5bec20b28f55ce14c1.jpg)

![](images/49990a83e1c58a8ce9ec24a662fa9b80cb4731878d3a04500e1bdeecc00269c2.jpg)

![](images/cc9508e929782fb59d9809733a1feb59d97ea59b7a41cfb14be7179ee73f88e4.jpg)  
Low-dexterity

Manipulation task

→ Long-sequence

![](images/812abb8453faa77c5886caa7a85fd353a9a0476e7bf561f3af095b322517a05b.jpg)

## Complex & long-sequence

![](images/b718171fa7327531a19e11bc22c64922b12b03577c4cf086efc83634ef15b8b9.jpg)

![](images/9b444cd178666064635d34ec77f21b61e70e54cb37ec9a53bc0330c536cb27f0.jpg)  
High-dexterity

![](images/46b04b98f58eadd12e0a8426aaccd8c4dfdc79030466ef4f5266dcb354156bd8.jpg)  
$\rightarrow$ Reliability of continuous operation

![](images/ac94b30ae89ad6b9e4c11b2b0bb9c9981328f00961d5995779ce7db7d2c88592.jpg)

![](images/580b23cca717964bc6076c9e802b944ace9feca2015e541b69f12469403cd2b8.jpg)

![](images/319080f03a980f262341d83208f1d9543c932b237321283a64e45c00249d136e.jpg)  
→ Shadowing a human

![](images/d7e0470914371971af0d6368e5df8744f9686c02c92d0dd8998319c45cb3a409.jpg)

## Pre-defined task sequence

![](images/8f8fdf44cffd7f4e13b2b3f1e27dba69c1af1bb9f742b9b7d11e261bb8e21c69.jpg)

![](images/e9ef03f04b42a442b8b81e72d5831de2a56038c5a49e23ba2fa1af8f3310c761.jpg)

![](images/d69381263a74590b991918c09c77ae0a630e41aa1b2c18f3491e11fcb58d7122.jpg)

![](images/3f13181735fede48137db31ff036f159dd1a85b86b19d280e9e4ca8037e01968.jpg)

## Transferable and generalizable skill

## Directly trained robotic model

-- Model of Optimus robot, RT-1

## Brain model

## LLM/VLM + separated motion control

Directly use a VLM for high-level reasoning and a separated system for motion control -- SayCan, Text2Motion

![](images/144858c707afa2527b1affe7723a08d95a6d9c5b0fc8e7dc96aa3004e7cd863e.jpg)  
Uses a pre-trained VLM for high-level reasoning, integrated with a motion control system. -- Helix 02, $\pi 0.5$ , GR00T N1

## Vision-Language-Action Model

![](images/af8b57d75747b4ad4b1423e877cf2a610e7d852a95d39b9c954a2f1bb81b18de.jpg)

![](images/17d1767d07b82922f405da132ec945dc22ce75816619f85897f7b2847da97e98.jpg)

## Scene/ environment data

![](images/e20c7dbe8e83959ab5d2c061f8fe7e99dd296704291bf755fcdf0d76b7bcee48.jpg)

![](images/62052ca74cc5557550f82d6dbc0d16e48e3ee6b2abd224267cd3f55d4650b539.jpg)

![](images/fdda30ce3fc4233317905d425f143425123e104b92f89977dd4bea2668b1612e.jpg)

![](images/345ea520809105d26a582f0874beb857def77d3aa3413e2fcd6fe70fa8e6b540.jpg)

![](images/37d32c3a7b5404cc9ee62a16cf9f83c9dd2c4476f89eb9812e2498ffb0c22be6.jpg)

## World Action Model

![](images/fff0f89b2e0af59c2283bb9a1fd29841c7983ad954afcf8862c5e34b4daa0069.jpg)

![](images/4bf4915204e32d25d9ab73ef7b855f8cf08d1d16a888b438880f3ec6addb6cd0.jpg)

Leverages a multimodal model (e.g., a generative video model) as a backbone to predict future states and plan actions accordingly. -- DreamZero, 1XWM, UnifoLM-WMA-0

![](images/38dec4bcec2e438d3239c3216851d94538e0546326a9dd065b978c9939cc8d2c.jpg)

## Robot action data

![](images/61569e91cade39e21974d9c86f03d698f334eb25da6d32b35e8c3135733649b4.jpg)

![](images/cd95a118a83eb1e6cda436f113db8c35493277f475aeca899f3abac38a35e637.jpg)

![](images/188aefc4749dedaf610d3be6c6e72a8629f35060631f945acc2286aa742cb002.jpg)

![](images/a68d2fb35dc8bb9a9824d97f658140341cf7888a216f5fb73e724cccea6fadec.jpg)  
→...  
Source: Unitree, CCTV, Figure AI, academic papers (see detail in the end of this note), Bernstein analysis GLOBAL AUTOMATION

EXHIBIT 2: Examples of latest demonstration in the key frontiers from notable humanoid players

<table><tr><td rowspan="2">Company</td><td colspan="2">Locomotion</td><td colspan="2">Manipulation</td><td rowspan="2">Brain &amp; wolrd model</td></tr><tr><td>High dynamic</td><td>Adaptive</td><td>Dexterity &amp; long-horizon</td><td>Reliability</td></tr><tr><td>Unitree</td><td>Spring Festival Gala  $Peformance^1$ </td><td>Chase wild boars across varied  $terrain^2$ </td><td></td><td></td><td>UnifoLM-WMA-0 model</td></tr><tr><td>Agibot</td><td></td><td></td><td></td><td>Continuous inspection-line  $operation^3$ </td><td></td></tr><tr><td>LimX</td><td></td><td></td><td>Fully autonomous  $housekeeping^4$ </td><td></td><td>COSA 0.5 model</td></tr><tr><td>Paxini</td><td></td><td></td><td></td><td></td><td>Integrates Tactile Simulator into Nvidia Isaac Sim</td></tr><tr><td>Figure AI</td><td></td><td></td><td>Fully autonomous  $housekeeping^5$ </td><td>Continuous package  $sorting^6$ </td><td>Helix 02 model</td></tr><tr><td>Boston Dynamics</td><td>&quot;The Ghost Rabona&quot; — a deceptive football trick  $shot^7$ </td><td>Whole-fridge  $transport^8$ </td><td></td><td></td><td></td></tr><tr><td>Physical Intelligence</td><td></td><td></td><td></td><td></td><td> $\pi_{0.7}$  model</td></tr><tr><td>Nvidia</td><td></td><td></td><td></td><td></td><td>DreamZero model</td></tr></table>

Note: Please see the link of each example by order in the last page of this note. Unitree, Agibot, Paxini, Figure AI, and Physical Intelligence are private. Boston Dynamic is a subsidiary of Hyundai Motor Group which is not covered by Bernstein. Nvidia is covered by Bernstein U.S. semiconductors team.
Source: Bernstein analysis

EXHIBIT 3: Compared to a VLA, world models forecast the outcome of evolution of environment (“predicted observation”), which is used to generate future actions.

![](images/1c256f14fb2e789b3dd5f869e55d70b4fe4d14e13683d016c26444e701dbc130.jpg)  
Source: Bernstein analysis

EXHIBIT 4: WAM is analogous to human brains imagining outcomes before taking actions, while VLA outputs the next action directly.  
![](images/02e3a33df65eb882c50327c5c72f59ef1d8c18aac73495b872f9563eb41f1d39.jpg)  
Source: Bernstein analysis

EXHIBIT 5: Three main types of world models and their applications

<table><tr><td>World model</td><td>“Render”</td><td>“Simulator”</td><td>“Planner”</td></tr><tr><td>Renderingvisual scene</td><td>++</td><td>+</td><td>+</td></tr><tr><td>Predictingfuture states</td><td>+</td><td>++</td><td>++</td></tr><tr><td>Reasoning andaction planning</td><td></td><td></td><td>++</td></tr><tr><td>Models</td><td>SORA, Kling, Veo, Wan-Video</td><td>Cosmos</td><td>DreamZero, 1XWM, UnifoLM-WMA-0</td></tr></table>

Source: Bernstein analysis

EXHIBIT 6: “Render” world models generate visually plausible outputs, while “simulator” and “planner” world models embed learned physical laws to produce physically feasible outputs.

![](images/41af4d61c16ecde0bff7abdc9c1f49025cbcc13eddca72e69905c4f29a6c5589.jpg)  
Source: "PhyGround: Benchmarking Physical Reasoning in Generative World Models" by Juyi Lin and etc., "PhyWorld: Physics-Faithful World Model for Video Generation" by Pu Zhao and etc., Bernstein analysis.

EXHIBIT 7: Diffusion policy models can capture multiple solution modes and select one as the final one, while other model types may collapse toward a single mode or oscillate between modes, limiting task generalization capability.

Task: "Push the T-shape block into the green area"

![](images/ed55a6d790e9e78ac7efd0cfb71bbbf0e044602d2436ab636765391f0653e9cb.jpg)  
Source: “Diffusion Policy: Visuomotor Policy Learning via Action Diffusion” by Cheng and etc., Bernstein analysis

EXHIBIT 8: World Action Models with a diffusion-policy backbone can output physically feasible policies and better handle tasks with multiple valid solutions – such as picking up a mug filled with water.

![](images/bf9ca7b272bd97fc14590c3346dce81331c98c7f7f3079edeaff4a50329ca043.jpg)  
Source: Bernstein analysis

EXHIBIT 9: Evolution of Physical Intelligence's VLA models over time  
![](images/d3ec9bb0e3aff896f427076ba71b8d83b3fdc70ac299d900b8a0276c489a1251.jpg)  
Note: Physical Intelligence is private.  
Source: Physical Intelligence's website and reports, Bernstein analysis

EXHIBIT 10: The adoption of the world model not only improved $\pi 0.7$ 's performance in complex tasks but also enhanced its capability for skill transfer between robots.  
![](images/97e7ae21256d1051ee908ada2b660061da993cf84de5d8da806da51487562a1f.jpg)  
Note: Performance of using subgoal image generation with world model is labeled as $\pi 0.7$ (GC) in the plot. Physical Intelligence is private. Please refer to the following note for a detailed definition of task progress by Physical Intelligence: https://arxiv.org/pdf/2504.16054.
Source: Physical Intelligence, Bernstein analysis  
EXHIBIT 11: With the embedded World Model, π0.7 (GC) breaks strong training dataset biases – trained on “microwave to fridge” and tested on “fridge to microwave”  
Reverse "Fridge to Microwave" task

![](images/67db413ce0beb902d7d397016d56b9b51d87c9d9fd5b96991623d4b8328d3e38.jpg)  
Note: Performance of using subgoal image generation with world model is labeled as $\pi 0.7$ (GC) in the plot. Physical Intelligence is private. Please refer to the following note for a detailed definition of task progress by Physical Intelligence: https://arxiv.org/pdf/2504.16054.
Source: Physical Intelligence, Bernstein analysis

Academic paper as the source for Exhibit 1, as follows: "Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control" by Yitang Li and etc., "Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching" by Zhen Wu and etc., "Learning Getting-Up Policies for Real-World Humanoid Robots" by Xialin He and etc., "RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation" by Xuetao Li and etc., "Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation Tasks" by Lequn Fu and etc., "Path and Motion Optimization for Efficient Multi-Location Inspection with Humanoid Robots" by Jiayang Wu and etc., "LESSMIMIC: Long-Horizon Humanoid Interaction with Unified Distance Field Representations" by Yutang Lin and etc., "MANA: Dexterous Manipulation of Articulated Tools" by Zhaoheng Yin and etc., "Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA" by Tutian Tang and etc., "TWIST: Teleoperated Whole-Body Imitation System" by Yannjie Ze and etc., "CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System" by Noboru Myers and etc., "EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos" by Ruihan Yang and etc., "Learning from Massive Human Videos for Universal Humanoid Pose Control" by Jiageng Mao and etc., "Cortex 2.0: Grounding World Models in Real-World Industrial Deployment" by Adriana Aida and etc., "Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning" by Chenhao Liu and etc., "RoboPaint: From Human Demonstration to Any Robot and Any View" by Jiacheng Fan and etc., "Structured World Models from Human Videos" by Russell Mendonca and etc., "Stereo4D: Learning How Things Move in 3D from Internet Stereo Videos" by Linyi Jin and etc..

## Link to each example in Exhibit 2:

1. https://thekidshouldseethis.com/post/martial-arts-robots-viral-video-2026-spring-festival-gala;

2. https://apnews.com/video/humanoid-robot-chases-wild-boars-in-the-polish-capital-warsaw-189795eb9cc641f7a5b5d071632e7c01

3. https://interestingengineering.com/videos/chinas-agibot-is-livestreaming-humanoid-robots-from-a-real-factory

4. https://www.limxdynamics.com

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
