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
U.S. Semiconductors

Texas Instruments Inc

Rating

Market-Perform

Price Target

TXN

290.00 USD (250.00 OLD)

![](images/eb0b6a78881e81fff557a8ce7073553e9b04d94da7f9c8eb5d65ef7310d5bedb.jpg)

![](images/5804de50be86b844ffbab5c08315896e5c99d3704f9f9a3f58ff4fb72f1cab91.jpg)

Stacy A. Rasgon, Ph.D.
+1 213 559 5917
stacy.rasgon@bernsteinsg.com

![](images/e4c0045a3bd6a0a824366458ef13554d4bf9fcb1c3e686f39d5536910d3e4eee.jpg)

Alrick Shaw
+1 917 344 8454
alrick.shaw@bernsteinsg.com

Arpad von Nemes
+1 917 344 8461
arpad.vonnemes@bernsteinsg.com

Eva Zhang
+1 212 845 7839
yiwei.zhang@bernsteinsg.com

# Texas Instruments (TXN): Q226 recap - The world is not enough?

Texas Instruments' Q2 results were strong (\$5,463M/\$2.14/61.4\% vs Street at \$5,234M/\$1.93/59.5\%, including a 5 cent benefit not in guidance) with continued industrial recovery and datacenter growth, and more positive auto performance. Industrial grew \~30\% YoY and \~10\% QoQ; Data center doubled Y/Y and rose\~20\% QoQ, and Automotive grew mid-teens \% YoY and climbed HSD\% QoQ. Personal electronics were flat YoY and were up HSD\% QoQ, while communications equipment continued to grow YoY and QoQ. Gross margins at 61.4\% were \~185bps above expectations on better revenues and loadings.

Q3 guidance was well above consensus ( $5.90B$ / $2.40$ /\~62% vs Street $5.61B$ / $2.15$ /60.4%), seasonal to perhaps a touch above with similar drivers (industrial, datacenter, automotive etc, though with possibly weaker PE vs normal patterns). Capex was reiterated at in the $2$ - $3B$ range for the year, probably closer to the high end (vs \~ $4.6B$ in 2025).

