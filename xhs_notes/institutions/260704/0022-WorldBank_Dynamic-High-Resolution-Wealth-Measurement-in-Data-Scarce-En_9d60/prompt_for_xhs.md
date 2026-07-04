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
# Dynamic, High-Resolution Wealth Measurement in Data-Scarce Environments

Zhuo Zheng

Timothy Wu

Richard Lee

David Newhouse

Talip Kilic

Marshall Burke

Stefano Ermon

David B. Lobell

POLICY RESEARCH WORKING PAPER 11058

## Abstract

Accurate and comprehensive measurement of household livelihoods is critical for monitoring progress toward poverty alleviation and targeting social assistance programs for those who most need it. However, the high cost of traditional data collection has historically made comprehensive measurement a difficult task. This paper evaluates alternative satellite-based deep learning approaches using detailed household census extracts from four African countries to accelerate progress toward comprehensive, fine-scale, and dynamic measurement of asset wealth at scale. The results indicate that transformer architectures solve multiple open measurement problems, by providing the most accurate measurement of local-level variation in household asset wealth across countries and cities, as well as changes in household asset wealth over time. Experiments that artificially restrict data availability show the model's ability to achieve high performance with limited data. The proposed approach demonstrates the promise of combining satellite imagery, publicly available geo-features, and new deep learning architectures for hyperlocal and dynamic measurement of wealth in data-scarce environments.

# Dynamic, High-Resolution Wealth Measurement in Data-Scarce Environments

Zhuo Zheng, $^{a}$ Timothy Wu, $^{a}$ Richard Lee, $^{b,c}$ David Newhouse, $^{d}$ Talip Kilic, $^{d}$ Marshall Burke, $^{c,e}$ Stefano Ermon, $^{a}$ and David B. Lobell $^{b,c}$

$^{a}$ Department of Computer Science, Stanford University, Stanford, 94305, CA, USA

$^{b}$ Department of Earth System Science, Stanford University, Stanford, 94305, CA, USA

$^{c}$ Center on Food Security and the Environment, Stanford University, Stanford, 94305, CA, USA

$^{d}$ Development Economics Data Group, World Bank Group, Washington DC, 20433, DC, USA

$^{e}$ Department of Environmental Social Science, Stanford University, Stanford, 94305, CA, USA

## ARTICLE INFO

Keywords:
Economic well-being
High-resolution
Poverty mapping
Satellite image
Deep learning

JEL codes: C45, I32

Accurate, up-to-date, and highly resolved measurements of economic well-being are essential for monitoring and achieving international goals of poverty alleviation. These goals include the United Nations' Sustainable Development Goal 1 of "No Poverty," which is nearing its original 2030 deadline, as well as countless other international and regional poverty targets. Granular estimates of household poverty and wealth are critical for understanding whether these goals are being met, as well as for targeting and evaluating anti-poverty interventions in regions where progress is lagging [6].

Official poverty measurement in low- and middle-income countries has long relied on household surveys, an indispensable but time-consuming tool for livelihood measurement. Given the technical capacity needed for reliable survey measurement and the substantial logistical difficulties in carrying out nationally or sub-nationally representative livelihood surveys, such surveys are often infrequently completed in much of the world, rendering comprehensive and timely measures of poverty and related outcomes unavailable for many periods in many regions $[6, 9]$ . Meanwhile, survey data are typically based on samples meant to be representative at larger spatial scales and are thus usually inadequate for generating reliable estimates at the village or neighborhood level – the level at which anti-poverty interventions often need to be targeted. Consequently, there is a pressing need for more cost-effective and scalable alternatives to local-level livelihood measurement that can complement and scale existing household survey-based efforts.

In recent years, the abundance of publicly available remote sensing data and recent advances in machine learning have transformed the livelihood measurement landscape, progressively shifting from national censuses and related household surveys to efforts to combine this information with information from satellites and other sensors. Early studies used coarse, publicly

