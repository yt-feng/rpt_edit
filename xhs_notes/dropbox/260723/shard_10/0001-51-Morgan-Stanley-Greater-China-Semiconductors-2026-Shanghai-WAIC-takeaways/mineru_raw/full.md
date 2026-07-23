# 2026上海WAIC观察：中国规模化技术驱动的SuperPod演进

## 核心观察

国内AI竞争正从加速器规格向SuperPod、任务调度和全系统利用率等更高层次演进。

从新加速器到系统级扩展：2026年WAIC上，芯片新品发布有所减少，而SuperPod解决方案的展示范围显著扩大。几乎所有国内加速器厂商都展示了64卡或128卡的扩展系统，这些系统基于国内AI GPU厂商自研的扩展技术（对比全球同行——Nvidia的NVLink或AMD的UALink）。扩展技术对比详见附图4。正如我们在《中国AI加速器——谁将胜出？》中所分析的，虽然国内AI GPU在芯片层面受限于晶圆工艺，但在系统层面的光网络和服务器机架设计方面具有优势（附图11）。

中国AI计算市场的竞争焦点正从单一芯片规格转向互连、内存共享和系统可靠性：回顾2025年WAIC，当时的关注点包括：1）强劲的推理需求，2）AI应用超越聊天机器人范畴，3）华为发布384-NPU CloudMatrix 384，以及4）多家国内厂商推出新加速器。

## 其他亮点

- **AI服务器系统：华为扩展至超过1000个NPU**：华为Atlas 950将扩展域从384个Ascend 910C处理器提升至1024个下一代Ascend 950DT NPU。结合混合铜缆与光纤互连以及光路保护，Atlas 950为国内大模型训练提供了重要的硬件基础。

- **AI GPU芯片：Prefill和Decode（P/D）分离成为推理新主题**：将计算密集型的Prefill与带宽和延迟敏感的Decode分离，使运营商能够独立优化硬件分配和调度。详见下文。

- **伴随WAIC，我们于7月16-17日举办了China Tech Tour**。详见《China Tech Tour：关键要点》。

## 关于国内AI计算领域的观察

在国内AI计算领域，基于较强的订单可见性和稳健的供应链，我们关注Cambricon、Iluvatar和Hygon；对MetaX保持中性。在关键赋能环节，我们关注SMIC的先进节点产能扩张；对Hua Hong保持中性，其AI PMIC需求强劲，应能支撑特色晶圆定价。国内存储和逻辑制造的持续投入利好半导体设备领域。

---

# 2026年WAIC关键要点

## 华为昇腾：SuperPod扩展至超过1000个NPU

华为在WAIC上发布了其下一代Atlas 950 SuperPod，标志着其扩展架构的又一次重要升级：根据我们在展会上的了解，新系统主要针对华为下一代Ascend 950DT系列设计，而非当前出货的950PR系列。与2025年发布的连接384个Ascend 910C处理器的CloudMatrix 384平台相比，Atlas 950将扩展域提升至1024个NPU。该系统由16个计算柜组成，每个柜内装64个NPU，并配备4个专用的UnifiedBus互连柜，支持整个SuperPod的全互联通信。

系统级计算和内存容量显著提升：每个64-NPU计算柜可提供高达64 PFLOPS的FP8性能和128 PFLOPS的FP4性能，意味着整个SuperPod的总性能约为1 EFLOPS FP8和2 EFLOPS FP4。每个计算柜包含约6TB HBM，16个计算柜总计约96TB。通过将HBM与外部DRAM进行内存池化，华为表示总可寻址内存容量可达256TB。更大的内存池对于大模型训练尤为重要，因为模型参数、优化器状态和中间数据日益超出单个加速器节点的容量。

UnifiedBus 2.0是关键架构升级，在物理层之上扩展了统一的通信和内存协议：在每个刀片内，8个NPU通过全网格拓扑连接。在机柜层面，8个刀片（即64个NPU）通过Clos架构连接，采用全正交、无背板设计。跨机柜层面，4个UnifiedBus互连柜为整个1024-NPU系统提供光扩展架构。因此，最终架构在物理上保持分层，但在逻辑上更为扁平：UnifiedBus不将机架和互连层视为独立的通信域，而是为整个SuperPod提供统一的寻址、内存语义和加载/存储操作。

