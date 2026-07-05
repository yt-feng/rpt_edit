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
Working paper

#12

February 2026

UNCTAD/WP/2026/1

Giovanni Valensisi
Policy Analysis and Research Branch
Division for Africa, Least Developed Countries and Special Programmes
UNCTAD
giovanni.valensisi@unctad.org

H. Birce Akay
Policy Analysis and Research Branch
Division for Africa, Least Developed Countries and Special Programmes

# Fragile Prosperity: Natural Disasters and Economic Growth in Small Island Developing States

## Abstract

This study re-examines the complex link between climate-related disasters and economic growth in developing countries, with a focus on the specific vulnerabilities of Small Island Developing States (SIDS). It underscores the importance of combining diverse disaster metrics to fully capture the risks faced by SIDS. Using system GMM estimation, the analysis reveals that SIDS experience disproportionately severe medium-term growth setbacks compared to other developing nations, even after accounting for standard growth determinants. This can be linked to sector-specific pathways of vulnerability, as storms have a relatively more pronounced impact on services growth, and floods on industrial value-added growth.

## Key words

Natural disasters, economic growth, climate change, small island developing states (SIDS), vulnerability.

## Contents

1. Introduction......3
2. Literature review......5
3. Data and related sources......8
3.1 Natural disasters' metrics......8
3.2 SIDS specificities through the lenses of disaster metrics......12
3.3 Dependent and control variables......14
4. Model specifications and estimation strategy......16
4.1 Introducing Disaster Variables into the Growth Model......16
4.2 Estimation Methodology......18
5. Results......21
6. Robustness checks......27
6.1 Capital Investment......27
6.2 Subsample Stability......28
7. Conclusions......30
References......31
APPENDIX......33

# 1. Introduction

Natural disasters are becoming a more prominent feature of our day-to-day lives. Scientific evidence has unequivocally warned that rising temperatures trigger an increase in the frequency and intensity of weather and climate extremes, with natural hazards entailing harsh socioeconomic impacts on the most vulnerable economies like Least Developed Countries (LDCs) or Small Island Developing States (SIDS) (Coronese et al., 2019; IPCC, 2022; UNCTAD, 2022). $^{1}$ Moreover, this trend will continue to intensify as anthropogenic greenhouse gas emissions progressively destabilize the climate system and surface temperatures break record after record.

Against this background, several initiatives have been implemented to enhance the monitoring and assessment of disaster risks under the Sendai Framework for Disaster Risk Reduction. $^{2}$ A range of alternative indicators have been proposed to gauge related countries’ vulnerabilities, including the Economic and Environmental Vulnerability Index, the University of Notre Dame’s Global Adaptation Initiative (ND-GAIN) Index and the Multidimensional Vulnerability Index (United Nations, 2024a, 2024b). Moreover, after years of intense negotiations, the 27th Conference of the Parties (COP 27) of the United Nations Framework Convention on Climate Change (UNFCCC) agreed to establish a fund for responding to loss and damage associated with the adverse effects of climate change, including extreme weather events and slow onset events (UNCTAD, 2023).

If the ongoing improvements in disaster risk monitoring and the operationalization of the loss and damage fund testify to the growing relevance of this issue in international debates, the analysis of the impacts of natural disasters on macroeconomic variables warrants further research. In particular, the understanding of the nexus between natural disasters and economic growth – i.e. the key driver of countries' capacity to sustainably mobilize resources for reconstruction and recovery – remains partial, or at best nuanced. The need for a fine-grained understanding of the relationship between natural disasters and growth is all the more pronounced in the case of LDCs and SIDS, for which data limitations have been most prevalent.

Hazards are defined as natural processes, such as storms or wildfires, that can trigger disasters only upon interaction with human-made features such as settlements, agriculture, infrastructure and the like (Chaudhary and Piracha, 2021). While acknowledging this important conceptual distinction, henceforth we refer to “natural disasters” in line with most of the literature concerned with the socio-economic impacts of natural hazards.

2 The Sendai Framework for Disaster Risk Reduction 2015-2030 is a document adopted at the third UN World Conference on Disaster Risk Reduction, outlining four international priorities for action: (i) Understanding disaster risk; (ii) Strengthening disaster risk governance; (iii) Investing in disaster reduction for resilience and; (iv) Enhancing disaster preparedness for effective response, and to "Build Back Better".

This paper contributes to filling this knowledge gap by empirically assessing the extent to which SIDS' specificities translate into a differentiated pattern of impacts of climate-related natural disasters on economic growth. $^{3}$

