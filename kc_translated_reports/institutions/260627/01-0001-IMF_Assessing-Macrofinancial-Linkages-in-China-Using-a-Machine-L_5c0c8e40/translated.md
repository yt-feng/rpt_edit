# 利用机器学习精简向量自回归模型评估中国的宏观金融关联

国际货币基金组织工作论文描述作者正在进行的研究，发布旨在征求意见并鼓励讨论。工作论文中表达的观点仅代表作者本人，不一定代表国际货币基金组织、其执行董事会或管理层。

2026年
6月

[[KC_IMAGE_001]]

# 国际货币基金组织工作论文 货币与资本市场部

利用机器学习精简向量自回归模型评估中国的宏观金融关联 编制人：Jin-Chuan Duan\*, Dimitrios Laliotis\*\*, 和 Wei Sun\*\*，

经 Hiroko Oura 授权发布
2026年6月

国际货币基金组织工作论文描述作者正在进行的研究，发布旨在征求意见并鼓励讨论。工作论文中表达的观点仅代表作者本人，不一定代表国际货币基金组织、其执行董事会或管理层。

摘要：本文研究了中国的房地产开发商、金融机构与宏观经济结果之间的宏观金融关联。利用机器学习算法实现的精简向量自回归模型，本文量化了异质性冲击如何跨部门传导和放大，并可能对金融稳定产生影响。源自民营开发商和区域性金融机构的压力——尽管规模相对有限——可通过借贷关系、共同敞口、共享市场以及市场情绪变化产生持续的溢出效应。房价下跌可能削弱投资、打击消费者信心，并对房地产和金融部门的健康产生不利影响，从而扰乱金融中介并拖累更广泛的经济增长。政策考量应考虑到这些反馈循环。基于市场和敞口的工具有助于监测宏观金融关联并评估冲击的传导。

# 利用机器学习精简向量自回归模型评估中国的宏观金融关联

编制人：Jin-Chuan Duan, Dimitrios Laliotis, 和 Wei Sun

## 目录

I. 引言 .... 3
II. 文献综述 .... 5
III. 方法论设计 .... 6
数据 .... 7
模型选择 .... 9
IV. 实证结果 .... 10
模型估计 .... 10
脉冲响应 .... 13
V. 结论 .... 17
参考文献 .... 18

## 图表

1. 脉冲响应：民营开发商违约概率的1个基点冲击 ....14
2. 脉冲响应：城市商业银行违约概率的1个基点冲击 ....15
3. 脉冲响应：房价的1个百分点冲击 ....16
4. 脉冲响应：消费者信心指数的1个百分点冲击 ....16

## 表格

1. 跨期关系：回归系数 .... 12
2. 同期关系：扰动项协方差 .... 13

## I. 引言

宏观金融稳定是全球政策议程的核心目标。自1980年代以来，一系列银行业和金融危机表明，金融稳定与价格稳定一样，对于宏观经济韧性至关重要。2007-09年的全球金融危机凸显了宏观金融关联的深远影响，促使全球经济政策转向更加宏观审慎的方向（Claeseens, 2015; Adrian, 2017b; 以及 IMF-FSB-BIS, 2016）。这些努力旨在通过传统货币和汇率工具无法完全管理的复杂关联来解决传导和放大效应（Borio et al., 2022）。

宏观金融关联指的是宏观经济与金融部门之间的双向互动（Claessens and Kose, 2018）。经济冲击可能损害家庭、企业和金融中介的资产负债表。在金融市场不完美的放大作用下，此类损害可能扰乱金融中介的需求（如金融加速器效应）和供给（如银行贷款、资本、杠杆、流动性约束），从而加剧经济波动。金融失衡——如信贷快速增长和资产价格波动——可能扭曲宏观经济均衡，若未能及时解决，往往先于衰退或加深衰退（Claessens et al., 2012a）。

尽管关于宏观金融关联的研究不断推进，但由于数据限制和方法论约束，挑战依然存在。对于系统性风险评估至关重要的资产负债表数据、双边敞口以及高频资产价格序列仍存在巨大缺口（Brunnermeier and Krishnamurthy, 2014）。理论模型，包括动态随机一般均衡框架，难以捕捉主体异质性、展示传导渠道，或在不同的制度设置下产生稳健的预测（Blanchard, 2017a）。

本文通过评估中国的宏观金融关联，为不断发展的文献做出贡献。中国现在是世界第二大经济体和第二大金融体系所在地。中国的增长模式，直到最近仍严重依赖房地产投资，并得到日益复杂和相互关联、但并未完全反映风险收益关系的金融中介的支持（IMF, 2025），这催生了错综复杂的宏观金融关联，可能产生深远的宏观经济后果。

周期性冲击使得这一分析尤为及时。自2021年以来，中国的房地产市场经历了数十年来最严重的调整。一级市场的销售和价格已经下降。二级市场的调整更为显著，尽管在2025年初左右出现暂时反弹。房地产开发商——规模和所有权结构各异——的违约事件有所增加。闲置土地、未完工项目和未交付住房单元的累积造成了巨大的社会经济成本。

本文揭示了受房地产市场表现影响并对其产生影响的关键经济主体和活动之间的相互关联性。使用向量自回归模型来捕捉一般均衡特征和内生反应。通过已识别的传导和放大渠道，我们量化了异质性冲击产生深远且持久影响的程度。

