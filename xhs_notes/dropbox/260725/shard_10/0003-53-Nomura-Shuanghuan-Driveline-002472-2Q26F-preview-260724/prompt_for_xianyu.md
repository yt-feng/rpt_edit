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

# 2Q26F preview

## EV and construction drive growth; ICE decline narrowed in 2Q26F; robotics and Semi gradually kick-in in 2H26F

## 2Q26F to improve as NEV and construction machinery drive growth

For 2Q26F, we expect Shuanghuan to deliver solid revenue growth: i) with new energy vehicle (NEV) revenue up 10-20% y-y, as April was flat but May–June turned positive and the June coaxial-gear ramp further added momentum; ii) internal combustion engine (ICE) gears should see the decline narrow to single digits in 2Q26F from 20–30% in 1Q26, aided by a diversified customer base; we expect a further narrowing in 2H26F and deliver a high-single-digit full-year decline; iii) commercial-vehicle sales look broadly flat y-y, with Tesla (TSLA US, Not rated) Semi commencing and a slight full-year sales contribution likely; iv) construction-machinery likely sustained 20–30% growth into 2Q26F; v) Intelligent Actuator sales tracked slightly below our expectation (\~CNY1.05bn vs previous estimated CNY1.1–1.2bn) on flat robot-vacuum share. In addition, 2Q26F gross margin is unlikely to exceed 1Q26 on mix. We view full-year financials as broadly on guidance.

## Robot client at \~CNY6,000 content value; capacity to likely scale out

Regarding robotics, Shuanghuan is positioning itself as a beneficiary through robotics firms' shipment ramp-up. For one robotics client: i) we expect Shuanghuan to ship six RV-type (rotary vector) reducers at an average selling price (ASP) of roughly CNY1,000 each; ii) for the next-generation robot, we expect Shuanghuan to supply cycloidal reducers with six units per robot. On capacity, we expect Shuanghuan may further expand capacity to accommodate the anticipated demand against the scale-up backdrop (Optimus ramps; China scales up as cost curves bend lower). Furthermore, despite the pull-ins from robotics firms, we remain cautious that shifting technical roadmaps could still alter joint content over time.

Maintain Buy and TP of CNY50: 2026F growth in-line, robotics and Semi kick-in
We maintain our Buy rating and TP of CNY50, as: i) 2026F growth looks broadly in line with guidance, and ii) robotics and Tesla Semi may start contributions in the long term. We raise 2027/28F EPS to CNY1.99/2.34 from CNY1.96/2.25. Our TP implies 25x 2027F P/E (previously: 29x 2026F P/E), largely in-line with its historical average at 26x, supported by a $16.5\%$ EPS CAGR in 2026-28F. The stock currently trades at 18x 2027F P/E. Downside risks: slower shipment ramp-up schedules of robotics firms, lackluster shipments of construction machinery in 4Q26F.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>9,112</td><td>9,920</td><td>10,204</td><td>11,045</td><td>12,082</td><td>12,224</td><td>14,050</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>1,262</td><td>1,449</td><td>1,455</td><td>1,660</td><td>1,693</td><td>1,905</td><td>1,989</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>1,262</td><td>1,449</td><td>1,455</td><td>1,660</td><td>1,693</td><td>1,905</td><td>1,989</td><td></td></tr><tr><td>FD normalised EPS</td><td>1.48</td><td>1.71</td><td>1.71</td><td>1.96</td><td>1.99</td><td>2.25</td><td>2.34</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>22.9</td><td>14.9</td><td>15.3</td><td>14.5</td><td>16.4</td><td>14.8</td><td>17.5</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>23.8</td><td>-</td><td>20.7</td><td>-</td><td>17.7</td><td>-</td><td>15.1</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>13.2</td><td>-</td><td>11.9</td><td>-</td><td>10.2</td><td>-</td><td>8.6</td><td></td></tr><tr><td>Price/book (x)</td><td>2.9</td><td>-</td><td>2.4</td><td>-</td><td>2.1</td><td>-</td><td>1.8</td><td></td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>ROE (%)</td><td>12.8</td><td>13.6</td><td>12.7</td><td>13.9</td><td>12.6</td><td>14.1</td><td>12.7</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>8.6</td><td>7.0</td><td>3.9</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Remains
CNY 50.00

