你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# After the Rally, What's Next?

Low inventories, seasonally stronger demand, and the ongoing loss of supply has pushed JKM toward our forecast, with prices now up >2x YTD. VG & Cheniere have bounced off the late-June lows, but still trade below our estimate of base asset value. We review latest market trends & preview 2Q results.

## Key Takeaways

JKM prices +35% since the start of July, now up >2x YTD. With low storage & 20% of supply still offline, we would be buyers of any de-escalation pullbacks.

\- Cheniere: 2Q EBITDA of \~\$1.7 B sits near consensus while our full-year estimate of \$7.8 B is just above the FY26 guide of \$7.25-7.75 B.

■ EE: In-line 2Q EBITDA of \$119 MM with full-year estimate roughly aligned with the midpoint of guidance (MS: \$494 MM, guide: \$480-510).

NEXT: Phase 1 tracks of schedule and management hones in on growth with Train 6's FERC permit filed in May. Focus is on continuing to de-risk future projects.

VG: 2Q EBITDA of \$2.5 B, in-line with cons. MSe 2026 of \$8.5 B is just above cons of \$8.4 B and at the high end of the FY26 range.

JKM (Asia LNG) & TTF (European Gas) move higher. Over the last few months, we have argued that global LNG prices were too low, with risks skewed to the upside in 2H26 from low global inventories, seasonally recovering demand, ongoing loss of supply, and lingering geopolitical risks. As the Iran conflict re-escalated in early July, further delaying any resumption in Qatari exports, JKM and TTF prices have rallied sharply - up >35% since the start of the month and now \~2x higher than pre-conflict. Asia demand has recovered alongside supportive summer weather, +1% y/y over the past month, pulling cargos away from an EU market that desperately needs them. Over the last 30 days, European imports were -24% lower y/y, leaving storage only 54% full vs 64% this time last year. Even with a near-term restart of Qatari exports, normalizing storage ahead of winter appears increasingly unlikely. As a result, upside risks persist and we would be buyers of any de-escalation pullbacks in both the commodity and exposed stocks.

What's priced in? In late June we explored upside across the US LNG Exporters (see Exploring Upside). Share prices had broken far below our estimate of base asset value (assets that are operational, under construction, or locked in). While the stocks have recovered over the last few weeks, both VG and Cheniere still trade intrinsically cheap, on our estimates. We value VG's base portfolio (including under construction projects) at \$17/sh (+21% above the current share price) and \$272/sh for Cheniere (+4%). Execution on further growth, which we view as likely for both, represents upside to these figures. Conversely, NEXT is relatively in-line with our valuation.

Devin McDermott
Equity Analyst and Commodities Strategist
Devin.McDermott@morganstanley.com +1 212 761-1125

Joe Laetsch, CFA
Equity Analyst
Joe.Laetsch@morganstanley.com +1 212 761-8804

## DIVERSIFIED NATURAL GAS

North America
Industry View In-Line

Previewing 2Q results for US LNG companies. With this note, we refresh our forecasts for latest company updates. Our 2026 EBITDA estimates are largely in-line with consensus. See below for our views into earnings:

\- Cheniere. We forecast \$1.7 B of 2Q EBITDA (cons: \$1.7 B), representing a relatively clean quarter with no major operational disruptions or notable downtime. Our full-year estimate of \$7.8 B is unchanged vs prior (cons: \$7.8 B, guide: \$7.25 - 7.75), although would be closer to \$8.0 B if TTF/JKM futures as of 7/21 hold. Cheniere achieved substantial completion at CCL Stage 3 Train 6 in June and Train 7 is tracking towards fall completion. On July, 17th, Cheniere received permission from FERC to introduce fuel gas to the train. We continue to model full year sales volumes of \~53 mt. With Sabine Pass Train 7 now commercialized and limited notice to proceed (LNTP) issued, we look forward to receiving updates on permitting before final investment decision (FID, MSe YE26). Cheniere PT is unchanged at \$308, remain Overweight. CQP PT moves to \$62/sh (\$72 prior) as we shift some of our assumed future growth away from Sabine Pass to the Corpus Christi site, remain Equal-weight.

