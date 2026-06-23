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
## One-stop Outlook 2026 Mid-Year Check-In

June 2026

Andrew Casella | Ryan Dowling | Miles Highsmith | Aaron Watts | Sean-M Wondrack
Brett Ryan | Steve Caprio | Karthik Nagalingam

\- US HY Research - Organizational Structure and Contact Info 3
- Introduction | 2026 Mid-Year Check-in 4
- Single-Name Top Picks - Summary 5
- Single-Name Top Picks – Potential Total Return Categorization by Ticker 6
- Topical Datasite Names – Aggregate Table 7
- US Economics 8
- Growth: Oil drag versus fiscal and FCI boost 9
- Labor market: Growing confidence in stabilization 10
- Inflation: Another year well above target 11
- Risks to our outlook... 12
- DB US Forecast Summary 13
- Strategy Outlook 14
- Nimble? More dispersion is coming 15
- Technicals remain strong, which can moderate \$HY spread widening 16
- US recession probability remains low, even as pockets of weakness will lead to dispersion 17
- A US Software glitch can materially tighten funding markets 18
- \$HY Ratings: Mind \$B3 downgrade risks 20
- Which sectors are more exposed to defaults and fundamental risks? 21
- Consumer and Retail 23
- Key Themes in Consumer 24
- Crocs Inc. (CROX) – Apparel 25
- Dave & Buster's (PLAY) – Restaurants 26

■ Healthcare
• Still Many Moving Parts
• Community Health Systems, Inc. (CYH) – Healthcare
■ Industrials
• U.S. Building Products | Residential and Non-residential – 2026 Outlook
• Bristow (VTOL) – Aerospace & Defense
• Park River Holdings Inc. (a/k/a Primesource) (PRIMBP) – Building Products
• Iris Holding, Inc. (a/k/a Intertape Polymer Group) (ITPCN) - Packaging
• Whirlpool Corporation (WHR) – Building Products
• Media / Business Services
• HY Media Mid-Year 2026 Outlook
• Gray Television (GTN) – TV Broadcaster
• iHeart Media (IHRT) – Radio Broadcasting
• Rental Services, Auto Suppliers and Metals & Mining
• Equipment Rental Services – 2026 Mid-year Outlook
• Herc Rentals (HRI) – Rental Services
• EquipmentShare (EQPT, EQMSRM) – Rental Services
• Auto Suppliers – 2026 Mid-year Outlook
• Rivian Automotive (RIVN, RIVHOL) – Automotive Suppliers
• Datasite Issuers
• Cox Media (CMGMCO) – TV Broadcasting – Datasite
• Global Auto Holdings (GLOBAU) (B3,B+) – Automotive Suppliers - Datasite
• Lifepoint Health, Inc. (RGCARE) – Healthcare - Datasite
• R1 RCM, Inc. (RCM) – Healthcare – Debt domain
• Shearer’s Foods (SHEARE) – Food & Beverage - Debtdomain
• U.S. Acute Care Solutions, Inc. (USACUT) – Healthcare - Intralinks

Andrew Casella, CFA
Head of US HY Research
(212) 250-0777
Industrials
Building Products, Packaging,
Chemicals,
General Industrials

Aaron Watts
Managing Director
(212) 250-2592
Media, Cable,
Satellites, Business
Services

Miles Highsmith
Managing Director
(212) 250-1606
Healthcare

Sean Wondrack
Director
(212) 250-8980
Metals, Mining,
Rentals, Auto
Suppliers

Marisa Moss
Director
(212) 250-8113
Energy & Utilities

Harsha Mohan
Associate
(212) 250-2599
Media, Cable,
Satellites, Business
Services

Anna Yang
Vice President
(212) 250-9980
Gaming, Lodging,
Leisure

Ryan Dowling
Vice President
(212) 250-4549
Food/Bev, Consumer,
Retail, Restaurants

Angeline Mathew
Vice President
(212) 250-3328
FIG & Technology

Amelia Srebnik
Analyst
(212) 250-0775
Building Products,
Packaging, Chemicals,
General Industrials

