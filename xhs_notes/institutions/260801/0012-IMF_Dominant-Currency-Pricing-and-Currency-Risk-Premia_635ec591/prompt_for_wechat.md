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
# Dominant Currency Pricing and Currency Risk Premia

Prepared by Husnu C. Dalgic and Galip Kemal Ozhan

WP/26/158

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/4086583e64817db34d66e712fb00731a61ce76fe30427a508a6164236c555141.jpg)

# IMF Working Paper Research Department

# Dominant Currency Pricing and Currency Risk Premia Prepared by Husnu C. Dalgic and Galip Kemal Ozhan\*

Authorized for distribution by Deniz Igan
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper studies how dominant-currency pricing affects currency risk premia. Empirically, we extract common risk factors from excess currency returns using principal components and relate countries' factor exposures to observable macroeconomic characteristics, with export dollar invoicing emerging as a predictor of carry trade exposure. A small open-economy model with dominant-currency pricing and dollar-denominated liabilities explains why. Dollar export invoicing weakens the exchange rate's stabilizing effect on external demand, while dollar debt makes depreciation costly for leveraged intermediaries. When the two frictions interact, depreciations occur in bad states, local-currency assets become risky, the currency premium rises, and the risk-adjusted neutral rate increases. Under a standard Taylor rule, this mechanism generates persistently higher inflation.

<table><tr><td>JEL Classification Numbers:</td><td>E44, E32, F41, G15, G21</td></tr><tr><td>Keywords:</td><td>Currency returns; dominant currency pricing; uncovered interest parity; inflation; dollar debt</td></tr><tr><td>Authors&#x27; email addresses:</td><td>gozhan@IMF.orgdalgic@uni-mannheim.de</td></tr></table>

WORKING PAPERS

# Dominant Currency Pricing and Currency Risk Premia

Prepared by Husnu C. Dalgic and Galip Kemal Ozhan\*

# Dominant Currency Pricing and Currency Risk Premia\*

Husnu C. Dalgic $^{†}$ University of Mannheim

Galip Kemal Ozhan $^{\dagger}$ International Monetary Fund
and NBER

July 23, 2026

## Abstract

This paper studies how dominant-currency pricing affects currency risk premia. Empirically, we extract common risk factors from excess currency returns using principal components and relate countries' factor exposures to observable macroeconomic characteristics, with export dollar invoicing emerging as a predictor of carry-trade exposure. A small open-economy model with dominant-currency pricing and dollar-denominated liabilities explains why. Dollar export invoicing weakens the exchange rate's stabilizing effect on external demand, while dollar debt makes depreciation costly for leveraged intermediaries. When the two frictions interact, depreciations occur in bad states, local-currency assets become risky, the currency premium rises, and the risk-adjusted neutral rate increases. Under a standard Taylor rule, this mechanism generates persistently higher inflation.

JEL Classification: E44, F32, F41, G15, G21.

Keywords: Currency returns; dominant currency pricing; uncovered interest parity; inflation; dollar debt.

## 1 Introduction

One of the salient features of the international monetary system is the asymmetric use of currencies in global trade and finance (see, for example, Gopinath and Stein (2021)). The U.S. dollar is the dominant vehicle currency in international trade, as documented by Goldberg and Tille (2008) and Gopinath, Boz, Casas, Díez, Gourinchas and Plagborg-Møller (2020). The dollar is also central to global financial intermediation and to the denomination of cross-border liabilities. These two forms of dollar dominance are typically studied separately. Trade invoicing affects pass-through and expenditure switching, while liability dollarization affects balance sheets and financial fragility. This paper's hypothesis is that their interaction is central to the risk properties of exchange rates.

The cross section of currency returns provides a natural testing ground for this hypothesis. If the international price system and global balance sheets are disproportionately dollar denominated, then exchange rates need not be merely relative prices; but they also affect the state-contingent payoff of nominal assets, the tightness of financial constraints, and the severity of downturns. We therefore ask whether dominant-currency pricing and liability dollarization shape currencies' exposure to global risk, the cross section of currency risk premia, and the transmission of monetary policy in small open economies.

In particular, the paper asks three questions. First, do dollar export invoicing and dollar-denominated liabilities help explain why some currencies are more exposed to global currency risk than others? Second, through what mechanism do these structural features make local-currency assets pay off poorly in bad states and thereby raise currency risk premia? Third, what are the implications for inflation and monetary policy in small open economies?

