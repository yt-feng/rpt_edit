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
# The Coming Great Repression?

# New Measures and a Century of Evidence

Marijn A. Bolhuis, Jakree Koosakul, Neil Shenai, and Jie Yang

WP/26/160

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/b036de4cd972fad134554acf926e56706ebcada71adbe159f1772ce34c6bbadc.jpg)

# IMF Working Paper Strategy, Policy & Review

The Coming Great Repression? New Measures and a Century of Evidence Prepared by Marijn A. Bolhuis, Jakree Koosakul, Neil Shenai, and Jie Yang\*

Authorized for distribution by Martin Kaufman
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Governments have historically used financial repression to reduce debt and fiscal pressures, yet few systematic measures of repression exist. To fill this gap, we introduce two quantity-based repression indicators grounded in a structural portfolio-choice model, exploiting the gap in government-bond demand between captive and non-captive investors. A narrow fiscal indicator captures pressure on banks to hold government bonds. A consolidated measure adds the perimeter of central bank liabilities. Applying our measures to a novel dataset of 17 advanced economies since 1920, we find that financial repression has been a persistent feature of modern history, peaking after World War II, receding during the capital account liberalization era, and rising again after the Global Financial Crisis. Our measures correlate with conditions typically associated with repression—such as high debt burdens and restricted capital mobility—along with crowding out of private investment and credit. Using a debt decomposition framework, we show that repression was a major driver of debt reduction after World War II, generating larger fiscal savings than traditional seigniorage, and has again generated fiscal savings since the Global Financial Crisis. With the conditions historically associated with elevated repression present today, our evidence suggests that financial repression may see increased use going forward.

RECOMMENDED CITATION: Bolhuis, Marijn A., Jakree Koosakul, Neil Shenai, and Jie Yang (2026), “The Coming Great Repression? New Measures and a Century of Evidence.” IMF Working Paper 26/160.

<table><tr><td>JEL Classification Numbers:</td><td>E63; E58; H63; N10; N20</td></tr><tr><td>Keywords:</td><td>financial repression; sovereign debt dynamics; captive markets; banks&#x27; sovereign holdings</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>mbolhuis@imf.org, jkoosakul@imf.org, nshenai@imf.org, jyang5@imf.org</td></tr></table>

WORKING PAPERS

# The Coming Great Repression? New Measures and a Century of Evidence

Prepared by Marijn A. Bolhuis, Jakree Koosakul, Neil Shenai, and Jie Yang

## Contents

Glossary of Acronyms 2   
1. Introduction 3   
2. Concepts, Data, and Stylized Facts 9   
3. Theoretical Framework 21   
4. Estimates and Correlates of Financial Repression 26   
5. Financial Repression in Sovereign Debt Dynamics 32   
6. Conclusions 46   
Annex 51   
References 63

## Glossary of Acronyms

AE Advanced Economy

AR(n) Auto-regressive by order n

BIS Bank for International Settlements

CBDC Central Bank Digital Currency

FR Financial Repression

GFC Global Financial Crisis (2007–2009)

GDP Gross Domestic Product

GMD Global Macro Database (Müller-Plantenberg et al., 2024)

JST Jordà–Schularick–Taylor Macrohistory Database (Jordà et al., 2017)

LCR Liquidity Coverage Ratio

PFIMH Public Finances in Modern History (Mauro et al., 2013)

QE Quantitative Easing

UIP Uncovered Interest Rate Parity

WID World Inequality Database

WWI World War I (1914–1918)

WWII World War II (1939–1945)

## 1. Introduction

Fiscal outlooks in many advanced economies have become increasingly challenging, with public debt at high peacetime levels. $^{1}$ Standard approaches to restoring fiscal space, such as fiscal consolidation and growth-enhancing reforms, remain central to countries' debt-reduction strategies, yet they can be slow to deliver results and politically difficult to sustain. Fiscal consolidation can have limited effects on debt ratios if not well-timed (International Monetary Fund, 2023a), while polarization can hamper the formation of enabling coalitions that support fiscal adjustment (Alesina et al., 1998; Cottarelli et al., 2017). Structural reforms face related constraints, as they can impose near-term costs on concentrated interests while generating diffuse benefits over time horizons beyond typical political cycles (Campos et al., 2025; Furceri et al., 2024).