We have structured our 2026 Mid-Year Check-in as follows:

\- Updating 2026's macroeconomic framework: We have included updated summaries of the respective 2026 outlooks from DB's US Economics and US HY Credit Strategy teams. These are meant to refresh from our 2026 outlook (released in December 2025).

\- High-conviction single-name credit ideas and brief sector overviews: Each of the HY sector analysts have provided a high-level sector outlook, followed by their highest-conviction and published, single-name ideas. These have been put into three one-year potential total return baskets: 5-9.99%, 10-14.99% and >15%.

\- Topical VDR names: We have included a section to highlight what the HY analyst team has considered to be the most topical datasite-based (i.e. private) corporate issuers amongst our clients. As a reminder, these are not formally covered securities due to financial data confidentiality obligations with the respective issuers.

■ General housekeeping: All pricing is as of 6/16/26, unless noted otherwise, and all term loans have been priced with the swapped curve.

The US HY Research team has extensive knowledge across both public and private (datasite) names, across both HY bonds and broadly-syndicated loan. As always, the team is ready and available to assist clients navigate what has already been an eventful 2026.

Andrew Casella
Head of US HY Research

<table><tr><td>Analyst</td><td>DB Rec</td><td>BBG Ticker</td><td>Ranking/ Seniority</td><td>Coupon</td><td>Amt O/S</td><td>Maturity</td><td>Price</td><td>YTW/YTM</td><td>DM / OAS</td><td>Mdy&#x27;s/ S&amp;P</td></tr><tr><td>Aaron Watts</td><td>HOLD</td><td>*GTN</td><td>1L</td><td>S+300</td><td>$739</td><td>12/1/2028</td><td>100.250</td><td>6.92%</td><td>292</td><td>Ba3 / B+</td></tr><tr><td>Aaron Watts</td><td>HOLD</td><td>*GTN</td><td>1L</td><td>10.500%</td><td>$1,125</td><td>7/15/2029</td><td>105.625</td><td>5.09%</td><td>139</td><td>Ba3 / B+</td></tr><tr><td>Aaron Watts</td><td>NR</td><td>*GTN</td><td>1L</td><td>7.250%</td><td>$775</td><td>8/15/2033</td><td>97.500</td><td>7.71%</td><td>337</td><td>Ba3 / B+</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*GTN</td><td>2L</td><td>9.625%</td><td>$900</td><td>7/15/2032</td><td>95.250</td><td>10.69%</td><td>643</td><td>B3 / CCC</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*GTN</td><td>Sr Unsec&#x27;d</td><td>4.750%</td><td>$790</td><td>10/15/2030</td><td>71.750</td><td>13.61%</td><td>944</td><td>Caa1 / CCC</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*GTN</td><td>Sr Unsec&#x27;d</td><td>5.375%</td><td>$1,220</td><td>11/15/2031</td><td>69.625</td><td>13.46%</td><td>923</td><td>Caa1 / CCC</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*IHRT</td><td>1L</td><td>S +577.5</td><td>$2,119</td><td>5/1/2029</td><td>95.750</td><td>11.47%</td><td>753</td><td>Caa1/CCC+</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*IHRT</td><td>1L</td><td>4.750%</td><td>$277</td><td>1/15/2028</td><td>96.250</td><td>7.42%</td><td>343</td><td>Caa1/CCC+</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*IHRT</td><td>1L</td><td>9.125%</td><td>$718</td><td>5/1/2029</td><td>97.750</td><td>10.09%</td><td>596</td><td>Caa1/CCC+</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*IHRT</td><td>1L</td><td>7.750%</td><td>$661</td><td>8/15/2030</td><td>93.500</td><td>9.72%</td><td>555</td><td>Caa1/CCC+</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*IHRT</td><td>1L</td><td>7.000%</td><td>$178</td><td>1/15/2031</td><td>89.375</td><td>10.04%</td><td>584</td><td>Caa1/CCC+</td></tr><tr><td>Aaron Watts</td><td>BUY</td><td>*IHRT</td><td>2L</td><td>10.875%</td><td>$675</td><td>5/1/2030</td><td>86.500</td><td>15.70%</td><td>1,153</td><td>Caa3/CCC-</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>VTOL</td><td>1L</td><td>6.750%</td><td>$500</td><td>2/1/2033</td><td>101.125</td><td>6.47%</td><td>199</td><td>Ba3/BB</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>PRIMBP</td><td>1L</td><td>S+450</td><td>$1,020</td><td>3/17/2031</td><td>99.875</td><td>8.34%</td><td>453</td><td>B3/B-</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>PRIMBP</td><td>1L</td><td>8.000%</td><td>$800</td><td>3/15/2031</td><td>101.250</td><td>7.39%</td><td>305</td><td>B3/B-</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>PRIMBP</td><td>2L</td><td>8.750%</td><td>$538</td><td>12/31/2030</td><td>98.125</td><td>9.25%</td><td>492</td><td>Caa2/CCC</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>ITPCN</td><td>1L</td><td>S+475</td><td>$1,448</td><td>6/28/2028</td><td>95.625</td><td>11.21%</td><td>718</td><td>B3/B-</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>ITPCN</td><td>Sr Unsec&#x27;d</td><td>10.000%</td><td>$400</td><td>12/15/2028</td><td>88.250</td><td>15.89%</td><td>1,179</td><td>Caa3/CCC</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>WHR</td><td>2L</td><td>7.500%</td><td>$1,000</td><td>7/1/2031</td><td>101.625</td><td>7.02%</td><td>288</td><td>Ba1/BB+</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>WHR</td><td>2L</td><td>7.875%</td><td>$1,000</td><td>7/1/2034</td><td>101.125</td><td>7.60%</td><td>342</td><td>Ba1/BB+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>4.750%</td><td>$700</td><td>2/26/2029</td><td>94.375</td><td>7.08%</td><td>299</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>6.125%</td><td>$600</td><td>6/15/2030</td><td>93.625</td><td>8.00%</td><td>386</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>2.400%</td><td>$300</td><td>5/15/2031</td><td>75.125</td><td>8.75%</td><td>458</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>4.700%</td><td>$300</td><td>5/14/2032</td><td>79.625</td><td>9.24%</td><td>500</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>5.500%</td><td>$300</td><td>3/1/2033</td><td>80.250</td><td>9.56%</td><td>527</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>6.500%</td><td>$600</td><td>6/15/2033</td><td>88.500</td><td>8.73%</td><td>443</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>5.750%</td><td>$300</td><td>3/1/2034</td><td>79.250</td><td>9.62%</td><td>528</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>5.150%</td><td>$250</td><td>3/1/2043</td><td>63.875</td><td>9.50%</td><td>471</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>4.500%</td><td>$500</td><td>6/1/2046</td><td>60.250</td><td>8.74%</td><td>378</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>SELL</td><td>WHR</td><td>Sr Unsec&#x27;d</td><td>4.600%</td><td>$500</td><td>5/15/2050</td><td>59.750</td><td>8.59%</td><td>364</td><td>B2/B+</td></tr><tr><td>Andrew Casella</td><td>BUY</td><td>WHRCORP SR 5Y</td><td></td><td>Spread:</td><td>441</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Analyst</td><td>DB Rec</td><td>BBG Ticker</td><td>Ranking/ Seniority</td><td>Coupon</td><td>Amt O/S</td><td>Maturity</td><td>Price</td><td>YTW/YTM</td><td>DM / OAS</td><td>Mdy&#x27;s/ S&amp;P</td></tr><tr><td>Miles Highsmith</td><td>BUY</td><td>CYH</td><td>1L</td><td>6.000%</td><td>$644</td><td>1/15/2029</td><td>99.375</td><td>6.29%</td><td>199</td><td>Caa1 / B-</td></tr><tr><td>Miles Highsmith</td><td>BUY</td><td>CYH</td><td>1L</td><td>5.250%</td><td>$1,535</td><td>5/15/2030</td><td>94.250</td><td>6.94%</td><td>280</td><td>Caa1 / B-</td></tr><tr><td>Miles Highsmith</td><td>BUY</td><td>CYH</td><td>1L</td><td>4.750%</td><td>$689</td><td>2/15/2031</td><td>91.750</td><td>6.83%</td><td>267</td><td>Caa1 / B-</td></tr><tr><td>Miles Highsmith</td><td>BUY</td><td>CYH</td><td>1L</td><td>10.875%</td><td>$1,549</td><td>1/15/2032</td><td>107.750</td><td>6.86%</td><td>278</td><td>Caa1 / B-</td></tr><tr><td>Miles Highsmith</td><td>BUY</td><td>CYH</td><td>1L</td><td>10.750%</td><td>$700</td><td>6/15/2033</td><td>107.250</td><td>9.16%</td><td>487</td><td>Caa1 / B-</td></tr><tr><td>Miles Highsmith</td><td>BUY</td><td>CYH</td><td>1L</td><td>9.750%</td><td>$1,790</td><td>1/15/2034</td><td>104.625</td><td>8.42%</td><td>399</td><td>Caa1 / B-</td></tr><tr><td>Miles Highsmith</td><td>HOLD</td><td>CYH</td><td>2L</td><td>6.875%</td><td>$1,244</td><td>4/15/2029</td><td>98.750</td><td>7.37%</td><td>315</td><td>Caa3 / CCC-</td></tr><tr><td>Miles Highsmith</td><td>HOLD</td><td>CYH</td><td>2L</td><td>6.125%</td><td>$1,227</td><td>4/1/2030</td><td>90.250</td><td>9.22%</td><td>510</td><td>Caa3 / CCC-</td></tr><tr><td>Miles Highsmith</td><td>HOLD</td><td>CYH</td><td>Sr. Unsec&#x27;d</td><td>6.875%</td><td>$42</td><td>4/1/2028</td><td>97.000</td><td>8.71%</td><td>468</td><td>Ca / CCC-</td></tr><tr><td>Ryan Dowling</td><td>BUY</td><td>PLAY</td><td>1L</td><td>S + 325</td><td>$691</td><td>6/29/2029</td><td>85.625</td><td>12.66%</td><td>901</td><td>B3/B-</td></tr><tr><td>Ryan Dowling</td><td>BUY</td><td>PLAY</td><td>1L</td><td>S + 325</td><td>$690</td><td>10/31/2031</td><td>79.375</td><td>12.33%</td><td>868</td><td>B3/B-</td></tr><tr><td>Ryan Dowling</td><td>BUY</td><td>CROX</td><td>1L</td><td>S + 225</td><td>$500</td><td>2/20/2029</td><td>100.625</td><td>5.66%</td><td>199</td><td>Ba1/BBB-</td></tr><tr><td>Ryan Dowling</td><td>BUY</td><td>CROX</td><td>Sr. Unsec&#x27;d</td><td>4.250%</td><td>$350</td><td>3/15/2029</td><td>97.500</td><td>5.24%</td><td>113</td><td>Ba3/BB</td></tr><tr><td>Ryan Dowling</td><td>BUY</td><td>CROX</td><td>Sr. Unsec&#x27;d</td><td>4.125%</td><td>$350</td><td>8/15/2031</td><td>94.000</td><td>5.46%</td><td>127</td><td>Ba3/BB</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>HRI</td><td>1L</td><td>S+175</td><td>$748</td><td>6/2/2032</td><td>100.125</td><td>3.12%</td><td>172</td><td>Baa3 / BBB-</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>HRI</td><td>Sr. Unsec&#x27;d</td><td>6.625%</td><td>$800</td><td>6/15/2029</td><td>102.500</td><td>5.28%</td><td>109</td><td>Ba3 / BB-</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>HRI</td><td>Sr. Unsec&#x27;d</td><td>7.000%</td><td>$1,650</td><td>6/15/2030</td><td>103.875</td><td>5.59%</td><td>125</td><td>Ba3 / BB-</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>HRI</td><td>Sr. Unsec&#x27;d</td><td>5.750%</td><td>$600</td><td>3/15/2031</td><td>100.125</td><td>5.72%</td><td>139</td><td>Ba3 / BB-</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>HRI</td><td>Sr. Unsec&#x27;d</td><td>7.250%</td><td>$1,100</td><td>6/15/2033</td><td>104.625</td><td>5.94%</td><td>141</td><td>Ba3 / BB-</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>HRI</td><td>Sr. Unsec&#x27;d</td><td>6.000%</td><td>$600</td><td>3/15/2034</td><td>99.375</td><td>6.10%</td><td>149</td><td>Ba3 / BB-</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>EQMSRM</td><td>2L</td><td>9.000%</td><td>$1,040</td><td>5/15/2028</td><td>103.375</td><td>5.19%</td><td>136</td><td>B3 / B</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>EQMSRM</td><td>2L</td><td>8.625%</td><td>$600</td><td>5/15/2032</td><td>104.875</td><td>6.76%</td><td>235</td><td>B3 / B</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>EQMSRM</td><td>2L</td><td>8.000%</td><td>$500</td><td>3/15/2033</td><td>103.625</td><td>6.74%</td><td>227</td><td>B3 / B</td></tr><tr><td>Sean Wondrack</td><td>BUY</td><td>RIVHOL</td><td>1L HoldCo</td><td>10.000%</td><td>$1,250</td><td>1/15/2031</td><td>99.500</td><td>10.12%</td><td>584</td><td>N/A / N/A</td></tr></table>

