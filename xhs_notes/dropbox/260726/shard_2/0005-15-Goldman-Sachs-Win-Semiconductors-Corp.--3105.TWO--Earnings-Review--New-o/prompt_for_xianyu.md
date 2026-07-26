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
# Win Semiconductors Corp. (3105.TWO)

# Earnings Review: New optical product to ramp up in 2H26, higher margin but limited contribution; reiterate Sell

3105.TWO 12m Price Target: NT\$142.00 Price: NT\$341.50 Downside: 58.4%

Win Semi's 2Q26 core business (operating income) was 56/5% higher than GSe/BBG consensus, mainly due to a more favorable product mix with higher contribution from high margin infrastructure business, which led to a 1.9ppt QoQ increase in 2Q26 GPM, and came in 0.4ppt above GSe but is 1.0ppt below BBG consensus. Win Semi's OPEX further declined to NT\$743mn (vs. NT\$778mn in 1Q26). NI was 114/52% higher than GSe/BBG consensus due to the NT\$447mn recognized in non-operating income (account for 38% of total pretax income).

For 3Q26, the company expects revenue to increase by low teens QoQ, and expects optical business to deliver the strongest growth driven by the ramp up of new PD (photodiodes) products at the end of 2Q26, infrastructure should also see strong growth, while cellular and WiFi business might see flattish to slight QoQ increase. On GM, the company guides the 3Q26 level to be around low-thirties %, which is better than our prior expectation but is in line with BBG consensus of 31.3%. Management indicated 2Q26 UTR to be higher at 65% (was 60% in 1Q26), with no guidance for 3Q26, and we expect UTR to further increase to \~70%.

Win Semi continued to highlight the company's progress with its AI-related business, expecting shipments of new PD (photodiodes) products for a single client to ramp up in 2H26. For new LD (laser diodes) products, the company is currently engaged with multiple clients on several new solutions (including CW laser and EML solutions), but expects to see more contribution in 2027/28. The company mentioned that CAPEX this year will mainly focus on expanding InP and GaN capacity for the datacom optical and infrastructure business. Overall, management now expect that the AI-related business might reach double-digits of total revenue in 2027 and potentially reach a similar scale as the cellular and infrastructure business in the long term (each at $30 - 35\%$ in 2Q26).

## SELL

Chao Wang
+886(2)2730-4195 | kuan-chao.wang@gs.com
GS (Asia) L.L.C., Taipei Branch

Allen Chang
+852-2978-2930 | allen.k.chang@gs.com
GS (Asia) L.L.C.

Al Wang
+886(2)2730-4081 | al.wang@gs.com
GS (Asia) L.L.C., Taipei Branch

## Key Data

Market cap: NT\$137.7bn / \$4.3bn
Enterprise value: NT\$141.8bn / \$4.4bn
3m ADTV: NT\$12.5bn / \$396.1mn
Taiwan
Taiwan Electronic Components
M&A Rank: 3
Leases incl. in net debt & EV?: No

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (NT$ mn) New</td><td>16,638.5</td><td>21,320.0</td><td>24,016.0</td><td>25,863.5</td></tr><tr><td>Revenue (NT$ mn) Old</td><td>16,638.5</td><td>20,119.5</td><td>22,342.2</td><td>25,147.4</td></tr><tr><td>EBITDA (NT$ mn)</td><td>4,708.4</td><td>6,085.5</td><td>6,569.2</td><td>7,276.9</td></tr><tr><td>EPS (NT$) New</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (NT$) Old</td><td>4.00</td><td>5.13</td><td>6.09</td><td>7.31</td></tr><tr><td>P/E (X)</td><td>25.9</td><td>45.5</td><td>53.7</td><td>43.5</td></tr><tr><td>P/B (X)</td><td>1.1</td><td>3.4</td><td>3.3</td><td>3.2</td></tr><tr><td>Dividend yield (%)</td><td>1.9</td><td>1.4</td><td>1.2</td><td>1.5</td></tr><tr><td>CROCI (%)</td><td>8.2</td><td>9.9</td><td>9.7</td><td>10.1</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (NT$)</td><td>2.30</td><td>2.73</td><td>1.22</td><td>1.06</td></tr></table>

GS Factor Profile

