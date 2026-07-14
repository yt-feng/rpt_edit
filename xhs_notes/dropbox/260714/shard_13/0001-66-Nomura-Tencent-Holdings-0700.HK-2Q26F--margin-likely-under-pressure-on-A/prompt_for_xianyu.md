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
# 2Q26F: margin likely under pressure on AI investment

AI initiatives show promise, yet it is premature to declare victory; maintain Buy

2Q26F: Expecting in-line revenue and slightly lower profits; maintain Buy
For 2Q26F, we forecast a 10% y-y increase in revenue to CNY203bn, in line with the Bloomberg consensus forecast. We estimate non-IFRS net profit rose 6% y-y to CNY67bn, 3% below the consensus of CNY69bn. Our forecast non-IFRS operating margin (OPM) retreated 0.4pp y-y to 37.1% due to ramped-up AI investments, slightly below the consensus of 37.4% (Fig. 1).

Across business segments, online gaming likely rose 10% y-y to CNY65.3bn, backed by an 11% y-y increase in domestic gaming and an 8% y-y increase in overseas gaming revenue. Advertising revenue likely increased 18% y-y, driven by Video Account ads. The fintech and business segment (FBS) likely increased 9% y-y, of which business segment revenue likely rose 22% y-y, accelerating from 20% in 1Q26, driven by the Tencent Cloud business.

We trim FY26 and FY27 non-IFRS net profit estimates by 2% and 1%, respectively, reflecting our lowered margin assumptions as we consider its ongoing AI investments. We maintain our Buy rating with an unchanged sum-of-the-parts (SOTP) based target price of HKD727, implying an FY27F P/E of 20x, versus the current 12.7x.

Hy LLM, WorkBuddy, and WeChat agent highlight Tencent's core AI strategy Tencent has made encouraging progress on the AI front over the past few months. The company launched the official version of Hy 3.0 in early July, which has been widely recognized by developers for its meaningful improvements over the April preview version. The preliminary success of Hy 3.0 reinforces our view that Tencent is well-positioned to close the gap with current AI leaders.

WorkBuddy has gained impressive traction with white-collar and student users. Analysys, a third-party research firm, reported that WorkBuddy was the most popular desktop AI agent in China as of March 2026, with monthly visits reaching 8.85mn. However, the survey also noted a highly crowded field, as major AI platforms—notably Alibaba (BABA US, Buy) and ByteDance (unlisted) — have all launched competing desktop agents. Competition will likely remain fierce in the coming months, given that Chinese online consumers typically exhibit low switching costs and a lower willingness to pay. Currently, no desktop agent has established a definitive lead among enterprise users.

(Continued on page 4...)

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>751,766</td><td>828,516</td><td>827,308</td><td>906,572</td><td>905,255</td><td>990,470</td><td>989,061</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>224,842</td><td>233,794</td><td>229,418</td><td>251,553</td><td>247,467</td><td>273,814</td><td>272,640</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>259,626</td><td>278,671</td><td>274,240</td><td>302,018</td><td>297,871</td><td>330,434</td><td>329,195</td><td></td></tr><tr><td>FD normalised EPS</td><td>27.89</td><td>30.24</td><td>29.76</td><td>33.10</td><td>32.65</td><td>36.58</td><td>36.45</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>18.6</td><td>8.4</td><td>6.7</td><td>9.5</td><td>9.7</td><td>10.5</td><td>11.6</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>15.2</td><td>-</td><td>13.9</td><td>-</td><td>12.7</td><td>-</td><td>11.3</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>14.0</td><td>-</td><td>12.8</td><td>-</td><td>11.3</td><td>-</td><td>10.0</td><td></td></tr><tr><td>Price/book (x)</td><td>3.3</td><td>-</td><td>2.7</td><td>-</td><td>2.4</td><td>-</td><td>2.1</td><td></td></tr><tr><td>Dividend yield (%)</td><td>1.1</td><td>-</td><td>1.2</td><td>-</td><td>1.3</td><td>-</td><td>1.5</td><td></td></tr><tr><td>ROE (%)</td><td>21.1</td><td>18.4</td><td>18.1</td><td>16.9</td><td>16.7</td><td>16.1</td><td>16.1</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>9.7</td><td>1.1</td><td>1.5</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Remains
HKD 727.00

Closing price 10 July 2026 HKD 460.20

<table><tr><td>Implied upside</td><td>+58.0%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>533,748.6</td></tr><tr><td>ADT (USD mn)</td><td>1,873.0</td></tr></table>

