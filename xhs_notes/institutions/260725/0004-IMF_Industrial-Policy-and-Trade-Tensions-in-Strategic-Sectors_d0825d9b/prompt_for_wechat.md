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
# Industrial Policy and Trade Tensions in Strategic Sectors

Lorenzo Rotunno, Michele Ruta and Priyam Verma

WP/26/155

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/f0713f22b09e4898e8b4bf4d4b22abbbb4a9004d005b51bda58d7abc940d5f6e.jpg)

# IMF Working Paper Strategy, Policy & Review

# Industrial Policy and Trade Tensions in Strategic Sectors Prepared by Lorenzo Rotunno, Michele Ruta and Priyam Verma\*

Authorized for distribution by Daria Zakharova
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper examines the global trade and welfare effects of industrial subsidies, employing a multi-country, multi-sector general equilibrium trade model with economies of scale. We first estimate the magnitude of industrial subsidies across countries relying on a novel approach that exploits information on subsidy counts during the period 2015-23. We then quantify the impact of the implied subsidy rates on trade flows and find that subsidies boost net exports in strategic sectors especially for China, while causing export declines in competing economies. Subsidies by the EU and the US produce qualitatively similar but smaller effects, as these economies target relatively more non-strategic sectors. A decomposition of the trade effects highlights the role of economies of scale and productivity changes in explaining sectoral specialization in response to subsidies. Tariff actions in 2018-19 and since 2025 partly offset these trade patterns. While targeting strategic sectors, recent subsidies and import tariffs lower global welfare by creating distortions and negative cross-border externalities.

JEL Classification Numbers: F12, F14

Keywords:

Industrial Policy; Trade Spillovers; sectoral imbalances; Geoeconomics.

Author's E-Mail Address:

Irotunno@imf.org; mruta@imf.org; priyam.verma@ashoka.edu.in

# Industrial Policy and Trade Tensions in Strategic Sectors

Prepared by Lorenzo Rotunno, Michele Ruta and Priyam Verma $^{1}$

## 1 Introduction

The recent increase in industrial policies and subsidies targeting strategic sectors, i.e., sectors that are considered of significant importance for a country's economic or national security, has spurred a debate on their effectiveness and impact on global markets (Juhász et al., 2022; Evenett et al., 2025). Although industrial policies have a recognized economic rationale in the presence of market failures (Juhász, Lane and Rodrik, 2024), their efficient targeting is difficult in practice and their repercussions on trade patterns and global prices may promote perceptions of unfair competitive advantages for subsidized firms on the international stage. In fact, governments have often adopted countermeasures such as import tariffs and retaliatory subsidies in response to trade partners' industrial policies, especially if they target strategic sectors (Bown, 2024), making the interaction between subsidies and tariffs an equally important policy question. In spite of their spillover effects and policy responses, there remains relatively little understanding of how recent industrial policy could reshape global markets, especially in more sensitive and strategic sectors.

Against this backdrop, this paper makes two main contributions. First, we introduce new estimates of industrial subsidies by sector and across countries — which cover the 2015-23 period, complementing existing measurement efforts. Second, we use these estimates as policy shocks in a quantitative multi-country, multi-sector general equilibrium trade model with external economies of scale to assess how recent subsidy changes across many countries and sectors reshape global trade patterns and welfare. We also analyze how the US-China tariff actions of 2018-19 and since 2025 interact with these subsidy trends. We remain agnostic about the WTO-consistency of the subsidy measures identified in our analysis and on the tariff actions, focusing instead on their observed trade effects irrespective of their legal framing or stated policy rationale.

In the analysis, we focus on strategic sectors, which have been at the center of geoeconomic rivalries (Clayton, Maggiori and Schreger, 2023; Aiyar et al., 2023). These sectors are dominated by large economies. As illustrated in Figure 1, panel (a), China, the EU, and the US together account for over half of global exports of strategic products — captured here by the list of Advanced Technology Products (ATPs) as defined by the US Census Bureau — which include semiconductors, industrial robots, biotech, and other high-tech items. More tellingly, their combined share of world exports of strategic products exceeds their share of world exports of all products by roughly 10 percentage points, underscoring the highly concentrated nature of these markets. The figure further highlights China’s significant role in global markets of strategic products, with a larger export share than both the EU and US, whereas China’s share is comparable to the EU and US in non-strategic products. Figure 1, panel (b), also reveals that China has implemented the largest share of subsidies targeting strategic products during the same period, based on subsidy measures recorded in the Global Trade Alert (GTA) database. By contrast, for the EU and the US the shares of subsidy measures targeting strategic products are less than half that of China.

