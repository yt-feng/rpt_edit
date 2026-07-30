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
Global Luxury Goods
Hermes International

Rating
Outperform

Price Target

RMS.FP

2,150.00 EUR

![](images/1e9b8ad7a3c68fca5d0d25f15eae33ef69391d4c7078a54c8b2c27ce90f1471a.jpg)

![](images/549552d5244d280767c07bc5dbde02836c7f7571499c3f9bf00dcf92d3ab34a2.jpg)

![](images/120def4a8e3cf5a442dad5b1aa3e4e14d3a468feccfb018b90e5a1ba6d7cdf94.jpg)

![](images/4ac20a0a263d7f8e05d2d2bee52008535c9b1574ea609e06bc903371e1e65e8b.jpg)

Luca Solca
+41 582 723 126
luca.solca@bernsteinsg.com

Maria Meita
+44 20 7170 0540
maria.meita@bernsteinsg.com

Eric Chen, CFA
+852 2123 2628
eric.chen@bernsteinsg.com

Yi-Peng Khoo, CFA
+44 20 7676 6822
yi-peng.khoo@bernsteinsg.com

# Hermès: Highlights from the 1H26 conference call

Hermès reported 1H26 results yesterday. This report contains key points from its investor conference call. Results Quick Take: Hermès: 1H26 organic sales in line; EBIT 2% above

Management's priority remains cultivating Hermès' brand equity. Investors fret that this will come at the expense of the DD growth the market has come to expect - a difficult trade-off for a company trading at $>30\mathrm{x}$ P/E (see Hermès: Valuations already discount a 'Ferrari reset'). These concerns have found a lightning rod in management's commentary on the leather goods growth algorithm: a clarification that $+6\%$ growth refers to production hours, not volumes per se, has been interpreted as a step-down in guidance. Additional commentary that LFL pricing will be lower in FY27E than FY26E did not help, leading to a significant post-earnings share price reaction.

Hand-wringing around price and volumes leaves mix opportunities underappreciated (see Hermès: Stretching upwards). Hermès could still pull levers on marketing, category and product innovation. High jewellery, haute couture, and bigger flagship stores all offer opportunities for Hermès to expand non-leather categories upwards in the coming years. Management too seems open to the idea that they could stretch upwards in leather goods. Indeed, expanding mix would absorb production growth slated for the rest of the decade (a positive for investors worried about overcapacity) while adding to the leather goods growth algorithm (a positive for those worried about long-term growth).

## Investment Implications

Hermès points to a sequential acceleration in top-line growth in 2H26E. All regions are either stable or accelerating sequentially. The leather goods growth algorithm for FY26E (of +5-6% pricing and +6% volumes) has been effectively confirmed. Sell-through in 1H26A has been strong, particularly in RTW and supported by a strong collection in Silks. We would expect supply to naturally increase as we approach the key EOY holiday season. Going forward, markets have also learnt to take company commentary in the lead up to earnings at face-value. We also note that net cash has been above €12bn since FY25, which makes extraordinary dividends more likely. We update our model by bringing down FY26E OSG up by -25bps to 7.7% (+33bps above consensus), driven by lower than expected Leather OSG in 2Q26, and weakness in Perfumes. We continue to model +11% for Leather for FY26E. This is offset by higher margin, given the beat in 1H26, continued growth, and FX headwinds

<table><tr><td>Close Date</td><td>28 Jul 2026</td></tr><tr><td>RMS.FP Close Price (EUR)</td><td>1,695.50</td></tr><tr><td>Price Target (EUR)</td><td>2,150.00</td></tr><tr><td>Upside/(Downside)</td><td>27%</td></tr><tr><td>52-Week Range</td><td>2,417.00/1,491.50</td></tr><tr><td>EDME</td><td>1,606.72</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>1.2%</td></tr><tr><td>Market Cap (EUR) (M)</td><td>157,932</td></tr><tr><td>EV (EUR) (M)</td><td>147,909</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(29.5)</td><td>(7.4)</td><td>(26.2)</td><td>(37.1)</td></tr><tr><td>EDME (%)</td><td>9.1</td><td>1.3</td><td>6.5</td><td>17.8</td></tr><tr><td>Relative (%)</td><td>(38.6)</td><td>(8.7)</td><td>(32.7)</td><td>(54.9)</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/6cf6febeb7e6cc0f1e6b1859c9e29407eb6617306d2cd7b8386c773cb7ac9a20.jpg)

