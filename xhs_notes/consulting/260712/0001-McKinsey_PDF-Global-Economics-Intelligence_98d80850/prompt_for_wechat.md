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
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Global Economics Intelligence

Global Summary Report
Released July 2025 (data through June 2025)

SUBSCRIBE

## Disclaimer

This report is intended for the purpose of illustrating the broad capability of McKinsey & Company. No part of it may be circulated, quoted, or reproduced for distribution outside the client organization without McKinsey & Company's express prior written consent.

We also recommend that its content not be used for critical decision making without first consulting your McKinsey contact. McKinsey & Company shall not be responsible or liable for any decisions made by you or your company based on the use of this report.

## IMF revises global growth estimates upward but warns of ongoing trade tensions, while major economies—mainly the US and China—recorded strong growth in Q2 2025

Real GDP growth : IMF projections
Percent

![](images/23d3681851bbfcb0342200f479585415e6e30115c4bb987652c34dd0a949b29a.jpg)

IMF revises global growth estimates upward but warns of ongoing trade tensions, while major economies—mainly the US and China—recorded strong growth in Q2 2025. Central banks remain in a holding pattern on interest rates.

The International Monetary Fund has raised global growth estimates to 3.0 percent for 2025 and 3.1 percent in 2026, according to its July 2025 World Economic Outlook Update released on July 29. Representing an upward revision from the April update, the projections reflect “front-loading ahead of tariffs, lower effective tariff rates, better financial conditions (including a weaker US dollar), and fiscal expansion in some major jurisdictions.” Nevertheless, the IMF emphasizes that its latest projections are some 0.2 percentage points below its pre-April 2 forecasts, “indicating that the trade tensions are hurting the global economy.”

The IMF suggests global inflation is expected to fall, while US inflation is predicted to stay above target. It anticipates global inflation reaching 4.2% in 2025 and 3.6% in 2026. It has flagged the downside risks from potentially higher tariffs, elevated uncertainty, and persistent geopolitical tensions, urging policymakers to make “restoring confidence, predictability, and sustainability” a priority. Notably, the Washington-based institution highlighted the need to reduce trade policy uncertainty and for countries to address fiscal vulnerabilities.

Meanwhile, the tariff story continues to unfold. A day after the IMF urged a reduction in tariff uncertainty, US President Donald Trump signed an executive order imposing 50% tariffs on Brazilian imports to the United States. Previously announced on July 9, the move is widely seen as designed to apply pressure in relation to the trial of former president Jair Bolsonaro in Brazil's Supreme Court. On July 31, further tariff announcements saw US near neighbors—Mexico and Canada—each fare somewhat differently. Canadian

goods now face a 35% tariff (up from 25%) on all products not covered by the US-Mexico-Canada trade agreement, while the White House held the import tax rate for Mexican goods at 25% for 90 days as talks with Mexican President Claudia Sheinbaum continue. Moreover, in the case of Canada, goods transshipped to another country to evade the new tariffs would be subject to a transshipment levy of 40%, the White House says. Among other countries to be hit with significant tariffs are Switzerland (39%), India (25%), and Taiwan (20%). Earlier in the month, the United States announced that it had reached new trade agreements with the European Union and Japan. In both cases, the deals establish new tariffs on most exports to the US at a rate of 15%. The framework deal with Europe also includes a commitment to purchase \$750 billion in US energy over the next three years. What does this mean for the US tax take? The latest US customs duties data show that new tariffs have increased monthly import tax revenue around \$6.5 billion to \$21.5 billion. If the current trajectory continues, new tariffs might bring around \$250 billion to \$300 billion into US government coffers in 2025.

July was largely uneventful in terms of monetary policy, with only Russia cutting its policy rate, by 200 basis points to 18%, hard on the heels of a 100 basis points cut the previous month. Notably, the US Federal Reserve's Federal Open Market Committee held interest rates steady for a seventh consecutive month in a split decision on July 30, despite a strong steer from President Trump. This decision maintains interest rates within the target range of 4.25–4.5%, where they have remained since January.

Initial GDP estimates for Q2 2025 indicate the US economy grew $3\%$ (quarter on quarter, annualized), primarily driven by household consumption and an improvement in net trade due to a significant decline in imports. Meanwhile, China's second-quarter GDP growth rate was reported at $5.2\%$ year on year, almost in

## June saw broad-based consumer price increases, particularly in developed economies (1/2)

