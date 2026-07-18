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
# Zhongji Innolight Co Ltd | Asia Pacific

# Updating estimates

We raise our Innolight financial forecasts to reflect our positive view on industry demand.

## Key Takeaways

We raised our 2026e and 2027e earnings estimates 33% and 180%.

Scale-out, scale-up, and scale-across to drive stronger-than-expected industry demand.

NPO and OCS are potential new growth drivers beyond 2026-2028.

Upbeat 1Q26 results: Driven by robust customer investment in AI and computing infrastructure, Innolight achieved 192% revenue growth, 39% above our forecasts. Its gross margin is 46.1%, 0.5ppt ahead of our forecasts. As a result, its net profit was Rmb5.7bn, 31% ahead of our original forecasts.

AI transceiver demand is stronger than expected: Thanks to the wider application of scale-out, scale-up and scale-across architectures, we expect accelerating adoption of AI transceivers. We therefore raise our AI transceiver industry shipment forecast from 53mn units to 73mn units for 2026, 71mn units to 141mn units for 2027, and 80mn units to 150mn units for 2028. The significant upward revisions in 2027 and 2028 stem mainly from a more positive view on 1.6T demand. Given these revisions, we now forecast the AI transceiver industry TAM to grow from US\$18bn in 2025 to US\$102bn in 2028, expanding >4x within three years.

Global leader in AI transceivers: Innolight is a first mover in 800G and 1.6T commercialization and, given its expertise, we expect it will remain a pioneer in the next node (3.2T). The company's long-term partnerships with global CSPs, close joint R&D, and differentiated new product introductions (NPI) support faster yield improvements and cost reductions, making Innolight more competitive than peers on key metrics such as time-to-market, time-to-volume and time-to-cost.

Potential new growth drivers beyond 2027: We expect accelerated new technology innovation, such as optical circuit switching (OCS) and near-packaged optics (NPO), to become technological breakthroughs in the coming years. We believe Innolight is well positioned to capture such growth opportunities, and these new technologies could support the company's growth beyond 2027. The success of NPO could also help alleviate concerns about co-packaged optics (CPO) disruption.

Raise earnings forecasts to reflect 2026-28 growth opportunity: Innolight's AI transceiver momentum is supported by industry growth and competitive advantages in time-to-market, time-to-volume and time-to-cost, underpinning strong top-line performance. From 2027 onward, 3.2T, NPO and OCS could add new growth. As a result, we raise our 2026 and 2027 net profit forecasts by a respective 33% and 180%, leading to 53% revenue and 66% earnings CAGRs, 2026–28.

MS ASIA LIMITED+

Andy Meng, CFA

Equity Analyst
Andy.Meng@morganstanley.com

+852 2239-7689

Betty Chen

Research Associate
Betty.H.Chen@morganstanley.com

+852 2239-7213

![](images/8d028cad44f5d94d8c22fcf501ab1aedc19b9318137d1ec562d9459b3f670832.jpg)

Asia Summer School 2026

## Zhongji Innolight Co Ltd (300308.SZ, 300308 CS)

<table><tr><td>Stock Rating</td><td>++</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>++</td></tr><tr><td>Up/downside to price target (%)</td><td>-</td></tr><tr><td>Shr price, close (Jul 17, 2026)</td><td>Rmb979.46</td></tr><tr><td>52-Week Range</td><td>Rmb1,416.88-169.17</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>1,111</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb1,088,296</td></tr><tr><td>EV, curr (mn)</td><td>Rmb1,077,907</td></tr><tr><td>Avg daily trading value (mn)</td><td>Rmb23,107</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>9.72</td><td>29.91</td><td>63.03</td><td>82.90</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EPS (Rmb)§</td><td>9.72</td><td>29.71</td><td>52.76</td><td>76.54</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>38,240</td><td>107,904</td><td>196,339</td><td>251,279</td></tr><tr><td>EBITDA (Rmb mn)</td><td>14,244</td><td>44,903</td><td>86,934</td><td>113,205</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>10,797</td><td>33,232</td><td>70,032</td><td>92,107</td></tr><tr><td>P/E</td><td>62.8</td><td>32.7</td><td>15.5</td><td>11.8</td></tr><tr><td>P/BV</td><td>22.8</td><td>11.9</td><td>6.9</td><td>4.6</td></tr><tr><td>RNOA (%)</td><td>73.7</td><td>189.3</td><td>178.9</td><td>142.3</td></tr><tr><td>ROE (%)</td><td>56.4</td><td>111.6</td><td>76.6</td><td>58.8</td></tr><tr><td>EV/EBITDA</td><td>46.9</td><td>23.1</td><td>11.5</td><td>8.2</td></tr><tr><td>Div yld (%)</td><td>0.5</td><td>0.4</td><td>0.9</td><td>1.2</td></tr><tr><td>FCF yld ratio (%)**</td><td>1.1</td><td>1.1</td><td>4.0</td><td>7.0</td></tr><tr><td>Leverage (EOP) (%)</td><td>(38.5)</td><td>(59.6)</td><td>(61.7)</td><td>(69.2)</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
§ = Consensus data is provided by Refinitiv Estimates
\*\* = Based on consensus methodology
e = MS estimates
++ = Stock Rating, Price Target or Estimates are not available or have been removed due to applicable law and/or MS policy.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## 1Q26 Earnings Review

