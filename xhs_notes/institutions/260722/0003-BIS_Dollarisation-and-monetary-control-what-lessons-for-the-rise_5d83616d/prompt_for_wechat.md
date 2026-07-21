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
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/70849613b0fb8324f25b4a6fa886b244bd6c84d2d295b046062372f462c1bec5.jpg)

## BIS Working Papers No 1370

Dollarisation and monetary control: what lessons for the rise of stablecoins?

by Boris Hofmann, Aaron Mehrotra and Jan Paulick

Monetary and Economic Department

July 2026

JEL classification: E44, E58, F32, F38, G15, G23

Keywords: dollarisation, capital flows, stablecoins, monetary control, EMDEs

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# Dollarisation and monetary control: what lessons for the rise of stablecoins?\*

Boris Hofmann, $^{\dagger}$ Aaron Mehrotra, and Jan Paulick

Bank for International Settlements

This version: 30 June 2026

## Abstract

The emergence of stablecoins has created a new channel to access US dollar liquidity in emerging market and developing economies (EMDEs), similar to the historical role of foreign-currency deposits, or “deposit dollarisation”. This has raised concerns about the possible implications for monetary control in EMDEs. Drawing on data on foreign currency deposits and dollar-pegged stablecoin inflows for more than 130 economies, we compare the dynamics and drivers of “stablecoin dollarisation” with those of conventional deposit dollarisation. We document that historical deposit dollarisation and recent stablecoin flows are both associated with similar macro-financial drivers, including the strength of exchange rate pass-through and sovereign or banking crises. We further document significant persistence in both deposit and stablecoin dollarisation, suggesting that dollarisation is hard to reverse once established. Unlike deposit dollarisation, stablecoin flows seem to be largely unaffected by either broad or specific capital flow restrictions. This likely occurs because stablecoins are partly circulating outside the regulatory perimeter. The historical record also suggests that moderate deposit dollarisation has been associated with somewhat higher inflation risks, although there is little evidence of significant impacts on monetary policy transmission.

JEL codes: E44, E58, F32, F38, G15, G23.

Keywords: dollarisation, capital flows, stablecoins, monetary control, EMDEs.

## 1 Introduction

Stablecoins, a type of cryptoasset designed to maintain a stable value relative to a reference currency—most commonly the US dollar—have risen sharply in prominence in recent years. Since 2023, their market capitalisation has nearly tripled, driven almost exclusively by the two major US dollar-denominated coins (Graph 1). Some projections suggest stablecoin market capitalisation could rise further in the coming years, potentially positioning them as a significant factor in the global financial system. $^{1}$

Several factors could drive wider stablecoin adoption. One is their use as a settlement asset in the crypto ecosystem. But more importantly for our paper, they also offer easy access to foreign currencies for residents in emerging market and developing economies (EMDEs), particularly to the US dollar. The use of stablecoins as a store of value (and potentially as a means of payment) could counteract recent de-dollarisation tendencies in some EMDEs; in others, it could further entrench existing dollarisation.

![](images/1eb89bf1babb8449bcfcb504fa968641962dcfd2802b3166197635d76746cc23.jpg)  
Graph 1. Stablecoin market capitalisation

Note: Total market capitalisation of stablecoins, in billions of US dollars. Source: Kosse et al. (2023); CoinGecko; authors' calculations.

The use of stablecoins in EMDEs is reminiscent of the widespread reliance of many of these economies on foreign-currency deposits as a store of value, often referred to as "deposit dollarisation". $^{2}$ A number of EMDEs continue to feature significant deposit dollarisation today, and there are clear parallels between conventional dollarisation and the newer phenomenon of "stablecoin dollarisation". At the same time, dollarisation through stablecoins may bring about new challenges. Their ease of access, essentially just requiring a device with internet access, makes them attractive as instruments to gain exposure to foreign currency. Du et al. (2026) show that stablecoin-implied FX rates reflect a sizeable stablecoin access premium driven by the strong demand for dollar exposure in emerging market economies. Operating within borderless, decentralised networks, stablecoins offer use cases in payments and settlements. At the same time, these features make stablecoins harder to track and regulate than traditional dollar deposits. This could increase risks for users and raise challenges for policymakers. $^{3}$

