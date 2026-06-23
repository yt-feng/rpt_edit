你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`DB`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Industry Industrial Logic

Europe Capital Goods Electrical Equipment

![](images/90e1557362db7f0e5f08479c97d1e03097de13cf34f3bd75cc3db3474aeaecad.jpg)

# Cyclicals: Back on the Menu?

Chart of the week: Sensitivity to IP vs price performance since Iran war
With the US and Iran signing an MoU last week, the Hormuz blockade lifted and the ceasefire extended by 60 days, the companies hit hardest by the war may now have the most to gain. Europe bore much of the pain given its sensitivity to energy prices, but as inflationary pressure fades and corporate investment sentiment recovers, capital goods names most exposed to industrial production should be well placed for a rebound. This week's chart plots the correlation between organic sales growth and German industrial production across our coverage, against share price performance since the start of the Iran war. Those with the highest short-cycle exposure, including KION, Knorr-Bremse and SKF, still trade below pre-war levels. As the market moves through the post-war aftershocks, a number of upcoming catalysts could support the recovery in the shares.

Figure 1: Cap goods sales growth correlation to German IP vs price performance since Iran war  
![](images/e5bae1f2fdb235dd70907e7903991c7d9bccd492a28f068454c8073090cc848e.jpg)  
Source : Company data, DB estimates, Bloomberg; Note: Price change since 27-Feb-2026

Periodical

Date
22 June 2026

John Kim

Research Analyst +44-20-754-18699

Nabil Najeeb
Research Analyst
+44-20-754-17410

Lars Vom-Cleff
Research Analyst
+49-69-910-13526

Seetharaman Ramakrishna
Research Associate

## DB AG

1/ Knorr-Bremse will provide a strategic update alongside Q2 results on 30 July, including new mid-term targets. We expect a 16%+ margin target for 2029 or 2030, around 2pts above its 2026 guidance. 2/ KION, meanwhile, continues to trade near historically low multiples, with the market giving little credit for its more resilient business mix versus prior cycles. A potential mid-single-digit cut to FY26 EBIT guidance should be a clearing event, while a better post-war growth outlook creates an attractive risk/reward skew. 3/ For SKF, the planned spin-off of the Automotive division remains on track for the autumn and should help drive a re-rating.

## Last week

Schneider announced a strategic collaboration with Foxconn to deliver integrated, ready-to-deploy solutions that enable customers to build AI data centers more rapidly and with greater efficiency. This collaboration brings together Foxconn's expertise in advanced compute platforms, AI rack integration, and global manufacturing with Schneider's expertise in power and cooling. Production will begin later this year.

Wärtsilä announced a 50/50 JV with RCT Solutions for its Energy Storage business with new investors possibly joining at a later stage. The company had struggled with profitability in Storage (6% target margins vs. core group margin of 14%), with the JV creating more vertical integration as RCT has been a key supplier to Wärtsilä for several years. The press release indicates that the JV will be loss-making in 2026, with -€40m to -€50m in expected EBIT contribution to Wärtsilä, including a negative impact from transformative actions such as the write-down of R&D. The deal is expected to close in Q3 2026, with the JV to be reported as a share of results in associated companies going forward.

According to Manager Magazin, Siemens Energy is looking into a potential separation of its Tol division through an IPO, the spin-off of a majority stake, or a merger with a competitor. If completed, the separation would allow Siemens Energy to fully refocus on electrification markets, eliminate its Oil&Gas/petrochemical exposure, and mechanically improve its margin profile by at least +50bps.

