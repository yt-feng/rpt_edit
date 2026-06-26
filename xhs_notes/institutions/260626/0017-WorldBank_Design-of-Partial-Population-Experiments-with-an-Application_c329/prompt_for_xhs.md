你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# Design of Partial Population Experiments with an Application to Spillovers in Tax Compliance

Guillermo Cruces

Dario Tortarolo

Gonzalo Vazquez-Bare

POLICY RESEARCH WORKING PAPER 11059

## Abstract

This paper develops a framework to analyze partial population experiments, a generalization of the cluster experimental design where clusters are assigned to different treatment intensities. The framework allows for heterogeneity in cluster sizes and outcome distributions. The paper studies the large-sample behavior of OLS estimators and cluster-robust variance estimators and shows that (i) ignoring cluster heterogeneity may result in severely underpowered experiments and (ii) the cluster-robust variance estimator may be upward-biased when clusters are heterogeneous. The paper derives formulas for power, minimum detectable effects, and optimal cluster assignment probabilities. All the results apply to cluster experiments, a particular case of the framework. The paper sets up a potential outcomes framework to interpret the OLS estimands as causal effects. It implements the methods in a large-scale experiment to estimate the direct and spillover effects of a communication campaign on property tax compliance. The analysis reveals an increase in tax compliance among individuals directly targeted with the mailing, as well as compliance spillovers on untreated individuals in clusters with a high proportion of treated taxpayers.

![](images/d66009dc61093aa0f1111d5ab3c8f2a1455ccf91b1e8fd442765d181c9d19647.jpg)

# Design of Partial Population Experiments with an Application to Spillovers in Tax Compliance\*

Guillermo Cruces, U. of Nottingham & CONICET-CEDLAS-UNLP
Dario Tortarolo, World Bank DECRG
Gonzalo Vazquez-Bare, UC Santa Barbara

JEL CODES: C01, C93, H71, H26, H21, O23.

KEYWORDS: partial population experiments, spillovers, randomized controlled trials, cluster experiments, two-stage designs, property tax, tax compliance.

## 1 Introduction

Randomized controlled trials (RCTs) are extensively used in economics. A large fraction of these experiments are based on the assumption that the treatment assignment of one unit or subject does not influence the outcomes of others. The assumption of no interference, however, may be violated in many settings. In such cases, identifying and measuring spillovers between units is crucial for understanding the nature and magnitude of interactions between subjects, as well as for accurately assessing the direct impact of the treatment.

While the early experimental literature considered the impact on untreated units in an ex-post manner (e.g. Miguel and Kremer, 2004), field experiments incorporating spillover effects into their design have gained traction in applied research. In settings where units are grouped into independent clusters, such as schools, villages, or firms, a common design is the partial population design. Partial population designs are a generalization of the clustered design wherein clusters assigned to different treatment intensities or saturations are compared to pure control clusters with no treated units (Moffit, 2001; Duflo and Saez, 2003; Hudgens and Halloran, 2008; Hirano and Hahn, 2010; Baird et al., 2018). The variation in treatment intensity allows researchers to disentangle the direct and indirect effects of a treatment. In this paper, we provide a framework to analyze this type of experiment when clusters are heterogeneous.

We consider two dimensions of cluster heterogeneity that have important practical implications: heterogeneity in cluster sizes and heterogeneity in outcome distributions across clusters (distributional heterogeneity) $^{1}$ . When analyzing an experiment with heterogeneous clusters, correctly accounting for this heterogeneity is crucial for several reasons. On the one hand, variance formulas have to be adjusted accordingly, and failing to do so may result in severely underpowered experiments. On the other hand, cluster heterogeneity can affect the accuracy of the large sample normal approximation, and inference based on this approximation can be misleading when clusters are very heterogeneous (Carter, Schnepel and Steigerwald, 2017; Djogbenou, MacKinnon and ∅rregaard Nielsen, 2019; Hansen and Lee, 2019; Sasaki and Wang, 2022; Chiang, Sasaki and Wang, 2023).