available satellite imagery and/or mobile phone data, combined with early machine learning and deep learning architectures, to show how these new sources of information could be used to support broad-scale measurement of wealth and poverty $[4, 17, 29]$ . Subsequent studies introduced further refinements that used publicly available or proprietary geospatial data to improve satellite-based wealth measurement $[8, 12, 2]$ . These advances confirmed that leveraging satellite images and machine learning can be an accurate, inexpensive, and scalable solution to estimate wealth $[6, 21, 23]$ .

Here we assemble a large-scale, multi-resolution, and multi-temporal wealth dataset using national censuses or extracts obtained from National Statistics Offices and multi-spectral satellite imagery from multiple public and private sensors of varying resolutions. Our dataset comprises over 12 million households in four African countries (Malawi, Mozambique, Burkina Faso, and Madagascar) and, uniquely, contains precisely georeferenced measurements within two Malawian cities as well as repeated measurements of the same locations over time – two features lacking in prior studies.

We use these data to make four contributions relative to earlier work. First, we directly test a new type of deep learning model – specifically, vision transformers – against earlier deep learning architectures based on convolutional neural networks (CNNs) that are common in the literature, as well as against simpler models that use geospatial features and a tabular machine learning approach (XGBoost) for prediction. Specifically, we design a conditioning module that enables our transformer model to handle multi-modal inputs, integrating both satellite imagery and geospatial features simultaneously (see “Methods”). We test models that use satellite imagery from Landsat (30m/pixel), PlanetScope (3m/pixel), and/or SkySat (0.5m/pixel) sensors. We then compare these more sophisticated methods and inputs with simpler methods that rely

solely on predefined geospatial features from a range of sources.

These comparisons are important because simpler approaches that rely on publicly available data could be both easier and cheaper to implement at scale, particularly for public organizations interested in their widespread application, and so understanding performance tradeoffs across model architectures and inputs is critical to understanding how to scale promising new measurement approaches.

Second, a key advantage in our setting is the use of accurate, high-resolution data from national censuses or extracts for model training and evaluation. In contrast to earlier work that relied primarily on publicly available household survey data characterized by spatially imprecise location data and limited household samples, our data cover a much larger set of households in a given location and in some cases are precisely georeferenced. Comparisons against such “gold standard” data allow us to understand whether model prediction errors are a result of inaccurate predictions or noise in the measure of ground truth – an understanding that was often elusive in earlier work in developing countries $[6, 29]$ . In addition, it allows us to consider a wide range of sample sizes to assess the minimum training data requirements for advanced machine learning methods to produce accurate estimates. To quantify the importance of training sample size for performance, we extensively test the extent to which additional training data affects model performance across multiple settings.

Third, our high-resolution census data enables a novel understanding of how satellite imagery and other geospatial data can be used to predict variation in livelihoods within urban areas in Africa – a capability that was again hard to evaluate in previous settings given limited samples and spatial noise in training data. This could be particularly consequential in urban environments that exhibit substantial spatial variability in livelihoods even within small spatial domains. Using comprehensive and precisely georeferenced census data from two cities in Malawi, we are able to train and test models using different resolutions of satellite data, and we find that the models are surprisingly accurate in predicting street- and neighborhood-level variation in wealth within these cities.

Fourth, the censuses and extracts allow us to evaluate whether imagery-based models can make accurate predictions of changes in wealth over time. Previous efforts were again substantially constrained by ground data that did not repeatedly sample the same locations in different surveys $[29]$ . As a result, it remains unclear whether an imagery-based model trained largely to predict spatial variation in wealth or consumption would be able to predict temporal variation, as the latter is typically both smaller and potentially driven by changes that are harder to detect in imagery. Repeated census data from the same locations 10 years apart in Malawi and Mozambique allows us to evaluate whether models can indeed extract information from imagery capable of predicting temporal variation in asset wealth.

## Results

