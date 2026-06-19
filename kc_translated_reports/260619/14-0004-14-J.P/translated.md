# 半导体
# AI驱动定制芯片（ASIC）复苏——ASIC市场概览/更新

## ASIC——专用集成电路：

- 为特定客户、特定应用或平台设计的芯片：

• 示例：苹果iPhone A19处理器芯片（苹果完成全部设计）
• 示例：诺基亚Reef Shark BTS处理器芯片（诺基亚、Marvell、博通）
• 示例：谷歌TPU AI处理器（谷歌、博通）
• 示例：亚马逊Trainium 3 AI处理器（AWS、Marvell、Alchip）

## ASSP——专用标准产品（有时称为"商用芯片"）

• 为多个客户、特定应用设计的芯片：

• 示例：高通骁龙移动处理器系列
• 示例：英伟达AI GPU、AMD AI GPU

## GP——通用产品——多个客户/多个应用

• 为多个客户、多个应用设计的芯片

• 示例：英特尔/AMD PC或服务器CPU
• 示例：英飞凌、意法半导体、安森美——功率半导体/微控制器
• 示例：三星、SK海力士、美光——内存/存储

[[KC_IMAGE_001]]

## 自研定制芯片或ASIC的价值主张：

- 客户拥有软件栈
- 如果拥有软件栈，可以针对特定软件栈和驱动程序定制芯片，实现更优的系统级性能（计算性能/功耗）
- 经济性（高产量应用和/或高ASP基础设施平台非常适合ASIC）——需要驱动客户芯片设计团队的ROI/合理性论证：
- 苹果是定制ASIC的典范——他们创建/拥有整个软件栈/应用层，拥有整个系统设计，可以在平台性能/低功耗上实现差异化，并且每年出货2.5亿台（内部芯片设计研发投入回报率强劲）——将投资扩展到PC CPU、手表CPU等...
- 游戏主机（索尼/微软）——与苹果相同的价值主张——相对高产量
- 基站RAN处理器ASIC——产量小，但ASP非常高，跨整个网络/用户群实现ROI
- 谷歌TPU AI处理器、亚马逊Trainium AI处理器、Meta MTIA处理器、微软Maia AI处理器——产量小，但ASP非常高——token生成/AI变现将驱动强劲ROI

## 示例：AI GPU对比AI定制ASIC处理器

AI ASIC/XPU提供有竞争力的性能、经济性和能效

来源：公司报告，JPM

## 芯片和机架架构——TPUv7 Ironwood ASIC对比英伟达Blackwell GPU

[[KC_IMAGE_002]]

[[KC_IMAGE_003]]

[[KC_IMAGE_004]]

来源：公司报告，JPM

定制ASIC需求正在上升，因为许多大型OEM/CSP/超大规模企业正在寻求比现成芯片解决方案（或ASSP）更高的差异化、更好的性能、更低的功耗以及更低的总体拥有成本——博通（高端ASIC市场第一，80-85%份额）和Marvell（高端ASIC市场第二，10-12%份额）应继续主导这一机遇。
这些客户既不具备进行大型复杂片上系统（SOC）设计的能力，也没有广泛的片上设计模块IP组合，如高速SERDES能力或高速内存接口技术。他们需要与拥有IP和芯片设计专业知识的半导体公司合作。
数字定制AI ASIC市场在CY26年是一个约600-700亿美元的市场机遇，未来几年将以40-50%以上的复合年增长率增长：

■ 云/超大规模ASIC（AI处理器、SmartNIC、安全/视频处理器、网络/存储加速）

我们估计博通在FY26年将实现600亿美元以上的AI总收入（较FY25年的约200亿美元大幅增长），随着新产品/项目上量（Meta MTIA 3nm ASIC项目、谷歌TPUv7/V8 3nm、Anthropic（TPU）、OpenAI和软银/ARM）......预计FY27年AI收入将超过1500亿美元
我们预计Marvell在CY26年将实现约93亿美元的数据中心收入（较CY25年的约61亿美元增长），CY27年约146亿美元——强劲的光DSP出货量（800G/1.6T、相干lite、初期CPO上量）以及持续的亚马逊Trainium 3和4 ASIC合作和微软3nm Maia ASIC开始上量......总计超过25个XPU/XPU配套ASIC设计中标。

来源：JPM

## 博通ASIC管线：

累计超过100个7nm/5nm/3nm/2nm设计

强大的2nm/3nm ASIC平台（更快的上市时间）：

