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
21 Jul 2026 06:33:15 ET | 13 pages

# Chagee Holdings (CHA.O)

## 2Q26E Earnings Preview; Reducing TP & Estimates

## CITI'S TAKE

We forecast Chagee's group same-store GMV to decline by \~15% YoY in 2Q26E, rough in line with that in 1Q26 (-16.0% YoY). We expect its 2Q26E non-GAAP NP to be largely flat QoQ (vs. Rmb507m in 1Q26) and down \~20% YoY. We anticipate its YoY decline in same-store GMV to sequentially improve in 2H26E, on a low comp base (due to its reluctance to participate in delivery platforms' subsidy war in 2H25). With plans to slow openings in 2026, Chagee "optimized its organization" in 4Q25, per mgmt commentary on its earnings call. We believe this included HQ-level admin headcount cut, with potentially more pronounced opex savings in 2H26E. We lower our 2026E/27E non-GAAP NP forecasts by 25%/30% and cut our DCF-based target price to US\$15.2 (from US\$24.6); we also introduce 2028E estimates. We expect the market to have higher conviction on Chagee's recovery if its operation sequentially improves in 2H26E.

2Q26E results preview — We expect Chagee's average monthly GMV per store to be \~Rmb350k+ in China in 2Q26E (vs. Rmb356k in 1Q26, Rmb404k in 2Q25) and group sales to stay largely flat YoY in 2Q26E. Since 2026, its China franchisees switched to a GMV-based revenue-sharing model, where Chagee takes a higher fee rate but reduces its markup on sales to franchisees. Financially, this has limited impact on its GPM (on transactions with franchisees) and group revenue, despite some technically shifted components in GP dollars. We model non-GAAP OPM of \~17% in 2Q26E, largely flat QoQ (1Q26: 17.1%) and down YoY (vs. 19.8% in 2Q25). Excluding an estimated \~Rmb40m of SBC, we expect non-GAAP NP to reach \~Rmb500m in 2Q26E (vs. Rmb507m in 1Q26). Unlike most other listed on-premise fresh tea players (who should face a high comp base in 2H26E due to their significant benefit from the 2H25 delivery platforms' price war), Chagee will have a low comp base in 2H26E due to its limited participation. We believe the conversion of its \~400 China franchised stores to DTC was largely completed by end-2025. We expect its YoY same-store GMV decline to narrow in 3Q26E before turning positive in 4Q26E.

Target price & estimates reductions — We lower 2026E/27E non-GAAP NP by 25%/30%, given 18%/27% cuts in '26E/27E sales (on a slower-than-expected 1H SSS recovery and reset of 2026 net store opening plan to \~300 in China) and operating deleveraging. We forecast sales to stay flat YoY and non-GAAP NP to decline 5% YoY in '26E. Our DCF-based TP (on 17.0% WACC and 2% terminal growth rate) is lowered to US\$15.2 (from US\$24.6).

## Earnings Summary

<table><tr><td>Year to 31 Dec</td><td>Net Profit (RmbM)</td><td>Diluted EPS (Rmb)</td><td>EPS growth (%)</td><td>P/E (x)</td><td>P/B (x)</td><td>ROE (%)</td><td>Yield (%)</td></tr><tr><td>2024A</td><td>2,517</td><td>14.904</td><td>210.2</td><td>5.3</td><td>3.7</td><td>103.1</td><td>na</td></tr><tr><td>2025A</td><td>1,895</td><td>11.503</td><td>-22.8</td><td>6.8</td><td>2.0</td><td>34.7</td><td>8.2</td></tr><tr><td>2026E</td><td>1,808</td><td>9.383</td><td>-18.4</td><td>8.4</td><td>1.9</td><td>23.9</td><td>8.3</td></tr><tr><td>2027E</td><td>1,940</td><td>10.069</td><td>7.3</td><td>7.8</td><td>1.8</td><td>23.9</td><td>8.3</td></tr><tr><td>2028E</td><td>2,012</td><td>10.442</td><td>3.7</td><td>7.5</td><td>1.7</td><td>23.1</td><td>8.3</td></tr></table>

Source: Powered by dataCentral

## Buy / High Risk

Price (20 Jul 26 16:00) US\$11.58

Target price US\$15.20↓

from US\$24.60

Expected share price return 31.3%

Expected dividend yield 8.3%

Expected total return 39.6%

Market Cap US\$2,209M

## Price Performance

## (RIC: CHA.O, BB: CHA US)