Closing price 24 July 2026 CNY 35.36

<table><tr><td>Implied upside</td><td>+41.4%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>4,436.2</td></tr><tr><td>ADT (USD mn)</td><td>252.2</td></tr></table>

## Relative performance chart

![](images/2ee244d5af60e153536d66771b4af70b6de867bcc64b7ca96793c99b6eaf4bf9.jpg)  
Source: LSEG, NOM

## Research Analysts

Advanced Manufacturing

Frank Fan - NIHK
frank.fan@NOM.com
+852 2252 2195

Donnie Teng - NIHK
donnie.teng@NOM.com
+852 2252 1439

## Key data on Shuanghuan Driveline

Income statement (CNYmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (CNY)</td><td>-11.7</td><td>-3.5</td><td>1.8</td><td>M cap (USDmn)</td><td>4,436.2</td></tr><tr><td>Absolute (USD)</td><td>-11.3</td><td>-2.6</td><td>7.4</td><td>Free float (%)</td><td>73.2</td></tr><tr><td>Rel to CSI 300</td><td>-7.4</td><td>-2.6</td><td>-12.2</td><td>3-mth ADT (USDmn)</td><td>252.2</td></tr></table>

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>8,781</td><td>9,112</td><td>10,204</td><td>12,082</td><td>14,050</td></tr><tr><td>Cost of goods sold</td><td>-6,585</td><td>-6,621</td><td>-7,398</td><td>-8,790</td><td>-10,194</td></tr><tr><td>Gross profit</td><td>2,196</td><td>2,491</td><td>2,805</td><td>3,292</td><td>3,857</td></tr><tr><td>SG&amp;A</td><td>-947</td><td>-1,030</td><td>-1,123</td><td>-1,341</td><td>-1,560</td></tr><tr><td>Employee share expense</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Operating profit</td><td>1,249</td><td>1,461</td><td>1,682</td><td>1,951</td><td>2,297</td></tr><tr><td>EBITDA</td><td>1,984</td><td>2,339</td><td>2,572</td><td>2,879</td><td>3,243</td></tr><tr><td>Depreciation</td><td>-736</td><td>-878</td><td>-860</td><td>-900</td><td>-920</td></tr><tr><td>Amortisation</td><td>0</td><td>0</td><td>-30</td><td>-28</td><td>-26</td></tr><tr><td>EBIT</td><td>1,249</td><td>1,461</td><td>1,682</td><td>1,951</td><td>2,297</td></tr><tr><td>Net interest expense</td><td>-38</td><td>-47</td><td>-35</td><td>-33</td><td>-30</td></tr><tr><td colspan="6">Associates &amp; JCEs</td></tr><tr><td>Other income</td><td>-7</td><td>91</td><td>70</td><td>80</td><td>80</td></tr><tr><td>Earnings before tax</td><td>1,203</td><td>1,505</td><td>1,717</td><td>1,998</td><td>2,347</td></tr><tr><td>Income tax</td><td>-147</td><td>-180</td><td>-206</td><td>-240</td><td>-282</td></tr><tr><td>Net profit after tax</td><td>1,057</td><td>1,325</td><td>1,511</td><td>1,758</td><td>2,065</td></tr><tr><td>Minority interests</td><td>-33</td><td>-64</td><td>-56</td><td>-65</td><td>-76</td></tr><tr><td colspan="6">Other items</td></tr><tr><td colspan="6">Preferred dividends</td></tr><tr><td>Normalised NPAT</td><td>1,024</td><td>1,262</td><td>1,455</td><td>1,693</td><td>1,989</td></tr><tr><td colspan="6">Extraordinary items</td></tr><tr><td>Reported NPAT</td><td>1,024</td><td>1,262</td><td>1,455</td><td>1,693</td><td>1,989</td></tr><tr><td colspan="6">Dividends</td></tr><tr><td>Transfer to reserves</td><td>1,024</td><td>1,262</td><td>1,455</td><td>1,693</td><td>1,989</td></tr><tr><td colspan="6">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td>29.3</td><td>23.8</td><td>20.7</td><td>17.7</td><td>15.1</td></tr><tr><td>Normalised P/E (x)</td><td>29.3</td><td>23.8</td><td>20.7</td><td>17.7</td><td>15.1</td></tr><tr><td>FD normalised P/E (x)</td><td>29.3</td><td>23.8</td><td>20.7</td><td>17.7</td><td>15.1</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Price/cashflow (x)</td><td>17.8</td><td>12.6</td><td>14.4</td><td>11.9</td><td>10.3</td></tr><tr><td>Price/book (x)</td><td>3.2</td><td>2.9</td><td>2.4</td><td>2.1</td><td>1.8</td></tr><tr><td>EV/EBITDA (x)</td><td>15.7</td><td>13.2</td><td>11.9</td><td>10.2</td><td>8.6</td></tr><tr><td>EV/EBIT (x)</td><td>25.0</td><td>21.2</td><td>18.2</td><td>15.1</td><td>12.1</td></tr><tr><td>Gross margin (%)</td><td>25.0</td><td>27.3</td><td>27.5</td><td>27.3</td><td>27.4</td></tr><tr><td>EBITDA margin (%)</td><td>22.6</td><td>25.7</td><td>25.2</td><td>23.8</td><td>23.1</td></tr><tr><td>EBIT margin (%)</td><td>14.2</td><td>16.0</td><td>16.5</td><td>16.2</td><td>16.3</td></tr><tr><td>Net margin (%)</td><td>11.7</td><td>13.8</td><td>14.3</td><td>14.0</td><td>14.2</td></tr><tr><td>Effective tax rate (%)</td><td>12.2</td><td>11.9</td><td>12.0</td><td>12.0</td><td>12.0</td></tr><tr><td>Dividend payout (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>ROE (%)</td><td>11.7</td><td>12.8</td><td>12.7</td><td>12.6</td><td>12.7</td></tr><tr><td>ROA (pretax %)</td><td>9.4</td><td>9.5</td><td>9.8</td><td>10.4</td><td>11.2</td></tr><tr><td colspan="6">Growth (%)</td></tr><tr><td>Revenue</td><td>8.8</td><td>3.8</td><td>12.0</td><td>18.4</td><td>16.3</td></tr><tr><td>EBITDA</td><td>22.8</td><td>17.9</td><td>10.0</td><td>11.9</td><td>12.6</td></tr><tr><td>Normalised EPS</td><td>25.8</td><td>22.9</td><td>15.3</td><td>16.4</td><td>17.5</td></tr><tr><td>Normalised FDEPS</td><td>25.8</td><td>22.9</td><td>15.3</td><td>16.4</td><td>17.5</td></tr></table>

Source: Company data, NOM estimates

Cashflow statement (CNYmn)

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>1,984</td><td>2,339</td><td>2,572</td><td>2,879</td><td>3,243</td></tr><tr><td>Change in working capital</td><td>-151</td><td>98</td><td>-716</td><td>-301</td><td>-232</td></tr><tr><td>Other operating cashflow</td><td>-152</td><td>-45</td><td>229</td><td>-62</td><td>-91</td></tr><tr><td>Cashflow from operations</td><td>1,681</td><td>2,391</td><td>2,085</td><td>2,516</td><td>2,920</td></tr><tr><td>Capital expenditure</td><td>-1,989</td><td>-2,069</td><td>-1,600</td><td>-1,600</td><td>-1,600</td></tr><tr><td>Free cashflow</td><td>-307</td><td>322</td><td>485</td><td>916</td><td>1,320</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-143</td><td>-5</td><td>-10</td><td>-10</td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>87</td><td>34</td><td>-10</td><td>-10</td><td></td></tr><tr><td>Adjustments</td><td>27</td><td>-169</td><td>-29</td><td>20</td><td>20</td></tr><tr><td>CF after investing acts</td><td>-280</td><td>98</td><td>485</td><td>916</td><td>1,320</td></tr><tr><td>Cash dividends</td><td>-160</td><td>-421</td><td>-364</td><td>-423</td><td>-497</td></tr><tr><td>Equity issue</td><td>45</td><td>202</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>981</td><td>1,205</td><td>353</td><td>631</td><td>758</td></tr><tr><td>CF from financial acts</td><td>866</td><td>985</td><td>-10</td><td>208</td><td>261</td></tr><tr><td>Net cashflow</td><td>586</td><td>1,083</td><td>474</td><td>1,123</td><td>1,581</td></tr><tr><td>Beginning cash</td><td>822</td><td>1,407</td><td>2,490</td><td>2,965</td><td>4,089</td></tr><tr><td>Ending cash</td><td>1,408</td><td>2,491</td><td>2,965</td><td>4,089</td><td>5,669</td></tr><tr><td>Ending net debt</td><td>1,104</td><td>906</td><td>485</td><td>-639</td><td>-2,219</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>1,407</td><td>2,490</td><td>2,965</td><td>4,089</td><td>5,669</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>2,563</td><td>2,759</td><td>3,248</td><td>3,762</td><td>4,252</td></tr><tr><td>Inventories</td><td>2,031</td><td>2,226</td><td>2,644</td><td>3,056</td><td>3,455</td></tr><tr><td>Other current assets</td><td>802</td><td>965</td><td>1,002</td><td>1,183</td><td>1,378</td></tr><tr><td>Total current assets</td><td>6,803</td><td>8,440</td><td>9,859</td><td>12,089</td><td>14,754</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>8,301</td><td>9,402</td><td>10,142</td><td>10,842</td><td>11,522</td></tr><tr><td>Goodwill</td><td>61</td><td>60</td><td>60</td><td>60</td><td>60</td></tr><tr><td>Other intangible assets</td><td>499</td><td>516</td><td>486</td><td>458</td><td>432</td></tr><tr><td>Other LT assets</td><td>202</td><td>345</td><td>350</td><td>360</td><td>370</td></tr><tr><td>Total assets</td><td>15,867</td><td>18,763</td><td>20,897</td><td>23,808</td><td>27,137</td></tr><tr><td>Short-term debt</td><td>1,983</td><td>3,122</td><td>3,200</td><td>3,200</td><td>3,200</td></tr><tr><td>Accounts payable</td><td>2,626</td><td>3,039</td><td>3,630</td><td>4,384</td><td>5,183</td></tr><tr><td>Other current liabilities</td><td>952</td><td>1,191</td><td>828</td><td>879</td><td>933</td></tr><tr><td>Total current liabilities</td><td>5,561</td><td>7,353</td><td>7,658</td><td>8,463</td><td>9,315</td></tr><tr><td>Long-term debt</td><td>529</td><td>274</td><td>250</td><td>250</td><td>250</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>538</td><td>626</td><td>660</td><td>650</td><td>640</td></tr><tr><td>Total liabilities</td><td>6,628</td><td>8,253</td><td>8,568</td><td>9,363</td><td>10,205</td></tr><tr><td>Minority interest</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>847</td><td>850</td><td>850</td><td>850</td><td>850</td></tr><tr><td>Retained earnings</td><td>3,477</td><td>4,319</td><td>6,138</td><td>8,255</td><td>10,741</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td>4,914</td><td>5,341</td><td>5,341</td><td>5,341</td><td>5,341</td></tr><tr><td>Total shareholders&#x27; equity</td><td>9,238</td><td>10,510</td><td>12,329</td><td>14,446</td><td>16,932</td></tr><tr><td>Total equity &amp; liabilities</td><td>15,867</td><td>18,763</td><td>20,897</td><td>23,808</td><td>27,137</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>1.22</td><td>1.15</td><td>1.29</td><td>1.43</td><td>1.58</td></tr><tr><td>Interest cover</td><td>32.9</td><td>31.1</td><td>48.1</td><td>59.1</td><td>76.6</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>0.56</td><td>0.39</td><td>0.19</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>12.0</td><td>8.6</td><td>3.9</td><td>net cash</td><td>net cash</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>1.21</td><td>1.48</td><td>1.71</td><td>1.99</td><td>2.34</td></tr><tr><td>Norm EPS (CNY)</td><td>1.21</td><td>1.48</td><td>1.71</td><td>1.99</td><td>2.34</td></tr><tr><td>FD norm EPS (CNY)</td><td>1.21</td><td>1.48</td><td>1.71</td><td>1.99</td><td>2.

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
