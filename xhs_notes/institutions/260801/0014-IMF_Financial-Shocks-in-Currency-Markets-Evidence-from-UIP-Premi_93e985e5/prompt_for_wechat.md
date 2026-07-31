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
# Financial Shocks in Currency Markets:

Evidence from UIP Premia

Prepared by Ece Özge Emeksiz, Andrés Fernández, Nikhil Patel, Ivan Petrella, and Tatjana Schulze

WP/26/162

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/f2a02f7d467adf9fafb436359002377e94d89493f992e5ed3146201a53686269.jpg)

# IMF Working Paper Research Department Financial Shocks in Currency Markets: Evidence from UIP Premia Prepared by Ece Özge Emeksiz, Andrés Fernández, Nikhil Patel, Ivan Petrella, and Tatjana Schulze\*

Authorized for distribution by Emine Boz
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper proposes a sign-narrative VAR approach to identifying financial shocks in currency markets. The approach imposes minimal sign restrictions shared across canonical exchange rate models, leveraging their key insights while remaining robust to misspecification relative to structural models typically used in the literature. To sharpen the identification, sign restrictions are complemented with narrative restrictions anchored on episodes of well documented FX market dysfunction. Focusing on two emerging economies (Brazil and Chile), our estimates suggest that financial shocks account for about one third of UIP fluctuations, and contribute less than 10% to the variance of macro variables including output and inflation. While infrequent, when they do materialize, financial shocks trigger sharp declines in output, suggesting economically meaningful spillovers from frictions in currency markets to the real economy.

RECOMMENDED CITATION: Emeksiz, Ece Özge, Andrés Fernández, Nikhil Patel, Ivan Petrella, and Tatjana Schulze. 2026. “Financial Shocks in Currency Markets: Evidence from UIP Premia” IMF Working Paper, WP/26/162, Washington, D.C.

<table><tr><td>JEL Classification Numbers:</td><td>F32, F41</td></tr><tr><td>Keywords:</td><td>Exchange rates; financial shocks; uncovered interest parity; narrative VARs</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>eemeksiz@imf.org; afernandez3@imf.org; npatel@imf.org; ivan.petrella@carloalberto.org; tschulze@imf.org;</td></tr></table>

# Financial Shocks in Currency Markets: Evidence from UIP Premia \*

Ece Özge Emeksiz $^{*}$ , Andrés Fernández $^{*}$ , Nikhil Patel $^{*}$ , Ivan Petrella $^{**}$ , and Tatjana Schulze $^{*}$

\* International Monetary Fund

\*\* Collegio Carlo Alberto, University of Turin and CEPR

July 16, 2026

## Abstract

This paper proposes a sign-narrative VAR approach to identifying financial shocks in currency markets. The approach imposes minimal sign restrictions shared across canonical exchange rate models, leveraging their key insights while remaining robust to misspecification relative to structural models typically used in the literature. To sharpen the identification, sign restrictions are complemented with narrative restrictions anchored on episodes of well documented FX market dysfunction. Focusing on two emerging economies (Brazil and Chile), our estimates suggest that financial shocks account for about one third of UIP fluctuations, and contribute less than 10% to the variance of macro variables including output and inflation. While infrequent, when they do materialize, financial shocks trigger sharp declines in output, suggesting economically meaningful spillovers from frictions in currency markets to the real economy.

JEL No. F32, F41

Key words: Exchange rates; financial shocks; uncovered interest parity; narrative VARs

## 1 Introduction

A central question in open-economy macroeconomics is how much of exchange-rate variation reflects shifts in macroeconomic fundamentals versus movements in financial conditions that are orthogonal to fundamentals and alter currency risk premia and market functioning. The answer is pivotal for both positive and normative reasons. Positively, it bears directly on the interpretation of the ubiquitous failure of uncovered interest parity (UIP) and the forward-premium anomaly (Fama, 1984). Normatively, it delineates appropriate targets of policy—including when foreign exchange intervention (FXI), liquidity operations, or macro-financial tools are warranted to address price wedges such as currency premia, as opposed to fundamental imbalances.

