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
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# BIS Bulletin

## No 130

AI and the global economy: implications for central banks

Iñaki Aldasoro, Leonardo Gambacorta, Enisse Kharroubi and Matthias Rottner

BIS Bulletins are written by staff members of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks. The authors thank Pablo Hernández de Cos, Phurichai Rungcharoenkitkul, Olivier Sirello and Philip Wooldridge for helpful comments and suggestions, Adam Cap, Andrew Li and Emese Kuruc for excellent statistical assistance and Nicola Faessler for administrative support.

The editor of the BIS Bulletin series are Gaston Gelos and Frank Smets.

This publication is available on the BIS website (www.bis.org).

# AI and the global economy: implications for central banks

## Key takeaways

\- The AI boom is driving a large, increasingly debt-financed investment surge and boosting trade and equity markets, generating sizeable terms-of-trade and wealth effects that differ across countries.

\- The productivity payoff from AI, though potentially large, remains uncertain and uneven, across both sectors and countries.

\- By simultaneously affecting demand and supply, AI blurs cyclical signals, complicating central banks' assessment of underlying economic conditions and monetary policy calibration.

The sustained boom in artificial intelligence (AI) has contributed to surprisingly resilient growth. AI's footprint on investment, trade and asset prices has grown large enough to shape the global outlook in real time. Moreover, it has acted as a powerful countervailing force to trade tensions and geopolitical shocks that have raised energy prices and weighed on growth. In this way, AI has supported aggregate demand, trade, financial market valuations and overall macroeconomic resilience.

This Bulletin assesses how the AI boom is shaping near-term macroeconomic dynamics and the attendant implications for monetary policy and financial stability. It documents four sets of findings. First, AI is driving a large investment and financing impulse: spending on data centres, semiconductors and related infrastructure has reached around 1% of GDP in the most exposed economies, and the associated capital expenditures increasingly rely on public debt markets as well as private credit. Second, these forces are reshaping trade and equity markets, generating sizeable terms-of-trade and wealth effects that differ markedly across countries. Third, the productivity payoff, though potentially large, remains uncertain and uneven and is accompanied by some early signs of labour market softening in the economies most exposed to AI. Finally, by moving demand and supply at the same time, AI blurs the cyclical signals on which central banks rely, thereby complicating monetary policy calibration.

## AI as a driver of short-term macroeconomic dynamics

AI affects economic activity through channels that operate via aggregate demand and supply. On the demand side, AI is driving a powerful investment cycle, lifting the valuations of AI-related firms and reshaping trade flows. On the supply side, AI promises to raise productivity over time. The demand side effects are already large and observable; the supply side effects, while potentially more consequential, remain uncertain in scale and timing. Because these forces affect growth, labour markets and inflation in different – and sometimes offsetting – directions, AI's net macroeconomic impact is unclear and will likely vary across countries and over time.

A broad investment boom and its financing. The promise of AI has unleashed a global investment boom. AI-related investment already accounts for a material share of GDP in some countries (Graph 1.A). This spending spans data centres, specialised chip manufacturing facilities, cloud infrastructure and hardware, and has also bolstered investment in information technology (IT) products and software more broadly. $^{1}$ Available estimates point to a sharp increase in AI-related investment: in the United States and Australia, where more granular investment data are available, estimated spending on data centres (including the IT equipment they house) and IT manufacturing facilities rose steeply to 0.8% and over 1% of GDP, respectively (purple and brown lines, right-hand scale). Industry participants expect global AI-related investment to grow further – from 500 billion today to 3–4 trillion by 2030 – while capital expenditures on data centres are projected to triple by 2030 (Graph 1.B).

## AI firms are growing rapidly and so are AI-related investments

![](images/56b1120c4c7369658f1e06f00f016d782ea5ca466ad53dba2abd01009e919d0f.jpg)  
$^{1}$ For EA, estimates for 2025. See the online annex for details. $^{2}$ Projections are for global spending on AI infrastructure and data centres. See the online annex for details. $^{3}$ Revisions to 2026 GDP growth forecasts and the contributions of some GDP components. Forecasts are displayed by publication month; survey cutoff precedes this by several weeks.

Sources: Aldasoro et al (2026); Federal Reserve Bank of St Louis; IMF; US Census Bureau; Dell'Oro Group; Focus Economics; Gartner; Goldman Sachs; LSEG Datastream; Omdia; Reuters; Wind Economic Database; national data; BIS.

