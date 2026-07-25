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
# CATL (300750.SZ)

# Earnings Review: 2Q26 results inline; demand outlook reaffirmed; largest A-share buyback announced to date; Buy

<table><tr><td>300750.SZ</td><td>12m Price Target: Rmb565.00</td><td>Price: Rmb383.01</td><td>Upside: 47.5%</td></tr><tr><td>3750.HK</td><td>12m Price Target: HK$947.00</td><td>Price: HK$622.00</td><td>Upside: 52.3%</td></tr></table>

CATL reported 2Q26 results after market close on July 24 and hosted an analyst call later that night. Net profit reached Rmb22.55bn in 2Q26, up 36% yoy, in line with our estimate and market expectations of Rmb22-23bn. The company also announced a Rmb20-40bn share buyback plan—the largest announced in the A-share market to date—to enhance shareholder returns. On the call, management reaffirmed a robust near-term demand outlook for 2H26 and 2027. Reiterate Buy.

## Key numbers

Battery sales volume was up +60% yoy to \~435GWh in 1H26 (vs. production: 498GWh), with ESS representing one-quarter of total. Implied 2Q26 sales volume was up +c.60% yoy to \~235GWh, sustaining the strong growth since 4Q25 (at \~60%).

Unit net profit was Rmb97/kWh, down 7% qoq from Rmb104/kWh in 1Q26 and Rmb103/kWh in 4Q25, reflecting the raw material cost inflation and unfavorable mix shift.

## Key takeaways

Demand: Management remains upbeat on 2H26/2027 demand and reiterated 20-30% long-term volume CAGR.

■ Capacity: Most capacity under construction (764GWh) should come online in the next 1-2 years, supporting growth amid high utilization and tight supply.

Sodium-ion: Large orders and flexible production lines support faster commercialization, with cost improvement tied to scale.

AIDC BESS: CATL expects AIDC-tailored power solutions to scale commercially over the next 1-2 years.

■ Policy: Consumption tax and export VAT changes are expected

## BUY

Nick Zheng, CFA
+852-2978-1405 | nick.zheng@gs.com
GS (Asia) L.L.C.

Selina Yan
+852-2978-0178 | shuling.yan@gs.com
GS (Asia) L.L.C.

Key Data
Market cap: Rmb1.8tr / \$270.5bn
Enterprise value: Rmb1.6tr / \$231.3bn
3m ADTV: Rmb14.3bn / \$2.1bn
China
China Battery, Machinery & Advanced Materials
M&A Rank: 3
Leases incl. in net debt & EV?: Yes

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn) New</td><td>423,701.8</td><td>598,596.9</td><td>712,248.9</td><td>787,315.3</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>423,701.8</td><td>611,723.6</td><td>728,340.7</td><td>804,085.7</td></tr><tr><td>EBITDA (Rmb mn)</td><td>100,832.9</td><td>136,728.3</td><td>169,419.5</td><td>196,913.8</td></tr><tr><td>EPS (Rmb) New</td><td>16.04</td><td>20.19</td><td>24.77</td><td>28.88</td></tr><tr><td>EPS (Rmb) Old</td><td>16.04</td><td>20.30</td><td>24.87</td><td>28.82</td></tr><tr><td>P/E (X)</td><td>18.5</td><td>19.0</td><td>15.5</td><td>13.3</td></tr><tr><td>P/B (X)</td><td>4.0</td><td>4.4</td><td>3.9</td><td>3.4</td></tr><tr><td>Dividend yield (%)</td><td>2.7</td><td>3.0</td><td>3.2</td><td>3.8</td></tr><tr><td>CROCI (%)</td><td>37.4</td><td>33.7</td><td>39.1</td><td>42.4</td></tr><tr><td></td><td>3/26</td><td>6/26</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>4.40</td><td>4.79</td><td>5.16</td><td>5.84</td></tr></table>

![](images/ad09dc00214a651f4641cccf6df743a1330ab152c73125654f9c502d64bb7359.jpg)  
Source: Company data, GS estimates. See disclosures for details.

CATL (300750.SZ) Rating since Jul 9, 2026

