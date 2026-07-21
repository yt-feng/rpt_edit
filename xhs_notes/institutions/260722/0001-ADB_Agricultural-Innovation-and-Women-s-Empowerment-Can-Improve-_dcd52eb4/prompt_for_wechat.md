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
No. 2026-11 (July)

## Key Points

• Climate vulnerability and structural gender inequality reinforce each other in Southeast Asian smallholder agriculture, generating measurable welfare, and productivity losses.

\- Standard household-level interventions fail because they ignore documented intra-household resource misallocation. Male- and female-managed plots within the same household receive unequal inputs despite identical shock exposure.

\- Three forms of agricultural innovation, i.e., biological, digital, and financial, offer evidence-based pathways to address both constraints simultaneously.

\- Immediate actions include increasing public agricultural research and development investment in women's crops, expanding price-information technology to female smallholders, and disbursing agricultural subsidies directly into women's mobile money accounts.

\- Medium-term reforms require formalizing women's land tenure rights and incorporating gender markers into regional climate finance.

# Agricultural Innovation and Women's Empowerment Can Improve Climate Resilience in Southeast Asia

Ngawang Dendup, Junior Research Economist, Asian Development Bank Institute
Raja Rajendra Timilsina, Junior Research Economist, Asian Development Bank Institute
Dil B Rahul, Vice Chair of Research and Senior Research Economist,

Asian Development Bank Institute

Marie Lotfi Fard, Master's Degree in Public Policy, University of Tokyo/Sciences Po, Paris

## INTRODUCTION

Southeast Asia's economic dynamism rests on an agricultural foundation that is under growing climate stress and constrained by persistent gender inequality. The region is among the world's most climate-exposed, with Myanmar, the Philippines, and Viet Nam regularly appearing in global climate risk indices, while agriculture employs a disproportionately large share of the female labor force. Yet the interventions commonly deployed fail to reach the women who safeguard the region's food security.

Despite agriculture's centrality to Southeast Asian economies, public investment in the sector remains inadequate. South-eastern Asia's Agriculture Orientation Index, defined as the ratio of agriculture's share of government spending to its share of gross domestic product (GDP), has stagnated since 2015, indicating that budget allocations are not keeping pace with the sector's economic and social weight (FAO 2023). Therefore, this policy brief draws on evidence from development economics to argue that climate vulnerability and gender inequality are not separate problems requiring isolated responses. They are structurally linked, and agricultural innovation offers a lever to address both simultaneously. The brief identifies five concrete interventions: increasing public agricultural research and development (R&D) investment in crops grown by women; expanding market price-information technology to female smallholders; disbursing government subsidies directly into women's private mobile money accounts; formalizing women's land tenure rights; and incorporating gender markers into regional climate finance.

## THE DUAL CONSTRAINT

development challenge well. The first constraint is climate vulnerability: rainfall variability, temperature extremes, and intensifying storms already reduce agricultural yields and income, and these impacts are projected to worsen significantly over the coming decades (IPCC 2023). The second is structural gender inequality: customary land tenure systems, biased credit markets, limited extension service access, and intra-household resource misallocation collectively prevent female farmers from operating at full productivity. Addressing these constraints in isolation leads to maladaptation.

About $75\%$ of the region's GDP depends heavily on sectors tied to natural capital, including agriculture. In Southeast Asia this dependence is particularly acute: smallholder agriculture sustains livelihoods for hundreds of millions of people, and the sector is simultaneously the region's primary source of female employment and its most climate-exposed economic activity (ADB 2025) (Figure 1).

Evidence supports that these two constraints amplify each other. When a drought strikes, households facing resource constraints tend to concentrate inputs on male-managed plots only, widening the intra-household productivity gap.

Interventions that address only one constraint will be undermined by the other. A climate resilience program that disburses resources at the household level will, under documented intra-household dynamics, reproduce existing resource allocation failures. A gender-equity intervention that does not account for climate exposure will see its gains eroded during subsequent climate shocks. Agricultural innovation is the entry point where both constraints can be addressed together.