With these challenges in mind, our paper provides five contributions. First, in Theorem 1, we derive an asymptotic distributional approximation for OLS regression estimators in a setting with between-cluster heterogeneity. We consider a double-array asymptotic setting where cluster sizes are allowed, but not required, to grow with the sample size. We provide conditions under which OLS estimators are consistent for cluster-size-weighted averages of within-cluster differences in means, and are asymptotically normal. We also show that, in the presence of distributional heterogeneity, the usual cluster-robust variance estimator is generally upward-biased, and hence inference based on this estimator is conservative (Proposition 1). While similar results have been obtained in design-based settings with non-random potential outcomes (see e.g. Hudgens and Halloran, 2008; Basse and Feller, 2018; Abadie et al., 2022; Jiang, Imai and Malani,

2023), to our knowledge we are the first to show this result in a superpopulation setting under distributional heterogeneity.

Our second contribution is to derive explicit, closed-form formulas to conduct power and minimum detectable effect (MDE) calculations under the two aforementioned sources of cluster heterogeneity. We then consider an intermediate setting where clusters differ in size but not in their outcome distributions, which simplifies power and minimum detectable effects calculations and can be applied more easily when baseline outcome data is not available. We show how our formulas generalize those available in the existing methodological literature on experimental design (Duflo, Glennerster and Kremer, 2007; Hirano and Hahn, 2010; Baird et al., 2018) by allowing for multiple treatment intensities, cluster heterogeneity, heteroskedasticity and general forms of intracluster correlation in outcomes and treatments.

Our third contribution is to derive optimal assignment probabilities determining the proportion of clusters to be assigned to each treatment saturation (Theorem 2). We provide a tractable, closed-form solution to the optimal choice problem of minimizing a weighted average of estimators' variances. We also discuss how alternative optimality criteria may be used in combination with our variance formulas using numerical methods.

Our fourth contribution is to set up a potential outcomes framework with within-cluster spillovers, heterogeneous treatment effects, and heterogeneous clusters. We use this framework to provide sufficient conditions for OLS estimands to recover causal direct and spillover effects.

Fifth, based on our framework, we designed and conducted a large-scale field experiment to estimate direct and spillover effects of a randomized communication campaign on property tax compliance in Argentina. Our experiment sent personalized letters to randomly selected dwellings with reminders about taxes due, information about the status of the account, due dates, past due debt, and payment methods. While there is ample evidence on the effect of tax reminders on compliance and collection (Antinyan and Asatryan, 2024), our goal was to find evidence on relatively elusive spillover effects from information campaigns on tax collection. We designed the experiment based on our methodological results to capture spillover effects of our mailings on neighbors who live in the same street blocks of treated individuals but who did not receive a letter. Our results reveal higher payment rates for treated individuals, but also for their untreated neighbors in the same street block, compared to accounts in pure control blocks where no one received the letter. Spillover effects are lower in magnitude but still substantial and precisely estimated in high-saturation street blocks, especially when accounting for expected (pre-registered) heterogeneity in past compliance: payment rates of untreated accounts in high saturation blocks with above median past compliance increased by 2.6 percentage points, compared to direct effects of about 5.1 percentage points.

Comparison with current literature. Our paper contributes to a growing literature on experimental design (Duflo, Glennerster and Kremer, 2007; Bruhn and McKenzie, 2009; Bugni, Canay and Shaikh, 2018, 2019; Bai, 2022) and in particular to the literature on design and analysis of experiments under spillovers or interference (Hirano and Hahn, 2010; Athey, Eckles and Imbens, 2018; Baird et al., 2018; Basse, Feller and Toulis, 2019; Jiang, Imai and Malani, 2023; Puelz et al., 2022; Viviano, 2024; Leung, 2022; Liu, 2023). More specifically, our results generalize those of Hirano and Hahn (2010), Hudgens and Halloran (2008) and Baird et al. (2018) by allowing for cluster heterogeneity, heteroskedasticity, general treatment assignment mechanisms and within-group correlation structures and alternative criteria for optimal treatment assignment.

