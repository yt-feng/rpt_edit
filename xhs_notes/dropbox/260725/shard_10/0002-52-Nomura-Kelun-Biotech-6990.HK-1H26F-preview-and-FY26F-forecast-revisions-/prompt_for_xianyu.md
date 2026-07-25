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
EQUITY: HEALTH CARE & PHARMACEUTICALS

# 1H26F preview and FY26F forecast revisions

## We expect sales ramp-up and big non-recurring income in 1H26F and anticipate more clinical catalysts in 2H26F

We forecast 1H26F revenue reached CNY1.41bn, up +48.4%, along with a positive earnings book of CNY731mn in 1H26F, led by lawsuit settlement payment

We estimate Kelun Biotech will report 1H26F revenue of CNY1.41bn (+48% y-y), on the back of CNY650mn drug sales (mainly from sac-TMT) and CNY750mn collaboration revenue. We think sac-TMT sales is on track to reach management's target of doubling FY25 sales, considering the accelerated sales ramp-up after NRDL inclusion.

On the margins front, we estimate 1H26F gross margin rose 9.1pp y-y to 78.5%. We forecast opex of CNY994mn in 1H26F (15% y-y), considering the sales team expansion.

We anticipate other income reached CNY750mn in 1H26, owing to payment it received from the legal settlement with MediLink Therapeutics (unlisted).