Figure 1: Climate Vulnerability, Gender Inequality, and Maladaptation in Southeast Asian Agriculture Creates a Self-Reinforcing Hotspot  
![](images/59315ca96751807a6d0830bbc72a1a21f98e27ecd7937b97e26c222d44d8fbee.jpg)  
Source: Author.

## QUANTIFYING THE DUAL CONSTRAINT

## Climate Vulnerability and Agriculture

Southeast Asia is one of the world's most climate risk-exposed regions. Myanmar, the Philippines, and Viet Nam rank among the 10 countries most affected by extreme weather events over the past decade (Germanwatch 2026). Across the region, rainfall variability, rising temperatures, sea-level rise, and more frequent cyclones are reducing crop yields, destroying infrastructure, and pushing vulnerable households into poverty (Table 1).

For smallholder agriculture, climate shocks operate through two channels. The first is a direct productivity channel: droughts reduce yields, floods destroy standing crops, and heat stress accelerates soil moisture loss. The second is a human capital channel: resource scarcity following a climate shock has been shown to trigger gender-biased nutritional rationing, with households allocating nutrition away from daughters and toward sons, producing lasting disadvantages for girls in health and education (Maccini and Yang 2009). Agricultural income shocks further reduce human capital investment in girls by increasing their domestic labor burden and rates of early marriage (Shah and Steinberg 2017). Climate change therefore functions as a multiplier of gender inequality.

Measuring climate stress accurately matters for policy design. Precipitation-based drought indices capture historical variability well, while satellite-based tools such as the United States' National Oceanic and Atmospheric Administration Vegetation Health Index provide continuous, spatially disaggregated stress measures (Nordstrom and Cotton 2023). A combination of both approaches is appropriate for regional policy design.

## Gender Inequality and Development Pressure

Gender inequality in Southeast Asian agriculture is not only an equity concern: it is a source of aggregate inefficiency. Closing the farm productivity gender gap could increase agricultural value-added by 0.47 GDP points in lower-middle-income countries (FAO 2023). Gender-based discrimination imposes an economic cost per capita ranging from roughly \$200 in Cambodia to over \$6,000 in more prosperous economies such as Singapore, and reductions in discrimination are associated with GDP growth gains (OECD 2021).

Table 1: Top 10 Countries with the Highest Climate Risk Index Scores, 2024

<table><tr><td>Global Rank</td><td>Country</td><td>Region</td><td>Income Group</td></tr><tr><td>1</td><td>St. Vincent and the Grenadines</td><td>Caribbean</td><td>Upper-middle</td></tr><tr><td>2</td><td>Grenada</td><td>Caribbean</td><td>Upper-middle</td></tr><tr><td>3</td><td>Chad</td><td>Sub-Saharan Africa</td><td>Low</td></tr><tr><td>4</td><td>Papua New Guinea</td><td>Pacific</td><td>Lower-middle</td></tr><tr><td>5</td><td>Niger</td><td>Sub-Saharan Africa</td><td>Low</td></tr><tr><td>6</td><td>Nepal</td><td>South Asia</td><td>Lower-middle</td></tr><tr><td>7</td><td>Philippines*</td><td>Southeast Asia</td><td>Lower-middle</td></tr><tr><td>8</td><td>Malawi</td><td>Sub-Saharan Africa</td><td>Low</td></tr><tr><td>9</td><td>Myanmar*</td><td>Southeast Asia</td><td>Lower-middle</td></tr><tr><td>10</td><td>Viet Nam*</td><td>Southeast Asia</td><td>Lower-middle</td></tr></table>

\* Southeast Asian country.  
Source: Germanwatch (2026). https://www.germanwatch.org/en/cri.

The agriculture sector remains heavily female-staffed but male-controlled. In Indonesia, only 13% of women have ownership or secure rights over agricultural land, compared to 52% of men (ASEAN and UN Women 2024). Women are overrepresented in agriculture, household services, food processing, and textiles, all of which are systematically underserved by both private innovation and public extension systems (OECD 2024).

Gender gaps in access to credit, extension services, and market information further depress female farm productivity. These gaps reflect structural features of customary tenure systems, intra-household bargaining environments, and directed innovation markets rather than individual choices or differences in human capital.

