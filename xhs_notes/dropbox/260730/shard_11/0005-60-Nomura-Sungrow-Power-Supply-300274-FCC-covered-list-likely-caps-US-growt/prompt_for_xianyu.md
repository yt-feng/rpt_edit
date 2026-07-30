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
EQUITY: TECHNOLOGY

# FCC covered list likely caps US growth

## Grandfathering cushions 2026F, but frozen model pipeline erodes competitiveness into 2027F and beyond

FCC adds foreign-produced inverters to Covered List, effective immediately

The FCC (Federal Communications Commission) Public Safety and Homeland Security Bureau released Public Notice DA 26-786 on 28 July 2026, adding foreign-produced power inverters to the Covered List. The determination defines a power inverter on "two limbs": i) a bi-directional DC/AC conversion device, explicitly including micro-inverters, string, central and hybrid battery-based inverters; and ii) contains components enabling remote communication, control, sensing, data collection or monitoring via Wi-Fi, cellular or Bluetooth. In our view, the product portfolio of Sungrow likely falls within the defined scope, and the explicit naming of hybrid battery-based inverters likely brings storage PCS (power conversion system) into the perimeter. Critically, "foreign-produced" is defined by reference to 48 CFR §25.101(a), the Buy American "domestic end product" test, rather than country-of-origin rules; hence, third-country capacity therefore does not qualify.

Frozen model pipeline near term; SST and margins worth monitoring long term

In the near term, the closure of the new-model certification pathway is one binding constraint, which we expect to erode product competitiveness as the range of inverters ages. In addition, we also see impairment risk to overseas capacity built on a third-country strategy, since such capacity does not satisfy the "Buy America" test and Conditional Approval outcomes remain uncertain. In the long term, we flag classification risk around the EnerNeo SST (solid-state transformer). It is, in our view, an AC-to-DC conversion device that would satisfy both definitional limbs (we also expect the US certification plus grid-interconnection testing to likely extend availability to mid-2028F), would weaken the second-growth-driver narrative. Further, Sungrow's hardware re-sourcing toward non-China components and software and data localization, including US-hosted cloud and source-code audits, should raise costs/expenses, while a stripped-down no-connectivity product variant would impair products competitiveness.

## Maintain Neutral and TP of CNY120; trim 2027/28F EPS

We reiterate our Neutral rating for Sungrow with an unchanged TP of CNY120 to reflect near-term certification and long-term structural margin compression risks. We revise down our 2027/28F EPS to CNY8.78/10.41 from CNY9.13/11.20. Our TP is based on 14x 2027F P/E (previously 16x 2026F P/E), at -0.2x SD of its historical P/E. The stock currently trades at 12x 2027F P/E.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>89,184</td><td>106,417</td><td>103,136</td><td>128,480</td><td>125,455</td><td>156,765</td><td>152,317</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>13,461</td><td>15,083</td><td>15,030</td><td>18,924</td><td>18,201</td><td>23,222</td><td>21,572</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>13,461</td><td>15,083</td><td>15,030</td><td>18,924</td><td>18,201</td><td>23,222</td><td>21,572</td><td></td></tr><tr><td>FD normalised EPS</td><td>6.49</td><td>7.28</td><td>7.25</td><td>9.13</td><td>8.78</td><td>11.20</td><td>10.41</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>22.0</td><td>12.0</td><td>11.7</td><td>25.5</td><td>21.1</td><td>22.7</td><td>18.5</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>16.4</td><td>-</td><td>14.7</td><td>-</td><td>12.1</td><td>-</td><td>10.2</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>11.1</td><td>-</td><td>9.5</td><td>-</td><td>7.2</td><td>-</td><td>5.4</td><td></td></tr><tr><td>Price/book (x)</td><td>4.4</td><td>-</td><td>3.4</td><td>-</td><td>2.6</td><td>-</td><td>2.0</td><td></td></tr><tr><td>Dividend yield (%)</td><td>1.5</td><td>-</td><td>1.7</td><td>-</td><td>2.1</td><td>-</td><td>2.4</td><td></td></tr><tr><td>ROE (%)</td><td>29.9</td><td>26.1</td><td>26.1</td><td>25.1</td><td>24.2</td><td>23.6</td><td>22.4</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

