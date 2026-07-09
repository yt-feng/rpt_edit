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
# Commodity Market Positioning & Flows

The OI finds a floor after six weeks of declines

\- The estimated value of open interest across tracked commodity markets increased marginally to \$1.7 trillion as of Jul 3 (Table 2, Figure 2). Across all trader types, contract-based outflows totalled \$13 billion WoW across all sectors, concentrated in crude oil market, which was largely offset by higher petroleum products, natural gas and precious metals prices over the week. This marks the first increase in the estimated OI value since its recent peak in mid-May, when the markets started to price in the reopening of the Strait of Hormuz. On the macro front, our economists continue to see a tightening labor market, alongside solid growth and sticky inflation, as the catalyst that pushes Fed policy rates higher (Global Data Watch: Which supply side are you on?, Kasman et al, 2 July 2026).

\- The estimated value of net investor positioning aggregated across global commodity futures markets decreased by 5% WoW (-\$9 billion WoW) to \$169 billion as of the latest data available (Table 1, Figure 3, Figure 4). The decline was largely driven by the energy and agricultural markets. Net length in energy markets declined by \$7 billion WoW, primarily driven by the decline across ICE Brent, where net length decreased from \$35 billion to \$30 billion over the week, followed by a \$1.7 billion net shortening in TTF natural gas to \$7.1 billion. Net length in agricultural markets declined by \$2.3 billion WoW, driven by declines across soy (-\$2.3 billion) and livestock markets (-\$1.3 billion), though partially offset by increases across coffee (+\$0.8 billion) and sugar (+\$0.5 billion) markets. Net length in precious metals increased by \$4 billion WoW, led by gold (\$3.5 billion WoW) and silver (\$0.8 billion WoW), while net length in base metals decreased by \$4.2 billion WoW, driven by copper and aluminum. JPM QDS's latest projections, as of July 6, indicate that positioning across commodity markets is set to increase by \$13 billion, largely driven by further lengthening in gold (+\$6 billion WoW), corn (+\$2.3 billion WoW), soy (+\$3.8 billion WoW), and coffee markets (+\$1.6 billion WoW).

\- The Global Commodities Inventory Monitor (GCIM) declined by 1% in June to 69 days-of-use. On an ex-China basis—which is a proxy for globally tradeable inventories—the monitor also declined by 2% in June to 58 days-of-use. The decline was largely driven by an estimated c. 100mn bbl decline in global oil inventories in June (c. 62mn bbl in China). This was further accelerated by declines in copper and aluminium inventories, partially offset by rising US natural gas availability in line with seasonal trends. Stripping out the seasonal impact of US natural gas storage, GCIM through June declined by 2% to 73 days-of-use. Ex-China commodity availability (ex. US natural gas) also declined by 2% in June to 64 days-of-use.

\- The estimated value of open interest in energy markets decreased by 1% WoW (-\$4 billion WoW) to \$718 billion (3 Jul, Figure 6). This was driven by net contract-based outflows of \$12 billion out of the crude oil markets, though partially offset by net contract-based inflows of \$4 billion into the petroleum products markets and a 7% increase in the ICE Gasoil price WoW. We note a surge in stranded oil which is re-entering the system, risking a temporary glut as demand (especially from China) remains subdued. The market's recovery

Global Commodities Research

Otar Dgebuadze, CFA
(44-20) 3493-8246
otar.dgebuadze@JPM.com
JPM Securities plc

Natasha Kaneva
(1-212) 834-3175
natasha.kaneva@JPM.com
JPM Chase Bank NA

Gregory C. Shearer
(44-20) 7134-8161
gregory.c.shearer@JPM.com
JPM Securities plc

Tracey Allen
(44-20) 7134-6732
tracey.l.allen@JPM.com
JPM Securities plc

Ali A. Ibrahim
(44-20) 3493-6438
ali.ibrahim@JPM.com
JPM Securities plc

Aradhaya Makkar
aradhaya.makkar@jpmchase.com
JPM India Private Limited

Ananyashree Gupta
(91-22) 6157 3627
ananyashree.gupta@jpmchase.com
JPM India Private Limited

hinges on two key variables—whether China resumes buying oil and how quickly global inventories are replenished. Our base case remains that China will ultimately return to the market and we estimate China's oil demand to decline by 600 kbd in 2026, before rebounding by 800 kbd in 2027. The estimated value of open interest in natural gas markets increased by 1% over the week to \$170 billion (3 Jul, Figure 13). This was driven by an increase in prices across European and Asian benchmarks which more than offset the net contract-based outflows of \$2.6 billion. We note that Qatar Energy continues broadly stable operations and, at its current observed pace and assuming the Strait remains open, we estimate it will reach its normalized full capacity (i.e., excluding the two damaged trains) in August, broadly in line with our existing forecasts.