总体而言，Atlas 950将华为的SuperPod架构从数百个NPU扩展到超过1000个紧密互连的NPU，为下一代950DT平台上的大模型训练奠定了硬件基础。计算柜内采用铜缆连接、柜间采用光缆连接，在短距离带宽和能效与长距离可扩展性之间取得了平衡。华为还引入了光路保护，使单链路故障不会中断系统运行。这一点很重要，因为随着集群规模增大，通信效率和容错能力对于维持有效计算利用率和稳定训练性能变得愈发关键。

附图1：华为在2026年WAIC上展示其新款Atlas 950 SuperPod
（图片链接）

附图2：Atlas 950 SuperPod的NPU刀片
（图片链接）

附图3：Atlas 950背面主要展示UBlink采用的光互连
（图片链接）

## 蓬勃发展的SuperPod生态

如果说2025年WAIC主要是国内AI加速器的展示，那么2026年WAIC则表明竞争焦点已从单个芯片转向系统级扩展：几乎所有国内AI GPU和ASIC厂商都展示了SuperPod解决方案，通常与服务器ODM和网络合作伙伴共同开发。因此，我们在不同展台观察到多个相似甚至相同的系统设计。这反映了国内AI服务器生态系统日益模块化的特点：加速器厂商提供计算平台和软件栈，而ODM将服务器、互连、散热和电源基础设施集成到机架级或集群级解决方案中。

64-128加速器的扩展配置已日益普遍：与早期围绕八卡服务器或相对较小集群的国内系统相比，最新解决方案旨在将多个计算刀片或机架连接到一个更高带宽的扩展域内。64卡和128卡架构的广泛采用表明，国内厂商更加重视集体通信效率、内存共享和系统级利用率。然而，类似ODM开发平台的反复出现也表明，差异化将越来越取决于互连性能、软件优化、容错能力和有效应用吞吐量——而不仅仅是连接的加速器数量。

我们还观察到机架级互连的架构多样性增加，包括正交和传统线缆树解决方案：在正交架构中，前后板相互垂直排列，允许高速连接器直接跨两个平面连接。包括华为和中兴在内的国内厂商越来越青睐无背板的正交设计，这消除了传统背板中使用的大型中央PCB。这可以降低制造和良率挑战，并缩短某些电气路径。但代价是机械和连接器设计复杂性增加，而可实现带宽仍取决于连接器密度、通道损耗和信号完整性工程。

## 国内AI服务器配置仍以GPU与CPU比例约为4:1或8:1为中心

我们认为这在一定程度上反映了当前的工作负载组合。中国的智能体AI需求尚未大规模增长，而许多部署仍集中在传统模型推理或选定的训练工作负载上。国内加速器目前单卡计算性能仍低于领先的海外产品，这意味着加速器吞吐量——而非主机CPU容量——通常是主要的系统瓶颈。随着智能体工作负载的扩展，需要更多的数据预处理、编排、检索和工具执行，对额外CPU资源的需求可能会上升，从而可能随时间改变最优的CPU与加速器配置。

附图4：2026年WAIC部分关键SuperPod解决方案对比

| 解决方案 | 厂商/合作伙伴 | 规模 | 架构亮点 | 关键差异化 |
|---|---|---|---|---|
| Atlas 950 | 华为 | 1024个Ascend 950DT NPU | 16个计算柜+4个UnifiedBus柜；UnifiedBus 2.0统一内存语义；混合铜缆+光互连；最高256TB池化内存 | WAIC上展示的最大扩展域，强调大模型训练和统一内存架构 |
| MTT C256 SuperPod | 摩尔线程 | 128-256个S系列GPGPU | 单级扩展，线缆树连接 | 专注于可扩展的国产GPU集群，用于AI训练和推理 |
| Yunsui SL64-O | 燧原科技+中兴 | 64个L600 AI加速器 | 联合开发的机架级解决方案，采用无背板正交架构，集成计算、网络和散热 | 展示ODM驱动的生态协作和模块化SuperPod部署 |
| Xijing S6000 | 沐曦+中兴 | 64个C600 AI加速器 | 与Yunsui SL64-o类似，采用无背板正交架构 | 配备最新的沐曦AI训练+推理加速器C600芯片 |

来源：公司数据

附图5：燧原科技展示其与中兴联合开发的SuperPod解决方案
（图片链接）

