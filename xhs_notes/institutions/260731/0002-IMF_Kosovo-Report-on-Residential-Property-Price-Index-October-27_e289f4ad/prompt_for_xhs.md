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
## HIGH-LEVEL SUMMARY TECHNICAL ASSISTANCE REPORT

KOSOVO

Report on Residential Property Price Index (October 27–31, 2025)

November 2025

Prepared By

Barra Casey

## DISCLAIMER

The contents of this document constitute a high-level summary of technical advice provided by the staff of the International Monetary Fund (IMF) to the authorities of a member country or international agency (the "CD recipient") in response to their request for capacity development. Unless the CD recipient specifically objects within 30 business days of its transmittal, the IMF will publish this high-level summary on IMF.org (see Staff Operational Guidance on the Dissemination of Capacity Development Information).

2026 International Monetary Fund [HLS/26/043]

## High-Level Summary Technical Assistance Report Statistics Department

## Report on Residential Property Price Index (October 27–31, 2025) Prepared by Barra Casey

The High-Level Summary Technical Assistance Report series provides high-level summaries of the assistance provided to IMF capacity development recipients, describing the high-level objectives, findings, and recommendations.

ABSTRACT: This technical assistance mission, conducted from October 27 to 31, 2025, supported the Kosovo Agency of Statistics (KAS) in developing the country's first official Residential Property Price Index (RPPI). The mission focused on refining data cleaning and filtering processes, advancing compilation methods using the hedonic regression approach implemented in the R statistical package, and building local capacity for sustainable index production. The RPPI is critical for monitoring real estate market developments and financial sector risks, particularly for the Central Bank of Kosovo's (CBK) surveillance and stress testing frameworks. Key recommendations include launching the RPPI by end-2025, ensuring ongoing staff training and adequate resourcing, enhancing data quality through cross-checks, and establishing transparent dissemination practices with detailed methodological documentation.

JEL Classification Numbers (consult https://www.aeaweb.org/econlit/jelCodes.php)
Keywords: Residential Real Estate, Price Index, Financial Stability, Macroprudential Analysis

![](images/9711b398d2d3beb958e84a0d29d9d1921dace3a61e4d3791fbfb097aecbd1db7.jpg)

## Background

The technical assistance (TA) mission was part of an ongoing effort to support Kosovo in developing a reliable Residential Property Price Index (RPPI), a structural benchmark under the International Monetary Fund's (IMF) Stand-By Arrangement (SBA) and the Resilience and Sustainability Facility (RSF). The RPPI is essential for providing timely and accurate indicators of property market dynamics, which are crucial for macroeconomic surveillance, financial stability analysis, and policy formulation. Prior to this mission, Kosovo lacked an official government-published RPPI, limiting the authorities' ability to monitor real estate price trends and assess related financial risks.

This mission built upon previous engagements, including a June 2024 TA visit, by focusing on advanced methodological development and practical implementation. It assisted KAS in processing administrative data from the Kosovo Cadastral Agency (KCA), improving data quality, and applying a hedonic regression model with a rolling window approach to better capture pure price changes while controlling for property characteristics. The mission also emphasized capacity building to ensure that KAS staff could maintain and update the RPPI independently. The development of the RPPI aligns with the CBK's strategic priorities to strengthen financial sector risk monitoring and stress testing, thereby enhancing the overall macroprudential framework in Kosovo.

## Summary of Findings

The mission found that significant progress has been made toward establishing a robust RPPI for Kosovo, with KAS planning to publish the index for the reference quarter of Q2 2025. The administrative data from the Kosovo Cadastral Agency, spanning 2015 to mid-2025, was identified as the most suitable data source, although only records from 2018 onward were deemed reliable due to earlier quality issues. Despite improvements, concerns remain about potential underreporting of transaction prices, highlighting the need for cross-validation with alternative data sources such as real estate and construction company records.

Methodologically, the mission advanced the compilation of the RPPI by adopting a hedonic regression approach, which offers a more precise estimation of price changes by adjusting for property attributes like floor area, location, and floor number. The use of a four-quarter rolling window allowed the model coefficients to adapt over time, reflecting evolving market preferences. The RPPI was compiled at both the district level (Pristina and the rest of the country) and nationally, using annually updated expenditure weights to aggregate strata-level indices. The mission also supported the development of R scripts and Excel tools for index compilation, ensuring transparency and maintainability.

However, the sustainability of the RPPI production system remains a key risk, as the staff responsible have other duties and require ongoing training in regression techniques and the R statistical package. The mission emphasized the importance of regular data quality checks, timely feedback to the Cadastral Agency, and the establishment of internal procedures to maintain consistency and quality. Dissemination plans include launching the RPPI with a dedicated event, designing a new statistical release, publishing a detailed methods document, and making data easily accessible online.

## Summary of Recommendations

To ensure the RPPI's successful launch and sustainability, the mission recommended that KAS prioritize the design of a new statistical release and prepare comprehensive communication materials ahead of the planned publication in November or December 2025. This includes organizing a promotional event to raise awareness among media and users, thereby enhancing the index's visibility and utility. The publication of a detailed methods document is crucial to provide transparency about data sources, quality assurance procedures, and compilation methodologies, fostering user confidence and facilitating informed interpretation.

Capacity building is essential for maintaining the RPPI's quality over time. KAS should ensure that the staff assigned to the RPPI have adequate time and resources to focus on this task, supported by targeted training in regression-based statistical methods and proficiency with the R statistical package. The development of an internal procedures document will help institutionalize best practices and ensure continuity, especially as personnel changes occur. On the data front, KAS should implement regular quality checks on the quarterly data received from the Kosovo Cadastral Agency and establish mechanisms to promptly address any identified issues. Cross-checking declared prices with alternative sources remains a high priority to improve data reliability.

Finally, the hedonic regression models should be regularly monitored through diagnostic testing to maintain their explanatory power and relevance. Model updates should be carefully managed, ideally synchronized with annual weight revisions, and accompanied by a clear revision policy outlined in the methods document. These steps will support the RPPI's role as a vital tool for macroeconomic surveillance and financial stability monitoring in Kosovo.

Table 1. Country Priority Recommendations

<table><tr><td>Target Date</td><td>Priority Recommendation</td><td>Responsible Institutions</td></tr><tr><td>November 2025</td><td>Design a new statistical release to disseminate the RPPI</td><td>KAS</td></tr><tr><td>December 2025</td><td>Draft and publish an RPPI methods document.</td><td>KAS</td></tr><tr><td>December 2025</td><td>Launch the first-time RPPI at a promotion event for media and users.</td><td>KAS</td></tr></table>
"""
