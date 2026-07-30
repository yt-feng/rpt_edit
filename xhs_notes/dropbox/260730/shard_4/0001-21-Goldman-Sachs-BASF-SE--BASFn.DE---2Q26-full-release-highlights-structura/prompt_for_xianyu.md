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
# BASF SE (BASFn.DE): 2Q26 full release highlights structural transformation, focus on cash returns/deleveraging, and rising

Today (July 29) BASF released its full 2Q26 with EBITDA (b.s.i) coming in at €2,449mn (+18% vs. Vara Consensus - updated July 7th) with sales at €17,206mn (+5% vs. Vara Consensus). The company had already announced preliminary results on July 15, and today's results were in-line with the previously disclosed numbers (see here).

Divisions: On the volumes side, the biggest differences to consensus numbers were in the Chemicals division (+21% vs. consensus at +9%) and Nutrition & Care (+12% vs. consensus at +1%). Volumes beat consensus expectations across all divisions. Pricing at group level was below consensus expectations, the differences came mostly from Materials (+13% vs. consensus of +21%) as well as Nutrition & Care (-2% vs. consensus at +2%) and Agricultural Solutions (-3% vs. consensus at +1%). At the EBITDA level, Materials and Industrial Solutions were the main beats to consensus numbers (+28%/29% vs. consensus). The Corporate/Other division came in better than expectations on strong commodity trading results. Chemicals and Surface Technologies were the negative surprises with Chemicals margins -486bps below consensus expectations. All in, volumes came in stronger than expectations (+7.3% vs. consensus at +2.0%) while prices were below estimates (11.5% vs consensus at +12.7%).

Cash: Operating cash flow in the quarter was €524mn, down from €1,585mn in 2Q25 driven by higher receivables and inventory. The implied cash conversion (CFO/adj. EBITDA) for the quarter was 21% vs. 89% in 2Q25. Operating cash flow was also impacted by \~€200mn of cash transformation spending in relation to restructuring measures and new ERP systems in Agricultural Solutions. BASF expect higher earnings and lower capital expenditures to offset the higher working capital buildup for the full-year.

Outlook: BASF had already altered its FY26 guidance when it released its preliminary results - no incremental changes were made. EBITDA guidance stands at €6.9-7.7bn (from €6.2-7.0bn prior to the pre-release) vs. Vara Consensus at €7.3bn and GSe at €8.0bn, while free cash flow guidance is at €1.5bn-2.3bn vs. Vara Consensus €2.3bn and GSe at €1.36bn.

The conference call will be held at 07:30am UK time.

Georgina Fraser, Ph.D.
+44(20)7552-5984 |
georgina.fraser@gs.com
GS International

Marcus von Scheele
+44(20)7774-7676 |
marcus.vonscheele@gs.com
GS International

Thomas Ward  
+44(20)7051-2527 | thomas.ward@gs.com GS International

Gabriel Simoes  
+44(20)7051-6922 | gabriel.simoes@gs.com GS International

Exhibit 1: BASF 2Q26 Actuals vs. GSe and Consensus Volume and Price on Visible Alpha Consensus Data; Rest on Vara Consensus

