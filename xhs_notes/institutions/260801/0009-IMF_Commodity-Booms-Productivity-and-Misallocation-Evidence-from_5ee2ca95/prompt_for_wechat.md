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
# Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data

Prepared by Pablo Filippi, Ryan Kim, Nan Li, María Jesús Pérez, Younghun Shim

WP/26/163

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/8c8e4ee6dfe212f7f7270c47c5369890bc1ad7e71034437a86441689dc76803a.jpg)

# IMF Working Paper Research Department

Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data Prepared by Pablo Filippi, Ryan Kim, Nan Li, María Jesús Pérez, Younghun Shim\*

Authorized for distribution by Petia Topalova
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: We study how commodity booms affect productivity using administrative microdata from Chile combining firm exports by product and destination, employer-employee records, and firm-to-firm production networks. Exploiting differential Chinese demand across Chilean commodity products, we measure firms' exposure to the boom and trace its effects on productivity and resource allocation. We find three mechanisms. First, more exposed firms experience larger revenue increases but no differential productivity gains, channeling revenues into wages and materials. Second, among exposed firms, low-productivity firms expand employment while high-productivity firms do not, hiring workers from more productive employers. Third, domestic suppliers with greater indirect exposure show larger sales and productivity gains. We develop a model with heterogeneous export wedges and labor market frictions in which commodity booms can reduce sectoral productivity by exacerbating input misallocation, consistent with firm-level and aggregate evidence. Calibrated to Chile, this mechanism explains half of the mining TFP decline from 2005 to 2013.

RECOMMENDED CITATION: Filippi, P., R. Kim, N. Li, M. J. Pérez, and Y. Shim. 2026. Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data. IMF Working Paper WP/26/163. Washington, DC: International Monetary Fund.

<table><tr><td>JEL Classification Numbers:</td><td>E23, E24, F41, F43</td></tr><tr><td>Keywords:</td><td>Commodity booms; Misallocation; Productivity; Micro-level Data; Labor reallocation.</td></tr><tr><td>Authors&#x27; email addresses:</td><td>pfilippi@hacienda.gov.cl; rkim59@snu.ac.kr; nli@imf.org; mperezg@fen.uchile.cl; yshim@imf.org</td></tr></table>

# Commodity Booms, Productivity, and Misallocation: Evidence from Chile's Administrative Data

Prepared by Pablo Filippi, Ryan Kim, Nan Li, María Jesús Pérez, Younghun Shim

## 1 Introduction

The global commodity price fluctuations—including periods of sustained price change known as commodity super-cycles—have long been an important driver of economic activity in emerging economies. A substantial literature documents their effects on output volatility and long-run economic growth. Yet, how these booms affect productivity of commodity-exporting countries remains unclear, with several potential mechanisms pointing in different directions. Understanding these mechanisms matters for a large number of resource-dependent developing countries, from copper and lithium exporters in Latin America and Africa to oil producers in the Middle East. For these countries, whether commodity windfalls translate into lasting productivity gains, rather than transitory income, shapes long-run development. These questions are newly relevant as commodity markets appear to have entered a new super-cycle, driven by the global energy transition and rising demand for critical minerals.

This paper provides micro-level evidence on how commodity booms affect firm productivity and resource allocation. We focus on Chile, a commodity-dependent economy that experienced a striking pattern of productivity dynamics during the 2000s: the China-driven commodity boom generated massive export revenue increases, yet aggregate mining sector productivity declined sharply. Between 2005 and 2013, real mining total factor productivity (TFP) fell by approximately 8 percent even after controlling for geological factors, while non-mining sectors saw productivity gains (Figure 1 and A.1; De Solminihac et al., 2018). This aggregate pattern contradicts both the traditional “scale effect” prediction—where rising revenues could stimulate productivity by boosting investment or technological upgrading—and the classical Dutch disease mechanism, which predicts productivity declines in non-resource tradables rather than in the booming commodity sector itself (e.g., Corden and Neary 1982; Corden 1984).