<table><tr><td>Rating Remains</td><td>Neutral</td></tr><tr><td>Target price Remains</td><td>CNY 120.00</td></tr><tr><td>Closing price 29 July 2026</td><td>CNY 106.55</td></tr><tr><td>Implied upside</td><td>+12.6%</td></tr><tr><td>Market Cap (USD mn)</td><td>32,631.8</td></tr><tr><td>ADT (USD mn)</td><td>1,629.4</td></tr></table>

## Relative performance chart

![](images/d1b46fd0fb7fd5e8acfdcb303ea780217db99aee7e4db5bb7d8cd6bee0666d79.jpg)  
Source: LSEG, NOM

## Research Analysts

Advanced Manufacturing

Frank Fan - NIHK

frank.fan@NOM.com

+852 2252 2195

Donnie Teng - NIHK
donnie.teng@NOM.com
+852 2252 1439

## Key data on Sungrow Power Supply

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td><td></td></tr><tr><td>Absolute (CNY)</td><td>-31.5</td><td>-22.8</td><td>41.2</td><td colspan="2">M cap (USDmn)</td><td>32,631.8</td></tr><tr><td>Absolute (USD)</td><td>-31.3</td><td>-22.1</td><td>49.7</td><td colspan="2">Free float (%)</td><td>61.0</td></tr><tr><td>Rel to CSI 300</td><td>-24.3</td><td>-17.8</td><td>31.2</td><td colspan="2">3-mth ADT (USDmn)</td><td>1,629.4</td></tr><tr><td colspan="7">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td></td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td></td><td>77,857</td><td>89,184</td><td>103,136</td><td>125,455</td><td>152,317</td></tr><tr><td>Cost of goods sold</td><td></td><td>-54,545</td><td>-60,795</td><td>-72,344</td><td>-88,576</td><td>-108,621</td></tr><tr><td>Gross profit</td><td></td><td>23,312</td><td>28,389</td><td>30,791</td><td>36,879</td><td>43,696</td></tr><tr><td>SG&amp;A</td><td></td><td>-8,528</td><td>-11,230</td><td>-12,715</td><td>-15,066</td><td>-17,835</td></tr><tr><td colspan="7">Employee share expense</td></tr><tr><td>Operating profit</td><td></td><td>14,784</td><td>17,159</td><td>18,076</td><td>21,812</td><td>25,860</td></tr><tr><td>EBITDA</td><td></td><td>15,706</td><td>18,414</td><td>19,389</td><td>23,184</td><td>27,295</td></tr><tr><td>Depreciation</td><td></td><td>-783</td><td>-1,112</td><td>-1,168</td><td>-1,226</td><td>-1,288</td></tr><tr><td>Amortisation</td><td></td><td>-138</td><td>-143</td><td>-144</td><td>-146</td><td>-147</td></tr><tr><td>EBIT</td><td></td><td>14,784</td><td>17,159</td><td>18,076</td><td>21,812</td><td>25,860</td></tr><tr><td>Net interest expense</td><td></td><td>-290</td><td>-40</td><td>-651</td><td>-459</td><td>-560</td></tr><tr><td colspan="7">Associates &amp; JCEs</td></tr><tr><td>Other income</td><td></td><td>-950</td><td>-859</td><td>307</td><td>187</td><td>229</td></tr><tr><td>Earnings before tax</td><td></td><td>13,544</td><td>16,260</td><td>17,733</td><td>21,540</td><td>25,529</td></tr><tr><td>Income tax</td><td></td><td>-2,280</td><td>-2,727</td><td>-2,673</td><td>-3,231</td><td>-3,829</td></tr><tr><td>Net profit after tax</td><td></td><td>11,264</td><td>13,533</td><td>15,060</td><td>18,309</td><td>21,700</td></tr><tr><td>Minority interests</td><td></td><td>-228</td><td>-72</td><td>-30</td><td>-108</td><td>-128</td></tr><tr><td colspan="7">Other items</td></tr><tr><td colspan="7">Preferred dividends</td></tr><tr><td>Normalised NPAT</td><td></td><td>11,036</td><td>13,461</td><td>15,030</td><td>18,201</td><td>21,572</td></tr><tr><td colspan="7">Extraordinary items</td></tr><tr><td>Reported NPAT</td><td></td><td>11,036</td><td>13,461</td><td>15,030</td><td>18,201</td><td>21,572</td></tr><tr><td>Dividends</td><td></td><td>-2,217</td><td>-3,367</td><td>-3,757</td><td>-4,550</td><td>-5,393</td></tr><tr><td>Transfer to reserves</td><td></td><td>8,820</td><td>10,095</td><td>11,272</td><td>13,651</td><td>16,179</td></tr><tr><td colspan="7">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td></td><td>20.0</td><td>16.4</td><td>14.7</td><td>12.1</td><td>10.2</td></tr><tr><td>Normalised P/E (x)</td><td></td><td>20.0</td><td>16.4</td><td>14.7</td><td>12.1</td><td>10.2</td></tr><tr><td>FD normalised P/E (x)</td><td></td><td>20.0</td><td>16.4</td><td>14.7</td><td>12.1</td><td>10.2</td></tr><tr><td>Dividend yield (%)</td><td></td><td>1.0</td><td>1.5</td><td>1.7</td><td>2.1</td><td>2.4</td></tr><tr><td>Price/cashflow (x)</td><td></td><td>18.3</td><td>13.1</td><td>13.4</td><td>10.1</td><td>8.5</td></tr><tr><td>Price/book (x)</td><td></td><td>5.5</td><td>4.4</td><td>3.4</td><td>2.6</td><td>2.0</td></tr><tr><td>EV/EBITDA (x)</td><td></td><td>13.4</td><td>11.1</td><td>9.5</td><td>7.2</td><td>5.4</td></tr><tr><td>EV/EBIT (x)</td><td></td><td>14.2</td><td>11.9</td><td>10.2</td><td>7.7</td><td>5.7</td></tr><tr><td>Gross margin (%)</td><td></td><td>29.9</td><td>31.8</td><td>29.9</td><td>29.4</td><td>28.7</td></tr><tr><td>EBITDA margin (%)</td><td></td><td>20.2</td><td>20.6</td><td>18.8</td><td>18.5</td><td>17.9</td></tr><tr><td>EBIT margin (%)</td><td></td><td>19.0</td><td>19.2</td><td>17.5</td><td>17.4</td><td>17.0</td></tr><tr><td>Net margin (%)</td><td></td><td>14.2</td><td>15.1</td><td>14.6</td><td>14.5</td><td>14.2</td></tr><tr><td>Effective tax rate (%)</td><td></td><td>16.8</td><td>16.8</td><td>15.1</td><td>15.0</td><td>15.0</td></tr><tr><td>Dividend payout (%)</td><td></td><td>20.1</td><td>25.0</td><td>25.0</td><td>25.0</td><td>25.0</td></tr><tr><td>ROE (%)</td><td></td><td>31.7</td><td>29.9</td><td>26.1</td><td>24.2</td><td>22.4</td></tr><tr><td>ROA (pretax %)</td><td></td><td>18.5</td><td>18.0</td><td>17.4</td><td>17.6</td><td>17.6</td></tr><tr><td colspan="7">Growth (%)</td></tr><tr><td>Revenue</td><td></td><td>7.8</td><td>14.5</td><td>15.6</td><td>21.6</td><td>21.4</td></tr><tr><td>EBITDA</td><td></td><td>18.9</td><td>17.2</td><td>5.3</td><td>19.6</td><td>17.7</td></tr><tr><td>Normalised EPS</td><td></td><td>-16.4</td><td>22.0</td><td>11.7</td><td>21.1</td><td>18.5</td></tr><tr><td>Normalised FDEPS</td><td></td><td>-16.4</td><td>22.0</td><td>11.7</td><td>21.1</td><td>18.5</td></tr></table>