\- The estimated value of open interest in precious metals markets increased by 3% WoW (\$7 billion) to \$250 billion, rebounding from the lows of the previous week (3 Jul, Figure 8). Across all trader types, the sector saw strong net contract-based inflows totalling \$2 billion WoW, primarily into gold (\$2.5 billion WoW), though it was slightly offset by outflows from silver (\$0.3 billion WoW). Meanwhile, net Managed Money positioning in COMEX Gold futures increased by 4.7k contracts to a total of 120k contracts net long. Amid a drop in buying intensity from other demand sectors for now, rate-sensitive ETF flows have regained marginal pricing power in gold, cementing a re-correlation between gold prices and real yields. While we ultimately think the Fed will end up remaining more patient this year, warding off sustained further significant downside for gold from current levels and allowing for a recovery higher over 2H26, reduced demand forecasts point towards an overall more range-bound base case gold outlook in the near-term with prices averaging \$4,300/oz in 3Q26 and \$4,500/oz in 4Q26.

\- The estimated value of open interest in base metals markets remained flat WoW at around \$212 billion (3 Jul, Figure 9). The sector saw net contract-based outflows across all trader types reaching \$0.6 billion WoW, as the outflows from aluminium and nickel (-\$2.6 billion WoW) were largely offset by inflows into lead and zinc, while net flows in copper were broadly muted. In China, copper inventories have been cumulatively drawn 82 kmt in the last 3 weeks. These significant reductions have reduced China's total copper inventory to multi-year lows for this time of year at 163kt. We interpret this as a signal of improved China copper consumption, synchronous with the US continuing to pull metal to COMEX, ahead of the US Department of Commerce decision on whether to impose US copper import tariffs.

\- The estimated value of open interest across environmental markets decreased by 3% WoW (-\$2 billion) to \$74.5 billion WoW (3 July, Figure 7). This was driven by net contract-based outflows of \$3.3 billion, primarily out of the EUA market as the June contract expired, partially offset by a 1.5% increase in the EUA prices. Investment Funds increased their net long position across EUAs as of 26 June to 62,116 lots, up by 3,327 lots WoW.

\- The estimated value of open interest in agricultural markets remained largely unchanged over the week at \$368 billion (3 July, Figure 10, Figure 14), as the impact of net contract-based outflows of \$2 billion, primarily out of corn and soybean/soymeal markets, and a decline in prices across the livestock markets, was largely offset by an increase in prices across the coffee and cotton markets. See Agricultural Commodities CFTC COT Report for relevant supplemental data across agricultural markets.

\- Price momentum increased across the agricultural markets, while it was largely mixed in energy and metals markets (3 July, Figure 17, Figure 18). Both long and short-term price momentum trading signals on CBOT Wheat and the short-term signal on sugar all switched positive to a ‘buy’ signal during the week, while the long-term price momentum trading signal on soybean switched negative to a ‘sell’. Meanwhile, gasoline momentum trading signal breached its positive threshold, indicating potential exhaustion in the buying trend.

Table 1: Net investor positioning across tracked commodity markets USD million

