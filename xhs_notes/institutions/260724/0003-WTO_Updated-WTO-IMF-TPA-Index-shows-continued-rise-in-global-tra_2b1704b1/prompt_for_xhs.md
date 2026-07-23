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
# MEASURING GLOBAL TRADE POLICY ACTIVITY $^{1}$

Samuele Centorrino (IMF)
Antonia Diakantoni (WTO)
Alexander Keck (WTO)
Michele Ruta (IMF)
Monika Sztajerowska (IMF)
Yuting Wei (Bocconi University)

This draft: 1 October 2025

## Abstract

This paper introduces the Trade Policy Activity (TPA) Index, a novel indicator measuring evolving global trade policy dynamics since the Global Financial Crisis. Using a Dynamic Factor Model on comprehensive trade policy data covering 197 countries and territories, we document a structural shift around 2019 with a substantial expansion in the use of trade policies. The TPA Index also identifies cyclical episodes of heightened activity and reveals interconnections between different types of measures. We are also able to identify systematic differences in trade policy deployment among groups of economies. Additionally, we employ MIDAS (Mixed Data Sampling) regressions with high-frequency data to develop nowcasting capabilities for trade policy activity, enabling real-time identification of potential policy shifts. These results contribute to the trade policy measurement literature and offer a tool for monitoring global trade policy developments in real time.

JEL codes: F13, C32, C38, C53
Keywords: Trade policy, Dynamic factor models, Nowcasting

## 1 INTRODUCTION

Global trade policy is changing rapidly, with economies adopting various tariff and non-tariff measures that can significantly affect global trade and economic growth (IMF, 2025; WTO, 2025). In this environment, accurate and timely data on global trade policy dynamics is increasingly important for both policy and economic analysis. While there are several initiatives aimed at monitoring changes in trade and trade-related policies globally, notably by the WTO through its Trade Monitoring Database and the IMF in collaboration with the Global Trade Alert, what is currently missing is an indicator that is able to efficiently extract coherent insights from the plethora of information on measures and different policy tools (e.g. tariffs, quantitative restrictions, subsidies) across a large number of countries and products, thus capturing global trade-policy dynamics in a timely and overarching fashion. In this paper, we aim to fill this knowledge gap.

Our approach relies on detailed trade policy information starting from the Global Financial Crisis for up to 197 countries and territories and seeks to develop a novel indicator that tracks global trade policy over time and enables real-time monitoring of trade policy developments. The underlying data draws from two monitoring exercises – the WTO's Trade Monitoring Database (TMDB) and the Global Trade Alert (GTA). They track information on tariffs, other import and export restrictions, trade remedies, customs-related procedures, trade-related investment measures, subsidies and other trade-related policies, allowing for a comprehensive view of trade policy dynamics. They also differ in their methodological approaches and verification methods, making them complementary for the purposes of this exercise. For example, TMDB relies mainly on official government sources and undergoes extensive verification to track implemented measures while GTA also scouts news outlets for policy announcements.

Based on this broad set of information, we apply a Dynamic Factor Model (DFM) to extract a common factor across diverse trade policy measures and capture overall policy dynamics – i.e. overall trade policy activity. We also accommodate idiosyncratic variation in different types of measures through a block structure and identify patterns specific to each category (clearly trade-facilitating versus all other measures). We also distinguish by groups of countries, notably G20 and non-G20. Importantly, the model incorporates both nonlinear deterministic trends and stationary factors to distinguish between long-term structural shifts and cyclical components in the use of trade policy. By adapting this established macroeconomic modeling framework to high-frequency trade policy data in an innovative manner, our approach offers an advancement in the tracking of overall policy activity globally and over time.

The resulting Trade-Policy Activity (TPA) Index reveals several key insights about the evolution of trade policy since the Global Financial Crisis. First, after remaining flat for over a decade, the index shows a marked increase around 2019 with a continued upward trajectory, which corresponds to the COVID-19 pandemic and the increased use of trade policy for trade and non-trade objectives—a trend that was later reinforced by the war in Ukraine, enduring trade tensions and rising geopolitical risks. Second, in addition to this long-term structural shift, the index captures distinct cyclical patterns. Specifically, we observe temporal peaks during specific events, with notable spikes coinciding with escalating U.S.-China tariffs (2018-2019), the onset of the COVID-19 pandemic (2020), and the war in Ukraine (2022). Third, the index demonstrates that clearly trade-facilitating and all other types of measures often move in tandem, reflecting the fact that many economies use trade policy to adjust to external shocks and related trade policies by others. $^{2}$ Fourth, accounting for the different economic size of economies adopting trade policy measures reveals both differences in long-term trends, with G20 economies being on a more persistent upward path, and differences in the relative importance of specific policy peaks, with e.g. U.S.-China 2018-19 tariffs not substantially impacting trade policy dynamics in non-G20 economies.