As a result, net profit should turn positive at CNY731mn (vs a loss of CNY145mn in 1H25.

For 2H26F, we forecast revenue to grow 30% y-y to CNY1.44bn, led by continued sac-TMT sales growth. Together with a gross margin of 81.1% and opex of CNY1.0bn (-8.5% y-y), 2H26F net profit will likely come in at CNY206mn (vs a loss of CNY237mn in 2H25).

## Maintain Buy and lift TP from HKD544.42 to HKD612.66

We lower FY26F revenue by 14% but lift earnings estimates by 226%(considering the above-mentioned lawsuit gain), while lifting our mid-term growth estimates, considering the recent smooth clinical development of sat-TMT. (see our reports: Kelun Biotech (6990 HK) (Buy) - Another big win for sac-TMT in upcoming ASCO Quick Note - Kelun Biotech (6990 HK) (Buy) - The first global phase III clinical trial meet primary endpoints, ahead of schedule).

We thus lift our DCF-based (assuming an unchanged WACC of 10.8% and an unchanged terminal growth rate of 4.0%) TP from HKD544.42 to HKD612.66. The stock currently trades at 4.0x FY35F sales of CNY26.8bn.

We think the BLA filing of sac-TMT by Kelun Biotech's overseas partner, Merck (MRK US, Not rated) will be a key monitorable in 2H26.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>2,058</td><td>3,298</td><td>2,851</td><td>4,945</td><td>4,972</td><td>6,252</td><td>6,922</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>-382</td><td>287</td><td>937</td><td>1,021</td><td>999</td><td>1,640</td><td>1,746</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>-382</td><td>287</td><td>937</td><td>1,021</td><td>999</td><td>1,640</td><td>1,746</td><td></td></tr><tr><td>FD normalised EPS</td><td>-1.74</td><td>1.31</td><td>4.26</td><td>4.64</td><td>4.54</td><td>7.45</td><td>7.93</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>–</td><td>–</td><td>–</td><td>255.6</td><td>6.7</td><td>60.6</td><td>74.7</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>–</td><td>–</td><td>109.3</td><td>–</td><td>102.4</td><td>–</td><td>58.6</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>–</td><td>–</td><td>62.9</td><td>–</td><td>17.8</td><td>–</td><td>9.6</td><td></td></tr><tr><td>Price/book (x)</td><td>21.0</td><td>–</td><td>12.5</td><td>–</td><td>11.1</td><td>–</td><td>9.3</td><td></td></tr><tr><td>Dividend yield (%)</td><td>–</td><td>–</td><td>–</td><td>–</td><td>–</td><td>–</td><td>–</td><td></td></tr><tr><td>ROE (%)</td><td>-9.3</td><td>5.7</td><td>14.3</td><td>18.0</td><td>11.5</td><td>23.4</td><td>17.3</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Increased from
HKD 544.42
HKD 612.66

<table><tr><td>Closing price23 July 2026</td><td>HKD 521.50</td></tr></table>

<table><tr><td>Implied upside</td><td>+17.5%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>15,897.7</td></tr><tr><td>ADT (USD mn)</td><td>63.4</td></tr></table>

## Relative performance chart

![](images/04793a31044241c40d0a29a464fdfb4b45e1982369b158e8856751a6af7292af.jpg)  
Source: LSEG, NOM

## Research Analysts

China Health Care & Pharmaceuticals
Jialin Zhang, CFA, CPA - NIHK
jialin.zhang@NOM.com
+852 2252 6134

## Key data on Kelun Biotech

Cashflow statement (CNYmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (HKD)</td><td>31.0</td><td>12.2</td><td>39.1</td><td>M cap (USDmn)</td><td>15,897.7</td></tr><tr><td>Absolute (USD)</td><td>31.0</td><td>12.1</td><td>39.2</td><td>Free float (%)</td><td>69.4</td></tr><tr><td>Rel to Hang Seng Index</td><td>23.0</td><td>15.0</td><td>40.3</td><td>3-mth ADT (USDmn)</td><td>63.4</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>1,933</td><td>2,058</td><td>2,851</td><td>4,972</td><td>6,922</td></tr><tr><td>Cost of goods sold</td><td>-659</td><td>-579</td><td>-575</td><td>-1,071</td><td>-1,429</td></tr><tr><td>Gross profit</td><td>1,274</td><td>1,479</td><td>2,276</td><td>3,901</td><td>5,493</td></tr><tr><td>SG&amp;A</td><td>-1,552</td><td>-1,974</td><td>-2,009</td><td>-2,798</td><td>-3,536</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>-279</td><td>-495</td><td>266</td><td>1,103</td><td>1,957</td></tr><tr><td>EBITDA</td><td>-222</td><td>-385</td><td>353</td><td>1,211</td><td>2,077</td></tr><tr><td>Depreciation</td><td>-56</td><td>-109</td><td>-86</td><td>-105</td><td>-114</td></tr><tr><td>Amortisation</td><td>0</td><td>-1</td><td>-1</td><td>-3</td><td>-6</td></tr><tr><td>EBIT</td><td>-279</td><td>-495</td><td>266</td><td>1,103</td><td>1,957</td></tr><tr><td>Net interest expense</td><td>-4</td><td>-6</td><td>-9</td><td>-15</td><td>-21</td></tr><tr><td>Associates &amp; JCEs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other income</td><td>140</td><td>145</td><td>855</td><td>99</td><td>138</td></tr><tr><td>Earnings before tax</td><td>-143</td><td>-356</td><td>1,113</td><td>1,187</td><td>2,074</td></tr><tr><td>Income tax</td><td>-124</td><td>-26</td><td>-167</td><td>-178</td><td>-311</td></tr><tr><td>Net profit after tax</td><td>-267</td><td>-382</td><td>946</td><td>1,009</td><td>1,763</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>-9</td><td>-10</td><td>-18</td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>-267</td><td>-382</td><td>937</td><td>999</td><td>1,746</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>-267</td><td>-382</td><td>937</td><td>999</td><td>1,746</td></tr><tr><td>Dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Transfer to reserves</td><td>-267</td><td>-382</td><td>937</td><td>999</td><td>1,746</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>-</td><td>-</td><td>109.3</td><td>102.4</td><td>58.6</td></tr><tr><td>Normalised P/E (x)</td><td>-394.6</td><td>-268.0</td><td>109.3</td><td>102.4</td><td>58.6</td></tr><tr><td>FD normalised P/E (x)</td><td>-</td><td>-</td><td>109.3</td><td>102.4</td><td>58.6</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Price/cashflow (x)</td><td>-</td><td>-</td><td>172.1</td><td>102.9</td><td>55.7</td></tr><tr><td>Price/book (x)</td><td>31.8</td><td>21.0</td><td>12.5</td><td>11.1</td><td>9.3</td></tr><tr><td>EV/EBITDA (x)</td><td>-</td><td>-</td><td>62.9</td><td>17.8</td><td>9.6</td></tr><tr><td>EV/EBIT (x)</td><td>-</td><td>-</td><td>83.4</td><td>19.5</td><td>10.2</td></tr><tr><td>Gross margin (%)</td><td>65.9</td><td>71.9</td><td>79.8</td><td>78.5</td><td>79.4</td></tr><tr><td>EBITDA margin (%)</td><td>-11.5</td><td>-18.7</td><td>12.4</td><td>24.4</td><td>30.0</td></tr><tr><td>EBIT margin (%)</td><td>-14.4</td><td>-24.0</td><td>9.3</td><td>22.2</td><td>28.3</td></tr><tr><td>Net margin (%)</td><td>-13.8</td><td>-18.6</td><td>32.9</td><td>20.1</td><td>25.2</td></tr><tr><td>Effective tax rate (%)</td><td>-</td><td>-</td><td>15.0</td><td>15.0</td><td>15.0</td></tr><tr><td>Dividend payout (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>ROE (%)</td><td>-9.5</td><td>-9.3</td><td>14.3</td><td>11.5</td><td>17.3</td></tr><tr><td>ROA (pretax %)</td><td>-11.3</td><td>-17.4</td><td>9.3</td><td>33.6</td><td>51.1</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>25.5</td><td>6.5</td><td>38.5</td><td>74.4</td><td>39.2</td></tr><tr><td>EBITDA</td><td></td><td>-</td><td>-</td><td>242.9</td><td>71.4</td></tr><tr><td>Normalised EPS</td><td></td><td>-</td><td>-</td><td>6.7</td><td>74.7</td></tr><tr><td>Normalised FDEPS</td><td></td><td>-</td><td>-</td><td>6.7</td><td>74.7</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>-222</td><td>-385</td><td>353</td><td>1,211</td><td>2,077</td></tr><tr><td>Change in working capital</td><td>-405</td><td>-58</td><td>-438</td><td>-123</td><td>-46</td></tr><tr><td>Other operating cashflow</td><td>197</td><td>263</td><td>680</td><td>-94</td><td>-193</td></tr><tr><td>Cashflow from operations</td><td>-430</td><td>-180</td><td>595</td><td>995</td><td>1,837</td></tr><tr><td>Capital expenditure</td><td>-77</td><td>-126</td><td>-131</td><td>-178</td><td></td></tr><tr><td>Free cashflow</td><td>-507</td><td>-307</td><td>464</td><td>817</td><td>1,837</td></tr><tr><td>Reduction in investments</td><td>-773</td><td>504</td><td>-123</td><td>-135</td><td>-149</td></tr><tr><td colspan="6">Net acquisitions</td></tr><tr><td>Dec in other LT assets</td><td>-85</td><td>-25</td><td>1</td><td>1</td><td>-11</td></tr><tr><td>Inc in other LT liabilities</td><td>79</td><td>-33</td><td>19</td><td>20</td><td>20</td></tr><tr><td>Adjustments</td><td>34</td><td>91</td><td>-2</td><td>-2</td><td>-170</td></tr><tr><td>CF after investing acts</td><td>-1,252</td><td>231</td><td>359</td><td>700</td><td>1,528</td></tr><tr><td colspan="6">Cash dividends</td></tr><tr><td>Equity issue</td><td>1,094</td><td>1,777</td><td>2,406</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="6">Convertible debt issue</td></tr><tr><td>Others</td><td>-35</td><td>-101</td><td>-1</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>1,060</td><td>1,677</td><td>2,405</td><td>0</td><td>0</td></tr><tr><td>Net cashflow</td><td>-192</td><td>1,907</td><td>2,764</td><td>700</td><td>1,528</td></tr><tr><td>Beginning cash</td><td>1,529</td><td>1,337</td><td>3,244</td><td>6,008</td><td>6,708</td></tr><tr><td>Ending cash</td><td>1,337</td><td>3,244</td><td>6,008</td><td>6,708</td><td>8,236</td></tr><tr><td>Ending net debt</td><td>-1,337</td><td>-3,244</td><td>-6,008</td><td>-6,708</td><td>-8,236</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>1,337</td><td>3,244</td><td>6,008</td><td>6,708</td><td>8,236</td></tr><tr><td>Marketable securities</td><td>1,732</td><td>1,228</td><td>1,351</td><td>1,486</td><td>1,634</td></tr><tr><td>Accounts receivable</td><td>304</td><td>346</td><td>508</td><td>817</td><td>1,043</td></tr><tr><td>Inventories</td><td>111</td><td>241</td><td>142</td><td>235</td><td>274</td></tr><tr><td>Other current assets</td><td>10</td><td>90</td><td>92</td><td>93</td><td>95</td></tr><tr><td>Total current assets</td><td>3,493</td><td>5,149</td><td>8,100</td><td>9,339</td><td>11,283</td></tr><tr><td colspan="6">LT investments</td></tr><tr><td>Fixed assets</td><td>595</td><td>636</td><td>669</td><td>719</td><td>741</td></tr><tr><td colspan="6">Goodwill</td></tr><tr><td>Other intangible assets</td><td>3</td><td>1</td><td>14</td><td>36</td><td>64</td></tr><tr><td>Other LT assets</td><td>178</td><td>203</td><td>202</td><td>202</td><td>213</td></tr><tr><td>Total assets</td><td>4,268</td><td>5,989</td><td>8,986</td><td>10,296</td><td>12,301</td></tr><tr><td>Short-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Accounts payable</td><td>447</td><td>685</td><td>293</td><td>554</td><td>752</td></tr><tr><td>Other current liabilities</td><td>363</td><td>320</td><td>338</td><td>358</td><td>381</td></tr><tr><td>Total current liabilities</td><td>810</td><td>1,004</td><td>631</td><td>912</td><td>1,133</td></tr><tr><td colspan="6">Long-term debt</td></tr><tr><td colspan="6">Convertible debt</td></tr><tr><td>Other LT liabilities</td><td>150</td><td>117</td><td>136</td><td>156</td><td>177</td></tr><tr><td>Total liabilities</td><td>959</td><td>1,121</td><td>767</td><td>1,068</td><td>1,309</td></tr><tr><td>Minority interest</td><td>0</td><td>0</td><td>9</td><td>20</td><td>37</td></tr><tr><td>Preferred stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Common stock</td><td>227</td><td>233</td><td>239</td><td>239</td><td>239</td></tr><tr><td>Retained earnings</td><td>3,081</td><td>4,634</td><td>7,970</td><td>8,970</td><td>10,715</td></tr><tr><td colspan="6">Proposed dividends</td></tr><tr><td colspan="6">Other equity and reserves</td></tr><tr><td>Total shareholders&#x27; equity</td><td>3,309</td><td>4,867</td><td>8,209</td><td>9,209</td><td>10,954</td></tr><tr><td>Total equity &amp; liabilities</td><td>4,268</td><td>5,989</td><td>8,986</td><td>10,296</td><td>12,301</td></tr><tr><td colspan="6">Liquidity (x)</td></tr><tr><td>Current ratio</td><td>4.31</td><td>5.13</td><td>12.85</td><td>10.24</td><td>9.96</td></tr><tr><td>Interest cover</td><td>-73.4</td><td>-80.4</td><td>31.2</td><td>74.1</td><td>94.5</td></tr><tr><td colspan="6">Leverage</td></tr><tr><td>Net debt/EBITDA (x)</td><td>–</td><td>–</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td colspan="6">Per share</td></tr><tr><td>Reported EPS (CNY)</td><td>-1.21</td><td>-1.74</td><td>4.26</td><td>4.54</td><td>7.93</td></tr><tr><td>Norm EPS (CNY)</td><td>-1.21</td><td>-1.74</td><td>4.26</td><td>4.54</td><td>7.93</td></tr><tr><td>FD norm EPS (CNY)</td><td>-1.22</td><td>-1.74</td><td>4.26</td><td>4.54</td><td>7.93</td></tr><tr><td>BVPS (CNY)</td><td>15.03</td><td>22.11</td><td>37.30</td><td>41.84</td><td>49.77</td></tr><tr><td>DPS (CNY)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td colspan="6">Activity (days)</td></tr><tr><td>Days receivable</td><td>49.0</td><td>57.6</td><td>54.6</td><td>48.6</td><td>49.2</td></tr><tr><td>Days inventory</td><td>48.0</td><td>110.7</td><td>121.5</td><td>64.2</td><td>65.2</td></tr><tr><td>Days payable</td><td>268.6</td><td>356.5</td><td>310.3</td><td>144.4</td><td>167.3</td></tr><tr><td>Cash cycle</td><td>-171.6</td><td>-188.2</td><td>-134.2</td><td>-31.6</td><td>-52.9</td></tr></table>

Source: Company data, NOM estimates

## Company profile

Kelun-Biotech is a biopharmaceutical company founded in 2016, It is one of the pioneers in the dev

[中间内容因长度限制已省略]

a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
