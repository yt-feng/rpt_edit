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
# Seagate Technology

# Solid visibility, improving pricing trends drive upside; PO stays at \$1,150

Reiterate Rating: BUY | PO: 1,150.00 USD | Price: 747.30 USD

## Strong beat & raise; strength and durability intact

STX shares traded higher after-hours as STX beat F4Q expectations & guided F1Q27 rev/EPS materially above BofA & Street ests. F4Q GM of 52.7% was above our est of 50.2%. F1Q guide implies GM of 57.3% (on mid-pt), & mgmt expects rev & margins to increase sequentially throughout F27 & expects F27 rev growth to exceed F26 (>34% y/y). Visibility continues to improve with build-to-order contracts through the end of F27, while vast majority of nearline EB is now allocated into C28 & customers are extending planning horizons into C29 & beyond. Reiterate Buy on secular demand from cloud, continued pricing & margin improvement, and STX's path toward higher-capacity HAMR HDDs.

## Strong pricing supports continued margin expansion

STX delivered incremental GM of 83.2% y/y in F4Q, while F1Q guidance implies incremental GM of \~88% y/y, reflecting favorable pricing, higher capacity nearline mix, and continued cost improvements. Mgmt noted the supply/demand gap has widened and incremental EBs available above contracted volumes are being sold at higher prices. While the expiration of preferential pricing for STX's initial HAMR customer provides a modest F1Q benefit, mgmt indicated this is not the primary driver of the pricing improvement. Broader demand & customers seeking volume are more meaningful.

## Other takeaways from the earnings call

HAMR was \~40% of nearline shipment run rate exiting F26. Mozaic 4+ was a contributor in F4Q, should contribute more in F1Q, and is expected to continue ramping through F27. 50% of HAMR EB is expected to be on Mozaic 4+ exiting C26, while Mozaic 5+ qual shipments remain on track for late C27. Nearline supply is largely allocated into C28, with customers extending planning into C29. STX reiterated mid-20% EB growth target. Longer term, data growth is broadening beyond traditional workloads as inference & agentic apps (and eventually physical AI) create and retain more unstructured data.

## Adjusting estimates; PO stays at \$1,150

Our F27 revenue/EPS move to \$17.5bn/\$32.06 from \$16.9bn/\$26.88. Our PO stays at \$1,150 on 19x (unchanged) C28 EPS of \$61.42 (prior \$61.24).

<table><tr><td>Estimates (Jun) (US$)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>EPS</td><td>8.11</td><td>15.59</td><td>32.06</td><td>54.06</td><td>71.64</td></tr><tr><td>GAAP EPS</td><td>6.87</td><td>14.03</td><td>31.28</td><td>52.73</td><td>69.85</td></tr><tr><td>EPS Change (YoY)</td><td>528.7%</td><td>92.2%</td><td>105.6%</td><td>68.6%</td><td>32.5%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>27.76</td><td>41.61</td><td>NA</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>28.40</td><td>48.31</td><td>67.81</td></tr><tr><td>DPS</td><td>2.84</td><td>2.94</td><td>2.96</td><td>2.96</td><td>2.96</td></tr><tr><td colspan="6">Valuation (Jun)</td></tr><tr><td>P/E</td><td>92.1x</td><td>47.9x</td><td>23.3x</td><td>13.8x</td><td>10.4x</td></tr><tr><td>GAAP P/E</td><td>108.8x</td><td>53.3x</td><td>23.9x</td><td>14.2x</td><td>10.7x</td></tr><tr><td>Dividend Yield</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td></tr><tr><td>EV / EBITDA*</td><td>69.2x</td><td>34.8x</td><td>17.6x</td><td>10.6x</td><td>8.2x</td></tr><tr><td>Free Cash Flow Yield*</td><td>0.5%</td><td>1.9%</td><td>3.4%</td><td>4.8%</td><td>7.1%</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 6.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 7 to 9. Analyst Certification on page 5. Price Objective Basis/Risk on page 5.

## 28 July 2026

Equity

## Key Changes

<table><tr><td>(US$)</td><td>Previous</td><td>Current</td></tr><tr><td>2027E Rev (m)</td><td>16,860.0</td><td>17,470.2</td></tr><tr><td>2028E Rev (m)</td><td>26,238.4</td><td>26,370.0</td></tr><tr><td>2029E Rev (m)</td><td>NA</td><td>33,629.1</td></tr><tr><td>2027E EPS</td><td>26.88</td><td>32.06</td></tr><tr><td>2028E EPS</td><td>50.75</td><td>54.06</td></tr><tr><td>2029E EPS</td><td>NA</td><td>71.64</td></tr><tr><td>2027E DPS</td><td>2.88</td><td>2.96</td></tr></table>

