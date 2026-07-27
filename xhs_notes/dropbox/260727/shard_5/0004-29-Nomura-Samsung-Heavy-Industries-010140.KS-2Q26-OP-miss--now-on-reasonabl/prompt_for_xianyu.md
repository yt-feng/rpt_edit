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
EQUITY: CAPITAL GOODS

# 2Q26 OP miss; now on reasonable level

Upgrade to Neutral and lower TP to KRW25,000

## Upgrade to Neutral and lower TP to KRW25,000, implying $9.2\%$ upside

We upgrade our rating to Neutral from Reduce owing to the recent steep decline in share price. We think that Samsung Heavy's (SHI) valuation is now on a reasonable level. The stock price has corrected $33.4\%$ from its peak on 24 Apr (vs. KOSPI up $+3.6\%$ ). SHI is trading at 2026F P/B of 3.7x. We have not raised our rating to Buy owing to the downside pressure on newbuilding prices from Chinese shipyard expansion. Upside risks are (1) blockage of Bab Al-Mandab Strait which could lead to massive new orders of tankers and (2) unexpected floating datacenter (FDC) new orders. Downside risk will be continued expansion of Chinese shipyards.

We lower our TP to KRW25,000 from KRW27,000. Our new TP is based on a 12-month-forward (12MF) BVPS of KRW7,456 (previously: 12MF BVPS of KRW6,738), multiplied by a target P/B of $3.35\mathrm{x}$ (previously: $4.01\mathrm{x}$ ). Our target P/B implies a $4.3\%$ premium to SHI's core-shipbuilding implied P/B of $3.21\mathrm{x}$ (Fig. 11). We factor in the premium coming from the US naval opportunity, as SHI is now participating in MASGA (Make America Shipbuilding Great Again) through its partnerships with General Dynamics (GD US, Not rated) and Vigor (unlisted).

## 2Q26 OP miss owing to one-off cost

SHI recorded revenue of KRW3.2tn (+20.4% y-y) and operating profit (OP) of KRW325bn (+58.7% y-y) in 2Q26 (Fig. 2). OP was below the Quantiwise consensus estimate of KRW374bn by 13.2%. KRW25bn of one-off cost occurred from additional booking of retirement pension. KRW150bn of additional revenue was booked from global operations and the re-activated No. 2 dock. Management expects KRW900bn of revenue addition in 2026E. However, in our estimate, the operating margin from the new capacity was below the SHI's average shipbuilding margin. In 2Q26, shipbuilding revenue increased to KRW2.4tn (+14.3% y-y) thanks to new order and capacity addition. We estimate 2Q26F offshore revenue increased to KRW723bn (+49.7% y-y), following the revenue ramp-up of F-LNG projects.

(Continued on page 4)

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (KRW)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (bn)</td><td>10,650</td><td>13,019</td><td>13,016</td><td>15,571</td><td>16,036</td><td>16,486</td><td>17,077</td><td></td></tr><tr><td>Reported net profit (bn)</td><td>546</td><td>1,243</td><td>1,088</td><td>1,628</td><td>1,820</td><td>1,924</td><td>2,189</td><td></td></tr><tr><td>Normalised net profit (bn)</td><td>546</td><td>1,243</td><td>1,088</td><td>1,628</td><td>1,820</td><td>1,924</td><td>2,189</td><td></td></tr><tr><td>FD normalised EPS</td><td>620</td><td>1,412</td><td>1,236</td><td>1,849</td><td>2,068</td><td>2,187</td><td>2,488</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>753.9</td><td>127.8</td><td>99.3</td><td>31.0</td><td>67.4</td><td>18.2</td><td>20.3</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>36.9</td><td>-</td><td>18.5</td><td>-</td><td>11.1</td><td>-</td><td>9.2</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>18.6</td><td>-</td><td>10.8</td><td>-</td><td>6.0</td><td>-</td><td>4.8</td><td></td></tr><tr><td>Price/book (x)</td><td>4.9</td><td>-</td><td>3.7</td><td>-</td><td>2.8</td><td>-</td><td>2.2</td><td></td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.2</td><td></td></tr><tr><td>ROE (%)</td><td>13.7</td><td>26.1</td><td>22.5</td><td>26.2</td><td>28.4</td><td>24.7</td><td>26.7</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>30.7</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

26 July 2026

Rating
Up from Reduce
Neutral

