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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
BCG

# European Chemicals 2030–2040

Strategic Pathways to Rebuild Advantage

June 2026

By Jan Friese, Jan Beier, Hubert Schönberger, Christian Hoffmann, Julia Meisel, and Katarzyna Raszka

## BCG

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

## Table of Contents

03 Executive Summary
04 A Structural Shift in Industry Economics
06 The Diverging Outlook Across Chemical Segments
07 A Limited Spectrum of Future Outcomes
09 Strategic Choices Become More Selective
10 Business Model Evolution
12 Building Resilience Through No-Regret Moves
14 Conclusion

![](images/2d8c565d0b536eae0065f20e5d443b264095bb29d43b17163f57a99e12dc5e5a.jpg)

# Executive Summary

The European chemical industry is undergoing a structural reset. In recent years, higher energy and feedstock costs, tighter regulation, persistent global overcapacity, and shifting demand patterns have steadily eroded Europe's competitive position. These pressures are not cyclical. They reflect lasting changes in the economics of the chemical industry and in where value is created.

In Q2 2026, the global disruption to oil supply routes caused by developments in the Middle East resulted in an improvement in the competitive position of European chemical producers. This was largely due to tighter supply-demand balances worldwide and the renewed willingness of domestic customers to pay higher prices for reliable European supply. However, the improvement should be viewed as a temporary upturn rather than a structural recovery, given that the main problems facing European producers - weak demand, high input costs, global overcapacity, and lower-priced competition from Asia and the Middle East - remain unresolved.

The effects of Europe's structural reset are already visible in lower plant utilization, margin pressure, closures, and divestments. Between 2020 and 2025, European utilization rates were roughly 10 percentage points below the 2015–2020 average. Yet the impact of these forces has been uneven. Differentiated, defensible segments with stronger innovation or customer proximity remain comparatively resilient, while energy-intensive and globally traded valuechains face a much tougher challenge to stay competitive. Portfolio averages are becoming less useful, and legacy assumptions about integrated value chains are under pressure. Strategic choices increasingly need to be made segment by segment and, in some cases, asset by asset.

Uncertainty persists, but the set of plausible industry outcomes is narrower than it might appear at first sight. Current trajectories suggest that competitive disadvantages among players could become visible across most major value chains by 2030. But by 2040, the resulting industry structure is likely to be far more entrenched. Across scenarios, the companies most likely to outperform will be those that move early to reshape their portfolios, improve structural costs, secure financially advantaged feedstock and energy, and build stronger positions in differentiated, defensible segments. Those that delay action now risk becoming trapped between rising costs and intensifying import pressures.

![](images/0049507c82bf4aa1c9f8270e5d111d45d3901b00a4bb998fe330a25899ab20a7.jpg)

# A Structural Shift in Industry Economics

The current situation is not the result of a single shock but is due to several structural shifts occurring at once. Any one of these shifts would be manageable in isolation but not when combined. Together, they are reshaping the economics of chemical production in Europe.

Global capacity expansion, but particularly in Asia, has outpaced demand growth and created sustained overcapacity across multiple value chains. This has resulted in materially lower European utilization rates, weakening the cost efficiency of capital-intensive assets.

Demand is gradually shifting toward circular and lower-carbon products, supported by regulation and customer commitments - although customer research suggests the willingness to pay a green premium remains limited and adoption is still at an early stage. However, these premiums are insufficient to offset the structural cost disadvantages faced by many European producers.

These cost disadvantages are pronounced. In 2025, European gas and power prices were still materially above those in the United States and the Middle East, with the largest impact felt in energy-intensive chains. This gap in energy prices directly affects commodity value chains where energy is a dominant cost component.

Import pressure is also becoming more visible in selected chains. In polypropylene, for example, China's share of Western European imports has increased significantly over the past decade. The absolute level remains modest, but the trend signals rising vulnerability to import-led price pressure.

Regulation adds further cost pressure. Carbon pricing under the European Union's Emissions Trading System has increased by roughly €40 per ton over the past five years, alongside broader regulatory tightening.

Taken together, these pressures create a structural competitiveness gap that incremental improvement programs will not close.

## EXHIBIT 1