Growth & Margins (%)  
Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>18.5</td><td>19.0</td><td>15.5</td><td>13.3</td></tr><tr><td>P/B (X)</td><td>4.0</td><td>4.4</td><td>3.9</td><td>3.4</td></tr><tr><td>FCF yield (%)</td><td>6.6</td><td>5.2</td><td>7.1</td><td>8.5</td></tr><tr><td>EV/EBITDAR (X)</td><td>11.4</td><td>11.3</td><td>8.8</td><td>7.1</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>11.4</td><td>11.3</td><td>8.8</td><td>7.1</td></tr><tr><td>CROCI (%)</td><td>37.4</td><td>33.7</td><td>39.1</td><td>42.4</td></tr><tr><td>ROE (%)</td><td>24.7</td><td>25.3</td><td>26.6</td><td>27.1</td></tr><tr><td>Net debt/equity (%)</td><td>(58.4)</td><td>(67.0)</td><td>(74.9)</td><td>(82.7)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(58.4)</td><td>(67.0)</td><td>(74.9)</td><td>(82.7)</td></tr><tr><td>Interest cover (X)</td><td>27.2</td><td>41.2</td><td>44.6</td><td>48.1</td></tr><tr><td>Days inventory outst, sales</td><td>66.5</td><td>57.0</td><td>49.8</td><td>49.4</td></tr><tr><td>Receivable days</td><td>102.8</td><td>86.9</td><td>89.5</td><td>85.5</td></tr><tr><td>Days payable outstanding</td><td>269.9</td><td>242.0</td><td>249.3</td><td>258.4</td></tr><tr><td>DuPont ROE (%)</td><td>19.5</td><td>20.9</td><td>22.7</td><td>23.0</td></tr><tr><td>Turnover (X)</td><td>0.4</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Leverage (X)</td><td>2.6</td><td>2.5</td><td>2.5</td><td>2.4</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>304,411.4</td><td>336,582.6</td><td>360,105.2</td><td>381,444.3</td></tr><tr><td>Average capital employed (Rmb)</td><td>130,023.9</td><td>152,481.1</td><td>140,964.8</td><td>117,591.7</td></tr><tr><td>BVPS (Rmb)</td><td>73.87</td><td>86.99</td><td>99.37</td><td>113.82</td></tr></table>

Balance Sheet (Rmb mn)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>17.0</td><td>41.3</td><td>19.0</td><td>10.5</td></tr><tr><td>EBITDA growth</td><td>26.0</td><td>35.6</td><td>23.9</td><td>16.2</td></tr><tr><td>EPS growth</td><td>39.0</td><td>25.9</td><td>22.7</td><td>16.6</td></tr><tr><td>DPS growth</td><td>37.3</td><td>42.9</td><td>9.6</td><td>16.6</td></tr><tr><td>EBIT margin</td><td>17.5</td><td>17.1</td><td>17.9</td><td>18.9</td></tr><tr><td>EBITDA margin</td><td>23.8</td><td>22.8</td><td>23.8</td><td>25.0</td></tr><tr><td>Net income margin</td><td>17.0</td><td>15.9</td><td>16.6</td><td>17.5</td></tr></table>

