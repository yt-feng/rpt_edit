# 最优货币篮子估计

IMF工作论文报告了作者正在进行的研究，并发布以征求意见和鼓励讨论。IMF工作论文中表达的观点仅代表作者本人，不一定代表IMF、其执行董事会或IMF管理层的观点。

2026年
4月

[[KC_IMAGE_001]]

# IMF工作论文 货币与资本市场

2026年4月

IMF工作论文报告了作者正在进行的研究，并发布以征求意见和鼓励讨论。IMF工作论文中表达的观点仅代表作者本人，不一定代表IMF、其执行董事会或IMF管理层的观点。

摘要：小型开放经济体通常将其汇率锚定于一篮子外币，权重通常根据贸易份额或金融敞口设定。此类方案忽略了汇率传导在不同货币间的异质性以及双边汇率的协方差结构，因此无法最小化进口通胀的波动性——而这正是央行的政策目标。本文提出了一个最小方差框架——在形式上类似于汇率传导空间中的Markowitz投资组合问题——在该框架中，篮子权重在保持篮子累积传导率的约束下，最小化汇率驱动的进口通胀方差。以斐济（一个进口密集型岛国，采用五货币篮子）为例，优化使进口通胀方差降低了近20%，且结果在不同模型设定下均保持稳健。

推荐引用：E. Vaccaro-Grange, "Optimal Currency Basket Estimation", IMF Working Paper No. 26/131, International Monetary Fund, Washington DC.

# 最优货币篮子估计

## 目录

缩略语....3
引言....4
模型....5
小型开放经济体的应用....10
结论....16
附录一. 推导....17
参考文献....19

## 图表

2. 通胀....11
3. 通胀传导率....12
4. 货币收益率相关性....13

表格
1. 货币篮子权重（百分比）....14
2. 稳健性——模型设定....14
3. 货币篮子权重（百分比）....15

## 缩略语

CPI 消费者价格指数

## 引言

货币篮子盯住是一种汇率制度，本币锚定于多种外币的加权平均值，而非单一锚定货币。通过将汇率风险分散到多个贸易伙伴，篮子盯住在硬盯住和有管理的浮动之间提供了中间灵活性，并在一定程度上隔离了单一交叉汇率的波动性（Williamson, 1998）。这种安排通常被小型开放经济体采用，因为自由浮动制度对这些经济体而言不切实际——通常是由于外汇市场薄弱、金融体系欠发达，或希望从更稳定的货币管辖区引入可信度（Imam, 2010; Yoshino, Helble, and Prasetyo, 2017）。斐济、萨摩亚、汤加和所罗门群岛等太平洋岛国经济体，以及包括科威特和摩洛哥在内的其他小型开放经济体，目前均实行此类篮子制度。

任何篮子盯住的核心设计问题是如何确定其组成货币的权重。最广泛使用的方法依赖于贸易份额，权重反映出口和进口的地理分布，有时还辅以服务流、汇款或外债偿还（Edison and Vårdal, 1990; Yoshino, Helble, and Prasetyo, 2017）。虽然透明且直观，但基于贸易的权重仅描述了外部交易的结构，通常与最能支持央行价格稳定目标的权重不一致。特别是，它们既未利用汇率传导在不同货币间的异质性，也未利用双边汇率变动的协方差结构——这两个特征对进口通胀行为至关重要。

大量文献试图在明确的宏观经济目标下推导最优篮子权重。Flanders and Helpman (1979) 提供了一个将篮子权重与国际收支和实际收入稳定性联系起来的早期框架，后由 Branson and Katseli (1981)、Turnovsky (1982) 和 Bhandari (1985) 扩展。Edison and Vårdal (1990) 推导了最小化可贸易品生产方差的最优权重，并将其应用于北欧国家。Yoshino, Kaji, and Suzuki (2004) 开发了一个三国篮子模型，后由 Yoshino, Helble, and Prasetyo (2017) 扩展到包含旅游流的四国设定，以最小化汇率和产出的波动性。他们将该模型应用于太平洋岛国经济体。Ma and Cheng (2014) 提出了一个两阶段模型，其中篮子选择旨在最小化产出和通胀波动性的加权平均值，同时考虑事后财政调整，并将其应用于香港特别行政区。

Slavov (2005)、Teo (2009)、Shioji (2006)、Xu (2011) 以及 Zhang, Shi, and Zhang (2011) 的平行研究工作将篮子选择嵌入一般均衡设定中，纳入了贸易计价、国际投资净头寸和外币债务。另一个独立但密切相关的文献记录了汇率对进口价格的传导是不完全的，在不同货币和行业间具有异质性，并受到定价到市场、名义刚性和战略互补性的影响（Krugman, 1987; Knetter, 1989; Betts and Devereux, 2000; Campa and Goldberg, 2005; Gopinath and Itskhoki, 2010; Gopinath, Itskhoki, and Rigobon, 2010）。

