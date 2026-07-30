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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
No. 2026-12 (July)

## Key Points

\- Human development inequality remains substantial across Asian economies, with inequality-related Human Development Index losses ranging from below 10% to over 35%.

\- Education and income inequalities are the largest contributors to inequality-related human development losses, particularly in South Asia, where both remain higher than in East Asia and the Pacific.

\- Gender equality is associated with lower human development losses, highlighting the importance of women's education, labor force participation, and empowerment.

\- Countries with stronger government effectiveness tend to experience lower levels of human development inequality, underscoring the role of institutional quality.

\- Regional comparisons show that South Asia faces substantially greater challenges than East Asia and the Pacific.

\- Reducing educational and income disparities, promoting gender-inclusive development, and strengthening governance should be central priorities.

# Explaining Human Development Inequality in Asia: Evidence and Policy

Deepak Kumar Behera, Lecturer, Economics and Finance Department, The Business School, RMIT University Viet Nam

Dil B. Rahul, Vice Chair of Research and Senior Research Economist, Asian Development Bank Institute (ADBI)

Thi Thu Tra Pham, Professor, Economics and Finance Department, The Business School, RMIT University Viet Nam

## 1. Background and Data

Asia has experienced remarkable progress in human development over recent decades, driven by improvements in health, education, and income. However, aggregate measures of development often conceal substantial inequalities within societies. To address this limitation, the Inequality-adjusted Human Development Index (IHDI) incorporates disparities in life expectancy, education, and income, providing a more comprehensive assessment of human development achievements. Studies have shown that inequality can substantially reduce effective human development outcomes, even in countries with relatively high levels of development (Grimm et al. 2010; Permanyer and Smits 2020).

The importance of addressing inequality has become increasingly evident in the global development agenda. According to the Human Development Report 2025, global human development progress has slowed markedly in recent years, highlighting the need for more inclusive and resilient development pathways (UNDP 2025). Within this context, understanding the sources and consequences of human development inequality has become a critical policy priority.

Beyond disparities in health, education, and income, gender inequality and institutional quality are increasingly recognized as important determinants of development outcomes. Gender inequalities in education, health, political representation, and labor market participation can constrain both individual opportunities and broader socioeconomic progress (Gaye et al. 2010; Klasen 2018). Similarly, effective governance plays a crucial role in delivering public services, promoting social inclusion, and ensuring that development gains are distributed more equitably across populations (Ferreira et al. 2022).

Against this backdrop, this policy brief examines the extent and drivers of human development inequality across Asian economies using data from the Human Development Report 2025. Particular attention is given to the roles of gender inequality and government effectiveness, together with regional differences between East Asia and the Pacific and South Asia. The analysis provides evidence-based insights to inform policies aimed at promoting more inclusive and equitable human development across the region.

This policy brief draws primarily on data from the Human Development Report 2025 database published by the United Nations Development Programme (UNDP 2025). The principal outcome measure is the percentage loss in the Human Development Index (HDI) due to inequality, which is derived by comparing the HDI with the Inequality-adjusted Human Development Index (IHDI). The IHDI adjusts the HDI for inequalities in the distribution of achievements in life expectancy, education, and income within each country, while the percentage loss in HDI quantifies the reduction in potential human development attributable to these inequalities. The analysis also uses the Human Inequality Coefficient and dimension-specific inequality measures for life expectancy, education, and income to identify the major sources of inequality-related losses in human development.

