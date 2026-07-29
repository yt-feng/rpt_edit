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
# Huaming Power Equipment | Asia Pacific Priced for Fear, Built for Growth

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Huaming Power Equipment (002270.SZ)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb34.50</td><td>Rmb26.40</td></tr></table>

We believe the market has been overly concerned about competition and under-appreciates Huaming's long-term growth. We reiterate OW after valuation reset and expect better-than-feared results to be a positive catalyst.

Huaming's share price has corrected by as much as 54% from the historical peak in early 2026 amid market concerns including a major competitor's capacity ramp-up, slower-than-expected US market development, and disappointing 1Q26 results. However, we hold a different view and view current valuation of 19x 2027E P/E as attractive vs. global peers' average valuation of 30x. We cut our 2026-28 net profit estimates by 5-10% to reflect more conservative growth seen for non-grid domestic revenue, a higher SG&A expense ratio due to share incentives, and FX losses on Rmb appreciation. We lower our P/E-based PT to Rmb26.40 (from Rmb34.50) based on 25x one-year forward P/E (previously 30.5x).

What does MR's capacity expansion really mean? Maschinenfabrik Reinhausen (MR), Huaming's key competitor with 50% global market share, plans to double production capacity by 2028-30. The market believes this will intensify competition, but we think it may also indicate unexpected TAM expansion, for which we see some clues from the recent EU Electricification Action Plan. EU targets an electrification rate of 46% by 2040, compared to a stagnant 23% over the past decade. This should come with more renewable and EV adoption, making installation of low-to-medium voltage tap changers in the distribution networks more imminent to secure grid stability, and thus creating a greater TAM than the current >35kV tap changer market.

Has Huaming changed its overseas strategy? We reiterate our bullish view on Huaming's overseas expansion, which is not driven by shortages but rather cost attractiveness and customers' improved willingness to diversify the supply chain, especially against a backdrop of China's transformer exports. US business development is subject to product testing, which we view as a catalyst for 4Q26. We expect Huaming's power equipment export revenue to increase at a \~30% CAGR over 2025-29, bringing overseas revenue contribution to 54% in 2029 (vs. 34% in 2025).

Earnings growth set to re-accelerate from 2027: After our estimate revisions, we see 11% net profit growth in 2026, largely in line with sell-side consensus but above buy-side expectations as some investors expect no growth or a slight decline in 1H26. Beyond 2026, we believe earnings growth can return to 18-20% pa, with an improving product mix and alleviated drag from FX losses and share incentive expenses.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Tom Li</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tom.Li1@morganstanley.com</td><td>+852 2239-1059</td></tr><tr><td colspan="2">Eva Hou</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Eva.Hou@morganstanley.com</td><td>+852 2848-6964</td></tr></table>

## Asia Summer School 2026

![](images/db70f6720ccde7ff9bcf54838d0155d70b056b580b99ef2d0305199ed94df896.jpg)

## Huaming Power Equipment (002270.SZ, 002270 CS)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>Rmb26.40</td></tr><tr><td>Up/downside to price target (%)</td><td>33</td></tr><tr><td>Shr price, close (Jul 27, 2026)</td><td>Rmb19.86</td></tr><tr><td>52-Week Range</td><td>Rmb38.01-17.23</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>896</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb17,799.0</td></tr><tr><td>EV, curr (mn)</td><td>Rmb17,239.6</td></tr><tr><td>Avg daily trading value (mn)</td><td>Rmb411</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>0.8</td><td>0.9</td><td>1.0</td><td>1.2</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>0.9</td><td>1.1</td><td>1.4</td></tr><tr><td>EPS (Rmb)§</td><td>0.8</td><td>0.9</td><td>1.1</td><td>1.3</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>2,426.8</td><td>2,697.6</td><td>3,088.4</td><td>3,524.8</td></tr><tr><td>EBITDA (Rmb mn)</td><td>847.5</td><td>938.2</td><td>1,106.1</td><td>1,298.2</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>709.7</td><td>785.3</td><td>938.9</td><td>1,110.4</td></tr><tr><td>P/E</td><td>31.7</td><td>22.7</td><td>19.0</td><td>16.0</td></tr><tr><td>P/BV</td><td>7.1</td><td>5.3</td><td>4.8</td><td>4.4</td></tr><tr><td>RNOA (%)</td><td>29.4</td><td>28.2</td><td>28.0</td><td>31.2</td></tr><tr><td>ROE (%)</td><td>22.4</td><td>25.0</td><td>27.8</td><td>30.1</td></tr><tr><td>EV/EBITDA</td><td>25.8</td><td>18.7</td><td>15.8</td><td>13.3</td></tr><tr><td>Div yld (%)</td><td>2.2</td><td>3.1</td><td>3.5</td><td>4.2</td></tr><tr><td>FCF yld ratio (%)**</td><td>2.1</td><td>3.5</td><td>4.0</td><td>4.8</td></tr><tr><td>Leverage (EOP) (%)</td><td>(27.5)</td><td>(17.2)</td><td>(19.1)</td><td>(21.1)</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
§ = Consensus data is provided by Refinitiv Estimates
\*\* = Based on consensus methodology
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

