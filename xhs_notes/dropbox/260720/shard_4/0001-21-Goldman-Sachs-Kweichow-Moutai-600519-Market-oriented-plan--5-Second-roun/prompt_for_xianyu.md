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
# Kweichow Moutai (600519.SS)

# Market-oriented plan #5: Second round of unexpected ex-factory and suggested retail price hike of Feitian in July 2026; Buy

600519.SS 12m Price Target: Rmb1,667.00 Price: Rmb1,253.00 Upside: 33.0%

What's New: Kweichow Moutai officially announced a new round of price hikes for Feitian Moutai on July 17, effective immediately on July 18, 2026. Kweichow Moutai raised the ex-factory price of Feitian Moutai (53% vol, 500ml, 2026 edition) by 7.9% or Rmb100/bottle from Rmb1,269/bottle to Rmb1,369/bottle (mainly covering wholesale channels), and the suggested retail sales price (RSP) of Feitian Moutai on i-Moutai platform by 6.5% or Rmb100 per bottle from Rmb1,539/bottle to Rmb1,639/bottle (mainly covering direct sales channels). Recalling that the company raised Feitian Moutai's ex-factory price/RSP by Rmb100/Rmb40 per bottle on 31 March, this move marks the second price hike for Feitian this year, which is more frequently vs. its historic pattern of raising prices once every few years (Exhibit 1). Price hikes in aggregate this year have amounted to 17%/9% for ex-factory price and RSP of 500ml Feitian Moutai, respectively, post July 18, 2026 vs. 2025, after the two rounds of price hikes, which we expect to contribute more to 2H26 results. Other prices hikes for 500ml Feitian based on our channel checks: Meanwhile, group-buy RSP of 500ml Feitian in self-operated specialty stores has increased to Rmb1,719 per bottle (vs. Rmb1,639 new RSP in i-Moutai), and direct exfactory price to KA/E-commerce platforms has also increased to Rmb1,529 from Rmb1,399 per bottle. In addition, according to the i-Moutai announcement, Feitian 53% vol 1L Feitian Moutai RSP increased by 4.8%, or Rmb150/bottle, from Rmb3,119/bottle to Rmb3,269/bottle.

GSE Sales and Earnings impact to 2026: We estimate a $1.2\%$ incremental sales, and $1.6\%$ incremental earnings contribution to 2026 applying a $30\%$ pro-rata to wholesale channels/c.40% pro-rata to Direct sales channels (see Exhibit 2), but estimate a c.3%/4%+ sale/earnings accretion to 2027. We view this price hike action as a continued positive signal built on the constructive market feedback and stable wholesale price trends observed after the Mar price hike (see Our recent spirits in-depth research)

## BUY

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Key Data

Market cap: Rmb1.6tr / \$232.3bn  
Enterprise value: Rmb1.4tr / \$210.4bn  
3m ADTV: Rmb5.9bn / \$866.6mn  
China  
China Consumer Staples  
M&A Rank: 3  
Leases incl. in net debt & EV?: No

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn) New</td><td>172,054.2</td><td>178,763.9</td><td>193,635.5</td><td>204,873.9</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>172,054.2</td><td>177,167.1</td><td>188,628.5</td><td>199,593.6</td></tr><tr><td>EBITDA (Rmb mn)</td><td>116,165.1</td><td>119,126.5</td><td>130,240.6</td><td>138,515.9</td></tr><tr><td>EPS (Rmb) New</td><td>65.74</td><td>67.79</td><td>74.23</td><td>78.99</td></tr><tr><td>EPS (Rmb) Old</td><td>65.74</td><td>67.07</td><td>71.96</td><td>76.59</td></tr><tr><td>P/E (X)</td><td>22.5</td><td>18.5</td><td>16.9</td><td>15.9</td></tr><tr><td>P/B (X)</td><td>7.6</td><td>6.0</td><td>5.5</td><td>5.1</td></tr><tr><td>Dividend yield (%)</td><td>3.5</td><td>4.2</td><td>4.6</td><td>4.7</td></tr><tr><td>CROCI (%)</td><td>32.6</td><td>29.9</td><td>29.9</td><td>28.9</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>21.75</td><td>14.52</td><td>15.62</td><td>15.89</td></tr></table>

GS Factor Profile

