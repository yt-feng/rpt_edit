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
# JPM

# Skyworks Solutions

Results and Guidance a Mixed Bag; Memory Headwinds Muted (For Now), Offset by Momentum in Broad Markets

SWKS reported solid Jun-Q results, with revenue/EPS beating consensus expectations, though the Sep-Q guide screens slightly sub-seasonal. Alongside the print, the company announced a broad reset of the QRVO merger and capital-returns cadence, with timing of the transaction pulled forward to “as early as” fiscal year-end, and the quarterly dividend eliminated (\~\$430M/yr, a \~5% yield) in favor of a new \$2B repurchase authorization (through Jan ‘29), which mgmt framed as repo-first, then deleveraging and accretive M&A. Our key takeaways: (1) The fall build is intact and Dec is largely locked, with mobile guided up high-teens% Q/Q and AAPL growing well above the blended mobile ramp. Book-to-bill is >1, channel inventories are lean, and history suggests any true demand reset for AAPL (if one comes) arrives as a CQ1 mix adjustment after Dec-Q sell-through, making Mar-Q (not Dec-Q) the memory test. (2) The content story improved as the content decline at AAPL is now tracking low-teens% vs. the 20-25% originally framed in Feb ‘25, driven by volume (customer units running +20-22% Y/Y in recent quarters) and favorable model mix rather than socket recapture (cyclical uplift), though it pairs with RF complexity increasing “for the first time in many years”. We would want evidence from the next down-selection cycle before underwriting a durable content inflection at a customer that is still \~57% of revenue. (3) Broad Markets’ optical deceleration (+8% Y/Y in Jun-Q, +5% guided) is a base effect plus consumer IoT absorbing the AI DC supply squeeze.(4) Gross margin is potentially capped until the annual pricing reset, as pressure from input cost inflation continues, and mobile pricing recapture rolls into FY27 negotiations, while BM pricing actions (above-corporate GM%) fold into the mix in the interim. Net, risk/reward screens balanced, in our view, against an undemanding valuation, but with CQ1 mix-adjustment still ahead, GM% ostensibly capped until the FY27 pricing reset, and FCF negative into a \~\$2B debt raise, we prefer to stay on the sidelines. We do continue to view the QRVO acquisition favorably (see note here), as it should drive scale and diversification benefits. We adjust our estimates and establish a Dec-27 PT of \$65 (from prior Dec-26 PT of \$70).

\- Jun-Q beats on healthy AAPL sell-through and strong US Android quarter. Jun-Q revenue came in at \$935M (-1% Q/Q, -3% Y/Y) vs. Street \~\$925M, with EPS of \$1.08 also ahead of Street (\$1.03). Mobile revenue (-2% Q/Q, -10% Y/Y) was supported by healthy AAPL sell-through (\~57% of total revenue, from \~60% in Mar-Q) and strong new-product ramps at SWKS' largest Android customer, which mgmt framed as an anomaly of that customer's launch timing, not repeating in Sep-Q, while Asia Android declines this quarter and next. Broad Markets grew +8% Y/Y (\~flat Q/Q), with Wi-Fi/DC/autos (\~2/3 of BM) +15% Y/Y collectively (from +30% in Mar-Q), partially offset by a deceleration in consumer IoT. GM of 44.9% (-220bps Y/Y) landed essentially in line with Street (45.0%) as input cost pressures persist.

\- Slightly sub-seasonal Sep-Q guide fell modestly short of expectations. Sep-Q revenue guidance of \$1,035M (at midpt) implies \~11% Q/Q growth - a touch leaner than typical low-teens%. Mobile is forecast up high-teens% Q/Q on

Neutral

![](images/776d7981d5619d7371c9b5e4d1780d35421a59aaf42d8a145d2448d3a9cad3a4.jpg)

SWKS, SWKS US

▼Price Target (Dec-27):\$65.00
Prior (Dec-26):\$70.00

Semiconductors & Semiconductor Capital Equipment / IT Hardware

Mayur Ramdhani AC
(1-212) 622-1664
mayur.ramdhani@JPM.com

Harlan Sur
(1-415) 315-6700
harlan.sur@JPM.com

Apoorva Kumar
(1-212) 270-0668
apoorva.kumar@JPM.com
JPM Securities LLC

Quarterly Forecasts (FYE Sep)
Adj. EPS (\$)