附图6：WAIC上的无背板正交设计
（图片链接）

## P/D分离实现更高效的异构推理

降低Token成本同时提高可用加速器资源的利用率是WAIC上的另一个反复出现的主题：大模型推理包含两个特性截然不同的工作负载。Prefill并行处理输入提示，生成初始KV缓存，主要是计算密集型。Decode顺序生成后续Token，重复访问模型权重和不断增长的KV缓存，对内存带宽、延迟和批处理调度更为敏感。在同一个加速器池上运行这两个阶段可能会造成资源争用和利用率不平衡，尤其是在模型规模、提示长度和并发请求增加的情况下。

P/D分离通过将Prefill和Decode放在不同的加速器池上来解决这种不匹配：这使得运营商能够根据各自的工作负载特性配置和调度每个池，防止长时间的Prefill请求中断延迟敏感的Decode任务。它还允许使用不同的加速器进行异构部署。WAIC上讨论的一种配置将约90%的国内加速器容量分配给Prefill，10%的H2O容量分配给Decode，据称吞吐量提高了54%，P90首Token延迟降低了64%。实际收益将取决于模型架构、工作负载模式、调度和互连性能。

Attention/FFN分离可能代表下一阶段，尽管我们在WAIC上未观察到有意义的演示或基准测试结果：这种方法进一步将Decode执行划分为Attention节点（反复访问不断增长的KV缓存，对HBM容量和带宽高度敏感）和FFN节点（使用相对固定的模型权重或MoE模型中的选定专家执行更多计算密集型操作）。理论上，这可以为Attention启用高带宽、高容量内存系统，为FFN启用更面向计算的加速器。然而，两个池之间的频繁激活传输引入了大量的互连和同步要求，使得A/F分离在今天仍是一种新兴而非生产就绪的架构。

## 燧原科技发布Tiangai 300用于全阶段AI推理

燧原科技在WAIC上发布了Tiangai 300系列，将其产品定位扩展到Prefill和Decode推理：该加速器支持FP4、FP8和BF16数据格式，并将内存容量提升至144GB。根据我们的供应链了解，Tiangai 300将采用HBM3E，内存带宽约为4TB/s，这应能提升其处理带宽敏感的Decode阶段以及计算密集的Prefill工作负载的能力。燧原科技表示，该架构可以并行执行矩阵和向量运算，从而实现更快的长上下文处理。根据公司对国内大语言模型（包括DeepSeek V3.2和GLM 5.2）的测试，Tiangai 300在Prefill和Decode性能上均优于Nvidia H100。

附图7：燧原科技在WAIC上展示的新款Tiangai 300芯片
（图片链接）

## 东方计算：3D堆叠提供超越工艺缩放的另一路径

一家私营公司——东方计算，展示了其DF1000，这是一款基于国内14nm级工艺构建的软件定义近内存3D AI芯片。概念上类似于华为的T（Tao）缩放愿景，该设计使用晶圆级混合键合垂直堆叠DRAM和逻辑芯片，缩短数据传输距离，在不完全依赖领先工艺迁移的情况下解决内存墙瓶颈。该公司声称内存带宽为6.4TB/s，BF16性能为520TFLOPS，而一个128卡集群已完成全功能稳定性验证。我们认为该产品是国内厂商利用架构和先进封装来弥补工艺节点限制的又一例证。

附图8：东方计算展示了一款3D堆叠AI计算芯片
（图片链接）

## China Tech Tour：关键要点

我们于7月16-17日与多家中国半导体和AI半导体公司举行了会议。以下是我们总结的关键要点。

## 韦尔股份：智能手机CIS之外的新增长引擎

新兴市场CIS：管理层对运动相机、机器视觉、AR/VR和医疗影像持积极看法，这得益于规格升级和内容增加。运动相机CIS单设备价值量可达约40美元，而早期产品为15-20美元。机器视觉正从低分辨率传感器向数千万像素产品迁移，用于高精度检测和人形机器人，系统价值量显著增加。一次性内窥镜在医疗影像领域支持有吸引力的盈利能力，而专业相机可能从2027-28年成为另一个增长驱动力。