What micro-level mechanisms can explain this aggregate pattern? $^{1}$ We argue that the answer lies in understanding how commodity booms interact with pre-existing distortions in resource allocation and affect firm-level efficiency—dynamics that granular firm- and worker-level data uniquely reveal. Chile offers an ideal setting for such an investigation due to the availability of detailed administrative microdata. We construct a comprehensive firm-level dataset by merging multiple administrative sources: transaction-level customs data on export and import prices (unit values) and quantities, firm-to-firm production networks capturing domestic supply chains, matched employer-employee records tracking worker mobility and wages, and administrative tax records on firm operations. This combined dataset, covering from 2003 to 2013, allows us to trace how global price shocks affect within-firm productivity, across-firm reallocation, workers, and propagation through supply chains at a highly detailed level of granularity, thereby uncovering the mechanisms underlying the aggregate productivity decline.

Figure 1: Global Copper Price and Chile's Mining TFP  
![](images/7ecc464f29524a76276b40fe0296460ed2efe38be7b74896bd15ec70bd407667.jpg)  
Notes. All series are expressed as ratios relative to the base year 2002. Global copper price is obtained from the London Metal Exchange, and TFP estimates are sourced from the Chilean National Commission of Productivity, which are obtained after controlling for geological factors such as ore grades, waste-to-ore ratio, pit slope, and the long gestation period of capital investments. See CNEP (2017) for details (CNEP 2017).

Our identification exploits differential price changes across commodity products, driven by China's WTO accession and rapid industrialization (Fernández et al., 2023). We assign these product-level price changes to firms using their pre-boom export shares. Because Chilean commodity exporters are highly specialized, each firm's shock is largely inherited from its dominant product, so the identifying variation comes from differences across firms in which product they specialize in, rather than from diversification within a firm's own export portfolio. To address a remaining concern about endogenous Chilean supply responses, we use a leave-one-out instrument—Chinese import prices from all countries except Chile, an approach common in the trade and labor literature (Autor et al., 2013)—which isolates the

China-driven demand component and lets us attribute differences in firm outcomes to the commodity price shock itself. $^{2}$

Our empirical analysis uncovers three key mechanisms through which commodity booms affect productivity. First, we document that while more exposed commodity exporters experience greater increases in revenues, material expenditures, and employment, they show no differential improvement in revenue-based TFP (TFPR) or sales per employee. This null effect persists across various production function specifications (including Cobb-Douglas, translog, and Leontief forms) that allow for flexible returns to scale. $^{3}$ Since commodity price increases likely raise firm-level output prices, an unchanged TFPR is consistent with declining physical productivity (TFPQ), potentially reflecting deteriorating ore grades or input quality as firms rapidly expand. $^{4}$ Moreover, these firms show no differential increase in domestic sales or capital accumulation, suggesting that export revenues flow primarily into variable inputs associated with exports rather than productivity-enhancing investments.

Second, we find evidence of labor misallocation across firms within the commodity sector: firms respond differently depending on initial productivity—not because low-TFPR firms face larger shocks, but because they expand more in response. Using matched employer-employee data, we show that among more exposed firms, those with high initial TFPR (above-median revenue productivity) do not differentially increase employment relative to less exposed high-TFPR firms. In contrast, low-TFPR firms that are more exposed to the commodity shock significantly expand their workforce relative to less exposed low-TFPR firms. This asymmetry is not a selection effect: the correlation between shock exposure and initial TFPR is essentially zero (-0.027). In addition, more exposed commodity exporters grow by hiring workers from other firms in the same sector, with a disproportionate share coming from more productive employers. This pattern of labor reallocation—from high- to low-productivity firms—provides direct micro-level evidence of increasing misallocation. When combined with our finding that more exposed exporters offer relatively higher wages, these results suggest that commodity booms enable less productive but export-favored firms to poach workers from more efficient producers, thereby reducing aggregate sectoral productivity.

Third, in contrast to the muted productivity response among commodity exporters, we document positive productivity spillovers to upstream domestic suppliers. Using firmto-firm transaction data, we construct measures of indirect exposure: firms that supply commodity exporters but do not themselves export commodities. We find that suppliers with greater indirect exposure (those more connected to commodity exporters) experience larger increases in sales, employment, materials expenditure, and importantly, capital investment and productivity—outcomes absent among directly exposed commodity exporters. This positive spillover effect aligns with the observed productivity gains in Chile’s non-mining sectors during the commodity boom (Figure A.1) and is consistent with demand-driven productivity improvements documented in other contexts (Ilzetzki, 2024).

