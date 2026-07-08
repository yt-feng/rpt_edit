你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
JULY 2026

# A FRAGILE OUTLOOK AS ENERGY MARKET DISRUPTIONS PERSIST

## HIGHLIGHTS

The growth forecast for developing Asia and the Pacific (DAP) is lowered to 4.9% in 2026—down from the 5.1% projected in April, and 0.6 percentage points below the 5.5% growth recorded in 2025. The Middle East conflict has led to prolonged disruption to energy and supply chains, raising production costs and dampening economic activity. The growth projection is maintained at 5.1% in 2027, reflecting recovering activity as these pressures ease.

In developing East Asia, the outlook is maintained at $4.6\%$ in 2026 and $4.5\%$ in 2027 on the strength of resilient exports and continued infrastructure investment in the People's Republic of China (PRC), despite weak private consumption and rising geopolitical risks.

South Asia's growth forecasts are reduced to $6.0\%$ in 2026 and $6.7\%$ in 2027, weighed down by higher oil prices, rising freight costs, and uncertainty over remittances stemming from the conflict.

Developing Southeast Asia's growth forecast is downgraded slightly to $4.6\%$ in 2026, reflecting heightened uncertainty, weaker external demand, and rising commodity costs linked to the conflict. The 2027 projection is maintained at $4.8\%$ .

■ Growth forecasts for the Caucasus and Central and West Asia are lowered to 3.8% in 2026 and 4.2% in 2027 in response to trade disruption, rising trade costs, and prolonged geopolitical tensions.

The Pacific's growth outlook is lowered to $3.3\%$ in 2026 as higher fuel, food, and input costs stemming from the conflict dampen economic activity despite government mitigation measures. The 2027 projection is unchanged.

Inflation in DAP is projected to rise to 4.3% in 2026, from 3.0% in 2025, driven by elevated oil and gas prices and spillover to other commodities that broadens price pressures across the region. It will ease to 3.4% in 2027.

Downside risks to the outlook are significant: renewed escalation of the Middle East conflict, prolonged energy market uncertainty, tighter global financial conditions, a sharp correction in global equity markets and re-pricing of AI-related stocks, rising trade policy uncertainty, food price pressures, and a deeper property downturn in the PRC.

## Recent Developments and Outlook

The Middle East conflict evolved into a major energy shock, leaving global oil markets highly exposed to supply disruptions. At its peak in March, the crisis removed more than 10 million barrels per day of oil supply from global markets, making it one of the largest supply shocks in modern history (Box 1). Brent crude oil prices surged from about \$71/barrel before the conflict escalated on 28 February to a peak of about \$144/barrel in early April. Prices moderated to \$98/barrel in early June, reflecting alternative crude sourcing, weaker demand, and the expectation that energy flows and shipping conditions would gradually normalize. Prices eased further following the announcement of a framework agreement on 14 June, hovering below \$80/barrel, as previously trapped vessels exited the Strait of Hormuz, easing concerns about near-term supply disruptions.

The conflict could leave persistent scars on energy markets as energy disruptions unwind only gradually. Geopolitical risk premia could narrow relatively rapidly if a durable and credible ceasefire materializes. Physical disruption, however, will be stickier. Reopening the Strait of Hormuz requires mine-clearing and the full return of war-risk insurance rates. Even as the conflict winds down, transit through the Strait of Hormuz may remain below pre-conflict levels. Tankers that diverted during the closure must reposition back to Gulf routes, adding further delay before flows normalize. Production that halted across the Gulf could restart relatively quickly, but reservoir damage from wells left shut for a long time could slow supply recovery. The time required to repair damaged export and refining infrastructure could be months or several quarters. Gas supply may recover even more slowly than oil, as liquefied natural gas is harder to reroute and lacks comparable alternative supply. More broadly, global gas inventories have been drawn down sharply to compensate for lost supply, reducing buffers and leaving energy markets more exposed to further shocks.

