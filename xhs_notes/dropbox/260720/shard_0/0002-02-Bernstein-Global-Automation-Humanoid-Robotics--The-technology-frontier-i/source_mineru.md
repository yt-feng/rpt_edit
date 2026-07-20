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

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="4">16 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>002747.CH (Estun)</td><td>M</td><td>CNY</td><td>42.43</td><td>26.00</td><td>74.4%</td><td>CNY</td><td>0.05</td><td>0.31</td><td>0.32</td><td>848.6</td><td>138.0</td><td>131.2</td><td></td></tr><tr><td>2715.HK (Estun)</td><td>M</td><td>HKD</td><td>22.70</td><td>17.26</td><td>NA</td><td>CNY</td><td>0.05</td><td>0.31</td><td>0.32</td><td>454.0</td><td>73.8</td><td>70.2</td><td></td></tr><tr><td>6954.JP (Fanuc)</td><td>O</td><td>JPY</td><td>7,020.00</td><td>7,000.00</td><td>44.9%</td><td>JPY</td><td>178.47</td><td>207.32</td><td>193.15</td><td>39.3</td><td>33.9</td><td>36.3</td><td></td></tr><tr><td>6324.JP (HDSI)</td><td>O</td><td>JPY</td><td>7,200.00</td><td>7,800.00</td><td>130.3%</td><td>JPY</td><td>16.99</td><td>57.37</td><td>79.51</td><td>423.8</td><td>125.5</td><td>90.6</td><td></td></tr><tr><td>6861.JP (Keyence)</td><td>O</td><td>JPY</td><td>74,050</td><td>86,000</td><td>(7.9)%</td><td>JPY</td><td>1,835.63</td><td>2,248.48</td><td>2,494.78</td><td>40.3</td><td>32.9</td><td>29.7</td><td></td></tr><tr><td>300124.CH (Inovance)</td><td>O</td><td>CNY</td><td>60.31</td><td>82.00</td><td>(34.8)%</td><td>CNY</td><td>1.87</td><td>2.19</td><td>2.65</td><td>32.3</td><td>27.5</td><td>22.8</td><td></td></tr><tr><td>CGNX (Cognex)</td><td>O</td><td>USD</td><td>63.89</td><td>75.00</td><td>73.3%</td><td>USD</td><td>0.67</td><td>1.46</td><td>1.62</td><td>95.4</td><td>43.8</td><td>39.5</td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,865.18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,545.21</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,457.69</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

6954.JP, 6861.JP base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Estun Automation Co Ltd

We use EV/EBITDA multiple as the primary valuation method. Our price target of RMB26.0 (A-share) and HKD 17.3 (H-share) are based on an EV/EBITDA multiple of 35.9x against our 1-year forward EBITDA estimate of RMB677.2mn. We set the multiple referencing previous cycles but adjust for secular or competitive trends that we believe are moving multiples higher or lower across multiple cycles. We set Estun's H-share TP based on the average A/H share premium. We use DCF as reference for the company's long-term intrinsic value. As we move along the different stages of a cycle, the time-dependent target price may deviate from the DCF-implied value.

## FANUC Corp

We use EV/EBITDA multiple as the primary valuation method. We set a JPY7,000 target price using an EV/EBITDA multiple of 22.5x against our 1-year forward-looking EBITDA estimates (from the PT date) of JPY 251,396 million. We set the target multiple referencing previous cycles but adjust for secular or competitive trends that we believe are moving multiples higher or lower across multiple cycles. We use DCF as reference for the company's long-term intrinsic value. As we move along the different stages of a cycle, the time-dependent target price may deviate from the DCF-implied value.

## Harmonic Drive Systems Inc

We use EV/EBITDA multiple as the primary valuation method. We set a JPY 7,800 target price using an EV/EBITDA multiple of 45.5x against our 1-year forward-looking EBITDA estimates (from the PT date) of JPY16,194 mn. We set the target multiple referencing previous cycles but adjust for secular or competitive trends that we believe are moving multiples higher or lower across multiple cycles. We use DCF as reference for the company's long-term intrinsic value. As we move along the different stages of a cycle, the time-dependent target price may deviate from the DCF-implied value.

## Keyence Corp

We use EV/EBITDA multiple as the primary valuation method. We set a JPY86,000 target price using an EV/EBITDA multiple of 21.5x against our 1-year forward-looking EBITDA estimates (from the PT date) of JPY 831,323 million. We apply our target multiple on the upcoming cycle peak to get the enterprise value, and discount it back to derive our price target. We use DCF as reference for the company's long-term intrinsic value. As we move along the different stages of a cycle, the time-dependent target price may deviate from the DCF-implied value.