AlphaSignals Earnings Preview

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Huaming Power Equipment 002270.SZ</td></tr><tr><td>Tap Changer Export Revenue</td><td>↑ Likely upside surprise</td><td>↑ Modest revision higher</td></tr><tr><td colspan="3">*Likely impact to consensus EPS is for the next 12 monthsSource: Company data, MS</td></tr></table>

Balance sheet

## Financial Summary

Exhibit 1: Financial Summary

<table><tr><td>Rmb mn</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>2,427</td><td>2,698</td><td>3,088</td><td>3,525</td></tr><tr><td>COGS</td><td>(1,104)</td><td>(1,209)</td><td>(1,349)</td><td>(1,501)</td></tr><tr><td>Gross profit</td><td>1,322</td><td>1,488</td><td>1,740</td><td>2,023</td></tr><tr><td>Business Tax and Surcharges</td><td>(32)</td><td>(36)</td><td>(41)</td><td>(47)</td></tr><tr><td>Selling Expenses</td><td>(252)</td><td>(243)</td><td>(263)</td><td>(282)</td></tr><tr><td>Admin Expenses</td><td>(170)</td><td>(252)</td><td>(297)</td><td>(347)</td></tr><tr><td>R&amp;D Expenses</td><td>(88)</td><td>(98)</td><td>(113)</td><td>(129)</td></tr><tr><td>EBIT</td><td>781</td><td>859</td><td>1,027</td><td>1,219</td></tr><tr><td>Financial Costs</td><td>26</td><td>10</td><td>17</td><td>20</td></tr><tr><td>Non-Operating Income</td><td>47</td><td>76</td><td>86</td><td>96</td></tr><tr><td>Non-Operating Expenditure</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td></tr><tr><td>Profit before tax</td><td>848</td><td>939</td><td>1,122</td><td>1,327</td></tr><tr><td>Income tax</td><td>(129)</td><td>(142)</td><td>(170)</td><td>(201)</td></tr><tr><td>Profit for the year</td><td>720</td><td>796</td><td>952</td><td>1,126</td></tr><tr><td>Minorities</td><td>(10)</td><td>(11)</td><td>(13)</td><td>(15)</td></tr><tr><td>Net profit</td><td>710</td><td>785</td><td>939</td><td>1,110</td></tr><tr><td>One-off Items</td><td>39</td><td>50</td><td>58</td><td>66</td></tr><tr><td>Recurring Net profit</td><td>671</td><td>735</td><td>881</td><td>1,044</td></tr><tr><td>EPS</td><td>0.79</td><td>0.88</td><td>1.05</td><td>1.24</td></tr><tr><td>DPS</td><td>0.61</td><td>0.70</td><td>0.84</td><td>0.99</td></tr></table>