本文通过将这两条研究线索结合起来，为文献做出了贡献。我们提出了一个篮子权重优化框架，其目标是最小化进口通胀中汇率驱动成分的方差——即篮子的通胀传导率——而非国际收支或总产出波动性。与贸易加权方案相比，该程序利用了从标准进口价格方程中估计出的特定货币传导系数以及双边汇率收益率的协方差结构。由此产生的问题在形式上类似于Markowitz最小方差投资组合，其中货币为"资产"，经传导率调整的汇率变动为"收益率"，篮子权重为投资组合份额。一个结构性约束保持了当前篮子所隐含的累积传导率，因此优化后的权重在降低进口通胀波动性的同时，不会改变国内价格对篮子变动的平均敏感度。据我们所知，这是第一篇明确将最优篮子设计构建为在不变结构性传导率约束下的最小方差传导率问题的论文。

我们用一个自1980年代以来实行五货币篮子的小型进口密集型岛国经济体——斐济——来说明该框架。我们表明，新优化的权重相对于当前权重可将通胀方差降低约20%，同时保持篮子的结构性传导。一系列稳健性检验证实了主要结果在传导方程不同设定下的稳定性。

最优篮子设计的另外两个决定因素值得一提，但不在本文讨论范围内。第一，本国经济与各货币区域之间的商业周期同步程度为锚定提供了补充论据：更高的协同程度加强了赋予相应货币更大权重的理由。第二，金融美元化——通过外币计价存款或外部债务——引入了资产负债表稳定性约束，这是基于贸易或价格的方案都无法捕捉的。我们忽略这两个维度，严格聚焦于最小化汇率驱动的进口通胀方差，这与央行的价格稳定使命一致。将周期同步和资产负债表考量纳入优化问题留待未来研究。

本文其余部分结构如下：第1节介绍模型，第2节将其应用于一个小型开放经济体，第3节总结。

## 模型

根据一价定律，进口商品的本币价格为：

$$
P _ {t} ^ {m} = E _ {t} P _ {t} ^ {x}\tag{1}
$$

其中 $E_{t}$ 是名义汇率（每单位外币的本币单位数；上升表示贬值），$P_{t}^{m}$ 是以本币计价的进口价格，$P_{t}^{x}$ 是以外币计价的出口价格。取对数差分，我们得到：$^{2}$

$$
\Delta p _ {t} ^ {m} = \Delta e _ {t} + \Delta p _ {t} ^ {\mathrm{x}}
$$

(2)

或者用常用符号 $\pi_t^m = \Delta p_t^m$ ，$\pi_t^x = \Delta p_t^x$ ：

$$
\pi_ {t} ^ {m} = \Delta e _ {t} + \pi_ {t} ^ {\mathrm{x}}\tag{3}
$$

该等式对单一贸易伙伴 j 成立：

$$
\pi_ {j, t} ^ {m} = \Delta e _ {j, t} + \pi_ {j, t} ^ {\mathrm{x}}\tag{4}
$$

总进口通胀是所有 n 个伙伴的贸易加权总和：

$$
\pi_ {t} ^ {m} = \sum_ {j = 1} ^ {n} w _ {j} \pi_ {j, t} ^ {m}\tag{5}
$$

$$
\pi_ {t} ^ {m} = \sum_ {j = 1} ^ {n} w _ {j} \Delta e _ {j, t} + \sum_ {j = 1} ^ {n} w _ {j} \pi_ {j, t} ^ {\mathrm{x}}\tag{6}
$$

其中 $w_{j}$ 是伙伴 j 的进口份额，且 $\sum_{j=1}^{n} w_{j}=1$ 。

理论上，一价定律意味着汇率变动会完全且即时地反映在本币计价的进口价格中。然而在实践中，一系列有据可查的微观经济摩擦削弱了这种传导。我们称传导是不完全的。

在本地货币定价下（Betts and Devereux, 2000），出口商以目的地货币设定价格，使得进口价格在重新定价期间对汇率波动机械地不敏感。即使在重新定价时，在不完全竞争市场中运营的企业也可能最优地将部分汇率变动吸收到其加价中，而不是将其传导至最终价格，这种行为在定价到市场文献中已被形式化（Krugman, 1987; Knetter, 1989）。这种加价调整因定价中的策略互补性而得到加强：当进口商的需求取决于其相对于国内竞争对手的价格时，最优定价倾向于国内价格水平，从而抑制了对汇率冲击的反应（Gopinath and Itskhoki, 2010）。菜单成本或Calvo（1983）式交错价格调整形式的名义刚性在传导过程中引入了额外的延迟。总体而言，这些摩擦意味着任何给定的汇率变动最终只有一部分被传导至进口价格，这一结果得到了实证证据的一致支持（Campa and Goldberg, 2005; Gopinath, Itskhoki, and Rigobon, 2010）。这促使我们采用一种实证设定，其中不完全传导是自由估计的，而不是强制设定为1。