Our results remain robust to several additional tests, including alternative specifications and approaches to extracting the underlying trend, possible compositional effects or consideration of alternative time periods. For example, inclusion of additional policies beyond the core scope of trade policy, such as FDI policies or capital flow restrictions, or consideration of additional trade-policy intensity measures (such as the number of implementing countries) do not significantly alter the results. Similarly, the exclusion of subsidies from the estimation does not impact the overall dynamics, and results also remain robust to considering alternative cut-off periods used for the estimation.

This exercise contributes to three broad strands of literature. First, it contributes to the literature measuring trade policy. Following the theoretical foundations established by Anderson and Neary (2005), Kee, Nicita and Olarreaga (2009) developed country-level indicators of trade policy restrictiveness across numerous economies. $^{3}$ These indicators have the merit of providing a theory-consistent measure of trade restrictions imposed at and behind the border, but they rely on data available with significant time lags, making them unsuitable for regular monitoring. $^{4}$ They also do not take into account dynamics in facilitating trade policy measures. Other exercises aiming to provide more up-to-date indicators of trade policy also either capture partial aspects of trade policy, do not identify common dynamics, or face temporal limitations. $^{5}$ We address these constraints by developing a parsimonious global indicator of trade policy that i) exploits a DFM to extract common dynamics at monthly frequency, ii) enables timely monitoring in rapidly evolving environments and iii) provides an alternative to existing partial or low-frequency measures of trade policy changes at the global level.

Second, we extend the application of Dynamic Factor Models to the domain of trade policy analysis. While DFMs have been widely applied in macroeconomic forecasting and business cycle analysis (Forni et al., 2000; Giannone et al., 2008, 2010), their use in identifying common trade policy dynamics represents a novel application. Specifically, we build on earlier approaches that control for idiosyncrasies in particular subgroups of series through a block structure (e.g., Bańbura et al., 2011; Bok et al., 2018; Bańbura et al., 2023), adapting this framework to distinguish between trade-facilitating and other measures. We additionally introduce new elements to account for both structural and cyclical components of trade policy dynamics, allowing us to disentangle persistent policy shifts from temporary fluctuations. This methodological innovation addresses an important challenge in the trade policy literature—the need to synthesize diverse policy instruments into a coherent, timely indicator while preserving their distinct characteristics. $^{6}$

Finally, we contribute to the rapidly expanding literature on geoeconomic fragmentation (e.g., Aiyar et al., 2023, 2024; Fernandez-Villaverde et al., 2024; Gopinath et al., 2024) by offering a distinct methodological focus. By specifically examining trade policy in its different forms, we measure the magnitude and direction of trade policy changes rather than broader geoeconomic fragmentation or geopolitical tensions. $^{7}$ This approach provides a more precise measurement of trade policies based on actual changes, complementing broader indices that capturegeopolitical tensions or uncertainty. As such, our index offers granular insights into the concrete manifestations of trade policy evolution, also enabling a deeper understanding of how specific trade measures evolve over time. Furthermore, by incorporating related uncertainty indices and relevant textual information into the nowcasting of our TPA index, we are able to produce more timely updates of the indicators and account for trade policy uncertainty and broader measures of trade policy expectations. $^{8}$ Our methodology also distinctively incorporates both trade-facilitating and other measures, enabling analysis of policy dynamics associated with their potential co-movement patterns documented in previous research (Giordani et al., 2016; Ederington and Ruta, 2016; Egger et al. 2022; Evenett et al., 2022). $^{9}$

The rest of the paper is structured as follows. Section 2 provides a brief overview of the data used for the construction of the input indicators. Section 3 outlines the methodology used. Section 4 presents the results and introduces our new Trade Policy Activity (TPA) Index. Section 5 presents the results of a series of robustness checks. Section 6 describes the data and methodology for the nowcasting of the TPA and Section 7 concludes.

## 2 DATA

## Data Sources

To construct a new global indicator of trade-policy activity, we require timely and accurate data on different types of trade-policy measures for a large sample of countries. We rely on two main data sources that have such characteristics and are key references for monitoring trade policy developments, namely the WTO Trade Monitoring Database (TMDB) and the Global Trade Alert (GTA) database. The TMDB database, created in October 2008, has been tracking trade policy measures implemented by WTO Members and Observers through formal WTO channels, i.e., communications by the governments and records by the WTO Secretariat, based on publicly available official sources, including government websites, other international organizations' websites or press releases (WTO, 2024). The GTA database, developed by the University of St. Gallen, compiles announced and implemented measures from a variety of publicly available sources, including press articles (GTA, 2022). Both databases were created in the aftermath of the Global Financial Crisis to help monitor trade policy measures adopted by governments and provide complementary trade policy information.