<table><tr><td>Rmb mn</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; equivalents</td><td>1,166</td><td>884</td><td>1,006</td><td>1,155</td></tr><tr><td>Accounts receivable &amp; contract asset</td><td>580</td><td>645</td><td>738</td><td>843</td></tr><tr><td>Other receivables</td><td>867</td><td>964</td><td>1,104</td><td>1,260</td></tr><tr><td>Inventory</td><td>387</td><td>424</td><td>473</td><td>526</td></tr><tr><td>Other current assets</td><td>274</td><td>268</td><td>261</td><td>254</td></tr><tr><td>Total current assets</td><td>3,274</td><td>3,185</td><td>3,583</td><td>4,038</td></tr><tr><td>Net tangible fixed assets</td><td>1,016</td><td>1,017</td><td>1,018</td><td>1,019</td></tr><tr><td>Other long term assets</td><td>918</td><td>927</td><td>938</td><td>952</td></tr><tr><td>Total non-current assets</td><td>1,935</td><td>1,945</td><td>1,957</td><td>1,971</td></tr><tr><td>Total assets</td><td>5,208</td><td>5,130</td><td>5,540</td><td>6,009</td></tr><tr><td>Short-term Loans</td><td>220</td><td>220</td><td>220</td><td>220</td></tr><tr><td>Accounts payable</td><td>221</td><td>242</td><td>270</td><td>301</td></tr><tr><td>Advance payment / contract liabilities</td><td>68</td><td>68</td><td>68</td><td>68</td></tr><tr><td>LT borrowing mature in 1 year</td><td>106</td><td>106</td><td>106</td><td>106</td></tr><tr><td>Other short term liabilities</td><td>466</td><td>510</td><td>568</td><td>631</td></tr><tr><td>Total current liabilities</td><td>1,081</td><td>1,146</td><td>1,232</td><td>1,326</td></tr><tr><td>Long term debt</td><td>393</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Long-term Accounts Payable</td><td>161</td><td>161</td><td>161</td><td>161</td></tr><tr><td>Other long term liabilities</td><td>401</td><td>401</td><td>401</td><td>401</td></tr><tr><td>Total non-current liabilities</td><td>955</td><td>562</td><td>562</td><td>562</td></tr><tr><td>Total liabilities</td><td>2,036</td><td>1,708</td><td>1,794</td><td>1,888</td></tr><tr><td>Minority interests</td><td>30</td><td>41</td><td>54</td><td>70</td></tr><tr><td>Paid-in Capital (or Share Capital)</td><td>227</td><td>227</td><td>227</td><td>227</td></tr><tr><td>Capital Reserve</td><td>1,083</td><td>1,083</td><td>1,083</td><td>1,083</td></tr><tr><td>Reserves &amp; Retained earnings</td><td>1,832</td><td>2,071</td><td>2,381</td><td>2,741</td></tr><tr><td>Shareholders&#x27; equity</td><td>3,142</td><td>3,381</td><td>3,692</td><td>4,051</td></tr><tr><td>Total equity</td><td>3,172</td><td>3,422</td><td>3,746</td><td>4,121</td></tr><tr><td>Total liabilities &amp; equity</td><td>5,208</td><td>5,130</td><td>5,540</td><td>6,009</td></tr></table>

Source: FactSet, company data, MS (E) estimates

<table><tr><td>Rmb mn</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Profit for the year</td><td>720</td><td>796</td><td>952</td><td>1,126</td></tr><tr><td>Adjustments for:</td><td></td><td></td><td></td><td></td></tr><tr><td>Depreciation</td><td>6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Amortization</td><td>67</td><td>79</td><td>79</td><td>79</td></tr><tr><td>Finance cost</td><td>19</td><td>(10)</td><td>(17)</td><td>(20)</td></tr><tr><td>Others</td><td>86</td><td>41</td><td>39</td><td>37</td></tr><tr><td>Changes in Working capital</td><td>(294)</td><td>(128)</td><td>(190)</td><td>(212)</td></tr><tr><td>Net cash flows from operating activities</td><td>604</td><td>778</td><td>863</td><td>1,009</td></tr><tr><td>CAPEX</td><td>(112)</td><td>(140)</td><td>(140)</td><td>(140)</td></tr><tr><td>Others</td><td>163</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Net cash flows from investing activities</td><td>51</td><td>(130)</td><td>(130)</td><td>(130)</td></tr><tr><td>Share issuance</td><td>0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Increase/(decrease) in debt</td><td>193</td><td>(393)</td><td>0</td><td>0</td></tr><tr><td>Dividends &amp; interest paid</td><td>(614)</td><td>(537)</td><td>(611)</td><td>(731)</td></tr><tr><td>Other cash from financing</td><td>(166)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net cash flows from financing activities</td><td>(587)</td><td>(929)</td><td>(611)</td><td>(731)</td></tr><tr><td>Effect of FX rate changes</td><td>(6)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net change in cash flow</td><td>62</td><td>(281)</td><td>122</td><td>148</td></tr><tr><td>Cash at the beginning</td><td>1,104</td><td>1,166</td><td>884</td><td>1,006</td></tr><tr><td>Cash restatement</td><td></td><td></td><td></td><td></td></tr><tr><td>Cash at the end</td><td>1,166</td><td>884</td><td>1,006</td><td>1,155</td></tr></table>

