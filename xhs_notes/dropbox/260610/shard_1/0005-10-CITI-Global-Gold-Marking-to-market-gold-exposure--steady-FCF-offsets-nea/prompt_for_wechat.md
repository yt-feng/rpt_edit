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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

![](images/bc9e87392ede9780b6143f04e1448905edfbde95ec786e63cd533ac8c6b6afef.jpg)

## BULL Assumptions

• +10% LT commodity prices

![](images/9e0cc5c6195e73037bbc0001166687b033fa76d7b8d197e8ed902aeea13c2c60.jpg)

## BASE Assumptions

• Citi's base case commodity price and fx estimates play out

## BEAR Assumptions

![](images/94bff7cf3d66eb67cbb9ec9abae9df87063057769bbd023ca071fb071dffd592.jpg)

-10% LT commodity prices  
• LT cost escalation +10% higher vs our estimates  
• LT capex escalation +10% higher vs our estimates

## Bull/Bear: Gold Fields Ltd (GFI.N)

![](images/ca7b07d398c9f8d8419ff0ab7bcfc709ccaa6b5ca9e84c1c3c6b7b6fee7010a2.jpg)

<details>
<summary>line chart</summary>

| Date       | Price (US$) |
| ---------- | ----------- |
| Jun 26     | 36.62       |
| Jun 27     | 74.00       |
| Jun 27     | 58.00       |
| Jun 27     | 35.00       |
</details>

Spread 106pp  
Current Price and expected returns (upside/downside) as of 05 Jun 2026

![](images/dc37bd76e96c0383c853c83cb934133e852b8d88f6ec7ea0975414fba96acedf.jpg)

## BULL Assumptions

• +10% LT commodity prices

![](images/1317fa9ae164a2f92f020118eb76c2d25505cfeabe1ed48bc7ff63ef71211a7b.jpg)

## BASE Assumptions

• Citi's base case commodity price and fx estimates play out

## BEAR Assumptions

![](images/4987439497da990a0206a2644f619460aa5a5f9e7bbb506a3f6cc770a49bfe34.jpg)

-10% LT commodity prices  
• LT cost escalation +10% higher vs our estimates  
• LT capex escalation +10% higher vs our estimates

## Anglogold Ashanti PLC

## Company description

AngloGold is the 6th-largest gold producer in the world (and the 4th-largest listed) with a diversified asset base. Currently, it owns 11 producing assets located across the globe and is in the process of developing the North Bullfrog project in Nevada, US. In 2024, c.60% of production came from Africa, c.20% from Australia, and c.20% from Americas. In 2025, the company is expected to produce c3.1mn oz of gold.

## Investment strategy

We rate AngloGold as Buy. The company accounts for only 2% of gold production (top-10 gold producers around 28% of gold production on our calculations) and appears well-placed to benefit from the scarcity of large listed gold miners in a rising gold price environment. With increased production from Sukari and longer-term expansion in Nevada starting with North Bullfrog as a platform for growth in the Beatty district), the AISC profile should improve, and the jurisdictional risk (c.65% of production and c.75% of NAV currently from Africa) should reduce. There is also organic growth potential led by the ramp-ups of the Obuasi mine and North Bullfrog project.

## Valuation

Our target price of \$130/share for AngloGold is based on the average of a DCF-based NPV valuation and an EV/EBITDA valuation. Our DCF analysis uses a Weighted Average Cost of Capital (WACC) of 5% for gold minin

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