在该框架下，方程（6）变为：

$$
\pi_ {t} ^ {m} = \sum_ {j = 1} ^ {n} \beta_ {j} \Delta e _ {j, t} + \sum_ {j = 1} ^ {n} \delta_ {j} \pi_ {j, t} ^ {\mathrm{x}} + \varepsilon_ {t}\tag{7}
$$

其中 $\beta_{j}$ 不再受限于等于 $w_{j}$ ——它们捕捉了每个双边汇率对总进口价格的有效传导，反映了贸易份额和每个伙伴特有的传导程度。类似地，$\delta_{j}$ 可能不同于 $w_{j}$ ，因为同样的定价摩擦——加价吸收、名义刚性和策略互补性——也适用于外国成本变化的传导（尽管程度较轻，因为企业有更强的动机传导自身生产成本的增长）。两个系数预计都低于贸易权重 $w_{j}$ ，因此 $\sum_{j=1}^{n}\beta_{j}<1$ 且 $\sum_{j=1}^{n}\delta_{j}<1$ 。

实证设定包含若干由理论驱动的标准特征。双边汇率收益率和出口价格通胀的滞后项捕捉了名义刚性下进口价格的渐进调整。实际上，由于企业在离散的时间间隔重新定价，汇率冲击的完全传导需要多个时期而非即时实现，因此当期和滞后系数的总和衡量了累积的长期传导，而单个系数则描绘了动态调整路径（Campa and Goldberg, 2005）。进口通胀的滞后项也出于同样的原因被纳入——在Calvo（1983）式交错定价下，每个时期只有一部分进口商重新定价，产生了自回归项所捕捉的总进口价格水平的内在持续性。常数项吸收了与汇率变动无关的进口通胀的任何长期趋势，例如国内与国外趋势通胀之间的持续差异或进口商加价随时间的系统性演变。

方程（7）变为：

$$
\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k} \pi_ {j, t - k} ^ {\mathrm{x}} + \varepsilon_ {t}\tag{8}
$$

其中 $\mu$ 是常数，$\rho_{k}$ 捕捉了由交错定价引起的进口通胀持续性，$\beta_{j,k}$ 是货币 j 在滞后 k 期的传导，$\delta_{j,k}$ 捕捉了伙伴 j 出口价格通胀的滞后传导。此外，为模型的可处理性，我们假设外国出口通胀近似等于外国通胀：$\pi_{j,t}^{x} \approx \pi_{j,t}^{*}$ 。³

在相对购买力平价条件下，方程(8)可进一步简化，因为：$\Delta e_{j,t} = \pi_{t} - \pi_{j,t}^{*} \approx \pi_{t}^{m} - \pi_{j,t}^{x}$。即，国内通胀与国外通胀之差大致等于进口通胀与国外出口通胀之差。

因此，

$$
\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k} (\pi_ {t - k} ^ {m} - \Delta e _ {j, t - k}) + \varepsilon_ {t}\tag{9}
$$

$$
\pi_ {t} ^ {m} = \mu + \left(\sum_ {k = 1} ^ {p} \rho_ {k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k}\right) \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} - \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k} \Delta e _ {j, t - k} + \varepsilon_ {t}
$$

(10)

$$
\pi_ {t} ^ {m} = \mu + \left(\sum_ {k = 1} ^ {p} \rho_ {k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k}\right) \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \left(\sum_ {k = 1} ^ {q} \beta_ {j, k} - \sum_ {k = 1} ^ {l} \delta_ {j, k}\right) \Delta e _ {j, t - k} + \varepsilon_ {t}\tag{11}
$$

$$
\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {\tilde {p}} \tilde {\rho} _ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {\tilde {q}} \tilde {\beta} _ {j, k} \Delta e _ {j, t - k} + \varepsilon_ {t}\tag{12}
$$

其中 $\sum_{k=1}^{\tilde{p}}\tilde{\rho}_k = \sum_{k=1}^p\rho_k + \sum_{j=1}^n\sum_{k=1}^l\delta_{j,k}$ 且 $\sum_{k=1}^{\tilde{q}}\tilde{\beta}_{j,k} = \sum_{k=1}^q\beta_{j,k} - \sum_{k=1}^l\delta_{j,k}$。为简便起见，我们将去掉 $\sim$ 并保留以下传递方程：

$$
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} + \varepsilon_ {t}}\tag{13}
$$

另一种不那么严格的设定是假设国外出口通胀大致等于国外通胀：$\pi_{j,t}^{\mathrm{x}}\approx \pi_{j,t}^{*}$。则方程(7)变为：

$$
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k}   \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k}   \Delta e _ {j, t - k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k}   \pi_ {j, t - k} ^ {*} + \varepsilon_ {t}}\tag{14}
$$

