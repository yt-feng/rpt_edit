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
# Canada Goose Holdings (GOOS.TO)

F1Q27 Earnings Review: Incremental evidence of progress in seasonally small quarter; weak DTC store comps in focus

<table><tr><td>GOOS.TO</td><td>12m Price Target: C$11.50</td><td>Price: C$12.97</td><td>Downside: 11.3%</td></tr><tr><td>GOOS</td><td>12m Price Target: $8.25</td><td>Price: $9.26</td><td>Downside: 10.9%</td></tr></table>

GOOS reported a healthy F1Q27 beat. Revenue growth of +10.3% Y/Y was well above GS/FactSet consensus at -1.9%/+0.6%, and adj. EPS of -C\$0.89 was above GS/consensus of -C\$0.95/-C\$0.99. There were several bright spots in the quarter, including stronger ecommerce momentum, strength in the wholesale orderbook and customer reorders, and solid momentum in Asia (particularly China). However, this is offset by a significant sequential slowing in underlying comp trends as a result of weak store traffic (particularly in EMEA), moderating growth and soft margin guidance in 2Q, and incremental tariff risk (where unmitigated pressure could be up to 200bps to FY27 margins should currently announced duties be implemented).

Management reaffirmed its LSD revenue growth and 11-12% adj. EBIT margin guide for the FY, which continue to embed tailwinds from 2026 cost headwind recapture and pricing actions taken earlier in the year. That said, macro remains uncertain and traffic trends remain in focus as we move into the seasonally important fall/winter selling season.

We step away from the quarter with our view largely unchanged. We are incrementally encouraged by the trajectory of the company's wholesale and ecommerce businesses, and believe initiatives are gaining traction evidenced by improving conversion. That said, the deceleration in DTC comp momentum is somewhat worrying (-3.2% Y/Y vs. 10.0% in F4Q), US traffic trends remain weak, and EMEA demand remains a laggard. Additionally, part of the outperformance this quarter was as a result of a wholesale timing shift. We look for evidence of sustainable and profitable growth while levering SG&A spend (beyond one-time cost recapture) to get more positive from here.

## SELL

Brooke Roach, CFA
+1(212)357-2421 | brooke.roach@gs.com
GS & Co. LLC

Mentesnot Adamu
+1(801)744-0630 | mentesnot.adamu@gs.com
GS & Co. LLC

Carly Chasen
+1(212)902-2327 | carly.chasen@gs.com
GS & Co. LLC

## Key Data

Market cap: C\$1.3bn / \$898.9mn  
Enterprise value: C\$1.2bn / \$848.5mn  
3m ADTV: C\$1.9mn / \$1.4mn  
Canada  
Americas Apparel & Accessories Brands  
M&A Rank: 3

GS Forecast

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Revenue (C$ mn) New</td><td>1,528.2</td><td>1,566.6</td><td>1,641.2</td><td>1,720.3</td></tr><tr><td>Revenue (C$ mn) Old</td><td>1,528.2</td><td>1,553.8</td><td>1,627.8</td><td>1,706.3</td></tr><tr><td>EBITDA (C$ mn)</td><td>279.5</td><td>316.6</td><td>335.4</td><td>355.7</td></tr><tr><td>EBIT (C$ mn)</td><td>148.0</td><td>173.4</td><td>182.5</td><td>192.1</td></tr><tr><td>EPS (C$) New</td><td>0.79</td><td>1.07</td><td>1.13</td><td>1.19</td></tr><tr><td>EPS (C$) Old</td><td>0.79</td><td>1.03</td><td>1.12</td><td>1.18</td></tr><tr><td>P/E (X)</td><td>21.2</td><td>12.1</td><td>11.5</td><td>10.9</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.0</td><td>(0.3)</td><td>(0.7)</td><td>(1.1)</td></tr></table>

<table><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (C$)</td><td>(0.89)</td><td>(0.25)</td><td>1.71</td><td>0.49</td></tr></table>

GS Factor Profile