As recent theoretical work emphasizes, exchange-rate premia (UIP deviations) are key sufficient statistics for the optimal design of FXI when intermediaries face balance-sheet constraints or risk-bearing limits. $^{1}$ At the same time, a sizable component of measured UIP deviations may reflect macroeconomic fundamentals, for example sovereign risk, time-varying disaster risk, or trade-related rebalancing forces (e.g. Bodenstein et al., 2024). Empirically, however, distinguishing fundamental from financial forces has proven challenging. $^{2}$

This paper develops and implements a structural Vector Autoregression (SVAR) with narrative sign restrictions, building on the methodology of Antolin-Diaz and Rubio-Ramirez (2018) that isolates financial (non-fundamental, frictional) shocks in the foreign-exchange market and quantifies their importance for UIP deviations, exchange rates, and macro aggregates. By financial shocks, we mean disturbances that tighten intermediation capacity, impair price discovery, or generate wedge-like currency premia, as distinct from fundamental drivers such as productivity, demand, monetary policy, or trade shocks. An example of such a shock is when exchange-rate overreaction is driven by liquidity strains in FX markets and rapid portfolio shifts as investors rush to unwind positions, motivated by beliefs about what others will do rather than by changes in underlying fundamentals—consistent with self-reinforcing market dysfunction.

Our identification strategy has two pillars. First, we impose a minimal set of impact sign restrictions on the components of the UIP deviation—the interest rate differential and expected depreciation—that is shared across canonical models with intermediary constraints. Financial shocks in these models generate a negative co-movement between these components, so that larger differentials forecast appreciation, simultaneously raising the UIP deviation and depreciating the currency. Fundamental shocks generally imply the opposite co-movement. Second, to overcome the "shock masquerading" problem of pure sign-restricted SVARs, we refine identification with narrative sign restrictions. Such restrictions are grounded in episodes of market dysfunction for which well documented narratives from central banks and market participants exist and point to the presence of financial shocks unrelated to market fundamentals.

Our approach of using narrative information to identify financial shocks is deliberately broad and multi-layered. We begin with a detailed case study of Chile's 2019 social unrest. The episode is particularly informative since official Central Bank reports and market analysts documented exchange-rate decoupling from usual fundamentals, liquidity strains, and broader market dysfunction, offering a clear narrative anchor for our identification of a financial shock. We then extend the narrative analysis systematically to Chile and Brazil over the past two decades—a period that combines inflation-targeting frameworks with deep FX markets in both economies as well as episodes of large and volatile UIP premia. In this broader exercise, we combine quantitative screening—such as the statistical identification of sharp and rapid exchange-rate depreciation episodes—with a two-step narrative pipeline. First, we rely on large language models (LLMs) to triage a large corpus of central bank and market based reports related to these episodes, and extract candidate passages that meet minimal relevance criteria (using targeted keywords and guiding questions). Second, we subject the LLM-filtered excerpts to expert review and human scoring by the research team, which determines whether each episode contains narrative evidence consistent with non-fundamental, frictional disturbances in currency markets related to the exchange-rate depreciation episodes. This design scales coverage while preserving a transparent, human-coded final classification, and yields narrative anchors that are both comprehensive and tailored to each countrys institutional context.

We estimate the SVAR with narrative-sign restrictions at a monthly frequency for Chile and Brazil. The observable vector includes the UIP premium and its components (interest differentials, expected depreciation), nominal depreciation, output and inflation, policy rates, net capital flows, FX bid-ask spreads, and measures of CIP deviations. Including CIP premia and bid-ask spreads allows us to cross-validate episodes of intermediation stress and differentiate financial from fundamental drivers in a disciplined yet parsimonious way.

Empirically decomposing exchange-rate movements and UIP premia into fundamental and financial drivers is central to several active debates. Recent structural and semi-structural work reaches divergent conclusions: some models imply that financial forces account for a large share of exchange-rate variation, while other contributions attribute large roles to trade rebalancing or demand shocks, with financial shocks appearing more important only at high frequency. On the empirical side, agnostic/max-share approaches have uncovered non-trivial roles for productivity or hard-to-classify financial shocks in real exchange-rate dynamics. In parallel, a growing body of evidence documents the behavior of UIP premia across advanced and emerging economies and their links to local and global risk, policy, and institutional features. $^{3}$ This paper contributes to this debate by delivering a conceptually tight and empirically robust identification of the financial component of nominal exchange-rate movements through the lens of UIP premia, while remaining agnostic about whether the underlying stress is local or global. Methodologically, we combine minimal theoretical structure (shared sign implications across models) with curated narrative anchors. Our use of narrative sign restrictions, systematically extracted from policy documents and market intelligence using a combination of quantitative, manual, and LLM-based methods, sharpens identification in macro-finance VARs relative to purely sign-restricted approaches.