<table><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>1.60</td><td>1.54A</td><td>1.36</td></tr><tr><td>Q2</td><td>1.24</td><td>1.15A</td><td>1.05</td></tr><tr><td>Q3</td><td>1.33</td><td>1.08A</td><td>1.02</td></tr><tr><td>Q4</td><td>1.76</td><td>1.28</td><td>1.37</td></tr><tr><td>FY</td><td>5.93</td><td>5.05</td><td>4.80</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>17</td><td>15</td><td>24</td><td>27</td><td>50</td></tr><tr><td>Growth</td><td>84</td><td>82</td><td>82</td><td>64</td><td>68</td></tr><tr><td>Momentum</td><td>54</td><td>81</td><td>74</td><td>76</td><td>60</td></tr><tr><td>Quality</td><td>34</td><td>28</td><td>15</td><td>25</td><td>5</td></tr><tr><td>Low Vol</td><td>28</td><td>43</td><td>49</td><td>27</td><td>42</td></tr><tr><td>ESGQ</td><td>35</td><td>71</td><td>81</td><td>89</td><td>19</td></tr></table>

Price Performance  
![](images/878d8f6bded3b4c487023abb16342d04e80867abdbb4ff1c43c717f55b0cd2de.jpg)

— SWKS Price (\$) — S&P500 (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>2.0%</td><td>-4.9%</td><td>6.1%</td><td>-9.3%</td></tr><tr><td>Rel</td><td>-6.5%</td><td>-5.9%</td><td>2.0%</td><td>-25.6%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>150</td></tr><tr><td>52-week range ($)</td><td>90.90-51.93</td></tr><tr><td>Market cap ($ mn)</td><td>9,721.40</td></tr><tr><td>Exchange rate</td><td>1.00</td></tr><tr><td>Free float (%)</td><td>99.6%</td></tr><tr><td>3M ADV (mn)</td><td>5.34</td></tr><tr><td>3M ADV ($ mn)</td><td>367.3</td></tr><tr><td>Volatility (90 Day)</td><td>59</td></tr><tr><td>Index</td><td>S&amp;P 500</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>3|18|3</td></tr></table>

Key Metrics (FYE Sep)

<table><tr><td>$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>4,087</td><td>3,952</td><td>4,172</td><td>4,392</td></tr><tr><td>Adj. EBIT</td><td>949</td><td>835</td><td>847</td><td>896</td></tr><tr><td>Adj. EBITDA</td><td>1,213</td><td>648</td><td>693</td><td>742</td></tr><tr><td>Adj. net income</td><td>919</td><td>762</td><td>732</td><td>776</td></tr><tr><td>Adj. EPS</td><td>5.93</td><td>5.05</td><td>4.80</td><td>5.06</td></tr><tr><td>BBG EPS</td><td>5.60</td><td>4.99</td><td>5.15</td><td>6.58</td></tr><tr><td>Cashflow from operations</td><td>1,301</td><td>589</td><td>859</td><td>959</td></tr><tr><td>FCFF</td><td>1,106</td><td>314</td><td>651</td><td>739</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>(2.2%)</td><td>(3.3%)</td><td>5.6%</td><td>5.3%</td></tr><tr><td>EBIT margin</td><td>23.2%</td><td>21.1%</td><td>20.3%</td><td>20.4%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>(15.9%)</td><td>(12.0%)</td><td>1.4%</td><td>5.8%</td></tr><tr><td>EBITDA margin</td><td>29.7%</td><td>16.4%</td><td>16.6%</td><td>16.9%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>(15.7%)</td><td>(46.6%)</td><td>7.0%</td><td>7.2%</td></tr><tr><td>Net margin</td><td>22.5%</td><td>19.3%</td><td>17.6%</td><td>17.7%</td></tr><tr><td>Adj. EPS growth</td><td>(5.7%)</td><td>(14.9%)</td><td>(4.8%)</td><td>5.5%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>10.6%</td><td>8.8%</td><td>8.4%</td><td>8.5%</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>15.2%</td><td>13.2%</td><td>11.9%</td><td>11.4%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>11.0%</td><td>3.2%</td><td>6.6%</td><td>7.4%</td></tr><tr><td>Dividend yield</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EV/Revenue</td><td>2.0</td><td>2.3</td><td>2.1</td><td>1.9</td></tr><tr><td>EV/EBITDA</td><td>6.9</td><td>13.8</td><td>12.7</td><td>11.0</td></tr><tr><td>Adj. P/E</td><td>10.9</td><td>12.8</td><td>13.5</td><td>12.8</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

\- Skyworks Solutions is a market leader for RF semiconductors with \~70% exposure to mobile and \~30% exposure to non-mobile end markets.

\- Our Neutral thesis is based on the fact that despite Skyworks' strong financial performance, we believe the company's valuation is mostly range bound with a large amount of exposure to the mobile device market and with Apple as its largest customer ( $>50\%$ of revenues).

\- We see the potential for multiple expansion if the company inorganically (or organically over time) diversifies its revenue streams and/or increases its target shareholder returns in line with leading analog peers (of 100% of FCF).

## Valuation

Our Dec-27 PT of \$65 (from prior Dec-26 PT of \$70) is based on a \~12-13x multiple applied to our CY28 EPS estimate of \$5.08. The \~12-13x multiple is in-line with pure-play wireless semiconductor solutions peers.

Performance Drivers  
![](images/d0ba1f41f61eac9b6132cbb3f1b9ebe33e73d4a99fcfe72fe50358d63337a910.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI US</td><td>0.31</td><td>0.44</td></tr><tr><td>Sect: Technology</td><td>-0.03</td><td>-0.03</td></tr><tr><td>Ind: Semicond &amp; S Equip</td><td>-0.20</td><td>-0.15</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>US 10yr yield</td><td>0.06</td><td>0.14</td></tr><tr><td>US Dollar</td><td>-0.02</td><td>-0.10</td></tr><tr><td>US 10yr Breakeven</td><td>-0.20</td><td>-0.09</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>DivYld</td><td>0.41</td><td>0.37</td></tr><tr><td>Value</td><td>0.27</td><td>0.35</td></tr><tr><td>Quality</td><td>-0.30</td><td>-0.35</td></tr></table>

seasonal new-product ramps, with AAPL expected to grow well above the blended rate for Mobile, partially offset by Android. BM is projected up $\sim 5\%$ Y/Y ( $\sim$ flat Q/Q) with growth still supply-gated. GM guidance of $44.5\%$ steps down $\sim 40$ bps Q/Q on the seasonal mobile mix shift and persistent input-cost inflation.

\- Adjusting estimates and establishing Dec-27 PT of \$65. We establish a Dec-27 PT of \$65 (from prior Dec-26 PT of \$70), which is based on a \~12-13x multiple applied to our CY28 EPS estimate of \$5.08.

## SWKS F3Q26 (Jun-Q) Summary and F4Q26 (Sep-Q) Outlook

Table 1: SWKS F3Q26 (Jun-Q) Summary and F4Q26 (Sep-Q) Outlook

\$ in millions, %  
Table 2: SWKS Revenue by End-Market (F3Q26 vs. F2Q26) – Estimated

<table><tr><td rowspan="2"></td><td colspan="4">F3Q26 (Jun-Q)</td><td colspan="2">F4Q26E (Sep-Q)</td></tr><tr><td>Consensus</td><td>JPM Est</td><td>Actual</td><td>Delta</td><td>Consensus</td><td>Guidance</td></tr><tr><td>Revenue ($M)</td><td>$924.9</td><td>$925.0</td><td>$934.8</td><td>$9.8</td><td>$1,029.7</td><td>$1,035</td></tr><tr><td>Q/Q Change</td><td></td><td>-2.0%</td><td>-0.9%</td><td>1.0%</td><td></td><td></td></tr><tr><td>Gross Margin (NG)</td><td>45.0%</td><td>45.0%</td><td>44.9%</td><td>-0.1%</td><td>45.4%</td><td>44.5%</td></tr><tr><td>Op Margin (NG)</td><td></td><td>18.5%</td><td>19.4%</td><td>0.9%</td><td></td><td></td></tr><tr><td>Non-GAAP EPS</td><td>$1.03</td><td>$1.00</td><td>$1.08</td><td>$0.08</td><td>$1.29</td><td>$1.27</td></tr></table>

Source: Company reports, Bloomberg Finance L.P., and JPM estimates.

<table><tr><td rowspan="2"></td><td colspan="2">F3Q26 (Jun-Q)</td><td colspan="2">F2Q26 (Mar-Q)</td></tr><tr><td>Revenue</td><td>% of Total</td><td>Revenue</td><td>% of Total</td></tr><tr><td>Mobile</td><td>$532</td><td>57%</td><td>$537</td><td>57%</td></tr><tr><td>Broad Markets</td><td>$403</td><td>43%</td><td>$398</td><td>43%</td></tr><tr><td>TOTAL</td><td>$935</td><td>100%</td><td>$944</td><td>100%</td></tr></table>

Source: Company reports, JPM estimates. Note: Skyworks provides sales by end-market as a percentage of overall sales

## Balance Sheet and Cash Flow

Skyworks exited F3Q26 with \$814M of cash/cash equivalents. Cash flow from operations was \$70M in F3Q26, while capex was \$87M in the quarter. Skyworks generated -\$17M in FCF in F3Q26. Inventories rose to \$1.02B from \$0.89B in the prior quarter.

## Adjusting Forward Estimates

Our CY26 revenue / EPS estimates move to \$4.01B/\$4.87 from \$4.05B/\$5.15, and we now forecast CY27 and CY28 revenue / EPS of \$4.26B/\$4.95 and \$4.43B/\$5.08, respectively.

# Appendix I: Valuation and Comp Table

Table 3: Semiconductor Comp and Group Valuation Table  
\$ in millions

<table><tr><td rowspan="2"></td><td rowspan="2">JPM Rating</td><td rowspan="2">Market Cap</td><td rowspan="2">7/27/26 Price</td><td colspan="2">Non-GAAP EPS</td><td colspan="2">P/E</td><td colspan="2">Revenues</td><td colspan="2">P/S</td><td colspan="3">Consensus Non-GAAP EPS</td><td colspan="3">Consensus Revenues</td><td colspan="3">Consensus P/E</td><td colspan="3">Consensus P/S</td></tr><tr><td>C25</td><td>C26E</td><td>C25</td><td>C26E</td><td>C25</td><td>C26E</td><td>C25</td><td>C26E</td><td>C25</td><td>C26E</td><td>C27E</td><td>C25</td><td>C26E</td><td>C27E</td><td>C25</td><td>C26E</td><td>C27E</td><td>C25</td><td>C26E</td><td>C27E</td></tr><tr><td colspan="24">Harlan Sur, Lead Coverage phone: 415-315-6700, email: harlan.sur@jpmchase.com</td></tr><tr><td colspan="24">PC Semiconductors</td></tr><tr><td>INTC</td><td>UW</td><td>$467,884</td><td>$91.67</td><td>$0.43</td><td>$1.14</td><td>215.0x</td><td>80.4x</td><td>$52,853</td><td>$58,953</td><td>8.9x</td><td>7.9x</td><td>$0.43</td><td>$1.44</td><td>$1.95</td><td>$52,853</td><td>$62,959</td><td>$71,634</td><td>215.0x</td><td>63.5x</td><td>47.0x</td><td>8.9x</td><td>7.4x</td><td>6.5x</td></tr><tr><td>NVDA</td><td>OW</td><td>$4,793,075</td><td>$196.51</td><td>$4.77</td><td>$8.73</td><td>41.2x</td><td>22.5x</td><td>$215,938</td><td>$382,230</td><td>22.2x</td><td>12.5x</td><td>$4.77</td><td>$8.60</td><td>$12.56</td><td>$215,938</td><td>$380,828</td><td>$556,576</td><td>41.2x</td><td>22.8x</td><td>15.6x</td><td>22.2x</td><td>12.6x</td><td>8.6x</td></tr><tr><td>AMD</td><td>N</td><td>$816,668</td><td>$494.95</td><td>$4.18</td><td>$7.70</td><td>118.4x</td><td>64.3x</td><td>$34,639</td><td>$50,046</td><td>23.6x</td><td>16.3x</td><td>$4.18</td><td>$7.36</td><td>$13.58</td><td>$34,639</td><td>$49,991</td><td>$78,496</td><td>118.4x</td><td>67.3x</td><td>36.5x</td><td>23.6x</td><td>16.3x</td><td>10.4x</td></tr><tr><td colspan="24">Memory</td></tr><tr><td>MU</td><td>OW</td><td>$1,030,729</td><td>$900.20</td><td>$11.21</td><td>$103.46</td><td>80.3x</td><td>8.7x</td><td>$42,244</td><td>$172,887</td><td>24.4x</td><td>6.0x</td><td>$11.21</td><td>$112.71</td><td>$165.52</td><td>$42,244</td><td>$186,357</td><td>$264,833</td><td>80.3x</td><td>8.0x</td><td>5.4x</td><td>24.4x</td><td>5.5x</td><td>3.9x</td></tr><tr><td colspan="24">Enterprise/Networking/Datacenter Semiconductors</td></tr><tr><td>MRVL</td><td>OW</td><td>$168,986</td><td>$189.17</td><td>$2.85</td><td>$4.04</td><td>66.4x</td><td>46.8x</td><td>$8,195</td><td>$11,528</td><td>20.6x</td><td>14.7x</td><td>$2.85</td><td>$3.89</td><td>$6.04</td><td>$8,195</td><td>$11,102</td><td>$16,317</td><td>66.4x</td><td>48.7x</td><td>31.3x</td><td>20.6x</td><td>15.2x</td><td>10.4x</td></tr><tr><td>AVGO</td><td>OW</td><td>$1,868,581</td><td>$383.22</td><td>$7.28</td><td>$13.71</td><td>52.7x</td><td>28.0x</td><td>$68,282</td><td>$123,235</td><td>27.4x</td><td>15.2x</td><td>$7.28</td><td>$12.95</td><td>$20.50</td><td>$68,282</td><td>$116,695</td><td>$183,726</td><td>52.7x</td><td>29.6x</td><td>18.7x</td><td>27.4x</td><td>16.0x</td><td>10.2x</td></tr><tr><td>ALAB</td><td>OW</td><td>$43,960</td><td>$282.52</td><td>$1.84</td><td>$3.04</td><td>153.

[中间内容因长度限制已省略]

unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Disseminated 29 Jul 2026 12:17 AM EDT
"""