Historically, advanced economies have resorted to less orthodox channels to reduce debt burdens. One such channel is surprise inflation, which reduces the real value of nominal claims on the government when inflation exceeds what was originally priced into nominal securities at issuance (Eichengreen and Esteves, 2022; Hilscher et al., 2021). $^{2}$ A second channel operates through debt monetization, which involves central bank financing of government deficits through the issuance of non-interest-bearing liabilities, such as currency or bank reserves, thereby relaxing the government's intertemporal budget constraint (Feldberg and Lawson, 2020). $^{3}$ A third channel is financial repression, which refers to regulatory policies that compress sovereign borrowing costs by inducing financial institutions to absorb government debt as captive buyers. By limiting alternative investments and ensuring steady demand for public debt, financial repression reduces debt servicing costs and acts as an implicit tax on domestic savers. $^{4}$

While the literatures on surprise inflation and debt monetization are relatively well developed, systematic historical evidence on the use and impact of financial repression remains limited. $^{5}$ This reflects two distinct challenges. First, measuring financial repression requires detailed historical data on the composition and cost of government debt not readily available in standard sources, especially in the decades following World War II, when such policies were widespread in advanced economies (Reinhart and Sbrancia, 2015). Second, estimating the impact of financial repression requires constructing a credible counterfactual for government bond yields absent repression, which is an inherently unobservable variable (Acalin and Ball, 2024). Existing studies of repression hence tend to rely on simplifying assumptions about the counterfactual interest rates or focus on individual country episodes or specific instruments. This makes it difficult to quantify the magnitude and persistence of financial repression in a systematic and comparable way across countries and time.

We address these challenges by developing new theory, data, and evidence of financial repression. In so doing, we contribute to the literature in three ways:

First, we develop a theoretically-grounded framework for measuring financial repression based on sectoral holdings of public sector liabilities. Our identification exploits the fact that financial repression operates through regulatory pressure targeting domestic financial institutions, disproportionately shifting their demand toward public liabilities relative to other investor groups. We formalize this differential response in a portfolio-demand model in which repression enters as a demand shifter for regulated institutions—hereafter “banks”—making them willing to hold more public liabilities at a given yield than market incentives alone would imply. Because households face no such regulatory pressure, their portfolio behavior provides a clean benchmark for return-driven allocation. The gap between bank and household holdings, after controlling for relative returns, identifies the intensity of financial repression. We propose two complementary indicators differing in the perimeter of public sector liabilities considered: a narrow fiscal measure based on government bond holdings, as well as a consolidated measure which includes repression operating through requirements to hold commercial bank reserves. This distinction allows us to separate repression that forces banks to own government debt from repression that compels them to own central bank liabilities. $^{6}$

Second, we construct a new historical dataset consolidating multiple sources on general government debt, central bank liabilities, and the sectoral composition of their holdings. We then apply our theoretical measures to this dataset covering 17 advanced economies since 1920. Cross-country averages of the repression measures suggest that repression has been a persistent feature of modern financial systems, with its use peaking around World War II and remaining elevated through the Bretton Woods era. While its use gradually declined during most of the post-1971 capital account liberalization era, repression has risen again since the Global Financial Crisis (GFC).

We also find significant association between our repression measures and conditions typically conducive to repression: repression is most pervasive when government debt and interest expenditures are high, and is also associated with higher primary balances, consistent with governments historically turning to repression when room for adjustment through traditional fiscal tools is more limited. Repression also tends to coincide with low short- and long-term interest rates and depressed government bond yields relative to private asset returns. It correlates with lower private credit growth, lower loan-to-deposit ratios, and reduced investment, which are consistent with the notion that repression leads to crowding out private capital. Finally, using newly collected post-WWII data on reserve and portfolio requirements, we show that our indicators line up systematically with these de jure policy instruments, such as reserve requirements and portfolio requirements. These results provide additional validation that our measures capture the policy environment associated with financial repression.