1Q26 earnings beat: Driven by robust customer investment in AI and computing infrastructure, Innolight reported strong 1Q26 results. 1Q26 revenue was up 192% YoY and 47% QoQ, 39% above our forecasts. Its gross margin is 46.1%, up 9.4ppt YoY and 1.6ppt QoQ, 0.5ppt ahead of our forecasts. As a result, its net profit was Rmb5.7bn, up 262% YoY and 56% QoQ, 31% ahead of our original forecasts.

Exhibit 1: Innolight has reported upbeat 1Q26 results

<table><tr><td>Rmb mn</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>MSE</td></tr><tr><td>Revenue</td><td>4,843</td><td>5,956</td><td>6,514</td><td>6,550</td><td>6,674</td><td>8,115</td><td>10,216</td><td>13,235</td><td>19,496</td><td>14,016</td></tr><tr><td>Gross profit</td><td>1,586</td><td>1,991</td><td>2,191</td><td>2,298</td><td>2,449</td><td>3,367</td><td>4,371</td><td>5,887</td><td>8,980</td><td>6,389</td></tr><tr><td>Operating expenses</td><td>-467</td><td>-475</td><td>-440</td><td>-788</td><td>-499</td><td>-523</td><td>-652</td><td>-1,006</td><td>-1,227</td><td>-911</td></tr><tr><td>Opearing income</td><td>1,119</td><td>1,517</td><td>1,751</td><td>1,510</td><td>1,950</td><td>2,844</td><td>3,719</td><td>4,882</td><td>7,753</td><td>5,478</td></tr><tr><td>Non-op</td><td>56</td><td>38</td><td>-68</td><td>130</td><td>40</td><td>48</td><td>240</td><td>-122</td><td>-217</td><td>25</td></tr><tr><td>Tax&amp; Minorities</td><td>-166</td><td>-205</td><td>-289</td><td>-221</td><td>-407</td><td>-479</td><td>-823</td><td>-1,094</td><td>-1,801</td><td>-1,126</td></tr><tr><td>Net income</td><td>1,009</td><td>1,349</td><td>1,394</td><td>1,419</td><td>1,583</td><td>2,412</td><td>3,137</td><td>3,665</td><td>5,735</td><td>4,377</td></tr></table>

<table><tr><td>YoY%</td><td>QoQ%</td><td>Diff. vs MSE</td></tr><tr><td>192%</td><td>47%</td><td>39%</td></tr><tr><td>267%</td><td>53%</td><td>41%</td></tr><tr><td>146%</td><td>22%</td><td>35%</td></tr><tr><td>298%</td><td>59%</td><td>42%</td></tr><tr><td>-646%</td><td>77%</td><td>-967%</td></tr><tr><td>343%</td><td>65%</td><td>60%</td></tr><tr><td>262%</td><td>56%</td><td>31%</td></tr></table>

<table><tr><td colspan="11">Key metrics %</td></tr><tr><td>Gross margin</td><td>32.8%</td><td>33.4%</td><td>33.6%</td><td>35.1%</td><td>36.7%</td><td>41.5%</td><td>42.8%</td><td>44.5%</td><td>46.1%</td><td>45.6%</td></tr><tr><td>Opex</td><td>9.6%</td><td>8.0%</td><td>6.8%</td><td>12.0%</td><td>7.5%</td><td>6.4%</td><td>6.4%</td><td>7.6%</td><td>6.3%</td><td>6.5%</td></tr><tr><td>Net margin</td><td>20.8%</td><td>22.7%</td><td>21.4%</td><td>21.7%</td><td>23.7%</td><td>29.7%</td><td>30.7%</td><td>27.7%</td><td>29.4%</td><td>31.2%</td></tr></table>

Source: Company data, MS estimates

<table><tr><td>9.4%</td><td>1.6%</td><td>0.5%</td></tr><tr><td>-1.2%</td><td>-1.3%</td><td>-0.2%</td></tr><tr><td>5.7%</td><td>1.7%</td><td>-1.8%</td></tr></table>

## Earnings Estimate Revision Summary

