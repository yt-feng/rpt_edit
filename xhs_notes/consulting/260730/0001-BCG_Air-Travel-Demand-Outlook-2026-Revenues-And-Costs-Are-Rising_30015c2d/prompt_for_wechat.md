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
## Revenues—And Costs—Are Rising

Air Travel Demand Outlook 2026

![](images/78d62b828e9db206dc6c5e293bb865628ddeb46698935739b197dd064d0fe90a.jpg)

## Five trends to watch for in 2026 and beyond

## 1

Macro factors
driving volatility

Geopolitical turbulence (e.g., tariffs), economic uncertainty, and infrastructure reliability (e.g., air traffic controller shortages, IT outages) continue to affect supply and demand patterns, driving volatility for airlines worldwide

Divergence in margins

The airline industry is in a period of profitability, although profits are not distributed evenly, as FSC and LCC performance diverges in North America and Asia-Pacific

Cost focus and emerging AI use cases

Growth in CASK is outpacing RASK, leading airlines to explore permanent shifts in cost structure, such as consolidation or leveraging AI to help cut costs

## Easing OEM delays

While there is cautious optimism that aircraft production will ramp up, any growth remains vulnerable to raw material and labor shortages, supply chain disruptions, and increasing regionalization

## 5

## New fleet types

Fleet types such as the A321XLR are entering the market at scale, and networks are being reshaped with new cost structures as a result. For example, XLR aircraft can open transatlantic narrowbody routes, and A350-1000 ULR aircraft will enable ultra-long-haul flights

## Three macro factors create volatility for aviation by shifting supply and demand patterns

## Air Travel Demand Shifts Changes to passenger buying patterns

## Air Travel Supply Shifts Changes to flight availability

Lower leisure demand, declining business travel

Travel visa
restrictions

Airspace or
airport closures

ATC staffing shortages,
IT outages

![](images/f63b051799f1df794624cf406f2ae0126aafa8287ac950e82aad16b2712cfa47.jpg)

## Economic uncertainty

\- Consumer sentiment and spending power Changes in GDP growth, the job market, recession risks, or consumer discretionary spending

\- Unclear business outlook Uncertainty affects business and investor confidence, decreasing cross-border business and investment activity (e.g., accessing credit becomes more difficult)

Note: Fuel price is currently stable, but in other years may be a source of uncertainty

![](images/056f4be921c19d1c7b4910700fa2e2266256dc3e7f997b94e2da4d67bac9470b.jpg)

## Geopolitical turbulence

• Trade and tariff realignments Policy shifts, tariffs, and export controls disrupt global supply chains and corporate planning

\- Regional conflicts Ongoing or emerging conflict zones threaten infrastructure and create defense risks

\- Fragmentation of alliances and global institutions Weakening of multilateral frameworks and competing blocs increases unpredictability in regulation and cross-border operations

![](images/d9b37cfa1eec05a5e97bcc093fa63eefd61b195dab03ad72d43bd2ea83162d60.jpg)

## Infrastructure reliability

\- Governance and oversight High public debt and government disruptions constrain ability to make decisions or investments in infrastructure

• Labor shortage Public infrastructure is understaffed, leading to service gaps

\- Aging IT/cyber attacks IT infrastructure is built on aging technology, highly dependent on a few key players, and vulnerable to cyber offensives

## Macro factors will likely continue shaping air travel in 2026 and beyond