本文的一个关键特征是基于微观经济行为分析宏观金融关联（Claessens and Kose, 2018）。模型包括三个房地产开发部门和五个金融部门，每个部门在应对冲击时面临不同的约束。国有开发商更容易获得银行融资，而民营开发商通常依赖成本更高的资金，并在压力时期失去市场准入。国有银行资金来源相对稳定，服务于更安全的借款人，而较小的银行则从事风险更高的金融市场交易并向开发商放贷。非银行金融机构支持资本向非国有部门配置，在近期监管收紧之前通常提供隐性担保（Allen et al., 2023）。

为解决与资产负债表和双边风险敞口相关的数据局限性，我们采用新加坡国立大学信用研究倡议（NUS-CRI, 2023）的违约概率指标。CRI数据库覆盖全球92,000家公司，包括中国所有上市房地产开发商和金融机构。作为包含市场指标（如股票收益率和波动性）与基本面指标（如流动性、盈利能力和杠杆率）的综合指数，违约概率的联动性比纯粹基于市场的指标（如CDS利差或股价）更能反映双边风险敞口（Craig et al., 2024）。它们还通过情绪和市场认知反映了超越直接借贷关系的相互依存性。

在VAR框架中对八个行业变量和三个宏观变量进行建模是一项高维挑战。为识别有意义的宏观金融关联，我们应用零范数惩罚来正则化非零系数的数量（Duan, 2024）。在操作上，使用序贯蒙特卡洛优化技术求解10折交叉验证的似不相关回归似然函数。这种新颖的机器学习方法具有若干优势：它生成一个简约模型，仅保留显著关系，且无需事先指定方向性链接。该模型完全可解释，避免了众多模型的"黑箱"特性，支持透明的政策分析（Duan, 2025）。

我们的实证分析揭示了宏观经济表现、房地产开发商与金融机构之间的关键关联。通过这些关联可能形成恶性循环，放大特质性冲击。值得注意的是，私营开发商的压力会在后续时期影响国有开发商和金融机构。即使是规模较小、区域性的银行也可能产生系统性影响。房价处于这些关联的核心，其下跌会对投资、情绪和金融部门健康产生不利影响。

实证分析表明，资本充足且资金来源稳定的金融体系与维持信贷和流动性供应的更大能力相关。影响房地产开发商的措施与更广泛的金融部门韧性考量之间可能存在潜在权衡。当与持久恢复商业和消费者信心的更广泛努力相结合时，稳定房价更为有效。房地产市场的可持续复苏通常以关键市场参与者财务健康支撑的有机交易增长为特征。考虑复杂的反馈效应有助于描述商业周期中的宏观金融动态。

基于市场和综合指数的分析为宏观金融关联及冲击引发的结果提供了及时洞察。它们还超越了借贷关系，纳入了商业模式相似性、共同风险敞口和市场情绪——这些在现代传染动态中日益重要的因素。开发综合工具包以定期监测关联并评估宏观金融影响，可以增强风险管理。收集细粒度跨部门风险敞口的补充努力可进一步加深对中国宏观金融复杂性的理解。

本文其余部分结构如下。第二部分简要评述相关文献。第三部分介绍方法论设计。第四部分讨论实证结果。第五部分总结。

## II. 文献综述

本文基于两股文献。首先，它有助于研究宏观金融关联，这一领域在全球金融危机后受到重视。金融部门与实体经济之间的双向互动可以传播和放大冲击，留下持久的经济伤痕。政策制定者一直难以使用传统的财政、货币和金融工具来抵消这些影响（Claessens and Kose, 2018）。

关于宏观金融关联的文献强调了资产价格在驱动经济结果中的核心作用。在无摩擦的阿罗-德布鲁市场中，资产价格为经济主体提供信号，以做出最优消费和投资决策（Geanakoplos, 2008）。资产价格变动影响家庭在整个生命周期中的财富，从而影响消费和储蓄模式（Deaton, 1992; Guiso and Sodini, 2013）。它们还预示未来企业盈利能力（Allen, 1993）并影响投资计划。伴随资产价格暴跌的衰退往往更深、更持久（Claessens et al., 2012a; Drehmann et al., 2012; and Muir, 2017）。在资产类别中，房价对消费的影响比股价更为显著（Carroll et al., 2011; Case et al., 2005, 2013; Kim, 2004; Gan 2010）。

由于信息不对称和执行困难，金融不完善放大了冲击对实体经济的影响。在需求侧，金融加速器理论解释了初始冲击如何影响信贷需求以及随后的支出和投资决策。最值得注意的是，资产负债表和现金流的恶化会扰乱融资渠道或增加成本。额外溢价降低了收入和盈利能力，推迟了消费或生产活动，这反过来又使获取未来融资变得更加困难（Antony and Broer, 2010; BCBS, 2011; Coric, 2011; Quadrini, 2011）。

在供给侧，银行可能因不确定性而在困境期间缩减贷款（例如，Bernanke and Blinder, 1988; Stein, 1998）。出于资本保全动机，它们可能回避风险借款人（Bernanke and Lown, 1991; Holmström and Tirole, 1997; Repullo and Suarez, 2000; Van den Heuvel, 2006, 2008）。顺周期杠杆（Adrian and Shin, 2008, 2011a; Geanakoplos, 2010）可能限制融资渠道，影响银行和非银行金融机构。银行间市场冻结可能引发信贷紧缩（Freixas and Jorge, 2008; Bruche and Suarez, 2010），去杠杆和流动性囤积可能加剧金融和经济压力。

