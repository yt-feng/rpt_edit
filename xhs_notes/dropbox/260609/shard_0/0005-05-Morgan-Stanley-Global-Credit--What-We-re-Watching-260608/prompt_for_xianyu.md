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
## GLOBAL CREDIT STRATEGY

## Global Credit: What We're Watching

US Investment Grade: The pullback in equities also weighed on credit, with US IG spreads ending the week 1bp wider, resulting in excess returns of -0.1%. Spread curves bear-steepened while better rated bonds underperformed. Telecoms, technology, utilities delivered the weakest excess returns, while basic industry and services held up better. US IG funds saw \$3.6bn of net inflows last week, lifting YTD inflows to +\$69bn. Primary market activity was robust, with \$47bn of bonds pricing last week. YTD supply is tracking at \$1,095bn (+26% YoY).

US Leveraged Credit: HY spreads widened by 7bp, translating into excess returns of -0.1%. Loans delivered positive total returns at 0.05% last week, outperforming HY (-0.4%). The moves were accompanied by decompression across HY and Loans. Within HY, telecom and consumer goods underperformed, while energy and technology held in better. HY funds reported net inflows of \$880mn (-\$6.2bn YTD), while loan funds saw net inflows of \$760mn last week (+\$3.5bn YTD). Both HY and Loans recorded \$13bn of issuance last week. YTD issuance now stands at \$160bn (+42% YoY) in HY and \$188bn (-3% YoY) in loans.

EU Investment Grade: European credit outperformed the US last week with spreads tightening by 3bp, resulting in excess returns of +0.1%. Curves bull-flattened, while BBBs saw slight outperformance across ratings. Media outperformed, while transportation and basic industry lagged. European IG fund inflows rose to \~\$700m (0.1% of AUM) following last week's more muted but positive print (\~\$155m). The inflows were heavily skewed towards ETFs, while mutual funds reported small net outflows. Issuance moderated to €12bn last week, lifting YTD volumes to €378bn (flat YoY).

EU High Yield: EU HY outperformed IG, with spreads tightening by 13bp last week resulting in excess returns of +0.4%. However, the moves were most pronounced in BBs, while performance was more mixed further down the ratings spectrum. Leisure and tech outperformed, while telecoms and real estate lagged. European HY fund net inflows rose to \~\$425mln / 0.4% of AUM, with both mutual funds and ETFs saw net inflows. YTD supply is tracking at €67bn (+11% YoY).

Key Trades: We reiterate our key trade recommendations across sectors in IG that we outlined in our Mid-Year Outlooks. In the US, we are overweight banks, utilities, while technology/hyperscalers remain our key underweights. In Europe, we like banks, energy, and defensives, while we recommend an underweight on cyclical sectors, autos in particular. In Asia, we like Japan Banks TLAC Senior debt and unhedged AUD LC Corp bonds.

Credit Derivatives: Synthetic spreads widened across the US and EU, with CDX IG and iTraxx Main ending the week 2bp and 1bp wider, respectively, while HY/Xover underperformed. While implied volatility ticked up from the YTD lows, credit lagged the rise in equities vol.

Asia Credit: Asia Credit spreads tightened by 2bp over the last week, while APAC Credit spreads remained flat. In Asia credit, Asia HY (-18bp) outperformed Asia IG (-2bp). Similarly, in APAC credit, HY spreads tightened by 3bp while IG spreads were flat.

## List of Recent Publications:

European Credit Mid-Year Outlook: Glass Half Full

US Credit Strategy Mid-Year Outlook: Financing the Future

US Credit Playbook: Focus Back on Supply

Asia Credit Mid-Year Outlook: A "Low-Fire, Low-Hire" Credit Market

## MS Global

## MS & Co. LLC

## Vishwas Patkar

Strategist

Vishwas.Patkar@morganstanley.com

+1 212 761 8041

## MS & Co. International plc+

## Aron Becker

Strategist

Aron.Becker@morganstanley.com

+44 0(207) 677 0754

## MS Asia Limited+

## Kelvin Pang

Strategist

Kelvin.Pang@morganstanley.com

+852 2848 8204

## MS & Co. LLC

## Christina Sigler

Strategist

Christina.Sigler@morganstanley.com

+1 212.761.4116

Note: The EPFR data and charts displayed here must not be extracted and republished (whether internally or externally). Such use will violate the terms of MS's contract with EPFR which only covers named users.

## Table of Contents

Global Credit Snapshot 3

Performance Across Asset Classes 4

Global Credit Percentile Ranges 5

