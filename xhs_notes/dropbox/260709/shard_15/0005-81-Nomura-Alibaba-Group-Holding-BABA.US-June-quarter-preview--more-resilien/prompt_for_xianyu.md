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
EQUITY: INTERNET & NEW MEDIA

# June quarter preview: more resilient earnings

Robust AI cloud, weak e-commerce; maintain Buy

Stronger cloud offset weaker ecommerce business

As noted in our 24 June report, we expect BABA's June quarter results to be a mixed bag – the company is likely to report weak China ecommerce CMR (customer management revenue), down 8% y-y or up slightly by 1% y-y on a like-for-like basis. However, its China Cloud revenue likely grew 45% y-y, by our estimate, much higher than the Street expectation of 37.5%. We estimate that the ARR (annualized recurring revenue) from its MaaS (Model-as-a-Service) likely surpassed the guidance of CNY10bn, reaching CNY12bn as of the end of the June quarter. We believe BABA's cloud revenue will accelerate further over the next few quarters, while margins for AliCloud should improve further from the current level of 11-12%, driven by price hikes taken earlier this year and the increased revenue share for BABA's higher-margin MaaS business. We think BABA's strength in China's AI cloud industry lies in its all-stack capability with strong position in all the critical fields of the AI value chain, spanning AI chips (T-head), IT infrastructure (operating the largest public cloud platform), LLM platform (Bailian) and, importantly, the advanced proprietary Qwen foundation model. Please see Figs 1-3 for our detailed forecasts for BABA's June quarter results.

## Resilient earnings despite macro headwinds; maintain Buy

In the June quarter, BABA's efforts to steady its earnings despite the weak ecommerce business and continued AI investment should be viewed positively by the market. We estimate that its China ecommerce EBITA (excluding quick commerce [QC]) likely declined by just 3% y-y to CNY48bn despite an 8% drop in CMR, while the loss of QC likely narrowed significantly to CNY10.3bn (vs. a loss of CNY18bn one quarter earlier) compared with the market expectation for a CNY12-13bn loss. Its international commerce, AIDC, likely swung into a profit with EBITA of CNY658mn, from a slight loss a year ago. We estimate the overall ecommerce segment (including China and overseas ecommerce) will report stable (y-y) EBITA of CNY38bn in the June quarter, above the Bloomberg consensus estimate of CNY36bn. The loss for BABA's "all others" segment likely came in at CNY15.8bn, narrowing from the loss of CNY21bn in the prior quarter. We estimate BABA's consolidated EBITA rebounded strongly by 78% y-y in 2HCY26F on an aligned basis for the QC investment and disciplined investment in non-AI initiatives. We maintain our Buy rating and TP of USD178. Our top picks in the China internet space are Alibaba, Tencent (700 HK, Buy), Meituan (3690 HK, Buy), NetEase (NTES US, Buy) and J&T (1519 HK, Buy).

## (Continued on page 1...)

<table><tr><td>Year-end 31 Mar</td><td colspan="2">FY26</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td><td colspan="2">FY29F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>1,023,670</td><td>1,125,101</td><td>1,125,101</td><td>1,308,005</td><td>1,308,005</td><td>1,566,078</td><td>1,566,078</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>105,904</td><td>76,536</td><td>76,536</td><td>107,070</td><td>107,070</td><td>321,206</td><td>321,206</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>64,438</td><td>96,424</td><td>96,424</td><td>128,683</td><td>128,683</td><td>173,420</td><td>173,420</td><td></td></tr><tr><td>FD normalised EPS</td><td>26.80</td><td>40.31</td><td>40.31</td><td>54.06</td><td>54.06</td><td>73.22</td><td>73.22</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>-59.0</td><td>50.4</td><td>50.4</td><td>34.1</td><td>34.1</td><td>35.4</td><td>35.4</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>25.8</td><td>-</td><td>16.6</td><td>-</td><td>12.3</td><td>-</td><td>9.1</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>9.7</td><td>-</td><td>7.5</td><td>-</td><td>6.3</td><td>-</td><td>5.1</td><td></td></tr><tr><td>Price/book (x)</td><td>1.5</td><td>-</td><td>1.3</td><td>-</td><td>1.2</td><td>-</td><td>1.1</td><td></td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>-</td><td>1.1</td><td>-</td><td>1.1</td><td>-</td><td>1.1</td><td></td></tr><tr><td>ROE (%)</td><td>10.1</td><td>6.9</td><td>6.9</td><td>9.0</td><td>9.0</td><td>24.6</td><td>24.6</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>6.8</td><td>8.1</td><td>8.1</td><td>8.8</td><td>8.8</td><td>6.4</td><td>6.4</td><td></td></tr></table>

