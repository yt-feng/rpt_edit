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
# Tesla Inc. (TSLA)

Business and technical progress in key markets, and costs of investments, remain in focus; 2Q wrap

TSLA 12m Price Target: \$360.00 Price: \$374.01 Downside: 3.7%

Key takeaways and implications

Tesla’s 2Q non-GAAP EPS came in below both consensus estimates and our expectation driven by lower margins. This included from lower gross margins in the Automotive and Energy segments, as well as from higher opex. We think the lower 2Q profits were somewhat surprising to investors after the strong 2Q vehicle delivery report from early July. Specifically, 2Q revenue/gross margins/EBIT/non-GAAP EPS of \$28.2 bn/16.8%/\$398 mn/\$0.33 compared to company-compiled consensus at \$27.6 bn/19.5%/\$1,503 mn/\$0.55 and GS at \$28.5 bn/19.8%/\$1,805 mn/\$0.58.

We think commentary on Tesla's progress and outlook in key markets will likely be more of a focus for investors than the 2Q results, including those that are AI-related (e.g. FSD/robotaxis and Optimus), and in more traditional areas including EVs and energy. There were some signs of progress this quarter. For example: 1) Tesla commented on good commercial traction with FSD, especially in North America where management stated that attach rates are \~55% on new vehicle deliveries; 2) Tesla disclosed that it has had no material crash incidents in \~380K miles with its driverless robotaxis; 3) Tesla exited the quarter with its highest vehicle backlog in several years, and we think the Y L product cycle in western markets and FSD can be positive volume/margin drivers. However, Tesla also described Optimus as being a complex technical challenge with a likely quite flat and long initial ramp on the S-curve. In addition, the scale of Tesla's robotaxi fleet is still small relative to some competitors. Finally, on the cost to fund these investments, the company suggested capex could rise for another two to three years, and that its opex is also likely to increase.

We maintain our Neutral rating on the stock. We continue to believe that Tesla can benefit over time from its opportunities in

## NEUTRAL

Mark Delaney, CFA
+1(212)357-0535 | mark.delaney@gs.com
GS & Co. LLC

Will Bryant
+1(212)934-4705 | will.bryant@gs.com
GS & Co. LLC

Aman Gupta
+1(212)357-1549 | aman.s.gupta@gs.com
GS & Co. LLC

## Key Data

<table><tr><td colspan="2">Key Data</td></tr><tr><td></td><td>Market cap: $1.3tr</td></tr><tr><td></td><td>Enterprise value: $1.3tr</td></tr><tr><td></td><td>3m ADTV: $19.4bn</td></tr><tr><td></td><td>United States</td></tr><tr><td></td><td>Americas Autos &amp; Industrial Tech</td></tr><tr><td></td><td>M&amp;A Rank: 3</td></tr></table>

GS Forecast

<table><tr><td colspan="5">CS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue ($ mn) New</td><td>94,827.0</td><td>111,756.6</td><td>128,687.5</td><td>144,939.1</td></tr><tr><td>Revenue ($ mn) Old</td><td>94,827.0</td><td>112,367.6</td><td>127,030.5</td><td>139,995.9</td></tr><tr><td>EBITDA ($ mn)</td><td>14,596.0</td><td>15,928.2</td><td>24,825.2</td><td>31,054.2</td></tr><tr><td>EBIT ($ mn)</td><td>4,355.0</td><td>4,647.4</td><td>9,311.3</td><td>12,343.2</td></tr><tr><td>EPS ($) New</td><td>1.09</td><td>1.00</td><td>2.00</td><td>2.55</td></tr><tr><td>EPS ($) Old</td><td>1.09</td><td>1.65</td><td>2.35</td><td>2.75</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>146.6</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(0.8)</td><td>(1.3)</td><td>(0.6)</td><td>(0.5)</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS ($)</td><td>0.05</td><td>0.31</td><td>0.43</td><td>0.24</td></tr></table>

GS Factor Profile

![](images/5e6b0e763a501a1079805c05bb95d8af5aa10486f9964bc50f1370f475f47f42.jpg)  
Source: Company data, GS estimates. See disclosures for details.