Performance on prediction of country-level wealth
For country-level wealth prediction, we train each model on each country individually and conduct country-wise five-fold cross validation for each model. The CNN model uses only Landsat satellite imagery as input. XGBoost utilizes geospatial features (geo-features) either alone or combined with satellite image statistical features. All models were trained to predict the asset wealth index (AWI) [29]. Estimates of AWI were generated and linked to imagery at fine administrative levels in Madagascar, Malawi, and Mozambique. In Burkina Faso, AWI estimates are only available for 334 communes (Table 1). This reduced the effective sample size of the training data in Burkina Faso, as seen in the clumped pattern of survey-measured asset wealth shown in the right panel of Figure 1d. This difference is reflected in the results. As shown in Figure 1a, a naive transformer model that does not condition on geo-features consistently outperforms other models across the Malawi, Mozambique, and Madagascar datasets. In those countries, predictions using the transformer model achieve $R^2$ values of 0.83, 0.70, and 0.62, respectively, when trained on the full census extract. In Burkina Faso, because of the smaller effective sample size, XGBoost using satellite imagery and geospatial features achieves the best average performance among the models (62.9% of variation explained). A naive transformer, when using only satellite imagery, remains competitive (57.4% of variation explained). We also limit the number of training samples to 1%, 5%, 10%, 25%, and 50% of the original training dataset to analyze how model performance varies with training sample size. Based on the results from these four countries, we empirically identify 10% as a critical inflection point for model performance, below which the accuracy of the estimates deteriorates rapidly.

Another key factor in reducing training sample collection costs for wealth prediction is the number of households aggregated per sample. To analyze this factor, we randomly sample 10 households per administrative area to construct the training sample, yielding a “10-household” training dataset for each country. We then train a naive transformer model on this “10-household” training set while still evaluating its performance on the original full household test set. The results (Figure 1b) indicate that our transformer models trained with the 10-household data exhibit comparable performance to those trained with data on all households. Using Malawi as an example, the 10-household data only include approximately 23% of all surveyed households. The performance gap between models trained on all households and the 10-household sample is only 3 percentage points (82% versus 79%). In contrast, when reducing the number of training samples, the performance gap between models trained on full training samples and those trained on 25% of the samples is as large as 12 percentage points (82% versus 70%).

These results offer significant insights into data-efficient wealth measurement. When at least 10 households are available per image, surveying more enumeration areas takes precedence over surveying additional households within the enumeration area for predicting wealth with our transformer model. Geospatial features, recognized as valuable auxiliary data for improving economic measurement $[21]$ , are widely used in wealth prediction. Here we design a conditioning module (see “Methods”) for our transformer model, enabling the efficient fusion of geospatial features and deep visual features. The results, as shown in Figure 1c, suggest that geospatial features significantly improve the

a  
![](images/01b7bf0abde2c749b6b71332b4be1ac2cebe8434a8e5bce5964ec3d17ff754ed.jpg)

b  
![](images/c475263d746e3ba3e9633cac83179673c25022ad0377ba46b2b9580bf9e34fe6.jpg)

![](images/8567aecfc2e04e4e0675ad3a92692bcdb018a4103f1553c7ca8fd3134b6f46b1.jpg)

![](images/347a5b879eb63d5bcbeddde3f85565f11c890eac972f8a2b055b541748fb8526.jpg)

![](images/391b3740e075972f42c3accee127956c7684392d9def804f21e43eabf34fa74a.jpg)

![](images/060ecb69f945ab8df0599a12ab7ebcd0b8c5a1b11527c137fd486abb8c0d8bcc.jpg)

![](images/9067da4510f020c22edf48c4d47fa23afd09224b94afbab472cbc988042c8f0f.jpg)

![](images/5f5b67c4dd22ed2165d174eea310b452982235d73df271ffea188068fc4ad812.jpg)

![](images/becc5fcecd2091247b1dbcbb8180f239f866f17bd87c13e500a3a42ffaa6a386.jpg)

![](images/f0b641db8035ae215f2ffdd8f2083ae2fadd4066a5705beb4af2de34f7889802.jpg)

![](images/fe7cbe90da9025ff5ccc645206e7dfa7aa7f78965737ddf0fcec2a513c48e9f5.jpg)

d  
![](images/9dd1a5f5fa99f8975138d2d2089667ae7e6f7a5b7b17494cd216c24c9fee49a0.jpg)

