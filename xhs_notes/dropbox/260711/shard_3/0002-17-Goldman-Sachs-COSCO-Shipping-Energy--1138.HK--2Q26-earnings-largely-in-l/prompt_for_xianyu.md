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
GS Factor Profile

# COSCO Shipping Energy (1138.HK)

# 2Q26 earnings largely in-line, with much lower revenue contribution from tankers trapped inside the Gulf

<table><tr><td>1138.HK</td><td>12m Price Target: HK$30.00</td><td>Price: HK$13.08</td><td>Upside: 129.4%</td></tr><tr><td>600026.SS</td><td>12m Price Target: Rmb33.00</td><td>Price: Rmb15.77</td><td>Upside: 109.3%</td></tr></table>

Post market close on July $10^{\text{th}}$ , COSCO Shipping Energy released 1H26 prelim results, with 1H26 reported net profit of c.Rmb4.5bn and recurring net profit of c.Rmb4.4bn. This implies 2Q26 net profit of c.Rmb 2.3bn (+7% QoQ) and 2Q26 recurring net profit of c. Rmb2.4bn (+15% QoQ) (see Exhibit 1), which largely in-line with our expectation and modestly ahead of the range mentioned in investors' conversations with us. On the other hand, the QoQ growth of COSCO Shipping Energy's 2Q26 net profit is lower than that (50% QoQ) of another Chinese listed tanker peer China Merchants Energy Shipping Co Ltd (CMES, 601872.SS, Not Covered). We attribute COSCO's underperformance to 7 tankers (incl. 3 VLCCs, 3 LR2s and 1 Panamax) of COSCO's fleet trapped inside the Persian Gulf since Strait of Hormuz closed (from Feb $28^{\text{th}}$ , 2026), which were not able to charge demurrage fees (see Mar-26 report) to compensate the idleness from the customers and thus could only contribute a much lower revenue during 2Q26, while CMES had no tankers trapped in the Gulf.

Going forward, given all COSCO's tankers trapped in the Gulf have sailed out after Strait of Hormuz temporarily reopened in June, we expect COSCO to catch up with peers from 3Q26. Beyond earnings, we believe the market focus would be still on the freight rate, which we forecast to be US\$150k/day for the full-year 2026 average in our base case (vs. c90k implied from current share price), and would be driven by a formal reopening of Hormuz and restocking demand afterwards. We maintain our price target unchanged of HK\$30/Rmb33 per share for H/A-share.

For crude tankers, based on the VLCC TCE of US Gulf-China and West Africa-China, we estimate the average industry VLCC TCE during 2Q26 was at c.US\$125k/day (+31% QoQ) if considering 1-month lag for revenue recognition vs. industry quotes, which is largely in-line with peer's mgmt comment (see Jul-26 report). For

## BUY

Herbert Lu  
+852-2978-0726 | herbert.lu@gs.com  
GS (Asia) L.L.C.

Simon Cheung, CFA
+852-2978-6102 | simon.cheung@gs.com
GS (Asia) L.L.C.

Wing Huang  
+852-2978-0415 | ying.huang@gs.com  
GS (Asia) L.L.C.

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn)</td><td>23,805.0</td><td>38,856.4</td><td>36,861.7</td><td>34,825.8</td></tr><tr><td>EBITDA (Rmb mn)</td><td>8,768.8</td><td>21,506.2</td><td>19,007.8</td><td>16,500.1</td></tr><tr><td>EPS (Rmb)</td><td>0.79</td><td>2.52</td><td>2.19</td><td>1.80</td></tr><tr><td>P/E (X)</td><td>8.9</td><td>4.5</td><td>5.2</td><td>6.3</td></tr><tr><td>P/B (X)</td><td>0.8</td><td>1.0</td><td>0.9</td><td>0.9</td></tr><tr><td>Dividend yield (%)</td><td>5.4</td><td>11.3</td><td>9.7</td><td>7.9</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>2.1</td><td>0.5</td><td>0.6</td><td>0.7</td></tr><tr><td>CROCI (%)</td><td>9.0</td><td>16.7</td><td>13.6</td><td>11.1</td></tr><tr><td>FCF yield (%)</td><td>3.7</td><td>14.1</td><td>8.5</td><td>6.4</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.43</td><td>0.43</td><td>0.43</td><td>1.22</td></tr></table>