在中国，房地产市场波动显著影响商业周期（Ge et al., 2022）。过去几十年房价上涨通过地方政府土地出让和以土地为抵押品的表外借款支持了财政支出（Chen et al., 2020）。房价上涨还通过财富效应支持了消费，因为家庭将大量储蓄投资于这一提供卓越回报的首选工具（Fang et al., 2015）。传统银行部门支持了房地产开发，直至2009年后的紧缩货币政策（Chen, et al., 2018）。非银行金融机构后来填补了这一空白，提供隐性担保，直至最近的监管变革（Allen et al., 2023）。

3/8

第二类文献聚焦于高维数据的模型选择。正则化技术解决了回归变量过多而观测值过少的问题。LASSO方法（Tibshirani, 1996）在原始优化问题中引入了 $L^{1}$ 范数惩罚项，通过收缩系数绝对值之和来优化目标函数，使许多系数归零。

后续研究通过实现Oracle性质推进了基于 $L^{1}$ 范数的方法论，即其表现与预先已知真实模型时一样出色（Fan and Li, 2001）。例如Fan（1997）提出的SCAD方法。Fan and Li（2001）将SCAD方法推广至更多参数和非参数模型，并开发了提升计算效率的算法。与原始LASSO方法中应用固定权重不同，Zou（2006）提出的Adaptive Lasso根据系数的相对重要性使用不同权重进行惩罚，同时生成一致的模型估计。

采用零范数惩罚的回归直接限制非零系数的数量，而非绝对值之和。这类模型在概念上天然适用于处理高维问题，但计算成本高昂（Natarajan, 1995）。借助现代机器学习技术，Duan（2024）提出了适用于各类高维参数模型的SCOFS。SCOFS比LASSO类方法更有效地缓解了多重共线性和过拟合问题。

本文应用SCOFS评估中国宏观金融关联性。实证证据表明，房地产市场冲击具有持续的宏观经济效应。在微观层面，金融与房地产部门以放大冲击的方式相互关联。

## III. 方法论设计

我们设计了一个惩罚VAR模型来研究中国的宏观金融关联性。简化型VAR模型若未预先指定方向性关系则无法识别。为避免对复杂系统做出过度简化的假设，我们引入零范数惩罚来正则化非零系数的数量。该方法使包含持续滞后效应的高维模型成为可能。机器学习的最新进展使这种正则化在计算上可行且完全可解释，不同于"黑箱"替代方案。

随后进行的脉冲响应分析量化了特质性冲击对相关变量随时间的影响。这与预测误差方差分解有所不同但互为补充，后者衡量的是波动溢出效应（Diebold and Yilmaz, 2012）。

我们选取了11个宏观与部门变量来支撑VAR模型。这些变量代表可能高度依赖或影响房地产市场的经济主体与活动。房价、消费者信心和房地产投资作为捕捉市场与宏观经济状况的代理变量。这些月度序列与国民账户数据密切相关，但频率更高且更具前瞻性。价格反映现金流预期和投资机会，而消费者信心反映需求压力并可能塑造未来消费行为。

部门变量包括八组房地产开发商和金融机构的违约概率指标。与基于风险暴露或价格的指标不同，综合PD指数融合了市场与基本面信息，反映部门健康状况。我们基于PD的关联性分析并非旨在隔离单一冲击传导渠道，而是捕捉可能由共同风险暴露、商业模式相似性、市场情绪及借贷关系共同驱动的协同变动（Craig et al., 2024），揭示一个由相互关联的微观部门构成的复杂系统。

选择11个变量旨在聚焦关键部门间的基本反馈效应。鉴于部分变量是反映多重潜在力量（如政策变化、共同宏观冲击和情绪）的综合指数，脉冲分析并非旨在捕捉任何特定结构性扰动的影响，而是依赖于简化型模型所隐含的传导动态。尽管如此，该高维VAR框架可容纳更多政策指标，以支持未来工作中包括制度变迁在内的更细致讨论。

## 数据

我们使用2011年至2023年的月度时间序列。丰富的时间维度允许VAR模型包含最多12期滞后，以捕捉持续的时间效应。

## 部门PD

我们使用八个部门层面的PD序列来反映选定房地产开发商和金融机构的信用状况。PD衡量实体在未来期限内无法履行财务义务的概率。这些PD基于Duan et al.（2012）的前向强度模型生成，由新加坡国立大学信用研究倡议（NUS-CRI, 2023）发布。该模型针对约7500家中国上市公司进行校准，包括因并购等原因已违约或退市的公司。

在前向强度模型中，申请破产、本金或利息支付延迟超过30天等事件被视为违约，而仅债券价格急剧下跌则不归类为违约（NUS-CRI, 2023）。该模型使用两组解释变量：（i）金融状况——利率、股票市场回报和信贷周期指标；（ii）实体层面基本面——杠杆率、流动性、盈利能力、规模和股票市场波动性。PD指标对中国实体展现出强大的预测准确性（NUS-CRI, 2023）。与其他流行的基于价格的指标（如股票回报和CDS利差）相比，PD相关性更能反映直接和间接风险暴露（Craig et al., 2024）。

我们将222家上市房地产开发商分为三组：民营（110家）、国有（51家）和物业服务公司（61家）。三个部门PD以各组成实体的中位数计算 $^{1}$ 。虽然未涵盖中国开发商的全样本，但样本包含了影响市场情绪的最Daiwa主要公司。尽管抵押贷款在银行贷款中占比较大，但本文未将家庭作为独立部门纳入。健康的贷款价值比和低违约率迄今仅构成有限的金融稳定风险。我们仅通过后文讨论的宏观消费者信心指数考虑对家庭消费的影响。

4/8