Inflationary pressure may persist because impacts have extended beyond energy markets, and some effects of the shock will materialize only after a lag. Higher fuel costs and transport bottlenecks have raised freight and air transport rates and disrupted global supply chains (Box 2). These pressures have spilled into fertilizer and other commodity markets, raising concerns about broader inflationary effects and food security. Several of these effects feed through slowly. Higher energy and fertilizer costs take time to move through food supply chains to consumers, while pass-through from fuel prices typically unfolds over several months. Similarly, higher natural gas prices take time to reach household gas and electricity bills, depending on tariff structures, fuel contracts, and market regulation.

As the crisis evolved, the most direct impacts from rising global commodity prices were to drive up inflation across developing Asia and the Pacific (DAP). Headline inflation in the region rose from $2.9\%$ in January to $4.1\%$ in May 2026, driven by higher global energy prices and second-round effects on input and transport costs from supply chain disruption (Figure 1). Excluding the People's Republic of China (PRC), regional inflation was much higher at $7.6\%$ during the same month, reflecting persistently elevated price pressures in Türkiye and broad-based increases in more than half of the region's economies.

The shock was transmitted through producer prices and, increasingly, food and core inflation. Energy inflation surged in April and May, raising costs across energy-intensive sectors and pushing up producer prices across major economies. In the PRC, higher energy costs lifted producer price inflation to a 46-month high of 3.8% in May, while wholesale price inflation in India recorded an even steeper increase to 9.7% in May, a 43-month peak. Since March, governments across the region have introduced measures to limit pass-through to consumer prices, including fuel subsidies, tax cuts, price controls, releases from strategic petroleum reserves, and energy conservation policies. Inflationary pressures have nonetheless broadened beyond energy. Higher input and logistics costs are feeding through to food and core inflation, while higher fertilizer prices are adding to food price pressures. Food inflation rose in 15 of 19 regional economies with data from March to April 2026. Since January, food inflation has increased markedly in South Asia and developing Southeast Asia, while remaining high in the Caucasus and Central and West Asia. Core inflation has risen most in developing Southeast Asia and remains elevated in South Asia.

Growth dynamics varied substantially across the region's largest economies in the first quarter (Q1) of 2026. Growth remained resilient in Q1, buoyed by solid pre-conflict activity and strong domestic demand, even as momentum varied across economies. In the PRC, growth accelerated to $5.0\%$ in Q1, supported by robust exports and industrial production—particularly in high-tech manufacturing—alongside a strong pickup in investment. By contrast, India experienced mild deceleration to $7.8\%$ in Q1 (Q4 of fiscal year 2025) from $8.1\%$ in the second half of 2025, as higher global fuel prices squeezed real incomes. Growth in the rest of the region also slowed, notably in the Philippines and Türkiye. At the regional level, domestic demand was the main driver of growth. Consumption held up despite headwinds in major economies, as lower consumption growth in the PRC and India was partly offset by higher government spending in Indonesia, Thailand, and Türkiye. Investment strengthened across much of the region, underpinned by capital spending related to artificial intelligence (AI), but weakened in the Philippines due to low public infrastructure spending and in Türkiye due to tight credit conditions and

Figure 1 Contributions to Inflation, Developing Asia and the Pacific

Global commodity price increases are lifting inflation across developing Asia and the Pacific, as energy costs gradually spill over into food and core inflation.

Energy-related Food Core Headline, %

![](images/32d742793fefcb4f8356632504b1269c20fc7e80a503995d632a9be4fce52d37.jpg)  
B. DAP Excluding the PRC

![](images/eee80aa3aa9e6d4c3bc83d92a07f366da48fd8c35086f5fa159906a03baba88d.jpg)  
C. DAP Excluding the PRC and Türkiye  
Percentage points, year on year

![](images/b519de85294519654297189d55432f6a30b86e8eb00db02d78dbbddb32f21270.jpg)

elevated borrowing costs. Net exports contributed less than in previous quarters as rising imports of capital goods and components weighed on external balances, as did conflict-related increases in energy, shipping, aviation, and other production costs. Services edged up slightly, supported by sustained strength in wholesale and retail trade, hotel accommodation, and other services, particularly in India, Indonesia, and Thailand. Financial intermediation, real estate, and professional services also expanded, reflecting generally improving financial conditions in the PRC. Meanwhile, expansion in industry steadied as a surge in manufacturing in the PRC was offset by more subdued gains in the rest of the region. In addition, construction remained a drag on growth in the PRC and contracted in the Philippines for a third consecutive quarter (Figure 2, Panel B).

