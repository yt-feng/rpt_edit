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
12m Price Target: ¥116,000

## 1Q effectively in line; 2Q guidance likely to fulfill investor expectations

## Key takeaways from the results briefing

Kioxia's 1Q non-GAAP operating profits, announced after the July 31 close, came in at ¥1.33 tn, a little below GSe of ¥1.42 tn / Bloomberg consensus of ¥1.37 tn, but broadly within our expectations when considering provisions for special employee bonuses (c.¥50 bn for the year) and the delay of some shipments scheduled for the end of the quarter (on an IFRS basis, the company also recorded expenses totaling ¥56 bn for two items—provision for litigation losses and stock-based compensation expenses). 2Q guidance for non-GAAP operating profits is ¥1.9 tn, close to our estimate of ¥1.97 tn and the Bloomberg consensus of ¥1.95 tn. Considering that expectations for NAND price increases from 2Q onward appear to have declined with the recent correction in the share price, we believe this level of profit guidance is likely to fulfill investor expectations. Along with 2Q results, Kioxia announced capital policies including the launch of a share buyback of up to ¥800 bn/30 mn shares (5.5% of shares outstanding) and a stock split (3-for-1 with a record date of September 30).

(1) 1Q results/2Q outlook: 1Q volume slightly missed (we estimate by 2-3%) due in part to some shipments slipping into 2Q. For 2Q, management guides for a 34% qoq increase in USD-based revenue, and expects the contribution from price increases to be greater than that from volume. At present, prices have been determined for c.50% of 2Q sales volume, while the remainder is under negotiation.

BUY

(2) Supply/demand balance: NAND demand for inference/agentic AI is increasing significantly but is still in the launch phase, and Kioxia expects very strong demand to continue and exceed supply through CY27. Regarding capex, the company said it will continue to

Shuhei Nakamura
+81(3)4587-9932 | shuhei.nakamura@gs.com
GS Japan Co., Ltd.

Kaho Otake
+81(3)4587-7498 | kaho.otake@gs.com
GS Japan Co., Ltd.

Market cap: ¥21.6tr / \$135.4bn  
Enterprise value: ¥20.2tr / \$126.6bn  
3m ADTV: ¥2.7tr / \$16.9bn  
Japan  
Japan Semiconductor, SPE & Precision  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Revenue (¥ bn)</td><td>2,337.6</td><td>10,405.2</td><td>13,874.3</td><td>16,364.1</td></tr><tr><td>Op. profit (¥ bn) New</td><td>870.4</td><td>8,286.5</td><td>11,371.8</td><td>13,463.9</td></tr><tr><td>Op. profit (¥ bn) Old</td><td>870.4</td><td>8,390.4</td><td>11,069.4</td><td>12,984.5</td></tr><tr><td>Op. profit CoE (¥ bn)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EPS (¥) New</td><td>1,024.1</td><td>10,827.8</td><td>14,918.7</td><td>17,669.1</td></tr><tr><td>EPS (¥) Old</td><td>1,024.1</td><td>10,725.0</td><td>14,170.8</td><td>16,628.1</td></tr><tr><td>P/E (X)</td><td>8.0</td><td>3.6</td><td>2.6</td><td>2.2</td></tr><tr><td>P/B (X)</td><td>3.2</td><td>3.5</td><td>1.6</td><td>1.0</td></tr><tr><td>CROCI (%)</td><td>25.5</td><td>103.6</td><td>102.8</td><td>104.8</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (¥)</td><td>1,539.9</td><td>2,499.7</td><td>3,161.4</td><td>3,626.8</td></tr></table>

GS Factor Profile