Consumer Price Inflation
Percent, 12-month change line with the pace of growth in the first quarter (5.4%). The annual target was set at 5.0% earlier this year by the government. Consumption accounted for most of the growth in GDP (52.3%), followed by investment (24.7%) and net exports (23.0%).

![](images/1ffc6dc3bec95a4865ed195ed358dcacf5e94cb5ee7293ef0d7a28f42397faaa.jpg)

Global consumer confidence has recently seen a slight increase, driven mainly by improvements in sentiment among US and UK consumers. However, US consumer confidence deteriorated in June, dropping by 5.4 points to 93.0, according to the Conference Board. In the eurozone, consumer confidence edged up by 0.6 points in July but remained well below its long-term average, highlighting continued caution among households. Nevertheless, business sentiment in the eurozone showed modest improvement in July. In Brazil, consumer confidence remained below the neutral 100 mark, with the seasonally adjusted June figure (from FGV) trending down at 85.9 (86.7 in May). At the same time, Brazil saw business confidence slide slightly in June, to 92.5 (from 94.2 in May).

Despite this, consumers—especially in some developed economies—continue to spend, while China has seen some deceleration. In the US, retail and food services sales rose by 0.6% in June to \$720.1 billion, up from \$715.5 billion in May. In contrast, eurozone retail sales weakened in May, falling 0.7% month on month but increasing 1.8% year on year. In India the strength of domestic demand was underlined by figures from the Retail Association of India showing an 8% year-on-year retail sales increase in June.

In July, financial markets expectations for short- and long-term inflation edged up to 2.5%. In the United States, median inflation expectations declined slightly to 3.0% for the one-year-ahead horizon and remained stable at 3.0% and 2.6% for the three- and five-year horizons, respectively.

On the commodities markets, precious metals have continued one of their strongest growth runs since 2011, while other asset classes moved sideways in

July, although gold prices remained largely flat. At the same time, copper prices have surged, driven by the US imposing a 50% tariff on imported copper and ongoing supply chain constraints. After a brief increase in June, overall energy markets calmed and resumed their downward trajectory. Headline agriculture prices remained stable in July; however, underlying categories experienced some volatility.

Inflation ticked up across the board, partly driven by higher import prices. However, the deflationary environment in China persists, while consumers in other emerging markets caught a break due to slowing price increases. Among the advanced economies, US headline inflation rose 2.7% year over year in June (up from 2.4% in May), while core inflation ticked up to 2.9% (annualized). Eurozone inflation has stabilized around the ECB's 2% target, but services inflation remained elevated at 3.3% in June. UK inflation edged up to 3.6% in June, compared to 3.4% in May, with broad-based increases across most consumption categories.

Among the emerging economies, India's headline consumer price inflation slowed for the eighth consecutive month, reaching $2.1\%$ in July—the lowest reading since 2019. However, core inflation, which excludes the more volatile food and energy components, has been rising steadily since mid-2024 to reach $4.5\%$ . In Brazil, inflation was slightly up, touching $5.35\%$ in June, compared with $5.32\%$ in May. Inflation remains above the central bank's upper target limit of $4.50\%$ . Russia's headline inflation fell to $9.5\%$ in June, with disinflation visible in all main categories. It is expected to continue to decline gradually towards year-end. In June, annual inflation in Mexico declined slightly to $4.3\%$ , down from $4.4\%$ in May.

Globally, both the manufacturing and services sectors expanded in June. That said, the manufacturing sector is giving off mixed signals across countries—some remain in contraction, while a few are expanding. The

# June saw broad-based consumer price increases, particularly in developed economies (1/2)

services sector appears to be much more resilient; however, most countries showed little to no change compared to May.

Taking a closer look at individual country indicators, the US showed mixed results with the industrial production index edging up to 104 in June, while the manufacturing purchasing managers' index (PMI) fell to 49.5 in July (down from 52.0 in June), signaling contraction. Eurozone industrial production gained momentum in May, rising 1.7% month on month and 3.7% year on year, while the HCOB Flash Eurozone PMI rose to 51.0 in July (June: 50.6), although the manufacturing PMI was marginally down at 50.7, a four-month low, from 50.8 in June. UK manufacturing showed mild improvement but remained in contraction territory, with industrial production also declining.

