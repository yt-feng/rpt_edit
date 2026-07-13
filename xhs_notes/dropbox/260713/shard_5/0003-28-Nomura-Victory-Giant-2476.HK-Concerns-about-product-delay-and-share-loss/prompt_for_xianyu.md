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

# Concerns about product delay and share loss overdone...

... rubin upgrade, ASIC and optical transceiver PCB are key drivers

Action: Maintain Buy but cut TP to CNY389; implying $94\%$ upside; short-term concerns overdone

Despite recent market concerns about the delay of NVIDIA's (NVDA US, Not rated) Kyber rack, we think the production ramp-up of Rubin GPU in 2H26 would continue to support Victory Giant's (VGT) PCB value content upgrade as well as margin expansion. Although there might be more competition in NVIDIA's Rubin compute tray / HDI (High Density Interconnect) PCB, likely from ZDT (4958 TT, Buy), we think this should be the supply chain diversification efforts of AI customers, amid an extremely under supply situation. Meanwhile, we think VGT remains as the leading supplier of a GPU customer, while its entry into ASIC and optical transceiver customers would drive sustainable growth and more balanced customer exposure in 2H26-2027F. We cut FY26-28F revenue / earnings forecasts by 7-13%/ 7-14% to reflect a likely lower HDI revenue contribution. We maintain our Buy rating with a lower TP of HKD447, based on 27x (unchanged) FY27F EPS of CNY14.41. The stock is currently trading at 14x FY27F EPS.

Market concerns about Kyber / backplane delay and GPU customer's supply chain diversification likely overdone; the company's HDI capacity is still a strategic asset We think VGT's GPU shipments for NVIDIA's Rubin GPU may have already started in mid-2026, and this could ramp up in 2H26F. Despite market concerns about technology issues and huge market share loss, we think the company's existing and potential HDI capacity remain as a strategic asset to secure a lead in this segment, and there are not many challengers in sight due to high technology barriers and material / equipment shortages, in our view. Moreover, we believe not only the GPU customer, but also ASIC customers may start to adopt HDI from 2028F, leading to better demand for the company's HDI products. We expect a $82\%$ revenue CAGR for the HDI segment in FY26-28F, contributing $63\%$ of total revenue in FY28F.

ASIC and optical transceiver help company to diversify its customer portfolio
We think the company has already made good progress in the ASIC customer segment, as well as the 800G / 1.6T transceiver market, which should enjoy strong demand uptick in the next few years. We believe VGT still stands out as one of the leading AI PCB makers, and we estimate a 77% revenue CAGR for the company's AI & HPC (high performance computing) sector over 2026F-28F, contributing 77% of total sales in FY28F.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>19,292</td><td>31,948</td><td>27,850</td><td>52,317</td><td>49,158</td><td>75,880</td><td>70,941</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>4,312</td><td>8,698</td><td>7,497</td><td>15,174</td><td>14,162</td><td>22,509</td><td>20,927</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>4,312</td><td>8,698</td><td>7,497</td><td>15,174</td><td>14,162</td><td>22,509</td><td>20,927</td><td></td></tr><tr><td>FD normalised EPS</td><td>4.98</td><td>9.39</td><td>8.09</td><td>15.44</td><td>14.41</td><td>22.90</td><td>21.29</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>271.9</td><td>88.6</td><td>62.6</td><td>64.5</td><td>78.1</td><td>48.3</td><td>47.8</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>39.1</td><td>-</td><td>24.0</td><td>-</td><td>13.5</td><td>-</td><td>9.1</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>2.9</td><td>-</td><td>0.9</td><td>-</td><td>0.1</td><td>-</td><td>-0.4</td><td></td></tr><tr><td>Price/book (x)</td><td>10.2</td><td>-</td><td>4.6</td><td>-</td><td>3.5</td><td>-</td><td>2.5</td><td></td></tr><tr><td>Dividend yield (%)</td><td>0.2</td><td>-</td><td>0.2</td><td>-</td><td>0.4</td><td>-</td><td>0.7</td><td></td></tr><tr><td>ROE (%)</td><td>33.8</td><td>29.5</td><td>26.0</td><td>30.5</td><td>29.5</td><td>33.2</td><td>32.2</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Reduced from
HKD 479.00
HKD 447.00

Closing price
10 July 2026
HKD 230.20

<table><tr><td>Implied upside</td><td>+94.2%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>3,236.7</td></tr><tr><td>ADT (USD mn)</td><td>249.6</td></tr></table>

## Relative performance chart

![](images/442f6141df4b6abef6bbca6830dae066ed348a8e03fa76508facd1a3c2368b0e.jpg)  
Source: LSEG, NOM

## Research Analysts

China Technology
Bing Duan - NIHK
bing.duan1@NOM.com
+852 2252 2141

Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