Tesla Inc. (TSLA)
Rating since Jun 25, 2023

Ratios & Valuation

<table><tr><td colspan="5">Ratios &amp; Valuation</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>146.6</td></tr><tr><td>EV/EBITDA (X)</td><td>78.1</td><td>80.9</td><td>56.4</td><td>45.3</td></tr><tr><td>EV/sales (X)</td><td>12.0</td><td>11.5</td><td>10.9</td><td>9.7</td></tr><tr><td>FCF yield (%)</td><td>0.5</td><td>(0.5)</td><td>(0.5)</td><td>0.0</td></tr><tr><td>EV/DACF (X)</td><td>88.9</td><td>88.7</td><td>62.7</td><td>50.2</td></tr><tr><td>CROCI (%)</td><td>15.9</td><td>16.1</td><td>21.0</td><td>20.6</td></tr><tr><td>ROE (%)</td><td>5.0</td><td>4.4</td><td>8.3</td><td>9.3</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(0.8)</td><td>(1.3)</td><td>(0.6)</td><td>(0.5)</td></tr><tr><td>Net debt/equity (%)</td><td>(13.5)</td><td>(23.0)</td><td>(13.3)</td><td>(12.0)</td></tr><tr><td>Interest cover (X)</td><td>12.9</td><td>12.7</td><td>23.3</td><td>30.9</td></tr><tr><td>Inventory days</td><td>57.3</td><td>56.2</td><td>61.0</td><td>60.8</td></tr><tr><td>Receivable days</td><td>17.3</td><td>15.6</td><td>15.2</td><td>15.1</td></tr><tr><td>Days payable outstanding</td><td>60.7</td><td>64.5</td><td>72.2</td><td>74.1</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(2.9)</td><td>17.9</td><td>15.1</td><td>12.6</td></tr><tr><td>EBITDA growth</td><td>(15.6)</td><td>10.4</td><td>74.2</td><td>31.0</td></tr><tr><td>EPS growth</td><td>(46.5)</td><td>(8.0)</td><td>99.4</td><td>27.5</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Gross margin</td><td>18.0</td><td>19.3</td><td>20.9</td><td>21.0</td></tr><tr><td>EBIT margin</td><td>4.6</td><td>4.2</td><td>7.2</td><td>8.5</td></tr></table>

Price Performance  
![](images/53c4c8f8eb38f47c666a574811eae29bc37a63d06a93648d08bc9a5688b215e6.jpg)  
Source: FactSet. Price as of 22 Jul 2026 close.

Income Statement (\$ mn)

<table><tr><td colspan="5">Income Statement ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>94,827.0</td><td>111,756.6</td><td>128,687.5</td><td>144,939.1</td></tr><tr><td>Cost of goods sold</td><td>(77,733.0)</td><td>(90,220.0)</td><td>(101,747.7)</td><td>(114,486.6)</td></tr><tr><td>SG&amp;A</td><td>(6,328.0)</td><td>(7,756.3)</td><td>(7,869.5)</td><td>(8,146.3)</td></tr><tr><td>R&amp;D</td><td>(6,411.0)</td><td>(9,132.9)</td><td>(9,759.0)</td><td>(9,963.0)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>10,503.0</td><td>11,593.2</td><td>20,193.9</td><td>26,456.0</td></tr><tr><td>Depreciation &amp; amortization</td><td>(6,148.0)</td><td>(6,945.8)</td><td>(10,882.6)</td><td>(14,112.8)</td></tr><tr><td>EBIT</td><td>4,355.0</td><td>4,647.4</td><td>9,311.3</td><td>12,343.2</td></tr><tr><td>Net interest inc./(exp.)</td><td>1,342.0</td><td>1,250.0</td><td>1,050.0</td><td>1,005.0</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>5,346.0</td><td>5,281.4</td><td>10,361.3</td><td>13,348.2</td></tr><tr><td>Provision for taxes</td><td>(1,439.0)</td><td>(1,416.1)</td><td>(2,175.9)</td><td>(2,803.1)</td></tr><tr><td>Minority interest</td><td>(61.0)</td><td>(62.0)</td><td>(70.0)</td><td>(88.0)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>3,846.0</td><td>3,803.2</td><td>8,115.4</td><td>10,457.1</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>3,794.0</td><td>3,803.2</td><td>8,115.4</td><td>10,457.1</td></tr><tr><td>EPS (basic, pre-except) ($)</td><td>1.19</td><td>1.09</td><td>2.15</td><td>2.75</td></tr><tr><td>EPS (diluted, pre-except) ($)</td><td>1.09</td><td>1.00</td><td>2.00</td><td>2.55</td></tr><tr><td>EPS (ex-ESO exp., dil.) ($)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>DPS ($)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>3,224.8</td><td>3,500.6</td><td>3,780.7</td><td>3,800.7</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>3,526.3</td><td>3,789.9</td><td>4,055.7</td><td>4,097.6</td></tr></table>