Raise Innolight's forecasts: Reflecting the solid 1Q26 results and more positive industry outlook, we raise our Innolight revenue forecasts 36%-138% in 2026-2027, mainly driven by 38%-98% increases in our high-end transceiver industry volume forecasts in the same period. We also raise our gross margin forecasts by 0.9-3.1ppt to reflect improved product mix from higher contribution from high-end products. As a result, we raise Innolight's net profit forecasts for 2026-27e by 33%-180%. We also introduce our 2028 estimates.

Key risks to our earnings forecasts include: 1) CPO disruption risk (timing and magnitude), 2) competitive intensity and customer diversification, and 3) geopolitics, tariffs, and supply chain volatility.

Exhibit 2: Earnings revisions: New vs. Old

<table><tr><td colspan="4">New</td><td colspan="3">Old</td><td colspan="3">New vs Old</td></tr><tr><td>Rmb mn</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2028E</td><td>2027E</td><td>2028E</td><td>2028E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Sales</td><td>107,904</td><td>196,339</td><td>251,279</td><td>79,361</td><td>82,523</td><td>NA</td><td>36%</td><td>138%</td><td>NA</td></tr><tr><td>% Growth YoY</td><td>182%</td><td>82%</td><td>28%</td><td>101%</td><td>4%</td><td>NA</td><td></td><td></td><td>NA</td></tr><tr><td>Gross profit</td><td>50,178</td><td>94,409</td><td>122,220</td><td>36,176</td><td>37,116</td><td>NA</td><td>39%</td><td>154%</td><td>NA</td></tr><tr><td>% margin</td><td>46.5%</td><td>48.1%</td><td>48.6%</td><td>45.6%</td><td>45.0%</td><td>NA</td><td>0.9%</td><td>3.1%</td><td>NA</td></tr><tr><td>Net Profit</td><td>33,232</td><td>70,032</td><td>92,107</td><td>25,050</td><td>25,015</td><td>NA</td><td>33%</td><td>180%</td><td>NA</td></tr><tr><td>% Growth YoY</td><td>207.8%</td><td>110.7%</td><td>31.5%</td><td>129.3%</td><td>-0.1%</td><td>NA</td><td></td><td></td><td>NA</td></tr><tr><td>% margin</td><td>30.8%</td><td>35.7%</td><td>36.7%</td><td>31.6%</td><td>30.3%</td><td>NA</td><td>-1%</td><td>5%</td><td>NA</td></tr></table>

Source: Company data, MS estimates

## Innolight: Financial Summary

Exhibit 3: Innolight: Financial Summary

<table><tr><td>Income statements</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net sales</td><td>38,240</td><td>107,904</td><td>196,339</td><td>251,279</td></tr><tr><td>COGS</td><td>(22,166)</td><td>(57,726)</td><td>(101,931)</td><td>(129,059)</td></tr><tr><td>Gross profit</td><td>16,074</td><td>50,178</td><td>94,409</td><td>122,220</td></tr><tr><td>Selling expenses</td><td>(226)</td><td>(436)</td><td>(785)</td><td>(1,005)</td></tr><tr><td>ADM expenses</td><td>(761)</td><td>(2,265)</td><td>(3,150)</td><td>(3,632)</td></tr><tr><td>R&amp;D expenses</td><td>(1,615)</td><td>(3,202)</td><td>(4,596)</td><td>(5,624)</td></tr><tr><td>Operating Inc.</td><td>13,394</td><td>43,753</td><td>85,485</td><td>111,456</td></tr><tr><td>Finance cost</td><td>(183)</td><td>(1,001)</td><td>200</td><td>200</td></tr><tr><td>Pre-tax Income</td><td>13,600</td><td>42,786</td><td>85,685</td><td>111,656</td></tr><tr><td>Income Tax</td><td>(2,020)</td><td>(6,921)</td><td>(12,853)</td><td>(16,748)</td></tr><tr><td>Net income</td><td>10,797</td><td>33,232</td><td>70,032</td><td>92,107</td></tr><tr><td>EBITDA</td><td>14,244</td><td>44,903</td><td>86,934</td><td>113,205</td></tr></table>