To examine broader institutional and social conditions associated with variations in human development inequality across countries, the analysis incorporates indicators from the Gender Inequality Index (GII), including reproductive health (maternal mortality ratio and adolescent birth rate), empowerment (female secondary educational attainment and women's representation in national parliaments), and labor market participation (female labor force participation). Institutional quality is measured using the Government Effectiveness indicator from the Worldwide Governance Indicators (WGI) database, which reflects perceptions of public service quality, policy implementation, civil service effectiveness, and the credibility of government policies. The analysis employs descriptive analysis, graphical comparisons, and regional benchmarking to examine patterns of human development inequality across Asian economies and their associations with gender inclusion and government effectiveness.

## 2. Patterns and Dimensions of Human Development Inequality

Human development inequality remains a significant challenge across Asian economies. Figure 1 reveals substantial cross-country variation in inequality-related losses in human development. HDI loss due to inequality ranges from 9.7% in Brunei Darussalam to 35.3% in Afghanistan, indicating that some countries forfeit more than one-third of their potential human development gains due to unequal outcomes in health, education, and income. High levels of HDI loss are also observed in Pakistan (33.1%), Bhutan (31.5%), India (30.7%), Nepal (29.7%), and Bangladesh (29.6%), whereas Singapore (13.0%), Malaysia (13.7%), Mongolia (13.4%), and Tonga (11.3%) record comparatively lower levels of human development inequality. A similar pattern is reflected in the Human Inequality Coefficient, suggesting that both indicators consistently capture disparities in the distribution of development achievements.

To better understand the sources of these inequalities, Figure 2 decomposes human development inequality into its three core dimensions: life expectancy, education, and income. The results reveal considerable variation across countries and dimensions. Education inequality is the most severe source of disparity across several economies, reaching 48.8% in Afghanistan, 48.2% in Bhutan, 44.9% in Timor-Leste, and 43.5% in Pakistan. Income inequality is also substantial, exceeding 35% in countries such as Palau (40.9%), India (37.4%), Sri Lanka (36.6%), Bangladesh (35.9%), and Cambodia (35.8%). In contrast, life expectancy inequality is generally lower, although Pakistan (26.0%), Afghanistan (25.2%), Kiribati (24.7%), and Timor-Leste (22.2%) continue to experience notable life expectancy disparities.

Overall, the evidence suggests that human development inequality in Asia is driven primarily by disparities in education and income rather than inequalities in life expectancy. Persistent inequalities in educational attainment and economic opportunities remain key constraints to inclusive human development (Grimm et al. 2010; Permanyer and Smits 2020). Addressing these disparities should therefore be a central policy priority across the region.

While Figures 1 and 2 examine inequalities in health, education, and income as constituent components of human development inequality, Figure 3 explores their association with the Gender Inequality Index (GII), a separate composite measure of gender disparities in reproductive health, empowerment, and labor market participation (Gaye et al. 2010). Although the two indices are conceptually related, they capture different dimensions of human development. A clear positive association is observed between the GII and HDI loss due to inequality, suggesting that countries with greater gender disparities also tend to experience larger inequality-related human development losses. Such an analysis aims to uncover how broader institutional and social environments are associated with human development inequalities across countries.

Figure 1: Human Development Inequality Across Asian Economies  
A. HDI Loss due to Inequality (%), 2023  
![](images/d16952c7bb46ee44ef1c64f64c6dd516fc917864fd645bf231aa39d970cdccc7.jpg)

B. Human Inequality Coefficient, 2023  
![](images/8fff4070a2f67497472e6101e9df7110bf9c29322b81655210292cde6f0e56ec.jpg)  
HDI = human development index, Lao PDR = Lao People's Democratic Republic; PRC = People's Republic of China.  
Note: Panel A presents HDI loss due to inequality (%), measuring the reduction in potential human development arising from unequal achievements in health, education, and income. Panel B reports the Human Inequality Coefficient, a composite measure summarizing inequality across these dimensions. Higher values in both panels indicate greater human development inequality.  
Source: Authors' calculations and illustration using data from UNDP (2025).

The upper-right quadrant ("high vulnerability") is dominated by countries such as Afghanistan, Pakistan, Bangladesh, Cambodia, and Papua New Guinea, which simultaneously exhibit relatively high gender inequality and substantial HDI losses. Afghanistan, for example, records the highest GII value (0.661) and the largest HDI loss (35.3%), highlighting how gender disparities may reinforce broader inequalities in health, education, and income.

In contrast, the lower-left quadrant ("strong performers") includes economies such as Singapore, the People's Republic of China (PRC), Malaysia, Brunei Darussalam, Thailand, and Viet Nam, which combine lower gender inequality with comparatively smaller human development losses. Singapore, which records the lowest GII value (0.031), also experiences a relatively low HDI loss (13.0%), illustrating the potential benefits of gender inclusion for equitable development outcomes.

Figure 2: Dimensions of Human Development Inequality Across Asian Economies  
A. Inequality in Life Expectancy, 2023  
![](images/9dd7ccb4fe43258b9ae3c1f841169b49eb149dfdafe7e94b6dfa40d8803a0a3b.jpg)

B. Inequality in Education, 2023  
![](images/5a4f6d2a2ad69c01a6681e581c5f302af6fbf44c84410b333326dd5c29467029.jpg)

C. Inequality in Income, 2023  
![](images/7f7ea4d73c392b4481d5f150bc738fa6b60774d316bd60a0707900144838ab1b.jpg)  
PRC = People's Republic of China.  
Note: Panel A reports inequality in life expectancy, Panel B presents inequality in education, and Panel C shows inequality in income across Asian economies. The indicators are derived from the inequality-adjusted Human Development Index (IHDI) framework and range from 0 to 100, where higher values indicate greater inequality within each dimension. Larger values, therefore, reflect wider disparities in health outcomes, educational attainment, and income distribution among individuals within a country.  
Source: Authors' calculations and illustration using data from UNDP (2025).

Figure 3: Gender Inequality and Human Development Inequality in Asia, 2023  
![](images/03c0fc0a3e2c255bde5c465c39123a136f36fc8b7effe6fc223495e1dcee0573.jpg)  
HDI = human development index, Lao PDR = Lao People's Democratic Republic, PRC = People's Republic of China.  
Note: Dashed lines represent the median values of the Gender Inequality Index (GII) and HDI loss due to inequality (%), a measure of human development inequality. The lower-left quadrant (“strong performers”) includes countries with relatively low gender and human development inequality, while the upper-right quadrant (“high vulnerability”) reflects countries facing high inequality in both gender and human development. The lower-right quadrant (“transitional economies”) represents countries with relatively high gender inequality but comparatively lower human development inequality, suggesting ongoing progress toward inclusive development. Conversely, the upper-left quadrant (“uneven development”) captures countries with lower gender inequality but relatively higher human development inequality, indicating that improvements in gender outcomes alone may not fully address broader socioeconomic disparities.  
Source: Authors' illustration.

Several economies, including Indonesia, Solomon Islands, Samoa, Tonga, and Vanuatu, fall within the “transitional economies” quadrant. These countries continue to experience relatively higher gender inequality but maintain comparatively moderate HDI losses, suggesting ongoing structural transitions and gradual progress toward more inclusive development. Meanwhile, the “uneven development” quadrant includes countries such as Bhutan and the Maldives, where relatively lower gender inequality coexists with comparatively high human development losses. This pattern indicates that improvements in gender outcomes alone may not be sufficient to address broader socioeconomic inequalities.

Figure 4 complements the gender perspective by examining the role of institutional quality. A generally negative association is observed between government effectiveness and HDI loss due to inequality, indicating that countries with stronger governance tend to experience lower levels of human development inequality.

The lower-right quadrant ("strong performers") includes economies such as Singapore, Brunei Darussalam,

Malaysia, PRC, Thailand, and Samoa, which combine relatively effective governance with comparatively low HDI losses. Singapore records the highest government effectiveness score (2.26) alongside a relatively low HDI loss (13.0%), demonstrating how effective institutions can contribute to more inclusive development outcomes.

In contrast, the upper-left quadrant ("high vulnerability") includes countries such as Afghanistan, Pakistan, Nepal, Bangladesh, Lao PDR, and Papua New Guinea, where weaker governance is accompanied by substantial development losses related to inequality. Afghanistan, which records the weakest government effectiveness score (-2.09), also experiences the highest HDI loss (35.3%), suggesting that institutional constraints may limit the capacity to deliver inclusive development outcomes.

The upper-right quadrant (“transitional governance”) includes countries such as Bhutan and India, which exhibit relatively stronger government effectiveness but continue to experience high human development losses. These cases indicate that governance improvements alone may not be sufficient to overcome entrenched socioeconomic disparities. Meanwhile, the lower-left quadrant (“uneven institutional development”) contains economies such as Mongolia, Tonga, Marshall Islands, and Tuvalu, where comparatively weaker governance coexists with moderate HDI losses. This suggests that factors beyond institutional quality, including demographic characteristics, social policies, and economic structures, may also influence human development outcomes.

Figure 4: Government Effectiveness and Human Development Inequality in Asia, 2023  
![](images/0515a67389d269ba0073150e47cf036c73663a78b88399aa80840e37f4f1ccbb.jpg)  
HDI = human development index, Lao PDR = Lao People's Democratic Republic, PRC = People's Republic of China.  
Note: Dashed lines represent the median values of the government effectiveness score and HDI loss due to inequality (%), a measure of human development inequality. The lower-right quadrant (“strong performers”) includes countries with relatively effective governance and lower human development inequality, whereas the upper-left quadrant (“high vulnerability”) includes countries with weaker governance and greater human development inequality. The upper-right quadrant (“transitional governance”) represents countries with relatively strong governance but still comparatively high levels of human development inequality, suggesting that institutional improvements have not yet fully translated into inclusive development outcomes. The lower-left quadrant (“uneven institutional development”) captures countries with weaker governance but relatively lower human development inequality, indicating that factors beyond governance may also influence development outcomes.  
Source: Authors' illustration.

Overall, the findings suggest that stronger government effectiveness and greater gender inclusion are associated with lower levels of human development inequality across Asian economies. Although the analysis is descriptive, the observed patterns highlight the potential importance of institutional quality and gender inclusion in promoting more equitable human development.

Regional comparisons reveal substantial disparities in human development inequality across Asia (Table 1). South Asia records considerably higher inequality-related HDI losses (30.2%) than East Asia and the Pacific (16.3%) and exceeds the global average (22.0%). A similar pattern is observed for the Human Inequality Coefficient, indicating that inequality remains a more significant constraint on development outcomes in South Asia.

The differences are particularly pronounced across the dimensions of inequality. Education inequality is more than three times higher in South Asia (36.9%) than in East Asia and the Pacific (11.8%), while income inequality (35.4% versus 27.9%) and life expectancy inequality (16.5% versus 7.8%) are also substantially higher. These patterns are consistent with the country-level evidence presented in Figures 1 and 2, highlighting education and income disparities as the principal drivers of inequality-related HDI losses.

Regional disparities are also evident in gender inclusion and governance. South Asia records a higher Gender Inequality Index (0.458) than East Asia and the Pacific (0.315), alongside weaker outcomes in reproductive health, female educational attainment, political representation, and labor force participation. Similarly, East Asia and the Pacific exhibit a positive average government effectiveness score (0.3), whereas South Asia records a negative score (-0.5), indicating weaker institutional capacity.

Table 1: Human Development Inequality, Gender, and Governance by Region, 2023

<table><tr><td>Country</td><td>East Asia and the Pacific</td><td>South Asia</td><td>World</td></tr><tr><td colspan="4">Human Development Inequality</td></tr><tr><td>Human developme

[中间内容因长度限制已省略]

n 2018; Carlsen 2020). Expanding female educational attainment, improving reproductive health outcomes, increasing women's labor force participation, and strengthening women's representation in decision-making institutions can therefore contribute to more inclusive development (Kabeer 2010; Duflo 2012). Such measures are particularly relevant for South Asia, where female educational attainment and labor force participation remain below regional and global averages.