AI investment has been a significant tailwind to growth. AI-related capital expenditures supported aggregate investment, which has been an important driver of upward revisions to growth forecasts across several countries (Graph 1.C). In line with this, business investment has grown faster in economies with higher scores in an AI preparedness index (AIPI) than in those with lower scores (Graph 2.A). $^{2}$ The fact that total investment is also higher for countries with a high AIPI score suggests that business investment growth has not come at the expense of less investment elsewhere, ie housing or public sector investments (Graph 2.B).

The AI investment boom has also reshaped trade through supply chain linkages that run from semiconductors to data storage and digital infrastructure. These shifts are clearly visible in trade data, where goods with high AI content have recorded the fastest rates of export growth (Graph 3.A). Although volumes have risen, a large part of the increase in exports reflects higher prices. Granular data from the United States show that export prices for goods with high AI content climbed markedly over the past two years, even as prices for other goods fell or stayed broadly flat (Graph 3.B).

AI preparedness raises business investment and supports total investment at the low end of the distribution $^{1}$

![](images/87ed8c3e468bc3945734c89a21b9636b7b0ea974df81f358803f90c88bad1992.jpg)

![](images/6f767c45b93cf531741b14f9836fb95c57925147bd852d2dfe07ec0b8026e61f.jpg)  
$^{1}$ AIPi = AI preparedness index. “High AIPi” refers to countries with AIPi scores above the sample median. AIPi scores reflect the capacity to adopt, develop and benefit from AI technologies. See the online annex for details. $^{2}$ The solid blue line plots the difference in cumulative business investment growth since Q4 2023 between countries with high and low AIPi scores. The dashed blue line shows projections based on OECD forecasts. Country sample: AU, CA, DE, DK, FI, FR, GB, JP, KR, NL, NO, NZ, SE and US. $^{3}$ Lines plot the distribution of gross fixed capital formation as a share of GDP, based on quarterly national accounts data for countries with an AIPi score above and below the sample median. Sample: 32 economies (24 advanced economies and eight emerging market economies) over Q4 2023–Q4 2025.  
Sources: IMF; OECD; national data; BIS.

Strong AI-related investment has put upward pressure on AI investment input prices, not least because investment by AI firms has far exceeded that by semiconductor producers. As a result, the impact has been uneven along the AI supply chain. Upstream exporters of AI-related goods (eg semiconductors) – such as Korea, Chinese Taipei, Malaysia and Singapore – have seen export prices outpace import costs, delivering sizeable terms-of-trade gains. This has caused national income and purchasing power to increase by substantially more than real GDP, which measures production volumes.

## AI delivers an export boom, but with price pressures building up

![](images/671620860175868a75c2677e8b48367aa5e52a2d709ddb9b66bf7ea3d131cea3.jpg)

![](images/1b6cba4c7c05a1eb66a7d9358779520d5de035a37b9b8e9a866145b63b695745.jpg)  
$^{1}$ Annual growth rate of exports for different categories of goods and total exports. $^{2}$ Lines plot the US export price indices for goods with high AI content and other goods, rebased to 100 in February 2023.  
Sources: Waugh (2026); UN Comtrade; China Customs; Focus Economics; BIS.

These gains have, however, been narrowly concentrated. In Korea, for example, five firms accounted for 43% of export earnings in the first quarter of 2026, up from 27% two years earlier. By contrast, countries expanding their digital infrastructure often need to import large quantities of AI-related goods, with the higher prices of these goods weighing on their terms of trade. In line with this, terms of trade have weakened in economies with higher AI digital infrastructure scores (Graph A.2.A in the online annex), partly because the cost of imported AI-related equipment and infrastructure has risen.

Financial markets have amplified the demand impulse from AI, although here too the effects have been uneven across countries. The weight of AI firms in equity markets has risen sharply, supported by strong earnings. In the United States, their share of total market capitalisation climbed from 24% to 40% between 2022 and 2025, with similar, though less pronounced, developments in other economies integrated into the AI production chain (Graph A.3.A in the online annex). By contrast, equity markets with more limited exposure to AI production have generally recorded weaker performance. Higher valuations have generated wealth effects for asset-holding households, supporting consumption (notably in the United States and, to a lesser extent, the euro area).