另一种建模方法是定义由 $\bar{\beta}_{j} = \sum_{k=0}^{q} \beta_{j,k}$ 给出的累积传递效应。

假设对于国家 j，$\beta_{j,k}$ 随时间恒定，即 $\beta_{j,1} = \beta_{j,2} = \ldots = \beta_{j,q}$，则我们可以将方程(13)重写为：

$$
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \bar {\beta} _ {j} \sum_ {k = 1} ^ {q} \Delta e _ {j, t - k} + \varepsilon_ {t}}\tag{15}
$$

方程(13)、(14)和(15)是传递回归方程的三种不同形式。现在，我们定义 $z_{j,t}$ 为货币 j 的总传递贡献：

$$
z _ {j, t} = \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k}\tag{16}
$$

进一步，我们将篮子汇率定义为 n 种货币的加权几何平均值：

$$
e _ {t} ^ {B} = \prod_ {j = 1} ^ {n} e _ {j, t} ^ {\theta_ {j}}\tag{17}
$$

其中 $e_{t}^{B}$ 是每单位本币的篮子汇率，$e_{j,t}$ 是每单位本币的外币 j 汇率，$\theta_{j}$ 是其在该篮子中的权重。此外，我们有：$\theta_{j} \in [0, 1]$ 且 $\sum_{j=1}^{n} \theta_{j} = 1$。

在该框架下，来自货币篮子的总通胀传递 $z_{t}^{B}$ 是所有货币总传递贡献的加权平均值：

$$
z _ {t} ^ {B} = \sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\tag{18}
$$

注意，如果篮子汇率使用加权算术平均值计算：

$$
e _ {t} ^ {B} = \sum_ {j = 1} ^ {n} \theta_ {j} e _ {j, t}\tag{19}
$$

那么，

$$
z _ {t} ^ {B} \approx \sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\tag{20}
$$

方程(20)只是一个近似，因为根据詹森不等式：

$$
\Delta e _ {t} ^ {B} = e _ {t} ^ {B} - e _ {t - 1} ^ {B} = \log \left(\sum_ {j = 1} ^ {n} \theta_ {j} e _ {j, t}\right) - \log \left(\sum_ {j = 1} ^ {n} \theta_ {j} e _ {j, t - 1}\right) \neq \log \left(\sum_ {j = 1} ^ {n} \theta_ {j} e _ {j, t} - \sum_ {j = 1} ^ {n} \theta_ {j} e _ {j, t - 1}\right)\tag{21}
$$

现在，我们寻找使通胀传递 $z_{t}^{B}$ 方差最小化的权重 $\theta_{j}$。即（证明见附录1）：

$$
a r g m i n _ {\theta} \left[ V a r (z _ {t} ^ {B}) \right] = a r g m i n _ {\theta} \left[ V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) \right]\tag{22}
$$

它可以表示为矩阵形式：

$$
a r g m i n _ {\theta} [ V a r (z _ {t} ^ {B}) ] = a r g m i n _ {\theta} [ \theta^ {\prime} B V a r (\Delta E _ {t}) B \theta ]\tag{23}
$$

其中 $\Delta E_{t}=\left\{\Delta e_{j,t}\right\}$ 对于 $j\in[1,n]$ 是对数货币收益的向量，B 是累积特定货币传递 $\bar{\beta}_{j}=\sum_{k=0}^{q}\beta_{j,k}$ 的对角矩阵（每种货币一行），$\theta=\left\{\theta_{j}\right\}$ 对于 $j\in[1,n]$ 是篮子权重的向量。

注意，如果所有货币具有相同的传递效应，即 $B = c * I_{n}$，那么：

$$
a r g m i n _ {\theta} [ \theta^ {\prime} B V a r (\Delta E _ {t}) B \theta ] = a r g m i n _ {\theta} [ \theta^ {\prime} V a r (\Delta E _ {t}) \theta ]\tag{24}
$$

也就是说，最小化传递加权对数汇率变化的方差等价于简单地最小化对数汇率变化的方差。然而，每个 $e_{j,t}$ 都是以本币单位表示的货币 j 的价格。因此，所有序列都以本币作为共同计价单位。这会产生一个虚假的协方差问题。实际上，本币的任何变动都会同时以相同的幅度和方向改变所有双边汇率。这种机械性的共同变动使得汇率之间的成对协方差无法提供关于篮子货币之间真实交叉汇率关系的信息。因此，需要将所有货币对重新以篮子中不存在的基准货币计价。

这一调整引入了修正项。可以证明（见附录I）：

$$
a r g m i n _ {\theta} \left[ V a r (z _ {t} ^ {B}) \right] = a r g m i n _ {\theta} [ \theta^ {\prime} \Sigma_ {\overline {{Z}}} \theta ]\tag{25}
$$

其中 $\Sigma_{\overline{Z}}$ 是 $z_{t}^{B}$ 的修正协方差矩阵。