These parallels and contrasts motivate a structured comparison. The historical experience of deposit dollarisation offers decades of cross-country evidence on what drives dollarisation, how persistent it is, and what it implies for monetary control. To the extent that similar forces are at work in the case of stablecoins, that evidence provides a useful benchmark; to the extent that they differ, the comparison helps isolate new dynamics and policy implications.

In this paper, we draw on historical data on dollar deposits going back to the 1990s and novel data on stablecoin flows in recent years to assess the parallels between the two forms of dollarisation. Our analysis yields four main findings.

First, there are important similarities between the drivers of deposit and stablecoin dollarisation. A higher exchange rate pass-through—associated with the portfolio motive of financial dollarisation—and economic or financial crises are both associated with higher deposit dollarisation and greater USD-pegged stablecoin flows. A noteworthy difference is the particular relevance of banking crises for higher stablecoin flows, consistent with the notion that the non-bank nature of stablecoins becomes more attractive if there has been instability in the banking sector.

Second, both deposit dollarisation and stablecoin dollarisation are highly persistent, implying that it is hard to reverse dollarisation once established. At the same time, we find only limited evidence of substitution between dollar deposits and stablecoins, suggesting that the growing demand for US dollar stablecoins in EMDEs largely does not stem from existing US dollar deposits, and vice versa. This could hint that the two markets are segmented to some degree. While the motives of demand for dollar deposits and stablecoins are similar, the economic agents behind these two types of transactions may be different to some extent, for example tech savvy users turning to stablecoins.

Third, FX-related restrictions including prudential regulation and capital controls appear to have little effect on stablecoin dollarisation. While restrictions on accounts and cross-border capital flow restrictions generally reduce deposit dollarisation, neither the latter nor specific restrictions on stablecoin use between residents and non-residents seem to have a statistically significant effect on gross stablecoin inflows.

Fourth, deposit dollarisation has some, albeit generally contained, effects on monetary control. Using an inflation-at-risk framework, we show that the consequences of deposit dollarisation for inflation are non-monotonic: low dollarisation is not significantly associated with inflation risks, moderate dollarisation tends to coincide with somewhat higher inflation across the inflation forecast distribution and highly dollarised economies appear to import monetary-policy credibility. At the same time, interacting monetary policy shocks with the degree of deposit dollarisation does not indicate significant effects of deposit dollarisation on the overall transmission of monetary policy.

The remainder of the paper is structured as follows. This section ends with a review of the relevant literature. Section 2 presents the data. In Section 3, we re-assess the drivers of deposit dollarisation and compare them with early evidence on the drivers of cross-border stablecoin flows. In Section 4, we assess the persistence of deposit dollarisation as an indicator of the lock-in risk from a dollarisation surge. This is followed in Section 5 by an analysis about the impact of regulatory restrictions on dollarisation. In Section 6, we focus on evidence for Latin America and the Caribbean, where the existence of higher frequency data allows us to analyse the dynamic interaction between dollar deposits and stablecoin flows as substitutes or complements, and the role of regional restrictions. In Section 7, we zoom in on the implications of financial dollarisation for monetary control, assessing the effects on inflation control and monetary transmission. Section 8 concludes.

## Literature review

Our paper stands at the intersection of three main strands of literature: the long-standing literature on the causes and implications of dollarisation in EMDEs, the more recent literature on the economic consequences of stablecoins and the literature on macro-financial stability frameworks in EMDEs.