## The Burning Platform | Five forces pressuring the European chemical industry

![](images/9dc73bb52637ebab31a07eee0053dd18ec73d3ee71a3aecbe46338a002c6d8ae.jpg)

Note: ME = Middle East  
Source: BCG

## Supply

## Global overcapacity & utilization pressure

\- Persistent overcapacities across value chain steps and in end markets (e.g., Auto in China)

European utilization 2020-25 down 10 ppts vs. 2015–20

## Demand

## Evolving customer needs & regional shifts

\- Trend towards circularity/ sustainability, lightweight, modularization – but not enough to counter other risks

>80% consumers are ready to accept a green premium

![](images/2de4e584b44995c4f2ddc3c21a0b8e9fa4cb805aae626fbcf3e29e55430d5faa.jpg)

## Cost competitiveness

## Feedstock & energy costs

\- Unit cost multiple times higher in Europe than in, e.g., ME or North America

European gas up to 4x more costly than US/ME, power 2x more than US in 2025

![](images/ed3ea53dc9a1a15288fa8c687cfe0d19f587b74f15a7e1e80e3a885287f00063.jpg)

## Global dynamics

## Import pressure & trade exposure

\- New trade policies reshape trade flows (e.g., US)

\- Insufficient foreign market demand drives search for alternatives

China doubled share of poly-propylene imports (3% to 6%) in Western Europe over past 10 years

![](images/9240ac320902ddb43c444d0b0be5ce4ce6c2fef54008660ed15a80325e2ca8aa.jpg)

## Policy

## Carbon & regulatory cost exposure

\- Increasing sectorial scope of Emissions Trading System (ETS)

Significant price increase of ETS 40€/ton over last five years

![](images/5189b04301a43da8fb28af839cdc862950ecab710ae5f0ee49d1ae53e74f33d3.jpg)

Select quantitative example

![](images/009b3ca950dba76beff0d98c10f02806d6d8e25246932cc21b93bafca0104e47.jpg)

# The Diverging Outlook Across Chemical Segments

The industry is separating into three broad groups: differentiated, defensible segments; pressured transition segments; and structurally exposed commodity chains.

Segments with meaningful differentiation, innovation advantages, or strong customer proximity remain relatively well positioned and, in some cases, can strengthen over time. These differentiated, defensible segments are less exposed to global price competition and better able to sustain margins.

A larger set of segments sits in a pressured transition zone. These businesses remain viable but face increasing pressure from cost disadvantages, regulatory exposure, or trade dynamics. Without active repositioning, their competitiveness is likely to erode.

Structurally exposed commodity chains face the biggest challenge. These products tend to be energy-intensive, widely traded, and difficult to differentiate.

Many polymer value chains fall into this category and are expected to remain under structural pressure.

The divergence is driven by four structural variables: energy intensity, trade exposure, end-market cyclicality, and regulatory burden. Products with high energy intensity are directly affected by Europe's cost position. Chemicals that are easily transported face stronger import competition. Exposure to cyclical industries increases demand volatility, and a high carbon footprint raises regulatory costs.

Portfolio-level averages are becoming less useful. Strategic decisions increasingly need to be made at the segment, asset, and customer level.

![](images/50920a1f0e4fbaf7149c90187067bf009430aa3ea5d9605a8742cc39752b642c.jpg)

# A Limited Spectrum of Future Outcomes

The range of plausible industry outcomes is limited, even if timing and magnitude remain uncertain. The main changes should become visible over the next decade across most value chains, with longer-term implications extending toward 2040.

![](images/aa0bba01615748122193c8302e0f2a3a7e4d70ac39e6026f98c432f2a560cbf8.jpg)

In a regionalization scenario, security of supply concerns and policy measures increase the attractiveness of European production. Utilization improves in selected value chains, although the underlying cost gap with non-European players remains. The strategic implication for European chemical companies is to prioritize assets with security of supply relevance and policy support while taking a selective approach where structural disadvantages persist.

![](images/3c6f38b70c4c825f353cd05452af9609a5e351cfcf3c6cd818c3d330e975543e.jpg)

## In a cost-convergence scenario, lower