Fujikura raised its FY26 operating profit guide by 47%, and its H1 profit guide by 89% after just one quarter into the fiscal year. The upgrade came only a month after Fujikura provided a conservative FY26 guide, which lead to a sell-off in its shares. Fujikura has secured new orders for optical components, raised its prices and sees an easing of the impact from hydrogen shortages. While the update from Fujikura is supportive for sentiment in the space, the read-across for Prysmian is limited, in our view. Fujikura does not have meaningful domestic bare fiber capacity in the US (making it exposed to tariffs), while the previous FY26 guide took into account hydrogen shortages on the back of the war (while in Prysmian's case, the company was not affected by the Hormuz blockade for inputs such as hydrogen).

On Friday, Nexans' shares were up nearly 3%. We attribute the strength to its Electra event on Thursday. The Q&A with management was positive with CEO indicating that they would know the result of an MI project tender to replace GSI in the short term, by early Q3. Outside of transmission, management sounded very positive on the demand outlook within data centers, both in Europe (where large project momentum is accelerating) and in the US, with Republic Wire providing a springboard for its MV cable offering.

On the macro side, US Empire manufacturing index for June declined to +5.7 (vs. cons: +13.7) from +19.6 in May, Industrial production for May increased +0.1% MoM (vs. cons: +0.3%, April: +0.7%), Housing starts declined to 1.177m (cons: 1.43m) from 1.465m in April, and provisional building permits for May stayed almost flat MoM at 1.413m (vs. cons: 1.418m, Apr: 1.423m). Germany's ZEW survey expectations index for June improved to +10.5 (vs. cons: -5.5) from -10.2 in May and PPI increased to +2.2% YoY in May (vs. cons: +2.5%) from +1.7% in April. China's industrial production for May increased +4.5% YoY (vs. cons: +4.4%, April: +4.1%).

## This week

On the macro front, key releases this week include the provisional Eurozone, Germany, France - Manufacturing PMI for June, France's Manufacturing Confidence Index for June, and US - Richmond Fed manufacturing Index for June on Tuesday, US Building Permits MoM (May F) on Wednesday, followed by provisional US Wholesale inventories for May and Italy's Manufacturing Confidence Index for June on Friday. A full schedule is shown below.

Figure 2: Calendar of upcoming events this week

<table><tr><td></td><td>Event</td></tr><tr><td>23-Jun</td><td>Eurozone, Germany, France - Manufacturing PMI (June prov); France - Manufacturing Confidence Index (June); US - Richmond Fed manufacturing Index (June)</td></tr><tr><td>24-Jun</td><td>US - Building Permits MoM (May F)</td></tr><tr><td>26-Jun</td><td>US - Wholesale inventories MoM (May Prov); Italy - Manufacturing Confidence Index (June)</td></tr></table>

Source : DB, Bloomberg Finance LP

Sector weekly performance and valuation: The sector ended the week up +6.0%, and up +3.5% vs. the STOXX Europe 600. As of Thursday, the sector traded on a median 2026E P/E of 22.2x and EV/EBITA of 16.0x. For detailed valuation and risk sections, please see referenced reports.

## Table Of Contents

Reports you might have missed....5   
We read in the news....9   
European EV/EBITA Multiples....12   
European Share Price Performance....14   
US Share Price Performance....15   
Asia Share Price Performance....16   
Valuation table....17

## Reports you might have missed

Siemens Energy: TI in the spotlight: According to Manager Magazin (June 18), Siemens Energy is exploring the separation of its "Transformation of Industry" division (TI, €5.7bn revenue, 14% of group) through an IPO, the spin-off of a majority stake, or a merger with a competitor. If completed, we believe the move would benefit shareholders; it would allow Siemens Energy to fully refocus on electrification markets, eliminate its Oil&Gas/petrochemical exposure, and mechanically improve its margin profile (we estimate by at least +50bps). It would also simplify the group's reporting structure and make its profile even more comparable to that of GEV, potentially further reducing the gap between the two companies' valuation multiples. We rate the stock Buy. See full report here.

Kion: Six arguments for asymmetric upside: While the stock came under pressure due to valid concerns (unpredictable macro, rising interest rates, inflationary pressures, at-risk guidance), the extent of its decline (-40% YTD) appears excessively severe. KION is now trading nearing historically low multiples, both on an absolute and relative basis. With the risk of appearing naïve, we continue to believe that valuation matters. The current stock price already seems to reflect a worst-case scenario, suggesting the market may be underestimating the group's enhanced resilience characteristics including a more dynamic pricing strategy, escalation clauses in place and a lower breakeven point. Although a MSD downward revision to the FY26 EBIT guidance is possible, the buyside has already factored this in, and it should be viewed as a clearing event. The risk/reward profile is very asymmetric, as we see 20% downside risk and 100% upside potential. See full report here.

Assa Abloy: Q2'26 results due July 17 - volume growth remains subdued: Assa Abloy will release its Q2 results on July 17. After a subdued Q1 performance primarily due to adverse weather conditions and significant negative FX effects, we anticipate Q2 will better align with the group's usual standards, although still slightly below consensus estimates. So far this year, the M&A contribution has been relatively limited and volume growth has been modest compared to the sector average. Higher rates and weaker consumer confidence are further delaying the recovery of the residential market. We retain a Hold rating. See full report here.

Nexans: Feedback from the Electra event: We attended Nexans' inauguration of its third cable-laying vessel, Electra, in Oslo yesterday, which was followed by a Q&A with management. Electra is a best-in-class cable laying vessel with lower emissions that should help Nexans win more tenders and improve margins as it relies less on 3rd parties. Nexans should also know the result of an MI project tender to replace GSI in the short term, by early Q3. Outside of transmission, management sounded very positive on the demand outlook within data centers, both in Europe (where large project momentum is accelerating) and in the US, with Republic Wire providing a springboard for its MV cable offering. The valuation remains compelling with the shares trading at a deep c.40% discount to Prysmian, with a growing exposure to data centers and the US market. See full report here.

Sandvik: Q2 faces tougher order comps but trend growth remains intact: Sandvik reports Q2 results on July 17. The company is enjoying positive market dynamics in both mining and industrial exposures but growth comps get tougher from here in Mining. That said, we think the company will deliver Q2 results in line with DB estimates to slightly ahead of consensus for Q2 and the year. We see better positive operational leverage in the quarter, with c.300bps margin expansion yr/yr in group

EBITA and with forex less of a headwind (-80bps vs -240bps yr/yr in Q1). On the SMM side, tungsten pricing has come off its relative peak but continues to underpin positive price cost on cutting tools where we continue to see real growth. We remain BUY rated on the share with a new target price of 445 SEK. See full report here.

Epiroc: Fundamentals intact but limited ability to beat in the quarter: Epiroc is set to report Q2 results on July 17th. The quarter looks good with soft order comps in E&S, unchanged positive fundamentals with execution and margin delivery the watch items this year as the market looks for evidence that positive industry dynamics will translate to margin improvement more in-line with historic levels. DB estimates are in-line to slightly ahead for Q2 and full-year numbers for 2026. With no announced large orders in the quarter to date, visibility is lower on equipment orders and we trim our estimate here. With its recent capital markets day (link here), we expect little to no change in messaging on the company's outlook statement 'mining demand remains strong with construction expected to increase somewhat from a low level.' We maintain our HOLD rating but adjust our target price to 267 SEK. See full report here.

SKF: Q2 looks benign with separation on track, new target price 280 SEK: SKF reports Q2 2026 results on July 17th. DB estimates are in line with consensus at the group level on Q2 numbers with the expected spin of Automotive the larger driver for the share. Normal cyclicality has been distorted in 2025 and 2026 due to the start-stop nature of tariff changes, as well as various bouts of pre-buy activity. We continue to forecast modest volume recovery in late 2026 with recent cost inflation more of a headwind in H2. We remain positive on SKF as a share due to the expected re-rating post-spinoff of SKF Automotive and adjust our target price to 280 SEK as we maintain our BUY rating. See full report here.

GEA: A compelling mismatch / Upgrade to Buy: We upgrade GEA to Buy and raise our target price to EUR 70 (from EUR 64) as we now see a more compelling mismatch between the group's resilient fundamentals and the current valuation. We have become more confident in the outlook for improving revenue momentum, sustained margin expansion and continued execution against MISSION 30, supported by a favorable mix shift towards higher-margin service and digital revenues, additional cost savings and disciplined capital allocation. Against this background, we have increased our FY26E-FY28E EPS forecast by 4-6%. At the same time, GEA's defensive end-market exposure, low customer concentration and healthy order/backlog dynamics continue to underpin earnings resilience. Yet the shares trade at 10.3x EV/EBITDA, c.15% below their 10-year median and without the historical premium to peers, which in our view leaves the stock offering an attractive risk-reward profile from current levels. GEA management has already invested EUR 1.6m ytd in GEA shares via 13 disclosed purchases by all six board members, which we also view as a strong signal of confidence. Nevertheless, following the drop to a 52-week low at the beginning of this month, the stock has underperformed the MDAX and STOXX 600 Industrial Goods & Services ytd, leaving \~25% potential upside to our new price target. See full report here.

US and Asia Capital Goods
Humanoid Robot: Comparing Unitree, UBTECH, DEEP, Dobot and Leju: Opportunities and risks coexist
Iris Zheng, 15 June 2026

DeBLASEing the Trail: HVAC Update: It's Getting Hot In Here
Nicole DeBlase, 14 June 2026

## Macro

US Economic Perspectives: Yield to Warsh: 50bps of hikes in 2026
Matthew Luzzetti, 19 June 2026

UK Weekly Digest: The Consequences of Peace – What a MoU means for the UK
Sanjay Raja, 19 June 2026

Euro Weekly Digest: Memorandum is welcomed, but price pressures are already in the pipeline
Michael Kirker, 19 June 2026

Fed Notes: Who's who in the June 2026 dot plot
Matthew Luzzetti, 18 June 2026

UK economic notes: BoE Recap: A steady hand
Sanjay Raja, 18 June 2026

Focus Europe: Europe and 'China Shock 2.0': Competitiveness Under Pressure
Clemente Delucia, 18 June 2026

Thematic Research: AI's tightest bottleneck: Memory chips
Marion Laboure, 18 June 2026

Focus Europe: Inflation Chartbook: Energy shock might be peaking, but inflation persistence risks have not disappeared
Maria Contreras, 17 June 2026

Fed Notes: June FOMC recap: Rock Chalk, Warsh-hawk
Matthew Luzzetti, 17 June 2026

UK Macro Handbook: Inflation Chartbook – More Discounts, More Time
Sanjay Raja, 17 June 2026

Europe Blog: What to expect for China trade defence, competitiveness & the next EU budget
Marion Muehlberger, 17 June 2026

Hsueh On Oil: New data points
Michael Hsueh, 16 June 2026

Thematic Research: AI twist in the tale for Anthropic's Fable and Mythos
Adrian Cox, 16 June 2026

Thematic Research: Is the Ceasefire a reset: Iran, the US and the Middle East they can't restore
Helen Belopolsky, 16 June 2026

China Macro: May activity: deepening K-shaped divide
Yi Xiong, 16 June 2026

Europe Blog: Core goods inflation, is it back?
Maria Contreras, 15 June 2026

US Economic Chartbook: Who is buying Treasuries, mortgages, credit and munis? (June 2026)
Steven Zeng, 15 June 2026

China Macro: RMB Internationalization Blog (4): How China Becomes an Exporter of Capital
Yi Xiong, 15 June 2026

## We read in the news

System solutions for Europe's new train platform: Knorr-Bremse wins contract from Siemens Mobility: Rail travel across Europe is becoming more important, attractive, and popular. Siemens Mobility has created Vectouro, a new passenger train platform for flexible international use in Europe. Knorr-Bremse is supplying key technologies – including braking and entrance systems – to enhance the performance, availability, and efficiency of the trains. Equipment contract with an order volume for Knorr-Bremse in the mid double-digit million-euro range. (Source: Knorr-Bremse, 18 June 2026)

Alstom-led consortium signed €690 million to modernise Egypt's strategic rail corridors: Alstom, leading a consortium with Rowad Modern Engineering and Concrete Plus, has signed four landmark contracts with Egyptian National Railways (ENR) to modernise Egypt's strategic railway corridors, covering the 6th of October–Alexandria corridor and Belbes–10th of Ramadan (B10) line. The combined value of the contracts is approximately €690 million, with Alstom's share representing around €300 million. As four of Egypt's most significant rail modernisation projects, the contracts support Egypt Vision 2030 by strengthening national logistics and improving connectivity between new dry ports, industrial zones, and major seaports. The 6th of October–Alexandria corridor, valued at €550 million, of which Alstom's share amounts to approximately €240 million, will be delivered across three major implementation lots. It will modernise the corridor with next-generation digital railway systems, upgraded telecommunications, reinforced power supply, and comprehensive civil and track rehabilitation. These enhancements will improve safety, increase capacity, enhance operational reliability, and reduce full route travel time by nearly 80 minutes. The Belbes–10th of Ramadan (B10) project, valued at approximately €140 million, of which Alstom's share amounts to approximately €60 million, will introduce the same advanced railway technologies and modernisation scope. It will enhance connectivity to one of Egypt's largest industrial hubs, strengthening freight efficiency and supporting industrial growth across 

[中间内容因长度限制已省略]

out prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