Price Performance  
![](images/1d2df5f9a66d89367a2323d00432f2870fff1a4d3b601c101e95d00988a61219.jpg)  
Source: FactSet. Price as of 24 Jul 2026 close.

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>423,701.8</td><td>598,596.9</td><td>712,248.9</td><td>787,315.3</td></tr><tr><td>Cost of goods sold</td><td>(312,383.3)</td><td>(449,687.9)</td><td>(531,174.6)</td><td>(581,037.7)</td></tr><tr><td>SG&amp;A</td><td>(15,401.9)</td><td>(19,155.1)</td><td>(21,367.5)</td><td>(22,832.1)</td></tr><tr><td>R&amp;D</td><td>(22,146.6)</td><td>(27,535.5)</td><td>(32,407.3)</td><td>(35,429.2)</td></tr><tr><td>Other operating inc./(exp.)</td><td>463.5</td><td>403.5</td><td>487.8</td><td>806.3</td></tr><tr><td>EBITDA</td><td>100,832.9</td><td>136,728.3</td><td>169,419.5</td><td>196,913.8</td></tr><tr><td>Depreciation &amp; amortization</td><td>(26,599.3)</td><td>(34,106.4)</td><td>(41,632.3)</td><td>(48,091.3)</td></tr><tr><td>EBIT</td><td>74,233.6</td><td>102,621.9</td><td>127,787.2</td><td>148,822.6</td></tr><tr><td>Net interest inc./(exp.)</td><td>7,860.6</td><td>7,514.2</td><td>9,695.0</td><td>12,553.5</td></tr><tr><td>Income/(loss) from associates</td><td>7,353.1</td><td>11,193.2</td><td>10,942.6</td><td>11,692.9</td></tr><tr><td>Pre-tax profit</td><td>89,526.6</td><td>118,326.3</td><td>148,221.7</td><td>172,865.9</td></tr><tr><td>Provision for taxes</td><td>(12,740.2)</td><td>(17,157.3)</td><td>(22,233.3)</td><td>(25,929.9)</td></tr><tr><td>Minority interest</td><td>(4,585.0)</td><td>(6,070.1)</td><td>(7,559.3)</td><td>(8,816.2)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>72,201.3</td><td>95,098.8</td><td>118,429.1</td><td>138,119.8</td></tr><tr><td>Post-tax exceptionals</td><td>(7,693.4)</td><td>(9,517.7)</td><td>(11,253.5)</td><td>(12,439.6)</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>64,507.9</td><td>85,581.1</td><td>107,175.6</td><td>125,680.2</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>16.04</td><td>20.19</td><td>24.77</td><td>28.88</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>16.04</td><td>20.19</td><td>24.77</td><td>28.88</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>14.33</td><td>18.17</td><td>22.41</td><td>26.28</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>14.33</td><td>18.17</td><td>22.41</td><td>26.28</td></tr><tr><td>DPS (Rmb)</td><td>7.91</td><td>11.30</td><td>12.38</td><td>14.44</td></tr><tr><td>Div. payout ratio (%)</td><td>49.3</td><td>56.0</td><td>50.0</td><td>50.0</td></tr></table>

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>333,512.9</td><td>418,619.2</td><td>521,588.8</td><td>637,434.1</td></tr><tr><td>Accounts receivable</td><td>120,988.6</td><td>163,999.1</td><td>185,379.8</td><td>183,347.4</td></tr><tr><td>Inventory</td><td>94,526.2</td><td>92,401.6</td><td>101,869.1</td><td>111,431.9</td></tr><tr><td>Other current assets</td><td>89,453.8</td><td>89,451.6</td><td>92,565.4</td><td>94,622.0</td></tr><tr><td>Total current assets</td><td>638,481.5</td><td>764,471.6</td><td>901,403.1</td><td>1,026,835.4</td></tr><tr><td>Net PP&amp;E</td><td>176,133.7</td><td>205,320.9</td><td>226,204.1</td><td>225,189.2</td></tr><tr><td>Net intangibles</td><td>16,101.2</td><td>17,055.0</td><td>17,971.9</td><td>18,851.9</td></tr><tr><td>Total investments</td><td>81,181.2</td><td>92,974.4</td><td>104,517.0</td><td>116,809.9</td></tr><tr><td>Other long-term assets</td><td>62,929.9</td><td>61,097.7</td><td>59,942.2</td><td>59,213.5</td></tr><tr><td>Total assets</td><td>974,827.6</td><td>1,140,919.6</td><td>1,310,038.3</td><td>1,446,899.8</td></tr><tr><td>Accounts payable</td><td>263,606.0</td><td>332,645.8</td><td>392,923.7</td><td>429,808.7</td></tr><tr><td>Short-term debt</td><td>35,173.0</td><td>13,073.5</td><td>14,516.1</td><td>15,314.5</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>100,847.0</td><td>116,560.3</td><td>141,696.8</td><td>153,308.8</td></tr><tr><td>Total current liabilities</td><td>399,626.0</td><td>462,279.7</td><td>549,136.6</td><td>598,432.0</td></tr><tr><td>Long-term debt</td><td>81,678.4</td><td>100,161.4</td><td>115,645.3</td><td>125,330.8</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>122,496.9</td><td>122,496.9</td><td>122,496.9</td><td>122,496.9</td></tr><tr><td>Total long-term liabilities</td><td>204,175.2</td><td>222,658.3</td><td>238,142.2</td><td>247,827.6</td></tr><tr><td>Total liabilities</td><td>603,801.2</td><td>684,938.0</td><td>787,278.8</td><td>846,259.6</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>337,107.8</td><td>415,992.9</td><td>475,211.4</td><td>544,276.0</td></tr><tr><td>Minority interest</td><td>33,918.6</td><td>39,988.7</td><td>47,548.0</td><td>56,364.2</td></tr><tr><td>Total liabilities &amp; equity</td><td>974,827.5</td><td>1,140,919.6</td><td>1,310,038.3</td><td>1,446,899.8</td></tr><tr><td>Net debt, adjusted</td><td>(216,661.5)</td><td>(305,384.3)</td><td>(391,427.3)</td><td>(496,788.8)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>76,786.3</td><td>101,169.0</td><td>125,988.5</td><td>146,936.0</td></tr><tr><td>D&amp;A add-back</td><td>26,599.3</td><td>34,106.4</td><td>41,632.3</td><td>48,091.3</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>27,374.6</td><td>43,869.5</td><td>51,452.4</td><td>38,910.0</td></tr><tr><td>Other operating cash flow</td><td>2,459.8</td><td>(20,995.5)</td><td>(23,298.1)</td><td>(27,137.5)</td></tr><tr><td>Cash flow from operations</td><td>133,220.0</td><td>158,149.3</td><td>195,775.0</td><td>206,799.8</td></tr><tr><td>Capital expenditures</td><td>(42,344.6)</td><td>(62,415.2)</td><td>(62,276.8)</td><td>(47,227.6)</td></tr><tr><td>Acquisitions</td><td>(2,053.7)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>27.4</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(50,105.0)</td><td>9,405.4</td><td>11,958.6</td><td>15,047.7</td></tr><tr><td>Cash flow from investing</td><td>(94,475.8)</td><td>(53,009.9)</td><td>(50,318.3)</td><td>(32,179.9)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(34,923.0)</td><td>(54,034.5)</td><td>(59,210.6)</td><td>(69,055.3)</td></tr><tr><td>Inc/(dec) in debt</td><td>(11,912.0)</td><td>(173.0)</td><td>16,926.5</td><td>10,483.9</td></tr><tr><td>Other financing cash flows</td><td>38,091.7</td><td>34,174.3</td><td>(203.1)</td><td>(203.1)</td></tr><tr><td>Cash flow from financing</td><td>(8,743.3)</td><td>(20,033.2)</td><td>(42,487.2)</td><td>(58,774.5)</td></tr><tr><td>Total cash flow</td><td>30,000.9</td><td>85,106.3</td><td>102,969.6</td><td>115,845.3</td></tr><tr><td>Free cash flow</td><td>90,875.4</td><td>95,734.1</td><td>133,498.2</td><td>159,572.2</td></tr></table>