European energy and feedstock prices narrow the competitiveness gap. However, persistent global overcapacity continues to limit margins. The implication is to use temporary input cost relief to accelerate restructuring rather than assume a return to historical margin levels.

![](images/740b9f9dbe6897406d0c86b924472007ae181ab1d14342fd383034e0f66dd002.jpg)

## In a green-premium scenario, demand

for low-carbon products grows fast enough to reward producers that can credibly differentiate themselves. Meanwhile, conventional product chains face increasing pressure. The implication is to invest selectively where willingness to pay can be demonstrated by customer segment rather than assumed at the market level.

![](images/1e61f358042271f873ab2f80a52078f17b159ec9a3023a95ef30a1983c169a0b.jpg)

In an import-intensification scenario, sustained global overcapacity drives rising pressure from imports coming into Europe, accelerating market-share erosion across exposed value chains. The implication is to exit or resize the most exposed assets early, before import pressure removes any strategic optionality.

The above scenarios differ in who captures value, where margins settle, and how quickly restructuring occurs. None, however, restores the previous equilibrium.

## Scenarios | In different future scenarios, the five forces have a varying impact on the chemical industry

![](images/255ba01abbc67c4985169d253f0b876cf84ea2eac0a7217a8621572601483732.jpg)

Supply

![](images/341b257b4ed18b175c49a37b6ca827878efc0503e7e17a9ebdf92c66fc51ebd5.jpg)

Demand

![](images/adafeace97e2dc54c8bff709407509e673d16483d28876fef80b2b197b4aaf1a.jpg)

![](images/4caecaadda65016c7d88f210320d94e976937f84739a838c6388ab853d9b28ea.jpg)

Domestic prod. priority

EU regulation encourages local production and increasing asset utilization

Customers choose domestic European supply, driven by de-risking and tariff considerations

Economic cooling results in commodity price reduction; feedstock & energy price gap closes

![](images/e69fde99dab4008568ebc5fe317361a5a3cec9adaba7396ba66f5e23c8810371.jpg)

Input price easing

Cost comp.

Overcapacity persists in European market due to domestic and global sources

Local supply is more affordable, increasing its competitiveness with imports

Europe is able to secure reliable sources of affordable energy and feedstock

![](images/69722c61a67870345e492a8cb80c8161f73c886ee9ed220369e70932dd65ef57.jpg)

Low-carbon transition

Regulation causes "green" chemicals to replace carbon-intensive; overcapacity persists

Carbon-intensive chemicals lose relative competitiveness; import pressure for "greener" alternatives remains high

Feedstock & energy price gap narrows but remains

Elimination of European overcapacity does not make up for increasing import volumes

![](images/f0ad95d4cedf4ca2f4df136c467dc81168076b7caa9ae88151552a677b5f1008.jpg)

Oversupply Influx

Feedstock and energy cost gap remains wide

![](images/6b98837661b2efd1fef5432e67c4fd278dadf48274aea3afb3106189d397263d.jpg)

Increased import pressure due to persistent overcapacities outside of Europe

Global dynamics

Internal demand grows, but exports (of end products) decline

Exposure to imports continues but they have a lower input cost advantage

![](images/55f158fc8e73f88fbd2179a8ea3ce177079c0b5d6c977e05746aa5c2d041d28c.jpg)

Carbon & regulatory cost base reduces

Carbon & regulatory cost base remains unchanged

Policy

New rules reduce carbon allocations & limit certificates, raising prices - but CBAM acts as an equalizer between domestic & foreign producers

Greater demand uncertainty due to green transition

Positive

Imports replace regional production across multiple value chain steps, affecting demand stability

Implication for European chemical industry:

Carbon & regulatory cost base is unchanged

Neutral/constant

Note: CBAM = Carbon Border Adjustment Mechanism  
Source: BCG

![](images/edf9f3d24cf89afecc47da049ddca9c56e73d18afeeb2bbd8ae5da556cc69bf7.jpg)

Negative

![](images/39ec5343711c74cc8a29ff99b8316d305a576fcfb29149d4131fb863103ee862.jpg)

# Strategic Choices Become More Selective

Broad portfolio-level strategies are giving way to segment-specific and asset-specific decisions.