![](images/9b293ebe60853b7760b65ebdacde857986f820a0a68b787dd95ad32aeffbf8b3.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## COSCO Shipping Energy (1138.HK) Rating since Sep 24, 2023

Growth & Margins (%)  
Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>8.9</td><td>4.5</td><td>5.2</td><td>6.3</td></tr><tr><td>P/B (X)</td><td>0.8</td><td>1.0</td><td>0.9</td><td>0.9</td></tr><tr><td>FCF yield (%)</td><td>3.7</td><td>14.1</td><td>8.5</td><td>6.4</td></tr><tr><td>EV/EBITDAR (X)</td><td>6.4</td><td>3.6</td><td>4.1</td><td>4.8</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>6.4</td><td>3.5</td><td>4.0</td><td>4.7</td></tr><tr><td>CROCI (%)</td><td>9.0</td><td>16.7</td><td>13.6</td><td>11.1</td></tr><tr><td>ROE (%)</td><td>9.8</td><td>26.7</td><td>19.7</td><td>15.1</td></tr><tr><td>Net debt/equity (%)</td><td>38.2</td><td>17.5</td><td>16.6</td><td>16.6</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>37.0</td><td>16.4</td><td>15.5</td><td>15.5</td></tr><tr><td>Interest cover (X)</td><td>3.6</td><td>13.3</td><td>12.8</td><td>12.0</td></tr><tr><td>Days inventory outst, sales</td><td>17.7</td><td>9.6</td><td>10.8</td><td>12.1</td></tr><tr><td>Receivable days</td><td>9.7</td><td>8.1</td><td>10.3</td><td>10.3</td></tr><tr><td>Days payable outstanding</td><td>41.9</td><td>41.2</td><td>41.8</td><td>41.7</td></tr><tr><td>DuPont ROE (%)</td><td>8.1</td><td>22.5</td><td>17.7</td><td>13.6</td></tr><tr><td>Turnover (X)</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.3</td></tr><tr><td>Leverage (X)</td><td>1.9</td><td>1.7</td><td>1.5</td><td>1.5</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>102,730.0</td><td>110,886.0</td><td>120,836.3</td><td>130,351.4</td></tr><tr><td>Average capital employed (Rmb)</td><td>67,323.3</td><td>70,193.9</td><td>75,329.4</td><td>80,798.4</td></tr><tr><td>BVPS (Rmb)</td><td>9.08</td><td>11.38</td><td>12.39</td><td>13.20</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>2.9</td><td>63.2</td><td>(5.1)</td><td>(5.5)</td></tr><tr><td>EBITDA growth</td><td>2.3</td><td>145.3</td><td>(11.6)</td><td>(13.2)</td></tr><tr><td>EPS growth</td><td>(1.3)</td><td>218.6</td><td>(13.1)</td><td>(17.9)</td></tr><tr><td>DPS growth</td><td>(11.6)</td><td>236.4</td><td>(14.4)</td><td>(17.9)</td></tr><tr><td>EBIT margin</td><td>20.4</td><td>45.7</td><td>40.7</td><td>34.7</td></tr><tr><td>EBITDA margin</td><td>36.8</td><td>55.3</td><td>51.6</td><td>47.4</td></tr><tr><td>Net income margin</td><td>17.0</td><td>36.0</td><td>32.4</td><td>28.2</td></tr></table>

Price Performance  
![](images/3c9c433093adbb5ea3d861476b68e09fab243a0a86a390001815a66cd1b07fe4.jpg)  
Source: FactSet. Price as of 10 Jul 2026 close.

Income Statement (Rmb mn)

<table><tr><td colspan="5">Income Statement (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>23,805.0</td><td>38,856.4</td><td>36,861.7</td><td>34,825.8</td></tr><tr><td>Cost of goods sold</td><td>(17,650.3)</td><td>(19,145.7)</td><td>(20,183.2)</td><td>(21,333.1)</td></tr><tr><td>SG&amp;A</td><td>(1,299.8)</td><td>(1,949.9)</td><td>(1,664.9)</td><td>(1,398.1)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>8,768.8</td><td>21,506.2</td><td>19,007.8</td><td>16,500.1</td></tr><tr><td>Depreciation &amp; amortization</td><td>(3,913.9)</td><td>(3,745.3)</td><td>(3,994.3)</td><td>(4,405.5)</td></tr><tr><td>EBIT</td><td>4,854.9</td><td>17,760.8</td><td>15,013.6</td><td>12,094.6</td></tr><tr><td>Net interest inc./(exp.)</td><td>(1,173.4)</td><td>(1,085.1)</td><td>(786.3)</td><td>(769.8)</td></tr><tr><td>Income/(loss) from associates</td><td>1,262.3</td><td>1,382.4</td><td>1,436.8</td><td>1,504.7</td></tr><tr><td>Pre-tax profit</td><td>5,356.7</td><td>18,506.4</td><td>15,842.1</td><td>13,007.7</td></tr><tr><td>Provision for taxes</td><td>(933.5)</td><td>(3,904.3)</td><td>(3,284.4)</td><td>(2,622.7)</td></tr><tr><td>Minority interest</td><td>(385.8)</td><td>(629.8)</td><td>(597.4)</td><td>(564.4)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>4,037.3</td><td>13,972.4</td><td>11,960.3</td><td>9,820.6</td></tr><tr><td>Post-tax exceptionals</td><td>(173.3)</td><td>(202.7)</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>3,864.1</td><td>13,769.7</td><td>11,960.3</td><td>9,820.6</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>0.83</td><td>2.56</td><td>2.19</td><td>1.80</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>0.83</td><td>2.56</td><td>2.19</td><td>1.80</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>0.79</td><td>2.52</td><td>2.19</td><td>1.80</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>0.79</td><td>2.52</td><td>2.19</td><td>1.80</td></tr><tr><td>DPS (Rmb)</td><td>0.38</td><td>1.28</td><td>1.09</td><td>0.90</td></tr><tr><td>Div. payout ratio (%)</td><td>46.0</td><td>50.0</td><td>50.0</td><td>50.0</td></tr></table>

<table><tr><td colspan="5">Balance Sheet (Kmb mln)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>14,422.7</td><td>22,393.1</td><td>14,008.6</td><td>13,303.9</td></tr><tr><td>Accounts receivable</td><td>654.6</td><td>1,068.5</td><td>1,013.7</td><td>957.7</td></tr><tr><td>Inventory</td><td>978.1</td><td>1,061.0</td><td>1,118.5</td><td>1,182.2</td></tr><tr><td>Other current assets</td><td>3,247.2</td><td>4,841.6</td><td>4,736.5</td><td>4,636.7</td></tr><tr><td>Total current assets</td><td>19,302.6</td><td>29,364.2</td><td>20,877.2</td><td>20,080.6</td></tr><tr><td>Net PP&amp;E</td><td>55,606.2</td><td>57,847.7</td><td>63,734.9</td><td>68,766.0</td></tr><tr><td>Net intangibles</td><td>150.6</td><td>139.0</td><td>127.5</td><td>115.9</td></tr><tr><td>Total investments</td><td>13,309.8</td><td>13,802.5</td><td>14,265.1</td><td>14,757.2</td></tr><tr><td>Other long-term assets</td><td>3,709.5</td><td>3,709.5</td><td>3,709.5</td><td>3,709.5</td></tr><tr><td>Total assets</td><td>92,078.6</td><td>104,862.9</td><td>102,714.2</td><td>107,429.1</td></tr><tr><td>Accounts payable</td><td>2,072.8</td><td>2,248.5</td><td>2,370.3</td><td>2,505.3</td></tr><tr><td>Short-term debt</td><td>10,864.3</td><td>10,864.3</td><td>2,864.3</td><td>2,864.3</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>2,825.6</td><td>3,053.2</td><td>3,211.1</td><td>3,386.1</td></tr><tr><td>Total current liabilities</td><td>15,762.8</td><td>16,166.0</td><td>8,445.7</td><td>8,755.8</td></tr><tr><td>Long-term debt</td><td>21,917.4</td><td>21,746.0</td><td>21,677.3</td><td>21,618.4</td></tr><tr><td>Long-term lease liabilities</td><td>625.6</td><td>652.8</td><td>721.4</td><td>780.3</td></tr><tr><td>Other long-term liabilities</td><td>4,129.7</td><td>4,129.7</td><td>4,129.7</td><td>4,129.7</td></tr><tr><td>Total long-term liabilities</td><td>26,672.6</td><td>26,528.4</td><td>26,528.4</td><td>26,528.4</td></tr><tr><td>Total liabilities</td><td>42,435.4</td><td>42,694.4</td><td>34,974.2</td><td>35,284.2</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>46,405.2</td><td>58,300.8</td><td>63,274.8</td><td>67,115.3</td></tr><tr><td>Minority interest</td><td>3,238.0</td><td>3,867.8</td><td>4,465.2</td><td>5,029.6</td></tr><tr><td>Total liabilities &amp; equity</td><td>92,078.6</td><td>104,862.9</td><td>102,714.2</td><td>107,429.1</td></tr><tr><td>Net debt, adjusted</td><td>18,359.0</td><td>10,217.1</td><td>10,533.0</td><td>11,178.8</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>4,037.3</td><td>13,972.4</td><td>11,960.3</td><td>9,820.6</td></tr><tr><td>D&amp;A add-back</td><td>3,913.9</td><td>3,745.3</td><td>3,994.3</td><td>4,405.5</td></tr><tr><td>Minority interest add-back</td><td>385.8</td><td>629.8</td><td>597.4</td><td>564.4</td></tr><tr><td>Net (inc)/dec working capital</td><td>(1,134.2)</td><td>(1,688.0)</td><td>382.2</td><td>402.0</td></tr><tr><td>Other operating cash flow</td><td>(174.3)</td><td>(1,382.4)</td><td>(1,436.8)</td><td>(1,504.7)</td></tr><tr><td>Cash flow from operations</td><td>7,028.5</td><td>15,277.1</td><td>15,497.4</td><td>13,687.8</td></tr><tr><td>Capital expenditures</td><td>(5,635.1)</td><td>(5,975.3)</td><td>(9,870.0)</td><td>(9,425.0)</td></tr><tr><td>Acquisitions</td><td>(123.3)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>2,580.4</td><td>889.6</td><td>974.3</td><td>1,012.7</td></tr><tr><td>Cash flow from investing</td><td>(3,178.1)</td><td>(5,085.7)</td><td>(8,895.7)</td><td>(8,412.3)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(2,051.4)</td><td>(2,076.8)</td><td>(6,986.2)</td><td>(5,980.1)</td></tr><tr><td>Inc/(dec) in debt</td><td>(87.8)</td><td>(144.2)</td><td>(8,000.0)</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>7,049.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>4,909.7</td><td>(2,221.0)</td><td>(14,986.2)</td><td>(5,980.1)</td></tr><tr><td>Total cash flow</td><td>8,760.1</td><td>7,970.5</td><td>(8,384.5)</td><td>(704.7)</td></tr><tr><td>Free cash flow</td><td>1,393.3</td><td>9,301.8</td><td>5,627.4</td><td>4,262.8</td></tr></table>

Source: Company data, GS estimates.

product tankers, we estimate industry BCTI TCE was at c.US\$57k/day (+113% QoQ) during 2Q26. We believe COSCO Energy's VLCCs outside the Gulf reached the industry-level TCE in 2Q26, while product tankers underperformed the industry given China suspended the product oil export from Mar 11 $^{th}$ , 2026, and COSCO has a higher exposure to China routes.

Exhibit 1: COSCO Shipping Energy quarterly results

<table><tr><td>mn RMB</td><td>1H26 Prelim</td><td>1Q26 Reported</td><td>2Q26 Implied</td><td>QoQ mn RMB</td><td>%</td></tr><tr><td>Net profit</td><td>4,500</td><td>2,173</td><td>2,327</td><td>153</td><td>7%</td></tr><tr><td>Adjusted net profit</td><td>4,400</td><td>2,050</td><td>2,350</td><td>301</td><td>15%</td></tr><tr><td>- One off</td><td>100</td><td>124</td><td>-24</td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 2: COSCO Shipping Energy's tankers trapped inside the Persian Gulf

<table><tr><td>Vessels trapped inside the Gulf</td><td>Date of Hormuz closure</td><td>Date of departing from the Gulf</td><td>Days trapped inside the Gulf</td></tr><tr><td>Cospearl Lake 远珍湖</td><td>2/28/2026</td><td>4/11/2026</td><td>42</td></tr><tr><td>Yuan Hua Hu 远花湖</td><td>2/28/2026</td><td>5/13/2026</td><td>74</td></tr><tr><td>Yuan Gui Yang 远贵洋</td><td>2/28/2026</td><td>5/20/2026</td><td>81</td></tr><tr><td>Tong Lin Wan 桐林湾</td><td>2/28/2026</td><td>4/6/2026</td><td>37</td></tr><tr><td>Nan Lin Wan 楠林湾</td><td>2/28/2026</td><td>4/8/2026</td><td>39</td></tr><tr><td>Song Lin Wan 松林湾</td><td>2/28/2026</td><td>4/22/2026</td><td>53</td></tr><tr><td>Hua Lin Wan 桦林湾</td><td>2/28/2026</td><td>5/27/2026</td><td>88</td></tr><tr><td>Total</td><td></td><td></td><td>414</td></tr></table>

Source: Data compiled by GS Global Investment Research

Exhibit 3: COSCO Energy's average crude oil TCE (GSe, incl. both spot and LT contract) vs. China avg. VLCC TCE (excl. TD3C)  
![](images/1d7a83009e3b7041cd0684bbe4617317aa605260a45b01ab8b6ccc38be7fb679.jpg)  
Note: COSCO Energy crude tanker TCE is the avg spot rate assuming total capacity of its crude tanker fleet (incl. self-owned and charted-in) are in spot market

Exhibit 4: COSCO Energy's product oil TCE (GSe) vs. BCTI TCE  
![](images/efb3071204f21ace382f78555a3f6738b

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