Three findings stand out from our analysis. First, the identified financial shock explains roughly one-third of the variance of the UIP premium and about one-half of the variance of monthly nominal exchange-rate depreciation in Chile. By comparison, the shock accounts for less than 10 percent of the variance of output and inflation. In Brazil, the same ordering holds, although the contrast is somewhat less stark. These magnitudes are economically large for FX variables yet modest for macro aggregates, consistent with the exchange-rate disconnect emphasized in theory, but smaller than the large shares implied by some canonical models. $^{4}$

Second, the tightening in financial conditions that raises currency premia induces a statistically and economically significant short-run contraction in economic activity. The pass-through to prices and policy responses differs across countries: in Chile, prices rise on impact and the policy rate tightens, whereas in Brazil near-term price pressure is weaker and the policy rate eases. Indicators of market functioning corroborate the mechanism: FX bid–ask spreads widen strongly in Chile, whereas CIP deviations respond more sharply in Brazil. We discuss how this is consistent with evidence of institutional microstructure differences.

Third, narrative anchors markedly sharpen the results relative to sign-only identification. They eliminate rotations that understate the role of financial stress during well-documented episodes of market dysfunction, strengthening the estimated output response and raising the contributions to UIP and exchange-rate variation without mechanically increasing macro responses.

Our estimates occupy a middle ground relative to the literature discussed above. They imply a larger role for frictional forces than studies that ascribe most exchange-rate variation to fundamentals such as trade rebalancing or demand shocks, yet smaller shares than those implied by structural frameworks in which intermediary constraints almost entirely dominate exchange-rate dynamics. This pattern fits a synthesis view: financial shocks are episodically dominant for FX variables, especially during stress and intervention windows, but fundamentals remain the primary drivers of macro aggregates. Our historical decompositions make this episodic nature explicit.

There are three advantages to our identification strategy that relies on a disciplined, model-consistent set of sign restrictions with narrative anchors. First, it is robust to misspecification: we do not hard-wire a single equilibrium mapping from shocks to observables or rely on tight parametric priors over key elasticities and adjustment cost parameters that are hard to identify from macro data. Second, it is portable and transparent: the same minimal sign logic applies across countries and is easy to audit, while the narrative events are documented by policymakers and market participants. Third, it is designed for the object of interest: by focusing on the UIP premium and its components (and, in extensions, CIP premia and bid-ask spreads), we directly target the friction that policy would plausibly seek to offset.

Our approach is intentionally scoped. First, it delivers shock-level counterfactuals but not a full general-equilibrium welfare mapping and hence does not by itself pin down optimal policy rules. Second, since it relies on the availability and quality of narrative classification as well as human validation, it is more resource-intensive to scale to a large set of countries. Third, while narrative restrictions mitigate the shock-masquerading risk inherent in sign-only SVARs, identification remains set-valued by construction, and the approach retains the usual VAR sensitivity to specification choices, including variable selection, horizon, and lag length. Finally, because we use monthly data to integrate macro aggregates with financial indicators, we cannot examine dynamics at higher-than-monthly frequency (e.g., daily or weekly), and such movements are necessarily averaged out in our framework.

While we do not conduct welfare analysis or evaluate specific policy rules, our results speak to a growing theoretical literature in which financial shocks orthogonal to fundamentals drive wedges in currency markets, providing a rationale for FXI (Adrian et al., 2021; Basu et al., 2025). In such environments, interventions that target liquidity and risk-bearing constraints—FX swaps, sterilized spot operations, and funding backstops—can be welfare enhancing precisely because they compress inefficient premia. Our framework thus provides an empirically disciplined way to identify and quantify the non-fundamental financial shocks that can give rise to such inefficiencies. In this sense, our work expands the empirical toolkit available for assessing when and through which channels FX and related financial policies may be appropriate.

