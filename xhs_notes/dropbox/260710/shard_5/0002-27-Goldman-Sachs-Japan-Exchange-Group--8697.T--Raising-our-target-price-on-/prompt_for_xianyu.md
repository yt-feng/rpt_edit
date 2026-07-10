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
# Japan Exchange Group (8697.T)

Raising our target price on higher trading value and turnover; maintain Buy; trading value ex AI stocks also strong

8697.T

12m Price Target: ¥2,400

Price: ¥2,122

Upside: $13.1\%$

We adjust our earnings estimates and raise our target price by 23% for JPX, reflecting recent earnings, trading value trends, and changes in the interest rate environment. ADTV for April-June 2026 was ¥12.392 tn (domestic common stocks, ETFs/REITs), representing a +106% yoy increase, with strong growth of +63% yoy in April, +118% yoy in May, and +139% yoy in June. Turnover (trading value divided by market cap) is also up, reaching 193% in April, 244% in May, and 250% in June. Although AI-related stocks contributed significantly, ADTV excluding AI stocks (calculated by subtracting the trading value and market cap of AI-related stocks) also grew sharply by +49-137% yoy in April-June, with non-AI turnover also up substantially at 175% in April, 230% in May, and 244% in June. This expansion in trading activity could be attributed to increased trading by foreign and retail investors, possibly driven by expectations for corporate governance reforms.

We adjust our profit estimates for JPX using the past 12-month average adjusted turnover (excludes AI-related stocks from both the numerator and denominator for monthly turnover) to eliminate AI-related volatility. Even when excluding AI-related stocks, turnover remains high, and we therefore make upward adjustments to our ADTV estimates of +38% for FY3/27, +22% for FY3/28, and +26% for FY3/29. At the same time, factoring in capacity updates for the “arrowhead” equity order processing system and scope for general IT system investment, we also raise our operating expense estimates by +10%/+11%/+12%. As a result, we raise our EPS forecasts by +28%/+12%/+12%.