Third, our model allows us to derive counterfactual sovereign borrowing costs absent financial repression and then to quantify the contribution of repression to debt dynamics during historical episodes. We do so by solving for the counterfactual interest rate on government debt that clears the bond market absent repression and then embedding the implied yield wedge in a unified debt-decomposition framework alongside primary balances, interest-growth differentials, inflation surprises, central bank purchases, and debt restructuring. Applying this framework to our country sample with a focus on the United Kingdom and United States, we find that repression has historically generated sizable fiscal savings. In the United Kingdom, it was the single largest deleveraging channel in the postwar decade, accounting for more of the observed debt reduction than either surprise inflation or fiscal consolidation. In the United States, fiscal consolidation played the largest role in postwar debt reduction, but repression was also a major contributor. Across the full panel, median annual fiscal savings from financial repression averaged around 0.57 percent per year, peaking sharply in the mid-1940s. Dispersion across countries is particularly pronounced in the 1940s and early 1950s, with another widening in the 1980s, pointing to sizable heterogeneity in the fiscal gains from repression. Median fiscal savings rise again after the GFC, from about 0.08 percent in 2008 to about 0.51 percent in 2020.

Related Literature. Our paper contributes to three related strands of literature: the measurement and historical correlates of financial repression, studies of debt monetization and monetary financing, and the decomposition of public debt dynamics.

The literature on financial repression dates back to McKinnon (1970) and Shaw (1973), who define financial repression as policies that constrain financial intermediation and implicitly tax savings. Subsequent work often adopts a narrower usage, focusing on policies that lower the effective cost of domestic funding to governments. Measurement remains challenging because the relevant counterfactual interest rate absent repression is unobserved. Giovannini and de Melo (1990) address this challenge by exploiting the wedge between the government's external borrowing cost (less directly shaped by domestic repression) and its domestic cost of funds to infer the implicit revenue from repression. This approach is less useful when external borrowing is limited or when cross-border markets are segmented (for example, due to capital controls or heterogeneous investor bases). A seminal contribution by Reinhart and Sbrancia (2015) quantifies the fiscal savings from repression by comparing the ex-post real return on government debt to fixed counterfactual real interest rates (one to three percentage points lower than realized), showing that this channel could account for a substantial share of postwar debt reduction across advanced economies. In addition, single-country studies leverage richer institutional detail to construct tighter interest rate counterfactuals, including Acalin and Ball (2024) for the postwar United States and Lehner et al. (2025), who construct tax- and option-adjusted corporate-Treasury yield spreads for the United States since 1860 to provide a consistent historical estimate of the government's funding advantage. We contribute to this literature by developing quantity-based indicators that exploit differential sectoral absorption of government liabilities and map these quantity shifts into an explicit repression wedge, enabling systematic comparisons across countries and time. $^{7}$

Our work also relates to the literature on debt monetization and monetary financing. In this literature, “monetization” is typically understood as relaxing the government resource constraint through the issuance of currency or other non-interest-bearing central bank liabilities, rather than simply central bank purchases of government bonds (Feldberg and Lawson, 2020). This perspective connects to classic arguments about the fiscal constraints on monetary outcomes and the seigniorage implications of central bank balance sheets (Sargent and Wallace, 1981; Reis, 2016). That literature focuses primarily on the fiscal dividend from issuing non-interest-bearing liabilities; our monetary repression indicator captures a related but distinct mechanism, namely the below-market remuneration of interest-bearing government liabilities, which generates an implicit fiscal transfer that typical seigniorage accounting does not capture (Reis, 2025; Payne and Szöke, 2025).

Finally, we contribute to the broader literature on sovereign debt reduction and the decomposition of public debt dynamics. This literature studies the multiple channels underpinning debt reductions, including inflation and its historical role in consolidations (Eichengreen and Esteves, 2022), interest-growth dynamics and the associated “debt revenue” from issuing safe/liquid public debt (Reis, 2022), the conditions under which fiscal consolidations durably reduce debt ratios (International Monetary Fund, 2023a), financial repression through persistently low or negative real returns (Reinhart and Sbrancia, 2015; Acalin and Ball, 2024), and debt monetization (Feldberg and Lawson, 2020). More synthetic historical accounts stress that high-debt episodes can be long-lived and that countries draw on a menu of orthodox and heterodox tools depending on institutions and debt composition (Reinhart et al., 2012; Kose et al., 2022). We add to this literature by embedding our repression measures in debt-decomposition frameworks that quantify the contribution of financial repression alongside fiscal adjustment and inflation-related channels. $^{8}$

