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
08 Jun 2026 11:30:00 ET | 24 pages

## Global Gold

Marking-to-market gold exposure, steady FCF offsets near-term headwinds

## CITI'S TAKE

Consolidation in gold prices from the peak in Jan'26 has led up to 25% correction for gold stocks. Near-term earnings risk from lower gold prices are somewhat offset by the steady operational performance delivered for Q1'26 by both gold stocks in our coverage, which should be supportive of continued steady cash generation in 2026. Despite near term caution, Citi house views are constructive for gold price in outer years with expectations for \$5,000/oz in 2027 vs spot at c\$4,350. We have updated our estimates with latest gold prices leading to net upgrades to our EBITDA estimates. However, we have lowered the target multiples used to set TPs for both the stock, but still maintain our views that elevated earnings and cash generation should help stocks to re-rate vs their long-term averages. We maintain Buy ratings on both the stocks.

Cash generation likely to remain solid for ANG/GFI — Gold stocks have strong balance sheets, and we expect significantly higher excess cash over the next 12 months. Potential volume growth is likely to further help enhance cash generation with peak capex likely already behind. ANG/GFI have 81%/85% R2 with gold price, while Citi house views on gold prices are constructive for \$5,000/oz in 2027. ANG is currently trading at a 1 YF EV/EBITDA of 4.7x which is in-line with its own long-term average but lower than global gold peers, while FCF yield at 10.5% is attractive. GFI currently trades at 1 YF EV/EBITDA of 3.6x, lower than its own long-term and global peers, while FCF yield at 12% remain attractive. We have now revised our target multiple for the stocks to 7x EBITDA (vs 8x earlier) for ANG and 6x (vs 8x earlier) for GFI, reflecting our expectations for continued re-rating ahead of their long-term averages. We maintain our Buy ratings on the stocks. We now update the TPs for ANG at \$130/ZAR2,100, slightly up from \$120/ZAR1,950 earlier. The TPs for GFI have however, come down to \$58/ZAR950 vs \$65/ZAR1,100 earlier.

Operational performance is likely to be key in near term amid gold price volatility — among the gold equities in our coverage, we would look for production ramp-up at Obuasi mine and progress at Nevada project as key catalysts for AngloGold. Moreover, for Gold Fields we watch for progress of Windfall project in addition to the shared risk from regulatory uncertainty in Ghana for both stocks. Cost inflation pressure from higher energy prices is a macro risk, that could play out should the oil prices remains higher for longer.

Earnings changes — We update our models by incorporating latest commodity prices with positive revisions by 8%/25%/13% for 2026/2027/2028 respectively, together with marking to market our assumptions for forex major operational drivers. The net result is +1%/+24%/+9% changes to our 2026/2027/2028 EBITDA estimates for ANG and +2%/+24%/+6% changes to our FY26/27/28 EBITDA estimates for GFI (Details inside).

Ephrem Ravi $^{AC}$

+44-20-7986-2462

ephrem.ravi@citi.com

Shashi Shekhar, CFA

+91-22-4277-5028

shashi.shekhar@citi.com

Krishan M Agarwal

+44-020-7986-4092

krishan.agarwal@citi.com

Data Summary

