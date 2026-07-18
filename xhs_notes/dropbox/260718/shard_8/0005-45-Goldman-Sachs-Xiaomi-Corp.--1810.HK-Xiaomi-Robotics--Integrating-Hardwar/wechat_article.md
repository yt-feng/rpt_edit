# GS：小米机器人整合硬件数据与模型以扩大规模

2026年7月，小米机器人部门连续发布三项进展，让这家公司从“造车新势力”的讨论中，悄然进入了一个更硬核的赛道。GS在最新报告中指出，小米已初步完成机器人框架中本体、数据和模型的整合，这可能催生一个自我强化的循环，指向通用工业与家庭自动化。

这份报告最值得关注的判断不是某个具体参数，而是小米在机器人领域的布局节奏——它正在用自己最擅长的方式，把消费电子和智能电动汽车的经验复制到机器人上：先有场景，再有数据，最后用模型反哺场景。

![研报原图 1](assets/source_image_01.jpg)

## 1. 人形机器人已进入产线，成功率接近熟练工人

小米的人形机器人从今年3月开始在自攻螺母加载工位部署，到7月任务成功率已从90%以上提升至98%，仅比经验丰富的工人低1个百分点。从7月起，机器人开始承担新的物流任务，包括分拣柔性中控台侧盖和折叠可回收箱，成功率维持在90%，并首次实现了对柔性工件的长时间连续操作。

尽管在速度和产量上仍有明显差距，但这一进展让小米与Figure AI等全球领先者站在了同一队列——它们都是少数将人形机器人部署到活跃汽车生产线的公司。GS认为，小米在部署场景上拥有清晰优势，包括自有制造工厂和庞大的家庭AIoT生态。

> **KC评论：** 98%的成功率在实验室环境中可能不算惊艳，但在真实产线上意味着机器人已经能处理“边缘案例”——那些最容易被忽略但最影响稳定性的异常情况。这正是从演示到量产的关键一步。

![研报原图 2](assets/source_image_02.jpg)

## 2. 38B参数生成模型，解决机器人训练的数据瓶颈

真实世界的数据稀缺是机器人行业公认的瓶颈。小米发布的Robotics-U0是一个380亿参数的统一生成模型，设计用于合成高保真机器人轨迹和物理交互场景。它的独特之处在于将文本到图像生成、任意到图像编辑、多视角具身场景生成、具身迁移和具身视频生成统一到一个架构中，允许跨模态的自回归缩放，同时保持几何完整性和视角一致性。

据小米称，Robotics-U0在具身场景生成和具身迁移方面超越了GPT-Image-2，并在具身世界模型评估基准WorldArena上排名第一。这意味着小米不仅在用机器人干活，还在用生成模型“制造”机器人干活的数据。

![研报原图 3](assets/source_image_03.jpg)

## 3. VLA基础模型实现跨本体迁移，规模化信号清晰

小米发布的Robotics-1是一个视觉-语言-动作基础模型，专为端到端物理执行设计。该模型经过10万小时真实世界机器人操作轨迹的大规模预训练，以及1万小时的跨本体后训练，展现出清晰的VLM缩放行为，并支持跨本体适应——包括双足、四足、双机械臂或轮式系统。

在RoboCasa365和RoboDojo-Sim等多个基准测试中，Xiaomi-Robotics-1取得最高分，超越了阿里巴巴的ABot-M0.6和腾讯的Hy-Embodied-0.5-VLA等开源模型。GS指出，真实世界的部署失败会被分析并反馈到场景生成模型中，合成类似的边缘案例场景，这些合成数据再用于重新训练核心基础模型，然后重新部署到物理硬件上——这正是那个“自我强化循环”的关键。

当然，报告也坦承小米与全球领先者之间仍存在差距，包括Figure 03在宝马工厂展示的更快速度，以及Physical Intelligence、Figure、Optimus和Gemini Robotics等闭源模型的能力。小米也未披露成本结构和性能参数等细节。

但一个更值得关注的信号是：GS认为，未来3-5年小米机器人将聚焦于更结构化的商业场景，包括在自有工厂和合作伙伴工厂大规模部署人形机器人。这让人联想到特斯拉对Optimus的策略——先用自有场景跑通闭环，再向外输出能力。

对于一家已经拥有智能手机、智能电动汽车和庞大AIoT生态的公司来说，机器人可能不是最性感的业务，但可能是最能串联起所有硬件能力的那条线。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
