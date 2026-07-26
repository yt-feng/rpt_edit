# BARC：BARC估算，Google向SPV出售每颗TPU的价格约为2万美

Google正在启动一项规模可能被市场低估的新业务模式：将TPU作为独立硬件销售给外部客户，而非仅通过Google Cloud Platform租赁。BARC在最新报告中拆解了这一模式的结构、激励逻辑与财务影响，认为到2028年，TPU即服务可能为Alphabet带来约2500亿美元的外部收入，相当于当前市场共识营收预期的36%以上。

这一判断的基础是两份近期公开信息。5月，Blackstone与Google Cloud成立合资企业，由前Google基础设施高管负责运营，首期0.5 GW的TPU即服务能力将在2027年上线。6月，Broadcom与Blackstone、Apollo共同宣布AI XPV平台，目标是在2028年前部署20 GW的AI计算能力，其中约15 GW将使用Google的TPU。BARC估算，Google向SPV出售每颗TPU的价格约为2万美元，毛利率约25%，对应每GW约143亿美元的收入。

![研报原图 1](assets/source_image_01.jpg)

## 1. Google为何选择出售而非自用TPU

如果Google自身也面临计算资源约束，为何不将所有TPU保留在GCP内部？BARC认为有四个原因。第一，Alphabet自身能部署的AI资本支出存在自然上限，包括资金和电力两方面。第二，部分大型GCP客户——如Anthropic——越来越要求对计算资源拥有更多控制权和灵活性，并愿意为此付费。第三，TPU即服务是一种轻资产方式，有助于将更多AI开发者和实验室生态标准化在TPU架构上，带来长期生态收益。第四，出售TPU而非提供服务，使Alphabet与下游AI应用中可能出现的版权、安全、隐私等责任保持距离。

> **KC评论：** 第四点容易被忽略。如果AI训练和推理过程中出现合规问题，云服务商可能承担连带责任。通过硬件销售模式，Google将这部分不确定性转移给了客户和SPV结构。

![研报原图 2](assets/source_image_02.jpg)

## 2. 从GCP租赁到自控计算：AI实验室的算力宏观环境学变化

对于Anthropic这样的AI实验室，TPU即服务模式提供了GCP租赁无法实现的三项价值。其一，通过SPV拥有计算资产后，实验室可以获得更底层的TPU访问权限，实现更精细的计算定制。其二，垂直整合能力增强，不再受限于超大规模云服务商的服务协议条款。其三，即使这种不确定性目前看来概率较低，控制计算资源也意味着实验室的业务模式不会因违反云服务使用政策而被单方面终止。

BARC对1 GW集群的对比分析显示，通过GCP租赁时，AI实验室的总资本支出约为200亿美元，而通过TPU即服务模式则需要250亿美元。但后者带来的推理收入与前者相同，约为66.7亿美元，只是推理利润率从70%降至63%。这意味着AI实验室为获得控制权付出了约7个百分点的利润率代价。

![研报原图 3](assets/source_image_03.jpg)

## 3. 财务影响：2500亿美元收入与15%的毛利润增量

BARC的测算框架显示，到2028年，外部TPU出货量可能达到约474万颗，对应11.5 GW的计算能力。按每颗TPU 5.3万美元的平均售价计算，当年外部TPU收入约为2527亿美元，毛利润约632亿美元。这相当于对当前市场共识中Alphabet 2028年总营收的36%上行空间，以及对毛利润的15%上行空间。

报告特别指出，Google在2026年第二季度财报中披露的811亿美元采购承诺——较上一季度增加479亿美元——以及过去6个月内超过2750亿美元的积压订单增长，都指向这一模式的规模可能远超市场预期。BARC认为，这种轻资产的AI基础设施方式还可能降低Google未来的资本支出增速，对其此前500亿美元的2028年资本支出预测构成节奏变化不确定性。

## 4. 生态链中的赢家与结构变化

TPU即服务模式的影响不限于Google本身。Broadcom作为TPU的联合设计方，将获得一个新的收入来源，并使其客户基础从Google扩展到其他合作伙伴。Blackstone等机构则获得了规模化研究AI基础设施的新资金工具。Fluidstack作为托管服务提供商，其角色从Google墙外的“智能手”扩展为TPU的专属云服务商，近期融资可能正是为此布局。

BARC认为，这一模式使TPU有机会成为AI开发者社区的行业标准，而不仅仅是Google云平台内部的专有硬件。对于读者而言，关注点不应仅限于Google的云收入增长，还应理解TPU即服务如何改变AI基础设施的资金结构、不确定性分配和生态竞争格局。

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