<table><tr><td colspan="5">Key ratios</td></tr><tr><td></td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="5">Growth</td></tr><tr><td>Revenue</td><td>4.5%</td><td>11.2%</td><td>14.5%</td><td>14.1%</td></tr><tr><td>Gross profit</td><td>16.7%</td><td>12.5%</td><td>16.9%</td><td>16.3%</td></tr><tr><td>EBIT</td><td>16.9%</td><td>10.1%</td><td>19.5%</td><td>18.7%</td></tr><tr><td>Net profit</td><td>15.5%</td><td>10.7%</td><td>19.6%</td><td>18.3%</td></tr><tr><td>Recurring Net profit</td><td>15.3%</td><td>9.6%</td><td>19.9%</td><td>18.5%</td></tr><tr><td colspan="5">Margin</td></tr><tr><td>Gross Margin</td><td>54.5%</td><td>55.2%</td><td>56.3%</td><td>57.4%</td></tr><tr><td>EBITDA</td><td>35.2%</td><td>34.8%</td><td>35.8%</td><td>36.8%</td></tr><tr><td>EBIT</td><td>32.2%</td><td>31.9%</td><td>33.3%</td><td>34.6%</td></tr><tr><td>Net profit</td><td>29.2%</td><td>29.1%</td><td>30.4%</td><td>31.5%</td></tr><tr><td>Net profit</td><td>27.6%</td><td>27.2%</td><td>28.5%</td><td>29.6%</td></tr><tr><td colspan="5">Return</td></tr><tr><td>ROA</td><td>12.9%</td><td>14.3%</td><td>15.9%</td><td>17.4%</td></tr><tr><td>ROAE</td><td>21.3%</td><td>22.5%</td><td>24.9%</td><td>27.0%</td></tr><tr><td>ROE</td><td>21.3%</td><td>21.7%</td><td>23.9%</td><td>25.8%</td></tr><tr><td colspan="5">Gearing</td></tr><tr><td>Net Debt (Net Cash) /Equity</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net Debt (Net Cash)/Capital</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>EBITDA Interest Coverage</td><td>(32.7)</td><td>(95.5)</td><td>(12.9)</td><td>(13.5)</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>EV/EBITDA</td><td>25.8</td><td>18.4</td><td>15.5</td><td>13.1</td></tr><tr><td>P/E</td><td>31.7</td><td>22.7</td><td>19.0</td><td>16.0</td></tr><tr><td>P/BV</td><td>7.1</td><td>5.3</td><td>4.8</td><td>4.4</td></tr><tr><td>Dividend Yield</td><td>2.4%</td><td>3.5%</td><td>4.2%</td><td>5.0%</td></tr></table>

## Estimate and PT changes

We lower our 2026-28 revenue forecasts by 2-6%, mainly to factor in more conservative growth in non-grid domestic revenue, including industrial and renewables given weak FAI growth and a high base of renewable installations in 2025. We also assume a higher SG&A expense ratio due to share incentives and more FX losses on Rmb appreciation, leading 5-10% cuts to our net profit estimates for the period.

We are now 4% below sell-side consensus net profit forecasts for 2026-28 but likely still well above buy-side expectations. Based on recent conversations, some most bearish investors are expecting slight declines in net profit in 1H26 and 2Q26. With 2Q25 representing a low base and pent-up demand from 1Q26 for delivery catch-up, we believe 2Q26 earnings growth is likely to be be