\- EE. We model \$119 MM of 2Q EBITDA (cons: \$118 MM) with full-year EBITDA of \$494 MM, slightly above consensus of \$491 MM and just below the midpoint of guidance (\$480 - 510 MM). We assume that EE did not receive its contracted volume under its Qatar LNG contract during 2Q, a \~\$3 MM EBITDA impact. We also now assume that this volume disruption persists through 3Q, but our full-year EBITDA estimate remains near the midpoint of guidance. We continue to model a mid-2027 start for the Iraq terminal. We look forward to receiving updates on fleet optimization, macro environment, growth project progress, and QatarEnergy deliveries on the call. PT of \$40/sh unchanged, stay Equal-weight.

\- NEXT. Rio Grande Phase 1 continues to track ahead of schedule and NEXT is messaging first LNG in 1H27, although directionality within those months is limited. While NEXT has been quietly preparing for commissioning on Train 1, the company has seconded \~100 people on the operations team to Bechtel to train employees and expedite commissioning. Looking towards longer-dated growth, NEXT filed its full application for Train 6 in late May -- an acceleration vs prior expectations. While we wait formal guidance on permit timing, NEXT expects to concurrently progress contracting and EPC negotiations. Stay Equal-weight with \$8/sh PT.

\- VG. We model $2.47$ B of 2Q EBITDA (cons $2.52$ B) with 37 cargoes from Calcasieu Pass and 90 from Plaquemines, anchored by fixed liquefaction fees of $6.45$ /mmbtu for the quarter (disclosed earlier this month). Earlier this summer, VG signed agreements with EnBW for a new LNG SPA and announced an upsize of its existing agreement with Atlantic-SEE. VG's 2026 guidance provided alongside 1Q earnings implies a liquefaction fee range of $9.50 - 10.50$ /mmbtu. We estimate actuals in 2Q were near the midpoint of this range, but bal-year pricing currently sits closer to $15$ – potentially supporting upside to VG's EBITDA outlook alongside 2Q results. Our EBITDA of $8.5$ B sits just above cons of $8.4$ B and at the high end of its $8.3 - 8.5$ B range. If current JKM/TTF prices hold, estimate would be closer to $9.0$ B.

Remain Overweight, \$22/sh PT.  
Exhibit 1: After a dip in June following MoU news, share prices have begun to recover for LNG stocks in our coverage.  
![](images/4ff041b7703a439de594f7fe9eb5fb00b64c4d8c65e146b8df52929ae4b96cd1.jpg)  
Source: FactSet, MS

Exhibit 2: JKM prices have rallied, in-line with our constructive view. Our 2026 forecasts remain modestly above the forward curve, more in-line on 2027-28.

<table><tr><td rowspan="2"></td><td colspan="3">Asia LNG (JKM)</td></tr><tr><td>MSe</td><td>Forward Curve</td><td>% Upside/Downside</td></tr><tr><td>3Q26e</td><td>$22.50</td><td>$21.64</td><td>4%</td></tr><tr><td>4Q26e</td><td>$25.00</td><td>$20.75</td><td>20%</td></tr><tr><td>Bal-2026e</td><td>$23.75</td><td>$20.97</td><td>13%</td></tr><tr><td>2027e</td><td>$15.00</td><td>$14.85</td><td>1%</td></tr><tr><td>2028e</td><td>$10.00</td><td>$10.58</td><td>-5%</td></tr><tr><td>Long Term</td><td>$10.00</td><td>N/A</td><td>N/A</td></tr></table>

Source: Bloomberg, MS

## LNG Supply & Demand Trends

Supply. CEO Saad Al-Kaabi said on July 9th that QatarEnergy had decided to halt plans to resume output after an attack on one of its tankers put the safety of strait transit in question. Back in June, QatarEnergy noted that it expects to be able to raise output to 50% of capacity a month after safe passage is restored and 80% within 2 months (all capacity excluding damaged trains). This week, Yemen's Houthis declared a naval blockade on Saudi Arabia, presenting risk to transit through Bab-el-Mandeb – a lesser impact for LNG but a move that could introduce greater geopolitical uncertainty as \~4.5 bbl/d of crude, condensate, and petroleum products transit through the waterway (see more here).

Outside of the Middle East, LNG supply disruptions have been somewhat minimal. Golden Pass (18 mtpa once fully ramped) continues commissioning, but recent feedgas flows indicate a spotty startup. So far, the facility has exported 4 cargoes (one currently en route to Korea, diverted away from the Netherlands and later Brazil). Freeport LNG (16.5 mtpa total) began planned maintenance on July 10th and feedgas flows fell accordingly. Latest messaging is that the turnaround is expected to last until late August. After Corpus Christi Stage 3 Train 6 achieved substantial completion in June, Train 7 appears on track for the fall, if not sooner.