<table><tr><td>Target priceReduced fromKRW 27,000</td><td>KRW 25,000</td></tr></table>

<table><tr><td>Closing price24 July 2026</td><td>KRW 22,900</td></tr></table>

<table><tr><td>Implied upside</td><td>+9.2%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>13,738.7</td></tr><tr><td>ADT (USD mn)</td><td>106.3</td></tr></table>

## Relative performance chart

![](images/a1d319c89158a8b3dff06a5430cf4283d05c9b7e4617b096d72dc3464cabf188.jpg)  
Source: LSEG, NOM

## Research Analysts

Korea Industrials
Eon Hwang - NFIK
eon.hwang@NOM.com
+822 3783 2318

## Key data on Samsung Heavy Industries

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td><td></td></tr><tr><td>Absolute (KRW)</td><td>-6.9</td><td>-33.4</td><td>17.7</td><td colspan="2">M cap (USDmn)</td><td>13,738.7</td></tr><tr><td>Absolute (USD)</td><td>-1.9</td><td>-32.6</td><td>9.9</td><td colspan="2">Free float (%)</td><td>76.2</td></tr><tr><td>Rel to KOSPI 200</td><td>16.0</td><td>-42.0</td><td>-127.7</td><td colspan="2">3-mth ADT (USDmn)</td><td>106.3</td></tr><tr><td colspan="7">Income statement (KRWbn)</td></tr><tr><td>Year-end 31 Dec</td><td></td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td></td><td>9,903</td><td>10,650</td><td>13,016</td><td>16,036</td><td>17,077</td></tr><tr><td>Cost of goods sold</td><td></td><td>-8,983</td><td>-9,276</td><td>-11,116</td><td>-13,355</td><td>-14,006</td></tr><tr><td>Gross profit</td><td></td><td>921</td><td>1,374</td><td>1,900</td><td>2,680</td><td>3,071</td></tr><tr><td>SG&amp;A</td><td></td><td>-418</td><td>-512</td><td>-534</td><td>-550</td><td>-567</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td></td><td>503</td><td>862</td><td>1,365</td><td>2,130</td><td>2,504</td></tr><tr><td>EBITDA</td><td></td><td>795</td><td>1,151</td><td>1,777</td><td>2,809</td><td>3,128</td></tr><tr><td>Depreciation</td><td></td><td>-289</td><td>-284</td><td>-406</td><td>-673</td><td>-618</td></tr><tr><td>Amortisation</td><td></td><td>-4</td><td>-5</td><td>-6</td><td>-6</td><td>-5</td></tr><tr><td>EBIT</td><td></td><td>503</td><td>862</td><td>1,365</td><td>2,130</td><td>2,504</td></tr><tr><td>Net interest expense</td><td></td><td>-192</td><td>-115</td><td>13</td><td>80</td><td>166</td></tr><tr><td>Associates &amp; JCEs</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other income</td><td></td><td>-626</td><td>-96</td><td>-161</td><td>0</td><td>0</td></tr><tr><td>Earnings before tax</td><td></td><td>-315</td><td>650</td><td>1,217</td><td>2,210</td><td>2,670</td></tr><tr><td>Income tax</td><td></td><td>369</td><td>-115</td><td>-138</td><td>-398</td><td>-481</td></tr><tr><td>Net profit after tax</td><td></td><td>54</td><td>536</td><td>1,079</td><td>1,812</td><td>2,189</td></tr><tr><td>Minority interests</td><td></td><td>10</td><td>10</td><td>9</td><td>9</td><td></td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td></td><td>64</td><td>546</td><td>1,088</td><td>1,820</td><td>2,189</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td></td><td>64</td><td>546</td><td>1,088</td><td>1,820</td><td>2,189</td></tr><tr><td>Dividends</td><td></td><td>0</td><td>-1</td><td>0</td><td>0</td><td>-440</td></tr><tr><td>Transfer to reserves</td><td></td><td>64</td><td>544</td><td>1,088</td><td>1,820</td><td>1,749</td></tr><tr><td colspan="7">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td></td><td>315.5</td><td>36.9</td><td>18.5</td><td>11.1</td><td>9.2</td></tr><tr><td>Normalised P/E (x)</td><td></td><td>315.5</td><td>36.9</td><td>18.5</td><td>11.1</td><td>9.2</td></tr><tr><td>FD normalised P/E (x)</td><td></td><td>315.5</td><td>36.9</td><td>18.5</td><td>11.1</td><td>9.2</td></tr><tr><td>Dividend yield (%)</td><td></td><td>-</td><td>0.0</td><td>-</td><td>-</td><td>2.2</td></tr><tr><td>Price/cashflow (x)</td><td></td><td>30.8</td><td>12.9</td><td>7.5</td><td>8.3</td><td>7.5</td></tr><tr><td>Price/book (x)</td><td></td><td>5.3</td><td>4.9</td><td>3.7</td><td>2.8</td><td>2.2</td></tr><tr><td>EV/EBITDA (x)</td><td></td><td>28.1</td><td>18.6</td><td>10.8</td><td>6.0</td><td>4.8</td></tr><tr><td>EV/EBIT (x)</td><td></td><td>44.5</td><td>24.8</td><td>14.0</td><td>7.9</td><td>6.0</td></tr><tr><td>Gross margin (%)</td><td></td><td>9.3</td><td>12.9</td><td>14.6</td><td>16.7</td><td>18.0</td></tr><tr><td>EBITDA margin (%)</td><td></td><td>8.0</td><td>10.8</td><td>13.7</td><td>17.5</td><td>18.3</td></tr><tr><td>EBIT margin (%)</td><td></td><td>5.1</td><td>8.1</td><td>10.5</td><td>13.3</td><td>14.7</td></tr><tr><td>Net margin (%)</td><td></td><td>0.6</td><td>5.1</td><td>8.4</td><td>11.4</td><td>12.8</td></tr><tr><td>Effective tax rate (%)</td><td></td><td>-</td><td>17.6</td><td>11.4</td><td>18.0</td><td>18.0</td></tr><tr><td>Dividend payout (%)</td><td></td><td>0.0</td><td>0.2</td><td>0.0</td><td>0.0</td><td>20.1</td></tr><tr><td>ROE (%)</td><td></td><td>1.8</td><td>13.7</td><td>22.5</td><td>28.4</td><td>26.7</td></tr><tr><td>ROA (pretax %)</td><td></td><td>3.2</td><td>5.7</td><td>8.9</td><td>12.7</td><td>14.7</td></tr><tr><td colspan="7">Growth (%)</td></tr><tr><td>Revenue</td><td></td><td>23.6</td><td>7.5</td><td>22.2</td><td>23.2</td><td>6.5</td></tr><tr><td>EBITDA</td><td></td><td>66.8</td><td>44.7</td><td>54.4</td><td>58.0</td><td>11.4</td></tr><tr><td>Normalised EPS</td><td></td><td></td><td>753.9</td><td>99.3</td><td>67.4</td><td>20.3</td></tr><tr><td>Normalised FDEPS</td><td></td><td></td><td>753.9</td><td>99.3</td><td>67.4</td><td>20.3</td></tr></table>