US Credit Long-Term Spreads and Yields 6

Europe and Asia Credit Long-Term Spreads 7

Macro Sentiment Indicators 8

Credit Sentiment Indicators 9

Key Trades Across Sectors in IG 10

## US and EU Credit

Yields, Dollar Prices, and Index Quality 20

Curve Performance 21

Global Credit Demand 22

Global Credit Supply 24

Debt Outstanding 25

Maturity Walls 26

Defaults and Rating Changes 27

Fundamentals 28

Credit Derivatives/DTCC Positioning 29

IG Best + Worst Performers 31

IG 5-10Y Carry and Roll Down 37

Performance across Capital Structure 39

Sector Performance 41

Credit/Equity Screen 43

## Asia Credit

Asia Credit Demand 48

Asia Credit Supply 49

Asia Maturity Wall and Default Rate 50

Asia Debt Outstanding 51

Global Credit Snapshot

<table><tr><td>Global IG Credit</td><td>Current</td><td>1 Wk Δ</td><td>3 Mth Δ</td><td>12 Mth Δ</td><td>1Y %Tile</td><td>1Y %Tile Range</td><td>5Y Tights</td><td>5Y Wides</td><td>5Y %Tile</td><td>5Y %Tile Range</td></tr><tr><td>US IG</td><td>73</td><td>1</td><td>(7)</td><td>(14)</td><td>38%</td><td>■</td><td>71</td><td>165</td><td>10%</td><td>■</td></tr><tr><td>EUR IG</td><td>77</td><td>(3)</td><td>(6)</td><td>(22)</td><td>48%</td><td>■</td><td>72</td><td>234</td><td>10%</td><td>■</td></tr><tr><td>Asia IG</td><td>53</td><td>(2)</td><td>(14)</td><td>(28)</td><td>0%</td><td>■</td><td>53</td><td>198</td><td>0%</td><td>■</td></tr><tr><td>CDX IG</td><td>52</td><td>2</td><td>(1)</td><td>(3)</td><td>60%</td><td>■</td><td>46</td><td>111</td><td>38%</td><td>■</td></tr><tr><td>iTraxx Main</td><td>54</td><td>1</td><td>(3)</td><td>(3)</td><td>68%</td><td>■</td><td>44</td><td>138</td><td>39%</td><td>■</td></tr><tr><td>EM IG</td><td>80</td><td>(2)</td><td>(13)</td><td>(27)</td><td>0%</td><td>■</td><td>80</td><td>159</td><td>0%</td><td>■</td></tr><tr><td>Agency MBS</td><td>25</td><td>3</td><td>4</td><td>(17)</td><td>46%</td><td>■</td><td>14</td><td>88</td><td>12%</td><td>■</td></tr><tr><td>CLO AAAs</td><td>123</td><td>0</td><td>(5)</td><td>(12)</td><td>0%</td><td>■</td><td>115</td><td>233</td><td>15%</td><td>■</td></tr><tr><td>RMBS AAAs</td><td>125</td><td>0</td><td>(5)</td><td>(20)</td><td>12%</td><td>■</td><td>60</td><td>280</td><td>20%</td><td>■</td></tr><tr><td>US As</td><td>62</td><td>1</td><td>(5)</td><td>(11)</td><td>44%</td><td>■</td><td>58</td><td>145</td><td>11%</td><td>■</td></tr><tr><td>US BBBs</td><td>90</td><td>1</td><td>(10)</td><td>(18)</td><td>31%</td><td>■</td><td>89</td><td>199</td><td>10%</td><td>■</td></tr><tr><td>US 3-5Y</td><td>64</td><td>1</td><td>(6)</td><td>(13)</td><td>31%</td><td>■</td><td>50</td><td>158</td><td>23%</td><td>■</td></tr><tr><td>US 5-7Y</td><td>72</td><td>2</td><td>(5)</td><td>(19)</td><td>17%</td><td>■</td><td>66</td><td>173</td><td>13%</td><td>■</td></tr><tr><td>US 7-10Y</td><td>86</td><td>1</td><td>(7)</td><td>(16)</td><td>35%</td><td>■</td><td>81</td><td>200</td><td>11%</td><td>■</td></tr><tr><td>US 10Y+</td><td>89</td><td>2</td><td>(11)</td><td>(15)</td><td>34%</td><td>■</td><td>87</td><td>203</td><td>7%</td><td>■</td></tr><tr><td>US Financials</td><td>76</td><td>1</td><td>(8)</td><td>(12)</td><td>55%</td><td>■</td><td>71</td><td>188</td><td>24%</td><td>■</td></tr><tr><td>US Industrials</td><td>70</td><td>1</td><td>(7)</td><td>(14)</td><td>29%</td><td>■</td><td>69</td><td>160</td><td>7%</td><td>■</td></tr><tr><td>US Utilities</td><td>78</td><td>1</td><td>(8)</td><td>(18)</td><td>16%</td><td>■</td><td>77</td><td>161</td><td>6%</td><td>■</td></tr><tr><td>EUR As</td><td>69</td><td>(2)</td><td>(6)</td><td>(19)</td><td>49%</td><td>■</td><td>65</td><td>200</td><td>16%</td><td>■</td></tr><tr><td>EUR BBBs</td><td>89</td><td>(3)</td><td>(5)</td><td>(25)</td><td>50%</td><td>■</td><td>83</td><td>273</td><td>10%</td><td>■</td></tr><tr><td>EUR 3-5Y</td><td>77</td><td>(2)</td><td>(5)</td><td>(24)</td><td>47%</td><td>■</td><td>71</td><td>245</td><td>12%</td><td>■</td></tr><tr><td>EUR 5-7Y</td><td>90</td><td>(2)</td><td>(7)</td><td>(22)</td><td>43%</td><td>■</td><td>85</td><td>251</td><td>15%</td><td>■</td></tr><tr><td>EUR 7-10Y</td><td>95</td><td>(2)</td><td>(7)</td><td>(21)</td><td>39%</td><td>■</td><td>91</td><td>247</td><td>8%</td><td>■</td></tr><tr><td>EUR 10Y+</td><td>90</td><td>(3)</td><td>(8)</td><td>(18)</td><td>45%</td><td>■</td><td>88</td><td>234</td><td>9%</td><td>■</td></tr></table>