with pooled resources and shared preferences. Under this assumption, it does not matter who receives an income transfer or subsidy, as the allocation outcome is assumed to be identical regardless of the recipient. Most agricultural development programs and climate adaptation packages are designed on this basis. The empirical work of 3 decades has rejected this.

Within the same household, plots managed by women yield approximately 30% less than plots managed by men, not because women are less productive farmers, but because households allocate too much labor and too little fertilizer to male-managed plots relative to female-managed ones. The estimated efficiency loss from this misallocation is equivalent to roughly 6% of total household agricultural output (Udry 1996). Farm production decisions are also driven by household demographic composition rather than by prices and technology alone, and female labor is effectively constrained to the family farm because the cost of hiring outside help is prohibitive, depressing productivity on women-managed plots (LaFave and Thomas 2016). Household-level aid is therefore likely to bypass women-managed plots, reproducing rather than correcting the misallocation the literature documents.

## WHY STANDARD SOLUTIONS FAIL

## The Unitary Household Model

The unitary household model is a standard assumption in development economics whereby all members of a household are treated as a single decision-making unit

## Structural Barriers to Female Agricultural Investment

Even where women are motivated to invest in their plots, two structural features of the institutional environment frequently prevent them from doing so.

The first is insecure land tenure. Farmers who lack secure tenure shorten fallow periods out of fear that idle plots will be claimed by others, even though fallowing is essential for soil regeneration. This constraint falls disproportionately on women, whose tenure within customary systems is often contingent on social and political status. As a result, climate adaptation strategies such as cover cropping, mulching, and controlled fallowing are effectively unavailable to female farmers with insecure tenure, since all require a credible multi-year investment horizon (Goldstein and Udry 2008).

The second is directed innovation. Private R&D investment flows toward technologies serving the largest and most profitable markets. When commercially dominant crops are exposed to temperature stress, innovation in those crops accelerates; when the same shocks affect subsistence vegetables and orphan crops, no equivalent private response materializes (Moscona and Sastry 2022). The crops that women disproportionately grow in Southeast Asian smallholder systems, including cassava, sweet potato, leafy vegetables, and legumes, have smaller market footprints and are therefore the least served by new climate-resilient varieties. This constitutes a market failure in R&D that public investment is required to correct.

## EVIDENCE-BASED INNOVATION PATHWAYS

The literature identifies three types of agricultural innovation with demonstrated capacity to address the dual constraint. Biological innovation involves the development of climate-resilient crop varieties and improved agronomic techniques targeted at the crops female smallholders grow. Digital innovation encompasses market information technologies and mobile communication tools that reduce information asymmetries between farmers and buyers. Financial innovation involves redesigning disbursement mechanisms, particularly through mobile money, to ensure that resources reach women as individual decision-making agents rather than being absorbed into household budgets outside their control.

## Biological Innovation: Correcting the Research and Development Market Failure

Private R&D investment responds to market incentives rather than social need. When temperature shocks affect commercially dominant crops, private firms develop heat-tolerant varieties; when the same shocks affect orphan crops or subsistence vegetables, no equivalent response materializes. The commercial crops that attract private investment are also the crops for which climate adaptation technologies are most available, compounding the disadvantage of female farmers.

Figure 2: Cereal Yield, Cambodia, India, Malaysia, Philippines, Thailand, Viet Nam (in kg per hectare)  
![](images/2039ec8ad74dbd8e795b8d896ec04bcda416ca664eb888f71ebbb456aa0819e6.jpg)  
Source: World Bank (2026). https://data.worldbank.org/indicator/AG.YLD.CREL.KG.

The Green Revolution illustrates both the potential and the limits of directed biological innovation. Global cereal yields rose from roughly 1.5 tons to nearly 4 tons per hectare between 1961 and 2016, driven by public and private investment in high-yielding cereal varieties (World Bank 2026). However, this gain is concentrated in wheat, rice, and maize. Horticulture, root crops, and food processing, i.e., sectors where female labor in Southeast Asia is concentrated, received a fraction of equivalent research investment. The resulting yield gap reflects not differences in farmer ability but differences in the technological resources available to different crop categories (Figure 2).