Source: Company data, NOM estimates  
Cashflow statement (KRWbn)

<table><tr><td colspan="6">Cashflow statement (KRWbn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>795</td><td>1,151</td><td>1,777</td><td>2,809</td><td>3,128</td></tr><tr><td>Change in working capital</td><td>891</td><td>786</td><td>999</td><td>-66</td><td>-118</td></tr><tr><td>Other operating cashflow</td><td>-1,032</td><td>-374</td><td>-93</td><td>-324</td><td>-320</td></tr><tr><td>Cashflow from operations</td><td>655</td><td>1,563</td><td>2,683</td><td>2,418</td><td>2,690</td></tr><tr><td>Capital expenditure</td><td>210</td><td>-195</td><td>-241</td><td>-265</td><td>-291</td></tr><tr><td>Free cashflow</td><td>865</td><td>1,368</td><td>2,443</td><td>2,153</td><td>2,398</td></tr><tr><td>Reduction in investments</td><td>101</td><td>-263</td><td>-295</td><td>0</td><td>0</td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-1</td><td>-23</td><td>86</td><td>86</td><td>26</td></tr><tr><td>Inc in other LT liabilities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Adjustments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CF after investing acts</td><td>965</td><td>1,082</td><td>2,233</td><td>2,240</td><td>2,424</td></tr><tr><td>Cash dividends</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>-440</td></tr><tr><td>Equity issue</td><td>-111</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>-339</td><td>-1,170</td><td>-1,363</td><td>-766</td><td>0</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>-143</td><td>-95</td><td>41</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-593</td><td>-1,266</td><td>-1,322</td><td>-766</td><td>-440</td></tr><tr><td>Net cashflow</td><td>372</td><td>-183</td><td>911</td><td>1,473</td><td>1,984</td></tr><tr><td>Beginning cash</td><td>584</td><td>956</td><td>773</td><td>1,684</td><td>3,157</td></tr><tr><td>Ending cash</td><td>956</td><td>773</td><td>1,684</td><td>3,157</td><td>5,141</td></tr><tr><td>Ending net debt</td><td>2,262</td><td>1,275</td><td>-917</td><td>-3,157</td><td>-5,141</td></tr><tr><td colspan="6">Balance sheet (KRWbn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>956</td><td>773</td><td>1,684</td><td>3,157</td><td>5,141</td></tr><tr><td>Marketable securities</td><td>48</td><td>312</td><td>608</td><td>608</td><td>608</td></tr><tr><td>Accounts receivable</td><td>1,186</td><td>1,422</td><td>1,136</td><td>1,576</td><td>1,678</td></tr><tr><td>Inventories</td><td>452</td><td>490</td><td>734</td><td>791</td><td>808</td></tr><tr><td>Other current assets</td><td>6,728</td><td>4,411</td><td>5,701</td><td>6,142</td><td>6,274</td></tr><tr><td>Total current assets</td><td>9,370</td><td>7,407</td><td>9,863</td><td>12,273</td><td>14,510</td></tr><tr><td>LT investments</td><td>1,680</td><td>1,532</td><td>2,376</td><td>2,376</td><td>2,376</td></tr><tr><td>Fixed assets</td><td>5,116</td><td>5,107</td><td>4,984</td><td>4,581</td><td>4,258</td></tr><tr><td>Goodwill</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other intangible assets</td><td>28</td><td>32</td><td>32</td><td>28</td><td>24</td></tr><tr><td>Other LT assets</td><td>1,001</td><td>871</td><td>844</td><td>909</td><td>929</td></tr><tr><td>Total assets</td><td>17,195</td><td>14,949</td><td>18,099</td><td>20,167</td><td>22,097</td></tr><tr><td>Short-term debt</td><td>3,081</td><td>1,732</td><td>766</td><td>0</td><td>0</td></tr><tr><td>Accounts payable</td><td>946</td><td>1,023</td><td>1,286</td><td>1,488</td><td>1,421</td></tr><tr><td>Other current liabilities</td><td>8,002</td><td>6,668</td><td>8,651</td><td>9,321</td><td>9,522</td></tr><tr><td>Total current liabilities</td><td>12,029</td><td>9,422</td><td>10,703</td><td>10,808</td><td>10,943</td></tr><tr><td>Long-term debt</td><td>137</td><td>316</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>1,279</td><td>1,116</td><td>1,961</td><td>2,113</td><td>2,158</td></tr><tr><td>Total liabilities</td><td>13,445</td><td>10,854</td><td>12,664</td><td>12,921</td><td>13,101</td></tr><tr><td>Minority interest</td><td>-45</td><td>-54</td><td>-65</td><td>-74</td><td>-83</td></tr><tr><td>Preferred stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Common stock</td><td>880</td><td>880</td><td>880</td><td>880</td><td>880</td></tr><tr><td>Retained earnings</td><td>-2,136</td><td>-1,603</td><td>-515</td><td>1,305</td><td>3,063</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td>5,051</td><td>4,872</td><td>5,135</td><td>5,135</td><td>5,135</td></tr><tr><td>Total shareholders&#x27; equity</td><td>3,795</td><td>4,149</td><td>5,500</td><td>7,320</td><td>9,078</td></tr><tr><td>Total equity &amp; liabilities</td><td>17,195</td><td>14,949</td><td>18,099</td><td>20,167</td><td>22,097</td></tr><tr><td colspan="6">Liquidity (x)</td></tr><tr><td>Current ratio</td><td>0.78</td><td>0.79</td><td>0.92</td><td>1.14</td><td>1.33</td></tr><tr><td>Interest cover</td><td>2.6</td><td>7.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="6">Leverage</td></tr><tr><td>Net debt/EBITDA (x)</td><td>2.84</td><td>1.11</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>59.6</td><td>30.7</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td colspan="6">Per share</td></tr><tr><td>Reported EPS (KRW)</td><td>73</td><td>620</td><td>1,236</td><td>2,

[中间内容因长度限制已省略]

rofessional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved.
"""