此外，由于经济体的总篮子传递可被视为一个结构性参数（即短期内恒定），我们寻找能够保持传递效应的最优权重 $\theta^{opt}$。即，我们有以下约束条件：

$$
\theta^ {o p t} \bar {\beta} = \theta^ {c u r r} \bar {\beta}\tag{26}
$$

其中 $\theta^{opt}=\left\{\theta_{j}^{opt}\right\}$ 是新优化的一篮子货币权重向量，$\theta^{curr}=\left\{\theta_{j}^{curr}\right\}$ 是当前一篮子货币权重向量，$^{4}$ 而 $\bar{\beta}=\left\{\beta_{j}^{cum}\right\}$ 是所有货币 j 的累积传导系数向量：$\bar{\beta}_{j}=\sum_{k=1}^{p}\beta_{j,k}$，其中 $j\in[1,n]$。

因此，优化问题为：

$$
\mathop{\arg\min}\limits_{\theta} [\theta' \Sigma_{\overline{Z}} \theta] \quad \text{约束条件} \quad \left\{ \begin{array}{c} \theta_{j}^{opt} \in [0, 1] \text{ 且 } \sum_{j=1}^{n} \theta_{j}^{opt} = 1 \\ \theta^{opt} \bar{\beta} = \theta^{curr} \bar{\beta} \end{array} \right.\tag{27}
$$

该框架在形式上类似于马科维茨投资组合问题：货币是"资产"，经传导调整后的汇率变动是"回报" $\theta^{curr}\bar{\beta}$，央行的目标不是最大化预期回报，而是选择最小化方差 $\theta'\Sigma_{\overline{Z}}\theta$ 的权重。从这个意义上说，以价格稳定为导向的一篮子货币对应于传导空间中的最小方差组合。

## 应用于小型开放经济体

我们将该模型应用于一个进口密集型的小型岛屿开放经济体。该经济体的货币与五种货币挂钩：美元、新西兰元、澳元、欧元和日元（图1）。该国自80年代以来一直实行一篮子货币挂钩制度。这一篮子货币很好地服务于国家发展，有助于对冲该国外币敞口面临的汇率波动风险，并提升了外部竞争力稳定性。然而，这并不总能转化为价格稳定。同比整体通胀波动较大，且在新冠疫情后大幅震荡，从2024年4月的6.9%降至2025年9月的-3.8%。同样，整体通胀和进口通胀的环比数据也表现出高波动性，在过去几年中在正负两个百分点之间摆动（图2）。

图1. 历史汇率（1999年1月归一化=100）
斐济元/FC（左轴）vs 斐济元/一篮子货币（右轴）

[[KC_IMAGE_002]]

来源：当局数据及国际货币基金组织工作人员计算。

图2. 通胀

[[KC_IMAGE_003]]

来源：当局数据。

该国央行根据经济体的整体货币收支状况来确定其货币篮子权重。当局每年根据商品贸易、旅游业、汇款相关流量和偿债情况更新一次货币权重。

根据贸易份额或金融敞口来调整货币篮子权重是一种传统且直观的方法，因为它反映了经济体对外交易的结构。然而，这种方法并不能完全满足央行维护价格稳定的职责。贸易或金融敞口权重并不等同于能够最小化汇率传导至国内价格方差的权重。由于进口通胀不仅取决于敞口，还取决于特定货币传导系数的大小和协方差结构，因此仅根据贸易份额构建的货币篮子可能会在进口通胀中产生可避免的波动。要实现价格稳定，需要选择能够最小化经传导调整后的汇率变动方差（即进口通胀方差）的权重，而这在传统的基于敞口的加权方案下是无法保证的。

通过汇率传导来最小化进口通胀方差具有若干好处。首先，稳定进口通胀有助于实现整体价格稳定的目标，即低通胀方差。其次，降低进口通胀的不可预测性有助于锚定国内通胀预期，尤其是在像小岛屿这样大多数消费品依赖进口的小型开放经济体中。这有助于改善货币政策的传导。第三，最小化汇率驱动的进口通胀方差与降低篮子汇率方差是相辅相成的。

我们将该模型应用于这个小型开放经济体。我们使用十二个月的累计货币回报率来运行方程（14），以捕捉在进口占比较高的CPI篮子且价格刚性较强的经济体中，汇率对进口价格的渐进影响。此外，回归中包含了进口通胀（环比）的一期滞后项和国外整体通胀的一期滞后项，回归区间为2013年7月至2025年12月。$^{5}$ 传导系数估计值见图3。

图3. 通胀传导系数

[[KC_IMAGE_004]]

[[KC_IMAGE_005]]

所有货币的传导系数符号均符合预期。也就是说，斐济元兑美元每贬值1%，12个月后进口通胀将上升0.13个百分点。其他两个主要贸易伙伴货币的传导系数估计值（绝对值）也合理：新西兰元为0.10，澳元为0.08。欧元和日元的传导系数估计值最低，分别为0.02和0.01。

该经济体的总篮子传导系数可视为一个结构性参数（即在短期内保持不变）。使用当前权重，估计值为0.10。也就是说，斐济元兑一篮子货币每贬值1%，12个月后进口通胀将上升0.10个百分点。我们现在运行针对这一结构性传导水平的目标优化算法。

新优化的权重与当前权重基本一致，但建议将部分美元权重重新分配给澳元，同时将欧元从篮子中剔除（表1）。权重优化得出最优篮子的配置如下：美元36.77%（当前为42.41%），欧元0%（当前为3.56%），澳元37.82%（当前为30.75%），新西兰元22.83%（当前为19.72%），日元2.58%（当前为3.05%）。这些新权重保留了当前篮子估计为-0.10的结构性传导水平，同时最小化了通胀传导的方差。欧元权重为零，反映了该货币对国内通胀的重要性较低，这从其正的估计传导系数以及其在贸易、旅游和金融敞口中作用较小可以看出。此外，优化后的权重也与其历史均值大致相符。

权重优化可将通胀传导的方差降低44.7%。$^{6}$ 在结构性篮子传导率不变的前提下，以指数形式归一化的传导方差从央行现行篮子权重下的100降至新优化权重下的55.3。作为对比，若仅优化篮子汇率本身的方差（即假设所有货币具有相同的单位累积传导率，$\bar{\beta} = -1$），则总传导方差（以及篮子汇率方差）仅能降低28%。此外，仅以美元、澳元和新元作为篮子货币进行优化，可将方差降低40.4%。因此，在篮子中纳入欧元和日元的收益甚微，这一收益还需与名义锚的额外复杂性和透明度进行权衡。

我们现在进行稳健性分析以验证结果的稳定性（表2）。除前述优化（称为模型1）外，我们还采用非累积传导率并包含12期汇率回报滞后项来估计模型（模型2）。第三种方案是在方程右侧不纳入外国通胀滞后项（模型3）。第四种方案是在方程右侧不纳入国内通胀滞后项（模型4）。第五种方案同时剔除国内和外国通胀滞后项。最后，第六种方案采用非累积传导率且不含国内和外国通胀滞后项进行估计。优化结果见表3。

在所有六种方案中，相对于现行篮子及其历史均值，呈现出三个稳健模式。第一，美元在当前配置中持续超配：每个模型给出的美元权重介于36.66%至40.77%之间，系统性地低于当前的42.91%，且与2010-2025年历史均值37.37%高度吻合，表明现行篮子已偏离通胀方差最小化的合理水平而向美元倾斜。第二，新元持续低配：所有方案赋予新元的份额均高于22%，远高于当前的19.72%以及1999-2025年历史均值20.00%和2010-2025年历史均值20.97%，这表明无论传导率如何设定，新元的稳定作用都被低估。第三，澳元配置均超过当前的30.75%，但幅度对方案设定敏感：累积传导率方案将澳元集中在35%至38%之间，而非累积传导率方案将澳元回调至约28-32%，这一区间更符合历史贸易权重。欧元-日元配置呈现出显著的替代模式：欧元在模型1和模型4中被排除，在其余四个方案中配置在4.73%至5.03%之间；而日元则呈现镜像特征，仅在模型1和模型4中出现（2.51-2.58%），在其他方案中被剔除。值得注意的是，在保留欧元的四个方案中，欧元权重徘徊在2010-2025年历史均值5.36%附近，表明基于贸易的欧元历史处理方式大体上与通胀稳定一致，而欧元在两个方案中归零则反映了模型将其角色重新分配给日元，而非真正的冗余。总体而言，稳健性分析强化了基准模型的两个核心结论——即现行篮子中美元超配、新元低配——同时指出欧元-日元的分配是对外国通胀处理方式以及累积滞后与分布滞后选择最为敏感的维度。

鉴于在任何方案中欧元和日元合计从未超过篮子的约8%，且这两种货币在各模型间表现为近乎完美的替代品——保留一种时另一种即被排除——当局可考虑简化篮子，将两者剔除，并将其合计权重重新分配给美元、澳元和新元。这将形成一个更简洁的三货币篮子，与该国主要贸易和计价伙伴保持一致，降低篮子管理的操作复杂性，且鉴于这两种货币所起的边际性和方案敏感性作用，在通胀方差最小化方面几乎不会有所牺牲。代价是损失了对欧元和日元计价进口冲击的适度分散化效果，当局应就此与精简篮子带来的透明度和简化收益进行权衡。

## 结论

本文提出了一个与央行价格稳定使命相一致的优化货币篮子设计框架。我们并非根据贸易份额或外部金融敞口分配权重，而是在保持篮子累积传导率不变的约束下，选择使进口通胀中汇率驱动成分方差最小化的篮子构成。该问题表现为传导率空间中的马科维茨最小方差组合形式，其中双边汇率回报的方差-协方差结构以及货币特定传导系数的异质性共同决定了最优权重。

将该框架应用于一个实行五货币篮子的小型进口密集型岛国经济体，我们发现，相对于现行配置，重新加权其构成可使进口通胀方差降低近20%，同时保持结构性传导率不变。优化后的权重与现行方案的历史均值大体一致，但将敞口从估计传导率在经济上较小或统计上较弱的货币，重新配置到那些传导率幅度与协方差属性组合更有利于稳定进口通胀的货币上。

虽然贸易份额权重透明且直观，但通常并非实现价格稳定的最优选择。通过根据估计的传导系数和汇率协方差调整贸易份额权重，可以在几乎不增加信息成本的情况下，在进口通胀波动性方面获得不可忽视的改善。该方法操作简单，依赖大多数央行已有的数据，并且得出的权重可按通常用于贸易审查的年度频率进行更新。两个自然的扩展方向留待未来研究：将本国经济与各货币区之间的商业周期同步性纳入考量，并考虑由存款和外债的金融美元化产生的资产负债表效应。将这些维度整合到最小方差框架中，将为小型开放经济体的最优篮子提供更完整的刻画。

## 附录 I. 推导

我们从篮子通胀传导的定义出发：

$$
z _ {t} ^ {B} = \sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\tag{1}
$$

我们的优化问题为：

$$
\operatorname{argmin} _ {\theta} \left[ \operatorname{Var} \left(z _ {t} ^ {B}\right) \right] = \operatorname{argmin} _ {\theta} \left[ \operatorname{Var} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) \right]\tag{2}
$$