To interpret the first two empirical patterns and clarify the aggregate implications, we develop a tractable theoretical framework. Our model features a small open economy with heterogeneous firms facing two distortions. First, firm-specific export wedges capture differential access to foreign markets (arising from subsidies, other differential policies, historical relationships, or others) that allow some firms to export more easily than others, regardless of their underlying productivity. Because such a wedge could be read as reduced-form heterogeneity rather than a real distortion, we discipline it in two ways: we provide three microfoundations, and we measure a concrete policy component directly from administrative data and show it moves firm behavior in the direction the mechanism requires (Section 6.4.2). Second, we model the labor market as oligopsonistic. Firms' wage-setting power generates firm-specific labor wedges, letting the model reproduce the wage increases and labor poaching we document in the data.

In this environment, a uniform increase in commodity demand has asymmetric effects across firms. Consistent with our empirical findings, the mechanism operates through differential sensitivity: firms with larger export wedges expand disproportionately, drawing labor and materials away from more productive but less export-favored competitors. This reallocation exacerbates misallocation: resources shift toward firms that generate high revenues due to privileged market access rather than superior technology. The model shows that aggregate sectoral productivity—properly measured as the output-weighted average of productivities—can decline even as output and employment rise. The framework also explains our empirical findings on labor reallocation and wage premia: in an oligopsonistic labor market, expanding low-productivity firms must offer higher wages to attract workers from more productive employers, generating the “poaching” patterns we observe in the data.

We calibrate the model to match key moments from Chilean administrative data, including export shares, sales dispersion, and export intensity variation across firms. Without targeting any of our firm-level regression coefficients, the calibrated model reproduces the muted productivity response and the disproportionate employment expansion among low-TFPR firms, both close to their empirical counterparts. These coefficients identify differential responses across firms that differ in exposure and initial productivity, net of the common boom absorbed by the intercept, and validate the reallocation mechanism at the firm level. Taking the same calibrated model to the aggregate level, we simulate a commodity boom comparable to Chile's experience. The resulting reallocation toward low-TFPR firms lowers sectoral productivity by 3.94 percent, roughly half of the $8\%$ TFP decline documented by CNEP (2017). The remaining gap likely reflects factors outside our parsimonious framework, such as capacity constraints in mining capital investment, within-firm productivity slowdown due to declining ore grades, or other sector-specific shocks and frictions. Our results demonstrate that the misallocation channel, operating through the interaction of export distortions and labor market power, can quantitatively explain a substantial portion of the aggregate productivity decline.

Literature Review. This paper contributes to several strands of literature. First, it adds to research on commodity price shocks and economic performance in small open economies (SOEs), which documents that many SOEs are highly sensitive to fluctuations in commodity prices. A central debate in this literature often concerns whether terms-of-trade shocks are key drivers of business cycle dynamics (Mendoza, 1995; Schmitt-Grohé and Uribe, 2018; Fernández et al., 2023). There are multiple channels through which commodity price shocks affect the aggregate economy, including wealth effects that benefit non-exporters more and low-tradability industries (Corden and Neary, 1982), a sovereign risk premium channel that affects borrowing costs (Shousha, 2016; Drechsel and Tenreyro, 2018), a wage channel that increases the cost of less skill-intensive industries and induces labor reallocation across sectors (Benguria et al., 2024a), and a banking sector liquidity channel that amplifies real responses (Toma and Cuba, 2024). Another recent literature quantifies the economic consequences of commodity super-cycles (Reinhart et al., 2016; Alberola and Benigno, 2017; Fernández et al., 2017; Kohn et al., 2021; González, 2021). Across this work, the focus is on aggregate and cross-country outcomes rather than on how a boom reallocates resources across firms within a sector. We use firm-level data to open that question, and find that pre-existing export distortions can channel inputs toward low-TFPR firms and lower the booming sector's productivity even as revenues surge.

Second, the paper also adds to the recent literature that studies the transmission of commodity price shocks using disaggregated data. For example, Benguria et al. (2024a)