## Shenzhen Inovance Technolo-A

We use EV/EBITDA multiple as the primary valuation method. We set a RMB82 target price using an EV/EBITDA multiple of 24.0x against our 1-year forward-looking EBITDA estimates (from the PT date) of RMB 8971.6 million. We set the multiple referencing previous cycles but adjust for secular or competitive trends that we believe are moving multiples higher or lower across multiple cycles. We use DCF as reference for the company's long-term intrinsic value. As we move along the different stages of a cycle, the time-dependent target price may deviate from the DCF-implied value.

## Cognex Corp

We use EV/EBITDA multiple as the primary valuation method. We set a USD75.00 price target using an EV/EBITDA multiple of 36.5x against our 1-year forward-looking EBITDA estimates (from the PT date) of USD 333.4 million. We set the multiple referencing previous cycles but adjust for secular or competitive trends that we believe are moving multiples higher or lower across multiple cycles. We use DCF as reference for the company's long-term intrinsic value. As we move along the different stages of a cycle, the time-dependent price target may deviate from the DCF-implied value.

## RISKS

## Estun Automation Co Ltd

The risks to our view on Estun are mainly associated with China and global macro economy, including industrial capex cycles, trade frictions, and currency. In addition, the integration of Cloos and realization of planned synergies are important to our thesis and sources of additional risks. The upside risks include 1) faster than expected margin expansion; 2) faster than expected market share gain. The downside risks include 1) weaker than expected automation demands in China; 2) delayed or slower than expected in operating and net margin improvement; 3) delayed or slower than expected market share gain.

## FANUC Corp

FANUC's end user markets are cyclical in nature. The risks are mainly associated with the global macro economy and currency. The downside risks include 1) delayed or weaker than expected global automation demand, 2) losing market share to competitors, and 3) appreciation of JPY.

## Harmonic Drive Systems Inc

The risks to our view on HDSI are mainly associated with the global macro economy, including industrial capex cycles, competition and currency. As HDSI has $>50\%$ of global share in strain wave reducer, potential change in competitive landscape would be a more relevant risk than to other companies. Therefore, the downside risks include: 1) weaker than expected global robot demand, 2) losing market share to competitors, and 3) appreciation of JPY.

## Keyence Corp

The risks are mainly associated with the global macro economy. Our analysis shows that company's growth correlates with the overall utilization of manufacturing capacity in the major economies. Fluctuations in utilization may lead to unexpected near term fluctuations in growth rates. A global recession as severe as that of 2009 may even result in decline in Keyence's revenue. In addition, there is currency risk associated with the exchange rate of JPY. Therefore, the downside risks include: 1) weaker than expected overall utilization, 2) delayed or weaker than expected global automation demand, and 3) appreciation of JPY.

## Shenzhen Inovance Technolo-A

The risks to our view on Inovance are mainly associated with macro economy, including industrial capex cycles, trade frictions, and currency. The downside risks to our view on Inovance include 1) weaker than expected automation demands in China, 2) weaker or slower than expected share gain in China in segments besides servo motor and VFD, 3) weaker than expected EV demands.

## Cognex Corp

Similar to Keyence, the risks are mainly associated with the global macro economy and the overall utilization of manufacturing capacity in the major economies. The downside risks include: 1) delayed or weaker than expected global automation demands, 2) delayed or slower than expected progress in "emerging customer" program, 3) delayed or slower than expected in the integration of Moritex and realization of planned synergies.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price

Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

• Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.2%</td><td>15.3%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>35.8%</td><td>16.2%</td></tr><tr><td>Underperform</td><td>SELL</td><td>13.1%</td><td>13.6%</td></tr></table>

## PRICE CHARTS / RATINGS AND PRICE TARGET HISTORY

