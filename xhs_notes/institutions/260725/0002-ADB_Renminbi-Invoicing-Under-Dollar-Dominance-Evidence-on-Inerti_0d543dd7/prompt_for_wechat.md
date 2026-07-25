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
ADBI Working Paper Series

RENMINBI INVOICING UNDER
DOLLAR DOMINANCE:
EVIDENCE ON INERTIA,
INSTITUTIONS, AND POLICY

Junko Shimizu and Katsuyuki Tomizawa

No. 1541

July 2026

Asian Development Bank Institute

Junko Shimizu is a professor in the Graduate School of Economics at Gakushuin University. Katsuyuki Tomizawa is a doctoral student in the Graduate School of Economics at Gakushuin University and a senior administrative officer at the Asian Development Bank Institute.

The views expressed in this paper are the views of the author and do not necessarily reflect the views or policies of ADBI, ADB, its Board of Directors, or the governments they represent. ADBI does not guarantee the accuracy of the data included in this paper and accepts no responsibility for any consequences of their use. Terminology used may not necessarily be consistent with ADB official terms.

Discussion papers are subject to formal revision and correction before they are finalized and considered published.

The Working Paper series is a continuation of the formerly named Discussion Paper series; the numbering of the papers continued without interruption or change. ADBI's working papers reflect initial ideas on a topic and are posted online for discussion. Some working papers may develop into other forms of publication.

The Asian Development refers to “China” as the People’s Republic of China and “Russia” as the Russian Federation.

The views expressed in this paper are solely those of the author and do not represent the official views of the Asian Development Bank Institute. Any errors are the sole responsibility of the author.

## Suggested citation:

Shimizu, J. and K. Tomizawa. 2026. Renminbi Invoicing Under Dollar Dominance: Evidence on Inertia, Institutions, and Policy. ADBI Working Paper 1541. Tokyo: Asian Development Bank Institute. Available: https://doi.org/10.56506/AUQZ9207

Please contact the authors for information about this paper.

Email: junko.shimizu@gakushuin.ac.jp, ktomizawa@adbi.org

Asian Development Bank Institute
Kasumigaseki Building, 8th Floor
3-2-5 Kasumigaseki, Chiyoda-ku
Tokyo 100-6008, Japan

Tel: +81-3-3593-5500

Fax: +81-3-3593-5571

URL: www.adbi.org

E-mail: info@adbi.org

ADBI Working Paper 1541

## Abstract

This paper examines the conditions under which renminbi invoicing has expanded despite the continued dominance of the United States (US) dollar in international trade. Using IMF trade invoicing data for 70 economies from 2016 to 2023, as reported by Boz et al. (2025), we show that RMB invoicing is systematically shaped by trade dependence on the People's Republic of China (PRC), exchange rate regimes, capital and foreign exchange controls, settlement infrastructure, and the strength of political and institutional ties with the PRC. While dollar-oriented exchange rate regimes and capital liberalization tend to restrict use of the renminbi, renminbi invoicing is expanding in economies with remaining controls and deeper integration into PRC-led financial, logistical, and digital networks, indicating that RMB internationalization is a gradual, complementary process rather than a substitute for the dollar.

Keywords: Dominant Currency Paradigm, internationalization of the renminbi, invoice currency, foreign exchange controls, logistics

JEL Classification: F23, F31, F33

## Contents

1. INTRODUCTION.... 1
2. RECENT RESEARCH ON INVOICE CURRENCY CHOICE.... 3
3. EXAMINATION AND ANALYSIS OF EXPLANATORY VARIABLES RELATED TO INVOICE CURRENCY CHOICE.... 8
3.1 Exchange Rates and Their Institutional Factors.... 8
3.2 Examination of Capital Market Factors.... 10
3.3 The PRC's Policies: Currency Swaps and Overseas Financial Institutions (Financial Infrastructure).... 16
3.4 Other PRC Government-Led Policies: Number of Visits by PRC Government Officials and Their Counterparts, and Other Related Policies .. 21
4. EMPIRICAL ANALYSIS OF FACTORS PROMOTING RMB-INVOICED TRANSACTIONS.... 29
4.1 Examination of Dependent Variables.... 29
4.2 Empirical Analysis Model.... 31
4.3 Empirical Analysis Results: Share of RMB-invoiced Imports.... 33
4.4 Empirical Analysis Results: Share of RMB-Invoiced Exports.... 35
4.5 Discussion.... 37
5. CONCLUSION AND FUTURE RESEARCH.... 39
REFERENCES.... 41

## 1. INTRODUCTION

