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
## KEY POINTS

\- Cross-border e-commerce is rapidly transforming trade, driving growth and productivity, and expanding market access across Asia and the Pacific.

\- Its benefits remain uneven across economies, sectors, and firms due to varying digital readiness and facilitation initiatives.

\- Micro, small, and medium-sized enterprises have strong potential but remain underrepresented in cross-border e-commerce.

• Regulatory fragmentation, higher compliance costs, and lower trust hinder expansion of cross-border e-commerce.

\- To enable inclusive cross-border e-commerce, governments should build adaptive and interoperable regulatory frameworks, strengthen digital trade agreements and trade facilitation, develop digital skills, and bridge digital divides.

# Advancing Digital Trade and Cross-Border E-Commerce in Asia and the Pacific

Sanchita Basu Das
Senior Economist
Economic Research and Development
Impact Department (ERDI)
Asian Development Bank (ADB)

Angel Love Roque
Operations Analyst
ERDI, ADB

Rachita Gulati

Research Economist

ADB Institute

James Correia

Consultant, ADB

## INTRODUCTION

Digitalization is reshaping trade and commerce across Asia and the Pacific. Digitally delivered services now account for more than half of all services trade (UNESCAP, 2024a). $^{1}$ Foreign direct investment (FDI) in the digital economy has tripled since 2020 (ADB, 2026). $^{2}$ In the Association of Southeast Asian Nations (ASEAN) alone, the digital economy is projected to triple by 2030, with every 1% increase in digital growth associated with a 0.8% rise in gross domestic product (GDP) per capita (UNESCAP, 2024a). At the core of this transformation is the expansion of cross-border e-commerce, where goods and services are exchanged across jurisdictions through digital platforms that integrate ordering, payments, and logistics (OECD, 2025).

Notes: The index combines various indicators grouped into seven core pillars: digital economy, digital government, digital infrastructure, digital regulation, household digitalization, human capital and innovation, and production digitalization.
Effective 1 February 2021, ADB placed a temporary hold on sovereign project disbursements and new contracts in Myanmar.
Source: ADB, 2025e (58026-001: Digital Development Facility for Asia and the Pacific - Phase 2).

Globally, e-commerce sales across 43 economies grew by nearly 60% between 2016 and 2022, reaching \$27 trillion (UNCTAD, 2024). Of the 10 fastest-growing e-commerce economies across the globe, seven are located in Asia and the Pacific (ADB, 2023). In ASEAN, e-commerce rose by 16% in 2025 alone (Nikkei Asia, 2025), reflecting the rapid adoption of digital platforms and online payments. Cross-border e-commerce is reshaping production and consumption patterns, expanding market access, and reshaping value chains.

Asia and the Pacific is particularly well positioned to benefit from cross-border e-commerce. The region accounts for nearly two-thirds of global e-commerce sales, with online transactions forming over 60% of retail sales—far higher than in Europe or North America (ADB, 2024). Mobile payments facilitate around 70% of transactions (McKinsey Global Institute, 2024). Large economies such as the People’s Republic of China and India play a central role in global e-commerce, while emerging economies such as Indonesia, the Philippines, and Viet Nam lead in financial technology (fintech) adoption (ICRIER, 2024; ASEAN, 2023). Strong fundamentals support these trends, including a doubling of internet access since 2012, deepening trade integration, and a growing share in global manufacturing (East Asia Forum, 2025; Eastspring, 2024; ADBI, 2025).

Despite these advantages, significant challenges persist. Digital divides remain pronounced in the region, with about one-third of the population still unconnected and half of those in rural areas (ITU, 2021). Market concentration is high, with a handful of economies accounting for the majority of digital exports, while least developed economies lag far behind (UNCTAD, 2024). The disparities among economies are also evident in Figure 1, which indicates that regional digitalization comprises of four stages of development—advanced, transitioning, emerging, and limited—with uneven levels of development. Micro, small and medium-sized enterprises (MSMEs) often lack the capabilities and resources to fully participate in cross-border e-commerce.

Unlocking the full potential of the digital economy requires a strong enabling ecosystem. These include reliable digital infrastructure, interoperable payment systems, efficient logistics networks, trade facilitation measures, regulatory harmonization, and enhanced digital capabilities among businesses and consumers. However, regulatory fragmentation, rising trade restrictions, and limited interoperability across national digital frameworks continue to create significant structural barriers (ADBI, 2025; ITU, 2025). Growing cybersecurity threats, coupled with gaps in data protection and consumer trust, further constrain digital growth and cross-border digital integration (Aon, 2024).

