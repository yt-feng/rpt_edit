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

# Chow Tai Fook Jewellery Group (1929.HK)

# 1QFY27 solid SSSG as expected, Jul decelerates with weather headwinds; confidence on full year guidance; Neutral

1929.HK 12m Price Target: HK\$13.00 Price: HK\$12.51 Upside: 3.9%

Chow Tai Fook (CTF) announced its 1QFY27 (Jun-26 quarter) trading update and hosted a conference call after the market close on Jul 23. Echoing our read across from Luk Fook result, Mainland China SSSG was strong at 19.6% for self-operated stores (compared to Apr-May at 19.7%, in line with GSe of 20%), and 15.7% for franchised stores respectively; HK&Macau performance remained robust at 41.7% (compared to Apr-May at 40.6%, slightly ahead of GSe of 40%). In ML China, compared to Luk Fook (+16%/+25% for self-operated stores/franchised stores), CTF outperformed in self-operated store channel while franchised stores underperformed; HK&Macau SSSG performance was similar to Luk Fook's 41%. By category, weight based products outperformed amid gold price correction, with +38%/+63.7% SSSG growth in ML China/HK&Macau, vs. fixed priced products at -1%/+13.1% respectively. ML China net closure was at 258 in the Jun quarter, and management expects full year store closure in ML China to be 600-700.

Looking ahead, management showed confidence to achieve the full year guidance and noted 1QFY27 performance was ahead of their expectation. Into Jul, the SSSG in Jul 1-19 saw deceleration from Jun quarter at SD% positive growth in ML China, which management attributed to weather headwinds and traffic dilution from World Cup event in the first two weeks. That said, performance saw sequential improvement in the third week. On the positive side, fixed price products saw outperformance in Jul (DD% at self-owned store channel), supported by gold price stabilization and successful products such as Dawn series (management revised up FY27 sales guidance to HK\$3bn from HK\$2bn).

We view the result as largely in line with market expectation with a strong Apr-May SSSG reported earlier. Dawn series is a positive surprise which also provided support to fixed priced products outperformance in Jul, yet 1QFY27 fixed priced product mix

## NEUTRAL

Xinyu Ruan
+852-2978-7347 | xinyu.ruan@gs.com
GS (Asia) L.L.C.

Michelle Cheng
+852-2978-6631 | michelle.cheng@gs.com
GS (Asia) L.L.C.

Molly Dai
+852-3966-4000 | molly.dai@gs.com
GS (Asia) L.L.C.

## Key Data

GS Forecast

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Revenue (HK$ mn)</td><td>94,398.4</td><td>98,750.8</td><td>101,045.9</td><td>103,308.7</td></tr><tr><td>EBITDA (HK$ mn)</td><td>20,654.8</td><td>15,652.6</td><td>16,617.6</td><td>17,016.9</td></tr><tr><td>EPS (HK$)</td><td>0.91</td><td>1.04</td><td>1.06</td><td>1.10</td></tr><tr><td>P/E (X)</td><td>14.6</td><td>12.1</td><td>11.7</td><td>11.4</td></tr><tr><td>P/B (X)</td><td>4.1</td><td>3.5</td><td>3.2</td><td>2.9</td></tr><tr><td>Dividend yield (%)</td><td>5.0</td><td>5.9</td><td>5.9</td><td>5.9</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>0.5</td><td>0.7</td><td>0.6</td><td>0.4</td></tr><tr><td>CROCI (%)</td><td>23.8</td><td>21.4</td><td>20.9</td><td>20.9</td></tr><tr><td>FCF yield (%)</td><td>0.6</td><td>6.1</td><td>7.9</td><td>8.5</td></tr><tr><td></td><td>9/25</td><td>3/26</td><td>9/26E</td><td>3/27E</td></tr><tr><td>EPS (HK$)</td><td>0.26</td><td>0.65</td><td>0.41</td><td>0.62</td></tr></table>

![](images/99790ef9da2c7733dde2b424653ee79b565e9f453a77b57794a9a7e852e05fda.jpg)  
Source: Company data, GS estimates. See disclosures for details.

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>14.8%</td><td>(10.7)%</td><td>(6.2)%</td></tr><tr><td>Rel. to the Hang Seng Index</td><td>18.0%</td><td>(5.3)%</td><td>(5.0)%</td></tr></table>

![](images/d3f82ca8d3f3a7827201ace6af7462b59e11a2127453752dcf0954ba9fdc7265.jpg)  
Chow Tai Fook Jewellery Group (1929.HK)  
Rating since Jun 21, 2017

Ratios & Valuation