## Key data on Victory Giant

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (HKD)</td><td>-35.9</td><td></td><td></td><td>M cap (USDmn)</td><td>3,236.7</td></tr><tr><td>Absolute (USD)</td><td>-35.9</td><td></td><td></td><td>Free float (%)</td><td>62.0</td></tr><tr><td>Rel to Hang Seng Index</td><td>-34.9</td><td></td><td></td><td>3-mth ADT (USDmn)</td><td>249.6</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>10,731</td><td>19,292</td><td>27,850</td><td>49,158</td><td>70,941</td></tr><tr><td>Cost of goods sold</td><td>-8,293</td><td>-12,497</td><td>-16,544</td><td>-27,602</td><td>-38,516</td></tr><tr><td>Gross profit</td><td>2,439</td><td>6,795</td><td>11,306</td><td>21,556</td><td>32,425</td></tr><tr><td>SG&amp;A</td><td>-1,013</td><td>-1,631</td><td>-2,370</td><td>-4,700</td><td>-7,530</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>1,425</td><td>5,164</td><td>8,936</td><td>16,856</td><td>24,895</td></tr><tr><td>EBITDA</td><td>2,142</td><td>6,047</td><td>10,714</td><td>19,159</td><td>27,370</td></tr><tr><td>Depreciation</td><td>-717</td><td>-883</td><td>-1,778</td><td>-2,303</td><td>-2,475</td></tr><tr><td>Amortisation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>1,425</td><td>5,164</td><td>8,936</td><td>16,856</td><td>24,895</td></tr><tr><td>Net interest expense</td><td>-114</td><td>-142</td><td>-206</td><td>-363</td><td>-524</td></tr><tr><td>Associates &amp; JCEs</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other income</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Earnings before tax</td><td>1,312</td><td>5,022</td><td>8,730</td><td>16,493</td><td>24,371</td></tr><tr><td>Income tax</td><td>-157</td><td>-710</td><td>-1,234</td><td>-2,331</td><td>-3,444</td></tr><tr><td>Net profit after tax</td><td>1,154</td><td>4,312</td><td>7,497</td><td>14,162</td><td>20,927</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>1,154</td><td>4,312</td><td>7,497</td><td>14,162</td><td>20,927</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>1,154</td><td>4,312</td><td>7,497</td><td>14,162</td><td>20,927</td></tr><tr><td>Dividends</td><td>-163</td><td>-258</td><td>-448</td><td>-846</td><td>-1,250</td></tr><tr><td>Transfer to reserves</td><td>991</td><td>4,054</td><td>7,049</td><td>13,316</td><td>19,677</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>145.3</td><td>39.1</td><td>24.0</td><td>13.5</td><td>9.1</td></tr><tr><td>Normalised P/E (x)</td><td>145.3</td><td>39.1</td><td>24.0</td><td>13.5</td><td>9.1</td></tr><tr><td>FD normalised P/E (x)</td><td>145.3</td><td>39.1</td><td>24.0</td><td>13.5</td><td>9.1</td></tr><tr><td>Dividend yield (%)</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.4</td><td>0.7</td></tr><tr><td>Price/cashflow (x)</td><td>81.0</td><td>36.5</td><td>30.3</td><td>10.6</td><td>9.7</td></tr><tr><td>Price/book (x)</td><td>18.8</td><td>10.2</td><td>4.6</td><td>3.5</td><td>2.5</td></tr><tr><td>EV/EBITDA (x)</td><td>8.8</td><td>2.9</td><td>0.9</td><td>0.1</td><td>-0.4</td></tr><tr><td>EV/EBIT (x)</td><td>13.2</td><td>3.5</td><td>1.1</td><td>0.1</td><td>-0.5</td></tr><tr><td>Gross margin (%)</td><td>22.7</td><td>35.2</td><td>40.6</td><td>43.8</td><td>45.7</td></tr><tr><td>EBITDA margin (%)</td><td>20.0</td><td>31.3</td><td>38.5</td><td>39.0</td><td>38.6</td></tr><tr><td>EBIT margin (%)</td><td>13.3</td><td>26.8</td><td>32.1</td><td>34.3</td><td>35.1</td></tr><tr><td>Net margin (%)</td><td>10.8</td><td>22.4</td><td>26.9</td><td>28.8</td><td>29.5</td></tr><tr><td>Effective tax rate (%)</td><td>12.0</td><td>14.1</td><td>14.1</td><td>14.1</td><td>14.1</td></tr><tr><td>Dividend payout (%)</td><td>14.1</td><td>6.0</td><td>6.0</td><td>6.0</td><td>6.0</td></tr><tr><td>ROE (%)</td><td>13.9</td><td>33.8</td><td>26.0</td><td>29.5</td><td>32.2</td></tr><tr><td>ROA (pretax %)</td><td>8.7</td><td>20.9</td><td>22.3</td><td>28.7</td><td>34.5</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>35.3</td><td>79.8</td><td>44.4</td><td>76.5</td><td>44.3</td></tr><tr><td>EBITDA</td><td>41.7</td><td>182.3</td><td>77.2</td><td>78.8</td><td>42.9</td></tr><tr><td>Normalised EPS</td><td>2.2</td><td>271.9</td><td>62.6</td><td>78.1</td><td>47.8</td></tr><tr><td>Normalised FDEPS</td><td>2.2</td><td>271.9</td><td>62.6</td><td>78.1</td><td>47.8</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>2,142</td><td>6,047</td><td>10,714</td><td>19,159</td><td>27,370</td></tr><tr><td>Change in working capital</td><td>184</td><td>2,128</td><td>-3,374</td><td>1,506</td><td>-3,773</td></tr><tr><td>Other operating cashflow</td><td>-255</td><td>-3,555</td><td>-1,399</td><td>-2,654</td><td>-3,928</td></tr><tr><td>Cashflow from operations</td><td>2,071</td><td>4,620</td><td>5,941</td><td>18,011</td><td>19,669</td></tr><tr><td>Capital expenditure</td><td>-1,116</td><td>-6,364</td><td>-15,000</td><td>-10,000</td><td>-5,000</td></tr><tr><td>Free cashflow</td><td>955</td><td>-1,744</td><td>-9,059</td><td>8,011</td><td>14,669</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-5,263</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>1,869</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Adjustments</td><td>469</td><td>666</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>1,424</td><td>-4,471</td><td>-9,059</td><td>8,011</td><td>14,669</td></tr><tr><td>Cash dividends</td><td>-163</td><td>-258</td><td>-258</td><td>-448</td><td>-846</td></tr><tr><td>Equity issue</td><td>0</td><td>1,876</td><td>17,300</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>-935</td><td>2,119</td><td>2,441</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>1,186</td><td>2,351</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>89</td><td>6,089</td><td>19,483</td><td>-448</td><td>-846</td></tr><tr><td>Net cashflow</td><td>1,513</td><td>1,618</td><td>10,424</td><td>7,563</td><td>13,823</td></tr><tr><td>Beginning cash</td><td>749</td><td>1,662</td><td>3,280</td><td>13,704</td><td>21,267</td></tr><tr><td>Ending cash</td><td>2,262</td><td>3,280</td><td>13,704</td><td>21,267</td><td>35,090</td></tr><tr><td>Ending net debt</td><td>927</td><td>-806</td><td>-8,789</td><td>-16,352</td><td>-30,175</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>1,662</td><td>3,280</td><td>13,704</td><td>21,267</td><td>35,090</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>4,272</td><td>6,561</td><td>9,077</td><td>18,525</td><td>21,308</td></tr><tr><td>Inventories</td><td>2,045</td><td>3,162</td><td>3,732</td><td>7,771</td><td>8,280</td></tr><tr><td>Other current assets</td><td>101</td><td>511</td><td>511</td><td>511</td><td>511</td></tr><tr><td>Total current assets</td><td>8,080</td><td>13,514</td><td>27,023</td><td>48,074</td><td>65,189</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>7,477</td><td>12,876</td><td>26,098</td><td>33,796</td><td>36,321</td></tr><tr><td>Goodwill</td><td>615</td><td>588</td><td>547</td><td>507</td><td>466</td></tr><tr><td>Other intangible assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT assets</td><td>3,004</td><td>8,267</td><td>8,267</td><td>8,267</td><td>8,267</td></tr><tr><td>Total assets</td><td>19,175</td><td>35,244</td><td>61,935</td><td>90,643</td><td>110,243</td></tr><tr><td>Short-term debt</td><td>1,908</td><td>2,474</td><td>4,915</td><td>4,915</td><td>4,915</td></tr><tr><td>Accounts payable</td><td>5,473</td><td>11,144</td><td>10,855</td><td>25,848</td><td>25,368</td></tr><tr><td>Other current liabilities</td><td>155</td><td>429</td><td>429</td><td>429</td><td>429</td></tr><tr><td>Total current liabilities</td><td>7,537</td><td>14,047</td><td>16,199</td><td>31,192</td><td>30,711</td></tr><tr><td>Long-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>2,711</td><td>4,580</td><td>4,580</td><td>4,580</td><td>4,580</td></tr><tr><td>Total liabilities</td><td>10,247</td><td>18,627</td><td>20,779</td><td>35,772</td><td>35,291</td></tr><tr><td>Minority interest</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>863</td><td>870</td><td>18,170</td><td>18,170</td><td>18,170</td></tr><tr><td>Retained earnings</td><td>8,065</td><td>15,747</td><td>22,986</td><td>36,700</td><td>56,781</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total shareholders&#x27; equity</td><td>8,928</td><td>16,618</td><td>41,157</td><td>54,871</td><td>74,952</td></tr><tr><td>Total equity &amp; liabilities</td><td>19,175</td><td>35,244</td><td>61,935</td><td>90,643</td><td>110,243</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>1.07</td><td>0.96</td><td>1.67</td><td>1.54</td><td>2.12</td></tr><tr><td>Interest cover</td><td>12.5</td><td>36.2</td><td>43.4</td><td>46.4</td><td>47.5</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>0.43</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>10.4<

[中间内容因长度限制已省略]

a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