所有权结构的区分旨在捕捉冲击可能引发的异质性反应。民营房企率先遭遇销售下滑和违约。国有企业开发商最初维持了销售，这很可能得益于市场对其政府背景的隐性背书。物业服务公司（如物业管理公司）的业绩可能跟随更广泛的市场趋势，或保持非周期性，具体取决于其管理物业的收入。

我们将119家上市金融机构分为五类——国有商业银行（6家）、股份制银行（10家）、城市商业银行（30家）、农村商业银行（13家）和非银行金融机构（60家）。由于业务模式和市场认知的差异，这些细分领域对冲击的敏感度及系统性影响可能不同。违约概率中位数采用类似方法计算。

国有银行和股份制银行是全国性机构，约占中国银行体系总资产的60%。国有银行拥有相对稳定的存款基础，并向风险较低的居民和企业发放贷款。股份制银行中民营资本占比较高，更依赖批发融资（例如企业存款和同业拆借），并向风险较高的企业放贷。城商行和农商行专注于区域市场，规模较小，且至少部分由政府注资。许多股份制银行和城商行将大量资产配置于高收益、低资本占用的“其他投资”，这些投资包括非银行金融机构发行的资管产品。

非银行金融机构规模相对较小，但在以银行为中心的中国金融体系中普遍存在。我们的样本包括上市资产管理公司、信托公司和证券公司（即经纪交易商），为简便起见，后文统称为“资产管理公司”。这些实体从银行借款、动用信贷额度，并将资源中介至风险较高的领域，例如房地产开发。它们在不同监管机构的管辖下提供类似的投资产品。与这些产品相关的隐性担保，是支持资本向非国有实体配置的次优方案（Allen et al., 2023）。

## 宏观经济指标

我们使用了三个变量——房价、消费者信心和房地产投资——来捕捉关键的宏观经济结果。房价是宏观金融联系的核心（Claessens and Kose, 2018），并在中国的商业周期动态中发挥核心作用（Ge et al., 2022）。房价通过财富效应影响消费，因为房地产资产仍是家庭的主要储蓄工具（Fang et al., 2015）。房价也影响财政表现，因为地方政府严重依赖土地出让收入来补充预算（Chen et al., 2020）。开发商和地方政府融资平台普遍使用土地和房产作为抵押品向金融中介借款。因此，抵押品估值的任何变化都会直接影响杠杆和投资决策。

我们纳入了消费者信心指数以捕捉需求压力，这种压力可能通过预期渠道形成自我强化的周期（Chen and Wen, 2017）。我们还使用了房地产投资——这密切反映了开发商的活动——来追踪短期经济动能（Fang et al., 2015）。这两个月度指标与国民账户中的消费和增长模式紧密相关，同时其高频特性提供了更丰富的变化，并通过保持与违约概率数据集的一致性，便利了模型实施。

## 模型选择

我们设定了一个标准向量自回归模型，形式如下：

$$
\boldsymbol {X} _ {t} = \boldsymbol {A} + \sum_ {j = 1} ^ {1 2} \boldsymbol {B} _ {j} \boldsymbol {X} _ {t - j} + \boldsymbol {\epsilon} _ {t}\tag{1}
$$

这里，$X_{t}$ 代表一个包含11个变量的向量——三个开发商组别、五个金融机构组别的行业违约概率，以及三个宏观经济指标。每个变量都由其自身滞后项及其他变量最多12个月的滞后项来解释。A 和 $B_{j}$ 分别是截距项和斜率系数。$B_{j}$ 一旦被识别，即意味着格兰杰因果关系。扰动项 $\epsilon_{t}$ 可能存在截面相关性。

这个由11个方程组成的系统有1,463个系数和66个残差协方差需要估计，若无正则化则无法识别。为避免武断假设，我们应用零范数惩罚，在固定非零系数数量的同时，选择最佳的特征组合，并确定最佳的非零系数数量。最优解会将不重要的系数强制归零，仅保留显著且有意义的系数。尽管计算量更大，但零范数正则化在概念上优于 $L^1$ 范数，后者通过像LASSO和自适应LASSO方法那样收缩非零系数的数值总和来间接实现这一目标（Fan, 1997; Fan and Li, 2001; Zou, 2006）。

我们使用由Duan（2024）开发的稳定组合优化特征选择器方法来求解带惩罚的向量自回归模型。具体来说，SCOFS最大化一个k折交叉验证的似不相关回归目标函数：

$$
a r g m a x _ {\{p _ {l} \leq p _ {s} \leq p _ {u}, \mathbf {X} _ {t - 1} ^ {(p _ {s})} \}} \exp \left\{\lambda \sum_ {j = 1} ^ {k} L \left(\hat {\theta} _ {j -}; [ \mathbf {X} _ {t}, \mathbf {X} _ {t - 1} ^ {(p _ {s})} ] _ {j -}, t \in T\right) \right\}\tag{2}
$$

这里，$\mathbf{X}_{t-1}^{(p_{s})}$ 表示 $\{1, X_{t-1}, X_{t-2}, ..., X_{t-l_{max}}\}$ 中 $p_{s}$ 个元素的一个子集。$\hat{\theta}$ 是最优参数集。$L(\cdot; \cdot)$ 是向量自回归模型的对数似然函数。$\lambda$ 是一个用于数值精度的正自适应装置，用于调整完全离散的目标函数。我们设定k=10，即将观测值分为10个子样本用于训练和测试。在每次验证中，交叉验证技术最大化第j折（即测试数据）的样本外拟合度，同时使用除第j折之外的所有数据训练的参数。如Duan（2024）所示，多次验证练习也增强了估计的稳健性和稳定性。