This paper examines how subsidies — serving as the primary instrument of industrial policy — impact global markets across sectors over the long term. Our interest is in the enduring consequences of such policies. Specifically, we ask: How do recent industrial policies shape the global landscape for strategic industries? How do tariffs change the trade effects of these subsidies? And what are the implications for global efficiency and welfare? We assess the reallocation effects that these industrial policies would have in the long run, holding fixed other potentially important structural and policy-driven determinants of trade flows and aggregate efficiency.

Figure 1: Global exports of and subsidies to strategic products (2012-23 average)  
![](images/8b8ffe011e347dbf1de0c3fc6c4245c34ad6774e607710a6a9d229b661fbb1ca.jpg)

(b) Share of subsidy measures  
![](images/10ea68c6bd12d4daa97f63565fa8b02be214c3bc72a7df559cbff2381b8d6d7d.jpg)  
Note: Averages over 2012-23. Strategic products are HS products included in the US Census Bureau list of Advanced Technology Products (ATPs). In panel (a), the Rest of the World (ROW) share is an export-weighted average of each country's share of world exports (excluding CHN, EU and USA). In panel (b), subsidies are policy measures classified as 'domestic' subsidies in the GTA (i.e., excluding trade finance and export subsidy measures). We consider measures introduced since 2009 and in force in a given year which are classified by the GTA database as distorting trade flows. For subsidies without an expiry date, we assign the average duration in the sample (see Section 2 for details). Source: OECD ICIO and Global Trade Alert database.

To evaluate the impact of industrial subsidies, we utilize a quantitative trade model incorporating external economies of scale, building on Ju et al. (2024). This framework enables us to isolate the effects of subsidies not only within the subsidizing countries and targeted sectors, but also to capture cross-border spillovers affecting trade patterns in other countries and across multiple sectors. By integrating production externalities at the sector level, the model reflects the positive production spillovers commonly observed in advanced manufacturing industries (e.g., Goldberg et al. (2024)). The theoretical framework incorporates multiple countries and sectors, with firms operating under perfect competition. Production relies on a single factor of production and traded intermediate goods. Industrial policy enters the model through production subsidies and import tariffs, which generate a wedge between producer and consumer prices. In the model, the rationale for policy intervention is the correction of a market failure arising from external economies of scale: production subsidies proportional to sectoral scale elasticities target the underlying production externality (Bartelme et al., 2025; Lashkaripour and Lugovskyy, 2023). As a result, the trade effects we document arise even though subsidies are not targeted at exports, but operate instead through their impact on production costs and sectoral specialization. In the static framework of the model, policy shocks do not alter the aggregate deficit, which is held constant. Model simulations can identify policy effects on sectoral net exports through reallocation, abstracting from any possible implications for the aggregate trade balance. In the model, net government expenditure is financed by, or rebated through, lump-sum transfers to and from consumers.

In this general equilibrium setting, subsidies can influence trade patterns through three types of effects. First, in the subsidizing country and supported sectors, subsidies are expected to raise exports and lower imports, as the price of subsidized products goes down. Crucially, resource reallocation toward these sectors further reduces producer prices through economies of scale — a productivity effect that compounds the direct price-reducing effect of subsidies. In addition, subsidies can enhance competitiveness by decreasing the cost of subsidized inputs, within the same sector or from other upstream industries. These positive impacts on net exports in targeted industries can be partially offset by rising wages in the subsidizing country relative to those of other economies. Second, in sectors that receive lower subsidies, the reallocation mechanism operates in reverse, leading to declines in net exports. Third, subsidies are expected to lower exports by trading partners with lower subsidies in the same targeted sectors. By effectively acting as import barriers, subsidies reduce exports to the subsidizing countries. They also undermine exports from non-subsidizing countries to third markets, as exports from the subsidizing countries become globally more competitive. These export-reducing cross-border spillovers may be partially mitigated in a general equilibrium setting, as factor prices increase in the subsidizing country and imported subsidized inputs lower production costs.

