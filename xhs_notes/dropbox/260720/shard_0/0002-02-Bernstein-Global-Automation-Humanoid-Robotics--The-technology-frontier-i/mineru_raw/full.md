# Humanoid Robotics: The technology frontier in 2026

Humanoid robotics is entering a phase of accelerated development and at the threshold of large-scale commercial adoption. This note explains the current frontier of the industry and provides benchmarks for observers to assess progress and the numerous claims made by industry players.

We highlight the frontier and future directions in five dimensions (Exhibit 1), along which, examples of progresses from notable players are shown in Exhibit 2. In locomotion, stable walking on flat surface, which was impressive two years ago, has progressed to motions that require high dynamic full-body control and adaptive interaction with environment. Manipulation tasks have advanced from single-step pick-and-place to increasing dexterity, longer task sequence, and industrial level reliability, although in all these areas, development remains in the early stage. In the level of autonomy, remote control is largely abandoned, and autonomous short-horizon tasks and pre-defined long-horizon tasks are currently the most common. Long-horizon autonomous planning, skill transfer, and task generalization are just emerging and the focus of future development. The robotic brain paradigm has evolved from LLM/VLM to vision-language-action (VLA) models (2024-2025), which are enhanced by World Action Models (WAM) from 2026 onward. Data modality has greatly diversified, and the general trend is to move away from teleoperation (high cost, low efficiency, and hardware dependent) and prioritize egocentric, platform-agnostic data (such as human videos), and the complementary use of non-vision data.

At the center of these progresses is the evolution of robotic brain models to use World Model as the "planner". In essence, VLA is "language to action", while WAM is "action based on environmental state, context, and experience". WAM predicts physically feasible future states (Exhibit 6) and then generates future actions based on those predictions. It is analogous to human brains imagining outcomes before taking actions (Exhibit 4). This way, WAM promises to improve task generalization and performance robustness (Exhibit 8, Exhibit 10, Exhibit 11). Humanoid robot players are quickly embracing the idea of teaching robots to "imagine the future", by either developing standalone WAM or embedding World Model within an existing VLA (Exhibit 9). Currently, challenges include slower inference speed compared to VLA and the very limited non-vision data such as tactile and material properties to train WAMs.

The rise of WAM may reshape the industry ecosystem and competitive dynamics. WAM emphasizes data diversity with regard to both robot actions and environment. This type of data is more likely to be available from open sources and agnostic of hardware platforms. This potentially lowers the burden of post-training data collected from teleoperation or deployed robots. Therefore, the competitive moat partially shifts from "data ownership" to superior model architecture and data consolidation capabilities. This shift conceivably benefits independent brain / foundational WAM developers such as Physical Intelligence (private) and Nvidia. They will likely complement the brain-body integrated robot OEMs such as Figure AI, Agibot, and LimX (all private). We imagine that robot brain will evolve to be analogous to EV battery and power train — some best OEMs choose to have their own, and the rest find it better to purchase from the best third-party suppliers. The WAM paradigm may also favor players that fill the critical physical data gaps for World Models, such as PaXini (private) in tactile sensing.

## DETAILS

EXHIBIT 1: The frontier and future directions in five dimensions of humanoid robots

EXHIBIT 2: Examples of latest demonstration in the key frontiers from notable humanoid players

EXHIBIT 3: Compared to a VLA, world models forecast the outcome of evolution of environment ("predicted observation"), which is used to generate future actions.

EXHIBIT 4: WAM is analogous to human brains imagining outcomes before taking actions, while VLA outputs the next action directly.

EXHIBIT 5: Three main types of world models and their applications

EXHIBIT 6: "Render" world models generate visually plausible outputs, while "simulator" and "planner" world models embed learned physical laws to produce physically feasible outputs.

EXHIBIT 7: Diffusion policy models can capture multiple solution modes and select one as the final one, while other model types may collapse toward a single mode or oscillate between modes, limiting task generalization capability.

EXHIBIT 8: World Action Models with a diffusion-policy backbone can output physically feasible policies and better handle tasks with multiple valid solutions – such as picking up a mug filled with water.

EXHIBIT 9: Evolution of Physical Intelligence's VLA models over time

EXHIBIT 10: The adoption of the world model not only improved π0.7's performance in complex tasks but also enhanced its capability for skill transfer between robots.

EXHIBIT 11: With the embedded World Model, π0.7 (GC) breaks strong training dataset biases – trained on "microwave to fridge" and tested on "fridge to microwave"

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