The extensive literature on dollarisation reflects the historical relevance of the phenomenon going back to the 1970s. As highlighted by Levy-Yeyati (2006, 2021), there are different forms of dollarisation. There is official (or de jure) dollarisation when foreign currency gains legal tender status, while unofficial (or de facto) dollarisation refers to situations of parallel use of a local and foreign currency in an economy. In the latter case, there is in turn the distinction between real dollarisation, when foreign currency is used as means of payment or unit of account, and financial dollarisation, when foreign currency is used for borrowing and store of value. Previous literature on deposit dollarisation has highlighted both its macroeconomic and institutional drivers (see eg Honohan and Shi (2001); Reinhart et al. (2014); Levy-Yeyati (2006)). A number of policy papers have also explored the implications of dollarisation for monetary policy (see eg Bennett et al. (1999); Reinhart et al. (2014)). Our paper contributes to this literature in three ways. First, we revisit and expand the assessment of the drivers of deposit dollarisation and provide new evidence on the implications for monetary control. Second, we provide a comparative analysis of the factors driving deposit dollarisation and the use of stablecoins in EMDEs. Third, focusing on data for Latin America and the Caribbean, we analyse the interaction between deposit dollarisation and stablecoin dollarisation. In this respect, a closely related study is Auer et al. (2025), who analyse the factors driving cross-border stablecoin flows, considering a set of macro factors in sending and receiving countries. We complement this study by focusing on factors that help predict future flows and by investigating the possible interplay between deposit and stablecoin dollarisation.

The literature on the macroeconomic implications of stablecoins, to which our paper contributes, is still nascent. $^{4}$ A first strand of this literature studies how stablecoins affect bank balance sheets and credit supply. The key mechanism is that stablecoins compete with bank deposits and thereby weaken the liquidity premium traditionally enjoyed by banks. Recent empirical evidence by Altavilla et al. (2026) shows that stablecoin adoption induces substitution away from retail deposits and increases banks' reliance on wholesale funding. On the theoretical side, Huang and Keister (2026) develop a banking model with stablecoins to analyse credit supply, while Bindseil (2026) discusses the balance-sheet implications of stablecoins. A second strand of the stablecoin literature studies how inflows into stablecoins affect government financing costs. Since stablecoin issuers hold a substantial share of their assets in short-term government securities, inflows into stablecoins can raise demand for safe public debt and compress sovereign yields. Ahmed and Aldasoro (2025) and Cerutti et al. (2026) provide empirical evidence that inflows into dollar-backed stablecoins lower short-term U.S. Treasury bill yields. $^{5}$ A third strand emphasises the international dimension of stablecoins. Because stablecoins can be held and used across borders, their macroeconomic effects depend not only on domestic adoption but also on foreign demand. Azzimonti and Quadrini (2025) show that stablecoins can reshape global demand for dollar reserve assets and increase equilibrium demand for U.S. Treasury bills. Similarly, Minesso and Siena (2026) develop a multi-country model in which foreign households hold stablecoins backed by U.S. treasuries, thereby compressing sovereign yields. Conceptually, this mechanism is related to the broader literature on global safe-asset demand and to work on deposit dollarisation in emerging markets. Hofmann et al. (2026) develop a quantitative macroeconomic model bringing all the different channels together to assess the overall macroeconomic implications from the perspective of the stablecoin issuing economy. Aldasoro, Beltrán, and Grinberg (2026) analyse how inflows into foreign currency denominated stablecoins create spillovers between crypto and conventional FX markets, while Du et al. (2026) study the cost differences between cross-border payments made through banks, fintechs and stablecoins. Aldasoro, Frost, and Ito (2026) examine the various implications of stablecoin use for the international monetary and financial system. Our paper contributes to this literature by assessing the implications of stablecoins from the perspective of EMDEs holding foreign currency denominated stablecoins.

Finally, the paper also contributes to the literature on macro-financial stability frameworks in EMEs. Rey (2013) prominently highlighted that financial globalization has transformed the classical trilemma into a dilemma, so that monetary control can only be reestablished through the active management of capital flows. In this vein, Jeanne and Korinek (2010), Bianchi (2011), Farhi and Werning (2014), Benigno et al. (2015), Korinek and Sandri (2016) and Bruno et al. (2017) demonstrate how macroprudential and capital flow management measures can be effective in enhancing macro-financial stability. We contribute to this literature by assessing the implications of stablecoins for EMDEs and the challenges they may pose for these economies' macro-financial stability frameworks.