汽车和智能手机CIS：在海外ADAS采用的支持下，汽车需求应在季节性疲软的第一季度后恢复。部分产品的供应紧张使韦尔股份能够准备提价并传导潜在的代工厂成本上涨，而客户本地化要求应支持国内制造的使用增加。相比之下，管理层对智能手机持谨慎态度，原因是安卓出货量疲软、机型发布减少以及内存成本上升导致的规格降级。更高分辨率的产品提供了一些支持，但智能手机不太可能推动近期增长。

模拟：数据中心光模块提供了最清晰的规模和盈利路径。定制化模拟产品单芯片ASP约为2-3美元，在1.6T NPO系统中潜在价值量约为30美元。韦尔股份正在开发光电探测器、TIA、SerDes和其他光电转换产品，这得益于最近收购的通信技术专长。初始产品已开始爬坡，预计未来两年内将更广泛采用。国产替代和海外组件短缺创造了进一步的机会，尽管大多数产品仍处于开发或早期认证阶段。

## 中微公司：存储可见性依然强劲；先进逻辑机会扩大

存储客户订单：管理层认为存储代工厂是三年需求可见性较强的细分领域，这更多由本地化和技术迁移驱动，而非全球存储定价。DRAM客户继续增加产能和采购研发工具，而NAND客户专注于技术升级和设备更换。近期NAND需求部分取决于更换高深宽比刻蚀和PECVD设备，更大规模的扩张与下一代3D NAND相关。几个初步奖项正在转化为采购订单和出货，尽管2027年潜在需求的很大一部分尚未正式下达。

先进逻辑和本地化：管理层预计未来五年国内先进逻辑投资将保持强劲。设备本地化率已超过10%，而部分产线可能达到25-30%。中微公司正在为FinFET、GAA和3D架构开发平台，并表示某些产品发布仅比全球领先者晚约六个月。

产品扩展和执行：除刻蚀外，中微公司强调了在ALD、CMP、检测和计量方面的进展。海外组件交货期正在延长，但管理层预计年底交付将按计划进行。主要客户的价格谈判已不那么激烈，运营费用保持可控，随着新平台商业化，研发强度应会下降。

## 华虹半导体：定价复苏和新产能支持增长

利用率和定价：华虹的三座8英寸晶圆厂利用率约为110%，而首座12英寸晶圆厂也保持高负荷。自去年底以来，两个平台的代工价格已上涨约10-15%，2027年可能进一步上涨。需求基础广泛，目前由服务器相关应用引领，而功率半导体相对较弱。管理层将减少较弱功率产品的负荷，而不是重新利用专用产能。

产能爬坡：9A晶圆厂目前产能约为60kwpm，预计到2026年第三季度达到满产83kwpm，并在2027年上半年实现满载。主要专注于40-55nm产品，目标是在2027年底实现盈利。9B的建设已经开始，预计年底达到10-20kwpm，2027年开始量产。该晶圆厂最终将提供55kwpm产能，专注于40-28nm。明年折旧将上升，但管理层预计收入增长将超过折旧。

收购和本地化：84亿元人民币的HLMC Fab 5收购预计将于8-9月完成。该晶圆厂拥有40kwpm产能，在华虹接管运营控制后盈利能力正在改善。华虹将28nm视为特色工艺的实际极限，潜在应用包括逻辑、NOR闪存、MCU和CIS。

## 燧原科技：Tiangai 300拓宽推理覆盖范围

产品路线图：除了在WAIC上发布新产品外，燧原科技还参加了我们的会议。管理层正在等待核心客户对Tiangai 300的反馈，并表示某些性能指标超过H100，但该产品仍落后于Blackwell。Tiangai 150主要针对Prefill，而Tiangai 300扩展到Decode和训练后处理。燧原科技还在开发一个少于200个加速器的SuperPod。Tiangai 400计划于2027年流片，并将以Blackwell代际为基准。

出货量和客户：燧原科技预计今年出货约10万张卡，明年数量预计不低于此。公司最初优先考虑可扩展的推理部署，而非积极追求大型训练集群。一些互联网客户已在使用其产品，而国内大语言模型开发商近期的融资可能支持明年更强的加速器支出。管理层更倾向于能够进行有意义部署的大客户，因为支持小型安装所需的工程资源较多。