We begin empirically. We construct monthly excess currency returns for 25 countries from 2003:02 to 2018:11 using FX4Casts and IMF IFS data, together with the invoicing measures in Gopinath, Boz, Casas, Díez, Gourinchas and Plagborg-Møller (2020). Following Lustig, Roussanov and Verdelhan (2011), we extract common factors from currency excess returns. The first factor is a broad dollar factor that comoves with global equity returns, while the second is a carry-trade factor associated with global risk aversion. We then relate each currency's exposure to these factors to country characteristics, focusing on export dollar invoicing, foreign-currency liabilities in the banking system,

and net foreign asset positions.

The main empirical result is that countries' exposure to currency risk is systematically shaped by their trade and financial structures. Greater dollar invoicing of exports is strongly associated with higher exposure to the carry-trade risk factor, and this relationship remains robust after controlling for additional country characteristics, including country size, reserves, trade-network centrality, and NFA-to-GFP. Banking-sector foreign liability exposure and net debtor positions also help explain cross-country differences in factor loadings. These exposures are priced in currency markets: currencies with higher loadings on global risk factors earn higher average excess returns, and the same exposures are associated with higher average inflation. Taken together, the evidence points to a macro-financial risk channel. In economies with dollarized trade and balance sheets, local-currency assets tend to lose value in adverse global states, leading investors to demand compensation for holding them.

Figure 1 summarizes this empirical pattern. Panel (a) shows that export dollar invoicing is a strong predictor of carry-trade exposure. Panel (b) shows that currencies with greater carry-trade exposure earn higher average excess returns. Panel (c) shows that these exposures are also associated with higher average inflation. Together, the panels motivate the paper's central mechanism by showing that the same structural features that make a currency risky for investors also shape monetary transmission.

To interpret the empirical evidence, we develop a small open-economy model with dominant-currency pricing, dollar-denominated bank liabilities, and segmented international asset markets. The model builds on the literature on open-economy financial intermediation with foreign-currency liabilities, including Aoki, Benigno and Kiyotaki (2020), Ozhan (2020), and Benhima, Blengini and Merrouche (2025). In the model, exporters set prices in dollars, imported goods are priced in dollars, domestic intermediaries borrow partly in dollars, and foreign investors require compensation for holding local-currency assets when exchange-rate risk rises.

The analytical results show that the premium on local-currency assets rises through a covariance channel created by the interaction of dollar liabilities and sticky dollar export prices. Dollar liabilities determine the direct balance-sheet exposure to depreciation. When the domestic currency depreciates, the local-currency value of banks' dollar debt rises, bank net worth falls, and the marginal value of bank capital increases. Sticky dollar export prices determine how much stabilization the exchange rate provides on the real side of the economy. When export prices are slow to adjust in dollars, a depreciation

![](images/ceaeb7893b3b3c26ae98ba89ee79651515429d81f033cbb0b34377c0177e4058.jpg)  
(a) Carry-trade exposure and dollar invoicing

![](images/fb37f1f3783d04594e59810866e26d5f42d7bfa96266bcbbc0fdca102406e855.jpg)  
(b) Carry-trade exposure and excess returns

![](images/6f34dd590b348e04d01bd8dd712caecc244eddc6c49c7e318ed644a29d8e4038.jpg)  
(c) Carry-trade exposure and inflation  
Figure 1: Carry-trade risk, currency returns, and inflation

Notes: Carry-trade exposure is the loading on the second principal component of currency excess returns, following Lustig, Roussanov and Verdelhan (2011). Currency returns cover 25 countries from 2003:02 to 2018:11. Data sources are FX4Casts, IMF IFS, and Gopinath, Boz, Casas, Díez, Gourinchas and Plagborg-Møller (2020).

does not quickly lower the price faced by foreign buyers, so export demand responds only gradually. The exchange rate therefore has weaker shock-absorbing properties. Instead of rapidly supporting external demand, the depreciation immediately raises import prices and dollar-debt burdens while the export response is delayed. This timing makes depreciation coincide with lower consumption, weaker investment, lower bank net worth, and a higher continuation value of intermediary wealth. Local-currency assets are risky in this environment because their payoff is low when the pricing kernel is high. Investors therefore require a higher expected return to hold them. The premium is largest when both frictions are present because each friction strengthens a different part of the same pricing mechanism. Dollar liabilities make a depreciation reduce bank net worth directly by increasing the local-currency value of banks' dollar debt. Sticky dollar export prices make the depreciation less useful for stabilizing the real economy because foreign buyers do not quickly see lower dollar prices, so exports do not immediately offset the rise in import costs and the fall in domestic spending. The depreciation therefore comes with weaker consumption, lower investment, tighter credit, and a higher value of bank capital. Since local-currency assets lose value in exactly these states, investors require a higher expected return to hold them.