![](images/7ae9e894085847c41cfc706068be7547ff498a9723f7cd6deb3294d33b2959b2.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Kweichow Moutai (600519.SS) Rating since Nov 23, 2021

BUY

Growth & Margins (%)  
Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>22.5</td><td>18.5</td><td>16.9</td><td>15.9</td></tr><tr><td>P/B (X)</td><td>7.6</td><td>6.0</td><td>5.5</td><td>5.1</td></tr><tr><td>FCF yield (%)</td><td>3.1</td><td>4.7</td><td>5.4</td><td>5.7</td></tr><tr><td>EV/EBITDAR (X)</td><td>14.7</td><td>11.9</td><td>10.8</td><td>10.0</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>14.7</td><td>11.9</td><td>10.8</td><td>10.0</td></tr><tr><td>CROCI (%)</td><td>32.6</td><td>29.9</td><td>29.9</td><td>28.9</td></tr><tr><td>ROE (%)</td><td>34.5</td><td>33.4</td><td>33.9</td><td>33.3</td></tr><tr><td>Net debt/equity (%)</td><td>(59.4)</td><td>(58.2)</td><td>(60.0)</td><td>(60.8)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(59.4)</td><td>(58.2)</td><td>(60.0)</td><td>(60.8)</td></tr><tr><td>Interest cover (X)</td><td>3,966.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Days inventory outst, sales</td><td>122.8</td><td>137.0</td><td>140.4</td><td>139.0</td></tr><tr><td>Receivable days</td><td>7.0</td><td>9.4</td><td>9.2</td><td>9.3</td></tr><tr><td>Days payable outstanding</td><td>758.3</td><td>681.8</td><td>723.3</td><td>722.2</td></tr><tr><td>DuPont ROE (%)</td><td>32.4</td><td>30.8</td><td>30.9</td><td>30.1</td></tr><tr><td>Turnover (X)</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Leverage (X)</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.2</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>272,555.4</td><td>296,886.5</td><td>324,146.4</td><td>355,105.0</td></tr><tr><td>Average capital employed (Rmb)</td><td>79,350.3</td><td>109,276.7</td><td>117,879.1</td><td>124,709.1</td></tr><tr><td>BVPS (Rmb)</td><td>195.36</td><td>210.37</td><td>227.44</td><td>247.19</td></tr></table>

Balance Sheet (Rmb mn)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(1.2)</td><td>3.9</td><td>8.3</td><td>5.8</td></tr><tr><td>EBITDA growth</td><td>(3.3)</td><td>2.5</td><td>9.3</td><td>6.4</td></tr><tr><td>EPS growth</td><td>(4.2)</td><td>3.1</td><td>9.5</td><td>6.4</td></tr><tr><td>DPS growth</td><td>0.9</td><td>1.8</td><td>8.1</td><td>3.6</td></tr><tr><td>EBIT margin</td><td>66.2</td><td>65.3</td><td>66.0</td><td>66.3</td></tr><tr><td>EBITDA margin</td><td>67.5</td><td>66.6</td><td>67.3</td><td>67.6</td></tr><tr><td>Net income margin</td><td>47.8</td><td>47.5</td><td>48.0</td><td>48.3</td></tr></table>

Price Performance  
![](images/6a2d6ed175517cdfbc2d019149904f5f41a134cd6900a3edb3a8eca0a918139c.jpg)  
Source: FactSet. Price as of 17 Jul 2026 close.

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>172,054.2</td><td>178,763.9</td><td>193,635.5</td><td>204,873.9</td></tr><tr><td>Cost of goods sold</td><td>(15,068.2)</td><td>(17,857.4)</td><td>(18,679.1)</td><td>(19,601.6)</td></tr><tr><td>SG&amp;A</td><td>(42,927.8)</td><td>(44,055.0)</td><td>(47,139.1)</td><td>(49,321.8)</td></tr><tr><td>R&amp;D</td><td>(190.1)</td><td>(89.4)</td><td>(96.8)</td><td>(102.4)</td></tr><tr><td>Other operating inc./(exp.)</td><td>93.4</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>116,165.1</td><td>119,126.5</td><td>130,240.6</td><td>138,515.9</td></tr><tr><td>Depreciation &amp; amortization</td><td>(2,203.6)</td><td>(2,364.4)</td><td>(2,520.0)</td><td>(2,667.9)</td></tr><tr><td>EBIT</td><td>113,961.5</td><td>116,762.1</td><td>127,720.6</td><td>135,848.1</td></tr><tr><td>Net interest inc./(exp.)</td><td>815.2</td><td>679.6</td><td>723.5</td><td>812.4</td></tr><tr><td>Income/(loss) from associates</td><td>0.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>114,755.3</td><td>117,419.6</td><td>128,422.1</td><td>136,638.5</td></tr><tr><td>Provision for taxes</td><td>(29,444.9)</td><td>(29,354.9)</td><td>(32,105.5)</td><td>(34,159.6)</td></tr><tr><td>Minority interest</td><td>(2,990.3)</td><td>(3,169.7)</td><td>(3,359.9)</td><td>(3,561.4)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>82,320.1</td><td>84,895.1</td><td>92,956.7</td><td>98,917.4</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>82,320.1</td><td>84,895.1</td><td>92,956.7</td><td>98,917.4</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>65.74</td><td>67.79</td><td>74.23</td><td>78.99</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>65.74</td><td>67.79</td><td>74.23</td><td>78.99</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>65.74</td><td>67.79</td><td>74.23</td><td>78.99</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>65.74</td><td>67.79</td><td>74.23</td><td>78.99</td></tr><tr><td>DPS (Rmb)</td><td>51.93</td><td>52.88</td><td>57.16</td><td>59.24</td></tr><tr><td>Div. payout ratio (%)</td><td>79.0</td><td>78.0</td><td>77.0</td><td>75.0</td></tr></table>

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>150,786.8</td><td>160,545.0</td><td>180,288.6</td><td>199,915.6</td></tr><tr><td>Accounts receivable</td><td>4,502.6</td><td>4,678.1</td><td>5,067.0</td><td>5,361.0</td></tr><tr><td>Inventory</td><td>61,427.4</td><td>72,798.3</td><td>76,147.8</td><td>79,908.6</td></tr><tr><td>Other current assets</td><td>35,801.8</td><td>41,172.1</td><td>47,347.9</td><td>54,450.1</td></tr><tr><td>Total current assets</td><td>252,518.7</td><td>279,193.5</td><td>308,851.4</td><td>339,635.3</td></tr><tr><td>Net PP&amp;E</td><td>24,961.1</td><td>26,844.0</td><td>28,718.9</td><td>30,491.0</td></tr><tr><td>Net intangibles</td><td>8,802.6</td><td>8,988.1</td><td>9,158.6</td><td>9,314.1</td></tr><tr><td>Total investments</td><td>150.3</td><td>210.3</td><td>270.3</td><td>330.3</td></tr><tr><td>Other long-term assets</td><td>17,402.2</td><td>17,402.2</td><td>17,402.2</td><td>17,402.2</td></tr><tr><td>Total assets</td><td>303,834.8</td><td>332,638.1</td><td>364,401.4</td><td>397,172.9</td></tr><tr><td>Accounts payable</td><td>30,532.9</td><td>36,184.9</td><td>37,849.8</td><td>39,719.1</td></tr><tr><td>Short-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>19,077.5</td><td>20,262.1</td><td>25,620.6</td><td>28,232.0</td></tr><tr><td>Total current liabilities</td><td>49,610.5</td><td>56,447.0</td><td>63,470.4</td><td>67,951.2</td></tr><tr><td>Long-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>265.1</td><td>265.1</td><td>265.1</td><td>265.1</td></tr><tr><td>Total long-term liabilities</td><td>265.1</td><td>265.1</td><td>265.1</td><td>265.1</td></tr><tr><td>Total liabilities</td><td>49,875.6</td><td>56,712.1</td><td>63,735.6</td><td>68,216.3</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>244,637.8</td><td>263,434.8</td><td>284,814.9</td><td>309,544.2</td></tr><tr><td>Minority interest</td><td>9,321.4</td><td>12,491.1</td><td>15,851.0</td><td>19,412.4</td></tr><tr><td>Total liabilities &amp; equity</td><td>303,834.8</td><td>332,638.1</td><td>364,401.4</td><td>397,172.9</td></tr><tr><td>Net debt, adjusted</td><td>(150,786.8)</td><td>(160,545.0)</td><td>(180,288.6)</td><td>(199,915.6)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>82,320.1</td><td>84,895.1</td><td>92,956.7</td><td>98,917.4</td></tr><tr><td>D&amp;A add-back</td><td>2,203.6</td><td>2,364.4</td><td>2,520.0</td><td>2,667.9</td></tr><tr><td>Minority interest add-back</td><td>2,990.3</td><td>3,169.7</td><td>3,359.9</td><td>3,561.4</td></tr><tr><td>Net (inc)/dec working capital</td><td>(24,874.4)</td><td>(5,894.4)</td><td>(2,073.6)</td><td>(2,185.4)</td></tr><tr><td>Other operating cash flow</td><td>(1,117.3)</td><td>(5,370.3)</td><td>(6,174.8)</td><td>(7,100.2)</td></tr><tr><td>Cash flow from operations</td><td>61,522.2</td><td>79,164.4</td><td>90,588.2</td><td>95,861.1</td></tr><tr><td>Capital expenditures</td><td>(3,127.6)</td><td>(4,432.8)</td><td>(4,566.3)</td><td>(4,597.5)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>0.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(28,514.5)</td><td>(60.0)</td><td>(60.0)</td><td>(60.0)</td></tr><tr><td>Cash flow from investing</td><td>(31,641.9)</td><td>(4,492.8)</td><td>(4,626.3)</td><td>(4,657.5)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(64,671.8)</td><td>(65,033.6)</td><td>(66,218.1)</td><td>(71,576.7)</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(907.1)</td><td>120.1</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(65,578.9)</td><td>(64,913.5)</td><td>(66,218.1)</td><td>(71,576.7)</td></tr><tr><td>Total cash flow</td><td>(35,698.6)</td><td>9,758.2</td><td>19,743.7</td><td>19,627.0</td></tr><tr><td>Free cash flow</td><td>58,394.6</td><td>74,731.6</td><td>86,021.8</td><td>91,263.6</td></tr></table>

Source: Company data, GS estimates.

that reaffirmed Moutai's pricing power strength. Additionally, wholesale prices reacted positively over the weekend post the announcement of Feitian's price hikes, and have now reached Rmb1,720/Rmb1,680 per bottle for original case/unpacked Feitian, vs. Rmb1,650/1,630 on Friday, up c. Rmb70/Rmb50 per bottle. We view the timing of these price hikes as unexpected and see the company preparing to support wholesale pricing ahead of the Mid-Autumn Festival, as i-Moutai retail demand has proved to be resilient in 2Q26 to date.

2Q26 Earnings outlook: We currently expect a c.1% topline growth in 2Q26 for Moutai with i-Moutai sales in April-May 2026 reaching c.Rmb11bn or c.30% of 2Q25 sales (GSe based on 7.13mn transacting users in 5M26 assuming c.3 bottles purchased per user on average, see Exhibit 3). For i-Moutai: We also estimate that c. 9,400 tons of Feitian volume sold was already in i-Moutai in 5M26 at a weighted average RSP of Rmb1,512 (Rmb1,499 in 1Q26 and Rmb1,539 in 31 March to 31 May per bottle).

Earnings revisions: We updated our earnings estimates by raising our Moutai spirit ASP by 1% in 2026 and by 3% in 2027-2028E to reflect the price hikes on ex-factory prices and higher volume mix of direct sales, while we largely maintain our volume forecast/series spirits forecast unchanged. We now expect 2026 sales/NP growth at 3.9%/3.1% yoy. We expect 2027 sales/NP growth to accelerate to 8%/9%. Our 2026/27/28E EPS rise by c.1\~3% on our stronger sales outlook. Our 12-month target price increases to Rmb1,667 (prior Rmb1,616), based on unchanged 23.4x 2027E P/E discounted back to mid-2027. We reiterate our Buy rating on Moutai on its differentiated brand position in China spirits and resilient consumer demand driving market share gain through the cycles, a solid dividend yield at 4.2%/4.6% and trading at 19x/17x P/E in 2026E/2027E, respectively.

The authors would like to thank Lily Qi for her contribution to this report.

## See also:

China Spirits: Accelerated destocking and healthier inventories, but awaiting clear/broad

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