供应链和成本：燧原科技的目标是明年海外和国内产能各占约50%，具体取决于美国政策和国内制造进展。长期来看，本地化应会增加，这得益于自2023年以来开发的双芯片架构和芯片间互连。7月的布局主要是为了确保供应链资源并支持2027年增长。燧原科技拥有约100亿元人民币现金，并正在谈判额外的信贷额度。内存已占卡成本的一半以上，而代工价格也在上涨；因此Tiangai 300的定价可能包含HBM成本传导机制。

## 长电科技：加速先进封装扩张

长电科技正在加速其AI芯片封装扩张：这包括在上海临港投资78亿元人民币（11亿美元）建设新的先进封装和测试工厂，以加强AI计算、高性能芯片的产能。除了这个新宣布的工厂，位于江阴的JME也用于2.5D封装；该工厂去年实现了2亿元人民币收入。管理层认为，国内AI GPU的爬坡仍处于早期阶段，这是一个多年的结构性趋势。

长电科技在OSAT定价方面跟随市场：尽管基板供应紧张，但对生产影响有限，但可能影响新增产能。

公司维持了今年100亿元人民币的资本支出目标，并认为2027年资本支出可能更高：2026年第一季度利用率约为80%，2026年第二季度利用率环比改善。

## 中国AI半导体关键图表

附图9：我们预计中国AI GPU市场规模到2030年将增长至910亿美元
（图片链接）

附图10：我们预计中国AI芯片自给率到2030年将达到70%
（图片链接）

附图11：中美AI产业相对优势
（图片链接）

附图12：中国主流AI大语言模型平均Token价格
（图片链接）

附图13：字节跳动（火山引擎/豆包）Token激增表明AI需求旺盛
（图片链接）

附图14：中国云服务商的资本支出将成为中国AI GPU的关键需求驱动因素
（图片链接）

附图15：国内芯片在总拥有成本和每Token成本（AI大语言模型推理）方面与Nvidia面向中国的处理器相比具有竞争力
（图片链接）

---

本报告提及美国第14032号行政令和/或其中指定的实体或证券。美国人士可能被禁止购买本报告中提及的某些实体证券。读者全权负责确保其投资活动符合适用法律。

本报告提及出口管制和/或可能受出口管制限制的实体。读者全权负责确保其投资或贸易活动符合适用法律。

本报告提及美国第14105号行政令和/或可能属于该行政令范围的实体。美国人士可能被禁止进行某些交易，或需要将某些其他交易通知美国财政部。读者全权负责确保其投资或贸易活动符合适用法律。

## 披露部分

（此处为标准的法律披露和免责声明内容，为保持合规，保留原文格式和内容，但根据要求不输出具体金融操作建议和收益承诺等。由于原文披露部分包含大量金融术语和具体公司评级，为符合要求，此处进行简化处理，仅保留必要结构。）

本报告中的信息和观点由MS Asia Limited（对其内容负责）和/或MS Asia (Singapore) Pte. (Registration number 199206298Z) 和/或MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H)（由新加坡金融管理局监管，对其内容承担法律责任，如有任何相关问题应联系该机构）和/或MS Taiwan Limited 和/或MS & Co International plc, Seoul Branch 和/或MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742) 和/或MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813) 和/或MS India Company Private Limited (CIN U22990MH1998PTC115305)（由印度证券交易委员会（SEBI）监管）及其关联公司（统称“MS”）编制或传播。本报告中的所有建议均由合格的行业分析师做出。

如需了解本报告所涉及公司的重要披露、股价图表和股票评级历史，请访问MS披露网站 www.morganstanley.com/eqr/disclosures/webapp/generalresearch，或联系您的投资代表或MS。

## 分析师认证

以下分析师特此证明，他们对本报告中讨论的公司及其证券的看法准确表达，并且他们没有也不会因表达具体的建议或观点而直接或间接获得补偿：Charlie Chan; Daisy Dai, CFA; Tiffany Yeh; Daniel Yen, CFA。

## 全球研究冲突管理政策

MS已根据我们的冲突管理政策发布，该政策可在 www.morganstanley.com/institutional/research/conflictpolicies 获取。

## 关于标的公司的重要监管披露