SCOFS技术选择最优的非零系数数量 $p_{s}$，以及在 $p_{l}$ 和 $p_{u}$ 界定的所有允许变量组合中的最优 $p_{s}$ 变量组合。它通过不允许所选模型中存在不显著的解释变量，来解决潜在的过拟合问题。这些特性使SCOFS成为选择适用于典型操作需求的简约且稳定的向量自回归模型的理想技术。其透明度和可解释性有助于支持政策解读和审议。

在操作层面，段（2024）采用了一种分布调整的序贯蒙特卡洛（SMC）抽样方法，通过机器学习来寻找由SCOFS设定的最优简约模型。SMC是一种基于模拟的算法，它首先将目标函数（无论是统计的还是非统计的）转换为一个分布/密度函数，进而能够以序贯方式进行蒙特卡洛抽样。在我们的语境中，SMC算法通过为每个潜在的 $p_{s}$ 个滞后回归变量组合分配一个概率或重要性权重来初始化。因此，一个包含 $p_{s}$ 个变量的抽样器与一个初始概率分布相关联。这些重要性权重自然是不均匀的，需要重新抽样来平衡权重。该算法随后通过Metropolis-Hastings移动来增强经验支持，以去除因重新抽样而产生的重复粒子。这三个步骤持续进行，直到目标函数稳定并达到其最大值。关于SMC优化在各种常见模型上的全面综述，可参见段等人（2022）的研究。

一旦选定最优模型并估计出系数，实证设计便以一系列脉冲响应分析作为收尾。这些分析量化了某个感兴趣变量（例如房地产价格）受到的特定冲击，通过内生响应，随时间推移对宏观金融结果产生的影响。总影响结合了跨期（即回归系数）和同期（即扰动项之间的相关性）传导渠道的放大效应。

## IV. 实证结果

本节展示了机器学习选出的模型以及若干脉冲响应分析。所选模型是稀疏的，因为它剔除了微小且不显著的关系，并解决了任何潜在的过拟合问题。该模型也是最优的，因为在所有可能的变量选择排列中，它实现了接近理论最大值的 $R^{2}$。在每次脉冲响应分析中，我们分别对开发商健康状况、金融机构健康状况、房地产价格或消费者情绪施加一次特定的冲击。随后，我们通过它们的跨期和同期关系，量化随时间推移对每个其他变量的综合影响。

## 模型估计

机器学习算法将1,463维的VAR模型缩减为32个显著关系。这些关系解释了因变量变动的很大一部分，如较高的 $R^{2}$ 值所示（表1）。以下一些关键发现将塑造系统对各种性质宏观金融冲击的响应：

**持续的滞后效应占主导地位。** 大多数变量都显著地受其自身近期滞后值的影响。

**私有房地产开发商对宏观和金融状况高度敏感。** 消费者情绪疲软会增加其违约风险，这可能是由于需求减弱进而导致盈利能力下降。金融部门稳健性恶化也会降低其信用度，这可能是由于信贷供给受限。显著影响不仅来自国有银行和股份制银行，也来自资产管理公司，后者将银行部门的信贷引导至风险更高的房地产部门（Allen等人，2023）。

- **私营开发商压力会溢出至国有开发商和金融机构。** 国有开发商最初可能因被认为（隐性）有国家支持而受益于有利的消费者情绪，但最终会面临类似的市场压力。一旦未来收入和盈利前景黯淡且消费者情绪恶化，它们的融资渠道可能中断（例如金融加速器效应），使业务运营难以为继。股份制银行似乎特别容易受到私营开发商压力的影响，这可能反映了它们通过贷款和资产管理产品对风险较高行业的敞口不成比例（IMF，2025）。

**房地产市场状况对宏观和金融结果至关重要。** 房地产价格上涨格兰杰导致股份制银行信贷质量改善，反映了它们对房地产开发行业的敞口不成比例。房地产价格上涨也预示着更好的市场和经济前景，通过财富效应提振房地产投资和消费者情绪（Fang等人，2015）。

**股份制银行疲软会溢出至城市商业银行。** 这种跨期联系可能反映了它们相似的商业模式、借贷关系、金融市场交易、对它们的同步情绪，以及对包括房地产开发商在内的风险行业的共同敞口。

**表1. 跨期关系：回归系数**


来源：新加坡国立大学信用研究倡议；国际清算银行房地产价格数据库；Haver Analytics。
注：AM=资产管理公司，JS=股份制银行，CC=城市商业银行，RC=农村商业银行，RE=房地产投资，PP=房地产价格。

除了回归系数所体现的跨期关系（表1）之外，扰动项的协方差矩阵（表2）显示了同期联系。这些同期相关性揭示了金融机构之间以及开发商与银行之间的强关联。它们可能反映了金融加速器效应、借贷关系、共同敞口、市场状况和情绪。

**表2. 同期关系：扰动项协方差**


来源：新加坡国立大学信用研究倡议；国际清算银行房地产价格数据库；Haver Analytics。
注：AM=资产管理公司，JS=股份制银行，CC=城市商业银行，RC=农村商业银行，RE=房地产投资，PP=房地产价格。

## 脉冲响应

我们模拟对各个变量的特定冲击，并追踪其随时间推移在系统中的放大效应。这些影响由同期相关性和跨期关系所隐含的内生响应驱动。在所有练习中，对基于PD的变量的冲击为1个基点，意味着信用质量恶化。对宏观金融变量的冲击为1个百分点，意味着房地产价格、消费者情绪或房地产投资的改善。或许并不令人意外，对PD的1个基点冲击在比例上小于对宏观变量的1个百分点冲击。因此，即使宏观金融联系很强，对金融和开发商部门的冲击对宏观表现的影响在几次练习中看起来很小。