Figure 1: Digitalization Index, 2024  
![](images/513a27c0b664860d9a850884f1a6db8af130b064abf7bb999fba0ed6ede582f7.jpg)

This policy brief analyzes key trends, patterns, and impacts of digital trade and cross-border e-commerce in Asia and the Pacific and identifies regulatory challenges and opportunities. It draws on papers and discussions emerging from the Asian Think Tank Network 2025 and provides policy recommendations to support a more inclusive and resilient digital trade ecosystem.

## TRENDS AND IMPACT IN DIGITAL TRADE AND CROSS-BORDER E-COMMERCE

Global e-commerce sales have expanded significantly, and the growth trajectory of cross-border e-commerce has been strong and sustained. Digital exports in Asia and the Pacific have nearly quadrupled since 2005, as illustrated in Figure 2, and e-commerce has doubled since 2016 (Rahman and Rahman, 2022; CSIS, 2024). This has been supported by a rapidly evolving digital ecosystem encompassing online marketplaces, digital payments, logistics providers, and digitally enabled supply chains. New forms of commerce, such as social commerce, live-stream shopping, gamification, and app-based retail, are gaining traction, particularly among younger consumers (KPMG, 2024). These developments reduce information asymmetries by efficiently matching buyers and sellers, streamline administrative processes, such as customs and compliance, and lower transaction costs by expanding market access and scale (López González and Ferencz, 2018; ADB, 2025a).

Cross-border e-commerce is rapidly transforming the scale and direction of trade across Asia and the Pacific and accounts for a higher share of the total than in other regions (Rahman and Rahman, 2025). Its importance varies significantly across economies, reflecting differences in levels of economic development, digital readiness, and institutional capacity. Advanced economies tend to derive greater value from the digital economy, with contributions to GDP reaching 6.1% in Taipei, China; 5.8% in the Republic of Korea; and 5.4% in Singapore, compared to just 2.5% in the Philippines and 1.8% in the Lao People's Democratic Republic and Cambodia (Ortiz and Manguera, Unpublished). A significant growth potential remains for e-commerce in emerging economies. In Indonesia, e-commerce already accounts for 72% of the digital economy and is projected to reach \$146 billion, or 9%–10% of GDP, by 2025 (Supriyadi et al., Unpublished). In the Philippines, e-commerce adoption expanded dramatically from 14% of firms in 2013 to 31.2% in 2021 (Ortiz and Manguera, Unpublished). These variations highlight the central role of infrastructure, digital literacy, and regulatory systems in shaping both domestic and cross-border e-commerce outcomes across economies and regions.

Sectoral composition further illustrates these differences. Emerging economies tend to specialize in information and communications technology goods and basic electronics, while advanced economies are increasingly oriented toward higher-value, digitally delivered services, including finance, information technology, and cultural industries (Ghosh, Unpublished; Ortiz and Manguera, Unpublished). As a result, digitally delivered services trade is more prominent in advanced economies, whereas goods-based digital trade remains dominant in countries such as Malaysia, Thailand, and Viet Nam (Ortiz and Manguera, Unpublished; Ghosh, Unpublished). However, in recent years, there is a structural shift toward service-led growth and digital transformation, with knowledge-intensive services emerging as the fastest-growing segment across the region (Ghosh, Unpublished; Baker and Le, Unpublished).

Figure 2: Trade in Digitally Delivered Services in Asia and the Pacific, 2010–2024  
![](images/ca00f80b9e1a8ed1c509a591a6a053372166ddc78852b2c98913221ca6f02107.jpg)  
Source: UNCTAD Statistics, 2026.

Trade agreements are critical in providing an enabling regulatory environment for cross-border e-commerce. Multilateral and regional frameworks have increasingly shaped the governance of digital trade. The WTO Joint Statement Initiative (JSI) on E-Commerce has advanced negotiations on global rules for e-commerce, while agreements, such as the Regional Comprehensive Economic Partnership (RCEP) and the Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP), have incorporated e-commerce chapters and provisions on cross-border data flows, digital trade facilitation, and regulatory cooperation (Baker and Le, Unpublished; WTO, 2023). While these agreements have facilitated cross-border e-commerce, more can be done. For example, the RCEP provides broad regional coverage and significant scope for deepening digital trade commitments, while the CPTPP incorporates more advanced and comprehensive rules but continues to face implementation challenges among its members (CSIS, 2024; KPMG, 2021; Baker and Le, Unpublished).