<table><tr><td>Global HY Credit</td><td>Current</td><td>1 Wk Δ</td><td>3 Mth Δ</td><td>12 Mth Δ</td><td>1Y %Tile</td><td>1Y %Tile Range</td><td>5Y Tights</td><td>5Y Wides</td><td>5Y %Tile</td><td>5Y %Tile Range</td></tr><tr><td>US HY</td><td>265</td><td>7</td><td>(16)</td><td>(47)</td><td>16%</td><td>■</td><td>250</td><td>583</td><td>7%</td><td>■</td></tr><tr><td>EUR HY</td><td>250</td><td>(13)</td><td>(40)</td><td>(59)</td><td>39%</td><td>■</td><td>247</td><td>668</td><td>8%</td><td>■</td></tr><tr><td>CDX HY</td><td>312</td><td>12</td><td>(14)</td><td>(33)</td><td>53%</td><td>■</td><td>269</td><td>627</td><td>31%</td><td>■</td></tr><tr><td>Xover</td><td>263</td><td>4</td><td>(2)</td><td>(31)</td><td>63%</td><td>■</td><td>225</td><td>662</td><td>23%</td><td>■</td></tr><tr><td>US BBs</td><td>157</td><td>4</td><td>(10)</td><td>(27)</td><td>20%</td><td>■</td><td>149</td><td>413</td><td>8%</td><td>■</td></tr><tr><td>US Bs</td><td>282</td><td>9</td><td>(25)</td><td>(17)</td><td>51%</td><td>■</td><td>236</td><td>653</td><td>27%</td><td>■</td></tr><tr><td>US CCCs</td><td>724</td><td>18</td><td>96</td><td>13</td><td>82%</td><td>■</td><td>444</td><td>1,133</td><td>45%</td><td>■</td></tr><tr><td>EUR HY BBs</td><td>149</td><td>(13)</td><td>(27)</td><td>(57)</td><td>26%</td><td>■</td><td>149</td><td>526</td><td>6%</td><td>■</td></tr><tr><td>EUR HY Bs</td><td>321</td><td>(19)</td><td>(71)</td><td>(9)</td><td>71%</td><td>■</td><td>279</td><td>837</td><td>21%</td><td>■</td></tr><tr><td>EUR HY CCCs</td><td>1,099</td><td>14</td><td>72</td><td>(4)</td><td>40%</td><td>■</td><td>556</td><td>1,549</td><td>43%</td><td>■</td></tr></table>

