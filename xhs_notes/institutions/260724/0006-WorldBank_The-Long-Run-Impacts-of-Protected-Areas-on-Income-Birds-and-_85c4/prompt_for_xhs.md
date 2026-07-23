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
# The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa

Dennis Engist

Gabriel Englander

Alan Lee

Frederik Noack

POLICY RESEARCH WORKING PAPER 11430

## Abstract

Protected areas cover $17\%$ of the world's land surface, yet credible evidence on their long-run economic and ecological impacts remains scarce. This paper estimates the effects of South Africa's protected areas on household income, bird biodiversity, and tourism consumer surplus. For the income and biodiversity analyses, it develops a machine-learning counterfactual approach that recovers the present-day impacts of protected areas created up to 100 years ago. Short-run impacts of newer protected areas are small and statistically insignificant, while older protected areas generate large gains. Prior research may have severely underestimated the benefits of protected areas by only estimating the short-run effects of newly established protected areas. In aggregate, this paper estimates that protected areas increase annual household income by approximately R300 billion (roughly 10% of 2011 GDP). This yields approximately 7.6 million job-equivalents attributable to South Africa's protected areas. Different types of protected areas play complementary roles in conserving different categories of threatened birds, demonstrating the value of South Africa's entire protected area network. A structural travel cost model estimates that South Africa's national parks generate R7.7 billion per year (2023 rand) in recreational value for domestic and international tourists. These results suggest that in South Africa there is little tradeoff between wildlife conservation and economic development. Realizing the economic and ecological benefits of protected areas, however, requires patience: returns to conservation accumulate over decades, not years.

![](images/0c97b62bceb01e1685cc5420d4c5eb2c06aafff9e25474d9676d54e1c975b044.jpg)

# The Long-Run Impacts of Protected Areas on Income, Birds, and Tourism in South Africa\*

Dennis Engist $^{\dagger}$ Gabriel Englander $^{\ddagger}$ Alan Lee $^{\S}$ Frederik Noack $^{\P}$

Authorized for distribution by Florence Kondylis, Research Manager, Development Research Group, Development Economics, World Bank Group

JEL classi ication: Q56, Q57, Q26, O13, C21

Keywords: Protected areas, Household income, Biodiversity conservation, Tourism, South Africa

## 1 Introduction

Protected areas are the principal instrument for conserving biodiversity (Gurney et al., 2023; Watson et al., 2014). Collectively spanning more than $17\%$ of the world's land surface, they represent one of the largest deliberate allocations of land to a single policy objective, with potentially far-reaching consequences for the economies of surrounding communities (UNEP-WCMC and IUCN, 2024). Yet robust causal evidence on their economic and ecological consequences remains limited. Because protected areas are typically established in locations with high biodiversity or low economic opportunity costs, simple correlations between protection, biodiversity, and development outcomes are prone to selection bias and reverse causality. While protected areas such as national parks contribute to human well-being through recreational opportunities, tourism revenue, and biodiversity benefits, they may also impose substantial economic costs by restricting local land use and limiting resource extraction (Bahrami, Gustafson, and Steiner, 2025).

These concerns raise a central policy dilemma. Governments may optimally locate protected areas in regions where conservation is inexpensive, but where biodiversity benefits and economic spillovers are limited (Pfaff et al., 2015; Grupp et al., 2023). This challenge is particularly acute because many global biodiversity hotspots are concentrated in developing and emerging economies, where conservation competes directly with poverty reduction and economic development objectives (Myers et al., 2000). Understanding whether protected areas simultaneously promote biodiversity conservation and local economic welfare is therefore critical for global conservation policy.

We study these questions in South Africa, one of the world's most biologically diverse countries and a globally recognized biodiversity hotspot. South Africa hosts exceptional levels of plant, bird, and invertebrate diversity and supports iconic megafauna including elephants, lions, and rhinoceroses. The country maintains an extensive protected area network, covering approximately $11\%$ of its terrestrial land surface and consisting of national parks, provincial nature reserves, and a rapidly expanding system of private conservation areas (Figure 1). Despite well-developed management systems, many protected areas face pressures from poaching, land encroachment, and surrounding economic deprivation, potentially limiting conservation effectiveness.