<table><tr><td rowspan="2"><img src="images/9e554b5f8620af06926eeb857242ecb012a9a03a3dad17734f3840dbe0ab776d.jpg"/></td><td>· International business travel spending remains stable, though concerns around visa requirements and border permissions persist</td></tr><tr><td>· Premium economy and business class flights will make up a greater share of all flights as population growth slows and GDP per capita rises (e.g., China&#x27;s population is projected to remain flat while GDP per capita rises about 50% to 60% over the next ten years)</td></tr><tr><td>Economic uncertainty</td><td>· US consumer demand for premium products will grow, with tax reforms favoring upper-income households while reducing benefits (e.g., SNAP and Medicaid) for lower-income groups, potentially impacting the market for budget fares</td></tr><tr><td rowspan="2"><img src="images/04657f1611da80af4bc332ce86b9fefd86e6e43d478b4ea821a4b17734dd1c6a.jpg"/></td><td>· Airspace closures in the Middle East, Pakistan, and Europe are likely to persist and may worsen, making routes unviable, increasing stage length, and requiring greater operating flexibility to respond to sudden changes</td></tr><tr><td>· An ~6x increase in tariffs on imported goods to the US—especially on parts, FF&amp;E, and infrastructure materials—will raise costs and increase pressure throughout the supply chain; in addition, the outcome of the US Section 232 probe into commercial aircraft is pending and may result in tariffs and/or quotas</td></tr><tr><td>Geopolitical turbulence</td><td>· Canada/US transborder demand will likely not recover to 2024 levels; however, overall North American demand will remain steady, with Canada/US transborder travel spending shifting to Mexico, APAC, and the EU</td></tr><tr><td rowspan="2"><img src="images/77d80a7500d130a646317c466b395870e2d5b06441eea865026aa73a7028d30d.jpg"/></td><td>· Across all regions, airport reliability issues will likely persist</td></tr><tr><td>· Airport delays and closures (e.g., due to ATC shortages across the EU and North America) may increase, constraining airport throughput</td></tr><tr><td rowspan="2">Infrastructure reliability</td><td>· Day-of disruptions due to ATC staffing shortages in peak months or during airport construction may increase</td></tr><tr><td>· IT systems may become more vulnerable to cyber attacks and outages from individual vendors</td></tr></table>

## Airport disruption rates can shift rapidly due to seasonality and unforeseen macro shocks

Europe: About 7K cancellations per month, shifting around 50% to 60% between months

MONTHLY FLIGHT CANCELLATIONS 2025  
![](images/61dd1cae775c1e1091cda7584ea61b565c1bd7b9b0bd144536a7ae09fc7efebd.jpg)  
MONTHLY FLIGHT CANCELLATIONS 2025

"Helsinki ground services strike...led to cancellation of more than 1,200 Finnair flights since early spring"
—Helsinki Times (July 13, 2025)

North America: About 11K cancellations per month, up 200% in November due to staffing shortages during the US government shutdown

"France ATC strike July 3–4...across Europe, 1,422 flights were cancelled (4.7% of all scheduled flights) each day on average, affecting more than 1 million passengers"
—EUROCONTROL (July 10, 2025)

![](images/1a200dce23c1c4240e97e480157bb9fd15f809ec95f404b650194a24a531d265.jpg)

"Sightings of 2–3 large drones in Denmark...halted all takeoffs and landings for nearly four hours at Copenhagen airport in what prime minister called a serious attack on Danish critical infrastructure. Aalborg and Billund airports also closed later in the week due to drone activity"—CNN (September 26, 2025)

“Since US government shutdown ...as many as 53% of airport delays are due to ATC staffing shortages, compared to an average of about 5%. Since the shutdown began, 222 staffing shortages have been reported, more than 4x the same dates last year”

—CNN (October 24, 2025)

## Aside from macro shocks, four systemic factors will continue to affect airport reliability in 2026

• Capacity constraints (e.g., limited gates)

\- Construction (e.g., buildouts causing gate and runway closures)

\- Structural staffing shortages (e.g., persistent ATC shortages in many countries)

• Aviation authority technology (e.g., IT outages affecting ATCs)

<table><tr><td rowspan="2" colspan="2">Profits are not being realized evenly, as FSC and LCC margins diverge in North America and Asia-Pacific</td><td colspan="2">AVERAGE LTM OPERATING MARGIN1</td></tr><tr><td>FSC</td><td>LCC</td></tr><tr><td>Global2</td><td>FSCs and LCCs are both able to realize positive margins, with FSCs outperforming overall</td><td>8.4% outperform</td><td>4.6%</td></tr><tr><td>North America</td><td>FSCs outperform by capturing a range of demand using premiumization and fare segmentation, while LCCs struggle and start to explore hybrid models</td><td>3.6% outperform</td><td>-2.2%</td></tr><tr><td>Europe</td><td>LCCs slightly outperform, though leading players in both categories operate at margins of 15%+</td><td>7.4%</td><td>8.2% outperform</td></tr><tr><td>Asia-Pacific</td><td>Performance varies widely as FSCs capitalize on long-haul and premium fares, while LCCs respond more quickly to rising demand from the growing emerging-market middle class</td><td>7.5% outperform</td><td>2.8%</td></tr></table>

Sources: S&P Capital IQ; company filings; BCG analysis.  
Note: Reflects information available as of November 2025. FSC = full-service carrier; LCC = low-cost carrier; LTM = last twelve months.  
$^{1}$ Measured from Q4 2024 to Q3 2025. $^{2}$ Based on a group of 52 full-service carriers and 36 low-cost carriers across Europe, North America, Asia-Pacific, Latin America, and the Middle East.

## Full-service carriers maintain profitability across regions despite rising costs

<table><tr><td>North America</td><td>·Legacy carriers capture the full demand spectrum, with ongoing premiumization supporting revenue mix·Loyalty and co-brand monetization (e.g., co-branded credit cards) continue to stabilize US big-three airlines’ margins·Canada underperforms, pressured by soft demand and high costs</td><td>3.6%(across 7 FSCs)</td></tr><tr><td>Europe</td><td>·Capacity discipline and premium demand (especially transatlantic) underpin margins for leading carriers·Airspace disruptions and higher ATC costs continue to weigh on margins, especially for Europe-Asia routes·Ongoing consolidation and joint ventures (e.g., Lufthansa–ITA) expected to drive future scale and margin upside</td><td>7.4%(across 18 FSCs)</td></tr><tr><td>Asia-Pacific</td><td>·Regional recovery uneven, with Japan and India performing well, but Chinese FSCs still below pre-COVID profitability·Re-opening tailwinds fading as yields normalize; competition from Gulf carriers on long-haul flights remains a structural challenge·FSCs leaning on partnerships and joint ventures to rebuild long-haul profitability</td><td>7.5%(across 20 FSCs)</td></tr><tr><td>Latin America</td><td>·FSC margins recovering strongly as carriers maintain discipline on capacity and yield management</td><td>17.0%(across 4 FSCs)</td></tr><tr><td>Middle East</td><td>·Capacity expansion and fleet renewal continue to support strong margins, although exposure to geopolitics remains a risk</td><td>14.4%(across 3 FSCs)</td></tr></table>

Sources: S&P Capital IQ; company filings; BCG analysis.  
Note: Reflects information available as of November 2025. LTM = last twelve months; FSC = full-service carrier; ATC = air traffic controller.  
$^{1}$ Measured from Q4 2024 to Q3 2025 for select FSCs by region.

## LCC performance is steady in Europe, while North America and APAC have both stronger and weaker performers

AVERAGE LTM OPERATING MARGIN $^{1}$ FOR GLOBAL FSC PEER SET

<table><tr><td>North America</td><td>·LCC margins lag sharply as cost inflation (e.g., wage increases) and pricing pressures erode short-haul profitability·Business model strain is evident as several carriers move toward hybrid models (e.g., FSC loyalty partnerships, service upgrades)·Fleet utilization and industrywide labor cost headwinds limit competitiveness versus larger FSCs</td><td>-2.2%(across 7 LCCs)</td></tr><tr><td>Europe</td><td>·Strongest LCC region globally; top carriers continue to grow share while maintaining a conservative balance sheet·Point-to-point leisure demand remains resilient; yields stabilizing after exceptional 2023 highs</td><td>8.2%(across 8 LCCs)</td></tr><tr><td>Asia-Pacific</td><td>·Robust domestic growth in India and Philippines creating opportunities for scale and network expansion·Competitive intensity rising as multiple carriers expand simultaneously, leading to yield compression in select markets·Market is sensitive to currency fluctuations (e.g., current traffic increase in Japan due to low Yen)</td><td>2.8%(across 13 LCCs)</td></tr><tr><td>Latin America</td><td>·LCCs facing financial strain as multiple carriers operate under restructuring amid persistent cost inflation and FX weakness</td><td>7.0%(across 3 LCCs)</td></tr><tr><td>Middle East</td><td>·LCC profitability among highest globally, benefiting from government-backed tourism initiatives</td><td>14.0%(across 2 LCCs)</td></tr></table>

Sources: S&P Capital IQ; company filings; BCG analysis.

## Margins are under pressure globally as CASK increases outpace PRASK

Includes FSCs and LCCs

All regions see modest yield growth, with North America leading LTM YOY% CHANGE IN PRASK $^{1}$

![](images/a66fb1f732b37e1d71b169a8b4bd81ed7fd7d758e2832f346b6e7e26fbbc7773.jpg)  
- LCCs and aggressive capacity increases are pressuring yields, especially in short- and medium-haul markets  
However, CASK growth outpaces PRASK across the board
LTM YOY% CHANGE IN CASK EXCL. FUEL $^{1}$

\- Fuel surcharges and COVID-era ancillary revenue (e.g., flexible ticket fees) have eased, stalling total unit revenue growth

![](images/564b68320958fdc1bdbf9c959c46eace774f6261c9872b99c551526530f1a6bd.jpg)  
- Europe: Labor negotiations and inflation-driven airport and handling costs are inflating CASK  
CASK deep dive: increase in CASK, driven by MX, crew, and other costs
LTM YOY% INCREASE IN COST PER ASK $^{1}$

\- North America: Cost base pressured by crew and handling cost inflation, partly offset by easing inflation within other cost buckets

![](images/7fb566a940c9a63c2b7197318392d543ad87bff47056f8343b8410e037de8e17.jpg)

\- Crew costs remain a key inflation driver, up 5% to 7% YoY in 2025, following major contract renewals across Europe and North America

\- Ground handling costs continue to increase (4% to 7% YoY in 2025) as airport and third-party providers pass through wage and inflation adjustments

\- Maintenance costs stable overall, with some pressure in APAC

## As cost pressure mounts and carrier performance diverges, airlines look to permanently shift cost structures

## Returning to fundamentals with holistic cost-out programs

![](images/711b4d9239669d79c94c627444b2c6f2de8b7727ccb6474cc655a02468d49936.jpg)

Identify levers to drive savings, including maintenance, fuel, crew, airport operations, IT, guest experience, and corporate

![](images/45b0a57a5bf5c018cac12e7cf8ed49b544d7cfea8820d57e3ae1b2efcef928e1.jpg)

Find the optimal sequence for cost initiatives by prioritizing early quick wins to showcase early impact

![](images/c6501ed80c33a9bfd66fce150af2eb70e9e30bd071cbfc6ca0a5d0a687322623.jpg)

Realize savings with successful implementation and governance (e.g., maintain central roadmap and conduct rigorous tracking)

![](images/a136e56e4637469c5e8ae947741cea7ac40e38a0a4f628739c329602cb10bd08.jpg)

Sustain cost leadership position over the long term by articulating an organization-wide cost culture and aligning incentives with cost goals

BCG experience suggests a 5% to 10% savings opportunity with full airline cost transformations

## Incorporating AI for structural 5% to 6% margin advantage over peers

Airline AI leaders $^{1}$ have higher IT budgets and invest more in AI...

1.2x

![](images/605819960ba3305ca03d5c042907f45ed152bff1eae17bf90858a2d1b7610586.jpg)

IT budget 2025 $^{2}$

Share of IT budget for AI 2025 $^{3}$

...fueling revenue growth and cost efficiency...

4.9%

5.8%

Expected revenue increases from Al $^{3}$

Expected unit cost decreases from AI $^{4}$

...meaning sustained advantage for margin leaders

5.4% Projected operating margin benefit for AI leaders

## Exploring consolidation to find margin through scale

\- Combine overlapping networks to get scale in mainline network, cargo, and/or LCCs (e.g., Air Busan–Air Seoul–Jin Air merger)

\- Join complementary networks, fleets, and loyalty programs to improve ability to compete on product and network depth (e.g., Alaska Airlines acquisition of Hawaiian Airlines)

\- Increase negotiation power with OEMs (e.g., better discounts and after-market service conditions)

\- Stabilize airlines that have weaker financial performance

## AI USE CASE

## Al-based recommendations for operations and network control can result in more efficient utilization of fleet and 30% to 40% reduction in delays

## Today

## Predictive insights in the ops center

\- Centralized control decisions must be made quickly leading into and during “day-of” operations

\- Vast data is available, but difficult to combine and meaningfully synthesize

\- Data governance and capture have not evolved, meaning data either not present, not well-segmented, or unreliable

![](images/087fd0ef655760cd6c9217fec57e17c5f677ba1fb6ade6aacce41e0dcd71de6d.jpg)

## Innovative case study

## Pathfinder fleet assignment tool

• Who: KLM Royal Dutch Airlines (in partnership with BCG)

\- Tool for operations control to optimize fleet and tail assignments based on predictive factors for optimizing cost, robustness, and OTP

\- Considers multitude of factors to make OCC predictions and recommendations, including operating rules, maintenance planning, crew rosters, passenger behavior, delay predictions, and potential cost/revenue

\- Shown to rapidly improve multiple target KPIs after model is used, including fuel burn, carbon emissions, delays, and OTP

## Tomorrow

## AI-built, holistically integrated operations control

Integrated and predictive operations

People and organization enablement

Disruption recovery

Schedule robustness
simulations

Pilots + FA crew scheduling

Optimized (re)routing and schedule moves

## Signature capabilities

Facilities (e.g., gating) utilization forecasts

Customer and resource risk assessments

Integrated ground planning (internal and external)

Real-time risk visibility and prioritization

Dynamic resource dispatching

Seamless, specific customer comms

Data products

## Foundational capabilities

Data foundations

Data platforms

Real-time, integrated data products offering visibility into risk, available levers, and recommendations to operate robust schedules balancing reliability, service, and profitability through more precise buffer allocation

## OEM production in 2026 is expected to surpass 2018 peak as delays ease

Delivery outlook signals ramp-up across OEMs and fleet types
BCG FORECAST OF ANNUAL AIRCRAFT DELIVERIES AS OF OCTOBER 2025

![](images/94dfbf7e79abcc12871cd5a04227ae555356418d4453357415b75a9cad27b71a.jpg)  
Sources: Reports from Cirium, JPMorgan, Barclays, and Jefferies; FAA; Boeing and Airbus public disclosures; BCG analysis. Note: Reflects information available as of November 2025. Ye

[中间内容因长度限制已省略]

td><td>Limited human capitalMany experienced workers retired or left the industry, especially during COVID; across the industry, the share of MRO staff with &lt;3 yrs experience is double that of pre-COVID</td><td>Push for regionalizationPushing production (including final assembly) into localized areas to reduce footprints and reliance on long supply chains</td></tr><tr><td>Emerging risks</td><td>Additional trade sanctions could disrupt sourcing networks, and environmental pressures could slow extraction output</td><td>Few suppliers (e.g., largest 3 players have 75%+ share for castings) leads to high switching costsDefaults of niche suppliers create bottlenecks</td><td>Competition from retail and warehousing in addition to long training time (3–6+ months)Structural industry shortage of ~10% for skilled AMT labor</td><td>Border closures, long shipping lead times, and export license issues will increase likelihood of regionalization</td></tr><tr><td>2026 outlook</td><td>[6Yxz] Aircraft demand increasing in a tough geopolitical environment would keep lead times long</td><td>Suppliers become more confident with ramp-up, but demand continues to rise</td><td>Generally stabilizing across the industry, with improved hiring and retention</td><td>Continued intensification of regional efforts could lengthen timelines and impact ambitious delivery goals</td></tr></table>

![](images/5154470890b682c7ab5c9c9e476731182108da86f9ed99389cebbbac5316a1e6.jpg)

Situation likely to improve

![](images/63805bc874b5d6cf7fda0fafc62060902f907b0925da3caf49a25c1b77a7bce7.jpg)

Solution likely to remain the same

![](images/393812f3dccc624654481a34be85752cc99128cfe0f6125fc205dc4ae5e71c09.jpg)  
Sources: International Air Transport Association; BCG Henderson Institute; BCG analysis.  
Note: Reflects information available as of November 2025. MRO = maintenance, repair, and overhaul; AMT = aircraft maintenance technicians.

Situation likely to worsen

## New fleet types are entering service and beginning to reshape networks at scale

## A321XLR: Around 500 deliveries in the next five years will reshape transatlantic routes

Iberia “The A321XLR will allow us to reach new destinations, operating (launch customer) transoceanic routes, and doing so in a more efficient way.”
—CEO of Iberia via Airbus website

American Airlines FSCs opening routes: “...the first US carrier to take delivery of the A321XLR, with 50 on order...its 4,700-nautical-mile range opens up long and thin routes...at operating frequencies widebody aircraft have no hope of sustaining”—Simple Flying

IndiGo LCCs extending reach: “...largest customer for the A321XLR [with 69 on order], using its additional range to reach new destinations across Europe, East Asia, and Africa... plans to commence service from Mumbai to Athens in January 2026.” —Simple Flying

![](images/22fcfc1a3e2489685bc413657a31291207bb076a812a2e622eafe13a108e219e.jpg)  
Sources: Airbus; Qantas; Simple Flying; Cirium fleet forecast 2025; BCG analysis. Note: Reflects information available as of November 2025. ULR = ultra-long range.

## A350-1000 ULR: Qantas is committing to an ultra-long-haul configuration capable of flying 20+ hours

Qantas Airways “In 2017, we announced direct flights from Sydney to Europe and New York... which would revolutionize Australian air travel and code-named Project Sunrise for our long history of endurance flying. The Airbus A350-1000 was chosen... and 12 aircraft were ordered ...the first aircraft is scheduled to arrive in October 2026, which will operate flights from Sydney to London and New York.”
—via Qantas website

Qantas is the only ULR buyer to date. Delivery of 12 A350-1000 with ultra-long-haul configuration expected between 2026 and 2028

![](images/869ff987877cd5901221a39f77723448999bad5e2f9171d44dc031515a55c6d1.jpg)

![](images/65edfdeaab4868e67452d3f5f3e8dd77f7be06f8a0fbe572c7e8ec557f1e086f.jpg)

\- Plan actively for geopolitical turbulence: Regularly update, refine, and engage experts on geopolitical scenario-planning to be ready to shift capacity profitably as the operating landscape evolves (e.g., new trade announcements, changing visa requirements)

\- Capture upside in fast-growing regions: Target growth in high-momentum markets (e.g., India, Africa, ASEAN) to capture demand from the emerging middle class

\- Target RASK premium: To gain an edge in an unpredictable market, evaluate a wider range of indicators—such as loyalty data trends or flight-pattern changes due to geopolitical turbulence—to look for opportunities

\- Evaluate new fleet types: Consider new fleet types (e.g., XLR) to capture demand from long and thin $^{1}$ routes not viable for widebodies or to expand the range for low-cost carriers

\- Turn tech into a source of value and invest in AI foundations: Upgrade older systems with the buildout of AI use cases in mind to create future-ready data products, platforms, and foundations

\- Proactively plan for disruptions: Build additional flexibility into the schedule and improve two-way dialogue with airports to get ahead of potential disruptions (e.g., ATC shortage in peak months, closures from construction) weeks or months in advance

\- Manage cost fundamentals: Consider department-level or holistic cost-out programs that target key expense levers (e.g., fuel, crew, maintenance) with the governance to sustain changes long-term

\- Find margin through scale: Consider consolidation or alliances to unlock network scale, enhance negotiation power, and build financial stability through improved margins

\- Increase aircraft utilization with AI: Implement AI-driven predictive maintenance to reduce out-of-service times for aircraft, especially for older fleets
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