截至2026年6月30日，MS实益拥有本报告所涵盖的以下公司一类普通股证券的1%或以上：ACM Research Inc, Advanced Micro-Fabrication Equipment Inc, Advanced Wireless Semiconductor Co, Alchip Technologies Ltd, AllRing Tech Co., AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMPT Ltd, Cambricon Technology Corporation, Dosilicon Co Ltd, FOCI Fiber Optic Communications Inc, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Hangzhou Silan Microelectronics Co. Ltd., King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, Montage Technology Co Ltd, Parade Technologies Ltd, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, SG Micro Corp., Shanghai Fudan Microelectronics, Silergy Corp., Silicon Motion, TSMC, UMC, Unigroup Guoxin Microelectronics Co Ltd, Vanguard International Semiconductor, WIN Semiconductors Corp, Winbond Electronics Corp, WPG Holdings, WT Microelectronics Co. Ltd.。

在过去12个月内，MS管理或共同管理了Alchip Technologies Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co的公开（或144A）证券发行。

在过去12个月内，MS因投资银行服务从ASMPT Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co获得报酬。

在未来3个月内，MS预计将或打算寻求从以下公司获得投资银行服务报酬：Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd.。

在过去12个月内，MS因投资银行服务以外的产品和服务从以下公司获得报酬：ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd.。

在过去12个月内，MS已向或正在向以下公司提供投资银行服务，或与以下公司存在投资银行客户关系：Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd.。

在过去12个月内，MS已向或正在向以下公司提供非投资银行、证券相关服务，和/或过去已签订协议提供服务或与以下公司存在客户关系：ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Montage Technology Co Ltd, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd.。

主要负责编制MS的股权研究分析师或策略师的薪酬基于多种因素，包括研究质量、读者客户反馈、选股、竞争因素、公司收入和整体投资银行收入。股权研究分析师或策略师的薪酬不与MS执行的投资银行或资本市场交易或特定交易台的盈利能力或收入挂钩。

MS及其关联公司从事与MS所涵盖的公司/工具有关的业务，包括做市、提供流动性、基金管理、商业银行、信贷扩展、投资服务和投资银行。MS以自营方式向客户买卖MS所涵盖公司的证券/工具。MS可能持有本报告中讨论的公司或工具的债务头寸。MS作为自营交易商交易或可能交易作为债务研究报告主题的债务证券（或相关衍生品）。

上述某些披露也是为了遵守非美国司法管辖区的适用法规。

## 股票评级

MS使用相对评级系统，采用“超配”、“标配”、“未评级”或“低配”等术语（定义见下文）。MS不对我们覆盖的股票分配“买入”、“持有”或“卖出”评级。“超配”、“标配”、“未评级”和“低配”不等同于买入、持有和卖出。读者应仔细阅读MS中使用的所有评级的定义。此外，由于MS包含分析师观点的更完整信息，读者应仔细阅读MS全文，而不要仅从评级推断内容。在任何情况下，评级（或研究）都不应被用作或依赖为研究交流。读者买卖股票的决定应取决于个人情况（例如读者现有持仓）和其他考虑因素。

## 全球股票评级分布

（截至2026年6月30日）

下文描述的股票评级适用于MS的基础股权研究，不适用于公司生产的债务研究。

仅为披露目的（根据FINRA要求），我们在“超配”、“标配”、“未评级”和“低配”评级旁边包含了“买入”、“持有”和“卖出”的类别标题。MS不对我们覆盖的股票分配“买入”、“持有”或“卖出”评级。“超配”、“标配”、“未评级”和“低配”不等同于买入、持有和卖出，而是代表建议的相对权重（见下文定义）。为满足监管要求，我们将“超配”（我们最积极的股票评级）对应为买入建议；我们将“标配”和“未评级”对应为持有建议，将“低配”对应为卖出建议。

| 股票评级类别 | 覆盖范围 | 投资银行客户（IBC） | 其他重要投资服务客户（MISC） |
|---|---|---|---|
| 超配/买入 | 1544 | 42% | 453 | 49% | 29% | 757 | 44% |
| 标配/持有 | 1577 | 43% | 390 | 42% | 25% | 769 | 44% |
| 未评级/持有 | 3 | 0% | 1 | 0% | 33% | 1 | 0% |
| 低配/卖出 | 544 | 15% | 89 | 10% | 16% | 204 | 12% |
| 总计 | 3,668 | | 933 | | | 1731 | |

数据包括当前已分配评级的普通股和ADR。投资银行客户是指MS在过去12个月内从中获得投资银行报酬的公司。由于四舍五入，“占总计百分比”列中的百分比可能不完全等于100%。