<table><tr><td rowspan="2" colspan="14"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td rowspan="2" colspan="2">EPS</td><td rowspan="2" colspan="2">EPS</td></tr><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td colspan="3"></td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>ESPR (%)</td><td>Div Yld (%)</td><td>ETR (%)</td><td>Last Rpt Yr</td><td>Old</td><td>New</td><td>Old</td></tr><tr><td>Anglogold</td><td>AU</td><td>US$</td><td>84.12</td><td>42,532</td><td>05 Jun 16:00</td><td>1</td><td>nc</td><td>-</td><td>120.00</td><td>130.00</td><td>54.5</td><td>5.6</td><td>60.1</td><td>Dec-25</td><td>9.34</td><td>9.57</td><td>8.60</td></tr><tr><td>Ashanti PLC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AngloGold</td><td>ANGJJ</td><td>R</td><td>1,365.88</td><td>690,602</td><td>08 Jun 13:19</td><td>1</td><td>nc</td><td>-</td><td>1,950.00</td><td>2,100.00</td><td>53.7</td><td>5.1</td><td>58.9</td><td>Dec-25</td><td>9.34</td><td>9.57</td><td>8.60</td></tr><tr><td>Ashanti plc</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gold fields</td><td>GFIJJ</td><td>R</td><td>589.09</td><td>527,250</td><td>08 Jun 13:19</td><td>1</td><td>nc</td><td>-</td><td>1,100.00</td><td>950.00</td><td>61.3</td><td>5.1</td><td>66.4</td><td>Dec-25</td><td>5.94</td><td>6.34</td><td>5.13</td></tr><tr><td>Gold Fields</td><td>GFI Ltd</td><td>US$</td><td>36.62</td><td>32,754</td><td>05 Jun 16:00</td><td>1</td><td>nc</td><td>-</td><td>65.00</td><td>58.00</td><td>58.4</td><td>5.5</td><td>63.8</td><td>Dec-25</td><td>5.94</td><td>6.34</td><td>5.13</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="12">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="12">^Catalyst Watch</td></tr></table>

## Anglogold Ashanti PLC (AU.N)

Buy | TP US\$130.00 from US\$120.00 | Price US\$84.12 (05 Jun 26 16:00)

Recommendation (s) — We maintain our Buy rating on AngloGold. The balance sheet is very strong with a net cash position of c\$0.9bn by 1Q'26 end, and we expect substantial excess cash over the next 12 months. This excess cash generates further growth (Nevada projects) and cash returns optionality. Assets are well-capitalized and will likely reap maximum benefit from higher gold prices - AU/ANG have an 81% R2 with gold price and Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at c\$4,350. On our estimates company is currently trading at a 1 yr fwd EV/EBITDA multiple of 4.7x (in line with LT avg, but lower vs global peers) and FCF yield of c10.5% (mining stocks have historically traded on an average of 8% FCF yield).

What to look out for — (i) production ramp-up at Obuasi mine; (ii) progress at Nevada project; (iii) regulatory risks in Ghana, and (iv) cost inflation pressures.

Maintain Buy with TP at \$130 — We update our model by incorporating latest commodity prices (link, resulting in +8%/+25%/+13% changes to gold prices estimates for CY26/27/28e), marking to market fx and revisiting our operational assumptions. The net result is +1%/+24%/+9% changes to our FY26/27/28 EBITDA estimates. Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at c\$4,350 leading to upwards revision for our EBITDA forecasts. We lower our valuation multiple for the company, but still maintain at higher to their respective long-term averages. Valuation multiple used for ANG is now at 7x EBITDA (vs 8x earlier), ahead of its long-term average at 4.7x. We raise our TP to \$130 (from \$120) driven by higher gold price estimates, partially offset by lower multiple. At our TP AU offers c60% ETR and we maintain Buy rating on the stock.

## Anglogold Ashanti PLC (ANGJ.J)

Buy | TP R2,100.00 from R1,950.00 | Price R1,365.88 (08 Jun 26 13:19)

Recommendation (s) — We maintain our Buy rating on AngloGold. The balance sheet is very strong with a net cash position of c\$0.9bn by 1Q'26 end, and we expect substantial excess cash over the next 12 months. This excess cash generates further growth (Nevada projects) and cash returns optionality. Assets are well-capitalized and will likely reap maximum benefit from higher gold prices - AU/ANG have an 81% R2 with gold price and Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at c\$4,350. On our estimates company is currently trading at a 1 yr fwd EV/EBITDA multiple of 4.7x (in line with LT avg, but lower vs global peers) and FCF yield of c10.5% (mining stocks have historically traded on an average of 8% FCF yield).