<table><tr><td colspan="13">tapering off. Overall, this leads to our FY26E EPS being +2% higher (in line with consensus).</td></tr><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>RMS.FP (EUR)</td><td>43.12</td><td>44.66</td><td>52.67</td><td>Revenues (M)</td><td>16,002</td><td>16,940</td><td>18,726</td><td>--</td><td>Adjusted P/E (x)</td><td>39.3</td><td>38.0</td><td>32.2</td></tr><tr><td>OLD</td><td>--</td><td>43.89</td><td>52.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

## DETAILS

## BUSINESS UPDATE

## - Outlook:

\- 2026: management re-iterated the 11% growth for Leather Goods for FY26, with rough split of 6% volume and 5% pricing.

\- 2027: pricing is likely to be slightly lower than 2026. This shouldn't come as a surprise as Hermes have always used pricing to offset FX and production costs inflation, which appears to tapering off.

• Current trend by geography:

• No change in trends for Americas, Japan, Korea and Europe

\- France remains a question, but there's a sequential improvement in 2Q26

\- Middle East impact represented -1.5pts drag on growth in 2Q26 and the outlook remains uncertain. UAE retail stores have managed compensate the drop in traffic with higher tickets, but the situation is more complicated in Kuwait, Qatar, Bahrain where Hermes runs concession stores.

\- China: The market has been stabilising, but there has yet been material improvements. Management continues to see wealth creation - in the property and stock market - as key driver for market rebound. Overall sales appears to be stabilising in China for Hermes.

\- FX: Total FX impact on EBIT was EUR200m for 1H26, with a 50/50 split between negative hedging impact and FX translation. At the current spot rate, management flagged that the translation component is likely to be flat for the year

## COMMENTARY BY CATEGORY

## LEATHER GOODS (+10.2% CFX IN 2Q26 / +9.8% CFX IN H1 26)

\- Strong demand across all regions, with management stating that virtually all production was sold.

\- New model launches supported desirability, including Cliquetis, Kelly Hobo and Double Longe.

• Continued investment in production capacity:

• 25th leather workshop opened in Loupes (Gironde) in April-26.

• Charleville-Mézières scheduled for 2027.

• Colombelles scheduled for 2028.

• Les Andelys scheduled for 2030.

\- Approximately one new leather workshop per year remains the long-term ambition, with \~300 jobs created per site.

## RTW & ACCESSORIES (+3.6% CFX IN 2Q26 / +2.0% CFX IN H1 26)

\- Growth improved meaningfully in Q2, driven primarily by Ready-to-Wear.

• Major brand events included:

\- Women’s FW26 collection presentation.

\- Los Angeles second chapter presentation.

\- Men's fashion show in Tokyo.

\- High-end RTW remained strong while more volume-oriented categories such as footwear saw softer momentum due to weaker traffic in selected markets.

## SILK & TEXTILES (+12.2% CFX IN 2Q26 / +9.7% CFX IN H1 26)

\- Strong acceleration in Q2, driven by creativity, product innovation and strong customer reception.

\- Scarves and ties performed well across regions.

\- Silk was highlighted as one of the strongest-performing métiers in China.

## OTHER HERMÈS SECTORS – JEWELLERY AND THE HOME (+4.0% CFX IN 2Q26 / +5.4% CFX IN H1 26)

\- Jewellery remained a standout performer. Ninth High Jewellery collection (Into the Horsescape) received an enthusiastic reception globally.

\- Management indicated the July High Jewellery event significantly exceeded expectations.

• Home collections attracted approximately 36,000 visitors at the Milan Furniture Fair.

\- Continued investment in home and tableware production capacity (new Couzeix site scheduled in 2027).

## PERFUMES & BEAUTY (-9.5% CFX IN 2Q26 / -4.5% CFX IN H1 26)

\- Weakest-performing métier.

\- Beauty and makeup continued to perform well.

\- Perfume performance was stronger within Hermès stores than through external distribution channels.

\- Launches included:

\- Plein Air foundation.

\- Un Jardin sous la Mer.