<table><tr><td>Asia Credit</td><td>Current</td><td>1 Wk Δ</td><td>3 Mth Δ</td><td>12 Mth Δ</td><td>1Y %Tile</td><td>1Y %Tile Range</td><td>5Y Tights</td><td>5Y Wides</td><td>5Y %Tile</td><td>5Y %Tile Range</td></tr><tr><td>iTraxx Japan</td><td>60</td><td>(1)</td><td>(2)</td><td>(2)</td><td>69%</td><td>■</td><td>42</td><td>117</td><td>55%</td><td>■</td></tr><tr><td>iTraxx Australia</td><td>72</td><td>(0)</td><td>(2)</td><td>(3)</td><td>70%</td><td>■</td><td>56</td><td>152</td><td>47%</td><td>■</td></tr><tr><td>Asia Credit</td><td>93</td><td>(3)</td><td>(14)</td><td>(41)</td><td>13%</td><td>■</td><td>93</td><td>407</td><td>3%</td><td>■</td></tr><tr><td>Asia IG</td><td>53</td><td>(2)</td><td>(14)</td><td>(28)</td><td>0%</td><td>■</td><td>53</td><td>198</td><td>0%</td><td>■</td></tr><tr><td>Asia HY</td><td>326</td><td>(16)</td><td>(23)</td><td>(124)</td><td>55%</td><td>■</td><td>309</td><td>1,536</td><td>11%</td><td>■</td></tr><tr><td>China IG</td><td>39</td><td>(3)</td><td>(17)</td><td>(35)</td><td>0%</td><td>■</td><td>39</td><td>226</td><td>0%</td><td>■</td></tr><tr><td>China HY</td><td>498</td><td>(18)</td><td>7</td><td>(64)</td><td>86%</td><td>■</td><td>345</td><td>2,570</td><td>33%</td><td>■</td></tr></table>

![](images/91770c2e3e6fddd8a00ba879083952e582f1e98ad420c4ac8ff33f2186575b0c.jpg)

<details>
<summary>bar chart</summary>

YTD Global Credit Returns
| Category | Total Return (%) | Excess Return (%) |
| :--- | :--- | :--- |
| US IG | 0.1 | 0.8 |
| US AAs | -0.3 | 0.4 |
| US As | -0.1 | 0.6 |
| US BBBs | 0.3 | 1.0 |
| EU IG | 0.5 | 0.6 |
| EU AAs | 0.3 | 0.5 |
| EU As | 0.4 | 0.6 |
| EU BBBs | 0.5 | 0.7 |
| Asia IG | 0.2 | 0.6 |
| US HY | 1.3 | 1.2 |
| US BBs | 1.3 | 1.3 |
| US Bs | 1.5 | 1.3 |
| US CCCs | 1.3 | 1.1 |
| EU HY | 1.3 | 1.3 |
| EU BBs | 1.3 | 1.3 |
| EU Bs | 1.2 | 1.1 |
| EU CCCs | 2.1 | 2.2 |
| US Loans | 1.3 | |
| EU Loans | 1.6 | |
The chart displays a single bar for each category, with the total return percentage labeled above the bars and excess return percentage below it.
</details>

![](images/18ae72366546b278dc5c8773b2bdae20a8b08366d88e9798d35036de34ef2f50.jpg)

<details>
<summary>bar chart</summary>

YTD Asset Class Returns
| Asset Class | Total Return (%) | Excess Return (%) |
| :--- | :--- | :--- |
| Treasuries | -0.5 | -1.0 |
| Aggregate | -0.2 | 0.3 |
| Agency | 0.1 | 0.6 |
| MBS | 0.1 | 0.3 |
| US IG | 0.8 | 0.1 |
| Asia IG | 0.2 | 0.6 |
| EUR IG | 0.5 | 0.6 |
| ABS | 0.6 | 0.4 |
| US HY | 1.3 | 1.2 |
| EUR HY | 1.3 | 1.3 |
| US Loans | 1.3 | 0 |
| EU Loans | 1.6 | 0 |
| S&P 500 | 8.4 | 0 |
</details>

Performance Across Asset Classes