\* 每芯片500-1200亿+晶体管
\* 2nm/3nm/5nm小芯片架构
\* 50/100/200G已验证SERDES I/O
\* 最广泛的IP组合
\* 先进封装（HBM 3/4、2.5/3D SOIC）
\* 共封装电/光（CPO）

## Marvell ASIC管线：

累计超过70个12nm/5nm/3nm/2nm设计
开始接触<2nm

\* 每芯片500-1200亿+晶体管
\* 50/100G已验证SERDES I/O
\* SRAM内存IP（LPU）
\* 广泛IP组合
\* 先进封装

来源：JPM

[[KC_IMAGE_005]]

来源：博通和JPM

## 博通已开发出2nm/3nm AI ASIC参考平台，使客户能够快速上市：

• 2nm/3nm/5nm计算芯片
• 100/200Gbps I/O芯片
• 2.5D/3D SOIC（芯片堆叠）

• 2nm/3nm芯片堆叠
• CY26年先进基板制造能力

• 芯片到芯片I/O连接

• AI/计算/IO/内存/接口IP

• CY26年机架级系统专业知识上量

## 博通正在与5个AI ASIC客户中的3个合作开发下一代3D SOIC芯片堆叠ASIC项目

[[KC_IMAGE_006]]

来源：Marvell和JPM

## Marvell拥有强大的5nm、3nm和2nm IP组合

最近推出的HBM内存IP差异化技术可实现：

• 每个封装增加33%的HBM堆叠
• 接口功耗降低70%
• XPU硅面积增加25%
• Marvell已赢得多个与DRAM供应商合作的HBM4 ASIC逻辑基底芯片项目

[[KC_IMAGE_007]]

来源：JPM

Meta/ARM CPU公告并非博通ASIC——Meta项目仅为CPU......博通ASIC是完整的AI XPU（CPU+AI加速器）

商用（半导体公司）芯片设计流程

[[KC_IMAGE_008]]

[[KC_IMAGE_009]]

COT芯片设计流程（系统OEM/云巨头完成85-100%的设计和IP）

[[KC_IMAGE_010]]

## ASIC设计示例：

1) 谷歌TPU（博通ASIC）
2) 谷歌VCU（Marvell ASIC）
3) Meta TPU（博通ASIC）
4) 亚马逊第3代（Marvell ASIC）
5) 谷歌CPU（Marvell ASIC）
6) 思科交换（博通/Marvell）
7) 诺基亚5G BTS（博通/Marvell）
8) 三星5G BTS（Marvell ASIC）

## COT设计示例：

1) 苹果A和M系列CPU
2) 亚马逊第1/2代SoC
3) 特斯拉DOJO AI SoC
4) 思科——云规模SoC

## 博通ASIC管线更新

- Google TPU 订单持续增加 CY27 积压订单——目前 V7/V8 出货量约 650 万+……营收约 1000 亿美元
- Google 近期——TPUv7（Ironwood）每周 3000 片晶圆启动——为 2H26 强劲表现奠定基础（伴随 V8 初步上量）……支持 Google 内部及 Anthropic。

Meta 正在加速推进首个 3nm 项目（Athena），"Iris" 3nm 于 CY26 年中，"Arke" 于 CY26 年底，"Astrid" 于 1H27——新增 2nm 项目于 2H27 上量……共计五个项目——CY27 达 1GW

OpenAI（2nm/3nm）及 Softbank/ARM XPU 首颗芯片均已出晶圆厂——功能表现良好……按计划于年底/CY27 上量——OpenAI 于 CY27 达 1GW

Google/AVGO 评估 v8i "下一代"——4 个计算芯片，12 个 HBM 堆叠——将 TPUv8i 生命周期延长 6 个月……随后上量下一代 v9/v10 2nm TPU（4 个计算芯片，16 个 HBM）……任一策略均不会导致 CY28 出现营收"空窗期"（CY28 增长 70%+）

## Marvell ASIC 产品线更新

XPU ASIC Trainium 3（3nm）已于上季度开始生产——按计划于 CY26 年中上量……Trainium 4（2nm）按计划于 CY27 下半年上量
Celestial CPO 方案（与 Trainium 4 绑定）2H27 订单已现上行空间
XPU ASIC Microsoft Maia 3nm——即将流片——项目将于 CY27 年初开始上量（全 ASIC 参与——前端/后端设计）
XPU 附加：Google SmartNIC/DPU ASIC 数十亿美元/多年期订单——CY27 上量——CXL 控制器 ASIC——2H26 上量
XPU 附加：早期参与 "LPU" 推理引擎卸载（回顾 MRVL 曾因强大 SRAM 存储 IP 设计第一代 Groq LPU ASIC）——尚未获得订单，但预期乐观