## 对私营开发商的冲击

在第一个练习中，我们对私营开发商施加一次性冲击，以反映其销售和股市表现的突然下滑。资产负债表受损可能限制其融资渠道、约束业务运营并削弱未来现金流。这1个基点的冲击通过宏观金融联系传导，造成放大且持续的损害，其影响在一年内大约放大十倍（图1）。

6/8

国有开发商最初因民营竞争对手表现疲弱而受益。然而，随着市场情绪、销售和盈利能力下滑，它们的信用质量也随之恶化，尽管整体影响仍温和得多。

对金融体系的溢出效应相当显著。国有银行逐渐受到影响。由于其业务模式偏向国有借款人，它们往往只有在国有开发商在几个时期后开始违约时才会确认损失。相比之下，股份制银行则立即受到显著影响。这些银行风险偏好更高，对最终为房地产开发活动提供资金的房地产行业贷款和投资资产的敞口不成比例地大。

理论上，资产管理公司通过信托和投资产品将开发商信用风险完全转移给银行和其他最终投资者。然而，在实践中，它们历史上通过隐性担保吸收了部分损失，这种做法在2018年《资管新规》后受到限制（Allen et al., 2023）。其信用质量的恶化也可能反映了可行的房地产投资项目和创收机会的丧失。

图1. 脉冲响应：民营开发商PD 1个基点冲击（Y轴：PD以基点计，宏观变量以百分点计；X轴：月份）

[[KC_IMAGE_002]]

资料来源：新加坡国立大学信用研究倡议；国际清算银行房地产价格数据库；Haver Analytics。

## 对城市商业银行的冲击

城市商业银行PD恶化1个基点，模拟了暂时的流动性冲击或资本短缺。尽管其规模较小且具有区域性，但这些银行面临的压力可能引发系统性影响（图2）。

股份制银行和资产管理公司似乎受到特别影响，这可能是由于它们与城市商业银行的资产负债表关联以及共同的市场情绪动态。股份制银行和城市商业银行具有相似的业务模式：依赖批发融资、活跃于银行间交易、且对风险较高的借款人有敞口（IMF, 2025）。城市商业银行经历的暂时压力可能削弱市场情绪，并鼓励其他机构囤积流动性，从而扰乱其融资渠道。由此产生的流动性和信贷紧缩也可能传导至资产管理公司，后者将银行资源引导至风险行业。

相比之下，国有银行在初始冲击后几乎立即表现更好。对更安全业务模式的积极情绪可能将流动性从金融体系中风险较高的部分转移出去，暂时提升其表现，尽管可能出现一些过度反应并在之后逆转。

民营和国有开发商的信用质量均有所下降，但程度不同。民营开发商遭受长期且显著的压力，这可能是由于融资流中断——直接来自城市商业银行，间接来自更广泛的流动性收缩。国有开发商受影响较小，这很可能反映了其更多元化的融资来源。

图2. 脉冲响应：城市商业银行PD 1个基点冲击（Y轴：PD以基点计，宏观变量以百分点计；X轴：月份）

[[KC_IMAGE_003]]

资料来源：新加坡国立大学信用研究倡议；国际清算银行房地产价格数据库；Haver Analytics。

## 对房地产价格的冲击

房地产价格是中国宏观金融联系的核心（Ge et al., 2022）。价格上涨在后续时期直接改善民营开发商的信用质量（图3）。价格上涨支撑更强的销售和盈利能力，增强开发商的资产负债表。此外，它还增强消费者信心，鼓励购房和投资（图4，表1）。同时，它有助于形成更有利的金融条件，维持对开发商和购房者的资金流。

在宏观层面，有利的价格动态因回报前景改善而鼓励后续时期的房地产投资（Allen, 1993）。开发商和金融机构更健康的资产负债表进一步使这些实体能够在价格条件保持有利时扩大投资。

图3. 脉冲响应：房地产价格1个百分点冲击（Y轴：PD以基点计，宏观变量以百分点计；X轴：月份）

[[KC_IMAGE_004]]

资料来源：新加坡国立大学信用研究倡议；国际清算银行房地产价格数据库；Haver Analytics。

## 对消费者信心的冲击

消费者信心的积极提振改善了许多其他部门的表现（图4）。购房意愿的提高增加了销售并增强了民营开发商的财务状况，从而改善其信用质量。活跃的经济活动也巩固了几个金融部门的地位，反映了更强的信贷需求、改善的资产质量和更有利的经营环境。

图4. 脉冲响应：消费者信心指数1个百分点冲击（Y轴：PD以基点计，宏观变量以百分点计；X轴：月份）

[[KC_IMAGE_005]]

资料来源：新加坡国立大学信用研究倡议；国际清算银行房地产价格数据库；Haver Analytics。

## V. 结论

宏观金融稳定仍是政策制定者的核心目标。过去的危机凸显了理解宏观金融联系及其在放大冲击中的作用的重要性。作为回应，全球政策议程日益采纳宏观审慎方法。

在中国，一个复杂且相互关联的金融体系支撑着依赖房地产和基础设施投资的增长模式。宏观金融联系显著，持续的房地产市场调整引发了对更广泛宏观经济影响的重大担忧。

本文使用机器学习VAR模型，结合细粒度的高频时间序列，量化实体部门与金融部门之间的双向互动。通过纳入开发商和金融机构的PD指标，分析揭示了宏观金融冲击的异质性效应。一种新颖的、完全可解释的机器学习方法解决了高维问题，并捕捉了持续的时间动态，而无需依赖任何不透明的“黑箱”模型。

