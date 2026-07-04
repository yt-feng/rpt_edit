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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/e760342b32cfd6ba43df8c885e9fcc9bf602224edeccb5b7c0ff5e4b06501dc8.jpg)

Annual Economic Report
June 2026

# The provided image contains no text. It is a graphic design featuring abstract line art and a stylized mountain silhouette, which is not textual content to extract. Therefore, no OCR output can be generated.

Annual Economic Report
June 2026

The views expressed here do not necessarily reflect the views of the BIS member central banks.

This publication is available on the BIS website (https://www.bis.org/publ/arpdf/ar2026e.htm).

© Bank for International Settlements 2026. All rights reserved. Brief excerpts may be reproduced or translated provided the source is stated.

ISSN 2616-9428 (print)

ISSN 2616-9436 (online)

ISBN 978-92-9259-961-4 (print)

ISBN 978-92-9259-960-7 (online)

## Contents

From resilience to robustness?......1
The year in review......1
Old and new fiscal-financial stability nexus......2
Policy implications......3
Stablecoins and beyond......4

I. Progress and peril....7   
Resilience tested....7   
A resilient start....7   
Box A: Global supply chains: adaptability and vulnerability....9   
The conflict and its peril....12   
Box B: The persistent economic effects of the Iran conflict....14   
Navigating progress and peril....17   
An inflation comeback....17   
AI progress and investment boom under pressure....19   
Box C: Transformative AI, long-term growth and r-star....20   
Financial vulnerabilities as amplifiers....23   
Fiscal positions under increasing strain....27   
Policy implications....28   
Endnotes....33   
Additional notes to graphs....33   
References....37

II. High public debt and shifting financial markets: challenges for central banks....41
Introduction....41
Near record-high public debt and evolving fiscal space....42
Box A: Insufficient debt consolidation in good times....44
Box B: Why financial intermediation matters for fiscal space....48
A new form of fiscal-financial stability nexus....49
The increasing role of NBFIs in government bond markets....50
Market functioning and fiscal policy interactions....53
International spillovers and the FX-repo link....54
When fiscal and financial risks reach the central bank....56
The effects of fiscal risk repricing and fiscal policy....56
Monetary policy transmission....58
Addressing market dysfunction....60
Confronting the emerging policy challenges....61

Monetary policy....61
Fiscal policy....62
Regulation....62
The design of central bank backstop facilities....64
Conclusion....64
Endnotes....66
Additional notes to graphs....69
References....71

III. Anchoring trust in money: innovation beyond stablecoins....77
Introduction....77
The foundations of trust in money....79
Foundational properties of money....79
Network effects of money....80
Today's two-tier architecture and the current wave of innovation....81
Box A: The historical emergence of money and of central banking....82
Digital innovation and the quest for new forms of money....83
DLT network settings....83
Box B: The economics of public permissionless blockchains....85
Emergence of stablecoins on public permissionless blockchains....87
Challenges associated with today's stablecoin arrangements....89
Box C: Regulatory frameworks for stablecoins....92
Macro-financial implications of stablecoins....93
Scenarios for stablecoin reserve assets....93
Macroeconomic implications....95
Box D: Quantifying the impact of stablecoins on bank lending and fiscal space....98
Stablecoin dollarisation....100
Box E: Deposit dollarisation and stablecoins....101
Moving towards the next-generation monetary system....104
Addressing issues in current stablecoin arrangements....105
Bringing technological innovation into the two-tier system....106
Conclusion....108
Endnotes....110
Additional notes to graphs....115
References....115

## Graphs

Chapter I
1 Global growth proved resilient despite tariff and geopolitical shocks...... 8
2 Several offsets muted the impact of tariffs...... 9
3 AI exuberance lent support to growth and kept financial conditions loose...... 11
4 Unprecedented blockade of the Strait of Hormuz disrupted activity...... 12
5 Asia is most exposed to the Hormuz energy supply shock...... 13
6 The conflict shifted inflation and policy outlooks...... 16
7 Risk appetite remained high despite the energy crisis...... 17
8 Severe energy shock increases inflationary pressures...... 18
9 Initial conditions determine upside risks to inflation...... 19
10 AI holds promise of large productivity gains, but with risks to labour markets...... 22
11 Rapid AI boom raises questions about its sustainability...... 23
12 Rich equity valuations are becoming a source of macroeconomic vulnerability...... 24
13 Corporate credit is vulnerable to repricing on AI disappointments...... 25
14 Sudden tightening of financial conditions may overly curtail credit supply...... 26
15 Higher public debt is cutting fiscal space...... 27
16 Fiscal vulnerability is growing on multiple fronts...... 28
17 Adverse supply shocks pose challenges to monetary policy...... 29
Chapter II
1 The evolution of government debt and deficits...... 43
2 Private debt has remained high since the Great Financial Crisis...... 46
3 Sovereign borrowing costs and stress episodes...... 47
4 The rise of non-bank financial institutions in AE sovereign debt markets...... 50
5 Hedge funds' repo borrowing has surged given lax funding terms...... 51
6 The broadening of the bank-sovereign nexus...... 53
7 Fiscal risk shocks and market liquidity: two-way interactions and tail risks...... 54
8 International dimensions: FX swaps and dealer linkages...... 55
9 The financial and real effects of fiscal risk repricing...... 57
10 High public debt blunts the price effects of monetary policy...... 59
11 Public debt maturity matters for monetary transmission...... 60
Chapter III
1 Stablecoin use focuses on crypto trading, with coins backed by low-risk assets...... 87
2 Stablecoin market growth concentrated in two US dollar-pegged coins...... 88
3 Stablecoin fragmentation and the lack of interoperability across blockchains...... 90
4 The first-round balance sheet effects of introducing stablecoins under different reserve asset scenarios...... 94
5 Quantifying the macroeconomic effects of stablecoin adoption...... 97
6 Limited pass-through of changes in interest rates to stablecoin yields from lending pools in decentralised finance...... 100
7 Stablecoins vs foreign currency deposits...... 103
8 Demand for foreign stablecoins connects FX markets with crypto ecosystem...... 104
9 Unified ledger, anchored in central bank money, to host different forms of tokenised private money...... 107

This Report went to press on 22 June 2026 using data available up to 29 May 2026. A section in the endnotes containing detailed explanations for the graphs and tables is included at the end of each chapter.

## Conventions used in the Annual Economic Report

std dev standard deviation
σ² variance
\$ US dollar unless specified otherwise
'000 thousands
mn million
bn billion (thousand million)
trn trillion (thousand billion)
% pts percentage points
bp basis points
bbl barrel
lhs, rhs left-hand scale, right-hand scale
pa per annum
sa seasonally adjusted
saar seasonally adjusted annual rate
mom month on month
yoy year on year
qoq quarter on quarter
... not available
. not applicable
– nil or negligible

Components may not sum to totals because of rounding.

The terms “country” and “economy” used in this publication also cover territorial entities that are not states as understood by international law and practice but for which data are separately and independently maintained. The designations used and the presentation of material in this publication do not imply the expression of any opinion whatsoever on the part of the BIS concerning the legal status of any country, area or territory or of its authorities, or concerning the delimitation of its frontiers or boundaries. Names of countries or other territorial entities are used in a short form which is not necessarily their official name.

Country codes

<table><tr><td>AE</td><td>United Arab Emirates</td><td>FR</td><td>France</td><td>MY</td><td>Malaysia</td></tr><tr><td>AL</td><td>Albania</td><td>GB</td><td>United Kingdom</td><td>NG</td><td>Nigeria</td></tr><tr><td>AM</td><td>Armenia</td><td>GE</td><td>Georgia</td><td>NI</td><td>Nicaragua</td></tr><tr><td>AR</td><td>Argentina</td><td>GG</td><td>Guernsey</td><td>NL</td><td>Netherlands</td></tr><tr><td>AT</td><td>Austria</td><td>GI</td><td>Gibraltar</td><td>NO</td><td>Norway</td></tr><tr><td>AU</td><td>Australia</td><td>GR</td><td>Greece</td><td>NZ</td><td>New Zealand</td></tr><tr><td>AW</td><td>Aruba</td><td>GT</td><td>Guatemala</td><td>PA</td><td>Panama</td></tr><tr><td>AZ</td><td>Azerbaijan</td><td>HK</td><td>Hong Kong SAR</td><td>PE</td><td>Peru</td></tr><tr><td>BA</td><td>Bosnia and Herzegovina</td><td>HN</td><td>Honduras</td><td>PH</td><td>Philippines</td></tr><tr><td>BB</td><td>Barbados</td><td>HR</td><td>Croatia</td><td>PK</td><td>Pakistan</td></tr><tr><td>BE</td><td>Belgium</td><td>HU</td><td>Hungary</td><td>PL</td><td>Poland</td></tr><tr><td>BG</td><td>Bulgaria</td><td>ID</td><td>Indonesia</td><td>PT</td><td>Portugal</td></tr><tr><td>BH</td><td>Bahrain</td><td>IE</td><td>Ireland</td><td>PW</td><td>Palau</td></tr><tr><td>BM</td><td>Bermuda</td><td>IL</td><td>Israel</td><td>PY</td><td>Paraguay</td></tr><tr><td>BO</td><td>Bolivia</td><td>IN</td><td>India</td><td>QA</td><td>Qatar</td></tr><tr><td>BR</td><td>Brazil</td><td>IS</td><td>Iceland</td><td>RO</td><td>Romania</td></tr><tr><td>BY</td><td>Belarus</td><td>IT</td><td>Italy</td><td>RS</td><td>Serbia</td></tr><tr><td>CA</td><td>Canada</td><td>JE</td><td>Jersey</td><td>RU</td><td>Russia</td></tr><tr><td>CH</td><td>Switzerland</td><td>JP</td><td>Japan</td><td>SA</td><td>Saudi Arabia</td></tr><tr><td>CL</td><td>Chile</td><td>KR</td><td>Korea</td><td>SE</td><td>Sweden</td></tr><tr><td>CN</td><td>China</td><td>KW</td><td>Kuwait</td><td>SG</td><td>Singapore</td></tr><tr><td>CO</td><td>Colombia</td><td>KY</td><td>Cayman Islands</td><td>SI</td><td>Slovenia</td></tr><tr><td>CR</td><td>Costa Rica</td><td>KZ</td><td>Kazakhstan</td><td>SK</td><td>Slovakia</td></tr><tr><td>CY</td><td>Cyprus</td><td>LB</td><td>Lebanon</td><td>SV</td><td>El Salvador</td></tr><tr><td>CZ</td><td>Czechia</td><td>LT</td><td>Lithuania</td><td>TH</td><td>Thailand</td></tr><tr><td>DE</td><td>Germany</td><td>LU</td><td>Luxembourg</td><td>TM</td><td>Turkmenistan</td></tr><tr><td>DK</td><td>Denmark</td><td>LV</td><td>Latvia</td><td>TR</td><td>Türkiye</td></tr><tr><td>DO</td><td>Dominican Republic</td><td>MA</td><td>Morocco</td><td>TW</td><td>Chinese Taipei</td></tr><tr><td>DZ</td><td>Algeria</td><td>MD</td><td>Moldova</td><td>UA</td><td>Ukraine</td></tr><tr><td>EA</td><td>euro area</td><td>ME</td><td>Montenegro</td><td>US</td><td>United States</td></tr><tr><td>EC</td><td>Ecuador</td><td>MK</td><td>North Macedonia</td><td>UY</td><td>Uruguay</td></tr><tr><td>EE</td><td>Estonia</td><td>MN</td><td>Mongolia</td><td>UZ</td><td>Uzbekistan</td></tr><tr><td>EG</td><td>Egypt</td><td>MO</td><td>Macao SAR</td><td>VE</td><td>Venezuela</td></tr><tr><td>ES</td><td>Spain</td><td>MT</td><td>Malta</td><td>VN</td><td>Vietnam</td></tr><tr><td>EU</td><td>European Union</td><td>MU</td><td>Mauritius</td><td>ZA</td><td>South Africa</td></tr><tr><td>FI</td><td>Finland</td><td>MX</td><td>Mexico</td><td></td><td></td></tr></table>

Currency codes

<table><tr><td>AED</td><td>UAE dirham</td><td>KRW</td><td>Korean won</td></tr><tr><td>ARS</td><td>Argentine peso</td><td>KWD</td><td>Kuwaiti dinar</td></tr><tr><td>AUD</td><td>Australian dollar</td><td>MAD</td><td>Moroccan dirham</td></tr><tr><td>BRL</td><td>Brazilian real</td><td>MXN</td><td>Mexican peso</td></tr><tr><td>CAD</td><td>Canadian dollar</td><td>MYR</td><td>Malaysian ringgit</td></tr><tr><td>CHF</td><td>Swiss franc</td><td>NOK</td><td>Norwegian krone</td></tr><tr><td>CLP</td><td>Chilean peso</td><td>NZD</td><td>New Zealand dollar</td></tr><tr><td>CNY (RMB)</td><td>Chinese yuan (renminbi)</td><td>PEN</td><td>Peruvian sol</td></tr><tr><td>COP</td><td>Colombian peso</td><td>PHP</td><td>Philippine peso</td></tr><tr><td>CZK</td><td>Czech koruna</td><td>PLN</td><td>Polish zloty</td></tr><tr><td>DKK</td><td>Danish krone</td><td>RON</td><td>Romanian leu</td></tr><tr><td>DZD</td><td>Algerian dinar</td><td>RUB</td><td>Russian rouble</td></tr><tr><td>EUR</td><td>euro</td><td>SAR</td><td>Saudi riyal</td></tr><tr><td>GBP</td><td>pound sterling</td><td>SEK</td><td>Swedish krona</td></tr><tr><td>HKD</td><td>Hong Kong dollar</td><td>SGD</td><td>Singapore dollar</td></tr><tr><td>HUF</td><td>Hungarian forint</td><td>THB</td><td>Thai baht</td></tr><tr><td>IDR</td><td>Indonesian rupiah</td><td>TRY</td><td>Turkish lira</td></tr><tr><td>ILS</td><td>new shekel</td><td>USD</td><td>US dollar</td></tr><tr><td>INR</td><td>Indian rupee</td><td>VND</td><td>Vietnamese dong</td></tr><tr><td>JPY</td><td>Japanese yen</td><td>ZAR</td><td>South African rand</td></tr></table>

Advanced economies (AEs): Australia, Canada, Czechia, Denmark, the euro area, Hong Kong SAR, Israel, Japan, Korea, New Zealand, Norway, Singapore, Sweden, Switzerland, the United Kingdom and the United States.

Major AEs (G3): the euro area, Japan and the United States.

Other AEs: Australia, Canada, Czechia, Denmark, Hong Kong SAR, Israel, Korea, New Zealand, Norway, Singapore, Sweden, Switzerland and the United Kingdom.

Emerging market economies (EMEs): Algeria, Argentina, Brazil, Chile, China, Colombia, Hungary, India, Indonesia, Kuwait, Malaysia, Mexico, Morocco, Peru, the Philippines, Poland, Romania, Russia, Saudi Arabia, South Africa, Thailand, Türkiye, the United Arab Emirates and Vietnam.

## Global: all AEs and EMEs, as listed.

Depending on data availability, country groupings used in graphs and tables may not cover all the countries listed. The grouping is intended solely for analytical convenience and does not represent an assessment of the stage reached by a particular country in the development process.

## From resilience to robustness?

The past year saw investment in artificial intelligence (AI) ecosystems help global growth to withstand the blow from major tariff hikes. Yet geopolitical headwinds and rising fiscal and financial fragilities remain. Reinforcing the foundations of effective macroeconomic and financial policies is increasingly critical. Such foundations include fiscal sustainability, an unambiguous commitment to price stability and congruent prudential policies across the financial system. Progress on each of these dimensions bolsters trust in the capacity of economic policies to deliver on their mandates. Building on the resilience of the past year, the challenge for authorities is to work towards greater robustness and thus to contribute to sustainable growth going forward.

## The year in review

Growth held up well in 2025, despite significant headwinds from higher tariffs and geopolitical uncertainty. Three factors stand out. First, the drag from higher trade barriers was lessened by effective tariff rates that were lower than initially anticipated, trade diversion and firms' willingness to absorb costs through lower margins. Second, a wave of optimism about AI spurred a surge in capital expenditure on AI infrastructure, lifting investment in the United States with spillovers along global supply chains. Third, animal spirits about AI lifted stock valuations, sustaining favourable global financial conditions.

Yet this resilience was soon tested in early 2026, when the closure of the Strait of Hormuz delivered a major shock to global energy supplies. Rising energy prices once again pushed inflation well above central banks' targets, echoing the post-Covid-19 inflation surge. Although the recent conflict in the Middle East seems to have abated, the economic effects of the Hormuz disruption may linger as the full restoration of physical energy supply takes time and the initial price increases propagate through supply chains. The closure of the Strait of Hormuz has raised the costs of manufacturing and agriculture inputs, with potentially dire consequences for food prices and food security among the poorest countries. Despite these challenges, financial markets have remained buoyant, reflecting expectations that the disruptions would be short-lived and the AI boom would continue.

Looking forward, four pressure points demand attention.

First, inflation has risen. The energy supply shock has been substantial, and its effects may propagate through supply chains. Global headline inflation picked up shortly after the conflict in the Middle East began, and prices of plastics and fertilisers – key inputs – have risen by 30% and 50%, respectively. The central question is whether these initial price increases will broaden and persist, as during 2021–23. On the one hand, mitigating factors limit second-round effects. Greater slack in the labour market may help to contain wage pressures. And policy rates are higher now than in 2022. On the other hand, memories of the post-pandemic inflation surge are still fresh. Given that it will take several quarters to purge the imbalances in oil physical markets, further volatility in energy prices could arise. In turn, inflation expectations could de-anchor more quickly than in the past.

Second, the optimism surrounding AI may not last, despite its promise of future productivity gains. The current surge in capital expenditure could prove unsustainable if supply bottlenecks restrain production. Intense competition for market leadership may fuel overinvestment further, as seen in previous innovation waves, increasing the risk of a sharp reversal if AI payoffs disappoint.

Third, financial vulnerabilities persist. Easy financial conditions could tighten and become a potent amplifier in adverse scenarios where interest rates rise and AI payoffs disappoint. Compressed risk premia and stretched valuations highlight the scope for unwinding. Increasingly opaque financing of AI activities, high leverage in core markets and the growing footprint of private credit further undermine the resilience of financial markets. The current tension between exuberant risk appetite and elevated macroeconomic risks could unwind abruptly.

Fourth, fiscal pressures are mounting. With already high debt levels, governments face rising demands for spending amid energy shocks and geopolitical tensions. These rising pressures coincide with a less benign financial environment than the one prevailing in the aftermath of the Great Financial Crisis. Moreover, GDP growth has also slowed from post-pandem

[中间内容因长度限制已省略]

33.

Griffin, J, K Mei and Z Wang (2025): "Are crypto anti-money laundering policies effective?", mimeo.

Griswold, G (1970): "Aboriginal patterns of trade between the Columbia Basin and the Northern Plains", Archaeology in Montana, vol 11, no 2–3.

Ha, J, M Kose and F Ohnsorge (2023): "One-stop source: a global database of inflation", Journal of International Money and Finance, vol 137, 102896.

Hausmann, R and U Panizza (2010): "Redemption or abstinence? Original sin, currency mismatches and counter-cyclical policies in the new millennium", Harvard University John F Kennedy School of Government, Growth Lab Working Papers, vol 23.

He, D, A Kokenyne, X Lavayssière, I Lukonga, N Schwarz, N Sugimoto and J Verrier (2022): "Capital flow management measures in the digital age: challenges of crypto assets", International Monetary Fund Fintech Note, no 2022/005.

Hempel, S, J P Perez-Sangimino and J X Wang (2026): "Banks in the age of stablecoins: lessons from their historical responses to financial innovations", FEDS Notes, 1 May.

Hernández de Cos, P (2026): "Stablecoins: framing the debate", speech at a Bank of Japan seminar, Tokyo, 20 April.

Hofmann, B, M Kaldorf and M Rottner (2026): "The macroeconomics of stablecoins", BIS Working Papers, no 1363.

Hofmann, B, A Mehrotra and J Paulick (2026): "Dollarisation and monetary control: what lessons for the rise of stablecoins?", mimeo.

Holmström, B (2015): "Understanding the role of debt in the financial system", BIS Working Papers, no 479.

Honohan, P and A Shi (2001): "Deposit dollarization and the financial sector in emerging economies", World Bank Policy Research Paper, no 2748.

Huang, X and T Keister (2025): "Can redemption fees prevent runs?", Federal Reserve Bank for New York Staff Reports, no 1160.

Ilzetzki, E, C Reinhart and K Rogoff (2019): "Exchange arrangements entering the 21st century: which anchor will hold?", Quarterly Journal of Economics, vol 134, no 2.

(2021): "Rethinking exchange rate regimes", in G Gopinath, E Helpman and K Rogoff (eds), Handbook of International Economics, vol 5.

Kocherlakota, N (1998): "Money is memory", Journal of Economic Theory, vol 81, issue 2.

Kose, M, S Kurlat, F Ohnsorge and N Sugawara (2022): "A cross-country database of fiscal space", Journal of International Money and Finance, vol 128, 102682.

Kosse, A, M Glowka, I Mattei and T Rice (2023): "Will the real stablecoin please stand up?", BIS Papers, no 141.

Levy-Yeyati, E (2006): "Financial dollarization: evaluating the consequences", Economic Policy, vol 21, no 45.

(2021): "Financial dollarization and de-dollarization in the new millennium", Fondo Latinoamericano de Reservas, working paper.

Liao, G and J Caramichael (2022): "Stablecoins: growth potential and impact on banking", Board of Governors of the Federal Reserve System International Finance Discussion Papers, no 1334.

Maechler, A M (2025): “How deposits can harness tokenisation”, remarks at the Singapore Fintech Festival, Singapore, 12 November.

Mehrling, P (2011): The new Lombard Street: how the Fed became the dealer of last resort, Princeton University Press.

Minto, A, A Kosse, T Shirakami and P Wierts (2026): "From cash to crypto: towards a consistent regulatory approach to illicit payments", BIS Papers, no 166.

Mitchell Innes, A (1913): "What is Money?", The Banking Law Journal, May.

Mueller, K, C Xu, M Lehbib and Z Chen (2025): "The global macro database: a new international macroeconomic dataset", NBER Working Paper, no 33714.

Nakamoto, S (2008): "Bitcoin: a peer-to-peer electronic cash system", white paper.

Nigrinis, A (2025): "The lending impact of stablecoin-induced deposit outflows", mimeo.

Quinn, S and W Roberds (2016): "Death of a Reserve Currency", International Journal of Central Banking, vol 12.

Reinhart, C, K Rogoff and M Savastano (2014): "Addicted to dollars", Annals of Economics and Finance, vol 15, no 1.

Reuter, M, I Agur, A Copestake, M Martinez Peria and K Teoh (2025): "Payment frictions, capital flows, and exchange rates", IMF Working Paper, no 2025/171.

Rolnick, A, B Smith and W Weber (1998): "Lessons from a laissez-faire payments system: the Suffolk Banking System (1825–58)", Federal Reserve Bank of Minneapolis Quarterly Review, vol 22.

Rolnick, A and W Weber (1982): "Free banking, wildcat banking, and shinplasters", Federal Reserve Bank of Minneapolis Quarterly Review, vol 6.

Schär, F (2024): "Enhancing financial services with permissionless blockchains", European Commission Report.

Schär, F, A Kosse, T Rice, T Shirakami and J Siridhasanakul (2026): "The anatomy of stablecoin transactions", BIS Working Papers, no 1359.

Schnabel, I and H S Shin (2004): "Liquidity and contagion: the crisis of 1763", Journal of the European Economic Association, vol 2, no 6.

Shin, H S (2023): "A blueprint for the future monetary system", speech on the occasion of the BIS Annual General Meeting, 25 June.

—— (2026): "Tokenomics and blockchain fragmentation", BIS Working Papers, no 1335.

Voellmy, L (2021): "Preventing runs with fees and gates", Journal of Banking & Finance, vol 125 (C), 106065.

Waller, C (2025): "Embracing new technologies and players in payments", speech given at the Payments Innovation Conference, Federal Reserve Board, Washington DC, 21 October.

Wang, J J (2025): “Banks in the age of stablecoins: some possible implications for deposits, credit, and financial intermediation”, FEDS Notes, December.

![](images/b5d03f00214f10add0f1b3705e968d9173a4505da7ba835a79e4a8c8f421a1bf.jpg)

![](images/ef55f0b94344372c9dd20fe6ba5e2db7119c045960c9121a4a9f79f695b55046.jpg)

Bank for International Settlements (BIS)

www.bis.org
email@bis.org

ISSN 2616-9428
ISBN 978-92-9259-961-4
"""