<table><tr><td colspan="5">Balance Sheet ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>17,950.0</td><td>29,265.6</td><td>21,912.6</td><td>22,340.8</td></tr><tr><td>Accounts receivable</td><td>4,576.0</td><td>4,965.3</td><td>5,731.9</td><td>6,299.1</td></tr><tr><td>Inventory</td><td>12,392.0</td><td>15,409.6</td><td>18,579.3</td><td>19,549.1</td></tr><tr><td>Other current assets</td><td>34,438.0</td><td>14,874.0</td><td>14,874.0</td><td>14,874.0</td></tr><tr><td>Total current assets</td><td>69,356.0</td><td>64,514.5</td><td>61,097.7</td><td>63,063.1</td></tr><tr><td>Net PP&amp;E</td><td>46,670.0</td><td>66,924.2</td><td>86,081.6</td><td>102,008.8</td></tr><tr><td>Net intangibles</td><td>381.0</td><td>328.0</td><td>288.0</td><td>248.0</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>22,113.0</td><td>25,777.0</td><td>25,777.0</td><td>25,777.0</td></tr><tr><td>Total assets</td><td>137,806.0</td><td>156,818.8</td><td>172,519.3</td><td>190,371.9</td></tr><tr><td>Accounts payable</td><td>13,371.0</td><td>18,491.5</td><td>21,741.7</td><td>24,762.2</td></tr><tr><td>Short-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Current lease liabilities</td><td>1,640.0</td><td>1,418.0</td><td>1,418.0</td><td>1,418.0</td></tr><tr><td>Other current liabilities</td><td>16,703.0</td><td>18,683.0</td><td>18,683.0</td><td>18,683.0</td></tr><tr><td>Total current liabilities</td><td>31,714.0</td><td>38,592.5</td><td>41,842.7</td><td>44,863.2</td></tr><tr><td>Long-term debt</td><td>6,736.0</td><td>7,924.0</td><td>7,924.0</td><td>7,924.0</td></tr><tr><td>Non-current lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>16,491.0</td><td>17,656.0</td><td>17,656.0</td><td>17,656.0</td></tr><tr><td>Total long-term liabilities</td><td>23,227.0</td><td>25,580.0</td><td>25,580.0</td><td>25,580.0</td></tr><tr><td>Total liabilities</td><td>54,941.0</td><td>64,172.5</td><td>67,422.7</td><td>70,443.2</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>82,137.0</td><td>91,985.2</td><td>104,435.6</td><td>119,267.7</td></tr><tr><td>Minority interest</td><td>728.0</td><td>661.0</td><td>661.0</td><td>661.0</td></tr><tr><td>Total liabilities &amp; equity</td><td>137,806.0</td><td>156,818.8</td><td>172,519.3</td><td>190,371.9</td></tr><tr><td>BVPS ($)</td><td>23.29</td><td>24.27</td><td>25.75</td><td>29.11</td></tr></table>