Source: Company data, NOM estimates

Cashflow statement (CNYmn)

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>15,706</td><td>18,414</td><td>19,389</td><td>23,184</td><td>27,295</td></tr><tr><td>Change in working capital</td><td>-6,009</td><td>1,473</td><td>5,655</td><td>-1,022</td><td>-2,144</td></tr><tr><td>Other operating cashflow</td><td>2,372</td><td>-2,969</td><td>-8,549</td><td>-321</td><td>736</td></tr><tr><td>Cashflow from operations</td><td>12,068</td><td>16,918</td><td>16,495</td><td>21,841</td><td>25,887</td></tr><tr><td>Capital expenditure</td><td>-2,786</td><td>-3,008</td><td>-3,720</td><td>-4,391</td><td>-5,331</td></tr><tr><td>Free cashflow</td><td>9,282</td><td>13,910</td><td>12,775</td><td>17,451</td><td>20,556</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-810</td><td>-899</td><td>-738</td><td>-798</td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>-1,099</td><td>-689</td><td>0</td><td>0</td><td></td></tr><tr><td>Adjustments</td><td>-8,067</td><td>1,646</td><td>2,242</td><td>738</td><td>798</td></tr><tr><td>CF after investing acts</td><td>1,215</td><td>13,647</td><td>13,429</td><td>17,451</td><td>20,556</td></tr><tr><td>Cash dividends</td><td>-2,217</td><td>-3,367</td><td>-3,757</td><td>-4,550</td><td>-5,393</td></tr><tr><td>Equity issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Debt issue</td><td>897</td><td>-2,713</td><td>2,280</td><td>2,280</td><td>2,280</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>3,637</td><td>-4,536</td><td>6,827</td><td>1,399</td><td>2,242</td></tr><tr><td>CF from financial acts</td><td>2,317</td><td>-10,616</td><td>5,350</td><td>-871</td><td>-871</td></tr><tr><td>Net cashflow</td><td>3,532</td><td>3,031</td><td>18,779</td><td>16,579</td><td>19,684</td></tr><tr><td>Beginning cash</td><td>16,267</td><td>19,799</td><td>22,831</td><td>41,610</td><td>58,189</td></tr><tr><td>Ending cash</td><td>19,799</td><td>22,831</td><td>41,610</td><td>58,189</td><td>77,874</td></tr><tr><td>Ending net debt</td><td>-10,722</td><td>-17,343</td><td>-36,248</td><td>-52,828</td><td>-72,512</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>19,799</td><td>22,831</td><td>41,610</td><td>58,189</td><td>77,874</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>28,486</td><td>24,733</td><td>34,468</td><td>42,517</td><td>52,269</td></tr><tr><td>Inventories</td><td>29,028</td><td>27,255</td><td>36,918</td><td>48,585</td><td>59,988</td></tr><tr><td>Other current assets</td><td>17,836</td><td>20,609</td><td>16,038</td><td>17,360</td><td>18,791</td></tr><tr><td>Total current assets</td><td>95,149</td><td>95,428</td><td>129,034</td><td>166,652</td><td>208,922</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>11,267</td><td>13,674</td><td>14,538</td><td>15,293</td><td>16,187</td></tr><tr><td>Goodwill</td><td>297</td><td>297</td><td>297</td><td>297</td><td>297</td></tr><tr><td>Other intangible assets</td><td>1,122</td><td>1,231</td><td>1,295</td><td>1,321</td><td>1,348</td></tr><tr><td>Other LT assets</td><td>7,239</td><td>8,049</td><td>8,948</td><td>9,685</td><td>10,483</td></tr><tr><td>Total assets</td><td>115,074</td><td>118,679</td><td>154,111</td><td>193,248</td><td>237,237</td></tr><tr><td>Short-term debt</td><td>4,214</td><td>2,422</td><td>2,279</td><td>2,279</td><td>2,279</td></tr><tr><td>Accounts payable</td><td>36,757</td><td>36,636</td><td>50,762</td><td>66,805</td><td>82,484</td></tr><tr><td>Other current liabilities</td><td>19,327</td><td>18,169</td><td>24,525</td><td>28,498</td><td>33,261</td></tr><tr><td>Total current liabilities</td><td>60,298</td><td>57,228</td><td>77,565</td><td>97,582</td><td>118,024</td></tr><tr><td>Long-term debt</td><td>4,863</td><td>3,065</td><td>3,083</td><td>3,083</td><td>3,083</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>9,714</td><td>8,615</td><td>7,926</td><td>7,926</td><td>7,926</td></tr><tr><td>Total liabilities</td><td>74,875</td><td>68,908</td><td>88,574</td><td>108,591</td><td>129,033</td></tr><tr><td>Minority interest</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>2,073</td><td>2,073</td><td>2,073</td><td>2,073</td><td>2,073</td></tr><tr><td>Retained earnings</td><td>28,346</td><td>37,640</td><td>52,670</td><td>70,871</td><td>92,444</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td>9,779</td><td>10,058</td><td>10,793</td><td>11,712</td><td>13,688</td></tr><tr><td>Total shareholders&#x27; equity</td><td>40,199</td><td>49,772</td><td>65,537</

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