## 2 Data

The analysis draws on cross-country data on deposit dollarisation as well as data on cross-border stablecoin flows as the main outcome variables.

## Dollar deposits

For dollar deposits, we use both annual data for the broad global sample and quarterly data for a smaller group of Latin American countries.

Annual data on deposit dollarisation - defined as the ratio of foreign-currency deposits to total deposits - are obtained from Levy-Yeyati (2021). They cover more than 130 economies over 1990 to 2019. Despite substantial changes in the macroeconomic environment, especially the longer-term global decline in inflation, the cross-country distribution of deposit dollarisation has been remarkably stable. Graph 2 plots the cross-country distribution of deposit dollarisation in 1990, 2000, 2010 and 2019. In each year the median sits in a narrow band around 0.2 to 0.3, the interquartile range stretches from roughly 0.05 to 0.5, and the upper whisker reaches close to 1, indicating that some economies are fully dollarised. Economies that are fully dollarised are those where the US dollar acts as official legal tender. The 1990 distribution is somewhat more compressed at the top, with a maximum nearer to 0.85, but from 2000 onwards the picture is essentially unchanged.

![](images/4649c10b4154cabd97131943825525cc5060d58111f25c03dcee274719220232.jpg)  
Graph 2. Distribution of deposit dollarisation by year

Note: Boxes show medians and interquartile (IQR) ranges; whiskers show the 25th/75th percentiles plus or minus 1.5 times the IQR. Source: Levy-Yeyati (2021) and authors' calculations.

To leverage recent and higher-frequency (quarterly) data available for a sub-sample of Latin American countries, we use data on foreign-currency deposits from the Inter-American Development Bank. Dollarisation is a longstanding, yet a heterogeneous feature of Latin American financial systems. Several regional economies are fully dollarised (eg Panama, Ecuador and El Salvador), while others exhibit partial dollarisation with significant shares of bank deposits denominated in US dollars (eg Argentina, Bolivia and Peru). $^{6}$

Graph 3 plots the median and the interquartile range of the foreign currency deposit ratio for the Latin American countries over the period 1990-2024. The chart shows that deposit dollarisation across Latin America is heterogeneous and relatively volatile. Specifically, over the last two decades, the median deposit dollarisation ratio dropped from around 40% to roughly 20%. However, data availability is not stable in the earlier years.

![](images/1977263558db37164080017f46e38242455240e300ef0454c21c1d2a81b884a8.jpg)  
Graph 3. Distribution of deposit dollarisation in Latin America over time, quarterly data

Note: The figure illustrates the cross-country distribution, where the line represents the median and the shaded band indicates the interquartile range. The sample of countries is not consistent over time due to data availability. Source: Inter-American Development Bank and authors' calculations.

## Cross-border stablecoin flows

As a measure of stablecoin use and adoption, we rely on cross-border stablecoin flows. As stablecoin transfers lack country attribution, a first step derives inter-entity flows based on address-entity associations and transfers in blockchain networks. In a second step, stablecoin flows are allocated pro rata to countries based on web-traffic distribution of the respective transacting entities, primarily major crypto exchanges. We employ gross inflows on a country basis. We use gross rather than net flows - the latter tend to be small, as stablecoin inflows and outflows are highly correlated. $^{7}$ Gross inflows on a country level are also more likely correlated with overall adoption and thus

[中间内容因长度限制已省略]

.1$ . Dependent variable: cumulative stablecoin inflows to GDP, 2017 to 2024. Explanatory variables refer to 2016 or longer-run averages; see text for details. Source: authors' estimates based on Auer et al. (2025) and Chainalysis data; explanatory variables as in Table A1.

## B Additional tables

Table B3. Inflation at risk and low deposit dollarisation (first decile)