Looking at indicators for the emerging economies, data from India's PMI surveys point to further momentum in business activity. Demand-related indicators, including new export orders and domestic sales, showed strong expansion. Manufacturing output rose at its quickest pace in 14 months. Brazil's manufacturing industry has been rebounding, with the Monthly Industrial Physical Production (PIM) Index climbing strongly from 99.2 in April to 106.9 in May (versus the neutral 100 line from January 2022). This was the result of a rise in the extractive industry, which saw a $9.2\%$ rise during the period, while factory production increased $7.4\%$ . Mexico's manufacturing PMI remained in the contraction zone during June, with the S&P Global PMI falling to 46.3 from 46.7 in May. This marked a full year of deteriorating conditions, driven by sharp drops in new and international orders as clients delayed purchases. In turn, manufacturers reduced output, cut back on inputs, and lowered staffing. The picture for services varies across countries. In the United States, the services PMI improved to 55.2 from 52.9, while in the eurozone, the HCOB Flash Eurozone Services PMI Business Activity Index also gained, up from 50.5 to 51.2 and reaching a six-month high.

The UK services sector, typically a key engine of job creation, posted its strongest growth in activity for ten months in June, driven by a surge in new orders.

Among emerging economies, India's services sector recorded its fastest growth in ten months. In Brazil, the Monthly Services Survey (PMS) revenue index increased to 121.04 in May, from 118.2 in April (versus the neutral 100 line from January 2022). This was mirrored in the volume index, which rose to 107.87 (from 104.97).

Looking at labor market dynamics among the developed economies, US total nonfarm payroll employment changed little in July (+73,000)—the trend since April. Similarly, the unemployment rate, at 4.2%, also saw little change in July. However, the U.S. Bureau Of Labor Statistics has reported that revisions for May and June were larger than normal. The change in total nonfarm payroll employment for May was revised down by 125,000, from +144,000 to +19,000, and the change for June was revised down by 133,000, from +147,000 to +14,000. With these revisions, employment in May and June combined is 258,000 lower than previously reported. UK unemployment climbed to 4.7% in the three months to May 2025, up from 3.7% in the same period two years earlier. There are now 2.3 unemployed individuals for every job vacancy, more than double the 1.0 ratio seen in 2022. Among the emerging economies, China’s overall surveyed urban unemployment rate decreased slightly to 5.0% in June (5.2% in March). The youth unemployment rate was down to 14.5% in June (16.5% in March). In Brazil, the three-month moving average unemployment rate fell to 6.2% in May (from 6.6% in April), marking a two-month downward trend.

Mexico's total unemployment remained stable at $2.65\%$ in June, while formal employment declined by approximately 46,400 jobs.

July has seen equity markets reach new highs in the majority of countries, although Russia's market remains subdued. In the US, the S&P 500 posted $5.0\%$ gains in June, bringing its 12-month return to $13.6\%$ , while the Dow Jones rose $4.3\%$ and is up $3.6\%$ year to date. Volatility also eased in June, with the CBOE Volatility Index averaging 16.8 (down from 18.6 in May). The cost of capital for governments has remained stable, but at an elevated level.

Global container throughput rose $0.8\%$ in May, while global supply chain pressure eased from its highest level in 2025, as port volumes normalized. Port volumes held steady in June, while inbound spot freight rates dropped in July from their 2025 highs the previous month. However, June also saw ocean freight rates from Chicago to Shanghai undergo a significant increase, approaching their 2023 peaks.

Export growth has remained uneven, rising in the US and China, flat in emerging markets, plunging in the eurozone. Similarly, global import momentum has stayed patchy, dragged down by a sharp eurozone drop. However, the euro area's trade surplus rose significantly in May, reaching €16.2 billion (April: €9.9 billion), driven largely by a rebound in the chemicals sector (surplus up from €22.0 billion to €24.3 billion) and a moderate increase in the machinery and vehicles surplus (from €12.1 billion to €12.9 billion). Exports were stable at €243.0 billion, while imports declined by $7.3\%$ month on month to €226.5 billion. The US goods and services deficit was \$60.2 billion in June, down \$11.5 billion from \$71.7 billion in May. June exports were \$277.3 billion, \$1.3 billion less than May's exports; June imports were \$337.5 billion, \$12.8 billion less in May. The June decrease in the goods and services deficit reflected a decrease in the goods deficit of \$11.4 billion to \$85.9 billion and an