Estun Automation Co Ltd (002747.CH) Rating History for Bernstein as of 07/17/2026  
![](images/ee85dcd78e73ed70e6d758adce8ffeea5cbffa158c7c69a2b807005d23d94631.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Estun Automation Co Ltd (2715.HK) Rating History for Bernstein as of 07/17/2026  
![](images/94430e4b297b37baae64969ba3256e4d738a266bdc8b71bf8aa4fd7a916c85b2.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

FANUC Corp (6954.JP) Rating History for Bernstein as of 07/17/2026  
![](images/910cb462fcc8b7ad947834054d14f1bef4d8441d50e9d7c32fd357b8cbdf43ee.jpg)

Harmonic Drive Systems Inc (6324.JP) Rating History for Bernstein as of 07/17/2026  
![](images/01b5fe4fb5a55fc8fd1f4568bca42573d779b2c2ad554a052707824df4f5a660.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Keyence Corp (6861.JP) Rating History for Bernstein as of 07/17/2026  
![](images/339de50c79d4985ca61be5a14439e08b7f8a420d79de1b0f38380a367ed5357c.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

Shenzhen Inovance Technolo-A (300124.CH) Rating History for Bernstein as of 07/17/2026  
![](images/c6a13e9c65343be8d143b8f8f44fc66459dab008cf5d516502dfd6b2177799e6.jpg)  
Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

![](images/4cd729f0d121bd905b6a75a015273adac3edb69f4fd3b0b4e6379b045458a018.jpg)  
All price target and closing price data in the chart(s) above are denominated in the currency noted in the Ticker Table of this report.

## CONFLICTS OF INTEREST

Certain affiliates of Bernstein act as market maker or liquidity provider in the equities securities of: Cognex Corp.

## OTHER MATTERS

The legal entity(ies) employing the analyst(s) listed in this report, and their location, can be determined by the country code of their phone number, as follows:

+1 Bernstein Institutional Services LLC; New York, New York, USA

+44 Bernstein Autonomous LLP; London UK

+212 SG Africa Technologies & Services; Casablanca, Morocco

+33 BSG France S.A.; Paris, France

+34 BSG France S.A.; Madrid, Spain

+41 Bernstein Autonomous LLP; Geneva, Switzerland

+49 BSG France S.A.; Frankfurt, Germany

+91 Bernstein (India) Private Limited; Mumbai, India

+852 Bernstein (Hong Kong) Limited 盛博香港有限公司; Hong Kong, China

+65 Bernstein (Singapore) Private Limited; Singapore

+81 Bernstein Japan KK; Tokyo, Japan

Where this report has been prepared by research analyst(s) employed by a non-US affiliate, such analyst(s), is/are (unless otherwise expressly noted below) not registered as associated persons of Bernstein Institutional Services LLC or any other SEC-registered broker-dealer and are not licensed or qualified as research analysts with FINRA. Accordingly, such analyst(s) may not be subject to FINRA's restrictions regarding (among other things) communications by research analysts with a subject company, interactions between research analysts and investment banking personnel, participation by research analysts in solicitation and marketing activities relating to investment banking transactions, public appearances by research analysts, and trading securities held by a research analyst account.

Where this report has been prepared by research analyst(s) employed by SG Africa Technologies & Services (part of the SG group of companies), it has been prepared on behalf of a Bernstein company under a Global Services Agreement in place between Bernstein and SG.

## CERTIFICATION

Each research analyst listed in this report, who is primarily responsible for the preparation of the content of this report, certifies that all of the views expressed in this publication accurately reflect that analyst's personal views about any and all of the subject securities or issuers and that no part of that analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views in this publication.

## II. ADDITIONAL GLOBAL CONFLICT DISCLOSURES

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e., the private side) within the Firm, and into other areas, units, groups or affiliates (i.e., public side) of the Firm.

## III. OTHER IMPORTANT INFORMATION AND DISCLOSURES

Separate branding is maintained for “Bernstein” and “Autonomous” research products.

\- Bernstein produces a number of different types of research products including, among others, fundamental analysis and quantitative analysis under both the “Autonomous” and “Bernstein” brands. Recommendations contained within one type of research product may differ from recommendations contained within other types of research products, whether as a result of differing time horizons, methodologies or otherwise. Furthermore, views or recommendations within a research product issued under one brand may differ from views or recommendations under the same type of research product issued under the other brand. The Research Ratings System for the two brands and other information related to those Rating Systems are included in the previous section.

\- Autonomous operates as a separate business unit within the following entities: Bernstein Institutional Services LLC, Bernstein Autonomous LLP, Bernstein (Hong Kong) Limited 盛博香港有限公司 and Bernstein (India) Private Limited. For information relating to “Autonomous” branded products (including certain Sales materials) please visit: www.autonomous.com. For information relating to Bernstein branded products please visit: www.bernsteinresearch.com.

Analysts are compensated based on aggregate contributions to the research franchise as measured by account penetration, productivity and proactivity of investment ideas. No analysts are compensated based on performance in, or contributions to, generating investment banking revenues.

This report has been produced by an independent analyst as defined in Article 3 (1)(34)(i) of EU 596/2014 Market Abuse Regulation (“MAR”) and the same article of MAR as it forms part of United Kingdom domestic law by virtue of the European Union (Withdrawal) Act 2018.

To our readers in the United States: Bernstein Institutional Services LLC, a broker-dealer registered with the U.S. Securities and Exchange Commission (“SEC”) and a member of the U.S. Financial Industry Regulatory Authority, Inc. (“FINRA”) is distributing this publication in the United States and accepts responsibility for its contents. Where this material contains an analysis of debt product(s), such material is intended only for institutional investors and is not subject to the US independence and disclosure standards applicable to debt research prepared for retail investors.

Bernstein Institutional Services LLC may act as principal for its own account or as agent for another person (including an affiliate) in sales or purchases of any security which is a subject of this report. This report does not purport to meet the objectives or needs of any specific individuals, entities or accounts.

To our readers in Canada: If this publication pertains to a Canadian domiciled company, it is being distributed in Canada by Bernstein (Canada) Limited, which is licensed and regulated by the Canadian Investment Regulatory Organization. If the publication pertains to a non-Canadian domiciled company, it is being distributed by Bernstein Institutional Services LLC, which is licensed and regulated by both the SEC and FINRA, into Canada under the International Dealers Exemption.

This document may not be passed onto any person in Canada unless that person qualifies as "permitted client" as defined in Section 1.1 of NI 31-103.

To our readers in Brazil: This report has been prepared by Bernstein Institutional Services LLC, and Banco BTG Pactual S.A. ("BTG") is responsible for the distribution of this report in Brazil.

To readers in the United Kingdom: This publication has been issued or approved for issue in the United Kingdom by Bernstein Autonomous LLP, authorised and regulated by the Financial Conduct Authority and located at 60 London Wall, London EC2M 5SH, +44 (0)20-7170-5000. Registered in England & Wales No OC343985.

This document is for distribution only to persons who (i) have professional experience in matters relating to investments falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the “Financial Promotion Order”), (ii) are persons falling within Article 49(2)(a) to (d) (“high net worth companies, unincorporated associations, etc.”) of the Financial Promotion Order, (iii) are outside the United Kingdom, or (iv) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the FSMA) in connection with the issue or sale of any securities may otherwise lawfully be communicated or caused to be communicated (all such persons together being referred to as “relevant persons”). This document is directed only at relevant persons and must not be acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this document relates is available only to relevant persons and will be engaged in only with relevant persons.

To our readers in the member states of the EEA: This publication is being distributed by BSG France SA, which is authorised and regulated by the Autorité de Contrôle Prudentiel et de Résolution (ACPR) and Autorité des Marchés Financiers (AMF).

To our readers in Hong Kong: This publication is being distributed in Hong Kong by Bernstein (Hong Kong) Limited 盛博香港有限公司, which is licensed and regulated by the Hong Kong Securities and Futures Commission (Central Entity No. AXC846) to carry out Type 4 (Advising on Securities) regulated activities and subject to the licensing conditions mentioned in the SFC Public Register (https://www.sfc.hk/publicregWeb/corp/AXC846/details)). This publication is solely for professional investors, as defined in the Securities and Futures Ordinance (Cap. 571). The purpose of this report is solely to provide an analysis of the issuers referred to in this report and is not intended for any purpose contrary to the laws of Hong Kong.

To our readers in Singapore: This publication is being distributed in Singapore by Bernstein (Singapore) Private Limited, only to accredited investors or institutional investors, as defined in the Securities and Futures Act 2001 of Singapore ("SFA"). Recipients in Singapore should contact Bernstein (Singapore) Private Limited in respect of matters arising from, or in connection with, this publication. Bernstein (Singapore) Private Limited is regulated by the Monetary Authority of Singapore and licensed under the SFA as a capital markets services licence holder for dealing in capital markets products that are securities and collective investment schemes and an exempt financial adviser for advising on, issuing and promulgating analyses and reports on securities. Bernstein (Singapore) Private Limited is registered in Singapore with Company Registration No. 20213710W and located at 8 Marina Boulevard, #12-01, Marina Bay Financial Centre, Singapore 018981, +65-6326-7000.

To our readers in the People's Republic of China: The securities referred to in this document are not being offered or sold and may not be offered or sold, directly or indirectly, in the People's Republic of China (for such purposes, not including the Hong Kong and Macau Special Administrative Regions or Taiwan, the "PRC") in contravention of any applicable laws of the PRC.

This document does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC to any person to whom it is unlawful to make the offer or solicitation in the PRC.

We do not represent that this document may be lawfully distributed, or that any securities may be lawfully offered, in compliance with any applicable registration or other requirements in the PRC, or pursuant to an exemption available thereunder, or assume any responsibility for facilitating any such distribution or offering. In particular, no action has been taken by us which would permit a public offering of any securities or distribution of this document in the PRC. Accordingly, the securities are not being offered or sold within the PRC by means of this document or any other document. Neither this document nor any advertisement or other offering material may be distributed or published in the PRC, except under circumstances that will result in compliance with any applicable laws and regulations.

To our readers in Japan: This publication is being distributed in Japan by Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社), which is registered in Japan as a Financial Instruments Business Operator with the Kanto Local Finance Bureau (registration number: The Director-General of Kanto Local Finance Bureau (FIBO) No.3387) and regulated by the Financial Services Agency. It is also a member of Investment Management Association of Japan. This publication is solely for qualified institutional investors in Japan only, as defined in Article 2, paragraph (3), items (i) of the Financial Instruments and Exchange Act.

For the institutional client readers in Japan who have been granted access to the Bernstein website by Daiwa Group Inc. ("Daiwa"), your access to this document should not be construed as meaning that Bernstein is providing you with investment advice for any purposes. Whilst Bernstein has prepared this document, your relationship is, and will remain with, Daiwa, and Bernstein has neither any contractual relationship with you nor any obligations towards you.

To our readers in Australia: Bernstein (Hong Kong) Limited 盛博香港有限公司 is responsible for distributing research in Australia. It is regulated by the Securities and Exchange Commission under U.S. laws, by the Financial Conduct Authority under U.K. laws, which differs from Australian laws. Bernstein (Hong Kong) Limited 盛博香港有限公司 is exempt from the requirement to hold an Australian financial services license under the Corporations Act 2001 in respect of the provision of the

following financial services to wholesale clients:

• providing financial product advice;

• dealing in a financial product;

\- making a market for a financial product; and

• providing a custodial or depository service.

To our readers in India: This publication is being distributed in India by Bernstein (India) Private Limited (SCB India) which is licensed and regulated by Securities and Exchange Board of India ("SEBI") as a research analyst entity under the SEBI (Research Analyst) Regulations, 2014, having registration no. INH000006378 and as a stock broker having registration no. INZ000213537. SCB India is currently engaged in the business of providing research and stock broking services. Please refer to www.bernsteinresearch.in for more information.

\- SCB India is a Private limited company incorporated under the Companies Act, 2013, on April 12, 2017 bearing corporate identification number U65999MH2017FTC293762, and registered office at Level 3A, 4th Floor, First International Financial Centre, Plot Nos C-54 and C-55, G Block, Near CBI Office, Bandra Kurla Complex, Bandra (East), Mumbai 400098, Maharashtra, India (Phone No: +91-22-68421401).

\- For details of Associates (i.e., affiliates/group companies) of SCB India, kindly email MUM-BERNSTEIN-InCompliance@bernsteinsg.com.

• SCB India does not have any disciplinary history as on the date of this report.

\- Except as noted above, SCB India and/or its Associates (i.e., affiliates/group companies), the Research Analysts authoring this report, and their relatives

• do not have any financial interest in the subject company

• do not have actual/beneficial ownership of one percent or more in securities of the subject company;

• is not engaged in any investment banking activities for Indian companies, as such;

• have not managed or co-managed a public offering in the past twelve months for any Indian companies;

\- have not received any compensation for investment banking services or merchant banking services from the subject company in the past 12 months;

• have not received compensation for brokerage services from the subject company in the past twelve months;

\- have not received any compensation or other benefits from the subject company or third party related to the specific recommendations or views in this report; and

\- do not currently, but may in the future, act as a market maker in the financial instruments of the companies covered in the report.

\- do not have any conflict of interest in the subject company as of the date of this report.

\- Except as noted above, the subject company has not been a client of SCB India during twelve months preceding the date of distribution of this research report. Neither SCB India nor its Associates (i.e., affiliates/group companies) have received compensation for products or services other than investment banking, merchant banking or brokerage services from the subject company in the past twelve months.

\- The principal research analyst(s) who prepared this report, members of the analysts' team, and members of their households are not an officer, director, employee or advisory board member of the companies covered in the report.

\- Our Compliance officer / Grievance officer is Ms. Rupal Talati, who can be reached at +91-22-68421451, or MUM-BERNSTEIN-InCompliance@bernsteinsg.com / Scbin-investorgrievance@bernsteinsg.com

\- The Research investor charter and Terms & Conditions of SCB India are available on its website and may be accessed at Bernstein (India) Private Limited (https://bernsteinresearch.in/) for your reference.

\- Disclaimer: Registration granted by SEBI, and certification from NISM, is in no way a guarantee of performance of the intermediary or provide any assurance of returns to investors. Investments in securities market are subject to market risks. Read all the related documents carefully before investing.

To our readers in Switzerland: This document is provided in Switzerland by or through Bernstein Autonomous LLP, and is provided only to qualified investors as defined in article 10 of the Swiss Collective Investment Scheme Act (“CISA”) and related provisions of the Collective Investment Scheme Ordinance and in strict compliance with applicable Swiss law and regulations. The products mentioned in this document may not be suitable for all types of investors. This document is based on the Directives on the Independence of Financial Research issued by the Swiss Bankers Association (SBA) in January 2008.

To our readers in the Middle East: Bernstein Autonomous LLP, DIFC branch has its principal office at Gate Village 06, DIFC, Dubai, UAE. Bernstein Autonomous LLP, DIFC branch is regulated by the Dubai Financial Services Authority (DFSA) with the registration number CL10040 and is provisioned for Arranging Deals in Investments and Advising on Financial Products. All communications and services are directed at Professional Clients and Market Counterparties only (as defined in the DFSA rulebook). Persons other than Professional Clients and Market Counterparties, such as Retail Clients, are not the intended recipients of our communications or services.

## LEGAL

All research publications are disseminated to our clients through posting on the firm's password protected websites, bernsteinresearch.com and autonomous.com. Certain, but not all, research publications are also made available to clients through third-party vendors or redistributed to clients through alternate electronic means as a convenience.

This publication has been published and distributed in accordance with the Firm's policy for management of conflicts of interest in investment research, a copy of which is available from Bernstein Institutional Services LLC, Director of Compliance, 245 Park Avenue, New York, NY 10167. Additional disclosures and information regarding Bernstein's business are available on our website www.bernsteinresearch.com.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. This publication is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of, or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or which would subject any of the entities referenced herein or any of their subsidiaries or affiliates to any registration or licensing requirement within such jurisdiction. This publication is based upon public sources we believe to be reliable, but no representation is made by us that the publication is accurate or complete. We do not undertake to advise you of any change in the reported information or in the opinions herein. This publication was prepared and issued by entity referred to herein for distribution to eligible counterparties or professional clients. This publication is not an offer to buy or sell any security, and it does not constitute investment, legal or tax advice. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with their professional advisors in light of their specific circumstances. The value of investments may fluctuate, and investments that are denominated in foreign currencies may fluctuate in value as a result of exposure to exchange rate movements. Information about past performance of an investment is not necessarily a guide to, indicator of, or assurance of, future performance.

This report is directed to and intended only for our clients who are “eligible counterparties”, “professional clients”, “institutional investors” and/or “professional investors” as defined by the aforementioned regulators, and must not be redistributed to retail clients as defined by the aforementioned regulators. Retail clients who receive this report should note that the services of the entities noted herein are not available to them and should not rely on the material herein to make an investment decision. The result of such act will not hold the entities noted herein liable for any loss thus incurred as the entities noted herein are not registered/authorised/licensed to deal with retail clients and will not enter into any contractual agreement/arrangement with retail clients. This report is provided subject to the terms and conditions of any agreement that the clients may have entered into with the entities noted herein. All research reports are disseminated on a simultaneous basis to eligible clients through electronic publication to our client portal.

The information in this report was prepared by Bernstein solely for the internal business use of our clients. Clients may store, display, analyze, reformat and print the information in this report for this limited use only. Clients may not copy, alter, create derivative works, resell, reverse engineer, commercially exploit, share or distribute any part of the information contained herein for any purpose without Bernstein's express written consent. These restrictions include extracting data or using the content to develop indices or other products. Further, you may not use this report, or any portion of this report, to train or finetune any third-party machine learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.