\- Musc Pallida.

\- Management explicitly acknowledged that execution in perfume can improve and identified the category as an area requiring additional work.

## WATCHES (+4.4% CFX IN 2Q26 / +0.2% CFX IN H1 26)

\- Returned to growth during Q2 following a weaker start to the year. Supported by iconic collections, particularly the H08.

\- Continued manufacturing investment through Swiss capacity expansion, with the expansion of the Noirmont site scheduled for 2028.

## OTHER PRODUCTS (+1.9% CFX IN 2Q26 / +2.8% CFX IN H1 26)

\- Broadly stable growth.

\- Includes John Lobb, Saint-Louis, Puiforcat and manufacturing activities for third parties.

## COMMENTARY BY GEOGRAPHY

## FRANCE (+6.2% CFX IN 2Q26 / +1.8% CFX IN H1 26)

\- Sharp improvement in Q2 versus Q1.

• Growth driven by:

\- Local customers.

\- Recovery in tourism.

\- Paris was negatively impacted during parts of H1 by lower Middle Eastern tourism.

• Regional France, Paris and the French Riviera all improved in Q2.

\- Management remains somewhat more cautious on France for 2H26

## REST OF EUROPE (+8.3% CFX IN 2Q26 / +8.8% CFX IN H1 26)

• Continued strong momentum across the region.

• Particularly strong trends in: Italy, Northern Europe, Germany, Greece, United Kingdom.

\- New Bond Street Maison in London was highlighted as a major operational and communication milestone.

\- Berlin store reopened following renovation and expansion.

## JAPAN (+12.3% CFX IN 2Q26 / +11.0% CFX IN H1 26)

• Strong acceleration in Q2. Driven by loyal local customers and healthy traffic trends.

• Store investments included:

\- Osaka renovation and expansion.

\- New Nagoya store opening.

\- Japan remains an important example of Hermès' "local customer first" strategy.

## ASIA EX-JAPAN (+2.5% CFX IN 2Q26 / +2.4% CFX IN H1 26)

• Positive but subdued growth.

\- Korea delivered outstanding performance and was identified as the largest positive contributor.

\- Southeast Asia showed mixed trends, with Thailand slowing.

\- Greater China remained stable rather than materially improving.

\- Consumer confidence remains constrained by the property-market downturn and elevated savings rates, with management noting that aspirational customers remain under greater pressure than high-net-worth clients.

\- Chinese customers continue to purchase predominantly in their domestic market, while management highlighted jewellery, beauty and silk among the strongest-performing categories in China.

## AMERICAS (+13.7% CFX IN 2Q26 / +15.3% CFX IN H1 26)

\- Remained Hermès' strongest major region.

• Growth described as balanced across countries and métiers.

\- Management highlighted no material change in U.S. trends entering H2.

• Continued investment in distribution:

\- San Diego relocation.

\- Planned openings in Williamsburg, Manhattan, Chicago and Brooklyn.

\- Targeted hiring expected to continue to support growth.

## OTHER / MIDDLE EAST (-2.4% CFX IN 2Q26 / -4.2% CFX IN H1 26)

\- Region remained negatively impacted by geopolitical disruption.

\- Management estimated the Middle East reduced Group growth by roughly 150bps in both Q1 and Q2.

\- UAE remained resilient, supported by higher average transaction values.

\- Kuwait, Qatar and Bahrain faced a more difficult environment.

\- Middle Eastern customers travelled less and spent more domestically.

\- Management emphasized that customer appetite remained intact despite the temporary disruption.

## RETAIL FOOTPRINT AND FTES

\- Added more than 600 employees in H1, including over 300 in France. Total workforce reached 27,107 employees.

\- Network strategy remains focused on productivity and larger-format stores rather than store-count expansion. Current network comprises roughly 294 stores.

• Major H1 projects:

\- Beijing opening.

\- Nagoya opening.

\- Berlin renovation.

\- Osaka renovation.

• Hong Kong renovations.

\- New Bond Street Maison opening.

\- Planned H2 opening:

\- Chicago.

\- Brooklyn.

\- Rio de Janeiro.

\- Chengdu.

\- Management reiterated that future growth should come primarily from productivity, category expansion and client penetration rather than significant store-count growth.