## Wamsi Mohan

Research Analyst
BofAS
+1 646 855 3854
wamsi.mohan@bofa.com

## Ruplu Bhattacharya

Research Analyst
BofAS
+1 646 855 0315
ruplu.bhattacharya@bofa.com

## Ryan Seungin Choi

Research Analyst
BofAS
+1 646 743 0587
ryan.choi2@bofa.com

## Aisling Grueninger

Research Analyst
BofAS
+1 646 855 4273
aisling.grueninger@bofa.com

## Stock Data

<table><tr><td>Price</td><td>747.30 USD</td></tr><tr><td>Price Objective</td><td>1,150.00 USD</td></tr><tr><td>Date Established</td><td>1-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>C-1-7</td></tr><tr><td>52-Week Range</td><td>138.30 USD - 1,145.00 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>167,566 USD / 224.2</td></tr><tr><td>Free Float</td><td>99.8%</td></tr><tr><td>Average Daily Value (mn)</td><td>3889.34 USD</td></tr><tr><td>BofA Ticker / Exchange</td><td>STX / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>STX US / STX.OQ</td></tr><tr><td>ROE (2027E)</td><td>132.2%</td></tr><tr><td>Net Dbt to Eqty (Jun-2026A)</td><td>85.9%</td></tr></table>

## Abbreviations are on page 4

## iQprofile $^{SM}$ Seagate Technology

iQmethod $^{SM}$ – Bus Performance\*

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Return on Capital Employed</td><td>36.9%</td><td>61.0%</td><td>73.1%</td><td>64.4%</td><td>49.6%</td></tr><tr><td>Return on Equity</td><td>NM</td><td>412.9%</td><td>132.2%</td><td>83.5%</td><td>57.0%</td></tr><tr><td>Operating Margin</td><td>21.1%</td><td>34.7%</td><td>50.3%</td><td>56.1%</td><td>57.5%</td></tr><tr><td>Free Cash Flow</td><td>818</td><td>3,105</td><td>5,676</td><td>8,067</td><td>11,868</td></tr></table>

iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Cash Realization Ratio</td><td>0.6x</td><td>1.0x</td><td>0.9x</td><td>0.7x</td><td>0.8x</td></tr><tr><td>Asset Replacement Ratio</td><td>1.1x</td><td>2.1x</td><td>3.1x</td><td>4.5x</td><td>5.4x</td></tr><tr><td>Tax Rate</td><td>3.8%</td><td>15.5%</td><td>16.0%</td><td>16.0%</td><td>16.0%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>NM</td><td>85.9%</td><td>-31.6%</td><td>-47.6%</td><td>-56.0%</td></tr><tr><td>Interest Cover</td><td>6.6x</td><td>15.7x</td><td>43.5x</td><td>NM</td><td>NM</td></tr></table>

Income Statement Data (Jun)

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Sales</td><td>9,097</td><td>12,195</td><td>17,470</td><td>26,370</td><td>33,629</td></tr><tr><td>% Change</td><td>38.9%</td><td>34.1%</td><td>43.3%</td><td>50.9%</td><td>27.5%</td></tr><tr><td>Gross Profit</td><td>3,200</td><td>5,558</td><td>10,227</td><td>16,320</td><td>20,930</td></tr><tr><td>% Change</td><td>108.3%</td><td>73.7%</td><td>84.0%</td><td>59.6%</td><td>28.2%</td></tr><tr><td>EBITDA</td><td>2,378</td><td>4,726</td><td>9,333</td><td>15,476</td><td>20,148</td></tr><tr><td>% Change</td><td>152.7%</td><td>98.7%</td><td>97.5%</td><td>65.8%</td><td>30.2%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>(325)</td><td>(264)</td><td>(119)</td><td>54</td><td>336</td></tr><tr><td>Net Income (Adjusted)</td><td>1,734</td><td>3,539</td><td>7,500</td><td>12,797</td><td>16,944</td></tr><tr><td>% Change</td><td>537.6%</td><td>104.1%</td><td>111.9%</td><td>70.6%</td><td>32.4%</td></tr></table>