The findings further suggest that stronger government effectiveness is associated with lower human development inequality. Effective institutions play a critical role in delivering education, health, and social protection services and ensuring that development benefits reach vulnerable populations. Evidence indicates that stronger governance can support both human development and the reduction of inequality (Ferreira et al. 2022). Governments should therefore focus on improving institutional capacity, strengthening accountability mechanisms, enhancing public service delivery, and increasing the effectiveness of social programs. Recent evidence also suggests that government effectiveness can directly reduce inequality and improve development outcomes (Barra et al. 2023).

Despite substantial progress in human development, significant inequalities persist across Asian economies. The evidence presented in this policy brief indicates that education and income disparities remain the primary drivers of inequality-related human development losses, while greater gender inclusion and stronger government effectiveness are consistently associated with more equitable human development outcomes. Regional comparisons further show that South Asia faces greater challenges than East Asia and the Pacific across multiple dimensions of inequality. Addressing these challenges requires integrated policy approaches that promote equitable access to education, advance gender equality, and strengthen institutional effectiveness. Future research could extend this analysis by examining trends over time, exploring subnational disparities, and investigating how government effectiveness is associated with specific dimensions of human development inequality, including inequalities in education, income, and life expectancy.

## AI Declaration

We declare that ChatGPT (OpenAI) was used only to improve language, including grammar, spelling, and reference formatting. No part of the analysis or original intellectual contribution was generated by the tool.

