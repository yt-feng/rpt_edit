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
# Anta Sports Products (2020.HK)

# 2Q26 retail sales broadly in-line; 1H26 modestly ahead of the full-year guidance; Buy

2020.HK 12m Price Target: HK\$108.00 Price: HK\$74.15 Upside: 45.7%

Anta Sports reported healthy 2Q26 sell-through results, tracking largely in-line with market expectation and our conversation with mgmt, though we believe Fila's 1H26 MSD growth is slightly below market's expectation of HSD while Kolon's strong growth should provide upside to overall other brands' growth. Although Anta brand/Fila/Other brands retail sales decelerated to +LSD%/+LSD%/+25-30% in 2Q26 (or +MSD%/+MSD%, but close to HSD%/+35-40% yoy in 1H26) mainly due to seasonality and the industry-wise headwinds we observed, including later CNY, unfavorable weather conditions and softer macro demand, etc. Yet, Anta continued to outperform peers, with Xtep/ Li Ning adult+kids /Pou Sheng/ Topsports reporting -MSD%/flat/ -3%/-low-teens% yoy decline in 2Q26. Mgmt remained confident to achieve and maintain the full year guidance (>+LSD%/+MSD%/>20% retail sales growth for Anta brand/Fila/other brands) considering demand uncertainty and weather volatility, despite an easier comparison base in 2H26 and a favorable Mid-Autumn Festival calendar shift in 3Q26.

More specifically, 1) Anta brand growth in 2Q26 was led by online channel of low-DD% yoy growth following product and channel strategy optimization initiated from 3Q25, though online discount was deepened by c.2pp due to the longer 618 shopping festival. Offline retail sales declined with stable yoy discount. On the recent mgmt change decision, the company emphasized that recent management changes will not affect the brand's long-term strategy or operating direction. 2) Fila growth was also led by online channel of low-DD% yoy growth with stable discount yoy, though dragged by offline channel decline with c.1pp deepened discount. 3) Descente recorded +20% yoy growth in 2Q26 (or +25-30% in 1H26) with stable and disciplined discount, as well as healthy inventory level. Management attributed the strong performance to resilient spending by high-income consumers and continued product appeal. To broaden its customer base, the brand is expanding into footwear,

## BUY

Michelle Cheng
+852-2978-6631 | michelle.cheng@gs.com
GS (Asia) L.L.C.

Molly Dai
+852-3966-4000 | molly.dai@gs.com
GS (Asia) L.L.C.

Keira Liu
+852-2978-0473 | keira.liu@gs.com
GS (Asia) L.L.C.

## Key Data

Market cap: HK\$207.4bn / \$26.5bn
Enterprise value: HK\$249.0bn / \$31.8bn
3m ADTV: HK\$564.6mn / \$72.1mn
China
Greater China Retail
M&A Rank: 3
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn) New</td><td>80,219.0</td><td>88,352.1</td><td>95,068.3</td><td>101,761.3</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>80,219.0</td><td>87,373.3</td><td>94,350.1</td><td>101,273.0</td></tr><tr><td>EBITDA (Rmb mn)</td><td>22,427.0</td><td>24,799.9</td><td>27,858.3</td><td>30,311.4</td></tr><tr><td>EPS (Rmb) New</td><td>4.89</td><td>5.15</td><td>5.93</td><td>6.58</td></tr><tr><td>EPS (Rmb) Old</td><td>4.89</td><td>5.11</td><td>5.93</td><td>6.58</td></tr><tr><td>P/E (X)</td><td>16.7</td><td>12.4</td><td>10.8</td><td>9.7</td></tr><tr><td>P/B (X)</td><td>3.5</td><td>2.5</td><td>2.2</td><td>2.0</td></tr><tr><td>Dividend yield (%)</td><td>2.7</td><td>3.2</td><td>3.6</td><td>4.0</td></tr><tr><td>CROCI (%)</td><td>18.1</td><td>17.3</td><td>31.1</td><td>40.9</td></tr><tr><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>2.53</td><td>2.36</td><td>2.69</td><td>2.46</td></tr></table>

GS Factor Profile