Goods exports expanded in Q1 2026, driven mainly by electronics and machinery. Across Asia and the Pacific, most economies with data through March recorded positive export growth year on year, which strengthened over the quarter. This

DAP = developing Asia and the Pacific, PRC = People's Republic of China. Notes: Component contributions are calculated based on available data. Core inflation excludes food and energy. For some economies, core inflation is estimated as the residual between headline inflation and the contributions of food and nonalcoholic beverages and energy-related items. Energy-related consumer prices include housing, water, and nonfuel transport in most economies. For the PRC, energy-related inflation is calculated using revised weight estimates from Oxford Economics and includes energy use and maintenance items. Regional averages are weighted using shares of gross domestic product at purchasing power parity for 19 economies.

Sources: Asian Development Bank estimates using data from Oxford Economics, Haver Analytics, and official sources.

largely reflected strong external demand for electronics and machinery, underpinned by the AI investment boom, particularly in economies closely integrated into global technology supply chains: Hong Kong, China; the Republic of Korea; Singapore; and Taipei, China in advanced Asia and the Pacific (AAP); and Malaysia and Thailand in DAP (Figure 3). In contrast, all other sectors' exports (excluding fuel) continued to lag overall, though recovery has gathered pace since 2025 in AAP and Malaysia. Recent tariff developments in the United States (US) could weigh on export performance in the near term, as the transition from Section 122 to Section 301 tariffs has heightened uncertainty around external demand (Box 3).

Leading indicators point to manufacturing activity improvement across most DAP economies in May, albeit uneven. Manufacturing conditions weakened in several economies in March and April, at the peak of the energy shock. Activity recovered in May, with purchasing managers' indexes (PMIs) above the 50-threshold in five of eight economies,

Percentage points, year on year

## 4 ASIAN DEVELOPMENT OUTLOOK JULY 2026

## Figure 2 Contributions to GDP Growth

A. Demand-Side  
Growth momentum remained firm in Q1 2026, largely reflecting solid pre-conflict activity and robust domestic demand.

<table><tr><td>Consumption</td><td>Statistical discrepancy</td></tr><tr><td>Investment</td><td>GDP growth, %</td></tr><tr><td>Net exports</td><td></td></tr></table>

![](images/8adb36602e66a58420ee489acf4ac3401ff851c987e9e1bf7fed0089bb99b4e8.jpg)

## B. Supply-Side

Industry and services improved modestly, as steady services growth and stable industrial expansion led by the PRC, Indonesia, and Thailand offset weaker growth in the rest of the region.

![](images/6a083ba64600e4b89b8707c663299133fdc0fc0bd7f65eadb5708999a73ab243.jpg)  
Percentage points, year on year

![](images/4ef999239cbc25f78900830dca56dbfa93606d143cdf3cbe2e910257ab98f046.jpg)  
DAP = developing Asia and the Pacific, GDP = gross domestic product, H = half, PRC = People's Republic of China, Q = quarter.  
Notes: Economies included are the PRC, India, Indonesia, Malaysia, the Philippines, Thailand, and Türkiye, which report quarterly GDP with supply- and demand-side breakdowns. They account for 89% of DAP GDP, weighted by purchasing power parity. Totals may not sum precisely because of statistical discrepancy and chain-linking in Panel A, and product taxes less subsidies in Panel B. Data are calendar year and not seasonally adjusted. For the PRC, supply-side contributions are estimated using sector shares from the 2023 Asian Development Bank Multiregional Input–Output Table.  
Sources: Asian Development Bank estimates using data from Haver Analytics, CEIC Data Company, and official sources.

Figure 3 Contributions to Nominal Export Growth, Electronics and Machinery versus All Other Sectors (excluding fuel) Growth momentum remained firm in Q1 2026, largely reflecting solid pre-conflict activity and robust domestic demand.  
![](images/f0123c030aefd9ed146f0c357898c3fe122f374e62000d3de81088cd8d5aae0f.jpg)  
PRC = People's Republic of China, Q = quarter, ROK = Republic of Korea.  
Notes: Electronics and machinery are goods under Harmonized System (HS) codes 84 (machinery and mechanical appliances) and 85 (electrical machinery and equipment); other sectors exclude HS 27 (mineral fuels). Economies are sorted according to contributions of electronics and machinery to exports growth in Q1 2026.
Source: Asian Development Bank calculations using data from International Trade Centre Trade Map.