## References

Barra, C., A. Papaccio, and N. Ruggiero. 2023. Government Effectiveness and Inequality in Italian Regions. Economic Change and Restructuring. 56 (2). pp. 781–801.

Becker, G. S. 1993. Human Capital: A Theoretical and Empirical Analysis, with Special Reference to Education (3rd ed.). University of Chicago Press.

Carlsen, L. 2020. Gender Inequality and Development. Sustainability Science. 15 (3). pp. 759–780.

Duflo, E. 2012. Women Empowerment and Economic Development. Journal of Economic Literature. 50 (4). pp. 1051–1079.

Ferreira, I. A., R. M. Gisselquist, and F. Tarp. 2022. On the Impact of Inequality on Growth, Human Development, and Governance. International Studies Review. 24 (1), viab058.

Gaye, A., J. Klugman, M. Kovacevic, S. Twigg, and E. Zambrano. 2010. Measuring Key Disparities in Human Development: The Gender Inequality Index. Human Development Research Paper. United Nations Development Programme.

Grimm, M., K. Harttgen, S. Klasen, M. Misselhorn, T. Munzi, and T. Smeeding. 2010. Inequality in Human Development: An Empirical Assessment of 32 Countries. Social Indicators Research. 97 (2). pp. 191–211.

Kabeer, N. 2010. Women's Empowerment, Development Interventions and the Management of Information Flows. IDS Bulletin. 41 (6). pp. 105–113.

