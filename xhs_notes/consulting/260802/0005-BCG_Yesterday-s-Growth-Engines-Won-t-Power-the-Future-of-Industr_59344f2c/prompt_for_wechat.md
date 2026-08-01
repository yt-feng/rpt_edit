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
![](images/61dfb30160ff376c80525550a0595b7d59bdaa96e1d46ccff3a4110ff67b8368.jpg)

INDUSTRIAL GOODS

# Yesterday's Growth Engines Won't Power the Future of Industrial Technology

By Markus Lorenz, Sebastian Heimbach, Simon Rees, Yoichi Hangai, Bernhard Siegert, and Franziska Maassen

ARTICLE APRIL 13, 2026 12 MIN READ

On the surface, the future looks bright for producers of industrial technology, a \$5.8 trillion industry that supplies everything from factories to power plants. Global compound annual growth is projected at 6% through 2030.

Underneath, however, things are shifting. The value pools driving the industry's growth are rapidly changing. The China market is cooling for many foreign equipment suppliers, likely for good. So is demand for machinery and equipment in the automotive sector and in some once-booming segments of the market for the low-carbon energy transition.

In their place, defense, data centers, and infrastructure are emerging as new growth drivers. By 2030, these sectors are projected to account for \$1.1 trillion in additional demand, or around 37% of the industry's growth.

To gauge the opportunities in different end markets, we analyzed more than 3,000 earnings calls by 280 industrial-tech companies, as well as hundreds of market intelligence reports. We also estimated production volumes and demand shifts in five key sectors spanning 158 product segments. (See “Our Methodology.”)

## - Our Methodology

To estimate the size of the global market for the industrial-tech industry, we grouped products into five sectors (shown in the exhibit below):

\- Machinery and Components. With \$2 trillion in global revenue and a projected CAGR of 3.3% through 2030, these products include stationary machinery, general-purpose equipment, other instruments and subsystems, base components, mechanical components, process components, and electric base components.

\- Industrial Automation. With \$1.3 trillion in global revenue and a projected CAGR of 12.5% through 2030, these products include software for plant operations, digital-enabling technology, intelligent field modules, identification systems, actuators, field controls, smart elements, and industrial information technology infrastructure and connectivity.

\- Building Technologies. With \$900 billion in global revenue and a projected CAGR of 4.6% through 2030, these products include building systems and building components.

\- Off-Highway Mobile Machinery. With \$600 billion in global revenue and a projected CAGR of 3.9% through 2030, these products include machinery for the agriculture, construction, mining, rail, and forestry sectors.

\- Green-Tech, Propulsion, and Power-Generating Equipment. With \$1.1 trillion in global revenue and a projected CAGR of 4.5% through 2030, these products include green-tech equipment, fluid and process power equipment, and engines and mechanical power.

<table><tr><td></td><td>CAGR, 2010-2015 (%)</td><td>CAGR, 2025-2030 (%)</td></tr><tr><td>Machinery and components</td><td>8.5</td><td>3.3</td></tr><tr><td>Industrial automation</td><td>46.8</td><td>12.2</td></tr><tr><td>Building technologies</td><td>11.8</td><td>4.6</td></tr><tr><td>Off-highway mobile machinery</td><td>2.6</td><td>3.9</td></tr><tr><td>Green tech, $^{1}$  propulsion, and power-generating equipment</td><td>14.8</td><td>4.5</td></tr></table>

## The Industrial-Tech Industry Is Diverse

![](images/ab3a7160fdaf1190a25943e4eaace5e03c3640def8dc79099df2a9ac7d189c68.jpg)  
Source: BCG markets model.  
$^{1}$ Green tech refers to equipment and machinery for low-emission industrial applications.

These sectors cover 158 product segments. We aggregated the market size for each segment by drawing on hundreds of reports from leading providers of market intelligence. We then mapped the market for target verticals. We leveraged capital expenditure data for specific countries from Oxford Economics to estimate the size and growth trajectories of all 158 segments across verticals and geographies. According to this analysis, we project continued growth across all industrial-tech segments through 2030. (See the exhibit below.)

Steady Growth Is Projected Across All Industrial-Technology Segments

![](images/2d4a407bf20f1603f44c7de3d2afd39e93b2cde4ad9e868985a7021d065bd329.jpg)  
Source: BCG markets model.  
$^{1}$ Green tech refers to equipment and machinery for low-emission industrial applications.

The implications of our research are clear: in many instances, the winners of the past will not be winners in the future. To succeed, manufacturers should consider transforming their business models and adapting their product and service offerings. For many companies, that will mean letting go of old assumptions and considering new alliances. It may also mean acting boldly on what might be a painful change agenda to foster the resilience and flexibility needed to thrive in uncertainty and capture emerging opportunities in a new industrial era.