<table><tr><td colspan="5">Ratios &amp; Valuation</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>P/E (X)</td><td>14.6</td><td>12.1</td><td>11.7</td><td>11.4</td></tr><tr><td>P/B (X)</td><td>4.1</td><td>3.5</td><td>3.2</td><td>2.9</td></tr><tr><td>FCF yield (%)</td><td>0.6</td><td>6.1</td><td>7.9</td><td>8.5</td></tr><tr><td>EV/EBITDAR (X)</td><td>6.9</td><td>8.6</td><td>8.0</td><td>7.7</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>7.1</td><td>9.0</td><td>8.4</td><td>8.0</td></tr><tr><td>CROCI (%)</td><td>23.8</td><td>21.4</td><td>20.9</td><td>20.9</td></tr><tr><td>ROE (%)</td><td>31.4</td><td>31.5</td><td>29.6</td><td>27.8</td></tr><tr><td>Net debt/equity (%)</td><td>35.1</td><td>34.1</td><td>27.0</td><td>19.1</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>32.0</td><td>30.0</td><td>23.3</td><td>15.7</td></tr><tr><td>Interest cover (X)</td><td>29.0</td><td>16.3</td><td>17.5</td><td>18.4</td></tr><tr><td>Days inventory outst, sales</td><td>230.3</td><td>241.7</td><td>244.8</td><td>244.2</td></tr><tr><td>Receivable days</td><td>17.2</td><td>17.5</td><td>17.7</td><td>17.6</td></tr><tr><td>Days payable outstanding</td><td>146.6</td><td>124.2</td><td>122.7</td><td>121.1</td></tr><tr><td>DuPont ROE (%)</td><td>28.2</td><td>29.2</td><td>27.4</td><td>25.8</td></tr><tr><td>Turnover (X)</td><td>1.1</td><td>1.1</td><td>1.1</td><td>1.0</td></tr><tr><td>Leverage (X)</td><td>2.7</td><td>2.6</td><td>2.5</td><td>2.4</td></tr><tr><td>Gross cash invested (ex cash) (HK$)</td><td>57,176.6</td><td>61,046.2</td><td>62,925.8</td><td>64,394.5</td></tr><tr><td>Average capital employed (HK$)</td><td>40,841.5</td><td>43,815.4</td><td>46,309.8</td><td>47,805.4</td></tr><tr><td>BVPS (HK$)</td><td>3.22</td><td>3.55</td><td>3.88</td><td>4.24</td></tr></table>

Income Statement (HK\$ mn)

Growth & Margins (%)

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue growth</td><td>5.3</td><td>4.6</td><td>2.3</td><td>2.2</td></tr><tr><td>EBITDA growth</td><td>22.6</td><td>(24.2)</td><td>6.2</td><td>2.4</td></tr><tr><td>EPS growth</td><td>53.2</td><td>14.3</td><td>2.7</td><td>2.9</td></tr><tr><td>DPS growth</td><td>28.3</td><td>10.9</td><td>0.0</td><td>0.0</td></tr><tr><td>EBIT margin</td><td>20.0</td><td>14.1</td><td>14.7</td><td>14.8</td></tr><tr><td>EBITDA margin</td><td>21.9</td><td>15.9</td><td>16.4</td><td>16.5</td></tr><tr><td>Net income margin</td><td>9.5</td><td>10.4</td><td>10.4</td><td>10.5</td></tr></table>

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue</td><td>94,398.4</td><td>98,750.8</td><td>101,045.9</td><td>103,308.7</td></tr><tr><td>Cost of goods sold</td><td>(63,898.0)</td><td>(72,674.0)</td><td>(73,515.3)</td><td>(74,817.5)</td></tr><tr><td>SG&amp;A</td><td>(12,343.1)</td><td>(12,861.7)</td><td>(13,354.2)</td><td>(13,942.8)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>692.9</td><td>692.3</td><td>695.6</td><td>701.2</td></tr><tr><td>EBITDA</td><td>20,654.8</td><td>15,652.6</td><td>16,617.6</td><td>17,016.9</td></tr><tr><td>Depreciation &amp; amortization</td><td>(1,804.6)</td><td>(1,745.2)</td><td>(1,745.6)</td><td>(1,767.3)</td></tr><tr><td>EBIT</td><td>18,850.2</td><td>13,907.4</td><td>14,872.0</td><td>15,249.6</td></tr><tr><td>Net interest inc./(exp.)</td><td>(649.2)</td><td>(851.9)</td><td>(851.9)</td><td>(827.1)</td></tr><tr><td>Income/(loss) from associates</td><td>2.7</td><td>0.0</td><td>0.0</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>11,945.8</td><td>13,570.4</td><td>13,934.9</td><td>14,337.4</td></tr><tr><td>Provision for taxes</td><td>(2,865.4)</td><td>(3,255.1)</td><td>(3,342.5)</td><td>(3,439.1)</td></tr><tr><td>Minority interest</td><td>(76.1)</td><td>(86.4)</td><td>(88.8)</td><td>(91.3)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>9,004.3</td><td>10,228.8</td><td>10,503.6</td><td>10,807.0</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>0.0</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>9,004.3</td><td>10,228.8</td><td>10,503.6</td><td>10,807.0</td></tr><tr><td>EPS (basic, pre-except) (HK$)</td><td>0.91</td><td>1.04</td><td>1.06</td><td>1.10</td></tr><tr><td>EPS (diluted, pre-except) (HK$)</td><td>0.91</td><td>1.04</td><td>1.06</td><td>1.10</td></tr><tr><td>EPS (basic, post-except) (HK$)</td><td>0.91</td><td>1.04</td><td>1.06</td><td>1.10</td></tr><tr><td>EPS (diluted, post-except) (HK$)</td><td>0.91</td><td>1.04</td><td>1.06</td><td>1.10</td></tr><tr><td>DPS (HK$)</td><td>0.67</td><td>0.74</td><td>0.74</td><td>0.74</td></tr><tr><td>Div. payout ratio (%)</td><td>73.5</td><td>71.4</td><td>69.5</td><td>67.5</td></tr></table>