Both databases include information on a wide array of trade-related policy measures. The TMDB includes data on import and export restrictions (such as tariffs, quantitative restrictions and other taxes), trade remedies (i.e., anti-dumping, countervailing and safeguard measures), customs-related procedures, trade-related investment measures (such as local content requirements) and other trade measures. The GTA database covers an even wider range of measures that can affect trade, including subsidies, such as financial and in-kind grants, state loans or state aid, which have been used to monitor industrial policies (e.g., Evenett et al., 2024) and other measures that may potentially affect cross-border commercial flows. $^{10}$ For the purpose of constructing a new trade-policy indicator, only trade-policy related measures are considered (see Table A1.1 in the Annex for the list of all the measures captured in each database and those included in the baseline). $^{11}$ Combining the information from both data sources allows us to cover a wider and more timely set of policies that may affect trade and develop a single trade-policy indicator that captures the multi-faceted nature of policy changes. In addition, given that certain trade-policy measures may be under- or over-represented in a particular data source, combining them can help correct for potential idiosyncratic biases of each database.

There are several reasons as to why both databases may differ in the coverage of trade policy developments and capture different, yet complementary, dynamics. First, the scope of the type of trade-policy measures covered differs, with GTA tracking a broader set than TMDB (such as subsidies) $^{12}$ as well as measures applied to specific firms, and those adopted by subnational bodies. As such, TMDB covers changes in policy measures most directly associated with trade policy and affecting the economy as a whole (i.e., national measures applied broadly). Second, while TMDB relies mainly on official government sources and undergoes extensive verification processes, its mandate is narrower compared to that of GTA, which additionally scouts unofficial news outlets. As such, TMDB benefits from an additional layer of quality control, ensuring precise coverage of different measures across countries as stipulated by their respective laws. Meanwhile, GTA benefits from additional sources independent of government notifications or review but may also be influenced by transparency of the governmental process of notifying the public about new measures (as they rely on public announcements by the authorities). Third, while TMDB records implemented measures only, GTA also includes policy announcements, potentially providing early signals of possible policy action. Fourth, TMDB data is released twice a year (with new measures for a given period being added subsequently), while GTA data includes ongoing updates with measures being added as they are discovered over time. $^{13}$ Overall, the strength of TMDB is accuracy and quality control as it provides data on effectively implemented measures of a traditionally trade-related scope, as communicated and verified by governments. In comparison, the strength of GTA is that it tracks a broader array of measures, including in areas outside of traditional trade policy, that are announced publicly (but not necessarily implemented) and close-to-real-time updates. As such, these two sources capture different number of measures and dynamics over time (see Annex 1) and, when combined, may help better capture the overall dynamics in global trade policy.

For these reasons, in the exercise envisioned in this paper, the two databases will be complementary in terms measures covered and provide additional information on policy dynamics. More specifically, this paper aims to extract meaningful information from each data source by capturing the common dynamics through estimation of a global factor using a dynamic factor model (see the next section).

## Data Construction

To generate input variables used in the model, we first calculate the total count of new trade-policy measures introduced globally and the average number of products affected by those measures in a given month and year, by type, and data source (see Table A1.2 in the Annex for the list of variables). $^{14}$ The former set of variables (total counts) allow us to capture the extensive margin of the trade policy activity while the latter (average number of products) further gauge the extent of their application. In the robustness checks, we also test if our results hold when including a wider set of variables accounting for measures' reach, such as the number of implementing countries, or, alternatively, retaining the total counts of measures only (Section 5).

During the data construction process, we also need to account for data collection features that could impact trade policy dynamics unrelated to changes in policies. For example, as mentioned above, the GTA database allows for continuous updates of the data, with some measures added retroactively to the earlier years. If the stock of all measures at the end of the sample period was to be used directly, this may create a potential temporal bias as earlier periods would systematically contain more recorded measures due to more time being available for their discovery. To address this issue, we construct consecutive "as-of" data snapshots instead of using the complete dataset as of 2024. In addition, we implement a consistent 12-month discovery window—chosen based on GTA (2018) findings about peak dis

[中间内容因长度限制已省略]

form reports the relative number of searches for that concept and all associated terms across different languages and expressions (rather than exact keyword matches in the search language).

## Google Trend Data