Sources: Bloomberg Finance LP and DB \* Indicates pricing from EOD 6/17/26

<table><tr><td colspan="3">Potential Total Return Categorization by Ticker</td></tr><tr><td>Carry/low-beta5% - 9.99%</td><td>Moderate risk/mid-beta10% - 14.99%</td><td>Higher risk/high-beta&gt;15%</td></tr><tr><td>CROX</td><td>EQMSRM</td><td>WHR 5Y CDS</td></tr><tr><td>CYH</td><td>GTN</td><td></td></tr><tr><td>IHRT</td><td>HRI</td><td></td></tr><tr><td>PRIMBP</td><td>ITPCN</td><td></td></tr><tr><td>VTOL</td><td>PLAY</td><td></td></tr><tr><td></td><td>RIVHOL</td><td></td></tr><tr><td></td><td>WHR Bonds</td><td></td></tr></table>

<table><tr><td>Analyst</td><td>DB Rec</td><td>BBG Ticker</td><td>Ranking/ Seniority</td><td>Coupon</td><td>Amt O/S</td><td>Maturity</td><td>Price</td><td>YTW/YTM</td><td>STW</td><td>Mdy&#x27;s/ S&amp;P</td></tr><tr><td>Aaron Watts</td><td>NR</td><td>*CMGMCO</td><td>1L</td><td>S+350</td><td>$1.82bn</td><td>6/18/2029</td><td>90.000</td><td>11.23%</td><td>737</td><td>B3/B</td></tr><tr><td>Aaron Watts</td><td>NR</td><td>*CMGMCO</td><td>2L</td><td>8.875%</td><td>$574mm</td><td>6/18/2029</td><td>74.500</td><td>20.77%</td><td>1668</td><td>Caa3/CCC</td></tr><tr><td>Miles Highsmith</td><td>NR</td><td>RGCARE</td><td>1L</td><td>9.875%</td><td>$800</td><td>8/15/2030</td><td>105.625</td><td>4.89%</td><td>121</td><td>B2 / B</td></tr><tr><td>Miles Highsmith</td><td>NR</td><td>RGCARE</td><td>1L</td><td>7.000%</td><td>$1,500</td><td>5/1/2034</td><td>97.125</td><td>7.49%</td><td>300</td><td>B2 / B</td></tr><tr><td>Miles Highsmith</td><td>NR</td><td>RGCARE</td><td>Sr. Unsec&#x27;d</td><td>5.375%</td><td>$500</td><td>1/15/2029</td><td>96.000</td><td>7.11%</td><td>302</td><td>Caa1 / CCC+</td></tr><tr><td>Miles Highsmith</td><td>NR</td><td>RGCARE</td><td>Sr. Unsec&#x27;d</td><td>10.000%</td><td>$800</td><td>6/1/2032</td><td>101.750</td><td>9.31%</td><td>489</td><td>Caa1 / CCC+</td></tr><tr><td>Miles Highsmith</td><td>NR</td><td>RCM</td><td>Secured</td><td>6.875%</td><td>$1,300</td><td>11/15/2031</td><td>98.375</td><td>7.24%</td><td>287</td><td>B3/B-</td></tr><tr><td>Miles Highsmith</td><td>NR</td><td>USACUT</td><td>1L</td><td>9.750%</td><td>$1,000</td><td>5/15/2029</td><td>96.875</td><td>11.00%</td><td>691</td><td>B3 / B-</td></tr><tr><td>Ryan Dowling</td><td>NR</td><td>SHEARE</td><td>1L</td><td>S+275</td><td>$1,199</td><td>2/12/2031</td><td>98.250</td><td>6.83%</td><td>320</td><td>B2/B</td></tr><tr><td>Ryan Dowling</td><td>NR</td><td>SHEARE</td><td>1L</td><td>7.875%</td><td>$500</td><td>3/1/2031</td><td>100.750</td><td>7.56%</td><td>320</td><td>B2/B</td></tr><tr><td>Ryan Dowling</td><td>NR</td><td>SHEARE</td><td>Sr. Unsec&#x27;d</td><td>9.625%</td><td>$450</td><td>9/15/2032</td><td>97.500</td><td>10.17%</td><td>577</td><td>Caa2/CCC+</td></tr><tr><td>Sean Wondrack</td><td>NR</td><td>GLOBAU</td><td>Sr. Unsec&#x27;d</td><td>8.375%</td><td>$525</td><td>1/15/2029</td><td>99.375</td><td>8.63%</td><td>442</td><td>B3 / B+</td></tr><tr><td>Sean Wondrack</td><td>NR</td><td>GLOBAU</td><td>Sr. Unsec&#x27;d</td><td>8.750%</td><td>$525</td><td>1/15/2032</td><td>96.375</td><td>9.60%</td><td>528</td><td>B3 / B+</td></tr></table>