In related work, Athey, Eckles and Imbens (2018), Basse, Feller and Toulis (2019) and Puelz et al. (2022) derive randomization inference tests for a general class of null hypotheses under interference. A closely related study is Jiang, Imai and Malani (2023), who analyze two-stage completely randomized experiments and provide randomization-based variance estimators and sample size formulas. Our results complement this literature by considering different estimands, different assignment mechanisms and by conducting super-population-based large-sample (instead of design-based) inference in a double array asymptotic framework. Our approach allows us to determine the role of cluster heterogeneity in the asymptotic behavior of the treatment effect estimators.

Our paper is also related to the literature on inference in clustered experiments, which are a particular case of partial population experiments with only two saturations and no within-cluster treatment variation. Bugni et al. (2023) study inference in clustered experiments with non-ignorable cluster sizes and derive variance estimators and valid inference procedures in a setup with random cluster sizes. We further discuss the relationship between our results and that paper in Section 3.5.

We also contribute to a large empirical literature on property taxes and a small but growing empirical literature on spillover effects in tax compliance. On property taxes, recent contributions include Brockmeyer et al. (2020) study of Mexico City, Bergeron, Tourek and Weigel (2024) and Weigel (2020) for the Democratic Republic of Congo, and Krause (2020) for Haiti, among others. The latter two are randomized controlled trials, and in both cases, the authors address the presence of spillovers, but in ex-post analysis rather than in the experimental designs. The effect of social interactions in tax compliance interventions has remained a relatively elusive issue in the broader experimental compliance literature. Some notable exceptions are Pomeranz (2015), who detects enforcement spillovers up the VAT chain in Chilean firms, Drago, Mengel and Traxler (2020) who study enforcement spillovers of TV licensing inspections on untreated households in Austria, and Boning et al. (2020) who analyze direct and network effects from in-person visits by revenue officers on visited and non-visited firms in the United States (see the review in Pomeranz and Vila-Belda, 2019, for more studies covering spillover effects). In Argentina, a recent study by Carrillo, Castro and Scartascini (2021) finds neighborhood spillover effects from a program that randomly awarded 400 taxpayers with the repair of a sidewalk. Whereas these papers find spillover effects in tax compliance, their original experiments were not designed to capture these effects. We build on these pioneering works with an intervention designed with the purpose of capturing spillovers.

The paper is organized as follows. Section 2 illustrates the practical importance of cluster heterogeneity when conducting power calculations. In Section 3, we set up our framework and derive the main results. In

Section 4, we implement our methods in a large-scale randomized communication campaign, we describe the administrative data used in the analysis, the empirical strategy, and evidence of direct and spillover effects. Section 5 provides some practical recommendations for designing and analyzing partial population experiments. Section 6 concludes.

## 2 Why is Cluster Heterogeneity Important?

We consider a population where units are grouped into mutually exclusive and independent clusters. Common examples of this type of clustering are students in schools (Miguel and Kremer, 2004; Beuermann et al., 2015), family members in households (Barrera-Osorio et al., 2011; Foos and de Rooij, 2017), job seekers in local labor markets (Crépon et al., 2013), employees in firms or organizations (Duflo and Saez, 2003), or households in neighborhoods, villages or other geographic administrative units (Angelucci and De Giorgi, 2009; Ichino and Schündeln, 2012; Haushofer and Shapiro, 2016; Giné and Mansuri, 2018). In our application, a local property tax reminder information campaign, the population of interest consists of taxpayers in residential blocks. Within this population, we study an experimental design where treatment assignments can vary both between and within clusters.