其中 $z_{j,t} = \sum_{k=1}^{q}\beta_{j,k}\Delta e_{j,t-k}$

每个 $e_{j,t-k}$ 表示为以本币计价的货币 $j$ 的价格。让我们将所有货币对重新以某一种不在篮子中的基准货币计价。

具体而言，我们有：

$$
\Delta e _ {j, t} ^ {F C / L C} = \Delta e _ {j, t} ^ {F C / F C _ {0}} + \Delta e _ {t} ^ {F C _ {0} / L C}\tag{3}
$$

其中 FC 代表篮子中的外币（例如：{USD, AUD, NZD, EUR, JPY}），LC 代表本币，$FC_{0}$ 代表不在篮子中的基准外币（例如：GBP）。

因此，

$$
V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} ^ {F C / L C}\right)\tag{4}
$$

$$
V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} \sum_ {k = 1} ^ {q} \beta_ {j, k} \left(\Delta e _ {j, t - k} ^ {F C / F C _ {0}} + \Delta e _ {t - k} ^ {F C _ {0} / L C}\right)\right)\tag{5}
$$

$$
V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} ^ {F C / F C _ {0}} + \sum_ {j = 1} ^ {n} \theta_ {j} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {t - k} ^ {F C _ {0} / L C}\right)\tag{6}
$$

