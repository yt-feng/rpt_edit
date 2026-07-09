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
# All Ring Tech Co. (6187.TWO)

CPO concern likely largely priced in; building in stronger CoWoS into 2027E; reiterate Buy

6187.TWO 12m Price Target: NT\$1,550.00 Price: NT\$955.00 Upside: 62.3%

## 2Q26 tracking ahead of expectations

All Ring reported its June 2026 revenue on July 8, 2026, with June revenue of NT\$1,012mn, bringing total 2Q26 revenue to NT\$2,355mn, coming in 12.8% ahead of GSe. We attribute the strong 2Q26 momentum primarily to the stronger ramp of CoWoS demand from customers. With this, we raise our 2Q26 GM as we anticipate All Ring to exceed our prior expectation (52.3% previously), supported by a higher advanced packaging mix, though we now expect a modest sequential decline in 4Q26 GM as All Ring begins shipping new products including new panel-level equipment, which we believe will weigh on margins during the initial ramp-up phase. Overall, we now forecast 2Q26/3Q26/4Q26E GM to be 54.0%/54.5%/52.7%.

## Stronger advanced packaging expansion supporting 2027 outlook

Stronger advanced packaging expansion supporting 2027 Outlook In our recent TSMC report (see: TSMC (2330.TW) Accelerating capacity build to secure a stronger growth trajectory, 3 Jul 2026), we raised our end-2027E CoWoS (include WMCM) capacity to 280kwpm (vs. 250kwpm previously), fueled by stronger AI accelerator and server-CPU demand. As a key back-end equipment supplier for CoWoS, we expect All Ring to benefit directly from such accelerating capacity expansion. We now model All Ring's CoWoS-related revenue to grow $27\%$ YoY in 2027E (vs. $16\%$ YoY previously) and account for $77\%$ of total revenue (vs. $60\%$ previously).

CPO trending towards fewer shipment but higher-value tools
On the CPO side, we revise down our revenue forecast as we factor in lower equipment shipment as we believe All Ring is working to increase the throughput to meet customer requests. While we believe this could translate into fewer equipment shipments given higher productivity, we expect the content value per equipment to increase. On pricing, we now see upside to ASP and are now

## BUY

Evelyn Yu  
+886(2)2730-4187 | evelyn.yu@gs.com  
GS (Asia) L.L.C., Taipei Branch

Ryan Huang, CFA
+886(2)2730-4084 | ryan.huang@gs.com
GS (Asia) L.L.C., Taipei Branch

Market cap: NT\$91.7bn / \$2.9bn
Enterprise value: NT\$88.6bn / \$2.8bn
3m ADTV: NT\$3.7bn / \$117.0mn
Taiwan
Taiwan Semiconductor
M&A Rank: 3
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (NT$ mn) New</td><td>5,366.2</td><td>9,276.9</td><td>13,477.6</td><td>17,193.8</td></tr><tr><td>Revenue (NT$ mn) Old</td><td>5,366.2</td><td>8,865.3</td><td>14,693.0</td><td>19,889.0</td></tr><tr><td>EBITDA (NT$ mn)</td><td>1,679.3</td><td>3,265.4</td><td>5,316.0</td><td>7,197.3</td></tr><tr><td>EPS (NT$) New</td><td>15.47</td><td>28.23</td><td>44.30</td><td>59.13</td></tr><tr><td>EPS (NT$) Old</td><td>15.47</td><td>26.33</td><td>47.13</td><td>66.88</td></tr><tr><td>P/E (X)</td><td>22.7</td><td>33.8</td><td>21.6</td><td>16.2</td></tr><tr><td>P/B (X)</td><td>4.5</td><td>11.2</td><td>8.8</td><td>7.1</td></tr><tr><td>Dividend yield (%)</td><td>3.3</td><td>2.2</td><td>3.5</td><td>4.6</td></tr><tr><td>CROCI (%)</td><td>44.2</td><td>36.5</td><td>66.9</td><td>71.2</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (NT$)</td><td>3.37</td><td>6.25</td><td>10.82</td><td>7.79</td></tr></table>

GS Factor Profile

