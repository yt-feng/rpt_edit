你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

During the data construction process, we also need to account for data collection features that could impact trade policy dynamics unrelated to changes in policies. For example, as mentioned above, the GTA database allows for continuous updates of the data, with some measures added retroactively to the earlier years. If the stock of all measures at the end of the sample period was to be used directly, this may create a potential temporal bias as earlier periods would systematically contain more recorded measures due to more time being available for their discovery. To address this issue, we construct consecutive "as-of" data snapshots instead of using the complete dataset as of 2024. In addition, we implement a consistent 12-month discovery window—chosen based on GTA (2018) findings about peak discovery rates—for all observations. Under this approach, a measure is only included in our dataset if it was discovered within 12 months of its announcement date. For example, a measure announced in October 2022 is only included if it was discovered by October 2023. To implement this adjustment, we obtained precise discovery dates for each measure directly from the GTA team.

This approach enables us to compare trade-policy dynamics over time within a consistent discovery window. However, incomplete discovery periods still pose a challenge for accurately assessing the trends in the latest months and could result in systematic undercounting of measures at the end of the period. To address this issue, we exploit historical discovery patterns to calculate an adjustment for each calendar month, accounting for possible future discovery of measures. By calculating the average historical ratio of measures discovered within the 12-month reporting period after the time that has already elapsed, we can identify the proportion of measures likely to be discovered in the future. $^{15}$ This adjustment factor is then applied to the observed number of measures to account for incomplete discovery in the latest months. This approach leverages historical data to account for the truncated discovery windows to provide a more accurate representation of the likely trends in the latest period. $^{16}$

The new global indicator we have deve

[中间内容因长度限制已省略]

Trade and security: (Worldwide)</td><td>Weekly</td><td>Google Trends</td></tr></table>

Note: The table lists the time-series predictors used in the nowcasting model. All raw data are used from January 2010 to June 2025. All the keywords from Google Trends data listed above are \`topics' – besides "free trade", "free trade agreements", "customs regulations", "trade protectionism", "subsidies", and "trade agreements" – for which the platform reports the relative number of searches for that concept and all associated terms across different languages and expressions (rather than exact keyword matches in the search language).

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

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