The paper is structured as follows: Sections 2 and 3 outline related literature and discuss methodological issues, particularly those related to the measurement of natural disasters, and of SIDS' specific vulnerabilities. Section 4 presents the econometric specification, and Section 5 examines the results. Sections 6 and 7 provide some robustness checks and conclusions, respectively.

![](images/6943a1dd5688cebf196df883370a2b78c5d9de056019dfee4ef4dedb55b03ae9.jpg)

# 2. Literature review

Natural disasters exert complex wide-ranging impacts on macroeconomic variables, from physical asset destruction to fiscal effects, and from productivity losses to reduced human capital investment, via health and education disruptions (Skidmore, 2022a; Ehlers et al., 2025). Disasters' effects on GDP growth play an important role in this respect, as growth represents not only the path to recovery, but also a key driver of countries' capacity to mobilize financial resources for reconstruction in a sustainable way. While a large body of literature has been devoted to this subject, its conclusions have so far offered a nuanced and somewhat inconclusive picture.

On the one hand, theoretical considerations do not provide a decisive answer on the relationship between natural disasters and GDP growth (Cavallo et al., 2013). In the aggregate neoclassical framework (i.e. the so-called augmented Solow model), the destruction of human or physical capital provoked by a disaster can trigger short-run growth spurts, as it triggers a temporary acceleration of investment to regain the steady-state equilibrium; however, this temporary adjustment is unlikely to affect the long-term growth determinant, namely technological progress. Endogenous growth theory offers even less clearcut predictions: in Schumpeterian models, natural disasters could even lead to higher growth by inducing reinvestments in new and more efficient vintages of capital; in so-called “AK models” with constant returns to capital/knowledge, the rate of growth would be unchanged, while in endogenous growth models with increasing returns, disasters would trigger a permanently lower growth path.

On the other hand, the empirical literature yields varied conclusions, depending on factors, such as the type of disasters considered, the metrics used to assess their impact, the sample of countries and time period, the focus on temporary versus long-term effects, as well as the array of methodologies employed (Botzen et al., 2019; Onuma et al., 2021; Cuaresma, 2022). In one of the seminal contributions on the subject, Skidmore and Toya (2002) show, using a cross-section of 89 countries, that climatic disasters are positively correlated with real GDP per capita growth, unlike their geological counterparts. The authors also find that higher frequencies of climatic disasters lead to stronger human capital accumulation and faster total factor productivity growth; a finding they interpret as a sign that disasters provide an incentive to update the capital stock with new vintages of technologies. The existence of similar “blessings in disguise effects” is also postulated by various studies on spatial economic resilience, underscoring effective public management as a key factor shaping the recovery (Nijkamp and Borsekova, 2019; Bănică et al., 2020). In the same vein, a study across United States’ counties estimated that disasters triggering federal aid raise per capita personal income over the long run (8 years), while local population and employment remain unaffected (Roth Tran and Wilson, 2024).

These rather benign conclusions are, however, contradicted by a wide range of other empirical studies, finding either no systematic effects, or negative ones. Cuaresma (2022), for instance, employs Bayesian model averaging techniques on a sample of 123 countries, and finds a consistent lack of partial correlation between the risk of natural disasters and economic growth, with no systematic evidence of effect heterogeneity across income levels or regions. Cavallo et al (2022) find evidence of sizeable negative effects on growth when the severity of disasters is determined by the associated mortality, but negligible effects when severity is determined by the physical intensity (which implies a more balanced sample of developed and developing economies).

Again, numerous studies – mainly based on panel data techniques suitable to address endogeneity concerns – find evidence of a negative effects of natural disasters on countries’ economic growth (Noy, 2009; Raddatz, 2009; Hochrainer, 2009; Loayza et al., 2012; Fomby et al., 2013; Felbermayr and Gröschl, 2014; Onuma et al., 2021; Naoaj, 2023; Ehlers et al., 2025). Though converging on the negative impacts of natural disasters on growth, this literature yields a nuanced picture in relation to the pattern and drivers of these results. Three main considerations stand out in this respect. First, most studies find heterogeneous impacts across countries, with nations at lower levels of income per capita and/or with lower human capital typically suffering more severe shocks (Noy, 2009; Loayza et al., 2012; Fomby et al., 2013; Felbermayr and Gröschl, 2014; Onuma et al., 2021; Naoaj, 2023). Second, distinct sectoral impacts emerge across disaster types, whereby agriculture and industry display heightened vulnerability, notably to droughts and storms (Raddatz, 2009; Loayza et al., 2012; Fomby et al., 2013; Coulibaly et al., 2020; Naoaj, 2023; Ehlers et al., 2025). Third, the negative effects on economic growth can be largely traced to the most severe disasters, while for less intense ones some studies even find positive effects (Loayza et al., 2012; Fomby et al., 2013; Felbermayr and Gröschl, 2014; Onuma et al., 2021; Naoaj, 2023). $^{4}$