Source: Company data, NOM estimates

8 July 2026

Rating Remains Buy

Target price Remains USD 178.00

Closing price 7 July 2026 USD 98.14

<table><tr><td>Implied upside</td><td>+81.4%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>235,613.4</td></tr><tr><td>ADT (USD mn)</td><td>1,434.7</td></tr></table>

## Relative performance chart

![](images/7697bde096c130c02377f9c2a54e64b832a757b4c0ceba07ded15d7a60df13f6.jpg)  
Source: LSEG, NOM

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK

Jialong.shi@NOM.com

Rachel Guo - NIHK
rachel.guo@NOM.com
+852 2252 1400

## Key data on Alibaba Group Holding

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (USD)</td><td>-18.9</td><td>-18.0</td><td>-7.7</td><td>M cap (USDmn)</td><td>235,613.4</td></tr><tr><td>Absolute (USD)</td><td>-18.9</td><td>-18.0</td><td>-7.7</td><td>Free float (%)</td><td>43.5</td></tr><tr><td>Rel to NASDAQ COMPOSITE</td><td>-19.4</td><td>-35.3</td><td>-34.1</td><td>3-mth ADT (USDmn)</td><td>1,434.7</td></tr></table>

<table><tr><td>Year-end 31 Mar</td><td>FY25</td><td>FY26</td><td>FY27F</td><td>FY28F</td><td>FY29F</td></tr><tr><td>Revenue</td><td>996,347</td><td>1,023,670</td><td>1,125,101</td><td>1,308,005</td><td>1,566,078</td></tr><tr><td>Cost of goods sold</td><td>-598,285</td><td>-616,136</td><td>-672,686</td><td>-774,194</td><td>-917,548</td></tr><tr><td>Gross profit</td><td>398,062</td><td>407,534</td><td>452,415</td><td>533,811</td><td>648,530</td></tr><tr><td>SG&amp;A</td><td>-243,742</td><td>-344,586</td><td>-358,548</td><td>-403,863</td><td>-469,795</td></tr><tr><td>Employee share expense</td><td>-13,415</td><td>-12,798</td><td>-11,518</td><td>-10,366</td><td>-9,330</td></tr><tr><td>Operating profit</td><td>140,905</td><td>50,150</td><td>82,349</td><td>119,581</td><td>169,405</td></tr><tr><td>EBITDA</td><td>176,501</td><td>92,296</td><td>125,099</td><td>163,019</td><td>213,612</td></tr><tr><td>Depreciation</td><td>-29,260</td><td>-37,067</td><td>-38,179</td><td>-39,324</td><td>-40,504</td></tr><tr><td>Amortisation</td><td>-6,336</td><td>-5,079</td><td>-4,571</td><td>-4,114</td><td>-3,703</td></tr><tr><td>EBIT</td><td>140,905</td><td>50,150</td><td>82,349</td><td>119,581</td><td>169,405</td></tr><tr><td>Net interest expense</td><td>11,163</td><td>77,719</td><td>9,717</td><td>9,203</td><td>8,663</td></tr><tr><td colspan="6">Associates &amp; JCEs</td></tr><tr><td>Other income</td><td>16,035</td><td>6,566</td><td>7,576</td><td>8,181</td><td>8,848</td></tr><tr><td>Earnings before tax</td><td>168,103</td><td>134,435</td><td>99,642</td><td>136,966</td><td>186,916</td></tr><tr><td>Income tax</td><td>-35,445</td><td>-30,045</td><td>-21,706</td><td>-28,695</td><td>-38,151</td></tr><tr><td>Net profit after tax</td><td>132,658</td><td>104,390</td><td>77,936</td><td>108,270</td><td>148,765</td></tr><tr><td>Minorities</td><td>4,133</td><td>1,465</td><td>2,000</td><td>2,200</td><td>2,420</td></tr><tr><td>Other items</td><td>21,149</td><td>-41,417</td><td>16,488</td><td>18,212</td><td>22,235</td></tr><tr><td colspan="6">Preferred dividends</td></tr><tr><td>Normalised NPAT</td><td>157,940</td><td>64,438</td><td>96,424</td><td>128,683</td><td>173,420</td></tr><tr><td>Extraordinary items</td><td>-28,470</td><td>41,466</td><td>-19,888</td><td>-21,612</td><td>147,785</td></tr><tr><td>Reported NPAT</td><td>129,470</td><td>105,904</td><td>76,536</td><td>107,070</td><td>321,206</td></tr><tr><td>Dividends</td><td>-29,077</td><td>-33,732</td><td>-17,500</td><td>-16,003</td><td>-15,763</td></tr><tr><td>Transfer to reserves</td><td>100,393</td><td>72,172</td><td>59,036</td><td>91,067</td><td>305,442</td></tr><tr><td colspan="6">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td>13.2</td><td>15.7</td><td>20.9</td><td>14.8</td><td>4.9</td></tr><tr><td>Normalised P/E (x)</td><td>10.8</td><td>25.8</td><td>16.6</td><td>12.3</td><td>9.1</td></tr><tr><td>FD normalised P/E (x)</td><td>10.8</td><td>25.8</td><td>16.6</td><td>12.3</td><td>9.1</td></tr><tr><td>Dividend yield (%)</td><td>1.7</td><td>2.1</td><td>1.1</td><td>1.1</td><td>1.1</td></tr><tr><td>Price/cashflow (x)</td><td>10.5</td><td>21.8</td><td>11.6</td><td>10.7</td><td>7.4</td></tr><tr><td>Price/book (x)</td><td>1.6</td><td>1.5</td><td>1.3</td><td>1.2</td><td>1.1</td></tr><tr><td>EV/EBITDA (x)</td><td>5.7</td><td>9.7</td><td>7.5</td><td>6.3</td><td>5.1</td></tr><tr><td>EV/EBIT (x)</td><td>7.1</td><td>17.8</td><td>11.5</td><td>8.6</td><td>6.4</td></tr><tr><td>Gross margin (%)</td><td>40.0</td><td>39.8</td><td>40.2</td><td>40.8</td><td>41.4</td></tr><tr><td>EBITDA margin (%)</td><td>17.7</td><td>9.0</td><td>11.1</td><td>12.5</td><td>13.6</td></tr><tr><td>EBIT margin (%)</td><td>14.1</td><td>4.9</td><td>7.3</td><td>9.1</td><td>10.8</td></tr><tr><td>Net margin (%)</td><td>13.0</td><td>10.3</td><td>6.8</td><td>8.2</td><td>20.5</td></tr><tr><td>Effective tax rate (%)</td><td>21.1</td><td>22.3</td><td>21.8</td><td>21.0</td><td>20.4</td></tr><tr><td>Dividend payout (%)</td><td>22.5</td><td>31.9</td><td>22.9</td><td>14.9</td><td>4.9</td></tr><tr><td>ROE (%)</td><td>12.8</td><td>10.1</td><td>6.9</td><td>9.0</td><td>24.6</td></tr><tr><td>ROA (pretax %)</td><td>8.9</td><td>2.9</td><td>4.5</td><td>6.1</td><td>8.1</td></tr><tr><td colspan="6">Growth (%)</td></tr><tr><td>Revenue</td><td>5.9</td><td>2.7</td><td>9.9</td><td>16.3</td><td>19.7</td></tr><tr><td>EBITDA</td><td>9.2</td><td>-47.7</td><td>35.5</td><td>30.3</td><td>31.0</td></tr><tr><td>Normalised EPS</td><td>5.1</td><td>-59.0</td><td>50.4</td><td>34.1</td><td>35.4</td></tr><tr><td>Normalised FDEPS</td><td>5.1</td><td>-59.0</td><td>50.4</td><td>34.1</td><td>35.4</td></tr></table>

