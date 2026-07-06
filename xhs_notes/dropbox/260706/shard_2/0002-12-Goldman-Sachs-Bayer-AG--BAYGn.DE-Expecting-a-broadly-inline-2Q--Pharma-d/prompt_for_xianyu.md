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
# Bayer AG (BAYGn.DE)

# Expecting a broadly inline 2Q; Pharma delivery is key post-litigation

BAYGn.DE

12m Price Target: €62.50

Price: €53.36

Upside: 17.1%

For 2Q26, our forecasts are 2% below Visible Alpha Consensus on Group sales but broadly in line on EBITDA pre-special, driven by our optimism on Pharma margins. We expect FY26 guidance to be reiterated. With respect to the glyphosate litigation, following the favorable SCOTUS ruling for Bayer, the fairness hearing for the Class Settlement has been delayed to August 19th, which gives Bayer more time to potentially encourage any remaining opt-outs to join the settlement. Additionally, we believe the consolidation of the glyphosate business into Ruveon could effectively ringfence future glyphosate liabilities, with both the settlement and any subsequent liabilities residing within Ruveon rather than Bayer. Beyond litigation, we expect investor focus to shift to a potential break-up of the company (as discussed here) and an unwind of the conglomerate discount which is c.€10 in our SOTP. With this note, we roll forward our DCF valuation, reduce the discount we apply to the Pharma business (to 15% from 25%) given the sector-like outlook, but balanced by lower historical R&D productivity, and lower our WACC assumption (to 8.8% from 9.3%) due to reduced litigation risks. We remain Buy rated with our price target up 14% to €62.5 (prev. €55) which implies c.17% upside to the share price at market close on July 3rd.

Bayer is due to report on Aug 4 at 6.30am BST.

For 2Q26, our forecasts are 2% below Visible Alpha Consensus on Group sales but broadly in line on EBITDA pre-special, driven by our optimism on Pharma margins. We are 2% below Visible Alpha Consensus estimates on Group Sales, driven by our cautious view on the generic pressure on Xarelto and Eylea for Pharma and phasing for Corn and Soybean seed and traits in 2Q for Crop. We are less behind on EBITDA-pre special (1% behind) due to our optimism on Pharma margins. On Core EPS, we are 8% behind, potentially due to consensus

## BUY

James Quigley
+44(20)7051-3800 | james.quigley@gs.com
GS International

Rajan Sharma
+44(20)7051-7995 | rajan.sharma@gs.com
GS International

Max Da, Ph.D.
+44(20)7051-8835 | max.da@gs.com
GS International

Key Data

Market cap: €52.4bn / \$60.0bn  
Enterprise value: €86.0bn / \$98.4bn  
3m ADTV: €128.2mn / \$148.4mn  
Germany  
Europe Pharma & Life Sciences  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (€ mn) New</td><td>45,575.0</td><td>45,558.5</td><td>46,878.9</td><td>48,523.7</td></tr><tr><td>Revenue (€ mn) Old</td><td>45,575.0</td><td>45,196.7</td><td>46,555.0</td><td>48,201.9</td></tr><tr><td>EBIT (€ mn)</td><td>8,082.0</td><td>7,394.2</td><td>8,027.0</td><td>8,955.7</td></tr><tr><td>EPS (€) New</td><td>4.91</td><td>4.32</td><td>4.61</td><td>5.43</td></tr><tr><td>EPS (€) Old</td><td>4.91</td><td>4.28</td><td>4.57</td><td>5.38</td></tr><tr><td>P/E (X)</td><td>5.3</td><td>12.3</td><td>11.6</td><td>9.8</td></tr><tr><td>Dividend yield (%)</td><td>0.4</td><td>2.1</td><td>2.2</td><td>2.4</td></tr><tr><td>CROCI (%)</td><td>1.0</td><td>7.8</td><td>7.4</td><td>7.7</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>3.2</td><td>3.5</td><td>3.2</td><td>2.8</td></tr><tr><td></td><td>12/25</td><td>3/26E</td><td>6/26E</td><td>9/26E</td></tr><tr><td>EPS (€)</td><td>0.62</td><td>2.71</td><td>0.77</td><td>0.44</td></tr></table>

GS Factor Profile