## A Shifting Industrial-Tech Value Pool

We divide industrial technology into five key sectors: machinery and components; industrial automation; building technologies; off-highway mobile machinery; and green tech, propulsion, and power-generating equipment. In this article, we focus specifically on the end-market opportunities for industrial-tech suppliers within these sectors—as opposed to the growth trajectories of the sectors themselves. Although global investment in renewable energy, for example, will continue to expand, there will be more limited opportunities for US and European suppliers of machinery and industrial automation.

Industries such as construction, high-tech electronics, and processed foods have been sources of steady growth for industrial-tech suppliers. But until recently, several growth drivers really stood out: the industrialization of China, the automotive sector, and the green transition. For suppliers, the old success formula changed little: develop strong relationships with OEMs, ensure mechanical excellence, and keep generating incremental innovation. European machinery companies were among the biggest winners, accounting for about one-third of global output as of 2018. But that landscape has changed dramatically.

The China Challenge. China alone accounted for one-quarter of all global industrial-tech sales from 2015 through 2020. Although China's domestic industrial-tech market remains attractive for foreign suppliers that are already well established there, export opportunities for European and American manufacturers are diminishing. China is now self-sufficient in much of the machinery and equipment it needs. China's market is also more challenging for new entrants to penetrate because of local sourcing rules and the presence of domestic manufacturers that benefit from supportive industrial policies, cost advantages, and a knack for rapid execution.

In fact, China is now the world's dominant producer of photovoltaic cells, batteries, networking equipment, and other goods. It also has significant overcapacity. Chinese manufacturers are competing head-on with Western machinery and equipment manufacturers in their home markets. And they're expected to grow stronger. In many cases, Chinese producers have caught up with or even surpassed their Western counterparts in technological know-how.

To better compete in China, European suppliers are giving greater autonomy to their local operations so they can more flexibly navigate the market. To defend their global market share from low-priced Chinese competition, some midsize European companies are securing support from deep-pocket investors, such as private equity firms. IFM, for instance, in May 2025 partnered with KKR to jointly navigate the country’s business landscape in this new era. Others are partnering with Asian competitors or exiting markets altogether when it appears that they will no longer be able to compete in the long run. Viessmann, for instance, combined its heat pump business with Carrier’s after realizing that scale will be a key success factor going forward.

The Decelerating Automotive Market. The automotive market is weakening. The transition from internal combustion engines to electric vehicles translates into less demand for machinery because EVs require fewer mechanical parts. While the automotive market accounted for 9% of industry demand from 2010 through 2015, that share is projected to drop to only 4% through 2030.

Shifting competitive dynamics in the auto sector are also affecting industrial-tech suppliers. Asian OEMs have been growing by more than 10% annually since 2023, which has given Asian suppliers an edge. European OEMs, by contrast, have lost more than 13 percentage points in market share since 2017. Their margins dropped from 7.4% in 2017 to 5.1% in 2023. What’s more, Chinese and US companies dominate the automotive sector’s big growth areas—such as EV powertrains, batteries, and advanced driver assistance systems—leaving little room for European suppliers. Firms in the US, where EVs as a percentage of sales rose from 5.9% in 2022 to around 8% in 2025, lead in such key technologies as advanced driver assistance systems and EV software. More than \$278 billion in public and private capital has been committed to US EV and battery manufacturing over the past few years.

Speed Bumps in the Green Economy. Although the green economy is projected to keep growing strongly, the market for US and European suppliers of decarbonization technologies will account for just 3% of growth for industrial-tech suppliers over the next five years, compared with 5% from 2020 through 2025. One key reason is lowered expectations that the hydrogen economy will create a large demand for suppliers of electrolyzers, fuel cells, and compression and storage equipment. Forecasters have cut projected 2030 hydrogen production by around half, to 5.5 million tons, far below industry and government ambitions. As a result, many suppliers in the hydrogen economy ecosystem are in restructuring mode. Industrial gas giant Air Products, for example, halted construction of a \$500 million green hydrogen plant in New York in 2025.

Ranked by number of mentions in more than 3,000 earnings calls of more than 280 machinery and industrial automation firms

Some other high-profile renewable-energy projects are viewed as stranded assets, particularly in the US owing to policy changes. ∅rsted cancelled two major wind farms off the coast of New Jersey in late 2023, at a cost of several billion dollars. And while China’s green-tech market continues to grow, European industrial-tech suppliers have been losing ground to domestic manufacturers, which produce most of the world’s green-energy systems and core components. China accounts for around 80% of the world’s manufacturing capacity for solar modules, cells, and wafers.

## The Industry's Rising Value Creators