This was another solid print from the company as industrial strength persists, datacenter accelerates, and automotive grows more positive, and results were pretty clean; the only issue is that a strong beat was likely already expected given those dynamics are fairly well known at this point. From here the questions will probably center around how much longer the industrial cycle can continue (we note this was the company's strongest Q2 QoQ growth since 2009), how long it will take datacenter (currently low double digit % of sales?) to become truly meaningful, what happens to PE into year-end, and whether or not pricing actions can help drive gross margins higher; given we are moving into the 2H we would (as always) also watch seasonality into Q4 (which still appears to be mis-modeled by consensus, something to watch into October).

Overall though we have few nitpicks to go after here and can see good things happening, though given valuation we prefer to look elsewhere in our space for now.

Raising estimates and rolling valuation horizon forward to avg FY27/28, PT raised from \$250 to \$290 (30x, unchanged, on avg FY27/28 EPS). We rate TXN MP.

## Investment Implications

TXN (MP, \$290): TXN shares feel fully valued in the current environment.

<table><tr><td>Reported EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>TXN (USD)</td><td>5.45</td><td>8.33</td><td>9.16</td></tr><tr><td>OLD</td><td>--</td><td>7.62</td><td>8.22</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

![](images/d60a39b50ab8ccbbb5328794fde24d92f9f7c6d0cf92ea63ab63f329091710a8.jpg)

<table><tr><td>Close Date</td><td>22 Jul 2026</td></tr><tr><td>TXN Close Price (USD)</td><td>294.19</td></tr><tr><td>Price Target (USD)</td><td>290.00</td></tr><tr><td>Upside/(Downside)</td><td>(1)%</td></tr><tr><td>52-Week Range</td><td>334.03/152.73</td></tr><tr><td>SPX</td><td>7,498.96</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>1.9%</td></tr><tr><td>Market Cap (USD) (M)</td><td>267,740</td></tr><tr><td>EV (USD) (M)</td><td>274,791</td></tr></table>

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>EBIT (M)</td><td>5,710</td><td>8,737</td><td>9,764</td><td>--</td></tr><tr><td>FCF (M)</td><td>2,603</td><td>8,159</td><td>9,523</td><td>--</td></tr><tr><td>Revenues (M)</td><td>17,682</td><td>21,661</td><td>23,171</td><td>--</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>69.6</td><td>(11.5)</td><td>50.9</td><td>36.9</td></tr><tr><td>SPX (%)</td><td>9.5</td><td>0.4</td><td>8.5</td><td>18.8</td></tr><tr><td>Relative (%)</td><td>60.0</td><td>(11.8)</td><td>42.4</td><td>18.0</td></tr></table>

Price Performance, 1YR  
Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Reported P/E (x)</td><td>54.0</td><td>35.3</td><td>32.1</td></tr></table>

## DETAILS

For our updated TXN model please click here: TXN model.

Texas Instruments' Q2 results were strong (\$5,463M/\$2.14/61.4\% vs Street at \$5,234M/\$1.93/59.5\%, including a 5 cent benefit not in guidance) with continued industrial recovery and datacenter growth, and more positive auto performance. Industrial grew \~30\% YoY and \~10\% QoQ; Data center doubled Y/Y and rose\~20\% QoQ, and Automotive grew mid-teens\% YoY and climbed HSD\% QoQ. Personal electronics were flat YoY and were up HSD \% QoQ, while communications equipment continued to grow YoY and QoQ. Gross margins at 61.4\% were \~185bps above expectations on better revenues and loadings.

\- Texas Instruments' results beat consensus on revenues and on EPS (\$5,463M/\$2.14 vs Street \$5,234M/\$1.93 and guidance \$5,200M/\$1.91) (Exhibit 1).

\- Analog, Embedded and Other were all above expectations (Exhibit 2).

\- Total revenue was up \~13% sequentially, better than typical seasonality (Exhibit 3) and grew \~23% YoY.

\- Analog sales of \$4,365M were up \~11% QoQ and up \~26% YoY (Exhibit 5). Operating margins for the segment were 45.6%, up \~390bps QoQ.

\- Embedded Processing sales of \$788M were up \~9% QoQ and up \~16% YoY (Exhibit 5). Segment operating margins came in at 21.3%, up \~440bps QoQ.

\- Other Revenues of \$310M grew \~74% QoQ and were down \~2% YoY (Exhibit 5). Operating margins were 48.4% for the quarter.

\- On a sequential basis, Datacenter revenue was up \~20%, Industrial was up \~10%, Auto was up HSD %, Personal Electronics was up HSD%, and Comms equipment grew as well. On a YoY basis, Datacenter grew the fastest (doubled), followed by Industrial (>30%), Auto (mid-teens %), Comms equipment (positive growth), and PE (\~flat) (Exhibit 6).

\- Gross margins were 61.4% vs 58.0% last quarter (Exhibit 7), and were \~185bps above street expectations of 59.5% (Exhibit 8) due to higher revenue and loadings.

\- Opex for the quarter came in at \$1,025M (excluding acquisition expenses of \$17M), higher than our estimate (\$1,010M) and consensus (\$1,006M).

Q3 guidance was well above consensus on revenues and EPS, with margins also above (\$5.90B/\$2.40/\~62% vs Street \$5.61B/\$2.15/60.4%), seasonal to perhaps a touch above with similar drivers (industrial, datacenter, automotive etc, though with possibly weaker PE vs normal patterns). Capex was reiterated at in the \$2-\$3B range for the year, probably closer to the high end (vs \~\$4.6B in 2025).

\- TXN sees Q326 at \$5.90B/\$2.40, well above Street expectations on revenues and EPS with Street at \$5,614M/\$2.15 (Exhibit 9). Revenues are seen up \~8% sequentially, seasonal to perhaps a bit above (Exhibit 4).

\- Gross margins appear implicitly guided at \~62% or so (Exhibit 10, Exhibit 11), above consensus (60.4%).

\- Opex is expected to be flattish QoQ (suggesting \~\$1,025M excluding acquisition charges, roughly in-line with consensus expectations of \$1,016M).

\- EPS was guided to \$2.40 at the midpoint, above the Street at \$2.15 on higher revenues and margins.

\- Management suggested that while Q3 is typically driven by personal electronics, strength will be more broad-based this time with continued upside in Industrial, Data Center and Automotive; it sounded like personal electronics will grow less than usual (unsurprising given the current memory dynamics).

\- Capex for the year was reiterated to land between \$2B-\$3B, with capex focus shifting to assembly and test equipment. Management noted capex could possibly skew to high-end of this range given the demand profile.

This was another solid print from the company as industrial strength persists, datacenter accelerates, and automotive grows more positive, and results were pretty clean; the only issue is that a strong beat was likely already expected given those dynamics are fairly well known at this point. From here the questions will probably center around how much longer the industrial cycle can continue (we note that this was the company's strongest Q2 QoQ growth since 2009), how long it will take datacenter (currently low double digit % of sales?) to become truly meaningful, what happens to PE into year-end, and whether or not pricing actions can help drive gross margins higher; given we are moving into the 2H we would (as always) also watch seasonality into Q4 (which still appears to be mis-modeled by consensus, something to watch into October). Overall though we have few nitpicks to go after here and can see good things happening, though given valuation we prefer to look elsewhere in our space for now.

\- The analog recovery continues to pick up steam in industrial. Datacenter (power, etc), while not that big for the company (yet) remains (unsurprisingly) strong, doubling YoY in Q2 and accelerating from Q1 (where it rose 90% YoY). And automotive (which has been a touch squishier) seems to be growing more positive.

\- From here questions will probably center around how much longer the industrial cycle (which has been going on for quite a few quarters) can persist (we note that this was the company's strongest Q2 QoQ growth since 2009...), how long it will take datacenter (we think currently low double-digit % of sales) to become truly meaningful, what happens to PE into year-end, and whether (or if) pricing can help to drive gross margins structurally higher (we note gross margins are likely going up a bit QoQ into Q3 but not a ton in the context of the sequential volume increase and supposed beginning of some pricing impact).

\- Given we are moving into the 2H we would also (as always) call out a watch into Q4 seasonality, which once again may be mis-modeled by consensus; normal seasonal patterns into Q4 generally call for a high single to low double digit sequential decline (even an argument for lower PE exposure probably would not fully eliminate this), whereas consensus remains above this (something to watch into October) (Exhibit 12).

\- Overall though we have few nitpicks to go after here, and can see good things happening as growth returns and FCF (and FCF/share) build to higher levels. Given valuations though (>30x our new 2027 EPS?) we prefer to look elsewhere for now (Exhibit 13).

## Other Tidbits:

\- Inventories on the balance sheet were down \$90M QoQ at \$4,605M vs last quarter at \$4,695M. Days of inventory came in at 196 vs. 209 last quarter (Exhibit 14). Inventory days are below their target range ("over 200 days").

\- Cash return for the quarter totaled \$1,322M, combining dividends of \$1,295M and share repurchases of \$27M (Exhibit 15, Exhibit 16), while free cash flow grew again sequentially to \$2,738M vs \$1,399M last quarter (Exhibit 17).

\- Over the last 12 months the company has returned \~90% of FCF, which has come down over the last quarters with FCF improving as the company is now nearing the end of its multi-year capex cycle (Exhibit 18).

\- Capex was \$514M for the quarter, \~9% of revenue.

We update our model, raising estimates. We roll our valuation horizon forward from FY27 to the average of FY27/28. We raise our price target to \$290 from \$250 previously (30x, unchanged, on avg FY27/28 EPS) and maintain our Market-Perform rating.

• We update our model, raising estimates.

\- Given we are halfway through the year, we roll our valuation horizon forward from FY27 to the average of FY27/28.

\- We raise our FY2026 revenue estimate from \$20.7B to \$21.6B, FY2027 from \$21.7B to \$23.2B, and FY2028 from \$22.8B to \$24.3B.

\- We raise our FY2026 GAAP diluted EPS estimate from \$7.62 to \$8.33, FY2027 from \$8.22 to \$9.16, and FY2028 from \$9.05 to \$9.94.

\- We raise our price target from \$250 (\~30x, unchanged, on our FY27 GAAP diluted EPS of \$8.22) to \$290 (\~30x on the average of our FY27/28 GAAP diluted EPS estimates of \~\$9.55).

• We maintain our Market-Perform rating.

EXHIBIT 1: TXN Q2 results were above the high-end of the guidance and beat consensus both on top and bottom-line.

<table><tr><td>Q226</td><td>Prior Guidance</td><td>Actual</td><td>Consensus</td><td>Actual vs. Consensus</td><td>Bernstein</td><td>Actual vs. Bernstein</td></tr><tr><td>Revenue ($M)</td><td>$5,200</td><td>$5,463</td><td>$5,234</td><td>$229</td><td>$5,201</td><td>$262</td></tr><tr><td>EPS</td><td>$1.91</td><td>$2.14</td><td>$1.93</td><td>$0.21</td><td>$1.91</td><td>$0.23</td></tr></table>

Source: Company reports, Bloomberg, Bernstein estimates and analysis

EXHIBIT 2: All segments were above expectations

<table><tr><td>Q226 Actual vs Cons ($M)</td><td>Analog</td><td>Embedded</td><td>Other</td></tr><tr><td>Actual</td><td>$4,365</td><td>$788</td><td>$310</td></tr><tr><td>Consensus</td><td>$4,229</td><td>$775</td><td>$250</td></tr><tr><td>Difference</td><td>$136</td><td>$13</td><td>$60</td></tr><tr><td>Bernstein</td><td>$4,199</td><td>$752</td><td>$251</td></tr><tr><td>Difference</td><td>$166</td><td>$36</td><td>$59</td></tr></table>

Source: Company reports, Bloomberg, Bernstein estimates and analysis

EXHIBIT 3: Q2 revenues were up 13%, above seasonality (and the strongest since 2009)...  
![](images/3344c5c4fb75e25c34aa0ce53633000cc7f75f3c89648b86a65a24caf2b54e53.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 4: ... with Q3 guided up \~8% QoQ, roughly in-line to above typical seasonality  
![](images/542bc2ff60ed6ad1fe4c11f26073817e2b6ce44c515f9f0bf14849cd127ef868.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 5: Analog and Embedded were both up YoY and up QoQ, while Other revenue was up sequentially and down slightly YoY

<table><tr><td>($MM)</td><td>Q122</td><td>Q222</td><td>Q322</td><td>Q422</td><td>Q123</td><td>Q223</td><td>Q323</td><td>Q423</td><td>Q124</td><td>Q224</td><td>Q324</td><td>Q424</td><td>Q125</td><td>Q225</td><td>Q325</td><td>Q425</td><td>Q126</td><td>Q226</td></tr><tr><td colspan="19">Analog</td></tr><tr><td>Revenue ($M)</td><td>$ 3,816</td><td>$ 3,992</td><td>$ 3,993</td><td>$ 3,558</td><td>$ 3,289</td><td>$ 3,278</td><td>$ 3,353</td><td>$ 3,120</td><td>$ 2,836</td><td>$ 2,928</td><td>$ 3,223</td><td>$ 3,174</td><td>$ 3,210</td><td>$ 3,452</td><td>$ 3,729</td><td>$ 3,615</td><td>$ 3,924</td><td>$ 4,365</td></tr><tr><td>QoQ Growth</td><td>2%</td><td>5%</td><td>0%</td><td>(11%)</td><td>(8%)</td><td>(0%)</td><td>2%</td><td>(7%)</td><td>(9%)</td><td>3%</td><td>10%</td><td>(2%)</td><td>1%</td><td>8%</td><td>8%</td><td>(3%)</td><td>9%</td><td>11%</td></tr><tr><td>YoY Growth</td><td>16%</td><td>15%</td><td>13%</td><td>(5%)</td><td>(14%)</td><td>(18%)</td><td>(16%)</td><td>(12%)</td><td>(14%)</td><td>(11%)</td><td>(4%)</td><td>2%</td><td>13%</td><td>18%</td><td>16%</td><td>14%</td><td>22%</td><td>26%</td></tr><tr><td>Operating Profit ($M)</td><td>$ 2,150</td><td>$ 2,226</td><td>$ 2,185</td><td>$ 1,798</td><td>$ 1,574</td><td>$ 1,463</td><td>$ 1,504</td><td>$ 1,280</td><td>$ 1,008</td><td>$ 1,047</td><td>$ 1,316</td><td>$ 1,237</td><td>$ 1,206</td><td>$ 1,325</td><td>$ 1,486</td><td>$ 1,395</td><td>$ 1,638</td><td>$ 1,992</td></tr><tr><td>Operating Margin</td><td>56.3%</td><td>55.8%</td><td>54.7%</td><td>50.5%</td><td>47.9%</td><td>44.6%</td><td>44.9%</td><td>41.0%</td><td>35.5%</td><td>35.8%</td><td>40.8%</td

[中间内容因长度限制已省略]

e in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of Societe

## Generale.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