Overall, the above picture points to the need to develop a more nuanced and context-specific understanding of the disaster-growth nexus, as “disasters can have differential effects depending on conditions, circumstances, study scope, and study design” (Skidmore, 2022b: 8). The present paper represents a step in that direction, unravelling the extent to which SIDS’ defining structural characteristics shape the relationship between natural disasters and growth. To the best of our knowledge, this is the first paper empirically testing whether these impacts in SIDS differ from those in other developing countries.

More broadly, our contribution is also related to the recent policy research emphasizing the unique climate vulnerabilities of SIDS, the potential risks of a “climate-debt trap”, as well as the rising magnitude of loss and damage (Ishizawa and Miranda, 2019; Slany, 2020; IPCC, 2022; Addison et al., 2022; Park and Samples, 2024; Panwar et al., 2024; Tandrayen-Ragoobur et al., 2026). Much of this literature has focused on financial gaps and proposed mechanisms to address them, in line with the progress of international negotiations on the establishment and operationalization of the Loss and Damage Fund, as well as the growing call for boosting of adaptation finance. While this paper does not directly address financing issues, an accurate understanding of the relationship between natural disasters and growth remains a precondition to develop viable forms of financial support for vulnerable countries.

![](images/d11d4a451b95e943b5ac4aa6a3a4050e6d965a445801cc2586ea9b7137d78c90.jpg)

# Data and related sources

The present section discusses data issues and is divided into three parts. The first subsection examines disaster-related data at granular level, presents related descriptive statistics and explains the construction of the frequency and intensity measures utilized in the following econometric analysis. The second subsection links key methodological considerations with the specific traits of SIDS vulnerability, while the third discusses control variables.

## 3.1 Natural disasters' metrics

Like most of the empirical literature reviewed above, data on natural disasters is drawn from the Emergency Events Database - EM-DAT (Delforge et al., 2023). EM-DAT provides core data on individual disasters, their location, date of occurrence, and their health and economic impacts, for 26,000 disasters worldwide, from 1900 to the present. The database is compiled from various sources of information, including UN agencies, non-governmental organizations, insurance companies, research institutes, and press agencies. Disasters are recorded if they meet at least one of the following inclusion criteria: (i) at least ten deaths (including dead and missing); (ii) at least 100 affected (people affected, injured, or homeless); and (iii) a call for international assistance or an emergency declaration. These criteria confine the dataset to major disasters with considerable economic consequences.

Since we focus on climate-related hazards, the analysis below is restricted to the following disaster types: droughts, floods, storms and a residual group including wildfires, extreme temperatures, wet mass movements and glacial lake outburst floods. Moreover, we circumscribe the sample to developing countries (as per M49 classification as of 2022). Finally, despite the existence of earlier data, we only focus on the 1979-2023 period to include a broader set of controls, some of which are not available before 1979, as well as to partly attenuate concerns about uneven data quality and improving coverage over time, which could generate spurious time biases. This choice is particularly important in the context of vulnerable countries such as SIDS, for which data availability and reliability are primary concerns.

Table 1 provides the summary statistics at individual disaster level, from which several considerations can be drawn. First, data availability differs across the various metrics of impact. Compared to the total number of climate-related disasters in the sample, the share of missing observations reaches 17 per cent in the case of the affected population, 27 per cent for the number of deaths and as much as 69 per cent for total economic damage. This limitation seems particularly pronounced in the case of droughts and storms. Second, the impacts of climate-related disasters display a marked variability across all dimensions. $^{5}$ Third, while droughts are relatively rare, they tend to have by far the most severe human and socio-economic costs. This is presumably due to their prolonged effects on agricultural markets and broader macroeconomic fundamentals, via food prices and import bill, as well as to the wide-ranging and multifaceted harm caused by water scarcity. Floods, conversely, are relatively common representing over half of the disasters in our sample, but typically entail more circumscribed impacts. A similar assessment applies to storms.