signaling improvement (Figure 4, Panel A). PMIs in India, Thailand, and Viet Nam remained comfortably above 50, reflecting sustained expansion in output and demand. Activity continued to improve in the PRC, though it eased from the previous month. Indonesia and the Philippines recovered from contraction in April as new orders picked up, while manufacturing conditions in Malaysia and Türkiye broadly worsened. The component breakdown for May shows what drove the uneven recovery (Figure 4, Panel B). New orders and output supported expansion in most economies, with gains ranging from robust in India and Viet Nam to moderate in the Philippines. In contrast, supply chain friction weighed on manufacturing

performance across the region, albeit to varying degrees. Delivery times lengthened in all economies apart from India, where precautionary stockpiling also increased. In services, PMIs point to strengthening activity, supported by AI-driven demand in the PRC, new business expansion in India, and rising tourism in the Philippines (Figure 4, Panel C).

Navigating an increasingly challenging growth-inflation trade-off, regional central banks have adopted more guarded monetary policies. With price pressures intensifying in recent months, headline inflation ran above target in 10 of 17 inflation-targeting economies in March–May. Inflation breached

New orders index Stocks of purchases index Suppliers' delivery times Employment index Output index Headline PMI target ranges in early 2026 in Armenia, Georgia, Mongolia, Nepal, Pakistan, the Philippines, and Viet Nam, and remained above target. In response, monetary policy decisions have shifted toward rate holds and selective rate hikes, with central banks calibrating the pace of tightening to contain inflation while limiting drag on growth. In April–June, policy rates were raised in Indonesia, Pakistan, and Sri Lanka by 100 basis points; the Philippines by 50 points; and Georgia by 25 points. Some central banks used foreign exchange intervention or regulatory measures to stabilize currencies. Bucking the trend, the central bank in Kazakhstan cut rates by 100 basis points in June as annual and monthly inflation eased with lower price increases for food and services.

Figure 4 Purchasing Managers' Index, Selected DAP Economies PMI readings in May signal firmer manufacturing activity, though conditions remain uneven across economies.  
![](images/de594774d171750b6725a44ff3bb5ead0f026ce92da4620bca34a6f20243784b.jpg)  
B. Breakdown of Manufacturing PMI, by Components, May 2026  
Distance from the 50-point threshold

![](images/b474e32fe1723c8a5b57f989c52043abb54a0b60d090b0368b073d3618a57199.jpg)

![](images/4e0d9510b6f3a569cb9c0f24da4bed54ba997112d5c4c974db1a05bc67e5da5b.jpg)  
DAP = developing Asia and the Pacific, PMI = purchasing managers' index, PRC = People's Republic of China.  
Notes: The manufacturing PMI is a weighted composite index of five subindexes: new orders (30%), output (25%), employment (20%), suppliers' delivery times (15%), and inventories (10%). A reading above 50 indicates expansion, while a reading below 50 indicates contraction, but with readings reversed for suppliers' delivery times. The contribution of each component to the headline PMI is calculated as the deviation from the 50-threshold multiplied by its weight. Positive (+) values indicate improvement, and negative (−) values deterioration. For suppliers' delivery times, negative (−) values indicate faster delivery, and positive (+) values slower delivery.

Despite a more cautious policy stance, real monetary conditions have loosened across many economies this year, while policy-rate expectations have moved higher. In most regional economies, upward revisions to 2026 inflation expectations have more than offset modest nominal policy rate actions since the end of 2025, lowering ex-ante real policy rates. Indonesia stands out as the clearest case of real policy tightening, as nominal rate increases exceeded the rise in inflation expectations (Figure 5). Looking ahead, year-end policy rate expectations for 2026 and 2027 have adjusted upward in most regional economies, reflecting broadening inflationary pressures, risks of persistently higher energy prices, currency pressures, and a more hawkish monetary policy stance in advanced economies (Figure 6).