![](images/f5887b8bdd78c772b804af9836e9352786c14c8f5942e69612e9b931d88a4725.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Kioxia Holdings (285A.T)

Rating since May 31, 2026

Cash Flow (¥ bn)  
Ratios & Valuation

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>P/E (X)</td><td>8.0</td><td>3.6</td><td>2.6</td><td>2.2</td></tr><tr><td>P/B (X)</td><td>3.2</td><td>3.5</td><td>1.6</td><td>1.0</td></tr><tr><td>FCF yield (%)</td><td>13.8</td><td>18.3</td><td>34.1</td><td>42.5</td></tr><tr><td>EV/EBITDAR (X)</td><td>4.4</td><td>2.3</td><td>1.1</td><td>0.4</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>4.3</td><td>2.3</td><td>1.1</td><td>0.4</td></tr><tr><td>CROCI (%)</td><td>25.5</td><td>103.6</td><td>102.8</td><td>104.8</td></tr><tr><td>ROE (%)</td><td>51.9</td><td>157.2</td><td>82.4</td><td>53.1</td></tr><tr><td>Net debt/equity (%)</td><td>55.9</td><td>(23.7)</td><td>(56.7)</td><td>(69.5)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>41.2</td><td>(26.4)</td><td>(57.7)</td><td>(70.0)</td></tr><tr><td>Interest cover (X)</td><td>9.0</td><td>168.4</td><td>563.0</td><td>727.8</td></tr><tr><td>Days inventory outst, sales</td><td>59.8</td><td>17.3</td><td>16.7</td><td>16.7</td></tr><tr><td>Receivable days</td><td>70.2</td><td>63.2</td><td>90.2</td><td>95.3</td></tr><tr><td>Days payable outstanding</td><td>162.3</td><td>151.4</td><td>160.6</td><td>164.0</td></tr><tr><td>DuPont ROE (%)</td><td>39.6</td><td>97.1</td><td>59.5</td><td>42.5</td></tr><tr><td>Turnover (X)</td><td>0.6</td><td>1.3</td><td>0.9</td><td>0.7</td></tr><tr><td>Leverage (X)</td><td>2.6</td><td>1.3</td><td>1.2</td><td>1.1</td></tr><tr><td>Gross cash invested (ex cash) (¥)</td><td>4,552.4</td><td>7,195.8</td><td>8,594.8</td><td>9,741.0</td></tr><tr><td>Average capital employed (¥)</td><td>1,661.8</td><td>3,175.9</td><td>5,013.8</td><td>6,147.8</td></tr><tr><td>BVPS (¥)</td><td>2,562.0</td><td>11,151.8</td><td>25,070.5</td><td>41,539.6</td></tr></table>

Income Statement (¥ bn)

Growth & Margins (%)

<table><tr><td>Growth &amp; Margins (%)</td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue growth</td><td>37.0</td><td>345.1</td><td>33.3</td><td>17.9</td></tr><tr><td>EBITDA growth</td><td>54.9</td><td>629.3</td><td>36.2</td><td>18.4</td></tr><tr><td>EPS growth</td><td>97.0</td><td>957.3</td><td>37.8</td><td>18.4</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>25.0</td><td>20.0</td></tr><tr><td>EBIT margin</td><td>37.2</td><td>79.6</td><td>82.0</td><td>82.3</td></tr><tr><td>EBITDA margin</td><td>50.6</td><td>82.9</td><td>84.7</td><td>85.0</td></tr><tr><td>Net income margin</td><td>23.7</td><td>55.5</td><td>57.3</td><td>57.6</td></tr></table>

Price Performance  
![](images/147954212cabea9f9d88788735a1cc0c4d99e6f0e292a716d08b1986c918e5c9.jpg)  
Source: FactSet. Price as of 31 Jul 2026 close.

<table><tr><td colspan="5">Income Statement (+ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue</td><td>2,337.6</td><td>10,405.2</td><td>13,874.3</td><td>16,364.1</td></tr><tr><td>Cost of goods sold</td><td>(1,235.5)</td><td>(1,716.3)</td><td>(2,078.6)</td><td>(2,403.5)</td></tr><tr><td>SG&amp;A</td><td>(146.6)</td><td>(243.4)</td><td>(286.3)</td><td>(329.9)</td></tr><tr><td>R&amp;D</td><td>(89.3)</td><td>(129.7)</td><td>(149.6)</td><td>(178.8)</td></tr><tr><td>Other operating inc./(exp.)</td><td>4.0</td><td>(29.3)</td><td>12.0</td><td>12.0</td></tr><tr><td>EBITDA</td><td>1,183.2</td><td>8,629.0</td><td>11,751.0</td><td>13,912.5</td></tr><tr><td>Depreciation &amp; amortization</td><td>(312.8)</td><td>(342.5)</td><td>(379.2)</td><td>(448.6)</td></tr><tr><td>EBIT</td><td>870.4</td><td>8,286.5</td><td>11,371.8</td><td>13,463.9</td></tr><tr><td>Net interest inc./(exp.)</td><td>(87.2)</td><td>(42.8)</td><td>(13.3)</td><td>(11.1)</td></tr><tr><td>Income/(loss) from associates</td><td>0.9</td><td>1.2</td><td>1.3</td><td>1.4</td></tr><tr><td>Pre-tax profit</td><td>784.1</td><td>8,244.9</td><td>11,359.8</td><td>13,454.2</td></tr><tr><td>Provision for taxes</td><td>(229.6)</td><td>(2,473.5)</td><td>(3,407.9)</td><td>(4,036.3)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>554.5</td><td>5,771.4</td><td>7,951.9</td><td>9,417.9</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>554.5</td><td>5,771.4</td><td>7,951.9</td><td>9,417.9</td></tr><tr><td>EPS (basic, pre-except) (¥)</td><td>1,024.1</td><td>10,827.8</td><td>14,918.7</td><td>17,669.1</td></tr><tr><td>EPS (diluted, pre-except) (¥)</td><td>1,024.1</td><td>10,827.8</td><td>14,918.7</td><td>17,669.1</td></tr><tr><td>EPS (basic, post-except) (¥)</td><td>1,024.1</td><td>10,827.8</td><td>14,918.7</td><td>17,669.1</td></tr><tr><td>EPS (diluted, post-except) (¥)</td><td>1,024.1</td><td>10,827.8</td><td>14,918.7</td><td>17,669.1</td></tr><tr><td>DPS (¥)</td><td>-</td><td>800.0</td><td>1,000.0</td><td>1,200.0</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>7.4</td><td>6.7</td><td>6.8</td></tr></table>

Balance Sheet (¥ bn)

<table><tr><td colspan="5">Balance Sheet (+ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>470.7</td><td>2,040.4</td><td>8,157.9</td><td>15,918.9</td></tr><tr><td>Accounts receivable</td><td>660.6</td><td>2,940.3</td><td>3,920.6</td><td>4,624.1</td></tr><tr><td>Inventory</td><td>412.6</td><td>575.0</td><td>694.0</td><td>804.3</td></tr><tr><td>Other current assets</td><td>74.0</td><td>74.0</td><td>74.0</td><td>74.0</td></tr><tr><td>Total current assets</td><td>1,617.8</td><td>5,629.6</td><td>12,846.4</td><td>21,421.3</td></tr><tr><td>Net PP&amp;E</td><td>1,055.3</td><td>1,148.6</td><td>1,239.4</td><td>1,280.8</td></tr><tr><td>Net intangibles</td><td>584.9</td><td>584.1</td><td>584.1</td><td>584.1</td></tr><tr><td>Total investments</td><td>227.3</td><td>228.5</td><td>229.8</td><td>231.2</td></tr><tr><td>Other long-term assets</td><td>204.8</td><td>259.1</td><td>485.2</td><td>752.9</td></tr><tr><td>Total assets</td><td>3,690.1</td><td>7,849.8</td><td>15,384.8</td><td>24,270.2</td></tr><tr><td>Accounts payable</td><td>594.9</td><td>829.0</td><td>1,000.7</td><td>1,159.7</td></tr><tr><td>Short-term debt</td><td>175.5</td><td>25.4</td><td>25.4</td><td>25.4</td></tr><tr><td>Short-term lease liabilities</td><td>43.9</td><td>30.1</td><td>26.6</td><td>22.0</td></tr><tr><td>Other current liabilities</td><td>283.7</td><td>283.7</td><td>283.7</td><td>283.7</td></tr><tr><td>Total current liabilities</td><td>1,098.0</td><td>1,168.2</td><td>1,336.3</td><td>1,490.8</td></tr><tr><td>Long-term debt</td><td>872.1</td><td>446.8</td><td>421.4</td><td>396.0</td></tr><tr><td>Long-term lease liabilities</td><td>161.7</td><td>131.6</td><td>105.0</td><td>83.0</td></tr><tr><td>Other long-term liabilities</td><td>159.2</td><td>159.2</td><td>159.2</td><td>159.2</td></tr><tr><td>Total long-term liabilities</td><td>1,193.0</td><td>737.5</td><td>685.5</td><td>638.2</td></tr><tr><td>Total liabilities</td><td>2,291.0</td><td>1,905.7</td><td>2,021.9</td><td>2,128.9</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>1,398.9</td><td>5,943.9</td><td>13,362.8</td><td>22,141.1</td></tr><tr><td>Minority interest</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td></tr><tr><td>Total liabilities &amp; equity</td><td>3,690.1</td><td>7,849.8</td><td>15,384.8</td><td>24,270.2</td></tr><tr><td>Net debt, adjusted</td><td>576.9</td><td>(1,568.3)</td><td>(7,711.1)</td><td>(15,497.5)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (¥ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Net income</td><td>554.5</td><td>5,771.4</td><td>7,951.9</td><td>9,417.9</td></tr><tr><td>D&amp;A add-back</td><td>312.8</td><td>342.5</td><td>379.2</td><td>448.6</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (incl)/dec working capital</td><td>(400.3)</td><td>(2,208.0)</td><td>(927.7)</td><td>(654.8)</td></tr><tr><td>Other operating cash flow</td><td>149.5</td><td>(55.5)</td><td>(227.4)</td><td>(269.1)</td></tr><tr><td>Cash flow from operations</td><td>616.5</td><td>3,850.4</td><td>7,176.0</td><td>8,942.6</td></tr><tr><td>Capital expenditures</td><td>(0.5)</td><td>(0.5)</td><td>(0.5)</td><td>(0.5)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(221.0)</td><td>(434.5)</td><td>(469.5)</td><td>(489.5)</td></tr><tr><td>Cash flow from investing</td><td>(221.5)</td><td>(435.0)</td><td>(470.0)</td><td>(490.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>(426.4)</td><td>(533.0)</td><td>(639.6)</td></tr><tr><td>Inc/(dec) in debt</td><td>(80.8)</td><td>(619.4)</td><td>(55.5)</td><td>(52.0)</td></tr><tr><td>Other financing cash flows</td><td>(11.5)</td><td>(800.0)</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(92.3)</td><td>(1,845.8)</td><td>(588.5)</td><td>(691.6)</td></tr><tr><td>Total cash flow</td><td>302.8</td><td>1,569.7</td><td>6,117.5</td><td>7,761.0</td></tr><tr><td>Free cash flow</td><td>616.0</td><td>3,849.9</td><td>7,175.5</td><td>8,942.0</td></tr></table>

Source: Company data, GS estimates.

make disciplined investments with an emphasis on profitability rather than chasing market share, but if the demand outlook were to be revised up substantially, it has the flexibility to undertake capex in line with market conditions.

(3) Long-term agreements (LTAs): Management views LTAs as an important strategy from the three perspectives of long-term demand visibility, backing for growth investments, and technical engagement with key customers. The company said it is making steady progress toward a $50\%$ LTA coverage ratio for CY28 shipment volume, and in some cases talks are beginning for periods from CY28 onward.

(4) Shareholder returns: Following the recent share price decline, the company said it resolved to conduct a share buyback, judging that a good opportunity had arrived to improve capital efficiency. Regarding cash flow, management's policy remains unchanged: after investing in capex, R&D, and human capital (returns to employees), it will allocate c.50% of surplus cash flow to shareholder returns. However, with cash expected to accumulate steadily from 2Q, Kioxia commented that it is exploring the possibility of additional shareholder returns, including dividends.

## Maintaining our view that earnings can expand at higher profit levels, unlike in past cycles

In the wake of 1Q results, we lower our FY3/27 operating profit estimate by 1% to factor in various provisions, but we raise our FY3/28-FY3/29 operating profit estimates by 3%/4%, mainly due to a change in our USD/JPY assumption to 160, from 155. We view management's decision to execute a share buyback just after a rapid correction in Kioxia's share price as a sign of its confidence in continued earnings growth and cash flow generation ahead. We also believe this move is likely to lead to Kioxia gaining a growing reputation as a management team capable of taking flexible action in the capital markets.

Although Kioxia's FY3/28 P/E has declined to around 3X, we continue to see NAND supply/demand tightening through 2027, and we believe higher profit levels compared to previous cycles are sustainable. We expect the share price multiple to expand as the market comes to recognize that profit levels over the next 2-3 years will be higher than its expectations as well as sustainable. We maintain our 12-month target price of ¥116,000 and reiterate our Buy rating.

Exhibit 1: Kioxia Holdings: Earnings summary

<table><tr><td colspan="15">Kioxia HD (285A)</td></tr><tr><td>(JPY mm)</td><td></td><td>GSE</td><td>GSE</td><td>GSE</td><td></td><td></td><td></td><td></td><td></td><td>GSE</td><td>GSE</td><td>GSE</td><td>CoE</td><td>CoE</td></tr><tr><td>Consolidated income statement</td><td>3/2026</td><td>3/2027</td><td>3/2028</td>

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