This study uses Google Trends data to capture the weekly search intensity for a predefined set of keywords, covering the period from January, 2010, to June 2025. The data are downloaded directly from the Google Trends platform (https://trends.google.com/trends) at a weekly frequency.

When a keyword is entered as a topic (e.g., "Tariff"), the platform reports the relative number of searches for that concept, including all associated terms across different languages and expressions, rather than exact keyword matches in the search language. This ensures that conceptually related queries — such as "tariff policy," "tariff pause," or searches in non-English languages — are captured under a unified measure. In this sense, searching by topic effectively consolidates a wide range of related keyword searches into a single measure.

The values reported by Google Trends are normalized on a scale from 0 to 100, where 100 represents the peak popularity of a term within the selected time and region. As a result, these figures do not reflect absolute search volumes but rather relative keyword popularity at a particular time. Given that our goal is to use these time series to nowcast constructed indicators, after downloading the data for the keywords, we normalize them through a within-series scaling. Specifically, following the approach in Choi and Varian (2012), we compute growth rates of the normalized Google Trends index to emphasize short-term fluctuations and enhance comparability across predictors. In the future, further checks could be undertaken to ensure that the inherent characteristics of the Google Trends data are adequately handled for purposes of prediction, buildings on the recommendations from the literature (e.g., Cebrián and Domenech, 2024).

Table A4.1 Nowcast RMSE by Single High-Frequency Predictor

<table><tr><td>Predictor (Worldwide)</td><td>RMSE</td></tr><tr><td>Globalization</td><td>27.9048</td></tr><tr><td>Trade liberalization</td><td>28.3407</td></tr><tr><td>Market access</td><td>28.4866</td></tr><tr><td>Trade barriers</td><td>29.0178</td></tr><tr><td>Free trade</td><td>29.2971</td></tr><tr><td>Customs regulations</td><td>29.5086</td></tr><tr><td>Free trade agreements</td><td>29.5544</td></tr><tr><td>Trade restriction</td><td>29.7732</td></tr><tr><td>Trade and security</td><td>29.9103</td></tr><tr><td>Trade war</td><td>30.1914</td></tr><tr><td>Trade protectionism</td><td>30.1000</td></tr><tr><td>Tariff</td><td>30.5798</td></tr><tr><td>Subsidies</td><td>30.6543</td></tr><tr><td>Trade agreements</td><td>30.8250</td></tr><tr><td>Import duties</td><td>31.2695</td></tr><tr><td>Export controls</td><td>31.5042</td></tr><tr><td>World Trade Organization</td><td>32.2878</td></tr></table>

Note: Each root mean squared error (RMSE) value is obtained from a nowcasting model that includes only one high-frequency predictor at a time. The RMSE values are reported on a 0–100 scale for comparability. For each predictor, we estimate a restricted ADL-MIDAS model using the corresponding column from the predictor matrix, with the autoregressive component fixed at AR(1). The RMSE is computed based on out-of-sample predictions. This table facilitates relative performance comparison across predictors, where lower values indicate better nowcasting accuracy.

## Figure A4.1 Nowcasting Stationary Component of TPA

![](images/595dbb9b3d31b30ce8527fd15568c8f4f43822c1144ae4c91c972e0f773eec7d.jpg)  
Note: The nowcasting result plotted in Figure A4.1 corresponds to the nowcasted stationary target with leads in Equation 2 with h = 1. From April 2019 to May 2025, the nowcasted values are shown as a red dashed line with dots (referred to as one-step predictions). The green dotted line (referred to as AR(1) predictions) represents a simple AR(1) forecast used for comparison.

Table A4.2 Nowcast RMSE by Number of Predictors (K)

<table><tr><td>Number of Predictors (K)</td><td>Normalized RMSE (RMSE(AR(1)) = 1)</td></tr><tr><td>1</td><td>0.953573</td></tr><tr><td>2</td><td>0.903596</td></tr><tr><td>3</td><td>0.872285</td></tr><tr><td>4</td><td>0.875684</td></tr><tr><td>5</td><td>0.959054</td></tr><tr><td>6</td><td>0.962986</td></tr><tr><td>7</td><td>0.993655</td></tr><tr><td>8</td><td>0.989964</td></tr><tr><td>9</td><td>0.997955</td></tr><tr><td>10</td><td>1.014154</td></tr><tr><td>11</td><td>1.038936</td></tr><tr><td>12</td><td>1.168822</td></tr><tr><td>13</td><td>1.220326</td></tr><tr><td>14</td><td>1.318528</td></tr><tr><td>15</td><td>1.323343</td></tr><tr><td>16</td><td>1.332687</td></tr><tr><td>17</td><td>1.315322</td></tr></table>

Note: The RMSE values are computed from out-of-sample forecasts using a rolling-window ADL-MIDAS regression. For each specification, we include K high-frequency predictors and all other low frequency predictors. The RMSE is calculated over the same evaluation period to ensure comparability across different values of K. We observe that ADL-MIDAS with less than 10 best-performing predictors have a better performance compared with AR(1) which has absolute RMSE at 27.07.
"""