[中间内容因长度限制已省略]

y modules and 5 regional modules linked through trade flows and price transmission equations. Oil prices are used as a proxy for fertilizer price movements, given the absence of a single global fertilizer price. Oil shocks are introduced as exogenous changes and transmitted via urea fertilizer prices, affecting input use, yields, and production. The business as usual bar assumes oil prices remain at the 2025 baseline of \$69/barrel, with no fertilizer cost shock. Scenarios 1, 2, and 3 correspond respectively to crude oil price increases of 25%, 50%, and 75% above that baseline in 2026, or \$86, \$104, and \$121/barrel.

Source: Asian Development Bank estimates.

## Governments should avoid trade restrictions and

strengthen food security resilience. Diversifying fertilizer supply chains and expanding domestic production capacity where feasible would reduce exposure to energy price shocks. Regional coordination of rice stocks should be strengthened, particularly for economies with low reserves. Export restrictions should be avoided, as they amplify global price pressures and deepen food insecurity in import-dependent economies. Targeted safety nets for vulnerable households should be designed in advance and made ready for rapid rollout, as sharp food price increases disproportionately affect low-income communities across Asia and the Pacific.

Box Continued

## References

Abiad, A. et al. 2026. The Impact of the Middle East Conflict on Asia and the Pacific: An Updated Analysis. Asian Development Bank brief.

AMIS. 2026. Market Monitor No. 139. Agricultural Market Information System.

Arita, S. and J. Glauber. 2026. Will the Iran Crisis Lead to Another Round of Food Price Spikes? International Food Policy Research Institute blog. 7 April.

Bogsman, C. et al. 2026. Commodity Special Feature: Market Developments and the Economics of Rare Earths. International Monetary Fund.

FAO. 2012. FAO Statistical Yearbook 2012 Part 5: Metadata. Food and Agriculture Organization.

——. 2023. FAOSTAT. Food and Agriculture Organization.

IFPA. 2026. Why Food Prices Rise Months After Fertilizer Spikes. International Fresh Produce Association. 11 May.

Omojomolo, D. 2026. Fertiliser Price Surge to Hit Low-income EMs Most Acutely. Capital Economics.

UNCTAD. 2026. From Gas to Grain: Fertilizer Disruptions Raise Risks for Food Security and Trade. United Nations Conference on Trade and Development.

USDA. 2026. World Agricultural Supply and Demand Estimates. United States Department of Agriculture. 11 June.

US National Oceanic and Atmospheric Administration. El Niño Conditions Are Present and Expected to Strengthen into the Northern Hemisphere Winter 2026-27.

a The IRRI Global Rice Model is a structural, partial-equilibrium economic model of the global rice market, developed to represent rice production, consumption, trade, and prices and their linkages to related agricultural and non-agricultural markets. It is used for medium-term market outlook and policy analysis, including assessments of price volatility and food security.

b These scenarios are intended to illustrate the sensitivity of rice production to fertilizer-cost increases and do not correspond to the oil-price paths assumed elsewhere in this report. The baseline assumes crude oil prices remain at the 2025 level of \$69/barrel.

This box was written by Shyam Basnet, Alisher Mizabaev, Valerien O. Pede, Takashi Yamano, Pilipinas Quising, and Melanie Grace Quintos.

## Asian Development Outlook July 2026

Asian Development Outlook is the main economic forecasting product from ADB. It is published each April with an update published in September and brief reports published in July and December.

## Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.

![](images/690da9beccae4a1c6b4a0ea89f5d9e457b4c3ad60729e790271cbf9d5d8497a9.jpg)

Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)

© 2026 Asian Development Bank
6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines
Tel +63 2 8632 4444; Fax +63 2 8636 2444
www.adb.org
Some rights reserved. Published in 2026.

ISBN 978-92-9277-854-5 (print); 978-92-9277-855-2 (PDF)
Publication Stock No. FLS260274-3
DOI: http://dx.doi.org/10.22617/FLS260274-3

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent. By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. Please contact pubsmarketing@adb.org if you have questions or comments with respect to content or permission to use. Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.
"""
