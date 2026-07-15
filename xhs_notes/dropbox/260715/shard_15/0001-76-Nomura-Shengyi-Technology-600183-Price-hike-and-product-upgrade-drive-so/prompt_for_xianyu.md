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

# Price hike and product upgrade drive solid 1H26 performance...

## ... and, we expect the AI upcycle to continue

Action: Maintain Buy and raise TP to CNY195, implying 31.6% upside
Shengyi Technology (ST) reported a strong 1H26E profit alert on 13 July after market close, guiding for CNY3.1-3.3bn net profit (+117%-131% y-y), and CNY2.72-2.92bn recurring earnings (+97%-112% y-y). We think the strong profit alert was attributable to a CCL price hike in 1H26, demand uptick from an AI PCB/CCL customer, as well as new capacity contribution. We believe the company has already become one of the global leaders in the AI CCL/PCB market, and will continue to gain market share thanks to its solid execution power and sustained technological innovations. We revise up our FY26-28F revenue forecasts by 24.5-50.1% to reflect the stronger volume and ASP growth in both the CCL and PCB segments, and raise our FY26-28F earnings forecasts by 38.7-55.2% due to margin expansion driven by better AI product exposure. We maintain Buy and raise TP to CNY195 (from CNY95), based on 43x (previously 32x) FY27F EPS of CNY4.51, in line with an FY26-28F earnings CAGR of 43%. The stock is trading at 32.8x FY27F EPS.

CCL: price hike to drive near-term earnings, tech upgrade to underpin long-term global AI market expansion

We think the CCL price hike in 1H26 (>50% y-y) was driven by upstream material shortage (copper foil, glass fiber, etc.), which will continue in 2H26F, and underpin further revenue/margin expansion. Meanwhile, we believe the company enjoys solid content value upgrade opportunities in the global AI infrastructure market, as it is well-prepared for new technology roadmaps such as M9 / M10 CCL, PTFE, etc. We estimate a 40% revenue CAGR for CCL & Prepreg segment in FY26-28F, contributing 67% to total sales in FY28F. Despite recent market concerns about the slower product upgrade from its leading GPU customer, we think the AI CCL market is already consolidated, and the company's market share gain story in the high-end CCL segment still looks intact.

PCB: ASIC product upgrade leads to stronger demand; diversification on track
The key ASIC customer has already started upgrading its product, leading to better demand for ST's HLC (high layer count) PCB products in 2Q26F, which will continue in 2H26F, in our view. Meanwhile, we think the company might gradually develop more AI customers in both the overseas market (ASIC, switch) and China market (AI server, switch), and reduce customer concentration risk. We estimate a 48% revenue CAGR for the PCB segment in FY26-28F, contributing 28% to total sales in FY28F.

14 July 2026

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>28,431</td><td>37,349</td><td>46,481</td><td>47,574</td><td>66,858</td><td>59,197</td><td>88,843</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>3,334</td><td>5,262</td><td>7,296</td><td>7,245</td><td>10,964</td><td>9,549</td><td>14,824</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>3,334</td><td>5,262</td><td>7,296</td><td>7,245</td><td>10,964</td><td>9,549</td><td>14,824</td><td></td></tr><tr><td>FD normalised EPS</td><td>1.37</td><td>2.17</td><td>3.00</td><td>2.98</td><td>4.51</td><td>3.93</td><td>6.10</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>88.8</td><td>57.8</td><td>118.8</td><td>37.7</td><td>50.3</td><td>31.8</td><td>35.2</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>107.8</td><td>-</td><td>49.2</td><td>-</td><td>32.8</td><td>-</td><td>24.2</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>62.9</td><td>-</td><td>31.3</td><td>-</td><td>21.6</td><td>-</td><td>16.4</td><td></td></tr><tr><td>Price/book (x)</td><td>21.5</td><td>-</td><td>15.6</td><td>-</td><td>13.1</td><td>-</td><td>11.2</td><td></td></tr><tr><td>Dividend yield (%)</td><td>0.3</td><td>-</td><td>1.8</td><td>-</td><td>2.8</td><td>-</td><td>3.8</td><td></td></tr><tr><td>ROE (%)</td><td>21.1</td><td>27.9</td><td>36.7</td><td>32.6</td><td>43.5</td><td>38.3</td><td>49.8</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>11.4</td><td>3.9</td><td>3.9</td><td>8.9</td><td>9.3</td><td>12.3</td><td>12.8</td><td></td></tr></table>