研究结果表明，即使是暂时性冲击也可能引发巨大且持续的宏观金融后果。来自民营开发商和区域性银行的压力可能通过贷款关系、共同敞口、共享市场和情绪溢出到其他部门。房地产价格是这些联系的核心。急剧的修正可能削弱房地产投资，侵蚀消费者信心，并削弱房地产和金融部门——通过需求和供给渠道扰乱金融中介，并抑制更广泛的经济前景。

实证分析表明，资本充足且资金来源稳定的金融机构，更具备持续提供信贷和流动性的能力。稳定房地产价格若能与恢复持久商业和消费者信心的更广泛努力相结合，往往能取得更佳效果。研究结果指出了影响房地产开发商的措施与更广泛的金融部门韧性考量之间可能存在的权衡取舍。房地产市场的可持续复苏，其典型特征是在关键市场参与者财务健康状况支撑下的有机交易增长。考虑复杂的反馈效应有助于刻画经济周期中的宏观金融动态。

建立一套全面的工具包来监测宏观金融联系并定期评估冲击引发的结果，可以加强风险管理。现代传染动态日益受到商业模式相似性、共同风险敞口和市场情绪的影响，其范围已超越双边风险敞口。借助现代技术，高频、公开可用的市场指标能够提供及时、前瞻性的洞察。改进跨部门风险敞口的数据收集，可以加深对中国宏观金融复杂性的理解。

## 参考文献

Adrian, T. (2017b), “Macroprudential Policy and Financial Vulnerabilities,” Speech at the European Systemic Risk Board Annual Conference, September 22, Frankfurt am Main.

Adrian, T., and H. S. Shin (2008), “Liquidity, Monetary Policy, and Financial Cycles”, Current Issues in Economics and Finance, Vol. 14, No. 1, Federal Reserve Bank of New York, New York.

Adrian, T., and H. S. Shin (2010a), “Liquidity and Leverage”, Journal of Financial Intermediation, Vol. 19, No. 3, pp. 418–37.

Allen, F. (1993), “Stock Markets and Resource Allocation,” in Capital Markets and Financial Intermediation, C. Mayer and X. Vives (eds), pp. 81–108, New York: Cambridge University Press.

Allen, F., X. Gu, C.W. Li, J. Qian, and Y. Qian (2023), “Implicit Guarantees and the Rise of Shadow Banking: The Case of Trust Products”, Journal of Financial Economics, 149(2), 115-141.

Antony, J., and P. Broer (2010), “Linkages between the Financial and the Real Sector of the Economy: A Literature Survey”, CPB Document, 216, CPB Netherlands Bureau for Economic Policy Analysis, Hague.

Basel Committee on Banking Supervision (BCBS, 2011), “The Transmission Channels between the Financial and Real Sectors: A Critical Survey of the Literature”, BCBS Working Paper 18, Bank for International Settlements, Basel.

Bernanke, B. S., and A. Blinder (1988), “Credit, Money, and Aggregate Demand”, American Economic Review, Vol. 78, No. 2, pp. 435–9.

Bernanke, B. S., and C. S. Lown (1991), “The Credit Crunch”, Brookings Papers on Economic Activity, Vol. 1991, No. 2, pp. 205–39.

Blanchard, O. (2017a), “Distortions in Macroeconomics”, Paper submitted to NBER Macroeconomics Annual, June 18, Peterson Institute for International Economics, Washington, DC.

Borio, C., I. Shim, and H.S. Shin (2022), “Macro-financial Stability Frameworks: Experience and Challenges”, BIS Working Papers No 1057.

Bruche, M., and J. Suarez (2010), “Deposit Insurance and Money Market Freezes”, Journal of Monetary Economics, Vol. 57, No. 1, pp. 45–61.

Brunnermeier, M., and A. Krishnamurthy (eds) (2014), “Risk Topography: Systemic Risk and Macro Modeling”, Chicago: University of Chicago Press.

Carroll, C. D., M. Otsuka, and J. Slacalek (2011), “How Large Are Housing and Financial Wealth Effects? A New Approach”, Journal of Money, Credit and Banking, Vol. 43, No. 1, pp. 55–79.

Case, K. E., J. M. Quigley, and R. J. Shiller (2005), “Comparing Wealth Effects: The Stock Market versus the Housing Market”, Advances on Macroeconomics, Vol. 5, No. 1, Article 1.

Case, K. E., J. M. Quigley, and R. J. Shiller (2013), “Wealth Effects Revisited 1975–2012”, Critical Finance Review, Vol. 2, No. 1, pp. 101–28.

Chen, K. and Y. Wen (2017), "The Great Housing Boom of China", American Economic Journal: Macroeconomics, 9(2), 73-114.

Chen, Z., Z. He, and C. Liu (2020), “The Financing of Local Government in China: Stimulus Loan Wanes and Shadow Banking Waxes”, Journal of Financial Economics, 137(1), 42-71.

Claessens, S. (2015), “An Overview of Macroprudential Policy Tools”, Annual Review of Financial Economics, Vol. 7, pp. 397–422.

Claessens, S. and M.A., Kose (2018), “Frontiers of Macrofinancial Linkages”, BIS Papers, No. 95.

Claessens, S., M. A. Kose, and M. E. Terrones (2012a), “How do Business and Financial Cycles Interact?” Journal of International Economics, Vol. 87, No. 1, pp. 178–90.

Coric, B. (2011), “The Financial Accelerator Effect: Concept and Challenges”, Financial Theory and Practice, Vol. 35, No. 2, pp. 171–96.

