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
EQUITY: HANDSETS

# Faster progress in CPO FA

## More concrete progress in CPO components to mark a step closer to mass production; maintain Buy

## Action: Maintain Buy; TP raised to TWD6,000, implying \~52% upside

We believe Largan's conviction in fiber array (FA) mass production has become stronger than it was during the COMPUTEX (report). We fine-tune our 2026/27F earnings by -2.4%/-2.4% as we bake in FX fluctuations, and recent price hikes by Apple (AAPL US, Not rated) for its end products temporarily hurting demand; however, we raise our 2028F earnings by 2.3% to reflect an accelerated pace of iPhone camera/lens upgrades from 2H27F to 2028F. We maintain our Buy rating and raise TP to TWD6,000, based on 25x 2028F EPS of TWD240.0 (previously: TWD4,310, based on 20x 2027F EPS of TWD215.5). We shift our valuation base to 2028F, as we believe visibility on more camera/lens upgrades in iPhones has improved, and thus raise our target P/E from 20x to 25x to reflect Largan's better-than-expected progress on CPO FA mass production. The target P/E of 25x is at the high end of the stock's historical trading band (10-25x) since 2015. Largan trades at 18x 2027F P/E.

One anchor client for CPO FA, likely mass production by mid-2027F at the earliest Largan has secured one client for one-row FA product, aiming to kick off a pilot run by Sep 2026E. The mass production could start in mid-2027 at the earliest, and Largan plans to leverage its full automation capability to help with volume scale-up and more efficient troubleshooting as well as high-precision alignment for FA. Engagements with other clients at this moment are primarily PoC for next-gen products. Largan has noted that its focus is on grating coupling (GC) FA, and that it is unaffected by Corning's (GLW US, Not rated) GlassBridge for edge coupling (EC); Largan believes GC is the mainstream design route.

Largan also has prism/microlens array (PMLA) for CPO based on molding glass, but it appears to have a lower priority than FA. The company notes that molding glass offers less insertion loss than metalens alternatives but acknowledges another competitive prism solution on quartz glass using semiconductor-grade fabrication to demonstrate a better cost structure and absence of thermal effect.

## More intense iPhone camera/lens upgrades in 2027-28F

Beyond variable aperture (VA) adoption in flagship iPhone main camera in 2026F, we expect an enhanced VA camera in 2027F in which Largan could address blades on top of lens, and the main camera may further improve the resolution in 2028F. We also expect a more complicated periscope camera designs in 2027F to enable inner zooming with higher resolutions, and Largan should benefit from its technology leadership.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (TWD)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>61,148</td><td>66,520</td><td>65,936</td><td>74,234</td><td>72,266</td><td>79,402</td><td>80,815</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>21,275</td><td>25,583</td><td>24,968</td><td>28,764</td><td>28,070</td><td>30,690</td><td>31,381</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>21,275</td><td>25,583</td><td>24,968</td><td>28,764</td><td>28,070</td><td>30,690</td><td>31,381</td><td></td></tr><tr><td>FD normalised EPS</td><td>159.40</td><td>191.68</td><td>190.75</td><td>215.51</td><td>214.68</td><td>229.94</td><td>240.01</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>-17.9</td><td>20.2</td><td>19.7</td><td>12.4</td><td>12.5</td><td>6.7</td><td>11.8</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>24.8</td><td>-</td><td>20.7</td><td>-</td><td>18.4</td><td>-</td><td>16.5</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>12.8</td><td>-</td><td>11.5</td><td>-</td><td>9.9</td><td>-</td><td>8.5</td><td></td></tr><tr><td>Price/book (x)</td><td>2.8</td><td>-</td><td>2.8</td><td>-</td><td>2.6</td><td>-</td><td>2.4</td><td></td></tr><tr><td>Dividend yield (%)</td><td>2.2</td><td>-</td><td>2.4</td><td>-</td><td>2.8</td><td>-</td><td>3.2</td><td></td></tr><tr><td>ROE (%)</td><td>11.4</td><td>13.4</td><td>13.1</td><td>14.5</td><td>14.2</td><td>14.5</td><td>14.8</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Increased from
TWD 4,310.00
TWD 6,000.00