Table 1
Granular summary statistics of disaster variables, developing countries, 1979–2023

<table><tr><td></td><td>N</td><td>Mean</td><td>Median</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>All Climate-Related Disasters</td><td>8,372</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total Deaths</td><td>6,099</td><td>225.9</td><td>17</td><td>5,171.6</td><td>1</td><td>300,000</td></tr><tr><td>Total Affected</td><td>6,913</td><td>1,082,143.2</td><td>15,000</td><td>9,528,031.7</td><td>1</td><td>330,000,000</td></tr><tr><td>Total Damage (&#x27;000 US$)</td><td>2,609</td><td>455,845.9</td><td>45,000</td><td>1,798,851.2</td><td>3</td><td>40,000,000</td></tr><tr><td>Droughts</td><td>597</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total Deaths</td><td>49</td><td>11,921</td><td>80</td><td>49,151</td><td>2</td><td>300,000</td></tr><tr><td>Total Affected</td><td>457</td><td>5,626,472.5</td><td>1,000,000</td><td>26,450,721</td><td>380</td><td>330,000,000</td></tr><tr><td>Total Damage (&#x27;000 US$)</td><td>133</td><td>822,046.2</td><td>120,000</td><td>1,737,184.4</td><td>50</td><td>13,755,200</td></tr><tr><td>Floods</td><td>4,320</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total

[中间内容因长度限制已省略]

00560</td><td>0.00650</td><td>0.00670</td></tr><tr><td>Arellano-Bond test for AR(2) in first differences</td><td>0.566</td><td>0.497</td><td>0.517</td><td>0.490</td><td>0.531</td><td>0.494</td><td>0.610</td><td>0.601</td></tr><tr><td>Hansen test of overidentifying restrictions</td><td>0.379</td><td>0.346</td><td>0.366</td><td>0.379</td><td>0.231</td><td>0.183</td><td>0.240</td><td>0.209</td></tr></table>

Standard errors in parentheses  
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1  
Period fixed effects are included (coefficients not reported)

![](images/43a059c14eacc6d247a34c91c0e5f8af11447bc3128ac319ce42d3d999b7c111.jpg)

## Table A.4

Robustness Checks: Subsample Stability. SIDS Interactions, Dependent Variable: GDPpc growth, Sample: 106 Developing Countries, 2000-2023 (3-year period observations)

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td></tr><tr><td>VARIABLES</td><td>FR</td><td>N_FR</td><td>Inten</td><td>N_Inten</td><td>FR</td><td>N_FR</td><td>Inten</td><td>N_Inten</td></tr><tr><td>All Climate-Related Disasters</td><td>0.38(0.32)</td><td>0.02(0.06)</td><td>0.11(0.08)</td><td>0.02(0.05)</td><td></td><td></td><td></td><td></td></tr><tr><td>SIDS x All Disasters</td><td>-0.52(0.34)</td><td>0.02(0.06)</td><td>-0.23**(0.10)</td><td>-0.01(0.05)</td><td></td><td></td><td></td><td></td></tr><tr><td>Droughts</td><td></td><td></td><td></td><td></td><td>-0.08(0.20)</td><td>-0.06(0.07)</td><td>-0.03(0.03)</td><td>-0.03(0.03)</td></tr><tr><td>Floods</td><td></td><td></td><td></td><td></td><td>0.28(0.21)</td><td>0.14*(0.08)</td><td>0.08(0.06)</td><td>0.07(0.05)</td></tr><tr><td>Storms</td><td></td><td></td><td></td><td></td><td>0.11(0.20)</td><td>0.07(0.08)</td><td>0.06(0.05)</td><td>0.06(0.04)</td></tr><tr><td>Other Climate-Related Disasters</td><td></td><td></td><td></td><td></td><td>0.31(0.19)</td><td>0.11(0.08)</td><td>0.10**(0.05)</td><td>0.09**(0.04)</td></tr><tr><td>SIDS x Droughts</td><td></td><td></td><td></td><td></td><td>1.39*(0.72)</td><td>0.33*(0.20)</td><td>0.29***(0.07)</td><td>0.23***(0.05)</td></tr><tr><td>SIDS x Floods</td><td></td><td></td><td></td><td></td><td>-0.71*(0.38)</td><td>-0.27**(0.11)</td><td>-0.20*(0.11)</td><td>-0.16**(0.08)</td></tr><tr><td>SIDS x Storms</td><td></td><td></td><td></td><td></td><td>-0.66**(0.29)</td><td>-0.16*(0.09)</td><td>-0.14(0.09)</td><td>-0.12*(0.07)</td></tr><tr><td>SIDS x Other Disasters</td><td></td><td></td><td></td><td></td><td>-0.28(0.70)</td><td>0.07(0.21)</td><td>-0.11(0.18)</td><td>0.03(0.09)</td></tr><tr><td>Lagged Dependent Variable</td><td>0.00(0.14)</td><td>0.02(0.15)</td><td>-0.02(0.12)</td><td>0.02(0.14)</td><td>-0.03(0.15)</td><td>-0.02(0.15)</td><td>-0.01(0.15)</td><td>-0.00(0.14)</td></tr><tr><td>Initial Enrolment</td><td>-2.43(2.46)</td><td>-2.64(2.59)</td><td>-2.48(2.32)</td><td>-2.36(2.41)</td><td>-2.98(2.20)</td><td>-2.10(2.00)</td><td>-2.54(2.06)</td><td>-2.45(1.97)</td></tr><tr><td>Financial Depth</td><td>0.70(2.02)</td><td>1.25(2.06)</td><td>0.64(2.14)</td><td>0.96(1.95)</td><td>0.98(1.78)</td><td>0.23(1.80)</td><td>0.27(1.89)</td><td>0.12(1.79)</td></tr><tr><td>Government Consumption</td><td>-1.74(2.85)</td><td>-1.80(3.26)</td><td>-1.39(3.18)</td><td>-1.56(3.19)</td><td>-2.37(3.22)</td><td>-1.48(3.19)</td><td>-1.10(2.98)</td><td>-0.91(2.82)</td></tr><tr><td>Inflation</td><td>-8.18(24.68)</td><td>-1.80(25.09)</td><td>-15.28(25.86)</td><td>-3.88(24.69)</td><td>-11.77(23.47)</td><td>-11.19(23.40)</td><td>-14.26(19.98)</td><td>-15.44(19.87)</td></tr><tr><td>Trade Openness</td><td>1.60(2.10)</td><td>1.38(1.94)</td><td>2.55(2.00)</td><td>1.30(1.89)</td><td>2.88(1.85)</td><td>2.91*(1.71)</td><td>3.18*(1.88)</td><td>3.20*(1.83)</td></tr><tr><td>Terms of Trade</td><td>0.01(0.04)</td><td>0.02(0.04)</td><td>0.01(0.03)</td><td>0.02(0.04)</td><td>0.02(0.03)</td><td>0.02(0.03)</td><td>0.02(0.03)</td><td>0.02(0.03)</td></tr><tr><td>Constant</td><td>46.09(118.02)</td><td>16.63(118.24)</td><td>74.23(121.83)</td><td>25.85(117.21)</td><td>61.62(112.48)</td><td>58.25(111.96)</td><td>67.67(95.39)</td><td>76.04(94.75)</td></tr><tr><td>Observations</td><td>533</td><td>533</td><td>533</td><td>533</td><td>533</td><td>533</td><td>533</td><td>533</td></tr><tr><td>Number of ISO_num</td><td>106</td><td>106</td><td>106</td><td>106</td><td>106</td><td>106</td><td>106</td><td>106</td></tr><tr><td>Number of instruments</td><td>38</td><td>38</td><td>38</td><td>38</td><td>44</td><td>44</td><td>44</td><td>44</td></tr><tr><td>Arellano-Bond test for AR(1) in first differences</td><td>0.0151</td><td>0.0169</td><td>0.0132</td><td>0.0146</td><td>0.0287</td><td>0.0292</td><td>0.0233</td><td>0.0226</td></tr><tr><td>Arellano-Bond test for AR(2) in first differences</td><td>0.571</td><td>0.585</td><td>0.623</td><td>0.578</td><td>0.761</td><td>0.795</td><td>0.757</td><td>0.785</td></tr><tr><td>Hansen test of overidentifying restrictions</td><td>0.135</td><td>0.0676</td><td>0.191</td><td>0.0709</td><td>0.200</td><td>0.159</td><td>0.282</td><td>0.300</td></tr></table>

Standard errors in parentheses  
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Period fixed effects are included (coefficients not reported)

@UNCTAD
@UNCTAD
unctad.org/facebook
unctad.org/youtube
unctad.org/flickr
unctad.org/linkedin
"""