Public R&D can correct this market failure. When women participate in variety selection, the resulting seeds are better suited to the mixed-crop, risk-averse, labor-constrained farming systems that female smallholders typically manage.

## Digital Innovation: Reducing Information Asymmetries

A significant constraint on female agricultural productivity is the absence of real-time market price information, which would allow smallholders to identify the highest-value market for their produce and avoid exploitation by intermediaries who benefit from the information gap.

Table 2: Mobile Wallet Payment Usage Rates in Southeast Asian Countries

<table><tr><td>Country</td><td>Mobile Wallet Payment Usage</td><td>QR Payment Usage</td><td>Mobile Wallet Online/In-App</td></tr><tr><td>Southeast Asia (aggregate)</td><td>79%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Indonesia</td><td>92%</td><td>66%</td><td>76%</td></tr><tr><td>Malaysia</td><td>87%</td><td>68%</td><td>63%</td></tr><tr><td>Philippines</td><td>87%</td><td>n.a.</td><td>62%</td></tr><tr><td>Viet Nam</td><td>n.a.</td><td>62%</td><td>n.a.</td></tr></table>

QR = quick response.  
Source: Visa (2024). https://www.visa.com.ph/content/dam/VCOM/regional/ap/singapore/global-elements/documents/visa-cpa-2024-report-ipvmc.pdf.

Access to real-time price information has been shown to reduce price dispersion substantially, increase producer profits, and lower consumer prices, with gains persisting beyond the initial period of technology adoption (Jensen 2007). In the Philippine agricultural context, mobile phone access raises the farmgate prices that producers receive, and the gains accrue to the individual who controls the device (Lee and Bellemare 2013). Distributing price-information tools to farm households rather than to individual women will therefore not deliver the intended benefits if the device is controlled by the male household head.

## Financial Innovation: Reaching Women as Individual Agents

The third innovation pathway addresses the intra-household resource control problem. The relevant question is not how much money reaches the household but whether the delivery channel ensures that women retain control over resources intended for them.

Mobile money has been shown to allow households to smooth consumption entirely in response to negative income shocks, by reducing the transaction cost of receiving transfers from geographically dispersed network members (Jack and Suri 2014). This matters in agricultural contexts where income shocks tend to be spatially correlated: a drought affects an entire region simultaneously, making local risk-sharing networks less effective precisely when they are most needed. Mobile money extends the geographic reach of these networks. Experimental evidence further shows that disbursing funds directly into women's individual accounts significantly increases the share of resources that women retain and invest in productive activities (Riley 2022).

Mobile wallet payment usage has reached 79% across Southeast Asia, and above 85% in Indonesia, Malaysia, and the Philippines (Visa 2024). This infrastructure is already in place and can be directly leveraged for agricultural subsidy disbursement and insurance payouts without requiring new technical investment (Table 2).

## POLICY RECOMMENDATIONS

The five recommendations below are organized by implementation horizon. Immediate actions can be initiated through administrative decisions or platform-level redesign within a 1-to-2-year window. Medium-term reforms require legislative or regulatory change and are best framed as 3-to-5-year targets.

## Immediate Actions

## Increase Public Agricultural Research and Development Investment in Women's Crops

Private R&D investment tends to follow large commercial markets, systematically bypassing the crops that female smallholders in Southeast Asia grow most, such as cassava, leafy vegetables, legumes, and root crops. Because these crops generate lower commercial returns, private firms have little incentive to develop climate-resilient varieties for them. Public research institutions should fill this gap. National agricultural research agencies should substantially increase the share of R&D budgets allocated to horticulture and climate-substitute crops and involve wom

[中间内容因长度限制已省略]

ary practice.

## Incorporate Gender Markers into Regional Climate Finance

Climate adaptation finance that reaches the household but bypasses the female member's decision-making authority is unlikely to correct the resource misallocation that reduces female agricultural productivity. Gender markers are reporting requirements attached to climate finance flows that track whether women are direct beneficiaries and decision-makers. Association of Southeast Asian Nations member states and development finance institutions should require gender markers as a standard condition for regional agricultural climate finance, consistent with existing frameworks such as the United Nations Framework Convention on Climate Change Gender Action Plan.

## CONCLUSION

