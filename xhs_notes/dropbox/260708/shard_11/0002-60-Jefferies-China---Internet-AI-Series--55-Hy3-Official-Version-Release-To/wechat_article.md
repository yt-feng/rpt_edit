# JEF：中国AI模型成本仅为美国几分之一，不是补贴而是架构优势

当市场还在争论中国大模型是否陷入价格内卷时，JEF最新发布的AI系列报告给出了一个更微妙的判断：价格竞争已经不再是主要矛盾，真正的分水岭出现在模型能否在真实工作场景中创造可量化的效率提升。

这份报告的核心信号来自腾讯Hy3正式版的发布。与预览版相比，Hy3在输入输出价格上直接腰斩——每百万token收费从2元/8元降至1元/4元。但真正值得关注的不是价格本身，而是伴随降价而来的能力跃升：任务成功率从72%提升至90%，幻觉率下降15个百分点，在文字处理和PPT生成场景中分别节省47.4%和49%的token消耗。

换句话说，中国头部模型厂商正在做的事情，不是单纯的价格竞争，而是用更低的推理成本换取更高的场景渗透率。

![研报原图 1](assets/source_image_01.jpg)

## 1. 降价的逻辑不是“烧钱换市场”，而是架构效率的自然结果

JEF在报告中提供了一个关键对比：中国模型厂商的API成本仅为美国同类产品的几分之一。以DeepSeek、Qwen、Kimi、MiniMax和智谱为代表的中国模型，其成本优势源于MoE架构、分组查询注意力机制以及更高的模型算力利用率。这不是补贴行为，而是架构选型带来的结构性优势。

腾讯Hy3的定价策略印证了这一点。在保持甚至提升核心能力的前提下，降价反而成为推动更大规模用户和场景接入的手段。报告提到，Hy3在超过50个业务单元收集反馈后进行了针对性优化，在软件开发、办公、资金、设计和游戏开发等生产力场景中验证了价值创造。

> **KC评论：** 这里的关键不是“谁更便宜”，而是“谁能在低价位下依然保持可用的效果”。Hy3在SWE-bench系列测试中与GLM-5.2、DeepSeek-V4 pro的差距正在缩小，部分场景甚至反超。对于企业采购决策者而言，模型选型的标准正从单一的价格维度转向“价格-效果-场景匹配”的三维评估。

![研报原图 2](assets/source_image_02.jpg)

## 2. token消耗指数走弱背后，是企业在主动控制推理成本

报告中的一组数据值得仔细看：基于硅动力的LLM Token消耗指数在6月28日当周继续走弱，从5月31日的2.04高点回落至1.62-1.71区间。同时，媒体报道多家科技和互联网公司正在为员工设置token消耗上限。

这传递了一个与市场直觉相反的信息：不是需求不足，而是企业开始有意识地管理推理成本。当模型能力足够好用，企业反而会更审慎地分配token预算——就像云计算时代企业对计算资源的精细化管理一样。

OpenRouter的数据也印证了这一点：6月29日当周的周token消耗量稳定在46.7万亿，没有出现爆发式增长。排名方面，DeepSeek V4 Flash位居第一，小米MiMo-V2.5和MiniMax M3紧随其后。头部模型之间的token消耗差距正在收窄，用户的选择更加分散。

![研报原图 3](assets/source_image_03.jpg)

## 3. 报告尚未完全回答的关键问题：场景渗透的拐点何时到来

JEF在报告中指出了几个值得持续跟踪的方向，但并未给出明确的时间判断。

第一个问题是，当企业开始设置token消耗上限后，后续的增长动力来自哪里。是模型能力的进一步提升带来新的使用场景，还是Agent工作流的普及推动被动消耗？报告提到了WorkBuddy在桌面端月访问量达到885万，领先于字节跳动的Trae、腾讯的QClaw和阿里巴巴的Qoder Work，但这个数据能否代表整个市场从“尝鲜”进入“依赖”阶段，仍有待观察。

第二个问题是，监管对AI拟人化服务的限制会如何影响用户增长曲线。报告提到，网信办等五部门在2026年4月发布的措施将自7月15日起实施，豆包和通义已分别于7月10日和7月15日停止相关功能。虚拟亲密关系服务曾是部分C端产品的活跃度引擎，这一限制是否会拖慢用户时长增长，报告没有给出量化判断。

> **KC评论：** 对于关注中国AI产业的研究者来说，当前阶段最值得观察的指标不是某个模型的benchmark排名，而是“单位token创造的实际业务价值”。当企业愿意为每个token付费，并主动管理消耗时，说明模型已经进入了生产环境。这才是产业化的真正起点。

## 4. 对读者的观察框架：从三个维度判断竞争格局

基于JEF报告提供的信息，可以建立一个简化的观察框架：

第一，看模型厂商的“场景密度”。不是看它们发布了多少个模型，而是看这些模型在多少真实业务场景中被调用。腾讯Hy3超过50个业务单元的反馈闭环是一个参考样本。

第二，看token消耗的“结构性变化”。是集中在少数头部模型，还是向长尾模型扩散。报告显示，DeepSeek V4 Flash的领先优势正在被追赶，这意味着竞争格局尚未固化。

第三，看“成本-能力”曲线的斜率变化。中国模型厂商在保持成本优势的同时，能否在SWE-bench Pro、Terminal-Bench等工程化能力测试中持续缩小与美国领先模型的差距。报告中的Exhibit 5和Exhibit 6提供了详细的对比数据，值得反复研读。

这份报告的真正价值不在于给出结论，而在于提供了足够多的数据锚点，让读者能够建立自己的判断框架。在AI行业，信息密度比观点本身更重要。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>