<table><tr><td>VARIABLES</td><td>5% q. $\pi_{t+1}$ </td><td>25% q. $\pi_{t+1}$ </td><td>50% q. $\pi_{t+1}$ </td><td>75% q. $\pi_{t+1}$ </td><td>95% q. $\pi_{t+1}$ </td></tr><tr><td> $\pi_t$ </td><td>-0.0242(0.0842)</td><td>0.283***(0.0641)</td><td>0.495***(0.0686)</td><td>0.742***(0.0818)</td><td>1.349***(0.174)</td></tr><tr><td> $y_t^{\text{gap}}$ </td><td>0.0392(0.0907)</td><td>0.135**(0.0540)</td><td>0.201***(0.0719)</td><td>0.278***(0.105)</td><td>0.468*(0.269)</td></tr><tr><td> $\Delta exc_t$ </td><td>0.00602(0.0385)</td><td>-0.0152(0.0396)</td><td>-0.0299(0.0496)</td><td>-0.0471(0.0639)</td><td>-0.0891(0.137)</td></tr><tr><td>SovDebtCrisist</td><td>4.185(2.716)</td><td>4.062***(1.361)</td><td>3.977*(2.034)</td><td>3.878(3.674)</td><td>3.634(7.586)</td></tr><tr><td>CurrencyCrisist</td><td>3.863(4.622)</td><td>10.17***(2.139)</td><td>14.54***(2.547)</td><td>19.62***(5.162)</td><td>32.10***(11.80)</td></tr><tr><td>BankingCrisist</td><td>3.140(3.571)</td><td>0.888(2.563)</td><td>-0.668(2.115)</td><td>-2.481(2.622)</td><td>-6.933(5.266)</td></tr><tr><td>Dollar 1st decilet</td><td>-0.688(2.552)</td><td>-0.297(2.035)</td><td>-0.0261(1.929)</td><td>0.289(2.388)</td><td>1.063(3.177)</td></tr><tr><td>Type of economies</td><td>EMDEs</td><td>EMDEs</td><td>EMDEs</td><td>EMDEs</td><td>EMDEs</td></tr><tr><td>Observations</td><td>2,108</td><td>2,108</td><td>2,108</td><td>2,108</td><td>2,108</td></tr></table>

Note: Bootstrapped standard errors in parentheses; $*\*\*$ $p < 0.01$ , $*\*$ $p < 0.05$ , $*$ $p < 0.1$ . Dependent variable: one-year-ahead inflation ( $\pi_{t+1}$ ). Source: authors' estimates following Machado and Santos Silva (2019); inflation-at-risk framework as in Banerjee et al. (2024).

Table B4. Inflation at risk and moderate deposit dollarisation (second quartile)

<table><tr><td>VARIABLES</td><td>5% q. $\pi_{t+1}$ </td><td>25% q. $\pi_{t+1}$ </td><td>50% q. $\pi_{t+1}$ </td><td>75% q. $\pi_{t+1}$ </td><td>95% q. $\pi_{t+1}$ </td></tr><tr><td> $\pi_t$ </td><td>-0.0345(0.0942)</td><td>0.286***(0.0647)</td><td>0.495***(0.0729)</td><td>0.740***(0.0827)</td><td>1.322***(0.191)</td></tr><tr><td> $y_t^{\text{gap}}$ </td><td>0.0352(0.0827)</td><td>0.136***(0.0526)</td><td>0.202***(0.0769)</td><td>0.279***(0.0996)</td><td>0.462(0.290)</td></tr><tr><td> $\Delta exc_t$ </td><td>0.00632(0.0465)</td><td>-0.0151(0.0315)</td><td>-0.0291(0.0513)</td><td>-0.0455(0.0716)</td><td>-0.0844(0.132)</td></tr><tr><td> $SovDebtCrisis_t$ </td><td>3.997(2.794)</td><td>3.882***(1.485)</td><td>3.807**(1.611)</td><td>3.719(3.542)</td><td>3.510(8.059)</td></tr><tr><td> $CurrencyCrisis_t$ </td><td>3.634(5.032)</td><td>10.29***(2.001)</td><td>14.64***(2.777)</td><td>19.74***(4.775)</td><td>31.83**(12.51)</td></tr><tr><td> $BankingCrisis_t$ </td><td>2.972(3.760)</td><td>0.832(2.495)</td><td>-0.569(2.225)</td><td>-2.209(2.633)</td><td>-6.098(5.212)</td></tr><tr><td> $Dollar\ 2nd\ quartile_t$ </td><td>1.881(1.610)</td><td>2.035**(0.904)</td><td>2.136***(0.822)</td><td>2.255**(1.074)</td><td>2.535(2.823)</td></tr><tr><td>Observations</td><td>2,108</td><td>2,108</td><td>2,108</td><td>2,108</td><td>2,108</td></tr></table>