Beyond equity valuations, the scale of AI investments has implications for financial markets in terms of financing. As AI firms' capital expenditures have increased markedly in recent years, free cash flows have shrunk significantly (Graph A.3.B in the online annex, red arrows). This prompted a shift to debt financing, with two sources standing out. The first is private credit, which has grown particularly fast in the United States (Aldasoro et al (2026)). Outstanding private credit loans to AI-related firms grew from near zero in 2016 to \$200 billion in 2025, while their share in total private credit loans rose from less than 2% to 8% over the same period (Graph A.3.C in online annex). The second financing source is bond markets. AI firms raised \$243 billion through bonds in 2025, up from \$79 billion in 2023 (against total non-financial corporate bond issuance of around \$3.0 trillion and \$2.1 trillion, respectively) (OECD (2026)). While US-based AI firms account for most of this, issuance is also increasing elsewhere, albeit from a lower base.

An uncertain productivity payoff. AI also affects activity through productivity, although the size and persistence of these effects remain highly uncertain. Early micro evidence suggests that generative AI can deliver sizeable productivity gains, particularly by automating components of non-routine cognitive tasks. Evidence also suggests that AI compresses performance differences, as less experienced workers often benefit more than senior ones (Graph A.4.A in the online annex). Whether these micro-level gains will translate into higher aggregate total factor productivity (TFP) remains uncertain. $^{3}$ While the range of macro estimates is relatively wide, the median TFP growth gain is around 0.5 percentage points per year (Graph A.4.B in the online annex). Cross-country evidence suggests that some of these effects may already be materialising, with higher AI preparedness as of 2023 correlating positively with labour productivity growth over the subsequent two years (Graph A.5.A in the online annex).

Economic growth and the labour market. The growth effects of AI will reflect both the demand and supply side factors described above. Therefore, they currently vary substantially across countries, reflecting differences in economic structure, the scale of AI-related investment, the countries' capacity to adopt and deploy the technology, or the presence of demand bottlenecks that may constrain the growth benefits of AI (BIS (2026)). The available evidence suggests that advanced economies (AEs) are better positioned to capture the near-term gains, while outcomes across emerging market economies (EMEs) are more heterogeneous (Graph A.5.B in the online annex; Gambacorta et al (2025)).

Beyond its effects on GDP growth, AI could also reshape labour markets. Two broad forces are at work: complementarity between generative AI and tasks that benefit from human input, and substitution for routine cognitive tasks that can be fully or partially automated. So far, labour displacement has been limited, although some early signs are emerging in specific tasks and occupations (ie call centres, business centres). Many firms remain in a “wait-and-see” phase, experimenting with AI technologies but still facing uncertainty regarding regulation, costs, organisational adaptation and the reliability of AI systems, consistent with the current “low hiring, low firing” dynamics observed in several jurisdictions.

Even so, corporate behaviour points to an intensifying impact. In recent earnings calls, nearly 80% of firms indicated plans to automate a growing share of production processes and increase labour substitution (Graph 4.A). Consistent with these soft indicators, employment growth in the United States has been weaker in sectors with higher AI exposure: between the third quarter of 2023 and the third quarter of 2025, employment in high AI-exposure sectors grew around 0.8 percentage points less than in low AI-exposure sectors (Graph 4.B). Unemployment trends tell a similar story. Countries with a high AICI score saw unemployment rates increase by 0.75 percentage points on average between 2023 and 2025; those with low AICI scores saw flat unemployment rates (Graph 4.C).

## AI could pose some risks to labour markets

![](images/ea00cb2eb9462cdca91bcddf81997807367487e5b31e0847980be099952419a0.jpg)

![](images/32430c4ff2f4498dba3785e08ecb4dbce453c72b80017874d73960405936a583.jpg)  
Graph 4

![](images/4e45f098951470e47843c80dc823e50527586832b89ac36fda7cf269d8e7535b.jpg)  
$^{1}$ Share of companies reporting the following in their earnings calls: early stage or advanced use of AI within the business, significant positive impact of AI on company productivity and actual or potential reduction in labour input due to AI or automation. Based on earnings call analysis using a large language model. $^{2}$ Estimates based on a cross-sectoral period-by-period regression where cumulative employment growth is regressed on the Q3 2024 log of employment and Q3 2024 sectoral exposure to AI in the United States. Sectoral exposure to AI measured as the fraction of data scientists in sectoral employment in Q3 2024. $^{3}$ Solid lines plot the median change in unemployment rate relative to 2023. Dotted lines display the respective interquartile ranges.