analyzes the transmission of commodity price super-cycles in Brazil by focusing on regional variations and identifying wealth and cost channels through which these cycles affect local economies. Benguria et al. (2024b) extends this analysis to study spatial linkages, documenting substantial heterogeneity in how commodity booms affect workers across regions and skill levels, with inter-regional trade and migration playing crucial roles in the transmission. Similarly, Allcott and Keniston (2018) studies oil and gas booms in the United States, finding that manufacturing grows through upstream linkages rather than being crowded out—contradicting the classical Dutch disease prediction for non-resource tradables. Silva et al. (2024) investigates how commodity price shocks propagate through upstream and downstream linkages, affecting sectoral outputs and prices in SOEs. Amodio et al. (2025) use firm-to-firm transaction data to trace how a surge in Chinese beef demand propagates across sectors in Uruguay, finding sizable indirect gains in services linked to the export value chain. Taken together, these studies find that commodity booms propagate across regions and sectors, lifting output, wages, and producer prices in connected parts of the economy. We document a more troubling possibility within the booming sector itself: the same demand expansion that lifts firms downstream depresses productivity at its center, as inputs flow toward low-TFPR firms.

Third, we relate to the literature on misallocation and productivity. Following Hsieh and Klenow (2009)'s influential framework, numerous studies have documented substantial productivity losses from resource misallocation across firms (Oberfield, 2013; Restuccia and Rogerson, 2017; Adamopoulos et al., 2022; Heise and Porzio, 2022). A key question is how aggregate shocks reshape misallocation. Larrain and Stumpner (2017) and Bau and Matray (2023) show that positive shocks can reduce misallocation when they relax binding capital constraints on productive firms. We show how positive external shocks can instead exacerbate misallocation within the booming sector itself, where pre-existing export distortions channel inputs toward low-TFPR firms. $^{5}$ This perspective builds on Gopinath et al. (2017), who document that capital inflows in Southern Europe flowed to high-net-worth but low-productivity firms, reducing aggregate TFP. While their mechanism operates through selection, ours operates through differential sensitivity: low-TFPR firms do not face larger commodity shocks but respond more strongly to common shocks. Our perspective relates to Bai et al. (2024), which demonstrates that trade liberalization can worsen mi

[中间内容因长度限制已省略]

 cap the catch and make the quota a tradable right, working like a tax on the marginal catch worth roughly 15% of landed value (Kroetz et al., 2017). Aquaculture concessions (Decree 125 of 2003) administratively limit the number and size of maritime sites, which we treat as a 2% restriction.

Product-level wedge. For each HS6 product h,

$$
\begin{array}{r} \mathrm{subsidy} _ {h} = \max \big (0. 0 3 \cdot \mathbf {1} [ \mathrm{Reintegro} _ {h} ], t _ {h} \cdot \mathbf {1} [ \mathrm{Drawback} _ {h} ] \big) \cdot s _ {h} ^ {\mathrm{norm}}, \\ \mathrm{restriction} _ {h} = \left(0. 1 5 \cdot \mathbf {1} [ \mathrm{ITQ} _ {h} ] + 0. 0 2 \cdot \mathbf {1} [ \mathrm{Aqua} _ {h} ]\right) \cdot s _ {h} ^ {\mathrm{norm}}, \end{array}
$$

with net product wedge $\tau_{h}=subsidy_{h}-restriction_{h}$ . The input tariff $t_{h}$ is built from customs data alone in three steps: a national HS6 tariff $t_{j}^{nat}=\sum_{2003}duties_{j}/\sum_{2003}CIF_{j}$ , the effective duty on inputs of HS6 j (capped at the statutory 11%); a firm input tariff $t_{f}^{input}=\sum_{j}w_{fj}^{imp}t_{j}^{nat}$ , where $w_{fj}^{imp}$ is firm f's CIF share in input j; and a product tariff $t_{h}=\sum_{f}w_{fh}^{exp}t_{f}^{input}$ , the FOB-weighted average of $t_{f}^{input}$ across firms exporting h. The multiplier $s_{h}^{norm}$ is the 2003 FOB share of h shipped under the normal-export operation code; it down-weights products whose recorded flow is mostly re-export or temporary movement (its median is one, so only the re-export-heavy tail is affected).