For structurally exposed segments, the priority becomes disciplined value preservation rather than attempted value recovery. Actions to achieve this aim include reducing capacity, divesting assets, and resetting the cost base to limit ongoing value erosion.

For pressured transition segments, the goal is to sustain competitiveness through tighter integration, selective partnerships, and rigorous operational improvement. These measures can enhance resilience and preserve optionality.

For differentiated, defensible segments, the focus shifts toward targeted growth. Investment in innovation, applications, and capacity can reinforce competitive advantages and capture higher-value opportunities.

Across all segment types, execution discipline will determine whether strategy translates into resilience. Companies that combine cost transformation, portfolio reshaping, and operational improvement are more likely to succeed than those relying on isolated initiatives.

![](images/4321ceaee6ea45e9d86f718a6e7ac61dbef64290d99ca2094f3e660ce814f75c.jpg)

# Business Model Evolution

The industry's strategic choices are crystallizing into three business models. Each one involves a different capital-allocation logic, operating model, and partnership agenda.

![](images/9d2881ca598248a493c949d4190dda4bdaee14f1c273343db74e5e67565fd410.jpg)

The scale-driven cost leader is one model. This is built around advantaged assets, high utilization, and strict operational discipline. The model is most relevant in commoditized value chains where cost position determines long-term viability.

![](images/eea286594a1478a6f097ba8e5b9772700d24c171c307961afcdbeee251531c3f.jpg)

A second model is the integrated network player and involves using feedstock access, partnerships, and more stable downstream linkages to reduce volatility and improve resilience. This model can strengthen positioning in uncertain and fragmented value chains.

![](images/059269ef38a16e730d9acdd703931524d7932f7f61832b74475d7f82f303bff1.jpg)

A third model is the innovation-led specialist. It combines differentiated products, application expertise, and closer customer relationships to support margin quality and more stable demand.

Clarity of direction is essential. Trying to straddle all three models usually creates complexity without advantage.

Response | Three distinct business models are emerging

<table><tr><td>Impact archetype</td><td>Pressured</td><td>Exposed</td><td>Resilient</td></tr><tr><td>How to react</td><td>Scale, Efficiency, and Cost Leader</td><td>Value Chain and Partnership Optimizer</td><td>Performance and Innovation Champion</td></tr><tr><td>Core logic:</td><td>Build or consolidate capacity to achieve competitive advantage (e.g., lowest cost) and resilience; become last-one-standing</td><td>Secure advantaged feedstock or downstream access through integration; build closed and stable value chains</td><td>Focus on innovation, customization &amp; market intimacy to sustain premium margins; develop specialty products</td></tr><tr><td>Example levers:</td><td>Operational ExcellenceOpEx EfficiencyCapEx DisciplineAsset Rationalization</td><td>Chain IntegrationStrategic AlliancesDigital &amp; AIOperational Excellence</td><td>Growth InvestmentInnovation EngineDigital and AIOperational Excellence</td></tr><tr><td>Enablers required:</td><td>Asset utilizationSimple product portfoliosStable demand (regional or export to cover fix costs)Low feedstock/energy cost</td><td>Predominantly regional value chain to limit logistics costLow feedstock cost for upstream chemicals &amp; low energy cost to ensure captive value chain economics</td><td>Customer proximity &amp; technical salesInnovation capabilitiesPricing power to ensure sufficiently high margins</td></tr></table>

Source: BCG

![](images/22b0638a2a86d2d20648bc550b4eb29bf9fa2ed6e963e51af8cfe3b14cf9edb6.jpg)

# Building Resilience Through No-Regret Moves

Even when companies are faced with uncertainty, some moves make sense across virtually every plausible scenario.

The starting point for developing resilience requires a hard-nosed portfolio analysis grounded in structural economics rather than legacy assumptions. Companies need to identify where they have a sustainable advantage and where they do not, and act accordingly.

Closing the cost gap is essential, through both operational improvements and structural cost reduction. This involves improving asset utilization, reducing overheads, and increasing productivity.

Securing access to feedstocks and energy can materially improve resilience while long-term contracts, recycling, and integration can reduce exposure to volatility.