Exhibit 3: Ex the Middle East, global liquefaction utilization in July so far has sat at 95%, above the 83% 5-year avg and 90% seen last year. August utilization is expected to sit at 92%, above last year's 91% and the 5-year avg of 84%.  
![](images/6e7dc194c5aa2dd0828eb903a155f2461b9fa586439951c74342fd61195ef6de.jpg)  
Source: Vortexa, MS

Exhibit 4: Feedgas flows at Golden Pass remain volatile as the facility continues commissioning.  
![](images/b11e965884f9004972a7363fa0b739178ad9bd88a6a0391debf53c64d5079b64.jpg)  
Source: Platts, MS

## Exhibit 5:

With the strait's status in flux, near-term deliveries on the water are limited. Beyond the 0.2 mtpa nearing final destinations, 0.5 mtpa is loaded and waiting behind the strait.

![](images/bf4d9f7549c7dc945c025df37971d1c2e9d97a5b4249a78b1441b257cf785f77.jpg)  
Source: Vortexa, MS. Note: Scheduled arrivals exclude vessels behind Strait of Hormuz, data as of 7.17.26

Demand. Global imports ex-Europe are 3% higher over the last 30 days y/y, driven in part by India (+12%) and Taiwan (+10%). Growth over the last 2 weeks has accelerated globally (ex-EU) as Japan (+25% y/y over last 2 weeks) has worked to refill inventories and Taiwan is 23% higher over that same time period. Since diversifying its sources of LNG, the US is Taiwan's largest supplier. July is shaping up to be warmer than normal with CDDs (cooling degree days) 5% above the 10-year normal while August is more in-line with normal levels. In Europe, July is expected to be the second hottest since 2000 with CDDs 26% above the 10-year normal. With European inventory levels below normal levels and imports lower than last year's, we expect LNG demand in the continent to accelerate over the coming quarters – driving LNG prices higher as a result.

Exhibit 6: Over the last 30 days, global imports ex-Europe are 3% higher y/y and are now flat y/y YTD.  
![](images/40659f20071536957488d20287a9a6adc3a51306a4230d0f28b4de61862b5921.jpg)  
Source: Vortexa, MS

Exhibit 7: Asia's LNG imports now sit 3% lower y/y YTD and are +1% over the last 30 days y/y– supported by 6% growth over the last 2 weeks compared to the same time last year.  
![](images/a1ac38276887ddae5e25622a31728f1957eeeb0a188d6ab50cd1c404db1a0dab.jpg)  
Source: Vortexa, MS

Exhibit 8: After dipping earlier in the summer, Japan's natural gas inventories have moved sharply higher...  
![](images/8969c8414fef22287d327277e90bdd69b2378dd3f9393c935508f97fbe707dcb.jpg)  
Source: Bloomberg, MS.

Exhibit 9: ... Supported by an increase in LNG imports. While YTD imports are 3% lower y/y and the 30-day figure is -4%, imports have recovered over the last 2 weeks and were 25% higher y/y.  
![](images/b9673246dc3394be8fe66d72f9f3cb3c475d393eebeb47000a896114f2890fbb.jpg)  
Source: Vortexa, MS.

Exhibit 10: In contrast, Europe's LNG imports sit 2% lower y/y YTD and -24% lower over the last 30 days y/y...  
![](images/9e15abd5d03f9cbdd0bf557171da1391ee2c63b783cfcb2156ad65febe39cc00.jpg)  
Source: Vortexa, MS.

Exhibit 11: ... and European gas inventories are now 54% full, below last year's 64% fill at this time and the 2016-25 average of 69%.  
![](images/304a649bfe680b2e8fcb7dcade1b80a215fe9108be5943a76fb0cd699d771bbd.jpg)  
Source: Bloomberg, MS.

## Exhibit 12:

We see the market in a shortfall this year, moving closer to balance in 2027-28 before swinging to a greater surplus later in the decade.