increase in the services surplus of \$0.1 billion to \$25.7 billion. Meanwhile, China's cross-border trade experienced a recovery in the second quarter, registering a year-on-year growth rate of 3.1%, compared to 0.2% in the first quarter. Exports growth remained stable at 6.0%, compared with 5.7% in the first quarter, while imports contraction eased significantly, from -7.0% in the first quarter to -0.9% in the second. India saw both exports and imports fall at similar rates in June, keeping the trade deficit broadly stable at around US \$20 billion. Brazil's June trade balance recorded a surplus of US \$5.8 billion, according to preliminary data, down from US \$7.0 billion in May. The lower surplus was driven by a reduction in exports (US \$29.1 billion in June, down from US \$29.9 billion in May), accompanied by a rise in imports (US \$23.2 billion in June, up from US \$22.9 billion in May). Mexico also recorded a trade surplus in June—of \$514 million—with exports declining to \$54.0 billion (down from \$55.5 billion in May), and imports down to \$53.5 billion (from \$54.4 billion).

[Advanced economies]: US Q2 GDP expands 3% quarter on quarter; EU and US agree trade deal, setting US tariff on EU goods at 15%; UK signs India trade agreement.

## United States

The US economy expanded by 3% in Q2 2025; however, interest rates remain high, inflation persists, and growth expectations are slowing.

First GDP estimates for Q2 2025 show the economy grew 3% (quarter on quarter, annualized), primarily driven by household consumption and an improvement in net trade due to a significant decline in imports.

The Federal Reserve held interest rates steady for a seventh consecutive month, keeping the target range at 4.25%–4.5%, where it has remained since January. Despite mounting inflation pressures and slowing GDP forecasts, Fed officials still anticipate two rate cuts later in 2025. The central bank's latest projections show inflation rising to 3.0%, GDP growth slowing to 1.4% (from 2.1%), and unemployment edging up to 4.5%.

Headline consumer price index (CPI) inflation rose 2.7% year over year in June (up from 2.4% in May), while core inflation ticked up to 2.9% (annualized). Median inflation expectations declined slightly to 3.0% for the one-year-ahead horizon and remained stable at 3.0% and 2.6% for the three- and five-year horizons, respectively.

US total nonfarm payroll employment changed little in July (+73,000)—the trend since April. Similarly, the unemployment rate, at 4.2%, also saw little change in July. However, U.S. Bureau Of Labor Statistics revisions for May and June were larger than normal. The change in total nonfarm payroll employment for May was revised down by 125,000, from +144,000 to +19,000, and the change for June was revised down by 133,000, from +147,000 to +14,000. Consumer confidence deteriorated—dropping by 5.4 points to 93.0, according to the Conference Board.

On the consumer front, retail and food services sales rose by 0.6% in June to \$720.1 billion, up from \$715.5 billion in May. Housing activity remained mixed: residential starts rose by 4.6% to 1.32 million units, completions dropped to 1.31 million, the 30-year fixed mortgage rate dipped slightly to 6.7%, and existing home sales declined by 2.7%.

Financial markets remained upbeat. The S&P 500 gained 5.0% in June, bringing its 12-month return to 13.6%, while the Dow Jones rose 4.3% and is up 3.6% year to date. Market volatility declined slightly, with the CBOE Volatility Index averaging 16.8 (down from 18.6 in May).

Industrial activity also showed mixed results: the industrial production index edged up to 104 in June, but the manufacturing PMI fell to 49.5 in July (down from 52.0 in June), signaling contraction. Conversely, t

[中间内容因长度限制已省略]

S \$23.2 billion in June, up from US \$22.9 billion in May).

On July 9, the US Government imposed 50% tariffs on imports from Brazil. According to US President Donald Trump's public statements, the move is designed to apply pressure in relation to domestic political issues in Brazil, notably former president Jair Bolsonaro's trial in the Supreme Court for allegedly attempting a coup d'état. More recently, the US administration suspended travel visas for selected Supreme Court justices and family members. More sanctions are expected, as President Lula has set a confrontational tone in his public appearances.

![](images/09e45483e9161e26616b074a6bc62d26ff176f665056a81389daa0d0929c25ae.jpg)

## Inflation's steady rise was driven by food and beverages and transportation in July

![](images/54175bb8ce5b294b14e822ab7513e4e5b88faab788b3a56b1de3adeaeadb5e36.jpg)

![](images/ae21c146a033372816e44ccefb18753c4958541088cc9983e976d1b9a6ec848f.jpg)

# Both real economy and financial markets sending ambiguous signals

Significant improvement Improving No significant change Worsening Severe decline

