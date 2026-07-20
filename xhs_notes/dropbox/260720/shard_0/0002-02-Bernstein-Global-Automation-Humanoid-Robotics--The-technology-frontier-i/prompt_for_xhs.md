你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

4. https://www.limxdynamics.com/zh/news/BK000065

5. https://www.figure.ai/

6. https://www.rockingrobots.com/figure-ai-claims-200-hour-autonomous-package-sorting-run-with-figure-03/

7. https://www.youtube.com/watch?v=V1Lxp-Q6Y9g

8. https://www.youtube.com/watch?v=3aQWvdCac9o

## INVESTMENT IMPLICATIONS

Reiterate Outperform for FANUC, Inovance, Harmonic Drive, Cognex, and Keyence; Market-Perform for Estun.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="4">16 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>002747.CH (Estun)</td><td>M</td><td>CNY</td><td>42.43</td><td>26.00</td><td>74.4%</td><td>CNY</td><td>0.05</td><td>0.31</td><td>0.32</td><td>848.6</td><td>138.0</td><td>131.2</td><td></td></tr><tr><td>2715.HK (Estun)</td><td>M</td><td>HKD</td><td>22.70</td><td>17.26</td><td>NA</td><td>CNY</td><td>0.05</td><td>0.31</td><td>0.32</td><td>454.0</td><td>73.8</td><td>70.2</td><td></td></tr><tr><td>6954.JP (Fanuc)</td><td>O</td><td>JPY</td><td>7,020.00</td><td>7,000.00</td><td>44.9%</td><td>JPY</td><td>178.47</td><td>207.32</td><td>193.15</td><td>39.3</td><td>33.9</td><td>36.3</td><td></td></tr><tr><td>6324.JP (HDSI)</td><td>O</td><td>JPY</td><td>7,2

[中间内容因长度限制已省略]

tained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