Source: Company data, NOM estimates  
Production Complete: 2026-07-14 13:48 UTC

<table><tr><td>RatingRemains</td><td>Buy</td></tr></table>

Target price
Increased from
CNY 95.00
CNY 195.00

<table><tr><td>Closing price14 July 2026</td><td>CNY 147.90</td></tr></table>

<table><tr><td>Implied upside</td><td>+31.8%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>47,489.2</td></tr><tr><td>ADT (USD mn)</td><td>1,397.0</td></tr></table>

## Relative performance chart

![](images/5c384109f943bc3975e43c819d7dc7b048d9a462a95fff3d22dd519e271f62c7.jpg)  
Source: LSEG, NOM

## Research Analysts

China Technology

Bing Duan - NIHK

bing.duan1@NOM.com

+852 2252 2141

Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

## Key data on Shengyi Technology

Cashflow statement (CNYmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (CNY)</td><td>-2.2</td><td>121.3</td><td>349.4</td><td>M cap (USDmn)</td><td>47,489.2</td></tr><tr><td>Absolute (USD)</td><td>-2.5</td><td>122.5</td><td>375.2</td><td>Free float (%)</td><td>48.7</td></tr><tr><td>Rel to CSI 300</td><td>-0.5</td><td>121.5</td><td>332.5</td><td>3-mth ADT (USDmn)</td><td>1,397.0</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>20,388</td><td>28,431</td><td>46,481</td><td>66,858</td><td>88,843</td></tr><tr><td>Cost of goods sold</td><td>-15,895</td><td>-20,905</td><td>-32,246</td><td>-45,713</td><td>-60,062</td></tr><tr><td>Gross profit</td><td>4,493</td><td>7,526</td><td>14,235</td><td>21,145</td><td>28,780</td></tr><tr><td>SG&amp;A</td><td>-2,495</td><td>-3,226</td><td>-5,042</td><td>-7,387</td><td>-10,260</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>1,998</td><td>4,300</td><td>9,193</td><td>13,758</td><td>18,521</td></tr><tr><td>EBITDA</td><td>2,835</td><td>5,187</td><td>10,391</td><td>15,105</td><td>20,021</td></tr><tr><td>Depreciation</td><td>-837</td><td>-887</td><td>-1,198</td><td>-1,347</td><td>-1,500</td></tr><tr><td>Amortisation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>1,998</td><td>4,300</td><td>9,193</td><td>13,758</td><td>18,521</td></tr><tr><td>Net interest expense</td><td>-70</td><td>-97</td><td>-159</td><td>-229</td><td>-304</td></tr><tr><td>Associates &amp; JCEs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other income</td><td>140</td><td>214</td><td>349</td><td>502</td><td>667</td></tr><tr><td>Earnings before tax</td><td>2,068</td><td>4,416</td><td>9,383</td><td>14,031</td><td>18,884</td></tr><tr><td>Income tax</td><td>-200</td><td>-524</td><td>-1,114</td><td>-1,666</td><td>-2,243</td></tr><tr><td>Net profit after tax</td><td>1,868</td><td>3,892</td><td>8,269</td><td>12,365</td><td>16,641</td></tr><tr><td>Minority interests</td><td>-129</td><td>-558</td><td>-973</td><td>-1,402</td><td>-1,818</td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>1,739</td><td>3,334</td><td>7,296</td><td>10,964</td><td>14,824</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>1,739</td><td>3,334</td><td>7,296</td><td>10,964</td><td>14,824</td></tr><tr><td>Dividends</td><td>-1,583</td><td>-972</td><td>-6,641</td><td>-9,980</td><td>-13,494</td></tr><tr><td>Transfer to reserves</td><td>156</td><td>2,362</td><td>654</td><td>983</td><td>1,330</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>203.5</td><td>107.8</td><td>49.2</td><td>32.8</td><td>24.2</td></tr><tr><td>Normalised P/E (x)</td><td>203.5</td><td>107.8</td><td>49.2</td><td>32.8</td><td>24.2</td></tr><tr><td>FD normalised P/E (x)</td><td>203.5</td><td>107.8</td><td>49.2</td><td>32.8</td><td>24.2</td></tr><tr><td>Dividend yield (%)</td><td>0.4</td><td>0.3</td><td>1.8</td><td>2.8</td><td>3.8</td></tr><tr><td>Price/cashflow (x)</td><td>243.0</td><td>68.1</td><td>77.1</td><td>45.8</td><td>31.3</td></tr><tr><td>Price/book (x)</td><td>24.1</td><td>21.5</td><td>15.6</td><td>13.1</td><td>11.2</td></tr><tr><td>EV/EBITDA (x)</td><td>114.7</td><td>62.9</td><td>31.3</td><td>21.6</td><td>16.4</td></tr><tr><td>EV/EBIT (x)</td><td>162.7</td><td>75.8</td><td>35.4</td><td>23.7</td><td>17.7</td></tr><tr><td>Gross margin (%)</td><td>22.0</td><td>26.5</td><td>30.6</td><td>31.6</td><td>32.4</td></tr><tr><td>EBITDA margin (%)</td><td>13.9</td><td>18.2</td><td>22.4</td><td>22.6</td><td>22.5</td></tr><tr><td>EBIT margin (%)</td><td>9.8</td><td>15.1</td><td>19.8</td><td>20.6</td><td>20.8</td></tr><tr><td>Net margin (%)</td><td>8.5</td><td>11.7</td><td>15.7</td><td>16.4</td><td>16.7</td></tr><tr><td>Effective tax rate (%)</td><td>9.7</td><td>11.9</td><td>11.9</td><td>11.9</td><td>11.9</td></tr><tr><td>Dividend payout (%)</td><td>91.0</td><td>29.1</td><td>91.0</td><td>91.0</td><td>91.0</td></tr><tr><td>ROE (%)</td><td>12.0</td><td>21.1</td><td>36.7</td><td>43.5</td><td>49.8</td></tr><tr><td>ROA (pretax %)</td><td>8.4</td><td>15.2</td><td>26.1</td><td>30.7</td><td>32.9</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>22.9</td><td>39.4</td><td>63.5</td><td>43.8</td><td>32.9</td></tr><tr><td>EBITDA</td><td>35.6</td><td>83.0</td><td>100.3</td><td>45.4</td><td>32.5</td></tr><tr><td>Normalised EPS</td><td>118.9</td><td>88.8</td><td>118.8</td><td>50.3</td><td>35.2</td></tr><tr><td>Normalised FDEPS</td><td>118.9</td><td>88.8</td><td>118.8</td><td>50.3</td><td>35.2</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>2,835</td><td>5,187</td><td>10,391</td><td>15,105</td><td>20,021</td></tr><tr><td>Change in working capital</td><td>-1,283</td><td>-567</td><td>-4,001</td><td>-4,628</td><td>-5,014</td></tr><tr><td>Other operating cashflow</td><td>-96</td><td>653</td><td>-1,730</td><td>-2,628</td><td>-3,531</td></tr><tr><td>Cashflow from operations</td><td>1,456</td><td>5,274</td><td>4,659</td><td>7,849</td><td>11,476</td></tr><tr><td>Capital expenditure</td><td>-926</td><td>-2,376</td><td>-2,676</td><td>-2,876</td><td>-3,076</td></tr><tr><td>Free cashflow</td><td>530</td><td>2,898</td><td>1,983</td><td>4,973</td><td>8,401</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td></td><td></td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>0</td><td>0</td><td></td><td></td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>0</td><td>0</td><td></td><td></td><td></td></tr><tr><td>Adjustments</td><td>-8</td><td>-557</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>522</td><td>2,341</td><td>1,983</td><td>4,973</td><td>8,401</td></tr><tr><td>Cash dividends</td><td>-1,192</td><td>-2,727</td><td>-972</td><td>-6,641</td><td>-9,980</td></tr><tr><td>Equity issue</td><td>773</td><td>35</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>-281</td><td>136</td><td>2,277</td><td>500</td><td>500</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>-582</td><td>-56</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-1,281</td><td>-2,613</td><td>1,306</td><td>-6,141</td><td>-9,480</td></tr><tr><td>Net cashflow</td><td>-759</td><td>-272</td><td>3,289</td><td>-1,168</td><td>-1,080</td></tr><tr><td>Beginning cash</td><td>2,775</td><td>2,016</td><td>1,744</td><td>5,033</td><td>3,865</td></tr><tr><td>Ending cash</td><td>2,016</td><td>1,744</td><td>5,033</td><td>3,865</td><td>2,785</td></tr><tr><td>Ending net debt</td><td>1,536</td><td>1,902</td><td>890</td><td>2,558</td><td>4,138</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>2,016</td><td>1,744</td><td>5,033</td><td>3,865</td><td>2,785</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>7,541</td><td>9,655</td><td>14,056</td><td>20,218</td><td>26,866</td></tr><tr><td>Inventories</td><td>5,119</td><td>5,786</td><td>8,411</td><td>11,924</td><td>15,667</td></tr><tr><td>Other current assets</td><td>1,937</td><td>2,204</td><td>2,204</td><td>2,204</td><td>2,204</td></tr><tr><td>Total current assets</td><td>16,613</td><td>19,389</td><td>29,704</td><td>38,211</td><td>47,522</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>9,105</td><td>11,083</td><td>12,420</td><td>13,808</td><td>15,242</td></tr><tr><td>Goodwill</td><td>626</td><td>620</td><td>620</td><td>620</td><td>620</td></tr><tr><td>Other intangible assets</td><td>1,300</td><td>1,678</td><td>1,652</td><td>1,627</td><td>1,601</td></tr><tr><td>Other LT assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total assets</td><td>27,643</td><td>32,770</td><td>44,396</td><td>54,265</td><td>64,986</td></tr><tr><td>Short-term debt</td><td>2,994</td><td>2,743</td><td>5,020</td><td>5,520</td><td>6,020</td></tr><tr><td>Accounts payable</td><td>6,609</td><td>9,059</td><td>12,084</td><td>17,131</td><td>22,508</td></tr><tr><td>Other current liabilities</td><td>247</td><td>278</td><td>278</td><td>278</td><td>278</td></tr><tr><td>Total current liabilities</td><td>9,849</td><td>12,080</td><td>17,382</td><td>22,929</td><td>28,806</td></tr><tr><td>Long-term debt</td><td>558</td><td>903</td><td>903</td><td>903</td><td>903</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>731</td><td>877</td><td>877</td><td>877</td><td>877</td></tr><tr><td>Total liabilities</td><td>11,138</td><td>13,859</td><td>19,162</td><td>24,709</td><td>30,586</td></tr><tr><td>Minority interest</td><td>1,600</td><td>2,187</td><td>2,187</td><td>2,187</td><td>2,187</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>2,429</td><td>2,429</td><td>2,429</td><td>2,429</td><td>2,429</td></tr><tr><td>Retained earnings</td><td>12,475</td><td>14,294</td><td>20,619</td><td>24,941</td><td>29,784</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total shareholders&#x27; equity</td><td>14,905</td><td>16,724</td><td>23,048</td><td>27,370</td><td>32,213</td></tr><tr><td>Total equity &amp; liabilities</td><td>27,643</td><td>32,770</td><td>44,396</td><td>54,265</td><td>64,986</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>1.69</td><td>1.61</td><td>1.71</td><td>1.67</td><td>1.65</td></tr><tr><td>Interest cover</td><td>28.4</td><td>44.2</td><td>57.8</td><td>60.2</td><td>61.0

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