<table><tr><td colspan="10">BASF 2Q26 Results Review</td></tr><tr><td>Interim results in EUR mn</td><td>Actual 2Q26</td><td>Cons 2Q26</td><td>Actual vs. cons</td><td>GSe Q226E</td><td>Actual vs. GS</td><td>Actual Q225</td><td>chg yoy</td><td>Actual Q126</td><td>chg qoq</td></tr><tr><td>P&amp;L items (cont.)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Chemicals</td><td>3,595</td><td>3,324</td><td>8.2%</td><td>2,906</td><td>23.7%</td><td>2,502</td><td>43.7%</td><td>2,662</td><td>35.0%</td></tr><tr><td>Materials</td><td>3,790</td><td>3,843</td><td>-1.4%</td><td>4,269</td><td>-11.2%</td><td>3,240</td><td>17.0%</td><td>3,238</td><td>17.0%</td></tr><tr><td>Industrial Solutions</td><td>2,328</td><td>2,283</td><td>2.0%</td><td>2,531</td><td>-8.0%</td><td>2,160</td><td>7.8%</td><td>2,092</td><td>11.3%</td></tr><tr><td>Surface Technologies</td><td>2,625</td><td>2,445</td><td>7.4%</td><td>2,082</td><td>26.1%</td><td>2,355</td><td>11.5%</td><td>2,409</td><td>9.0%</td></tr><tr><td>Nutrition &amp; Care</td><td>1,709</td><td>1,675</td><td>2.0%</td><td>1,600</td><td>6.8%</td><td>1,618</td><td>5.6%</td><td>1,669</td><td>2.4%</td></tr><tr><td>Agricultural Solutions</td><td>2,210</td><td>2,146</td><td>3.0%</td><td>2,288</td><td>-3.4%</td><td>2,198</td><td>0.5%</td><td>3,104</td><td>-28.8%</td></tr><tr><td>Corporate/Other</td><td>948</td><td>760</td><td>24.7%</td><td>787</td><td>20.5%</td><td>715</td><td>32.6%</td><td>849</td><td>11.7%</td></tr><tr><td>Sales</td><td>17,206</td><td>16,462</td><td>4.5%</td><td>16,462</td><td>4.5%</td><td>14,788</td><td>16.4%</td><td>16,023</td><td>7.4%</td></tr><tr><td>Chemicals</td><td>377</td><td>510</td><td>-26.1%</td><td>494</td><td>-23.7%</td><td>209</td><td>80.4%</td><td>233</td><td>61.8%</td></tr><tr><td>Materials</td><td>792</td><td>617</td><td>28.4%</td><td>693</td><td>14.3%</td><td>408</td><td>94.1%</td><td>511</td><td>55.0%</td></tr><tr><td>Industrial Solutions</td><td>434</td><td>337</td><td>28.8%</td><td>448</td><td>-3.1%</td><td>307</td><td>41.4%</td><td>361</td><td>20.2%</td></tr><tr><td>Surface Technologies</td><td>115</td><td>182</td><td>-36.8%</td><td>148</td><td>-22.2%</td><td>172</td><td>-33.1%</td><td>275</td><td>-58.2%</td></tr><tr><td>Nutrition &amp; Care</td><td>204</td><td>192</td><td>6.3%</td><td>205</td><td>-0.7%</td><td>196</td><td>4.1%</td><td>192</td><td>6.3%</td></tr><tr><td>Agricultural Solutions</td><td>448</td><td>386</td><td>16.1%</td><td>430</td><td>4.1%</td><td>417</td><td>7.4%</td><td>1,102</td><td>-59.3%</td></tr><tr><td>Corporate/Other</td><td>80</td><td>-142</td><td>156.3%</td><td>-99</td><td>-180.6%</td><td>-114</td><td>-170.2%</td><td>-319</td><td>-125.1%</td></tr><tr><td>Adj. EBITDA</td><td>2,449</td><td>2,082</td><td>17.6%</td><td>2,319</td><td>5.6%</td><td>1,595</td><td>53.5%</td><td>2,355</td><td>4.0%</td></tr><tr><td>Adj. EBITDA margin</td><td>14.2%</td><td>12.6%</td><td>159 bps</td><td>14.1%</td><td>15 bps</td><td>10.8%</td><td>345 bps</td><td>14.7%</td><td>-46 bps</td></tr><tr><td>EBITDA (reported)</td><td>1,965</td><td>2,032</td><td>-3.3%</td><td>2,256</td><td>-12.9%</td><td>1,318</td><td>49.1%</td><td>2,186</td><td>-10.1%</td></tr><tr><td>EBITDA (reported) margin</td><td>11.4%</td><td>12.3%</td><td>-92 bps</td><td>13.7%</td><td>-229 bps</td><td>8.9%</td><td>251 bps</td><td>13.6%</td><td>-222 bps</td></tr><tr><td>Adj. EBIT</td><td>685</td><td>1,081</td><td>-36.6%</td><td>1,453</td><td>-52.9%</td><td>685</td><td>0.0%</td><td>1,434</td><td>-52.2%</td></tr><tr><td>Adj. EBIT margin</td><td>4.0%</td><td>6.6%</td><td>-259 bps</td><td>8.8%</td><td>-485 bps</td><td>4.6%</td><td>-65 bps</td><td>8.9%</td><td>-497 bps</td></tr><tr><td>EPS (adj.)</td><td>1.28</td><td>0.85</td><td>50.6%</td><td>0.84</td><td>52.9%</td><td>0.48</td><td>164.5%</td><td>1.32</td><td>-3.2%</td></tr><tr><td>Balance sheet items</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net interest bearing debt (period end)</td><td>17,117</td><td></td><td></td><td>20,858</td><td>-17.9%</td><td>21,337</td><td>-19.8%</td><td>20,580</td><td>-16.8%</td></tr><tr><td>Cashflow items</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cash from operations</td><td>524</td><td></td><td></td><td>1,300</td><td>-59.7%</td><td>1,585</td><td>-66.9%</td><td>-797</td><td>-165.7%</td></tr><tr><td>Capex expenditure</td><td>-713</td><td></td><td></td><td>-909</td><td>-21.5%</td><td>-1,053</td><td>-32.3%</td><td>-578</td><td>23.4%</td></tr><tr><td>FCF</td><td>-189</td><td></td><td></td><td>391</td><td>-148%</td><td>532</td><td>-136%</td><td>-1,375</td><td>-86.3%</td></tr><tr><td>Volume % (y/y, cont.)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Chemicals</td><td>20.7%</td><td>8.5%</td><td>1218 bps</td><td>4%</td><td>1718 bps</td><td>-1%</td><td>2130 bps</td><td>11%</td><td>930 bps</td></tr><tr><td>Materials</td><td>4.6%</td><td>2.9%</td><td>169 bps</td><td>2%</td><td>260 bps</td><td>2%</td><td>310 bps</td><td>4%</td><td>30 bps</td></tr><tr><td>Industrial Solutions</td><td>4.9%</td><td>1.0%</td><td>389 bps</td><td>3%</td><td>228 bps</td><td>-3%</td><td>750 bps</td><td>1%</td><td>350 bps</td></tr><tr><td>Surface Technologies</td><td>-0.6%</td><td>-3.9%</td><td>326 bps</td><td>3%</td><td>-323 bps</td><td>13%</td><td>-1340 bps</td><td>-1%</td><td>70 bps</td></tr><tr><td>Nutrition &amp; Care</td><td>12.3%</td><td>1.1%</td><td>1117 bps</td><td>-5%</td><td>1686 bps</td><td>-4%</td><td>1620 bps</td><td>9%</td><td>340 bps</td></tr><tr><td>Agricultural Solutions</td><td>4.0%</td><td>-1.5%</td><td>545 bps</td><td>-3%</td><td>700 bps</td><td>21%</td><td>-1710 bps</td><td>3%</td><td>130 bps</td></tr><tr><td>Group</td><td>7.3%</td><td>2.0%</td><td>533 bps</td><td>1%</td><td>636 bps</td><td>4%</td><td>325 bps</td><td>5%</td><td>277 bps</td></tr><tr><td>Pricing % (y/y, cont.)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Chemicals</td><td>23.8%</td><td>25.5%</td><td>-166 bps</td><td>13%</td><td>1080 bps</td><td>-12%</td><td>3620 bps</td><td>-14%</td><td>3770 bps</td></tr><tr><td>Materials</td><td>13.3%</td><td>20.7%</td><td>-738 bps</td><td>30%</td><td>-1671 bps</td><td>-3%</td><td>1670 bps</td><td>-5%</td><td>1850 bps</td></tr><tr><td>Industrial Solutions</td><td>4.2%</td><td>5.9%</td><td>-174 bps</td><td>15%</td><td>-1079 bps</td><td>-2%</td><td>660 bps</td><td>-4%</td><td>820 bps</td></tr><tr><td>Surface Technologies</td><td>19.3%</td><td>11.4%</td><td>790 bps</td><td>-9%</td><td>2808 bps</td><td>4%</td><td>1580 bps</td><td>26%</td><td>-630 bps</td></tr><tr><td>Nutrition &amp; Care</td><td>-1.7%</td><td>2.3%</td><td>-400 bps</td><td>3%</td><td>-508 bps</td><td>3%</td><td>-500 bps</td><td>-5%</td><td>330 bps</td></tr><tr><td>Agricultural Solutions</td><td>-2.5%</td><td>1.4%</td><td>-391 bps</td><td>6%</td><td>-850 bps</td><td>-2%</td><td>-90 bps</td><td>-1%</td><td>-200 bps</td></tr><tr><td>Group</td><td>11.5%</td><td>12.7%</td><td>-121 bps</td><td>11%</td><td>12 bps</td><td>-3%</td><td>1451 bps</td><td>-1%</td><td>1277 bps</td></tr><tr><td>Adj. EBITDA margins % (cont.)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Chemicals</td><td>10.5%</td><td>15.3%</td><td>-486 bps</td><td>17.0%</td><td>-651 bps</td><td>8.4%</td><td>213 bps</td><td>8.8%</td><td>173 bps</td></tr><tr><td>Materials</td><td>20.9%</td><td>16.1%</td><td>484 bps</td><td>16.2%</td><td>467 bps</td><td>12.6%</td><td>830 bps</td><td>15.8%</td><td>512 bps</td></tr><tr><td>Industrial Solutions</td><td>18.6%</td><td>14.8%</td><td>388 bps</td><td>17.7%</td><td>95 bps</td><td>14.2%</td><td>443 bps</td><td>17.3%</td><td>139 bps</td></tr><tr><td>Surface Technologies</td><td>4.4%</td><td>7.4%</td><td>-306 bps</td><td>7.1%</td><td>-272 bps</td><td>7.3%</td><td>-292 bps</td><td>11.4%</td><td>-703 bps</td></tr><tr><td>Nutrition &amp; Care</td><td>11.9%</td><td>11.5%</td><td>47 bps</td><td>12.8%</td><td>-90 bps</td><td>12.1%</td><td>-18 bps</td><td>11.5%</td><td>43 bps</td></tr><tr><td>Agricultural Solutions</td><td>20.3%</td><td>18.0%</td><td>228 bps</td><td>18.8%</td><td>146 bps</td><td>19.0%</td><td>130 bps</td><td>35.5%</td><td>-1523 bps</td></tr><tr><td>Corporate/Other</td><td>8.4%</td><td>-18.7%</td><td>2712 bps</td><td>-12.6%</td><td>2106 bps</td><td>-15.9%</td><td>2438 bps</td><td>-37.6%</td><td>4601 bps</td></tr></table>

