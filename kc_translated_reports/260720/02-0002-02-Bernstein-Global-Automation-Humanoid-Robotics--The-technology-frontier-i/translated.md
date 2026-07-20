# 伯恩斯坦：全球自动化-人形机器人-2026年技术前沿

人形机器人正进入加速发展阶段，并处于大规模商业应用的临界点。本报告阐述了当前行业前沿，并为读者提供了评估行业进展及众多行业参与者主张的基准。

这些进展的核心是机器人脑模型向使用世界模型作为“规划器”的演进。本质上，VLA是“语言到动作”，而WAM是“基于环境状态、上下文和经验的行动”。WAM预测物理上可行的未来状态（图表6），然后基于这些预测生成未来动作。这类似于人类大脑在采取行动前先想象结果（图表4）。通过这种方式，WAM有望提升任务泛化能力和性能鲁棒性（图表8、图表10、图表11）。人形机器人玩家正迅速接受教导机器人“想象未来”的理念，要么开发独立的WAM，要么将世界模型嵌入现有的VLA中（图表9）。目前，挑战包括相比VLA推理速度较慢，以及用于训练WAM的非视觉数据（如触觉和材料属性）非常有限。

WAM的兴起可能重塑行业生态系统和竞争格局。WAM强调机器人动作和环境两方面的数据多样性。这类数据更可能从开源渠道获得，且与硬件平台无关。这潜在地降低了从遥操作或已部署机器人收集的后训练数据负担。因此，竞争护城河部分地从“数据所有权”转向了优越的模型架构和数据整合能力。这一转变理论上有利于独立的脑/基础WAM开发者，如Physical Intelligence（私营）和英伟达。它们可能会与Figure AI、Agibot和LimX（均为私营）等脑体一体化机器人OEM厂商形成互补。我们设想，机器人脑将演变为类似于电动汽车电池和动力总成——一些最优秀的OEM选择自研，而其余厂商则发现从最佳第三方供应商处购买更为合适。WAM范式也可能有利于填补世界模型关键物理数据空白的玩家，例如触觉传感领域的PaXini（私营）。

[[KC_IMAGE_001]]

[[KC_IMAGE_002]]

→...
→...

## 详情：公司情况更新

图表1：人形机器人五个维度的前沿与未来方向

[[KC_IMAGE_003]]

[[KC_IMAGE_004]]

[[KC_IMAGE_005]]

[[KC_IMAGE_006]]

[[KC_IMAGE_007]]

低灵巧度

操作任务

→ 长序列

[[KC_IMAGE_008]]

## 复杂与长序列

[[KC_IMAGE_009]]

[[KC_IMAGE_010]]

高灵巧度

[[KC_IMAGE_011]]

$\rightarrow$ 连续运行的可靠性

[[KC_IMAGE_012]]

[[KC_IMAGE_013]]

[[KC_IMAGE_014]]

→ 模仿人类

[[KC_IMAGE_015]]

## 预定义任务序列

[[KC_IMAGE_016]]

[[KC_IMAGE_017]]

[[KC_IMAGE_018]]

[[KC_IMAGE_019]]

## 可迁移与可泛化的技能

## 直接训练的机器人模型

-- Optimus机器人模型,RT-1

## 脑模型：公司情况更新

## 大语言模型/视觉语言模型 + 分离的运动控制

直接使用视觉语言模型进行高层推理，并使用分离系统进行运动控制 -- SayCan,Text2Motion

[[KC_IMAGE_020]]

使用预训练的视觉语言模型进行高层推理，并与运动控制系统集成。-- Helix 02,$\pi 0.5$,GR00T N1

## 视觉-语言-动作模型

[[KC_IMAGE_021]]

[[KC_IMAGE_022]]

## 场景/环境数据

[[KC_IMAGE_023]]

[[KC_IMAGE_024]]

[[KC_IMAGE_025]]

[[KC_IMAGE_026]]

[[KC_IMAGE_027]]

## 世界动作模型

[[KC_IMAGE_028]]

利用多模态模型（例如，生成式视频模型）作为主干网络来预测未来状态并据此规划动作。-- DreamZero,1XWM,UnifoLM-WMA-0

## 机器人动作数据

→...
来源：宇树科技，央视，Figure AI，学术论文（详见本报告末尾），Bernstein分析 全球自动化

图表2：来自知名人形机器人厂商在关键前沿领域的最新演示示例

注：请按顺序参见本报告最后一页每个示例的链接。宇树科技、Agibot、Paxini、Figure AI和Physical Intelligence均为私营公司。波士顿动力是现代汽车集团的子公司，Bernstein未对其进行覆盖。英伟达由Bernstein美国半导体团队覆盖。
来源：Bernstein分析

图表3：与世界模型相比，世界模型预测环境演化的结果（“预测观测值”），用于生成未来动作。