## Free Cash Flow Data (Jun)

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>1,733</td><td>3,538</td><td>7,500</td><td>12,797</td><td>16,945</td></tr><tr><td>Depreciation &amp; Amortization</td><td>251</td><td>276</td><td>285</td><td>296</td><td>311</td></tr><tr><td>Change in Working Capital</td><td>(965)</td><td>(159)</td><td>(1,316)</td><td>(3,787)</td><td>(3,787)</td></tr><tr><td>Deferred Taxation Charge</td><td>(8)</td><td>(34)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Adjustments, Net</td><td>72</td><td>53</td><td>79</td><td>80</td><td>80</td></tr><tr><td>Capital Expenditure</td><td>(265)</td><td>(569)</td><td>(874)</td><td>(1,319)</td><td>(1,681)</td></tr><tr><td>Free Cash Flow</td><td>818</td><td>3,105</td><td>5,676</td><td>8,067</td><td>11,868</td></tr><tr><td>% Change</td><td>23.2%</td><td>279.6%</td><td>82.8%</td><td>42.1%</td><td>47.1%</td></tr><tr><td>Share / Issue Repurchase</td><td>72</td><td>(120)</td><td>(140)</td><td>(140)</td><td>(140)</td></tr><tr><td>Cost of Dividends Paid</td><td>(607)</td><td>(634)</td><td>(692)</td><td>(701)</td><td>(700)</td></tr><tr><td>Change in Debt</td><td>(678)</td><td>(1,442)</td><td>0</td><td>0</td><td>0</td></tr></table>

Balance Sheet Data (Jun)

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Cash &amp; Equivalents</td><td>891</td><td>1,704</td><td>6,554</td><td>13,786</td><td>24,820</td></tr><tr><td>Trade Receivables</td><td>959</td><td>1,534</td><td>2,088</td><td>4,323</td><td>6,200</td></tr><tr><td>Other Current Assets</td><td>1,803</td><td>1,983</td><td>2,873</td><td>5,220</td><td>6,745</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>1,657</td><td>2,034</td><td>2,882</td><td>4,165</td><td>5,795</td></tr><tr><td>Other Non-Current Assets</td><td>2,713</td><td>2,717</td><td>2,717</td><td>2,717</td><td>2,717</td></tr><tr><td>Total Assets</td><td>8,023</td><td>9,972</td><td>17,115</td><td>30,212</td><td>46,278</td></tr><tr><td>Short-Term Debt</td><td>0</td><td>185</td><td>185</td><td>185</td><td>185</td></tr><tr><td>Other Current Liabilities</td><td>2,648</td><td>2,942</td><td>3,071</td><td>3,865</td><td>3,481</td></tr><tr><td>Long-Term Debt</td><td>4,995</td><td>3,380</td><td>3,465</td><td>3,380</td><td>3,380</td></tr><tr><td>Other Non-Current Liabilities</td><td>833</td><td>1,298</td><td>1,091</td><td>1,298</td><td>1,298</td></tr><tr><td>Total Liabilities</td><td>8,476</td><td>7,805</td><td>7,812</td><td>8,728</td><td>8,344</td></tr><tr><td>Total Equity</td><td>(453)</td><td>2,167</td><td>9,181</td><td>21,483</td><td>37,934</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>8,023</td><td>9,972</td><td>16,993</td><td>30,212</td><td>46,278</td></tr></table>

\* For full definitions of IQmethod $^{SM}$ measures, see page 6.

## Company Sector

IT Hardware

## Company Description

Seagate Technology (STX) designs, manufactures and markets hard disk drives for use in enterprise storage, servers, desktops, laptop computers, and other consumer electronic devices. It also has a growing solid state drive and storage systems portfolio. The company sells its products directly to OEMs, as well as distributors and retailers, and its production capabilities are vertically integrated.

## Investment Rationale

We expect revenue and earnings to inflect higher as legacy market headwinds become smaller and mass capacity needs increase net of any cannibalization from Flash. We expect overall industry margins to improve and strong shareholder returns to continue. We rate STX Buy.

## Stock Data

<table><tr><td>Average Daily Volume</td><td>5,204,519</td></tr></table>

## Quarterly Earnings Estimates

<table><tr><td></td><td>2026</td><td>2027</td></tr><tr><td>Q1</td><td>2.61A</td><td>7.40E</td></tr><tr><td>Q2</td><td>3.11A</td><td>7.99E</td></tr><tr><td>Q3</td><td>4.10A</td><td>7.77E</td></tr><tr><td>Q4</td><td>5.71A</td><td>8.88E</td></tr></table>

## Model

Figure 1: STX guided F1Q27 revs of \$4.1bn and EPS of \$7.30 (both at the mid-point)
STX Income Statement