![](images/9890ed73e96f9676fc11358f0471472dbe1dfdc4ad5174bc83cec7d2e485a192.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Win Semiconductors Corp. (3105.TWO) Rating since Dec 2, 2024

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>25.9</td><td>45.5</td><td>53.7</td><td>43.5</td></tr><tr><td>P/B (X)</td><td>1.1</td><td>3.4</td><td>3.3</td><td>3.2</td></tr><tr><td>FCF yield (%)</td><td>7.4</td><td>1.5</td><td>1.7</td><td>2.3</td></tr><tr><td>EV/EBITDAR (X)</td><td>10.6</td><td>24.5</td><td>22.5</td><td>20.1</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>10.6</td><td>24.5</td><td>22.5</td><td>20.1</td></tr><tr><td>CROCI (%)</td><td>8.2</td><td>9.9</td><td>9.7</td><td>10.1</td></tr><tr><td>ROE (%)</td><td>4.3</td><td>7.6</td><td>6.2</td><td>7.5</td></tr><tr><td>Net debt/equity (%)</td><td>13.3</td><td>15.6</td><td>20.6</td><td>23.2</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>13.3</td><td>15.6</td><td>20.6</td><td>23.2</td></tr><tr><td>Interest cover (X)</td><td>1.0</td><td>4.7</td><td>5.1</td><td>5.6</td></tr><tr><td>Days inventory outst, sales</td><td>109.4</td><td>92.4</td><td>93.4</td><td>94.2</td></tr><tr><td>Receivable days</td><td>32.9</td><td>32.7</td><td>34.0</td><td>34.7</td></tr><tr><td>Days payable outstanding</td><td>39.9</td><td>42.5</td><td>42.7</td><td>43.7</td></tr><tr><td>DuPont ROE (%)</td><td>4.0</td><td>7.9</td><td>6.9</td><td>8.9</td></tr><tr><td>Turnover (X)</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td>Leverage (X)</td><td>1.4</td><td>1.5</td><td>1.5</td><td>1.6</td></tr><tr><td>Gross cash invested (ex cash) (NT$)</td><td>61,343.0</td><td>63,693.2</td><td>67,123.2</td><td>70,164.4</td></tr><tr><td>Average capital employed (NT$)</td><td>48,929.8</td><td>47,177.2</td><td>46,772.6</td><td>46,370.8</td></tr><tr><td>BVPS (NT$)</td><td>98.00</td><td>100.63</td><td>102.85</td><td>105.60</td></tr></table>

Balance Sheet (NT\$ mn)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(4.7)</td><td>28.1</td><td>12.6</td><td>7.7</td></tr><tr><td>EBITDA growth</td><td>(13.8)</td><td>29.2</td><td>7.9</td><td>10.8</td></tr><tr><td>EPS growth</td><td>120.5</td><td>88.0</td><td>(15.4)</td><td>23.7</td></tr><tr><td>DPS growth</td><td>NM</td><td>144.1</td><td>(15.4)</td><td>23.7</td></tr><tr><td>EBIT margin</td><td>4.3</td><td>13.7</td><td>13.1</td><td>13.3</td></tr><tr><td>EBITDA margin</td><td>28.3</td><td>28.5</td><td>27.4</td><td>28.1</td></tr><tr><td>Net income margin</td><td>10.2</td><td>14.9</td><td>11.2</td><td>12.9</td></tr></table>

Price Performance  
![](images/92895170fd00a6eff43adf5e86df2f6885970facf2dd79b3bba9867a878c0f6d.jpg)  
Source: FactSet. Price as of 24 Jul 2026 close.

Income Statement (NT\$ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>16,638.5</td><td>21,320.0</td><td>24,016.0</td><td>25,863.5</td></tr><tr><td>Cost of goods sold</td><td>(12,612.4)</td><td>(15,172.2)</td><td>(16,882.8)</td><td>(17,933.7)</td></tr><tr><td>SG&amp;A</td><td>(1,711.1)</td><td>(1,807.1)</td><td>(2,098.7)</td><td>(2,172.3)</td></tr><tr><td>R&amp;D</td><td>(1,600.3)</td><td>(1,416.7)</td><td>(1,893.1)</td><td>(2,327.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>4,708.4</td><td>6,085.5</td><td>6,569.2</td><td>7,276.9</td></tr><tr><td>Depreciation &amp; amortization</td><td>(3,993.7)</td><td>(3,161.4)</td><td>(3,427.8)</td><td>(3,847.1)</td></tr><tr><td>EBIT</td><td>714.7</td><td>2,924.1</td><td>3,141.4</td><td>3,429.8</td></tr><tr><td>Net interest inc./(exp.)</td><td>(546.0)</td><td>(417.3)</td><td>(437.8)</td><td>(485.4)</td></tr><tr><td>Income/(loss) from associates</td><td>0.0</td><td>(149.2)</td><td>(500.0)</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>1,386.9</td><td>3,221.4</td><td>2,641.4</td><td>3,429.8</td></tr><tr><td>Provision for taxes</td><td>(297.1)</td><td>(686.4)</td><td>(566.8)</td><td>(729.6)</td></tr><tr><td>Minority interest</td><td>604.0</td><td>649.2</td><td>619.0</td><td>631.2</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>1,693.8</td><td>3,184.1</td><td>2,693.6</td><td>3,331.4</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>1,693.8</td><td>3,184.1</td><td>2,693.6</td><td>3,331.4</td></tr><tr><td>EPS (basic, pre-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (diluted, pre-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (basic, post-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (diluted, post-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>DPS (NT$)</td><td>2.00</td><td>4.88</td><td>4.13</td><td>5.11</td></tr><tr><td>Div. payout ratio (%)</td><td>50.1</td><td>65.0</td><td>65.0</td><td>65.0</td></tr></table>

<table><tr><td colspan="5">Balance Sheet (NT$ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>7,066.9</td><td>6,343.4</td><td>4,665.0</td><td>4,005.7</td></tr><tr><td>Accounts receivable</td><td>1,713.9</td><td>2,102.8</td><td>2,368.7</td><td>2,550.9</td></tr><tr><td>Inventory</td><td>4,978.5</td><td>5,819.5</td><td>6,475.6</td><td>6,878.7</td></tr><tr><td>Other current assets</td><td>797.6</td><td>797.6</td><td>797.6</td><td>797.6</td></tr><tr><td>Total current assets</td><td>14,556.9</td><td>15,063.2</td><td>14,306.8</td><td>14,232.8</td></tr><tr><td>Net PP&amp;E</td><td>19,671.9</td><td>19,297.5</td><td>18,856.7</td><td>18,096.7</td></tr><tr><td>Net intangibles</td><td>65.5</td><td>(21.5)</td><td>(108.6)</td><td>(195.6)</td></tr><tr><td>Total investments</td><td>21,091.0</td><td>20,941.8</td><td>20,441.8</td><td>20,441.8</td></tr><tr><td>Other long-term assets</td><td>5,343.4</td><td>5,343.4</td><td>5,343.4</td><td>5,343.4</td></tr><tr><td>Total assets</td><td>60,728.7</td><td>60,624.4</td><td>58,840.2</td><td>57,919.1</td></tr><tr><td>Accounts payable</td><td>1,661.9</td><td>1,870.5</td><td>2,081.4</td><td>2,211.0</td></tr><tr><td>Short-term debt</td><td>330.7</td><td>330.7</td><td>330.7</td><td>330.7</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>3,872.5</td><td>5,094.4</td><td>4,775.5</td><td>5,190.0</td></tr><tr><td>Total current liabilities</td><td>5,865.1</td><td>7,295.6</td><td>7,187.6</td><td>7,731.7</td></tr><tr><td>Long-term debt</td><td>12,328.2</td><td>12,328.2</td><td>12,328.2</td><td>12,328.2</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>544.5</td><td>544.5</td><td>544.5</td><td>544.5</td></tr><tr><td>Total long-term liabilities</td><td>12,872.7</td><td>12,872.7</td><td>12,872.7</td><td>12,872.7</td></tr><tr><td>Total liabilities</td><td>18,737.9</td><td>20,168.3</td><td>20,060.4</td><td>20,604.5</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>41,545.3</td><td>42,659.7</td><td>43,602.5</td><td>44,768.4</td></tr><tr><td>Minority interest</td><td>445.6</td><td>(2,203.6)</td><td>(4,822.6)</td><td>(7,453.8)</td></tr><tr><td>Total liabilities &amp; equity</td><td>60,728.7</td><td>60,624.4</td><td>58,840.2</td><td>57,919.1</td></tr><tr><td>Net debt, adjusted</td><td>5,592.0</td><td>6,315.5</td><td>7,993.9</td><td>8,653.2</td></tr></table>

<table><tr><td colspan="5">Cash Flow (NT$ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>1,693.8</td><td>3,184.1</td><td>2,693.6</td><td>3,331.4</td></tr><tr><td>D&amp;A add-back</td><td>3,993.7</td><td>3,161.4</td><td>3,427.8</td><td>3,847.1</td></tr><tr><td>Minority interest add-back</td><td>(604.0)</td><td>(649.2)</td><td>(619.0)</td><td>(631.2)</td></tr><tr><td>Net (inc)/dec working capital</td><td>207.1</td><td>(1,021.2)</td><td>(711.1)</td><td>(455.8)</td></tr><tr><td>Other operating cash flow</td><td>(337.6)</td><td>149.2</td><td>500.0</td><td>-</td></tr><tr><td>Cash flow from operations</td><td>4,953.0</td><td>4,824.4</td><td>5,291.3</td><td>6,091.5</td></tr><tr><td>Capital expenditures</td><td>(1,691.4)</td><td>(2,700.0)</td><td>(2,900.0)</td><td>(3,000.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>6,292.1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>511.6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>5,112.3</td><td>(2,700.0)</td><td>(2,900.0)</td><td>(3,000.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(423.9)</td><td>(847.9)</td><td>(2,069.7)</td><td>(1,750.8)</td></tr><tr><td>Inc/(dec) in debt</td><td>791.3</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(8,785.0)</td><td>(2,000.0)</td><td>(2,000.0)</td><td>(2,000.0)</td></tr><tr><td>Cash flow from financing</td><td>(8,417.6)</td><td>(2,847.9)</td><td>(4,069.7)</td><td>(3,750.8)</td></tr><tr><td>Total cash flow</td><td>1,647.6</td><td>(723.5)</td><td>(1,678.4)</td><td>(659.3)</td></tr><tr><td>Free cash flow</td><td>3,261.6</td><td>2,124.4</td><td>2,391.3</td><td>3,091.5</td></tr></table>

Source: Company data, GS estimates.

## Downward revision to PA foundry TAM on weaker smartphone shipment We have revised down our 2026/27/28E PA foundry TAM by 1/1/4% to

US\$1.3bn/1.4bn/1.6bn as we factor in our latest smartphone shipment assumptions (-10%/+3% in 2026/27, was -6%/+2% previously, and now expect shipment to see +1% in 2028, see here) as end-demand continues to be impacted by high memory price (see here). Despite the near-term weakness in the smartphone market, we continue to believe the PA foundry house will gain share in the smartphone PA segment. This continues to be driven by the increasing design complexity and production costs of the PA, and we continue to see newer smartphone projects from design houses being allocated to foundries, which will benefit Win Semi in the long term. We expect the market TAM to deliver an 11% CAGR over 2025-30E (was 13% previously), and we expect foundries' cellular PA shipments to increase by 11% in 2026 (vs. 17% previously), while weak smartphone shipments continue to offset content value growth driven by higher 5G penetration in 2026.

Win Semi delivered 2Q26 revenue that in line with the company's guidance, with the cellular business seeing PA inventory pull-in. Management expects this momentum to continue into 3Q26 and guided revenue to be flattish to slight QoQ growth in the cellular business. We now expect Win Semi's PA foundry revenue to grow 28% YoY in 2026, outpacing the overall PA foundry TAM growth of 17% YoY, as the company continue to focus on mid-to-high-end and premium smartphone models, which are relatively more resilient to rising memory costs, although management did acknowledge potential downside risks to end-demand if high-end smartphone prices increase. Moreover, we expect Win Semi's PA foundry market share to decline from 74% in 2020 to 52% in 2026, and further to 40–50% by 2030, but its revenue will continue to expand further due to the growing foundry TAM.

We continue to see a modest recovery in 2026 CAPEX plans among Taiwan PA foundry players. However, we do not see this as an indication of a more constructive demand outlook for the PA foundry industry. Win Semi reiterated its 2026 CAPEX guidance of NT\$2-3bn, with the majority of spending allocated to the optical and infrastructure businesses rather than GaAs capacity expansion. We continue to believe GaAs capacity r

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any

such system.
"""