The remainder of the paper is organized as follows. This section concludes with a brief overview of the related literature. Section 2 describes the methodology in detail, introducing the theoretical sign logic for distinguishing financial from fundamental shocks, and motivating and describing the full set of narrative restrictions used in the analysis. Section 3 describes the data and estimation procedure. Section 4 presents the main results—impulse responses, variance decompositions, and historical decompositions—and quantifies the contribution of financial shocks to UIP premia and exchange rates, benchmarking against the literature. Section 5 concludes with a summary of the main messages.

## Related literature.

Exchange rate theory. This paper complements the growing theoretical literature that highlights the role of frictions faced by intermediaries in currency markets in driving exchange rates away from macroeconomic fundamentals (Gabaix & Maggiori, 2015; Itskhoki & Mukhin, 2021). These models provide a unifying theory for the well-documented failure of the UIP condition to hold (Backus et al., 2001; Engel, 2016; Fama, 1984; Meese & Rogoff, 1983). They also delineate avenues for optimal exchange rate policy that render the UIP premium—a barometer of inefficiencies in FX markets—a key object of interest in the rationale for foreign exchange intervention (FXI) (Adrian et al., 2021; Basu et al., 2025) and targeted policies that help relax domestic financing constraints (Acosta-Henao et al., 2025). However, while UIP premia may signal limits to the risk-bearing capacity of financial intermediaries, they may also capture shifts in fundamentals (Bocola & Lorenzoni, 2020; Verdelhan, 2010), including sovereign risk, and other risks such as rare disasters (Farhi & Gabaix, 2016). In fact, Bodenstein et al. (2024) attribute 50% of exchange rate fluctuations to trade rebalancing, while only 20% of fluctuations stem from exogenous changes in UIP premia that can be linked to financial frictions. Kekre and Lenel (2024) in turn find a significant role for demand shocks, operating through interest rate differentials, in accounting for 75% of the variation in G10 currency pairs, while financial shocks matter only at higher frequency. We add to this debate by offering a novel approach to tease out fundamental from non-fundamental—or “frictional”—shocks to exchange rates through the lens of UIP premia, focusing on two EMs.

Methodology. A related body of work then empirically explores origins of exchange rate movements through (semi-)structural approaches. Miyamoto et al. (2023) and Chahrour et al. (2025) use max-share identification—an agnostic statistical approach imposing little structure—to uncover the dominant drivers of exchange rates. They find a significant role of productivity shocks (Chahrour et al., 2025) and financial shocks that are unexplained by the usual business cyc

[中间内容因长度限制已省略]

dollar, and frictions in international capital markets. In G. Gopinath, E. Helpman, & K. Rogoff (Eds.), Handbook of international economics: International macroeconomics, volume 6 (pp. 147–197). Elsevier. https://doi.org/10.1016/bs.hesint.2022.03.001

Engel, C. (2016). Exchange rates, interest rates, and the risk premium. American Economic Review, 106(2), 436–474. https://doi.org/10.1257/aer.20121365

Fama, E. F. (1984). Forward and spot exchange rates. Journal of monetary economics, 14(3), 319–338.

Fanelli, S., & Straub, L. (2021). A theory of foreign exchange interventions. The Review of Economic Studies, 88(6), 2857-2885.

Fang, H., Li, M., & Lu, G. (2025). Decoding china's industrial policies (tech. rep.). National Bureau of Economic Research.

Farhi, E., & Gabaix, X. (2016). Rare disasters and exchange rates. Quarterly Journal of Economics, 131(1), 1–52. https://doi.org/10.1093/qje/qjv040

Gabaix, X., & Maggiori, M. (2015). International liquidity and exchange rate dynamics. Quarterly Journal of Economics, 130(3), 1369–1420. https://doi.org/10.1093/qje/qjv016

Garcia, M., Medeiros, M., & Santos, F. (2014). Price discovery in brazilian fx markets (tech. rep.). Texto para discussão.

Goldman Sachs. (2002, June 14). Brazil: A few ideas to stabilize local financial markets (Latin America Economic Analyst No. 02/12). Goldman Sachs Global Investment Research.

Goldman Sachs. (2020, March 18). Brazil: Copom: Restarting easing with a 50bp selic cut (LATAM Today). Goldman Sachs Global Investment Research.

Goldman Sachs. (2022, July 15). Chile: A taxing tax reform and a new constitution that pleases neither left nor right (Latin America Economics Analyst). Goldman Sachs Global Investment Research.