<table><tr><td>Balance sheet</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash</td><td>10,987</td><td>54,049</td><td>96,126</td><td>164,598</td></tr><tr><td>Trade receivables</td><td>6,350</td><td>17,917</td><td>32,601</td><td>41,723</td></tr><tr><td>Inventories</td><td>12,681</td><td>33,024</td><td>58,314</td><td>73,834</td></tr><tr><td>Other current assets</td><td>1,067</td><td>1,067</td><td>1,067</td><td>1,067</td></tr><tr><td>Current Assets</td><td>31,084</td><td>106,057</td><td>188,108</td><td>281,222</td></tr><tr><td>Property, plant and equipment</td><td>8,503</td><td>10,353</td><td>11,903</td><td>13,153</td></tr><tr><td>Intangible assets</td><td>2,316</td><td>2,316</td><td>2,316</td><td>2,316</td></tr><tr><td>Other assets</td><td>3,386</td><td>3,386</td><td>3,386</td><td>3,386</td></tr><tr><td>Total Assets</td><td>45,289</td><td>122,112</td><td>205,713</td><td>300,078</td></tr><tr><td>Trade payables</td><td>7,800</td><td>20,315</td><td>35,871</td><td>45,418</td></tr><tr><td>Other payables</td><td>2,672</td><td>2,672</td><td>2,672</td><td>2,672</td></tr><tr><td>Bank loans - due within one year</td><td>1,086</td><td>1,086</td><td>1,086</td><td>1,086</td></tr><tr><td>Current Liabilities</td><td>11,558</td><td>24,073</td><td>39,629</td><td>49,176</td></tr><tr><td>Bank loans - due after one year</td><td>510</td><td>510</td><td>510</td><td>510</td></tr><tr><td>Other liabilities</td><td>1,599</td><td>1,599</td><td>1,599</td><td>1,599</td></tr><tr><td>Total Liabilities</td><td>13,668</td><td>26,182</td><td>41,738</td><td>51,285</td></tr><tr><td>Share capital</td><td>1,111</td><td>31,111</td><td>31,111</td><td>31,111</td></tr><tr><td>Reserves and minority interests</td><td>28,654</td><td>60,331</td><td>125,575</td><td>207,593</td></tr><tr><td>Shareholders&#x27; equity</td><td>29,765</td><td>91,442</td><td>156,686</td><td>238,704</td></tr><tr><td>Total Liab./Shrhldr&#x27;s Equity</td><td>45,289</td><td>122,112</td><td>205,713</td><td>300,078</td></tr></table>

<table><tr><td>Cashflow statements</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cashflow from operations</td><td>10,896</td><td>16,617</td><td>50,065</td><td>81,762</td></tr><tr><td>Profits from operation</td><td>13,600</td><td>42,786</td><td>85,685</td><td>111,656</td></tr><tr><td>Depreciation &amp; Amortization</td><td>850</td><td>1,150</td><td>1,450</td><td>1,750</td></tr><tr><td>Change in Working Capital</td><td>(2,029)</td><td>(19,397)</td><td>(24,417)</td><td>(15,095)</td></tr><tr><td>Others</td><td>(1,524)</td><td>(7,922)</td><td>(12,653)</td><td>(16,548)</td></tr><tr><td>Cashflow from investing</td><td>(2,619)</td><td>(3,000)</td><td>(3,000)</td><td>(3,000)</td></tr><tr><td>(Purchases) sale of PPE</td><td>(2,752)</td><td>(3,000)</td><td>(3,000)</td><td>(3,000)</td></tr><tr><td>Others</td><td>133</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cashflow from financing</td><td>(2,144)</td><td>29,445</td><td>(4,988)</td><td>(10,290)</td></tr><tr><td>Increase in bank loans</td><td>(1,114)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends &amp; Interests</td><td>(1,083)</td><td>(1,556)</td><td>(4,788)</td><td>(10,090)</td></tr><tr><td>Others</td><td>(2,113)</td><td>27,890</td><td>(9,776)</td><td>(20,379)</td></tr><tr><td>Net change in cash</td><td>5,956</td><td>43,062</td><td>42,077</td><td>68,472</td></tr></table>

Source: Company data, MS (E) estimates

<table><tr><td>Ratio analysis</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="5">YoY growth %</td></tr><tr>

[中间内容因长度限制已省略]

></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb94.23</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb26.65</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb979.46</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$23.16</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb36.00</td></tr><tr><td colspan="3">Derrick Yang</td></tr><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,090.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$513.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,265.00</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,200.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$25.80</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$913.00</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$1,765.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb6.07</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,095.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$1,850.00</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$1,740.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$181.50</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$52.50</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,345.00</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$306.00</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$52.60</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$7,890.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb34.24</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$196.50</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$84.50</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb5.00</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb6.19</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb237.02</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$29.60</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$700.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$186.50</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.00</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$5.32</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb57.59</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$325.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$927.00</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$234.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb77.40</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$1,480.00</td></tr><tr><td>Lenovo (0992.HK)</td><td>O (07/10/2026)</td><td>HK$21.42</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$1,865.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$1,150.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$82.20</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$325.50</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb132.29</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb334.00</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$794.00</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$282.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$139.00</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,620.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$699.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$521.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