<table><tr><td rowspan="2">Seagate Technology Inc. (STX)($ Millions Except Per Share Data)</td><td colspan="4">F2026E</td><td colspan="9">F2027E</td></tr><tr><td>9/25A</td><td>12/25</td><td>3/26</td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td><td>6/27E</td><td>F2024</td><td>F2025</td><td>F2026</td><td>F2027E</td><td>F2028E</td></tr><tr><td colspan="14">Income Statement</td></tr><tr><td>Revenue</td><td>$2,629.0</td><td>$2,825.0</td><td>$3,112.0</td><td>$3,629.0</td><td>$4,150.0</td><td>$4,379.5</td><td>$4,242.5</td><td>$4,698.2</td><td>$6,551.0</td><td>$9,097.0</td><td>$12,195.0</td><td>$17,470.2</td><td>$26,370.0</td></tr><tr><td>Cost of Goods Sold (post options)</td><td>1,592.0</td><td>1,649.0</td><td>1,665.0</td><td>1,731.0</td><td>1,785.4</td><td>1,839.3</td><td>1,742.0</td><td>1,876.9</td><td>5,015.0</td><td>5,897.0</td><td>6,637.0</td><td>7,243.5</td><td>10,049.6</td></tr><tr><td>Gross Profit (Post Options Expense)</td><td>1,040.0</td><td>1,178.0</td><td>1,449.0</td><td>1,899.0</td><td>2,365.6</td><td>2,541.2</td><td>2,501.6</td><td>2,822.4</td><td>1,638.0</td><td>3,204.0</td><td>5,566.0</td><td>10,230.7</td><td>16,324.4</td></tr><tr><td>Total Operating Expenses (Post Options Expense)</td><td>319.0</td><td>330.0</td><td>336.0</td><td>334.0</td><td>346.9</td><td>355.8</td><td>366.5</td><td>375.4</td><td>1,088.0</td><td>1,277.0</td><td>1,319.0</td><td>1,444.7</td><td>1,539.6</td></tr><tr><td>R&amp;D (incl SBC)</td><td>186.0</td><td>187.0</td><td>194.0</td><td>188.0</td><td>195.5</td><td>201.4</td><td>207.4</td><td>211.6</td><td>654.0</td><td>724.0</td><td>755.0</td><td>815.9</td><td>867.7</td></tr><tr><td>SG&amp;A (Incl SBC)</td><td>144.0</td><td>143.0</td><td>143.0</td><td>147.0</td><td>151.4</td><td>154.4</td><td>159.1</td><td>163.8</td><td>460.0</td><td>561.0</td><td>577.0</td><td>628.8</td><td>671.9</td></tr><tr><td>Operating Income (Post Options Expense)</td><td>721.0</td><td>848.0</td><td>1,113.0</td><td>1,565.0</td><td>2,018.6</td><td>2,185.4</td><td>2,135.1</td><td>2,446.9</td><td>550.0</td><td>1,927.0</td><td>4,247.0</td><td>8,786.0</td><td>14,784.8</td></tr><tr><td>Operating Income (Pre Options Expense)</td><td>763.0</td><td>901.0</td><td>1,167.0</td><td>1,619.0</td><td>2,080.9</td><td>2,251.1</td><td>2,198.7</td><td>2,517.4</td><td>677.0</td><td>2,127.0</td><td>4,450.0</td><td>9,048.1</td><td>15,180.3</td></tr><tr><td>Total Interest and Other Income/(Expense)</td><td>(74.0)</td><td>(70.0)</td><td>(62.0)</td><td>(58.0)</td><td>(45.1)</td><td>(35.9)</td><td>(24.8)</td><td>(13.4)</td><td>(343.0)</td><td>(325.0)</td><td>(264.0)</td><td>(119.2)</td><td>54.0</td></tr><tr><td>Interest Income</td><td>7.0</td><td>7.0</td><td>6.0</td><td>10.0</td><td>14.9</td><td>24.1</td><td>35.2</td><td>46.6</td><td>15.0</td><td>25.0</td><td>30.0</td><td>120.8</td><td>294.0</td></tr><tr><td>Interest Expense</td><td>(80.0)</td><td>(72.0)</td><td>(68.0)</td><td>(64.0)</td><td>(52.0)</td><td>(52.0)</td><td>(52.0)</td><td>(52.0)</td><td>(332.0)</td><td>(321.0)</td><td>(284.0)</td><td>(208.0)</td><td>(208.0)</td></tr><tr><td>Other Income/(Expense)</td><td>(1.0)</td><td>(5.0)</td><td>0.0</td><td>(4.0)</td><td>(8.0)</td><td>(8.0)</td><td>(8.0)</td><td>(8.0)</td><td>(26.0)</td><td>(29.0)</td><td>(10.0)</td><td>(32.0)</td><td>(32.0)</td></tr><tr><td>Pretax Income (Pre Options Expense)</td><td>689.0</td><td>831.0</td><td>1,105.0</td><td>1,561.0</td><td>2,035.8</td><td>2,215.2</td><td>2,173.9</td><td>2,504.0</td><td>334.0</td><td>1,802.0</td><td>4,186.0</td><td>8,928.9</td><td>15,234.3</td></tr><tr><td>Income Taxes Expense/(Credit)</td><td>106.0</td><td>129.0<

[中间内容因长度限制已省略]

 the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This

information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