Partnerships can improve value-chain coordination and help stabilize demand in selected chains.

Better use of data and analytics can improve yields, sharpen planning, reduce downtime, and lower working capital.

None of these moves change the external environment. When combined, however, they improve resilience and expand strategic options.

# Strategic Imperative | No-regret actions required across scenarios, archetypes

## Checklist of revenue and growth actions

√ Focus portfolios on defensible value pools
Exit structurally disadvantaged products and prioritize higher-margin segments

√ Invest selectively in resilient chemicals
Allocate capital to segments with credible long-term advantage

√ Accelerate digital and AI deployment
Enhance efficiency, yield, and working capital through technology

√ Engage on trade and regulation
Actively shape policy and mitigate unfair trade exposure

## Checklist of cost and efficiency actions

√ Reset the cost base structurally
Drive productivity and overhead reduction to close competitiveness gaps

√ Rationalize uncompetitive assets
Proactively close or divest persistently underperforming capacity

√ Secure feedstock and energy positions
Improve resilience via contracts, recycling, or integration

√ Strengthen value chain partnerships
Stabilize demand and utilization through strategic alliances

![](images/726930b6ee2713d9e5ce6802634046b92b798c411b47954f7c4927300f3eae4e.jpg)

## Conclusion

The European chemical industry cannot afford to wait for a cyclical rebound. It has to adapt to a structurally different competitive environment. The forces driving change are unlikely to reverse. Consequently, players must accept that the previous equilibrium is a thing of the past.

Based on current trajectories, the winners and losers from this transformation are likely to become visible by 2030. Furthermore, by 2040, the consequences of today's capital-allocation decisions will be deeply embedded in the industry's structures.

For companies, the implication is clear. Those that continue to rely on legacy assumptions and portfolio averages will find it increasingly difficult to compete. Those that move early to reallocate capital, reshape portfolios, and build stronger positions in differentiated, defensible segments will be better placed to create value.

The question is no longer whether adjustment is needed. It is who will act quickly and decisively enough to benefit.

SIDEBAR

![](images/9c76bb3a5ec63969f903b52466307b9bd9e668d34afffaa88bbe98eafed576a3.jpg)

Geopolitical disruption and volatility in hydrocarbon markets are persistent risks for European chemical companies. Given its reliance on imported hydrocarbons, Europe is structurally exposed to rising feedstock costs and energy price shocks. In an oversupplied global market, these are difficult to pass on, resulting in margin compression. Compared to regions with access to lower-cost domestic feedstocks, Europe's competitive position may further erode. Beyond cost impacts, ongoing uncertainty also raises the risk of supply disruptions in critical inputs. Taken together, these dynamics could significantly intensify the pressure on the industry to transform.

## About the Authors

![](images/4a5b36746dff5da6017cd13085d8cd7416dc94d886fb40cc402658e818b59a00.jpg)  
Jan Friese
Managing Director and Senior Partner
Frankfurt
friese.jan@bcg.com

![](images/1a97713f835f82b112a5f01245d8dda6542ac53410d1d7a02e1e4217f06fa153.jpg)  
Jan Beier
Managing Director and Partner
Cologne
beier.jan@bcg.com

![](images/6912df11448e427298f47620dab21fb1db7dae470b9a44f0be369f0f05d9e4e2.jpg)  
Hubert Schönberger
Senior Director - Chemicals, BCG Vantage Munich
schoenberger.hubert@bcg.com

![](images/174caaeeca2c27af7da6126a710f30cd327c307abe0d25e5bda753aac64b0929.jpg)  
Christian Hoffmann
Partner and Director, Chemicals
Hamburg
hoffmann.christian@bcg.com

![](images/28e1e15c5195a7d14eea6dc2bced9fe063317ef22f605dac5e0818825e7f13a2.jpg)  
Julia Meisel
Senior Manager - BCG Vantage
Düsseldorf
meisel.julia@bcg.com

![](images/578e447299a51bfaf00ae2a99c351f195ae97c18e4830ef525ad4f1ca930ddff.jpg)  
Katarzyna Raszka
Senior Analyst - BCG Vantage
Düsseldorf
raszka.katarzyna@bcg.com
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