![](images/1580fb8c1194ae11353835bb1c6714306b4cc251ece61ce60bfb3a80cfd9ba9d.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Bayer AG (BAYGn.DE)

BUY

Rating since Jun 5, 2025

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>EV/sales (X)</td><td>1.2</td><td>1.9</td><td>1.8</td><td>1.7</td></tr><tr><td>EV/EBITDAR (X)</td><td>5.8</td><td>9.1</td><td>8.3</td><td>7.5</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>5.8</td><td>9.1</td><td>8.3</td><td>7.5</td></tr><tr><td>EV/EBIT (X)</td><td>7.0</td><td>11.6</td><td>10.6</td><td>9.3</td></tr><tr><td>P/E (X)</td><td>5.3</td><td>12.3</td><td>11.6</td><td>9.8</td></tr><tr><td>Dividend yield (%)</td><td>0.4</td><td>2.1</td><td>2.2</td><td>2.4</td></tr><tr><td>EV/GCI (X)</td><td>0.5</td><td>0.7</td><td>0.6</td><td>0.6</td></tr><tr><td>CROCI (%)</td><td>1.0</td><td>7.8</td><td>7.4</td><td>7.7</td></tr><tr><td>ROIC (%)</td><td>9.2</td><td>9.1</td><td>9.6</td><td>10.8</td></tr><tr><td>ROA (%)</td><td>5.9</td><td>5.4</td><td>6.1</td><td>6.8</td></tr><tr><td>Days inventory outst, sales</td><td>103.5</td><td>96.1</td><td>93.9</td><td>96.6</td></tr><tr><td>Asset turnover (X)</td><td>3.5</td><td>3.6</td><td>3.6</td><td>3.6</td></tr><tr><td>Capex/D&amp;A (%)</td><td>89.3</td><td>58.9</td><td>64.3</td><td>66.3</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>118.6</td><td>117.5</td><td>109.5</td><td>97.1</td></tr><tr><td>EBIT interest cover (X)</td><td>3.2</td><td>3.1</td><td>2.9</td><td>3.5</td></tr><tr><td>FCF cover of dividends (X)</td><td>31.6</td><td>(0.6)</td><td>3.5</td><td>3.6</td></tr></table>

Balance Sheet (€ mn)

<table><tr><td colspan="5">Balance Sheet (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>6,671.0</td><td>8,668.5</td><td>8,139.0</td><td>5,823.9</td></tr><tr><td>Accounts receivable</td><td>9,077.0</td><td>9,361.3</td><td>9,632.7</td><td>10,103.6</td></tr><tr><td>Inventory</td><td>12,378.0</td><td>11,610.6</td><td>12,515.1</td><td>13,176.9</td></tr><tr><td>Other current assets</td><td>4,785.0</td><td>4,785.0</td><td>4,785.0</td><td>4,785.0</td></tr><tr><td>Total current assets</td><td>32,911.0</td><td>34,425.4</td><td>35,071.8</td><td>33,889.4</td></tr><tr><td>Net PP&amp;E</td><td>12,649.0</td><td>12,931.1</td><td>13,379.4</td><td>13,773.9</td></tr><tr><td>Net intangibles</td><td>48,683.0</td><td>46,750.9</td><td>44,993.9</td><td>43,401.7</td></tr><tr><td>Total investments</td><td>546.0</td><td>546.0</td><td>546.0</td><td>546.0</td></tr><tr><td>Other long-term assets</td><td>9,752.0</td><td>9,752.0</td><td>9,752.0</td><td>9,752.0</td></tr><tr><td>Total assets</td><td>104,541.0</td><td>104,405.4</td><td>103,743.1</td><td>101,363.0</td></tr><tr><td>Accounts payable</td><td>7,081.0</td><td>5,311.6</td><td>5,450.6</td><td>5,321.4</td></tr><tr><td>Short-term debt</td><td>5,746.0</td><td>4,396.0</td><td>6,728.0</td><td>7,098.0</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>19,758.0</td><td>17,442.0</td><td>17,442.0</td><td>17,442.0</td></tr><tr><td>Total current liabilities</td><td>32,585.0</td><td>27,149.6</td><td>29,620.6</td><td>29,861.4</td></tr><tr><td>Long-term debt</td><td>31,833.0</td><td>37,837.0</td><td>34,055.0</td><td>29,853.0</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>14,060.0</td><td>10,853.7</td><td>10,257.3</td><td>9,592.4</td></tr><tr><td>Total long-term liabilities</td><td>45,893.0</td><td>48,690.7</td><td>44,312.3</td><td>39,445.4</td></tr><tr><td>Total liabilities</td><td>78,478.0</td><td>75,840.3</td><td>73,933.0</td><td>69,306.8</td></tr><tr><td>Preferred shares</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total common equity</td><td>25,947.0</td><td>28,445.1</td><td>29,690.1</td><td>31,936.1</td></tr><tr><td>Minority interest</td><td>116.0</td><td>120.0</td><td>120.0</td><td>120.0</td></tr><tr><td>Total liabilities &amp; equity</td><td>104,541.0</td><td>104,405.4</td><td>103,743.1</td><td>101,363.0</td></tr><tr><td>Capital employed</td><td>63,642.0</td><td>70,798.1</td><td>70,593.1</td><td>69,007.1</td></tr><tr><td>Adj for unfunded pensions &amp; GW</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(2.2)</td><td>(0.0)</td><td>2.9</td><td>3.5</td></tr><tr><td>EBITDA growth</td><td>(4.5)</td><td>(1.8)</td><td>8.0</td><td>8.5</td></tr><tr><td>EBIT growth</td><td>(5.3)</td><td>(8.5)</td><td>8.6</td><td>11.6</td></tr><tr><td>Net inc. growth</td><td>(41.8)</td><td>172.0</td><td>(9.7)</td><td>44.9</td></tr><tr><td>EPS growth</td><td>(3.0)</td><td>(11.9)</td><td>6.6</td><td>17.7</td></tr><tr><td>DPS growth</td><td>0.0</td><td>925.0</td><td>5.0</td><td>8.0</td></tr></table>

Price Performance  
![](images/9cb965a98f9a4f3d5cdf274b0bcbd473b181cc0a25cad05f184d7c8f734ba3bf.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>34.4%</td><td>40.4%</td><td>104.8%</td></tr><tr><td>Rel. to the FTSE World Europe (EUR)</td><td>22.6%</td><td>27.9%</td><td>69.9%</td></tr></table>

Cash Flow (€ mn)

<table><tr><td colspan="5">Cash Flow (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>(1,077.0)</td><td>4,723.9</td><td>5,727.6</td><td>6,896.4</td></tr><tr><td>D&amp;A add-back</td><td>2,785.0</td><td>4,010.0</td><td>3,668.7</td><td>3,557.7</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>6,151.0</td><td>(6,808.6)</td><td>(1,633.3)</td><td>(1,926.8)</td></tr><tr><td>Other operating cash flow</td><td>(1,929.0)</td><td>(230.1)</td><td>(1,383.7)</td><td>(1,638.0)</td></tr><tr><td>Cash flow from operations</td><td>5,930.0</td><td>1,695.2</td><td>6,379.3</td><td>6,889.2</td></tr><tr><td>Capital expenditures</td><td>(2,487.0)</td><td>(2,360.0)</td><td>(2,360.0)</td><td>(2,360.0)</td></tr><tr><td>Acquisitions</td><td>(196.0)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>1,413.0</td><td>(88.7)</td><td>(162.7)</td><td>(168.2)</td></tr><tr><td>Cash flow from investing</td><td>(1,270.0)</td><td>(2,448.7)</td><td>(2,522.7)</td><td>(2,528.2)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(127.0)</td><td>(108.1)</td><td>(1,107.7)</td><td>(1,163.1)</td></tr><tr><td>Inc/(dec) in debt</td><td>(2,045.0)</td><td>4,654.0</td><td>(1,450.0)</td><td>(3,832.0)</td></tr><tr><td>Other financing cash flows</td><td>(1,712.0)</td><td>(1,794.9)</td><td>(1,828.5)</td><td>(1,681.1)</td></tr><tr><td>Cash flow from financing</td><td>(3,884.0)</td><td>2,751.0</td><td>(4,386.1)</td><td>(6,676.2)</td></tr><tr><td>Total cash flow</td><td>480.0</td><td>1,997.5</td><td>(529.5)</td><td>(2,315.1)</td></tr><tr><td>Reinvestment rate (%)</td><td>NM</td><td>27.8</td><td>29.5</td><td>26.8</td></tr></table>

Source: Company data, GS estimates.  
Source: FactSet. Price as of 3 Jul 2026 close.

Income Statement (€ mn)

<table><tr><td colspan="5">Income Statement (€ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>45,575.0</td><td>45,558.5</td><td>46,878.9</td><td>48,523.7</td></tr><tr><td>Total operating expenses</td><td>(39,504.1)</td><td>(33,318.1)</td><td>(34,057.1)</td><td>(34,414.1)</td></tr><tr><td>R&amp;D</td><td>(6,262.9)</td><td>(6,016.5)</td><td>(6,094.3)</td><td>(6,213.2)</td></tr><tr><td>Other operating inc./(exp.)</td><td>8,274.0</td><td>1,170.3</td><td>1,299.4</td><td>1,059.3</td></tr><tr><td>EBITDA</td><td>9,669.0</td><td>9,490.9</td><td>10,247.6</td><td>11,116.4</td></tr><tr><td>Depreciation &amp; amortisation</td><td>(1,587.0)</td><td>(2,096.7)</td><td>(2,220.6)</td><td>(2,160.7)</td></tr><tr><td>EBIT</td><td>8,082.0</td><td>7,394.2</td><td>8,027.0</td><td>8,955.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>(2,008.0)</td><td>(1,896.6)</td><td>(2,394.8)</td><td>(2,184.3)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Profit/(loss) on disposals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total other net</td><td>458.0</td><td>124.0</td><td>403.6</td><td>335.0</td></tr><tr><td>Pre-tax profit</td><td>6,532.0</td><td>5,621.6</td><td>6,035.9</td><td>7,106.4</td></tr><tr><td>Provision for taxes</td><td>(1,688.0)</td><td>(1,371.7)</td><td>(1,509.0)</td><td>(1,776.6)</td></tr><tr><td>Minority interest</td><td>(25.0)</td><td>(4.0)</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>4,819.0</td><td>4,245.9</td><td>4,526.9</td><td>5,329.8</td></tr><tr><td>Post-tax exceptionals</td><td>(8,439.0)</td><td>(1,639.7)</td><td>(2,174.2)</td><td>(1,920.7)</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>(3,620.0)</td><td>2,606.1</td><td>2,352.7</td><td>3,409.1</td></tr><tr><td>EPS (basic, pre-except) (€)</td><td>4.91</td><td>4.32</td><td>4.61</td><td>5.43</td></tr><tr><td>EPS (basic, post-except) (€)</td><td>(3.71)</td><td>2.65</td><td>2.39</td><td>3.47</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>982.4</td><td>982.4</td><td>982.4</td><td>982.4</td></tr><tr><td>Tax rate (%)</td><td>25.8</td><td>24.4</td><td>25.0</td><td>25.0</td></tr><tr><td>Common dividends declared</td><td>108.1</td><td>1,107.7</td><td>1,163.1</td><td>1,256.1</td></tr><tr><td>DPS (€)</td><td>0.11</td><td>1.13</td><td>1.18</td><td>1.28</td></tr></table>

calculation issues as we are broadly in line on Core EBIT and Core Net income.

We expect FY26 guidance to be reiterated. Visible Alpha Consensus estimates are broadly in line with the mid-point of the company's guidance range on Group sales/EBITDA-pre special and slightly above on Core EPS (3% above).

Litigation - what's next? Ruveon could ultimately separate long-tail glyphosate litigation risk from Bayer, in our view. Following the positive US Supreme Court ruling, the fairness hearing for the Class Settlement has been delayed to August 19th (from July 9th), which gives Bayer more time to potentially encourage any remaining opt-outs to join the settlement. In addition, Bayer announced that it has consolidated all glyphosate operations into a new fully owned entity, Ruveon. Operationally, the structure allows Ruveon management to focus on running a strategically distinct business from the other Crop Protection businesses in the Bayer portfolio. However, we see scope for a future spin-out/separation of the business, which is non-core to the Crop Protection business. Such a transaction could effectively ringfence future glyphosate liabilities, with both the settlement and any residual litigation exposure remaining within Ruveon (with Bayer funding the settlement payments before any possible separation).

We increase our 12m price target 14% to €62.5 from €55, driven by reduced litigation risks and a lower WACC. Our estimates for sales are 0-1% higher for each division and the Group across FY26-30, driven by FX. As a result, our estimates on Core EPS are 1% higher across FY26-30. Our price target moves up 14% from €55.0 to €62.5, driven by rolling forward our DCF, reducing the discount we apply to the Pharma business (to 15% from 25%) given the sector-like outlook, but balanced by lower historical R&D productivity, and a lower WACC assumption (to 8.8% from 9.3%) due to reduced litigation risk that impacted our company beta.

## 2Q26 preview table

2Q26 GSe 2% below consensus on Group Sales but broadly in line on EBITDA pre-special, driven by our optimism on Pharma margins. We are 8% behind on Core EPS potentially due to consensus calculation issues as we are broadly in line on Core EBIT and Core Net

[中间内容因长度限制已省略]

luding individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY

## 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