## 分析师股票评级

**超配（O）**：预计该股票的总回报在未来12-18个月内，在风险调整基础上，超过分析师行业（或行业团队）覆盖范围的平均总回报。

**标配（E）**：预计该股票的总回报在未来12-18个月内，在风险调整基础上，与分析师行业（或行业团队）覆盖范围的平均总回报一致。

**未评级（NR）**：目前分析师对该股票的总回报相对于分析师行业（或行业团队）覆盖范围的平均总回报，在风险调整基础上，没有足够的信心。

**低配（U）**：预计该股票的总回报在未来12-18个月内，在风险调整基础上，低于分析师行业（或行业团队）覆盖范围的平均总回报。

除非另有说明，MS中包含的价格目标的时间范围为12至18个月。

## 分析师行业观点

**有吸引力（A）**：分析师预计其行业覆盖范围在未来12-18个月内的表现相对于相关广泛市场基准具有吸引力，如下所示。

**中性（I）**：分析师预计其行业覆盖范围在未来12-18个月内的表现与相关广泛市场基准一致，如下所示。

**谨慎（C）**：分析师对其行业覆盖范围在未来12-18个月内的表现相对于相关广泛市场基准持谨慎态度，如下所示。

各地区基准如下：北美 - S&P 500；拉丁美洲 - 相关MSCI国家指数或MSCI拉丁美洲指数；欧洲 - MSCI欧洲；日本 - TOPIX；亚洲 - 相关MSCI国家指数或MSCI次区域指数或MSCI AC亚太（除日本）指数。

## MS Smith Barney LLC客户的重要披露

关于任何可能合理预期会影响MS Smith Barney LLC选择第三方研究提供商或第三方研究报告标的公司的重大利益冲突的重要披露，可在MS财富管理披露网站 www.morganstanley.com/online/researchdisclosures 上获取。对于MS的具体披露，您可以参考 https://www.morganstanley.com/eqr/disclosures/webapp/generalresearch。

每份MS报告均由代表MS Smith Barney LLC的人员审查和批准。此审查和批准由审查MS研究报告的同一人进行。这可能会产生利益冲突。

## 其他重要披露

MS的政策是根据研究分析师和研究管理层认为适当的情况，基于发行人、行业或市场的发展可能对研究观点或意见产生重大影响，更新研究报告。此外，某些研究出版物旨在定期更新（每周/每月/每季度/每年），并且通常会按此频率更新，除非研究分析师和研究管理层根据当前情况确定不同的发布时间表是适当的。

MS不担任市政顾问，本文包含的意见或观点无意也不构成《多德-弗兰克华尔街改革和消费者保护法》第975条意义上的建议。

MS生产一种称为“战术想法”的股权研究产品。关于特定股票的“战术想法”中包含的观点可能与针对同一股票的研究中表达的建议或观点相反。这可能是由于不同的时间范围、方法论、市场事件或其他因素造成的。如需获取特定股票的所有研究，请联系您的销售代表或访问Matrix网站 http://www.morganstanley.com/matrix。

MS通过我们在Matrix上的专有研究门户网站提供给我们的客户，并由MS以电子方式分发给客户。某些（但非全部）MS产品也通过第三方供应商提供给客户，或通过替代电子方式重新分发给客户，以方便起见。如需访问所有可用的MS，请联系您的销售代表或访问Matrix网站 http://www.morganstanley.com/matrix。

任何访问和/或使用MS均须遵守MS的使用条款（http://www.morganstanley.com/terms.html）。通过访问和/或使用MS，您表示您已阅读并同意受我们的使用条款（http://www.morganstanley.com/terms.html）的约束。此外，您同意MS根据我们的隐私政策和全球Cookie政策（http://www.morganstanley.com/privacy_pledge.html）处理您的个人数据并使用Cookie，包括用于设置您的偏好和收集读者数据，以便我们为您提供更好、更个性化的服务和产品。要了解有关MS如何处理个人数据、我们如何使用Cookie以及如何拒绝Cookie的更多信息，请参阅我们的隐私政策和全球Cookie政策（http://www.morganstanley.com/privacy_pledge.html）。请使用提供的链接查看MS India Company Private Limited的条款和条件以及最重要的条款和条件（https://www.morganstanley.com/assets/pdfs/about-us-global-offices/india/Terms_and_conditions.pdf），并使用以下链接查看审计报告（https://ny.matrix.ms.com/eqr/research/webapp/researchdocs/MSICPL_Morgan_Stanley_Research_Audit_Report.pdf）。