Price Performance  
![](images/28056dbe14a05a2bf40b048c6777b4372362ec4a49488fe2b5a9bf3882317dd0.jpg)  
Source: FactSet. Price as of 23 Jul 2026 close.

Balance Sheet (HK\$ mn)

<table><tr><td colspan="5">Balance Sheet (HK$ mn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>8,262.1</td><td>10,172.2</td><td>12,300.9</td><td>14,635.7</td></tr><tr><td>Accounts receivable</td><td>4,637.9</td><td>4,847.9</td><td>4,943.9</td><td>5,038.7</td></tr><tr><td>Inventory</td><td>63,715.8</td><td>67,058.1</td><td>68,466.9</td><td>69,756.0</td></tr><tr><td>Other current assets</td><td>21.5</td><td>46.2</td><td>46.7</td><td>47.1</td></tr><tr><td>Total current assets</td><td>76,637.3</td><td>82,124.4</td><td>85,758.4</td><td>89,477.5</td></tr><tr><td>Net PP&amp;E</td><td>4,810.8</td><td>4,983.1</td><td>5,191.9</td><td>5,401.2</td></tr><tr><td>Net intangibles</td><td>5.3</td><td>(36.0)</td><td>(77.3)</td><td>(118.6)</td></tr><tr><td>Total investments</td><td>40.0</td><td>40.0</td><td>40.0</td><td>40.0</td></tr><tr><td>Other long-term assets</td><td>4,361.1</td><td>4,361.1</td><td>4,361.1</td><td>4,361.1</td></tr><tr><td>Total assets</td><td>85,854.5</td><td>91,472.6</td><td>95,274.1</td><td>99,161.2</td></tr><tr><td>Accounts payable</td><td>24,725.9</td><td>24,726.1</td><td>24,687.5</td><td>24,961.5</td></tr><tr><td>Short-term debt</td><td>18,480.4</td><td>20,651.8</td><td>21,200.3</td><td>21,215.9</td></tr><tr><td>Short-term lease liabilities</td><td>579.7</td><td>571.4</td><td>571.0</td><td>570.7</td></tr><tr><td>Other current liabilities</td><td>1,752.2</td><td>1,752.2</td><td>1,752.2</td><td>1,752.2</td></tr><tr><td>Total current liabilities</td><td>45,538.2</td><td>47,701.4</td><td>48,211.1</td><td>48,500.3</td></tr><tr><td>Long-term debt</td><td>0.0</td><td>0.0</td><td>-</td><td>-</td></tr><tr><td>Long-term lease liabilities</td><td>426.1</td><td>865.7</td><td>865.2</td><td>864.7</td></tr><tr><td>Other long-term liabilities</td><td>713.1</td><td>713.1</td><td>713.1</td><td>713.1</td></tr><tr><td>Total long-term liabilities</td><td>8,357.5</td><td>8,797.1</td><td>8,796.6</td><td>8,796.1</td></tr><tr><td>Total liabilities</td><td>53,895.7</td><td>56,498.5</td><td>57,007.6</td><td>57,296.4</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>30,973.4</td><td>33,902.2</td><td>37,105.9</td><td>40,612.9</td></tr><tr><td>Minority interest</td><td>985.4</td><td>1,071.8</td><td>1,160.6</td><td>1,252.0</td></tr><tr><td>Total liabilities &amp; equity</td><td>85,854.5</td><td>91,472.6</td><td>95,274.1</td><td>99,161.2</td></tr><tr><td>Net debt, adjusted</td><td>10,218.3</td><td>10,479.6</td><td>8,899.4</td><td>6,580.1</td></tr></table>

<table><tr><td colspan="5">Cash flow (HK$ mn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Net income</td><td>9,004.3</td><td>10,228.8</td><td>10,503.6</td><td>10,807.0</td></tr><tr><td>D&amp;A add-back</td><td>1,804.6</td><td>1,745.2</td><td>1,745.6</td><td>1,767.3</td></tr><tr><td>Minority interest add-back</td><td>76.1</td><td>86.4</td><td>88.8</td><td>91.3</td></tr><tr><td>Net (inc)/dec working capital</td><td>(10,615.3)</td><td>(3,544.2)</td><td>(1,531.4)</td><td>(1,098.6)</td></tr><tr><td>Other operating cash flow</td><td>1,047.3</td><td>(32.6)</td><td>(12.3)</td><td>(11.7)</td></tr><tr><td>Cash flow from operations</td><td>1,317.0</td><td>8,483.7</td><td>10,794.3</td><td>11,555.4</td></tr><tr><td>Capital expenditures</td><td>(593.0)</td><td>(987.5)</td><td>(1,010.5)</td><td>(1,033.1)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>11.9</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>205.7</td><td>(93.4)</td><td>(93.4)</td><td>(93.4)</td></tr><tr><td>Cash flow from investing</td><td>(375.4)</td><td>(1,080.9)</td><td>(1,103.9)</td><td>(1,126.5)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(5,327.1)</td><td>(7,300.0)</td><td>(7,300.0)</td><td>(7,300.0)</td></tr><tr><td>Inc/(dec) in debt</td><td>(1,214.5)</td><td>2,171.4</td><td>548.5</td><td>15.6</td></tr><tr><td>Other financing cash flows</td><td>6,279.7</td><td>(364.1)</td><td>(810.1)</td><td>(809.7)</td></tr><tr><td>Cash flow from financing</td><td>(261.9)</td><td>(5,492.7)</td><td>(7,561.6)</td><td>(8,094.1)</td></tr><tr><td>Total cash flow</td><td>679.7</td><td>1,910.1</td><td>2,128.8</td><td>2,334.8</td></tr><tr><td>Free cash flow</td><td>724.0</td><td>7,496.2</td><td>9,783.8</td><td>10,522.3</td></tr></table>

Source: Company data, GS estimates.

declined by 5pp yoy in ML China amid gold price headwinds. We believe the SSSG sustainability and whether new products are able to drive fixed priced products mix improvement (vs. company guidance of slight yoy mix expansion in FY27) will be key to watch. Remain Neutral.

We would like to thank Mattie, He for her contribution to the report.

## 1QFY27 trading updates

## Mainland China:

1QFY27 SSSG of self-operated stores came in at +19.6% yoy, mainly driven by ASP increase offset by 5.2% volume decline. It implies Jun-quarter SSS at 5% below the same period in 2019 (or pre-COVID level), accelerated from 15% below in the Mar quarter. SSSG of franchised stores was at 15.7%.

By product, fixed-price jewelry SSS was down by 1% yoy, with fixed-price gold/gem-set ASP growing by +40%/+4% yoy to HK\$9,100/8,700. Weight-based jewelry SSSG was up 38% yoy, with ASP increased by +26% to HK\$10,600. The company is still going through retail network optimization and it recorded net closed 258 stores in mainland China in the Jun quarter. RSV of e-commerce remained strong and grew by 28.9%, contributing to 8.9% of retail sales.

## HK and Macau:

1QFY27 SSSG was up 41.7% yoy, with Hong Kong up by 35% and Macau up by 64.6%, mainly driven by ASP increase while volume also saw 9.4% yoy increase. It implies Jun-quarter SSS at 71% of the level in 2018 (or normal level, i.e. pre-COVID and before the HK macro situation), vs. 4QFY26 of 80%.

By product, fixed-price jewelry SSS was up by 13.1% yoy, with fixed-price gold/gem-set ASP changed by +71%/+2% yoy to HK\$8,700/16,600. Weight-based jewelry SSSG was up 63.7% yoy, with ASP increased by +10% to HK\$17,100.

## Key takeaways from conference call

FY27 guidance reiterated: Mgmt reiterated MSD-HSD revenue growth, HSD SSSG in ML China and low-teens SSSG in HK and Macau. Under the assumption of gold price US\$4,300/oz, GPM/OPM guidance remained at 26.5%-27.5%/c.14%, respectively; and HK\$500-800mn of hedging gains. At the current c.US\$4,100 per ounce, mgmt expects limited revenue impact with weight-based gold demand being supported. A higher weight-based gold mix may affect GPM, but would be offset by operating leverage from higher weight based products sales/hedgi

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