Sources: Bloomberg Finance LP and DB  
\* Indicates pricing from EOD 6/17/26

## 01. US Economics

Brett Ryan | +1 212 250-6294 | brett.ryan@db.com

Our baseline is that as long as oil prices have peaked, the economy is likely to weather another substantial shock relatively well. We currently project real GDP growth of 2.2% (Q4/Q4) this year, down only slightly from our estimate of 2.4% before the US/Iran war.

This downgrade reflects the drag from higher oil prices (roughly -0.2pp) as well as weaker consumer spending to start the year, counterbalanced by continued tailwinds for growth that include: supportive financial conditions and fiscal policy, robust productivity, and a continued strong pace of AI investments.


[中间内容因长度限制已省略]

nse in the Russian Federation.

Kingdom of Saudi Arabia: Deutsche Securities Saudi Arabia (DSSA) is a closed joint stock company authorized by the Capital Market Authority of the Kingdom of Saudi Arabia with a license number (No. 37-07073) to conduct the following business activities: Dealing, Arranging, Advising, and Custody activities. DSSA registered office is Faisaliah Tower, 17th Floor, King Fahad Road - Al Olaya District Riyadh, Kingdom of Saudi Arabia P.O. Box 301806.

United Arab Emirates: DB AG in the Dubai International Financial Centre (registered no. 00045) is regulated by the Dubai Financial Services Authority. DB AG - DIFC Branch may only undertake the financial services activities that fall within the scope of its existing DFSA license. Principal place of business in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by DB AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority.

Australia and New Zealand: This research is intended only for 'wholesale clients' within the meaning of the Australian Corporations Act and New Zealand Financial Advisors Act, respectively. Please refer to Australia-specific research disclosures and related information at https://www.dbresearch.com/PROD/RPS\_EN-PROD/PROD0000000000521304.xhtml. Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG
"""