We then quantify the mechanism. We calibrate the model to a small open emerging-market economy and study a foreign interest-rate shock across economies that differ in two dimensions: the degree of dollar export invoicing and the share of dollar liabilities. The largest UIP deviation arises when both frictions are present. High dollar debt without high dollar invoicing generates a sizable premium, but a smaller one, because the exchange rate can still work more effectively through export prices. High invoicing without high dollar debt generates only a modest premium, because depreciation does not impose large valuation losses on intermediary balance sheets. The interaction is therefore the central quantitative force because dollar liabilities make depreciation financially costly, while sticky dollar export prices prevent depreciation from delivering sufficient real stabilization.

The impulse responses also clarify the role of the exchange rate. In economies with limited dollar invoicing of exports and low financial-sector dollar debt, depreciation acts more like a shock absorber. It improves external competitiveness without generating large balance-sheet losses. In vulnerable economies, where a large share of exports is invoiced in dollars and the financial sector carries substantial dollar debt, depreciation instead becomes a macro-financial state variable. It raises the domestic price of imports, increases the local-currency burden of dollar liabilities, tightens financial constraints, and raises the premium investors require to hold local-currency assets. Although exports may rise after the shock, this expansion does not reflect the frictionless expenditure-switching mechanism of the textbook model. It is achieved through a larger depreciation, a higher UIP premium, and a sharper compression of domestic absorption.

The stochastic steady-state results show that this mechanism also has long-run implications for inflation and monetary policy. Following Benigno, Benigno and Nisticò (2012) and Ghironi and Ozhan (2025), we solve the model using a higher-order approximation and find that greater export-price stickiness raises exchange-rate volatility in the stochastic steady state. As a result, local-currency assets become riskier, and the UIP premium remains elevated even in the long run. This premium acts like an increase in the risk-adjusted neutral interest rate. Under a conventional Taylor rule with a fixed intercept, the policy rate is too low relative to the return required by investors, causing average inflation to rise above target. A rule that responds more robustly to movements in the neutral rate, in the spirit of Orphanides and Williams (2006), can stabilize inflation, but only by sustaining higher interest-rate spreads.

The paper contributes to three related literatures. First, it contributes to the literature on trade invoicing, which studies how vehicle-currency use and nominal rigidities shape exchange-rate pass-through and monetary transmission (Obstfeld and Rogoff, 1995; Betts and Devereux, 2000; Devereux and Engel, 2003; Goldberg and Tille, 2008; Gopinath, Boz, Casas, Díez, Gourinchas and Plagborg-Møller, 2020; Mukhin, 2022; Amiti, Itskhoki and Konings, 2022; Egorov and Mukhin, 2023). The paper connects this literature to currency asset pricing by showing that the currency in which exports are priced affects the payoff of local-currency assets in global bad states. Second, it contributes to the literature on the determinants of currency risk premia and the UIP puzzle, which links currency excess returns to global risk factors, country characteristics, trade networks, financial intermediation, external positions, and limits to international risk sharing (Hassan, 2013; Della Corte, Riddiough and Sarno, 2016; Ready, Roussanov and Ward, 2017a,b; Richmond, 2019; Wiriadinata, 2021; Jiang, 2021, 2022; Hassan and Zhang, 2021; Kalemli-Özcan and Varela, 2021; Goldberg and Krogstrup, 2023; Liao and Zhang, 2025; Bocola and Lorenzoni, 2020; Dao, Gourinchas and Itskhoki, 2025). Relative to this work, the paper identifies dollar export invoicing and foreign-currency liabilities as observable structural sources of exposure to global currency risk. Third, it contributes to work on exchange rate volatility and monetary policy by showing how dollar liabilities and dollar export invoicing jointly determine inflation dynamics (Benigno, Benigno and Nisticò, 2012; Kalemli-Özcan, 2019; Aoki, Benigno and Kiyotaki, 2020; Auclert, Rognlie, Souchier and Straub, 2021; Bacchetta, Benhima and Berthold, 2023a; Bacchetta, Cordonier and Merrouche, 2023b; Kalemli-Özcan and Unsal, 2023). The central contribution is to connect these literatures through a single macro-financial mechanism in which the currency risk premium is determined by the interaction between the currency denomination of liabilities and the currency denomination of export prices.