![](images/9660c3b27035035b38be8dc251e43027046579e41ff1a199e1eb55b08c278adc.jpg)

Xiaopo Wei, CFA $^{AC}$ +852-2501-2472
xiaopo.wei@citi.com

Vincent Young
+852-2501-2738
vincent.young@citi.com

<table><tr><td>Profit &amp; Loss (Rmbm)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue</td><td>12,406</td><td>12,907</td><td>12,969</td><td>13,631</td><td>14,435</td></tr><tr><td>Cost of sales</td><td>-6,257</td><td>-6,001</td><td>-5,967</td><td>-6,228</td><td>-6,543</td></tr><tr><td>Gross profit</td><td>6,149</td><td>6,906</td><td>7,002</td><td>7,404</td><td>7,892</td></tr><tr><td>Gross Margin (%)</td><td>49.6</td><td>53.5</td><td>54.0</td><td>54.3</td><td>54.7</td></tr><tr><td>EBITDA (Adj)</td><td>2,948</td><td>1,494</td><td>2,333</td><td>2,418</td><td>2,525</td></tr><tr><td>EBITDA Margin (Adj) (%)</td><td>23.8</td><td>11.6</td><td>18.0</td><td>17.7</td><td>17.5</td></tr><tr><td>Depreciation</td><td>-61</td><td>-146</td><td>-139</td><td>-133</td><td>-141</td></tr><tr><td>Amortisation</td><td>0</td><td>0</td><td>-90</td><td>0</td><td>0</td></tr><tr><td>EBIT (Adj)</td><td>2,887</td><td>1,347</td><td>2,104</td><td>2,285</td><td>2,384</td></tr><tr><td>EBIT Margin (Adj) (%)</td><td>23.3</td><td>10.4</td><td>16.2</td><td>16.8</td><td>16.5</td></tr><tr><td>Net interest</td><td>37</td><td>147</td><td>196</td><td>206</td><td>220</td></tr><tr><td>Associates</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Non-Op/Except/Other Adj</td><td>118</td><td>123</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Pre-tax profit</td><td>3,042</td><td>1,618</td><td>2,300</td><td>2,491</td><td>2,603</td></tr><tr><td>Tax</td><td>-528</td><td>-432</td><td>-480</td><td>-511</td><td>-534</td></tr><tr><td>Extraord./Min.Int./Pref.div.</td><td>2</td><td>-15</td><td>-52</td><td>-80</td><td>-97</td></tr><tr><td>Reported net profit</td><td>2,516</td><td>1,171</td><td>1,768</td><td>1,900</td><td>1,972</td></tr><tr><td>Net Margin (%)</td><td>20.3</td><td>9.1</td><td>13.6</td><td>13.9</td><td>13.7</td></tr><tr><td>Core NPAT</td><td>2,517</td><td>1,895</td><td>1,808</td><td>1,940</td><td>2,012</td></tr></table>

Price: US\$11.58; TP: US\$15.20; Market Cap: US\$2,209m; Recomm: Buy/High Risk

<table><tr><td>Valuation ratios</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>PE (x)</td><td>5.3</td><td>6.8</td><td>8.4</td><td>7.8</td><td>7.5</td></tr><tr><td>PB (x)</td><td>3.7</td><td>2.0</td><td>1.9</td><td>1.8</td><td>1.7</td></tr><tr><td>EV/EBITDA (x)</td><td>3.8</td><td>5.7</td><td>3.0</td><td>2.8</td><td>2.5</td></tr><tr><td>FCF yield (%)</td><td>19.7</td><td>9.4</td><td>9.6</td><td>11.4</td><td>12.0</td></tr><tr><td>Dividend yield (%)</td><td>na</td><td>8.2</td><td>8.3</td><td>8.3</td><td>8.3</td></tr><tr><td>Payout ratio (%)</td><td>0</td><td>56</td><td>69</td><td>65</td><td>62</td></tr><tr><td>ROE (%)</td><td>103.1</td><td>21.4</td><td>23.3</td><td>23.4</td><td>22.6</td></tr></table>