Figure 1 shows the distribution of cluster sizes in six partial population experiments, including our analysis sample and five published papers (Crépon et al., 2013; Giné and Mansuri, 2018; Haushofer and Shapiro, 2016; Ichino and Schündeln, 2012; Imai, Jiang and Malani, 2021). The figure reveals substantial variation in cluster sizes. When cluster sizes are heterogeneous, it is likely that the distribution of outcomes will vary across clusters as well. For instance, one may expect the mean and the variance of the outcome to be different in large clusters compared to small clusters. We refer to the variation in outcome distributions across clusters as distributional heterogeneity.

Intuitively, with heterogeneous clusters, the variance of an estimator of interest $\hat{\beta}$ , such as a difference in means between units in treated and untreated clusters (we define the estimators of interest precisely in the next section), can be decomposed into four parts:

$$
\mathbb {V} [ \hat {\beta} ] \approx \text {variance under uncorrelated observations}\tag{1}
$$

$$
+ \text {   clustering   with   equally - sized   clusters   }\tag{2}
$$

$$
+ \text { cluster   size   heterogeneity }\tag{3}
$$

$$
+ \text { cluster   distributional   heterogeneity }\tag{4}
$$

The first term is the variance that would be obtained if observations were uncorrelated within clusters. The second term is an adjustment factor that accounts for the within-cluster correlation, often known as the “design effect” or the “Moulton factor” (after Moulton, 1986) that depends on the average cluster size. The term in the third line represents the additional variation due to the heterogeneity in cluster sizes, which intuitively accounts for the variance of cluster sizes (Moulton, 1986, also derives this adjustment for a random effects model). Finally, the last component accounts for the between-cluster heterogeneity in outcome distributions. While the need to account for within-cluster correlations (lines (1) and (2)) is well-understood for designing and analyzing clustered experiments, the adjustment terms that account for cluster heterogeneity are typically assumed away by the literature on experimental design (e.g. Bloom, 2005; Duflo, Glennerster and Kremer, 2007; Hirano and Hahn, 2010; Baird et al., 2018).

To numerically illustrate the importance of appropriately accounting for cluster heterogeneity in this design, we consider the simple setting of a cluster RCT (which is a particular case of a partial population experiment) where “a few” clusters are “large”. Specifically, we consider a sample of 200 clusters, indexed by $g = 1, \ldots, 200$ , each having size $n_{g}$ . The first 10 clusters contain 100 units, $n_{g} = 100$ , and the remaining 190 clusters contain 25 units each, $n_{g} = 25$ (these values are chosen to match the median values in the literature in Figure 1). We assume the treatment has no effect, and the outcome of unit $i = 1, \ldots, n_{g}$ in cluster g is given by a random effects model: $Y_{ig} = \alpha_{g} + \nu_{g} + \omega_{ig}, \nu_{g} \stackrel{iid}{\sim} \mathcal{N}(0, 1/2)$ , $\omega_{ig} \stackrel{iid}{\sim} \mathcal{N}(0, 1/2)$ with $\nu_{g}$ independent of $\omega_{ig}$ and where $\alpha_{g}$ is a (non-random) intercept with $\alpha_{g} = 0$ if $n_{g} = 25$ and $\alpha_{g} = 1$ if $n_{g} = 100$ . This model implies that the average outcome is $E[Y_{ig}] = 1$ in large clusters and $E[Y_{ig}] = 0$ in small clusters. In addition, $V[Y_{ig}] = 1$ and the within-cluster correlation between outcomes is $cor(Y_{ig}, Y_{jg}) = 0.5$ .

Figure 2 plots three power functions for the d

[中间内容因长度限制已省略]

partial q _ {t} ^ {2}} = \frac {2 B _ {t} (\pmb {\omega})}{q _ {t} ^ {3}} + \frac {2 B _ {0}}{q _ {0} ^ {3}}, \quad \frac {\partial^ {2} f}{\partial q _ {t} \partial q _ {l}} = \frac {2 B _ {0}}{q _ {0} ^ {3}}
$$

and therefore the Hessian matrix H can be written as:

