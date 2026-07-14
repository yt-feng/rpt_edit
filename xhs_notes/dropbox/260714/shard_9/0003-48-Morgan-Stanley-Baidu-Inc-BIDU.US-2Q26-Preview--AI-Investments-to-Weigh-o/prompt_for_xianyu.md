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
Baidu Inc | Asia Pacific

# 2Q26 Preview: AI Investments to Weigh on Core OP

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Baidu Inc (BIDU.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>US$140.00</td><td>US$130.00</td></tr></table>

We expect core revenue to be down 4% in 2Q26, with strong AI cloud infra revenue (+56%) offsetting an 18.5% decline in ads. Non-core asset spin-off and first dividend by year-end remain key market focus areas. EW.

## Key Takeaways

2Q core revenue Rmb25.3bn, -4% YoY. Core non-GAAP OP Rmb3.7bn, -15% YoY.

2Q core ad revenue Rmb13bn, -18.5% YoY (vs. -21% in 1Q), limited visibility in turnaround.

AI cloud infra revenue Rmb7.6bn, +56% YoY, sustained by triple-digit GPU cloud growth.

Full-year 2026 core non-GAAP OP down $3 - 4\%$ with increasing AI investments in 2H.

AI cloud remains the bright spot: We expect 2Q AI cloud infra revenue to be Rmb7.6bn (+56% YoY), mainly driven by robust GPU cloud growth sustained in triple digits. Current major offerings are still IAAS-related; the Qianfan MaaS platform is seeing robust token usage ramp-up. With AI cloud rising in the mix, cloud margins are improving, in line with industry trend.

Ads still at trough: We expect 2Q online ads revenue of Rmb13bn, -18.5% YoY (vs. -21% in 1Q), affected by a weak macro climate and AI transformation. Baidu is ramping up agents and "digital humans" offerings, which contributed 18% of core ad revenue in 1Q. We expect this transformation to take time and see limited recovery in 2H26.

Increasing AI investments in 2H: We expect 2Q core OP of Rmb3.7bn, -15% YoY (margin 14.7%, -2.0ppt), mainly driven by a weak top line and increasing investments in AI, partially offsetting cost optimization from organizational restructuring. Baidu has recently hired Tianxiang Sun to head its Basic Model Unit (BMU), aiming to step up Ernie AI model capabilities. We estimate core non-GAAP OP at Rmb13.8bn, -3-4% YoY in full-year 2026.

Lower price target to US\$130; EW: We expect market focus to remain on non-core asset spin-off (ongoing process). Upcoming events include first dividend payout by year-end and dual primary listing potentially in 1Q27. We trimmed core revenue estimates 3% for 2026 and 2027 rto reflect weaker ads; our OP estimates drop 11-12% in view of rising AI investments. Our target implies 14x 2027e P/E vs. 13x now.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Gary Yu</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Gary.Yu@morganstanley.com</td><td>+852 2848-6918</td></tr><tr><td colspan="2">Joanne Lau</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Joanne.CY.Lau@morganstanley.com</td><td>+852 3963-1592</td></tr><tr><td colspan="2">Rebecca Xu</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Rebecca.Xu@morganstanley.com</td><td>+852 2848-7359</td></tr></table>

![](images/21cd743797e2086e0b7a8b927fa7ddeb6029544b569339149de17ed553c66348.jpg)  
Baidu Inc (BIDU.O, BIDU US)

China Internet and Other Services | China

<table><tr><td>Stock Rating</td><td>Equal-weight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>US$130.00</td></tr><tr><td>Up/downside to price target (%)</td><td>11</td></tr><tr><td>Shr price, close (Jul 10, 2026)</td><td>US$117.53</td></tr><tr><td>52-Week Range</td><td>US$165.30-84.64</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>343</td></tr><tr><td>Mkt cap, curr (mn)</td><td>US$40,254</td></tr><tr><td>EV, curr (mn)</td><td>US$5,116</td></tr><tr><td>Avg daily trading value (mn)</td><td>US$436</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>11.77</td><td>41.06</td><td>54.04</td><td>62.56</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>47.67</td><td>57.69</td><td>66.81</td></tr><tr><td>EPS (Rmb)§</td><td>51.68</td><td>53.56</td><td>59.55</td><td>72.96</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>129,079</td><td>129,884</td><td>145,335</td><td>158,948</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>5,589</td><td>14,063</td><td>18,509</td><td>21,427</td></tr><tr><td>P/E</td><td>56.0</td><td>19.4</td><td>14.7</td><td>12.7</td></tr><tr><td>ROE (%)</td><td>2.1</td><td>5.3</td><td>6.5</td><td>7.0</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework  
\*\* = Based on consensus methodology  
§ = Consensus data is provided by Refinitiv Estimates  
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Baidu Inc BIDU.O</td></tr><tr><td>Baidu core OP growth</td><td>↓ Likely downside surprise</td><td>↓ Modest revision lower</td></tr><tr><td colspan="3">• Increasing AI investments to weigh on core OP</td></tr><tr><td colspan="3">*Likely impact to consensus EPS is for the next 12 monthsSource: Company data, MS</td></tr></table>

## 2Q26 Results Preview

Exhibit 1: 2Q26 results preview

<table><tr><td>GAAP (Rmb mn)</td><td>2Q25</td><td>1Q26</td><td>2Q26E</td><td>YoY</td><td>Cons.</td><td>vs. Cons (%)</td></tr><tr><td>Baidu Core</td><td>26,251</td><td>26,001</td><td>25,274</td><td>-3.7%</td><td>26,551</td><td>-2.1%</td></tr><tr><td>- Core Marketing Revenue</td><td>16,200</td><td>12,600</td><td>13,203</td><td>-18.5%</td><td></td><td></td></tr><tr><td>- Non-marketing Revenue</td><td>10,051</td><td>13,401</td><td>12,071</td><td>20.1%</td><td></td><td></td></tr><tr><td>AI cloud infra</td><td>4,900</td><td>8,800</td><td>7,630</td><td>55.7%</td><td></td><td></td></tr><tr><td>iQIYI</td><td>6,628</td><td>6,226</td><td>6,346</td><td>-4.3%</td><td>6,434</td><td>-3.2%</td></tr><tr><td>Inter-Segment Revenue</td><td>(166)</td><td>(152)</td><td>(149)</td><td></td><td></td><td></td></tr><tr><td>Total Net Revenue</td><td>32,713</td><td>32,075</td><td>31,471</td><td>-3.8%</td><td>32,941</td><td>-2.6%</td></tr><tr><td>Cost of Revenue</td><td>18,357</td><td>19,589</td><td>18,092</td><td></td><td>19,602</td><td></td></tr><tr><td>Gross Profit</td><td>14,356</td><td>12,486</td><td>13,378</td><td>-6.8%</td><td>13,339</td><td>-6.4%</td></tr><tr><td>SG&amp;A</td><td>5,960</td><td>4,912</td><td>5,367</td><td></td><td>5,469</td><td></td></tr><tr><td>Research &amp; Development</td><td>5,119</td><td>4,381</td><td>4,934</td><td>-3.6%</td><td>4,988</td><td></td></tr><tr><td>Operating Profit</td><td>3,277</td><td>3,193</td><td>3,077</td><td></td><td>2,886</td><td></td></tr><tr><td>Net Income</td><td>7,259</td><td>3,291</td><td>3,092</td><td></td><td>3,602</td><td></td></tr><tr><td>Net Income Attributable to Baidu</td><td>7,322</td><td>3,445</td><td>3,097</td><td></td><td>3,674</td><td></td></tr><tr><td>Basic EPADS</td><td>20.9</td><td>9.4</td><td>9.1</td><td></td><td>10.7</td><td></td></tr><tr><td>Diluted EPADS</td><td>20.4</td><td>8.8</td><td>9.0</td><td></td><td>10.6</td><td></td></tr><tr><td colspan="7">Non-GAAP (Rmb mn)</td></tr><tr><td>Adjusted EBITDA</td><td>6,492</td><td>5,954</td><td>5,823</td><td></td><td>4,851</td><td>-24.7%</td></tr><tr><td>Baidu Core Operating Profit</td><td>4,385</td><td>3,950</td><td>3,715</td><td>-15.3%</td><td>3,666</td><td>7.7%</td></tr><tr><td>Operating Profit</td><td>4,445</td><td>3,807</td><td>3,711</td><td></td><td>3,823</td><td></td></tr><tr><td>Baidu Core Net income</td><td>4,792</td><td>4,433</td><td>3,656</td><td>-23.7%</td><td>4,455</td><td>-0.5%</td></tr><tr><td>Net Income Attributable to Baidu</td><td>4,795</td><td>4,332</td><td>3,645</td><td></td><td>4,556</td><td></td></tr><tr><td>Non-GAAP Diluted EPADS</td><td>13.6</td><td>12.1</td><td>10.5</td><td></td><td>13</td><td></td></tr><tr><td colspan="7">Margin (%)</td></tr><tr><td>Gross Margin</td><td>43.9%</td><td>38.9%</td><td>42.5%</td><td>-1.4ppt</td><td>40.5%</td><td>-1.6ppt</td></tr><tr><td>Baidu Core Non-GAAP Operating Margin</td><td>16.7%</td><td>15.2%</td><td>14.7%</td><td>-2.0ppt</td><td>13.8%</td><td>1.4ppt</td></tr><tr><td>Operating Margin</td><td>10.0%</td><td>10.0%</td><td>9.8%</td><td></td><td>8.8%</td><td>1.2ppt</td></tr><tr><td>Non-GAAP Operating Margin</td><td>13.6%</td><td>11.9%</td><td>11.8%</td><td></td><td>11.6%</td><td>0.3ppt</td></tr><tr><td>Baidu Core Non-GAAP Net margin</td><td>18.3%</td><td>17.0%</td><td>14.5%</td><td>-3.8ppt</td><td>16.8%</td><td>0.3ppt</td></tr><tr><td>Non-GAAP Net Margin Attributable to Baidu</td><td>14.7%</td><td>13.5%</td><td>11.6%</td><td></td><td>13.8%</td><td>-0.3ppt</td></tr></table>

Source: Company data, Visible Alpha consensus, MS estimates

## Estimate Changes

Exhibit 2: Baidu: What's Changed

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">Changes (%)</td></tr><tr><td>GAAP (Rmb mn)</td><td>Dec-26 2026E</td><td>Dec-27 2027E</td><td>Dec-28 2028E</td><td>Dec-26 2026E</td><td>Dec-27 2027E</td><td>Dec-28 2028E</td><td>Dec-26 2026E</td><td>Dec-27 2027E</td><td>Dec-28 2028E</td></tr><tr><td>Baidu Core</td><td>104,554</td><td>119,880</td><td>133,513</td><td>108,255</td><td>123,828</td><td>137,698</td><td>-3%</td><td>-3%</td><td>-3%</td></tr><tr><td>Core Marketing Revenue</td><td>51,019</td><td>52,550</td><td>54,126</td><td>53,210</td><td>54,806</td><td>56,450</td><td>-4%</td><td>-4%</td><td>-4%</td></tr><tr><td>Other Baidu Core</td><td>53,535</td><td>67,330</td><td>79,387</td><td>55,045</td><td>69,022</td><td>81,247</td><td>-3%</td><td>-2%</td><td>-2%</td></tr><tr><td>iQiyi</td><td>26,031</td><td>26,239</td><td>26,293</td><td>26,031</td><td>26,239</td><td>26,293</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Inter-Segment Revenue</td><td>(700)</td><td>(784)</td><td>(857)</td><td>(720)</td><td>(805)</td><td>(880)</td><td>-3%</td><td>-3%</td><td>-3%</td></tr><tr><td>Total Net Revenue</td><td>129,884</td><td>145,335</td><td>158,948</td><td>133,566</td><td>149,262</td><td>163,111</td><td>-3%</td><td>-3%</td><td>-3%</td></tr><tr><td>Cost of Revenue</td><td>75,092</td><td>81,576</td><td>86,969</td><td>77,077</td><td>83,659</td><td>89,140</td><td>-3%</td><td>-2%</td><td>-2%</td></tr><tr><td>Gross Profit</td><td>54,793</td><td>63,759</td><td>71,979</td><td>56,489</td><td>65,603</td><td>73,971</td><td>-3%</td><td>-3%</td><td>-3%</td></tr><tr><td>SG&amp;A</td><td>21,852</td><td>23,957</td><td>25,670</td><td>22,689</td><td>24,845</td><td>26,601</td><td>-4%</td><td>-4%</td><td>-3%</td></tr><tr><td>Research &amp; Development</td><td>21,702</td><td>24,829</td><td>27,651</td><td>21,300</td><td>24,322</td><td>27,052</td><td>2%</td><td>2%</td><td>2%</td></tr><tr><td>Operating Profit</td><td>11,239</td><td>14,973</td><td>18,658</td><td>12,500</td><td>16,436</td><td>20,318</td><td>-10%</td><td>-9%</td><td>-8%</td></tr><tr><td>Interest Income</td><td>8,507</td><td>8,694</td><td>9,261</td><td>8,507</td><td>8,757</td><td>9,376</td><td>0%</td><td>-1%</td><td>-1%</td></tr><tr><td>Interest Expense</td><td>(3,001)</td><td>(2,923)</td><td>(2,799)</td><td>(3,001)</td><td>(2,923)</td><td>(2,799)</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Profit Before Tax</td><td>17,285</td><td>24,061</td><td>28,436</td><td>20,045</td><td>25,585</td><td>30,211</td><td>-14%</td><td>-6%</td><td>-6%</td></tr><tr><td>Tax Expenses</td><td>(2,540)</td><td>(3,745)</td><td>(4,522)</td><td>(3,037)</td><td>(4,020)</td><td>(4,842)</td><td>-16%</td><td>-7%</td><td>-7%</td></tr><tr><td>Net Income</td><td>14,745</td><td>20,316</td><td>23,914</td><td>17,008</td><td>21,566</td><td>25,369</td><td>-13%</td><td>-6%</td><td>-6%</td></tr><tr><td>Less Net Loss Attributable to NCI</td><td>682</td><td>1,807</td><td>2,487</td><td>682</td><td>1,807</td><td>2,487</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Net Income Attributable to Baidu</td><td>14,063</td><td>18,509</td><td>21,427</td><td>16,326</td><td>19,759</td><td>22,882</td><td>-14%</td><td>-6%</td><td>-6%</td></tr><tr><td colspan="10">EPADS (Rmb)</td></tr><tr><td>Basic</td><td>41.3</td><td>54.4</td><td>63.0</td><td>48.0</td><td>58.1</td><td>67.3</td><td>-14%</td><td>-6%</td><td>-6%</td></tr><tr><td>Diluted</td><td>41.1</td><td>54.0</td><td>62.6</td><td>47.7</td><td>57.7</td><td>66.8</td><td>-14%</td><td>-6%</td><td>-6%</td></tr><tr><td colspan="10">Non-GAAP</td></tr><tr><td>Total Net Revenue</td><td>129,884</td><td>145,335</td><td>158,948</td><td>133,566</td><td>149,262</td><td>163,111</td><td>-3%</td><td>-3%</td><td>-3%</td></tr><tr><td>Gross Profit</td><td>55,183</td><td>64,197</td><td>72,455</td><td>56,956</td><td>66,128</td><td>74,543</td><td>-3%</td><td>-3%</td><td>-3%</td></tr><tr><td>EBITDA</td><td>23,021</td><td>30,933</td><td>37,709</td><td>25,036</td><td>33,368</td><td>40,526</td><td>-8%</td><td>-7%</td><td>-7%</td></tr><tr><td>Operating Profit</td><td>14,316</td><td>18,435</td><td>22,448</td><td>16,210</td><td>20,616</td><td>24,901</td><td>-12%</td><td>-11%</td><td>-10%</td></tr><tr><td>Net Income Attributable to Baidu</td><td>17,097</td><td>21,477</td><td>24,672</td><td>19,898</td><td>23,337</td><td>26,801</td><td>-14%</td><td>-8%</td><td>-8%</td></tr><tr><td colspan="10">EPADS (Rmb) - Attributable to Baidu</td></tr><tr><td>Non-GAAP Basic EPADS</td><td>43.4</td><td>54.1</td><td>62.1</td><td>50.5</td><td>59.0</td><td>67.6</td><td>-14%</td><td>-8%</td><td>-8%</td></tr><tr><td>Non-GAAP Diluted EPADS</td><td>41.3</td><td>51.9</td><td>59.9</td><td>48.4</td><td>56.8</td><td>65.4</td><td>-15%</td><td>-8%</td><td>-8%</td></tr><tr><td colspan="10">Baidu Core</td></tr><tr><td>Net Revenue</td><td>104,554</td><td>119,880</td><td>133,513</td><td>108,255</td><td>123,828</td><td>137,698</td><td>-3.4%</td><td>-3.2%</td><td>-3.0%</td></tr><tr><td>Non-GAAP Operating Profit</td><td>13,801</td><td>17,383</td><td>21,229</td><td>15,697</td><td>19,565</td><td>23,684</td><td>-12.1%</td><td>-11.2%</td><td>-10.4%</td></tr><tr><td>Non-GAAP OPM</td><td>13.2%</td><td>14.5%</td><td>15.9%</td><td>14.5%</td><td>15.8%</td><td>17.2%</td><td>(1.3 ppt)</td><td>(1.3 ppt)</td><td>(1.3 ppt)</td></tr><tr><td colspan="10">iQIYI</td></tr><tr><td>Net Revenue</td><td>26,031</td><td>26,239</td><td>26,293</td><td>26,031</td><td>26,239</td><td>26,293</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Non-GAAP Operating Profit</td><td>546</td><td>1,109</td><td>1,301</td><td>546</td><td>1,109</td><td>1,301</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Non-GAAP OPM</td><td>2.1%</td><td>4.2%</td><td>4.9%</td><td>2.1%</td><td>4.2%</td><td>4.9%</td><td>-</td><td>-</td><td>-</td></tr></table>

Source: Company data, MS (E) estimates

## Valuation

Our price target is reduced to US\$130 (was US\$140).

Our price target is our base case scenario value, derived from a sum-of-the-parts approach, including US\$123 DCF value (was US\$133) for the core business and US\$7 (unchanged) for associate investments. Our key assumptions for the core business DCF model include an 11% discount rate and 3% terminal growth rate (unchanged). We also consider the implied market valuations of Baidu's key investments in Trip.com and IQIYI, and continue to apply a 30% holdco discount to investment value.

Exhibit 3: Baidu: DCF matrix: Unlevered free cash flow breakdown

<table><tr><t

[中间内容因长度限制已省略]

ll only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: China Internet and Other Services

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/10/2026)</td></tr><tr><td>Eddy Wang, CFA</td><td></td><td></td></tr><tr><td>Autohome Inc (ATHM.N)</td><td>E (02/09/2023)</td><td>US$20.30</td></tr><tr><td>Full Truck Alliance Co. Ltd (YMM.N)</td><td>O (07/05/2023)</td><td>US$8.57</td></tr><tr><td>JD.com, Inc. (JD.O)</td><td>U (11/10/2025)</td><td>US$28.20</td></tr><tr><td>Kanzhun Ltd (BZ.O)</td><td>O (08/04/2021)</td><td>US$13.76</td></tr><tr><td>KE Holdings Inc (BEKE.N)</td><td>O (03/16/2022)</td><td>US$15.57</td></tr><tr><td>PDD Holdings Inc (PDD.O)</td><td>O (03/02/2023)</td><td>US$85.13</td></tr><tr><td>Vipshop Holdings Ltd (VIPS.N)</td><td>E (02/24/2022)</td><td>US$13.94</td></tr><tr><td>Gary Yu</td><td></td><td></td></tr><tr><td>Alibaba Group Holding (BABA.N)</td><td>O (02/24/2025)</td><td>US$112.33</td></tr><tr><td>Baidu Inc (BIDU.O)</td><td>E (05/17/2024)</td><td>US$117.53</td></tr><tr><td>Meituan (3690.HK)</td><td>O (08/29/2024)</td><td>HK$77.95</td></tr><tr><td>Tencent Holdings Ltd. (0700.HK)</td><td>O (03/19/2020)</td><td>HK$457.60</td></tr><tr><td>Rebecca Xu</td><td></td><td></td></tr><tr><td>HUYA Inc (HUYA.N)</td><td>E (05/16/2024)</td><td>US$2.45</td></tr><tr><td>IQIYI Inc (IQ.O)</td><td>E (01/19/2023)</td><td>US$1.13</td></tr><tr><td>JOYY Inc. (JOYY.O)</td><td>E (06/02/2022)</td><td>US$70.54</td></tr><tr><td>Weibo Corp (WB.O)</td><td>U (05/17/2024)</td><td>US$7.72</td></tr><tr><td>Yang Liu</td><td></td><td></td></tr><tr><td>Bilibili Inc (BILI.O)</td><td>O (04/13/2026)</td><td>US$17.70</td></tr><tr><td>Kuaishou Technology (1024.HK)</td><td>O (05/26/2026)</td><td>HK$43.60</td></tr><tr><td>NetEase, Inc (NTES.O)</td><td>O (01/08/2025)</td><td>US$128.03</td></tr><tr><td>Tongcheng Travel Holdings (0780.HK)</td><td>O (01/04/2019)</td><td>HK$12.18</td></tr><tr><td>Trip.com Group Ltd (TCOM.O)</td><td>O (05/17/2021)</td><td>US$42.80</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