The rest of this paper proceeds as follows. Section 2. defines fiscal and monetary repression, describes the data used in the paper, and provides stylized facts to motivate the paper's theoretical framework. Section 3. introduces the paper's theoretical model and describes how we measure fiscal and monetary repression. Section 4. presents the paper's results and shows both the use of financial repression over time and the correlates of financial repression at the country level. Section 5. explains the role of financial repression in sovereign debt dynamics, computes the market-free interest rate absent repression, and quantifies the contribution of repression to debt dynamics. Section 6. concludes.

## 2. Concepts, Data, and Stylized Facts

This section motivates our measurement framework in three steps. We first distinguish between fiscal and monetary forms of financial repression and relate this taxonomy to the indicators developed below. We then describe the historical dataset used to construct these measures across 17 advanced economies. Finally, we use these data to document a set of stylized facts that motivate the theoretical framework developed in the next section.

## 2.1. Varieties of Financial Repression

Financial repression describes a suite of policies that share a common balance-sheet mechanism: they induce financial intermediaries to hold government liabilities at administered or below-market returns, thereby transferring resources from the private sector to the state. We organize the concept around the two implementation channels that map directly into the empirical indicators developed below. $^{9}$ The organizing distinction is the perimeter of the public sector liability being placed onto regulated intermediaries. In some episodes, repression operates primarily through the fiscal authority's liabilities, by compelling financial institutions to absorb sovereign debt on favorable terms for the state. In other episodes, repression operates through the monetary authority's liabilities, by expanding and/or mandating holdings of central bank liabilities at returns below market alternatives. Table 1 summarizes how this taxonomy maps into our narrow and broad indicators, as introduced in Section 3.

We use the term fiscal repression to refer to policy interventions in which regulated intermediaries absorb a share of government bonds relative to other investors, compressing the sove

[中间内容因长度限制已省略]

onomy, 128 (2), 710–739.

COTTARELLI, C. et al. (2017). Fiscal politics. In Fiscal Politics, 1, International Monetary Fund.

DALIO, R. (2025). How Countries Go Broke: The Big Cycle. Avid Reader Press / Simon & Schuster, first edition edn.

EICHENGREEN, B. and ESTEVES, R. (2022). Up and away? Inflation and debt consolidation in historical perspective. Oxford Open Economics, 1, odac008.

EREN, E., SCHRIMPF, A. and XIA, F. D. (2023). The Demand for Government Debt. BIS Working Papers 1105, Bank for International Settlements, revised December 2025.

FELDBERG, G. and LAWSON, T. (2020). Monetization of fiscal deficits and covid-19: A primer. Journal of Financial Crises, 2 (4), 1–35.

FURCERI, D., OSTRY, J. D., PAPAGEORGIOU, C. and QUINN, D. P. (2024). Navigating the Treacherous Political Economy of Structural Reform. Tech. rep., Bruegel.

GASPAR, V. (2024). Solving the global fiscal policy trilemma. Foreign Policy.

GIOVANNINI, A. and DE MELO, M. (1990). Government Revenue from Financial Repression. Tech. Rep. WPS 533, World Bank.

GOPINATH, G. (2024). Navigating fragmentation, conflict, and large shocks. Speech at the NBU-NBP Annual Research Conference, First Deputy Managing Director, IMF.

GRAF VON LUCKNER, C., MEYER, J., REINHART, C. M. and TREBESCH, C. (2024). Sovereign haircuts: 200 years of creditor losses. IMF Economic Review, 73, 150–195.

HALL, G. J. and SARGENT, T. J. (2011). Interest rate risk and other determinants of post-WWII U.S. government debt/GDP dynamics. American Economic Journal: Macroeconomics, 3 (3), 192–214.

HILSCHER, J., RAVIV, A. and REIS, R. (2021). Inflating away the public debt? An empirical assessment. Review of Financial Studies, 35 (3), 1553–1595.

HUMPHREY, T. M. and KELEHER, R. E. (1982). The Monetary Approach to the Balance of Payments, Exchange Rates, and World Inflation. New York: Praeger.

INTERNATIONAL MONETARY FUND (2023a). Coming down to earth: How to tackle soaring public debt. In World Economic Outlook: A Rocky Recovery, 3, Washington, DC: International Monetary Fund.