Southeast Asia's agricultural sector cannot afford to address climate vulnerability and gender inequality as separate policy problems. The evidence reviewed in this brief demonstrates that both constraints share the same root causes, including intra-household misallocation, insecure land rights, and market failures in directed innovation, and respond to the same set of targeted interventions. The five recommendations presented here are grounded in causal evidence and can be implemented using infrastructure, institutions, and finance mechanisms that already exist in the region. What is required is the political will to redesign how resources are directed, delivered, and tracked, so that they reach the female farmers whose productivity gains would generate the largest returns for the region's food security and economic resilience.

## REFERENCES

Asian Development Bank (ADB). 2025. Asia-Pacific Climate Report 2025. Manila: ADB. https://www.adb.org/sites/default/files/publication/1094721/asia-pacific-climate-report-2025.pdf.

ASEAN. 2024. ASEAN Gender Outlook 2024. Jakarta: ASEAN Secretariat. https://data.unwomen.org/sites/default/files/documents/Publications/2024/ASEAN-gender-outlook\_2024.pdf.

Food and Agriculture Organization (FAO). 2023. The Status of Women in Agrifood Systems. Rome: FAO. https://openknowledge.fao.org/items/adc0741f-9de2-4d09-ae68-b19cc871601a.

——. 2023. Government Expenditures in Agriculture (2001–2022): Global and Regional Trends. Rome: FAO. https://doi.org/10.4060/cc9148en.

Germanwatch. 2026. Climate Risk Index 2026. Bonn: Germanwatch. https://www.germanwatch.org/en/cri.

Goldstein, M., and C. Udry. 2008. The Profits of Power: Land Rights and Agricultural Investment in Ghana. Journal of Political Economy 116(6): 981–1022.

Jack, W., and T. Suri. 2014. Risk Sharing and Transactions Costs: Evidence from Kenya's Mobile Money Revolution. American Economic Review 104(1): 183–223.

Jensen, R. 2007. The Digital Provide: Information (Technology), Market Performance, and Welfare in the South Indian Fisheries Sector. Quarterly Journal of Economics 122(3): 879–924.

LaFave, D., and D. Thomas. 2016. Farms, Families, and Markets: New Evidence on Completeness of Markets in Agricultural Settings. Econometrica 84(5): 1917–1960.

Lee, J., and M. F. Bellemare. 2013. Look Who's Talking: The Impacts of the Intrahousehold Allocation of Mobile Phones on Agricultural Prices. Journal of Development Studies 49(5): 624–640.

Maccini, S., and D. Yang. 2009. Under the Weather: Health, Schooling, and Economic Consequences of Early-Life Rainfall. American Economic Review 99(3): 1006–1026.

Moscona, J., and K. Sastry. 2022. Does Directed Innovation Mitigate Climate Damage? Evidence from US Agriculture. Quarterly Journal of Economics 138(2): 637–701.

Nordstrom, E., and M. Cotton. 2023. Satellite-Based Vegetation Health Indices for Agricultural Monitoring. Working Paper.

OECD. 2021. SIGI 2021 Regional Report for Southeast Asia. Paris: OECD Publishing. https://doi.org/10.1787/236f41d0-en.

—. 2024. SIGI 2024 Regional Report for Southeast Asia. Paris: OECD Publishing. https://doi.org/10.1787/7fc15e1c-en.

Riley, E. 2022. Resisting Social Pressure in the Household Using Mobile Money: Experimental Evidence on Microenterprise Investment in Uganda. Working Paper.

Shah, M., and B. M. Steinberg. 2017. Drought of Opportunities: Contemporaneous and Long-Term Impacts of Rainfall Shocks on Human Capital. Journal of Political Economy 125(2): 527–561.

Udry, C. 1996. Gender, Agricultural Production, and the Theory of the Household. Journal of Political Economy 104(5): 1010–1046.

Visa. 2024. The Future of Commerce on the Cusp of Change: Visa Consumer Payment Attitudes Study 2024. Singapore: Visa. https://www.visa.com.ph/content/dam/VCOM/regional/ap/singapore/global-elements/documents/visa-cpa-2024-report-ipvmc.pdf.

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