<table><tr><td colspan="5">Cash Flow ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>3,855.0</td><td>4,606.2</td><td>8,115.4</td><td>10,457.1</td></tr><tr><td>D&amp;A add-back</td><td>6,148.0</td><td>6,945.8</td><td>10,882.6</td><td>14,112.8</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>642.0</td><td>2,409.6</td><td>(686.1)</td><td>1,483.4</td></tr><tr><td>Others</td><td>4,102.0</td><td>4,168.0</td><td>4,335.0</td><td>4,375.0</td></tr><tr><td>Cash flow from operations</td><td>14,747.0</td><td>18,129.6</td><td>22,647.0</td><td>30,428.3</td></tr><tr><td>Capital expenditures</td><td>(8,527.0)</td><td>(25,282.0)</td><td>(30,000.0)</td><td>(30,000.0)</td></tr><tr><td>Acquisitions</td><td>(6,951.0)</td><td>17,338.0</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>0.0</td><td>(7.0)</td><td>0.0</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(15,478.0)</td><td>(7,951.0)</td><td>(30,000.0)</td><td>(30,000.0)</td></tr><tr><td>Dividends paid</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Share issuance/(repurchase)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>40.0</td><td>757.0</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>1,684.0</td><td>417.0</td><td>-</td><td>-</td></tr><tr><td>Cash flow from financing</td><td>1,620.0</td><td>1,137.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Total cash flow</td><td>889.0</td><td>11,315.6</td><td>(7,353.0)</td><td>428.3</td></tr><tr><td>Free cash flow</td><td>6,116.0</td><td>(7,189.4)</td><td>(7,353.0)</td><td>428.3</td></tr><tr><td>Free cash flow per share (basic) ($)</td><td>1.90</td><td>(2.05)</td><td>(1.94)</td><td>0.11</td></tr></table>

Source: Company data, GS estimates.

several large markets, including autonomy, robotics, EVs and energy. However, the trajectory to that better profitability/FCF appears somewhat lower than we had previously expected over the near-to-medium term given headwinds to margins in 2Q and ongoing planned increases in investments in both opex and capex. In addition, while we expect improved growth from these areas to support an attractive long-term EPS CAGR, we also believe the magnitude and pace of that EPS improvement will be somewhat limited by competition (e.g. Tesla is facing several competitors in AVs, EVs, Energy and robotics) and by ongoing R&D/development needs on technology (for example with Optimus). Finally, we see valuation as full.

We lower our EPS estimates for 2026-2028 on lower EBIT margins, and adjust our 12-month price target to \$360 from \$390.

## Results

Tesla reported 2Q26 revenue of \$28,236 mn (up 26% qoq and up 26% yoy) which was 1% below GS at \$28,478 mn, 7% above the Street (FactSet) at \$26,423 mn, and 2% above company-compiled consensus at \$27,584 mn.

The total company gross margin (including SBC) was 16.8%, well below GS at 19.8%, company-compiled consensus at 19.5%, and the Street (FactSet) at 19.3%. The 1Q26 margin was 21.1%, and 2Q25 was 17.2%. By segment:

The automotive gross margin (including SBC, excluding regulatory credits) was 16.3%, well below both GS and the Street at 18.5%. Management cited costs of interest rate incentives (e.g. promotional APRs) and commodity costs as headwinds. The earnings deck cited lower vehicle ASPs (including due to mix) as a yoy headwind. Per the company, the non-GAAP auto gross margin would have been flattish sequentially when backing-out one-time benefits that were realized in 1Q.

The Energy segment gross margin of 20.4% was impacted by vendor cell related warranty costs of \~\$240 mn, and excluding this the margin would have been \~28% (similar to 1Q26 when excluding \~\$200 in one-time benefits from a tariff refund).

■ Services gross margin of 14.1% in 2Q was a record high.

EBIT (including SBC) of \~\$398 mn (1.4% of sales) was well below our forecast of \~\$1,805 mn (6.3% of sales) and company-compiled consensus of \$1,503 mn (5.4% of sales).

Company-reported non-GAAP diluted EPS (excluding SBC and non-cash mark to market adjustments) was \$0.33, \$0.25 below GS at \$0.58, \$0.20 below the Street at \$0.53 and \$0.22 below company-compiled consensus at \$0.55.

Cash, cash equivalents, and investments were down by \$1.2 bn qoq to \$43.5 bn, with FCF of -\$1,092 mn in 2Q.

## Product updates and roadmap

On automotive, the company highlighted its strong deliveries as being supported by record deliveries in several emerging markets like South Korea, Australia, Japan, and Colombia. Additionally, Tesla stated that the Semi truck is on tr

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