Closing price 9 July 2026 TWD 3,950.00

<table><tr><td>Implied upside</td><td>+51.9%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>16,077.6</td></tr><tr><td>ADT (USD mn)</td><td>285.1</td></tr></table>

## Relative performance chart

![](images/8ff4a6b19b4f2b8bae87e9195d91c648431dc47abcb4e4419089c4657725e596.jpg)  
Source: LSEG, NOM

## Research Analysts

Taiwan Technology/Hardware

Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

Eric Chen, CFA - NITB
eric.chen@NOM.com
+886(2) 21769965

Carol Hu - NITB
carol.r.hu@NOM.com
+886(2) 21769963

## Key data on Largan Precision

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (TWD)</td><td>1.7</td><td>73.2</td><td>80.8</td><td>M cap (USDmn)</td><td>16,077.6</td></tr><tr><td>Absolute (USD)</td><td>-0.3</td><td>71.3</td><td>63.7</td><td>Free float (%)</td><td>69.6</td></tr><tr><td>Rel to TaiwanTAIEX Index</td><td>-0.6</td><td>42.1</td><td>-22.2</td><td>3-mth ADT (USDmn)</td><td>285.1</td></tr></table>

<table><tr><td colspan="6">Income statement (TWDmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>59,458</td><td>61,148</td><td>65,936</td><td>72,266</td><td>80,815</td></tr><tr><td>Cost of goods sold</td><td>-28,248</td><td>-30,311</td><td>-32,746</td><td>-34,859</td><td>-38,775</td></tr><tr><td>Gross profit</td><td>31,209</td><td>30,837</td><td>33,190</td><td>37,407</td><td>42,040</td></tr><tr><td>SG&amp;A</td><td>-7,177</td><td>-7,279</td><td>-7,783</td><td>-8,393</td><td>-8,932</td></tr><tr><td>Employee share expense</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Operating profit</td><td>24,033</td><td>23,558</td><td>25,407</td><td>29,013</td><td>33,108</td></tr><tr><td>EBITDA</td><td>30,262</td><td>31,290</td><td>34,349</td><td>39,022</td><td>44,184</td></tr><tr><td>Depreciation</td><td>-6,230</td><td>-7,732</td><td>-8,942</td><td>-10,009</td><td>-11,076</td></tr><tr><td>Amortisation</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>EBIT</td><td>24,033</td><td>23,558</td><td>25,407</td><td>29,013</td><td>33,108</td></tr><tr><td>Net interest expense</td><td>4,404</td><td>4,259</td><td>4,370</td><td>4,800</td><td>4,800</td></tr><tr><td>Associates &amp; JCEs</td><td>117</td><td>212</td><td>89</td><td>80</td><td>80</td></tr><tr><td>Other income</td><td>3,621</td><td>-2,129</td><td>807</td><td>800</td><td>800</td></tr><tr><td>Earnings before tax</td><td>32,174</td><td>25,900</td><td>30,674</td><td>34,693</td><td>38,788</td></tr><tr><td>Income tax</td><td>-5,963</td><td>-4,340</td><td>-5,600</td><td>-6,624</td><td>-7,407</td></tr><tr><td>Net profit after tax</td><td>26,211</td><td>21,560</td><td>25,074</td><td>28,070</td><td>31,381</td></tr><tr><td>Minority interests</td><td>-296</td><td>-285</td><td>-105</td><td>0</td><td>0</td></tr><tr><td>Other items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Normalised NPAT</td><td>25,915</td><td>21,275</td><td>24,968</td><td>28,070</td><td>31,381</td></tr><tr><td>Extraordinary items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Reported NPAT</td><td>25,915</td><td>21,275</td><td>24,968</td><td>28,070</td><td>31,381</td></tr><tr><td>Dividends</td><td>-10,811</td><td>-11,412</td><td>-12,446</td><td>-14,894</td><td>-16,762</td></tr><tr><td>Transfer to reserves</td><td>15,104</td><td>9,864</td><td>12,522</td><td>13,176</td><td>14,619</td></tr><tr><td colspan="6">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td>20.3</td><td>24.8</td><td>20.7</td><td>18.4</td><td>16.5</td></tr><tr><td>Normalised P/E (x)</td><td>20.3</td><td>24.8</td><td>20.7</td><td>18.4</td><td>16.5</td></tr><tr><td>FD normalised P/E (x)</td><td>20.3</td><td>24.8</td><td>20.7</td><td>18.4</td><td>16.5</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>2.2</td><td>2.4</td><td>2.8</td><td>3.2</td></tr><tr><td>Price/cashflow (x)</td><td>16.7</td><td>20.2</td><td>17.2</td><td>16.0</td><td>14.6</td></tr><tr><td>Price/book (x)</td><td>2.9</td><td>2.8</td><td>2.8</td><td>2.6</td><td>2.4</td></tr><tr><td>EV/EBITDA (x)</td><td>13.3</td><td>12.8</td><td>11.5</td><td>9.9</td><td>8.5</td></tr><tr><td>EV/EBIT (x)</td><td>16.8</td><td>16.9</td><td>15.6</td><td>13.3</td><td>11.4</td></tr><tr><td>Gross margin (%)</td><td>52.5</td><td>50.4</td><td>50.3</td><td>51.8</td><td>52.0</td></tr><tr><td>EBITDA margin (%)</td><td>50.9</td><td>51.2</td><td>52.1</td><td>54.0</td><td>54.7</td></tr><tr><td>EBIT margin (%)</td><td>40.4</td><td>38.5</td><td>38.5</td><td>40.1</td><td>41.0</td></tr><tr><td>Net margin (%)</td><td>43.6</td><td>34.8</td><td>37.9</td><td>38.8</td><td>38.8</td></tr><tr><td>Effective tax rate (%)</td><td>18.5</td><td>16.8</td><td>18.3</td><td>19.1</td><td>19.1</td></tr><tr><td>Dividend payout (%)</td><td>41.7</td><td>53.6</td><td>49.8</td><td>53.1</td><td>53.4</td></tr><tr><td>ROE (%)</td><td>14.8</td><td>11.4</td><td>13.1</td><td>14.2</td><td>14.8</td></tr><tr><td>ROA (pretax %)</td><td>25.4</td><td>22.9</td><td>23.2</td><td>24.9</td><td>27.3</td></tr><tr><td colspan="6">Growth (%)</td></tr><tr><td>Revenue</td><td>21.7</td><td>2.8</td><td>7.8</td><td>9.6</td><td>11.8</td></tr><tr><td>EBITDA</td><td>30.3</td><td>3.4</td><td>9.8</td><td>13.6</td><td>13.2</td></tr><tr><td>Normalised EPS</td><td>44.8</td><td>-17.9</td><td>19.7</td><td>12.5</td><td>11.8</td></tr><tr><td>Normalised FDEPS</td><td>44.8</td><td>-17.9</td><td>19.7</td><td>12.5</td><td>11.8</td></tr></table>

Source: Company data, NOM estimates

Cashflow statement (TWDmn)

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>30,262</td><td>31,290</td><td>34,349</td><td>39,022</td><td>44,184</td></tr><tr><td>Change in working capital</td><td>-948</td><td>-1,472</td><td>6,659</td><td>-2,205</td><td>-1,949</td></tr><tr><td>Other operating cashflow</td><td>2,264</td><td>-3,738</td><td>-10,883</td><td>-4,472</td><td>-6,856</td></tr><tr><td>Cashflow from operations</td><td>31,579</td><td>26,080</td><td>30,126</td><td>32,345</td><td>35,378</td></tr><tr><td>Capital expenditure</td><td>-11,126</td><td>-12,338</td><td>-8,341</td><td>-8,000</td><td>-8,000</td></tr><tr><td>Free cashflow</td><td>20,453</td><td>13,743</td><td>21,785</td><td>24,345</td><td>27,378</td></tr><tr><td>Reduction in investments</td><td>-7,374</td><td>-1,704</td><td>-1,022</td><td>0</td><td>0</td></tr><tr><td>Net acquisitions</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Dec in other LT assets</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Inc in other LT liabilities</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adjustments</td><td>2,434</td><td>4,805</td><td>951</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>15,512</td><td>16,845</td><td>21,714</td><td>24,345</td><td>27,378</td></tr><tr><td>Cash dividends</td><td>-10,811</td><td>-11,412</td><td>-12,446</td><td>-14,894</td><td>-16,762</td></tr><tr><td>Equity issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>212</td><td>-212</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>1,255</td><td>-2,937</td><td>-3,824</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-9,344</td><td>-14,561</td><td>-16,270</td><td>-14,894</td><td>-16,762</td></tr><tr><td>Net cashflow</td><td>6,168</td><td>2,283</td><td>5,444</td><td>9,451</td><td>10,616</td></tr><tr><td>Beginning cash</td><td>107,490</td><td>113,658</td><td>115,942</td><td>121,386</td><td>130,837</td></tr><tr><td>Ending cash</td><td>113,658</td><td>115,942</td><td>121,386</td><td>130,837</td><td>141,453</td></tr><tr><td>Ending net debt</td><td>-113,455</td><td>-115,942</td><td>-121,386</td><td>-130,837</td><td>-141,453</td></tr></table>

<table><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>113,658</td><td>115,942</td><td>121,386</td><td>130,837</td><td>141,453</td></tr><tr><td>Marketable securities</td><td>9,961</td><td>15,353</td><td>16,941</td><td>16,941</td><td>16,941</td></tr><tr><td>Accounts receivable</td><td>11,307</td><td>11,454</td><td>14,115</td><td>15,859</td><td>17,364</td></tr><tr><td>Inventories</td><td>5,733</td><td>6,713</td><td>10,406</td><td>11,431</td><td>12,419</td></tr><tr><td>Other current assets</td><td>5,105</td><td>4,823</td><td>5,048</td><td>5,048</td><td>5,048</td></tr><tr><td>Total current assets</td><td>145,764</td><td>154,285</td><td>167,896</td><td>180,115</td><td>193,225</td></tr><tr><td>LT investments</td><td>12,460</td><td>8,517</td><td>9,984</td><td>10,064</td><td>10,144</td></tr><tr><td>Fixed assets</td><td>46,936</td><td>51,472</td><td>50,974</td><td>48,965</td><td>45,889</td></tr><tr><td>Goodwill</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other intangible assets</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other LT assets</td><td>11,367</td><td>6,512</td><td>7,434</td><td>10,885</td><td>15,936</td></tr><tr><td>Total assets</td><td>216,527</td><td>220,787</td><td>236,288</td><td>250,029</td><td>265,194</td></tr><tr><td>Short-term debt</td><td>203</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Accounts payable</td><td>25,100</td><td>25,243</td><td>33,258</td><td>33,258</td><td>33,258</td></tr><tr><td>Other current liabilities</td><td>5,275</td><td>4,506</td><td>9,727</td><td>10,291</td><td>10,834</td></tr><tr><td>Total current liabilities</td><td>30,578</td><td>29,749</td><td>42,986</td><td>43,549</td><td>44,093</td></tr><tr><td>Long-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other LT liabilities</td><td>561</td><td>171</td><td>228</td><td>230</td><td>232</td></tr><tr><td>Total liabilities</td><td>31,139</td><td>29,919</td><td>43,214</td><td>43,779</td><td>44,325</td></tr><tr><td>Minority interest</td><td>1,869</td><td>2,001</td><td>2,110</td><td>2,110</td><td>2,110</td></tr><tr><td>Preferred stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Common stock</td><td>1,335</td><td>1,335</td><td>1,335</td><td>1,335</td><td>1,335</td></tr><tr><td>Retained earnings</td><td>148,623</td><td>153,570</td><td>155,702</td><td>168,878</td><td>183,497</td></tr><tr><td>Proposed dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other equity and reserves</td><td>33,561</td><td>33,963</td><td>33,927</td><td>33,927</td><td>33,927</td></tr><tr><td>Total shareholders&#x27; equity</td><td>183,519</td><td>188,867</td><td>190,964</td><td>204,140</td><td>218,759</td></tr><tr><td>Total equity &amp; liabilities</td><td>216,527</td><td>220,787</td><td>236,288</td><td>250,029</td><td>265,194</td></tr><tr><td colspan="6">Liquid

[中间内容因长度限制已省略]

nal Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Taipei Branch, Taiwan. All rights reserved.
"""