At the same time that growth in traditional value pools is slowing, defense buildups, data centers, and infrastructure renewal are emerging as key sources of growth. This shift was clear in our analysis of industry sentiment based on the earnings calls of listed US and European industrial tech companies. Aside from inflation and cost pressures—which are driven by economic cycles—data centers, defense spending, and the energy transition were cited most often as key demand drivers. (See Exhibit 1.) This shift is also apparent in revenue trends and forecasts for these firms. (See Exhibit 2.)

EXHIBIT 1 The Shifting Relevance of Demand Drivers  
![](images/5197711c4ad2e1e7a6ec17b7444f56cc749a5c04d17c303e4e88fc860a352b7b.jpg)  
Source: BCG analysis. $^{1}$ Green tech refers to equipment and machinery for low-emission industrial applications.

## EXHIBIT 2

Data Centers and Defense Are Replacing China, Automotive, and Green Tech as Top Value Creators

European and US suppliers' sources of growth in industrial technology (%)

![](images/1d5f428a1d20c266b1786cdb7e68aa551d0270983d7f07d9e696c687503611ca.jpg)  
Source: BCG markets model.  
$^{1}$ Green tech refers to equipment and machinery for low-emission industrial applications. $^{2}$ Other sectors include general manufacturing, pharmaceuticals, and process industries.

Defense is emerging as a new industrial lifeline. Europe's military buildup is projected to generate more than \$900 billion in new spending from 2024 through 2029, an 83% increase. In the US, government goals call for 60% of defense-related goods and services to be sourced domestically. US spending is projected to increase by 11% from 2024 through 2029 on systems including manned and unmanned aircraft, land-based systems, naval vessels, and satellites.

Defense reindustrialization will create new opportunities across the industrial-tech spectrum. For suppliers, defense offers a chance to repurpose capabilities and excess capacity and secure long-term, high-margin, service-heavy contracts. Building technology providers can benefit as governments expand facilities and logistics infrastructure that require secure, energy-efficient, and technologically advanced building solutions.

The defense sector will also boost demand for advanced industrial-automation capabilities. Manufacturers of off-highway mobile machinery, for example, should explore opportunities to leverage existing platforms for defense applications that integrate AI-driven control systems, sensors, and global-positioning and global-navigation satellite systems. In addition, customization requirements for defense customers will increase demand for specialized machinery with complex components, such as five-axis, hybrid additive-subtractive machines.

To succeed, suppliers will often need to innovate more quickly and streamline product development, such as by adopting modular architectures and virtual prototyping. Companies not already established in the defense sector, however, must overcome steep hurdles. Tendering processes are lengthy and require high upfront costs. Industrial ecosystems are complex and require building new relationships. Certification requirements are strict. And supply chains for

critical equipment are a growing bottleneck: lead times for backup generators, for example, have stretched from months to years. To keep pace, operators and suppliers should move toward bulk purchasing, joint investments to achieve scale, and agreements that provide long-term visibility. They should also scale up investments and talent development. And they will need to build new relationships with clients and state-owned stakeholders.

Suppliers that succeed will benefit from stable, long-term demand. Caterpillar, for example, has a five-year, \$1.3 billion contract to supply construction equipment to the US Department of War. In Germany, the defense contractor Rheinmetall has repurposed former automotive plants for military production, and KNDS acquired a factory that it will repurpose to make military-vehicle components.

Data centers are becoming a major high-tech value pool. As recently as five years ago, data centers accounted for just 5% of the industry’s growth. That share has now reached 15%. The sector is expected to keep growing over the next five years, fueled by rising demand for AI, the Internet of Things, and cloud storage. Data centers require a large range of industrial-tech products, which account for more than 10% of the build cost, or more than \$500 million per 500,000 square feet. (See Exhibit 3.)

## EXHIBIT 3

Data Centers Offer Opportunities Across the Industrial-Technology Spectrum

![](images/b24bb556a8338543f58f80fbf3fc85f563bcbe24f19219d2c2c8a0d5b53a991b.jpg)  
Source: BCG analysis.

Power generation equipment manufacturers will likely be prime beneficiaries. The immense electricity needs of data centers are already generating strong demand for on-site, distributed power solutions, such as modular turbines, renewable-energy systems, and hybrid backup systems. This is a space where power equipment manufacturers can secure long-term contracts through pilot microgrids and co-investment models.

Data centers also require climate control, cooling, and power management systems, a significant opportunity for building technology providers. Industrial-automation companies can meet data centers' needs for precision robotics, control systems, and sensor technologies. Industry leaders are already repositioning themselves to compete in this value pool. Ebm-papst, whose core businesses are fans and motors, is providing energy-efficient electronically commutated motor and digital airflow management systems for cooling data centers.

