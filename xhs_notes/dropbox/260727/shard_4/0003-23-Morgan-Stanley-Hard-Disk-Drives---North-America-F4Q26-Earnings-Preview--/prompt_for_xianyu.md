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
# F4Q26 Earnings Preview – Reigniting The Bull Case

Our HDD checks continue to strengthen and we expect both STX/WDC to report strong pricing-driven beats/raises this qtr. Expectations are growing, but we're pounding the table after this pullback and reiterate both STX/WDC as our favored OW's, with STX our tactical favorite into earnings/Top Pick.

## Key Takeaways

■ HDD fundamentals continue to strengthen, with demand visibility extending to 2032 and industry checks indicating a 300-400EB supply shortfall through 2027.

We expect STX and WDC to report near the high end of June guidance and guide September well-above Consensus as pricing momentum remains robust.

\- Pricing remains the key differentiator, with CY27-CY28 discussions moving towards \$25-30/TB and spot EBs carrying a 30-40%+ premium vs. contracted volumes.

Recent concerns around STX clean room expansion, NAND pricing, open-source AI, and compares to memory are overdone based on our checks.

Despite elevated headline P/Es, STX/WDC trade at \~16x base case CY27 EPS and \~7x bull case CY28 EPS, for 75%+ annual EPS growth through at least 2028.

For more details on our latest HDD views, please see IT Hardware: HDDs – The Next Leg Higher (15 Jun 2026) and Western Digital: Mgmt Meetings Highlight Customers Seeking Visibility Into 2032 (15 Jun 2026).

We view upcoming HDD earnings as an important catalyst to reignite confidence in the HDD bull case, and help to reinforce confidence in the broader AI infrastructure spending cycle. Our intra-quarter checks continue to point to a strengthening HDD pricing environment, tightening exabyte supply, and improving visibility into long-term demand from hyperscalers, which we believe will support meaningful upside to Street revenue, gross margin, and EPS expectations for both STX and WDC (and likely surpass high buy-side expectations). Importantly, this setup coincides with positive cloud capex revisions and accelerating cloud revenue growth, creating the potential for a broader re-rating across AI infrastructure beneficiaries that have underperformed in the last 4 weeks (macro/inflation/rates view notwithstanding). Conversations across the supply chain continue to suggest that the HDD market remains structurally undersupplied, with CY27-CY28 pricing discussions increasingly pushing towards \$25-30/TB and spot exabyte deals continuing to command a 30-40% (or greater) premium to contracted volumes. Against this backdrop, our sensitivity analysis (Exhibit 1) highlights where September quarter revenue, gross margin, and EPS could ultimately land for STX and WDC under a range of near-term pricing scenarios.

Erik W Woodring
Equity Analyst
Erik.Woodring@morganstanley.com +1 212 296-8083

Dylan Liu
Research Associate
Dylan.Liu@morganstanley.com +1 212 761-4519

Rauf Ural
Research Associate
Rauf.Ural@morganstanley.com +1 212 761-5958

## IT HARDWARE

North America
Industry View    Cautious

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

Beyond June and September quarter results, we expect investors to focus on management commentary around pricing beyond current guidance, the duration of demand visibility, long-term exabyte supply growth, customer capacity reservations extending into the next decade, and the pace of HAMR adoption as a driver of sustained earnings power. While STX and WDC currently trade at \~16x our base-case CY27 EPS estimates, and 12-13x our bull-case estimates (or \~11x our CY28 base case EPS / \~7x our CY28 bull case EPS), we view these valuations as attractive given the industry's improving pricing structure, expanding profitability, and stronger long-term demand visibility, particularly relative to STX's historical 8-14x trading range during periods of materially lower earnings power. We reiterate Overweight on both STX and WDC into earnings and maintain STX as our Top Pick.

Exhibit 1: While our September quarter EPS estimates are already 4-5% above Street, stronger pricing momentum could drive further earnings upside even in the near term.