[中间内容因长度限制已省略]

 of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Utilities

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/27/2026)</td></tr><tr><td colspan="3">Eva Hou</td></tr><tr><td>CGN Power Co., Ltd (1816.HK)</td><td>E (03/21/2026)</td><td>HK$2.86</td></tr><tr><td>CGN Power Co., Ltd (003816.SZ)</td><td>U (03/29/2021)</td><td>Rmb4.03</td></tr><tr><td>China Longyuan Power Group (0916.HK)</td><td>E (01/20/2026)</td><td>HK$5.74</td></tr><tr><td>China Longyuan Power Group (001289.SZ)</td><td>E (08/06/2024)</td><td>Rmb16.42</td></tr><tr><td>China Resources Power (0836.HK)</td><td>E (03/21/2026)</td><td>HK$18.98</td></tr><tr><td>China Yangtze Power Co. (600900.SS)</td><td>O (11/14/2023)</td><td>Rmb28.35</td></tr><tr><td>Dajin Heavy Industry (002487.SZ)</td><td>O (04/18/2026)</td><td>Rmb40.54</td></tr><tr><td>Goldwind (002202.SZ)</td><td>U (01/20/2026)</td><td>Rmb18.15</td></tr><tr><td>Goldwind (2208.HK)</td><td>E (08/17/2022)</td><td>HK$9.94</td></tr><tr><td>Hangzhou First Applied Material Co. Ltd (603806.SS)</td><td>O (01/18/2023)</td><td>Rmb14.10</td></tr><tr><td>Henan Pinggao Electric (600312.SS)</td><td>O (01/18/2024)</td><td>Rmb19.10</td></tr><tr><td>Huaneng Power International Inc. (0902.HK)</td><td>E (06/30/2022)</td><td>HK$5.93</td></tr><tr><td>Huaneng Power International Inc. (600011.SS)</td><td>U (04/07/2021)</td><td>Rmb7.14</td></tr><tr><td>JA Solar Technology Co Ltd (002459.SZ)</td><td>E (09/02/2025)</td><td>Rmb7.22</td></tr><tr><td>Jiangsu Zhongtian Technology Co. Ltd. (600522.SS)</td><td>O (10/12/2020)</td><td>Rmb32.66</td></tr><tr><td>LONGi Green Energy Technology Co Ltd (601012.SS)</td><td>U (09/02/2025)</td><td>Rmb12.64</td></tr><tr><td>NARI Technology (600406.SS)</td><td>O (11/01/2015)</td><td>Rmb23.90</td></tr><tr><td>Ningbo Orient Wires &amp; Cables Co Ltd (603606.SS)</td><td>O (08/17/2022)</td><td>Rmb39.06</td></tr><tr><td>Riyue Heavy Industry Co., Ltd. (603218.SS)</td><td>O (02/11/2025)</td><td>Rmb9.58</td></tr><tr><td>Shanghai Electric (2727.HK)</td><td>U (03/26/2021)</td><td>HK$3.24</td></tr><tr><td>Shanghai Electric (601727.SS)</td><td>U (03/26/2021)</td><td>Rmb6.60</td></tr><tr><td>Sieyuan Electric Co.Ltd. (002028.SZ)</td><td>O (07/01/2025)</td><td>Rmb168.30</td></tr><tr><td>Sinoma Science &amp; Technology Co. Ltd. (002080.SZ)</td><td>O (09/23/2025)</td><td>Rmb51.94</td></tr><tr><td>Sungrow Power Supply Co. Ltd (300274.SZ)</td><td>O (06/09/2026)</td><td>Rmb116.21</td></tr><tr><td>Tongwei Co. Ltd. (600438.SS)</td><td>E (09/02/2025)</td><td>Rmb11.17</td></tr><tr><td>XJ Electric (000400.SZ)</td><td>E (03/21/2026)</td><td>Rmb22.30</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>Xinyi Solar Holdings Ltd (0968.HK)</td><td>O (07/30/2020)</td><td>HK$2.15</td></tr></table>

Tom Li

<table><tr><td>Anhui Yingliu Electromechanical Co Ltd (603308.SS)</td><td>O (04/08/2026)</td><td>Rmb47.02</td></tr><tr><td>China Gas Holdings (0384.HK)</td><td>E (07/10/2026)</td><td>HK$5.85</td></tr><tr><td>China Resources Gas (1193.HK)</td><td>E (07/10/2026)</td><td>HK$16.08</td></tr><tr><td>Huaming Power Equipment (002270.SZ)</td><td>O (04/08/2026)</td><td>Rmb19.86</td></tr><tr><td>Ningbo Sanxing Medical Electric Co. Ltd. (601567.SS)</td><td>O (04/08/2026)</td><td>Rmb15.13</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
