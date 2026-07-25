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
# More than a Space Programme

## The Value of Space Exploration to Empower the Future of Europe

November 2023

## About the Report

This report provides the findings of a work by Boston Consulting Group (BCG) and the European Space Policy Institute (ESPI) to quantify the overall impact of Europe's Mission for Space Exploration. It is meant as a contribution to a plan for a transformation and invigoration of the European space ecosystem, as requested in the "Revolution Space" report published in March 2023 by the High-Level Advisory Group on Human and Robotic Space Exploration for Europe, and in preparation for the Space Summit held in Sevilla on 6-7 November 2023.

This report is a concise and publicly accessible rendition of the original study. The study was funded by ESA, as an independent assessment performed by ESPI and BCG. The findings and conclusion or recommendations expressed in the study are those of the authors and do not necessarily represent the views of ESA.

A three-step methodology has been employed to analyse the various economic benefits that Europe can gain from space exploration. These benefits encompass immediate economic returns, cross-fertilisation within the space industry, and significant broader improvements and outcomes for the economy and society at large.

The authors acknowledge that the study, by its mandate and very nature, reaches across classical boundaries of space programmes (e.g., launchers, exploration, space applications), which in most European programmes are traditionally defined and funded within their respective objectives, funding, and governance frameworks. The report however demonstrates that these benefits are inseparable and can only be achieved in full if addressed as a whole within a European space industry at scale and globally competitive. Indeed, the development of core space exploration capabilities is pivotal to unlock cross-fertilisation effects for the space industry and, therefore, enhance value generation for the broader economy and society.

The study also acknowledges that the precise quantification of the economic benefits, across individual domains of space programmes, and from the space economy into other sectors of the economy is still at an earlier stage of research and relatively new to the space community. It is however believed that the general assessment of such broader impact and the presented order of magnitude of impact provide valid indicators of actual impact.

Overall, it is in the hope of the authors that the study will contribute to a debate across those domains and the formulation of strategies that optimise synergies across different programmatic domains, as done by global space powers.

## Table of Contents

About the Report iii
1. Key findings 1
2. Introduction 3
2.1 Context 3
2.2 Rationales 5
2.3 Objectives 6
3. The value of space exploration 7
3.1 Economic and societal benefits of space exploration 8
3.1.1 Direct, indirect, and induced benefits 9
3.1.2 Catalytic benefits: economic 9
3.1.3 Catalytic benefits: (geo)political 10
3.1.4 Catalytic benefits: technological and scientific 11
3.1.5 Catalytic benefits: societal 12
3.2 Space exploration's cross-fertilisation benefits with the space industry 12
3.2.1 Application-specific and systemic benefits 12
3.2.2 Cross-fertilisation from launch and manufacturing capabilities 15
3.3 Benefits of space for the broader economy and society 21
3.3.1 Space and other critical sectors 21
3.3.2 Value of space for the broader economy and society 23
4. Time to act 29
5. Cost of inaction 32
6. Closing remarks 39
Appendix 42
A. Methodology for GDP impact estimation 42
A.1 Input-output analysis 43

A.2 Data sources 45  
A.3 Modelling approach 45  
A.4 Strengths and limitations 47  
B. Scope of space exploration activities 48  
C. Additional clarification on space economy vs global economy enhanced by space 51  
D. Gap analysis 53  
D.1 List of studies 58  
E. The SpaceX Case: How Funding Space Exploration Induces Commercial Market Leadership 60

## List of Figures