![](images/da4ff28a718fcc323566c69f502eff4cb30195838bc28785bee30e6f4acfd03c.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## All Ring Tech Co. (6187.TWO)

BUY

Rating since Mar 11, 2026

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>22.7</td><td>33.8</td><td>21.6</td><td>16.2</td></tr><tr><td>P/B (X)</td><td>4.5</td><td>11.2</td><td>8.8</td><td>7.1</td></tr><tr><td>FCF yield (%)</td><td>4.3</td><td>0.2</td><td>2.6</td><td>4.9</td></tr><tr><td>EV/EBITDAR (X)</td><td>17.8</td><td>27.2</td><td>16.6</td><td>12.1</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>17.8</td><td>27.2</td><td>16.6</td><td>12.1</td></tr><tr><td>CROCI (%)</td><td>44.2</td><td>36.5</td><td>66.9</td><td>71.2</td></tr><tr><td>ROE (%)</td><td>21.5</td><td>35.3</td><td>46.2</td><td>49.1</td></tr><tr><td>Net debt/equity (%)</td><td>(51.3)</td><td>(37.1)</td><td>(32.9)</td><td>(36.8)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(51.3)</td><td>(37.1)</td><td>(32.9)</td><td>(36.8)</td></tr><tr><td>Interest cover (X)</td><td>172.6</td><td>459.1</td><td>824.4</td><td>1,113.7</td></tr><tr><td>Days inventory outst, sales</td><td>70.2</td><td>72.4</td><td>83.7</td><td>73.2</td></tr><tr><td>Receivable days</td><td>82.1</td><td>46.5</td><td>56.4</td><td>56.4</td></tr><tr><td>Days payable outstanding</td><td>210.6</td><td>173.0</td><td>206.7</td><td>191.5</td></tr><tr><td>DuPont ROE (%)</td><td>19.8</td><td>32.8</td><td>40.5</td><td>43.7</td></tr><tr><td>Turnover (X)</td><td>0.6</td><td>0.8</td><td>0.9</td><td>1.0</td></tr><tr><td>Leverage (X)</td><td>1.3</td><td>1.4</td><td>1.5</td><td>1.4</td></tr><tr><td>Gross cash invested (ex cash) (NT$)</td><td>3,924.6</td><td>5,543.8</td><td>7,534.1</td><td>8,891.0</td></tr><tr><td>Average capital employed (NT$)</td><td>3,457.9</td><td>4,430.7</td><td>6,140.3</td><td>7,651.2</td></tr><tr><td>BVPS (NT$)</td><td>77.10</td><td>85.60</td><td>108.51</td><td>134.16</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(3.0)</td><td>72.9</td><td>45.3</td><td>27.6</td></tr><tr><td>EBITDA growth</td><td>13.2</td><td>94.4</td><td>62.8</td><td>35.4</td></tr><tr><td>EPS growth</td><td>0.7</td><td>82.5</td><td>56.9</td><td>33.5</td></tr><tr><td>DPS growth</td><td>0.7</td><td>82.5</td><td>56.9</td><td>33.5</td></tr><tr><td>EBIT margin</td><td>30.0</td><td>34.1</td><td>38.4</td><td>40.8</td></tr><tr><td>EBITDA margin</td><td>31.3</td><td>35.2</td><td>39.4</td><td>41.9</td></tr><tr><td>Net income margin</td><td>27.7</td><td>29.3</td><td>31.7</td><td>33.1</td></tr></table>

Price Performance  
![](images/b8b6a01fcbc9d3fac1cc5878dede050de85365d774cf5544a5b05166d28b4322.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>(2.6)%</td><td>143.0%</td><td>140.9%</td></tr><tr><td>Rel. to the Taiwan SE Weighted Index</td><td>(25.9)%</td><td>61.3%</td><td>17.8%</td></tr></table>

Source: FactSet. Price as of 8 Jul 2026 close.

Income Statement (NT\$ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>5,366.2</td><td>9,276.9</td><td>13,477.6</td><td>17,193.8</td></tr><tr><td>Cost of goods sold</td><td>(2,452.9)</td><td>(4,315.3)</td><td>(6,155.2)</td><td>(7,448.7)</td></tr><tr><td>SG&amp;A</td><td>(535.8)</td><td>(961.9)</td><td>(986.2)</td><td>(1,271.3)</td></tr><tr><td>R&amp;D</td><td>(766.8)</td><td>(835.2)</td><td>(1,161.9)</td><td>(1,460.3)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>1,679.3</td><td>3,265.4</td><td>5,316.0</td><td>7,197.3</td></tr><tr><td>Depreciation &amp; amortization</td><td>(68.5)</td><td>(100.9)</td><td>(141.7)</td><td>(183.7)</td></tr><tr><td>EBIT</td><td>1,610.8</td><td>3,164.5</td><td>5,174.3</td><td>7,013.6</td></tr><tr><td>Net interest inc./(exp.)</td><td>40.0</td><td>37.2</td><td>39.7</td><td>39.6</td></tr><tr><td>Income/(loss) from associates</td><td>(0.6)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>1,812.8</td><td>3,283.8</td><td>5,234.0</td><td>7,073.2</td></tr><tr><td>Provision for taxes</td><td>(316.4)</td><td>(570.0)</td><td>(968.3)</td><td>(1,379.3)</td></tr><tr><td>Minority interest</td><td>(11.2)</td><td>4.6</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>1,485.2</td><td>2,718.4</td><td>4,265.7</td><td>5,693.9</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>1,485.2</td><td>2,718.4</td><td>4,265.7</td><td>5,693.9</td></tr><tr><td>EPS (basic, pre-except) (NT$)</td><td>15.47</td><td>28.23</td><td>44.30</td><td>59.13</td></tr><tr><td>EPS (diluted, pre-except) (NT$)</td><td>15.47</td><td>28.23</td><td>44.30</td><td>59.13</td></tr><tr><td>EPS (basic, post-except) (NT$)</td><td>15.47</td><td>28.23</td><td>44.30</td><td>59.13</td></tr><tr><td>EPS (diluted, post-except) (NT$)</td><td>15.47</td><td>28.23</td><td>44.30</td><td>59.13</td></tr><tr><td>DPS (NT$)</td><td>11.56</td><td>21.11</td><td>33.12</td><td>44.21</td></tr><tr><td>Div. payout ratio (%)</td><td>74.8</td><td>74.8</td><td>74.8</td><td>74.8</td></tr></table>

Balance Sheet (NT\$ mn)

<table><tr><td colspan="5">Balance Sheet (NT$ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>4,182.0</td><td>3,210.1</td><td>3,594.4</td><td>4,925.2</td></tr><tr><td>Accounts receivable</td><td>858.6</td><td>1,505.4</td><td>2,656.4</td><td>2,660.4</td></tr><tr><td>Inventory</td><td>1,114.0</td><td>2,564.9</td><td>3,616.8</td><td>3,279.6</td></tr><tr><td>Other current assets</td><td>180.4</td><td>294.5</td><td>294.5</td><td>294.5</td></tr><tr><td>Total current assets</td><td>6,335.2</td><td>7,574.9</td><td>10,162.1</td><td>11,159.8</td></tr><tr><td>Net PP&amp;E</td><td>1,878.7</td><td>2,797.9</td><td>3,840.9</td><td>4,848.9</td></tr><tr><td>Net intangibles</td><td>31.8</td><td>47.4</td><td>64.2</td><td>74.0</td></tr><tr><td>Total investments</td><td>986.8</td><td>1,111.4</td><td>1,111.4</td><td>1,111.4</td></tr><tr><td>Other long-term assets</td><td>376.9</td><td>431.0</td><td>431.0</td><td>431.0</td></tr><tr><td>Total assets</td><td>9,609.4</td><td>11,962.6</td><td>15,609.6</td><td>17,625.1</td></tr><tr><td>Accounts payable</td><td>1,292.4</td><td>2,799.2</td><td>4,173.3</td><td>3,644.8</td></tr><tr><td>Short-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>348.0</td><td>593.9</td><td>633.9</td><td>673.9</td></tr><tr><td>Total current liabilities</td><td>1,640.4</td><td>3,393.1</td><td>4,807.2</td><td>4,318.7</td></tr><tr><td>Long-term debt</td><td>339.2</td><td>132.8</td><td>132.8</td><td>132.8</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>141.6</td><td>143.4</td><td>143.4</td><td>143.4</td></tr><tr><td>Total long-term liabilities</td><td>480.8</td><td>276.2</td><td>276.2</td><td>276.2</td></tr><tr><td>Total liabilities</td><td>2,121.2</td><td>3,669.3</td><td>5,083.4</td><td>4,594.9</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>7,299.0</td><td>8,108.6</td><td>10,341.5</td><td>12,845.5</td></tr><tr><td>Minority interest</td><td>189.2</td><td>184.6</td><td>184.6</td><td>184.6</td></tr><tr><td>Total liabilities &amp; equity</td><td>9,609.4</td><td>11,962.6</td><td>15,609.6</td><td>17,625.1</td></tr><tr><td>Net debt, adjusted</td><td>(3,842.8)</td><td>(3,077.2)</td><td>(3,461.6)</td><td>(4,792.4)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (NT$ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>1,485.2</td><td>2,718.4</td><td>4,265.7</td><td>5,693.9</td></tr><tr><td>D&amp;A add-back</td><td>68.5</td><td>100.9</td><td>141.7</td><td>183.7</td></tr><tr><td>Minority interest add-back</td><td>11.2</td><td>(4.6)</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>287.1</td><td>(590.9)</td><td>(828.8)</td><td>(195.3)</td></tr><tr><td>Other operating cash flow</td><td>106.1</td><td>(1,054.7)</td><td>-</td><td>-</td></tr><tr><td>Cash flow from operations</td><td>1,958.0</td><td>1,169.1</td><td>3,578.6</td><td>5,682.3</td></tr><tr><td>Capital expenditures</td><td>(512.9)</td><td>(1,010.0)</td><td>(1,161.5)</td><td>(1,161.5)</td></tr><tr><td>Acquisitions</td><td>(87.8)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(65.2)</td><td>(45.3)</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(665.9)</td><td>(1,055.3)</td><td>(1,161.5)</td><td>(1,161.5)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(980.0)</td><td>(1,110.6)</td><td>(2,032.8)</td><td>(3,189.9)</td></tr><tr><td>Inc/(dec) in debt</td><td>142.1</td><td>(2.0)</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>191.3</td><td>26.9</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(646.5)</td><td>(1,085.7)</td><td>(2,032.8)</td><td>(3,189.9)</td></tr><tr><td>Total cash flow</td><td>645.6</td><td>(972.0)</td><td>384.3</td><td>1,330.8</td></tr><tr><td>Free cash flow</td><td>1,445.2</td><td>159.0</td><td>2,417.1</td><td>4,520.8</td></tr></table>

Source: Company data, GS estimates.

expecting at least around 20% higher pricing, reflecting the higher complexity and performance of these next-generation systems. We continue to see CPO as the next key growth driver for All Ring, and we now model All Ring's CPO revenue to reach NT\$2.1bn/NT\$10.2bn, accounting for 16%/60% of revenue in 2027E/2028E (vs. 29%/69% previously).

## Risk-reward now skewed to the upside

All Ring's shares have declined -31% from its recent peak in April (vs. TAIEX's +21%). We believe this weakness largely reflects a cluster of market concerns including potential CPO delay. However, we see All Ring's fundamental demand remaining solid across both CoWoS and CPO, and the company continues to lead peers on CPO equipment throughput. Given the improving near-term outlook, an accelerating advanced packaging build plan into 2027, and resilient long-term CPO demand, we view the risk-reward as skewed to the upside and reiterate our Buy rating. Accordingly, we adjust our 2026E-2028E earnings by +7%/-6%/-12% and revise our 12-month TP to NT\$1,550 from NT\$1,650 implying 62% upside.

Exhibit 1: All Ring's revenue growth outlook  
![](images/ad18e3733a186300f10028563315a873650890e8998006aa2c7dc946f9e6235b.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: All Ring's margin trend  
![](images/68e9c58311fa2402d4265f38b1e9fdc66a9b14b2daca489604c47e1883758191.jpg)  
Source: Company data, GS Global Investment Research

## Earnings changes, valuation and risks

## Forecast changes

We revise our 2026E-28E EPS by $+7.2\% / -6.0\% / -11.6\%$ mainly as we factor in 1) stronger 2Q26 revenue and GM assumptions, 2) accelerating CoWoS expansion in 2027E/2028E, but 3) lower CPO equipment units in 2027E/2028E.

Exhibit 3: Earnings revisions

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Diff (%)</td><td>Old</td><td>New</td><td>Diff (%)</td><td>Old</td><td>New</td><td>Diff (%)</td></tr><tr><td>Revenue</td><td>8,865</td><td>9,277</td><td>4.6%</td><td>14,693</td><td>13,478</td><td>-8.3%</td><td>19,889</td><td>17,194</td><td>-13.6%</td></tr><tr><td>Gross profit</td><td>4,709</td><td>4,962</td><td>5.4%</td><td>8,046</td><td>7,322</td><td>-9.0%</td><td>11,351</td><td>9,745</td><td>-14.1%</td></tr><tr><td>Op. income</td><td>2,923</td><td>3,164</td><td>8.3%</td><td>5,460</td><td>5,174</td><td>-5.2%</td><td>7,8

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