South Africa simultaneously faces severe socio-economic challenges, including high unemployment and persistent inequality. Nature-based tourism represents a major economic sector, with protected areas serving as key attractions. Protected areas contribute to human well-being through tourism revenues accruing to local communities and substantial recreational consumer surplus enjoyed by domestic and international visitors. Biodiversity spillovers may further affect surrounding communities through ecosystem services and wildlife-related damages (Gulati et al., 2021; Noack, Engist, and Larsen, 2025). Conversely, conservation restrictions may constrain agricultural expansion and resource-based livelihoods in rural regions. Whether protected areas alleviate or exacerbate local economic challenges, therefore, remains an open empirical question.

Quantifying the causal impacts of protected areas is difficult because protection is not randomly assigned. Standard approaches in economics rely on two-way fixed effects (TWFE) designs that compare outcomes before and after protected area establishment relative to contemporaneous changes in outcomes in non-protected areas. However, many of the world's most important protected areas were established decades before modern socio-economic and biodiversity data became available. For example, Kruger National Park was formally established in 1926. Consequently, TWFE approaches primarily identify short-run impacts of newly-established protected areas and implicitly assume that conservation effects do not evolve over time and that older and newer protected areas are comparable.

![](images/5622c493f7b511b973d16f58cf15ae5d6cf03a94906ed300707b22821b879816.jpg)  
Figure 1: A map of South Africa with protected areas in green, national parks labelled in black, and major cities labelled in blue.

To overcome these limitations, we develop a complementary identification strategy grounded in the literature on economic geography and long-run development. We assemble a spatial dataset of pre-protection geographic variables that are known to shape long-run economic outcomes (Gollin, Parente, and Rogerson, 2002; Bleakley and Lin, 2012; Nunn and Puga, 2012; Dell, Jones, and Olken, 2012; Jedwab and Moradi, 2016; J Vernon Henderson et al., 2018; Donaldson, 2018), consisting of predictors of economic activity determined before the establishment of South Africa's first national park. These variables include historical railway networks, early twentieth-century economic agglomerations, climatic conditions, agricultural suitability, and terrain ruggedness.

Using machine-learning prediction algorithms trained exclusively on locations distant from protected areas, we estimate counterfactual household income based solely on pre-protection characteristics. This counterfactual prediction represents what income would have been in the absence of protected areas. Comparing predicted and observed incomes allows us to recover both short- and long-run economic impacts of protected areas. We apply the same framework to bird biodiversity outcomes while incorporating additional ecological predictors such as ecoregions.

We find that protected areas generate positive long-run economic and ecological effects. Old protected areas significantly increase local household income, while recently established protected areas exhibit small and statistically insignificant short-run impacts. National parks produce larger income gains than other types of protected areas. Simultaneously, protected areas preserve threatened bird species and shift bird communities toward species reliant on intact natural habitats. Finally, a key motivation for establishing protected areas, including national parks, is their contribution to human well-being through recreational value. Visitors derive enjoyment that is not fully captured by entrance fees but is at least partially reflected in their willingness to travel long distances to visit a protected area. These benefits may be substantial, as they are a direct and intended consequence of establishing protected areas. We use a structural travel-cost model to estimate that South Africa's national park system generates approximately R7.7 billion annually in tourism consumer surplus, with domestic visitors capturing roughly one-quarter of the total.

The concordance between our machine-learning counterfactual approach and conventional TWFE estimates is reassuring, but the larger effects estimated for long-established protected areas could still reflect spatial selection into conservation. That is, early planners may have preferentially protected locations with inherently higher economic or ecological potential. We test this selection concern directly using predicted counterfactual outcomes based solely on pre-protection characteristics. We find no evidence that older protected areas were placed in more favorable locations, which suggests that their larger impacts primarily reflect dynamic processes that unfold over decades.