Sources: Kansal and Rungcharoenkitkul (2026); BIS (2026), IMF; OECD; US Bureau of Economic Analysis; US Bureau of Labor Statistics; S&P Global Market Intelligence; BIS.

AI may also create skills mismatches by increasing demand for workers with AI-related and complementary skills. When the skills of unemployed workers do not match those required for newly created jobs, labour market matching efficiency may decline. Consistent with this mechanism, economies that are more advanced in AI adoption tend to exhibit a steeper vacancy-unemployment relationship than countries with lower AI preparedness (Graph A.6 in the online annex).

Impact on inflation. The channels discussed above point to opposing short-run inflation pressures. On the one hand, AI-related investment, trade and wealth-driven consumption can boost aggregate demand and add to price pressures. On the other hand, productivity gains, if they occur, would expand supply, helping to contain inflation. Concerns about AI-induced job losses could also curb demand, wages and, in turn, inflationary pressures. The relative strength and timing of these forces, however, remain uncertain.

Beyond the strength and direction of effects, there are differences in their timing. AI could exert upward pressure on inflation before becoming disinflationary as productivity gains broaden and supply adjusts. Near-term inflationary effects may already be emerging, albeit modestly (Abecasis (2026)). Disinflationary effects from higher productivity or changes in workers' perceptions of their bargaining power are likely to emerge more gradually. Canonical macro models suggest AI tends to be inflationary, as households boost consumption in anticipation of stronger future income growth. And even if they do not anticipate the AI boom, financial markets may, in turn, lift household consumption through wealth effects. The effects on inflation are more muted (possibly even reversed) if the AI-led productivity boom exceeds expectations or if households restrain consumption against potential labour displacement.

## Implications for central banks

The considerable uncertainty surrounding the effects of AI raises several challenges for monetary policy and financial stability. For one, AI simultaneously affects demand and supply, in both cyclical and structural ways. Moreover, the effects differ across sectors, complicating the assessment of underlying trends. Strong activity may reflect temporary demand factors (eg investment booms and wealth effects) rather than sustained increases in potential output, while productivity gains are uneven and hard to measure. The AI boom may thus alter key unobservable benchmarks, including the natural rates of interest and unemployment, frequently used in monetary policy analysis.

Greater uncertainty increases the risk of policy miscalibration. If central banks overestimate supply improvements or underestimate the rise in underlying demand, policy may remain too accommodative; the opposite risk could lead to unnecessarily restrictive conditions. In this environment, a gradual and data-dependent approach may help reduce the risk of policy errors.

The AI boom could also have important financial stability implications. For one, AI can disrupt the business models of specific sectors and generate negative spillovers to their stock prices and employment prospects, as experienced by software as a service (SaaS) companies in February 2026. In some jurisdictions, large export windfalls may also risk contributing to domestic asset price bubbles. More broadly, a key risk at the current juncture is that expectations about the transformative impact of AI may be overly optimistic, raising the risk of overinvestment, resource misallocation and weaker credit quality. A correction in asset prices could tighten financial conditions, dampen investment and weaken aggregate demand, as discussed at greater length in BIS (2026).

## References

Abecasis, M (2026): "AI and (measured) inflation: up then down", Goldman Sachs, US Economics Analyst.

Aldasoro, I, S Doerr and D Rees (2026): "Financing the AI boom: from cash flows to debt", BIS Bulletin, no 120.

Bank for International Settlements (BIS) (2026): "Progress and peril", Annual Economic Report 2026, Chapter I.

Brynjolfsson, E, D Rock and C Syverson (2021): "The productivity J-curve: how intangibles complement general purpose technologies", American Economic Journal: Macroeconomics, vol 13, no 1.

Cazzaniga, M, F Jaumotte, L Li, G Melina, A Panton, C Pizzinelli, E Rockall and M Mendes Tavares (2024): "Gen-Al: artificial intelligence and the future of work", IMF Staff Discussion Notes, no 2024/1.

Gambacorta, L, E Kharroubi, A Mehrotra and T Oliviero (2025): "Artificial intelligence and growth in advanced and emerging economies: short-run impact", BIS Working Papers, no 1321.

Kansal, R and P Rungcharoenkitkul (2026): "AI impacts on firms: insights from earning calls", mimeo.

Organisation for Economic Co-operation and Development (OECD) (2026): Global debt report 2026: sustaining debt market resilience under growing pressure.

Waugh (2026): "Trade in AI-related products", NBER Working Papers, no 35053.
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