<table><tr><td rowspan="2"></td><td rowspan="2"># of markets /Last reported date</td><td rowspan="2">Lastreportedvalue</td><td rowspan="2">Latestprojection06-Jul-26</td><td rowspan="2">Projectionvs lastreported</td><td colspan="4">Change in Positioning (reported)</td></tr><tr><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td></tr><tr><td>Total Commodities</td><td>33</td><td>169,094</td><td>182,304</td><td>13,210</td><td>-9,451</td><td>-53,933</td><td>-45,122</td><td>-25,310</td></tr><tr><td>Energy</td><td>8</td><td>18,230</td><td>17,469</td><td>-762</td><td>-7,063</td><td>-17,206</td><td>-28,445</td><td>19,525</td></tr><tr><td>Crude Oil</td><td>3</td><td>29,680</td><td>28,433</td><td>-1,248</td><td>-5,457</td><td>-14,447</td><td>-29,905</td><td>15,734</td></tr><tr><td>ICE Brent</td><td>30-Jun-26</td><td>1,523</td><td>634</td><td>-888</td><td>-5,635</td><td>-16,062</td><td>-23,223</td><td>6,620</td></tr><tr><td>NYMEX WTI</td><td>30-Jun-26</td><td>7,682</td><td>7,322</td><td>-359</td><td>-710</td><td>-6,933</td><td>-15,151</td><td>3,868</td></tr><tr><td>ICE Dubai</td><td>30-Jun-26</td><td>20,476</td><td>na</td><td>na</td><td>889</td><td>8,547</td><td>8,469</td><td>5,246</td></tr><tr><td>Petroleum Products</td><td>3</td><td>-13,010</td><td>-12,610</td><td>400</td><td>166</td><td>3,914</td><td>12,553</td><td>-7,135</td></tr><tr><td>NYMEX Gasoline</td><td>30-Jun-26</td><td>6,879</td><td>7,269</td><td>390</td><td>403</td><td>-467</td><td>-1,394</td><td>1,502</td></tr><tr><td>ICE Gasoil</td><td>30-Jun-26</td><td>-20,399</td><td>na</td><td>na</td><td>-872</td><td>4,506</td><td>15,107</td><td>-7,523</td></tr><tr><td>NYMEX Heat Oil</td><td>30-Jun-26</td><td>511</td><td>521</td><td>10</td><td>635</td><td>-125</td><td>-1,160</td><td>-1,113</td></tr><tr><td>Natural Gas</td><td>2</td><td>1,560</td><td>1,645</td><td>86</td><td>-1,772</td><td>-6,673</td><td>-11,093</td><td>10,926</td></tr><tr><td>NYMEX Natgas</td><td>30-Jun-26</td><td>-5,594</td><td>-5,508</td><td>86</td><td>-33</td><td>300</td><td>-313</td><td>675</td></tr><tr><td>TTF Natgas</td><td>26-Jun-26</td><td>7,154</td><td>na</td><td>na</td><td>-1,739</td><td>-6,974</td><td>-10,780</td><td>10,251</td></tr><tr><td>Environmental</td><td>2</td><td>7,646</td><td>7,646</td><td>0</td><td>142</td><td>902</td><td>3,694</td><td>-6,367</td></tr><tr><td>EUA</td><td>26-Jun-26</td><td>5,888</td><td>na</td><td>na</td><td>258</td><td>896</td><td>3,046</td><td>-6,433</td></tr><tr><td>UKA</td><td>26-Jun-26</td><td>1,757</td><td>na</td><td>na</td><td>-117</td><td>6</td><td>648</td><td>65</td></tr><tr><td>Metals</td><td>10</td><td>123,821</td><td>130,320</td><td>6,499</td><td>-178</td><td>-21,571</td><td>4,967</td><td>-43,801</td></tr><tr><td>Precious</td><td>4</td><td>87,133</td><td>93,856</td><td>6,724</td><td>4,017</td><td>-2,320</td><td>4,374</td><td>-30,071</td></tr><tr><td>CMX Gold</td><td>30-Jun-26</td><td>78,355</td><td>84,586</td><td>6,232</td><td>3,463</td><td>-663</td><td>5,562</td><td>-24,964</td></tr><tr><td>CMX Silver</td><td>30-Jun-26</td><td>8,139</td><td>8,516</td><td>377</td><td>768</td><td>-900</td><td>-290</td><td>-3,795</td></tr><tr><td>NYMX Platinum</td><td>30-Jun-26</td><td>1,163</td><td>1,290</td><td>127</td><td>-92</td><td>-510</td><td>-577</td><td>-889</td></tr><tr><td>NYMX Palladium</td><td>30-Jun-26</td><td>-524</td><td>-536</td><td>-12</td><td>-123</td><td>-248</td><td>-321</td><td>-423</td></tr><tr><td>Base</td><td>6</td><td>36,688</td><td>36,464</td><td>-225</td><td>-4,194</td><td>-19,250</td><td>593</td><td>-13,730</td></tr><tr><td>CMX Copper</td><td>30-Jun-26</td><td>10,030</td><td>9,805</td><td>-225</td><td>-978</td><td>-3,128</td><td>4,435</td><td>1,217</td></tr><tr><td>LME Copper</td><td>3-Jul-26</td><td>9,982</td><td>na</td><td>na</td><td>-1,188</td><td>-5,647</td><td>872</td><td>-12,478</td></tr><tr><td>LME Aluminum</td><td>3-Jul-26</td><td>11,832</td><td>na</td><td>na</td><td>-1,742</td><td>-6,883</td><td>-5,469</td><td>-2,327</td></tr><tr><td>LME Zinc</td><td>3-Jul-26</td><td>4,609</td><td>na</td><td>na</td><td>671</td><td>127</td><td>1,975</td><td>1,931</td></tr><tr><td>LME Nickel</td><td>3-Jul-26</td><td>1,384</td><td>na</td><td>na</td><td>-743</td><td>-2,445</td><td>-1,505</td><td>-1,528</td></tr><tr><td>LME Lead</td><td>3-Jul-26</td><td>-1,148</td><td>na</td><td>na</td><td>-214</td><td>-1,273</td><td>284</td><td>-545</td></tr><tr><td>Agriculture</td><td>13</td><td>19,397</td><td>26,870</td><td>7,473</td><td>-2,352</td><td>-16,058</td><td>-25,338</td><td>5,333</td></tr><tr><td>Grains</td><td>6</td><td>9,156</td><td>15,587</td><td>6,431</td><td>-2,195</td><td>-16,752</td><td>-18,840</td><td>5,244</td></tr><tr><td>CBT Corn</td><td>30-Jun-26</td><td>1,324</td><td>3,591</td><td>2,266</td><td>129</td><td>-3,079</td><td>-5,204</td><td>131</td></tr><tr><td>CBT Wheat</td><td>30-Jun-26</td><td>-1,597</td><td>-1,291</td><td>306</td><td>-177</td><td>-368</td><td>-1,038</td><td>250</td></tr><tr><td>KBT Wheat</td><td>30-Jun-26</td><td>-316</td><td>-187</td><td>129</td><td>152</td><td>-30</td><td>-425</td><td>-268</td></tr><tr><td>CBT Soy beans</td><td>30-Jun-26</td><td>4,279</td><td>7,176</td><td>2,897</td><td>-1,353</td><td>-6,662</td><td>-7,794</td><td>-2,214</td></tr><tr><td>CBT Soy Meal</td><td>30-Jun-26</td><td>1,483</td><td>2,201</td><td>718</td><td>-304</td><td>-3,611</td><td>-2,160</td><td>1,555</td></tr><tr><td>CBT Soy Oil</td><td>30-Jun-26</td><td>3,982</td><td>4,098</td><td>115</td><td>-642</td><td>-3,001</td><td>-2,219</td><td>5,790</td></tr><tr><td>Softs</td><td>4</td><td>2,930</td><td>4,989</td><td>2,059</td><td>1,135</td><td>784</td><td>237</td><td>2,799</td></tr><tr><td>ICE Cotton</td><td>30-Jun-26</td><td>2,811</td><td>3,160</td><td>349</td><td>-279</td><td>-471</td><td>623</td><td>3,826</td></tr><tr><td>ICE Sugar</td><td>30-Jun-26</td><td>-1,554</td><td>-1,550</td><td>4</td><td>467</td><td>172</td><td>-398</td><td>780</td></tr><tr><td>ICE Coffee</td><td>30-Jun-26</td><td>2,396</td><td>3,996</td><td>1,600</td><td>771</td><td>1,095</td><td>67</td><td>-888</td></tr><tr><td>ICE Cocoa</td><td>30-Jun-26</td><td>-723</td><td>-618</td><td>106</td><td>176</td><td>-12</td><td>-55</td><td>-918</td></tr><tr><td>Livestock</td><td>3</td><td>7,311</td><td>6,294</td><td>-1,016</td><td>-1,291</td><td>-90</td><td>-6,736</td><td>-2,710</td></tr><tr><td>CME Live Cattle</td><td>30-Jun-26</td><td>9,074</td><td>8,264</td><td>-810</td><td>-841</td><td>602</td><td>-1,252</td><td>1,708</td></tr><tr><td>CME Lean Hogs</td><td>30-Jun-26</td><td>-2,349</td><td>-2,338</td><td>11</td><td>-193</td><td>-931</td><td>-4,036</td><td>-3,789</td></tr><tr><td>CME Feeder Cattle</td><td>30-Jun-26</td><td>586</td><td>369</td><td>-218</td><td>-257</td><td>239</td><td>-1,447</td><td>-629</td></tr></table>

<table><tr><td>Total Regions</td><td>33</td><td>169,094</td><td>182,304</td><td>13,210</td><td>-9,451</td><td>-53,933</td><td>-45,122</td><td>-25,310</td></tr><tr><td>US</td><td>22</td><td>126,037</td><td>140,136</td><td>14,099</td><td>981</td><td>-28,731</td><td>-34,547</td><td>-18,589</td></tr><tr><td>UK</td><td>9</td><td>30,015</td><td>29,127</td><td>-888</td><td>-8,951</td><td>-19,125</td><td>-2,841</td><td>-10,539</td></tr><tr><td>EU</td><td>2</td><td>13,042</td><td>13,042</td><td>0</td><td>-1,481</td><td>-6,077</td><td>-7,734</td><td>3,818</td></tr></table>

Where projections are not available, latest reported values are used for totals  


[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 07 Jul 2026 06:51 PM BST

Disseminated 07 Jul 2026 06:52 PM BST
"""