$$
\mathbf {H} = \mathrm{diag} \left(\frac {2 B _ {1} (\pmb {\omega})}{q _ {1} ^ {3}}, \dots , \frac {2 B _ {M} (\pmb {\omega})}{q _ {M} ^ {3}}\right) + \left(\frac {2 B _ {0}}{q _ {0} ^ {3}}\right) \mathbf {1} _ {M} \mathbf {1} _ {M} ^ {\prime}
$$

where $1_{M}$ is an $M \times 1$ vector of ones. Thus, for any non-zero $M \times 1$ vector v,

$$
\mathbf {v} ^ {\prime} \mathbf {H} \mathbf {v} = \sum_ {t = 1} ^ {M} \frac {2 B _ {t} (\boldsymbol {\omega}) v _ {t} ^ {2}}{q _ {1} ^ {3}} + \left(\frac {2 B _ {0}}{q _ {0} ^ {3}}\right) \mathbf {v} ^ {\prime} \mathbf {1} _ {M} \mathbf {1} _ {M} ^ {\prime} \mathbf {v} = \sum_ {t = 1} ^ {M} \frac {2 B _ {t} (\boldsymbol {\omega}) v _ {t} ^ {2}}{q _ {1} ^ {3}} + \left(\frac {2 B _ {0}}{q _ {0} ^ {3}}\right) \left(\sum_ {t = 1} ^ {M} v _ {t}\right) ^ {2} > 0
$$

using that $B_{t}(\omega) > 0$ for all t so the Hessian is positive definite as required. □

## D.6 Proof of Corollary 1

This proof follows from Theorem 1 and Proposition 1 setting $\mu_g(d,t) = \mu_n^p (d,t) = \mu (d,t)$ throughout.

## D.7 Proof of Proposition 2

Let $\mathcal{D}_g(d,t)$ denote the set of possible values for $\mathbf{D}_{(i)g}$ given $D_{ig} = d$ and $T_{g} = t$ . Then,

$$
\begin{array}{l} \mathbb {E} [ Y _ {i g} | D _ {i g} = d, T _ {g} = t ] = \sum_ {\mathbf {d} _ {g} \in \mathcal {D} _ {g} (d, t)} \mathbb {E} [ Y _ {i g} | D _ {i g} = d, \mathbf {D} _ {(i) g} = \mathbf {d} _ {g}, T _ {g} = t ] \mathbb {P} [ \mathbf {D} _ {(i) g} = \mathbf {d} _ {g} | D _ {i g} = d, T _ {g} = t ] \\ \qquad = \sum_ {\mathbf {d} _ {g} \in \mathcal {D} _ {g} (d, t)} \mathbb {E} [ Y _ {i g} (d, \mathbf {d} _ {g}) | D _ {i g} = d, \mathbf {D} _ {(i) g} = \mathbf {d} _ {g}, T _ {g} = t ] \mathbb {P} [ \mathbf {D} _ {(i) g} = \mathbf {d} _ {g} | D _ {i g} = d, T _ {g} = t ] \\ \qquad = \sum_ {\mathfrak {d} _ {g} \in \mathcal {D} _ {g} (d, t)} \mathbb {E} [ Y _ {i g} (d, \mathbf {d} _ {g}) ] \mathbb {P} [ \mathbf {D} _ {(i) g} = \mathbf {d} _ {g} | D _ {i g} = d, T _ {g} = t ] \\ \qquad = \sum_ {s _ {g} = 0} ^ {n _ {g} - 1} \mathbb {E} \left[ Y _ {i g} \left(d, \frac {s _ {g}}{n _ {g} - 1}\right) \right] \mathbb {P} [ S _ {i g} = s _ {g} | D _ {i g} = d, T _ {g} = t ] \end{array}
$$

where the first equality follows by the law of iterated expectations, the second equality plugs in the potential outcomes under the exclusion restriction (Assumption 6), the third equality uses independence (Assumption 7), and the fourth equality uses exchangeability (Assumption 8).