![](images/f225d3b2e825cefdd3bbd1235687e90f3c8abf4ebe8345ab728b9fffd9bbcf2c.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Anta Sports Products (2020.HK) Rating since Jun 27, 2019

BUY

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>16.7</td><td>12.4</td><td>10.8</td><td>9.7</td></tr><tr><td>P/B (X)</td><td>3.5</td><td>2.5</td><td>2.2</td><td>2.0</td></tr><tr><td>FCF yield (%)</td><td>5.8</td><td>8.6</td><td>8.9</td><td>10.1</td></tr><tr><td>EV/EBITDAR (X)</td><td>11.6</td><td>8.7</td><td>6.1</td><td>5.4</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>14.6</td><td>10.7</td><td>7.3</td><td>6.3</td></tr><tr><td>CROCI (%)</td><td>18.1</td><td>17.3</td><td>31.1</td><td>40.9</td></tr><tr><td>ROE (%)</td><td>21.3</td><td>20.8</td><td>21.6</td><td>21.5</td></tr><tr><td>Net debt/equity (%)</td><td>(7.4)</td><td>(15.2)</td><td>(22.0)</td><td>(28.4)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(19.1)</td><td>(26.9)</td><td>(33.1)</td><td>(39.0)</td></tr><tr><td>Interest cover (X)</td><td>31.6</td><td>55.8</td><td>64.2</td><td>70.5</td></tr><tr><td>Days inventory outst, sales</td><td>52.1</td><td>50.7</td><td>49.6</td><td>48.9</td></tr><tr><td>Receivable days</td><td>20.7</td><td>20.0</td><td>20.3</td><td>20.3</td></tr><tr><td>Days payable outstanding</td><td>50.8</td><td>47.6</td><td>48.5</td><td>48.4</td></tr><tr><td>DuPont ROE (%)</td><td>18.8</td><td>17.6</td><td>17.8</td><td>17.5</td></tr><tr><td>Turnover (X)</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.6</td></tr><tr><td>Leverage (X)</td><td>1.7</td><td>1.7</td><td>1.6</td><td>1.6</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>86,875.0</td><td>98,651.3</td><td>64,019.4</td><td>68,748.9</td></tr><tr><td>Average capital employed (Rmb)</td><td>57,800.0</td><td>59,025.6</td><td>60,679.0</td><td>62,859.8</td></tr><tr><td>BVPS (Rmb)</td><td>23.52</td><td>25.80</td><td>28.79</td><td>32.01</td></tr></table>

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>80,219.0</td><td>88,352.1</td><td>95,068.3</td><td>101,761.3</td></tr><tr><td>Cost of goods sold</td><td>(30,485.0)</td><td>(33,463.2)</td><td>(35,344.7)</td><td>(37,431.2)</td></tr><tr><td>SG&amp;A</td><td>(31,444.0)</td><td>(34,719.8)</td><td>(36,740.8)</td><td>(39,167.5)</td></tr><tr><td>R&amp;D</td><td>(2,198.0)</td><td>(2,394.3)</td><td>(2,576.4)</td><td>(2,757.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>22,427.0</td><td>24,799.9</td><td>27,858.3</td><td>30,311.4</td></tr><tr><td>Depreciation &amp; amortization</td><td>(6,335.0)</td><td>(7,025.2)</td><td>(7,451.8)</td><td>(7,906.5)</td></tr><tr><td>EBIT</td><td>16,092.0</td><td>17,774.8</td><td>20,406.5</td><td>22,404.8</td></tr><tr><td>Net interest inc./(exp.)</td><td>897.0</td><td>427.6</td><td>411.9</td><td>600.4</td></tr><tr><td>Income/(loss) from associates</td><td>1,203.0</td><td>1,762.4</td><td>2,397.2</td><td>2,867.1</td></tr><tr><td>Pre-tax profit</td><td>21,446.0</td><td>22,941.1</td><td>26,138.7</td><td>28,785.8</td></tr><tr><td>Provision for taxes</td><td>(5,784.0)</td><td>(6,051.4)</td><td>(6,783.6)</td><td>(7,405.7)</td></tr><tr><td>Minority interest</td><td>(2,074.0)</td><td>(2,557.6)</td><td>(2,855.1)</td><td>(3,080.9)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>13,588.0</td><td>14,332.1</td><td>16,500.1</td><td>18,299.2</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>13,588.0</td><td>14,332.1</td><td>16,500.1</td><td>18,299.2</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>4.89</td><td>5.15</td><td>5.93</td><td>6.58</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>4.68</td><td>4.94</td><td>5.68</td><td>6.30</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>4.89</td><td>5.15</td><td>5.93</td><td>6.58</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>4.68</td><td>4.94</td><td>5.68</td><td>6.30</td></tr><tr><td>DPS (Rmb)</td><td>2.23</td><td>2.06</td><td>2.31</td><td>2.53</td></tr><tr><td>Div. payout ratio (%)</td><td>45.6</td><td>40.0</td><td>39.0</td><td>38.5</td></tr></table>

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>13.3</td><td>10.1</td><td>7.6</td><td>7.0</td></tr><tr><td>EBITDA growth</td><td>14.1</td><td>10.6</td><td>12.3</td><td>8.8</td></tr><tr><td>EPS growth</td><td>(12.0)</td><td>5.5</td><td>15.1</td><td>10.9</td></tr><tr><td>DPS growth</td><td>2.1</td><td>(7.5)</td><td>12.2</td><td>9.4</td></tr><tr><td>EBIT margin</td><td>20.1</td><td>20.1</td><td>21.5</td><td>22.0</td></tr><tr><td>EBITDA margin</td><td>28.0</td><td>28.1</td><td>29.3</td><td>29.8</td></tr><tr><td>Net income margin</td><td>16.9</td><td>16.2</td><td>17.4</td><td>18.0</td></tr></table>

Price Performance  
![](images/70471845f241197b69a63b01a3c179cf75b9ae253bfe5c4ed4118f7d38511089.jpg)  
Source: FactSet. Price as of 17 Jul 2026 close.

Balance Sheet (Rmb mn)

<table><tr><td colspan="5">Balance Sheet (Kmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>37,115.0</td><td>45,176.2</td><td>53,960.0</td><td>64,117.1</td></tr><tr><td>Accounts receivable</td><td>4,616.0</td><td>5,084.0</td><td>5,470.5</td><td>5,855.6</td></tr><tr><td>Inventory</td><td>12,152.0</td><td>12,381.4</td><td>13,431.0</td><td>13,849.6</td></tr><tr><td>Other current assets</td><td>5,773.0</td><td>5,773.0</td><td>5,773.0</td><td>5,773.0</td></tr><tr><td>Total current assets</td><td>59,656.0</td><td>68,414.6</td><td>78,634.4</td><td>89,595.3</td></tr><tr><td>Net PP&amp;E</td><td>18,824.0</td><td>20,250.9</td><td>21,262.7</td><td>21,930.7</td></tr><tr><td>Net intangibles</td><td>5,095.0</td><td>4,918.0</td><td>4,741.0</td><td>4,564.0</td></tr><tr><td>Total investments</td><td>20,881.0</td><td>22,643.4</td><td>25,040.6</td><td>27,907.7</td></tr><tr><td>Other long-term assets</td><td>19,839.0</td><td>19,839.0</td><td>19,839.0</td><td>19,839.0</td></tr><tr><td>Total assets</td><td>124,295.0</td><td>136,065.8</td><td>149,517.7</td><td>163,836.6</td></tr><tr><td>Accounts payable</td><td>4,158.0</td><td>4,564.2</td><td>4,820.8</td><td>5,105.4</td></tr><tr><td>Short-term debt</td><td>11,532.0</td><td>11,532.0</td><td>11,532.0</td><td>11,532.0</td></tr><tr><td>Short-term lease liabilities</td><td>3,687.0</td><td>4,030.8</td><td>4,301.2</td><td>4,567.4</td></tr><tr><td>Other current liabilities</td><td>13,981.0</td><td>15,398.5</td><td>16,569.0</td><td>17,735.5</td></tr><tr><td>Total current liabilities</td><td>33,358.0</td><td>35,525.5</td><td>37,223.1</td><td>38,940.3</td></tr><tr><td>Long-term debt</td><td>11,770.0</td><td>11,770.0</td><td>11,770.0</td><td>11,770.0</td></tr><tr><td>Long-term lease liabilities</td><td>4,775.0</td><td>5,450.0</td><td>5,980.9</td><td>6,503.5</td></tr><tr><td>Other long-term liabilities</td><td>1,987.0</td><td>1,987.0</td><td>1,987.0</td><td>1,987.0</td></tr><tr><td>Total long-term liabilities</td><td>18,532.0</td><td>19,207.0</td><td>19,737.9</td><td>20,260.5</td></tr><tr><td>Total liabilities</td><td>51,890.0</td><td>54,732.5</td><td>56,961.0</td><td>59,200.8</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>65,782.0</td><td>72,152.7</td><td>80,521.1</td><td>89,519.3</td></tr><tr><td>Minority interest</td><td>6,623.0</td><td>9,180.6</td><td>12,035.7</td><td>15,116.6</td></tr><tr><td>Total liabilities &amp; equity</td><td>124,295.0</td><td>136,065.8</td><td>149,517.7</td><td>163,836.6</td></tr><tr><td>Net debt, adjusted</td><td>(13,813.0)</td><td>(21,874.2)</td><td>(30,658.0)</td><td>(40,815.1)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>13,588.0</td><td>14,332.1</td><td>16,500.1</td><td>18,299.2</td></tr><tr><td>D&amp;A add-back</td><td>6,335.0</td><td>7,025.2</td><td>7,451.8</td><td>7,906.5</td></tr><tr><td>Minority interest add-back</td><td>2,074.0</td><td>2,557.6</td><td>2,855.1</td><td>3,080.9</td></tr><tr><td>Net (inc)/dec working capital</td><td>230.0</td><td>(291.2)</td><td>(1,179.4)</td><td>(519.1)</td></tr><tr><td>Other operating cash flow</td><td>(1,231.0)</td><td>(344.9)</td><td>(1,226.7)</td><td>(1,700.6)</td></tr><tr><td>Cash flow from operations</td><td>20,996.0</td><td>23,278.8</td><td>24,400.8</td><td>27,066.9</td></tr><tr><td>Capital expenditures</td><td>(2,716.0)</td><td>(2,060.2)</td><td>(1,940.8)</td><td>(1,721.1)</td></tr><tr><td>Acquisitions</td><td>(2,218.0)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(2,112.0)</td><td>(1,762.4)</td><td>(2,397.2)</td><td>(2,867.1)</td></tr><tr><td>Cash flow from investing</td><td>(7,046.0)</td><td>(3,822.6)</td><td>(4,338.1)</td><td>(4,588.2)</td></tr><tr><td>Repayment of lease liabilities</td><td>(4,787.0)</td><td>(5,196.0)</td><td>(5,544.6)</td><td>(5,887.6)</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(6,585.0)</td><td>(6,199.0)</td><td>(5,734.4)</td><td>(6,433.9)</td></tr><tr><td>Inc/(dec) in debt</td><td>(1,359.0)</td><td>0.0</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>562.0</td><td>(5,196.0)</td><td>(5,544.6)</td><td>(5,887.6)</td></tr><tr><td>Cash flow from financing</td><td>(7,382.0)</td><td>(11,395.0)</td><td>(11,279.0)</td><td>(12,321.5)</td></tr><tr><td>Total cash flow</td><td>6,568.0</td><td>8,061.2</td><td>8,783.7</td><td>10,157.2</td></tr><tr><td>Free cash flow</td><td>13,493.0</td><td>16,022.6</td><td>16,915.4</td><td>19,458.1</td></tr></table>

Source: Company data, GS estimates.

women's categories and sub-brands, etc. In addition, expanding product portfolios will support higher store productivity, while aggressive store expansion is not the first priority. 4) For other brands, Kolon growth in 2Q26 remained solid at $+ > 40\%$ yoy with healthy discount and inventory level; MAIA saw offline growth outpace online growth for the first time, driven by successful new product launches; Jack Wolfskin brand's repositioning is faster than expected in China and on track in Europe. The brand plans to open several new stores with refreshed product assortments in cities in Northern China beginning in October 2026. Nevertheless, mgmt expects the brand to remain loss-making in 2026, and aims to be profitable in 2027 for China, followed by profitability for the global business in 2028; Management also noted that Puma acquisition process is on track.

All in all, we revised up Anta group's revenue upward by $<1.5\%$ and earnings upward by $<1\%$ in 2026-28E, reflecting solid growth at other brands including Descente and Kolon and disciplined OPEX control, though partly offset by slightly lower GPM given the mildly expanded discounts. Our 12-month target price and valuation methodology stay unchanged at HK\$108. Current valuation of c.13x 2026E P/E remain undemanding considering the group's proven ability to operate multi-brands and navigate cycles. Reiterate Buy on Anta group.

## Key operating updates & takeaways from the conference call Anta core brand:

2Q retail sales: Anta brand delivered +LSD% yoy growth (moderated vs. +HSD% in 1Q26), the sequential moderation was due to the timing shift of CNY, longer 618 promotional period and unfavorable weather. That said, mgmt highlighted healthy online performance during 618 promotion; By channel, adult offline/kids offline declined and online grew by +LDD% yoy in 2Q26 (vs+MSD%/+HSD%/+mid-teens% in 1Q26).

■ Discounts/Inventory: Anta offline discount was stable yoy yet online discount deepened by 2pp due to longer 

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