Source: Company data, Vara Research, Visible Alpha Consensus Data, GS Global Investment Research

## GS View

Limited incremental vs. the ad hoc but we expect investors will perceive the magnitude of the “Other” driven beat (mainly from commodity trading business gains) as lower quality. That said the strength of performance in Ag and Industrial Solutions we find higher quality than expected and more sustainable. Details on the weaker cashflow highlight BASF transformation costs weighing as well as working capital. The release highlights important structural changes taking place at BASF to set up for a more profitable future: 1) as of May 2026 FTE at BASF stood below 30,000 for the first time since 1954, 2) CoreShift targets 20% lower net cash fixed costs by 2029 vs. 2024 (the target is on cash fixed costs and a notable magnitude meaning it aims to go materially further than offsetting inflation, in our view). As long as management can reassure on its framework for determining “value creative M&A” we do not expect investors to be surprised by the more direct messaging re capital allocation (BASF states that the relative attractiveness of inorganic versus organic growth opportunities has increased).

Investors we speak to have been increasingly cautious on the shares even as geopolitical tensions started to rise again. We see little in the release to change the market's perception that we have seen the peak quarterly momentum at 2Q26 and that destocking/margin compression lies ahead for the coming quarters. Any change in sentiment would have to come from better-than-expected current trading commentary on the conference call, in our view.