<table><tr><td>Cashflow (Rmbm)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EBITDA</td><td>2,948</td><td>1,494</td><td>2,333</td><td>2,418</td><td>2,525</td></tr><tr><td>Working capital</td><td>382</td><td>-293</td><td>-578</td><td>-149</td><td>-192</td></tr><tr><td>Other</td><td>-492</td><td>428</td><td>-193</td><td>-434</td><td>-411</td></tr><tr><td>Operating cashflow</td><td>2,838</td><td>1,629</td><td>1,562</td><td>1,834</td><td>1,921</td></tr><tr><td>Capex</td><td>-226</td><td>-417</td><td>-110</td><td>-110</td><td>-110</td></tr><tr><td>Net acq/disposals</td><td>-16</td><td>-35</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other</td><td>12</td><td>-373</td><td>259</td><td>0</td><td>0</td></tr><tr><td>Investing cashflow</td><td>-229</td><td>-825</td><td>149</td><td>-110</td><td>-110</td></tr><tr><td>Dividends paid</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Financing cashflow</td><td>-174</td><td>2,047</td><td>-1,240</td><td>-1,240</td><td>-1,240</td></tr><tr><td>Net change in cash</td><td>2,446</td><td>2,850</td><td>471</td><td>485</td><td>571</td></tr><tr><td>Free cashflow to s/holders</td><td>2,612</td><td>1,212</td><td>1,452</td><td>1,724</td><td>1,811</td></tr></table>

<table><tr><td>Per share data</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Reported EPS (Rmb)</td><td>14.900</td><td>7.110</td><td>9.175</td><td>9.862</td><td>10.234</td></tr><tr><td>Core EPS (Rmb)</td><td>14.904</td><td>11.503</td><td>9.383</td><td>10.069</td><td>10.442</td></tr><tr><td>DPS (Rmb)</td><td>0</td><td>6.464</td><td>6.500</td><td>6.500</td><td>6.500</td></tr><tr><td>CFPS (Rmb)</td><td>16.804</td><td>9.889</td><td>8.104</td><td>9.520</td><td>9.970</td></tr><tr><td>FCFPS (Rmb)</td><td>15.469</td><td>7.357</td><td>7.533</td><td>8.949</td><td>9.399</td></tr><tr><td>BVPS (Rmb)</td><td>21.246</td><td>38.486</td><td>40.982</td><td>44.024</td><td>47.352</td></tr><tr><td>Wtd avg ord shares (m)</td><td>169</td><td>162</td><td>191</td><td>191</td><td>191</td></tr><tr><td>Wtd avg diluted shares (m)</td><td>169</td><td>165</td><td>193</td><td>193</td><td>193</td></tr></table>

<table><tr><td>Growth rates</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue (%)</td><td>167.4</td><td>4.0</td><td>0.5</td><td>5.1</td><td>5.9</td></tr><tr><td>EBIT (Adj) (%)</td><td>168.7</td><td>-53.3</td><td>56.2</td><td>8.6</td><td>4.3</td></tr><tr><td>Core NPAT (%)</td><td>210.2</td><td>-24.7</td><td>-4.6</td><td>7.3</td><td>3.7</td></tr><tr><td>Core EPS (%)</td><td>210.2</td><td>-22.8</td><td>-18.4</td><td>7.3</td><td>3.7</td></tr></table>

<table><tr><td>Balance Sheet (Rmbm)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; cash equiv.</td><td>4,869</td><td>7,993</td><td>8,114</td><td>8,599</td><td>9,170</td></tr><tr><td>Accounts receivables</td><td>122</td><td>146</td><td>78</td><td>81</td><td>85</td></tr><tr><td>Inventory</td><td>132</td><td>228</td><td>187</td><td>228</td><td>273</td></tr><tr><td>Net fixed &amp; other tangibles</td><td>1,044</td><td>2,262</td><td>2,337</td><td>2,520</td><td>2,646</td></tr><tr><td>Goodwill &amp; intangibles</td><td>20</td><td>110</td><td>20</td><td>20</td><td>20</td></tr><tr><td>Financial &amp; other assets</td><td>409</td><td>724</td><td>312</td><td>322</td><td>333</td></tr><tr><td>Total assets</td><td>6,596</td><td>11,463</td><td>11,048</td><td>11,770</td><td>12,528</td></tr><tr><td>Accounts payable</td><td>597</td><td>630</td><td>483</td><td>504</td><td>530</td></tr><tr><td>Short-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Long-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Provisions &amp; other liab</td><td>2,311</td><td>3,256</td><td>2,460</td><td>2,500</td><td>2,500</td></tr><tr><td>Total liabilities</td><td>2,908</td><td>3,886</td><td>2,943</td><td>3,004</td><td>3,030</td></tr><tr><td>Shareholders&#x27; equity</td><td>3,588</td><td>7,342</td><td>7,818</td><td>8,398</td><td>9,033</td></tr><tr><td>Minority interests</td><td>101</td><td>235</td><td>287</td><td>368</td><td>465</td></tr><tr><td>Total equity</td><td>3,688</td><td>7,577</td><td>8,105</td><td>8,766</td><td>9,498</td></tr><tr><td>Net debt (Adj)</td><td>-4,869</td><td>-7,993</td><td>-8,114</td><td>-8,599</td><td>-9,170</td></tr><tr><td>Net debt to equity (Adj) (%)</td><td>-132.0</td><td>-105.5</td><td>-100.1</td><td>-98.1</td><td>-96.5</td></tr></table>