![](images/32dd4d222571540b0ab610f0fe28c67826b1997f2a9eef936a3755dd19cc9c8c.jpg)

![](images/c7a27a62e784c4b2777df0b6f1fb57f4bb210822d1d02daaf7c5cc4b052dd928.jpg)

![](images/d9ca19033152008abcf5d26db4dadcb88d4859877482e47eedc23f3dd7bb8a99.jpg)  
Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}$ values are not shown. Transformer results do not integrate geo-features and are trained using asset wealth constructed from all sample households. b. Performance comparison between Transformer models trained with asset wealth constructed from all households versus 10 households per administrative area. c. Performance comparison between Transformer models with and without integrating geospatial features. d. Scatterplot of survey-measured asset wealth against predicted wealth from the best-performing fold.

model performance across all countries, especially in Burkina Faso due to the lower effective sample size resulting from linking images to survey data at the commune level. Geospatial features appear particularly beneficial when the training sample size is smaller, indicating that the model can struggle to learn optimal visual representations from raw imagery at smaller sample sizes, at which point geospatial features serve as a valuable supplement for wealth prediction. Of the methods shown in Figure 1, the transformer model with geo-features shown in Figure 1c yields estimates with the highest $R^{2}$ in all cases except one, when training using the full census in Mozambique, for which the naive transformer model is slightly more accurate. The four gridded wealth maps in Figure 2, with a 4.8 km/pixel resolution, are generated solely using our transformer model and Landsat imagery. Without the need for geospatial feature preparation, the entire mapping process can be completed within an hour using 8 NVIDIA RTX A4000 GPUs. This means that our approach has great potential to accelerate granular wealth measurement at a national scale.

![](images/35dc913edfc7be77215a572d2626e4c7e26ea1bb9a366b1b6308e1f23a8583a0.jpg)

![](images/ccc1e3003776cb09ef191100238ecfb72777f593820fe71931b9dcc91b4863c3.jpg)  
Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018. d. Country-level wealth asset map for Burkina Faso in 2019. AWI values are generated from country-specific models and are therefore not comparable across countries.

## Performance on prediction of change in country-level wealth

We further evaluate country-level wealth change prediction for each country via fivefold cross-validation. Following $[29]$ , the CNN model uses concatenated bitemporal Landsat images along the channel dimension as input. Our transformer model processes each of the bitemporal images individually through a weight-sh

[中间内容因长度限制已省略]

icroestimates of wealth for all low-and middle-income countries. Proceedings of the National Academy of Sciences 119, e2113658119.

[9] Dang, H.A.H., Serajuddin, U., 2020. Tracking the sustainable development goals: Emerging measurement challenges and further reflections. World Development 127, 104570.

[10] Didan, K., 2021. Modis/terra vegetation indices 16-day l3 global 500m sin grid v061 [data set]. URL: https://doi.org/10.5067/MODIS/MOD13A1.061.accessed 2024-06-08.

[11] Elvidge, C.D., Baugh, K., Zhizhin, M., Hsu, F.C., Ghosh, T., 2017. Viirs night-time lights. International Journal of Remote Sensing 38, 5860–5879.

[12] Engstrom, R., Hersh, J., Newhouse, D., 2022. Poverty from space: Using high resolution satellite imagery for estimating economic well-being. The World Bank Economic Review 36, 382–412.

[13] Filmer, D., Pritchett, L.H., 2001. Estimating wealth effects without expenditure data—or tears: an application to educational enrollments in states of india. Demography 38, 115–132.

[14] Goldblum, M., Souri, H., Ni, R., Shu, M., Prabhu, V.U., Somepalli, G., Chattopadhyay, P., Ibrahim, M., Bardes, A., Hoffman, J., Chellappa, R., Wilson, A.G., Goldstein, T., 2023. Battle of the backbones: A large-scale comparison of pretrained models across computer vision tasks, in: Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track.