A growing interdisciplinary literature evaluates the impacts of protected areas on development and conservation outcomes (Sims, 2010; Ferraro and Hanauer, 2014; Andam et al., 2010; Pfaff et al., 2015; Grupp et al., 2023; Geldmann et al., 2013; Gray et al., 2016; Denny, Englander, and Hunnicutt, 2024; Baylis, Garcia, and Heilmayr, 2026). Our paper contributes to this literature by jointly quantifying economic, biodiversity, and recreational welfare impacts within a unified causal framework—an integration that prior analyses have not attempted. More fundamentally, the existing literature predominantly relies on short-run variation in protection status. Our findings suggest that this risks substantially underestimating the long-run benefits of conservation.

Taken together, our results suggest that protected areas can simultaneously enhance biodiversity conservation and generate substantial economic benefits. These findings provide cautious optimism that biodiversity-rich emerging economies can leverage conservation investments to support both ecological sustainability and economic development.

## 2 Household Income

We estimate the impact of South African protected areas on household income using data from the South African census, which provides monthly household income for 4,277 electoral wards in 2001 and 2011 (Statistics South Africa, 2011a). South Africa did not release income data from its 2021 census or from censuses before 2001 at the ward level. This narrow temporal window of 2001 to 2011 illustrates the limits of TWFE models in this setting: they only allow estimation of short-term effects of the small number of protected areas established in this period. For this reason, we complement the TWFE panel estimation with a cross-sectional regression and a machine learning approach to capture the long-term effects of the full protected area network.

In all models and specifications, we use log-transformed total household income per ward as the outcome. We use total rather than per capita income to capture not only individual income gains, but also the aggregate economic effects of labor migration. Our treatment variables are the log-transformed area (in square meters) of protected areas within the ward and, separately, within a 15 km buffer surrounding the ward. We select 15 km as the buffer distance because the average ward area of $285 \, km^2$ corresponds roughly to a square with 15 km sides, so the buffer extends spillover detection to approximately one ward-length beyond each ward's boundary. This specification allows us to capture both the direct local impacts of protected areas and the spatial spillover effects on neighboring communities. In the cross-sectional and machine learning estimations, we further subset the treatment variable in three ways: all protected areas pooled together, national parks versus other types of protected areas, and protected areas separated into age groups by the year in which they were established. To correct for spatial autocorrelation and generated regressors, we calculate standard errors using spatial block bootstrapping across all models. Specifically, because our machine learning approach relies on predicted counterfactuals as inputs, standard analytical errors would ignore the sampling variation from this first-stage estimation and artificially deflate our confidence intervals. By resampling spatial blocks and re-estimating the entire procedure for each draw, the bootstrap accurately accounts for both local spatial dependence and the additional uncertainty introduced by the generated regressors.

In the TWFE model, the treatment exposure of electoral wards is restricted to the protected areas established from 2002 to 2011, with 2001 serving as the baseline. Year and ward fixed effects (i.e., binary variables for each year and each electoral ward) absorb annual income shocks common across all wards and all time-invariant differences between wards, respectively. The resulting estimates stem from comparing the change in income from 2001 to 2011 between electoral wards with different levels of expansion of protected areas. To avoid further limiting the sample, in the TWFE approach we only estimate the pooled specification, grouping all protected areas together.

To estimate the long-term effects of the full set of protected areas, we deploy two distinct strategies. First, we use the household income data as a repeated cross-sectional outcome in an Ordinary Least Squares (OLS) linear regression, controlling for an extensive set of covariates. These covariates are not determined by protected areas; they consist of environmental characteristics (e.g., temperature, elevation, ruggedness, distance to rivers) and historical infrastructure (e.g., distance to railways in 1925, distance to metropolitan centers in 1921 — see Figure B.1). By explicitly controlling for these determinants of income, we absorb differences in economic potential across wards. This approach relies on the assumption that, conditional on these controls, the placement of protected areas is quasi-random, so that the residual variation explained by the protected area treatment variables is the causal effect of protected areas on income. Importantly, this assumption does not require that the controls capture all determinants of household income—only that they are sufficient to render the placement of protected areas uncorrelated with unobserved determinants of income.