## Relative performance chart

![](images/f862fc336bd6e5d5a812e098ee06b8e88340b688840e55e528bf8b5996a1ad55.jpg)  
Source: LSEG, NOM

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK

Jialong.shi@NOM.com +852 2252 1409

Rachel Guo - NIHK
rachel.guo@NOM.com
+852 2252 1400

## Key data on Tencent Holdings

Cashflow statement (CNYmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (HKD)</td><td>-1.2</td><td>-8.8</td><td>-7.3</td><td>M cap (USDmn)</td><td>533,748.6</td></tr><tr><td>Absolute (USD)</td><td>-1.2</td><td>-8.9</td><td>-7.2</td><td>Free float (%)</td><td>60.0</td></tr><tr><td>Rel to Hang Seng Index</td><td>-0.2</td><td>-2.1</td><td>-7.9</td><td>3-mth ADT (USDmn)</td><td>1,873.0</td></tr></table>

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>660,257</td><td>751,766</td><td>827,308</td><td>905,255</td><td>989,061</td></tr><tr><td>Cost of goods sold</td><td>-311,011</td><td>-329,173</td><td>-354,198</td><td>-383,934</td><td>-418,827</td></tr><tr><td>Gross profit</td><td>349,246</td><td>422,593</td><td>473,111</td><td>521,321</td><td>570,235</td></tr><tr><td>SG&amp;A</td><td>-121,919</td><td>-143,143</td><td>-179,383</td><td>-202,621</td><td>-217,423</td></tr><tr><td>Employee share expense</td><td>-27,230</td><td>-34,711</td><td>-38,199</td><td>-41,798</td><td>-45,668</td></tr><tr><td>Operating profit</td><td>200,097</td><td>244,739</td><td>255,529</td><td>276,902</td><td>307,144</td></tr><tr><td>EBITDA</td><td>256,310</td><td>310,767</td><td>321,713</td><td>349,323</td><td>386,269</td></tr><tr><td>Depreciation</td><td>-27,332</td><td>-32,799</td><td>-24,819</td><td>-27,158</td><td>-29,672</td></tr><tr><td>Amortisation</td><td>-28,881</td><td>-33,229</td><td>-41,365</td><td>-45,263</td><td>-49,453</td></tr><tr><td>EBIT</td><td>200,097</td><td>244,739</td><td>255,529</td><td>276,902</td><td>307,144</td></tr><tr><td>Net interest expense</td><td>3,557</td><td>3,453</td><td>4,133</td><td>4,887</td><td>5,723</td></tr><tr><td>Associates &amp; JCEs</td><td>25,176</td><td>23,740</td><td>18,674</td><td>18,829</td><td>18,829</td></tr><tr><td>Other income</td><td>8,468</td><td>-4,851</td><td>2,600</td><td>2,600</td><td>2,600</td></tr><tr><td>Earnings before tax</td><td>237,298</td><td>267,081</td><td>280,936</td><td>303,219</td><td>334,297</td></tr><tr><td>Income tax</td><td>-45,018</td><td>-47,448</td><td>-54,518</td><td>-58,752</td><td>-64,656</td></tr><tr><td>Net profit after tax</td><td>192,280</td><td>219,633</td><td>226,418</td><td>244,467</td><td>269,640</td></tr><tr><td>Minorities</td><td>-2,394</td><td>-4,959</td><td>-3,000</td><td>-3,000</td><td>-3,000</td></tr><tr><td>Other items</td><td>32,817</td><td>44,952</td><td>50,822</td><td>56,404</td><td>62,555</td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>222,703</td><td>259,626</td><td>274,240</td><td>297,871</td><td>329,195</td></tr><tr><td>Extraordinary items</td><td>-28,630</td><td>-34,784</td><td>-44,822</td><td>-50,404</td><td>-56,555</td></tr><tr><td>Reported NPAT</td><td>194,073</td><td>224,842</td><td>229,418</td><td>247,467</td><td>272,640</td></tr><tr><td>Dividends</td><td>-37,907</td><td>-44,041</td><td>-46,105</td><td>-50,584</td><td>-56,467</td></tr><tr><td>Transfer to reserves</td><td>156,166</td><td>180,801</td><td>183,313</td><td>196,884</td><td>216,173</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>20.7</td><td>17.6</td><td>16.6</td><td>15.2</td><td>13.7</td></tr><tr><td>Normalised P/E (x)</td><td>18.1</td><td>15.2</td><td>13.9</td><td>12.7</td><td>11.3</td></tr><tr><td>FD normalised P/E (x)</td><td>18.1</td><td>15.2</td><td>13.9</td><td>12.7</td><td>11.3</td></tr><tr><td>Dividend yield (%)</td><td>1.0</td><td>1.1</td><td>1.2</td><td>1.3</td><td>1.5</td></tr><tr><td>Price/cashflow (x)</td><td>15.6</td><td>13.0</td><td>12.1</td><td>9.9</td><td>10.6</td></tr><tr><td>Price/book (x)</td><td>4.1</td><td>3.3</td><td>2.7</td><td>2.4</td><td>2.1</td></tr><tr><td>EV/EBITDA (x)</td><td>16.9</td><td>14.0</td><td>12.8</td><td>11.3</td><td>10.0</td></tr><tr><td>EV/EBIT (x)</td><td>21.7</td><td>17.8</td><td>16.1</td><td>14.3</td><td>12.5</td></tr><tr><td>Gross margin (%)</td><td>52.9</td><td>56.2</td><td>57.2</td><td>57.6</td><td>57.7</td></tr><tr><td>EBITDA margin (%)</td><td>38.8</td><td>41.3</td><td>38.9</td><td>38.6</td><td>39.1</td></tr><tr><td>EBIT margin (%)</td><td>30.3</td><td>32.6</td><td>30.9</td><td>30.6</td><td>31.1</td></tr><tr><td>Net margin (%)</td><td>29.4</td><td>29.9</td><td>27.7</td><td>27.3</td><td>27.6</td></tr><tr><td>Effective tax rate (%)</td><td>19.0</td><td>17.8</td><td>19.4</td><td>19.4</td><td>19.3</td></tr><tr><td>Dividend payout (%)</td><td>19.5</td><td>19.6</td><td>20.1</td><td>20.4</td><td>20.7</td></tr><tr><td>ROE (%)</td><td>21.8</td><td>21.1</td><td>18.1</td><td>16.7</td><td>16.1</td></tr><tr><td>ROA (pretax %)</td><td>14.8</td><td>15.1</td><td>13.9</td><td>13.9</td><td>14.2</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>8.4</td><td>13.9</td><td>10.0</td><td>9.4</td><td>9.3</td></tr><tr><td>EBITDA</td><td>19.6</td><td>21.2</td><td>3.5</td><td>8.6</td><td>10.6</td></tr><tr><td>Normalised EPS</td><td>44.5</td><td>18.6</td><td>6.7</td><td>9.7</td><td>11.6</td></tr><tr><td>Normalised FDEPS</td><td>44.5</td><td>18.6</td><td>6.7</td><td>9.7</td><td>11.6</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>256,310</td><td>310,767</td><td>321,713</td><td>349,323</td><td>386,269</td></tr><tr><td>Change in working capital</td><td>22,863</td><td>-20,825</td><td>-16,538</td><td>60,870</td><td>-9,268</td></tr><tr><td>Other operating cashflow</td><td>-20,652</td><td>13,110</td><td>10,133</td><td>-29,448</td><td>-24,410</td></tr><tr><td>CF from operations</td><td>258,521</td><td>303,052</td><td>315,308</td><td>380,745</td><td>352,590</td></tr><tr><td>Capital expenditure</td><td>-62,927</td><td>-87,482</td><td>-115,823</td><td>-135,788</td><td>-148,359</td></tr><tr><td>Free cashflow</td><td>195,594</td><td>215,570</td><td>199,485</td><td>244,956</td><td>204,231</td></tr><tr><td>Reduction in investments</td><td>-6,994</td><td>-43,824</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-180,662</td><td>-79,119</td><td>-61,422</td><td>-62,493</td><td>-63,608</td></tr><tr><td>Inc in other LT liabilities</td><td>-17,721</td><td>158</td><td>21,834</td><td>24,848</td><td>28,298</td></tr><tr><td>Adjustments</td><td>146,117</td><td>4,535</td><td>-24,001</td><td>-28,671</td><td>-33,940</td></tr><tr><td>CF after investing acts</td><td>136,334</td><td>97,320</td><td>135,897</td><td>178,639</td><td>134,981</td></tr><tr><td>Cash dividends</td><td>-31,244</td><td>-39,907</td><td>-44,041</td><td>-46,105</td><td>-50,584</td></tr><tr><td>Equity issue</td><td>1,932</td><td>2,721</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>-107</td><td>-107</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>-146,716</td><td>-51,505</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-176,135</td><td>-88,798</td><td>-44,041</td><td>-46,105</td><td>-50,584</td></tr><tr><td>Net cashflow</td><td>-39,801</td><td>8,522</td><td>91,856</td><td>132,535</td><td>84,398</td></tr><tr><td>Beginning cash</td><td>172,320</td><td>132,519</td><td>141,041</td><td>232,897</td><td>365,431</td></tr><tr><td>Ending cash</td><td>132,519</td><td>141,041</td><td>232,897</td><td>365,431</td><td>449,829</td></tr><tr><td>Ending net debt</td><td>76,123</td><td>112,156</td><td>20,300</td><td>-112,234</td><td>-196,632</td></tr></table>

<table><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>132,519</td><td>141,041</td><td>232,897</td><td>365,431</td><td>449,829</td></tr><tr><td>Marketable securities</td><td>192,977</td><td>236,801</td><td>236,801</td><td>236,801</td><td>236,801</td></tr><tr><td>Accounts receivable</td><td>48,203</td><td>49,930</td><td>54,334</td><td>59,753</td><td>64,895</td></tr><tr><td>Inventories</td><td>440</td><td>530</td><td>530</td><td>530</td><td>530</td></tr><tr><td>Other current assets</td><td>122,041</td><td>167,158</td><td>167,158</td><td>167,158</td><td>167,158</td></tr><tr><td>Total current assets</td><td>496,180</td><td>595,460</td><td>691,719</td><td>829,674</td><td>919,213</td></tr><tr><td>LT investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Fixed assets</td><td>80,185</td><td>149,905</td><td>240,909</td><td>349,540</td><td>468,227</td></tr><tr><td colspan="6">Goodwill</td></tr><tr><td>Other intangible assets</td><td>196,127</td><td>205,999</td><td>193,589</td><td>180,011</td><td>165,175</td></tr><tr><td>Other LT assets</td><td>1,008,503</td><td>1,087,622</td><td>1,149,044</td><td>1,211,537</td><td>1,275,144</td></tr><tr><td>Total assets</td><td>1,780,995</td><td>2,038,986</td><td>2,275,261</td><td>2,570,761</td><td>2,827,759</td></tr><tr><td>Short-term debt</td><td>52,885</td><td>42,618</td><td>42,618</td><td>42,618</td><td>42,618</td></tr><tr><td>Accounts payable</td><td>118,712</td><td>121,127</td><td>92,362</td><td>139,050</td><td>113,393</td></tr><tr><td>Other current liabilities</td><td>225,312</td><td>249,006</td><td>265,636</td><td>285,238</td><td>306,768</td></tr><tr><td>Total current liabilities</td><td>396,909</td><td>412,751</td><td>400,616</td><td>466,906</td><td>462,779</td></tr><tr><td>Long-term debt</td><td>149,521</td><td>208,369</td><td>208,369</td><td>208,369</td><td>208,369</td></tr><tr><td>Convertible debt</td><td>6,236</td><td>2,210</td><td>2,210</td><td>2,210</td><td>2,210</td></tr><tr><td>Other LT liabilities</td><td>174,433</td><td>174,591</td><td>196,425</td><td>221,272</td><td>249,570</td></tr><tr><td>Total liabilities</td><td>727,099</td><td>797,921</td><td>807,620</td><td>898,757</td><td>922,929</td></tr><tr><td>Minority interest</td><td>80,348</td><td>86,913</td><td>89,913</td><td>92,913</td><td>95,913</td></tr><tr><td colspan="6">Preferred stock</td></tr><tr><td>Common stock</td><td>81,518</td><td>143,716</td><td>143,716</td><td>143,716</td><td>143,716</td></tr><tr><td>Retained earnings</td><td>854,123</td><td>966,395</td><td>1,187,907</td><td>1,384,791</td><td>1,608,734</td></tr><tr><td>Proposed dividends</td><td>37,907</td><td>44,041</td><td>46,105</td><td>50,584</td><td>56,467</td></tr><tr><td colspan="6">Other equity and reserves</td></tr><tr><td>Total shareholders&#x27; equity</td><td>973,548</td><td>1,154,152</td><td>1,377,728</td><td>1,579,090</td><td>1,808,918</td></tr><tr><td>Total equity &amp; liabilities</td><td>1,780,995</td><td>2,038,986</td><td>2,275,261</td><td>2

[中间内容因长度限制已省略]

a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