Nonetheless, empirical evidence suggests that such agreements significantly boost digitally delivered services trade, particularly in finance, IT, and cultural services (Ghosh, Unpublished). Singapore is pursuing a multifaceted approach to tap into the varied strengths of available trade channels, adopting six bilateral digital economy agreements $^{3}$ while participating in the broader ASEAN, RCEP, and CPTPP processes (Ministry of Trade and Industry, 2025). The rise and role of digital trade agreements and provisions in Asia and the Pacific is illustrated in Figure 3.

Despite these positive trends, the benefits of cross-border e-commerce remain unevenly distributed across firms, sectors, and geographies. Larger firms are generally better positioned to participate due to greater access to finance, technology, and skilled labor, while smaller firms—especially those in rural, remote or less-developed areas—face persistent barriers of connectivity, capabilities, and scale (Chhorn et al., Unpublished; Ortiz and Manguera, Unpublished). This is particularly significant among the MSMEs, which are significant in the services sector and account for 97% of enterprises, 69% of employment, and 41% of GDP in the region (UNESCAP, 2024; Nikkei, 2025).

Targeted interventions demonstrate that these constraints can be overcome. In the People's Republic of China, the development of Taobao villages has generated over

RMB1 trillion in transactions, enabling small-scale rural producers to access national and global markets and diversify their economic activities (Cai and Tian, Unpublished). A case study of Taobao villages is provided in Box 1. Azerbaijan's export promotion portal has upgraded local firms' participation in international platforms and trade, with 3,500 companies reaching 122 economies (Huseyn and Gadashov, Unpublished). These examples underscore the potential of cross-border e-commerce to advance inclusive growth when supported by appropriate policies and infrastructure.

Fintech is another critical enabler of cross-border e-commerce, particularly cross-border payments and expanding financial inclusion. Adoption rates are especially high in emerging economies such as the Philippines and Viet Nam, often surpassing those in more mature markets (PCMI, 2023). Platforms such as MBANK in the Kyrgyz Republic demonstrate how digital finance can broaden access to payment systems, facilitate cross-border transactions, and support innovative financial services. The platform has expanded rapidly and now serves approximately $80\%$ of the country's adult population (PR Newswire, 2024). However, the rapid expansion of fintech also introduces risks, including cybersecurity threats, fraud, and over-indebtedness. Moreover, significant disparities persist, with fintech usage in urban areas far exceeding that in rural regions, reflecting underlying inequalities in access and digital literacy (Morgan, 2022).

## Box 1: Taobao Villages—A Decentralized Ecosystem for Rural E-Commerce in the People's Republic of China

Taobao villages are localized rural e-commerce hubs that demonstrate the interplay between micro, small and medium-sized enterprises and large-scale online providers. These include 29,600 active online shops across 5,425 villages. Alibaba provides a platform and logistics network for connecting these firms to new consumers and markets, expanding the reach of their commercial activities while lowering transaction costs. This initiative has fostered rural development, boosted productivity and innovation, and improved community resilience, including by reducing agricultural sector dependence and shifting local economies toward higher-value manufacturing and services. These benefits have been particularly pronounced in economically disadvantaged areas.

Source: M. Cai and S. Tian. Unpublished. Can Digital Platforms Boost Economic Growth? Evidence from the Taobao Villages. Paper presented at the Asian Think Tank Network Forum 2025, Tokyo, Japan.

Figure 3: Timeline of Digital Trade Agreements and Provisions in Asia and the Pacific  
![](images/04f9c2674383041743b8ce4d43365858048bdaf836d8a00e61104ae4828a6994.jpg)  
CEPA UK–JP = United Kingdom–Japan Comprehensive Economic Partnership Agreement, CPTPP = Comprehensive and Progressive Agreement for Trans-Pacific Partnership, CSFTA = China–Singapore Free Trade Agreement, CSFTA CL–SG = Chile–Singapore Free Trade Agreement, DEA = Digital Economy Agreement, DEPA = Digital Economy Partnership Agreement, EP = Economic Partnership, EPA = Economic Partnership Agreement, JSEPA = Japan–Singapore Economic Partnership Agreement, KSDPA = Korea–Singapore Digital Partnership Agreement, RCEP = Regional Comprehensive Economic Partnership, USMCA = United States–Mexico–Canada Agreement.  
Notes: The list of economies and agreements is not exhaustive. The diagram is intended solely for illustrative purposes, highlighting relatively active economies in digital regulatory cooperation, with a focus on Asia and the Pacific, as well as post-COVID-19 developments in the growing importance of digital regulatory cooperation and digital trade agreements. Effective 1 February 2021, the Asian Development Bank (ADB) placed a temporary hold on sovereign project disbursements and new contracts in Myanmar.
Source: ADB, 2025a