Note: Bootstrapped standard errors in parentheses; \*\*\* $p < 0.01$ , \*\* $p < 0.05$ , \* $p < 0.1$ . Specification identical to Table B3 except that the dollarisation dummy refers to the second quartile of the deposit-dollarisation distribution. Source: authors' estimates following Machado and Santos Silva (2019); inflation-at-risk framework as in Banerjee et al. (2024).

Table B5. Inflation at risk and high deposit dollarisation (fourth quartile)

<table><tr><td>VARIABLES</td><td>5% q. $\pi_{t+1}$ </td><td>25% q. $\pi_{t+1}$ </td><td>50% q. $\pi_{t+1}$ </td><td>75% q. $\pi_{t+1}$ </td><td>95% q. $\pi_{t+1}$ </td></tr><tr><td> $\pi_t$ </td><td>-0.0179(0.0835)</td><td>0.286***(0.0638)</td><td>0.494***(0.0707)</td><td>0.741***(0.0908)</td><td>1.360***(0.181)</td></tr><tr><td> $y_t^{\text{gap}}$ </td><td>0.0522(0.0795)</td><td>0.140***(0.0515)</td><td>0.200***(0.0732)</td><td>0.272**(0.124)</td><td>0.451*(0.252)</td></tr><tr><td> $\Delta exc_t$ </td><td>0.00106(0.0355)</td><td>-0.0185(0.0415)</td><td>-0.0320(0.0378)</td><td>-0.0480(0.0641)</td><td>-0.0880(0.127)</td></tr><tr><td> $\text{SovDebtCrisis}_t$ </td><td>4.012(2.591)</td><td>3.911***(1.324)</td><td>3.843*(1.964)</td><td>3.761(4.081)</td><td>3.557(8.913)</td></tr><tr><td> $\text{CurrencyCrisis}_t$ </td><td>4.246(3.906)</td><td>10.41***(1.916)</td><td>14.65***(2.305)</td><td>19.67***(4.988)</td><td>32.25***(11.30)</td></tr><tr><td> $BankingCrisis_t$ </td><td>3.407(3.322)</td><td>0.892(2.346)</td><td>-0.836(2.318)</td><td>-2.883(2.510)</td><td>-8.011(6.563)</td></tr><tr><td> $Dollar\ 4th\ quartile_t$ </td><td>0.238(1.595)</td><td>-1.893*(1.147)</td><td>-3.357**(1.564)</td><td>-5.093***(1.718)</td><td>-9.439***(2.974)</td></tr><tr><td>Observations</td><td>2,108</td><td>2,108</td><td>2,108</td><td>2,108</td><td>2,108</td></tr></table>

Note: Bootstrapped standard errors in parentheses; \*\*\* $p < 0.01$ , \*\* $p < 0.05$ , \* $p < 0.1$ . Specification identical to Table B3 except that the dollarisation dummy refers to the fourth quartile of the deposit-dollarisation distribution. Source: authors' estimates following Machado and Santos Silva (2019); inflation-at-risk framework as in Banerjee et al. (2024).
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