Unlike recent quantitative studies that rely on hypothetical subsidy scenarios (Ju et al., 2024; Hodge et al., 2024; Bartelme et al., 2025; Lashkaripour and Lugovskyy, 2023), we offer a quantitative assessment of the trade effects stemming from actual recent subsidy trends across countries and sectors. The global coverage of the subsidy data allows us to evaluate the cross-country spillovers from industrial policy. Our subsidy rate estimates, covering the period 2015-23, are derived using a two-step empirical methodology that combines data from the New Industrial Policy Observatory (NIPO) and the Global Trade Alert (GTA). First, a 10-fold cross-validation procedure (James et al., 2013; Zhang, 1993) is applied to NIPO data for 2023-24 to identify the most accurate predictive relationship between subsidy rates (measured per dollar of output) and subsidy policy counts at the sector level. This relationship is then used to estimate annual subsidy rates, by leveraging GTA policy counts from 2009 to 2023. This approach represents a novel attempt to quantify the scale of industrial subsidies across countries and sectors. $^{1}$ The predicted subsidy rates we obtain compare fairly well with the admittedly few estimates of subsidies available in the literature (Garcia-Macia et al., 2025; OECD, 2025a; European Commission, 2025) despite some well-known limitations in the GTA data, such as the lack of legacy subsidies introduced before 2009 and the recording of separate firm- and region-specific interventions that could in reality belong to the same policy. As mentioned above, we employ the set of HS products defined as Advanced Technology Products (ATPs) by the US Census Bureau to identify strategic sectors. While the precise definition may well vary across countries and over time, the list has the merit of capturing sectors that the US authorities consider of special interest and that are often referred to in public debates as being of strategic importance, such as electronics, robotics, and biotechnology. Aggregated sectors in the model simulations are considered strategic if they include at least one product classified as ATP.

Consistent with evidence in Figure 1, China has the highest aggregate subsidy as a share of value added in goods sectors, with subsidies averaging 1.8 percent between 2015 and 2023. In comparison, the US and the EU exhibit relatively lower subsidy rates at around 1.3 and 0.6 percent respectively. Interestingly, estimated subsidy rates have increased more strongly in strategic sectors, with important differences across countries. Globally, while subsidy values as a share of value added were at around 0.5 percent in 2015 for both strategic and non-strategic sectors, they rose to 1.8 percent within strategic sectors and to 0.9 percent in other sectors in 2023. This global relative increase in subsidies to strategic sectors is driven by China, where the increase in the subsidy rate in strategic sectors is more than three times the increase observed in other industries. In the EU and the US, the increase in subsidies to strategic sectors is weaker as their policies target other sectors such as agriculture and mineral products.

We simulate the trade effects of the estimated changes in subsidy rates during 2015-23 using our quantitative trade model. The model is calibrated with 2015 data on trade, value added, and input-output linkages from the OECD Inter-Country Input-Output (ICIO) tables (OECD, 2025c), for the ten largest subsidizers and a rest-of-the-world (ROW) aggregate. The economy is divided into 20 sectors, including a services aggregate, with 8 sectors defined as strategic since they contain at least one product in the ATP list. The trade and scale elasticities are drawn from Giri, Yi and Yilmazkuday (2021) and Bartelme et al. (2025). $^{2}$ We first introduce observed subsidies from China, the US, and the EU individually, and then jointly incorporate subsidy changes from all countries in the sample. In extended analyses, we also incorporate import tariff changes between the US and China during the 2018-19 period of heightened trade tensions, and the tariff changes since February 2025.

The simulation results quantify the trade effects of subsidies highlighted in the theoretical framework, and underscore the significant long-term impact of China's subsidies on trade patterns across sectors. In a scenario where only China implements the estimated 2015-23 subsidy changes — holding everything else fixed relative to a 2015 baseline — its exports in strategic sectors rise by approximately 12 percent. In contrast, when only the EU or only the US implements their own estimated subsidy changes, the subsidizing country's strategic-sector exports increase by around 2 percent. The asymmetry largely reflects the different targeting of subsidies by China, the EU, and the US, coupled with differences in the strength of economies of scale, which are stronger in sectors targeted by China's subsidies. Therefore, subsidies by the EU and the US still meaningfully reshape trade flows, but more so in non-strategic sectors, reflecting where these countries direct a larger share of their subsidies. The trade effects observed under the China-only subsidy scenario are largely confirmed in a scenario that incorporates subsidy changes from all countries in the sample. China's share of world exports of strategic products rises to around 29 percent, while other countries experience declines in their market shares. This dynamic impacts sectoral trade balances. China's net exports in strategic sectors increase while others' decline, with the opposite pattern emerging in non-strategic sectors, consistent with resources being reallocated away from non-strategic toward subsidized sectors.