Since the late 2010s, the environment surrounding currency choice in international trade and cross-border investment has been undergoing a major transformation. Although there has been no major change in the United States (US) dollar's dominant position in global trade, movements to reevaluate excessive reliance on the US dollar have become apparent in various countries against the backdrop of rising geopolitical and political-economic risks, such as the prolonged conflict between the US and the People's Republic of China (PRC), the normalization of financial sanctions triggered by the Russian invasion of Ukraine, and the recent resurgence of trade friction through tariff policies. Policy initiatives aimed at promoting so-called “local currency transactions”—where trade and investment are conducted either in the domestic currency or in that of the counterparty—are being advanced, primarily in emerging economies and Global South countries.

Rather than being seen as a radical challenge to the existing international monetary system, these moves should be understood through the lens of practical risk management and economic security. While US dollar invoicing still holds an overwhelming advantage in terms of liquidity, inertia, and network effects, it is also susceptible to political influence through sanctions and financial regulations. Particularly for countries that have faced the risk of restricted access to international payment infrastructure and major banking networks, currency diversification is increasingly seen not merely as a cost-cutting measure but as an institutional option for maintaining stable external transactions. From a geopolitical perspective, countries located far from the United States (most of which are emerging markets or developing nations) tend to use the US dollar as their invoicing currency and remain dependent on it, though data indicate that this dependence is decreasing in some major economies. Since 2021, the correlation between the use of invoicing currencies and geopolitical distance from the currency's issuing country has trended downward, suggesting that geopolitical fragmentation is progressing. Since the Russian invasion of Ukraine, the influence of geopolitical distance on the choice of invoicing currency has become pronounced. In countries far from the US and the eurozone, the use of the dollar and the euro has declined, with greater reliance on the renminbi, local currencies, and other third-country currencies. Conversely, in countries that have become more distant from the PRC, there has been a tendency to reduce the use of domestic and third-country currencies in favor of the US dollar. $^{1}$

Previous research, primarily conducted by the IMF, has empirically demonstrated the phenomenon known as the “Dominant Currency Paradigm” (DCP), in which the dominant position of the US dollar exerts a strong influence on corporate pricing and the adjustment of trade volumes. In recent years, however, attention has focused on the fact that, even as the DCP persists, the use of nondollar currencies is expanding in certain regions and sectors. The PRC’s efforts to internationalize the renminbi have steadily expanded its use in trade settlements and certain capital transactions through government-led institutional reforms, such as currency swap agreements, the establishment of clearing banks, and the development of the Cross-border Interbank Payment System (CIPS). Furthermore, in ASEAN countries, alongside the expansion of intraregional trade, the use of regional currencies is progressing through frameworks such as the Local Currency Settlement Framework (LCSF). In specific countries and regions, although their share in actual trade statistics remains small, the presence of currencies other than the US dollar is becoming clear.

Furthermore, as the world's largest energy importer, the PRC has promoted the use of the renminbi in transactions with resource-exporting countries, with an increasing number of renminbi settlements in oil and gas imports from suppliers such as the Russian Federation and Saudi Arabia. Such a shift in currency choice for resource and energy transactions—driven by developments such as the Russian invasion of Ukraine and the expansion of bilateral settlements in non-US dollar currencies—indicates that dedollarization is increasingly supported by transaction-based demand, particularly among emerging economies. The growth of local-currency invoicing, especially for import payments, underscores the importance of exchange rate risk allocation between exporters and importers and highlights the role of domestic factors, including exchange control regimes, financial market development, and external balance sheet structures, in shaping currency choice.

The purpose of this paper is to conduct an empirical analysis of the conditions under which renminbi-invoiced transactions expand, based on factors derived from a detailed examination of published statistics and institutional frameworks across various countries, primarily in Asia, as conducted by Tomizawa and Shimizu (2026). Tomizawa and Shimizu (2026), based on data published by governments and central banks in countries other than the PRC, noted that transactions denominated in local currencies and the renminbi have been increasing in countries such as Thailand and Brazil. They highlighted geopolitical factors that had not previously been identified in existing research as drivers of local currency use, the implementation of policies promoting such use, technological factors such as the movement of people and the spread of digital payments, and the construction of payment infrastructure—all of which may contribute to the expansion of renminbi usage. The contribution of this study lies in the fact that, by cross-referencing the mechanisms promoting local currency transactions and the results of factor analysis revealed through the analysis of local currency-denominated transactions in various countries and regions, we extracted new explanatory variable data from various statistics and publicly available information, constructed a dataset, and identified a new model using various “PRC policy factor” variables—which had not been employed in previous studies—as explanatory variables.