$$
V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} ^ {F C / F C _ {0}} + \sum_ {j = 1} ^ {n} \theta_ {j} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {t - k} ^ {F C _ {0} / L C}\right)\tag{7}
$$

定义 $c_{j,t} = \sum_{k=1}^{p}\beta_{j,k}\Delta e_{t-k}^{FC_0/LC}$ ，则：

$$
V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {F C / F C _ {0}} + \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right)\tag{8}
$$

$$
\begin{array}{l} V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}\right) + V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) + \operatorname{cov} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}, \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) \\ + \operatorname{cov} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}, \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) ^ {T} \end{array}\tag{9}
$$

定义 $Z_{t}^{FC/FC_{0}} = \left\{ z_{j,t}^{FC/FC_{0}} \right\}$ ，$\Sigma_{z}^{FC/FC_{0}} = \text{Var}(Z^{FC/FC_{0}})$ ，$\Sigma_{c} = \text{Var}(c_{t})$ ，以及 $\Gamma = \text{Cov}(Z_{t}^{FC/FC_{0}}, c_{t})$ 。则，

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = \theta^ {\prime} \Sigma_ {\mathrm{z}} ^ {\mathrm{FC/FC} _ {0}} \theta + \theta^ {\prime} \Sigma_ {\mathrm{c}} \theta + \theta^ {\prime} \Gamma \theta + \theta^ {\prime} \Gamma^ {\prime} \theta\tag{10}
$$

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = \theta^ {\prime} \left(\Sigma_ {\mathrm{z}} ^ {\mathrm{FC/FC} _ {0}} + \Sigma_ {\mathrm{c}} + \Gamma + \Gamma^ {\prime}\right) \theta\tag{11}
$$

定义 $\Sigma_{\overline{Z}} = \Sigma_{z}^{\mathrm{FC / FC_0}} + \Sigma_c + \Gamma +\Gamma '$

因此，