These outcomes are driven by China's specialization in strategic sectors such as electronics and pharmaceuticals in response to subsidies. In a scenario where all countries implement the 2015-23 subsidy changes, China's electronics exports increase by around 20 percent over the long term, while exports in other non-strategic sectors such as agriculture and textiles decline. Consequently, strategic sectors exhibit pronounced export spillovers: the EU and US experience export reductions of around 1 percent overall, and up to 7 percent in electronics. Under the same subsidies scenario, the EU and the US instead expand net exports mainly in non-strategic sectors with weak economies of scale, such as agriculture.

A decomposition of the trade effects of subsidies reveals that economies of scale and the associated productivity responses are important drivers behind the specialization patterns. A conceptual contribution of our analysis is a distinction between the partial-equilibrium price-reducing effect of subsidies and the other general equilibrium effects, including notably changes in sectoral productivity due to economies of scale. Our results indicate that China's expansion in the electronics sector — and the corresponding decline in exports from other countries — is primarily driven by shifts in sectoral employment and the associated productivity gains induced by subsidies. $^{3}$ Across all sectors and subsidizing countries, input-output linkages tend to amplify trade responses through lower input prices, while higher subsidy-led competition in foreign markets attenuates export expansions.

We extend our counterfactual analysis by incorporating the US-China tariff increases implemented during 2018-19, and the recent US tariff actions since February 2025 and the response by China. These are the most significant tariff policy shifts since 2015 (and since the tariff hikes of the inter-war period), and the implementing countries have at times framed them as a response to the need to

[中间内容因长度限制已省略]

<tr><td>USA</td><td>7.2</td><td>3.5</td><td>0.4</td><td>1.1</td><td>0.1</td><td>-1.5</td><td>0.9</td><td>0.9</td></tr></table>

Note: Percent changes in trade flows in goods sectors evaluated at producer prices (net of tariffs and subsidies), under a scenario where all countries and the ROW aggregate implement the estimated 2015-23 subsidy changes.

Figure A.8: World markets in electronics at baseline and under a counterfactual with subsidy changes by all countries

(a) Share of world exports  
![](images/e93ec58707e3cc14430b64be688f6dc23c2f9e9ae7b8a7ecfa963622827ac2e3.jpg)

(b) Net exports (in billions USD)  
![](images/573a5b18a798412a1c9dc397e886cf4e4f8395d2a27832911c946876d7684e1a.jpg)  
Note: Values at baseline are computed from the OECD ICIO data for the year 2015. World exports and net exports are computed for the electronics sector only.

Figure A.9: Simulated changes (in %) in exports and imports — alternative elasticities  
(a) No economies of scale  
![](images/0f8ea2b9bde6c9dbd1834c6513dae7985101caff761c2e059048e682f13d1f36.jpg)

(b) Higher scale elasticities from Bartelme et al. (2025)  
![](images/d83d58596858392a8c7b991fcdcca0eb6bf97c12a0abd160d3d8837779547ed5.jpg)

(c) Scale and trade elasticities from Lashkaripour and Lugovskyy (2023)  
![](images/d83a4fcb43eddb929bd7400a0f01fcda4eee8d048f037d02f01033df65dc9920.jpg)  
Note: Percent changes in trade flows in goods sectors evaluated at producer prices (net of tariffs and subsidies), under a scenario where all the ten largest subsidizers and ROW implement the estimated 2015-23 subsidy changes. In Panel (a), scale elasticities are set to zero for all sectors. In Panel (b), scale elasticities are as in column (7) of Table A.1, and Table 1 in Bartelme et al. (2025). In Panel (c), trade and scale elasticities are as in columns (5) and (8) of Table A.1 and Lashkaripour and Lugovskyy (2023).