<table><tr><td>Sept &#x27;26 Quarter</td><td>MSe</td><td>Cons</td><td>Diff.</td><td colspan="6">Potential Outcomes for Blended $/TB</td></tr><tr><td>STX</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>$/TB Q/Q Growth</td><td>3.7%</td><td>2.3%</td><td>130bps</td><td>3.0%</td><td>4.0%</td><td>5.0%</td><td>6.0%</td><td>7.0%</td><td>8.0%</td></tr><tr><td>Revenue ($M)</td><td>3,806</td><td>3,782</td><td>1%</td><td>3,782</td><td>3,819</td><td>3,856</td><td>3,892</td><td>3,929</td><td>3,966</td></tr><tr><td>Gross Margin</td><td>53.2%</td><td>49.9%</td><td>330bps</td><td>52.9%</td><td>53.4%</td><td>53.8%</td><td>54.3%</td><td>54.7%</td><td>55.1%</td></tr><tr><td>EPS</td><td>$6.11</td><td>$5.84</td><td>4%</td><td>$6.02</td><td>$6.15</td><td>$6.29</td><td>$6.42</td><td>$6.55</td><td>$6.69</td></tr><tr><td>WDC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>$/TB Q/Q Growth</td><td>3.6%</td><td>2.8%</td><td>80bps</td><td>3.0%</td><td>4.0%</td><td>5.0%</td><td>6.0%</td><td>7.0%</td><td>8.0%</td></tr><tr><td>Revenue ($M)</td><td>4,046</td><td>4,027</td><td>0%</td><td>4,028</td><td>4,067</td><td>4,106</td><td>4,145</td><td>4,184</td><td>4,223</td></tr><tr><td>Gross Margin</td><td>55.3%</td><td>51.8%</td><td>350bps</td><td>55.1%</td><td>55.5%</td><td>56.0%</td><td>56.4%</td><td>56.8%</td><td>57.2%</td></tr><tr><td>EPS</td><td>$3.96</td><td>$3.78</td><td>5%</td><td>$3.92</td><td>$4.00</td><td>$4.09</td><td>$4.17</td><td>$4.25</td><td>$4.34</td></tr></table>

Source: Company data, FactSet, MS estimates. Note: Consensus \$/TB estimates are calculated using Consensus revenue divided by MSe EB shipment estimates for both the June and September quarters.