## FINANCIAL PERFORMANCE (GM 71.1%; EBIT MARGIN 41.0% IN H1 26)

• Revenue reached €8.2bn, up +6.1% cFX in H1 26 and +6.7% cFX in 2Q26.

• Gross Margin reached +71.1%, up 40bps YoY.

\- Benefited from exceptional sell-through and disciplined inventory management.

\- Partly offset by approximately €100m of negative hedging impact.

\- Recurring Operating Income reached €3.4bn with a 41.0% EBIT margin.

\- Margin declined only 40bps despite approximately 100bps FX headwind.

• Currency impact on EBIT estimated at nearly €200m.

\- Management described the H1 EBIT margin as outstanding, but highlighted higher H2 investments, a larger negative hedging impact and a diminishing FX translation benefit.

EXHIBIT 1: Global Luxury Goods - OSG Breakdown

<table><tr><td rowspan="2">Company</td><td rowspan="2">Division</td><td colspan="2">Bernstein - New</td><td colspan="2">Bernstein - Old</td><td colspan="2">New vs. Old (bps)</td><td colspan="2">Consensus</td><td colspan="2">New vs. Consensus</td></tr><tr><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td></tr><tr><td rowspan="6">LVMH</td><td>Group</td><td>3.6%</td><td>6.2%</td><td>3.1%</td><td>6.2%</td><td>55</td><td>-3</td><td>2.7%</td><td>4.8%</td><td>99</td><td>133</td></tr><tr><td>Wines &amp; Spirits</td><td>3.5%</td><td>2.0%</td><td>0.6%</td><td>2.0%</td><td>284</td><td>0</td><td>3.6%</td><td>3.7%</td><td>-15</td><td>-166</td></tr><tr><td>Fashion &amp; Leather Goods</td><td>2.4%</td><td>7.0%</td><td>2.4%</td><td>7.0%</td><td>0</td><td>0</td><td>0.9%</td><td>4.7%</td><td>146</td><td>233</td></tr><tr><td>Perfumes &amp; Cosmetics</td><td>1.1%</td><td>5.0%</td><td>2.8%</td><td>5.0%</td><td>-174</td><td>0</td><td>0.5%</td><td>3.9%</td><td>57</td><td>107</td></tr><tr><td>Watches &amp; Jewelry</td><td>7.7%</td><td>5.0%</td><td>4.4%</td><td>5.0%</td><td>333</td><td>0</td><td>7.6%</td><td>6.7%</td><td>10</td><td>-171</td></tr><tr><td>Selective Retailing</td><td>5.2%</td><td>7.0%</td><td>4.8%</td><td>7.0%</td><td>47</td><td>0</td><td>4.4%</td><td>5.3%</td><td>80</td><td>168</td></tr><tr><td rowspan="8">Hermès</td><td>Group</td><td>7.4%</td><td>10.5%</td><td>7.7%</td><td>10.5%</td><td>-25</td><td>0</td><td>7.1%</td><td>8.4%</td><td>33</td><td>216</td></tr><tr><td>Leather Goods - Saddlery</td><td>11.1%</td><td>12.0%</td><td>11.3%</td><td>12.0%</td><td>-20</td><td>0</td><td>11.1%</td><td>10.3%</td><td>6</td><td>166</td></tr><tr><td>Ready-to-Wear &amp; Acc.</td><td>3.7%</td><td>10.0%</td><td>3.8%</td><td>10.0%</td><td>-10</td><td>0</td><td>3.4%</td><td>6.3%</td><td>33</td><td>368</td></tr><tr><td>Silk and Textiles</td><td>9.1%</td><td>8.0%</td><td>7.2%</td><td>8.0%</td><td>191</td><td>0</td><td>6.6%</td><td>6.4%</td><td>248</td><td>159</td></tr><tr><td>Other Hermès Sectors</td><td>7.0%</td><td>10.0%</td><td>7.5%</td><td>10.0%</td><td>-50</td><td>0</td><td>6.3%</td><td>8.0%</td><td>65</td><td>199</td></tr><tr><td>Perfumes</td><td>-4.9%</td><td>8.0%</td><td>2.3%</td><td>8.0%</td><td>-723</td><td>0</td><td>-0.1%</td><td>5.3%</td><td>-482</td><td>270<

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