The rising electricity needs of data centers are also boosting demand for grid technology, such as transformers and switchgears, and new power generation capacity. In June 2025, Rolls-Royce announced it will double production of diesel backup generation units for the US market. Johnson Controls has made a significant investment in Accelsius, a specialist in advanced cooling solutions, while Schneider Electric is partnering with tech giant Nvidia to develop next-generation thermal-management systems for data centers. Honeywell and LS Electric are co-developing AI-driven power and energy storage solutions that regulate usage based on capacity, weather, and utility rates.

Infrastructure spending is surging. An estimated \$4.2 trillion in infrastructure investment is projected through 2029, representing a compound annual growth rate of more than 4%. Transportation projects will remain the largest value pool in Europe, with more than \$320 billion in spending planned from 2024 through 2027, while investment in energy-related projects is expected to grow by 4.7% annually.

Infrastructure renewal will translate into stable and rising demand for industrial-tech suppliers, supported by long investment cycles, solid government support, and regional diversification. Building technology providers will see sustained demand for heating, ventilation, and air conditioning systems and for renewable-energy technologies, especially those that meet tightening energy efficiency standards and requirements for digital building management. There will also be robust demand for off-highway vehicles and other equipment.

Global construction machinery sales are forecast to increase by 5.6% per year through 2029, reaching \$400 billion. In the Netherlands, ABB has won a major contract from the water supply company Vitens to modernize around 200,000 input and output connectors at 250 sites. In the US, Siemens Energy has announced that it will employ 560 workers in North Carolina to manufacture power transformers to help modernize the electrical grid.

If our analysis teaches us one thing, it’s that the industrial-tech market remains robust and rich with opportunities to drive growth. But winning in the evolving environment will require many companies to transform their go-to-market strategies, broaden their customer base, and place bets on new regional markets.

The customer universe for most industrial-tech suppliers is evolving from one that was simple and straightforward to one that is becoming more diverse and dynamic. Companies will increasingly need to tailor their business models and offerings to the needs of different sectors. Production

cycles may remain long for traditional customers such as construction firms and vehicle manufacturers. But in the rapidly growing data center industry, customers may require delivery of large orders within months. The processes for winning contracts also vary by sector. To serve defense customers, for example, suppliers must meet the requirements not only of prime contractors but of defense ministries and procurement agencies in different nations as well.

Industrial-tech suppliers also need to take a differentiated approach to global markets. As more nations pursue industrial policies designed to promote strategic domestic industries, they must navigate different trade and investment rules, local sourcing requirements, and financial incentive schemes. In addition, suppliers must carefully weigh geopolitical concerns when choosing which markets to prioritize—and which technology-intensive products they can offer. And they will need the flexibility and agility to capture new opportunities created by future shifts in demand.

## Authors

![](images/67fd3a5a843605f608c8dbff21e1608c5e3769b1957864c597c31d21525ad324.jpg)

![](images/85aee52529e9dadee05b60c81691878292bf110bbd150440bb7f0fd4f7ae4847.jpg)

![](images/3d5df816b2c7347a66e341ff8dab45a2fc4870f735b67c0b3f3510adc43e90d1.jpg)  
Markus Lorenz  
Managing Director & Senior Partner
Munich

![](images/c41e0cdf122da060bea8ceba545846f68b68ec838cff6ced212c11ebfcd7b999.jpg)

## Simon Rees

Managing Director & Partner
Boston

![](images/829d3625d7e10ff1c6cadeccf5dda202dea6c3bc13941a046bfbe0e71f564cec.jpg)

## Bernhard Siegert

Director, Greentech, Machinery & Industrial Technology, BCG Vantage
Munich

![](images/b928704e8d4303031bd00325d8abb864db0968cc7d94d4b106490d317fd4514d.jpg)

![](images/77beb89d8704034f13db1ac178882a02f0f737dc5fb7d4f77b833e462bd8abe4.jpg)

![](images/1ed822fdddd84a307aa759bd5be64111ab6c267204f2ce275501b1a911084a7d.jpg)

![](images/77c2a21690ea5c84debcacfcd18b4f58543c47de95652571cf3d45d9123d60b7.jpg)

![](images/f717389583e7e5e13d2112551cc1bcaeb2280d85e11b8935bf437c4f61d9245f.jpg)

![](images/520d8f5d30e5786b41df64bc2d934e47a73d2adf43bd0b66a9eebbba7506d43a.jpg)

Managing Director & Partner
Munich

## Yoichi Hangai

Managing Director & Senior Partner
Tokyo

![](images/0db0e0932179f6c9088771c1ecf7b9ea37d8332b3d130cf5dbac10992c29234a.jpg)

## Franziska Maassen

Project Leader
Düsseldorf

![](images/f61e0b01e1b0d4f1b08adaae4aa9dc62cb554d69b86c4e1e453bb75c4abd5f2d.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## © Boston Consulting Group 2026. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly Twitter).
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