Second, we apply the same core logic using a more sophisticated machine learning approach. Rather than using the environmental and historical variables simply as linear controls, we train an XGBoost algorithm to predict household income based on these variables. Crucially, we train it only on untreated electoral wards: those that are located, on average, more than 15 km away from the nearest protected area and do not contain any protected areas (see Figure B.2 for a map of training wards). We then use the trained model to predict income for all wards, which yields a counterfactual income level in the absence of protected areas (see Tables C.1 and C.2 and Figure B.3 for XGBoost model parameters and out-of-fold performance of the income and nightlights predictions). We achieve out-of-fold $R^{2}$ -values of 0.34 for household income prediction, and 0.3 for nighttime lights. While traditional in-sample spatial regressions demonstrate that fundamental geographic characteristics can explain up to 35% of the within-country variation in economic activity (J Vernon Henderson et al., 2018), an out-of-fold $R^{2}$ of 0.34 is robust and aligns with the performance of established spatial machine learning applications predicting local economic well-being (Yeh et al., 2020). The difference between observed and predicted income is then regressed on our protected area treatment variables. As in the cross-sectional linear approach, we run separate estimations for all protected areas, protected areas by type, and protected areas by age group.

Across both the cross-sectional regression and machine learning approaches, we find positive and statistically significant effects of protected areas on household income (Figure 2, left panel titled “All”; see Table C.3, C.4, C.5, C.6, C.7, and C.8 for full income and nightlights regression output tables). An addition

[中间内容因长度限制已省略]

></tr><tr><td>Biome 19</td><td>0.0524(0.0678)</td><td>-0.1977(0.1444)</td><td>0.1090(0.2111)</td><td>1.626(1.646)</td><td>0.5087(1.002)</td><td>1.073(0.7678)</td></tr><tr><td>Biome 9</td><td>-0.2158(0.1354)</td><td>-0.0903(0.1268)</td><td>0.3625(0.2761)</td><td>-1.997(4.038)</td><td>-1.300(1.670)</td><td>-1.972(1.446)</td></tr><tr><td>Biome 26</td><td>0.1076(0.0867)</td><td>0.1750(0.1482)</td><td>0.0346(0.2394)</td><td>-2.552(2.427)</td><td>1.406(1.306)</td><td>-2.157*(1.116)</td></tr><tr><td>Biome 29</td><td>0.4772***(0.1728)</td><td>0.1532(0.1782)</td><td>0.2048(0.3602)</td><td>-0.6374(3.168)</td><td>-0.4228(1.713)</td><td>0.9681(1.413)</td></tr><tr><td>Biome 18</td><td>0.0640(0.1059)</td><td>0.0088(0.1404)</td><td>-0.3731**(0.1843)</td><td>-1.033(2.166)</td><td>-1.328(1.088)</td><td>1.085(1.105)</td></tr><tr><td>Fixed-effects year</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="7">Fit statistics</td></tr><tr><td> $R^2$ </td><td>0.46111</td><td>0.15866</td><td>0.22584</td><td>0.14111</td><td>0.47220</td><td>0.47523</td></tr><tr><td>Observations</td><td>292,955</td><td>292,955</td><td>292,955</td><td>292,955</td><td>292,955</td><td>292,955</td></tr></table>

Custom standard-errors in parentheses  
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1  
This table presents the results from estimating the models by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.31: Estimated Effect of Protected Areas on Bird Biodiversity (Adj. Species Richness Grouped by IUCN Threat Level, with Least Concern Split Into Urban Avoiders and Urban Adaptors) using the Machine Learning Approach–Protected Areas by Size