<table><tr><td>Global Supply Demand (mtpa)</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>2030</td></tr><tr><td>Global Demand</td><td>351</td><td>370</td><td>396</td><td>399</td><td>404</td><td>423</td><td>426</td><td>466</td><td>508</td><td>547</td><td>576</td></tr><tr><td>Sequential Growth</td><td>2%</td><td>5%</td><td>7%</td><td>1%</td><td>1%</td><td>5%</td><td>1%</td><td>9%</td><td>9%</td><td>8%</td><td>5%</td></tr><tr><td>Global Effective Capacity</td><td>412</td><td>407</td><td>417</td><td>436</td><td>440</td><td>446</td><td>448</td><td>510</td><td>560</td><td>607</td><td>656</td></tr><tr><td>Sequential Growth</td><td>7%</td><td>-1%</td><td>2%</td><td>5%</td><td>1%</td><td>1%</td><td>0%</td><td>14%</td><td>10%</td><td>8%</td><td>8%</td></tr><tr><td>Global Supply - Adjusted for Downtime</td><td>370</td><td>354</td><td>369</td><td>404</td><td>404</td><td>424</td><td>412</td><td>469</td><td>515</td><td>559</td><td>604</td></tr><tr><td>Utilization Rate</td><td>90%</td><td>87%</td><td>89%</td><td>93%</td><td>92%</td><td>95%</td><td>92%</td><td>92%</td><td>92%</td><td>92%</td><td>92%</td></tr><tr><td>Surplus/(shortage)</td><td>19</td><td>(16)</td><td>(27)</td><td>5</td><td>(0)</td><td>1</td><td>(13)</td><td>3</td><td>7</td><td>12</td><td>27</td></tr><tr><td>% surplus/(shortage)</td><td>5%</td><td>-4%</td><td>-7%</td><td>1%</td><td>0%</td><td>0%</td><td>-3%</td><td>1%</td><td>1%</td><td>2%</td><td>5%</td></tr><tr><td>Global Supply (ex-potential FIDs)</td><td>412</td><td>407</td><td>417</td><td>436</td><td>440</td><td>446</td><td>448</td><td>510</td><td>560</td><td>607</td><td>653</td></tr><tr><td>MSe Supply From Unsanctioned Projects</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3</td></tr><tr><td>Surplus/(shortage) at 92% utilization (Excluding potential FIDs)</td><td>19</td><td>(16)</td><td>(27)</td><td>5</td><td>(0)</td><td>1</td><td>(13)</td><td>3</td><td>7</td><td>12</td><td>24</td></tr></table>

Source: MS

## Venture Global (VG), Overweight, PT \$22

Remain Overweight, PT of \$22/sh. Venture Global's "design one, build many" approach for mid-scale factory-made trains provides attractive speed to market and outperformance vs. nameplate, a strength relative to peers. Further, VG's contracting strategy offers the most upside exposure to elevated global LNG prices, with \~15% of 2026 cargo sales open to the market as of the start of May and an average of 35% 2026-29 on VG's latest disclosure. For 2026, each \$1 change in margins on this unsold capacity impacts this year's EBITDA by \$300 - 350 MM as of the 1Q call in early May, making VG the most exposed name in our coverage to elevated global LNG prices. Guidance assumes an open liquefaction fee range of \$9.50-10.50/mmbtu for unsold cargoes.

Bolt-ons provide upside. Beyond existing and under-construction growth, Venture Global has messaged bolt-on expansions of \~10 mtpa at CP2 and \~6.4 mtpa at Plaquemines, both inclusive of optimization upside. VG expects to reach positive FID on the CP2 expansion in early 2027 with a short 18-month timeline to first LNG with a broader 2027 goal for the Plaquemines expansion. Regulatory pre-filing requirements were waived by FERC for CP2, while the Plaquemines bolt-on filed for approval with FERC and DOE in late 2025.

## Exhibit 13: Venture Global's bolt-on strategy

![](images/e055ebb10602fd79598b97abb53945abbf3ebee31a16f16fad191923c3cbf186.jpg)  
Source: Company presentation  
Plaquemines Bolt-on Phase I
> Addition of 8 mid-scale liquefaction train

[中间内容因长度限制已省略]

es and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Diversified Natural Gas

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/20/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Cheniere Energy Inc (LNG.N)</td><td>O (03/23/2026)</td><td>$264.95</td></tr><tr><td>Cheniere Energy Partners LP (CQP.N)</td><td>E (09/20/2019)</td><td>$63.83</td></tr><tr><td>Excelerate Energy Inc (EE.N)</td><td>E (11/06/2025)</td><td>$38.91</td></tr><tr><td>NextDecade Corporation (NEXT.O)</td><td>E (09/12/2025)</td><td>$7.68</td></tr><tr><td>Venture Global Inc (VG.N)</td><td>O (03/23/2026)</td><td>$14.29</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