The rest of the paper is organized as follows. Section 2 describes the data and presents the empirical analysis. Section 3 presents the small open-economy model. Section 4 analytically derives the expressions for the model's key mechanism. Section 5 takes the analytical mechanism to the quantitative model and studies the transmission of foreign monetary shocks. Section 6 concludes.

## 2 Empirical Analysis

We identify two principal sources of currency market risk—the Dollar Risk Factor, tied to global asset prices, and the Carry Trade Risk Factor, linked to global risk aversion (Section 2.1). Both represent priced risks that command higher average excess returns (Table 1). The underlying macroeconomic channel for this risk is the co-movement between GDP and the exchange rate (Section 2.4); currencies that depreciate during recessions are inherently riskier to hold.

Crucially, we link these cyclical co-movements and risk exposures directly to observable structural frictions (Sections 2.3 and 2.5). High dollar invoicing, significant banking-sector foreign liabilities (FL/FA), and a net debtor position (low NFA/GDP) jointly exacerbate this risky GDP-ER correlation and determine a country's exposure to both global factors. Furthermore, professional forecast data confirms that investors ex-ante price the higher returns associated with these structural vulnerabilities (Section 2.6). Ultimately, the empirical finding that dollar debt and trade invoicing jointly shape a currency's risk profile directly motivates our theoretical framework.

## 2.1 Currency Returns

Our primary dataset consists of monthly data for 25 countries from 02/2003 to 11/2018, sourced from FX4casts. $^{1}$ We define the realized excess currency return $(RX_{t+1})$ for a USD based investor as:

$$
R X _ {t + 1} \equiv R _ {t} ^ {L} \frac {S _ {t}}{S _ {t + 1}} - R _ {t} ^ {U S}\tag{1}
$$

where $S_{t}$ is the spot exchange rate (LCU per USD), and $R_{t}^{L}$ and $R_{t}^{US}$ are the respective local and US gross short-term interest rates from t to $t + 1$ . This formula represents the ex-post profit from borrowing in USD, investing in the local currency, and converting the proceeds back to USD one period later.

From a macroeconomic perspective, our primary object of interest is the unconditional average of these returns, which forms the currency risk premium:

$$
\mathbb {E} [ R X _ {t + 1} ] \equiv \mathbb {E} \left[ R _ {t} ^ {L} \frac {S _ {t}}{S _ {t + 1}} - R _ {t} ^ {U S} \right]
$$

We aim to understand the cross-sectional determinants of this premium. To expand our sample for the cross-sectional analysis, we augment th

[中间内容因长度限制已省略]

The impulse responses show that the largest UIP spread occurs when high dollar liabilities are combined with high dollar export invoicing. The stochastic steady-state exercises that vary $\theta_{x}$ show that export-price stickiness raises exchange-rate volatility, makes depreciation more countercyclical, and increases the unconditional UIP premium. The appendix exercises that vary $\bar{\phi}$ show that the level of dollar liabilities raises the same premium by strengthening the negative covariance between depreciation and bank net worth. All three results are the same mechanism viewed from different margins of (167).

## F Additional Quantitative Results

## F.1 Response to Foreign Interest Rate Shocks

Figure 24 decomposes the transmission mechanism by simulating the foreign interest rate shock across four distinct economy profiles, varying both the level of dollar-denominated debt and the degree of dollar invoicing.

The key observation: the amplification effect of trade frictions is highly contingent on the presence of financial frictions. When foreign currency debt is low, the choice of invoicing currency has a negligible impact on real macroeconomic outcomes; the output and investment trajectories remain largely insulated regardless of the invoicing regime.

Conversely, when the economy has high foreign currency debt, dollar invoicing severely amplifies the shock. In this highly dollarized economy, high dollar invoicing drastically exacerbates the downturn, roughly doubling the peak declines in both investment and GDP compared to an identical low dollar debt economy with low dollar invoicing.