Figure A.10: 2026-2015 changes in import-weighted average tariffs and scale elasticities  
![](images/6f05a2a2ebbbb4fb2ae6bfa8b0a28cfc736bf0dae310f47c0d9467be07bedf4d.jpg)

(b) US tariffs  
![](images/ffc3f5ea19fccd530f687e4e126ae246b50dcb2ac7836da9377c6eecd383cd80.jpg)  
Note: Import-weighted average tariffs using 2015 import values as weights. Tariffs on imports from all countries. For China, only tariffs on imports from the US have been updated to their levels as of March 2026.

Figure A.11: Import-weighted US import tariffs by sector (in percent)  
![](images/8c3f8c86383db31552e6d3a879aab17b3b73cca67f96a3263bef6564096b5206.jpg)  
Note: Simple average applied tariffs at the HS 6-digit product level are aggregated using import weights from the CEPII BACI database in 2015.

Figure A.12: World markets in strategic sectors with China and US tariffs  
(a) Share of world exports  
![](images/25ca6e1a7cfd218818e36dd2ec0c64d90ddf4031f84903927f37bf899942aa44.jpg)

(b) Net exports (in trillions USD)  
![](images/aa664a7672ccb09431ba7cc0bff8c244e032b564b288d056e7af3415a60fe258.jpg)  
Note: Baseline values are computed using data from the OECD ICIO for the year 2015. The “subsidies” scenario includes the estimated 2015-23 subsidy changes by all countries. The “subsidies + 18-19 tariffs” scenario adds bilateral US-China import tariffs changes as during the 2018-19 US-China trade tensions. The “subsidies + 18-19 tariffs + 25 tariffs” further adds US and China tariff changes since February 2025, so that the counterfactual US and China tariffs are as of March 2026.

Figure A.13: Simulated changes in China's and US sales by destination (in %)  
(a) China's sales  
![](images/98a072b82ac77ff8d2d47eb7fdd759fa610a61d0b683fa698b64c981996fcb28.jpg)

(b) US sales  
![](images/0ab5c8dca3125ccc8096ac00c57e6e4cda6b8c936a034624a4baf0b06a22fe26.jpg)  
Note: Percent changes in trade flows in goods sectors evaluated at producer prices (net of tariffs and subsidies), under a scenario where all countries implement the estimated 2015-23 subsidy changes, a scenario where the US and China apply import tariffs at their post 2018-19 levels, and another scenario where the two countries apply import tariffs as of March 2026 (see Figure 9).

Figure A.14: Simulated changes in real wages and income (in %) — No economies of scale  
![](images/8f66f9b15bee470037a631127300f5389562ff98ab4db9aaa8b268413c22c326.jpg)

(b) Real income  
![](images/022ebf636b9932e6fc04a4d0733a770ff98ce6c691673b108f5e22330106452a.jpg)  
Note: Model calibrated with scale elasticities set to zero for all sectors. Horizontal dashed lines are world averages, computed using real GDP in 2015 as weights.

Figure A.15: Simulated changes in real wages and income (in %) — Higher scale elasticities  
(a) Real wages  
![](images/9c698a66d5d740bf08926459f6eb549b2fb04f55ffbb6c7b749bb87298f77da3.jpg)

(b) Real income  
![](images/4818d546206368d954b2e0953ed6095481cfcdc062efd254dda70aaff9cd64f2.jpg)  
Note: Model calibrated with scale elasticities as in column (7) of Table A.1, sourced from Table 1 in Bartelme et al. (2025). Horizontal dashed lines are world averages, computed using real GDP in 2015 as weights.

Figure A.16: Simulated changes in real wages and income (in %) — Trade and scale elasticities from LL (2023)  
(a) Real wages  
![](images/1749d6ec0c9ba034df665f4b0e864a77a17f02f6aeda985d522fdf9a1301f108.jpg)

(b) Real income  
![](images/80f0ba2d41d6b475980d71e156f09fd06adf6d57bb56a5eef31df5e5f6ee969a.jpg)  
Note: Model calibrated with trade elasticities as in column (5), and scale elasticities as in column (8) of Table A.1, sourced from Lashkaripour and Lugovskyy (2023). Horizontal dashed lines are world averages, computed using real GDP in 2015 as weights.

![](images/e02569bf504b36a1b4421be6691b05fd50ef85bb38a89e388036f9ef1126e92e.jpg)
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