We raise our 12-month target price to ¥2,400 (+13% upside from the July 9 close; previous TP ¥1,950) reflecting the increase in our EPS estimates. Our TP is calculated by multiplying our FY3/28 EPS estimate by 5-year average 12-month forward P/E (25.19X). Key catalysts include a potential upward revision to full-year guidance reflecting upside in trading value (historically implemented in

Makoto Kuroda
+81(3)4587-9920 | makoto.kuroda@gs.com
GS Japan Co., Ltd.

Hibiki Takuma  
+81(3)4587-4935 | hibiki.takuma@gs.com  
GS Japan Co., Ltd.

Key Data

Market cap: ¥2.2tr / \$13.4bn  
3m ADTV: ¥8.1bn / \$50.8mn  
Japan  
Japan Financials  
M&A Rank: 3

GS Forecast

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Revenue (¥ bn) New</td><td>198.7</td><td>243.6</td><td>248.5</td><td>264.5</td></tr><tr><td>Revenue (¥ bn) Old</td><td>188.6</td><td>205.6</td><td>226.0</td><td>239.0</td></tr><tr><td>EPS (¥) New</td><td>76.8</td><td>98.1</td><td>95.3</td><td>103.3</td></tr><tr><td>EPS (¥) Old</td><td>70.7</td><td>76.5</td><td>85.1</td><td>91.8</td></tr><tr><td>P/E (X)</td><td>21.7</td><td>21.6</td><td>22.3</td><td>20.5</td></tr><tr><td>P/B (X)</td><td>5.0</td><td>6.2</td><td>6.0</td><td>5.5</td></tr><tr><td>ROE (%)</td><td>23.2</td><td>28.9</td><td>27.4</td><td>27.8</td></tr><tr><td>DPS (¥)</td><td>60.9</td><td>75.9</td><td>65.9</td><td>70.0</td></tr><tr><td>Dividend yield (%)</td><td>3.7</td><td>3.6</td><td>3.1</td><td>3.3</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (¥)</td><td>23.5</td><td>28.8</td><td>21.4</td><td>22.9</td></tr></table>

GS Factor Profile

![](images/7cabe9e8fb86671eaa52ab7c5bc93fcef25b1058e21800f9b99b90bb9eecb63d.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Japan Exchange Group (8697.T)

Rating since Aug 14, 2025

Ratios & Valuation

<table><tr><td colspan="5">Ratios &amp; Valuation</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>P/E (X)</td><td>21.7</td><td>21.6</td><td>22.3</td><td>20.5</td></tr><tr><td>P/B (X)</td><td>5.4</td><td>6.2</td><td>6.0</td><td>5.5</td></tr><tr><td>Dividend yield (%)</td><td>3.7</td><td>3.6</td><td>3.1</td><td>3.3</td></tr><tr><td>ROE (%)</td><td>23.2</td><td>28.9</td><td>27.4</td><td>27.8</td></tr><tr><td>Clearing house funds (¥ bn)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Margin funds (¥ bn)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total client assets (¥ bn)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue growth</td><td>22.5</td><td>22.6</td><td>2.0</td><td>6.5</td></tr><tr><td>EPS growth</td><td>30.8</td><td>27.8</td><td>(2.9)</td><td>8.4</td></tr><tr><td>EBITDA margin</td><td>67.0</td><td>66.5</td><td>63.3</td><td>63.7</td></tr><tr><td>Op. profit margin</td><td>57.9</td><td>58.7</td><td>55.5</td><td>56.1</td></tr><tr><td>Pre-tax margin</td><td>59.0</td><td>59.9</td><td>56.7</td><td>57.3</td></tr><tr><td>Net margin</td><td>39.8</td><td>41.1</td><td>38.9</td><td>39.4</td></tr></table>

Price Performance  
![](images/f1795f3bc08d62dac8c670dd9fed662d0d24acd6e9e8f99e41f7da68d94def8c.jpg)

<table><tr><td></td><td>3m</td><td>6m</td><td>12m</td></tr><tr><td>Absolute</td><td>10.5%</td><td>20.3%</td><td>41.8%</td></tr><tr><td>Rel. to the TOPIX</td><td>2.8%</td><td>5.1%</td><td>(0.3)%</td></tr></table>

Source: FactSet. Price as of 9 Jul 2026 close.

Income Statement (¥ bn)

<table><tr><td colspan="5">Income Statement (¥ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Equity trading &amp; clearing fees</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Derivatives trading fees</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Depository services</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Market data</td><td>33.7</td><td>35.4</td><td>36.6</td><td>38.0</td></tr><tr><td>Listing fees</td><td>18.7</td><td>20.0</td><td>20.8</td><td>21.5</td></tr><tr><td>Investment income (operating)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other revenue</td><td>14.8</td><td>15.7</td><td>16.5</td><td>17.3</td></tr><tr><td>Total revenue</td><td>198.7</td><td>243.6</td><td>248.5</td><td>264.5</td></tr><tr><td>Compensation &amp; benefits exp.</td><td>(24.3)</td><td>(25.8)</td><td>(27.2)</td><td>(28.5)</td></tr><tr><td>Technology &amp; comm. exp.</td><td>(20.8)</td><td>(22.6)</td><td>(23.3)</td><td>(24.4)</td></tr><tr><td>Depreciation &amp; amortization</td><td>(18.0)</td><td>(19.1)</td><td>(19.5)</td><td>(19.9)</td></tr><tr><td>Occupancy expense</td><td>(1.0)</td><td>(0.9)</td><td>(0.9)</td><td>(0.9)</td></tr><tr><td>Other costs</td><td>(19.4)</td><td>(32.3)</td><td>(39.8)</td><td>(42.2)</td></tr><tr><td>Total operating expense</td><td>(46.2)</td><td>(49.3)</td><td>(51.4)</td><td>(53.9)</td></tr><tr><td>Inv. inc. &amp; other (non-op.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Profit/(loss) on disposals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total other net</td><td>2.1</td><td>2.9</td><td>3.0</td><td>3.2</td></tr><tr><td>Pre-tax profit</td><td>117.2</td><td>145.8</td><td>140.9</td><td>151.7</td></tr><tr><td>Provision for taxes</td><td>(35.5)</td><td>(43.4)</td><td>(42.0)</td><td>(45.2)</td></tr><tr><td>Tax rate (%)</td><td>30.3</td><td>29.8</td><td>29.8</td><td>29.8</td></tr><tr><td>Minorities, pref div &amp; others</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>79.1</td><td>100.1</td><td>96.6</td><td>104.2</td></tr><tr><td>GS net income</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>GS EPS (¥)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>DPS (¥)</td><td>60.9</td><td>75.9</td><td>65.9</td><td>70.0</td></tr><tr><td>Div. payout ratio (%)</td><td>78.9</td><td>77.4</td><td>69.2</td><td>67.8</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>1,030.3</td><td>1,020.1</td><td>1,013.8</td><td>1,009.2</td></tr></table>

<table><tr><td colspan="5">Balance Sheet (¥ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>274.5</td><td>245.7</td><td>254.9</td><td>287.3</td></tr><tr><td>Restricted cash</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Investments</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Accounts receivable</td><td>24.7</td><td>25.0</td><td>26.0</td><td>27.4</td></tr><tr><td>Other current assets</td><td>71,121.9</td><td>71,744.0</td><td>73,895.3</td><td>77,425.1</td></tr><tr><td>Total current assets</td><td>71,421.1</td><td>72,014.8</td><td>74,176.2</td><td>77,739.8</td></tr><tr><td>Net PP&amp;E</td><td>12.3</td><td>14.9</td><td>17.5</td><td>20.1</td></tr><tr><td>Intangible assets</td><td>30.3</td><td>30.3</td><td>30.3</td><td>30.3</td></tr><tr><td>Goodwill, net book value</td><td>69.4</td><td>65.9</td><td>62.5</td><td>59.0</td></tr><tr><td>Other long-term assets</td><td>66.6</td><td>67.0</td><td>68.0</td><td>69.7</td></tr><tr><td>Total assets</td><td>71,599.6</td><td>72,192.9</td><td>74,354.5</td><td>77,918.9</td></tr><tr><td>Accounts payable</td><td>8.7</td><td>8.7</td><td>8.7</td><td>8.7</td></tr><tr><td>Income tax payable</td><td>23.4</td><td>19.7</td><td>20.3</td><td>21.7</td></tr><tr><td>Short-term debt</td><td>52.5</td><td>52.5</td><td>52.5</td><td>52.5</td></tr><tr><td>Other current liabilities</td><td>71,145.5</td><td>71,740.0</td><td>73,891.1</td><td>77,420.6</td></tr><tr><td>Total current liabilities</td><td>71,230.0</td><td>71,820.8</td><td>73,972.6</td><td>77,503.5</td></tr><tr><td>Deferred revenue</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Long-term debt</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term liabilities</td><td>11.8</td><td>11.8</td><td>11.8</td><td>11.8</td></tr><tr><td>Total liabilities</td><td>71,242.0</td><td>71,832.6</td><td>73,984.4</td><td>77,515.3</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>345.0</td><td>347.7</td><td>357.5</td><td>391.0</td></tr><tr><td>Minority interest</td><td>12.6</td><td>12.6</td><td>12.6</td><td>12.6</td></tr><tr><td>Total shareholders&#x27; equity</td><td>357.6</td><td>360.3</td><td>370.1</td><td>403.6</td></tr><tr><td>Total liabilities &amp; equity</td><td>71,599.6</td><td>72,192.9</td><td>74,354.5</td><td>77,918.9</td></tr></table>

Source: Company data, GS estimates.

September in recent years), a higher dividend to maintain the dividend payout ratio (we raise our FY3/27 DPS forecast from ¥57 to ¥76), the BOJ rate hike outlook (we estimate that collateral management income accounts for 6-10% of the bottom line), and derivative product growth and inorganic growth in the medium to long term. Downside risks include declines in stock market capitalization and turnover.

## Our estimates/target price

Reflecting trading value trends, FY3/27 guidance, and our economists' BOJ policy rate hike outlook, we raise our FY3/27-FY3/29 net profit estimates by 27%/11%/12%. Our 12-month target price of ¥2,400 (+23% vs. previous TP of ¥1,950) is based on a 12-month forward P/E (past 5-year average) of 25.19X and our FY3/28 EPS estimate of ¥95.3. We maintain our Buy rating.

Exhibit 1: Japan Exchange Group: Our new vs. old estimates

<table><tr><td></td><td>FY25</td><td>FY26E</td><td colspan="2">FY26E</td><td colspan="2">FY27E</td><td colspan="2">FY28E</td><td></td><td colspan="4">Chg (%)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td colspan="2">3/27E</td><td colspan="2">3/28E</td><td colspan="2">3/29E</td><td></td><td>FY25</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>(JPY bn)</td><td>Actual</td><td>CoE</td><td>Prior</td><td>Revised</td><td>Prior</td><td>Revised</td><td>Prior</td><td>Revised</td><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Trading fees</td><td>77.3</td><td></td><td>74.1</td><td>95.1</td><td>78.0</td><td>91.1</td><td>82.6</td><td>97.5</td><td></td><td>7%</td><td>28%</td><td>17%</td><td>18%</td></tr><tr><td>of which: cash equity</td><td>55.3</td><td></td><td>51.5</td><td>70.9</td><td>54.2</td><td>66.1</td><td>57.5</td><td>71.7</td><td></td><td>9%</td><td>38%</td><td>22%</td><td>25%</td></tr><tr><td>of which: derivatives</td><td>10.6</td><td></td><td>11.3</td><td>12.8</td><td>12.5</td><td>13.6</td><td>13.8</td><td>14.2</td><td></td><td>4%</td><td>13%</td><td>8%</td><td>3%</td></tr><tr><td>of which: other access</td><td>11.5</td><td></td><td>11.2</td><td>11.4</td><td>11.3</td><td>11.5</td><td>11.4</td><td>11.5</td><td></td><td>2%</td><td>1%</td><td>1%</td><td>1%</td></tr><tr><td>Income from securities settlement</td><td>54.2</td><td></td><td>61.9</td><td>77.3</td><td>75.1</td><td>83.5</td><td>79.8</td><td>90.1</td><td></td><td>7%</td><td>25%</td><td>11%</td><td>13%</td></tr><tr><td>Listing fees</td><td>18.7</td><td></td><td>19.5</td><td>20.0</td><td>20.2</td><td>20.8</td><td>20.9</td><td>21.5</td><td></td><td>3%</td><td>3%</td><td>3%</td><td>3%</td></tr><tr><td>Information income</td><td>33.7</td><td></td><td>34.4</td><td>35.4</td><td>36.2</td><td>36.6</td><td>38.3</td><td>38.0</td><td></td><td>2%</td><td>3%</td><td>1%</td><td>-1%</td></tr><tr><td>Other income</td><td>14.8</td><td></td><td>15.7</td><td>15.7</td><td>16.5</td><td>16.5</td><td>17.3</td><td>17.3</td><td></td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Total revenue</td><td>198.7</td><td>205.0</td><td>205.6</td><td>243.6</td><td>226.0</td><td>248.5</td><td>239.0</td><td>264.5</td><td></td><td>5%</td><td>18%</td><td>10%</td><td>11%</td></tr><tr><td>Transaction revenue</td><td>131.5</td><td></td><td>135.9</td><td>172.5</td><td>153.1</td><td>174.6</td><td>162.4</td><td>187.6</td><td></td><td>7%</td><td>27%</td><td>14%</td><td>16%</td></tr><tr><td>Non-transaction revenue</td><td>67.2</td><td></td><td>69.6</td><td>71.1</td><td>72.9</td><td>73.9</td><td>76.6</td><td>76.9</td><td></td><td>2%</td><td>2%</td><td>1%</td><td>0%</td></tr><tr><td>Other expenses</td><td>44.7</td><td></td><td>50.4</td><td>59.0</td><td>57.4</td><td>67.9</td><td>59.7</td><td>71.6</td><td></td><td>3%</td><td>17%</td><td>18%</td><td>20%</td></tr><tr><td>Other expenses (incl. cost of system development)</td><td>44.7</td><td></td><td>50.4</td><td>59.0</td><td>57.4</td><td>67.9</td><td>59.7</td><td>71.6</td><td></td><td>3%</td><td>17%</td><td>18%</td><td>20%</td></tr><tr><td>Total operating expenses</td><td>83.6</td><td>91.0</td><td>91.4</td><td>100.7</td><td>99.8</td><td>110.7</td><td>103.8</td><td>116.0</td><td></td><td>1%</td><td>10%</td><td>11%</td><td>12%</td></tr><tr><td>Systems expense</td><td>38.9</td><td></td><td>41.0</td><td>41.7</td><td>42.4</td><td>42.8</td><td>44.0</td><td>44.3</td><td></td><td>-1%</td><td>2%</td><td>1%</td><td>1%</td></tr><tr><td>Non-systems expense</td><td>44.7</td><td></td><td>50.4</td><td>59.0</td><td>57.4</td><td>67.9</td><td>59.8</td><td>71.7</td><td></td><td>3%</td><td>17%</td><td>18%</td><td>20%</td></tr><tr><td>Operating profit</td><td>115.1</td><td>115.0</td><td>114.2</td><td>142.9</td><td>126.2</td><td>137.8</td><td>135.2</td><td>148.5</td><td></td><td>9%</td><td>25%</td><td>9%</td><td>10%</td></tr><tr><td>Net non operating income</td><td>2.1</td><td></td><td>2.1</td><td>2.9</td><td>2.2</td><td>3.0</td><td>2.3</td><td>3.2</td><td></td><td>11%</td><td>41%</td><td>41%</td><td>41%</td></tr><tr><td>Ordinary income</td><td>117.2</td><td></td><td>116.3</td><td>145.8</td><td>128.3</td><td>140.9</td><td>137.4</td><td>151.7</td><td></td><td>9%</td><td>25%</td><td>10%</td><td>10%</td></tr><tr><td>Extraordinary gain / (loss)</td><td>-0.3</td><td></td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><t

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