\- In June, the monthly average exchange rate was BRL 5.54 per US dollar versus BRL 5.66 in May. On July 23, the real closed on 5.52 per dollar.

## Markets revise CPI projections down, but maintain policy rate expectations

\- The Central Bank's Focus Bulletin—a summary of current financial market projections (published July 18)—revised CPI forecasts downwards for 2025 (to $5.10\%$ from $5.17\%$ ) and for 2026 (to $4.45\%$ from $4.50\%$ ), while maintaining previous projections for 2027 $(4\%)$ and making a slight downward revision for 2028 $(3.8\%$ from $3.81\%$ ).

\- Benchmark (SELIC) interest rate expectations remain at 15% for 2025. They were also maintained at 12.5% for 2026 and 10.5% for 2027. GDP is projected to grow 2.23% in 2025, 1.88% in 2026, and 2% in 2027 and 2028.

## Mexico

Mexico posted a trade surplus in June, while inflation declined slightly; Mexican peso appreciated against the US dollar.

In June, annual inflation in Mexico declined slightly to 4.3%, down from 4.4% in May. On the currency front, the peso appreciated against the US dollar, strengthening from MXN 19.4 = USD 1 in May to MXN 19.0 in June.

Mexico's manufacturing purchasing managers' index (PMI) remained in the contraction zone during June, with the S&P Global PMI falling to 46.3 from 46.7 in May. This marked a full year of deteriorating conditions, driven by sharp drops in new and international orders as clients delayed purchases. In turn, manufacturers reduced output, cut back on inputs, and lowered staffing.

In the labor market, total unemployment remained stable at 2.65% in June. However, formal employment declined by approximately 46,400 jobs.

Mexico recorded a trade surplus of \$514 million in June, as exports declined to \$54.0 billion (down from \$55.5 billion in May), while imports were down to \$53.5 billion (from \$54.4 billion). In June 2025, Mexico's total exports fell slightly by 0.1%, driven by a sharp drop in oil exports (-9.2%) and agricultural products (-6.5%), partially offset by a modest rise in manufacturing exports (+0.4%). Imports dropped more notably, by 0.8%, mainly due to reduced purchases of petroleum-related goods and intermediate inputs.

In July 2025, US President Donald Trump announced plans to impose 30% tariffs on all Mexican imports

starting August 1 unless Mexico steps up efforts to fight fentanyl trafficking, reduce migration at the US border, and improve cooperation on security.

President Claudia Sheinbaum and Foreign Minister Alicia Bárcena pushed back, saying these are shared responsibilities, while calling on the US to curb the flow of guns into Mexico and address its own drug demand. The Mexican government stressed the need for dialogue over confrontation to avoid a trade war.

This comes amid heightened tensions over Mexico's controversial judicial reform, which has raised alarms in Washington regarding the rule of law and investor protections. Rising cartel violence, record asylum applications, and a series of mass killings in Mexico have further fueled concerns among US policymakers.

Total Mexican exports to the US exceeded \$450 billion in 2024, and a 30% blanket tariff could severely disrupt major industries. While the proposed 30% tariffs would apply broadly, they would largely target non-USMCA-compliant products. Goods that meet USMCA rules—covering about half of Mexico’s exports—are expected to remain exempt indefinitely, offering some relief to sectors such as automotive and electronics. Separately, 25% tariffs on steel and 10% on aluminum imports from Mexico have been in effect since early 2025, ending prior exemptions and piling pressure on Mexico’s heavy industry. Still, some sectors—such as tequila—remain shielded from tariffs under USMCA rules, offering limited protection in an otherwise uncertain trade environment.

![](images/43ca03656a416ccb4f53849779c809036021180b7553179ab414ca3ea52ff892.jpg)

Source: Banco de México (Banxico); Haver Analytics; Instituto Nacional de Estadística y Geografía (INEGI); Secretaría de Economía

## Peso appreciated against US dollar; inflation declined; unemployment remained stable

![](images/8b40abb4254f4dd7341bf567d3fece736b7622e6b78d91869e7b1f7ffbc3fb9b.jpg)

\- In June and July, cartel-related violence in Mexico intensified, with a surge in attacks targeting public officials, local candidates, and civil servants. This violence has taken place against the backdrop of Mexico's June 2025 judicial elections, which saw record low turnout and widespread skepticism over whether courts can remain independent and protect political dissent.

## McKinsey & Company
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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