For definitions of the items in this table, please click here.

## Estimates revisions

Figure 1. Estimates revision

<table><tr><td>New</td><td>GMV (Rmb m)</td><td>Chg (%)</td><td>Sales (Rmb m)</td><td>Chg (%)</td><td>Non-GAAP NP (Rmb m)</td><td>Chg (%)</td></tr><tr><td>2026E</td><td>31,222</td><td>-14.6%</td><td>12,969</td><td>-18.0%</td><td>1,808</td><td>-24.5%</td></tr><tr><td>2027E</td><td>32,501</td><td>-19.7%</td><td>13,631</td><td>-26.8%</td><td>1,940</td><td>-30.3%</td></tr><tr><td>2028E</td><td>34,031</td><td>New</td><td>14,435</td><td>New</td><td>2,012</td><td>New</td></tr><tr><td>Previous</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026E</td><td>36,551</td><td></td><td>15,807</td><td></td><td>2,396</td><td></td></tr><tr><td>2027E</td><td>40,463</td><td></td><td>18,609</td><td></td><td>2,782</td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

We lower 2026E/27E non-GAAP NP estimates by 25%/30%, given 18%/27% cuts in '26E/27E sales (on a slower-than-expected 1H SSS recovery and reset of 2026 net store opening plan to \~300 in China) and operating deleveraging. We forecast sales to stay flat YoY and non-GAAP NP to decline 5% YoY in '26E.

Target price revision  
Figure 2. Chagee - DCF valuation

<table><tr><td></td><td>FY26</td><td>FY27</td><td>FY28</td><td>FY29</td><td>FY30</td><td>FY31</td><td>FY32</td><td>FY33</td><td>FY34</td><td>FY35</td><td>Terminal</td></tr><tr><td>EBITDA</td><td>2,333</td><td>2,418</td><td>2,525</td><td>2,652</td><td>2,774</td><td>3,005</td><td>3,187</td><td>3,282</td><td>3,428</td><td>3,577</td><td></td></tr><tr><td>Add: Chg in Working Capital</td><td>(578)</td><td>(149)</td><td>(192)</td><td>(196)</td><td>(199)</td><td>(203)</td><td>(210)</td><td>(210)</td><td>(205)</td><td>(197)</td><td></td></tr><tr><td>Less: Capex</td><td>(110)</td><td>(110)</td><td>(110)</td><td>(111)</td><td>(112)</td><td>(113)</td><td>(114)</td><td>(115)</td><td>(116)</td><td>(117)</td><td></td></tr><tr><td>Less: Cash tax paid</td><td>(480)</td><td>(511)</td><td>(534)</td><td>(562)</td><td>(591)</td><td>(642)</td><td>(684)</td><td>(708)</td><td>(743)</td><td>(778)</td><td></td></tr><tr><td>Free Operating Cashflow</td><td>1,165</td><td>1,648</td><td>1,689</td><td>1,784</td><td>1,872</td><td>2,046</td><td>2,179</td><td>2,249</td><td>2,364</td><td>2,485</td><td>16,898</td></tr><tr><td>PV of free operating cashflow</td><td>1,165</td><td>1,409</td><td>1,234</td><td>1,114</td><td>999</td><td>933</td><td>849</td><td>749</td><td>673</td><td>605</td><td>4,113</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WACC</td><td>17.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Risk-free Rate</td><td>4.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Adjusted beta</td><td>1.25</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Market Risk Premium</td><td>10.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost of Equity</td><td>17.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>After-tax Cost of Debt</td><td>6.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Target Equity Percentage</td><td>100%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Target Debt Percentage</td><td>0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Assumed Long-term Growth Rate</td><td>2.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Enterprise value</td><td>12,678</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Add : Cash</td><td>8,114</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Less: Debt</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Less: Minorities</td><td>(287)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Equity Value (Rmbm)</td><td>20,79

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