<table><tr><td colspan="2">Market</td><td>Ccy</td><td>Latest</td><td>1Y</td><td>1 Mth Δ</td><td>3 Mth Δ</td><td>2026 Δ</td></tr><tr><td colspan="2">EQUITIES</td><td colspan="3">Level</td><td colspan="3">Total Returns (%)</td></tr><tr><td rowspan="5">US</td><td>S&amp;P 500</td><td>USD</td><td>7,384</td><td></td><td>1.9</td><td>8.4</td><td>8.4</td></tr><tr><td>Russell 2000</td><td>USD</td><td>2,834</td><td></td><td>(0.3)</td><td>10.0</td><td>14.8</td></tr><tr><td>DJIA</td><td>USD</td><td>50,867</td><td></td><td>3.5</td><td>6.5</td><td>6.6</td></tr><tr><td>NASDAQ</td><td>USD</td><td>25,709</td><td></td><td>1.6</td><td>13.2</td><td>10.9</td></tr><tr><td>MSCI EAFE</td><td>USD</td><td>3,074</td><td></td><td>2.1</td><td>4.7</td><td>8.3</td></tr><tr><td>Europe</td><td>MSCI EUROPE</td><td>EUR</td><td>208</td><td></td><td>3.1</td><td>5.0</td><td>7.6</td></tr><tr><td rowspan="5">Asia</td><td>TOPIX</td><td>JPY</td><td>3,952</td><td></td><td>5.9</td><td>7.8</td><td>17.1</td></tr><tr><td>HSI</td><td>HKD</td><td>24,962</td><td></td><td>(2.9)</td><td>(0.2)</td><td>(1.4)</td></tr><tr><td>CSI 300</td><td>CNY</td><td>4,817</td><td></td><td>0.4</td><td>4.0</td><td>4.6</td></tr><tr><td>KOSPI</td><td>KRW</td><td>8,161</td><td></td><td>17.7</td><td>46.8</td><td>94.8</td></tr><tr><td>Nifty</td><td>INR</td><td>23,367</td><td></td><td>(2.5)</td><td>(5.4)</td><td>(10.1)</td></tr><tr><td>EM</td><td>MSCI EM</td><td>USD</td><td>1,717</td><td></td><td>4.4</td><td>15.0</td><td>23.3</td></tr></table>

<table><tr><td colspan="2">RATES</td><td colspan="3">Yield (%)</td><td colspan="3">Yield Change (bp)</td></tr><tr><td>US</td><td>US 2 Year</td><td>USD</td><td>4.15</td><td>■</td><td>14</td><td>35</td><td>67</td></tr><tr><td></td><td>US 5 Year</td><td>USD</td><td>4.27</td><td>■</td><td>13</td><td>32</td><td>54</td></tr><tr><td></td><td>US 10 Year</td><td>USD</td><td>4.53</td><td>■</td><td>9</td><td>21</td><td>36</td></tr><tr><td></td><td>US 30 Year</td><td>USD</td><td>5.00</td><td>■</td><td>2</td><td>9</td><td>15</td></tr><tr><td>Europe</td><td>Bund 2Y</td><td>EUR</td><td>2.69</td><td>■</td><td>16</td><td>8</td><td>57</td></tr><tr><td></td><td>Bund 5Y</td><td>EUR</td><td>2.77</td><td>■</td><td>13</td><td>4</td><td>32</td></tr><tr><td></td><td>Bund 10Y</td><td>EUR</td><td>3.04</td><td>■</td><td>10</td><td>3</td><td>18</td></tr><tr><td></td><td>Bund 30Y</td><td>EUR</td><td>3.57</td><td>■</td><td>7</td><td>11</td><td>9</td></tr><tr><td>Japan</td><td>Japan 5Y</td><td>JPY</td><td>1.93</td><td>■</td><td>2</td><td>14</td><td>37</td></tr><tr><td></td><td>Japan 10Y</td><td>JPY</td><td>2.67</td><td>■</td><td>1</td><td>32</td><td>61</td></tr><tr><td>China</td><td>China 5Y</td><td>CNY</td><td>1.41</td><td>■</td><td>0</td><td>(11)</td><td>(20)</td></tr><tr><td></td><td>China 10Y</td><td>CNY</td><td>1.72</td><td>■</td><td>1</td><td>(10)</td><td>(13)</td></tr><tr><td>India</td><td>India 5Y</td><td>INR</td><td>6.65</td><td>■</td><td>(18)</td><td>(10)</td><td>34</td></tr><tr><td></td><td>India 10Y</td><td>INR</td><td>6.

[中间内容因长度限制已省略]

nsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. dr0806

## The Americas

1585 Broadway

New York, NY 10036-8293

United States

+1 212 761 4000

## Europe

20 Bank Street, Canary Wharf

London E14 4AD

United Kingdom

+44 (0)20 7425 8000

## Japan

1-9-7 Otemachi, Chiyoda-ku

Tokyo 100-8104

Japan

+81 (0) 3 6836 5000

## Asia/Pacific

1 Austin Road West

Kowloon

Hong Kong

+852 2848 5200
"""