来源：Bernstein分析

图表4：WAM类似于人类大脑在采取行动前想象结果，而VLA直接输出下一个动作。
来源：Bernstein分析

图表5：三种主要的世界模型类型及其应用

来源：Bernstein分析

图表6：“渲染”世界模型生成视觉上合理的输出，而“模拟器”和“规划器”世界模型则嵌入学习到的物理定律以产生物理上可行的输出。

来源："PhyGround:Benchmarking Physical Reasoning in Generative World Models" by Juyi Lin 等,"PhyWorld:Physics-Faithful World Model for Video Generation" by Pu Zhao 等,Bernstein分析。

图表7：扩散策略模型可以捕获多种解决方案模式并选择一种作为最终方案，而其他模型类型可能坍缩到单一模式或在模式之间振荡，限制了任务泛化能力。

任务：“将T形块推入绿色区域”

来源：“Diffusion Policy:Visuomotor Policy Learning via Action Diffusion” by Cheng 等,Bernstein分析

图表8：具有扩散策略主干网络的世界动作模型可以输出物理上可行的策略，并更好地处理具有多个有效解决方案的任务——例如拿起一个装满水的杯子。

来源：Bernstein分析

图表9：Physical Intelligence的VLA模型随时间的演变
注：Physical Intelligence为私营公司。
来源：Physical Intelligence网站和报告，Bernstein分析

图表10：世界模型的采用不仅提升了$\pi 0.7$在复杂任务中的表现，还增强了其在机器人之间进行技能迁移的能力。
来源：Physical Intelligence，Bernstein分析
图表11：通过嵌入的世界模型，π0.7 (GC)打破了强训练数据集偏差——在“微波炉到冰箱”上训练，并在“冰箱到微波炉”上测试
反向“冰箱到微波炉”任务

来源：Physical Intelligence，Bernstein分析

图1的学术论文来源如下：《报告观点My Beer:学习温和的人形机器人运动与末端执行器稳定控制》（Yitang Li 等）、《感知型人形跑酷：通过运动匹配链接动态人类技能》（Zhen Wu 等）、《学习真实世界人形机器人起身策略》（Xialin He 等）、《RGMP：面向通用人形机器人操作的循环几何先验多模态策略》（Xuetao Li 等）、《工业运输任务中人形机器人的负载感知运动控制》（Lequn Fu 等）、《人形机器人高效多点巡检的路径与运动优化》（Jiayang Wu 等）、《LESSMIMIC：基于统一距离场表示的长期人形交互》（Yutang Lin 等）、《MANA：铰接工具的精巧操作》（Zhaoheng Yin 等）、《通过强化学习增强遥操作与混合灵巧专家VLA实现类人操作》（Tutian Tang 等）、《TWIST：全身遥操作模仿系统》（Yannjie Ze 等）、《CHILD（人形模仿与现场演示控制器）：全身人形遥操作系统》（Noboru Myers 等）、《EgoVLA：从自我中心人类视频学习视觉-语言-动作模型》（Ruihan Yang 等）、《从海量人类视频学习通用人形姿态控制》（Jiageng Mao 等）、《Cortex 2.0：在真实工业部署中落地世界模型》（Adriana Aida 等）、《通过多阶段强化学习实现人形全身羽毛球》（Chenhao Liu 等）、《RoboPaint：从人类演示到任意机器人与任意视角》（Jiacheng Fan 等）、《来自人类视频的结构化世界模型》（Russell Mendonca 等）、《Stereo4D：从互联网立体视频学习物体在3D中的运动方式》（Linyi Jin 等）。

## 图2中各示例链接

1. https://thekidshouldseethis.com/post/martial-arts-robots-viral-video-2026-spring-festival-gala

2. https://apnews.com/video/humanoid-robot-chases-wild-boars-in-the-polish-capital-warsaw-189795eb9cc641f7a5b5d071632e7c01

3. https://interestingengineering.com/videos/chinas-agibot-is-livestreaming-humanoid-robots-from-a-real-factory

4. https://www.limxdynamics.com/zh/news/BK000065

5. https://www.figure.ai/

6. https://www.rockingrobots.com/figure-ai-claims-200-hour-autonomous-package-sorting-run-with-figure-03/

7. https://www.youtube.com/watch?v=V1Lxp-Q6Y9g

8. https://www.youtube.com/watch?v=3aQWvdCac9o

## 观察提示：公司情况更新

重申对发那科、汇川技术、哈默纳科、康耐视和基恩士的“跑赢大盘”评级；对埃斯顿的“与大盘持平”评级。

O - 跑赢大盘，M - 与大盘持平，U - 跑输大盘，NR - 未评级，CS - 暂停覆盖

6954.JP、6861.JP 基准年为2026年

来源：彭博、Bernstein估计与分析。