[15] Gong, P., Li, X., Wang, J., Bai, Y., Chen, B., Hu, T., Liu, X., Xu, B., Yang, J., Zhang, W., Zhou, Y., 2020. Annual maps of global artificial impervious area (gaia) between 1985 and 2018. Remote Sensing of Environment 236, 111510. URL: https://www.sciencedirect.com/science/article/pii/S0034425719305292, doi:https://doi.org/10.1016/j.rse.2019.111510.

[16] Hengl, T., Miller, M.A.E., Križan, J., Shepherd, K.D., Sila, A., Kilibarda, M., Antonijević, O., Glušica, L., Doğan, I., Shutcha, M.N., Leenaars, J.G.B., Wolf, J.W., van den Bosch, R., Kempen, B., de Jesus, J.M., Ribeiro, E., MacMillan, R.A., 2021. African soil properties and nutrients mapped at 30 m spatial resolution using two-scale ensemble machine learning. Scientific Reports 11, 6130. doi:10.1038/s41598-021-85639-y.

[17] Jean, N., Burke, M., Xie, M., Davis, W.M., Lobell, D.B., Ermon, S., 2016. Combining satellite imagery and machine learning to predict poverty. Science 353, 790–794.

[18] Linard, C., Gilbert, M., Snow, R.W., Noor, A.M., Tatem, A.J., 2012. Population distribution, settlement patterns and accessibility across africa in 2010. PLoS ONE 7, e31743. doi:10.1371/journal.pone.0031743.

[19] Liu, Z., Hu, H., Lin, Y., Yao, Z., Xie, Z., Wei, Y., Ning, J., Cao, Y., Zhang, Z., Dong, L., et al., 2022. Swin transformer v2: Scaling up capacity and resolution, in: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 12009–12019.

[20] Loshchilov, I., 2017. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101.

[21] Newhouse, D., 2024. Small area estimation of poverty and wealth using geospatial data: What have we learned so far? Calcutta Statistical Association Bulletin 76, 7–32.

[22] OpenCellid, 2024. Opencellid: The world's largest open database of cell towers. Accessed: 2024-06-08. URL: https://opencellid.org. data governed by Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

[23] Pettersson, M.B., Kakooei, M., Ortheden, J., Johansson, F.D., Daoud, A., 2023. Time series of satellite imagery improve deep learning estimates of neighborhood-level poverty in africa., in: IJCAI, pp. 6165–6173.

[24] Running, S., Zhao, M., 2021. Modis/aqua net primary production gap-filled yearly l4 global 500m sin grid v061 [data set]. URL: https://doi.org/10.5067/MODIS/MYD17A3HGF.061. accessed 2024-06-08.

[25] Sahn, D.E., Stifel, D., 2003. Exploring alternative measures of welfare in the absence of expenditure data. Review of income and wealth 49, 463–489

[26] Schiavina, M., Melchiorri, M., Pesaresi, M., 2023. Ghs-smod r2023a - ghs settlement layers, application of the degree of urbanisation methodology (stage i) to ghs-pop r2023a and ghs-built-s r2023a, multitemporal (1975-2030). URL: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA. [Dataset]

[27] Sirko, W., Kashubin, S., Ritter, M., Annkah, A., Bouchareb, Y.S.E., Dauphin, Y.N., Keysers, D., Neumann, M., Cissé, M., Quinn, J., 2021. Continental-scale building detection from high resolution satellite imagery. CoRR abs/2107.12283. URL: https://arxiv.org/abs/2107.12283, arXiv:2107.12283.

[28] WorldPop, School of Geography and Environmental Science, University of Southampton, Department of Geography and Geosciences, University of Louisville, Departement de Geographie, Universite de Namur, Center for International Earth Science Information Network (CIESIN), Columbia University, 2018. Global high resolution population denominators project - funded by the bill and melinda gates foundation (opp1134076). URL: https://dx.doi.org/10.5258/SOTON/WP00674. accessed: 2024-06-08.

[29] Yeh, C., Perez, A., Driscoll, A., Azzari, G., Tang, Z., Lobell, D., Ermon, S., Burke, M., 2020. Using publicly available satellite imagery and deep learning to understand economic well-being in africa. Nature communications 11, 2
"""