What to look out for — (i) production ramp-up at Obuasi mine; (ii) progress at Nevada project; (iii) regulatory risks in Ghana, and (iv) cost inflation pressures.

Maintain Buy with TP at ZAR2100 — We update our model by incorporating latest commodity prices (link, resulting in +8%/+25%/+13% changes to gold prices estimates for CY26/27/28e), marking to market fx and revisiting our operational assumptions. The net result is +1%/+24%/+9% changes to our FY26/27/28 EBITDA estimates. Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at c\$4,350 leading to upwards revision for our EBITDA forecasts. We lower our valuation multiple for the company, but still maintain at higher to their respective long-term averages. Valuation multiple used for ANG is now at 7x

EBITDA (vs 8x earlier), ahead of its long-term average at 4.7x. We raise our TP to ZAR2100 (from ZAR1950) driven by higher gold price estimates, partially offset by lower multiple. At our TP ANG offers c60% ETR and we maintain Buy rating on the stock.

## Gold Fields Ltd (GFIJ.J)

Buy | TP R950.00 from R1,100.00 | Price R589.09 (08 Jun 26 13:19)

Recommendation (s) — We maintain our Buy rating on Gold Fields. The balance sheet is strong and the company is likely to end FY26 at a net cash position of c\$0.7bn on our estimates. This excess cash generates further growth (Windfall project) and cash returns optionality. Assets are well-capitalized and will likely reap maximum benefit from higher gold prices - GFI has an 85% R2 with gold price and Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at c\$4,350. On our estimates company is currently trading at a 1 yr fwd EV/EBITDA multiple of 3.6x (lower vs LT avg and global peers) and FCF yield of c12% (mining stocks have historically traded on an average of 8% FCF yield).

What to look out for — (i) progress of Windfall project, (ii) regulatory risks in Ghana, and (iii) cost inflation pressures.

Maintain Buy with TP reduced to ZAR950 — We update our model by incorporating latest commodity prices (link, resulting in +8%/+25%/+13% changes to gold prices estimates for CY26/27/28e), marking to market fx and revisiting our operational assumptions. The net result is +2%/+24%/+6% changes to our FY26/27/28 EBITDA estimates. Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at \$4,350 leading to upwards revision for our EBITDA forecasts. We lower our valuation multiple for the company (reflecting short term cautious view on gold), but still maintain it at higher to their respective long-term averages. Valuation multiple used for GFI is now at 6x EBITDA (vs 8x earlier), ahead of its long-term average at 5.1x. We reduce our TP to ZAR950 (from ZAR1100) driven by higher gold price estimates, partially offset by lower multiple and higher operating cost estimates. At our TP GFI offers c66% ETR and we maintain Buy rating on the stock.

## Gold Fields Ltd (GFI.N)

Buy | TP US\$58.00 from US\$65.00 | Price US\$36.62 (05 Jun 26 16:00)

Recommendation (s) — We maintain our Buy rating on Gold Fields. The balance sheet is strong and the company is likely to end FY26 at a net cash position of c\$0.7bn on our estimates. This excess cash generates further growth (Windfall project) and cash returns optionality. Assets are well-capitalized and will likely reap maximum benefit from higher gold prices - GFI has an 85% R2 with gold price and Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at c\$4,350. On our estimates company is currently trading at a 1 yr fwd EV/EBITDA multiple of 3.6x (lower vs LT avg and global peers) and FCF yield of c12% (mining stocks have historically traded on an average of 8% FCF yield).

What to look out for — (i) progress of Windfall project, (ii) regulatory risks in Ghana, and (iii) cost inflation pressures.