Klasen, S. 2018. The Impact of Gender Inequality on Economic Performance in Developing Countries. Annual Review of Resource Economics. 10 (1). pp. 279–298.

Lanzi, D. 2007. Capabilities, Human Capital and Education. Journal of Socio-Economics. 36 (3). pp. 424–435.

Machin, S. and A. Vignoles. 2004. Educational Inequality: The Widening Socioeconomic Gap. Fiscal Studies. 25 (2). pp. 107–128.

Permanyer, I. and J. Smits. 2020. Inequality in Human Development Across the Globe. Population and Development Review. 46 (3). pp. 583–601.

Sylwester, K. 2002. Can Education Expenditures Reduce Income Inequality? Economics of Education Review. 21 (1). pp. 43–52.

United Nations Development Programme (UNDP). 2025. Human Development Report 2025: A Matter of Choice: People and Possibilities in the Age of AI. UNDP.

## Asian Development Bank Institute

ADBI, located in Tokyo, is the think tank of the Asian Development Bank (ADB). Its mission is to identify effective development strategies and improve development management in ADB's developing member countries.

ADBI Policy Briefs are based on events organized or co-organized by ADBI. The series is designed to provide concise, nontechnical accounts of policy issues of topical interest, with a view to facilitating informed debate.

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of ADBI, ADB, or its Board or Governors or the governments they represent.

ADBI encourages printing or copying information exclusively for personal and noncommercial use with proper acknowledgment of ADBI. Users are restricted from reselling, redistributing, or creating derivative works for commercial purposes without the express, written consent of ADBI.

Asian Development Bank Institute
Kasumigaseki Building 8F
3-2-5 Kasumigaseki, Chiyoda-ku
Tokyo 100-6008
Japan
Tel: +813 3593 5500
www.adbi.org
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