$$
\boxed {a r g m i n _ {\theta} \left[ V a r (z _ {t} ^ {B}) \right] = a r g m i n _ {\theta} \left[ V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) \right] = a r g m i n _ {\theta} [ \theta^ {\prime} \Sigma_ {\overline {{Z}}} \theta ]}\tag{12}
$$

## 参考文献

Betts, Caroline, and Michael B. Devereux. 2000. “Exchange Rate Dynamics in a Model of Pricing-to-Market.” Journal of International Economics, 50(1): 215–244.

Bhandari, Jagdeep S. 1985. "Experiments with the Optimal Currency Composite." Southern Economic Journal, 51(3): 711–730.

Branson, William H., and Louka T. Katseli, 1981. "Currency Baskets and the Real Effective Exchange Rates." NBER Working Paper 0666, National Bureau of Economic Research, Inc.

Calvo, Guillermo A. 1983. “Staggered Prices in a Utility-Maximizing Framework.” Journal of Monetary Economics, 12(3): 383–398.

Campa, José Manuel, and Linda S. Goldberg. 2005. "Exchange Rate Pass-Through into Import Prices." Review of Economics and Statistics, 87(4): 679–690.

Edison, Hali J., and Erling Vårdal. 1990. “Optimal Currency Baskets for Small, Developed Economies.” Scandinavian Journal of Economics, 92(4): 559–571.

Flanders, M. June, and Elhanan Helpman. 1979. “An Optimal Exchange Rate Peg in a World of General Floating.” Review of Economic Studies, 46(3): 533–542.

Gopinath, Gita, and Oleg Itskhoki. 2010. “Frequency of Price Adjustment and Pass-Through.” Quarterly Journal of Economics, 125(2): 675–727.

Gopinath, Gita, Oleg Itskhoki, and Roberto Rigobon. 2010. "Currency Choice and Exchange Rate Pass-Through." American Economic Review, 100(1): 304–336.

Imam, Patrick A. 2010. “Exchange Rate Choices of Microstates.” IMF Working Paper No. 10/12. Washington, DC: International Monetary Fund.

Jayaraman, T. K., and C-K., Choong. 2011. "Impact of Exchange Rate Changes on Domestic Inflation: A Study of a Small Pacific Island Economy." MPRA Paper No. 33719, University Library of Munich.

Knetter, Michael M. 1989. "Price Discrimination by U.S. and German Exporters." American Economic Review, 79(1): 198–210.

Krugman, Paul. 1986. "Pricing to Market When the Exchange Rate Changes.", NBER Working Paper 1926, National Bureau of Economic Research, Inc.

Ma, Zihui, and Leonard K. Cheng. 2014. “An Optimal Currency Basket to Minimize Output and Inflation Volatility: Theory and an Application to Hong Kong.” Pacific Economic Review, 19(1): 90–111.

Peiris, S. J., and D. Ding. 2012. "Global Commodity Prices, Monetary Transmission, and Exchange Rate Pass Through in the Pacific Islands."

Shioji, Etsuro. 2006. “Invoicing Currency and the Optimal Basket Peg for East Asia: Analysis Using a New Open Economy Macroeconomic Model.” Journal of the Japanese and International Economies, 20(4):569–589.

Slavov, Slavi T. 2005. “Should Small Open Economies in East Asia Keep All Their Eggs in One Basket? The Role of Balance Sheet Effects.” Journal of the Korean Economy, 9(1): 1–43.

Teo, Wing Leong. 2009. "Should East Asia's Currencies Be Pegged to the Yen? The Role of Invoice Currency." Journal of the Japanese and International Economies, 23(3): 283–308.

Turnovsky, Stephen J. 1982. "A Determination of the Optimal Currency Basket: A Macroeconomic Analysis." Journal of International Economics, 12(3–4): 333–354.

Williamson, John. 1998. “Crawling Bands or Monitoring Bands: How to Manage Exchange Rates in a World of Capital Mobility.” International Finance, 1(1): 59–79.

Xu, Juanyi. 2011. "Optimal Currency Basket with Vertical Trade." Journal of International Money and Finance, 30(7): 1323–1340.

Yoshino, Naoyuki, Matthias Helble, and Ahmad Danu Prasetyo. 2017. “Exchange Rate Policy in the Pacific: An Evaluation of Currency Basket Regimes.” Asian-Pacific Economic Literature, 31(1): 3–20.

Yoshino, Naoyuki, Sahoko Kaji, and Ayako Suzuki. 2004. “The Basket-Peg, Dollar-Peg, and Floating: A Comparative Analysis.” Journal of the Japanese and International Economies, 18(2): 183–217.

Zhang, Zhichao, Nan Shi, and Xiaoli Zhang. 2011. “China’s New Exchange Rate Regime, Optimal Basket Currency and Currency Diversification.” MPRA Paper No. 32642. Munich: University Library of Munich.

[[KC_IMAGE_006]]