![](images/1817fc251e7b1bb372da403971e7251f1400e9c0f0dc3da6c6810692093b93c7.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Canada Goose Holdings (GOOS.TO) Rating since Oct 20, 2024

Ratios & Valuation

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>P/E (X)</td><td>21.2</td><td>12.1</td><td>11.5</td><td>10.9</td></tr><tr><td>EV/EBITDA (X)</td><td>7.6</td><td>4.8</td><td>3.9</td><td>3.1</td></tr><tr><td>EV/sales (X)</td><td>1.1</td><td>0.8</td><td>0.6</td><td>0.5</td></tr><tr><td>FCF yield (%)</td><td>4.0</td><td>6.9</td><td>10.3</td><td>10.6</td></tr><tr><td>EV/DACF (X)</td><td>7.0</td><td>5.5</td><td>4.5</td><td>3.9</td></tr><tr><td>CROCI (%)</td><td>22.6</td><td>21.9</td><td>23.2</td><td>23.5</td></tr><tr><td>ROE (%)</td><td>13.0</td><td>15.1</td><td>13.3</td><td>11.9</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.0</td><td>(0.3)</td><td>(0.7)</td><td>(1.1)</td></tr><tr><td>Net debt/equity (%)</td><td>0.4</td><td>(9.4)</td><td>(22.2)</td><td>(31.4)</td></tr><tr><td>Interest cover (X)</td><td>6.7</td><td>8.0</td><td>9.0</td><td>10.0</td></tr><tr><td>Inventory days</td><td>303.8</td><td>300.7</td><td>288.1</td><td>280.8</td></tr><tr><td>Receivable days</td><td>22.8</td><td>25.6</td><td>25.3</td><td>25.3</td></tr><tr><td>Days payable outstanding</td><td>152.1</td><td>168.6</td><td>165.6</td><td>165.5</td></tr></table>

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue growth</td><td>13.3</td><td>2.5</td><td>4.8</td><td>4.8</td></tr><tr><td>EBITDA growth</td><td>(7.5)</td><td>13.3</td><td>5.9</td><td>6.0</td></tr><tr><td>EPS growth</td><td>(29.8)</td><td>36.5</td><td>5.2</td><td>5.9</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Gross margin</td><td>69.7</td><td>70.4</td><td>70.6</td><td>70.8</td></tr><tr><td>EBIT margin</td><td>9.7</td><td>11.1</td><td>11.1</td><td>11.2</td></tr></table>

Price Performance

<table><tr><td colspan="5">Balance Sheet (C$ mn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>408.2</td><td>457.5</td><td>587.6</td><td>722.0</td></tr><tr><td>Accounts receivable</td><td>108.4</td><td>111.1</td><td>116.4</td><td>122.0</td></tr><tr><td>Inventory</td><td>386.3</td><td>378.0</td><td>383.4</td><td>388.9</td></tr><tr><td>Other current assets</td><td>65.5</td><td>54.8</td><td>54.8</td><td>54.8</td></tr><tr><td>Total current assets</td><td>968.4</td><td>1,001.4</td><td>1,142.2</td><td>1,287.7</td></tr><tr><td>Net PP&amp;E</td><td>493.6</td><td>549.9</td><td>596.1</td><td>656.8</td></tr><tr><td>Net intangibles</td><td>199.0</td><td>198.4</td><td>198.4</td><td>198.4</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>92.2</td><td>139.4</td><td>139.4</td><td>139.4</td></tr><tr><td>Total assets</td><td>1,753.2</td><td>1,889.1</td><td>2,076.1</td><td>2,282.3</td></tr><tr><td>Accounts payable</td><td>214.0</td><td>214.6</td><td>223.1</td><td>232.1</td></tr><tr><td>Short-term debt</td><td>4.2</td><td>17.1</td><td>17.1</td><td>17.1</td></tr><tr><td>Current lease liabilities</td><td>92.8</td><td>94.3</td><td>94.3</td><td>94.3</td></tr><tr><td>Other current liabilities</td><td>57.5</td><td>43.3</td><td>43.3</td><td>43.3</td></tr><tr><td>Total current liabilities</td><td>368.5</td><td>369.3</td><td>377.8</td><td>386.8</td></tr><tr><td>Long-term debt</td><td>406.4</td><td>369.2</td><td>369.2</td><td>369.2</td></tr><tr><td>Non-current lease liabilities</td><td>281.8</td><td>324.4</td><td>355.4</td><td>388.8</td></tr><tr><td>Other long-term liabilities</td><td>68.7</td><td>67.3</td><td>67.3</td><td>67.3</td></tr><tr><td>Total long-term liabilities</td><td>756.9</td><td>760.9</td><td>791.9</td><td>825.3</td></tr><tr><td>Total liabilities</td><td>1,125.4</td><td>1,130.2</td><td>1,169.6</td><td>1,212.2</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>627.8</td><td>758.9</td><td>906.4</td><td>1,070.2</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total liabilities &amp; equity</td><td>1,753.2</td><td>1,889.1</td><td>2,076.1</td><td>2,282.3</td></tr><tr><td>BVPS (C$)</td><td>6.47</td><td>7.78</td><td>9.28</td><td>10.96</td></tr></table>

![](images/e094c514b1023840254406b4a67807d4bd76857790c4f2d7f486868a2cb6af07.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(16.2)%</td><td>(21.5)%</td><td>(26.6)%</td></tr><tr><td>Rel. to the Russell 2000 Index</td><td>(19.2)%</td><td>(29.4)%</td><td>(43.7)%</td></tr></table>

Source: FactSet. Price as of 30 Jul 2026 close.

Income Statement (C\$ mn)

<table><tr><td colspan="5">Cash Flow (C$ mn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Net income</td><td>27.8</td><td>98.3</td><td>110.9</td><td>117.9</td></tr><tr><td>D&amp;A add-back</td><td>131.5</td><td>143.2</td><td>153.0</td><td>163.5</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(63.3)</td><td>(28.5)</td><td>(2.1)</td><td>(2.1)</td></tr><tr><td>Others</td><td>98.4</td><td>20.5</td><td>36.7</td><td>45.9</td></tr><tr><td>Cash flow from operations</td><td>194.4</td><td>233.5</td><td>298.4</td><td>325.2</td></tr><tr><td>Capital expenditures</td><td>(42.6)</td><td>(50.1)</td><td>(55.1)</td><td>(60.7)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(7.9)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(50.5)</td><td>(50.1)</td><td>(55.1)</td><td>(60.7)</td></tr><tr><td>Dividends paid</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Share issuance/(repurchase)</td><td>0.0</td><td>0.0</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>10.0</td><td>(39.5)</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>7.1</td><td>1.7</td><td>-</td><td>-</td></tr><tr><td>Cash flow from financing</td><td>(70.1)</td><td>(134.1)</td><td>(113.2)</td><td>(130.1)</td></tr><tr><td>Total cash flow</td><td>73.8</td><td>49.3</td><td>130.1</td><td>134.4</td></tr><tr><td>Free cash flow</td><td>64.6</td><td>87.1</td><td>130.1</td><td>134.4</td></tr><tr><td>Free cash flow per share (basic) (C$)</td><td>0.67</td><td>0.89</td><td>1.33</td><td>1.38</td></tr></table>

<table><tr><td colspan="5">Income Statement (C$ mn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue</td><td>1,528.2</td><td>1,566.6</td><td>1,641.2</td><td>1,720.3</td></tr><tr><td>Cost of goods sold</td><td>(462.7)</td><td>(463.9)</td><td>(482.3)</td><td>(501.9)</td></tr><tr><td>SG&amp;A</td><td>(917.5)</td><td>(929.3)</td><td>(976.4)</td><td>(1,026.2)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>279.5</td><td>316.6</td><td>335.4</td><td>355.7</td></tr><tr><td>Depreciation &amp; amortization</td><td>(131.5)</td><td>(143.2)</td><td>(153.0)</td><td>(163.5)</td></tr><tr><td>EBIT</td><td>148.0</td><td>173.4</td><td>182.5</td><td>192.1</td></tr><tr><td>Net interest inc./(exp.)</td><td>(37.8)</td><td>(41.7)</td><td>(42.1)</td><td>(42.9)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>110.2</td><td>131.7</td><td>140.3</td><td>149.2</td></tr><tr><td>Provision for taxes</td><td>(33.1)</td><td>(26.8)</td><td>(29.5)</td><td>(31.3)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>77.1</td><td>104.8</td><td>110.9</td><td>117.9</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>39.8</td><td>98.3</td><td>110.9</td><td>117.9</td></tr><tr><td>EPS (basic, pre-except) (C$)</td><td>0.79</td><td>1.07</td><td>1.14</td><td>1.21</td></tr><tr><td>EPS (diluted, pre-except) (C$)</td><td>0.79</td><td>1.07</td><td>1.13</td><td>1.19</td></tr><tr><td>EPS (ex-ESO exp., dil.) (C$)</td><td>0.79</td><td>1.07</td><td>1.13</td><td>1.19</td></tr><tr><td>DPS (C$)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>97.1</td><td>97.6</td><td>97.7</td><td>97.7</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>98.1</td><td>97.7</td><td>98.3</td><td>98.7</td></tr></table>

Source: Company data, GS estimates.

## What happened

F1Q results: Consolidated sales grew 10.3% Y/Y (8.6% ex-FX) to \$118.9mn, ahead of GS/consensus at \$105.8mn/\$108.4mn, with the beat driven by wholesale acceleration and strength in China / Asia Pacific. Wholesale revenues increased 66.5% Y/Y (65.4% ex-FX) to \$29.8mn, above GS/consensus of \$17.7mn/\$16.8mn. DTC sales grew 8.6% Y/Y (6.7% ex-FX) to \$84.8mn, above GS/consensus estimates of \$79.8mn/\$79.3mn, with comp sales of -3.2% Y/Y. Other revenue fell -63.6% Y/Y (-64.4% ex-FX) to \$4.3mn vs. GS/consensus at \$8.3mn/\$8.5mn. Gross margin of 62.4% expanded 100bps Y/Y and was reported above GS/consensus of 62.1%/60.6%, largely driven by favorable channel and region mix. Adjusted EBIT margin came in at -87.3%, above GS/consensus at -104.1%/-109.7%. Inventories came in +11.5% Y/Y vs. GS expectations of +10.0% Y/Y.

\- Outlook: Looking ahead, management reiterated guidance. GOOS continues to expect LSD% Y/Y revenue growth vs. GS/consensus at 1.7%/2.4%. The company also reaffirmed its expectation for adj. EBIT margin to range between 11%-12%, which compares to GS/consensus at 10.9%/10.7%. Assumptions underlying management's outlook remain unchanged, though the company did indicate that they expect no material impact from incremental US tariffs announced on 7/20/26 regarding Canada/US trade, which would currently be expected to apply to a range of Canadian goods including certain of their products.

## Estimates, valuation, and key risks

We update our FY27/FY28/FY29 EPS estimates to C\$1.07/C\$1.13/C\$1.19 from C\$1.03/C\$1.12/C\$1.18 prior to reflect the F1Q result, stronger wholesale trends, weaker near-term margin delivery as a result of 2Q marketing investments, and other minor adjustments to our margin forecasts. We modestly lower our 12-month price target to C\$11.50/US\$8.25 from C\$12.00/US\$8.50 prior as we roll forward our Q5-Q8 EV/EBITDA valuation framework. We lower our target multiple from 4.00x to 3.75x to reflect a higher degree of uncertainty given weaker trends in DTC comps and a choppy macro backdrop across several of GOOS's key regions.

Key upside risks include: (1) reacceleration of brand momentum; (2) improved margin profile; and (3) faster-than-anticipated improvement in global / luxury consumer spending.

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

## Disclosure Appendix

## Reg AC

We, Brooke Roach, CFA, Mentesnot Adamu and Carly Chasen, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Brooke Roach, CFA GS & Co. LLC, Mentesnot Adamu GS & Co. LLC, Carly Chasen GS & Co. LLC.

Unle

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