Maintain Buy with TP reduced to US\$58 — We update our model by incorporating latest commodity prices (link, resulting in +8%/+25%/+13% changes to gold prices estimates for CY26/27/28e), marking to market fx and revisiting our operational assumptions. The net result is +2%/+24%/+6% changes to our FY26/27/28 EBITDA estimates. Citi house views on gold prices are bullish in outer years, \$5,000/oz for 2027 vs spot at \$4,350 leading to upwards revision for our EBITDA forecasts. We lower our valuation multiple for the company, but still maintain at higher to their respective long-term averages. Valuation multiple used for GFI is now at 6x EBITDA (vs 8x earlier, (reflecting short term cautious view on gold)) ahead of its long-term average at 5.1x. We reduce our TP to US\$58 (from US\$65) driven by higher gold price estimates, partially offset by lower multiple and higher operating cost estimates. At our TP GFI offers c64% ETR and we maintain Buy rating on the stock.

## Bull/Bear: Anglogold Ashanti PLC (AU.N)

![](images/ba1d85e8c79ca988932fe9a6cbe1a14f4aa25db68bd4acbb7abfcc8805b8d8b1.jpg)

<details>
<summary>line chart</summary>

| Date       | Price     |
| ---------- | --------- |
| Jun 26     | US$84.12  |
| Jun 27     | US$174.00 |
| Jun 27     | US$130.00 |
| Jun 27     | US$76.00  |
</details>

Spread 117pp  
Current Price and expected returns (upside/downside) as of 05 Jun 2026

## BULL Assumptions

![](images/5b4cea950ef1b42ab51b40aa9c66a85c613f45ca810f3726f6d8a0d6336b3477.jpg)

• +10% higher LT commodity prices vs CitiE  
- Arthur project

![](images/70a17d3ec248fcd4855cb47cc6ad2309299aa48e6b3e67aab82abf53dbd022d5.jpg)

## BASE Assumptions

• Citi's base case commodity price and fx estimates play out

## BEAR Assumptions

![](images/e9585121abfbb47d5386d41c71ef665e0301b3d8bbbb8dd58f0f327989ec06fb.jpg)

- -10% lower LT commodity prices vs CitiE  
• LT cost escalation +10% higher vs our estimates  
• LT capex escalation +10% higher vs our estimates

## Bull/Bear: Anglogold Ashanti PLC (ANGJ.J)

![](images/fad199e4566a8ab72a80a5cd577a316147d3b937d8519f8c8d6e843eca2060d1.jpg)

<details>
<summary>line chart</summary>

| Date       | Price     |
| ---------- | --------- |
| 08 Jun 26  | 1,365.88  |
| Jun 27     | 1,225.00  |
| Jun 27     | 2,800.00  |
| Jun 27     | 2,100.00  |
| Jun 27     | 1,225.00  |
</details>

Spread 115pp  
Current Price and expected returns (upside/downside) as of 08 Jun 2026

## BULL Assumptions

![](images/5d3c00fd661eb7d93f6f24c853bbeaa9aeffcea0028203cf6d91d510af439bd6.jpg)

• +10% higher LT commodity prices vs CitiE  
- Arthur project

![](images/4e0abb04ba4442753c54ef8608d60854b17e96a293e732f6f8fddd15908f76fc.jpg)

## BASE Assumptions

• Citi's base case commodity price and fx estimates play out

## BEAR Assumptions

![](images/55a0cc451e28b9b0588b7e569e4339fc2526a3e659e41172a9d56927a3c3f2df.jpg)

- -10% lower LT commodity prices vs CitiE  
• LT cost escalation +10% higher vs our estimates  
• LT capex escalation +10% higher vs our estimates

## Bull/Bear: Gold Fields Ltd (GFIJ.J)

R 1,210.00

▲105% Upside

R 950.00

▲ 61% Upside

R 570.00

▼3.2% Downside

![](images/1d5bb3fd64d873a291983ebaf97f0578485ff0eebdb92644501173ff0c5d2e1b.jpg)

<details>
<summary>line chart</summary>

| Date       | Value   |
| ---------- | ------- |
| 08 Jun 26  | 589.09  |
| Jun 27     | 1,210.00 |
| Jun 27     | 950.00  |
| Jun 27     | 570.00  |
</details>

Spread 109pp  
Current Price and expected returns (upside/downside) as of 08 Jun 2026

![](i

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