![](images/fc00fec42f4f6bd226669c123def104ca450d0c2b0fdf1635d310125dbede2dc.jpg)  
Source: UNCTAD Statistics, 2026.

At a macroeconomic level, cross-border e-commerce is contributing to structural transformation by shifting the balance of economic activity toward services and digital trade (Bernardo, Unpublished). Trade in services has expanded rapidly since COVID-19, while the relative share of goods trade has declined (UNCTAD, 2024). These trajectories are shown in Figure 4. Services now account for more than half of employment in the region, driven by the growth of sectors closely linked to cross-border e-commerce such as finance, technology, and logistics (IMF, 2024). These offer substantial productivity gains. For example, financial services are, on average, four times more productive than manufacturing in Asia and the Pacific (IMF, 2024). Cross-border e-commerce also enhances economic resilience by diversifying sources of growth and reducing dependence on primary commodities, which are often vulnerable to price volatility and climate risks (Cai and Tian, Unpublished).

At the same time, the rise of large digital platforms introduces new challenges. Market concentration, driven by network effects, can limit competition and create asymmetric dependencies between platforms and smaller firms. Four in five MSMEs in Asia and the Pacific view large platforms as critical infrastructure, and their role in sustaining operations, broadening customer bases and market access, and reducing costs can be a double-edged sword (Nikkei,

2025; As'ad et al., 2022; ADB, 2024; ADB, 2025b). The expansion of the gig economy—now accounting for a significant share of the labor force in some countries—raises concerns about job quality, income stability, and social protection (WEF, 2025). These dynamics highlight the need for balanced policy approaches that support innovation while addressing emerging risks.

Realizing the full potential of cross-border e-commerce requires a comprehensive and coordinated policy framework. Investing in infrastructure, which continues to loom large as a barrier to digital trade (Figure 5), interoperable payments, regulatory alignment, digital skills, and strong data, cybersecurity, and consumer protection frameworks are essential for inclusive and sustained cross-border e-commerce growth. These are discussed further in the next section.

## CROSS-BORDER E-COMMERCE REGULATIONS AND CHALLENGES

Regulatory gaps, fragmentation, and trade restrictions remain major barriers to the expansion of cross-border e-commerce in Asia and the Pacific. These challenges arise from the absence of comprehensive and binding regulatory frameworks; narrow and outdated legislation with significant gaps in coverage; overlapping and sometimes inconsistent laws governing e-commerce;

■ Other Barriers to Trade in Digital Services

Figure 5: Infrastructural and Regulatory Hurdles to Digital Trade in Asia and the Pacific, 2025  
![](images/8047fbd96e383adac64a39d15723cd4bfcacc02025455eeca7c561da405a3ebb.jpg)  
Source: OECD Digital Services Trade Restrictiveness Index (Digital STRI), 2025 (OECD Data Explorer • Digital Services Trade Restrictiveness Index).

the largely “soft” nature of existing e-commerce rules; fragmented institutional responsibilities across government agencies; and limit

[中间内容因长度限制已省略]

Ortiz, M. K., and M. C. R. Manguera. Unpublished. Connected for Growth: Analyzing the Impact of E-Commerce Adoption on Firm Performance and Labor Outcomes in the Philippines through Peer Effects.

Payments CMI (PCMI). 2023. Understanding Asia-Pacific: Where the Future of Fintech Is Shaped. https://paymentscmi.com/insights/asia-pacific-fintech-industry/.

PR Newswire. 2024. MBank Transforms Kyrgyzstan's Banking Landscape with Digital Ecosystem and Mobile App Milestones. https://www.prnewswire.com/news-releases/mbank-transforms-kyrgyzstans-banking-landscape-with-digital-ecosystem-and-mobile-app-milestones-302387195.html.

Rahman, M. N., and B. Rahman. 2022. Exploring Digital Trade Provisions in Regional Trade Agreements in Times of Crisis: India and Asia-Pacific Countries. https://doi.org/10.1016/j.aglobe.2022.100036.

Rivera, J. P. Unpublished. Digital Trade for Macroeconomic Resilience: Evidence from ASEAN's Cross-Border E-Commerce Integration. Paper presented at the Asian Think Tank Network Forum 2025, Tokyo, Japan.

Supriadi, A. Y., S. Rachmad, K. G. C. Dillena, H. Kardoyo, D. Asiati, and R. Elizabeth. Unpublished. Unlocking Economic Gains: How E-Commerce Enhances Efficiency, Productivity, and Market Access in Indonesia—Evidence from 2024 Survey. Paper presented at the Asian Think Tank Network Forum 2025, Tokyo, Japan.

Tang, M., Jiang, L., Mao, Y. and Cao, L. 2025. Does the depth of digital trade rules promote bilateral value chain cooperation? International Review of Financial Analysis. https://doi.org/10.1016/j.irfa.2025.103952.

Times of Central Asia. 2025. Uzbekistan Introduces New Rules for E-Commerce Platforms. https://timesca.com/uzbekistan-introduces-new-rules-for-e-commerce-platforms/.

United Nations Conference on Trade and Development (UNCTAD). 2023. Digital Trade Fuels Asia-Pacific's Growth, but Progress Remains Uneven. https://unctad.org/news/digital-trade-fuels-asia-pacifics-growth-progress-uneven.

UNCTAD. 2024. Digital Economy Report 2024. Geneva: United Nations Conference on Trade and Development. https://unctad.org/publication/digital-economy-report-2024.

UNCTAD. 2026. UNCTADstat Data Centre. https://unctadstat.unctad.org/datacentre/.

United Nations Economic and Social Commission for Asia and the Pacific (UNESCAP). 2022a. Asia-Pacific Digital Trade Regulatory Review 2022. Bangkok: United Nations Economic and Social Commission for Asia and the Pacific. https://www.unescap.org/sites/default/d8files/knowledge-products/Asia%20Pacific%20Digital%20Trade%20Regulatory%20Review%202022.pdf.

UNESCAP. 2022b. Asia-Pacific Digital Transformation Report 2022: Shaping Digital Futures for All. Bangkok: United Nations Economic and Social Commission for Asia and the Pacific. https://www.unescap.org/sites/default/d8files/knowledge-products/ESCAP-2022-Flagship-Asia-Pacific-Digital-Transformation-Report.pdf.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.

ADB Briefs are based on papers or notes prepared by ADB staff and their resource persons. The series is designed to provide concise, nontechnical accounts of policy issues of topical interest, with a view to facilitating informed debate. The Department of Communications and Knowledge Management administers the series.

www.adb.org/publications/series/adb-briefs

UNESCAP. 2024a. Trends in Digital Trade and Investment in Asia and the Pacific. https://www.unescap.org/sites/default/d8files/event-documents/reading2.pdf.

UNESCAP. 2024b. Overview of MSMEs in Asia and the Pacific. https://msmepolicy.unescap.org/overview-msmes-asia-pacific-regions.

United Nations News. 2024. Digital Trade Can Boost Livelihoods and Economic Growth in Asia-Pacific. https://news.un.org/en/story/2024/09/1153931.

World Bank. 2025. Individuals Using the Internet (% of Population). World Development Indicators. https://data.worldbank.org/indicator/IT.NET.USER.ZS.

World Economic Forum (WEF). 2025. What We Learned about the Future of Work in Asia. https://www.weforum.org/stories/2025/07/what-we-learned-about-the-future-of-work-in-asia-at-amnc25-and-other-trends-in-jobs-and-skills-this-month/.

World Trade Organization (WTO). 2023. Work Programme on Electronic Commerce. INF/ECOM/87. Geneva: World Trade Organization. https://docs.wto.org/dol2fe/Pages/SS/directdoc.aspx?filename=q:/INF/ECOM/87.pdf.

WTO. 2024. Trade in Services Database. https://data.wto.org.

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent. ADB does not guarantee the accuracy of the data included here and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned. By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

Asian Development Bank
6 ADB Avenue, Mandaluyong City
1550 Metro Manila, Philippines
www.adb.org

![](images/4559988188b7c5d4fcf827fcfbf3090e355f30ab95e11e189564f382b80ab46f.jpg)

## Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)
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