Source: Company data, NOM estimates

Cashflow statement (CNYmn)

<table><tr><td>Year-end 31 Mar</td><td>FY25</td><td>FY26</td><td>FY27F</td><td>FY28F</td><td>FY29F</td></tr><tr><td>EBITDA</td><td>176,501</td><td>92,296</td><td>125,099</td><td>163,019</td><td>213,612</td></tr><tr><td>Change in working capital</td><td>-32,192</td><td>9,454</td><td>6,190</td><td>-13,596</td><td>15,339</td></tr><tr><td>Other operating cashflow</td><td>19,200</td><td>-25,537</td><td>6,314</td><td>-1,402</td><td>-14,310</td></tr><tr><td>CF from operations</td><td>163,509</td><td>76,213</td><td>137,603</td><td>148,021</td><td>214,641</td></tr><tr><td>Capital expenditure</td><td>-85,972</td><td>-126,063</td><td>-135,012</td><td>-143,881</td><td>-172,269</td></tr><tr><td>Free cashflow</td><td>77,537</td><td>-49,850</td><td>2,591</td><td>4,141</td><td>42,372</td></tr><tr><td>Reduction in investments</td><td>-114,267</td><td>-14,499</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>32,671</td><td>-11,565</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Inc in other LT liabilities</td><td>17,520</td><td>24,523</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adjustments</td><td>-40,849</td><td>62,011</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>-27,388</td><td>10,620</td><td>2,591</td><td>4,141</td><td>42,372</td></tr><tr><td>Cash dividends</td><td>-29,077</td><td>-33,732</td><td>-17,500</td><td>-16,003</td><td>-15,763</td></tr><tr><td>Equity issue</td><td>-86,652</td><td>-6,596</td><td>-5,000</td><td>-5,000</td><td>-5,000</td></tr><tr><td>Debt issue</td><td>-7,110</td><td>5,770</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>47,589</td><td>9,981</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-75,250</td><td>-24,577</td><td>-22,500</td><td>-21,003</td><td>-20,763</td></tr><tr><td>Net cashflow</td><td>-102,638</td><td>-13,957</td><td>-19,909</td><td>-16,863</td><td>21,609</td></tr><tr><td>Beginning cash</td><td>248,125</td><td>145,487</td><td>131,530</td><td>111,621</td><td>94,758</td></tr><tr><td>Ending cash</td><td>145,487</td><td>131,530</td><td>111,621</td><td>94,758</td><td>116,367</td></tr><tr><td>Ending net debt</td><td>49,382</td><td>72,605</td><td>92,514</td><td>109,377</td><td>87,768</td></tr><tr><td>Balance sheet (CNYmn)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>As at 31 Mar</td><td>FY25</td><td>FY26</td><td>FY27F</td><td>FY28F</td><td>FY29F</td></tr><tr><td>Cash &amp; equivalents</td><td>145,487</td><td>131,530</td><td>111,621</td><td>94,758</td><td>116,367</td></tr><tr><td>Marketable securities</td><td>272,607</td><td>197,348</td><td>197,348</td><td>197,348</td><td>197,348</td></tr><tr><td>Accounts receivable</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Inventories</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other current assets</td><td>255,955</td><td>281,891</td><td>289,907</td><td>329,239</td><td>331,557</td></tr><tr><td>Total current assets</td><td>674,049</td><td>610,769</td><td>598,876</td><td>621,345</td><td>645,272</td></tr><tr><td>LT investments</td><td>566,987</td><td>656,745</td><td>656,745</td><td>656,745</td><td>656,745</td></tr><tr><td>Fixed assets</td><td>203,348</td><td>282,699</td><td>379,532</td><td>484,088</td><td>615,853</td></tr><tr><td>Goodwill</td><td>255,501</td><td>247,378</td><td>247,378</td><td>247,378</td><td>247,378</td></tr><tr><td>Other intangible assets</td><td>20,911</td><td>16,983</td><td>12,412</td><td>8,298</td><td>4,595</td></tr><tr><td>Other LT assets</td><td>83,431</td><td>94,996</td><td>94,996</td><td>94,996</td><td>94,996</td></tr><tr><td>Total assets</td><td>1,804,227</td><td>1,909,570</td><td>1,989,939</td><td>2,112,850</td><td>2,264,839</td></tr><tr><td>Short-term debt</td><td>22,562</td><td>28,224</td><td>28,224</td><td>28,224</td><td>28,224</td></tr><tr><td>Accounts payable</td><td>332,537</td><td>359,893</td><td>377,888</td><td>396,782</td><td>416,621</td></tr><tr><td>Other current liabilities</td><td>80,247</td><td>88,281</td><td>84,492</td><td>91,334</td><td>89,151</td></tr><tr><td>Total current liabilities</td><td>435,346</td><td>476,398</td><td>490,604</td><td>516,340</td><td>533,997</td></tr><tr><td>Long-term debt</td><td>172,307</td><td>175,911</td><td>175,911</td><td>175,911</td><td>175,911</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>106,468</td><td>130,991</td><td>130,991</td><td>130,991</td><td>130,991</td></tr><tr><td>Total liabilities</td><td>714,121</td><td>783,300</td><td>797,506</td><td>823,242</td><td>840,899</td></tr><tr><td>Minority interest</td><td>68,535</td><td>57,539</td><td>55,539</td><td>53,339</td><td>50,919</td></tr><tr><td>Preferred stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Common stock</td><td>372,700</td><td>373,419</td><td>368,419</td><td>363,419</td><td>358,419</td></tr><tr><td>Retained earnings</td><td>616,401</td><td>674,650</td><td>764,045</td><td>869,917</td><td>1,011,909</td></tr><tr><td>Proposed dividends</td><td>29,077</td><td>33,732</td><td>17,500</td><td>16,003</td><td>15,763</td></tr><tr><td>Other equity and reserves</td><td>3,393</td><td>-13,070</td><td>-13,070</td><td>-13,070</td><td>-13,070</td></tr><tr><td>T

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