INTERNATIONAL MONETARY FUND (2023b). Fiscal Monitor: Climate Crossroads—Fiscal Policies in a Warming World. Washington, DC: International Monetary Fund.

INTERNATIONAL MONETARY FUND (2023c). Inflation and Disinflation: What Role for Fiscal Policy? Fiscal monitor: On the path to policy normalization, chapter 2, International Monetary Fund, Washington, DC.

INTERNATIONAL MONETARY FUND (2026). Understanding Global Imbalances. IMF Policy Paper PPEA/2026/006, International Monetary Fund, Washington, D.C., discussed by the IMF Executive Board on April 1, 2026.

JAFAROV, E., MAINO, R. and PANI, M. (2019). Financial Repression Is Knocking at the Door, Again: Should We Be Concerned? IMF Working Paper WP/19/211, International Monetary Fund, Washington, DC.

JEANNE, O. (2025). From Fiscal Deadlock to Financial Repression: Anatomy of a Fall. Working Paper 33395, National Bureau of Economic Research.

JORDÀ, O., SCHULARICK, M. and TAYLOR, A. M. (2017). Macrofinancial history and the new business cycle facts. NBER Macroeconomics Annual, 31, 213–263.

KOSE, M. A., OHNSORGE, F. L., REINHART, C. M. and ROGOFF, K. S. (2022). The aftermath of debt surges. Annual Review of Economics, 14 (1), 637–663.

KRISHNAMURTHY, A. and VISSING-JORGENSEN, A. (2012). The aggregate demand for treasury debt. Journal of Political Economy, 120 (2), 233–267.

LEEPER, E. M. (1991). Equilibria under ‘Active’ and ‘Passive’ monetary and fiscal policies. Journal of Monetary Economics, 27 (1), 129–147.

LEHNER, C., PAYNE, J., SHURTLEFF, J. and SZÖKE, B. (2025). The U.S. treasury funding advantage since 1860, manuscript; revise and resubmit at the Journal of Political Economy.

MAURO, P., ROMEU, R., BINDER, A. and ZAMAN, A. (2013). A Modern History of Fiscal Prudence and Profligacy. IMF Working Paper WP/13/5, International Monetary Fund.

MCKINNON, R. I. (1970). Money and Capital in Economic Development. Washington, DC: Brookings Institution.

MÜLLER-PLANTENBERG, N. et al. (2024). The Global Macro Database. Tech. rep., Global Macro Database Project.

ONGENA, S., POPOV, A. and VAN HOREN, N. (2019). The invisible hand of the government: Moral suasion during the european sovereign debt crisis. American Economic Journal: Macroeconomics, 11 (4), 346–379.

PAYNE, J. and SZÖKE, B. (2025). Inflation and regulation of government debt: Us historical evidence. Annual Review of Financial Economics, 17, 151–172, review Article, Open Access.

PIKETTY, T. and ZUCMAN, G. (2014). Capital is back: Wealth-income ratios in rich countries, 1700–2010. Quarterly Journal of Economics, 129 (3), 1255–1310.

REINHART, C. M., REINHART, V. R. and ROGOFF, K. S. (2012). Debt overhangs: Past and present. Tech. rep., National Bureau of Economic Research.

— and ROGOFF, K. S. (2009). This Time Is Different: Eight Centuries of Financial Folly. Princeton, NJ: Princeton University Press.

— and SBRANCIA, M. B. (2015). The Liquidation of Government Debt. Tech. Rep. WP/15/7, International Monetary Fund.

REIS, R. (2016). Can the Central Bank Alleviate Fiscal Burdens? NBER Working Paper 23014, National Bureau of Economic Research.

— (2022). Debt revenue and the sustainability of public debt. Journal of Economic Perspectives, 36 (4), 103–124.

— (2025). Financial repression in the XXIst century, mundell-Fleming Lecture, IMF XXVIth Jacques Polak Annual Research Conference, November 2025.

SARGENT, T. J. and WALLACE, N. (1981). Some unpleasant monetarist arithmetic. Federal Reserve Bank of Minneapolis Quarterly Review, 5 (3).

SHAW, E. S. (1973). Financial Deepening in Economic Development. New York.

![](images/fd6a0dba0239bd27efabed710712fd99113c33f3aec0d9ebd13cc6b515faebb5.jpg)

## PUBLICATIONS
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
