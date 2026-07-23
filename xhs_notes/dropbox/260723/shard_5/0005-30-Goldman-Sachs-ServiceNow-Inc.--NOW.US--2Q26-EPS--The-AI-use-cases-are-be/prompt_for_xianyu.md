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
ServiceNow is indicated +5% post a mostly straightforward quarter: 2Q subscription revenue growth of +23% was 175bps above guidance. 2Q cRPO was 21.5%, 200bps above guidance (above the 3yr average cRPO beat of 150bps). FY26 subscription guidance is now for 21.0% yoy cc, raised to the high end and up 25bps at the midpoint. Given a number of crosscurrents to demand (e.g. the risk of elongated sales cycles and crowding out, federal, last quarter's ME pushouts), we view the solid beat as a good thing.

We continue to believe the single biggest driver of a stock rerating will be whether ServiceNow can prove its relevance in the enterprise AI stack, and we believe a stabilization in organic revenue and upward revisions to WholeCo revenue will help demonstrate this relevance. In our view, the most interesting product cycle for ServiceNow to execute this is L1 ITSM (for the IT support desk), which became GA in May and resolves 80-85% of service requests without human intervention. ServiceNow also noted new voice capabilities, with one airline customer running all customer service calls on ServiceNow's Voice AI, at 5mn annual calls. As adoption of these autonomous solutions accelerates, the complexity of tasks executed by agents will increase, driving more assists and consumption, and ultimately greater monetization. This quarter, ServiceNow surpassed \$1bn of AI ACV and reiterated confidence in exceeding its \$1.5bn AI ACV target by YE2026, and tracking ahead of its long term objective of 30% AI ACV by 2030. AI NNACV growth was 40%+ qoq; customers with AI in production increased 9x over the last nine months; and deal volume among first time AI buyers grew 45% yoy. We view AI ACV as more valuable than core workflow revenue as AI deployments increase customer entrenchment, drive greater workflow execution, and create a runway for future consumption growth.

Gabriela Borges, CFA
+1(212)902-7839 | gabriela.borges@gs.com
GS & Co. LLC

Maura Hager
+1(212)9028724 | maura.hager@gs.com
GS & Co. LLC

Noah Naparst
+1(917)343-6395 | noah.x.naparst@gs.com
GS & Co. LLC

Key Data

Market cap: \$102.5bn  
Enterprise value: \$103.1bn  
3m ADTV: \$2.9bn  
United States  
Americas Software  
M&A Rank: 3

GS Forecast

<table><tr><td colspan="5">CS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue ($ mn) New</td><td>13,278.0</td><td>16,220.5</td><td>19,340.1</td><td>22,965.4</td></tr><tr><td>Revenue ($ mn) Old</td><td>13,278.0</td><td>16,213.6</td><td>19,376.1</td><td>23,022.1</td></tr><tr><td>EBITDA ($ mn)</td><td>4,887.0</td><td>6,551.2</td><td>7,596.9</td><td>9,018.6</td></tr><tr><td>EBIT ($ mn)</td><td>4,149.0</td><td>5,107.5</td><td>6,298.1</td><td>7,706.1</td></tr><tr><td>EPS ($) New</td><td>3.52</td><td>4.09</td><td>5.17</td><td>6.40</td></tr><tr><td>EPS ($) Old</td><td>3.52</td><td>4.14</td><td>5.17</td><td>6.44</td></tr><tr><td>P/E (X)</td><td>52.5</td><td>23.3</td><td>18.5</td><td>14.9</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(0.5)</td><td>0.1</td><td>(0.7)</td><td>(1.4)</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS ($)</td><td>0.90</td><td>1.03</td><td>1.18</td><td>1.21</td></tr></table>

GS Factor Profile

![](images/72188dfb03db07b2e344618a3d5770aa354bcbfcbc5b4b9e9c7475b9651a846c.jpg)  
Source: Company data, GS estimates. See disclosures for details.

![](images/c27fc8f63e192540f973085947b3346dcffdf167809698d6819ea413d4a49b05.jpg)

## ServiceNow Inc. (NOW)

Rating since Feb 1, 2019

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>52.5</td><td>23.3</td><td>18.5</td><td>14.9</td></tr><tr><td>EV/EBITDA (X)</td><td>38.8</td><td>15.2</td><td>12.4</td><td>9.8</td></tr><tr><td>EV/sales (X)</td><td>14.3</td><td>6.1</td><td>4.9</td><td>3.8</td></tr><tr><td>FCF yield (%)</td><td>2.4</td><td>5.3</td><td>6.9</td><td>8.2</td></tr><tr><td>EV/DACF (X)</td><td>37.6</td><td>17.1</td><td>13.1</td><td>10.3</td></tr><tr><td>CROCI (%)</td><td>48.5</td><td>39.3</td><td>41.6</td><td>50.3</td></tr><tr><td>ROE (%)</td><td>32.5</td><td>31.8</td><td>33.8</td><td>31.8</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(0.5)</td><td>0.1</td><td>(0.7)</td><td>(1.4)</td></tr><tr><td>Net debt/equity (%)</td><td>(17.2)</td><td>4.8</td><td>(28.5)</td><td>(51.1)</td></tr><tr><td>Interest cover (X)</td><td>230.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inventory days</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Receivable days</td><td>66.9</td><td>64.0</td><td>59.6</td><td>53.5</td></tr><tr><td>Days payable outstanding</td><td>19.7</td><td>24.9</td><td>25.8</td><td>25.8</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>20.9</td><td>22.2</td><td>19.2</td><td>18.7</td></tr><tr><td>EBITDA growth</td><td>28.0</td><td>34.1</td><td>16.0</td><td>18.7</td></tr><tr><td>EPS growth</td><td>26.4</td><td>16.2</td><td>26.3</td><td>24.0</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Gross margin</td><td>81.0</td><td>78.8</td><td>78.6</td><td>78.2</td></tr><tr><td>EBIT margin</td><td>31.2</td><td>31.5</td><td>32.6</td><td>33.6</td></tr></table>

Balance Sheet (\$ mn)

<table><tr><td colspan="5">Balance Sheet ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>3,726.0</td><td>4,773.0</td><td>10,647.9</td><td>17,911.3</td></tr><tr><td>Accounts receivable</td><td>2,627.0</td><td>3,064.0</td><td>3,256.2</td><td>3,470.3</td></tr><tr><td>Inventory</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>4,118.0</td><td>4,030.6</td><td>4,375.0</td><td>4,778.3</td></tr><tr><td>Total current assets</td><td>10,471.0</td><td>11,867.6</td><td>18,279.1</td><td>26,159.8</td></tr><tr><td>Net PP&amp;E</td><td>3,095.0</td><td>3,037.1</td><td>3,188.9</td><td>3,369.1</td></tr><tr><td>Net intangibles</td><td>4,699.0</td><td>13,238.4</td><td>12,851.6</td><td>12,622.0</td></tr><tr><td>Total investments</td><td>5,313.0</td><td>4,116.0</td><td>4,116.0</td><td>4,116.0</td></tr><tr><td>Other long-term assets</td><td>2,460.0</td><td>2,574.4</td><td>2,878.8</td><td>3,234.3</td></tr><tr><td>Total assets</td><td>26,038.0</td><td>34,833.6</td><td>41,314.4</td><td>49,501.2</td></tr><tr><td>Accounts payable</td><td>204.0</td><td>264.7</td><td>320.4</td><td>386.9</td></tr><tr><td>Short-term debt</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Current lease liabilities</td><td>112.0</td><td>114.0</td><td>114.0</td><td>114.0</td></tr><tr><td>Other current liabilities</td><td>10,127.0</td><td>13,795.1</td><td>15,609.9</td><td>17,607.2</td></tr><tr><td>Total current liabilities</td><td>10,443.0</td><td>14,173.8</td><td>16,044.3</td><td>18,108.1</td></tr><tr><td>Long-term debt</td><td>1,491.0</td><td>5,435.0</td><td>5,435.0</td><td>5,435.0</td></tr><tr><td>Non-current lease liabilities</td><td>800.0</td><td>822.0</td><td>822.0</td><td>822.0</td></tr><tr><td>Other long-term liabilities</td><td>220.0</td><td>605.0</td><td>605.0</td><td>605.0</td></tr><tr><td>Total long-term liabilities</td><td>2,631.0</td><td>6,957.9</td><td>6,972.1</td><td>6,987.3</td></tr><tr><td>Total liabilities</td><td>13,074.0</td><td>21,131.7</td><td>23,016.3</td><td>25,095.4</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>12,964.0</td><td>13,701.9</td><td>18,298.1</td><td>24,405.7</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total liabilities &amp; equity</td><td>26,038.0</td><td>34,833.6</td><td>41,314.4</td><td>49,501.2</td></tr><tr><td>BVPS ($)</td><td>12.50</td><td>13.26</td><td>17.56</td><td>23.11</td></tr></table>

Price Performance  
![](images/bc3da11177706260a506b92a2606826380dff99064338cdca5e8cfa8b75dd6a9.jpg)

Cash Flow (\$ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>1,748.0</td><td>1,664.1</td><td>3,082.0</td><td>4,581.5</td></tr><tr><td>D&amp;A add-back</td><td>738.0</td><td>1,443.6</td><td>1,298.8</td><td>1,312.5</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>29.0</td><td>(142.0)</td><td>313.6</td><td>242.2</td></tr><tr><td>Others</td><td>2,929.0</td><td>2,984.4</td><td>3,244.3</td><td>3,390.3</td></tr><tr><td>Cash flow from operations</td><td>5,444.0</td><td>5,950.2</td><td>7,938.6</td><td>9,526.5</td></tr><tr><td>Capital expenditures</td><td>(911.0)</td><td>(678.2)</td><td>(1,063.7)</td><td>(1,263.1)</td></tr><tr><td>Acquisitions</td><td>(1,084.0)</td><td>(8,776.0)</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>306.0</td><td>1,926.0</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(1,689.0)</td><td>(7,528.2)</td><td>(1,063.7)</td><td>(1,263.1)</td></tr><tr><td>Dividends paid</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Share issuance/(repurchase)</td><td>(1,840.0)</td><td>(3,225.0)</td><td>(1,000.0)</td><td>(1,000.0)</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(493.0)</td><td>5,850.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(2,333.0)</td><td>2,625.0</td><td>(1,000.0)</td><td>(1,000.0)</td></tr><tr><td>Total cash flow</td><td>1,422.0</td><td>1,047.0</td><td>5,874.9</td><td>7,263.4</td></tr><tr><td>Free cash flow</td><td>4,533.0</td><td>5,272.0</td><td>6,874.9</td><td>8,263.4</td></tr><tr><td>Free cash flow per share (basic) ($)</td><td>4.37</td><td>5.10</td><td>6.60</td><td>7.82</td></tr></table>

Source: FactSet. Price as of 22 Jul 2026 close.

Income Statement (\$ mn)

<table><tr><td colspan="5">Income Statement ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>13,278.0</td><td>16,220.5</td><td>19,340.1</td><td>22,965.4</td></tr><tr><td>Cost of goods sold</td><td>(2,517.0)</td><td>(3,440.5)</td><td>(4,131.8)</td><td>(4,997.5)</td></tr><tr><td>SG&amp;A</td><td>(4,464.0)</td><td>(5,189.6)</td><td>(6,017.7)</td><td>(6,920.9)</td></tr><tr><td>R&amp;D</td><td>(2,148.0)</td><td>(2,482.9)</td><td>(2,892.5)</td><td>(3,340.9)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>4,887.0</td><td>6,551.2</td><td>7,596.9</td><td>9,018.6</td></tr><tr><td>Depreciation &amp; amortization</td><td>(738.0)</td><td>(1,443.6)</td><td>(1,298.8)</td><td>(1,312.5)</td></tr><tr><td>EBIT</td><td>4,149.0</td><td>5,107.5</td><td>6,298.1</td><td>7,706.1</td></tr><tr><td>Net interest inc./(exp.)</td><td>433.0</td><td>294.2</td><td>455.4</td><td>776.6</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>4,586.0</td><td>5,278.7</td><td>6,753.5</td><td>8,482.7</td></tr><tr><td>Provision for taxes</td><td>(917.0)</td><td>(1,039.3)</td><td>(1,350.7)</td><td>(1,696.5)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>3,669.0</td><td>4,239.4</td><td>5,402.8</td><td>6,786.2</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>1,748.0</td><td>1,664.1</td><td>3,082.0</td><td>4,581.5</td></tr><tr><td>EPS (basic, pre-except) ($)</td><td>3.54</td><td>4.10</td><td>5.18</td><td>6.42</td></tr><tr><td>EPS (diluted, pre-except) ($)</td><td>3.52</td><td>4.09</td><td>5.17</td><td>6.40</td></tr><tr><td>EPS (ex-ESO exp., dil.) ($)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>DPS ($)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>1,037.3</td><td>1,033.1</td><td>1,042.3</td><td>1,056.3</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>1,042.1</td><td>1,036.6</td><td>1,045.8</td><td>1,059.8</td></tr></table>

Source: Company data, GS estimates.

## Earnings Recap

Exhibit 1: 2Q26 Actuals vs. Estimates

<table><tr><td rowspan="2">$ millions, unless specified</td><td colspan="5">2Q26A</td></tr><tr><td>Actual</td><td>GSe</td><td>Street</td><td>Actual vs GSe</td><td>Actual vs Street</td></tr><tr><td>Subscription Revenue</td><td>$3,877</td><td>$3,817</td><td>$3,817</td><td>1.6%</td><td>1.6%</td></tr><tr><td>% yoy</td><td>24.5%</td><td>23%</td><td>23%</td><td></td><td></td></tr><tr><td>% yoy CC</td><td>23.0%</td><td>21%</td><td></td><td></td><td></td></tr><tr><td>Total Revenue</td><td>$3,987</td><td>$3,934</td><td>$3,927</td><td>1.4%</td><td>2%</td></tr><tr><td>% yoy</td><td>24.0%</td><td>22%</td><td>22%</td><td></td><td></td></tr><tr><td>% yoy CC</td><td>22.5%</td><td></td><td></td><td></td><td></td></tr><tr><td>Gross Profit</td><td>$3,107</td><td>$3,122</td><td>$3,111</td><td>-0.5%</td><td>-0.1%</td></tr><tr><td>% margin</td><td>78%</td><td>79%</td><td>79%</td><td></td><td></td></tr><tr><td>% yoy</td><td>19%</td><td>20%</td><td>19%</td><td></td><td></td></tr><tr><td>Operating Income</td><td>$1,173</td><td>$1,043</td><td>$1,043</td><td>12.4%</td><td>12.5%</td></tr><tr><td>% Margin</td><td>29%</td><td>27%</td><td>27%</td><td></td><td></td></tr><tr><td>% yoy</td><td>23%</td><td>9%</td><td>9%</td><td></td><td></td></tr><tr><td>Earnings Per Share</td><td>$0.90</td><td>$0.86</td><td>$0.86</td><td>4.6%</td><td>4.8%</td></tr><tr><td>% yoy</td><td>10%</td><td>5%</td><td>5%</td><td></td><td></td></tr><tr><td>cRPO</td><td>$13,200</td><td>$12,995</td><td>$12,997</td><td>1.6%</td><td>1.6%</td></tr><tr><td>% yoy</td><td>21.0%</td><td>19%</td><td>19%</td><td></td><td></td></tr><tr><td>% yoy CC</td><td>21.5%</td><td>20%</td><td></td><td></td><td></td></tr><tr><td>Total deferred revenue</td><td>$8,192</td><td>$8,352</td><td>$8,213</td><td>-1.9%</td><td>-0.3%</td></tr><tr><td>% yoy</td><td>19%</td><td>21%</td><td>19%</td><td></td><td></td></tr><tr><td>Free Cash Flow</td><td>$634</td><td>$656</td><td>$691</td><td>-3.3%</td><td>-8.2%</td></tr><tr><td>% Margin</td><td>16%</td><td>17%</td><td>18%</td><td></td><td></td></tr></table>

Source: FactSet, Company data, GS Global Investment Research

## Valuation and Key Risks

We maintain our Buy rating and raise our 12-month price target to \$152 (from \$145) based on a 27x P/E multiple (unchanged) to ServiceNow's SNTM (Q5-Q8) non-GAAP earnings. Our 2026/2027/2028 subscription revenue estimates go to \$15,770/\$18,829/\$22,388 (from \$15,756/\$18,852/\$22,425) on the back of results.

Key downside risks include: 1) Slowing momentum in new market expansion reducing growth trajectory, 2) Lack of adoption of AI solutions and disintermediation of existing solutions by competitor AI technologies, and 3) Higher expense growth limiting margin expansion.

## Disclosure Appendix

## Reg AC

We, Gabriela Borges, CFA, Maura Hager and Noah Naparst, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Gabriela

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