## Valuation & Risks

## Valuation

We are Buy rated on BASF, with a 12-month price target of €57. We value BASF using 9.75x EV/DACF. We derive our multiple by applying a factor of 0.97 to the historical EV/DACF multiple of 10.0x. The factor is below 1 as our forecast CROCI is lower vs. history.

## Risks

## Downside risks to our view and price target include:

■ Weaker-than-expected demand in key end markets (automotive, construction, consumer goods) amid European recession or prolonged German industrial stagnation.

■ Value-destructive M&A if BASF consolidates European chemical assets.

■ Chinese chemical producers intensify competition on cost and capacity.

\- Chinese monetary and fiscal stimulus fails to support domestic production and domestic chemical demand.

BASF's Zhanjiang ramp is delayed and/or margins at the site remain subdued. This could lead to a lower-than-expected earnings contribution from the new businesses.

\- Inability to pass through feedstock cost inflation compressing margins in upstream chemicals.

■ Agricultural end markets weaken due to farmer economics and/or trade uncertainty.

■ Continued structural erosion of European chemical competitiveness due to energy costs, regulatory burden and capital flight.

Suez Canal fully reopens, lowering logistics costs and enabling an increase in Asian chemical imports into Europe.

<table><tr><td>BASFn.DE</td><td>12m Price Target: €57.00</td><td colspan="2">Price: €48.97</td><td colspan="2">Upside: 16.4%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9">Market cap: €45.0bn / $51.2bnEnterprise value:€66.6bn / $75.8bn3m ADTV: €122.0mn / $141.1mnGermanyEurope ChemicalsM&amp;A Rank: 3Leases incl. in net debt &amp; EV?:Yes</td><td>Revenue (€ mn)</td><td>59,657.0</td><td>61,911.7</td><td>60,685.1</td><td>62,407.3</td></tr><tr><td>EBIT (€ mn)</td><td>2,888.0</td><td>4,251.2</td><td>4,165.6</td><td>5,049.2</td></tr><tr><td>EPS (€)</td><td>2.24</td><td>3.09</td><td>2.78</td><td>3.37</td></tr><tr><td>P/E (X)</td><td>19.9</td><td>15.9</td><td>17.6</td><td>14.5</td></tr><tr><td>EV/EBITDA (ex lease,X)</td><td>8.5</td><td>7.5</td><td>7.3</td><td>6.8</td></tr><tr><td>Dividend yield (%)</td><td>5.1</td><td>4.9</td><td>6.1</td><td>6.1</td></tr><tr><td>FCF yield (%)</td><td>3.3</td><td>3.0</td><td>7.3</td><td>8.3</td></tr><tr><td>CROCI (%)</td><td>4.7</td><td>5.5</td><td>5.1</td><td>5.4</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>2.8</td><td>2.4</td><td>2.2</td><td>1.8</td></tr><tr><td></td><td></td><td>12/25</td><td>3/26E</td><td>6/26E</td><td>9/26E</td></tr><tr><td></td><td>EPS (€)</td><td>(1.39)</td><td>1.32</td><td>0.84</td><td>0.33</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 28 Jul 2026 close.

## Disclosure Appe

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