## D.8 Proof of Theorem 3

We verify the conditions for Theorem 1. First, condition (i) implies that Proposition 2 holds. Second, condition (ii) and Proposition 2 imply Assumption 1. Next, condition (iii) implies that:

$$
\begin{array}{r l} & {\mathbb {P} [ S _ {i g} = s _ {g} | D _ {i g} = d, T _ {g} = t ] = \frac {\mathbb {P} [ S _ {i g} = s _ {g} , D _ {i g} = d | T _ {g} = t ]}{p _ {g} (d | t)} = \frac {\mathbb {P} [ N _ {g} ^ {1} - D _ {i g} = s _ {g} , D _ {i g} = d | T _ {g} = t ]}{p _ {g} (d | t)}} \\ & {\qquad = \frac {\mathbb {P} [ N _ {g} ^ {1} = s _ {g} + d , D _ {i g} = d | T _ {g} = t ]}{p _ {g} (d | t)} = \mathbb {1} (s _ {g} + d = n _ {g} p _ {g} (1 | t)) \frac {\mathbb {P} [ D _ {i g} = d | T _ {g} = t ]}{p _ {g} (d | t)}} \\ & {\qquad = \mathbb {1} (s _ {g} = n _ {g} p _ {g} (1 | t) - d)} \end{array}
$$

and thus by Proposition 2, $\mathbb{E}[Y_{ig}^{\ell}|D_{ig} = d,T_g = t] = \mathbb{E}\left[Y_{ig}^{\ell}\left(d,\frac{n_g p_g(1|t) - d}{n_g - 1}\right)\right]$ . This fact also implies that

$$
\begin{array}{r l} & {\mathbb {E} [ Y _ {i g} | D _ {i g} = d, T _ {g} = t, \mathbf {D} _ {(i) g} ] = \sum_ {\mathbf {d} _ {g}} \mathbb {E} [ Y _ {i g} | D _ {i g} = d, T _ {g} = t, \mathbf {D} _ {(i) g} = \mathbf {d} _ {g} ] \mathbb {1} (\mathbf {D} _ {(i) g} = \mathbf {d} _ {g})} \\ & {\qquad = \sum_ {\mathbf {d} _ {g}} \mathbb {E} [ Y _ {i g} (d, (\mathbf {d} _ {g} ^ {\prime} \mathbf {1} _ {g} - d) / (n _ {g} - 1)) ] \mathbb {1} (\mathbf {D} _ {(i) g} = \mathbf {d} _ {g})} \\ & {\qquad = \sum_ {s _ {g}} \mathbb {E} [ Y _ {i g} (d, (s _ {g} / (n _ {g} - 1)) ] \mathbb {1} (S _ {i g} = s _ {g})} \\ & {\qquad = \mathbb {E} [ Y _ {i g} (d, (n _ {g} p _ {g} (1 | t) - d) / (n _ {g} - 1)) ]} \end{array}
$$

and an analogous argument gives the result for the joint moments, so Assumption 2 holds. Next, condition (iii) implies that Assumption 3 holds, so all the requirements for Theorem 1 are satisfied. Finally, by Proposition 2 and condition (iv),

$$
\beta_ {n} (d, t) := \sum_ {g} \frac {n _ {g}}{n} \mu_ {g} (d, t) - \sum_ {g} \frac {n _ {g}}{n} \mu_ {g} (0, 0) = \sum_ {g} \frac {n _ {g}}{n} \mathbb {E} \left[ Y _ {i g} \left(d, \frac {n _ {g} p (1 | t) - d}{n _ {g} - 1}\right) \right] - \sum_ {g} \frac {n _ {g}}{n} \mathbb {E} [ Y _ {i g} (0, 0) ]
$$

which completes the proof. □

## D.9 Proof of Theorem 4

This result follows from the fact that conditions (i) and (ii) imply Assumption 5 and thus under the conditions for Theorem 3, Corollary 1 holds. $\square$
"""