Figure 1. Different level of benefits from space exploration activities 8  
Figure 2. Estimated benefits of space exploration in Europe (2025-40) 9  
Figure 3. Human spaceflight missions for Falcon 9 and Soyuz launchers (2020-22) 13  
Figure 4. Share of HSE-related revenues for US and European players 14  
Figure 5. Cross-fertilisation potential from launch and manufacturing capabilities 16  
Figure 6. Revenue CAGR and EBITDA margin for space OEMs 18  
Figure 7. Value of space launch market in 2015-40, by application 19  
Figure 8. Value of space manufacturing market in 2015-40, by application 20  
Figure 9. Comparable industries to space 21  
Figure 10. Space industry exceptional funding in Europe compared to other industries 22  
Figure 11. Space industry multiplier on the broader economy and society 23  
Figure 12. Value of space for economy & society in 2022, by industry 24  
Figure 13. Selected examples of space enhancement across sectors 25  
Figure 14. Main drivers of space technology adoption 26  
Figure 15. Evolution of value of space for economy & society (2022-40) 27  
Figure 16. Time for orbital capabilities and manufacturing cost for space station OEMs 30  
Figure 17. Cost of inaction related to direct, indirect, induced, and catalytic benefits 33  
Figure 18. Cost of inaction related to European space industry size and competitiveness 34  
Figure 19. Key examples of lost opportunities 37  
Figure 20. Space exploration comprehensive benefits for Europe in 2025-40 40  
Figure 21. Space exploration intangible benefits for Europe in 2025-40 41  
Figure 22. Cumulative GDP and average FTEs linked to space exploration in Europe ('25-40) 42  
Figure 23. Methodology for direct, indirect, induced impact calculation 45  
Figure 24. Comparison of European space exploration investment and NASA impacts 46  
Figure 25. Methodology for catalytic impact calculation 47  
Figure 26. Space economy taxonomy 51

Figure 28. SpaceX institutional support through Space Act Agreements (SAA) in COTS, NASA commercial crew contracts and private capital raising (\$ million)

## List of Tables

Table 1. Rationale behind chosen indicators....57
Table 2. List of studies....59
Table 3. SpaceX Company Valuation and Revenue Multiplier....63

## List of Abbreviations

<table><tr><td>CAGR</td><td>Compound Annual Growth Rate</td></tr><tr><td>C4ISR</td><td>Command, Control, Communications, Computers, Intelligence, Surveillance and Reconnaissance</td></tr><tr><td>EO</td><td>Earth Observation</td></tr><tr><td>FMS</td><td>Fleet Management System</td></tr><tr><td>GDP</td><td>Gross Domestic Product</td></tr><tr><td>GEO</td><td>Geostationary Earth Orbit</td></tr><tr><td>GNC</td><td>Guidance, Navigation, and Control</td></tr><tr><td>GNSS</td><td>Global Navigation Satellite System</td></tr><tr><td>HSE</td><td>Human Space Exploration</td></tr><tr><td>ILRS</td><td>International Lunar Research Station</td></tr><tr><td>ISRU</td><td>In-Situ Resource Utilisation</td></tr><tr><td>ISS</td><td>International Space Station</td></tr><tr><td>LEO</td><td>Low Earth Orbit</td></tr><tr><td>MDS</td><td>Missile Defence Systems</td></tr><tr><td>MEO</td><td>Medium Earth Orbit</td></tr><tr><td>OEM</td><td>Original Equipment Manufacturer</td></tr><tr><td>PNT</td><td>Positioning, Navigation, and Timing</td></tr><tr><td>SatCom</td><td>Satellite Communications</td></tr><tr><td>SBSP</td><td>Space-Based Solar Power</td></tr><tr><td>SWE</td><td>Space Weather Events</td></tr><tr><td>SSA</td><td>Space Situational Awareness</td></tr><tr><td>TSR</td><td>Total Shareholder Return</td></tr></table>

## 1. Key findings

The report shows that the implementation of a major European space exploration programme would allow to generate a GDP multiplier effect of >5x the overall budget. Considering an investment of €50 billion between 2025 and 2040, the estimated benefits would amount to a cumulative GDP impact of at least €260 billion and an average of 90,000 FTEs created over the same period.

The impact distinguishes a multiplier of 3x resulting in a GDP impact of €150 billion...

\- In terms of direct economic benefits, the investment is anticipated to contribute to €25 billion of direct cumulative GDP impact through the value added generated by an average of 4,000 new space exploration-related FTEs. In addition, procurement expenditures are projected to generate \~€70 billion of indirect GDP impact within the European space industry. Finally, the budget's injection into the economy is anticipated to increase household spending of employees in the space sector within the broader supply chain, further contributing to \~€55 billion of induced cumulative GDP impact throughout the 2025-40 timeframe.

... and a further GDP impact of €110 billion, thus resulting in a total multiplier of >5x:

\- In terms of catalytic benefits, Europe's investment will generate \~€110 billion of incremental GDP contribution within the 2025-40 timeframe. The lion's share of this contribution (€85 billion) will stem from new space markets, including space travel, in-space R&D and manufacturing, in-orbit services, and edge computing. Additionally, a renewed focus on space innovation driven by investment in space exploration is also expected to generate a GDP impact of \~€10 billion between 2025-40 from technological spinoffs as well as an increase in GDP of \~€15 billion through the comparably higher productivity and value generation of STEM jobs.

Together with the direct, indirect, induced, and catalytic economic gains, space exploration provides cross-fertilisation effects across different elements of the broader space sector, by both supporting the overall development of the space economy and generating improvements in critical capabilities that strengthen companies' competitiveness. In both cases, investment in space exploration goes beyond its own borders and positively affects other core European capabilities across the whole space ecosystem (e.g., launch capabilities).

Looking at the US, the correlation between space exploration expenditures and industry competitiveness can also be observed, particularly considering SpaceX and its transformative impact on the entire ecosystem. Indeed, as shown in Annex E, SpaceX's business model was mostly enabled by the initial support provided by public institutions (e.g., NASA) in exploration and space transportation.

The value created by space exploration for the broader space economy manifests itself in systemic benefits that provide critical size, bolster the industrial ecosystem, and promote synergies with other space domains (e.g., industrial capability as part of security policy).

The report also shows that due to its role in providing scale to the industrial ecosystem, in enabling economies of scale, and serving as a vehicle for increasing competitiveness, investment in space exploration cannot be dissociated from the overall investment in space and the economic benefits enhanced by space, beyond the space programme, for the whole economy and its sectors. Indeed, as a prominent element of space programmes across all space powers, exploration is central to the creation of a resilient space industrial landscape, often linked to strategic capabilities in security and defence, and to the benefit of other applications too. In short, exploration impacts space and the broader economy as enhancement of key economic activities in sectors like telecom and defence.

The value of the space economy in 2022 is \~\$460 billion, whereas the estimated value of space for the broader economy amounts to \~\$3.1 trillion in the same year. This estimation is built on the analysis of 15+ business cases across different industries, where space demonstrates its enabling effects in terms of creating new markets, generating incremental value-added, and enabling core industries.

Looking at the future, the estimated value the space economy will reach \$1 trillion in 2040, while the value of space for the broader economy and society is projected to reach approximately \$7.9 trillion, leading to a cumulative impact of over \$80 trillion between 2025 and 2040.

While the economic benefits of space exploration and space at large are promising, there are several risks that must be carefully managed for its full realisation. Firstly, budget deployment is critical, as resources must be allocated appropriately, deployed in a timely manner, and distributed effectively among key stakeholders and across existing silos between space domains in Europe. The ability to attract private capital is also essential, particularly in establishing the necessary infrastructure at European level to develop effective public-private partnerships. Moreover, a strategy without strong own capabilities and relaying mainly on cooperation with other countries as a junior partner poses a risk, as Europe would only support an established market of leading space powers, a market outside Europe, which would potentially represent a more attractive target for private investors. Lastly, the risk associated with human exploration activities cannot be ignored as the occurrence of severe accidents could temporarily halt missions, thus hindering the realization of these benefits. Coordinated planning and ad hoc risk mitigation strategies will be essential to navigate these challenges successfully and seize the Space Revolution opportunity. Ultimately, a related space strategy would require dedicated efforts to include space in strategies of other sectors, like the European Green Deal and Digital Strategy.

## 2. Introduction

## 2.1 Context

The space industry is a critical sector for government investments with tremendous potential in the future. Space represents a substantial market that exceeded expectations in 2022, achieving a remarkable \$464 billion size, growing higher than previous forecasts at an impressive 6% CAGR and it is foreseen to reach \$1 trillion by 2040. Moreover, the industry plays a pivotal role in fostering the creation of highly skilled employment and driving innovation spinoffs across multiple sectors.

The space industry's contribution extends beyond economic value as it profoundly impacts society and positively influences the lives of people on Earth. For example, space technologies significantly contribute to achieving sustainable development goals (SDGs) and are core enablers in realizing the net-zero climate change ambitions set by COP27 with 50% of essential climate variables only measurable from space. Additionally, they also actively assist disaster responses and crisis management. Indeed, 400+ international relief efforts are supported by earth observation imagery, navigation, or satellite communications, and 600+ remote sensing satellites survey across borders.

The space industry is currently experiencing an unprecedented momentum. Over the last decade, the industry has grown remarkably, boasting more than 1,000 active space companies in 2022, compared to around 600 in 2012 $^{1}$ . The number of satellites launched annually has surged from an average of \~300 from 2010-19 to 2,000+ in 2022, with a significant portion driven by Starlink. Consistently, in-orbit services are being developed to sustain orbital infrastructures (e.g., satellite refuelling). Similarly, the need for Space Traffic Management services and Space Situational Awareness (SSA) has become evident, as happened with the International Space Station (ISS) performing three manoeuvres in 2022 to avoid debris collision, compared to a total of 33 since 1999.

The space sector's growth has also sparked intense competition. NATO has declared space as the $5^{\text{th}}$ battleground and the United States has set up an independent Space Force. Governments worldwide are allocating substantial resources, with spending in 2022 surpassing \$100 billion, representing a $9\%$ year-on-year increase from 2021, driven mainly by defence-related endeavours. Key countries are prioritizing their space initiatives, and new nations are entering the arena. However, despite representing circa 25% of global GDP, Europe only covers a 15% share (\~€15 billion) of the total government budgets allocated to space.

The capital influx into the industry is substantial, with significant investments coming from both government institutions and private investors. The commercialisation potential of space has driven considerable private funds, particularly from the United States and China. Even in Europe, investments in space start-ups reached a significant threshold of €1 billion in 2022, marking a 65% increase compared to the previous year, with Venture Capital accounting for approximately 75% of the total $^{2}$ .

Space exploration is a core engine of all these transformations, and investments and developments in space exploration are on the rise globally. The international space exploration landscape sets the beginning of a new historical juncture. In LEO, the development of sovereign space stations has already been showcased. While China's space station is operational, India will likely have its own orbital infrastructure soon after the ISS era together with Russia, despite not in the near term. Additionally, US OEMs, often supported by NASA, are also leading the way towards nascent commercial LEO space stations (i.e., Axiom station, Northrop Grumman station, Orbital Reef, Starlab, Haven-1). In this context, Europe risks to become a junior partner contributing only to the development of one of the five US main stations, which will compete for CLD funding in the coming years. Beyond LEO, the Moon has re-emerged as a key target for human space exploration activities of the major spacefaring nations. On this front, the three leading space powers, the United States, China, and Russia, all have plans for landing and sustaining their respective astronauts, taikonauts and cosmonauts on the lunar surface within the next decade.

In this rapidly evolving context, today Europe still has the opportunity to also become a transformative player in the unfolding space revolution.

## 2.2 Rationales

In 2023, ESPI supported the High-Level Advisory Group (HLAG) in the preparation of the report “Revolution Space”. This report marked a decisive moment in showcasing the strategic importance of space exploration activities and outlining how Europe must stand to benefit from increased participation. The study laid the foundation for defining the advantages of heightened involvement and proposed an initial roadmap for a European strategy.

Subsequently, it was evident that the critical relevance of the subject required a clear and comprehensive categoriz

[中间内容因长度限制已省略]

acecraft having invested \$100 million of his PayPal proceeds to the effort. NASA's call to partner with commercial companies crucially provided additional incentive to formulate vehicle specifics and turn the concept into reality. After three failed attempts to reach orbit, the Falcon 1 first successful launch occurred in September 2008.

Due to the successful launch, NASA awarded SpaceX a \$1.6 billion fixed price contract under the first phase of the Commercial Resupply Service (CRS-1) program $^{10}$ . It required the delivery of 20 metric tons of cargo to ISS over 12 missions between January 2009, through to the end of 2016. At that time, SpaceX was close to bankruptcy and the awarded ISS cargo

"SPACEX WAS CLOSE TO BANKRUPTCY AND THE AWARDED ISS CARGO MISSIONS SAVED THE

missions saved the company, according to Elon Musk. The commercial contract would then help SpaceX to finish the development of their Falcon 9 launcher $^{11}$ and Dragon capsule. The company released the total combined development costs for both the Falcon 9 launch vehicle and the Dragon capsule; NASA provided \$396 million (from COTS) while SpaceX provided over \$450 million to fund both development efforts. After the successful Falcon 9 launches and Cargo Dragon C1 demonstration mission, which delivered cargo to the ISS, in 2010, SpaceX received additional funding from the Commercial Crew Program (CCP) program between 2010 and 2014 in order to develop a crew variant of the Dragon spacecraft. This included \$450 million for vehicle design in 2011 from the CCDEV2, \$440 million for the end-to-end concept in 2012 under CCiCap, and \$10 million for the certification plan under the CPC1. While previous funding under the CCP has been for developing the spacecraft, SpaceX received a ground-breaking \$2.6 billion contract in 2014 for the actual service of the crew flights under the CCtCap.

## 2015-2023: Falcon 9 and Starlink, from public to commercial funding.

In January 2015, shortly after securing the CCtCap contract, the company announced it would build its Starlink satellite internet constellation. Only a few days after this announcement, SpaceX confirmed that it closed a Series G funding round worth \$1 billion led by internet giant Google marking the tremendous pull a fully commercial service announcement had on raising capital for the company. At the end of 2015, SpaceX also managed to successfully land the first Falcon 9, with the estimated cost of developing reusability at just above \$1 billion on top of the Flacon 9's development cost. $^{12}$ By the end of that year, SpaceX had raised \$1.2 billion in private funds and been awarded over \$8.7 billion in NASA contracts and funding.

![](images/f31a54608e23ce816890acb7357c21df20c3fd08540dde70b747756c4bae71b8.jpg)

![](images/3928e0ed5c95ea1dbe3fe385fc2c1e062c443cdcc551c115020469bb31d6e904.jpg)  
Figure 28. SpaceX institutional support through Space Act Agreements (SAA) in COTS, NASA commercial crew contracts and private capital raising (\$ million)

Figure 28 above clearly illustrates the transition between NASA funding and SpaceX's funding through private markets. The 2014 CCtCAp funding and the announcement of Starlink provided the impetus for the subsequent \$1 billion private funding round and represented a turning point in the company's capital raising efforts. \_ $^{13}$

The successful demonstrated reuse of a flown booster and the FCC approval of the initial batch of Starlink satellites led to additional large private funding rounds between 2017 and 2019 $^{14}$ accumulating to \~2 billion, paving the way for development and deployment of the Starlink constellation in 2019, which in turn made Falcon 9 the most successful commercial launcher in history. $^{15}$ With the ongoing deployment of Starlink and the successful first crew transfer to the ISS in seven years from US soil by SpaceX on its Crew Dragon capsule in May 2020, the company managed to raise a record funding round of 1.9 billion by private venture capital firms later the same year. As of today, SpaceX raised 9.8 billion in funding over 30 rounds by 84 investors, valuing the company at approx. \$140 billion as can be seen in Table 3. $^{16}$

<table><tr><td></td><td>FY2022</td><td>FY(2023)</td></tr><tr><td>Company Valuation ($ billion)</td><td>137 $^{17}$ </td><td>140</td></tr><tr><td>Revenue (end of year) ($ billion)</td><td>4.6 $^{18}$ </td><td>8 $^{19}$ </td></tr><tr><td>Starlink Revenue Attribution ($ billion) (% of Total Revenue)</td><td>1.4 (30.43%)</td><td>Estimated 3.2 (40%)</td></tr><tr><td>Revenue Multiple</td><td>29.78x</td><td>17.5x</td></tr><tr><td>Average Revenue Multiple</td><td colspan="2">23.6x</td></tr></table>

Table 3. SpaceX Company Valuation and Revenue Multiplier

## 2024 and beyond: Starshield, Starship and Space Exploration

"ADDITIONAL LARGE PRIVATE FOUNDING ROUNDS [...] PAVING THE WAY FOR THE DEVELOPMENT AND DEPLOYMENT OF THE STARLINK CONSTELLATION, WHICH MADE FALCON 9 THE MOST SUCCESSFUL COMMERCIAL LAUNCHER IN HISTORY"

Private funding, the revenues from Starlink services and the availability of Falcon 9 enable SpaceX to pursue the development of the super heavy lift launch vehicle Starship and receive government contracts for the military constellation Starshield. Starship will enable wider exploration goals

in commercial LEO as a potential space station, on the Moon through the HLS, and potential Mars exploration.

This example shows that institutional contracts for space exploration do not only spillover to launchers and commercial funding for connectivity applications, but also enable private actors to serve the defence market, together with widening ambitious exploration programmes.
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