Greenwood, R., Hanson, S., Stein, J. C., & Sunderam, A. (2023). A quantity-driven theory of term premia and exchange rates. Quarterly Journal of Economics, 138(4), 2327–2389. https://doi.org/10.1093/qje/qjad024

Hofmann, B., Patel, N., & Wu, S. P. Y. (2022). Original sin redux: A model-based evaluation. Bank for International Settlements, Monetary; Economic Department.

Inoue, A., & Kilian, L. (2020). The role of the prior in estimating VAR models with sign restrictions (Working Paper No. 2030). Federal Reserve Bank of Dallas.

Itskhoki, O., & Mukhin, D. (2021). Exchange rate disconnect in general equilibrium. Journal of Political Economy, 129(8), 2183-2232.

Itskhoki, O., & Mukhin, D. (2023). Optimal exchange rate policy (tech. rep.). National Bureau of Economic Research.

Jara, A., & Piña, M. (2022). Exchange rate volatility and the effectiveness of fx interventions: The case of chile (Working Paper No. 962). Central Bank of Chile.

Joignant, A., & Garrido-Vergara, L. (2025). Revisiting the chilean social uprising: Explanations, interpretations, and over-interpretations. Latin American Research Review, 1–12.

J.P. Morgan. (2019, November 15). Chile and ecuador (Economic Research, Global Data Watch). J.P. Morgan Securities LLC.

Kalemli-Özcan,, & Varela, L. (2025). Five facts about the uip premium (Working Paper No. No. 28923) (Revised January 2025). National Bureau of Economic Research.

Kekre, R., & Lenel, M. (2024). Exchange rates, natural rates, and the price of risk. University of Chicago, Becker Friedman Institute for Economics Working Paper, (2024-114).

Koch, K. (2007). Gibbs sampler by sampling-importance-resampling. Journal of Geodesy, 81(9), 581–591.

Korinek, A. (2025). Generative ai for economic research: Use cases and implications [Forthcoming]. Journal of Economic Literature.

Medel, C. (2018). Econometric analysis on survey-data-based anchoring of inflation expectations in chile (Working Paper No. 825). Central Bank of Chile.

Meese, R. A., & Rogoff, K. S. (1983). Empirical exchange rate models of the seventies: Do they fit out of sample? Journal of International Economics, 14(1), 3–24. https://doi.org/10.1016/0022-1996(83)90017-X

Miyamoto, W., Nguyen, T. L., & Oh, H. (2023). In search of dominant drivers of the real exchange rate. Review of Economics and Statistics, 105(4), 1–14. https://doi.org/10.1162/rest\_a\_01342

Ottonello, P., Song, W., & Sotelo, S. (2024). An anatomy of firms political speech (tech. rep.). National Bureau of Economic Research.

Patel, N., & Xia, F. D. (2019). Offshore markets drive trading of emerging market currencies. BIS Quarterly Review, December.

Robitaille, P., Zhang, T., & Weisberg, B. (2024, December). How well-anchored are long-term inflation expectations in latin america (FEDS Notes). Board of Governors of the Federal Reserve System.

Romer, C. D., & Romer, D. H. (1989). Does monetary policy matter? a new test in the spirit of friedman and schwartz. In O. J. Blanchard & S. Fischer (Eds.), Nber macroeconomics annual (pp. 121-184, Vol. 4). MIT Press.

Rubio-Ramírez, J. F., Waggoner, D. F., & Zha, T. (2010). Structural vector autoregressions: Theory of identification and algorithms for inference. The Review of Economic Studies, 77(2), 665–696.

Stavrakeva, V., & Tang, J. (2024). A fundamental connection: Exchange rates and macroeconomic expectations. Review of Economics and Statistics, 106(4), 1–49. https://doi.org/10.1162/rest\_a\_01520

Uhlig, H. (2005). What are the effects of monetary policy on output? results from an agnostic identification procedure. Journal of Monetary Economics, 52(2), 381–419.

Verdelhan, A. (2010). A habit-based explanation of the exchange rate risk premium. Journal of Finance, 65(1), 123–145. https://doi.org/10.1111/j.1540-6261.2009.01525.x

Wolf, C. K. (2022). What can we learn from sign-restricted vars? AEA papers and proceedings, 112, 471–475.

![](images/dd6499b96b77e2d3364c1e617382e226211e0f83cb4eaf78beb03a66cef56d09.jpg)

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