Craig, B., M. Karamysheva, and D. Salakhova (2024), "Do Market-based Networks Reflect True Exposures Between Banks?" ECB Working Paper Series, No 2867.

Credit Research Initiative, National University of Singapore (NUS-CRI, 2023), “NUS Credit Research Initiative Technical Report, 2023 Update 1”.

Deaton, A. (1992), “Understanding Consumption”, Oxford: Clarendon Press.

Diebold, F. and K. Yilmaz (2012), “Better to Give Than to Receive: Predictive Directional Measurement of Volatility Spillover”, International Journal of Forecasting 28, 57-66.

Drehmann, M., C. Borio, and K. Tsatsaronis (2012), “Characterising the Financial Cycle: Don’t Lose Sight of the Medium Term!”, BIS Working Paper 380, Bank for International Settlements, Basel.

Duan, J-C. (2024), “Stable Combinatorially-Optimized Features Selection via Sequential Monte Carlo Optimization”, Working Paper. https://adbiza.com/static/docs/PublishFiles/VariableSelection-SMC\_October-25-2024.pdf

Duan, J-C. (2025), “Interpretable vs Black-box AI in Action”, ADBIZA Whitepaper.
https://adbiza.com/static/docs/PublishFiles/Interpretable%20vs%20Black-box%20AI%20in%20Action.pdf

Duan, J.-C., S. Li, and Y. Xu, 2022, Sequential Monte Carlo Optimization and Statistical Inference, Wiley Integrative Reviews: Computational Statistics, e1598. https://doi.org/10.1002/wics.1598

Duan, J.C., J. Sun and T. Wang, 2012, Multiperiod Corporate Default Prediction – A Forward Intensity Approach, Journal of Econometrics 170, 191-209.

Fan, J. (1997), “Comments on “Wavelets in Statistics: a Review” by A. Antoniadis”, Journal of the Italian Statistical Society, 6(20), 131-138.

Fang, H., Q. Gu, W. Xiong, and L. Zhou (2015), “Demystifying the Chinese Housing Boom”, NBER Macroeconomics Annual, Vol 30.

Freixas, X., and J. Jorge (2008), “The Role of Interbank Markets in Monetary Policy: A Model with Rationing”, Journal of Money, Credit and Banking, Vol. 40, No. 6, pp. 1151–76.

Gan, J. (2010), “Housing Wealth and Consumption Growth: Evidence from a Large Panel of Households”, Review of Financial Studies, Vol. 23, No. 6, pp. 2229–67.

Ge, X., X. Li, Y. Li, and Y. Liu (2022), “The Driving Forces of China’s Business Cycles: Evidence from an Estimated DSGE Model with Housing and Banking”, China Economic Review.

Geanakoplos, J. (2008), “Arrow Debreu Model of General Equilibrium,” in The New Palgrave Dictionary of Economics, 2nd edition, S. N. Durlauf and L. E. Blume (eds), Palgrave Macmillan.

Geanakoplos, J. (2010), “The Leverage Cycle” in NBER Macroeconomic Annual 2009, Vol. 24, D. Acemoglu, K. Rogoff, and M. Woodford (eds), pp. 1–65, Chicago: University of Chicago Press.

Guiso, L., and P. Sodini (2013), “Household Finance: An Emerging Field,” in Handbook of the Economics of Finance, Vol. 2, G. M. Constantinides, M. Harris, and R. M. Stulz (eds), pp. 1397–532, Amsterdam: North-Holland.

Holmström, B., and J. Tirole (1997), “Financial Intermediation, Loanable Funds, and the Real Sector”, Quarterly Journal of Economics, Vol. 112, No. 3, pp. 663–91.

IMF (2025), “Financial System Stability Assessment”, People’s Republic of China.

IMF-FSB-BIS (2016), “Elements of Effective Macroprudential Policies: Lessons from International Experience”, Report to the G-20, August 31.

Kim, K. H. (2004), “Housing and the Korean Economy”, Journal of Housing Economics, Vol. 13, pp. 321–41.

Muir, T. (2017), “Financial Crises and Risk Premia”, Quarterly Journal of Economics, Vol. 132, No. 2, pp. 765–809.

Natarajan, B.K. (1995), “Sparse Approximate Solutions to Linear Systems”, SIAM Journal on Computing, 24(2), 227-234.

Quadrini, V. (2011), “Financial Frictions in Macroeconomic Fluctuations”, Economic Quarterly, Vol. 97, No. 3, pp. 209–54, Federal Reserve Bank of Richmond, Richmond.

Repullo, R., and J. Suarez (2000), “Entrepreneurial Moral Hazard and Bank Monitoring: A Model of the Credit Channel”, European Economic Review, Vol. 44, No. 10, pp. 1931–50.

Stein, J. C. (1998), “An Adverse-Selection Model of Bank Asset and Liability Management with Implications for the Transmission of Monetary Policy”, RAND Journal of Economics, Vol. 29, No. 3, pp. 466–86.

Tibshirani, R. (1996), “Regression Shrinkage and Selection via the Lasso”, Journal of the Royal Statistical Society, Ser. B, 58(1), 267-288.

Van den Heuvel, S. J. (2006), “The Bank Capital Channel of Monetary Policy”, Society for Economic Dynamics, Meeting Paper 512.

Van den Heuvel, S. J. (2008), “The Welfare Cost of Bank Capital Requirements”, Journal of Monetary Economics, Vol. 55, No. 2, pp. 298–320.

[[KC_IMAGE_006]]