We still believe the data retention tailwinds from AI are in the early innings, as our checks continue to point to a strengthening HDD demand outlook, with supply-demand dynamics becoming tighter and potentially longer-lasting than investors appreciate. HDD demand signals remain aligned with broader LLM adoption, new AI application launches (e.g. ByteDance's AI video app, Seedance), expanding enterprise AI deployments and data lake creation, and the ongoing need to generate and retain data for both model training and, increasingly, inferencing. Put differently, nearly every check we have done so far suggests either the HDD supply shortage is intensifying or the duration of the cycle is extending. For example, CSPs are now requesting capacity visibility through 2032, while our industry checks continue to indicate a 300-400EB HDD supply shortfall every year through CY28. Against that backdrop, HDD pricing discussions for CY27-CY28 are increasingly moving towards \$25-30/TB, per our early June checks, while out-of-contract EB volumes ("spot") currently command a 30-40%+ premium to contracted EBs. Importantly, HDD vendors are also becoming incrementally more constructive in their public commentary on pricing. During our roadshow with WDC in early June, management noted that "an opportunity exists" for \$/TB growth to reach teens % on a Y/Y basis, vs. +9% Y/Y in the March quarter.

Against this backdrop, we expect both STX and WDC to deliver June quarter results at the high end of guidance, supported by continued pricing momentum. While we are not changing our estimates into earnings, we expect June quarter results to come in solidly above both MSe and Consensus expectations. For what it's worth, the Nikkei reported nearline HDD pricing increased \~10% Q/Q during the June quarter. If accurate, that would imply meaningful upside to both our estimates and current Consensus expectations, though this feels quite aggressive vs. our \~3% Q/Q nearline price/EB base case forecasts, which are already above-Street. To be very clear, while spot pricing / negotiations for future nearline prices are both moving higher, most of the contracts impacting the June '26 quarter were decided quarters ago, meaning we should expect healthy upside to guidance/MSe/Consensus in the June quarter, but not the level quoted above. For STX, we expect June quarter revenue of \$3.50B-\$3.55B (vs. guidance of \$3.45B-\$3.55B) and gross margin of 50-51%, implying operating margin of 41.5-42.5% (vs. low-40% guidance) and EPS of \$5.14-\$5.33. For WDC, we expect June quarter revenue of \$3.70B-\$3.75B (vs. guidance of \$3.55B-\$3.75B) and gross margin of 52-53% (vs. guidance of 51-52%), resulting in EPS of \$3.34-\$3.44.

We also expect a strong September quarter outlook, with pricing remaining the primary driver of earnings upside. Our base case assumes HDD pricing continues to increase at a MSD% Q/Q pace, supporting revenue and margin trajectories above current Consensus expectations. That said, while "spot" EBs continue to transact at a meaningful premium, we do not expect broad-based nearline HDD pricing increases of 10%+ Q/Q in the September quarter. In our view, that is unlikely because: (1) "spot" EBs likely represent only 15-20% of nearline EB shipments, and (2) memory pricing did not begin its sharp upward move until September of last year – HDD pricing negotiations might not turn aggressive immediately after memory contract pricing increase. Even so, STX should benefit from a relative \$/TB tailwind as the discounted HAMR volumes shipped to GOOGL are largely fulfilled exiting the June quarter. In addition, as we enter a new fiscal year, both STX and WDC could see incremental benefit from higher-priced contracts coming into production. While we expect modest opex increases (\$5-10M Q/Q for STX and \$10-15M Q/Q for WDC), we still anticipate September quarter guidance to come in above MSe and meaningfully above Consensus. For STX, we expect guidance for revenue of \$3.80B-\$3.85B and gross margin of 53-54%, representing \~300bps of Q/Q expansion and implying operating margins in the mid-40% range and EPS of \$6.10-\$6.30 (Exhibit 2). For WDC, we expect management to guide to revenue of \$4.05B-\$4.15B and gross margin of 54-55%, 200bps higher Q/Q (we believe WDC guides a bit more conservatively than STX), implying EPS of \$3.95-\$4.15 (Exhibit 3).

Exhibit 2: STX: Our June quarter estimates are largely in line with Street, while our September quarter EPS estimate is 4% above Street, driven by both revenue and margin upside.

<table><tr><td rowspan="2">($M)</td><td colspan="5">Jun-26</td><td colspan="5">Sep-26</td></tr><tr><td>Reported</td><td>MSe Old</td><td>Diff.</td><td>Cons</td><td>Diff.</td><td>MSe New</td><td>MSe Old</td><td>Diff.</td><td>Cons</td><td>Diff.</td></tr><tr><td>Revenue</td><td>3,474</td><td>3,474</td><td>0%</td><td>3,497</td><td>-1%</td><td>3,806</td><td>3,806</td><td>0%</td><td>3,782</td><td>1%</td></tr><tr><td>Gross Profit</td><td>1,734</td><td>1,734</td><td>0%</td><td>1,747</td><td>-1%</td><td>2,027</td><td>2,027</td><td>0%</td><td>1,888</td><td>7%</td></tr><tr><td>Operating Profits</td><td>1,437</td><td>1,437</td><td>0%</td><td>1,468</td><td>-2%</td><td>1,724</td><td>1,724</td><td>0%</td><td>1,643</td><td>5%</td></tr><tr><td>Profit Before Tax</td><td>1,388</td><td>1,388</td><td>0%</td><td>1,403</td><td>-1%</td><td>1,679</td><td>1,679</td><td>0%</td><td>1,554</td><td>8%</td></tr><tr><td>Net Income</td><td>1,166</td><td>1,166</td><td>0%</td><td>1,171</td><td>0%</td><td>1,411</td><td>1,411</td><td>0%</td><td>1,334</td><td>6%</td></tr><tr><td>EPS</td><td>$5.05</td><td>$5.05</td><td>0%</td><td>$5.10</td><td>-1%</td><td>$6.11</td><td>$6.11</td><td>0%</td><td>$5.84</td><td>4%</td></tr><tr><td>Gross Margin</td><td>49.9%</td><td>49.9%</td><td>0bps</td><td>50.0%</td><td>-10bps</td><td>53.2%</td><td>53.2%</td><td>0bps</td><td>49.9%</td><td>330bps</td></tr><tr><td>Operating Margin</td><td>41.4%</td><td>41.4%</td><td>0bps</td><td>42.0%</td><td>-60bps</td><td>45.3%</td><td>45.3%</td><td>0bps</td><td>43.4%</td><td>180bps</td></tr><tr><td>Diluted Shares (M)</td><td>231</td><td>231</td><td>0%</td><td>230</td><td>1%</td><td>231</td><td>231</td><td>0%</td><td>228</td><td>1%</td></tr></table>

Source: Company data, FactSet, MS estimates

Exhibit 3: WDC: Our June quarter estimates are largely in line with Street, while our September quarter EPS estimate is 8% above Street, driven primarily by margin upside.

<table><tr><td rowspan="2">($M)</td><td colspan="5">Jun-26</td><td colspan="5">Sep-26</td></tr><tr><td>MSe New</td><td>MSe Old</td><td>Diff.</td><td>Cons</td><td>Diff.</td><td>MSe New</td><td>MSe Old</td><td>Diff.</td><td>Cons</td><td>Diff.</td></tr><tr><td>Revenue</td><td>3,685</td><td>3,685</td><td>0%</td><td>3,693</td><td>0%</td><td>4,046</td><td>4,046</td><td>0%</td><td>4,027</td><td>0%</td></tr><tr><td>Gross Profit</td><td>1,917</td><td>1,917</td><td>0%</td><td>1,905</td><td>1%</td><td>2,238</td><td>2,238</td><td>0%</td><td>2,085</td><td>7%</td></tr><tr><td>Operating Profits</td><td>1,522</td><td>1,522</td><td>0%</td><td>1,526</td><td>0%</td><td>1,829</td><td>1,829</td><td>0%</td><td>1,743</td><td>5%</td></tr><tr><td>Profit Before Tax</td><td>1,516</td><td>1,516</td><td>0%</td><td>1,519</td><td>0%</td><td>1,830</td><td>1,830</td><td>0%</td><td>1,750</td><td>5%</td></tr><tr><td>Net Income</td><td>1,273</td><td>1,273</td><td>0%</td><td>1,271</td><td>0%</td><td>1,537</td><td>1,537</td><td>0%</td><td>1,446</td><td>6%</td></tr><tr><td>EPS</td><td>$3.30</td><td>$3.30</td><td>0%</td><td>$3.30</td><td>0%</td><td>$3.96</td><td>$3.96</td><td>0%</td><td>$3.78</td><td>5%</td></tr><tr><td>Gross Margin</td><td>52.0%</td><td>52.0%</td><td>0bps</td><td>51.6%</td><td>40bps</td><td>55.3%</td><td>55.3%</td><td>0bps</td><td>51.8%</td><td>350bps</td></tr><tr><td>Operating Margin</td><td>41.3%</td><td>41.3%</td><td>0bps</td><td>41.3%</td><td>0bps</td><td>45.2%</td><td>45.2%</td><td>0bps</td><td>43.3%</td><td>190bps</td></tr><tr><td>Diluted Shares (M)</td><td>385</td><td>385</td><td>0%</td><td>386</td><td>0%</td><td>389</td><td>389</td><td>0%</td><td>383</td><td>2%</td></tr></table>

Source: Company data, FactSet, MS estimates

Recent investor concerns around capacity additions and cycle durability appear increasingly disconnected from what our checks are telling us. Over the last several weeks, we've heard a range of questions from investors, despite incrementally more bullish industry data points. The most common concerns center on: (1) STX's clean room expansion in Minnesota, (2) how HDD pricing should be viewed amid pockets of NAND pricing weakness, (3) whether recent open-source LLM launches or hyperscaler initiatives – such as META's move toward leasing datacenter capacity through a neocloud-like model – could ultimately pressure HDD demand, and (4) comparisons to memory stocks. We address each of these concerns below.

\- STX clean room expansion reflects HAMR requirements rather than broad-based capacity additions. Our checks suggest the expansion in MN represents \~20% additional capacity, but specifically for modern HAMR head wafers, which are not interchangeable with conventional head wafers. Assuming STX's nearline drives average \~23TB today, reaching 30-40TB+ capacities during C2H26 will, by definition, require significantly more HAMR heads than STX produces now. Importantly, this is not a greenfield expansion. In parallel, our Asia checks continue to point to \~5% HDD unit growth this year, with growth extending through 2030, supported by HAMR adoption, improved production yields, and shortening manufacturing cycle times.

\- We believe concerns linking potential NAND pricing weakness to HDD pricing are misplaced. While some investors have focused on softer NAND spot pricing in recent months, our HDD checks continue to indicate very robust pricing fundamentals, including CY27-CY28 negotiations headed towards

[中间内容因长度限制已省略]

rch relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: IT Hardware

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/24/2026)</td></tr><tr><td colspan="3">Erik W Woodring</td></tr><tr><td>Apple, Inc. (AAPL.O)</td><td>O (05/26/2009)</td><td>$333.02</td></tr><tr><td>CDW Corporation (CDW.O)</td><td>O (06/23/2026)</td><td>$133.82</td></tr><tr><td>Cricut Inc (CRCT.O)</td><td>U (08/12/2021)</td><td>$4.46</td></tr><tr><td>Dell Technologies Inc. (DELL.N)</td><td>E (06/01/2026)</td><td>$437.50</td></tr><tr><td>Everpure, Inc. (P.N)</td><td>E (06/11/2024)</td><td>$74.56</td></tr><tr><td>Garmin Ltd (GRMN.N)</td><td>E (02/18/2026)</td><td>$243.03</td></tr><tr><td>GoPro Inc (GPRO.O)</td><td>U (12/12/2023)</td><td>$0.67</td></tr><tr><td>Hewlett Packard Enterprise (HPE.N)</td><td>E (11/16/2025)</td><td>$47.69</td></tr><tr><td>HP Inc. (HPQ.N)</td><td>U (11/16/2025)</td><td>$25.75</td></tr><tr><td>IBM (IBM.N)</td><td>E (01/18/2023)</td><td>$214.19</td></tr><tr><td>Ingram Micro (INGM.N)</td><td>E (06/11/2025)</td><td>$29.44</td></tr><tr><td>Kornit Digital Ltd. (KRNT.O)</td><td>E (11/06/2025)</td><td>$15.23</td></tr><tr><td>Logitech International SA (LOGI.O)</td><td>U (01/20/2026)</td><td>$105.78</td></tr><tr><td>NetApp Inc (NTAP.O)</td><td>U (01/20/2026)</td><td>$167.74</td></tr><tr><td>Resideo Technologies Inc (REZI.N)</td><td>O (08/11/2025)</td><td>$34.54</td></tr><tr><td>Seagate Technology (STX.O)</td><td>O (03/26/2024)</td><td>$851.69</td></tr><tr><td>SmartRent, Inc. (SMRT.N)</td><td>++</td><td>$0.95</td></tr><tr><td>Sonos Inc. (SONO.O)</td><td>E (11/06/2025)</td><td>$14.69</td></tr><tr><td>TD Synnex Corporation (SNX.N)</td><td>O (06/11/2025)</td><td>$242.92</td></tr><tr><td>Teradata (TDC.N)</td><td>O (04/08/2025)</td><td>$28.52</td></tr><tr><td>Western Digital (WDC.O)</td><td>O (04/16/2025)</td><td>$519.80</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Nutanix Inc (NTNX.O)</td><td>E (01/12/2026)</td><td>$55.04</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