<table><tr><td>Dependent Variables: Model:</td><td>CR+EN (1)</td><td>VU (2)</td><td>NT (3)</td><td>LC (4)</td><td>Urban (5)</td><td>Non-urban (6)</td></tr><tr><td colspan="7">Variables</td></tr><tr><td>Size Q1 (Smallest)</td><td>-0.7726(1.119)</td><td>-2.442(2.526)</td><td>-10.01*(5.313)</td><td>24.71(100.1)</td><td>29.99(29.64)</td><td>-34.27(25.52)</td></tr><tr><td>Size Q2</td><td>-0.3939(0.3322)</td><td>-0.4034(0.3902)</td><td>0.5977(1.380)</td><td>6.909(10.51)</td><td>1.013(6.088)</td><td>1.137(3.669)</td></tr><tr><td>Size Q3</td><td>0.2214(0.4624)</td><td>0.0159(0.2742)</td><td>2.987***(1.039)</td><td>6.991(5.302)</td><td>-5.217(4.797)</td><td>2.429(3.041)</td></tr><tr><td>Size Q4 (Largest)</td><td>1.185***(0.2946)</td><td>0.0694(0.0518)</td><td>0.1057(0.1519)</td><td>-1.916(1.517)</td><td>-4.878***(0.8333)</td><td>2.589**(1.155)</td></tr><tr><td>Fixed-effects year</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="7">Fit statistics</td></tr><tr><td> $R^2$ </td><td>0.22302</td><td>0.00419</td><td>0.01723</td><td>0.00460</td><td>0.08230</td><td>0.04977</td></tr><tr><td>Observations</td><td>292,974</td><td>292,974</td><td>292,974</td><td>292,974</td><td>292,974</td><td>292,974</td></tr></table>

Custom standard-errors in parentheses  
Signif. Codes: \*\*\*: 0.01, \*\*: 0.05, \*: 0.1  
This table presents the results from estimating the machine learning counterfactual differences by ordinary least squares regression. Spatial block bootstrapped standard errors in parentheses.

Table C.32: Estimated Effect of Travel Cost on National Park Visitation

<table><tr><td></td><td>(1)Heterogeneous</td><td>(2)Pooled</td></tr><tr><td>Travel Cost (2023 R) × Domestic</td><td> $-1.028 \times 10^{-3}$  $(1.048 \times 10^{-4})$ </td><td></td></tr><tr><td>Travel Cost (2023 R) × International</td><td> $-1.286 \times 10^{-4}$  $(3.436 \times 10^{-5})$ </td><td></td></tr><tr><td>Travel Cost (2023 R)</td><td></td><td> $-2.598 \times 10^{-4}$  $(5.377 \times 10^{-5})$ </td></tr><tr><td> $R^{2}$ </td><td>0.861</td><td>0.858</td></tr><tr><td>Observations</td><td>48,415</td><td>48,415</td></tr></table>

Notes: This table presents the results from estimating Equation 10 by ordinary least squares regression. Column (1) is our primary specification, allowing the travel cost coefficient to differ between domestic and international visitors. Column (2) imposes a single travel cost coefficient as a robustness check. Both specifications include park fixed effects and origin-by-fiscal year fixed effects. Standard errors clustered at the origin level in parentheses. The main-text estimates that a $1\%$ increase in travel cost reduces visits by $1.4\%$ (domestic) and $2.1\%$ (international) are computed from the coefficients in Column (1) using Equation 13, $\eta_{ojt} = \hat{\alpha}_{g(o)} \times TC_{ojt} \times (1 - s_{ojt})$ , where $\hat{\alpha}_{g(o)}$ is the travel cost coefficient for the group (domestic or international) to which origin $o$ belongs, $TC_{ojt}$ is the travel cost for an origin-park-year, and $s_{ojt}$ is the smoothed visit share defined in Equation 9. Reported main-text values are visitor-weighted means computed separately for domestic and international visitors. The number of observations (48,415) is fewer than the total number of origin-park-year combinations (48,246 international + 1,926 domestic = 50,172) because Table Mountain and West Coast National Parks are missing data on the number of visitors for all but the final two years of our study period.
"""