Furthermore, the finding of significance for many of these variables constitutes a key contribution of this study. Specifically, using the share of renminbi-denominated invoices in each country's exports, as published by Boz et al. (2025, IMF) as the dependent variable, and by attempting to quantify not only the factors indicating the internationalization of the renminbi used in previous studies but also new factors, we examine the roles played by factors such as currency and capital controls, financial infrastructure, and the formation of regional economic blocks. Through this, we aim to present a perspective that views the impact of recent changes in the global situation on the international monetary system not as a simple binary opposition of “dedollarization” but as a more multilayered, gradual structural change.

The structure of this paper is as follows. In Section 2, we summarize the key independent and dependent variables used in empirical analyses of currency choice and invoice currency in major prior studies, as well as the findings obtained. Next, in Section 3, we analyze phenomena that have not previously been identified as factors promoting local currency usage—specifically, those driving the increasing use of local currencies other than the US dollar—and attempt to quantify them as explanatory variables. Then, in Section 4, we conduct an empirical analysis using the share of the renminbi as the invoice currency in each country's exports and imports to the rest of the world as the dependent variable, and the new explanatory variables discussed in Section 2. Finally, in Section 5, we summarize our conclusions and future research directions in discussing the results.

## 2. RECENT RESEARCH ON INVOICE CURRENCY CHOICE

This section summarizes the main findings of recent research on currency choice and invoice currencies, including the Chinese renminbi, as well as the explanatory variables used in these analyses.

Boz et al. (2025, IMF) analyze invoicing–currency patterns in global trade and the impact of geopolitical factors (Table 1). Specifically, they conduct an empirical analysis using the share of invoicing currencies (USD, EUR, RMB) in each country's exports as the dependent variable, and the share of exports to the issuing countries of those currencies (the United States, the eurozone, and the PRC) as independent variables. Their main findings indicate that a limited number of currencies, including the US dollar and the euro, continue to dominate as invoicing currencies in global trade, and their shares remain stable even in the face of geopolitical factors. On the other hand, while the use of the renminbi has been steadily increasing since the early 2010s and expanding beyond Asia, its share remains relatively small.

Table 1: Boz et al. (IMF 2025)

<table><tr><td>Category</td><td>Contents</td></tr><tr><td>Dependent Variable</td><td>Share of invoice currencies in each country&#x27;s exports (USD/EUR/RMB)</td></tr><tr><td rowspan="6">Explanatory Variable</td><td>- Invoice currency share in the previous period (inertia)</td></tr><tr><td>- Ratio of exports to the country issuing the invoicing currency</td></tr><tr><td>- Ratio of exports to countries with currency pegs</td></tr><tr><td>- Homogeneity of exported goods (ratio of fuels, ores, and agricultural raw materials; ratio of petroleum)</td></tr><tr><td>- Bilateral exchange rates</td></tr><tr><td>- Geopolitical distance (from the US/EU/PRC) (UN voting distance)</td></tr><tr><td rowspan="4">Key Findings</td><td>- The USD remains globally dominant</td></tr><tr><td>- Use of the RMB is increasing but remains limited</td></tr><tr><td>- Geopolitical divisions (especially since 2021) have a strong influence on the choice of invoicing currency</td></tr><tr><td>- Countries with greater political distance from the US/EU are shifting toward the RMB and their own currencies</td></tr><tr><td># of sample</td><td>132 countries</td></tr><tr><td>Analysis period</td><td>1990–2023 (invoice currency share estimates are primarily for 1999–2023)</td></tr></table>

Summary by the author.

Furthermore, from a geopolitical perspective, countries located far from the United States (most of which are emerging markets or developing countries) tend to use the US dollar as the invoicing currency and remain dependent on it, while the study indicates that this dependence is decreasing in some major economies. Since 2021, the correlation between the use of invoicing currencies and the geopolitical distance from the currency's issuing country has trended downward, suggesting that geopolitical fragmentation is progressing. Since the Russian invasion of Ukraine, the influence of geopolitical distance on the choice of invoicing currency has become pronounced. In countries geographically distant from the United States and the eurozone, the use of the US dollar and the euro has declined, with a shift toward the Chinese yuan, domestic currencies, and third-country currencies. Conversely, countries that have become more distant from the PRC have tended to reduce their use of domestic and third-country currencies in favor of the US dollar.

In addition, the paper analyzes the relationship between the share of exports of resources and primary commodities. While commodities such as oil are still frequently traded in US dollars, and although transactions in renminbi and other currencies have increased recently, the paper states that no systematic evidence has been found to substantiate the effectiveness of policy initiatives aimed at reducing dependence on the US dollar in oil exports.