![](images/4b4721f9c6cc08777c85c61391a9b7402832856dbe02c68ff78e6ff14efb8b23.jpg)  
Figure 24: Response to Foreign Interest Rate Shock

Figure 25 shows how financial system moves following foreign interest rate shock. Under high dollar debt, leverage goes up to rebuild balance sheets that have been deteriorated. Local residents decrease savings because they want to smooth consumption so the economy needs to attract foreign capital both in local currency (panel 1,1) and foreign currency (panel 2,1)

![](images/b729cb16a1d6d25358d129947b3f09b7142fb7a0ce231dd62bc9fc3d364c20d3.jpg)  
Figure 25: Financial Flows

## F.2 Varying Dollar Debt in the Steady State

In this Section, we replicate results in Section 5.4 by varying dollar debt in the steady state by changing target portfolio of bankers $\bar{\phi}$ . Figure 26 plots the increase in ER volatility, and rising UIP premium and inflation following increasing target dollar ratio.

![](images/1d4af50b73c9d9de77a7c747039bd97714bb5f3e3cbe5c0f28646f40c9425a18.jpg)  
(a) Exchange rate volatility ( $\phi$ )

![](images/c70326efb3058e1921a418d3784d1c77f90769ff060fa255e1bc917b30aa13f7.jpg)  
(b) Output and exchange rate comovement ( $\phi$ )

![](images/25fbcd711687f32ad6b23f757257fa4e17b877131569bea3a19fc628dd13779e.jpg)  
(c) UIP premium ( $\phi$ )

![](images/13849cf3d0fe90f242b597bc4faf5e09ae32443671c9ad928ec720ebb122dfbf.jpg)  
(d) Steady state inflation  
Figure 26: Steady State with respect to Dollar Debt ( $\phi$ )

## F.3 Inflation and GDP-ER Co-movement

In this section, we use above simulations to generate the relationship between GDP-ER comovement and inflation. Figure 27 is able to capture the negative relationship between average inflation and the comovement between output and the exchange rate along both dollar debt and dollar invoicing. In countries with negative comovement between GDP and ER, exchange rate is not able to insulate the economy against external shocks; which makes inflation and output more volatile. As a response, both local and foreign investors demand risk premium and if the central bank does not address this premium, inflation increases.

![](images/1c4522d4606af9e0958d266f0ec5e65d9d36cecd441201815efcd1a8a5a857f4.jpg)  
(a) Along export prices stickiness ( $\theta^{x}$ )

![](images/db89cf9947aab7d73911394b52e0173fafa45fd9e3915418dcb125a18d789ebe.jpg)  
(b) Along Dollar Debt ( $\bar{\phi}$ )  
Figure 27: Inflation and GDP-ER Co-movement

## F.3.1 Equity Premium

In this section, we look at what happens to equity premium as the macro risk increases with higher dollar invoicing. Equity premium,

$$
\mathbb {E} _ {t} (R _ {t + 1} ^ {k}) - R _ {t}
$$

where return to capital is defined as marginal product of capital $(r_{t}^{k})$ and undepreciated capital priced at current price of capital $((1-\delta)P_{t}^{k})$ divided by price of capital previous period $(P_{t-1}^{k})$

$$
R ^ {k} = \frac {r _ {t} ^ {k} + (1 - \delta) P _ {t} ^ {k}}{P _ {t - 1} ^ {k}}
$$

We define equity premium as the difference between return to capital and local interest rates. This is slightly misleading because actual cost of capital is defined as the weighted average of funding sources, which also include dollar financing.

Figure 28a plots what happens to equity premium as dollar invoicing and dollar debt increase. Equity premium falls. This is because both $R_{t}^{k}$ and $R_{t}$ increase but $R_{t}$ increases more. Capital gains part of return to capital provides cushion against global shocks because, as real assets, their value increases with pass through inflation generated by exchange rate depreciations. On the other hand, local interest rates become unattractive investment because they lose value following adverse global shocks, which makes investors require premium to invest.

![](images/3e39d589272df814926aac79f10c5c0ae64edb4169bba2d8a1bb63ab374225c5.jpg)  
(a) Equity Premium and export dollar price stickiness ( $\theta^{x}$ )  
Figure 28: Steady State Equity Premium

![](images/552874ed94cce59f2d5804a54d6c1fbfcd28dba5457feb6f5546bed5788c1591.jpg)

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