Firm-level wedge. We aggregate to firms by a 2003 export-share shift-share, $\tau_f^F = \sum_h w_{fh} \tau_h$ , where $w_{fh}$ is firm $f$ 's 2003 FOB share in commodity-shock product $h$ . Each product term is a statutory parameter set independently of the firm's decisions, and the 2003 portfolio weights are predetermined relative to the 2003–2011 shock, so $\tau_f^F$ is predetermined; it also lives in the same shift-share space as the firm shock. In the commodity-exporter sample, $\tau^{F}$ splits cleanly into net-subsidy firms (Reintegro/Drawback-eligible, $\tau^{F} > 0$ ), zero-wedge firms (mining, primary copper, raw agriculture, $\tau^{F} \approx 0$ ), and net-restriction firms (fisheries and aquaculture, $\tau^{F} < 0$ ).

Scope and caveats. The measure is statutory-imputed (rate × eligibility), not realized refunds or duties, and it captures explicit instruments only. Implicit support—state financing for the national copper producer, DL 600 tax stability for foreign miners, sectoral promotion through ProChile and CORFO—is not measured, reinforcing the lower-bound interpretation. We exclude the copper-export levy (Cobre Reservado, Law 13,196) because by statute it falls on a single firm whose net position is confounded by unmeasured state support.

## C.3 The Wedge Predicts Differential Expansion

If $\tau_{f}^{F}$ captures a genuine export advantage, firms with a higher net wedge should expand exports more when the shock hits—the misallocation prediction. On the cross-section of commodity exporters we estimate

$$
g _ {f} = \beta \operatorname{shock} _ {f} + \delta \tau_ {f} ^ {F} + \gamma (\operatorname{shock} _ {f} \times \tau_ {f} ^ {F}) + \alpha_ {h (f)} + \varepsilon_ {f},
$$

where $g_{f}$ is 2003–2011 export growth (Davis–Haltiwanger–Schuh mid-point growth) and $\alpha_{h(f)}$ are fixed effects for the firm's dominant 2-digit sector, with standard errors clustered at that level; the wedge is centered. The prediction is $\gamma > 0$ . Table A.5 confirms it: comparing firms within the same broad sector, those with a more favorable net wedge expand exports significantly more when the shock arrives. The effect is robust to dropping the normal-channel multiplier $s^{norm}$ and to winsorizing the outcome at the 1st and 99th percentiles. Decomposing the wedge, the net effect is driven by the restriction (implicit-tax) side; the subsidy side has little cross-firm variation in this sample and is imprecisely estimated. Identification compares firms within the same broad (2-digit) sector, which is the level at which the wedge varies across firms: the wedge differs mainly across narrow product lines within a sector, so this is the appropriate comparison.

Table A.5: Export Wedge × Commodity Shock and Firm Export Growth

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td colspan="4">Dependent variable: firm export growth</td></tr><tr><td>Shock × net wedge</td><td>4.18**(1.96)</td><td>4.27**(2.04)</td><td>4.17**(1.95)</td></tr><tr><td>Drop  $s_{norm}$  multiplier</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Winsorized outcome (1/99)</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Dominant-HS2 FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Firms</td><td>760</td><td>760</td><td>760</td></tr></table>

Notes. Dependent variable: firm export growth (DHS mid-point growth, 2003–2011). Cross-section of commodity exporters. The firm net export wedge (subsidy minus restriction) is built from four predetermined statutory programs and aggregated to the firm by 2003 export shares (Appendix C.2); it is centered. Each column regresses export growth on the commodity shock, the net wedge, and their interaction, with dominant-HS2 fixed effects and standard errors clustered by dominant HS2. Column (2) drops the normal-channel multiplier $s_{norm}$ ; column (3) winsorizes the outcome at the 1st and 99th percentiles. A positive interaction is the misallocation prediction: firms with a more favorable wedge expand more when the shock arrives. $* * * p < 0.01$ , $**p < 0.05$ , $*p < 0.10$ .

![](images/5624899e3108d2f40c0d66e2ff4873d4807f102ec6dbc15b5adb82130e2a26dc.jpg)

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