The paper provides a dataset covering 132 countries from 1990 to 2023, showing the share of invoicing currencies for exports and imports, specifically the US dollar, the euro, the renminbi, and other currencies (such as domestic currencies not listed above).

Perez-Saiz and Zhang (2023, IMF) analyze the use of the renminbi as an international currency, regional patterns, and the role of local-currency swaps and offshore renminbi clearing banks, both of which are implemented by the People's Bank of China. They note that while the global use of the renminbi is still in its early stages, accounting for only 2% of global settlements, there are significant regional differences in usage, with its use expanding particularly in Asia and certain emerging market economies (such as Mongolia, the Lao People's Democratic Republic, Chile, Türkiye, and Argentina). Furthermore, their empirical analysis confirms that local-currency swaps and renminbi clearing banks are effective in promoting the use of the renminbi in international settlements. Furthermore, the study noted that political distance (measured using the correlation of countries' voting patterns at the UN General Assembly to gauge political distance from the PRC) and geographical distance are also key factors influencing the use of the renminbi. In particular, it indicated that the renminbi is spreading across Asia and that its role as a regional currency is likely to expand further.

Table 2: Perez-Saiz and Zhang (2023, IMF)

<table><tr><td>Category</td><td>Contents</td></tr><tr><td>Dependent Variable</td><td>Share of the RMB in international settlements with PRC (SWIFT MT data)</td></tr><tr><td rowspan="7">Explanatory Variable</td><td>- RMB usage in the previous period (inertia)</td></tr><tr><td>- Swap lines (dummy)</td></tr><tr><td>- Presence of RMB clearing banks (dummy)</td></tr><tr><td>- Trade integration with PRC (import-export ratio)</td></tr><tr><td>- Geographical distance (capital–PRC)</td></tr><tr><td>- Political distance (UN voting distance)</td></tr><tr><td>- Other (GDP, income, financial deepening, inflation, etc.)</td></tr><tr><td rowspan="4">Key Findings</td><td>- The effect of swap lines alone is unclear</td></tr><tr><td>- Countries with deep trade ties to PRC expand RMB usage</td></tr><tr><td>- Clearing banks contribute to promoting the use of RMB settlements</td></tr><tr><td>- Political and geographical distance are also important factors</td></tr><tr><td># of sample</td><td>Not explicitly stated in the document (using SWIFT dat

[中间内容因长度限制已省略]

y-in-global-trade-49574 (accessed 21 March, 2026).

Brüggen, A., G. Georgiadis, and A. Mehl. 2025. Global Trade Invoicing Patterns: New Insights and the Influence of Geopolitics published as part of The International Role of the Euro, June 2025.ECB. https://www.ecb.europa.eu/press/other-publications/ire/article/html/ecb.ireart202506\_02\~a8e66f5ea3.en.html (accessed 21 March, 2026).

Casas, C., F. J. Díez, G. Gopinath, and P. Gourinchas. 2017. Dominant Currency Paradigm: A New Models for Small Open Economies. IMF Working Paper, WP/17/264.

Chinn, M.D. and H. Ito. 2008. A New Measure of Financial Openness, Journal of Comparative Policy Analysis, Volume 10, Issue 3 (September): 309–22.

Georgiadis, G., H. Le Mezo, A. Mehl, and C. Tille. 2021. Fundamentals vs. Policies: Can the US Dollar's Dominance in Global Trade be Dented? ECB Working Paper series no.2574. https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2574\~664b8e9249.en.pdf (accessed 21 March, 2026).

Goldberg, L., and C. Tille. 2008. Vehicle-currency Use in International Trade. Journal of International Economics 76: 177–192. Gopinath, G. 2015. The International Price System. In Jackson Hole Symposium, volume 27. Federal Reserve Bank of Kansas City.

Gopinath, G., E., Boz, C. Casas, F. J. Díez, P. Gourinchas, and M. Plagborg-Møller. 2016. Dominant Currency Paradigm. NBER Working Paper 22943. http://www.nber.org/papers/w22943 (accessed 21 March, 2026).

Ilzetzki, E., C. M. Reinhart, and K. Rogoff. 2021. Rethinking Exchange Rate Regimes. NBER Working Paper 29347. Data for Ilzetzki, Reinhart, and Rogoff (2019, 2021) Revised: November 2021. Ito, H., and M. Chinn. 2014. The Rise of the Redback and the Peoples Republic of China's Capital Account Liberalization: An Empirical Analysis of the Determinants of Invoicing Currencies. ADBI Working Paper 473.

Ito, T., S. Koibuchi, K. Sato, and J. Shimizu. 2018. Managing Currency Risk: How Japanese Firms Choose Invoicing Currency. Edward Elgar (ISBN: 9781785360121).

Japan External Trade Organization (JETRO). 2025. Overview of Cross-Border E-Commerce in China and Key Considerations for Exporting to China （中国における越境 EC の概要と留意点：中国向け輸出。）Trade and Investment Consultation Q&A. (in Japanese) https://www.jetro.go.jp/world/qa/J-210602.html (accessed 21 March 2026).

Kamps, A. 2006. The Euro as Invoicing Currency in International Trade, Working Paper, No.665, European Central Bank.

Novy, D. 2006. Hedge Your Costs: Exchange Rate Risk and Endogenous Currency Invoicing. Warwick Economic Research Paper No. 765, University of Warwick.

Peng, P. 2025. The Impact of RMB Settlement on China's Cross-Border E-Commerce Imports and Exports. Design Engineering and Creative Industry. 9(8): 86–90. https://doi.org/10.47297/wspdecWSP2515-797315.20250908 (accessed 21 March 2026).

Perez-Saiz, H., and L. Zhang. 2023. Renminbi Usage in Cross-Border Payments: Regional Patterns and the Role of Swap Lines and Offshore Clearing Banks. IMF Working Paper WP/23/77. https://www.imf.org/en/Publications/WP/Issues/2023/03/31/Renminbi-Usage-in-Cross-Border-Payments-Regional-Patterns-and-the-Role-of-Swaps-Lines-and-531684 (accessed 21 March, 2026).

Perez-Saiz, H., L. Zhang, and R. Iyer. 2023. Currency Usage for Cross-Border Payments. IMF Working Paper, WP/23/72. https://www.imf.org/en/Publications/WP/Issues/2023/03/24/Currency-Usage-for-Cross-Border-Payments-531324 (accessed 21 March, 2026).

Papke, L., and Wooldridge, J. 1996. ‘Econometric Methods for Fractional Response Variables with an Application to 401(K) Plan Participation Rates’, Journal of Applied Econometrics 11(6), 619–632.

Renminbi ASEAN. 2021. Report on the Use of the Renminbi in ASEAN Countries. Compiled by the Guangxi Financial Society (December 2021).

RMB Internationalization Report 2025. The People's Bank of China.
https://www.pbc.gov.cn/en/3688241/3688636/3828468/5624529/2025123116494089198/2025123116480428858.pdf (accessed 21 March, 2026).

Shimizu, J., T. Ito, K. Sato, T. Yoshimi, and U. Yoshimoto. 2022. Currency Selection for Trade Invoicing by Japanese Firms: Insights from Country-by-Country Invoice Currency Shares Based on Aggregated Customs Data. (日本企業の貿易建値通貨選択—税関データを集計した各国別インボイス通貨シェアからわかること—). PRI Discussion Paper Series No. 22A-04. Tokyo: Policy Research Institute, Ministry of Finance. (in Japanese) https://www.mof.go.jp/pri/research/discussion\_paper/ron348.pdf (accessed 21 March 2026).

Shimizu, J., K. Sato, T. Ito, Y. Yoshida, T. Yoshimi, and . Yoshimoto. 2024., Invoice Currency Choice and its Determinants in Japanese Trade: New Evidence from Japanese Customs Data. (税関申告データから何がわかるのか? —インボイス通貨選択と為替レートのパススルー—). PRI Discussion Paper 24A-02. (in Japanese) https://www.mof.go.jp/pri/publication/financial\_review/fr\_list8/r160/r160\_2.pdf (accessed 21 March 2026).

Tomizawa, K. 2020. Financial Cooperation between China and ASEAN. (中国とASEANの金融協力). PRI ASEAN Workshop Material, 4 November. (in Japanese) https://www.mof.go.jp/pri/research/conference/fy2020/asean2020\_01\_02.pdf (accessed 21 March 2026).

——. 2023. Prospects and Challenges for Local Currency Transactions in Asia (アジアにおける現地通貨建て取引の展望と課題): Cross-Border Transactions and Settlements in Local Currencies, Direct Exchange Markets, and the Impact of Changes in the Funding and Settlement Environment on Currency Selection. Institute for Fiscal and Monetary Policy Research Paper (July 7, 2023; revised June 6, 2025) PRI Research Paper No. 23-RP-04. Tokyo. (in Japanese) https://www.mof.go.jp/pri/publication/research\_paper\_staff\_report/research16.pdf (accessed 21 March 2026).

Tomizawa, K., and J. Shimizu. 2026. Outlook and Challenges for Local Currency Transactions – An Analysis of the Trend Toward De-Dollarization, Centered on Asia. Mimeo.
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