如果您不同意我们的使用条款和/或您不希望同意MS处理您的个人数据或使用Cookie，请不要访问我们的研究。MS不提供量身定制的个人研究交流。MS的编制未考虑接收者的具体情况和目标。MS建议读者独立评估特定的投资和策略，并鼓励读者寻求财务顾问的建议。投资或策略的适当性将取决于读者的具体情况和目标。MS中讨论的证券、工具或策略可能不适合所有读者，某些读者可能没有资格购买或参与其中部分或全部。MS不是购买或出售任何证券/工具或参与任何特定交易策略的要约或要约邀请。您的研究价值和收入可能会因利率、汇率、违约率、提前还款率、证券/工具价格、市场指数、公司的运营或财务状况或其他因素的变化而波动。证券/工具交易中期权或其他权利的行使可能存在时间限制。过往表现不一定是未来表现的指南。对未来表现的估计基于可能无法实现的假设。如果提供，除非另有说明，封面上的收盘价是标的公司证券/工具的主要交易所价格。

主要负责编制MS的固定收益研究分析师、策略师或经济学家的薪酬基于多种因素，包括质量、准确性和研究价值、公司盈利能力或收入（包括固定收益交易和资本市场盈利能力或收入）、客户反馈和竞争因素。固定收益研究分析师、策略师或经济学家的薪酬不与MS执行的投资银行或资本市场交易或特定交易台的盈利能力或收入挂钩。

MS中“关于标的公司的重要监管披露”部分列出了MS持有1%或以上公司普通股证券的所有公司。对于MS中提及的所有其他公司，MS可能持有少于1%的证券/工具或衍生品，并且可能以与MS中讨论的方式不同的方式进行交易。未参与MS编制的MS员工可能持有所提及公司的证券/工具或衍生品，并且可能以与MS中讨论的方式不同的方式进行交易。衍生品可能由MS或关联人士发行。

除有关MS的信息外，MS基于公开信息。MS尽一切努力使用可靠、全面的信息，但我们不保证其准确或完整。我们没有义务在MS中的意见或信息发生变化时通知您，除非我们打算停止对标的公司的股权研究覆盖。MS中提出的事实和观点未经MS其他业务领域的专业人士审查，可能不反映他们所知的信息，包括投资银行人员。

MS人员可能参与公司活动，例如实地考察，并且通常被禁止接受公司支付相关费用，除非事先获得研究管理层的授权成员批准。

MS可能做出与本报告中的建议或观点不一致的投资决策。

致我们位于台湾或交易台湾证券/工具的读者：关于在台湾交易的证券/工具的信息由MS Taiwan Limited（“MSTL”）分发。此类信息仅供您参考。读者应独立评估投资风险，并对其投资决策全权负责。未经MS明确书面同意，MS不得向公共媒体分发或引用或由公共媒体使用。在台湾证券交易所推荐法规第7-1条范围内的任何非客户读者访问和/或接收MS，不得将MS提供给任何第三方（包括但不限于关联方、关联公司和任何其他第三方）或从事任何可能产生或看似产生利益冲突的与MS相关的活动。关于不在台湾交易的证券/工具的信息仅供参考，不得解释为建议或要约交易此类证券/工具。MSTL可能不为客户执行这些证券/工具的交易。

MS中的某些信息由MS Asia Limited上海代表处的员工为MS Asia Limited的使用而获取。MS未根据中国法律注册，与本报告相关的研究在中国境外进行。MS不构成在中国境内出售或要约购买任何证券的要约。中国读者应具有投资此类证券的相关资格，并应自行负责从相关政府机构获得所有必要的批准、许可、验证和/或注册。本报告或其任何部分均不旨在也不构成中国法律定义的证券投资咨询或顾问服务。此类信息仅供您参考。

MS在巴西由MS C.T.V.M. S.A.分发，地址为Av. Brigadeiro Faria Lima, 3600, 6th floor, São Paulo - SP, Brazil；由Comissão de Valores Mobiliários监管；在墨西哥由MS México, Casa de Bolsa, S.A. de C.V分发