Source: Company data, GS estimates.

to have limited impact and favor industry leaders.

## 2Q26/1H26 Results Summary

## Topline Performance

2Q26 revenue reached a record Rmb147.79bn (+57% yoy), 3% above GSe. 1H26 revenue was Rmb276.92bn (+55% yoy, +15% hoh). Segment details are as follows:

Power Battery: 1H26 sales reached Rmb192.13bn (+46% yoy), supported by strong volume growth (+50% yoy). Estimated 2Q26 sales volume increased +46% yoy. Management highlighted a +5.6ppt domestic power battery market share expansion in 1H26 and a +3.7ppt yoy overseas market share gain in 5M26.

■ ESS: 1H26 sales grew +88% yoy to Rmb53.26bn, with volume nearly doubling yoy to account for 25% of total sales volume (vs. 20% previously). Implied 2Q26 volume more than doubled yoy.

☐ Regional mix: management mentioned overseas shipments now account for nearly 50%. Management highlighted order wins across Germany, Spain, Chile, Australia, and Malaysia (CATL acts as a system integrator), with overseas order growth outpacing domestic.

☐ By product, battery sales contributed 60%+ of ESS segment sales, with the rest from system integration and supporting services.

☐ ASP Strategy: Despite industry-wide price competition, CATL focuses on value over price, leveraging product safety, lifespan, performance, system integration, and comprehensive after-sales services to win clients.

■ Battery Recycling & Minerals: 1H26 sales grew strongly by +67% yoy.

\- Geographic breakdown: Robust growth was seen across both domestic (+61% yoy) and overseas (+42% yoy) markets.

## Profitability

Margin: 2Q26 GPM of 23.2% (-2.4ppt yoy) was -1.2ppt below GSe. Management attributed GPM contraction to product mix shift and raw material cost inflation. Looking ahead, management shared cost inflation could be passed downstream through metal-cost-linked pricing mechanism.

2Q26 EBITM was 17.2% (-0.2ppt yoy), +0.8ppt above GSe, with EBIT of Rmb25.48bn (+55% yoy) +8% above GSe. It was mainly supported by lower-than-expected opex (opex ratio down to a historical-low level) from lower admin expenses and impairment losses, higher investment gains (mostly FX hedging activities), partially offset by lower other non-operating profit.

■ 1H26 EBITDA reached a record Rmb64.98bn, +54% yoy/+11% hoh.

Net Profit: Below the EBIT line, net finance income was Rmb693mn vs. Rmb3.53bn in 2Q25 due to unfavorable FX movements (FX loss est

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
